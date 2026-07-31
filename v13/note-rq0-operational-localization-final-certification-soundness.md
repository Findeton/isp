# RQ0-L0 final estimator — finite soundness and completeness proof

**Status:** PRE-FIXTURE THEOREM NOTE, 2026-07-31.

**Estimator:** `code/rq0_l0_certification_estimator_exact.py`.

**Binding pin:** `note-rq0-operational-localization-final-certification-pin.md`.

This note is committed with the generic estimator before the main fixture,
its abstract multiplication law, its factor truth, its access contexts, or its
atlas truth exists.  It proves a finite conditional theorem about every valid
input in the estimator's declared class.  Public calibrations exercise the
hypotheses and counterhypotheses; they are not the proof.

---

## 1. Exact declared scope

The positive theorem applies to a finite operational dataset whose quotient
composition object has:

1. one fixed compatible boundary/composition type;
2. at most 256 exact operational classes and 65,536 complete ordered rows;
3. exactly one row for each ordered class pair;
4. status `IMPLEMENTED` on every positive-path row;
5. an independently supplied exact monomial amplitude law on each row;
6. one identity, associative multiplication, and one two-sided inverse for
   every class;
7. exact operational signatures modulo one global `mu_24` row phase;
8. exact represented amplitudes over `Q(zeta_24)`;
9. finite search caps frozen in the pin and estimator.

Thus the positive quotient is a finite group-like operational object with an
exact unitary representation.  The theorem does not claim completeness for:

- arbitrary partial monoids, categories with several boundary types, or
  noninvertible process theories;
- non-normal subsystem notions;
- arbitrary unitary tensor factorizations outside the supplied represented
  amplitude class;
- continuous gauge groups;
- spatial, causal, topological, field, or gravitational localization.

`UNAVAILABLE` and `COLLAPSED` rows remain valid typed negative controls.  They
cannot enter the positive theorem because total implemented multiplication is
one of its stated hypotheses.

---

## 2. Row lemma: the quotient operation is physically typed

For every raw ordered pair `(a,b)`, the validator separately checks:

1. the boundary types and composition context `tau`;
2. the status and presence/absence of result and row law;
3. membership of the result in the operation family;
4. exact carrier and monomial-law well-formedness;
5. gauge equality of supplied `M` with the independently composed input laws;
6. gauge equality of `M` with the result representative;
7. equality of the supplied observed signature with both exact laws.

For an unavailable row, the validator requires `result = M = signature =
None` and returns before any amplitude multiplication.  It therefore cannot
silently turn an unavailable schedule into a synthetic implemented schedule.

Raw aliases are grouped only by boundary type, exact operational signature,
and independent-selectability status.  Every combination of aliases in an
ordered class pair must have the same context, status, quotient result, row-
law signature, and observed signature.  Otherwise the quotient raises
`AccessUnderdetermined`.

Therefore multiplication on quotient classes is a well-defined typed
operation, and each positive quotient row retains an independently supplied
law that was compared—rather than substituted—with physical composition.

---

## 3. Enumeration lemma: every normal subobject is found

Let `G` be the validated finite positive quotient.

For every `g in G`, the estimator constructs the normal closure

\[
N_g=\langle xgx^{-1}:x\in G\rangle.
\]

It starts with the trivial subgroup and all `N_g`, then repeatedly adjoins the
product `HK` of every already found pair of normal subgroups.  In a group,
`HK` is their join whenever `H` and `K` are normal.

Let `N` be any normal subgroup.  Because `G` is finite,

\[
N=\langle n:n\in N\rangle
 =\bigvee_{n\in N}N_n.
\]

Each `N_n` is in the initial family, and a finite join is obtained by finitely
many pairwise joins.  Hence the fixed point contains every normal subgroup.
Every constructed member is normal by induction: normal closures are normal,
and joins/products of normal subgroups are normal.  Thus the returned list is
exactly the finite normal-subgroup lattice at the declared scope.

The join loop increments an explicit counter.  Crossing the frozen cap raises
`RQ0-L0-INVALID`; it never returns a truncated lattice.

---

## 4. Candidate-pool lemma

Suppose `(A_1,...,A_k)`, `k >= 2`, is a normal direct-factor decomposition of
`G`.  For each `A_i`, the product of all other factors

\[
B_i=\prod_{j\ne i}A_j
\]

