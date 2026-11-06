const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const content = require('../content.js');
const resources = require('../catalog.js');

test('the library deduplicates the published resource families and retains both entry routes', () => {
  assert.equal(resources.length, 32);
  assert.equal(new Set(resources.map(item => item.id)).size, 32);
  const shared = resources.filter(item => item.types.includes('papers') && item.types.includes('benchmarks'));
  assert.equal(shared.length, 7);
  assert.ok(shared.every(item => item.entries.length === 2));
});

test('each concept, relation and resource reference resolves to an existing identity', () => {
  const nodes = new Set(content.concepts.map(item => item.id));
  const ids = new Set(resources.map(item => item.id));
  assert.equal(nodes.size, content.concepts.length);
  assert.equal(new Set(content.edges.map(item => item.id)).size, content.edges.length);
  for (const view of content.views) assert.ok(view.nodes.every(id => nodes.has(id)));
  for (const node of content.concepts) assert.ok([...node.examples, ...node.stories].every(id => ids.has(id)));
  for (const edge of content.edges) {
    assert.ok(nodes.has(edge.from) && nodes.has(edge.to) && edge.from !== edge.to);
    assert.ok(edge.evidence.length && edge.evidence.every(id => ids.has(id)));
    assert.ok(edge.explanation && edge.source.startsWith('https://'));
    assert.ok(['documented', 'synthesis'].includes(edge.kind));
  }
});

test('literary analogies remain separate from technical example references', () => {
  const fiction = new Set(resources.filter(item => item.types.includes('fiction')).map(item => item.id));
  for (const node of content.concepts) {
    assert.ok(node.stories.every(id => fiction.has(id)));
    assert.ok(node.examples.every(id => !fiction.has(id)));
  }
});

test('evaluation previews preserve both source summaries and comparison conditions', () => {
  for (const item of resources.filter(resource => resource.types.includes('benchmarks'))) {
    assert.equal(item.summaryKind, 'benchmarks');
    assert.equal(item.summary, item.summaries.benchmarks);
    assert.ok(item.evaluationNote.includes('dataset version') && item.evaluationNote.includes('judge'));
    if (item.types.includes('papers')) assert.ok(item.summaries.papers);
  }
});

test('every resource has a public source and a working source-page heading', () => {
  for (const resource of resources) {
    assert.ok(resource.summary && resource.sources.length, resource.id);
    assert.ok(resource.sources.every(source => source.url.startsWith('https://')), resource.id);
    for (const entry of resource.entries) {
      const markdown = fs.readFileSync(path.join(__dirname, '../..', entry.path), 'utf8');
      assert.ok(markdown.includes(`## ${resource.title}\n`), entry.path + resource.title);
    }
  }
});
