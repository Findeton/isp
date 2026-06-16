# The record click-law, II: the content supply — a forced coboundary clock and a forced capacity ceiling on the seal spacing

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-15. Second paper of the v7 program; it continues the pre-geometric record click-law of Paper I. Tags: **[FORCED]** = uniquely required (symbolic / high-precision numeric); **[PHYSICAL]** = a record-intrinsic but configuration-dependent input (a form is forced, a magnitude is not); **[CHOICE]** = a well-motivated but unforced selection; **[OPEN]** = an unsolved obligation. All numeric claims at mpmath `dps ≥ 100` (here 140) and sympy-exact where the structure permits; receipt `v7/code/p2a_content_supply.py`.

## Abstract

Paper I forced the *shape* of the pre-geometric record click-law in the intrinsic content `χ = D(P_AB‖P_BA)` — the seal is an orthogonal projection, the content is a sequentially-additive odometer, the divisible survival law is `exp(−κχ)`, the indivisible law a power-law lattice skeleton `S(nd)=S(d)ⁿ` with a free inter-seal profile — but it left the content's own *supply* open: the **magnitude** of the increment `dχ` (hence the scale `κ`) and the **spacing `d`**. This paper asks whether the record's own closed-holonomy ledger generates its clock, and reports a sharp two-part answer. **(1) The clock's form is forced.** The content increment is the **coboundary** of the holonomy potential, `dχᵢ = ρᵢ = h_{i+1} − h_i`, with the telescope `Σρᵢ = h_b − h_a` — a theorem three ways over (it *is* Paper I's odometer additivity; the discrete Poincaré lemma makes "concatenation-additive content ⟺ coboundary of a scalar potential" an identity; it matches the source-as-coboundary law of the sealed-record corpus). Only *which* potential `{hᵢ}` is realized — the **magnitude** — is left, and that is configuration-dependent physical data, not a law. The absolute scale `κ` (content → commit-order rate) stays the single no-go floor: it carries one absolute unit the weight-zero records provably cannot supply. **(2) The spacing gets a forced ceiling, and the corpus's seal-firing law commits *strictly under* it.** A capacity/saturation structure absent from Paper I forces a real bound: the per-diamond content cannot exceed the one-diamond Kullback–Leibler-equals-Fisher capacity `W_* = 1 − θ_*² = 0.36478…` — accumulated content `C(η)` rises while Fisher capacity `J(η)` falls, crossing once at the **self-consistency root `η_A = 1.0903`** (which fixes `W_*`), so `W_* = max_η min(C(η), J(η))`, and an over-saturated commitment is self-inconsistent. **Hence `d ≤ W_*` is forced** given that a committed record is self-consistent (`C ≤ J`) — a constraint Paper I's composition-self-consistency *could not* supply (it left `d ∈ (0,∞)`). But the *equality* `d = W_*` is **not** forced, and the reason is structural rather than a mere absence of proof. Paper4's self-consistency law (§5, the capacity *constant* `η_A`) and its **division-event seal-firing law** (§71–76) are *distinct and mutually consistent* — the former fixes the diamond's constants; the latter is a *vector* fixed point `∂ψ/∂h = e^{−h}` on the complete primitive ledger that fires the seals — so there is **no contradiction within the corpus**. What `d = W_*` is equivalent to is the *postulate* `(P-sat)` "the seal fires *at* capacity"; and *that* the firing law contradicts, because it commits **strictly below** `W_*` — structurally, throughout the admissible class of orthogonal parity ledgers on the count-dual base (`C = 0.156` on the one-mode-parity slice, `0.109` on the coupled `{x,y,xy}` ledger; the one-mode value `0.428 W_*` is the supremum there, since reaching `W_*` needs an inadmissible cochain unit and coupling only dilutes) — the firing itself running on a *random* evidence clock `I ~ Exp(1)` (mean 1 in RN units), not at the fixed `W_*`. The firing root is moreover **mode-dependent** (`η_B = 0.6094` is the one-mode slice, not a unique canonical value), so the robust corpus fact is the **inequality** — committed content `< W_*` in every mode — not a magic number. The honest ledger: `composition → d ∈ (0,∞); + no-over-saturation → d ∈ (0, W_*]` **[forced]**; the seal-firing law commits *strictly inside* that interval (sub-capacity, mode-dependent, on a Poisson clock), with `d = W_*` an *overriding choice* the firing law denies. The genuine open obligation is therefore **what fixes the spacing `d`** — not the (already consistent) §5-vs-§71 reconciliation; the cross-tier bridge remains a candidate, since `d` is weight-zero and the scale no-go *permits* a derived Tier-B gravitational dimensionless coefficient to pin it (the one-mode root's reciprocal `1/η_B = 1.641` is the corpus's 1d mass-gap correlation length). Pre-geometric throughout: no spacetime, metric, light cone, or interval `s²`.

