# 系统与产品导航

基础资料已核表示文档支持这里的功能说明；未运行系统，也不是成熟度或安全认证。待核线索与历史资料单列。

[返回 README](../README.zh-CN.md) · [七问全景](../docs/landscape.zh-CN.md)

## Harness 与编码 / 个人 Agent

<a id="aider"></a>

### Aider

**基础资料已核 · Coding Harness**

提供聊天历史文件、可选的历史恢复和按 token 软阈值触发的摘要。

**值得看**：是区分“历史留档、恢复旧对话、缩减模型输入”的简洁工程入口。

**边界**：恢复聊天历史默认关闭；这些设置不能直接证明有自动画像或独立长期记忆策略。

**提供方式**：原生历史与摘要；恢复需配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Harness 按参数处理 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 对话历史与摘要 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 保存的聊天历史 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 历史文件、摘要 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、可选恢复、摘要 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 恢复或压缩后进入模型上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://aider.chat/docs/config/options.html) · [项目仓库](https://github.com/Aider-AI/aider)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="claude-code"></a>

### Claude Code

**基础资料已核 · Coding Harness**

通过 CLAUDE.md / AGENTS.md 等指令文件和 auto memory（自动记忆）承接跨会话知识。自动记忆记录从工作中积累的偏好、修正和经验。

**值得看**：人工规则与 Agent 自己写的笔记分开，便于理解谁负责记什么。

**边界**：官方说明这些内容是上下文，不是强制执行的安全配置；与 Claude-Mem 插件、托管 Agent memory 是三个对象。

**提供方式**：原生自动记忆＋指令文件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 用户写规则；Agent 写自动笔记；Harness 加载 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 规则、偏好、修正、任务经验 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 项目/用户文件与跨会话笔记，按配置区分 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | Markdown 指令与记忆文件 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 记录、读取、编辑 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 会话启动加载相关上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 可检查与调整记忆；指令文件不强制约束工具 |

</details>

