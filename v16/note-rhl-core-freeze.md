# RHL generic exact core freeze

**Date:** 2026-08-18

**Pin:** `05d8107` (`v16/note-rhl-pin.md`)

**Status:** result-neutral abstract core frozen before any RHL regulator,
physical data, scorer, outcome, or candidate paper exists.

## Frozen artifacts

| artifact | SHA-256 |
|---|---|
| `v16/code/rhl_core.py` | `032ede336c8cf23b168e018ecd0748e0467d1ca25cb2b44ae750ae320ae9ba8a` |
| `v16/code/rhl_core_output.txt` | `c56c8e3dece8357d3af0e39ea2459b8a29b6fd58bc3ffc99e5ba1cabe85adafb` |
| `v16/code/rhl_core_receipt.json` | `cfd7f243c96f29b303d7c0ef6c283b40be3994b3f6eb1945a801f0677903e060` |

## What is frozen

The core supplies exact `Q(i)` operations for Gram functionals, coarse
graining, refinement pullback, composition, tensor product, interference
defects, and all-input instrument completeness. Its ten public calibration
gates pass:

```text
CORE-EXACT-FIELD
CORE-GRAM-STRONG-POSITIVITY
CORE-REFINEMENT-ISOMETRY
CORE-REFINEMENT-PULLBACK
CORE-COARSE-BIADDITIVITY
CORE-INTERFERENCE-DEFECT
CORE-CUT-ASSOCIATIVITY
CORE-DISJOINT-MONOIDAL
CORE-INSTRUMENT-COMPLETE
CORE-STATE-NORMALIZATION-NOT-COMPLETE
```

The last control is load-bearing: an operator preserves the norm of the one
registered public preparation while its all-input effect is `diag(1,4)`, so
prepared-state normalization cannot be confused with a complete instrument.

## What is not frozen

No graph, lattice, point set, tick, region catalogue, physical history,
record, geometry, coupling, target truth, result word, or candidate-paper
sentence enters these artifacts. The displayed finite matrices authenticate
algebra only. They are not a model of spacetime and cannot support a discrete
ontology claim.

The arbitrary-region descent, no-intermediate-kernel, stable-division, and
geometry-nonselection statements remain theorem targets for the paper. The
core does not prove them by census.

## Verification

Two fresh generations in `/private/tmp/rhl-core.yv4FxW` are byte-identical to
each other and to the frozen output and receipt. The explicit self-test changes
the upstream cross term and confirms that the public interference anchor no
longer passes. Source compilation succeeds with Python 3.13. No floating-point
or numerical-tolerance dependency is present in the substantive path.

The next authorized event is the result-neutral regulator/control freeze. It
must contain at least two nonisomorphic subdivisions, two non-nested cuts, an
intermediate-kernel kill, a pseudo-record eraser, a redundant-record control,
and geometry-blind/sensitive law counterfamilies. Their finite realization is
only a receipt for the general propositions frozen by the pin.
