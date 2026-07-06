# q2 — the D* rate law for churn supplies, and powered verdict semantics

**Status:** theorem note + convention, 2026-07-05 (PLAN.md T0.2). The theorem closes the rate half of paper 16 §3's named open ("the *rate* — hence the ratio to the same-`N` faithful band — is not claimed"); the convention replaces "band-adjacent `1.2–1.5×`" language with pre-registered equivalence tests. Receipt: `v9/code/q2_rate_law_powered_semantics.py` (the identity, the collapse, the regeneration scaling, the transient, and the convention's first application — to the corner's own standing numbers).

## 1. The theorem

**Setting.** The churn supply `W(L, reset)`: `M` slots, uniform race, churn events at rate `1/L` per commit with uniform victim and `χ`-reset, exchangeable positive continuous increments; `N` commits; the canonical rank embedding `(r₁, r₂)/N` with `r₁` = commit index (an exact grid) and `r₂` = the `χ`-rank; `D*_N` its star discrepancy.

**Lemma 1 (reduction — exact).** Let `H_m(x) = (1/m)#{t ≤ m : χ_t ≤ x}` be the prefix empirical CDF of the at-commit contents and `q_k` the `k/N`-quantile of the full sample. Then

> `D*_N = sup_{m, k} (m/N) · |H_m(q_k) − k/N| + O(1/N)`,

with the `O(1/N)` an explicit `≤ 2/N` discretization sandwich (both box closures, as the instrument computes them).

*Proof.* The `r₁`-marginal is the exact grid, so an anchored box `[0, m/N] × [0, k/N]` contains `#{t ≤ m : rank(χ_t) ≤ k}` points; `rank(χ_t) ≤ k ⟺ χ_t ≤ q_k` up to ties of measure zero (continuous increments); the box area is `(m/N)(k/N)`; only corners at data thresholds matter for the sup, and the open/closed closures differ by at most `2/N`. Divide by `N`. ∎

**Lemma 2 (fleet regeneration is coupon collection).** The full slot-state process regenerates at stopping times with mean gap `τ_reg(L, M) ≤ c·L·M·log M` commits: churn events arrive at rate `1/L` per commit and each kills a uniform slot, so all `M` slots are killed within `M log M + O(M)` events with high probability — the coupon collector — i.e. within `L·(M log M + O(M))` commits; the gap has sub-exponential tails (geometric event gaps composed with the collector's tail). *(Wording correction, logged: slot ages at a renewal are dependent and generated inside the preceding cycle, so consecutive cycles are 1-dependent, not i.i.d.; Lemma 3's blocking argument survives via the standard odd/even block split — or Harris regeneration — with only the constant affected.)* ∎

**Lemma 3 (regenerative DKW with a log).** For the stationary chain, with probability `≥ 1 − 2/N` simultaneously over all prefixes `m ≤ N` and all thresholds:

> `sup_x |H_m(x) − F(x)| ≤ c₀ · √(τ_reg · log N / m)`,

