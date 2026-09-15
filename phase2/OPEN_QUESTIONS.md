# Phase 2 Decisions and Remaining Questions

## Approved decisions

### Counterterrorism repository scope

The current public repository remains a **broad research workspace** for Islamic State-linked attack patterns, ethnosectarian context, spatial analysis, missingness diagnostics, and related reproducible workflows.

Canonical ID: `islamic-state-ethnosectarian-attack-patterns`.

### UN transcript architecture

The current repository remains intact during migration. The approved long-term target is:

1. a reusable transcript collection / attribution / evidence-extraction engine; and
2. a separate empirical project for dynamic voting alignment and related longitudinal institutional analysis.

No split occurs until the reusable engine has a stable interface and release boundary.

### AI governance visibility

The working repository remains **private**. The eventual public architecture should expose a sanitized project repository or public reproducibility layer containing only releasable analytical artifacts and metadata.

### Repository renames

Manifest deployment is independent of repository renaming. Current repository names remain canonical URLs until coordinated migration occurs.

## Remaining blocking question

### Final package name for `draftmapR`

The repository is `draftmapR`, while the internal development package is currently `driftmapR`. The software repository must not be renamed and its manifest must not be deployed until the final package name is frozen.

## Deferred non-blocking work

### Course standardization

The APSTA repositories are classified as course artifacts. A future `course.yml` schema may standardize them, but they remain outside the research-project graph under v1.0.
