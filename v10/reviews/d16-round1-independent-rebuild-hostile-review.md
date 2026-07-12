# D16 hostile review, round 1: independent rebuild and reproducibility

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Finite interval-action nonselection theorem:** **INDEPENDENTLY CONFIRMED, RECEIPT HARDENING REQUIRED**

The executable is exactly reproducible at the byte level.  Normal and
optimized Python pass 20/20 with identical stdout; source, generated packet,
semantic payload, and receipt hashes match.  A separate standard-library
census confirms all five frozen orders, all 84 permutation presentations,
their automorphism and linear-extension counts, all 16 binary coefficient
packets, exactly eight phase signatures, the gluing cross interval, and the
normalization obstruction.

The mathematical core is true: on this finite class, interval locality and
relabeling covariance do not select one coefficient packet.  In particular,
`S_A=N_0` and `S_B=N_2` have phase signatures that agree on four frozen orders
and differ on the diamond, so they cannot differ by one common global phase.

The exact receipt nevertheless needs major revision before hostile PASS:

1. check 14 claims the two packets are not related by a common additive phase,
   but its predicate tests only unequal integer action values on the diamond;
   it neither compares the other four orders nor works modulo the phase;
2. the supposedly exact normalization/orbit cells use binary floats, and the
   `1/24` orbit check assigns `1/24` and compares it to the identical expression,
   making the nontrivial antichain weight assertion tautological;
3. C0/C1 require boundary types and ownership, but the executable stores only
   untyped past/future index sets;
4. C5 requires typed boundary sewing, quotient/automorphism ownership and
   once-only shared terms, while the code implements only a hardwired
   last/first identification of two chains to demonstrate the obstruction.

These gaps do not refute the finite nonselection result; they block the exact
receipt and full D16 protocol.  The paper's formal status and ceiling correctly
remain `INCOMPLETE-INVESTIGATION`.

## 1. Reproduction and frozen hashes

### Commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d16_covariant_causal_action_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d16_covariant_causal_action_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d16_covariant_causal_action_exact.py | shasum -a 256
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d16_covariant_causal_action_exact.py | shasum -a 256
shasum -a 256 v10/code/d16_covariant_causal_action_exact.py
shasum -a 256 v10/data/d16-covariant-causal-action-exact.json
```

Both direct executions completed with the same labels and ended in:

```text
PASS 020: pre-final exact check count is frozen
CHECKS PASSED: 20/20
SEMANTIC SHA256: 107bedcdc071c0be21edc12aa928dc57fd45416206d4049ad643aa67712dd04f
SOURCE SHA256: 989f996af855daceffa8bff68d687ada60ab4f35a1736b76e6c0508156f7e386
VERDICT: INTERVAL-ACTION-FAMILY-NONSELECTING
```

Complete stdout hashes:

```text
normal  212df3c028e0fa7387170ba14dce541e868983e75c6a09c8bf6cb735635424ef
-O      212df3c028e0fa7387170ba14dce541e868983e75c6a09c8bf6cb735635424ef
```

Current authoritative file hashes:

```text
989f996af855daceffa8bff68d687ada60ab4f35a1736b76e6c0508156f7e386  source
d6b6efa782750bfcd59b79e8ebc849b2c82ae7daeb64027bef186fbf10a70ec0  packet
107bedcdc071c0be21edc12aa928dc57fd45416206d4049ad643aa67712dd04f  semantic
```

I independently selected the eight semantic fields and serialized them with
sorted compact JSON, reproducing `107bedcd...`.  Every value in
`d16-pre-review-receipt.md` matches current bytes.

No Python `assert`, `__debug__` branch, random input, external package, or
self-read JSON supplies a gate.  The output packet is written only after all
checks and the frozen semantic digest pass.  `-O` cannot remove `check` or the
explicit final guards.

## 2. Independent census

I implemented a separate strict-order representation using only sets,
`itertools`, and `fractions.Fraction`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/d16_cleanroom_rebuild.py
```

The independent summary is:

| Order | `N_k` | Automorphisms | Linear extensions | Permutations | Distinct labeled presentations |
|---|---:|---:|---:|---:|---:|
| antichain4 | `(0,0,0,0)` | 24 | 24 | 24 | 1 |
| chain4 | `(3,2,1,0)` | 1 | 1 | 24 | 24 |
| V3 | `(2,0,0)` | 2 | 2 | 6 | 3 |
| Lambda3 | `(2,0,0)` | 2 | 2 | 6 | 3 |
| diamond4 | `(4,0,1,0)` | 2 | 2 | 24 | 12 |

