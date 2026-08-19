# Paper 13 Stage-A support-split repair — independent Records/Integrity audit

**Seat:** Records / histories / integrity
**Verdict:** **ACCEPT**
**Recommended disposition:** retain `REPAIR-GREEN-UNREVIEWED`; the repaired
source is eligible for the separately authorized Stage-B attempt and earns no
new scientific rung by this audit.

## 1. Immutable target and method

I bound this audit to:

| object | authenticated identity |
|---|---|
| Git `HEAD` | `f77e184b3ff6067c8014e5ff790df5cae806857a` |
| repaired source | `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e` |
| v2 freeze note | `216ffd6ad9559f68d54dedc46cc4be82146619659f0493b120689a814965f9f6` |
| forward-repair pin | `8ae54ada2a97f347a18b90adcab86dcb2e7c18c04c748cc5e0779b8251449a36` |

The unrelated untracked `v15/scoutt` paths were neither read nor changed. I
did not read the parallel Physics repair review or its scratch. I did not
import, monkeypatch, or call any evaluator function. The evaluator was used
only as a frozen command-line subprocess. All independent calculations lived
under `/private/tmp`.

The pin-only clean-room model used here is
`/private/tmp/p13_support_split_cleanroom.py`, SHA-256
`047667e174a17a1d1588f9a85148c99d5dac46f61f93a7ad3c1805974774c553`.
Its contract is SHA-256
`67014414bc112077de9bebd9041ec822dd6bb771af821b8b7b3e52c1dda44b48`.
The post-freeze no-import verifier is
`/private/tmp/p13_repair_records_verify.py`; it independently parses the
public payload, reconstructs the proofs and hashes, and imports no repository
module.

## 2. Black-box and integrity replay

Three executions of the exact source passed:

