# T2.1 — the pair-budget law of the corner's dispersion excess, and the y1 retest

**Status:** derivation note + pre-registration, 2026-07-05 (PLAN.md T2.1; round 2). Gates pinned here before `y1` ran. Receipt: `v9/code/y1_d1_family_retest.py` (5/5). **[EXECUTED same-date. P1 REFUTED-as-stated in the pre-registered second branch: the D1 cure at N = 512 is significant (z-difference +2.28 vs 2 SE 1.95 — knife-edge, stated) and EXCEEDS the pair-budget prediction (nominal ratio 6.85 vs 1.88; the ratio is [ill-conditioned at this power] — its denominator is consistent with zero — so the load-bearing statement is the z-difference); the lifetime tail suppresses dispersion superlinearly in the pair count; exponent unresolved; mechanism hunt named. P2 HELD-as-gated: no RESOLVABLE N-trend at K = 12 for either law (uniform +59.5%/+28.1%, D1 +8.7%/+22.1% at 512/2048, differences within 2 SE; a ≤2× decline remains unexcluded at this power — stated symmetrically with P1's unresolved-at-2048 clause). P3: D1-continuous 1.12× and D1+atoms 1.04× at N = 2048 both CERTIFIED-IN-BAND at Δ = 2σ_b, K = 12 — paper 17's directional 0.96× headline de-asterisked. P4 REFUTED: no monotone N-trend for the strict corner (1.21×/1.33×/1.23×, all certified-or-adjacent) — the transient story over-generalized the uniform-kernel split; u1's 1.60× was stream scatter. Budgets measured: uniform 1.90/commit (Geometric{0,1,…}-class, cv² 1.44) vs D1 1.01 (Geometric{1,…}-dispersion class, cv² 0.52 — far from the deterministic endpoint cv² = 0); dispersion-monotonicity of the budget confirmed directionally; the ≈2 coincidence with the Lemma's geometric-vs-deterministic factor is an L = 2 artifact (L/(L−1) = 2), not a confirmation of that endpoint. D1-continuous's 1σ sensitivity read BAND-ADJACENT beside its 2σ CERTIFIED, carried here.]**

## 1. The law, derived

**Setting.** The churn web at the corner (`L`, `M`, continuous content), scored by the per-draw interval-count dispersion (the `j1`/fano convention). Paper 16/17 measured a mean-level dispersion *excess* over the sprinkling ensemble at every scale, with its cross-scale trend unresolved at power (three pooled-calibration streams); `u3` measured that concentrating the lifetime law cures most of it. The claim to derive: *what property of the placement law sets the excess?*

**Lemma (the same-lineage pair budget).** For a victim law with realized per-lineage own-commit lifetime law `g` (mean `L̄`), the expected number of same-lineage pairs in an `N`-commit web is

> `E[SL] = (N/E[g]) · E[g(g−1)]/2`

(lineage arrivals at rate `N/E[g]`; each completed lineage contributes `C(g, 2)` pairs; edge terms `O(L̄M/N)` as in paper 16 Thm A). For geometric lifetimes of mean `L`: `E[g(g−1)] = 2L(L−1)`, recovering paper 16's `E[SL] = N(L−1)`; for a deterministic lifetime `g ≡ L`: `E[g(g−1)] = L(L−1)` — **half the geometric budget at equal mean**. At fixed mean, `E[g(g−1)] = L̄²(1 + cv²[g]) − L̄` is strictly increasing in the lifetime law's dispersion — the tail drives the budget.

**The law [DERIVED at leading order; the receipt measures its constant].** Same-lineage pairs are the correlated ones (both clocks strictly co-monotone along a lineage — paper 16 Thm A(i)); distinct-slot cross pairs are sign-balanced, and the same-slot O(L/N) bias (paper 16 Thm A(ii-b)) is subleading at this order. The interval-count over-dispersion is driven, at leading order in the renewal fraction, by the same-lineage pair density, so at fixed `(L̄, M, N)`:

> `mean-level dispersion excess ∝ E[SL]/N = E[g(g−1)]/(2·E[g])` — **the pair budget per commit**,

with two consequences pre-registered as `y1`'s predictions:

- **P1 (the cure ratio).** Across victim laws at fixed mean, `excess(F)/excess(F′) = budget(F)/budget(F′)` — for uniform-victim (geometric-class) vs D1 kill-the-oldest (concentrated), the predicted ratio is the *measured* lifetime-law budget ratio (from `u3`'s lifetime moments, ≈ 1.6; exactly 2 for perfect concentration). Gate: measured excess ratio within `×1.6` of the measured budget ratio, both scales. Both directions live: a cure ratio far *above* the budget ratio would say the tail acts through more than the pair count.
- **P2 (N-flatness — the staircase dissolved).** The budget per commit is `N`-free at fixed law, so the mean-level excess is **flat in `N`** — the memo's "finite-`N` staircase" should dissolve into an `N`-flat excess once measured at power (consistent with all three unresolved streams). Gate: `512` vs `2048` standardized excesses within `2 SE` per law. A confirmed `N`-trend would refute this law's leading order.

**Scope.** Leading order in `L̄M/N`; the constant in `∝` is named-measured (the receipt prints it per scale); nothing here claims the *per-draw* z-layer convention changes.

## 2. The rest of the retest (pre-registered)

- **P3 (the D1 certifications, `Δ = 2σ_b`, `K = 12` — full power at this margin).** D1-continuous and D1+atoms (synthetic 128-menu) at `N = 2048`: expected CERTIFIED-or-ADJACENT; a REFUSED verdict demotes paper 17's `0.96×` headline honestly. Both content readings run, per the registration paper 17 §9 item 6 left owed.
- **P4 (the strict corner's volume face — the `N`-dependence paper 17 §3 owes).** Strict-j3 corner at `N ∈ {512, 1024, 2048}`, `K = 12` each, powered verdicts; prediction (from `q2` CHECK 5's fresh-vs-warm split): the ratio-to-band declines with `N` toward band (transient-dominated), REFUSED at `512` and ADJACENT-or-better at `2048`.

Conventions: `q2`'s TOST semantics (`Δ = 2σ_b`, `1σ` sensitivity printed); one pooled 64-draw fano calibration per scale (the #37 lesson); seeds `default_rng(20260706)` (the round-2 stream), disclosed; float64 landscapes.

## References

Paper 16 Thm A (the SL accounting; the correlated-pair mechanism); paper 17 §6 (the withdrawn staircase reading; the D1 cure at [directional]); `u3` (the lifetime moments this note's P1 consumes); `q2` (the semantics; the three unresolved streams; the fresh-vs-warm split behind P4); PLAN.md T2.1; `j1` (the fano convention).
