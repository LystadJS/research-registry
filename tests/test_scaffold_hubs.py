from pathlib import Path

from scaffold_hubs import scaffold
from validate_manifest import validate_one


def test_scaffold_missing_hubs(tmp_path: Path):
    methods, domains = scaffold(tmp_path, skip_methods=["unsupervised-learning"])

    assert methods == 7
    assert domains == 6
    assert not (tmp_path / "methods" / "method-unsupervised-learning").exists()

    method_manifests = sorted(tmp_path.glob("methods/*/.research/method.yml"))
    domain_manifests = sorted(tmp_path.glob("domains/*/.research/domain.yml"))
    assert len(method_manifests) == 7
    assert len(domain_manifests) == 6

    for manifest in method_manifests:
        result = validate_one("method", manifest)
        assert result["errors"] == []
        readme = manifest.parents[1] / "README.md"
        assert "JSL:AUTO-PROJECTS:START" in readme.read_text(encoding="utf-8")

    for manifest in domain_manifests:
        result = validate_one("domain", manifest)
        assert result["errors"] == []
        readme = manifest.parents[1] / "README.md"
        text = readme.read_text(encoding="utf-8")
        assert "JSL:AUTO-METHODS:START" in text
        assert "JSL:AUTO-PROJECTS:START" in text


def test_scaffold_refuses_unknown_skip(tmp_path: Path):
    try:
        scaffold(tmp_path, skip_methods=["not-a-method"])
    except ValueError as exc:
        assert "Unknown method IDs" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unknown method ID")
