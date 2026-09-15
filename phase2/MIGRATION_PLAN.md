# Phase 2 Migration Plan

## Objective

Move the existing GitHub portfolio toward Research Repository Architecture v1.0 without breaking public links, conflating courses with research, or prematurely renaming active software.

## Classification summary

| Current repository | v1.0 role | Canonical ID | Proposed eventual name | Action |
|---|---|---|---|---|
| `AI-Governance-and-Non-Proliferation-Task-Force` | Applied research project | `ai-governance-non-proliferation` | `project-ai-governance-non-proliferation` | Draft manifest first; rename later |
| `APSTA-GE-2012-Causal-Inference` | Course | `apsta-ge-2012-causal-inference` | `course-apsta-ge-2012-causal-inference` | Preserve for now |
| `APSTA-GE-2042-Multilevel-Modeling-Nested-and-Longitudinal-Data` | Course | `apsta-ge-2042-multilevel-modeling` | `course-apsta-ge-2042-multilevel-modeling` | Preserve for now |
| `counterterrorism_ethnosectarian_islamic_state` | Academic research project | `islamic-state-ethnosectarian-attack-patterns` | `project-islamic-state-ethnosectarian-attack-patterns` | Draft manifest first; rename later |
| `draftmapR` | Software / R package | `longitudinal-embedding-alignment` | **deferred** | Freeze package name before rename |
| `LystadJS` | GitHub profile infrastructure | `github-profile` | unchanged | Never rename |
| `LystadJS.github.io` | Portfolio infrastructure | `portfolio-website` | unchanged | Never rename |
| `research-registry` | Registry infrastructure | `research-registry` | unchanged | Already canonical |
| `UN-Transcript-Intelligence-Dynamic-Voting-Alignment` | Technical project | `un-transcript-voting-alignment` | `project-un-transcript-voting-alignment` | Draft manifest first; rename later |
| `Unsupervised-Machine-Learning` | Method hub | `unsupervised-learning` | `method-unsupervised-learning` | Highest-priority hub migration |

## P2-A — Inventory and classification

Completed against all 10 owner repositories exposed by the connected GitHub installation.

### High-confidence classifications

- `Unsupervised-Machine-Learning` is already functioning as a method/reference hub.
- `counterterrorism_ethnosectarian_islamic_state` is an academic research project repository.
- `UN-Transcript-Intelligence-Dynamic-Voting-Alignment` is a technical project shell.
- `draftmapR` is software/package development, not a substantive research project.
- the APSTA repositories are courses, not method hubs or research projects.
- `LystadJS`, `LystadJS.github.io`, and `research-registry` are infrastructure/presentation repositories.

## P2-B — Draft manifests

Schema-valid drafts are stored under `phase2/draft-manifests/`. They use **current repository names**, not proposed rename targets, so they can later be installed without creating a false repository reference.

The drafts are intentionally conservative. For example, the AI-governance manifest records the PCoA/dimension-reduction and visualization work that is actually present in the current repository rather than claiming every method used in the broader research program.

## P2-C — Naming review

Before any rename, resolve these decisions:

1. **Software name:** freeze the final package name for the current `draftmapR` repository. The repository should ultimately use the package name.
2. **Counterterrorism project scope:** confirm whether the current repository should remain a broad Islamic State ethnosectarian attack-patterns workspace or be narrowed to a single publication-specific repository.
3. **UN transcript project scope:** confirm whether transcript collection and dynamic voting alignment remain one project repository or should later split into reusable infrastructure plus an empirical project.
4. **AI governance visibility:** decide whether the current private repository remains private, becomes a releasable public project, or is split into public/private layers.

## P2-D — Non-destructive manifest deployment

After the naming review, add metadata without renaming repositories:

```text
<repository>/.research/project.yml
```

or, for the existing method hub:

```text
Unsupervised-Machine-Learning/.research/method.yml
```

Deployment order:

1. `Unsupervised-Machine-Learning`
2. `counterterrorism_ethnosectarian_islamic_state`
3. `UN-Transcript-Intelligence-Dynamic-Voting-Alignment`
4. `AI-Governance-and-Non-Proliferation-Task-Force`
5. `draftmapR` only after package naming is frozen

Each deployment must pass the registry validator before commit.

## P2-E — Rename and link migration

Repository renames are separate from manifest deployment.

### Rename candidates with known inbound links

The website currently hard-codes links to:

- `Unsupervised-Machine-Learning`
- `counterterrorism_ethnosectarian_islamic_state`
- `UN-Transcript-Intelligence-Dynamic-Voting-Alignment`

The GitHub profile README also links to these repositories. Therefore, their rename operation must be coordinated with updates to the website, profile README, and the current empirical-tag resolver.

Even though GitHub generally redirects an old repository URL after rename, the portfolio should not rely on redirects as its canonical link architecture.

### Rename candidates without discovered public inbound links

- `AI-Governance-and-Non-Proliferation-Task-Force`
- `draftmapR`

The AI repository is private and the package repository is private, reducing immediate public-link risk. They still require scope/name review before rename.

## P2-F — Discovery audit

After manifests are deployed but before mass rename:

1. run `discover_projects.py` against the owner account;
2. verify project IDs are unique;
3. verify the method hub resolves correctly;
4. generate a candidate `research-registry.json` and `research-graph.json`;
5. compare generated project/domain/method relationships against the migration plan;
6. only then begin coordinated renames.

## Repositories intentionally excluded from the project graph

### Course repositories

The two APSTA repositories remain educational/course artifacts. They may be standardized later, but they should not appear as substantive research projects solely because they contain statistical methods.

### Profile and portfolio repositories

`LystadJS` and `LystadJS.github.io` are navigation/presentation layers. Their job is to expose the research graph, not become nodes in it.

### Registry infrastructure

`research-registry` defines the graph; it is not itself a research node.

## Missing hubs

Only one of the eight approved method hubs currently exists in repository form (`Unsupervised-Machine-Learning`). None of the six approved domain hubs currently exist as dedicated repositories.

Their creation should occur only after the first existing repositories are successfully discovered from manifests. This prevents building empty hub repositories before the registry is proven against real projects.
