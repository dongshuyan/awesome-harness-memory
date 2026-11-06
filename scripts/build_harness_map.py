#!/usr/bin/env python3
"""Embed the reviewed Harness profiles and regenerate the README preview (stdlib only)."""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def cell(system, property_id):
    return next((c for c in system['claims'] if property_id in c['features']), {'status': 'unknown'})


def script_json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')


def compiled_data(root):
    data = json.loads((root / 'assets/harness-map.json').read_text())
    resources = {r['id']: r for r in json.loads((root / 'catalogue.json').read_text())['resources']}
    properties = {o['id'] for d in data['dimensions'] for o in d['options']}
    ids = set()
    for system in data['systems']:
        if system['id'] in ids or system['resourceId'] not in resources:
            raise ValueError('Duplicate profile or missing catalogue reference: ' + system['id'])
        ids.add(system['id'])
        system['name'] = system.get('displayName', resources[system['resourceId']]['title'])
        if system['kind'] not in ('agent', 'harness') or system['identitySource'] not in data['sources']:
            raise ValueError('Profile needs a Harness/Agent identity source: ' + system['id'])
        assigned = set()
        for claim in system['claims']:
            if claim['status'] not in ('yes', 'no', 'config', 'unknown') or claim['source'] not in data['sources']:
                raise ValueError('Invalid claim: ' + system['id'])
            if not claim['note'] or not claim['section'] or assigned.intersection(claim['features']) or not set(claim['features']) <= properties:
                raise ValueError('Missing evidence or conflicting property: ' + system['id'])
            assigned.update(claim['features'])
    for source in data['sources'].values():
        if not source['url'].startswith('https://'):
            raise ValueError('Only HTTPS source links are supported')
    return data


BLOCK = '''<section id="kn-layers-host" hidden>
<div id="memory-colored-layers" lang="zh-CN">
  <style id="harness-layers-style">__CSS__</style>
  <div class="cl-stack">
    <div class="cl-heading"><h2>Harness / Agent 的真实记忆组合</h2><span id="cl-subtitle" class="text-small"></span></div>
    <div class="cl-legend text-small" aria-label="颜色与符号图例">
      <span class="cl-key"><span class="cl-chip" data-status="yes">✓</span>文档明确说明</span>
      <span class="cl-key"><span class="cl-chip" data-status="config">△</span>需配置 / 特定条件</span>
      <span class="cl-key"><span class="cl-chip" data-status="unknown">?</span>尚未核实</span>
      <span class="cl-key"><span class="cl-chip" data-status="no">×</span>该范围明确不提供</span>
    </div>
    <p class="text-small">图中包括会话上下文和持久记忆，两者按属性区分。点击格子查看定义、条件和来源；问号不表示不支持，色块数量不代表效果或质量。</p>
    <details><summary id="cl-object-count">选择对比对象</summary><div id="cl-object-controls" class="cl-object-controls"></div><button type="button" id="cl-select-all">全选</button> <button type="button" id="cl-select-none">取消全选</button></details>
    <div class="cl-stack"><span>显示哪些层（可多选）</span><div id="cl-layer-controls" class="cl-layer-controls" role="group" aria-label="显示哪些维度"></div></div>
    <div class="cl-field-grid">
      <div class="cl-field"><label for="cl-system">跨层高亮对象</label><select id="cl-system"></select></div>
      <div class="cl-field"><label for="cl-view">看图角度</label><select id="cl-view"><option value="layers">立体分层</option><option value="front">正视展开</option></select></div>
      <div class="cl-field"><label for="cl-angle">转向 <span id="cl-angle-value">−3°</span></label><input id="cl-angle" type="range" min="-20" max="20" step="1" value="-3"></div>
      <div class="cl-field"><label for="cl-gap">层间距 <span id="cl-gap-value">展开</span></label><input id="cl-gap" type="range" min="0" max="100" step="1" value="100"></div>
    </div>
    <p id="cl-object-note" class="text-small"></p>
    <span id="cl-readout" class="text-small" aria-live="polite"></span>
    <p class="text-small">左右滑动查看全部对象；每层的对象顺序相同。可先勾选几个对象，再比较它们的七层组合。</p>
    <div id="cl-scroll" class="cl-scroll" tabindex="0" role="region" aria-label="记忆切片，左右滚动查看更多对象"><svg id="cl-scene" class="cl-scene" role="img" aria-labelledby="cl-scene-title cl-scene-description"></svg></div>
    <details id="cl-details"><summary>查看各层文字对照与来源（支持键盘）</summary><div id="cl-data" class="cl-data"></div></details>
    <dialog id="cl-evidence" aria-labelledby="cl-evidence-title"><button type="button" id="cl-close-evidence" autofocus>关闭</button><h3 id="cl-evidence-title"></h3><div id="cl-evidence-body"></div></dialog>
  </div>
</div>
</section>'''


class PageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'iframe' and attrs.get('id') == 'codex-visualization':
            self.inner = attrs['data-srcdoc']


VIEWPORT_BRIDGE = '''<script id="harness-viewport-bridge">
(() => {
  const frame = document.getElementById('codex-visualization');
  let active = false, pending = false, scrollBeforeDialog = [0, 0];
  function sendViewport() {
    pending = false;
    if (!active) return;
    const rect = frame.getBoundingClientRect();
    frame.contentWindow.postMessage({type:'harness:viewport', top:Math.max(0, -rect.top), height:Math.max(0, Math.min(innerHeight, rect.bottom) - Math.max(0, rect.top))}, '*');
  }
  window.addEventListener('message', event => {
    if (event.source !== frame.contentWindow) return;
    if (event.data?.type === 'harness:dialog-shown' && active) {
      window.scrollTo(...scrollBeforeDialog);
      sendViewport();
      return;
    }
    if (event.data?.type !== 'harness:dialog') return;
    active = event.data.open === true;
    if (active) scrollBeforeDialog = [scrollX, scrollY];
    sendViewport();
  });
  function update() {
    if (active && !pending) {pending = true; requestAnimationFrame(sendViewport);}
  }
  window.addEventListener('scroll', update, {passive:true});
  window.addEventListener('resize', update);
})();
</script>'''


def page(root, data):
    outer = (root / 'index.html').read_text()
    parser = PageParser()
    parser.feed(outer)
    inner = parser.inner
    block = BLOCK.replace('__CSS__', (root / 'assets/harness-layers.css').read_text().strip())
    inner, n = re.subn(r'<section id="kn-layers-host" hidden>.*?</section>', lambda _: block, inner, count=1, flags=re.S)
    if n != 1:
        raise ValueError('Missing chart host')
    scripts = '<script id="harness-map-data" type="application/json">' + script_json(data) + '</script>\n<script id="harness-layers-script">\n' + (root / 'assets/harness-layers.js').read_text().strip() + '\n</script>'
    if '<script id="harness-map-data"' in inner:
        pattern = r'<script id="harness-map-data".*?</script>\s*<script id="harness-layers-script">.*?</script>'
    else:
        pattern = r"<script>\s*\(\(\) => \{\s*const root=document.getElementById\('memory-colored-layers'\);.*?</script>"
    inner, n = re.subn(pattern, lambda _: scripts, inner, count=1, flags=re.S)
    if n != 1:
        raise ValueError('Missing chart script')
    outer = re.sub(r'data-srcdoc="[^"]*"', lambda _: 'data-srcdoc="' + html.escape(inner, quote=True) + '"', outer, count=1)
    if '<script id="harness-viewport-bridge">' in outer:
        return re.sub(r'<script id="harness-viewport-bridge">.*?</script>', lambda _: VIEWPORT_BRIDGE, outer, count=1, flags=re.S)
    if outer.count('</body>') != 1:
        raise ValueError('Expected one outer body')
    return outer.replace('</body>', VIEWPORT_BRIDGE + '\n</body>')


