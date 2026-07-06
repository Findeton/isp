# ml3b-c — step (c): the sign readout (the campaign's falsifiable moment; conventions pinned before any sign is computed)

**Status:** design note, 2026-07-06 (v9 round 17; note-ml3b §2 G2's anchored semantics govern: the world is on the ODD branch — SELECTED-CORRECT = odd, SELECTED-WRONG = the locus refuted). Receipt: `v9/code/ml3b_c_sign_readout.py` (gates pinned here, committed pre-receipt). The four round-16 §3 obligations are discharged as pins §2.

## 1. The mode assignment (the disclosed import)

The CHSH four-cell structure needs two settings per party. The record-native realization, declared not derived (the mode import, the campaign's standing one): **each species' two settings = its scalar and pseudoscalar bilinear channels**, O_S = ψ̄ψ, O_P = ψ̄γ̂₅-compatible pseudoscalar (implemented as Γ_P = γ₅ at the source/sink insertions; the exchange itself runs through the four-fermi scalar vertex). The four cells: E_xy = the windowed connected correlator ⟨O_x^A O_y^B⟩ for (x, y) ∈ {S, P}², computed as

  `C^{xy}_AB(u, v) = g_x · Σ_z Π_A^{x,S}(u, z) Π_B^{S,y}(z, v)`,  `Π^{a,b}_s(u, v) = −Tr[Γ_a S_s(u, v) Γ_b S_s(v, u)]`.

The flux backgrounds (Q_A, Q_B) = (0, 1) break parity in the B sector — the P-channels need not vanish; whether they are large enough to define the cells is Gc1's question. **The parity bit:** π = sign(E_SS · E_SP · E_PS · E_PP) — the gauge-invariant CHSH-class label from ml3a (odd = Bell-violation-capable).

## 2. The four pinned conventions (the round-16 inheritance, discharged)

1. **Zero-mode convention:** the correlator propagators are **zero-mode-subtracted** (S → S − S·P₀ per species with topological zeros), matching the gap side's §4 convention — ONE convention across the whole construction. The full-propagator variant is printed as INFO (the round-16 sensitivity on record).
2. **Windows:** E_xy computed on the pinned window set **{w = 1 (d ≤ 1), the d = 1 shell alone, d ≤ 2}**. Any SELECTED verdict requires the parity to **agree on all three windows** (the round-16 lesson: the contact term can own w-inclusive signs).
3. **Vertex sign:** g_x > 0 (the mass-reinforcing orientation, step (a)) is the reference; the parity under g_x → −g_x is printed — if π flips with sign(g_x), the verdict is **RELOCATED** (the import moves to the sign of g_x; reported as such per note-ml3b G2).
4. **Estimators:** E_xy = mean of C^{xy}_AB over the window, exactly as coded; parity is sign-only, so the §4 normalization does not block this step (magnitudes remain uninterpreted).

## 3. Pinned gates and verdict semantics

- **Gc1 (the cells exist):** all four |E_xy| > 1e-14 on the w = 1 window at (g², g_x) = (4, ½), sectors (0, 1). REFUSED ⇒ **KINEMATIC-NULL**: the S/P assignment cannot express the four cells on these backgrounds — the mode assignment redesigns (a different bilinear pair or sector pair); not a locus kill.
- **Gc2 (THE PARITY — the falsifiable gate):** π computed on all three windows, at g_x ∈ {¼, ½}, with the zero-mode-subtracted convention. **SELECTED** requires: all three windows agree AND both g_x values agree. Then: **SELECTED-ODD ⇒ the construction+assignment class derives the empirically correct (Bell-violation-capable) sign — the campaign's success condition. SELECTED-EVEN ⇒ the GW-flow locus with this assignment is REFUTED (note-ml3b G2's kill; the fallback activates).** Window-disagreement ⇒ **WINDOW-CONTINGENT** (not selected — honest inconclusive; the finding names which window class flips). g_x-flip sensitivity ⇒ RELOCATED (convention 3).
- **Gc3 (kinematic vs dynamic — the discriminator, printed + adjudicated):** the parity recomputed at the free-field point (masses set to the g_x = 0 single-species values, exchange amputated to the same diagram at fixed masses) and at a second coupling point (g² = 2, g_x = ¼ — the coupled system re-solved). **KINEMATIC-π** (invariant across all points incl. free) = the γ-algebra + backgrounds force it given the assignment — for π = odd this is the *strongest* form (the class cannot express the Bell-satisfying sign); **DYNAMIC-π** (coupling-dependent) = the dynamics selects. Either, if odd-and-robust, is SELECTED-CORRECT; even-and-robust in any form is the refutation.
- **INFO prints (unpinned):** the full-propagator variant's parity; the four signed E_xy per window; an alternative-assignment probe (the vector bilinear pair Γ ∈ {γ₁, γ₂} in place of {1, γ₅}) — the assignment-dependence on record for the review.

## 4. Honest scope

The verdict is conditional on the declared mode assignment (S/P) and the sector pair — the assignment IS the mode import, and the alternative-pair INFO print measures how much rides on it. Tree-level exchange (the dressing class = the standing §4 obligation; the σ-pole argument suggests sign-stability under RPA dressing but this is NOT claimed). L = 6, float64 on the correlator layer (sign robustness against float noise is Gc1's 1e-14 floor vs the measured 1e-4..1e-1 scales). Large-N, 2d, quenched — paper 5's scope verbatim. **What a SELECTED-ODD here would and would not mean:** it would be the first time the record-native matter construction produces the empirically-correct Bell-class sign from its own dynamics/algebra — at toy scale, under a declared assignment; it would NOT yet be "the theory derives Bell violation" (the assignment import, the scale, and the dressing class all stand between).

## References

note-ml3b (G2's anchored semantics: the world is odd); note-ml3b-a §4 (the conventions this note discharges); note-ml3b-b §3 (the four inherited obligations); ml3a + rounds 11–12 (the parity bit; the gauge orbits); v8 paper 5 (the operator machinery; the scope); v8 paper 3 (the mode wall — why the assignment is an import); LEDGER #67–#68.
