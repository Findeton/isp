# D16 hostile round-1 order-theory/action review

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**  
**Formal status:** `INCOMPLETE-INVESTIGATION`

## Decision

The narrow nonselection statement is correct: interval counts are relabeling
invariants, and `S_A=N_0` and `S_B=N_2` have a nonconstant relative phase on
the five frozen orders. Covariance plus interval-count dependence therefore
does not select unique coefficients.

The 20-check receipt reproduces, and the displayed interval, automorphism and
linear-extension counts are correct. Hostile PASS is blocked by four exact
defects:

1. `glue_at_last_first` glues numeric indices, not declared boundaries.
   Relabeling one input changes the result from a chain to a Lambda order.
2. Boundaries have no types or owners, may overlap past/future, and need not be
   minimal/maximal collars.
3. Normalization and orbit weights use binary floats, not exact rationals.
4. The common-phase gate checks one unequal value, not class-wide relative
   phase.

The coefficient and construction-order censuses also need hardening. These
defects do not refute nonselection, but they block C0/C1/C3/C5 and the claimed
exact regional receipt.

## Reproduction

```text
a37fbbbc23f153b58aa65ae43e0e1c6472777588d7c22df50f3d0eed5c7593f6  protocol
b24a4c511dd4e82bf900d0dd0e66a07ee7d160c614ec675b8c3dbb235a8510bc  theorem draft
989f996af855daceffa8bff68d687ada60ab4f35a1736b76e6c0508156f7e386  source
d6b6efa782750bfcd59b79e8ebc849b2c82ae7daeb64027bef186fbf10a70ec0  JSON packet
59b6374544a0817dc3bb5507053eb104008625e312a6d7d14b3de0319e415cec  receipt

checks                         20/20
normal stdout SHA-256          212df3c028e0fa7387170ba14dce541e868983e75c6a09c8bf6cb735635424ef
optimized stdout SHA-256       212df3c028e0fa7387170ba14dce541e868983e75c6a09c8bf6cb735635424ef
semantic SHA-256               107bedcdc071c0be21edc12aa928dc57fd45416206d4049ad643aa67712dd04f
```

Normal and optimized stdout are byte-identical. No Python `assert` supplies a
gate. The findings concern what the checks establish.

## Blocker ledger

```text
O1 MAJOR    gluing fails relabeling covariance.
O2 MAJOR    typed, owned and extremal boundary semantics are absent.
O3 MAJOR    common-phase inequivalence gate is logically insufficient.
O4 MODERATE exact normalization and automorphism weights use floats.
O5 MODERATE beta_1 is invisible on the signature carrier.
O6 MODERATE the linear-extension phase gate is tautological.
O7 MODERATE 1/|Aut| is one measure convention, not uniquely forced.
O8 MINOR    dimension tags are metadata, not BDG provenance.
```

## 1. Strict orders and boundary semantics

The strict-order constructor is sound: square, irreflexive, asymmetric and
transitively closed finite relations are required. Cycles and missing
transitive pairs reject.

Boundary validation is incomplete. `past_boundary` and `future_boundary` are
only integer tuples. The constructor checks range, uniqueness and antichain
status, but stores no type, owner or collar data and imposes no extremality or
overlap rule.

Two hostile examples admit exactly:

```text
one point in both past_boundary and future_boundary;
the middle point of a three-chain declared as past_boundary.
```

An overlap could be legal for an explicitly defined identity region, but no
such convention exists. Calling the range check “boundary ownership” is
incorrect because ownership is absent.

Repair O2 by adding typed, owned boundary ports and declaring disjointness,
extremality and any identity exception. Add wrong-type, wrong-owner,
nonminimal-past, nonmaximal-future and overlap controls.

## 2. Relabelings, automorphisms and extensions

`permute` correctly transports the relation and boundary membership. All
`n!` relabelings are genuinely exhausted for the five orders. The exact
counts are correct:

```text
intervals: antichain4 (0,0,0,0), chain4 (3,2,1,0), diamond4 (4,0,1,0)
automorphisms: 24,1,2,2,2
linear extensions: 24,1,2,2,2
```

The construction-order gate is nevertheless tautological:

```python
{action_a.phase(order) for _ in order.linear_extensions()}
```

It repeats one unchanged value and never uses an extension. The earlier
relabeling test already implies phase invariance, so the prose conclusion is
true. Repair O6 by transporting each natural labeling and comparing phases.
Keep linear extensions, natural labelings modulo automorphisms, and growth
histories conceptually distinct.

## 3. Exact gluing counterexample

For canonical two-chains `0<1`, current gluing yields a three-chain:

```text
intervals (2,1,0), automorphisms 1, extensions 1.
```

Relabel only the left input by swapping `0` and `1`. The same function still
identifies numeric `left.n-1` with right index `0`, so the output is Lambda:

```text
relations 1<0 and 1<2
intervals (2,0,0), automorphisms 2, extensions 2.
```

