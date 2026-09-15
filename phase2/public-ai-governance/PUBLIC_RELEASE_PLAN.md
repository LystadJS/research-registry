# Sanitized Public AI-Governance Release

**Canonical public repository:** `LystadJS/project-ai-governance-non-proliferation`  
**Private working repository:** `LystadJS/temp` (repository ID `1364709765`; formerly `AI-Governance-and-Non-Proliferation-Task-Force`)  
**Canonical project ID:** `ai-governance-non-proliferation`  
**Publication status:** published and live

## Release principle

The public repository is a releasable reproducibility layer, not a mirror of the private working repository. The private repository remains a separate working environment and was not made public during this step.

## Public contents

The public release contains:

- `.research/project.yml` — canonical public project metadata;
- `README.md` — project scope, methodological summary, and disclosure boundary;
- `analysis/01_pcoa_process_terrain.R` — exact public PCoA coordinate-reproduction workflow;
- `analysis/02_strategic_terrain_figure.R` — sanitized publication-figure workflow;
- `data/README.md` — data boundary and optional-input specification;
- `REPRODUCIBILITY.md` — execution order and expected numerical checks;
- `RIGHTS.md` — conservative reuse statement;
- `CITATION.cff` — repository citation metadata;
- `.gitignore` — generated outputs and local-only inputs; and
- `.github/workflows/validate-public-release.yml` — live manifest and reproducibility validation.

## Sanitization rules

The public layer does not contain:

- private evidence packets or source-body archives;
- internal working notes or negotiation notes;
- private proposal/process panels;
- non-public actor-level evidence files;
- internal decision-support products;
- private intermediate analysis objects;
- credentials, tokens, local paths, or account identifiers.

The private source repository contains the working analytical scripts used to construct this release. The PCoA workflow was carried forward as a bounded public reproduction. The strategic-terrain workflow was normalized for public paths and its caption was restricted to claims reproduced by the public repository itself.

Optional `actor_venue_involvement.csv` support remains documented, but that file is not included in the public repository. Without it, the public plotting workflow uses explicitly coded fallback positions.

## Reproducibility boundary

The public release reproduces the process-terrain PCoA coordinates and the publication-style strategic-terrain visualization from the releasable analytical specification. It does not claim to reproduce the complete private AI-governance research program, source collection, influence analysis, diffusion models, forecasting panel, or internal decision-support workflow.

The public repository CI validates its project manifest, runs the exact PCoA reproduction and numerical assertions, parses the sanitized plotting workflow, and verifies the expected generated PCoA files.

## Registry integration

Completed integration:

1. public discovery resolves `ai-governance-non-proliferation` from the sanitized repository;
2. the private working repository is not portfolio-facing;
3. `method-dimension-reduction` lists the public project;
4. `method-statistical-computing` lists the public project;
5. `domain-emerging-technology` lists the public project;
6. `domain-human-security` lists the public project;
7. the website research card points to the public repository; and
8. the GitHub profile features the public repository under Selected Work.
