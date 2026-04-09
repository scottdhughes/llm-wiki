---
title: "LLM Wiki Architecture"
created: 2026-04-05
last_updated: 2026-04-07
source_count: 3
status: draft
---

# LLM Wiki Architecture

Synthesis of three diagrams describing an agent-maintained markdown wiki that turns raw sources into a compounding knowledge base through ingest, Q&A, outputs, and file-back loops.

## Architecture At A Glance

- `raw/` is the immutable intake layer for files, images, and other source artifacts.
- `wiki/` is the compiled markdown knowledge base where summaries, concepts, links, and analyses live.
- Q&A happens against the wiki, not directly against the full raw corpus.
- Outputs are rendered from the wiki, then important results are written back into the wiki so future work starts from a stronger baseline.
- Maintenance is continuous through indexing, linting, search, and heal suggestions.

## Evidence

- [LLM Wiki Diagram 1](../sources/llm-wiki-diagram-1.md) emphasizes the five-step pipeline and the knowledge-compounding feedback loop. [Source: llm-wiki-diagram-1.md]
- [LLM Wiki Diagram 2](../sources/llm-wiki-diagram-2.md) decomposes the engine into compile, Q&A, linting, and indexing subsystems. [Source: llm-wiki-diagram-2.md]
- [LLM Wiki Diagram 3](../sources/llm-wiki-diagram-3.md) presents the architecture as a user-facing workflow and product story. [Source: llm-wiki-diagram-3.md]

## Operating Loop

1. Ingest raw sources into the immutable layer.
2. Replace generated source pages with real summaries and extracted points.
3. Synthesize durable concepts, entities, and analyses from those sources.
4. Search and read the wiki before answering new questions.
5. File durable answers back into the wiki instead of leaving them only in chat.
6. Run lint and heal so the graph stays connected, non-duplicative, and navigable.

## Key Points

- All three diagrams agree that the wiki, not the raw source store, is the main operational surface for future reasoning.
- The most important loop is not ingest alone; it is ingest plus synthesis plus file-back.
- Obsidian and CLI tooling are support layers around the same underlying markdown knowledge base.
- The architecture assumes the wiki stays small and curated enough that a lightweight search-and-read workflow remains practical.

## Design Implications For This Repo

- Image files should be first-class sources because diagrams often contain architecture intent that is missing from prose.
- The first paragraph of each page matters disproportionately because it drives both the index and fast retrieval.
- `heal` should act as a maintenance queue, not just a checker, by pointing to missing ingests, broken links, orphan pages, and duplicate topics.
- The repo should bias toward reusable markdown synthesis first, with output renderers layered on top later.

## Contradictions

- No direct contradictions appear across the three diagrams, but Diagram 1 is more aggressive about "no RAG needed" than the repo should promise in general use.

## Related Pages

- [Overview](../overview.md)
- [LLM Wiki Diagram 1](../sources/llm-wiki-diagram-1.md)
- [LLM Wiki Diagram 2](../sources/llm-wiki-diagram-2.md)
- [LLM Wiki Diagram 3](../sources/llm-wiki-diagram-3.md)

## Open Questions

- What should the next major implementation step be after ingest, search, lint, and heal: compile automation or output renderers?
- How should the repo represent confidence, uncertainty, and conflicting sources as the wiki grows?
- When the wiki gets materially larger, what replaces or augments the current lightweight local search model?