---

## 1. The question: where does the content come from?

Paper I established the pre-geometric click-law's shape but isolated two pieces of its content-supply as open: the *magnitude* of each content increment `dχ` (and so the one absolute scale `κ`), and the *spacing* `d` between seals in the indivisible regime — with the leading candidate `d = W_*` (one seal per one-diamond's worth of content) flagged plausible but unforced, because composition-self-consistency only ever checks the law *at* the seal points and is silent on the spacing.

This paper asks the upstream question: **does the record's own closed-holonomy ledger generate its clock?** We keep the discipline of Paper I — **pre-geometric** throughout (records, the commit order, the weight-zero content `χ`; no spacetime, metric, or `s²`) — and report what the ledger forces (§2, §3), what it leaves as physical input (§4), and what remains a named choice and open frontier (§3.3, §5).

---

## 2. The clock's form is a forced coboundary

**The content increment is the coboundary of the holonomy potential. [FORCED]** The sealed-record corpus carries a closed-holonomy potential `{hᵢ}` along the commit order (the cochain whose differences are the per-step holonomy increments). The intrinsic content `χ`, identified in Paper I with the accumulated entropy production `σ = D(P_AB‖P_BA)`, is forced to accumulate as the **coboundary**

  **`dχᵢ = ρᵢ = h_{i+1} − h_i`**,  with the exact telescope  **`Σ_{i=a}^{b-1} ρᵢ = h_b − h_a`**.

This is a theorem. Its core is a single fact seen two ways, which the corpus then instantiates:
- **The discrete Poincaré lemma — equivalently Paper I's odometer.** Along a one-dimensional commit order the first cohomology of a path vanishes (`H¹ = 0`), so "concatenation-additive content" and "coboundary of a scalar potential `{hᵢ}`" are the *same* statement — and that statement is exactly Paper I §3.2's sequential, `dχ ≥ 0` odometer, whose telescoping sum of per-step increments *is* the coboundary `h_{i+1} − h_i`. There is no freedom in the form.
- **The corpus instantiates it.** The sealed-record source/conservation law is itself a cellular coboundary of the complete interface holonomy, so the content increment inherits exactly this coboundary structure — leaving only *which* coboundary is realized (the magnitude layer, §4).

Two layers should be kept apart. The discrete Poincaré lemma forces the content to be the coboundary of *some* scalar potential `{hᵢ}` — that is the theorem, and it is pure form. *Identifying* that potential with the corpus's closed-holonomy cochain (so the increments `ρᵢ` are the per-step exchange-defect holonomies) is the physical-input layer of §4: it is what gives the forced form its *magnitudes*. The form is forced; the identification is the place the actual process enters.

Verified sympy-exact over all sub-blocks of a worked commit chain, with the corpus potential/increment numbers reproduced to `< 10⁻¹⁰⁰` (receipt `p2a_content_supply.py`). So the *form* of the clock — how content accrues — is fixed by the ledger, not assumed.

**Only the magnitude is left, and the scale `κ` is the no-go floor.** What the coboundary form does *not* fix is *which* potential `{hᵢ}` is realized — the absolute sizes of the increments `ρᵢ` (§4). And turning the accumulated content (a weight-zero number) into a commit-order *rate* requires the single conversion `κ`, which carries one absolute unit the records provably cannot supply (the scale no-go). The content is record-eligible; the rate's absolute scale is not. So Paper I's `κ` remains exactly one free no-go floor, untouched by anything here.

---

## 3. The spacing: a forced ceiling, and a seal-firing law that commits under it

The substantive new result concerns the indivisible spacing `d` — the content committed per seal.

### 3.1 `W_*` is a genuine capacity. [FORCED]

