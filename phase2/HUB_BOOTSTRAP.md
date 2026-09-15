# Method and Domain Hub Bootstrap

P2-F proved that the live registry can discover and validate existing project metadata. The next safe step is to create the missing hub repositories without renaming any current project repository.

## Repositories to create

### Method hubs

The existing `Unsupervised-Machine-Learning` repository already serves as the transitional `unsupervised-learning` hub. Create the remaining seven canonical hubs:

- `method-clustering`
- `method-dimension-reduction`
- `method-network-analysis`
- `method-missing-data`
- `method-longitudinal-multilevel`
- `method-spatial-statistics`
- `method-statistical-computing`

### Domain hubs

Create all six canonical domain hubs:

- `domain-political-violence`
- `domain-terrorism-counterterrorism`
- `domain-humanitarian-response`
- `domain-human-security`
- `domain-emerging-technology`
- `domain-anthropocene-human-ecology`

## Generate the scaffold

From `research-registry`:

```bash
python scripts/scaffold_hubs.py \
  --output-dir /tmp/jsl-hubs \
  --skip-method unsupervised-learning
```

The command generates **7 method hubs and 6 domain hubs**. Each output repository contains:

```text
README.md
.research/method.yml
```

or:

```text
README.md
.research/domain.yml
```

The READMEs use the standard auto-generation markers from v1.0 so projects can be indexed later without overwriting human-authored material.

## Publication contract

1. Create each repository as **public** unless a later review identifies a reason not to.
2. Use the exact canonical repository names above.
3. Do not initialize with generated boilerplate that would conflict with the scaffold; an empty repository or one initialized with a temporary README is acceptable.
4. Publish the generated `.research/` manifest and README before adding method notes or project indexes.
5. Validate each hub against `research-registry` after publication.
6. Do not rename existing project repositories as part of hub creation.

## Why hub creation precedes renaming

Canonical IDs already connect projects to methods and domains. Creating hubs first gives every future website tag a stable destination while leaving existing public project URLs untouched. Repository renames can then occur later as a coordinated link migration rather than being coupled to the research-graph rollout.
