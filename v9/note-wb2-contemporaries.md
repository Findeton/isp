# wb2 — the contemporaries test: the bridge in the instrument-native regime

**Status:** design note, 2026-07-06 (v9 round 19). Receipt: `v9/code/wb2_contemporaries.py` (pinned here, committed strictly before the receipt per the round-18 rule). Provenance disclosed: wb1's CONFOUNDED verdict + the corrected differential-decay mechanism (note-wb1 §4) + the referee's unpinned scouting (restricted partial flips positive on wb1's seeds; k3's native fleet measured fully contemporaneous). **Fresh seeds are therefore mandatory: 20260737–39** (primary first) — the scouting numbers must have no vote in their own gates.

## 1. The test

wb1's construction verbatim (web (2048, 32, 16), dominance order, W = cross-comparability, χ̂ = Hasse-GFF cross-chain covariance, the supply channels). New: each chain's **lifespan** = [first commit, last commit]; a pair is **strong-overlap** iff the lifespan intersection exceeds 50% of the shorter lifespan (the referee's definition, pinned verbatim). The identification's corrected prediction: in the contemporaneous regime — the only regime the tomography instruments use — the supply-partialled W↔χ̂ association is **positive** (the differential-decay imprint that drove wb1's negative lives in the cross-era pairs, which the restriction removes).

## 2. Pinned gates (2-regressor rank-partial: levels-outer rank + birth-affinity rank; nulls = 24 chain-relabeling permutations of χ̂ through the full restricted pipeline)

- **Gv1 [directional]:** the strong-overlap partial ρ_r > 0 on 3/3 fresh seeds.
- **Gv2 (evidence):** Stouffer-combined null-z across the three seeds ≥ 3.
- **Gv3 (the mechanism's own signature):** ρ_r(strong-overlap) > ρ_r(complement) on 3/3 seeds — the restriction itself must be what flips it.
- **Gv4 (placebo):** the supply-fit-plus-permuted-residual fake field runs the same restricted pipeline and reads |z| < 2 on the primary seed (wiring check: the fitting procedure must not manufacture the positive).
- **Verdicts:** all hold ⇒ **BRIDGE-SUPPORTED-RESTRICTED [DEMONSTRATED given the Hasse-GFF import; contemporaneous regime]** — the W-port's first supported form; ≥ 2/3 seeds negative on Gv1 ⇒ **REFUTED-AT-GRADE** (the rung falls even in its native regime); otherwise **UNDETERMINED** (named power fix: more seeds / larger fleets). INFO: pair counts under the restriction; raw and unrestricted values alongside.

## 3. Honest scope

Grade unchanged from wb1 (ml2-class field — NOT the GW matter); a supported verdict licenses the W-port for ml2-class fields in the contemporaneous regime only, and the GW-grade bridge stays open. The restriction is pinned pre-receipt on an independent principle (the instruments' measured native regime) with the pre-confirmation disclosed — the fresh seeds carry the adjudication.

## 4. Review corrections (2026-07-06, the round-19 hostile review — applied; PASS-WITH-CORRECTIONS, reproduction exact, verdict stands)

- **MINOR-1 (the placebo instrument, honestly re-graded):** 30 referee replicates per seed show the supply-fit+permuted-residual pipeline carries a POSITIVE bias (+0.4–0.9σ ≈ +0.02 in ρ units; 3–4/30 replicates breach |z| < 2) — the recorded primary z = −0.0 was a lucky-low draw. The bias is 4–6× below the observed effect and cannot own the verdict, but **Gv4 is a single-draw wiring check, not evidence**, and "placebo clean" overstated it.
- **MINOR-2 (headline caveat restated inline):** SUPPORTED means the §1 identification passed its necessary first rung in the instrument-native regime — **association is NOT automatic evidence of the physical identification** (wb1 §3, load-bearing): both W and χ̂ are functionals of the same web order. The empirical answer to the circularity worry is the complement's strong anti-correlation (−0.27..−0.45) — same-graph functionals do NOT trivially agree; the restricted agreement is a regime-specific fact.
- **MINOR-3 (null design):** the pinned χ̂-relabel null is the most liberal of three natural designs; at 300–500 perms the alternatives give z 2.87/2.33/3.13 (permute-W) and 2.26/1.69/2.57 (joint relabel) — **the pinned Stouffer ≥ 3 bar passes under all three (7.4 / 4.8 / 3.76)** and the 500-perm pinned z's are higher than recorded (4.21/3.35/5.22). Defensible (Mantel-with-fixed-covariates); no verdict impact.
- **Referee attacks that strengthened the result (on record):** threshold-robust and monotone in contemporaneity (30/50/70% ⇒ +0.087/+0.118/+0.137 on the primary — anti-knife-edge); the pinned gates would have passed on wb1's OLD seeds too (Stouffer 7.70 — thresholds not reverse-engineered); the third-regressor attack FAILS DECISIVELY — adding overlap-fraction, |Δbirth|, chain-length, lifespan-length, or all four at once INCREASES the partial (up to +0.200/+0.116/+0.180, z 4.3–7.0).

## References

note-wb1 (+§4: the corrected mechanism; the referee scouting; MINOR-2's ordering rule); round-17 scout (the W-port); LEDGER #72–#73; `n3_derived_must_fail.py` (construction provenance).
