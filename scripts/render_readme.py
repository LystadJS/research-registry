#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

from common import ROOT, load_yaml

TOKEN = re.compile(r"\{\{\s*([a-zA-Z0-9_.-]+)\s*\}\}")


def resolve(data: dict, dotted: str) -> str:
    value = data
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            raise KeyError(f"Template token {dotted!r} is not present in the manifest")
        value = value[part]
    if isinstance(value, (dict, list)):
        raise TypeError(f"Template token {dotted!r} must resolve to a scalar value")
    return str(value)


def render(template: str, data: dict) -> str:
    return TOKEN.sub(lambda match: resolve(data, match.group(1)), template)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a starter README from a JSL manifest and canonical template.")
    parser.add_argument("--type", dest="kind", choices=("project", "method", "domain"), required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if args.output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {args.output}. Use --force to replace it.")
    template = (ROOT / "templates" / f"{args.kind}-readme.md").read_text(encoding="utf-8")
    data = load_yaml(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(template, data), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
