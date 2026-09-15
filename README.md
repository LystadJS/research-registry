# JSL Research Registry

Infrastructure for the **Research Repository Architecture v1.0** used across the John S. Lystad research portfolio.

The registry treats the portfolio as a many-to-many research graph. A substantive project exists once, while methodological and substantive hub repositories index that same project through machine-readable metadata. This avoids duplicate project repositories while allowing one project to appear under several methods, domains, contexts, and empirical settings.

## Phase 1 scope

This repository contains the infrastructure layer only. Phase 1 does **not** rename, migrate, or modify existing research repositories.

Included in v1.0:

- canonical method, technique, domain, context, and country taxonomies;
- JSON Schemas for project, method-hub, and domain-hub manifests;
- schema and semantic validation;
- project discovery for public GitHub repositories;
- project-to-method and project-to-domain README synchronization;
- method- and domain-hub project indexes;
- website registry generation;
- research-graph generation;
- canonical README templates;
- automated self-validation and tests.

## Architectural rule

> **Projects are atomic. Hubs are indexes.**

A project is stored once. Method and domain hubs reference it rather than copying it.

```text
                     METHODS
                   ↙    ↓    ↘
              PROJECT PROJECT PROJECT
                   ↘    ↓    ↙
                     DOMAINS
                        ↓
                EMPIRICAL SETTINGS
```

## Canonical repository classes

| Class | Pattern | Example |
|---|---|---|
| Method hub | `method-<id>` | `method-clustering` |
| Domain hub | `domain-<id>` | `domain-human-security` |
| Research project | `project-<id>` | `project-protecting-aid-workers` |
| Software | Package/project name | package-specific |
| Course | `course-<code>-<id>` | `course-apsta-ge-2042-multilevel-modeling` |
| Infrastructure | Fixed descriptive name | `research-registry` |

Existing repositories are not required to adopt these names until a later migration phase.

## Canonical IDs

Machine-readable IDs use lowercase kebab-case and become immutable once published.

```text
clustering
network-analysis
human-security
political-violence
protecting-aid-workers
```

Display labels may change without changing IDs.

## Registry layout

```text
research-registry/
├── README.md
├── schema/
│   ├── project.schema.json
│   ├── method.schema.json
│   └── domain.schema.json
├── taxonomy/
│   ├── methods.yml
│   ├── techniques.yml
│   ├── domains.yml
│   ├── contexts.yml
│   └── countries.yml
├── scripts/
│   ├── discover_projects.py
│   ├── validate_manifest.py
│   ├── validate_taxonomy.py
│   ├── render_readme.py
│   ├── build_method_index.py
│   ├── build_domain_index.py
│   ├── sync_project_readme.py
│   ├── build_web_registry.py
│   └── build_research_graph.py
├── templates/
│   ├── project-readme.md
│   ├── method-readme.md
│   └── domain-readme.md
├── examples/
├── dist/
└── tests/
```

## Controlled methodological taxonomy

The initial top-level method hubs are:

1. **Unsupervised Learning**
2. **Cluster Analysis**
3. **Dimension Reduction**
4. **Network Analysis**
5. **Missing Data and Measurement**
6. **Longitudinal and Multilevel Statistics**
7. **Spatial and Geographic Statistics**
8. **Statistical Computing and Visualization**

Individual algorithms such as K-means, DBSCAN, HDBSCAN, PCA, UMAP, MICE, and community detection are registered as **techniques**, not top-level repositories.

## Controlled domain taxonomy

The initial substantive domain hubs are:

1. Political Violence
2. Terrorism and Responses to Terrorism
3. Humanitarian Response
4. Human Security
5. Emerging Technology
6. Anthropocene Dynamics and Human Ecology

Military service and independent reporting are treated as empirical **contexts**, not research domains.

## Project manifest

Every project repository will eventually contain:

```text
.research/project.yml
```

See [`examples/project.yml`](examples/project.yml) for the canonical v1.0 example.

The manifest distinguishes substantive geographic scope from map representation:

```yaml
geography:
  scope: multilateral
  countries: []
  map_countries: [SY, MM, PS, IL, RU, UA, LB, IR]
```

`countries` describes country-specific substantive scope. `map_countries` records explicit empirical or analytical coverage for portfolio visualization without converting a multilateral project into separate national studies.

