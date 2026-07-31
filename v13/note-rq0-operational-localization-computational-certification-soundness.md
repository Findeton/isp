# RQ0-L0 computational-certification estimator — finite proof

**Status:** PRE-FIXTURE FREEZE CANDIDATE, 2026-07-31.

**Estimator:** `code/rq0_l0_compcert_estimator_exact.py`.

**Binding pin:**
`note-rq0-operational-localization-computational-certification-pin.md`.

This note proves a conditional result about the generic estimator.  The
opened order-192 object is used only for public performance and regression
tests.  It is not a premise of the proof and cannot earn a scientific rung.
The proof and estimator become byte-immutable together at Stage B, before a
new held-out multiplication object, factor truth, record layout, context
family, scorer, receipt, or delivery exists.

---

## 1. Exact declared scope

The positive theorem applies to a finite operational dataset with:

1. at most 256 raw operation handles and 65,536 complete ordered rows;
2. carrier dimension at most 64 in the generic public implementation (the
   held-out pin imposes the stricter bound 32);
3. one explicit boundary type and composition context on each arrow/row;
4. an independently supplied exact monomial amplitude law over
   \(\mathbb Q(\zeta_{24})\) for each implemented or collapsed row;
5. an observed operational signature checked separately from that law;
6. a quotient with an identity, associative multiplication, and exact
   two-sided inverses on the positive path;
7. at most eight returned normal direct factors;
8. the registered finite candidate and wall-clock caps.

The theorem is not complete for arbitrary process categories, partial
monoids, noninvertible operations, non-normal subsystem notions, arbitrary
unitary tensor decompositions, continuous gauge groups, or infinite systems.
`UNAVAILABLE` and `COLLAPSED` remain typed negative rows and never enter the
positive group-like theorem.

---

## 2. Complete-row lemma

For every raw ordered pair \((a,b)\), validation separately checks:

- source/target boundary compatibility and the supplied `tau`;
- status;
- the explicit result class;
- the independently supplied exact row law \(M\);
- the observed row signature;
- equality of \(M\), modulo the declared global \(\mu_{24}\) row phase, with
  both physical composition and the result representative;
- literal agreement of the observed signature with the supplied law and
  result class.

An unavailable row must have no result, no law, and no signature.  The
validator returns before multiplying amplitudes, so it never silently
replaces an unavailable row with a synthetic product.  A collapsed row is
kept distinct from an injectivity collision of a multiplication map.

Raw aliases are quotiented only when their boundary types, operational
signatures, and independent-selectability declarations agree.  Every raw row
between aliases must induce the same typed quotient row.  Otherwise the input
is invalid or access-underdetermined.  Hence the quotient row

\[
(a,b,\tau,\mathrm{status},\mathrm{result},M)
\]

is a well-defined physical operational datum, not a multiplication table with
an amplitude law filled in afterward.

---

## 3. Complete normal-subobject enumeration

For every quotient element \(g\), the estimator constructs its normal closure

\[
N_g=\langle xgx^{-1}:x\in G\rangle.
\]

Starting with the identity subgroup and all \(N_g\), it closes under products
of normal subgroups.  For normal \(H,K\), the product \(HK\) is their join.
Every normal subgroup \(N\) of a finite group satisfies

\[
N=\bigvee_{n\in N}N_n.
\]

Therefore the fixed point contains every normal subgroup.  Conversely every
constructed object is normal.  Cap exhaustion returns procedural
`RQ0-L0-INVALID`; it never returns a truncated lattice as a negative theorem.

---

## 4. Direct-factor pool and pruned tuple completeness

If \((A_1,\ldots,A_k)\) is an admissible normal direct-factor decomposition,
then for each \(A_i\) the product of the other factors is a commuting normal
direct complement.  The complete pair scan therefore places every \(A_i\) in
the candidate pool.

Before tuple recursion, a pool member is removed only if it fails either:

- generation by its independently selectable classes; or
- exact closure and inverse membership.

Both are necessary positive predicates, so that removal cannot discard an
admissible tuple.

The recursive enumeration uses only hereditary necessary conditions:

1. the prefix order product must divide \(|G|\);
2. every new factor must have identity-only intersection with every chosen
   factor;
3. every new factor must commute operationally with every chosen factor;
4. at most eight factors are admitted.

Every complete positive tuple has order product \(|G|\), so every prefix
product divides \(|G|\); pairwise intersection and commutation are inherited
by prefixes.  Thus the pruning changes enumeration time but not the eligible
set.  Every surviving tuple with product \(|G|\) is submitted to the full
certificate.  All tied maximum-cardinality tuples are retained; ambiguity is
never resolved by lexical choice.

---

## 5. Certificate predicates P1–P8

Every returned tuple passes all of the following exact predicates.

### P1 — independent operability

