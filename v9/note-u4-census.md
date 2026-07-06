# u4 — the growth-measure census (Tier 4 opening): exact `n ≤ 7` induced measures for the surviving law class, with the owed V-lab / `e(P)` accounting executed

**Status:** design note, 2026-07-05 (PLAN.md T4.1; round 7 secondary — think-first, no code this round; the receipt executes in a later round). Repairs a verified pre-registration breach: design note 8 C6 pre-registered *both* covariance arms ("**V-cov** (Φ order-invariant) vs **V-lab** (Φ reads labels), both run, the induced-measure accounting disclosed per arm") and `u2` ran neither the V-lab arm nor the multiplicity accounting. Reserved name `u4_growth_census.py` kept (design note 8 §receipts).

## 1. What changed since the reservation — the law list is now measured, not hypothesized

Design note 8 reserved u4 for "the" growth law class before any candidate was scored. Three rounds of measurement have since collapsed the candidate list:

- **Increment-optimization is dead as production** (s5 TRUTH-REJECTED 3.9%, LEDGER #48; robust to the centering family, s6, LEDGER #49). Bare-action argmin endpoints are additionally *disqualified* as G1 pathology (antichains — the u-line memo's endpoint screen).
- **The churn corner passes the cell and always has** (u1 positive control; paper 16 §4's membership; the D1/D1+atoms family beneficial per u3/y1).

So u4's census columns are re-scoped: the *primary* arms are the corpus's actual in-cell laws — **trivial-Φ churn corner**, **D1 (kill-the-oldest) churn**, **D1+atoms** — and the argmin family appears only as one labeled **pathology-control column** (its row exhibits what disqualification looks like in measure space; it is not a candidate). This is a design *narrowing*, disclosed here before any run: the census now answers "where does the surviving production class put its mass?", not "which of many classes survives?".

## 2. The objects and the ledger (all exact at `n ≤ 7`)

For each law arm, the census computes the **induced probability measure on unlabeled orders** at `n = 3..7`:

- **Reachability support**: which of the unlabeled posets on `n` points receive positive probability under the law started from the empty web (exact enumeration of growth histories; the frontier state space at `n ≤ 7` is tractable).
- **Per-arm weights**: V-cov (label-invariant read) and V-lab (label-reading), with the **`e(P)` linear-extension / labeled-history multiplicity accounting executed and disclosed per arm** — the C6 debt. The V-lab arm's induced unlabeled measure must be computed by *summing labeled-history weights over the `e(P)`-class*, never by dividing by a global count (paper 7 §4's sting: this is exactly where the history measure's anti-selection came from).
- **Two-layer bulk weight**: total mass on the KR-type (three-layer / two-layer-bulk) order classes per `n`.
- **The comparison frame**: the counting measure's KR-type share and the history measure's anti-selected share — at `n = 7`: **0.2405 → 0.3424** (paper 7 §4). These two numbers are the census's fixed goalposts.
- **The `g3` identity** as the consistency check on the induced-measure computation (the receipt asserts it per arm and per `n`).
- **Frontier-Markov ablation** (the third owed item): re-run the primary arm with the law's history-dependence truncated to the frontier state; the induced-measure distance (total variation, exact) between full-history and frontier-Markov versions measures how much of the law is genuinely non-Markov at census scale.

## 3. Theorem U alongside (the support and weight legs, stated for the receipt to instantiate)

- **Support leg [target: THEOREM]**: every web built by a C1–C7 law scored in the two-clock frame is a two-clock configuration, hence `dim ≤ 2` by construction (paper 13 Thm 2.1 constructive direction); with paper 7's realizer-pair count (`≤ (n!)²` labeled `dim ≤ 2` orders) against the `2^{⌊n²/4⌋}` two-layer bulk, bulk mass is unreachable at the **support** level — annihilation, not suppression. The census verifies the instantiation exactly: **every reached order at `n ≤ 7` must measure `dim ≤ 2`** (exact 2-dimension test at these sizes). One reached `dim ≥ 3` order = the leg's counterexample, halt and report.
- **Weight leg [fallback, for arms where support alone does not close]**: `μ_β(P) ≤ mult(P)·e^{−βS(P)}` gives free-bipartite suppression at explicit `β > 4 ln 2`. Only invoked if an arm's support turns out to include bulk-type orders.

## 4. Pre-registered gates (pinned now; the receipt asserts these verbatim)

- **G-A (support)**: 100% of reached orders at `n ≤ 7` are `dim ≤ 2`, per arm. FAIL ⇒ Theorem U's support leg has a counterexample — report, do not proceed to weights.
- **G-B (bulk share)**: each primary arm's KR-type share at `n = 7` is `< 0.2405` (beats the counting measure) — the pinned success line; `≥ 0.3424` (at-or-worse than the history measure's anti-selection) = the pinned failure line; between = MIXED, reported as measured.
- **G-C (arm agreement)**: V-cov vs V-lab induced measures per law — total-variation distance printed; if TV > 0.1 at any `n`, the covariance fork is *load-bearing* for this law and T4.2 (the fork made exact) promotes to next-round primary.
- **G-D (consistency)**: the `g3` identity holds per arm and per `n` (exact arithmetic; any violation = implementation bug, not physics — halt).
- **G-E (Markov ablation)**: TV(full-history, frontier-Markov) printed per arm; no pass/fail — a measurement with its number carried to the classification program (T4.3).

Verdict semantics per the house convention: gates that refuse print the gate ledger and the receipt exits 1 by design; [directional] tags on any read taken from < 8 histories per cell (at `n ≤ 7` exact enumeration should make this moot — if any cell falls back to sampling, that fallback is itself disclosed).

## 5. Kill conditions and what each outcome buys

- **G-A fails** ⇒ the two-clock support theorem is false as stated — the biggest possible negative, redirects Tier 4 to the weight leg immediately.
- **G-B fails on all primary arms** ⇒ the churn class *also* anti-selects at small `n` — the production mechanism has a measure-level pathology invisible to the cell (which scores single webs, not ensembles); the manifoldlikeness story would need ensemble-level repair. This is the sharpest possible census outcome and the reason u4 outranks further cell-level work.
- **G-B passes** ⇒ the growth measure beats counting at the exact scale where paper 7 showed history measures anti-select — the first *measure-level* (not single-web) manifoldlikeness evidence in the corpus, and Theorem U's census half is instantiated.

## 6. Receipt plan

`v9/code/u4_growth_census.py`: exact enumeration (integer/rational arithmetic for weights where the law's probabilities are rational; mpmath dps ≥ 50 otherwise — no float64 in the measure accounting), `default_rng` only if a sampling fallback triggers (disclosed), gate ledger printed, LOG/LEDGER entries per round discipline.

## References

Design note 8 (C6 the pre-registered fork; §4 G4; the receipts reservation); u-line memo + paper 17 (the executed u1–u3/u3b arc; the owed-items line); v8 paper 7 (Thm 4.1/Cor 4.2; §4 the census, 0.2405/0.3424); v8 paper 13 (Thm 2.1; the two-clock frame); v8 paper 16 (§4 churn membership); v9 LOG rounds 5–7 + LEDGER #46–#49 (the law-list collapse); Kleitman–Rothschild (1975); Brightwell–Henson–Surya CQG 25, 105025 (2008); Rideout–Sorkin PRD 61, 024002 (2000); PLAN.md T4.1–T4.3.

## Addendum (2026-07-05, round 10) — the exact-law reduction: the race model

**Theorem (the churn ranking law).** In any churn-class web (j3 corner, D1, kernel variant) with continuous per-commit increments, partition the commits into **slot-lives** (maximal runs of one slot between resets). Each life's committed χ values are the arrival-time prefix of a unit-rate Poisson process, independent across lives. Hence the **ranking** of all n committed values, conditional on the life-partition, follows the **sequential race model**: reading ranks from smallest, at each position every life with pending arrivals is equally likely to own the next value (memorylessness of the exponential race; verified in closed form on the {2,1} pattern: interleaving probabilities ½, ¼, ¼ — not the uniform ⅓ each). All probabilities are products of reciprocals of pending-life counts — **exact rationals**. The life-partition law itself is an exact-rational DP over (slot-choice, reset) sequences (denominators M^n L^n; slot exchangeability collapses M^n to set-partition patterns, CRP-style: P(join a specific used slot) = 1/M, P(fresh) = (M − used)/M). The induced unlabeled-order measure is therefore computable **exactly in `fractions.Fraction` arithmetic** — no float enters the measure accounting, per this note's §6 pledge.

**Corollary A (Theorem U's support leg, by construction).** Every churn web is the dominance order of (commit index, value rank) — an explicit 2-realizer — so **dim ≤ 2 holds identically** for the class; G-A reduces to verifying the construction per reached class rather than testing dimension blind.

**Corollary B (anchor).** When every life is a singleton (M → ∞ or all-reset), the race model gives the uniform random ranking: the induced measure is the 2D random box order exactly — the census's consistency anchor at every n.

**Corollary C (D1+atoms).** With atomic content the values are sums from a finite menu: comparisons are exact rational-arithmetic decisions with **ties possible** (ties ⇒ incomparability in the strict dominance order) — the atoms arm enumerates menu-choice sequences (3ⁿ) instead of the race model; still exact.

**Validation receipt `u4a_race_model.py` (this session):** exact n ≤ 4 induced measures for the j3 corner (M = 32, L = 2) via the reduction, against large-sample Monte Carlo of the *actual* j3 generator (the s8-ported code) — pinned gate: total-variation distance ≤ 3σ_MC per n, plus Corollary-B's anchor check. The full n ≤ 7 census (G-A..G-E, all arms, the paper-7 KR classifier) runs on this validated core next session.
