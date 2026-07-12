# D16 hostile review, round 2: independent clean-room verification

**Referee:** independent reconstruction/reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **PASS FOR THE FINITE INTERVAL-ACTION NONSELECTION THEOREM**  
**Formal D16 status:** **`INCOMPLETE-INVESTIGATION`**

The repaired D16 receipt is reproducible and all round-1 clean-room openings
are materially closed.  Normal and optimized Python pass 26/26 with
byte-identical stdout.  Source, generated packet, semantic object, and receipt
hashes agree with current bytes.

Independent adversarial probes establish more than the source's direct cells:

- all four combinations of independently relabeling the left and right
  two-chain regions produce the same typed sewn-order interval counts,
  automorphism count, linear-extension count, and external boundary marks;
- wrong boundary type and wrong owner reject separately;
- nonminimal past, nonmaximal future, and past/future overlap reject;
- all 16 coefficient packets have 16 distinct phase signatures on the expanded
  six-order census;
- the complete action-difference and phase-ratio vectors are nonconstant;
- normalized weights and orbit factors are exact `Fraction` values.

The finite theorem is therefore established: poset relabeling covariance and
intrinsic interval-count dependence do not select one action in the frozen
binary family.  The claim remains deliberately narrower than continuum
diffeomorphism covariance, BDG coefficient selection, a quantum measure,
records, geometry, units, or gravity.

One documentation-only hardening remains: the semantic JSON's `orders` field
lists the five base orders, while `distinct_phase_signatures=16` is computed on
those five plus the sewn three-chain.  The source, theorem, and receipt expose
the sewn order, so this is not a mathematical or reproducibility blocker; a
final packet should rename the field `base_orders` or add
`signature_orders:[...,"sewn_chain3"]`.

## 1. Reproduction

### Commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d16_covariant_causal_action_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d16_covariant_causal_action_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d16_covariant_causal_action_exact.py | shasum -a 256
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d16_covariant_causal_action_exact.py | shasum -a 256
shasum -a 256 v10/code/d16_covariant_causal_action_exact.py
shasum -a 256 v10/data/d16-covariant-causal-action-exact.json
```

Both direct executions completed with identical labels and ended in:

```text
PASS 026: pre-final exact check count is frozen
CHECKS PASSED: 26/26
SEMANTIC SHA256: a3931af2f999a7381b86792f03750420c3be411d83c7a0598cb6dfe6eb9e10a6
SOURCE SHA256: 861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
VERDICT: INTERVAL-ACTION-FAMILY-NONSELECTING
```

Complete stdout hashes:

```text
normal  bbc674b8052e7e1a7ca9aca438f82eb2cd644b1ee82cb8c0ada392b43fc6e037
-O      bbc674b8052e7e1a7ca9aca438f82eb2cd644b1ee82cb8c0ada392b43fc6e037
```

Authoritative hashes:

```text
861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37  source
8882ce9ff680336ef747fefe500f9d9927d6b273081017faa09fb932c2423640  packet
a3931af2f999a7381b86792f03750420c3be411d83c7a0598cb6dfe6eb9e10a6  semantic
```

I independently selected the eight semantic fields and reproduced the compact
sorted JSON digest `a3931af2...`.  Every value in `d16-pre-review-receipt.md`
matches current execution and bytes.

No Python `assert`, optimization-dependent branch, random input, external
package, floating calculation, or packet self-read supplies a gate.

## 2. Adversarial probe driver

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/d16_round2_adversarial_probes.py
```

Focused output:

```text
glue relabel pair id/id       ((2,1,0),1,1,outer-past,outer-future)
glue relabel pair id/swap     ((2,1,0),1,1,outer-past,outer-future)
glue relabel pair swap/id     ((2,1,0),1,1,outer-past,outer-future)
glue relabel pair swap/swap   ((2,1,0),1,1,outer-past,outer-future)
wrong type REJECTED typed owned gluing boundary mismatch
wrong owner REJECTED typed owned gluing boundary mismatch
nonminimal past REJECTED past boundary must be minimal
nonmaximal future REJECTED future boundary must be maximal
past/future overlap REJECTED past and future boundaries must be disjoint
packet/signature counts 16 16
full differences (0,2,2,2,3,2)
full phase ratios (1,1,1,1,-1,1)
exact weights 2 (1/2,1/2) (1,1/24)
D16 ROUND2 PROBES COMPLETE
```

These are fresh constructions, not parsed PASS labels.

## 3. Typed owned boundary repair

`BoundaryPort` now carries:

```text
element index;
kind/type;
owner.
```

`CausalOrder` requires every boundary mark to be nonempty, unique by element,
in range, an antichain, and extremal with the correct polarity.  Past and
future boundary element sets must be disjoint.  Permutation transports the
element index while preserving type and owner.

The typed-boundary automorphism counts are now:

```text
(antichain4,chain4,V3,Lambda3,diamond4)=(24,1,1,1,2).
```

The V/Lambda swaps cease to be automorphisms because their two boundary legs
have distinct owners.  Their order-theoretic linear-extension counts remain
`2`, correctly separating gauge-preserving automorphisms from construction
presentations.

