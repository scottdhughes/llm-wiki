# Knowledge Base Schema

## Identity

This is a persistent markdown knowledge base maintained by an LLM agent. The human curates sources, directs the analysis, and asks questions. The LLM handles ingest, synthesis, linking, maintenance, and report generation.

## Architecture

- `raw/` contains immutable source documents. Never modify files in `raw/` after ingest.
- `wiki/` contains the compiled wiki.
- `outputs/` contains generated reports, analyses, and saved answers.
- `AGENTS.md` and `PROMPTS.md` define the operating rules and reusable prompts.
- Managed git hooks can refresh `wiki/index.md` and `outputs/status.md` during commit, checkout, and merge flows.

## Wiki Conventions

- Use one durable page per topic.
- Generated pages start with YAML frontmatter for `title`, `created`, `last_updated`, `source_count`, and `status`.
- Keep a one-paragraph summary immediately under the `# Title` heading.
- Use normal markdown links for internal references.
- Cite synthesized claims in `[Source: page-or-file]` form.
- Track disagreements under `## Contradictions`.
- Keep `## Related Pages` current.

## Workflows

- Ingest: read local files or fetched web snapshots, summarize them, update or create relevant wiki pages, add backlinks, note contradictions, and log the change.
- Status: generate a concise health snapshot before major synthesis passes so the agent sees coverage gaps, structural issues, and next actions.
- Query: read `wiki/index.md` first, then read relevant pages before answering. Save durable outputs when they are worth keeping.
- Lint: check for broken links, orphan pages, duplicate topics, missing summaries, stale claims, and missing citations.
- Brief: package existing wiki knowledge into a clean markdown artifact in `outputs/`.
- Hook automation: if managed hooks are installed, let them refresh derived files instead of maintaining `wiki/index.md` or `outputs/status.md` by hand.
