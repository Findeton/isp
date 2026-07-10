# 3p1-dialsweep — Phase 2b: the specialization/mixing dial vs (cone shape, order dimension)

**Status:** design note, 2026-07-10 (v9 round 42; the round-40 close's named receipt). Receipt: `v9/code/dimwall_dialsweep.py` (pinned here, committed strictly before running). Reviews ON.

## 1. The question and the registered tension

Round 40 established: the α-preference dominantly concentrates the occupied cone cross-section (F 2.17 at α = 0.75 vs 1.46 at α = 0), and Dirichlet mixing rounds it (kdir 1.78). The dimension results (d = C + 1, paper 6) live at the uniform-choice end. The tension, registered as the round's hypothesis-to-test: **mixing that rounds the cone may collapse the dimension** (channel co-monotonicity ⇒ effective clock merger ⇒ the two-clock wall returns). The deliverable is the measured trade-off frontier.

**The theory memo (the limit point, proved here):** at Dirichlet β → ∞ with FULL-VECTOR resets, every deposit moves all channels by exactly e/C and every reset zeroes the whole vector, so χ₁ = χ₂ = … = χ_C at every commit — dominance degenerates to the two-clock order (b, χ) and **dim ≤ 2 exactly** (the weak two-clock lemma; single shared clock). Under the Lorentz-line PER-CHANNEL churn, independent per-channel resets break exact equality even at β = ∞ — the endpoint is then partial decorrelation, and its dimension is a measurement, not a corollary. Both endpoint flavors are in the sweep.

## 2. Builders (two conventions, disclosed and separated)

- **The Lorentz-line builder** (verbatim from rounds 36/40: web_window — one-hot deposits with α-preference OR per-slot Dirichlet(β) weights; PER-CHANNEL churn victims; window Δ = 1024 central, NW = 256): the F-side convention, wiring-anchored to round 40.
- **The paper-6 class** (verbatim conventions of dimwall_phase1's web_rel_C: uniform channel choice, one-hot deposits, FULL-VECTOR churn): the dimension-side certified class, included as the anchor point A6.
- The sweep builds each web ONCE per (dial, seed) at N = 2048; F is computed on the central windowed subsample; the ordering fraction, d_MM, and the 2-realizer refusal (two 144-commit induced subposets per seed, Golumbic tester verbatim from phase 0/1) are computed on the full web.

## 3. Dial grid (5 seeds per point, seeds 20262200+)

- Preference dial: α ∈ {0, 0.25, 0.5, 0.75, 1.0} (one-hot, Lorentz-line churn).
- Mixing dial: Dirichlet β ∈ {0.25, 1, 4, 16, EQUAL} (EQUAL = exact 1/C split; Lorentz-line churn).
- Anchors: A6 = the paper-6 class; plus the frozen instruments' own anchors via the wiring gates below.

## 4. Pinned gates (exit 1 only on wiring/anchor refusal; the trade-off verdict is a read, not a pass/fail)

- **Gd0a (wiring, F side):** corner (α = 0.75) and kdir (β = 1) windowed F at seeds 20262000–4 reproduce the round-40 prints exactly.
- **Gd0b (wiring, MM side):** the in-receipt re-derived MM reference fractions equal the frozen `v9/data/mm_reference.json` to 1e-9 (M2/M3/M4).
- **Gd0c (the dimension anchor):** A6 at C = 3: 2-realizer refusals ≥ 4/5 AND d_MM ≥ 3.0 (phase-1's own floors — instrument consistency with the certified class).
- **Gd1 (the shape curves) [MEASURED]:** F(dial), both parametrizations, 5-seed bands; the registered directional read: F decreasing in mixing, increasing in α.
- **Gd2 (the dimension curves) [MEASURED]:** per dial point: refusal count (of 10 draws: 2 per seed), mean ordering fraction, d_MM; the channel-correlation diagnostic (mean pairwise corr of χ columns).
- **Gd3 (THE TRADE-OFF VERDICT; pinned semantics):** SWEET-SPOT-EXISTS iff some dial point has F ≤ 1.10 AND refusals ≥ 8/10 AND d_MM ≥ 3.0. TRADE-OFF-NO-GO iff every point with F ≤ 1.20 has refusals ≤ 2/10 OR d_MM ≤ 2.5. Otherwise MIXED-FRONTIER (the frontier printed: the max-d point among F ≤ 1.2 and the min-F point among refusals ≥ 8/10). All three verdicts are decisive reads; none is a receipt failure.
- **Gd4 (the scale leg) [directional]:** at three points (α = 0.75; β = 1; β = 16): N = 4096 builds, F at (Δ, NW) = (1024, 256) vs (2048, 512) — the direction of F under window scaling printed per point (persist/sharpen/decay).
- **INFO:** tie fractions and cap-mass per dial; the angular tie-immune F at three points; pair counts; per-dial channel-corr.

## 5. Scope and kill-risks

The F instrument reads OCCUPANCY (the round-40 #104 scoping); geometric cones are orthants at every dial point — "rounding" means the occupied cross-section approaches the round band, and the β = ∞/full-reset endpoint degenerates by construction (the memo; its F is printed but flagged degenerate — the v-cloud collapses toward a line, and dimension is ≤ 2 there by proof, not measurement). Named kills: (K1) the 144-subposet refusal test may lack power exactly where the frontier matters (partial mixing) — the refusal COUNT (not a binary) is the print, and d_MM is the second dial; (K2) windowed F vs full-web dimension = different supports — disclosed, matches the round-40/paper-6 conventions respectively; (K3) the two churn conventions differ across builders — never mixed within a curve, and A6 ties them.

## References

Round-40 close (LEDGER #103–#105; the ablation; the re-review's both-parametrizations requirement); note-3p1-lorentz2-footprint (+ its corrections section); dimwall_phase0/phase1 (the certified dimension instruments, copied verbatim); v9/data/mm_reference.json (frozen); note-3p1-p1-multichannel (the paper-6 pinned class); the weak two-clock lemma (note-3p1-dimension-ledger, round-35 corrected form).
