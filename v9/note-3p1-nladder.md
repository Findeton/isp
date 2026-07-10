# 3p1-nladder — round 46: does the frontier converge with scale? (NO-REVIEW MODE, on record)

**Status:** design note, 2026-07-10 (v9 round 46). Receipt: `v9/code/dimwall_nladder.py` (pinned here, committed strictly before running). NO-REVIEW MODE (user, token-constrained): the wiring gate to 45e and exit-1 discipline are the compensating controls; findings are graded [MEASURED, unreviewed].

## 1. The question and the design

45e closed at: F-gap ≈ +0.06–0.09 above the same-pipeline round band, d_ball = 3.84, at N = 2048. The convergence question: gap(N) and d_ball(N) for N ∈ {2048, 8192, 32768}, everything scale-covariant — window = the central N/2, calibration segment = the first N/4 (split-sample τ), NW = 256 (F) / 128 (volume) fixed subsamples, the P0 class verbatim (K = 24, α = 0.75, c = 0.5, dipole kernel, full-vector churn). **The reference lines are rebuilt AT EACH N** (10 confetti seeds per rung per convention; the volume references d = 2..6 at 6 seeds per rung) — so each rung's gap is same-size-calibrated, exactly as 45e. 10 web seeds per rung. **The churn axis (INFO): one row at N = 8192 with L = 64** (slower churn = longer ballistic segments = the reset-teleport suspect diluted).

## 2. The influence theorem (analysis, recorded here; no receipt needed)

The wb-line content dynamics is FREE: deposits are slot-local, churn destroys (resets to zero, no transfer), and the commit/victim choices are exogenous randomness. Hence a localized perturbation of one slot's content at t* alters ONLY that slot's subsequent snapshots: the influence set is a single worldline; no disturbance ever propagates across slots; no collective excitation exists at any scale. **Corollary: the user's "sound" picture of matter requires slot coupling — absent from every builder in the corpus.** Minimal record-native coupling, named for the next builder round: CONSERVATION-CHURN (the reset transfers the victim's content to a receiver slot — content conserved, interactions nonlocal-in-fleet, and the reset-teleport residual suspect simultaneously removed). The influence-cone receipt (the bridge machinery) becomes meaningful only on a coupled builder.

## 3. Pinned gates (exit 1 on G0 only; the trend is a read)

- **G0 (wiring):** the N = 2048 rung runs 45e's exact seeds (20263000+) and must reproduce P0's numbers (F_dom 1.298, F_m4 1.237, d_ball 3.84 at 2 d.p.).
- **G1 [MEASURED, unreviewed]:** per rung: web F (both conventions, 10 seeds, SE), the rung's confetti lines, gap(N) per convention, d_ball(N) on the rung's own volume reference, in-window refusals, S₄ on a 1024-node window subsample (disclosed: full-web witness search is memory-infeasible at 32k).
- **G2 (the trend; a read):** per convention: SHRINKS (gap(32k) ≤ gap(2k) − 2·pooled SE) / GROWS (the mirror) / PERSISTS (else). The physics conclusions attach to the convention-STABLE reading only.
- Fresh seeds: webs 20263300+ (8k), 20263400+ (32k); confetti 20263500+; volume refs 20263600+.

## References

45e (the protocol and the frozen comparison logic, reused verbatim); the arc review O1/O2; the particle reframe (note-3p1-manifoldweb, final section); round-42's scale leg (the old class's PERSISTS — not transferable, the caution precedent).
