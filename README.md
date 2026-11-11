# Awesome Harness Memory

> An Agent Memory tutorial: learn how to understand a memory system, then read carefully selected research, engineering systems, benchmarks, and cultural thought experiments.

[简体中文教程](README.zh-CN.md) · **[Open the interactive tutorial (Chinese)](https://dongshuyan.github.io/awesome-harness-memory/)** · [Legacy catalogue](resources/systems.md) · [Repository structure](docs/repository-structure.md)

The public site is a course rather than a leaderboard. It starts with six questions that can be asked of any Memory system, then applies the same questions to named research methods, agents, harnesses, independent memory systems, and benchmarks. Literature and film are kept as clearly labelled analogies, not as evidence about model capability or engineering safety.

## Course path

1. **First lesson: the six questions.** What is stored? What form and substrate carries it? Who owns it and who can share it? How does it form, change, expire, or get forgotten? How does a later call obtain and use it? Who may read, write, change, or delete it, and what responsibility follows?
2. **Concept bridge.** Context, session history, RAG, checkpoints, parameters/KV state, and generic storage can participate in Memory without being the same concept.
3. **Research.** Selected research frameworks and methods. Each entry starts with identity, inclusion evidence, source boundaries, and then answers the six questions.
4. **Engineering.** Named agents, harnesses, frameworks, standalone memory systems, and managed memory services. A documented mechanism is kept separate from an assumption about hidden implementation.
5. **Benchmarks.** Each benchmark is described by its target abilities, task protocol, metrics, and relation to the six questions. The site does not turn different benchmark scores into a single ranking.
6. **Literature and screen.** Real novels, stories, films, and series used as analogy or thought experiment. They are not research, product, or evaluation evidence.

The final comparison page is optional. It places selected entries side by side after the reader has studied their individual pages.

## Current tutorial edition

The snapshot checked on **2026-11-12** contains:

- **10 selected Research entries**, with CoALA, Forms–Functions–Dynamics, MemGPT, Generative Agents, and A-Mem as complete six-question exemplars; four additional review leads remain visible as screened candidates;
- **15 engineering entries**, with Claude Code, LangGraph, Google Agent Platform Memory Bank, Mem0, and Graphiti as complete exemplars;
- **10 benchmarks**, with LongMemEval, MemoryAgentBench, COLLABMEM, LoCoMo, and MemBench as complete exemplars;
- **6 literature and screen entries**, with *Memento* and “Funes the Memorious” as complete cultural examples;
- **2 human-memory background entries**, plus topic and tool pages.

The other entries are deliberately marked **待完善 / pending**. A pending entry is a useful lead with a source and a boundary statement; it is not presented as if its six answers had already been verified.

Research and engineering are selected for source quality, identifiable authors or maintainers, recency, and verifiability. Peer-reviewed or proceedings sources are preferred; arXiv-only work is kept only with an explicit evidence boundary. The lists are ordered by known public year, with entries whose public date is not stated placed after dated entries. The order is not a quality ranking.

## Public data and preserved material

- [`site/tutorial.json`](site/tutorial.json) is the authoritative tutorial data: the six questions, sources, entries, status, sample answers, benchmark coverage, and visualization descriptions.
- [`site/tutorial.js`](site/tutorial.js) renders the tutorial routes, detail pages, six-question comparison, and coverage views.
- [`site/frame.html`](site/frame.html) and [`site/app.js`](site/app.js) provide the UI shell and routing. [`index.html`](index.html) is generated for GitHub Pages.
- The earlier catalogue, topic pages, seven-layer Harness projection, and [research × engineering report](https://dongshuyan.github.io/awesome-harness-memory/report/index.html) remain available under the reference and tools links. They are preserved editions with their own evidence scope; the tutorial is the default learning path.

The root catalogue contains **136 public resources** after the 2026-11-12 identity correction to its 2026-11-06 edition. That count is separate from the tutorial workset above. Neither count is an industry total, market share, performance result, or completeness claim.

## Local preview and checks

From the repository root:

```sh
python3 scripts/build_site.py
python3 -m unittest discover -s tests -v
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. The build embeds the catalogue and tutorial data into the static page; no server-side rewrite or package installation is required. `python3 scripts/build_site.py --check` verifies that generated files are current.

Public pages report documented facts and source boundaries. They do not claim that a system was installed, that a benchmark was run, or that a missing public detail means a capability is absent. Private research plans and review records stay outside this repository.

See the [contribution guide](CONTRIBUTING.md), [roadmap](ROADMAP.md), or [repository structure and publishing notes](docs/repository-structure.md).
