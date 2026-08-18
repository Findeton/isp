# SRW repaired candidate and postcommit verification

Status: **REPLAY-VERIFIED GREEN-UNREVIEWED; HOSTILE PROTOCOL PENDING**.

Verified candidate commit: `cd3ad8f`.

The original candidate remains preserved at `4f465d0`; its failed verification
is frozen in `v16/note-srw-candidate-verification.md`. The bounded exactness
source repair was committed before repaired physical execution at `86fd5ac`.

## Frozen repaired artifacts

| artifact | SHA-256 |
|---|---|
| `v16/code/srw_core.py` | `dd902c37375f87185f693f8b1e4b22ba3ddeaf9de5641e5d7d951cbba1d3c585` |
| `v16/code/srw_score.py` | `73dfb580b056b4ed2cee511542684bdbe9943633bd2c9888fd4934cd521742f9` |
| `v16/code/srw_fixture.json` | `e40650f04c60635e68fd91938dbba201afec6e426c2e1cfaa0b4f4d8dcefd2e3` |
| `v16/code/srw_output.txt` | `e52c5573c0c784a83419de368286152302bbbfe02cf0c12fb132bd568f0c8695` |
| `v16/code/srw_receipt.json` | `c9b036c9d6382bfd8f1402fe5eee39d3a362842b82b1690e28e5a0130a4d5675` |
| `v16/paper-04-support-rewrite-weld.md` | `f61dde79e5fc0e10db1e5dbe13dec25dceaff9842d5e0c5c06ba2ae90eb4bcae` |

## Repair boundary

The repair adds `GQ.__post_init__`, which coerces both runtime components
through `Fraction`; distinguishes the fixture's historical core hash from the
repaired runtime core hash; adds `SRW-RUNTIME-GAUSSIAN-EXACT`; and adds the
direct `runtime-scalar-leak` mutant. The repaired runtime gate inspects 213
phase-group, connection, holonomy, frame, transformed-connection, and screen
values; every real and imaginary component is a `Fraction`.

The repaired ordinary run passes 37/37. Compared with candidate `4f465d0`, the
complete primary list, measurement object, twelve claims, consequences,
limitations, and Paper 4 bytes are identical. Only core provenance, the new
runtime gate, and the expanded 27-mutant contract move. The unchanged physical
fixture proves that no equation, graph, dictionary, angle grid, classifier, or
outcome word was repaired by assertion.

## Deterministic replay and CLI

Two clean worktree invocations into distinct empty output triples are mutually
byte-identical and byte-identical to all three committed result artifacts. An
ordinary invocation at the canonical existing paths refuses with exit 2 and
changes no byte. `--selftest` exits zero by killing the anchor corruption and
writes no artifact; an unknown option exits 2.

A `git archive` containing only the six committed runtime/read files at
`cd3ad8f` was extracted into a directory with no `.git` metadata. From alien
CWD `/private/tmp`, the archived scorer wrote to fresh explicit paths. Its
paper, transcript, and receipt are byte-identical to the committed artifacts.

## Independent integrity audit

An external reader, sharing neither the scorer's renderer nor its outcome
builder, confirms:

- all 9 payload keys are present in the seal manifest and all 9 canonical JSON
  hashes recompute;
- all 37 gate rows pass;
- all 12 generated exact-claim sentences occur exactly once in Paper 4;
- source, fixture, paper, output, receipt, historical-core, and repaired-core
  hashes match their registered roles;
- the fixture has no nested key containing `expected`, `result`, `verdict`, or
  `outcome`;
- both Python sources compile, contain zero floating-point literals, and have
  no `isclose` or tolerance path;
- all 27 mutant names are distinct and sealed; and
- direct reconstruction from the sealed measurements independently yields all
  four primary conditions and indices `(2,3,5,6)`.

The first external-reader attempt used the nonexistent key
`support_analysis` after completing the replay, mutant, and seal checks; it
stopped with `KeyError` before the primary/off-tree checks. The reader was
corrected to the sealed `support` and `bundle` schema without modifying any
repository artifact, after which the independent primary and off-tree checks
passed.

## Mutation battery

Every mutant exits 1 at its registered first rejecting gate, raises no
traceback, and writes none of its requested output, receipt, or paper paths:

| mutant | first rejecting gate |
|---|---|
| `anchor-corrupt` | `SRW-ANCHORS` |
| `legacy-product-move` | `SRW-LEGACY-IDENTITIES` |
| `dictionary-drop` | `SRW-DICTIONARY-CENSUS` |
| `dictionary-preplant` | `SRW-DICTIONARY-CENSUS` |
| `persistence-spelling` | `SRW-PERSISTENCE-NATURALITY` |
| `graph-probe-row` | `SRW-GRAPH-FUTURE` |
| `swap-call-gauge` | `SRW-CONTINUATION-CLASSIFICATION` |
| `future-reactivation-drop` | `SRW-CONTINUATION-COMMUTANT` |
| `support-equality` | `SRW-ACTUAL-SUPPORT` |
| `forbidden-support` | `SRW-FORBIDDEN-SUPPORT` |
| `port-role-erase` | `SRW-REFERENT-TYPES` |
| `functor-dimension-type` | `SRW-FIBER-DIMENSIONS` |
| `internal-call-gauge` | `SRW-INTERNAL-CLASSIFICATION` |
| `internal-reactivation-drop` | `SRW-INTERNAL-REACTIVATION` |
| `relabel-break` | `SRW-BUNDLE-NATURALITY` |
| `recurrence-site-drift` | `SRW-RECURRING-LOCALITY` |
| `angle-lock-constructor` | `SRW-INDEPENDENT-ANGLE-VARIETY` |
| `reciprocity-assume` | `SRW-RECIPROCITY-LOCUS` |
| `reciprocity-remove` | `SRW-RECIPROCAL-LEFT-INVERSE` |
| `phase-frame-break` | `SRW-PHASE-GAUGE` |
| `runtime-scalar-leak` | `SRW-RUNTIME-GAUSSIAN-EXACT` |
| `holonomy-flatten` | `SRW-HOLONOMY-SCREEN` |
| `cycle-call-gauge` | `SRW-PHASE-ORBITS` |
| `result-count-type` | `SRW-PAPER-BINDINGS` |
| `verdict-flip` | `SRW-OUTCOME-COMPARATOR` |
| `transcript-forge` | `SRW-TRANSCRIPT-RECONCILIATION` |
| `seal-after-write` | `SRW-PREWRITE-SEALS` |

The former crashing `phase-frame-break` now refuses normally at
`SRW-PHASE-GAUGE`; the new leak mutant proves that runtime exact type, rather
than merely absence of float literals, is gated.

## Scientific status

Implementation integrity is verified; physical truth and scope are not. The
candidate still says:

1. an anonymous transition map alone does not recover the relational rewrite;
2. the two currently blind dictionaries become physically different under
   registered lawful futures;
3. the viable finite object is a typed rewrite-plus-transport bundle morphism,
   while catalogue and couplings remain unselected; and
4. exact unrecorded reconvergence fixes the eraser on the reached image, while
   recorded-successor weights remain free.

This is not a unique joint successor law, gravity, QFT, a Hamiltonian,
particles, actualization, a continuum, Lorentz invariance, or phenomenology.
The next process step is a separately frozen three-lens hostile protocol.
Reviewers are not assigned by this note.
