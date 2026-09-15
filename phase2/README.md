# Phase 2 — Repository Inventory and Migration

**Architecture:** Research Repository Architecture v1.0  
**Mode:** Non-destructive metadata deployment and discovery validation  
**Scope:** Repositories owned by `LystadJS` and visible to the connected GitHub installation.

Phase 2 maps existing repositories into the frozen v1.0 taxonomy, deploys machine-readable metadata without renaming repositories, and verifies that the registry can discover and graph the resulting research entities.

## Rules

1. Canonical IDs are independent of repository names.
2. Current repository names remain authoritative until a coordinated rename occurs.
3. GitHub-special repositories (`LystadJS`, `LystadJS.github.io`) retain their exact names.
4. Software repositories are not renamed until the software/package name is frozen.
5. Renames with inbound links require coordinated website/profile updates even when GitHub redirects old URLs.
6. Course repositories are classified but are not ingested as research projects under schema v1.0.
7. Metadata remains conservative: methods are included only when supported by repository content or explicit project scope.
8. Private working repositories are never made public merely to satisfy registry discovery.

## Current inventory

The connected account exposes **10 owner repositories**. Detailed classifications are in [`inventory.yml`](inventory.yml), and the migration sequence is in [`MIGRATION_PLAN.md`](MIGRATION_PLAN.md).

## Approved Phase 2 decisions

- The counterterrorism repository remains a broad Islamic State / ethnosectarian attack-patterns research workspace rather than being reduced to one publication.
- The UN transcript project remains intact during migration, but the long-term architecture should split the reusable transcript/evidence engine from the empirical voting-alignment project.
- The AI-governance working repository remains private; a sanitized public project layer should be created later for releasable reproducibility artifacts.
- `draftmapR` remains untouched until the final package name is frozen.

## Metadata deployments

The following live repositories now contain registry metadata:

- `Unsupervised-Machine-Learning/.research/method.yml`
- `counterterrorism_ethnosectarian_islamic_state/.research/project.yml`
- `UN-Transcript-Intelligence-Dynamic-Voting-Alignment/.research/project.yml`
- `AI-Governance-and-Non-Proliferation-Task-Force/.research/project.yml`

The `draftmapR` software manifest remains staged only under `phase2/draft-manifests/`.

## Discovery audit

The deployed manifests validate against the v1.0 schemas and controlled vocabularies. The public candidate graph contains the two discoverable public project manifests; the private AI-governance manifest is validated separately and intentionally excluded from public GitHub discovery.

See [`DISCOVERY_AUDIT.md`](DISCOVERY_AUDIT.md) for counts and acceptance criteria.

## Phase 2 checkpoints

- **P2-A:** inventory and classification — complete
- **P2-B:** draft manifests and schema validation — complete
- **P2-C:** naming/architecture review — complete, with package naming explicitly deferred
- **P2-D:** non-destructive manifest deployment — complete for approved repositories; `draftmapR` intentionally deferred
- **P2-E:** coordinated rename and inbound-link migration — pending
- **P2-F:** registry discovery audit — complete

The next implementation boundary is P2-E plus creation of the missing method/domain hubs after the live discovery workflow is confirmed.
