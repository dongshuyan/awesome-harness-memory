# Awesome Harness Memory

**一门面向初学者的 Agent Memory 图文教程。** 从一条信息如何被保存、更新和再次使用开始，逐步认识研究方法、工程实现与评测，再借助文学影视和人类记忆研究拓宽思考。

**[开始学习 →](https://dongshuyan.com/awesome-harness-memory/)** · [English](README.md) · [课程覆盖](docs/coverage.md) · [贡献指南](CONTRIBUTING.md)

正文使用中文，原始资料保留原文。阅读不需要框架使用经验：必要术语会结合例子解释，公式、API、源码定位和复现细节放在可展开的部分。学完后，你应能沿着一条信息的流转解释系统的主要机制，并判断还有哪些问题需要查资料或做实验。

## 学习路径

| 顺序 | 课程 | 这一课要弄清楚什么 |
| --- | --- | --- |
| 01 | [六个核心问题](https://dongshuyan.com/awesome-harness-memory/#tutorial/lesson) | 学习认识 Memory 的六个方向；同一页依次讲意义、回答方法、例子，最后给出来源与论证 |
| 02 | [相关概念辨析](https://dongshuyan.com/awesome-harness-memory/#tutorial/concepts) | 分清 Context、对话历史、RAG、checkpoint、模型内部信息与通用存储，理解它们和 Memory 的关系 |
| 03 | [Research](https://dongshuyan.com/awesome-harness-memory/#tutorial/research) | 研究者想解决什么问题，方法为什么这样设计，实验支持了哪些结论 |
| 04 | [工程实现](https://dongshuyan.com/awesome-harness-memory/#tutorial/engineering) | 真实系统怎样把保存、更新、读取、共享与权限落实到接口和配置 |
| 05 | [Benchmark](https://dongshuyan.com/awesome-harness-memory/#tutorial/benchmarks) | 一道评测题如何构造、怎样作答和计分，结果与六问有哪些联系及局限 |
| 06 | [文学与影视](https://dongshuyan.com/awesome-harness-memory/#tutorial/culture) | 用真实作品中的记忆设定思考遗忘、外部记录与身份，并区分作品事实和工程类比 |

主路径之外，可以按需要阅读[人类记忆背景](https://dongshuyan.com/awesome-harness-memory/#tutorial/human-memory)和[专题与实践](https://dongshuyan.com/awesome-harness-memory/#tutorial/topics)。读过具体条目后，[并排阅读](https://dongshuyan.com/awesome-harness-memory/#tutorial/compare)可以把它们的六问答案放在一起查看。

## 第一课的六个问题

| 问题 | 沿着它去理解 |
| --- | --- |
| **Q1 · 保存的是什么？** | 事实、经历、步骤、偏好或规则分别起什么作用；一个系统可能同时保存几种内容 |
| **Q2 · 它以什么形式、放在哪里？** | 原文、摘要、图、向量等表示，以及权威记录、索引与保存位置的区别 |
| **Q3 · 这份 Memory 归谁、服务谁、谁可以共享？** | 用户、会话、任务、项目、Agent 与团队之间的归属和共享范围 |
| **Q4 · 它如何形成、更新、失效和遗忘？** | 从事件进入系统，到提取、修订、合并、过期或删除的过程 |
| **Q5 · 后续调用如何获得并使用它？** | 信息怎样被选中、进入当前输入，以及是否真正影响了回答或行动 |
| **Q6 · 谁能读、写、改、删，并承担什么责任？** | 操作控制、授权、来源追溯、不可信输入与撤回责任 |

六问是从研究框架、官方工程资料和评测中归纳出的学习清单。[第一课](https://dongshuyan.com/awesome-harness-memory/#tutorial/lesson)最后给出事实、引用、推导和反例，解释为什么保留这些问题。它们帮助理解主要机制；没有被证明是唯一最小、数学正交或穷尽全部机制的集合。实际能力、成本和安全仍需要相应测试。

## 一篇详解怎样展开

每篇先介绍研究或系统是什么、作者或维护者是谁、可核对的机构、日期、原始入口与收录理由，再带入一个具体案例。六问的回答按机制拆成子节，用前后状态、对话、步骤、表格和配图说明原因。必要的技术细节和依据可以展开阅读，结尾有小练习、适用范围与来源。

下面三篇分别展示研究、工程和评测的阅读方式：

| 章节 | 跟着案例学什么 |
| --- | --- |
| [A-Mem](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/research/a-mem) | 一次经历如何形成记忆笔记，如何联系已有笔记，以及新信息怎样影响旧笔记的组织 |
| [Graphiti](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/engineering/graphiti) | 从原始事件走到实体与事实；事实发生变化时，怎样区分当前有效信息、历史和来源 |
| [LongMemEval](https://dongshuyan.com/awesome-harness-memory/#tutorial/detail/benchmarks/longmemeval) | 从多次会话、问题和证据，到检索、作答与评分；理解一道题能测到什么 |

配图紧邻相关解释，可以打开原图查看；手机上可横向阅读较宽的图表。教学假设、论文原例、作者报告的结果与作品类比分别标明，避免把示意过程当成已运行的实验。

## 课程内容

截至 **2026-11-15**，当前选定的 **49 篇详解、294 个六问回答和 61 张图**已纳入教程。各篇分别记录资料版本与核对日期；这个数量表示当前课程的范围。

| 类别 | 篇数 | 内容举例 |
| --- | ---: | --- |
| Research 主课 | 10 | A-Mem、CoALA、MemGPT、Generative Agents、Reflexion、Voyager |
| 研究延伸阅读 | 4 | 结构综述、图记忆、自主 Agent 记忆与 Storage–Reflection–Experience；在 Research 页面单列 |
| 工程实现 | 15 | Claude Code、Claude-Mem、Pi、LangGraph、Graphiti、Mem0、Hindsight 等 |
| Benchmark | 10 | LongMemEval、LoCoMo、MemoryAgentBench、COLLABMEM 等 |
| 文学与影视 | 8 | 《记忆碎片》《初恋50次》《记忆警察》《博士的爱情算式》等真实作品 |
| 人类记忆背景 | 2 | 记忆系统，以及遗忘与巩固 |

Research 主课最多两篇综述。条目按已知公开日期排序，不做质量排名；收录考虑原始材料可核、方法与证据质量、作者或维护团队、发表状态和时效性。团队声望和关注度不单独构成效果证据。详见[课程覆盖与证据边界](docs/coverage.md)。

## 从阅读走到实践

[专题与实践](https://dongshuyan.com/awesome-harness-memory/#tutorial/topics)进一步讨论安全与删除、成本与容量、评测设计，并提供一个无需 API Key 的本地示例。它用 SQLite 展示持久化、更正、范围过滤、过期与召回。

```sh
python3 examples/memory_lab.py
```

[实践步骤与预期输出](docs/practice.zh-CN.md)解释每一步与六问的关系。示例不调用模型；本站没有独立复现所引用论文的效果分数，也没有运行全部上游产品。

## 本地预览与维护

克隆仓库后，在仓库根目录启动静态服务器：

```sh
git clone https://github.com/dongshuyan/awesome-harness-memory.git
cd awesome-harness-memory
python3 -m http.server 8000 --bind 127.0.0.1
```

浏览器打开 <http://127.0.0.1:8000/>。配图从 `site/figures/` 加载，预览或发布时需要将它与 `index.html` 一起保留。

编辑教程时，修改权威数据 [`site/tutorial.json`](site/tutorial.json)，再构建页面并检查：

```sh
python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 scripts/build_lesson_figures.py --check
python3 -m unittest discover -s tests -v
node --check site/routes.js
node --check site/app.js
node --check site/tutorial.js
```

构建和教学示例使用 Python 标准库；完整测试还需要 Node.js，无需 npm 依赖。生成器、图稿规格与维护方式见[仓库结构](docs/repository-structure.md)；引用图片的许可见[配图来源](site/figures/pilot/ATTRIBUTIONS.md)。

贡献时请附原始来源、版本、具体章节、完整例子与局限。资料未说明的行为应保留为未知；作者报告、独立复现和文学类比应明确区分。本地下载的论文、源码和数据放在已忽略的 `.study-sources/`，不随网站发布。参见[贡献规范](CONTRIBUTING.md)与[维护计划](ROADMAP.md)。
