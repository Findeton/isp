# The record click-law, III: the seal spacing is mode-dependent and bound-only, and its cross-tier scale-bridge is a no-go

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-15. Third paper of the v7 program; it closes the spacing question left open by Paper II. Tags: **[FORCED]** = uniquely required (symbolic / high-precision numeric); **[MODE]** = deterministic given a mode but mode/ledger-dependent; **[RANDOM]** = an irreducible distribution; **[NO-GO]** = a proved impossibility within a stated scope; **[OPEN]** = a disclosed, unproved residue. All numeric claims at mpmath `dps ≥ 100` (here 140) and sympy-exact where the structure permits; receipts `v7/code/p2b_event_law_saturation.py`, `p2c_vector_ledger_roots.py`, `p3_d_nogo.py`.

## Abstract

Paper II forced a ceiling on the seal spacing (`d ≤ W_* = 0.36478…`) but left the spacing's *value* open, and named the cross-tier bridge — fixing the weight-zero `d` from a derived gravitational dimensionless coefficient — as the candidate route. This paper settles both halves with a sharp negative answer, and a precise account of what `d` actually is. **`d` is not a fixed quantity.** Three objects that the law keeps on three distinct footings must never be conflated: the **content** committed at a seal is deterministic *given a mode* but is irreducibly **mode/ledger-dependent** — a finite indexed set `{C(η_B) = 0.15611…, C(h_*) = 0.10900…, …}` with no canonical member, every element strictly below the forced **capacity** `W_*` (itself a fixed scalar, but a *bound*, not the spacing — the firing law commits strictly inside it and denies `d = W_*`); and the **evidence clock** that triggers each seal is an irreducibly **random** `Exp(1)` variable (`E[I] = 1`, `Var[I] = 1`), in *evidence* units whose mean-1 firing cannot be read as a content spacing without the conversion `κ` the scale no-go forbids the records to supply. So the only corpus-robust quantitative statement is the **inequality** `d < W_*` in every admissible mode. **The cross-tier scale-bridge is blocked.** Because `d` is weight-zero throughout, the scale no-go *permits* a derived dimensionless gravitational coefficient to pin it without supplying `κ` — but the same weight-counting grading (paper6 Theorem G) that grants `d` its weight-zero eligibility forces every record-derived dimensionless coefficient into an exhaustive trichotomy — *ratio-of-twins* (circular: the scale cancels), *scale-blind* (vacuous: carries zero information about `d`), or *Tier-A-intrinsic* (wrong tier and wrong axis: `W_*` is an amplitude, not a spacing) — none of which fixes the absolute scale. The strongest numerical candidate, `θ_B² = 0.29560…` against the Srednicki area coefficient `a = 0.29542…`, is refuted *algebraically*: `θ_B` is a degree-3 algebraic irrational (`e^{η_B}` is the tribonacci constant), numerically distinct from the Srednicki coefficient, with the corpus partial-wave sequence converging away from it. The most natural bridge generator, the Chamseddine–Connes spectral action, lands on the weight-zero invariant `G·Λ²` and fixes only the *ratio* `G/l_step²`, never the absolute scale — independently of its coefficient value; its conjectured "factor-`2π` gap" is *plausibly* a moment-labelling ambiguity (the zeroth and first collar moments differ by exactly `2π`: `1/(2π)` vs `1/(2π)²`), a candidate correction to the corpus's `[CONJECTURED]` value but not a settled one, and immaterial to the no-go. The no-go is **airtight modulo a single named, isolated premise** — gate G1, that no sealed law consumes the record area outside the continuum labeling map — which is proved-finite for the executed corpus but whose universal quantifier remains a scope assumption (the seal-rate primitive *refutes the sharpest counterexample* to it but does not discharge it). Two doors stay honestly open and weight-zero-eligible — the dimensionless *strength* coupling `c_m = Gm²/ℏc` (a hierarchy, not the spacing) and an undiscovered external structural identity. Pre-geometric throughout on the Tier-A side: no spacetime, metric, or interval `s²`; the gravitational coefficients enter only in the cross-tier sections, where the result is precisely that they cannot fix the spacing.

---

## 1. Introduction: the question, and the three-object discipline

