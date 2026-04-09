# LLM Wiki Agent Guidelines

This repo is a persistent thinking layer. Treat it like a disciplined markdown knowledge base, not like a chat transcript.

## Operating Model

- `raw/` stores immutable source material.
- `wiki/` stores the compiled markdown knowledge base.
- `outputs/` stores generated briefs, reports, and durable answer artifacts.
- `wiki/index.md` is the content map.
- `wiki/log.md` is the chronological change trail.
- Source pages preserve provenance; concept, entity, and analysis pages do synthesis.

## Directory Rules

- Never edit files in `raw/` after they have been ingested or compiled.
- Put images, diagrams, screenshots, and other visual artifacts in `raw/assets/`.
- Keep source interpretation in `wiki/sources/`.
- Keep reusable ideas in `wiki/concepts/`.
- Keep people, organizations, projects, datasets, and tools in `wiki/entities/`.
- Keep comparisons, deep dives, recurring questions, and durable reports in `wiki/analyses/`.
- Use relative markdown links for internal references.

## Core Loop

1. Ingest new material with `python3 -m llm_wiki ingest ...`, `python3 -m llm_wiki ingest-url ...`, or batch-process `raw/inbox/` with `python3 -m llm_wiki compile`.
2. Replace generated starter text with a sharp first paragraph, key points, evidence, contradictions, and open questions.
3. Pull durable ideas into concept, entity, and analysis pages instead of leaving them stranded in source pages.
4. Read `wiki/index.md` and use `python3 -m llm_wiki search "<query>"` before answering.
5. File durable answers back into the wiki. Use `python3 -m llm_wiki brief ...` when a report-shaped markdown output is useful, and save those artifacts in `outputs/` when they are worth keeping.
6. Run `python3 -m llm_wiki watch --status-output outputs/status.md` while actively editing, or install managed hooks with `python3 -m llm_wiki hook install --status-output outputs/status.md` so commit, checkout, and merge flows keep the derived files fresh.
7. Periodically run `python3 -m llm_wiki status`, `python3 -m llm_wiki index`, `python3 -m llm_wiki lint`, and `python3 -m llm_wiki heal` to keep the graph coherent.

## Commands

- `ingest`: copy one file into canonical raw storage and create a source page.
- `ingest-url`: fetch a web page, save an immutable markdown snapshot, and create a source page.
- `compile`: promote all files from `raw/inbox/` into canonical raw storage and create source pages in one batch.
- `search`: find relevant pages before answering.
- `brief`: assemble selected or query-matched wiki pages into a markdown report.
- `status`: summarize corpus health, coverage, structural issues, and next actions.
- `watch`: monitor `raw/inbox/` and `wiki/`, compile new inbox files, rebuild the index after wiki edits, and optionally refresh a status snapshot.
- `hook install`: install managed git hooks for pre-commit, post-checkout, and post-merge refreshes.
- `hook status`: show whether the managed hooks are installed cleanly.
- `hook uninstall`: remove managed hooks and restore any backups created with `--force`.
- `lint`: catch broken links, orphan pages, and missing summaries.
- `heal`: turn the lint state into concrete repair suggestions.

## Page Rules

- Every page gets exactly one `# Title`.
- Generated pages include YAML frontmatter for title, dates, source count, and status.
- The first paragraph must stand alone as the page summary. It drives indexing and retrieval.
- Prefer expanding an existing page over creating a near-duplicate.
- Keep synthesized claims attributable in `[Source: page-or-file]` form whenever possible.
- Keep a `## Contradictions` section current when sources disagree or older claims have been superseded.
- Keep a `## Related Pages` section current whenever a page touches existing material.
- If a question keeps recurring, convert it into a durable analysis page.

## Style

- Keep markdown terse and scannable.
- Prefer bullets for evidence, distinctions, and open questions.
- Preserve uncertainty explicitly when sources disagree or remain incomplete.
- Do not hide contradictions; surface them and link the conflicting pages.
