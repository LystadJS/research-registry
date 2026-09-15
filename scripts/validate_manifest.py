#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from common import find_manifests, load_yaml, schema, taxonomy


def schema_errors(kind: str, data: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema(kind), format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"schema:{location}: {error.message}")
    return errors


def semantic_project_errors(data: dict[str, Any], repository_name: str | None = None) -> tuple[list[str], list[str]]:
    methods = taxonomy("methods")
    domains = taxonomy("domains")
    contexts = taxonomy("contexts")
    techniques = taxonomy("techniques")
    countries = taxonomy("countries")

    errors: list[str] = []
    warnings: list[str] = []

    project = data.get("project", {})
    if repository_name and project.get("repository") != repository_name:
        errors.append(
            f"semantic:project.repository: expected {repository_name!r}, found {project.get('repository')!r}"
        )

    for idx, method in enumerate(data.get("methods", [])):
        method_id = method.get("id")
        if method_id not in methods:
            errors.append(f"semantic:methods[{idx}].id: unknown method ID {method_id!r}")
            continue
        if not method.get("usage"):
            warnings.append(f"warning:methods[{idx}].usage: no project-specific usage explanation")
        for technique_id in method.get("techniques", []):
            technique = techniques.get(technique_id)
            if technique is None:
                errors.append(f"semantic:methods[{idx}].techniques: unknown technique ID {technique_id!r}")
                continue
            allowed = technique.get("methods", [])
            if method_id not in allowed:
                errors.append(
                    f"semantic:methods[{idx}].techniques: {technique_id!r} is not registered under method {method_id!r}"
                )

    for domain_id in data.get("domains", []):
        if domain_id not in domains:
            errors.append(f"semantic:domains: unknown domain ID {domain_id!r}")

    for context_id in data.get("contexts", []):
        if context_id not in contexts:
            errors.append(f"semantic:contexts: unknown context ID {context_id!r}")

    geography = data.get("geography", {})
    for field in ("countries", "map_countries"):
        for country_code in geography.get(field, []):
            if country_code not in countries:
                errors.append(f"semantic:geography.{field}: unknown country code {country_code!r}")

    if not data.get("outputs"):
        warnings.append("warning:outputs: no public output has been registered")
    if not data.get("software"):
        warnings.append("warning:software: no software environment has been registered")
    return errors, warnings


def semantic_method_errors(data: dict[str, Any], repository_name: str | None = None) -> tuple[list[str], list[str]]:
    methods = taxonomy("methods")
    techniques = taxonomy("techniques")
    errors: list[str] = []
    warnings: list[str] = []
    item = data.get("method", {})
    method_id = item.get("id")
    if method_id not in methods:
        errors.append(f"semantic:method.id: method ID {method_id!r} is not in taxonomy/methods.yml")
    if repository_name and item.get("repository") != repository_name:
        errors.append(f"semantic:method.repository: expected {repository_name!r}, found {item.get('repository')!r}")
    for family in item.get("family", []):
        if family not in methods:
            errors.append(f"semantic:method.family: unknown method ID {family!r}")
    for related in item.get("related_methods", []):
        if related not in methods:
            errors.append(f"semantic:method.related_methods: unknown method ID {related!r}")
        if related == method_id:
            errors.append("semantic:method.related_methods: method cannot relate to itself")
    for technique_id in item.get("techniques", []):
        if technique_id not in techniques:
            errors.append(f"semantic:method.techniques: unknown technique ID {technique_id!r}")
        elif method_id not in techniques[technique_id].get("methods", []):
            errors.append(f"semantic:method.techniques: {technique_id!r} is not registered under {method_id!r}")
    if not item.get("aliases"):
        warnings.append("warning:method.aliases: no aliases defined")
    return errors, warnings


def semantic_domain_errors(data: dict[str, Any], repository_name: str | None = None) -> tuple[list[str], list[str]]:
    domains = taxonomy("domains")
    errors: list[str] = []
    warnings: list[str] = []
    item = data.get("domain", {})
    domain_id = item.get("id")
    if domain_id not in domains:
        errors.append(f"semantic:domain.id: domain ID {domain_id!r} is not in taxonomy/domains.yml")
    if repository_name and item.get("repository") != repository_name:
        errors.append(f"semantic:domain.repository: expected {repository_name!r}, found {item.get('repository')!r}")
    for related in item.get("related_domains", []):
        if related not in domains:
            errors.append(f"semantic:domain.related_domains: unknown domain ID {related!r}")
        if related == domain_id:
            errors.append("semantic:domain.related_domains: domain cannot relate to itself")
    return errors, warnings


def validate_one(kind: str, path: Path, repository_name: str | None = None) -> dict[str, Any]:
    try:
        data = load_yaml(path)
    except Exception as exc:  # noqa: BLE001 - CLI should report malformed YAML cleanly.
        return {"path": str(path), "kind": kind, "errors": [f"yaml:<root>: {exc}"], "warnings": []}

    errors = schema_errors(kind, data)
    warnings: list[str] = []
    if not errors:
        if kind == "project":
            sem_errors, warnings = semantic_project_errors(data, repository_name)
        elif kind == "method":
            sem_errors, warnings = semantic_method_errors(data, repository_name)
        else:
            sem_errors, warnings = semantic_domain_errors(data, repository_name)
        errors.extend(sem_errors)
    return {"path": str(path), "kind": kind, "errors": errors, "warnings": warnings}


def duplicate_id_errors(results: list[dict[str, Any]], kind: str) -> list[str]:
    key = kind
    seen: dict[str, str] = {}
    errors: list[str] = []
    for result in results:
        if result["errors"]:
            continue
        data = load_yaml(result["path"])
        entity_id = data[key]["id"]
        if entity_id in seen:
            errors.append(f"duplicate:{kind}.id: {entity_id!r} appears in {seen[entity_id]} and {result['path']}")
        else:
            seen[entity_id] = result["path"]
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a JSL research manifest against schema and taxonomy.")
    parser.add_argument("--type", dest="kind", choices=("project", "method", "domain"), required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=Path)
    group.add_argument("--manifest-dir", type=Path)
    parser.add_argument("--repository-name", help="Expected owner/repository value for the manifest entity.")
    parser.add_argument("--strict-warnings", action="store_true", help="Treat warnings as validation failures.")
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable JSON report.")
    args = parser.parse_args()

    paths = [args.file] if args.file else find_manifests(args.manifest_dir, args.kind)
    if not paths:
        print("No matching manifests found.", file=sys.stderr)
        return 2

    results = [validate_one(args.kind, Path(path), args.repository_name) for path in paths]
    duplicates = duplicate_id_errors(results, args.kind) if len(results) > 1 else []

    if args.json:
        print(json.dumps({"results": results, "duplicate_errors": duplicates}, indent=2))
    else:
        for result in results:
            state = "PASS" if not result["errors"] else "FAIL"
            print(f"[{state}] {result['path']}")
            for message in result["errors"]:
                print(f"  ERROR: {message}")
            for message in result["warnings"]:
                print(f"  {message}")
        for message in duplicates:
            print(f"ERROR: {message}")

    has_errors = any(result["errors"] for result in results) or bool(duplicates)
    has_warnings = any(result["warnings"] for result in results)
    return 1 if has_errors or (args.strict_warnings and has_warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
