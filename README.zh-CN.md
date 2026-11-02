# Awesome Harness Memory

> 面向科研与应用开发者的 Agent Harness Memory 精选导航：梳理上下文管理、跨 Session 连续性、长期记忆、系统、Benchmark、论文，以及文学影视中的记忆设定。

[English](README.md) · [简体中文](README.zh-CN.md)

如果你正在构建、研究或评估 AI Agent，这里帮助你快速找到合适的记忆相关入口，并保留不同项目术语之间的差异。

在本仓库中，Harness 指围绕 Agent 的运行时与控制边界。只要有助于理解或评估 Agent Memory，我们也会收录独立记忆系统、托管服务、论文、Benchmark 和文学影视作品。

## 按需求查找

| 我想要…… | 从这里开始 |
| --- | --- |
| 理解上下文和对话状态 | [LangGraph](resources/systems.md#langgraph) · [Deep Agents](resources/systems.md#deep-agents) · [OpenAI Agents SDK](resources/systems.md#openai-agents-sdk) |
| 在多个 Session 之间承接信息 | [Google ADK](resources/systems.md#google-adk) · [Mem0](resources/systems.md#mem0) · [Letta](resources/systems.md#letta--letta-code) |
| 比较托管记忆服务 | [Google Agent Platform Memory Bank](resources/systems.md#google-agent-platform-memory-bank) · [Amazon Bedrock AgentCore Memory](resources/systems.md#amazon-bedrock-agentcore-memory) |
| 为多个 Agent 组织信息 | [CrewAI](resources/systems.md#crewai) |
| 追踪事实变化及其历史 | [Graphiti](resources/systems.md#graphiti) |
| 复用已有尝试和任务的经验 | [Reflexion](resources/papers.md#reflexion) · [ReasoningBank](resources/papers.md#reasoningbank) · [OpenAI Agents SDK](resources/systems.md#openai-agents-sdk) |
| 评估召回、更新、冲突和不确定性 | [LongMemEval](resources/benchmarks.md#longmemeval) · [LoCoMo](resources/benchmarks.md#locomo) · [MemoryAgentBench](resources/benchmarks.md#memoryagentbench) |
| 检查记忆是否改变工具调用 | [Mem2ActBench](resources/benchmarks.md#mem2actbench) |
| 考察记忆容量与读写耗时 | [MemBench](resources/benchmarks.md#membench) |
| 评估遗忘、视觉记忆和角色间共享 | [Memora](resources/benchmarks.md#memora) · [Mem-Gallery](resources/benchmarks.md#mem-gallery) · [COLLABMEM](resources/benchmarks.md#collabmem)（协议参考） |
| 考察成本对照与记忆投毒 | [Token-budget study](resources/papers.md#online-memory-under-token-budgets) · [AgentPoison](resources/papers.md#agentpoison) |
| 从故事中理解记忆约束 | [文学与影视](resources/fiction.md) — 有限回忆、外部记录、访问分隔、过度记忆和集体遗忘 |

顺序仅用于导航，不代表排名。

选择 benchmark 可先看[评测选择指南](docs/evaluation-guide.md)；比较不同项目的术语，可看[机制实例与开放问题](docs/research-questions.md)。

## 按资源类型浏览

- [系统与产品](resources/systems.md)：Agent 框架、Harness、独立记忆层和托管服务。
- [论文与研究报告](resources/papers.md)：按时间排列，并链接原始来源。
- [Benchmark 与评估](resources/benchmarks.md)：测什么，以及结论适用到哪里。
- [文学与影视](resources/fiction.md)：用于提出设计问题的记忆设定，并明确标注为类比。

这些分组是当前用于导航的暂定安排，后续可能随着调研发展而调整。

## 本仓库收录什么

仓库通过小批量调研持续更新，提供代表性入口，不声称是完整目录或排名。正式分类、条目格式和架构图仍保持开放，会在比较实际系统和评估方法的过程中继续确定。

## 关于这一版

来源核对日期：**2026-11-02**

- 条目链接到论文、官方文档、项目仓库或出版方/制作方资料。
- 产品行为依据项目或厂商公开文档概括，不推断内部实现。
- 不代表已经安装系统、复现 Benchmark、完成生产验证或安全审计。
- 文学影视条目属于编辑类比，不是模型认知或工程效果证据。

资源条目目前以英文为主；中文 README 提供导航和范围说明。继续阅读：[研究路线图](ROADMAP.md)、[待调研问题](docs/research-questions.md)、[仓库结构](docs/repository-structure.md)和[贡献指南](CONTRIBUTING.md)。

问题和建议会帮助我们决定下一轮优先调研什么；如果这个导航帮你节省了时间，也欢迎点 Star，帮助更多人找到它。
