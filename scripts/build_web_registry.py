#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from common import dump_json, load_project_records, repo_url, taxonomy


def normalized_hubs(kind: str) -> dict:
    hubs = {}
    for hub_id, meta in taxonomy(kind).items():
        hubs[hub_id] = {
            "id": hub_id,
            "label": meta["label"],
            "repository": meta.get("repository"),
            "url": repo_url(meta["repository"]) if meta.get("repository") else None,
            "description": meta.get("description"),
            "parents": meta.get("parents", []),
        }
    return hubs


def main() -> int:
    parser = argparse.ArgumentParser(description="Build normalized JSON registry files for the website and hub automation.")
    parser.add_argument("--manifest-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    projects = load_project_records(args.manifest_dir)
    methods = normalized_hubs("methods")
    domains = normalized_hubs("domains")
    contexts = taxonomy("contexts")
    techniques = taxonomy("techniques")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    dump_json(projects, args.output_dir / "projects.json")
    dump_json(methods, args.output_dir / "methods.json")
    dump_json(domains, args.output_dir / "domains.json")
    dump_json({
        "schema_version": "1.0",
        "methods": methods,
        "domains": domains,
        "contexts": contexts,
        "techniques": techniques,
        "projects": {project["id"]: project for project in projects},
    }, args.output_dir / "research-registry.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
