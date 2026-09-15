# Phase 2 — Repository Inventory and Migration

**Architecture:** Research Repository Architecture v1.0  
**Mode:** Non-destructive metadata deployment, hub bootstrap, public-project release, link integration, and automatic synchronization  
**Scope:** Repositories owned by `LystadJS` and visible to the connected GitHub installation.

Phase 2 maps existing repositories into the frozen v1.0 taxonomy, deploys machine-readable metadata without forcing renames, validates live discovery, creates the approved method/domain hubs, publishes a sanitized AI-governance reproducibility layer, connects the public portfolio to the resulting graph, and automatically synchronizes generated registry and hub indexes.

## Rules

1. Canonical IDs are independent of repository names.
2. Current project repository names remain authoritative until a coordinated rename occurs.
3. GitHub-special repositories (`LystadJS`, `LystadJS.github.io`) retain their exact names.
4. Software repositories are not renamed until the software/package name is frozen.
5. Renames with inbound links require coordinated website/profile updates even when GitHub redirects old URLs.
6. Course repositories are classified but are not ingested as research projects under schema v1.0.
7. Metadata remains conservative: methods are included only when supported by repository content or explicit project scope.
8. Private working repositories are never made public merely to satisfy registry discovery.

## Inventory

The initial Phase 2 inventory contained **10 owner repositories**. Hub bootstrap added **13 public repositories**: seven method hubs and six domain hubs. Publication of the sanitized AI-governance layer added one public project repository. The account therefore now contains **24 repositories** within the Phase 2 architecture boundary.

The original repository classifications remain in [`inventory.yml`](inventory.yml), and the migration sequence is in [`MIGRATION_PLAN.md`](MIGRATION_PLAN.md). The private AI-governance working repository is currently named `LystadJS/temp` but retains repository ID `1364709765`; the public portfolio-facing layer is `LystadJS/project-ai-governance-non-proliferation`.

## Approved Phase 2 decisions

- The counterterrorism repository remains a broad Islamic State / ethnosectarian attack-patterns research workspace rather than being reduced to one publication.
- The UN transcript project remains intact. Splitting reusable transcript/evidence software from the empirical voting-alignment project is explicitly deferred until that software is mature.
- AI governance uses a private/public split: the private working repository remains separate, while the sanitized public reproducibility layer is published.
- `draftmapR` remains untouched; package naming and repository migration are explicitly deferred.

## Metadata deployments

The following live repositories contain registry metadata:

- `Unsupervised-Machine-Learning/.research/method.yml`
- `counterterrorism_ethnosectarian_islamic_state/.research/project.yml`
- `UN-Transcript-Intelligence-Dynamic-Voting-Alignment/.research/project.yml`
- `project-ai-governance-non-proliferation/.research/project.yml`
- the private AI-governance working repository retains a private manifest but is not the public project location;
- all seven new `method-*` hubs contain `.research/method.yml`; and
- all six new `domain-*` hubs contain `.research/domain.yml`.

The `draftmapR` software manifest remains staged only under `phase2/draft-manifests/` and is not part of active synchronization work.

## Discovery and hub audits

The deployed project manifests validate against the v1.0 schemas and controlled vocabularies. The public discovery workflow validates the discoverable public projects and builds a candidate research graph. The discovery acceptance contract requires all three current public project IDs:

- `ai-governance-non-proliferation`
- `islamic-state-ethnosectarian-attack-patterns`
- `un-transcript-voting-alignment`

The live `Phase 2 Hub Audit` fetches all 13 newly published hub manifests directly from GitHub and verifies their canonical IDs, repository pointers, schema validity, and README auto-generation markers.

See [`DISCOVERY_AUDIT.md`](DISCOVERY_AUDIT.md), [`HUB_BOOTSTRAP.md`](HUB_BOOTSTRAP.md), [`AUTOMATION.md`](AUTOMATION.md), and [`public-ai-governance/PUBLIC_RELEASE_PLAN.md`](public-ai-governance/PUBLIC_RELEASE_PLAN.md).

## Cross-link population

Current public project relationships are generated into the appropriate hub README auto-blocks:

- Islamic State / ethnosectarian attack-pattern research → Spatial Statistics, Missing Data, Statistical Computing, Political Violence, Terrorism and Responses to Terrorism, and Human Security;
- UN transcript/voting alignment → Statistical Computing, Network Analysis, and Longitudinal and Multilevel Statistics; and
- AI governance and non-proliferation → Dimension Reduction, Statistical Computing, Emerging Technology, and Human Security.

No public association is created merely to make a hub appear populated.

## Website and profile integration

The empirical-map and research-card tag resolvers now use canonical IDs rather than hard-coded repository URLs. On page load they resolve those IDs against the generated public registry in `research-registry/dist/research-registry.json`. The AI-governance project card similarly resolves its public project repository from the registry.

The GitHub profile exposes the method and domain architecture directly. GitHub Pages is validated after routing changes before integration is treated as deployed.

## Automatic synchronization

Automatic synchronization is operational:

- `Synchronize Public Research Registry` discovers public project manifests every four hours, validates them, rebuilds `dist/`, rebuilds the research graph, and commits only when generated content changes.
- All **14** live method/domain hubs contain a `Synchronize Research Hub` caller workflow. Each hub updates daily and on manual dispatch using the reusable workflow in `research-registry`.
- Hub synchronization rewrites only `JSL:AUTO-*` README blocks; hand-written content is preserved.
- The website consumes the live generated registry directly, so repository URL changes propagate after registry synchronization without another website code edit.
- If the live registry is unavailable, website repository buttons fall back to the public `LystadJS` repository index rather than stale URLs.

The implementation and acceptance contract are documented in [`AUTOMATION.md`](AUTOMATION.md).

## Phase 2 checkpoints

- **P2-A:** inventory and classification — complete
- **P2-B:** draft manifests and schema validation — complete
- **P2-C:** naming/architecture review — complete, with deferred software naming separated from active work
- **P2-D:** non-destructive manifest deployment — complete for approved repositories; `draftmapR` intentionally deferred
- **P2-E:** coordinated rename and inbound-link migration — rename execution optional/pending; hub-aware link architecture is in place
- **P2-F:** registry discovery audit — complete and extended to the public AI-governance layer
- **P2-G:** method/domain hub bootstrap — complete
- **P2-H:** public hub cross-linking and portfolio/profile integration — complete
- **P2-I:** sanitized public AI-governance reproducibility layer — complete
- **P2-J:** automatic registry → hub → website synchronization — complete

## Deferred / optional work

The active synchronization architecture is complete. Remaining items are intentionally deferred or optional rather than blockers:

1. UN transcript software split — deferred until the reusable software is complete enough to define a stable boundary.
2. `draftmapR` naming and migration — deferred.
3. Coordinated renaming of mature legacy repositories — optional future cleanup; canonical IDs and live-registry routing mean it is no longer required for synchronization to function.