The one-diamond self-consistency law `KL content = Fisher capacity`, `D(P_η‖μ_D) = J(η)`, fixes the internal constants (Paper I §2): `η_* = 1.090344354879492…`, `θ_* = tanh η_* = 0.797003794162878…`, `W_* = J(η_*) = 1 − θ_*² = 0.364784952089976…` (balance residual `1.3×10⁻¹⁴¹` at `dps = 140`). The key structural fact, not visible at the single self-consistency point, is monotone opposition:

  the **accumulated content** `C(η)` rises monotonically (`0 → log 2 = 0.6931…`), while the **Fisher capacity** `J(η) = sech²η` falls monotonically (`1 → 0`);

they cross exactly once, at `η_*`. Therefore

  **`W_* = max_η min( C(η), J(η) )`**  (attained analytically at the crossing) —

`W_*` is the *largest content a single diamond can simultaneously accrue and hold within its capacity*. This is a genuine saturation-bound structure, not an arbitrary equality. (The reduction to a *scalar* `min(C, J)` — content and capacity as single comparable numbers — inherits Paper I §3.1's single-channel screen: the `q = 2` one-contrast object collapses the matrix capacity to one scalar. With several independent contrast channels the capacity would be a vector and the bound a Pareto frontier; the single-channel record makes it the scalar above.)

### 3.2 The capacity ceiling `d ≤ W_*` is forced (given no over-saturation). [FORCED]

The bound rests on one named premise — the symmetric partner of the extremal postulate (P-sat) below:

  **(no-over-sat)** *a committed record is self-consistent: it carries no more coherent content than its own capacity,* `C(η) ≤ J(η)`.

This is not a free assumption: a record *is* a self-consistent diamond, and `C > J` is precisely the over-saturated regime the one-diamond law excludes. Granting it, since `C(η) > J(η)` is self-inconsistent, **no seal can carry more than `W_*` of content**:

  **`d ≤ W_*`.**

This is a real constraint on the spacing — and one that Paper I's principle could not supply. Composition-self-consistency (the Cauchy/refinement condition) gives *no* bound on `d` (we re-confirm: any `d > 0` is admissible to it, because composition only ever evaluates the law at sums of seal points). The capacity bound is a *different*, non-composition constraint, and it tightens Paper I's open `d ∈ (0,∞)` to `d ∈ (0, W_*]`. Note the asymmetry with §3.3: this ceiling needs only *self-consistency of what commits* (a record is a non-over-saturated diamond), whereas the *equality* `d = W_*` would need the stronger claim that commitment waits for full saturation — which paper4 §71 denies.

### 3.3 The equality `d = W_*` is not forced — the corpus's seal-firing law commits *under* the capacity. [CHOICE, in tension with the postulate (P-sat), not with the corpus]

The capacity bound forbids *over*-commitment; it never forbids *under*-commitment. So `d ≤ W_*` plus an *extremal selection* would be needed to reach the equality, via the postulate **(P-sat)** *a diamond commits at capacity — the seal fires as late as the capacity admits.* The decisive fact is that the corpus already carries a seal-firing law, and it does **not** seal at capacity.

**The seal-firing law and the capacity law are distinct, and consistent.** Two information-geometric conditions live on the *same* one-mode tilt axis `η` of the same parity family `P_η(q) = e^{ηq}/(2 cosh η)` (same log-partition `ψ`, same RN/KL units), but they are roots of *different* equations answering *different* questions:
- the **capacity / self-consistency** condition (paper4 §5) is the `ψ″`-balance `C(η) = J(η)` (KL content = Fisher capacity), root `η_A = 1.0903…`, fixing the diamond's *constants* and the capacity `W_* = 0.36478…`. It is a structural equilibrium constant — paper4 §7 is explicit that a single diamond "has no memory … no previous or next diamond," i.e. it carries *no firing dynamics at all*;
- the **division-event / seal-firing** law (paper4 §71–76) is the `ψ′`-balance `∂ψ/∂h = e^{−h}` (retained closed-holonomy memory = no-division survival), whose firing actually runs on a *separate* evidence clock `S(I) = e^{−I}` (`I` the accumulated RN/KL evidence — a Poisson process, inter-seal evidence `~ Exp(1)`, mean 1).

A structural capacity constant and a sub-capacity firing threshold are different scalars on one axis, exactly as paper4 §0 lists them as separate claims. **So §5 and §71 are mutually consistent — there is no contradiction within the corpus.**

**What the firing law delivers is an inequality, not a magic number.** The firing fixed point `∂ψ/∂h = e^{−h}` is a *vector* law on the complete primitive ledger (paper4 §73–76), so its root is **mode/ledger-dependent**: the one-mode-parity slice gives `tanh η = e^{−η}`, root `η_B = 0.60938…`, content `C(η_B) = 0.15611…`; the coupled three-statistic `{x, y, xy}` ledger gives `h_* = 0.49505…` (all components equal; commitment potential strictly convex), content `C(h_*) = 0.10900…` (both verified, receipt `p2c`). So `η_B` is the *one-mode-parity seal value*, not a unique canonical commitment root. The **robust, mode-independent** fact is the inequality

  **the committed content lands strictly *below* `W_*`** (`C(η_B) = 0.156`, `C(h_*) = 0.109`, both `< W_* = 0.365`),

and this is *structural*, not merely "every mode we happened to check," **for the admissible class** — complete primitive *orthogonal* parity ledgers (paper4 §73–76) on the *count-dual* eventless base `μ = (½, ½)` (paper4 §5–6). Within that class: seal content `C(η)` is monotone increasing in the seal coefficient (`C′ = η sech²η > 0`); reaching content `W_*` would require the coefficient `η_A` (since `C(η_A) = W_*` exactly), which the seal law `tanh η = e^{−λη}` attains only at the cochain unit `λ ≈ 0.208 < 1` — *under*-counting the forced RN action, inadmissible by the same argument that rejects the `λ = 2` double-count; orthogonal modes each sit *at* `η_B`, and coupling only *dilutes* the per-mode coefficient (over the symmetric character group, `η_B = 0.609 → 0.495 → 0.368` for 1/3/7 characters). So the one-mode content `C(η_B) = 0.428 W_*` is the **supremum over the admissible class**, strictly below `W_*` (receipt `p2c`, TASK 6). The admissibility gates are load-bearing, not decorative: a *non*-count-dual base (skewing `μ(+) = 0.2`) yields content `0.526 > W_*`, and such skewed or non-orthogonal / mixed-basis ledgers are exactly what the count-dual structure (§5–6) and the cover-independence theorem (§75) exclude. The count-symmetry (`q² = 1`, `μ(q=±1) = ½`) that bounds the firing content under capacity is the *same* primitive structure that fixes the §5 constants — so the bound and the constants stand on one footing.

Three objects must be kept apart and not conflated: the **tilt** `η_B` (the selected coefficient), the **evidence** `I ~ Exp(1)` (the *random* Poisson firing clock, mean 1 in evidence units), and the **content** `C(η_B) = 0.156` (a *deterministic* function of the selected tilt, in content units). The randomness belongs to the evidence clock, not to `C(η_B)`.

**Hence `d = W_*` is not forced — and the *postulate* that would force it is what is contradicted.** `d = W_*` is equivalent to `(P-sat)`: "the seal waits for full saturation." But `(P-sat)` and the §71 firing law *both* speak to when the seal fires, and the firing law fires *under* capacity — so the firing law **contradicts `(P-sat)`** (not §5). Reaching `d = W_*` would require a completeness principle that *overrides* the corpus's own firing law. Independently, paper4 §69 found a *fixed-content* commitment threshold (commit when content reaches a fixed value — exactly what `d = W_*` is) to be **non-canonical**: the selected `η` drifts with the renewal shape. (paper4 §71 then *closes* that drift — it forces the Poisson shape and the unit `r = 1` by RN self-accounting; what it does *not* close, and what survives here as the genuine non-canonicity, is the **ledger/mode dependence** `η_B` vs `h_*` established above.) The honest ledger:

  `composition → d ∈ (0, ∞)`;  `+ no-over-saturation → d ∈ (0, W_*]`  **[forced ceiling]**;  the corpus's seal-firing law commits *strictly inside* that interval (sub-capacity, mode-dependent, on a Poisson clock), with `d = W_*` an **overriding choice** the firing law denies.

---

## 4. The accumulation magnitude is physical

The form is forced (§2); the *size* of each increment `ρᵢ = h_{i+1} − h_i` is the realized closed-holonomy potential `{hᵢ}`, which the corpus names explicitly as the *physical free data* of the sealed process — the actual relative-holonomy configuration the two branches carry. **[PHYSICAL]** The law constrains only *differences* (the coboundary form, §2), never the absolute magnitude: a configuration and its tenfold rescaling both telescope cleanly and equally satisfy every constraint here (verified). So "the content increment" is forced in form and free in size — the size being where the actual physics of a given process enters, exactly as the holonomy itself is the physical input upstream of the click-law.

---

## 5. The open frontier: what fixes the spacing

Paper II does **not** leave a contradiction to reconcile: paper4 §5 (the capacity constant `η_A`) and paper4 §71–76 (the seal-firing law) are mutually consistent (§3.3). What it leaves open is the genuine question *what fixes the inter-seal spacing `d`* — and the obstruction is that three distinct quantities are in play, on three different footings:

- the **structural capacity** `W_* = 0.36478` (the ceiling, from `η_A`) — forced, but only a *bound*;
- the **seal-firing content**, which is sub-capacity and **mode-dependent** (`C(η_B) = 0.156` one-mode-parity, `C(h_*) = 0.109` coupled) — robustly *below* `W_*`, but not a single number;
- the **evidence clock** `I ~ Exp(1)` (mean 1 in RN units) on which firing actually runs — a *random* variable, and moreover one in *evidence* units: turning its mean-1 firing into a *content* spacing `d` would require the rate `κ` (the no-go floor), the one quantity the records provably cannot supply. So the evidence clock cannot fix a content `d` either.

None of the three delivers a forced deterministic content spacing: `W_*` is a bound not an equality, the firing content `C(η_B)`/`C(h_*)` is mode-dependent, and the evidence clock is random *and* `κ`-blocked. Identifying the per-seal *content spacing* `d` with the content at the firing fixed point (`d = C(η_B)`, say) is itself a modeling step the corpus does not state — of the *same* character as the rejected `d = W_* = C(η_A)`. So the honest open obligation is sharper than "pick a root": it is **whether, and how, the seal-firing law's sub-capacity commitment fixes a content spacing `d` at all**, given that the firing content is mode-dependent and the firing clock is random. Three live routes:

1. **A completeness / canonicalization principle.** Is the spacing pinned to one mode (e.g. the one-mode-parity slice `η_B`), or pushed up to the capacity `W_*` by a principle under which a record may not commit before finishing its self-consistent diamond? paper4 §69 weighs against any *fixed-content* threshold (the selected `η` drifts with the renewal shape); §71 then fixes that shape and the unit `r = 1`, leaving the **ledger/mode dependence** (§3.3) as the live non-canonicity — so this route demands a genuine principle, not a stipulation. This is the decisive, currently-open structural question.
2. **The cross-tier bridge (Paper III).** Fix `d` from an *independently derived* Tier-B gravitational dimensionless coefficient. The scale no-go *permits* this precisely because `d` is **weight-zero**: a derived dimensionless gravitational number (the area-law coefficient, the geometry-universal constant, or `W_*` itself) equalling the per-seal content would pin the spacing — without ever manufacturing the forbidden absolute scale. That the one-mode firing root already satisfies `1/η_B = 1.641…` (the corpus's 1d mass-gap correlation length) is a suggestive thread for this bridge.
3. **A non-circular variational principle** on the inter-seal stretch whose extremum selects the spacing — distinct from merely restating "maximize packing."

Other inherited residues are unchanged from Paper I and untouched here: the entanglement correlation between parallel chains, the free inter-seal coherence profile, and the magnitude `κ` (the no-go floor).

---

## 6. What this paper does and does not claim

It **claims**, with high-precision receipts: that the content increment is forced to be the coboundary `dχᵢ = h_{i+1} − h_i` of *some* scalar potential (the discrete Poincaré lemma / Paper I's odometer / the corpus coboundary law), so the clock's *form* is generated by the ledger (§2); that `W_*` is a genuine forced capacity (`W_* = max_η min(C,J)`, the unique crossing of rising content and falling Fisher capacity, given Paper I's single-channel screen), so the spacing obeys the forced ceiling `d ≤ W_*` given that what commits is a non-over-saturated diamond — a bound composition-self-consistency could not give (§3.1–3.2); that paper4's capacity law (§5, constant `η_A`) and its seal-firing law (§71–76, the vector fixed point `∂ψ/∂h = e^{−h}`) are **distinct and mutually consistent**, the firing law committing **strictly below** `W_*` in every mode checked (`C(η_B) = 0.156` one-mode-parity, `C(h_*) = 0.109` coupled — receipt `p2c`), the firing running on a random evidence clock `I ~ Exp(1)` (§3.3); and that the magnitude of the increments and the conversion `κ` remain, respectively, physical input and the one no-go floor (§2, §4).

It does **not** claim: that `d = W_*` is forced — the *postulate* `(P-sat)` that would force it ("seal at capacity") is contradicted by the corpus's sub-capacity seal-firing law, and reaching `d = W_*` would require *overriding* that law with a completeness principle (§3.3, §5); that §5 and §71 are in conflict (they are *consistent* — one fixes a capacity constant, the other a firing threshold below it); that `η_B` is *the* canonical seal root (the firing root is **mode-dependent**); a value for `κ` (the no-go floor); a derivation of the realized potential magnitudes (physical input); or any geometric/relativistic content (nothing here presupposes spacetime). The honest one-line summary: **the record ledger generates the clock's form (a forced coboundary) and a forced capacity ceiling on the spacing (`d ≤ W_*`); the corpus's own seal-firing law is consistent with that ceiling and commits strictly *under* it (mode-dependently, on a Poisson clock), so what fixes the exact spacing `d` is the genuine open obligation — and `d = W_*` is the one reading the firing law denies.**

---

## 7. Precision discipline

Every numeric quantity was computed in mpmath at `dps ≥ 100` (here 140) and sympy-exact where the structure permits. The `KL = Fisher` root `W_* = 0.364784952089976…` (balance residual `1.3×10⁻¹⁴¹`), the monotonicity of `C(η)` and `J(η)` and their single crossing, the `W_* = max_η min(C,J)` saturation identity, the coboundary/telescope identities, and the rescaling-invariance of the form (magnitude-free) are all in `v7/code/p2a_content_supply.py` (13 machine checks, all pass). The capacity constant and the seal-firing roots of §3.3 are in `v7/code/p2b_event_law_saturation.py` (13 checks) and `v7/code/p2c_vector_ledger_roots.py` (25 checks): the self-consistency constant `η_A = 1.090344354879492…` (`C = J`, `W_* = 0.364784952089976…`); the one-mode-parity seal value `η_B = 0.609377863436006…` (`tanh η_B = e^{−η_B}` to working precision), content `C(η_B) = 0.156109… < J(η_B) = 0.704402…` (under capacity), `1/η_B = 1.641018…`; and the coupled three-statistic seal value `h_* = 0.495053…` (vector fixed point `∂ψ/∂h = e^{−h}`, all components equal, commitment potential strictly convex), content `C(h_*) = 0.109004… < W_*`. The structural robustness of `content < W_*` is also in `p2c` (TASK 6): `C(η)` strictly monotone (`C′ = η sech²η > 0`) and bounded (`C → log 2`), `C(η_A) = W_*` exactly, the cochain unit to reach `W_*` is `λ ≈ 0.208 < 1` (inadmissible), and over the symmetric character group the per-mode coefficient *falls* (`η_B = 0.609 → 0.495 → 0.368` for 1/3/7 characters) — so within the admissible class `C(η_B) = 0.428 W_*` is the supremum. The class is load-bearing: dropping the count-dual base (a skewed base `μ(+) = 0.2`) gives content `0.526 > W_*` (`p2c` exhibits this), which the count-dual/orthogonality gates exclude. The corpus potential/increment reproductions are exact to `< 10⁻¹⁰⁰`. Never float64 for the cancellation-heavy self-consistency balance.

---

## References

**Companion (this program).**

[I] *The record click-law, I: a self-consistent pre-geometric sealing law and its emergent thermodynamic limit* (`v7/relativistic-isp-v7-paper1-record-click-law`) — the forced shape; the odometer; the divisible `exp` and indivisible skeleton; the free spacing this paper bounds.
[4] *SHARD: Sealed Holonomy and Record Dynamics* (v6 paper4) — the record diamond, the one-diamond `KL=Fisher` constants (§5), the closed-holonomy cochain and source-as-coboundary law (§34–45), and the intrinsic division-event/seal-firing commitment law as a vector fixed point `∂ψ/∂h = e^{−h}` on the complete primitive ledger (§71–76; the non-canonicity of a fixed-content threshold, §69).
[10] *The Arrow-Positivity Theorem* (v6 paper10) — `σ = D(P_AB‖P_BA)` as entropy production; the eventless-collar primitive-Markov presentation.
[XI] *Emergent Einstein equations without an emergent Newton constant* (`v6/publishable/paper-XI-sealed-record-gravity-no-go`) — the scale no-go (`κ`/`G` forbidden, dimensionless data eligible); the derived gravitational dimensionless coefficients the cross-tier route of §5 would use.

**External.**

[A] J. Aczél, *Lectures on Functional Equations and Their Applications* (Academic Press, 1966).
