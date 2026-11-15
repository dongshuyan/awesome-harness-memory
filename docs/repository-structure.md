# Repository structure

The public site is a Chinese Agent Memory course. Its main path is six questions → related concepts → Research → engineering → Benchmark → literature and film. Human-memory background, topics, local practice, and optional comparison support that path.

```text
.
├── README.md / README.zh-CN.md   # English and Chinese course entry points
├── index.html                   # Generated course HTML
├── site/
│   ├── tutorial.json            # Lessons, entries, examples, sources and topics
│   ├── tutorial.js              # Chapter and detail renderers
│   ├── tutorial.css             # Reading layout and responsive styles
│   ├── figures/pilot/           # Teaching diagrams, credited source figures
│   ├── figures/lessons/         # Original diagrams and their logical specifications
│   ├── routes.js                # Shareable chapter, section and comparison URLs
│   ├── app.js                   # Navigation, focus and comparison interactions
│   └── frame.html               # Document, course navigation and content slots
├── examples/memory_lab.py       # Standard-library SQLite teaching example
├── docs/
│   ├── coverage.md              # Course scope and evidence limits
│   ├── practice.zh-CN.md        # Walkthrough and expected output
│   └── repository-structure.md
├── scripts/build_site.py        # Validate data and generate index.html
├── scripts/build_pilot_figures.py # Regenerate the six teaching SVGs
├── scripts/build_lesson_figures.py # Render the remaining chapters' teaching SVGs
├── .study-sources/              # Ignored local papers, pinned code and small data
└── tests/                      # Data, route, renderer and example behavior
```

## Content ownership

`site/tutorial.json` is the authoritative course content. It contains 10 Research core entries, four further readings, 15 engineering entries, 10 benchmarks, eight cultural works, and two human-memory lessons: **49 entries with six answers each**. Six concept sections and four practical topics support the main path. The Research core includes at most two surveys; `researchCandidates` is the internal key for the four further readings.

Each answer contains `answer`, `why`, `example`, and `trace`. Technical answers also list `sources` IDs for direct references. Blank lines in `example` form paragraphs. An optional `caseStudy` connects the six examples; `profile.affiliation` and `affiliationSources` record verified author institutions. Dates distinguish first publication, reading version, and source checks. The internal `status` field helps validate the data and is not shown to readers.

Chapters use `sections` for structured explanations. These replace the rendered `why` and `example` summaries while retaining `answer` and `trace`. Their blocks support paragraphs, dialogue, code, steps, tables, figures and optional detail. `openingBlocks` introduces the ongoing example and `recapBlocks` provides a reading check. Research frameworks, implementations, benchmarks and cultural works retain their own evidence boundaries; a teaching scenario is not a reported experiment or a plot claim.

The browser reads only course content. It presents single-column lists and continuous detail pages, with a section directory and expandable source notes. The Benchmark page retains a readable relation table; it does not claim that describing a direction establishes a tested capability. Comparison displays the existing answers without generating scores.

## Build and verify

Edit the sources, then regenerate the public page:

```sh
python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 scripts/build_lesson_figures.py --check
python3 -m unittest discover -s tests -v
node --check site/routes.js
node --check site/app.js
node --check site/tutorial.js
python3 examples/memory_lab.py
```

The builder and example use the Python standard library. Renderer tests require Node.js; there are no npm dependencies. The builder embeds course data, CSS and JavaScript into `index.html`. Do not edit that output directly. The site has no external scripts, font downloads or embedded application frame.

Figures load from `site/figures/pilot/` and `site/figures/lessons/`, so keep both directories with the HTML when previewing or publishing. The pilot's `ATTRIBUTIONS.md` records reused figures' credits and licenses. The lessons' `specs.json` records the goal, structure, caption, alternative text and source IDs of each original diagram. Regenerate with `python3 scripts/build_pilot_figures.py` or `python3 scripts/build_lesson_figures.py` after editing the respective sources, then inspect the rendered images. Generation checks verify consistency, not the scientific validity of a diagram.

Tests check source references, six-question completeness, unique identities, dates, generated-file consistency, routes, comparison discovery, answer ordering and local example behavior. They do not establish scientific correctness. Check changed passages against primary sources and inspect desktop/mobile reading, keyboard navigation and history in a browser.

## Preview and publish

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. GitHub Pages serves `master` at `/` with `.nojekyll`, at [the course URL](https://dongshuyan.com/awesome-harness-memory/).

Before publishing, check the complete diff, data and source links, synchronized README content, and independent review. After pushing, verify the remote commit, Pages build and live course. Local source material belongs in the ignored `.study-sources/` directory; keep private review transcripts outside the repository. Retired catalogues, maps and reports remain available in Git history rather than the current site.
