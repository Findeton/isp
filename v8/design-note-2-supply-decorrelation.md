# Design note 2: mechanisms for supply decorrelation — paper 13's named target

**Status:** design document, 2026-07-02. Think-first, no code. Paper 13 proved the relocation (Theorem 2.1: the 2D manifoldlikeness gate *is* a condition on the joint (commit, supply) statistics) and measured the obstruction (natural supplies carry clock correlation Spearman `+0.42…+0.78` vs the faithful `≈ 0.04`; every natural family fails the volume layer, best case `3.4×` the pooled band). This note designs the mechanism search: what could *physically* erase the clock correlation, what each candidate predicts, and the experiment that separates them — including the control that decides whether the 2D route closes.

## 1. The target, made quantitative

The faithful cell, read off paper 13's own measurements, has three nested requirements on a two-clock configuration (`b` = commit rank, `χ` = supply rank):

- **T1 (necessary, cheap):** rank–rank Spearman(`b`, `χ`) `≲ 0.1` fleet-wide — chains must cross and interleave diffusively, not persist as rays/staircases.
- **T2 (the volume layer):** `D*`(rank embedding) within the pooled same-`N` faithful band (`0.0263 ± 0.0047` at `N = 512`).
- **T3 (the statistical layer):** ensemble-calibrated dispersion consistent with the sprinkling ensemble (the layer that killed the best natural family at `z = 12`, and the jittered lattice at `z = 5.2`).

T1 without T2 is possible (decorrelation ≠ cell membership — paper 13 is explicit that erasing the correlation is necessary, not sufficient); the design below therefore always measures all three, in order, and reports where each candidate dies.

**Why natural supplies fail, mechanically.** Both clocks grow with time; any per-chain rate persistence turns a chain's `(b, χ)` path into a ray of slope ≈ its rate. The sweep's own deconfounding control says most of the available "natural" relief is mechanical interleaving from more, shorter chains (`0.163 → 0.102` from `M = 32 → 128`), not increment statistics (`Lévy: 0.102 → 0.097`). So the mechanism must attack *persistence itself*, not the increment law's tails.

## 2. The martingale criterion (the design's organizing idea)

A sprinkling's chains are diffusive in rank–rank space: a chain's content history behaves like a random walk with **no chain-identity drift** — conditional on the past, no chain is durably faster. Formalized as the design target: per-chain cumulative content `χ_c(b)` should be (approximately) a **martingale relative to the fleet average** — increments exchangeable *across* chains at each commit epoch, with per-chain rate autocorrelation time `τ` short compared to chain length `L`. The natural families fail exactly this: static heterogeneous rates have `τ = ∞`; wandering log-rates have `τ` of order the walk's own persistence; homogeneous renewal has exchangeable increments but *within-chain* diagonality plus Poisson chain-length dispersion still leaves ray geometry at `M = 32` (measured: `6.2×`).

Three physical mechanisms plausibly deliver short `τ`, and they make different, separable predictions:

**(M1) Supply–commit feedback (capacity-mediated mean reversion).** Paper 1's sub-capacity firing law (§4.3) is a ready-made negative feedback: content accumulation presses against the capacity ceiling, suppressing the effective rate of chains that have recently committed rich content. Model class: rate `r_c ∝ exp(−γ · (χ_c − χ̄))` with gain `γ`. Predictions: Spearman decreasing in `γ` with a *finite optimal* `γ*` (overdamping oscillates chains around the mean — anti-persistent staircases are also non-diffusive); dispersion (T3) should approach the ensemble *from above*. Physical reading in paper 1 §4.4's ledger: this is configuration feedback, not a new law — it lives in the [PHYSICAL] supply slot and needs no new posits.

**(M2) Branching/merging chain topology.** The disjoint-chain fleet is paper 13's modeling simplification; real record webs are DAGs. Merging pools content histories (a merged chain inherits a mixture — drift averages out); branching resets chain identity. Persistence dies at the branching rate: `τ ≈ 1/μ` for merge-branch rate `μ`. Predictions: Spearman decreasing in `μ` *without tuning any rate law* (the increments can stay iid — topology alone does the work); chain-length distribution shifts toward the sprinkling's (this is measurable and is *not* predicted by M1); at large `μ` the configuration must degrade differently — toward the interleaving floor, not toward staircases. If M2 reaches T1 at `μ` values comparable to a sprinkling's own chain-decomposition churn, the conclusion is the strong one: *decorrelation is automatic for web-shaped supplies, and the ray pathology was an artifact of the disjoint-chain idealization.*

