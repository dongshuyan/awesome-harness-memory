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


def framework_categories(framework):
    if framework.get('categories'):
        return framework['categories']
    return [category for dimension in framework.get('dimensions', []) for category in dimension.get('categories', [])]


def content_methods(data):
    return {method['id']: method for method in data.get('draftTaxonomy', {}).get('items', [])}


def validate(data, catalogue):
    ids = {r['id'] for r in catalogue['resources']}
    if len(ids) != len(catalogue['resources']):
        raise ValueError('Duplicate catalogue IDs')
    source_ids = set(data['sources'])
    all_sources = [*data['sources'].values(), *[s for r in catalogue['resources'] for s in r['sources']]]
    for source in all_sources:
        parsed = urlsplit(source['url'])
        if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('Expected HTTPS source')
    draft_items = data.get('draftTaxonomy', {}).get('items', [])
    draft = data.get('draftTaxonomy', {})
    if draft.get('status') != '待验证' or len(draft_items) != 7:
        raise ValueError('Draft taxonomy must contain seven explicitly unverified items')
    for item in [*data['types'].values(), *data['terms'].values(), *data['topics'], *[m for t in data['topics'] for m in t['methods']], *draft_items]:
        if not set(item.get('resources', [])) <= ids or not set(item.get('sources', [])) <= source_ids:
            raise ValueError('Unresolved resource or source reference')
    for topic in data['topics']:
        if len({m['id'] for m in topic['methods']}) != len(topic['methods']):
            raise ValueError('Duplicate method IDs')
    framework_ids = set(data['frameworks'])
    for framework_id, framework in data['frameworks'].items():
        required_source_facts = {'classificationBasis', 'categoryRelations', 'structureEvidence', 'empiricalSupport', 'scope', 'limitations'}
        required_reader_guide = {'scenarios', 'focus', 'advantages', 'tradeoffs'}
        if not required_source_facts <= set(framework.get('sourceFacts', {})):
            raise ValueError(f'Incomplete framework source facts: {framework_id}')
        if not required_reader_guide <= set(framework.get('readerGuide', {})):
            raise ValueError(f'Incomplete framework reader guide: {framework_id}')
        if not framework.get('sourceScenarios'):
            raise ValueError(f'Framework needs at least one sourced scenario: {framework_id}')
        for scenario in framework.get('sourceScenarios', []):
            required = {'title', 'source', 'location', 'background', 'memory', 'storage', 'write', 'read', 'maintenance', 'effect', 'contrast', 'evidence'}
            if not required <= set(scenario) or scenario['source'] not in source_ids or any(not str(scenario[field]).strip() for field in required):
                raise ValueError(f'Incomplete framework scenario: {framework_id}')
        categories = framework_categories(framework)
        category_ids = [category['id'] for category in categories]
        if len(category_ids) != len(set(category_ids)):
            raise ValueError(f'Duplicate framework category IDs: {framework_id}')
        if not set(framework.get('sources', [framework.get('source')])) <= source_ids:
            raise ValueError(f'Unresolved framework source: {framework_id}')
        if not set(framework.get('roots', [])) <= set(category_ids):
            raise ValueError(f'Unresolved framework root: {framework_id}')
        for child_ids in framework.get('children', {}).values():
            if not set(child_ids) <= set(category_ids):
                raise ValueError(f'Unresolved framework child: {framework_id}')
        for category in categories:
            if category.get('typeId') and category['typeId'] not in data['types']:
                raise ValueError(f'Unresolved type reference: {category["typeId"]}')
            if category.get('term') and category['term'] not in data['terms']:
                raise ValueError(f'Unresolved term reference: {category["term"]}')
        if framework.get('dimensions'):
            flattened = [c for dimension in framework['dimensions'] for c in dimension.get('categories', [])]
            if flattened != categories:
                raise ValueError(f'Framework category flattening drift: {framework_id}')
    index = data.get('contentIndex', {})
    methods = content_methods(data)
    content_ids = {item for group in index.get('groups', []) for item in group.get('items', [])}
    if content_ids != set(methods):
        raise ValueError('Content index must cover exactly the draft taxonomy items')
    if next(topic for topic in data['topics'] if topic['id'] == 'types').get('methods'):
        raise ValueError('Formal memory taxonomy topic must not own editorial content labels')
    for framework_id, rows in index.get('mappings', {}).items():
        if framework_id not in framework_ids:
            raise ValueError(f'Unknown content mapping framework: {framework_id}')
        category_ids = {category['id'] for category in framework_categories(data['frameworks'][framework_id])}
        if not set(rows) <= content_ids:
            raise ValueError(f'Unknown content mapping row: {framework_id}')
        for row in rows.values():
            if not set(row) <= category_ids:
                raise ValueError(f'Unknown content mapping column: {framework_id}')
            if not set(row.values()) <= {'direct', 'parent', 'related', 'possible', 'unclear', 'none'}:
                raise ValueError(f'Unknown content mapping state: {framework_id}')
    for update in data.get('updates', []):
        if not set(update.get('sources', [])) <= source_ids:
            raise ValueError(f'Unresolved update source: {update.get("id")}')


