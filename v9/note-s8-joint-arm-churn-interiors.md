# s8 — the two receipts paper 3's round-1 review demands: (A) the joint fully-centered arm; (B) churn's interiors under the arc's own instruments

**Status:** design note, 2026-07-05 (v9 round 9; paper-3 review round 1, science referee MAJOR-1 and MAJOR-2 — both repairs are experiments, not rescopings, per the referee's own urging). Receipt: `v9/code/s8_paper3_repairs.py` (one receipt, parts A + B, seed `default_rng(20260716)`). Gates pinned here BEFORE the run. Machinery: s7's calibration + s5/s6b's menus/instruments verbatim; `web_j3` ported verbatim from v8 `u1_growth_positive_control.py` (M = 32, L = 2 — the paper-16 corner parameters).

## Part A — the joint arm (MAJOR-1): both terms centered at their faithful expectations

The untested member: **ΔS̃ = [ΔS_A − c·|D|] + [S̃_comp(ρ)-increment]** — the per-pair allowance AND the stage-priced global block together, i.e. note-s6 §1's derivation shape *completed*. Admissible for c < ¼ (arm B's wall arithmetic; arm C adds nothing at the endpoint). The review's arithmetic, **registered as predictions**: at the derived point c = c̄ (the arrival-level faithful mean per-pair charge, re-calibrated in-run alongside ρ(t)), truth beats the **empty set** at typical loss steps (margin ≈ +2 at the s7 anatomy's means); the open question is the large decoys, whose per-element Row-A charges (kernel-floor interiors) sit near c̄ — the measurement decides.

Measured on forced-faithful trajectories (4 reps, t ≥ 64, the 14-candidate menus, tie-generous `≤`), **paired on one evaluation per candidate** (A, C_ρ, |D| computed once; the c-grid scored arithmetically):

- **A1 — the joint family curve**: truth-win rate at c ∈ {0, 0.05, c̄, 0.15, 0.20, 0.24} on the staged base. (The c = 0 column is arm C's measurement on this stream — its own consistency anchor, expected ≈ 1–2%.)
- **A2 — staged-base dominance** (the M3-analogue): fraction of steps carrying a decoy both **larger and staged-cheaper** than truth (truth loses there at every c ≥ 0 — the exact algebra of s6b M3, base swapped).
- **A3 — the staged-base per-step oracle** (the M4-analogue): fraction of steps where ANY c ∈ [0, ¼) makes truth the argmin, from the exact per-step feasibility windows. **This bounds the entire two-term family** (any profile assigns one c per step).

**Pinned gates.** **G-A1 (the branch, at the derived point c̄):** rate ≥ 0.6 ⇒ JOINT-PREFERRED (the production line reopens; the free-run bench G-A2 decides the grade); ≤ 0.3 ⇒ REJECTED; else MIXED. **G-A2 (the bench, runs whatever the branch):** free-run pure-kernel endpoints under the joint action at c̄, 4 reps — r ∈ [0.35, 0.60] all reps, r_I ∈ [0.35, 0.65] ≥ 3/4, m_ab ≤ 3× the 3-sprinkling faithful base. **The class verdict rides A3, stated in advance:** A3 < 0.3 ⇒ the two-term family is closed class-wide and paper 3's part (5) becomes TRUE as written (upgraded from four-actions to the family bound); A3 ≥ 0.3 ⇒ a live window exists — the surviving-arm finding, and paper 3's part (5) is rewritten around it. Chance line [7.1%, 7.7%] carried; rep-level t printed.

## Part B — churn's interiors (MAJOR-2): the builder faces the arc's instruments

No receipt in the corpus has pointed the interior instruments (heredity r_I, abundance misfit m_ab) at a churn web; churn's credential is the three-layer cell (coarser instruments). The bench every action arm faced, now applied to the builder:

- Webs: `web_j3` (trivial-Φ churn corner, M = 32, L = 2) at **N ∈ {256, 512}**, 4 reps each; the causal order = the dominance order on the (b, χ) stream (paper 13's two-clock reading; b strictly increasing, χ continuous — ties measure-zero). The uniform-victim kernel variant (`web_kernel`, u2's β = 0) runs as an **ungated INFO row** (2 reps per N).
- Instruments: global r; r_I = `heredity_axis2`; m_ab = `sampled_mab2` against the 3-sprinkling faithful base **at matching N** (the estimator's ≤ 256 interval filter binds at N = 512 exactly as in the s2 usage — disclosed).

**Pinned gates (per N, the arc's own bench):** **G-B1:** r_I ∈ [0.35, 0.65] in ≥ 3/4 reps. **G-B2:** m_ab ≤ 3× the matching-N faithful base. Both directions live, stated in advance: **pass ⇒** the builder's interiors are certified at n ≤ 512 [DEMONSTRATED — the paper-3 slogan "churn builds" gains its missing grade]; **fail ⇒ NOTHING tested builds** — the campaign's sharpest possible outcome; paper 3 §5 and the Tier-4 redirect are rewritten around it (the census question then includes "where does churn's interior pathology live?"), and the verdict is recorded with the same prominence every action-arm refusal received.

## Verdict semantics

House convention: refused pinned gates print the gate ledger and exit 1 by design; branch verdicts recorded whatever they are; [directional] on any cross-receipt comparison (fresh seed, unpaired); mechanism claims ride within-stream decompositions only. The A3 oracle and A2 dominance get the s6b I-check treatment (internal consistency: wins-at-c ⊆ feasible; dominated ⊆ infeasible).

## References

Paper-3 round-1 reports (science MAJOR-1/MAJOR-2 — the c* arithmetic 0.051–0.080 < c̄ adopted as registered predictions; the churn-interior gap); note-s6 §§1,3 (the allowance's wall arithmetic; c̄'s definition); note-s7 (ρ(t); the stage-priced base); s6b (the M2/M3/M4 machinery being base-swapped); v8 u1 (`web_j3`/`web_kernel` verbatim; M = 32, L = 2); v8 paper 16 §4 (the cell churn passed — the coarse credential part B refines); v9 paper 2 (the kernel floor the churn interiors are measured against); LEDGER #53.
