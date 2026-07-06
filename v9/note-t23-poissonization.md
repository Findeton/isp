# t23 — Poissonization of the churn class: the dispersion layer as a theorem (T2.3; the discharge's third layer)

**Status:** theorem note, 2026-07-06 (v9 round 13; PLAN T2.3). Receipt: `v9/code/t23_poisson_intermediates.py` (gates §4, pinned pre-run; committed at pin per the freeze discipline). Target grade: **[THEOREM-track: statement + Chen–Stein skeleton with the measurable joints verified; formalization = the assembly paper's obligation]**. Role in the discharge: Theorems U (dim ≤ 2) and W (D* → 0) cover the cell's geometric layers; **Theorem P** (this note) covers the third — per-draw interval-count dispersion → Poisson — so the assembly can claim the *full three-layer manifoldlike cell* in the limit, not only volume-faithfulness.

## 1. Statement

**Theorem P (statement).** For churn-class supplies with (i) sub-geometric lifetime tails (the lifetime law's tail dominated by a geometric; exponential/geometric and concentrated laws qualify) and (ii) quasi-continuous content (atomless increments), the interval-count statistics of the rank embedding converge to Poisson: for intervals at matched expected count k, the count distribution's total-variation distance to Poisson(k) is

  `TV ≤ c · (pair-dependency density) = O( L / N )` at fixed fleet and lifetime,

so the cell's per-draw dispersion (Fano) gap obeys `|Fano − 1| = O(L/N)` and the z-layer passes in the limit at every fixed draw size.

## 2. The Chen–Stein skeleton (three lemmas)

**Lemma P1 (the dependency graph is the life partition).** An interval's count is a sum of point-indicators. Two points are dependent only through their slot-life (same-life values are comonotone — the accumulation order); distinct lives are independent given the life partition (the race-model factorization, note-u4 Addendum — already validated by u4a). So the dependency graph's neighborhoods are the lives: size Geometric(1/L), mean L, sub-geometric by hypothesis (i).

**Lemma P2 (Chen–Stein).** For a sum of indicators with dependency neighborhoods, TV(count, Poisson) ≤ Σ_{i~j} (p_i·p_j + p_{ij}) over neighborhood pairs. Per point, the neighborhood contributes O(L) partners out of N; at matched intensity the bound collapses to `O(L/N)` per unit expected count — the same-lineage pair density, exactly the object paper 16's τ-ledger already computed at the correlation level (`E[SL]/C(N,2)`-form, asymptotically `2(L−1)/(N−1)`).

**Lemma P3 (the tail hypothesis is load-bearing).** If the lifetime law has heavy tails (e.g., infinite-variance Pareto), the neighborhood-size distribution loses its geometric domination: rare giant lives contribute O(1) dependent clusters at every N, the Chen–Stein sum does not vanish, and the Fano gap plateaus — the hypothesis (i) boundary is real, not decorative. (This is also T2.1's superlinear-tail mechanism seen from the theorem side.)

**Corollary (the full-cell discharge input).** P + W + U + paper 12 ⇒ the churn class enters all three layers of the manifoldlike cell in the limit: geometry (dim ≤ 2, exact), volume (D* → 0, rate), statistics (Poisson, rate). The atoms exclusion is shared with W (atomless content is hypothesis (ii); the atomic corner fails it and is the measured pathology — consistent, disclosed).

## 3. The honest gap list (the assembly paper's obligations)

1. P1's conditional-independence step imports the race-model factorization — proved for value *rankings*; the interval-count functional needs the standard extension (counts are ranking-measurable per window — one lemma).
2. P2's constant: the Chen–Stein neighborhood sum needs the boundary-interval accounting done honestly (intervals near the embedding's corners have deficient neighborhoods — an edge-effect term, expected O(1/N) extra).
3. The "matched expected count" clause: the cell's instrument uses k ≥ 10 intervals (u1's `interval_fano`); the theorem's k-uniformity (TV bound uniform over k ranges growing with N) needs the standard stratification argument.
4. Hypothesis (ii)'s role: atomless content ⇒ no exact ties ⇒ the count functional is a.s. well-defined; the assembly states it once with W's continuity hypothesis.

## 4. Receipt t23 — the measurable joints, gates pinned

Instruments: u1's `interval_fano` (verbatim) on `web_j3`-class generators; seed `default_rng(20260720)`; float64 (measurement landscapes); 12 reps per cell unless marked; [directional] on all band reads.

- **V1 (the rate, Lemma P2):** the pooled |Fano − 1| gap at (M, L) = (32, 2) across N ∈ {512, 1024, 2048, 4096}. Pinned: the gap decreases monotonically in N (12-rep means) AND the N = 512 → 4096 decrease is ≥ 4× (the O(1/N) prediction is 8×; ≥ 4× is the generous half-band; [directional]).
- **V2 (the L-dependence, P2's density):** the gap at N = 2048 across L ∈ {2, 4, 8}: pinned monotone non-decreasing in L (the same-lineage density mechanism; 12 reps, [directional]).
- **V3 (the tail boundary, Lemma P3 — the load-bearing hypothesis):** three lifetime laws at (M, N) = (32, 2048), matched mean lifetime ≈ 4: geometric (cv² ≈ 1, qualifies), deterministic-4 (cv² = 0, qualifies — concentrated), and a heavy-tail law (lifetime = 1 + Pareto(α = 1.5), infinite variance, VIOLATES (i)). Pinned: the two qualifying laws' gaps are within 2× of each other; the heavy-tail law's gap exceeds the geometric's by ≥ 3× (the plateau signature; [directional]). REFUSED-with-both-qualifying-large ⇒ the theorem's rate is wrong, not just the tail clause — investigate before verdict prose.
- **V4 (the density ledger, P2 = paper 16's object):** the measured same-life pair density at (32, 2) across N ∈ {1024, 4096} matches the `2(L−1)/(N−1)` asymptote within 25% (paper 16's ledger re-verified on this stream; exact-count instrumentation, not an estimate).

Refusals print the ledger and exit 1 by design; the first-run ledger is preserved verbatim in this note if any amendment cycle occurs (the round-12 lesson, now under the VCS freeze: this note is committed before the receipt runs).

## References

PLAN T2.1–T2.3 (the statistical-layer bracket; T2.2 = the deterministic converse, out of this note's scope); note-u4 Addendum + u4a (the race-model factorization P1 imports); v8 paper 16 (§2 the τ/same-lineage ledger — P2's density object; §4 the cell's z layer; the L = 2 staircase residual this theorem's rate contextualizes); note-w1/Theorem W (the companion pillar; the shared continuity/atomless hypothesis); u1 (`interval_fano` — the instrument, verbatim); Chen (1975), Stein (1972), Arratia–Goldstein–Gordon (1989) — the dependency-graph Poisson approximation; LEDGER #61–#62.
