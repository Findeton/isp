# D6 hostile mathematics review — round 2

**Date:** 2026-07-11  
**Reviewer role:** independent hostile mathematics audit  
**Verdict:** **PASS AT REPAIRED SCOPE**

## 1. Frozen material reviewed

| artifact | SHA-256 |
|---|---|
| `v10/code/d6_sealed_holonomy_token_exact.py` | `4addff806650f5286f567565f2369fb1014ae625116c45af215c098024287983` |
| `v10/note-d6-sealed-holonomy-factor-token.md` | `e1980919ee128dc2ae9d34b90df3095b0877be92fbdb35360aecf7ab5ce061f3` |
| `v10/relativistic-isp-v10-paper7-sealed-holonomy-reconstructs-change-not-birth.md` | `93af04e284258cb8008ef3933aa4b608893e0c8da520d1eb6effebd2dedfc8c8` |
| `v10/reviews/d6-hostile-round1-opening-ledger.md` | `c2aa6613dfc75c328212972ef93f02f87f3e683909ebded94fbecc7d3222a57c` |

The executable reports `84/84`. Ordinary and optimized execution produce the
same complete stdout SHA-256:

```text
7c1940601bad3a570b25afc2cab605e4e4d1926d2efb2e6708465d00c133f10c
```

Thus the receipt no longer depends on Python's removable `assert` statement.
The fixed `EXPECTED_CHECKS=84` gate also makes silent deletion of a successful
check fail the receipt instead of producing a self-congratulatory `N/N`.

## 2. What I independently recomputed

I rebuilt the central witnesses without importing the production module.

1. For `P=(1/4,3/4)` and `Q=(3/4,1/4)`, the RN field is exactly
   `(1/3,3)`, both normalization identities equal one, and
   `D(P||Q)=log(3)/2`. The reverse field is its reciprocal although the two
   directed KL values coincide.
2. The three-bit parity laws at `theta=+/-1/2` have identical one- and
   two-coordinate marginals and triple expectations `+1/2` and `-1/2`.
3. Their log-Walsh coefficients agree below the top mask; the top coefficients
   are `+log(3)/2` and `-log(3)/2`. Full reconstruction returns the supplied
   law to the Decimal precision floor.
4. The two hidden lifts have the same endpoint laws and RN field but the same
   future kernel `Y=H` gives probabilities `7/12` and `5/12`.
5. Bisection gives
   `h=0.6093778634360062315368033711683986954...`; substituting it in
   `tanh(h)=exp(-h)` gives only the chosen precision residual. Uniqueness on
   the positive half-line is analytic: `tanh(h)-exp(-h)` is strictly
   increasing, is negative at zero, and tends to one.
6. The two-bit parity RN table is `(3/2,1/2,1/2,3/2)` and has determinant
   exactly `2`; an independently factorized two-coordinate RN field has
   determinant zero.
7. Bernoulli cylinder laws at `p=1/3`, `2/3`, and `1/2` are normalized and
   projective at every level by the binomial identity. The first two towers
   are related by global sign flip; the fair tower is outside that pair.

These computations agree with the executable and with every numerical claim
used by Paper 7.

## 3. Round-1 mathematical openings

| opening | hostile round-2 result |
|---|---|
| M1 — ambiguous `R=1` / eventless language | **Closed.** The code tests `R` identically one, and the manuscripts explicitly restrict the conclusion to `P=Q`; null proposal and eventlessness are refused. |
| M2 — missing positivity domains | **Closed.** The parity family is restricted to `-1<theta<1`; Bernoulli parameters are restricted to `0<p<1`. The audited cells are strictly positive. |
| M3 — unexecuted lower log-Walsh fiber | **Closed.** Both twins are transformed. Masks `0..6` agree within the declared high-precision tolerance, while mask `7` is nonzero and reverses sign. The analytic coefficients confirm the result. |
| M4 — vacuous commitment-scope comparison | **Closed.** The executable constructs normalized positive one-body and two-body parity-mode laws from the same root, verifies their distinct essential dependence sets, verifies the fixed-point expectation, and constructs the mirrored orientation. This proves nonselection of mode/scope at exactly the claimed presentation-relative level. |
| M5 — unproved v6/v7 coefficient identification | **Closed by refusal.** The paper now displays `h_commitment ?= h_effective` and says Paper 32 left it open. No equality is used downstream. |
| M6 — vacuous ownership check | **Closed.** One two-coordinate representation with ID `xy` and two unary representations with IDs `x,y` are evaluated to the same RN table. Census and identities differ, and duplicate identity is rejected. This establishes representational nonuniqueness; the paper does not pretend that either representation has been physically selected. |
| M7 — two profinite examples differed only by sign | **Closed.** The mirror relation is admitted and the `p=1/2` tower provides a compatible family outside that mirror pair. |
| R1 — optimized execution and self-referential count | **Closed.** `python3` and `python3 -O` give identical output; the fixed cardinality gate is effective. |
| R2 — additive survival gluing absent | **Closed.** A separate positive `I,J` witness checks `exp(-(I+J))=exp(-I)exp(-J)` and the complementary weights sum to one. |
| R5 — ill-typed h-transform inputs | **Closed.** Duplicate candidates, zero `h`, negative multiplicity, and missing multiplicity are rejected. The successful domain is finite, nonempty, complete, and has positive total weight. |
| R6 — hidden future was only a renamed static marginal | **Closed.** The same explicit kernel `Y=H` is applied to both hidden histories and separates their future predictions. |
| R8 — token census strings mistaken for proof | **Closed by scope.** The strings are presented as a ledger summarizing preceding constructions and absences, not as an independent theorem. |

