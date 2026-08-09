# RSQ — HOSTILE REVIEW R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator-system / algebraic lens.  **Date:** 2026-08-09.
**Protocol:** `v13/note-rsq-hostile-protocol.md` (FROZEN, kill-shots K1–K5).
**Independent recomputations:** **84** (enumerated in §0.3).
**Grade:** stated last, §8.

---

## 0. Provenance, and what I verified before reading

### 0.1 SHA verification of the frozen object

All four pinned artifacts verified BEFORE any analysis, and re-verified after
every run:

| artifact | required | measured |
|---|---|---|
| `v13/paper-rsq-reposed-square.md` | `f208ff12974b` | `f208ff12974b` ✓ |
| `v13/code/rsq_reposed_square_exact.py` | `18eb651d1ab1` | `18eb651d1ab1` ✓ |
| `v13/code/rsq_reposed_square_output.txt` | `810f923392d8` | `810f923392d8` ✓ |
| `v13/code/rsq_reposed_square_receipt.json` | `4db809f7b618` | `4db809f7b618` ✓ |

The unit's own 11 hash pins (TB3/LCB/HA/BRG/PSI papers and receipts, plus the
pin) were independently recomputed against the repo files: **11 of 11 match**.
The 15 numeric anchors were traced to their sources — TB3's ladder table
(`paper-tb3-third-base.md` §§ at |K| = 168 / 2 520 / 360 / 12 / 1), LCB's
`3p+1` thresholds (16 at p=5, 22 at p=7, `paper-lcb-livecell.md` line 839),
HA's d=2 determinant 2 (`paper-ha-successor.md` line 197). **26 anchors,
0 failures, all traceable.**

### 0.2 Determinism and the mutant harness

A full delivery re-run on `/opt/homebrew/bin/python3.13` reproduced
`_output.txt` and `_receipt.json` **byte-identically** (the delivery path
rewrites them in place; the SHAs above are unchanged after the rewrite —
see F16). The 57-mutant harness re-ran with **0 survivors**, and I confirmed
from the mutant table that **every one of the 38 must-pass gates is falsified
by at least one declared mutant** (`never_falsified: []` is correct).

### 0.3 What I recomputed independently

84 quantities, on instruments I wrote from the paper's declarations, sharing no
code with the unit:

*Deformation side (20):* site/link counts; det of both readout conventions;
the exact characteristic polynomial of the natural E (= (x−1)³(x−2)³, hence the
spectrum, not read off a triangular diagonal); the general-d law at d=2,3,4,5;
720 slot orders; 1 440 covariant cells; the 2 equivariant identifications and
their exact slot orders; the LEX order; precheck survivors and stillborn per
prime; the 4 420 total; module/lex fixed-space dimensions at all 7 primes; the
20 160-row criterion sweep by two routes; the diag(6,6,6,4,4,4) positive
control; the 210-row module table; ρ_V's permutation-ness; and an R1 extension
of the module sweep to all **50 400** rows.

*Transport side (21):* |G_C|; the wing group's order, element orders,
non-abelianness, closure over all 36 compositions, fixed labels, involution
count; F₁=F₃ at 20/30 and 20/20; the five ladder |K|; |fix δ_π| at 6/6;
the p-torsion census of S₇ and v_p(5040) per prime; the 9 declared census cells
rebuilt from the declared rule; 315 rows; 25 live; 0 injective by my own
image-size test; route-B projective calibration; all four threshold columns at
all 7 primes; the meeting table; the normalisation table.

*Grown arena (19):* m=6/43 labels; Σ's order; the normalisation at 6/6; the
commutation; generator orders; Ẽ; (I−Ẽ)³; 117 649 square cells; injectivity;
hom violations; 117 648 held; H1; H2 by my own entry-by-entry comparison; the
fixed-label value set; both teeth; the exemption; BREAK-HOM's two kernels and
its 0/1 536.

*Forced-emptiness theorem (4)*, *HA's G29 and the K1 relation (12)*,
*provenance/instrument (4)*, and *four hostile mutants of my own* (§7).

### 0.4 The headline finding first

**No number in this paper is wrong.** I recomputed every quantity I could
reach and found zero numerical errors. The verdict
`RSQ-SQUARE-FOUND-BRIDGE-EMPTY` with `UNIVERSAL-FOR-THIS-FAMILY` is correct,
and on my analysis **understated** — the emptiness is a theorem valid at every
prime p ≥ 5, not a census result at seven declared primes (§3, F8).

What does not survive is a cluster of five load-bearing claims about the
**instrument**: that the verdict rests on three independent sources; that a
containment was measured; that emptiness was measured at five ladder bases;
that FOUND and EMPTY were separated at the same arena by the same machinery;
and that the held-out verification is predictive with three independent checks.
Four of the five I killed with mutants the declared 57 do not contain.

---

## 1. K1 — THE PERMUTATION-MODULE OBSTRUCTION, DERIVED INDEPENDENTLY

### 1.1 The derivation, re-done

