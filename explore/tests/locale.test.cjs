const test = require('node:test');
const assert = require('node:assert/strict');
const content = require('../content.js');
const resources = require('../catalog.js');
const locale = require('../locale.js');
const chinese = require('../locale.zh-CN.js');

test('Chinese preserves every concept, connection, resource, source URL, and evidence boundary', () => {
  const original = JSON.stringify({ content, resources });
  const translated = locale.localize(content, resources, chinese);
  for (const [group, fields] of [['views', ['label', 'question', 'description']], ['concepts', ['title', 'subtitle', 'definition', 'distinction']], ['edges', ['label', 'explanation']]]) {
    assert.deepEqual(Object.keys(chinese[group]).sort(), content[group].map(item => item.id).sort());
    assert.equal(translated.content[group].length, content[group].length);
    content[group].forEach((item, index) => {
      const actual = translated.content[group][index];
      for (const field of fields) assert.match(actual[field], /[\u3400-\u9fff]/u, item.id + '.' + field);
      const structural = Object.fromEntries(Object.entries(actual).filter(([key]) => !fields.includes(key)));
      assert.deepEqual(structural, Object.fromEntries(Object.entries(item).filter(([key]) => !fields.includes(key))));
    });
  }
  assert.deepEqual(Object.keys(chinese.resources).sort(), resources.map(item => item.id).sort());
  translated.resources.forEach((item, index) => {
    const source = resources[index];
    assert.equal(item.id, source.id);
    assert.equal(item.title, source.title);
    assert.match(item.summary, /[\u3400-\u9fff]/u, item.id);
    if (source.analogy) assert.match(item.analogy, /[\u3400-\u9fff]/u, item.id + ' analogy');
    if (source.evaluationNote) assert.match(item.evaluationNote, /数据集版本.*评判/u);
    assert.deepEqual(item.entries, source.entries);
    assert.deepEqual(item.types, source.types);
    assert.deepEqual(item.sources.map(x => x.url), source.sources.map(x => x.url));
    assert.ok(item.sources.every(x => /[\u3400-\u9fff]/u.test(x.label) || x.label === 'MemFS'));
  });
  assert.equal(JSON.stringify({ content, resources }), original, 'localization must not mutate English data');
});

test('Chinese provides every UI message with the same dynamic placeholders', () => {
  assert.equal(new Set(resources.filter(item => item.evaluationNote).map(item => item.evaluationNote)).size, 1, 'different evaluation notes require separate translations');
  assert.deepEqual(Object.keys(chinese.ui).sort(), Object.keys(locale.ui).sort());
  for (const key of Object.keys(locale.ui)) {
    assert.deepEqual((chinese.ui[key].match(/\{\w+\}/g) || []).sort(), (locale.ui[key].match(/\{\w+\}/g) || []).sort(), key);
  }
  assert.deepEqual(locale.localize(content, resources), { content, resources });
});
