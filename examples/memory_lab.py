#!/usr/bin/env python3
"""A local memory mechanism lab. No LLM, network, or production authentication."""
import json
from pathlib import Path
import sqlite3
import tempfile


class MemoryStore:
    """Caller-supplied scopes demonstrate filtering, not identity verification."""

    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute('''CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY, scope TEXT NOT NULL, key TEXT NOT NULL,
            value TEXT NOT NULL, source TEXT NOT NULL, created_at REAL NOT NULL,
            expires_at REAL, active INTEGER NOT NULL DEFAULT 1
        )''')
        self.db.commit()

    def close(self):
        self.db.close()

    def remember(self, scope, key, value, source, *, now, expires_at=None):
        if not all(isinstance(x, str) and x.strip() for x in (scope, key, value, source)):
            raise ValueError('scope, key, value, and source must be nonempty strings')
        if expires_at is not None and expires_at <= now:
            raise ValueError('expires_at must be later than the write time')
        # Supersession and the replacement commit together; old versions remain inspectable.
        with self.db:
            self.db.execute('UPDATE memories SET active=0 WHERE scope=? AND key=?', (scope, key))
            self.db.execute('''INSERT INTO memories
                (scope,key,value,source,created_at,expires_at) VALUES (?,?,?,?,?,?)''',
                (scope, key, value, source, now, expires_at))

    def recall(self, scope, query, *, now):
        rows = self.db.execute('''SELECT * FROM memories WHERE scope=? AND active=1
            AND created_at<=? AND (expires_at IS NULL OR expires_at>?)
            ORDER BY created_at DESC, id DESC''', (scope, now, now))
        terms = query.casefold().split()
        return [dict(row) for row in rows
                if all(term in (row['key'] + ' ' + row['value']).casefold() for term in terms)]

    def forget(self, scope, key):
        """Stop retrieval; this is NOT physical deletion of the history or SQLite pages."""
        with self.db:
            self.db.execute('UPDATE memories SET active=0 WHERE scope=? AND key=?', (scope, key))

    def history(self, scope, key):
        return [dict(row) for row in self.db.execute(
            'SELECT * FROM memories WHERE scope=? AND key=? ORDER BY id', (scope, key))]


def render_context(rows, *, max_chars):
    """Return whole JSON records within a character budget (not a token budget)."""
    selected = []
    used = 0
    for row in rows:
        line = json.dumps({k: row[k] for k in ('key', 'value', 'source')}
                          | {'trust': 'unverified'}, ensure_ascii=False) + '\n'
        if used + len(line) <= max_chars:
            selected.append(line)
            used += len(line)
    return ''.join(selected)


def demo():
    # Fictional data; separate connections stand in for two caller invocations.
    with tempfile.TemporaryDirectory(prefix='memory-lab-') as directory:
        path = Path(directory) / 'memory.sqlite'
        first = MemoryStore(path)
        try:
            first.remember('alice/repo', 'package_manager', 'npm', 'meeting-1', now=1)
            first.remember('alice/repo', 'package_manager', 'pnpm', 'correction-2', now=2)
            first.remember('bob/repo', 'package_manager', 'yarn', 'bob-note', now=2)
            first.remember('alice/repo', 'temporary_branch', 'release', 'task-note', now=2, expires_at=4)
        finally:
            first.close()
        second = MemoryStore(path)
        try:
            print('下一次调用可用的材料（没有调用模型）：')
            print(render_context(second.recall('alice/repo', 'package_manager', now=3), max_chars=500), end='')
            print('已过期记录：', second.recall('alice/repo', 'temporary_branch', now=4))
            print('其他范围：', second.recall('carol/repo', 'package_manager', now=3))
            second.forget('alice/repo', 'package_manager')
            print('停止召回后：', second.recall('alice/repo', 'package_manager', now=4))
            print('历史仍保留的版本数：', len(second.history('alice/repo', 'package_manager')))
        finally:
            second.close()


if __name__ == '__main__':
    demo()
