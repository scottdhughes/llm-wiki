# Prompt Library

Use these prompts with a local-file-aware coding agent. If your agent prefers `CLAUDE.md`, reference that file instead of `AGENTS.md`.

## Ingest One Source

```text
Read AGENTS.md and CLAUDE.md. Process [FILENAME] from raw/ or raw/inbox/. Read it fully, then create or update the relevant wiki pages, add backlinks, note contradictions, update wiki/index.md, and append to wiki/log.md.
```

## Ingest URL

```text
Read AGENTS.md and CLAUDE.md. Fetch [URL], review the extracted markdown snapshot, then create or update the relevant wiki pages, add backlinks, note contradictions, update wiki/index.md, and append to wiki/log.md.
```

## Compile Inbox

```text
Read AGENTS.md and CLAUDE.md. Process all unprocessed files in raw/inbox/ sequentially. For each file, create or update the relevant source page, connect it to the rest of the wiki, update wiki/index.md, and log the work.
```

## Query

```text
Read wiki/index.md first. Based on the existing wiki, answer: [QUESTION]. Cite the wiki pages or source pages that informed the answer. If the answer reveals a durable new synthesis, file it back into wiki/ or outputs/.
```

## Explore

```text
Read wiki/index.md and identify the 5 most interesting unexplored connections between existing topics. For each, explain the possible insight, the evidence already in the wiki, and what additional source would help confirm it.
```

## Brief

```text
Read wiki/index.md and the most relevant pages. Write a concise markdown brief on [TOPIC] using only wiki knowledge, cite the pages used, and save the result in outputs/[topic]-brief.md.
```

## Status Snapshot

```text
Run `python3 -m llm_wiki status --output outputs/status.md` and review the biggest structural risks, coverage gaps, and next actions before making major changes.
```

## Watch Mode

```text
Start `python3 -m llm_wiki watch --status-output outputs/status.md` while editing the wiki so inbox drops compile automatically, the index stays fresh, and the current workspace status is always available.
```

## Hook Setup

```text
Install managed git hooks with `python3 -m llm_wiki hook install --status-output outputs/status.md` so pre-commit, post-checkout, and post-merge keep derived files current without leaving a watcher running.
```

## Lint

```text
Run a health check on wiki/. Identify broken links, orphan pages, duplicate topics, missing summaries, stale claims, contradictions, and unsupported claims without clear source attribution. Save the findings in outputs/lint-report-[date].md.
```
