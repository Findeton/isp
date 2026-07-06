# wb1 — the w ↔ χ_AB bridge test at the constructible grade (the 3+1 redesign's first build)

**Status:** design note, 2026-07-06 (v9 round 18; the round-17 scout's binding gap: no tomography instrument accepts a correlation matrix — the order-derived fleet coupling W is the only port, and the identification w ↔ χ_AB is [POSITED], unbuilt, in both v8 papers 14/15). Receipt: `v9/code/wb1_bridge_test.py` (gates pinned here, committed pre-receipt).

## 1. The test

On ONE grown record web (no planted geometry; ml2's construction verbatim: (N, M, L) = (2048, 32, 16), chains = lineage segments ≥ 8 commits, dominance order on (b, χ)), compute over the SAME chain fleet:

- **W** (order-derived, the k3/l2/m1 port formula): `W_ij = mean over cross pairs (a ∈ chain_i, b ∈ chain_j) of comparable(a, b)` under the web's dominance order — the tomography instruments' own coupling.
- **χ̂** (field-derived, ml2 verbatim): the Hasse-GFF exact cross-chain covariance `χ̂_ij = Cov[chains_i, chains_j].mean()`, `Cov = (L_g + 0.1·I)^{-1}` on the Hasse graph.

The posited identification predicts a positive monotone association between the two M×M matrices over chain pairs. **Grade disclosed:** χ̂ here is ml2-class (the Hasse-GFF import) — NOT the GW matter field; a supported bridge licenses the W-port for ml2-class fields only; the GW-grade bridge stays open (named).

## 2. Pinned gates (seeds 20260734–36; primary = 20260734; Spearman over the off-diagonal upper triangle; nulls = 24 chain-relabeling permutations of χ̂ against fixed W)

- **Gw1 (association, primary):** Spearman ρ(W, χ̂) > 0 with null-z ≥ 3 on the primary seed. [directional: positive] REFUSED ⇒ **BRIDGE-REFUTED at this grade** (the posited rung falls where it is currently constructible).
- **Gw2 (robustness):** ρ > 0 and z ≥ 2 on 3/3 seeds.
- **Gw3 (THE CONFOUND CONTROL — the n3-derived lesson applied to the bridge):** the supply surrogate (verbatim n3-derived: level outer product + birth affinity) must not own the association — the rank-partial Spearman of (W, χ̂) given the surrogate stays > 0 with partial-null-z ≥ 2 on ≥ 2/3 seeds including the primary. Gw1 holds ∧ Gw3 refuses ⇒ **CONFOUNDED** (both W and χ̂ read supply; the round-16 diagnosis extends to the bridge — itself a named finding).
- **Verdicts:** all hold ⇒ **BRIDGE-SUPPORTED [DEMONSTRATED given the Hasse-GFF import]** — the matter side gains its first wired path into the tomography stack (via the W-port); refusal patterns as above. INFO (unpinned): raw ρ values; the supply-alone associations Spearman(sur, W) and Spearman(sur, χ̂) (how much either matrix is supply); Mc per seed.

## 3. Honest scope

Both W and χ̂ are functionals of the same web, so association is NOT automatic evidence of the physical identification — it is the necessary first rung (the posited claim fails if even this refuses), and Gw3 guards the known failure mode. Float64; exits 1 by design; house verdict conventions.

## References

Round-17 scout (LOG dafe8ca: the binding gap; the W-port formulas at k3:112-117 / l2:143-147 / m1:109-114); v8 papers 14 §4/§6 + 15 §6 (the [POSITED] flags); ml2 + n3-derived (`n3_derived_must_fail.py` — the construction and surrogate ported verbatim); LEDGER #68 (the zero-readouts adjudication this line answers).
