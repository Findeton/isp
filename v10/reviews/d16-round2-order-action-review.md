# D16 round-2 order-theory/action repair review

**Date:** 2026-07-11  
**Verdict:** **PASS AT THE FROZEN FINITE NONSELECTION SCOPE**  
**Formal status:** `INCOMPLETE-INVESTIGATION`

## Decision

All round-one blockers are repaired. Typed, owned, disjoint and extremal
boundaries replace integer-only boundary sets. Quotient gluing matches
future/past ports by `(kind,owner)`, rejects mismatches, retains external
boundaries and is relabeling covariant. Exact weights use `Fraction`. The
common-phase test uses full vectors, and the sewn three-chain exposes
`beta_1`, giving 16 signatures for 16 binary packets.

No blocker remains for the finite theorem: poset relabeling covariance plus
interval-count dependence does not select a unique binary coefficient packet.
This does not provide a quantum measure, growth law, D14 records, BDG packet,
continuum dimension, cones, scales or `G`.

## Reproduction

```text
861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37  source
8882ce9ff680336ef747fefe500f9d9927d6b273081017faa09fb932c2423640  JSON
152d65ec1ff037238b9a486a3012479b818ffdff3d09c30b9eb2f450cbc553f2  theorem
faaf2cc9c468ca2be0195f208e569f599d7ac9a38949a74282af7527f6ac4101  receipt

checks                         26/26
normal stdout SHA-256          bbc674b8052e7e1a7ca9aca438f82eb2cd644b1ee82cb8c0ada392b43fc6e037
optimized stdout SHA-256       bbc674b8052e7e1a7ca9aca438f82eb2cd644b1ee82cb8c0ada392b43fc6e037
semantic SHA-256               a3931af2f999a7381b86792f03750420c3be411d83c7a0598cb6dfe6eb9e10a6
```

Normal and optimized output are byte-identical. No Python `assert` supplies a
gate.

## Opening disposition

```text
O1 numeric gluing failure                 CLOSED
O2 boundary type/owner/extremality        CLOSED
O3 insufficient common-phase gate         CLOSED
O4 floating exactness                     CLOSED
O5 beta_1 invisibility                    CLOSED
O6 linear-extension overclaim             CLOSED BY NARROWED WORDING
O7 automorphism convention ambiguity      CLOSED AS EXTRA MEASURE DATA
O8 dimension overread                     CLOSED IN SCOPE
```

## Boundary and gluing audit

`BoundaryPort(element,kind,owner)` is now required. Boundary elements must be
unique, typed, owned, pairwise incomparable, disjoint across past/future, and
minimal/maximal on the appropriate side. The former nonminimal and overlap
counterexamples reject.

`glue_typed` identifies equal `(kind,owner)` keys, rejects unequal or duplicate
key sets, copies both orders, takes transitive closure and returns left-past
and right-future boundaries. The canonical quotient has:

```text
intervals (2,1,0), automorphisms 1, linear extensions 1.
```

I tested all four identity/swap combinations independently on the two inputs.
Every output has those invariants and matching typed external boundaries up to
element renaming. This includes the one-sided swap that produced Lambda in
round one. The built-in receipt checks the simultaneous swap; exhaustive
one-sided coverage is a useful future regression addition, not a blocker.

The quotient has one cross `N_1` interval. Recomputing its action once gives
one, while naive left-plus-right addition gives zero. The gluing obstruction
is now covariant and exact.

## Relabeling and counts

Every relabeling of the five original orders preserves interval counts,
action values and boundary metadata. Typed owners reduce the V and Lambda
automorphism groups, giving the correct counts:

```text
automorphisms       24,1,1,1,2
linear extensions  24,1,2,2,2.
```

The linear-extension check still repeats the same whole-order phase rather
than computationally transporting an extension. The theorem now claims only
that a scalar defined on the completed order ignores its presentation. That
follows by definition and from exhaustive relabeling; no growth measure or
transition law is inferred. The former overclaim is closed.

## Coefficients and common phase

The frozen domain is

```text
alpha,beta_0,beta_1,beta_2 in {0,1}, phase=(-1)^S.
```

Adding the sewn chain with odd `N_1` produces 16 distinct signatures for all
16 packets. No binary direction is invisible.

For `S_A=N_0` and `S_B=N_2`, the source computes the full action-difference
and phase-ratio vectors over all six orders and requires each to be
nonconstant. This is exactly the criterion missing in round one. The finite
census is binary-parity only; nonselection of the larger real family follows
because it contains these two examples.

## Exact measure and dimension scope

Normalization and illustrative orbit weights are exact fractions:

```text
two-history masses (1/2,1/2), chain weight 1, antichain weight 1/24.
```

The theorem treats the orbit convention and alternative set as extra measure
data; it does not infer a quantum measure from phases. Dimension tags remain
input metadata, and no BDG or emergence claim is made.

## Gate disposition

```text
C0 PASS for the declared strict typed-boundary class.
C1 PASS for orders and typed quotient gluing.
C2 PASS at intrinsic interval scope.
C3 PASS for finite binary nonselection.
C4 NOT EXERCISED; no BDG packet claimed.
C5 PASS for the finite quotient/cross-interval cell.
C6 PASS as an exact refusal, not a quantum measure.
C7 OPEN; no D14 record bridge.
C8 PASS as a whole-order presentation statement.
C9/C10 OPEN; V9 correctly withheld.
C11 OPEN beyond this mathematics stream.
```

## Final verdict

**PASS AT THE FROZEN FINITE NONSELECTION SCOPE.** All round-one mathematical
blockers are repaired and 26/26 reproduces. Preserve
`INCOMPLETE-INVESTIGATION` for the unbuilt measure, record, continuum,
geometry and empirical gates.