For each candidate factor, take only classes explicitly declared
independently selectable and compute their subgroup closure.  It must equal
the entire factor.  Composite reachability alone therefore cannot create an
address.

### P2 — mixed implementation in both orders

For every pair of factors and every cross pair of classes, both ordered rows
must have status `IMPLEMENTED`.  No unavailable law is synthesized.

### P3 — exact operational commutation

Every cross pair must give the same quotient result and compatible exact
supplied row laws/signatures in both orders.  Abstract commutation without
operational-law agreement is insufficient.

### P4 — faithful multiplication

The complete Cartesian product of candidate factors is multiplied through
the validated quotient rows.  Every output class must have one and only one
coordinate tuple.  A collision stores two distinct coordinate tuples and the
shared result.  This measured collision is separate from declared
`COLLAPSED` status.

### P5 — closure and inverses

Each factor contains the identity, inverses, and all pairwise products.

### P6 — typed scalar intersection

At this first rung the declared operational scalar center is the identity
subobject.  Every pairwise factor intersection must be exactly that object.
The represented algebras are separately required to intersect in dimension
one.

### P7 — represented-algebra product

For each factor, the exact represented algebra is the span of its monomial
amplitude laws over \(\mathbb Q(\zeta_{24})\).  Factor algebras must commute,
intersect pairwise in the scalar line, and satisfy

\[
\prod_i\dim\mathfrak A_i=\dim\mathfrak A_G.
\]

### P8 — restriction stability

Every nonempty product of returned factors is reconstructed through the
faithful coordinate map.  It must remain closed and inverse-stable, and every
inherited row must stay implemented with an in-scope result, supplied law,
and matching observed signature.

The full certificate is replayed after discovery using the same validated
input and exact cache.  Object equality and the conjunction P1–P8 must both
hold.

---

## 6. Cheap-first evaluation is sound

The optimized predicate order is:

\[
\text{P1}\to\text{P2}\to\text{P3}\to\text{P4}\to
\text{P5}\to\text{P6}\to\text{P8}\to\text{P7}.
\]

The scientific certificate is the conjunction of P1–P8.  For a conjunction,
returning false immediately after any false conjunct is logically equivalent
to evaluating every remaining conjunct and then returning false.  Exact
represented-algebra construction is delayed until all cheaper necessary
predicates pass, but no true candidate can be rejected by that reordering.

---

## 7. Sparse/dense exact-algebra equivalence

Let \(F=\mathbb Q(\zeta_{24})\).  Flattening an \(n\times n\) matrix gives the
linear isomorphism

\[
\operatorname{vec}:M_n(F)\longrightarrow F^{n^2}.
\]

For a monomial law \(U\), each column has one nonzero exact cyclotomic entry.
The sparse backend stores precisely the nonzero coordinates of
\(\operatorname{vec}(U)\), at index `target*n + source`.  The dense antecedent
stores the same vector with explicit zeros.

Both backends perform exact Gaussian elimination over the same field.  Sparse
elimination omits only coordinates whose coefficient is exactly zero.
Therefore, by induction over the supplied law sequence, both maintain bases
for the same linear span.  They have equal dimension, containment, union and
intersection dimensions.  No numerical tolerance or floating-point test is
used.

The public equivalence audit additionally constructs both implementations on
every canonical algebra subobject requested by the opened benchmark run and
checks equality by the rank of the union of their exact bases.  This is a
regression falsifier for the implementation, not the logical premise of the
argument above.

---

## 8. Cache theorem

For one validated dataset, `ExactAlgebraCache` is keyed only by a
`frozenset` of quotient-class indices: the canonical operational subobject.
No dataset handle, operation alias, context name, record handle, target
factor order, fixture hash, or truth label enters the key.

For a fixed quotient representation, the represented algebra is a pure
function of that subobject.  Memoization therefore changes only evaluation
multiplicity.  The ambient key is the full quotient set, so its algebra is
constructed once.  Factor discovery, certificate replay, regional
restriction, and artifact replay share the same cache.  A repeated request
returns the same exact immutable basis.

`MonomialLaw` objects are likewise cached before dense or sparse conversion.
Hence identical laws are not repeatedly converted while exact content is
unchanged.

---

## 9. Full regional morphisms

Faithful factor coordinates provide an executable restriction from a source
factor product to a target factor product.  A `RegAddr` arrow carries:

- every source and target operation class;
- independent-selectability declarations;
- every complete source/target row pair;
- both `tau` values, statuses, explicit results, independently supplied laws,
  and observed signatures;
- preparations, contexts, probes, readouts, record candidates, and gauges.

The row result square, law/signature data, complete context field maps,
identity arrows, composites, and direct-versus-composite diagrams are checked
executable field by executable field.  Hashes authenticate structural
objects but do not substitute for any map.

