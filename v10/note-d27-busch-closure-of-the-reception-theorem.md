# D27 — the Busch closure of the reception theorem: the thermal receiver and the corrected characterization

**Status:** PIN (pre-receipt), 2026-07-12; committed before `code/d27_busch_thermal_receiver_exact.py` runs. Provenance labels per D20. Campaign context: the assembly round's M4 (physics stream) — repair executed constructively per its O2.

## 1. The defect and the repair

D25 stated "admitted closures = exactly the isometric dilations `V rho V†`" and bridged via Wigner/Kadison/Molnár — theorems whose hypotheses include surjectivity, which the campaign's closures (8-dim into 16-dim) do not satisfy. The correct non-surjective theorem is **Busch, "Stochastic Isometries in Quantum Mechanics", Math. Phys. Anal. Geom. 2, 83 (1999) [LITERATURE]**: trace-norm-isometric stochastic (positive, trace-preserving) maps are exactly the convex combinations `rho -> sum_k p_k V_k rho V_k†` of isometries with mutually orthogonal ranges. This class is strictly broader than a single isometric dilation — and the physically load-bearing member is the **thermal receiver** `rho -> U(rho (x) sigma_mixed)U†` (dispersal into a receiver in a mixed state — the paradigm laboratory environment), which preserves every trace distance yet maps pure states to mixed ones. The corrected NSE characterization:

> Admitted closures are, by Busch's theorem, exactly the mixtures `sum_k p_k V_k rho V_k†` with orthogonal ranges — isometric dilations up to a fixed, **preparation-independent classical flag** (which branch k fired). The flag distribution carries no content (it is independent of the preparation; it receives nothing); the dispersal reading is unchanged.

## 2. Receipt gates (`code/d27_busch_thermal_receiver_exact.py`; stdlib Fractions; exit 1 on any failure)

- **B0 (instrument upgrade, self-gated):** the exact trace-distance certificate is strengthened from D25's single-pair spectrum test to the identity `Delta^3 = c·Delta` (verified entrywise, exact) — which certifies spectrum ⊆ {0, ±sqrt(c)} — with `||Delta||_1 = tr(Delta^2)/sqrt(c)`; the D25 cases re-verified under the new certificate (backward compatibility gate).
- **B1 (the thermal receiver preserves):** `T(rho) = U(rho (x) sigma_mixed)U†` with `U = CNOT(A->E)`, `sigma_mixed = I/2`: every pairwise trace distance (eta pairs and the diagonal pair) is preserved EXACTLY.
- **B2 (it is no single isometry):** T maps the pure GHZ state (eta = 1) to purity exactly 1/2 — pure to mixed, so `T ≠ V rho V†` for any isometry V. Together with B1: the D25 characterization sentence is refuted by exhibit, exactly as the review found; the Busch form is verified — T decomposes as `1/2 V_0 rho V_0† + 1/2 V_1 rho V_1†` with the two isometry ranges mutually orthogonal (checked exactly).
- **B3 (the flag receives nothing):** the branch weights are (1/2, 1/2) for every preparation in the family (eta grid and diagonal preparations) — preparation-independent; the flag marginal carries zero content distinction.
- **B4 (NSE verdicts unchanged under the upgraded instrument):** C_bare, C_half, R_cl still strictly contract; U, Q_disp, and now T preserve — the admitted class is the Busch class, and every exclusion of D25 stands.

## 3. What this does and does not claim

**Does:** close the reception theorem at cited-theorem grade for non-surjective closures (Busch 1999), with the paradigm mixed-environment dispersal as an in-family member; correct D25's characterization sentence (supersession recorded with the assembly-round LEDGER entry); leave every D25 exclusion and the falsifier untouched.
**Does not:** re-prove Busch's theorem (cited, verified on-family); extend beyond the declared family; alter the D21 ladder falsifier or the attribution gate.

## 4. Round-1 outcomes (fronts pinned above; 2026-07-12; LEDGER #130)

(F1) **SOUND:** the certificate class is proven in review (the D25 moment form: tr D³ = 0 ∧ (tr D²)² = 2 tr D⁴ ⇒ spectrum exactly {x, −x}; the Δ³ = cΔ form certifies spectrum ⊆ {0, ±√c} directly); the failure mode is fail-closed (None ⇒ visible gate failure) — no silent uncertification. (F2) **ADEQUATE:** all states and isometries here are real matrices in the computational basis; the Euclidean inner product is the Hilbert–Schmidt one restricted to real vectors — verified V†V = I and V₀†V₁ = 0 exactly. (F3) **GATED:** B3 checks both the branch weights (½, ½ for every preparation) and the E-flag marginal (preparation-independent) — the joint concern is covered by B1's total-distance preservation together with B3's marginal checks.