is normal, commutes with `A_i`, intersects it only in the identity, and the
multiplication map `A_i x B_i -> G` is bijective.  Both `A_i` and `B_i` occur
in the complete normal-subobject enumeration.  Therefore the estimator's
exhaustive complementary-pair scan places every `A_i` in its direct-factor
candidate pool.

Conversely, admission to that pool alone is not a positive factor result.  It
only prevents the later tuple enumeration from considering normal subobjects
that have no direct complement.  Every scientific predicate is replayed on
the complete tuple afterward.

---

## 5. Tuple completeness lemma

The estimator enumerates every unordered tuple of two through eight members
of the complete candidate pool whose order product is `|G|`.  The pin caps the
first finite rung at eight returned factors.  By the candidate-pool lemma,
every admissible normal direct-factor tuple within that bound is among these
combinations.

No supplied generator list, lexical handle, dataset name, hidden partition,
or expected order multiset prunes the combinations.  Ordering is used only to
make deterministic serialized output.  Exceeding the tuple-test cap raises an
invalid result rather than lowering the search.

Thus every eligible tuple in the declared finite normal-direct-factor class
is submitted to the same certificate predicate.

---

## 6. Certificate soundness, predicate by predicate

Let the estimator return a factor certificate for `(A_1,...,A_k)`.  Source
inspection and executable replay establish each required predicate as
follows.

### P1. Independently selectable generation

For every `A_i`, the code takes the classes in `A_i` whose independently-
selectable flag is true and computes their exact subgroup closure using the
validated multiplication and inverse tables.  It compares that closure with
`A_i` as a set.  The flag is therefore read in the scientific predicate.

In particular, composite reachability does not imply independent generation.
If the only selectable member of a nontrivial factor is its identity, the
closure is trivial and P1 fails.

### P2. Mixed implementation in both orders

For every distinct factor pair and every `(a,b)` in their Cartesian product,
the certificate reads the actual quotient rows `(a,b)` and `(b,a)` and
requires status `IMPLEMENTED` on both.  Missing or unavailable rows cannot be
synthesized because the row validator and quotient type carry no law for
them.

### P3. Exact operational commutation

For the same ordered pairs, the certificate requires:

- equal quotient results;
- independently supplied laws present in both rows;
- exact global-`mu_24` gauge equivalence of those laws;
- equal observed operational signatures.

This is stronger than abstract group commutation alone.

### P4. Faithful multiplication

The code enumerates the complete finite Cartesian product

\[
A_1\times\cdots\times A_k
\]

and multiplies each tuple through the validated rows.  It stores the first
tuple producing each result.  A second distinct tuple producing that result
returns the exact two tuples and collision class.  A positive certificate
requires no collision and image cardinality `|G|`.

No probabilistic hashing or sample is used.  Declared `COLLAPSED` status is a
different earlier obstruction and is never reported as this measured
collision.

### P5. Closure and involution

For every factor, the code checks identity membership, inverse membership, and
the product of every ordered element pair.  The same checks are repeated on
every factor product used as a restriction object.

### P6. Typed central/scalar intersection

At this first scope the declared central quotient is the exact identity
subobject.  Each pairwise set intersection must be precisely that singleton.
The represented amplitude algebras are independently required to have exact
intersection dimension one.  Both the operational and represented notions are
therefore typed and measured.

### P7. Represented-algebra product

The exact `Q(zeta_24)` matrices of every factor class generate an exact finite
star algebra.  For every factor pair, the estimator checks matrix
commutation and exact algebra-intersection dimension one.  It computes each
factor-algebra dimension and the ambient algebra dimension by exact row
reduction.  A positive certificate requires

\[
\prod_i\dim\mathfrak A_i=\dim\mathfrak A_G.
\]

Together with commuting scalar intersections and the represented products
already present among the group laws, this is the finite product-algebra
certificate at the declared representation scope.

### P8. Restriction stability

For every nonempty subset of returned factors, the code constructs its exact
product subobject from the faithful coordinate map.  It checks closure,
inverses, every inherited row's implemented status, result membership,
presence of supplied law, and exact row signature.  Later regional arrows are
constructed only between these certified products and replay their complete
row maps.

### Replay

After all candidates are filtered, every returned finest certificate is
recomputed from the serialized dataset, quotient composition object, and
factor sets.  Object equality and `passes` must both hold.  A forged or stale
certificate therefore fails before return.

It follows directly that every returned factor tuple satisfies P1–P8.

---

## 7. Finite soundness theorem