where `F` is the stationary at-commit content law and `c₀` is absolute. *Proof sketch (the standard blocking argument, spelled out in the receipt's docstring):* per fixed `x`, the centered indicator sums decompose over regeneration cycles (1-dependent; odd/even split per the Lemma 2 note) with sub-exponential cycle lengths; Bernstein for sums of sub-exponential cycle contributions gives `P(|H_m(x) − F(x)| > ε) ≤ 2 exp(−c m ε²/τ_reg)` for `ε` below the Bernstein knee; a union bound over the `N` data thresholds and the `N` prefixes costs `2 log N` inside the square root; monotonicity of `H_m` and `F` extends the grid sup to the full sup at `+1/m`. ∎

**Theorem (the rate law).** For the churn supply at fixed `(L, M)`, with probability `≥ 1 − 3/N`:

> `D*_N ≤ 2 c₀ √(τ_reg(L, M) · log N / N) + c₁ · L M / N`,  `τ_reg ≤ c·L M log M`,

i.e. `D*_N = O(√(L M log M · log N / N))`. *(Scope correction, logged: the first draft claimed this "proves" the bounded band-ratio paper 16 measured; it does not — the lemma upper-bounds both `D*` and the band, but a ratio bound needs a band LOWER bound, and the iid anchored-box sup is `Θ_P(1/√N)` (the log is union-bound slack), so the theorem yields only `ratio = O(√(τ_reg·log N))`. Bounded ratio — paper 16's `1.35× → 1.01×`, and CHECK 2's own drift-free-to-decreasing normalized values — remains a MEASURED behavior with a named route to a proof: chaining over the box family per regeneration block to shed the log, plus the classical band lower bound.)*

*Proof.* Write `(m/N)(H_m(q_k) − k/N) = (m/N)(H_m(q_k) − F(q_k)) − (m/N)(H_N(q_k) − F(q_k)) ± 1/N` (the full-sample quantile satisfies `H_N(q_k) = k/N ± 1/N`). Both terms are prefix deviations covered by Lemma 3; the weight `(m/N)·√(τ log N/m) = √(m τ log N)/N` is maximized at `m = N`. The fresh-start (common-birth) transient differs from the stationary coupling on `O(L M)` *expected* pre-renewal commits (the in-expectation form; the whp form carries an extra `log N`), and `k` changed points move any anchored-box count by at most `k`, hence `D*` by `≤ k/N` — the `c₁ L M/N` term (paper 16 Thm A(iii)'s own coupling, reused). Lemma 1 assembles. ∎

**Grade, with the first execution's correction (logged 2026-07-05).** Lemma 1 exact [THEOREM]; Lemmas 2–3 and the assembly [DERIVED — the blocking argument is standard, the constants named-measured]. The first draft additionally claimed `C(L, M) ∼ √τ_reg` as the scaling content; **the first execution refuted that scaling** — measured `D*` is **M-flat** while `τ_reg` grows `∼ M log M` (the `√τ_reg` normalization spreads `2.28×` where the data collapses at `1.23×` under `√L`). The corrected reading: **`C(L, M) ≈ c·√L`, M-flat** [measured; conjecture named] — the effective per-observation dependence is the *same-lineage cluster* scale (each lineage contributes `∼L` dependent at-commit values; consecutive commits rotate slots), exactly paper 16 Thm A(iv)'s dependence range for `τ`'s fluctuation. The theorem's bound is unchanged (blocking at `τ_reg` is valid, loose by `√(M log M)`); proving the `√L` form — blocking at per-lineage renewals with an exchangeability argument across slots — is the named refinement. Sharp constants remain open.

**What it buys.** (i) Paper 16's Theorem B upgrades from "`D* → 0`, rate not claimed" to a rate with the `(L, M)` dependence explicit — every corner verdict now has a predicted scale behind it. (ii) The `N`-staircase reading (u1's `1.60×` at `N = 512` vs `1.18×` at `N = 2048`) stops being a tension: at fixed `(L, M)` the *ratio to band* is asymptotically constant but approaches from above on the transient term `c₁ L M/N ÷ Θ(√(log N/N)) = Θ(L M/√(N log N))` — the receipt checks this direction. (iii) It sets the default equivalence margin for the semantics below at the scale the theorem says fluctuations live.

## 2. Powered verdict semantics (the convention)

**The problem.** "In the cell / band-adjacent `1.2–1.5×`" has been read off single streams at 4–6 seeds; u1's `1.60×` disclosure showed the cost. An exactness-adjacent verdict must never ride an unpowered gate (LEDGER #36's lesson, now applied to *every* band verdict).

**The convention (pre-registered here, used by every subsequent receipt).**
Given `n_b` reference draws (band mean `μ_b`, sd `σ_b`) and `K` arm draws (mean `m`, sd `s`):

