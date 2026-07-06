# ml3b-b — build-step (b): the connected cross-species correlator (the live kill: existence + decay)

**Status:** build note, 2026-07-06 (v9 round 16; note-ml3b §3 step (b); the §4 conventions of note-ml3b-a govern). Receipt: `v9/code/ml3b_b_correlator.py` (gates pinned here, committed pre-receipt).

## 1. The object

At the step-(a) coupled masses (L = 6, sectors (Q_A, Q_B) = (0, 1), g² = 4; the zero-mode-subtracted-both-channels convention), the **connected cross-species scalar-density correlator at leading connected order** — the one-contact exchange through the four-fermi vertex:

  `C_AB(x, y) = g_x · Σ_z Π_A(x, z) Π_B(z, y)`,  `Π_s(u, v) = −Tr_spinor[S_s(u, v) S_s(v, u)]`,

with S_s = (D_s + M_s(1 − D_s/2))⁻¹ the massive overlap propagator at the coupled mass M_s. The correlator inherits its range from the dynamical masses — the ml1 shape (nonzero at seals, decaying with distance) is the live prediction. **Disclosures:** leading connected order only (O(g_x) exchange; O(1/N) pieces not computed); float64 (a decay-shape measurement, not a near-vacuum identity); the operator-level chirality kill is NOT live at this order (the coupling still enters through masses + contact exchange — the mean-field+exchange class; per the round-15 lesson, no survival rhetoric will attach to gates that cannot fail).

## 2. Pinned gates

- **Gb1 (existence + decay — THE live kill):** on the L = 6 torus with L1 distance (per-axis wrap at 3), the distance-binned mean |C_AB| over bins d ∈ {0, 1}, {2, 3}, {4–6} is **strictly decreasing** AND the far bin < 0.5× the near bin, at g_x = ½. |C_AB| at the near bin > 1e-12 (well above float noise). REFUSED ⇒ the channel produces masses but no communication ⇒ **step-(b) kill**, note-ml3b's fallback activates.
- **Gb2 (mass-scale consistency) [directional]:** the fitted exponential rate of the binned envelope lies within a factor 3 of 2·min(M_A, M_B) (the two-propagator exchange decays at the summed lighter gap; the loose band owns L = 6 lattice artifacts).
- **Gb3 (the derived-χ readout):** `χ̂_AB` = the seal-window sum (w = 1: mean of C_AB over d ≤ 1), printed with sign and magnitude; **pinned only nonzero-and-finite** — the magnitude interpretation awaits the Lagrangian normalization (note-ml3b-a §4); NO claim that χ̂ equals the physical χ_AB (note-ml3b-a §3's disclaimer carried).
- **Gb4 (the g_x scaling) [directional, printed]:** C_AB at g_x = ¼ vs ½ — ratio expected > 1 and below 2 (linear-in-g_x at fixed masses, sublinear once the masses' own g_x-dependence enters; measured, not gated).

## 3. Review corrections (2026-07-06, the round-16 review — applied; gates stand as pinned, the narrative corrected)

- **MAJOR-1 — the "1% match" was bin-choice luck, withdrawn as a headline.** The per-distance local rates (4.06, 3.43, 0.48, 0.25, 0.57, 0.28) never pass through 1.54 anywhere on the lattice; defensible estimator definitions spread 0.24×–2.63× of the target; at L = 8 the same bins give 1.25×. The near bin is 94% d = 0 contact term. **The honest statement: the rate is consistent with the two-propagator scale within the pinned 3× band** (Gb2's actual gate — which is definition-robust and held); the min(2M) reasoning is right in principle (the convolution inherits the slower two-particle threshold), but no estimator on an L = 6 torus can measure it to 1%. Lesson (MINOR-5): estimator definitions get pinned with the gate henceforth.
- **MAJOR-2 — the correlator-side zero-mode convention was silent, and the far tail is convention-sensitive.** The gap side uses the zero-mode-subtracted bulk (the §4 convention); the correlator used the FULL propagator, undisclosed. The signed profile oscillates (d = 1 shell 100% negative: +2.10e-1 / −3.64e-3 / −1.18e-4 / +7.3e-5 …) — the pinned |C| binning is what renders a monotone decay. Under zero-mode-subtracted S_B the far bin moves 3–5× and the strict-decrease conjunct is fragile (the review's rank-1 split: REFUSES; this receipt's eigenprojection variant: holds marginally at far/mid = 0.84 — both now printed as INFO). Gb1 as pinned passed and stands; **the step-(c) pin must fix the correlator-side zero-mode convention and own the sign structure.**
- **MAJOR-3 — χ̂'s "+" is window-contingent** (d = 0 contact dominates; the d = 1 shell is negative) — reported without caveat in LOG/LEDGER #67, now corrected: the sign at w = 1 is a contact-term artifact class; **the vertex-sign and window conventions are step-(c) pin obligations** (with the §4 normalization), since step (c) IS the sign readout.
- **MINOR-4 —** "O(1/N) pieces not computed" mischaracterized the truncation: the RPA/self-channel chains are leading-order in 1/N and O(1) at g² = 4 — the receipt computes the **tree-level exchange**; the dressing class joins the §4 convention obligations (the review notes the σ pole sits at the 2M threshold, so Gb2's scale survives dressing). The diagram's combinatorial factor is exactly 1 (review-verified), the spinor-trace index convention and loop sign correct, Hermiticity at 9e-18.

**What stands:** all three gates at their pinned definitions; the correlator exists with genuine spatial structure; χ̂ = +3.90e-2 as a defined-window number; the g_x scaling; the diagram form. **What step (c) inherits as pin obligations: the zero-mode convention (both sides), the window/vertex-sign conventions, the estimator definitions, and the dressing-class disclosure.**

## References

note-ml3b(-a) (+§4 conventions); paper 5 (the propagator machinery); ml1 (the estimator shape this readout instantiates); LEDGER #65–#66.
