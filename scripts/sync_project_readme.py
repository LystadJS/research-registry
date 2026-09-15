#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from common import load_yaml, replace_auto_block, repo_url, taxonomy


def render_methods(manifest: dict) -> str:
    methods = taxonomy("methods")
    lines = []
    for item in manifest.get("methods", []):
        meta = methods[item["id"]]
        role = item["role"].title()
        usage = f" — {item['usage'].strip()}" if item.get("usage") else ""
        lines.append(f"- **[{meta['label']}]({repo_url(meta['repository'])})** — {role}{usage}")
    return "\n".join(lines) if lines else "_No methodological hubs registered._"


def render_domains(manifest: dict) -> str:
    domains = taxonomy("domains")
    lines = []
    for domain_id in manifest.get("domains", []):
        meta = domains[domain_id]
        lines.append(f"- [{meta['label']}]({repo_url(meta['repository'])})")
    return "\n".join(lines) if lines else "_No domain hubs registered._"


def main() -> int:
    parser = argparse.ArgumentParser(description="Synchronize generated method/domain links in a project README.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--readme", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest = load_yaml(args.manifest)
    original = args.readme.read_text(encoding="utf-8")
    updated = replace_auto_block(original, "methods", render_methods(manifest))
    updated = replace_auto_block(updated, "domains", render_domains(manifest))
    if args.check:
        return 0 if updated == original else 1
    args.readme.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
