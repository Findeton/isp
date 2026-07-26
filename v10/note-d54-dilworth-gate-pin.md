# D54 — THE DILWORTH GATE, and the targeted shatter construction (PIN)

**Status:** PIN, STRICT, 2026-07-26.  Committed BEFORE any receipt
code exists.  Parents: D47b (sky size is an actor-width phenomenon),
D48 (actor count is physical content), D53 (only SKY-B can shatter;
the corrected capacity condition SC5), D45b §1 + the author's binding
"infinite clocks" doctrine.  Review: hostile round via an
independent Opus 5 worker after the receipts are green.

## 1. Why this unit exists

The 3+1 question is measure-free — shatter-4 needs no completion —
so it does not wait on the dichotomy line.  What it has lacked is a
STRUCTURAL account of what shattering *costs* in the framework's own
currency.  This pin supplies a candidate account and then spends it.

## 2. STAGE 0 — the premise, gated before anything leans on it

**[PREMISE P] Any two events sharing an actor wire are comparable in
the event poset, at TRANSPORT scope (d42b1: p/r/n/d/m).**

At arbitration scope this is the gated chain law (D44c clause (iv)).
At transport scope, deliveries carry TWO actors, and the premise has
never been gated there.  *Pre-registered expectation: HOLDS* — the
event poset is the carrier-wise wire closure and every event carries
its initiator — but D51's monotonicity surprise is the standing
warning that layer-reading beats layer-believing.  **If P fails, the
unit ends at Stage 0 and the failure is the deliverable.**

## 3. STAGE 1 — the theorem

> **[TARGET T — the Dilworth gate.]**  Fix any sky (any base event,
> any definition whose directions form an antichain).  Each event is
> assigned to its initiating actor; by P, same-initiator events are
> totally ordered, so their down-sets are nested, so **the traces
> contributed by one actor's worldline form a chain under
> inclusion**.  Hence the shadow family of a k-actor record is a
> union of at most k inclusion-chains.  Shattering a 4-set requires
> all 16 subsets of B4 realized as traces; B4's largest antichain is
> the 6 pairs; by Dilworth/Mirsky no chain cover has fewer than 6
> chains.  **Therefore shatter-4 requires at least 6 actors;
> shatter-k requires at least C(k, floor(k/2)); a sphere-like sky —
> shattering at every k — requires unboundedly many actors.**

The last clause, if it survives, derives the author's
infinite-clocks doctrine as a THEOREM: a continuum of directions
needs a continuum of actors, by Sperner's count applied to actor
sequentiality.

Gates: the written proof in the result note (the word THEOREM is
earned by the proof; the sweep CORROBORATES, per D44c-P round-1 P2);
mechanical decomposition of every sky's shadow family in the
enumerated+sampled transport family into per-initiator chains, zero
exceptions; the B4 certificate exhibited exactly (a 6-antichain AND
a 6-chain symmetric-chain cover, so min cover = 6 with both bounds
constructive); Sperner corroborated by brute force for k <= 5.

## 4. STAGE 2 — the construction (the converse T is silent on)

T makes 6 actors NECESSARY.  Sufficiency is a construction problem,
and this pin commits a BLUEPRINT rather than a blind search:

**The 9-actor blueprint (X, A1..A4, B1..B4).**  X proposes on v0 and
arbitrates it — the arbitration is the base event `e`, minting v1.
X delivers v1 to A1..A4 (four events on X's wire, heights +1..+4
above e).  Each Ai pads its own wire (idles) and then proposes on v1
so that all four proposals p1..p4 land at the SAME height, e+5:
**pairwise incomparable by proposal locality** (a proposal's only
carrier is its proposer), each above e via its delivery.  These are
the four directions of SKY-B(5) at e.  Then the accumulators realize
the missing subsets, one symmetric chain each, by RE-DELIVERIES of
v1 (re-delivery is admissible and physical, d42b1 docstring):

| trace needed | realized by |
|---|---|
| empty | X's first delivery (above e, above no direction) |
| singletons | the directions themselves |
| {12},{123},{1234} | B1 receives from A1, A2, A3, A4 in order |
| {23},{234} | B2 receives from A2, A3, A4 |
| {13},{134} | B3 receives from A1, A3, A4 |
| {24},{124} | B4 receives from A2, A4, A1 |
| {14} | A1 receives from A4 (after all B-deliveries from A1) |
| {34} | A3 receives from A4 (likewise) |