def validate_tutorial(tutorial):
    if tutorial.get('version') != 1:
        raise ValueError('Unsupported tutorial data version')
    questions = tutorial.get('questions', [])
    expected_questions = ['content', 'substrate', 'scope', 'lifecycle', 'exposure', 'governance']
    if [q.get('id') for q in questions] != expected_questions:
        raise ValueError('Tutorial questions must keep the six-question order')
    if tutorial.get('comparisonCategories') != ['research', 'engineering', 'benchmarks', 'culture']:
        raise ValueError('Tutorial comparison categories must match the comparison view')
    sources = tutorial.get('sources', {})
    for source_id, source in sources.items():
        parsed = urlsplit(source.get('url', ''))
        if parsed.scheme != 'https' or not parsed.hostname:
            raise ValueError(f'Invalid tutorial source URL: {source_id}')
    entries = tutorial.get('entries', {})
    for category in ('research', 'engineering', 'benchmarks', 'culture'):
        rows = entries.get(category, [])
        if len(rows) < 1:
            raise ValueError(f'Tutorial category is empty: {category}')
        if category in ('research', 'engineering', 'benchmarks') and sum(row.get('status') == 'complete' for row in rows) < 1:
            raise ValueError(f'Tutorial category needs at least one complete sample: {category}')
        ids = set()
        for row in rows:
            if row.get('id') in ids:
                raise ValueError(f'Duplicate tutorial entry: {row.get("id")}')
            ids.add(row.get('id'))
            if not row.get('checkedAt') or not set(row.get('sources', [])) <= set(sources):
                raise ValueError(f'Incomplete tutorial entry provenance: {row.get("id")}')
            if row.get('status') == 'complete':
                if len(row.get('questions', [])) != 6:
                    raise ValueError(f'Complete tutorial entry must answer six questions: {row.get("id")}')
                if not row.get('selectionEvidence') or not row.get('limitations') or not row.get('next'):
                    raise ValueError(f'Complete tutorial entry is missing evidence fields: {row.get("id")}')
                profile = row.get('profile', {})
                if not profile.get('kind') or not profile.get('artifact'):
                    raise ValueError(f'Complete tutorial entry is missing identity fields: {row.get("id")}')
                if category == 'benchmarks':
                    evaluation = row.get('evaluation', {})
                    required_evaluation = {'abilities', 'taskProtocol', 'metrics', 'designMapping', 'limitations'}
                    if not required_evaluation <= set(evaluation) or any(not str(evaluation[field]).strip() for field in required_evaluation):
                        raise ValueError(f'Complete benchmark is missing evaluation fields: {row.get("id")}')
                for answer in row['questions']:
                    if not answer.get('answer') or not answer.get('trace'):
                        raise ValueError(f'Incomplete tutorial answer: {row.get("id")}')
            if category == 'culture' and not row.get('realityNote'):
                raise ValueError(f'Culture entry needs a reality note: {row.get("id")}')
    if len(tutorial.get('visualizations', [])) < 3:
        raise ValueError('Tutorial needs at least three visualization descriptions')


