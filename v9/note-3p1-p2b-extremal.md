# 3p1-p2b — Phase 2-II: the extremal-statistics cone discriminator

**Status:** design note, 2026-07-06 (v9 round 27). Receipt: `v9/code/dimwall_phase2b.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE on record.**

## 1. The instrument (post-void redesign)

Round 26 measured chain MOMENTS cone-blind. Attempt II uses extremal order statistics from one Mirsky peeling per instance: **H** = height (= number of layers) and **W** = max layer size (the width proxy — pinned as-is). Both are affine-invariant order invariants; extremal statistics are N-dependent, so every instance runs at **matched N = 768** (webs enter via induced 768-subsamples, two draws per seed, averaged). The comparison machinery is round 26's verbatim with (log H, log W) as the locus coordinates: reference families = round M^{2,3,4} and orthant k = 3, 4, 5 (10 seeds each), matched at the web's s2 by log-interpolation along the family parameter, log-space distances d_round / d_orthant. The d = 2 anchor (M2 = orthant-2 exactly) is printed as wiring.

## 2. Pinned gates (webs = the Phase-1b class, C = 3, per-channel churn; corner = one-hot alpha 0.75; kdir = Dirichlet slot directions; seeds 20260870+)

- **Gx0 (separation certification, FIRST):** matched round-vs-orthant (log H, log W) loci differ by > 3x the pooled seed-sd, per component, across the webs' s2 range. REFUSED => **VOID-INSTRUMENT-II** — and the named pivot: cone shape is invisible to counting AND extremal order statistics at this N; Phase 2 moves to directional/embedding instruments (the tomography machinery adapted), a fresh design.
- **Gx1 (baseline, registered):** corner webs nearer the ORTHANT locus on >= 4/5 seeds.
- **Gx2 (mixing, [directional]):** the K-direction webs' mean d_round < the corner webs' mean d_round.
- **Gx3 (retention):** K-direction webs keep 2-realizer refusals >= 4/5 (144-subposets) and full-web d_MM >= 3.0.
- **INFO:** the (s2, H, W) table for all families and webs; the layer-profile peak fraction; both distances per seed; the d = 2 anchor coincidence.
- **Verdicts:** as round 26 — MIXING-ROUNDS / POLYHEDRAL-RIGID / MEASURE-DOMINATED / VOID-INSTRUMENT-II. Exit 1 by design on refusal.

## 3. Scope

No hostile review (mode). H and W at one N are the coarsest extremal pair; a second void is a real possibility and would itself be the finding (the discrimination then provably needs directional data). The K-direction variant carries over from round 26 unread.

## References

note-3p1-p2 (+ the r26 void and banked tables); note-3p1-p1b (the web classes); PLAN SS-the-3+1-program; LEDGER #85.
