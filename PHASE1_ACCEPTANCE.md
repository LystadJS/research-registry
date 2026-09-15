# Phase 1 Acceptance Record

**Architecture:** Research Repository Architecture v1.0  
**Phase:** Infrastructure Registry  
**Status:** Ready for publication after repository creation  

## Deliverables

- [x] Project JSON Schema
- [x] Method-hub JSON Schema
- [x] Domain-hub JSON Schema
- [x] Method taxonomy
- [x] Technique taxonomy
- [x] Domain taxonomy
- [x] Context taxonomy
- [x] ISO country registry with portfolio-facing display overrides
- [x] Schema + semantic manifest validator
- [x] Taxonomy validator
- [x] Public GitHub project-manifest discovery tool
- [x] Project README renderer
- [x] Method README renderer
- [x] Domain README renderer
- [x] Method-hub project index builder
- [x] Domain-hub project and method index builder
- [x] Project README reverse-link synchronizer
- [x] Website registry builder
- [x] Research graph builder
- [x] GitHub Actions self-validation workflows
- [x] Acceptance fixtures and automated tests

## Frozen constraints

1. Projects are atomic; hubs are indexes.
2. Canonical IDs use immutable lowercase kebab-case.
3. Existing repositories are not renamed or migrated during Phase 1.
4. Human-authored README content outside `JSL:AUTO-*` markers is never overwritten.
5. `.research/project.yml` is the authoritative project metadata source; GitHub topics are secondary.
6. `countries` and `map_countries` remain semantically distinct.
7. Method, technique, domain, context, and country references must resolve against controlled vocabularies.
8. Phase 1 public-project discovery is read-only.

## Acceptance test baseline

The initial local acceptance suite contains 17 tests covering validation, cross-link generation, registry generation, and graph construction.