Paper I forced the shape of the pre-geometric click-law and Paper II forced the content increment (a coboundary) and the spacing ceiling (`d ≤ W_*`), then isolated the genuine open obligation: *what fixes the spacing `d`?* The roadmap's candidate was a **cross-tier bridge** — since `d` is a weight-zero (dimensionless) number, the scale no-go of the gravity program permits a *derived* dimensionless gravitational coefficient to equal a per-seal content and so pin `d`, without ever manufacturing the forbidden absolute scale.

This paper answers two questions and finds both answers negative in a precise, instructive way:

1. **Is `d` even a fixed quantity?** No. It is mode-dependent on the content axis, bound-only from above, and distribution-valued on its firing axis.
2. **Can a derived gravitational coefficient fix it?** No, not the absolute scale: the record-derived bridge is provably circular, scale-blind, or wrong-tier; the bridge that could carry genuine length is structurally forbidden.

Everything turns on **not conflating three objects** the law keeps separate:

- **the content `C(h)`** — the Kullback–Leibler evidence (in nats) committed at a seal, given the firing law's selected tilt coefficient `h`;
- **the capacity `W_*`** — the one-diamond `KL = Fisher` ceiling, a *fixed* scalar but an upper *bound*;
- **the evidence clock `I`** — the accumulated RN/KL action at which the division event fires, a *random* variable in evidence units.

The four naive readings of "what is `d`" — (a) a fixed scalar, (b) a fixed mean with random fluctuations, (c) a mode-dependent set, (d) an irreducible distribution — sort cleanly onto these objects: (a) describes only `W_*` and the at-fixed-mode tilt; (b) describes the *evidence clock* (not the content); (c) is the most accurate single description of the *content*; (d) is true of the *clock*. The honest verdict is the layered **(c)+(b)/(d)** below. All Tier-A quantities here are weight-zero record-internal numbers; the gravitational coefficients appear only in §5–6.

---

## 2. What `d` is not: the single-fixed-scalar reading fails

The capacity `W_* = 0.364784952089976…` is a genuine fixed scalar — the unique `C(η) = J(η)` balance (`η_A = 1.090344354879492…`), `W_* = 1 − θ_*²` (Paper II §3.1). But it is the **ceiling**, not the spacing. The firing law of paper4 §71–76 commits **strictly inside** it: the one-mode content is `C(η_B) = 0.428 W_*`, the coupled content `0.299 W_*`, and reaching `W_*` would require an inadmissible cochain unit `λ ≈ 0.208 < 1` (Paper II §3.3). So `d = W_*` is the one reading the firing law denies. Independently, paper4 §69 found a *fixed-content* commitment threshold non-canonical — the selected tilt drifts with the renewal unit — so no fixed content value is canonical *a priori*. The only corpus-robust quantitative statement about the spacing is therefore an **inequality**:

  **`d < W_*` in every admissible mode** (the gated class of orthogonal parity ledgers on the count-dual base, Paper II §3.3; the firing law commits *strictly* inside the `d ≤ W_*` ceiling). **[FORCED]**

This already rules out reading `d` as a single forced scalar: `W_*` is fixed but is not `d`, and the firing law supplies no other fixed number.

---

## 3. The content axis: deterministic per mode, mode-dependent across modes [MODE]

The seal-firing law is the vector fixed point `∂ψ/∂h = e^{−h}` on the complete primitive ledger — the Euler equation of the strictly-convex commitment potential `Φ(h) = ψ(h) + Σ_j e^{−h_j}` (paper4 §71–76; `p2c` verifies the coupled root is the unique strictly-convex minimizer, Hessian eigenvalues `> 0`). This fixed point selects the **tilt coefficient** `h`, and the random evidence draw `I` (§4) does **not** enter it. Hence the content committed at a seal is a *deterministic function value*, the same at every firing of a given mode:

  `E[content per seal | fixed mode] = C(h)`,  `Var[content per seal | fixed mode] = 0`.

