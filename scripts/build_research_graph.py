#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from common import dump_json, load_project_records, taxonomy


def add_node(nodes: dict, node_id: str, node_type: str, label: str, **extra) -> None:
    nodes[node_id] = {"id": node_id, "type": node_type, "label": label, **extra}


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a graph representation of the JSL research portfolio.")
    parser.add_argument("--manifest-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    methods = taxonomy("methods")
    techniques = taxonomy("techniques")
    domains = taxonomy("domains")
    contexts = taxonomy("contexts")
    countries = taxonomy("countries")
    projects = load_project_records(args.manifest_dir)

    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    for method_id, meta in methods.items():
        add_node(nodes, f"method:{method_id}", "method", meta["label"])
        for parent in meta.get("parents", []):
            edges.append({"source": f"method:{parent}", "target": f"method:{method_id}", "type": "PARENT_OF"})
    for technique_id, meta in techniques.items():
        add_node(nodes, f"technique:{technique_id}", "technique", meta["label"])
        for method_id in meta.get("methods", []):
            edges.append({"source": f"method:{method_id}", "target": f"technique:{technique_id}", "type": "PARENT_OF"})
    for domain_id, meta in domains.items():
        add_node(nodes, f"domain:{domain_id}", "domain", meta["label"])
    for context_id, meta in contexts.items():
        add_node(nodes, f"context:{context_id}", "context", meta["label"])

    for project in projects:
        pid = f"project:{project['id']}"
        add_node(nodes, pid, "project", project["title"], url=project["url"], status=project["status"])
        for method in project.get("methods", []):
            edges.append({"source": pid, "target": f"method:{method['id']}", "type": "USES_METHOD", "role": method["role"]})
            for technique_id in method.get("techniques", []):
                edges.append({"source": pid, "target": f"technique:{technique_id}", "type": "USES_TECHNIQUE"})
        for domain_id in project.get("domains", []):
            edges.append({"source": pid, "target": f"domain:{domain_id}", "type": "STUDIES_DOMAIN"})
        for context_id in project.get("contexts", []):
            edges.append({"source": pid, "target": f"context:{context_id}", "type": "OCCURS_IN"})
        for country_code in project.get("geography", {}).get("map_countries", []):
            cid = f"country:{country_code}"
            if cid not in nodes:
                add_node(nodes, cid, "country", countries[country_code]["label"], code=country_code)
            edges.append({"source": pid, "target": cid, "type": "APPLIES_TO_COUNTRY"})
        for software in project.get("software", []):
            sid = f"software:{software.lower()}"
            if sid not in nodes:
                add_node(nodes, sid, "software", software)
            edges.append({"source": pid, "target": sid, "type": "USES_SOFTWARE"})

    edge_keys = set()
    deduped = []
    for edge in edges:
        key = tuple(sorted(edge.items()))
        if key not in edge_keys:
            edge_keys.add(key)
            deduped.append(edge)

    dump_json({
        "schema_version": "1.0",
        "nodes": sorted(nodes.values(), key=lambda n: (n["type"], n["label"].casefold())),
        "edges": sorted(deduped, key=lambda e: (e["source"], e["type"], e["target"])),
    }, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