After construction, the complete atlas is rebuilt from the typed input.  A
positive outcome requires literal equality with this replay.  An adversarial
change to a row, context field, record map, or projector map therefore closes
the positive branch.

---

## 10. Handle-invariant record descent

W3 record candidates are frozen before their exact occurrence/availability
tests.  Their scientific identities use their support, boundary type,
projector resolution, and record dynamics; presentation handles are absent.

For a regional restriction, the record functor constructs exact generator
projector pullbacks.  A target Boolean atom maps to the exact union of source
atoms refining it.  The implementation checks:

- projector equality;
- Boolean partition/homomorphism data;
- identities;
- composition;
- direct-versus-composite naturality.

Consequently renaming a record or witness handle while preserving projectors,
dynamics, support and contexts gives an isomorphic `FactIface` and the same
canonical `Rec` result.  Equal marginal probabilities alone never enter this
criterion.

---

## 11. Twisted-triple discriminator

The public control constructs three full amplitude instruments independently.
Each pairwise map is checked on operations, complete rows/laws, preparations,
contexts, probes, readouts, W3 record projectors/dynamics, and gauges.  The
chosen direct map differs from the two-step map by a nontrivial carrier/record
automorphism.  Thus all three pair maps are valid while

\[
\phi_{12}\phi_{23}\ne\phi_{13}.
\]

Rejection occurs only at the triple-loop equation.  A control with one invalid
pair map would not test descent and is not counted.

---

## 12. Total resolver theorem

The serialized entry point catches deserialization/type failures before
calling the scientific resolver.  The scientific resolver maps every branch
to exactly one registered object:

- positive atlas or localization groupoid, exit 0;
- complete address or regional-map scientific block, exit 0;
- malformed input, exception, timeout, cap/search exhaustion, failed
  artifact replay, missing outcome, or multiple outcome, procedural
  `RQ0-L0-INVALID`, exit 1.

The `Outcome` constructor rejects unregistered code/category/exit
combinations.  The final artifact adjudicator verifies that positives carry
valid certificates and a replayed atlas, while each negative carries exactly
the artifacts allowed by its rung.  Therefore no normal return can emit
`None`, an unregistered label, or exit 0 after procedural invalidity.

Frozen-source anchors are checked by the external public/official runner
before scientific output is admitted.  An anchor mismatch returns the same
registered procedural invalid result.

---

## 13. Soundness theorem

**Theorem.** For every valid input in section 1, every factor tuple returned by
the estimator is independently generated, mixed-implemented in both orders,
exactly operationally commuting, faithfully multiplying, closed and
inverse-stable, scalar-intersecting, represented-algebra-product, and stable
under all declared restrictions.  Every positive regional outcome carries
full executable `RegAddr` maps and a handle-invariant projector/Boolean record
functor whose identity and composition laws hold.

**Proof.** Sections 2–4 establish a complete validated quotient and exhaustive
candidate path at the declared scope.  A tuple is returned only after the
conjunction P1–P8 and exact replay.  Sections 6–8 show that optimization and
memoization preserve those predicates.  Sections 9–10 show that a positive
regional outcome is admitted only after complete map and record-functor
replay.  Section 12 closes every exceptional or inconsistent branch.
Therefore every returned positive has all stated properties.  QED.

---

## 14. Declared completeness theorem

**Theorem.** Subject to section 1's type, normality, representation, factor-
count and cap bounds, the estimator returns every finest tuple satisfying
P1–P8.

**Proof.** Section 3 enumerates all normal subobjects.  Section 4 puts every
factor of an admissible tuple in the direct pool and proves that every
recursive pruning predicate is necessary and hereditary.  Thus every
admissible tuple reaches the full certificate.  All passing tuples are kept,
and all tied maximum-factor-count tuples remain as an ambiguity groupoid.
Cap exhaustion is procedural invalid rather than partial scientific return.
QED.

This is completeness only for the declared finite normal-direct-factor
search class.  It does not assert that this class exhausts physical quantum
locality.

---

## 15. Epistemic labels and ceiling

- **Definitions:** typed operational rows, quotient classes, P1–P8,
  `RegAddr`, `FactIface`, `Rec`, and registered outcomes.
- **Postulates:** complete finite row access, independent-selectability data,
  preparations, contexts, probes/readouts, exact row laws, and finite gauge
  scope.
- **Theorems:** conditional soundness, declared completeness, cache
  equivalence, and sparse/dense equivalence above.
- **Measurements/controls:** public performance, regression, metamorphic,
  twisted-triple, ambiguity and mutant receipts; later, exactly one held-out
  score.

Nothing here constructs topology, spatial locality, influence, causal order,
Lorentzian geometry, spacetime, fields, stress, or gravity.  `RQ0-T1` and
`RQ0-C1` remain prohibited.
