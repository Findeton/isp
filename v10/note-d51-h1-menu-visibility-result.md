# D51 — result: (H1) IS NOT REDUCED IN THE CLAIMED DIRECTION. The projections REFINE sigma; the durable content is three refutations.

**Status:** ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.  Round 1 was
an independent Opus 5 hostile batch review, frozen at
`v10/reviews/batch-round1-d50-to-d60.md` — for D51, REVISE, 2
BLOCKER / 3 MAJOR / 8 MINOR / 2 NIT.  The reviewer re-implemented the
whole d42a admission layer from scratch (DFS reachability, brute-force
MIS, explicit permutation replay for PK1) and it agreed with the
committed layer on all 6,471 histories — menus *with exact Fraction
weights* and posets, **zero mismatches** — and every published number
reproduced.  **Both BLOCKERs are interpretation sentences, and the
first inverts the unit's headline.**  Repairs applied; this note is
one of them (round-1 NIT 1: D51 shipped as pin + receipt + LOG, and
all three defective sentences reached `THE-THEORY-SO-FAR.md` from
there — the repairs must reach the book).  Pin
`note-d51-h1-menu-visibility-pin.md` (LOG #423, committed before
code).  Receipt: `v10/code/d51_menu_visibility_exact.py` (12 PASS /
0 FAIL, exit 0), output under `v10/data/`.  An independent hostile
round is required before anything here is citable.

## 1. MV0(σ) — the correction that inverts the headline

Round-1 BLOCKER 1.  The committed VERDICT said: *"Since sigma IS an
abstraction of exactly those projections, menus are sigma-determined
here."*  The receipt never loaded `sigma` at all (round-1 MINOR 6 —
and that omission is what made the error possible; the comparison
takes seconds).  Loaded now, verbatim by text slice from the
committed d44a receipt:

```
  distinct committed-sigma states on the depth-5 family = 32
  distinct D51 projection keys                          = 209
  D51 key determines sigma?   keys with >1 sigma state  = 0    <- REFINES sigma
  sigma determines D51 key?   sigma states with >1 key  = 32   <- ALL of them
```

"σ is an abstraction of the projections" means *projections ⇒ σ*.
The measurement says the opposite: the projections are strictly
**finer**.

> **MV3's `projections-equal ⇒ menus-equal` is therefore IMPLIED BY
> σ-determination, not the converse.  (H1) IS NOT REDUCED IN THE
> CLAIMED DIRECTION.**  The same inversion voids the committed MV4
> reading of (H2): `key(h) → key(h+e)` says nothing about
> `σ(h) → σ(h+e)`, because `σ(h)` does not determine `key(h)`.

## 2. What IS established

> **EQUAL FULL-VIEW PROJECTIONS GIVE EQUAL MENUS with exact weights,
> over every history to depth 7 — 179,783 histories, 1,089 projection
> keys, zero violations — and the successor projection state is a
> function of (projection state, event), 2,530 pairs, zero
> violations.  That is the PROJECTION reduction of the MENU function,
> at finite depth, and GIVEN (H0) for the fifth read.**

Round-1 MINOR 1: the committed `CAP = 5` was hard-coded with no
feasibility statement, against the pin's explicit instruction to beat
d44a's depth 7.  The sweep now runs 5 / 6 / 7 (209 / 481 / 1,089
keys; 498 / 1,122 / 2,530 transitions; zero violations throughout),
matching d44a's own 179,783 / 145,408 census.

Round-1 MINOR 8: "MV3 is the menu-level form of MV1+MV2" is
withdrawn.  MV3 reads only FULL views; MV1/MV2 are about CANDIDATE
views.  Neither implies the other.

## 3. MV3b — the positive content is subsumed by its own parent

Under the COMMITTED σ, (H1) and (H2) do hold on this family (32 σ
states, zero states carrying more than one renamed menu; zero
transition violations).  But these are **d44a's results at a
shallower depth**: d44a's CG1 *is* (H1) verbatim (34,375 histories,
36 σ-classes, zero exceptions; CG7b extends to 145,408 depth-7
transitions) and CG2 *is* (H2) verbatim.  So the committed MV4 label
— "(H2) IS SETTLED HERE, not left dangling as d44a left it" — is
**false about d44a's receipt**.  What d44a left open is the LOGICAL
question, and its note answers that in the *opposite* direction
("(H2) … NOT a consequence of (H1)").  D51's positive content is
strictly subsumed by its parent.

## 4. The durable content: three refutations

**(a) MV-STRONG fails for every event type — and more cheaply than
claimed** (round-1 MAJOR 2).  `regs_of(('p',a,b,x)) = {a} =
regs_of(('n',a))`, so a propose candidate's view **is** its actor's
noop cone (12,916/12,916).  "p candidates lag too" is the idle lag
recounted with different multiplicities, not a second refutation, and
pin §2's "a propose additionally pulls in the wires the event
touches" is false.  Better: pin §5 dies on its own premise —
"`pred[e]` contains every live proposal on the base `b`" misses in
2,440 of 12,916 `'p'` cases and 2,032 of 8,516 `'r'` cases, because
proposals are carried on the *proposer's* register, not the base
wire.  4,472 exhibited counterexamples, and a cleaner refutation than
the one the receipt claimed.

