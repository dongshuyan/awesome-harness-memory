# Repository structure

[Home](../README.md) · [中文](../README.zh-CN.md) · [Interactive guide](https://dongshuyan.github.io/awesome-harness-memory/)

The main reading path is the Agent Memory tutorial: six questions → concept bridge → Research → engineering → benchmarks → literature and screen. The earlier landscape, catalogue, comparisons, and layered illustrations remain reference editions.

```text
.
├── README.md                 # English entry and scope
├── README.zh-CN.md           # Chinese entry and scope
├── index.html               # Current standalone Chinese navigator
├── site/                    # Authoritative templates, UI, tutorial data and legacy topic mappings
│   ├── tutorial.json         # Six-question course, entries, sources, status and visualization data
│   └── tutorial.js           # Tutorial routes, detail pages, comparison and matrices
├── scripts/build_site.py    # Generate HTML, guide and graph preview without dependencies
├── catalogue.json           # Current public records, sources, and status
├── .nojekyll                # Serve static files without Jekyll processing
├── report/
│   ├── index.html           # Published research × engineering report (preserved reference report with documented identity corrections)
│   └── MANIFEST.json        # Version, source hash, counts, and evidence boundary for report/
├── assets/                  # README images and real Harness graph data/UI
├── scripts/build_harness_map.py # Embed graph data/UI and generate static preview
├── tests/test_harness_map.py # Graph coverage, provenance and generation checks
├── docs/
│   ├── landscape.zh-CN.md    # Legacy taxonomy and method navigator
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

The tutorial is the default learning edition. Its 2026-11-12 workset contains 10 selected Research entries, 15 engineering entries, 10 benchmarks, 6 literature/screen entries, and 2 human-memory background entries; four additional research leads remain visible as screened candidates. Each technical category now has five complete entries. Research covers CoALA, Forms–Functions–Dynamics, MemGPT, Generative Agents, and A-Mem; engineering covers Claude Code, LangGraph, Google Agent Platform Memory Bank, Mem0, and Graphiti; benchmarks cover LongMemEval, MemoryAgentBench, COLLABMEM, LoCoMo, and MemBench. Other entries are explicitly pending until their six answers are sourced. The older navigator, expanded Chinese Markdown pages, and root `catalogue.json` share a separate 136-resource edition (identity-corrected on 2026-11-12), including 48 systems with documented basic functions. A resource status does not certify performance or safety.

`explore/` preserves the earlier concept-and-relationship map and its 32-resource English/Chinese catalogue. Its `build_catalog.py` reads the earlier English resource pages and writes only `explore/catalog.js`; it does not update the root catalogue or latest navigator. Follow [its maintenance notes](../explore/README.md#maintain-the-content) when changing that edition.

The legacy learning guide has nine editorial questions and separately sourced memory taxonomies. The tutorial's six questions are a newer course structure and do not claim that the older nine labels are invalid. The seven-layer diagram remains a selected evidence projection, rather than a complete measurement of the tutorial questions. It uses 21 real Harness / Agent profiles (including three labeled historical projects). `assets/harness-map.json` owns those property claims, configuration conditions, and source references. Profiles link to root catalogue IDs; a documented component may have a more specific display name. Missing claims remain unknown. The broader resource directory retains memory services, plugins, and general frameworks.

After editing `site/`, the root catalogue, graph data or graph UI, run `python3 scripts/build_site.py`. It embeds the full catalogue, legacy topic data, tutorial data and graph into `index.html`, and generates `docs/landscape.zh-CN.md` and `assets/memory-layers.svg`. These generated files should not be edited directly. `build_harness_map.py` remains the graph-specific builder used by the site build. Run with `--check` to detect stale generated files, and run `python3 -m unittest discover -s tests -v` for the data contract. The static preview deliberately shows six objects and three perspectives; the interactive graph contains all profiles. Tutorial data is checked separately for six-question order, one complete technical sample per category, source provenance, pending states, real culture entries, and visualization descriptions.

## Publishing and maintenance

GitHub Pages serves the `master` branch at `/` with `.nojekyll`; `index.html` is the entry point. No package install is required. Run the standard-library Python site builder before publishing changes. The standalone page contains its catalogue; it uses pinned CDN scripts for interface utilities. Its original-source links open through the outer page while the inner frame remains sandboxed.

Before publishing a content update, keep `catalogue.json`, the rendered catalogue in `index.html`, and the corresponding Markdown entries consistent. Check local links, evidence labels, counts, JavaScript syntax, source-link navigation, and the affected interactions. The public site does not perform new research or run benchmarks.

Run a local server from the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. For a deployed revision, verify the Pages build commit matches the pushed commit and inspect the live page.

Only public descriptions, references, and interface files belong in this tree. Private research plans, source receipts, internal assessments, and review records remain outside it.
