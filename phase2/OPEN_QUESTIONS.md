# Phase 2 Open Questions

These decisions should be resolved before Phase 2 performs any rename or deploys metadata into source repositories.

## 1. Final package name for `draftmapR`

The package is currently named `driftmapR` internally while the repository is `draftmapR`. The software repository should ultimately use the final package name. No rename should occur until package naming is frozen.

## 2. Scope of the counterterrorism repository

The current public repository is broader than a single article title: it presents an active analytical workspace for Islamic State-linked attack patterns, ethnosectarian context, spatial analysis, missingness diagnostics, and related workflows.

**Provisional Phase 2 decision:** canonical ID `islamic-state-ethnosectarian-attack-patterns` rather than a publication-only ID such as `target-map`.

## 3. UN transcript architecture

The current public repository combines two related ideas in one shell: transcript intelligence and changing voting alignment.

Possible future structures:

- **single project:** keep collection, evidence extraction, and voting-alignment analysis together;
- **infrastructure + project:** split the reusable transcript collector/evidence engine into software or technical infrastructure, then keep voting alignment as an empirical project.

Phase 2 does not split the repository without an explicit decision.

## 4. AI governance repository visibility

The current repository is private and contains analytical reproduction/visualization code. Before any public migration, determine whether to:

- keep the full repository private and expose registry metadata only;
- publish a sanitized/releasable project repository; or
- separate public reproducibility artifacts from private working materials.

## 5. Course standardization

Course repositories fit the approved repository taxonomy but currently have no dedicated `course.yml` schema. Phase 2 therefore classifies them without forcing them into `project.yml`.
