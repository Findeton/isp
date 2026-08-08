# HA — HOSTILE REVIEW, R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator/algebraic lens.  **Date:** 2026-08-08.
**Protocol:** `v13/note-ha-hostile-protocol.md` (FROZEN, v13 #240), kill-shots
K1–K5.  Primary weight K2 and K1; K4 at full depth; K3 and K5 at lower depth.
**Method:** independent recomputation only.  Nothing was imported from
`v13/code/ha_successor_exact.py`.  All linear algebra was rebuilt by a different
route (closed-form `q`-from-counts and adjugate/determinant inversion, against
the delivery's Gauss–Jordan), all residuals rebuilt from the paper's stated
definitions, in `fractions.Fraction` throughout.  Scripts in
`…/scratchpad/r1_rebuild.py`, `r1_operator.py`, `r1_probe.py`.
**No repository file was modified.**  The three mutant runs below write no
artifacts (`WRITE_ARTIFACTS = DELIVERY_RUN and not SELFTEST_ONLY`); the frozen
`_output.txt` and `_receipt.json` hashes were re-verified unchanged afterwards.

## 0. SHA verification (gate to review)

| object | committed sha256-12 | recomputed | |
|---|---|---|---|
| `v13/paper-ha-successor.md` | `4e7589da58fe` | `4e7589da58fe6931…` | MATCH |
| `v13/code/ha_successor_exact.py` | `19dad19b01ee` | `19dad19b01ee09f3…` | MATCH |
| `v13/code/ha_successor_output.txt` | `fda287ee86c3` | `fda287ee86c345f3…` | MATCH |
| `v13/code/ha_successor_receipt.json` | `7d74bea76760` | `7d74bea767606e94…` | MATCH |

Both hash pins in §11 also match on my instrument
(`nt_transport_receipt.json` → `d256891b…`, `gen_generality_receipt.json` →
`e0b2f444…`).  Anchors A01–A08 recompute from the repository exactly as
committed: the ten frozen-tree `.py` counts `{353, 273, 137, 101, 84, 9, 8, 7,
3, 1}`, 3 at the root, 12 `lapse`-carrying files in `code/` and 0 in every
other frozen tree, NT's 34,024 reduced paths and its per-setting orders
`(1,1,1,1,4,4)`.

---

## 1. What reproduced (the part I could not break)

Every headline number of the primary unit reproduced **exactly** on my own
instrument, and in several places I widened the measurement and it still held.

| object | delivery | R1 independent | |
|---|---|---|---|
| record readout, 11 records: counts, `q`, `det q`, `I`, admissibility | table §4.1 | identical, adjugate route | ✔ |
| admissible / rejected | 9 / 2 (one per failure mode) | 9 / 2 | ✔ |
| lapse family, ordered pairs | 12 / 132 | 12 / 132 | ✔ |
| identifiability rank per site | 2 at all 9 | 2 at all 9 | ✔ |
| **closure table, 11 rules × 9 records** | §6.1 | **cell-for-cell identical** | ✔ |
| **sector law, 63 transported cells** | 0 mismatches | 0 mismatches | ✔ |
| G08B frozen front | Λ=I at 9/9, residual 0 at 0/9 | 9/9, 0/9 | ✔ |
| cross-term `(Λ−I)(0,0)`, `max|ρ|` | §6.1 table | identical incl. `−4/33, 2/11, −4/55`, `40/33`, `20/33` | ✔ |
| operator layer | 1056 built / 33 undefined / 0 non-bij / 0 mismatch | identical | ✔ |
| `A-linkframe|G-OFFDIAG2` residual `(35/132, 7/660)` | undefined mod 5, `(0,0)` mod 7, `(11,2)` mod 13 | identical | ✔ |
| density-weight flip, cells that move | 4 (`G-ANISO`, `G-ANISO2`, `G-CURVED`, `G-DIAG2`) | 4, same names, 92 at `G-CURVED` | ✔ |
| D-TOT census | 1188 / 864 / 332 / 856 / 8 | identical | ✔ |
| HHH detector | 108 cells, Jacobi 0, **81** non-identity, 27 per rule | identical | ✔ |
| d = 3 | `A-axis` 0/0/18, `A-chart` 0/30/30, `A-linkframe` 30/30/30, `A-insert` all CLOSES | identical | ✔ |

**K1 — the construction.**  The bijection and its closed-form inverse are
correct.  I verified `H⁻¹H = HH⁻¹ = id` on 1,584 (rule, record, lapse,
base-front) instances **with a non-zero address register** — the delivery tests
the H family only at `m ≡ 0` — with 0 failures.  The transported-second-step
property is correct **by construction**: I computed `drag(M, n₀+N)` separately
and matched it against the register produced by `H[M]H[N]`, exactly.

I re-derived the closed form by hand from the five-map composition and confirm
it is not an approximation:

> `m_final = −β − w[M,n₀−M] − w[N,n₀−M−N] + w[M,n₀−M−N] + w[N,n₀−N]`, and since
> `w[N,·]` is additive in its front argument this telescopes to
> `w[N,M] − w[M,N] − β`, i.e. **`ρⁱ = (Λ^{ij} − I^{ij}) ω_j`** for architecture
> A and `Σ_ℓ λ_ℓ e_ℓ^i ω_ℓ − βⁱ` for architecture B.  The front returns exactly.

I then checked the two routes against each other at **all** 11 × 9 × 132 =
13,068 cells (the delivery cross-checks 1,188, i.e. 9.1%): **0 disagreements**.

**K2 — the forcing disclosure (X02) is correct.**  Given the measured rank 2 at
every site, `(Λ−I)ω = 0` on a spanning covector family iff `Λ = I`.  Note the
rank is measured on `G-FLAT` only — which is legitimate, because `ω` is a
function of the lapse pair and the site alone and does not read the record at
all.  I verified that independently.

**No-smuggling scan (K1).**  I enumerated the inputs of every drag rule.  For
the record-native rules (`A-chart`, `A-axis`, `A-linkframe`, `A-linkhalf`,
`B-axis`, `B-all`, `B-chart`) the *only* inputs are the link interval counts at
the site, the front tilt `n(x+e) − n(x)`, and the eventwise lapse value `N(x)`.
No embedding coordinate, no metric estimator call, no background normal, no
planted frame enters.  `A-insert*` insert `I` explicitly and are declared
controls.  **The construction passes GW1 §1.2's first three exclusions
cleanly.**  See F12 for the fourth.

**Controls I added that the unit passes.**  (a) The residual is
**front-independent**: 4,752 literal evaluations over four distinct base fronts,
0 variation — so the single declared base front is not a scope restriction.
(b) The HHH detector's 81/108 is **robust to the composition order** of the
three corrected switches: I re-ran with the reversed order and got 81/108 with
cell-by-cell agreement at 108/108.  (c) Chart equivariance survives extension to
the **whole** declared translation group and all eleven rules (384,912 site
comparisons, 0 violations).

---

## 2. Findings

### MAJOR

**F1 [K4] — `G22` cannot return POSABLE anywhere in the declared arena, and its
positive control cannot fail.  `HA-BRIDGE-NOT-POSABLE` is an arena-determined
output, not a measurement.**

`posable = carrier_match AND in_spectrum AND relation_holds`, and
`G22 = gen_dih AND (not posable)`.  Evaluating each conjunct across the whole
declared arena (primes {5,7,13} × d ∈ {2,3}, k = 2 independent lapses):

| p, d | carrier `p^{k+d}` | `carrier_match` (∈{36,81}) | holonomy order | `in_spectrum` |
|---|---|---|---|---|
| 5, 2 | 625 | False | 5 | False |
| 5, 3 | 3125 | False | 5 | False |
| 7, 2 | 2401 | False | 7 | False |
| 7, 3 | 16807 | False | 7 | False |
| 13, 2 | 28561 | False | 13 | False |
| 13, 3 | 371293 | False | 13 | False |

`carrier_match` requires the *cardinality* of a `p^{k+d}` carrier to equal 36 or
81 — impossible for every declared prime.  `in_spectrum` tests a prime for
membership in `{1,4,6,8,10,12,14,30}`, which contains no prime.  Both conjuncts
are **identically False** over the entire declared arena.  And the third leg,
the "positive control" `gen_dih`, is **analytically forced**: with
`D = ΣQ⁻¹ΣQ` and `Σ² = id`,
`ΣDΣ = Q⁻¹ΣQΣ = (ΣQ⁻¹ΣQ)⁻¹ = D⁻¹` for *every* completion `Q`.  Measured: 0
failures over GEN's full 40,320-member family and over 1,200 random `Q` at
n = 3,4,5.

Therefore **`G22 ≡ True` for every legitimate input**.  The only thing that
kills it is `bridge-lax`, which rewrites the predicate itself — i.e. the gate is
falsified only by deleting it.  I confirmed the insensitivity directly: under
`closure-lax`, which fails five must-pass gates, `G22` still prints PASS and the
bridge verdict still prints NOT POSABLE.

The pin asked for the secondary "a yes or no BY MEASUREMENT, not analogy".  An
instrument that can only emit "no" has not measured anything.  Note the
*substantive* observation underneath (NT/GEN is a different arena with no
committed map to HA's carrier) may well be right — the coordinate table exhibits
real mismatches — but it is a reasoned coordinate audit, not a measured verdict.

*Repair (choose one):* (i) supply a positive control — a construction, however
artificial, at which `posable` evaluates True — and demonstrate it; or (ii)
demote `G22` to a **recorded** gate, restate §10.4 as a coordinate-mismatch
report rather than a verdict, and replace `carrier_match` with a criterion that
a morphism could actually satisfy (equal cardinality is not a necessary
condition for a carrier morphism to exist).

---

**F2 [K4] — the "elementary abelian of exponent 5, order 5" holonomy is the
declared prime, not a property of `R_HH`.  RUNBOOK §15 violation.**

On the reduced carrier `R_HH` acts as the **translation by `ρ(x*) mod p`** in
`(F_p)^d` (the fronts return to themselves), so `⟨R⟩ ≅ Z/p` whenever `ρ ≢ 0`,
and `Z/1` otherwise.  "Elementary abelian of exponent p" is then true of any
group of prime order and carries no information.  Measured at the declared loop,
where `ρ(0,0) = (1/6, 1/6)`:

| p | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---|---|---|---|---|---|---|
| `ρ mod p` | (1,1) | (6,6) | (2,2) | (11,11) | (3,3) | (16,16) | (4,4) |
| `|⟨R⟩|` | **5** | **7** | 11 | **13** | 17 | 19 | 23 |

5, 7 and 13 are all **declared arena coordinates** (`DECL["primes"]`), yet §10.1
hard-wires `p = 5` and the paper enters "order 5" as a *conclusion* ("the
measured consequences: the HA holonomy group has order 5, exponent 5, which is
NOT in GEN's measured order spectrum").  RUNBOOK §15: quantities not gated
invariant across the unit's admissible arenas "may serve as instruments but
never as conclusions"; and §14 requires an instrument that enforces an arena
action to be self-tested under it.  Neither is done.

*Repair:* compute the holonomy at all three declared primes, gate the
(non-)invariance explicitly, and remove the group order from the argument — or
state it as an instrument reading with the prime attached at the claim.

---

**F3 [K4] — the §10.2 spectrum row is false as stated.**

The paper's row reads *"in GEN's measured order spectrum {1,2,3,4,5,6,7,15} for
the defect, holonomy {1,4,6,8,10,12,14,30}"* → HA: **"no (order 5)"**.  I
reproduce GEN's defect order spectrum independently (A14):
`{1:96, 2:1440, 3:4224, 4:4608, 5:4608, 6:6912, 7:9216, 15:9216}`.
**5 is in it, with multiplicity 4,608.**  The coordinate table's own
"defect construction" row pairs `R_HH` with `D`, so the defect spectrum is the
natural comparator; the code's `in_spectrum` silently uses only the *holonomy*
spectrum, which is the one of the two printed spectra that yields the wanted
answer.  At p = 7 the order (7) is likewise in the defect spectrum.

*Repair:* name the single spectrum being compared against and justify it; if it
is the defect spectrum, the honest entry is "yes", and §10.4's second "measured
consequence" must be withdrawn.

### MEDIUM

**F4 [K2] — G09: the claim is a THEOREM, but the exhibited witness does not
establish the family §6.5's own definition names.**

§6.5 defines link-local as "`λ_ℓ` is a function of `n_ℓ` alone", which for
architecture A is `Λ = Σ_ℓ f_ℓ(n_ℓ) e_ℓ e_ℓᵀ`, so at d = 2
`Λ¹¹ = f₁(a) + f₃(c)`, `Λ²² = f₂(b) + f₃(c)`, `Λ¹² = f₃(c)`.  The exhibited
witness is `G-CURVOFF (2,2,6)` vs `G-DIAG2 (2,2,4)`, which share `a = 2` but
**differ in `c`** (6 vs 4).  It constrains `f₁(2)+f₃(6) = 2/3` against
`f₁(2)+f₃(4) = 1/2` — **satisfiable** (take `f₁(2)=0, f₃(6)=2/3, f₃(4)=1/2`).
So the witness kills only the *diagonal-restricted* subfamily `Λ^{jj} = f(n_{e_j})`
— i.e. exactly `A-axis` — not the family the paper names, which includes the
`A-linkframe`/`A-linkhalf`/`B-*` shapes.  The prose ("a weight that reads only
its own link's count cannot see it") is loose for the same reason: the *sum*
over links sees two counts.

The claim is nevertheless **true and provable**, and a valid witness exists
inside the declared nine:

> `Λ¹² = f₃(c)` must equal `I¹² = −((c−a−b)/2)/det q` for every admissible
> `(a,b)`.  `G-DIAG2 (2,2,4)` and `G-OFFNEG (3,5,4)` share `c = 4` and demand
> `f₃(4) = 0` and `f₃(4) = 2/11`.  Contradiction.  ∎

I also swept the admissible count lattice: 2,808 witnesses with the same
`(n_{e₁}, n_{e₁+e₂})` and different demanded `Λ¹¹`, and 23,133 with the same
`n_{e₁+e₂}` and different demanded `Λ¹²`.

*Repair:* swap the witness for the `c = 4` pair and add the two-line proof.
The verdict is unaffected; the evidence currently does not support the stated
generality.

---

**F5 [K4] — "the dihedral relation … holds at 17 of them" is a single-site
surrogate, not the relation.**

The instrument's predicate at those 24 pairs is `ρ₁ + ρ₂ == 0` evaluated over
**Q at the single site (0,0)**, not `ΣRΣ = R⁻¹`.  Recomputed three ways:

| reading | result |
|---|---|
| delivery's single-site proxy | **17 / 24** (reproduces the paper's number) |
| the full-field statement `σ·ρ = −ρ` at all 9 sites | **8 / 24** |
| the carrier-level group relation, counting only pairs at which Σ preserves the front sector so the relation is even **defined** | **3 / 24** |

Σ preserves the front sector only for swap-symmetric lapse pairs; for 21 of the
24 the carrier-level relation is undefined, not "holding" or "failing".  The
inference drawn ("a coordinate coincidence, not a structural property")
**survives and is strengthened** — but the printed number does not measure the
stated quantity.

*Repair:* report 8/24 (field) or 3/24-of-defined (group), and say which.

---

**F6 [K1] — G04's negative control is evaluated at a coordinate the positive
side never visits (§15 addendum, #196 like-for-like).**

The H family is measured invertible at register `m ≡ 0`; the declared
non-injective falsifier `RegisterCollapse` is fed `m ≡ 1`.  Measured directly:

| configuration | falsifier passes `H⁻¹H = HH⁻¹ = id`? |
|---|---|
| `m ≡ 0` — the coordinate the H family is tested at | **True** (i.e. NOT rejected) |
| `m ≡ 1` — the coordinate the falsifier is tested at | False (rejected) |

At the H family's own coordinate the falsifier is indistinguishable from a
bijection, because collapsing an already-zero register is the identity.  G04's
teeth come entirely from the coordinate switch.  The conclusion is nonetheless
sound: I measured the H family invertible at `m ≠ 0` (1,584 instances, 0
failures).

*Repair:* run both sides at both registers.

---

**F7 [K4/K5] — the bridge's "positive control" cannot fail.**  See F1: `gen_dih`
is an identity of `D = ΣQ⁻¹ΣQ`.  Per RUNBOOK §14 addendum (#208),
analytically-forced clauses are disclosures, not controls.  A control that holds
for all 40,320 members of the family, by algebra, does not license the sentence
"while the same relation is measured **to** hold for GEN's own defect", which
reads as a discriminating measurement.

*Repair:* disclose the forcing (as X02 does for G08) and find a control that can
fail — e.g. a completion-like object built without the `Σ…Σ` sandwich.

### LOW–MEDIUM

**F8 [K2] — the headline closure table is single-route.**  §3.7 says the
residual "is computed by routes that share no code", but §6.1's table is
produced by `residual_field_closed` alone; the literal five-map composition
cross-checks only pairs with both indices < 4, i.e. **1,188 of 13,068 (9.1%)**.
*I closed this gap*: literal vs closed at all 13,068 cells, **0 disagreements**.
No error — but the paper claims more cross-validation than was performed.
*Repair:* state the 9.1% scope, or cite this recomputation.

**F9 [K5] — G14's claim text overstates its measurement.**  The gate claims
equivariance "under **every** declared chart translation and direction
relabelling"; the run uses 3 of the 9 translations, 1 of the 11 rules
(`A-axis`), and 10 of the 132 pairs.  The receipt discloses `translations: 3`;
the paper does not, and §12 does not carry it as a deviation (failure-catalogue
#40 F1/F2 — scope tags at the claim, not just the receipt).  *I closed this
gap*: all 9 translations × 2 relabellings × 11 rules × 24 pairs = **384,912 site
comparisons, 0 violations**.  The claim is true; the scope tag is missing.
Also: the 4,860 are *site* comparisons of 2-component tuples, so "4860 component
comparisons" is a factor of two off (9,720 components).

**F10 [K5] — G13 likewise.**  "360 pairs tested" = `A-axis` only, 9 records, 40
of the 132 pairs.  *I closed this gap*: antisymmetry over all 11 rules and all
132 pairs, 13,068 cells, **0 violations**.

**F11 [receipt] — G08's cell count disagrees with the paper.**  The receipt's
`G08` detail reports `"cells": 72` (= all 8 architecture-A rules × 9 records);
the paper §6.3 claims **63**, and 63 is what the gate's predicate actually
adjudicates (7 transported rules × 9).  My rebuild compares exactly 63.  The
paper is right and the receipt field is mislabelled — but this is the
`#21→#23` shape (a count in the receipt that is not the count in the claim) and
an adjudicator would trip on it.

**F12 [K1] — GW1 §1.2's fourth exclusion is vacuous at this arena and is not
disclosed.**  The exclusion list forbids "algebraic data equivalent to the
target metric".  At d = 2 the three link counts and the three components of `q`
are related by an invertible linear map (`q₁₁ = a`, `q₂₂ = b`,
`q₁₂ = (c−a−b)/2`); at d = 3, six and six.  So **every** record-native rule has
access to data equivalent to the target metric by construction, and the fourth
clause cannot discriminate here.  §2's boast lists only the first three
exclusions.  The unit's real claim — which is honest and is stated correctly in
§6.5 and §13 — is about *which function* of the counts a rule computes, not
about what data it can see.  *Repair:* add one sentence to §2 or §12 disclosing
that the fourth clause is vacuous at this arena because the readout is a linear
bijection of the record.

**F13 [K4] — §10.1's "based closed-loop product of the link transports" does not
describe the computation.**  The instrument builds one permutation
`R = P_N P_M P_N⁻¹ P_M⁻¹ P_D` and takes `⟨R⟩` — a cyclic group with a single
generator.  There are no link transports and no loop product.  Comparing a
one-generator cyclic group against NT's Klein four-group and GEN's dihedral
group (both genuinely multi-generator) is not like-for-like (§15 addendum,
#196).  *Repair:* say "the cyclic group generated by the residual".

### LOW

**F14 — the operator norm is a boolean in disguise.**  Definition 2.4's
`‖R‖ = moved/carrier` can only be 0 or 1 here, because a non-zero translation of
`(F_p)^d × fronts` moves *every* configuration.  The 81-row table in §8 of the
output carries exactly one bit per row.  Not an error; worth saying, since
"‖R_HH‖" reads as a magnitude and is not one.

**F15 — the verdict string is gated, the verdict prose is not.**  I ran
`closure-lax`: it fails G07, G08, G08B, G12, G21 and correctly prints
`HA-STILL-BLOCKED + HA-BRIDGE-NOT-POSABLE` (so the §13-addendum verdict-gate
requirement, #234, is met for the first component, and `bridge-lax` covers the
second).  But the paragraph immediately after — "A record-native `H_a[N]`
EXISTS at finite N … The GW1 residual `R_HH` RUNS" — prints **unconditionally**,
including in that failed run.  *Repair:* gate the prose on the same booleans.

**F16 [K2] — G08 is analytically forced and is carried as must-pass.**  X02
discloses this.  I do not press it: the forcing is *conditional* on G03, and
`rank-lax` genuinely breaks G03 and takes G08 with it, so the pair is not
vacuous.  Flagged only against §14 addendum #208 for the adjudicator's judgement.

### K3 and K5, at the protocol's lower depth

- **K3 (the `v6_task2b` deviation).**  I did not audit the v6 fixture itself.
  On GW1's own text the rejection is correct: §2 grades that fit as running
  against embedding coordinate separations `dx = P[b] − P[a]` with `K`
  calibrated against the true interval, and §1.2 forbids held-out embedding
  coordinates outright.  The substitute readout imports no embedding data — see
  the no-smuggling scan in §1 above — but see **F12** for the clause it cannot
  satisfy non-vacuously.  Deviation 1 in §12 declares it plainly.  No finding
  beyond F12 at this depth.
- **K5.**  16 anchors reproduced (A01–A08 by me directly).  Three mutants
  executed (`closure-lax`, `bridge-lax`, `rank-lax`); all exit 1, and I verified
  the frozen artifacts are byte-identical afterwards.  `never_falsified` is
  empty in the receipt.  The cache gate (283,133 hits / 1,377 misses / 486 fresh
  bypasses) is genuinely two-sided in the §14-addendum sense.  The AST guard's
  synthetic injection is real.  Findings at this depth are F9, F10, F11, F15.

---

## 3. Recomputation count

**31 independent recomputation blocks**, totalling roughly **5.1 × 10⁵ exact
rational / F_p evaluations**, none of them routed through the delivery
instrument.  The largest: 13,068 literal five-map compositions + 13,068 closed
forms (the whole closure table, both routes, all 132 pairs — the delivery
cross-checks 1,188); 13,068 antisymmetry pairs; 384,912 chart-equivariance site
comparisons; 4,752 front-independence evaluations; 1,089 reduced-carrier
constructions with full permutation products at p ∈ {5,7,13}; 1,584
invertibility instances at non-zero register; GEN's 40,320-member family rebuilt
from scratch plus 1,200 randomised completions; the holonomy computed at seven
primes; ~26,000 admissible count vectors swept for the G09 witness.

**Numerical result found false: none.**  Every closure, sector, anomaly,
operator, detector, d = 3, density-flip and D-TOT number in the paper is exactly
right.  The defects are in what the numbers are *claimed to measure*, and they
are concentrated in the secondary (K4).

---

## 4. Disposition of the verdicts

- **`HA-RUNNABLE`: sustained.**  A record-native `H_a[N]` exists at finite N, is
  an exact bijection with a closed-form inverse, is lapse-profiled, transports
  its second normal step, and the GW1 residual runs — verified independently and
  at wider scope than the delivery ran it.  The two-sided closure result
  (diagonal sector exact, cross-term anomaly at 96/132) is correct, and its
  honest reading — closure holds precisely where the link-local weight coincides
  with the record-read inverse metric by arithmetic — is the paper's own (§6.5,
  X02, §13).  F8/F9/F10 narrow no conclusion; I closed all three gaps myself and
  the results held.
- **`HA-BRIDGE-NOT-POSABLE`: not sustained as a *measured* verdict.**  F1 shows
  the deciding predicate cannot return the other value at any point of the
  declared arena and its positive control cannot fail; F2 shows the group order
  it cites is the declared prime; F3 shows the spectrum comparison is false as
  written.  What survives is a reasoned coordinate audit whose *conclusion* I
  believe is probably right — NT/GEN really do live on a different carrier with
  no committed morphism — but which is currently dressed as a measurement it is
  not.  §13's last-but-one non-claim ("scoped to the committed coordinates …
  no nonexistence theorem") is the right register; §10.4 and the receipt are
  not written in it.

## 5. Grade

**ACCEPT-WITH-FIXES.**

The primary unit is sound, and I could not break it: no false number, the whole
closure result reproduced at ~11× the delivery's own cross-check density, and
three added controls (front-independence, reversed detector order, full chart
group) that it passes.  F4 and F6 are repairs to *evidence* for claims that are
themselves true, and F8–F11 are scope tags and a receipt field.  But F1–F3 are
not cosmetic: the secondary's verdict is produced by a gate that cannot fail,
resting on two quantities that are artifacts of declared arena coordinates and
one comparison that is false as printed.  Under the pin's own words — "a yes or
no BY MEASUREMENT, not analogy" — that leg is not delivered.

Required before TERMINAL: **F1, F2, F3** (the bridge must be either
re-instrumented with a falsifiable predicate and a working positive control, or
demoted from a verdict to a coordinate audit with the prime-dependence
disclosed), **F4** (swap in the valid witness and add the two-line proof, which
I supply), **F5**, **F6** and **F7**.  F8–F13 are scope tags, one receipt field
and three wording repairs.  F14–F16 are recorded for the adjudicator.