Let α : V = 𝔽_p⁶ → G_C satisfy **S1b** (additive), so A := α(V) is abelian of
exponent p, hence elementary abelian, hence an 𝔽_p-space, and α is 𝔽_p-linear;
and **S3** (injective), so α : V → A is an isomorphism.

**S1a forces Σ_π A Σ_π⁻¹ = A.** From δ_π(α(r)) = Σ_π α(r)⁻¹ Σ_π⁻¹ α(r) = α(Er)
we get Σ_π α(r)⁻¹ Σ_π⁻¹ = α(Er)α(r)⁻¹ = α(Er − r) ∈ A for every r; A is a group,
so Σ_π A Σ_π⁻¹ ⊆ A, and equality follows by finiteness.

Write ρ for conjugation by Σ_π restricted to A — an automorphism of A, hence an
element of GL(A). On the abelian A, δ_π|_A(a) = −ρ(a) + a = (I − ρ)(a).
The square then reads (I − ρ)∘α = α∘E, and since α is an isomorphism:

> **(†)  I − E = α⁻¹ ρ α.**  *I − E is the conjugation automorphism, read
> through α.*

Everything the unit calls an obstruction is a reading of (†):

| reading of (†) | consequence | name |
|---|---|---|
| **(a)** ρ ∈ GL(A) | I − E invertible ⟹ dim ker(E − I) = 0 | **LCB's fixed-point mismatch** |
| **(b)** ρ^{ord(Σ_π)} = I | **(I − E)^{ord(π)} = I** | RSQ's **order obstruction** |
| **(c)** S1c-module: ρ = α ρ_V(π) α⁻¹ | **E = I − ρ_V(π)** | RSQ's **permutation-module obstruction** |

I confirm ord(Σ_π) = ord(π) (π ↦ Σ_π is faithful; measured element orders
{1,2,2,2,3,3}), and the polynomial forms: at ord 2, (I−E)²=I ⟺ E(E−2I)=0 ⟺
E = 2I (E invertible); at ord 3, ⟺ E(E²−3E+3I)=0 ⟺ E²−3E+3I = 0, whose roots
are 1−ω, ω³=1. **The derivation in §7.1 and §8 is sound. I found no error in
it.**

### 1.2 The module form and the all-ones argument, verified

Under S1c-module, ρ_A(π)α = αρ_V(π), so δ_π(α(r)) = α(r) − α(ρ_V(π)r) =
α((I−ρ_V(π))r); S1a and injectivity give **E = I − ρ_V(π)** exactly, in V's own
basis. ρ_V(π) is a permutation matrix (the chart symmetry permutes links), so
(I−ρ_V(π))·**1** = 0, while E·**1** ≠ 0 because det E = ±8 ≠ 0 mod p for p ≥ 5.

My measurement over the unit's 210 rows: **0 equalities; (I−ρ_V)·1 = 0 at
210/210; E·1 = 0 at 0/210; ρ_V a permutation matrix at 6/6 with 6 distinct
images.** Exact agreement.

**R1 extension.** I re-ran the module comparison over the WHOLE covariant
family — 1 440 cells × 7 primes × 5 non-identity wings = **50 400 rows** —
and obtained **0 equalities and 0 E·1 = 0**. So the §8 box's universality
("any prime, any identification, any direction, any dimension") holds well
beyond the 210 rows the unit measured. It holds as **algebra**, not as a
census: see F7.

### 1.3 The 0/20 160 census, verified by my own route

My own linear algebra over exact 𝔽_p, on my own E-construction:
**20 160 rows swept, 0 satisfy, 0 matrix-vs-polynomial disagreements**, and the
diag(6,6,6,4,4,4) positive control satisfies it by both routes. Exact
agreement with the frozen output.

### 1.4 K1's attack: is the module obstruction NEW, or LCB's wall in module clothing?

**It is genuinely new, and I can prove it is not LCB's wall.** The decisive
test is to run the module-*forced* E = I − ρ_V(π) through LCB's own precheck
and through the order criterion. Measured at all 10 (p, π) rows for p ∈ {5,7}:

| | measured |
|---|---|
| dim ker((I−ρ_V(π)) − I) = dim ker(−ρ_V(π)) | **0** at 10 of 10 → LCB's precheck **PASSES** |
| (I − (I−ρ_V(π)))^{ord} = ρ_V(π)^{ord} = I | **True** at 10 of 10 → the order criterion **PASSES** |
| dim ker(I − ρ_V(π)) | **4** (involutions) / **2** (order 3) → the killer |

So the module-forced E clears **both** of the other two walls. What kills it is
a third fact: **E must be invertible, and I − ρ_V(π) is not**. That
contradiction uses **nothing** about the transport side — not |fix δ_π| = 1,
not the p-part, not cardinality. The permutation-module obstruction is
therefore **arena-free AND transport-free**, and it is a strictly disjoint
reading of (†), not a corollary.

By contrast, the **order obstruction IS LCB's wall** — the next term in the
same series. LCB used "ρ invertible"; RSQ uses "ρ^{ord} = I", which implies it.
The paper's own phrase, "it subsumes the fixed-point mismatch, which is its
first-order shadow", is exactly right, and I confirm the implication.

