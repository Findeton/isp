# Independent hostile review — RQ0-L0

## Frozen surface

Reviewed read-only at the exact commits:

- Pin: `f218dde7b73631f7fd6359582d7bf494990eb076`
- Estimator freeze: `a5b71735fb80d7214e1cc4e5a389289572895d53`
- Delivery: `3572774435c8940993610c3204edf85b94627141`

Verified SHA-256 values:

- Pin: `02ed47ad0a294741e613639b02066797a2057fcfcd816edd81203f353b1f9a59`
- Estimator: `0b8d90bad735f6574ee367dd0bf7e98bcc1c6f2854f7a12070c82bae84e063b8`
- Fixtures: `ada6dcbce2e9686b7ab45523cb8e8937a0c98cbae6504fd95092cf60aa7388f5`
- Scorer: `60a9819790b4c81ff76c04ef14b0bb2e0dedeb41a516ec884bd11eebdfb61988`
- Delivery note: `89f038ca2521a9c65f476693743d2a4bb7536905d41d2164fba82486284d2778`
- Text receipt: `0297ac85c85743eb5ef0dc15ca4fdb07acf421b142019cc256da3f4d671e5068`
- JSON receipt: `a073dd2da23d2236658b118ab3d0e19965ae12a1b5caafbac7e7ad1fc59144a5`

The repository remained clean.

## Executive verdict

**RED / REJECT terminalization.**

The exact algebraic construction is real, but the delivery does not establish the pinned notion of an independently addressable operational localization. The current `GREEN-UNREVIEWED / RQ0-LOCAL-ATLAS` receipt should be withdrawn.

Recommended adjudication:

- Receipt status: `RQ0-L0-INVALID`
- Highest defensible scientific outcome: `RQ0-L0-BLOCKED-AT-ADDRESS`
- Do not open `RQ0-C1`

The blocking outcome is justified by an explicit candidate class, an exact quotient, and an exact access/presentation obstruction—not merely by absence of data.

## Independent reruns

The official executable reproduced:

- exit `0`
- `56/56`
- four dimension-4 factor atoms
- 14 local objects
- 66 pair overlaps
- 134 triple overlaps
- 10 record-bearing regions
- reported highest rung `RQ0-LOCAL-ATLAS`

The observed-anchor mutant reproduced:

- exit `1`
- `55/56`
- status `INVALID`
- both positive rungs suppressed
- highest outcome `None`

Thus source locking and the one-anchor fail-closed path work. The scientific certification nevertheless fails because mandatory pinned predicates are absent from the dataset and ledger.

# Ranked findings

## F1 — FATAL: `Comp_D` and operational addressability are absent

The pin defines the input with an explicit flat typed composite table

\[
\mathsf{Comp}_D
\]

and requires:

- independently selectable generators;
- exact joint implementation;
- faithful composition;
- detection of collapsed intervention pairs;
- closure and the algebraic product test.

`OperationalDataset` contains preparations, interventions, contexts, probes, support actions, presentation actions, and records. It has no composite table, no joint-implementation relation, and no faithful-pair-composition data.

`support_actions` is only an untyped tuple used to construct reachable support. It is not a table mapping intervention tuples to physically implemented composite classes.

The factorization loop checks only:

- non-scalar generated star-algebras;
- product of algebra dimensions;
- cross-block generator commutation;
- scalar pairwise intersections.

It never checks whether mixed-block operations are physically jointly implementable.

This creates an exact indistinguishability countermodel:

- In world \(W_+\), the supplied individual matrices have all required mixed flat composites.
- In world \(W_-\), the same individually accessible matrices and all stored Born tables exist, but mixed-block joint schedules are forbidden or composition pairs collapse.
- Both worlds serialize to the identical `OperationalDataset`.
- The estimator returns the same positive localization for both.
- \(W_-\) fails the pinned definition of addressability.

Therefore the code proves an algebra factorization, not operational independent addressability. This alone closes both positive L0 rungs.

