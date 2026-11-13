(() => {
'use strict';
const tutorial = JSON.parse(document.getElementById('tutorial-data').textContent);
const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const tutorialComparisonCategories = tutorial.comparisonCategories;
const main = document.getElementById('course-main');
const sidebar = document.getElementById('course-nav');
const menu = document.getElementById('menu-toggle');
const toc = document.getElementById('page-toc');
const validIds = new Set(tutorialComparisonCategories.flatMap(c => tutorialReadings(c).map(e => e.id)));
function normalize(s) {
  const selected = Array.isArray(s.tutorialCompare) ? s.tutorialCompare : DEFAULT_COMPARISON_IDS;
  return {...s, tutorialCompare:[...new Set(selected)].filter(id => validIds.has(id))};
}
let state = normalize(routeState(location.hash));
function crumbs(label, category) {
  return `<nav class="breadcrumb" aria-label="当前位置"><a href="#tutorial">教程</a><span>/</span>${category ? `<a href="${tutorialCategoryRoute(category)}">${esc(tutorialCategoryLabel(category))}</a><span>/</span>` : ''}<span>${esc(label)}</span></nav>`;
}
/*__TUTORIAL_RENDERERS__*/
function notFound() {
  return `${crumbs('页面不存在')}<h1>找不到这个课程页面</h1><p>链接 <code>${esc(state.routePath || '')}</code> 没有对应的章节。请从课程目录选择要读的内容。</p><a href="#tutorial">回到课程首页 →</a>`;
}
const renderers = {
  'tutorial-home':tutorialHome, 'tutorial-lesson':tutorialLesson,
  'tutorial-concepts':tutorialConcepts, 'tutorial-research':() => tutorialIndex('research'),
  'tutorial-engineering':() => tutorialIndex('engineering'), 'tutorial-benchmarks':() => tutorialIndex('benchmarks'),
  'tutorial-culture':() => tutorialIndex('culture'), 'tutorial-human':() => tutorialIndex('humanMemory'),
  'tutorial-topics':tutorialTopics, 'tutorial-compare':tutorialCompare,
  'tutorial-about':tutorialAbout, 'tutorial-detail':tutorialDetail, 'not-found':notFound
};
function render({focus = true, selectedId = '', openGroups = []} = {}) {
  main.innerHTML = (renderers[state.view] || notFound)();
  const active = state.view === 'tutorial-detail' ? (state.tutorialCategory === 'humanMemory' ? 'human' : state.tutorialCategory) : state.view.replace(/^tutorial-/, '');
  sidebar.querySelectorAll('[data-nav]').forEach(a => {
    if (a.dataset.nav === active) a.setAttribute('aria-current','page');
    else a.removeAttribute('aria-current');
  });
  const sections = [...main.querySelectorAll('section[id]')].map(section => ({id:section.id, title:section.querySelector('h2')?.textContent})).filter(s => s.title);
  toc.innerHTML = sections.length ? `<p>本页内容</p>${sections.map(s => `<a href="${routeHash({...state, section:s.id})}">${esc(s.title)}</a>`).join('')}` : '';
  const title = main.querySelector('h1');
  const pageTitle = title?.textContent || 'Agent Memory 教程';
  document.title = pageTitle === 'Agent Memory 教程' ? pageTitle : `${pageTitle} · Agent Memory 教程`;
  document.getElementById('course-announcement').textContent = title?.textContent || '页面已更新';
  if (selectedId) {
    main.querySelectorAll('details[data-compare-group]').forEach(d => {d.open = openGroups.includes(d.dataset.compareGroup);});
    [...main.querySelectorAll('[data-tutorial-compare]')].find(el => el.dataset.tutorialCompare === selectedId)?.focus({preventScroll:true});
    return;
  }
  sidebar.classList.remove('is-open');
  menu.setAttribute('aria-expanded','false');
  if (!focus && !state.section) return;
  requestAnimationFrame(() => {
    const section = state.section && document.getElementById(state.section);
    const target = section && main.contains(section) ? section : title;
    if (!target) return;
    target.setAttribute('tabindex','-1');
    target.focus({preventScroll:true});
    if (target === title) window.scrollTo({top:0, behavior:'instant'});
    else target.scrollIntoView({block:'start', behavior:'instant'});
  });
}
function navigate(next, options) {
  state = normalize(next);
  const hash = routeHash(state);
  if (hash !== location.hash) history.pushState(null, '', hash);
  render(options);
}
function restoreLocation() {
  const next = normalize({...state, section:'', ...routeState(location.hash)});
  if (JSON.stringify(next) !== JSON.stringify(state)) {state = next; render();}
}
// A history traversal can emit both events; render the resulting state once.
window.addEventListener('hashchange', restoreLocation);
window.addEventListener('popstate', restoreLocation);
menu.addEventListener('click', () => {
  const open = sidebar.classList.toggle('is-open');
  menu.setAttribute('aria-expanded', String(open));
});
sidebar.addEventListener('click', event => {
  const link = event.target.closest('a[href]');
  if (!link) return;
  if (sidebar.classList.contains('is-open') && link.hash === location.hash) menu.focus();
  sidebar.classList.remove('is-open');
  menu.setAttribute('aria-expanded','false');
});
document.querySelector('.skip-link').addEventListener('click', event => {event.preventDefault(); main.focus();});
main.addEventListener('click', event => {
  const button = event.target.closest('[data-tutorial-add-to-compare]');
  if (!button) return;
  const [category, id] = button.dataset.tutorialAddToCompare.split(':');
  if (!tutorialEntryBy(category,id)) return;
  navigate({...state, view:'tutorial-compare', section:'', tutorialCompare:[...state.tutorialCompare,id]});
});
main.addEventListener('change', event => {
  const id = event.target.dataset.tutorialCompare;
  if (!id || !validIds.has(id)) return;
  const openGroups = [...main.querySelectorAll('details[data-compare-group][open]')].map(d => d.dataset.compareGroup);
  const selected = event.target.checked ? [...state.tutorialCompare,id] : state.tutorialCompare.filter(x => x !== id);
  navigate({...state, tutorialCompare:selected}, {selectedId:id, openGroups});
});
render({focus:false});
})();
