# Benchmarks and evaluation

[Home](../README.md) · [Choose an evaluation](../docs/evaluation-guide.md) · [Paper timeline](papers.md)

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

## MemBench

[Findings of ACL 2025 paper](https://aclanthology.org/2025.findings-acl.989/) · [Repository and data instructions](https://github.com/import-myself/Membench)

Evaluates factual and reflective memory when an agent participates in conversations or observes messages. Its protocol measures multiple-choice answering, evidence retrieval, capacity under added noise, and memory read/write time. Useful when accuracy alone hides storage or retrieval overhead. The constructed profiles and conversations, sampled test subsets, and multiple-choice format limit what the results establish about unconstrained tasks.

## Memora

[Findings of ACL 2026 paper](https://aclanthology.org/2026.findings-acl.1337/)

Tests remembering, reasoning, and recommending over simulated histories with additions, updates, and invalidations. Forgetting-Aware Memory Accuracy combines valid-information coverage with a penalty for using obsolete information, judged against explicit criteria. Useful when an assistant must follow a user's current state. This tests response behavior, not physical deletion from storage. The study uses constrained personas and LLM judges, and does not compare runtime or latency.

## Mem-Gallery

[ACL 2026 paper](https://aclanthology.org/2026.acl-long.1892/) · [Repository and dataset links](https://github.com/YuanchenBei/Mem-Gallery)

Tests visual and textual memory across sessions, including retrieval, temporal and visual reasoning, conflicts, and refusal when evidence is missing. Reports answer metrics, model-judged correctness, and retrieval diagnostics. Useful when important information is carried in images. Conversations are constructed and reviewed; text-only methods receive image captions. The scope does not cover audio, embodied interaction, or general planning and tool use.

## COLLABMEM

[EMNLP 2026 paper](https://aclanthology.org/2026.emnlp-main.1194/) · [Repository linked by the paper](https://github.com/NLPerWS/COLLABMEM)

A diagnostic protocol for sharing, withholding, routing, source attribution, updates, and retention across roles. It holds interaction traces and the answering layer fixed and uses semantic and stricter evidence-oriented grading. Useful for separating memory-access failures from planning failures. Its SDK comparisons use controlled sharing policies, not complete native team deployments; the authors also identify limitations in the compression metric. **Artifact status, 2026-11-02:** the linked repository is empty, so this is currently a protocol reference rather than a runnable starting point.

## Reading a reported result

Before comparing results, check whether the dataset version, task subset, model, available history, retrieval budget, and judge are comparable. Also check which costs are counted, including memory writing and consolidation. These are questions for interpreting the original experiments; this repository does not provide a combined leaderboard.

For a compact map from application needs to evaluations, see [Choose an evaluation](../docs/evaluation-guide.md). The [token-budget study](papers.md#online-memory-under-token-budgets) and [AgentPoison](papers.md#agentpoison) add cost and adversarial perspectives; neither is a general memory leaderboard.
