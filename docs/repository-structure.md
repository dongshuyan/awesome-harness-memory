# Repository structure

[Home](../README.md) · [中文](../README.zh-CN.md) · [Interactive guide](https://dongshuyan.github.io/awesome-harness-memory/)

The main reading path is landscape → methods → resources. Needs and object types provide shortcuts; system comparisons and layered illustrations are deeper views.

```text
.
├── README.md                 # English entry and scope
├── README.zh-CN.md           # Chinese entry and scope
├── index.html               # Current standalone Chinese navigator
├── catalogue.json           # Current public records, sources, and status
├── .nojekyll                # Serve static files without Jekyll processing
├── assets/                  # README overview and illustrative layered diagram
├── docs/
│   ├── landscape.zh-CN.md    # Seven perspectives and methods
│   ├── needs.zh-CN.md        # Routes from concrete needs
│   ├── evaluation-guide.md  # English evaluation comparison guide
│   └── research-questions.md
├── resources/
│   ├── systems.zh-CN.md      # Current systems and products
│   ├── papers.zh-CN.md       # Current papers and methods
│   ├── benchmarks.zh-CN.md   # Current evaluations
│   ├── surveys.zh-CN.md      # Survey reading routes
│   ├── human.zh-CN.md        # Human memory research
│   ├── fiction.zh-CN.md      # Literature and screen analogies
│   └── *.md                 # Earlier English reference pages
└── explore/                 # Earlier bilingual concept map, 32 resources
```

## Reading editions

The latest navigator, expanded Chinese Markdown pages, and root `catalogue.json` share the same 137-resource edition, including 48 systems with documented basic functions. A resource status does not certify performance or safety.

`explore/` preserves the earlier concept-and-relationship map and its 32-resource English/Chinese catalogue. Its `build_catalog.py` reads the earlier English resource pages and writes only `explore/catalog.js`; it does not update the root catalogue or latest navigator. Follow [its maintenance notes](../explore/README.md#maintain-the-content) when changing that edition.

The seven-layer diagram uses fictional systems to explain the visualization. Real-system comparisons use documented descriptions and explicitly unknown properties.

## Publishing and maintenance

GitHub Pages serves the `master` branch at `/` with `.nojekyll`; `index.html` is the entry point. No package install or site build is required. The standalone page contains its catalogue; it uses pinned CDN scripts for interface utilities. Its original-source links open through the outer page while the inner frame remains sandboxed.

Before publishing a content update, keep `catalogue.json`, the rendered catalogue in `index.html`, and the corresponding Markdown entries consistent. Check local links, evidence labels, counts, JavaScript syntax, source-link navigation, and the affected interactions. The public site does not perform new research or run benchmarks.

Run a local server from the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. For a deployed revision, verify the Pages build commit matches the pushed commit and inspect the live page.

Only public descriptions, references, and interface files belong in this tree. Private research plans, source receipts, internal assessments, and review records remain outside it.
