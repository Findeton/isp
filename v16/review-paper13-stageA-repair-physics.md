# Paper 13 Stage-A support-split repair — independent physics/ontology review

Date: 2026-08-19
Seat: Physics / ontology
Verdict: **ACCEPT**
Scope of acceptance: the bounded Stage-A instrumentation repair only

## 1. Immutable target and review isolation

I authenticated the following frozen target before inspecting the repaired
implementation:

| object | authenticated identity |
|---|---|
| repository HEAD | `f77e184b3ff6067c8014e5ff790df5cae806857a` |
| repaired source | `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e` |
| source-freeze v2 note | `216ffd6ad9559f68d54dedc46cc4be82146619659f0493b120689a814965f9f6` |
| forward-repair pin | `8ae54ada2a97f347a18b90adcab86dcb2e7c18c04c748cc5e0779b8251449a36` |
| RUNBOOK | `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58` |

I did not import or call any measurement function from the source under audit.
The independent oracle and attack contract were frozen before repaired-source
access. I did not read the Records-seat report or scratch. No fresh or official
mode ran, and no scientific/publication artifact was created.

## 2. Independent reconstruction receipts

The pin-only split oracle is:

- `/private/tmp/p13_stageA_repair_cleanroom_reference.py`, SHA-256
  `57af4abce77ca82deac75ce0a64a808a67642a7cf798d44bee4f5bddda18d29d`;
- deterministic output SHA-256
  `f1d4debe14024debab0f449752b9e0846842771399b438340a7621c612facdfd`;
- internal payload SHA-256
  `a3a12bf1699f86d2d20804920a7e29a29c4a5ab18b5b9f38ec05860957bbeb21`.

The independent scientific reconstruction is:

- `/private/tmp/p13_stageA_pin_rebuild.py`, SHA-256
  `8c06b3c434ff71b3f7bc34bc30f3dec1bb0dc341da9840d1f5cb4e352a59cce3`;
- deterministic output SHA-256
  `0708794ac1ef33c661261877ebac80dd187387e7bec6817108caf8fa3f6957a6`;
- internal receipt SHA-256
  `b97bb40dc0815ceb35dc51ff3e668b5a12e78d7a79b30e18f5130b43d2bdbf7c`.

The post-freeze no-import semantic checker is:

- `/private/tmp/p13_stageA_repair_postfreeze_physics_check.py`, SHA-256
  `5f684e90c9684deb0fca523a50434656e0640ca560658d35dd7079961833753f`;
- deterministic output SHA-256
  `57b0d4020cd7045361a7eef60e8adfadafc4a15b2b56371fd7032b9eea912361`;
- internal receipt SHA-256
  `5155651f3a5ce15a4c4e77241a0ad2ef9e87f76409ede8bc22455e218e39be1f`.

That checker independently recomputed eight grouped obligations:
authentication, `R/B/C/B2/K` and native nondivision, division/reciprocity,
matching-family scope, the `72/42` quotient, every branch-bound certificate,
all assigned changed objects, and the ontology ceiling.

## 3. Clean replay and source integrity

Three independent black-box executions of `--selftest` passed:

