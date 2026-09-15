# AI Governance and Non-Proliferation

Public reproducibility materials for statistical analysis of **AI-governance institutional terrain** across the United Nations and wider multilateral ecosystem.

This repository is intentionally narrower than the underlying working project. It publishes only releasable analytical code and documentation needed to reconstruct the process-terrain embedding and its publication-style visualization. Private working materials remain separate.

## Research scope

AI governance does not develop in one institution. Governance proposals, technical standards, ethics frameworks, development processes, and political coalitions move through overlapping venues with different procedural architectures and different evidence environments.

The public workflow represents those institutional processes as structured observations and asks a limited statistical question:

> How similar are multilateral AI-governance processes when compared on the kinds of public process evidence they make available?

The analysis does **not** interpret geometric proximity as political alignment, influence, preference similarity, or causal effect.

## Public analytical workflow

```text
19 public-process evidence features
            ↓
five equal-weight conceptual blocks
            ↓
structural mixed-data Gower distance
            ↓
Lingoes correction for non-Euclidean distance
            ↓
principal coordinates analysis (PCoA)
            ↓
deterministic orientation + numerical validation
            ↓
strategic-terrain visualization
```

The PCoA reproduction script contains the releasable feature matrix directly, making the core embedding reproducible without a private data dependency.

## Reproduced numerical baseline

The coordinate-generation workflow validates against the following expected diagnostics:

- PCoA 1: **39.8046%** of corrected positive inertia;
- PCoA 2: **27.0937%**;
- first two dimensions combined: **66.8983%**;
- Lingoes constant: **0.0107432366**.

Small platform-level floating-point differences are allowed by the script's validation tolerances.

## Repository structure

```text
README.md
.research/project.yml
analysis/
  01_pcoa_process_terrain.R
  02_strategic_terrain_figure.R
data/
  README.md
figures/
pcoa_outputs/
REPRODUCIBILITY.md
RIGHTS.md
CITATION.cff
```

Generated outputs under `figures/` and `pcoa_outputs/` are reproducible artifacts rather than source inputs.

## What is not included

This public repository is **not a mirror of the private working repository**. It does not publish private source archives, evidence packets, working proposal/process panels, internal notes, private actor-level evidence files, intermediate analytical objects, or decision-support products.

It also does not claim to reproduce every model used in the broader AI-governance research program. The initial release is limited to the process-terrain PCoA and associated visualization.

## Methods

### Structural mixed-data distance

The process-evidence matrix uses values of `0`, `0.5`, `1`, and structurally meaningful `NA` values. Pairwise distance treats:

- observed versus observed as absolute difference;
- `NA` versus `NA` as zero structural difference;
- `NA` versus observed as maximum structural difference.

Feature weights are normalized within five conceptual blocks so blocks contribute equal total weight despite containing different numbers of variables.

### Principal coordinates analysis

Classical PCoA is applied to the resulting distance matrix. A Lingoes correction is used when negative raw eigenvalues indicate non-Euclidean structure. Axis signs are then oriented deterministically for stable reproduction.

### Visualization

The strategic-terrain figure combines the statistical embedding with clearly labeled contextual elements. Functional halos and contextual perimeter nodes are descriptive visual structures and should not be interpreted as estimated clusters unless separately supported by an explicit statistical procedure.

## Reproducibility

See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) for execution order and dependencies.

## Data and disclosure

See [`data/README.md`](data/README.md) for the public-data boundary. No private working dataset is required for the core PCoA reproduction.

## Related research architecture

- [Dimension Reduction](https://github.com/LystadJS/method-dimension-reduction)
- [Statistical Computing and Visualization](https://github.com/LystadJS/method-statistical-computing)
- [Emerging Technology](https://github.com/LystadJS/domain-emerging-technology)
- [Human Security](https://github.com/LystadJS/domain-human-security)
- [Research Registry](https://github.com/LystadJS/research-registry)

## Citation and reuse

Use `CITATION.cff` for repository citation metadata. See `RIGHTS.md` before reusing analytical content or adapting the release.