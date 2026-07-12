# D11 hostile mathematics review — round 2 closure

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**

The round-1 mathematical blockers are repaired or honestly downgraded. The
exact sign logic, owned intervention witness, schedule probability, stricter
influence statistic, receipt gates, extinction theorem, and
`INCOMPLETE-PACKET` adjudication all survive. One new blocker appears in the
new typed durable-outcome records: the stored “effect” has the wrong operator
and, for sibling-MERGE, the wrong dimension.

## 1. Reproduction

The repaired exact engine reports `72/72`; ordinary and optimized stdout are
byte-identical with SHA-256

```text
9bee377674fdbffa8573e54d33b30066cebf64829e64cf743d10dbf196f1deb7
```

and the internally frozen summary receipt passes:

```text
7ae48df9da9853a581f262fbc74f183ead19f2745e64b57ebef0362addf7f5d6
```

The numerical campaign reproduces downstream sibling-MERGE influence in
`1/24, 4/24, 5/24` histories and passes its internal receipt gate:

```text
f1ab9e04caa42f200c3af53adb295d8f78d547178d0b67fff0bcffd9af547224
```

It still reports zero cone violations, false join/support/rank gates,
`INTERACTION-INERT`, and the more accurate diagnosis
`POPULATION-EXTINCT_INTERACTION-SPARSE`.

## 2. Round-1 mathematics closure table

| obligation | round-2 result |
|---|---|
| Exact `Q(sqrt(2))` signs | **CLOSED.** `sign()` uses rational sign and squared-magnitude comparisons. The tests `3-2sqrt(2)>0` and `-3+2sqrt(2)<0` straddle the nontrivial branch. Decimal remains only in the explicitly external direction diagnostic. |
| Owned root-intervention merge witness | **CLOSED.** Both worlds start from the registered `P0` versus `P+` root, receive the same H-SPLIT and fresh `P0` sibling, and the nonselective partial-iSWAP merge gives different downstream `P0` seal probabilities. |
| Numerical JOIN influence proxy | **CLOSED at registered potential-seal-law scope.** A state or coordinate difference no longer suffices; the merge output's downstream `P0/P1` Born law must differ. The repaired prevalence is `1,4,5`, making the failed `20/24` gate stronger. |
| Disjoint schedule probability | **CLOSED for the selected cell.** From the post-root-split history the first prescribed SPLIT has probability `(1/5)(1/2)=1/10`; afterward the other prescribed SPLIT has `(1/7)(1/2)=1/14`. Both orders therefore have exact presentation mass `1/140` and the same canonical state. |
| Expected checks and receipts | **CLOSED.** The exact check count is fixed at 72; exact and numerical semantic receipts are asserted internally; normal and optimized exact execution agree. |
| Extinction theorem | **CLOSED.** Sibling joins are port-disjoint, so `j<=floor(p/2)`; drift is `-j/(2p+j)`; total SEAL chance is at least `2/5`; optional stopping plus a uniform bounded-region run-of-SEAL argument proves almost-sure extinction. |
| Projective pushforward | **HONESTLY OPEN.** Prefix normalization is no longer called projectivity. Code, notes, receipt, and Paper 12 all state that canonical deletion/pushforward and decentralized construction-order gauge are unproved. |
| Primary verdict | **CLOSED.** Because canonical projective pushforward, decentralized clicking, integrated generated-history gauge, and general bridge birth remain open, the frozen verdict is correctly downgraded to `INCOMPLETE-PACKET`. |

## 3. New blocker — durable outcome effects are not the instrument effects

**Severity: MAJOR**

`DurableOutcome` introduces a field named `effect`, but two constructors store
operators that cannot be the corresponding input-space outcome effects.

### SPLIT

The two Kraus/isometry legs are `K_H` and `K_T`, each scaled by `1/sqrt(2)`.
Therefore their outcome effects are

```text
K_H^dagger K_H = I_2/2,
K_T^dagger K_T = I_2/2.
```

The SPLIT outcome record instead stores `I2`. That operator predicts unit
weight, whereas each logged outcome has exact probability `1/2`.

### Sibling-MERGE

Sibling-MERGE owns two qubit inputs. Its outcome Kraus maps are `J_b: C^4 ->
C^2`, so the input-space effects are

```text
J_b^dagger J_b,
```

which are `4 x 4`. The durable record stores `P0` or `P1`, each `2 x 2`.
Those projectors describe the pointer measurement on the discarded second
output, not the POVM effect on the owned two-input domain. The record does not
type which space its `effect` acts on, so this is not merely a harmless choice
of representation.

Terminal-SEAL is the one case where the stored `P0/P1` is correctly the qubit
input effect.

This metadata error does not change the already computed branch weights or the
extinction dynamics, because firing uses the correct token packets. It does
invalidate the new claims that every committed outcome has a complete typed
effect and that the repaired history is self-describing at that field.

**Required repair:** either store the actual input-domain effects
`K_g^dagger K_g`, `P_b`, and `J_b^dagger J_b` together with explicit domain
types, or rename the field to a typed pointer/readout operator and separately
store the Kraus/input effect needed to reconstruct probability. Add dimension
and equality checks for all three rule types.

## 4. Minor textual inconsistency

Paper 12 still says an open carrier stores an “ancestry word,” although the
repair intentionally removed that unbounded string and the `Port` type now
stores only distributed parent provenance. The theorem and receipt use the
repaired representation; the sentence should be synchronized.

## 5. Scope and verdict

The following repaired ceiling is otherwise defensible:

```text
INCOMPLETE-PACKET
+ globally raced normalized finite-prefix kernel
+ exact incidence-scoped instrument dynamics
+ separate dual-SL(2,C) covariance template
+ algebraic cone containment
+ owned sibling-interaction witness
+ almost-sure extinction
- canonical projective pushforward
- decentralized local click law
- integrated generated-history gauge
- general bridge birth
```

**MAJOR REVISION.** Do not reopen extinction, the numerical failure, or the
`INCOMPLETE-PACKET` verdict. Correct and type the durable outcome effects; then
the mathematics package should be eligible for a narrow final closure review.
