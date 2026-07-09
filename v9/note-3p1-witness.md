# 3p1-witness — the committed witness certification + the selection-logic successor

**Status:** design note, 2026-07-09 (v9 round 35 — the paper-6 hostile review's MAJOR-4a and MINOR-1). Receipts: `v9/code/dimwall_witness.py` (§1) and `v9/code/dimwall_selection_v2.py` (§2), pinned here and committed strictly before the receipts (which are themselves committed pre-run). **REVIEWS RESTORED (round 35, a1fa12c).**

## 1. The witness receipt (`dimwall_witness.py`) — MAJOR-4a

The round-30 reserved review's S_{C+1} witness certification — the lower-bound half of the [MEASURED — sharp] grade (LEDGER #89) — ran uncommitted: no committed artifact carries it, and the round-35 openings replacement searcher died its own validation (0/5 on iid 4-orthant, LEDGER #94 — diagnosed as tries = 200 underpower; the paper-6 review validated the same searcher 5/5 at 20,000 tries). This receipt makes the certification a committed, rerunnable artifact.

**The searcher (pinned):** `find_s4` ported from `openings_pass.py` — identical bucket logic (a size-k antichain A from a random permutation; candidate points above exactly k − 1 of the a's, bucketed by the one missing a and required incomparable to it; 60 mutual-incomparability draws for B) — generalized to generic k (the S3 variant: 3 + 3, sum(above) = 2), with the bucket step vectorized (numpy) and early exit on the first witness. **tries = 20000, FROZEN: a refusal is recorded, never re-tried at higher power.** One search-RNG stream, seed 20261440, consumed in the printed gate order. Builders `web_chiv` / `rel_win` ported verbatim from `openings_pass.py` (the pinned class: alpha = 0.75, per-channel churn, N = 2048, M = 32, L = 16, Exp(0.109551) deposits).

**W1 (validation — all five legs must hold, else searcher-dead and exit 1):**

- S4 found in iid 4-orthant (N = 128; seeds 700–704) on **5/5**;
- S4 found **0/5** on iid 3-orthant (seeds 800–804) — theorem-guaranteed absence (dim ≤ 3);
- S4 found **0/10** on C = 2 windows (web seeds 20261420–20261424, 2 consecutive draws each; Δ = 512 central, N = 128) — theorem-guaranteed absence (dim ≤ 3 by the weak-form Lemma);
- S3 found in iid 3-orthant (seeds 800–804) on **5/5**;
- S3 found **0/5** on iid 2-orthant (seeds 900–904) — dim ≤ 2.

**W2 (the certification):** the five pinned C = 3 seeds **20260960–20260964** (the round-29/30 window class), Δ = 512 central windows ([768, 1280)), N = 128 subsamples drawn from the builder's returned RNG, **up to 6 draws per seed, stopping at the seed's first witness**: S4 witnesses on **5/5 seeds**, AND S3 witnesses in the same five seeds' C = 2 windows on **5/5**. Every witness found anywhere in the receipt is **explicitly re-verified against the relation matrix** — the full induced-S_k standard-example pattern asserted: A an antichain, B an antichain, a_i < b_j iff i ≠ j (and never b_j < a_i), a_i incomparable b_i — and the witness tuples printed (seed, draw, global commit indices). Exit 1 on any refusal; a seed that refuses after 6 draws at the frozen tries is recorded as such — the verdict prints what it prints.

## 2. The selection successor (`dimwall_selection_v2.py`) — MINOR-1

Round 31's `dimwall_selection.py` prints the superseded "SELECTS (C_eff ~ 7.2)" on every rerun: the pinned C_max-independence conjunct (note-3p1-p5 §a) was never implemented in the class logic — ce5 is computed and never used; the record's C_MAX-TRACKING correction (LEDGER #90) is verified right. Receipts are single-commit frozen, so the fix ships as a successor: the survival part ported verbatim (web_survival, the eta × L grid, SEEDS 20261110–20261112, the C_max = 5 spot at center dials), the d_MM curve loaded from the frozen `v9/data/mm_reference.json` (byte-identical to the round-31 in-receipt curve — same seed recipe), and the class logic fixed:

- **COLLAPSE** — max C_eff ≤ 2 everywhere (as before);
- **SELECTS** — span ≤ 1.5× AND |mean − median| < 0.5 AND the C_max = 5 spot REFUSES the tracking test below (the pinned C_max-independence conjunct: C_eff must not scale with C_max);
- **C_MAX-TRACKING** — |ce5/5 − mean(ceffs)/8| < 0.1 (the per-C_max ratios agree, both ~0.9: C_eff ~ 0.9 × C_max — no survival selection);
- **DIAL-TRACKING** — otherwise (span > 1.5×), as before.

Registered expectation: **C_MAX-TRACKING** (the corrected class). Mapping receipt; exit 0.

## References

The paper-6 hostile review (v9 round 35, MAJOR-REVISION — MAJOR-4a and MINOR-1; LOG round-35 receipt 3 will carry the disposition); LEDGER #89 (the reserved review and its grade), #90 (the SELECTS class correction), #94 (the openings searcher death); `openings_pass.py` (the ported searcher and builders); note-3p1-p5-selection (the pinned survival classes); note-3p1-p2d / `dimwall_phase2d.py` (the pinned seeds' provenance).