## 4. New hostile attacks

### 4.1 Does the determinant prove a physical bridge?

No, and Paper 7 no longer says that it does. For a positive `2 x 2` table,
nonzero determinant exactly rejects product factorization across the **declared
tensor split**. It cannot determine whether the coordinates are physically
disconnected, whether dependence arose from conditioning or a hidden common
cause, or whether one primitive carrier exists. The manuscript preserves all
of those alternatives.

### 4.2 Does complete Walsh reconstruction smuggle in holonomy?

No. The proved statement is only finite log-density identifiability. The
constant coefficient is fixed by normalization and the `2^n-1` nonconstant
coordinates match the positive-simplex dimension. The paper explicitly says
that typed loops, cochain provenance, orientation, units, and physical
measurement remain missing. This is the correct mathematical ceiling.

### 4.3 Does the commitment root choose a mode by itself?

No. The one- and two-body constructions are counterexamples: the same scalar
root produces positive normalized laws on different supplied parity modes.
Orientation reversal also produces the mirror law. The root selects a
coefficient only after a naturally parameterized balanced `+/-1` mode is
supplied. Rescaling or replacing that mode is outside the theorem, as it must
be.

### 4.4 Does projective consistency choose a path measure?

No. Three analytic all-level Bernoulli families satisfy the same bonding
rule. The five-level executable is only a finite audit of the formula, and
the prose correctly distinguishes that audit from the analytic all-level
statement. It also refuses to identify end deletion with arbitrary-subset
naturality or physical locality.

### 4.5 Does an RN-neutral field encode the missing null outcome?

No. `R identically 1` says the two supplied comparison laws coincide. The two
explicit symmetric proposal laws have different null masses, proving that
comparison symmetry and RN neutrality do not determine proposal frequency.

### 4.6 Are the numerical claims stronger than the arithmetic supports?

No. Rational incidence, marginal, rank, determinant, and projectivity claims
use exact `Fraction` or integer arithmetic. Transcendental claims are labeled
high-precision `Decimal` calculations and are guarded by residual bounds.
No approximate number decides physical identity, incidence, or
identifiability.

## 5. Remaining boundaries, not defects

The following are deliberately **not** results of D6:

- construction of a typed sealed diamond or a physical holonomy measurement;
- generation of the candidate extension domain or its null probability;
- selection of primitive scope, orientation, ID, or ownership;
- identification of expected KL with a realized evidence carrier;
- sampling of a commitment outcome, execution of a seal, or birth of a record;
- proof that the v6 commitment coefficient equals the v7 effective h-weight;
- derivation of locality, a construction-order gauge, or a physical bridge
  from a statistical dependence table;
- selection of one profinite/path measure by compatibility alone.

These omissions are stated in the theorem hypotheses, token census, refusal,
and conclusion. They no longer appear covertly as positive claims.

## 6. Verdict

**PASS AT REPAIRED SCOPE.** The 84-check receipt is reproducible, survives
optimized execution, and agrees with an independent reconstruction. Every
round-1 mathematical opening is either actually repaired or retained as an
explicit non-theorem. I found no new mathematical opening requiring another
revision round.

This is not a pass for “sealed holonomy generates the interacting click law.”
It is a pass for the narrower and now accurately named result:

> supplied ordered positive laws reconstruct a relative RN field and support
> conditional numerical weighting; they do not generate, own, seal, or birth
> the next physical record.