| execution | exit | bytes | stdout SHA-256 |
|---|---:|---:|---|
| repository root | `0` | `27,380,971` | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1` |
| alien CWD, absolute source | `0` | `27,380,971` | same |
| true source-only off-tree, no `.git` | `0` | `27,380,971` | same |

The payload reports `42/42` checks, `92/92` registered mutation kills,
normalized payload SHA-256
`0894a736dd27ac2be619c0c4e9f24e79ac897b1d8675e2176096df40e7d307fa`,
zero fixture evaluation, zero fresh reads, zero official-artifact reads, and
zero publication writes. Every forbidden Stage-A output/fresh/verification/
paper path named by the freeze note was absent.

## 4. Boolean split theorem and contextual quotient

For source cells `S`, contextual Boolean element `P`, and fresh relational role
`N`, I independently reconstructed

```text
E = S union {s union {N} : s in S and P(s)=1}.
```

The repaired proof checks the literal fiber over every source cell. A
`P=0` fiber is exactly `{s}`; a `P=1` fiber is exactly
`{s,s union {N}}`. It separately checks target exhaustiveness, the exact role
set and old types, forgetful recovery, the cell-count identity, nonzero
`P and N`, nonzero `P and not N`, and child freshness/type. These conditions
are necessary and sufficient for the registered split. Recovery, role count,
or scalar cell count alone cannot promote it.

The census is exact:

| context | ambient nonzero representatives | contextual classes |
|---|---:|---:|
| C1 | 3 | 3 |
| C2 | 15 | 15 |
| C3 | 14 | 7 |
| C4 | 14 | 7 |
| C5 | 14 | 7 |
| C6 | 12 | 3 |
| total | **72** | **42** |

The quotient is physical in the registered sense: formulas differing only on
zero/absent cells share one contextual truth vector. In C3, `B` and
`A and B` both give `(0,0,1)`. Their raw formula hashes differ, while their
contextual parent, source boundary, Arrow, presentation key, target context,
operator, endpoint law, lineage, and bound certificate are identical.

This does not collapse distinct laws accidentally. Occurrence identity uses a
boundary-wide contextual formula profile, not a profile on one selected state.
Thus two queries are identified only when they agree on every source context
in the complete boundary catalogue.

## 5. Branch-bound lineage

The repaired implementation has two different proof types:

1. `ContextSplitProof`, a diagnostic context-level theorem that is explicitly
   nonpromotive;
2. `BoundSplitCertificate`, rebuilt from an actual nonzero transition of the
   candidate Gamma.

I independently checked all twelve representative bound certificates. Their
operation census is `CREATE=4`, `MERGE=4`, `UNCHANGED=4`. For every certificate:

- the coefficient is nonzero;
- the law, semantic Arrow/occurrence, source configuration, port, input/output
  bit, source/target sector, contextual parent, child, literal target, and
  operation are bound;
- the parent and child keys equal the embedded context proof;
- the operation/sector relation is exact;
- every literal fiber reconstructs exactly from the serialized source and
  target semantic contexts;
- removing `classifier_consumed_sha256` and canonically hashing the remaining
  certificate reproduces that hash exactly;
- `binding_exact`, `operation_exact`, the context proof, and the final
  conjunction are all true.

The support predicate consumes these certificates and the split-groupoid
evidence. A context proof alone and the legacy role/cell inequality are both
explicitly nonpromotive. A valid split from another port or branch cannot
decorate the actual transition.

## 6. Hostile changed objects

### S1 — real final-byte source mutation

I copied the frozen source off-tree and applied only the registered
retention-to-replacement change. The mutant source SHA-256 is
`edb8e4900ab77f61c264348080d18140d918489d2653e173059bc2e88babb2c7`.
Its selftest exited `1`; stdout was empty (SHA-256 `e3b0c442...b855`) and
stderr SHA-256 was
`afe0fe4e57549ae4cb72aca8443638c5d0ddb4c12b88f378323512e3eb4f6439`,
with `INTEGRITY-FAILURE: claim falsifier does not change its object`.

The independent oracle gives the decisive physics: forgetting still succeeds,
but the satisfying fiber has observed child bits `{1}` instead of `{0,1}`;
the count residual is `-1`, `P and not N` is false, and the native split is
false. The frozen registered changed-object replay independently renders
`P13-SUPPORT-CHANGE-UNPROVEN`. The real source mutant therefore fails closed
before any stale positive claim can be emitted.

### Assigned independent controls

| attack | independent witness | black-box result / SHA-256 |
|---|---|---|
| S4 scalar-count padding | count `3` and forgetting pass, but both fiber rows fail | PASS / `b70ce259d6d3ae8de5ae6b36853a49bd8443a22c4cec014faae823ba22c3f9ae` |
| S6 transport sever | transported `A->B` parent versus stale `A` has exact truth-vector Hamming residual `2` | PASS / `4efcd6ce3fa1e22ee72f1b843b2ca752a0d5fe5a4fb94dd3a2c24979af451af7` |
| S8 branch/port certificate swap | `A=(0,1)` and `not A=(1,0)` bind different parents and targets | PASS / `193d90e6868eef54992d4d8b5144d17cbc194d67ddb683f27ab4065b28488efb` |
| S9 child reuse/type change | disjoint typed-role union fails | PASS / `536932e535de5cc333faef1729439a5cb377cac2cf8564ccf2617f187ea5ef22` |
| S10 ambient padding | scalar count can pass, but role exactness and target exhaustiveness fail | PASS / `b5049166992f0623b5022988a0dbbf9dac018196ce17098874b27a23595d15c5` |
| S11 contextual alias | raw formulas differ; all nine physical fields and certificate agree | PASS / `f1d1845ad8d977c1b7fc6b96a626c3b019d1d05d1f961a01b16502bb469d751f` |

I also checked that copying a proof across law/occurrence identity, using a
non-`RELATION` child, a zero/nontotal parent, an unrelated merge origin, or a
forged output bit/sector is excluded by exact typing or by rebuilding the bound
certificate. No assigned or fresh semantic survivor was found.

## 7. Preserved scientific anchors

Independent rational arithmetic reproduces the frozen values:

```text
R  = [[  3/5,   -4/5], [   4/5,    3/5]]
B  = [[ 9/25,  16/25], [ 16/25,   9/25]]
C  = [[49/625,576/625],[576/625, 49/625]]
B2 = [[337/625,288/625],[288/625,337/625]]
K  = [[351/175,-176/175],[-176/175,351/175]]
```

`K B=C` exactly and its nontrivial eigenvalue is `527/175>1`, excluding a
positive source-independent restart on the registered native cut. The
history-conditioned positive control remains present. Writer normalization,
all-input alternate-cut equality, the finite-word recovery induction, and the
active-reuse eraser remain exact.

The same-law reciprocal joint remains

```text
00 -> 9/25,  01 -> 0,  10 -> 144/625,  11 -> 256/625,
```

with unit normalization and zero opposite-incidence probe response. The
matching-family resource parity, equal blind prefix/prior record law, unequal
same-root responses, and the explicitly class-relative blind-transducer
conclusion also remain unchanged.

## 8. Ontology and scope

The repair now establishes precisely what it claims: a proper extension of a
finite regional Boolean algebra, not a coextensive new name. The two-point
fiber makes the child relation extensionally distinct from every old Boolean
element. Raw cells and role names remain presentation data; contextual Boolean
classes and explicit groupoid transports carry the registered referent.

This is still not metric geometry. Cell number is used only as a redundant
integrity equation after the fiber theorem; it is not a valuation, volume,
dimension, distance, or topology. The repaired output correctly keeps
valuation, metric, curvature, continuum, and GR `UNCONSTRUCTED`, actualization
`POSTULATED`, the division doctrine grammar-relative, and event/filling
selection priced. Operational significance for the new raw relation comes
from the separately preserved later same-law reciprocal response, not from
the split certificate alone.

The strict Paper-13 primary printed by the Stage-A selftest remains historical
regression data, not a new Stage-A award. `REPAIR-GREEN-UNREVIEWED` is the
proper immediate disposition of the frozen source. This report supports only
acceptance of the repair and eligibility to proceed to Stage B once the
independent-review/adjudication conditions are satisfied. It does not establish
law selection, absolute relational irreducibility, geometry, gravity, QFT,
continuum recovery, or actualization.

## 9. Final grade and repair/kill list

Grade: **ACCEPT**.

Numbered findings:

1. The adjudicated tautological-child survivor is killed by the literal fiber
   theorem and by a real final-byte source mutation.
2. Scalar counts, forgetful recovery, role counts, supplied booleans, and
   context proofs alone cannot promote support change.
3. Branch, port, target, coefficient, occurrence, and law binding are native
   and reconstructible for every nonzero transition checked.
4. The `72` ambient representatives correctly quotient to `42` contextual
   classes; contextual aliases do not split physical source identity.
5. All preserved quantum/process controls remain exact and no scope coordinate
   is promoted.
6. No repair, narrowing, or scientific kill is required at this stage.

Final verdict: **ACCEPT / NO-GO condition not triggered**.
