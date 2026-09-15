# Sanitized Public AI-Governance Release

**Canonical public repository:** `LystadJS/project-ai-governance-non-proliferation`  
**Private working repository:** `LystadJS/AI-Governance-and-Non-Proliferation-Task-Force`  
**Canonical project ID:** `ai-governance-non-proliferation`

## Release principle

The public repository is a releasable reproducibility layer, not a mirror of the private working repository. The private repository remains the working environment and is not made public or renamed during this step.

## Public contents

The initial public release contains:

- `.research/project.yml` — canonical public project metadata;
- `README.md` — project scope, methodological summary, and disclosure boundary;
- `analysis/01_pcoa_process_terrain.R` — exact PCoA coordinate-reproduction workflow derived from the current publication-oriented script;
- `analysis/02_strategic_terrain_figure.R` — sanitized publication-figure workflow;
- `data/README.md` — data boundary and optional-input specification;
- `REPRODUCIBILITY.md` — execution order and expected numerical checks;
- `RIGHTS.md` — conservative reuse statement;
- `CITATION.cff` — repository citation metadata;
- `.gitignore` — generated outputs and local-only inputs.

## Sanitization rules

The public layer MUST NOT contain:

- private evidence packets or source-body archives;
- internal working notes or negotiation notes;
- private proposal/process panels;
- non-public actor-level evidence files;
- internal decision-support products;
- private intermediate analysis objects;
- credentials, tokens, local paths, or account identifiers.

The current private repository contains two R scripts. Both were reviewed for explicit sensitive/internal markers. None were found. The PCoA script is already framed as an exact publication reproduction and uses an embedded process-evidence matrix. It is suitable for the public release without copying the private repository structure.

The strategic-terrain script is suitable after two release-specific changes:

1. public paths are normalized so the PCoA output is consumed from `pcoa_outputs/` and generated figures are written under `figures/`;
2. the figure caption no longer claims reproduction of the separate 3,000-block-bootstrap analysis, because the plotting script does not itself execute that procedure.

Optional `actor_venue_involvement.csv` support may remain documented, but that file is not included in the public repository. Without it, the script uses the explicitly coded fallback positions.

## Reproducibility boundary

The public release reproduces the process-terrain PCoA coordinates and the publication-style strategic-terrain visualization from the releasable analytical specification. It does not claim to reproduce the complete private AI-governance research program, source collection, influence analysis, diffusion models, forecasting panel, or internal decision-support workflow.

## Registry integration

After publication:

1. public discovery should resolve `ai-governance-non-proliferation` from the new repository;
2. the private working manifest should remain private and should no longer be treated as the portfolio-facing project location;
3. `method-dimension-reduction` and `method-statistical-computing` should list the public project;
4. `domain-emerging-technology` and `domain-human-security` should list the public project;
5. website and profile links for the public AI-governance project should point to the sanitized repository, while the private repository remains unlinked.