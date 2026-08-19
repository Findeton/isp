# APR Paper 12 pin addendum — regional congruence and canonical boundaries

**Date:** 2026-08-18

**Status:** BINDING PIN ADDENDUM. Frozen after the APR pin and before the APR
generic core.

**Parent pin:** v16/note-apr-pin.md at commit ab41871.

## 1. Reason for the addendum

The first independent hostile design pass found two type errors that must be
removed before construction:

1. a linear history quotient V/kernel(Phi) is not automatically a quotient of
   a Boolean or distributive algebra of regions;
2. a boundary is not minimal merely because deleting one presented label makes
   a partial implementation fail. Predictively duplicate labels must be
   merged.

These corrections sharpen the frozen question. They do not introduce fixture
truth or a preferred outcome.

## 2. Two quotients, permanently distinct

### 2.1 Linear predictive quotient

For a vector/history presentation V with a linear complete-future map Phi,

    Q_lin = V / kernel(Phi)

is a valid linear predictive quotient when the future catalogue is closed
under the registered continuations. This statement concerns history or
boundary vector spaces.

It does not by itself define parthood, meet, join, complement, contact, or an
algebra of physical regions.

### 2.2 Regional contextual quotient

For candidate regions A and B, define

    A ~reg B

only when every licensed one-hole regional context C[-], every compatible
future filling F, and every calibrated stable record Z give the same
prediction after substituting A or B:

    Pred(Z | F o C[A]) = Pred(Z | F o C[B]).

The context catalogue must include every operation whose descent is claimed:
meet, join, complement or relative complement, boundary gluing, disjoint
tensor, passive refinement, and every registered continuation.

The physical region quotient exists only if ~reg is a congruence for those
operations. APR must check:

- A~A' and B~B' imply A meet B ~ A' meet B';
- likewise for join;
- A~A' implies complement(A) ~ complement(A');
- contact and causal predicates are invariant or explicitly priced;
- gluing representatives gives equivalent composites;
- passive refinements descend to identity classes.

If these fail, the unit returns

    APR-BLOCKED-AT-REGIONAL-CONGRUENCE

rather than calling a set of equal profile numbers a region algebra.

## 3. Mandatory volume-only counterexample

Let the candidate atomless prefix algebra contain the disjoint regions [0] and
[1]. The scalar profile

    Phi(A) = mu(A)

assigns both value 1/2. But the regional context C[-]=[-] meet [0] gives

    Phi(C([0])) = 1/2,
    Phi(C([1])) = 0.

Thus equality under a restricted scalar profile is not a regional congruence.
The APR scorer must reject any construction that forms a physical region
quotient from this profile alone.

The positive complete-probe candidate

    Phi(A)(B) = mu(A meet B) for every licensed B

still has to prove contextual closure. Its faithfulness makes equality
trivial in the proposed model, but that conclusion must be generated rather
than copied into the scorer.

## 4. Canonical predictive boundary

A boundary presentation carries a map to its complete future behavior.
The physical predictive boundary is the quotient by equality of complete
future behavior, equipped with the following universal property:

> Every sufficient boundary map factors uniquely through the predictive
> quotient, up to the registered natural isomorphism and null directions.

At finite linear scope this is represented by row/column space or a canonical
rank factorization. At a configuration scope it is the set of complete-profile
equivalence classes. Neither representation is ontology by itself.

Deletion-minimality is not sufficient. The mandatory negative control has two
reachable boundary labels with identical constant future profiles. Removing
one literal label makes a naive partial lookup fail, but the canonical boundary
must merge them into one class.

APR may say MINIMAL-AT-CATALOGUE only when:

- the future catalogue and contextual closure are stated;
- duplicate classes are merged;
- every sufficient presentation factors through the quotient;
- a lossy coarsening moves a generated held-out future prediction;
- an appended legal continuation either factors through the same quotient or
  explicitly demotes the earlier completeness claim.

## 5. Binding changes to the parent pin

The parent pin is read with these substitutions:

- APR-T3 concerns congruence of the complete contextual regional profile, not
  a bare linear kernel.
- APR-T5's uniqueness is the universal-property uniqueness above.
- K2 also fires when a linear quotient is promoted to a regional algebra.
- K5 also fires when gluing is not well-defined on regional equivalence
  classes.
- D7 must distinguish extension of a linear future map from extension of the
  contextual regional catalogue.
- the outcome ladder inserts APR-BLOCKED-AT-REGIONAL-CONGRUENCE immediately
  after APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS.

New orthogonal receipt coordinate:

    regional_quotient =
      PROFILE-EQUIVALENCE-ONLY |
      CONGRUENCE |
      INCONSISTENT

No APR positive physical-referent rung is reachable unless the coordinate is
CONGRUENCE.

## 6. Ontology consequence

This is not bookkeeping. A vector direction and a region have different
referents. Quotienting amplitudes that no future test can distinguish does not
automatically tell us which bounded relational facts are the same.

APR earns a physical regional ontology only when the law's contextual
indistinguishability respects all regional and compositional operations. Until
then it has a predictive vector quotient and a candidate region syntax, not a
physical region algebra.
