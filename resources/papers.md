# Papers and research reports

> Earlier English reference edition (sources checked 2026-11-02). See the [expanded current catalogue in Chinese](papers.zh-CN.md) or the [interactive guide](https://dongshuyan.github.io/awesome-harness-memory/) for the latest coverage.

[Home](../README.md) · [Systems](systems.md) · [Benchmarks](benchmarks.md)

A reading timeline, newest first by the verified **first arXiv submission date**. Entries whose preprint dates remain unverified appear after the timeline. Venue or later publication is stated separately. Sources checked **2026-11-02**; these summaries introduce the research questions and mechanisms, without independently reproducing reported results.

## Online memory under token budgets

**2026-06-12** · [First preprint](https://arxiv.org/abs/2606.15017) · [EMNLP 2026 paper](https://aclanthology.org/2026.emnlp-main.1657/)

*Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents.* Compares online workflow, skill, and reasoning-memory modules with a base actor given more steps and context pruning. Useful for examining total token accounting and variation across runs. Budget matching is approximate; the tested web tasks are largely self-contained, so the findings do not settle the value of memory in tasks that depend on earlier episodes.

## Memora

**2026-04-21** · [First preprint](https://arxiv.org/abs/2604.20006) · [Findings of ACL 2026](https://aclanthology.org/2026.findings-acl.1337/)

*From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents.* Tests remembering, reasoning, and recommending as preferences, activities, and goals change. Its scoring penalizes use of invalidated information. See the [benchmark entry](benchmarks.md#memora) for what this establishes about forgetting.

## Mem2ActBench

**2026-01-13** · [First preprint](https://arxiv.org/abs/2601.19935) · [ACL 2026, July proceedings](https://aclanthology.org/2026.acl-long.370/)

*Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents.* Tests whether earlier interactions inform tool selection and argument grounding. Start here when memory must support action. See the [benchmark entry](benchmarks.md#mem2actbench) for scope and limits.

## Mem-Gallery

**2026-01-07** · [First preprint](https://arxiv.org/abs/2601.03515) · [ACL 2026 paper](https://aclanthology.org/2026.acl-long.1892/)

*Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents.* Extends conversation-memory evaluation to visual evidence, cross-session reasoning, and changing knowledge. See the [benchmark entry](benchmarks.md#mem-gallery) for its vision-language setting and controls.

## ReasoningBank

**2025-09-29** · [Paper](https://arxiv.org/abs/2509.25140) · [Google Research account](https://research.google/blog/reasoningbank-enabling-agents-to-learn-from-experience/)

*ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory.* Distills reusable strategies from experiences the agent judges successful or unsuccessful, then retrieves them for later tasks. Useful for studying memory of problem-solving experience. The authors and Google Research identify it as an ICLR 2026 paper. Self-judged outcomes and additional test-time computation are important conditions when interpreting the reported benefits.

## MemBench

**2025-06-20** · [First preprint](https://arxiv.org/abs/2506.21605) · [Findings of ACL 2025](https://aclanthology.org/2025.findings-acl.989/)

*MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents.* Compares factual and reflective memory in participation and observation scenarios, including retrieval, answering, capacity, and read/write time. See the [benchmark entry](benchmarks.md#membench) for the protocol and its limits.

## MemoryOS

**2025-05-30** · [First preprint](https://arxiv.org/abs/2506.06326) · [EMNLP 2025 paper](https://aclanthology.org/2025.emnlp-main.1318/) · [Author repository](https://github.com/BAI-LAB/MemoryOS)

*Memory OS of AI Agent.* Organizes recent dialogue, topic-based dialogue segments, and longer-lived persona information, with explicit storage, update, retrieval, and generation operations. Useful for examining migration and retrieval across memory stores. Evaluation uses GVD and LoCoMo; capacities are set empirically and topic segments lack dynamic merging. This is a different project from MemOS.

## A-Mem

**2025-02-17** · [First preprint](https://arxiv.org/abs/2502.12110) · [NeurIPS 2025 proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html)

*A-Mem: Agentic Memory for LLM Agents.* Organizes memories as linked notes and allows incoming information to change existing notes. Its distinctive question is how memory organization can evolve after writing. A useful reference for comparing retrieval over fixed records with a memory structure that is itself updated.

## LongMemEval

**2024-10-14** · [First preprint and paper record](https://arxiv.org/abs/2410.10813) · ICLR 2025 (as stated in the paper record)

*LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.* Evaluates several abilities needed across extended chat histories, including updates and abstention. See the [benchmark entry](benchmarks.md#longmemeval) when choosing an evaluation.

## AgentPoison

**2024-07-17** · [First preprint](https://arxiv.org/abs/2407.12784) · [NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html)

*AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases.* Studies how poisoned retrieval entries can redirect later agent behavior. Useful for designing memory threat models and separating retrieval compromise from action-level failure. Its setup assumes record insertion and embedding-model access for trigger optimization. The authors also report transfer to other embedders, linking this to similar training-data distributions. A closed embedding interface is therefore not established as a defense; the experiments do not show that every memory system has the same exposure.

## LoCoMo

**2024-02-27** · [First preprint](https://arxiv.org/abs/2402.17753) · [ACL 2024 proceedings](https://aclanthology.org/2024.acl-long.747/)

*Evaluating Very Long-Term Conversational Memory of LLM Agents.* Introduces long conversations and tasks covering questions, event summaries, and multimodal dialogue. See the [benchmark entry](benchmarks.md#locomo); a QA-only adaptation covers only part of the original work.

## MemoryBank

**2023-05-17** · [First preprint](https://arxiv.org/abs/2305.10250) · [AAAI 2024 publication](https://doi.org/10.1609/aaai.v38i17.29946) · [Author repository](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)

*MemoryBank: Enhancing Large Language Models with Long-Term Memory.* Combines conversation records, event summaries, user information, and retrieval with an exploratory decay-and-reinforcement mechanism. Useful as an early reference for personalized memory and selective retention. Its companion-agent study includes simulated conversations; the forgetting analogy does not establish biological fidelity or reliability in other applications.

## Generative Agents

**2023-04-07** · [First preprint](https://arxiv.org/abs/2304.03442) · [Stanford publication record: UIST 2023](https://hci.stanford.edu/publications/paper.php?id=482)

*Generative Agents: Interactive Simulacra of Human Behavior.* Stores experiences, retrieves relevant memories, and synthesizes reflections to inform agent behavior. Included as a historical reference for the relationship between memory, reflection, and planning. Its simulated social setting has different goals from a deployed assistant or coding agent.

## Reflexion

**2023-03-20** · [First preprint](https://arxiv.org/abs/2303.11366) · [NeurIPS 2023 paper](https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)

*Reflexion: Language Agents with Verbal Reinforcement Learning.* Turns task feedback into reflective text that informs subsequent attempts, without updating model weights. Useful as a foundation for experience memory and feedback-driven retries. The experiments use bounded reflection buffers and task-specific feedback; their benefits depend on feedback quality and repeated attempts, rather than demonstrating indefinite learning across arbitrary tasks.

**Proceedings date only — not ordered within the preprint timeline**

## COLLABMEM

**2026-10** · Proceedings month; earlier preprint date unverified · [EMNLP 2026 paper](https://aclanthology.org/2026.emnlp-main.1194/)

*COLLABMEM: A Diagnostic Benchmark for Collaborative Memory Operations in Multi-Agent LLM Systems.* Uses controlled traces and role-specific probes to study sharing, access, provenance, and conflicting updates. See the [benchmark entry](benchmarks.md#collabmem) for its evaluation boundary and artifact availability.

New papers and formal laboratory reports will be added through the [research rounds](../ROADMAP.md). A laboratory affiliation or a venue name alone does not establish that a result applies to a reader's task.
