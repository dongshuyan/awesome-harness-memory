import json
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
            self.assertEqual(entry.get('status'), 'pending')
            self.assertTrue(entry.get('boundary'))
            self.assertTrue(entry.get('checkedAt'))
            self.assertTrue(set(entry.get('sources', [])) <= set(self.data['sources']))

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

    def test_visualizations_have_explanations_and_no_rankings(self):
        self.assertGreaterEqual(len(self.data['visualizations']), 3)
        for viz in self.data['visualizations']:
            for field in ('id', 'title', 'purpose', 'note'):
                self.assertTrue(viz.get(field), (viz.get('id'), field))
        self.assertNotIn('rank', json.dumps(self.data).lower())

    def test_every_detail_comparison_button_has_a_visible_picker_entry(self):
        source = (ROOT / 'site/tutorial.js').read_text()
        self.assertIn(
            "tutorialComparisonCategories.includes(category)?",
            source,
            'detail pages must only offer comparison for categories in the picker',
        )
        self.assertIn(
            'for(const category of tutorialComparisonCategories)',
            source,
            'the picker must use the same category allowlist as detail pages',
        )
        self.assertNotIn('category of [\'research\',\'engineering\',\'benchmarks\',\'culture\']', source)

    def test_engineering_dates_are_explicit(self):
        for entry in self.data['entries']['engineering']:
            self.assertTrue(entry['date'])
            self.assertIsInstance(entry['date'], str)

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


if __name__ == '__main__':
    unittest.main()
