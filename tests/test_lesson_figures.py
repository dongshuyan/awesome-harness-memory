"""Regression checks for the relationships shown by teaching diagrams."""
import importlib.util
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('lesson_figures', ROOT / 'scripts/build_lesson_figures.py')
figures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(figures)


class LessonFigureRelationships(unittest.TestCase):
    def render(self, nodes, connections):
        figure = figures.Figure({
            'id': 'relationship-test', 'layout': 'split', 'title': 'Test',
            'alt': 'Two independent observations inform one conclusion.',
            'nodes': nodes, 'connections': connections,
        })
        svg, _ = figure.render()
        tree = ET.fromstring(svg)
        arrows = [p for p in tree.iter('{http://www.w3.org/2000/svg}path')
                  if p.get('marker-end')]
        return figure.boxes, arrows

    def test_two_independent_branches_join_only_at_the_shared_result(self):
        nodes = [{'title': name, 'lines': []} for name in
                 ['Monday record', 'Thursday record', 'Monday reflection',
                  'Thursday reflection', 'Shared candidate']]
        nodes[-1]['span'] = 2
        edges = [{'from': a, 'to': b} for a, b in [(0, 2), (1, 3), (2, 4), (3, 4)]]
        boxes, arrows = self.render(nodes, edges)
        self.assertEqual(len(arrows), 4, 'Every declared relationship must be visible')
        left, right, shared = boxes[2], boxes[3], boxes[4]
        self.assertLess(left[0], right[0])
        self.assertEqual(shared[0], left[0])
        self.assertEqual(shared[0] + shared[2], right[0] + right[2])
        self.assertGreater(shared[1], max(left[1] + left[3], right[1] + right[3]))

    def test_diagonal_relationships_are_drawn_not_only_described(self):
        nodes = [{'title': str(i), 'lines': []} for i in range(4)]
        edges = [{'from': a, 'to': b} for a, b in [(0, 3), (1, 2)]]
        _, arrows = self.render(nodes, edges)
        self.assertEqual(len(arrows), len(edges))


if __name__ == '__main__':
    unittest.main()
