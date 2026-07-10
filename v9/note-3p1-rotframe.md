# 3p1-rotframe — round 44: the rotating-frame class (4D-and-round, or the family's last no-go)

**Status:** design note, 2026-07-10 (v9 round 44; the twice-endorsed spec of rounds 42–43). Receipt: `v9/code/dimwall_rotframe.py` (pinned here, committed strictly before running). Reviews ON.

## 1. The class and why it is the last route

Every no-go of rounds 40–43 shares one mechanism: NON-NEGATIVE one-hot/mixed increments in a FIXED frame can only fill orthant-shaped occupancy (corner-concentrated when anti-associated, iid-floor when independent, collapsed when co-monotone). The rotating-frame class breaks the premise: the deposit basis B_t ∈ SO(C) DRIFTS (B_{t+1} = R(ω, random axis) · B_t; the ω = ∞ mode draws a fresh Haar rotation per commit), deposits are e · (B_t e_k) — with NEGATIVE components allowed raw (the pinned negativity decision; clipping or projecting would re-impose the orthant mechanism and is rejected). The RELATION stays componentwise dominance in the fixed accumulator frame, so: (memo) the order is still the intersection of C+1 linear orders (b strict-injective; χ_k weak with b tie-break) — **dim ≤ C + 1 at every ω**, and all instruments keep their meaning. C = 3 throughout (parking at 4 is the target; dim ≤ 4 automatic).

## 2. Pre-registered endpoints and the interesting region (derived before running)

- **ω = 0:** B_t ≡ I — the round-40 corner class VERBATIM (the code path draws identically; the wiring gate is byte-level).
- **ω = ∞:** increments isotropic (uniform direction × Exp magnitude); the accumulators are isotropic walks with per-channel resets; dominance conditions an isotropic displacement law on the positive orthant ⇒ occupancy fills the orthant cross-section uniformly-ish — **F at the iid-floor at best, on a SPARSIFIED relation** (signed increments make componentwise-≥ rarer; the ordering-fraction column and pair guards are load-bearing prints, and a too-sparse row is flagged SPARSE and parking-ineligible, disclosed).
- **Intermediate ω (the hope, pre-registered):** a slowly drifting common direction produces positive SHORT-TIME association of increments (central concentration ⇒ F below the floor, toward round) while no FIXED linear functional dominates (the common direction itself rotates — there is no static two-clock collapse target). Registered shape: **F(ω) possibly non-monotone with a minimum at intermediate ω; PARKING = that minimum entering the round band with the realizer refusing and S₄ witnesses intact.** The registered kill: the association time-averages away and the curve runs monotonically from corner to floor — the family's last no-go, completing the arc.

## 3. Instruments (all carried from rounds 40–43, with the review-mandated upgrades)

F_iso (primary; PCA-3 + 64-direction sphere) with its RECEIPT-CARRIED REFERENCE CARD re-printed in-receipt as the calibration section (must match the 43b bands); native-F (continuity INFO; ω = 0 wiring); **F_2D (new, the collapse-robust secondary): supports in the top-2 PCA plane over a pinned 16-gon of directions, top-4/bottom-4 ratio** — reads in-plane anisotropy even when eig3 collapses; eigenvalue ratios; ordering fraction; pair counts; win d_MM (frozen curve; volume-proxy tags apply); in-window 2-realizer refusals; find_sk/verify_sk S₄ at candidates (full tries).

## 4. Grid and gates (fresh seeds 20262600+; 5 per point)

- Grid: ω ∈ {0, 0.1, 0.3, 1.0, 3.0, ∞} at the corner base (α = 0.75, per-channel churn, C = 3, N = 2048, Δ = 1024/NW = 256 windows for shape; Δ = 512 for the dimension metrics). One per-commit-Dirichlet β = 1 row as cross-round continuity INFO.
- **Gw0 (wiring):** ω = 0 windowed native-F reproduces the round-40 corner prints exactly (seeds 20262000+).
- **Gw0b (calibration):** the reference card re-run matches the 43b bands; the M4/orthant-4 F_iso anchors re-run match the round-43 bands (thresholds derive from the in-receipt anchor values).
- **Gw1 [MEASURED]:** the full ω-curve: F_iso, F_2D, native-F, eig3/1, fraction, pairs, win d_MM, win refusals — with SPARSE flags where pair guards fire.
- **Gw2 (parking certification):** candidates = F_iso ≤ 1.1 × max(M4 band) AND refusals ≥ 8/10 AND win d_MM ≥ 3.7 AND non-degenerate AND non-sparse; S₄ (full tries) — CONFIRMED at ≥ 3/5 seeds. F_2D must corroborate (≤ its M4-anchor-derived band × 1.1) — the collapse-masquerade veto.
- **Gw3 (the verdict; a read):** PARKING-EXISTS / LAST-NO-GO (no point reaches F_iso ≤ 1.2 × max(M4) with win d_MM ≥ 3.0 — completing the rounds-40–44 arc) / MIXED-FRONTIER.
- Exit 1 only on Gw0/Gw0b.

## 5. Scope and kill-risks

Occupancy, not geometry (the #104 scoping stands — the geometric cone is the orthant at every ω). Named kills: (K1) sparsification at high ω starves every instrument — the SPARSE flag is the honest exit, and windows may carry few related pairs even mid-dial (printed); (K2) negative χ values change the standardization's meaning — same affine applied everywhere, disclosed; (K3) the drift's finite-time association may produce F_2D/F_iso disagreement (planarizing clouds) — the card + F_2D veto adjudicate; (K4) d_MM volume-proxy caveats (two exhibits on record) — parking rides the realizer + S₄ witnesses.

## References

Rounds 40–43 (LEDGER #103–#112: the no-go arc, the card, the confound exhibits, the endorsed spec); note-3p1-dimension-ledger (the weak two-clock lemma; R-A + its supersession); dimwall_footprint/dialsweep{,_b}/cladder{,_b} (machinery, verbatim); the frozen mm_reference.json.
