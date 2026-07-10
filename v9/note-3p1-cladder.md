# 3p1-cladder — round 43: the large-C parking hypothesis (round-occupied AND 4D?)

**Status:** design note, 2026-07-10 (v9 round 43). Receipt: `v9/code/dimwall_cladder.py` (pinned here, committed strictly before running). Reviews ON.

## 1. The hypothesis and the two mechanisms

Round 42/42b measured, at C = 3: rounding the occupied cone is reachable only on the common-reset branch and costs volume-dimension in lockstep down to 2 (the sweet spot empty). The mechanism there is CLOCK-MERGING: common resets correlate the channels toward co-monotonicity. The parking hypothesis (user-posed; = the R-A ledger's registered "round Lorentz cone is the many-channel/mixed limit"): at larger C a SECOND mechanism exists — STATISTICAL ROUNDING — displacement between related events is a sum of many multi-channel increments, so the transverse cloud Gaussianizes (isotropizes) without the clocks merging; ride the common-reset dial down from dim ≤ C+1 and ask whether some point is simultaneously round-occupied and certified ≥ 4D. The pessimistic scenario, registered: the (shape, effective-dimension) frontier is C-independent — F ≈ round always demands effective-d ≈ 2 — and larger C only lengthens the dial. Either outcome is decisive: PARKING-EXISTS would be the first record-grown object simultaneously 4D and round-occupied (with the 4 dial-tuned, not selected — the constants-pattern disclosure applies); UNIVERSAL-FRONTIER generalizes the no-go and sends the program to the rotating-frame class.

## 2. The instrument upgrade: F_iso (effective-3-frame isotropy; certification-gated)

The native-frame footprint's corner directions are C+1-dependent; cross-C comparison needs a common frame. Pinned construction: standardize coordinates per component; d-hat = diagonal/sqrt(C+1); related pairs with s >= 0.3; v = w/s (transverse, C-dim). PCA: eigenvectors of the v-cloud covariance, top 3 (sign convention: largest-|component| positive); project v to the effective 3-space. Directional supports h(u) = q90 of positive projections over a PINNED 64-direction Fibonacci sphere; **F_iso = mean(top 8 of h) / mean(bottom 8 of h)**. Round cloud → ≈ 1; simplex-like → well above 1. NO corner knowledge needed (orientation-free). Degenerate guard: if the third PCA eigenvalue < 1e-6 × the first, the point is flagged DEGENERATE (collinear/planar cloud) and excluded from parking eligibility (the round-42 collinearity-identity lesson).

## 3. Grid and baselines (seeds 20262400+; 5 per point)

- **The ladder:** C ∈ {3, 4, 6, 8} × the rounding branch (per-slot Dirichlet(β) weights, FULL-VECTOR churn), β ∈ {1, 4, 16, 64}.
- **INFO rows:** per-channel-churn equal-split at each C (the dimension-preserving baseline); the equal+full endpoint is NOT run (proved identity-artifact, round-42 close).
- **Anchors:** M4-own-coordinates; orthant-iid k = 4; orthant-iid k = 9 (the C = 8 coordinate count) — all read through the SAME F_iso pipeline (PCA + Fibonacci directions).

## 4. Pinned gates

- **Gc0 (certification, strict separation):** min over {orthant-4, orthant-9} seeds of F_iso > max over M4 seeds of F_iso (5 each). REFUSED ⇒ VOID-INSTRUMENT (the projection/statistic is unfair), stop before any web.
- **Gc-w (wiring):** the NATIVE-frame F for C = 3 fv β ∈ {1, 4, 16} at the 42b seeds reproduces the 42b rows (mean and band to 3 d.p.).
- **Gc1 [MEASURED]:** F_iso(C, β) grid + per-point windowed d_MM (Δ = 512, NW = 128, frozen M2–M5 curve, clamp at 5) + in-window 2-realizer refusals (2 × 144 per seed) + the PCA-degeneracy flag; the C = 3 F_iso column's rank agreement with the native F (INFO consistency).
- **Gc2 (parking certification):** at every PARKING CANDIDATE (F_iso ≤ 1.1 × max(M4 band) AND refusals ≥ 8/10 AND win d_MM ≥ 3.7, non-degenerate): S₄-witness search (find_sk verbatim from dimwall_witness, tries = 20000) — candidate CONFIRMED iff witnesses found + verified on ≥ 3/5 seeds; S₅ search at C ≥ 4 confirmed candidates as INFO.
- **Gc3 (the verdict; a read):** PARKING-EXISTS (≥ 1 confirmed candidate) / UNIVERSAL-FRONTIER (no point reaches F_iso ≤ 1.2 × max(M4) with win d_MM ≥ 3.0) / MIXED-FRONTIER (the frontier per C printed).
- Exit 1 only on Gc0/Gc-w.

## 5. Scope and kill-risks

F_iso reads OCCUPANCY in the effective 3-frame; geometric cones remain polyhedral at every point (the #104 scoping). Named kills: (K1) PCA on the v-cloud could align to noise at near-isotropic points — the eigenvalue spectrum is printed per point; (K2) the d_MM proxy is volume-conditional with two recorded confound exhibits — parking eligibility therefore requires the REALIZER and the S₄ WITNESS, with d_MM as the volume co-signature only; (K3) at C = 8 the dominance relation is sparse (ordering fraction ~2^-8 iid) — pair counts after the s-floor are printed and MIN_PROJ guards fire visibly; (K4) cross-C d_MM comparability rides the SAME frozen curve (a 4-coordinate-family calibration applied to higher-C webs — disclosed; the realizer/witness instruments carry the dimension claims).

## References

Rounds 40/42/42b (LEDGER #103–#109; the frontier, the confound exhibits, the collinearity identity); note-3p1-dimension-ledger §2 R-A (the registered limit); dimwall_witness (find_sk/verify_sk, verbatim); dimwall_dialsweep{,_b} (builders, metrics — verbatim); the frozen mm_reference.json.

## Round-43 amendment 1 (Gc0 VOID, diagnosed; appended before the amended receipt runs)

The certification refused exactly as designed, catching two wiring flaws before any web was read: **(a)** the F_iso pipeline used the diagonal causal axis for ALL families — but M4's axis is the t-axis (the round-40 convention, dropped in transcription); the mis-axed M4 transverse cloud is offset/anisotropic and starves sphere directions below MIN_PROJ. Fix: family-specific d-hat exactly as round 40 (M4 → t-axis; dominance families → the diagonal). **(b)** the orthant-9 anchor at N = 256 has ~2^-9 ordering fraction → ~80 related pairs — the pin's own K3 sparsity risk, firing on the anchor itself. Fix: the orthant-9 anchor runs at N = 1024 (≈ 1000 pairs); web pair counts remain printed and MIN_PROJ-guarded. Gates otherwise unchanged.
