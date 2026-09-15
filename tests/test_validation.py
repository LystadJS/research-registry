from pathlib import Path

from common import ROOT, load_yaml
from validate_manifest import duplicate_id_errors, validate_one
from validate_taxonomy import main as validate_taxonomy_main

FIXTURES = ROOT / "tests" / "fixtures"
PROJECTS = FIXTURES / "projects"


def test_taxonomy_is_self_consistent():
    assert validate_taxonomy_main() == 0


def test_valid_project_passes_schema_and_semantics():
    path = PROJECTS / "project-protecting-aid-workers" / ".research" / "project.yml"
    result = validate_one("project", path)
    assert result["errors"] == []


def test_valid_method_manifest_passes():
    result = validate_one("method", FIXTURES / "clustering.method.yml")
    assert result["errors"] == []


def test_valid_domain_manifest_passes():
    result = validate_one("domain", FIXTURES / "human-security.domain.yml")
    assert result["errors"] == []


def test_unknown_method_is_rejected():
    result = validate_one("project", FIXTURES / "invalid" / "unknown-method.project.yml")
    assert any("unknown method ID" in error for error in result["errors"])


def test_repository_name_contract_is_enforced():
    path = PROJECTS / "project-protecting-aid-workers" / ".research" / "project.yml"
    result = validate_one("project", path, repository_name="LystadJS/wrong-name")
    assert any("project.repository" in error for error in result["errors"])


def test_duplicate_project_ids_are_detected(tmp_path: Path):
    source = PROJECTS / "project-protecting-aid-workers" / ".research" / "project.yml"
    first = tmp_path / "a.project.yml"
    second = tmp_path / "b.project.yml"
    first.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    second.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    results = [validate_one("project", first), validate_one("project", second)]
    duplicate_errors = duplicate_id_errors(results, "project")
    assert len(duplicate_errors) == 1
    assert "protecting-aid-workers" in duplicate_errors[0]


def test_fixture_country_codes_are_registered():
    data = load_yaml(PROJECTS / "project-protecting-aid-workers" / ".research" / "project.yml")
    assert "PS" in data["geography"]["map_countries"]
