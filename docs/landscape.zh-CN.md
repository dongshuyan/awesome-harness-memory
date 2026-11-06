# 从七个问题理解 Memory

[返回 README](../README.zh-CN.md)

这七个问题是可交叉的导航视角，不是互斥的记忆种类、七个必备模块或唯一分类。

<a id="owner"></a>

## 谁在管理记忆？

先看谁决定写入、读取和更新。一个系统可以把这些工作分给不同部分；产品名里有没有 Memory，并不能说明全部职责。

Agent 是执行任务并作出选择的主体；Harness 是组织模型调用、工具和状态的运行环境。两者可以共同管理记忆。

<details>
<summary>用生活例子理解</summary>

小组成员决定记下什么，秘书保存会议进度，档案室负责存放。一个小组可以同时采用三种做法。

</details>

### Agent 主动调用

让 Agent 通过工具选择何时写入、读取或整理信息。

使用时要看：适合需要灵活决策的任务；仍要检查工具权限、误写和遗漏。

[Letta Code](../resources/systems.zh-CN.md#letta-code) · [Google ADK](../resources/systems.zh-CN.md#google-adk) · [Claude Code](../resources/systems.zh-CN.md#claude-code)

### Harness 自动维护

运行环境保存对话或执行状态，并在后续运行时恢复、准备输入。

使用时要看：适合重复出现的保存与恢复流程；保存内容和后端配置仍需明确。

[LangGraph](../resources/systems.zh-CN.md#langgraph) · [OpenAI Agents SDK](../resources/systems.zh-CN.md#openai-agents-sdk) · [Pi](../resources/systems.zh-CN.md#pi) · [OpenAI Codex](../resources/systems.zh-CN.md#codex) · [Microsoft Agent Framework](../resources/systems.zh-CN.md#microsoft-agent-framework)

### 独立或托管记忆服务

把存储、提取和检索封装成接口，接入现有 Agent 或应用。

使用时要看：服务负责哪些工作、调用方还要负责什么，需要分别核对。

[Mem0](../resources/systems.zh-CN.md#mem0) · [Amazon Bedrock AgentCore Memory](../resources/systems.zh-CN.md#amazon-bedrock-agentcore-memory) · [Google Agent Platform Memory Bank](../resources/systems.zh-CN.md#google-agent-platform-memory-bank) · [Hindsight](../resources/systems.zh-CN.md#hindsight) · [Memobase](../resources/systems.zh-CN.md#memobase) · [Honcho](../resources/systems.zh-CN.md#honcho) · [MemOS](../resources/systems.zh-CN.md#memos)

### 应用决定组合与边界

应用将多个组件接起来，确定用户、项目、存储后端和权限。

使用时要看：框架提供能力，不表示每个应用都已配置全部能力。

[LangGraph](../resources/systems.zh-CN.md#langgraph) · [Deep Agents](../resources/systems.zh-CN.md#deep-agents)

<a id="content"></a>

## 记住什么？

先区分保存的内容，再看它在任务里起什么作用。同一段信息可以从事件记录中提炼成事实、流程或经验。

“工作集”描述当前选来使用的材料。模型本轮实际收到的 Context（上下文）包含其中一部分；外部保存的历史还没有读入时，不等于已在上下文中。

<details>
<summary>用生活例子理解</summary>

“上周五开过会”是事件；“小林喜欢上午开会”是偏好；“会前先发议程”是流程；“上次议程太晚导致返工”可以提炼成经验。

</details>

### 经历与事件

记录某次对话、任务、观察、工具调用及结果。

使用时要看：保留细节有助于追溯，但不能假设所有历史都能放进一次模型输入。

[Generative Agents](../resources/papers.zh-CN.md#generative-agents) · [Graphiti](../resources/systems.zh-CN.md#graphiti) · [OpenAI Agents SDK](../resources/systems.zh-CN.md#openai-agents-sdk) · [Claude-Mem](../resources/systems.zh-CN.md#claude-mem) · [Pi](../resources/systems.zh-CN.md#pi) · [Mastra Memory](../resources/systems.zh-CN.md#mastra)

### 事实与用户偏好

提取可供后续交互使用的事实、属性与偏好。

使用时要看：事实可能改变；用户画像本身也不是使用这些信息的授权。

[Mem0](../resources/systems.zh-CN.md#mem0) · [MemoryBank](../resources/papers.zh-CN.md#memorybank) · [Google Agent Platform Memory Bank](../resources/systems.zh-CN.md#google-agent-platform-memory-bank) · [OpenAI Codex](../resources/systems.zh-CN.md#codex) · [Memobase](../resources/systems.zh-CN.md#memobase) · [Honcho](../resources/systems.zh-CN.md#honcho)

### 步骤与流程

保存“这件事怎么做”的步骤、操作说明和可执行流程。

使用时要看：流程是否适用取决于环境和条件；保存流程不保证执行正确。

[Deep Agents](../resources/systems.zh-CN.md#deep-agents) · [Online memory under token budgets](../resources/papers.zh-CN.md#online-memory-under-token-budgets) · [Hermes Agent](../resources/systems.zh-CN.md#hermes) · [OpenViking](../resources/systems.zh-CN.md#openviking)

### 可复用经验与策略

从尝试结果中归纳以后可以参考的做法和适用条件。

使用时要看：反馈质量、额外尝试和迁移条件会影响收益。

[Reflexion](../resources/papers.zh-CN.md#reflexion) · [ReasoningBank](../resources/papers.zh-CN.md#reasoningbank) · [Hindsight](../resources/systems.zh-CN.md#hindsight) · [Letta Code](../resources/systems.zh-CN.md#letta-code)

### 关系与时间事实

记录谁与什么有关，以及一个事实在什么时候成立。

使用时要看：用图表示是一种实现选择；关系存在不证明因果。

[Graphiti](../resources/systems.zh-CN.md#graphiti)

### 规则与约束

保存用户约定、任务限制或组织规则，供后续工作参考。

使用时要看：保存了规则，不代表已经强制执行；权限与审计另见治理专题。

[Letta Code](../resources/systems.zh-CN.md#letta-code) · [COLLABMEM](../resources/papers.zh-CN.md#collabmem) · [Claude Code](../resources/systems.zh-CN.md#claude-code) · [Gemini CLI](../resources/systems.zh-CN.md#gemini-cli) · [Cline Memory Bank](../resources/systems.zh-CN.md#cline)

### 当前工作集与上下文

为当前问题选择历史、摘要、目标或检索结果，再把需要的内容送入模型。

使用时要看：为了以后而保存的信息属于外部记忆；读入当前请求后，才成为当前上下文的一部分。

[LangGraph](../resources/systems.zh-CN.md#langgraph) · [MemoryOS](../resources/papers.zh-CN.md#memoryos) · [Letta Code](../resources/systems.zh-CN.md#letta-code)

<a id="scope"></a>

## 为谁保存，保留多久？

范围回答信息围绕谁或什么任务组织；持续时间回答什么时候还保留。它们相关，但不能互相替代。

跨会话不一定是用户画像，项目文件也可以跨会话保留。按用户标识分组，不自动证明权限隔离正确。

<details>
<summary>用生活例子理解</summary>

同一个社团既有每场会议的记录，也有全年项目档案。档案属于谁，与它会保存几个月，是两个问题。

</details>

### 同一次会话或执行线程

围绕一段对话保存消息、状态和检查点。

使用时要看：线程是否能在重启后恢复，取决于持久化配置。

[LangGraph](../resources/systems.zh-CN.md#langgraph) · [OpenAI Agents SDK](../resources/systems.zh-CN.md#openai-agents-sdk) · [Google ADK](../resources/systems.zh-CN.md#google-adk) · [Pi](../resources/systems.zh-CN.md#pi)

### 任务、项目与工作区

把进度、文件和相关知识放在同一个任务或项目边界内。

使用时要看：恢复状态与重新检索事实是不同需求，不能只靠一个“长期”标签判断。

[Deep Agents](../resources/systems.zh-CN.md#deep-agents) · [Letta Code](../resources/systems.zh-CN.md#letta-code)

### 用户、Agent 与团队

围绕身份组织记忆，支持个人偏好、Agent 自有信息或协作共享。

使用时要看：组织范围和访问控制需分别检查，团队标签不等于安全边界。

[Mem0](../resources/systems.zh-CN.md#mem0) · [CrewAI](../resources/systems.zh-CN.md#crewai) · [COLLABMEM](../resources/papers.zh-CN.md#collabmem)

### 跨会话保留与可恢复

让上一次交互留下的信息能进入后续工作。

使用时要看：保留原始事件、检查点和提炼后的事实，是三种不同的延续方式。

[LangGraph](../resources/systems.zh-CN.md#langgraph) · [Amazon Bedrock AgentCore Memory](../resources/systems.zh-CN.md#amazon-bedrock-agentcore-memory) · [OpenAI Codex](../resources/systems.zh-CN.md#codex) · [Claude-Mem](../resources/systems.zh-CN.md#claude-mem) · [ChatGPT Memory](../resources/systems.zh-CN.md#chatgpt-memory)

### 更新、失效与保留策略

区分旧信息不再适用、仍保留历史，以及真正删除。

使用时要看：当前目录未逐一核验所有产品的保留期或删除语义。

[Graphiti](../resources/systems.zh-CN.md#graphiti) · [Memora](../resources/papers.zh-CN.md#memora)

<a id="form"></a>

## 用什么保存和查找？

这部分关注信息如何被表示和保存，以及怎样找到它。同一个事实可以同时有文本、字段、向量索引和图关系。

向量索引是按相似含义查找的手段；图是表示关系的方式。它们不等于“事实记忆”或“经验记忆”这样的内容类别。

<details>
<summary>用生活例子理解</summary>

图书馆里有书的正文、按栏目填写的目录、关键词索引，也有作者和作品的关系。它们帮助你以不同方式找到同一本书。

</details>

### 文件与版本仓库

用可阅读、修改和保留版本的文件保存信息。

使用时要看：容易人工检查；同步、冲突、权限和持久化仍要配置。

[Letta Code](../resources/systems.zh-CN.md#letta-code) · [Deep Agents](../resources/systems.zh-CN.md#deep-agents) · [Basic Memory](../resources/systems.zh-CN.md#basic-memory) · [Cline Memory Bank](../resources/systems.zh-CN.md#cline) · [ReMe](../resources/systems.zh-CN.md#reme)

### 原始记录、摘要与结构化字段

保留原文，或把信息整理成简短摘要与明确字段。

使用时要看：摘要会丢失细节，抽取也可能出错；来源应能被找回。

[Amazon Bedrock AgentCore Memory](../resources/systems.zh-CN.md#amazon-bedrock-agentcore-memory) · [MemoryOS](../resources/papers.zh-CN.md#memoryos) · [Mem0](../resources/systems.zh-CN.md#mem0)

### 检查点与命名空间存储

检查点保留执行进度；分组存储把不同用户或任务的记录组织开来。

使用时要看：检查点不是自动可检索的事实库；分组也不等于授权。

[LangGraph](../resources/systems.zh-CN.md#langgraph)

### 相似度与混合检索

按含义、关键词或多个信号寻找相关材料。

使用时要看：相似不等于最新、正确或被允许访问。

[Mem0](../resources/systems.zh-CN.md#mem0) · [Graphiti](../resources/systems.zh-CN.md#graphiti)

### 关系图与时序图

把实体、事实、来源和有效时间组织成可查询关系。

使用时要看：构图和更新需要成本；关系存在不证明因果。

[Graphiti](../resources/systems.zh-CN.md#graphiti) · [A-Mem](../resources/papers.zh-CN.md#a-mem)

<a id="operation"></a>

## 怎样形成和维护记忆？

把记忆看成会变化的资料：写进去只是开始，之后还要整理、查找、纠正和决定保留什么。

反思和压缩是操作；反思文本和摘要是操作后的产物。“不再在答案里使用”与“从存储中删除”也要分开。

<details>
<summary>用生活例子理解</summary>

先留下课堂录音，再写笔记，考前提炼要点，发现错误后修订。找不到笔记、忘记某条内容和把笔记销毁，并不是同一件事。

</details>

### 记录与提取

保存事件，或从原始交互中抽取事实、偏好和任务信息。

使用时要看：应区分实际原话、模型推断和后来确认的结论。

[Amazon Bedrock AgentCore Memory](../resources/systems.zh-CN.md#amazon-bedrock-agentcore-memory) · [Mem0](../resources/systems.zh-CN.md#mem0)

### 整理、巩固与反思

合并重复信息，形成总结，或从经历中归纳经验。

使用时要看：归纳会增加解释，也可能引入错误，不能丢掉原始依据。

[Generative Agents](../resources/papers.zh-CN.md#generative-agents) · [Reflexion](../resources/papers.zh-CN.md#reflexion) · [ReasoningBank](../resources/papers.zh-CN.md#reasoningbank)

### 检索与筛选

从已保存的信息中取回当前需要的部分。

使用时要看：检索命中还不等于被正确使用，后续读入与行动需另看。

[Graphiti](../resources/systems.zh-CN.md#graphiti) · [Mem0](../resources/systems.zh-CN.md#mem0)

### 更新与历史失效

新事实出现时修改记录，或让旧事实不再作为当前状态使用。

使用时要看：保留旧版本和标注事实有效期是两件事。

[Graphiti](../resources/systems.zh-CN.md#graphiti) · [A-Mem](../resources/papers.zh-CN.md#a-mem)

### 压缩与分层整理

把有限输入空间留给更有用的信息，其他内容放到外部，按需再读。

使用时要看：节省上下文可能牺牲细节；需要核对任务质量与成本。

[MemoryOS](../resources/papers.zh-CN.md#memoryos) · [Online memory under token budgets](../resources/papers.zh-CN.md#online-memory-under-token-budgets) · [Pi](../resources/systems.zh-CN.md#pi) · [Aider](../resources/systems.zh-CN.md#aider) · [Mastra Memory](../resources/systems.zh-CN.md#mastra)

### 选择性遗忘与删除

研究何时不再使用旧信息，以及何时清除保存的记录。

使用时要看：答案不引用旧事实，不能作为物理删除成功的证据。

[Memora](../resources/papers.zh-CN.md#memora) · [MemoryAgentBench](../resources/papers.zh-CN.md#memoryagentbench)

<a id="use"></a>

## 记忆怎样进入下一次行动？

保存的信息只有被正确选择、读入和使用，才可能帮助下一次回答或行动。这一页关注从存储到使用之间的步骤。

常驻或按需，描述读取方式；执行中或后台，描述处理时机。它们不是新的记忆内容类型。

<details>
<summary>用生活例子理解</summary>

常驻像每次开会都摆在桌上的目标卡；按需像讨论预算时再取出的账本。账本被拿出来后，还要检查决策有没有真正参考它。

</details>

### 常驻上下文

每次模型调用都放入指定信息。

使用时要看：便于持续提供约束和背景，但占用输入容量。

[Letta Code](../resources/systems.zh-CN.md#letta-code)

### 按需检索或读文件

需要时再请求相关材料。

使用时要看：是否读、读多少和选哪些内容，会影响任务效果。

[Google ADK](../resources/systems.zh-CN.md#google-adk) · [Deep Agents](../resources/systems.zh-CN.md#deep-agents) · [Mem0](../resources/systems.zh-CN.md#mem0) · [OpenClaw](../resources/systems.zh-CN.md#openclaw) · [Memorix](../resources/systems.zh-CN.md#memorix) · [DeepSeek Harness](../resources/systems.zh-CN.md#deepseek-harness)

### Agent 请求或运行时预载

由 Agent 决定查询，或由程序在调用前准备相关信息。

使用时要看：触发位置与存储后端是不同选择，可以组合。

[Google ADK](../resources/systems.zh-CN.md#google-adk) · [LangGraph](../resources/systems.zh-CN.md#langgraph)

### 执行中写入或后台整理

在当前步骤保存信息，或把部分整理放到交互之外。

使用时要看：后台处理可能有延迟；后续请求应考虑信息尚未完成处理的状态。

[LangGraph](../resources/systems.zh-CN.md#langgraph) · [Amazon Bedrock AgentCore Memory](../resources/systems.zh-CN.md#amazon-bedrock-agentcore-memory)

### 回答、规划与工具行动

检查记忆是否改变回答、计划、工具选择或参数。

使用时要看：会回忆事实，并不自动意味着任务行动更成功。

[Mem2ActBench](../resources/papers.zh-CN.md#mem2actbench) · [ReasoningBank](../resources/papers.zh-CN.md#reasoningbank) · [Online memory under token budgets](../resources/papers.zh-CN.md#online-memory-under-token-budgets)

<a id="governance"></a>

## 怎样让记忆可追溯、可控制？

记住的信息也可能过时、未经授权，甚至被恶意写入。治理关心谁能使用它、依据在哪里，以及出错后如何纠正。

这里的资料包含诊断协议和攻击研究，不表示列出的系统都已经完成安全认证。

<details>
<summary>用生活例子理解</summary>

小组资料需要记录出处、限制借阅；某条通知被撤回后，后来的成员也不能继续把旧通知当成有效指令。

</details>

### 权限与共享边界

检查谁能写入、读取、传播某段信息，以及共享是否符合角色约定。

使用时要看：同一个用户或团队标签本身不证明权限实现正确。

[COLLABMEM](../resources/papers.zh-CN.md#collabmem)

### 原始来源与版本

保留记录的出处和变化，支持核对与纠正。

使用时要看：文件修改时间不等于事实有效期，二者需要分别解释。

[Graphiti](../resources/systems.zh-CN.md#graphiti) · [Letta Code](../resources/systems.zh-CN.md#letta-code)

### 冲突、撤销与遗忘

检查新旧信息冲突时采用什么，撤回的内容如何停止影响后续行为。

使用时要看：要区分答案层、检索层与存储层的处理。

[MemoryAgentBench](../resources/papers.zh-CN.md#memoryagentbench) · [Memora](../resources/papers.zh-CN.md#memora) · [COLLABMEM](../resources/papers.zh-CN.md#collabmem)

### 记忆投毒与不可信输入

研究恶意记录被检索后如何影响回答或工具动作。

使用时要看：攻击研究只支持其威胁模型下的结论，不能据此给所有系统统一打分。

[AgentPoison](../resources/papers.zh-CN.md#agentpoison)