**Theorem.** For every valid input in section 1's scope, every factor tuple
returned by `analyze_addressability` is an independently generated, two-order
jointly implemented, exactly operationally commuting, faithful, closed,
typed-scalar-intersecting, represented-algebra-product, restriction-stable
normal direct factorization of the input's validated quotient composition
object.

**Proof.** The row lemma makes the quotient multiplication and supplied laws
well defined.  The enumeration and candidate-pool lemmas ensure returned
candidates are drawn from closed normal subobjects.  A tuple is appended only
if its certificate's conjunction P1–P8 is true.  Section 6 proves that each
boolean is the stated exhaustive exact predicate on the input rows rather than
a fixture declaration.  The final replay recomputes the certificate.  Hence
every returned tuple has all stated properties.  QED.

---

## 8. Declared finite completeness theorem

**Theorem.** Subject to section 1's type, normality, representation and cap
restrictions, `analyze_addressability` returns every finest tuple of two
through eight commuting normal direct factors satisfying P1–P8.

**Proof.** Section 3 enumerates every normal subobject.  Section 4 puts every
factor of every admissible tuple in the candidate pool.  Section 5 submits
every possible candidate tuple with order product `|G|` to the certificate.
The certificate predicates are necessary by the definition of the target
class and do not consult fixture truth.  Therefore no admissible tuple is
discarded.  The estimator retains all passing tuples and defines “finest” as
maximal factor count, retaining every tied maximum rather than choosing one.
Cap exhaustion raises invalid instead of returning a partial list.  QED.

This is not an assertion that normal direct factors exhaust every physically
meaningful notion of quantum localization.  It is completeness for the exact
first-rung search class engraved above.

---

## 9. Regional and factual map consequences

For any returned factorization, faithfulness gives a unique coordinate tuple
for every operation class.  Dropping coordinates outside a target factor
product therefore defines an executable operation restriction.  The regional
constructor uses that map to transport every source row to the target row and
checks result-square commutation.  It separately maps independent-selection
flags and lifts preparations, contexts, probes, readouts, record candidates,
and gauge actions by their exact structural keys.  Direct and composite maps
are compared field by field.

Record candidates are evaluated by the exact W3 procedure after their readout
and dynamics are frozen.  Their scientific identifiers hash exact projectors,
dynamics, boundary type, and quotient support; record and witness handles are
absent.  Joint factual atoms are exact nonempty intersections of diagonal
projector atoms.  A regional restriction induces the Boolean map that sends a
target atom to the exact union of source atoms refining it.  Exact set equality
proves the projector pullback, and a partition of source atoms proves the
Boolean homomorphism on the full generated algebra.  Generator-projector maps,
identities, composition, and direct/composite naturality are checked.

These consequences are conditional on a fixture supplying valid operational
contexts and W3 records.  They prove the generic map constructors' typing;
they do not predict that the future fixture will pass.

---

## 10. Public falsifiers before freeze

The estimator's public suite is deliberately heterogeneous and contains no
future main truth.  It measures:

- a fully selectable finite product with replayed factor certificates;
- the hostile `S3 x C2` copy in which the full nontrivial `C2` coset is
  composite-only and no positive address factorization survives;
- one declared `COLLAPSED` row, rejected by status;
- one `UNAVAILABLE` row with no supplied result/law;
- a true injectivity collision with the two colliding tuples printed;
- a record-bearing `V4` ambiguity object with three finest factorizations and
  exact arrows connecting every source/target pair;
- a public coprime regional calibration with full `RegAddr`/`Rec` maps;
- row-type, wrong-law, wrong-signature, handle-renaming, serialization, and
  pairwise-valid twisted-triple controls.

These objects can refute an implementation error.  Their success is not used
as a premise in the theorems of sections 7–8.

---

## 11. Four epistemic labels

- **Definition:** the finite typed input, row statuses, address predicates,
  normal-direct-factor search class, regional restriction, and fact interface.
- **Postulate:** complete finite operational tomography/access, independent-
  selectability declarations, exact row laws, contexts, preparations,
  readouts, and finite gauge scope.
- **Theorem:** conditional soundness and completeness within sections 1 and 8.
- **Measurement/control:** public 29-gate calibration receipt and the later
  unseen-fixture results.

No manifold, spatial adjacency, influence, causal order, Lorentzian geometry,
field propagation, stress tensor, or gravity statement follows from this
proof.
