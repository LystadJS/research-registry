#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from common import load_project_records, method_label, replace_auto_block, repo_url, taxonomy


def matching_projects(domain_id: str, projects: list[dict]) -> list[dict]:
    return [project for project in projects if domain_id in project.get("domains", [])]


def render_projects(domain_id: str, projects: list[dict]) -> str:
    rows = []
    for project in matching_projects(domain_id, projects):
        methods = ", ".join(method_label(item["id"]) for item in project.get("methods", [])) or "—"
        rows.append(f"| [{project['title']}]({project['url']}) | {methods} | {project['status'].title()} |")
    if not rows:
        return "_No registered projects currently belong to this domain._"
    return "\n".join([
        "| Project | Methods | Status |",
        "|---|---|---|",
        *rows,
    ])


def render_methods(domain_id: str, projects: list[dict]) -> str:
    methods = taxonomy("methods")
    counts = Counter(
        item["id"]
        for project in matching_projects(domain_id, projects)
        for item in project.get("methods", [])
    )
    if not counts:
        return "_No methodological hubs are currently represented in this domain._"
    rows = []
    for method_id, count in sorted(counts.items(), key=lambda pair: (-pair[1], methods[pair[0]]["label"].casefold())):
        meta = methods[method_id]
        rows.append(f"- [{meta['label']}]({repo_url(meta['repository'])}) — {count} registered project{'s' if count != 1 else ''}")
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Update a domain hub README project and method indexes.")
    parser.add_argument("--domain", required=True)
    parser.add_argument("--manifest-dir", type=Path, required=True)
    parser.add_argument("--readme", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.domain not in taxonomy("domains"):
        raise SystemExit(f"Unknown domain ID: {args.domain}")
    projects = load_project_records(args.manifest_dir)
    original = args.readme.read_text(encoding="utf-8")
    updated = replace_auto_block(original, "methods", render_methods(args.domain, projects))
    updated = replace_auto_block(updated, "projects", render_projects(args.domain, projects))
    if args.check:
        return 0 if updated == original else 1
    args.readme.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
