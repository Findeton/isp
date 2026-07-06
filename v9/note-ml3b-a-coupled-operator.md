# ml3b-a — build-step (a): the two-species coupled record GW system; G4 first (the cheapest kill)

**Status:** build note, 2026-07-06 (v9 round 15; note-ml3b §3's sequencing — step (a) of the one-sign machine). Receipt: `v9/code/ml3b_a_coupled_operator.py` (gates pinned here, committed before the receipt exists — freeze discipline). Machinery: paper 5's production receipt `v8/code/s_igw_production_gap_flow.py`, functions extracted verbatim (no import guard in the source; the port pattern of u1/s5).

## 1. The object

Two record species A, B, each on its own record GW/overlap operator (paper 5's construction: flux sector Q_s, the Lüscher-correct massive operator `D(M) = D + M(1 − D/2)`, the deformed generator `γ̂₅ = γ₅(1 − D)`), coupled by the **scalar-channel cross four-fermi term at seals**, which at large N becomes the coupled gap system

  `M_A = g²·Σ_A(M_A) + g_x·Σ_B(M_B)`,  `M_B = g²·Σ_B(M_B) + g_x·Σ_A(M_A)`

with Σ_s the Lüscher-subtracted condensate (paper 5's closed eigenvalue sum). g_x is the sector's one new dial (disclosed import, per note-ml3b §2). The step-(a) questions, in kill order: does the coupling **break exact chirality** (if yes, the GW-flow locus dies here — the cheapest kill); and is the coupling **sterile** (zero cross-susceptibility — the locus produces no cross-dependence; the fallback activates).

## 2. Pinned gates

- **G4c (exact-chirality survival under coupling — the kill gate).** At dps = 120, lattice L = 4 (32-dim; small-lattice disclosed — the identities are algebraic, size-free), sectors Q ∈ {0, 1}: (i) the GW identity `‖{γ₅, D} − Dγ₅D‖_max < 1e-90` and the Lüscher Ward `‖Dγ̂₅ + γ₅D‖_max < 1e-90` per species (paper 5's standard re-asserted on this build's operators); (ii) **the coupled-mass Ward breaking is EXACTLY `M_s·(γ₅ − s)`**: `‖(D(M_s)γ̂₅ + γ₅D(M_s)) − M_s(γ₅ − s)‖_max < 1e-90` per species **at the coupled masses** (M_A, M_B) from Ga2's anchor solve — the cross-coupling enters only through the scalar mass values and adds no new chirality structure, *algebraically*. REFUSED ⇒ the coupled construction breaks exact chirality ⇒ step-(a) kill, the mode-selecting-Hamiltonian fallback activates (note-ml3b §2 G1-kill semantics).
- **Ga2 (existence + cross-susceptibility).** At L = 6 (disclosed; paper 5's anchors live at ≤ 10×10), (Q_A, Q_B) = (0, 1), g² = 4 (the paper-5 anchor coupling): the coupled system solves with M_A, M_B > 0 at g_x ∈ {0, 1/4, 1/2} (dps ≥ 60 scalar Newton on the closed eigenvalue sums; the g_x = 0 column must reproduce the single-species masses — the continuity anchor); **the cross-susceptibility |ΔM_A/Δg_x| over [0, 1/2] exceeds 1e-6**. Registered expectation [directional]: positive (the scalar cross term is mass-reinforcing). REFUSED-sterile ⇒ the scalar channel produces no cross-dependence ⇒ redirect per note-ml3b §2's G1-kill. A symmetric control column (Q_A = Q_B = 1) is printed unpinned.
- **Verdict semantics:** house convention (refusals print the ledger, exit 1 by design); eigenvalues are [LATTICE-NUMERIC, FLAGGED] per paper 5; the mass values [DERIVED given the matter sector: large-N, 2d, quenched, small lattices, mode-relative — paper 5's scope block inherited verbatim; NOT the Clay gap].

## 3. What step (a) does NOT do (the sequencing contract)

No sign readout (step (c): the four-cell mode-pair structure — needs the mode-assignment design, the campaign's known import); no correlator-decay measurement (step (b)); no claim that the coupled masses ARE χ_AB (the readout map is rung-1's estimator pointed at step-(b) correlators). Step (a) is the existence-and-survival gate: the cheapest kills first.

## References

note-ml3b (§2 the machine + G-gates; §3 the sequencing); v8 paper 5 (§3 the interacting flow; the Lüscher standard < 1e-90; the scope block; the anchors 0.762/0.886/0.787 at g² = 4); `s_igw_production_gap_flow.py` (the extracted machinery: flux_links/wilson/overlap_float/overlap_hp/msign_hp/build_sigma_extended); ml3a + round-11/12 corrections (the one-bit target; the empirical ODD anchor); LEDGER #59–#64.
