# The grading no-go across the program's scales: the spacing, the gravitational coupling, and the volume

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, companion to publishable Paper XI, version 2026-06-15. Every load-bearing line is tagged by epistemic status: **[EXTERNAL]** = standard graded-ring / dimensional-analysis content used as machinery, not claimed as new; **[NO-GO]** = the program-internal proved obstruction this note assembles; **[OPEN]** = a disclosed, unproved residue. All numeric claims were verified at mpmath `dps ≥ 100` and symbolically (sympy) where exact; the receipt scripts are `v7/code/p3_d_nogo.py` and `v7/code/p5_cm_calibration.py`.

## Abstract

Within the sealed-records program, the parent Paper XI proved a *single* negative theorem about gravity — the records derive the Einstein equation of state but provably cannot fix Newton's `G` — and located the obstruction in one place: under the length-rescaling gauge `g_λ: l → μl`, every intrinsic record functional is weight-zero while the area density `σ_A ∼ 1/l²` (in bijection with `G` via `G·σ_A = 1/4`) is weight `−2`. This companion makes the *scope* of that one wall explicit. The same gauge induces an **additive grading homomorphism** `weight(XY) = weight(X) + weight(Y)`, and the weight-0 (dimensionless) record functionals — the only ones the records may carry — fall into an exhaustive **trichotomy**: *ratio-of-twins* (the absolute scale appears and cancels, so the functional is consistent with every scale), *scale-blind* (the scale never entered, so the functional carries zero information about it), or *wrong-tier* (a genuine record number on the wrong axis). No member of this trichotomy can fix an absolute scale. We then run that one structural fact against the program's *other* two scale-shaped unknowns and find it forbids each in the same way: the seal **spacing** `d` (weight-zero on both its axes, so no record-derived dimensionless coefficient can pin its absolute value — receipt `p3_d_nogo.py`) and the per-species **gravitational coupling** `c_m = Gm²/ℏc = (m/M_Planck)²` (weight-zero, hence permitted, but factoring exactly as `c_m = (G·σ_A)·(m²/σ_A)` so that the absolute area density cancels and the matter content is relocated entirely into a mass-amplitude the gravity sector is complete-and-blind to — receipt `p5_cm_calibration.py`). **Honest and up front:** the grading-homomorphism and weight-zero-subring structure is *standard* — it is the algebra of a graded ring and the content of dimensional analysis (Buckingham-Π; Coleman–Weinberg dimensional transmutation yields a ratio, never an absolute scale). This note proves no new mainstream theorem. Its one program-internal contribution is a *positioning statement about the records*: the **same** scale wall that forbids an emergent Newton constant (parent XI) forbids fixing the spacing `d` and the coupling `c_m`, and `G` — one external absolute length unit — is the single input that closes all three at once. The result is a no-go with one shared open premise (gate G1) and one explicitly permitted lane (a matter-sector calibration), not a derivation of any of the three numbers.

---

## 1. What is external, what is the contribution

This is a companion note, and the strip test has already run on it; we state plainly where the machinery comes from before using it.

**External / standard. [EXTERNAL]** Three pieces of the argument are textbook and are *used*, not claimed:

- *Graded-ring algebra.* A one-parameter group action `g_λ: l → μl` on a ring of functionals defines a `ℤ`-grading; on a multiplicative ring the weight (degree) map is an additive homomorphism `weight(XY) = weight(X) + weight(Y)`, and the weight-0 elements form a subring. This is the definition of a graded ring, nothing more.
- *Dimensional analysis (Buckingham-Π).* That the dimensionless combinations are exactly the weight-0 ones, that they are the only quantities a scale-free theory can predict, and that fixing the absolute scale needs one external unit, is the content of the Π-theorem. The "trichotomy" below is a bookkeeping refinement of it, not a new theorem.
- *Dimensional transmutation (Coleman–Weinberg).* That a marginal coupling running can manufacture a *scale ratio* (a `Λ_QCD/μ`-type number) but never an absolute scale is standard. Parent XI already identifies the gravity no-go as "the same structural fact as QCD's dimensional transmutation" (XI §2.4).

**Program-internal contribution. [NO-GO / positioning]** What is *this program's* — and it is a statement *about the records*, not a mainstream theorem — is the **unified scope** claim: the one weight-counting wall behind Paper XI's "no emergent Newton constant" is *the same wall* behind two further program unknowns, the seal spacing `d` and the per-species coupling `c_m`, and it forbids fixing each by exactly the trichotomy mechanism. The contribution is therefore (i) a *no-go* — no record-internal dimensionless coefficient fixes the absolute scale of `d` or `c_m` — and (ii) a *positioning* — `G` (one external absolute length) is the single input that closes all three, so the three unknowns are not three holes but one. No new physical constant is computed; the claim is that three of them are, structurally, the *same* free input.

