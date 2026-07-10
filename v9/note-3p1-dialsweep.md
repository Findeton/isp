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

## Round-42 amendment (pre-review, wiring-driven; appended)

**What the wiring gates caught, in order:** (1) Gd0b refused twice — the sweep's sprinkler must be `openings_pass.py`'s (the frozen json's writer, 6N-batch); the corpus carries THREE sprinkle_mink variants (phase0 one-at-a-time; m5cal 4N; openings 6N) — flagged for the review as a lineage item. (2) Gd0c refused for a REAL reason: the anchor was mis-pinned from memory. The corpus record (LOG rounds 24/29/30): the uniform+full-reset builder ("A6") read full-web d_MM = 2.50 at round 24 — **Gm3 REFUSED, DIM-WITHOUT-VOLUME** — and my A6 reproduces it (2.46 fresh seeds; 2.51 at the round-24 seeds through the frozen reference). The d = C+1 = 4.04 crown reading is the WINDOWED metric (Δ = 512, m5cal, S₄-witnessed at round 30), and **the crown class is α = 0.75 with PER-CHANNEL churn (m5cal's web_chiv) — the same class as the round-40 corner webs**; this note's §2 and the round-42 LOG open mis-identified the certified class as the uniform builder — corrected here.

**Re-pinned gates (supersede §4's Gd0c/Gd2/Gd3):**
- **Gd0c′ (the crown anchor):** `win_frac` (m5cal verbatim: Δ = 512, NW = 128) at m5cal's own seeds 20260960–4, mean fraction through the frozen M2–M5 curve, must reproduce the m5cal print: fraction 0.1008, windowed d_MM = 4.04 (two decimals).
- **Gd2′ (the dimension curves, WINDOWED):** per dial point: windowed fraction (Δ = 512, NW = 128, the win_frac construction on the dial builder; the window draw follows the F-window draw in rng order — disclosed, fresh seeds) → windowed d_MM through the frozen M2–M5 curve (M5 included; below-M5 clamps at 5 per m5cal); refusals = two 144-index draws from the central Δ = 512 window per seed. Full-web d_MM and fraction demoted to INFO (the round-29 mixture-dilution).
- **Gd3′ (the verdict, on the crown metric):** SWEET-SPOT-EXISTS iff some point has F ≤ 1.10 AND windowed refusals ≥ 8/10 AND windowed d_MM ≥ 3.7 (the crown band floor). TRADE-OFF-NO-GO iff every point with F ≤ 1.20 has refusals ≤ 2/10 OR windowed d_MM ≤ 3.0. Else MIXED-FRONTIER (frontier printed both directions).
- **A6 demoted to an INFO consistency print** (must sit near the round-24 2.50 full-web reading; it does).

**Gd0c″ (the anchor's mapping, corrected with a disclosure):** the m5cal builder byte-reproduces (windowed fraction 0.1008 exactly at m5cal's seeds), but the FROZEN reference curve maps 0.1008 to **d_MM = 3.97**, not the m5cal-printed 4.04 — m5cal interpolated on its own in-receipt M4/M5 (4N-batch sprinkler; its M4 sat above the frozen 0.0966, placing 0.1008 in the M4–M5 segment). Under the corpus's canonical frozen curve the crown windowed reading is **3.97**; the 0.07 shift is within the round-30 review's noted calibration wobble (±0.2–0.4 across curve draws) and is now on the record. The anchor gate pins: fraction = 0.1008 (4 d.p.) AND d_MM(frozen) = 3.97 (2 d.p.). The Gd3′ floors are unchanged (3.7/3.0 — both sides of the wobble).

## Round-42 review corrections (appended) + the in-family completion receipt (42b)

**MAJOR-1 (scope):** the no-go verdict is scoped to THE SWEPT DIAL FAMILY (one-hot preference; per-slot Dirichlet incl. equal-split; per-channel churn on the mixing branch); the mechanism sentence ("rounding needs positive cross-channel association…") is re-tagged [directional]. Two cheap in-family dials were NOT swept and are pinned below as receipt 42b; family-wide wording is restorable only if both hold the floor. **MINOR-1:** at α = 1.0 the two dimension instruments DISAGREE (win d_MM 3.34 vs 2-realizable 10/10) — the realizer is ground truth; the fraction-d_MM proxy is confounded at segregated/sparse classes (the α = 1.0 row = the standing exhibit; recorded in the dimension ledger). **NIT-2 disclosure (review-required):** the two refused wiring attempts printed full sweep rows under the superseded full-web metric before the re-pin; the re-pin was corpus-forced (the original Gd0c was unsatisfiable — full-web A6 = 2.46/2.50 vs a floor of 3.0 mis-pinned from memory), so no result-shopping was available; the rows themselves were unchanged by the metric re-pin (same builders, same seeds). **NIT-1:** the Gd0c″ pin+receipt edits shared one commit (zero-degrees-of-freedom change; two-commit discipline resumes). **NIT-3:** the scale read is "persists under one doubling [directional]". **MINOR-2 decision:** the canonical sprinkler is openings_pass's 6N (the frozen json's writer); frozen receipts stay untouched (freeze discipline beats docstring hygiene) — the lineage lives here and in LEDGER #108.

### Receipt 42b (`v9/code/dimwall_dialsweep_b.py`; pinned here, committed strictly before running)

- **Ge-w (wiring):** the round-42 per-slot b = 1.0 row (F, windowed fraction) reproduced exactly at the round-42 seeds.
- **Ge1 (per-commit Dirichlet):** fresh W ~ Dir(β·1) drawn PER DEPOSIT (not per slot), β ∈ {0.25, 1, 4}; per-channel churn; F + windowed d_MM + windowed refusals per point (5 seeds, 20262300+).
- **Ge2 (mixing × full-vector churn):** per-slot Dirichlet W, β ∈ {1, 4, 16}, churn = full-vector single-victim resets (the phase-1 convention); plus the memo's degenerate endpoint (equal-split + full-vector churn) — expected by proof: co-monotone, dim ≤ 2, F degenerate; printed and flagged.
- **Ge3 (the floor verdict):** FLOOR-HOLDS iff no non-degenerate point reads F below the orthant-iid band minimum (1.307); FLOOR-BEATEN otherwise (with the point named). Either read decisive: HOLDS ⇒ the family-wide no-go wording is restored (with the family now actually covered); BEATEN ⇒ MIXED-FRONTIER reopens in-family.
- Exit 1 only on Ge-w.

**Re-review addendum (round-42 close):** F ≡ 1 is an IDENTITY for a collinear transverse cloud (the equal+full endpoint's χ-columns are identical, so the standardized transverse cloud is collinear along ℓ ∝ (3,−1,−1,−1); corner/face direction weights cancel — γ₀ = 1 vs 3 × ⅓ — for any distribution along the line). The endpoint's 1.000 is a degeneracy artifact, NOT a round cross-section; the honest rounding datum on the common-reset branch is β = 16's 1.270. Also on record: the per-commit branch's validation anchor — its β → ∞ limit is round-42's equal-split/per-channel-churn row, and the measured trend converges onto it (1.462 → 1.409 → 1.348 vs 1.343).
