import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HarnessMapContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'assets/harness-map.json').read_text())
        cls.catalogue = json.loads((ROOT / 'catalogue.json').read_text())['resources']

    def test_every_catalogued_harness_has_a_real_profile(self):
        actual = {p['resourceId'] for p in self.data['systems']}
        required = {r['id'] for r in self.catalogue if r.get('group') == 'harness'}
        self.assertLessEqual(required, actual)
        self.assertLessEqual({'pi', 'codex', 'claude-code'}, actual)
        self.assertTrue(all(p['kind'] in ('harness', 'agent') for p in self.data['systems']))
        self.assertFalse({'claude-mem', 'mem0', 'graphiti', 'langgraph'} & actual)

    def test_claims_have_traceable_sources_and_valid_properties(self):
        properties = {o['id'] for d in self.data['dimensions'] for o in d['options']}
        ids = set()
        for system in self.data['systems']:
            self.assertNotIn(system['id'], ids)
            ids.add(system['id'])
            self.assertIn(system['identitySource'], self.data['sources'])
            seen = set()
            for claim in system['claims']:
                self.assertIn(claim['source'], self.data['sources'])
                self.assertTrue(claim['note'] and claim['section'])
                self.assertIn(claim['status'], ('yes', 'no', 'config', 'unknown'))
                self.assertFalse(seen.intersection(claim['features']))
                seen.update(claim['features'])
                self.assertLessEqual(set(claim['features']), properties)
        for source in self.data['sources'].values():
            self.assertTrue(source['url'].startswith('https://'))
            self.assertTrue(source['checked'] and source['kind'])

    def test_undeclared_capability_stays_unknown_and_config_stays_conditional(self):
        spec = importlib.util.spec_from_file_location('builder', ROOT / 'scripts/build_harness_map.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        self.assertEqual(builder.cell({'claims': []}, 'form.graph')['status'], 'unknown')
        cline = next(p for p in self.data['systems'] if p['id'] == 'cline')
        self.assertEqual(builder.cell(cline, 'form.files')['status'], 'config')
        deepseek = next(p for p in self.data['systems'] if p['id'] == 'deepseek-harness')
        self.assertEqual(builder.cell(deepseek, 'owner.external')['status'], 'config')

    def test_generated_page_preserves_data_and_cannot_close_json_script(self):
        spec = importlib.util.spec_from_file_location('builder', ROOT / 'scripts/build_harness_map.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        payload = {'label': '</script><img src=x onerror=alert(1)>', 'amp': '&'}
        encoded = builder.script_json(payload)
        self.assertNotIn('<', encoded)
        self.assertEqual(json.loads(encoded), payload)
        self.assertEqual(builder.generated_files(ROOT), {p: p.read_text() for p in builder.generated_files(ROOT)})

if __name__ == '__main__':
    unittest.main()
