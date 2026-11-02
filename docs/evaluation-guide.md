# Choose an evaluation

[Home](../README.md) · [Benchmark entries](../resources/benchmarks.md) · [Research questions](research-questions.md)

Choose the behavior your application needs first. A system can answer questions about old conversations yet fail to use that information in an action. The resources below cover different questions; their scores are not interchangeable.

| What needs to work? | Starting points | What to check |
| --- | --- | --- |
| Recall and connect information from long conversations | [LoCoMo](../resources/benchmarks.md#locomo), [LongMemEval](../resources/benchmarks.md#longmemeval) | QA subset versus broader tasks; supplied history; updates and abstention |
| Use information as it arrives | [MemoryAgentBench](../resources/benchmarks.md#memoryagentbench) | Ingestion order, dataset revision, task-specific metrics |
| Respect changed preferences and invalidated facts | [Memora](../resources/benchmarks.md#memora) | Valid-information coverage and obsolete-information penalties; response correctness does not verify storage deletion |
| Put remembered information into tool calls | [Mem2ActBench](../resources/benchmarks.md#mem2actbench) | Tool selection and argument grounding; synthesized histories and tasks |
| Preserve and use visual evidence across sessions | [Mem-Gallery](../resources/benchmarks.md#mem-gallery) | Image access versus captions, retrieval evidence, visual reasoning and conflicts |
| Share information with the right role | [COLLABMEM](../resources/benchmarks.md#collabmem) | Visibility, provenance, and authority under a fixed trace; artifacts are not yet available in the linked repository |
| Handle capacity pressure and memory overhead | [MemBench](../resources/benchmarks.md#membench) | Noise and capacity settings, answering format, read/write timing |
| Justify memory's extra computation | [Online memory under token budgets](../resources/papers.md#online-memory-under-token-budgets) | All model calls, actor steps, context pruning, repeated runs, and whether tasks actually require earlier experience |
| Withstand poisoned stored information | [AgentPoison](../resources/papers.md#agentpoison) | Attacker write access, trigger optimization and transfer between embedders, and downstream actions |

These are entry points, not a complete test suite. Several may be needed for one application. Sources and limitations are linked in each resource entry; none was run for this guide.

## Make comparisons interpretable

Record the dataset revision, selected tasks, model and judge versions, prompts, and memory-visible information. Keep history availability and ingestion order explicit: building a store from all conversations in advance is a different setup from learning as sessions arrive. [MemoryAgentBench](../resources/benchmarks.md#memoryagentbench) and [Memora](../resources/benchmarks.md#memora) are useful protocol references.

Compare with simple alternatives appropriate to the task, such as no memory, full available history, or retrieval over unchanged records. Count writing, consolidation, retrieval, and answer generation where applicable. If budgets or preprocessing differ, report the difference. The [token-budget study](../resources/papers.md#online-memory-under-token-budgets) is particularly useful for seeing why actor steps and auxiliary calls both matter; its approximate budget matching also illustrates a limit that should remain visible.

Read failure categories alongside aggregate results. [Memora](../resources/benchmarks.md#memora) distinguishes missing current information from reuse of invalid information. [COLLABMEM](../resources/benchmarks.md#collabmem) makes source and role part of the question. A better total score can still leave the failure most relevant to your application unresolved.

## Add checks for your deployment

The cited tasks do not, by themselves, establish successful recovery after a restart, deletion from every storage copy, isolation between real users, or reliability in a live workflow. Add checks against the actual persistence, access, retention, and task contracts of the system you deploy. Keep that evidence separate from benchmark results.
