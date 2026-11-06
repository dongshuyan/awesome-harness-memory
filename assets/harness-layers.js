(() => {
  'use strict';
  const root = document.getElementById('memory-colored-layers');
  const data = JSON.parse(document.getElementById('harness-map-data').textContent);
  const q = s => root.querySelector(s);
  const dims = data.dimensions, systems = data.systems;
  const names = {yes:'文档明确说明', config:'需配置 / 特定条件', unknown:'尚未核实', no:'该范围明确不提供'};
  const symbols = {yes:'✓', config:'△', unknown:'?', no:'×'};
  const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const state = {layers:dims.map((_,i)=>i), visible:systems.map(s=>s.id), system:'all', view:'layers', angle:-3, gap:100};
  const visibleSystems = () => systems.filter(s => state.visible.includes(s.id));
  const cell = (s, property) => s.claims.find(c=>c.features.includes(property)) || {status:'unknown', note:'当前资料尚不足以确认这一属性；不能据此判断不支持。'};
  const label = s => s.name + (s.historical ? '（历史）' : '');
  const sourceLink = (id, text) => `<a href="${esc(data.sources[id].url)}" target="_blank" rel="noopener noreferrer">${esc(text || data.sources[id].label)} ↗</a>`;
  let evidenceRequested = false;
  // The standalone host grows the iframe to its content height. Position dialogs
  // inside the visible part of that frame, not the centre of the entire document.
  window.addEventListener('message', event => {
    if (!evidenceRequested || event.source !== window.parent || event.data?.type !== 'harness:viewport') return;
    const {top, height} = event.data;
    if (!Number.isFinite(top) || !Number.isFinite(height) || height <= 0) return;
    const dialog = q('#cl-evidence');
    dialog.style.maxHeight = Math.max(100, height - 32) + 'px';
    if (!dialog.open) {
      dialog.style.top = top + 16 + 'px';
      dialog.showModal();
      window.parent.postMessage({type:'harness:dialog-shown'}, '*');
    }
    dialog.style.top = top + Math.max(16, (height - dialog.getBoundingClientRect().height) / 2) + 'px';
  });
  q('#cl-evidence').addEventListener('close', () => {
    evidenceRequested = false;
    window.parent.postMessage({type:'harness:dialog', open:false}, '*');
  });
  q('#cl-subtitle').textContent = `${systems.length} 个真实 Harness / Agent · 7 个视角 · ${systems.filter(s=>s.historical).length} 个历史项目已标记 · ${data.checked}。${data.scope}`;
  q('#cl-layer-controls').innerHTML = dims.map((d,i)=>`<label class="form-check"><input type="checkbox" data-layer="${i}" checked><span>${i+1} ${esc(d.name)}</span></label>`).join('');
  q('#cl-object-controls').innerHTML = systems.map(s=>`<label class="form-check" title="${esc(s.note)}"><input type="checkbox" data-object="${esc(s.id)}" checked><span>${esc(label(s))}</span></label>`).join('');
  q('#cl-system').innerHTML = '<option value="all">全部对象，不单独高亮</option>' + systems.map(s=>`<option value="${esc(s.id)}">${esc(label(s))}</option>`).join('');

  function showEvidence(systemId, property) {
    const s = systems.find(x=>x.id===systemId);
    const dim = dims.find(d=>d.options.some(o=>o.id===property));
    const option = dim.options.find(o=>o.id===property), c = cell(s, property);
    q('#cl-evidence-title').textContent = `${s.name} · ${option.name}`;
    q('#cl-evidence-body').innerHTML = `<p><span class="cl-chip" data-status="${c.status}">${symbols[c.status]}</span> <strong>${names[c.status]}</strong></p><p>${esc(c.note)}</p><dl><dt>这一属性指什么</dt><dd>${esc(option.definition)}</dd><dt>对象与配置范围</dt><dd>${esc(s.note)}</dd><dt>${c.source ? '判断依据' : '对象资料（尚不能证明该属性）'}</dt><dd>${sourceLink(c.source || s.identitySource)}${c.source ? `<br>${esc(c.section)} · ${esc(data.sources[c.source].kind)} · 核对 ${esc(data.sources[c.source].checked)}` : ''}</dd></dl><p class="text-small">图中为公开资料的属性映射，未运行这些系统或验证效果。各项可以重叠，不按色块数量排名。</p>`;
    evidenceRequested = true;
    window.parent.postMessage({type:'harness:dialog', open:true}, '*');
  }

  let lastWidth = 0;
  function draw() {
    const svg = q('#cl-scene'), shown = visibleSystems();
    const viewport = Math.max(250, q('#cl-scroll').clientWidth); lastWidth = viewport;
    const width = Math.max(viewport, 185 + shown.length * 132);
    const front = state.view==='front', theta=(front?0:state.angle)*Math.PI/180;
    const co=Math.cos(theta), si=Math.sin(theta), elevation=front?1:.62;
    const rowDepth=36, planeDepth=rowDepth*Math.max(...dims.map(d=>d.options.length));
    const planeWidth=(width-175-Math.abs(si)*planeDepth)/co, cellWidth=planeWidth/Math.max(1,shown.length);
    const project=(x,y)=>[x*co-y*si,(x*si+y*co)*elevation];
    const corners=[[0,0],[planeWidth,0],[planeWidth,planeDepth],[0,planeDepth]].map(([x,y])=>project(x,y));
    const minX=Math.min(...corners.map(p=>p[0])), minY=Math.min(...corners.map(p=>p[1]));
    const planeHeight=Math.max(...corners.map(p=>p[1]))-minY;
    const gap=front?planeHeight+75:32+(planeHeight+75-32)*state.gap/100;
    const compact=!front&&gap<planeHeight+55, top=70-minY, originX=150-minX;
    const pos=(x,y,k)=>{const p=project(x,y);return [originX+p[0],top+p[1]+k*gap];};
    const points=ps=>ps.map(p=>p.map(v=>v.toFixed(2)).join(',')).join(' ');
    const height=state.layers.length&&shown.length?Math.ceil(planeHeight+(state.layers.length-1)*gap+100):95;
    svg.setAttribute('viewBox',`0 0 ${width} ${height}`); svg.style.width=`${width}px`; svg.style.height=`${height}px`;
    let markup='<title id="cl-scene-title">真实 Harness 与 Agent 的记忆属性</title><desc id="cl-scene-description">列为真实对象，层为研究视角，行是属性。点击格子查看来源；下方有可用键盘操作的文字对照。</desc>';
    if (!shown.length || !state.layers.length) {
      svg.innerHTML=markup+`<text x="12" y="38">${!shown.length?'请勾选至少一个对比对象。':'请选择至少一个维度层。'}</text>`; return;
    }
    const focusIndex=shown.findIndex(s=>s.id===state.system);
    if (!front&&state.layers.length>1&&focusIndex>=0) {
      const a=pos((focusIndex+.5)*cellWidth,planeDepth/2,0),b=pos((focusIndex+.5)*cellWidth,planeDepth/2,state.layers.length-1);
      markup+=`<line class="track" x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}"/>`;
    }
    for(let k=state.layers.length-1;k>=0;k--) {
      const d=state.layers[k],dim=dims[d],sheet=[[0,0],[planeWidth,0],[planeWidth,planeDepth],[0,planeDepth]].map(([x,y])=>pos(x,y,k));
      markup+=`<g data-layer-index="${d}"><polygon class="sheet" points="${points(sheet)}"/>`;
      shown.forEach((s,i)=>dim.options.forEach((o,j)=>{
        const c=cell(s,o.id),x0=i*cellWidth+2,x1=(i+1)*cellWidth-2,y0=j*rowDepth+2,y1=(j+1)*rowDepth-2;
        const shape=[[x0,y0],[x1,y0],[x1,y1],[x0,y1]].map(([x,y])=>pos(x,y,k)),center=pos((i+.5)*cellWidth,(j+.5)*rowDepth,k);
        markup+=`<g class="cl-cell" data-system="${esc(s.id)}" data-property="${o.id}"><title>${esc(`${s.name} · ${o.name}：${names[c.status]}。点击查看依据`)}</title><polygon class="status-cell" data-status="${c.status}" points="${points(shape)}"/><text class="cell-symbol" x="${center[0]}" y="${center[1]+4.5}" text-anchor="middle">${symbols[c.status]}</text></g>`;
      }));
      if(focusIndex>=0) {
        const i=focusIndex,outline=[[i*cellWidth,0],[(i+1)*cellWidth,0],[(i+1)*cellWidth,planeDepth],[i*cellWidth,planeDepth]].map(([x,y])=>pos(x,y,k));
        markup+=`<polygon class="selected-column" points="${points(outline)}"/>`;
      }
      markup+='</g>';
    }
    state.layers.forEach((d,k)=>{
      const dim=dims[d]; markup+=`<text class="layer-title" x="8" y="${k*gap+25}">${d+1} ${esc(dim.name)}</text>`;
      if(!compact||k===0) shown.forEach((s,i)=>{
        const p=pos((i+.5)*cellWidth,-32,k), words=s.name.split(' ');
        let lines=[s.name];
        if(s.name.length>15&&words.length>1) lines=[words.slice(0,-1).join(' '),words.at(-1)];
        if(s.historical)lines.push('历史项目');
        markup+=`<text class="system-label ${state.system===s.id?'selected':''}" x="${p[0]}" y="${p[1]}" text-anchor="middle">${lines.map((line,n)=>`<tspan x="${p[0]}" dy="${n?15:0}">${esc(line)}</tspan>`).join('')}</text>`;
      });
      if(!compact) dim.options.forEach((o,j)=>{const p=pos(-10,(j+.5)*rowDepth,k);markup+=`<text x="${p[0]}" y="${p[1]+4.5}" text-anchor="end">${esc(o.name)}</text>`;});
    });
    svg.innerHTML=markup;
  }
  function renderData() {
    const shown=visibleSystems();
    q('#cl-data').innerHTML=state.layers.map(d=>`<section><h3>${d+1} ${esc(dims[d].name)}</h3><div class="table-responsive"><table><caption class="sr-only">${esc(dims[d].name)}：点击状态查看依据</caption><thead><tr><th scope="col">属性</th>${shown.map(s=>`<th scope="col">${esc(label(s))}</th>`).join('')}</tr></thead><tbody>${dims[d].options.map(o=>`<tr><th scope="row">${esc(o.name)}</th>${shown.map(s=>{const c=cell(s,o.id);return `<td><button class="cl-chip" data-system="${esc(s.id)}" data-property="${o.id}" data-status="${c.status}" aria-label="${esc(`${s.name}，${o.name}，${names[c.status]}，查看依据`)}">${symbols[c.status]}</button></td>`;}).join('')}</tr>`).join('')}</tbody></table></div></section>`).join('');
  }
  function render() {
    const shown=visibleSystems();
    q('#cl-system').value=state.system; q('#cl-view').value=state.view;
    q('#cl-angle').value=state.angle; q('#cl-gap').value=state.gap;
    q('#cl-angle').disabled=q('#cl-gap').disabled=state.view==='front';
    q('#cl-angle-value').textContent=state.angle+'°'; q('#cl-gap-value').textContent=state.gap===100?'展开':state.gap===0?'合拢':state.gap+'%';
    root.querySelectorAll('[data-object]').forEach(input=>input.checked=state.visible.includes(input.dataset.object));
    const selected=systems.find(s=>s.id===state.system);
    q('#cl-readout').textContent=`显示 ${shown.length}/${systems.length} 个对象 · ${state.layers.length}/7 层${selected?` · ${selected.name} 已加框`:''}${state.view==='layers'&&state.gap<100?' · 重叠时可拉开层间距或切换正视':''}`;
    q('#cl-object-count').textContent=`选择对比对象（${shown.length}/${systems.length}）`;
    q('#cl-object-note').innerHTML=selected?`<strong>${esc(label(selected))}</strong>：${esc(selected.note)} ${sourceLink(selected.identitySource,'对象原始资料')}`:'默认包含全部已定位对象。可先取消全选，再勾选要对比的几项；历史项目不作为当前维护推荐。';
    renderData(); draw();
  }
  root.addEventListener('change',e=>{
    if(e.target.hasAttribute('data-layer')){const i=Number(e.target.dataset.layer);state.layers=e.target.checked?[...state.layers,i].sort((a,b)=>a-b):state.layers.filter(x=>x!==i);}
    else if(e.target.hasAttribute('data-object')){const id=e.target.dataset.object;state.visible=e.target.checked?[...state.visible,id]:state.visible.filter(x=>x!==id);if(state.system===id&&!e.target.checked)state.system='all';}
    else if(e.target.id==='cl-system'){state.system=e.target.value;if(state.system!=='all'&&!state.visible.includes(state.system))state.visible.push(state.system);}
    else if(e.target.id==='cl-view')state.view=e.target.value;
    else return;
    render();
    if(e.target.id==='cl-system'&&state.system!=='all') {
      const i=visibleSystems().findIndex(s=>s.id===state.system); q('#cl-scroll').scrollLeft=Math.max(0,150+i*132-q('#cl-scroll').clientWidth/2);
    }
  });
  root.addEventListener('click',e=>{
    const c=e.target.closest('[data-system][data-property]');
    if(c){showEvidence(c.dataset.system,c.dataset.property);return;}
    if(e.target.id==='cl-close-evidence')q('#cl-evidence').close();
    if(e.target.id==='cl-select-all'||e.target.id==='cl-select-none'){
      state.visible=e.target.id==='cl-select-all'?systems.map(s=>s.id):[];state.system='all';render();
    }
  });
  ['angle','gap'].forEach(key=>q('#cl-'+key).addEventListener('input',e=>{
    state[key]=Number(e.target.value);q('#cl-'+key+'-value').textContent=key==='angle'?state.angle+'°':state.gap===100?'展开':state.gap===0?'合拢':state.gap+'%';draw();
  }));
  new ResizeObserver(()=>{if(Math.abs(q('#cl-scroll').clientWidth-lastWidth)>.5)draw();}).observe(q('#cl-scroll'));
  render();
})();
