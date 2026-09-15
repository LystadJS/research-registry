from pathlib import Path

from build_domain_index import render_methods as render_domain_methods
from build_domain_index import render_projects as render_domain_projects
from build_method_index import render as render_method_projects
from common import ROOT, load_project_records, replace_auto_block
from render_readme import render
from sync_project_readme import render_domains, render_methods
from common import load_yaml

FIXTURES = ROOT / "tests" / "fixtures"
PROJECTS = FIXTURES / "projects"


def test_method_index_lists_projects_and_roles():
    records = load_project_records(PROJECTS)
    text = render_method_projects("clustering", records)
    assert "Protecting Aid Workers" in text
    assert "AI Governance Diffusion" in text
    assert "Primary" in text
    assert "Supporting" in text


def test_domain_index_lists_projects_and_methods():
    records = load_project_records(PROJECTS)
    projects = render_domain_projects("human-security", records)
    methods = render_domain_methods("human-security", records)
    assert "Protecting Aid Workers" in projects
    assert "AI Governance Diffusion" in projects
    assert "Cluster Analysis" in methods
    assert "Network Analysis" in methods


def test_project_auto_links_point_to_hubs():
    manifest = load_yaml(PROJECTS / "project-protecting-aid-workers" / ".research" / "project.yml")
    methods = render_methods(manifest)
    domains = render_domains(manifest)
    assert "https://github.com/LystadJS/method-clustering" in methods
    assert "https://github.com/LystadJS/domain-human-security" in domains


def test_replace_auto_block_preserves_human_text():
    original = "Before\n<!-- JSL:AUTO-PROJECTS:START -->\nold\n<!-- JSL:AUTO-PROJECTS:END -->\nAfter\n"
    updated = replace_auto_block(original, "projects", "new")
    assert updated.startswith("Before")
    assert "new" in updated
    assert updated.endswith("After\n")
    assert "old" not in updated


def test_project_template_renders_required_values():
    manifest = load_yaml(PROJECTS / "project-protecting-aid-workers" / ".research" / "project.yml")
    template = (ROOT / "templates" / "project-readme.md").read_text(encoding="utf-8")
    text = render(template, manifest)
    assert text.startswith("# Protecting Aid Workers")
    assert "Public materials contain only releasable" in text
    assert "JSL:AUTO-METHODS" in text
