import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('memory_lab', ROOT / 'examples/memory_lab.py')
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


class MemoryLabBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'memory.sqlite'
        self.store = lab.MemoryStore(self.path)
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(self.store.close)

    def test_reload_update_and_scope_are_independent(self):
        self.store.remember('alice/project', 'package', 'npm', 'meeting-1', now=1)
        self.store.remember('bob/project', 'package', 'yarn', 'meeting-2', now=2)
        self.store.remember('alice/project', 'package', 'pnpm', 'correction-3', now=3)
        self.store.close()
        self.store = lab.MemoryStore(self.path)
        self.addCleanup(self.store.close)
        self.assertEqual([r['value'] for r in self.store.recall('alice/project', 'package', now=4)], ['pnpm'])
        self.assertEqual([r['value'] for r in self.store.recall('bob/project', 'package', now=4)], ['yarn'])
        self.assertEqual(len(self.store.history('alice/project', 'package')), 2)

    def test_expiry_and_forget_stop_recall_but_keep_history(self):
        self.store.remember('a', 'deadline', 'Friday', 'note', now=1, expires_at=5)
        self.assertEqual(len(self.store.recall('a', 'deadline', now=4)), 1)
        self.assertEqual(self.store.recall('a', 'deadline', now=5), [])
        self.store.remember('a', 'deadline', 'Monday', 'correction', now=6)
        self.store.forget('a', 'deadline')
        self.assertEqual(self.store.recall('a', 'deadline', now=7), [])
        self.assertEqual(len(self.store.history('a', 'deadline')), 2)

    def test_budget_preserves_whole_records_and_source(self):
        self.store.remember('a', 'note', 'x' * 100, 'source', now=1)
        rows = self.store.recall('a', 'note', now=2)
        self.assertEqual(lab.render_context(rows, max_chars=10), '')
        context = lab.render_context(rows, max_chars=1000)
        self.assertLessEqual(len(context), 1000)
        self.assertEqual(json.loads(context), {
            'key': 'note', 'value': 'x' * 100,
            'source': 'source', 'trust': 'unverified',
        })

    def test_failed_replacement_rolls_back_retirement(self):
        self.store.remember('a', 'note', 'valid', 'original', now=1)
        self.store.db.execute('''CREATE TRIGGER reject_replacement BEFORE INSERT ON memories
            WHEN NEW.value = 'rejected'
            BEGIN SELECT RAISE(ABORT, 'simulated insert failure'); END''')
        self.store.db.commit()
        with self.assertRaisesRegex(sqlite3.IntegrityError, 'simulated insert failure'):
            self.store.remember('a', 'note', 'rejected', 'replacement', now=2)
        self.assertEqual([r['value'] for r in self.store.recall('a', 'note', now=3)], ['valid'])
        self.assertEqual(self.store.history('a', 'note')[0]['active'], 1)
        self.store.close()
        self.store = lab.MemoryStore(self.path)
        self.addCleanup(self.store.close)
        self.assertEqual([r['value'] for r in self.store.recall('a', 'note', now=3)], ['valid'])
        history = self.store.history('a', 'note')
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]['active'], 1)

    def test_invalid_write_does_not_retire_valid_record(self):
        self.store.remember('a', 'note', 'valid', 'source', now=1)
        with self.assertRaises(ValueError):
            self.store.remember('a', 'note', '', 'source', now=2)
        self.assertEqual(self.store.recall('a', 'note', now=3)[0]['value'], 'valid')


if __name__ == '__main__':
    unittest.main()
