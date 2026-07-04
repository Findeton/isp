# The onset of the forced regime: the exact click-law crossover, and the record count at which the conformal order becomes readable

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-07-02. Eighth paper of the v8 line — **new research, not consolidation** (extends paper 1 §3.3–3.4 on the content axis and papers 4 §1 / 7 §2 on the order axis; supersedes nothing). Tags as in paper 1. Precision discipline: the §2 theorems are proved in-paper with mpmath `dps = 60` corroboration; the §3 Monte-Carlo landscape is float64 (a *measurement*, per the corpus rule — every asserted analytic anchor is mpmath). Receipts in `code/`.

## Abstract

Between "one record" and the corpus's forced regimes sits a crossover the corpus had priced only qualitatively: paper 1's premise **(a)** takes seals *dense* on the content axis and calls the sparse regime "weaker" without a modulus, and papers 4/7 demonstrate the order→conformal readout at comfortable sizes (`N = 400–3000` in paper 4 §1; `N = 480` in paper 7's battery) without saying when it turns on. This paper supplies both moduli. **(1) The content axis [THEOREM].** For seals on a lattice of spacing `d` (content units), *every* admissible inter-seal survival profile — monotone, through the forced skeleton `S(kd) = S(d)^k` — satisfies `|log S(χ) + κχ| < κd` uniformly in `χ`, and the bound is exactly tight: the hold profiles approach deviation `±κd`, so **the sparse freedom's sup-norm radius around the dense exponential is exactly `κd`** — the crossover is linear in the spacing, two-sided, with constant exactly `1`, and the per-cell band is paper 1's squeeze `s^k(1−s)`. Corollary: an experiment resolving log-survival to `±ε` cannot distinguish any sparse profile from the dense law iff `κd ≤ ε` — the forced-shape onset density is `ρ* = κ/ε`. Premise (a) is thereby **delimited, not discharged**: the click-law *shape* degrades linearly and controllably as seals thin, and "dense vs sparse" becomes a measured dimensionless parameter `κd` rather than a binary. The inter-seal *coherence witness* is explicitly not covered — that freedom is the genuinely-quantum content (paper 1 §3.4/§3.5) and survives at every `d > 0`. **(2) The order axis [DEMONSTRATED].** With manifold-like input (fixed-`N` diamond sprinklings; coordinates held out as scoring truth only) and the tolerance floors of paper 7's certificate (`0.15` dimension units on the Myrheim–Meyer axis, `0.40` on the midpoint axis), the order→conformal readout **turns on at measured record counts**: in `M²`, `N*₁ = 128` (d_MM) and `N*₃ = 64` (midpoint) — the certificate's **dimension-axes onset** `N* = 128` (the two axes with N-free tolerances; the height and abundance axes are scored separately, §3.1); in `M³`, `N*₁ = 1024` (borderline at `512`: `22/25` seeds, disclosed) and `N*₃ = 256`. Below onset the readout is *void*, not merely noisy (`N = 16`: `38%`/`18%` pass). The d_MM error concentrates as `N^{−α}`, fitted `α = 0.507` (the U-statistic `N^{−1/2}`, as expected); the height axis lands within `4%` of the Baik–Deift–Johansson finite-size law `E[H] ≈ 2√N − 1.7711·N^{1/6}` for `N ≥ 256` [IMPORT]; the abundance profile's internal TV falls monotonically (`0.095 → 0.0004`), crossing paper 7's `0.03`-scale at `N = 64`. **(3) The ladder.** One record: neither law readable. Content axis: the click-law shape is operationally forced once `κd ≲ ε` — a *per-chain* condition, cheap, met early. Order axis: the conformal class becomes readable and certifiable only at `N ≳ 10²` records (`2D`) to `10³` (`3D`) — the geometric readout is the *expensive* onset. What stays gated is unchanged and stated: manifoldlikeness itself (papers 4 §5, 7), covariance (paper 4 §6), the spacing `d` (paper 1 §4.4 — this paper *prices* the distance from dense; it does not fix `d`), and the conversion `κ`.

## 1. The two axes, and what "onset" means here

**The question.** The corpus's Tier-A results are conditional on regime premises: the dense-seal premise **(a)** for the unique exponential (paper 1 §3.3), and — for anything geometric — enough records for the order→conformal estimators to mean something (papers 4 §1, 7 §2). "How does the forced regime *turn on*, starting from one record?" is then two separable questions with two different parameters:

- **the content axis** — one commit chain, seals every `d` units of accumulated content `χ`; parameter: the dimensionless `κd` (`κ` the free conversion of paper 1 §3.6). Sparse→dense is `κd → 0`.
- **the order axis** — the record web as a partial order, `N` records; parameter: `N`. The conformal readout stabilizes as `N → ∞` *given* manifold-like order.

The two axes are independent inputs (a chain can be seal-dense while the web is tiny, and vice versa), so the onset story is a *ladder*, not a single threshold. §2 proves the content-axis crossover exactly; §3 measures the order-axis onset; §4 assembles the ladder and its guards.

**What this paper does not claim.** Nothing here derives *emergence*: §3 is conditional on manifold-like input by construction (the gate is papers 4 §5 and 7), and §2's theorem is about the *committed survival readout* — the sparse regime's coherent inter-seal content remains exactly as free as paper 1 §3.4 left it. The deliverable is the onset of the **forced click-law shape** and of the **readable conformal order** — the two regimes the corpus already owns, now with their thresholds.

## 2. The content axis: the exact crossover [THEOREM]

### 2.1 The setting and the admissible class

Paper 1 §3.4: sparse seals at the lattice `L = {kd}` force the geometric skeleton `S(kd) = S(d)^k =: s^k` by finite induction (no regularity), with the inter-seal profile free; committed survival is monotone nonincreasing *by definition* (§3.5 there); and on the lattice `S(d)^{χ/d} = e^{−κχ}` identically, `κ := −log S(d)/d`. Call a profile **admissible** if `S : [0,∞) → (0,1]` is monotone nonincreasing with `S(0) = 1` and `S(kd) = s^k` for all `k`. The dense law `e^{−κχ}` is admissible; the question is how far any other admissible profile can sit from it.

### 2.2 The crossover theorem, exact both ways

> **Theorem 2.1 (uniform crossover bound).** For every admissible profile and every `χ ≥ 0`: `|log S(χ) + κχ| < κd` off the lattice, `= 0` on it. Equivalently `e^{−κd} < S(χ)·e^{κχ} < e^{κd}`.

*Proof.* For `χ ∈ [kd, (k+1)d]`, monotonicity plus the skeleton pin `S(χ) ∈ [s^{k+1}, s^k]`, and `e^{−κχ}` lies in the same interval; both logs lie in `[−κ(k+1)d, −κkd]`, an interval of width `κd`, and `−κχ` is interior for interior `χ`. ∎

> **Theorem 2.2 (tightness — the freedom's exact diameter).** The hold-high profile `S⁺(χ) = s^{⌊χ/d⌋}` and hold-low profile `S⁻(χ) = s^{⌈χ/d⌉}` are admissible, and `sup_χ [log S⁺(χ) + κχ] = κd`, `inf_χ [log S⁻(χ) + κχ] = −κd` (extrema over `χ` for the stated profiles; approached, not attained — the class-radius statement is the consequence drawn below).

*Proof.* Both are monotone step profiles through the skeleton. On `[kd, (k+1)d)`, `log S⁺ + κχ = κ(χ − kd) ↑ κd` as `χ ↑ (k+1)d`; symmetrically for `S⁻`. ∎

So the admissible class's sup-norm radius around the dense exponential, in log-survival, is **exactly `κd`** — linear in the spacing, constant exactly `1`, two-sided. The crossover has no threshold, no plateau, and no hidden constant.

**Corollary 2.3 (the per-cell band is paper 1's squeeze).** On cell `k` the allowed survival band has width `s^k(1−s)` — precisely the squeeze amplitude `B(d)` of paper 1 §3.4 — and globally `|S(χ) − e^{−κχ}| < 1 − s ≤ κd`.

**Corollary 2.4 (detectability / the onset density).** A measurement resolving log-survival to `±ε` cannot distinguish *any* admissible sparse profile from the dense exponential iff `κd ≤ ε` (Theorem 2.1 gives the "if"; Theorem 2.2 gives a distinguishable profile whenever `κd > ε`). The forced-shape onset spacing is `d* = ε/κ`; the onset density `ρ* = κ/ε` seals per unit content. One-directional care: `κd > ε` makes *some* profile distinguishable, not every one.

**Two structural companions.** (i) The per-cell *average* hazard is `κ` exactly for every admissible profile (`Λ((k+1)d) − Λ(kd) = κd` identically, `Λ = −log S`): the freedom lives entirely in *where within the cell* the hazard sits, never in its cell budget. (ii) The dense limit is the `d → 0` face of the skeleton, not a separate postulate — the identity `S(d)^{χ/d} = e^{−κχ}` (paper 1 §3.4), re-verified sympy-exact in the receipt.

### 2.3 What this does and does not do to premise (a)

**Delimited, not discharged.** Premise (a) — dense seals — remains an assumption about the physical realization; nothing here derives seal density (the spacing `d` is [OPEN], bounded by `d ≤ W_*` and mode-disciplined, paper 1 §4.2–4.4, and this paper's theorem *prices* distance-from-dense without fixing `d`). What changes is (a)'s *role*: the click-law shape claim no longer degrades from "forced" to "unconstrained" at the regime boundary — it degrades **linearly and controllably**, with the exact modulus `κd`, and "dense vs sparse" becomes an operational dimensionless parameter with a detectability threshold (Corollary 2.4) rather than a binary premise. In paper 1's terms: §3.3's `[CONDITIONAL(a, …)]` survival shape is, on the shape axis alone, now `[CONDITIONAL(κd ≤ ε, …)]` with `ε` the stated resolution — a premise an experiment can price.

**What survives at every `d > 0` — stated as prominently.** The *coherence witness* between seals (the off-diagonal decoherence-functional content) is not an admissible profile in the sense above — it may rise transiently, and its freedom is the genuinely-quantum content the dense limit annihilates (paper 1 §3.4–3.5; v6 Paper 56's CP-divisibility line, with the Tier-1 seal-supply/sparseness functor there **still open** — this section delimits the survival readout, it does not build that functor). No-revival for *committed* survival stays definitional; the observable revival fingerprint lives in the coherence axis and is bounded per cell only in the survival-band sense of Corollary 2.3.

## 3. The order axis: the conformal-order onset [DEMONSTRATED]

### 3.1 Methodology and onset definitions (disclosed in full)

**Input and held-out discipline.** Fixed-`N` (binomial) sprinklings of causal diamonds in `M²` and `M³` — the field's standard finite-`N` surrogate for Poisson, and the fixed-`N` choice is exactly what makes the §3.2 BDJ comparison an equality-in-law statement — a *manifold-like order by construction*; the coordinates are held out as scoring ground truth and never fed to the estimators (papers 4 §1, 7 §2 methodology). This section therefore measures **when the instruments turn on given geometric input** — the readout onset — and says nothing about whether record webs *are* manifold-like (the gate: papers 4 §5, 7).

**Estimators.** Standalone copies of paper 7's `g1` battery (same definitions, so onsets are commensurable with the certificate's bands): Myrheim–Meyer `d_MM` (ordering-fraction inversion, exact `f(d)` anchors), height `H` (longest chain), midpoint-scaling `d_mid` (`NaN ⇒ fail`), and the interval-abundance profile `(N₀…N₅)`.

**Onset rule (N-independent tolerances, from paper 7's operative floors).** The two *dimension-unit* axes take paper 7's certificate floors as tolerances — `|d_MM − d| ≤ 0.15`, `|d_mid − d| ≤ 0.40` — and the onset `N*` per axis is the smallest tabulated `N` (powers of two; grid resolution is the quote's precision) at which `≥ 90%` of seeds pass **and** every larger tabulated `N` also passes (the stable-upward rule; seed counts `40/40/40/40/40/40/25/15` for `N = 16…2048` in 2D, `30…15` in 3D — disclosed because the `90%` quantile is coarse at small seed counts). The height axis has no `N`-free tolerance and is scored against the Baik–Deift–Johansson finite-size law instead [IMPORT]; the abundance axis is scored as internal concentration (median TV of a seed's profile against the same-`N` ensemble mean), with paper 7's `0.03` threshold quoted as the `N = 480`-calibrated scale it is, not as an `N`-free constant.

### 3.2 The measured onsets

**`M²` (receipt `o2`, seeds/sizes as above):**

| `N` | med `\|d_MM−2\|` | pass₁ | med `\|d_mid−2\|` | pass₃ | `H` mean / BDJ | med TV |
|---|---|---|---|---|---|---|
| 16 | 0.189 | 38% | 0.528 (22 NaN) | 18% | 5.6 / 5.2 | 0.095 |
| 32 | 0.142 | 55% | 0.193 | 72% | 8.7 / 8.2 | 0.054 |
| 64 | 0.084 | 78% | 0.142 | **95%** | 12.6 / 12.5 | 0.026 |
| 128 | 0.051 | **95%** | 0.085 | 100% | 19.6 / 18.7 | 0.012 |
| 256 | 0.036 | 100% | 0.056 | 100% | 28.0 / 27.5 | 0.005 |
| 512 | 0.024 | 100% | 0.033 | 100% | 41.4 / 40.3 | 0.002 |
| 1024 | 0.021 | 100% | 0.033 | 100% | 58.8 / 58.4 | 0.001 |
| 2048 | 0.013 | 100% | 0.027 | 100% | 84.6 / 84.2 | 0.0004 |

*(Midpoint medians are over the non-NaN seeds only — the NaN count is shown where nonzero; the pass-rate columns count NaN as fail.)*

> **Onsets, `M²`: `N*₁ = 128` (d_MM), `N*₃ = 64` (midpoint) — the certificate's dimension-axes onset `N* := max(N*₁, N*₃) = 128`** (two of the four axes — the two with `N`-free tolerances; not the full four-axis certificate, whose height/abundance bands are per-`N` control-calibrated).

**`M³`:** `N*₁ = 1024`, `N*₃ = 256`. The d_MM onset is quoted conservatively under the stable-upward rule: `N = 256` reaches exactly `90%` (`27/30`) but `N = 512` dips to `88%` (`22/25` — one seed short of the quantile at that seed count), so the stable value is `1024`; the honest reading is **"between `256` and `1024`, conservatively `1024`"**. The 3D readout needs roughly an order of magnitude more records than 2D on the same tolerance — higher dimension is *harder* to read at fixed `N`, as the ordering-fraction geometry predicts.

**Three quantitative companions.** (i) **Scaling:** the median d_MM error fits `N^{−α}` with `α = 0.507` over `N ≥ 64` — the `N^{−1/2}` of a U-statistic's concentration (the ordering fraction is a pair average), as expected [IMPORT, standard]. The onset count for a tolerance `τ` therefore scales as `N*(τ) ∼ τ^{−2}`: certifying one more decimal digit of dimension costs `100×` the records. (ii) **The height law:** mean `H` lands within `4%` of `2√N − 1.7711·N^{1/6}` for every `N ≥ 256` (at `N = 2048`: `84.60` measured vs `84.20`) — the Vershik–Kerov/Logan–Shepp constant with the Baik–Deift–Johansson Tracy–Widom correction, imported and confirmed on the record-order implementation; the `11%` deficit paper 7's `g1` noted at `N = 480` against the bare `2√N` is exactly this finite-size term. (iii) **Below onset the readout is void, not noisy:** at `N = 16`, `38%`/`18%` pass and `22/40` seeds cannot even form a midpoint estimate (NaN) — there is no "approximate geometry" reading at tens of records; the conformal readout *has* an onset, it does not fade in from `N = 1`.

## 4. The ladder, assembled

| Regime | Content axis (one chain) | Order axis (the web) |
|---|---|---|
| one record | no law — a single commit has no survival curve and no order statistics | no geometry — `N = 1` has no pairs |
| few records (`N ∼ 10¹`) | skeleton forced at whatever `d` holds; shape free within `±κd` | readout **void** (`38%/18%` pass at `N = 16`; midpoint mostly NaN) |
| `κd ≤ ε` (chain) | **click-law shape operationally forced** — no admissible profile distinguishable at resolution `ε` (Cor 2.4) | — |
| `N ≳ 10²` (2D web) / `10³` (3D) | — | **conformal order readable** at paper 7's dimension-axis floors (`N* = 128`/`1024`); improves as `N^{−1/2}` |

Reading: the click-law's shape is the *cheap* onset — a per-chain, per-resolution condition met as soon as sealing is moderately dense in content — while the geometric readout is the *expensive* one, needing hundreds to thousands of records before the conformal class means anything statistically. "One record → forced spacetime" is therefore two ladders apart from a single record even under the friendliest assumptions: first `κd ≲ ε` (the law), then `N ≳ N*` (the readable order) — and above both still sit the gates.

**What remains gated, unchanged:** manifoldlikeness itself (papers 4 §5 and 7 — §3's input is manifold-like *by construction*); covariance (paper 4 §6); the spacing `d` (paper 1 §4.4 — [OPEN], `d ≤ W_*`; this paper prices `κd`, it does not fix it); the conversion `κ` (paper 1 §3.6 no-go); and the sparse regime's coherence content (§2.3 — free at every `d > 0`, the quantum face). No claim in this paper crosses any of these.

## 5. Honest scope

§2 is a theorem about the *committed survival readout* under the corpus's own definitions (monotone survival, forced skeleton): it neither derives seal density nor constrains the inter-seal coherence witness, and the detectability corollary is resolution-relative by construction. §3 is a *conditional measurement*: manifold-like input, flat diamonds only (no curvature, no topology change), two dimensions of tolerance imported from paper 7's operative floors (the height and abundance axes are scored against an import and an internal-concentration metric respectively, because no `N`-free tolerance exists for them); onsets are quoted at power-of-two grid resolution under a disclosed stable-upward rule, and the 3D d_MM onset carries a disclosed borderline (`22/25` at `N = 512`). The `N^{−1/2}` scaling is a fit (`α = 0.507`, `N ≥ 64`) consistent with the standard U-statistic rate, not a proved rate for record orders. Nothing here bears on whether physical record webs realize manifold-like orders — that is the gate, flanked in paper 7 and still [OPEN].

## 6. Receipts

All in `code/`, run green this date: `o1_clicklaw_crossover.py` (11/11 — the skeleton recursion's induction step and the `S(d)^{χ/d} = e^{−κχ}` identity sympy-exact (the forcing premise itself is paper 1 §3.4's); Theorem 2.1 strict on `200` random admissible profiles across five `(κ, d)` regimes, worst normalized deviation `0.508 < 1`; Theorem 2.2's hold profiles reaching `±(399/400)·κd` on the scoring grid, with the hold profiles checked admissible *as functions* (monotone on a 1165-point grid, exact skeleton hits); Corollary 2.3's band `s^k(1−s)` exact and the global `1−s ≤ κd` cap; Corollary 2.4 exercised in *both* directions (at `0.9·d*` all 40 sampled profiles within `ε`; at `1.5·d*` the hold profile exceeds `ε`); the measured hold-profile sup deviation halving exactly under `d → d/2` plus the linear scaling of random-profile deviations; the profile-independent per-cell hazard budget `κd` — mpmath `dps = 60`, fixed seed), `o2_estimator_onset.py` (12/12 — the `f(d)` anchors at `dps = 40`; the 2D and 3D sweeps with the tables of §3.2; onset existence and upward stability; the void-below-onset check; the `α = 0.507` fit; the BDJ agreement `≤ 4%` for `N ≥ 256`; monotone TV concentration and the `0.03`-scale crossing; the 3D ordering `N*₁(3D) ≥ N*₁(2D)`; the 3D-midpoint convergence test (void at `N = 16`, majority-pass by `128`, `100%` at `1024`) — float64 measurement landscape, `default_rng(20260702)`, estimator definitions copied from `g1` with the boolean matmuls in exact-range float32 BLAS). Dependencies: none beyond numpy/mpmath/sympy; `o2`'s estimators are standalone copies of `g1_estimator_concordance.py`'s (paper 7), kept definitionally identical so the onsets are commensurable with the certificate bands.

## References

**This series.** Paper 1 (the click-law, the sparse skeleton and squeeze `B(d)`, premises (a)/(b1)/(b2), the `κ` no-go, the spacing ledger); Paper 4 (order→conformal with the held-out methodology; the gates); Paper 7 (the four-axis certificate whose floors §3 imports; the `g1` battery; the manifoldlikeness flanks); Paper 6 (where the sparse coherence freedom meets phenomenology). Ledger: `LEDGER.md`.

**External.** J. Aczél, *Lectures on Functional Equations and Their Applications* (1966) — the dense-regime uniqueness import (via paper 1); J. Myrheim, CERN TH-2538 (1978), and D. A. Meyer, MIT PhD thesis (1988) — the dimension estimator; L. Bombelli, Syracuse PhD thesis (1987) — midpoint scaling; D. Benincasa, F. Dowker, Phys. Rev. Lett. **104**, 181301 (2010), and L. Glaser, S. Surya, Phys. Rev. D **88**, 124026 (2013) — interval abundances; A. M. Vershik, S. V. Kerov, Soviet Math. Dokl. **18**, 527 (1977), and B. F. Logan, L. A. Shepp, Adv. Math. **26**, 206 (1977) — the `2√N` law; J. Baik, P. Deift, K. Johansson, J. Amer. Math. Soc. **12**, 1119 (1999), and C. A. Tracy, H. Widom, Commun. Math. Phys. **159**, 151 (1994) — the `N^{1/6}` fluctuation term and its mean (`−1.7711`); W. Hoeffding, Ann. Math. Statist. **19**, 293 (1948) — U-statistic concentration (the expected `N^{−1/2}`).
