# Contributing

[Course](https://dongshuyan.com/awesome-harness-memory/) · [中文入口](README.zh-CN.md) · [Data ownership](docs/repository-structure.md)

A contribution should help a reader explain a memory mechanism, evaluate a claim, or inspect a useful counterexample. Propose additions or corrections with primary sources. Keep unrelated refactoring separate from content updates.

## Choose the right place

- `site/tutorial.json`: the six-question lesson, detailed research/engineering/benchmark entries, cultural analogies, human-memory background, concepts, and topics.
- `examples/` and `docs/practice.zh-CN.md`: runnable teaching examples and their assumptions. Prefer small local examples with no paid service requirement.

## Detailed entry requirements

Keep the existing six-question order: content, substrate, scope, lifecycle, exposure, governance. A complete entry needs identity, public date, checked date, original URL, selection evidence, sources, limitations, and a next reading step. Research core entries include at most two surveys; additional reviewed surveys belong in the separate further-reading list.

Each question contains the following fields:

| Field | Required content |
| --- | --- |
| `answer` | Explain the mechanism or state explicitly what the source does not specify |
| `why` | Explain why this answer follows from the design and matters to the reader |
| `example` | Give a concrete example; identify whether it comes from the source, paraphrases it, or is constructed for teaching |
| `sources` | List the registered source IDs supporting this answer; link to the relevant section or code location where possible |
| `trace` | Point to the source, version, section, figure, API, or code location supporting the answer |

Examples should follow the information through a concrete situation: input, storage or transformation, and later use. Use paragraphs rather than a string of labels. An optional `caseStudy` introduces a scenario shared by the six questions. Add `profile.affiliation` only when `affiliationSources` identifies a paper author block or official source. A one-line label is not a complete explanation. Length should follow the mechanism's complexity; repeated disclaimers cannot substitute for evidence. Use `pending` honestly if a future entry is not ready. Set `complete` only after all six answers and identity/evidence fields are checked.

Benchmark entries additionally describe abilities, task protocol, metrics, the design-to-evaluation mapping, and limitations. A capability score does not identify a storage architecture or establish an authorization guarantee. Keep separate metrics when they answer different questions.

## Evidence and dates

Prefer the paper, official documentation, maintainer repository, original publisher, or release metadata. Record access dates and the inspected version. Distinguish first public release, later revision, venue publication, and documentation snapshot dates. If only a year is known, do not invent a month or day. Lists use known public dates; unknown dates come last, with no quality ranking.

Attribute reported experiments and identify their tasks, models, budgets, and controls. Mark reproductions only when they were actually run. Assess confidence qualitatively from the evidence, not from author reputation or popularity alone. A source that omits a feature does not prove that the system lacks it. Keep same-origin reports from counting as independent corroboration.

Literary and screen entries must refer to real works. Cite the original publisher, credited creator, official synopsis, or inspected passage. Separate the work's premise from the editor's AI analogy; avoid unnecessary spoilers and long quotations. Human-memory findings and computational analogies also require separate evidence.

## Validate before publishing

The builder and local example require Python; the test suite also uses Node.js. No package installation is required.

```sh
python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 -m unittest discover -s tests -v
node --check site/app.js
node --check site/tutorial.js
python3 examples/memory_lab.py
```

Inspect the changed page, its source links, hash route, and comparison behavior when affected. Check README counts and local links. Review the complete diff and preserve accepted content. Content batches receive an independent review before publication; model agreement does not replace source verification or runtime checks.

Disclose relevant affiliations. Do not commit private research logs, credentials, personal data, or unpublished security reports. Linked publications, code, datasets, and media retain their original licenses; inclusion grants no redistribution rights.
