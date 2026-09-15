# Phase 2 — Repository Inventory and Migration

**Architecture:** Research Repository Architecture v1.0  
**Mode:** Non-destructive metadata deployment, hub bootstrap, public-project release, and link integration  
**Scope:** Repositories owned by `LystadJS` and visible to the connected GitHub installation.

Phase 2 maps existing repositories into the frozen v1.0 taxonomy, deploys machine-readable metadata without forcing renames, validates live discovery, creates the approved method/domain hubs, publishes a sanitized AI-governance reproducibility layer, and connects the public portfolio to the resulting graph.

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
- The UN transcript project remains intact during migration, but the long-term architecture should split the reusable transcript/evidence engine from the empirical voting-alignment project.
- AI governance uses a private/public split: the private working repository remains separate, while the sanitized public reproducibility layer is now published.
- `draftmapR` remains untouched until the final package name is frozen.

## Metadata deployments

The following live repositories contain registry metadata:

- `Unsupervised-Machine-Learning/.research/method.yml`
- `counterterrorism_ethnosectarian_islamic_state/.research/project.yml`
- `UN-Transcript-Intelligence-Dynamic-Voting-Alignment/.research/project.yml`
- `project-ai-governance-non-proliferation/.research/project.yml`
- the private AI-governance working repository retains a private manifest but is not the public project location;
- all seven new `method-*` hubs contain `.research/method.yml`; and
- all six new `domain-*` hubs contain `.research/domain.yml`.

The `draftmapR` software manifest remains staged only under `phase2/draft-manifests/`.

## Discovery and hub audits

The deployed project manifests validate against the v1.0 schemas and controlled vocabularies. The public discovery workflow validates the discoverable public projects and builds a candidate research graph. The discovery acceptance contract now requires all three current public project IDs:

- `ai-governance-non-proliferation`
- `islamic-state-ethnosectarian-attack-patterns`
- `un-transcript-voting-alignment`

The live `Phase 2 Hub Audit` fetches all 13 published hub manifests directly from GitHub and verifies their canonical IDs, repository pointers, schema validity, and README auto-generation markers.

See [`DISCOVERY_AUDIT.md`](DISCOVERY_AUDIT.md), [`HUB_BOOTSTRAP.md`](HUB_BOOTSTRAP.md), and [`public-ai-governance/PUBLIC_RELEASE_PLAN.md`](public-ai-governance/PUBLIC_RELEASE_PLAN.md).

## Cross-link population

Current public project relationships have been written into the appropriate hub README auto-blocks:

- Islamic State / ethnosectarian attack-pattern research → Spatial Statistics, Missing Data, Statistical Computing, Political Violence, Terrorism and Responses to Terrorism, and Human Security;
- UN transcript/voting alignment → Statistical Computing, Network Analysis, and Longitudinal and Multilevel Statistics; and
- AI governance and non-proliferation → Dimension Reduction, Statistical Computing, Emerging Technology, and Human Security.

No public association is created merely to make a hub appear populated.

## Website and profile integration

The empirical-map tag resolver sends method and substantive-domain tags to the corresponding hub repositories. Research-page tags use the same hub architecture. The AI-governance project card now links directly to the sanitized public reproducibility repository, and the GitHub profile features that project under Selected Work.

GitHub Pages is validated after each routing change before the integration is treated as deployed.

## Phase 2 checkpoints

- **P2-A:** inventory and classification — complete
- **P2-B:** draft manifests and schema validation — complete
- **P2-C:** naming/architecture review — complete, with package naming explicitly deferred
- **P2-D:** non-destructive manifest deployment — complete for approved repositories; `draftmapR` intentionally deferred
- **P2-E:** coordinated rename and inbound-link migration — rename execution pending; hub-aware link architecture is in place
- **P2-F:** registry discovery audit — complete and extended to the public AI-governance layer
- **P2-G:** method/domain hub bootstrap — complete
- **P2-H:** public hub cross-linking and portfolio/profile integration — complete
- **P2-I:** sanitized public AI-governance reproducibility layer — complete

## Remaining Phase 2 work

The remaining work is now narrower:

1. freeze the final package name for `draftmapR` before any software-repository rename;
2. decide and implement the final split point between reusable UN transcript infrastructure and the voting-alignment empirical project;
3. execute coordinated project-repository renames only after those scope decisions are frozen; and
4. replace remaining transitional hard-coded project URLs after canonical project names are established.
