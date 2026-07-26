# D54 — result: THE DILWORTH GATE, and a record that shatters

**Status:** ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.  Round 1 was
an INDEPENDENT OPUS 5 hostile review, frozen at
`v10/reviews/d54-round1-hostile-review.md` — REVISE, 1 BLOCKER /
2 MAJOR / 8 MINOR / 3 NIT, every attack run by recomputation; the
mathematical core and the construction survived everything, and all
three top findings hit the INTERPRETATION layer.  Repairs applied
in-receipt and below; delta appended to the round.  Pin:
`note-d54-dilworth-gate-pin.md` (§1–§7 committed before any code;
§8 the first-run amendment).  Receipts:
`v10/code/d54_dilworth_gate_exact.py` (9 PASS / 0 FAIL) and
`v10/code/d54b_shatter_construction_exact.py` (12 PASS / 0 FAIL
post-repair; 11 before K11 was added), outputs under `v10/data/`.

---

## 1. THEOREM (the Dilworth gate), with proof

> **Theorem.**  At transport scope (d42b1), fix any history, any
> base event `e`, and any sky whose direction set is an antichain in
> the event poset.  If the record has `k` actors, then the sky's
> shadow family is a union of at most `k` chains under inclusion.
> Consequently: realizing all `2^m` subsets of an `m`-element
> direction set as traces — in particular, shattering — requires at
> least `C(m, floor(m/2))` actors.  **Shatter-4 requires at least
> 6 actors.**

**Proof.**  (i) *[The physical step.]*  Any two events sharing an
actor wire are comparable.  **Round-1 MINOR 3 upgraded this from a
gated fact to a THEOREM OF THE LAYER:** `event_poset` chains every
register by construction (same-register events are ordered by
history position, transitively), and every event's initiator is
among its registers for all five event types — so same-initiator ⇒
same register ⇒ comparable, always.  The Stage 0 sweep (218,795
actor-sharing pairs, zero violations, deliveries' two-carrier case
included) is CORROBORATION of a proved step; the round verified
the stronger register-sharing form too (226,223 pairs, zero
violations) `[REFEREE-CARRIED]`.

(ii) Assign each event to its initiating actor.  By (i) the events
assigned to one actor are totally ordered, so their REFLEXIVE
down-sets are nested (`x ≤ y ⇒ down(x) ∪ {x} ⊆ down(y) ∪ {y}`), so
the traces they contribute — `{c ∈ dirs : c ≤ f}`, exactly the
committed instrument's definition (round-1 MINOR 8 corrected the
first draft's strict-down-set wording) — form a chain under
inclusion.  The full shadow family is covered by at most `k`
chains, one per actor.  When shattering is tested on a subset `S`
of a larger direction set, the restriction `r ↦ r ∩ S` is
monotone, so chains map to chains and the bound transfers.

(iii) A chain contains at most one member of any antichain.  The
middle layer of the Boolean lattice `B_m` is an antichain of size
`C(m, floor(m/2))` (constructively verified for m ≤ 6; the de
Bruijn–Tengbergen–Kruyswijk recursion simultaneously exhibits a
chain PARTITION of the same size, so the count is exact both ways).
A family realizing all of `B_m` therefore needs at least that many
chains, hence at least that many actors.  ∎

**Scope of each step:** (iii) is classical mathematics, exact for
every m.  (ii) is bookkeeping given (i).  (i) is a theorem of the
layer, so **the theorem is unconditionally exact at transport
scope.**  The sweep corroboration (15,909 skies, 33,546 per-actor
groups, zero non-nested pairs) carries a declared limit (round-1
MINOR 4): no swept sky reaches 4 directions or more than 7 distinct
traces, so the 16-trace regime is covered by the proof and by the
round's direct check on the constructed records, not by the
sweep.

**The sphere consequence — WITHDRAWN as first stated, re-derived
by a better route (round-1 BLOCKER 1).**  The first delivery said
"a sphere-like sky (shattering at every m) requires unboundedly
many actors" and called the infinite-clocks doctrine a theorem by
that route.  **The antecedent is satisfied by no 2-sphere sky:**
caps on S² are halfspace traces with VC dimension 4 — they shatter
4 points and NEVER 5, certified in the round by an exact Radon
partition on rational sphere points (λ = (−23/49, −19/49, −24/49,
17/49, 1); conv{3,4} meets conv{0,1,2}) `[REFEREE-CARRIED]`.  The
Sperner route never fires on the sphere.

**The conclusion survives by TRACE COUNTING — no shattering
anywhere in the derivation** `[REFEREE-CARRIED, verified in the
round]`: a sphere sky on n directions realizes
2·Σ_{i≤3} C(n−1, i) = Θ(n³) distinct cap traces, while the
nested-trace lemma caps one actor's chain at n+1 traces, so
**actors ≥ Θ(n²) → ∞: a sky rich enough to be a 2-sphere still
requires unboundedly many actors.**  The infinite-clocks statement
holds at this scope by counting.  Promoting this bound to an
in-receipt gate is a residue.

**And what width actually prices (round-1 MAJOR 1):** the same
counting gives a 2+1 CIRCLE sky n²−n+2 arc traces, hence ≥ n−2
actors — also unbounded.  **Width is the provable price of SKY
SIZE, not of dimension.**  The dimensional signal in the Dilworth
gate is the shatter offset alone: arcs shatter 3 (≥ 3 actors),
caps shatter 4 (≥ 6 actors).  Three versus six — a factor, not a
divergence.

