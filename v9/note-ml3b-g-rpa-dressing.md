# ml3b-g — the RPA dressing: the σ-pole sign object (this route's one shot)

**Status:** design note, 2026-07-06 (v9 round 21; PLAN §post-round-20 line 2 — the funded continuation). Receipt: `v9/code/ml3b_g_rpa.py` (pinned here, committed strictly before the receipt). Token-restricted mode: the reserved hostile review fires ONLY on a SELECTED outcome; refusals stand unreviewed. Registered [directional]: odd (the standing record's direction, disclosed as always); mechanistic registration: pole dominance should REDUCE the E1-vs-E2 spread (printed).

## 1. The object

The tree-level exchange C = g_x Π_A Π_B failed adjudication because the dominant cell crosses zero inside every pinned grid (paper 5 §6). RPA resums the bubble chains so the cells are σ-channel-dressed (RPA-resummed); the original framing — cells dominated by the σ-pole, a structurally different sign object located away from the crossings — survives only as the pre-receipt registration, labeled as such (§4: the measured dressing is a bounded ~20% correction, nowhere near a pole). With P_s = Π_s^{SS} the improved scalar-scalar bubble (full propagator — the standing principled content, r20), the Hubbard–Stratonovich pair (σ_A, σ_B) has bare propagator G = [[g²I, g_xI], [g_xI, g²I]] over species⊗sites and polarization Π = blockdiag(P_A, P_B); the dressed propagator is

  **D_σ = (I − GΠ)⁻¹ G**,  and the dressed cells are **C^{xy}_RPA = Π_A^{x,S} · [D_σ]_{AB} · Π_B^{S,y}**.

Leading order reproduces tree exactly ([D_σ]_{AB} = g_xI + g²g_x(P_A + P_B) + …). The sign convention is derived, not gate-certified: the loop-minus Π branch — Π entering (I − GΠ)⁻¹ with the fermion loop's minus sign — is the branch whose expansion reproduces the step-(a) four-fermi structure, with the O(2) term +g²g_x(P_A + P_B) receipt-gated (§4); the stability spectrum does not adjudicate it (§4: the flipped convention is also stable at every run point).

## 2. Pinned gates

- **Gr1 (wiring + convergence):** (i) with D_σ truncated to g_xI the code path reproduces the tree cells to machine precision; (ii) at the anchor with G scaled by 1/8 (masses held fixed — a pure algebra check), the closed form (I − GΠ)⁻¹G matches the partial geometric sum (K = 40) to relative 1e-12.
- **Gr2 (RPA validity):** min Re eig(I − GΠ) > 0 at ALL four run points ({g_x = ¼, ½} × {L = 8, 10}, masses re-solved per L from the step-(a) system). REFUSED at any point ⇒ **RPA-INVALID** — the dressing is inapplicable at the accessible couplings; terminal for this route (no coupling-shopping).
- **Gr3 (THE DRESSED ADJUDICATION — this route's one shot):** the parity on 8 legs = {E1, E2} × {g_x = ¼, ½} × {L = 8, 10} on C_RPA, full convention, improved family. **Unanimous ⇒ SELECTED-ODD-DRESSED** (the record-native construction derives the empirically correct Bell-class sign at the resummed order — the reserved hostile review then fires before any grade is recorded) **or SELECTED-EVEN-DRESSED** (the locus refuted at the dressed order). **Any split ⇒ FAILS-AT-RPA**: the sign question exits the perturbative/resummed reach of this construction; the registered continuations reduce to the Hamiltonian fallback and ml4.
- **INFO (unpinned):** the σ-spectrum (min eig per point — the pole gap); per-distance tables at the anchor; the subtracted-convention row (scheme sensitivity); the E1-vs-E2 spread ratio dressed vs tree (the mechanistic registration); the dressed cells at L = 6 for continuity with the tree tables.

## 3. Scope

Everything of paper 5 §1's inherited scope, plus: RPA is the leading resummation (vertex corrections and beyond-RPA diagrams excluded — the dressing class boundary, disclosed); the S/P channel labels remain the mode import; the g_x-flip structure is no longer prefactor-trivial under dressing and is not part of the protocol. A SELECTED-ODD-DRESSED, if review-confirmed, would be the one-sign machine's target achieved at its honest scope — one loop up from where three tree-level protocols refused; it would still not be a derivation of Bell violation (assignment, scale, dressing-class).

## 4. Review corrections (2026-07-09, the round-35 paper-5 hostile review — applied; amended receipt supersedes the dc1f489 original; verdict unchanged)

- **MAJOR (the convention-certification claim — §1 corrected in place):** §1 originally claimed Gr2 certifies the sign convention ("a backwards convention shows up as a non-positive spectrum"). Review-measured FALSE throughout the run region: spec(GΠ) ⊂ [−0.389, +0.193] at all four run points, so the flipped branch (I + GΠ)⁻¹G has min Re eig +0.611..+0.628 — Gr2 passes under BOTH conventions (the claim could bind only if Re eig(GΠ) ≤ −1); and under the flip all 8 legs read odd — the arc's success condition — on the arc's sole externally unreviewed leg. The repair: the convention is DERIVED, not gate-certified — the loop-minus Π branch re-derived from the step-(a) four-fermi expansion — and the amended receipt adds Gr1b, the O(2)-expansion gate: ‖[D_σ]_AB − g_x·I − g²g_x(P_A + P_B)‖/‖[D_σ]_AB‖ computed at the anchor AND at couplings scaled by ½ and ¼ (masses fixed — pure algebra) must SHRINK monotonically, confirming the implemented branch is the expansion's. **FAILS-AT-RPA stands** — the implemented branch is the derivable one.
- **MINOR (Gr1(i) vacuous):** the wiring check ran at g_x = ½ — a power of two, so truncated-vs-direct equality was bitwise-guaranteed by float algebra ("wiring 0.0e0" could not fail). Amended: the check runs at the non-power-of-two coupling g_x = 0.3, gated rel < 1e-12; the "0.0e0 certification" framing is withdrawn.
- **MINOR (the σ-pole framing — §1 corrected in place):** the receipt's own spectrum refutes pole dominance — dressing multipliers in [0.72, 1.24] (eig(GΠ) ∈ [−0.389, +0.193]); |[D_σ]_AB − g_x·I|/|[D_σ]_AB| = 0.21 — a bounded σ-channel dressing, nowhere near a pole; the registered pole-dominance mechanism held only marginally (spread 1.67 vs 1.72). §1 reworded to "σ-channel-dressed (RPA-resummed)"; the pole framing survives only as the pre-receipt registration, labeled as such.

## References

Paper 5 (the arc; §7's continuation registration); note-ml3b-f (+ the r20 review: the full-convention resolution and its certification); LEDGER #77/#78; v8 paper 5 §3 (the σ-channel machinery); PLAN §post-round-20 (the funded fork; the reserved-review rule).
