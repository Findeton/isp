# 3p1-p2d — the time-window diagnosis: is the web a time-cylinder?

**Status:** design note, 2026-07-06 (v9 round 29). Receipt: `v9/code/dimwall_phase2d.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE on record; token-lean, one design only.**

## 1. The hypothesis and the test

Round 28: the tall-narrow anomaly is measure-intrinsic. The cylinder hypothesis: stationary chi-marginals x unbounded b = a time-cylinder measure; references are diamonds/cubes. Prediction: inside b-windows of width ~ the chi-correlation time the web joins the uniform-causality locus, and the anomaly grows with window length. The principled window scale: a slot-channel resets w.p. 1/(L*M) per step => tau ~ L*M = 512; **Delta* = 512 pinned.** Central windows (start = (N - Delta)/2), subsampled to matched N = 128; sweep Delta in {128, 256, 512, 1024, 2048}.

## 2. Pinned gates (webs = the pinned class, C = 3 corner alpha 0.75 per-channel churn; seeds 20260960+; orthant refs k = 3, 4, 5 at N = 128, 8 seeds; z = max-component |log obs - log matched|/pooled rel-sd)

- **Gt1 (the cylinder signature):** z(Delta = 2048) > z(Delta* = 512) on >= 4/5 seeds.
- **Gt2 (the joining):** z(Delta*) <= 3 on >= 4/5 seeds.
- **Gt3 (in-window dimension):** windowed d_MM(Delta*) >= 3.2 (seed mean) AND 2-realizer refuses the Delta*-window subsamples on >= 4/5 seeds.
- **INFO:** the full Delta-sweep table (s2, H, W, z, d_MM); a C = 2 spot row at Delta*.
- **Verdicts:** all => **CYLINDER-CONFIRMED** (Phase 3 reconstructs on Delta* windows); Gt1 + sweep-joining at another Delta => **BAND-SHIFTED** (the scale argument off, the phenomenon real); Gt2 fails at every Delta => **CYLINDER-REFUTED** (the anomaly is deeper than the measure's shape). Exit 1 by design on refusal.

## References

note-3p1-p2c (+ r28: the refusal and the hypothesis); r27's tall-narrow tables; PLAN SS-the-3+1-program; LEDGER #87.