All `24+24+6+6+24=84` permutation presentations preserve the interval counts.
The mapped past/future boundary sets keep the same cardinalities and remain
antichains.  Thus no boundary-index permutation bug exists at the implemented
untyped-set scope.

## 3. Complete 16-packet census

The frozen packet is exactly

```text
(alpha,beta_0,beta_1,beta_2) in {0,1}^4.
```

The source destructuring `for alpha,*beta in product(...,repeat=4)` therefore
correctly creates one alpha and three beta coefficients.  The independent loop
visited all 16 tuples exactly once and found eight distinct five-order phase
signatures.

The full result groups in pairs because `beta_1` changes the chain4 action by
`N_1=2`, an even amount, while every other frozen order has `N_1=0`; hence it
does not change any `(-1)^S` signature on this class.  This explains eight
rather than sixteen phase signatures and confirms that the loop is complete,
not truncated.

## 4. Nonselection and the weak common-phase check

For

```text
A=(0,1,0,0),  S_A=N_0,
B=(0,0,0,1),  S_B=N_2,
```

the independent integer values across
`(antichain,chain,V,Lambda,diamond)` are:

```text
S_A = (0,3,2,2,4),
S_B = (0,1,0,0,1),
A-B = (0,2,2,2,3).
```

Their phase signatures are:

```text
phase_A = (+1,-1,+1,+1,+1),
phase_B = (+1,-1,+1,+1,-1).
```

The phase ratio is therefore not constant.  This is the load-bearing physical
inequivalence and it independently confirms the theorem.

Source check 14, however, is only:

```python
action_a.value(diamond) != action_b.value(diamond)
```

That predicate cannot establish absence of a common phase across a class.  It
does not even compare another order, and raw integer inequality is not the
same as phase inequality modulo two.  Check 13 already establishes the diamond
phase difference; check 14 adds no class-wide evidence despite its label.

**Required repair:** freeze both complete signatures or verify that the ratio
`phase_A(C)/phase_B(C)` takes more than one value over all five orders.  Also
print or hash the full 16-packet signature table so loop completeness is an
auditable result rather than only a semantic aggregate.

## 5. Automorphisms and construction presentations

The automorphism and linear-extension tuples independently reproduce:

```text
(24,1,2,2,2).
```

For every linear extension of each order, `S_A` is evaluated on the same
completed relation and gives the same phase.  This correctly removes birth-
label presentation from the whole-order action.

It does not produce a sequential growth kernel or prove local computability.
The theorem states that limitation accurately.

## 6. Regional gluing reconstruction

Identifying the last point of a two-chain with the first point of another and
taking transitive closure gives the three-chain:

```text
left/right N = (1,0),
glued N       = (2,1,0).
```

For the `N_1` action:

```text
S(left)+S(right)=0,
S(glued)=1.
```

The missing term is the cross-boundary comparable pair whose open interval is
the identified middle point.  The naive-additivity obstruction is exact.

The implementation is not yet a C5 sewing law.  `glue_at_last_first` ignores
the stored boundary fields and always identifies positional “last” and
“first” elements.  It has no boundary type, owner, explicit bijection,
automorphism quotient, shared-boundary measure, or once-only corner/action
ledger.  The manuscript correctly calls the result a gluing **obstruction**
and says such a law remains necessary.

**Required repair for C5:** define typed/owned boundary objects, validate a
boundary isomorphism, glue through that map, and execute relabeled versions of
the same sewing.  Separately record which regional, shared, cross-interval and
automorphism factors are owned once.

## 7. Float and exactness audit

The raw phase weights are integers `+/-1`, so their Born mass `2` is exact.
The source then uses `/`, producing floats:

```python
normalized = (... / 2)       # 0.5, exactly representable here
orbit_weight_antichain=1/24  # not exactly representable
```

The `(0.5,0.5)` result happens to be exact in binary and is numerically safe.
The antichain weight is not exact.  Worse, the check assigns `1/24` and then
compares it to the same `1/24` expression, so it would pass without validating
an independently expected rational value.

My clean-room computation with `Fraction` gives:

```text
raw Born mass       = 2,
normalized weights = (1/2,1/2),
chain orbit factor  = 1,
antichain factor    = 1/24.
```