def markdown(data, catalogue):
    records = {r['id']: r for r in catalogue['resources']}

    def sources(ids):
        links = []
        for source_id in dict.fromkeys(ids or []):
            source = data['sources'][source_id]
            meta = '；'.join(str(source[k]) for k in ('year', 'evidence') if source.get(k))
            suffix = f'（{meta}）' if meta else ''
            links.append(f'[{source["label"]}]({source["url"]}){suffix}')
        return '；'.join(links)

    def framework_category_data(category):
        if category.get('typeId'):
            return data['types'][category['typeId']]
        if category.get('term'):
            return data['terms'][category['term']]
        return category

    def status_symbol(value):
        return {'direct': '●', 'parent': '◆', 'related': '◐', 'possible': '◇', 'unclear': '?', 'none': '—'}.get(value, '—')

    def framework_categories(framework):
        return framework.get('categories') or [c for dimension in framework.get('dimensions', []) for c in dimension.get('categories', [])]

    methods = content_methods(data)
    lines = [
        '# 记忆分类与方法导航',
        '',
        '从九个问题学习记忆系统。记忆分类先展示有来源的主流分类方式，再用典型记忆内容索引做交叉对照；九问是编者导航，不声称唯一、穷尽或完全正交。',
        '',
        '[打开交互页面](https://dongshuyan.github.io/awesome-harness-memory/) · [GitHub 仓库](https://github.com/dongshuyan/awesome-harness-memory) · [资源目录](../README.zh-CN.md#从具体对象开始)',
        '',
        '## 页面导航',
        '',
    ]
    lines += [f'- [{topic["title"]} · {topic["en"]}](#{topic["id"]})' for topic in data['topics']]
    for topic in data['topics']:
        lines += ['', f'<a id="{topic["id"]}"></a>']
        lines += [f'<a id="{old}"></a>' for old, new in data['aliases'].items() if new == topic['id']]
        lines += ['', f'## {topic["title"]} / {topic["en"]}', '', topic['intro'], '', topic['enIntro'], '', topic['boundary'], '']
        if topic['id'] == 'types':
            lines += ['### 有来源的分类入口', '', '下面四套入口处于同一层级。每套都按“来源事实 / 编者解释 / 类别结构 / 来源场景”展开；顺序按来源清晰度和当前证据状态排列。', '']
            for number, (framework_id, framework) in enumerate(sorted(data['frameworks'].items(), key=lambda item: item[1].get('order', 99)), 1):
                lines += [f'#### {number}. {framework["name"]} / {framework["en"]}', '', framework['intro'], '', f'- 来源与年份：{sources(framework.get("sources", [framework.get("source")]))}', f'- 证据与状态：{framework.get("status", "待补")}；{framework.get("confidence", "待定")}', '']
                lines += ['**来源事实**', '', f'- 分类依据：{framework["sourceFacts"]["classificationBasis"]}', f'- 类别之间的关系：{framework["sourceFacts"]["categoryRelations"]}', f'- 结构证据：{framework["sourceFacts"]["structureEvidence"]}', f'- 实证支持：{framework["sourceFacts"]["empiricalSupport"]}', f'- 原文声称的适用范围：{framework["sourceFacts"]["scope"]}', f'- 原文声称的限制：{framework["sourceFacts"]["limitations"]}', '']
                lines += ['**编者解释**', '', f'- 适用场景：{framework["readerGuide"]["scenarios"]}', f'- 侧重点：{framework["readerGuide"]["focus"]}', f'- 优势：{framework["readerGuide"]["advantages"]}', f'- 代价：{framework["readerGuide"]["tradeoffs"]}', '']
                lines += ['**这套分类自己的类别**', '']
                categories = framework_categories(framework)
                by_id = {category['id']: category for category in categories}
                if framework.get('dimensions'):
                    for dimension in framework['dimensions']:
                        lines += [f'- **{dimension["zh"]} / {dimension["en"]}**：{dimension["description"]}']
                        for category in dimension['categories']:
                            raw = framework_category_data(category)
                            lines += [f'  - **{category["zh"]} / {category["en"]}**：{category["definition"]} 教学例子：{category["example"]} 边界：{raw.get("boundary", "原文未单独说明")}', f'    - 来源：{sources(raw.get("sources", framework.get("sources", [])))}']
                            if raw.get('evidenceLevel') or raw.get('standardization'):
                                lines += [f'    - 术语证据：{raw.get("evidenceLevel", "未分级")}；标准化状态：{raw.get("standardization", "原文未说明")}', f'    - 术语来源说明：{raw.get("evidenceSummary", "原文未说明")}']
                else:
                    for root_id in framework.get('roots', []):
                        category = by_id[root_id]
                        raw = framework_category_data(category)
                        lines += [f'- **{category["zh"]} / {category["en"]}**：{category["definition"]} 教学例子：{category["example"]} 边界：{raw.get("boundary", "原文未单独说明")}', f'  - 来源：{sources(raw.get("sources", framework.get("sources", [])))}']
                        if raw.get('evidenceLevel') or raw.get('standardization'):
                            lines += [f'  - 术语证据：{raw.get("evidenceLevel", "未分级")}；标准化状态：{raw.get("standardization", "原文未说明")}', f'  - 术语来源说明：{raw.get("evidenceSummary", "原文未说明")}']
                        for child_id in framework.get('children', {}).get(root_id, []):
                            child = by_id[child_id]
                            raw_child = framework_category_data(child)
                            lines += [f'  - **{child["zh"]} / {child["en"]}**：{child["definition"]} 教学例子：{child["example"]} 边界：{raw_child.get("boundary", "原文未单独说明")}', f'    - 来源：{sources(raw_child.get("sources", framework.get("sources", [])))}']
                            if raw_child.get('evidenceLevel') or raw_child.get('standardization'):
                                lines += [f'    - 术语证据：{raw_child.get("evidenceLevel", "未分级")}；标准化状态：{raw_child.get("standardization", "原文未说明")}', f'    - 术语来源说明：{raw_child.get("evidenceSummary", "原文未说明")}']
                lines += ['', '**有来源的场景与证据边界**', '']
                for scenario in framework.get('sourceScenarios', []):
                    lines += [f'- **{scenario["title"]}**（{sources([scenario["source"]])}；位置：{scenario["location"]}）', f'  - 场景背景：{scenario["background"]}', f'  - 记忆内容：{scenario["memory"]}', f'  - 承载与表示：{scenario["storage"]}', f'  - 写入触发与主体：{scenario["write"]}', f'  - 读取与注入：{scenario["read"]}', f'  - 更新、压缩或遗忘：{scenario["maintenance"]}', f'  - 原文效果或定性结论：{scenario["effect"]}', f'  - 与相邻类别的区别：{scenario["contrast"]}', f'  - 证据性质：{scenario["evidence"]}', '']

            draft = data['draftTaxonomy']
            lines += ['### 待验证草案：编者综合的典型记忆内容标签', '', draft['intro'], '', f'- 状态：{draft["status"]}', f'- 形成依据：{draft["rationale"]}', f'- 限制：{draft["limitation"]}', '', '这些标签用于分类外导航，不是第五套已确立分类方式。', '']
            for item in draft['items']:
                lines += [f'- **{item["zh"]} / {item["en"]}**：{item["definition"]}；边界：{item["boundary"]}；来源：{sources(item["sources"])}']
            lines += ['']

            index = data['contentIndex']
            lines += [f'### {index["title"]}', '', index['description'], '', '本索引是分类外的导航层；它把不同分类方式中常见的内容词汇集中起来，便于进入交叉映射。', '']
            for group in index['groups']:
                lines += [f'#### {group["zh"]} / {group["en"]}', '', group['note'], '']
                for item_id in group['items']:
                    method = methods[item_id]
                    lines += [f'<a id="types-{method["id"]}"></a>', f'- **{method["zh"]} / {method["en"]}**：{method["definition"]} 教学例子：{method["example"]} 边界：{method["boundary"]} 来源：{sources(method["sources"])}']
                lines += ['']
            lines += ['### 跨分类映射', '', '交叉表的行是待验证草案中的典型内容，列是某一套正式分类自己的类别；它不表示不同分类方式之间的父子关系，其中 `◆` 只表示当前分类方式内部的上层类别与该内容的包含关系。符号：`●` 直接对应，`◆` 上层包含，`◐` 有关联，`◇` 可落入，`?` 待核，`—` 未标注直接对应。', f'- 映射性质：{index.get("mappingStatus", "编者映射；待验证")}', '']
            for framework_id, framework in sorted(data['frameworks'].items(), key=lambda item: item[1].get('order', 99)):
                categories = framework_categories(framework)
                lines += [f'#### {framework["name"]}', '', '| 典型内容 | ' + ' | '.join(category['zh'] for category in categories) + ' |', '| --- | ' + ' | '.join('---' for _ in categories) + ' |']
                mapping = index['mappings'].get(framework_id, {})
                for group in index['groups']:
                    for item_id in group['items']:
                        row = mapping.get(item_id, {})
                        lines.append('| ' + methods[item_id]['zh'] + ' | ' + ' | '.join(status_symbol(row.get(category['id'])) for category in categories) + ' |')
                lines += ['']
            lines += ['### 相关研究视角', '', '这些工作补充结构、生命周期、成本和图记忆等问题，放在分类模块之外供继续研究。', '']
            for update in data.get('updates', []):
                lines += [f'- **{update["title"]} / {update["en"]}（{update["year"]}）**：{update["summary"]} 与分类模块的关系：{update["relation"]} 来源：{sources(update["sources"])}', '']
        if topic['id'] != 'types':
            for method in topic['methods']:
                lines += [f'<a id="{topic["id"]}-{method["id"]}"></a>', '', f'### {method["zh"]} / {method["en"]}', '', method['definition'], '', method['enDefinition'], '', f'什么时候用：{method["when"]}', f'用来做什么：{method["purpose"]}', '', f'例子（编者构造）：{method["example"]}', '', f'边界：{method["boundary"]}', '', sources(method['sources']), '']
                if method['resources']:
                    links = []
                    for resource_id in method['resources']:
                        record = records[resource_id]
                        if record['sources']:
                            links.append(f'[{record["title"]}]({record["sources"][0]["url"]})')
                    lines += ['继续阅读：' + '；'.join(links), '']
    lines += ['以上关联用于导航，不表示每个条目实现了该专题的所有方法。来源核对深度、版本和限制见资源目录；未运行系统或复现评测。', '']
    return '\n'.join(lines)


