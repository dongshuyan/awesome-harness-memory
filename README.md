# Agent Memory Landscape

English | [简体中文](README.zh-CN.md)

A curated guide to memory in AI agents: systems to build with, papers to learn from, benchmarks to evaluate with, and stories that make memory constraints easier to think about.

For researchers and application developers. Entries explain what a resource does, what makes it interesting, and where to start reading.

## Find by need

| I want to… | Start here |
| --- | --- |
| Manage conversation state and context across turns | [LangGraph](resources/systems.md#langgraph), [Deep Agents](resources/systems.md#deep-agents) |
| Carry useful information across sessions | [LangGraph stores](resources/systems.md#langgraph), [Mem0](resources/systems.md#mem0), [Memory Bank](resources/systems.md#google-agent-platform-memory-bank) |
| Track changing facts and their history | [Graphiti](resources/systems.md#graphiti) |
| Learn from earlier tasks and organize experience | [ReasoningBank](resources/papers.md#reasoningbank), [A-Mem](resources/papers.md#a-mem), [Generative Agents](resources/papers.md#generative-agents) |
| Evaluate conversational recall, updates, and uncertainty | [LoCoMo](resources/benchmarks.md#locomo), [LongMemEval](resources/benchmarks.md#longmemeval), [MemoryAgentBench](resources/benchmarks.md#memoryagentbench) |
| Check whether memory helps an agent act | [Mem2ActBench](resources/benchmarks.md#mem2actbench) |
| Explore memory constraints through literature and film | [Fiction and screen](resources/fiction.md) |

These routes can overlap. A system may support several needs, and similar labels can mean different things across projects. The [research questions](docs/research-questions.md) explain what remains to be compared before a memory taxonomy or architecture map is proposed.

## Browse by resource

- [Systems and products](resources/systems.md): agent frameworks, harnesses, memory libraries, and managed services.
- [Papers and research reports](resources/papers.md): a timeline with publication status and primary sources.
- [Benchmarks and evaluation](resources/benchmarks.md): what a benchmark tests, why it is useful, and the limits of its conclusions.
- [Fiction and screen](resources/fiction.md): memory settings and explicitly labeled design analogies.

## About this edition

Initial edition, sources checked **2026-11-02**. It contains a small set of introductory examples across the scope; coverage grows through successive research rounds. The title and navigation are provisional.

Descriptions are based on the linked papers, project documentation, and official product or publisher material. This edition has not installed the systems, reproduced benchmark results, or audited security. Product documentation describes the provider's stated behavior. Fiction analogies are editorial interpretations.

English is the working language; this README also has a Chinese version. See the [roadmap](ROADMAP.md), [open questions](docs/research-questions.md), and [contribution guide](CONTRIBUTING.md).
