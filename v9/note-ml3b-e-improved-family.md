# ml3b-e — the sign readout at the chirally-consistent (improved-bilinear) assignment family: this family's one shot

**Status:** design note, 2026-07-06 (v9 round 19). Receipt: `v9/code/ml3b_e_improved_family.py` (pinned here, committed strictly before the receipt). Admissibility: the round-18 clause closed the tree/L = 6 chapter for the NAIVE family and named "a different assignment family argued independently" as an admissible structural move — this note is that move, and the clause propagates: **one shot per family.**

## 1. The independent argument (data-free, twice over)

1. **Chiral covariance.** On a GW lattice the densities that transform covariantly under the exact (Lüscher) chiral symmetry are the improved bilinears ψ̄ Γ (1 − D/2) ψ — the standard overlap-fermion construction. The naive Γ ∈ {1, γ₅} insertions of rounds 17–18 are not covariant densities of the symmetry this machine is built on.
2. **Internal consistency.** Step (a)'s gap equation prices Tr[(1 − D/2) S] — the machine's masses are DEFINED by the improved scalar density. The seal vertex therefore already IS the improved density; using naive insertions at source and sink made the correlator operators inconsistent with the machine's own operator content. The improved family is the one the construction had implicitly chosen.

Both arguments were available at round 15 (step (a)'s own receipt contains the (1 − D/2) trace); neither depends on any sign ever measured.

## 2. The receipt (everything held fixed except the family)

Bubbles with **K = (1 − D/2) S** in place of S (source, vertex, and sink all improved — full consistency): Π^{ab}(u, v) = −Tr_spinor[Γ_a K(u, v) Γ_b K(v, u)], Γ ∈ {1 (S-channel), γ₅ (P-channel)}. Zero-mode convention: subtraction on the propagator then improvement (K_sub = (1 − D/2) S_sub) — exactly the gap side's subtraction of the zero modes from the same trace. All else verbatim from ml3b-d: sectors (1, 2), masses from the step-(a) coupled solve, the principled estimator pair E1/E2 (note-ml3b-d §2 — the standing principled choice, carried unchanged), exchange C^{xy} = g_x Π_A^{x,S} @ Π_B^{S,y}.

## 3. Pinned gates

- **Ge1 (cells exist):** all eight |E{1,2}_xy| > 1e-14 at (4, ½) subtracted. REFUSED ⇒ SEPARATION-NULL for this family (redesign; not a locus kill).
- **Ge2 (THE FAMILY'S ONE SHOT):** the 8-way protocol verbatim — {E1, E2} × {g_x = ¼, ½} × {subtracted, full}; unanimity ⇒ **SELECTED-ODD** (the chirally-consistent record construction derives the empirically correct Bell-class sign at tree level/L = 6) or **SELECTED-EVEN** (the GW-flow locus under its OWN consistent family is refuted — a much harder kill than round 18's, since no operator-choice freedom remains); any split ⇒ FAILS-AT-THIS-ORDER for this family, closing it irrevocably (the structural options then shrink to: RPA dressing, the Hamiltonian fallback, new order/scale).
- **Ge3 [directional, printed]:** (i) the convention fragility narrows — the sub/full E1 disagreement of the naive family is expected to shrink or vanish (the improvement suppresses the doubler side of the GW circle and matches the gap-side subtraction exactly); (ii) the free point and the (4, −½) root reproduce the anchor pattern. INFO: both conventions' distance tables (the round-18 MINOR-1 lesson — both from the first run); the naive-family cells alongside for the record.

**Registered expectation [directional]:** if unanimity obtains, odd (the standing empirical anchor); the fragility reduction (Ge3-i) is the mechanism-level registration. The parity outcome is genuinely open — the improvement changes every bubble, including the previously-stable E2 legs.

## 4. Honest scope

All of note-ml3b-d §5 verbatim (tree exchange, L = 6, large-N, 2d, quenched, sectors (1, 2)). The S/P **channel labels** remain the mode import; what this family removes is the operator-level arbitrariness *within* the channels (the covariant densities are unique up to normalization, which cancels in signs). A SELECTED here inherits the same "not yet a Bell derivation" caveats; a kill here is graver than round 18's split — it would refute the locus at its own consistent operator content.

## References

note-ml3b-d (+§6) and `ml3b_d_one_shot.py` (protocol + machinery, verbatim); note-ml3b-c §6 (the corrected zero-mode form); note-ml3b-a §2/MINOR-3 (the gap-side (1 − D/2) trace — the consistency argument's source); v8 paper 5 (the Lüscher standard); LEDGER #71/#73.