def preview(data):
    """A clearly labelled subset preview; the interactive graph includes every profile."""
    selected = ['pi', 'codex', 'claude-code', 'openclaw', 'hermes', 'deep-agents']
    systems = [next(s for s in data['systems'] if s['id'] == id) for id in selected]
    dims = data['dimensions'][:3]
    colors = {'yes': '#a8d0c0', 'config': '#edd19a', 'unknown': '#e4e7e4', 'no': '#e6bbb5'}
    symbols = {'yes': '✓', 'config': '△', 'unknown': '?', 'no': '×'}
    pieces = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="920" viewBox="0 0 1080 920" role="img" aria-labelledby="title desc"><title id="title">真实 Harness 与 Agent 记忆切片</title><desc id="desc">{len(systems)} 个真实对象与 {len(dims)} 个视角的静态预览；完整 {len(data["systems"])} 个对象与 {len(data["dimensions"])} 个视角见交互页。状态来自公开文档，不是性能排名。</desc><style>text{{font-family:system-ui,PingFang SC,Microsoft YaHei,sans-serif;fill:#23332e;font-size:14px}}.heading{{font-weight:650;font-size:23px}}.label{{font-weight:600}}</style><rect width="1080" height="920" fill="#f8f9f6"/><text x="28" y="40" class="heading">真实 Harness / Agent · 记忆切片</text>', f'<text x="28" y="68">静态预览：{len(systems)} / {len(data["systems"])} 个真实对象 · {len(dims)} / {len(data["dimensions"])} 个视角 · 完整对照与逐格来源见交互页</text>']
    for i, (key, name) in enumerate([('yes', '文档明确说明'), ('config', '需配置 / 特定条件'), ('unknown', '尚未核实'), ('no', '该范围明确不提供')]):
        x = 28 + i * 260
        pieces.append(f'<rect x="{x}" y="88" width="23" height="23" rx="3" fill="{colors[key]}"/><text x="{x+11.5}" y="105" text-anchor="middle">{symbols[key]}</text><text x="{x+31}" y="105">{name}</text>')
    for k, dim in enumerate(dims):
        y = 166 + k * 235
        pieces.append(f'<text x="28" y="{y}" class="label">{k+1} {html.escape(dim["name"])}</text>')
        for j, option in enumerate(dim['options']):
            row_y = y + 36 + j * 30
            pieces.append(f'<text x="153" y="{row_y+14}" text-anchor="end">{html.escape(option["name"])}</text>')
            for i, system in enumerate(systems):
                x = 168 + i * 145 + j * 3
                dy = -i * 5
                c = cell(system, option['id'])
                points = f'{x},{row_y+dy} {x+138},{row_y+dy-5} {x+141},{row_y+dy+21} {x+3},{row_y+dy+26}'
                pieces.append(f'<polygon points="{points}" fill="{colors[c["status"]]}"/><text x="{x+70}" y="{row_y+dy+17}" text-anchor="middle">{symbols[c["status"]]}</text>')
        for i, system in enumerate(systems):
            pieces.append(f'<text x="{237+i*145}" y="{y+24-i*5}" text-anchor="middle">{html.escape(system["name"])}</text>')
    pieces += ['<text x="28" y="833">范围：当前目录中已定位的 Harness / Agent，非全行业清单；历史项目在交互图中标记。</text>', '<text x="28" y="865">问号不表示不支持；色块数量不代表效果。Codex 自动记忆需启用；Deep Agents 的持久记忆依配置。</text>', f'<text x="28" y="892">核对日期 {data["checked"]} · 点击图片进入完整交互页</text></svg>']
    return '\n'.join(pieces) + '\n'


def generated_files(root=ROOT):
    data = compiled_data(root)
    return {root / 'index.html': page(root, data), root / 'assets/memory-layers.svg': preview(data)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for path, text in generated_files().items():
        if args.check:
            if path.read_text() != text:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(text)
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    print('Harness graph and README preview: ' + ('in sync' if args.check else 'generated'))


if __name__ == '__main__':
    main()
