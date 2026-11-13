#!/usr/bin/env python3
"""Build the self-contained Agent Memory course from its authoritative sources."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate_url(value, label):
    parsed = urlsplit(value or '')
    if (parsed.scheme != 'https' or not parsed.hostname or parsed.username is not None
            or parsed.password is not None or any(c.isspace() for c in value)):
        raise ValueError(f'Invalid tutorial URL: {label}')


def script_json(value):
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':'))
            .replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')
            .replace('\u2028', '\\u2028').replace('\u2029', '\\u2029'))


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
        validate_url(source.get('url', ''), source_id)
    for question in questions:
        if not question.get('sources') or not set(question['sources']) <= set(sources):
            raise ValueError(f'Unknown tutorial question source: {question["id"]}')
    for concept in tutorial.get('concepts', []):
        if any(not concept.get(field) for field in ('id', 'title', 'what', 'detail', 'example', 'check', 'sources')):
            raise ValueError(f'Incomplete tutorial concept: {concept.get("id")}')
        if not set(concept['sources']) <= set(sources):
            raise ValueError(f'Unknown tutorial concept source: {concept["id"]}')
    for topic in tutorial.get('topics', []):
        if any(not topic.get(field) for field in ('id', 'title', 'intro', 'sections')):
            raise ValueError(f'Incomplete tutorial topic: {topic.get("id")}')
        for field in ('guideUrl', 'codeUrl'):
            if topic.get(field):
                validate_url(topic[field], f'{topic["id"]}.{field}')
        for section in topic['sections']:
            if any(not section.get(field) for field in ('title', 'text', 'example', 'check')):
                raise ValueError(f'Incomplete tutorial topic section: {topic["id"]}')
            if 'sources' not in section or not set(section['sources']) <= set(sources):
                raise ValueError(f'Unknown tutorial topic source: {topic["id"]}')
    entries = tutorial.get('entries', {})
    all_ids = set()
    for category in ('research', 'engineering', 'benchmarks', 'culture', 'humanMemory', 'researchCandidates'):
        if category == 'researchCandidates':
            rows = tutorial.get('researchCandidates', [])
        else:
            rows = entries.get(category, [])
        if len(rows) < 1:
            raise ValueError(f'Tutorial category is empty: {category}')
        if category in ('research', 'engineering', 'benchmarks') and sum(row.get('status') == 'complete' for row in rows) < 1:
            raise ValueError(f'Tutorial category needs at least one complete sample: {category}')
        for row in rows:
            if row.get('id') in all_ids:
                raise ValueError(f'Duplicate tutorial entry: {row.get("id")}')
            all_ids.add(row.get('id'))
            validate_url(row.get('canonicalUrl', ''), row.get('id'))
            if not row.get('checkedAt') or not set(row.get('sources', [])) <= set(sources):
                raise ValueError(f'Incomplete tutorial entry provenance: {row.get("id")}')
            if row.get('profile', {}).get('affiliation'):
                if not row.get('affiliationSources') or not set(row['affiliationSources']) <= set(sources):
                    raise ValueError(f'Unknown tutorial affiliation source: {row.get("id")}')
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
                    if any(not answer.get(field) for field in ('answer', 'why', 'example', 'trace')):
                        raise ValueError(f'Incomplete tutorial answer: {row.get("id")}')
                    if 'sources' in answer and not set(answer['sources']) <= set(sources):
                        raise ValueError(f'Unknown tutorial answer source: {row.get("id")}')
            if category == 'culture' and not row.get('realityNote'):
                raise ValueError(f'Culture entry needs a reality note: {row.get("id")}')


def generated_files(root=ROOT):
    tutorial = json.loads((root / 'site/tutorial.json').read_text())
    validate_tutorial(tutorial)
    template = (root / 'site/frame.html').read_text()
    css = (root / 'site/tutorial.css').read_text()
    app = (root / 'site/app.js').read_text().replace(
        '/*__TUTORIAL_RENDERERS__*/', (root / 'site/tutorial.js').read_text())
    js = (root / 'site/routes.js').read_text() + '\n' + app
    page = (template.replace('__COURSE_CSS__', css)
            .replace('__COURSE_DATA__', script_json(tutorial))
            .replace('__COURSE_JS__', js))
    return {root / 'index.html': page}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for path, content in generated_files().items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content)
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    print('Agent Memory course: ' + ('in sync' if args.check else 'generated'))
