# D2 hostile review, round 2: ontology, locality, and category scope

**Referee:** independent hostile ontology/locality audit  
**Date:** 2026-07-11  
**Verdict:** **PASS WITH REQUIRED SCOPE CORRECTIONS**

No further D2 computation is required for the finite marked-support theorem.
Several headline sentences must still be corrected before Paper 3 is frozen,
because they promote the support-skeleton result to “diamond” or
“factorized-record” scope.

## Frozen artifacts reviewed

- `v10/note-d2-primitive-carrier-amalgamation.md`
- `v10/code/d2_marked_diamond_amalgamation_exact.py`
- `v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md`

Hashes executed in this review:

```text
c1cddaf5bd9785ce73f2fc035852e13c7b2f95c1063a5ec3c3211889f017fc36  note-d2-primitive-carrier-amalgamation.md
3a09225eee20888aea932fab191e4c4f3003654e60bb79ab02585f5b1df37891  d2_marked_diamond_amalgamation_exact.py
509ae3821bc90d01bf2a4d378c060d600d5edf700c6af802b07d256b1025df98  relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

The repaired receipt reproduces **33/33** exact checks.

## Round-1 major findings: disposition

### M1 — Support hypergraph versus sealed diamond: CLOSED at skeleton scope

The paper now explicitly defines a **marked support skeleton** and lists what
it forgets: the complete probability law, screens, collar response,
transports, and holonomy. It says that positive D2 results concern marked
support incidence and that a full-diamond law inherits a negative closure
theorem only if it descends to this skeleton.

That conditional statement is honest. No faithful or conservative abstraction
from full sealed diamonds has been proved, and the paper no longer claims one
in its formal claims/nonclaims.

### M2 — Typed and marked spans: CLOSED

The new receipt contains:

- `MarkedSystem` objects with port/interface type and stable
  provenance/ancestry colors;
- explicit interface, left object, right object, and two legs;
- injective leg validation;
- general mark-preserving weak support homomorphisms;
- a quotient pushout with canonical maps;
- rejection of incompatible marks;
- marked canonical signatures.

Marks are load-bearing. Red/blue provenance rejects the crossed matching, and
`root:R1` maps to `R1` ancestry ports but not an `R2` port.

### M3 — Universal property and iterated pushouts: CLOSED

The proof of Proposition 4.1 is valid in the chosen weak-homomorphism category.
The receipt supplements it by exhausting all valid cocones into one audit
target and checking the unique mediator. It also executes both genuine
iterated typed pushouts of one three-object chain and compares marked
isomorphism signatures. The construction-order result is now more than
associativity of preidentified set union.

### M4 — Bare-state closure scope: PARTLY CLOSED; wording repair required

The note's A4 correctly says “refusal to join an edgeless two-record history.”
The abstract also says “two isolated records.” The executable census remains a
bare pair-edge census, as it should.

Paper 3 nevertheless reverts to **“factorized two-record refusal”** in Theorem
7.1, its proof, Proposition 10.2, the claims list, and several summaries. No
probability law or factorization test occurs in that census. An edgeless marked
support skeleton is not logically equivalent to a factorized record law.

This is a scope error, not an arithmetic failure.

**Required correction:** replace “factorized refusal” in the pair and
stochastic theorems by “edgeless/isolated two-vertex refusal in the bare
support skeleton.” If a probability-factorization theorem is desired later,
it needs a different marked-law receipt.

### M5 — Stochastic symmetric choice: CLOSED

The revision now distinguishes deterministic invariance from covariance in
law. It exhibits the unique symmetric one-pair kernel

$$
P(AB)=P(AC)=P(BC)=1/3
$$

and correctly reports that it is covariant but fails the frozen strong pair
restriction gate: the retained named pair has inherited edge probability
`1/3`, whereas the isolated two-vertex rule requires zero.

This does not rule out a non-natural stochastic bridge law. The paper calls
the kernel additional dynamics and scopes the refusal to the frozen strong
restriction gate, which is correct.

### M6 — Root and ancestry semantics: CLOSED conditionally, with one wording caveat

Ancestry provenance now affects interface admissibility in T6. The root
projection control still uses the unmarked `SupportSystem`, but Section 11
begins by **supposing** a supplied root event and explicitly says neither
restriction derives the root. Thus the calculation may be read as the
consequence of two alternative support projections on a supplied
root-provenance hyperedge.

It is not evidence that `r` is dynamically a root or that `a,b` are descendants.
The phrase “the descendants inherit” should therefore remain conditional or be
replaced by “the retained vertices carry the intersection shadow.” The paper's
conclusion that the root law remains open is honest.

## Current category and locality assessment

### The category is explicit but chosen

Weak support homomorphisms allow a support to collapse to one vertex and
require every image retaining at least two vertices to be a target support.
This choice makes the displayed finite pushouts and empty coproduct work. It is
not derived from sealed-holonomy physics, and another morphism category could
have different colimits.

The paper calls it the finite marked-support category and limits the theorem to
that category. That is sufficient. It must not imply that the category is the
unique physical category of sealed diamonds.

### Fixed-span conditionality is now correct

The interface object and both injective mark-preserving legs are supplied.
Indistinguishable marks permit two legal nonisomorphic pushouts; distinguishing
marks can reject one matching. This establishes exactly the intended
boundary:

> the universal property selects a pushout of a supplied span; it does not
> select the interface, its legs, or the marks that make one leg admissible.

### Locality remains interface-relative

D2 contains no emergent metric or propagation law. “Local” means local to a
supplied finite interface. The paper states this explicitly and makes no
relativistic locality or no-signaling claim.

## Remaining required scope corrections

### R1 — Replace the residual full-diamond headline

The formal body and claims list say “marked support skeleton,” but the boxed
abstract verdict still says:

> typed diamond amalgamation gives canonical conditional composition.

The conclusion similarly says that composition of two sealed record diamonds
can be canonical. D2 has proved only the pushout of their proposed marked
support skeletons; it has not glued their probability laws, screens, collars,
transports, seals, or holonomies.

Required wording:

> a supplied typed span has a canonical conditional pushout in the marked
> support-skeleton category.

The sentence claiming a “precise conditional form” of v6 overlap/sheaf and
artificial-seam cancellation should likewise say **incidence shadow** or
**support-level analogue**. No source/collar cancellation is executable here.

### R2 — State the full-history primitive-law fork with its required structure

The newly added fork is conceptually correct: if a probability law on variable
marked histories, including its extension domain, is primitive, then that law
rather than D2 supplies carrier probabilities.

Strictly, a bare path-space measure does not automatically provide a unique
pointwise expression `P(next|H)`. One also needs a specified history
sigma-algebra/filtration or extension relation, existence of a regular
conditional distribution, and an understanding of “next” compatible with
construction-order gauge. Conditional kernels are generally determined only
almost surely.

Required wording: say that a primitive variable-history measure **together
with its extension/conditioning structure** supplies an almost-sure kernel on
candidate one-extension classes. This preserves the intended fork without
reintroducing a physical global commit order.

### R3 — Qualify the birth-refusal conclusion by the frozen axioms

The statement “a first carrier requires an additional root/bridge-sector law”
is defensible only within the frozen alternatives:

- ordinary support-union pushout;
- bare support closure;
- strong induced-restriction naturality;
- isolated two-vertex refusal;
- deterministic selection, or the tested uniform stochastic kernel.

A primitive full-history measure, a non-natural stochastic kernel, richer
marks surviving restriction, or a different derived restriction ontology is
not ruled out. These are still additional law/structure, so the architectural
lesson survives.

Add “under the frozen support-skeleton axioms” to the abstract and conclusion
where birth is said to be refused or to require a root/bridge sector.

## Restriction-semantics audit

This portion now passes.

- Intersection/shadow and contained-event restriction are defined separately.
- The two surviving intersection fill predicates are asserted exactly.
- All 256 contained fill predicates are enumerated.
- Covariance, monotonicity, and empty refusal leave four contained rules;
  adding isolated-component refusal still leaves three.
- The paper explicitly says the corpus has not selected the physical
  restriction ontology.

The higher-support theorems remain limited to the frozen fill-predicate class,
not arbitrary marked-history dynamics. The paper's wording should retain that
scope.

## Full-history primitive-law fork

With R2 applied, the fork is sound:

1. **Primitive-law program:** posit the full variable-history law and its
   conditioning/extension structure. Carrier birth is already one marginal of
   that law; D2 is then a representation/consistency test.
2. **Derivation program:** ask sealed record structure to determine the
   candidate-event domain and the full law. D2 shows that ordinary conditional
   support-skeleton pushout does not perform that derivation.

D2 does not decide which foundational program is correct.

## Precise surviving claim ceiling

After R1-R3, the strongest defensible result is:

> In the chosen finite category of marked support skeletons and
> mark-preserving weak support homomorphisms, every supplied span with
> injective legs has a support-conserving pushout unique up to marked
> isomorphism. Compatible supplied spans compose independently of
> parenthesization. The universal property does not select its interface or
> legs. In the separate bare pair-graph closure class, strong induced-
> restriction naturality plus fixed isolated two-vertex states forces the
> identity closure. Frozen higher-support fill predicates remain nonunique and
> depend on intersection versus contained restriction. Deterministic symmetric
> one-pair selection is impossible, while the unique uniform stochastic
> one-pair kernel is covariant but fails that same strong restriction gate.

It is not defensible to promote this to:

- a pushout theorem for complete sealed-diamond laws;
- a faithful or conservative diamond-to-skeleton abstraction theorem;
- a universal carrier-birth no-go;
- a probability-factorization theorem;
- a derivation of the interface, its marks, or its legs;
- a root/branch or bridge nucleation law;
- a unique restriction ontology;
- relativistic locality or no-signaling;
- a continuum or marked-profinite theorem;
- or a final interacting click law.

## Opening ledger before final verification

No new receipt is mandatory for the current finite theorem. The required
repairs are scope corrections:

1. **D2-R2-O1:** replace residual “typed diamond composition” and v6
   cancellation language by “marked support-skeleton pushout/incidence
   analogue.”
2. **D2-R2-O2:** replace “factorized refusal” by the exact edgeless/isolated
   bare-skeleton axiom.
3. **D2-R2-O3:** state the primitive full-history fork using an explicit
   extension/conditioning structure and almost-sure conditional kernel.
4. **D2-R2-O4:** qualify root/bridge birth refusal by the frozen
   support-skeleton and strong-restriction axioms.
5. **D2-R2-O5:** keep common-root “inheritance” conditional on a supplied
   ancestry mark; the executable restriction itself proves only a hyperedge
   shadow/drop statement.

An optional future campaign could enrich the closure census with marked
boundary laws that survive restriction. That is not needed to publish D2's
present support-skeleton theorem, but it would be required for a record-level
no-bootstrap theorem.

## Final recommendation

The round-1 ontology defects are substantively repaired. The category theorem,
typed leg dependence, construction-order result, restriction-family result,
and deterministic/stochastic distinction now survive hostile review.

Apply R1-R3 and the associated terminology corrections, then freeze Paper 3
at the marked support-skeleton claim ceiling. The remaining question—what
physical law supplies or derives the typed span—is correctly left open.

## Final verification addendum

**Independent recheck:** 2026-07-11  
**Verdict:** **PASS at the finite marked-support-skeleton scope, subject to one
remaining minor phrase correction**

The post-review artifacts were inspected and the production receipt rerun.
D2 remains **33/33** exact checks. The reviewed hashes are:

```text
edd7c62e5424ed4143f219432758489f2c1bf40f9310fd9b82d88f6cd82975a1  note-d2-primitive-carrier-amalgamation.md
bf8e9a749dc961978263fb787ac059567467890f204d5a9b1e39bf94235300e8  d2_marked_diamond_amalgamation_exact.py
98fc7d8d58f13b43a65cc02b04f8e988feb8305093ed24ab8dfec2f822971b23  relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

