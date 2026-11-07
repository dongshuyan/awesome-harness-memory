# Awesome Harness Memory

> Understand how agents remember, update, and use information. Find useful methods, systems, papers, and evaluations.

[English](README.md) · [简体中文](README.zh-CN.md) · **[Explore the interactive guide (中文) →](https://dongshuyan.github.io/awesome-harness-memory/)**

For researchers, engineers, and curious learners: start with the memory landscape, understand the available approaches, then follow their features, highlights, limitations, and original sources.

Here, *harness* means the runtime and control boundary around an agent. The guide also includes standalone memory layers, managed services, personal assistants, human memory research, and literary analogies.

[![Seven questions about agent memory](assets/memory-landscape.en.svg)](https://dongshuyan.github.io/awesome-harness-memory/)

## Understand the landscape

| Question | What to look for |
| --- | --- |
| [Who manages memory?](docs/landscape.zh-CN.md#owner) | Agent, harness, memory service, application |
| [What is remembered?](docs/landscape.zh-CN.md#content) | Events, facts, procedures, experience, relations |
| [Who is it for, and how long does it last?](docs/landscape.zh-CN.md#scope) | Session, project, user, team, retention |
| [How is it stored and found?](docs/landscape.zh-CN.md#form) | Files, records, checkpoints, indexes, graphs |
| [How is it formed and maintained?](docs/landscape.zh-CN.md#operation) | Recording, extraction, consolidation, retrieval, revision, forgetting |
| [How does it inform the next action?](docs/landscape.zh-CN.md#use) | Preloading, active queries, persistent context, on-demand retrieval |
| [How is it traced and controlled?](docs/landscape.zh-CN.md#governance) | Permissions, provenance, conflicts, revocation, poisoning |

These are overlapping perspectives, not seven mutually exclusive memory types or seven required modules. Each topic introduces the problem and approaches before linking to implementations and evidence.

The expanded guide and detailed catalogue are currently **in Chinese**; source titles and original links retain their original languages. The earlier [English reference pages](resources/systems.md) and [bilingual concept map](explore/README.md) remain available with their narrower coverage marked.

## Find a useful starting point

- **[Browse systems and products](resources/systems.zh-CN.md)** — Pi, Codex, Claude Code, Claude-Mem, OpenClaw, Hermes, Letta Code, LangGraph, Mem0, Hindsight, MemOS, Graphiti, Zep, and more. ChatGPT Memory is a separate personal-assistant comparison.
- **[Start from your needs](docs/needs.zh-CN.md)** — continue across sessions, remember preferences, reuse experience, track changing facts, or coordinate several agents.
- **[Read papers and methods](resources/papers.zh-CN.md)** or **[start with surveys](resources/surveys.zh-CN.md)** — distinguish research claims from current product behavior.
- **[Choose evaluations](resources/benchmarks.zh-CN.md)** — examine recall, useful actions, updates, sharing, safety, and cost. The [English evaluation guide](docs/evaluation-guide.md) explains comparison conditions.
- **[Explore human memory](resources/human.zh-CN.md)** and **[fiction and screen](resources/fiction.zh-CN.md)** — cognitive and neural evidence, alongside clearly labeled analogies.

## Explore combinations visually

The [interactive guide](https://dongshuyan.github.io/awesome-harness-memory/) provides search, filters, explanations, and views for comparing documented system properties. Open **图解探索** for the layered diagram: select several perspectives, adjust the view, and highlight one system across layers.

The diagram covers the Harness / Agent entries identified in this catalogue, not an exhaustive industry list. It includes **22 real Harness / Agent profiles**, with three historical projects clearly labeled. Select objects and perspectives, then open any cell for its definition, conditions, and source. The [static preview](assets/memory-layers.svg) shows six of these objects across three perspectives. Unknown properties stay unknown; colors are not a quality ranking. Standalone memory services, plugins, and general frameworks remain in the resource directory.

README links and static images work directly on GitHub. For a local preview, run `python3 -m http.server 8000 --bind 127.0.0.1` from the repository root and open `http://127.0.0.1:8000/`.

## Coverage and evidence

Sources checked through **2026-11-07 UTC**. The catalogue contains **138 resources**: 56 with documented basic information, 47 research reading entries, 32 unresolved leads, and 3 historical entries. Within that total, **49 systems** have primary sources supporting their basic functional descriptions. Inspect the [structured catalogue](catalogue.json) for entries, sources, and status.

Document checks do not establish implementation completeness, reproduced performance, deployment maturity, or security certification. No system installation or benchmark execution is implied. Unresolved names and properties remain labeled; the catalogue is not exhaustive, and its counts are not market shares. Fiction illustrates design questions rather than supplying evidence about model cognition.

See the [contribution guide](CONTRIBUTING.md), [roadmap](ROADMAP.md), or [repository structure and publishing notes](docs/repository-structure.md). If the guide helps you learn or find useful work, a star helps others discover it.
