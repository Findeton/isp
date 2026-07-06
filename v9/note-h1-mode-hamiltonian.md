# h1 — the mode-selecting Hamiltonian: the orbit-splitting reduction and this route's one shot

**Status:** design note, 2026-07-06 (v9 round 22; PLAN line 3, FUNDED). Receipt: `v9/code/h1_mode_hamiltonian.py` (pinned here, committed strictly before the receipt). Token-restricted mode: the reserved hostile review fires on **any SELECTED** (odd or even); a split stands unreviewed. Registered [directional]: odd (the standing empirical anchor; disclosed as always, weak). One shot per the propagated clause.

## 1. Why a Hamiltonian route evades the crossing disease

Paper 5's four adjudications all failed through one mechanism: the sign was read off *windowed correlator values* that drift through zero inside the accessible grid. The Hamiltonian route changes the observable's type: the parity becomes a **discrete selection between ml3a's two gauge orbits** (odd/even), decided by which orbit minimizes a derived effective potential. A classification cannot drift; the residual risk is only that the *deciding coefficient* itself changes sign in the grid — and that coefficient is ONE algebraic number per point (no windows, no estimator pair, no distance structure), so the protocol has no estimator axis left to split on.

## 2. The reduction (derived, three steps)

**(i) The discriminator is the four-cell product — a little lemma.** ml3a's gauge acts as E_xy → s^A_x s^B_y E_xy (local setting/outcome sign flips, s = ±1). Quadratics Σ E²_xy are invariant; every cubic cell-monomial picks up uncancelled s-factors and is forbidden from any gauge-invariant functional; the quartic ∏_xy E_xy is invariant (each s appears squared). So the FIRST orbit-discriminating term of any gauge-invariant effective potential is κ_Γ·∏E — and on the ml3a manifold (equal magnitudes |E| = c/2 forced), |∏E| = (c/2)⁴ is orbit-independent: **the two orbits differ only through the sign of the quartic product term.**

