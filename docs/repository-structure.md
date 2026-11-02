# Repository structure

[Home](../README.md) · [Research questions](research-questions.md) · [Roadmap](../ROADMAP.md)

The guide uses a small set of Markdown pages so that navigation can change as the mechanism research develops. The directory is intentionally easy to reorganize.

```text
.
├── README.md                 # English entry point
├── README.zh-CN.md           # Chinese README
├── ROADMAP.md                # Research rounds and future work
├── CONTRIBUTING.md           # Public sourcing and contribution guidance
├── docs/
│   ├── repository-structure.md
│   ├── research-questions.md # Open questions and sourced comparisons
│   └── evaluation-guide.md  # Choose evaluations by the behavior needed
└── resources/
    ├── systems.md            # Systems, harnesses, libraries, products
    ├── papers.md             # Chronological reading timeline
    ├── benchmarks.md         # Evaluation methods and limits
    └── fiction.md            # Literature and screen analogies
```

The private research directory is a sibling of this repository and is not part of the public tree. It contains the research plan, candidate queue, source log, assessment research, review resolution, and validation notes. Keeping those records physically separate avoids treating `.gitignore` as the privacy boundary.

The directory names and page split are provisional. After representative implementations and evaluations have been compared, this repository may gain a mechanism map, cross-links, or a different entry format. Such a change should be supported by the collected evidence rather than by an assumed number of memory types.
