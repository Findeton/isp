# D42b2 — the elementary-click refinement of the kernel draws (front 4)

**Status:** CAMPAIGN PIN (strict), 2026-07-18. Parent: d42a TERMINAL
(#289), d42b1 GREEN (#291, round in flight — this front is
independent of that round's outcome: it refines the KERNEL layer,
which survived d42a round 1 unconditionally). Receipt:
`v10/code/d42b2_click_refinement_exact.py`.

## 1. The object and the claim

d42a RF3 admitted the K1 winner draw as ONE composite recorded click
(uniform over |C|! orders + greedy). The #152 standard wants
randomness as ELEMENTARY recorded click outcomes. Claim: both kernel
draws and the merge click refine EXACTLY into chains of elementary
recorded clicks with past-conditioned Fraction weights, preserving
every composite weight; the refinement changes the RECORD BASIS
(finer records exist in the refined grammar), and which basis nature
seals is an EMPIRICAL question deferred to the lift (d42b4), where
the NSE/D25/D27 gates apply per record type.

## 2. The refinements [POSITED; exactness gated]

- **K1 (order + greedy).** The order draw = a chain of SELECTION
  clicks on the initiator's wire: at stage i, ('k', a, C, t) selects
  the next proposal uniformly from the |C|−i+1 remaining, q_i =
  1/(|C|−i+1); the chain weight is exactly 1/|C|!. Greedy is a
  DETERMINISTIC map from the completed order to the winner set
  (acceptance carries q = 1 given the chain). The composite kernel is
  the pushforward: P_K1(w|C) = Σ over orders mapping to w of 1/|C|!.
  Prior clicks ride the initiator's wire, so each click's enabled set
  is past-computable (#152-form: uniform over the enabled set,
  conditioned on causal past). Within the chain there is no gauge
  freedom (one wire, totally ordered); gauge with other actors'
  events is untouched.
- **K2 (uniform maximal).** A chain of BINARY membership clicks over
  the component's proposals in canonical order: at each stage,
  include/exclude t with conditional weights = (#MIS consistent with
  decisions so far and t in) / (#MIS consistent so far), etc. Every
  conditional is an exact Fraction; every completed chain lands on
  exactly one MIS with product weight 1/#MIS. Clicks are recorded;
  weights are past-conditioned but NOT uniform — #152 requires
  recordedness and fixed budget, not per-click uniformity (declared).
- **The merge click (binds d42b1 RF5).** The value-conflict pair
  click is ALREADY elementary (uniform binary, 1/2); the equal-value
  merge is deterministic (no click, q = 1). Nothing to refine; gated.
- **Budget factorization.** The sector price is untouched: the
  composite q = (sector share) × P_K(w|C) factors as (sector share) ×
  Π(elementary click weights) × 1(deterministic acceptance) — the
  refinement lives strictly INSIDE the arb event's share.

## 3. Gates (exit 1; exact equality)

E1 the path component P-Q-R: all 3! chains at weight exactly 1/6;
pushforward = {P,R} 2/3, {Q} 1/3 == the composite (paper 25 §10
numbers preserved under refinement). E2 the component-shape sweep:
for EVERY distinct component shape (size, edge pattern) arising in
the d42a-family census (sizes 1-3, all patterns), pushforward ==
P_K1 exactly; same for K2's chain == P_K2. E3 the refined mini-
fixture: the pair-conflict arb implemented WITH click events —
(i) every click uniform over its remaining set; (ii) Σ over chains of
(sector share × chain weight) == the d42b1 composite arb q exactly;
(iii) resequence-invariance of the mini-fixture with the click chain
in place (other-actor gauge preserved). E4 K2 chains: conditionals
exact, product = 1/#MIS per MIS, pushforward == P_K2, on path + star
+ triangle + all censused shapes. E5 the merge-click binding (1/2
elementary; equal-value deterministic) at the d42b1-anchored values.
E6 record basis: two distinct click orders yield distinct canonical
DAGs (finer basis exists); the pushforward-coarsening declared, the
fine-vs-coarse question EMPIRICAL, deferred to d42b4 with NSE gates.
E7 #152-form conservation: every click weight has the exact
enabled-count form; the budget factorization identity gated.

## 4. Scope and risks

RF1 no claim about WHICH basis nature seals (empirical; lift-front).
RF2 K2's non-uniform conditionals are declared, not hidden — if a
referee reads #152 as demanding per-click uniformity, the honest
statement is: K1 refines uniformly; K2 refines recordedly; the
difference is itself a discriminator between the kernels (a NEW
observable of the refinement, noted for d42b7's second-grammar
protocol). RF3 the refined grammar is exhibited on the MINI-fixture
only (full-family click-refined enumeration is a blow-up; declared,
not needed for the exactness claims).
