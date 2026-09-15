# Phase 2 Discovery Audit

**Architecture:** Research Repository Architecture v1.0  
**Audit date:** 2026-09-15  
**Status:** PASS

## Live metadata checked

| Repository | Entity | Canonical ID | Result |
|---|---|---|---|
| `Unsupervised-Machine-Learning` | method hub | `unsupervised-learning` | PASS |
| `counterterrorism_ethnosectarian_islamic_state` | academic project | `islamic-state-ethnosectarian-attack-patterns` | PASS |
| `UN-Transcript-Intelligence-Dynamic-Voting-Alignment` | technical project | `un-transcript-voting-alignment` | PASS |
| `AI-Governance-and-Non-Proliferation-Task-Force` | applied project (private) | `ai-governance-non-proliferation` | PASS |

`draftmapR` is intentionally excluded until package naming is frozen.

## Validation results

- Controlled vocabularies: **8 methods, 33 techniques, 6 domains, 13 contexts, 249 countries** — PASS.
- Public project manifests: **2 unique project IDs** — PASS.
- All currently deployed project manifests, including the private AI repository: **3 unique project IDs** — PASS.
- Live Unsupervised Learning method manifest — PASS.
- Transitional method-hub URL resolves to `LystadJS/Unsupervised-Machine-Learning` rather than the not-yet-created future rename target.

The UN transcript project produces two expected non-fatal warnings because the public repository is still a project shell: no public output and no software environment are registered yet.

## Candidate graph results

### Public-discovery graph

Projects:

- `islamic-state-ethnosectarian-attack-patterns`
- `un-transcript-voting-alignment`

Generated graph: **64 nodes, 74 edges**.

### All-deployed metadata audit

Adds private working metadata for:

- `ai-governance-non-proliferation`

Generated graph: **101 nodes, 122 edges**.

The private project is intentionally not expected to appear in anonymous/public GitHub discovery.

## Relationship checks

- Counterterrorism project resolves to `spatial-statistics`, `missing-data`, and `statistical-computing`.
- Counterterrorism project resolves to `political-violence`, `terrorism-counterterrorism`, and `human-security`.
- UN transcript project resolves to `statistical-computing`, `network-analysis`, and `longitudinal-multilevel`.
- AI governance resolves to `dimension-reduction` and `statistical-computing`, plus `emerging-technology` and `human-security`.
- The existing Unsupervised Learning repository validates as the live `unsupervised-learning` method hub.

## Acceptance decision

P2-F passes. The architecture is now proven against live repository manifests without repository renames. Missing method and domain hubs may be created after this checkpoint; coordinated renames remain a separate operation.
