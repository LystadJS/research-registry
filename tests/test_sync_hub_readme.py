from pathlib import Path

import yaml

from sync_hub_readme import detect_hub, sync_hub


METHOD_README = """# Cluster Analysis

## Projects Using Cluster Analysis

<!-- JSL:AUTO-PROJECTS:START -->

_placeholder_

<!-- JSL:AUTO-PROJECTS:END -->
"""

DOMAIN_README = """# Human Security

## Methods Used Across This Domain

<!-- JSL:AUTO-METHODS:START -->

_placeholder_

<!-- JSL:AUTO-METHODS:END -->

## Research and Applied Projects

<!-- JSL:AUTO-PROJECTS:START -->

_placeholder_

<!-- JSL:AUTO-PROJECTS:END -->
"""

PROJECT = {
    "schema_version": "1.0",
    "project": {
        "id": "fixture-project",
        "title": "Fixture Project",
        "repository": "LystadJS/fixture-project",
        "type": "academic-research",
        "status": "active",
        "summary": "Fixture project for testing automatic hub synchronization behavior.",
    },
    "methods": [{"id": "clustering", "role": "primary"}],
    "domains": ["human-security"],
    "contexts": [],
    "geography": {"scope": "global", "countries": [], "map_countries": []},
    "access": {
        "repository_visibility": "public",
        "data_access": "none",
        "code_access": "full",
        "disclosure": "Fixture content only for automated synchronization tests.",
    },
}


def write_project(root: Path) -> None:
    path = root / "fixture-project" / ".research" / "project.yml"
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(PROJECT, sort_keys=False), encoding="utf-8")


def test_sync_method_hub(tmp_path: Path):
    hub = tmp_path / "method-clustering"
    (hub / ".research").mkdir(parents=True)
    (hub / ".research" / "method.yml").write_text(
        yaml.safe_dump({"schema_version": "1.0", "method": {"id": "clustering"}}),
        encoding="utf-8",
    )
    (hub / "README.md").write_text(METHOD_README, encoding="utf-8")
    manifests = tmp_path / "projects"
    write_project(manifests)

    assert detect_hub(hub)[0:2] == ("method", "clustering")
    assert sync_hub(hub, manifests) is True
    updated = (hub / "README.md").read_text(encoding="utf-8")
    assert "Fixture Project" in updated
    assert "Primary" in updated
    assert sync_hub(hub, manifests) is False


def test_sync_domain_hub(tmp_path: Path):
    hub = tmp_path / "domain-human-security"
    (hub / ".research").mkdir(parents=True)
    (hub / ".research" / "domain.yml").write_text(
        yaml.safe_dump({"schema_version": "1.0", "domain": {"id": "human-security"}}),
        encoding="utf-8",
    )
    (hub / "README.md").write_text(DOMAIN_README, encoding="utf-8")
    manifests = tmp_path / "projects"
    write_project(manifests)

    assert detect_hub(hub)[0:2] == ("domain", "human-security")
    assert sync_hub(hub, manifests) is True
    updated = (hub / "README.md").read_text(encoding="utf-8")
    assert "Fixture Project" in updated
    assert "Cluster Analysis" in updated
    assert sync_hub(hub, manifests) is False