## 2. The construction: a record whose sky shatters

**The pinned blueprint failed, and the failure is a finding (pin §8
A1).**  The 9-actor build is admissible end to end — 31 events, all
menu-offered — and realizes only **8 of 16** subsets.  Mechanism:
**a delivery is a join in both directions.**  The sender's wire
absorbs the receiver's accumulated past, so after B delivers into an
accumulator holding A, every later send from B carries {A,B}, and
the other chains are contaminated before they start.  The
per-sender send-traces form a chain — the theorem biting its own
construction.  This is gated as a negative exhibit (N1), not
discarded.

**The courier architecture succeeds (pin §8 A2).**  Sending into an
EMPTY receiver folds nothing back — the sender stays clean.  So each
direction-actor mints one fresh courier per contaminating step, and
each courier performs exactly one send into a charged accumulator:

> **A 20-actor, 42-event transport record, every event selected
> from the committed layer's own menu, whose SKY-B sky at the
> minting event has 4 pairwise-incomparable directions, 16 distinct
> traces including the empty one (SC5 capacity, D53's corrected
> condition), realizes ALL 16 subsets, and returns a shattered
> 4-set — at THREE depths, d = 4, 5, 6 (round-1 MINOR 2; the
> promised per-d table is now gate K11) `[EXACT]`.**

Consistency checks: the record's traces decompose into
per-initiator chains with zero crossings; **the realized 16-trace
family's minimum chain cover is EXACTLY 6 — Dilworth-tight**
(round-1 MINOR 5 replaced the first draft's false "saturates";
the 6-vs-20 gap is architectural, the scheduling cost of backflow,
not slack in the family); and SKY-A/SKY-C on the same record have
no empty trace ([THEOREM-PASS] per D53 — a consistency exhibit,
not evidence).  The first-run failing output (9 PASS / 3 FAIL on
the 9-actor blueprint) is preserved at commit `e07582c`.

## 3. What may and may not be concluded

**MAY (restated per round-1 MAJOR 2):** the transport layer admits
a record whose SKY-B sky **is not an arc system** — arcs realize at
most 14 of 16 traces on any 4 points, missing the crossing pairs
(theorem, re-verified in the round).  "Not a 2+1 celestial sky"
holds ONLY under the strict stipulation that a 2+1 sky means an arc
system on the circle of directions — and the corpus's own demotion
(D47a SG3b; recounted in the round at 218/397) shows a MAJORITY of
genuine discrete 2+1 skies are non-arc, so that stipulation must be
said aloud.  **The sound discrete claim is EMPIRICAL and now has
its control:** over 1,925 SC5-capable genuine M^{2+1} SKY-B pairs
at depths 1..10, ZERO shattered 4-sets `[REFEREE-CARRIED]` — while
this record shatters at three depths.  Measure-free throughout: no
completion, no normalization, no H1.

**MAY NOT:** any positive 3+1 claim.  Shattering rules OUT the
circle; it does not rule IN the sphere.  The positive side — exact
rational cap-realization of this shadow system on S² — is a
separate unit (the D47c shape), now warranted for the first time.
The claim is reading-relative to SKY-B at depth 5 and says so.

## 4. The physical reading `[MY READING]`

The two halves fit together tightly.  The theorem says sky
RICHNESS is bought with actors — each actor's worldline can only
ever sweep a nested family of shadows, so a rich sky is
parallelism, never history (round-1 MAJOR 1: a circle costs
unboundedly many actors too; the dimension signal is the shatter
offset, 3 vs 6, and the ladder continues — halfspaces in R^d
shatter d+1, so shatter-5 would certify beyond-3+1).  The construction says the price is *payable*: the
grammar does admit records that spend 20 actors to buy a sky no
circle can host.  And the failed blueprint says the currency is
subtle — knowledge backflow taxes every join, and only clean
couriers transfer a single direction.  Dimension, in this
framework, is a *supply-chain problem*.

## 5. Residues

1. **Minimality.**  The bound is 6; the construction uses 20 — and
   the round showed the realized FAMILY is already Dilworth-tight
   at 6 chains, so the whole gap is architectural.  Whether
   backflow forces MORE than 6 actors (a stronger lower bound) or
   clever scheduling reaches 6 is open and decidable.
1b. **Promote the trace-counting bound** (the round's Θ(n²) sphere
   result and the circle's n−2) to an in-receipt gate — currently
   `[REFEREE-CARRIED]`.
1c. **Shatter-5.**  Halfspaces in R⁴ shatter 5; caps on S² never
   do.  So "does the transport layer admit shatter-5?" (cost ≥
   C(5,2) = 10 actors by the gate) asks whether the framework can
   exceed 3+1 — the shatter ladder is a dimension METER, not just
   a 2+1 obstruction.  `[MY READING]`
2. **The S² cap-realization** of the constructed shadow system —
   the positive side, now warranted.
3. **Genericity.**  One engineered record shatters; whether the
   completed measure (D49's `Zhat`, delivery-free scope) assigns
   such records any weight is a different question, currently not
   even posable at transport scope (D52).
4. **The depth parameter.**  d = 5 here; the committed SKYB_DEPTH
   elsewhere is 2.  A d = 2 construction, or a proof that d ≥ some
   bound is forced, would sharpen the reading-relativity.
