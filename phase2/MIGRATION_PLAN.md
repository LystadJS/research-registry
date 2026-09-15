# Phase 2 Migration Plan

## Objective

Move the existing GitHub portfolio toward Research Repository Architecture v1.0 without breaking public links, conflating courses with research, exposing private working material, or prematurely renaming active software.

## Classification summary

| Current repository | v1.0 role | Canonical ID | Proposed eventual name | Current action |
|---|---|---|---|---|
| `AI-Governance-and-Non-Proliferation-Task-Force` | Applied research project | `ai-governance-non-proliferation` | `project-ai-governance-non-proliferation` | Manifest deployed; remain private; public layer later |
| `APSTA-GE-2012-Causal-Inference` | Course | `apsta-ge-2012-causal-inference` | `course-apsta-ge-2012-causal-inference` | Preserve for now |
| `APSTA-GE-2042-Multilevel-Modeling-Nested-and-Longitudinal-Data` | Course | `apsta-ge-2042-multilevel-modeling` | `course-apsta-ge-2042-multilevel-modeling` | Preserve for now |
| `counterterrorism_ethnosectarian_islamic_state` | Academic research project | `islamic-state-ethnosectarian-attack-patterns` | `project-islamic-state-ethnosectarian-attack-patterns` | Manifest deployed; broad workspace approved |
| `draftmapR` | Software / R package | `longitudinal-embedding-alignment` | **deferred** | Leave untouched until package name freezes |
| `LystadJS` | GitHub profile infrastructure | `github-profile` | unchanged | Never rename |
| `LystadJS.github.io` | Portfolio infrastructure | `portfolio-website` | unchanged | Never rename |
| `research-registry` | Registry infrastructure | `research-registry` | unchanged | Already canonical |
| `UN-Transcript-Intelligence-Dynamic-Voting-Alignment` | Technical project | `un-transcript-voting-alignment` | `project-un-transcript-voting-alignment` | Manifest deployed; split reusable engine later |
| `Unsupervised-Machine-Learning` | Method hub | `unsupervised-learning` | `method-unsupervised-learning` | Manifest deployed; live transitional hub |

## P2-A — Inventory and classification

**Complete.** All 10 owner repositories exposed by the connected GitHub installation are classified.

## P2-B — Draft manifests

**Complete.** Schema-valid drafts remain under `phase2/draft-manifests/` as migration records.

## P2-C — Naming and architecture review

**Complete with one explicit deferral.** Approved decisions:

1. `draftmapR`: no rename or source-manifest deployment until the final package name is frozen.
2. Counterterrorism: retain the broad Islamic State / ethnosectarian attack-patterns research workspace.
3. UN transcript: retain the current combined repository during migration, then eventually split reusable transcript/evidence infrastructure from the voting-alignment empirical project.
4. AI governance: retain the private working repository and later create a sanitized public project/reproducibility layer.

## P2-D — Non-destructive manifest deployment

**Complete for approved repositories.** Metadata was added without renaming or restructuring repositories:

```text
Unsupervised-Machine-Learning/.research/method.yml
counterterrorism_ethnosectarian_islamic_state/.research/project.yml
UN-Transcript-Intelligence-Dynamic-Voting-Alignment/.research/project.yml
AI-Governance-and-Non-Proliferation-Task-Force/.research/project.yml
```

`draftmapR` remains intentionally untouched.

## P2-E — Rename and link migration

**Pending.** Repository renames remain separate from metadata deployment.

### Known coordinated-link repositories

The website and/or profile currently hard-code links to:

- `Unsupervised-Machine-Learning`
- `counterterrorism_ethnosectarian_islamic_state`
- `UN-Transcript-Intelligence-Dynamic-Voting-Alignment`

Any rename must update the portfolio website, GitHub profile README, and empirical-tag resolver in the same migration window. GitHub redirects are a safety net, not the canonical architecture.

### AI governance

The private working repository should not simply be made public. A sanitized public project layer should be created first; its eventual canonical name can then be used for public graph discovery.

### Software

`draftmapR` remains excluded from P2-E until package naming is frozen.

## P2-F — Discovery audit

**Complete.** See [`DISCOVERY_AUDIT.md`](DISCOVERY_AUDIT.md).

Acceptance results:

- public project IDs are unique;
- all deployed project IDs are unique;
- the existing method hub validates and now resolves through its current live repository URL;
- candidate public and all-deployed research graphs build successfully;
- expected project/domain/method relationships match the migration plan.

## Repositories intentionally excluded from the project graph

### Course repositories

The APSTA repositories remain educational/course artifacts and should not appear as substantive research projects solely because they contain statistical methods.

### Profile and portfolio repositories

`LystadJS` and `LystadJS.github.io` remain navigation/presentation layers rather than research graph nodes.

### Registry infrastructure

`research-registry` defines the graph; it is not itself a research node.

## Missing hubs

The existing `Unsupervised-Machine-Learning` repository is now the validated transitional `unsupervised-learning` hub. The other seven approved method hubs and all six domain hubs do not yet exist as repositories.

P2-F has now satisfied the prerequisite for creating those hubs. Hub creation may proceed before or independently of repository renaming because canonical IDs do not depend on repository names.
