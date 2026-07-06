# s7 — the stage-priced growth test ("arm C"): Row C's target replaced by the faithful stage profile ρ(t); gates pinned pre-run

**Status:** design note, 2026-07-05 (v9 round 8; the round-7 review's surviving derivation-shaped candidate — LEDGER #50 item 3, LOG round-7 review entry). Receipt: `v9/code/s7_stage_priced.py`. Everything below is pinned BEFORE the receipt runs.

## 1. The candidate, and why it is the last of its kind

The round-7 review established on the committed stream (s6b): the increment-argmin rejects the true move because **Row C's endpoint target ½ is wrong along the whole faithful transient** — the u+v prefix runs at comparability ρ ≈ ⅓, so the block increment carries gradient 2(r_t − ½) ≈ −⅓ and pays the argmin to take the biggest candidate at 93.8% of decisions; the per-pair family (arms A/B and everything |D|-linear, including per-step-tuned oracles) is closed at ≤ 7.7% ≈ chance. Arm C attacks the binding term:

**S̃_comp(nrel, n; stage t) = (n(n−1)/2) · (r − ρ(t))²**, with ρ(t) the faithful prefix expectation of the comparability rate at stage t. The growth action is Row A (unchanged) + the stage-priced block increment [S̃_comp(nrel+|D|, t+1; t+1) − S̃_comp(nrel, t; t)] — each stage scored against its own stage's target.

Three properties, stated in advance:
- **The endpoint functional is untouched.** ρ(N) = ½ (up to calibration error, printed), so at completion S̃_comp = S_comp up to the printed calibration error (run value: ρ(N) = 0.4904 vs ½ — walls robust to the shift; the round-8 review, NIT-7): the GRADER and its wall/floor theorems are unchanged up to that disclosed error. Arm C re-prices the *path*, not the judge. No wall arithmetic is owed (contrast note-s6 §3).
- **It is derived, not tuned.** ρ(t) is a computable property of faithful growth under the registered arrival order. The receipt calibrates it (4 oracle profiles, mean-of-rates per stage, edge-normalized window-15 smoothing per the s6 lesson; CALIBRATED grade), and the flat regime is DERIVED exactly in §2 — the calibration must reproduce it (a pinned consistency check, not a free fit).
- **It is the endgame of the re-pricing program.** The per-pair/|D|-linear family is measured closed (s6b M2–M4); the global term is the only remaining lever with a derivation-shaped stage target. If arm C fails G1, increment-optimization is closed, full stop, and paper 3 records the division of labor as final: the action grades, churn builds.

## 2. The flat-regime derivation (the transient floor, exact)

While the prefix cut s_t ≤ 1 (the sub-diagonal regime), the prefix region is the triangle T_s = {u, v ≥ 0, u+v ≤ s}, and ρ is scale-free: for two iid uniform points in T₁, P(u₁<u₂, v₁<v₂) = ∫_T (1−u−v)²/2 du dv ÷ |T|² = (½·B(2,3)) / ¼ = (1/24)/(1/4) = 1/6, so **ρ = 2·(1/6) = 1/3 exactly** — the early transient gradient is 2(⅓ − ½) = **−⅓ exact**. (s6b measured 0.327/0.327 at t = 64/128 — the finite-n value with boundary corrections.) For s_t > 1 the prefix is the square minus the upper corner triangle and ρ(t) rises from ⅓ to ½ at completion (s6b: 0.383 at t = 192, 0.504 at t = 255); the receipt takes this segment from calibration (the closed form is a longer integral, not needed for the run — the accompanying theory task for paper 3).

Pinned consistency check **C-ρ**: the calibrated ρ(t) over the sub-diagonal regime (operationally: the first half of scored stages, t ∈ [64, 128]) must sit within ±0.02 of the derived ⅓ **as the window mean** (the receipt implements the mean form; a pointwise reading would refuse on the window's right edge, which genuinely rises at finite n — ambiguity disclosed and resolved per the round-8 review, MINOR-5b; the gate is measured weak, ~21% population false-refusal under correct code, so it is an integrity check, not a sharp instrument); ρ(N) within ±0.02 of ½. Fails ⇒ calibration bug, halt (integrity class, not physics).

## 3. What is measured (all pinned)

Same substrate, instrumentation, and conventions as s5/s6 (14-candidate menus = truth + 12 kernel decoys + empty; forced-faithful trajectories; t ≥ 64; tie-generous `≤`; n = 256; 4 reps; single `default_rng(20260715)`; float64 accumulators over the float32 Gram fast-path — decision-invariance carried from the round-7 review).

- **G1 (the branch gate):** arm-C marginal truth-preference rate. **≥ 0.6 ⇒ STAGE-PRICED-PREFERRED; ≤ 0.3 ⇒ REJECTED; else MIXED.** The chance line is pre-registered this time: null in [1/14, 1/13] = [7.1%, 7.7%]; the receipt prints the rep-level t against 1/14 alongside the rate, and the verdict prose will distinguish below-chance / chance-level / above-chance *in addition to* the branch.
- **D1 (the mechanism signature, registered as a prediction):** the s6b decomposition runs in-receipt on the same stream. **Registered expectation: the Row-C dominance collapses** (the |Row-C| > |Row-A| fraction at loss steps falls from 93.8% to below 50%), and the truth-vs-winner Row-C gap centers near 0. If G1 rejects *and* D1 shows the dominance collapsed, the rejection localizes to Row A + residual fluctuations — a new fact either way. If D1 shows dominance persisting, the stage profile failed to neutralize the transient (calibration/instrument suspect — investigate before any verdict prose).
- **G2 (the production bench; runs whatever G1's branch, s6 precedent):** free-run pure-kernel-menu endpoints under arm C, 4 reps: global r ∈ [0.35, 0.60] (the guard; note ρ steers toward ½ at completion by construction), r_I ∈ [0.35, 0.65] in ≥ 3/4 reps, m_ab ≤ 3× the 3-sprinkling faithful base (the base's ±10–40% instance spread is on record — note-s6 C4). Passing G1 ∧ G2 = increment-production reborn at DEMONSTRATED-calibrated grade. G2 refusing while G1 passes = marginal preference without endpoint fidelity — the path-effects fork, named for investigation.
- **Verdict semantics:** branch verdicts recorded whatever they are; refused gates print the ledger and the receipt exits 1 by design; [directional] tags on any 4-rep cross-arm comparison (vs raw/A/B: unpaired, seed-confounded).

## 4. Kill conditions and downstream

- **G1 REJECTED with D1-collapse:** the re-pricing program is closed at BOTH terms (per-pair family measured closed at ≤ 7.7%; the global term's stage-priced form rejected with its transient neutralized). Paper 3's ending: the action is a grader; no admissible increment re-pricing builds; churn is the production mechanism (division of labor final at this move class). No further arms — "trajectory-level pricing" (non-Markovian path functionals) would be a C4 class extension needing its own design note and corpus legality argument, explicitly out of s7's scope.
- **G1 STAGE-PRICED-PREFERRED:** the production line reopens; G2 decides at what grade; the immediate follow-ups (pinned now): the s2-scale rerun (n = 512/1024) and the forgery battery under arm C.
- **MIXED:** the rate lands in (0.3, 0.6) — report as measured, no verdict prose beyond the branch; the follow-up decision goes to the next round's design note with the D1 decomposition as input.

## References

LEDGER #48–#50; LOG rounds 6–7 (incl. the review entry); note-s5 + addendum; note-s6 §§1–5, Addendum, Review corrections C1–C6; receipts s5/s6/s6b (the committed-stream facts arm C answers); v9 paper 1 (Row C's derivation and floor); v9 paper 2 (the grader results arm C must not touch — and does not, §1); paper 11 §3 (the misfit ledger). Precision rule: feedback_precision_mpmath_80bit does not bind here (no near-vacuum/modular kernels; float64 + the reviewed fast-path, as in s5/s6).