The five requested scope repairs are verified:

1. **Headline:** the boxed verdict now says “typed marked-support
   amalgamation,” and the conclusion says only that support incidence of
   supplied sealed diamonds composes canonically. Full
   probability/collar/transport gluing is explicitly separate.
2. **Pair axiom:** note, code, theorem, proof, stochastic statement, claims,
   and conclusion now use the exact edgeless/isolated two-vertex
   support-skeleton axiom rather than probability factorization. G9's output
   is correspondingly renamed.
3. **Primitive-history fork:** Paper 3 now supplies
   `(\Omega,\mu,\mathcal F_n)`, requires existence of the relevant regular
   conditional law, defines `Ext_\mu(H)` through its support, and treats the
   carrier as a mark marginal. This correctly describes a primitive-law fork,
   not a derivation by D2. The filtration/extension presentation is part of the
   primitive structure and should not be reinterpreted as a derived physical
   global order.
4. **Frozen-axiom refusal:** abstract, receipt verdict, and conclusion qualify
   first-carrier refusal by the frozen support-skeleton, strong-restriction,
   and edgeless-pair axioms. A non-natural stochastic law or richer full-history
   measure is not claimed impossible.
5. **Supplied root:** Section 11 now begins with a supplied root event and
   ancestry provenance, says both projections are conditional on that supplied
   mark, and explicitly refuses derivation of the root. T6 independently makes
   ancestry provenance load-bearing in interface admissibility.

