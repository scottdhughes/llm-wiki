# Knowledge Compounds Brief

This brief compiles 4 wiki pages relevant to `knowledge compounds`.

## Scope

- Generated: 2026-04-05 21:11 EDT
- Query: `knowledge compounds`
- Pages: 4

## Highlights

- LLM Wiki Diagram 1: This diagram presents the LLM wiki as a five-step pipeline: gather sources, store them in `raw/`, compile them into a markdown wiki, answer questions against that wiki, and render outputs that can be filed back into the knowledge base.
- LLM Wiki Architecture: Synthesis of three diagrams describing an agent-maintained markdown wiki that turns raw sources into a compounding knowledge base through ingest, Q&A, outputs, and file-back loops.
- LLM Wiki Diagram 2: This diagram reframes the same LLM wiki idea as a systems map, separating data ingest, the LLM engine, the markdown knowledge store, outputs, and the IDE frontend into distinct modules connected by explicit flows.
- LLM Wiki Diagram 3: This diagram turns the LLM wiki architecture into a cleaner presentation narrative, emphasizing the user journey: collect sources, let the model organize the wiki, ask questions, render outputs, and file the results back so the wiki compounds.

## Source Pages

- [LLM Wiki Diagram 1](../wiki/sources/llm-wiki-diagram-1.md) - This diagram presents the LLM wiki as a five-step pipeline: gather sources, store them in `raw/`, compile them into a markdown wiki, answer questions against that wiki, and render outputs that can be filed back into the knowledge base.
- [LLM Wiki Architecture](../wiki/analyses/llm-wiki-architecture.md) - Synthesis of three diagrams describing an agent-maintained markdown wiki that turns raw sources into a compounding knowledge base through ingest, Q&A, outputs, and file-back loops.
- [LLM Wiki Diagram 2](../wiki/sources/llm-wiki-diagram-2.md) - This diagram reframes the same LLM wiki idea as a systems map, separating data ingest, the LLM engine, the markdown knowledge store, outputs, and the IDE frontend into distinct modules connected by explicit flows.
- [LLM Wiki Diagram 3](../wiki/sources/llm-wiki-diagram-3.md) - This diagram turns the LLM wiki architecture into a cleaner presentation narrative, emphasizing the user journey: collect sources, let the model organize the wiki, ask questions, render outputs, and file the results back so the wiki compounds.

## Notes By Page

### LLM Wiki Diagram 1

This diagram presents the LLM wiki as a five-step pipeline: gather sources, store them in `raw/`, compile them into a markdown wiki, answer questions against that wiki, and render outputs that can be filed back into the knowledge base.

Source: [LLM Wiki Diagram 1](../wiki/sources/llm-wiki-diagram-1.md)

Key details:

- The central red `WIKI` block is the hub of the system, with arrows feeding in from `raw/` and out to Q&A and outputs.
- A top feedback arrow labeled "filed back - knowledge compounds" shows that each output can improve the wiki instead of remaining a one-off artifact.
- A support layer under the main pipeline highlights Obsidian, lint-and-heal workflows, and CLI tools as connected maintenance infrastructure.
- The footer calls out the main thesis explicitly: the human steers, while the LLM does the writing and the knowledge compounds over time.

### LLM Wiki Architecture

Synthesis of three diagrams describing an agent-maintained markdown wiki that turns raw sources into a compounding knowledge base through ingest, Q&A, outputs, and file-back loops.

Source: [LLM Wiki Architecture](../wiki/analyses/llm-wiki-architecture.md)

Key details:

- `raw/` is the immutable intake layer for files, images, and other source artifacts.
- `wiki/` is the compiled markdown knowledge base where summaries, concepts, links, and analyses live.
- Q&A happens against the wiki, not directly against the full raw corpus.
- Outputs are rendered from the wiki, then important results are written back into the wiki so future work starts from a stronger baseline.

### LLM Wiki Diagram 2

This diagram reframes the same LLM wiki idea as a systems map, separating data ingest, the LLM engine, the markdown knowledge store, outputs, and the IDE frontend into distinct modules connected by explicit flows.

Source: [LLM Wiki Diagram 2](../wiki/sources/llm-wiki-diagram-2.md)

Key details:

- The left side groups ingestion sources such as articles, papers, repos, datasets, and images, with an Obsidian web clipper feeding them into `raw/`.
- The center column decomposes the LLM engine into compile, Q&A, linting, and indexing rather than treating the model as a single opaque step.
- The knowledge store on the right is the `Wiki (.md)` box, annotated with summaries, backlinks, concepts, and categories.
- The bottom layers show outputs and interface surfaces separately, emphasizing that markdown, slides, and charts are generated from the wiki while Obsidian remains the browsing frontend.

### LLM Wiki Diagram 3

This diagram turns the LLM wiki architecture into a cleaner presentation narrative, emphasizing the user journey: collect sources, let the model organize the wiki, ask questions, render outputs, and file the results back so the wiki compounds.

Source: [LLM Wiki Diagram 3](../wiki/sources/llm-wiki-diagram-3.md)

Key details:

- The page is designed like an explanatory landing page, with a headline, a core insight banner, and grouped cards for each step.
- The top row breaks the flow into five cards: collect sources, LLM organizes wiki, ask questions, render outputs, and file back to wiki.
- A dedicated "tools layer" highlights Obsidian, lint-and-heal, and search-plus-CLI as enabling infrastructure beneath the main loop.
- The right-hand callout "Try This Workflow Yourself" translates the diagram into an operational checklist for a real repo.

## Related Pages

- [LLM Wiki Diagram 1](../wiki/sources/llm-wiki-diagram-1.md)
- [LLM Wiki Architecture](../wiki/analyses/llm-wiki-architecture.md)
- [LLM Wiki Diagram 2](../wiki/sources/llm-wiki-diagram-2.md)
- [LLM Wiki Diagram 3](../wiki/sources/llm-wiki-diagram-3.md)
