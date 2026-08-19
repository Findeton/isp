# RHL Paper 11 scorer freeze

**Date:** 2026-08-18

**Pin:** `05d8107`

**Generic core:** `24c65b1`

**Regulator controls:** `0241b90`

**Status:** scorer frozen before the Paper 11 candidate, official transcript,
official receipt, result, or any theorem disposition is generated.

## Frozen scorer

| artifact | SHA-256 |
|---|---|
| `v16/code/rhl_score.py` | `b2f1f780d5b907b628adcd4994ac5d6eeb2d2a5abb78783d0a18c06e6582e1c2` |

The scorer authenticates all seven frozen pin/core/regulator hashes, consumes
the exact upstream data rather than copied summary Booleans, audits the
paper's fourteen analytical claim referents and six named theorem statements,
and keeps analytical proof status separate from finite receipts. It expressly
does not claim that Python proves the arbitrary-region theorems. Those proofs
must be verified line by line before green status and attacked by the later
hostile panel.

The registered candidate primary is derived only when all upstream lineages,
paper scope clauses, and registered rung relations coexist:

```text
RHL-REGIONAL-QUANTUM-LAW-CONSTRUCTED-BUT-GEOMETRY-UNENTERED
```

with the possible qualifiers, in rung order:

```text
RHL-POINT-FREE-REGIONAL-KINEMATICS-CONSTRUCTED
RHL-REFINEMENT-INVARIANT-UNSLICED-QUANTUM-LAW-CONSTRUCTED
RHL-STABLE-DIVISION-SHADOW-CONSTRUCTED
RHL-BLOCKED-AT-DYNAMIC-LOCALITY
```

If a required proof referent, scope wall, upstream mechanism, or outcome
relation is absent, the scorer emits `RHL-METHOD-INCONCLUSIVE` and writes no
official artifact.

## Frozen law-type typing

The scorer reports different law types at different grains rather than one
global answer:

```text
unrecorded regional representation -> HISTORY-DECOHERENCE-FUNCTIONAL-REQUIRED
stochastic fundamental reading      -> INDIVISIBLE-MULTITIME-LAW-REQUIRED
stable record boundary              -> DIVISION-KERNEL-SUFFICIENT
higher-order causal process         -> METHOD-INCONCLUSIVE
```

This is the pin's ontology/representation split. It does not make the
decoherence functional ontic.

## Frozen mutants

Fifteen named mutants alter upstream objects or paper scope:

```text
MUT-CORE-HASH
MUT-REG-HASH
MUT-INTERFERENCE-DIAGONAL
MUT-PRESENTATION-MISMATCH
MUT-TAMPER-INERT
MUT-RECORD-UNERASABLE
MUT-REDUNDANCY-LOST
MUT-CHARACTER-INERT
MUT-FIXED-FACTOR-SIGNAL
MUT-DYNAMIC-TRANSPORT-SMUGGLED
MUT-DELETE-DESCENT-THEOREM
MUT-ONTOLOGIZE-MESH
MUT-PROMOTE-GEOMETRY
MUT-PROMOTE-GR
MUT-OUTCOME-TAMPER
```

Source compilation, mutant enumeration, and the upstream cross-term mutation
self-test pass. No candidate paper or official output path exists at this
freeze. The next authorized event is authorship of the self-contained
analytical candidate followed by one official scorer run.