But the selected root `h` is **mode/ledger-dependent**. The one-mode-parity slice `tanh η = e^{−η}` gives `η_B = 0.609377863436006…`, `C(η_B) = 0.156109200157…`; the coupled three-statistic `{x, y, xy}` ledger gives `h_* = 0.495053264332…` (all components equal), `C(h_*) = 0.109004107833…`. These differ (`|C(η_B) − C(h_*)| = 0.0471…`), so the per-seal content is a deterministic member of a **finite, mode-indexed set with no canonical member** — `η_B` is the one-mode-parity slice, not a corpus-unique value. Coupling more modes only dilutes the per-mode *coefficient* (`η_B = 0.609 → 0.495 → 0.368` over the 1/3/7-character groups), whose *contents* are the strictly smaller `C = 0.156 → 0.109 → 0.063` — so the content set is monotone-decreasing under coupling and the one-mode `C(η_B) = 0.156` is its supremum. A non-admissible skewed base would instead *over*-shoot (`μ(+) = 0.2` gives content `0.526 > W_*`), excluded by the count-dual/orthogonality gates that also fix the §2 constants (Paper II §3.3). Within the admissible class the one-mode content `C(η_B) = 0.428 W_*` is the supremum; in no admissible mode does the content reach `W_*`.

So the content axis realizes option **(c)**: a mode-dependent set, every element strictly below `W_*`, none canonical.

---

## 4. The evidence axis: the firing clock is the genuine randomness [RANDOM]

The division event fires at an accumulated-evidence threshold. paper4 §71 derives the survival law from eventless RN/KL gluing `S(I + J) = S(I) S(J)` together with exact self-accounting `−log S(I) = I` (which fixes the rate `λ = 1` and the commitment ratio `r = 1`):

  `S(I) = e^{−I}`,  so the inter-seal evidence `I ~ Exp(1)`,  `E[I] = 1`,  `Var[I] = 1`

(both moments computed exactly by quadrature at `dps = 140`, `p3`). The seal fires at a **random** evidence threshold — this is the law's genuine randomness, option **(d)**, and it lives in **evidence units**, not content units. Turning the mean-1 firing into a *content* spacing would require the conversion rate `κ` (content per unit commit-order) — exactly the one weight-bearing quantity the scale no-go forbids the records to supply (Paper XI; §5 below). So neither the deterministic content (§3) nor the random clock (§4) manufactures an absolute scale, and neither pins a single `d`. The randomness belongs to the clock; the content at the selected tilt is deterministic; the two never mix without `κ`.

**The layered verdict.** `d` is the per-seal content: deterministic given a mode (§3, `Var = 0`), mode-dependent across modes (§3, a finite set with no canonical member), bounded strictly above by `W_*` (§2), and committed by a seal that fires on a random `Exp(1)` clock (§4). It is **not** a fixed deterministic scalar. The corpus-robust content is the inequality `d < W_*`.

---

## 5. Cross-tier bridge, I — the absolute scale is blocked [NO-GO]

Because `d` is weight-zero on both axes, the scale no-go *permits* a derived dimensionless gravitational coefficient to equal a per-seal content and pin `d` without producing the forbidden absolute length. We prove the record-derived version of this bridge cannot exist.

**The weight grading is a homomorphism, and dimensionless is exhaustively a trichotomy. [FORCED]** The record-length gauge `g_λ : l → λl` acts as a one-parameter group, so the weight assignment is an *additive grading homomorphism* `weight(XY) = weight(X) + weight(Y)` (paper6 Theorem G, cofinal-equivariance theorem). A generic record monomial `W_*^a κ^b l_step^c σ_A^e` carries weight `2b + c − 2e`, and "dimensionless" is exactly `weight = 0`, which **forces** `c = 2(e − b)`: the absolute-length power `c` is even and is carried entirely by `κ`/`σ_A` powers that *cancel* it (`p3`, sympy-exact). There is no monomial — and, since any transcendental functional of weight-zero ratios is itself weight-zero, no functional — that is dimensionless yet retains an absolute length. Even irrational/anomalous weights cannot leak length (`a + b√2 = 0` over `ℤ` only for `a = b = 0`). The exhaustive case split is the trichotomy:

- **ratio-of-twins (circular):** `1/4 = G·σ_A`, `2π = κ·σ_A`, `G·Λ²`, `η = 1/4G` — dimensionless *only because* the record scale appears and cancels; consistent with **every** record scale (SIGMA-SPLIT), so consistent with every `d`. (Here `κ = 8πG`, the SIGMA-SPLIT gravitational coupling of weight `+2` — distinct from the Tier-A conversion-rate `κ` of §4, the no-go floor, and from paper4's source amplitude `κ = W_*` in bin 3 below.) `p3` confirms `G·σ_A = 1/4` and `κ·σ_A = 2π` are invariant under `l → μl` for `μ = 1, 1.7, 3` — the absolute scale is a free modulus.
- **scale-blind (vacuous):** Srednicki `a = 0.295417`, `U_G = 1`, `η/s = 1/4π`, `c/6 = 1/6`, the graviton fraction `4/9` — the scale cancels, so they carry zero information selecting `d`.
- **Tier-A-intrinsic (wrong tier and axis):** `W_* = 0.364785` is a genuine per-seal content, but a *Tier-A* record constant (the same tier as `d`), and on the *amplitude* axis (it is the source coefficient `κ = W_*` of paper4), not the spacing/length axis. Equating `d` to it is intra-tier bookkeeping, not a cross-tier constraint.

The three requirements — record-derived ∧ scale-independent ∧ carries per-seal/length content — are mutually exclusive; there is no fourth bin.

**The numerology is refuted algebraically. [FORCED]** The strongest numerical near-miss is `θ_B² = 0.295597742522…` against the Srednicki area coefficient `a = 0.295417…` (gap `1.8 × 10⁻⁴`). This is not a near-identity awaiting more digits: `θ_B = tanh η_B = e^{−η_B}` satisfies `t³ + t² + t − 1 = 0` (equivalently `e^{η_B}` is the **tribonacci constant**, root of `x³ − x² − x − 1`), and `θ_B²` satisfies `s³ + s² + 3s − 1 = 0` — both irreducible degree-3 polynomials over `ℚ` (`p3`, sympy). So `θ_B²` is a *specific* cubic algebraic irrational, numerically distinct from the Srednicki coefficient (the gap `1.8 × 10⁻⁴` exceeds the precision to which `a` is known), and the corpus partial-wave sequence converges *toward* `a = 0.295417` and *away* from `θ_B² = 0.295598` — the near-match is numerology, not an identity. The other threads fail likewise (`1/η_B = 1.641018` vs `π²/6 = 1.644934`, gap `3.9 × 10⁻³`; `1/4` has no clean factor to any `d`-candidate). The mass-gap thread `1/η_B = 1.641018` is real as an identity (`= −1/log tanh η_B`) but is itself a weight-zero record-internal number — the corpus already lists this `ξ_1d` length as a *second-scale attack* that collapses onto the weight-zero invariant — so it opens no crack.

**The spectral-action route lands on the named invariant. [NO-GO]** The most natural bridge generator — a Chamseddine–Connes / Sakharov-induced spectral action making `G·Λ²` record-intrinsic — does not fix the absolute scale: `Λ = 1/l_step` *is* the record-scale label, so the route delivers only the ratio `G/l_step²`, never absolute `G`. (Its conjectured obstruction — that the eventless-collar profile gives `1/(2π)²` while the action "wants" `1/(2π)` — is *plausibly* a moment-labelling ambiguity: the zeroth and first `u`-moments of the boost profile `e^{−2πu}` differ by exactly `2π` (`M0 = ∫e^{−2πu}du = 1/(2π)`, `M1 = ∫u e^{−2πu}du = 1/(2π)²`, `p3`), and under one reading of the Chamseddine–Connes moment indexing the Einstein–Hilbert `Λ²` coefficient is carried by the *zeroth* (rather than first) `u`-moment — which, if it applies here, would *correct* the corpus's first-moment computation, where the value is honestly tagged `[CONJECTURED]`. That identification is itself unverified and convention-dependent — a candidate correction, not a settled one.) The point load-bearing for the no-go is independent of both the coefficient's value and this labelling: the route lands on `G·Λ²`, and the coefficient is in every scheme (the corpus's `3π²`, Sakharov `192π²/N`, …) merely a pure number, so it fixes only the *ratio* `G/l_step²`, never absolute `G`. The absolute-scale door is **closed within the weight grading** (modulo G1, §7).

---

## 6. Cross-tier bridge, II — the permitted weight-zero strength lane [OPEN]

The no-go is about the **absolute scale**. A categorically different object is *permitted* and remains genuinely open: a weight-zero *strength*. The dimensionless gravitational coupling-per-species `c_m = Gm²/ℏc` is weight-zero, hence intrinsic-eligible — it is *not* forbidden by the no-go, and the records may in principle output it. But `c_m` fixes a dimensionless **hierarchy/strength**, categorically distinct from the **spacing** `d` (the area density `σ_A` is weight `−2`): `c_m·σ_A` inherits the free scale but never produces it, so fixing `c_m` never fixes `σ_A` or the absolute `d`. The spectral action is *one* unverified candidate generator for such a dimensionless coefficient, contingent on an unproven identification (the eventless-collar Gibbs profile at `β = 2π` with the spectral-action test function) and a record-fixed normalization — a candidate, not a prediction. This lane is the honest constructive residue, pursued elsewhere; it is not a route to fixing `d`.

---

## 7. Gate G1, and the completeness sweep

**G1 is the single load-bearing premise. [OPEN — scope assumption]** The whole no-go rests on one gate: that no sealed law consumes the record area `A_rec` outside the continuum labeling map `ℓ` (paper6; the same premise as Paper 57's `G` no-go). G1 is *proved-finite for the executed corpus* (clause table plus audit-by-execution, worst gap `0`), but only *interface-level* for the un-imported earlier texts, and it is **not** a closure theorem against future-added laws — its universal quantifier remains a scope assumption, parallel to the temperature axiom. The seal-rate primitive **refutes the sharpest candidate counterexample** (an intrinsic rate carrying an absolute scale, killed by the weight trichotomy `{0, −1, −2}`) but does **not** discharge the quantifier; it must not be described as "closing G1."

**Every other candidate crack is closed. [FORCED]** A hostile completeness sweep dispatched, sympy-exact, every other route by which an absolute length might survive: an additive grading anomaly collapses into G1; reaching a negative weight needs a negative-weight primitive, all of which are chart/label images of `ℓ`; fractional/irrational label-roots stay labels (`weight(A_rec^{−3/7}) = −6/7`, still a label); the `ℏ = c = 1` convention hides no second length (it fixes two of three unit freedoms; the residual length *is* `l_step`, the gauge direction); log-running/dimensional transmutation gives a weight-`−1` transmuted scale (`= l_step` again) and merely reproduces SIGMA-SPLIT; non-monomial transcendental functionals of weight-zero ratios stay weight-zero; and every record mass gap is a pure number times `l_step` (weight `+1`), including `1/η_B = 1.641018`. There is no fourth independent door and no second intrinsic length.

---

## 8. The open-doors ledger, and the sharpened obligation

The honest scope of the no-go, door by door:

| door | status |
|---|---|
| absolute-scale bridge (record-derived coefficient → absolute `d`) | **closed** [NO-GO] — forced trichotomy + algebraic numerology refutation |
| spectral-action absolute-scale route | **closed** — lands on `G·Λ²`, fixes the *ratio* not the scale, regardless of the coefficient value (the apparent `2π` gap is *plausibly* a moment-labelling ambiguity, `[CONJECTURED]`/unverified, and immaterial to the no-go) |
| gate G1 (no sealed law consumes `A_rec` outside `ℓ`) | **open scope assumption** — the sole load-bearing premise; seal-rate refutes the sharpest counterexample but does not discharge the quantifier |
| dimensionless strength `c_m = Gm²/ℏc` | **open, permitted** [OPEN] — weight-zero, intrinsic-eligible; a *strength/hierarchy*, categorically not the spacing |
| external structural identity (`d` = an independently-derived weight-zero coefficient) | **permitted, undiscovered** — `d` being weight-zero, two dimensionless numbers may coincide without invoking the scale; not exhibited, not excluded |

The driver Paper II opened — *what fixes the spacing `d`* — is therefore **well-posed and open**, orthogonal to and consistent with the scale no-go, with three live non-circular routes: (i) a completeness/canonicalization principle selecting one mode or pushing the commitment to `W_*`; (ii) the external structural identity of the last row, with the weight-zero `1/η_B = 1.641018` mass-gap thread as a (suggestive, not derived) entry point; (iii) a non-circular variational principle on the inter-seal stretch. What this paper settles is sharper and final: **`d` is not a fixed quantity to begin with, and no record-derived gravitational coefficient can manufacture an absolute one.**

---

## 9. What this paper does and does not claim

It **claims**, with high-precision receipts: that `d` is *not* a fixed scalar — mode-dependent on the content axis (a finite set `{0.156, 0.109, …}`, no canonical member, all `< W_*`), bound-only by `W_*` from above, and committed on a random `Exp(1)` evidence clock (`E[I] = Var[I] = 1`) — so the only robust quantitative statement is `d < W_*` (§2–4); that the record-derived cross-tier *absolute-scale* bridge is a **no-go**, forced by the grading-homomorphism trichotomy, with the strongest numerical thread refuted *algebraically* (`θ_B` is the tribonacci-related cubic irrational, numerically distinct from the Srednicki `a` with the corpus partial-wave sequence converging away from it) and the spectral-action route landing on `G·Λ²` and fixing only a ratio (the "factor-`2π` gap" *plausibly* a moment-labelling ambiguity, unverified and immaterial to the no-go) (§5); and that the whole no-go rests on the single isolated premise G1, every other crack closed sympy-exact (§7).

It does **not** claim: that `d` has a fixed value; that the no-go is unconditional (it is airtight *modulo G1*, an honestly disclosed scope assumption); that the weight-zero *strength* lane `c_m` is closed (it is permitted and open — a different question); or that an external structural identity is excluded (it is permitted-undiscovered). No geometric content is used on the Tier-A side; the gravitational coefficients enter only in §5–6, where the result is exactly that they cannot fix the Tier-A spacing. The honest one-line summary: **the seal spacing is mode-dependent and bound-only — not a fixed quantity — and the only cross-tier route that could have made it one cannot manufacture an absolute scale; what `d` is and what (if anything) selects it among admissible modes remains the genuine, well-posed open obligation.**

---

## 10. Precision discipline

Every numeric quantity was computed in mpmath at `dps ≥ 100` (here 140) and sympy-exact where structural. The evidence-clock moments (`E[I] = 1`, `Var[I] = 1`), the mode-dependent contents (`η_B = 0.609377863436…`, `C(η_B) = 0.156109200157…`; `h_* = 0.495053264332…`, `C(h_*) = 0.109004107833…`; all `< W_* = 0.364784952090…`), the grading homomorphism and its dimensionless case-split (`c = 2(e−b)`, no surviving length; irrational-weight leak closed), the tribonacci algebraicity (`θ_B` root of `t³+t²+t−1`, `θ_B²` of `s³+s²+3s−1`, both irreducible over `ℚ`; gap to Srednicki `1.8×10⁻⁴`), the spectral moments (`M0 = 1/(2π)`, `M1 = 1/(2π)²`, `M0/M1 = 2π`), and the SIGMA-SPLIT invariance (`G·σ_A = 1/4`, `κ·σ_A = 2π` under `l → μl`) are all in `v7/code/p3_d_nogo.py` (9 machine checks, all pass), with the underlying seal roots in `p2b` (13 checks) and `p2c` (25 checks). Never float64 for the cancellation-heavy balances.

---

## References

**Companion (this program).**

[I] *The record click-law, I: a self-consistent pre-geometric sealing law and its emergent thermodynamic limit* (`v7/relativistic-isp-v7-paper1-record-click-law`).
[II] *The record click-law, II: the content supply* (`v7/relativistic-isp-v7-paper2-content-supply`) — the forced ceiling `d ≤ W_*`, the mode-dependent firing content, the open spacing this paper closes.
[4] *SHARD: Sealed Holonomy and Record Dynamics* (v6 paper4) — the one-diamond `KL = Fisher` constants (§5), the division-event/seal-firing commitment law and its vector fixed point `∂ψ/∂h = e^{−h}` (§71–76), the non-canonicity of a fixed-content threshold (§69).
[6] *`A_rec` gauge closure* (v6 paper6) — the weight-counting lemma / Theorem G: the record-length gauge as a grading homomorphism, the invariant ring, gate G1.
[57] *Gravity from sealed records* (v6 paper57) — the `G` no-go (`κ·σ_A = 2π` and, separately, `G·Λ² = const` — distinct weight-zero invariants, not numerically equal); the seal-rate primitive; the graviton/covariance residues.
[XI] *Emergent Einstein equations without an emergent Newton constant* (`v6/publishable/paper-XI-sealed-record-gravity-no-go`) — the scale no-go; weight-zero eligibility (`c_m`); the spectral-action / `G·Λ²` discussion.

**External.**

[A] M. Srednicki, *Entropy and area*, Phys. Rev. Lett. **71**, 666 (1993) — the geometry-universal entanglement area coefficient.
[B] A. Chamseddine, A. Connes, *The spectral action principle*, Commun. Math. Phys. **186**, 731 (1997).
