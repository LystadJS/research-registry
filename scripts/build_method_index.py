#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from common import domain_label, load_project_records, replace_auto_block, taxonomy


def render(method_id: str, projects: list[dict]) -> str:
    rows = []
    for project in projects:
        matches = [item for item in project.get("methods", []) if item.get("id") == method_id]
        if not matches:
            continue
        role = matches[0].get("role", "")
        domains = ", ".join(domain_label(item) for item in project.get("domains", [])) or "—"
        rows.append(f"| [{project['title']}]({project['url']}) | {domains} | {role.title()} |")
    if not rows:
        return "_No registered projects currently use this method._"
    return "\n".join([
        "| Project | Domain | Method role |",
        "|---|---|---|",
        *rows,
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description="Update a method hub README project index.")
    parser.add_argument("--method", required=True)
    parser.add_argument("--manifest-dir", type=Path, required=True)
    parser.add_argument("--readme", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.method not in taxonomy("methods"):
        raise SystemExit(f"Unknown method ID: {args.method}")
    projects = load_project_records(args.manifest_dir)
    original = args.readme.read_text(encoding="utf-8")
    updated = replace_auto_block(original, "projects", render(args.method, projects))
    if args.check:
        return 0 if updated == original else 1
    args.readme.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
