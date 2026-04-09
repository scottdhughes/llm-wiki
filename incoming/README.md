# Variant Intake

Drop external versions here so we can evaluate and merge the best ideas into this repo.

## Accepted Inputs

- A cloned repo directory (for example `incoming/version-a/`)
- A zip extracted into a directory
- Individual files plus notes about where they came from

## What To Include Per Variant

- Source link (repo URL, gist URL, or file origin)
- Commit hash or date if available
- Short note on what seems better in that variant

## Merge Rubric

We score each candidate on:

- Reliability: testability, error handling, deterministic behavior
- CLI ergonomics: command clarity, safe defaults, useful output
- Wiki quality: page structure, indexing/search quality, linking behavior
- Maintainability: code simplicity, readability, low dependency footprint
- Documentation: setup clarity, command accuracy, workflow guidance

## Process

1. Compare candidate behavior against this repo.
2. Keep only improvements that are clearly better on the rubric.
3. Port changes with tests.
4. Re-run `python3 -m unittest discover -s tests -v`.
5. Re-run `python3 -m llm_wiki lint` and `python3 -m llm_wiki heal`.
