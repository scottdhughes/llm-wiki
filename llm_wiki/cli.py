from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from .workspace import (
    build_brief,
    build_status_report,
    compile_inbox,
    create_page,
    heal_workspace,
    ingest_url,
    ingest_source,
    inspect_git_hooks,
    install_git_hooks,
    init_workspace,
    lint_workspace,
    rebuild_index,
    relative_link,
    search_pages,
    uninstall_git_hooks,
    watch_workspace,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Maintain a local agent-written markdown wiki.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create the wiki/raw directory structure.")
    init_parser.add_argument("root", nargs="?", default=".", help="Workspace root. Defaults to the current directory.")

    ingest_parser = subparsers.add_parser("ingest", help="Copy a source into raw/sources and create a source page.")
    ingest_parser.add_argument("source", help="Path to the source file to ingest.")
    ingest_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    ingest_parser.add_argument("--title", help="Override the page title.")
    ingest_parser.add_argument("--summary", help="Optional initial summary for the source page.")
    ingest_parser.add_argument(
        "--kind",
        choices=("auto", "source", "asset"),
        default="auto",
        help="How to classify the ingest. Defaults to auto, which routes images to raw/assets and other files to raw/sources.",
    )

    ingest_url_parser = subparsers.add_parser("ingest-url", help="Fetch a web page and create a source page.")
    ingest_url_parser.add_argument("url", help="HTTP or HTTPS URL to ingest.")
    ingest_url_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    ingest_url_parser.add_argument("--title", help="Override the page title.")
    ingest_url_parser.add_argument("--summary", help="Optional initial summary for the source page.")

    page_parser = subparsers.add_parser("new-page", help="Create a non-source wiki starter page.")
    page_parser.add_argument("title", help="Page title.")
    page_parser.add_argument("--category", required=True, help="Category directory under wiki/, for example analyses or concepts.")
    page_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    page_parser.add_argument("--summary", help="Optional summary paragraph to seed the page.")

    index_parser = subparsers.add_parser("index", help="Rebuild wiki/index.md.")
    index_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")

    compile_parser = subparsers.add_parser("compile", help="Batch-process files from raw/inbox into source pages.")
    compile_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    compile_parser.add_argument("--limit", type=int, help="Optional maximum number of inbox files to process.")

    lint_parser = subparsers.add_parser("lint", help="Check the wiki for structural problems.")
    lint_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")

    heal_parser = subparsers.add_parser("heal", help="Suggest fixes, links, and missing ingests.")
    heal_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")

    search_parser = subparsers.add_parser("search", help="Search the wiki.")
    search_parser.add_argument("query", help="Search query.")
    search_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    search_parser.add_argument("--limit", type=int, default=10, help="Maximum number of results to show.")

    brief_parser = subparsers.add_parser("brief", help="Turn wiki pages into a markdown report.")
    brief_parser.add_argument("query", nargs="?", help="Search query used to choose relevant pages.")
    brief_parser.add_argument("--page", action="append", default=[], help="Explicit wiki page path or title to include. Can be repeated.")
    brief_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    brief_parser.add_argument("--limit", type=int, default=5, help="Maximum number of search hits to include.")
    brief_parser.add_argument("--title", help="Override the report title.")
    brief_parser.add_argument("--output", help="Optional output path for the markdown report.")

    status_parser = subparsers.add_parser("status", help="Summarize corpus health, coverage, and next actions.")
    status_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    status_parser.add_argument("--limit", type=int, default=5, help="Maximum number of gap items or actions to show.")
    status_parser.add_argument("--title", help="Override the status report title.")
    status_parser.add_argument("--output", help="Optional output path for the markdown report.")

    watch_parser = subparsers.add_parser("watch", help="Watch raw/inbox and wiki markdown for changes.")
    watch_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    watch_parser.add_argument("--limit", type=int, default=5, help="Maximum number of gap items or actions in status snapshots.")
    watch_parser.add_argument("--status-output", help="Optional path for a refreshed status markdown file.")
    watch_parser.add_argument("--debounce-ms", type=int, default=1000, help="Debounce interval for filesystem events.")

    hook_parser = subparsers.add_parser("hook", help="Install or inspect managed git hooks.")
    hook_subparsers = hook_parser.add_subparsers(dest="hook_command", required=True)

    hook_install_parser = hook_subparsers.add_parser("install", help="Install managed git hooks.")
    hook_install_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")
    hook_install_parser.add_argument("--status-output", help="Optional path for a refreshed status markdown file.")
    hook_install_parser.add_argument(
        "--force",
        action="store_true",
        help="Back up and replace existing unmanaged hooks that would otherwise conflict.",
    )

    hook_status_parser = hook_subparsers.add_parser("status", help="Show managed git hook status.")
    hook_status_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")

    hook_uninstall_parser = hook_subparsers.add_parser("uninstall", help="Remove managed git hooks.")
    hook_uninstall_parser.add_argument("--root", default=".", help="Workspace root. Defaults to the current directory.")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "init":
        created = init_workspace(Path(args.root))
        print(f"Initialized workspace at {Path(args.root).resolve()}")
        for path in created:
            print(f"- {path}")
        return 0

    if args.command == "ingest":
        result = ingest_source(
            root=Path(args.root),
            source=Path(args.source),
            title=args.title,
            summary=args.summary,
            kind=args.kind,
        )
        root = Path(args.root).resolve()
        print(f"Copied source to {result['raw_source']}")
        print(f"Created wiki page {result['wiki_page']}")
        print(f"Index rebuilt at {root / 'wiki' / 'index.md'}")
        return 0

    if args.command == "ingest-url":
        result = ingest_url(
            root=Path(args.root),
            url=args.url,
            title=args.title,
            summary=args.summary,
        )
        root = Path(args.root).resolve()
        print(f"Ingested URL {result['url']}")
        print(f"Copied source to {result['raw_source']}")
        print(f"Created wiki page {result['wiki_page']}")
        print(f"Index rebuilt at {root / 'wiki' / 'index.md'}")
        return 0

    if args.command == "new-page":
        page_path = create_page(
            root=Path(args.root),
            title=args.title,
            category=args.category,
            summary=args.summary,
        )
        print(f"Created page {page_path}")
        print(f"Index rebuilt at {Path(args.root).resolve() / 'wiki' / 'index.md'}")
        return 0

    if args.command == "index":
        index_path = rebuild_index(Path(args.root))
        print(f"Rebuilt {index_path}")
        return 0

    if args.command == "compile":
        report = compile_inbox(Path(args.root), limit=args.limit)
        if not report.has_items:
            print("No inbox files to compile.")
            return 0
        print(f"Compiled {len(report.items)} inbox files:")
        for item in report.items:
            print(f"- {item.original_path.name} -> {item.raw_source} ({item.kind})")
            print(f"  wiki page: {item.wiki_page}")
        print(f"Index rebuilt at {Path(args.root).resolve() / 'wiki' / 'index.md'}")
        return 0

    if args.command == "lint":
        report = lint_workspace(Path(args.root))
        if report.broken_links:
            print("Broken links:")
            for item in report.broken_links:
                print(f"- {item.source}: {item.target_text} -> {item.resolved}")
        if report.orphan_pages:
            print("Orphan pages:")
            for page in report.orphan_pages:
                print(f"- {page.path}")
        if report.missing_summaries:
            print("Pages missing summary paragraphs:")
            for page in report.missing_summaries:
                print(f"- {page.path}")
        if not report.has_issues:
            print("No structural issues found.")
            return 0
        return 1

    if args.command == "search":
        root = Path(args.root).resolve()
        results = search_pages(root, args.query, limit=args.limit)
        if not results:
            print("No matches.")
            return 0
        for score, page in results:
            print(f"[{score:>3}] {page.title}")
            print(f"      {relative_link(root / 'wiki' / 'index.md', page.path)}")
            print(f"      {page.summary or 'Summary not yet written.'}")
        return 0

    if args.command == "heal":
        report = heal_workspace(Path(args.root))
        if not report.has_suggestions:
            print("No heal suggestions. The workspace looks coherent.")
            return 0
        current_kind = None
        for suggestion in report.suggestions:
            if suggestion.kind != current_kind:
                current_kind = suggestion.kind
                print(f"{current_kind}:")
            print(f"- {suggestion.message}")
        return 0

    if args.command == "brief":
        try:
            report = build_brief(
                root=Path(args.root),
                query=args.query,
                page_refs=args.page,
                limit=args.limit,
                title=args.title,
                output_path=Path(args.output) if args.output else None,
            )
        except ValueError as exc:
            print(str(exc))
            return 1

        if report.output_path:
            print(f"Wrote brief to {report.output_path}")
            print(f"Pages used: {len(report.pages)}")
            return 0

        print(report.content, end="")
        return 0

    if args.command == "status":
        report = build_status_report(
            root=Path(args.root),
            limit=args.limit,
            title=args.title,
            output_path=Path(args.output) if args.output else None,
        )
        if report.output_path:
            print(f"Wrote status report to {report.output_path}")
            return 0
        print(report.content, end="")
        return 0

    if args.command == "watch":
        try:
            watch_workspace(
                root=Path(args.root),
                status_output_path=Path(args.status_output) if args.status_output else None,
                limit=args.limit,
                debounce_ms=max(args.debounce_ms, 50),
            )
        except KeyboardInterrupt:
            print("Stopped watcher.")
            return 0
        return 0

    if args.command == "hook":
        if args.hook_command == "install":
            report = install_git_hooks(
                root=Path(args.root),
                status_output_path=Path(args.status_output) if args.status_output else None,
                force=args.force,
            )
            print(f"Installed managed git hooks in {report.git_dir / 'hooks'}")
            print(f"- Helper: {report.helper_path}")
            print(f"- Metadata: {report.metadata_path}")
            for path in report.hook_paths:
                print(f"- Hook: {path.name}")
            if report.status_output:
                print(f"- Status output: {report.status_output}")
            else:
                print("- Status output: disabled")
            for backup in report.backup_paths:
                print(f"- Backup: {backup}")
            return 0

        if args.hook_command == "status":
            report = inspect_git_hooks(Path(args.root))
            state = "installed" if report.is_installed else "partial" if report.installed_hooks else "not installed"
            print(f"Managed hook state: {state}")
            print(f"- Git dir: {report.git_dir}")
            print(f"- Helper: {'managed' if report.helper_managed else 'missing or unmanaged'}")
            print(f"- Metadata: {'managed' if report.metadata_managed else 'missing or unmanaged'}")
            print(
                "- Installed hooks: "
                + (", ".join(report.installed_hooks) if report.installed_hooks else "none")
            )
            print("- Missing hooks: " + (", ".join(report.missing_hooks) if report.missing_hooks else "none"))
            print(
                "- Unmanaged hook conflicts: "
                + (", ".join(report.unmanaged_hooks) if report.unmanaged_hooks else "none")
            )
            print(f"- Status output: {report.status_output or 'disabled'}")
            if report.backup_paths:
                for backup in report.backup_paths:
                    print(f"- Backup: {backup}")
            return 0 if report.is_installed else 1

        if args.hook_command == "uninstall":
            report = uninstall_git_hooks(Path(args.root))
            if report.removed_paths:
                print(f"Removed managed git hooks from {report.git_dir / 'hooks'}")
                for path in report.removed_paths:
                    print(f"- Removed: {path}")
            else:
                print(f"No managed git hooks found in {report.git_dir / 'hooks'}")
            for path in report.restored_paths:
                print(f"- Restored backup: {path}")
            return 0

    parser.error(f"Unknown command: {args.command}")
    return 2
