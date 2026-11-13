function tutorialParagraphs(text, className = '') {
  return String(text || '').split(/\n\s*\n/).filter(p => p.trim()).map(p => `<p${className ? ` class="${className}"` : ''}>${esc(p.trim())}</p>`).join('');
}
function tutorialSourceLinks(ids, compact = false) {
  const sources = [...new Set(ids || [])].map(id => tutorial.sources[id]).filter(Boolean);
  if (compact) return `<div class="source-inline">${sources.map(s => `<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.label)} ↗</a>`).join('')}</div>`;
  return `<ul class="source-list">${sources.map(s => `<li><a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.label)} ↗</a><small>${esc(s.year || '')}</small>${s.evidence ? `<details class="source-details"><summary>来源范围</summary>${tutorialParagraphs(s.evidence)}</details>` : ''}</li>`).join('')}</ul>`;
}
function tutorialReadings(category) { return [...(tutorial.entries[category] || []), ...(category === 'research' ? tutorial.researchCandidates || [] : [])]; }
function tutorialReadingLabel(entry, category) { return tutorialCategoryLabel(category) + (category === 'research' && tutorial.researchCandidates.some(e => e.id === entry.id) ? ' · 延伸阅读' : ''); }
function tutorialEntryBy(category, id) { return tutorialReadings(category).find(e => e.id === id) || null; }
function tutorialCategoryLabel(category) { return ({research:'Research', engineering:'工程', benchmarks:'Benchmark', culture:'文学与影视', humanMemory:'人类记忆背景'}[category] || category); }
function tutorialCategoryRoute(category) { return `#tutorial/${category === 'humanMemory' ? 'human-memory' : category}`; }
function tutorialEntryRoute(category, id) { return `#tutorial/detail/${encodeURIComponent(category)}/${encodeURIComponent(id)}`; }
function tutorialCounts() { return Object.fromEntries(Object.entries(tutorial.entries).map(([k, v]) => [k, {total:v.length, complete:v.filter(e => e.status === 'complete').length, pending:v.filter(e => e.status !== 'complete').length}])); }
function tutorialPublicationKey(entry) {
  const match = String(entry.date || '').match(/(?:19|20)\d{2}(?:-\d{2}(?:-\d{2})?)?/);
  if (!match) return 0;
  const [year, month = '00', day = '00'] = match[0].split('-');
  return Number(year + month + day);
}
function tutorialPublicationOrder(a, b) { return tutorialPublicationKey(b) - tutorialPublicationKey(a) || String(a.title).localeCompare(String(b.title), 'zh-CN'); }
function tutorialSortedEntries(category) { return (tutorial.entries[category] || []).slice().sort(tutorialPublicationOrder); }
function tutorialExample(text) { return `<div class="example"><div class="example-title">例子</div>${tutorialParagraphs(text)}</div>`; }
function tutorialSectionLinks(items, base) { return `<nav class="section-links" aria-label="本页目录">${items.map(([id, label]) => `<a href="${base}?section=${encodeURIComponent(id)}">${esc(label)}</a>`).join('')}</nav>`; }
function tutorialHeader(label, title, intro) { return `${crumbs(label)}<p class="eyebrow">${esc(label)}</p><h1>${esc(title)}</h1>${tutorialParagraphs(intro, 'lead')}`; }
function tutorialHome() {
  const path = [
    ['lesson','六个核心问题','先沿一条信息的去向，认识记忆系统里需要解释的六件事。'],
    ['concepts','相关概念辨析','分清上下文、对话历史、RAG 和检查点，读论文时不再混淆这些词。'],
    ['research','Research','带着六问阅读研究方法，了解它想解决的问题、设计和实验依据。'],
    ['engineering','工程实现','看这些想法怎样落实到真实系统的文件、接口、范围和控制中。'],
    ['benchmarks','Benchmark','了解怎样设计任务和指标，以及一项得分究竟能说明什么。'],
    ['culture','文学与影视','通过真实作品思考记忆、遗忘与身份，再审视工程类比的边界。']
  ];
  return `<p class="eyebrow">从概念到实践</p><h1>Agent Memory 教程</h1><p class="lead">一份信息怎样被保存，又怎样影响 Agent 下一次的回答和行动？这门教程从这个问题出发，带你阅读记忆系统的原理、研究和工程实现。</p><p>你不需要先选定框架，也不用背一套固定分类。沿着下面的路径学习，再把同样的问题带到具体系统中。</p><a class="start-link" href="#tutorial/lesson">开始第一课 →</a><h2>学习路径</h2><ol class="course-path">${path.map(([id, title, intro], i) => `<li><span class="path-number">0${i + 1}</span><div><a href="#tutorial/${id}">${esc(title)}</a><p>${esc(intro)}</p></div></li>`).join('')}</ol><h2>继续深入</h2><p>读过具体系统后，可以用本地实践观察记忆的读写过程，或并排查看不同系统的六问答案。人类记忆背景课帮助理解研究中借用的认知术语。</p><div class="reading-links"><a href="#tutorial/topics">专题与实践 →</a><a href="#tutorial/human-memory">人类记忆背景 →</a><a href="#tutorial/compare">并排阅读 →</a></div><p class="note">课程收录 14 篇研究与延伸阅读、15 个工程系统和 10 项评测。各类按已知公开日期排列，原始来源与适用范围随文提供。</p>`;
}
function tutorialLesson() {
  return tutorialHeader('第一课', '用六个问题认识 Memory', '先看一份信息怎样从过去的交互进入下一次调用，再分别回答内容、载体、范围、变化、使用和控制的问题。') +
    `<p>假设你告诉助手“项目使用 Python 3.12”。下一次调用要继续遵守这条约定，系统需要保存合适的内容，在正确的项目范围内把它找回来，并让模型实际看到。项目升级以后，还要避免继续使用旧版本。</p><p>这条过程就是六问的入口。下面逐一说明每个问题在问什么、怎样寻找答案，以及它与其他问题的区别。最后一节给出这套学习清单的来源与推导。</p>` +
    tutorialSectionLinks([...tutorial.questions.map(q => [q.id, q.short]), ['why-six', '为什么是六问']], '#tutorial/lesson') +
    tutorial.questions.map(q => `<section class="lesson-section" id="${esc(q.id)}"><h2>${esc(q.title)}</h2>${tutorialParagraphs(q.what)}${tutorialParagraphs(q.why)}<h3>怎样读一个新系统</h3>${tutorialParagraphs(q.how)}${tutorialExample(q.example)}<p class="check">读完这一问：${esc(q.check)}</p><details class="source-details"><summary>依据与推导</summary>${tutorialParagraphs(q.evidence)}${tutorialParagraphs(q.confidence)}${tutorialSourceLinks(q.sources, true)}</details></section>`).join('') +
    `<section class="lesson-section" id="why-six"><h2>为什么是这六个问题？</h2><p>六问是一份综合不同资料形成的学习清单。要判断它是否合理，需要看原始资料分别解释了什么，再检查哪些区别在合并之后会丢失。</p><h3>研究框架分别讨论内容、承载与变化</h3><p>CoALA 区分工作记忆与长期的情景、语义、程序性记忆；Forms–Functions–Dynamics 分开讨论形式、功能和动态；Foundation Agent Memory 同时分析承载、认知机制、主体与操作。它们采用不同的分类树，却反复要求读者区分信息的用途、表示、归属和变化过程。</p>${tutorialSourceLinks(['coala','survey','foundation-agent-taxonomy-arxiv'], true)}<h3>工程文档补充了调用路径和控制条件</h3><p>LangGraph 把 state、checkpoint 和 store 分开；Claude Code 说明不同范围的指令文件与自动记忆；Graphiti 描述关系、时间和检索。沿文档阅读时，仍然需要分别找到“保存什么、放在哪里、属于谁、怎样更新、如何进入下一次调用”的答案。权限、来源与删除请求还需要单独核对。</p>${tutorialSourceLinks(['langgraph','claude-code','graphiti'], true)}<h3>评测提醒我们区分机制描述与实际结果</h3><p>LongMemEval、LoCoMo 和 MemoryAgentBench 通过任务观察长期交互、检索、更新或冲突处理的结果。仅凭回答正确，通常无法确定内部载体、访问权限或删除传播是否符合要求。因此，六问用于理解设计；能力、成本和安全需要与相应任务及指标一起检查。</p>${tutorialSourceLinks(['longmemeval','locomo-paper','memoryagentbench'], true)}<h3>合并问题会丢掉什么</h3><p>把内容和载体合并，就难以区分一条事实与存放它的文件；把范围和控制合并，就容易混淆“数据归谁”与“谁得到授权”；把更新和使用合并，则无法解释为什么记录已经更正，下一次调用仍然读到旧值。版本、索引、过期时间和审计等更细的问题，可以继续放在各问内部展开。</p><p>由这些观察，我们把主要机制链路组织为六问。它们可以分别回答，但实现上会相互影响。回答完整意味着读者能说明这条链怎样工作、证据在哪里以及什么仍未知，并不保证系统在任何任务中都有效。</p><p class="scope-note">这一归纳的置信度为中等。目前没有学习者实验证明它是唯一最小集合，也没有证明它数学上完全正交或覆盖所有未来系统。遇到无法解释的重要机制时，需要据新证据修订。</p></section><section class="next-reading"><h2>下一课：把相邻概念分清楚</h2><p>有了观察问题，再辨析文档中经常出现的 Context、RAG 和 Checkpoint，之后就可以进入具体研究。</p><a href="#tutorial/concepts">阅读相关概念辨析 →</a></section>`;
}
function tutorialConcepts() {
  return tutorialHeader('第二课', '上下文、记忆和存储，各指什么？', '这些词经常出现在同一个系统里，但描述的是不同环节。沿具体信息的去向阅读，更容易看清它们的关系。') +
    tutorialSectionLinks(tutorial.concepts.map(c => [c.id, c.title]), '#tutorial/concepts') +
    tutorial.concepts.map(c => `<section class="concept-section" id="${esc(c.id)}"><h2>${esc(c.title)}</h2>${tutorialParagraphs(c.what)}${tutorialParagraphs(c.detail)}${tutorialParagraphs(c.confusion)}${tutorialExample(c.example)}<p class="check">读完后可以检查：${esc(c.check)}</p><details class="source-details"><summary>来源与说明</summary>${tutorialParagraphs(c.confidence)}${tutorialSourceLinks(c.sources, true)}</details></section>`).join('') +
    `<section class="next-reading"><h2>接着读研究方法</h2><p>现在已经有了六问，也分清了常见术语。下一步看研究者如何选择其中的机制来解决一个具体问题。</p><a href="#tutorial/research">进入 Research →</a></section>`;
}
function tutorialEntryCard(category, entry) {
  const route = tutorialEntryRoute(category, entry.id);
  return `<article class="entry-row"><div class="entry-meta">${esc(entry.date)} · ${esc(entry.profile?.kind || tutorialCategoryLabel(category))}</div><h2><a href="${route}">${esc(entry.title)}</a></h2>${tutorialParagraphs(entry.summary)}<a class="read-more" href="${route}">阅读详解 →</a></article>`;
}
function tutorialResearchCandidates() {
  if (!tutorial.researchCandidates?.length) return '';
  return `<section><h2>延伸阅读</h2><p>下面的文章进一步讨论记忆结构、图表示、自主控制与经验形成。可以在读过具体方法后，选择感兴趣的方向继续阅读。</p><div class="entry-list">${tutorial.researchCandidates.slice().sort(tutorialPublicationOrder).map(e => tutorialEntryCard('research', e)).join('')}</div></section>`;
}
function tutorialIndex(category) {
  const titles = {research:['第三课','Research：研究者怎样设计记忆'], engineering:['第四课','工程：记忆怎样进入真实系统'], benchmarks:['第五课','Benchmark：怎样知道记忆有没有用'], culture:['第六课','文学与影视中的记忆'], humanMemory:['背景阅读','人类记忆背景']};
  const intros = {
    research:'先看论文要解决的问题和提供的证据，再沿六问分析它的设计。综述用于建立视野，具体方法帮助看清机制怎样运转。',
    engineering:'同样的记忆思路，落实到工程中会变成文件、接口、配置与权限。这里聚焦 Agent、Harness 和独立 Memory 系统的记忆部分。',
    benchmarks:'评测通过任务和评分观察能力，六问帮助解释这些任务与系统设计的关系。先看它给了什么输入、要求什么输出，再判断分数支持多大的结论。',
    culture:'小说与影视让我们思考：当人只能保留有限记忆、依赖外部记录，或无法自主遗忘时，会发生什么？这里只收录真实作品，作品情节与工程类比分开说明。',
    humanMemory:'Agent 研究借用了工作、情景、语义和程序性记忆等词。认识这些术语的人类认知背景，有助于理解类比，也能看清类比的限度。'
  };
  const [chapter, title] = titles[category];
  return tutorialHeader(chapter, title, intros[category]) +
    `<p class="note">按已知首次公开日期由新到旧排列；日期未说明的条目置后。阅读顺序不代表质量排名。</p><div class="entry-list">${tutorialSortedEntries(category).map(e => tutorialEntryCard(category, e)).join('')}</div>` +
    (category === 'research' ? tutorialResearchCandidates() : '') +
    (category === 'benchmarks' ? tutorialBenchmarkViz() : '') +
    (category === 'research' ? `<section class="next-reading"><p>读过研究设计，再看它们在工程中怎样落地。</p><a href="#tutorial/engineering">进入工程实现 →</a></section>` : category === 'engineering' ? `<section class="next-reading"><p>机制怎样工作已经清楚，接着检查它的能力如何被测量。</p><a href="#tutorial/benchmarks">进入 Benchmark →</a></section>` : '');
}
function tutorialProfile(entry) {
  const labels = {kind:'对象类型', authors:'作者', affiliation:'作者署名机构', creator:'创作者', cast:'主演', team:'团队 / 维护者', maintainer:'维护者', venue:'发表 / 发布', artifact:'公开材料', version:'阅读版本'};
  return Object.keys(labels).filter(k => entry.profile?.[k]).map(k => `<div><dt>${labels[k]}</dt><dd>${esc(entry.profile[k])}${k === 'affiliation' ? tutorialSourceLinks(entry.affiliationSources || [], true) : ''}</dd></div>`).join('');
}
function tutorialEvaluation(entry) {
  const labels = {abilities:'测哪些能力', taskProtocol:'任务与数据如何组织', metrics:'怎样评分', designMapping:'与六问有什么关系', limitations:'结果的适用范围'};
  if (!entry.evaluation) return '';
  return `<section class="lesson-section" id="evaluation"><h2>评测设计</h2>${Object.entries(entry.evaluation).filter(([k,v]) => labels[k] && v).map(([k,v]) => `<h3>${labels[k]}</h3>${tutorialParagraphs(v)}`).join('')}</section>`;
}
function tutorialNextReading(entry) {
  const next = {
    engineering:['工程实现','接着看记忆机制怎样落实到真实系统。'],
    benchmarks:['Benchmark','接着看哪些任务和指标能够检验这些机制的效果。'],
    culture:['文学与影视','也可以换一个角度，通过作品思考记忆、遗忘与身份。'],
    'human-memory':['人类记忆背景','再读认知研究中的相关概念，分清作品类比与研究结论。'],
    topics:['专题与实践','接着把理解转成具体检查，观察一条记忆怎样保存和使用。']
  }[entry.next];
  return next ? `<p>${esc(next[1])} <a href="#tutorial/${esc(entry.next)}">${esc(next[0])} →</a></p>` : '';
}
function tutorialDetail() {
  const category = state.tutorialCategory;
  const entry = tutorialEntryBy(category, state.tutorialEntry);
  if (!entry) return `${crumbs('页面不存在')}<h1>找不到这个条目</h1><p>请从对应课程列表选择文章。</p><a href="#tutorial">回到课程首页 →</a>`;
  const route = tutorialEntryRoute(category, entry.id);
  const sections = tutorial.questions.map(q => [q.id, q.short]);
  return `${crumbs(entry.title, category)}<p class="eyebrow">${esc(tutorialReadingLabel(entry, category))}</p><h1>${esc(entry.title)}</h1>${tutorialParagraphs(entry.summary, 'lead')}<dl class="metadata"><div><dt>类别</dt><dd>${esc(tutorialCategoryLabel(category))}</dd></div><div><dt>首次公开日期</dt><dd>${esc(entry.date)}</dd></div><div><dt>原始来源</dt><dd><a href="${esc(entry.canonicalUrl)}" target="_blank" rel="noopener noreferrer">${esc(entry.canonicalUrl)} ↗</a></dd></div>${tutorialProfile(entry)}<div><dt>资料核对日期</dt><dd>${esc(entry.checkedAt)}</dd></div></dl><section class="selection"><h2>为什么读这篇</h2>${tutorialParagraphs(entry.why)}${tutorialParagraphs(entry.selectionEvidence)}<div class="scope-note">${tutorialParagraphs(entry.boundary)}</div></section>${entry.caseStudy ? `<section><h2>本页案例</h2>${tutorialParagraphs(entry.caseStudy)}</section>` : ''}${category === 'benchmarks' ? '<p>下面仍沿六问阅读，但回答指向这个评测要求或观察到的受测系统行为。具体任务与评分在后文单独展开。</p>' : ''}${tutorialSectionLinks([...sections, ...(entry.evaluation ? [['evaluation','评测设计']] : []), ['sources','原始资料']], route)}${entry.questions.map((a,i) => `<section class="question-section" id="${tutorial.questions[i].id}"><h2>${esc(tutorial.questions[i].title)}</h2>${tutorialParagraphs(a.answer, 'answer')}${tutorialParagraphs(a.why)}${tutorialExample(a.example)}<details class="source-details"><summary>依据与出处</summary>${tutorialParagraphs(a.trace)}${a.sources?.length ? tutorialSourceLinks(a.sources, true) : `<a href="${esc(entry.canonicalUrl)}" target="_blank" rel="noopener noreferrer">回到原始来源 ↗</a>`}</details></section>`).join('')}${tutorialEvaluation(entry)}<section class="lesson-section" id="limits"><h2>读完以后</h2>${tutorialParagraphs(entry.limitations)}${tutorialNextReading(entry)}${entry.realityNote ? `<p class="scope-note">${esc(entry.realityNote)}</p>` : ''}<div class="actions"><a href="${tutorialCategoryRoute(category)}">返回${esc(tutorialCategoryLabel(category))}列表 →</a>${tutorialComparisonCategories.includes(category) ? `<button type="button" data-tutorial-add-to-compare="${esc(category)}:${esc(entry.id)}">放入并排阅读</button>` : ''}</div></section><section class="lesson-section" id="sources"><h2>原始资料</h2>${tutorialSourceLinks([...entry.sources, ...(entry.affiliationSources || [])])}</section>`;
}
function tutorialBenchmarkViz() {
  const qs = tutorial.questions;
  return `<section class="lesson-section" id="benchmark-map"><h2>这些评测与六问有什么关系？</h2><p>这张表标记评测的任务或资料涉及哪些观察方向。它帮助定位要读的部分，不代表评测验证了这一方向的全部机制。“未标注”也不表示被测系统没有该能力。</p><div class="table-scroll" tabindex="0" role="region" aria-label="可横向滚动的评测对应表"><table class="matrix"><caption class="sr-only">Benchmark 与六问的资料关联</caption><thead><tr><th scope="col">Benchmark</th>${qs.map(q => `<th scope="col">${esc(q.short)}</th>`).join('')}</tr></thead><tbody>${tutorialSortedEntries('benchmarks').map(e => `<tr><th scope="row"><a href="${tutorialEntryRoute('benchmarks', e.id)}">${esc(e.title.split(' · ')[0])}</a></th>${qs.map(q => `<td class="${e.coverage?.includes(q.id) ? 'related' : 'unmarked'}">${e.coverage?.includes(q.id) ? '涉及' : '未标注'}</td>`).join('')}</tr>`).join('')}</tbody></table></div></section>`;
}
function tutorialCompare() {
  const all = [];
  for(const category of tutorialComparisonCategories) for(const entry of tutorialReadings(category)) all.push({...entry, category});
  const chosen = all.filter(e => state.tutorialCompare.includes(e.id));
  const picker = `<fieldset class="compare-picker"><legend>选择要并排阅读的条目</legend>${tutorialComparisonCategories.map(category => `<details data-compare-group="${category}"${category === 'research' ? ' open' : ''}><summary>${esc(tutorialCategoryLabel(category))}</summary><div class="picker-options">${all.filter(e => e.category === category).sort(tutorialPublicationOrder).map(e => `<label><input type="checkbox" data-tutorial-compare="${esc(e.id)}" ${state.tutorialCompare.includes(e.id) ? 'checked' : ''}>${esc(e.title)}</label>`).join('')}</div></details>`).join('')}</fieldset>`;
  const width = Math.max(46, 10 + chosen.length * 19);
  const table = chosen.length >= 2 ? `<div class="table-scroll" tabindex="0" role="region" aria-label="可横向滚动的六问答案对照"><table class="compare-table" style="min-width:${width}rem"><caption class="sr-only">所选条目的六问答案</caption><thead><tr><th scope="col">问题</th>${chosen.map(e => `<th scope="col"><a href="${tutorialEntryRoute(e.category,e.id)}">${esc(e.title)}</a><small>${esc(tutorialReadingLabel(e,e.category))}</small></th>`).join('')}</tr></thead><tbody>${tutorial.questions.map((q,i) => `<tr><th scope="row">${esc(q.title)}</th>${chosen.map(e => `<td>${tutorialParagraphs(e.questions[i].answer)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>` : '<p>选择至少两个条目后，这里会显示六问答案对照。</p>';
  return tutorialHeader('阅读工具','并排看六问答案','读过具体条目后，再选择两篇或更多文章，逐问看它们怎样回答。这里展示已有答案，帮助你自己判断差异。') + picker + `<p class="note">已选择 ${chosen.length} 个条目。Benchmark 解释评测范围；文学影视仅作类比，不能据此比较系统性能。</p>` + table;
}
function tutorialTopics() {
  const flow = [['输入与出处','先知道这条信息来自哪次对话或哪个工具。'],['筛选并写入','决定是否保存，以及保留原文还是提取事实。'],['保存与更新','更正旧记录，保留需要的来源与版本。'],['按范围检索','在适当的用户或项目范围内查找相关内容。'],['组装调用材料','把选出的记录交给下一次调用，再观察它是否被正确使用。']];
  return tutorialHeader('继续深入','从理解机制到动手检查','读过具体系统后，沿安全、成本和评测继续深入，再用本地例子观察一次记忆的完整读写过程。') + tutorialSectionLinks(tutorial.topics.map(t => [t.id,t.title]), '#tutorial/topics') + `<h2>先沿一条记忆走一遍</h2><ol class="flow">${flow.map(([label,text]) => `<li><div><strong>${label}</strong><span>${text}</span></div></li>`).join('')}</ol><p>保存成功、召回正确和任务完成，是三个需要分别观察的结果。下面的专题围绕这条过程展开。</p>` + tutorial.topics.map(t => `<section class="lesson-section" id="${esc(t.id)}"><h2>${esc(t.title)}</h2>${tutorialParagraphs(t.intro)}${t.sections.map(s => `<h3>${esc(s.title)}</h3>${tutorialParagraphs(s.text)}${tutorialExample(s.example)}<p class="check">检查方法：${esc(s.check)}</p><details class="source-details"><summary>来源</summary>${tutorialSourceLinks(s.sources, true)}</details>`).join('')}${t.guideUrl ? `<div class="reading-links"><a href="${esc(t.guideUrl)}" target="_blank" rel="noopener noreferrer">实践步骤与六问解释 ↗</a><a href="${esc(t.codeUrl)}" target="_blank" rel="noopener noreferrer">示例源码 ↗</a></div>` : ''}</section>`).join('');
}
function tutorialAbout() {
  return tutorialHeader('阅读说明','怎样使用本教程的资料','每篇文章先说明它是什么、为什么值得读，再用六问解释设计。具体结果必须连同来源、版本和实验条件一起看。') + `<h2>收录与排序</h2><p>课程选择能说明不同机制、且有原始资料可核对的研究、工程系统和评测。发表情况、作者团队与时效性帮助判断阅读价值；机构声望或关注度不能单独证明方法有效。条目按已知首次公开日期排列，日期未说明的置后。</p><h2>怎样阅读证据</h2><p>论文中的实验结果属于作者报告，官方文档描述的是其公开接口与行为。教程不会把这些材料写成已经独立复现的结论。每问后的“依据与出处”提供具体章节和原始链接，条目末尾集中列出完整资料。</p><p>例子注明教学构造时，人物、项目和输入用于解释机制，并非原始评测样本，也不是本仓库运行得到的结果。资料未说明某项功能时，会明确保留未知，不能由此认定系统不支持它。</p><h2>六问与评测的关系</h2><p>六问组织的是理解系统所需的问题。Benchmark 观察能力与任务结果；仅凭得分不能确定系统采用了哪一种载体、权限或删除机制。请结合每项评测的任务、输入、指标和限制阅读。</p><h2>作品与认知类比</h2><p>文学影视均为真实作品。作品情节、教学类比和工程事实分别标注；人类记忆研究用于解释术语背景，不直接证明 Agent 的设计正确。</p><p><a href="https://github.com/dongshuyan/awesome-harness-memory/blob/master/docs/coverage.md" target="_blank" rel="noopener noreferrer">查看课程范围与证据说明 ↗</a></p>`;
}