**(M3) Non-renewal anti-correlated increments (bare mean reversion).** M1 without the capacity story: AR(1) log-rates with negative correlation, `τ` set directly. This is the *ablation* of M1 — same statistics, no physical mechanism — included to decide whether anything is gained by the capacity reading beyond curve-fitting (if M1 at its physical parameterization does no better than M3 tuned to the same `τ`, the capacity story adds nothing measurable and must not be claimed).

## 3. The decisive control: the exchangeable ceiling

Before any mechanism is credited or blamed, run the **oracle supply**: increments drawn exchangeably across the whole fleet at each epoch (τ = 0 by construction, the best any identity-blind mechanism can do). Its role is asymmetric and it is the single most informative run in the design:

- If the exchangeable ceiling **passes T1 but fails T2/T3**, then *no* decorrelation mechanism of this type can ever reach the cell — the failure is not persistence but something the two-clock frame itself is missing at these regimes — and paper 13's stated risk fires: the 2D kinematic route closes, and the program redirects to `d ≥ 3` (where papers 14–15 now stand ready, which is precisely why this control is affordable to run *now*).
- If it **passes T1 + T2**, the target is reachable and the mechanism race (M1/M2/M3) is meaningful; the winner is whichever reaches the band at a physically defensible parameter value, judged also on its T3 behavior.
- Anything the mechanisms do must be benchmarked as *fraction of the ceiling's gap closed*, not raw ratios — the sweep's `3.4×`-vs-band numbers taught that raw ratios flatter interleaving effects.

## 4. Experiment design

One receipt, one sweep grid, all comparisons within-seed: fleet sizes `M ∈ {32, 128}`, `N = 512` (the paper 13 conventions, so every number lands on the existing band), plus one `N = 1024` row for the winner (the `m1` scale-lesson convention). Arms: A/B/C reruns as anchors (the paper 13 families), M1 over `γ` (5 points, log-spaced around the capacity-derived estimate), M2 over `μ` (5 points), M3 over `τ` matched to M1's realized autocorrelation times, and the exchangeable ceiling. Measured per arm: Spearman (T1), `D*` ratio to the pooled band (T2), dispersion `z` (T3), plus two mechanism fingerprints — chain-length distribution distance to the sprinkling's (separates M2) and the staircase statistic (runs-test on per-chain increment signs; separates overdamped M1/M3). Gates: T1 `< 0.1`; T2 within `2σ` of the band; T3 `|z| < 3`; fingerprints reported, not gated. Verdicts per paper 13's vocabulary, UNDECIDED allowed and disclosed.

## 5. What each outcome means upstream

- **Any arm reaches T1+T2+T3:** paper 13's necessary condition is shown *achievable by a mechanism*; the two-clock route to "records measure positive in 2D" reopens with a named supply class, and design note 1's L3 rung unblocks (it consumes exactly this supply). The spacing-ledger connection is then live: the winning mechanism's parameter is new [PHYSICAL] configuration data in paper 1 §4.4's slot, and its physical derivation becomes the next open.
- **Ceiling passes, all mechanisms stall short:** the target is real but the tested mechanism classes are too weak — the honest report is the measured gap ordering, and the next design iterates on topology (M2 variants) first, since it is the least tuned.
- **Ceiling fails T2:** the 2D kinematic route closes at these regimes (the strongest result in this note's range — a clean, receipted negative that converts paper 13's "stated risk" into a measured verdict), and the program's manifoldlikeness weight shifts fully onto the `d ≥ 3` tomography line.

## 6. Receipts plan (names reserved, not written)

`j3_decorrelation_mechanisms.py` — the §4 grid, anchors first, ceiling before mechanisms, fingerprints logged; `j4_winner_scale.py` — the winner (if any) at `N = 1024` plus the paper 12 full pipeline end-to-end. Conventions: `default_rng(20260702)`, pooled-band comparisons at matched `N`, all gates as fixed in §4. As with design note 1, the gates are quoted here so the receipts assert against the design.