## 4. Relabeling-invariant typed gluing

`glue_typed` matches the complete key `(kind,owner)`, identifies the associated
future/past elements, transports all unshared right elements, takes transitive
closure, and retains the left external past and right external future.

For two two-chains, each region has two possible label permutations.  I tested
their full Cartesian product, not only the source's both-reversed example.
All four outputs have:

```text
N=(2,1,0);
|Aut|=1;
linear extensions=1;
past mark=(outer-past,cell-C);
future mark=(outer-future,cell-C).
```

Changing only type or only owner breaks the key match and rejects.  This
closes the boundary-permutation and owner/type aliasing risks.

The quotient action is evaluated once on the sewn order, where the new
cross-boundary interval contributes `N_1=1`.  Naive regional addition remains
zero for that term, so the obstruction and once-only quotient computation are
both exact.

This is a valid finite typed quotient evaluator.  A physical factorizable path
integral would still need state/boundary/corner and measure factors, which the
theorem explicitly leaves open.

## 5. Exact rejection controls

Fresh probes independently confirm:

```text
nonminimal past boundary       rejected;
nonmaximal future boundary     rejected;
same element in past/future    rejected;
wrong shared type              rejected;
wrong shared owner             rejected.
```

Thus the repaired API does not rely on the caller to promise extremality or
ownership consistency.

## 6. Six-order coefficient census

The expanded signature census uses:

```text
antichain4, chain4, V3, Lambda3, diamond4, sewn_chain3.
```

The sewn chain has phase sensitivity to `beta_1`, which was invisible modulo
two on the original five-order census because chain4 has `N_1=2`.  Independent
enumeration of every

```text
(alpha,beta_0,beta_1,beta_2) in {0,1}^4
```

now gives 16 distinct six-entry signatures.  No coefficient packet is omitted
and no collision remains.

The semantic count `distinct_phase_signatures=16` is therefore correct.  The
packet documentation should merely expose the sixth order explicitly.

## 7. Full phase-factor inequivalence

For `A=N_0` and `B=N_2`, the complete difference vector on the six-order
census is:

```text
(0,2,2,2,3,2).
```

The corresponding phase-ratio vector is:

```text
(+1,+1,+1,+1,-1,+1).
```

Both vectors are nonconstant.  Therefore A and B are related by neither one
common additive constant nor one common multiplicative phase over the frozen
class.  The repaired source now checks the full vectors rather than one
diamond value, closing the load-bearing round-1 defect.

## 8. Exact normalization and orbit factors

All probability/orbit values now use `fractions.Fraction`:

```text
raw phase Born mass          2;
normalized alternative mass (1/2,1/2);
chain orbit factor           1;
antichain orbit factor       1/24.
```

The orbit check compares independently constructed rational values and also
requires them to differ.  There is no binary-float or self-comparison artifact.

As before, the example does not assert that `1/|Aut|` is the unique physical
measure.  It proves that an orbit convention must be specified.

## 9. Receipt and verdict scope

The theorem title is repaired to “poset relabeling does not select the causal
action,” and the body immediately limits the claim to the frozen finite
family.  It explicitly denies continuum diffeomorphism covariance and
microcausality.

The candidate theorem verdict is justified:

```text
INTERVAL-ACTION-FAMILY-NONSELECTING.
```

The formal protocol status remains correctly separate:

```text
INCOMPLETE-INVESTIGATION.
```

No published BDG coefficient provenance, quantum/decoherent measure, D14
record instrument, stable `3+1` phase, cone prediction, physical unit bridge,
or `G` is supplied.  No V9 holdout is licensed.

## 10. Round-1 opening disposition

| Opening | Round-2 result |
|---|---|
| common-phase check used one order | repaired with full differences and phase ratios |
| float normalization/orbit checks | repaired with `Fraction` |
| boundary types/owners absent | repaired with `BoundaryPort` |
| nonextremal/overlap admission | rejected in constructor |
| positional last/first glue | replaced by typed/owned boundary-key quotient |
| relabeling of sewn regions | all four independent pairs pass |
| incomplete/colliding packet signatures | expanded census gives 16/16 |
| formal D16 overclaim | none; incomplete status and ceiling retained |

## 11. Final determination

```text
26/26 NORMAL AND -O                    = REPRODUCED
SOURCE/PACKET/SEMANTIC/STDOUT HASHES   = EXACT
TYPED/OWNED BOUNDARY PERMUTATIONS      = PASS
WRONG TYPE/OWNER                       = REJECTED
NONEXTREMAL/OVERLAP                    = REJECTED
TYPED QUOTIENT GLUING                  = PASS
EXACT FRACTION WEIGHTS                 = PASS
16 PACKETS / 16 SIGNATURES             = PASS
FULL PHASE-RATIO NONCONSTANCY          = PASS
FINITE FAMILY NONSELECTION             = PROVED
FORMAL D16 PROTOCOL                    = INCOMPLETE
ROUND-2 CLEAN-ROOM VERDICT             = PASS AT FINITE THEOREM SCOPE
```

No clean-room blocker remains against the finite interval-action
nonselection theorem.

`git diff --check` passed before this review was written.  No primary D16 file
was edited by this referee.

