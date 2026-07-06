# 3p1 — the dimension ledger: the two-clock obstruction, the escape routes, and Phase 0's instrument

**Status:** design note, 2026-07-06 (v9 round 23; PLAN §the-3+1-program, Phase 0). Receipt: `v9/code/dimwall_phase0.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE (user, 2026-07-06): this note and receipt run without hostile review; the wiring gate below is therefore load-bearing and deliberately over-built.** Freeze discipline unchanged.

## 1. The obstruction (theorem-grade, and why it re-attributes the whole T6 track)

**Lemma (two-clock wall).** Let ≺ be defined on a finite set by x ≺ y iff f_i(x) < f_i(y) for all i ∈ {1..k}, for k real coordinates (ties broken consistently). Then ≺ is the intersection of k linear orders, so its order dimension is ≤ k. *Proof: each f_i (with the tie-break) is a linear order; dominance is their intersection; order dimension is the minimum number of linear orders whose intersection realizes ≺.* ∎

Every corpus web's causal order is (b, χ)-dominance — k = 2 — so **dim ≤ 2 always, by definition** (the census's set-equality result and paper 13's universal realizer are this lemma's instances). And 2D Minkowski is *exactly* two-clock causality (light-cone coordinates u = t − x, v = t + x). Conversely, the round cone of M^d for d ≥ 3 is not an intersection of two half-space orders, and sprinklings of it refuse 2-realizers at modest N (the receipt measures this). **Re-attribution:** every 3+1 readout refusal in the T6 track was structural — the instruments were pointed at webs that could not carry d > 2. The wall is in the ontology's coordinate system, not in the dynamics or the readers.

## 2. The escape-route ledger

- **R-A (primary): multi-channel evidence clocks.** Commits accumulate evidence in C independent channels (channel-specific seals/species — vocabulary the ontology already owns); dominance = birth-and-every-channel ⇒ order dim ≤ C + 1, with **polyhedral** causal cones (intersections of C + 1 half-space orders). The round Lorentz cone is the many-channel/mixed limit. Registered predictions for Phase 1: d_MM ≈ C + 1 for grown multi-channel webs (2 → 3 → 4 at C = 1, 2, 3); a measurable polyhedral-anisotropy signature at finite C. Named kill-risks (both informative): channel correlation through the shared fleet collapsing the effective clock count; the race-model kill extending (the dynamics not filling the higher cone).
- **R-B (parked): seal-graph transverse structure** — extra dimensions carried by the seal network rather than the order. Parked because the causal order of M⁴ is not a product of a 2D order with a proximity graph; at best an effective/emergent route, revisit only if R-A dies.
- **R-C (the honest null): effective-2D** — accept dim 2 as the ontology's native dimension; the 2D-closure program (PLAN fallback: the manifoldlikeness certificate, scalar QFT kinematics, the dynamical-gravity probe).

## 3. Phase 0's instrument and pinned gates

The receipt builds and certifies the tools Phase 1 will trust, with no external review — hence the over-built wiring gate.

- **Gw (wiring — load-bearing):** the order-dim ≤ 2 tester (Golumbic implication classes on the incomparability graph: G is a comparability graph iff no implication class contains an edge and its reverse; dim(P) ≤ 2 iff inc(P) is a comparability graph) must agree with an INDEPENDENT brute-force decision (enumerate linear extensions L1; dim ≤ 2 iff for some L1 the conjugate relation P ∪ reverse(L1 on incomparables) is acyclic) on 300 random posets (n ≤ 7, mixed densities) AND on the canned cases: the standard example S₃ (dim 3) REFUSES; chains, antichains, and random 2D-dominance posets PASS. Any disagreement ⇒ the receipt dies here (exit 1), nothing downstream is read.
- **Gd1 (the tester sees genuine 3D):** M³ diamond sprinklings (N = 128) REFUSE dim ≤ 2 on 5/5 seeds.
- **Gd2 (the tester passes genuine 2D at scale):** M² diamond sprinklings (N = 128) PASS on 5/5 seeds (M² is two-clock by construction — this is the tester's large-instance positive control).
- **Gd3 (instrument consistency on the corpus):** induced 128-commit subposets of grown corpus webs (the wb-line builder, one subsample from each of 5 seeds) PASS on 5/5 — consistent with the constructive (b, χ) realizer; the whole-web dim ≤ 2 is by the Lemma, not by this test.
- **Gd4 (the MM calibration, printed):** the Myrheim–Meyer dimension estimator implemented **formula-free** — the ordering-fraction reference curve is MEASURED from M^d diamond sprinklings (d = 2, 3, 4; N = 512; 8 seeds each; means ± sd printed), and d_MM(·) = monotone interpolation on that measured curve. Printed readings: M³ test sprinkles in the 3-band; corpus webs in the 2-band. This calibrated estimator is Phase 1's primary dial; its reference table ships in the receipt output.

**Verdict semantics:** all gates held ⇒ THE WALL IS MEASURED — the two-clock obstruction is real and instrument-visible (the tester distinguishes genuine > 2D causality from everything the ontology has ever grown), and Phase 1's tools are certified-by-wiring. This is a lemma-verification receipt, not an adjudication; refusals exit 1 as always.

## 4. Scope and disclosures

No hostile review (user instruction, on record here and in PLAN); the wiring gate and the brute-force cross-check are the compensating discipline. The Lemma is elementary (stated for the record, not claimed novel); the polyhedral-cone correspondence and the C + 1 prediction are REGISTERED HYPOTHESES for Phase 1, not results of this receipt. Order dimension is the sharp invariant here; Myrheim–Meyer is the continuum-facing estimator — the two can disagree on non-manifoldlike orders, which is exactly why both ship.

## References

v9 paper 4 §2 / v8 paper 13 Thm 2.1 (the universal two-clock realizer — the Lemma's corpus instance); the census (LEDGER #58 and the round-10 record; the natural-labeling contract); k1/l3 machinery (sprinkling constructions); PLAN §the-3+1-program; Golumbic (1977) (transitive orientation via implication classes); Myrheim (1978), Meyer (1988) (the dimension estimator, here re-derived by measurement).