We carry both halves forward without conflating them: every "homomorphism / weight-0 / trichotomy" line below is [EXTERNAL] machinery; every "and therefore the records cannot fix `d` / `c_m` / `G`, and `G` closes all three" line is the [NO-GO] contribution.

---

## 2. The one gauge, the one homomorphism

The record-length gauge `g_λ: l → μl` holds all sealed data fixed and rescales the single dimensionful primitive — the seal-spacing length (parent XI §2.1; the seal rate attack there confirms it is the *unique* dimensionful primitive). The degree map

  `weight(X) = log[X(μl)/X(l)] / log μ`

is, because the action is a one-parameter group on a multiplicative ring, an **additive grading homomorphism** [EXTERNAL]:

  `weight(XY) = weight(X) + weight(Y)`, `weight(X/Y) = weight(X) − weight(Y)`.

On the program's generators it reads (sympy-exact, residual `0`, `p3` check 3a; reproducing parent XI §2.1):

  `weight(A_rec = l²) = +2`, `weight(σ_A = 1/l²) = −2`, `weight(G) = +2`, `weight(l_step) = +1`, `weight(m ∼ 1/l) = −1`, `weight(pure count) = 0`.

A generic record monomial `W_*^a κ^b l_step^c σ_A^e` carries `weight = 2b + c − 2e`. "Dimensionless" is exactly `weight = 0`, which **forces** `c = 2(e − b)` (`p3` check 3b, sympy-exact): the absolute-length power `c` is even and is carried entirely by `κ`/`σ_A` powers that cancel it. There is no monomial — and, since any transcendental functional of weight-0 ratios is itself weight-0, no functional — that is dimensionless yet retains an absolute length. Even an irrational/anomalous weight cannot leak length: `a + b√2 = 0` over `ℤ` only for `a = b = 0` (`p3` check 3c, sympy). So the weight-0 subring is exactly the records' eligible output, and it contains no absolute scale. This is the parent XI weight-counting lemma, stated once as the homomorphism whose corollaries §4–§6 are.

---

## 3. The weight-0 trichotomy

Restricting to the eligible (weight-0) functionals, an exhaustive case split governs whether any of them can fix an absolute scale. The split is [EXTERNAL] (it is the content of the Π-theorem, organized by *why* a given dimensionless number is dimensionless); its use as a *no-go template* applied uniformly to `d`, `c_m`, and `G` is the contribution.

A weight-0 record functional is in exactly one of three bins:

- **ratio-of-twins (circular).** The absolute scale appears in the functional and *cancels*: e.g. `G·σ_A = 1/4`, `κ·σ_A = 2π` (with `κ = 8πG`), `G·Λ²`. These are invariant under `l → μl` for *every* `μ` (`p3` check 6: `G·σ_A = 0.25` and `κ·σ_A = 2π` at `μ = 1, 1.7, 3`, residual `0`), hence consistent with every absolute scale — so consistent with every candidate value of any scale-shaped unknown. A ratio-of-twins *constrains a ratio*, never a scale.
- **scale-blind (vacuous).** The absolute scale never entered: e.g. the Srednicki area coefficient `a = 0.295417`, the capacity ratio `U_G = 1`, the graviton fraction `4/9`, `η/s = 1/4π`. These carry zero information selecting any scale because the scale is not among their arguments.
- **wrong-tier / wrong-axis.** A genuine record number, but on the wrong footing to be the unknown in question: e.g. the per-seal content ceiling `W_* = 0.364785` is a real Tier-A constant, but on the *amplitude* axis (it is the source coefficient `κ = W_*` of the firing law), not the spacing/length axis (`p3` §5). Equating it to the spacing is intra-tier bookkeeping, not a cross-tier scale constraint.

The three requirements an absolute-scale fixer would need — *record-derived* ∧ *scale-independent* ∧ *carries absolute length/scale* — are mutually exclusive across the three bins, and there is no fourth bin (`p3` check 3b: the trichotomy is exhaustive). This is the lever. The rest of the note is three applications of it.

---

## 4. Application I — the seal spacing `d` [NO-GO]

The first scale-shaped unknown is internal to the click-law: the seal spacing `d`, left open after Paper II forced only its ceiling `d ≤ W_*`. Two facts (receipt `p3_d_nogo.py`) place it under the §3 lever.

