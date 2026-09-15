# Method and Domain Hub Bootstrap

**Status:** Complete  
**Completed:** 2026-09-15

P2-F proved that the live registry could discover and validate existing project metadata. The approved hub bootstrap has now been executed without renaming any existing project repository.

## Published method hubs

The existing `Unsupervised-Machine-Learning` repository remains the transitional `unsupervised-learning` umbrella hub. The remaining seven canonical method hubs are live:

- `method-clustering`
- `method-dimension-reduction`
- `method-network-analysis`
- `method-missing-data`
- `method-longitudinal-multilevel`
- `method-spatial-statistics`
- `method-statistical-computing`

## Published domain hubs

All six canonical domain hubs are live:

- `domain-political-violence`
- `domain-terrorism-counterterrorism`
- `domain-humanitarian-response`
- `domain-human-security`
- `domain-emerging-technology`
- `domain-anthropocene-human-ecology`

## Hub structure

Each hub was generated from the frozen taxonomy using `scripts/scaffold_hubs.py` and contains:

```text
README.md
.research/method.yml
```

or:

```text
README.md
.research/domain.yml
```

The README auto-generation markers remain intact so registered projects can be indexed without overwriting human-authored methodological or substantive material.

## Validation

The `Phase 2 Hub Audit` GitHub Actions workflow fetches the live manifests directly from the published repositories and verifies:

1. schema validity;
2. controlled-vocabulary validity;
3. canonical IDs;
4. repository pointers; and
5. required README auto-generation markers.

The first live audit completed successfully.

## Initial cross-link population

The currently public project manifests have been used to populate hub indexes conservatively:

- the Islamic State / ethnosectarian attack-pattern project is indexed under Spatial and Geographic Statistics, Missing Data and Measurement, Statistical Computing and Visualization, Political Violence, Terrorism and Responses to Terrorism, and Human Security;
- the UN transcript/voting-alignment project is indexed under Statistical Computing and Visualization, Network Analysis, and Longitudinal and Multilevel Statistics;
- hubs with no currently public registered project retain an empty-state message rather than inventing project associations;
- the private AI-governance working repository is not exposed through public project indexes until the approved sanitized public layer exists.

## Website and profile integration

The portfolio's empirical-map and Research-page tag routing now points method and substantive-domain labels to these hubs. The GitHub profile README also exposes the complete method-hub and domain-hub architecture.

## Remaining migration boundary

Hub creation does not authorize project-repository renames. Existing project URLs remain unchanged. Coordinated renames, public/private AI-governance separation, and the final `draftmapR` package/repository name remain later Phase 2 work.
