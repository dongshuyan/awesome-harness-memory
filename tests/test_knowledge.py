import importlib.util
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class KnowledgeContract(unittest.TestCase):
    def test_all_legacy_methods_remain_discoverable(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        methods = [m for t in data['topics'] for m in t['methods']] + data['draftTaxonomy']['items']
        covered = [old for m in methods for old in m.get('legacy', [])]
        expected = [f'{axis}:{i}' for axis, n in [('owner', 4), ('content', 7), ('scope', 5), ('form', 5), ('operation', 6), ('use', 5), ('governance', 4)] for i in range(n)]
        self.assertEqual(set(expected), set(covered))
        catalogue = {r['id'] for r in json.loads((ROOT / 'catalogue.json').read_text())['resources']}
        for item in methods:
            self.assertLessEqual(set(item['resources']), catalogue)
            for field in ['en', 'definition', 'what', 'when', 'purpose', 'example', 'boundary', 'sources']:
                self.assertTrue(item[field], (item['id'], field))
            self.assertLessEqual(set(item['sources']), set(data['sources']))

    def test_taxonomies_and_engineering_names_do_not_share_parent_edges(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        self.assertEqual(data['frameworks']['coala']['roots'], ['working', 'longterm'])
        self.assertEqual(data['frameworks']['coala']['children']['longterm'], ['episodic', 'semantic', 'procedural'])
        self.assertEqual(data['frameworks']['functional']['roots'], ['working', 'factual', 'experiential'])
        self.assertEqual(list(data['frameworks']), ['coala', 'functional', 'three-dimensional', 'engineering-terms'])
        self.assertEqual([data['frameworks'][key]['order'] for key in data['frameworks']], [1, 2, 3, 4])
        self.assertFalse(any('coala' in term or 'functions' in term for term in data['terms'].values()))
        self.assertEqual(len(data['topics']), 9)

    def test_build_includes_full_authoritative_catalogue_and_is_current(self):
        spec = importlib.util.spec_from_file_location('build_site', ROOT / 'scripts/build_site.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        outputs = builder.generated_files()
        self.assertEqual(outputs, {p: p.read_text() for p in outputs})
        self.assertEqual(outputs, builder.generated_files())
        parser = builder.harness.PageParser()
        parser.feed(outputs[ROOT / 'index.html'])
        embedded = re.search(r'<script type="application/json" id="catalogue-data">(.*?)</script>', parser.inner, re.S)
        self.assertEqual(json.loads(embedded.group(1)), json.loads((ROOT / 'catalogue.json').read_text()))

    def test_preserved_method_references_resolve_after_reclassification(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        navigation = json.loads((ROOT / 'site/navigation.json').read_text())
        methods = [m for t in data['topics'] for m in t['methods']] + data['draftTaxonomy']['items']
        for axis in navigation['legacyAxes']:
            for i, old in enumerate(axis['methods']):
                destinations = [m for m in methods if f'{axis["id"]}:{i}' in m.get('legacy', [])]
                self.assertTrue(destinations)
                self.assertLessEqual(set(old[4]), {rid for m in destinations for rid in m['resources']})
        topic_ids = {t['id'] for t in data['topics']}
        for targets in navigation['projectionTopics'].values():
            self.assertLessEqual(set(targets), topic_ids)

    def test_memory_taxonomy_updates_have_traceable_years_and_evidence(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        required_sources = {
            'microsoft-memory', 'aws-agent-memory', 'foundation-agent-taxonomy',
            'anatomy-agentic-memory', 'agent-memory-characterization',
            'graph-agent-memory', 'storage-experience'
        }
        self.assertTrue(required_sources <= set(data['sources']))
        for source_id in required_sources:
            source = data['sources'][source_id]
            self.assertRegex(str(source.get('year')), r'20\d{2}')
            self.assertTrue(source.get('evidence'))
            self.assertTrue(source['url'].startswith('https://'))
        self.assertGreaterEqual(len(data.get('updates', [])), 4)
        for update in data['updates']:
            self.assertTrue(update['title'] and update['en'] and update['year'])
            self.assertTrue(update['summary'] and update['relation'])
            self.assertLessEqual(set(update['sources']), set(data['sources']))

    def test_main_taxonomies_and_content_index_are_explicit(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        three = data['frameworks']['three-dimensional']
        self.assertEqual([d['id'] for d in three['dimensions']], ['substrate', 'cognitive', 'subject'])
        self.assertIn('accepted at TMLR with Survey Certification', three['status'])
        self.assertTrue({'foundation-agent-taxonomy-arxiv', 'foundation-agent-taxonomy'} <= set(three['sources']))
        index = data['contentIndex']
        self.assertEqual([g['id'] for g in index['groups']], ['primary', 'attributes'])
        self.assertEqual(len(index['groups'][0]['items']), 5)
        self.assertEqual(len(index['groups'][1]['items']), 2)
        self.assertEqual(set(index['mappings']), set(data['frameworks']))
        content_ids = set(index['groups'][0]['items'] + index['groups'][1]['items'])
        self.assertEqual(content_ids, {m['id'] for m in data['draftTaxonomy']['items']})
        self.assertEqual(next(t for t in data['topics'] if t['id'] == 'types')['methods'], [])
        for framework_id, rows in index['mappings'].items():
            category_ids = {c['id'] for c in data['frameworks'][framework_id].get('categories', [])}
            self.assertTrue(set(rows) <= content_ids)
            self.assertTrue(all(set(cell) <= category_ids for cell in rows.values()))

    def test_engineering_terms_are_a_named_framework(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        framework = data['frameworks']['engineering-terms']
        self.assertIn('非统一学术 taxonomy', framework['status'])
        self.assertEqual([c['term'] for c in framework['categories']], ['context', 'workspace', 'longterm'])
        for term_id in ('context', 'workspace', 'longterm'):
            term = data['terms'][term_id]
            self.assertTrue(term.get('evidenceLevel'))
            self.assertTrue(term.get('standardization'))
        js = (ROOT / 'site/knowledge.js').read_text()
        self.assertIn('kn-crosswalk', js)
        self.assertIn('kn-comic', js)
        self.assertIn('典型记忆内容 × 当前分类方式', js)

    def test_primary_sources_use_verifiable_titles_and_dates(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        three_source = data['sources']['foundation-agent-taxonomy-arxiv']
        self.assertIn('A Survey of Agent Memory in the Second Half', three_source['label'])
        self.assertNotIn('Rethinking Memory Mechanisms', three_source['label'])
        self.assertIn('accepted at TMLR', three_source['evidence'])
        self.assertEqual(data['sources']['coala']['year'], '2023 arXiv / 2024 TMLR')
        self.assertEqual(data['frameworks']['coala']['status'], '2023 arXiv / 2024 TMLR · 研究框架论文')
        self.assertIn('感觉/工作/情景/语义/程序性', three_source['evidence'])

    def test_taxonomy_controls_keep_native_toggle_and_selection(self):
        knowledge_js = (ROOT / 'site/knowledge.js').read_text()
        app_js = (ROOT / 'site/app.js').read_text()
        self.assertIn('role="group" aria-label="主流分类方式"', knowledge_js)
        self.assertNotIn('role="list" aria-label="主流分类方式"', knowledge_js)
        self.assertIn('categoryOpen', app_js)
        self.assertIn('event.preventDefault()', app_js)
        self.assertNotIn("memoryType:'working-context'", app_js)
        self.assertIn('kn-map-unclear', knowledge_js)
        self.assertIn('kn-map-unclear', knowledge_js.split('kn-map-legend', 1)[1])

    def test_draft_taxonomy_is_explicitly_unverified_and_four_frameworks_share_fields(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        draft = data['draftTaxonomy']
        self.assertEqual(draft['status'], '待验证')
        self.assertEqual(len(draft['items']), 7)
        self.assertIn('不是某篇论文提出的分类', draft['limitation'])
        self.assertIn('七项', draft['rationale'])
        required = {'classificationBasis', 'categoryRelations', 'structureEvidence', 'empiricalSupport', 'scope', 'limitations'}
        reader = {'scenarios', 'focus', 'advantages', 'tradeoffs'}
        for framework in data['frameworks'].values():
            self.assertTrue(required <= set(framework['sourceFacts']))
            self.assertTrue(reader <= set(framework['readerGuide']))
            self.assertGreaterEqual(len(framework['sourceScenarios']), 1)
            for scenario in framework['sourceScenarios']:
                self.assertTrue({'title', 'source', 'location', 'background', 'memory', 'storage', 'write', 'read', 'maintenance', 'effect', 'contrast', 'evidence'} <= set(scenario))
                self.assertIn(scenario['source'], data['sources'])

    def test_generated_outputs_keep_draft_anchors_evidence_and_mapping_status(self):
        spec = importlib.util.spec_from_file_location('build_site', ROOT / 'scripts/build_site.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        outputs = builder.generated_files()
        markdown = outputs[ROOT / 'docs/landscape.zh-CN.md']
        html = outputs[ROOT / 'index.html']
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        for item in data['draftTaxonomy']['items']:
            self.assertIn(f'<a id="types-{item["id"]}"></a>', markdown)
        self.assertIn(data['draftTaxonomy']['title'], markdown)
        self.assertIn(data['contentIndex']['mappingStatus'], markdown)
        for term_id in ('context', 'workspace', 'longterm'):
            term = data['terms'][term_id]
            self.assertIn(term['evidenceLevel'], markdown)
            self.assertIn(term['standardization'], markdown)
        self.assertIn('kn-term-evidence', html)
        self.assertIn('kn-map-unclear', (ROOT / 'site/knowledge.css').read_text())
        self.assertNotIn('kn-map-unknown', (ROOT / 'site/knowledge.css').read_text())

    def test_taxonomy_rendering_keeps_cross_sections_outside_classification(self):
        js = (ROOT / 'site/knowledge.js').read_text()
        self.assertIn('draftTaxonomySection()', js)
        self.assertIn('contentIndexSection()', js)
        render = js.split('function renderTaxonomy()', 1)[1].split('function renderTopic()', 1)[0]
        classification = render.split('</section>${draftTaxonomySection()', 1)[0]
        self.assertNotIn('contentIndexNav()', classification)
        self.assertNotIn('taxonomyCrosswalk()', classification)
        self.assertNotIn('relatedResearchPerspectives()', classification)
        self.assertNotIn('当前选中的典型内容', classification)
        self.assertNotIn('回答不同问题', classification)


if __name__ == '__main__':
    unittest.main()