**`d` is weight-0 on both its axes.** The per-seal *content* `C(h)` is a Kullback–Leibler value in nats (a pure number); the *evidence clock* that fires each seal is `I ∼ Exp(1)` with `E[I] = Var[I] = 1` (`p3` check 1, exact quadrature at `dps = 140`), in evidence units. Both are dimensionless; turning the mean-1 firing into a *content* spacing would need a conversion rate `κ` (content per unit commit-order) that is precisely the one weight-bearing quantity the no-go forbids the records to supply. So `d` is weight-0 throughout — which, by §2, makes it *eligible* but, by §3, gives no route to its absolute value.

**No record-derived coefficient fixes it.** Because `d` is weight-0, the scale no-go *permits* a derived dimensionless gravitational coefficient to equal a per-seal content and pin `d` without manufacturing the forbidden length — and this is exactly the route the §3 trichotomy forecloses. Every record-derived dimensionless candidate is ratio-of-twins (circular: scale cancels), scale-blind (vacuous), or wrong-tier (`W_*` is an amplitude, not a spacing). The strongest numerical near-miss — `θ_B² = 0.295598` against the Srednicki coefficient `a = 0.295417`, gap `1.8 × 10⁻⁴` — is refuted *algebraically*, not merely numerically: `θ_B = tanh η_B = e^{−η_B}` is a degree-3 algebraic irrational (root of `t³ + t² + t − 1`; `e^{η_B}` is the tribonacci constant), and `θ_B²` is the root of the irreducible `s³ + s² + 3s − 1` (`p3` check 4/4b, sympy; both irreducible over `ℚ`), numerically distinct from `a` with the corpus partial-wave sequence converging *away* from it. The one structurally honest bridge generator, the Chamseddine–Connes spectral action, lands on the weight-0 invariant `G·Λ²` (a ratio-of-twins) and fixes only `G/l_step²`, never the absolute scale — independent of its coefficient's value; its conjectured "factor-`2π` gap" is *plausibly* a moment-labelling ambiguity (`M0 = ∫e^{−2πu}du = 1/(2π)`, `M1 = ∫u e^{−2πu}du = 1/(2π)²`, `M0/M1 = 2π` exactly, `p3` check 5), tagged `[CONJECTURED]` and immaterial to the no-go.

So the spacing's absolute value is closed to record-internal coefficients by the *same* trichotomy that closes `G` — the records, having no absolute length, cannot supply `d`'s either. (Receipt `p3_d_nogo.py`, 9 machine checks, all pass.)

---

## 5. Application II — the per-species gravitational coupling `c_m` [NO-GO / PERMITTED]

The second scale-shaped unknown is the dimensionless gravitational coupling-per-species, the gravitational analog of the fine-structure constant:

  `c_m = Gm²/ℏc = (m/M_Planck)²` — `c_m(electron) = 1.7518 × 10⁻⁴⁵`, `c_m(proton) = 5.9061 × 10⁻³⁹` (`p5` check 1; the weakness of gravity made dimensionless).

**It is weight-0, hence permitted.** `weight(c_m) = weight(G) + 2·weight(m) − weight(ℏc) = (+2) + 2(−1) − 0 = 0` (`p5` check 2, sympy), and it is gauge-invariant: `l → μl` sends `G → μ²G`, `m → m/μ`, so `Gm²` is unchanged (`c_m(μl)/c_m(l) = 1` to `< 10⁻⁴⁰`, `p5` check 2b). Equivalently `c_m = (m/M_Planck)²` is a squared mass ratio: the absolute scale cancels. So, unlike `G` or `σ_A`, `c_m` is *not* forbidden by the no-go — it lives in the weight-0 subring the records do carry. This is the one lane the parent XI flags as eligible (XI §2.4: "*not* the dimensionless gravitational coupling-per-species `c_m`, which is weight-zero, intrinsic, and therefore eligible").

**But it is a ratio-of-twins whose matter content is relocated out of gravity.** `c_m` factors *exactly* as

  `c_m = γ_G · ν_m² = (G·σ_A)·(m²/σ_A) = Gm²` — the area density `σ_A` cancels identically (`p5` check 3, sympy-exact),

