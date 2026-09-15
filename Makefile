.PHONY: test validate dist clean-dist

test:
	pytest

validate:
	python scripts/validate_taxonomy.py
	python scripts/validate_manifest.py --type project --manifest-dir tests/fixtures/projects

dist:
	python scripts/build_web_registry.py --manifest-dir dist/manifests --output-dir dist
	python scripts/build_research_graph.py --manifest-dir dist/manifests --output dist/research-graph.json

clean-dist:
	rm -rf dist/manifests dist/projects.json dist/methods.json dist/domains.json dist/research-registry.json dist/research-graph.json
