# Awesome Harness Memory

**一门从原理到实例的 Agent Memory 教程。** 面向想理解 Agent、Harness 和独立记忆系统的读者：先建立观察方法，再读研究与工程，学会判断评测结果，最后通过实践和真实作品拓宽理解。

**[开始学习 →](https://dongshuyan.com/awesome-harness-memory/)** · [English](README.md) · [课程覆盖与证据边界](docs/coverage.md) · [贡献指南](CONTRIBUTING.md)

你不需要先选一个框架或背一棵分类树。完成主路径后，应能解释一份信息怎样被保存、更新、取回并影响后续调用，也能指出一个系统的文档没有回答什么。

## 第一课：用六个问题认识 Memory

[打开连续教程：解释、例子与六问论证](https://dongshuyan.com/awesome-harness-memory/#tutorial/lesson)

| 问题 | 要弄清楚什么 |
| --- | --- |
| **1. 内容角色** | 保存的是事实、经历、步骤、偏好还是规则？它解决什么问题？ |
| **2. 载体与表示** | 信息放在哪里，以原文、摘要、图、向量或其他形式表示？ |
| **3. 主体与范围** | 描述谁、服务谁，在哪些会话、任务、项目或Agent之间共享？ |
| **4. 生命周期** | 什么时候写入、更正、合并、过期、遗忘或删除？ |
| **5. 暴露方式** | 后续调用怎样得到这些信息：常驻、自动检索、工具读取，还是别的方式？ |
| **6. 控制与治理** | 谁决定操作，谁有权限，怎样追溯、撤回并处理不可信内容？ |

六问是一套有来源的学习清单。它综合研究框架、官方工程文档与评测中反复出现的区别；不是某一篇论文的统一分类，也没有证明为唯一最小、数学正交的集合。第一课最后列出事实、引用、推导与反例。六问帮助理解主要机制；实际能力、成本和安全仍需要相应测试。

例如，项目先约定周五交付，后来改成周一。“两句话都存下来了”还不足够：需要识别有效版本、限定项目范围、在合适的调用中取回，并保留更正来源。这条过程贯穿后面的课程。

## 接下来怎么学

| 顺序 | 课程 | 为什么接着学它 |
| --- | --- | --- |
| 02 | [相关概念辨析](https://dongshuyan.com/awesome-harness-memory/#tutorial/concepts) | 先分清Context、对话历史、RAG、checkpoint、参数/隐状态/KV与通用存储，避免同词异义 |
| 03 | [Research](https://dongshuyan.com/awesome-harness-memory/#tutorial/research) | 看研究者提出了什么问题，方法如何工作，实验能够支持什么 |
| 04 | [工程](https://dongshuyan.com/awesome-harness-memory/#tutorial/engineering) | 看真实系统怎样把读写、持久化、范围和控制落实到接口与配置 |
| 05 | [Benchmark](https://dongshuyan.com/awesome-harness-memory/#tutorial/benchmarks) | 看任务、协议与指标分别测到了什么，怎样与六问对应 |
| 06 | [文学与影视](https://dongshuyan.com/awesome-harness-memory/#tutorial/culture) | 用真实作品思考遗忘、外部记录、身份与共享；明确区分作品事实和工程类比 |

每个详解条目先交代身份、作者或维护者、可核对的作者机构、时间、原始入口和收录理由，再逐问解释**答案、为什么、具体例子与溯源**。Research、工程和Benchmark各有入口页与独立详情页，读完后可以用[比较工具](https://dongshuyan.com/awesome-harness-memory/#tutorial/compare)并排查看已有答案。

## 课程中的实例

截至2026-11-14，详解工作集如下；各条目的具体核对日期单独记录。列表按已知公开日期排序，不给方法或团队排名。

| 类别 | 详解数量 | 可以从这里开始 |
| --- | ---: | --- |
| Research主课 | 10 | [CoALA](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/coala)、[MemGPT](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/memgpt)、[Generative Agents](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/generative-agents) |
| 研究延伸阅读 | 4 | 结构综述、图记忆、自主Agent记忆与Storage–Reflection–Experience；单列于Research入口 |
| 工程系统 | 15 | [Claude Code](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/claude-code)、[LangGraph](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/langgraph)、[Mem0](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/mem0) |
| Benchmark | 10 | [LongMemEval](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/longmemeval)、[LoCoMo](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/locomo)、[COLLABMEM](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/collabmem) |
| 文学与影视 | 8 | Memento、Funes the Memorious、Severance、50 First Dates等真实作品 |
| 人类记忆背景 | 2 | [记忆系统；遗忘与巩固](https://dongshuyan.com/awesome-harness-memory/#tutorial/human-memory) |

这 **49 个条目都有六问详解**；其中35个是Research、工程与Benchmark技术主课。主课最多两篇综述，其他综述保留在延伸阅读。精选依据包括原始材料可核、研究方法与证据质量、作者或维护团队、发表状态和时效性；团队声望和关注度不单独构成效果证据。

## 从阅读走到验证

[横向专题与工具实践](https://dongshuyan.com/awesome-harness-memory/#tutorial/topics)进一步讲清：

- **安全与删除：** 不可信输入怎样变成记忆，访问控制与相关性有何区别，停止召回是否等于清除副本。
- **成本与容量：** 分别计算建库、维护、检索与生成，检查压缩丢失了哪些条件。
- **评测设计：** 用六问覆盖矩阵和分轴指标提出可执行检查，不把能力分数当成内部机制证明。
- **本地实践：** 用标准库示例观察持久化、更正、范围、过期与召回，无需API Key。

```sh
python3 examples/memory_lab.py
```

[实践步骤与预期输出](docs/practice.zh-CN.md)会说明每行结果与六问的关系。示例不调用模型；测试通过不代表任何上游产品的效果被复现。

## 本地预览与贡献

构建和示例只需Python标准库；完整测试另需Node.js执行JavaScript检查，无需安装npm依赖。

```sh
python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 -m unittest discover -s tests -v
python3 -m http.server 8000 --bind 127.0.0.1
```

浏览器打开`http://127.0.0.1:8000/`。教程权威数据是[`site/tutorial.json`](site/tutorial.json)，页面由构建器生成；维护方法见[仓库结构](docs/repository-structure.md)。

贡献时请附原始来源、版本、具体章节、例子与局限。资料没说明不等于不支持，作者报告不等于独立复现，文学类比不等于科学证据。参见[贡献规范](CONTRIBUTING.md)与[后续维护](ROADMAP.md)。