- **Margin:** `Δ = δ·σ_b`, with `δ = 2.0` — matching paper 16 §4's own T2 gate scale (band mean `+ 2σ`), so the convention powers the corpus's existing cell definition rather than silently redefining it — with the `δ = 1` verdict printed beside it as sensitivity. *(Correction, logged: the first draft set `δ = 1.0`, which is stricter than the corpus's own gate and manufactured REFUSED verdicts at the margin; corrected before any verdict was consumed.)*
- **CERTIFIED-IN-BAND:** the two one-sided tests (TOST) at `α = 0.05` both reject — equivalently the `90%` Welch CI for `m − μ_b` lies inside `(−Δ, +Δ)`.
- **REFUSED:** the `90%` CI lies entirely outside `[−Δ, +Δ]` on one side.
- **BAND-ADJACENT:** neither — with the *power caveat printed*: the receipt must state the minimum detectable offset at `80%` power for its `K`, so "adjacent" is never silent under-power.
- **Power rule:** a certification claim requires `K ≥ K₈₀(Δ)` — the seed count at which a true offset `0` is certified with probability `≥ 0.8`. *(Corrected, logged: the first draft computed `K₈₀` from the one-sided MDO inversion `(z₉₀+z₈₀)·SE < Δ`, which is ~55–64% joint-TOST power, not 80%; the correct condition is `Δ/SE ≥ z₀.₉₅ + z₀.₉₀`, giving `K₈₀ = 19` at `Δ = 1σ_b, n_b = 16` by formula — the receipt also prints the simulated power of the implemented procedure, `0.75` at `K = 19` and `0.56` at `K = 11`, so as-implemented certification at `Δ = 1σ_b` wants `K ≳ 25`. The CHECK-7 verdicts are unaffected — issued at `Δ = 2σ_b`, where `K = 12` power `≈ 1` — and the u-line's 4–6 seeds is a fortiori below certification power.)*

**Application discipline.** Verdict vocabulary in papers: CERTIFIED / BAND-ADJACENT / REFUSED replace "in the cell / band-adjacent / fails" wherever a band comparison is the claim; the old language survives only for layers with their own conventions (`ρ`, per-draw dispersion `z`).

## 3. First application — the corner's own standing numbers (executed)

The receipt applies the convention to **both** corner kernels — the strict-j3 corner (victim = committer; paper 16 §4's cell object, u1's `1.18×` kernel) and the uniform-victim growth kernel (u2/u3's `β_v = 0` object) — at `N ∈ {512, 2048}`, `K = 12` fresh seeds vs `n_b = 16` reference draws. *(The first draft ran only the uniform kernel and read it against the strict corner's literature values — a conflation, corrected before any verdict was consumed; the cross-kernel and cross-stream spread is itself a measured deliverable.)* Pre-registered readings and the executed verdicts:

| arm | ratio | verdict at `Δ = 2σ_b` | at `1σ_b` |
|---|---|---|---|
| `N = 512` strict | `1.36×` | BAND-ADJACENT | REFUSED |
| `N = 512` uniform | `1.63×` | REFUSED | REFUSED |
| `N = 2048` strict | `1.30×` | BAND-ADJACENT | BAND-ADJACENT |
| `N = 2048` uniform | `1.13×` | CERTIFIED-IN-BAND | BAND-ADJACENT |

Readings: (i) at `N = 512` the corner family is genuinely above band — the transient term, consistent with CHECK 5's fresh-vs-warm split — and every `N = 512` "band-adjacent" phrase in the corpus inherits that; (ii) at `N = 2048` the family is band-adjacent-to-certified, and *which* kernel looks better flips across streams vs u1 (`1.18×/1.32×` there, `1.30×/1.13×` here) — the `±0.2×` seed noise now measured, the reason 4–6-seed numbers were correctly [directional] (`K₈₀ = 19`-by-formula / `≈ 25` as-implemented at `Δ = 1σ_b`); (iii) the dispersion staircase (CHECK 8, one pooled 64-draw calibration per scale, two independent streams): **UNRESOLVED at power in both, opposite leans** — the paper-17 regrade input. The D1-family retest (`y1`, Tier 2) runs under this same convention.
## References

Paper 16 §3 (Theorem B, the rate as named open; Thm A(iii)'s coupling, reused for the transient) and §4 (the corner arc; the `1.35× → 1.01×` trend); u1 (the `1.60×` disclosure); paper 12 (the instrument; `D*` conventions); LEDGER #36 (the power lesson); PLAN.md T0.2. External: the Dvoretzky–Kiefer–Wolfowitz inequality and its blocking extensions to regenerative processes (standard; the receipt's docstring carries the self-contained Bernstein-block argument); Schuirmann's TOST (equivalence testing); coupon collector folklore for Lemma 2.
