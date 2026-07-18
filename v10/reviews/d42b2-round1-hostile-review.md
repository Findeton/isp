# D42b2 round 1 — hostile review (elementary-click refinement, front 4)

**Reviewer:** independent hostile referee, fresh session, 2026-07-18.
**Object:** pin `v10/note-d42b2-elementary-click-refinement.md` (4c2ba31);
receipt `v10/code/d42b2_click_refinement_exact.py`; output
`v10/data/d42b2_click_refinement_exact.out` (7/7, exit 0); LOG #292–#293;
HEAD 122148a. Context read: paper 25 §10 (kernels), note-d42a §2 + A1–A8
(+ round-1 report §gate-quality), note-d42b1 (+ its receipt's actual
`admissible()`), the #152 texts (LOG #152 entry, the d42 pin's carry-in,
paper 25 §10.1).

**Method:** 4-seed rerun (byte-identity vs the committed .out);
independent re-implementations of BOTH refinements (my own chain
enumerators, greedy, MIS, census — no receipt code reused); the shape
census re-derived from first principles AND widened (payload x
comparability); the E3/E5/E7 anchors re-derived by driving the REAL
d42b1 `admissible()`/poset machinery (imported, definitions only);
seven mutation tests on receipt copies. Referee artifacts (scratchpad,
not committed): `referee_d42b2_independent.py` (17/17 green),
`mut_M-*.py`, the click-fixture repair demo.

## Verdict

**0 BLOCKER / 5 MAJOR / 6 minor / 3 nit. Zero false numbers.** Every
numeric claim in the pin, receipt, and LOG entry checked out exactly
under independent recomputation. All five MAJORs are gate-quality /
pin-semantics class: the mathematics survives; the receipt's
evidentiary architecture is below the campaign's own d42a round-1
standard (hand anchors missing where d42a had them, censuses printed
rather than gated, one pin sentence in direct tension with d42a A4).

| # | sev | class | one line |
|---|-----|-------|----------|
| M1 | MAJOR | ungated census | the five-shape / no-triangle claim is print-only — mutations that corrupt the domain both ways leave the receipt 7/7 GREEN |
| M2 | MAJOR | unanchored gate | the K2 block has no external anchor (maximality-dropped `mis_of` passes 7/7); pinned E4 domain included "triangle", silently dropped |
| M3 | MAJOR | gate theater | E3(iii) "resequence-invariance of the mini-fixture" is a 4-iteration cannot-fail toy; the one contentful case (concurrent alien click) crashes it |
| M4 | MAJOR | gate theater | the sector/budget layer is literals throughout (E3(ii) hand-anchor, E5 literal x literal, E7(b) tautology); D>1 never exercised |
| M5 | MAJOR | pin semantics | the click chain's carriers/atomicity are unpinned; "clicks ride the initiator's wire, enabled set past-computable" contradicts d42a A4 at click 1 |
| m1–m6, n1–n3 | minor/nit | below | |

## Independent verification (what I confirmed with my own code)

