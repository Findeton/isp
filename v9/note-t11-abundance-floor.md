# T1.1 — the abundance campaign's go/no-go: the backwards derivation, the exact reference law, the comparability block, and the faithful floor

**Status:** derivation note + theorem statements, 2026-07-05 (PLAN.md T1.1 — the master fork). Receipt: `v9/code/s0_abundance_floor.py` (the exact-law verification, the variance hypothesis, the floor observable, the cluster pricing). The receipt name `s0` is reserved here (PLAN reserved `s1` for the growth bench; the floor gets its own).

## 0. The verdict up front

The go/no-go question — *is the faithful floor of the backwards-derived abundance action sub-quadratic?* — decomposes on derivation into two rows with different answers and different jobs:

1. **The pair-block comparability row** (the `k = n` instance of paper 11 Thm 2.2, with pair multiplicity): faithful floor **O(N)** with exact constants — immediate, unconditional — and this row *alone* carries **both Ω(n²) walls** (the antichain/sparse class and the dense-compromise class). The u-line's both-sides demand is answered by the ledger's own top row.
2. **The per-interval abundance rows** (the cluster-adversary axis paper 11 §4 named): the reference law `E[A_j(k)]` is derived here in **closed form** (Beta/digamma — exact at every finite `k`, no asymptotic-bias term), which reduces the floor to a single named variance hypothesis (H-var). Conditional on H-var: **E[S_ab] = Θ(N log² N)** — the same class as paper 11's `S_r`. H-var is measured in the receipt.

