# Phase 2 — Repository Inventory and Migration Design

**Architecture:** Research Repository Architecture v1.0  
**Mode:** Non-destructive planning  
**Scope:** Repositories currently owned by `LystadJS` and visible to the connected GitHub installation.

Phase 2 maps existing repositories into the frozen v1.0 taxonomy before any repository is renamed or any research repository receives registry metadata.

## Rules

1. No existing project, course, software, profile, or website repository is modified during the inventory pass.
2. Draft manifests live only in `research-registry/phase2/` until explicitly approved for deployment.
3. Current repository names remain authoritative until a coordinated rename occurs.
4. GitHub-special repositories (`LystadJS`, `LystadJS.github.io`) retain their exact names.
5. Software repositories are not renamed until the software/package name is frozen.
6. Renames with inbound links require a coordinated link-update pass even when GitHub redirects old repository URLs.
7. Course repositories are classified but are not ingested as research projects under schema v1.0.
8. Provisional metadata is conservative: methods are included only when supported by current repository content or explicit project scope.

## Current inventory

The connected GitHub account currently exposes **10 owner repositories**. The detailed classification is in [`inventory.yml`](inventory.yml); the migration sequence and rename policy are in [`MIGRATION_PLAN.md`](MIGRATION_PLAN.md).

## Draft manifests

Schema-valid draft manifests have been prepared for the repositories that already map cleanly to v1.0 entities:

- `AI-Governance-and-Non-Proliferation-Task-Force` → applied-research project
- `counterterrorism_ethnosectarian_islamic_state` → academic-research project
- `UN-Transcript-Intelligence-Dynamic-Voting-Alignment` → technical project
- `draftmapR` → software project
- `Unsupervised-Machine-Learning` → method hub

These drafts are **not yet installed into the source repositories**.

## Phase 2 checkpoints

- **P2-A:** inventory and classification — complete
- **P2-B:** draft manifests and schema validation — complete
- **P2-C:** naming/rename review — pending
- **P2-D:** non-destructive manifest deployment to approved repositories — pending
- **P2-E:** coordinated rename and inbound-link migration — pending
- **P2-F:** registry discovery audit — pending