- **Census (claim 6).** My own enumeration: labeled connected
  0/1-realizable conflict shapes on n ≤ 3 = **exactly 5** (per-size
  1/1/3: vertex; edge; the three labelings of the 3-path). As
  isomorphism classes: **3** (vertex, edge, P3). Triangle NOT
  realizable. **Widened sweep** the receipt never argues: payloads x
  ALL comparability patterns (all 19 posets on 3 elements; conflict
  edge iff payloads differ AND incomparable — the pin's actual conflict
  relation): every arising connected component is still one of the same
  5 labeled patterns / 3 classes; no triangle; comparability deletions
  only produce already-censused smaller components. **Control:** payload
  alphabet {0,1,2} DOES realize the triangle — the corollary's scope is
  the BINARY payload rule (d42a §2 pins x ∈ {0,1}; note paper 25's
  record-ID payload field is alphabet-generic and §10.1 contemplates
  b-bit marks, so a future non-binary grammar re-opens triangles; the
  corollary must cite the binary rule, which LOG #293's "the 0/1
  payload rule" does — correct scope as worded).
- **E1 (claim 1).** My permutation-based enumerator: 6 chains, each
  exactly 1/6, per-click (1/3, 1/2, 1); pushforward {P,R} = 2/3,
  {Q} = 1/3 == my composite == paper 25 §10.2. Exact.
- **E2/E7(a) (claims 1, 4).** My chains + my greedy (adjacency-set
  implementation) on all 5 realizable shapes AND on
  triangle/P4/C4 controls: n! chains, uniform 1/n!, clicks
  1/(remaining), pushforward == composite, sums 1. Exact everywhere.
- **E4 (claim 2).** My K2 chain builder with an EXPLICIT decision-order
  parameter, run over EVERY decision order (all n!) on every shape:
  well-defined throughout — no zero-denominator branch is reachable
  (the recursion only enters branches with a consistent MIS, and the
  consistent set is nonempty from the root since `mis_of` is nonempty
  on any nonempty vertex set); the leaf is always unique and equals
  `decided_in`; every product = 1/#MIS; sums 1. Exact.
- **E3's anchor (claim on the 1/8).** Driven through the REAL d42b1
  `admissible()` (machinery imported from the committed receipt): the
  pair arb on [pA0, pB1] prices at **1/8 per winner**, with D = 1 read
  off the real `arb_components_in_view` + `merge_pairs` and the kernel
  1/2 from the real `PK1` — so 1/4 x 1/2 is the true grammar
  factorization, not just hand arithmetic. **Extension the receipt
  lacks:** I constructed a D = 2 record point in the real grammar
  (SIG_FM[:6] + a live v1-pair: `p(B,v1,0)`, `p(A,v1,1)`): real arb
  q = **1/16 = (1/4)/2 x 1/2**, and the fork-merge pair click at the
  same point also 1/16 — the budget-factorization identity holds at a
  NON-trivial sector share.
- **Claim 3 (merge click elementary).** Confirmed in the real grammar:
  the value-conflict merge is a single binary outcome at 1/2 inside
  the shared sector (1/8 at D = 1, 1/16 at my D = 2 point); the
  equal-value branch carries no click factor.
- **Claim 5 (finer basis).** Confirmed against the REAL `canon()`
  (d42b1's): same-wire orderings are canon-distinct; my click-typed
  fixture (below) gives distinct canonical DAGs for the two chain
  orders at equal winner.
- **Plumbing.** PYTHONHASHSEED 0/1/42/31337: byte-identical to the
  committed .out, exit 0, <1 s (LOG's 0/53 consistent, wider than my
  check). No randomness source; all prints sorted or
  iteration-deterministic. Wrong-expectation mutation (M-C) and
  click-law corruption (M-D) both exit 1 cleanly.
- **Greedy fidelity (attack d).** The receipt's conflict-graph greedy
  is the d42a round-1 §gate-quality (f) accepted abstraction of paper
  25 §10.2's "participants remain unused" (the D36-carrier conflict
  relation); it reproduces 2/3–1/3 on the path. Consistent with
  precedent; no finding. (K3 is not refined here — consistent with the
  d42a grammar's supplied-kernel set K1/K2; K3 is a regional family
  that can select empty/nonmaximal sets, not a per-component draw.)

## MAJOR findings

### M1 (CONFIRMED). The five-shape census and the triangle corollary are ungated — print-only

`SHAPES = realizable_shapes(3)` is printed (`realizable connected
shapes (n <= 3): 5`) and never asserted. E2's own detail string —
"realizability itself gated by construction" — is false as worded:
a construction is not a gate. Mutation evidence (receipt copies):

- **M-A (triangle wrongly ADDED to the domain):** receipt runs
  **7/7 GREEN, exit 0** — E2/E4/E7 happily verify the refinements on
  the triangle (they are graph-generic identities) and nothing checks
  that it should not be there.
- **M-B (all three n = 3 shapes silently DROPPED):** **7/7 GREEN,
  exit 0** — the sweep hollows to 2 shapes undetected.

So the receipt cannot distinguish the true domain from a corrupted one
in either direction, yet LOG #293 and the commit headline the census
("exactly FIVE — the 0/1 payload rule FORBIDS triangles, an implicit
structural census"). "Implicit" is the defect: this program's own
standard (d42a A4/G2: hand-derivable censuses gated at exact values)
requires the census asserted. The CLAIM is true — referee-verified
above, including the widened comparability sweep and the {0,1,2}
control — but nothing in the receipt would have caught it being false.

**Repair (pre-verified, my suite runs all four green):** assert
`len(SHAPES) == 5` with per-size counts (1, 1, 3); assert no shape
contains an odd cycle / triangle-free; assert the {0,1,2}-payload
control DOES produce the triangle (so the gate demonstrably bites at
the boundary); print the isomorphism-class count 3 alongside (see m1).

### M2 (CONFIRMED). The K2 block has no external anchor; the pinned E4 domain silently shrank

- **Mutation M-G:** corrupt `mis_of` to return ALL independent sets
  (drop the maximality filter — i.e. delete K2's safety/progress
  content). The FULL receipt stays **7/7 GREEN, exit 0**. E4 verifies
  `k2_chain_weights` against the same corrupted `mis_of` and
  `PK2_composite` against the same list — pure self-consistency.
  Paper 25 §10.3's path anchor (1/2–1/2) is nowhere in d42b2 (it was
  gated in d42a G5; this receipt's K2 numbers are anchored to nothing
  outside themselves). Contrast: K1 has E1's hard-coded 2/3–1/3.
- **Pin drift:** pinned E4 reads "on path + star + **triangle** + all
  censused shapes". The receipt never runs the triangle anywhere —
  the census excluded it and the pin promise was silently dropped
  rather than amended (the program's own forward-correction discipline,
  A5'/A7' style, requires the declared amendment). The construction
  handles the triangle fine as an abstract control — my run: chains
  land on the 3 singleton MIS at exactly 1/3 each, conditionals
  {1/3, 2/3} — it just was never run.

**Repair (pre-verified):** (i) hard-assert the path K2 pushforward
== {{P,R}: 1/2, {Q}: 1/2} (paper 25 §10.3 literals), symmetric to
E1; (ii) add the structural cross-tie `set(P_K1 support) ==
set(mis_of(...))` per shape — I verified it holds on all 5 shapes + 3
controls, and it catches BOTH mutation classes (M-G: corrupted MIS
list contains non-maximal sets that greedy never produces; M-E:
corrupted greedy leaves the MIS support); (iii) run the triangle as a
declared ABSTRACT control (unrealizable in-grammar, exercised as a
graph), which also gives the K2 non-uniformity its only ≤3 witness
(see m2).

### M3 (CONFIRMED). E3(iii)'s "resequence-invariance" gate is a cannot-fail toy; the contentful case crashes it

The pin promises "(iii) resequence-invariance of the mini-fixture with
the click chain in place (other-actor gauge preserved)". What the
receipt computes: a 4-iteration loop inserting `('x','b')` into a
3-element list, collecting values of `chain_weight_at(prefix, 2)` — a
function of the chain-prefix COUNT by construction. No event poset, no
admission, no linear-extension machinery, no canon; the alien's
position CANNOT enter the computed value. This is claim-wider-than-
computation (attack b: confirmed) and a cannot-fail simulation
(attack a: confirmed).

- **Mutation M-F:** make the alien a click on wire b (`('k','b')`) —
  the physically REAL interleaving case: two disjoint components
  arbitrated concurrently, which is exactly paper 25 §10.2's
  "cross-component shuffles of a global presentation order are gauge"
  lifted to chains, and which the d42b1 grammar generates. The toy
  **crashes** (`ZeroDivisionError: Fraction(1, 0)`) — its global
  prefix counter conflates the two chains. The one interleaving
  scenario where refined-grammar resequence-invariance has content is
  unrepresentable in the gate that claims to test it.

The law-level claim itself is sound (click weights are past-functions;
an incomparable event is in no click's past; every linear extension
preserves every factor — two lines), and I verified it with real
machinery: a click-extended fixture on the d42b1 poset
(`event_poset`/`linear_extensions`-equivalent enumeration, alien
actor-C idle floating free): **12 linear extensions per chain, every
factor invariant under prefix-recompute, pushforward = 1/8 per winner
== the real composite q, canon-distinct chains**. So: PLAUSIBLE →
referee-CONFIRMED at the law level; the receipt's gate remains
theater.

**Repair (choose one; both program-consistent):** (A) the real thing —
extend the d42b1 alphabet with typed click events and run the G1-class
resequence-and-recompute gate on the click-refined mini-fixture family
including an alien actor AND the two-disjoint-component concurrent-
chain case (my demo shows the cost is small); or (B) re-scope per the
d42a A4/G2 precedent: declare the invariance DEFINITIONAL
(past-computability ⇒ extension-invariance), delete the toy loop, and
NAME the concurrent-chain and mid-chain-drift questions as carried
obligations of the full refinement (they are currently unnamed; RF3's
"blow-up" clause covers enumeration size, not law definition).

### M4 (CONFIRMED). The sector/budget layer is hand-anchored literals end-to-end; D > 1 never exercised

Three gates share one defect — no gate ever computes a sector share
from the grammar:

- **E5 is theater in the strict sense** (attack a: confirmed): it
  multiplies two literals and compares to literals
  (`F(1,4)*F(1,2) == F(1,8)`; `F(1,4) == F(1,4)`). No mutation of
  anything outside its own two lines can fail it. Yet LOG #293 records
  "E5 the merge click binding (d42b1 RF5 discharged)". A discharge
  that touches no d42b1 object discharges nothing.
- **E3(ii)** hard-codes `sector = F(1, 4)` where the pin promised
  "== the d42b1 composite arb q exactly". The banner honestly declares
  the hand-anchoring (RF3 "self-contained") — but pin ≠ receipt, and
  the pin's wording is what the round adjudicates.
- **E7(b)'s "budget factorization identity"** is
  `sector * p == sector * push` immediately after E2 gated
  `p == push` — multiplying both sides of an already-gated equality by
  the same literal. Tautology. The factorization claim (§2 bullet 4:
  "the refinement lives strictly INSIDE the arb event's share") has
  content exactly where the share is nontrivial (D > 1, the sector
  split over components + merge pairs) — never tested.

All three VALUES are correct — referee-verified against the real
d42b1 `admissible()`: pair arb 1/8 with D = 1 and kernel 1/2 read off
the real machinery; merge pair click 1/8 at D = 1; and at my
constructed D = 2 record point (SIG_FM[:6] + live v1-pair) both the
arb and the merge price at **1/16 = (1/4)/2 x 1/2** — the
factorization identity at a non-trivial share.

**Repair (pre-verified above):** import (or verbatim-embed) the d42b1
admission layer and gate E3(ii)/E5/E7(b) against `admissible()`
outputs at BOTH a D = 1 and a D = 2 record point; the D = 2
construction in my referee script is 8 events and runs in
milliseconds.

### M5 (CONFIRMED, pin-level). The click chain's carrier/atomicity semantics are unpinned — and the pinned sentence contradicts d42a A4 at click 1

Pin §2 K1: "Prior clicks ride the initiator's wire, so each click's
enabled set is past-computable." But the FIRST click's enabled set is
the component C — and d42a A4 (the adjudicated grammar) says: "the
initiator alone cannot see the component; the join is precisely where
it first exists as a record." A click with carriers {a} has only the
initiator's own singleton view in its past; under the A7 admission
discipline (opportunity = past-local admission and NOTHING else) an
initiator-wire-only click 1 referencing C is inadmissible — the chain
cannot start. The pin never declares the click events' carrier sets at
all, and oscillates between two readings with DIFFERENT physics:

- **atomic reading** ("the refinement lives strictly INSIDE the arb
  event's share"): the chain is fine structure of the one join event —
  then mid-chain drift/interruption questions vanish, but the "finer
  record basis" is finer only AT the join point;
- **multi-event reading** ("prior clicks ride the initiator's wire"):
  the chain is a sequence of grammar events — then click 1 must itself
  be join-typed (carriers = C's proposers) for past-computability, and
  the pin must say what the local law does BETWEEN clicks (are other
  sectors open mid-chain? can a mid-chain delivery supersede the base?
  does the component drift?) — none of which is defined.

Which reading nature is offered is exactly the d42b4 empirical
question the pin defers (RF1), so the ambiguity is load-bearing.
The receipt's toy instantiates no carriers and is compatible with
both readings — it gates neither.

**Repair (pre-verified):** one declared paragraph choosing the
semantics. The multi-event reading works: my fixture types click 1 as
the chain-opening JOIN (carriers = C's proposers, A4-consistent; C in
the event data per A6's ckey convention), later clicks on the
initiator wire, acceptance deterministic and version-creating — the
real-poset run lands pushforward 1/8 == the composite with all
extensions factor-invariant. Alternatively declare the atomic reading
and strike the "initiator's wire" sentence. Either way, name mid-chain
drift (component growth / base supersession between clicks) as a
carried question of the full refinement — it is the refinement's
analogue of paper 25 §11.1's batch-closure and currently appears
nowhere.

## minor findings

- **m1 (CONFIRMED).** "Exactly FIVE shapes" counts LABELED edge
  patterns; the three n = 3 entries are relabelings of one graph. The
  honest census is "5 labeled patterns, 3 isomorphism classes (vertex,
  edge, path)". The pin's own unit "(size, edge pattern)" makes 5
  well-defined, but the LOG headline should carry the clause —
  "five" overstates the structural content by conflating labelings.
- **m2 (CONFIRMED).** K2's "recorded, NON-uniform" has no witness in
  the tested domain: my sweep over every realizable shape and EVERY
  decision order finds every conditional in {1/2, 1} — i.e. within
  the census, K2's refinement is per-click uniform-or-forced, exactly
  like K1's. The non-uniform witness first exists on the FORBIDDEN
  triangle (1/3, 2/3) or at n = 4 (P4 first click 2/3 — and P4 is
  in-grammar realizable at n = 4 only via comparability deletion,
  outside the receipt's all-incomparable sweep rule). RF2's "new
  K1-vs-K2 discriminator" is therefore a claim about untested
  territory, and E4's printed "non-uniform — DECLARED" label is wider
  than every tested instance. Repair: one declared sentence + the
  abstract triangle/P4 control prints (M2 repair (iii) provides the
  witness).
- **m3 (CONFIRMED).** The K2 refinement is canonical-order-RELATIVE
  and the pin does not declare it: the click RECORD identities depend
  on the decision order at every n ≥ 2, and beyond the tested sizes
  the conditional VALUES do too — witness (my run): P4, same MIS
  {0,2}, same product 1/3, clicks (2/3, 1, 1/2, 1) under order
  (0,1,2,3) vs (1/3, 1, 1, 1) under (2,0,1,3). At n ≤ 3 the weights
  happen to coincide across orders (verified), so the dependence is
  latent in the receipt. K1's refinement needs no such convention —
  itself a structural K1-vs-K2 asymmetry worth the RF2 list. Repair:
  declare the canonical order part of the posited refinement (a
  convention the record basis inherits).
- **m4 (CONFIRMED).** E6 theater (attack e): `canon_chain` embeds the
  order in the record by construction — distinct orders give distinct
  tuples with certainty; no grammar canon is exercised. The claim is
  trivially true and ALSO true in the real machinery (verified: d42b1
  `canon()` separates same-wire orderings; my click fixture's canonical
  DAGs are distinct at equal winner). Repair: one line driving the
  real canon on click-typed events, or a declared-definitional note.
- **m5 (CONFIRMED).** E2/E7's shared-map blindness: both sides of
  "pushforward == composite" use the same greedy/conflict conventions.
  Referee run: corrupt greedy CONSISTENTLY in both code paths and
  remove E1's two anchor lines — E1, E2, E4, E7 all PASS (6/7; only
  E3's hand-anchored 1/8 fails). So E2's shape-wide "exactness" is
  enumerator-consistency; external correctness rides entirely on three
  hand-anchored literals (2/3, 1/3 at the path; 1/8 at the pair). With
  E1/E3 present the receipt IS protected for K1 (M-E crashes E1,
  exit 1) — hence minor, not MAJOR — but the per-shape claim should be
  worded as consistency, and M2's `support == MIS` cross-tie anchors
  every shape structurally.
- **m6 (CONFIRMED).** The sector share's PLACEMENT is unpinned: §2
  bullet 4's product formula carries "(sector share)" as an ownerless
  factor — which record point pays it (the chain-opening join click,
  as in my demo, or the acceptance) is undeclared, and the mid-chain
  budget state (what is enabled on the initiator's wire between
  clicks) is undefined. Both feed d42b3 (placement) and d42b4 (record
  basis). Repair: fold into M5's declared paragraph.

## nits

- **n1.** E2's `ok2 &= (... if len(items) == 1 else ok2)` is a no-op
  for 4 of the 5 shapes — dead conditional dressed as a gate line
  (chain uniformity is actually gated by E7). Delete or hoist.
- **n2.** Click ontology inconsistency: forced (q = 1) outcomes are
  RECORDED clicks in the K1/K2 chains (E1 checks ws[2] == 1; K2
  records forced membership decisions) but the equal-value merge's
  forced outcome is "no click" (pin §2). Whether forced outcomes are
  records is itself record-basis content for d42b4 — declare one
  convention.
- **n3.** "#152-form" is used in two senses inside one pin: §2-K1
  glosses it "uniform over the enabled set…", while §2-K2/RF2 argue
  #152 requires recordedness + fixed budget, NOT per-click uniformity;
  E7's gate name inherits the uniform gloss. The RF2 reading itself is
  **defensible — CONFIRMED against the actual texts** (attack c): LOG
  #152's design standard is "redistribute a fixed interaction budget"
  with controls — its founding instance (paper 20's directional
  variant) is non-uniform redistribution BY DESIGN; the d42 pin's
  carry-in demands "conflict/arbitration randomness as recorded click
  outcomes"; paper 25 §10.1 demands a "recorded click outcome, not an
  external coin". No text demands per-click uniformity. One clarifying
  clause kills the internal ambiguity.

## What survives (with verified numbers)

1. **K1 refines exactly** (claim 1): n! selection-click chains, each
   click 1/(remaining), chain weight 1/|C|!, greedy deterministic,
   pushforward == composite — referee-verified with independent
   enumerators on all 5 realizable shapes AND triangle/P4/C4 controls;
   path anchor {P,R} 2/3, {Q} 1/3 == paper 25 §10.2.
2. **K2 refines exactly and is well-defined** (claim 2): binary
   membership chains, exact MIS-count conditionals, no reachable
   zero-denominator branch, unique leaf, product 1/#MIS, pushforward
   uniform — verified for EVERY decision order on every shape. Caveats
   m2/m3: within the tested domain the conditionals are all {1/2, 1}
   (per-click uniform), and the construction is canonical-order-
   relative.
3. **The merge pair click is already elementary** (claim 3): confirmed
   in the REAL d42b1 grammar — single binary 1/2 inside the shared
   sector; 1/8 at D = 1 and 1/16 at my constructed D = 2 point.
4. **The budget factorization** (claim 4): TRUE and now verified
   against the real grammar at D = 1 (1/4 x 1/2 = 1/8, with D and the
   kernel value read off `admissible()`'s own components/merge-pairs/
   PK1) and at D = 2 (1/16) — though the receipt's own E7(b) gate is a
   tautology (M4).
5. **The finer record basis** (claim 5): real — distinct click orders
   are canon-distinct at equal winner in the real canon; the
   fine-vs-coarse deferral to d42b4 (RF1) is properly declared.
   M5's carrier ambiguity must be resolved for the basis to be
   well-posed as an empirical offer.
6. **The census** (claim 6): 5 labeled patterns / 3 isomorphism
   classes; the BINARY payload rule forbids triangles — verified
   independently, including the widened payload-x-comparability sweep
   (components stay within the 5) and the {0,1,2} control (triangle
   realized; scope is the binary rule; paper 25's payload field is
   alphabet-generic, so the corollary is d42a-instance-scoped). The
   receipt merely never gates any of it (M1).
7. **Plumbing:** deterministic, 4 seeds byte-identical to the
   committed .out, exit-1 mutations work (M-C, M-D), <1 s. The greedy
   is the d42a-round-1-accepted abstraction of paper 25 §10.2.

## Prescribed repairs (all pre-verified in the referee scripts)

1. **Gate the census** (M1): assert len == 5, per-size (1,1,3),
   triangle-free, and the {0,1,2} boundary control; print iso-class
   count 3.
2. **Anchor K2** (M2): hard-assert path K2 == 1/2–1/2 (paper 25
   §10.3); add `support(P_K1) == mis_of` per shape (kills both M-E and
   M-G mutation classes); run the triangle as a declared abstract
   control (products 1/3; conditionals {1/3, 2/3} — the m2 witness).
3. **Replace or re-scope E3(iii)** (M3): real click-extended
   resequence gate incl. the concurrent-chain case (demo exists), or
   declared-definitional per the d42a precedent — and NAME mid-chain
   drift as a carried question.
4. **Make the sector real** (M4): gate E3(ii)/E5/E7(b) against d42b1's
   `admissible()` at D = 1 and the 8-event D = 2 context (1/16 both
   arb and merge).
5. **Pin the click semantics** (M5 + m6): one paragraph — carriers
   (join-typed click 1 per A4/A6, or the atomic reading), sector-share
   placement, mid-chain budget state.
6. One-clause repairs: m1 (labeled/iso wording), m2/m3 (declarations),
   m4 (real canon or definitional note), m5 (consistency wording),
   n1–n3.

The exactness mathematics of this front is correct and now
independently confirmed; what the round demands before TERMINAL is
that the receipt's gates be made as honest as its numbers.
