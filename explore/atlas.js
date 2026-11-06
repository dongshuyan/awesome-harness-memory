(function () {
  'use strict';
  const translated = document.documentElement.lang === 'zh-CN' ? window.AtlasChinese : undefined;
  const localized = window.AtlasLocale.localize(window.AtlasContent, window.AtlasResources, translated);
  const data = localized.content;
  const resources = localized.resources;
  const messages = translated ? translated.ui : window.AtlasLocale.ui;
  const t = (key, values = {}) => messages[key].replace(/\{(\w+)\}/g, (_, name) => values[name]);
  const model = window.AtlasModel;
  const byId = new Map(data.concepts.map(item => [item.id, item]));
  const resourceById = new Map(resources.map(item => [item.id, item]));
  const kindLabel = { systems: t('systems'), papers: t('papers'), benchmarks: t('benchmarks'), fiction: t('fiction') };
  const edgeLabel = { documented: t('documented'), synthesis: t('synthesis') };
  // Stagger labels that meet between the same two rows on narrower maps.
  const labelRows = { 'records-user': 46, 'user-revision': 53, 'state-revision': 47 };
  const $ = selector => document.querySelector(selector);
  const inspector = $('#inspector');
  const dialog = $('#resource-dialog');
  let state = model.readState(location.hash, data);
  let focusAfterRender = false;
  let dialogOpener = null;
  let fromLibrary = false;

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function link(text, href, className) {
    const node = el('a', className, text);
    node.href = href;
    node.target = '_blank';
    node.rel = 'noopener noreferrer';
    return node;
  }
  function button(text, className, action, id) {
    const node = el('button', className, text);
    node.type = 'button';
    node.dataset.action = action;
    if (id) node.dataset.id = id;
    return node;
  }
  function resourceButton(id) {
    const resource = resourceById.get(id);
    const node = button('', 'resource-button', 'resource', id);
    const title = el('span');
    title.append(el('strong', '', resource.title), el('small', '', resource.types.map(type => kindLabel[type]).join(' · ')));
    const arrow = el('span', 'resource-arrow', '↗');
    arrow.setAttribute('aria-hidden', 'true');
    node.append(title, arrow);
    return node;
  }
  function select(patch, focusDetails = false) {
    const next = model.nextState(state, patch, data);
    focusAfterRender = focusDetails;
    const hash = model.stateHash(next);
    if (hash === location.hash) {
      if (focusDetails) focusDetail();
      return;
    }
    location.hash = hash;
  }
  function focusDetail() {
    const heading = $('#concept-title');
    heading.focus({ preventScroll: true });
    if (matchMedia('(max-width:1100px)').matches) heading.scrollIntoView({ block: 'start', behavior: 'instant' });
    focusAfterRender = false;
  }

  function initializeControls() {
    for (const [index, view] of data.views.entries()) {
      const node = button('', 'lens', 'view', view.id);
      node.id = 'lens-' + view.id;
      node.setAttribute('role', 'tab');
      node.setAttribute('aria-controls', 'lens-panel');
      node.append(el('span', '', view.number), document.createTextNode(view.label));
      node.addEventListener('keydown', event => {
        let destination;
        if (event.key === 'ArrowRight') destination = (index + 1) % data.views.length;
        if (event.key === 'ArrowLeft') destination = (index + data.views.length - 1) % data.views.length;
        if (event.key === 'Home') destination = 0;
        if (event.key === 'End') destination = data.views.length - 1;
        if (destination === undefined) return;
        event.preventDefault();
        $('#lens-' + data.views[destination].id).focus();
        select({ view: data.views[destination].id });
      });
      $('#lenses').append(node);
    }
    for (const concept of data.concepts) {
      const node = button('', 'node', 'concept', concept.id);
      node.id = 'node-' + concept.id;
      node.dataset.color = concept.color;
      node.style.left = concept.x + '%';
      node.style.top = concept.y + '%';
      node.setAttribute('aria-controls', 'inspector');
      node.setAttribute('aria-label', concept.title);
      node.append(el('span', 'node-number', concept.number), el('strong', '', concept.title), el('small', '', concept.subtitle));
      $('#nodes').append(node);
    }
  }

  function drawConnections(view) {
    const svg = $('#connections');
    svg.replaceChildren();
    $('#edge-labels').replaceChildren();
    const ns = 'http://www.w3.org/2000/svg';
    for (const edge of data.edges) {
      const active = edge.from === state.node || edge.to === state.node;
      const inView = view.nodes.includes(edge.from) && view.nodes.includes(edge.to);
      if (!active && !inView) continue;
      const from = byId.get(edge.from);
      const to = byId.get(edge.to);
      const path = document.createElementNS(ns, 'path');
      const x1 = from.x * 10, x2 = to.x * 10, y1 = from.y * 5, y2 = to.y * 5;
      path.setAttribute('d', `M ${x1} ${y1} C ${x1} ${(y1 + y2) / 2}, ${x2} ${(y1 + y2) / 2}, ${x2} ${y2}`);
      path.setAttribute('class', `connection ${edge.kind}${active ? ' active' : ''}`);
      svg.append(path);
      if (active) {
        const label = el('span', 'edge-label', edge.label);
        label.style.left = (from.x + to.x) / 2 + '%';
        label.style.top = (labelRows[edge.id] ?? (from.y === to.y ? from.y - 24 : (from.y + to.y) / 2 - 3)) + '%';
        $('#edge-labels').append(label);
      }
    }
  }

  function renderInspector(view) {
    const concept = byId.get(state.node);
    inspector.replaceChildren();
    const top = el('div', 'detail-topline');
    top.append(el('span', 'detail-number', concept.number), el('span', 'tag', t('conceptTag')));
    const title = el('h2', '', concept.title);
    title.id = 'concept-title';
    title.tabIndex = -1;
    inspector.append(top, title);
    if (!view.nodes.includes(concept.id)) inspector.append(el('p', 'outside-note', t('outside')));
    inspector.append(el('p', 'definition', concept.definition));
    const distinction = el('div', 'distinction');
    distinction.append(el('strong', '', t('distinction')), document.createTextNode(concept.distinction));
    inspector.append(distinction, el('h3', '', t('connections')));
    for (const edge of model.relationsFor(concept.id, data)) {
      const other = byId.get(edge.from === concept.id ? edge.to : edge.from);
      const row = el('div', 'relation');
      const jump = button(other.title + ' →', 'relation-button', 'concept', other.id);
      const detail = el('details');
      detail.append(el('summary', '', t('why', { kind: edgeLabel[edge.kind] })), el('p', '', edge.explanation));
      detail.append(link(t('reference'), edge.source, 'source-link'));
      const sources = el('div', 'evidence-resources');
      for (const id of edge.evidence) sources.append(resourceButton(id));
      detail.append(sources);
      row.append(jump, el('p', 'relation-label', edge.label), detail);
      inspector.append(row);
    }
    inspector.append(el('h3', '', t('representatives')), el('p', 'section-note', t('representativeIntro')));
    for (const id of concept.examples) inspector.append(resourceButton(id));
    if (concept.stories.length) {
      const stories = el('details', 'story-section');
      stories.append(el('summary', '', t('literary', { count: concept.stories.length })), el('p', '', t('literaryIntro')));
      for (const id of concept.stories) stories.append(resourceButton(id));
      inspector.append(stories);
    }
  }

  function render() {
    state = model.readState(location.hash, data);
    const view = data.views.find(item => item.id === state.view);
    for (const item of data.views) {
      const tab = $('#lens-' + item.id);
      tab.setAttribute('aria-selected', String(item.id === view.id));
      tab.tabIndex = item.id === view.id ? 0 : -1;
    }
    $('#lens-panel').setAttribute('aria-labelledby', 'lens-' + view.id);
    $('#lens-number').textContent = t('perspective', { number: view.number });
    $('#lens-question').textContent = view.question;
    $('#lens-description').textContent = view.description;
    for (const concept of data.concepts) {
      const node = $('#node-' + concept.id);
      node.className = 'node ' + (view.nodes.includes(concept.id) ? 'in-focus' : 'outside');
      node.setAttribute('aria-pressed', String(concept.id === state.node));
    }
    drawConnections(view);
    renderInspector(view);
    $('#announcement').textContent = t('announcement', { view: view.label, concept: byId.get(state.node).title });
    $('#language-link').href = $('#language-link').dataset.page + model.stateHash(state);
    if (focusAfterRender) focusDetail();
  }

  function showDialog() {
    if (!dialog.open) {
      dialogOpener = document.activeElement;
      dialog.showModal();
    }
    $('#dialog-title').focus({ preventScroll: true });
    dialog.scrollTop = 0;
  }
  function dialogTitle(text) {
    const title = el('h2', 'dialog-title', text);
    title.id = 'dialog-title';
    title.tabIndex = -1;
    return title;
  }
  function showResource(id) {
    const resource = resourceById.get(id);
    const body = $('#dialog-body');
    body.replaceChildren();
    if (fromLibrary) body.append(button(t('back'), 'back-library', 'library'));
    body.append(el('p', 'eyebrow', resource.types.map(type => kindLabel[type]).join(' / ')), dialogTitle(resource.title), el('p', 'dialog-summary', resource.summary));
    if (resource.evaluationNote) {
      const note = el('details', 'evaluation-note');
      note.append(el('summary', '', t('compare')), el('p', '', resource.evaluationNote));
      body.append(note);
    }
    if (resource.analogy) {
      body.append(el('h3', 'dialog-subtitle', t('analogy')), el('p', 'dialog-analogy', resource.analogy));
    }
    const entries = el('div', 'dialog-links');
    for (const entry of resource.entries) entries.append(link(t('entry', { kind: kindLabel[entry.label].toLowerCase() }), entry.url));
    body.append(entries, el('h3', 'dialog-subtitle', t('sources')));
    for (const source of resource.sources) body.append(link(source.label + ' ↗', source.url, 'dialog-source'));
    body.append(el('p', 'dialog-note', t(resource.analogy ? 'analogyNote' : 'resourceNote')));
    showDialog();
  }
  function showLibrary() {
    fromLibrary = true;
    const body = $('#dialog-body');
    body.replaceChildren(el('p', 'eyebrow', t('library')), dialogTitle(t('libraryTitle', { count: resources.length })), el('p', 'dialog-summary', t('libraryIntro')));
    const technical = new Set(data.concepts.flatMap(concept => concept.examples));
    const stories = new Set(data.concepts.flatMap(concept => concept.stories));
    const remaining = new Set(resources.filter(item => !technical.has(item.id) && !stories.has(item.id)).map(item => item.id));
    for (const [group, heading] of [[technical, t('technical', { count: technical.size })], [stories, t('stories', { count: stories.size })], [remaining, t('more', { count: remaining.size })]]) {
      body.append(el('h3', 'dialog-subtitle', heading));
      const list = el('div', 'library-list');
      for (const resource of resources.filter(item => group.has(item.id))) list.append(resourceButton(resource.id));
      body.append(list);
    }
    showDialog();
  }

  document.addEventListener('click', event => {
    const target = event.target.closest('[data-action]');
    if (!target) return;
    if (target.dataset.action === 'view') select({ view: target.dataset.id });
    if (target.dataset.action === 'concept') select({ node: target.dataset.id }, true);
    if (target.dataset.action === 'resource') {
      if (!dialog.open) fromLibrary = false;
      showResource(target.dataset.id);
    }
    if (target.dataset.action === 'library') showLibrary();
  });
  $('#library-button').addEventListener('click', showLibrary);
  $('.skip').addEventListener('click', event => {
    event.preventDefault();
    $('#main').focus();
  });
  $('#close-dialog').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => {
    const target = dialogOpener && dialogOpener.isConnected ? dialogOpener : $('#concept-title');
    target.focus({ preventScroll: true });
    fromLibrary = false;
  });
  window.addEventListener('hashchange', () => {
    if (dialog.open) dialog.close();
    render();
  });
  const technical = new Set(data.concepts.flatMap(concept => concept.examples));
  const stories = new Set(data.concepts.flatMap(concept => concept.stories));
  $('#library-count').textContent = t('curated', { count: resources.length });
  $('#coverage-count').textContent = t('coverage', { concepts: data.concepts.length, technical: technical.size, stories: stories.size });
  $('#checked-date').textContent = t('checked', { date: data.checked });
  initializeControls();
  render();
})();
