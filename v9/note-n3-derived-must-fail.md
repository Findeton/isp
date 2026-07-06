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

## 3. The refusal ledger and the diagnosis (2026-07-06; the run frozen pre-analysis)

**Gn1 HELD (closure 0.871–0.942, 6/6) — everything else REFUSED, and the refusal is the leg's finding:**

- **Gn2a — the must-fail control fired on its first real outing:** the supply-only surrogate closes the "own geometry" at **0.713–0.797** on every seed (null 0.10–0.14). The pipeline does NOT reject bookkeeping-only fields *in this design*.
- **Gn3:** the derived field's recovered coordinates correlate with supply observables at max-statistic 0.86–0.92 vs null 95th ≈ 0.22–0.30 — on every seed. **Gn2b:** residual retention 0.71–0.90× (4/6 above the 0.85 line) — not benign.

**The diagnosis (design-level, not instrumental):** the own-geometry target — each chain's mean two-clock rank position — is **built from (mean commit rank, mean content rank) ≈ (birth time, content level): the target IS a supply readout.** A field carrying only bookkeeping closes it because the bookkeeping and the target are nearly the same object. This is the round-4 review's M6 caveat ("probe and target are functionals of the same committed (b, χ)") materialized as a gate refusal — the rung-2 *own-geometry* form cannot, even in principle, distinguish "the field carries geometry" from "the field carries the web's bookkeeping", because in this design the geometry IS the bookkeeping's shadow.

**Per the pinned kill semantics (§2, verbatim): "Gn2(a) refusing ⇒ the pipeline cannot distinguish geometry from bookkeeping — T6.4 refused at the void, and the readout line redesigns."** T6.4 therefore stands: **L2 conjunct certified (Tier-A legs); the must-fail void REFUSED on the own-geometry derived leg; the gate NOT met — and now for a measured reason, not a paper-trail gap.** No amendment: the branch fired as pre-agreed.

**What the redesign requires (named for the next leg, not begun here):** a target that is *not derivable from supply observables* — neither planted (the Tier-A legs' limitation: the web contributes only the roster) nor the two-clock positions (this leg's: supply-aligned). The corpus already owns the candidate instrument class: the **tomography line's invariants** (papers 14–15 — celestial structure, reconstruction certificates), which are functions of the *causal pattern across many sheets*, not of per-chain bookkeeping. The genuinely binding 3+1 test: **ml3b's matter-derived field at fleet scale, scored against tomographic invariants** — both halves now have their first pieces (the step-(b) correlator exists and decays; the tomography certificates run at pilot scale).

**Retro-scope on ml2 (recorded, to be reviewed):** rung 2's "the derived field reads out the web's own two-clock geometry" survives as a *measurement* (it does close it) but its **evidential weight is demoted**: closing a supply-aligned target is necessary, not probative — the ml2 size-residual void tested one supply feature (size); this leg's two-feature surrogate (level × birth) closes the target nearly as well as the field does. The demotion notice belongs in the ml2 record (LEDGER row; the note stands as history).

## References

ml2 (`ml2_derived_field_web.py` — the construction verbatim; the size-residual void this generalizes); note-n3-full §4 (MINOR-6/7 — the placebo finding and the outstanding-void status); PLAN T6.4 (the amended gate's named must-fail control); the round-15 review; LEDGER #66.
