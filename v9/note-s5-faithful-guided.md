# note-s5 — the faithful-guided control: does the action prefer the truth when offered?

**Status:** design note + pre-registration, 2026-07-05 (round 6). Gates pinned pre-run. Receipt: `v9/code/s5_faithful_guided.py`.

**The refinement (correcting round 5's framing, logged).** "Expressively closed against faithfulness" is trivially false for the attachment class: adding elements in a sprinkling's arrival order with their true ancestor-sets rebuilds the sprinkling exactly (the ORACLE arm, run as the anchor). The operative questions:

- **Q1 — action-preference (the fork's real content).** Along the *faithful trajectory* (the web forced to track the sprinkling), offer at each arrival the TRUE down-set plus the kernel's 12 decoys, and ask whether `ΔS_A1(truth)` is the argmin. The **marginal-preference rate** over late arrivals (`t ≥ 64`) is the decider — no path-dependence contaminates it.
- **Q1b — the free-run form.** The same menus but picks actually taken (truth-candidates closed downward in the grown web where decoy history has deviated, disclosed): endpoint layers measure the dynamics with path dependence.
- **Q2 — the offer gap.** Mean Jaccard distance of the best kernel decoy from the truth — the enrichment spec if the road is the kernel.

**Pinned gates/branches (n = 256, 4 reps; both directions live):**
- **G-O (anchor):** the oracle arm reproduces the sprinkling bit-exactly; its `r_I`/`m_ab` printed as the target values.
- **G1:** marginal-preference rate ≥ 0.6 ⇒ **TRUTH-PREFERRED** (the forgery is the kernel's offer distribution; enrichment road; Q2 = the spec); ≤ 0.3 ⇒ **TRUTH-REJECTED** (the action's marginal landscape is anti-faithful — no kernel saves argmin-A1; redirect = the interior-multiplicity/action side or the churn-class moves); else **MIXED** (dose-response measured).
- **G2:** free-run endpoints' heredity `r_I ∈ [0.35, 0.65]` in ≥ 3/4 reps AND `m_ab ≤ 3×` faithful ⇒ UN-FORGED under guidance (with G1 this separates landscape from path effects).
- **G3:** the offer gap printed per arrival-decile (the spec, whatever the branch).

Seed `default_rng(20260712)`; float64; A1 = r+link+S_comp with exact increments (s1/s4 machinery verbatim); sprinkling arrival order = `u+v`.

## Addendum — results + review record (2026-07-05; owed since round 6, flagged by both round-7 referees)

**Committed results (receipt `s5_faithful_guided.py`, seed 20260712; exits 1 by design, gate ledger printed).** G-O held (bit-exact oracle rebuild — expressibility trivial; the fork is action-preference). **G1 = TRUTH-REJECTED at 3.9%** (reps 0.021/0.036/0.073/0.026; pinned rejection line 30%). G2 REFUSED: free-run guided endpoints forged (r_I 0.804–0.916, 0/4 in-band; m_ab 1.283 ≈ 15× faithful; truth-taken 5.1–7.5% — itself chance-level, see below). Offer gap (Jaccard) 0.553 overall; the pinned per-decile print was missing from the first run (registration deviation, both referees) and is now delivered in-receipt: 0.653/0.626/0.653/0.638/0.576/0.507/0.453/0.382/0.399/0.641 across arrival-deciles.

**The chance line (round-7 review; receipted in `s6b_mechanism_family.py` M5).** Menus carry 14 candidates (truth + 12 kernel decoys + the empty set; duplicate-empties mean 0.60 → null in [7.1%, 7.7%]). Raw 3.9% sits below chance (rep-level t = −2.76, 4 reps) — the anti-faithful direction is supported, moderately, at rep-level noise; the verdict itself gates on the pinned 30% line with ~20σ-equivalent margin.

**The mechanism (CORRECTED by the round-7 review; receipted on this note's committed stream, s6b I1+M1).** The round-6 record's "the true down-set's new pairs pay full increments; skimpy decoys undercut" is refuted: at 93.1% of truth-losses the winner is *larger* than truth (menu-max at 73.7%); truth is Row-A-cheaper at 93.0% of losses; the decision is carried by **Row C's comparability-block increment** (|Row-C| > |Row-A| at 93.8% of loss steps). Under the registered u+v arrival order the faithful prefix runs at comparability ≈ 0.33 against Row C's equilibrium target ½ (reached only at completion, 0.504), so the transient gradient 2(r_t − ½) ≈ −0.3 pays the argmin to take the biggest candidate at every step. **TRUTH-REJECTED stands; its mechanism is the transient-vs-equilibrium mismatch of increment-optimizing an endpoint functional.** Full statement + the family-of-re-pricings closure: note-s6 §Review corrections (C1–C3); LEDGER #50.

**Receipt repairs (round-7 review).** Dead code stripped (an s4-era `heredity_axis` fallback vestige, unused `grow`/`top_interval_misfit`/`delta_S_ab`/`BETA_STAR`/`sqrt`); the float64 pledge corrected (float32 Gram fast-path; decision-invariance verified 0/768 flips by the code referee); output otherwise bit-identical on re-run.