**原始资料**：[功能原始来源](https://code.claude.com/docs/en/memory) · [项目仓库](https://github.com/anthropics/claude-code)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 v2.1.318。文档与发行版对应关系未完整审计。

<a id="cline"></a>

### Cline Memory Bank

**基础资料已核 · Harness 的文档记忆方法**

官方文档提供 Memory Bank：用项目中的结构化 Markdown 文件记录项目背景、进度与约定，再通过规则指导 Cline 维护和读取。

**值得看**：适合学习不依赖独立向量服务的工作区记忆。

**边界**：这是需要设置规则与初始化的文档方法，不是每次安装 Cline 都自动启用的后台记忆服务。

**提供方式**：配置与提示约定

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 用户配置规则；Agent 读写文档 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 项目背景、进度与约定 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 项目、跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | Markdown 文档集 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 初始化、读取、维护 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 按规则重新建立任务上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://docs.cline.bot/prompting/cline-memory-bank) · [项目仓库](https://github.com/cline/cline)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="deep-agents"></a>

### Deep Agents

**基础资料已核 · Agent Harness**

一个提供文件、规划和子代理能力的 Agent Harness。它的记忆接口允许 Agent 读取选定文件，并在获得许可时跨对话更新这些文件。持久化由后端决定：默认状态后端的范围是单个对话线程，存储后端则可以跨线程共享文件。适合研究 Harness 如何通过普通文件操作提供持久信息。

**值得看**：文件上下文和可插拔持久后端

**边界**：持久化范围由后端决定：默认状态后端限于单个线程，Store 后端可跨线程；不能把文件工具存在视为已启用长期共享。

**提供方式**：按文档及应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 读写文件；Harness 提供上下文和后端 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 工作状态、文件记忆与技能 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 线程/工作区；依后端 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 文件与状态/Store |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 读写、压缩、持久化 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 文件上下文与按需读取 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目仓库](https://github.com/langchain-ai/deepagents) · [记忆文档](https://docs.langchain.com/oss/python/deepagents/memory) · [后端文档](https://docs.langchain.com/oss/python/deepagents/backends)

核对：2026-11-06 UTC。当前官方后端文档及 README 已读；默认 StateBackend 与 StoreBackend 范围分开，未运行。

来源页面核对日期见条目；具体部署版本需另核。

<a id="deepseek-harness"></a>

### DeepSeek Harness

**基础资料已核 · Agent Harness**

官方示例通过 MCP（让 Agent 调用外部工具的协议）接入第三方记忆服务器，提供 Memorix、MCP Reference Memory 和 Engram 的配置示例。

**值得看**：展示 Harness 负责工具连接、记忆组件负责存储策略的分工。

**边界**：参考配置默认关闭；Harness 不替用户安装数据库、选择模型或维护外部 HTTP 服务，示例不代表厂商背书。

**提供方式**：第三方 MCP 接入，默认关闭

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Harness 接工具；第三方服务器管理记忆 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 取决于选用的记忆服务器 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 由服务器和项目配置决定 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 由外部服务器决定 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 发现和调用记忆工具 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | Agent 通过 MCP 请求 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 外部服务认证、许可与数据边界需分别配置 |

</details>

**原始资料**：[功能原始来源](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/mcp-memory.md) · [项目仓库](https://github.com/deepseek-ai/deepseek-harness)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="gemini-cli"></a>

### Gemini CLI

**基础资料已核 · Coding Harness**

用分层 GEMINI.md 文件提供持续的项目与用户指令；/memory 可以查看已加载内容并重新扫描文件。

**值得看**：清楚展示文件型“记忆”怎样成为当前模型的指令上下文。

**边界**：/memory 命令名本身不证明自动形成长期画像或情景记忆；本条已核范围是指令文件机制。

**提供方式**：原生上下文文件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 用户维护文件；Harness 加载 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 项目/用户规则与约定 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 分层的项目及用户上下文 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | GEMINI.md 文件 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 加载、查看、重新加载 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 拼接进指令上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://www.geminicli.com/docs/cli/gemini-md) · [项目仓库](https://github.com/google-gemini/gemini-cli)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 v0.67.0。文档与发行版对应关系未完整审计。

<a id="hermes"></a>

### Hermes Agent

**基础资料已核 · Personal Agent / Harness**

将 Agent 维护的笔记、历史会话搜索与可复用技能放在同一运行环境。README 描述周期性记忆提醒、全文搜索、摘要和从复杂任务创建技能。

**值得看**：适合观察经历怎样转成以后能调用的技能。可选 Honcho 集成用于主体建模。

**边界**：学习效果和自动技能质量是作者主张；Honcho 的能力不等于所有 Hermes 配置默认具备。

**提供方式**：原生笔记/会话搜索/技能；部分外部集成可选

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 维护知识，运行时提供提醒和工具 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 会话经历、笔记、技能 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 跨会话；用户建模依集成 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 笔记、技能文件、会话搜索索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、搜索、摘要、技能提炼 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 历史召回与后续技能使用 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/NousResearch/hermes-agent)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 v0.23.0。文档与发行版对应关系未完整审计。

<a id="letta-code"></a>

### Letta Code

**基础资料已核 · Stateful Coding Harness**

让 Agent 修改记忆块和技能；MemFS 以 Git 跟踪上下文，可选择同步到记忆仓库，另有周期性后台整理入口。

**值得看**：适合观察常驻记忆、技能学习、文件版本与长期 Agent 身份怎样组合。

**边界**：本地、云端与同步配置需区分；“自我改进”效果未由本轮验证。

**提供方式**：原生记忆与 MemFS；云端/同步可选

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 改写；Harness 提供记忆机制 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 记忆块、技能、上下文 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 持续 Agent 与跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 记忆块、文件、Git 版本 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 读取、改写、技能学习、后台整理 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 常驻上下文与按需读取 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | MemFS 跟踪版本；访问控制依部署 |

</details>

**原始资料**：[功能原始来源](https://github.com/letta-ai/letta-code)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="codex"></a>

### OpenAI Codex

**基础资料已核 · Coding Harness**

编码 Harness。官方文档将人工维护的 AGENTS.md 与可启用的本地 Memories 分开；后者从符合条件的历史聊天提炼有用信息，后台更新，并在以后工作中读取。

**值得看**：可分别控制当前聊天是否读取已有记忆、是否贡献新记忆。适合研究规则文件、会话连续性和跨会话学习的区别。

**边界**：此条聚焦本地 Codex 客户端；不能把 ChatGPT 网页记忆、云端任务、SDK 或所有客户端版本混为一谈。

**提供方式**：原生可选功能＋指令文件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Harness 后台生成；用户控制参与范围 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 历史工作的有用上下文、偏好与经验；人工规则另存 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 同一主机的本地记忆；逐聊天读写控制 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 本地生成的记忆文件 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 提炼、后台整合、读取、删除 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 后续聊天按记忆功能配置使用 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 开关、逐聊天控制、生成时秘密脱敏；非完整安全保证 |

</details>

**原始资料**：[功能原始来源](https://learn.chatgpt.com/docs/customization/memories) · [项目仓库](https://github.com/openai/codex)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 rust-v0.167.0。文档与发行版对应关系未完整审计。

<a id="openclaw"></a>

### OpenClaw

**基础资料已核 · Personal Agent / Harness**

个人 Agent 运行环境。官方记忆文档围绕工作区文件、个人与项目上下文、记忆搜索组件组织持续交互。

**值得看**：可把可读文件与搜索组件分开理解；文件被保存和当前会话能否使用它，是不同问题。

**边界**：搜索、权限与共享行为依配置；不能把个人上下文无条件推广到群组或其他用户。

**提供方式**：原生工作区文件＋可配置记忆搜索

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Harness 管理工作区；Agent 使用文件与搜索 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 用户信息、工作记录、持久笔记 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 工作区；个人和共享场景需区分 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | Markdown 文件与可配置索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 记录、搜索、读取 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 工作区上下文及按需检索 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 文档区分可信来源与个人上下文边界 |

</details>

**原始资料**：[功能原始来源](https://docs.openclaw.ai/concepts/memory) · [项目仓库](https://github.com/openclaw/openclaw)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 v2026.11.1。文档与发行版对应关系未完整审计。

<a id="opencode"></a>

### OpenCode

**基础资料已核 · Coding Harness**

保存会话历史，并在执行步骤前装配历史、指令和工具。当前 V2 会话规范说明压缩和指令基线的关系。

**值得看**：可研究“保存的完整历史”与“这一轮发送的上下文”如何分离。

**边界**：本条主要依据 V2 会话规范；规范不等于所有发行版本都已实现，跨会话语义记忆仍需单独核查。

**提供方式**：会话/上下文机制；V2 规范证据

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Harness 组织会话步骤 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 会话事件、指令与当前任务上下文 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 会话；分支和恢复按版本 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 持久化历史与压缩摘要 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、加载、压缩（V2规范） |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 每步重新组织模型输入 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/anomalyco/opencode/blob/dev/specs/v2/session.md) · [项目仓库](https://github.com/anomalyco/opencode)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="pi"></a>

### Pi

**基础资料已核 · Coding Harness**

以可扩展的编码运行环境管理任务。官方会话文档说明自动保存、恢复和分支，压缩文档说明旧消息摘要与分支摘要。

**值得看**：适合观察会话树、上下文压缩和扩展接口怎样配合。旧 badlogic/pi-mono 地址已转向 earendil-works/pi。

**边界**：会话恢复与压缩不等于自动积累跨会话用户画像；额外长期记忆需分别核对扩展。

**提供方式**：原生会话与压缩；其他记忆由扩展决定

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Harness 自动保存；用户选择恢复或分支 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 对话事件、任务上下文、摘要 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 会话及其分支；按工作目录恢复 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 持久化会话记录与摘要 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、恢复、分支、压缩 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 活动分支提供下一次模型输入 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sessions.md) · [项目仓库](https://github.com/earendil-works/pi)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 v1.5.0。文档与发行版对应关系未完整审计。

## Agent 框架

<a id="agno"></a>

### Agno Memory

**基础资料已核 · Agent Framework**

以 user_id 识别记忆所属用户，使偏好、职责和反复出现的目标在多次对话中可用；与知识检索分开介绍。

**值得看**：适合区分会话存储、用户记忆和外部知识库。

**边界**：记忆写入、调用方式和数据库需配置；身份标签本身不是权限保证。

**提供方式**：框架记忆组件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 框架与应用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 用户偏好、职责、持续目标 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 用户、跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 数据库记录 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 生成、保存、读取用户记忆 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 按用户装配后续上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://docs.agno.com/memory/overview) · [项目仓库](https://github.com/agno-agi/agno)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="camel"></a>

### CAMEL Memory

**基础资料已核 · Agent Framework 组件**

官方 Memory 模块提供保存、检索和管理 Agent 信息的接口，以 LongtermAgentMemory 等组合会话上下文。

**值得看**：适合阅读记忆模块与存储模块如何解耦。

**边界**：具体召回、后端、容量和长期保留依配置；未验证多 Agent 场景的权限隔离。

**提供方式**：框架模块

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 与框架记忆模块 |
| [记住什么](../docs/landscape.zh-CN.md#content) | Agent 记录与会话上下文 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 可组合记忆及存储后端 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 写入、检索、管理上下文 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | get_context 提供输入 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://docs.camel-ai.org/key_modules/memory) · [项目仓库](https://github.com/camel-ai/camel)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="crewai"></a>

### CrewAI

**基础资料已核 · Agent Framework**

文档中的统一 Memory 接口将记录组织到不同范围中，支持跨选定范围召回，并在保存信息时使用模型辅助分析和整合。适合探索 Agent 如何通过同一个接口处理自身信息和共享信息。它替代了原先分开的短期、长期、实体和外部记忆类型。分析会把内容发送给配置的模型；仅对信息划分范围，不应视为已验证的安全边界。

**值得看**：当前统一 Memory 的范围与召回机制

**边界**：分析会把内容发送给配置的模型；仅对信息划分范围，不应视为已验证的安全边界。

**提供方式**：按文档及应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 框架和记忆组件；应用配置范围 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 经历、事实与派生信息 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 按 Memory scope 配置 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 记忆记录与检索存储 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 记忆提取、保存与召回 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 在选定范围召回相关记忆 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目仓库](https://github.com/crewAIInc/crewAI) · [记忆指南（v1.15.34）](https://docs.crewai.com/v1.15.34/en/concepts/memory)

核对：2026-11-02。沿用此前原始来源核对；未运行系统或复现评测。

来源页面核对日期见条目；具体部署版本需另核。

<a id="google-adk"></a>

### Google ADK

**基础资料已核 · Agent Framework**

Agent 框架，分别提供会话状态管理与记忆服务。Agent 可通过 load_memory 查询，运行时也可通过 preload_memory 在模型请求前检索。持久化、检索和删除能力依后端与版本；删除会话不等于删除已导入的记忆。

**值得看**：Session Service 与 Memory Service 分开

**边界**：在内置后端中，固定版本的指南仅为内存实现注明了 delete_memory 支持；删除会话也不会清除此前已写入的记忆。

**提供方式**：按文档及应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 框架提供服务与工具；应用选择如何调用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 会话事件与导入的记忆 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | session；外部服务定义长期范围 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 会话记录及记忆服务 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 导入、load/preload、查询 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | load_memory 工具或 preload_memory 预载 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目仓库](https://github.com/google/adk-python) · [记忆服务指南](https://github.com/google/adk-python/blob/3655990f6ce1e55c40c5710351f6cf06cde0669b/docs/guides/memory/memory_service/index.md)

核对：2026-11-06 UTC。原始 README 与固定提交 3655990 的记忆服务指南已读；不推断所有发行版本一致。

来源页面核对日期见条目；具体部署版本需另核。

<a id="langgraph"></a>

### LangGraph

**基础资料已核 · 编排框架**

一个编排框架，其记忆文档区分了通过检查点持久化的对话线程状态，以及通过命名空间跨线程存储的信息。它适合用来理解：对话连续性与共享信息可以具有不同的生命周期和作用范围。持久化与检索取决于检查点保存器、存储组件和应用配置。

**值得看**：thread 检查点与跨 thread Store 分开

**边界**：持久化与检索取决于检查点保存器、存储组件和应用配置。

**提供方式**：按文档及应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 框架保存检查点；应用定义跨线程存储使用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 会话状态、跨线程信息 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | thread / namespace |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 检查点和 Store |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 持久化、恢复、查询 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 恢复线程状态，或查询 Store 后组织上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目仓库](https://github.com/langchain-ai/langgraph) · [记忆概念](https://docs.langchain.com/oss/python/concepts/memory)

核对：2026-11-02。沿用此前原始来源核对；未运行系统或复现评测。

来源页面核对日期见条目；具体部署版本需另核。

<a id="letta"></a>

### Letta

**基础资料已核 · Stateful Agent 平台**

以持续的 Agent 状态和可管理记忆支持长期交互。当前仓库指向 SDK、云端服务和 Letta Code 等不同入口。

**值得看**：区分 Agent 的持久身份、记忆与具体编码客户端；历史 MemGPT 另作为研究资料。

**边界**：旧服务器代码、SDK、云端服务和 Letta Code 的边界随版本变化，不能把一处能力复制到所有组件。

**提供方式**：平台与 SDK；部署方式影响能力

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 平台与运行环境 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 持久 Agent 上下文与记忆 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | Agent 身份和跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 由对应 SDK 或客户端读取 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/letta-ai/letta)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="llamaindex"></a>

### LlamaIndex Memory

**基础资料已核 · Agent Framework 组件**

在 Agent 输入中结合近期消息与长期 Memory Blocks（记忆块），还提供向量记忆和组合记忆等入口。

**值得看**：可按 token 预算调整信息从短期缓冲到长期块的去向。

**边界**：默认内存数据库不等于跨进程持久化；持久数据库、块处理器与检索策略需配置。

**提供方式**：可配置组件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 框架与记忆块处理器 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 近期对话、长期块中的事实或其他内容 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 会话；持久范围依数据库 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 消息缓冲、记忆块、向量存储 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、处理、检索、截断 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 组合成 Agent 上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/memory/) · [项目仓库](https://github.com/run-llama/llama_index)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="mastra"></a>

### Mastra Memory

**基础资料已核 · Agent Framework 组件**

提供历史消息、持久 working memory（结构化信息）和 Observational Memory（后台整理的观察日志）等不同机制。

**值得看**：观察日志替代不断变长的原始历史；适合研究上下文压缩与持续事实之间的分工。

**边界**：Mastra 的 working memory 不完全等于本报告“当前工作集”；保存范围、处理器和存储提供方需按配置理解。

**提供方式**：框架可配置组件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 框架与后台处理 Agent |
| [记住什么](../docs/landscape.zh-CN.md#content) | 消息、工具结果、结构化信息、观察日志 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 线程及配置的资源范围 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 历史、结构化 working memory、观察日志 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、观察整理、过滤/裁剪 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 为后续回答准备有限上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://mastra.ai/docs/memory/overview) · [项目仓库](https://github.com/mastra-ai/mastra)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="microsoft-agent-framework"></a>

### Microsoft Agent Framework

**基础资料已核 · Agent Framework / Harness**

官方 Harness 文档讨论历史持久化、压缩、文件记忆、Context Provider（提供上下文的组件）与审批。

**值得看**：适合把运行恢复、上下文准备和长期记忆分开设计。

**边界**：组件存在不代表所有应用默认启用；与旧 AutoGen 的版本与生命周期分别记录。

**提供方式**：框架组件，按应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Harness 与应用配置 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 会话历史、任务状态、文件记忆 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 会话、任务与配置的持久范围 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 历史、文件、检查点 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、恢复、压缩、上下文装配 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | Context Provider 提供模型输入 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 审批组件；记忆专属权限需另核 |

</details>

**原始资料**：[功能原始来源](https://learn.microsoft.com/en-us/agent-framework/concepts/harness) · [项目仓库](https://github.com/microsoft/agent-framework)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="openai-agents-sdk"></a>

### OpenAI Agents SDK

**基础资料已核 · Agent SDK**

提供两种不同机制：Sessions 维护对话历史；沙箱 Agent 记忆则使用模型将记录的对话提炼为文件，供后续运行查阅。适合区分对话连续性与可复用的任务经验。文件记忆需要保留相关工作区或快照；全新的空沙箱不包含这些记忆。文件布局和对话标识符决定了这些记忆产物如何共享。

**值得看**：Sessions、sandbox 工作区与记忆文件分别核对

**边界**：文件布局和对话标识符决定了这些记忆产物如何共享。

**提供方式**：按文档及应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | SDK 管理会话；模型提炼沙箱记忆文件 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 历史消息、任务状态、可复用笔记 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | session / workspace / memory files |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 会话后端、工作区、文件 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、恢复、压缩与记忆整理 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 恢复历史，或读取沙箱记忆文件 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目仓库](https://github.com/openai/openai-agents-python) · [会话文档](https://openai.github.io/openai-agents-python/sessions/) · [沙箱 Agent 记忆](https://openai.github.io/openai-agents-python/sandbox/memory/)

核对：2026-11-02。沿用此前原始来源核对；未运行系统或复现评测。

来源页面核对日期见条目；具体部署版本需另核。

<a id="pydantic-ai"></a>

### Pydantic AI Harness

**基础资料已核 · Agent Framework / Harness**

把记忆作为可组合能力。Memory 文档提供作用域内的文件搜索、编辑与删除工具；持久化和压缩另有独立能力。

**值得看**：适合比较文件记忆、逐步状态恢复与耐久执行的职责边界。

**边界**：持久化、压缩和记忆工具是可组合的不同能力；MEMORY.md 主文件不能通过删除工具删除，应改写内容，其他记忆文件可删除。

**提供方式**：可选 Harness 能力

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 调用工具；Harness 控制作用域 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 持久记忆文件 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 租户与 Agent 范围 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | MEMORY.md 与其他记忆文件 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 搜索、编辑、删除其他记忆文件 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 文件上下文与按需工具读取 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 作用域限制；主文件不能直接删除 |

</details>

**原始资料**：[功能原始来源](https://pydantic.dev/docs/ai/harness/memory/) · [项目仓库](https://github.com/pydantic/pydantic-ai)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

## 独立记忆层与工具

<a id="basic-memory"></a>

### Basic Memory

**基础资料已核 · 本地文件知识记忆**

让人和 AI 通过 MCP 读写同一组 Markdown 笔记，以观察与链接组织知识关系，并支持语义检索。

**值得看**：适合希望笔记可读、可编辑、可迁移的个人或团队。

**边界**：本地、云端团队协作与可选重排组件的能力分别核对；文件可读不自动保证同步或权限正确。

**提供方式**：MCP / 本地笔记；云端可选

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 人和 Agent 共同维护 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 笔记、观察与知识关系 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 本地项目；团队云端另配 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | Markdown 与链接知识图 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 读、写、搜索、同步（配置相关） |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 兼容 MCP 的客户端 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/basicmachines-co/basic-memory)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="claude-mem"></a>

### Claude-Mem

**基础资料已核 · 记忆插件 / 服务**

捕获编码 Agent 的工具使用观察，将其整理为摘要，并让后续会话检索或注入相关上下文。当前仓库列出多种宿主适配。

**值得看**：以观察记录到跨会话召回的流程补充现有 Harness，不需要把宿主原生记忆与插件能力混在一起。

**边界**：插件支持、存储和模型路径依宿主及部署配置变化；原生 auto memory 与插件同时启用时的行为需另核。

**提供方式**：第三方插件；本地/托管配置不同

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 插件捕获与处理，宿主使用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 工具观察、任务摘要 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 项目与跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 观察记录、语义摘要与检索索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 捕获、摘要、检索、注入 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 后续会话提供相关上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/thedotmack/claude-mem)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 v15.10.1。文档与发行版对应关系未完整审计。

<a id="cognee"></a>

### Cognee

**基础资料已核 · 记忆 / 知识图平台**

把文档、代码和对话组织成可检索的知识图，供 Agent 在后续工作中读取项目背景、决策和经验。

**值得看**：适合研究实体关系、领域结构与跨会话上下文的结合。

**边界**：知识图构建不自动证明完整记忆策略或效果；领域模型、存储和访问控制仍需配置。

**提供方式**：自托管平台与工具接口

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 记忆数据层与应用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 文档、代码、对话、决策与经验 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 项目及共享资料空间 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 知识图与搜索索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 摄入、结构化、检索 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | Agent 查找并复用 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/topoteretes/cognee)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="engram"></a>

### Engram（Gentleman-Programming）

**基础资料已核 · 本地编码记忆工具**

用本地 SQLite 保存编码 Agent 的持久记忆，并按项目组织；提供可选同步及宿主工具接入。

**值得看**：适合比较本地权威存储、项目隔离与跨机器同步的边界。

**边界**：这里指 Gentleman-Programming/engram，不能和同名神经记忆论文或其他 Engram 项目合并。

**提供方式**：本地工具 / MCP；同步可选

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 本地记忆工具 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 编码工作知识与观察 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 项目与会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | SQLite；可选可移植同步块 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、搜索、同步 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 宿主调用记忆工具 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/Gentleman-Programming/engram)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="evermemos"></a>

### EverOS（原 EverMemOS 仓库入口）

**基础资料已核 · 记忆运行时 / 库**

当前仓库使用 EverOS 名称，提供可跨编码助手与应用使用的本地优先记忆层，按用户、Agent、应用、项目和会话检索。

**值得看**：README 描述离线合并事件簇、提炼画像和技能的路径。

**边界**：历史 EverMemOS 论文/架构与当前仓库不可直接视为同一版本；本轮只据当前 README 介绍。

**提供方式**：库与本地运行时

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 记忆库与运行时 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 经历、画像、技能 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 用户、Agent、应用、项目、会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 检索、离线整合与提炼 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 跨助手和应用接入 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/EverMind-AI/EverOS)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="graphiti"></a>

### Graphiti

**基础资料已核 · 时序 Context Graph 框架**

从事件和业务数据构建带时间有效期的实体与关系图，保留事实到来源事件的联系。

**值得看**：适合研究事实变化、关系和来源的联合表达。Graphiti 是框架；Zep 是相关的企业上下文服务。

**边界**：数据库、模型、租户、访问控制和运行服务由应用配置；不因图中带来源就推断完整治理。

**提供方式**：图构建库；外围服务自建

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 图构建框架与应用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 来源事件、实体、关系、时间事实 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 由应用定义图和主体范围 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 时序图、事件来源、搜索索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 构建、更新、检索 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 应用查询图上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 事实有效时间和来源；租户权限由外围实现 |

</details>

**原始资料**：[仓库与文档](https://github.com/getzep/graphiti)

核对：2026-11-06 UTC。当前 README 的 context graph、Graphiti/Zep 边界已读。

来源页面核对日期见条目；具体部署版本需另核。

<a id="hindsight"></a>

### Hindsight

**基础资料已核 · 独立记忆系统**

通过 retain、recall、reflect（保留、召回、反思）组织事实与经历，进一步形成观察和 mental models（对环境的归纳理解）。

**值得看**：把原始经历与基于证据的归纳层分开，适合研究经验积累。

**边界**：论文旧分类与当前 README 术语不同。PR #6270 已合并保留设置修复，但本轮未核定所有发行版本覆盖；性能数字为作者报告。

**提供方式**：独立服务与宿主集成

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 记忆服务；Agent 调用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 世界事实、经历、观察、mental models |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | memory bank（记忆集合） |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 实体、关系、时间与检索索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保留、召回、反思、归纳 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 按需召回或反思输出 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/vectorize-io/hindsight) · [保留设置修复 PR（已合并，发行覆盖未核）](https://github.com/vectorize-io/hindsight/pull/6270)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="honcho"></a>

### Honcho

**基础资料已核 · 主体建模记忆服务**

保存会话消息与事件，在后台推理并更新 peer（主体）的表示，供应用查询上下文、关系认识或自然语言洞察。

**值得看**：不仅检索片段，也关注一个主体如何理解另一个主体。

**边界**：派生判断不等于事实；多主体关系、托管与自托管成本和隔离需按部署核对。

**提供方式**：服务、SDK 与宿主集成

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 后台记忆服务与应用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 事件、主体表示、推理结论 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | workspace、peer、session |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 消息与主体表示、混合索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、后台推理、更新、查询 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 返回上下文、搜索或自然语言结果 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/plastic-labs/honcho)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="mcp-reference-memory"></a>

### MCP Reference Memory Server

**基础资料已核 · 参考知识图记忆服务器**

MCP 官方参考服务器提供实体、关系和 observation（观察记录）的读写、搜索与删除工具，以本地知识图保存信息。

**值得看**：适合学习外部工具接口的最小记忆结构。

**边界**：参考实现不代表完整生产策略；普通搜索不等于语义检索，不能推断自动巩固、画像或遗忘。

**提供方式**：参考 MCP 服务器

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 工具服务器；Agent 决定调用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 实体、关系、观察 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 配置的存储文件 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 本地知识图 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 读写、搜索、删除 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | MCP 工具请求 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="mem0"></a>

### Mem0

**基础资料已核 · 独立记忆层 / 托管服务**

提供跨会话事实提取与检索。当前 README 描述单次 ADD-only 抽取、实体关联和多信号召回，适合研究事实积累与时间感知检索。

**值得看**：用户、Agent 与会话记忆有不同范围；2026 算法说明与2025论文分开阅读。

**边界**：README 的性能数字属于托管平台，不能当作开源 SDK 的同等结果；旧论文更新/删除流程不能直接代表当前抽取算法。

**提供方式**：SDK 与托管服务需区分

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 记忆层与应用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 事实、用户偏好、Agent 行为事实 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 用户、Agent、会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 事实记录及多信号索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | ADD-only 抽取、实体关联、召回（当前 README） |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 应用或 Agent 通过接口查询 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[仓库与文档](https://github.com/mem0ai/mem0)

核对：2026-11-06 UTC。当前官方 README 相关段落已读；历史论文与当前实现分开。

来源页面核对日期见条目；具体部署版本需另核。

<a id="memobase"></a>

### Memobase

**基础资料已核 · 用户画像记忆系统**

以用户画像和事件时间线组织持续交互信息，供个性化助手或应用读取。

**值得看**：明确聚焦“关于用户的记忆”，适合与任务/环境经验记忆比较。

**边界**：README 的时延表述随版本变化；本轮不把自报时延作为跨系统比较结论。

**提供方式**：用户记忆服务

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 服务与应用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 用户画像、偏好、事件 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 用户，跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 画像及事件时间线 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 提取、更新、查询 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 获取用户上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/memodb-io/memobase)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="memori"></a>

### Memori

**基础资料已核 · 记忆集成层 / 服务**

通过注册已有模型客户端并设置主体/流程归属，将对话持久化与召回接入现有应用。

**值得看**：重点是尽量沿用应用当前的模型调用路径，后台承接记忆。

**边界**：当前快速开始依赖 Memori API；不能沿用旧印象，直接宣称所有能力都是纯本地 SQL 方案。

**提供方式**：SDK 注册与服务配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 客户端集成层与服务 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 对话及行为相关记录 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | entity / process 标识 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 持久化、后台召回 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 接入已有模型客户端 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/MemoriLabs/Memori)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="memorix"></a>

### Memorix

**基础资料已核 · 共享项目记忆层**

为多个编码 Agent 提供随项目保留的共享、可搜索记忆，并通过 MCP 与不同宿主接入。

**值得看**：把记忆归属放在项目而非单次聊天，可用于工具切换和任务交接。

**边界**：列出的宿主支持仍需分别看适配器；本轮未验证共享并发、冲突和权限。

**提供方式**：独立项目记忆 / MCP / 插件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 项目记忆服务与宿主 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 项目知识与交接信息 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | Git 项目，跨 Agent / 会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、搜索、共享 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | MCP 与宿主适配 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/AVIDS2/memorix)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="memos"></a>