**Required repair:** use `fractions.Fraction` throughout these cells and assert
`Fraction(1,len(Aut(C)))` against explicitly frozen rational expectations.
This is essential for a source advertised as exact, though it does not affect
the finite coefficient nonselection theorem.

## 8. Boundary and covariance scope

The implemented `CausalOrder` validates:

- square, irreflexive, asymmetric, transitively closed relation;
- in-range unique boundary indices;
- antichain past and future boundary sets;
- permutation transport of those sets.

It does not store the boundary type or owner required by protocol C0, and C1
therefore cannot test preservation of those marks.  “Every relabeling” is true
for relation plus untyped boundary sets, not yet for typed owned histories.

This does not weaken the scalar `N_k` relabeling theorem.  It means C0/C1 are
only partially implemented and the full protocol must remain incomplete.

## 9. Normalization and gauge multiplicity

Two pure phases have raw squared mass two.  A probability law requires an
alternative domain and measure before normalization; the executable correctly
does not infer one from `exp(iS)` alone.

The different automorphism orders also correctly show that labeled sums and
unlabeled/orbit sums need an explicit convention.  The witness does not prove
that `1/|Aut|` is the unique physical convention; the theorem only uses it to
demonstrate that gauge-volume ownership matters.  That scope is defensible.

## 10. Verdict and protocol coverage

The executable/packet verdict

```text
INTERVAL-ACTION-FAMILY-NONSELECTING
```

is mathematically correct for the frozen finite binary family.  The broad
paper title “covariance does not select the causal action” must always be read
with the printed finite-family qualifier; the receipt does not prove
nonselection for every causal action class.

The semantic ceiling is accurate:

```text
no published BDG coefficient provenance;
no quantum/decoherent measure;
no D14 records or birth;
no continuum or stable 3+1 phase;
no cone observable, units, scale, or G.
```

Focused gate disposition:

| Gate | Round-1 result |
|---|---|
| C0 exact orders/boundaries | partial: strict orders and antichains pass; types/owners absent |
| C1 label gauge | pass for relation plus untyped boundary sets |
| C2 locality meaning | prose correctly says interval/quasilocal, not nearest-neighbor |
| C3 coefficient nonselection | theorem true; common-phase executable gate weak |
| C4 dimension provenance | metadata input control passes; no BDG packet |
| C5 regional gluing | obstruction passes; full sewing law absent |
| C6 quantum measure | normalization obstruction passes; physical measure absent |
| C7 records/birth | absent |
| C8 no global clock | presentation claim scoped correctly; growth law absent |
| C9 geometry predictions | absent; V9 withheld |
| C10 empirical discriminator | absent; holdout remains sealed |
| C11 hostile closure | round 1 has open repairs |

Formal D16 status therefore remains:

```text
INCOMPLETE-INVESTIGATION.
```

## 11. Priority opening ledger

| ID | Severity | Opening | Required repair |
|---|---:|---|---|
| R1 | major exact-gate defect | common-phase label checks one diamond value only | compare full phase ratios/signatures across all five orders |
| R2 | moderate exactness defect | float `1/24` and self-comparison | replace with `Fraction` and frozen rational expectations |
| R3 | major for C0/C1 | boundary types and owners absent | add typed/owned marks and exhaustive marked relabeling tests |
| R4 | major for C5 | positional chain glue is not regional sewing | add boundary isomorphism, quotient and ownership ledger |
| R5 | formal blocker | C7, C9, C10, C11 incomplete | retain formal incomplete status and V9 refusal |

## 12. Final determination

```text
20/20 NORMAL AND -O                    = REPRODUCED
SOURCE/PACKET/SEMANTIC/STDOUT HASHES   = EXACT
FIVE ORDER CENSUS                      = INDEPENDENTLY REBUILT
ALL 84 PERMUTATIONS                    = PASS
AUTOMORPHISMS/LINEAR EXTENSIONS        = (24,1,2,2,2)
INTERVAL COUNTS                        = EXACT
ALL 16 COEFFICIENT PACKETS             = ENUMERATED
DISTINCT PHASE SIGNATURES              = 8
GLUING CROSS INTERVAL                  = EXACT
NORMALIZATION OBSTRUCTION              = EXACT IN CLEAN-ROOM FRACTIONS
FINITE FAMILY NONSELECTION             = CONFIRMED
EXACT RECEIPT / FULL PROTOCOL           = MAJOR REVISION
FORMAL D16 STATUS                      = INCOMPLETE-INVESTIGATION
```

`git diff --check` passed before this review was written.  No primary D16 file
was edited by this referee.

