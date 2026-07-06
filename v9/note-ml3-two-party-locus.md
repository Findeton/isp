# ml3 — Tier 7 rung 3: the two-party matter locus proper (campaign design)

**Status:** design note, 2026-07-05 (PLAN.md T7.3; round 7 secondary — think-first, no code this round; multi-round campaign, cheap-first). Rungs 1–2 are executed (`ml1` 5/5, `ml2` 5/5 at final counts; LOG rounds 3–5) and have specified the target this note pins. The object is v8 paper 2 §4.7's named residue: "a genuine two-party matter interaction — the interacting Ginsparg–Wilson flow (paper 5) or a mode-selecting Hamiltonian — is the one place a coupling could arise, and it is unbuilt."

## 1. The no-go boundary this campaign must respect (and why it exists at all)

v8 paper 2's theorem stands: **the records cannot fix `χ_AB` from inside** (capacity blindness + field blindness; the free filling inside `Q̃`). Rung 3 does not contest this — it *routes around it by construction*: a matter sector is new dynamics with its own disclosed axioms, and everything it produces carries the grade ceiling **[DERIVED given the matter sector]** (PLAN 7b). The deliverable is not "quantum `χ_AB` from records alone" (that would contradict a proved theorem); it is a *built* dynamics whose output is a definite `χ_AB` law, with the import ledger stated exactly as paper 5 states its own (mode import; scale import; now the coupling constant `g²` as the sector's one new dial).

What rungs 1–2 measured, which now *specifies* the target:

- **Locality is not required for geometry** (ml1's 2×2 cell, review-executed: comparability-graph mediation + exact estimator closes at Procrustes 0.999). The rung-3 constraint is **amplitude/sampling-robustness**, not locality: full-causal mediation carries geometry at ~7× smaller relative amplitude (1.0% vs 0.14% rel-amp) — the built sector must put its cross-chain covariance where finite-sample estimators can see it.
- **The field functor must not wash out record geometry** (ml2: non-washout [directional, multi-seed] 0.743–0.919 with the 0.85 pin refusing on 1/2 off-seeds; graph-only baseline 0.704 with the field's margin +0.024…+0.19 seed-variable; size-residual void clean 0.048/0.889). Rung 3 inherits ml2's gates as *regression* gates: whatever dynamics is built, its induced field must still read out the web's own two-clock geometry at-or-above ml2's toy-Gaussian bands.
- **The M6 caveat binds until the sector is genuinely dynamical**: ml1/ml2's field was Gaussian *by construction* with order-mediated covariance — an independent random object, not dynamics. Rung 3's whole point is to replace "Gaussian by fiat" with "produced by an interaction."

## 2. Cheap-first: two sub-rungs, in order

### ml3a — the maximum-caliber route (cheap; derivation-shaped; this is the next executable step)

v4 p23's license-theorem engine, applied to the two-party joint law: **`χ_AB` as the unique least-bias joint law** (max-caliber / min-KL against the product of the derived marginals) **under the derived constraints only**:

1. the per-lineage marginals (paper 1's law — fixed, not free);
2. the connectivity floor and the manifoldlikeness obligation (v8 paper 2's constructive half — the two genuinely-new global constraints);
3. the amplitude band measured at rungs 1–2 (the estimability constraint of §1, entering as a moment condition on the windowed cross-chain covariance);
4. `Γ ⪰ 0` (the fence — already forced; the solution must live inside the almost-quantum envelope or the construction is inconsistent).

**The sharp question ml3a answers:** is this constraint set *sufficient to pin a point* in `Q̃`, and if so — is the point quantum, almost-quantum-extremal, or interior? Every branch is content: a **unique quantum point** = the missing-bit candidate found by least-bias (the strongest possible rung-3 outcome, immediately falsifiable against the Tsirelson value); a **unique non-quantum point** = the least-bias law is measurably wrong OR the constraint list is incomplete — either way the *degeneracy structure* becomes the sector's specification; **underdetermination** = the honest measurement of how much dynamics the locus actually requires (the degeneracy dimension is the deliverable, and ml3b inherits it as its target list).

Pre-registered gates (ml3a): **G1** — the optimization is well-posed (existence + uniqueness up to the disclosed symmetry) or the degeneracy dimension is computed exactly; **G2** — the solution satisfies the fence (inside `Q̃`) *without* being put there by hand (assert, don't project); **G3** — at CHSH marginals, the solution's `χ_AB` is compared against the quantum value with the verdict branch stated in advance (match to ≤ 1% / miss / underdetermined — all three reportable, none repaired post hoc). High precision throughout (mpmath, dps ≥ 80 per the standing precision rule — the objective is near-flat in the entangling direction by paper 2's own capacity-blindness measurement, so float64 is *known in advance* to be inadequate here).

### ml3b — the interacting two-species GW flow (the real dynamics; scheduled after ml3a's verdict)

Paper 5's mechanism, extended per its own disclaimer ("the two-party (`χ_AB`-coupling) interaction that paper 2 §4.7 names as its unbuilt matter locus remains unbuilt here too"): **two record species** on the record GW operator, coupled by a four-fermi cross-species term at seals; `χ_AB^derived` = the windowed cross-chain content covariance of the interacting flow's correlators (ml1's estimator, now pointed at dynamics instead of a planted Gaussian). Gates sketched, to be pinned in ml3b's own note *after* ml3a reports: cross-species correlator nonzero at seals and decaying with hop distance (the ml1 shape); the Lüscher-symmetry survival check extended to the coupled system; the ml2 regression gates; and the amplitude band of §1. Scope disclaimers inherited from paper 5 verbatim (large-`N`, 2d, quenched, small lattices — not the Clay gap; mode-relative).

## 3. Kill conditions

- **ml3a ill-posed in the strong sense** (the constraint set admits no law inside the fence): a consistency contradiction between the constructive half's constraints and the envelope — would be a MAJOR corpus finding on its own; halt and audit before any rung-3b work.
- **ml3b produces no cross-species covariance structure at seals** (flat correlators): the GW-flow shape is the wrong locus — redirect to the mode-selecting-Hamiltonian alternative, which then gets its own note.
- Neither kill touches rungs 1–2's results (they are measurements of the toy, terminal as scoped) or the n3 line (whose grade simply stays [DEMONSTRATED given the toy matter sector] until a rung-3 object exists to feed it).

## 4. Sequencing

ml3a is a single-receipt round item (optimization + verdict; no web simulation). ml3b is a multi-round build. Per PLAN 7b, rung 3 "gets its own campaign plan when rungs 1–2 have specified the target" — this note is that plan's head; ml3b's full note is written only after ml3a's branch is known (its target list depends on ml3a's degeneracy structure).

## References

v8 paper 2 (§4.7 the named residue; the two blindness mechanisms; the constructive half's connectivity floor + manifoldlikeness obligation; the fence `Γ ⪰ 0` and the `I3322`/Tsirelson numbers); v8 paper 5 (the interacting GW flow, single-species; the O8 closure; the import ledger style rung 3 adopts); v4 p23 (the maximum-caliber license machinery); `ml1`/`ml2` receipts + LOG rounds 3–5 (the executed rungs; the 2×2 cell retraction; the amplitude/sampling-robustness constraint; the non-washout bands); LEDGER #43 (iteration-ledger discipline), #46–#47 (paper 2's terminal state); feedback_precision_mpmath_80bit (the standing precision rule ml3a instantiates); PLAN.md 7b (T7.1–T7.3, the grade ceilings).

## ml3a verdicts (2026-07-05, round 11; receipt `ml3a_least_bias.py`, dps = 80, 5/5, exit 0)

**G1 HELD — well-posed, with the degeneracy computed exactly.** Under the derived constraints alone (zero marginals from paper 1's symmetric seal law; the amplitude budget Σ E² = c² as the moment form of the rung-1/2 band, with the connectivity floor = c > 0; the fence asserted, never imposed), the maximum-entropy joint law is **unique up to the local sign gauge × ONE discrete bit**: the entropy forces equal magnitudes |E_xy| = c/2 (all 24 budget-preserving asymmetric perturbations lower H; H strictly concave in E²), is **sign-blind exactly** (even in E to 1e-75 — the degeneracy is structural, not perturbative), and the gauge partitions the 16 sign patterns into exactly two orbits labeled by the CHSH parity s₀₀s₀₁s₁₀s₁₁ = ±1. **The un-fixable datum is one bit.**

**G2 HELD — the fence asserted via the exact TLM criterion** (Tsirelson–Landau–Masanes, the exact quantum boundary for the zero-marginal 2×2×2 correlator polytope): both parity branches are quantum for c < √2; **the odd branch saturates the boundary exactly at the Tsirelson budget** (4·asin(1/√2) = π, residual 4×10⁻⁸¹) and is excluded by the constraint set's own consistency above it; the even branch stays interior to c = 2.

**G3 = UNDERDETERMINED-AT-ONE-BIT, with conditional-exact quantum match** (the pinned third branch, in its strongest form): at the Tsirelson budget the odd branch's correlators equal the quantum behavior's 1/√2 to all 80 computed digits, CHSH = 2√2 exactly. Least-bias derives the magnitude *structure* (equal spread; the exact magnitude-budget map; the Tsirelson crossing) and provably cannot choose between the two parity classes; the quantum-value match is conditional on the scanned budget c = √2 (see the deviations paragraph).

**What this buys.** (1) **ml3b's target is now a specification, not a direction: the matter dynamics must fix ONE SIGN.** The entire remaining freedom of the two-party coupling, under the least-bias reading, is the parity bit. (2) **Structural consonance with the paper-2 no-go** [named conjecture, NOT claimed]: v8 paper 2 localized the records' unforceable datum to one binary choice in ker R (the tensor/local-tomography bit); the least-bias engine independently localizes its freedom to one binary datum (the parity). Whether these are the same bit under the reduction map is ml3b's opening theory question. (3) The grade ledger: the *shape* = [DERIVED given the max-caliber principle + the calibrated budget c]; the *bit* = [UNDERDETERMINED, exactly, at every order]; the budget c = the one import (scale-arbitrary until the matter sector fixes units — the structure is budget-independent, which is the derivation's content).

**Registration deviations (round-11 review, MAJOR-1 + MINOR-2 — disclosed here and in-receipt):** the pinned constraint list had FOUR items; the **manifoldlikeness obligation was not implemented** — it has no behavior-level expression at the 2×2×2 abstraction (the legitimate reason, now stated rather than silent); the one-bit theorem is about the *implemented* set (marginals + budget + fence), and since adding constraints can only shrink the degenerate set, **one bit is an upper bound on the freedom**. The pinned "amplitude band" enters only as the equality-budget *form*: c is a scanned free parameter — the measured ml1/ml2 band never enters, and the earlier "reproduces the quantum magnitudes from first principles" is corrected to its conditional form: *the structure is derived; the quantum match is conditional on c = √2, which is scanned, not calibrated or derived*. Scope corrections (MINOR-5): "excluded above √2" applies to the equal-magnitude maxent solution, not to odd-parity quantum behaviors as such (unequal-magnitude odd families persist to budget c² = 2.25); the even branch is interior for c < 2 and on the boundary (deterministic-local) at c = 2.

**Disclosed limitations:** CHSH scenario only (2×2×2; I3322/higher scenarios not run); the budget enters as an equality (the moment form chosen in-note); zero marginals per the derived symmetric law; TLM is the exact fence for precisely this polytope (cited) — richer scenarios need the NPA machinery.