with `γ_G = G·σ_A = 1/4` a ratio-of-twins convention (bin 1 of §3, fixed by the gauge, not physics) and the matter content *entirely* in the mass-amplitude `ν_m = m/√σ_A`. So fixing `c_m` is fixing `ν_m`, a matter-sector question — and the gravity sector is **complete-and-blind** to it: every executed gravity identity holds for *any* `c_m`, because `κ·σ_A` and `G·σ_A` are functions of `G, σ_A` alone (`p5` check 3c: `d/dc_m = 0`; the inherited toy-value scan passes `c_m = 12` and `c_m = 1200` identically). `c_m` is therefore *currently free* — one free dimensionless coupling per species, the strength-axis analog of the no-go's free unit — and its value awaits an unbuilt matter sector: the physical `ν_m(e) ≈ 8.4 × 10⁻²³` sits ~22 orders below the corpus's toy lattice gaps (`p5` check 3b), so those gaps pin nothing physical. The same algebraic refutation applies to the strongest record-number coincidence (`θ_B²` vs Srednicki `a`, `p5` check 5). (Receipt `p5_cm_calibration.py`, 10 machine checks, all pass.)

The verdict for `c_m` is two-sided and must not be collapsed to one side: *permitted* (weight-0, not forbidden) but *not gravity's to give* (complete-and-blind), so it is a free per-species calibration, not a hole in record gravity — exactly as the Einstein equations do not determine the electron mass.

---

## 6. The unified scope, and the one external input that closes all three

The three scale-shaped unknowns — Newton's `G` (parent XI), the spacing `d` (§4), the coupling `c_m` (§5) — are not three independent gaps. They are three faces of the *one* weight-counting wall of §2:

| unknown | weight footing | why no record coefficient fixes its absolute value |
|---|---|---|
| Newton's `G` / `σ_A` | weight `+2` / `−2` (parent XI §2) | not weight-0: forbidden outright; `G·σ_A = 1/4` is a ratio-of-twins (bin 1) |
| seal spacing `d` | weight-0 on both axes (`p3`) | permitted but every candidate is bin-1/2/3; absolute scale needs a conversion `κ` the records lack (§4) |
| coupling `c_m` | weight-0 (`p5`) | permitted but `c_m = (G·σ_A)·ν_m²` is a ratio-of-twins times a relocated matter amplitude; gravity is blind to it (§5) |

The single external datum that closes the column is **one absolute length unit** — equivalently, fixing `G` (parent XI: "the missing datum is exactly one absolute unit"). With one absolute length supplied: `σ_A` and `G` are set; the spacing `d` acquires a content↔commit-order conversion `κ` and so a value among its admissible modes; and `c_m`'s mass-amplitude `ν_m` acquires its scale. So `G` is not merely *a* missing input — it is *the* input, and the three unknowns are one. [NO-GO / positioning]

Two honest residues remain, neither of which a record coefficient can discharge. (i) **The shared open premise.** The weight-0 classification and the no-record-coefficient closures (for `d` and `c_m`) rest, like the parent `G` no-go, on the single isolated premise **gate G1** — no sealed law consumes the record area `A_rec` outside the continuum labeling map `ℓ` — proved-finite for the executed corpus but with its universal quantifier an open scope assumption (parent XI §2.1; `p3` §7). The `c_m` *blindness* result is G1-free (it leans only on the equivalence-principle theorem and the algebraic `c_m`-independence of the gravity invariants), but the weight-0 classifications are not. (ii) **One permitted lane stays open.** `c_m` is permitted and currently free; its value is relocatable to a matter sector that does not yet exist, sharing the spacing's mode-canonicalization sub-problem while carrying the extra matter-sector burden (§5). That lane is a forward obligation, not a route to fixing the absolute scale.

The one-line scope: **the same grading wall that forbids an emergent Newton constant forbids fixing the seal spacing and the per-species coupling; all three are closed to record-internal coefficients and opened by exactly one external length unit — they are one input, not three.**

---

## 7. What this companion claims and does not

It **claims**, with receipts: that the length gauge induces an additive grading homomorphism whose weight-0 subring is the records' only eligible output and contains no absolute scale (§2, `p3` checks 3a–3c); that the weight-0 functionals fall into an exhaustive trichotomy none of whose bins fixes an absolute scale (§3); and that running this one lever against the program's other two scale-shaped unknowns forbids fixing the absolute value of the seal spacing `d` (§4, `p3`) and the per-species coupling `c_m` (§5, `p5`), so that `G` — one external absolute length — is the single input closing all three (§6).

It does **not** claim: any new mainstream theorem — the homomorphism, the weight-0 subring, the Π-theorem trichotomy, and dimensional transmutation are standard and used as machinery (§1); a *value* for `d`, `c_m`, or `G` (none is derived; the contribution is that the records cannot supply them); that `c_m` is forbidden (it is *permitted* — weight-0 — but blind-to-gravity and currently free, §5); or that the no-go is unconditional (it is airtight *modulo* gate G1, the shared open premise, §6). The contribution is a statement *about the records* — a unified no-go plus a positioning of `G` as the one closing input — not a calculation of a constant of nature. The honest one-line summary: **three of the program's scale-shaped unknowns are one external length unit in disguise; the grading wall that hides Newton's `G` hides the spacing and the coupling too, and the same single external datum reveals all three.**

