import json
import importlib.util
import copy
import subprocess
import unittest
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('course_builder', ROOT / 'scripts/build_site.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class TextbookBehavior(unittest.TestCase):
    def node(self, script):
        result = subprocess.run(['node', '-e', script], cwd=ROOT,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr[-2500:])

    def test_public_page_only_loads_the_course(self):
        page = (ROOT / 'index.html').read_text()
        self.assertTrue('<iframe' not in page, 'The course must be a normal document')
        for retired in ('catalogue-data', 'knowledge-data', 'navigation-data',
                        'legacy-home', '先看几张图', '为什么这样回答', '这里不能推出'):
            self.assertTrue(retired not in page, 'Retired content is loaded: ' + retired)
        self.assertIn('id="tutorial-data"', page)

    def test_deep_links_anchors_empty_comparison_and_unknown_routes(self):
        self.node(r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const ctx=vm.createContext({URLSearchParams});
vm.runInContext(fs.readFileSync('site/routes.js','utf8'),ctx);
for(const section of ['lesson','concepts','research','engineering','benchmarks','culture','topics','compare']) {
  const s=ctx.routeState('#tutorial/'+section);
  assert.equal(s.view,'tutorial-'+section);
  assert.equal(ctx.routeState(ctx.routeHash(s)).view,s.view);
}
const d=ctx.routeState('#tutorial/detail/research/memgpt?section=exposure');
assert.equal(d.tutorialCategory,'research');
assert.equal(d.tutorialEntry,'memgpt');
assert.equal(d.section,'exposure');
assert.equal(ctx.routeHash(d),'#tutorial/detail/research/memgpt?section=exposure');
assert.equal(ctx.routeState('#tutorial/compare?ids=').tutorialCompare.length,0);
const selectionAfterChanging = ['claude-code','longmemeval'];
const restoredComparison = {...{tutorialCompare:selectionAfterChanging}, ...ctx.routeState('#tutorial/compare')};
assert.equal(restoredComparison.tutorialCompare.join(','),'coala,claude-code,longmemeval');
assert.equal(ctx.routeState('#tutorial/no-such-lesson').view,'not-found');
assert.equal(ctx.routeState('#library').view,'not-found');
assert.equal(ctx.routeState('#tutorial/detail/research').view,'not-found');
assert.doesNotThrow(()=>ctx.routeState('#tutorial/detail/research/%ZZ'));
''')

    def test_every_detail_has_full_questions_and_answers_before_explanations(self):
        self.node(r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const tutorial=JSON.parse(fs.readFileSync('site/tutorial.json','utf8'));
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const ctx=vm.createContext({tutorial,esc,crumbs:()=>'',state:{tutorialCompare:[]},tutorialComparisonCategories:tutorial.comparisonCategories});
vm.runInContext(fs.readFileSync('site/tutorial.js','utf8'),ctx);
for(const category of Object.keys(tutorial.entries)) for(const entry of ctx.tutorialReadings(category)) {
  ctx.state.tutorialCategory=category;ctx.state.tutorialEntry=entry.id;
  const html=ctx.tutorialDetail();
  for(let i=0;i<6;i++) {
    const question=esc(tutorial.questions[i].title);
    assert(html.includes(question),entry.id+' question '+i);
    const answer=entry.questions[i];
    const answerAt=html.indexOf(esc(answer.answer));
    const explanation=answer.sections ? '<h3>'+esc(answer.sections[0].title)+'</h3>' : esc(answer.why);
    assert(answerAt>=0 && html.indexOf(explanation)>answerAt,entry.id+' answer order '+i);
    if(answer.sections) for(const section of answer.sections) assert(html.includes('<h3>'+esc(section.title)+'</h3>'));
  }
  assert(!html.includes('为什么这样回答'));
  assert(!html.includes('<dt>状态</dt>'));
  assert(!html.includes('undefined'));
  assert(html.includes('href="#tutorial/'+entry.next+'"'),entry.id+' next lesson link');
  assert(!html.includes('<p>'+entry.next+'</p>'),entry.id+' must not expose an internal route as prose');
}
const sample=ctx.tutorialParagraphs('第一段。\n\n第二段含<script>。');
assert.equal((sample.match(/<p>/g)||[]).length,2);
assert(!sample.includes('<script>'));
assert(sample.includes('&lt;script&gt;'));
const detailed=ctx.tutorialBlocks([{type:'details',title:'More <script>',blocks:[
  {type:'p',text:'One <script>\n\nTwo'},
  {type:'table',caption:'Data',headers:['Name','Value'],rows:[['A','<img onerror=alert(1)>']]}
]}]);
assert(!detailed.includes('<script>'));
assert(!detailed.includes('<img onerror'));
assert(detailed.includes('&lt;img onerror=alert(1)&gt;'));
assert.equal((detailed.match(/<p>/g)||[]).length,2);
''')

    def test_lesson_blocks_reject_unknown_types_missing_assets_and_bad_sources(self):
        data = json.loads((ROOT / 'site/tutorial.json').read_text())
        def blocks(entry):
            for answer in entry['questions']:
                for section in answer.get('sections', []):
                    yield from section['blocks']
        original = next(e for e in data['entries']['research'] if e['id'] == 'a-mem')
        for failure in ('unknown-type', 'missing-file', 'unsafe-path', 'unknown-source'):
            broken = copy.deepcopy(original)
            figure = next(b for b in blocks(broken) if b['type'] == 'figure')
            if failure == 'unknown-type':
                figure['type'] = 'unrecognized'
            elif failure == 'missing-file':
                figure['src'] = 'site/figures/pilot/missing.svg'
            elif failure == 'unsafe-path':
                figure['src'] = '../private/image.svg'
            else:
                figure['sources'] = ['nonexistent-source']
            with self.subTest(failure=failure), self.assertRaises(ValueError):
                for block in blocks(broken):
                    builder.validate_blocks([block], data['sources'], 'sample')

    def test_embedded_data_cannot_terminate_its_script_element(self):
        value = {'example': '</script><script>alert(1)</script>\u2028 & 中文'}
        embedded = builder.script_json(value)
        self.assertNotIn('</script', embedded)
        self.assertEqual(json.loads(embedded), value)

    def test_course_figures_accept_both_collections_but_not_adjacent_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            block = {'type': 'figure', 'alt': 'A diagram', 'caption': 'A caption',
                     'credit': 'Original teaching diagram', 'sources': ['source'],
                     'width': 736, 'height': 400}
            for collection in ('pilot', 'lessons'):
                image = root / 'site/figures' / collection / 'example.svg'
                image.parent.mkdir(parents=True, exist_ok=True)
                image.write_text('<svg/>')
                builder.validate_blocks([{**block, 'src': image.relative_to(root).as_posix()}],
                                        {'source': {}}, 'example', root)
            for path in ('site/figures/lessons/../pilot/example.svg',
                         'site/figures/lessons/example.svg?other=1'):
                with self.assertRaises(ValueError):
                    builder.validate_blocks([{**block, 'src': path}], {'source': {}}, 'example', root)

    def test_sources_reject_active_urls_and_unregistered_citations(self):
        data = json.loads((ROOT / 'site/tutorial.json').read_text())
        for url in ('javascript:alert(1)', '//example.com', 'https://user:secret@example.com',
                    'https://example.com/line\nbreak'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                builder.validate_url(url, 'test-source')
        for field in ('question', 'affiliation'):
            bad = copy.deepcopy(data)
            entry = bad['entries']['research'][0]
            if field == 'question':
                entry['questions'][0]['sources'] = ['missing-source']
            else:
                entry['profile']['affiliation'] = 'Example Institution'
                entry['affiliationSources'] = ['missing-source']
            with self.subTest(field=field), self.assertRaises(ValueError):
                builder.validate_tutorial(bad)


if __name__ == '__main__':
    unittest.main()