### MemOS

**基础资料已核 · 记忆管理系统**

提供统一的添加、检索、编辑与删除接口，用 Memory Cubes（可组合的记忆集合）组织用户、项目和 Agent 的资料。

**值得看**：将知识、多模态、工具轨迹和画像放到统一管理入口。

**边界**：与研究论文 MemoryOS 不同；多模态与宿主适配的可用范围按版本和部署核对。

**提供方式**：独立记忆系统及集成

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 独立记忆系统 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 知识、图像/文本、工具轨迹、画像 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 用户、项目、Agent 的记忆集合 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | Memory Cubes 与图式记录 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 添加、检索、编辑、删除 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 通过统一 API 与宿主集成 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/MemTensor/MemOS)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="memsearch"></a>

### MemSearch

**基础资料已核 · 跨宿主语义记忆工具**

让编码会话形成可搜索记忆，支持不同宿主插件，并有维护项目/用户笔记和提炼重复流程为技能的可选后台任务。

**值得看**：适合观察语义检索、文件笔记与程序性技能三者的协作。

**边界**：后台维护、重排服务和各插件不是同一默认配置；效果按具体协议解释。

**提供方式**：插件、CLI 与 API

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 插件与记忆工具 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 会话知识、项目/用户笔记、技能 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 项目及跨宿主会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 可搜索记忆与 Markdown 笔记 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 捕获、检索、维护、技能提炼 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 插件召回或 API/CLI 查询 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/zilliztech/memsearch)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="memu"></a>

