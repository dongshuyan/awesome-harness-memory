# Benchmarks and evaluation

[Home](../README.md) · [Paper timeline](papers.md) · [Open questions](../docs/research-questions.md)

Start with the behavior you need to measure. These are introductions to existing evaluations, with sources checked **2026-11-02**. No benchmark was run for this edition.

## LoCoMo

[Repository](https://github.com/snap-research/locomo) · [ACL 2024 paper](https://aclanthology.org/2024.acl-long.747/)

Evaluates memory over long conversations through question answering, event summarization, and multimodal dialogue generation. Useful when comparing how a system retains and uses conversational information. The released dataset contains ten long conversations. An evaluation using only its QA component should identify that subset; it does not cover the entire original benchmark or general application reliability.

## LongMemEval

[Paper and ICLR 2025 record](https://arxiv.org/abs/2410.10813)

Tests information extraction, reasoning across sessions, temporal reasoning, knowledge updates, and abstention. Useful for finding which kinds of conversational memory fail, rather than relying on one aggregate result. Results depend on the supplied history, retrieval setup, and evaluation protocol; success on chat-history questions does not itself establish successful tool execution.

## MemoryAgentBench

[Repository and evaluation instructions](https://github.com/HUST-AI-HYZ/MemoryAgentBench) · [Paper](https://arxiv.org/abs/2507.05257)

Studies memory through incremental information ingestion. The current README names retrieval, test-time learning, long-range understanding, and conflict resolution. Useful for examining how memory handles incoming information across different tasks. Earlier paper wording refers to selective forgetting; terminology and dataset revisions should be tied to the version evaluated. Task metrics differ, so numbers should not be combined as if they measured one common notion of accuracy.

## Mem2ActBench

[Repository](https://github.com/Cantaloupe-M/Mem2ActBench) · [ACL 2026 paper](https://aclanthology.org/2026.acl-long.370/)

Evaluates whether an agent uses earlier interactions to select tools and ground their arguments. Useful when a product needs remembered preferences or task state to affect actions. Its histories and tasks are constructed through a synthesis pipeline; the results concern that protocol, rather than an observed deployment with real users.

## Reading a reported result

Before comparing results, check whether the dataset version, task subset, model, available history, retrieval budget, and judge are comparable. Also check which costs are counted, including memory writing and consolidation. These are questions for interpreting the original experiments; this repository does not provide a combined leaderboard.

Evaluation of memory capabilities will expand alongside research on efficiency, forgetting, isolation, and effects on completed tasks. See the [roadmap](../ROADMAP.md).
