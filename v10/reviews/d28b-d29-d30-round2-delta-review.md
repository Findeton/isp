# ARC ROUND-2 DELTA — v10 D28b/D29/D30 (2026-07-12; the pass the external review named as owed)

**VERDICT: PASS-WITH-RESIDUALS — all five round-1 MAJORs present, faithful, and consistent at every task-named locus; all reruns byte-identical at exit 0; the external review's four record repairs landed everywhere they name. Residuals: 0 MAJOR / 3 MINOR / 3 NIT, all trace-completeness defects at loci adjacent to the named fixes; none touches a result. (All six applied same day; LEDGER #138.)**

**Reproduction (scratch only):** d28b receipts 5/5 + 6/6, d30 5/5 BRANCH 3 — all exit 0, outputs byte-identical to v10/data/. The d29 card, receipt, AND code have a sole-commit history at 4d1d7e3 (git diff empty; d30's in-run sha assert re-confirms the card bytes). Working tree clean at all arc loci.

## MAJORs — all five verified
- **M1 (the verdict flip):** the corrected rule identical in note-d30 §2 and enters_band(); W4 prints BRANCH 3, all verdicts None; the residual print carries the external effective-dimension wording. Card arithmetic independently recomputed: (2.0062−1.756)/0.04005 = 6.25 ("~6 card-SD"); (56.535−34.41)/2.1987 = 10.06 ("~10 SD"); c2 = 2.91 vs 1.801 = +61.6%; 0.35/SD = 8.74 ("8.75x"). #135 quotes #134's superseded sentences verbatim (all three verified present in #134); the supersession chain traceable; 920fcf1 edited code and .out in lockstep.
- **M2 (the wire-DAG ownership):** note-d30 §1 owns the object as declared physics, attribution struck, 31.5%/3.2 carried; LOG + LEDGER match. Residual at an adjacent locus (the receipt's own header print) — MINOR-3.
- **M3 (the conjecture repair):** the non-degeneracy hypothesis edited in place; E5 gates I_mid = 576/625, I_end = 0, reach TRUE. INDEPENDENT REBUILD (amplitude engine with exact-rational angle addition — a different architecture): the 8 co-axial cRy ops compose to the exact rational identity (527^2 + 336^2 = 625^2), 4(asin(3/5) + asin(4/5)) = 2 pi exact by 3-4-5 complementarity; I_mid/I_end reproduce exactly. The scope-true claim is effectively self-gating (max same-pair touch in E1-E4's webs is 2).
- **M4 (the spatial vacancy):** the disclosure block replaces the §1 bullet (single-bullet diff); no card edit — byte-identity to the freeze git-proven.
- **M5 (K_flat's battery):** the fixed-horizon cylinder gate is a real computation (within a horizon, cylinder consistency == per-node normalization — R2-redundant but not fake); relabeling class 1 genuine (opposite fresh-label orders must canon-merge). Class 2 was tautological and §2(iii) unscoped — MINOR-1/-2.

## MINOR batch + external repairs — verified
10.1% confirmed from the card ((1.8208−1.6375)/1.8208 = 10.07%); the three 10.4% loci are append-only/frozen with the correction recorded at the arc LOG + #135(f) — the in-code strings ride the next-touch list (NIT-2, now applied). Far-rate relabel; counts as printed; the card sha hashlib-computed and asserted. Greps: 'non-integer' survives only in append-only history and the review files — zero hits in receipts, notes, code; 'provably not' gone from the arc (the surviving "provably order-dimension <= 2" is the D28 mirror-DFS theorem — correctly retained); the event-DAG scope sentence in the W4 print; no live locus asserts BRANCH 1.

## Residuals (all applied at LEDGER #138)
- **MINOR-1:** note-d28b §2(iii) still read bare "cylinder-consistent" while §4 claimed it scoped — fixed in place ("within each fixed horizon; the {K_flat^T} family is not projective across horizons"); the pin §2 R4 bullet likewise ("fixed-horizon cylinder consistency").
- **MINOR-2:** R4's second relabeling class was a tautology (a presence check that cannot fail) — replaced with the explicit renamed-web merge test canon(z2-copy) == canon(z1-web); rerun.
- **MINOR-3:** the d30 receipt header/docstring still printed "(D28b)" — the attribution M2 struck elsewhere; replaced with "the WIRE/CIRCUIT EVENT DAG (declared physics — note §1)"; rerun.
- **NIT-1:** the W4 prose conflated +61.6% (vs the card) with the ceiling margin (+45.5% above m_2 = 2) — both now printed.
- **NIT-2:** the in-code 10.4% strings (d29, two loci) → 10.1%; the d29 count relabel (7 substantive + 1 freeze gate) applied at this touch; rerun with the card byte-identity gate.
- **NIT-3:** box-4 clause (v)'s hardcoded pseudo-SD recorded — unreachable for these data; folds into the O-E card-schema upgrade (D32A).

**New-defect scan clean:** every W4 number re-derived from the card; mm_f spot-checked (1/2, 8/35, 1/10); E5's arithmetic right; R1's 1/40-vs-1/25 and 2/81-vs-1/25 re-derived by hand. With the residuals applied, the arc record is DELTA-CLEAN and "delta verification pending" is superseded.