### memU

**基础资料已核 · 共享文件记忆**

当前 README 将 memU 描述为用户共享的 LLM wiki，由后台任务从会话积累知识并提炼可复用技能。

**值得看**：把人可读的知识页与多宿主记忆连接起来。

**边界**：宿主适配的写入/召回模式不同；不能把旧版本分类或每个适配器的能力全部视为默认。

**提供方式**：文件记忆与宿主适配

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 与后台任务 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 用户知识与可复用技能 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 跨会话、Agent 与设备（依同步配置） |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | wiki 知识文件 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 积累、提炼、召回 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 宿主适配器读取 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/NevaMind-AI/memU)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="openviking"></a>

### OpenViking

**基础资料已核 · Context Database**

把知识、记忆和技能组织到 viking:// 虚拟文件系统中，可浏览目录、读取摘要并限定目录范围检索；提交会话时归档并提取记忆。

**值得看**：让检索对象具备可检查的文件层次，适合研究上下文分层访问。

**边界**：虚拟文件系统不等于普通本地目录；后端、模型与可选编译功能需分别配置。

**提供方式**：上下文数据库与 API

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 上下文数据库与 Agent |
| [记住什么](../docs/landscape.zh-CN.md#content) | 知识、用户偏好、经验、技能 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 目录、项目与会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 虚拟文件系统、目录摘要、索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 归档、提取、浏览、范围检索 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 按目录逐步读取或搜索 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/volcengine/OpenViking)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="reme"></a>

### ReMe

**基础资料已核 · 文件记忆管理**

把对话和资源组织成可读、可编辑、可搜索且互相链接的 Markdown 记忆，并提供上下文压缩等组件。

**值得看**：适合研究共享工作区中的文件记忆与可恢复压缩。

**边界**：历史 MemoryScope 分支与当前 ReMe 产品分开；不同自动记忆/压缩组件的模型和触发需按配置核对。

**提供方式**：记忆库与工作区集成

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 记忆库与 Agent |
| [记住什么](../docs/landscape.zh-CN.md#content) | 对话、资源与长期笔记 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 共享记忆工作区 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | Markdown、frontmatter、wikilinks |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 组织、搜索、维护、压缩 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 多运行环境共享工作区 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/agentscope-ai/ReMe)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="supermemory"></a>

### Supermemory

**基础资料已核 · 记忆与上下文服务**

提供事实抽取、用户画像、信息更新和混合搜索，结合外部知识资料与个人上下文；支持 API 和宿主插件等入口。

**值得看**：适合观察 RAG 资料与持续用户记忆怎样共同参与检索。

**边界**：不同托管、本地和插件路径需分别核对；README 的榜首和时延声明未由本轮验证。

**提供方式**：服务、API 与可选插件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 上下文服务与插件 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 事实、画像、近期活动与知识资料 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 用户与配置的资料集合 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 记忆记录与混合索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 抽取、更新、检索、过期处理 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | API/插件为 Agent 提供上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/supermemoryai/supermemory)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

## 托管记忆服务

<a id="amazon-bedrock-agentcore-memory"></a>

### Amazon Bedrock AgentCore Memory

**基础资料已核 · 托管记忆服务**

一个将原始交互事件与提取出的记忆记录分开的托管服务。配置的策略可以异步提取和整合信息，提供内置、自定义和自行管理的处理方式。适合比较由应用控制的记忆处理与提供方托管的提取。长期记忆提取需要配置策略，仅保存对话事件不会启用它。AWS 还提醒，事件元数据并非为存放敏感内容而设计。

**值得看**：原始事件和策略产生的长期记录分开

**边界**：AWS 还提醒，事件元数据并非为存放敏感内容而设计。

**提供方式**：按文档及应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 托管服务按策略提取；应用调用 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 事件、语义与偏好等派生记录 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | actor / session / namespace |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 原始事件与 memory records |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 事件写入、策略提取、检索 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 原始事件和长期记录通过接口读取 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[记忆类型](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html) · [记忆策略](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html)

核对：2026-11-02。沿用此前原始来源核对；未运行系统或复现评测。

来源页面核对日期见条目；具体部署版本需另核。

<a id="anthropic-managed-memory"></a>

### Anthropic Managed Agents Memory

**基础资料已核 · 托管记忆服务**

托管 Agent 的持久记忆存储可作为文件挂载；文档说明作用域、修订、归档与删除等管理能力。

**值得看**：可把工作区会话寿命与独立记忆存储寿命分开。

**边界**：与 Claude Code 本地自动记忆、Claude-Mem 插件不同；服务特性及开放范围按文档版本核对。

**提供方式**：托管服务

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 托管运行环境与记忆服务 |
| [记住什么](../docs/landscape.zh-CN.md#content) | Agent 维护的记忆文件 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 工作区作用域，跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 挂载文件存储 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 读取、写入、修订、归档、删除 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 运行时文件访问 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 读写作用域、修订；文档说明不可信输入可能写入恶意记忆 |

</details>

**原始资料**：[功能原始来源](https://platform.claude.com/docs/en/managed-agents/memory)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="google-agent-platform-memory-bank"></a>

### Google Agent Platform Memory Bank

**基础资料已核 · 托管记忆服务**

根据 Google 文档，这是一个从交互中提取并整合信息、在配置的范围内检索记忆的托管服务。适合比较提供方托管的记忆服务与应用自行管理的实现。ADK 通过 VertexAiMemoryBankService 接入；适配器特有的生命周期限制见 Google ADK 条目。本条目仅概括文档行为，未独立检查服务内部实现或部署行为。

**值得看**：后台抽取、整合与带期限记忆

**边界**：本条目仅概括文档行为，未独立检查服务内部实现或部署行为。

**提供方式**：按文档及应用配置

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 托管服务处理；调用方提供输入与范围 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 事实、偏好和关系 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 身份作用域 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 记忆记录与索引 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 抽取、整合、检索、修订、TTL |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 按作用域查询相关记忆 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[官方概览](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) · [记忆生成](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/generate-memories)

核对：2026-11-02。沿用此前原始来源核对；未运行系统或复现评测。

来源页面核对日期见条目；具体部署版本需另核。

<a id="redis-memory"></a>

### Redis Agent Memory

**基础资料已核 · 托管记忆基础设施**

当前仓库介绍 Redis Iris 下的托管 Agent Memory：保存事实、事件和偏好，并通过 SDK 或 REST API 跨会话检索。

**值得看**：适合研究把持续记忆交给数据库/上下文服务的集成路线。

**边界**：旧 agent-memory-server 名称不能代表当前仓库仍是一套相同的自托管服务器；需按当前服务文档核对。

**提供方式**：当前 README 为托管服务入口

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 托管记忆服务 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 事实、事件、偏好 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 跨会话 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 服务内持久存储 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存与检索 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | SDK / REST API |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/redis/agent-memory-server)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="zep"></a>

### Zep

**基础资料已核 · 企业 Context Layer**

以时序上下文图组织企业数据并为 Agent 提供相关上下文。Graphiti 是其图构建框架，Zep 还承担服务与治理层。

**值得看**：适合区分图算法库与面向企业的托管上下文服务。

**边界**：2025 年论文描述与当前服务不能直接等同；Graphiti 与 Zep 不共享一份功能保证或性能结论。

**提供方式**：服务；Graphiti 为相关组件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 企业上下文服务 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 事件、实体、关系及时间事实 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 企业上下文与 Agent 查询 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 时序 context graph |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 数据摄入、图构建与检索 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 为 Agent 服务上下文 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 产品声明治理功能；具体权限配置未审计 |

</details>

**原始资料**：[功能原始来源](https://github.com/getzep/graphiti#graphiti-and-zep)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

## 个人助手产品

<a id="chatgpt-memory"></a>

### ChatGPT Memory

**基础资料已核 · 个人助手产品**

从可用的历史聊天、已保存记忆及其他获准来源选取相关信息，帮助后续回答记住用户背景与偏好。记忆摘要、显式记忆条目和原始聊天需分别理解。

**值得看**：展示面向普通用户的长期记忆控制：查看、纠正与移除，以及回答中可用的来源入口。与 Codex 本地记忆是不同产品。

**边界**：设置和可用来源随方案、地区、平台及工作区变化；记忆摘要不保证包含全部内容。关闭记忆、不再提及、删除记忆和删除原始聊天不是同一操作。

**提供方式**：产品内置；可用性依账户、地区与工作区

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 产品服务整理；用户通过可用设置管理 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 偏好、用户背景及相关历史信息 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 跨聊天的个人上下文；依账户和工作区设置 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 已保存记忆、记忆摘要及原始来源；底层存储未核 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 保存、引用、修正与移除 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 选择相关个人上下文辅助回答 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 可用的开关与来源查看；关闭记忆不等于删除原始聊天 |

</details>

**原始资料**：[功能原始来源](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

## 待核线索

<a id="ai-memory"></a>

### ai-memory

**待核线索 · 待核对象**

官方仓库身份与 README 已读，跨宿主交接机制与信任边界尚未充分核对。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：官方仓库身份与 README 已读，跨宿主交接机制与信任边界尚未充分核对。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目入口](https://github.com/akitaonrails/ai-memory)

核对：2026-11-06 UTC。身份/机制未完成核对；不纳入已核系统计数。

来源页面核对日期见条目；具体部署版本需另核。

<a id="api-harness"></a>

### API Harness

**待核线索 · 待核对象**

名称既可指通用做法，也可能是某个具体项目；不能自动改成 Pi 或 Agents SDK。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：名称既可指通用做法，也可能是某个具体项目；不能自动改成 Pi 或 Agents SDK。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：名称未定位，不填造链接

核对：2026-11-06 UTC。身份/机制未完成核对；不纳入已核系统计数。

来源页面核对日期见条目；具体部署版本需另核。

<a id="cloudmem"></a>

### CloudMEM

**待核线索 · 待核对象**

用户原称尚不能唯一定位到项目；不擅自替换成 Claude-Mem。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：用户原称尚不能唯一定位到项目；不擅自替换成 Claude-Mem。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：名称未定位，不填造链接

核对：2026-11-06 UTC。身份/机制未完成核对；不纳入已核系统计数。

来源页面核对日期见条目；具体部署版本需另核。

<a id="continue"></a>

### Continue

**待核线索 · 待核对象**

编码工具身份已确认；本轮 README 不足以支持独立记忆管理机制，留待核对。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：编码工具身份已确认；本轮 README 不足以支持独立记忆管理机制，留待核对。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目入口](https://github.com/continuedev/continue)

核对：2026-11-06 UTC。身份/机制未完成核对；不纳入已核系统计数。

来源页面核对日期见条目；具体部署版本需另核。

<a id="cortex-ai"></a>

### Cortex AI

**待核线索 · 待核对象**

存在多个同名对象，尚不能确定此前所指。候选分别为 IDE、四层记忆库等，不能混合能力。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：存在多个同名对象，尚不能确定此前所指。候选分别为 IDE、四层记忆库等，不能混合能力。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[候选原始入口（未确认等同用户所指）](https://github.com/Cortex-AI-IDE/Cortex-Desktop) · [候选原始入口（未确认等同用户所指）](https://github.com/jdomian/cortex-ai)

核对：2026-11-06 UTC。身份/机制未完成核对；不纳入已核系统计数。

来源页面核对日期见条目；具体部署版本需另核。

<a id="cursor"></a>

### Cursor Rules / Memories

**待核线索 · Coding Agent**

当前官方 Rules 文档是持久项目指令的入口；旧 Memories 页面已跳转到文档首页。

**值得看**：保留规则型上下文与历史自动记忆资料的区别。

**边界**：当前自动 Memories 的可用性与机制本轮未确认；不能用旧搜索摘要作为现行功能证明。

**提供方式**：规则机制；自动记忆待核

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://cursor.com/docs/rules)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="langmem"></a>

### LangMem

**待核线索 · 记忆管理工具库**

提供对话信息抽取、对话中记录/搜索工具，以及后台抽取、巩固和更新能力。核心接口可配不同存储。

**值得看**：让执行中写入和后台整理成为可分别选择的路径。

**边界**：PR #212 仍在处理同步 MemoryStoreManager.invoke 的写/删异常传播问题；本轮未复现，不能泛化到所有接口。

**提供方式**：工具库，需存储与调度集成

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | Agent 工具与后台管理器 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 对话提取信息、行为提示 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 由存储命名空间决定 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 抽取、巩固、更新、记录与搜索 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 执行中或后台管理 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/langchain-ai/langmem) · [同步写入异常 PR（核对时仍 Open）](https://github.com/langchain-ai/langmem/pull/212)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="openhands"></a>

### OpenHands Software Agent SDK

**待核线索 · 待核对象**

SDK 的工作区、conversation 和代码能力已确认；本轮 condenser 路由失效，持久记忆与压缩边界仍需补查。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：SDK 的工作区、conversation 和代码能力已确认；本轮 condenser 路由失效，持久记忆与压缩边界仍需补查。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目入口](https://github.com/OpenHands/software-agent-sdk)

核对：2026-11-06 UTC。身份/机制未完成核对；不纳入已核系统计数。

来源页面核对日期见条目；具体部署版本需另核。

<a id="qwen-code"></a>

### Qwen Code

**待核线索 · Coding Harness**

官方 README 列出 Auto-Memory、Auto-Skills、会话管理和多 Agent 能力。

**值得看**：作为编码 Harness 中自动记忆与技能协作的补充调查入口。

**边界**：本轮只确认功能入口，尚未核清 Auto-Memory 的写入策略、存储范围与删除语义。

**提供方式**：官方列明原生功能；实现细节待核

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/QwenLM/qwen-code)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="serena"></a>

### Serena Memory

**待核线索 · 编码工具中的记忆组件**

Serena 是编码工具集，其 README 单独提供 Memory Management，用于长期工作流中跨会话、用户和项目保存知识。

**值得看**：是“工具套件含记忆组件”的例子，不需要把整套编码功能都当成记忆系统。

**边界**：本轮确认了组件定位；细粒度写入策略、存储后端和安全边界还未展开。

**提供方式**：工具集中的可关闭记忆组件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/oraios/serena)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对来源页面；精确发行版本、许可和依赖安全性未完整审计。

<a id="strands"></a>

### Strands Agents / Harness SDK

**待核线索 · Agent Framework / Harness**

当前仓库把 Harness 与 Python/TypeScript SDK 放在同一代码库，提供 memory、sessions 和 context management 的独立入口。

**值得看**：适合研究完整 Harness 默认组合与自行组装 Agent loop 的差异。

**边界**：本轮核对到组件入口；各记忆提供方、默认策略与跨会话存储细节尚待补查。

**提供方式**：Harness 组合及 SDK 组件

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[功能原始来源](https://github.com/strands-agents/harness-sdk)

核对：2026-11-06 UTC。已读官方文档或项目 README 的相关段落；未验证运行效果。

核对时仓库默认分支；发行标签 未核。文档与发行版对应关系未完整审计。

<a id="tencent-memory"></a>

### TencentDB-Agent-Memory

**待核线索 · 待核对象**

官方仓库身份已核；Team Memory Beta 的接口、保留策略和部署边界待进一步核对。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：官方仓库身份已核；Team Memory Beta 的接口、保留策略和部署边界待进一步核对。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目入口](https://github.com/TencentCloud/TencentDB-Agent-Memory)

核对：2026-11-06 UTC。身份/机制未完成核对；不纳入已核系统计数。

来源页面核对日期见条目；具体部署版本需另核。

## 历史资料

<a id="autogen"></a>

### AutoGen

**历史资料 · 历史框架 / Harness**

README 已有退休/归档转向 Microsoft Agent Framework 的说明；API 的 archived 标记核对时仍为 false。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：维护状态与功能存在性是两件事；本轮不评估继续部署风险。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目仓库](https://github.com/microsoft/autogen)

核对：2026-11-06 UTC。官方 README 与仓库元数据。

来源页面核对日期见条目；具体部署版本需另核。

<a id="roo-code"></a>

### Roo Code

**历史资料 · 历史框架 / Harness**

仓库 API 核对时 archived=true；作为历史资料，不作当前维护方案推荐。

**值得看**：从原始来源继续阅读，并结合对应研究问题比较。

**边界**：维护状态与功能存在性是两件事；本轮不评估继续部署风险。

**提供方式**：需按来源确认

<details>
<summary>七个视角下的已核描述</summary>

| 视角 | 描述 |
| --- | --- |
| [谁在管理记忆](../docs/landscape.zh-CN.md#owner) | 未核；不能解释为不支持 |
| [记住什么](../docs/landscape.zh-CN.md#content) | 未核；不能解释为不支持 |
| [为谁保存，保留多久](../docs/landscape.zh-CN.md#scope) | 未核；不能解释为不支持 |
| [如何承载与表示](../docs/landscape.zh-CN.md#form) | 未核；不能解释为不支持 |
| [怎样形成和维护](../docs/landscape.zh-CN.md#operation) | 未核；不能解释为不支持 |
| [怎样进入下一次行动](../docs/landscape.zh-CN.md#use) | 未核；不能解释为不支持 |
| [怎样追溯与控制](../docs/landscape.zh-CN.md#governance) | 未核；不能解释为不支持 |

</details>

**原始资料**：[项目仓库](https://github.com/RooCodeInc/Roo-Code)

核对：2026-11-06 UTC。官方 README 与仓库元数据。

来源页面核对日期见条目；具体部署版本需另核。
