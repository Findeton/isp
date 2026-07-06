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

## References

note-ml3b(-a) (+§4 conventions); paper 5 (the propagator machinery); ml1 (the estimator shape this readout instantiates); LEDGER #65–#66.
