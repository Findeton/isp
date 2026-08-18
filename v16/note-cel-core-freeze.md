# CEL generic exact core freeze

Status: **GENERIC CORE FROZEN BEFORE PHYSICAL FIXTURE**.

Ledger event: v16 #69. Immutable Paper 7 pin commit: `671a257`.

The following public artifacts are frozen before any CEL physical fixture,
scorer, official result, receipt, or Paper 7 candidate exists:

| artifact | SHA-256 |
|---|---|
| `v16/code/cel_core.py` | `f08b880095e71ac79082d2672ec849dc9ffd1ab66c702a85f2b24165a02aedac` |
| `v16/code/cel_public_output.txt` | `ec5061724cbcf50d57d5022566571a8360e5ab680e392d730d1a7ad8e6aa543d` |
| `v16/code/cel_public_receipt.json` | `a349c57087b60f2ac13f07006db92c9a349a8c0a8e543d07a3c4ff4433fc4eb2` |

The self-contained core contains no CEL context dictionary, recurrence
doctrine, JCV physical factorization, relational flag attachment, selected
coupling, primary comparator, or Paper 7 prose. It implements:

- exact Gaussian-rational scalar and matrix algebra, Kraus channels,
  history kernels, calibrated class operators, Stinespring stacking, and
  operational channel signatures;
- exact Hermitian PSD certification, rank, zero-pivot-safe `LDL^dagger`,
  deterministic four-square pivot decomposition, and a constructive
  rectangular `Q(i)` Gram factor with at most twice the matrix rank;
- exact Gaussian-norm obstruction tests for positive rationals;
- finite column-stochastic channels, disjoint-support zero-error recovery,
  branch coarse-graining, licensed recovery maps, exact continuation-
  semigroup closure, and all-word licensed-recovery certificates; and
- deterministic canonical JSON, payload seals, atomic writes, strict CLI,
  existing-target refusal, selftest, and public mutants.

Nine constructor-stated public gates pass. They exactly factor a non-real
Hermitian PSD matrix and a singular PSD matrix inside the `2r` row bound;
refuse a non-PSD matrix; decompose `5/3` into two Gaussian norms; distinguish
diagonal-algebra covariance from record recovery using a reset channel;
accept a relabeling permutation; show retained branch recovery can disappear
under coarse-graining; close a two-element continuation semigroup with an
all-word licensed certificate; and reconstruct a projective-measurement
Stinespring isometry. These are public calibrations, not CEL's physical
fixtures or registered `7/5` result.

Two fresh executions reproduce both public artifacts byte-for-byte. An
execution from alien CWD `/private/tmp` does the same. `--selftest` and all
three public mutants exit `1` without writing artifacts; an unknown option
exits `2`; and existing official targets refuse before evaluation. Static
parsing finds zero Python float literals. A separate exact stress battery
factors the zero matrix, a zero-leading-pivot matrix, a complex singular
matrix, and 32 constructed complex PSD matrices of orders one through four,
always reconstructing exactly within the registered row bound.

At this freeze the following later paths are absent:

```text
v16/code/cel_fixture.json
v16/code/cel_score.py
v16/note-cel-fixture-freeze.md
v16/code/cel_output.txt
v16/code/cel_receipt.json
v16/paper-07-creation-event-universality-recoverable-records.md
v16/note-cel-candidate-verification.md
v16/note-cel-hostile-protocol.md
```

The next authorized stage is a data-only physical fixture and verdict-neutral
scorer, both frozen before first official execution. This generic core may not
change after the core-freeze commit. Papers 3–6 and the unrelated untracked
v15 SCOUT-T files remain untouched.
