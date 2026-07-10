# 3p1-lorentz1 — Lorentz I: the directional anisotropy instrument (web-vs-web)

**Status:** design note, 2026-07-09 (v9 round 36). Receipt: `v9/code/dimwall_lorentz1.py` (pinned here, committed strictly before the receipt). Reviews ON.

## 1. The unlock

The r26/r27 voids proved cone shape invisible to ISOTROPIC statistics; the shelf's direction-resolved instruments were never pointed at grown webs; and the mixing question needs no cross-family calibration — it is web-vs-web. This receipt builds the ensemble-powered directional instrument paper 6 SS6(i) names.

## 2. The instrument

Per instance: sample related pairs (interval size >= 6); standardize coordinates (zero-mean unit-var per component within the instance — a diagonal affine, pinned); decompose the displacement along the family's causal axis d-hat (dominance families: the diagonal; M4: the t-axis) into (s, r); compute the longest chain ell(x, y) by DP over the induced interval. Fit log ell against log T for two clocks:
- **T_round = sqrt(max(s^2 - r^2, 0))** (the hyperboloid/proper-time clock);
- **T_poly = (prod_i max(u_i, eps))^{1/(C+1)}** with u = the displacement in the family's orthant frame (dominance: native clock coordinates; M4: the symmetric Hadamard 4-frame, components clamped at eps = 0.05 — if unfair, Gl0 voids).
**G = R2_round − R2_poly** per instance; positive = round-preferring.

## 3. Pinned gates (windows Delta = 1024 central, N = 256 subsamples, pairs <= 300/instance; seeds 20261900+; 5 per family)

- **Gl0 (certification — the first directional separation gate):** G(M4, own coordinates) > +0.05 on 5/5 AND G(orthant-iid k = 4) < −0.05 on 5/5. REFUSED => VOID-INSTRUMENT (named; the T_poly-on-M4 frame is the suspect).
- **Gl1 (the baseline; registered [directional]: polyhedral):** G(corner C = 3 webs) measured with seed band; expected < 0.
- **Gl2 (THE MIXING QUESTION; [directional]):** mean G(kdir C = 3 webs) > mean G(corner) — channel mixing moves the effective cone toward round. Either outcome is decisive: movement => Lorentzization-by-mixing lives (Phase 2b tunes toward the round limit); no movement => the finite-C polyhedral anisotropy stands as the framework's falsifiable PREDICTION, and the Lorentz-test fork (round the cone or face the bounds) is squarely posed.
- **INFO:** per-family theta exponents and R2 tables; s/r profile summaries; pair counts.

## 4. Scope

First directional measurement; one clock-pair (round vs box); the exponent-fit form is the coarsest direction-sensitive functional — a Gl0 pass certifies it suffices for the round-vs-orthant split, nothing more. Anchors at matched window N; the M4 Hadamard frame is a pinned construction whose fairness the certification gate itself adjudicates.

## References

The round-35 strategic sweep (LOG r36 open); paper 14 Thm 2.1 (shadow-per-direction — the shelf); note-3p1-dimension-ledger SSR-A (the registered anisotropy prediction); paper 6 SS6(i); LEDGER #85/#86 (the isotropic voids).
