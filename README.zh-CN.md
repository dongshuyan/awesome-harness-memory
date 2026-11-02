# Agent Memory Landscape

[English](README.md) | 简体中文

面向科研与应用开发者的 Agent Memory 精选导航：查找可用系统、阅读研究论文、选择评估方法，也从文学影视中的记忆设定获得启发。

每个条目简要介绍它的功能、值得关注的特点，以及进一步阅读的入口。

## 按需求查找

| 我想要…… | 从这里开始 |
| --- | --- |
| 管理对话中的状态和上下文 | [LangGraph](resources/systems.md#langgraph)、[Deep Agents](resources/systems.md#deep-agents) |
| 在多个 Session 之间保留有用信息 | [LangGraph stores](resources/systems.md#langgraph)、[Mem0](resources/systems.md#mem0)、[Memory Bank](resources/systems.md#google-agent-platform-memory-bank) |
| 追踪事实变化及其历史 | [Graphiti](resources/systems.md#graphiti) |
| 从已有任务中学习并组织经验 | [ReasoningBank](resources/papers.md#reasoningbank)、[A-Mem](resources/papers.md#a-mem)、[Generative Agents](resources/papers.md#generative-agents) |
| 评估对话记忆的召回、更新与不确定性处理 | [LoCoMo](resources/benchmarks.md#locomo)、[LongMemEval](resources/benchmarks.md#longmemeval)、[MemoryAgentBench](resources/benchmarks.md#memoryagentbench) |
| 评估记忆能否帮助 Agent 执行动作 | [Mem2ActBench](resources/benchmarks.md#mem2actbench) |
| 从文学影视理解记忆约束 | [文学与影视](resources/fiction.md) |

这些入口可以重叠。一个系统可能满足多种需求，不同项目中的同名术语也可能含义不同。正式分类和架构图将在比较实际机制之后设计；目前需要回答的问题见[调研问题](docs/research-questions.md)。

## 按对象浏览

- [系统与产品](resources/systems.md)：Agent 框架、Harness、记忆库和托管服务。
- [论文与研究报告](resources/papers.md)：按时间排列，并注明发表状态和原始来源。
- [Benchmark 与评估](resources/benchmarks.md)：测什么、适合了解什么，以及结果的适用边界。
- [文学与影视](resources/fiction.md)：记忆设定，以及明确标注为编辑解读的设计类比。

## 关于这一版

第一版的来源核对日期为 **2026-11-02**。各类先放少量完整样例，后续按调研轮次持续补充。仓库名称和导航结构均为暂定。

简介依据所链接的论文、项目文档，以及产品或出版方官方资料。这一版尚未安装运行系统、复现 Benchmark 或开展安全审计；产品文档代表厂商公开描述，文学影视类比属于编辑解读。

正文以英文为主，README 提供中文版。后续安排见[迭代计划](ROADMAP.md)、[待调研问题](docs/research-questions.md)和[贡献指南](CONTRIBUTING.md)。
