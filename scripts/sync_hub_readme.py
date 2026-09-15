#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from build_domain_index import render_methods as render_domain_methods
from build_domain_index import render_projects as render_domain_projects
from build_method_index import render as render_method_projects
from common import load_project_records, load_yaml, replace_auto_block, taxonomy


def detect_hub(hub_root: Path) -> tuple[str, str, Path]:
    method_manifest = hub_root / ".research" / "method.yml"
    domain_manifest = hub_root / ".research" / "domain.yml"

    present = [path for path in (method_manifest, domain_manifest) if path.exists()]
    if len(present) != 1:
        raise ValueError(
            "Hub repository must contain exactly one of .research/method.yml or .research/domain.yml"
        )

    manifest_path = present[0]
    kind = "method" if manifest_path == method_manifest else "domain"
    manifest = load_yaml(manifest_path)
    hub = manifest.get(kind, {})
    hub_id = hub.get("id")
    if not hub_id:
        raise ValueError(f"{manifest_path} does not define {kind}.id")

    vocab = taxonomy(f"{kind}s")
    if hub_id not in vocab:
        raise ValueError(f"Unknown {kind} ID: {hub_id}")

    return kind, hub_id, manifest_path


def sync_hub(hub_root: Path, manifest_dir: Path, check: bool = False) -> bool:
    kind, hub_id, _ = detect_hub(hub_root)
    readme = hub_root / "README.md"
    if not readme.exists():
        raise ValueError(f"Hub repository is missing {readme}")

    projects = load_project_records(manifest_dir)
    original = readme.read_text(encoding="utf-8")

    if kind == "method":
        updated = replace_auto_block(
            original,
            "projects",
            render_method_projects(hub_id, projects),
        )
    else:
        updated = replace_auto_block(
            original,
            "methods",
            render_domain_methods(hub_id, projects),
        )
        updated = replace_auto_block(
            updated,
            "projects",
            render_domain_projects(hub_id, projects),
        )

    changed = updated != original
    if check:
        return changed
    if changed:
        readme.write_text(updated, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Auto-detect a method/domain hub and synchronize its generated README indexes."
    )
    parser.add_argument("--hub-root", type=Path, default=Path("."))
    parser.add_argument("--manifest-dir", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        kind, hub_id, _ = detect_hub(args.hub_root)
        changed = sync_hub(args.hub_root, args.manifest_dir, check=args.check)
    except ValueError as exc:
        parser.error(str(exc))

    state = "changes required" if changed else "already synchronized"
    print(f"{kind} hub {hub_id}: {state}")
    if args.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
