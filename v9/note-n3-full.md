# n3-full — the record-native 3+1 readout at full leg (L2 ∧ voids, multi-seed, both substrates)

**Status:** design note, 2026-07-06 (v9 round 15; the deferred full leg of L3 — n3-lite ran round 3 under the user-amended gate, option (a): L2 ∧ n3's own void-controls; the spectral gate is RETIRED-by-attribution, kernel curvature, and stays retired). Receipt: `v9/code/n3_full_record_native.py` (gates pinned here, committed pre-receipt). Grade ceiling unchanged: **[DEMONSTRATED given Tier-A input]** — the χ-field is the disclosed free configuration (paper 2's no-go makes it legitimately free); ml3b's derived field is the future handoff that upgrades the grade.

## 1. What "full" adds over the lite

1. **The corner substrate (the named design item).** The lite used L = 16 lineage segments because the certified builder's corner (L = 2) has ~2-commit lineages that cannot serve as worldline surrogates. The full leg adds the corner via the **slot-worldline construction**: chains = fleet slots (each slot's entire commit history is one worldline — persistent at any lifetime; the physically honest reading: the slot is the record-bearing object, lives are its refresh cycles). Corner arm: (N, M, L) = (2048, 64, 2) → 64 worldlines of ~32 commits each. The lite's lineage-segment arm (2048, 32, 16) runs alongside as the continuity anchor.
2. **Multi-seed (the m2 transverse-coverage residual).** Six fresh seeds per arm (20260722…20260727); the lite was single-seed.
3. **The certification-band form (the m1-parity leg).** Closure quoted as a per-arm band over seeds, not a single number.

## 2. Pinned gates (per arm unless marked)

- **G-1 (L2 closure, the amended gate's first conjunct):** Procrustes(MDS(χ_AB), latent) ≥ 0.9 on **≥ 5/6 seeds**.
- **G-2 (VOID 1, shuffle):** shuffled χ_AB fails closure at > 3 null-sd (24-draw null) on **every** seed.
- **G-3 (VOID 2, confound):** recovered coordinates NULL against the web's supply structure at < 2.5 null-sd on every axis-pair, every seed. For the corner/slot arm the confound set is {slot mean-content level, slot lifetime count (its churn intensity), slot first-commit time} — the slot-level supply observables.
- **G-4 (the certification band):** the closure band's **floor ≥ 0.85** per arm (min over the six seeds) — the certificate-style statement the lite could not make.
- **G-5 (coverage, measured-not-gated):** the latent-square quadrant occupancy per seed (all four quadrants ≥ Mc/8 chains) printed — the m2 residual quantified for the record; refusals here inform, not gate (disclosed).

Tier-A field construction verbatim from the lite (latent 2D uniform, `exp(−d/ℓ)`, ℓ = 0.6, 5% symmetric noise); chains require ≥ 8 commits; float64; verdicts per the house convention (refusals print the ledger, exit 1 by design).

## 3. Kill semantics

G-1 or G-4 refusing on the **corner arm only** ⇒ the slot-worldline construction is the wrong chain surrogate at L = 2 — the finding names the next construction (life-concatenation with birth-order stitching), not a 3+1 failure. Refusing on **both arms** ⇒ the record-native readout does not survive multi-seed scrutiny — the L2 conjunct of the amended gate fails at full leg, and T6.4's status reverts to blocked-pending-construction (the honest outcome the single-seed lite could not exclude). Voids refusing ⇒ the run is void per the standing convention (not a physics verdict).

## References

n3-lite (`n3_lite_record_native.py` + the round-3 substrate correction and G-b retirement); note-n3-gate-decision + the user's option-(a) amendment (LOG round 3); note 1 §§3–5 (L3's design; the §5.2 confound form); paper 2 (the no-go that makes χ Tier-A-free); note-ml3b (the derived-field handoff that upgrades the grade); PLAN T6.4; LEDGER #42–#43 (the round-3 corrections this leg inherits).
