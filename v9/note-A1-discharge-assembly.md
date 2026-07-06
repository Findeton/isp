# A1 — the discharge assembly: design note for v9 paper 4 ("Growth implies spacetime")

**Status:** design note, 2026-07-06 (v9 round 13; think-first — the paper is rounds-14+ work). The target: paper 7 §5's discharge sentence, made a theorem. This note fixes the paper's statement, its imports, its consolidated proof obligations, and its honest scope, before any drafting.

## 1. The theorem the paper assembles

**Theorem D (the discharge; target statement).** For the churn class — click-law growth with fleet M, lifetime law sub-geometric with mean L, atomless content — the record web at size N satisfies, with probability → 1 as N → ∞:

1. **Geometry:** dim ≤ 2, identically (Theorem U — the two-clock 2-realizer, constructive; census set-equality at n ≤ 7: reached = exactly the dim ≤ 2 classes).
2. **Volume:** D*_N → 0 at rate O(√((τ_mix + log N)·log N / N)), τ_mix = O(L·M) (Theorem W — four lemmas, joints verified in w1).
3. **Statistics:** band-regime interval counts → Poisson at the dependency-density rate, with the sub-geometric hypothesis load-bearing (Theorem P″ — the t23 cycle; the heavy-tail boundary measured as a divergence).

Hence, by paper 12's sufficiency theorem (volume-faithful ⟺ dim ≤ 2 + vanishing canonical discrepancy) and paper 7's finite-N bridge (|r − ½| ≤ 14·D* + 1/(N−1), N ≥ 7): **click-law growth produces volume-faithful 2D record webs — spacetime-shaped order — in the limit, entering all three layers of the manifoldlike cell.** The ensemble complement (exact at census scale): the induced measure beats counting at n = 7 and sits at TV = 0.037 from the box ensemble (u4/u4b) — the measure-level face of the same statement.

## 2. Imports table (each named in-paper, once)

| Import | Source | Role |
|---|---|---|
| Sufficiency theorem | v8 paper 12 | (dim ≤ 2 ∧ D* → 0) ⇒ volume-faithful (the ⇐ direction, exact) |
| Finite-N bridge | v8 paper 7 §II | the quantitative certificate, N ≥ 7 |
| Chen–Stein | Arratia–Goldstein–Gordon (1989) | Theorem P″'s TV bound |
| Mixing-DKW (VC-2) | Rio / Doukhan class | Theorem W's Lemma W4 |
| The substrate ledger | v8 paper 16 | what (M, L) mean physically; the derived-supply parameter frame |
| The race model | note-u4 Addendum (u4a-validated) | W2/P1's conditional-independence engine |

## 3. Consolidated proof obligations (what the paper must write out; nothing else blocks)

From w1 §3: (1) W1's drift/minorization argument (τ_mix = O(LM) formally); (2) the cold-start TV-transient bound (O(τ_mix), the measured profile as companion); (3) the mixing-DKW conditions checked against W1's β-mixing; (4) the F-continuity statement (shared with P″'s atomless hypothesis — one lemma, stated once).
From t23 §§3/5/6/8: (5) the ranking-measurability lemma (band counts are ranking-functionals — extends the race model to counts); (6) boundary-interval accounting (edge effects O(1/N)); (7) k-stratification (band uniformity); (8) the mean-model-bias lemma (why the pooled instrument floors at ≈ 0.6 even for the box — the reference-floor discovery, stated as an instrument theorem); (9) the qualifying-class constant's lifetime-shape factor — **pending the t23 review's V3″ adjudication** (det/geom = 1.17 in-band vs the cv²-ordering in-pooled; the paper carries whichever resolution the review certifies).

## 4. Honest scope (the paper's §-last, pinned now)

2D record-native only (the 3+1 face is the tomography/coupling line — separate); the churn class at fixed (M, L) with atomless content — **the atomic corner is excluded by hypothesis and is the measured pathology, disclosed as consistency, not swept**; limits in N with finite-N certificates where available; cell membership at finite N remains band-calibrated measurement (the reference-floor theorem explains why); the KR/entropic question beyond census scale deliberately unclaimed (the exact-n ≤ 7 result + the rate laws are what is owned); Theorem D says nothing about *which* (M, L) nature realizes (paper 16's ledger) nor about content magnitudes (the standing no-gos).

## 5. Receipts and history the paper cites

u4a/u4/u4b (the exact census line; #57–#60); w1 (Theorem W's joints; the round-12 adjudicated amendment cycle); t23 (three pins, three runs, all git-frozen: d9189b3 → f959aeb → 9c053a1 → d0f9d87 → 080fd89 → 5997d75 — the freeze discipline's first full demonstration, to be cited as the paper's methods exhibit); the s5–s8 arc (paper 3) as the negative complement (why growth is churn and not action-argmin).

## 6. Sequencing

Blocked only on the t23 review (in flight at this note's commit). Then: draft (rounds 14+), hostile reviews till pass, confirmation. Paper name: `relativistic-isp-v9-paper4-discharge.md`.

## References

Papers 7/12/16 (the imports); notes w1/t23/u4(+Addendum)/u4b (the pillars); v9 papers 1–3 (the action arc the discharge complements); LEDGER #57–#62; PLAN §0 (the campaign target this note discharges).
