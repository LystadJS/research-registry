import json
import subprocess
import sys
from pathlib import Path

from common import ROOT

FIXTURES = ROOT / "tests" / "fixtures"
PROJECTS = FIXTURES / "projects"


def run_script(name: str, *args: str):
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / name), *args],
        check=True,
        capture_output=True,
        text=True,
    )


def test_web_registry_builder(tmp_path: Path):
    out = tmp_path / "dist"
    run_script("build_web_registry.py", "--manifest-dir", str(PROJECTS), "--output-dir", str(out))
    registry = json.loads((out / "research-registry.json").read_text(encoding="utf-8"))
    assert "clustering" in registry["methods"]
    assert "human-security" in registry["domains"]
    assert "protecting-aid-workers" in registry["projects"]
    assert registry["projects"]["protecting-aid-workers"]["geography"]["map_countries"][0] == "SY"


def test_research_graph_builder(tmp_path: Path):
    output = tmp_path / "research-graph.json"
    run_script("build_research_graph.py", "--manifest-dir", str(PROJECTS), "--output", str(output))
    graph = json.loads(output.read_text(encoding="utf-8"))
    node_ids = {node["id"] for node in graph["nodes"]}
    edge_tuples = {(edge["source"], edge["target"], edge["type"]) for edge in graph["edges"]}
    assert "project:protecting-aid-workers" in node_ids
    assert "method:clustering" in node_ids
    assert "country:PS" in node_ids
    assert ("project:protecting-aid-workers", "method:clustering", "USES_METHOD") in edge_tuples
    assert ("project:protecting-aid-workers", "country:PS", "APPLIES_TO_COUNTRY") in edge_tuples


def test_cli_validation_returns_success_for_valid_fixture():
    path = PROJECTS / "project-protecting-aid-workers" / ".research" / "project.yml"
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_manifest.py"), "--type", "project", "--file", str(path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "[PASS]" in result.stdout


def test_cli_validation_returns_failure_for_invalid_fixture():
    path = FIXTURES / "invalid" / "unknown-method.project.yml"
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_manifest.py"), "--type", "project", "--file", str(path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "unknown method ID" in result.stdout
