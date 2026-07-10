# 3p1-p4 — the extremal-anomaly characterization

**Status:** design note, 2026-07-06 (committed 2026-07-09) (v9 round 33, batch item iii). Receipt: `v9/code/dimwall_anomaly.py` (pinned strictly before). **NO-REVIEW MODE.**

Measure H(N), W(N) (one Mirsky peeling) at N in {96, 128, 192, 256, 384} for: windowed C = 3 pinned-class webs (Delta = 1024 central, subsampled), orthant k = 4 iid, round M4 (5 seeds each). Fit log-log slopes a_H, a_W per family.

- **Ga1 (reference sanity):** both reference families' a_H in [0.18, 0.32] and a_W in [0.65, 0.85].
- **Ga2 (the classification, registered directional = EXPONENT-CLASS):** webs' a_H > 0.32 => EXPONENT-CLASS (the tall profile is a different scaling LAW); else if H-ratio to orthant > 1.5 at every N => OFFSET-CLASS (same law, bigger constant); else ANOMALY-DISSOLVES-AT-SCALE (it was a small-N artifact — also a finding).
- **INFO:** the full tables; the W side; the signature sentence drafted from the measured class.

## References
r27/r29 (the tall-narrow finding, its scale-free persistence); LEDGER #86–#88.
