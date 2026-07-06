# 3p1-p1b — Phase 1b: decorrelating the channels at the source

**Status:** design note, 2026-07-06 (v9 round 25). Receipt: `v9/code/dimwall_phase1b.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE on record; the Phase-0-certified instruments carry the discipline. Reserved-review trigger (tightened): d_MM(C = 3, pinned point) ≥ 3.7 ⇒ the verdict is flagged PENDING-USER-REVIEW-DECISION, not graded.**

## 1. The refined diagnosis and the two mechanisms

Round 24 measured the gap's cause: the channel correlation (+0.73/+0.60) is the **common-age factor** — every channel of a slot grows with the slot's lifetime, so commit vectors align along (1, …, 1) and cross-slot dominance stays near two-clock-dense. Decorrelation must break age-commonality:

- **V-A (slot-channel affinity):** each slot has a preferred channel (round-robin over the fleet); a click deposits into the preferred channel with probability α, else uniformly over all channels (so P(pref) = α + (1−α)/C). Vectors acquire slot-specific *directions*. **The α = 1 control (registered, theorem-backed):** full segregation makes cross-group commits永incomparable — the order becomes a disjoint sum of two-clock orders, and dim(⊕ᵢ Pᵢ) = max dim(Pᵢ) ≤ 2: the 2-realizer test must PASS again at α = 1. So the registered shape is an **interior optimum in α**: dimension requires channels that are distinct *and* interacting — decorrelation alone is insufficient. This control doubles as the sharpest instrument check available without a referee.
- **V-B (independent per-channel churn):** each channel carries its own reset process at rate 1/L (independent victims) — resets desynchronize across channels and channel-ages decouple within a slot. (Round 24's probe reset one random channel *on the shared clock*; V-B gives each channel its own clock.)

The **vector-clock/seal-gossip ontology** (commits carry witnessed per-channel evidence propagated by seals — distributed-systems causality verbatim) is ledgered as the Phase-2 candidate: gossip *raises* correlation, so it is not a decorrelation mechanism; its role, if any, is Lorentzization (cone rounding by propagation). Not built this round.

## 2. Pinned gates (Phase-0/1 instruments verbatim; the pinned point = α = 0.75, per-channel churn, C = 3; seeds 20260790+)

- **Gb1 (decorrelation works):** at the pinned point, channel-corr < 0.25 on 5/5 seeds (round-24 baseline +0.598).
- **Gb2 (the dial responds):** at the pinned point, d_MM ≥ 3.0 (seed-mean, the Phase-0 calibrated curve) AND the 2-realizer REFUSES on ≥ 4/5 seeds (dimension retained — the α = 1 pathology must not be re-entered).
- **Gb3 (the C-ladder at the pinned mechanism):** d_MM strictly monotone over C = 1, 2, 3 (C = 1 = the corpus baseline) with d_MM(C = 2) ≥ 2.6.
- **Gb4 (the segregation control):** at α = 1 (C = 3, per-channel churn), the 2-realizer PASSES on ≥ 4/5 seeds — the disjoint-union theorem made visible; a refusal here impeaches the instrument or the theorem and voids the round (named).
- **INFO (unpinned):** the full sweep table at C = 3 — α ∈ {0, 0.5, 0.75, 0.9, 1.0} × churn ∈ {shared-full, per-channel}, 3 seeds each: corr / fraction / d_MM / realizer — the dimension-vs-affinity curve with its registered interior optimum; the polyhedral ideals alongside; overshoot beyond the M⁴ calibration range printed as "beyond-range" honestly.
- **Verdicts:** all gates ⇒ **DECORRELATION-ACHIEVED [MEASURED]** (and if d_MM(C = 3) ≥ 3.7: PENDING-USER-REVIEW-DECISION); Gb1 holds but Gb2's dial lags ⇒ DECORRELATED-BUT-FLAT (the common-age story was incomplete — the residual named from the sweep); Gb1 refuses ⇒ AFFINITY-INSUFFICIENT; Gb4 refusing ⇒ ROUND-VOID (instrument). Exit 1 by design on refusal.

## 3. Scope

No hostile review (mode on record). The affinity assignment (round-robin preferences, the α-mixture form) is the pinned class; the sweep is the probe. d_MM remains the round-cone-calibrated estimator read on polyhedral webs (systematically low, disclosed in p1 §2). A pass is still an order/volume-dial result at fixed C — Lorentzization (cone shape), the manifold copula, and "why C = 3" stay Phase 2/3.

## References

note-3p1-p1 (+ the round-24 receipt: the wall down, the gap measured, the no-churn inversion); note-3p1-dimension-ledger (the Lemma; the instruments); PLAN §the-3+1-program; LEDGER #83.
