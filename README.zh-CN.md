# Awesome Harness Memory

> Agent Memory 教程：先学会怎样认识一个 Memory 系统，再阅读精选的研究、工程、Benchmark，以及真实文学影视作品里的记忆思想实验。

[English](README.md) · **[打开交互教程](https://dongshuyan.github.io/awesome-harness-memory/)** · [旧版资源目录](resources/systems.zh-CN.md) · [仓库结构](docs/repository-structure.md)

这个仓库现在以“教程”为主，不是排行榜，也不是把所有资料堆在一起的百科目录。课程先用六个问题建立共同的观察方法，再把这六个问题带入 Research、Agent/Harness、独立 Memory 系统、Benchmark 和文化类比。文学与影视只用于类比和思想实验，不作为模型能力或工程安全的证据。

## 课程主路径

1. **第一课：六个核心问题。** 保存的是什么？它以什么形式、放在哪里？这份 Memory 归谁、服务谁、谁可以共享？它如何形成、更新、失效和遗忘？后续调用如何获得并使用它？谁能读、写、改、删，并承担什么责任？
2. **相关概念辨析。** Context、session history、RAG、checkpoint、参数/KV 状态和 generic storage 可能参与 Memory，但它们不是同一个概念。
3. **Research。** 先看身份、纳入依据和证据边界，再逐条按六问阅读研究框架和方法。
4. **工程。** 阅读具名 Agent、Harness、Framework、独立 Memory 系统和托管服务，区分官方文档、公开代码、观察结果与未说明项。
5. **Benchmark。** 说明目标能力、任务协议、指标，以及它们和六问的交集。不同 Benchmark 的分数不会被合成为一个排名。
6. **文学与影视。** 阅读真实的小说、短篇、电影和剧集，把它们作为直观的类比或思想实验。

读完具体条目后，可以进入最后的比较页，选择多个对象并排查看已有的六问答案。比较是辅助工具，不替代每个条目的独立阅读。

## 当前教程工作集

截至 **2026-11-12** 的教程快照包含：

- **10 个精选 Research**，其中 10 个已有完整六问详解；另有 4 个研究候选作为待筛线索保留在 Research 页面；
- **15 个工程系统**，其中 13 个已有完整六问详解；
- **10 个 Benchmark**，其中 10 个已有完整六问详解；
- **6 个文学与影视条目**，*Memento* 和 Borges 的短篇 “Funes the Memorious” 已完成文化类样板；
- **2 个人类记忆背景条目**，以及专题和工具页面。

其余条目会明确标记为 **待完善**。待完善表示它已经有来源入口、收录理由和证据边界，但六问答案还没有逐项核实；页面不会把摘要扩写成事实。

Research 和工程条目按来源质量、作者或维护团队可识别性、时效性和可复核性筛选。优先采用同行评议论文、会议论文集、官方文档和原作者仓库；只有预印本的条目会单独标明证据边界。列表按已知公开年份倒序，公开日期未说明的条目置后；顺序不是质量排名。

## 公共数据与保留内容

- [`site/tutorial.json`](site/tutorial.json) 是教程权威数据，保存六问、来源、条目、状态、样板答案、Benchmark 覆盖关系和可视化说明。
- [`site/tutorial.js`](site/tutorial.js) 负责教程路由、详情页、六问比较和覆盖矩阵。
- [`site/frame.html`](site/frame.html) 与 [`site/app.js`](site/app.js) 提供页面外壳和路由；[`index.html`](index.html) 是 GitHub Pages 的生成入口。
- 旧版分类与方法、资源目录、七层 Harness 图解和[研究 × 工程对照报告](https://dongshuyan.github.io/awesome-harness-memory/report/index.html)仍然保留在“参考与工具”入口。它们各自有独立的证据范围；默认学习路径改为本教程。

根目录的旧版结构化目录以 2026-11-06 版本为基础，经 2026-11-12 身份纠正后有 **136 项公共资源**。这个数字与上面的教程工作集分开统计，不表示行业总量、市场占比、性能结果或完整性承诺。

## 本地预览与检查

在仓库根目录运行：

```sh
python3 scripts/build_site.py
python3 -m unittest discover -s tests -v
python3 -m http.server 8000 --bind 127.0.0.1
```

打开 `http://127.0.0.1:8000/`。构建脚本会把目录和教程数据嵌入静态页面，不需要安装依赖，也不依赖服务端重写。`python3 scripts/build_site.py --check` 会检查生成文件是否与权威源同步。

公共页面只陈述已记录的事实和证据边界，不声称已经安装系统、运行 Benchmark 或完成效果复现。资料未说明某项机制时，页面保留为未知，不把它解释成“不支持”。私有检索计划和审阅记录不放入公共仓库。

参见[贡献指南](CONTRIBUTING.md)、[路线图](ROADMAP.md)和[仓库结构与发布说明](docs/repository-structure.md)。
