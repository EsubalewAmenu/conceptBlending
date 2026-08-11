# Structural integration

`StructuralIntegration.metta` connects the perspective-aware V-predicate
extraction pipeline to Cartesian generic-space construction.

For two concept names and one perspective,
`prepare-structural-blend`:

1. builds both compact V-predicates;
2. retrieves each concept's separately stored algebraic specification by
   concept name and perspective;
3. invokes the generalization component through its public `main-lcg` entry
   point to construct the generic-space algebraic specification; and
4. returns a `structural-blend-preparation` bundle.

The result deliberately records two unfinished dependencies:

- property truth scalars remain pending the GNN assignment stage;
- enriched Hom values remain pending a dedicated Hom extraction/building
  pipeline.

Consequently, the V-enriched colimit check is marked `Blocked` rather than
using fabricated or bottom Hom values.

The stable component boundary accepts grounded MeTTa text. Freeze each
already-computed producer result with `repr (reduce ...)`:

```metta
!(import! &self StructuralIntegration)
!(prepare-structural-blend-from-texts
    generic_name functional_use
    (repr (reduce (left-v-predicate-producer)))
    (repr (reduce (right-v-predicate-producer)))
    (repr (reduce (left-spec-producer)))
    (repr (reduce (right-spec-producer))))
```

`prepare-structural-blend-from-specs` is the typed convenience boundary for
producer expressions. The integration layer does not duplicate generic-space
cache lookup, Cartesian planning, pair resolution, or persistence; these remain
owned by `main-lcg` and the generalization component.
