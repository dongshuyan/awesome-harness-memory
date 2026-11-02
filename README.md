# Awesome Harness Memory

> A curated guide to memory around AI agent harnesses: context management, session continuity, long-term memory, systems, benchmarks, research, and literary analogies.

[English](README.md) · [简体中文](README.zh-CN.md)

If you build, study, or evaluate an AI agent, this guide helps you find a useful starting point without treating every project's terminology as interchangeable.

In this guide, *harness* means the runtime and control boundary around an agent. We also include standalone memory systems, managed services, papers, benchmarks, and fiction when they help explain or evaluate memory in agent systems.

## Find by need

| I want to… | Start here |
| --- | --- |
| Understand context and conversation state | [LangGraph](resources/systems.md#langgraph) · [Deep Agents](resources/systems.md#deep-agents) · [OpenAI Agents SDK](resources/systems.md#openai-agents-sdk) |
| Carry information across sessions | [Google ADK](resources/systems.md#google-adk) · [Mem0](resources/systems.md#mem0) · [Letta](resources/systems.md#letta--letta-code) |
| Compare managed memory services | [Google Agent Platform Memory Bank](resources/systems.md#google-agent-platform-memory-bank) · [Amazon Bedrock AgentCore Memory](resources/systems.md#amazon-bedrock-agentcore-memory) |
| Organize information for several agents | [CrewAI](resources/systems.md#crewai) |
| Track changing facts and their history | [Graphiti](resources/systems.md#graphiti) |
| Reuse experience from earlier attempts and tasks | [Reflexion](resources/papers.md#reflexion) · [ReasoningBank](resources/papers.md#reasoningbank) · [OpenAI Agents SDK](resources/systems.md#openai-agents-sdk) |
| Evaluate recall, updates, conflicts, or uncertainty | [LongMemEval](resources/benchmarks.md#longmemeval) · [LoCoMo](resources/benchmarks.md#locomo) · [MemoryAgentBench](resources/benchmarks.md#memoryagentbench) |
| Check whether memory changes tool use | [Mem2ActBench](resources/benchmarks.md#mem2actbench) |
| Examine memory capacity and read/write time | [MemBench](resources/benchmarks.md#membench) |
| Evaluate forgetting, visual memory, or role-based sharing | [Memora](resources/benchmarks.md#memora) · [Mem-Gallery](resources/benchmarks.md#mem-gallery) · [COLLABMEM](resources/benchmarks.md#collabmem) (protocol reference) |
| Examine cost controls and memory poisoning | [Token-budget study](resources/papers.md#online-memory-under-token-budgets) · [AgentPoison](resources/papers.md#agentpoison) |
| Explore memory constraints through stories | [Fiction and screen](resources/fiction.md) — bounded recall, external records, separated access, excessive recall, and collective forgetting |

Order is for navigation, not ranking.

Choosing a benchmark? Start with the [evaluation guide](docs/evaluation-guide.md). Comparing terminology? See the [mechanism examples and open questions](docs/research-questions.md).

## Browse by resource type

- [Systems and products](resources/systems.md) — agent frameworks, harnesses, standalone memory layers, and managed services.
- [Papers and research reports](resources/papers.md) — a chronological reading timeline with primary sources.
- [Benchmarks and evaluation](resources/benchmarks.md) — what existing evaluations measure and where their conclusions stop.
- [Fiction and screen](resources/fiction.md) — memory settings that prompt design questions, clearly labeled as analogies.

These groupings are provisional and may change as the research develops.

## What this guide covers

The guide grows through small research updates. It offers representative starting points and does not claim to be a complete catalog or ranking. The taxonomy, entry format, and architecture map remain open while we compare real systems and evaluations.

## Current edition

Sources checked: **2026-11-02**

- Entries link to papers, official documentation, project repositories, or publisher/studio material.
- Product behavior is summarized from project or provider documentation; private internals are not inferred.
- No system installation, benchmark run, production validation, or security audit is implied.
- Fiction entries are editorial analogies, not evidence about model cognition or engineering performance.

Continue with the [research roadmap](ROADMAP.md), [open questions](docs/research-questions.md), [repository structure](docs/repository-structure.md), or [contribution guide](CONTRIBUTING.md).

Issues and suggestions help us decide what to investigate next. A star helps others find the guide.
