# 3p1-manifoldweb — round 45: the grown channel-manifold web (growth vs the celestial-clock destination)

**Status:** design note, 2026-07-10 (v9 round 45; the LEDGER-#115 investigation's receipt-shaped question). Receipt: `v9/code/dimwall_manifoldweb.py` (pinned here, committed strictly before running). Reviews ON.

## 1. The question and the theory memo

The confetti probe (note-round-cone-mechanisms §2) proved the destination: K celestial clocks over a 4-dim latent space read ROUND by K ≈ 12–16 (F_iso 1.451 → 1.055 → M4's 1.046). The open physics: can GROWTH get there — or do growth correlations outrun the mechanism as they did at round 43? **The builder (pinned):** slots carry fixed preferred directions p_s ~ uniform(S²); a click at slot s draws u = p_s w.p. α else uniform(S²), magnitude e ~ Exp(0.109551); the K fixed clock directions v_k (Fibonacci sphere) each advance by **e · max(0, u · v_k)** (the half-cosine overlap); snapshots, per-clock churn (rate 1/L per clock, random victim), windows — all Lorentz-line conventions. Relation: b-strict ∧ all-K-clocks weak (dim ≤ K+1 by the weak lemma — now a feature: the bound grows with K). **The memo:** the half-cosine kernel on S² is monopole + dipole dominant in spherical harmonics (higher ℓ decay fast), so deposit displacements have a naturally ~4-dominant latent covariance (1 + 3) with small tails — the "many clocks, few factors" structure is geometric, not imposed. Registered risks: (K1) the monopole (every deposit advances most clocks) may act like the 42b common component — watch the collapse diagnostics; (K2) α-specialization may re-concentrate occupancy (the round-40 mechanism in directional form) — both α = 0 and 0.75 are on the grid; (K3) the win-d_MM rides the frozen 4-coordinate-family curve (volume-proxy tags apply); dimension claims ride refusals + witnesses.

## 2. Grid, anchors, gates (fresh seeds 20262800+; 5 per point)

- **Grid:** K ∈ {4, 8, 12, 16, 24} × α ∈ {0, 0.75}; (N, M, L) = (2048, 32, 16); F-window Δ = 1024/NW = 256; dimension window Δ = 512.
- **Gm0 (calibration):** the reference card + M4/orthant-4 F_iso anchors reproduce the 43/43b bands exactly; **the confetti K-curve reproduces the investigation note's numbers exactly (seeds 77000+, K ∈ {4, 8, 16, inf})** — the continuity anchor for this round (no byte-wiring to the one-hot classes exists: the deposit law is new, disclosed).
- **Gm1 [MEASURED]:** per grid point: F_iso, F_2D, native-(K+1)-frame F (INFO), eig spectrum ratios, pair counts, ordering fraction, win d_MM [volume-proxy], in-window 2-realizer refusals.
- **Gm2 (the witness ladder):** S₄ searches (tries = 8000, disclosed reduced; absence = not-found, never evidence of absence) at all K ∈ {4, 12, 16, 24} × both α; S₅ at K ≥ 12 points; S₆ INFO at K = 24 (tries 4000). The REGISTERED signature of the mechanism: max witness order GROWS with K (the corrected target's order-dimension-growth clause).
- **Gm3 (THE VERDICT; a read):** GROWTH-REACHES-ROUND iff some point has F_iso ≤ 1.1 × max(M4 band) AND refusals ≥ 8/10 AND win d_MM ≥ 3.7 AND S₄ found+verified ≥ 3/5 (non-degenerate, non-sparse). GROWTH-SPOILS iff no point reaches F_iso ≤ 1.2 × max(M4) with win d_MM ≥ 3.0. Else MIXED-FRONTIER (the K-trajectory printed against the confetti reference).
- **Gv1 (the F-covariance check [directional]):** order-only coordinates via the Johnston-style SVD embedding (top-4 singular vectors of the centered relation matrix, paper-14-cited); F computed on embedded coordinates; Spearman(F_native, F_embedded) across the 10 grid points ≥ 0.8 ⇒ the anisotropy is ORDER-READABLE (covariant, physical); below ⇒ the paper-XIV bookkeeping caveat FIRES and is recorded (F claims demoted to coordinate-facing pending stem-level instruments).
- Exit 1 only on Gm0.

## References

note-round-cone-mechanisms (LEDGER #115: the impossibility, the mechanism, the probe); v8 paper 14 (Thm 2.1 celestial clocks; §1 the detachment; Johnston SVD embeddings arXiv:2111.09331); rounds 40–44b (instruments verbatim; the card; the confound exhibits); the weak two-clock lemma (dim ≤ K+1); the frozen mm_reference.json.