The outputs are nonisomorphic. Thus isomorphic presentations produce
different glued histories. C1 and C5 fail.

The conceptual cross-interval point remains correct: covariantly identifying
a future endpoint with a matching past endpoint creates one `N_1` interval.
The implementation does not identify those boundaries covariantly.

Repair O1 by gluing explicit boundaries through a type/owner-preserving
bijection, carrying unconsumed external boundaries, and taking closure. Test
all independent input relabelings. Account separately for the shared point in
`alpha|C|`, internal intervals, cross intervals and boundary/corner terms.

## 4. Interval counts and coefficient census

The definition of `n(x,y)` and `N_k` is implemented correctly. Comparable
pairs are causally oriented and counted once.

The census is exactly the binary parity subclass

```text
alpha,beta_0,beta_1,beta_2 in {0,1}, phase=(-1)^S,
```

with 16 packets and eight signatures. It is not exhaustive for unrestricted
integer or real coefficients, though two subclass members suffice to prove
nonselection of the larger family.

`beta_1` has no phase effect on the five signature orders because their
`N_1` values are zero or even. The three-chain has odd `N_1` but is excluded
from signatures. Repair O5 by explicitly freezing the coefficient domain,
adding a correctly glued odd-`N_1` carrier, and printing the kernel and phase
equivalence classes of the coefficient-to-signature map.

## 5. Phase inequivalence

The actual phase pairs are

```text
antichain4 (+,+), chain4 (-,-), V3 (+,+), Lambda3 (+,+), diamond4 (+,-).
```

The relative phase `(+,+,+,+,-)` is nonconstant, so the selected actions are
not related by one common phase. The theorem conclusion is true.

The executable checks only `S_A(diamond) != S_B(diamond)`. Actions differing
by a nonzero common constant also pass that check. Repair O3 by evaluating the
relative phase on every frozen order and requiring more than one value, or by
requiring `S_A-S_B` nonconstant modulo the phase period.

## 6. Automorphism measure and normalization

Python `/` makes both `1/|Aut|` and normalized Born weights binary floats.
Comparisons to `1/24` and `0.5` repeat the same float expressions. Replace
them with `fractions.Fraction`.

Also declare the measure convention. An unlabeled sum can mean unit weight per
isomorphism class, groupoid weight `1/|Aut|`, or a labeled sum divided by
`n!`. Relabeling invariance alone does not select one.

Two unit phases have raw counting-measure mass two. Uniform probability after
division additionally assumes those two alternatives, their measure and a
decoherent/orthogonal interpretation. The draft correctly denies that phases
alone define a quantum measure; preserve this ceiling.

## 7. Dimension and theorem scope

`dimension_tag=2` and `dimension_tag=4` are metadata attached to arbitrary
beta tuples. This is not a BDG coefficient, normalization, scale or continuum
test. The draft admits this; rename the check as a provenance refusal.

The exact result currently supports only:

> On five named strict orders, interval counts and their actions are
> relabeling invariant. In the binary parity subclass, `N_0` and `N_2` have
> nonconstant relative phase. Covariance and interval dependence therefore do
> not select a unique action.

It does not yet establish a covariant typed gluing operation, boundary
category, exact orbit/quantum measure, growth law, D14 records, published BDG
packet, continuum dimension, cone, unit or `G` prediction.

## Gate disposition

```text
C0 PARTIAL/FAIL strict orders pass; typed/owned/extremal boundaries absent.
C1 PASS for interval actions; FAIL for gluing.
C2 PASS in prose at intrinsic interval scope.
C3 PASS for existence nonselection; census/equivalence gate needs repair.
C4 NOT EXERCISED; dimension is metadata.
C5 FAIL; gluing is presentation-dependent.
C6 PASS as a refusal; exact rational illustration needs repair.
C7 OPEN; no causal-order/matter D14 record cell.
C8 PASS in prose; executable extension gate is weak.
C9 OPEN; V9 correctly withheld.
C10 OPEN; no two complete predictive candidates.
C11 OPEN; round-one review finds major repairs.
```

## Required repair order

1. Implement typed boundary-bijection gluing and exhaust input relabelings.
2. Add boundary types, owners and extremal/overlap semantics.
3. Replace the common-phase gate with a class-wide relative-phase test.
4. Use `Fraction` and declare the orbit-measure convention.
5. Add an odd-`N_1` carrier and print coefficient degeneracies.
6. Make the linear-extension gate use natural labelings.
7. Keep dimension, measure, records and geometry outside the theorem until
   their dedicated gates exist.

## Final verdict

**MAJOR REVISION.** The narrow coefficient-nonselection conclusion is correct
and 20/20 reproduces. Regional gluing is not relabeling covariant, boundary
semantics do not match the frozen class, and several exact gates are
float-based or logically insufficient. Preserve `INCOMPLETE-INVESTIGATION`
and repair this ledger before freezing an executable regional theorem.
