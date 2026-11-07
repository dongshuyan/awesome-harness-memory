import importlib.util
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class KnowledgeContract(unittest.TestCase):
    def test_all_legacy_methods_remain_discoverable(self):
        data = json.loads((ROOT / 'site/knowledge.json').read_text())
        methods = [m for t in data['topics'] for m in t['methods']]
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
        self.assertFalse(set(data['terms']) & set(data['frameworks']['coala']['children'].get('working', [])))
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
        methods = [m for t in data['topics'] for m in t['methods']]
        for axis in navigation['legacyAxes']:
            for i, old in enumerate(axis['methods']):
                destinations = [m for m in methods if f'{axis["id"]}:{i}' in m.get('legacy', [])]
                self.assertTrue(destinations)
                self.assertLessEqual(set(old[4]), {rid for m in destinations for rid in m['resources']})
        topic_ids = {t['id'] for t in data['topics']}
        for targets in navigation['projectionTopics'].values():
            self.assertLessEqual(set(targets), topic_ids)


if __name__ == '__main__':
    unittest.main()
