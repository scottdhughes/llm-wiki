---
title: "LLM Wiki Architecture"
created: 2026-04-05
last_updated: 2026-04-08
source_count: 4
status: draft
---

# LLM Wiki Architecture

Synthesis of the repo's operating model: immutable raw sources, a compiled markdown wiki, portable agent instructions, and CLI maintenance loops that keep knowledge durable and reusable.

## Architecture At A Glance

- `raw/` is the immutable intake layer for files, images, and other source artifacts.
- `wiki/` is the compiled markdown knowledge base where summaries, concepts, links, and analyses live.
- `AGENTS.md`, `CLAUDE.md`, and `PROMPTS.md` define the portable workflow for agents that operate on the repo.
- Q&A happens against the wiki, not directly against the full raw corpus.
- Outputs are rendered from the wiki, then important results are written back into the wiki so future work starts from a stronger baseline.
- Maintenance is continuous through indexing, linting, status snapshots, search, watch mode, and hook-driven refreshes.

## Evidence

- The main architecture loop, command surface, and project layout are described in the root README. [Source: README.md]
- The agent operating rules, page conventions, and maintenance loop are defined in the repo guidelines. [Source: AGENTS.md]
- The schema file defines the durable distinction between `raw/`, `wiki/`, and `outputs/`. [Source: CLAUDE.md]
- The prompt library shows how the workflow is meant to be driven by a local-file-aware coding agent. [Source: PROMPTS.md]

## Operating Loop

1. Ingest raw sources into the immutable layer.
2. Replace generated source pages with real summaries and extracted points.
3. Synthesize durable concepts, entities, and analyses from those sources.
4. Search and read the wiki before answering new questions.
5. File durable answers back into the wiki instead of leaving them only in chat.
6. Run lint and heal so the graph stays connected, non-duplicative, and navigable.

## Key Points

- The wiki, not the raw source store, is the main operational surface for future reasoning.
- The most important loop is not ingest alone; it is ingest plus synthesis plus file-back.
- Obsidian and CLI tooling are support layers around the same underlying markdown knowledge base.
- Managed hooks and watch mode are convenience layers, not separate sources of truth.
- The architecture assumes the wiki stays small and curated enough that a lightweight search-and-read workflow remains practical.

## Design Implications For This Repo

- Image files should remain first-class sources even if the starter repo itself ships without bundled personal images.
- The first paragraph of each page matters disproportionately because it drives both the index and fast retrieval.
- `heal` should act as a maintenance queue, not just a checker, by pointing to missing ingests, broken links, orphan pages, and duplicate topics.
- The repo should bias toward reusable markdown synthesis first, with output renderers layered on top later.

## Contradictions

- The repo stays intentionally simple, but the docs should not over-promise that lightweight local search removes the need for other retrieval strategies in every domain.

## Related Pages

- [Overview](../overview.md)

## Open Questions

- What should the next major implementation step be after ingest, search, lint, and heal: compile automation or output renderers?
- How should the repo represent confidence, uncertainty, and conflicting sources as the wiki grows?
- When the wiki gets materially larger, what replaces or augments the current lightweight local search model?