def generated_files(root=ROOT):
    data = json.loads((root / 'site/knowledge.json').read_text())
    tutorial = json.loads((root / 'site/tutorial.json').read_text())
    catalogue = json.loads((root / 'catalogue.json').read_text())
    navigation = json.loads((root / 'site/navigation.json').read_text())
    graph = harness.compiled_data(root)
    navigation['graphDimensions'] = [{'id': dimension['id'], 'name': dimension['name']} for dimension in graph['dimensions']]
    validate(data, catalogue)
    validate_tutorial(tutorial)
    app = (root / 'site/app.js').read_text().replace('/*__KNOWLEDGE_RENDERERS__*/', (root / 'site/knowledge.js').read_text()).replace('/*__TUTORIAL_RENDERERS__*/', (root / 'site/tutorial.js').read_text())
    scripts = '\n'.join(f'<script type="application/json" id="{name}-data">{harness.script_json(value)}</script>' for name, value in [('catalogue', catalogue), ('knowledge', data), ('tutorial', tutorial), ('navigation', navigation)])
    scripts += '\n<script id="navigator-app">\n' + app + '\n</script>'
    inner = (root / 'site/frame.html').read_text().replace('__APP_SCRIPTS__', scripts).replace('__KNOWLEDGE_CSS__', (root / 'site/knowledge.css').read_text())
    outer = (root / 'site/shell.html').read_text().replace('__FRAME__', html.escape(inner, quote=True))
    return {root / 'index.html': harness.page(root, graph, outer), root / 'assets/memory-layers.svg': harness.preview(graph), root / 'docs/landscape.zh-CN.md': markdown(data, catalogue)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for path, text in generated_files().items():
        if args.check:
            if not path.exists() or path.read_text() != text:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(text)
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    print('Knowledge navigator: ' + ('in sync' if args.check else 'generated'))