One sentence still exceeds the executable ontology. The abstract says that
the marked-support pushout

> recovers a precise conditional form of the v6 overlap/sheaf and
> artificial-seam cancellation principles.

No probability sheaf, collar cochain, source, or seam-cancellation law is
represented. Replace this by:

> gives a support-incidence shadow/analogue of those conditional composition
> principles.

This is a wording correction only; it does not require another receipt or
alter any theorem. With that edit, D2 has no remaining ontology blocker at its
stated finite marked-support-skeleton claim ceiling. The unresolved physical
opening remains the derivation or positing of the typed span and the full
variable-history law.

## Closure confirmation

**Final recheck:** 2026-07-11  
**Final ontology verdict:** **PASS — D2 closed at the finite marked-support-
skeleton scope**

The last outstanding sentence is corrected. The abstract now calls the result
a **finite support-incidence analogue** of the v6 overlap/sheaf and
artificial-seam principles and immediately states that it does not model their
probability, collar, source, or holonomy data. This exactly matches the
executable ontology and the paper's formal nonclaims.

Reviewed final Paper 3 hash:

```text
fcdbd17dc7abdbd9a272749e27b8dd5c8b65a73c186722cb9e302acdf49240bd  relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

No D2 ontology or locality correction remains open. The next question is a new
investigation, not a repair: what physical law supplies or derives the typed
span and the full variable-history measure.
