# 记忆分类与方法导航

从九个问题学习记忆系统。记忆分类先展示有来源的主流分类方式，再用典型记忆内容索引做交叉对照；九问是编者导航，不声称唯一、穷尽或完全正交。

[打开交互页面](https://dongshuyan.github.io/awesome-harness-memory/) · [GitHub 仓库](https://github.com/dongshuyan/awesome-harness-memory) · [资源目录](../README.zh-CN.md#从具体对象开始)

## 页面导航

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

先看目前有来源的主流分类方式，再查看每套分类自己的类别、出处与限制。分类外另有待验证草案、典型内容索引和跨分类映射。

Start with named mainstream taxonomies, inspect each taxonomy on its own terms, then use the typical-content index for crosswalks.

四套主流分类方式是有来源的并列入口；待验证草案、索引和交叉映射属于分类外导航，不应被读成第五套已确立 taxonomy。

### 有来源的分类入口

下面四套入口处于同一层级。每套都按“来源事实 / 编者解释 / 类别结构 / 来源场景”展开；顺序按来源清晰度和当前证据状态排列。

#### 1. CoALA：架构角色分类 / CoALA: Architecture-role taxonomy

从 Agent 架构中的角色区分记忆：当前活跃的工作记忆，以及可在后续取回的长期记忆。长期记忆再按经历、知识和做法细分。

- 来源与年份：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）
- 证据与状态：2023 arXiv / 2024 TMLR · 研究框架论文；较高

**来源事实**

- 分类依据：按记忆在 Agent 架构中的角色组织：工作记忆保持当前活跃状态，长期记忆保存可在后续取回的内容；长期记忆再分为情景、语义和程序性记忆。
- 类别之间的关系：工作记忆与长期记忆是并列架构角色；情景、语义和程序性记忆是长期记忆的子类。原文没有把每条记录要求为唯一类别。
- 结构证据：CoALA §4.1 的文字与架构图；原文通过 Generative Agents 和 Voyager 说明情景、语义、程序性记忆的实例。
- 实证支持：论文提供架构分析和系统案例；原文未提供证明这套 taxonomy 唯一或优于其他 taxonomy 的独立消融实验。
- 原文声称的适用范围：适合解释 Agent 内部的记忆角色与长期记忆内容类型。
- 原文声称的限制：它不是承载、权限或产品术语分类；Working Memory、Context 和 Workspace 在工程实现中可能重叠。

**编者解释**

- 适用场景：学习 Agent memory 的基本组成，或需要把当前推理状态与可持久化记忆区分开时。
- 侧重点：架构角色和长期记忆内部的认知内容。
- 优势：结构清楚、来源较早且影响力高，适合做第一入口。
- 代价：对存储介质、生命周期触发和治理边界描述不足。

**这套分类自己的类别**

- **工作记忆 / Working Memory**：当前推理与行动中保持活跃的信息；它回答“现在为了完成任务要暂时保留什么”。 教学例子：解一道题时，题目条件、刚算出的中间结果和下一步计划都在草稿纸上。 边界：Working Memory（工作记忆）与 Workspace Memory（工作区记忆）不是同一个术语；也不等于模型的上下文窗口。
  - 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）
- **长期记忆 / Long-term Memory**：能够在后续任务中再次取回的经历、知识与做法；在 CoALA 中它是一个上层架构角色。 教学例子：实验笔记、已学公式和操作方法保存在资料夹里，需要时再取出。 边界：“长期”不对应统一天数。LangChain 还使用跨线程范围区分长短期；具体系统应注明自己的定义。
  - 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）
  - **情景记忆 / Episodic Memory**：长期记忆中关于具体经历、事件和结果的部分。 教学例子：“昨天第二次测量读数异常”描述的是一次具体经历。 边界：事件可以带有时间和关系。它们是记录的属性，不必单独成为与情景记忆并列的大类。
    - 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）
  - **语义记忆 / Semantic Memory**：长期记忆中关于概念、实体属性、事实和知识的部分。 教学例子：“小林偏好中文说明”是关于用户的事实或偏好。 边界：语义记忆不等于“语义检索”。前者说明记什么，后者说明如何查找。
    - 来源：[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）
  - **程序性记忆 / Procedural Memory**：长期记忆中关于如何行动、执行步骤和使用技能的部分。 教学例子：“先校准仪器，再检查样本标签”是一条可复用流程。 边界：“程序性”不只指电脑程序。保存一段流程文字，也不等于系统已能可靠执行。
    - 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）

**有来源的场景与证据边界**

- **CoALA 例子：事件进入情景记忆，再由反思形成更高层语义记忆**（[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；位置：§4.1.2 Episodic Memory 与 §4.1.3 Semantic Memory）
  - 场景背景：Agent 持续观察环境并执行多步任务，需要保留具体经历，也需要把重复经历提炼成以后可直接使用的知识。
  - 记忆内容：先记录带时间和结果的事件（情景记忆），再把多次事件归纳为更稳定的事实或概念（语义记忆）。
  - 承载与表示：原文以 memory stream、检索和反思说明结构；具体数据库或文件格式原文未说明。
  - 写入触发与主体：Agent 将新经历写入情景记忆；反思过程根据积累的经历产生更高层的记忆。
  - 读取与注入：与当前任务相关的记忆被检索并放入工作记忆，供后续推理使用。
  - 更新、压缩或遗忘：通过反思进行抽取和提炼；原文未规定统一的遗忘或删除策略。
  - 原文效果或定性结论：原文把它作为 Agent 形成长期知识、支持持续行为的架构案例；这不是 taxonomy 效果的独立实验。
  - 与相邻类别的区别：它说明情景与语义是长期记忆的不同角色；一次事件本身不等于稳定事实。
  - 证据性质：原文释义；用于说明 CoALA 的内部关系，不扩展为未被原文说明的实现细节。

- **CoALA 例子：Voyager 把可复用技能保存为程序性记忆**（[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；位置：§4.1.4 Procedural Memory）
  - 场景背景：Agent 在开放环境中反复完成任务，单次成功如果只停留在对话历史中，之后仍要重新探索。
  - 记忆内容：把成功的技能或代码保存为程序性记忆，以便后续按需调用。
  - 承载与表示：原文将技能库作为程序性记忆的例子；具体存储后端原文未说明。
  - 写入触发与主体：成功执行后把技能或代码加入技能库；触发条件和写入主体的工程细节原文未完全展开。
  - 读取与注入：后续任务按需要检索并调用相关技能。
  - 更新、压缩或遗忘：技能可被扩展或修订；统一版本、淘汰和冲突处理原文未说明。
  - 原文效果或定性结论：原文用它说明程序性记忆如何让 Agent 复用做法，而不是只复述事实。
  - 与相邻类别的区别：程序性记忆保存“怎么做”；情景记忆保存“发生过什么”。
  - 证据性质：原文案例释义；不把案例中的具体运行结果当作本页独立性能结论。

#### 2. 功能分类：Factual / Experiential / Working / Functional taxonomy: factual, experiential, working

按记忆用来解决什么问题来分：维持当前任务、提供事实背景、从过去经历中学习。

- 来源与年份：[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)（2025/2026；arXiv 综述；v1/v2 元数据与分类章节已核）
- 证据与状态：2025/2026 · arXiv 综述；中高

**来源事实**

- 分类依据：按记忆在任务中的功能分为 working、factual 和 experiential：维持当前任务、提供事实背景、从过去经历中抽取可迁移经验。
- 类别之间的关系：三类是同一功能层级的入口；综述还讨论经验记忆中的 case、strategy、skill 等子形态，不能与 CoALA 的树直接拼接。
- 结构证据：综述分类章节及其对 Agent memory 功能的概括；具体类别边界依赖综述的术语与引用来源。
- 实证支持：这是综述型分类，原文未提供证明三类互斥或覆盖全部系统的 taxonomy 消融实验。
- 原文声称的适用范围：适合从“我需要它完成什么”倒推记忆能力和实现路线。
- 原文声称的限制：功能随任务而变，同一条记录可以同时服务事实、工作或经验用途。

**编者解释**

- 适用场景：做方案选型、设计写入/读取流程，或需要把“保存内容”与“使用目的”联系起来时。
- 侧重点：记忆在任务中的作用，而不是它的物理位置。
- 优势：更容易从工程需求出发比较方案。
- 代价：功能标签容易随任务变化，无法单独说明数据结构、主体范围或治理方式。

**这套分类自己的类别**

- **工作记忆 / Working Memory**：按功能看，负责在一次任务中主动管理当前上下文、目标和中间状态。 教学例子：模型在有限窗口里保留当前问题、关键历史和下一步计划。 边界：这一功能视角讨论压缩、状态整理和规划；与 CoALA 的架构模块定义侧重点不同。
  - 来源：[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)（2025/2026；arXiv 综述；v1/v2 元数据与分类章节已核）
- **事实记忆 / Factual Memory**：按功能看，提供用户、历史互动和环境的事实背景。 教学例子：“实验室周五关闭”“用户希望按月份统计”都可作为后续背景。 边界：这是该综述的功能分类；不能直接把它等同于另一套分类中的 Semantic Memory。
  - 来源：[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)（2025/2026；arXiv 综述；v1/v2 元数据与分类章节已核）
- **经验记忆 / Experiential Memory**：按功能看，保存从过去经历中抽取的案例、策略和技能，以便迁移到相似任务。 教学例子：上次忘记备份导致返工，于是形成“处理前先备份”的策略。 边界：它与情景、程序性记忆会有交叉。这里展示的是另一套按功能组织的方法，不拼成统一的父子树。
  - 来源：[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)（2025/2026；arXiv 综述；v1/v2 元数据与分类章节已核）

**有来源的场景与证据边界**

- **LangChain 文档例子：短期线程状态与长期用户/项目记忆分工**（[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；位置：Memory concepts：short-term memory 与 long-term memory）
  - 场景背景：一个 Agent 连续处理同一线程，同时还要在新的线程中保留用户或项目层面的信息。
  - 记忆内容：当前线程消息和任务状态承担 working 功能；跨线程取回的用户偏好或项目事实承担 factual 功能。
  - 承载与表示：短期状态由 checkpointer 保存，长期信息由 store 按 namespace 保存；具体后端可配置。
  - 写入触发与主体：运行时保存线程状态；应用或 Agent 通过文档中的存储接口写入长期记忆。
  - 读取与注入：当前调用直接使用线程状态；需要背景时按 namespace 检索长期记忆并注入提示。
  - 更新、压缩或遗忘：文档把摘要、更新和命名空间管理作为实现责任；没有一套所有应用通用的遗忘规则。
  - 原文效果或定性结论：官方文档用这个拆分说明短期连续性和长期事实是不同功能，不等于任何产品都自动拥有两者。
  - 与相邻类别的区别：同一份事实可以支持多个线程；线程状态则围绕当前任务组织。
  - 证据性质：来源事实：官方文档区分 short-term/thread state 与 long-term store。编者映射：把它们放到 working/factual 功能标签下；不是综述 taxonomy 的实验验证。

#### 3. 三维分类：承载形式 × 认知机制 × 记忆主体 / Three-dimensional taxonomy: substrate, cognitive mechanism, subject

把“记忆放在哪里”“发挥什么认知作用”“主要围绕谁”拆成三个可以组合的研究轴。论文摘要明确列出内部/外部承载、五种认知机制和 Agent/User 两类主体。

- 来源与年份：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
- 证据与状态：2026 · arXiv；accepted at TMLR with Survey Certification；出版信息待补；中高（摘要分类清晰；具体出版信息待补）

**来源事实**

- 分类依据：将 memory 拆成可组合的轴：记忆承载形式、认知机制和记忆主体；同一系统可以在每个轴上同时取值。
- 类别之间的关系：三个轴彼此并列，不构成一棵父子树；感觉/工作/情景/语义/程序性属于认知机制轴，内部/外部属于承载轴，Agent/User 属于主体轴。
- 结构证据：2026 综述的摘要级分类说明列出三个轴及其类别；本页把实现级示例标为编者说明，分类章节仍需继续核查。
- 实证支持：综述样本与摘要整理提供覆盖线索；当前没有足够证据把三轴说成已完成独立验证的标准。
- 原文声称的适用范围：适合比较跨实现、跨主体和跨存储形式的系统，避免把不同问题强行塞进同一棵树。
- 原文声称的限制：分类较新，出版与全文细节仍需持续核查；轴之间的组合不代表系统一定有完整数据流。

**编者解释**

- 适用场景：比较一个 memory 系统到底存在哪里、承担什么认知作用、围绕谁服务时。
- 侧重点：多轴组合，而不是单一类别归属。
- 优势：能表达交叉组合，适合制作切片、矩阵和投影图。
- 代价：理解成本较高，且摘要级证据不足以支撑所有实现级判断。

**这套分类自己的类别**

- **记忆承载形式 / Memory Substrate**：记忆主要由模型内部还是外部组件承载；这是“记忆放在哪里”的研究轴。
  - **内部承载 / Internal Memory**：记忆主要由模型参数或模型内部状态承载，逐条查看、撤销和审计通常更困难。 教学例子：模型通过参数或内部状态保留模式。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
  - **外部承载 / External Memory**：记忆保存在模型之外的上下文、文件、数据库、向量库或图存储中。 教学例子：把用户偏好写入可检索的外部记录，下次按需读回。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
- **记忆认知机制 / Cognitive Mechanism**：记忆在认知功能上扮演什么角色；综述明确列出感觉、工作、情景、语义和程序性机制。
  - **感觉记忆 / Sensory Memory**：处理刚刚到达、极短暂的感知输入。 教学例子：Agent 先保留刚看到的界面变化，再决定是否记录。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
  - **工作记忆 / Working Memory**：维持当前推理所需的活跃信息。 教学例子：当前任务的目标、约束和中间结果留在活动工作集里。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
  - **情景记忆 / Episodic Memory**：保留具体经历、事件和结果。 教学例子：回看某次工具调用及其结果。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
  - **语义记忆 / Semantic Memory**：保留事实、概念和实体知识。 教学例子：取回用户偏好或项目中的稳定事实。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
  - **程序性记忆 / Procedural Memory**：保留如何行动的步骤、技能与程序。 教学例子：调用一套已经验证过的部署步骤。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
- **记忆主体 / Memory Subject**：记忆主要围绕谁或哪个主体；综述区分 Agent-centric 与 User-centric。
  - **Agent 相关 / Agent-centric**：围绕 Agent 自身的经验、运行状态、策略或能力组织。 教学例子：记录 Agent 哪种检索策略在项目中更有效。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）
  - **用户相关 / User-centric**：围绕用户信息、偏好、目标或长期关系组织。 教学例子：记录用户偏好的语言、格式和长期目标。 边界：原文未单独说明
    - 来源：[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；[A Survey of Agent Memory in the Second Half · OpenReview PDF（待核身份）](https://openreview.net/pdf/98c3fad1f896d4e66146ed72688c024989748b71.pdf)（2026；OpenReview PDF 当前返回 403；论文身份与正文未独立核验，不作为本页独立证据。）

**有来源的场景与证据边界**

- **三轴标注示例（编者构造，依据 2026 综述的轴定义）**（[A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents · arXiv:2602.06052](https://arxiv.org/abs/2602.06052)（2026；arXiv 元数据与摘要已核；摘要明确列出承载形式、感觉/工作/情景/语义/程序性认知机制、Agent/User 主体与 218 篇样本范围；页面注明 accepted at TMLR with Survey Certification，具体出版信息待补）；位置：摘要中列出的 substrate / cognitive mechanism / subject 三轴）
  - 场景背景：为了说明三轴如何组合，编者构造一个需要回答时间关系问题的 Agent 场景；这不是该综述报告的单独系统实验。
  - 记忆内容：把“谁在什么时候负责哪个项目”标注为外部承载、语义机制和用户/Agent 主体；具体主体取值取决于应用边界。
  - 承载与表示：以时间知识图或其他外部结构保存只是教学实现；综述摘要没有规定唯一图数据库。
  - 写入触发与主体：编者示例：从对话或事件中抽取实体、关系和时间；原文未说明该具体触发或写入主体。
  - 读取与注入：编者示例：按实体、关系和时间条件检索，再把结果放入当前工作上下文；原文未报告这条工作流。
  - 更新、压缩或遗忘：编者示例：随新事实更新有效时间；冲突消解和遗忘策略原文未说明。
  - 原文效果或定性结论：来源支持三个轴可以并列标注；其余效果是帮助读者理解组合方式的编者推演，不是论文报告的 benchmark 结果。
  - 与相邻类别的区别：它展示“同一条记忆可以在多个轴上取值”；不把承载形式误当作记忆内容类别。
  - 证据性质：来源事实：摘要级轴定义。编者构造：完整场景、存储/读写流程和效果说明均需继续核查，不作为论文原文结论。

#### 4. 工程术语族：Context / Workspace / Long-term / Engineering term family: context, workspace, long-term

这是产品和 Harness 文档中常见的导航叫法：上下文续接、项目/任务工作区、跨交互持久化。三者可以重叠，不是同一篇论文提出的互斥三分法。

- 来源与年份：[Microsoft Multi-Agent Reference Architecture · Memory.md（2026-08）](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/docs/memory/Memory.md)（2026；官方参考架构文档；STM/LTM/Working Memory 与非知识库边界已核）；[AWS Agent memory systems · 官方学习模块](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/agent-memory-systems?sc_channel=em)（2026；AWS 官方工程材料；duration/scope、working/session/long-term/shared 章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Anthropic · Context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)（2025；Anthropic 官方研究文章；上下文工程说明已核）；[AgentScope Java · Harness memory overview](https://github.com/agentscope-ai/agentscope-java/blob/main/docs/v1/en/docs/harness/overview.md)（2026；官方项目文档；workspace context、session persistence 与两层持久记忆入口已核）
- 证据与状态：工程术语集合 · 非统一学术 taxonomy；中（术语常见，边界不统一）

**来源事实**

- 分类依据：按工程文档中常见的连续性入口组织：当前上下文、项目/任务工作区、跨交互长期保存。
- 类别之间的关系：三者是常见术语入口，不是同一篇论文提出的互斥分类；一个实现可以同时包含或重新命名它们。
- 结构证据：LangChain、Cline 和其他官方 Harness/Agent 文档分别使用短期、工作区、长期或类似术语；本页保留术语差异。
- 实证支持：官方产品文档和实现案例支持术语确实存在；原文未提供统一术语的领域共识调查或 taxonomy 实验。
- 原文声称的适用范围：适合从熟悉的产品需求进入：继续当前上下文、恢复项目工作、长期记住用户或组织信息。
- 原文声称的限制：Context、Workspace、Long-term 的边界随系统变化；不能把某个产品文档的命名推广成普遍标准。

**编者解释**

- 适用场景：使用或设计 Harness、Personal Agent、CLI Agent，需要先用产品语言定位连续性需求时。
- 侧重点：工程入口和生命周期范围，而不是学术认知类型。
- 优势：容易被产品文档和工程师直接识别，能快速定位实现资料。
- 代价：命名不统一，必须回到具体系统文档核对实际含义。

**这套分类自己的类别**

- **上下文记忆 / Context Memory**：工程入口：当历史超出模型窗口或上下文被压缩/重置时，保住继续工作所需的信息。 教学例子：把“已完成第一章，下一步核对图表”的交接便条重新放入模型。 边界：这里是一种用途入口，不是新的内容类型。下方相关方法也不表示每个系统都同时采用。
  - 来源：[Anthropic · Context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)（2025；Anthropic 官方研究文章；上下文工程说明已核）；[Microsoft Multi-Agent Reference Architecture · Memory.md（2026-08）](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/docs/memory/Memory.md)（2026；官方参考架构文档；STM/LTM/Working Memory 与非知识库边界已核）；[AWS Agent memory systems · 官方学习模块](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/agent-memory-systems?sc_channel=em)（2026；AWS 官方工程材料；duration/scope、working/session/long-term/shared 章节已核）；[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）
  - 术语证据：中；标准化状态：常见工程入口，但“Context Memory”不是一套统一的标准分类名称
  - 术语来源说明：“working memory / active context / session memory”在 Microsoft、AWS、Anthropic 和研究综述中有相近用法；这里把 Context Memory 作为窗口受限后的续接问题入口，而不是声称它是独立的认知类型。
- **工作区记忆 / Workspace Memory**：工程入口：围绕一个项目或任务保存目标、进度、文件和工作方法。 教学例子：项目文件夹中的进度表、实验日志和操作手册共同支持下次恢复。 边界：工作区说明资料围绕哪个项目组织；工作记忆说明当前正在使用的信息。工作区资料也可以长期保存。
  - 来源：[Microsoft Multi-Agent Reference Architecture · Memory.md（2026-08）](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/docs/memory/Memory.md)（2026；官方参考架构文档；STM/LTM/Working Memory 与非知识库边界已核）；[AWS Agent memory systems · 官方学习模块](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/agent-memory-systems?sc_channel=em)（2026；AWS 官方工程材料；duration/scope、working/session/long-term/shared 章节已核）；[AgentScope Java · Harness memory overview](https://github.com/agentscope-ai/agentscope-java/blob/main/docs/v1/en/docs/harness/overview.md)（2026；官方项目文档；workspace context、session persistence 与两层持久记忆入口已核）；[Cline · Memory Bank](https://docs.cline.bot/best-practices/memory-bank)（2026；官方产品文档；Memory Bank 说明已核）
  - 术语证据：中低；标准化状态：多种 Harness / 产品使用的工程叫法；尚未发现把它与 Context、Long-term 固定并列的权威统一分类
  - 术语来源说明：“workspace”在工程文档中常表示项目/任务的组织边界，也常被写成 online workspace、workspace context 或 workspace memory。它可以承载多种内容，因此不能被当作单一内容类型。
- **长期记忆 / Long-term Memory**：工程入口：保存可跨交互取回的信息；不同来源对内容和范围的边界并不完全一致。 教学例子：新会话仍能取回用户偏好、历史事实或可复用经验。 边界：“长期”不对应统一天数。LangChain 还使用跨线程范围区分长短期；具体系统应注明自己的定义。
  - 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[Microsoft Multi-Agent Reference Architecture · Memory.md（2026-08）](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/docs/memory/Memory.md)（2026；官方参考架构文档；STM/LTM/Working Memory 与非知识库边界已核）；[AWS Agent memory systems · 官方学习模块](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/agent-memory-systems?sc_channel=em)（2026；AWS 官方工程材料；duration/scope、working/session/long-term/shared 章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）
  - 术语证据：较高；标准化状态：广泛使用的术语族，但不同来源对内容、范围和持久时间的边界仍不完全相同
  - 术语来源说明：CoALA、Microsoft 参考架构、AWS 工程材料和 LangChain 文档都使用长期/跨会话的相近概念；它通常表示可跨 Session 取回的持久信息，不等于只保存用户偏好。

**有来源的场景与证据边界**

- **Cline Memory Bank：以工作区文件承接项目连续性**（[Cline · Memory Bank](https://docs.cline.bot/best-practices/memory-bank)（2026；官方产品文档；Memory Bank 说明已核）；位置：Memory Bank / best practices documentation）
  - 场景背景：编码任务跨多个会话推进，模型每次重新启动时需要知道项目目标、当前进度和重要约束。
  - 记忆内容：工作区级的项目上下文和进度记录，内容包括项目说明、当前状态、决策和下一步。
  - 承载与表示：官方文档描述为项目工作区中的 Markdown 文件；具体文件集合和模板以文档版本为准。
  - 写入触发与主体：Agent 按 Memory Bank 约定更新工作区文档；具体自动或手动触发依版本和配置而定。
  - 读取与注入：新会话开始时读取工作区记忆，把与当前任务有关的内容加入上下文。
  - 更新、压缩或遗忘：通过持续更新、整理和删除过时项目说明维护状态；文档未给出通用自动遗忘算法。
  - 原文效果或定性结论：文档把它作为跨会话恢复项目上下文的工程做法；不等于对所有代码任务都有量化收益。
  - 与相邻类别的区别：它偏工作区连续性；用户长期偏好通常需要不同的 namespace 或长期存储。
  - 证据性质：来源事实：官方文档说明 Memory Bank 用于项目连续性。编者补充：跨会话背景、具体写入主体和与长期偏好的对比需按版本核查。

- **LangChain：短期线程状态与长期 namespace 的工程边界**（[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；位置：Memory concepts：short-term/thread state 与 long-term memory）
  - 场景背景：应用既要让一次线程连续，也要让多个线程共享稳定的用户或项目信息。
  - 记忆内容：线程状态对应当前上下文连续性，namespace 中的记录对应跨线程长期信息。
  - 承载与表示：checkpointer 保存线程状态，store 保存长期 namespace；文档允许不同后端。
  - 写入触发与主体：运行时保存线程状态，应用显式写入长期记录；自动抽取方式不是所有应用的默认行为。
  - 读取与注入：线程状态直接进入当前调用；长期信息按 namespace 检索后选择性注入。
  - 更新、压缩或遗忘：应用需要处理摘要、更新、冲突和删除；官方概念页未规定统一策略。
  - 原文效果或定性结论：这个边界帮助工程师区分“本线程继续”与“跨线程记住”，但不是统一学术 taxonomy。
  - 与相邻类别的区别：与 Cline 的工作区文件做法相比，它以运行时 namespace 和 checkpointer 表达相似的连续性需求。
  - 证据性质：来源事实：官方概念文档说明 thread state、namespace 和长期 store。编者映射：把它们与 context/workspace/long-term 入口对照，不是原文宣称的等价关系。

### 待验证草案：编者综合的典型记忆内容标签

这七项是为了帮助读者从具体内容进入不同分类方式而整理的导航标签，不是某篇论文提出的完整 taxonomy。

- 状态：待验证
- 形成依据：七项来自 CoALA、Agent memory 综述、官方记忆文档、Harness/Agent 实例和本仓库前期调研中的重复模式；它们把当前工作集、事件、事实、流程、经验、关系/时间和规则放到一个工程阅读索引中。单项有来源不等于七项整体有来源。
- 限制：不是某篇论文提出的分类，不保证正交、完整或稳定；其中关系/时间与规则更像跨内容属性，当前只保留为待验证导航假设。

这些标签用于分类外导航，不是第五套已确立分类方式。

- **当前工作集与上下文 / Working set & context management**：为当前问题选择历史、摘要、目标或检索结果，再把需要的内容送入模型。；边界：保存在窗口外的历史，尚未读入时不属于本次模型输入；工作记忆也不能简单等同于一次调用的上下文窗口。；来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[MemoryOS · 首版预印本](https://arxiv.org/abs/2506.06326)
- **经历与事件 / Episodic memory / Event records**：记录某次对话、任务、观察、工具调用及结果。；边界：保留细节有助于追溯，但不能假设所有历史都能放进一次模型输入。；来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Generative Agents · 首版预印本](https://arxiv.org/abs/2304.03442)；[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)
- **事实与用户偏好 / Semantic memory / Facts & preferences**：提取可供后续交互使用的事实、属性与偏好。；边界：事实可能改变；用户画像本身也不是使用这些信息的授权。；来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)；[MemoryBank · 首版预印本](https://arxiv.org/abs/2305.10250)
- **步骤与流程 / Procedural memory / Procedures**：保存“这件事怎么做”的步骤、操作说明和可执行流程。；边界：流程是否适用取决于环境和条件；保存流程不保证执行正确。；来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Deep Agents · 项目仓库](https://github.com/langchain-ai/deepagents)；[Online memory under token budgets · 首版预印本](https://arxiv.org/abs/2606.15017)
- **可复用经验与策略 / Experiential memory / Strategies**：从尝试结果中归纳以后可以参考的做法和适用条件。；边界：反馈质量、额外尝试和迁移条件会影响收益。；来源：[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)（2025/2026；arXiv 综述；v1/v2 元数据与分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Reflexion · 首版预印本](https://arxiv.org/abs/2303.11366)；[ReasoningBank · 论文](https://arxiv.org/abs/2509.25140)
- **关系与时间事实 / Relational & temporal facts**：记录谁与什么有关，以及一个事实在什么时候成立。；边界：用图表示是一种实现选择；关系存在不证明因果。；来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)
- **规则与约束 / Instructions / Constraints**：保存用户约定、任务限制或组织规则，供后续工作参考。；边界：保存了规则，不代表已经强制执行；权限与审计另见治理专题。；来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)；[COLLABMEM · EMNLP 2026 论文](https://aclanthology.org/2026.emnlp-main.1194/)

### 典型记忆内容索引

五类主要内容加两项横向属性。前五项回答“通常记住什么”，后两项描述记录中的关系、时间和规则属性；它们是编者综合导航，不冒充单一论文提出的七分类。

本索引是分类外的导航层；它把不同分类方式中常见的内容词汇集中起来，便于进入交叉映射。

#### 主要内容类型 / Primary content types

这五项是内容/功能层面的主要入口；同一系统可以同时具备多项。

<a id="types-working-context"></a>
- **当前工作集与上下文 / Working set & context management**：为当前问题选择历史、摘要、目标或检索结果，再把需要的内容送入模型。 教学例子：桌上只放当前实验要用的几页；完整记录保存在文件夹里，需要时再拿出来。 边界：保存在窗口外的历史，尚未读入时不属于本次模型输入；工作记忆也不能简单等同于一次调用的上下文窗口。 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[LangGraph · 项目仓库](https://github.com/langchain-ai/langgraph)；[MemoryOS · 首版预印本](https://arxiv.org/abs/2506.06326)
<a id="types-events"></a>
- **经历与事件 / Episodic memory / Event records**：记录某次对话、任务、观察、工具调用及结果。 教学例子：“昨天用仪器 A 测了三次，第二次读数异常。”记录的是一次经历。 边界：保留细节有助于追溯，但不能假设所有历史都能放进一次模型输入。 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Generative Agents · 首版预印本](https://arxiv.org/abs/2304.03442)；[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)
<a id="types-facts"></a>
- **事实与用户偏好 / Semantic memory / Facts & preferences**：提取可供后续交互使用的事实、属性与偏好。 教学例子：“小林喜欢用中文看解释”是偏好；“昨天小林提了这个要求”是事件。 边界：事实可能改变；用户画像本身也不是使用这些信息的授权。 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Mem0 · 仓库与文档](https://github.com/mem0ai/mem0)；[MemoryBank · 首版预印本](https://arxiv.org/abs/2305.10250)
<a id="types-procedures"></a>
- **步骤与流程 / Procedural memory / Procedures**：保存“这件事怎么做”的步骤、操作说明和可执行流程。 教学例子：实验前先校准仪器再检查标签，是可复用流程；昨天执行过它是事件。 边界：流程是否适用取决于环境和条件；保存流程不保证执行正确。 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Deep Agents · 项目仓库](https://github.com/langchain-ai/deepagents)；[Online memory under token budgets · 首版预印本](https://arxiv.org/abs/2606.15017)
<a id="types-experience"></a>
- **可复用经验与策略 / Experiential memory / Strategies**：从尝试结果中归纳以后可以参考的做法和适用条件。 教学例子：一次实验失败后总结“先备份原始数据”，下次遇到同类任务时参考。 边界：反馈质量、额外尝试和迁移条件会影响收益。 来源：[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)（2025/2026；arXiv 综述；v1/v2 元数据与分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Reflexion · 首版预印本](https://arxiv.org/abs/2303.11366)；[ReasoningBank · 论文](https://arxiv.org/abs/2509.25140)

#### 横向属性 / Cross-cutting attributes

关系、时间、规则可附着在多种内容上，不与情景、语义、程序性处于同一认知层。

<a id="types-relations"></a>
- **关系与时间事实 / Relational & temporal facts**：记录谁与什么有关，以及一个事实在什么时候成立。 教学例子：“小林在三月负责项目 A，四月交给小周。”关系和时间说明了事实适用范围。 边界：用图表示是一种实现选择；关系存在不证明因果。 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Graphiti · 仓库与文档](https://github.com/getzep/graphiti)
<a id="types-rules"></a>
- **规则与约束 / Instructions / Constraints**：保存用户约定、任务限制或组织规则，供后续工作参考。 教学例子：“只读原始数据，清洗结果另存。”是约束；把它记下来并不自动限制文件权限。 边界：保存了规则，不代表已经强制执行；权限与审计另见治理专题。 来源：[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[LangChain · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)（2026；官方概念文档；短期/长期记忆边界已核）；[Letta Code · 功能原始来源](https://github.com/letta-ai/letta-code)；[COLLABMEM · EMNLP 2026 论文](https://aclanthology.org/2026.emnlp-main.1194/)

### 跨分类映射

交叉表的行是待验证草案中的典型内容，列是某一套正式分类自己的类别；它不表示不同分类方式之间的父子关系，其中 `◆` 只表示当前分类方式内部的上层类别与该内容的包含关系。符号：`●` 直接对应，`◆` 上层包含，`◐` 有关联，`◇` 可落入，`?` 待核，`—` 未标注直接对应。
- 映射性质：编者映射 · 待验证；符号表示当前证据边界，不是效果分数。

#### CoALA：架构角色分类

| 典型内容 | 工作记忆 | 长期记忆 | 情景记忆 | 语义记忆 | 程序性记忆 |
| --- | --- | --- | --- | --- | --- |
| 当前工作集与上下文 | ● | — | — | — | — |
| 经历与事件 | — | ◆ | ● | — | — |
| 事实与用户偏好 | — | ◆ | — | ● | — |
| 步骤与流程 | — | ◆ | — | — | ● |
| 可复用经验与策略 | — | ◇ | ◐ | — | ◐ |
| 关系与时间事实 | — | — | — | ◐ | — |
| 规则与约束 | — | — | — | — | ◐ |

#### 功能分类：Factual / Experiential / Working

| 典型内容 | 工作记忆 | 事实记忆 | 经验记忆 |
| --- | --- | --- | --- |
| 当前工作集与上下文 | ● | — | — |
| 经历与事件 | — | ● | — |
| 事实与用户偏好 | — | ● | — |
| 步骤与流程 | — | — | ◐ |
| 可复用经验与策略 | — | — | ● |
| 关系与时间事实 | — | ◐ | — |
| 规则与约束 | — | ◐ | — |

#### 三维分类：承载形式 × 认知机制 × 记忆主体

| 典型内容 | 内部承载 | 外部承载 | 感觉记忆 | 工作记忆 | 情景记忆 | 语义记忆 | 程序性记忆 | Agent 相关 | 用户相关 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 当前工作集与上下文 | ◇ | ◇ | — | ● | — | — | — | ◇ | — |
| 经历与事件 | ◇ | ◇ | — | — | ● | — | — | ◇ | — |
| 事实与用户偏好 | ◇ | ◇ | — | — | — | ● | — | — | ◐ |
| 步骤与流程 | ◇ | ◇ | — | — | — | — | ● | ◐ | — |
| 可复用经验与策略 | ◇ | ◇ | — | — | ◐ | — | ◐ | ◐ | — |
| 关系与时间事实 | ◇ | ◇ | — | — | — | ◐ | — | ◇ | ◇ |
| 规则与约束 | ◇ | ◇ | — | — | — | — | ◐ | ◐ | — |

#### 工程术语族：Context / Workspace / Long-term

| 典型内容 | 上下文记忆 | 工作区记忆 | 长期记忆 |
| --- | --- | --- | --- |
| 当前工作集与上下文 | ● | ◐ | ◇ |
| 经历与事件 | — | ◐ | ● |
| 事实与用户偏好 | ◐ | ◐ | ● |
| 步骤与流程 | — | ● | ◐ |
| 可复用经验与策略 | — | ◐ | ● |
| 关系与时间事实 | — | ◐ | ◐ |
| 规则与约束 | ◐ | ● | ◐ |

### 相关研究视角

这些工作补充结构、生命周期、成本和图记忆等问题，放在分类模块之外供继续研究。

- **四种 MAG 结构 / Four MAG structure families（2026）**：《Anatomy of Agentic Memory》按 Memory-Augmented Generation 的组织结构归纳 Lightweight Semantic、Entity-Centric and Personalized、Episodic and Reflective、Structured and Hierarchical 四类。 与分类模块的关系：这是“记忆怎样组织”的结构视角，可与 CoALA 的内容/功能类型交叉；它不是把语义记忆、情景记忆重新定义成唯一实现。 来源：[Anatomy of Agentic Memory · arXiv](https://arxiv.org/abs/2602.19320)（2026；arXiv 论文正文与摘要级核对；四种 MAG 结构和评测限制章节已核）

- **Storage → Reflection → Experience / Storage → Reflection → Experience（2026）**：ACL 2026 Findings 综述把机制演化描述为 Storage（保留轨迹）、Reflection（精炼轨迹）和 Experience（跨轨迹抽象），强调记忆从原始记录走向可迁移策略。 与分类模块的关系：这是生命周期/抽象程度的演化路线，不是与情景、语义、程序性同一级的内容树；它解释了记录如何产生派生经验。 来源：[From Storage to Experience · ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.2069/)（2026；ACL Findings 出版页面与论文摘要级核对；Storage/Reflection/Experience 三阶段已确认）

- **Forms–Functions–Dynamics / Forms–Functions–Dynamics（2025/2026）**：《Memory in the Age of AI Agents》用 Forms、Functions、Dynamics 三个统一视角整理 Agent Memory：形式包括 token-level、parametric、latent；功能包括 factual、experiential、working；动态关注形成、演化和检索。 与分类模块的关系：这篇综述支持“分类体系可以并列存在”：功能分类回答记住什么，形式回答怎么表示，动态回答怎样形成和使用。页面中的九个专题是编者对这些问题的导航展开。 来源：[Memory in the Age of AI Agents · §4](https://arxiv.org/html/2512.13564v2#S4)（2025/2026；arXiv 综述；v1/v2 元数据与分类章节已核）

- **系统型四轴与成本剖析 / System-oriented four-axis characterization（2026）**：《Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads》提出系统型四轴分类，并把开销拆到 construction、retrieval、generation 三个阶段，提醒比较记忆系统时要同时看质量和运行成本。 与分类模块的关系：这是系统/评测视角，适合放在比较和 Benchmark 入口，不应被误读为新的记忆内容分类。论文摘要没有列出四轴的完整名称，本页不猜测。 来源：[Agent Memory: Characterization and System Implications · arXiv](https://arxiv.org/abs/2606.06448)（2026；arXiv 摘要与元数据核对；系统型四轴与构建/检索/生成成本分析已确认，四轴细目待全文核查）

- **图记忆的多重视角 / Graph-memory perspectives（2026）**：《Graph-based Agent Memory》从图实现出发，同时讨论 short-term / long-term、knowledge / experience、non-structural / structural 等维度。 与分类模块的关系：这是面向图记忆的专项综述，不是全领域唯一分类；它提醒我们把内容、时间和结构分开记录。 来源：[Graph-based Agent Memory: Taxonomy, Techniques, and Applications · arXiv](https://arxiv.org/abs/2602.05665)（2026；arXiv 摘要级核对；短/长期、知识/经验、非结构/结构与图实现视角已确认）


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

[CoALA · §4.1](https://arxiv.org/html/2309.02427v3#S4.SS1)（2023 arXiv / 2024 TMLR；研究框架论文；arXiv v3（2024-03）为 TMLR camera-ready；架构分类章节已核）；[Memory in the Age of AI Agents · 表示形式 §3](https://arxiv.org/html/2512.13564v2#S3)

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
