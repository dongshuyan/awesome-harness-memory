// Course URLs are also the shareable state of the comparison and section links.
const DEFAULT_COMPARISON_IDS = ['coala','claude-code','longmemeval'];
function routeState(hash) {
  const raw = String(hash || '').replace(/^#/, '');
  if (!raw || raw === 'home' || raw === 'tutorial' || raw === 'tutorial/home') return {view:'tutorial-home'};
  const [path, query = ''] = raw.split('?');
  const params = new URLSearchParams(query);
  const sections = {lesson:'lesson', concepts:'concepts', research:'research', engineering:'engineering', benchmarks:'benchmarks', culture:'culture', 'human-memory':'human', human:'human', topics:'topics', compare:'compare', about:'about'};
  let parts;
  try { parts = path.split('/').map(decodeURIComponent); }
  catch { return {view:'not-found', routePath:`#${raw}`}; }
  let result;
  if (parts[0] === 'tutorial' && parts.length === 2 && Object.hasOwn(sections, parts[1])) {
    result = {view:`tutorial-${sections[parts[1]]}`};
    if (parts[1] === 'compare') {
      result.tutorialCompare = params.has('ids') ? params.get('ids').split(',').filter(Boolean) : [...DEFAULT_COMPARISON_IDS];
    }
  } else if (parts[0] === 'tutorial' && parts[1] === 'detail' && parts.length === 4 &&
      ['research','engineering','benchmarks','culture','humanMemory'].includes(parts[2]) && parts[3]) {
    result = {view:'tutorial-detail', tutorialCategory:parts[2], tutorialEntry:parts[3]};
  } else return {view:'not-found', routePath:`#${raw}`};
  if (params.has('section')) result.section = params.get('section');
  return result;
}

function routeHash(s) {
  if (s.view === 'home' || s.view === 'tutorial-home') return '#tutorial';
  if (s.view === 'not-found') return s.routePath || '#tutorial';
  let hash;
  if (s.view === 'tutorial-detail') {
    hash = `#tutorial/detail/${encodeURIComponent(s.tutorialCategory)}/${encodeURIComponent(s.tutorialEntry)}`;
  } else if (s.view === 'tutorial-compare') {
    hash = '#tutorial/compare';
    if (Array.isArray(s.tutorialCompare)) hash += `?ids=${s.tutorialCompare.map(encodeURIComponent).join(',')}`;
  } else {
    const name = s.view.replace(/^tutorial-/, '');
    hash = `#tutorial/${name === 'human' ? 'human-memory' : name}`;
  }
  if (s.section) hash += `${hash.includes('?') ? '&' : '?'}section=${encodeURIComponent(s.section)}`;
  return hash;
}
