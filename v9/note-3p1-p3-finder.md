# 3p1-p3 — the window-aware finder: the first reconstruction score on a grown web

**Status:** design note, 2026-07-06 (v9 round 32, batch item ii). Receipt: `v9/code/dimwall_finder.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE on record.**

## The pipeline (order-only, m1-B seed form at d = 3)

Windowed C = 2 webs (pinned class, Delta = 512 central, N = 128): t-hat(x) = |past(x)|^{1/3} − |future(x)|^{1/3} (window-relative pasts/futures); transverse (x1, x2) = classical MDS (2 components) on D_ij = 1 − |past_i ∩ past_j|/sqrt(|past_i||past_j|); the certificate = **cone-fit balanced accuracy**: predict related iff dt > rho·|dx| with rho maximizing balanced accuracy in-sample (identical procedure per family; baseline 0.5).

## Pinned gates (seeds 20261200+; 5 per family)

- **Gp1 (positive control):** M3 diamond sprinklings (N = 128) mean balanced accuracy >= 0.85 — the pipeline reads genuine 2+1 order-only.
- **Gp2 (discrimination):** the chi-permuted null (each channel column independently permuted across the window's events — marginals kept, causal consistency destroyed) sits >= 0.10 below the web's mean accuracy. REFUSED => VOID (the certificate does not discriminate).
- **Gp3 (THE MEASUREMENT, [directional]):** the C = 2 webs' balanced accuracy quoted against both yardsticks; registered: null + 0.10 <= web <= M3 (the anomaly predicts sub-sprinkling); web >= M3 − 0.03 flags MANIFOLDLIKE-GRADE (would warrant escalation).
- **INFO:** per-seed scores; rho values; the t-hat/b rank correlation (how much of the reconstruction is just the time order).

## References

m1 (the intrinsic-finder seed form; the scout r17); r29/r30 (the windowed instrument + dim = C + 1); the r27 anomaly (why sub-sprinkling is the registered direction); LEDGER #86–#90.
