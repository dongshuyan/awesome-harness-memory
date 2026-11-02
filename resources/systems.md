# Systems and products

[Home](../README.md) · [Papers](papers.md) · [Evaluation](benchmarks.md)

Introductory examples, with sources checked on **2026-11-02**. Project descriptions retain the source's terminology; their placement here does not define a memory taxonomy. No system was installed or benchmarked for this edition.

## LangGraph

[Repository](https://github.com/langchain-ai/langgraph) · [Memory concepts](https://docs.langchain.com/oss/python/concepts/memory)

An orchestration framework whose memory documentation separates thread state persisted through checkpoints from information stored across threads in namespaces. This makes it a useful starting point for understanding how conversation continuity and shared information can have different lifetimes and scopes. Persistence and retrieval depend on the checkpointer, store, and application configuration.

## Deep Agents

[Repository](https://github.com/langchain-ai/deepagents) · [Memory](https://docs.langchain.com/oss/python/deepagents/memory) · [Backends](https://docs.langchain.com/oss/python/deepagents/backends)

An agent harness with files, planning, and subagents. Its memory interface lets an agent read selected files and, when permitted, update them across conversations. The backend determines persistence: the default state backend is thread-scoped, while a store backend can share files across threads. Useful for studying how a harness exposes durable information through ordinary file operations.

## Mem0

[Repository and documentation](https://github.com/mem0ai/mem0)

A memory layer with APIs for adding and searching information associated with users, agents, and sessions. Its appeal is an explicit memory interface that can be connected to an existing application. The repository describes open-source and hosted offerings; check the chosen edition before assuming that a documented feature is available in both.

## Graphiti

[Repository and documentation](https://github.com/getzep/graphiti)

A framework for building temporal context graphs from incoming information. It connects entities and facts with source episodes and time information, making it interesting when facts change and their history matters. It requires storage and model infrastructure around the framework. Invalidating an outdated fact and physically deleting information are separate operations to examine when selecting a design.

## Google Agent Platform Memory Bank

[Official overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) · [Memory generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/generate-memories)

A managed service that, according to Google's documentation, extracts and consolidates information from interactions and retrieves memories within a configured scope. Useful for comparing a provider-managed memory service with application-owned implementations. This entry covers documented behavior; service internals and deployment behavior were not independently examined.

The [research questions](../docs/research-questions.md) include scope, write control, retention, and the division of work between an agent and its harness.
