import copy
import importlib.util
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TutorialContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'site/tutorial.json').read_text())

    def test_course_has_main_path_and_six_questions(self):
        self.assertEqual(self.data['version'], 1)
        self.assertEqual(len(self.data['questions']), 6)
        self.assertEqual(
            [q['id'] for q in self.data['questions']],
            ['content', 'substrate', 'scope', 'lifecycle', 'exposure', 'governance'],
        )
        for question in self.data['questions']:
            for field in ('title', 'what', 'why', 'how', 'example', 'evidence'):
                self.assertTrue(question[field], (question['id'], field))

    def test_supporting_lessons_reject_broken_sources_and_incomplete_steps(self):
        spec = importlib.util.spec_from_file_location('build_site', ROOT / 'scripts/build_site.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        builder.validate_tutorial(self.data)
        broken = copy.deepcopy(self.data)
        broken['concepts'][0]['sources'] = ['nonexistent-source']
        with self.assertRaisesRegex(ValueError, 'concept'):
            builder.validate_tutorial(broken)
        broken = copy.deepcopy(self.data)
        broken['topics'][0]['sections'][0]['sources'] = ['nonexistent-source']
        with self.assertRaisesRegex(ValueError, 'topic'):
            builder.validate_tutorial(broken)
        broken = copy.deepcopy(self.data)
        del broken['topics'][0]['sections'][0]['check']
        with self.assertRaisesRegex(ValueError, 'topic'):
            builder.validate_tutorial(broken)

    def test_curated_lists_have_expected_scale(self):
        self.assertGreaterEqual(len(self.data['entries']['research']), 10)
        self.assertLessEqual(sum(e.get('researchKind') == 'survey' for e in self.data['entries']['research']), 2)
        self.assertGreaterEqual(len(self.data['entries']['engineering']), 10)
        self.assertGreaterEqual(len(self.data['entries']['benchmarks']), 8)
        self.assertGreaterEqual(len(self.data['entries']['culture']), 4)

    def test_research_candidates_are_explicit_and_not_in_selected_workset(self):
        selected = {e['id'] for e in self.data['entries']['research']}
        candidates = self.data.get('researchCandidates', [])
        self.assertGreaterEqual(len(candidates), 1)
        for entry in candidates:
            self.assertNotIn(entry['id'], selected)
            self.assertEqual(entry.get('status'), 'complete')
            self.assertEqual(len(entry.get('questions', [])), 6)
            for answer in entry['questions']:
                for field in ('answer', 'why', 'example', 'trace'):
                    self.assertTrue(answer.get(field), (entry['id'], field))
            self.assertTrue(entry.get('boundary'))
            self.assertTrue(entry.get('checkedAt'))
            self.assertTrue(set(entry.get('sources', [])) <= set(self.data['sources']))

    def test_publication_order_uses_full_known_date_and_places_unknown_last(self):
        script = r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const ctx=vm.createContext({tutorial:{entries:{research:[
{id:'older',date:'v1 2026-02-22; v2 2026-05-20',title:'A'},
{id:'newer',date:'2026-03-08',title:'Z'},
{id:'year-only',date:'2026',title:'B'},
{id:'unknown',date:'not_specified',title:'C'}]}}});
vm.runInContext(fs.readFileSync('site/tutorial.js','utf8'),ctx);
assert.equal(ctx.tutorialSortedEntries('research').map(x=>x.id).join(','),'newer,older,year-only,unknown');
ctx.tutorial.researchCandidates=ctx.tutorial.entries.research;
ctx.tutorialEntryCard=(_,entry)=>'['+entry.id+']';
assert(ctx.tutorialResearchCandidates().includes('[newer][older][year-only][unknown]'));
'''
        subprocess.run(['node', '-e', script], cwd=ROOT, check=True, capture_output=True, text=True)

    def test_extension_details_and_comparison_use_the_same_entries(self):
        # Exercise real renderer functions so extension links cannot lead to empty pages.
        script = r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const tutorial=JSON.parse(fs.readFileSync('site/tutorial.json','utf8'));
const ctx=vm.createContext({tutorial,esc:String,crumbs:()=>'',state:{tutorialCompare:[]},tutorialComparisonCategories:tutorial.comparisonCategories});
vm.runInContext(fs.readFileSync('site/tutorial.js','utf8'),ctx);
for (const entry of tutorial.researchCandidates) {
  assert.equal(ctx.tutorialEntryBy('research',entry.id).id,entry.id);
  assert(ctx.tutorialReadings('research').some(e=>e.id===entry.id));
  assert(ctx.tutorialCompare().includes('data-tutorial-compare="'+entry.id+'"'));
}
assert.equal(ctx.tutorialCounts().research.total,tutorial.entries.research.length);
assert.equal(ctx.tutorialEntryBy('research','nonexistent'),null);
'''
        subprocess.run(['node', '-e', script], cwd=ROOT, check=True, capture_output=True, text=True)

    def test_each_category_has_complete_sample_and_all_entries_are_named(self):
        for category in ('research', 'engineering', 'benchmarks'):
            entries = self.data['entries'][category]
            self.assertGreaterEqual(sum(e['status'] == 'complete' for e in entries), 1, category)
            for entry in entries:
                for field in ('id', 'title', 'date', 'summary', 'why', 'boundary', 'status', 'sources'):
                    self.assertIn(field, entry, (category, entry.get('id'), field))
                self.assertIn(entry['status'], {'complete', 'pending'})
                self.assertIsInstance(entry['sources'], list)
                if entry['status'] == 'complete':
                    self.assertEqual(len(entry['questions']), 6)
                    self.assertTrue(entry.get('selectionEvidence'))
                    self.assertTrue(entry.get('limitations'))
                    self.assertTrue(entry.get('next'))
                    self.assertTrue(entry.get('profile', {}).get('kind'))
                    self.assertTrue(entry.get('profile', {}).get('artifact'))
                    for answer in entry['questions']:
                        self.assertTrue(answer['answer'])
                        self.assertTrue(answer['trace'])
                    if category == 'benchmarks':
                        evaluation = entry.get('evaluation', {})
                        for field in ('abilities', 'taskProtocol', 'metrics', 'designMapping', 'limitations'):
                            self.assertTrue(evaluation.get(field), (entry['id'], field))

    def test_sources_are_explicit_and_culture_items_are_real_or_pending(self):
        source_ids = set(self.data['sources'])
        for category, entries in self.data['entries'].items():
            for entry in entries:
                self.assertTrue(set(entry['sources']) <= source_ids, entry['id'])
                self.assertTrue(entry.get('checkedAt'), entry['id'])
        for entry in self.data.get('researchCandidates', []):
            self.assertTrue(set(entry['sources']) <= source_ids, entry['id'])
            self.assertTrue(entry.get('checkedAt'), entry['id'])
        for entry in self.data['entries']['culture']:
            self.assertIn(entry['status'], {'complete', 'pending'})
            self.assertTrue(entry.get('realityNote'))
            if entry['status'] == 'complete':
                self.assertTrue(entry.get('canonicalUrl'))
                self.assertEqual(len(entry.get('questions', [])), 6)

    def test_course_does_not_rank_systems(self):
        # Retrieval rerankers are mechanisms, not cross-system rankings.
        self.assertNotRegex(json.dumps(self.data).lower(), r'\b(?:rank|ranking|rankings|leaderboard)\b')

    def test_every_detail_comparison_button_has_a_visible_picker_entry(self):
        script = r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const tutorial=JSON.parse(fs.readFileSync('site/tutorial.json','utf8'));
const ctx=vm.createContext({tutorial,esc:String,crumbs:()=>'',state:{tutorialCompare:[]},tutorialComparisonCategories:tutorial.comparisonCategories});
vm.runInContext(fs.readFileSync('site/tutorial.js','utf8'),ctx);
const picker=ctx.tutorialCompare();
for (const category of Object.keys(tutorial.entries)) for (const entry of ctx.tutorialReadings(category)) {
  ctx.state.tutorialCategory=category;ctx.state.tutorialEntry=entry.id;
  const button=ctx.tutorialDetail().includes('data-tutorial-add-to-compare="'+category+':'+entry.id+'"');
  assert.equal(button,tutorial.comparisonCategories.includes(category),entry.id);
  if (button) assert(picker.includes('data-tutorial-compare="'+entry.id+'"'),entry.id);
}
'''
        subprocess.run(['node', '-e', script], cwd=ROOT, check=True, capture_output=True, text=True)

    def test_engineering_dates_are_explicit(self):
        for entry in self.data['entries']['engineering']:
            self.assertTrue(entry['date'])
            self.assertIsInstance(entry['date'], str)

    def test_engineering_publication_dates_are_not_snapshot_dates(self):
        for entry in self.data['entries']['engineering']:
            self.assertNotRegex(entry['date'], r'快照|核对', entry['id'])

    def test_engineering_identities_have_sources_without_duplicate_misnamings(self):
        entries = {entry['id']: entry for entry in self.data['entries']['engineering']}
        for entry in entries.values():
            self.assertTrue(entry.get('canonicalUrl'), entry['id'])
            self.assertTrue(entry['sources'], entry['id'])
        for mistaken_id in ('cloudmem', 'hisight'):
            self.assertNotIn(mistaken_id, entries)
        for entry_id, repository in (
            ('claude-mem', 'https://github.com/thedotmack/claude-mem'),
            ('hindsight', 'https://github.com/vectorize-io/hindsight'),
        ):
            self.assertEqual(entries[entry_id]['canonicalUrl'], repository)

    def test_third_batch_has_six_sourced_explanations(self):
        for category, entry_id in (
            ('research', 'generative-agents'),
            ('engineering', 'mem0'),
            ('benchmarks', 'locomo'),
        ):
            entry = next(e for e in self.data['entries'][category] if e['id'] == entry_id)
            self.assertEqual(entry['status'], 'complete')
            self.assertEqual(len(entry['questions']), 6)
            for answer in entry['questions']:
                for field in ('answer', 'why', 'example', 'trace'):
                    self.assertTrue(answer.get(field), (entry_id, field))

    def test_question_evidence_has_sources_and_culture_entries_have_provenance(self):
        source_ids = set(self.data['sources'])
        for question in self.data['questions']:
            self.assertTrue(question.get('confidence'))
            self.assertTrue(question.get('sources'))
            self.assertTrue(set(question['sources']) <= source_ids)
        for entry in self.data['entries']['culture']:
            self.assertTrue(entry.get('sources'))
            self.assertTrue(set(entry['sources']) <= source_ids)
            if entry['status'] == 'pending':
                self.assertTrue(entry.get('canonicalUrl'))

    def test_first_batch_answers_include_rationale_and_examples(self):
        expected = {
            'forms-functions-dynamics',
            'langgraph',
            'memoryagentbench',
        }
        entries = [
            entry
            for rows in self.data['entries'].values()
            for entry in rows
            if entry.get('id') in expected
        ]
        self.assertEqual({entry['id'] for entry in entries}, expected)
        for entry in entries:
            self.assertEqual(entry['status'], 'complete')
            self.assertEqual(len(entry['questions']), 6)
            for answer in entry['questions']:
                for field in ('answer', 'why', 'example', 'trace'):
                    self.assertTrue(answer.get(field), (entry['id'], field))

    def test_second_batch_answers_include_rationale_and_examples(self):
        expected = {
            'memgpt',
            'google-memory-bank',
            'collabmem',
        }
        entries = [
            entry
            for rows in self.data['entries'].values()
            for entry in rows
            if entry.get('id') in expected
        ]
        self.assertEqual({entry['id'] for entry in entries}, expected)
        for entry in entries:
            self.assertEqual(entry['status'], 'complete')
            self.assertEqual(len(entry['questions']), 6)
            for answer in entry['questions']:
                for field in ('answer', 'why', 'example', 'trace'):
                    self.assertTrue(answer.get(field), (entry['id'], field))


if __name__ == '__main__':
    unittest.main()