## Validation

Install dependencies:

```bash
pip install -r requirements-dev.txt
```

Validate the controlled vocabularies:

```bash
python scripts/validate_taxonomy.py
```

Validate one project manifest:

```bash
python scripts/validate_manifest.py \
  --type project \
  --file .research/project.yml
```

Validate a collection:

```bash
python scripts/validate_manifest.py \
  --type project \
  --manifest-dir path/to/manifests
```

Validation has two layers:

1. **JSON Schema** — structure, required fields, enums, ID format, and URL syntax.
2. **Semantic validation** — canonical method IDs, technique-method compatibility, domain IDs, context IDs, country codes, repository identity, and duplicate project IDs.

Warnings are used for incomplete but non-invalid metadata such as missing outputs or software declarations. `--strict-warnings` can promote warnings to a non-zero exit status.

## README generation

Create a starter README from a manifest:

```bash
python scripts/render_readme.py \
  --type project \
  --manifest .research/project.yml \
  --output README.md
```

Generated content is restricted to explicit markers such as:

```html
<!-- JSL:AUTO-METHODS:START -->
<!-- JSL:AUTO-METHODS:END -->
```

Human-written text outside these blocks is never overwritten by the synchronization scripts.

## Bidirectional cross-linking

A project manifest can register several methods and domains:

```yaml
methods:
  - id: clustering
    role: primary
  - id: network-analysis
    role: secondary

domains:
  - political-violence
  - human-security
```

This creates four graph relationships without duplicating the project repository:

```text
project → clustering
project → network-analysis
project → political-violence
project → human-security
```

### Method hub → projects

```bash
python scripts/build_method_index.py \
  --method clustering \
  --manifest-dir manifests \
  --readme README.md
```

### Domain hub → projects and methods

```bash
python scripts/build_domain_index.py \
  --domain human-security \
  --manifest-dir manifests \
  --readme README.md
```

### Project → method/domain hubs

```bash
python scripts/sync_project_readme.py \
  --manifest .research/project.yml \
  --readme README.md
```

## Public project discovery

`discover_projects.py` scans public repositories owned by a GitHub account and retrieves `.research/project.yml` where present.

```bash
python scripts/discover_projects.py \
  --owner LystadJS \
  --output-dir dist/manifests
```

An optional `GITHUB_TOKEN` increases API capacity. Phase 1 discovery intentionally targets public repositories; private-repository ingestion can be added later if needed.

## Website registry

Build normalized JSON for downstream website use:

```bash
python scripts/build_web_registry.py \
  --manifest-dir dist/manifests \
  --output-dir dist
```

This creates:

```text
dist/projects.json
dist/methods.json
dist/domains.json
dist/research-registry.json
```

The portfolio website can consume `research-registry.json` so labels such as **Cluster Analysis** resolve to the canonical repository automatically rather than through hard-coded JavaScript mappings.

## Research graph

Build the graph representation:

```bash
python scripts/build_research_graph.py \
  --manifest-dir dist/manifests \
  --output dist/research-graph.json
```

Node classes include:

- project
- method
- technique
- domain
- context
- country
- software

Edge types include:

- `USES_METHOD`
- `USES_TECHNIQUE`
- `STUDIES_DOMAIN`
- `OCCURS_IN`
- `APPLIES_TO_COUNTRY`
- `USES_SOFTWARE`
- `PARENT_OF`

This graph is intended to support a later interactive Research Program Map.

## Tests

Run the complete Phase 1 test suite:

```bash
pytest
```

The test suite verifies schemas, controlled vocabularies, invalid-manifest rejection, repository identity checks, duplicate IDs, README synchronization, hub indexes, website registry generation, and graph construction.

## Phase 1 acceptance contract

Phase 1 is complete when:

- all controlled vocabularies pass self-validation;
- all JSON Schemas parse and validate canonical fixtures;
- invalid semantic references fail validation;
- README generation preserves human-authored sections;
- project-to-hub and hub-to-project links are generated deterministically;
- website registry output is deterministic;
- research graph output is deterministic;
- the automated test suite passes;
- no existing research repository has been modified.

See [`PHASE1_ACCEPTANCE.md`](PHASE1_ACCEPTANCE.md) for the frozen acceptance record.
