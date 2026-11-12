# 实践：一条记忆如何进入下一次调用

[课程首页](https://dongshuyan.com/awesome-harness-memory/) · [专题课](https://dongshuyan.com/awesome-harness-memory/#tutorial/topics) · [示例源码](../examples/memory_lab.py)

本例用 Python 标准库和 SQLite 展示跨调用的信息保留。没有调用语言模型、联网或下载模型，也没有生成模型效果分数。你会看到保存、更新、过滤与上下文组装的实际结果，再判断每一步解决了什么问题。

## 1. 先预测，再运行

在仓库根目录执行：

```sh
python3 examples/memory_lab.py
```

脚本使用临时目录，结束后自动清理。所有用户和项目内容都是教学构造。

先想一想：Alice先说使用npm，后来改成pnpm；Bob使用yarn。第二次调用读取Alice的记录时应该得到哪个值？如果一条记录已到期，或者用户要求不再召回，会发生什么？

实际输出：

```text
下一次调用可用的材料（没有调用模型）：
{"key": "package_manager", "value": "pnpm", "source": "correction-2", "trust": "unverified"}
已过期记录： []
其他范围： []
停止召回后： []
历史仍保留的版本数： 2
```

两次调用以两个独立数据库连接表示：第一次写入后关闭，第二次重新打开。这里只验证重新读取，尚未验证真实进程崩溃、网络故障或模型使用效果。

## 2. 用六问解释发生了什么

| 问题 | 代码中的回答 | 为什么这样设计 |
| --- | --- | --- |
| Q1 内容角色 | 项目工具偏好与临时任务信息 | 稳定偏好和短期信息的保留条件不同 |
| Q2 载体与表示 | SQLite记录，含key、value、source、时间和active；输出JSON | 保存来源和状态，便于定位答案用了哪一版 |
| Q3 主体与范围 | 每次读写都明确scope，如alice/repo | 同一个关键词不能自动混合不同范围；scope由调用方提供，不负责真实身份认证 |
| Q4 生命周期 | 更正时旧版失活，新版写入；过期不返回；forget停止召回 | 把“历史仍存在”和“当前应使用哪个值”分开 |
| Q5 暴露方式 | 词面匹配后将完整记录放进字符预算 | 库中有内容不等于模型收到；这里展示将交给调用方的材料，不实际调用模型 |
| Q6 控制与治理 | 调用方显式写入/更正/forget，保留source与unverified标记 | 不把保存过的信息自动升级为权威；标记本身不构成防提示注入保证 |

更正操作在一个数据库事务里先让旧版失活，再写新版。如果新写入失败，事务回滚，避免只留下“旧版已失效却没有新版”的中间状态。本例按调用顺序更新；不提供分布式冲突解决或历史时点查询。

## 3. 做三个小实验

1. **范围实验。** 把读取scope换成`bob/repo`，应得到yarn。换成`carol/repo`则为空。再检查：任何拿到数据库的本地代码都能传入这些scope，所以这只演示查询过滤，真实服务必须根据认证身份决定允许的scope。
2. **预算实验。** 把`max_chars=500`改成`10`，整条JSON会被略过，输出为空。这个预算按字符计算，不是模型token；不能据此宣称控制了实际模型费用。想用于真实模型，需要该模型的tokenizer和完整提示预算。
3. **遗忘实验。** 查看`forget`和`history`：前者只让记录不再参与正常召回，后者仍能读取旧版。SQLite文件、备份和派生索引的物理删除不在本例范围内。

## 4. 验证和继续学习

```sh
python3 -m unittest discover -s tests -p test_memory_lab.py -v
```

测试覆盖更正后重新打开读取、范围分离、过期边界、停止召回但保留历史、整条记录预算和无效写入不破坏已有记录。它们验证本地实现的行为，不是新Benchmark，也不评价任何上游Memory产品。

之后可以把检索材料送入真实模型，并加入无记忆、完整历史等对照，分别测正确性、来源保留、延迟和费用。那会产生新的数据与成本，本仓库当前示例没有执行这一步。

这些实验的设计与官方文档中的区分相呼应：[LangGraph Memory](https://docs.langchain.com/oss/python/concepts/memory)区分线程状态与跨线程存储；[Strands检查点与记忆](https://strandsagents.com/docs/user-guide/harness/configure/checkpoints-and-memory/)区分运行恢复与长期事实；[Anthropic Context Engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)讨论按需读取、压缩与结构化笔记。它们支持教学问题的来源，不是本地示例可靠性的认证。
