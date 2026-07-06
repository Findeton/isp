# n3-derived — the must-fail leg: T6.4's outstanding void, on the genuinely derived field

**Status:** design note, 2026-07-06 (v9 round 16; the round-15 review's MINOR-6/7 — the must-fail correlated-supply control's home is a field where a supply channel EXISTS; ml2's Hasse-GFF field is a web functional, so it binds here). Receipt: `v9/code/n3_derived_must_fail.py` (gates pinned here, committed pre-receipt). Grade: **[DEMONSTRATED given the toy derived field — rung-2 grade]**; the ml3b matter field at fleet scale is the eventual upgrade.

## 1. The design

ml2's construction verbatim (web (2048, 32, 16); chains = segments ≥ 8; the derived field = Hasse-mediated GFF exact cross-chain covariance; the target = the web's OWN two-clock chain positions — no planted anything), run at **6 seeds** (20260728–33), with the two review-prescribed instruments:

- **The must-fail surrogate:** χ̃_AB built from supply observables ONLY — the normalized outer product of the chains' mean accumulated-content levels plus a birth-time affinity term (`χ̃_ij = norm(level_i·level_j) + norm(exp(−|birth_i − birth_j|/τ))`, τ = N/4, equal weights). This field carries nothing but the web's bookkeeping; **the pipeline must reject it.**
- **The max-statistic confound calibration** (replacing the ~48%-family-chance-void per-pair form): per seed, the max over axis-pairs of |corr(XY, supply var)| compared against the 95th percentile of a 24-permutation null of the same max-statistic.

## 2. Pinned gates (per seed over 6 seeds)

- **Gn1 (closure, the derived field):** Procrustes(MDS(χ_AB^derived), own two-clock positions) ≥ 0.70 on ≥ 5/6 seeds — **the band is pinned NON-BLIND** (ml2's known 3-seed spread 0.743–0.919 with the 0.85 pin refusing 1/2 off-seeds; disclosed).
- **Gn2 (THE MUST-FAIL, T6.4's outstanding void):** (a) the supply-only surrogate's closure falls below (shuffle-null mean + 3 null-sd) on **6/6 seeds** — the pipeline visibly rejects supply-only fields; (b) the supply-partialled residual field (χ_AB regressed on the surrogate's feature columns, residual re-symmetrized) retains ≥ 0.85× the raw closure on ≥ 5/6 seeds — the derived field's geometry does not ride the supply channel (ml2's size-residual form, generalized).
- **Gn3 (the calibrated confound):** the derived field's max-statistic below its permutation-null 95th percentile on ≥ 5/6 seeds; a firing seed is adjudicated by Gn2(b) (supply-partialled closure retained ⇒ benign shared geometry, recorded; not retained ⇒ that seed VOID).
- **T6.4 semantics, pinned:** Gn1 ∧ Gn2(a,b) ∧ Gn3-or-benign ⇒ **the must-fail void is DISCHARGED and T6.4 is fully met at rung-2 grade**; Gn2(a) refusing ⇒ the pipeline cannot distinguish geometry from bookkeeping — T6.4 refused at the void, the readout line redesigns (the honest outcome).

## References

ml2 (`ml2_derived_field_web.py` — the construction verbatim; the size-residual void this generalizes); note-n3-full §4 (MINOR-6/7 — the placebo finding and the outstanding-void status); PLAN T6.4 (the amended gate's named must-fail control); the round-15 review; LEDGER #66.