**The master fork's answer: ALIVE — executed same-date, receipt `s0` 9/9.** Row C's floor matches the exact `(n−2)/18 + ¼` at every tested `N`; the closed-form abundance law is confirmed against Monte Carlo within the pre-registered 4-SEM gate at every `(k, j)` (max deviation `1.24` SEM); H-var measures Poisson-flat (`Var/E ≈ 0.8–1.1`, fitted `k`-exponent `0.054`); the floor observable passes its pre-registered gate (max/min `2.22` over `N = 256–1024`) *and* — the stronger read, added at first execution before any verdict was consumed — the exact-law finite-`N` prediction **tracks** the measured totals at a flat ratio of `0.89/0.96/0.90` (the first run printed `0.45`-class ratios from a factor-2 pair-count bug — `nonzero` of the strict dominance matrix already enumerates each unordered related pair once; caught by the bundle review, fixed and re-run, and the fix *strengthened* the tracking; the first draft's attribution of the offset to the `Var ≈ r̄·E` approximation was wrong and is retracted): the rising normalized observable is the law's own finite-`N` shape, and the floor claim stands on the law. The cluster adversary is priced at `7.4×` k-matched (`k ∈ [8, 288]`). Tier 1.2/1.3 unblocked — no quadratic floor anywhere in the derived family, conditionally for the abundance rows with the condition named and measured. Tier 1.2 (the sandwich) and 1.3 (the growth bench) are unblocked.

## 1. The backwards rows, in the ledger's own discipline

Faithfulness (the order is a sprinkling of a causally convex region) forces, by paper 11's heredity theorem, that *every* interval is a rectangle sprinkling, and — the top row — that the global order itself is a diamond sprinkling. Each forced statistical law is a ledger row; the action charges squared misfit against the law, one constraint per pair, exactly as `S_r` does.

**Row C (comparability block).** For every unordered pair `{u, v}` of a faithful order, `P(u ∼ v) = ½` (Thm 2.2's kernel at `k = n`), and the block average `r_P` obeys the exact U-statistic law `E[(r_P − ½)²] = Var(r_n) = (2/(n(n−1)))·[2(n−2)/36 + 1/4] ≈ 1/(9n)`. The block has `n(n−1)/2` exchangeable rows; its aggregate charge with row multiplicity is

> `S_comp(P) = (n(n−1)/2)·(r_P − ½)²`.

*Framing honesty (the PLAN's scope correction, kept):* the multiplicity is the same per-pair convention `S_r` uses (one constraint per pair; the block's rows are exchangeable so they enter through their mean), but nothing in Cor 4.2 *mandates* this weight for a growth measure — `S_comp` is the ledger-natural choice, disclosed, and the sandwich theorem treats it as sufficient-condition engineering.

**Row A (interval abundance).** For a related pair with interior size `k` (a `k`-point rectangle sprinkling), the small-interval abundance counts `A_j = #{related interior pairs with interior exactly j}` obey an **exact** law. Conditioning on the pair's lightcone gap fractions `(w₁, w₂)`, an interior related pair with gap rectangle of area `s = w₁w₂` has `P(interior = j) = C(k−2, j)·s^j(1−s)^{k−2−j}`, and the gap-area density for a dominated pair in the unit square is `g(s) = (1+s)·ln(1/s) − 2(1−s)`. Hence, exactly at every finite `k`:

> `E[A_j(k)] = k(k−1)·C(k−2, j)·∫₀¹ g(s)·s^j (1−s)^{k−2−j} ds`,

and the integral is closed-form via `∫₀¹ s^a(1−s)^b ln(1/s) ds = B(a+1, b+1)·[ψ(a+b+2) − ψ(a+1)]`:

> `E[A_j(k)] = k(k−1)·C(k−2, j)·{ B(j+1, k−1−j)[ψ(k) − ψ(j+1)] + B(j+2, k−1−j)[ψ(k+1) − ψ(j+2)] − 2[B(j+1, k−1−j) − B(j+2, k−1−j)] }`,

with leading behavior `E[A_j(k)] = k·(ln k + c_j + o(1))` for each fixed `j` (the receipt prints the exact values and the Monte Carlo agreement; `dps = 60`). **The reference is exact — the misfit below carries no asymptotic-bias term by construction.** The per-pair abundance charge, in the `A_j/k` normalization whose fluctuation scale is the estimator's own:

> `m_ab(I) = Σ_{j=0}^{J} (A_j(I)/k − E[A_j(k)]/k)²`,  `J = 2`,  and  `S_ab(P) = Σ_{x ≺ y, |I| ≥ m₀} m_ab(I(x, y))`,  `m₀ = 8`.

## 2. The walls and the floor from Row C [THEOREM, elementary]

**(a) Faithful floor.** `E[S_comp] = (n(n−1)/2)·Var(r_n) = (n(n−1)/2)·(2/(n(n−1)))·[2(n−2)ζ₁ + ζ₂] = 2(n−2)/36 + 1/4 = (n+2.5)/18` — **O(n), exact.**

**(b) The sparse wall.** Any order with comparability deficit `δ_− = ½ − r_P ≥ δ > 0` pays `S_comp ≥ (n(n−1)/2)·δ²`; the antichain (`r = 0`) pays `n(n−1)/8`. The `u2` growth endpoints (`r = 0.059, 0.017, 0.000`) all pay `≥ 0.097·n(n−1)` — **Ω(n²)**.

**(c) The dense wall.** The measured dense-compromise class (`r = 0.79/0.76`, paper 13; `r ≥ 0.7` as the class boundary) pays `S_comp ≥ (n(n−1)/2)·0.04` — **Ω(n²)**. The `j2` β = 0 near-chain (`r = 0.99`) pays `≥ 0.12·n(n−1)`.

One row, both walls, floor `O(n)`. What Row C cannot do — and why Row A exists — is *sufficiency*: the jittered lattice and any `r = ½` forgery pass Row C at zero charge (the standing necessity-not-sufficiency cage logic, paper 11 §4/§6); the cluster adversary passes Row C *and* `S_r` and is exactly what Row A's profile misfit prices (measured in the receipt).

## 3. The abundance floor [THEOREM conditional on H-var; H-var measured]

**Hypothesis H-var (named, measured).** For rectangle sprinklings, `Var(A_j(k)) = O(E[A_j(k)]·polylog k) = O(k·polylog k)` for each fixed `j ≤ J`. *(The counts are sums of locally-determined indicators — near-`j` pairs are dominance-close — so Poisson-class variance is the expected behavior; the receipt measures `Var/E` over `k = 64…256` and its growth. A proof via the second-moment/dependency integral is the named refinement, not attempted here.)*

**Theorem (the floor).** Under H-var, for faithful `M²` orders: `E[S_ab] = O(N log^{2+a} N)` (with `a` the H-var polylog exponent; `a = 0` gives `Θ(N log² N)`, paper 11's class).

*Proof.* Since the reference is the exact finite-`k` expectation, `E[m_ab(I_k)] = Σ_j Var(A_j/k) = Σ_j Var(A_j)/k² ≤ C·(J+1)·polylog(k)/k` by H-var. The comparable-pair size density (paper 11 Thm 3.2's computation, reused verbatim): a related pair's gap fractions `(s, t)` carry density `4(1−s)(1−t)` with `k ≈ Nst`, so `E[polylog(k)/k · 1(k ≥ m₀)] = O(polylog(N)·log N/N)` (the same `∬_{st ≥ m₀/N} (1/st)` integral that produced the `ln²` there, with the polylog riding along), and summing over `∼N²/4` related pairs gives `E[S_ab] = O(N log^{2+a} N)`. ∎

**Why the bias term is genuinely absent (the derivation's one subtle point, stated).** Had the reference been the one-term asymptotic law `k ln k`, the per-pair misfit in the `A_j/k` normalization would carry bias² `= Σ_j c_j² + o(1) = Θ(1)` (`c_j = −ψ(j+1) − 2`) — a **fully quadratic `Θ(N²)` floor** (corrected in review from the first draft's `Θ(N²/log²N)`; a correct two-term reference has only `Θ(log²k/k²)` bias — asymptotically harmless, but at `k ≈ 64` it still doubles the per-pair misfit, so exactness is what keeps growth increments faithful at bench scale). The closed-form reference removes this failure mode exactly; any implementation that substitutes an asymptotic reference re-introduces it (a named trap for the growth bench: the increment functional must use the exact law or same-`k` control calibration).

## 4. What the receipt decides

`s0_abundance_floor.py`: (1) Row C's floor and walls (exact arithmetic + measured `(r−½)²` decay on sprinklings); (2) the closed-form `E[A_j(k)]` against Monte Carlo at `k ∈ {64, 128}`, `j ≤ 2` (`dps = 60`); (3) **H-var** measured (`Var/E` growth over `k = 64…256`); (4) the floor observable: sampled-pair estimates of `E[S_ab](N)` on sprinklings at `N ∈ {256, 512, 1024}`, normalized by `N ln² N` (flatness = the go verdict); (5) **the cluster adversary priced**: per-interval `m_ab` on the paper-11 blow-up population vs same-`k` faithful — the separation Row A exists to buy (and `S_ab(antichain) = 0` disclosed: the sparse wall is Row C's job, not Row A's). Gates pre-registered in the receipt docstring; both directions live on (4) — a non-flat floor observable at these `N` is a finding against the theorem's practical reach (the conditional theorem stands or falls with H-var, and the measured window speaks first).

## References

Paper 11 (Thm 2.1 heredity; Thm 2.2 the U-statistic law and `ζ₁ = 1/36, ζ₂ = ¼`; Thm 3.2's size-density integral, reused; §4/§6 the cluster adversary and the named abundance axis); paper 13 (§3 the dense attractor `r = 0.79/0.76`; the `j2` kernel control `r = 0.99`); u-line/paper 17 (the sparse endpoints; the two-sided demand); paper 7 (Thm 4.1/Cor 4.2 — scope note honored: the walls are engineering for a growth measure, not Cor 4.2 obligations); paper 12 (control-calibration conventions); PLAN.md T1.1/T1.2. External: Glaser–Surya PRD 88, 124026 (2013) — interval abundances (the axis's causal-set ancestry); Hoeffding (1948) — U-statistics; standard Beta/digamma integrals (Gradshteyn–Ryzhik 4.253-class).