**(b) MONOTONICITY FAILS — with the CORRECT mechanism** (round-1
BLOCKER 2).  The committed text blamed the own-proposal exclusion.
That cannot happen: an actor's own live proposals are identical in
its noop cone and the full view in 12,942/12,942 pairs.  **The real
obstruction is MISSED SUPERSESSION** — a lagged view does not know
its base has been superseded — and both fibre elements now print
their shortest witnesses:

```
  full (F,F) -> cone (T,F): actor A, h = [('p','B',v0,1), ('r','B',{('B',v0,1)},{...})]
      A has proposed NOTHING; B self-arbitrated, superseding v0.
      Full view: v0 superseded -> has_p False.  A's cone is EMPTY -> has_p True.
  full (F,F) -> cone (F,T): the same prefix plus ('p','A',v0,0)
      A's own proposal is in A's cone in BOTH views; the cone misses B's ARB,
      so it still sees v0 un-superseded -> has_r True.
```

The conclusion survives, re-established directly on option sets
rather than the two bits: over 12,942 (h, actor) pairs the cone's
proposal options are equal in 11,938, **strictly MORE in 1,004**, and
strictly fewer in 0.  Any depth-free argument built on "the lagged
view sees a subset" is unsound, and the pin's §5 sketch is one of
those.  Told the obstruction is the own-proposal clause, a reader
looks for an argument handling that clause; the actual obstruction is
much harder, and is precisely what LOG #432 later hit at transport.

**(c) The `'r'` arm LAGS TOO** (round-1 MAJOR 3, newly measured).  The
committed MV2 preamble asserted the negation of the gate printed
three lines above it ("MV1 shows p/r candidates read the full-view
values") and used that to collapse the whole question onto the idle
2-bit pair, leaving the arbitration arm — the one running through
`arb_components_in_view`, `mis_of` and `PK1` — untested.  Tested now:
of 71 distinct full-view arbitration keys, **19 carry more than one
candidate-view value**.  The preamble was accidentally sound for
`'p'` (by MAJOR 2's theorem, which the receipt never noticed) and
unsound for `'r'`.

## 5. MV7 — the FIFTH read, and the (H0) dependence

Round-1 MAJOR 1.  The reduction reads a fifth thing: `view.pred`, via
`incomparable()` → `edges()` → `mis_of` (an **admissibility** test)
and `PK1(...)[wkey]` (the **weight**).  `components()` records only
the partition; the edge set inside a component is strictly finer, and
`projections()` drops it.  **The omitted read is where the weights
live.**  It is inert at this scope — but by a theorem the committed
receipt never stated, and that theorem is verbatim (H0)'s fourth
clause:

```
  views inspected = 53,787; same-base live-proposal pairs = 3,048, COMPARABLE = 0
  component sizes seen = {1: 24920, 2: 2540}
  (base, member-triples) keys = 70; keys carrying MORE THAN ONE edge set = 0
```

The committed σ records the edge set `E` explicitly, so d44a judged
it necessary; D51 drops it without argument.

> **"[STRUCTURAL, exact]" must read "exact GIVEN (H0)".**  Declared.

## 6. Gate hygiene (round-1 MINOR 2/3/4/5/7, NIT 2)

MV5 now implements the **pinned** mutant (drop an *opponent-authored*
proposal) alongside the committed protocol and an exhaustive one —
the committed protocol dropped the lowest-indexed proposal with no
author test and broke after the first `'r'` candidate, so in 82% of
cases it hid the candidate's OWN proposal, the opposite of the pinned
probe, and its "63%" was a sampling artefact quoted three times as if
it characterised the object (pinned: 1,776/2,992 = 59%; exhaustive:
6,024/8,512 = 70%).  Its gate is the pin's own "must CHANGE **some**
menu" (`> 0`), not the invented 50% bar that sat just under an
observed 63%.  MV1/MV2 no longer gate the author's *negative*
findings — on a family where the negatives did not occur, the
committed receipt would have exited 1 on a *stronger* result.  The
theorem-passes are labelled: MV0(a) is a `callable()` smoke test, and
MV0(b)'s "all extras are opponent-authored" clause cannot fail
(every event's initiator is in its own register set).  MV0's census
is a complete trichotomy — `2,032 + 19,400 + 0 + 0 = 21,432 =
12,916 + 8,516` — and says so.  The MV1 counterexample witness, which
the committed receipt computed and discarded, is printed.

The AST anti-vacuity scan (MV6) is real and better than its siblings'
— it requires a run-bound name, and injecting one bare-constant
`check()` makes it fail `[REFEREE-CARRIED, batch round 1]`.

## 7. Scope, held

d42a, DELIVERY-FREE, two actors (D44b's boundary).  Nothing transfers
to transport scope; LOG #432's independent probe later confirmed the
scope carried.

## 8. Residues

1. **(H1) itself.**  Undischarged, and this unit does not reduce it.
   The live asset is the *projection* reduction of the MENU function,
   which needs a bridge σ → projections that does not exist (they are
   strictly finer).
2. **The (H0) dependence** of the fifth read (§5) — inert here, live
   the moment same-base live proposals can be comparable.
3. **The `'r'` arm's lag** (§4c), newly exhibited and unexplained.