## F2 — FATAL: exact generator-presentation mutant defeats localization

The pin’s C1 requires distinct circuit **or generator presentations** of the same operational process to yield isomorphic localization.

I independently tested the public \(M_4\) process.

Base primitive presentation:

\[
G=(X_1,Z_1,X_2,Z_2).
\]

Alternative exact generating presentation:

\[
G'=(X_1,Z_1,X_1X_2,Z_2).
\]

They generate the same exact star-algebra:

\[
\operatorname{Alg}^*(G)
=
\operatorname{Alg}^*(G')
=
M_4,
\]

and the missing generator is recovered by the exact composite

\[
X_2=X_1(X_1X_2).
\]

Observed estimator results:

| Measurement | Base | Alternative |
|---|---:|---:|
| Ambient algebra dimension | 16 | 16 |
| Generated algebras equal | yes | yes |
| Valid factorizations | 1 | 0 |
| Finest factorizations | 1 | 0 |

A second mutant merely added the redundant accessible composite \(X_1X_2\) to the original four handles. The ambient algebra remained dimension 16, but valid factorizations again changed from one to zero.

The estimator therefore depends on which accessible operations are declared primitive rather than on the operational algebra plus composition closure. This is exactly the distinction the missing `Comp_D` was supposed to handle.

The delivered C1 control does not test this. Its two “circuit presentations” are reduced to exactly the same encoding matrix before the estimator sees them.

## F3 — FATAL for `RQ0-LOCAL-ATLAS`: mandatory C10 fails

The pin states:

> Every positive localized object counted toward the main atlas must contain a nonempty record algebra.

The delivered result contains:

- 14 objects counted as localized objects;
- 10 record-bearing objects;
- 4 singleton objects with empty record algebras.

The delivery note explicitly acknowledges that single-atom objects carry no record. The scorer nonetheless:

1. uses all 14 objects for `overlap.local_object_count`;
2. constructs the 14-object, 50-arrow localization category;
3. later filters to the 10 record-bearing objects only for the non-star metric;
4. never creates a C10 check.

This is not merely missing exposition. The positive atlas gate counts objects that violate its mandatory object condition.

Restricting the claim to the ten record-bearing objects does not directly repair the delivered category: many of their pairwise meets are singleton, recordless algebras, so the advertised meet structure and record-bearing object class no longer coincide.

## F4 — MAJOR: the ambiguity control supplies a symmetry instead of recovering ambiguity

The ambiguity fixture has:

- exactly one finest factorization;
- `is_factorization_ambiguous == False`;
- identity and atom-swap arrows only because the swap is supplied in `presentation_actions`.

Removing the supplied swap while preserving the preparations, intervention matrices, contexts, probes, and operational signatures produces only the identity arrow.

Observed:

- with supplied swap: `[(0,1), (1,0)]`;
- without supplied swap: `[(0,1)]`;
- number of finest factorizations in both cases: one.

Supplying gauge or symmetry actions is permitted as a declared postulate. What has not been demonstrated is C7’s harder case: several operationally indistinguishable finest factorizations discovered and retained without selecting a representative.

The outcome logic is also mismatched to the named rung. `groupoid_earned` requires the main check `localization.finest_count`, whose expected value is exactly one, plus a hidden atom match that itself refuses multiple finest factorizations. A genuinely ambiguous main fixture would therefore be downgraded rather than earn `RQ0-LOCALIZATION-GROUPOID`.

The defensible statement is:

> A supplied finite presentation action is transported to an automorphism of one recovered factorization.

That is weaker than recovered localization ambiguity.

## F5 — MAJOR: overlap algebras are structural, but restriction maps are mostly metadata

The positive part is genuine:

- all proper joins are generated from recovered atom algebras;
- pair and triple meets are computed as atom intersections;
- their dimensions are checked against exact algebra intersections;
- W3 records attach only when their actual projectors and dynamics lie in the candidate algebra.

Thus the algebraic overlap lattice is not copied directly from hidden incidence truth.

However, the claimed restriction category and projector descent are not returned as typed amplitude maps by the estimator. The scorer constructs:

- `LocalRestriction` from truth-mapped atom subsets;
- `RecordRestriction` containing source ID, target ID, record handle, and a constant descriptive string.

The “path-law” checks only verify that the handle `w0` occurs in the source and target record sets and that the corresponding tuple key exists. There is no executable algebra homomorphism, boundary map, projector pullback calculation, or naturality/composition square.

Because every object is represented as a subalgebra of one common carrier and `w0` is literally one global witness, an identity inclusion interpretation is plausible. The exact common-projector membership result should be retained. The stronger language of “three explicit typed projector pullbacks” is not yet executable at the standard reached by terminal RQ0-A.

The non-star counts are also largely forced once four factor atoms are recovered:

\[
14=2^4-2
\]

proper joins, with the pair/triple counts generated combinatorially from that Boolean lattice. They verify the algebraic lattice, but are not independent evidence that an overlap nerve was recovered from separately presented regional access data.

## F6 — MAJOR: controls and outcome gates are undercomplete and fail-open

Several checks can accept scientifically relevant mutants.

### Generator-presentation control

The delivered presentation control inserts cancelling gates and proves the two complete encoding matrices are exactly equal. The estimator never sees two different generator presentations. The independent \(G\rightarrow G'\) mutant above fails C1.

### Gauge helper

`dataset_is_exact_conjugate` does not compare `support_actions` or `presentation_actions`.

Independent mutants changing either field were still accepted as exact conjugates:

- changed support actions accepted: `True`;
- changed presentation group accepted: `True`.

The official fixture happens to conjugate these fields correctly, but the control predicate is fail-open.

The scorer also does not run `analyze_localization` on the main gauge variant or phase variant. It checks exact dataset conjugacy and hidden-handle atom-algebra descent instead. The underlying exact algebra algorithm is likely conjugation invariant, but the advertised end-to-end main-fixture control is not executed.

### No-smuggling detector

The static detector only scans imports for fixture/scorer-related module names.

Independent source mutants produced:

- fixture-truth import detected: `True`;
- hardcoded hidden atom partition detected: `False`;
- dataset-handle branch detected: `False`.

Thus the chosen import mutant works, but the detector does not establish the broader C12 claim that hidden component labels or expected overlaps cannot be read or hardcoded.

### Equal-law/no-bridge control

The equal-law comparison is exact, and a 4-to-8 fixed-carrier isomorphism is indeed impossible. But `bridge_exists=False` and its obstruction are literal fixture dictionary entries, not the result of a bridge-search routine. It establishes the elementary dimension obstruction, not general same-law/no-structural-bridge discrimination.

### Outcome ledger

The booleans are not hardcoded constants, and the anchor mutant is correctly fail-closed. The problem is omission:

- no `Comp_D` gate;
- no joint-implementation gate;
- no faithful-composition gate;
- no C10 all-positive-objects-have-records gate;
- no genuine multiple-factorization ambiguity gate;
- no typed projector-pullback gate;
- no actual generator-presentation C1 gate.

Consequently `56/56` means all implemented rows pass, not all pinned requirements pass.

The receipt also omits the delivery commit and its own text/JSON hashes from its provenance object, although those hashes are recorded later in the ledger.

# Algebraic assessment

The product-dimension part is not the defect.

For pairwise commuting finite-dimensional unital star-subalgebras \(A_i\), the multiplication map

\[
\bigotimes_i A_i\longrightarrow
\operatorname{Alg}^*(A_1,\ldots,A_n)
\]

is an algebra homomorphism. Here the partition covers every intervention class, so the image is the ambient generated algebra. If

\[
\prod_i\dim A_i=\dim A,
\]

surjectivity plus equal finite dimension makes the multiplication map an isomorphism.

Checking commutation on every cross-block generator is sufficient because the generated star-algebras then commute elementwise.

Therefore the delivered main fixture really does contain an exact algebraic factorization

\[
M_{16}\cong M_2^{\otimes4}
\]

through the globally conjugated presentation. The missing step is operational joint addressability, not the finite algebra calculation.

# Does the access contract encode localization?

Yes, structurally, although not through names.

For the main fixture, the exact noncommutation graph on the eight opaque intervention classes is four disconnected edges:

\[
(q7,q2),\quad(q0,q5),\quad(q6,q1),\quad(q3,q4),
\]

and every vertex has degree one.

Those are exactly the four hidden factor pairs. Global conjugation obscures visible tensor slots but preserves this commutation graph. Thus the fixture supplies a primitive intervention basis already aligned with the desired factors.

This is not literal label leakage: the estimator is genuinely fixture-independent and the handles are opaque. It is nevertheless target-built structural access. The exact generator mutant shows that the result disappears under an equivalent generating presentation of the same algebra/composite closure.

The defensible interpretation is therefore:

> Given a specially factor-aligned primitive intervention access basis, the frozen estimator reconstructs its commuting algebra factors through a global encoded presentation.

It is not yet generator-independent operational localization.

# What survives

The following results remain credible and useful:

- exact arithmetic over \(\mathbb Q(\zeta_8)\);
- the temporal estimator freeze and dependency separation;
- exact reachable-support removal of the inaccessible direct-sum completion;
- an exact operational-signature quotient at the supplied access scope;
- exhaustive enumeration of all 4,140 partitions of eight classes;
- exact recovery of four commuting dimension-4 star-algebras from the selected main generator surface;
- the resulting Boolean lattice of proper generated subalgebras;
- exact pair/triple algebra-intersection measurements;
- six genuine W3 write/preserve/erase/no-write witnesses;
- attachment of those witnesses by matrix-algebra membership rather than marginal-law matching;
- exact discrimination of an uncompensated cyclotomic phase;
- correct rejection of a trivial fixed-carrier 4-to-8 equal-law bridge;
- correct anchor mutation failure;
- no causal, geometric, field, or gravity object.

This is a sound finite algebra-and-record construction, but it is below the pinned operational-localization rung.

# Required repair

A compliant repair needs a fresh estimator freeze and genuinely new unseen fixture family because the frozen estimator must change after truth was opened.

Minimum repair:

1. Add an explicit typed `Comp_D` table.

   It must record admissible flat composites, result classes, unavailable pairs, and composition collapses.

2. Gate every candidate complement on:

   - independent single-handle selection;
   - mixed-block joint implementation;
   - faithful pair composition;
   - closure;
   - exact algebraic product factorization.

3. Normalize generator presentation.

   At minimum, the exact \(G\leftrightarrow G'\) mutant and redundant-composite mutant must return isomorphic localization. Candidate factorization should depend on the operational algebra/composite structure, not an arbitrary primitive generating list.

4. Repair C10.

   Either construct a fixture in which every counted local object has its own nonempty derived W3 record algebra, or define and verify a different record-bearing, overlap-closed category that actually satisfies the pin.

5. Add a genuine ambiguity fixture with multiple finest factorizations and verify that all objects and arrows are returned.

6. Return executable structural maps.

   Algebra inclusions/restrictions, record-projector pullbacks, composition, and triple-path naturality should be actual exact objects, not descriptive strings.

7. Strengthen controls and gating.

   Analyze the complete gauge and phase variants end-to-end; include all dataset fields in conjugacy checks; add hardcoded-truth and dataset-handle mutants; derive outcomes from every pinned mandatory gate.

# Final adjudication

\[
\boxed{\text{RQ0-LOCAL-ATLAS is not earned.}}
\]

\[
\boxed{\text{RQ0-LOCALIZATION-GROUPOID is not earned.}}
\]

\[
\boxed{\text{Highest defensible rung: RQ0-L0-BLOCKED-AT-ADDRESS.}}
\]

The programme has an exact encoded algebra factorization and a useful W3-decorated subalgebra lattice. It has not yet demonstrated operationally independent localization invariant under generator presentation.
