# ml3b-f — the zero-mode resolution and THE FINAL TREE-LEVEL ADJUDICATION

**Status:** design note, 2026-07-06 (v9 round 20). Receipt: `v9/code/ml3b_f_final.py` (pinned here, committed strictly before the receipt). Admissibility: rounds 18–19 closed the naive and improved families at tree/L = 6; "larger L" and "a principled correlator-level zero-mode treatment at a new order/scale" were both named admissible structural moves — this note is both at once, and it is the LAST: any non-SELECTED outcome ends the tree-level line (the fallbacks are RPA dressing and the mode-selecting Hamiltonian).

## 1. The fork, resolved on principle

The twice-measured fact (LEDGER #75, referee-verified): all 16 estimator-protocol splits are manufactured on the zero-mode-subtracted side; all 8 full-propagator legs read odd. The question the program owes itself is not "which side wins" but "which treatment is *correct* for quenched correlators at fixed Q ≠ 0" — decided by argument, not by the tally:

1. **The full propagator is the pinned convention.** The |Q| zero modes are exact eigenstates of the record overlap operator (index(D) = Q, machine-verified at paper 14's standard). Nothing in the construction licenses deleting exact spectral content from a two-point function. The known quenched pathology (unsuppressed 1/M zero-mode terms) is a *small-M* disease; this machine runs at M ≈ 0.7–0.95 — O(1), far from the divergence — where the modes are ordinary spectral content.
2. **The gap-side subtraction is not a counter-argument.** Step (a) subtracts nz/(MV) from a *scalar* trace to DEFINE the bulk condensate driving mass generation (separating the topological 1/M term that would make the M → 0 gap equation ill-posed). A definitional split of one scalar sum licenses nothing about deleting operators' spectral content from position-space correlators. (Round 18 measured what deletion does: the rank-1 projector, extended over the torus at |ω|² ~ 1/V, injects the long-range scar.)
3. **S − P cancellation, weighed and set aside as primary:** with Z the zero-mode part, γ₅Z = Zγ₅ = sZ (chirality), so the Z×Z pieces of Π^{PP} and Π^{SS} are equal and cancel in the difference — but the bulk×Z cross terms survive, and the trick does not map onto the four-cell parity (the verdict object is a product across mixed channels, not an S−P combination). Retained as an INFO diagnostic only.
4. **Sector-weighting, set aside:** summing Q-sectors with weights introduces new imports (the weights) and dilutes the parity-breaking backbone the cells require; a redesign, not a resolution.
5. **The V-scaling of the contamination is the falsifiable discriminator (§3 Gf3):** if the sub-vs-full discrepancy is a finite-V artifact (mode density ~ 1/V), it must shrink with L. If it does not, the §1 resolution loses its dissolution claim and the verdict downgrades — pinned below.

## 2. The disclosure (in full)

The direction is known: 8/8 full legs read odd at L = 6 across both families, and the round-18 referee's unpinned L = 10 naive-family run read full odd-odd. This pin is therefore integrity-loaded the same way wb2's was, and carries the same discipline: (i) the §1 argument is data-free (exact states, deletion license, mass regime — none of it cites a measured sign); (ii) the receipt's live content is genuinely unmeasured — the improved family at L = 8 and L = 10 has never been run, E2-full has never been evaluated off L = 6, and the masses re-solve per L; (iii) Gf3 can refuse and its refusal bites (downgrade pinned). One shot, final.

## 3. Pinned gates

Operators: the improved family (K = (1 − D/2)S — the chirally-consistent content certified in round 19), sectors (1, 2), FULL propagator per §1; masses re-solved per L from the step-(a) coupled system; estimators E1/E2 verbatim (note-ml3b-d §2).

- **Gf1 (cells exist):** all eight |E{1,2}_xy| > 1e-14 at (4, ½) full, at BOTH L = 8 and L = 10.
- **Gf2 (THE FINAL ADJUDICATION):** the parity on 8 legs = {E1, E2} × {g_x = ¼, ½} × {L = 8, 10}, full convention. **Unanimous ⇒ SELECTED-ODD** (the record-native matter construction, at its consistent operator content and pinned convention, derives the empirically correct Bell-class sign at tree level — the one-sign machine's target, achieved at its honest scope) **or SELECTED-EVEN** (the locus is refuted at its own consistent content and principled convention — the kill, activating the fallbacks). **Any split ⇒ FAILS-AT-TREE-LEVEL and the line ENDS.**
- **Gf3 (the V-scaling discriminator, REGISTERED and falsifiable):** at (4, ½), for each estimator, the max-over-cells relative sub-vs-full discrepancy max_xy |E_sub − E_full|/|E_full| DECREASES from L = 6 (the round-19 receipt's on-record values) to L = 10, with L = 8 printed. REFUSED ⇒ the contamination is not a vanishing finite-V artifact ⇒ **any Gf2 SELECTED downgrades to SELECTED-CONVENTION-CONDITIONAL** (the honest price, pinned now).
- **INFO (unpinned):** the sub-convention parities alongside (the scheme-sensitivity record); the S − P combination's zero-mode cancellation check (Z×Z equality to machine precision at one point); distance tables at (4, ½) both L, both conventions.

## 4. Scope

Tree-level exchange, 2d, large-N, quenched, sectors (1, 2), the S/P channel-label import — all standing qualifiers inherited. A SELECTED-ODD here is: the sign readout completed at tree level under a data-free operator content and a data-free convention, with the scheme question dissolved (Gf3) or explicitly carried (the downgrade). It remains NOT a derivation of Bell violation (assignment import, scale, dressing). This is the last tree-level word either way.

## References

LEDGER #71/#73/#75/#76 (the split history; the 8/8 fact; the pathology-class adjudication); note-ml3b-d §2 (estimators), note-ml3b-e (+§5: the certified improved contraction); v8 paper 5 + paper 14 (the operator standard; the index theorem); the round-18/19 reviews (the scar mechanism; the S − P addition).
