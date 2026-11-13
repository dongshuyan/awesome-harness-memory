# Awesome Harness Memory

**A tutorial for understanding Agent Memory, from mechanisms to working examples.** Learn how agents, harnesses, and independent memory systems retain and use information, then examine research, implementations, evaluations, and memory in literature and film.

**[Start the tutorial →](https://dongshuyan.com/awesome-harness-memory/)** · [中文](README.zh-CN.md) · [Coverage and evidence limits](docs/coverage.md) · [Contributing](CONTRIBUTING.md)

The interactive course is in Chinese; primary sources retain their original language. No framework experience is required. The goal is to explain how information is stored, revised, retrieved, and made available to a later model call, while identifying what the evidence does not establish.

## Lesson 1: Six questions for understanding memory

[Read the continuous lesson, examples, and supporting argument](https://dongshuyan.com/awesome-harness-memory/#tutorial/lesson).

| Question | What to understand |
| --- | --- |
| **1. Content and role** | Is the system retaining facts, experiences, procedures, preferences, or rules? What purpose do they serve? |
| **2. Storage and representation** | Where does information live, and how is it represented: source text, summaries, graphs, vectors, or another form? |
| **3. Subject and scope** | Whom does it describe or serve? Which sessions, tasks, projects, or agents share it? |
| **4. Lifecycle** | How is it written, revised, consolidated, expired, forgotten, or deleted? |
| **5. Exposure to later calls** | Does it arrive through persistent context, automatic retrieval, explicit tools, or another path? |
| **6. Control and governance** | Who decides operations, who is authorized, and how are provenance, withdrawal, and untrusted inputs handled? |

These questions are a sourced teaching checklist synthesized from research frameworks, official engineering documentation, and evaluations. They are not a universal taxonomy or a proven uniquely minimal, mathematically orthogonal set. The lesson separates facts, references, reasoning, and counterexamples. Understanding a mechanism still leaves performance, cost, and safety to be tested.

For example, a project's deadline changes from Friday to Monday. Saving both statements is only part of the problem: the system must choose the valid version, respect project scope, retrieve it at the right time, and retain the correction's source. This example connects the rest of the course.

## Follow the learning path

| Step | Lesson | Why it comes next |
| --- | --- | --- |
| 02 | [Related concepts](https://dongshuyan.com/awesome-harness-memory/#tutorial/concepts) | Distinguish context, session history, RAG, checkpoints, parameters/latent states/KV, and generic storage |
| 03 | [Research](https://dongshuyan.com/awesome-harness-memory/#tutorial/research) | Understand the research question, proposed mechanism, and what the experiments support |
| 04 | [Engineering](https://dongshuyan.com/awesome-harness-memory/#tutorial/engineering) | Trace memory through concrete interfaces, persistence, scope, configuration, and controls |
| 05 | [Benchmarks](https://dongshuyan.com/awesome-harness-memory/#tutorial/benchmarks) | Examine tasks, protocols, metrics, and their relationship to the six questions |
| 06 | [Literature and film](https://dongshuyan.com/awesome-harness-memory/#tutorial/culture) | Explore forgetting, external records, identity, and sharing through real works, with analogies clearly labeled |

Every detailed entry begins with identity, authors or maintainers, verified affiliations where available, dates, primary links, and reasons for inclusion. Each of the six answers then explains **the mechanism, its rationale, a concrete example, and the source location**. Research, engineering, and benchmarks have separate entry pages and individual detail pages. An optional [comparison tool](https://dongshuyan.com/awesome-harness-memory/#tutorial/compare) displays existing answers side by side.

## Examples in the course

As of **2026-11-14**, the workset contains the following detailed entries. Each entry records its own source-check date. Known public dates determine ordering; there is no quality ranking.

| Category | Detailed entries | Starting points |
| --- | ---: | --- |
| Research core | 10 | [CoALA](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/coala), [MemGPT](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/memgpt), [Generative Agents](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/generative-agents) |
| Further research reading | 4 | Structural surveys, graph memory, autonomous agents, and Storage–Reflection–Experience; listed separately on the Research page |
| Engineering systems | 15 | [Claude Code](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/claude-code), [LangGraph](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/langgraph), [Mem0](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/mem0) |
| Benchmarks | 10 | [LongMemEval](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/longmemeval), [LoCoMo](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/locomo), [COLLABMEM](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/collabmem) |
| Literature and film | 8 | Memento, Funes the Memorious, Severance, 50 First Dates, and other real works |
| Human memory background | 2 | [Memory systems; forgetting and consolidation](https://dongshuyan.com/awesome-harness-memory/#tutorial/human-memory) |

All **49 entries have six-question explanations**, including 35 technical core entries. The core Research selection contains at most two surveys; further surveys remain separate. Selection considers inspectable primary materials, methods and evidence quality, identifiable authors or maintainers, publication status, and recency. Prestige or attention alone does not establish effectiveness.

## Turn understanding into checks

[Topics and practice](https://dongshuyan.com/awesome-harness-memory/#tutorial/topics) develop four areas:

- **Safety and deletion:** how untrusted input becomes memory, why relevance differs from authorization, and why stopping retrieval differs from erasing copies.
- **Cost and capacity:** account for construction, maintenance, retrieval, and generation separately; inspect what compression loses.
- **Evaluation design:** connect a six-question coverage matrix to observable tasks and separate metrics, without inferring architecture from answer scores.
- **Local practice:** observe persistence, correction, scope filtering, expiry, and retrieval with a standard-library example and no API key.

```sh
python3 examples/memory_lab.py
```

The [practice guide](docs/practice.zh-CN.md) explains the expected output. The example does not call a model; its tests do not reproduce any upstream product's effectiveness.

## Preview and contribute

The builder and example use the Python standard library. The full test suite also needs Node.js to exercise JavaScript; no npm dependencies are required.

```sh
python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 -m unittest discover -s tests -v
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. [`site/tutorial.json`](site/tutorial.json) owns the course data; the builder generates the page. See [repository structure](docs/repository-structure.md) for maintenance details.

Contributions should include primary sources, versions, exact locations, examples, and limitations. Undocumented does not mean absent; author reports are distinct from independent replication; literary analogies are distinct from scientific evidence. See the [contribution requirements](CONTRIBUTING.md) and [maintenance roadmap](ROADMAP.md).
