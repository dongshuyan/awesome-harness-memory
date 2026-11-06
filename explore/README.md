# Memory Atlas

[English](README.md) · [简体中文](README.zh-CN.md)

An earlier bilingual interactive map for understanding memory in agent systems. Choose a perspective, select a concept, and follow its connections to systems, papers, evaluations, or literary analogies.

## Open the map

From the repository root, run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open [the local atlas](http://127.0.0.1:8000/explore/). The page runs directly from plain HTML, CSS, and JavaScript, with no external assets. The resource catalog is generated separately when the source pages change. The map is also [available online](https://dongshuyan.github.io/awesome-harness-memory/explore/). The [current knowledge navigator](https://dongshuyan.github.io/awesome-harness-memory/) provides the expanded catalogue.

A [Chinese edition](http://127.0.0.1:8000/explore/index.zh-CN.html) has the same concepts, connections, resources, and sources. The language link preserves the current perspective and selected concept. Resource names retain their original spelling for lookup.

## Read the map

- **Continuity:** what carries forward between interactions?
- **Construction:** how does information become usable memory?
- **Change & control:** what changes when facts, sessions, or access change?

The perspectives share eight concepts. Switching perspective keeps the selected concept, even when it falls outside the new focus. Each connection has an explanation, a source, and a label distinguishing a documented system example from an editorial connection. Literature appears separately as analogy.

The map connects 19 technical resources and six literary works. The resource library contains all 32 distinct entries in this earlier edition. Seven papers also appear in the Benchmarks section; each keeps both entry links. These are representative connections, and the structure can change as the research develops.

Use Tab to move between controls, arrow keys to switch perspective tabs, Enter to select a concept, and Escape to close a resource. Browser Back and Forward restore the perspective and selected concept. On narrow screens, concepts appear as a list with the same textual connections.

## Maintain the content

The public Markdown pages in `resources/` are the source for resource summaries and links. After editing them, regenerate the catalog:

```sh
python3 explore/build_catalog.py
```

`content.js` holds the editorial concepts, perspectives, connections, and source-check date. Keep stable IDs when revising labels. In entries shared by papers and evaluations, the preview uses the evaluation summary; `catalog.js` retains both summaries and links.

`locale.zh-CN.js` contains the Chinese text overlay; it preserves graph identities and source URLs. Update the translations when English text changes. `locale.js` holds shared UI messages and applies the overlay. The parity tests check structural coverage, links, and placeholders; translation fidelity also needs editorial review.

Before sharing changes, run from the repository root:

```sh
python3 explore/build_catalog.py --check
node --test explore/tests/*.test.cjs
node --check explore/atlas.js
git diff --check
```

Also check concept selection, view switching, browser history, dialog focus, keyboard use, and narrow-screen layout in a browser. Automated checks validate catalog consistency and state logic; they do not establish source accuracy or visual quality.