Ordering constraint, load-bearing: every B-delivery sourced from an
Ai precedes that Ai's own late receipts, else traces contaminate.
The blueprint is exactly the B4 symmetric chain decomposition worn
as worldlines — the theorem's lower bound turned into a wiring
diagram, with 9 actors against the bound's 6 (minimality is a
residue, not a target).

**Admissibility is decided ONLY by the committed d42b1
`candidates_for`: the builder SELECTS each event from the layer's
own menu by specification, never constructs tuples freehand.**  If a
step is refused, the receipt prints the prefix, the specification,
and the menu — the refusal and its clause are the deliverable.

*Pre-registered expectation: ADMISSIBLE.*  Recorded with its
reasoning (the blueprint above) and against my own prior lean:
before engineering it I leaned "blocked" on the strength of
D47-round-1's narrower-than-chance result; the sketch changed my
mind, and both states are on the record.  Five of my last six
pre-registrations were corrected by their receipts.

## 5. Capacity, readings, and what may be claimed

- Capacity is **SC5** (D53): >= 4 directions, >= 16 distinct traces,
  the empty trace present — never D47's SG2.
- **SKY-B only** (D53: A and C can never shatter).  The depth
  parameter is reported per d in {1..6}; a success under one d is
  READING-RELATIVE and says so (the blueprint targets d = 5).
- If the construction shatters: the claim is "**the transport layer
  admits a record whose SKY-B(5) sky is not realizable as a 2+1
  celestial sky**" — an obstruction certificate under the committed
  definition, no more.  The positive S^2 side (a D47c-style rational
  cap certificate) is a SEPARATE unit, only warranted then.
- If refused: a cap statement naming the blocking clause, at
  blueprint scope — not a no-go until the clause is shown generic.

## 6. Falsifiers / exits

Stage 0 P failing => the unit's result, exit 0.  Stage 1 decomposition
finding a non-nested per-initiator trace pair => T is FALSE and the
witness is printed, exit 0.  Anchor breakage, mutant misbehaviour,
or the builder constructing an event the layer's menu did not offer
=> exit 1.  Standard disciplines: AST anti-vacuity scan scoped per
LOG #403 MA-2; witness branches live AND exercised per LOG #354 F1;
deterministic keys everywhere (D49 A4); no silent caps.

## 7. Review

Hostile round by an **independent Opus 5 background worker** with a
self-contained brief, after both receipts are green — the reviewer
recomputes, never trusts printouts.  Nothing from this unit is
citable before that round is terminal.

## 8. First-run amendment (2026-07-26, pre-review; recorded, not
## silently fixed)

**A1 — the §4 blueprint is REFUTED by its own run, and the mechanism
is a finding.**  The 9-actor blueprint is ADMISSIBLE end to end (31
events, every one offered by the layer's menu) and realizes only
**8 of 16** traces: F's full chain plus singletons.  The cause, which
§4 missed: **a delivery is a join in BOTH directions** — the sender's
wire absorbs the receiver's accumulated past, so after B delivers into
F (which already held A), every later send FROM B carries {A,B}, and
G's chain is contaminated before it starts.  The per-sender send-traces
form a chain (the theorem, biting its own construction).

**A2 — the repair: the COURIER architecture.**  Sending into an EMPTY
receiver folds nothing back — the sender stays clean.  So each
direction-actor mints clean couriers (one fresh actor per
contaminating step, receiving v1 while empty), and each courier
performs exactly ONE send into a non-empty accumulator, then is spent.
Contaminating steps needed: F 3, G 2, H 2, I 2, the two late pairs 2 —
**11 couriers**, total 20 actors, ~42 events.  The amended schedule:
clean first receipts (A→F, B→G, A→H, B→I); courier mints (B→J; C→K,L,M;
D→N,O,P,Q,R,S; A→T); then J→F, K→F, N→F; L→G, O→G; M→H, P→H; Q→I, T→I;
R→A, S→C.

The Dilworth bound is untouched by A1 (it is a lower bound; the failed
run VIOLATES nothing).  The receipt keeps the §4 build as a gated
negative exhibit — the backflow mechanism on the record — and runs the
courier build as primary.