| execution | elapsed | exit/status | stdout SHA-256 | normalized payload |
|---|---:|---|---|---|
| repository root | 34.456770 s | `0 / PASS` | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1` | `0894a736dd27ac2be619c0c4e9f24e79ac897b1d8675e2176096df40e7d307fa` |
| alien CWD | 33.289174 s | `0 / PASS` | same | same |
| true off-tree, no `.git` | 33.307999 s | `0 / PASS` | same | same |

Each stdout is byte-identical at 27,380,971 bytes; each stderr is empty. All
42 checks pass. All 92 registered changed-object attacks are unique, executed,
killed, and independently two-way matched against the registry; the ordered
registry hash recomputes to
`7f60ecd06c85c4b4a3eb18ceb7b86470201904cfcd27c7f9c14392c58ea54aeb`.

I independently recomputed every check-evidence hash, every mutation-evidence
hash, all 92 old/new primitive byte hashes, all `changed` predicates, and the
normalized payload hash. No expected-answer mutation or unchanged object
received credit.

## 3. Context split and contextual Boolean quotient

For every tested source cell `s`, I reconstructed the literal fiber after
forgetting the child. A false parent has exactly child bits `{0}`; a true
parent has exactly `{0,1}`. Target-role equality, exhaustive projection,
disjoint fibers, retained parents, count identity, exact forgetting,
`P & N`, `P & !N`, and separation from every old Boolean all recompute from
the literal source and target cells.

The independent census is:

| context | ambient nonzero representatives | contextual classes |
|---|---:|---:|
| C1 | 3 | 3 |
| C2 | 15 | 15 |
| C3 | 14 | 7 |
| C4 | 14 | 7 |
| C5 | 14 | 7 |
| C6 | 12 | 3 |
| **total** | **72** | **42** |

All 72 target splits pass the independently reconstructed proof. Within each
of the 42 contextual classes, target, proof, contextual source, operator,
endpoint law, certificate, and classifier lineage are invariant.

The S11 control is exact: on C3, `B` and `A & B` have different raw ambient
formula hashes but the same contextual truth vector. Their physical source,
Arrow, target, operator entries, endpoint law, lineage, and bound certificate
are identical. Raw formula bytes remain provenance only.

## 4. Bound transitions and dependency reconstruction

The candidate's source-contact Cayley rule has one nonzero transition per
source column, plus one additional transition for each contact-true source.
Independent counting gives:

```text
coherent leaves:       12 + 6 + 12 + 6  = 36
record writer:                              72
source q0/q1/q2:        36 + 72 + 48       = 156
probe  q0/q1/q2:        36 + 72 + 48       = 156
reciprocal reader:                           48
total:                                      468
```

The q2 contact is true on 12 of 36 source states; q0 is never true and q1 is
always true. The selected-port three-sector involution divides every row
equally into CREATE, MERGE, and UNCHANGED. Thus the independent operation
counts are exactly `156 / 156 / 156`. They agree with all 12 serialized
generator-family rows and 312 declared source columns.

The payload fully serializes 12 representative bound certificates. I
independently rebuilt every embedded fiber proof and recomputed every binding
conjunction, inverse-proof hash, certificate hash, and
`classifier_consumed_sha256`. They split `4 CREATE / 4 MERGE / 4 UNCHANGED`;
all are exact. The recomputed aggregate classifier dependency is
`a683eee8e92c4cc6962875cadbcffc7b6ef3d945f77bb5013419d67dc7967258`.
The remaining 456 certificates are committed per generator-family classifier
hash rather than individually expanded in the public payload; their count and
operation typing were reconstructed independently as above.

The support measurement, operator lineage, shadow lineage, support-claim DAG,
gate, independent outcome index, claim row, receipt dependency, and seal all
consume certificate-derived coordinates. The promotive AST contains every
required certificate key and contains none of the legacy role/cell-count keys.

## 5. Mandatory split attacks

The independent controls give the following results:

1. **S1 TAUTOLOGICAL-CHILD — killed by real final-source mutation.** In a true
   off-tree/no-`.git` copy, the exact retention-to-replacement patch produced
   source SHA-256
   `edb8e4900ab77f61c264348080d18140d918489d2653e173059bc2e88babb2c7`.
   The selftest exited 1 after 19.495308 s with
   `INTEGRITY-FAILURE: claim falsifier does not change its object`. Stdout is
   empty (`e3b0c442...b855`); stderr SHA-256 is
   `afe0fe4e57549ae4cb72aca8443638c5d0ddb4c12b88f378323512e3eb4f6439`.
   Independently, the satisfying fiber has only child bit `{1}`, residual
   `-1`, and no `P & !N` witness.
2. **S2 COEXTENSIVE-CHILD-OBJECT — killed.** Exact forgetting survives, but
   the satisfying fiber is one-point and the split conjunction is false.
3. **S4 CELL-COUNT-PADDING — killed.** The scalar count and forgetful image
   pass, while the false-parent fiber is `{0,1}` and the true-parent fiber is
   `{1}`; literal fibers fail.
4. **S6 TRANSPORT-SPLIT-SEVER — killed.** Transporting source and target while
   retaining an old parent/child/fiber coordinate produces typed refusal or a
   nonzero covariance residual. Identity, inverse, and composition of the
   correctly transported proof pass.
5. **S8 CERTIFICATE-PORT-SWAP — killed.** A valid certificate for `P=A` cannot
   decorate the actual `P=!A` branch; port, bit, parent, child, target, and
   occurrence binding reject it before classification.
6. **S11 CONTEXTUAL-BOOLEAN-ALIAS — killed as a presentation split.** The
   physical keys remain equal while only raw ambient provenance changes.
7. **Freshness and ambient controls — killed.** Same-name child reuse, changed
   type reuse, extra target role, and unprojected target cell all refuse or
   make the native conjunction false.

The independently constructed S3, S5, and S7 controls also behave correctly:
forgetting alone, the legacy count predicate, and a supplied Boolean cannot
promote support. All S1--S11 registered rows carry changed native objects,
recomputed residuals, and the pinned outcome effects.

## 6. Anchors, seal, whitelist, and unchanged scientific surface

The live anchor order is exact. The prior source is correctly recorded as
`historical-unobserved`, not falsely authenticated at the now-forward-moved
path. The repair pin, original pin, RUNBOOK, predecessor gate, Paper-12
anchors, old freeze note, both old source reviews, and adjudication exist at
the exact registered paths and hashes. The Stage-A whitelist is exactly:

```text
v16/code/p13_gamma_exact.py
v16/note-paper13-gamma-source-freeze-v2.md
```

All nine Stage-B/fresh/output/receipt/verification/paper paths remain absent.
No run wrote a repository artifact. The seal reports two-way equality of
claims, walls, coordinates, mutations, reads, and covered top-level keys; all
mutation entries and evidence hashes independently recompute.

The preserved rational anchors also recompute independently:

- `g` remains rational on `[1/3,1/2]`;
- `R=((3/5,-4/5),(4/5,3/5))`;
- `B=((9/25,16/25),(16/25,9/25))`;
- `R^2=((-7/25,-24/25),(24/25,-7/25))` and
  `C=((49/625,576/625),(576/625,49/625))`;
- `K=((351/175,-176/175),(-176/175,351/175))` with the exact
  `527/175` nontrivial eigenvalue;
- the reciprocal joint remains normalized and scoped only as raw
  relation-mediated response/proto-backreaction;
- valuation, metric, curvature, continuum, GR, and a selected event law remain
  unconstructed; actualization remains postulated.

## 7. Grade, walls, and ordered disposition

**Grade: ACCEPT.** No semantic survivor, stale dependency, integrity mismatch,
or source/receipt discrepancy was found. The exact forward repair closes the
adjudicated support-recognition failure at the frozen finite scope.

This audit does **not** terminalize Paper 13, run fresh cases, select a blind
family, confer geometry or gravity, derive actualization, or construct a
continuum theory. Its sole procedural effect is to support the disposition
`REPAIR-GREEN-UNREVIEWED` and permit the separately governed Stage-B attempt.

There are no required repair items from this seat.
