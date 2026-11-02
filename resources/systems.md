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

A managed service that, according to Google's documentation, extracts and consolidates information from interactions and retrieves memories within a configured scope. Useful for comparing a provider-managed memory service with application-owned implementations. ADK connects through `VertexAiMemoryBankService`; see [Google ADK](#google-adk) for adapter-specific lifecycle limits. This entry covers documented behavior; service internals and deployment behavior were not independently examined.

## Google ADK

[Repository](https://github.com/google/adk-python) · [Memory service guide](https://github.com/google/adk-python/blob/3655990f6ce1e55c40c5710351f6cf06cde0669b/docs/guides/memory/memory_service/index.md)

Separates session state from retrieval over explicitly ingested interactions. An agent can request memories with `load_memory`, or the runtime can retrieve them before requests with `preload_memory`. Useful for comparing model-directed retrieval with automatic context preparation. Persistence and retrieval depend on the backend. Among built-in backends, the pinned guide documents `delete_memory` support only for the in-memory implementation; deleting a session also leaves previously ingested memory intact.

## OpenAI Agents SDK

[Repository](https://github.com/openai/openai-agents-python) · [Sessions](https://openai.github.io/openai-agents-python/sessions/) · [Sandbox agent memory](https://openai.github.io/openai-agents-python/sandbox/memory/)

Provides two distinct mechanisms: Sessions maintain conversation history, while sandbox agent memory uses models to distill recorded conversations into files that later runs can consult. Useful for separating conversation continuity from reusable task experience. File memory requires preserving the relevant workspace or snapshot; a fresh empty sandbox starts without those memories. Layouts and conversation identifiers determine how these memory artifacts are shared.

## CrewAI

[Repository](https://github.com/crewAIInc/crewAI) · [Memory guide, v1.15.34](https://docs.crewai.com/v1.15.34/en/concepts/memory)

The documented unified `Memory` interface organizes records into scopes, recalls across selected scopes, and uses model-assisted analysis and consolidation when saving information. Useful for exploring how agents can work with their own and shared information through one interface. It replaces separate short-term, long-term, entity, and external memory types. Analysis sends content to the configured model; scope organization alone should not be treated as a verified security boundary.

## Letta / Letta Code

[Letta Code repository](https://github.com/letta-ai/letta-code) · [Current SDK memory](https://docs.letta.com/agent-sdk/memory) · [MemFS](https://docs.letta.com/letta-code/memfs)

Uses an agent-owned Git repository for persistent memory, separating information kept in the prompt from reference files read when needed. Letta Code exposes this through a stateful agent harness, including background memory revision. Useful for studying editable, versioned context across conversations. Local-only agents require their own backup; sharing across machines depends on synchronization. The current SDK and MemFS documentation differ on which file paths are inlined, so check the applicable interface before adopting a layout.

## Amazon Bedrock AgentCore Memory

[Memory types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html) · [Memory strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html)

A managed service that separates raw interaction events from extracted memory records. Configured strategies can extract and consolidate information asynchronously, with built-in, customized, and self-managed processing options. Useful for comparing application-controlled memory processing with provider-managed extraction. Long-term extraction requires a configured strategy; storing conversation events alone does not enable it. AWS also cautions that event metadata is not intended for sensitive content.

The [research questions](../docs/research-questions.md) include scope, write control, retention, and the division of work between an agent and its harness.
