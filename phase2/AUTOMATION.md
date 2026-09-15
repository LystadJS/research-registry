# Automatic Research Graph Synchronization

Phase 2 synchronization treats project manifests and the frozen taxonomy as the source of truth. Generated indexes and website repository destinations are derived from those sources rather than maintained independently.

## Source-of-truth hierarchy

1. Public project repositories expose `.research/project.yml`.
2. `research-registry/taxonomy/` defines canonical method, domain, technique, and context IDs.
3. `research-registry/dist/` is generated from the current public project manifests plus the taxonomy.
4. Method/domain hub README auto-blocks are generated from current public project manifests.
5. The portfolio resolves canonical IDs against the live generated registry.

Private repositories are not pulled into the public registry by discovery.

## Central registry synchronization

Workflow: `.github/workflows/sync-public-registry.yml`

Triggers:

- every four hours at minute 17;
- manual `workflow_dispatch`;
- pushes that change registry scripts, schemas, taxonomies, or the synchronization workflow.

Each run:

1. discovers public `LystadJS` repositories containing `.research/project.yml`;
2. validates every discovered project manifest;
3. rebuilds `dist/projects.json`, `dist/methods.json`, `dist/domains.json`, and `dist/research-registry.json`;
4. rebuilds `dist/research-graph.json`; and
5. commits only when generated content changed.

Generated-file commits do not retrigger the workflow because `dist/**` is intentionally excluded from its push-path trigger.

## Hub synchronization

Reusable workflow: `.github/workflows/reusable-sync-hub.yml`

Caller workflow: `.github/workflows/sync-research-hub.yml` in each live method/domain hub.

Coverage: all eight method hubs and all six domain hubs.

Triggers:

- daily at 08:37 UTC;
- manual `workflow_dispatch`;
- changes to the hub's own `.research/**` manifest or synchronization caller.

Each hub run:

1. checks out the hub and `research-registry`;
2. discovers the current public project manifests;
3. validates those project manifests;
4. validates the hub manifest against the canonical taxonomy and current repository name;
5. auto-detects whether the caller is a method or domain hub;
6. regenerates only the protected `JSL:AUTO-*` README blocks; and
7. commits `README.md` only when the generated index changed.

Human-authored README content outside the auto-generation markers is never rewritten by the synchronization script.

## Website synchronization

The portfolio does not maintain a second copy of repository URLs.

`assets/js/empirical-tag-links.js` loads:

```text
https://raw.githubusercontent.com/LystadJS/research-registry/main/dist/research-registry.json
```

once per page load and stores the resulting promise in `window.JSLResearchRegistry`. `assets/js/research-tag-links.js` reuses the same registry object.

Labels are mapped to canonical method/domain/project IDs; the current repository URL is then read from the generated registry. A later repository rename therefore requires changing the canonical registry/manifests, not editing every website tag.

If the live registry cannot be retrieved, external tag links fall back to the public `LystadJS` repository index rather than using stale hard-coded repository URLs. Local portfolio links continue to work normally.

## Current deferred work

Automatic synchronization does **not** change the scope of unfinished or intentionally deferred software:

- the UN transcript/voting repository remains intact; the reusable transcript-engine split is deferred until the software is mature;
- `draftmapR` remains untouched until package naming is revisited.

Both deferrals are architectural decisions, not synchronization failures.

## Acceptance state

The automation has been live-tested against:

- central public registry discovery, validation, registry generation, and graph generation;
- a populated method hub (`method-dimension-reduction`);
- a populated domain hub (`domain-human-security`);
- an empty method hub (`method-clustering`); and
- the GitHub Pages deployment containing the live-registry website resolver.

All representative runs completed successfully before this automation layer was marked operational.