**Supplementary (R1).** At the native arena the module clause also dies on the
transport side, for a reason the unit does not use: S1c-module needs a nonzero
p-element of A centralising Σ_π, and I measure |C_{G_C}(Σ_π)| = 48 (involutions)
/ 18 (order 3), with **0 elements of order 5 and 0 of order 7** in either.
This is a second, independent kill of the module clause at 8 labels. Its
absence is not a defect — the unit's route is stronger because arena-free — but
it is worth recording as corroboration.

**Verdict on K1: the derivation survives. The obstruction is new. Its price is
F12: it is not a fact about HA.**

---

## 2. K2 — THE GROWN-ARENA FOUND CONTROL

### 2.1 Every number reproduces

Rebuilt from the declared growth rule L_m = {0} ∪ (𝔽_2³∖{0})×{1..m}, with S₃
on the 𝔽_2³ factor alone, on my own permutation instrument:

| measured | frozen | R1 |
|---|---|---|
| growth threshold (least m with 7m ≥ 42) / labels | 6 / 43 | **6 / 43** ✓ |
| Σ g_k Σ⁻¹ = g_k^{c_k}, c = (2,2,2,4,4,4) | 6 of 6 | **6 of 6** ✓ |
| generators commute / each of order 7 | yes | **yes / yes** ✓ |
| Ẽ = I − ρ | diag(6,6,6,4,4,4) | **diag(6,6,6,4,4,4)** ✓ |
| (I − Ẽ)³ = I | yes | **(2³,2³,2³,4³,4³,4³) = 1 mod 7** ✓ |
| square violations / record cells | 0 / 117 649 | **0 / 117 649** ✓ |
| injective, image size | yes, 117 649 | **yes, 117 649** ✓ |
| homomorphism violations | 0 | **0** ✓ |
| held cells, H1 | 117 648, 117 648 | **117 648, 117 648** ✓ |
| H2 (my own entry-by-entry route) | 117 648 | **117 648** ✓ |
| distinct fixed-label values | {1,8,15,22,29,36,43} | **{1,8,15,22,29,36,43}** ✓ |
| X-NOSQUARE / X-FLATFIX passes | 0 / 0 | **0 / 0** ✓ |
| analytically-forced exemptions | 1 | **1** ✓ |
| BREAK-HOM square / hom violations | 0 / 1 536 | **0 / 1 536** ✓ |

### 2.2 Audit of the "exactly 1 analytically-forced exemption" — **LEGITIMATE**

K2 asks for this specifically. My finding: **the exemption is sound.**

