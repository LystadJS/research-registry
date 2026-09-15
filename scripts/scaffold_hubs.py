#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import yaml

from common import ROOT, taxonomy
from render_readme import render


def method_techniques(method_id: str) -> list[str]:
    return [
        technique_id
        for technique_id, meta in taxonomy("techniques").items()
        if method_id in meta.get("methods", [])
    ]


def related_methods(method_id: str, methods: dict, techniques: dict) -> list[str]:
    related: set[str] = set(methods[method_id].get("parents", []))
    for candidate_id, meta in methods.items():
        if method_id in meta.get("parents", []):
            related.add(candidate_id)
    for technique in techniques.values():
        owners = set(technique.get("methods", []))
        if method_id in owners:
            related.update(owners - {method_id})
    related.discard(method_id)
    return [candidate_id for candidate_id in methods if candidate_id in related]


def method_manifest(method_id: str, methods: dict, techniques: dict) -> dict:
    meta = methods[method_id]
    aliases = []
    for alias in (meta["label"], method_id.replace("-", " ")):
        if alias not in aliases:
            aliases.append(alias)
    return {
        "schema_version": "1.0",
        "method": {
            "id": method_id,
            "label": meta["label"],
            "repository": meta["repository"],
            "status": "planned",
            "summary": meta["description"],
            "family": list(meta.get("parents", [])),
            "aliases": aliases,
            "techniques": method_techniques(method_id),
            "related_methods": related_methods(method_id, methods, techniques),
            "languages": ["R", "Python"],
        },
    }


def domain_manifest(domain_id: str, domains: dict) -> dict:
    meta = domains[domain_id]
    return {
        "schema_version": "1.0",
        "domain": {
            "id": domain_id,
            "label": meta["label"],
            "repository": meta["repository"],
            "status": "planned",
            "summary": meta["description"],
            "related_domains": [],
        },
    }


def write_yaml(path: Path, data: dict, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite {path}; use --force to replace generated scaffolds")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def write_readme(path: Path, kind: str, manifest: dict, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite {path}; use --force to replace generated scaffolds")
    template = (ROOT / "templates" / f"{kind}-readme.md").read_text(encoding="utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(template, manifest), encoding="utf-8")


def scaffold(output_dir: Path, skip_methods: Iterable[str] = (), force: bool = False) -> tuple[int, int]:
    methods = taxonomy("methods")
    techniques = taxonomy("techniques")
    domains = taxonomy("domains")
    skipped = set(skip_methods)

    unknown = skipped - set(methods)
    if unknown:
        raise ValueError(f"Unknown method IDs supplied to --skip-method: {sorted(unknown)}")

    method_count = 0
    for method_id in methods:
        if method_id in skipped:
            continue
        manifest = method_manifest(method_id, methods, techniques)
        repo_name = manifest["method"]["repository"].split("/", 1)[1]
        repo_dir = output_dir / "methods" / repo_name
        write_yaml(repo_dir / ".research" / "method.yml", manifest, force)
        write_readme(repo_dir / "README.md", "method", manifest, force)
        method_count += 1

    domain_count = 0
    for domain_id in domains:
        manifest = domain_manifest(domain_id, domains)
        repo_name = manifest["domain"]["repository"].split("/", 1)[1]
        repo_dir = output_dir / "domains" / repo_name
        write_yaml(repo_dir / ".research" / "domain.yml", manifest, force)
        write_readme(repo_dir / "README.md", "domain", manifest, force)
        domain_count += 1

    return method_count, domain_count


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate starter method- and domain-hub repositories from the frozen taxonomy.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--skip-method",
        action="append",
        default=[],
        help="Canonical method ID that already has a repository and should not be scaffolded. Repeat as needed.",
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    try:
        method_count, domain_count = scaffold(args.output_dir, args.skip_method, args.force)
    except (FileExistsError, ValueError) as exc:
        parser.error(str(exc))

    print(f"Generated {method_count} method hub(s) and {domain_count} domain hub(s) in {args.output_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
