# 3p1-p2 — Phase 2, Lorentzization I: the cone-shape discriminator

**Status:** design note, 2026-07-06 (v9 round 26). Receipt: `v9/code/dimwall_phase2.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE on record.**

## 1. The question, stated without illusion

The order is orthant-dominance by definition, so the exact causal cone is **polyhedral** (C + 1 flat faces) at any finite C; genuine Lorentz causality is the round cone. What is measurable is the webs' finer causal *statistics* — which see cone × measure jointly — and the question splits: (i) do the grown webs carry the polyhedral signature (registered: yes — the honest baseline); (ii) can a record-native mechanism move the statistics toward the round locus without collapsing dimension (the mixing question — either answer is decisive: movement opens Lorentzization-by-mixing; rigidity makes polyhedral anisotropy a falsifiable *prediction* of the framework at finite C, distinguishing it from exact Lorentz invariance).

## 2. The instrument: the chain-abundance triple

s_k = (# k-chains)/C(N, k) for k = 2, 3, 4 (transitivity makes counting matrix algebra; s_k is N-independent in expectation, so cross-N comparison is legitimate — N's printed). Two reference families, both MEASURED (no literature formulas — the Phase-0 lesson): **round** = M^{2,3,4} diamond sprinklings (N = 512, 8 seeds); **orthant** = iid uniform k-coordinate dominance, k = 3, 4, 5 (N = 512, 8 seeds). Comparison at matched s2: interpolate each family's (s3, s4) at the web's s2 (log-space interpolation in the family parameter); distances d_round, d_orthant = the log-space Euclidean distances of the web's (s3, s4) to each family's matched point. The polyhedral-vs-round score is their comparison; separations are certified before any web is read.

## 3. The K-direction (mixing) variant

Slot preferences become random **simplex points** w_m ~ Dirichlet(1,…,1) (not one-hot corners); each click deposits vector evidence e·w_m (the slot's whole direction). Cross-slot dominance becomes ray-dominance over many directions — the measure spreads over the orthant's interior. Retention is gated (the α = 1 lesson: mechanisms that decorrelate can also collapse).

## 4. Pinned gates (webs at the Phase-1b pinned class: C = 3, per-channel churn; one-hot α = 0.75 = "the corner webs"; seeds 20260800+)

- **Gc0 (instrument separation):** at every s2 in the webs' range, the round and orthant families' matched (s3, s4) differ by > 3× the pooled seed-sd (per component, at the interpolated points). REFUSED ⇒ VOID-INSTRUMENT (the round stops).
- **Gc1 (the baseline signature — registered):** the corner webs sit nearer the ORTHANT locus (d_orthant < d_round) on ≥ 4/5 seeds.
- **Gc2 (the mixing probe — [directional]):** the K-direction webs' mean d_round is smaller than the corner webs' mean d_round (movement toward round), with the per-seed values printed.
- **Gc3 (retention):** the K-direction webs keep 2-realizer refusals ≥ 4/5 and d_MM ≥ 3.0.
- **INFO (unpinned):** the full (s2, s3, s4) table for all families and webs; both distances per seed; the d_MM of every family through the Phase-0 curve (consistency); the ratio d_round/d_orthant per web class.
- **Verdicts:** Gc1 ∧ Gc2 ∧ Gc3 ⇒ **MIXING-ROUNDS [MEASURED, directional]** (Phase 2b: tune the mixing; re-pose the ≥ 3.7 review trigger there); Gc1 holds, Gc2 refuses ⇒ **POLYHEDRAL-RIGID** — the framework predicts finite-C anisotropy (the falsifiable-signature branch; Phase 2b becomes the anisotropy characterization instead); Gc1 refusing ⇒ the baseline expectation itself fails — the webs are NOT on the orthant locus either (named outcome: MEASURE-DOMINATED — the dynamics' measure already deforms the statistics away from both ideals; the finding is the table itself). Exit 1 by design on refusal.

## 5. Scope

No hostile review (mode on record). Chain abundances are the coarsest cone-sensitive statistics — a positive here licenses, not replaces, the full copula/certifier work (Phase 3). The K-direction variant is one mechanism from a family (per-click Dirichlet noise, seal-mediated direction exchange are ledgered alternates). "Why C = 3" stays open regardless.

## References

note-3p1-p1b (+ receipt: the pinned class, the interior-optimum law); note-3p1-dimension-ledger (instruments); PLAN §the-3+1-program Phase 2; LEDGER #84.
