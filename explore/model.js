(function (root) {
  'use strict';
  function readState(hash, data) {
    const params = new URLSearchParams(hash.replace(/^#/, ''));
    const view = data.views.find(item => item.id === params.get('view')) || data.views[0];
    const node = data.concepts.find(item => item.id === params.get('node'));
    return { view: view.id, node: node ? node.id : view.nodes[0] };
  }
  function stateHash(state) {
    return '#' + new URLSearchParams({ view: state.view, node: state.node }).toString();
  }
  function nextState(state, patch, data) {
    return readState(stateHash({ ...state, ...patch }), data);
  }
  function relationsFor(id, data) {
    return data.edges.filter(edge => edge.from === id || edge.to === id);
  }
  const api = { readState, stateHash, nextState, relationsFor };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.AtlasModel = api;
})(globalThis);
