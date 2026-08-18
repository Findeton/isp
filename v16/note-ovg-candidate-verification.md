# OVG candidate verification

Status: **REPLAY-VERIFIED GREEN-UNREVIEWED**.

Candidate commit: `bb0f13aedadc354068ea2bcc08478bcd8c43ded1`.

The candidate artifacts verified here are byte-immutable:

| artifact | SHA-256 |
|---|---|
| `v16/code/ovg_output.txt` | `48cf0fdecc43b1d148c97bac936a879cbbcf14daddfccd6e597014017155fe7f` |
| `v16/code/ovg_receipt.json` | `4ba954430acd0772da62c8df16b2c6b08bca9e76fd7b25d3b5b72fcc43ce2852` |
| `v16/paper-05-overlap-gram-instrument-variety.md` | `89a6ad8b10b97351d71a499ebbb36b2cf5a89f32d5ec9d005f9b4a68dab16b31` |

## Replay and CLI

Two clean worktree invocations to disjoint temporary paths reproduce all
three committed artifacts byte-for-byte. The public generic artifacts remain
unchanged. `--selftest` dies only at `OVG-ANCHORS`, exits `1`, writes no file,
and emits no traceback. Unknown options exit `2`. An invocation aimed at the
already existing official paths refuses before evaluation.

## Mutation battery

All 30 frozen mutants alter their registered measured object, exit `1` at
exactly the gate stored in the candidate mutation contract, emit no stdout or
traceback, and write no transcript, receipt, or paper:

```text
anchor-corrupt -> OVG-ANCHORS
history-order-drop -> OVG-REFERENT-TYPES
common-boundary-forge -> OVG-REFERENT-TYPES
gram-cross-term-move -> OVG-GRAM-OPERATOR
gram-self-compare -> OVG-GRAM-OPERATOR
state-only-normalize -> OVG-EQUAL-REAL-CONTROL
equal-real-universalize -> OVG-COMPLEX-WITNESS
complex-witness-drop -> OVG-COMPLEX-WITNESS
parity-factor-move -> OVG-PARITY-INSTRUMENT
scalar-call-distinct -> OVG-SPECTRAL-PHASE
eigenphase-count-move -> OVG-UNITARY-CERTIFICATES
phase-constraint-drop -> OVG-SPECTRAL-PHASE
nonnormal-spectral-shortcut -> OVG-NONNORMAL-DIRECT
z-zero-call-coherent -> OVG-SPECTRAL-PHASE
three-history-drop -> OVG-THREE-HISTORY-VARIETY
port-coarsegrain-break -> OVG-PORT-COARSEGRAIN
dependency-call-record -> OVG-DEPENDENCY-TYPE
divergent-call-common -> OVG-DEPENDENCY-TYPE
local-flag-call-implemented -> OVG-LOCAL-FLAG
local-factorization-drop -> OVG-LOCAL-FLAG
binary-product-call-primitive -> OVG-ARITY-COMPOSITE
ancilla-policy-hide -> OVG-ANCILLA-POLICY
durability-assume -> OVG-RECORD-PERMANENCE-SCOPE
causal-switch-word -> OVG-CAUSAL-SCOPE
all-n-promote -> OVG-ALL-N-SCOPE
typed-count -> OVG-ARITY-COMPOSITE
float-leak -> OVG-EXACT-ARITHMETIC
verdict-flip -> OVG-CLASSIFIER
transcript-forge -> OVG-TRANSCRIPT-RECONCILIATION
seal-after-write -> OVG-PREWRITE-INTEGRITY
```

The contract is total: its name set and expected-gate key set are equal.

## Independent payload and mathematics audit

An independent reader, not the scorer's result builder, confirms:

- outer transcript and paper hashes;
- every payload seal and the one-item unsealed manifest;
- 32 unique passing gate rows, exactly reconciled with the transcript;
- 12 generated claims, each appearing exactly once in the paper;
- all 30 mutation names and gate bindings;
- the two overlapping CNOT compositions and
  `A^dagger B = CNOT(A->C)` as exact permutation matrices;
- direct Gaussian-rational multiplication gives
  `K^dagger K=I` for `a=3/5,b=4i/5`, while the corresponding real pair fails;
- direct parity-port completeness;
- five length-at-most-four binary factorization words for each overlapping
  order map;
- the recorded Toffoli `F_2`-nonlinearity witness;
- the phase-nullity mapping
  `{scalar-one:2, scalar-quarter:2, overlap-cnot:1,
  two-quarter-phases:1, three-phase-control:0}`;
- normalization of every registered three-history probability row; and
- equality of the spectator marginal before/after the complete instrument,
  with inequality under the amplifier.

## True off-tree/no-git execution

A `git archive` of only the committed scorer, core, fixture, freeze note, and
immutable antecedent paths at candidate commit `bb0f13a` was extracted under
`/private/tmp`. The extracted directory contains no `.git`. From alien CWD
`/private/tmp`, the archived scorer produces all three candidate artifacts
byte-for-byte.

## Disposition

OVG is **REPLAY-VERIFIED GREEN-UNREVIEWED**, not terminal. The exact finite
candidate and its negative scope walls survive verification. A separately
committed three-lens hostile protocol, independent reports, adjudication, any
authorized repair, and terminal replay remain mandatory before citation as a
terminal result.
