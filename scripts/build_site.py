#!/usr/bin/env python3
"""Build the public navigator and Markdown learning guide from authoritative sources."""
import argparse
import html
import importlib.util
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('harness_builder', ROOT / 'scripts/build_harness_map.py')
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)


def validate(data, catalogue):
    ids = {r['id'] for r in catalogue['resources']}
    if len(ids) != len(catalogue['resources']):
        raise ValueError('Duplicate catalogue IDs')
    all_sources = [*data['sources'].values(), *[s for r in catalogue['resources'] for s in r['sources']]]
    for source in all_sources:
        parsed = urlsplit(source['url'])
        if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('Expected HTTPS source')
    for item in [*data['types'].values(), *data['terms'].values(), *data['topics'], *[m for t in data['topics'] for m in t['methods']]]:
        if not set(item.get('resources', [])) <= ids or not set(item['sources']) <= set(data['sources']):
            raise ValueError('Unresolved resource or source reference')
    for topic in data['topics']:
        if len({m['id'] for m in topic['methods']}) != len(topic['methods']):
            raise ValueError('Duplicate method IDs')


def markdown(data, catalogue):
    records = {r['id']: r for r in catalogue['resources']}
    def sources(ids):
        return '；'.join(f'[{data["sources"][i]["label"]}]({data["sources"][i]["url"]})' for i in dict.fromkeys(ids))
    lines = ['# 记忆分类与方法导航', '', '从九个问题学习记忆系统。分类树按来源展示；工程叫法允许重叠。九问是编者导航，不声称唯一、穷尽或完全正交。', '', '[打开交互页面](https://dongshuyan.com/awesome-harness-memory/) · [资源目录](../README.zh-CN.md#从具体对象开始)', '']
    lines += [f'- [{t["title"]} · {t["en"]}](#{t["id"]})' for t in data['topics']]
    for t in data['topics']:
        lines += ['', f'<a id="{t["id"]}"></a>']
        lines += [f'<a id="{old}"></a>' for old,new in data['aliases'].items() if new==t['id']]
        lines += ['',f'## {t["title"]} / {t["en"]}', '', t['intro'], '', t['enIntro'], '', t['boundary'], '']
        if t['id']=='types':
            lines += ['CoALA 分类：工作记忆；长期记忆下分情景、语义、程序性记忆。功能分类来自另一篇综述：工作、事实、经验记忆。这两套分类分别展示，不合成一棵互斥树。', '', sources(['coala','survey']), '']
            for k,v in data['types'].items():
                lines += [f'### {v["zh"]} / {v["en"]}'+('（功能综述）' if k=='working-functional' else ''),'',v['def'],'',v['enDefinition'],'',f'记录什么：{v["what"]}',f'什么时候用：{v["when"]}',f'用来做什么：{v["use"]}','',f'例子（编者构造）：{v["example"]}','',f'边界：{v["boundary"]}','',sources(v['sources']),'']
            lines += ['### 常见工程叫法对照','']
            for v in data['terms'].values():
                lines += [f'#### {v["zh"]} / {v["en"]}','',v['def'],'',v['relation'],'',v['boundary'],'',f'例子（编者构造）：{v["example"]}','',sources(v['sources']),'']
        for m in t['methods']:
            lines += [f'<a id="{t["id"]}-{m["id"]}"></a>','',f'### {m["zh"]} / {m["en"]}','',m['definition'],'',m['enDefinition'],'',f'什么时候用：{m["when"]}',f'用来做什么：{m["purpose"]}','',f'例子（编者构造）：{m["example"]}','',f'边界：{m["boundary"]}','',sources(m['sources']),'']
            if m['resources']:
                links=[]
                for rid in m['resources']:
                    r=records[rid]
                    if r['sources']:links.append(f'[{r["title"]}]({r["sources"][0]["url"]})')
                lines += ['继续阅读：'+'；'.join(links),'']
    lines += ['以上关联用于导航，不表示每个条目实现了该专题的所有方法。来源核对深度、版本和限制见资源目录；未运行系统或复现评测。','']
    return '\n'.join(lines)


def generated_files(root=ROOT):
    data = json.loads((root / 'site/knowledge.json').read_text())
    catalogue = json.loads((root / 'catalogue.json').read_text())
    navigation = json.loads((root / 'site/navigation.json').read_text())
    graph = harness.compiled_data(root)
    navigation['graphDimensions'] = [{'id': d['id'], 'name': d['name']} for d in graph['dimensions']]
    validate(data, catalogue)
    app = (root / 'site/app.js').read_text().replace('/*__KNOWLEDGE_RENDERERS__*/', (root / 'site/knowledge.js').read_text())
    scripts = '\n'.join(f'<script type="application/json" id="{name}-data">{harness.script_json(value)}</script>' for name,value in [('catalogue',catalogue),('knowledge',data),('navigation',navigation)])
    scripts += '\n<script id="navigator-app">\n' + app + '\n</script>'
    inner = (root / 'site/frame.html').read_text().replace('__APP_SCRIPTS__', scripts).replace('__KNOWLEDGE_CSS__', (root / 'site/knowledge.css').read_text())
    outer = (root / 'site/shell.html').read_text().replace('__FRAME__', html.escape(inner, quote=True))
    return {root / 'index.html': harness.page(root, graph, outer), root / 'assets/memory-layers.svg': harness.preview(graph), root / 'docs/landscape.zh-CN.md': markdown(data, catalogue)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale=[]
    for path,text in generated_files().items():
        if args.check:
            if not path.exists() or path.read_text()!=text: stale.append(str(path.relative_to(ROOT)))
        else: path.write_text(text)
    if stale: raise SystemExit('Stale generated files: '+', '.join(stale))
    print('Knowledge navigator: '+('in sync' if args.check else 'generated'))
