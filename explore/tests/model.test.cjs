const test = require('node:test');
const assert = require('node:assert/strict');
const { readState, nextState, stateHash, relationsFor } = require('../model.js');

const fixture = {
  views: [{ id: 'continuity', nodes: ['context', 'state'] }, { id: 'change', nodes: ['state', 'revision'] }],
  concepts: [{ id: 'context' }, { id: 'state' }, { id: 'revision' }],
  edges: [{ id: 'a', from: 'context', to: 'state' }, { id: 'b', from: 'state', to: 'revision' }]
};

test('a copied URL restores the chosen perspective and concept', () => {
  const chosen = { view: 'change', node: 'revision' };
  assert.deepEqual(readState(stateHash(chosen), fixture), chosen);
});

test('unknown links recover to a real view and concept', () => {
  assert.deepEqual(readState('#view=missing&node=%3Cscript%3E', fixture), { view: 'continuity', node: 'context' });
});

test('changing perspectives preserves the concept, even outside its focus', () => {
  assert.deepEqual(nextState({ view: 'continuity', node: 'context' }, { view: 'change' }, fixture), { view: 'change', node: 'context' });
});

test('connections include both incoming and outgoing relations without duplicates', () => {
  assert.deepEqual(relationsFor('state', fixture).map(edge => edge.id), ['a', 'b']);
  assert.deepEqual(relationsFor('missing', fixture), []);
});
