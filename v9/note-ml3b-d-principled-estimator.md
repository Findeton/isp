# ml3b-d — the principled two-party estimator and THE ONE-SHOT ADJUDICATION (tree level, L = 6)

**Status:** design note, 2026-07-06 (v9 round 18). Receipt: `v9/code/ml3b_d_one_shot.py` (gates pinned here, committed pre-receipt; machinery = the corrected ml3b-c verbatim). Supersedes the window FAMILY of note-ml3b-c §2.2 with a window-FREE estimator pair argued on principle; note-ml3b G2's anchored semantics still govern (the world is on the ODD branch).

## 1. The principle (argued from the ontology, not from round 17's data)

The target object (ml3a) is the CHSH parity of **seal** correlations. A seal joins **two distinct record threads**; a thread coinciding with itself is not a seal — there is no two-party event at zero separation. The lattice surrogate must therefore be the **separated** two-point correlator: the d = 0 contact cell is the expectation of a single composite operator at a point, and in standard QFT terms the contact term is the scheme-dependent piece of a two-point function — never its physical separated content. This principle was available (and flagged) in round 16: the review's MAJOR-3 identified the contact term as owning the w-inclusive signs, and the window obligation descends from it. Round 17 measured the consequence (the point-invariant contact/shell split); this note elevates the principle to the pin. The sequence (window pins → data → principled re-pin) is disclosed as such, and §4 pins the price: this adjudication is **one-shot**.

## 2. The pinned estimator pair (window-free, cutoff-free)

With C^{xy}(u, v) the step-(c) cell correlator (corrected machinery: sectors (1, 2), joint complex zero-mode projector, bubble estimator as coded):

- **E1 (the separated susceptibility, p = 0):** `E1_xy = (1/V) * sum_{u != v} C^{xy}(u, v)` — the zero-momentum mode of the off-diagonal correlator; every separated pair enters with weight 1; no window, no cutoff.
- **E2 (the lowest separated mode, p_min = 2π/L, star-averaged):** `E2_xy = (1/2) * sum_{axes a ∈ {x, y}} (1/V) * sum_{u != v} cos(2π Δa(u,v)/L) * C^{xy}(u, v)` with Δa the (torus) coordinate difference along axis a — the smallest-nonzero-momentum diagonal element of the separated kernel, averaged over the lattice-symmetry star (cos form; the ± pair is conjugate so the object is real by construction).

Both are long-wavelength readings of the same principled object (the separated correlator); they differ only in the canonical momentum (0 vs p_min). Parity per estimator: π = sign(∏_{xy} E_xy). Normalizations are sign-irrelevant and pinned anyway (per site, /V).

## 3. Pinned gates

- **Gd1 (cells exist at separation):** all eight |E{1,2}_xy| > 1e-14 at the anchor (g², g_x) = (4, ½), zero-mode-subtracted. REFUSED ⇒ SEPARATION-NULL (the assignment cannot express the cells away from contact; redesign, not a locus kill).
- **Gd2 (THE ONE-SHOT ADJUDICATION):** the parity computed **8 ways**: {E1, E2} × {g_x = ¼, ½} × {zero-mode-subtracted, full propagator} (the convention pair is a fair unanimity demand: LEDGER #70 established pattern-equality of the conventions at every window). **Unanimous ⇒ SELECTED-ODD** (the construction + S/P assignment derives the empirically correct Bell-class sign at tree level/L = 6) **or SELECTED-EVEN** (the GW-flow locus under this assignment is REFUTED as the sign's origin — note-ml3b G2's kill; the mode-selecting-Hamiltonian fallback activates). **Estimator disagreement ⇒ ESTIMATOR-SPLIT**; convention disagreement ⇒ CONVENTION-SPLIT — both = FAILS-AT-THIS-ORDER, a principled negative (the long-wavelength separated sign is indeterminate at tree level/L = 6).
- **Gd3 (invariance confirmations, [directional], printed not gate-blocking):** the free point (decoupled masses) and the (4, −½) positive root (0.109667, 0.503996) — registered expectation: the anchor's parities persist (round 17's pattern-invariance under the new estimators).
- **INFO (unpinned):** the full per-distance signed shell table (d = 0..6, all four cells, both conventions — total transparency of what the estimators aggregate); the exponential-amplitude fit sign over d ∈ [1, 3]; the demoted (0, 1) row.

## 4. The irrevocability clause and the disclosure

**One shot:** after this receipt, no estimator, window, or convention re-pin is admissible for the tree-level/L = 6 sign readout. Any non-SELECTED outcome closes the tree-level chapter; the admissible next moves are structural only — the dressing class (RPA), larger L, a different sector/assignment family argued independently, or the Hamiltonian fallback. This clause is the price of re-pinning after seeing round 17's data, and it is what makes the adjudication meaningful.

**Disclosure:** the d = 1 component of both estimators is already public (LEDGER #70: shell odd, point-invariantly), so a reader can anticipate the direction if d = 1 dominates. **Registered expectation [directional]: SELECTED-ODD via d = 1 dominance.** The receipt's genuinely live content: the multiplicity-weighted d ≥ 2 re-weighting (back-of-envelope from #70's printed window means, the SP cell's separated sum is near-cancelling — the unanimity could fail there), the cos re-weighting of E2, the full-propagator legs, and the 8-way unanimity demand itself. A SELECTED verdict earned through all eight readings is a far stronger object than any single window's sign; that, not surprise, is this receipt's value.

## 5. Honest scope

Tree-level exchange, L = 6, large-N, 2d, quenched, declared S/P assignment, sectors (1, 2) — every qualifier of note-ml3b-c §4 inherited verbatim. A SELECTED-ODD is: the first record-native matter construction whose **separated long-wavelength** two-party correlator carries the empirically-correct Bell-class sign pattern, principled-estimator-adjudicated, one-shot. It is NOT: a derivation of Bell violation (assignment import, scale, dressing all stand between), and NOT window-family-robust (round 17 measured that the contact-inclusive family reads even — on record, undisturbed).

## References

note-ml3b-c (+§5 amendment, §6 review corrections) and its corrected receipt (the machinery, verbatim); LEDGER #69–#70; round-16 review MAJOR-3 (the contact-term diagnosis — the principle's provenance); note-ml3b G2 (the anchored kill semantics); ml3a (the parity bit; odd = Bell-capable); v8 paper 5 (scope).
