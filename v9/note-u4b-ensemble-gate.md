# u4b — the calibrated ensemble gate: TV-to-box with pinned bands, the contrast columns, the n-trend, and the L-sweep

**Status:** design note, 2026-07-05 (v9 round 11; the round-10 review's redirect — LEDGER #58: "TV-to-box discriminates where the KR statistic separates nothing"). Receipt: `v9/code/u4b_ensemble_gate.py`, on the u4a-validated exact core with the #58 classifier-contract repair. Gates pinned here BEFORE the run. **Disclosure of known values:** TV(corner, box) = 0.0304 (n = 6) / 0.0371 (n = 7) and TV(atoms, box) = 0.5694 (n = 7) were computed in u4's post-refusal analysis and are already on the record; the gates below are therefore pinned on the *new* quantities (the counting-restricted column, the n = 5 point, the L-sweep) and on *relations* the known values do not by themselves decide.

## 1. The object

The ensemble question, properly calibrated: how far is the builder's exact induced measure from the faithful target (the 2D box measure = the L = 1 anchor), **relative to the right yardsticks**? Yardstick 1: the *counting* measure restricted to the builder's own support (m_L over dim ≤ 2 classes, renormalized) — "a blind lottery over the legal shapes." Yardstick 2: the known-pathological atoms arm. The gate is a *separation* statement: the builder must sit closer to the target than the blind lottery by a pinned factor, and closer than the pathology by a larger one.

## 2. Pinned gates

- **G-1 (separation, the headline):** at n = 7, `TV(corner, box) < TV(m_L-restricted, box) / 3` AND `< TV(atoms, box) / 10`. (The second clause is decidable from known values only if TV(corner) were unknown — both are known; the clause is kept as a formal record. The first clause is a genuine prediction: the counting-restricted distance is uncomputed; the pinned expectation is that a blind lottery over legal shapes is *far* from the box — order 0.3–0.6 — because counting weights shapes, not histories.)
- **G-2 (the n-trend, registered two-regime expectation):** TV(corner, box) at n = 5, 6, 7 exact. Registered: *mild monotone rise* across 5 → 7 (the census sits in the pre-washout regime n ≪ L·M = 64, where lives lengthen relative to n); the discharge-relevant decay is the *large-N* regime's, already measured as q2's `C(L,M)·√(log N / N)` law — u4b's trend read documents the small-n end of the same pillar, it does not decide the limit. Gate form: the three values are printed exact; REFUSED only if the rise exceeds 2× per step (TV(6)/TV(5) or TV(7)/TV(6) > 2 — a runaway inconsistent with the washout picture), else HELD-as-expected.
- **G-3 (the L-sweep, registered prediction):** TV(corner_L, box) at L ∈ {2, 4, 8, 16}, n = 6. Registered per paper 16's renewal law (common-birth wall as L grows at fixed fleet): **monotone non-decreasing in L**, with L = 2 the minimum. REFUSED if any L > 2 sits strictly below L = 2 by more than exact-zero (Fractions: any strict decrease refuses).
- **G-4 (integrity):** mass exactly 1 for every computed measure; the m_L-restricted weights sourced from pE's `process_n` lab_mult through the #58 relabeling-safe path (weights keyed by canon_fast of pE's own rel — no classifier involved, so no contract issue; the mapping is verified by class-count equality 1956 and total-mass restriction ratio = the known geo share 1956-class m_L mass / A001035(7)).

Verdict semantics per the house convention: refusals print the gate ledger and exit 1 by design; every TV is exact (Fractions), floats only in prints.

## 2b. Post-run registration record (round-11 review)

The registered order-of-magnitude expectation for the new column ("order 0.3–0.6") **missed low**: TV(m_L-restricted, box) = 0.2734 — recorded per the house convention (the miss is itself evidence of genuine pre-registration; the gate's refusal region TV ≤ 0.111 was live). Precision note (review NIT-9): within G-2, the TV(7)/TV(6) sub-clause was pre-decided by the disclosed known values; the TV(6)/TV(5) sub-clause was the live one (refusal iff TV(5) < 0.0152).

## 3. What each outcome buys

G-1 held ⇒ the round-10 headline gets its calibrated form: the builder is not merely "legal-shaped" (support) but *history-weighted toward the target* — the ensemble-level manifoldlikeness claim at pinned grade, ready for the discharge assembly's Tier-4 slot. G-1 refused (the blind lottery is also close to the box) ⇒ the TV statistic is weakly informative too and the ensemble claim demotes to support-only — reported as such. G-3 refused ⇒ the renewal-law picture is wrong at census scale — a real finding against paper 16's arc, investigate before any further ensemble claims.

## References

LEDGER #57–#58 (the census + the review; the known TVs); note-u4 + Addendum (the exact core; the race model); u4a/u4 receipts; v8 paper 16 §4 (the renewal law; the common-birth wall — G-3's source); q2/note-q2 (the large-N D* rate law — the other end of the pillar); v8 paper 12 (the sufficiency theorem the discharge assembly will invoke); pE_phase_causalset (lab_mult source, used classifier-free).
