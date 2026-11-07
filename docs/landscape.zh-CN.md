# 记忆分类与方法导航

从九个问题学习记忆系统。分类树按来源展示；工程叫法允许重叠。九问是编者导航，不声称唯一、穷尽或完全正交。

[打开交互页面](https://dongshuyan.com/awesome-harness-memory/) · [资源目录](../README.zh-CN.md#从具体对象开始)

- [记忆分类 · Memory Types](#types)
- [记忆的控制方式 · Memory Control](#control)
- [记忆的组织范围 · Memory Scope](#scope)
- [记忆的保留期限 · Memory Retention](#retention)
- [记忆的表示形式 · Memory Representation](#representation)
- [记忆的存储载体 · Memory Storage](#storage)
- [记忆的写入与维护 · Memory Formation & Update](#write)
- [记忆的检索与使用 · Memory Retrieval & Use](#read)
- [记忆的权限与可信性 · Memory Access & Trust](#trust)

<a id="types"></a>
<a id="content"></a>

## 记忆分类 / Memory Types

有哪些记忆，分别解决什么问题？先看一种明确的研究分类，再对照熟悉的叫法。

What kinds of memory are distinguished by a named research framework, and what are they used for?

分类必须带上来源与问题。不同论文可能按架构角色、内容或用途分类；这里提供两种可切换的阅读入口，不把它们拼成唯一的分类树。

CoALA 分类：工作记忆；长期记忆下分情景、语义、程序性记忆。功能分类来自另一篇综述：工作、事实、经验记忆。这两套分类分别展示，不合成一棵互斥树。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)

### 工作记忆 / Working Memory

处理当前任务时保持活跃的信息。CoALA 中，它可以跨模型调用保留；每次模型输入只取其中需要的部分。

In CoALA, working memory holds information active for the current task across model calls; each prompt uses a relevant subset.

记录什么：当前目标、最近观察、正在考虑的计划，以及取回的知识。
什么时候用：正在推理、规划或决定下一步行动时。
用来做什么：让下一步围绕当前目标展开。

例子（编者构造）：你正在做一道数学题：题目条件、刚算出的中间结果、下一步计划，都暂时放在草稿纸上。

边界：Working Memory（工作记忆）与 Workspace Memory（工作区记忆）不是同一个术语；也不等于模型的上下文窗口。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)

### 长期记忆 / Long-term Memory

在 CoALA 架构中，保存可供后续取回的经历、知识和做法，与当前活跃的工作记忆分工。

In CoALA, long-term memory retains experiences, knowledge, and procedures that can be retrieved for later tasks.

记录什么：情景、语义和程序性记忆；内容不限于用户偏好。
什么时候用：需要利用此前的经验或已积累的知识时。
用来做什么：让已有的信息和能力在后续任务中继续发挥作用。

例子（编者构造）：你的笔记本里既有上周实验的记录，也有学到的公式和实验操作方法。它们可以长期保留，做题时只取出需要的部分。

边界：“长期”不对应统一天数。LangChain 还使用跨线程范围区分长短期；具体系统应注明自己的定义。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)

### 情景记忆 / Episodic Memory

保存发生过的具体经历：做过什么、观察到什么、结果怎样。

Episodic memory records particular experiences: what happened, what was observed, and what the outcome was.

记录什么：对话片段、任务轨迹、某次工具调用及结果。
什么时候用：需要回顾先前发生的事情或参考一个具体案例时。
用来做什么：提供经历依据，帮助追溯和参考。

例子（编者构造）：“昨天实验时，我先加了试剂 A，随后温度升高，最后实验失败。”这是一次具体经历，不是已经证明的通用规律。

边界：事件可以带有时间和关系。它们是记录的属性，不必单独成为与情景记忆并列的大类。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)

### 语义记忆 / Semantic Memory

保存关于世界、任务对象或自身的事实与知识。

Semantic memory stores facts and knowledge about the world, task objects, or the agent itself.

记录什么：概念、实体属性、用户偏好，以及已确认的关系。
什么时候用：回答问题或作决定时需要已知背景。
用来做什么：提供事实依据，保持理解和交互的一致性。

例子（编者构造）：“小林更喜欢中文说明。”这是一条关于小林的偏好；“小林昨天要求我改成中文”则是一条具体事件。

边界：语义记忆不等于“语义检索”。前者说明记什么，后者说明如何查找。

[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)

### 程序性记忆 / Procedural Memory

让 Agent 知道如何行动的能力与程序。CoALA 包括模型中的隐式能力和 Agent 代码；LangChain 也讨论行为指令。

Procedural memory supports how an agent acts; definitions may include capabilities in model weights, agent code, or behavioral instructions.

记录什么：可执行步骤、技能和行为指令；具体边界随框架定义而变。
什么时候用：需要按照已掌握的方式执行工作时。
用来做什么：复用做事的方法。

例子（编者构造）：“每次实验前先校准仪器，再检查样本标签。”这是可复用做法；“昨天我校准了仪器”只是一次经历。

边界：“程序性”不只指电脑程序。保存一段流程文字，也不等于系统已能可靠执行。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)

### 事实记忆 / Factual Memory

这篇综述按用途归纳的事实性资料，包括用户信息、历史事件与环境知识。

In this survey, factual memory provides information about users, past interactions, and the environment.

记录什么：对话信息、偏好、用户和环境的相关事实。
什么时候用：需要保持对话连贯、事实一致或理解环境时。
用来做什么：为当前交互提供可参考的背景。

例子（编者构造）：“实验室周五关闭”“用户希望结果按月份统计”，都可以作为后续工作的事实背景。

边界：这是该综述的功能分类；不能直接把它等同于另一套分类中的 Semantic Memory。

[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)

### 经验记忆 / Experiential Memory

这篇综述把可复用的案例、策略和技能，归为支持从经历中学习的记忆。

In this survey, experiential memory supports learning from reusable cases, strategies, and skills.

记录什么：历史案例、经验教训、工作流和技能。
什么时候用：新任务与过去的经历存在可参考之处时。
用来做什么：复用已有做法，或避免再次踩同样的坑。

例子（编者构造）：上次忘记备份原始数据导致返工，因此总结出“处理前先备份”的做法，并在下一次实验中采用。

边界：它与情景、程序性记忆会有交叉。这里展示的是另一套按功能组织的方法，不拼成统一的父子树。

[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)

### 工作记忆 / Working Memory（功能综述）

在这篇综述中，工作记忆指一次任务过程中主动管理上下文的机制，包括单轮与多轮场景。

In this survey, working memory actively manages context during a task, including single-turn and multi-turn settings.

记录什么：当前任务需要的信息，以及维持这些信息的状态。
什么时候用：正在推理、规划或决定下一步行动时。
用来做什么：在有限上下文中维持任务连续性。

例子（编者构造）：你正在做一道数学题：题目条件、刚算出的中间结果、下一步计划，都暂时放在草稿纸上。

边界：这一功能视角讨论压缩、状态整理和规划；与 CoALA 的架构模块定义侧重点不同。

[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)

### 常见工程叫法对照

#### 上下文记忆 / Context Memory

当对话越来越长、模型窗口装不下全部历史时，保住继续工作所需的信息，并在后续调用中重新提供。

上下文续接 → 主要关联工作记忆的管理。它也可以从长期记忆中取回所需的事实或经历。

这里是一种用途入口，不是新的内容类型。下方相关方法也不表示每个系统都同时采用。

例子（编者构造）：你写报告写到一半，桌面已经堆满资料。先写一张交接便条：“已完成第一章，下一步核对图表”，清理桌面后，再凭便条继续。

[Anthropic · Context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)；[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)

#### 工作区记忆 / Workspace Memory

围绕一个项目或任务保存资料，使下一次打开工作区时，能够接着原来的进度工作。

工作区 → 可能同时包含当前状态、经历、事实和方法。高亮表示可能涉及，不表示每个工作区都具备全部类型。

工作区说明资料围绕哪个项目组织；工作记忆说明当前正在使用的信息。工作区资料也可以长期保存。

例子（编者构造）：一个实验项目文件夹里有进度表、实验日志、设备信息和操作手册。它们服务同一项目，但分别保存状态、经历、事实和方法。

[Cline · Memory Bank](https://docs.cline.bot/best-practices/memory-bank)；[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)

#### 长期记忆 / Long-term Memory

在 CoALA 架构中，保存可供后续取回的经历、知识和做法，与当前活跃的工作记忆分工。

长期记忆 → 在 CoALA 中，下分情景、语义和程序性记忆。切换研究框架后，应按该来源的定义理解。

“长期”不对应统一天数。LangChain 还使用跨线程范围区分长短期；具体系统应注明自己的定义。

例子（编者构造）：你的笔记本里既有上周实验的记录，也有学到的公式和实验操作方法。它们可以长期保留，做题时只取出需要的部分。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)

<a id="types-working-context"></a>

### 当前工作集与上下文 / Working set & context management

为当前问题选择历史、摘要、目标或检索结果，再把需要的内容送入模型。

History, summaries, goals, or retrieved information selected for the current problem, with the needed subset supplied to the model.

什么时候用：模型窗口有限、任务仍在继续时。
用来做什么：保住当前目标、必要历史和下一步。

例子（编者构造）：桌上只放当前实验要用的几页；完整记录保存在文件夹里，需要时再拿出来。

边界：保存在窗口外的历史，尚未读入时不属于本次模型输入；工作记忆也不能简单等同于一次调用的上下文窗口。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[MemoryOS · 首版预印本](https://arxiv.org/abs/2506.06326)

继续阅读：[LangGraph](https://github.com/langchain-ai/langgraph)；[MemoryOS](https://arxiv.org/abs/2506.06326)；[Letta Code](https://github.com/letta-ai/letta-code)

<a id="types-events"></a>

### 经历与事件 / Episodic memory / Event records

记录某次对话、任务、观察、工具调用及结果。

Records of particular conversations, tasks, observations, tool calls, and their results.

什么时候用：需要回顾某次对话、工具调用或任务过程时。
用来做什么：保留可追溯的经历，供回顾和案例参考。

例子（编者构造）：“昨天用仪器 A 测了三次，第二次读数异常。”记录的是一次经历。

边界：保留细节有助于追溯，但不能假设所有历史都能放进一次模型输入。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[Generative Agents · 首版预印本](https://arxiv.org/abs/2304.03442)；[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)

继续阅读：[Generative Agents](https://arxiv.org/abs/2304.03442)；[Graphiti](https://github.com/getzep/graphiti)；[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)；[Claude-Mem](https://github.com/thedotmack/claude-mem)；[Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md)；[Mastra Memory](https://mastra.ai/docs/memory/overview)

<a id="types-facts"></a>

### 事实与用户偏好 / Semantic memory / Facts & preferences

提取可供后续交互使用的事实、属性与偏好。

Facts, attributes, and preferences extracted for use in later interactions.

什么时候用：新会话需要沿用背景知识或用户偏好时。
用来做什么：减少重复询问，为决策提供可更新的事实。

例子（编者构造）：“小林喜欢用中文看解释”是偏好；“昨天小林提了这个要求”是事件。

边界：事实可能改变；用户画像本身也不是使用这些信息的授权。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)；[MemoryBank · 首版预印本](https://arxiv.org/abs/2305.10250)

继续阅读：[Mem0](https://github.com/mem0ai/mem0)；[MemoryBank](https://arxiv.org/abs/2305.10250)；[Google Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)；[OpenAI Codex](https://learn.chatgpt.com/docs/customization/memories)；[Memobase](https://github.com/memodb-io/memobase)；[Honcho](https://github.com/plastic-labs/honcho)

<a id="types-procedures"></a>

### 步骤与流程 / Procedural memory / Procedures

保存“这件事怎么做”的步骤、操作说明和可执行流程。

Reusable steps, instructions, and workflows describing how to carry out a task.

什么时候用：需要复用已知操作步骤或技能时。
用来做什么：让做事方法能够再次被调用。

例子（编者构造）：实验前先校准仪器再检查标签，是可复用流程；昨天执行过它是事件。

边界：流程是否适用取决于环境和条件；保存流程不保证执行正确。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[Deep Agents · 项目仓库](https://github.com/langchain-ai/deepagents)；[Online memory under token budgets · 首版预印本](https://arxiv.org/abs/2606.15017)

继续阅读：[Deep Agents](https://github.com/langchain-ai/deepagents)；[Online memory under token budgets](https://arxiv.org/abs/2606.15017)；[Hermes Agent](https://github.com/NousResearch/hermes-agent)；[OpenViking](https://github.com/volcengine/OpenViking)

<a id="types-experience"></a>

### 可复用经验与策略 / Experiential memory / Strategies

从尝试结果中归纳以后可以参考的做法和适用条件。

Lessons and strategies drawn from previous attempts, together with conditions under which they may be useful.

什么时候用：过去任务中有能用于新任务的案例、策略或技能时。
用来做什么：积累经验并保留适用条件。

例子（编者构造）：一次实验失败后总结“先备份原始数据”，下次遇到同类任务时参考。

边界：反馈质量、额外尝试和迁移条件会影响收益。

[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[Reflexion · 首版预印本](https://arxiv.org/abs/2303.11366)；[ReasoningBank · 论文](https://arxiv.org/abs/2509.25140)

继续阅读：[Reflexion](https://arxiv.org/abs/2303.11366)；[ReasoningBank](https://arxiv.org/abs/2509.25140)；[Hindsight](https://github.com/vectorize-io/hindsight)；[Letta Code](https://github.com/letta-ai/letta-code)

<a id="types-relations"></a>

### 关系与时间事实 / Relational & temporal facts

记录谁与什么有关，以及一个事实在什么时候成立。

Information about relationships and the periods during which a fact holds.

什么时候用：需要区分关系和随时间变化的事实时。
用来做什么：让事实带上主体、关系与有效时间。

例子（编者构造）：“小林在三月负责项目 A，四月交给小周。”关系和时间说明了事实适用范围。

边界：用图表示是一种实现选择；关系存在不证明因果。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)

继续阅读：[Graphiti](https://github.com/getzep/graphiti)

<a id="types-rules"></a>

### 规则与约束 / Instructions / Constraints

保存用户约定、任务限制或组织规则，供后续工作参考。

User agreements, task constraints, and organizational rules retained for later work.

什么时候用：有需要沿用的行为要求或项目约定时。
用来做什么：为后续工作提供明确的规则。

例子（编者构造）：“只读原始数据，清洗结果另存。”是约束；把它记下来并不自动限制文件权限。

边界：保存了规则，不代表已经强制执行；权限与审计另见治理专题。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)；[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)；[COLLABMEM · EMNLP 2026 论文](https://aclanthology.org/2026.emnlp-main.1194/)

继续阅读：[Letta Code](https://github.com/letta-ai/letta-code)；[COLLABMEM](https://aclanthology.org/2026.emnlp-main.1194/)；[Claude Code](https://code.claude.com/docs/en/memory)；[Gemini CLI](https://www.geminicli.com/docs/cli/gemini-md)；[Cline Memory Bank](https://docs.cline.bot/prompting/cline-memory-bank)


<a id="control"></a>
<a id="owner"></a>

## 记忆的控制方式 / Memory Control

谁决定何时写入、读取、修改或删除？决定者和执行者可以不同。

Who decides when memory is written, read, updated, or deleted? The decision-maker and executor may differ.

控制方式回答“谁实际作决定”；权限回答“谁被允许这样做”。两者不能合成一个“管理者”。

<a id="control-agent-control"></a>

### Agent 主动调用 / Agent-directed control

让 Agent 通过工具选择何时写入、读取或整理信息。

The agent uses tools to decide when to write, retrieve, or organize information.

什么时候用：需要 Agent 按任务决定记什么或查什么时。
用来做什么：允许根据当前目标灵活选择记忆操作。

例子（编者构造）：组员发现一个易错点，主动要求把它记进项目笔记。

边界：适合需要灵活决策的任务；仍要检查工具权限、误写和遗漏。

[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)；[Google ADK · 项目仓库](https://github.com/google/adk-python)；[Claude Code · 功能原始来源](https://code.claude.com/docs/en/memory)

继续阅读：[Letta Code](https://github.com/letta-ai/letta-code)；[Google ADK](https://github.com/google/adk-python)；[Claude Code](https://code.claude.com/docs/en/memory)

<a id="control-harness-control"></a>

### Harness 自动维护 / Harness-managed control

运行环境保存对话或执行状态，并在后续运行时恢复、准备输入。

The runtime saves conversation or execution state and restores it or prepares inputs for later calls.

什么时候用：每轮调用或运行结束都需要一致保存、恢复时。
用来做什么：把固定的记忆步骤交给运行程序。

例子（编者构造）：会议系统每次散会自动保存记录，不需要参会者逐次提醒。

边界：适合重复出现的保存与恢复流程；保存内容和后端配置仍需明确。

[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[OpenAI Agents SDK · 项目仓库](https://github.com/openai/openai-agents-python)；[Pi · 功能原始来源](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md)；[OpenAI Codex · 功能原始来源](https://learn.chatgpt.com/docs/customization/memories)

继续阅读：[LangGraph](https://github.com/langchain-ai/langgraph)；[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)；[Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md)；[OpenAI Codex](https://learn.chatgpt.com/docs/customization/memories)；[Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/concepts/harness)

<a id="control-service-control"></a>

### 独立或托管记忆服务 / Memory service integration

把存储、提取和检索封装成接口，接入现有 Agent 或应用。

A memory component exposes storage, extraction, and retrieval through an interface used by an agent or application.

什么时候用：想把已有记忆服务接入 Agent 时。
用来做什么：分清调用方、服务和模型各自负责什么。

例子（编者构造）：你把资料交给档案室整理；何时送交和准许谁查阅，仍需约定。

边界：服务负责哪些工作、调用方还要负责什么，需要分别核对。

[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)；[Amazon Bedrock AgentCore Memory · 记忆类型](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[Google Agent Platform Memory Bank · 官方概览](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)；[Hindsight · 功能原始来源](https://github.com/vectorize-io/hindsight)

继续阅读：[Mem0](https://github.com/mem0ai/mem0)；[Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[Google Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)；[Hindsight](https://github.com/vectorize-io/hindsight)；[Memobase](https://github.com/memodb-io/memobase)；[Honcho](https://github.com/plastic-labs/honcho)；[MemOS](https://github.com/MemTensor/MemOS)

<a id="control-application-control"></a>

### 应用决定组合与边界 / Application-defined orchestration

应用将多个组件接起来，确定用户、项目、存储后端和权限。

The application combines components and defines user, project, backend, and permission boundaries.

什么时候用：需要组合多种记忆组件或制定流程时。
用来做什么：由应用明确触发条件、边界和组件分工。

例子（编者构造）：组长规定谁交记录、谁审核、档案放哪里，秘书按流程执行。

边界：框架提供能力，不表示每个应用都已配置全部能力。

[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[Deep Agents · 项目仓库](https://github.com/langchain-ai/deepagents)

继续阅读：[LangGraph](https://github.com/langchain-ai/langgraph)；[Deep Agents](https://github.com/langchain-ai/deepagents)


<a id="scope"></a>

## 记忆的组织范围 / Memory Scope

这份资料围绕哪个会话、任务、项目或身份组织？这里先讨论资料归组。

Which conversation, task, project, or identity organizes these records?

按团队分组不代表所有成员都有访问权；按会话分组也不代表会话结束就删除。

<a id="scope-thread"></a>

### 同一次会话或执行线程 / Thread-scoped memory

围绕一段对话保存消息、状态和检查点。

Messages, state, and checkpoints organized around one conversation or execution thread.

什么时候用：需要保持一段对话或同一执行线程的连续性时。
用来做什么：把同一交互的消息和状态组织在一起。

例子（编者构造）：把同一封邮件的所有回复放进一个邮件线程；保存多久是另一问题。

边界：线程是否能在重启后恢复，取决于持久化配置。

[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[OpenAI Agents SDK · 项目仓库](https://github.com/openai/openai-agents-python)；[Google ADK · 项目仓库](https://github.com/google/adk-python)；[Pi · 功能原始来源](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md)

继续阅读：[LangGraph](https://github.com/langchain-ai/langgraph)；[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)；[Google ADK](https://github.com/google/adk-python)；[Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md)

<a id="scope-workspace"></a>

### 任务、项目与工作区 / Task / Project / Workspace scope

把进度、文件和相关知识放在同一个任务或项目边界内。

Progress, files, and relevant knowledge organized within a task or project boundary.

什么时候用：跨会话、跨天或多人接手同一个项目时。
用来做什么：把目标、进度和项目材料归在一起。

例子（编者构造）：毕业设计文件夹里放计划、实验日志、论文草稿和待办。

边界：恢复状态与重新检索事实是不同需求，不能只靠一个“长期”标签判断。

[Deep Agents · 项目仓库](https://github.com/langchain-ai/deepagents)；[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)

继续阅读：[Deep Agents](https://github.com/langchain-ai/deepagents)；[Letta Code](https://github.com/letta-ai/letta-code)

<a id="scope-identity"></a>

### 用户、Agent 与团队 / User / Agent / Team scope

围绕身份组织记忆，支持个人偏好、Agent 自有信息或协作共享。

Records organized around a user, an agent identity, or a collaborating team.

什么时候用：需要按用户、Agent 身份或团队组织信息时。
用来做什么：使不同对象的资料可以分别查找与维护。

例子（编者构造）：共享课题资料按团队归组，个人阅读偏好按成员归组；是否有权读还要另查。

边界：组织范围和访问控制需分别检查，团队标签不等于安全边界。

[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)；[CrewAI · 项目仓库](https://github.com/crewAIInc/crewAI)；[COLLABMEM · EMNLP 2026 论文](https://aclanthology.org/2026.emnlp-main.1194/)

继续阅读：[Mem0](https://github.com/mem0ai/mem0)；[CrewAI](https://github.com/crewAIInc/crewAI)；[COLLABMEM](https://aclanthology.org/2026.emnlp-main.1194/)


<a id="retention"></a>

## 记忆的保留期限 / Memory Retention

资料保存到什么时候、在什么条件下清除？保留期与事实的有效期要分开。

How long are records retained, and under what conditions are they removed? Retention differs from fact validity.

这是保留政策；执行删除、压缩或更新，属于“写入与维护”。跨会话也不等于保留固定天数。

<a id="retention-persistence"></a>

### 跨会话保留与可恢复 / Persistence / Resumability

让上一次交互留下的信息能进入后续工作。

Information from a previous interaction remains available to support later work.

什么时候用：结束会话或程序重启后还要继续工作时。
用来做什么：让保存的资料或执行状态在之后仍可访问。

例子（编者构造）：下课后把草稿装进文件夹，第二天能继续；这并不决定文件夹属于哪个项目。

边界：保留原始事件、检查点和提炼后的事实，是三种不同的延续方式。

[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[Amazon Bedrock AgentCore Memory · 记忆类型](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[OpenAI Codex · 功能原始来源](https://learn.chatgpt.com/docs/customization/memories)；[Claude-Mem · 功能原始来源](https://github.com/thedotmack/claude-mem)

继续阅读：[LangGraph](https://github.com/langchain-ai/langgraph)；[Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[OpenAI Codex](https://learn.chatgpt.com/docs/customization/memories)；[Claude-Mem](https://github.com/thedotmack/claude-mem)；[ChatGPT Memory](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)

<a id="retention-expiry"></a>

### 更新、失效与保留策略 / Retention policy / Fact validity

区分旧信息不再适用、仍保留历史，以及真正删除。

Distinguish information becoming inapplicable, retaining a historical record, and actually deleting it.

什么时候用：事实会变化，或系统规定数据何时清除时。
用来做什么：分别描述存多久、事实何时成立和何时不再使用。

例子（编者构造）：会议通知留档一年，但“周五开会”只在那个周五有效；过期并不等于档案已删。

边界：当前目录未逐一核验所有产品的保留期或删除语义。

[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)；[Memora · 首版预印本](https://arxiv.org/abs/2604.20006)

继续阅读：[Graphiti](https://github.com/getzep/graphiti)；[Memora](https://arxiv.org/abs/2604.20006)

<a id="retention-ttl"></a>

### 到期清除 / Time to Live · TTL

记录保存到配置的时间或条件，然后由系统执行相应清理。

A configured time or condition determines when a record expires and is subject to the specified cleanup process.

什么时候用：需要按用途限制保留期限时。
用来做什么：让保留政策可描述、可核查。

例子（编者构造）：借阅卡规定七天到期；“到期”是规则，“归还或清除”是执行。

边界：到期字段存在不证明备份、日志和索引已全部物理删除。

[Google Agent Platform Memory Bank · 官方概览](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)

继续阅读：[Google Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)


<a id="representation"></a>
<a id="form"></a>

## 记忆的表示形式 / Memory Representation

信息被编码成什么样子？这与它放在哪个设备或服务里，是两个问题。

How is information represented or encoded?

图结构不等于“关系记忆”的唯一实现；向量表示也不等于语义记忆这个内容类别。

<a id="representation-records"></a>

### 原始记录、摘要与结构化字段 / Raw records / Summaries / Structured records

保留原文，或把信息整理成简短摘要与明确字段。

Information can retain its original form or be organized into summaries and explicit fields.

什么时候用：需要决定保留原文、摘要还是明确字段时。
用来做什么：在细节、可读性和便于查询之间作选择。

例子（编者构造）：同一节课可以保留录音、整理一页摘要，或填成“日期、主题、结论”表格。

边界：摘要会丢失细节，抽取也可能出错；来源应能被找回。

[Amazon Bedrock AgentCore Memory · 记忆类型](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[MemoryOS · 首版预印本](https://arxiv.org/abs/2506.06326)；[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)

继续阅读：[Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[MemoryOS](https://arxiv.org/abs/2506.06326)；[Mem0](https://github.com/mem0ai/mem0)

<a id="representation-graphs"></a>

### 关系图与时序图 / Knowledge graphs / Temporal graphs

把实体、事实、来源和有效时间组织成可查询关系。

Entities, facts, sources, and validity times are organized as queryable relationships.

什么时候用：对象关系及其变化对任务很重要时。
用来做什么：把实体、关系、来源或有效时间明确组织起来。

例子（编者构造）：把“人—负责—项目”画成关系，并注明交接日期；连线不自动说明因果。

边界：构图和更新需要成本；关系存在不证明因果。

[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)；[A-Mem · 首版预印本](https://arxiv.org/abs/2502.12110)

继续阅读：[Graphiti](https://github.com/getzep/graphiti)；[A-Mem](https://arxiv.org/abs/2502.12110)

<a id="representation-parametric"></a>

### 参数化记忆 / Parametric Memory

把知识或能力编码在模型参数中。CoALA 的程序性记忆也可能包含模型权重中的能力。

Knowledge or capabilities are encoded in model parameters; CoALA also discusses capabilities in model weights as procedural memory.

什么时候用：研究模型如何学习、积累和保留能力时。
用来做什么：让知识或做法通过模型自身参与输出。

例子（编者构造）：经反复练习后，你不必翻笔记就能执行一个熟悉动作；这只是类比。

边界：改参数与维护一条外部记忆记录不同，不能用同一种删除承诺描述。

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)；[Memory in the Age of AI Agents · 表示形式 §3](https://arxiv.org/html/2512.13564v2#S3)

继续阅读：[Titans: Learning to Memorize at Test Time](https://research.google/pubs/titans-learning-to-memorize-at-test-time/)

<a id="representation-latent"></a>

### 潜在表示记忆 / Latent Memory

以非自然语言的内部表示保留信息；状态如何形成与更新取决于具体方法。

Information is retained in non-language internal representations, whose formation and update depend on the specific method.

什么时候用：研究超越可读文本的记忆机制时。
用来做什么：用内部表示携带上下文或经验。

例子（编者构造）：像把复杂资料编码成只有配套解码器才能利用的符号；符号本身不能直接阅读。

边界：不把所有缓存一律称为已实现长期记忆，需看论文定义。

[Memory in the Age of AI Agents · 表示形式 §3](https://arxiv.org/html/2512.13564v2#S3)


<a id="storage"></a>

## 记忆的存储载体 / Memory Storage

信息实际存放在哪个组件中？存储载体与信息的表示形式有关联，但不相同。

Which component stores the information?

本地与远程是部署位置；是否保留到明天，是保留政策；能否被别人读取，是权限。

<a id="storage-files"></a>

### 文件与版本仓库 / Files / Versioned repositories

用可阅读、修改和保留版本的文件保存信息。

Readable and editable files carry information; version retention depends on the chosen storage setup.

什么时候用：需要人工阅读、编辑或检查修改记录时。
用来做什么：用文件承载信息，并按配置保存版本。

例子（编者构造）：项目笔记放在 Markdown 文件中，版本记录告诉你谁改了哪一行。

边界：容易人工检查；同步、冲突、权限和持久化仍要配置。

[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)；[Deep Agents · 项目仓库](https://github.com/langchain-ai/deepagents)；[Basic Memory · 功能原始来源](https://github.com/basicmachines-co/basic-memory)；[Cline Memory Bank · 功能原始来源](https://docs.cline.bot/prompting/cline-memory-bank)

继续阅读：[Letta Code](https://github.com/letta-ai/letta-code)；[Deep Agents](https://github.com/langchain-ai/deepagents)；[Basic Memory](https://github.com/basicmachines-co/basic-memory)；[Cline Memory Bank](https://docs.cline.bot/prompting/cline-memory-bank)；[ReMe](https://github.com/agentscope-ai/ReMe)

<a id="storage-checkpoints"></a>

### 检查点与命名空间存储 / Checkpoints / Namespace stores

检查点保留执行进度；分组存储把不同用户或任务的记录组织开来。

Checkpoints retain execution progress, while namespaced stores organize records for different users or tasks.

什么时候用：需要恢复执行状态或分组保存跨会话资料时。
用来做什么：把运行进度和可查询记录交给适合的存储组件。

例子（编者构造）：检查点像游戏存档；资料库像分类笔记。存档不自动变成能问答的知识库。

边界：检查点不是自动可检索的事实库；分组也不等于授权。

[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)

继续阅读：[LangGraph](https://github.com/langchain-ai/langgraph)


<a id="write"></a>
<a id="operation"></a>

## 记忆的写入与维护 / Memory Formation & Update

资料如何产生，以及保存后如何变化？这里讨论写入侧，不把读取混进来。

How are records created, consolidated, corrected, compressed, or deleted?

“保存 30 天”是政策；“到期执行删除”是操作。退出检索结果，也不证明存储中的内容已删除。

<a id="write-capture"></a>

### 记录与提取 / Recording / Extraction

保存事件，或从原始交互中抽取事实、偏好和任务信息。

Preserve events or extract facts, preferences, and task information from interactions.

什么时候用：交互或行动产生了值得保留的信息时。
用来做什么：形成原始记录或提取更小的信息单元。

例子（编者构造）：保留整场会议记录，再提取“周五前交实验结果”的待办；两者的来源应关联。

边界：应区分实际原话、模型推断和后来确认的结论。

[Amazon Bedrock AgentCore Memory · 记忆类型](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)

继续阅读：[Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)；[Mem0](https://github.com/mem0ai/mem0)

<a id="write-consolidate"></a>

### 整理、巩固与反思 / Consolidation / Reflection

合并重复信息，形成总结，或从经历中归纳经验。

Organize existing records into consolidated information, summaries, or lessons from experience.

什么时候用：多条记录重复、零散，或需要归纳经验时。
用来做什么：把已有记录整理成便于复用的摘要和经验。

例子（编者构造）：每次实验都有日志，周末整理出常见失败原因；总结仍可能有误。

边界：归纳会增加解释，也可能引入错误，不能丢掉原始依据。

[Generative Agents · 首版预印本](https://arxiv.org/abs/2304.03442)；[Reflexion · 首版预印本](https://arxiv.org/abs/2303.11366)；[ReasoningBank · 论文](https://arxiv.org/abs/2509.25140)

继续阅读：[Generative Agents](https://arxiv.org/abs/2304.03442)；[Reflexion](https://arxiv.org/abs/2303.11366)；[ReasoningBank](https://arxiv.org/abs/2509.25140)

<a id="write-revision"></a>

### 更新与历史失效 / Updating / Invalidation

新事实出现时修改记录，或让旧事实不再作为当前状态使用。

Revise records when new facts arrive or prevent outdated facts from being used as the current state.

什么时候用：新信息取代旧信息，或原记录有误时。
用来做什么：修正当前知识，同时按需要保存历史。

例子（编者构造）：小周接手项目后更新负责人，旧负责人仍可留作历史，不再当作当前负责人。

边界：保留旧版本和标注事实有效期是两件事。

[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)；[A-Mem · 首版预印本](https://arxiv.org/abs/2502.12110)

继续阅读：[Graphiti](https://github.com/getzep/graphiti)；[A-Mem](https://arxiv.org/abs/2502.12110)

<a id="write-compaction"></a>

### 压缩与分层整理 / Context compaction / Hierarchical memory

把有限输入空间留给更有用的信息，其他内容放到外部，按需再读。

Keep useful information within a limited input budget and retain other details externally for later access.

什么时候用：历史过长，或输入预算不足时。
用来做什么：把关键状态留在近处，细节移到外部按需取回。

例子（编者构造）：桌面放一页摘要，抽屉放完整报告；摘要没写到的内容要去抽屉查。

边界：节省上下文可能牺牲细节；需要核对任务质量与成本。

[MemoryOS · 首版预印本](https://arxiv.org/abs/2506.06326)；[Online memory under token budgets · 首版预印本](https://arxiv.org/abs/2606.15017)；[Pi · 功能原始来源](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md)；[Aider · 功能原始来源](https://aider.chat/docs/config/options.html)

继续阅读：[MemoryOS](https://arxiv.org/abs/2506.06326)；[Online memory under token budgets](https://arxiv.org/abs/2606.15017)；[Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md)；[Aider](https://aider.chat/docs/config/options.html)；[Mastra Memory](https://mastra.ai/docs/memory/overview)

<a id="write-forgetting"></a>

### 选择性遗忘与删除 / Forgetting / Deletion

研究何时不再使用旧信息，以及何时清除保存的记录。

Decide when to stop using old information and when to remove stored records.

什么时候用：信息过时、被撤回或达到清理条件时。
用来做什么：停止使用某些信息，或执行有明确范围的删除。

例子（编者构造）：从学习清单去掉旧公式，不等于笔记本里的那一页已经撕掉。

边界：答案不引用旧事实，不能作为物理删除成功的证据。

[Memora · 首版预印本](https://arxiv.org/abs/2604.20006)；[MemoryAgentBench · 仓库与评测说明](https://github.com/HUST-AI-HYZ/MemoryAgentBench)

继续阅读：[Memora](https://arxiv.org/abs/2604.20006)；[MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench)

<a id="write-write-timing"></a>

### 执行中写入或后台整理 / Hot-path / Background memory updates

在当前步骤保存信息，或把部分整理放到交互之外。

Save information within the current step or perform some memory processing in the background.

什么时候用：要在及时保存与交互延迟之间作取舍时。
用来做什么：决定当前步骤完成写入，还是交给后台整理。

例子（编者构造）：会议中记下待办立即可查；完整纪要晚上整理，下午查询时它还没准备好。

边界：后台处理可能有延迟；后续请求应考虑信息尚未完成处理的状态。

[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[Amazon Bedrock AgentCore Memory · 记忆类型](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)

继续阅读：[LangGraph](https://github.com/langchain-ai/langgraph)；[Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)


<a id="read"></a>
<a id="use"></a>

## 记忆的检索与使用 / Memory Retrieval & Use

当前任务如何找到资料、读入需要的部分，并用于回答或行动？

How is relevant information found, supplied to the current task, and used?

“检索命中”不等于“任务做对”。谁触发检索，与使用哪种检索方法，也要分别描述。

<a id="read-hybrid-search"></a>

### 相似度与混合检索 / Semantic / Keyword / Hybrid retrieval

按含义、关键词或多个信号寻找相关材料。

Find relevant material using semantic similarity, keywords, or multiple retrieval signals.

什么时候用：需要从大量材料中找到当前相关内容时。
用来做什么：综合语义、关键词或其他信号缩小候选范围。

例子（编者构造）：找“实验温度异常”时，既查“温度”原词，也找“过热”这类相近意思。

边界：相似不等于最新、正确或被允许访问。

[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)；[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)

继续阅读：[Mem0](https://github.com/mem0ai/mem0)；[Graphiti](https://github.com/getzep/graphiti)

<a id="read-selection"></a>

### 检索与筛选 / Retrieval / Selection

从已保存的信息中取回当前需要的部分。

Retrieve and select the portion of stored information needed for the current task.

什么时候用：当前问题只需要存量记忆的一部分时。
用来做什么：选出相关、适用且可用的材料。

例子（编者构造）：做第三章习题时，先挑出第三章笔记，再检查是否用了新版公式。

边界：检索命中还不等于被正确使用，后续读入与行动需另看。

[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)；[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)

继续阅读：[Graphiti](https://github.com/getzep/graphiti)；[Mem0](https://github.com/mem0ai/mem0)

<a id="read-fixed-context"></a>

### 常驻上下文 / Pinned / Always-in-context memory

每次模型调用都放入指定信息。

Include designated information in each model call, subject to the implementation and input budget.

什么时候用：每次模型调用都需要一小组背景或约束时。
用来做什么：让指定信息持续可见。

例子（编者构造）：每页实验记录顶部都写上安全要求；放太多提醒也会挤占页面。

边界：便于持续提供约束和背景，但占用输入容量。

[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)

继续阅读：[Letta Code](https://github.com/letta-ai/letta-code)

<a id="read-on-demand"></a>

### 按需检索或读文件 / On-demand retrieval / File reading

需要时再请求相关材料。

Request relevant information or read files when they are needed.

什么时候用：只有部分请求需要某份资料时。
用来做什么：需要时才读，减少无关内容占用。

例子（编者构造）：遇到忘记的步骤时再翻手册，不把整本手册抄进每页草稿。

边界：是否读、读多少和选哪些内容，会影响任务效果。

[Google ADK · 项目仓库](https://github.com/google/adk-python)；[Deep Agents · 项目仓库](https://github.com/langchain-ai/deepagents)；[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)；[OpenClaw · 功能原始来源](https://docs.openclaw.ai/concepts/memory)

继续阅读：[Google ADK](https://github.com/google/adk-python)；[Deep Agents](https://github.com/langchain-ai/deepagents)；[Mem0](https://github.com/mem0ai/mem0)；[OpenClaw](https://docs.openclaw.ai/concepts/memory)；[Memorix](https://github.com/AVIDS2/memorix)；[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/mcp-memory.md)

<a id="read-preload"></a>

### Agent 请求或运行时预载 / Tool-requested retrieval / Preloading

由 Agent 决定查询，或由程序在调用前准备相关信息。

The agent may request retrieval, or the runtime may prepare related information before a model call.

什么时候用：需要选择何时把相关材料送入模型时。
用来做什么：区分 Agent 主动查询和运行程序提前准备。

例子（编者构造）：学生自己去找书，或助教课前把参考页放在桌上，两者都可能帮助解题。

边界：触发位置与存储后端是不同选择，可以组合。

[Google ADK · 项目仓库](https://github.com/google/adk-python)；[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)

继续阅读：[Google ADK](https://github.com/google/adk-python)；[LangGraph](https://github.com/langchain-ai/langgraph)

<a id="read-application"></a>

### 回答、规划与工具行动 / Memory-conditioned answering / Planning / Acting

检查记忆是否改变回答、计划、工具选择或参数。

Examine whether memory changes answers, plans, tool choices, or tool parameters.

什么时候用：要判断记忆是否改变最终回答或行动时。
用来做什么：把找到的知识用于计划、工具选择和参数。

例子（编者构造）：知道实验温度上限后，实际把设备设在安全范围；背得出上限不等于设对参数。

边界：会回忆事实，并不自动意味着任务行动更成功。

[Mem2ActBench · 首版预印本](https://arxiv.org/abs/2601.19935)；[ReasoningBank · 论文](https://arxiv.org/abs/2509.25140)；[Online memory under token budgets · 首版预印本](https://arxiv.org/abs/2606.15017)

继续阅读：[Mem2ActBench](https://arxiv.org/abs/2601.19935)；[ReasoningBank](https://arxiv.org/abs/2509.25140)；[Online memory under token budgets](https://arxiv.org/abs/2606.15017)


<a id="trust"></a>
<a id="governance"></a>

## 记忆的权限与可信性 / Memory Access & Trust

哪些操作被允许、资料来自哪里、受到污染或出现错误后如何追查？

Which operations are permitted, where did information come from, and how are errors or attacks investigated?

资料按谁归组，不代表谁有访问权；保存过来源，也不能自动证明内容为真。

<a id="trust-access"></a>

### 权限与共享边界 / Access control / Sharing boundaries

检查谁能写入、读取、传播某段信息，以及共享是否符合角色约定。

Control who may write, read, or share information and whether sharing follows the intended boundaries.

什么时候用：多用户、团队共享或敏感资料场景中。
用来做什么：限制谁能读、写、传播或删除。

例子（编者构造）：团队共享实验记录，但个人联系方式只有经授权的成员可以读。

边界：同一个用户或团队标签本身不证明权限实现正确。

[COLLABMEM · EMNLP 2026 论文](https://aclanthology.org/2026.emnlp-main.1194/)

继续阅读：[COLLABMEM](https://aclanthology.org/2026.emnlp-main.1194/)

<a id="trust-provenance"></a>

### 原始来源与版本 / Provenance / Version history

保留记录的出处和变化，支持核对与纠正。

Retain the origin and revision history of records so their content can be checked and corrected.

什么时候用：需要核实信息出处或查清修改过程时。
用来做什么：把内容和原始依据、后续修订联系起来。

例子（编者构造）：笔记写“导师同意”，旁边保留邮件出处；这也仍需检查邮件原意。

边界：文件修改时间不等于事实有效期，二者需要分别解释。

[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)；[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)

继续阅读：[Graphiti](https://github.com/getzep/graphiti)；[Letta Code](https://github.com/letta-ai/letta-code)

<a id="trust-revocation"></a>

### 冲突、撤销与遗忘 / Conflict handling / Revocation

检查新旧信息冲突时采用什么，撤回的内容如何停止影响后续行为。

Check how conflicting records are handled and how withdrawn information stops affecting later behavior.

什么时候用：记录互相矛盾，或某条信息撤回授权时。
用来做什么：检查纠错和撤回是否在使用链条中生效。

例子（编者构造）：联系人撤回手机号共享许可后，搜索结果和缓存都需按系统的承诺处理。

边界：要区分答案层、检索层与存储层的处理。

[MemoryAgentBench · 仓库与评测说明](https://github.com/HUST-AI-HYZ/MemoryAgentBench)；[Memora · 首版预印本](https://arxiv.org/abs/2604.20006)；[COLLABMEM · EMNLP 2026 论文](https://aclanthology.org/2026.emnlp-main.1194/)

继续阅读：[MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench)；[Memora](https://arxiv.org/abs/2604.20006)；[COLLABMEM](https://aclanthology.org/2026.emnlp-main.1194/)

<a id="trust-poisoning"></a>

### 记忆投毒与不可信输入 / Memory poisoning / Untrusted input

研究恶意记录被检索后如何影响回答或工具动作。

Study how malicious records can influence answers or tool actions after being retrieved.

什么时候用：外部内容可能被写入长期存储并再次使用时。
用来做什么：分析恶意记忆怎样影响回答或工具行为。

例子（编者构造）：有人把“管理员要求公开名单”混进共享笔记；后来读到它不意味着这条命令可信。

边界：攻击研究只支持其威胁模型下的结论，不能据此给所有系统统一打分。

[AgentPoison · 首版预印本](https://arxiv.org/abs/2407.12784)

继续阅读：[AgentPoison](https://arxiv.org/abs/2407.12784)

以上关联用于导航，不表示每个条目实现了该专题的所有方法。来源核对深度、版本和限制见资源目录；未运行系统或复现评测。
