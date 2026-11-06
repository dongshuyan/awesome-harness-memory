/* Chinese translation of the public atlas. Resource names retain their original spelling. */
(function (root) {
  'use strict';
  const translation = {
    ui: {
      systems: '系统', papers: '论文', benchmarks: '评测', fiction: '文学与影视',
      documented: '文档记载的实例', synthesis: '编者关联',
      conceptTag: '概念 / 阅读视角',
      outside: '保留当前选择 · 不在此视角的重点范围内',
      distinction: '注意区分', connections: '相关概念',
      why: '{kind} · 为什么有关联', reference: '查看引用来源 ↗',
      representatives: '代表资源', representativeIntro: '作为阅读起点，并非完整的能力清单。',
      literary: '文学关联 · {count}', literaryIntro: '这些类比用于启发问题，由编者整理，不属于技术证据。',
      perspective: '视角 {number} / 03', announcement: '{view}视角。已选择：{concept}',
      back: '← 返回资源库', compare: '如何比较报告中的结果', analogy: '编者类比',
      entry: '阅读{kind}条目 ↗', sources: '查看原始来源',
      analogyNote: '文学关联属于编者的解读，不是科学或工程研究结论。',
      resourceNote: '此阅读条目有来源依据。收录不代表已经安装所列系统、独立复现评测或完成安全审计。',
      library: '完整阅读资源库', libraryTitle: '{count} 项资源，多种阅读视角',
      libraryIntro: '地图呈现代表性的关联，其他条目仍可在这里查阅。未映射到地图，并不意味着该资源缺少依据。',
      technical: '技术实例 · {count}', stories: '文学类比 · {count}', more: '更多资源 · {count}',
      curated: '{count} 项精选资源', coverage: '{concepts} 个概念 · {technical} 项技术实例 · {stories} 项文学类比',
      checked: '来源核对日期 · {date}'
    },
    views: {
      continuity: { label: '连续性', question: '交互之间，哪些信息会被延续下来？', description: '区分当前请求中的信息、保留下来的信息、与用户关联的信息，以及可复用的经验。' },
      construction: { label: '记忆构建', question: '信息如何成为可用的记忆？', description: '理解原始记录、提炼出的经验、检索，以及 Agent 实际收到的上下文之间的区别。' },
      change: { label: '变化与控制', question: '事实、会话或访问条件变化时，会发生什么？', description: '考察信息变化、共享范围，以及更新、失效和删除之间的边界。' }
    },
    concepts: {
      context: { title: '当前上下文', subtitle: '模型此刻看到什么', definition: '在某一次请求中提供给模型的信息。筛选后的对话、检索出的信息和记忆文件都可以成为其中的一部分。', distinction: '信息已存入存储，并不意味着它会出现在下一次模型请求中。' },
      state: { title: '可恢复状态', subtitle: '承接已有工作', definition: '为继续工作而保留的对话状态或任务状态，例如检查点和会话历史。具体保留什么，取决于持久化配置。', distinction: '继续一个对话线程、开始一次新会话和恢复一个工作区，是不同的生命周期问题。' },
      profile: { title: '用户信息', subtitle: '偏好与事实', definition: '与用户关联的信息，例如偏好和事实，可以保留下来用于后续交互。', distinction: '与用户关联描述的是信息的归属范围；这种关联本身并未规定信息保留多久，也未规定谁能访问。' },
      scope: { title: '范围与来源', subtitle: '属于谁？来自哪里？', definition: '信息如何与用户、对话线程或角色关联，以及如何表示信息的来源。这些选择会影响信息共享和解读。', distinction: '给范围命名，不等于已经证明访问控制得到执行。来源信息有助于解读，但不能保证可信。' },
      records: { title: '记录与衍生', subtitle: '从交互到记录产物', definition: '原始交互及其衍生记录，包括摘要、提取出的事实或记忆文件。系统可能保留原始交互、衍生记录，或同时保留两者。', distinction: '保存交互和提取有用记忆是两种操作。有些服务需要显式配置提取策略。' },
      experience: { title: '可复用经验', subtitle: '从先前尝试中总结经验', definition: '从尝试中总结出的经验或策略，供之后使用。根据方法不同，它可能用于同一任务的下一次尝试，也可能用于后续任务。', distinction: 'Reflexion 研究多次尝试之间的反馈；ReasoningBank 还研究跨任务复用。两者的实验设置不同。' },
      retrieval: { title: '检索与使用', subtitle: '把记忆带入请求', definition: '筛选已存储的信息，使其可用于推理或行动。模型请求工具、自动预加载和读取文件，是不同的实现路径。', distinction: '在回答中找回一个事实，与在工具调用中正确使用这个事实，是需要分别评估的两种结果。' },
      revision: { title: '修订与遗忘', subtitle: '旧信息发生变化时', definition: '更新、纠正、失效或删除之后，已保留的信息会发生什么。不同系统和评测只覆盖这一问题的不同部分。', distinction: '回答中避免使用过时事实，并不能证明信息已从存储中删除。这里将 Graphiti 作为时序信息的参考，并未将其视为已验证的删除实例。' }
    },
    edges: {
      'visible-retained': { label: '当前可见 ≠ 已保留', explanation: '我们将请求中提供的信息，与为继续工作而保存的状态区分开来。这一区分参考了 LangGraph 检查点和本指南中的开放问题，属于编者为组织内容而建立的关联。' },
      'context-retrieval': { label: 'ADK：预加载或主动请求', explanation: 'Google ADK 文档介绍了通过 load_memory 由模型请求检索，以及通过 preload_memory 在请求前自动预加载。这条连线描述的是这些 ADK 接口，并非通用的执行流程。' },
      'records-experience': { label: '提炼经验', explanation: '记录下来的交互可以转化为供后续使用的信息。我们把 OpenAI 生成记忆文件的方式，与 ReasoningBank 提取策略的方式联系起来，是为了比较相关设计问题，并非认定两者存在实现上的传承关系。' },
      'records-user': { label: '提取用户信息', explanation: 'MemoryBank 组织对话、摘要和用户信息；AgentCore 则区分事件与提取出的记录。这是编者在相关方法之间建立的关联，并不表示它们的信息表示方式等价。' },
      'user-revision': { label: '偏好可能变化', explanation: 'Memora 评估偏好、活动和目标变化时的回答。我们将用户信息与修订联系起来，是为了指出值得考察的行为；其回答指标并不能证明物理删除。' },
      'state-revision': { label: 'ADK：会话 ≠ 记忆', explanation: '引用的 ADK 指南说明，删除会话后，之前已写入的记忆仍然保留。该指南仅为内置的内存实现注明了 delete_memory 支持。这是 ADK 适配器的一个实例，不能据此断言所有云服务都有相同限制。' },
      'scope-retrieval': { label: 'CrewAI：按范围召回', explanation: 'CrewAI 文档介绍了跨选定范围进行召回。这条连线描述的是文档中的召回接口。仅对信息划分范围，并不足以证明安全边界得到执行。' }
    },
    evaluationNote: '比较结果之前，应检查数据集版本、任务子集、模型、可用历史、检索预算和评判方式是否可比。还应检查统计了哪些成本，包括记忆写入和整合。这些问题用于解读原始实验；本仓库不提供合并排行榜。',
    resources: {
      langgraph: { summary: '一个编排框架，其记忆文档区分了通过检查点持久化的对话线程状态，以及通过命名空间跨线程存储的信息。它适合用来理解：对话连续性与共享信息可以具有不同的生命周期和作用范围。持久化与检索取决于检查点保存器、存储组件和应用配置。' },
      'deep-agents': { summary: '一个提供文件、规划和子代理能力的 Agent Harness。它的记忆接口允许 Agent 读取选定文件，并在获得许可时跨对话更新这些文件。持久化由后端决定：默认状态后端的范围是单个对话线程，存储后端则可以跨线程共享文件。适合研究 Harness 如何通过普通文件操作提供持久信息。' },
      mem0: { summary: '一个记忆层，提供添加和搜索与用户、Agent 及会话关联的信息的 API。它的特点是明确的记忆接口，可以接入现有应用。仓库介绍了开源和托管两类产品；在假定某项文档功能同时适用于两者之前，应先核对所选版本。' },
      graphiti: { summary: '一个根据输入信息构建时序上下文图的框架。它将实体和事实与来源事件及时间信息关联，适用于事实会变化、且需要关注历史的场景。使用时还需要配套的存储和模型基础设施。将过时事实标为失效与物理删除信息，是选择设计方案时需要分别考察的操作。' },
      'google-agent-platform-memory-bank': { summary: '根据 Google 文档，这是一个从交互中提取并整合信息、在配置的范围内检索记忆的托管服务。适合比较提供方托管的记忆服务与应用自行管理的实现。ADK 通过 VertexAiMemoryBankService 接入；适配器特有的生命周期限制见 Google ADK 条目。本条目仅概括文档行为，未独立检查服务内部实现或部署行为。' },
      'google-adk': { summary: '将会话状态，与对显式写入的交互进行检索区分开来。Agent 可以通过 load_memory 请求记忆，运行时也可以通过 preload_memory 在请求之前检索记忆。适合比较由模型控制的检索与自动准备上下文的方式。持久化和检索取决于后端。在内置后端中，固定版本的指南仅为内存实现注明了 delete_memory 支持；删除会话也不会清除此前已写入的记忆。' },
      'openai-agents-sdk': { summary: '提供两种不同机制：Sessions 维护对话历史；沙箱 Agent 记忆则使用模型将记录的对话提炼为文件，供后续运行查阅。适合区分对话连续性与可复用的任务经验。文件记忆需要保留相关工作区或快照；全新的空沙箱不包含这些记忆。文件布局和对话标识符决定了这些记忆产物如何共享。' },
      crewai: { summary: '文档中的统一 Memory 接口将记录组织到不同范围中，支持跨选定范围召回，并在保存信息时使用模型辅助分析和整合。适合探索 Agent 如何通过同一个接口处理自身信息和共享信息。它替代了原先分开的短期、长期、实体和外部记忆类型。分析会把内容发送给配置的模型；仅对信息划分范围，不应视为已验证的安全边界。' },
      'letta--letta-code': { summary: '使用 Agent 自有的 Git 仓库保存持久记忆，将直接放入提示词的信息与按需读取的参考文件分开。Letta Code 通过有状态的 Agent Harness 提供这些能力，包括后台修订记忆。适合研究跨对话可编辑、可追踪版本的上下文。仅在本地运行的 Agent 需要自行备份，跨机器共享依赖同步。当前 SDK 与 MemFS 文档对哪些文件路径会内联到提示词中有不同说明，采用文件布局前应核对适用接口。' },
      'amazon-bedrock-agentcore-memory': { summary: '一个将原始交互事件与提取出的记忆记录分开的托管服务。配置的策略可以异步提取和整合信息，提供内置、自定义和自行管理的处理方式。适合比较由应用控制的记忆处理与提供方托管的提取。长期记忆提取需要配置策略，仅保存对话事件不会启用它。AWS 还提醒，事件元数据并非为存放敏感内容而设计。' },
      'online-memory-under-token-budgets': { summary: '《在线技能与记忆模块始终值得消耗这些 Token 吗？一项预算约束下的 Web Agent 研究》。将在线工作流、技能和推理记忆模块，与获得更多执行步骤并使用上下文裁剪的基础执行 Agent 比较。适合考察总 Token 消耗的核算，以及不同运行之间的变化。预算匹配是近似的；测试的 Web 任务大多可以独立完成，因此这些结果不能判定记忆在依赖先前经历的任务中的价值。' },
      memora: { summary: '在包含新增、更新和失效信息的模拟历史中，测试记忆、推理和推荐。考虑遗忘的记忆准确率（Forgetting-Aware Memory Accuracy）将有效信息覆盖率与使用过时信息的惩罚结合，并依据明确标准评判。适用于助手需要跟进用户当前状态的场景。它测试的是回答行为，并非从存储中物理删除信息。研究使用受约束的角色设定和大模型评判，未比较运行时间或延迟。' },
      mem2actbench: { summary: '评估 Agent 是否使用先前交互来选择工具，并为工具参数提供依据。适用于需要让记住的偏好或任务状态影响行动的产品。其历史和任务由合成流程构建；结果针对该评测协议，并非对真实用户部署的观察。' },
      'mem-gallery': { summary: '测试跨会话的视觉与文本记忆，包括检索、时间和视觉推理、冲突，以及证据不足时拒绝回答。报告回答指标、模型评判的正确性和检索诊断。适用于重要信息存在于图像中的场景。对话经过构建和审查；纯文本方法接收图像描述。其范围不覆盖音频、具身交互或通用规划与工具使用。' },
      reasoningbank: { summary: '《ReasoningBank：用推理记忆扩展 Agent 自我演进》。从 Agent 自行判定成功或失败的经历中提炼可复用策略，再将其检索出来用于后续任务。适合研究解决问题的经验记忆。作者和 Google Research 将其列为 ICLR 2026 论文。解读所报告的收益时，需要注意结果由 Agent 自行判定，以及使用了额外的测试时计算。' },
      membench: { summary: '评估 Agent 参与对话或观察消息时的事实记忆和反思记忆。评测协议衡量多项选择题作答、证据检索、加入噪声后的容量，以及记忆读写时间。适用于仅看准确率会掩盖存储或检索开销的场景。构建的用户资料和对话、抽样测试子集以及多项选择题形式，限制了结果对开放任务的说明力。' },
      memoryos: { summary: '《AI Agent 的记忆操作系统》。组织近期对话、按主题划分的对话片段，以及保留更久的画像（persona）信息，明确区分存储、更新、检索和生成操作。适合考察不同记忆存储之间的信息迁移和检索。评估使用 GVD 和 LoCoMo；容量根据经验设置，主题片段缺少动态合并。这与 MemOS 是不同的项目。' },
      'a-mem': { summary: '《A-Mem：面向大模型 Agent 的自主记忆》。将记忆组织成相互关联的笔记，并允许新信息修改已有笔记。它关注的特色问题是：记忆写入后，组织方式如何继续演变。适合比较对固定记录进行检索，与记忆结构本身持续更新这两种方式。' },
      longmemeval: { summary: '测试信息提取、跨会话推理、时间推理、知识更新和拒答。适合定位对话记忆在哪些方面失效，而不只依赖一个汇总结果。结果取决于提供的历史、检索设置和评测协议；在聊天历史问答上成功，本身并不能证明工具执行也会成功。' },
      agentpoison: { summary: '《AgentPoison：通过记忆或知识库投毒对大模型 Agent 进行红队测试》。研究被投毒的检索条目如何改变 Agent 后续行为的方向。适合设计记忆威胁模型，并区分检索环节遭破坏与行动层面的失败。其设置假定攻击者能够插入记录，并访问嵌入模型以优化触发器。作者也报告了攻击可迁移到其他嵌入模型，并将其与相似的训练数据分布联系起来。因此，封闭嵌入接口尚未被证明是一种防御手段；实验也未表明每个记忆系统都面临相同程度的风险。' },
      locomo: { summary: '通过问答、事件摘要和多模态对话生成，评估长对话中的记忆。适合比较系统如何保留和使用对话信息。发布的数据集包含十段长对话。只使用其中问答部分进行评测时，应注明这一子集；这不涵盖完整的原始 Benchmark，也不能说明应用整体的可靠性。' },
      memorybank: { summary: '《MemoryBank：用长期记忆增强大语言模型》。结合对话记录、事件摘要、用户信息和检索，并探索衰减与强化机制。可作为个性化记忆和选择性保留的早期参考。其陪伴型 Agent 研究包含模拟对话；遗忘类比不能证明其符合生物机制，也不能证明在其他应用中的可靠性。' },
      'generative-agents': { summary: '《Generative Agents：人类行为的交互式模拟》。保存经历、检索相关记忆，并综合形成反思来指导 Agent 行为。作为理解记忆、反思和规划之间关系的历史参考收录。其模拟社交环境的目标，与实际部署的助手或编程 Agent 不同。' },
      reflexion: { summary: '《Reflexion：通过语言强化学习构建语言 Agent》。将任务反馈转化为反思文本，指导后续尝试，而不更新模型权重。可作为经验记忆和反馈驱动重试的基础参考。实验使用容量有限的反思缓冲区和针对具体任务的反馈；收益依赖反馈质量和重复尝试，并未证明它能在任意任务之间无限持续学习。' },
      collabmem: { summary: '一个诊断协议，考察角色之间的信息共享、不予共享、路由、来源归属、更新和留存。它固定交互轨迹与回答层，采用语义评分及更严格、注重证据的评分。适合区分记忆访问失败与规划失败。其 SDK 比较使用受控的共享策略，而非完整的原生团队部署；作者也指出了压缩指标的局限。产物状态（2026-11-02）：论文链接的仓库为空，因此目前应作为协议参考，而非可直接运行的起点。' },
      memoryagentbench: { summary: '通过逐步摄入信息研究记忆。当前 README 将能力称为检索、测试时学习、长程理解和冲突解决。适合考察记忆如何在不同任务中处理新信息。早期论文使用了选择性遗忘的表述；术语和数据集修订应与实际评测版本对应。各任务指标不同，不应把数值合并成仿佛衡量同一种准确率的结果。' },
      'the-housekeeper-and-the-professor': { summary: '教授对近期经历的记忆只能维持八十分钟，但仍保有数学知识。', analogy: '短暂的新近上下文可以与更持久的知识并存。这启发我们思考：近期上下文失效时，哪些信息必须被传递下去；新的交互又可以安全地假定哪些内容已经被知晓。这一类比并不将模型上下文限制与人类记忆丧失等同。' },
      severance: { summary: '故事将员工的工作记忆与私人生活记忆分隔开来。', analogy: '信息可以仍然保存在存储中，但访问权限随当前上下文而变化。这引出工作区、用户身份和权限的问题：谁能检索一段记忆，在什么条件下可以检索？这个设定关注访问和身份的分隔，不应简单理解为周期性删除。' },
      memento: { summary: 'Leonard 难以保留近期经历，依赖照片、书面笔记和纹身来保存线索。', analogy: '外部记录可以把信息带入后续决策，但决策仍然取决于记录的来源及其解读方式。这启发我们保留来源信息，并提供纠正已存结论的途径。这是对电影设定的解读，并非断言记录更多信息就能保证行动可靠。' },
      'funes-the-memorious': { summary: '所引用的片段描述了对细节异乎寻常的回忆能力，同时叙述者又怀疑 Funes 的思考能力。本条目依据这些节选；链接页面没有注明故事译本。', analogy: '保留细节和形成有用的抽象是不同目标。这个故事启发我们比较详尽档案与经过筛选的工作摘要，包括两者分别让哪些内容更容易被检索或用于推理。' },
      'the-memory-police': { summary: '岛上的物品不断消失，大多数居民却对这些变化浑然不觉。仍记得消失之物的人惧怕记忆警察。一位作家藏起了自己的编辑，两人试图用写作保留过去。', analogy: '记忆既有归属者，也受到权力控制。这一设定引出的问题是：谁能压制或保留共享记录，个体叙述又如何在集体知识变化时存续。这个类比关注对信息的控制，并不是技术删除的模型。' },
      '50-first-dates': { summary: '在电影设定中，Lucy 每晚都会失去当天的记忆，因此两人的关系必须反复重新建立。', analogy: '即使无法获得之前的交互，新会话也可能需要足够的背景说明，才能采取有意义的行动。这启发我们测试交接或重新介绍背景的质量，而不只统计保存了多少历史。这是虚构设定，并非对记忆丧失的临床描述。' }
    },
    sourceLabels: {
      'Repository': '项目仓库', 'Memory concepts': '记忆概念', 'Memory': '记忆文档', 'Backends': '后端文档',
      'Repository and documentation': '仓库与文档', 'Official overview': '官方概览', 'Memory generation': '记忆生成',
      'Memory service guide': '记忆服务指南', 'Sessions': '会话文档', 'Sandbox agent memory': '沙箱 Agent 记忆',
      'Memory guide, v1.15.34': '记忆指南（v1.15.34）', 'Letta Code repository': 'Letta Code 仓库',
      'Current SDK memory': '当前 SDK 记忆文档', 'MemFS': 'MemFS', 'Memory types': '记忆类型', 'Memory strategies': '记忆策略',
      'First preprint': '首版预印本', 'EMNLP 2026 paper': 'EMNLP 2026 论文', 'Findings of ACL 2026': 'Findings of ACL 2026 论文',
      'ACL 2026, July proceedings': 'ACL 2026 七月论文集', 'ACL 2026 paper': 'ACL 2026 论文',
      'Repository and dataset links': '仓库与数据集链接', 'Paper': '论文', 'Google Research account': 'Google Research 介绍',
      'Findings of ACL 2025': 'Findings of ACL 2025 论文', 'Repository and data instructions': '仓库与数据说明',
      'EMNLP 2025 paper': 'EMNLP 2025 论文', 'Author repository': '作者仓库', 'NeurIPS 2025 proceedings': 'NeurIPS 2025 论文集',
      'First preprint and paper record': '首版预印本与论文记录', 'NeurIPS 2024 paper': 'NeurIPS 2024 论文',
      'ACL 2024 proceedings': 'ACL 2024 论文集', 'AAAI 2024 publication': 'AAAI 2024 发表记录',
      'Stanford publication record: UIST 2023': '斯坦福发表记录：UIST 2023', 'NeurIPS 2023 paper': 'NeurIPS 2023 论文',
      'Repository linked by the paper': '论文链接的仓库', 'Repository and evaluation instructions': '仓库与评测说明',
      'Publisher page and excerpt': '出版方页面与节选', "Apple's official synopsis": 'Apple 官方剧情简介',
      'Distributor synopsis in French': '发行方剧情简介（法语）',
      'English excerpts discussed by Rodrigo Quian Quiroga (MIT Press)': 'Rodrigo Quian Quiroga 讨论的英文节选（MIT Press）',
      'Publisher synopsis': '出版方内容简介', 'Sony Pictures synopsis': 'Sony Pictures 剧情简介'
    }
  };
  if (typeof module !== 'undefined' && module.exports) module.exports = translation;
  else root.AtlasChinese = translation;
})(globalThis);
