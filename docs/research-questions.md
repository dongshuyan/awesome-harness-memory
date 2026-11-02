# Questions for the next research rounds

[Home](../README.md) · [Roadmap](../ROADMAP.md)

The first edition uses practical navigation routes. The following questions remain open; they are not a proposed taxonomy or a required entry schema.

## What is being called memory?

How do projects distinguish active context, resumable task state, shared workspace information, user preferences, facts, and accumulated experience? Which labels refer to lifetime, which to ownership, and which to the representation or purpose of information?

Context management, continuity across sessions in a workspace, and long-term interaction with a user are initial questions to investigate. They may overlap or split after studying real implementations. Workspace continuity here does not mean spatial or navigation memory.

## Where does the behavior live?

When does an agent decide what to remember, and when does its harness or a service make that decision? Which operations come from the model, prompts, runtime, storage, or application code? Can the same mechanism be exposed through several layers?

The comparison should follow actual reads, writes, retrieval, and updates before assigning labels such as "agent memory" or "harness memory."

## What survives a change?

What happens after a new turn, context compaction, a new session, a restart, a user switch, or a model change? How are conflicting facts, stale memories, and corrections handled? Does forgetting mean lower retrieval priority, invalidation, or deletion?

## What should evaluation establish?

Which benchmarks measure recall, and which measure useful behavior in later tasks? How do protocols account for insufficient evidence, conflicting information, cost, latency, privacy boundaries, or poisoned input? What controls separate the effect of memory from additional context or computation?

## How should readers navigate?

Would a map of mechanisms, a comparison by use case, or several linked views help more than one tree? Which details are necessary for choosing a resource, and which belong in the source documentation? These decisions will follow representative reading and reader feedback.
