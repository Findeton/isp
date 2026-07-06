# 3p1-p1 — Phase 1: the multi-channel builder and the dimension gates

**Status:** design note, 2026-07-06 (v9 round 24; PLAN §the-3+1-program Phase 1). Receipt: `v9/code/dimwall_phase1.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE (user, on record): the Phase-0-certified instruments (Gw 300/300) are the compensating discipline; a C = 3 PASS at d ≈ 4 is flagged PENDING-USER-REVIEW-DECISION, not graded terminal.**

## 1. The builder (record-native, one change from the corpus class)

The wb-line churn web with **C independent evidence channels**: each click deposits Exp(0.109551) evidence into ONE channel (chosen uniformly) of the committing slot; each commit snapshots the slot's full channel vector χ⃗; churn (rate 1/L) resets the victim's **whole vector** (the record dies — the ontology's reading; the per-channel-reset variant is an INFO probe, not the pinned class). **Dominance:** x ≺ y iff b_x < b_y AND χ_k(x) ≤ χ_k(y) for every channel k. The weak channel inequalities keep same-slot worldlines chains (only the event's channel grows per commit); the order is still the intersection of C + 1 linear orders — the (χ_k, b)-lexicographic clocks plus b — so **dim ≤ C + 1 by the Phase-0 Lemma**, and C = 1 reproduces the corpus class (cross-slot χ-ties have measure zero). Fixed frame: (N, M, L) = (2048, 32, 16); seeds 20260770+.

## 2. Registered expectations and the polyhedral references

For iid uniform (C+1)-coordinate dominance the ordering fraction is exactly 2^{−C} (analytic; C = 1 gives ½ = the M² anchor). The grown web sits ABOVE the iid fraction (slot chains add relations — measured at C = 1 in Phase 0: 0.594 vs 0.5), so d_MM (calibrated on ROUND-cone references) is expected to read BELOW C + 1: the registered shape is **monotone growth of d_MM with C toward the polyhedral ideal** (iid polyhedral C = 2 reads ≈ 2.9 and C = 3 ≈ 3.8 on the round curve), not exact equality. The sharp claim lives on the order-dimension side. Kill-risks (registered, both informative): whole-vector churn resets synchronize channels within slots → effective clock collapse (2-realizers keep passing at C ≥ 2, d_MM stuck near 2); the race-model kill extending (the higher cone not filled by the dynamics).

## 3. Pinned gates (Phase-0 instruments verbatim: the Golumbic tester; the measured MM curve re-derived in-receipt)

- **Gm1 (THE WALL COMES DOWN — sharp):** the 2-realizer test REFUSES induced 144-commit subposets of C = 2 and C = 3 webs on ≥ 4/5 seeds each (two draws per seed; a seed counts if either draw refuses — refusal on an induced subposet is a valid witness of whole-web dim ≥ 3, by monotonicity; dilution can only cause false passes, hence the two draws and the 4/5 bar).
- **Gm2 (the control):** C = 1 webs PASS on 5/5 seeds (the corpus class, instrument consistency).
- **Gm3 (the dimension dial — directional, generous):** on seed-means of the full-web (N = 2048) ordering fraction through the Phase-0 calibrated curve: d_MM strictly monotone in C (C = 1 < C = 2 < C = 3) AND d_MM(C = 2) ≥ 2.5 AND d_MM(C = 3) ≥ 3.0.
- **Gm4 (INFO, unpinned):** the analytic 2^{−C} polyhedral references and measured iid-dominance fractions alongside; the channel-correlation diagnostic (cross-slot correlation of channel levels per web); the per-channel-reset variant's d_MM (the reset-synchronization probe); the no-churn (L → ∞) variant's d_MM (the race-model probe).
- **Verdict semantics:** Gm1 ∧ Gm2 ∧ Gm3 ⇒ **DIMENSION-TRACKS-CHANNELS [MEASURED; C = 3 flagged PENDING-USER-REVIEW-DECISION]** — the wall of Phase 0 comes down by construction within the ontology, and Phase 2's questions (Lorentzization; what fixes C = 3) become live. Gm1 refusing with Gm4's correlation diagnostic high ⇒ **CLOCK-COLLAPSE** (the named kill: channel synchronization — the reset variant localizes it). Gm3 refusing with Gm1 holding ⇒ **DIM-WITHOUT-VOLUME** (the order dimension rises but the continuum estimator doesn't follow — the polyhedral/manifold gap becomes the finding). Exit 1 by design on any refusal.

## 4. Scope

No hostile review (mode on record). The builder's channel-choice (uniform per event) and the whole-vector reset are the pinned class; variants are probes. d_MM is calibrated on round-cone references and read on polyhedral-cone webs — the systematic direction (reads low) is disclosed in §2 and folded into Gm3's floors. A pass here is a dimension-of-the-ORDER result; manifoldlikeness of C ≥ 2 webs (the copula, the certifier) is Phase 2/3 territory, not claimed.

## References

note-3p1-dimension-ledger (+ Phase-0 receipt: the Lemma, the certified tester, the measured MM curve); PLAN §the-3+1-program; the wb-line builder (construction provenance); LEDGER #82.