**(ii) The coefficient is minus the fourth joint cumulant.** Couple sources to the four global cell charges q_xy = Σ_z O^A_x(z) O^B_y(z) (the seal-locus cell operators; O^A_S = ψ̄(1−D/2)ψ etc. — the standing improved content). W(λ) = log⟨exp Σλ_xy q_xy⟩; the effective potential is the Legendre transform Γ(q̄), and at leading connected order Γ⁽⁴⁾ = −W⁽⁴⁾ = −cum₄(q_SS, q_SP, q_PS, q_PB)|_mixed (the W₃-mediated Legendre corrections are excluded at this order — this route's dressing-class boundary, disclosed; by the lemma in (i) they are also cubic-cell objects and gauge-non-invariant in isolation). So Γ ⊃ −cum₄·C·∏E with C > 0 combinatorial.

**(iii) The selection rule.** Equilibrium selection = Γ-minimization (the standard Euclidean premise, disclosed as such). Minimizing −cum₄·C·∏E over the two orbits picks sign(∏E) = sign(cum₄):
  **cum₄ > 0 ⇒ ∏E > 0 selected ⇒ SELECTED-EVEN;  cum₄ < 0 ⇒ SELECTED-ODD.**
The entire question is the sign of one derived number.

## 3. The pinned object: κ_box

The leading fully-connected topology of the mixed fourth cumulant is **box×box**: each species contributes one closed 4-insertion fermion loop, the two loops sharing all four seal sites. The two loop signs cancel ((−1)² = +1), so
  κ_box = Σ_{σ,τ} Σ_{z1..z4} tr[Γ^A-chain along σ] · tr[Γ^B-chain along τ]
summed over all 6 × 6 cyclic insertion orderings per species (the full symmetrization — no aligned-only truncation), with A-side insertions (1, 1, γ₅, γ₅) and B-side (1, γ₅, 1, γ₅) in the cell-label order (SS, SP, PS, PP), legs K = (1 − D/2)S at the FULL propagator (the standing principled choices, carried). Excluded and named (this route's next order): jointly-connected topologies where one species' four-point factorizes into two-loops or carries tadpole insertions. Each κ_box evaluation is an exact tensor-network contraction (einsum; ~V³ intermediates) — one number per grid point, machine-precision algebra, no statistical layer.

## 4. Pinned gates

- **Gh1 (wiring):** at L = 3 (V = 9), the einsum route matches an independent brute-force nested-site-loop Wick sum (explicit 2×2 spinor chains over all 9⁴ site tuples and all 36 ordering pairs) to relative 1e-10, at the L = 3 solved masses (g² = 4, g_x = ½).
- **Gh2 (existence):** |κ_box| > 1e-14 at all six grid points {L = 6, 8, 10} × {g_x = ¼, ½} (masses re-solved per point from the step-(a) system).
- **Gh3 (THE SELECTION — this route's one shot):** sign(κ_box) unanimous over all six points ⇒ **SELECTED-ODD-H** (κ_box < 0) **or SELECTED-EVEN-H** (κ_box > 0), each graded [DERIVED given the matter sector; leading connected topology; the S/P assignment import; the equilibrium-selection premise] — the reserved hostile review fires before any grade is recorded. **Any sign split ⇒ FAILS-AT-H-LEADING**: the deciding coefficient itself crosses in the grid — the strongest evidence yet that the construction as built does not fix the bit, closing the funded continuations.
- **INFO (unpinned):** κ_box per point; the aligned (σ = τ) vs twisted shares; imaginary-part sanity (the summed object should be real up to roundoff); the g_x = 0 decoupled row; the per-L trend.

## 5. Honest scope

The S/P channel assignment remains the mode import (unchanged, disclosed). The selection premise is Euclidean equilibrium (Γ-minimization); a dynamical-selection alternative is out of scope. κ_box is the leading connected topology of the exact discriminator — the analog, in this route, of step (b)'s tree exchange; its named next order is the excluded-topology family. A SELECTED here is a one-coefficient, protocol-tight statement — and precisely because the observable is one number with no estimator freedom, a refusal here (a sign flip across six points) would be close to conclusive that the parity is not determined by this construction at any accessible object, sharpening paper 5's terminal statement into its final form.

## 6. Pre-rerun amendment (2026-07-06, committed before any κ was computed)

The first run exited at the L = 3 gap solve: the coupled system has **no positive root at L = 3** (g², g_x) = (4, ½) — a small-lattice feature (output on record; no κ value was ever evaluated). The wiring gate's purpose is mass-agnostic — it verifies that the einsum network and the brute-force Wick sum compute the same object from IDENTICAL inputs — so Gh1 now runs at pinned reference masses (M_A, M_B) = (0.9, 0.8) at L = 3. Nothing else changes; the grid, Gh2, Gh3, and all semantics are untouched. This amendment cannot be data-tuned: no κ_box number existed anywhere when it was committed.

## 7. The reserved review (2026-07-06 — VOIDED-AT-LINK-2; the disposition applied)

The SELECTED-EVEN-H reading is **voided at §2(ii), the Legendre step** — and it does not flip to ODD: the referee computed the exact objects this note truncated, at the receipt's own masses, and found: (MAJOR-1) the exact mixed cum₄ of the **pinned (uncentered) charges is negative grid-wide** (−2.8e-2..−4.7e-2 vs κ_box +1.4e-3..+4.1e-3) — the excluded tadpole families, fed by the nonzero condensate and topological-density means, are 12–19× the box and reverse it; "leading fully-connected topology" is measured false. (MAJOR-2) the W₃ exclusion is wrong-shaped — the W₃W₂⁻¹W₃ trees land in the invariant ∏E slot, W₃ ≠ 0 in both schemes (max |cum₃| ≈ 5e-2), the trees are 0.7–2.3× the amputated-W₄ piece, and **the exact Γ⁽⁴⁾ splits inside the grid** (+5.39 / −7.62 / +2.29 / +6.62). (MAJOR-3) the reduction lemma's mathematics is verified but its license fails for the actual non-invariant Γ; orbit-averaging restores it exactly — and then the selector is the exact Γ⁽⁴⁾, which splits. (MAJOR-4) centered vs uncentered charges give opposite stable simplified verdicts (ODD 4/4 vs EVEN 4/4) — the object was not pinned tightly enough to carry a verdict. (MINOR-1) "C > 0 combinatorial" false as argued (two of four Grassmann "variances" are negative; it held by parity of the count); the minimization algebra itself is correct. (MINOR-2) the Gh3 check conflates a decisive EVEN with a refusal (template note). What SURVIVES: κ_box confirmed (independent implementation, rel 1.4e-7/1.0e-8; loop signs and counting re-derived from scratch by exact Berezin integration — coefficient +1, no over/under-counting); Gh1/Gh2; the freeze (anti-tuning verified: the registered direction was ODD, the raw result EVEN, the exact completion voided both); and the q̄ ↔ E map adjudicated SAFE by a nice little theorem (any per-party factorized map contributes (∏N)² > 0 to the parity — no factorized map can flip it).

**Disposition (applied at LEDGER #81):** Gh1/Gh2 stand; κ_box > 0 stands as a CONFIRMED measured number; the grading is **FAILS-AT-H-EXACT** — the crossing disease this route was designed to evade relapses at the first exact completion of its own object. The construction does not determine the bit at the Hamiltonian object either; paper 5's terminal statement extends to this route in its "no accessible object selects" form.

## References

Paper 5 (the arc; §7's Hamiltonian registration and its crossing-immunity rationale); ml3a + the round-11/12 corrections (the manifold, the gauge, the equal-magnitude law, the orbits); note-ml3b (the fallback's original registration); notes ml3b-e/f (the improved content and full-propagator resolutions carried); PLAN §post-round-20 (the funded line; the reserved-review rule); LEDGER #77–#79.