---

## Reproducibility

Every numeric quantity was computed in mpmath at `dps ≥ 100` (the spacing receipt at `dps = 140`; the coupling receipt at `dps ≥ 60` for CODATA SI inputs) and sympy-exact where structural; never float64 for the cancellation-heavy weight balances. Two receipts in `v7/code/`:

- **`p3_d_nogo.py`** (9 machine checks, all pass): the evidence-clock moments `E[I] = Var[I] = 1` (§4); the mode-dependent contents `C(η_B) = 0.156109…`, `C(h_*) = 0.109004…`, both `< W_* = 0.364785…` (§4); the additive grading homomorphism and its dimensionless case-split `c = 2(e − b)` with no surviving length, and the irrational-weight leak closed (§2–3); the tribonacci algebraicity (`θ_B` root of `t³+t²+t−1`, `θ_B²` of `s³+s²+3s−1`, both irreducible over `ℚ`; gap to Srednicki `1.8 × 10⁻⁴`) (§4); the collar moments `M0 = 1/(2π)`, `M1 = 1/(2π)²`, `M0/M1 = 2π` (§4); and the SIGMA-SPLIT invariants `G·σ_A = 1/4`, `κ·σ_A = 2π` invariant under `l → μl` (§3).
- **`p5_cm_calibration.py`** (10 machine checks, all pass): the hierarchy values `c_m(e) = 1.7518 × 10⁻⁴⁵`, `c_m(p) = 5.9061 × 10⁻³⁹`, `c_m = (m/M_Planck)²` and `c_m ∝ m²` (§5); the weight-0 classification `weight(c_m) = +2 + 2(−1) − 0 = 0` and gauge invariance `c_m(μl)/c_m(l) = 1` (§5); the exact factorization `c_m = γ_G·ν_m² = Gm²` with `σ_A` cancelling and `γ_G = G·σ_A = 1/4` (§5); the `c_m`-independence of the gravity invariants `κ·σ_A`, `G·σ_A` (NOT-SELECTED) (§5); the physical `ν_m(e) ≈ 8.4 × 10⁻²³` far below the toy gaps (§5); and the algebraic refutation of the `θ_B²`/Srednicki numerology (§5).

Both receipts report ALL CHECKS PASS at the cited precision.

---

## References

**Companion (this program).**

[XI] *Emergent Einstein equations without an emergent Newton constant: a no-go for sealed-record gravity* (`v6/publishable/paper-XI-sealed-record-gravity-no-go`) — the parent: the scale no-go, the weight-counting lemma, SIGMA-SPLIT, gate G1, and the `c_m` eligibility this note generalizes.
[III] *The record click-law, III: the seal spacing is mode-dependent and bound-only, and its cross-tier scale-bridge is a no-go* (`v7/relativistic-isp-v7-paper3-seal-spacing-no-go`) — the spacing `d` no-go; the grading-homomorphism trichotomy; receipt `p3_d_nogo.py`.
[V] *The record click-law, V: the gravitational coupling per species is a free calibration* (`v7/relativistic-isp-v7-paper5-cm-free-calibration`) — the `c_m` weight-0/permitted/blind verdict and the factorization `c_m = γ_G·ν_m²`; receipt `p5_cm_calibration.py`.
[6] *`A_rec` gauge closure* (v6 paper6) — Theorem G (the weight grading as a homomorphism), the invariant ring, gate G1.
[57] *Gravity from sealed records* (v6 paper57) — the `G` no-go (`κ·σ_A = 2π`, `G·Λ²`); the seal-rate primitive.

**External.**

[1] E. Buckingham, *On physically similar systems; illustrations of the use of dimensional equations*, Phys. Rev. **4**, 345 (1914) — the Π-theorem (dimensionless = weight-0; one external unit sets the scale).
[2] S. Coleman, E. Weinberg, *Radiative corrections as the origin of spontaneous symmetry breaking*, Phys. Rev. D **7**, 1888 (1973) — dimensional transmutation (a marginal coupling yields a scale ratio, not an absolute scale).
[3] M. Srednicki, *Entropy and area*, Phys. Rev. Lett. **71**, 666 (1993) — the geometry-universal area coefficient `a = 0.295417`.
[4] A. Chamseddine, A. Connes, *The spectral action principle*, Commun. Math. Phys. **186**, 731 (1997) — the candidate bridge generator landing on `G·Λ²`.