* Its predicate is `alpha_perm == identity` — a *computed property of the
  candidate*, never a mutant name. RUNBOOK §14 addendum (v13 #208) is
  respected: the gate does not special-case its own falsifier by identity.
* Its count is **gated at exactly 1** (G25), so an instrument that exempted
  more cannot pass; `teeth-off` dies there.
* It is disclosed in the paper's own table.
* I independently enumerated the exempt set with no exemption logic at all:
  it is exactly **{r = (0,0,0,0,0,0)}**, one cell of 117 649.

What the exemption *reveals*, however, is F10: at that cell both declared-to-
fail extensions are TRUE, and off it both are FALSE **by algebra**, so neither
carries contingent information. The exemption is honest; the surrounding claim
that these are "negative controls with teeth" is not.

### 2.3 Is the control genuinely in-family?

**Arena: yes.** The grown family L_m is declared in the paper's own `family`
row, item (vi), before fixture truth, and its growth rule is disclosed as
deviation 5. The construction obeys the pin (S₃ acts on the 𝔽_2³ factor;
label 0 fixed; A ≤ G_C of the grown arena).

**Encoding: no, and disclosed.** Ẽ = I − ρ is read off the arena's own
conjugation action, not from HA. X05 says so plainly.

**A third gap, not disclosed.** I measured whether the control's A is stable
under the *whole* S₃:

| π | ord(Σ_π) | Σ_π A Σ_π⁻¹ = A |
|---|---|---|
| (0,1,2) | 1 | True |
| (1,2,0), (2,0,1) | 3 | **True** |
| (0,2,1), (1,0,2), (2,1,0) | 2 | **False** |

The three involutions do **not** normalise A. So the control is a
single-wing-symmetry (ℤ/3) control: at three of the five non-identity wing
symmetries S1a is not merely unsatisfied but **unposable**, and the module
clause is unposable everywhere on it. That is consistent with the paper's
deviation 6 ("π is a parameter, not a choice") and with X05, but the paper
nowhere states it, and §9.1's table's singular "the wing symmetry" is the only
hint.

### 2.4 What does its existence prove?

K2 asks: bridges at scale, or synthetic detectability only? My answer:

**Mostly the latter, plus one genuinely valuable thing.** The construction is
tautological in the precise sense that the encoding is *defined* as the arena's
own answer: given any Σ-stable elementary abelian A with conjugation exponents
c_k, setting Ẽ := I − diag(c) makes the square an algebraic identity —
δ(α(r)) = ∏ g_k^{(1−c_k)r_k} = α(Ẽr) for every r, given only the two premises
the unit measures (Σ g_k Σ⁻¹ = g_k^{c_k} and [g_i,g_j] = e), both of which I
verify. The 117 649-cell verification therefore confirms an identity, not a
discovery.

What it *does* establish, and what is worth keeping:

1. **Two-way-gate content.** The instrument's FOUND branch is reachable and its
   verifier is not vacuously rejecting. This is required discipline and it is
   correctly supplied.
2. **A sufficiency lemma.** At an arena carrying a rank-6 Σ-stable elementary
   abelian, S1a ∧ S1b ∧ S3 *are* jointly satisfiable at three wings. So the
   emptiness at HA's readout is attributable to the encoding rather than to an
   impossible clause set.

It does **not** establish that bridges exist at scale for any independently
motivated deformation side. §9.1's opening — "The FOUND branch is not
demonstrated only synthetically" — pulls against X05's "its encoding is the
SYNTHETIC I − ρ" and should be reworded.

---

## 3. R1 CONTRIBUTION — THE EMPTINESS IS A THEOREM, AND STRONGER THAN CLAIMED

Before the findings, a result that *helps* the unit. The 20 160-row sweep does
not need to be a sweep.

**Lemma.** Every row of the d = 3 readout, in any slot order, has one of exactly
two sorted profiles: axis links give **(0,0,0,0,0,1)**; diagonal links give
**(0,0,0,1,1,2)**. (Verified exhaustively over all 720 slot orders; row 0 — the
axis link e₀ — is a 0/1 unit vector at **720 of 720**.)

**Theorem.** For every slot order, every direction, and every prime p ≥ 5, the
order criterion fails. Write A for the readout, k for the position of slot
(0,0), so row₀(A) = e_k.

* *ord 2, q→counts:* E = 2I needs row₀ = 2e_k; row₀ is a 0/1 unit vector.
* *ord 2, counts→q:* E = 2I ⟺ A = 2⁻¹I, needing 1 ≡ 2⁻¹, i.e. p | 1.
* *ord 3, q→counts:* E²−3E+3I = 0 at row 0. If k = 0 it reads e₀ = 0. If k ≠ 0
  it forces row_k(A) = 3e_k − 3e₀, i.e. A[k][k] = 3 with A[k][k] ∈ {0,1,2}:
  needs p | 1, 2 or 3.
* *ord 3, counts→q:* equivalent to 3A²−3A+I = 0. If k = 0 it reads e₀ = 0. If
  k ≠ 0 it forces row_k(A) = e_k − 3⁻¹e₀ — exactly one 1, one −3⁻¹, nothing
  else. −3⁻¹ ∈ {0,1,2} at exactly one declared prime, p = 7 (−3⁻¹ = 2); and by
  the Lemma **no** readout row has profile (0,0,0,0,1,2). ∎

I confirmed every step exhaustively (including −3⁻¹ mod p at all seven primes;
only p = 7 is even a candidate) and re-swept the 20 160 rows split by direction
and order: **0 hits in each of the four branches.**

**Consequences.** (i) The result holds at **every prime p ≥ 5**, not only the
seven declared — a strengthening the paper is entitled to. (ii) The
`UNIVERSAL-FOR-THIS-FAMILY` qualifier is earned by algebra, not by coverage.
(iii) All three of G35's "sources" are therefore forced constants (F1, F7, F8),
which is why the instrument-level findings below matter more than they
otherwise would: with the science forced, the gates are measuring their own
plumbing.

---

## 4. FINDINGS — MAJOR

### F1 (MAJOR, K1). The verdict's "three sources that share no deciding variable" is false: source 1 **is** source 2's function.

**Evidence.** `rsq_reposed_square_exact.py`:

```
2734:  "injective_possible": order_criterion(E, p, pord(SIGMA[pi]))
2735:  live_full = sum(1 for r in census_rows if r["injective_possible"])
3418:  src1 = live_full
3419:  src2 = crit_total_hits      # the same order_criterion, summed over 1440 cells
3421:  census_empty = (src1 == 0 and src2 == 0)
```

The 315 census rows map onto (cell, prime, ord(π)) rows that are a **strict
subset** of source 2's 20 160-row domain. Sources 1 and 2 do not merely share a
deciding variable; they are the *same function call*.

**Hostile demonstration (R1 mutant h1, not among the declared 57).** I patched
`order_criterion` to return `True` at (p = 23, ord = 2) only:

```
source 1 -- the census table's own live-row sum : 27      (was 0)
source 2 -- the order-criterion sweep          : 1440     (was 0)
```

Both moved from one perturbation. A genuinely independent source 1 would have
stayed at 0. (G35 and G36 correctly died — the *verdict* is protected; the
*independence claim* is not.)

**Aggravating.** The paper's §7.4 places "rows admitting an injective candidate
… **0** of 315" inside the census table, immediately below "route A vs route B
disagreements: 0 of 315", which invites the reading that routes A/B/C decided
it. They did not: routes A and B compute the S1a+S1b count only. Further, at
the native arena that row is *doubly* forced — every candidate's image lies in a
cyclic group of order p, so |image| ≤ p < p⁶, exactly as §10.1 itself argues on
cardinality.

**Rule violated.** RUNBOOK §13 addendum (v13 #234): *"'two independent routes'
for a census must be genuinely independent computations."*

**Repair.** Make source 1 an actual injectivity measurement over the enumerated
candidates: for each admitted (g, λ), compute |image| = |⟨g⟩| = p and compare
with p⁶. That is a different computation, returns 0 for a different reason, and
survives a perturbation of `order_criterion`. Then restate G35's claim text and
§12 accordingly.

**Verdict impact: none.** Source 2 alone carries the emptiness, and I confirm it
independently and analytically (§3).

---

### F2 (MAJOR, K3). G19 does not measure the containment it claims.

**Evidence.** `crit_cells_set = crit_total_hits` counts **(cell, prime, ord)**
rows out of 20 160; `pre_surv_cells` counts **(cell, prime)** pairs out of
10 080. G19 compares the two integers (`subsumption_holds(0, 4420)` and
`0 < 4420`). No set relation is ever computed, and the two counts range over
different index sets.

**Hostile demonstration (R1 mutant h5).** I made the criterion return `True` at
exactly the 12 rows that are module cells at p = 5, ord 2 — cells whose precheck
**fails** (dim ker(E−I) = 3). That is a genuine violation of the claimed
containment. Result:

```
G19 PASS   criterion 12 <= precheck 4420
```

The gate passed while the containment was false. The only reason G19 has ever
returned a sensible answer is that its numerator is 0.

**Paper claim.** §7.3: "The containment is measured and measured **strict**".
It is neither: strictness here is `0 < 4420`, which says nothing about
containment.

**Repair.** Measure the implication: for each (cell, prime) at which the
criterion holds at some ord, assert that the precheck passes there. With 0 hits
the containment is **VACUOUS** and should be reported as such, with the
implication exercised on the one non-vacuous instance available — the synthetic
positive control diag(6,6,6,4,4,4) at p = 7, whose fixed space I verify is
trivial (Ẽ − I = diag(5,5,5,3,3,3) mod 7, invertible). The subsumption itself
remains a correct theorem; only the word "measured" must go.

---

### F3 (MAJOR, K2/discipline). S4's per-base emptiness is **typed**, not measured.

**Evidence.**

```
s4_rows.append({"base": nm, "K_order": len(K), "live_primes": live,
                "census_empty_at_this_base": True})          # literal
scale_rows = [{"scale": "native", "labels": NLAB, "census_empty": True},  # literal
              {"scale": "grown",  "labels": n_star, "census_empty": bool(empty_at_grown)}]
```

G28's predicate reads `len(s4_rows) == 5` and `all(r["census_empty"] for r in
scale_rows)` — it never reads `census_empty_at_this_base` at all. The literal
`True`s are nonetheless carried into the receipt at
`tables.controls.S4_bases` as if measured.

**Hostile demonstration (R1 mutant h2).** I flipped the ord6 base's value to
`False`:

```
G28 PASS   S2 stratification carried True; S4 bases 5, scales 2
```

The gate is blind to it.

**Paper claim.** §9.5: "the emptiness is **measured** at each of TB3's five
declared ladder bases". It is not. The only per-base measurements are |K| and
the primes dividing it.

**Aggravating.** The deciding quantity, (I − E)^{ord(π)} = I, contains **no
reference to the base completion Q**. Base-invariance is therefore forced by
the shape of the criterion, not a functoriality finding. Reporting five bases
"whose defect subgroups differ by more than two orders of magnitude" as evidence
that the verdict does not move overstates what varying them could ever have
shown.

**Rule violated.** The failure catalogue's *"counts computed, never typed"*
(#24) and RUNBOOK §13 addendum (#234) on derived-in-gate verdicts.

**Repair.** Either run the census at each base, or replace §9.5's sentence with:
"the deciding criterion is base-independent by construction; |K| is measured at
each base and ranges over 1 … 2 520, confirming the bases are genuinely
different objects."

---

### F4 (MAJOR, K2). §9.3's "separated by the ENCODING, not by the arena, the prime, or the instrument" is not what is computed.

**Evidence.**

```
empty_at_grown = None
if gens is not None:
    Ereal = encoding_matrix(tuple(range(NV)), "counts->q")
    empty_at_grown = empty_branch(not order_criterion(Ereal, pc, 3))
```

The 43-label arena appears only in the `gens is not None` guard. Nothing about
the grown arena enters the EMPTY decision — it is one 6×6 matrix power at p = 7.

**Hostile demonstration (R1 mutant h3).** I replaced the guard with `if True`,
deleting the grown arena from the EMPTY branch entirely:

```
G26 PASS   HA's encoding at the grown arena: EMPTY True
```

Unchanged.

**Three coordinate mismatches, not one.** (i) *Instrument*: FOUND is a literal
117 649-cell permutation verification; EMPTY is a 6×6 matrix identity. (ii)
*Arena*: FOUND is at 43 labels; EMPTY is at no arena. (iii) *Cell*: EMPTY uses
the natural identification, counts→q — a MODULE cell already declared
**STILLBORN** at dim fix = 3 — while FOUND's Ẽ has trivial fixed space. The
paper's "changing nothing else" changes all three.

**Rule violated.** RUNBOOK §15 addendum (v13 #196): *"a like-for-like comparison
must match EVERY coordinate of the compared objects … before any class contrast
is claimed."*

**The conclusion is nonetheless true**, because the order criterion is necessary
at any arena and HA's E fails it everywhere (§3).

**Repair.** State it as: "HA's readout fails a condition that is necessary at
*any* arena; the synthetic Ẽ satisfies it and is realised at the grown arena."
Drop "changing nothing else", "the same machinery", and "not by the instrument".

---

### F5 (MAJOR, K2). The held-out verification has no out-of-sample content, and H1/H2/H3 are one check, its duplicate, and a counter.

**(a) Nothing is fitted.** `gens` and `Ẽ` come from `control_blocks(m, p, cs)`
before any record cell is read. `fit` is used **only** to exclude one cell from
the held tally:

```
if r != fit:
    h_tot += 1
    if lhs == rhs:
        h1 += 1
        h2 += 1
    ...
    h3 += 1
```

§9.2's "The candidate is admitted on the FIT cell alone and then verified out of
sample", and G25's identical wording, describe an admission procedure that does
not occur. With no parameter estimated from FIT, HELD carries no predictive
information.

**(b) H1 and H2 are the same boolean.** Both are incremented inside one
`if lhs == rhs`, where `lhs` and `rhs` are permutation tuples — a tuple equality
*is* the entry-by-entry comparison. The paper's table lists them as two
verifications at 117 648 each. I recomputed H2 through a genuinely separate
element-wise loop and got 117 648, so the *number* is right; the *independence*
is not.

**(c) H3 verifies nothing.** `h3 += 1` executes unconditionally for every held
cell. `H3_fixed_label_counts_verified: 117648` is the held-cell count. The only
content in that row is `distinct_fixed_label_values`, which is gated
(`> 1`) — and which I show is analytically forced: pfix(δ(α(r))) = 1 + 7·#{k :
r_k = 0}, hence exactly {1, 8, 15, 22, 29, 36, 43}.

**(d) The square itself is forced.** Given the two measured premises, the
identity δ(α(r)) = α(Ẽr) holds for every r. So H1 = 117 648/117 648 confirms
algebra.

**Repair.** Either fit something (e.g. recover Ẽ's diagonal from the FIT cell
and predict the rest), or rename §9.2 an *exhaustive verification* and delete
the FIT/HELD language. H2 must build the defect permutation by a route that does
not read `rhs`; H3 must compare against a *predicted* fixed-label count.

---

## 5. FINDINGS — MODERATE

### F6 (MODERATE, K1/K3). The criterion's "two independent routes" are one route.

`order_criterion` computes (I−E)^ord = I by matrix power; `order_criterion_
polynomial` computes E = 2I / E²−3E+3I = 0. Given E invertible these are
identically the same condition — the paper says so itself in §7.1
("**Equivalently**, since E is invertible") and then calls them "independent
routes" one paragraph later. Their difference is the factor E in
(I−E)³ − I = −E(E²−3E+3I). RUNBOOK §13 addendum (#234): *a pair related by an
algebraic identity is one route*. **Repair:** relabel as a redundant-encoding
check, or add a genuinely third route (e.g. charpoly(E) mod p against
(x²−3x+3)³).

### F7 (MODERATE, K1). §8's 210-row table is analytically forced in all three columns; source 3 is a constant.

(I−ρ_V(π))·**1** = 0 for any permutation matrix; E·**1** ≠ 0 for any invertible
E; hence the equality count is 0 with no measurement. All three measured columns
are theorems, and `mod_equal` — G35's source 3 — cannot be nonzero for any
invertible E at any cell, prime or wing. RUNBOOK §14 addendum (#208):
*analytically-forced clauses are disclosures, not must-pass gates.* The only
contingent clause in G23 is the synthetic non-permutation control, and that
control runs *outside* `module_obstruction_measured` (it is a 2×2 kernel-dim
call), so the audited function's positive branch is never exercised.
**Repair:** mark §8's table a disclosure; route the positive control through
`module_obstruction_measured` itself so it has a two-way gate.

### F8 (MODERATE, K1/K3). The 20 160-row sweep is likewise forced — see §3.

Not a defect in the result; a defect in its description. §7.2 and §12 present
0/20 160 as measured coverage. It is a theorem (§3), valid at every p ≥ 5.
**Repair:** state the theorem, keep the sweep as its confirmation, and widen the
prime scope in the qualifier's supporting text.

### F9 (MODERATE, K5). G33's "tested set" is never tested over.

`tested = selftest_set(declared, verdict_selected)`; `selftest_set` returns its
first argument unchanged; `tested` is used **only** in `len(tested) == ncells`
and `len(tested) > …`. No self-test iterates it. The RUNBOOK §14-addendum
property ("a symmetry gate's tested set is fixed by declaration, never selected
by the very verdicts under audit") is named but not measured; `selftest-select`
proves only that a shorter list is shorter. **Repair:** have the covariant
precheck/criterion sweeps consume `tested`, so shrinking it shrinks a measured
sweep.

### F10 (MODERATE, K2/K5). Neither declared "tooth" is contingent.

X-NOSQUARE predicts α(r) ∈ fix δ, and fix δ = {e} is §4.2's own theorem.
X-FLATFIX predicts α(r) ∈ C(Σ), and α(r) ∈ C(Σ) ⟺ (c_k − 1)r_k ≡ 0 ∀k ⟺ r = 0,
since c_k − 1 ∈ {1,3} is invertible mod 7. I verify with no exemption logic:
each is true at exactly **1** of 117 649 cells, namely r = 0. So "0 passes" is
forced, and §9.2's "declared in advance to fail" controls have no teeth. (The
exemption itself is sound — §2.2.) **Repair:** report both as forced
disclosures; BREAK-HOM is the only teeth-bearing control here.

### F11 (MODERATE, K5). Route C's "measured majority" is the complement of a hyperplane.

For a rejected covector λ, violations = #{r : w·r ≠ 0} with w = (1−s)λ − λE ≠ 0,
which is p⁵(p−1). I compute 5⁵·4 = **12 500** and 7⁵·6 = **100 842** — exactly
the paper's numbers, analytically. §7.4's "the rejected control violates it at a
measured majority, so the verification is not vacuous" is true but forced.
Separately, BREAK-HOM (§9.4) IS a genuine control — I reproduce 0 square
violations of 117 649 and 1 536 S1b violations — but it lives at the **native
8-label arena** with a rank-1 α, while sitting inside §9's grown-arena section;
the paper never says which arena it is at.

### F12 (MODERATE, K1 — scope). §8's obstruction is not a fact about HA's readout.

The contradiction is "E invertible" vs "I − ρ_V(π) singular". **Any** invertible
deformation-side readout fails it, at any prime, identification, direction and
dimension; and no transport-side fact enters. The honest headline is therefore
*stronger* than the one printed: *the module-level square closes for no
invertible readout whatever, whenever the chart symmetry acts on the record
datum space by permutations.* §16 Open 2 approaches this; §8's box and §12's
"named obstruction" do not, and as written they attribute to HA a failure HA
does not own. **Repair:** one sentence in §8 and one in §12.

---

## 6. FINDINGS — MINOR

**F13.** The **210** rows are not reconstructible from the paper. They are
6 cells (4 MODULE + 2 LEX) × 7 primes × 5 non-identity wings. §8 states only
"rows swept 210". The 2 LEX cells are not S₃-equivariant, so by §5.1's own
criterion the module clause is not natively posable there; including them adds
70 rows and no information. *Repair:* state the factorisation, and either drop
the LEX cells or say why they are included.

**F14.** "**3-dimensional fronts**" is a misnomer. `ReducedCarrier3` has front
sector 𝔽_p^k with k **measured = 2** (printed in the output table) and address
register 𝔽_p³. §3.1's "the reduced carrier is then built with 3-dimensional
fronts" contradicts the quote box two lines below it ("the 3-dimensional
**address register**"), which is correct. The pin's phrasing is the origin; the
paper propagates it. *Repair:* one word.

**F15.** The twisted-cocycle clause in G10 cannot fail. F₂(π, XY) =
F₂(π,Y)·Y⁻¹F₂(π,X)·Y is an identity in any group for any Σ (I verify the algebra
and the 0/150). `cocycle_bad == 0` is an analytically-forced must-pass clause
(RUNBOOK §14 addendum #208), and no declared mutant perturbs `form_F2`.
*Repair:* demote to a disclosure.

**F16 (freeze hygiene).** A delivery run of the frozen script **rewrites**
`rsq_reposed_square_output.txt` and `rsq_reposed_square_receipt.json` in place
(`WRITE_ARTIFACTS = DELIVERY_RUN and not SELFTEST_ONLY`). Any reviewer who
reproduces the unit mutates the pinned artifacts. It was safe here only because
the run is deterministic — I re-verified both SHAs after the rewrite and they
are unchanged. *Repair:* a `--verify` mode that writes to a temp path and diffs.

**F17.** `order_criterion` and `module_obstruction_measured` — the functions
carrying verdict sources 1/2 and 3 — are absent from G37's 13 helper probes.
Given F1 and F7 this is where a probe would have been worth most.

**F18 (unstated lemma, in the unit's favour).** Route A's restriction to
candidates α(r) = g^{λ(r)} with ⟨g⟩ cyclic of order p is a **complete** census
at the native arena, because v_p(5040) = 1 at p = 5, 7 and 0 at p ≥ 11 (I
verify), so every elementary abelian p-subgroup of G_C = S₇ is cyclic of order p
or trivial. The unit never states this, yet it is exactly what makes route A a
census rather than a sample. It would also fail at a grown arena, which matters
for Open 1. *Repair:* state and gate it.

---

## 7. WHAT I COULD NOT BREAK

* **The mathematics.** Both derivations — the order criterion and the module
  form — are correct. I re-derived each from scratch and found no gap. The
  hidden steps (A elementary abelian; additive ⟹ 𝔽_p-linear; Σ_π-stability from
  S1a; conjugation an automorphism hence 𝔽_p-linear; ord(Σ_π) = ord(π)) all
  hold.
* **Every number.** 84 recomputations, zero disagreements with the frozen
  artifacts and zero disagreements with the paper's tables.
* **HA at d = 3 (K4).** I rebuilt the residual by hand from the declared A-axis
  drag rule: G3-OFF → q = [[2,1,0],[1,2,0],[0,0,2]]; q⁻¹ = ⅙[[4,−2,0],[−2,4,0],
  [0,0,3]]; Λ = diag(½,½,½); ω(x*) = (1,1,1); **ρ(x*) = (1/6, 1/6, 0)** — the
  paper's value, nonzero at **1 of 27** sites (ω vanishes off x* because N is a
  point indicator and supp(M) misses x* − e_j). All seven ρ mod p and all seven
  carriers p^{k+3} = p⁵ reproduce. **G29 at d = 3 stands.**
* **K4's pin-reading deviation (X01) is LEGITIMATE and forced.** A map
  𝔽_p³ → 𝔽_p⁶ has neither determinant nor spectrum, so the pin's "det 8,
  spectrum {1,1,1,2,2,2}" is unreadable under the literal 3→6 reading. More
  decisively, the *source* of the requirement — R2-LCB's F-10(d) — itself says
  "the readout becomes **6×6** with det = 8 and spectrum {1,1,1,2,2,2}". The
  paper reads the pin the way the pin's own source wrote it, and discloses the
  deviation. No finding.
* **The thresholds table (K4).** All 7 rows × 4 columns, including the d = 2
  anchors 16 and 22 against LCB §12.3.
* **The p = 7 meeting (K3).** Unique across the declared primes, realised
  in-arena only at the two order-3 wing symmetries, and landing on a cell the
  precheck has already killed. The framing — "what the meeting buys is a
  non-empty S1a + S1b census and nothing more" — is correctly and honestly
  hedged; I could not strengthen the criticism.
* **The declared census-cell rule (K5).** I rebuilt all 9 cells from the rule
  as stated, including both lex-first SET cells, and got an exact match. The
  rule is genuinely stated before fixture truth and genuinely returns cells of
  every precheck status.
* **Instrument hygiene generally.** No floats; no gate predicate references
  mutant identity (G03 scans for it); the freeze counter is real and
  `freeze-lax` dies; the cache discipline (2 000 bypasses, 0 self-test hits,
  against 9 501 pre-warmed hits) is correct §14-addendum practice; all 38
  must-pass gates are mutant-covered.

---

## 8. GRADE

The science is right and, on my analysis, stronger than the paper claims. The
verdict `RSQ-SQUARE-FOUND-BRIDGE-EMPTY` with `UNIVERSAL-FOR-THIS-FAMILY` is
correct; the emptiness is a theorem valid at every prime p ≥ 5 (§3); the two
obstructions are correctly derived; the permutation-module obstruction is
**genuinely new** relative to LCB's fixed-point mismatch and I proved it is not
the same wall (§1.4); the grown-arena control's every number reproduces and its
one exemption is legitimate (§2.2); and there are **zero false numerical
results**.

Against that: five load-bearing claims about the **instrument** are false as
implemented — three independent verdict sources (F1), a measured containment
(F2), emptiness measured at five bases (F3), FOUND/EMPTY separated at one arena
by one machinery (F4), and a predictive three-check held-out verification (F5).
Four of the five I killed with mutants the declared 57 do not contain. Each
violates a RUNBOOK rule engraved specifically to prevent it (§13 addendum #234;
§14 addendum #208/#219; §15 addendum #196; the catalogue's "counts computed,
never typed"). None moves the verdict, none is a false number, and all are
repairable — F1, F2 and F5 need bounded instrument changes; F3, F4, F7, F8,
F10–F12 need corrected prose and re-scoped claims.

That is not a rejection, and it is not a clean acceptance.

$$\boxed{\textbf{ACCEPT-WITH-FIXES}}$$

**Required before terminal (blocking):** F1, F2, F3, F4, F5.
**Required as scope/wording corrections:** F6, F7, F8, F10, F11, F12, F14.
**Recommended:** F9, F13, F15, F16, F17, F18 — and the §3 theorem, which the
unit should claim.

*Recomputations performed: 84. Numerical disagreements with the frozen
artifacts: 0. Hostile mutants written and run beyond the declared 57: 4
(h1, h2, h3, h5); 4 of 4 exposed a false instrument claim while leaving the
verdict intact.*
