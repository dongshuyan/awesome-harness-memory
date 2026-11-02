# Papers and research reports

[Home](../README.md) · [Systems](systems.md) · [Benchmarks](benchmarks.md)

A small reading timeline, newest first by the **first arXiv submission date** checked below. Venue or later publication is stated separately. Sources checked **2026-11-02**; these summaries introduce the research questions and mechanisms, without independently reproducing reported results.

## Mem2ActBench

**2026-01-13** · [First preprint](https://arxiv.org/abs/2601.19935) · [ACL 2026, July proceedings](https://aclanthology.org/2026.acl-long.370/)

*Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents.* Tests whether earlier interactions inform tool selection and argument grounding. Start here when memory must support action. See the [benchmark entry](benchmarks.md#mem2actbench) for scope and limits.

## ReasoningBank

**2025-09-29** · [Paper](https://arxiv.org/abs/2509.25140) · [Google Research account](https://research.google/blog/reasoningbank-enabling-agents-to-learn-from-experience/)

*ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory.* Distills reusable strategies from experiences the agent judges successful or unsuccessful, then retrieves them for later tasks. Useful for studying memory of problem-solving experience. The authors and Google Research identify it as an ICLR 2026 paper. Self-judged outcomes and additional test-time computation are important conditions when interpreting the reported benefits.

## A-Mem

**2025-02-17** · [First preprint](https://arxiv.org/abs/2502.12110) · [NeurIPS 2025 proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html)

*A-Mem: Agentic Memory for LLM Agents.* Organizes memories as linked notes and allows incoming information to change existing notes. Its distinctive question is how memory organization can evolve after writing. A useful reference for comparing retrieval over fixed records with a memory structure that is itself updated.

## LongMemEval

**2024-10-14** · [First preprint and paper record](https://arxiv.org/abs/2410.10813) · ICLR 2025 (as stated in the paper record)

*LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.* Evaluates several abilities needed across extended chat histories, including updates and abstention. See the [benchmark entry](benchmarks.md#longmemeval) when choosing an evaluation.

## LoCoMo

**2024-02-27** · [First preprint](https://arxiv.org/abs/2402.17753) · [ACL 2024 proceedings](https://aclanthology.org/2024.acl-long.747/)

*Evaluating Very Long-Term Conversational Memory of LLM Agents.* Introduces long conversations and tasks covering questions, event summaries, and multimodal dialogue. See the [benchmark entry](benchmarks.md#locomo); a QA-only adaptation covers only part of the original work.

## Generative Agents

**2023-04-07** · [First preprint](https://arxiv.org/abs/2304.03442) · [Stanford publication record: UIST 2023](https://hci.stanford.edu/publications/paper.php?id=482)

*Generative Agents: Interactive Simulacra of Human Behavior.* Stores experiences, retrieves relevant memories, and synthesizes reflections to inform agent behavior. Included as a historical reference for the relationship between memory, reflection, and planning. Its simulated social setting has different goals from a deployed assistant or coding agent.

New papers and formal laboratory reports will be added through the [research rounds](../ROADMAP.md). A laboratory affiliation or a venue name alone does not establish that a result applies to a reader's task.
