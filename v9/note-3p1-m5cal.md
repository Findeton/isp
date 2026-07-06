# 3p1-m5cal — the M5-extended calibration for the windowed d = C+1 finding

**Status:** design note, 2026-07-06 (v9 round 30, menu item i). Receipt: `v9/code/dimwall_m5cal.py` (pinned here, committed strictly before the receipt). **The reserved review fires on green — the standing d ~ 4 rule; grading withheld until it returns.**

## Pinned gates

- **Gm5-0 (the curve extends):** measured M5 diamond fraction sits below M4's by > 3x the pooled seed-sd (N = 512, 8 seeds; rejection sampling in the 4-spatial-ball diamond).
- **Gm5-1 (the re-read):** windowed d_MM(C = 3, Delta = 512, central, 5 seeds, matched N = 128 subsamples) lands in **[3.7, 4.3] by INTERPOLATION** on the extended curve (M2..M5).
- **Gm5-2 (the in-window ladder):** windowed d_MM strictly monotone over C = 1, 2, 3 with C = 2 in [2.8, 3.5].
- **INFO:** the orthant-scale reading (effective clock count via the measured 2^-C family); the per-Delta table re-read on the extended curve; the analytic anchors printed (M2 ~ 1/2; orthant k anchors ~ 2^{1-k}).

## The review brief (fires on green)

Attack the finding "multi-channel record webs read d = C + 1 in time-windows": independent web rebuild + instrument verification (anchors), window-position sweep (central was pinned — is position load-bearing?), the sparsity confound (the pair-defense: any sparse-but-low-dim control reads high d_MM but PASSES the 2-realizer; the finding requires BOTH dials), the calibration-edge issue (now interpolated), and the C-ladder's tracking (the reading follows C, not mere sparsity). Verdicts: CONFIRMED / NARROWED / REFUTED; grading per the outcome.

## References

r29 (`dimwall_phase2d.py` + LEDGER #88 — the banked finding and its disclosure); the Phase-0 instruments; PLAN SS-the-3+1-program (the reserved-review rule).
