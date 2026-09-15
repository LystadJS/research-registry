#!/usr/bin/env python3
from __future__ import annotations

import re
import sys

from common import taxonomy

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REPO = re.compile(r"^LystadJS/[A-Za-z0-9._-]+$")
COUNTRY = re.compile(r"^[A-Z]{2}$")


def main() -> int:
    errors: list[str] = []
    methods = taxonomy("methods")
    techniques = taxonomy("techniques")
    domains = taxonomy("domains")
    contexts = taxonomy("contexts")
    countries = taxonomy("countries")

    for method_id, meta in methods.items():
        if not SLUG.fullmatch(method_id):
            errors.append(f"methods:{method_id}: invalid canonical ID")
        if not meta.get("label"):
            errors.append(f"methods:{method_id}: missing label")
        if not REPO.fullmatch(meta.get("repository", "")):
            errors.append(f"methods:{method_id}: invalid repository")
        for parent in meta.get("parents", []):
            if parent not in methods:
                errors.append(f"methods:{method_id}: unknown parent {parent!r}")
            if parent == method_id:
                errors.append(f"methods:{method_id}: method cannot be its own parent")

    def visit(node: str, stack: tuple[str, ...]) -> None:
        if node in stack:
            errors.append(f"methods:{node}: parent cycle detected: {' -> '.join((*stack, node))}")
            return
        for parent in methods[node].get("parents", []):
            if parent in methods:
                visit(parent, (*stack, node))

    for method_id in methods:
        visit(method_id, ())

    for technique_id, meta in techniques.items():
        if not SLUG.fullmatch(technique_id):
            errors.append(f"techniques:{technique_id}: invalid canonical ID")
        if not meta.get("label"):
            errors.append(f"techniques:{technique_id}: missing label")
        owners = meta.get("methods", [])
        if not owners:
            errors.append(f"techniques:{technique_id}: no parent method")
        for method_id in owners:
            if method_id not in methods:
                errors.append(f"techniques:{technique_id}: unknown method {method_id!r}")

    for domain_id, meta in domains.items():
        if not SLUG.fullmatch(domain_id):
            errors.append(f"domains:{domain_id}: invalid canonical ID")
        if not meta.get("label"):
            errors.append(f"domains:{domain_id}: missing label")
        if not REPO.fullmatch(meta.get("repository", "")):
            errors.append(f"domains:{domain_id}: invalid repository")

    for context_id, meta in contexts.items():
        if not SLUG.fullmatch(context_id):
            errors.append(f"contexts:{context_id}: invalid canonical ID")
        if not meta.get("label"):
            errors.append(f"contexts:{context_id}: missing label")

    for code, meta in countries.items():
        if not COUNTRY.fullmatch(code):
            errors.append(f"countries:{code}: invalid country code")
        if not meta.get("label"):
            errors.append(f"countries:{code}: missing label")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"PASS: {len(methods)} methods, {len(techniques)} techniques, {len(domains)} domains, "
        f"{len(contexts)} contexts, {len(countries)} countries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
