# D54 — result: THE DILWORTH GATE, and a record that shatters

**Status:** GREEN-UNREVIEWED, 2026-07-26.  Pin:
`note-d54-dilworth-gate-pin.md` (§1–§7 committed before any code;
§8 the first-run amendment).  Receipts:
`v10/code/d54_dilworth_gate_exact.py` (9 PASS / 0 FAIL) and
`v10/code/d54b_shatter_construction_exact.py` (11 PASS / 0 FAIL),
outputs under `v10/data/`.  Review: an independent Opus 5 hostile
round is required before anything here is citable.

---

## 1. THEOREM (the Dilworth gate), with proof

> **Theorem.**  At transport scope (d42b1), fix any history, any
> base event `e`, and any sky whose direction set is an antichain in
> the event poset.  If the record has `k` actors, then the sky's
> shadow family is a union of at most `k` chains under inclusion.
> Consequently: realizing all `2^m` subsets of an `m`-element
> direction set as traces — in particular, shattering — requires at
> least `C(m, floor(m/2))` actors.  **Shatter-4 requires at least 6
> actors; a sphere-like sky (shattering at every m) requires
> unboundedly many.**

**Proof.**  (i) *[The physical step — gated as Stage 0.]*  Any two
events sharing an actor wire are comparable: the event poset is the
carrier-wise wire closure, and this is verified at transport scope
over 218,795 actor-sharing pairs (deliveries' two-carrier case
included) with zero violations `[EXACT at tested scope]`.

(ii) Assign each event to its initiating actor.  By (i) the events
assigned to one actor are totally ordered, so their down-sets are
nested, so the traces they contribute — down-set ∩ directions — form
a chain under inclusion.  The full shadow family is therefore
covered by at most `k` chains, one per actor.

(iii) A chain contains at most one member of any antichain.  The
middle layer of the Boolean lattice `B_m` is an antichain of size
`C(m, floor(m/2))` (constructively verified for m ≤ 6; the de
Bruijn–Tengbergen–Kruyswijk recursion simultaneously exhibits a
chain PARTITION of the same size, so the count is exact both ways).
A family realizing all of `B_m` therefore needs at least that many
chains, hence at least that many actors.  ∎

**Scope of each step, stated:** (iii) is classical mathematics,
exact for every m.  (ii) is bookkeeping given (i).  (i) is gated,
not proven from the grammar — the theorem is EXACT at every scope
where (i) holds, and (i) is corroborated, zero exceptions, over the
exhaustive 2-actor family and sampled families at widths 3, 4, 6.
The nested-trace lemma itself is separately corroborated over
15,909 skies (33,546 per-actor groups, zero non-nested pairs).

**What the theorem delivers for the programme:** the author's
infinite-clocks doctrine — 3+1 is not four clocks but infinitely
many — is no longer a doctrine at this scope.  **A sky rich enough
to be a 2-sphere requires unboundedly many actors, by Sperner's
count applied to actor sequentiality.**  Width is not merely the
observed scaling variable (D47b); it is the *provable price* of
dimension.

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
> from the committed layer's own menu, whose SKY-B(5) sky at the
> minting event has 4 pairwise-incomparable directions, 16 distinct
> traces including the empty one (SC5 capacity, D53's corrected
> condition), realizes ALL 16 subsets, and returns a shattered
> 4-set `[EXACT]`.**

Consistency checks: the record's traces decompose into
per-initiator chains with zero crossings and 16 contributing actors
(the construction SATURATES the theorem, it does not beat it); on
the same record SKY-A and SKY-C have no empty trace (D53's
disqualification reproduced on the constructed object).

## 3. What may and may not be concluded

**MAY:** the transport layer admits a record whose SKY-B(5) sky is
**not realizable as a 2+1 celestial sky** — arcs on a circle cannot
shatter a 4-set (D47a SG0, constructed, not cited).  This is the
first obstruction certificate against 2+1 in the corpus, and it is
measure-free: no completion, no normalization, no H1.

**MAY NOT:** any positive 3+1 claim.  Shattering rules OUT the
circle; it does not rule IN the sphere.  The positive side — exact
rational cap-realization of this shadow system on S² — is a
separate unit (the D47c shape), now warranted for the first time.
The claim is reading-relative to SKY-B at depth 5 and says so.

## 4. The physical reading `[MY READING]`

The two halves fit together tightly.  The theorem says directions
are bought with actors — each actor's worldline can only ever sweep
a nested family of shadows, so richness of the sky is parallelism,
never history.  The construction says the price is *payable*: the
grammar does admit records that spend 20 actors to buy a sky no
circle can host.  And the failed blueprint says the currency is
subtle — knowledge backflow taxes every join, and only clean
couriers transfer a single direction.  Dimension, in this
framework, is a *supply-chain problem*.

## 5. Residues

1. **Minimality.**  The bound is 6; the construction uses 20.  The
   gap is real: couriers exist because of backflow, and whether
   backflow forces MORE than 6 (a stronger lower bound) or clever
   scheduling reaches 6 is open and decidable.
2. **The S² cap-realization** of the constructed shadow system —
   the positive side, now warranted.
3. **Genericity.**  One engineered record shatters; whether the
   completed measure (D49's `Zhat`, delivery-free scope) assigns
   such records any weight is a different question, currently not
   even posable at transport scope (D52).
4. **The depth parameter.**  d = 5 here; the committed SKYB_DEPTH
   elsewhere is 2.  A d = 2 construction, or a proof that d ≥ some
   bound is forced, would sharpen the reading-relativity.
