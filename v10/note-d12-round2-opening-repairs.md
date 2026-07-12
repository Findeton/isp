# D12 hostile round-2 residual repairs

**Date:** 2026-07-11  
**Round-2 mathematics:** PASS at narrowed `A_D12` scope  
**Round-2 independent rebuild:** PASS at narrowed scope  
**Round-2 ontology:** MAJOR REVISION with three residual blockers  
**Status:** repaired and frozen for focused round 3.

## 1. Boundary-data eligibility

Round 2 directly mutated a collar's screen, order unit, and frame and found
that the old `eligible` predicate still returned true.  Eligibility now
requires all of:

```text
unconsumed eventless collar;
correct input types;
recorded connected two-owner tuple;
exact emitted opportunity;
unitary frame at the explicitly claimed scope;
correct local order unit;
screen equal to the frame-transported pointer family;
normalized collar state.
```

New exact negative controls reject a permuted screen, rank-one order unit, and
nonunitary diagonal frame, in addition to the prior wrong-type,
disconnected-owner, missing-opportunity, and stale controls.

## 2. Positive-support RN coordinates

The round-2 packet stored atomwise extended logarithms containing
`-infinity` strings and mislabeled them as contrast coefficients.  Those
fields are deleted.

Each packet now stores:

```text
ambient history atoms;
positive_history_support;
finite log_rn_coordinates_on_support of dimension |support|-1.
```

For quarter-iSWAP the positive support is `(1,2)` with one zero contrast
coordinate relative to its conditional uniform reference.  For half-iSWAP
the support is `(2,)` with no nonconstant coordinate.  The ambient atoms,
reference, contrast basis, evidence data, commitment mode, screens, and types
are shared; the positive support and induced law are correctly allowed to
differ.  This is the object that the complete ledger identifies but does not
select.

## 3. Finite local threshold memory

The old `ClassicalCollar` copied the full prefix.  It now contains only:

```text
block_phase in {0,1,2};
block_memory of length at most two;
parent record identifier.
```

The full history remains distributed over immutable `ClassicalRecord` objects
in the history.  Exact checks verify that this finite collar computes the same
conditional as the arbitrary-depth `P_r` block cylinder law at every prefix
through depth 9 for `r=1/2` and `r=1/3`.  Exponential race products reproduce
every tested cylinder, and the formula supplies the arbitrary-depth proof.

## 4. Mathematics review residuals

Paper 13 now displays the arbitrary-`n` formula

```math
P_r^{(n)}=\prod_{j<q}(1+r x_{3j+1}x_{3j+2}x_{3j+3})/8\;2^{-s},
\quad n=3q+s,
```

and proves its adjacent bonding maps.  It also states the finite-poset
adjacent-incomparable-swap lemma: the exact `AB/BA` cell generates
construction-order invariance for any finite schedule whose incomparable
instruments commute.  Overlapping events remain ordered.  Stale exclusion is
stated as a functional-history constructor invariant: only the newly born
collar is exposed as the next live boundary.

## 5. Frozen replacement receipt

```text
checks=142
semantic_receipt=47b5aecd660370264c2e5c377493b70a9e7371880168f2b3f9f04fed936af5ba
stdout_sha256 normal/-O=96df7ed44360c980f9bafbf5e86a792241d774a8995c2303bc3bbf47c8ed6e78
source_sha256=12ca4f04b65351158bdcb9eda3e455baa73340c077cbb604cf1c9582a555e0a6
paper13_sha256=39b42a4af1ab48a2059c18096fb616094583cce4ea26cde2c2e1664a1a741f9f
```

No claim is added outside the finite-packet, unitary-frame,
primitive-process scope.  Nonunitary Lorentz integration, physical selection
of the process, bridge grammar, gravity, scale, and V9 geometry remain open.
