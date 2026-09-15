from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_DIR = ROOT / "taxonomy"
SCHEMA_DIR = ROOT / "schema"

MANIFEST_FILENAMES = {
    "project": "project.yml",
    "method": "method.yml",
    "domain": "domain.yml",
}

SCHEMA_FILENAMES = {
    "project": "project.schema.json",
    "method": "method.schema.json",
    "domain": "domain.schema.json",
}

AUTO_MARKERS = {
    "projects": ("<!-- JSL:AUTO-PROJECTS:START -->", "<!-- JSL:AUTO-PROJECTS:END -->"),
    "methods": ("<!-- JSL:AUTO-METHODS:START -->", "<!-- JSL:AUTO-METHODS:END -->"),
    "domains": ("<!-- JSL:AUTO-DOMAINS:START -->", "<!-- JSL:AUTO-DOMAINS:END -->"),
}


def load_yaml(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping at the document root")
    return data


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(data: Any, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def taxonomy(name: str) -> dict[str, Any]:
    data = load_yaml(TAXONOMY_DIR / f"{name}.yml")
    return data.get(name, {})


def schema(kind: str) -> dict[str, Any]:
    return load_json(SCHEMA_DIR / SCHEMA_FILENAMES[kind])


def find_manifests(root: str | Path, kind: str = "project") -> list[Path]:
    root = Path(root)
    filename = MANIFEST_FILENAMES[kind]
    if root.is_file():
        return [root] if root.name == filename or root.suffix in {".yml", ".yaml"} else []
    if not root.exists():
        return []
    paths = set(root.rglob(filename))
    # Permit flat fixture collections named *.project.yml, *.method.yml, etc.
    paths.update(root.rglob(f"*.{kind}.yml"))
    paths.update(root.rglob(f"*.{kind}.yaml"))
    return sorted(paths)


def repo_url(repository: str) -> str:
    return f"https://github.com/{repository}"


def replace_auto_block(text: str, block: str, body: str) -> str:
    start, end = AUTO_MARKERS[block]
    if start not in text or end not in text:
        raise ValueError(f"README is missing {block!r} auto-generation markers")
    if text.index(start) > text.index(end):
        raise ValueError(f"README has reversed {block!r} markers")
    replacement = f"{start}\n\n{body.rstrip()}\n\n{end}"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(replacement, text, count=1)


def normalized_project_record(manifest: dict[str, Any]) -> dict[str, Any]:
    project = manifest["project"]
    geography = manifest.get("geography", {})
    return {
        "id": project["id"],
        "title": project["title"],
        "short_title": project.get("short_title", project["title"]),
        "repository": project["repository"],
        "url": repo_url(project["repository"]),
        "type": project["type"],
        "status": project["status"],
        "featured": bool(project.get("featured", False)),
        "summary": project["summary"],
        "methods": manifest.get("methods", []),
        "domains": manifest.get("domains", []),
        "contexts": manifest.get("contexts", []),
        "geography": geography,
        "software": manifest.get("software", []),
        "keywords": manifest.get("keywords", []),
        "outputs": manifest.get("outputs", []),
        "access": manifest.get("access", {}),
    }


def load_project_records(manifest_root: str | Path) -> list[dict[str, Any]]:
    records = []
    for path in find_manifests(manifest_root, "project"):
        data = load_yaml(path)
        if "project" in data:
            records.append(normalized_project_record(data))
    return sorted(records, key=lambda item: (not item.get("featured", False), item["title"].lower()))


def method_label(method_id: str) -> str:
    return taxonomy("methods").get(method_id, {}).get("label", method_id)


def domain_label(domain_id: str) -> str:
    return taxonomy("domains").get(domain_id, {}).get("label", domain_id)


def sort_unique(values: Iterable[str]) -> list[str]:
    return sorted(set(values), key=str.casefold)
