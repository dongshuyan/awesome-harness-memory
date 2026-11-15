# Awesome Harness Memory

**An illustrated Agent Memory tutorial for beginners.** Follow a piece of information as it is stored, revised, and used again. Then study research methods, engineering systems, and benchmarks, with literature, film, and human-memory research offering further perspectives.

**[Start learning →](https://dongshuyan.com/awesome-harness-memory/)** · [中文](README.zh-CN.md) · [Course coverage](docs/coverage.md) · [Contributing](CONTRIBUTING.md)

The course is in Chinese; primary sources retain their original language. No framework experience is required. Examples introduce necessary terms, while expandable sections hold formulas, APIs, source-code locations, and reproduction details. The aim is to help you explain a system's main mechanisms and identify what still needs documentation or an experiment.

## Learning path

| Step | Lesson | What you will examine |
| --- | --- | --- |
| 01 | [Six core questions](https://dongshuyan.com/awesome-harness-memory/#tutorial/lesson) | Six ways to understand memory, each with its purpose, a way to answer, and examples; the same page ends with sources and the argument for the checklist |
| 02 | [Related concepts](https://dongshuyan.com/awesome-harness-memory/#tutorial/concepts) | How context, session history, RAG, checkpoints, model-internal information, and generic storage relate to memory |
| 03 | [Research](https://dongshuyan.com/awesome-harness-memory/#tutorial/research) | The research problem, why a method works the way it does, and what its experiments support |
| 04 | [Engineering](https://dongshuyan.com/awesome-harness-memory/#tutorial/engineering) | How systems implement storage, updates, retrieval, sharing, and permissions through interfaces and configuration |
| 05 | [Benchmarks](https://dongshuyan.com/awesome-harness-memory/#tutorial/benchmarks) | How a task is constructed, answered, and scored, and how those observations relate to the six questions |
| 06 | [Literature and film](https://dongshuyan.com/awesome-harness-memory/#tutorial/culture) | Memory, forgetting, external records, and identity in real works, with plot facts distinguished from engineering analogies |

Alongside the main path, read [human-memory background](https://dongshuyan.com/awesome-harness-memory/#tutorial/human-memory) and [topics and practice](https://dongshuyan.com/awesome-harness-memory/#tutorial/topics) as needed. After studying individual entries, [side-by-side reading](https://dongshuyan.com/awesome-harness-memory/#tutorial/compare) lets you view their existing six-question answers together.

## The six questions in Lesson 1

| Question | What it helps you understand |
| --- | --- |
| **Q1 · What is retained?** | The roles of facts, experiences, procedures, preferences, and rules; one system may retain several kinds of content |
| **Q2 · In what form, and where?** | Text, summaries, graphs, vectors, and other representations; authoritative records, indexes, and storage locations |
| **Q3 · Whose memory is it, whom does it serve, and who can share it?** | Ownership and sharing across users, sessions, tasks, projects, agents, and teams |
| **Q4 · How is it formed, updated, invalidated, and forgotten?** | The path from an incoming event through extraction, revision, consolidation, expiry, or deletion |
| **Q5 · How do later calls obtain and use it?** | Selection, inclusion in the current input, and whether the information affects an answer or action |
| **Q6 · Who may read, write, change, and delete it, and who is responsible?** | Operational control, authorization, provenance, untrusted input, and responsibility for withdrawal |

This teaching checklist synthesizes research frameworks, official engineering documentation, and evaluations. [Lesson 1](https://dongshuyan.com/awesome-harness-memory/#tutorial/lesson) ends with facts, references, reasoning, and counterexamples explaining why these questions are retained. They help describe major mechanisms; they are not proven uniquely minimal, mathematically orthogonal, or exhaustive. Performance, cost, and safety still need appropriate tests.

## How a chapter works

Each chapter introduces the work or system, its authors or maintainers, verified affiliations where available, dates, original links, and reasons for inclusion. A concrete case then leads into the six questions. Answers use subsections, before-and-after states, dialogue, steps, tables, and diagrams to explain the mechanism and its rationale. Expandable sections hold technical detail and supporting evidence; the chapter closes with a reading check, limitations, and sources.

These three chapters show how the approach works for research, engineering, and evaluation:

| Chapter | Follow the example to learn |
| --- | --- |
| [A-Mem](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/a-mem) | How an experience becomes a memory note, how it connects to existing notes, and how new information affects their organization |
| [Graphiti](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/graphiti) | How source episodes become entities and facts, and how changes separate currently valid information from history and provenance |
| [LongMemEval](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/longmemeval) | How multiple sessions, a question, and evidence lead to retrieval, an answer, and a score; what that task can establish |

Figures sit beside their explanations and link to full-size originals. Wide figures and tables can be scrolled horizontally on phones. Teaching scenarios, examples from papers, author-reported results, and cultural analogies are labeled separately.

## Course contents

As of **2026-11-15**, the selected course contains **49 detailed entries, 294 six-question answers, and 61 figures**. Each entry records its own source version and check date. These counts describe the current course selection.

| Category | Entries | Examples |
| --- | ---: | --- |
| Research core | 10 | A-Mem, CoALA, MemGPT, Generative Agents, Reflexion, Voyager |
| Further research reading | 4 | Structural surveys, graph memory, autonomous-agent memory, and Storage–Reflection–Experience; listed separately on the Research page |
| Engineering | 15 | Claude Code, Claude-Mem, Pi, LangGraph, Graphiti, Mem0, Hindsight, and others |
| Benchmarks | 10 | LongMemEval, LoCoMo, MemoryAgentBench, COLLABMEM, and others |
| Literature and film | 8 | Memento, 50 First Dates, The Memory Police, The Housekeeper and the Professor, and other real works |
| Human-memory background | 2 | Memory systems; forgetting and consolidation |

The Research core contains at most two surveys. Entries are ordered by known public date, without a quality ranking. Selection considers inspectable primary materials, methods and evidence quality, identifiable authors or maintainers, publication status, and recency. Prestige or attention alone does not establish effectiveness. See [coverage and evidence limits](docs/coverage.md).

## From reading to practice

[Topics and practice](https://dongshuyan.com/awesome-harness-memory/#tutorial/topics) covers safety and deletion, cost and capacity, evaluation design, and a local example that requires no API key. The example uses SQLite to show persistence, correction, scope filtering, expiry, and retrieval.

```sh
python3 examples/memory_lab.py
```

The [practice guide](docs/practice.zh-CN.md) connects each step and its expected output to the six questions. The example does not call a model. This repository has not independently reproduced the papers' performance scores or run every upstream product.

## Local preview and maintenance

Clone the repository and start a static server from its root:

```sh
git clone https://github.com/dongshuyan/awesome-harness-memory.git
cd awesome-harness-memory
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/>. Figures load from `site/figures/`, so keep that directory with `index.html` when previewing or publishing.

To edit the course, update its authoritative data in [`site/tutorial.json`](site/tutorial.json), then build and check:

```sh
python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 scripts/build_lesson_figures.py --check
python3 -m unittest discover -s tests -v
node --check site/routes.js
node --check site/app.js
node --check site/tutorial.js
```

The builder and teaching example use the Python standard library. The full tests also require Node.js, with no npm dependencies. See [repository structure](docs/repository-structure.md) for generators, diagram specifications, and maintenance, and [figure credits](site/figures/pilot/ATTRIBUTIONS.md) for reused images and licenses.

Contributions should include primary sources, versions, exact locations, complete examples, and limitations. Keep undocumented behavior marked as unknown; distinguish author reports, independent replication, and literary analogies. Downloaded papers, code, and data belong in the ignored `.study-sources/` directory and are not published with the site. See the [contribution requirements](CONTRIBUTING.md) and [maintenance roadmap](ROADMAP.md).
