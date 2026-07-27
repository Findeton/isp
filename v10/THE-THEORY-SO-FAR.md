# THE THEORY SO FAR

### The record programme explained twice: once for a reader with no mathematics, once for a reader who wants the objects

**Corpus:** `~/workspace/isp`.  Author of the research programme: Felix
Robles Elvira (ORCID 0009-0009-2017-4394).
This document is a *brief*, not new research.  Every number in it is read
out of a committed source file; nothing is quoted from memory.

---

> **MAINTENANCE (binding, LOG #443, amended #444):** this book is a
> LIVING document and the corpus's single synthesis, and it must
> always read AS IF WRITTEN IN ONE GO at the present moment.  Current
> as of **LEDGER #491** (v10/LOG.md) / **#130** (v8/LEDGER.md).
> Every terminal unit's patch is an INTEGRATION, never an appendix:
> the patcher re-reads the whole book, weaves the new state into the
> chapters, and removes any accretion scaffolding ("late arrivals",
> "as first written", "restated per round N") before committing.  The
> LOG keeps the history; the book keeps the present.  Discarded roads
> live in the graveyard chapter as content, told timelessly.  A claim
> in the corpus but not here — or here but not in the corpus — is a
> defect in whichever is stale.

## 0. What this document is

This is one document containing two complete explanations of the same
body of work.

**PART A** explains the theory to an intelligent reader with no
mathematics.  It contains no formulas and no unglossed jargon.  It uses
analogies, and it says where each analogy breaks.

**PART B** explains the same theory to a mathematician or physicist who
wants the actual objects: the definitions as the code implements them,
the exact statements, the exact rational numbers, the provenance of
each, and the scope each claim is confined to.

The chapters are **mirrored**.  Chapter 1 of Part A and chapter 1 of
Part B are about the same thing; each says so and points at the other.
A reader who wants the intuition first can read Part A end to end and
then Part B end to end.  A reader who wants to check something can go
straight to the twin chapter in Part B.

**PART C** covers the earlier corpus (v1–v9, the SHARD/ISP arc) and
**PART D** the destination; both carry *both* registers inside each
chapter (① PLAINLY, then ② THE OBJECTS), so a reader who wants only Part
A's register can read the ① sections and stop.

**One document, written as one.**  This book states the corpus's present
understanding in a single voice.  It carries no record of the order in
which its own contents arrived: superseded roads are content, and they
live in the graveyard chapters, told timelessly.  The LOG keeps the
history; the book keeps the present.

**Two doors, same house.**  Neither part is a summary of the other.
Part A is not "Part B with the equations removed" — it is written to be
*true* at its own level of resolution, which sometimes means saying
less, and never means saying something Part B contradicts.  Where
Part A has to simplify in a way that could mislead, it says so in a
line beginning *"Where this picture breaks:"*.

### What this document is *not*

- It is not a paper.  The corpus's papers (30, 31, 32) are terminal,
  peer-attacked artefacts with their own scope discipline; this is a
  guide to them and to the notes and receipts around them.
- It is not a claim of physical results.  **No laboratory number may be
  quoted through any of this** (Part A ch. 10, Part B ch. 10 §B10.7).
- It is not a settled theory.  Roughly half of this document is an
  honest account of things that were tried, believed, published
  internally, attacked, and withdrawn.  That is not an embarrassment
  being confessed; it is the primary evidence that the surviving claims
  are worth anything.

---

## 0.1 Provenance labels (load-bearing, used throughout)

Copied from the convention of `v10/THE-COMPLETION-DICHOTOMY.md` §0,
which is the corpus's standard:

| label | meaning |
|---|---|
| `[THEOREM]` | proved, with the proof in the cited place |
| `[EXACT]` | computed in exact rational arithmetic by a committed receipt that exits 0 |
| `[MEASURED]` | computed, but at a declared finite scope only |
| `[EVIDENCE]` | supports a claim without being a premise of any proof |
| `[REFEREE-CARRIED]` | established in a frozen hostile-review record, not in a receipt |
| `[POSITED]` | an interpretive choice, not derived |
| `[MY READING]` | interpretation added in *this* brief, not a corpus claim |

`[SAMPLED]` also appears where a number comes from declared-seed
sampling rather than enumeration.

**Additional gate labels** introduced by the D49 round (LOG #419) and
used in Part B where they matter: `[SUBSTANTIVE]` (a test that could
have failed on the science), `[ANCHOR]` (reproduces a prior unit's
number), `[DERIVED]` (arithmetic given an earlier gate),
`[THEOREM-PASS]` (a check whose outcome is fixed by a proved statement,
so its passing is not evidence).  The D49 receipt's own split is
**15 / 5 / 6 / 5**.

## 0.2 The two disciplines a reader must obey

**(1) Green-unreviewed work is not citable.**  A unit in this corpus
goes: *pin* (a pre-registered plan, committed before any code) →
*receipt* (executable, exact, exits 0) → *result note* → **hostile
review round, frozen** → repairs → *delta appended to the round file* →
**terminal**.  Between the receipt and the terminal stamp the unit is
"green-unreviewed", and nothing may lean on it.  The rule has been broken once, and the breach
is itself on the record: a settlement banner was written into the
corpus's entry-point document in the same ledger entry that created the
unit, before any round.

**(2) Scope labels are part of the claim.**  "At d42a scope",
"delivery-free", "at transport scope", "reading-relative to SKY-B",
"at tested scale" are not hedges.  Dropping one turns a true statement
into a false one.  The programme's single most common failure mode is a
*true computation* wearing a *scope-free sentence*.

## 0.3 Forbidden sentences

These are on a standing blacklist in the corpus, and this document
observes it:

- **"forward-complete"** may never be written without "the law **plus**
  paper 30 §5.7's stationary form" (D49 round 1 BLOCKER B2; D50).
- **"the layer does not select 3+1"** — say instead: *the layer does
  not **cap** the shatter ladder at the sphere's rung* (D55 round 1
  BLOCKER 1).
- **"the sky IS a circle / a sphere"** — never licensed by any receipt
  (D47 pin's one-sidedness doctrine).
- **any laboratory number** — the bridge is blocked (d41c §1A).
- **any genericity or typicality claim at transport scope** — not
  posable there (D52, D56).
- **"H1 is discharged"** *bare* — it is discharged **only** at two-actor
  delivery-free d42a scope, and the scope is part of the claim; at three
  actors and at transport scope it is untouched (§B6.13).
- **"residue 1 is closed"** *bare* — quotable **only with its scope
  clause**: residue 1 is closed **at two-actor delivery-free d42a scope**,
  still inside the stationary form, with transport untouched and three
  actors out of scope (§B6.13b, §B6.14).  The unscoped sentence remains
  forbidden — it would assert closure at three actors and at delivery
  scope, where nothing has been shown.
- **"D44a's closure theorem is unconditional"** and **"`Zhat` holds at
  every depth"** — same rule: true **there**, forbidden bare.
- **"infinite clocks via Sperner"** — withdrawn; the surviving route is
  trace counting (D54 round 1 BLOCKER 1).
- **"the atlas carries a gauge structure"** (in any dress: *"a `Z/2`
  gauge structure"*, *"the transitions generate a group"*) — the
  transition class is a **coboundary** on every substrate tried:
  delivery crystals, conflict crystals and crossed-conflict crystals,
  `H¹ = 0`, at every port convention, and no non-trivial structure group
  is exhibited anywhere (§B8.8, §B8.9).  The quotable sentences are
  *"non-identity transitions exist and are mutually consistent"* and
  *"the class is trivial"*.
- **"`max |D| = 2k` for a `k`-proposer crystal"** — a property of two
  swept **schedules**, not a law: `2k` is the bound's value when every
  depth-1 successor of an arbitration is a delivery.  The true ceiling is
  W4c's `k·b ≤ k²`, and it is **realized at every `k` anyone has built —
  3, 4, 5 and 6** (§B8.9).  The same rule covers *"the delivery is what
  gives the crystal a second direction"*: the second direction is a
  second **concurrent conflict axis**, and the widest records in the
  corpus are delivery-free.
- **"width and uniformity compose only on the interior at `k = 4`"** (in
  any dress: *"no whole `k = 4` record is in band"*, *"there is a
  width-uniformity frontier"*, *"`k²` is unrealized at `k = 5`"*) —
  every one of these was written on a sweep that stopped one round and
  one levelling pass short of its own counterexample.  `DOUBLE-GRID(4,4)`
  is inside **both** `d = 3` band columns as a **whole** record at
  `max |D| = 16 = k²`, and `ARBCHAIN**` realizes `k²` at `k = 3, 4, 5, 6`
  (§B8.9).  The quotable sentences are *"the frontier does not exist"*
  and *"band membership is a **crossing** of a monotone family, read at a
  round number"*.
- **"the completions are precisely the objects that repair descent"** —
  false in **both** directions: the positive repair cone is
  573-dimensional at the depth-4 truncation while the `(depth, sigma)`
  family is a 28-dimensional slice, and repairing the commuting squares
  and descending to a record measure imply each other neither way
  (§B2.10).  Say instead: *the descent defect names the **job** the
  completions do; it does not single them out.*
- **"the record instrument is the exact boundary of permitted coherence"**
  (in any dress: *"coherence survives exactly between histories whose
  parents were already record-identical"*; *"the record instrument reaches
  back one step and decoheres precisely what it could already tell apart"*;
  *"F-II fires at depth 2, and only there"*) — an artifact of one
  **convention**, which forbids by hand, one level down, the cancellations
  that paper 29's actual decoherence condition explicitly permits.  Under
  the faithful condition **nothing is forced at any depth**, and an exact
  positive member carries coherence between two histories whose parents
  carry *different* records (§B2.11).  The quotable sentence is
  *consistency does not structure coherence.*
- **"a record measure of this shape cannot see a phase"** (in any dress:
  *"records cannot see a phase"*; *"the record demands are blind to the
  imaginary part"*) — a **shape tautology**: a row that sums over a
  product set is swap-symmetric and therefore annihilates the
  antisymmetric part, for any partition, any measure, any layer, with
  nothing computed.  It says nothing about records, and it **reverses**
  under the faithful reading, whose antisymmetric constraint rank is 268
  at depth 2 and 3,739 at depth 3 (§B2.11).  The quotable sentence is
  *the linear part of the two bracketing readings cannot see a phase,
  because both were built out of product-set sums.*
- **"the generated law admits a quantum layer"** *bare* — the space
  measured at closed scope is a fact about the record functor and the
  prefix map, not about the generated law (the coefficient matrix never
  sees the measure, and every strictly positive cut-consistent weight
  satisfies the same rows); and under the first fair **dynamical** demand
  the coherence dimension is **zero at every truncation tried**.  Quotable
  only with its reading, its depth, its record functor and its
  state-generation clause (§B2.11).
- **"the generated line is flat"** (in any dress: *"probability transport
  has no holonomy"*, *"the exchange defect vanishes"*) — true of **one
  grammar, one weight and one scope**, and false one grammar over.  Raw
  exchange flatness is a **theorem** on the placement grammar at closed
  scope (§B2.12), but the *normalised* kernel on the very same record graph
  has holonomy `⟨5/4⟩`, and at **transport scope 88 closed exchange squares
  carry `dP_AB/dP_BA ∈ {1/2, 2/3, 3/2, 2}`** with 40 more half-open — every
  one of them delivery-bearing, and none of them visible to the
  record-graph instrument.  The quotable sentence is *closed-scope raw
  transport is flat, as a theorem; transport scope is **curved**.*
- **"the direction index is the stage a rank-2 object lives on"** — the
  hint inverted on its own evidence: the wide charts' direction Grams are
  **two** matrices with degenerate spectra and stabiliser 8, and the narrow
  control is sometimes exactly `(1/4)I`.  A large stabiliser is **fewer**
  free components, not more.  Say instead: *a tensor stage needs
  **generic** — stabiliser-1 — direction geometry, which hand-built
  crystals do not have* (§B8.10).
- **"the trace already sits at the family's floor"** and **"`1.676e-5` is
  the family's floor"** — the number is the **rank-11 loser's** score in
  paper 30's own frontier, and the residual it names is a
  *sector-selection* artefact no function of the even 3-vector can reach.
  On the fixture the paper actually **selects**, the floor is `0` exactly
  (§B8.10).  The general rule this instances: **anchor on a paper's own
  selection, not on the tables it prints before falsifying them.**
- **"the `1.82` is the corpus's evidence for the odd-channel phase"** —
  `2·e^{−3/32}` reproduces all 32 published digits, and adversarial
  integers score `0` on the same test: the number is a **closed-form
  constant of the ansatz**, not a measurement about the record universe
  (§B2.12).  What it does establish is only that *some* record has
  `E = 3`.
- **"the odd-ring parity class is the phase"** — D66/D67's non-zero odd
  class is **label**-holonomy: its construction touches the weights
  nowhere and free relabelling trivialises it.  It is not a candidate for
  `Φ(O)` and may not be cited as one (§B2.12).

---

## 0.4 The whole story in thirteen sentences

*(Ten for the v10 campaign; one for the arc that precedes it, two for the
destination that follows.)*

1. The programme did not start here: for nine version lines it was
   **SHARD** — a ledger of *sealed records*, in which an irreversible
   commitment (a **seal**) destroys a coherent phase, and in which the
   classical/quantum line is whether an extra record could have been
   inserted in the middle (PART C).
2. The theory posits a world made of **records**: finitely many
   sequential *actors*, each writing versions on its own line, who
   propose values, arbitrate conflicts, deliver knowledge to one
   another, merge divergent versions, and idle.
3. **What may happen next is completely specified** — executable,
   exhaustively enumerable, with one function in a committed program as
   the sole authority — and the *relative weights* of the options are
   specified too.
4. **What actually happens is not specified**: the options at a moment
   sum to 2 or 5/2, not to 1, and the framework's own code says in its
   docstring that it makes *no measure claim*.
5. Turning weights into probabilities is called **completion**, and
   there is a theorem: you cannot have normalization, independence of
   the time-slicing, and untouched relative weights all at once — 36 of
   the 202 elementary loops of the enumerated depth-4 world refute it.
6. Dropping the third demand, completions exist; and in the
   delivery-free two-actor sub-theory a **canonical one exists that
   needs no boundary condition at all** — settled **at every depth**,
   because the two things it rested on are theorems: what
   a candidate event can see is settled by a dichotomy, and how the
   situation-summary updates is settled by a five-row table written out
   event by event — unique up to scale within a postulated shape, and
   pricing the beginning of the record identically to a later point the
   law itself cannot tell from the beginning.
7. But that shape is a **choice, not a law**: the two strongest
   invariance demands anyone has written down leave the freedom
   *growing* (12, then 32, then 125 dimensions as depth increases), so
   "the law completes itself" is true only of the law **plus** the
   shape.
8. Once deliveries are allowed — the scope where spacetime questions
   live — a short exact depth-free construction shows the menu of
   options grows without bound, so **no finite state summary
   reproducing menus exactly can exist, for any design**; the natural
   aggregated escape is closed too, so the method that settled the
   measure question provably cannot travel there.
9. In parallel, needing no measure at all, the theory has a
   **geometry**: the directions leaving an event form a *sky*, and how
   complicated a sky can be is **priced in actors** — one actor's
   worldline can only ever sweep a nested family of shadows, so
   realizing all subsets of *m* directions costs at least
   *C(m, ⌊m/2⌋)* actors (6 for four directions, 10 for five).
10. Records are **built** that pay the price: a 20-actor, 42-event
    record whose sky no circle can host, and a 42-actor, 84-event
    record whose sky no 2-sphere can host — so the admissibility layer
    does **not cap** the dimensional ladder at the sphere's rung, and
    whatever might prefer 3+1 is not in that layer.  Genuine sprinkled
    spacetime records, of every dimension tested, exhibit **none** of
    this — so the ladder measures coordination, not a record's
    dimension.
11. Both lines therefore arrive at the same wall: *does anything prefer
    3+1?* needs either a measure at delivery scope (no *bounded summary*
    of one can exist, by the unbounded-menu theorem), or a resource-cost
    principle, or a
    counting-typicality argument — and the corpus has **none of the
    three**, the last of them not even posable until the first lands; and
    beneath that sits a deeper one, since the *identified*
    law of measured physics and this generated grammar meet only at a
    **named missing map**, so until it closes the grammar's geometry and
    the laboratory's clicks are two ledgers — though three segments of that
    map are now measured: the generated law's *normalized* kernel does
    **not** descend to a measure on records, by exactly one repairable
    defect (the ratio of two menu totals), while the settled completion's
    measure genuinely does; and the quantum layer such a law could carry
    is large but structureless — consistency permits interference
    everywhere and prices it nowhere — while the **first** demand that the
    interference be generated by the law's own state leaves *none of it*,
    so at that scope a quantum layer cannot be both state-generated and
    coherent, and where superposition enters is now one of the
    programme's sharpest open questions; and the **phase** such a layer
    would need is exhibited nowhere in this line at all, every loop the
    theory owns returning a positive real number — though probability
    transport, flat at closed scope as a theorem, turns out to be
    **curved** where the geometry lives; and the measure itself, attacked from what the
    walls left standing, turns out to have a **surviving route** — the
    law's own finite-horizon kernels are proper out to a horizon of seven,
    their drift contracts at every pool and depth measured including a
    318,704-history four-actor arm, and what is missing is no longer a
    tool but a **bound**.
12. That earlier corpus already owns one piece of Einstein: it derives the
    field equations **in form**, as the thermodynamics of records, and
    proves — by one structural theorem, not a list of failures — that it
    **cannot** derive Newton's constant, because a ledger of counts and
    ratios carries no absolute length (PART C, chapter C2).
13. And the destination is now stated: **not** resemblance to a discretized
    flat spacetime — that target is withdrawn, with a measurement behind
    the withdrawal — but **full Einsteinian manifolds, enriched until
    quantum particles can be created in them**; of its eight arrows two are
    in hand, two are half in hand, three are open, and the last is blocked
    — and on the manifold arrow the width road now runs through **crossed
    conflict**, where records with no messages in them at all carry charts
    of nine, sixteen, twenty-five and thirty-six directions against a
    delivery circuit's four and a real spacetime's ten to seventeen, and
    the sixteen-direction one sits inside the band real sprinkled records
    occupy while carrying that width, while the charts' measured
    transition maps are **pure gauge** on every substrate tried, so the
    tensor programme still starts at zero — and the phase, which is what
    would complete a metric rather than merely decorate it, is not missing
    from the corpus but was found three version lines ago, receipted, and
    shelved, so that the live question is now whether the **curvature just
    measured in probability transport** carries an imaginary part or is
    only a positive number wearing a loop (PART D).

---

## TABLE OF CONTENTS

### FRONT MATTER
- §0 What this document is
- §0.1 Provenance labels
- §0.2 The two disciplines
- §0.3 Forbidden sentences
- §0.4 The whole story in thirteen sentences

### PART A — THE THEORY WITHOUT MATHEMATICS

- **A1. The world as a record** — actors, lines, versions; how well
  defined an actor is; what is deliberately *not* claimed; why the
  number of actors is physics and not bookkeeping.
- **A2. The click law** — the six kinds of thing that can happen; what
  is completely settled (what *can* happen), what is settled but odd
  (relative weights), what is not settled at all (what *does* happen);
  the known warts; the **three senses** of "the click law"; the
  programme's other stream — the identified law; the three measured
  segments of the map between them — the descent defect, and the quantum
  layer the law turns out to admit and the first dynamical demand takes
  away; and **the phase** — the imaginary exponential the corpus found,
  receipted and shelved three version lines ago, and the measurement that
  says where it can still be.
- **A3. Relativity without a global now** — cuts, slicings, gauge;
  views that lag; delivery as a two-way join; why every law here must
  be slicing-independent.
- **A4. Diamonds, and the flatness test** — the smallest loops, why
  agreement on them is the whole condition, and the three different
  things the word "diamond" means in this corpus.
- **A5. The sky** — directions, shadows, and the three committed ways
  of saying "the sky at an event"; what shattering actually requires;
  the instrument that was demoted; and the test that reads real
  spacetime's dimension.
- **A6. The measure problem** — the impossibility, the escape, the one
  canonical completion, why "the law completes itself" needed an extra
  postulate that turned out to be a choice, and how the last structural
  gap was closed at two actors, delivery-free.
- **A7. Buying dimension with actors** — why counting clocks was the
  wrong instrument; the shatter ladder; the theorem that dimension has
  a price in parallelism.
- **A8. Building the witnesses** — couriers, backflow, and the two
  records that pay the price; what they license and what they do not;
  the crystal, a record that tiles; the wide crystal that tiles *and*
  spreads; the theorem that says where the next width must come from;
  the transition maps between the charts, which turn out to be
  pure gauge; and the crystal made of conflicts, which tiles, reaches the
  corrected width ceiling with no messages in it at every dispute size
  anyone has built — nine, sixteen, twenty-five, thirty-six — holds the
  sprinkling band at sixteen, and glues just as trivially; and the
  rank-2 question the whole width road is *for* — whether anything in
  this programme is a metric rather than a table of covariances.
- **A9. The wall and the crack** — why the delivery-scope theory has
  no finite summary, the one thing that survives, and the route that
  survives it: the horizon limit, contracting everywhere measured and
  waiting only on a bound.
- **A10. The graveyard** — everything tried and discarded, and why
  that list is the best evidence in the document.
- **A11. Where we are, and what would decide it** — the two lines, the
  convergence question, the ranked open problems, and the method.

### PART B — THE THEORY WITH THE OBJECTS

- **B1. Actors, records, lines** — the primitive, its four defining
  properties, the aggregability results (D48) with counts.
- **B2. The grammar and the weight system** — the six event types with
  carriers and admission clauses; `candidates_for` as sole authority;
  the `1 + k/4` ladder with its spectra; the honest status ladder
  (i)–(vi); the `h12` off-ladder configuration; the merge pricing
  divergence; **the action line, the identified law, and the missing
  map**; the map's first measured segment, where the generated law is
  gated against paper 29's descent conditions one by one; and its second,
  where the functional slot above that law is measured by exact rank —
  permitted everywhere, priced nowhere, and emptied by the first
  dynamical demand; and **the phase segment** — the shelved amplitude
  form `A(R) ~ e^{−K(E)}e^{iΦ(O)}`, the holonomy identity the corpus
  proved in two halves that never met, and the weld's measured verdict:
  closed scope flat as a theorem, transport scope **curved**, and no
  `U(1)` part anywhere yet.
- **B3. Cuts, foliations, views, transport** — canonical classes; the
  own-view lag with its census; the monotonicity failure; the join-view
  lattice; the two-way join.
- **B4. The cut complex and the flatness ladder** — 1,191 / 427 / 202;
  the telescoping theorem; the three diamond senses disambiguated.
- **B5. The sky instrument** — SKY-A/B/C as the code defines them; the
  disjoint-row lemma and the capacity condition; the capacity laws in
  their two variables; the demotion; and the dimension discriminator with
  its two-sided controls.
- **B6. The completion dichotomy** — the theorem, its forcing, the
  gradient class, the quantum lift, residue 1, the settlement, the
  form-is-a-choice result, (H1) proved at two-actor scope by the
  own-view dichotomy, (H2) proved by the update table, and residue 1
  closed at that scope.
- **B7. The dimension ladder** — the doctrine, the collapse of
  counting, the shatter ladder with its exact certificates, the
  Dilworth gate with proof, trace counting.
- **B8. The constructions** — the courier architecture; the shatter-4
  and shatter-5 records; the generalized builder; what is licensed; the
  controls; the crystal's tiling capacity; the wide crystal that
  composes tiling with width; the branching bound that caps chart
  width at the delivery grammar's ceiling; the transition cocycle,
  whose class is a coboundary; and the arbitration crystal — conflict
  tiles, the dead-wire refinement `k·b ≤ k²`, delivery-free double grids
  that realize it at `k = 3, 4, 5, 6`, height-levelling as the mechanism,
  and a whole 16-wide record inside both `d = 3` sprinkling band columns;
  and the even Gram — the rank-2 candidate the corpus computed and threw
  away for its trace, resurrected, and found to be a covariance.
- **B9. The transport wall and the sector crack** — the
  self-arbitration ladder; the design-independent no-go; what remains
  exact; the open sector-exact question; and the **horizon limit**, the
  route the walls leave standing, with its measured contraction, its
  symmetry theorem at the root, and the named engine for its missing
  bound.
- **B10. The graveyard, itemized** — claim, killer, survivor, for each
  retired object.
- **B11. Status, open problems, method** — the ranked residues; the
  papers; the review statistics.

### PART C — THE EARLIER CORPUS (v1–v9, the SHARD / ISP arc)
*Each chapter carries both registers: ① PLAINLY (the non-technical twin) then ② THE OBJECTS.*
- **C1. The sealing premise and the original programme** — seals, holonomy,
  refinability, the Barandes barrier; the quarter law with its proof and
  receipts; the dissolved `[TARGET]`; the universality trap.
- **C2. Gravity from sealed records** — the Einstein FORM derived; the
  unified no-go on Newton's `G`; the second-scale test; graviton spin-2
  blindness; the Jacobson–Clausius conditional and the internal asymmetry;
  the three walls.
- **C3. Quantum foundations results** — the revival no-go; the
  gravitational-decoherence undecidability theorem; the Bell verdict; magic
  != indivisibility; Born = K1 and paper Va's 22 corpus-bound tags;
  covariantization by discreteness and the residues it leaves.
- **C4. The consolidations and the spin-offs** — v7 frozen; v8's 51 -> 6
  consolidation and its CONFIRMATION-PASSED grade with the referee-grade
  gap declared; the Yang–Mills line and its errata; Walsh–delta.
- **C5. The lineage question, honestly** — what is established, "the bridge
  is empty", the specified-but-unrun bridge measurement, and an explicit
  RELATION UNESTABLISHED list.
- **C6. The v9 channel-manifold arc — the other road to the manifold** —
  a *different* formalism (slots, celestial clocks, direction-valued
  deposits, churn); the two-clock wall and the parking hypothesis; the
  impossibility discovery and the channel-manifold law
  (`d = dim(channel manifold) + 2`; `S²` for 3+1); round 45's four
  isolated mechanisms and the arc review's retraction; 45e's NOT-PARKED
  with its 4D-by-volume positives; the **free-web influence theorem**
  (no coupling ⇒ no collective excitation at any scale ⇒ matter requires
  coupling); rounds 46–48d and the funded review that downgraded them to
  **PARKED-AT-PROTOCOL**; the unscheduled queue; the line's closure by
  user directive; a second RELATION-UNESTABLISHED note.

### PART D — THE DESTINATION
- **D1** The destination, stated — full Einsteinian manifolds enriched to
  create quantum particles; why the sprinkling target was withdrawn.
- **D1b** The **scale doctrine** `[BINDING]` — no fixture-scale object is a
  particle; units certify scale-invariant mechanisms, not objects; its
  convergence with the free-web theorem.
- **D2** The roadmap, arrow by arrow, with honest status — eight arrows,
  two HAVE, two PARTIAL, three OPEN, one BLOCKED; **arrow 3 carries both
  roads** (v10's atlas instrument, its wide crystal, its two proved width
  ceilings, its conflict crystals realizing the second of them at every
  dispute size built, and its trivially gluing transitions; v9's grown
  webs).
- **D3** Particle creation, and one labelled speculation — the
  boundary-freedom <-> vacuum-ambiguity resemblance, costed and marked.
- **D4** What the destination changes about the open problems.
- **D5** The destination in one paragraph.

### BACK MATTER
- **GLOSSARY** — every term, one line each, cross-linked.
- **GAPS IN THIS DOCUMENT** — what had to be compressed.

---

# PART A — THE THEORY WITHOUT MATHEMATICS

> **How to read Part A.**  There are no formulas here and no unexplained
> technical words.  Numbers appear only where a number is the point.
> Every chapter ends with a box called **"what this chapter does NOT
> claim"**, because in this programme the boundary of a claim is as much
> a result as the claim.  Each chapter also names its technical twin.

---

## A1. The world as a record

*Technical twin: Part B, chapter B1.*

### A1.1 The starting picture

Ordinary physics starts with things in space that change in time.  This
programme starts somewhere else, on purpose.  It starts with a
**record**: a growing body of writing that never gets unwritten.

Imagine a small number of scribes.  Each scribe keeps one notebook.  A
scribe can only write at the end of their own notebook — they never
branch into two parallel notebooks, and they never insert into the
middle.  Each new entry a scribe writes must build on the last entry
*that same scribe* wrote.  Scribes can send copies of pages to each
other.  When two scribes have written incompatible things, one of them
can settle the dispute, and the settlement itself is a new entry — a new
page that supersedes what came before.

That is the entire ontology.  There is nothing else: no space, no time
axis, no particles, no fields.  The scribes are called **actors**, the
notebooks are **record lines**, and the entries that create new content
are **versions**.  The whole collection — all the lines plus the events
that couple them — is **the record**.

The intended analogy inside physics is: *actor is to record line as
particle is to worldline.*  A particle in relativity has a worldline, a
one-dimensional track through spacetime, and everything that happens to
the particle happens somewhere along it, in order.  An actor has a
record line with exactly the same shape of constraint.

**Where this picture breaks:** an actor is not a particle, and the
corpus is explicit that it is not.  See §A1.3.

### A1.2 How well defined is an actor?

This is worth answering precisely, because "how well defined is your
primitive?" is the first question a sceptic should ask, and here the
answer has two halves that point in opposite directions.

**Formally, an actor is exactly defined by four properties, and only
those.**

1. **Sequential.**  All of one actor's own events are in a single line,
   one after another.  An actor never forks.
2. **Its own chain of versions.**  When an actor writes a new version,
   that version must descend from the last version *the same actor*
   wrote.  This is called the **mint chain**, and it turns out to be the
   load-bearing constraint of the whole framework (§A1.4).
3. **Addressable.**  Actors can send to each other; you can say "this
   one, not that one".
4. **The source of width.**  How much can happen *in parallel* in the
   record is bounded by how many actors there are.  Nothing else
   supplies parallelism.

Everything the framework does with actors is a consequence of those
four.  There is no fifth property waiting to be filled in.  In that
sense the primitive is completely specified.

**Physically, an actor is uninterpreted — deliberately.**  Nothing in
the corpus identifies an actor with anything: not a particle, not a
region of space, not a degree of freedom, not a detector, not an
observer with beliefs.  The corpus has attempted to build such an
identification exactly once, in a serious way, and the attempt is
currently *blocked* (chapter A10).

It is important not to read that as evasion.  It is closer to the
opposite: an interpretation is a commitment that every downstream number
inherits, and the corpus's own rule is that such commitments are
declared, unsigned, and criticizable rather than smuggled in.  The
present state is: **the formal object is finished; the interpretation is
an open, named, blocked problem.**

### A1.3 What is explicitly not claimed

- Not claimed: that an actor is a particle, an atom, an ion, a field
  mode, a qubit, or a molecule.
- Not claimed: that a record line is a worldline in a spacetime that
  exists independently.  The programme's ambition runs the other way —
  the causal structure of the record is meant to *be* what spacetime is,
  not to sit inside one.
- Not claimed: that the number of actors in a model corresponds to the
  number of anything in a laboratory.

### A1.4 The number of actors is physics, not description

This is the least obvious result in the chapter and one of the most
consequential.

A natural thought: "surely how many actors you use is a modelling
choice.  If I have four scribes, I can always relabel two of them as one
composite scribe and get an equally valid coarser description — like
treating a molecule as one object instead of many atoms."

**That was tested and it fails.**  If you take a legal record with four
actors and merge them into two by relabelling, the merged text is very
often *illegal* as a record of the two-actor world.  Across four
different ways of merging, the fraction of legal records that survive
was 50%, 50%, 74% and 18%.  Worse, the fraction **falls as records get
longer**: 100%, then 88%, then 70%, then 48% for records of length one,
two, three and four.  Long records are progressively less mergeable.

The reason is precisely the mint chain (property 2 above).  Two
*different* actors are each allowed to propose against the same version.
If you merge them into one actor, that one actor is now proposing twice
against a version its own notebook has already moved past — which the
law forbids.

Two controls make this a statement about *how many actors there are*
rather than about *what they are called*: renaming actors one-for-one
leaves 100% of records legal, and so does the identity map.

**But two important qualifications, both of which are themselves
results.**

*First*, the coarse description is never *spurious*.  Every legal
two-actor record does arise from some legal four-actor record — all
1,190 of the 1,190 tested.  So merging is a *partial* operation: it is
"onto" (nothing in the coarse world is unreachable) but not "total"
(most fine records have no legal coarse image).

*Second*, the merge failure is about the **written text**, not about the
**causal shape**.  If you ask the weaker question — "does the *pattern
of what depends on what* in the merged record occur in some legal
coarse record?" — the answer is **always yes**: 10,608 out of 10,608
cases, and 196,304 out of 196,304 at a larger size.  The causal order
aggregates perfectly.

So the corrected statement is: **the labelled record does not aggregate,
but the causal order does — and the cost of aggregating is enormous
loss.**  The loss was measured.  Counting the distinct causal shapes
available at each length: four actors give 1, 2, 4, 9 shapes at lengths
one to four, while two actors give 1, 2, 3, 5 — and at length five the
gap opens to 19 against 8.  So a quantity computed after merging is a
quantity of the *coarse* world, and cannot be read back as a statement
about the underlying record.

That result — established, then narrowed by hostile review from the
first, more dramatic version of itself — is why the number of actors
counts as physical content.  And that in turn is what makes chapter A7's
pricing of geometry in actors meaningful: if actor count were a free
redescription, a price quoted in actors would be a price quoted in
nothing.

> **What this chapter does NOT claim.**  It does not claim that the
> coarse description is meaningless (two separate gates forbid that
> reading).  It does not claim anything at all about ions, molecules,
> constituents, or mass — the step from *actors* to *physical
> constituents* is itself a bridge of the kind chapter A10 records as
> blocked.  What is licensed is only the conditional: *if* constituents
> were actors, *then* a composite would be irreducibly many lines — and
> the "if" is unsigned.

---

## A2. The click law: what can happen, and how well defined that is

*Technical twin: Part B, chapter B2.*

### A2.1 The six kinds of event

Everything that ever happens in this world is one of six kinds of event.
The corpus calls the whole system the **click law**, because each event
is a discrete "click" of the record — something is written, and it
stays written.

1. **Genesis.**  One initial version, held by everyone.  The record
   starts from it.  The corpus calls this *"the declared supplied
   boundary"*, and that phrase should be noticed: **the grammar already
   contains one boundary object, by declaration, at the start.**  A
   large part of chapter A6 is about whether the theory needs *another*
   boundary object at the far end, and it is only honest to record that
   it definitely has one at this end.
2. **Propose.**  An actor writes down a candidate value, built against
   some version it currently holds.  A proposal is a purely local event:
   it happens on the proposer's own line and nowhere else.  It does not
   yet change what anyone holds.
3. **Arbitrate.**  A group of mutually incompatible proposals gets
   settled by one of the actors who made one of them.  The settlement
   picks a winning set and *creates the successor version*.  This is the
   only way new content becomes official.  Notably, an actor with a
   single uncontested proposal can arbitrate it alone — that is how
   anything ever gets accepted when there is no dispute.
4. **Idle.**  An actor does nothing, and *that gets recorded*.  This is
   not a trick to pad the arithmetic; a recorded idle is a real event
   with real consequences, and later chapters will show idles doing
   structural work.
5. **Deliver.**  One actor sends a version to another.  This is the
   only event that genuinely couples two lines — and it is best thought
   of as a **join of knowledge**, not a transfer of a package.
   Delivering something the receiver already has is legal and physically
   meaningful, because what changes is not *what is held* but *what is
   known*.
6. **Merge.**  An actor that holds two versions which diverged from the
   same ancestor can reconcile them locally, producing one version that
   supersedes both.

The first four are the "base" theory, the smaller world the corpus can
enumerate most deeply.  Deliver and merge extend it.  The distinction
matters constantly: several of the strongest results hold *only* in the
smaller world, and the corpus is severe about saying which.

### A2.2 Admissibility: completely defined, and executable

The rules for *when* each of these is allowed are stated entirely in
terms of what is already in the past of the event in question.  Nothing
consults a global state, because there is no global state (chapter A3).

For example: a proposal against a version is allowed only if the event
that created that version is in the past, no superseding of it is in the
past, and the same actor has no unresolved earlier proposal against it
in the past.  An arbitration is allowed only if all the proposals it
settles are in its past, the group is a complete group there, the base
has not been superseded there, and no earlier arbitration on the same
base is in its past.

The important claim is not any one clause.  It is this:

> **The admissibility half of the click law is complete.**  It is
> unambiguous, it is executable, it is exhaustively enumerable, and it
> has a single authority: one function in a committed program which,
> given a record so far, returns *exactly* the list of allowed next
> events, each with a number attached.  Every result in the corpus that
> needs to know "what can happen here" calls that function.  Nothing
> re-implements it.

If someone asks *how well defined is the interactive click law?*, the
answer for this half is: **as well defined as a computer program that
runs and terminates.**  You can enumerate whole families of legal
records exhaustively, and the corpus has: hundreds of thousands of them,
at declared depths, in exact arithmetic.

### A2.3 The weights: defined, structured, and not probabilities

Each allowed event also carries a **weight** — an exact fraction.  These
weights encode *relative* preference among the options.  Their structure
is itself a result: they come in quarter-sized packets.  At any point in
the record, the weights of one actor's options sum to **one plus some
whole number of quarters**.

The "extra quarters" have a name and a mechanism.  Each one corresponds
to a **causally blind join**: a place where knowledge has been carried
past a seal, so that an actor is being priced for an option involving a
situation it cannot see from its own vantage point.  A relay handing a
branch of a fork to a third party is the canonical case.  Count those
blind layers and you get the number of extra quarters.

That is a satisfyingly clean structure, and it holds exactly across the
enumerated families.  Two honest defects sit next to it:

- **One constructed configuration sits off the ladder entirely.**  It
  prices to slightly *less* than one, and the reason is that a *dead*
  group of proposals — one whose base has already been superseded —
  still inflates the denominator of a live option.  The corpus calls
  this the `h12` constraint.
- Consequently, **the "one plus quarters" law is false in general**
  under the current pricing.  It holds where the enumeration reaches; it
  is not a theorem at all depths.  The corpus does not patch it, on the
  stated grounds that the obvious patch would destroy the clean spectra
  everywhere else.  Instead the defect is *carried forward into the
  measure problem* (chapter A6): whatever eventually turns weights into
  probabilities will have to price dead groups, and that is where the
  reconciliation belongs.

### A2.4 What is NOT defined: probabilities

Here is the crux of the whole programme.

The weights **do not sum to one**.  At a typical point in the record,
the options sum to **two**, or to **two and a half**.  They are not
probabilities and were never claimed to be.  The framework's own code
says so in its opening comment, and the sentence is worth quoting
exactly as it appears in the source file:

> *Weight-system level only (RF4): no measure claim; the placement
> front (d42b3) owns normalization; the `1+k/4` ladder is censused per
> A7/A7'.*

So the honest status of the click law is a **ladder with five rungs**:

- **(i) What CAN happen** — *complete*.  Unambiguous, executable,
  exhaustively enumerable, single-source.
- **(ii) Relative weights** — *defined*, and structurally
  characterized (the quarter ladder), with one known off-ladder
  configuration and the general-depth statement false under current
  pricing.
- **(iii) What DOES happen — probabilities** — **not defined.**  Not
  "left as an exercise", not "obvious by normalizing": provably
  impossible to define naively, which is the content of chapter A6.
- **(iv) A known internal wart** — one particular merge is priced
  differently in two places in the corpus's own machinery (one
  sixteenth in one, one twenty-fourth in the other).  It is exhibited,
  recorded, and *not reconciled*.  The form-level results do not depend
  on it, and the corpus says so rather than quietly harmonizing the
  numbers.
- **(v) Reading-relative pieces.**  Some conclusions depend on a
  *representation choice* nobody has justified.  The clearest case: one
  comparison, run over eleven reasonable ways of grouping the same data,
  gives one verdict under **sixteen** groupings and the opposite under
  **nine**.  Wherever this happens the corpus says "reading-relative" out
  loud and treats "which reading is physically privileged?" as an open
  question rather than an implementation detail.

### A2.5 The one-sentence answer, in three parts

*How well defined is the interactive click law?*

The question has three answers, because the corpus uses the phrase for
three different objects.

> **The grammar's ADMISSIBILITY law is complete.**  What may happen next
> is unambiguous, executable, exhaustively enumerable.
>
> **The grammar's PROBABILITY law is provably not self-normalizing.**
> That is the subject of chapter A6, and it is a theorem, not a gap.
>
> **The IDENTIFIED law is empirically anchored but not proved
> record-closed.**  This is a third object, from the programme's other
> stream, and §A2.6 introduces it.

The first is a fact about a finished object.  The second is a theorem
about an unfinished one — which is what makes the unfinished part
interesting rather than merely incomplete.  The third belongs to a
different stream of the programme, and the relation between it and the
first two is the corpus's deepest named gap.

### A2.6 The other stream: the identified law

Everything above describes one of the programme's **two** descriptions of
dynamics.  There is a second, and a reader should know it exists, because
it is where the corpus touches experiment.

**The action line** asks a different question.  Instead of *what grammar
could generate a world?*, it asks *given the world we measure, what law
have the measurements already identified?*  Its answer is assembled from
a chain of results: that a whole-history process has no second generator
besides its own conditional measure; that the operational core of a
record law is a small, named set of ingredients; and a proposed principle
— **no silent erasure**: every lost distinction must be *received* by
records, so sealing is dispersal and never intrinsic destruction.

With those in place the identification is stated plainly: the clicks we
have already measured identify the **Standard Model plus effective
gravity, at the measured couplings, as the leading history generator over
the energies those measurements reach.**  The corpus is careful about what
that means.  It is *identified, not derived* — the status Newtonian
gravity held in its era, and defeasible for the same reason.  It says
nothing about physics at energies nobody has probed.  And it presupposes
a spacetime for the fields to live on.

**That last clause is the whole problem.**  The grammar of this chapter
presupposes *no* spacetime — generating causal structure is exactly what
it is for.  The identified law lives *on* a spacetime and says what
happens there.  So the two streams describe dynamics in two incompatible
registers, and the corpus's own audit says they **meet at one missing
map**: what is needed is a demonstration that the identified law is itself
record-closed — that its boundary state, its measure, its record
instrument and, pointedly, its **generated record grammar** are *derived*
rather than supplied.  They are currently supplied.

Part of the crossing exists.  There is a conditional theorem giving the
conditions under which a click law descends from the quantum functional —
roughly: the records being asked about must genuinely decohere, both
routes must name the same event, the conditions must carry positive
weight, and the boundary must be **sufficient**.  That last condition has
teeth: erase the record of an experiment's setting and sufficiency
breaks.

> **So: one programme, one missing map.**  Until it closes, the grammar's
> geometry and the laboratory's clicks are **two ledgers**, and no result
> may be carried from one to the other.

### A2.7 The first segment of that map, measured

For a long time "the missing map" was a name for something nobody knew
how to attack.  One piece of it is now a measurement, and it is worth
having, because it is the first time the corpus has held its own grammar
up against a demand written for the *other* stream and read off the
answer.

The demand is the simplest one in the descent theorem, and it is the one
a physicist would ask first.  Suppose two things can happen next and
neither prevents the other.  Then doing the first and then the second
should be as likely as doing the second and then the first — because they
end at the *same record*, and a probability of a record cannot depend on
the order in which a bookkeeper wrote it down.  Whether the grammar's own
law obeys that is a finite question, and it has been asked of **every**
pair, at every reachable point of the two-actor delivery-free world:
794,570 ordered pairs, nothing sampled.

**Three facts come back, and the first two are the interesting ones.**

> **The raw weights obey it perfectly.**  Take the framework's own
> unnormalized numbers — the ones that sum to two or two-and-a-half
> rather than to one — and the two orders agree, on every single pair,
> without exception.  Order-independence is already there in the weight
> layer.
>
> **The normalized law does not.**  Divide each option by its menu's
> total, as anyone must to get probabilities, and the two orders disagree
> on about one pair in thirteen of the pairs the theorem actually speaks
> to (32,256 of 425,334).
>
> **And the whole discrepancy is one ratio.**  The two orders differ by
> exactly the ratio of the two menus' totals — the *two* against the
> *two-and-a-half* of chapter A2 — and by nothing else.  Zero
> exceptions.  It disappears whenever the two intermediate menus happen
> to weigh the same, and it appears whenever they do not.

So the failure is not ragged.  It is one named quantity, it is a
quantity the grammar already had a name for, and the place it comes from
is exactly the place chapter A2's quarter appears: the total jumps from
two to two-and-a-half at the moment a hidden conflict becomes visible in
the joint view.  **The defect is the mass jump, seen from the measure's
side.**

It has a third face, which §A2.9 needs: read as a *loop*, the defect says
that carrying a normalized probability around a closed loop of steps
multiplies it by a power of five-quarters.  That is a holonomy — a real,
positive one — and it is removable, because it is a ratio of two
quantities each attached to a point.  Keep the number five-quarters in
mind; §A2.9 measures a *different* loop, at a wider scope, whose values
include two that no power of five-quarters can produce.

**What follows, stated exactly.**  There is no probability measure on
records whose conditional probabilities are the grammar's normalized
menus.  That is not a contradiction anywhere: it is the reason a
**completion** is needed at all, restated in the vocabulary of the other
stream.  A completion multiplies the weights by a positive number
attached to each record point, and a completion that depends only on
*how deep* the record is and *what situation* it is in cancels the ratio
identically — a two-line argument, not a measurement.

**And the corpus's own completion really does descend.**  The settled
root-free one assigns each record a probability that depends on the
*record* and not on the writing order — verified on all 5,548 record
classes of the family, with no exceptions.  That is the strongest thing
the corpus owns on this side of the map, and it was not free: a
completion can cancel the ratio and still fail to define a measure on
records, and one can define a measure on records and still fail to cancel
the ratio.  Both failures are exhibited, so neither implies the other.

**The tempting overstatement, refused.**  It is very tempting to say the
completions the measure line was forced into are *precisely* the objects
that repair this defect — that the two lines meet here.  They are not,
and it does not.  Count the repairs: at the depth where the count is
exact there are **573** independent directions of positive repair, of
which 205 also define a record measure, of which the corpus's family is a
**28**-dimensional slice, of which the settled completion is a single
ray.  What collapses 573 to 1 is the *shape* postulated in §A6.8 — the
choice, again — and not descent.

> **So the honest sentence is:** the descent defect names the **job** a
> completion has to do; it does not single out which completion does it.
> The measure line's freedom, priced in §A6.8 as a choice, is now priced
> again from the other side, with a number.

**And one of the theorem's other conditions holds for the empty reason.**
Two of them hold on the generated law and are checkable.  The remaining
one asks whether the records being spoken about *decohere* — whether the
alternatives have stopped interfering enough for a probability to be
worth assigning — and the generated law answers it without saying
anything, because it is a plain bookkeeping process on records with no
interference in it to begin with.  A condition that is satisfied because
its subject matter is absent is not satisfied in any useful sense, and
that vacuity is the next section.

### A2.8 The quantum layer the law could carry — and the demand that empties it

The generated law has probabilities of records and nothing underneath
them.  The *other* stream has something underneath: amplitudes, which
can cancel, and which are what makes a theory quantum rather than merely
uncertain.  So the obvious question about the map — and the one the
descent measurement pointed straight at — is whether a layer of that
kind could sit under the generated law at all.

The question is finite, so it was asked as arithmetic rather than as
philosophy.  Write down every table of "overlaps" between pairs of
possible histories that (i) adds up to the law's own record
probabilities, (ii) is positive in the sense a genuine quantum object
must be, (iii) is consistent when you look at one step less of history,
and (iv) does not depend on which actor you called A.  That is a system
of linear equations, solvable exactly.  Its solutions are counted, not
sampled.  Four answers were possible in advance and all four were written
down before anything ran: **none** (a wall), **only the boring diagonal
one** (quantum structure forbidden here), **many** (permitted, and
priced), or **interference forced** (the strongest result the map could
have produced).  The unit declined to bet on which — the programme's
record on guessing about its own quantum layer being nought for two.

**One thing had to be decided before any of it could be counted**, and it
is the same kind of decision §A6.8 calls a *choice*, one level up.  "Adds
up to the law's own record probabilities" can be written three ways: the
weak one, which only checks the totals within each record and never asks
the records to stop interfering with each other; the strict one, which
forbids interference between different records entry by entry, by hand;
and the one in between, which is what the parent paper actually states —
the *coarse* table, the one an observer of records would see, must be
diagonal with the law's probabilities down it.  All three are carried
below, and the middle one is the headline, because it is the demand that
was written rather than the demand that was convenient.  That decision is
made and not open.  Two smaller ones are still open and are labelled
wherever they are used: what "consistent one step back" should mean, and
which notion of *same record* to use — one was chosen, and a coarser or
finer one changes which pairs can interfere at all.

**The first answer, and it is a deflation dressed as a positive.**  There
are many — enormously many.  The space of candidate layers is a cone of
dimension in the millions at the depths where it can be counted, and the
interference part of it alone runs 9, 134, 1,491, 15,058 as the horizon
moves out one step at a time.  The ordinary classical answer sits in the
*interior* of that cone, so positivity — the demand that looks like the
quantum one — never binds at all.  And the demands *do not organize the
interference in any way*: not one interfering pair is forced to zero, at
any depth, in any variant.  Coherence is permitted **everywhere** and
priced **nowhere**.  It is permitted even between two histories the
record could already have told apart one step earlier — that case is
built explicitly, as an exact positive example, and it is precisely the
case that the strict-by-hand way of writing the demand rules out, which
is one of the two retired sentences in §A10.14c.

Worse for the positive reading: the whole count never sees the law.  Swap
the law's own weights for a completely different set of positive weights
and every equation is unchanged, term for term — only the right-hand
side moves.  So the cone is a fact about the **record instrument and how
histories extend**, not about the generated law.  "The generated law
admits a quantum layer" is a sentence that is true of essentially any
bookkeeping on this substrate, which is another way of saying it is not
about the law.

**The second answer is the sharp one, and it points the other way.**  A
consistency demand is not a dynamical demand.  The natural dynamical
demand — the one the framework's own settled machinery makes available —
is that the interference not be free-floating decoration but be
*generated by the law's own situation-summary*: whatever coherence two
histories carry should be a function of the two situations the law is in,
and of nothing else.  This demand is **fair** in the only sense that
matters: the ordinary classical answer satisfies it, so it cannot be
accused of excluding the thing it was written to test.

Impose it and the interference dimension is **zero**.  At every horizon
tried — where the consistency demands alone had left 0, 50, 744 and
8,074 independent directions of interference — the dynamical demand
leaves none.  *(The demand is imposed on the **strictest** of the three
ways of reading the record condition — the reading whose equations pin
the generating rule one entry at a time.  Against the middle, faithful
reading it is a different computation, and that one has not been run;
the gap is part of the open question below.)*  And the reason is structural rather
than numerical: the
permitted/forbidden split that the strict reading *does* produce — and
that reads like a physical boundary — is **invisible** to the law's own
state space.
Every pair of situations that carries a permitted coherence also carries
a forbidden one, at every depth — so a coherence that is a function of
the situation alone must be zero wherever either kind of pair appears,
which is everywhere.

> **The sentence, with its scope.**  At the closed
> two-actor, delivery-free scope, a quantum layer over this law cannot be
> both **generated by the law's own state** and **coherent**.  Consistency
> with the records is far too weak to structure interference, and the
> first fair dynamical demand removes all of it.

**What that leaves, and it is one of the programme's sharpest open
questions.**  Superposition must enter somewhere else.  There are three
named places: at **transport scope** — where deliveries
exist, and where the conflict weights, the mass jump and the whole
dimension mechanism already live; at a **different joint** of the map
entirely; or under a **different fair dynamical demand**, since exactly
one was tried and its uniqueness was not established.  That last is the
cheapest to attack and nobody has attacked it.  The first is no longer
just a name: §A2.9 shows that transport scope is precisely where the
theory's probability transport stops being trivial, which is the only
place a phase could attach.

**And the phase story, where the easy sentence is false.**  It is very
tempting to say that a record measure of this shape simply cannot see a
phase — that no amount of record bookkeeping could ever pick out
interference's *sign*.  The sentence is on the blacklist (§0.3), and the
reason is that it is a property of how such equations are usually
written, not of records: a sum over a rectangle of possibilities is
symmetric under swapping the rectangle's two sides, and anything
symmetric that way is blind to the antisymmetric part automatically, for
any grouping of anything at all.  Written the way the parent paper
actually states it, the record demands **do** constrain phases, and
the constraint has a size (ranks 268 and 3,739 at the two depths where it
was computed).  Positivity sees phases too: the same example that carries
interference stops being positive when its imaginary part is doubled.

> **What this measurement is NOT.**  It is not a construction.  Nobody
> derived a quantum layer for the generated law; what was measured is the
> *space of candidates* for one, at one scope, under one record
> instrument, with one dynamical demand.  The map's functional segment is
> **narrowed, not discharged** — and narrowed by a negative: the shape of
> layer the segment needs cannot be built the obvious way at the scope
> where the corpus can compute.

> **What this chapter does NOT claim.**  That the weights are
> probabilities, or ratios of probabilities of anything observed.  That
> the quarter ladder holds at all depths.  That the two merge prices
> can be reconciled.  That the choice between the two arbitration
> kernels (two different, equally available rules for who wins a
> dispute) has been made — it has not; both remain posited
> alternatives, and they *disagree observably* on a three-way dispute.
> That any candidate layer counted in §A2.8 **is** the other stream's
> quantum object — none is, and none is claimed to be.  And nothing here
> claims the grammar **is** the identified law of §A2.6, or that any
> result about one transfers to the other: that transfer is exactly the
> missing map — of which §§A2.7–A2.9 measure three segments, from the
> generated side only, at two actors without deliveries, and no wider.

---

### A2.9 The phase: found, shelved, and hunted again

Everything in §A2.8 was about *whether* interference could sit over this
law.  This section is about the thing interference is made of — a **phase**,
the imaginary exponential `e^{iθ}` — and it is the one place in this
document where the honest report is not "we have not got there yet" but
**"we had it, wrote it down with a receipt, and put it away."**

**What the corpus already found.**  Three version lines back, a dedicated
campaign asked exactly the obvious question: can the record amplitude be
the usual `e^{i·action}`?  The answer was **no**, and it was a measured no
— the naive continuation destroys the agreement between the law and its
own reversal, in eight different ways.  But the same campaign found the
form that *does* survive, and its error is not small, it is **exactly
zero**:

> **the amplitude of a record is a real shrinking factor on the part of
> the record that is unchanged by reversal, times a pure phase on the part
> that changes sign.**

Real decay on the *even* channel, phase on the *odd* channel.  The reason
given was the same one that makes an odd quantity awkward in the first
place: something that flips sign under reversal cannot be a positive
observable, but it can be a phase.  This was never promoted to a theorem
and never carried forward, and the successor line — the one this book is
about — was built entirely out of positive real numbers without the
question being reopened.  A note that would have decided whether to reopen
it was scheduled, in a plan file, and never written.  **The deferral was a
descoping decision, not a finding.**

Alongside it sit three more facts, all of them already in the corpus and
none of them talking to each other: an earlier paper *derives* the complex
numbers as the value space and uses positivity to pick the ordinary circle
of phases over its impostor; a sibling document lists that same result as
an **input** rather than a derivation; and a third proves the records
cannot **force** it.  And a gated receipt in yet another paper returns, in
its own words, a **failure** for the real-only branch: positive real
weights provably cannot produce the cancellation that makes a theory
quantum.

**And the phase, if it exists here, has a name already.**  The programme's
founding question — written in the corpus's own front page, before any of
this — was whether quantum interference could be understood as the
**holonomy of probability transport**: you carry a probability around a
closed loop of steps, and you ask whether it comes back changed.  That
question and the odd-channel phase are not rivals.  They are one object,
proved in two halves on pages that never met.  One half proves that the
holonomy of a closed route pair *is* a phase and that two-route
interference *is* the loop-phase law.  The other half proves — with a
receipt, and without ever using the word *holonomy* — that reversing a
record's order conjugates its amplitude, which is the defining behaviour
of a holonomy phase.  **One sentence welds them, and the corpus never
wrote it:** that reversing a record's internal order is the same operation
as running a transport loop backwards.

**So the weld was pinned and tested, and the answer is the most
interesting kind of negative.**  The identification half survives: the two
reversals do have a common carrier, and on the small fixture they are
literally the same map.  The *holonomy* half dies where it was looked for
— and comes back to life one step outside.

- **At closed scope, on the grammar the measure line lives on, transport
  is flat — and that is now a theorem, not a measurement.**  Take any two
  things that can happen next, do them in either order, and the two
  products of weights are equal, at every depth.  The proof has six
  steps and they are worth compressing to one line each: what an event
  weighs depends only on its own past; two events interact only if they
  touch a common register; if they do not, they simply commute; if they
  do, one of them is always an **idle**; an idle changes nothing; and an
  idle always weighs exactly three quarters.  Sixty-four thousand loops,
  no exceptions.
- **But half of that proof is a coincidence of one grammar's budget.**
  The last two steps hold because two of the law's four budgets are set
  to the *same* quarter and exclude each other.  Change either constant
  and half the loops stop being flat.  That is a tuning, not a structure,
  and the book says so where it says the theorem.
- **One grammar over, it does fail — and that grammar is the one where
  the geometry lives.**  At transport scope, where deliveries exist,
  **eighty-eight closed loops come back changed**, by factors of a half,
  two-thirds, three-halves and two, with forty more loops that cannot
  be closed in one direction at all.  Every single one of them carries a
  **delivery**.  The shallowest sits two events above the empty record.
  **So probability transport in this theory is curved, and the curvature
  is carried by messages.**
- **The instrument the programme had could not have seen it.**  The
  census that certified flatness runs on the *record* graph, and a loop
  closes at record level exactly when its two events touch no common
  register — which is exactly the case the locality argument already
  covered.  The argument and the census have the same blind spot, and the
  whole defect lives in it: **none** of the eighty-eight closes at record
  level.  Where the instrument *can* see, the transport really is flat for
  a boring reason — the weight is an exact gradient there.
- **And the process's own probabilities were never flat either.**  The raw
  budget numbers are not probabilities; dividing by their total is what
  makes them one, and that division has its own holonomy, already known
  and already priced elsewhere in this book as a repairable defect.

> **The result, stated as it stands.**  Every closed loop in this theory
> that has ever been exhibited comes back multiplied by a **positive real
> number**.  Some of them come back multiplied by one; some by a half.
> **None of them comes back multiplied by a phase.**  A real holonomy of
> probability transport exists here, and it has no argument.

That last sentence is the honest state of the phase question, and it is
sharper than "we do not know".  The founding slogan is refuted *in the
direction the pre-registered falsifier named*: transport does have a
holonomy; it simply is not a phase, yet.  And the transport holonomy is
**not** the already-known defect wearing new clothes — two of its four
values lie outside that defect's group entirely, which is the first
evidence in the corpus that it might be a genuinely new object.

**Where that leaves the imaginary exponential.**  It has exactly one known
address left, and the address is specific rather than atmospheric: the
**odd sector of the curved transport loops**.  The even part of a record
is where the real shrinking lives; the odd part is where a phase would
have to live if there is one; and transport loops are now the only place
in the theory where anything at all fails to come back unchanged.
Characterising that holonomy — what carries it, what group it lives in,
whether it is removable by relabelling, and whether its odd sector has an
imaginary part — is the next unit, and it is the hinge of everything in
Part D.

**Three working assumptions died on the way here, and they are worth
carrying.**  The non-zero class the width road found in odd rings is
**not** a candidate phase: its construction never touches a weight, and
relabelling makes it vanish.  The number that had been quoted as the
strongest evidence for the odd-channel form — a decay-constant test
scoring 1.82 for the rival and 0 for the survivor — is a **closed-form
constant of the formula**, reproducible in one line and matched by
deliberately adversarial inputs; what it actually shows is only that some
record has a particular small integer in it.  And one structural
constraint nobody had stated turns out to be binding: the transport
holonomy vanishes identically **along the one-dimensional path of
commitment**, so any phase this theory ever carries must live *transverse*
to the order in which things are committed.

> **What this section does NOT claim.**  That the generated law is
> complex, or has an amplitude, or carries interference.  It does not.
> That the shelved form is correct — it is an unlifted result of an
> earlier version line, and this book cites it as archaeology.  That the
> transport curvature is a phase — it is measured, exhaustively, to be a
> positive real number.  And that any of this reaches the identified law:
> it is the same missing map as everywhere else in this chapter, measured
> from one side only.

---

## A3. Relativity without a global now

*Technical twin: Part B, chapter B3.*

### A3.1 There is no global state

In ordinary quantum mechanics you can ask "what is the state of the
world right now?".  In a relativistic theory you cannot, at least not
without choosing a slicing, and different observers choose differently.
This framework takes that seriously from the ground up: **there is no
global "now" anywhere in it.**

What exists instead:

- **A cut** — a slice through the record, a candidate "now".  Some
  events are behind it, some ahead.
- **A foliation** — a whole sequence of cuts, i.e. one specific way of
  laying the record out in a single order, respecting who depends on
  whom.  In the formal language, a foliation *is* one linear ordering
  consistent with causality.
- **Causal order is physical.  Incomparable order is gauge.**  If two
  events do not depend on each other, then the *order you happen to
  list them in* is bookkeeping, not physics.  Two records that differ
  only by swapping such events are **the same record**.  The corpus
  works with **canonical classes** — records identified up to exactly
  that freedom.

This is not decoration.  It is the demand every candidate law in the
corpus is tested against, and it is what kills the naive attempt to turn
weights into probabilities (chapter A6): the naive recipe gives
different answers depending on which slicing you compute it in, and a
relativistic theory may not tolerate that.

### A3.2 Views, and the fact that actors act on stale information

Each actor has a **view**: the part of the record it has witnessed.  The
**full view** at a point is everything that has happened.  An actor's
**own view** is only what has reached it.

**The own view lags the full view, and the lag is real.**  This was
measured, not assumed.  Across a family of nearly thirteen thousand
(actor, history) situations, the view an actor actually consults when
deciding what it may do exceeds its bare causal past in about eight
percent of cases, by at most four events — and in **every single one** of
those cases the extra events were **authored by the opponent**.

That last detail is not a curiosity; it is the reason a whole proof
strategy died (chapter A10).  The lag is not the actor's own
bookkeeping leaking in.  It is the *other* actor's activity becoming
visible through the wires the candidate event touches.

**And the lag is not simply "less information".**  The most
counterintuitive fact in this chapter: **a smaller view can offer MORE
options.**  The mechanism is concrete, and it is *not* the one it is
natural to guess.  It is not that an actor forgets its own earlier
proposal — an actor's own live proposals are always in its own past, so
that can never happen.  It is **missed supersession**: a settlement has
already retired a version, but the lagging view has not seen the
settlement, so it still counts that version as available to build on.
See less, do more.

This single fact demolishes any argument of the form "the lagged view
sees a subset, so it can only have fewer options, so the lag can be
bounded".  A whole family of attempted proofs, including the one the
corpus itself had pinned, rests on that step and is therefore unsound.

### A3.3 Menus run on views, and delivery changes only who knows

At delivery scope, this gets sharper still, and it is the cleanest
demonstration in the corpus that **knowledge itself is a physical
variable**.

Take two records.  The second is the first plus one delivery.  Choose
the delivery so that the receiver **already holds** the delivered
version: nothing is created, nothing is superseded, nobody's holdings
change.  By every summary of *what exists*, the two records are
identical.

**Their menus differ.**  In the verified witness, one actor's idle
weight moves from one half to three quarters, and two of its proposal
options *disappear entirely*.  Why: before the delivery, that actor's
own view had not seen that its base was superseded, so it could still
propose against it.  After the delivery, it has seen.

> **A delivery can change nothing about what is held and still change
> the law's menu, because it changes who knows.**

That is what "menus run on views" means, and it has a hard consequence
(chapter A9): any summary of the world that only records *what exists*
is too coarse at delivery scope, and one that was believed adequate was
refuted this way, with a two-line counterexample.

### A3.4 Delivery is a join in both directions

One more structural fact, discovered the hard way while trying to build
something (chapter A8).

Naively, a delivery is one-way: the sender's knowledge flows to the
receiver.  It is not.  **When A delivers to B, the record also records
that A's line and B's line have met** — and so *A's* subsequent sends
carry B's accumulated past with them.  Knowledge flows *back up the
wire*.

This was found because a carefully designed nine-actor construction
failed for exactly this reason: the intended independent channels
contaminated one another after the first join, and the construction
achieved only eight of the sixteen distinct configurations it needed.
The fix — and the reason chapter A8 exists — was to send only into
*empty* receivers, so that nothing folds back: dedicated single-use
messengers, called **couriers**.

### A3.5 Why foliation-invariance is the demand, not a preference

Put the pieces together.  If a law's predictions depend on which slicing
you used to compute them, then two observers who slice differently
disagree about probabilities, with no fact of the matter to settle it.
That is not a relativistic theory.  So:

> **Any candidate probability law in this framework must be a function
> of the record itself, not of the order you chose to read it in.**

This demand does real work.  It is one of the three demands in the
impossibility theorem of chapter A6, and it is the demand the naive
normalization violates.  It is also, unexpectedly, a demand that turned
out to add *nothing* on top of another one — a measured negative result
that closed off an obvious rescue (chapter A6 §A6.8).

> **What this chapter does NOT claim.**  That there is a preferred
> slicing (there is not, and finding one would be a defeat).  That views
> are observers with beliefs — a view is a sub-record, nothing
> psychological.  That the lag is small or negligible: it is bounded in
> the measured family at four events, and that bound is a measurement
> at a declared depth, not a theorem.

---

## A4. Diamonds, and the flatness test

*Technical twin: Part B, chapter B4.*

### A4.1 The space of "nows"

Take the enumerated world the corpus works with most: two actors, four
events deep.  Count the legal records: **1,191**.  Now identify records
that differ only by the order of independent events — remember, that
order is gauge, not physics.  You get **427** genuinely distinct records.

Now build a map.  Put a dot for every possible "now" (every cut), and
draw a line between two dots when one is reachable from the other by a
single legal event.  This is the **cut complex** — the space of nows,
with single steps as its edges.

### A4.2 A diamond is the smallest loop

Suppose from some now, two independent things could happen: event X and
event Y.  You can do X then Y, or Y then X, and you arrive at the same
now.  That closed four-cornered loop is a **diamond**.  Nothing exotic
— it is a commuting square.

In the depth-4 world there are **202** of these (counted up to gauge).

Why care?  Because diamonds are the test bench for **path
independence**.  Suppose you want to attach a number to every now, in
such a way that the numbers explain the steps — a "potential", in the
same sense as a height function explaining which way water flows.  For
that to be possible, going around any loop must bring you back to where
you started.  And since diamonds are the *smallest* loops, and every
larger loop is built from them, **agreement on all the diamonds is the
entire condition.**  This is standard discrete geometry: flat on all the
elementary two-dimensional cells implies a potential exists.

In physics language, this is a discrete version of the **integrability
condition** for evolving a state along arbitrary slicings — the discrete
Tomonaga–Schwinger condition.  In plain terms: *can you evolve the
theory along any slicing you like and always agree?*

### A4.3 The one result you need from this chapter

Run the test three times, on all 202 diamonds:

- On the **raw weights** (no attempt to normalize): **0 failures.**
- On the **naive fix** — at each now, just divide each option's weight
  by the total so they sum to one: **36 failures.**
- On a **properly constructed** completed law: **0 failures.**

The middle row is the whole problem.  The obvious way to make weights
into probabilities is path-dependent: it gives you different answers
along different slicings, in 36 out of 202 elementary loops.  Chapter A6
explains exactly why, and what it costs to avoid.

**Two things to carry forward from that table, because both are
load-bearing later.**  The top row — *the raw weights close every loop* —
is not a lucky measurement: it is a **theorem** at this scope, proved in
six steps, and §A2.9 gives them.  But it is a theorem about *this*
grammar, and half of it holds because two of the law's four budgets happen
to be the same quarter.  **Once messages are allowed, the top row stops
being zero**: eighty-eight loops come back changed, and the whole of §A2.9
is about what that means.  And the middle row's failures are not noise —
they are exactly the ratio of two menu totals, which is the same
repairable defect §A2.7 measures from the other side.

### A4.4 The trap in that table, defused

There is a natural but wrong conclusion to draw: *"the completed law
passes the geometric test the naive one fails, so the completed law is
right."*

**It is not that strong, and the corpus caught this itself.**  There is
a small theorem: *any* number-assignment that is (a) attached to nows
rather than to orderings, and (b) respects the gauge, will pass the
diamond test automatically — because the loop products simply telescope.
The receipt proves this by running a deliberately *wrong*
number-assignment (one with no dynamical justification at all) through
the same 202 diamonds: it passes all of them.

> **So what the flatness test certifies is gauge invariance, not
> correctness.**  Passing it is necessary, cheap, and no evidence at all
> for a particular choice.

By contrast, a number-assignment that is attached to *orderings* rather
than to nows genuinely fails — the receipt's example fails 51 diamonds.
So the test does discriminate; it just discriminates a different thing
than one might hope.

This is a good example of the corpus's habit of defusing its own
strongest-looking evidence.

### A4.5 Three different things called "diamond"

The word is overloaded in this corpus and confusing them produces
nonsense.  All three are real objects; they do different jobs.

1. **The 202 cut-complex cells** — this chapter.  Elementary loops in
   the space of nows.
2. **Paper 3's amalgamation figure** — a diamond-shaped diagram in an
   earlier paper whose result is that gluing two marked regions is
   *composition*, not the birth of a new carrier.  Nothing to do with
   counting loops.
3. **Action-level flat squares** — paper 29 checks flatness of a
   different quantity (an action-like functional) on squares.  Chapter
   A4's ladder generalizes that check; the objects are not the same.

And one thing they are **not**: the 202 are *not* the "causal diamonds"
of relativity — the region between two events, an Alexandrov interval.
That is a fourth meaning, from outside this corpus, and it is not what
these are.

**The word "flat" is overloaded the same way, and §A2.9 adds a sense, so
here are all four in one place.**  (1) **Diamond flatness** — this
chapter: a number attached to nows closes every elementary loop, which
certifies gauge invariance and nothing more.  (2) **Chart flatness** — an
atlas whose translation rules relabel away to nothing, which is what
§A8.8 measures and finds everywhere.  (3) **Transport flatness** — the
*weights themselves* returning unchanged around an exchange loop, which is
§A2.9's object: a theorem at closed scope and **false** at transport
scope.  (4) **Flat spacetime** — the thing the destination explicitly does
*not* target (§D1).  They are four different objects on four different
carriers, and a sentence that drops the qualifier is on the blacklist
(§0.3).

> **What this chapter does NOT claim.**  That flatness selects a
> completion (§A4.4). That the depth-4 complex is representative of all
> depths — it is the *decided* case, and every statement about it is
> scoped to it.

---

## A5. The sky

*Technical twin: Part B, chapter B5.*

### A5.1 The idea

Here is the geometric intuition the programme is chasing.

Stand at an event in ordinary spacetime and look outwards.  The
directions you could look in form a **sphere** — the celestial sphere.
In a world with only two space dimensions, they would form a **circle**.
If something blocks part of your view, the shadow it casts is a **cap**
on the sphere, or an **arc** on the circle.

*The shape of the sky is a signature of the number of dimensions.*  So:
if the record has an analogue of a sky, and if that analogue can be
tested for "circle-like" versus "sphere-like", then the framework could
in principle say something about dimension **without needing any
probabilities at all** — which is a large advantage, given chapter A6.

That is the programme of chapters A5, A7 and A8.

### A5.2 Making it precise, three different ways

In a record there is no continuum of directions.  There is only the
causal order: which events are in the future of which.  So "the sky at
an event" has to be *defined*, and the corpus refused to define it
once.  It committed **three** definitions in advance, before any data
was looked at, precisely so that a result depending on the choice would
be caught doing so:

- **SKY-A, the cover sky.**  The directions are the *immediate*
  successors of the event — the events right above it with nothing in
  between.
- **SKY-B, the antichain sky.**  The directions are the events at a
  fixed *height* above the event, so no direction is above another.
- **SKY-C, the dual past sky.**  Same as SKY-A but looking backwards
  into the past.

For any definition, once you have directions, each event further in the
future casts a **shadow**: the set of directions that lie below it.  The
collection of all such shadows — the corpus calls each one a **trace** —
is the object all the geometry is done on.

**Where this picture breaks:** these are three genuinely different
objects, and they **disagree materially**.  Any result holding under
only one of them is *reading-relative* and the corpus says so every
time.  Nobody has justified a privileged choice; that is an open
question, not a detail.

### A5.3 The test: shattering

How do you tell a circle from a sphere using only shadows?  With a
classical notion: **shattering**.

Pick some directions.  Ask: can you find shadows realizing *every
possible combination* of them — this one but not that one, those two but
not the other two, all of them, none of them?  If yes, the shadows
"shatter" that set.

The key facts, both **constructed by the corpus rather than cited**:

- **Arcs on a circle can shatter three directions, and never four.**
  (Four points around a circle: no single arc can contain the 1st and
  3rd without also containing the 2nd or the 4th.)
- **Caps on a sphere can shatter four**, including the genuinely hard
  case of two opposite edges of a tetrahedron, which is exhibited with
  an explicit certificate.

So a shattered set of four directions is a **certificate** that the
shadow system is not an arc system.  This is a one-sided instrument: it
can rule the circle out, and it can never rule the circle *in*.

That one-sidedness was declared as binding doctrine *before* any
measurement, and it turned out to be necessary rather than merely
cautious.  Which brings us to the two negative results that shaped
everything after.

### A5.4 First negative result: the demotion

The corpus originally intended a *second*, stronger instrument: a test
for whether a shadow system is *exactly* an arc system, which is
decidable both ways.  That would have been much better — it could say
"yes, circle-compatible" as well as "no".

It was run as a control on **genuine two-space-dimension Minkowski
records** — real, exactly computed, unquestionably 2+1 causal orders.
It **rejected 121 of 554** of their skies as "not arc systems".

**A discrete sky of real Minkowski space is not generally an arc
system.**  So arc-realizability is not a usable proxy for 2+1 at all,
and the instrument was **demoted to a diagnostic**.  (A later, sharper
recount on one of the definitions found the majority — 218 of 397 — of
genuine 2+1 skies non-arc.)

This is worth pausing on.  The corpus tested its own instrument against
a case where it knew the right answer, discovered the instrument was
wrong about the known case, and threw the instrument away rather than
the known case.  Everything after chapter A5 rests on the *weaker,
one-sided* test alone, because that is what survived.

### A5.5 What shattering actually requires, and the capacity condition

To shatter a set of directions you need *every* combination of them —
including the **empty** one: some later event whose shadow avoids all of
them.  The precise requirement is worth stating carefully, because a
weaker-looking version of it is false and cost the programme a result.

> **What is needed is a shadow DISJOINT FROM THE CHOSEN SET** — not a
> shadow that is empty outright.  A shadow can be non-empty (it may
> cover other directions entirely) and still meet none of the four you
> are testing.

The two coincide only when the chosen set is the *entire* direction set.
That single distinction decides which of the three sky definitions can
ever fire.

Under SKY-A the directions are the immediate successors, so every later
event lies above at least one of them and **no shadow is ever empty**.
That much is true, and it has exactly one consequence: a cover sky can
never shatter *its own full direction set*.  It says nothing at all
about shattering a four-element **subset** of a wider sky — and a wider
sky is the normal case.  A fifth direction's own shadow supplies the
missing combination on the other four while being perfectly non-empty.

**All three readings are live.**  SKY-A and SKY-C do shatter, on genuine
Minkowski records, and §A5.7 shows they are the readings under which the
instrument works best.  Which reading is physically privileged is
therefore an **open question**, not a settled one.

**Capacity still has to be gated, though.**  A test that "found nothing"
on a sky too poor to have found anything is not a measurement, and that
error was real: of 415 skies once counted as testable, **144** were
genuinely capable — a 2.8-fold reduction, not the tenfold one a
too-strong condition suggested.  So the honest capacity requirement is
the first two clauses only: **at least four directions, and at least
sixteen distinct shadows.**  Anything below that is reported as
undecidable, never as a negative.

### A5.6 How big can a sky get?

Two measured scaling laws, and they are in **different variables** —
which is the chapter's real deliverable.

- In a **Minkowski sprinkling** (points scattered in real spacetime),
  sky size grows with **density**.  With the box held fixed, the largest
  cover-sky runs 4, 7, 9, 14 directions as the number of points goes
  20, 40, 80, 160.
    *(The variable has to be density, not point count: let the box grow
  with the count and the sprinkling gets sparser as points are added,
  and the measurement reports the wrong thing.  Both columns are
  reported side by side.)*
- In the **record**, sky size grows only with **actor width**.  Over
  400 deep walks per width, out to depth 20, the largest sky has
  2, 3, 4, 4, 4, 4 directions at widths 2, 3, 4, 5, 6, 8.  **At width
  two the sky stays at two no matter how deep the record runs.**

> **Depth cannot buy what only width can.**

And the apparent plateau at four is **not a ceiling** — a denser probe
at width ten, with the SKY-B height parameter varied instead of pinned,
reaches five.  The corpus chased the suspicious flat line rather than
shipping it.

One more reversal belongs here, because it changed the conclusion's
character.  A control was built to check whether cross-actor causation
*produces* the sky sizes observed, or whether any record of that size
would have them.  The first control was broken twice over (it grouped
events by the wrong field, and its design could never have failed
anyway).  Rebuilt honestly — a random structure matched on size and
number of links — it reaches **seven** directions against transport's
**four**.

**Transport skies are narrower than chance.**  Against a control matched
on size and number of links — a control that *can* concentrate directions,
and does, reaching seven — the record's skies reach only four.  The law
*constrains* sky size below the generic value.  That is a real
restriction, not a by-product of record size, and it is the first sign of
something chapter A7 makes exact: sky richness is not free.

### A5.7 The instrument works: real spacetime reads its own dimension

The sharpest result in this chapter is that the test, run on genuine
sprinkled Minkowski records at sufficient density, **reads their
dimension** — and does it with controls on both sides.

Recall the exact geometry from §A5.3: shadows of arcs on a circle
shatter three directions and never four; shadows of caps on a sphere
shatter four and never five.  Now run the discrete test on real records:

| genuine sprinkled records | shatter 3? | shatter 4? | shatter 5? |
|---|---|---|---|
| two space dimensions (2+1) | **yes** | **never** | never |
| three space dimensions (3+1) | yes | **yes** | **never** |

That is the continuum ladder, reproduced exactly on discrete data.  On a
matched ladder of six sizes, the number of events at which a
four-direction set is fully resolved runs **0, 1, 11, 30, 116, 211** in
three space dimensions and is **zero at every size** in two.  Neither
shatters five, which is the halt condition the sphere's geometry
predicts.

**And it is not merely that bigger skies shatter more.**  Compare only
skies of the same size: in the band where the two dimensions have
comparable samples — 304 skies against 314 — the two-space-dimension
records shatter four **zero** times and the three-space-dimension
records shatter it **seven** times.  The signal survives the size
control.

Two further points keep this honest.

**Density, not size, is what the test needs.**  At low density the same
records shatter nothing, and reading a sparse sample as a negative is
exactly how this result was missed once: a sparse control, read through
the one sky definition that happened to be blind, returns zeros that
mean only "not enough events".

**And sprinkled records are not at zero on this scale — they are at
their own dimension's rung.**  Two-space-dimension sprinklings shatter
three, thousands of times.  What separates them from three-space-
dimension sprinklings is the *rung*, which is what a meter is supposed
to do.

> **So the shatter number is a dimension meter, and it works on real
> geometry.**  Chapter A7 gives the ladder its exact form, and chapter
> A8 uses it on the framework's own constructed records — which, as it
> turns out, read *above* every sprinkling of any dimension tested.

> **What this chapter does NOT claim.**  That any sky *is* a circle or a
> sphere — never licensed; the discrete test agrees with the continuum
> ladder, which is not the same as a record being one of those shapes.
> That the arc/cap dichotomy exhausts what a discrete sky can be — a
> discrete sky need be neither, and §A5.4 is why arc-realizability was
> abandoned as a proxy.  That an *absence* of shattering is evidence of
> low dimension in a single record: below the density at which the test
> fires, a zero means only that the sample is too thin.  And which of the
> three sky readings is physically privileged remains **open**.

---

## A6. The measure problem

*Technical twin: Part B, chapter B6.  The corpus's own standalone brief
on this is `v10/THE-COMPLETION-DICHOTOMY.md`, which this chapter
compresses.*

### A6.1 The problem in one paragraph

The framework says what can happen and how much each option "weighs".
The weights do not sum to one.  To get probabilities you must supply
something — a positive number attached to each possible now, used to
re-scale the options.  That supplement is called a **completion**.  The
question of this chapter is: *what does a completion have to be, and is
it forced by the law or chosen by us?*

### A6.2 Three demands, each obviously reasonable

- **(a) Normalized.**  At every now, the options sum to one.  Without
  this you have no probabilities at all.
- **(b) Slicing-independent.**  The answer must be a function of the
  record, not of which slicing you computed it in.  Without this, no
  relativistic theory (chapter A3).
- **(c) Ratios untouched.**  The *relative* weights of the options at a
  now should not be changed.  Without this, the completion is not
  merely normalizing the law — it is **changing** it.

### A6.3 The theorem: you cannot have all three

Here is the forcing, in four steps, and it is short enough to follow
without symbols.

1. Demand (c) says the relative weights survive.  So the only freedom a
   completion has, at each now, is one overall scale factor.
2. Demand (a) pins that factor: it must be exactly one over the total
   weight at that now.  **There is no choice left.**
3. So the whole question becomes a single yes/no: is that "total weight"
   quantity the kind of thing that can come from a potential?
4. **It is not.**  The total weight *is* attached to nows properly (it
   respects the gauge — verified constant across all 427 distinct
   records).  But being attached to nows is not enough.  Coming from a
   potential also requires path independence, and this quantity is
   path-dependent: **36 of the 202 diamonds refute it**, in two
   connected clusters, not one isolated pathology.

**And the mechanism has a name.**  The total weight **double-counts the
causally blind join layer** along exactly those slicings that expose it.
Two slicings of the same record disagree about how much weight a blind
layer contributes — which is why the products come out different.  You
can see it in the smallest case: along one slicing the totals run
2, 2, 2; along the other, 2, 2, and *two and a half*.  The jump happens
precisely when a blind pair becomes visible.

So: **(c) must go**, and that much no later result repairs.

### A6.4 An escape was tried, and closed

There is a way to restore the sums to one exactly: filter out the blind
part — the "zero-class counterterm".  It restores normalization by
exactly the missing quarters, and it respects the gauge.  It genuinely
refutes the impossibility result *as originally worded*.

**And it kills all joint arbitration.**  Every event where two actors
settle a dispute together gets weight zero.

So the theorem was **narrowed rather than defended**: it holds for
completions that keep every possible event possible.  The zero class is
declared excluded, on the stated ground that *a completion which
abolishes joint arbitration abolishes the physics it was meant to
normalize.*

This is the corpus's characteristic move, and a new reader should treat
it as the template: **the no-go was not defended, it was narrowed until
true, and the narrowing is on the record with its reason.**

### A6.5 What survives: completions that tilt

Give up demand (c) and completions exist, at every finite depth.  You
build them by working backwards from the far end: pick any positive
numbers at the deepest level, and propagate inwards.  This is a standard
construction (a Doob *h*-transform, for readers who know the term — a
process conditioned on where it is heading).

They work.  They are normalized everywhere, slicing-independent, and
positive.  Their **cost** is exactly what demand (c) forbade: relative
weights get tilted.  Under one natural choice of far-end numbers, 21 of
the 114 interior nows are tilted, **including the very beginning of the
record**.

That last point was, for a long time, the sharp end of the whole
problem.  A distortion buried deep in the interior might be dismissed as
an artefact of stopping the enumeration somewhere.  A distortion at the
*root* is a statement about the theory's beginning.

**The ratios, though, are law.**  Before any completion, two positive
statements hold: relative weights of histories are stable under common
extensions, and the density of the obstruction is exactly quarter-sized
per blind layer.  Any completion must respect both.  So:

> **Ratios are law; absolute probabilities are not.**  The completion
> problem is precisely the problem of getting from a ratio-structure to
> a measure, and the theorem says that step cannot be taken locally.

### A6.6 Quantum mechanics does not rescue this

It is natural to hope that a quantum formulation escapes a classical
obstruction.  **It does not**, and the corpus says so outright.

The lift *appears* to satisfy all three demands: it preserves ratios and
normalizes globally.  But when you look at what it is, it turns out to
**be** the classical construction of §A6.5 at one particular choice of
far-end numbers, wearing Hilbert-space clothing.  The two natural bases
one might use are exactly the two natural classical choices.  Hilbert
space supplies no new resource here.

And its own step-by-step operator — the object that would carry the
completion cut by cut rather than only at the end — faces a three-way
obstruction: make it cut-independent and it reproduces the
arbitration-killing zero class of §A6.4; make it cut-dependent and it
has to read the blind wire; hide the cut dependence in an ancilla and
the classical object comes back wearing a register.

**What the lift does establish** are real results: the internal
randomness of an arbitration lifts exactly; and there is a genuine
*discriminating observable* between two different ontologies of what a
record is — a coherence that is one-sixth under one reading and exactly
zero under the other.  Which one nature uses is empirical; the lift
supplies the instrument, not the verdict.

**And the question has since been asked from the other end, with a
harder answer.**  This section asks what happens when a quantum dress is
*put on* the law; §A2.8 asks what quantum layers the law would *permit*
if one were built, and counts them.  The count says the record demands
permit interference everywhere and organize none of it — and that the
first demand asking the interference to be generated by the law itself
removes all of it.  So the two ends agree: at this scope the quantum
option is not a resource the law supplies to itself.

### A6.7 The escape that worked: a completion with no far end

If the trouble is the imported far-end numbers, the way out is a
completion that has no far end — one defined on the unbounded structure
directly.

The corpus's key move was to stop enumerating records (there are
unboundedly many) and start enumerating **situations**: a bounded
summary of what a record looks like from the point of view of what can
happen next.  In the delivery-free two-actor world, that summary takes
**exactly 36 values**, and the search closes — no situation the search
reaches ever leads outside the 36.  Collapse situations that no
observation can distinguish, and you get **six**.

On six states you can do classical linear algebra.  The answer is
unique: one positive solution, up to scale, and it grows by a factor of
exactly **two** per step of the record.

Then — and this is the part the corpus was slow to do, and says so —
build the resulting object *back on records* and test it against the
actual demands of §A6.2.  It passes: positive, normalized at every now,
gauge-respecting, slicing-independent *directly* (checked across every
slicing of every record at the tested depth, not by the diamond proxy),
support-preserving, and it sums to exactly one over each depth.

**And it is root-free.**  Here is the cleanest symptom of the whole
problem, and its resolution.  The grammar has a **renewal** structure:
the beginning of the record and a certain later point (just after a
dispute has been settled and a fresh base exists) are *structurally
identical* — there is an exact matching of events, types, payloads and
weights.  The law cannot tell them apart.  **But every imported-far-end
completion prices them differently.**  The law has forgotten where it
started; the measure has not.

The canonical completion prices both at exactly one sixteenth — and not
only at that one pair: the *entire* matched subtree of 215 nows carries
identical completed options, event by event, with zero mismatches.

> The completion no longer distinguishes what the law identifies.

**And it is a probability of the record, not of the writing.**  The
demand that a completed law assign one number to a record however that
record is serialized — the demand the *other* stream states as a
condition on any click law at all — is met: the completed measure is
constant on every one of the 5,548 record classes of the family, checked
exhaustively (§A2.7).  Worth saying because it was assumed for years
before it was measured, and because the uncompleted normalized law
**fails** it.

### A6.8 The catch: the shape is a choice, not a law

There is a tempting way to state §A6.7 that is **false**, and it is worth
naming because it is the natural thing to say: *among completions that
respect the law's own identifications, there is exactly one, and it needs
no boundary.*

The measurements say otherwise:

- Demand that a completion price the beginning and the renewal point
  alike, and **308 of 313** directions of freedom remain.
- Demand full respect for indistinguishability at every interior now,
  and **137 of 313** remain.
- Demand the *shape* the corpus had assumed — a function of the
  situation times a fixed factor per step — and you get exactly one
  answer.

**So what delivers uniqueness is the shape, and the shape is a postulate
about the completion, not a principle stated about the record.**

The obvious next question was asked immediately, as its own unit: *is
there a demand statable on the record itself that forces the shape?*
The strongest candidate was "the same transition should have the same
probability regardless of how deep you are".  The prediction, written
down in advance with its argument, was that this *would* force the
shape.

**It does not.**  The space of distinct completions satisfying it has
dimension **12, then 32, then 125** as you go deeper — it *grows*.  And
the obvious rescue is closed off by measurement too: adding
slicing-independence more than doubles the number of constraints and
leaves the answer's dimension **exactly unchanged** at every depth.  The
residual freedom is not gauge freedom.

The diagnosis of why the pre-registered argument failed is worth having,
because it is not a technicality.  The argument needed the demand to
constrain each *individual* option.  But a demand stated on the record
constrains **sums** — the probability of moving from one kind of
situation to another — because that is what is observable.  A
per-option version would be a demand about labels nobody can see, which
is exactly the kind of demand that was disqualified one step earlier.
So the stronger hypothesis the argument needed **is not available as a
record-level demand at all.**

> **Therefore, permanently and at every citation:** the record law
> completes itself **given** that shape.  The shape is a choice.  Nobody
> has an invariance principle that forces it.

**And the choice now carries a second price tag, computed from a
different direction entirely.**  §A2.7 asks what a completion has to do
for the grammar's normalized law to define a probability on records at
all, and then counts the completions that do it: **573** independent
positive directions at the depth where the count is exact, **205** of
which also give a genuine measure on records, **28** of which have the
shape the corpus assumed, one ray of which is the settled completion.
So the demand that turns weights into a record probability leaves the
answer massively underdetermined, and it is the postulated shape — not
the demand — that picks out one.  The settled completion *does* pass the
demand, on all 5,548 record classes of the family; it is simply not
alone in passing it.

### A6.9 The gap closes — at two actors, delivery-free

For a long time everything in §A6.7 rested on **three** unproved
structural assumptions: a short list of facts about what a view can hold,
that the bounded summary determines what can happen next, and that the
summary of the next situation is fixed by this one plus the event.  **All
three are theorems**, in the two-actor delivery-free sub-theory, and both
arguments are short enough to state.

**The own-view dichotomy.**  When the law checks whether an event is
allowed, the view it consults is one of exactly **two** things: the
acting actor's own cone, or the *entire* record.  There is no third case
— and the reason has two halves, which is worth saying because the
obvious one-line version of it is backwards.  The framework keys its
causal order on actor names, and that bookkeeping *by itself* would allow
a **third** kind of view: an event settling a dispute the initiator is
not party to would see the opponent's past plus a sliver of its own.
What removes that case is a second clause — the law only ever offers a
settlement to an actor whose *own* proposal is in the dispute.  Register
geometry produces the third case; the proposer test kills it.  So the
dichotomy is a theorem of the two together, and the proposer test is
precisely the clause that would have to be re-examined for a third actor
or for delivery scope.

That single observation does two jobs.  It explains the lag that had
looked like an obstruction — the situations where an actor "sees more
than its own past" are exactly the two-actor events, all 2,032 of them.
And on the other branch, where an actor sees only its own cone, the law
turns out to be **rigid**: an actor has at most one live version, at most
one live proposal, and the possibilities are so constrained that only two
complementary configurations ever occur — which is why the idle weight is
simply constant.

Put together, the menu becomes an explicit **closed formula** in the
summary, with no depth parameter anywhere in the argument.  The short
list of structural facts about what a view can hold falls out of the same
lemmas, its last clause supplied as a three-line proof.  So the bounded
summary determines the menu at every depth.

**The update table.**  The other half is that the summary of the *next*
situation is fixed by the summary of this one plus the event.  That is
written out — not checked, *written out* — and it takes **five rows**,
because at two actors there are exactly five things an event can be:

1. **an idle** — nothing in the summary moves at all;
2. **a proposal against a version the summary still records** — one live
   proposal is added, and nothing else changes;
3. **a proposal against a version the summary has *discarded*** — the
   interesting row, and the one that looks impossible at first sight;
4. **a settlement by one actor of its own uncontested proposal**;
5. **a settlement of a genuine two-actor dispute.**

Each row is a short proof read directly off the framework's own source,
using the rigidity facts above; not one of them mentions the depth of the
record, and not one of them looks at the history.

Row 3 is where the work is.  The summary deliberately forgets versions
that have been superseded — that is what makes it bounded.  But an actor
can propose against a version *it* still believes alive because it has not
seen the settlement that retired it — the same invisible supersession of
chapter A3.  So the successor summary must mention a version the parent
summary does not record.  The row survives because that version is
**forced**: at two actors at most one such discarded version can exist, so
there is nothing to choose, and its "already superseded" mark is
*computed* from that fact rather than looked up.  The table never has to
recall something it dropped.  Two further obligations are discharged the
same way: a freshly minted version name can never collide with one
already present (a collision would mean the settling actor had settled
that same version before, which would have made this settlement illegal),
and the incomparability fact that decides which proposals conflict is a
theorem rather than something the summary would have to carry.

> **So: the bounded summary determines both the menu and its own
> successor, at every depth.**  The measure problem's core question — the
> oldest named gap in the programme — is **CLOSED** in this sub-theory.

**Two things fall out of the table that no sweep could have done better
than observe.**  The first: **who wins a dispute is invisible to the
summary.**  A
settlement's winning set enters only through the name of the version it
mints, and the table replaces that name with "one fresh version" — so the
next situation does not depend on the winner at all.  (The weights do; the
situation does not.)  The second is better: **every two-actor settlement
returns the record to the root situation exactly.**  Both actors end up
holding the same fresh version with nothing live and nothing pending —
which is, letter for letter, the summary of the empty record.  The
renewal structure that §A6.7's root-freeness rests on is therefore a *row
of the table*, derived, rather than a coincidence somebody measured.

**The evidence base, stated as it stands.**  An independent
re-implementation — written from the prose of the argument alone, with a
different internal representation and sharing no code with the original —
reproduces the table's prediction against the framework's own answer on
**4,778,310 transitions of records nine events deep, with zero
mismatches**, landing on the same 36 situations and the same 176 abstract
transitions; and the renaming the summary uses is *unique* on every one
of those records.  None of that is a premise of the argument.  The proof
is the five rows; the sweep is what would have caught a mistake in them.

A pleasing side-effect: the quarter-structure of chapter A2, which had
been a *measured* regularity, drops out of the closed formula as a
consequence — one actor's options weigh either exactly one or exactly
one-and-a-quarter, and the two actors are at a quarter over together or
neither is, so the table totals are two or two-and-a-half and nothing in
between.

**Four things this does not do.**  It does not make the shape of the
completion any less of a choice — §A6.8 stands entirely, and closing this
gap closes the *closure* question, not the selection of the shape.  It
does not reach delivery scope, where the geometry lives.  **It does not
reach three actors**: with a third actor the third view case becomes
genuinely available, and the dichotomy is the one thing that breaks — the
rest of the rigidity survives, which is what tells a successor unit where
to aim.  And the argument is prose reasoning checked against the code, not
machine-verified logic — a formal mechanization is the line's one
remaining residue.

At delivery scope — where chapters A5, A7 and A8 live — **the whole
question remains open**, and chapter A9 explains why the method that
settled it cannot travel.

Also, the specific numbers (the factor of two, the six weights) are
**toy-relative**.  A second grammar was tested and has no such state
chain at all.  What is claimed to generalize is the *form* — a unique
completion of this type — never the numbers.

> **What this chapter does NOT claim.**  That "the record law is
> forward-complete" full stop — only with the form; §A6.9 closes a
> different gap and leaves that one exactly where it was.  That "the
> measure problem is closed" anywhere but in the two-actor delivery-free
> sub-theory: at three actors and at delivery scope the question is
> untouched, and the sentence may never be quoted without that clause.
> That the tilt is
> physical: the tilt has been *characterized* exactly (each option is
> re-weighted by how much record-growth capacity the state it leads to
> has, and by nothing else), which converts a vague worry into one
> named principle to be judged — but judging it is open.  That the
> canonical completion is "better" by tilt count: it tilts 50 of 114
> nows, more than one canonical alternative (21) and fewer than the
> other (103); the count is not a figure of merit.

---

## A7. Buying dimension with actors

*Technical twin: Part B, chapter B7.*

### A7.1 The instrument that had to be abandoned

For a long time the natural handle on "how many dimensions does this
record have?" was a counting notion: how many independent orderings do
you need to reconstruct the causal order?  Two, for the flat
one-space-dimension case.  So climb: two, three, four…

**The author's own observation killed this, and it is binding doctrine
in the corpus:**

> *"3+1 spacetime is not four clocks; it is infinitely many."*

The mathematics behind that is exact.  Requiring exactly two orderings
does correspond precisely to one space dimension — that much is a
theorem.  But **any** spacetime with two or more space dimensions has a
*round* light cone, and a round cone contains obstructions of every
size, so its causal order needs **infinitely many** orderings.  Two is
special; three, four and five are *not* the next rungs of a ladder that
ends at our world.  Worse, there exist orders needing three orderings
that fit in no spacetime at all.

So the counting notion is a **detector for escaping one space dimension,
and a grading of clock complexity — never an estimator of the dimension
of spacetime.**

What that looks like from inside is instructive.  A serious attempt was
made to measure whether "wide" records — the ones capable of higher
counting-dimension — are *typical* under the theory's own weights.  Its
headline claim collapsed under review for three separate reasons: the
claim as stated could not have failed (the quantity was monotone in
depth by construction); it silently switched normalizations halfway; and
its central proxy counted an actor as "involved" merely for *idling*,
while roughly half of all weight is idle.  On honest proxies the
headline number fell from 0.98 to 0.67 to 0.41.  And the *discriminating*
comparisons pointed the other way: at fixed depth, the mass on full
width **falls** steadily as you add actors.

The corrected reading — much weaker than what was first announced — is
that what is typical-in-the-making is *escaping* one space dimension,
not unbounded complexity.

### A7.2 The replacement: stop counting, start constructing

The reframe is chapter A5's: forget counting orderings, look at the
**shape of the sky**.

And now the ladder is genuine, because it is the classical
**dimension-versus-shattering** ladder, and every rung of it was
constructed by the corpus in exact arithmetic rather than cited:

| shadows of… | shatter at most | costs at least |
|---|---|---|
| arcs on a circle (one space dimension of sky) | **3** | 3 actors |
| caps on a 2-sphere (our sky) | **4** | 6 actors |
| caps on a 3-sphere (one more dimension) | **5** | 10 actors |

Two things make this a *meter* rather than a mere obstruction test.
First, the top row is genuinely capped: caps on a sphere shatter four
and **never five** — certified by an exact algebraic dependency among
five rational points on the sphere that blocks one particular pair from
ever being cut off.  Second, the ladder continues upward without limit
in principle: shadows of half-spaces in *d* dimensions shatter *d+1*.

So "the largest set of directions these shadows can fully resolve" is a
number with a dimensional meaning: 3 is circle-compatible, 4 is sphere,
5 is beyond the sphere.  Every rung of that table is exact for
continuous shapes — **and §A5.7 shows the discrete test reproduces the
same ladder on genuine sprinkled records of real spacetime**, two space
dimensions reading 3 and three space dimensions reading 4, with the
predicted halt at 5.

So the meter has two calibrated uses, and both are live.  **On
sprinklings at sufficient density it reads geometry.**  And on the
framework's own constructed records — chapter A8 — it reads something
else: those records reach 5, above every sprinkling of any dimension
tested.  The number that separates them is not a dimension the
constructed records "have"; it is the amount of coordination their
worldlines achieve, and no random scattering of points achieves it.

### A7.3 The theorem: dimension has a price, paid in actors

This is the central structural result of the geometry line, and it is
**unconditional at delivery scope** — no measure, no completion, no
unproved lemma.

The argument is three steps and each is short.

1. **Two events sharing an actor are always comparable.**  This is not
   an assumption; it follows from how the framework builds causal order
   — every event carries its initiator, and events sharing a register
   are chained.  (It was also swept over 218,795 pairs with zero
   violations, and independently re-verified in the review at 226,223
   pairs.  The sweep corroborates a proved step.)
2. **Therefore one actor's worldline contributes a nested family of
   shadows.**  Assign each event to its initiator; by step 1, one
   actor's events are in a single line; so their pasts are nested; so
   the shadows they cast are nested — a *chain*.  So the whole shadow
   family of a record with *k* actors is covered by at most *k* nested
   families.
3. **Realizing all combinations of m directions needs many nested
   families.**  A nested family can contain at most one member of any
   collection of mutually incomparable sets.  The middle layer of the
   lattice of subsets is exactly such a collection, and its size is the
   central binomial coefficient — 6 for four directions, 10 for five.

> **Therefore: shattering four directions costs at least six actors;
> shattering *k* costs at least the middle binomial coefficient — 6,
> 10, 20, …**

In plain language: **a rich sky is parallelism, never history.**  You
cannot buy a complicated sky by running the record longer.  You can only
buy it by having more actors.  That is why chapter A5's measured "depth
cannot buy what only width can" is not an accident of the fixture: it is
this theorem showing through.

### A7.4 The infinite-clocks doctrine: derived, but not the way it was first claimed

The first announcement of §A7.3 went one step further and said: *a
sphere-like sky shatters at every size, so it needs unboundedly many
actors — the author's infinite-clocks doctrine is now a theorem.*

**That was refuted by the review, and the refutation is elegant.**  The
implication is valid; the antecedent is empty.  **No 2-sphere sky
shatters at every size** — a sphere sky shatters four and never five, as
§A7.2 says.  So the argument never fires on the object it was aimed at.

**And the conclusion was then rescued by a better route, with no
shattering anywhere in the derivation.**  Just *count shadows*.  A sphere
sky on *n* directions realizes on the order of *n*-cubed distinct
shadows.  One actor's nested family holds at most *n+1* of them.
Therefore the number of actors must grow at least like *n*-squared —
without bound.

> **A sky rich enough to be a 2-sphere requires unboundedly many actors.
> By counting, not by the combinatorial theorem the first version used.**

### A7.5 What width actually prices

The same review supplied the sharpening that keeps this honest.

Do the shadow count for a **circle** sky: on *n* directions it realizes
about *n*-squared shadows, so it needs on the order of *n* actors —
**also unbounded**.

> **Width prices SKY SIZE, not dimension.**

The *dimensional* signal in the theorem is not the growth rate.  It is
the **offset**: arcs shatter 3 and cost at least 3 actors; caps on the
sphere shatter 4 and cost at least 6; caps on the 3-sphere shatter 5 and
cost at least 10.  Three versus six versus ten — a factor, not a
divergence.

This is a good illustration of how the corpus's review culture changes
statements: nothing computed was wrong, and the headline still stands,
but what the headline *means* changed materially, and the change was
made by someone attacking it.

> **What this chapter does NOT claim.**  That the record's counting
> dimension says anything about spacetime dimension (the doctrine
> forbids it).  That shattering four directions rules *in* the sphere —
> it rules *out* the circle.  That the price is tight: the theorem says
> six actors are necessary for shatter-four; chapter A8's construction
> spends twenty, and closing that gap is open.

---

## A8. Building the witnesses

*Technical twin: Part B, chapter B8.*

### A8.1 Necessity is not sufficiency

Chapter A7 says a rich sky is *expensive*.  It says nothing about
whether the price is *payable* — whether the framework's rules actually
admit a record that spends six actors and gets a shattered four-set.
That is a construction problem, and the corpus attacked it by committing
a blueprint in advance rather than searching blindly.

### A8.2 The failure that taught the architecture

The pre-registered blueprint used nine actors: one to mint a fresh
version, four to hold the four directions, four to accumulate the
combinations by receiving deliveries in different orders.

It was **fully legal** — thirty-one events, every one of them offered by
the framework's own menu — and it produced **only eight of the sixteen**
required combinations.

The reason is chapter A3's two-way join.  When an accumulator receives
from a direction-actor, the *sender's* line also absorbs the receiver's
accumulated past.  So the second time that direction-actor sends
anything, it carries contamination, and the supposedly independent
channels collapse onto one.  In fact — and this is the pleasing part —
the collapse is **the theorem of chapter A7 biting its own
construction**: the per-sender shadows form a nested family, exactly as
the theorem demands.

The failure is kept as a gated exhibit, not discarded.

### A8.3 Couriers

The fix is a supply-chain fix.  **Sending into an empty receiver folds
nothing back** — a fresh actor has no accumulated past to contaminate
the sender with.  So each direction-actor mints a fresh, single-use
messenger — a **courier** — for every step where it would otherwise
contaminate itself, and each courier performs exactly one delivery.

With eleven couriers, the construction works:

> **A 20-actor, 42-event record — every event selected from the
> framework's own menu — whose sky has four mutually incomparable
> directions, sixteen distinct shadows including the empty one, realizes
> **all sixteen** combinations, and therefore shatters a four-set.  It
> does so at three different heights, not one.**

Consistency was checked: the shadows do decompose into per-actor nested
families with no crossings, and the realized family's minimum nested
cover is **exactly six** — the theorem's bound, tight.  So the gap
between six and twenty is **architectural**: it is the scheduling cost of
working around backflow, not slack in the family.

### A8.4 One rung higher: the meter reads five

The natural next question — and the sharp one — is whether the framework
can go *past* the sphere.  A mechanical generalization of the courier
recipe, driven by the standard decomposition of the subset lattice into
nested families, was built.  It first reproduced the four-direction
result as an anchor, then delivered:

> **A 42-actor, 84-event record (ten accumulator chains, twenty-six
> couriers), every event menu-selected, realizing **all thirty-two**
> combinations of five directions and shattering a five-set — at three
> heights.**

The independent reviewer rebuilt this record from scratch using the
*full* menus at every one of the 84 steps and found the record was
**forced**: at every step exactly one option matched the specification.
The realized family's minimum nested cover is exactly ten — the
theorem's bound again, tight.

And the calibration is exact on both sides: the four-direction shadow
family **is** realizable by caps on a 2-sphere (sixteen explicit
rational certificates), no five points ever shatter on a 2-sphere
(certified twice, on two different configurations), and the
five-direction family **is** realizable by caps on a 3-sphere
(thirty-two explicit certificates).

> **The meter's scale is concrete: this record's sky fits a 3-sphere and
> provably not a 2-sphere.**

### A8.5 What this licenses — carefully

Here the corpus made the *same mistake twice in two days*, and the
second time it was caught by the reviewer of the second unit, one rung
up from where the first reviewer had caught it.

The tempting sentence is: *"not realizable by caps on the sphere,
therefore not a 3+1 sky, therefore the framework does not select 3+1."*
The second arrow needs the assumption that discrete 3+1 skies **are**
cap systems — and that is exactly the class of assumption chapter A5's
demotion refuted, where the majority of genuine 2+1 skies turned out not
to be arc systems.

So the licensed claim is a **capacity** claim:

> **The admissibility layer does not CAP the shatter ladder at the
> sphere's rung.**  Whatever might prefer 3+1, it is not in the rules
> about what may happen.  Selection, if it exists anywhere, lives
> elsewhere — the candidates being a measure, a resource cost, or a
> counting-typicality argument.

**Where these records sit against real spacetime.**  §A5.7's ladder puts
genuine sprinkled records at 3 in two space dimensions and 4 in three,
with five never reached by either.  These constructed records reach
**five** — above every sprinkling of any dimension tested, and above the
rung the sphere's own geometry permits.

That is the whole of the capacity claim, and it is worth saying exactly
what it does and does not mean.  It means the framework's rules admit
coordination that random causal structure never produces, at a level the
2-sphere cannot host.  It does **not** mean the record "is" four space
dimensions: the meter reads a record's coordination, and only on
*sprinklings* does coordination coincide with dimension.

**And the meter is a property of a (record, reading) pair, not of a
record.**  The same 42-actor record reads 1 through 5 under one sky
reading depending on the height chosen, and differently under the
others.  Its value is the largest over the committed readings: five.

> **What the shatter constructions do NOT claim.**  Any positive 3+1
> claim.  Any statement about typical records — one engineered record per
> rung, no genericity, and genericity is *not even posable* at delivery
> scope (chapter A9).  Anything for six directions or beyond: the builder
> visibly generalizes and has not been run, and unrun is unclaimed.

### A8.6 The crystal: a record that tiles

The constructions so far were built to do one thing — spend actors to buy
a rich sky at a single event.  They are spikes.  Nothing about them
resembles a *space*, and the instrument that says so is straightforward:
ask what fraction of a record's events carry a usable local chart at all,
and how much neighbouring charts overlap.  Measured that way, the courier
records are the **opposite of an atlas**: about a third of their events
are charted, against roughly two-thirds to four-fifths for genuine
sprinkled spacetime records.

So the natural question — and it is the one that matters for the
destination — is whether the framework can build the other kind of thing.
Not a spike: a **tiling**.

**It can.**  The construction is a brick wall.  Eight actors in a ring;
one version minted and broadcast to all of them; then rounds of
alternating re-deliveries — evens to odds, odds to evens — which is
exactly the brick lattice of one-space-dimension spacetime worn as a
record.  Sixty-five events, every one of them offered by the framework's
own menu, and **every specification matched by exactly one candidate**:
the record is *forced*, nothing was chosen by tie-break.

Measured against genuine sprinkled records:

- **Homogeneity — inside the sprinkling band.**  77% of the brick's
  events carry a chart, against a band of 64% to 80% across eleven
  genuine sprinkling configurations.  Not above the band; **inside** it.
- **Overlap — above every sprinkling comparator.**  Neighbouring charts
  share 0.65 of their content, against 0.05 to 0.13 for the sprinklings.
- **Width — at the floor.**  No chart anywhere in the brick has four or
  more directions, at any parameter setting tried, against 42%–65% of
  events for the sprinklings.  The tiling is **thin**.

The width shortfall is a statement about the shallower of two chart
depths.  At the deeper one the brick does reach four-direction charts —
at 58% of its events, which is *just below* the corresponding sprinkling
band rather than inside it.  But at the depth where the comparison is
cleanest, the brick tiles and does not spread.

**And the headline number is not a property of the mechanism.**
Homogeneity rises without bound as the re-delivery circuit runs longer
(0.44 at four rounds, 0.77 at fourteen, 0.93 at fifty) and falls as the
ring widens.  Strip the record's non-lattice prefix and its top and
bottom layers and the interior reads 0.90.  So:

> **The shortfall from a perfect tiling is entirely BOUNDARY.**  A
> re-delivery circuit's homogeneity tends to one as it runs.  The
> published figure is a snapshot of one setting.

**What this licenses, and what it does not.**  It licenses a *mechanism*:
the framework's rules admit records that tile at sprinkling-grade
homogeneity with above-sprinkling overlap and thin charts.  It licenses
no claim that the brick *is* a spacetime, no claim about typical records,
and — under the standing scale doctrine — no claim about any object at
this size.

### A8.7 The wide crystal, and the wall behind it

The two mechanisms the programme certifies separately are **width**
(§§A8.3–A8.4's couriers: rich skies, no tiling) and **tiling** (§A8.6:
charted everywhere, thin skies).  The obvious question is whether one
record can do both.

**It can.**  Take two rings of eight actors, each running the brick
circuit of §A8.6, and couple them: after every round, each actor of one
ring delivers across to the other.  Sweep the coupling and the ring size
and the number of rounds — thirty-eight settings in all — and fourteen of
them land inside the sprinkling homogeneity band *and* carry
four-direction charts.  The best of them is a **177-event, sixteen-actor
double ring**, forced like the brick: at every one of its 177 steps the
whole menu is offered, up to 528 options at a time, and every step matches
exactly one of them.  It tiles at 80% homogeneity and a third of its
events carry a four-direction chart, where the uncoupled brick carries
none.

**The depth label is part of the claim, and it is load-bearing.**  This is
a statement about the *shallow* chart depth.  Go one level deeper and the
pattern is met by eleven of the thirty-eight settings, four of which have
no coupling at all — including the plain uncoupled brick.  So what is new
is not "tiling and width can coexist" in general; it is that they coexist
at the depth where no uncoupled record manages it.

**Two honest shapes in the sweep.**  Coupling is *not* monotone: one
coupled position is **worse than none** — homogeneity dips sharply at a
single courier or a single coupled pair and only recovers from two
upward.  The measured reason is that partial coupling desynchronises the
record's layer structure: the uncoupled ring runs 27 clean layers,
partial coupling stretches it to 36 ragged ones, and full coupling gives
37 layers with a perfectly regular tail.  And the recovery is
**family-specific** — the double rings peak at *complete* coupling while
the courier-augmented bricks peak at *partial* coupling, their complete
settings being the worst points in their own family.  Nothing here is a
single mechanism with a single dial.

**And one limit reported against the unit's own interest.**  Strip a
record's top and bottom layers, as §A8.6 does, and the width *rises* at
every one of the fourteen — so the width belongs to the circuit and not
to the record's edges.  But homogeneity rises too, and **ten of the
fourteen interiors rise straight out of the top of the band**.  So the
durable half of the result is the width; "inside the band" is a statement
about finite records with ends.

**Then the ceiling, which is a theorem rather than a measurement.**  How
wide can a chart get?  Count the wires an event touches.  Every step of
the record moves along one of them, so from any event you can reach at
most *B* events one level up, at most *B²* two levels up, and so on:

> **A chart at depth *d* has at most *B^d* directions, where *B* is the
> largest number of wires any single event touches.**

A delivery touches exactly two wires — sender and receiver.  So a record
made of deliveries can never carry more than **four** directions in a
shallow chart, no matter how it is built.  Genuine sprinkled spacetime
records carry ten to seventeen.  **That gap is not a construction problem;
it is unreachable by transport at all.**

The theorem also says where the next width must come from.  The grammar
has precisely one kind of event that touches three or more wires: the
**settlement of a dispute among several proposers**.  So:

> **Chart width past four is bought with conflict, not with delivery.**
> That is a necessity, not a recipe: it says where to look, and it does
> not say that looking there works.

It also says slightly less than it appears to.  Counting *wires touched*
overcounts, because one of a settlement's wires is a wire that is **born
there and never used again** — and a wire nothing travels along afterwards
carries no direction.  The corrected count is the number of wires that
**carry on**, which for a settlement is the number of **proposers**
disputing.  A settlement between two proposers is therefore no wider than
a delivery, three wires or not; the necessary condition is not "three
or more wires" but **three or more proposers**.  §A8.9 proves that and
builds the records.

The successor is therefore sharp and named: **a crystal made of
conflicts** rather than of deliveries.  It has been built, and it is the
next section.

### A8.8 The transitions between charts, and the atlas that trivializes

A tiling of charts is not yet a space.  What makes an atlas an atlas is
what happens where two charts **overlap**: the rule for translating one
chart's coordinates into the other's.  In ordinary geometry those
translation rules are where all the structure lives — they are what
carries curvature, what tensors transform under, what a "gauge field"
*is*.  Every atlas statement in this programme up to here quietly assumed
those rules were the identity.  On the wide crystal they can be measured,
and they have been.

**How to label a direction.**  A chart at an event is a set of directions
leading away from it.  Give each direction a name that the record itself
supplies: the sequence of wires a step-by-step path along that direction
uses.  Two overlapping charts then name the same direction in two ways,
and comparing the names *is* the transition rule.  This is a reading of
the framework's own generating relation, not a new structure laid on top
of it, and the receipt proves that the relation it reads generates
exactly the committed causal order before it measures anything.

**What comes back, in three steps, of which the third reverses the first
two.**

> **Step one: the rules are not the identity.**  Of the 172 overlapping
> chart pairs of the 177-event double ring, 115 translate non-trivially.
> On the pairs of *widest* charts — the four-direction ones, the ones the
> width mechanism bought — the split is 29 identity to 108 non-identity.
>
> **Step two: they are consistent.**  Go around any triangle of
> overlapping charts, composing the translations, and you come back where
> you started.  All 111 testable triangles, zero failures — and zero
> failures anywhere in the whole census, controls included.  Consistency
> around loops is exactly the condition an atlas has to satisfy to be an
> atlas at all, and it holds.
>
> **Step three, and it is the result: the whole thing is a relabelling.**
> Each chart in this record has a free binary choice built into it — which
> of a delivery's two wires is called "the first one".  Choose that flag
> per chart, correctly, and **every one of the 108 non-trivial
> translations becomes the identity.**  There is an explicit choice (32
> charts one way, 28 the other) that does it, with **zero obstructions**;
> going around loops was never going to detect anything, because there
> was nothing to detect.  The only survivors are the seven
> correspondences that change the *length* of a name, and those are not
> translations of one chart into another at all.

> **So: the atlas is globally trivializable.  There is no gauge
> structure.**  The transitions are real in the sense that they are not
> the identity as first written, and empty in the sense that a change of
> convention removes all of them at once.  The tensor-and-curvature
> programme starts at **zero** on records made of deliveries.

**This is a negative, and it is worth as much as a positive would have
been**, because it converts a vague hope into a sharp question.  Before
the measurement, "do the charts glue non-trivially?" had no answer and no
test.  Now the test exists and it is one number: the count of
obstructions.  The transition census behind it ran on five substrates —
the wide crystal, two uncoupled controls, and two genuine sprinkled
spacetime records — and the triviality test itself on the three the
grammar builds, where it is zero everywhere.  (On the two controls it is
zero for a reason worth knowing: their overlapping charts come in
disjoint pairs, so there are no loops to obstruct.)

**Three things the measurement refuses to say**, each of which the first
reading of it said and had to withdraw:

- **The translations do not name a group.**  Each non-trivial one is
  defined on only half of the directions it could act on, so calling it
  "an element of"
  any particular group requires extending it, and the extension is not
  unique — ten different groups are equally consistent with everything
  measured, and two of them are minimal in incomparable ways.  What is
  measured is that non-identity translations *exist* and *agree with each
  other*.
- **The contrast between the crystal and the controls is a convention,
  not a mechanism.**  Under one labelling the crystal's translations and
  the controls' translations look like different operations; under two
  others they do not, and the controls turn out to have no overlapping
  triples at all, so there is nothing there to compare with.
- **The crystal's identity pairs are duplicate charts, not flat pieces.**
  Two charts translate by the identity exactly when they contain the same
  directions — 172 of 172, both ways.  That is a bookkeeping fact about
  this record, and it fails at the deeper chart depth.

**What survives is an instrument and a question.**  The instrument is a
validated transition detector with the triviality test built in, which is
the piece the first version was missing; it caught a real bug in its own
first run, and it refuses to read an outcome off a labelling that forces
the answer.  The question is the one nobody had before:

> **Can any record at all carry a transition class that is *not* a
> relabelling?**

And there was a reason — a reason, not a promise — to look for it in
records made of **conflicts**.  What makes the relabelling available here
is that a delivery has exactly two wires and nothing distinguishes them,
so "which is first" is free at every chart.  A settlement among several
proposers has no such symmetry.  §A8.9 goes and looks, on the first
substrate where the symmetry is genuinely broken, and the answer there is
**no as well**.

> **What this chapter does NOT claim.**  That the wide crystal *is* a
> spacetime, or that it is typical — one engineered family, no genericity,
> and genericity is not posable here at all (chapter A9).  That the width
> ceiling is a limit of the framework: it is a limit of **delivery
> circuits**, and the theorem names the exit — which §A8.9 then walks.
> That the atlas carries a gauge structure of any size: it carries none,
> and the sentence is on the standing blacklist (§0.3).  That the
> triviality is a *theorem* about the grammar — it is a measurement, on
> substrates at chart depths under conventions that have been varied and
> agree, which is a strong measurement and not a proof.  **And that it is
> a statement about the theory rather than about the instrument**: the
> whole verdict is read off charts over records, and §A2.9 measures a
> different loop — probability transport itself — which the chart
> instrument provably cannot see and which is **not** trivial.

### A8.9 The crystal made of conflicts, and the width ceiling it reaches at every size

Three separate results — the width wall of §A8.7, the trivial gluing of
§A8.8, and the one place the law fails to be a probability of the record
(§A2.7) — all point at the same object: a record whose engine is
**disputes being settled** rather than **messages being delivered**.  It
is built here, and it is the most consequential geometry result the
programme has.

**First, the supply problem — which was expected to be the hard part.**
A delivery can be repeated forever: the same message can be sent again
next round.  A settlement **consumes** its dispute.  So a record that
runs on conflict has to *manufacture a new disagreement every round*, and
the expectation written down in advance was that it could not — that
conflict records would run for a few rounds and then have nothing left to
arbitrate.

That expectation was half wrong, and the half that was wrong is the
important half.  The framework hands over most of the answer for free:
when a dispute is settled, **every disputant receives the settled
version**, not only the one who settled it.  So the same group of actors,
having just fought over a value, all hold the same new value and can
immediately disagree about that.  A pair that quarrels together needs no
message to quarrel again.  What costs a message is **changing partners** —
and a record that never changes partners needs no messages at all.

> **Conflict tiles.**  Twenty-one three-way conflict configurations, over
> two thousand events, and eleven four-way ones, another fourteen hundred,
> run to full crystal length with **zero refusals**: every single event
> offered by the framework's own menu, and matched by exactly one option
> in it.  Records made of disputes are as forced, and as sustainable, as
> records made of messages.

**Second, and this corrects the ceiling itself.**  §A8.7's bound counts
the wires an event touches.  A settlement touches the disputants' wires
*plus one more*: the wire of the freshly minted version it creates.  It
looks like a three-wire event even when only two actors are disputing.

That third wire is a **dead wire**.  Nothing ever travels along it again,
and here is why, in four steps.  A version's own wire is occupied only at
the event that *creates* it; when that version is later delivered to
somebody, it rides in the message's *contents*, not on its own wire.  So
for the wire to be used twice, two different settlements would have to
mint the *same* version name — same base, same winner, same author, same
initiator.  Two such settlements would share a disputant's wire, and
anything sharing a wire in this framework is causally ordered.  So one
would come after the other; the later one would already see the earlier
settlement; and its own admissibility rule refuses to settle a dispute
whose base has already been superseded.  It cannot happen.

> **So the number that bounds a chart's width is not the wires an event
> touches; it is the wires that *carry on* — and for a settlement, that
> is exactly the number of disputants.**  A two-proposer conflict ring is
> therefore held to **four**, exactly like a delivery circuit, three
> wires or not.  "Three or more wires" was necessary and **not
> sufficient**; what buys width is **three or more proposers**.

**Third: the object.**  Give three actors a dispute; that is a start, and
a ring or a grid of such disputes carries six directions where a delivery
circuit carries four.  But the record that matters puts each actor in
**two disputes at once** — one along a row, one along a column — running
concurrently, so that each dispute's outcome immediately feeds two further
disputes rather than two messages:

> **THE DOUBLE GRID.**  Rows and columns quarrelling at the same time.
> **No messages at all** inside its rounds.  A fixed share of everything
> that happens in it is a settlement — a quarter with three disputants to
> a quarrel, a fifth with four.  And its charts carry **as many
> directions as the ceiling allows**: with three disputants, three
> successors each themselves three-way disputes, three times three —
> **nine**; with four, four times four — **sixteen**.  Every one of those
> directions was read out of the framework's own committed geometry,
> event by event, not counted by a summary statistic.

Sixteen, against a delivery circuit's four — and inside the ten to
seventeen that genuine sprinkled spacetime records of the same size
carry, from pure interaction with nothing delivered.  Two things
have to be said in the same breath, and they are said wherever this
comparison appears.  **The sprinkling range is two ranges wearing one
name:** the 2+1 records carry ten or eleven, the 3+1 records fourteen to
seventeen, so sixteen sits inside the 3+1 group and *outside* the 2+1
one.  And **the widest chart is the only statistic on which the record
touches the sprinklings at all**: its typical chart is far thinner than
theirs.  What is claimed is about the maximum, and it is a *parameter
picked* rather than a coincidence discovered — because five disputants
give twenty-five and six give thirty-six, above the whole sprinkling
range.

**And that is the ladder, which is the section's most general result.**
The ceiling is *k* times *k* for a *k*-way dispute, and it is **reached
at every size anyone has built: nine, sixteen, twenty-five,
thirty-six.**  What makes the difference between reaching it and falling
short is not the size of the quarrel but a **scheduling** matter, and the
framework supplies the fix out of its own vocabulary:

> **HEIGHT-LEVELLING.**  A chart at depth two counts what sits exactly
> two layers on from the event.  So a settlement collects its successor's
> own directions only if that successor sits **one** layer on; a
> successor that sits two layers on contributes only itself.  That
> much is definition, not discovery.  What is *discovered* is twofold.
> **The order in which quarrels are settled decides which successors
> land where** — reorder the settlements inside a round, change nothing
> else at all, and the sixteen-direction chart collapses to seven.  And
> **a schedule can always be arranged to meet the condition**: padding
> the bootstrap with the framework's own *idle* event — the do-nothing
> step it already uses to end records — lifts every straggler into line,
> and does so at three, four, five and six disputants alike.  Nothing
> else changes: no new actor, no message, no extra quarrel.

**Fourth, and it answers the previous section's own leftover question.**
§A8.7 could tile and could spread, but the tiling and the spreading were
in tension: across the whole swept family, the wide records were not
uniform and the uniform records were not wide.  The double grid is
**both** — and at four disputants, where the wider chart makes the
uniformity harder to hold, it is both on a **whole record and on both
of the two ways of measuring uniformity**.  Run the four-way grid one
round longer than the first sweep afforded — two hundred events, still
forced, still with no messages inside its rounds — and it sits inside the
band genuine sprinkled records occupy, on *both* band columns, while
carrying its sixteen-direction charts.  The three-way record manages one
column of the two.

> **THERE IS NO WIDTH-UNIFORMITY FRONTIER.**  It was natural to expect
> that width would be bought with uniformity — that a record wide enough
> to look like spacetime would be too lumpy to tile like it.  At three
> disputants the two compose; at four they compose on the whole record as
> well, and on the stricter reading too.  **No such frontier exists at
> any size that has been built.**

The honest form of that is a **crossing**, not a match, and the
difference matters.  Uniformity in this family rises steadily with the
number of rounds, and the sprinkling band is an interval — so a family
that rises through it is *inside* it at some round number and outside at
others.  The whole record enters the band at the fourth round; the
record's *interior* — the same events with the boundary layers dropped —
is inside at the second round and above the band by the third.  So *"in
band"* names a round number as much as it names an object, and the
lasting statement is the one about composition: **at the round where it
happens, it happens at full width.**  The interior figure carries one
further caution, stated once here and honoured throughout: dropping the
boundary layers gives a *sub-population of events*, not a smaller
record — the charts are still computed on the whole thing — so it is a
conditional average and never an object.

**And the mechanism, which is the part worth remembering.**  It is
tempting to credit the width to the messages, because a message-free
conflict record *can* collapse to a line — it does exactly that when each
actor has only **one** running dispute, since then its cycle is a chain of
diamonds, propose-propose-settle-propose-propose, and a diamond has no
width.  But the collapse belongs to the *single dispute*, not to the
absent message.  Give the same actors a second dispute running alongside
the first and the messages are still absent, the settlement share is
unchanged at its fixed value, and the width comes back ninefold — sixteenfold
when the quarrels are four-way.

> **What a crystal needs for a second direction is a second thing
> consuming an actor's wire, concurrently.**  A message is one way to buy
> that, and it costs a message.  **A second concurrent dispute is
> another, it is free, and it is better** — because a message forks two
> ways and a *k*-way dispute forks *k*.  **Crossed conflict alone
> generates both the uniformity and the width.**  Transport is still
> needed to *seed* the disputes and to *rotate* partners; it is not needed
> to make space.  And crossing the quarrels is not even the only way to
> meet the condition: the levelled chains, which have no crossing in them
> at all, reach the same ceiling at every size.  **What is load-bearing is
> the height condition; crossing and levelling are two ways of meeting
> it.**

**Fifth: still no gauge.**  The whole point of looking at conflict, on the
gluing side, was that a settlement among several proposers has no
free two-way symmetry to relabel away — so a conflict atlas was the first
place a genuine structure could live.  It does not.  Run §A8.8's
triviality test on the wide conflict records — including **both** of the
sixteen-direction ones, the widest substrates the programme has — at
**five** different conventions for how a settlement's wires are ordered,
and at every one of them the obstruction count is **zero**, as it is
under a free choice of labelling, which is the largest re-labelling
freedom there is.

> **The answer to §A8.8's question is negative on the first substrate
> that could have answered it positively.**  Conflict bought width and
> bought no gauge.  Three substrate families have now been tested —
> delivery, conflict, and crossed conflict — and every one of them glues
> trivially at every convention tried.

There is one exception-shaped thing in the data and it is honestly
reported rather than promoted.  A non-zero count does appear — on the
*narrow* two-way conflict rings when the number of quarrelling pairs per
round is **odd**, where the size of the count turns out to be a count of
*rounds* rather than a property of the ring; and, under **one** of the
five conventions, the one that orders a settlement's wires by who won and
who lost, on the double grid as well.  That last was the obvious place to
look for a real structure, and the sweep that looked settles it the
disappointing way: it fires at three disputants exactly as at four, so it
is a property of **the schedule and that one convention**, not of the
size of the quarrel.  A free choice of labelling removes every one of
these counts, there are no loops for them to live on, and genuine
sprinkled records produce such counts too.  They are filed, not claimed.

**And the third motivation, which is left where it was.**  The measure
defect of §A2.7 — the menu total jumping from two to two-and-a-half when a
hidden conflict becomes visible — is a statement about the *two-actor,
message-free* sub-theory.  These records are neither.  What can be
measured here is the analogous quantity: how far a record's total menu
mass rises above the number of actors, which is non-zero exactly where an
unsettled dispute is visible.  It does, and the excess is counted.  But it
is a different quantity at a different scope, the two-and-a-half does not
reappear, and nothing is claimed to bridge them.

> **What this section does NOT claim.**  That the double grid is a
> spacetime, or typical — one engineered family, and genericity is not
> posable here (chapter A9).  That any fixed number is *the* framework's
> ceiling: the ceiling is *k* times *k* for a *k*-way dispute and it has
> been reached at four sizes, which is four data points and not a proof
> that levelling works at every size.  That the sixteen-wide record is
> forced in the strongest sense available: the strongest offer test —
> every actor offered at every step — was run on three hundred and eighty
> of the sweep's fourteen hundred steps, and **no *tiling* four-way
> record passed it end to end**; what did pass end to end are two chain
> records, one carrying sixteen directions and one twenty-five.  That the
> odd rings or the winner/loser convention carry a real obstruction —
> they do not, on the evidence.  That any of this is a theorem about the
> grammar: the width ceiling and the dead wire are theorems, the records,
> the band memberships and the triviality are measurements.

### A8.10 The rank-2 question: is anything here a metric?

Widths and charts are means, not ends.  What a manifold arrow is *for* is
a **metric** — the rank-2 object that says how far apart things are and in
which directions — and the corpus has hunted one before, under a different
name, on a different substrate, and left a half-built answer behind.

The old hunt is worth stating because it is the source of the whole
odd/even split of §A2.9.  An earlier version line went looking for the
inverse spatial metric as the coefficient of a stochastic curvature, and
it half-failed **at theorem grade**: the *diagonal* entries of the metric
— the magnitudes — are recoverable from the probabilities, and the
**off-diagonal** entry provably is not, because it is the relative phase
and squaring destroys it.  That is an all-order no-go, not a shortfall.
The same split appears twice more, algebraically: the *anti*symmetric part
of a pair of transports is a rotation, which is a phase; the *symmetric*
part is a traceless rank-2 coupling, which is a metric.  So the corpus's
own structure is:

> **the real, even part builds the metric's diagonal; the odd part — the
> phase — carries the off-diagonal.**  A rank-2 tensor here is not
> *decorated* by a phase.  It is **completed** by one.

(And one adjudication, because the question keeps being asked in the wrong
vocabulary: every "2" on this programme's gravity line is a tensor **rank**
or a component count or a helicity.  No gauge group appears in any gravity
paper of the corpus, and importing one would be exactly that — an import.
On the generated line, composition of transports is measured and it
**commutes**, on every one of a hundred and seventy thousand pairs.)

**So the even half was resurrected and asked directly.**  Deep in an
earlier paper sits a three-by-three matrix of second moments on the even
channel — computed exactly, its determinants printed, and then **thrown
away in favour of its trace**, which is a single number.  The question is
the obvious one: was the trace a loss?  Is there a genuine rank-2 response
hiding under it?

The answer comes in two parts, and the first part is a lesson about
fixtures rather than about metrics.

**The anchor was the paper's own falsified example.**  The three record
pairs the matrix was originally built on are the ones that same paper,
thirty sections later, **audits and ranks eleventh**, directly above the
sentence declaring the old target falsified.  The residual quoted as "the
family's floor" is the loser's score, and it lives in a choice of *which
features to look at* — a place no function of the even channel can reach.
So the tempting central negative — *eleven candidate replacements and
nothing moved* — is **guaranteed by the fixture** and discovers nothing.  On the triples the paper actually **selects**, the error is
**zero exactly**, a wrong replacement is visibly punished, and the
question can be asked for the first time.

**And the surviving half is the better one.**  Rebuilt on the selected
fixture, the matrix is *more* lopsided than on the falsified one, its
three diagonal entries all differ, all three off-diagonals are non-zero,
and **nothing at all acts on its index** — no relabelling fixes it except
the trivial one.  That is exactly what a rank-2 object should look like as
a *starting point*.  It is also, on this substrate, all it is:

> **a scalar did not become a metric by interpretation.  It became a
> covariance matrix, which is a different thing.**  It has no index over
> the record's own points, it is rank one before averaging, no group acts
> on it to transform it, and promoting the law to use it changes not one
> predicted number.

The old verdict — that a scalar cannot become a full gravitational
response by reinterpretation — therefore **stands, and stands sharper**.

**One hint went the other way and had to be withdrawn.**  It looked, at
first, as if the right home for a rank-2 object were not that old paper's
three named channels at all but the *directions* of this book's own wide
charts, which do carry lopsided matrices.  Swept properly, the fifty-nine
matrices on the flagship record turn out to be **two**, with repeated
eigenvalues, one of them decomposing into two independent blocks; every
double ring gives the same answer, because a double ring is **built** with
a cyclic symmetry and its directions inherit it; and the narrow control —
the same index size as the old paper's three channels — is sometimes
exactly a multiple of the identity, which is the death condition the unit
itself had written down.  A big symmetry group means *fewer* free
components, not more.

> **So the redirection redirects.**  A form with a large stabiliser is a
> **cage, not a metric**.  If a rank-2 object on this programme is ever to
> be a form rather than a table, its stage has to have **generic**
> direction geometry — no hand-built symmetry at all.  That means
> sprinkling-like substrates, or crystals with deliberate defects, and
> nobody has built one.  `[MY READING]`

> **What this section does NOT claim.**  That anything here is a metric, a
> field, a response or a graviton — the licensed statement is a covariance
> on one channel index at one window under one measure.  That the earlier
> paper believed otherwise.  That the lopsidedness survives to any other
> window or substrate: it grows steadily with record size across the whole
> range measured and nobody knows whether it settles.  And that the phase
> half of the split has been tested at all — it has not; §A2.9 is where
> that hunt stands.

---

## A9. The wall and the crack

*Technical twin: Part B, chapter B9.*

### A9.1 The two lines and where they meet

By now the programme has two lines running:

- The **measure line** (chapters A4, A6) is deepest in the
  **delivery-free** sub-theory, where it has a settled answer at every
  depth, modulo one postulated shape.
- The **geometry line** (chapters A5, A7, A8) lives entirely at
  **delivery scope**, where deliveries and merges exist — and it needs
  no measure at all, which is why it could make progress.

The obvious next step is to bring the measure to where the geometry is.
**That step is blocked, and the block is a theorem.**

### A9.2 The unbounded menu

Everything in chapter A6's escape depended on one fact: in the
delivery-free world, the "situation" summary takes finitely many values
— 36 — which is what makes the algebra finite and the uniqueness
argument possible.

At delivery scope there is a short construction that destroys this, and
it destroys it **for any design whatsoever**:

One actor proposes, settles its own proposal alone, and thereby mints a
fresh version.  It does this again, and again.  Each round is legal.
Each round adds a version to what that actor holds.  Nothing removes the
old ones from the holdings list.  And **the delivery rule reads the
whole holdings list, superseded entries included.**

So after *k* rounds the actor has *k+1* different things it could
deliver, each priced at one quarter divided by *k+1*.  The number of
options grows without bound, and so does the set of exact prices.

> **Therefore no bounded summary of a record can reproduce menus exactly
> at delivery scope — not "this particular attempt blew up", but no
> attempt can succeed, because the menu itself takes infinitely many
> values.**

This also explains, retroactively, why the delivery-free world was so
well behaved: there, holdings are consulted through a rule that *skips*
superseded versions, so the same unbounded quantity exists but is
**invisible to the menu**.  The corpus's own verdict on its prize
result: **the 36-state closure is a starvation artefact.**  Delivery
makes the hidden coordinate visible.

Two further honest notes belong here.  First, a refined summary *was*
built which is menu-exact on the whole verified window, and it still
blows up: 1, 5, 17, 61, 191, 541, 1567 distinct situations by depth,
roughly tripling each level, with the search not closed at a cap of
twenty thousand.  But that curve is only an upper bound — the summary is
not proved minimal — so **the verdict rests on the unbounded-menu
construction, which is design-independent, and not on the curve.**
Second, an earlier reading of a similar table ("no situation ever
recurs") was **backwards**: situations recur totally, because padding a
record with idles changes nothing.  Only the count of *new* situations
per level carries information.

### A9.3 Why the menu runs on views, not on the world

The other half of the wall was already visible in chapter A3.  A summary
built from "what exists" — holdings, live proposals, supersessions and
their conflict structure — is **provably too coarse** at delivery scope.
The witness is two lines long: add one delivery of something the
receiver already holds, and the menu changes, because what changed was
*who knows*.  Measured over more than thirty thousand pairs of
same-summary records: 3,656 violations.

So a correct summary must track knowledge per actor — the sub-record
each actor has seen, and the combinations of those — which is exactly
the coordinate that does not exist in the delivery-free world.  It is
also, measured, the fastest-growing part of the blow-up at reachable
depths.

### A9.4 The crack, and how far it narrows

There is one gap in the wall, and it is worth understanding both what it
is and how much of it has already closed.

Look again at the ladder of §A9.2.  The individual delivery options get
smaller and smaller: a quarter split *k+1* ways.  But:

> **The delivery sector's TOTAL is exactly one quarter at every rung.**

The per-option weights vanish; that particular aggregate does not move.
So the no-go bites **per-option** descriptions, and one might hope that
**sector-level** descriptions escape it.

That hope has a good reason behind it, from an entirely different
direction — chapter A6's finding that a demand stated on the record can
only constrain **sums**, since what is observable is the probability of
moving from one kind of situation to another, not which labelled event
carried it.  **The physically meaningful objects are the aggregated
ones.**

So the escape candidate is sharp: **does a bounded sector-level summary
exist at delivery scope?**  It has been pinned and run at the natural
granularity — one sector per actor and event type — and **it is closed
there**, on one ground: a measurement, not an obstruction.  (A companion
argument that the sector alphabet must itself be infinite was withdrawn;
§A10.10c records why.)

**The coarsest possible lumping does not settle down.**  Track how many
distinct lumped situations survive as the enumeration deepens, and the
count keeps creeping upward at every window that can be checked — and a
control shows those counts are *lower bounds*, so the reading is the
conservative one.

The one hopeful measurement — that part of the menu *does* factor exactly
through a lumped summary on the tested window — is real, and it is not
enough.  Killing the unbounded counter is **necessary and demonstrably
not sufficient**.

**One caution about how strong this is.**  The wall of §A9.2 is an exact,
depth-free obstruction.  This closure is not: it is a measurement over
the depths anyone can reach, conservative but bounded.  It is also worth
knowing that the constant quarter is a fact about *deliveries*
specifically rather than a law of sectors generally — the other sectors
take several values — though at this size the values they take may well
be all there are.

> **The crack narrows rather than closes.**  What survives are strictly
> *coarser* aggregations — grouping by event type only, or by total budget
> only — and descriptions that give up exactness altogether and target
> only what a completion actually has to reproduce.  All untested.

### A9.5 What this costs the programme

Stated without softening:

> The method that settled the measure question at delivery-free scope —
> a finite exact quotient plus classical eigenvalue theory — **provably
> cannot transfer** to the scope where the dimension results live.  And
> the convergence question of chapter A11 — "does the measure prefer
> 3+1?" — is blocked on exactly this.

What that leaves is a search for a *different* method, and §A9.6 is where
that search now stands.  It is not blocked in the same way: the wall
forbids a **bounded summary**, and the route that survives never asks for
one.

### A9.6 The route the wall leaves standing: the horizon limit

Every attempt described so far tried to *compress* the theory — to find a
finite summary of a record from which the next step could be computed.
That is the thing the wall forbids.  So the surviving idea gives it up
entirely and asks a different question.

**The idea, in one paragraph.**  Do not summarize.  Instead, look a fixed
number of steps ahead — a **horizon** — and ask what probability the law
assigns to the next event *given* that the record still has that many
steps of future left in it.  That is a perfectly well-defined finite
computation at every horizon.  Then push the horizon out and watch: if
those probabilities settle down as the horizon recedes, the limit is a
probability law that needed no boundary condition at all, because the
boundary has been pushed to infinity.  Nothing in the construction ever
mentions a bounded summary, so nothing in it meets the wall.

The idea is not new to the corpus.  The machinery for it — horizon-limited
kernels at delivery scope — was built months ago as a side result and then
left unspent, and two independent earlier units name the same object as
the thing a delivery-scope law would have to be.  What the survey opening
this campaign added was discipline: it stratifies **every** wall by how
strong it actually is, so the campaign cannot mis-plan by quoting a
measurement as if it were an obstruction, and it enumerates and ranks
**nine** routes.  This one ranks first for a specific reason: **it is the
only route that needs finiteness nowhere.**

**What the measurement says.**

- **The construction behaves.**  The horizon-limited laws really are
  probability laws — every option list sums to one, at every record and
  at every horizon out to seven, over almost a quarter of a million
  records.  Chaining them across a cut is automatic rather than
  surprising: it follows from that one identity.
- **The drift shrinks.**  Compare each horizon's law with the next one's
  and ask how far apart they are.  At every depth, in every way of
  measuring distance, at **two, three and four actors**, the gap
  contracts.  The widest arm of this is a four-actor family of
  **318,704** records built one at a time on a single processor: the
  computation the campaign itself named as the one that would decide the
  headline, and which does decide it.
- **One convention question turns out to be two questions.**  A law like
  this needs a rule for what to do at the far end of the horizon, and
  changing the rule changes the numbers **at every single record** — so
  the truncation is a genuine choice, not a formality.  But on the object
  the programme actually cares about, the choice **cannot matter at the
  root**, and that is a *theorem*: swapping the two actors, or swapping
  the two proposal values, is an exact symmetry of the law, the options
  at the empty record form one orbit per kind under it, and therefore any
  rule that respects the symmetry gives the same answer there.  Off the
  root, where the choice does show, the separation is measured to shrink.
  A rule that *breaks* the symmetry separates immediately — which is what
  makes the theorem a statement about the rule's symmetry class rather
  than about horizons.
- **And what is missing is now a single named thing: a bound.**  A table
  that contracts is not a proof that it converges.  The classical way to
  get one is to show the process keeps **returning** to a state it has
  been in before, often enough that the future forgets the past.  The
  obvious version of that is dead here, and the receipt closes it: things
  an actor holds **never** get discarded, so the exactly-like-the-root
  class is left once and never re-entered, and by depth five more than
  three quarters of the completed mass is in records that will never
  regenerate.  But the *coarser* version — return to a state that merely
  looks the same at the level the law reads — is alive: it is re-entered
  thousands of times, and its chance of return within four steps is
  strictly positive on every window where it can be computed.

> **So the state of the measure campaign, exactly.**  The horizon-limited
> law is a genuine law out to horizon seven; its drift **contracts at
> every pool and depth measured**; it is protected from the truncation
> choice at the root by a symmetry theorem and measured to shrink off it;
> and what remains is **the bound** — the one theorem that would turn a
> contracting table into a limit.  The engine for it is named and
> unbuilt: the classical contraction theory of positive operators, run on
> the coarser return class.  **Nobody has attempted it, and it is the
> campaign's only surviving candidate.**

Two smaller routes closed on the way, and closing them is worth as much
as the positive: the two "cheap" aggregations the crack of §A9.4 left —
grouping options by type only, or by total budget only — both fail, and
they turn out to be **one test rather than two**, because at every depth
the decision uses they are the same grouping under different names.

> **What §A9.6 does NOT claim.**  That the route is alive: every positive
> statement above is a **table over computed horizons**, no bound was
> exhibited, and the word *converges* is banned from the receipt's own
> labels for exactly that reason.  That it is dead either: the four-actor
> row that looks, on two terms, like a drift that has stopped falling
> reverses at the very next horizon and ends below where it started.
> That any of this is *the* click law's measure: it is
> a mechanism, not an object, and the missing map is untouched.  And no
> claim about infinite volume is made anywhere under any outcome.

> **What this chapter does NOT claim.**  That the delivery-scope theory
> has *no* tractable description — only that no *menu-exact bounded* one
> exists, and that the natural aggregated version is closed too.  Strictly
> coarser objects, level-structured descriptions, and the boundary theory
> the corpus has already imported for a related purpose are untouched by
> both no-gos, and the horizon route of §A9.6 is the one that has been
> walked.  And the standing of the sources
> should be carried: §§A9.2–A9.3 rest on an advisory probe whose two
> load-bearing claims were independently re-verified and whose remainder
> must be re-derived before anything leans on it, while §A9.4's closure
> comes from a reviewed unit that lost one of its two published grounds
> in that review and now stands on the other alone — a measurement over
> reachable depths, materially weaker footing than §A9.2's exact wall.

---

## A10. The graveyard

*Technical twin: Part B, chapter B10.*

This chapter is a list of things that were claimed and then killed.  It
is the most important chapter in Part A.

Not out of modesty.  In a programme like this, where nobody outside is
yet checking, the only available evidence that a surviving claim means
anything is the **rate at which non-surviving claims were caught**.  A
document that presented only the live results would be
indistinguishable from one whose author had never looked hard.

Each entry: **what was claimed → what killed it → what survived.**

### A10.1 Dimension by counting clocks

*Claimed:* the record's "clock complexity" is a handle on its spacetime
dimension; climbing two → three → four means approaching our world.
*Killed by:* the author's own observation, plus exact mathematics: two
clocks is exactly one space dimension, but every richer spacetime needs
infinitely many, and some three-clock orders fit in no spacetime at all.
Then, from inside: the typicality study built on it collapsed for three
independent reasons (a claim that could not fail, a switched
normalization, and a proxy that counted idlers while half the weight is
idle).
*Survived:* counting is a legitimate **detector** of escaping one space
dimension and a grading of clock complexity.  And the *shape of the
sky* replaced it (chapters A5, A7).

### A10.2 The own-view abstraction route to H1

*Claimed:* the per-actor view can be summarized as an object determined
by the global summary, which would prove the missing lemma.
*Killed by:* its own review.  The per-actor object **is not an own-view
object at all** — the view an actor consults exceeds its bare causal past
in about eight percent of situations, and in **every** such case the
extra material is authored by the *opponent*.  Also withdrawn in the
same pass: a claim that one hypothesis subsumed another, which was
inverted.
*Survived:* the measurement of the lag, which is now a load-bearing fact
of chapter A3 — and which the eventual proof (§A6.9) *explains* rather
than works around: the lagging cases are exactly the two-actor events.

### A10.3 The wire-closure route to H1

*Claimed:* a candidate event touches a wire and therefore already sees
everything relevant on it, so the lag is menu-invisible, so the lemma
follows at every depth without induction.
*Killed by:* measurement, and then something worse.  Every event type
lags, not only the one predicted.  And **a smaller view can yield MORE
options** (chapter A3), so any argument built on "the lagged view sees a
subset" is unsound — which rules out a whole family of attempts,
including this one.
*Survived:* three refutations, and **not** the reduction the route
offered in their place.  That reduction — "the lemma is exactly a
question about four projections of a view" — runs the wrong way: the four
projections are *finer* than the summary, not determined by it.  What
stands is the bar it left behind: no depth-free argument may assume a
lagged view sees a subset.  The lemma was eventually proved by a
different route entirely, going through the summary directly (§A6.9).

### A10.4 Arc-realizability as the primary sky instrument

*Claimed:* a two-sided test for "is this shadow system arc-like?" would
decide circle-versus-sphere in both directions.
*Killed by:* running it on genuine 2+1 Minkowski, where it rejected 121
of 554 real skies (and, on a recount, a majority under one definition).
*Survived:* the weaker one-sided shattering test, alone — and the
empirical vindication of a doctrine that had been written as mere
caution.

### A10.5 Ratio-preserving completions

*Claimed:* implicitly, by anyone who thinks "just normalize the
weights".
*Killed by:* a theorem with a 36-of-202 certificate (chapter A6).
*Survived:* everything downstream, because the impossibility is what
makes the completion question a real question.

### A10.6 The zero-class counterterm

*Claimed:* the blind part can be filtered out, restoring normalization
exactly and preserving the gauge.
*Killed by:* it abolishes **all** joint arbitration.
*Survived:* the impossibility theorem, **narrowed** to
support-preserving completions, with the exclusion declared and its
reason given.

### A10.7 "Sign platform A, hold platform B" — the whole laboratory bridge

*Claimed:* two concrete experimental platforms could be identified with
record structures well enough to extract a bound, with one of them the
"strong" platform.
*Killed by:* the author's own objection, conceded in full: **an ion is
an enormous object in record terms.**  Four independent holes were then
recorded:
- a scale gap of roughly twenty orders of magnitude — illustratively, at
  a record spacing of one millimetre a proton would be of order ten
  light-years across;
- the corpus **cannot even fix that scale**: an earlier no-go gives
  exactly one record length with Newton's constant provably un-fixable
  within the framework, so the record scale is a free parameter and
  *any* assumption about where the laboratory sits is un-derived;
- a **layer gap**: records → background → quantum fields → atomic
  structure is at least three constructed layers, and **none of them is
  built**;
- and then, from chapter A1, the **loss** result: merging actors is
  never impossible but is massively lossy, so a bound extracted through
  a single-line description of a composite is a bound on the coarse
  world.

*Survived:* a named, empty slot — "the coarse-graining" — which is now
logically prior to the four things a bridge must fix, and is the sole
unblocking condition for the entire laboratory programme.  The eight
proposed correspondences are retained **unchanged**, as the criticizable
record, with the sign-off block sealed and not presented for signature.

The general lesson the corpus draws, and it is the practical reason the
measure problem matters: **a theory that has not chosen its measure
cannot produce a rate.**

### A10.8 "Infinite clocks, by Sperner's theorem"

*Claimed:* the combinatorial theorem of chapter A7 derives the
infinite-clocks doctrine, because a sphere-like sky shatters at every
size.
*Killed by:* the antecedent is empty — a sphere sky shatters four and
never five.
*Survived:* the conclusion, by a **different and cheaper** route
(counting shadows), with no shattering in the derivation at all — plus
the sharpening that width prices sky *size*, and the dimensional signal
is the *offset*.

### A10.9 "The construction saturates the theorem"

*Claimed:* the 20-actor record spends exactly what the theorem demands.
*Killed by:* it does not — the *family* it realizes needs exactly six
nested chains, so the bound is tight for the family, and the twenty
actors are the architectural cost of backflow.
*Survived:* the tightness result, which is sharper than the claim it
replaced, plus a clean open problem (is six actually achievable?).

### A10.10 "The admissibility layer does not select 3+1"

*Claimed:* because the layer admits a beyond-sphere sky.
*Killed by:* the same missing arrow that chapter A5's demotion had
already retired one rung down — it needs the assumption that discrete
3+1 skies are cap systems.
*Survived:* the **capacity** statement: the layer does not *cap* the
ladder at the sphere's rung.  And a named residue: a full-strength 3+1
control.

### A10.10b "Only empty shadows let a sky shatter" — and the zero it produced

*Claimed:* shattering requires a shadow that is **empty**; the two sky
readings whose shadows are never empty can therefore never shatter, at
any width or depth; so only one reading is usable.  And, downstream of
that: genuine three-space-dimension records never shatter four, so the
shatter number is not reading dimension.
*Killed by:* a one-line counterexample and then a measurement.  What
shattering needs is a shadow **disjoint from the set being tested**, not
an empty one — and a fifth direction's own shadow supplies that while
being perfectly non-empty.  All three readings are live.  With the
blinder removed and the density raised, genuine three-space-dimension
records **do** shatter four (0, 1, 11, 30, 116, 211 across a matched size
ladder) while two-space-dimension records never do, and neither shatters
five.  The zero that had looked structural was a **sparse sample read
through a blind reading**.
*Survived:* two things, and both are better than what they replaced.  The
narrow true lemma — a cover sky can never shatter *its own full direction
set* — and, in place of the retired negative, a **working two-sided
dimension discriminator** (§A5.7).  Also survived, and worth keeping: the
capacity discipline itself.  A test run on a sky too poor to have found
anything is not a measurement, and that error was real — of 415 skies
once counted as testable, 144 were genuinely capable.  What was wrong was
the *condition*, not the caution.

### A10.10c A sector-level escape from the delivery-scope wall

*Claimed:* the unbounded-menu theorem kills only per-option descriptions,
because the delivery sector's total is constant; so a description that
tracks sector totals rather than individual options should stay finite.
*Killed by:* one measurement.  The coarsest possible lumping does not
settle down — the count of distinct lumped situations creeps upward at
every window that can be checked, with a control showing those counts are
lower bounds.
*Nearly killed by a second fact that did not hold up.*  A companion
argument said the aggregated alphabet must itself be infinite, because
the arbitration sector divides its quarter by a count that grows with
depth.  At the scope measured that count never exceeds one, so the
handful of values observed **may be all there are**.  The argument was
withdrawn and the verdict rests on the measurement alone — which makes
this closure weaker than the wall of §A9.2, and it should be quoted as
such.
*Survived:* the observation that motivated the attempt — that the
physically meaningful objects are the aggregated ones — which still
points at the right *kind* of description; and a narrower crack, at
strictly coarser aggregations and at descriptions that abandon exactness
for what a completion actually has to reproduce.  See §A9.4.

### A10.11 Two uniqueness claims about the completion

*Claimed (first):* most of the far-end freedom acts trivially, so the
count of completions is far smaller than the count of boundary
parameters.
*Killed by:* an explicit perturbation, then upgraded by the corpus
itself from a witness to a **theorem**: every nonzero direction of that
freedom changes some transfer near the far end, because a transfer at
the outermost interior layer reads the boundary directly.  The published
count therefore stands, and a queued correction to a paper was cancelled
before it was applied.
*Survived:* a real and more careful statement — the map from far-end
data to the *interior potential* has rank exactly 84, so shallow
transfers see the boundary only through an 84-dimensional image while
the outermost layer sees all 313.

*Claimed (second):* among completions that do not distinguish record
points the law identifies, there is exactly one, and it needs no
boundary.
*Killed by:* measurement — that demand leaves 308 of 313 directions
free; the stronger indistinguishability demand leaves 137.
*Survived:* the **existence** result untouched, and the honest
replacement statement of chapter A6 §A6.8: uniqueness comes from a
postulated shape, and the shape is a choice.

### A10.12 "The atlas carries a gauge structure"

*Claimed:* the wide crystal's charts translate into one another by
non-identity rules that compose consistently, so the atlas carries a
genuine two-valued gauge structure — and the coupling between the two
rings changed *which* one it carries.
*Killed by:* the computation nobody had run.  Every number behind the
claim reproduced exactly under independent rebuild; then a single
further test — is the rule a relabelling? — turned **all** 108
non-identity translations into the identity at once, with zero
obstructions, at two independent conventions.  There is no structure
group, of any size.  Two supporting claims fell with it: the *name* of
the group was never determined by the data (ten groups are equally
consistent, two of them minimal and incomparable), and the
crystal-versus-control contrast is a convention that dissolves under two
of the three labelings and is confounded with chart width besides.
*Survived:* the **instrument** — a transition detector with the
triviality test now built into it, two artifact probes, and a validated
reading of the framework's own causal order — and a question nobody
could ask before: *can any record carry a gluing that is **not** a
relabelling?*, with a stated structural reason to look for it in records
made of conflicts (§A8.8).

### A10.13 "The completions are precisely what repairs descent"

*Claimed:* the objects the measure line was forced into are exactly the
objects that fix the generated law's failure to define a probability on
records — so the two lines of the programme meet there.
*Killed by:* counting.  The positive repairs form a **573**-dimensional
cone at the depth where the count is exact, of which the corpus's family
is a **28**-dimensional slice; and two explicit positive examples show
that fixing the order-dependence and defining a record probability imply
each other in **neither** direction.  Corrected in the same pass: the
load-bearing census is the narrower one the theorem actually speaks to
(32,256 failures of 425,334, not 88,632 of 665,286), and an item the
first version moved off the corpus's supplied-not-derived ledger stays
on it.
*Survived:* everything measured — the defect is exactly one ratio of
menu totals, with zero exceptions, exhaustively — plus two facts the
review added in the unit's favour: the *unnormalized* weight is
order-independent and constant on every record class, and the settled
completion's measure **genuinely descends**.  And the honest replacement
sentence: *the descent defect names the job a completion has to do; it
does not single out which completion does it* (§A2.7).

### A10.14 The two sentences the double grid refuted

*Claimed (first):* in a crystal made of conflicts, the widest chart a
*k*-way dispute can carry is **twice** *k* — with a mechanism that looked
legible in the chart itself, each disputant contributing one direction per
wire of its next message.
*Claimed (second), in the same breath:* a message-free conflict record
collapses to a line, so **the message is what gives a crystal its second
direction** — the schedule that maximizes conflict is the one that cannot
spread.
*Killed by:* the same reviewer that confirmed every number behind both,
who then built two records nobody had asked for.  Twice *k* is not a law
about disputes; it is the value the bound takes when every follow-on event
happens to be a **message**, which is what the schedules that were swept
imposed and what nothing in the grammar requires.  A disputant's wire can
instead be consumed by **another dispute** — and a dispute forks three
ways where a message forks two.  The true ceiling is *k* times *k*, and
the record that reaches it has **no messages in it at all**: rows and
columns quarrelling concurrently, nine charts of nine directions.  The
same object kills the second sentence, since it contains no messages and
was, when built, the widest record in the corpus — as is everything that
has outgrown it since, all of it message-free; the collapse that was
blamed on the absence of messages belongs instead to having only **one**
running dispute per actor, which makes the cycle a chain of diamonds.
*Survived:* everything measured — conflict tiles, the budget bound and its
saturation, the dead-wire theorem, the trivial gluing — plus a *better*
mechanism sentence in place of the refuted one: what a crystal needs for a
second direction is a **second concurrent conflict axis**, which a message
buys expensively and a concurrent dispute buys for free (§A8.9).

### A10.14b The frontier that was announced and never existed

*Claimed:* that uniformity is the **price** of width — that at four
disputants a record can be sixteen directions wide, or it can tile as
evenly as genuine spacetime, but no *whole* record can do both, only the
interior of one; and, alongside it, that the ceiling is out of reach
above four disputants, because the successors of a five-way quarrel
cannot be made to line up.
*Killed by:* the unit's own table, one round later, and by one extra
build.  The uniformity figures were sitting in the published sweep in a
straight line — rising with every round, with the gaps between them
*growing*, one step below the band's floor at the last round anyone had
paid for.  One more round of the same blueprint, unchanged, crosses into
the band — on **both** ways of measuring it, with the sixteen-direction
charts still in the record.  The "frontier" was the
last row of a table that had not been extended.  The five-disputant wall
went the same way: the alignment failure was a property of how one
bootstrap happened to be ordered, and padding it with the framework's own
idle event lifts the ceiling into reach at five *and* six.
*Survived:* every number of the sweep that produced the claim — an
independent rebuild reproduced all of it, figure for figure, including
the sixteen-direction witness event by event — and the design lesson
underneath, which is now stated the other way round and is stronger:
band membership in this family is a **crossing** of a rising sequence,
so it names a round number, and what composes with width is the thing to
report.  Also withdrawn with it: *"the first sprinkling-grade width in
the campaign"* as a claim about the mechanism — the comparison holds on
one statistic, at one dispute size, against a range that is really two
ranges (§A8.9).

### A10.14c The two sentences the quantum layer withdrew

*Claimed:* first, that the **record instrument is the exact boundary of
permitted coherence** — that a candidate quantum layer over the generated
law may hold interference exactly between histories whose immediate
parents the record could not already tell apart, and is forced to zero
everywhere else, by one equation each, with no cancellation anywhere.  It
was the sharpest sentence the programme had ever written about its own
quantum layer: the record instrument, which is *part of the click law*,
would have been the thing that removes a phase.  Second, alongside it,
that a **record measure of that shape cannot see a phase at all**, so no
amount of record bookkeeping could ever select one.
*Killed by:* one computation each, in the same round, after every number
of the unit had been reproduced from an independently written
instrument.  The first sentence was an artifact of *which* of three ways
of writing the record demand had been used: the version used forbids
interference between different records item by item, by hand, one level
below where the demand is actually stated — and so forbids exactly the
cancellations the stated version permits.  Written the way the parent
paper states it, **nothing whatever is forced**, at any depth, in any
variant; the "impossible" case was then built explicitly, as an exact
positive example, at the very pair the original had displayed as killed.
The second sentence was worse: it was a **tautology of the shape of the
equations**, not a fact about records.  A sum over a rectangle is
symmetric under swapping the rectangle's two sides, and anything
symmetric that way is automatically blind to the antisymmetric part — for
any grouping of anything, without computing anything.  Gated by running
the identical rows over a grouping with no relation to records at all.
Under the stated reading records **do** constrain phases, with a
measurable rank.
*Survived:* every number — the censuses, the whole dimension table with
every antisymmetric column, the geography counts, the witness and its
exact minor, all five controls, and the receipt's clean sheet under
hash-seed variation.  And the replacements are the better result, twice:
*consistency does not structure coherence*, and — from a computation the
unit's own residue had named and declined to spend ten lines on — *the
first fair dynamical demand eliminates all of it* (§A2.8).  This is the
graveyard's clearest case of a headline dying while its arithmetic lives,
and of the corrected reading being sharper than the one it replaced.
*Withdrawn quietly alongside them:* the phrase **"what the generated law
admits"**.  The count never sees the law — swap its weights for any other
positive ones and every equation is identical — so the honest subject of
the whole table is the record instrument and the way histories extend,
which is true of laws this corpus spent years excluding.

### A10.14d "The generated line is flat"

*Claimed:* that probability transport in this theory has **no holonomy at
all** — do any two available things in either order and the two products
of weights agree, so there is no loop for a phase to be the argument of,
and the founding question about interference-as-holonomy is answered
negatively at the root.
*Killed by:* the same round that **promoted half of it to a theorem**.
The sentence is true of one grammar, one weight and one scope, and the
round proved that half properly — six lemmas, depth-free — while
demonstrating that its last two steps hold only because two of the law's
four budgets happen to be set to the same quarter and exclude each other.
That is a **budget coincidence**, not a structure.  One grammar over, at
the scope where the geometry lives, it fails outright: eighty-eight closed
loops come back multiplied, forty more cannot be closed at all, and every
one of them carries a message.  Two further scope defects were exposed in
the same pass: the *normalised* law — the one that is actually a
probability — was never flat on that graph either, its loops returning
powers of a mass ratio the corpus had already named elsewhere; and the
instrument that certified flatness is **blind by construction** to exactly
the class where the whole defect lives, because a loop closes at record
level precisely when the locality argument already covers it.
*Survived:* every number, and more of the unit than usual — the
identification half of the weld (the two reversals do share a carrier),
the closed-scope statement itself, now upgraded from measurement to
**theorem** with its scope clause attached, and the pre-registered
falsifier's own verdict.  **And the replacement is the better result:**
transport scope is **curved**, the curvature is delivery-borne, and two of
its four values sit outside the already-known defect's group, which makes
it a candidate new object rather than a re-run.  This is the graveyard's
clearest case of a sentence being *too wide* rather than wrong — and of a
round returning a theorem and a discovery in exchange for a headline.

### A10.14e "The direction index is the stage" — and a fixture that had already been falsified

*Claimed:* first, that the right home for a rank-2 object in this
programme is the **direction index of the generated line's wide charts**,
because those charts carry lopsided matrices where an older paper's three
named channels supposedly do not.  Second, and underneath it, that eleven
candidate promotions of a scalar all landing on the same predicted number
showed the scalar *already sat at the family's floor*.
*Killed by:* one sweep and one act of reading further down the page.  The
fifty-nine "lopsided" matrices are **two** matrices, with repeated
eigenvalues, one of them splitting into independent blocks; every record
of that family gives the same answer, because the family is **built** with
a cyclic symmetry that its directions inherit; the first non-symmetric
record breaks the uniformity immediately; and the narrow control — never
actually measured by the unit that built it — is sometimes exactly a
multiple of the identity, which is the unit's own death condition.  A
large symmetry group means **fewer** free components, so the census had
been reading its evidence backwards.  The second claim died at its
fixture: the three record pairs everything was computed on are the ones
their own paper audits, ranks **eleventh**, and declares falsified, and
the number quoted as "the floor" is the loser's score — a residual living
in a choice of which features to look at, which no function of the
measured channel can reach.  **Nothing moved because nothing could.**
*Survived:* the factual half, and it is the durable one — the corpus did
compute a rank-2 object on that channel and did discard it for its trace.
Rebuilt on the fixture the paper actually **selects**, where the error is
zero exactly, the object is *more* lopsided than on the falsified one and
has no symmetry acting on it at all: the genuine starting point for a
rank-2 response, and the corrected verdict that it is nonetheless a
**covariance and not a metric**.  *The lesson this entry contributes to
§A10.16:* **anchor on a paper's own selection, not on the tables it prints
before falsifying them** — and measure your control before you cite it.

### A10.15 Smaller retirements, for completeness

- **"Cross-actor causation produces the sky"** — the control was miswired
  *and* could never have failed; rebuilt honestly, the comparison
  reversed and transport skies are **narrower** than chance.
- **"Sky size is bought with event count"** in Minkowski — the scan
  confounded count with density; withdrawn, both columns now reported.
- **"Width spreads with depth under the theory's own law"** — a
  near-tautology, withdrawn by name.
- **"All co-receivable pairs commute — an abelian monoid"** — true but
  structural, a consequence of how the state object is built, not a
  discovered finding; withdrawn as a finding.
- **"The failure is grain, not interaction"** — reversed once the family
  of readings was closed under products: sixteen readings say the
  interaction kills it, nine say grain.
- **"No situation ever recurs at delivery scope"** — backwards;
  recurrence is total.
- **"The total weight is not attached to nows"** — **false**, withdrawn,
  and the replacement is *stronger*: it is attached to nows but is not a
  gradient.
- **"H2 is subsumed by H1"** — inverted, withdrawn.  The two are
  independent, and each ended up needing its own proof: the dichotomy for
  one, the update table for the other (§A6.9).
- **Three register-theoretic bridges** to a full-poset structural no-go —
  all falsified, each at exit zero as a deliverable, so that nobody
  walks them again.
- **"The 1.82 is the evidence for the odd-channel phase"** — the corpus's
  most-quoted piece of bridge evidence, and a **closed-form constant of
  the formula it was computed from**: one line of algebra reproduces all
  thirty-two published digits, and deliberately adversarial inputs score
  the same perfect zero the survivor does.  What the number establishes
  is that some record carries a particular small integer.  Downgraded,
  not deleted — the *form* it was offered as evidence for is untouched
  (§A2.9).
- **"The odd-ring parity class is the phase"** — the one non-zero class
  the width road found looked like the missing odd-sector object because
  its index had the right parity.  It is **label**-holonomy: its
  construction never reads a weight, and a free choice of labelling
  removes it.  Settled negatively at the mechanical level.
- **"A drift that has stopped falling"** — a four-actor row announced as
  the measure route's negative on a **two-term** window; the third term
  reverses it and ends below the first.  The unit's own data already
  contained the counter-example, one pool over.  Withdrawn, and the
  replacement is the positive: contraction at every pool and depth
  measured (§A9.6).
- **"The truncation choice is object-dependent"** — half of that finding
  was **forced by construction**: the root leg is a symmetry theorem, so
  it could not have come out otherwise.  What is measured is only the
  off-root table, and it is much weaker than the headline it carried.
- **"The regenerative route is closed"** — closed for the *exact* return
  class and re-opened for the coarser one, which is re-entered thousands
  of times with a strictly positive return probability.  Two routes were
  being quoted as one, and the surviving one is the campaign's engine.

### A10.16 The pattern

Two observations about the list, which are the reason it is here.

**First: almost every correction hit an interpretation sentence, not a
computation.**  Across the reviewed units the computations survive
essentially intact — records rebuilt independently came out
identical, exact numbers reproduced, certificates re-derived by
different methods.  What failed, repeatedly, was the *sentence the
result was sold with*: a missing scope label, an arrow borrowed from a
premise class that had already been refuted, an antecedent nobody
checked was non-empty.  The eight most recent retirements above are the
purest form of it: in each, the reviewer confirmed **every** number and
then ran — or built — one thing the unit had not thought of, and the
headline did not survive it while the arithmetic did.  Which yields the
programme's current standing obligation: *name the computation that
would make the interesting reading false, and run it in the same
receipt.*  The recent cases also show what that obligation buys when it
is met: one refutation of a width sentence arrived with a **better
record** attached; the next killed a *negative* — a limit the unit had
announced — and left the strongest geometry statement the programme has;
the next inverted **both** of a unit's headline sentences and returned, in
their place, the sharpest fact the programme owns about its own quantum
layer *and* the sharpest open question it now has; and the three most
recent went further still — one ran the deciding computation the unit had
named, priced and declined, and turned a published negative into the
measure route's positive; one **closed a proof the unit had only
sketched** and, in the same pass, discovered the curvature that unit's
headline had denied; and one found a whole unit anchored on a fixture its
own source paper had already falsified.  **Being wrong in the pessimistic
direction is a failure mode too, and this list now contains both kinds.**

**A third kind, worth naming separately: a convention wearing the clothes
of a result.**  Two of the withdrawn sentences were true *of a choice the
unit had made about how to write its own equations* and false of the thing
being studied.  The check that catches that failure is not another
control; it is going back to the source the demand was quoted from and
writing the demand as it is actually stated.

**And a fourth, which the most recent round contributes: a fixture with a
provenance nobody read.**  A unit can be arithmetically perfect, gated end
to end, and still be computing on an example its own source paper audits
and discards a few sections later — in which case its central negative was
*guaranteed* and discovered nothing.  The check is cheap and is now
standing: **before anchoring on a published example, read what the paper
that published it says about it afterwards.**

**One more observation, and it has changed how the programme is run.**
The reviewers are no longer only finding defects; they are **out-building
the units**.  Recent rounds have supplied a theorem the unit had sketched
and could not close, a census the unit's own instrument was structurally
blind to, the deciding computation a unit had named and skipped, and a
correctly-measured control a unit had built and never read.  That is a
better outcome than catching an error, and it makes the round part of the
authorship rather than an audit of it — which is why this book credits
round-supplied results as content and does not narrate them as
corrections.

**Second: pre-registration is doing real work.**  The corpus writes down
what it expects *before* running, with the argument, and then reports
what happened.  In one recent unit's own accounting, **five of seven
pre-registrations in a campaign were corrected**.  A programme that only
recorded its confirmations would look far better and be worth far less.

---

## A11. Where we are, and what would decide it

*Technical twin: Part B, chapter B11.*
*Forward-look **superseded by PART D**: this chapter is accurate as the
state of the two lines, but the destination it gestures at has since been
stated explicitly (LOG #436).  Read PART D for what the open questions are
**for**.*

### A11.1 The state of the two lines

**The measure line.**  In the delivery-free, two-actor sub-theory the
completion question is *settled*: there is a boundary-free completion,
it is unique up to scale within a postulated shape, it prices the
beginning of the record and the renewal point identically, its cost is
exactly one named tilt, and the statement now holds **at every depth**
rather than at the depths anyone enumerated.  Three qualifications, all
permanent until someone does work: the shape is a **choice**; the proof
is prose reasoning checked against the code rather than machine-verified
logic, and a formal mechanization is the line's last residue; and the
specific numbers are **toy-relative**.  Three actors are out of scope
entirely.  At delivery scope the question is **open**, and chapter A9
shows the tool cannot travel.  One thing has been added from outside the
line: the completion's probability really is a function of the *record*
and not of the order it was written in (§A2.7) — which the completion had
always been assumed to deliver and had never been checked — while the
uncompleted normalized law is not, and the freedom the shape suppresses
is now counted from that side too.  **And the line has, for the first
time, a route to delivery scope that the wall does not forbid**: the
horizon limit of §A9.6, which never asks for a bounded summary, is a
genuine law out to horizon seven and contracts at every pool and depth
measured, with one theorem — a bound — standing between a contracting
table and a limit.

**The geometry line.**  At delivery scope, measure-free: the sky is an
actor-width phenomenon; sky richness has an exact price in actors; the
shatter ladder is a dimension meter; and the framework admits records
whose skies sit at the sphere's rung *and one rung beyond*, with the
higher one **forced** by the menus at every step of its construction.
So the admissibility layer does not cap the ladder.  The line has also
now built a record that tiles *and* spreads, proved four directions to be
the ceiling of any delivery circuit, and measured the transition rules
between that record's charts — which are **pure gauge** (§A8.8), so the
structure a manifold would carry starts at nothing here.  And it has gone
through the door the ceiling theorem left open: records built out of
**crossed disputes**, with no messages inside their rounds, tile at the
same cadence and carry charts of **nine, sixteen, twenty-five and
thirty-six** directions — the corrected ceiling, reached exactly at every
size built — while the sixteen-direction one sits inside the band that
genuine sprinkled records occupy, on both ways of measuring it, as a
whole record (§A8.9).  Their charts glue trivially too.  And it has asked
the question the whole width road is *for* — whether any of this is a
**metric** — and got back a covariance: an honestly lopsided second-moment
matrix with no symmetry acting on it, on a substrate where nothing
transforms it and promoting the law to use it changes no prediction
(§A8.10).

**And the map between the two lines, which belongs to neither.**  It has
stopped being only a name.  Three of its segments are now measurements
(§§A2.7–A2.9): the generated law's normalized weights do not descend to a
probability of a record, by one repairable defect, while the settled
completion's do; the quantum layer such a law could carry has been
counted rather than speculated about; and the **phase** — the thing that
would make such a layer quantum rather than merely uncertain — has been
hunted where the corpus's own archaeology says it should be.  The second
measurement is the more consequential and the less comfortable — what it
found is that consistency with the records is far too weak to organize
interference, and that the first demand asking the interference to come
from the law itself removes all of it.  So the map's functional stretch is
**narrower and harder** than it was: narrower because it has been
measured, harder because the measurement's answer is a negative at the
only scope where the corpus can compute.  The third is the one that
re-opened a door: probability transport is **flat at closed scope as a
theorem and curved at transport scope as a measurement**, so a holonomy
exists after all — and it is, so far, a positive real number with no phase
in it.

### A11.2 The convergence question

Put them together and one question remains, and it is now the
programme's centre of gravity:

> **Does anything in this framework prefer 3+1?**

The rules about what may happen do not — that is chapter A8's licensed
result.  So if anything does, it is elsewhere, and there are exactly
three named candidate homes:

1. **The measure.**  A completed law might assign the wide,
   courier-heavy records that buy high shatter numbers negligible
   weight.  Not posable at delivery scope by any *bounded summary*
   (chapter A9) — and now, for the first time, approached from the one
   direction that never asks for one: the horizon limit of §A9.6, which
   contracts everywhere it has been measured and waits on a bound.
2. **Resource cost.**  Dimension is priced in actors, and the price
   grows.  Perhaps something like a cost principle selects a rung.
   Nothing of the kind exists in the corpus.
3. **Counting typicality.**  Perhaps among all records of a given size,
   the ones with sphere-like skies dominate combinatorially without any
   measure at all.  Also unbuilt — **and not even posable** until home 1
   lands, because typicality is a statement about a measure.

**And here is the observation that reorganized the whole programme.**  The
four things this book most wants and does not have look like four separate
frontiers: we have a mechanism that *makes* space but engineers it rather
than finding it emergent; the number of dimensions is **unselected**,
since the dispute size is a dial the builder turns; typicality is
**unposable**; and the quantum layer is **excluded** at the only scope that
has been closed.  They are not four problems.  **They are one missing
object — a measure at transport scope** — and it is exactly the thing the
wall of §A9.2 proved cannot be built the obvious way.  That is why the
programme's current campaign is the measure itself, attacked from what the
wall leaves standing, and why §A9.6 is the most consequential section of
this chapter.

### A11.3 A reading, clearly labelled

`[MY READING / speculation — not a corpus claim]`

If I had to say what the shape of the answer *looks* like from here, it
is this: **dimension in this framework behaves like an economic
quantity.**

Every ingredient points that way.  A rich sky cannot be bought with
time, only with parallelism.  Each actor's worldline can contribute only
a nested family of shadows, so complexity of the sky is a *supply*
problem.  The construction that works is a *supply chain*: dedicated
single-use couriers, minted because the alternative (reusing a channel)
contaminates it.  And the price is a specific, computable number of
actors per rung of the ladder: 3, 6, 10, 20.

If that reading is right, then "why 3+1?" would not be answered by an
impossibility at rung five.  It would be answered by a *cost* — the rung
where the marginal cost of another dimension stops being worth paying,
under whatever counts as payment.  Which is why candidate home 2 above
seems to me under-explored relative to candidate home 1, even though 1
is the one the corpus has invested in.

**But this is speculation and must not be cited as anything else.**  The
corpus has no cost principle, no notion of what is being economized,
and no derivation.  I am describing the *shape* of a possible answer,
not an answer.

### A11.4 The ranked open problems

1. **What is the curvature of probability transport?**  Transport scope
   is **curved** — eighty-eight closed loops come back multiplied, all of
   them delivery-borne, none of them visible to the instrument that had
   certified flatness (§A2.9).  Everything hangs on characterising it:
   what carries it once records rather than sequences are the objects;
   what group it lives in; whether it is removable by relabelling like
   every other loop structure this programme has found; and whether its
   **odd** half has an imaginary part.  That last is the imaginary
   exponential's only known remaining address, and it is where the
   destination's whole phase story lives.

2. **The bound.**  The horizon route contracts at every pool and depth
   measured and exhibits **no bound** (§A9.6).  One theorem — the
   classical contraction theory of positive operators, run on the coarser
   return class — turns a contracting table into a measure at delivery
   scope, which is the object four separate frontiers are waiting on.
   Named, unattempted, and the campaign's only surviving candidate.

3. **A rank-2 response on a stage that can carry one.**  The even channel
   hosts a covariance and not a metric (§A8.10), and the substrates this
   line offered are hand-built crystals whose symmetry is a cage.  What is
   needed is **generic** direction geometry — sprinklings, or crystals
   with deliberate defects — and the cheapest first question is whether
   the selected fixture's lopsidedness survives its own controls.

4. **Where does superposition enter?**  At the one scope where it can be
   computed, a quantum layer over the generated law cannot be both
   generated by the law's own state and carry interference (§A2.8).  The
   demand that produced that verdict was *one* fair demand, tried against
   *one* of the three ways of writing the record condition, and its
   uniqueness was not established — so the cheapest move here is to run
   the same demand against the reading that is actually stated, and then
   against a second demand.  Beyond that the named homes are the delivery
   scope and a different joint of the map altogether — and item 1 is now
   the concrete form the delivery-scope answer would take.

5. **A bounded description of the theory at delivery scope.**  The one
   remaining gap in the wall (chapter A9) — noting that item 2's route
   does **not** need one, so this is no longer the only way through.
   Exact per-option descriptions are impossible for
   any design; the natural sector-level ones are closed, and so are the
   two cheap coarsenings, which turn out to be one test; what survives
   are inexact, observable-only descriptions — untested.

6. **Which sky reading is physically privileged?**  All three are live,
   and they disagree — the discriminator of §A5.7 is sharpest under the
   cover reading, while other results were computed under a different
   one.  Nothing justifies a choice, and several conclusions depend on
   it.
7. **What is left of the width road.**  The object three separate
   results pointed at — a crystal made of disputes rather than of
   messages — is built (§A8.9), and it gave one of the three things asked
   of it, refused the second, and left the third where it was.  It
   **tiles**; it carries **nine, sixteen, twenty-five and thirty-six**
   directions where a delivery circuit carries four, reaching the
   corrected ceiling at every dispute size anyone has built; the
   sixteen-direction record is *also* inside the sprinkling band, whole
   and on both readings, so width and uniformity have no frontier between
   them; its charts still glue **trivially**, at every convention tried,
   so the gluing motivation came back negative; and the measure defect
   that also named conflict lives at a different scope, which these
   records measure the analogue of and do not bridge.
   What is left here are two residues rather than a construction: a
   **proof** that the levelling trick works at *every* dispute size,
   rather than the four sizes measured, and whether a *tiling* record at
   five disputants or more exists at all, let alone one that holds the
   band.  Both are open; neither now blocks the road.
8. **Is there a record-level demand that forces the shape?**  The two
   strongest candidates and their conjunction are eliminated by
   measurement.  Nobody has a third — and the demand that the law be a
   probability of the record at all, which one might have hoped would do
   the job, cuts the freedom from 573 directions to 205 and stops there
   (§A2.7).
9. **A machine-checked version of the delivery-free settlement.**  Both
   halves of it — what a candidate can see, and how the summary updates —
   are proofs read off the framework's own source and checked against it
   at scale, not logic a proof assistant has verified.  That is the one
   thing left on a line that is otherwise finished.
10. **General rungs of the ladder.**  The builder visibly generalizes
   past five; it has not been run, and unrun is unclaimed.
11. **Minimality.**  Six actors are necessary for shatter-four and twenty
   were spent; ten are necessary for shatter-five and forty-two were
   spent.  Both gaps are architectural and both are decidable.
12. **The residual pricing defects.**  The off-ladder configuration; the
   general-depth ladder being false under current pricing; the one
   merge priced two ways.  All carried forward into the completion
   problem rather than patched.
13. **The reading-relativity questions.**  Which sky definition is
   physically privileged; which channel reading is.  Same class of
   question: structures whose conclusions depend on a representation
   choice nobody has justified.

### A11.5 What exists, and how it was made

Three papers are terminal — meaning attacked and repaired to
completion, not merely written.  They cover: the grammar and the
completion decision; four decisions at the joints of the theory; and the
boundary of closure.  Around them sit dozens of pinned units, each with
a pre-registered plan, an executable exact receipt, a result note, and a
frozen hostile-review record.

The method, in five lines, because the method is a substantial part of
what this programme has produced:

- **Pin first.**  The plan, the gates, and the *expected outcome with
  its argument*, committed before any code exists.
- **Receipts, not claims.**  Exact rational arithmetic, standard
  library only, exit zero required, deterministic across hash seeds
  (a determinism defect was caught this way and recorded rather than
  quietly fixed).
- **Report the boring outcome.**  Pre-registering the unexciting
  expectation is the cheapest defence against later talking yourself
  into an exciting one.
- **Hostile rounds, and now independent-model rounds** — a reviewer with
  no prior context, instructed to recompute rather than trust, writing
  its own code.  Thirteen such rounds have run; nine found a blocker;
  **all nine blockers were in interpretation, not arithmetic**, and the
  most recent eight were the same mistake eight times — a headline built
  on numbers that were all correct, refuted by a computation, or a
  construction, the unit had not thought of.  (Two of the last three
  reversed a headline without raising a blocker at all, which is why the
  blocker count is no longer the interesting statistic.)  The recent ones
  came back with more than they removed: one with a better record attached
  than the one it refuted; one that killed a **limitation** the unit
  had announced and left the stronger claim in its place; one that
  inverted **both** of a unit's headline sentences and returned the
  programme's first hard fact about its own quantum layer; one that ran
  the deciding computation a unit had named and skipped and turned its
  published negative into the measure route's positive; one that
  **finished a proof** the unit had only sketched *and* discovered the
  transport curvature that unit's headline denied; and one that found a
  whole unit anchored on a fixture its own source paper had already
  falsified.  **Reviewers on this programme now routinely out-build the
  units they review**, which is why their results are carried here as
  authorship rather than as a correction log.
- **Forward corrections only.**  The ledger is append-only.  Nothing is
  silently edited; superseded text is preserved verbatim next to its
  replacement.

That last rule is why this document can exist in the form it does.  The
graveyard of chapter A10 is not reconstructed from memory; it is copied
out of a record that was designed to make forgetting impossible.

---
---

# PART B — THE THEORY WITH THE OBJECTS

> **How to read Part B.**  Every claim carries a provenance label and a
> scope.  Numbers are quoted from committed sources, named at the point
> of use.  Unit identifiers (`d42a`, `D44a`, `D49`, `D54`…) are
> **work-unit names**, not concepts: each names a pin (pre-registered
> plan), a receipt (executable code), and a note (result).  `#NNN` are
> entries in the append-only ledger `v10/LOG.md`.
>
> **Standing scope vocabulary.**  **d42a** = the delivery-free grammar
> (`g`/`p`/`r`/`n`), receipt `v10/code/d42b3_placement_exact.py`.
> **d42b1 / transport scope** = d42a plus delivery and merge, receipt
> `v10/code/d42b1_transport_exact.py`.  Unless a sentence says
> otherwise, "two actors" is the width.

---

## B1. Actors, records, lines

*Non-technical twin: Part A, chapter A1.*

### B1.1 The primitive

An **actor** is the framework's primitive holder of history, defined by
exactly four properties (`THE-COMPLETION-DICHOTOMY.md` §1.1):

1. **Sequential** — all of one actor's events are totally ordered among
   themselves; an actor never branches.
2. **Own version chain (the mint chain)** — a version written by an
   actor must descend from the last version *that same actor* wrote.
3. **Addressable** — actors deliver to one another.
4. **The source of width** — the framework's parallelism is bounded by
   the number of actors.

A **record line** is one actor's trace: the succession of versions it
has written.  The **record** is the whole generated structure — all lines
plus the coupling events.  Actors and lines are in strict bijection.

**Interpretation status.**  Nothing in the corpus identifies an actor
with a particle, a region, a degree of freedom, an observer, or any
laboratory object.  The primitive is *physically uninterpreted, and
deliberately so*.  The one serious attempt at such an identification is
`note-d41c-step3-bridge-declarations.md`, whose status is **BLOCKED**
(§B10.7).

### B1.2 Aggregability [D48, LOG #413/#414/#415, round 1 terminal]

The question, in its only internally answerable form: *is the grammar
closed under actor coarse-graining?*  Receipt
`v10/code/d48_composite_line_exact.py` (11 PASS / 0 FAIL post-repair);
admissibility decided only by the committed d42b3 layer's own
`candidates_for`, never a re-implemented predicate.

**Controls (the exit-1 conditions) held `[EXACT]`:**

| map | admissible images |
|---|---|
| identity | 21,428 / 21,428 |
| bijective renaming | 21,428 / 21,428 |

So the grammar is equivariant under what actors are *called*; everything
below is about how many there *are*.

**CG3 — the labelled record does not aggregate `[EXACT]`.**  Every
non-injective actor map sends a positive fraction of admissible records
to inadmissible images:

| map | admissible images | fraction |
|---|---|---|
| `{A,B}→X, {C,D}→Y` | 10,820 / 21,428 | 50% |
| `{A,C}→X, {B,D}→Y` | 10,820 / 21,428 | 50% |
| `{A,B}→X, C, D` | 15,932 / 21,428 | 74% |
| all → X | 4,004 / 21,428 | 18% |

**CG5 — generic, not a boundary effect `[EXACT]`:** the admissible
fraction falls monotonically with record length — **100% → 88% → 70% →
48%** at lengths 1/2/3/4.

**CG4 — the mechanism, exhibited not counted.**  Two distinct actors
each propose on the same base version; the merged image is *one* actor
proposing twice on a base its own line has already left, which the
layer rejects.  **The obstruction is the mint chain.**

**CG6 — the dual, and the gate that asserted otherwise fired `[EXACT]`.**
Coarse-graining is **surjective**: all **1,190 / 1,190** admissible
coarse records lift to some admissible fine record.  The first version
of this gate asserted non-surjectivity, failed at exit 1, and the
assertion was withdrawn.  The correct picture is one-directional:
coarse-graining is a **partial map — onto but not total** — whose domain
shrinks with record length.

**The labelled/causal distinction, and it is decisive.**  CG3 decides
admissibility of the *literal renamed event sequence* — bookkeeping —
whereas the programme's own thesis is that the physics is the causal
order.  New gate CG8: of the records whose literal merged image is
inadmissible, how many have a causal poset realized by *some* admissible
coarse record?  **All of them: 10,608 / 10,608 at cap 4 (in-receipt) and
196,304 / 196,304 at cap 5 `[REFEREE-CARRIED]`** — zero exceptions in
206,912 cases.  Headline restated: **the labelled record does not
aggregate, but the causal order does.**

**The real obstruction is LOSS.**  Gate CG9: causal-poset isomorphism
classes.

| length | fine (4 actors) | coarse (2 actors) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 4 | 3 |
| 4 | 9 | 5 |
| 5 | **19** | **8** `[REFEREE-CARRIED]` |

**Coarse-graining is never impossible; it is massively lossy.**  Any
quantity computed after such a projection is a quantity of the coarse
world.

**Scope held (pin §4).**  This says nothing about ions, molecules,
constituents or mass.  The licensed conditional is *if constituents are
actors, then a composite is irreducibly many lines*, and the antecedent
**remains unsigned**.  It is explicitly **not** established that the
coarse description is meaningless — CG6 and CG8 both forbid that reading
and no citation may make it.

**Why this chapter matters downstream.**  D47/D47b measured that sky size
is set by actor count (§B5.6); D48 shows actor count is not a free
redescription.  Together: the number of directions at an event is
physical content, not a modelling choice — which is the first internal
foothold under the "infinite clocks" doctrine (§B7.1), since unboundedly
many directions require unboundedly many actors and that number cannot
be renegotiated by coarse-graining.

---

## B2. The grammar and the weight system

*Non-technical twin: Part A, chapter A2.*
*Primary source: paper 30 §1 (`relativistic-isp-v10-paper30-the-generated-record-and-its-completion.md`), §4.*

### B2.1 Carriers, order, gauge

Carriers are **wires**: participants and version objects.  The event
poset is the **carrier-wise wire closure**.  **Causal order is physical;
incomparable order is gauge.**  All weights are exact rationals (Python
`Fraction` in every receipt).  The event alphabet is typed with the
initiator carried in the type — paper 28's lesson that type data is
load-bearing.

### B2.2 The six event types, with carriers `[POSITED]`

| event | meaning | carriers |
|---|---|---|
| `('g', v0)` | **genesis**: version `v0` held by all participants — *"the declared supplied boundary"* | — |
| `('p', a, b, x)` | `a` proposes payload `x` against base version `b` | `{a}` alone |
| `('r', a, C, w)` | **arbitration**: initiator `a` ∈ `C`'s proposers resolves conflict component `C`, selecting feasible winner set `w` (a maximal independent set of `C`'s conflict graph).  *The arbitration event is acceptance*: it creates `v' = (base, value(w), authors(w), initiator)` | `C`'s proposers **plus `v'`**; the base enters as event data, never as a carrier |
| `('n', a)` | recorded idle, the budget absorber | `{a}` |
| `('d', s, r, v)` | **delivery** of `v` from `s` to `r` — a **join of knowledge**; re-delivery admissible and physical; after it, `r` holds `v` and `r`'s past contains `s`'s chain up to the delivery; supersessions travel with the join, not as payload | `{s, r}` |
| `('m', a, pkey, w)` | **merge**: `a` reconciles two versions it holds; `v_m` supersedes both members, pair-scoped, so unmerged third forks remain mergeable and reconciliation recurses | `{a, v_m}` |

**Design note, load-bearing:** version wires are touched *only* by
arbitration events.  A shared version carrier would chain same-base
proposals into comparability and make conflict grammatically impossible.
That is why `('p', a, b, x)` has carrier `{a}` alone.

**Holdings** propagate only through participation or delivery: `a` holds
genesis, every version created by an arbitration or merge `a`
participated in, and every version delivered to `a`.

### B2.3 Admission, past-local

- **Proposal** `('p', a, b, x)` is admissible iff the event creating `b`
  is in its past, no supersession of `b` is in its past, and no
  *unresolved* prior proposal by `a` on `b` is in its past.  (A prior
  resolved by a past arbitration does not block; supersession then
  blocks re-proposal on the old base on its own.)
- **Arbitration** is admissible iff all proposals of `C` are in its past,
  `C` is maximal there, the base is unsuperseded there, and no prior
  arbitration on that base is in its past.  **A singleton live proposal
  is a (trivial) component**, so its proposer may self-arbitrate — the
  uncontested-acceptance path, without which no version is ever created
  conflict-free.
- **Merge** is admissible iff both versions are held, both were created
  on the same base, their creating events are incomparable in the
  merger's past, and neither is superseded there.
- **Conflict `[POSITED]`:** two proposals conflict iff they share a base,
  their payloads differ, and the two events are incomparable.
  Same-payload proposals are compatible (co-authorship).  There is no
  separate conflict lottery: conflict is born from generated concurrency
  and exhibited as conditioning.

**`[THEOREM]` Live-triple uniqueness (paper 30 §1.3).**  No history
contains two proposals `('p', a, b, ·)`.  Proof: a first proposal lies on
`a`'s wire, hence in the past of any later same-base event by `a`; if
unresolved there the unresolved-prior clause blocks; if resolved, the
resolving arbitration's component key contains its triple, so that
arbitration's base is `b`, `b` is superseded in the past, and admission
blocks.  Receipts keep the census as a regression tripwire only:
**0 violations over 13,060 histories (d42a), 0 over 7,393 (d42b1)**
`[EXACT]`.

### B2.4 `candidates_for` is the sole authority

```
candidates_for(history, actors)  →  [(event, weight), …]
```
returns exactly the admissible next events with their exact rational
weights.  Read from `v10/code/d42b3_placement_exact.py`: it builds
`pred = event_poset(acts)` and the full view, enumerates the base set as
`{V0} ∪ {vname(...) : arbitrations in the full view}`, and then for each
actor sweeps proposals over (base, payload) pairs, arbitration events
over all non-empty subsets of the live proposals per base with all
non-empty winner submasks, and finally the idle — calling `admissible()`
on each and keeping the ones that pass.

> **This part of the theory is unambiguous, single-source, exhaustively
> enumerable, and exact.**  Every unit that needs admissibility calls
> this function; **no unit re-implements the predicate**, and D48's CG0
> gate exists precisely to enforce that.

**A7, the governing principle (paper 30 §1.4):**

> **The opportunity set is the past-local admission relation and nothing
> else.**

It binds three layers, each a gated law rather than a convention: the
**generator** (any enumeration must be a superset generator filtered by
admission — a filter computed from the global record would be an
unpinned batch-close mark and gauge-dependent), the **pricing layer**
(the same relation prices; the availability bit first exists at the
join, so the priced conditional has joint-record dependence, declared),
and **conduct beyond the caps**.

**Extension-invariance gates `[EXACT]`:** the enumerated family is closed
under linear extensions, and every enabled `(event, weight)` pair is
invariant under every linear extension of every history — **2,875
candidate-set points over 856 distinct resequenced histories** in the
base grammar; **7,509 points over 3,638 histories** in the transport
grammar.

### B2.5 Enumerated families and censuses `[EXACT]`

- **ARM-1** (two actors, d42a, depth ≤ 5): **6,471** histories.
  Cumulative layer census `[1, 7, 39, 215, 1191, 6471, 34375]` through
  depth 6; the depth-7 **level** is 145,408; **179,783** histories in
  all (D44a).
- **ARM-2** (three actors, d42a, depth ≤ 4): **6,589** histories.
- **ARM-1T** (two actors, transport, depth ≤ 4): **3,969**.  ARM-2T
  (three actors, depth ≤ 3): **3,424**.  The two-actor transport family
  cumulative census is `[1, 9, 69, 521, 3969, 30729]`, with **243,769**
  through depth 6 (D56 M1, both anchors matching the committed census).
- Depth-2 conflict census is exactly **4** in both grammars, with
  `mu([pA0, pB1]) = 1/64` under the extended budget; conflict histories
  at depth ≤ 5 number **3,316**, all with positive exact weight.
- **Transport serialization `[EXACT]`:** 60 in-family histories in which
  a delivery chains two would-be conflicting proposals into
  comparability and *prevents* the conflict.

> **Numerical hygiene note (D50 own defect 3, LOG #422).**  Paper 30's
> much-quoted "1,191 histories" is the **cumulative** count through
> depth 4; **976** sit at the depth-4 layer (1,191 − 215).  The figure is
> routinely quoted as if it were a layer count.

### B2.6 The local weight law `[POSITED, the fixed-budget standard]`

At each participant local step, conditioned on causal past only:

- **propose total `1/4`**, split equally over enabled `(base, payload)`
  options *in the initiator's view*;
- **arbitrate-and-merge total `1/4`**, split equally over admissible
  arbitration component keys (computed *at the join's own past* — the
  component first exists as a record at the join) plus enabled merge
  pairs, times the kernel law's winner distribution;
- **deliver total `1/4`**, split equally over enabled
  `(receiver, version)` pairs *in the sender's view*;
- **idle absorbs every unavailable total** — redistribution, never
  dilution.  Baseline idle at genesis is exactly `1/2` (propose and
  deliver open, arbitration closed); with all three sectors open it is
  `1/4`.

**Kernels `[POSITED as alternatives]`:** K1 = a uniform recorded
order-click over the `|C|!` component orders followed by greedy
acceptance; K2 = uniform over maximal independent sets.  On the
three-proposal path `P–Q–R` they give `{P,R}` weight **`2/3` versus
`1/2`** `[EXACT]` — the discriminating instance, here *generated* rather
than supplied.  A value-conflicted pair merge is a binary click at
uniform `1/2` (K1 and K2 agree on a pair); equal-value merge is
deterministic.

**Still supplied, declared:** the kernel *law* itself, the genesis
version, and the measure completion.

### B2.7 The ladder A7' and its spectra `[EXACT]`

> **A7'.**  A per-initiator weight sum at a record point equals
> `1 + k/4`, where `k` counts the additional join components the pinned
> law prices for that initiator beyond its own view.  The initiator's own
> view's sectors always sum to exactly 1 — at the record points of the
> enumerated families, at the declared caps.

The minimal case is blind self-arbitration: an initiator's own view holds
a sealable singleton while the join view holds the pair, and the sum is
`5/4`.  Spectra:

| family | spectrum |
|---|---|
| ARM-1 | `{1: 11,926, 5/4: 1,016}` |
| ARM-2 | `{1: 16,539, 5/4: 1,824, 3/2: 936, 7/4: 468}` |
| ARM-1T | `{1: 7,514, 5/4: 424}` |
| ARM-2T | `{1: 9,588, 5/4: 576, 3/2: 72, 7/4: 36}` |

In ARM-2, `k = 2` is an outer path actor priced in its pair and the
triple; `k = 3` is the central path actor blind-priced in both pair views
and the triple.  In the transport arms the deliver and merge sectors are
initiator-view priced, hence never blind: **blindness comes from
join-view arbitration layers only.**

**This ladder is also the whole of the descent defect.**  At two actors
the *total* menu mass is `2` or `5/2` accordingly — 34 of the 36 `sigma`
states at 2, two at 5/2 — and the failure of the normalized law to
define a measure on records is exactly the ratio of two such totals, and
nothing else (§B2.10).

**Mechanical decomposition, gated:** propose and deliver sectors exactly
`1/4`-or-`0`; every candidate component key group exactly `1/4`; totals
reconstructed from sectors at **18,210 points, 0 violations** `[EXACT]`.

**Obstruction density (paper 30 §4.2) `[EXACT, scope declared]`:** per
actor-point, `sum − 1` equals `(#blind component-key groups)/4`, every
blind group contributing exactly `1/4` — the obstruction functional is
component-additive and quarter-quantized.  Family-wide gate: **2,382
actor-points, 0 violations**, `k`-spectrum `{0: 2,134, 1: 248}`.  Scope:
the exact-`1/4` quantization is verified at single-component join views;
additivity at `k ≥ 2` is carried by the base-grammar spectra.

**The `h12` constraint (paper 30 §4.4) `[EXACT]`.**  One constructed
transport configuration is genuinely off the ladder: a *dead* component
(base superseded) still inflates a live singleton's view-relative
arbitration denominator, producing a per-actor sum of **`23/24`** — the
actor's arbitrate-and-merge sector prices `1/12 + 1/8 = 5/24` instead of
`1/4`.  The admission-based denominator fix is unavailable: it flattens
the anchored `5/4` spectra.

> **Therefore the general-depth ladder is FALSE under current pricing,
> and the reconciliation belongs to the completion problem, not to a
> pricing patch:** any completion `Z` on the extended grammar must price
> dead-component inflation.  This is paper 30 residue item 6, carried
> unchanged in paper 32 §6 item 8.

**Two named regression exhibits, both all-`1` `[EXACT]`:** `h5` and
`h11`, constructed deep configurations in which knowledge is transported
past a causally blind seal (a relay delivering a fork branch to a third
party; a live merge pair standing against a join-dead arbitration half).
They fix the law's conduct at depths the enumeration cannot reach.

### B2.8 The honest status ladder

**(i) What CAN happen — COMPLETE.**  §B2.4.  Unambiguous, executable,
exhaustively enumerable, single-source, exact.

**(ii) Relative weights — DEFINED, structurally characterized.**  §B2.6,
§B2.7.  With two declared defects: `h12` off-ladder, and the general-depth
ladder false under current pricing, both carried into the completion
problem.

**(iii) What DOES happen — NOT DEFINED.**  Menus sum to **2** or **5/2**.
Quoted verbatim from the docstring of `v10/code/d42b1_transport_exact.py`:

> *Weight-system level only (RF4): no measure claim; the placement front
> (d42b3) owns normalization; the `1+k/4` ladder is censused per
> A7/A7'.*

And, from the same docstring, the declared status of the boundary:
*"Genesis v0 = declared boundary."*

**(iv) A known internal pricing divergence, unreconciled.**  The D2H
merge prices **`1/16`** under the embedded head versus **`1/24`** under
the terminal d42b1 grammar.  Exhibited and recorded (paper 32 §6 item 6);
form-level results unaffected; **not reconciled.**

**(v) Reading-relative pieces.**  D46e (paper 32 §6 item 4's parent) is
the sharpest instance.  The channel family was closed under products of
its own labels (5 → 11 readings, each gated a genuine coarsening).
Corrected census: **66 evaluations / 25 discriminating pairs — 16
collapse at `g = 0` only (the interaction kills the ray), 9 at neither
(grain), 0 at `g = 1/2` only, 0 at both**; the delta's final
classification of all 66 is COLLAPSE 16 / STRUCTURED 10 / NO-COLLAPSE 24
/ SUPPORT-MISMATCH 7 / BOTH-ZERO 9.  The NPR reading gives
`c = 204703/480000` (b = 0) and `265103/480000` (b = 1).  **#389's "the
failure is GRAIN, not INTERACTION" is WITHDRAWN.**  The named successor
is the channel-reading question itself: *which reading is physically
privileged?* — open.

**(vi) And a third object wears the same name.**  "The interactive click
law" denotes three things in this corpus, and conflating them is the
single easiest error to make:

| sense | object | status |
|---|---|---|
| **ADMISSIBILITY law** | the grammar's `candidates_for` | **complete** — unambiguous, executable, exhaustively enumerable (§B2.4) |
| **PROBABILITY law** | the grammar's weight system, completed | **provably not self-normalizing** — the dichotomy (§B6) |
| **IDENTIFIED law** | the conditional measure of the D15 action | **empirically anchored, not proved record-closed** (§B2.9) |

> **The one-sentence answer to "how well defined is the interactive click
> law?":** the **admissibility** interactive law is **complete**; the
> **probabilistic** interactive law is **provably not self-normalizing**
> (§B6); and the **identified** law is **anchored but not record-closed**
> (§B2.9).  One programme, three senses, **one missing map**.

### B2.9 The action line, the identified law, and the missing map

*Sources: paper 18 (`relativistic-isp-v10-paper18-no-silent-erasure-and-the-identified-click-law.md`); paper 29 (`…-paper29-where-the-action-cocycle-lives.md`), the bridge audit; `note-d59-click-law-identity.md`; `v8/LEDGER.md` #126, #128–#130, which is this stream's own ledger.*

The corpus carries **two descriptions of dynamics**, and paper 29's
abstract opens by saying so:

> *"The program has carried two descriptions of dynamics without placing
> them on one type ledger."*

**THE ACTION LINE `[papers 13/15/18/19; D20–D27]`.**  Quantum-mechanical
throughout — amplitudes, class operators, a decoherence functional, with
durable clicks obtained only after a record instrument is **supplied**.
Its chain: paper 13 (a supplied whole-history process has no second
next-click generator — its **conditional measure is the click law**);
D18 (the operational `(E, D)` core plus record semantics); paper 16 (the
action does **not** select the complete history law); paper 17 (two
complete rulebooks agreeing on every proper record shadow and differing
at complete support).  Then a posited principle closes the coherence
clause:

> **NO SILENT ERASURE `[POSITED]`.**  Every loss of a record-accessible
> distinction must be **received** by records: distinctions are sealed
> only by dispersal of their content into other record systems, never by
> intrinsic destruction.  Equivalently: total content is conserved (the
> closure is unitary), and **sealing = dispersal**, with the v6 quarter
> law (§C1) as its metric.

It selects exactly one equivalence class at the coherence clause, forbids
intrinsic-collapse generators as silent erasure, and prints a
parameter-free falsifier (residual complete-history suppression zero
within stated sensitivity, no new constants).  A companion exact receipt
shows click statistics **identify both interaction graph and coupling** on
a rational witness family — star versus chain separating at every interior
coupling with closed forms `P(C=1) = s·16/25` versus `s²·16/25`,
necessarily coinciding at `s ∈ {0,1}`, with the coupling pinned by an
exactly linear statistic.  D25 later replaced the ensemble-injectivity
form of the principle with **distinguishability-isometry**, and D27
replaced the Molnár/Kadison surjectivity import with **Busch 1999** as the
governing non-surjective theorem.

**The identification `[SYNTHESIS + LITERATURE]`, as paper 18 states it:**

> the currently measured clicks identify the **Standard Model plus
> effective gravity** — the **D15 action** at the measured couplings
> (`α⁻¹ = 137.035999…`, `α_s(M_Z) = 0.1180`,
> `G_F = 1.1663787×10⁻⁵ GeV⁻²`, `sin²θ̂(M_Z) = 0.23122`, the Yukawa
> ladder, `λ_H ≈ 0.13`, `κ = 8πG/c⁴`) — **as the leading history
> generator over their tested energy domain.**

**The ceiling is carved in**, in the paper's own words: *identified, not
derived*; low-energy domain only; UV completion, carrier-birth selection,
**3+1 emergence** and the derivation of `G`'s value all remain open.  Not
claimed: the complete click law at every energy — the same global record
demands at least a neutrino-mass operator and a dark sector.

**THE GENERATED-LAW LINE `[papers 26–32; D34–D58]`** is everything else in
Parts A and B: record-closed conditional laws on generated carriers,
culminating in the d42a/d42b grammar, its weight system, the completion
dichotomy and the geometry programme.  Constructed and receipt-anchored;
**generates** causal structure; **presupposes no spacetime**.

**THE MISSING MAP.**  Paper 29 §1.1:

> *"The action line and the generated-law line now meet at one missing
> map."*

and its abstract closes on what is missing:

> *"the D15 low-energy action is retained, yet the corpus still **supplies
> rather than derives** its boundary state, measure and contour,
> renormalization, record instrument, **generated record grammar** and
> clock dictionary.  **The identified law has therefore not yet been
> proved record-closed.**"*

> **So the two are NOT the same object, and there is NO identity theorem.
> The relation is a named MISSING MAP** — and naming it is itself the
> result: the grammar of §§B2.2–B2.7 is precisely the *generated record
> grammar* that the identified law currently receives as a supplied slot.

Two segments of that map are now **measured**, from the generated side
only: §B2.10 gates the closed generated law against paper 29's stated
requirements one by one, and §B2.11 measures the **functional slot** the
first of those segments named — the exact space of paper-29-shaped
decoherence functionals over the closed law's own history layer.

**The partial bridge `[paper 29, conditional theorem]`.**  A scalar click
cocycle **descends** from the quantum decoherence functional exactly when
four conditions hold: the queried record algebra **decoheres**; both
routes name one refined cylinder or one declared pushforward atom; every
displayed conditioning cylinder has **positive mass**; and the regional
**boundary is sufficient**.  For a positive refined cylinder measure the
descended equality is elementary:

```
P(a|H) P(b|Ha)  =  mu(Hab)/mu(H)  =  P(b|H) P(a|Hb)
```

The sufficiency clause is not decorative: on the paper's exact Bell
fixture (`CHSH = 2√2`, four spacelike operator interchanges, sixteen
no-signalling marginal checks, sixteen refined click cocycles, 320 exact
Gram-positivity controls), **erasing a measurement-setting record makes
the boundary insufficient** and the descent fails.

**And a discipline that travels with it.**  Paper 28's chosen projected
generator fails **337 of 506** registered flat action squares, smallest
witness `1/18 ≠ 2/33`.  That inequality is **exact** — and paper 29
reclassifies what it means: the two serial weights push forward to **one
unordered action atom of mass `23/198`**, and the corresponding weights of
the embedded jump law (`1/32`, `1/48`) to one typed causal-DAG atom of
mass `5/96`.  Both pushforwards normalize.

> **Paper 28's flat action-variety nonmembership survives; NO
> probability-law inconsistency follows.**  An unordered atom sums
> serialization preimages; it does not require their weights to be equal.
> (Paper 29 also shows K-flat's completion form is a general positive
> `h`-ratio, **not** a uniquely Born signature — which is the same lesson
> §B4.3 teaches about flatness.)

**Where this stream's ledger lives:** `v8/LEDGER.md` #126 (the paper-18
hostile round: 12 MAJOR / 25 MINOR / 18 NIT applied, **zero false receipt
results**, the receipt surviving clean-room rebuild), #128 (round-2
integrated delta), #129–#130 (the complete-record-law campaign: D24's
birth kernel, D25's supersession of the F1 route, D26's declared
interface, D27's Busch correction, and the **uniqueness retyping** — "one
class" holds *given* the posited principle under a declared convention,
while the record alone additionally tolerates sub-bound intrinsic collapse
and modified-gravity laws).

### B2.10 The descent conditions — the missing map's first measured segment `[D65, LOG #465 → #467 → #468; round 1 TERMINAL]`

*Sources: `note-d65-descent-conditions-pin.md` (STRICT, committed before the receipt); `note-d65-descent-conditions-result.md`; `v10/code/d65_descent_conditions_exact.py` (39 PASS / 3 FAIL — the FAILs are the pre-registered negative, counted as the two statements it is — exit 0, ~336 s) + `data/d65_descent_conditions_exact.out`; `v10/reviews/d65-round1-hostile-review.md` — REVISE, 1 BLOCKER / 5 MAJOR / 8 MINOR / 3 NIT, arithmetic verdict "every single number reproduces".*

**SCOPE, load-bearing in every sentence here: two-actor, delivery-free,
d42a; the exhaustive depth-6 family (34,375 histories, census
`[1, 6, 32, 176, 976, 5280, 27904]`, 36 `sigma` states, 176 transition
keys, 5,548 record classes).**  Nothing transfers to the action line.
The missing map is an *identification* problem and remains open; this is
one segment of it, from the generated side.

**The test (DC1).**  Paper 29 Theorem 1's descended identity, applied to
the generated law's normalized menu kernel `P(e|H) = q(e|H)/N(H)` in
exact `Fraction`s:

```
        P(a|H)·P(b|Ha)  =?  P(b|H)·P(a|Hb)
```

**Two hypotheses were censused and only one is the theorem's.**  Paper 29
§3 defines commutation at the **refined record level** — both orders
denote the same cylinder, `[Hab] = [Hba]` — and §3.1 explicitly does not
require equal weights for distinct serial histories that later push to
one quotient atom.  So the **refined sub-census is the load-bearing
test**, and the wider `sigma`-commuting census is context.

| census | ordered pairs | identity holds / fails |
|---|---|---|
| ordered pairs `(a, b)` of distinct menu events | **794,570** | — |
| neither order admissible (mutual exclusion) | 129,284 | — |
| exactly one order admissible | **0** | — |
| both orders admissible | 665,286 | — |
| … non-commuting (`sigma(Hab) ≠ sigma(Hba)`) | **0** | — |
| … `sigma`-commuting (context) | 665,286 | 576,654 / **88,632** |
| … **refined-record identical (Theorem 1's hypothesis)** | **425,334** | 393,078 / **32,256** |
| … `sigma`-commuting but not refined (§3.1 exempts) | 239,952 | — / 56,376 |

Exhaustive over every parent of the family, deepest level in full,
nothing sampled.  The 56,376 exempt failures carry **no descent
content**, and the receipt exhibits a genuine positive record-cylinder
measure that fails that wider test too.  Three facts the census settles
in passing: admissibility on a menu pair is **symmetric**; the menu is
**not** all-concurrent (129,284 mutually exclusive ordered pairs); and
wherever both orders run they already agree on the successor state.

> **`[EXACT]` THE STRUCTURE OF THE FAILURE, ZERO EXCEPTIONS.**
> **(1)** The **raw** cocycle holds on **all 665,286** commuting pairs —
> `q(a|H)·q(b|Ha) = q(b|H)·q(a|Hb)`, spectrum `{1: 665286}`.  The entire
> defect lives in the normalization.  **(2)** The defect is exactly
> `d = M(sigma(Hb))/M(sigma(Ha))`, `M` the per-state menu mass — the
> **coboundary of a function of `sigma`**, read off d44a's committed row
> sums (34 states at `2`, 2 states at `5/2`), zero exceptions.
> **(3)** Spectrum `{1, 4/5, 5/4}`; a function of
> `(sigma(H), class(a), class(b))` (616 ordered pair classes, zero
> splits under either of two key resolutions); it vanishes **exactly** on
> same-mass intermediates and occurs at every mass-mixed pair; it is
> confined to **6 of the 36** states, two of which carry mass `5/2`.

**The witness is the quarter law seen from the measure's side.**  At
depth 1 (`H = [p_A(v0,0)]`, `a` = A's self-arb, `b` = `p_B(v0,1)`): raw
products identical at `1/32`, but `N(Ha) = 2` while `N(Hb) = 5/2`, so
`d = 5/4`.  **The mass jumps from 2 to 5/2 exactly when a blind conflict
group becomes visible in the join view** — §B2.7's `k/4` excess, in the
descent vocabulary.

**And the same object read as a connection (§B2.12).**  The defect is
exactly the holonomy of the *normalised* kernel on the record deletion
graph: its image is the infinite cyclic group **`⟨5/4⟩ ⊂ R₊`**, its square
spectrum the same `{4/5, 1, 5/4}`, and it is a coboundary because the menu
mass is a node potential.  That is worth stating in this vocabulary
because it fixes the reference against which the *transport*-scope
exchange holonomy is compared — and that one takes values `2/3` and `3/2`
**outside** `⟨5/4⟩`, so it is a different object and not this defect
reappearing at a wider scope.

**What this says, exactly.**

> **`[EXACT]`** At this scope **no positive measure on refined record
> cylinders has the generated normalized kernel as its conditionals.**
> This is Theorem 1's **contrapositive** applied to a conditional system
> meeting every one of its hypotheses (all displayed conditioning
> cylinders positive — 179,782 menu entries, smallest weight `1/8`; a
> common refined cylinder — 16,128 unordered failing squares).

**It is NOT an F1 hit.**  F1 asks for a positive refined cylinder measure
with unequal conditional products; Theorem 1 forbids that and Theorem 1
is a theorem.  What is exhibited is a conditional system **not induced by
any such measure**.  It does not touch the closure theorem, (H1), (H2) or
the six-state chain, which are statements about the *admissibility and
weight* law.  And the **unnormalized** weight `q(h) = Π q` is constant on
all **5,548** record classes — order-independent *and* a function of the
record — but it is **not a measure**: it is not additive along cuts (cut
masses `1, 2, 4, 257/32, 1037/64, 2101/64, 68313/1024`), which is exactly
why a completion is needed.

**The completion corollary `[PROOF, two lines]`.**  The hypothesis is one
equation, `Z(Hab) = Z(Hba)` for every commuting pair.  Given it both
displayed products telescope to `q·q·Z(Hab)/Z(H)` and `q·q·Z(Hba)/Z(H)`,
whose raw factors agree by the gated raw cocycle.  Any completion
factoring through `(depth, sigma)` satisfies the hypothesis, because
`|Hab| = |Hba|` and `sigma(Hab) = sigma(Hba)` **is** the definition of
the commuting class. ∎

**And the corollary is an IMPLICATION, not an equivalence — this is the
whole content of the round.**  Truncate at depth `D`, let `Z` be free and
positive on the depth-`D` histories and extend downward by the completion
recursion; then "repairs the squares" and "descends to a record measure"
are two *different* linear systems, both solved exactly over `Q`:

```
  D = 4 :  free variables (depth-4 histories)          976
           repair constraints Z(Hab) = Z(Hba)          403   exact rank 403
           dim POSITIVE REPAIR CONE                    573
           dim of the (depth, sigma) family inside it   28
           dim record-constant (descending) family     313
           dim REPAIRS THAT ALSO DESCEND               205
  D = 5 :  3,053  vs  32  vs  1,138 — the gap WIDENS with depth
```

`Z ≡ 1` solves both systems, so each solution space meets the positive
orthant in an **open** cone: every dimension above is a dimension of
strictly positive completions, leaving **545 independent directions of
positive repair transverse to the corpus's family**.  Two exact positive
witnesses, both reconstructed inside the receipt: one **repairs every one
of the 403 squares and does not descend** (two record classes carry two
`μ_Z` masses each), one **descends and does not repair** (a measure on
refined record cylinders, constant on all 427 depth-≤4 record classes,
that breaks `sigma`-commuting squares).  **Neither property implies the
other.**

> **`[EXACT]` THE HIERARCHY, AND WHAT SELECTS THE CORPUS'S COMPLETION.**
> repair cone (**573**) ⊃ repairs that also descend (**205**) ⊃ the
> `(depth, sigma)` family (**28**) ⊃ one ray, D49's `Zhat`.  **The object
> that collapses 573 to 1 is D50's FORM choice, not descent** (§B6.12).  The descent defect
> names the **JOB** the completions do; **it does not single them out**,
> and the sentence that it does is blacklisted (§0.3).

> **`[EXACT]` AND `Zhat` GENUINELY DESCENDS — the strongest descent-side
> fact the corpus owns.**  For the transfer operator
> `(T f)(s) = Σ_e q(e|s) f(s·e)` on the 36 states: `ker(T − 2I)` has
> dimension 1 with a **strictly positive** generator, values `{1, 4/3,
> 7/3}` at multiplicities `{29, 5, 2}` — D49's `f = (4,4,3,7,3,3)/3`;
> `ker(T − I)` is mixed-sign; `ker(T − 5/2 I)` and `ker(T − 9/4 I)` are
> empty.  `Zhat(h) = 2^(−|h|) f(sigma(h))` has **zero** harmonicity
> violations at every depth of the family, and `μ_Zhat = q·Zhat` is
> **constant on all 5,548 record classes** — zero splits.  So `Zhat` is
> the unique positive `λ = 2` harmonic completion of its form whose
> measure is a function of the record.  This is an **extra fact, not a
> corollary**: by the first witness above, repairing the squares does not
> imply it.

*(d42b3's gradient completion is not an independent second instance: it
is `Z ≡ 1` at depth 4 pulled back by the same recursion and factors
through `(depth, sigma)` — 64 occupied cells, zero carrying two values —
so its zero-failure result is the corollary instantiated.  Its two
anchors are re-derived: `Z(∅) = 1037/64` is exactly the depth-4 raw cut
mass, and the deformation census reproduces.)*

**DC2 — a RESTATEMENT, and it is not sold as more.**  Theorem 2 says a
boundary-only kernel exists exactly when the next-record law is constant
on the declared boundary's fibres.  With `pi = sigma` that condition **is
(H1)** (§B6.13) and the state update **is (H2)** (§B6.13b).  Nothing new
is proved.  What is delivered is the **exhibit**: fibre constancy
re-affirmed directly on the family (36 fibres, zero carrying two
different renamed menus, 34,375 histories swept) and the **36-row
normalized kernel `K(·|sigma)` printed in full** in exact `Fraction`s.

**DC3 — paper 29 §4.3's five durable-record hypotheses, gated one by
one:**

| # | hypothesis | label | verdict |
|---|---|---|---|
| 1 | exclusive & exhaustive durable alternatives | **SUBSTANTIVE** | **PASS** — 718,570-event adversarial pool built independently of `candidates_for`, plus 22,762 on the unrestricted surface; zero duplicates, zero omitted admissible events, zero weight disagreements.  It establishes **enumeration completeness of `candidates_for` against `admissible`**, not exclusivity independent of the layer |
| 2 | decoherence of the queried record algebra | **REPORTING-ONLY** | trivially satisfied and **uninformative** *(the hypothesis is now measured directly, one level up — §B2.11)* |
| 3 | one common refined cylinder | = DC1 | **FAIL** |
| 4 | positivity of every displayed conditioning cylinder | **SUBSTANTIVE** | **PASS** — 179,782 entries, smallest `1/8` |
| 5 | sufficient declared boundary | RESTATEMENT (= DC2) | satisfied |

**Hypothesis (2) holds for the empty reason, and that is where the map's
remaining width is.**  The generated law is a classical stochastic
process on records, so its decoherence functional is diagonal by
construction.  Paper 29's hypothesis is a condition on class *operators*
and their Gram functional; **the generated line has no derived functional
level at all**, and this unit does not build one.  That is exactly where
D59's *record instrument* and paper 29 §9.2's *preferred durable algebra*
still sit — and it is the segment §B2.11 measures: the **space of
candidate** functionals over this layer is now exactly counted, which
narrows the residue without discharging it, because measuring a space of
candidates is not deriving a member of it.

**DC4 — D59's six supplied-not-derived items, re-scored.  NO ITEM
MOVES.**

| # | item | verdict |
|---|---|---|
| 1 | boundary state | **stands** — it is the *action* line's slot |
| 2 | measure and contour | stands; **now PRICED with a number** |
| 3 | renormalization | stands; untouched |
| 4 | record instrument | stands; DC3(2) says why it cannot move — and §B2.11 measures the slot above it without filling it |
| 5 | generated record grammar | stands *for the action line* |
| 6 | clock dictionary | stands; untouched |

**Item 1 stands, and the positive statement belongs beside the ledger
rather than on it.**  D59's items are quoted from paper 29's abstract,
where the possessive is the *identified* law's: it is that law's
boundary/cosmological state — §9.2's slot table names it as selecting
amplitudes and long-range correlations — which is supplied.  The
generated line's `sigma` was never on that list, so it cannot move on it.
What is true, and stated beside it: on the generated side the declared
boundary statistic is **not supplied** — `sigma` is *constructed* from the
committed layer, its sufficiency is (H1) + (H2), and the 36-row kernel is
printed.  **The generated line has a derived boundary statistic; the
action line's item is untouched.**

**Item 2 is priced.**  The generated law has an order-independent
unnormalized weight and a normalized kernel that is not order-independent,
the gap being the coboundary of the state-mass function; a measure on
record cylinders therefore requires a **completion**, which is supplied
data whose form D50 already showed is a choice — and the repair cone is
573-dimensional at the depth-4 truncation, 205 of those dimensions also
descend, 28 are the `(depth, sigma)` family, and the collapse to one ray
is the form choice.

**Explicitly not licensed (the unit's own list, and this book observes
it):** anything about the identified law's measure; *"the completions are
**precisely** the objects that repair descent"* (§0.3); *"the generated
law descends to a record measure"* without the completion clause and its
D50 price; *"the generated law does not descend"* without the
normalized/unnormalized distinction; *"the unnormalized weight descends
to a record measure"* — it does not, it is order-independent and
record-constant and not additive along cuts; D59's boundary-state item as
**moved**; the 88,632 figure as the descent failure count — that number
is **32,256 on 425,334**; anything at three actors, at transport scope, or
beyond the exhaustive depth-6 family; and DC2 as a new result of any kind.

**Residues.**  (1) The map's **functional segment** is named here and
**narrowed, not discharged**, by §B2.11: there are still no *derived*
class operators and no *derived* Gram functional, so DC3(2) stays
uninformative until one is built — that, not DC1, is where the map is
widest.  What §B2.11 adds is a measurement of the candidate space and one
hard negative inside it (a candidate cannot be both state-generated and
coherent at this scope).  (2) Whether the defect's coboundary form survives beyond this
scope: `M` takes two values here because the quarter law's excess is
binary at two actors; at three actors or with delivery the mass spectrum
changes and the statement must be **re-derived, not carried**.  §B8.9
censuses the commensurable quantity at transport scope — the menu-mass
excess above the actor count, in quarters, which is non-zero exactly where
conflict groups are open — and reports explicitly that it does **not**
reproduce the `2 → 5/2` values and does not bridge to them.  (3) The
refined-record identification: `canon` was *chosen* as the record-identity
functor, and refined ⊆ `sigma`-commuting holds because `canon`-identity
implies `sigma`-identity — verified for this functor (0 splits over 5,548
classes), not a general fact.  (4) Depth is mostly discharged: the
class-level census is complete (`720 = 616 + 104 = Σ m(m−1)` over the 36
states, every class realized), which with (H1) + (H2) reduces the
all-depth statements to the finite check the receipt ran; what remains is
a renaming-composition lemma gated only on the diagonal at depth ≤ 2.
(5) A depth-free statement of the repair cone — 573 and 3,053 are
truncation dimensions — is the successor's obligation, and it is D50
sharpened.  (6) Three actors and transport, out of scope as always.

**The census's information content, said plainly** because the pair
counts invite overreading: by (H1) and (H2) every quantity in the DC1
census is a function of `(sigma(H), renamed a, renamed b)`, so the
794,570 ordered pairs collapse onto **720 class-level facts** (616
commuting + 104 exclusive), each replicated about 1,100 times.  The
multiplicity is replication, not independent confirmation — and it is
what makes the all-depth reading available at all.

### B2.11 The functional slot — the map's second measured segment, and the first hard fact about the quantum layer `[D68, LOG #478 → #479 → #480; round 1 TERMINAL]`

*Sources: `note-d68-functional-slot-pin.md` (STRICT, frozen and committed before any computation ran); `note-d68-functional-slot-result.md`; `v10/code/d68_functional_slot_exact.py` (**39 PASS / 0 FAIL**, exit 0, 271.2 s, peak RSS 1,270,890,496 bytes — runtime and memory printed by the receipt itself) + `data/d68_functional_slot_exact.out`; `v10/reviews/d68-round1-hostile-review.md` — REVISE, 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT, arithmetic verdict "the arithmetic is flawless; every single number reproduces".*

**SCOPE, load-bearing in every sentence here: two-actor, delivery-free,
d42a, the CLOSED scope; the truncations `D = 2…6` of the exhaustive
depth-6 family** (census `[1, 6, 32, 176, 976, 5280, 27904]` = 34,375
histories, 36 `sigma` states, 176 transition keys, **5,548 record
classes** `[1, 6, 23, 84, 313, 1138, 3983]`), **one record functor**
(`canon`), **one dynamical ansatz**.  **No member computed here is
claimed to BE the action line's decoherence functional.**  No
Hilbert-space ontology is claimed and **no class operators are
constructed**: `D` is a form on a finite set.

**THE QUESTION.**  §B2.10's residue 1 says the generated line has no
*derived* functional level, and that this, not the descent identity, is
where the missing map is widest.  That residue is made computable here.  Over the
depth-`D` history layer, measure the **exact** space of Hermitian forms
`D(h, h')` satisfying

* **C1** — the record demand, in **three readings** (below);
* **C2** — positive semidefiniteness (paper 29 §4.2's strong positivity);
* **C3** — cylinder consistency across a depth step, `R^(d)(g,g') =
  Σ_{a ⊐ g, b ⊐ g'} D(a,b)`, with `R^(D−1)` required to satisfy the same
  convention's C1 at depth `D−1`.  **This is the unit's construction, not
  paper 29's**: §4.2 asserts only that additive restrictions are *stable*.
  Labelled a construction wherever it is used;
* **C4** — equivariance under the **label-map group** (actor swap × value
  flip, four maps, computed rather than assumed).  **This is not the
  constraint system's symmetry group** — see the deflation below.

Dimensions are `variables − EXACT rational rank` by sparse elimination
over **Q**; positivity is certified by exact strict diagonal dominance
and exact 2×2 determinants, never a float (an AST gate on the receipt's
own syntax tree enforces it).  The real symmetric space is the headline;
the **Hermitian extension** `D = S + iA` is carried as a separate column
throughout.

**THE READING CHOICE IS A FORM CHOICE ONE LEVEL UP — AND IT IS DECIDED.**
C1 can be written three ways, and the three are ordered:

| reading | condition | status |
|---|---|---|
| **sum** (weaker bound) | `Σ_{h,h'∈r} D(h,h') = μ_Ẑ(r)` and nothing else | **drops decoherence entirely** — the queried algebra is never asked to decohere, so §4.3's own bookkeeping licenses no scalar record probability for what it constrains |
| **FAITHFUL / medium — THE HEADLINE** | `D̄(r,r') = Σ_{h∈r, h'∈r'} D(h,h') = δ_{rr'}·μ_Ẑ(r)` | paper 29 §4.3's load-bearing hypothesis 2 (*decoherence of the queried record algebra*) with §3.1's pushforward supplying the atom masses.  The coarse-grained functional is **diagonal** and its diagonal is the record measure.  **The only one of the three that is a stated condition of the parent paper** |
| **block** (stricter bound) | `D(h,h') = 0` for **every fine pair** with `record(h) ≠ record(h')`, plus block traces | implies the faithful condition and is far stronger: it **forbids by hand, one level down, the cancellations coarse decoherence explicitly permits** |

The choice is D50's pattern recurring one level up, and unlike D50's it is
**settled by reading the parent rather than by postulate**: paper 29
states one of the three, and this section is written at that one.  What
remain genuine form choices, labelled at every use: C3's lower-depth
reproduction, and the **record functor** — `canon` was chosen, and a
coarser or finer functor changes which pairs are within-class at all.

**One structural fact gives C3 its content and then leaves something
over.**  The record functor **does not commute with taking prefixes**:
`canon` identifies two histories when they are two serialisations of one
labelled event DAG, and two such serialisations have *different*
prefixes, so the depth-`D` record partition is not the pullback of the
depth-`(D−1)` one and C1 at depth `D` carries no C1 at depth `D−1`.  The
splitting is **partial** — which is exactly why coherence can survive at
all.  Also gated: **no two siblings share a record**, zero exceptions.

> **`[EXACT]` RESULT 1 — CONSISTENCY DOES NOT STRUCTURE COHERENCE.**
> Under the faithful reading the record demands force **no** within-class
> coherence to zero — at any depth, in any variant.  `cohdim = coh` in
> every one of the ten generically-built configurations and at every
> structurally-measured depth 2–5.  Coherence is **permitted everywhere
> and priced nowhere**, including between histories whose parents carry
> *different* records.  The classical member is **interior**, so C2 never
> binds; and the whole table is **measure-independent**.

**The faithful table** (`arank` = the constraint rank on the
antisymmetric block):

| `D` | C4 | C3 | vars | rows | rank | **dim** | coh | **cohdim** | arank |
|---|---|---|---|---|---|---|---|---|---|
| 2 | off | one | 528 | 297 | 296 | **232** | 9 | **9** | 268 |
| 2 | off | full | 528 | 298 | 296 | **232** | 9 | **9** | 268 |
| 2 | on | one | 146 | 297 | 88 | **58** | 4 | **4** | 60 |
| 2 | on | full | 146 | 298 | 88 | **58** | 4 | **4** | 60 |
| 3 | off | one | 15,576 | 3,846 | 3,845 | **11,731** | 134 | **134** | 3,739 |
| 3 | off | full | 15,576 | 3,868 | 3,865 | **11,711** | 134 | **134** | 3,754 |
| 3 | on | one | 3,968 | 3,846 | 1,006 | **2,962** | 35 | **35** | 900 |
| 3 | on | full | 3,968 | 3,868 | 1,013 | **2,955** | 35 | **35** | 902 |
| 4 | off | one | 476,776 | 52,711 | 52,666 | **424,110** | 1,491 | **1,491** | — |
| 4 | on | one | 119,592 | 52,711 | 13,329 | **106,263** | 390 | **390** | — |

Beyond depth 4 the faithful system's row count is quadratic in the
record-class census (49,141 class-pair rows at depth 4, 648,091 at depth
5), so it is measured there by an **exact structural identity** instead
of by elimination.  Every variable is an unordered pair of histories; the
C1 rows partition the variables by the pair's **record pair** and the C3
rows by the pair's **parent-record pair**, so the coefficient matrix is
the incidence matrix of a bipartite graph whose vertices are rows and
whose edges are variables:

```
    rank  =  (#C1 rows) + (#C3 rows) − (#connected components)
```

exactly — integer arithmetic, no elimination — and `dim(rowspace ∩
coherence-span)` is a second incidence rank on the same components.
**Cross-gated against generic rational elimination at depths 2, 3 and 4,
where both are computable: agreement everywhere.**

| `D` | vars | rows | components | rank | **dim** | coh | **cohdim** |
|---|---|---|---|---|---|---|---|
| 2 | 528 | 297 | 1 | 296 | **232** | 9 | **9** |
| 3 | 15,576 | 3,846 | 1 | 3,845 | **11,731** | 134 | **134** |
| 4 | 476,776 | 52,711 | 45 | 52,666 | **424,110** | 1,491 | **1,491** |
| 5 | 13,941,840 | 697,232 | 861 | 696,371 | **13,245,469** | 15,058 | **15,058** |

**The two bounding readings**, pinned configuration (C4 on, C3
one-step) / full form space (C4 off), for the record:

| `D` | **sum** dim (C4 on / off) | **block** dim (C4 on / off) | **block** cohdim (C4 on / off) |
|---|---|---|---|
| 2 | 136 / 499 | 0 / 4 | 0 / 0 |
| 3 | 3,938 / 15,469 | 30 / 120 | 13 / 50 |
| 4 | 119,487 / 476,379 | 335 / 1,332 | 189 / 744 |
| 5 | 3,487,199 / 13,940,389 | 3,002 / 11,944 | 2,032 / 8,074 |
| 6 | 97,342,324 / 389,325,439 | 25,578 / 102,072 | 19,847 / 79,168 |

Two structural facts about them, with their scope.  **(i)** Under the sum
reading with C4 off the constraint rows are linearly independent at every
depth (rank = row count `29, 107, 397, 1451, 5121`), which is exactly why
that reading **cannot reject any right-hand side at all**.  **(ii)** Its
dimension is essentially the whole space — 97,342,324 of 97,343,616 at
depth 6.  *A demand that does not ask the algebra to decohere is,
dimensionally, almost nothing.*

**EXISTENCE, AND WHY IT IS WEAKER THAN IT LOOKS.**  The classical
diagonal functional `D = diag(μ_Ẑ(h))` satisfies C1 in **all three
readings**, C2, C3 in both readings and C4, in every configuration,
verified by exact residual against every row, and is **positive
definite** (smallest diagonal entry `1/16777216` at depth 6).  So the
pre-registered outcomes **F-I (empty)** and **F-IV (coherence forced)**
are both **excluded**, by one line.  But every coefficient in every row
is a positive integer and the measure appears **only on the right-hand
side**: rebuilt from scratch with a second measure `ν(h) = Π_k
1/|menu_k|` — strictly positive, exactly cut-consistent, **not**
record-constant (4,156 of 5,548 classes carry two or more `ν` values),
differing from `μ_Ẑ` on 34,374 of 34,375 histories — the **coefficient
matrix is identical entry for entry** in every configuration.

> **`[EXACT]` THE DE-LICENSING.**  Rank, dimension, coherence dimension,
> the singleton census and every antisymmetric rank are functions of
> exactly three combinatorial objects: the truncated history tree,
> `canon`'s partition at depths `D` and `D−1`, and the prefix map.
> **D49's `λ = 2` completion and D65's descent are load-bearing for no
> number in this section.**  The honest title of the dimension table is
> *what `canon` and the prefix map permit*, not *what the generated law
> admits* — and `diag(w)` works for **any** strictly positive
> cut-consistent weight `w`, including laws the corpus spent D49–D65
> excluding.

**THE WITNESS TO RESULT 1** (depth 3, faithful, C4 off, one-step): an
exact member built by perturbing `diag(μ_Ẑ)` along a kernel direction,
zero residual against all 3,846 rows, positive definite by strict
diagonal dominance:

```
   h  = ( ('p','A',v0,0), ('p','B',v0,0), ('r','A',{(A,v0,0)},{(A,v0,0)}) )
   h' = ( ('p','A',v0,0), ('r','A',{(A,v0,0)},{(A,v0,0)}), ('p','B',v0,0) )
   record(h) = record(h'),        mu_Zhat = 3/8192 each
   record(parent h) != record(parent h')
   t = 1/81920,   D(h,h') = 1/81920 != 0
```

The two parents **are** distinguishable at the previous cut and the
coherence survives anyway.

> **`[EXACT]` RESULT 2 — THE FIRST DYNAMICAL DEMAND ELIMINATES ALL
> COHERENCE.**  Write `D = diag(μ_Ẑ) + E` and impose
>
> ```
>     E(h,h')  =  μ(h) μ(h') · K(σ(h), σ(h')),    K symmetric, K(s,s) = 0
> ```
>
> — *the coherence excess is generated by the closed law's own state
> space*.  The classical member is `K = 0`, so **the demand is fair**: it
> excludes nothing this unit exhibits as existence.  Then
> **`cohdim = 0` at `D = 2, 3, 4` and `5`**, where C1–C4 alone left
> `0 / 50 / 744 / 8,074`.

The mechanism is a census, not a cancellation.  Push the block/one-step
split into *permitted* (parents record-identical) and *forbidden*
(parents' records differ) within-class pairs through D62's closed state
map `σ`:

| `D` | permitted pairs | on σ-state pairs | forbidden pairs | on σ-state pairs | permitted **and not** forbidden |
|---|---|---|---|---|---|
| 2 | 0 | 0 | 9 | 9 | **0** |
| 3 | 50 | 15 | 84 | 15 | **0** |
| 4 | 744 | 28 | 747 | 28 | **0** |
| 5 | 8,074 | 32 | 6,984 | 32 | **0** |

**Every σ-state pair that carries a permitted coherence also carries a
forbidden one.**  Every cross-class C1 entry and every off-block
singleton C3 row forces `K = 0` on its σ-state pair; by the census
nothing is left.  The permitted/forbidden geography is **not a function
of the closed law's state variables at all** — it is a function of the
serialisation labels `canon` identifies and the prefix map does not.

**SCOPE OF RESULT 2, and it is load-bearing.**  C5 is imposed **on top of
the BLOCK reading** — the stricter bound, whose entrywise rows force `K`
pointwise.  Under the **faithful** reading the cross-class rows are
*sums*, so they do not force `K` pointwise, and that computation **has
not been performed**.  It is residue 1.

> **`[EXACT, at the stated scope]` THE VERDICT.**  At two-actor
> delivery-free closed scope, on this layer, with `canon` as the record
> functor and one state-generation ansatz: **a paper-29-shaped functional
> level cannot be both STATE-GENERATED and COHERENT.**  The consistency
> cone is large and structureless; the first fair dynamical demand
> collapses it to the classical member.  Superposition must therefore
> either break state-generation — the excess is not a function of the
> closed law's own variables — or enter somewhere else: **transport
> scope**, a different record functor, a different joint of the map, or a
> different fair demand.  **One demand, one functor, truncation-bound;
> the demand's uniqueness is not established, and that is the unit's new
> residue.**

**THE PHASE COLUMN, DEMOTED AND THEN REVERSED.**  Write `D = S + iA`.
Any linear row whose coefficient function satisfies `c(i,j) = c(j,i)`
annihilates `A` identically, term by transposed term.  **Every**
sum-reading row is a sum over a product set `C × C`, hence swap-symmetric
**by construction** — so its antisymmetric constraint rank is zero at
every depth, *for any partition, for any measure, on any layer, without
computing anything*.  Gated by running the same product-set rows over a
partition with no relation to records (histories grouped by index mod 7)
with `ν` on the right-hand side.  **It is a tautology of a chosen row
shape and carries no information about records.**  And it reverses the
moment anything else is switched on:

* **the faithful reading sees `A`** — its rows have asymmetric supports
  (`r × r'`, `r ≠ r'`), and the antisymmetric constraint rank is **268**
  at depth 2 and **3,739** at depth 3 (`3,754` full-chain; `900`/`902`
  with C4).  **A record demand of paper 29's shape does constrain
  phases** — and still prices none of the within-class ones
  (`acohdim = ancoh` everywhere);
* **C2 sees `A`** — positivity bounds `|A_ij|²` by `D_ii D_jj − S_ij²`;
  on the **pinned** (block-reading) witness's own 2×2 block an imaginary
  entry of `9/2048` leaves
  determinant `3887/67108864 > 0` and one of `9/1024` gives
  `−1/67108864 < 0`.  *The linear system is phase-blind; the constraint
  set C1–C4 is not.*

**THREE DEFLATIONS CARRIED WITH THE RESULT**, because each strips
physics off a number a reader would otherwise over-read.

1. **The block reading's forcing identity is one-step-specific.**  Under
   block + one-step C3 a within-class coherence is killed **iff** the two
   histories' parents carry different records, by a **singleton** row —
   true, and it reproduces.  But the unit's own full-chain C3 breaks it:
   at depth 3, `pinned 84 / unpinned 50 / cohdim 41`, and at depth 4,
   `pinned 747 / unpinned 744 / cohdim 651`.  The missing dimensions are
   not coordinate forcings — they are linear relations **among free
   coherences**, i.e. exactly the cancellation the "one term, no
   conspiracy" story says does not happen.
2. **C4 is a tiny subgroup of the real symmetry group.**  For two
   depth-`(D−1)` histories with the same record, the map exchanging their
   children by matching records is an exact symmetry of the one-step
   system in all three conventions (0 non-symmetric rows; full-chain
   breaks it: 18 / 27 / 99).  Nine such transpositions with pairwise
   disjoint supports at depth 3 give a symmetry group of order **≥ 2⁹ =
   512** against C4's **4**.  "The renaming-invariant column" is **not a
   canonical quotient**, and the honest quotient shrinks every headline
   number by 4–15×.
3. **Dimension is not volume.**  The affine solution space is unbounded;
   the PSD body is not.  The **pinned** witness carries
   `D(h,h') = 1/8192` against an entrywise PSD ceiling of `9/1024` on
   that entry — **1/72 of the maximum**.  **Nothing here measures how much coherence a member may
   carry.**

Also gated, and it kills a filtration reading outright: **no within-class
pair agrees on its whole ancestor record chain** — the column is `0` at
every depth, because two serialisations of one DAG always differ in their
first event.

**CONTROLS.**  *Perturbed measure* — each depth-`D` record class's mass
in turn multiplied by `101/100`, feasibility decided **exactly** by the
syzygies: the true `μ_Ẑ` is attainable in every configuration; the
**faithful** reading rejects 23/23 at depth 2 and 84/84 at depth 3 with
C4 on *and* off, and the block reading rejects 23/23, 84/84, 313/313;
the sum reading with C4 off has **no syzygies at all** and can reject
nothing.  *(A weaker disjointness predicate — comparing a class's perturbed mass
with its own — reduces to `101/100 ≠ 1` and cannot distinguish a
discriminating constraint system from one that accepts every measure,
which the sum/C4-off system is; the gate is therefore the faithful
reading's response, not that predicate.)*  *Pure-diagonal comparator* —
`4 / 70 / 588` (C4 off) and `0 / 17 / 146` (C4 on) at `D = 2/3/4`:
**`μ_Ẑ` is one point of a classical polytope before it is one point of
any quantum cone**; the record demands do not even pin the per-history
weights.

**Explicitly NOT licensed (the unit's own list, observed here):**
*"the record instrument is the exact boundary of permitted coherence"*
and *"a record measure of this shape cannot see a phase"* — both
**withdrawn**, §0.3, §B10.15c; that any member computed here **is** the
action line's decoherence functional — the map is untouched; any
Hilbert-space ontology; *"the generated law is quantum"* or *"permits
superposition"* without the reading, the depth, the record functor and
the state-generation clause; *"the generated law admits a functional
level"* without the measure-independence clause; the dimensions as a
measure of **how much** coherence a member may carry; the coherence
dimensions as depth-free numbers — they are truncation dimensions; the
sum-reading dimensions as evidence of anything physical; *"C3 is paper
29's demand"* — it is this unit's construction; *"C4 is the layer's
symmetry group"*; the C5 result as depth-free, functor-free or
ansatz-free; anything at three actors, at transport scope, with delivery,
or beyond depth 6; and **D65's DC3(2) as discharged — it is not.**

**Residues.**  (1) **The demand's uniqueness**, and it is the sharpest
successor question in the segment: whether the *faithful* reading plus C5
also collapses (its cross-class rows are sums, so they do not force the
kernel pointwise, and this computation was not run), and whether *every*
generation ansatz does what this one does.  Both are computations, not
arguments.  (2) **The unit is a measurement, not a construction** — D65's
residue 1 is narrowed, not closed; building a functional level means
*deriving* one.  (3) The **record functor** is interpretive and one was
tried; the "transportable mechanism" of any geography claim is downgraded
to a one-functor conjecture, and a coarsening control would settle it.
(4) The **full equivariance quotient** under the order-≥ 512 group was
computed by the round and is not rebuilt here.  (5) **C2 is untested
where it could bite**: positivity removes no dimension only because every
record class has strictly positive mass; at a scope with a null record
class none of this transfers.  (6) **Volume** — a ceiling measurement is
a separate unit.  (7) **Truncation** — every dimension is a truncation
dimension; the patterns held at every depth 2–6 with zero exceptions,
there is no proof, and the pin declined to bet.  (8) Three actors,
transport, delivery — out of scope, as always.

### B2.12 The phase segment — the shelved amplitude, the holonomy identity, and the weld `[D71/D71b/D71c archaeology; D72, LOG #487 → #488 → #490; round 1 TERMINAL]`

*Sources: the three archaeology surveys `note-d71-phase-archaeology.md` (24 cited appearances, 8 reduction points, 5 attachment slots), `note-d71b-holonomy-phase-identity.md` and `note-d71c-spin2-archaeology.md` — surveys, not receipts, every number quoted from a committed file by path and line; `note-d72-weld-pin.md` (STRICT, frozen verbatim from D71b's pinnable-claim section before any code); `note-d72-weld-result.md`; `v10/code/d72_weld_exact.py` (**77 PASS / 0 FAIL**, 9 of them labelled as carrying no independent information, exit 0, 468 s) + `data/d72_weld_exact.out`; `v10/reviews/d72-round1-hostile-review.md` — REVISE, 5 MAJOR / 5 MODERATE / 6 MINOR, arithmetic verdict "I broke nothing in the arithmetic of grammar 1.  I broke the scope, the instrument, and the second grammar."*

§B2.11 counted the *space* of quantum layers.  This section is about the
one ingredient any of them would need and none of them exhibits: an
**argument** — a phase.  The corpus's position on it is unusual and is
stated first, because it changes what "open" means here.

> **The imaginary exponential is missing from v10.  It is not missing
> from the corpus.**

#### (i) The archaeology, and what it found `[EXACT / MEASURED, earlier version lines]`

**v7 paper 30 ran a dedicated complex-amplitude campaign**
(`p30_complex_amplitude_campaign.py`, 11/11).  Three results, all
receipted:

- the naive path-interference continuation is **FALSIFIED** — total
  variation moves `1.68e-5 → 0.611` across eight phase settings;
- a **complex decay constant** breaks dual conjugation, at error `1.82`;
- **the survivor**, at dual-conjugation error **exactly 0**:

  ```
  A(R) ~ e^{−K(E)} · e^{i Φ(O)}
  ```

  real decay on the **reversal-even** channel `E`, phase on the
  **reversal-odd** channel `O`, with reflection positivity given as the
  reason — *"odd directions cannot be real positive observables; they
  become positive as imaginary amplitude channels."*

**It was never lifted to a theorem, and v10 was built without it.**  Three
sibling facts sit beside it, un-reconciled: **v6 paper 7** Thm 7.1–7.4
*derives* `C` as the value space and uses positivity to select `U(1)` over
split-complex — the corpus's high-water mark on phase, cited nowhere in
v10; the submitted batch (**paper Va**) lists that same result as an
**INPUT**; and **v8 paper 2** proves the bit sits in `ker R`, i.e. the
records cannot *force* it.  Meanwhile **v6 paper 4**'s own gated receipt
returns **`FAIL-BORN`** for the real-only branch (*"a purely real Gibbs
tilt … is not the whole phase-sensitive ISP process"*), and v8 records
that positive real weights provably cannot produce the cancellation.
**v7 paper 42** defines the complex functional `D_D(U,V)` in `C` — paper
29's `D(α,β)` three version lines early — and declares *"the delay is
intentional"*; `v9/PLAN.md:211` scheduled the triage note; **it was never
written.**  The deferral was a descoping decision with **no evaluated
trigger**.

**And the phase already has a name in this programme.**  `isp/README.md`
:43–44 states the founding question — *"whether quantum interference can
be understood as the **holonomy of probability transport** itself"* —
operationalized at :87–115 as the reversal `AB` vs `BA`.  That question
and v7's odd channel are **not rivals**.  They are one object, proved in
two halves on pages that never met:

| half | statement | grade |
|---|---|---|
| **1** (v6 paper 7) | the retained holonomy of a **closed route pair** is `U(1)`-valued (Thm 7.1), and two-route interference **is** the loop-phase law `P = \|A\|² + \|B\|² + 2\|A\|\|B\|cos(arg B(loop))` (Thm D3, machine gap `2.8e-17`) | `[THEOREM]` |
| **2** (v7 paper 30) | *"dual reversal sends `O` to `−O`; therefore dual reversal sends `L` to its complex conjugate"* (`:2846-9`) — i.e. `Hol(γ^{−1}) = conj(Hol(γ))`, **the** defining transformation law of a `U(1)` holonomy, proved with a receipt and never once called holonomy | `[MEASURED, error exactly 0]` |

**The one missing weld `[SILENT]`:** v6's reversal reverses **transport
order** (`T_A T_B` vs `T_B T_A`); v7's reverses a **record's own order
relations**.  Nothing in the corpus establishes that these are the same
operation.  That identification is what D72 pins.

**And the gravity side of the same split** (D71c).  The corpus's old
"something 2" was never a group: it was `h^{ij}`, the inverse spatial
metric, hunted as the coefficient of the stochastic exchange curvature
(`stochastic-curvature-gravity-investigation.md` Gate 2, executed as v2
paper 10).  **v2 paper 10 Prop 10.6** is an all-order no-go: the
Born-squared real shadow keeps `|z₁|²` and `|z₂|²` — the metric
**diagonal** — and **provably loses** `h^{12} = Re(z₁ z̄₂)`, the relative
phase.  **v6 paper 5**: the response tensor's minimal determining datum is
the **oriented** closed-route holonomy (*"scalar work, magnitude-only
holonomy, and unoriented holonomy all forget the sign"*).  The algebra the
corpus owns twice and never stated: commutator of transports →
antisymmetric → **rotation/phase** (v6 p53); anticommutator → traceless
symmetric **rank-2** coupling to the spin-2 shear, symmetric fraction
`1.000` (v6 p54); and `(1/2){γ^i, γ^j} = h^{ij} I` (v2 p10).  **ODD =
PHASE, EVEN = METRIC.**  `SU(2)` has **no** corpus foothold: every gravity
"2" is tensor rank, component count or helicity; no gauge group appears in
any gravity paper; and on the generated line non-abelian composition is
**zero** — `ACT` commutes on all **170,820** pairs.

**Live erratum carried from D71:** the quarter law's `BC` is only the
**Cauchy–Schwarz bound**, saturated iff the relative pointer phase is
constant; v6 paper 7 §12's correction never reached paper 26,
`ARCHIVE-STATUS`, or v10 paper 18 (§C1).

#### (ii) The weld, tested `[D72; 77 PASS / 0 FAIL, exact rationals]`

The pin (frozen before code): *the order-dual `*` on record types
coincides with transport-order reversal `AB → BA` on the generated line's
own objects, and `A(R) ~ e^{−K(E)}e^{iΦ(O)}` is the `U(1)` holonomy of
`∏√q`-transport around delete-then-insert round trips — `A_D` its
log-modulus, `Φ(O)` its argument.*  Four falsifiers, `F2`/`F4` settling
the founding slogan negatively as publishable outcomes.

**The identification leg survives.**  `rev : LinExt(P) → LinExt(P*)` is a
bijection on all **6,464** histories (the canonical common carrier), and
on the **32** two-event histories `*` and `AB → BA` are the **same partial
map**, term by term.  On histories of length `≥ 1` they agree on **0** of
2,214 closed squares, so the coincidence is exactly one fixture wide.  In
the *labelled* sense the order-dual is **not** an operation on v10's
records — 1,264 of 1,558 classes have no in-family dual; the *order-type*
statistic is different and `k`-dependent (absent-dual odd orbits `0/1` at
`k = 3`, `1/2` at `k = 4`, **`4/4` at `k = 5`**, which is v7's own
five-record type).

**The holonomy leg dies at closed scope — and it is a THEOREM there.**

> **`[THEOREM]` (round-supplied, gated here).**  Let `h` be any history of
> the d42b3 placement grammar over any finite actor pool and let
> `e_A ≠ e_B` both be admissible at `h` with both orders admissible.  Then
> `q(e_A|h)·q(e_B|h·e_A) = q(e_B|h)·q(e_A|h·e_B)` — i.e. `A_D ≡ 0` — **at
> every depth.**

Six lemmas: **L1** past-locality (`q(e|h) = Q(e, D(e))`; 2,708 keys, 0
clashes); **L2** comparability `⟺` register overlap; **L3** disjoint ⇒
commuting (40,507 + 1,923 + 630 squares, 0 violations); **L4** an
overlapping closed square always contains an idle (23,464 + 516 + 96, 0
without one); **L5** idle inertness; **L6** the idle weight is the
constant `3/4` (68,750 / 19,767 / 6,868 pairs, spectrum `{3/4}`,
`(has_p, has_r)` never `(T,T)` or `(F,F)`).  Measured consistently:
**63,971** closed squares at bases `|h| = 0..5` all at ratio `1`, plus
3- and 4-actor arms.

> **THE SCOPE CLAUSE, and it is the decisive half.**  L1–L3 and L5 are
> structural.  **L4 and L6 are not.**  L6 holds because the
> propose-budget `1/4` and the arbitrate-budget `1/4` are **equal** and
> mutually exclusive in an actor's own view — **a budget coincidence of
> d42b3**, not a theorem about the grammar.  *The depth-free result must
> never be stated for "the generated line" without naming the grammar.*

**The normalised kernel was never flat.**  The menu mass `M(h) = Σ_e q(e|h)`
has spectrum **`{2: 5963, 5/2: 508}`** — so raw weights are not
conditional probabilities — and is class-constant on 1,565/1,565, so `q/M`
descends to records exactly as `q` does.  Its square ratio is exactly
`M(h·e_B)/M(h·e_A)`, spectrum **`{4/5: 220, 1: 1687, 5/4: 320}`**, and its
holonomy on the same 758-cycle record graph has **image `⟨5/4⟩ ⊂ R₊`** —
which is §B2.10's mass-ratio **coboundary**, re-derived here.  (The
*count* of non-trivial basis cycles is spanning-forest-dependent — 148
forward, 118 reversed, 175 in the referee's build — and is **not**
licensed as a number; the image group is.)

**And transport scope is CURVED.**  On d42b1 at `(A,B)` depth ≤ 4:

| | count | spectrum | kinds | delivery-bearing | shallowest |
|---|---|---|---|---|---|
| non-unit closed squares | **88 / 1,546** | `{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}` | `{(r,d): 68, (d,r): 8, (d,n): 6, (d,d): 4, (n,d): 2}` | **88 / 88** | total depth **3** |
| half-open (`A_D = ±∞`) | **40** (`AB`-only 28, `BA`-only 12) | support defect | `{(r,d): 12, (d,r): 4, (p,d): 16, (d,p): 8}` | **40 / 40** | — |
| `(A,B,C)` depth ≤ 3 | **12 / 1,554** | `{1/2: 12}` | `{(r,d): 12}` | 12 / 12 | depth 3 |

The minimal witness, in full:

```
  h  = [('p','A',V0,0)]
  eA = ('r','A',{(A,V0,0)},{(A,V0,0)})     # arbitrate own proposal
  eB = ('d','A','B',V0)                    # deliver V0 to B
  q(eA|h)=1/4 , q(eB|h.eA)=1/8  ->  dP_AB = 1/32
  q(eB|h)=1/4 , q(eA|h.eB)=1/4  ->  dP_BA = 1/16
  dP_AB/dP_BA = 1/2 ,  A_D = −log 2
```

The mechanism is a **menu denominator**: arbitrating first creates a
second held value, doubling `A`'s delivery menu, while delivering first
does not change the arbitration menu.  Grammar 2 fails the theorem's
hypotheses exactly as the scope clause predicts — idle spectrum
`{1/2: 7738, 3/4: 200}` against grammar 1's single value, and **533 of
1,073** comparable closed squares with **no** idle member.

> **THE INSTRUMENT IS BLIND BY CONSTRUCTION, and this is the structural
> point.**  A square closes at record level **exactly when its two events
> are register-disjoint** — of 2,227 closed squares the record-deletion
> graph closes on **1,355 of the 1,355 disjoint** and **0 of the 872
> overlapping**.  So the locality argument and the loop census have the
> *same* domain and the *same* blind spot; **0 of 88** transport defects
> close at record level; and a negative control that perturbs an edge the
> graph already contains cannot detect that class of blindness.  Where the
> instrument can see, `μ` is an exact gradient (2,322/2,322 up-edges carry
> `φ(C₂)/φ(C₁)` with `φ = μ`), which is why every cycle there is trivial —
> one fact, not 758.

**The falsifier board.**  `F2` **FIRES** — at closed scope, on grammar 1,
for the raw weight, with a theorem behind it and three measured scope
clauses (grammar, instrument, weight).  `F4` **FIRES**, on two
independent objects: the normalised grammar-1 connection (`⟨5/4⟩ ⊂ R₊`)
and the raw transport squares (`{1/2, 2/3, 3/2, 2}` plus `±∞`).

> **The result, exactly.**  **Everything exhibited is `R₊`-valued.  A real
> holonomy of probability transport exists on this substrate and it has
> **no argument**.  No `U(1)` part has been exhibited anywhere in this
> programme.**  The founding slogan is refuted **in `F4`'s own
> direction** — not by the absence of a holonomy but by the presence of a
> phaseless one.

**And the transport holonomy is a NEW object.**  The values `2/3` and
`3/2` lie **outside `⟨5/4⟩`**, so it is not the D65 coboundary family.
That is the first evidence in the corpus that a transition class here
might not be a coboundary at all.

**Consequence for §B2.11.**  D71's phase-slot `+1` is **forced** — for the
`∏√q` lift D42b4 actually defines, on the raw budget amplitude, at closed
scope, where the record-graph holonomy is trivial so no other section of
the phase bundle is reachable by transport.  **For nothing wider.**

#### (iii) Licensed, and not `[D72]`

1. `[THEOREM, depth-free, grammar d42b3]` raw closed-scope exchange
   flatness, with the L4/L6 budget-coincidence clause; `[MEASURED]` on
   bases `|h| ≤ 5` at `(A,B)`, depth ≤ 4 at `(A,B,C)`, depth ≤ 3 at
   `(A,B,C,D)`.  **Explicitly FALSE for d42b1.**
2. `[EXACT]` `*` and `AB → BA` coincide as partial maps on two-event
   histories and on nothing larger; `A_D` is odd under `*` on the common
   carrier in the degenerate sense `0 = −0`.
3. `[MEASURED, depth ≤ 5, two actors]` the normalised kernel's holonomy
   image is `⟨5/4⟩ ⊂ R₊`, square spectrum `{4/5, 1, 5/4}` — D65's
   coboundary.
4. `[MEASURED, exact]` the transport-scope census above, every defect
   delivery-bearing, none closing at record level.
5. `[EXACT]` `2·e^{−3/32}` equals paper 30's published constant to all 32
   digits, and `E = 3` is the argmax over `E ∈ 0..3999` — so **the `1.82`
   is a constant of the ansatz** (§0.3), and the anchor that reproduces
   it on the 131,526-record universe is a **port fidelity check**, not
   evidence about records.
6. **Not claimed:** that the generated line is flat without naming the
   grammar, the scope and the weight; that the normalised defect is
   anything but D65's decided coboundary; that any `U(1)` holonomy has
   been exhibited anywhere; that the record-deletion-graph census is a
   sufficient instrument for exchange holonomy (it provably is not); that
   v7 paper 30 is wrong (it is not — it is narrower than the archaeology
   read it).

**Residues, ranked.**  **(1) THE HANDOFF — characterise the transport
holonomy** (D74): what carries it at record level (the defective squares
do not close, so either the right object is a delivery-aware record
functor or the holonomy is genuinely sequence-level); **is there an
odd-sector `U(1)` part** — nothing here exhibits a phase and `F4`'s own
wording makes that the interesting direction; and is the transport defect
**a coboundary or a genuine `H¹`**, the `2/3` and `3/2` values being the
first reason to doubt the former.  (2) L6a's induction (an actor's
holdings form a chain with one live member) is verified exhaustively, not
machine-proved.  (3) The **`±∞` squares are a different animal** — a
*support*-level defect, 100 % delivery-borne, and no holonomy formalism in
the corpus handles them.  (4) `O`'s sign-definiteness is unexplained and
survives to `k = 5` (`{−1: 384, 0: 754}`).  (5) One structural constraint,
new: **`A_D = 0` along the one-dimensional commit path**, so any
non-trivial phase must live **transverse** to commit order.

---

## B3. Cuts, foliations, views, transport

*Non-technical twin: Part A, chapter A3.*

### B3.1 Cuts, foliations, canonical classes

A **cut** is a slice through a record — a "now".  A **foliation** is a
sequence of cuts, i.e. **one linear extension** of the record's causal
order.  There is no preferred slicing.

**Causal order is physical; incomparable order is GAUGE.**  Two histories
differing only by the order of incomparable events are the same physical
record.  A **canonical class** is a history identified up to that gauge;
the depth-4 two-actor family's 1,191 histories fall into **427** classes
(§B4.1).

**Foliation-invariance** is therefore the relativistic demand on any
candidate law: the law must be a function of the record, i.e.
**class-constant**, equivalently its chain products must agree across
*every* linear extension of *every* history.  This is demand (b) of the
completion problem (§B6.2), and it is the demand the naive normalizer
violates.

### B3.2 Views, own views, and the lag

A **view** is the sub-record an observer has witnessed; the **full view**
at `h` is everything in `h`; an **own view** is the sub-history one actor
has witnessed.  **Actors act on their own views, which LAG the full
view.**

Read from the committed layer rather than assumed (D51 pin §2):
`admissible(acts, e)` builds `view = View(acts + [e], pred, pred[j])` —
**the candidate event's own causal past**.  For an idle `('n', a)` that
is `a`'s bare **noop cone**; for `('p', a, b, x)` and `('r', a, C, W)` it
additionally pulls in the wires the event touches, which is exactly why
the menu view can exceed the cone.  And the menu reads that view through
**exactly four projections**:

```
view.holdings(a),  view.superseded,  view.live / view.props,  view.components()
```

`sigma` (§B6.9) records exactly those four kinds of data on the **full**
view.

**The lag, measured `[EXACT]`.**

- D46a (its own round): the menu view strictly exceeds the noop cone on
  **1,016 of 12,942** actor-histories at depth ≤ 5 (**7.9%**), by at most
  **4** events, and in **ALL 1,016** cases the extra events are
  **OPPONENT-AUTHORED**.  The menu view is idempotent (`0/12,942`).
- D51 MV0 reproduced it independently: the menu view exceeds the cone in
  **2,032** `(actor, candidate)` pairs against **19,400** equal, max 4
  extra, **every** extra opponent-authored.
- D51 MV1 refuted its own pre-registered prediction that only idles lag:
  **every event type lags.**  Equal / total = `n` 4,606/12,942,
  `p` 5,636/12,916, `r` 3,820/8,516.

**D51 MV2 — MONOTONICITY FAILS, and this is the load-bearing negative.**
The cone-level pair `(has_p, has_r)` is **not** a function of the
full-view pair: full-view `(False, False)` maps to **both** `(False,
True)` and `(True, False)`.  **A smaller view can yield MORE options.**

**The mechanism is INVISIBLE SUPERSESSION, and the natural guess is
refuted.**  The guess — `prop_options_in_view` excludes a base the actor
already holds a live proposal on, so a view *missing* that proposal
*includes* the base — **can never fire**: an actor's own live proposals
are always inside its own cone (Lemma 4(c) of the §B6.13 proof).
Measured over **68,750** `(history, actor)` pairs at depth ≤ 6: the cone
yields strictly more options in **4,828** of them, and of the **9,656**
excess options **9,656 are caused by a missed supersession** and **0 by a
missed own proposal**; an actor's own live proposals differ between cone
and full view in **0 / 68,750**.  So the mechanism is that a view which
has not seen an arbitration still counts that arbitration's base as
alive.  The same mechanism reappears twice more, named both times: as the
self-arb case of §B6.13's rigidity lemma, and as **row R2′ of the update
table** (§B6.13b), where the very same **9,656** excess options turn out
to *be* the propose-on-a-dropped-base row.

> **Any depth-free argument built on "the lagged view sees a subset" is
> therefore unsound**, which rules out a whole family of attempts
> including D51's own pinned route (§B10.3).

**What D51 measured, and the direction it does NOT run.**  Equal full-view projections imply equal
menus with exact weights across all **6,471** histories over **209**
distinct projection keys, zero violations.  But the projections
**REFINE** `sigma` rather than being determined by it — **209 projection
keys against 32 states** — so the inference *"since `sigma` abstracts
those projections, menus are sigma-determined"* is **inverted** and is
withdrawn.  Menu-determinacy from `sigma` is established instead by
§B6.13's closed form, which goes through `sigma` **directly** and never
through the projections.  D44a already had transition determinism,
stronger and two depths deeper, so the projection-level version adds
nothing there either.  D51's durable content is **three refutations**
(§B10.3), not a reduction.

### B3.3 Menus run on per-actor views at transport scope

The B1 probe (D56, LOG #432; **ADVISORY**, with its two load-bearing
claims independently verified before acceptance) settles what a menu is a
function of at transport scope.  Read off `d42b1_transport_exact.py`:

| candidate | view `admissible()` builds | extra reads |
|---|---|---|
| `('p',a,b,x)` | `O_a` (a's own wire past, inclusive) | — |
| `('n',a)` | `O_a` | `admissible_arb_ckeys` on the **FULL** view |
| `('d',s,r,v)` | decision uses `own_view(s) = O_s` | — |
| `('m',a,pk,w)` | `O_a` | `admissible_arb_ckeys` (FULL) |
| `('r',a,C,W)` | the **join** `⋃_{a'∈props(C)} O_{a'}` | — |

So the object a menu is a function of is not one view but the **join
semilattice of own-views**, `V_S = View(h, pred, ⋃_{a∈S} O_a)` for
`∅ ≠ S ⊆ actors`.  At two actors that is `V_A`, `V_B`, `V_{AB}` (and
`V_{AB}` is the full view, since every event carries an actor register).
Lattice completeness is `[MEASURED to depth 5]`: **243,768** candidate
views compared against the join predicted for their actor set, **0
exceptions**, and **0** occurrences of the one structural escape
identified (an arb event's new-version register joining to an earlier arb
that minted the same name — a "renewal" collision).  **Not proved
complete at all depths** (caveat C3).

**THE WITNESS `[verified]`.**  The full-view four-projection design is
**too coarse** at transport scope: **3,656 violations over 30,454**
equal-sigma pairs.  Minimal counterexample as printed (idle padding
trimmed):

```
W1 = [ p(B, v0, 1), selfarb(B) ]
W2 = [ p(B, v0, 1), selfarb(B), d(B→A, v0) ]
```

Both have **identical full-view four projections** — the delivery moves
no holding (A already holds `v0`), mints nothing, supersedes nothing.
The menus differ:

| entry | W1 | W2 |
|---|---|---|
| `('n','A')` | `1/2` | `3/4` |
| `('p','A',w0,0)`, `('p','A',w0,1)` | `1/8` each | **absent** |

Before the delivery, A's own view has not seen `v0` superseded, so A can
still propose on it; after, it has.

> **The full view cannot see a delivery that only transports knowledge,
> and transport pricing is exactly about knowledge.  A delivery moves
> only WHO KNOWS, and changes the menu.**

D51's reduction is thereby confirmed **d42a-scoped**, exactly as its own
scope line said.

### B3.4 Sender-wire backflow: a delivery joins BOTH ways

Carriers `{s, r}` means the join is symmetric in the poset.  The
consequence was discovered destructively (D54 Stage 2, gated as negative
exhibit N1): **the sender's wire absorbs the receiver's accumulated
past.**  After B delivers into an accumulator holding A, every later send
from B carries `{A, B}`.  The referee's independent verification of the
mechanism: B's per-initiator trace family is `{}, {B}, {A,B}` — literally
`regs_of(d) = {s, r}`.  The per-sender send-traces form a chain: **the
Dilworth gate (§B7.3) biting its own construction.**

This is why §B8's architecture sends only into *empty* receivers.

### B3.5 Foliation-invariance, and one negative about it

Demand (b) of §B6.2 is the formal statement.  Two facts worth carrying:

- The **direct** test is the linear-extension sweep, not the diamond
  proxy: the diamond check's separating content is class-constancy, not
  harmonicity (§B4.3).  D49's gate D3 therefore compares completed chain
  products **across all 1,191 linear extensions of all 427 canonical
  classes** at depth ≤ 4 `[EXACT]`.
- **`[MEASURED]` Foliation-invariance adds nothing to depth-stationarity**
  (D50 SF4): imposing demand (b) at the `Z` level on top of
  depth-stationarity more than doubles the constraint count — **25 vs 16,
  210 vs 109, 1,374 vs 610** at truncation depths 2/3/4 — and leaves the
  completion dimension **exactly unchanged**.  **The residual freedom is
  not gauge freedom**, and the obvious rescue ("add gauge invariance and
  it will collapse") is closed off by measurement.

---

## B4. The cut complex and the flatness ladder

*Non-technical twin: Part A, chapter A4.*

### B4.1 The complex `[EXACT]`

The **cut complex** is the graph whose vertices are cuts and whose edges
are single admissible steps.  At the worked scope — the **depth-4
two-actor family** of d42a:

- **1,191 histories** (cumulative; **976** at the layer — §B2.5);
- **427 canonical classes**;
- **202 canonical diamonds**.

The class census by depth is `1 / 6 / 23 / 84 / 313` (summing to 427), so
the **interior** classes number `1 + 6 + 23 + 84 = 114` and the
**terminal** classes number **313**.  Interior histories (depth ≤ 3)
number **215**.  These five numbers recur throughout §B6 and it is worth
holding them together.

### B4.2 Diamonds, and what they are for

A **diamond** is the smallest loop in the cut complex: two elementary
steps performed in either order, arriving at the same cut — a commuting
square.

Diamonds test **path independence**.  If you assign numbers to the record
and want them to define a consistent potential, traversing any diamond
both ways must agree; since diamonds are the smallest loops, agreement on
all of them is the whole condition (flat on all 2-cells ⟹ a potential
exists).

The existence of a globally consistent `Z` is the **discrete
Tomonaga–Schwinger integrability condition** for the record functional:
per diamond the two-path constraint is solvable and underdetermined; the
global question is whether the ladder excess of §B2.7 is a **coboundary**
on the cut complex.  §B2.10 answers the corresponding question at the
level of the *normalized kernel*, exhaustively and in the affirmative:
the order defect is exactly the coboundary of the per-state menu mass,
which is why a completion factoring through `(depth, sigma)` annihilates
it and why no completion is forced to.

### B4.3 The flatness ladder, and the telescoping theorem

Gated on all 202 canonical diamonds `[EXACT]` (paper 30 §5.5):

| level | diamond violations |
|---|---|
| weight (`mu` factor products) | **0** |
| naive cut-normalized | **36** — exactly the census of §B6.3 |
| gradient-completed | **0** |

**`[THEOREM, EXACT]` The gradient leg's flatness is a telescoping
theorem.**  *Any* cut-attached, class-constant `Z` gives flat diamond
products identically, because the chain product telescopes to boundary
values.  The receipt gates this with an **arbitrary non-harmonic
class-constant probe passing 0/202**.

> **Therefore the separating content is CLASS-CONSTANCY — gauge
> invariance of the completion — and NOT harmonicity.**

A sequence-attached, non-class-constant `Z` does fail: **51 failing
diamonds** for the receipt's deterministic sequence probe (the count is
representative-dependent, because such a probe is gauge-breaking by
design, unlike the class-invariant 36) `[EXACT]`.

`[MY READING]` This defuses a trap the flatness result would otherwise
set.  "The completed measure passes the action-level check the naive
normalization fails" is true and says less than it appears: flatness buys
*gauge invariance*, not *harmonicity*.  Do not read the flat gradient leg
as evidence that the gradient completion is the right one.  For the same
reason D49's foliation gate (all 1,191 linear extensions) matters more
than its diamond gate: **the extension sweep is not a proxy for
anything.**

### B4.4 Three senses of "diamond", disambiguated

Following the warning in `THE-COMPLETION-DICHOTOMY.md` §1.5:

1. **Cut-complex cells** — the **202** of this chapter.  Elementary loops
   in the space of cuts.
2. **Paper 3's marked-support amalgamation figure**
   (`relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md`),
   where the result is that amalgamation is *composition*, not carrier
   birth.
3. **Paper 29's action-level "flat squares on diamonds"**
   (`relativistic-isp-v10-paper29-where-the-action-cocycle-lives.md`) —
   flatness of an action-like functional; §B4.3's three-level ladder is
   the generalization of that check onto this object.

And the fourth meaning, from outside: **the 202 are NOT Alexandrov
intervals** between two events.  Different job, same shape.

**"Flat" is overloaded on the same objects, and §B2.12 adds a sense.  All
four, with their carriers:**

| sense | object | carrier | status |
|---|---|---|---|
| **diamond flatness** | a cut-attached, class-constant `Z` closes every 2-cell | the cut complex | `[THEOREM]` by telescoping — it certifies **gauge invariance**, not harmonicity (§B4.3) |
| **chart flatness** | the transition class is a coboundary, `H¹ = 0` | the atlas nerve over records | `[MEASURED]` on three substrate families, five port conventions, three routes: **trivial every time** (§B8.8, §B8.9) |
| **transport flatness** | `A_D = log dP_AB/dP_BA ≡ 0` on closed exchange squares | histories / sequences | `[THEOREM]` at closed scope on the placement grammar, with a **budget-coincidence** clause — and **FALSE at transport scope** (§B2.12) |
| **flat spacetime** | Minkowski-sprinkling likeness | — | the destination's explicitly **withdrawn** target (§D1) |

The third is the one that carries physics, and the third is the one that
fails.  A sentence about "flatness" that does not name its carrier is on
the blacklist (§0.3).

---

## B5. The sky instrument

*Non-technical twin: Part A, chapter A5.*
*Sources: `note-d47-sphere-rung-{pin,result}.md`, `v10/code/d47a_sky_instrument_exact.py`, `v10/code/d47b_transport_skies_exact.py`, `v10/code/d53_sky_capacity_exact.py`, `v10/reviews/d47-round1-hostile-review.md`.*

### B5.1 The three committed definitions, as the code defines them

Committed **before any run** (the D46e lesson).  From
`d47a_sky_instrument_exact.py`, `sky(C, e, kind, depth=SKYB_DEPTH)` with
`SKYB_DEPTH = 2` (pin §3), where `C` is the strict causal relation:

- **SKY-A (cover sky).**  `fut = {f : C[e][f]}`;
  `dirs = {c ∈ fut : ¬∃k, C[e][k] ∧ C[k][c]}` — the **covers** of `e`;
  `rows = { {c ∈ dirs : c = f ∨ C[c][f]} : f ∈ fut }`.
- **SKY-B (antichain sky at a committed depth).**  With `h` the global
  height function, `dirs = {f ∈ fut : h[f] − h[e] = depth}`; rows as
  above.
- **SKY-C (the dual past sky).**  `pas = {f : C[f][e]}`;
  `dirs` = the covers of `e` downwards; `rows` built dually.

A **direction** is a member of `dirs`; a **trace** (equivalently a
**shadow**) is one row — the set of directions at or below a given
future (or past) event.  Note the **reflexive** form (`c = f ∨ …`): the
round corrected an earlier strict-down-set wording, and the reflexive
form is the instrument's actual definition, so the Dilworth proof of
§B7.3 is stated for it.

**A definitional caveat, recorded in the round rather than hidden:**
SKY-B's directions do form an antichain (equal global height implies
incomparability), but *"height difference d"* is **not** *"distance d from
e"*.  That is a caveat, not an error.

**Reading-relativity is structural, not incidental.**  SKY-A, SKY-B and
SKY-C disagree **materially** (SKY-A never reached decidability in D47b
while SKY-B did at width 4 and SKY-C at width 5), so **every
single-definition result is READING-RELATIVE and says so.**  *Which sky
definition is physically privileged* is an open residue.

### B5.2 The separator, constructed not cited (SG0) `[EXACT]`

- **Arcs on 4/5/6/7 points shatter 3 and NEVER 4.**  (Four points in
  cyclic order admit no connected arc holding the 1st and 3rd but not the
  2nd and 4th.)
- **Caps on an exact-rational tetrahedron on the unit sphere** (Fraction
  norms exactly 1) realize **all 16 subsets** by exact rational
  halfspaces, **including the hard opposite-edge case**, exhibited with
  its certificate `u = (1,1,1)`, `t = 1/3`.

Hence **a shattered 4-set proves a system is not an arc system** — by
construction, not by citation.

**The one-sidedness doctrine (pin §2), binding on every statement in the
line:** shatter-4 found ⟹ not arc-realizable ⟹ not a 2+1 sky *under the
committed definition* (a certificate, statable); the **absence** of
shattering is **not** evidence of 2+1.  **No statement of the form "the
sky IS a circle" may be made.**

### B5.3 The demotion of circular-ones `[EXACT]`

The corpus had planned a second, two-sided instrument: **circular-ones**,
exactly decidable for arc-realizability.  Run as a control on
exact-rational `M^{2+1}` records at a scale where it decides (554
decidable `(base event, sky definition)` pairs across N = 40/80/160):
zero shattered 4-sets, as the separator predicts — **but circular-ones
rejected 121 of 554 genuine 2+1 skies as non-arc systems.**

> **A discrete sky of real Minkowski is NOT generally an arc system.**
> Arc-realizability is therefore not a usable proxy for 2+1; instrument 1
> is **DEMOTED to a diagnostic**, and everything downstream rests on
> **shatter-4 alone**.  Any framing of circular-ones as "the primary
> two-sided test" is **WITHDRAWN**.

Later recounts sharpen it further: the D54 round recounted **218/397**
genuine 2+1 SKY-B skies non-arc — a **majority** `[REFEREE-CARRIED]` —
and the D55 round recorded a further recount one rung down (17/453 more
genuine 2+1 skies certified non-arc).  The direction is consistent: the
premise class *"discrete d-dimensional skies are continuum trace
systems"* is refuted as a premise, and this is exactly the arrow that
BLOCKER 1 of both the D54 and D55 rounds retired (§B8.5, §B10.10).

**SG3 was vacuous, and that is gated as its own finding.**  D46c's
committed `W3_CERT` (18 exact `M^{2+1}` points, read verbatim, max
denominator 64) yields skies of at most **2** directions against the 4 the
test needs: decidable at **0 of 54** base-event/definition pairs.  The
original consistency check carried **zero information**, and the receipt
says so in a dedicated gate rather than letting the pass read as
confirmation.

### B5.4 The disjoint-row lemma, and the capacity condition

*Sources: `v10/code/d53_sky_capacity_exact.py` (8 PASS / 0 FAIL after batch-round repair); `v10/reviews/batch-round1-d50-to-d60.md`, D53 BLOCKER 1 and MAJOR 1/2.*

**The requirement, stated correctly.**  Shattering a set `S` requires all
`2^{|S|}` traces **restricted to `S`**, and therefore requires a row
`r` with `r ∩ S = ∅` — **a row DISJOINT FROM `S`**, not a row that is
empty.  The two coincide only when `S` is the *entire* direction set.

> **`[THEOREM, hypotheses stated]` For a finite poset whose order is
> **reflexive** and **transitive**, every SKY-A and SKY-C trace is
> non-empty; hence such a sky can never shatter its FULL direction set
> (`k = |dirs|`).**  That is the whole of what the empty-trace argument
> buys.

The stronger reading — *no empty row ⟹ cannot shatter anything* — is
**false**, and the counterexample is one line, decided by the committed
instrument's own `shattered_set`: `rows = [{0}, {1}]` on `cols = [0,1]`
has no empty row and shatters the 1-set `(0,)`.  At `k = 4` the same
mechanism runs on a genuine finite poset (base, five covers, one event
above each non-empty subset of four of them; 21 events, transitivity
checked exhaustively): 5 directions, 16 distinct rows, **no empty row**,
and `shattered_set` returns the shattered 4-set.  **A fifth direction's
own trace `{c5}` supplies the empty trace *on the 4-set* while being
non-empty as a row**, and that mechanism is available at every width ≥ 5.

**And it happens in Minkowski `[REFEREE-CARRIED, batch round 1]`.**  On a
genuine exact-integer `M^{3+1}` sprinkling (`N = 300`, all points
distinct, transitivity verified), through the committed `sky()` /
`shattered_set()`: **SKY-A shatters 4-sets at 24 base events; SKY-C at
30** — with `EMPTY TRACE = False` at those events.  SKY-C shatters
**3-sets at 49 of 117** capable base events on the committed lattice
records, with zero empty rows anywhere.

> **THEREFORE: SKY-A and SKY-C are LIVE readings**, and the claim that
> only SKY-B can fire is **withdrawn**.  **Residue 2 — which sky reading
> is physically privileged — REOPENS**, and it now matters more than
> before, because §B5.7's discriminator is sharpest under SKY-A.

**The capacity condition, corrected.**  D47's gate — `|directions| ≥ 4`
and `|rows| ≥ 2` — is genuinely **necessary and not sufficient**, and
that correction stands: a zero over a stratum too poor to fire is not a
measurement.  But the empty-trace clause **false-negatives** and must
come out of the necessary condition.  The honest condition is the first
two clauses: **`≥ 4` directions AND `≥ 16` distinct traces.**

**The corrected census.**  Of the 415 skies once written off as
structurally incapable, **144 were genuinely capable** — a **2.8×**
reduction in what counts as testable, not the 10.7× a too-strong
condition produced.  With the empty-trace clause dropped, the same 554
pairs admit **69** under SKY-A and **52** under SKY-B.

> **What was right and what was wrong, kept apart.**  Right: capacity
> must be gated before a zero is read as a negative.  Wrong: the
> condition, its stated structural reason, and the exclusion of two
> readings that do in fact fire.  See §A10.10b / §B10.10b.

**Untouched by any of this:** D47a's constructed separator (arcs shatter
3 and never 4; exact-rational caps shatter 4); the instrument validation
on synthetic systems; the demotion of circular-ones (§B5.3), which never
used shatter-4; and D47b's actor-width result (§B5.6), which measures sky
**size** and does not invoke shattering.

### B5.5 Capacity in Minkowski: density, not count `[EXACT]`

**Point count and density must not be confounded.**  If the box extent is
allowed to scale with `N`, volume grows as `~4N³` while the point count
grows linearly and the sprinkling gets *sparser* as `N` rises — two
variables moving in opposite directions.  Both columns are therefore
reported side by side and **neither is quoted alone**:

| N | growing box: max `\|SKY-A\|` | fixed box (160): max `\|SKY-A\|` |
|---|---|---|
| 20 | 3 | **4** |
| 40 | 8 | 7 |
| 80 | 10 | 9 |
| 160 | 14 | 14 |

Growing box: first decidability at `N ≈ 40` (decidable base events
0/23/58/120).  Fixed box: **decidable already at `N = 20`.**
**The correct Minkowski variable is DENSITY, not point count.**

### B5.6 Capacity in the record: actor width `[MEASURED]`

D47b, 400 deterministic deep walks per width to depth 20:

| width | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|---|
| max `\|directions\|` | 2 | 3 | 4 | 4 | 4 | 4 |

**At width 2 the sky stays at 2 no matter how deep the walk runs.**

> **Two different scaling variables: Minkowski buys sky size with
> DENSITY; transport buys it only with ACTOR WIDTH.  Depth cannot buy
> what only width can** — so any future attempt at a decidable sky must
> scale **width**, and scaling depth is **certified futile**.

**Strata, labelled separately and never merged.**  EXHAUSTIVE: three
fully enumerated families, **30,729 + 243,769 + 764,584** histories — max
**3** directions against the 4 needed, so the question is **UNDECIDABLE**
there, reported as undecidability and **never** as a 2+1 cap.  SAMPLED:
**44** decidable triples (SKY-A 0, SKY-B 37, SKY-C 7), **0** shattered
4-sets.

**No ceiling and no saturation may be quoted (TG2(c), an in-receipt
retraction).**  The plateau at 4 from width 4 through 8 invites a
structural-ceiling reading; a denser probe at width 10 with SKY-B's depth
varied over `{1,2,3}` instead of pinned at its committed 2 reaches **5**.
The plateau was an artifact of sampling density plus a pinned parameter.

**The null, REVERSED at round 1 (MAJOR R1).**  The original TG5 null was
defective twice over: its actor extraction scanned each event tuple for
the first single alphabetic character, which in a transport event is the
**event type** (`'d'`,`'p'`,`'r'`,`'n'`), never the actor — verified on
720 sampled events, **100% returned the type**; and repairing that would
not have rescued it, since **any** null built as a disjoint union of
totally ordered groups gives every element exactly one cover, so its
maximum sky is **1 by construction** and the gate could never fail.  (The
D46f failure mode reproduced *inside* the gate written to prevent it.)

Rebuilt as a **link-count-matched random DAG** (same carrier size, same
cover count, relations re-drawn under a random linear order — a
construction that *can* concentrate covers), the null reaches **7
directions with 362 decidable triples** against transport's **4**.

> **The original claim "cross-actor causation PRODUCES the sky" is
> WITHDRAWN.  Transport skies are NARROWER THAN CHANCE**: the law
> *constrains* sky size below the generic value at matched carrier and
> link count.  This **strengthens** the actor-width reading — the bound is
> a real restriction, not an artifact of record size.

**A declared limit:** the null is **crude** (matched on carrier size and
link count, not on the height/width profile), so "narrower than chance"
is established against **that** null and not against every reasonable one.

### B5.7 The dimension discriminator: max-shatter reads geometry on sprinklings `[REFEREE-CARRIED + coordinator-confirmed]`

*Sources: `v10/code/d55c_m31_control_exact.py` (10 PASS / 0 FAIL after batch-round repair); `reviews/batch-round1-d50-to-d60.md`, D55c BLOCKER 1 and MAJOR 1; LOG #453(2).*

**The result.**  On genuine sprinkled Minkowski records **at sufficient
density**, and read under **SKY-A**, the shatter number reproduces the
continuum ladder of §B7.5 exactly:

| genuine sprinkling | shatter 3 | shatter 4 | shatter 5 |
|---|---|---|---|
| `M^{2+1}` | **yes** | **never** | never |
| `M^{3+1}` | yes | **yes** | **never** |

**The matched ladder `[REFEREE-CARRIED]`**, `N = 150 … 500`, same
generator, same box, only the dimension differing:

```
                       capable(4)                 SHATTER-4        best |r ∩ S|
  M^{2+1}:  56 / 100 / 137 / 189 / 288 / 375     0 everywhere         15/16
  M^{3+1}:  91 / 132 / 182 / 226 / 316 / 407   0/1/11/30/116/211      16/16
```

**Independently confirmed by the coordinator** with code sharing nothing
with the receipts: SKY-A shatter-4 at `N = 300`, box 40 — **`M^{3+1}` 17
events, `M^{2+1}` zero.**

**It is not merely sky size** — the trap D54's round named.  Size-
controlled, pooled over `N = 200…500` `[REFEREE-CARRIED]`:

```
  M^{2+1}: |dirs| 4-7: 0/173   8-11: 0/526   12-15: 0/304   16-19: 0/72
  M^{3+1}: |dirs| 4-7: 0/18    8-11: 1/162   12-15: 7/314   16-19: 63/337
                                              20-23: 117/253  24-27: 88/127
```

At `|dirs| = 12–15` the samples are comparable — **304 against 314** —
and the split is **0 versus 7**.

**The halt condition holds, and the continuum calibration transfers
exactly.**  Shatter-5 on dense genuine `M^{3+1}` under every reading:
SKY-A at `N = 300/400/500` gives `capable(5) = 186/278/370` with
**SHATTER-5 = 0** (best 26/27/28 of 32); SKY-C likewise 189/277/368,
**zero** (best 25/27/28).  So: *sprinkled 2+1 shatters 3 and never 4
(arcs shatter 3); sprinkled 3+1 shatters 4 and never 5 (caps shatter 4;
Radon stops at 5).*

> **MAX-SHATTER IS AN EMPIRICAL DIMENSION DISCRIMINATOR, with two-sided
> controls.**

**Density is the enabling variable, and reading a sparse sample as a
negative is the error to avoid.**  At the sampled densities `≤ 6e−05` no
sky of a sprinkled `M^{3+1}` record shatters 4; the transition sits
between `~2e−05` and `~9e−05` (`N=200, T=160, box=40` at `1.95e−05`:
`capable(4) = 917`, shatter-4 **0**, best 15/16 — *one trace short*).
The scoped negative that sparse data licenses is: *at those densities,
under that reading, no shattering* — and nothing more.

**And sprinkled records are not at meter reading zero.**  They sit at
their own dimension's rung: on the same four committed configurations,
gated at `≥ 3` dirs and `≥ 8` traces, **2,151 capable / 1,087
shatter-3**; on genuine `M^{2+1}` at `N = 160`, **1,002 capable / 492
shatter-3**.

**Scope, carried.**  Reading-relative — the discriminator is sharpest
under SKY-A, which is why §B5.4's reopening of residue 2 matters.  The
ladder numbers are `[REFEREE-CARRIED]`; the central comparison was
confirmed independently by the coordinator.
No claim is made that any record *is* a manifold of any dimension: what
is measured is where a record sits on a ladder calibrated against
continuous shadow systems.

## B6. The completion dichotomy

*Non-technical twin: Part A, chapter A6.*
*Primary sources: paper 30 §5–§6; `v10/THE-COMPLETION-DICHOTOMY.md` (the corpus's standalone brief, which this chapter compresses); `note-d42b3-placement-and-the-discrete-ts-condition.md`; `note-d44a-renewal-pumping-closure-theorem.md`; `note-d49-completion-dichotomy-settlement-{pin,result}.md`; `note-d50-{is-the-form-a-law-pin,form-law-or-choice-result}.md`; LOG #418–#422.*

### B6.1 The object

A **placement completion** is strictly positive data `Z` on record
prefixes with the transfer

```
q'(e | h)  =  q(e | h) · Z(h + e) / Z(h)
```

`N(h)`, the **frontier sum**, is the total raw weight of `h`'s menu — the
object the whole no-go is about.  The **ladder excess** is `N − 1`, which
sits at `k/4` per §B2.7.

### B6.2 The three demands

- **(a) PER-CUT NORMALIZED.**  `Σ_e q'(e|h) = 1` for every `h`.  Without
  this there are no probabilities.
- **(b) FOLIATION-INVARIANT.**  `q'` is a function of the record alone —
  class-constant; equivalently, chain products agree across **every**
  linear extension of every history.  Without this, "the probability"
  depends on the slicing.
- **(c) WITHIN-CUT RATIO-PRESERVING.**  Relative weights of alternatives
  at a cut are untouched.  Without this, completion is not *normalizing*
  the law but *changing* it.

### B6.3 `[THEOREM]` (a) + (b) + (c) is impossible

> **Ratio-preserving completions do not exist.**  Ratio preservation
> forces `Z(h+e)/Z(h) = 1/N(h)`.  No cut function has these increments,
> because `N`'s chain products are foliation-dependent: **36 of the 202
> canonical diamonds refute integrability** `[EXACT]`, the violations
> lying in **two diamond-connected components** `[REFEREE-CARRIED]`.

Source: paper 30 §5.2, receipt-gated; `note-d42b3…` D1.

**The forcing, step by step.**

1. Demand (c) fixes `Z`'s increments completely: the only freedom left is
   an overall factor per cut, and demand (a) pins it to `1/N(h)`.
   **`Z = N` is forced — there is no choice left.**
2. So the question collapses to: *is `N` a discrete gradient on the cut
   complex?*  Equivalently, is `log N`'s increment a coboundary?
3. **It is not.**  `N` *is* genuinely cut-attached data — constant on all
   **427** canonical classes, gated `[EXACT]` — but cut-attachment is not
   enough.  A gradient must have path-independent chain products, and
   `N`'s are foliation-dependent.
4. **The mechanism, named:** `N` **double-counts the causally blind join
   layer** along exactly those foliations that expose it.  Paper 30
   §4.3's witness pair makes it visible: on `[pA0, selfA, pB1]` versus
   `[pA0, pB1, selfA]` — one canonical DAG, `mu = 1/256` under both
   orders — the cut-normalized products differ, **`1/2048` versus
   `1/2560`**, because the `N`-sequence runs `(2, 2, 2)` along one order
   and `(2, 2, 5/2)` along the other.  `N` jumps from `2` to `5/2`
   exactly when the blind pair becomes visible.  **§B2.10 shows this
   mechanism is the *whole* story and not merely the smallest witness**:
   over all 665,286 commuting ordered menu pairs of the depth-6 family the
   order defect equals `M(sigma(Hb))/M(sigma(Ha))` with **zero
   exceptions**, `M` being that same total.
5. **The certificate:** 36 diamonds where the two paths give different
   products — a census in two connected components, not one pathological
   case.

> **A distinction worth holding, because the weaker version of it is
> false.**  "`N` is not cut-attached data" would be wrong: `N` *is*
> constant on all 427 canonical classes.  The true and **stronger**
> statement is that `N` is cut-attached **but not a discrete gradient** —
> which is what the 36-diamond census establishes, and what makes the
> no-go a census rather than a single witness (`note-d42b3…` D2).

### B6.4 The one escape, closed by narrowing `[EXACT]`

A **zero-class counterterm** (the own-view component filter) does restore
sums ≡ 1 — by exactly `k·(1/4)`, the ladder excess — and is
gauge-invariant.  It refutes the no-go **as originally worded**.

**It also kills ALL join arbitration.**

So the no-go was **repaired rather than abandoned**: it holds for
**support-preserving (strictly positive)** counterterms, by a nesting
argument (subset candidates, equal shared weights, strictly positive
extra mass — `1/4` over the two blind events) which is printed and gated.
Paper 30 §4.3 states the companion **actor-local no-go
`[THEOREM, positivity-qualified]`**: no support-preserving re-weighting
computed from the initiator's *own view* can restore per-initiator
normalization — witness: the own-view canonical DAG is *identical* at
`[pA0]` and `[pA0, pB1]` while the per-initiator sums differ (`1` vs
`5/4`).  The zero class is **declared excluded**, on the stated ground
that *a completion which abolishes joint arbitration abolishes the physics
it was meant to normalize.*

> This is the template for the corpus's style: **the no-go was not
> defended, it was narrowed until true, and the narrowing is on the
> record with its reason.**

### B6.5 Gradient (Doob `h`-transform) completions `[EXACT]`

Run the backward recursion `Z(h) = Σ_e q(e|h) Z(h+e)` from any strictly
positive boundary at terminal depth.  At the **unit boundary** on the
depth-4 two-actor object:

| quantity | value |
|---|---|
| `Z(empty)` | **`1037/64`** (reciprocal convention `64/1037`; every ratio-level quantity identical) |
| positivity | throughout |
| per-cut normalization | at **all 215 interior histories** — the recursion's defining identity |
| the §B6.3 witness pair | **equalizes at `1/2074`** under both orders |
| boundary freedom | **313-dimensional** `[REFEREE-CARRIED, LOG #302]` |

The other canonical choice is the **class-`1/k` boundary** (`Z` at a
terminal history = the reciprocal of its canonical class's
linear-extension count), with `Z(empty) = 325/64`.

**The corpus names this a Doob `h`-transform** (`note-d43-corpus-audit…`:
"*completion is a Doob h-transform*"; `note-d40-where-the-action-cocycle-lives…`:
"*the K-flat shape is an h-ratio/Doob completion form*").

`[MY READING]` A Doob `h`-transform is what you get conditioning a
process on its future behaviour: each step's relative weights are tilted
by a function of where the process is heading.  The 313 parameters are the
choice of that function.  So this class says the framework's
probabilities are **forward-local rules plus a boundary object**, and the
boundary object is not derivable from the rules.

**The cost `[EXACT]`:** within-cut ratio deformation at **21 of the 114**
interior cut classes, **the root included**.  At the root the successor
normalizers are not constant across candidates; extreme completed weights
`133/2074` versus `771/2074`, equivalently extreme successor normalizers
`16/133` versus `32/257`.

**What is invariant with no completion at all (paper 30 §5.4).**  Two
positive laws that any completion must respect, and the gradient class
does:

- **RATIO LOCALITY.**  `mu`-ratios of histories are stable under common
  admissible extensions with identical past-views — paper 28's ratios-only
  structure, recovered as the weight system's invariant content.  At this
  depth the **swept corner** (proposal branches, where the enumeration is
  complete) has every extension factor exactly `1/8`, which makes the law
  a `[THEOREM]` there; the census is kept as a tripwire (**28 tested, 0
  violations**) `[EXACT]`.  The law's *empirical* content begins where
  factors vary (idle and arbitration branches), declared.
- **THE DENSITY LAW** of §B2.7.

`[MY READING]` **Ratios are law; absolute probabilities are not.**  The
completion problem is exactly the problem of going from a ratio-structure
to a measure, and the theorem says that step cannot be taken locally.

### B6.6 The quantum lift does not escape

Paper 30 §6.  The endpoint lift assigns each complete history the
amplitude `∏ √q` on record ancillas and normalizes the global state.  On
the true depth-2 slice of the base grammar — **32 sequences in 23
canonical classes** — the Born diagonal on the canonical-class basis
equals `mu/Z` with `Z = Z_class = 3`, and every one of the **253**
quadratic ratio pairs is exact `[EXACT; mpmath at dps 80 with 1e-60
thresholds, Fraction side-derivations where rational]`.

**But the object must be named correctly:**

> the endpoint lift **is the classical gradient completion at the `1/k`
> boundary in Hilbert dress** — dividing by `√Z` is the flat pushforward,
> not "normalization by unitarity"; the class and sequence bases are the
> **two classical boundary choices**:

| lift basis | `Z` | classical identity |
|---|---|---|
| canonical-class diagonal | 3 | gradient completion, class-`1/k` boundary |
| sequence (word) partition | 4 | gradient completion, unit boundary |
| coherent aggregation | 6 | the one non-gradient object |

The three normalizations are **observably inequivalent**, and which basis
carries amplitude is OPEN.

**And its step operator faces a three-horn obstruction at the arbitration
layer `[EXACT exhibit; OPEN problem]`:**

1. **Cut-independent** operators cannot emit both witness menus — 2
   events summing to `1` at the early cut versus 4 events summing to
   `5/4` at the join cut, with the two pair-arbitration branches
   *inadmissible* at the early cut — so they place weight on inadmissible
   branches or none on admissible ones, reproducing the
   arbitration-killing zero class of §B6.4;
2. **cut-dependent** operators must read the blind wire — support
   overlapping a carrier the initiator's registers do not include,
   breaking the carrier structure that made incomparable isometries
   commute;
3. **dilations** re-import cut data as state — "the classical `Z` returns
   wearing a register".

> **The quantum completion problem begins at the arbitration layer,
> exactly where the classical one stopped.**

**What the lift does establish** (real results, at fixture scale, each
gated at `1e-60` with exact side-checks):

- **the kernel-layer lift is exact**: the arbitration's internal click
  structure lifts with path winner Born diagonal `(2/3, 1/3)` at norm 1
  `[EXACT]`;
- a complete **fine-versus-coarse instrument pair**: over all 15 order
  pairs of the path fixture, under **coarse** (winner-sealed) records the
  7 same-fiber pairs carry off-diagonal exactly **`1/6`** and the 8
  cross-fiber pairs exactly **`0`**; under **fine** (order-sealed)
  records every off-diagonal is `0` by construction `[EXACT]`.  Which
  sealing nature applies stays **empirical**.  (The numerical coincidence
  with the kernel total-variation distance — both `1/6` on this fixture —
  is a coincidence of two distinct observables.)
- the operational **D23 fiber**: from the coarse record, histories are
  identifiable only up to the greedy fiber; the `{P,R}` fiber contains
  four click orders, all 6 same-fiber pairs have identical reduced states
  (overlap 1), and every fiber-versus-`{Q}` pair is orthogonal `[EXACT]`;
- **the reception form**: the basis-copy reception map is a
  distinguishability isometry on the probed family (10 pairwise distances
  preserved), with the lossy-renormalized negative control failing as it
  must at violation `0.25989…` (dps 80) against the `1/100` threshold
  `[EXACT]`.

A second grammar (ternary payloads) lifts the structural forms tested —
**two-of-two grammars, and no more is claimed** — exposes the values as
**toy-relative**, and shows kernel discrimination is
component-shape-dependent.

> **Not the same object as §B2.11, and the difference matters.**  This
> lift *supplies* amplitudes to complete histories at fixture scale and
> asks what the classical structure becomes in Hilbert dress; §B2.11 asks
> the converse question — what Hermitian forms over the closed law's own
> history layer are *permitted* by the record demands — and answers it by
> exact rank.  Neither builds the other: the lift is a chosen map, not a
> derived functional, and none of §B2.11's members is claimed to be it or
> to be the action line's.  What they agree on is where the difficulty
> sits: the lift's three-horn obstruction is at the arbitration layer, and
> §B2.11's elimination hands superposition to transport scope, which is
> the scope arbitration-with-delivery lives at.

### B6.7 The dichotomy, and a correction to its framing

> **THE DICHOTOMY.**  Since (a) and (b) are non-negotiable, **(c) must
> go.**  Either **(I)** the completion **deforms within-cut ratios**, or
> **(II)** no completion need be imported at each finite depth because a
> **root-free** completion exists — which requires a strictly positive
> harmonic function on the *infinite-volume* state space.

**The two horns are not mutually exclusive**, and reading them as a fork
is a mistake: the settled completion `Zhat` does **both** — it is
root-free *and* it deforms ratios (at 50 of the 114 interior cut classes).
Demand (c) is unconditionally impossible; §B6.3 is a theorem nothing
later touches.

> **The genuine fork is not deformation versus none — it is an IMPORTED
> boundary versus a LAW-DETERMINED one.**

### B6.8 Rootedness: why truncated completions are convicted `[EXACT]`

The grammar has a **renewal** structure: the root and the
post-arbitration fresh-base record point are **structurally isomorphic** —
an event-level bijection, type- and payload-matched with `v0 ↔ v1`
translated, carrying **equal `q` at every matched event**.  Two record
points the grammar cannot tell apart.  Yet the completed transfer differs
at that pair under **both** canonical boundaries:

| boundary | `Z(empty)` | the matched pair prices |
|---|---|---|
| class-`1/k` | `325/64` | `21/325` vs `1/16` |
| unit | `1037/64` | `133/2074` vs `1/16` |

**So the completion distinguishes two points the *law* identifies.**  That
is precisely what "rooted" means, and it is why truncated completions are
**depth-non-stationary** — the uniform-rooting analysis of paper 28 §5.3
anticipated it at the level of root laws.  Sharpness disclosed in the
source: of the 1,191 histories, **331** share the root's bare menu shape,
**175** are structurally isomorphic to it, **31** exactly so; the exhibit
uses the strongest (structural event-level) notion.

`[MY READING]` The cleanest single symptom of the whole problem: **the
renewal isomorphism says the law has forgotten where it started; the
completion says the measure has not.**  The boundary information enters
exactly there.

### B6.9 Residue 1, and the state-space reduction

**RESIDUE 1.**  Does a strictly positive harmonic function exist on the
**infinite-volume state space**?

Paper 30 §5.7's reduction is **one-way**: stationary completions
`Z(h) = f(state(h))·λ^(−depth(h))` are a *subclass* of positive-harmonic
solutions, so the infinite-volume positive-harmonic residue *contains*
the root-free question — one open core, not two.  It is the discrete
relative of Martin-boundary existence theory `[LITERATURE]`.

**The change of enumeration space (the key move, D44a).**  Instead of
enumerating histories, enumerate a **bounded local-state abstraction**
`sigma(h)` — the abstraction of the *full view* of `h`, modulo base
renaming.  It records:

- the **per-actor holdings pattern** — which actors hold which
  non-superseded versions, as a partition-with-multiplicity over renamed
  bases (genesis and renewal bases identified by the renaming);
- the **live-proposal structure** — per renamed base, the multiset of
  `(proposer, value-bit)` data of live proposals, with the edge/conflict
  structure of their components;
- the **superseded-base pattern**, restricted to bases still carrying any
  of the above.  Dead structure no menu can see is dropped.

`sigma` is finite-valued **if** the dropped structure is truly
menu-invisible; **that invisibility is checked, never assumed** — it is
where the gap lived, and §B6.13 closes it as a theorem.  The companion
question — whether an event can force the successor state to *mention*
dropped structure — is §B6.13b's, and it closes too.

**What is gated `[EXACT]`:**

- **Menu factorization on the cache:** `menu(h)`, as an event-multiset up
  to renaming with exact weights, is a function of `sigma(h)` on the
  **entire depth-6 cache (34,375 histories)**; census re-anchored
  `[1, 7, 39, 215, 1191, 6471, 34375]`.  Zero exceptions.
- **Transition determinism on the cache:** `sigma(h + [e])` is a function
  of `(sigma(h), e-up-to-renaming)`, verified exhaustively; **176**
  abstract keys.
- **The depth-free closure (CG3a):** breadth-first search on `sigma`-space
  from `sigma([])` closes at **36 states, 176 edges** — a
  *frontier-exhausted* search, so no transition leaves the closed set;
  and the depth-7 family realizes no new state (**out-of-sample
  closure**).
- **The intrinsic partition:** `P_0` = menu shape, `P_{t+1}` = one
  probabilistic-bisimulation refinement under the committed per-candidate
  `(weight, target-class)`-multiset operator.  Fixed-point trajectory
  **`[4, 5, 6, 6]`** — reached at lookahead `t = 2`, stable thereafter —
  giving **SIX classes** with transfer `T_REF`.
- **The Perron package on the quotient:** `λ = 2`;
  `f = (4, 4, 3, 7, 3, 3)/3` unique up to scale; **root = renewal** as one
  `sigma`-state; `π = (1, 1, 2)/4` with mass transport exact.
- All three hypothesis laws verified exhaustively **through depth 7,
  179,783 histories, zero exceptions** — labelled `[EVIDENCE]`, **never a
  premise**.
- A pinned landing at six abstract states is **provably impossible** for
  any menu-exact abstraction (bisimilar histories can be menu-distinct;
  witness gated), so the **two-layer structure — 36 closing, six as the
  quotient — is forced, not incidental.**

**The conditional theorem.**  Three depth-indexed laws, **none implying
another**:

- **(H0)** the view invariants at every depth: own-view alive holding a
  singleton; non-superseded holdings inside it; live proposals on the
  proposer's base; conflicting live pairs incomparable.
- **(H1) MENU FACTORIZATION at every depth.**  `menu(h)`, as a renamed
  event-multiset with exact weights, is a function of `sigma(h)`.
  **Nontrivial because admissibility runs on OWN VIEWS that lag the full
  view `sigma` records** (§B3.2).
- **(H2) TRANSITION DETERMINISM at every depth.**  `sigma(h + [e])` is a
  function of `(sigma(h), e-up-to-renaming)`.  Explicitly **not** a
  consequence of (H1) — d44a's own note says so, and the conditional
  theorem consumes (H2) in both legs.

> **`[THEOREM, conditional]` Assume (H0)–(H2).  Then residue 1 is DECIDED
> at all depths at d42a scope**: `sigma` takes exactly 36 values at every
> depth; the intrinsic partition is at every depth the pullback of the
> abstract chain's bisimilarity; and the Perron package is the completion
> decision at every depth.  QED (conditional).

**And the antecedent is discharged.**  §B6.13 discharges **(H0)** in full
and proves **(H1)** as a theorem; §B6.13b proves **(H2)** by the update
table.  All three hold at two-actor delivery-free d42a scope, so **the
conditional theorem above is UNCONDITIONAL there** and residue 1 is closed
at that scope (§B6.13b, §B6.14).  The finite-depth sweeps stay
`[EVIDENCE]` and are never premises — the theorem force is in the two
proofs.

**Declared verification scope, which a reader must carry:** blockwise
equality of the pullback with the committed intrinsic partition is
computed **in-receipt at length ≤ 4** and **at length ≤ 5 by the frozen
round's referee** `[REFEREE-CARRIED]`; the **four minlen-6 `sigma`-states
are classified only via the closure argument**, which §B6.13/§B6.13b make
unconditional at this scope rather than assumed.  No minimality is
claimed for `sigma`'s superseded marks or serialization.  An earlier
"pumping" route is **retired** and is not a mechanism of this proof.

**Scope boundary:** the H1 lemma is **DELIVERY-FREE scope only** (D44b
terminal).  At transport scope the objects change and must be
re-established — and §B9 shows they cannot be, menu-exactly.

### B6.10 The settlement `[D49, LOG #418; round 1 → #419; TERMINAL]`

Receipt `v10/code/d49_dichotomy_settlement_exact.py`, **31 PASS / 0 FAIL**
post-repair, exit 0, byte-identical across `PYTHONHASHSEED` 0/7/61/999.

**What was missing was a receipt, not a theorem.**  Paper 30 §5.7
*defines* the stationary completion and declares its existence
`[OPEN, declared]`; D43b *computed the eigenproblem* (`λ = 2`,
`f = (4,4,3,7,3,3)/3`, gate MG4 "the root-free certificate" = YES,
#339/#345); D44a *closed the state space*.  **Every one of those gates
lives on the quotient.**  The object the dichotomy is about lives on the
cut complex.  No unit had built `Zhat` on **histories** and run it against
the §B6.2 demands.  The corpus carried a decided question as an open one
from #339 to #417.  `[MY READING]` The lesson generalizes: *a reduction
is not a result until the reduced answer is transported back and tested
where the question was asked.*

**The object:**

```
Zhat(h)  =  2^(−|h|) · f(class(sigma(h))),     f = (4, 4, 3, 7, 3, 3)/3,  λ = 2
```

**It is a completion, in the sense of §B6.2 `[EXACT]`:**

| demand | certificate |
|---|---|
| strictly positive | 0 non-positive completed weights |
| **(a) per-cut normalized** | **0 violations / 6,471 histories** at depth ≤ 5; and **0 / 27,904** at depth 6, whose menus reach the *uncached* depth-7 level (145,408 children) — out-of-sample |
| class-constant (gauge-invariant) | 0 violations / **5,548 canonical classes** (of which **813 are singletons** where it cannot fail; effective 4,735) |
| **(b) foliation-invariant, DIRECTLY** | completed chain products equal across **all 1,191 linear extensions of all 427 canonical classes** at depth ≤ 4 (137 classes have a single extension; effective 290) |
| diamond flatness | **0 / 202**, against the naive normalizer's **36 / 202** in the same run |
| support-preserving | **2,032** join arbitrations keep positive weight — **not** the excluded zero class |
| it is a *law* | the completed menu, up to base renaming, is a function of `sigma(h)` alone — 1,163 same-sigma comparisons, 0 mismatches |
| it is a *measure* | completed weights of all depth-`D` histories sum to **exactly 1**, `D = 1..6` |
| **it DESCENDS** `[D65, §B2.10]` | `μ_Zhat = q·Zhat` is **constant on all 5,548 record classes** — zero splits — so the completed measure is a function of the record and not of the serialization, which the *uncompleted* normalized kernel is not.  `Zhat` is the unique positive `λ = 2` harmonic completion of this form with that property |

**And it is root-free `[EXACT]`:**

| completion | `Z(empty)` | root | renewal `H3` |
|---|---|---|---|
| unit boundary | `1037/64` | `133/2074` | `1/16` |
| class-`1/k` boundary | `325/64` | `21/325` | `1/16` |
| **`Zhat`** | — | **`1/16`** | **`1/16`** |

And not only at that pair: **the entire 215-node matched subtree** — the
root tree against `H3`'s subtree under the `v0 → v1` substitution —
carries **identical completed menus event-by-event, 0 mismatches.**

> **HORN (II) HOLDS.  A root-free completion EXISTS** — exactly what paper
> 30 §5.7 declared `[OPEN, declared]`.

**Uniqueness, in three steps `[EXACT]`:**

- **`λ = 1` is impossible.**  Every menu of the closed 36-state chain sums
  to between `2` and `5/2`, so for any positive `f` the minimizing state
  forces `λ ≥ 2`.  The value 1 *is* an eigenvalue of the transfer, but
  `dim ker(T − I) = 1` and its generator `(−4/5, 4/5, −1, −1/5, −1, 1)`
  has **mixed signs**.  So there is **no positive harmonic function on the
  quotient** — and §5.7's `λ^(−depth)` factor is a **necessity, not a
  convention**.  The depth grading is what makes `Zhat` harmonic on
  *histories*, which is where the demand lives.
- **`λ = 2` is the only eigenvalue with a positive eigenvector.**
  `{2,4,5}` is closed and irreducible, so `f` restricted to it is its
  Perron vector and `λ = 2` exactly (`charpoly = (x−2)(x−3/2)(x−1)`); the
  transient extension is forced by the entrywise-nonnegative resolvent
  `(2I − M_t)^(−1)`, `det = 3/32`, returning `(4/3, 4/3, 7/3)`.
- **Not a quotient artifact.**  Re-run at the **fine 36-state level**:
  exactly **one** closed communicating class (9 states, every row summing
  to 2, Perron root 2), 27 transient states with
  `det(2I − M_t) = 2187/2^41` and a nonnegative resolvent, and
  `dim ker(2I − M36) = 1`.  Same answer, same vector, no collapsing
  required.

**What the settlement costs `[EXACT]`.**  Demand (c) is **not** restored,
and `Zhat` must be compared against **both** canonical boundaries, not one:

| completion | deformed cut classes | worst distortion | median |
|---|---|---|---|
| unit boundary | 21 / 114 | `23/16` | 1 |
| class-`1/k` boundary | **103 / 114** | `4` | 2 |
| **`Zhat`** | 50 / 114 | `7/3` | 1 |

**`Zhat` sits INSIDE the range spanned by the two canonical boundaries;
the deformed-class count is not a scalar figure of merit.**

**The root is not among `Zhat`'s 50** — there it is exactly
ratio-preserving, `q' = q/2`, every proposal `1/16`, every idle `3/8`.
**But this is TOY-RELATIVE:** it needs
`f(class 0) = f(class 1) = 4/3` with the root's menu leading only into
classes 0 and 1, and in any grammar where those Perron weights differ the
root deforms.  So paper 30 §5.3's sharp point is **not removed** — it
**does not occur in this grammar**.

**The deformation is exactly the Perron tilt** — a characterization, not a
count.  For every pair of alternatives at every cut,

```
q'(e1)/q'(e2)  =  [ q(e1)/q(e2) ] · [ f(class(h+e1)) / f(class(h+e2)) ]
```

gated over **77,541 pairs** (23,305 leading to the same successor state,
54,236 tilted), **0 violations**.  So the completion preserves the
weight-system ratio *exactly* between options leading to the same state
and tilts it *only* by the successors' Perron ratio: **each option is
re-weighted by how much record-growth capacity it leads to, and by nothing
else.**

`[MY READING]` This is the sharpest available form of "is the deformation
physical?" — what must be judged is one **named principle**, not an
unstructured distortion.  Judging it is open, and the corpus explicitly
does not claim it is a physical selection principle rather than the unique
mathematically canonical one.

**Washout: pre-registered, and it landed NEGATIVE.**  Unconstrained
boundaries do **not** wash out: the achievable root-transfer set is a
projective image of the boundary cone, hence the convex hull of its
vertices, and its **diameter is 1 at every truncation depth tested**
(6 / 23 / 84 / 313 terminal classes).  A boundary free to distinguish
anything can drive the root anywhere.  What *does* wash out is every
boundary respecting the law's own identifications: `π = (1,1,2)/4`
satisfies `π T = 2π` and is strictly positive on the dominant class, so
`π·b > 0` for every strictly positive `sigma`-measurable `b`; with the
spectral gap (every other modulus `≤ 3/2 + 2^(−5/3) ≈ 1.81498 < 2`) this
gives `T^n b / 2^n → (π·b / π·f) f` at rate `≈ 0.9075^n`, below `1e−9` by
`n = 400`.  **So horn (I) is refuted by uniqueness under the law's own
identifications, not by any limit.**

### B6.11 The two blockers of D49 round 1, and what they left standing

**BLOCKER B1 — #418's "229 of 313 boundary dimensions act trivially" is
FALSE.**  Refuted in-receipt (gate F3): two strictly positive boundaries
differing by a kernel direction give **identical interior potentials** and
**different completed transfers at depth-3 cuts** (witness `1/16` vs
`1001/16000`).  The reason is elementary: **a completion is the transfer
at EVERY interior cut, and a depth-3 transfer is `q·Z(h+e)/Z(h)` with
`|h+e| = 4` — it reads the boundary directly.**

**And #420 upgraded the round's witness to a THEOREM.**  A kernel
direction satisfies `Σ_e q(e|h)·db(h+e) = 0` at every depth-3 cut, so
`Z(h)` is unchanged there; the transfer at that cut is `q·Z(h+e)/Z(h)`
with `|h+e| = 4` — the boundary itself — so with the denominator fixed the
transfer is unchanged **iff `db` vanishes on every child of `h`**.  A
nonzero `db` is nonzero at some terminal history, which is a child of some
depth-3 cut, so that cut's transfer **moves**.  Hence *every* nonzero
kernel direction changes some depth-3 transfer; the gate's ">0" is in fact
"always".

> **Paper 30 §5.3's 313-dimensional boundary freedom is CORRECT; no
> erratum is owed, and the one #418 queued was cancelled before it could
> be applied.**  Surviving addendum: the boundary → interior-**potential**
> map has rank exactly **84** = the number of depth-3 cut classes (layer
> census `1/6/23/84/313`), so the completed transfer at cuts of depth ≤ 2
> sees the boundary only through an 84-dimensional image while the depth-3
> layer sees all 313.  Inside the 84, the depth-stationary completions are
> a **single ray**, realized by the strictly positive
> `b*(t) = 2^(−4) f(class(t))`, which reproduces `Zhat` at all 215
> interior histories exactly.

**BLOCKER B2 — the uniqueness rhetoric fell.**  The withdrawn sentence:

> ~~Among completions that do not distinguish record points the law
> identifies, there is exactly one, and it needs no boundary.~~

Measured at depth-4 truncation `[MEASURED — tangent-space counts at `b*`,
hence LOWER BOUNDS on the freedom left]`:

| demand imposed | constraints | rank | boundary directions still FREE |
|---|---|---|---|
| agreement on the root/renewal matched pair (I1) | 6 | 5 | **308 of 313** |
| bisimulation-invariance of the completed class transfer at every interior cut (I2) | 589 | 176 | **137 of 313** |
| paper 30 §5.7's FORM | — | — | **0** — one ray |

> **Neither invariance demand delivers uniqueness.  What delivers it is
> the FORM: `Z` a state function times `λ^(−depth)`.  The stationary form
> is a POSTULATE ABOUT THE SHAPE OF `Z`, not an invariance principle.**
> Therefore **"the record law is forward-complete" is true of the law PLUS
> that form and may never be quoted without it.**

**MAJOR M1 — the gate count overstated the evidence.**  #418 led with "25
PASS" as if 25 independent tests.  Verified otherwise: D1 is arithmetic
given d44a CG1+CG2 and d43b MG3; **E2 is a THEOREM-PASS** given d44a SG3
plus sigma-measurability — re-derived by the referee with **no event
serialization at all** (0 sigma-mismatches, 0 completed-weight-multiset
mismatches over 215 nodes), which confirms the determinism repair **and
shows the unit's most-quoted number, `1/16 = 1/16`, is a property of the
DEMAND and not evidence for the Perron vector**; D4 is the telescoping
theorem; D5, D7 and G5 are the definition of `q'` rearranged — **G5's
77,541 pairs are a restatement, not a sweep**.  Repair: every gate carries
`[SUBSTANTIVE]`/`[ANCHOR]`/`[DERIVED]`/`[THEOREM-PASS]`, AST-anchored,
**15 / 5 / 6 / 5**.

Three methodological findings of that round belong with the method
(§B11.6) rather than with the result, and are recorded there: a
**citation-discipline breach** (a settlement banner written into the
corpus's entry-point document before any round, and without scope); a
**determinism defect** caught only by hash-seed variation, from
serializing events through a raw `frozenset` repr; and a
**record-keeping defect**, a round logged as delta'd when the frozen
file contained no delta.  All three are on the record with their causes,
which is the point of having them.

### B6.12 D50: the form is a CHOICE `[LOG #421/#422; batch-round reviewed and repaired]`

Pin `note-d50-is-the-form-a-law-pin.md`; receipt
`v10/code/d50_form_law_or_choice_exact.py` (13 PASS / 0 FAIL after
batch-round repair, exit 0), importing D49's state by AST-stripping its
`check()`/`print()`/`sys.exit` statements — single source, D49's gates
not re-run.  Reviewed in the batch round
(`reviews/batch-round1-d50-to-d60.md`); **the headline STRENGTHENS
under repair** — the freedom is larger than first published and the
negative is now constructive.

**The question.**  Is there a demand stated on the **record** (rather than
on `Z`) that **forces** the form?  The pinned family: I1 renewal
agreement, I2 bisimulation invariance, **I3 depth-stationarity
(PRIMARY)**, I4 = I2 + I3, and (in the receipt) I5 = I3 + demand (b).

**PRE-REGISTERED EXPECTATION, with its argument, before running: I3
FORCES THE FORM.**  Sketch as pinned: I2 makes `r(h,e) = Z(h+e)/Z(h)` a
function of `(class(h), class(h+e))`; path-consistency then makes `r` a
discrete gradient on the class graph up to a constant factor per step,
`r(s,s') = g(s')/(c·g(s))` — which *is* `Z(h) = c^(−|h|) g(class(h))`,
with `c` fixed by normalization to `λ = 2`.

**THE FALSIFIER FIRED.**  The space of **distinct completions** satisfying
depth-stationarity has dimension **12, 32, 125** at truncation depths
2/3/4 — **it GROWS with depth** rather than collapsing to a ray.

- **The negative is rigorous while a positive would not have been** — the
  pin's one-sidedness doctrine fixed this in advance: a tangent dimension
  `> 1` mod scaling **exhibits** nearby non-proportional completions
  satisfying the demand.  A dimension of 1 would have been local evidence
  only.
- **SF4: foliation-invariance adds nothing.**  I5 more than doubles the
  constraint count (25 vs 16, 210 vs 109, **1,374 vs 610**) and leaves the
  completion dimension **exactly unchanged** at every depth.  **The
  residual freedom is not gauge freedom.**
- **SF5:** I3 is strictly stronger than I2 at every depth (16 vs 14, 109
  vs 101, 610 vs 589 constraints) — so this unit is not re-measuring B2;
  the cross-depth comparisons are really there and simply do not bite.
- **SF6 negative control held:** I1 stays loose.
- **The negative is CONSTRUCTIVE.**  Beyond a tangent count, an **exact
  positive line of distinct completions** satisfying the demand is
  exhibited — nearby non-proportional completions, written down rather
  than inferred.

> **A corpus-wide number correction, and its lesson.**  The published
> boundary-freedom figure under bisimulation-invariance was **119**; the
> correct value is **137**, the earlier rows having dropped half of a
> product rule.  A port check reproduced 119 exactly — **because porting
> the method ports the error.  A port check cannot be an independence
> check** (§B11.6).  Every quotation of 119 in this book is corrected.

**Why the pinned argument failed, diagnosed not hand-waved.**  The sketch
assumed the demand forces `Z(h+e)/Z(h)` to be a function of the two
classes **event by event**.  The record-level demand is **AGGREGATED** —
it equates the class-to-class transfer *summed* over events — so it
constrains **sums, not individual ratios**, and the path-consistency step
never obtains its hypothesis.  **And the aggregated reading is the CORRECT
one**, which is what makes this fatal rather than fixable: what is
observable is the probability of moving from class `s` to class `s'`; a
per-event version would be a demand on unobservable event labels — exactly
what B2 disqualified.  **So the stronger hypothesis the sketch needed is
not available as a record-level demand at all.**

> **Therefore paper 30 §5.7's stationary form is a genuine CHOICE, D49
> round-1 B2's restriction is PERMANENT, and every citation of D49 must
> carry it.**

**The choice is priced a second time, from the descent side `[D65,
§B2.10]`.**  Ask not "what invariance forces the form?" but "what does a
completion have to do for the normalized law to be a measure on records
at all?", and count the answers: at the depth-4 truncation the positive
**repair cone has dimension 573**, the completions that *also* descend
form a **205**-dimensional sub-cone, the `(depth, sigma)` family is a
**28**-dimensional slice of that, and `Zhat` is one ray inside the slice
— with the gap widening at `D = 5` (3,053 vs 32).  **The collapse to one
ray is this section's form choice, and nothing else does it.**  What
D65 adds in D49's favour is that `Zhat` genuinely descends: `μ_Zhat` is
constant on all 5,548 record classes, gated, and not implied by the
square identity (a positive witness repairs every square without
descending).

**Three own defects, owned.**  (1) Run 1 **exited 0 having run no gates** —
D49's module-level `sys.exit` survived the AST strip and killed the
process at D49's verdict; now stripped explicitly and gated
(`_exits == 1`).  (2) Run 2 crashed: D49's `_rank` closes over its global
`NB = 313` and cannot be reused at other truncation depths; the rank is
now width-taking.  (3) The anchor assertion was wrong: 1,191 is
cumulative, **976** at the layer (§B2.5).  **Depth cap declared, not
silent:** `D = 5` (≈5,280 layer histories, boundary dimension in the
thousands) did not finish its exact rank in 10 minutes and was cut; the
2/3/4 trend is monotone and decisive without it.

**UNTOUCHED: D49's existence result.**  A root-free completion exists;
horn (II) holds; paper 30 §5.7's `[OPEN, declared]` is answered
affirmatively.  D50 bears only on uniqueness.

### B6.13 (H0) and (H1) are THEOREMS at two-actor delivery-free scope — the own-view dichotomy `[D61, LOG #455; round 1 TERMINAL]`

*Sources: `note-d60p-h1-probe.md` (the adopted proof note, §3–§9); `note-d61-h1-closure-{pin,result}.md` incl. the pin's §4 first-run and §5 round-1 amendments; `v10/reviews/d61-round1-hostile-review.md`; `v10/code/d61_h1_closure_exact.py` (12 PASS / 0 FAIL, exit 0) and `data/d61_h1_closure_exact.out`.*

**Scope of the numbers in this section, stated once.**  The exhaustive
d42a two-actor family runs to **depth 6: 34,375 histories**.  Invariants
and the conclusion are gated per *history* over all 34,375; case
instances and the dichotomy are gated per *transition*, and a transition
has a parent of depth ≤ 5, so those counts run over the **34,374**
transitions out of parents at depth ≤ 5.  The probe and the round-1
review each carry the conclusion two levels deeper, to **depth 8 —
930,631 histories**.

**THE OWN-VIEW DICHOTOMY (Lemma 2), which is the whole engine.**

> **A candidate's own view is EITHER the initiator's register cone OR the
> FULL view — there is no third case.**  This is a theorem of `regs_of`
> **together with** `arb_components_in_view`'s proposer test, and the two
> halves pull in opposite directions.  Register geometry *alone* produces
> a **third** case: `regs_of(('r', a, C, W))` returns `C`'s **proposers**
> plus the fresh version name, and the proposers need not include the
> initiator `a` — such a candidate's view is the *opponent's* cone plus
> `a`'s version cone, neither the initiator's cone nor the full view
> (**5,712** such candidate views at depth ≤ 5).  What removes the case
> is `admissible`'s route to the `ckey` through
> `arb_components_in_view(view, a)`, which returns only components
> carrying an `a`-proposal: every *admitted* `'r'` therefore has its
> initiator among the proposers, and a pair arbitration then occupies
> both actors' registers and sees everything, while every other admitted
> candidate sees exactly its initiator's cone.

**The proposer test is the load-bearing clause for any extension.**  It
is exactly what a three-actor or transport-scope successor must
re-examine — and at three actors the third case becomes **admissible**
(**5,904** such views at depth ≤ 4), with **only Lemma 2 breaking**; the
rigidity invariants survive there, which is what tells a successor unit
which lemma to attack.

Gated at every instance: **34,374 candidate transitions (parents of depth
≤ 5) — cone 32,342, full 2,032, THIRD CASE = 0.**  And the 2,032
full-view cases are **exactly** the 2,032 "lag" pairs that had been read
as an obstruction (§B3.2): *the dichotomy explains the lag rather than
being defeated by it.*

**On the cone the layer is RIGID (Lemma 5).**  The invariants — `alive_a`
a singleton (5a); at most one live proposal, on `X_a` (5b); no pair-arb
after a self-arb, and the first self-arb of a history on the shared base
(5c); no opponent proposal live in `cone_a` on `X_a`, either bit (5d); at
most one full-view-superseded `X` (5e) — hold at **every one of 34,375
histories, zero violations**, layer-computed per history, and again in
lean form on every history to depth 8.  The case battery gates
**preconditions AND effects** at every cached transition:

| case | instances | precondition / effect violations |
|---|---|---|
| **propose** — on the actor's own alive singleton with no prior live; after it, alive tokens unchanged, exactly one live proposal on `X_a`, opponent untouched | 12,916 | **0 / 0** |
| **self-arb** — consumes a SINGLETON component on that actor's own `X_a`; after it, the actor advances with 0 live and the OPPONENT's state is unchanged with the arb **outside** its cone — the invisible supersession, gated as an effect | 6,484 | **0 / 0** |
| **pair-arb** — sits on a base that is BOTH actors' alive singleton (`X_A = X_B`); after it, both actors advance to the same fresh version and both live proposals resolve | 2,032 | **0 / 0** |
| case exhaustiveness — the menu alphabet is `p`, `r`, `n` | — | asserted as a **code-fact** against `candidates_for`'s source |

The exhaustiveness row is an assertion about the source, not a counter:
`candidates_for` constructs events only via `('n', a)`, `('p', …)` and
`('r', …)` literals, so a counter over enumerated menus could never have
failed and is not offered as evidence.

**This dissolves the standing obstruction.**  The cone-level bits are
indeed not full-view-determined — but rigidity means **only the two
complementary values ever occur**, so the idle weight is constant `3/4`.
The obstruction was real about the bits and inert about the menu.

**Consequently `menu(h) = G(sigma_raw(h))`** for an explicit ~10-line
closed form `G`, gated entrywise in exact Fractions.  **(H1) follows by
equivariance WITH NO DEPTH PARAMETER.**

**The conclusion, gated.**  Equal canonical `sigma` ⟹ **identical**
canonical menu (renamed event-multiset, exact weights), over all 34,375
histories, **exactly 36 sigma classes, zero splits**, with the cumulative
window spectrum `[11, 19, 28, 32, 36]` matching d44a's committed anchor —
and the same gated over **930,631 histories to depth 8** (census
`[1, 6, 32, 176, 976, 5280, 27904, 145408, 750848]`), with zero
sigma-class menu splits, plus sampling to depth 40, renewal-pumping
families to length 44, and adversarial pairs.

**Independently re-verified, layer and all.**  The round-1 review
re-implemented the admission layer from scratch — DFS reachability
instead of the incremental `pred` union, BFS components instead of
union-find, maximal independent sets by extension-closure, explicit
permutation replay for `PK1` — checked it against the committed layer on
all 6,471 histories to depth 5 with **zero menu or poset mismatches**,
and then ran the **entire lemma list** on its own layer exhaustively to
depth 8: every lemma, every invariant including the three the receipts do
not reach that deep, the quarter law, `G` entrywise in exact
`Fraction`s, (H1) **and** (H2) — **zero violations of every one** —
landing independently on **36 sigma states and 176 transition keys**.

**A bonus that runs the other way.**  The quarter law of §B2.7 —
per-actor menu mass in `{1, 5/4}` — is **derived** from `G` (propose
`1/8`, self-arb `1/4`, pair-arb `1/8` in twos; blind groups summing
exactly `1/4`) and re-gated at every history with **zero** off-law
points.  A gated-and-scoped law becomes a **theorem of the closed form**.
And the derivation fixes the *totals*: a `5/4` per-actor mass requires a
two-member full-view component, which by (5b) carries **both** actors'
proposals, so the actors sit at `5/4` together or neither does — the menu
total is **`2` or `5/2`**, and `9/4` is unreachable.

> **`[THEOREM at two-actor delivery-free d42a scope]` (H1) holds.**
>
> **`[THEOREM, same scope]` (H0) is FULLY DISCHARGED.**  Clauses 1–3 are
> corollaries of Lemmas 4/5; clause 4 — conflicting live pairs
> incomparable — is **Lemma 7b**, a three-line proof from Lemma 3's cone
> form plus (5b) plus pair-arb resolution, each step verified against the
> layer.
>
> **WHAT THIS SECTION DOES NOT DELIVER.**  (H2), transition determinism,
> is not proved *here*: D61 left D44a's closure theorem conditional on it
> alone.  §B6.13b is where it is proved, and only with both sections in
> hand may *"residue 1 is closed"* be written — and then only with the
> scope clause (§0.3, §B6.14).

**Three obligations this section hands to the next**, named by D61's
round and discharged in §B6.13b:

1. **The propose-on-a-dropped-base case.**  When `hold[x] = None` and `x`
   has no live proposal, `X_x` is a base `sigma(h)` has *discarded*, so a
   propose on it makes `sigma(h+e)` reference a token the parent does not
   record.  Determinism can survive only if that token is **forced up to
   renaming**.
2. **Fresh version-name non-collision.**  Each arb mints
   `vname(b, W, x)`, and any update table must produce a genuinely new
   base token; a collision would force `x` to have arbitrated `b` before,
   hence `b ∈ superseded` in `cone_x`, hence the arb inadmissible.
   Measured: **44,356 admissible arbs to depth 6, 0 collisions** — and
   the argument, not the count, is what was owed.
3. **Lemma 7b feeding the components**, since `comps(h+e)` is built from
   `edges()`, which is built from `incomparable()`.

**Four scope clauses, all binding.**

1. **Still within the stationary form.**  D50 is untouched: the form
   remains a **choice** (§B6.12), so "the record law is forward-complete"
   still may not be quoted without it.
2. **Transport untouched.**  Nothing here reaches delivery scope.
3. **THREE ACTORS ARE OUT OF SCOPE**, and the wall is now **exhibited**
   rather than asserted: the third view case is admissible there (5,904
   views at depth ≤ 4) and Lemma 2 is the single thing that breaks.
4. **The proof is PROSE-OVER-CODE, not machine-checked logic.**  The
   receipt gates the code-facts against the source, every case claim —
   preconditions and effects — at every cached transition, the
   dichotomy, and the conclusion; the depth-free force comes from the
   register-geometry argument, not from a sweep.  A **Lean-grade
   mechanization is a stated residue.**

**An over-promise, recorded rather than hidden.**  The pin said
"mechanize the induction", twice over-promising: run 1's hand-rolled
abstract state was **coarser than sigma** (1,932 menu mismatches), and —
the deeper point — *any* cache-gated state machine leaves exactly the
depth gap (H1) always had.  The deliverable was restated accordingly, and
the round then restated the *consequence* sentence the same way: the
mathematics survived everything thrown at it; the sentence it was sold
with did not.

**Standing: round 1 TERMINAL.**  The paper 30/32 updates remain queued.

### B6.13b (H2) is a THEOREM — the update table, and residue 1 CLOSED at that scope `[D62, LOG #457 → #460; round 1 TERMINAL]`

*Sources: `note-d62-h2-update-table.md` (Row 0, rows R1/R2/R2′/R3/R4, obligations O1/O2/O3, the §7 assembly); `note-d62-h2-update-table-pin.md` (STRICT, frozen first); `v10/reviews/d62-round1-hostile-review.md`; `v10/code/d62_h2_update_table_exact.py` (24 PASS / 0 FAIL, exit 0) and `data/d62_h2_update_table_exact.out`.*

> **`[THEOREM, two-actor delivery-free d42a scope]` (H2).**  For every
> history `h` of ANY depth and every event `e` admissible at `h`,
> `sigma(h + [e])` is a function of `(sigma(h), e renamed into
> sigma(h)'s token language)`.

**What the table transforms.**  `sigma = canon_sigma` is the minimum over
base bijections of `ser()`'s serialisation, and the **serialised state**
`Σ` is exactly what `ser()` writes — no more.  In a token language
`m : refs → {0,…,k−1}` (`k ≤ 2` here):

| field | content |
|---|---|
| `hold` | per actor, its own alive token, or `None` when that token is **full-view** superseded |
| `live` | the live-proposal triples `(proposer, token, bit)` |
| `comps` | the conflict components `(token, members, edges)` |
| `sup∣refs` | the superseded **flag** of each *referenced* token, `refs` being held-or-live-carrying bases and nothing else |

`Σ` is a **lossy** projection: dropped superseded marks are gone.  The
table is legitimate only because **no row ever consults a dropped mark** —
the rows *read* a flag in exactly one place (R3's precondition disjunct,
on a token that is in `refs` by construction) and *write* flags in two,
where the written value is **computed, not looked up**.  Read-versus-write
is the distinction that makes the claim true.

**THE TABLE — five rows, a partition of the event alphabet by
`(tag, base ∈ refs?, |proposers(ckey)|)` with no fall-through.**  Write
`x` for the actor, `y` for the opponent, `L_a` for `a`'s unique live
triple, `v` for the freshly minted version.

| row | event | `hold` | `live` | `comps` | `refs` | `sup∣refs` |
|---|---|---|---|---|---|---|
| **R1** | `('n', x)` idle | — | — | — | — | — |
| **R2** | propose on a **held** base | — | `+ (x, b, i)` | `f(live')` | — | — |
| **R2′** | propose on a **dropped** base | — | `+ (x, b, i)` | `f(live')` | `+ b` | `b ↦ True` |
| **R3** | **self**-arb on `b` | `x ↦ v`; `y ↦ None` iff `hold[y] = b` | `− L_x` | `f(live')` | recomputed | `b ↦ True`, `v ↦ False` |
| **R4** | **pair**-arb on `b` | `A, B ↦ v` | `= ()` | `= ()` | `= {v}` | `v ↦ False` |

Every row is a `[PROOF]`: each step is either a quoted line of the
committed layer (`vname`, the `arbs` loop that builds `superseded`, the
`live` comprehension, `holdings`, the `edges` bit predicate,
`prop_options_in_view`'s two skips, `arb_components_in_view`'s
supersession skip and **proposer test**, `admissible`'s ckey match) or a
named theorem of §B6.13 (Lemma 1(c), Lemma 2, Lemma 4, Lemma 7b,
invariants 5a–5e).  **No step is an induction on depth and no step reads
the history.**

**Row 0, the prerequisite:** `comps(Σ) = f(live)` — group live triples by
base; a base carrying two triples with **opposite** bits yields one
2-member component with one edge, everything else a singleton per triple.
This holds because `edges()` requires same base, opposite bits **and**
incomparability, and **Lemma 7b** makes the third conjunct automatic.
**So the table never transports an order relation** — that is obligation
O3, discharged.  Gated at all 34,375 states, 0 failures, with the
same-bit branch non-vacuous (2,236 states).

**R2′ is the whole difficulty, and O1 is its discharge.**  Its
precondition is `hold[x] = None` with no live `x`-triple: `x`'s own token
is alive in `cone_x` but superseded in the full view — **the invisible
supersession** of §B3.2, the opponent having self-arbitrated the shared
base.  The dropped token is not in `refs`, so `Σ` does not mention it;
the row is still deterministic because

1. `X_x ∈ sup` follows from `hold[x] = None`;
2. `X_x ∉ refs`: the opponent's token differs from it (both
   full-superseded is excluded by **(5e)**) and every live base is its
   proposer's `X` by (5b);
3. therefore the successor's new flag is **computed**, not recalled; and
4. the renaming is choice-free **by construction** — `canon_pair` renames
   the extras of *one* event and a propose has one base, so `|extras| ≤ 1`
   unconditionally and the single name `100` is assigned with no residual
   choice.

Gated at all **9,656** R2′ instances, 0 violations — and that 9,656 is
*exactly* D51's count of cone-extra propose options caused by missed
supersession (§B3.2): the dropped-base proposes **are** that excess,
identified as a row of the update rather than measured as an anomaly.

**O2 — a minted version name can never collide.**  Suppose
`v = vname(b, W, x)` equals a base already present.  `V0` is a 2-tuple
and `vname` returns a 5-tuple, so the collision partner was minted by some
arb `h[j]`; tuple equality then forces `h[j]` to be an arb **by `x` on the
very base `b`** (though not necessarily the same event — `vname` keys on
the winner, not the ckey).  If `e` is a pair-arb its view is the full view
and contains `h[j]`; if `e` is a self-arb its view is `cone_x`, and `h[j]`
was itself admitted, so the proposer test puts `x` among its proposers,
so `regs_of` puts `h[j]` on register `x`, so Lemma 1(c) puts it in
`cone_x`.  Either way `b` is superseded in `e`'s own view, the
component is skipped, the ckey match is empty and **`admissible` returns
`False`** — contradiction. ∎  Gated: **44,356** admissible arbs, 0
collisions; the premise attacked adversarially over 157,888 arb events of
which **49,964** would re-mint a present name (11,584 of them not in `h`
at all) and **every one is refused**; and a named witness shows the
obligation is not vacuous — at `h = [pA(v0,0), pB(v0,1)]` a self-arb and a
pair-arb are *both* admissible and mint the **same** name, each excluding
the other once it fires.  *The collision is excluded by admissibility, not
by luck.*

**The assembly.**  Extend the token language over the one new token
(fresh by O2, or the re-imported dropped base by O1); row correctness
gives `Σ_{m'}(h+e) = F(Σ_m(h), e^{m'})`; `F` only copies tokens,
introduces one fresh one and computes flags, so it is **equivariant**
under relabelling; `canon_sigma` minimises over relabellings on both
sides, so the two minima agree.  Well-definedness of the input needs only
that *some* attaining renaming realises `canon_pair`'s output — no
uniqueness required.  **Hence `sigma(h+e)` is a function of
`(sigma(h), renamed e)` at every depth, and the argument mentions no depth
anywhere. ∎**

**Two corollaries the table hands over.**

- **The arbitration WINNER is invisible to `sigma`.**  R3/R4 use the
  winner set `W` only through `vname(b, W, x)`, which the table abstracts
  to one fresh token — so `sigma(h+e)` does not depend on `W` at all.
  (The `PK1` kernel split moves menu *weight* between winners; it never
  moves the successor **state**.  No claim is made here about the chain's
  weights.)
- **Every pair-arb is a RENEWAL to the root state.**  R4 outputs
  `hold = {A: v, B: v}`, `live = ()`, `comps = ()`, `refs = {v}`,
  `flag(v) = False` — serialisation-identical to `sigma([])`.  **D44a's
  renewal/pumping structure is a ROW OF THE TABLE**, derived rather than
  measured — which puts §B6.8's renewal isomorphism, and with it §B6.10's
  root-freeness, on a proof rather than on a coincidence.

**The evidence base, and what it does and does not buy.**  The receipt
gates the table against the layer at all **179,782** cached transitions
into depth 7 (string-identical serialisation, 0 mismatches), the anchors
(**176** keys / **36** states), closure, Row 0 at every state, the row
preconditions at every instance by an *independent* classifier, and a
frontier-exhausted BFS on `sigma`-space (36 states, 176 edges).  Eleven
mutants are detected: five gate-predicate mutants each fail their owning
gate, and the six **row** mutants each fail two gates together, because
the BFS re-runs the same table.  **That BFS is not independent evidence —
its one-representative-per-class shortcut is licensed *by* (H2)** — and
the receipt prints that sentence at the gate.  The theorem force is the
rows.  An honest map of which of the 24 gates can genuinely fail is
carried in the note: three are corollaries or tautologies and are kept as
printed reporting lines, not counted.

**Independently re-implemented, and two levels deeper.**  An independent
re-implementation — the serialised state, its canonicalisation and **all
five rows built from the prose above alone**, in a different normal form
sharing nothing with the receipt — reproduces the table's prediction
against the layer's own `sigma(h+e)` with **0 mismatches on 4,778,310
transitions into depth 9**: 176 keys, 0 keys carrying two successors, 36
states at every level, an induced partition matching d44a's exactly in
both directions, and the row census reproduced to the unit.  On that
independent surface O2 is re-run **2.3×** wider than the receipt's, still
0 admitted, and the `sigma`-minimising renaming is **unique on all
4,778,311 histories** — the step the pin flagged as the highest residual
risk.  And the one attack the pin invited on O1 — long chains of
invisible supersession — is **structurally impossible**: drop onsets per
history never exceed 1.

> **THE VERDICT, with its scope clause, which is part of it.**
>
> **(H0) `[DISCHARGED]` + (H1) `[THEOREM]` (§B6.13) + (H2) `[THEOREM]`
> (here) ⟹ D44a's CLOSURE THEOREM IS UNCONDITIONAL AT TWO-ACTOR
> DELIVERY-FREE d42a SCOPE.**  The 36-state closure, the six-state chain
> and the Perron package hold **at every depth** there.  **RESIDUE 1 —
> open since D44 — IS CLOSED AT THAT SCOPE**, and D49's root-free
> completion is unconditional at every depth there.
>
> **Still inside the stationary FORM** (D50: the form remains a choice,
> §B6.12).  **Still delivery-free** — transport untouched, §B9's walls
> stand.  **Three actors out of scope**, the wall exhibited at §B6.13.
> The remaining residue of the (H1)/(H2) pair is the **Lean-grade
> mechanization**, inherited unchanged: (H2) has exactly the standing (H1)
> has and no better — the rows are proofs, the invariants they consume are
> theorems of the same style, and no machine has checked the induction *as*
> an induction.

### B6.13c The two routes that failed first, and what they left

Both are in the graveyard (§B10.2, §B10.3); what matters here is which
of their content survives into the proof above.

- **The `tau` own-view route `[D46a]`** established the lag as a real
  object — the menu view strictly exceeds the noop cone on 1,016 of
  12,942 actor-histories, all extras opponent-authored (§B3.2).  **That
  measurement is explained**: those are dichotomy full-view cases.
- **The wire-closure route `[D51]`** measured that every event type lags
  and that a smaller view can yield *more* options — by **missed
  supersession**, not by a missed own proposal (§B3.2) — so no argument
  may assume the lagged view sees a subset.  Both stand.  **What does not
  stand is its reduction**: the four menu-relevant projections
  **REFINE** `sigma` rather than being determined by it (209 projection
  keys against 32 states), so (H1) was **not reduced in the claimed
  direction**.  Its durable content is three refutations, not a
  reduction.
- **Neither proof is touched by either failure**, because both go through
  `sigma` **directly** — never through the projections, and never through
  the own-proposal clause.  §B6.13's self-arb case and §B6.13b's row R2′
  both name the **invisible supersession** as the mechanism, which is what
  the measurement says; and D51's 9,656 excess options reappear as R2′'s
  instance count, to the unit.

### B6.14 Scope, to be carried at every citation

- **d42a scope, delivery-free, TWO ACTORS.**  **CLOSED**: (H0) is fully
  discharged and (H1) is a theorem (§B6.13), (H2) is a theorem
  (§B6.13b), so **D44a's closure theorem is unconditional there** and
  `Zhat` holds **at every depth** there.  Three clauses travel with that
  sentence and are part of it: it is still **inside the stationary form**,
  which remains a **choice** (§B6.12), so "the record law is
  forward-complete" still may not be quoted without the form; it is still
  **delivery-free**, and §B9's walls stand untouched; and **three actors
  are OUT OF SCOPE** — the own-view dichotomy fails there, the third view
  case becoming admissible.  Nothing above may be quoted wider.  The
  line's one residue is the **Lean-grade mechanization**: both proofs are
  prose-over-code, gated against the source rather than machine-checked.
- **And what descends, at that same scope.**  `Zhat`'s measure is a
  function of the **record** — constant on all 5,548 record classes
  (§B2.10) — while the *uncompleted* normalized kernel is not, by exactly
  one mass-ratio coboundary.  Both halves travel together: quoting the
  first without the second makes the completion look like a formality,
  and quoting the second without the first reads as a defect in the
  settled law rather than in the object it completes.
- **And what does NOT sit above it, at that same scope.**  The space of
  paper-29-shaped functionals over this layer is measured (§B2.11), and
  two clauses travel with any citation of it: the space is **large,
  structureless and measure-independent** — it is a fact about the record
  functor and the prefix map, not about `Zhat` or about the closed law —
  and under the first fair **dynamical** demand its coherence dimension is
  **zero at every truncation tried**, so **a quantum layer here cannot be
  both state-generated and coherent.**  Neither clause may be quoted
  without its reading, its depth and its functor.
- **Transport scope (d42b1) is OPEN.**  Paper 32 §2.3's escape result
  stands untouched: deliveries reopen the absorbing sector (a three-event
  history — propose; blind self-seal; deliver the created version across —
  reconverges diverged holdings at exact weight `1/256`; census 1,044
  diverged histories, 124 reconverging `(history, delivery)` pairs over 84
  distinct diverged prefixes, 4 distinct minimal chains all at `1/256`),
  the window chain **escapes** (68 transitions from shallow parents land
  in 5 classes first realized at length 3), and the menu-shape shortcut
  **breaks** (zero of the 3,969 transport menus match any delivery-free
  menu shape).  §B9 adds the design-independent no-go.
- **Two-of-two breadth discipline.**  D42b7's second grammar (ternary
  payloads) has no state chain, so `λ = 2` and `f = (4,4,3,7,3,3)/3` are
  **toy-relative values**.  What is claimed to generalize is the **form**
  — a unique Perron completion — **not the numbers**.
- **And the laboratory block is untouched.**  A settled measure is not a
  bridge to a laboratory (§B10.7).  What changes is only that the
  completion is no longer the reason why.

---

## B7. The dimension ladder

*Non-technical twin: Part A, chapter A7.*
*Sources: `note-d45b-sn-ladder-polyhedral-confinement.md` §1 (the binding doctrine); `note-d46d-typicality.md`; `note-d54-dilworth-gate-{pin,result}.md`; `v10/reviews/d54-round1-hostile-review.md`; `note-d55-dimension-meter-{pin,result}.md`; paper 32 §3.*

### B7.1 The doctrine `[binding on all dimension claims in this line]`

Quoted in substance from `note-d45b…` §1:

- "`d` clocks" — an intersection of `d` linear orders, i.e.
  Dushnik–Miller (order) dimension `d` — is the dominance order of the
  positive **orthant** in `R^d`: polyhedral geometry.  The 1+1 light cone
  is polyhedral (two null rays), and **DM-dimension ≤ 2 ⟺ 1+1-Minkowski
  embeddability, exactly** (the corpus two-clock theorem; Meyer
  `[LITERATURE]`).
- Every Minkowski space with ≥ 2 spatial dimensions has a **round** cone:
  crowns `S_N` of **every** size embed (the antipodal construction: `N`
  events on a circle at `t = 0`; the `i`-th upper event above the
  antipode of the `i`-th lower, at a height between the largest and
  second-largest spatial separations), so its causal order has **infinite
  DM dimension**.  DM dimension and Minkowski dimension coincide **only
  at 2** (Meyer); dimension-3 orders exist that embed in **no** Minkowski
  space (Felsner–Fishburn–Trotter `[LITERATURE]`).
- **Therefore order dimension is a 1+1-ESCAPE DETECTOR and a
  CLOCK-COMPLEXITY GRADE — never a spacetime-dimension estimator.**
  *"3+1 spacetime is not four clocks; it is infinitely many."*  Unbounded
  `S_n` growth is **necessary** for any ≥ 2+1 reading of generated records
  and **not sufficient**.

This is the user's binding observation, and it is the reason the whole
line was re-founded on skies rather than on clock counting.

### B7.2 The collapse of dimension COUNTING as a physics instrument

**D46d** was the decisive experiment for the counting line, and its
headline was retired.  Round 1 (frozen at
`reviews/d46bd-round1-hostile-review.md`, REVISE 2B/4M/5m/2n):

- **BLOCKER D-A1: the headline could not fail.**  "Width spreads with
  depth" chained four exact numbers under the completed law at four
  different `(pool, depth)` pairs to one sampled number under the local
  law at a fifth, and switched statistic on the way.  Touched-width is
  **monotone non-decreasing in depth**, so the claim is a near-tautology,
  and *a control that cannot fail is not evidence*.  The referee's
  like-for-like series (pool 6, one law, growing depth) runs **0.027,
  0.242, 0.578, 0.903, 0.978, 1.000** by depth 10 — now gated *as* a
  near-tautology.
- **The DISCRIMINATING scalings point the other way `[SAMPLED]`.**  At
  fixed depth 8, pools 3–8, full-width mass **falls** — `0.963, 0.782,
  0.568, 0.333, 0.137, 0.037` (touched) and `0.525, 0.238, 0.105, 0.030,
  0.005, 0.003` (delivery-joined), both gated strictly decreasing; on the
  diagonal `depth = 2 × pool`, `0.867 → 0.623` (touched) and
  `0.340 → 0.073` (delivery-joined).
- **BLOCKER D-A2: "the theory's OWN law" was not established.**  The unit
  used two different normalizations — lookahead-completed for the exact
  arm, local for the sampled arm — and called both the theory's own law.
  Repaired by quoting the committed layer's *"no measure claim"*
  docstring from source and naming the normalization at every typicality
  statement.
- **MAJOR: the proxy counted IDLERS**, and the measure is ~50% idle.
  Three proxies side by side, pool 6 / depth 8, `N = 4,000`
  `[SAMPLED, declared seed]`: **0.9808 / 0.3068** (touched) →
  **0.6720 / 0.0765** (non-idle) → **0.4138 / 0.0305**
  (delivery-joined).  Idle mass is now labelled a **confound, never
  support**.
- **Direction stated:** width ≥ 4 is **necessary, not sufficient** for
  dimension, so those numbers **upper-bound** the dimension mass.

> **DELIVERED READING (post-round):** what is typical-in-the-making is
> **order dimension ≥ 3**, not D45b's unbounded dimension.

**What survived the attack, reported as such by the referee:** the
calibration horn did not fire (completed-vs-local gap computed at 14
`(pool, depth)` pairs, `2.73e−4` and `2.84e−4` at the sampled pools,
could not be made to grow); the sampler is sound.

### B7.3 The Dilworth gate `[THEOREM, unconditional at transport scope]`

> **Theorem (D54 §1).**  At transport scope (d42b1), fix any history, any
> base event `e`, and any sky whose direction set is an **antichain** in
> the event poset.  If the record has `k` actors, then the sky's shadow
> family is a **union of at most `k` chains under inclusion**.
> Consequently: realizing all `2^m` subsets of an `m`-element direction
> set as traces — in particular, shattering — requires at least
> **`C(m, ⌊m/2⌋)`** actors.  **Shatter-4 requires at least 6 actors.**

**Proof.**

*(i) The physical step.*  **Any two events sharing an actor wire are
comparable.**  This is a **theorem of the layer**, not merely a gated
fact: `event_poset` chains every register by
construction (same-register events are ordered by history position,
transitively), and **every event's initiator is among its registers for
all five event types** — so same-initiator ⟹ same register ⟹ comparable,
always.  The Stage 0 sweep (**218,795** actor-sharing pairs, zero
violations, deliveries' two-carrier case included) is **corroboration of a
proved step**; the round verified the stronger register-sharing form too
(**226,223** pairs, zero violations) `[REFEREE-CARRIED]`.

*(ii)* Assign each event to its initiating actor.  By (i) the events
assigned to one actor are totally ordered, so their **reflexive**
down-sets are nested (`x ≤ y ⟹ down(x) ∪ {x} ⊆ down(y) ∪ {y}`), so the
traces they contribute — `{c ∈ dirs : c ≤ f}`, exactly the committed
instrument's **reflexive** definition — form a **chain** under
inclusion.  The full
shadow family is covered by at most `k` chains, one per actor.  When
shattering is tested on a subset `S` of a larger direction set, the
restriction `r ↦ r ∩ S` is **monotone**, so chains map to chains and the
bound transfers.

*(iii)* A chain contains at most one member of any antichain.  The middle
layer of the Boolean lattice `B_m` is an antichain of size
`C(m, ⌊m/2⌋)` — constructively verified for `m ≤ 6`, with the
**de Bruijn–Tengbergen–Kruyswijk** recursion simultaneously exhibiting a
chain **partition** of the same size, so the count is exact both ways.  A
family realizing all of `B_m` therefore needs at least that many chains,
hence at least that many actors.  ∎

**Scope of each step:** (iii) is classical mathematics, exact for every
`m`; (ii) is bookkeeping given (i); (i) is a theorem of the layer.  **So
the theorem is unconditionally exact at transport scope.**

**The sweep corroboration, and its declared limit:**
15,909 skies, 33,546 per-actor groups, **zero non-nested pairs** — but
**no swept sky reaches 4 directions or more than 7 distinct traces**, and
61.4% of groups are single-trace.  So the 16-trace regime is covered **by
the proof** and by direct checks on the constructed records, **not by the
sweep** — which the T-LEMMA gate prints and declares.

### B7.4 The sphere consequence: withdrawn, then rescued by counting

**As first stated (LOG #427/#428):** *"a sphere-like sky (shattering at
every `m`) requires unboundedly many actors — the infinite-clocks doctrine
is now a THEOREM."*

**BLOCKER 1 of round 1: the antecedent is satisfied by no 2-sphere sky.**
Caps on `S²` are halfspace traces with **VC dimension 4** — they shatter 4
points and **never 5** — certified in the round by an exact Radon partition
on rational sphere points: affine dependence
`λ = (−23/49, −19/49, −24/49, 17/49, 1)`, Radon partition
`conv{3,4} ∩ conv{0,1,2} ≠ ∅`, so `{3,4}` is cut off by **no** halfspace;
an independent grid search finds **30/32** traces present, missing exactly
that pair `[REFEREE-CARRIED]`.

> **So the Sperner route never fires on the sphere**, and the
> infinite-clocks doctrine is not a theorem by that route (§B10.8).

**The conclusion holds by TRACE COUNTING instead — no shattering anywhere
in the derivation `[REFEREE-CARRIED, verified in the round]`:** a sphere
sky on `n` directions realizes `2·Σ_{i≤3} C(n−1, i) = Θ(n³)` distinct cap
traces (checked against brute-force arc enumeration at `d = 2` and against
d47a's tetrahedron count of 16 at `d = 3`), while the nested-trace lemma
caps one actor's chain at `n+1` traces.  Therefore

> **actors ≥ Θ(n²) → ∞: a sky rich enough to be a 2-sphere still requires
> unboundedly many actors.**

Promoting this bound to an in-receipt gate is residue 1b, still
`[REFEREE-CARRIED]`.

### B7.5 What width prices, and what prices dimension

The same counting prices a **2+1 circle** sky at `n² − n + 2` arc traces,
hence `≥ n − 2` actors — **also unbounded.**

> **Width is the provable price of SKY SIZE, not of dimension.**

**The dimensional signal is the shatter OFFSET alone:**

| shadow system | shatters | actor floor `C(k, ⌊k/2⌋)` |
|---|---|---|
| arcs on a circle | 3 | **3** |
| caps on `S²` | 4 | **6** |
| caps on `S³` | 5 | **10** |
| halfspaces in `R^d` | `d + 1` | `C(d+1, ⌊(d+1)/2⌋)` |

Three versus six versus ten — **a factor, not a divergence.**  And the
ladder continues upward, which is what makes "max shatter" a **meter**:
for **continuum trace systems**, 3 = circle-compatible, 4 = sphere,
5 = `S³`, `k` = `S^(k−1)`.  *Does transport admit shatter-5?* is exactly
the question §B8.4 answers.

> **What the meter reads, stated exactly, in two parts.**  **(1) On
> sprinklings it reads geometry.**  §B5.7 measures the discrete ladder on
> genuine sprinkled Minkowski records and recovers exactly the continuum
> table above — 3 in `M^{2+1}`, 4 in `M^{3+1}`, 5 never — with a
> size-controlled two-sided separation.  **(2) On the framework's
> engineered records it reads coordination.**  Those reach 5 (§B8.4),
> above every sprinkling of any dimension tested, and no claim that such
> a record *is* four space dimensions follows: what exceeds the sprinkling
> rungs is worldline coordination, which random causal structure does not
> produce.

**Sphere calibration, exact (D55 A2):**

- **A2a:** `B₄` realized by **16 exact rational caps on `S²`** (d47a's
  rational tetrahedron) — so D54's record upgrades from "not an arc
  system" to **sphere-compatible**.
- **A2b `[THEOREM, certificated twice]`:** **no five points shatter on
  `S²`** — exact affine dependences with non-empty sign splits on **two**
  rational configurations, plus a third configuration re-derived in the
  round by a different method; Radon closes it, and five points in `R³`
  always carry a dependence.
- **A2c:** `B₅` realized by **32 exact rational caps on `S³`**
  (`e₁..e₄` and `(−½,−½,−½,−½)`).
- **A2a and A2c are SCALE calibrations, not record-specific facts**: any
  ≤4-direction family fits `S²` and any ≤5 fits `S³`, so the
  record-specific content is entirely in the realization of **all** of
  `B₅`.

### B7.6 The older transport-dimension results, for completeness

Paper 32 §3 and paper 31 §5, all at **tested scale** and under the §B7.1
doctrine:

- **Arbitration alone cannot generate dimension** — zero failures of
  two-dimensionality across **1,124,884** distinct admissible
  proposal/arbitration histories, via the **component-confinement law**
  (five clauses gated, the sixth referee-carried), yielding the **funnel
  lemma**: the crown `S3` is impossible as an induced subposet at every
  width and depth `[REFEREE-CARRIED]`.
- **Transport generates dimension without ceiling** — one uniform
  constructor (the two-hop dedicated-courier firewall) realizes `S_n` as an
  induced subposet of an admissible pure-transport record at every
  `n ∈ {3,4,5,6}`: actors `n² + 3n`, events `2n²`, width `2n − 1` at the
  base cases `[MEASURED — the width formula is NOT claimed at all n]`,
  every event admission-priced at the uniform exact weight
  `1/(4(n² + 3n − 1))`; `[THEOREM, all n, at the schema level]`.
- **Sharp finite thresholds** (paper 31 §5.3) `[EXACT]`:

| actor width | dimension behaviour |
|---|---|
| 2 | `dim ≤ 2` always `[THEOREM via width]` |
| 3 | `dim ≤ 2` through 10 events |
| 4 | first failure at 6 events (`W4`: weights `(1/12,1/12,1/8,1/8,1/12,1/12)`, predecessors `[[],[],[0],[0],[0,1,2],[0,1,3]]`) |
| 6 | `S3` realized by pure transport (`W6`: six deliveries at weight `1/20` each, predecessors `[[],[],[],[1,2],[0,2],[0,1]]`) |

- **The schedule resolution:** ported at face value, the Charron-Bost
  dimension-`N` pattern `[LITERATURE]` is fully admissible yet its posets
  are two-dimensional — a **schedule** fact, not a semantics fact.
  Sweeping all `8! = 40,320` orderings of the same admissible
  multiset-with-marks at four actors, **248** reach order dimension 3.
  Schedule-independent: her designated crown dies under every ordering; no
  induced `S3` exists anywhere in the sweep; and **bare deliveries never
  escape two clocks — the idle marks are load-bearing**.  The true
  semantic divergence: the sends-before-receives schedule that realizes
  her crown in the one-way model is **inexpressible** under the grammar's
  fused two-carrier deliveries, and the crown price is paid in dedicated
  couriers — **quadratic, not linear, in `n`.**
- **The funnel lemma's promotion is PARTIAL (D44c-P, LOG #407/#412; paper
  32 §6 item 7 amended, not closed).**  Met: the sixth confinement clause
  and up-cone confinement are now gated in-receipt at zero violations over
  three committed exhaustive families (551,928 / 224,580 / 436,864), with
  the live stratum gated **first** at **23,226** incomparable arbitration
  pairs so the zeros are results, not vacuities.  Delivered: an
  **arbitration-scoped** scale-free crown no-go with a constructive
  two-pre-order proof (the reversal of the **root** order, not only the
  child order, is load-bearing — gated as near-miss mutant FG7(d)),
  corroborated grammar-independently over all **46,233** rooted forests on
  ≤ 8 nodes.  **Not met:** paper 32 §3.1's claim is **full-poset**, the
  full poset is not a rooted forest, and both natural register-theoretic
  bridges are **false** (a causal pair need not share an actor register,
  since a link may be carried by a minted version name; and domination is
  transitive, so a proposal reading a minted version name inherits the
  whole down-set).  **So the crown no-go remains REFEREE-CARRIED and the
  multi-author corner remains decided at TESTED SCALE.**
- **The in-family evidence for that theorem is empty, and is labelled so:**
  the 67,403 certified arbitration subposets have
  sizes `{1: 44,546, 2: 19,796, 3: 3,061}` — **maximum 3 elements** — and
  the smallest poset of dimension > 2 is the 3-crown at **six** elements,
  so every verdict was fixed **by cardinality alone**.  Evidence stratum
  (size ≥ 6) = **0**.  The stratification is printed and gated so that
  the count may never be quoted as in-family confirmation.  A related
  finding in the parent's favour: **230,706 cover pairs, ZERO with
  disjoint actor register sets**, so the actor word determines the cover
  relation and hence the poset — D44c's declared dedup convention is now
  **confirmed by measurement** rather than assumed.

---

## B8. The constructions

*Non-technical twin: Part A, chapter A8.*
*Sources: `note-d54-dilworth-gate-{pin,result}.md`, `v10/code/d54b_shatter_construction_exact.py`; `note-d55-dimension-meter-{pin,result}.md`, `v10/code/d55_shatter5_exact.py`, `v10/code/d55b_sphere_calibration_exact.py`; reviews `d54-round1`, `d55-round1`.*

### B8.1 The pinned blueprint, and why it failed (gated exhibit N1)

The pin committed a **9-actor blueprint** (X, A1..A4, B1..B4) rather than
a blind search: X proposes on `v0` and arbitrates it — that arbitration is
the base event `e`, minting `v1`; X delivers `v1` to A1..A4; each `Ai`
pads with idles and proposes on `v1` so that all four proposals land at the
**same height** `e+5`, hence **pairwise incomparable by proposal
locality** (a proposal's only carrier is its proposer); those are the four
directions of SKY-B(5) at `e`; then accumulators B1..B4 realize the
missing subsets by re-deliveries, one symmetric chain each, with X's first
delivery serving as the **empty trace**.

**It is admissible end to end — 31 events, all menu-offered — and it
realizes only 8 of 16 subsets.**

**Mechanism: a delivery is a join in BOTH directions** (§B3.4).  The
sender's wire absorbs the receiver's accumulated past, so after B delivers
into an accumulator holding A, every later send from B carries `{A,B}` and
the other chains are contaminated before they start.  **The per-sender
send-traces form a chain: the theorem biting its own construction.**  The
first-run failing output (9 PASS / 3 FAIL) is preserved at commit
`e07582c`.

### B8.2 The courier architecture

**Sending into an EMPTY receiver folds nothing back** — the sender stays
clean.  So each direction-actor mints one **fresh courier** per
contaminating step, and each courier performs exactly one send into a
charged accumulator.  Eleven couriers suffice at `m = 4`.

> **`[EXACT]` A 20-actor, 42-event transport record, every event selected
> from the committed layer's own menu, whose SKY-B sky at the minting
> event has 4 pairwise-incomparable directions, 16 distinct traces
> including the empty one (capacity satisfied), realizes ALL 16 subsets, and
> returns a shattered 4-set — at THREE depths, `d = 4, 5, 6` (round-1
> MINOR 2; the promised per-`d` table is now gate K11).**

**Consistency checks.**  The record's traces decompose into per-initiator
chains with zero crossings; **the realized 16-trace family's minimum chain
cover is EXACTLY 6 — Dilworth-tight**, so **the 6-vs-20 gap is
architectural**: the scheduling cost of backflow, not slack in the
family; and SKY-A/SKY-C on
the same record have **no empty trace** (`[THEOREM-PASS]` per D53 — a
consistency exhibit, not evidence).

**Independent verification (round 1, the corpus's first independent-model
round).**  Every number reproduced by code the reviewer wrote: both records
rebuilt from the committed menu, the poset re-derived with Floyd–Warshall,
16 distinct traces, shattered 4-set confirmed by code sharing nothing with
d47a but the definition; the negative exhibit and its backflow mechanism
re-derived (`B`'s per-initiator family `{}, {B}, {A,B}`, literally
`regs_of(d) = {s, r}`); blueprint fidelity to the pin; measure-freeness;
and record fidelity (pin genuinely preceded code; every LOG number
matched).

### B8.3 The generalized builder

D55's builder is **mechanical from `scd(m)`** — the symmetric chain
decomposition — with no hand tuning: **one accumulator per dBTK chain, one
clean courier per contaminating step**, cost `(|S1| − 1) + (len − 1)` per
chain.  For `m = 5`: 10 chains, 26 couriers, 42 actors, 84 events.

**Anchor first:** the builder re-derived `m = 4` (22 actors, 44 events,
all 16 subsets, shatter confirmed — the same trace family as D54's
hand-built record, at slightly higher actor/event cost because the machine
does not hand-optimize).

**Tractability, and the exact sense in which it is sound.**  The builder
uses **initiator-restricted menus**, and two facts about them are
load-bearing.  The restricted menu must include the delivery's
**receiver** (`candidates_for` enumerates receivers from its actor list).
And `admissible()` **does** read the actor list in the delivery branch, so
**weights differ** between restricted and full calls (e.g. `1/328` vs
`1/8`); **what is preserved is MEMBERSHIP** — proved, and swept over
**354,319** comparisons with **0 mismatches** — and the builder **discards
weights**, so the record is unaffected.

### B8.4 The shatter-5 record `[EXACT]`

> **A 42-actor, 84-event transport record (10 accumulator chains, 26
> couriers), every event selected from the committed layer's own menu,
> whose SKY-B sky realizes ALL 32 subsets of its 5 pairwise-incomparable
> directions and returns a shattered 5-set — at depths 5, 6 and 7.**
> Dilworth-consistent: per-initiator traces are chains, ≥ 10 contributing
> actors (the gate's price, paid), the realized family **Dilworth-tight at
> exactly 10 chains.**

**And it is FORCED.**  The independent round rebuilt the record with the
**full 42-actor menus at every one of the 84 steps** and obtained an
**identical** record: **every specification had exactly one menu hit
(max hits = 1)**.  Also re-derived: the record's own poset closure equals
the layer's; 32 traces / all 32 subsets / a **unique** shattered 5-set at
`d = 5, 6, 7` and **nowhere else in 1..17**; minimum chain cover exactly
**10** (and **6** for `m = 4`); all **48** cap certificates and both Radon
dependences re-derived by a different method plus a third configuration;
pin-before-code confirmed in git.

**Two reporting disciplines the receipt enforces:** the `m = 5`
menu-equivalence samples are gated on the `m = 5` build itself, and the
per-depth table runs the record's **full height range 1..17** — no silent
caps.

### B8.5 What is licensed, stated exactly

**MAY:** the transport layer admits
a record whose SKY-B sky **is not an arc system** — arcs realize at most
**14 of 16** traces on any 4 points, missing the crossing pairs (theorem,
re-verified in the round).  *"Not a 2+1 celestial sky"* holds **only**
under the strict stipulation that a 2+1 sky means an arc system on the
circle of directions — and the corpus's own demotion (§B5.3) shows a
**majority** of genuine discrete 2+1 skies are non-arc, so that
stipulation must be **said aloud**.

**The sound discrete separation is EMPIRICAL, and it has controls:**

**Where these records sit against genuine sprinklings (§B5.7).**
Sprinkled `M^{2+1}` reaches shatter-3 and never 4; sprinkled `M^{3+1}`
reaches 4 and never 5.  **These constructed records reach 5** — above
both, and above the rung the 2-sphere's own geometry permits (caps have
VC dimension 4).

So the separation from real spacetime is genuine and it is *by one rung
above the top of the sprinkling ladder*, not by the sprinklings reading
nothing.  What is demonstrated is **capacity for coordination no random
causal order of any tested dimension exhibits** — which is the licensed
claim below and the whole of it.

**MAY NOT.**  *"The admissibility layer does not select 3+1"* is **not**
licensed: it would need *"not cap-realizable on `S²` ⟹ not a 3+1 sky"* —
the stipulation that discrete 3+1 skies **are** cap systems, which is
exactly the premise class §B5.3's demotion refutes, one rung down.  The
licensed claim is **capacity**:

> **The admissibility layer does not CAP the shatter ladder at the
> sphere's rung.**  The ladder measures **capacity** at `C(k, ⌊k/2⌋)`
> actors; **selection, if anywhere, lives elsewhere** — and the candidate
> homes are the **measure**, **resource cost**, and **counting
> typicality**; the measure is not the only candidate.

**The meter is a (record, reading) PAIR property.**  The same record reads **0** under SKY-A/C and **1..5** under SKY-B by
depth — profile `2,3,4,5,5,5,4,4,4,3,3,2,2,1,1,1`, gated at G8 — and the
record's meter value is the **SUP over committed readings = 5**.

**No positive 3+1 claim.**  Shattering rules **OUT** the circle; it does
not rule **IN** the sphere.  The positive side — exact rational
cap-realization — is §B7.5's A2 calibration, which is a statement about
the shadow family, nothing stronger.

**No genericity claim.**  One engineered record per rung.  Typicality is
**not even posable** at transport scope (D52, and §B9).

**Residues.**  Minimality at every `m` (6 vs 20; 10 vs 42 — both
architectural, both decidable); the general-`m` claim (visibly patterned,
unrun, unclaimed beyond 5 — `m = 6` would need 20 chains, 57 couriers,
~66 actors); the depth parameter (`d = 5` here while the committed
`SKYB_DEPTH` elsewhere is 2 — a `d = 2` construction or a forced-depth
bound would sharpen the reading-relativity); and the convergence question.

### B8.6 The crystal: tiling capacity `[D60; batch-round reviewed and repaired]`

*Sources: `note-d60-crystal-question-pin.md` (LOG #447, committed before code); `note-d60-crystal-result.md`; `v10/code/d60_crystal_exact.py` (10 PASS / 0 FAIL, exit 0); `reviews/batch-round1-d50-to-d60.md`, D60 — REVISE, 0 BLOCKER / 3 MAJOR / 5 MINOR / 3 NIT.*

**The instrument** is the atlas of §D2 Road 1: **homogeneity** (the
fraction of events carrying a chart of `≥ 2` directions) and the
**chart-size ratio** `ω` along cover pairs.  The prior measurement is
that the engineered shatter records sit at **0.357–0.386** homogeneity
against a genuine-sprinkling band of **0.642–0.800** — *the opposite of
atlases.*  D60 asks whether the grammar can build the other kind.

**The objects, both forced.**

> **CRYSTAL-1D (the brick wall): 65 events over 8 ring actors, 14 rounds
> of alternating re-deliveries; every event offered by the layer's own
> menu, and every specification matched by EXACTLY ONE candidate — the
> record is FORCED.**  **CRYSTAL-2D (the grid): 46 events over 9 actors,
> 12 phases, no refusal.**

The round rebuilt the blueprint independently and reproduced the poset
(1,830 ordered pairs), the heights, the covers and every atlas number.
Honest correction carried: at `K = 3` the grid's phase generator
degenerates — the 12 phases reduce to **4 distinct pair sets** of 3
deliveries — so the grid is a smaller object than "3×3, 46 events"
suggests.

**The atlas verdict `[EXACT]`**, comparators recomputed with the repaired
instrument on eleven genuine sprinkling configurations rather than
re-typed from a rounded printout:

| | homogeneity (`d = 2`) | mean `ω` (`d = 2`) | `\|D\| ≥ 4` | max `\|D\|` |
|---|---|---|---|---|
| **brick, m = 8 (65 events)** | **0.7692** | **0.6510** | **0.0000** | **3** |
| grid 3×3 (46 events) | 0.5000 | 0.3915 | 0.0000 | 3 |
| genuine sprinklings (11 configs) | 0.6417 – 0.8000 | 0.0481 – 0.1329 | 0.425 – 0.650 | 10 – 17 |
| engineered shatter records | 0.357 – 0.386 | 0.467 – 0.473 | 0.000 | 3 |
| generic 2-actor walk | 0.0667 | 1.0000 (2 pairs) | 0.000 | 2 |

Three things follow, and they do not all point the same way.

- **The overlap leg STRENGTHENS**: 0.651 against 0.048–0.133 — a
  corrected comparator improving the result.
- **The homogeneity leg does NOT reach "above"**: against genuine
  `M^{3+1}` the brick's 0.769 sits **inside** the band and below its
  top configuration.  The licensed statement is the one the pin
  pre-registered — *comparable to the sprinkling band*.
- **A third metric, equally natural, is at the floor.**  Chart **width**:
  **no 4-direction chart anywhere in the brick, at any `(M, R)` tried**,
  against the sprinklings' 42–65%.  At `d = 3` the brick does reach
  `|D| ≥ 4` — at **38/65 = 0.5846**, which is **just BELOW** the `d = 3`
  sprinkling width band `[0.6000, 0.7583]`, not inside it.  So the width
  shortfall is a **`d = 2`** statement in order of severity — as is the
  homogeneity ordering (at `d = 3` the brick's 0.7385 sits *below*
  `M^{2+1}`'s 0.7500 and the ordering reverses; the overlap ordering
  holds at both depths).

> **THE LICENSED CLAIM: the grammar admits records that tile at
> sprinkling-grade HOMOGENEITY and above-sprinkling OVERLAP, WITH THIN
> CHARTS.**  A tiling-capacity **mechanism** statement at grammar layer,
> and nothing more.

**`ω` must be read with §D2's containment theorem:** it is a **chart-size
ratio** along covers, not a two-way overlap, and it systematically
favours thin-charted records.

**0.769 is a parameter, not a mechanism.**  Both hard-coded settings are
swept and printed:

```
  ROUNDS at M = 8 :  R=4  0.4400 | R=8  0.6341 | R=14 0.7692 | R=20 0.8315
                     R=30 0.8837 | R=50 0.9282        (|D|>=4 = 0 throughout)
  RING WIDTH at 14:  M=4  0.7879 | M=6  0.7755 | M=8  0.7692 | M=10 0.7531
                     M=12 0.7320 | M=16 0.6822        (|D|>=4 = 0 throughout)
```

and the shortfall is localized:

```
  brick FULL          (65 ev): d=2 homog 0.7692  omega 0.6510
  brick CIRCUIT-ONLY  (56 ev): d=2 homog 0.7857  omega 0.6420
  brick PREFIX-ONLY   ( 9 ev): d=2 homog 0.6667  omega 0.7500
  brick INTERIOR      (51 ev): d=2 homog 0.9020  omega 0.6496   (d=3: 0.9216)
```

> **THE MECHANISM STATEMENT — what the scale doctrine (§D1b) asks this
> unit to certify: the shortfall from 1 is entirely BOUNDARY, so a
> re-delivery circuit's homogeneity tends to 1 as it runs.**  `0.769` is a
> snapshot of `(M = 8, R = 14)`.

The fairness question is settled in the unit's disfavour and it still
clears: the brick's homogeneity is strongly size-dependent while the
sprinklings' is nearly size-independent, so the smaller record is the
handicapped one — and **size-matched at `N = 65` the brick still clears**
`[REFEREE-CARRIED, batch round 1]`.

**Scope, held.**  Grammar layer; transfer to the identified interactive
click law runs through the missing map (§B2.9).  No typicality (there is
no measure at transport scope).  No dimension claim beyond the measured
`|D|` census.  No physical-object claim (§D1b).

**Residues.**  (1) **Size** — both crystals are small, and the grid is
smaller than it looks; a larger grid at `K ≥ 5` would test the 2+1
analogue properly.  (2) **The width ceiling** — `max |D| = 3` at every
`(M, R)` tried at `d = 2`.  **This one is decided by §B8.7 and §B8.9**:
the empirical ceiling is beaten (3 → 4), the delivery ceiling is proved,
and conflict then beats *that* (4 → 9) against a second proved ceiling.  (3) The asymptotic claim rests on a six-point sweep and the
interior control, not on a proof.

### B8.7 The wide crystal, and the branching bound `[D63, LOG #458 → #459; round 1 TERMINAL]`

*Sources: `note-d63-wide-crystal-pin.md` (STRICT, committed before code); `note-d63-wide-crystal-result.md`; `v10/code/d63_wide_crystal_exact.py` (12 PASS / 0 FAIL, exit 0, ~6 min) + `data/d63_wide_crystal_exact.out`; `v10/reviews/d63-round1-hostile-review.md` — REVISE, 0 BLOCKER / 4 MAJOR / 8 MINOR / 4 NIT.*

**The question**, pre-registered with three outcomes: does §B8.6's tiling
mechanism **compose** with §B8.2's width mechanism, and at what
homogeneity cost?  Objects: `WIDE-BRICK(M, R, C)` (D60's brick plus `C`
couriers on ring chords, `C = 0` required to reproduce D60's row exactly)
and `DOUBLE-RING(M, R, cpl)` (two `M`-rings each running the brick
circuit, `cpl` inter-ring deliveries per round).  38 configurations swept.

> **`[EXACT]` F3 FIRED, AT `d = 2`.**  **14 of 38** configurations sit
> INSIDE the recomputed sprinkling homogeneity band **and** carry
> `|D| ≥ 4` charts at `d = 2` — 9 double rings, 5 wide bricks.  D60's
> residue-2 ceiling `max |D| = 3` was a property of the 1+1 brick's cone,
> **not of tiling records as such.**

**The witness, and the substrate §B8.8's cocycle census runs on:**

> **DOUBLE-RING(M = 8, R = 10, cpl = 8): 177 events over 16 actors**, two
> 8-actor rings with all 8 inter-ring deliveries per round.  **FORCED**:
> every event offered by the layer's own menu with **all sixteen actors
> offered at every one of the 177 steps** (widest full menu 528
> candidates), every specification matched by exactly one candidate.  At
> `d = 2`: homogeneity **47/59 ≈ 0.7966**, inside the band
> `[77/120, 4/5] = [0.6417, 0.8000]`; `|D| ≥ 4` at **1/3** of its events
> (the brick's is 0 at every parameter *at `d = 2`*); `max |D| = 4`; mean
> `ω` 0.7299.  At `d = 3`: 0.7740 / 0.6723 — inside **both** `d = 3`
> sprinkling bands.

**THE DEPTH LABEL IS LOAD-BEARING.**  At `d = 3` the F3 *pattern* is met
by **11** configurations, **four with zero coupling — D60's unmodified
brick among them** (0.7385 in band, `|D| ≥ 4` at 0.5846, `max |D|` 4).  So
the composition is **not news at `d = 3`**; what no uncoupled record does
at any parameter is carry `|D| ≥ 4` **at `d = 2`**, and that is this
unit's finding.  Every headline carries the label and the receipt gates
the census at both depths (F3-pattern-at-`d3` zero-coupling = 4, at-`d2`
= 0).

**The frontier, and two shapes in it that are findings in their own
right.**

1. **Coupling is not monotone, and one coupled position is WORSE THAN
   NONE.**  Every family dips at `C = 1` / `cpl = 1` (0.7692 → 0.6022;
   0.6907 → 0.3645) and recovers from 2 upward — but the recovery is
   **family-specific**: double rings peak at *full* coupling, wide bricks
   peak at *partial* coupling and their complete settings are the **worst
   points in their own families** (`(6,10,C=3)` reads 0.5258, below `C=0`
   and below the band floor; `(8,14,C=4)` 0.7062 below `C=3`'s 0.8658).
   The **height-layer census** measures the dip at `(8, 10)`:
   `cpl = 0` runs **27** layers; `cpl = 1` stretches the record to **36**
   ragged layers; `cpl = 8` runs **37** layers with a constant-8 tail.
   **Partial coupling desynchronises the height structure; complete
   inter-ring coupling restores layer regularity.**  Width cannot dip: it
   is 0 on both sides of `cpl = 1`.
2. **Width appears at the COUPLED wires, and the per-wire statement is
   the sharp one.**  At the jump points only a
   *minority* of actors are coupled, and the wide charts sit at exactly
   that minority (12 wide events carried by R0/R1/R4/R5; 8 of 117 by
   A0/A1/B0/B1).  *"Every wire"* is true only at `cpl = M`, which is not
   the jump; and the width column never returns to 0 above the jump.

**Band membership is largely an ENDS property, reported against the
unit's own interest.**  Under D60's interior excision, run on **all 14**
F3 members, **width rises at every one** — so the width is the circuit's,
not the prefix's, and that is the durable half.
But **10 of the 14 interiors leave the homogeneity band through the
TOP** (the winner: 0.8808 against a ceiling of 0.8000; 4 stay in band).
So the licensed reading is *the width mechanism does not destroy the
tiling mechanism*, with **band membership a finite-record statement about
ends.**

> **THE LICENSED CLAIM — a `d = 2` statement.**  Inside the swept
> `(M, R, C, cpl)` family, the tiling mechanism and the width mechanism
> **COMPOSE at `d = 2`**: a coupled delivery circuit can tile at
> sprinkling-band homogeneity while carrying 4-direction charts at a third
> of its events, which no uncoupled record does at `d = 2` at any
> parameter (at `d = 3` the uncoupled brick already meets the pattern).  A
> **mechanism** statement at grammar layer, about the swept family and no
> wider.

**Why the width stops at 4: the branching bound `[THEOREM, verified]`.**

> **Theorem (W4b).**  Let every event of a record carry at most `B`
> registers (`regs_of`).  Then for every event `e` and every `d ≥ 1`, the
> SKY-B chart obeys **`|D_e(d)| ≤ B^d`**.
>
> *Proof.*  Write `R_e(k) = {f : e ≤ f, h[f] = h[e] + k}` for the
> reflexive `k`-layer, so `R_e(0) = {e}` and `R_e(k) = D_e(k)` for
> `k ≥ 1`.  `event_poset` sets
> `pred[j] = ⋃_{r ∈ regs(j)} (pred[last[r]] ∪ {last[r]})`, so the order is
> the transitive closure of `P` (`x P y` iff `x` is the immediately
> preceding event on some register of `y`).  Each `P`-step raises height
> by at least 1, and each `x` has at most `|regs(x)| ≤ B` `P`-successors —
> one per register, the next event on that wire.  Every `f > e` is reached
> by a `P`-path whose first step is some `y` with `e P y`, so for `k ≥ 1`
> `R_e(k) = ⋃_{y : e P y} R_y(k − (h[y] − h[e]))`.  Induct on `k`: at most
> `B` terms, each of size at most `B^{k−1}` since `h[y] − h[e] ≥ 1`. ∎

Zero violations on all 38 records, at `d = 1, 2, 3, 4`, and **saturated by
26 of them**; `B` is **gated, not asserted** (`max |regs_of(e)|` measured
on every event of every record, mint prefixes included).  An independent
re-implementation re-derives the closure of `P` from `event_poset`'s
source, confirms it equals the layer's order on all 38 records, checks
`#P-successors(x) ≤ |regs(x)|` at every event, and reproduces the bound
event by event at `d = 1, 2, 3, 4` with `B = 2` measured throughout.

> **THE MECHANISM STATEMENT THIS UNIT CERTIFIES.**  A delivery carries
> `B = 2` (carriers `{s, r}`), so `max |D| ≤ 4` at `d = 2`: **3 was the
> brick's cone, 4 is the DELIVERY GRAMMAR'S CEILING**, and the
> sprinklings' `max |D|` of **10–17 is UNREACHABLE by any delivery circuit
> whatever.**  Chart width past 4 at `d = 2` therefore **requires
> arbitration** — the layer's only species with more than two registers is
> the **arbitration over a component with `k ≥ 2` distinct proposers**
> (`regs` = proposers ∪ {new version}).  **This is a NECESSITY, not a
> route.**
>
> **And the necessary condition is sharper than "3+ registers".**
> §B8.9's **W4c** proves the minted version register is a **dead wire** —
> it recurs in no later event's `regs_of` — so the operative branching
> factor is the **live** out-degree `Bl`, which for an arbitration is its
> **proposer count** `k`, not `|regs| = k + 1`.  A two-proposer conflict
> ring therefore has `Bl = 2` and is held to `max |D| = 4` exactly like a
> delivery circuit, three registers notwithstanding.  **W4b's "3+
> registers" is necessary but NOT SUFFICIENT; the correct statement is
> "3+ distinct PROPOSERS".**  Both are supplied by §B8.9, which builds
> the records and realizes the corrected ceiling `k²` at
> `k = 3, 4, 5, 6`.

**Instrument hygiene.**  The `C = 0` WIDE-BRICK **is** D60's
`brick(8, 14)` — the function object called in-process, not a re-typing —
reproducing the published row in exact `Fraction`s (10/13, 125/192, 0, 3).
D58's atlas re-run in-process on the same eleven genuine sprinkling
configurations reproduces D60's committed bands `[77/120, 4/5]` and
`[17/40, 13/20]`; **no threshold in this unit is anything but a measured
comparator**.  Tie-freedom is **structural, not discovered** (a delivery
specification is its full tuple, menu events pairwise distinct) — what the
gates measure is that the specified event is *offered* at every step, over
all 38 records (4,604 events), with five records additionally replayed
under full all-actor menus.  Determinism gated under three
`PYTHONHASHSEED`s, byte-identical.  One deviation from the pin's exit
protocol is declared and printed: the receipt also exits 1 if the
comparator reproduction breaks, on the ground that a changed comparator is
anchor breakage in the same sense.

**Scope, held.**  Grammar layer; the swept family and no wider — the
branching bound is the only universal statement here, and it is a theorem
with its hypothesis said aloud.  No measure claim, hence no typicality
(there is none at transport scope, §B9).  No physical-object claim: **a
crystal is a MECHANISM certificate, never an object** (§D1b).  `ω` is a
chart-size ratio along covers (§D2), never a symmetric overlap — and the
wide records' `ω` (0.43–0.75 against the sprinklings' 0.048–0.133) means
*less* here than it did for the brick, since the statistic favours thin
charts and these are the less thin records.

**Residues.**  (1) **The arbitration crystal** — a crystal made of
*conflicts* rather than deliveries; the sharp successor, and the only
route the branching bound leaves to width past 4 at `d = 2`.  **Built,
and it realizes the corrected ceiling at every `k` tried — 9, 16, 25,
36** (§B8.9).  (2) **Both
bands at `d = 2`:** no swept configuration in *this* family is inside the
homogeneity band and the `|D| ≥ 4` band simultaneously at `d = 2` (two
are at `d = 3`); the trend — width rises with rounds, homogeneity rises
faster — suggests it may be unreachable in this family, which would itself
be worth proving.  On the **conflict** substrate the composition is
achieved at `d = 3` by the delivery-free DOUBLE GRIDs — at 0.7833 with
`max |D| = 9`, and on **both** `d = 3` band columns at once with
`max |D| = 16` (§B8.9); at `d = 2` it remains open there too.
(3) The `cpl = 1` dip is measured but the *proof* that layer regularity
controls homogeneity is not written.  (4) **Size** — records run to 217
events against 120-point sprinkling comparators; D60's size residue is
inherited.  (5) **The transitions on this substrate** are measured in
§B8.8: D58's containment theorem says `ω`-overlaps are **nested**, so any
non-identity must live in the *coordinates* rather than in the `ω` pairs
— which is exactly where it is found, and exactly where it is then shown
to be removable.  (6) The `d = 3` story is thinner than the `d = 2`
story: band membership flips at 14 of 38 configurations between depths and
`max |D|` reaches 5 (14 records) and 6 (4 records) at `d = 3` — all within
W4b's bound of 8, and no `d = 3` claim beyond the printed census is made.

> **The two certified mechanisms are now composed, and the next ceiling is
> a theorem.**  §B8.2–§B8.4 buy **width** (rich skies, no tiling); §B8.6
> buys **tiling** (charted everywhere, thin skies); §B8.7 buys **both at
> `d = 2`**.  What stands between the grammar and sprinkling-grade chart
> width is not engineering but the branching bound — and the door it
> leaves open is **conflict**, not transport.  §B8.9 walks through it.

### B8.8 The transition cocycle: non-identity, consistent, and a COBOUNDARY `[D64, LOG #461 → #464 → #466; round 1 TERMINAL]`

*Sources: `note-d64-cocycle-pin.md` (STRICT, frozen and committed before the first receipt existed); `note-d64-cocycle-result.md`; `v10/code/d64_cocycle_exact.py` (15 PASS / 0 FAIL, exit 0, ~61 s) + `data/d64_cocycle_exact.out`; `v10/reviews/d64-round1-hostile-review.md` — REVISE, 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT, with every figure in every table reproduced from the referee's own driver.*

**The question, and why it is posable only now.**  Charts exist (§B8.7);
overlaps are **inclusions as set maps** by D58's containment theorem, so
any transition content must live in the **coordinates**.  The
committed-layer labeling supplies them: a direction's label in chart `e`
is the set of **wire words** — register sequences — realized by `P`-paths
`e → f`, where `P` is `event_poset`'s own generating relation
(`x P y` iff `x` is the immediately preceding event on some register of
`y`).  The instrument is **validated before it is used**: the transitive
closure of `P` **equals** the committed order `poset_of` on all three
grammar substrates, the `P`-path enumeration reaches exactly SKY-B's
`D_e(d)` at every base event, and every overlapping chart pair is
same-height.  *That gate earned its keep — it caught a closure bug (an
accumulation in index order, which is not a topological order on a
sprinkling) before any census was read.*

**The censuses, at `d = 2` on DOUBLE-RING(8, 10, 8)** (177 events, 141
charts with `|D| ≥ 2`, 59 wide, 172 overlapping pairs, 137 of them
wide–wide, 111 triples), at the canonical **ROLE** (port) labeling:

| | pairs | identity | non-identity | cocycle violations |
|---|---|---|---|---|
| **all overlapping pairs** | 172 | **57** | **115** | **0** of 111 triples |
| wide–wide subatlas | 137 | 29 | **108** | 0 |
| BRICK(8,14) control | 58 | 0 | 58 | 0 |
| DR(8,10,0) uncoupled control | 68 | 0 | 68 | 0 |
| `M²⁺¹` sprinkling (`COV`) | 247 | 3 | 244 | 0 |
| `M³⁺¹` sprinkling (`COV`) | 370 | 4 | 366 | 0 |

Across the whole census, 3,582 overlapping pairs and 993 tested triples,
**zero cocycle violations anywhere**.  The 115 are **108** pairs carrying
a length-preserving fibre map plus **7** carrying a *length-changing*
correspondence (from `P`-edges that skip a height: 335 `P`-edges against
328 covers); every group-level statement ranges over the 108.

**The outcome is refused at the RAW labeling, and the receipt says so
before it says anything else.**  On every grammar substrate at both
depths, *every* overlapping pair has base events with **disjoint register
sets**, so raw labels can never agree and RAW's 172/172 non-identity is a
**tautology of the labeling** — PROBE 2 fires and the reading is refused
there.  The mirror probe does not fire: **no labeling on any substrate at
any depth is blind**, so a flat reading would not have been an artifact
either.

> **`[EXACT]` AND THEN THE COMPUTATION THE QUESTION ACTUALLY TURNS ON.**
> Non-identity transitions plus a clean cocycle do **not** distinguish a
> non-trivial bundle from a trivial one.  The decisive test is whether
> the `Z/2`-valued 1-cochain `g` is a **coboundary**: is there
> `ε: charts → Z/2` with `g_ac = ε_a + ε_c`?  **IT IS.**  On the 138
> length-preserving classified overlaps, over 60 charts in 9 components,
> the propagation finds **0 obstructions** with `ε` = **32 charts at 0 /
> 28 at 1**; re-running the whole census with that relabelling turns
> **all 108 non-identity transitions into the identity**, leaving 165 of
> 172 pairs identity and **0 surviving non-identity length-preserving
> transitions**.  The Čech form `g_ik = g_ij + g_jk` agrees: 108 triples,
> 0 violations.  It is not a convention artefact: at the alternative port
> order **REGA**, 0 obstructions as well (`ε` = 40 / 20, 0 survivors).
>
> **THEREFORE `H¹ = 0`.**  The atlas is **globally trivializable** by a
> per-chart choice of which of a delivery's two wires is "port 0"; the
> holonomy of every loop in the nerve is trivial; the transitions are
> **pure gauge**.  **No non-trivial structure group is exhibited on the
> delivery crystal**, and the tensor/curvature programme starts at
> **zero** there.  The computation is gate **C7** — both routes,
> obstruction count and relabelled recount — so the verdict is
> self-verifying on every rerun.

**Four things the census does not establish**, each of them a sentence
that the measured numbers invite and the evidence refuses:

1. **The group is undetermined.**  No *non-identity* transition is a total
   permutation — each is defined on **2 of the 4** fibre points, the only
   total ones being the 29 identities — so naming "the group" requires
   *extending* 2-point partial bijections into `S₄`, and
   the extension is not unique.  Exhaustively: of the 30 subgroups of
   `S₄`, **10** are consistent with every observed map and **two of those
   are minimal by inclusion and incomparable** — `Z/2 = ⟨τ⟩` and a `Z/4`.
   **0 of the 108** transitions is uniquely `τ`, and the `Z/4` reading
   passes the same 108 triples with 0 violations.  The convention-robust
   statement is: **non-identity partial transitions exist and are mutually
   consistent.**
2. **The identity fraction is chart DUPLICATION.**  At `d = 2` on this
   substrate the split is an exact biconditional over all 172 pairs:
   *two charts transition by the identity **iff** they have the identical
   direction set* — `{(same D, identity): 57, (different D,
   non-identity): 115}`.  The controls' "0 identity" is simply their
   having no such pairs.  **Not a theorem:** at `d = 3` it fails in both
   directions.
3. **The substrate/control involution contrast is a REG-convention
   observation.**  At ROLE every control transition is a restriction of
   the all-letter flip `σ` and none of the substrate's is; but this holds
   at REG only (REGA and the register-free `COV` surrogate dissolve it),
   it is **width-confounded** (every non-identity substrate pair is a
   `(4,4)` wide–wide pair and the controls have no wide charts at `d = 2`
   at all), it rests on 41 pairs of 126, and **the controls' overlap
   graphs are perfect matchings** — 38 charts / 19 overlaps / 19
   components and 44 / 22 / 22, every component of size 2 — so there is
   no composition, no triple and no closure content behind "the controls
   close to `⟨σ⟩`".  *(The asymmetry runs against the unit's interest and
   is reported: on the controls `⟨σ⟩` **is** the unique minimal
   consistent subgroup, so the `σ` naming is better founded than the `τ`
   naming was.)*
4. **The pin's lean is half a population fact and half untested.**  All
   115 non-identity pairs sit at **odd** height — but the even layers
   contain almost no transitions *to be* non-identity (all 137 wide–wide
   pairs are odd), so the parity claim is equivalent to a placement fact
   about the blueprint, fixed before any labeling is chosen.  And the
   *coupled-wire* half cannot be evaluated: the 27 pairs both of whose
   base events are inter-ring deliveries are **exactly** the 27 pairs
   carrying no single-valued correspondence at all — the receipt gates
   that the two sets are identical.

> **THE LICENSED CLAIM, no wider than the census.**  On DOUBLE-RING(8, 10,
> 8), at SKY-B depth `d = 2`, at the canonical wire-word labeling: the
> overlapping-chart transitions are **not all identity** (115 of 172);
> they **satisfy the cocycle** on all 111 testable triples; every
> *non-identity* length-preserving transition is a **partial** map on 2 of
> 4 fibre points; and **their class is a COBOUNDARY** — `H¹ = 0` at REG and REGA
> alike.  A **width-≤ 4** statement (W4b caps chart width at `B^d = 4` on
> every delivery substrate), about this substrate at this labeling at this
> depth, **and no wider**.

**Scope and instrument hygiene.**  Grammar layer, five swept substrates.
No measure claim, hence no typicality; no physical-object claim (§D1b);
transfer to the identified law runs through the missing map (§B2.10) and
is not claimed.  Single sources by AST extraction — the substrate is
D63's own function object, not a re-typing, and the referee's independent
re-typing produces the same 177 events; exit-freedom of every extracted
body gated; the anchor reproduces D63's committed row exactly at both
depths.  Determinism gated over three `PYTHONHASHSEED`s on the
substrate's REG cells, byte-identical, with the label naming what it does
*not* cover.  The cocycle has **no content at `d = 3`** (261 of 273 pairs
carry no single-valued correspondence) or on the two grammar controls,
and where it does have content it has exactly one shape: of the 111
tested triples, 108 are `(identity, τ, τ)` and 3 are `(identity,
length-changing, length-changing)`, each testing 2 fibre points — so
*"all triples cocycle-clean"* means `τ ∘ τ = id` was verified 108 times
on 2 points each, and nothing else.

**Residues.**  (1) **The successor question, sharpened:** not *"is `Z/2`
enough"* but **can ANY substrate carry a transition class that is not a
coboundary?**  Everything measured here is compatible with `H¹ = 0` and
was; the test is the **obstruction count**.  The **arbitration crystal**
inherited the question with a *stated structural reason*: what makes `ε`
available is that a delivery's fibre has exactly two ports with no
intrinsic asymmetry, so "which is port 0" is free per chart, and an
arbitration event's conflict structure breaks that symmetry.  **That
attack has run and returned zero** (§B8.9): on wide conflict records the
`Z/2` cochain is identically zero at all five port conventions, and the
two routes with a non-trivial domain (PARITY, FREE) trivialize as well.
The question is now *"can any substrate at all"* with three substrate
families — delivery, conflict, crossed conflict — answering no **on the
chart carrier**, and one candidate answering *maybe* on a different one:
the transport exchange holonomy of §B2.12, which is non-trivial, takes
two values outside `⟨5/4⟩`, and is provably invisible to this
instrument.  (2) **The ambiguous pairs** — 27 of 172 at
`d = 2`, 261 of 273 at `d = 3` — carry a shared direction with two wire
words in *both* charts; whether a finer labeling resolves them is the
single biggest gap between this and a genuine manifold statement.  (3) A
**general** forcedness test applied to the controls: PROBE 2 is
RAW-specific and was never run on them.  (4) **Full overlap ⟹ identity,
here**: the 29 wide–wide overlaps sharing all four directions all carry
the identity, so the sharp open question is whether any substrate's full
overlaps carry a **non-identity total permutation** — that, not
partiality, is what would turn "restriction of a group" into "element of
a group".  (5) The 7 length-changing correspondences, which are the only
transitions surviving the `ε` relabelling and belong to no permutation
group.  (6) Which port convention is canonical: REG, REGA, COV and a
fourth convention the referee built disagree on the split, and **the
triviality of the class is the one outcome that survives all of them**.
(7) Size — 177 events against 120-point sprinklings.

> **What this section delivers is a validated instrument and an honest
> negative.**  The instrument is a transition detector with a triviality
> gate, two artifact probes and a validated reading of the committed
> order.  The negative is that on the delivery crystal there is nothing
> for it to find: the charts glue, they glue consistently, and they glue
> **trivially**.

### B8.9 The arbitration crystal: conflict tiles, the ceiling is `k·b ≤ k²`, and delivery-free DOUBLE GRIDs realize it at `k = 3, 4, 5, 6` `[D66, LOG #469 → #471 → #472; D67, LOG #474 → #475 → #476; both round 1 TERMINAL]`

*Sources: `note-d66-arbitration-crystal-pin.md` and `note-d67-k4-double-grid-pin.md` (both STRICT, frozen and committed before their receipts existed); `note-d66-arbitration-crystal-result.md`, `note-d67-k4-double-grid-result.md`; `v10/code/d66_arbitration_crystal_exact.py` (29 PASS / 0 FAIL, exit 0, 962 s) and `v10/code/d67_k4_double_grid_exact.py` (29 PASS / 0 FAIL, exit 0, 3,291 s) + their `data/*.out`; `v10/reviews/d66-round1-hostile-review.md` — REVISE, 1 BLOCKER / 5 MAJOR / 8 MINOR / 4 NIT — and `v10/reviews/d67-round1-hostile-review.md` — REVISE, 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT.  In **both** rounds every published figure was reproduced from the referee's own driver and the referee then **built records the unit had not**: two that broke D66's mechanism story, three that inverted D67's headline — including the one that turns its flagship negative into this section's strongest positive.*

**The question, and the three units that converge on it.**  §B8.7's
branching bound leaves conflict as the only route to chart width past 4 at
`d = 2`; §B8.8's coboundary makes an arbitration substrate the first place
a non-trivial transition class could live, since what trivializes the
delivery atlas is a two-port symmetry an arbitration lacks; and §B2.10's
descent defect originates exactly at the `2 → 5/2` menu-mass jump, which
is conflict-group visibility.  Width, gluing and measure all name the same
object.  It is built here — twenty-one three-proposer configurations
(**2,325 events**) and eleven four-proposer ones (**1,380 events**), at
grammar layer, together with the chain families that carry the ceiling to
`k = 5` and `k = 6`.

**The design problem the pin named, and the layer's own answer to it.**
Arbitrations **consume** their conflicts, so a conflict crystal must
re-supply a shared base every round; the pre-registered lean was that
*tiling* would be the hard part.  Half of it is free: `View.holdings`
gives the minted version to **every proposer**, not only to the
arbitrator, so a group that arbitrates together needs **no delivery** to
conflict again.  What costs a delivery is **rotation** — partners not
together last round hold mutually superseded versions.

> **`[EXACT]` A-IIIa FIRED: CONFLICT TILES, AT `k = 3` AND AT `k = 4`.**
> Twenty-one three-proposer configurations (2,325 events) and eleven
> four-proposer ones (1,380 events), **zero refusals** — every event
> offered by the committed layer's own menu and specified by its full
> event tuple, max menu hits per specification **1** at every step of
> every record.
>
> **THE TWO FORCEDNESS GRADES ARE SEPARATE, AND THE SECOND IS PRINTED AS
> A NUMBER.**  What the whole sweep carries is the **restricted-menu**
> grade just stated (the specified event is *offered* and unique).  D60's
> **C1 grade** — *all* actors offered at every step — is strictly
> stronger and expensive, and it is reported by count, never by
> implication.  At `k = 3` it completes on `RING(4,6)` 46/46 (widest menu
> 126), `RING(6,6)` 69/69 (301), `GRID(3,4)` 66/66 (530),
> **`DOUBLE-GRID(3,2)` 72/72 (536)** and `RING(6,10)` 117/117 (481), with
> `GRID(3,10)` **BUDGET-CUT at 108/174**.  In the `k = 4` sweep it was
> delivered on **380 steps of the 1,380 swept**, over five records, four
> of them complete — `ARBCHAIN*(0,4)` 22/22 (164), **`ARBCHAIN*(4,4)`
> 66/66 (896), the 16-direction witness**, **`ARBCHAIN**(5)` 157/157
> (2,125), the 25-direction witness**, `DOUBLE-GRID(3,2)` 72/72 (536) —
> while `DOUBLE-GRID(4,2)` is **BUDGET-CUT at 63/120** (986) against a
> printed 150 s.  So: **no *tiling* `k = 4` record is C1-complete**, the
> budget is a receipt-runtime choice rather than a property of the object
> (the 157-event chain replays complete in the same receipt at a larger
> printed budget), and the C1 grade for a ceiling-carrying record rests
> on the two chains and not on the cut record.  *"1,040 events,
> C1-graded" was never true and is not said here.*

> **THE CONFLICT BUDGET BOUND `[THEOREM, verified; saturated by the
> ring]`.**  An
> arbitration's `ckey` is a set of `k` live proposal triples and a
> proposal is resolved by at most one arbitration, so `#proposals ≥ k ·
> #arbs` and the arbitration share of any record of this layer is at most
> **`1/(k + 1)`**, `k` the smallest proposer count in it; deliveries only
> lower it.  *The step that needs the register geometry:* `View.resolved`
> is **view-relative**, so by itself it does not exclude two causally
> *incomparable* arbitrations each seeing the same triple live — the
> register argument closes it (both carry that proposer's register, so
> `event_poset` makes them **comparable**, the later one's component is
> gone from `arb_components_in_view`, and `admissible` returns `False`).
> **THREE READINGS, ALL PRINTED PER RECORD, AND THEY MUST NOT BE
> MERGED.**  `k_min` is the smallest proposer count *anywhere*, so the
> delivery-free ring saturates `1/3` exactly (`k_min = 2`).  A DOUBLE GRID
> mints its base lineages with **single-proposer** bootstrap
> arbitrations, so `k_min = 1` and **its own applicable bound is `1/2`**:
> at `k = 3` its total share is `1/4` and at `k = 4` exactly `1/5`, each
> equal to `1/(k_conflict + 1)` — the bound for a record *all* of whose
> arbitrations carry `k_conflict` proposers, which a bootstrapped grid is
> not.  Its **conflict**-arbitration share is a third number (`2/15` at
> `k = 4`).  So *"the budget bound saturated"* is true of the ring and
> **false of the grids**, whose own bound is `1/2` and is not saturated;
> the exact and `R`-independent equality `total share = 1/(g + 1)` is a
> **coincidence with a printed mechanism** — bootstrap and round each
> contribute `2g(g+1)` events with `2g` arbitrations, for unrelated
> reasons — and levelling breaks it (`1/5 → 6/35`) exactly as it should.
> Gated with the stronger per-arbitration equality `#proposals = Σ k` and
> "no consumed triple occurs twice", and labelled for measuring the
> equality rather than the prose inequality.

**The `k = 3` schedule variants, all reported:**

| variant | in-round deliveries | arb share | `d = 2` homog | `d = 3` homog | `max \|D\|` |
|---|---|---|---|---|---|
| `RING(6,10)` `sticky = 1` (rotate every round) | 27 | 10/39 ≈ 0.2564 | 0.6923 [in band] | 0.8974 [ABOVE] | 4 |
| `RING(6,10)` `sticky = 2` | 12 | 5/17 ≈ 0.2941 | 0.6471 [in band] | 0.5882 [below] | 4 |
| `RING(6,10)` `sticky = 0` (never rotate) | 0 | **1/3 — SATURATED** | 0.6000 [below] | 0.2667 [below] | **2** |
| **`DOUBLE-GRID(3,4)`** (two concurrent conflicts per actor) | **0** | **1/4 = 1/(k+1)** | 0.5167 [below] | **0.7833 [IN BAND]** | **9** |

**And the `k = 4` schedule variants, which decide the design questions the
`k = 3` family could only pose:**

| variant | forces? | in-round deliveries | total arb share | `max \|D\|` d2 / d3 |
|---|---|---|---|---|
| **V1 `DOUBLE-GRID(4, R)`** mints-first, phase-separated | **yes** | **0** (24 in the bootstrap, once) | **1/5** | **16 / 16** |
| V2 `SHARED-BASE(4)`, one *shared* base | **the 19-event stub refuses at event 18** | — | — | — |
| V3 `CONFLICT-GRID(4, R)` rotation, delivery-supplied, one lineage per actor | **yes** | **12 per round after the first, forever** (36 at `R = 4`, 60 at `R = 6`) | 4/29, 2/15 | 8 / 8 |
| V4 `DOUBLE-GRID(4, R, order = 'inter')` interleaved arbitrations | yes | 0 | 1/5 | **7 / 7** |
| **V5 `LEVELLED-DGRID(4, 2)`** | yes | 0 (24 + 20 idle pads, bootstrap) | 6/35 | **16 / 16** |

*(bands: the re-run sprinkling `[77/120, 4/5]` at `d = 2` and `[41/60,
49/60]` at `d = 3`; the second band column, `|D| ≥ 4`, is `[17/40, 13/20]`
and `[3/5, 91/120]`.)*  The winner convention is irrelevant: `win = R` and
`win = ALT` reproduce `win = S` in every column of every census.

Three of those rows carry findings of their own, each stated where it
bites: V2 against V3 here, V4's collapse with the width law below, V5's
levelling with the band verdict.

> **THE BOOTSTRAP IS FORCED BY THE GRAMMAR, AND THE REFUSAL SAYS EXACTLY
> WHAT IT SAYS (V2).**  A `k`-proposer arbitration needs `k` live
> proposals on **one** base, and `prop_options_in_view` skips a base on
> which the actor already holds a live proposal — two bases per actor.
> The step that upgrades that to `2g` **lineages** is that two concurrent
> groups cannot share a base: `admissible` demands
> `triples(view, comp) == ckey` for a *whole* component, `View.components()`
> groups live proposals by base, and on one base the two groups' conflict
> graph is **connected**, so one base admits exactly one arbitration per
> generation.  Hence `g` row bases + `g` column bases.  The V2 stub
> exhibits the block at the layer: mint one version, spread it to all
> sixteen actors, and the record **breaks at its 18th event**, with
> `prop_options_in_view(view, S01)` returning **`[]`** and the whole menu
> offered to that actor reading `['n', 'r']`.  **What V2 does NOT show:**
> that one lineage *per actor* fails — V3 is exactly that design, and it
> forces, tiles and reaches width 8.  The claim is about **one shared
> base**, and the stub is a 19-event demonstration of
> `prop_options_in_view`, never an alternative schedule that was driven.
> **The delivery economics, measured:** concurrency pays `2g(g−1) = 24`
> deliveries **once**; rotation pays `g(g−1) = 12` **every round for
> ever** and buys **less** width (8 against 16), because in it every
> depth-1 successor of an arbitration is a delivery — the `Bl = 2` corner
> again, now at `k = 4`.

**W4c — the mint-register refinement `[THEOREM, PROVED from the committed
layer]`.**

> The version register an arbitration mints is a **birth wire**: it has no
> `P`-successor.  Replacing `|regs(x)|` by the number of registers of `x`
> that **recur** — the live out-degree `b(x)` — in W4b's own proof gives
> `|D_e(d)| ≤ Bl^d` with `Bl = max b(x)`, and for an arbitration
> `b ≤ #proposers = |regs| − 1`.
>
> *Proof, four steps, each quoted against the committed `d42b1` source and
> gated.*  **(1)** A version occupies a register only where it is born:
> `regs_of` returns `{a}` for `p`/`n`, `{sender, receiver}` for `d`,
> `{a, ('mw', a, pk)}` for `m`, and `props ∪ {vname(base, op[3], op[1])}`
> for `r` — so a delivery of version `v` carries `v` in its **payload**
> `op[3]` and does **not** occupy `v`'s register (merge-created `mname`s
> appear in no `regs_of` at all).  **(2)** A version register can
> therefore recur only if two distinct arbitrations **mint the same
> `vname`** — sharing base, winner-key value tuple, author tuple and
> initiator.  **(3)** Two such arbitrations share at least one **proposer
> register** (the winner authors, and the initiator, are proposers of
> both), and in `event_poset` an event touching register `r` becomes
> `last[r]` while every later event touching `r` inherits its whole past —
> so they are **causally comparable**.  **(4)** The later one's `View`
> then has `base ∈ superseded`, `arb_components_in_view` skips the
> component, and `admissible` returns `False`.  **The second arbitration
> is inadmissible. ∎**  *(The same shape as D62's O2 argument, at
> transport scope.)*
>
> **CONSEQUENCE.**  A **two-proposer** conflict record has `Bl = 2`
> exactly like a delivery circuit and **cannot exceed 4 at `d = 2`**
> despite carrying 3-register events.  **W4b's "width past 4 at `d = 2`
> requires a 3+-register event" is true but NOT SUFFICIENT: what is
> required is 3+ distinct PROPOSERS** (§B8.7).
>
> The per-record census is kept beside the proof as **evidence, not
> warrant**, and the distinction is load-bearing: *"`regs_of` places a
> version name in exactly one event's register set"* is at the wrong
> level, since `regs_of` is a function of one *event* while "occurs once"
> is a property of the *record* — which is why the four steps above are the
> warrant and the census is not.  Measured: every version register occurs
> in exactly one event's `regs_of` on every record built here, and both
> bounds hold with zero violations at both depths.  *`b ≤ k` is an
> inequality, not an identity* — the last arbitration of each group at a record's end has
> `b = 0`, and the receipt prints the per-record count of arbitrations
> with `b < k`.  Nothing turns on it (the bound uses the maximum) and the
> gate is labelled for what it measures.

**The width verdict, by proposer count and by live branching:**

| record | `k` | `B` (regs) | W4b `B²` | live `Bl` | W4c `Bl²` | measured `max \|D\|` at `d = 2` |
|---|---|---|---|---|---|---|
| any delivery circuit (§B8.7), **at `d = 2`** | — | 2 | 4 | 2 | 4 | 4 |
| `CONFLICT-RING(M, R)` | 2 | **3** | **9** | **2** | **4** | **4** |
| `CONFLICT-GRID(3, R)` | 3 | 4 | 16 | 3 | 9 | **6** |
| `CONFLICT-GRID(4, 4)` / `(4, 6)` | 4 | 5 | 25 | 4 | 16 | **8** |
| **`DOUBLE-GRID(3, R)`** | **3** | 4 | 16 | **3** | **9** | **9 = k² — REALIZED** |
| `DOUBLE-GRID(4, 1)` | 4 | 5 | 25 | 4 | 16 | 4 (7 at `d = 3`) |
| **`DOUBLE-GRID(4, R ≥ 2)`**, `R = 2, 3, 4` | **4** | 5 | 25 | **4** | **16** | **16 = k² — REALIZED** |
| **`LEVELLED-DGRID(4, 2)`** | **4** | 5 | 25 | **4** | **16** | **16 = k²** |
| `DGRID-INTERLEAVED(3, 2)` / `(4, 2)` | 3 / 4 | 4 / 5 | 16 / 25 | 3 / 4 | 9 / 16 | **5 / 7** (order alone) |
| **`ARBCHAIN**(k)`**, `k = 3, 4, 5, 6` | **k** | `k+1` | — | **k** | **k²** | **9 / 16 / 25 / 36 — REALIZED** |
| genuine sprinklings (11 configurations, `N = 120`) | — | — | — | — | — | **hull [10, 17]** = `M21` `[10, 11]` ∪ `M31` `[14, 17]` |

**The comparator row is depth-labelled.**  *"`max |D| = 4` for any
delivery circuit"* is a **`d = 2`** statement: D63's own committed note
reports `max |D|` reaching 5 at 14 records and 6 at 4 more at `d = 3` —
**18 of its 38 configurations exceed 4 at `d = 3`** — and the receipt
reprints `DR(8,10,8)`'s and the brick's `d = 3` rows beside the claim.

> **WHAT "SPRINKLING-GRADE WIDTH" IS AND IS NOT.**  **(a) The comparison
> range is a hull of two dimensionally distinct clusters.**  The eleven
> genuine configurations are five `M21` (2+1) and six `M31` (3+1)
> sprinklings, all at `N = 120`; their `max |D|` at `d = 2` runs `[10, 11]`
> and `[14, 17]` respectively.  **16 is not inside the 2+1 cluster at
> all** — it sits in the 3+1 one — and every sentence comparing to "the
> sprinkling range" names which sprinklings.  **(b) `max` is the only
> column on which the record touches the population:** at `d = 2` the
> `k = 4` records are below both bands whole and interior, the headline's
> mean chart is 2.09 directions against the sprinklings' 3.26–6.41, and
> three events of 120 carry the 16-wide chart.  The supported claim is
> about **the maximum, at one depth, at one `k`**.  **(c) 16 is a
> parameter picked, not a coincidence discovered** — the same mechanism
> gives 25 and 36, above the whole hull.  So *"the first sprinkling-grade
> width in the campaign"* is **withdrawn as a milestone claim about the
> mechanism**; the surviving sentence is *crossed conflict realizes W4c's
> `k²` at every `k` anyone has built, and the sprinkling maxima happen to
> bracket the `k = 4` value*.  **(d) It is not a size objection:** all
> eleven configurations are at `N = 120` and the headline record is 120
> events, so the comparison **is** size-matched and no extreme-order
> statistic caveat applies.  What needed the label was the dimensional
> population.

> ### **THE WIDTH LAW, and what `2k` is.**
>
> Read off the RING and GRID schedules alone, `max |D| = 2k` looks like a
> law about `k`-proposer crystals with a legible mechanism (*"each
> proposer contributes one direction per wire of its next delivery"*).
> **It is neither.**  `2k` is the value of the bound when every depth-1
> successor of an arbitration is a **two-register event — a delivery** —
> which is what those blueprints impose and **nothing in the grammar
> forces**: an arbitration's proposer register can be consumed by
> **another arbitration**, since an actor may hold two live proposals on
> two distinct unsuperseded bases (`prop_options_in_view` blocks only a
> second live proposal on the *same* base).
>
> **The refinement, from W4c's own proof.**  Every `P`-edge raises the
> height by at least 1, so a depth-2 direction is reached from `e` by a
> `P`-path of length 1 or 2 — an **exact containment**, gated at every
> event of every record with **zero violations**:
>
> `D_e(2) ⊆ succ(e) ∪ ⋃_{y ∈ succ(e)} succ(y)`.
>
> When `e` has a successor at height `h(e) + 1` — no `P`-edge out of `e`
> skips a layer — the first term contributes nothing at depth 2 and the
> bound is the sharp
> `|D_e(2)| ≤ Σ_{y ∈ succ(e)} b(y) ≤ b(e)·Bl ≤ k·Bl ≤ k²`.  **The
> exceptions to the sharp form are counted AND characterised**, not waved
> through: exactly the events *all* of whose `P`-successors sit two or
> more layers above them (a height-skipping edge into a terminal
> arbitration at a record's end), seven in all, and at every one
> `|D_e(2)| ≤ 1`.  The ceiling itself is W4c's `Bl^d`, gated with zero
> violations on every record — and it is **REALIZED at `Bl² = k²` for
> `k = 3, 4, 5` and `6`: 9, 16, 25, 36 directions.**
>
> **`2k` is the `Bl = 2` corner, not the law.  W4c's bound is TIGHT at
> every `k` anyone has built, and the widest chart in the campaign is 36.**
>
> **AND THE CONDITION FOR TIGHTNESS IS DEFINITIONAL, WHICH IS WHY IT IS
> ALWAYS LABELLED SO.**  *"The `k` depth-1 consumers must sit at
> height + 1"* **cannot fail**: `SKY-B(2)` counts events at *exactly*
> height + 2, so a successor at offset 1 contributes its own `b(y)`
> successors while one at offset 2 contributes only **itself** (its
> successors land at offset ≥ 3 and are not counted), and `b(e) ≤ Bl = k`
> caps that route at `k`.  That is the instrument's definition plus one
> inequality.  **What is empirical is two other things:** that the
> *order* of the arbitrations inside a round decides which successors land
> at offset 1 — interleave them, change nothing else, and `16 → 7` at
> `g = 4` and `9 → 5` at `g = 3` — and that a schedule **can** meet the
> condition at every `k` tried.

**The witnesses, exhibited rather than counted** (the pins' demand that a
width claim not be an instrument artefact).  Every one is read from the
**committed `d47a.sky`** directly, every direction verified ordered after
the base in the **committed** `poset_of` and sitting exactly two height
layers above it, with its `P`-path printed:

- `CONFLICT-GRID(4, 4)`, base event 4 — an arbitration by `G00` over
  **four distinct proposers**, 5 registers, height 1, live out-degree 4;
  `|D| = 8` at directions 21, 24, 29, 31, 37, 39, 45, 47, all at height 3,
  role words `(p, 0)` and `(p, 1)` for `p = 0..3`.  This is the `2k` case:
  every successor is a **delivery**, `b(y) = 2`.
- **`DOUBLE-GRID(3, 4)`, nine bases — three per round** — each an
  arbitration over **three distinct proposers** whose three depth-1
  successors are themselves **three-proposer ARBITRATIONS** (out-degrees
  3, 3, 3), giving `|D| = 9 = Σ b(y) = k·Bl = k²`.
- **`DOUBLE-GRID(4, 2)`, three bases — and ONE direction set.**  Events
  73, 74, 75 are `r`-events by `D11`, `D22`, `D33` at height 10, with 5
  registers, **4 distinct proposers** and live out-degree 4, whose four
  depth-1 successors 76–79 are **all four four-proposer ARBITRATIONS**
  with out-degrees `[4,4,4,4]`, so `Σ_y b(y) = 16 = k²`.  The sixteen
  directions are events 80–95, at height exactly 12, `P`-paths printed.
  **The three bases share that one direction set** — all four round-0 row
  arbitrations have the same four column arbitrations as successors — so
  the record contains *one* 16-wide chart seen from three bases; *"three
  charts of width 16"* was literally true and materially misleading, and
  is not said.  `DOUBLE-GRID(4, 4)` carries **11** such bases
  (`g(R−1) − 1`), one direction set per round, repeats named as repeats.
- **The shortfall is characterised, not hidden.**  Of the `R = 2`
  record's 16 conflict arbitrations, **15 realize their whole `Σ_y b(y)`
  budget, 1 falls short, 3 attain the ceiling**; the one that falls short
  is the row-0 arbitration of the *first* round, whose successor height
  offsets read `[2]` rather than `[1]` because the bootstrap depresses it
  one layer.  It costs **one chart in the whole record, not one per
  round** (`g(R−1) − 1` against `g(R−1)`), and one levelling pass removes
  it — see `LEVELLED-DGRID` below.

**The smallest witnesses, and the ceiling ladder.**  `ARBCHAIN*(m, k)` is
one `k`-proposer arbitration whose `k` proposer registers are consumed by
`m` further **`k`-proposer** arbitrations and by `k − m` deliveries,
realizing `k·m + 2(k − m)` exactly:

| `k` | `m = 0` | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 3 | **6 = 2k** (the RING/GRID corner) | 7 | 8 | **9 = k²** | — | — |
| 4 | **8** | 10 | 12 | 14 | **16 = k²** | — |
| 5, *unlevelled* | 10 | 9 | 12 | 15 | 18 | **17, short of 25** |

So `2k` is not a law, not a ceiling and not even a typical value: it is
the `m = 0` corner of a one-parameter family whose other corner is `k²`.
*(A correction to a committed parent, said plainly: D66's own
`arbchain(m, k)` hardcodes **three**-proposer secondaries whatever `k`
is, so its docstring's claim to sweep `[2k, k²]` at general `k` is false —
at `k = 4` it returns `3m + 2(k − m)`.  **Nothing gated in D66 is
wrong**: its receipt only ever ran `k = 3`, where the two formulas
coincide.  `ARBCHAIN*` is the corrected object and reproduces D66's
6, 7, 8, 9 exactly at `k = 3`.)*

**The `k = 5` shortfall in that table is a bootstrap ordering, and the
grammar's own idle event removes it.**  In `ARBCHAIN*`, register `S_i`
supplies `A_i` **and** all `k − 2` helpers `T_ij` by a serial delivery
chain, so `p(S_i, Y_i, 0)` sits `k − 1` layers above its mint and at
`k = 5` two of the five secondary arbitrations land at height offset 2 —
where, by the definitional condition above, they contribute themselves
and nothing else.

> **`[EXACT]` THE CEILING LADDER — `ARBCHAIN**(k)`, and `k²` REALIZED AT
> `k = 3, 4, 5, 6`.**  `ARBCHAIN**(k)` is `ARBCHAIN*(k, k)` with every
> auxiliary register **height-levelled by the grammar's own `('n', a)`
> idle** — the same event kind the committed blueprints already use for
> their tails — inserted between the bootstrap and the proposals, so that
> all `k` depth-1 consumers sit at exactly height + 1.  Nothing else
> changes: no new lineage, no delivery, no arbitration.
>
> | `k` | events | actors | levelling idles | `h(e)` | `D(1)` | out-degrees | `\|D_e(2)\|` | `k²` |
> |---|---|---|---|---|---|---|---|---|
> | 3 | 47 | 9 | 6 | 8 | 3 × `r` at offset 1 | `[3,3,3]` | **9** | 9 |
> | 4 | 90 | 16 | 24 | 10 | 4 × `r` at offset 1 | `[4,4,4,4]` | **16** | 16 |
> | **5** | **157** | **25** | 60 | 12 | 5 × `r` at offset 1 | `[5]×5` | **25** | 25 |
> | **6** | **254** | **36** | 120 | 14 | 6 × `r` at offset 1 | `[6]×6` | **36** | 36 |
>
> Forced at every `k`: menu hits `min = max = 1`, no refusal.  **The
> `k = 5` member is verified to the full witness standard** — the closure
> of `P` **equals the committed `event_poset`** on all 157 events, the
> committed heights equal ours, `|D_e(2)| = 25` is read from the
> **committed `d47a.sky`**, the 25 directions are pairwise distinct, all
> ordered after the base in the committed order, all at height exactly
> `12 + 2`, `P`-paths printed, `Bl = 5`, W4c violations at `d = 1, 2, 3`
> **zero**, every version register in exactly one `regs_of` — and it
> carries a **complete C1 grade**, full-menu replay **157/157** at widest
> full menu **2,125 candidates**, a *higher* forcedness grade than any
> DOUBLE-GRID record in the corpus.
>
> **WHAT THIS SETTLES.**  `k²` is **realized at every `k` anyone has
> built**.  Height alignment is a **design requirement the grammar's own
> idles satisfy**, not an obstruction — so *"the ceiling is not reached at
> `k = 5`"* was a property of one unlevelled bootstrap, and D66's residue
> 6 stays **CLOSED**.  **And the attribution to phase separation is
> weakened accordingly:** `ARBCHAIN**` has no phase separation of any kind
> and reaches the ceiling at every `k`.  Phase separation is how a
> *tiling* schedule meets the height condition; levelling is another way;
> **the condition is what is load-bearing.**  What remains is the
> *general-`k`* proof — four data points are not a theorem — and the
> *tiling* question (residue 1).

> **THE `k = 3` FLAGSHIP — `DOUBLE-GRID(3, R)`.**  Rows and columns
> conflicting **concurrently**, so every actor stands in two independent
> conflict lineages at once.  **Zero in-round deliveries** (12 in the
> bootstrap only); total arbitration share **1/4 = `1/(k_conflict + 1)`**;
> C1-complete full-menu replay **72/72** at widest menu 536; **nine
> `|D| = 9` charts**, three per round, each verified against the committed
> `sky()` and `poset`, out-degrees `[3,3,3]` — **`k² = 9`, W4c's ceiling,
> REALIZED**; width histogram `{0:10, 1:48, 2:5, 3:46, 4:2,
> 9:9}`; `d = 2` homogeneity 31/60 with `|D| ≥ 4` at 11/120; **`d = 3`
> homogeneity 47/60 = 0.7833, INSIDE the band on the homogeneity column,
> with `max |D| = 9`** — though on the second `d = 3` column its
> `|D| ≥ 4` is 13/40 = 0.325, far **below** `[3/5, 91/120]`.  **The first
> record in the campaign that is both crystal-uniform and wide, in band on
> one column of the two.**

> **THE `k = 4` FLAGSHIP — `DOUBLE-GRID(4, 4)`, WIDE AND IN BAND AS A
> WHOLE RECORD, ON BOTH COLUMNS.**  200 events, 16 actors, **forced**
> (menu hits `[1, 1]`, zero refusals), **zero in-round deliveries** (24 in
> the bootstrap, once), total arbitration share `1/5`, **`max |D| = 16 =
> k²` at both depths**, 11 bases carrying it.
>
> | | `d = 2` homogeneity | `d = 2` `\|D\| ≥ 4` | `d = 3` homogeneity | `d = 3` `\|D\| ≥ 4` |
> |---|---|---|---|---|
> | `DOUBLE-GRID(4, 4)` | `97/200 = 0.4850` below | `0.4000` below | **`29/40 = 0.7250` IN** | **`0.6350` IN** |
> | re-run sprinkling band | `[0.6417, 0.8000]` | `[0.4250, 0.6500]` | `[0.6833, 0.8167]` | `[0.6000, 0.7583]` |
>
> Width histograms: `d = 2` `{0:28, 1:75, 2:7, 3:10, 4:69, 16:11}`,
> `d = 3` `{0:34, 1:21, 2:12, 3:6, 4:73, 5:1, 6:3, 7:2, 16:48}`.
> **This is more than the `k = 3` flagship achieves**, which holds one
> `d = 3` column of two.  **THE WIDTH-UNIFORMITY FRONTIER AT `k = 4` DOES
> NOT EXIST.**

**The band verdict, on both columns and as a crossing.**  Three
qualifications travel with that box, permanently.

- **(i) BOTH COLUMNS, EVERYWHERE.**  The receipt computes **two**
  sprinkling bands at each depth — homogeneity and the `|D| ≥ 4` share —
  and a verdict read on the first alone is not a verdict.  On the second
  column the `k = 3` flagship is **below** at `d = 3`, and so is the
  *interior* cell of `DOUBLE-GRID(4, 2)` (`d = 3` homogeneity `3/4` IN,
  `d = 3` `|D| ≥ 4` `47/80 = 0.5875` **below**).  `DOUBLE-GRID(4, 4)` is
  the record that is inside both.  This was a **corpus-level habit**, not
  one unit's slip, and it is corrected wherever "in band" appears.
- **(ii) IT IS A CROSSING, NOT A MATCH.**  Both `d = 3` homogeneity
  sequences are **monotone in `R`**, and the band is an interval each
  crosses at a different `R`:

  | `R` = | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | **WHOLE record**, `d = 3` | 0.4625 | 0.5417 | 0.6562 | **0.7250 IN** |
  | **INTERIOR population**, `d = 3` | 0.6154 | **0.7500 IN** | 0.8333 ABOVE | 0.8750 ABOVE |

  A one-parameter family monotone in a statistic crosses any interval
  somewhere, so **"in band" names a round number**; what is durable is
  that at the crossing the record still carries `k²`.  *(The mechanism is
  measured rather than guessed: a wider record at **fixed** round count is
  a more heterogeneous record — the `k = 4` histograms carry a large
  population of width-0 and width-1 charts against a handful of very wide
  ones — and the remedy is more rounds, which is what the `R = 4` row
  is.)*
- **(iii) THE INTERIOR IS A POPULATION, NOT AN OBJECT.**  `interior_of`
  returns the full closure and a **subset of events**; `profile` then
  averages over that subset while every chart is still computed on the
  whole record, so a base at height `hi − 3` still reads directions inside
  the excised layers.  An interior figure is a **conditional average over
  80 of 120 events** — not a record, not a sub-poset, not an object.  For
  the same reason "no wide chart is a boundary artefact" tests that the
  **base** is off the boundary (all wide bases sit at heights 9–10 inside
  `[2, 12]`), never that the chart's contents are.

**What the door does and does not buy, with depth labels.**

- **At `d = 2`**, in this family, width and tiling homogeneity do
  anti-correlate: the in-band-and-wide set has ten members, **every one of
  them `k = 2`** (they are not all *rings* — `GRID(g=2, R=10)` is one, and
  by the receipt's own gate it is the `M = 4` ring under another name),
  while every `k ≥ 3` record sits below the band, whole and interior, at
  `k = 3` and `k = 4` alike.  **The `d = 2` band is untouched by
  everything here.**
- **At `d = 3` the anti-correlation fails outright.**  D60's interior
  excision, run on **every** swept record at **both** depths, carries
  `GRID(3,6)` and `GRID(3,10)` **into** the `d = 3` band while they still
  carry `max |D| = 6` — D63's ends effect exactly; `DOUBLE-GRID(3,4)` is
  in the `d = 3` homogeneity band **outright** at `max |D| = 9`; and
  `DOUBLE-GRID(4,4)` is in **both** `d = 3` bands outright at
  `max |D| = 16`.  **In band and at the ceiling, at once, at two
  different `k`.**
- Symmetrically, the rings' in-band property is a **`d = 2`** property:
  their `d = 3` homogeneity is 0.83–0.93, **above** the band, interiors at
  1.0000.

**The levelling lever, and what it costs.**  `LEVELLED-DGRID(4, 2)` is the
DOUBLE-GRID bootstrap with the same idle pad `ARBCHAIN**` uses: 140 events
(20 pads), and the depressed row-0 arbitration now realizes its whole
budget — **four width-16 charts per round instead of three**, `d = 2`
homogeneity `61/140 = 0.4357` (from `0.4083`), `d = 3` `17/28 = 0.6071`
(from `0.5417`), interior `d = 3` `4/5 = 0.8000` IN.  **The trade is
recorded:** the pad dilutes the `1/(g+1)` share coincidence from `1/5` to
`6/35`, and levelling alone does **not** put the whole record in band —
that is the `R = 4` row.

`ω` is reported per D58's reading (a chart-size ratio along covers, never
a symmetric overlap): 0.75 for every rotating ring, 1.0000 for the
delivery-free ring (thin charts, as the statistic's bias predicts),
0.44–0.51 for the grids, 0.5566 for the DOUBLE GRID.

> ### **THE DESIGN FINDING — what actually makes a second direction.**
>
> The `sticky = 0` ring is delivery-free *and* collapses to `max |D| = 2`.
> That collapse is a property of **one live conflict lineage per actor**,
> not of delivery-freedom: with one lineage the propose/propose/arbitrate
> cycle is a **diamond** — two proposals fan out of an arbitration and fan
> straight back into the next one — so the depth-2 layer is a single
> event.  Give each actor **two standing conflicts** and the deliveries
> vanish, the arbitration share holds at `1/(g + 1)`, and the width
> returns nine times over — sixteen at `k = 4`.
>
> **What a crystal needs for a second direction is a second concurrent
> consumer of the proposer's register.**  Rotation buys that consumer with
> a **delivery**; concurrency buys it for **free**; and a concurrent
> **arbitration** is a *better* consumer than a delivery — `b = k` instead
> of `b = 2`.  **The second direction is a second CONCURRENT CONFLICT
> AXIS.  Crossed conflict alone generates both the uniformity and the
> width; transport is needed only to SEED and to ROTATE, never to make
> space.**  The maximum-conflict schedule is not the one that cannot tile
> widely: every ceiling-carrying record here has **zero in-round
> deliveries**.
>
> **AND CONCURRENCY IS THE TILING ROUTE TO THE CONDITION, NOT THE
> CONDITION.**  What the width actually requires is that the `k` depth-1
> consumers sit at height + 1 (definitional, above); crossing two conflict
> axes is how a *tiling* schedule meets it, and **height-levelling by the
> grammar's own idle is a second way**, with no crossing and no phase
> separation at all — which is why the ceiling is reached at `k = 5` and
> `k = 6` by chains and at `k = 3` and `k = 4` by grids.  The order in
> which a round's arbitrations are taken is load-bearing on exactly this
> point: `16 → 7` by re-ordering alone.

**The coboundary gate, and the answer to §B8.8's successor question.**
The instrument is D64's, **unmodified and anchored**: this receipt re-runs
D64's own `reg_tuple` / `out_reg` / `words_from` / `fibermap` / `classify`
/ `measure` / `cochain` / `extension_census` by AST extraction and gates
that on `DOUBLE-RING(8,10,8)` at REG and `d = 2` it reproduces **every**
committed figure (60 charts, 138 labelled overlaps, 9 components, 0
obstructions, `ε` 32/28, 0 survivors, 108 Čech triples / 0 violations,
split 57/115, REGA `ε` 40/20).  **So the same instrument produces every
number below.**  Five port conventions for 3+-register events are defined
and printed — **REG** (D64's canonical tuple order), **REGA** (all
registers name-sorted), **ARBLOSE** (losers, winners, version),
**ARBVFIRST** (version first), **COV** (register-free surrogate, the only
one also defined on sprinklings) — with initiator-first and winner-first
coinciding with REG on this family as a printed fact about the blueprint.
Two further routes are **validated before use** (a constructed true
positive *and* true negative): a **PARITY** route (`g = 1` on any
non-identity length-preserving transition, including the ones D64's
`cochain` drops as `other`) and a **FREE-RELABELLING** route (arbitrary
per-chart bijections — the largest possible gauge group).

> **`[EXACT]` THE CLASS IS TRIVIAL AGAIN, AND AGAIN ON THE WIDEST
> SUBSTRATE BUILT.**  `CONFLICT-GRID(3, 10)` at `d = 2`: 92 charts, 27
> wide, 90 overlapping pairs, 61 triples.  **All three routes return ZERO
> obstructions at all five conventions and both depths**, and PROBE 1 does
> not fire at any wide-record cell.  The `k = 4` census repeats it on
> **both** 16-wide records — `DOUBLE-GRID(4, 2)` *and* `DOUBLE-GRID(4, 3)`,
> the second added when a claim said "every `k = 4` wide record" and the
> census contained one of them: **D64's own C7 and the FREE-RELABELLING
> route return zero at every one of the 74 census cells.**
> **D64's successor question is answered NEGATIVELY on the first substrate
> that could have answered it positively, and then again on the widest one
> that exists: conflict bought WIDTH and bought no gauge.**

**Where the non-vacuity lives — the credit, said correctly.**  C7's `Z/2`
cochain is the **zero cochain at all five conventions**, but for two
different reasons.  At **REG, REGA, ARBVFIRST and COV** it is zero on the
full length-preserving domain because every such transition is outright
the identity: there is nothing to trivialize, and the 52 testable Čech
triples test `0 = 0 + 0`.  Citing that triple count as evidence of
non-vacuity is exactly the move §B8.8's census forbids; what **is**
non-vacuous there is **PROBE 1's failure to fire** — the labeling could
have shown a transition and did not.  At **ARBLOSE** the cochain is zero
only because D64's `cochain` **drops the `other` class by construction**,
its domain shrinking from 63 edges to 22 and discarding **exactly the 41
non-identity maps** a strong sentence would want to invoke; the routes
that genuinely trivialize a not-identically-zero cochain there are
**PARITY** (63 edges, 41 at `g = 1`, obstruction 0) and, independently,
**FREE**.  The five conventions are genuinely distinct labelings — the
receipt counts the `(chart, direction)` cells at which each disagrees with
REG on the ROLE label — but on the wide record REG, REGA, ARBVFIRST and
COV return the same number in every column, so the robustness sentence is
that the wide record admits **two** distinct readings, not five.

**The odd-ring residue, DECIDED as parity.**  The *narrow* two-proposer
rings do what nothing else in the campaign does — carry a **non-zero** C7
obstruction count.  Run at five ring sizes (REG, `d = 2`):

| ring | pairs/round | `M/2` | parity edges | non-identity | C7 obs | PARITY obs | `R − 1` |
|---|---|---|---|---|---|---|---|
| `RING(4, 6)` | 2 | EVEN | 35 | 15 | **0** | **0** | 5 |
| `RING(6, 6)` | 3 | ODD | 30 | 11 | **5** | **5** | 5 |
| `RING(8, 6)` | 4 | EVEN | 40 | 16 | **0** | **0** | 5 |
| `RING(10, 6)` | 5 | ODD | 50 | 21 | **5** | **5** | 5 |
| `RING(12, 6)` | 6 | EVEN | 60 | 26 | **0** | **0** | 5 |
| `RING(6, 10)` | 3 | ODD | 54 | 19 | **9** | **9** | 9 |
| `RING(10, 10)` | 5 | ODD | 90 | 37 | **9** | **9** | 9 |

The obstruction tracks the **parity of `M/2`** at five ring sizes, `M =
12` being the clean row that could have killed the reading.  **And the
magnitude is not a ring quantity**: the count is 5 at `R = 6` and 9 at
`R = 10` for **both** `M = 6` and `M = 10` — it is `R − 1`, a count of
**rounds**.  Reporting "5 and 9" as *the ring's* obstruction invites
reading a magnitude that is neither a ring quantity nor a cohomological
one; **the only invariant statement available is `≠ 0`.**  *(One row is
disclosed rather than smoothed: an independent re-measurement of
`RING(4,6)` reports its two auxiliary columns as "edges 23, non-id 3"
where this instrument measures 35 and 15.  The **obstruction count agrees
at 0 both ways**, the committed `RING(4,10)` row scales to this
instrument's numbers, and the parity reading is untouched.)*

**And it is still NOT `H¹ ≠ 0`.**  Four measured facts cut against it and
the pin requires survival of all four.  **(1)** The free-relabelling route
trivializes **every** such cell (0 obstructions, 0 survivors, everywhere
in the census) — what is obstructed is the *port* gauge group, not the
existence of a global labelling, and the two facts are consistent for a
legible reason: the fibre maps are **partial**, so with no 2-skeleton the
odd cycle's composite has empty domain.  **(2)** There is
**no Čech 2-skeleton to carry a class** — on the rings at `d = 2` every
chart triple with pairwise overlaps has an **empty** triple intersection,
zero testable triples, where the delivery crystal had 108 and was *still*
a coboundary.  **(3)** The group name is a convention exactly as in D64:
the extension census on the ring finds 10 subgroups of `S₄` consistent
with every observed map, **two incomparable minimal ones**, and **0 of
19** τ-classified pairs uniquely τ.  **(4)** The controls put the ring on
the wrong side of the interesting line — genuine sprinklings carry
non-zero PARITY obstructions too while the delivery crystal carries zero
everywhere, *and that comparison is **COV-only***, a sprinkling having no
`H` and hence no counterpart to the ring's other four conventions.  So it
is **not** the campaign's first non-zero obstruction in any absolute
sense — the sprinklings in the same run carry them too.  What is first
about it is being the first non-zero obstruction **on a grammar record**,
and that is the only priority claim available.  **PROBE 1 fires and is acted on:** the blind ROLE cells — all
five instruments on the delivery-free ring at `d = 2`, and COV on
`RING(4,10)` — are **excluded by name** from every convention-robustness
sentence, and no outcome anywhere is read at RAW.

**And the one convention that behaves differently has now been swept —
the answer is that it is the convention, not the conflict.**  `ARBLOSE`,
which reads a settlement's port order off the winner/loser asymmetry, is
the only cell of the `k = 4` census that is non-zero, and the sweep that
was asked for runs it at both proposer counts: **it obstructs on the
DOUBLE-GRID schedule at `k = 3` as well** — on `DOUBLE-GRID(3, 4)`, a
record never put through D66's own census — and on the sprinkling cells at
COV.  So it is **a property of the schedule and of that port convention,
not of the proposer count**, which closes the last "maybe conflict is
different" reading of it.  C7 does not see it because it drops the `other`
class by construction (its ARBLOSE domain shrinks from 133 edges to 29 on
the `R = 2` record).  The reporting rule is unchanged and now covers three
substrates: **`≠ 0` is the only statement**, the free-relabelling route
trivializes every one of those cells, and the genuine sprinklings carry
non-zero parity obstructions too — so on this statistic the DOUBLE GRID
sits with the sprinklings and against the delivery crystal, which is zero
everywhere.

**The mass census, labelled.**  d42b1 prices each actor's menu at
`1 + (m − 1)/4`.  Along the replayed prefixes the total menu mass sits at
`M` (the actor count) at most prefixes and rises where an unarbitrated
conflict group is visible — `RING(6, 10)`: total mass `{6: 87 prefixes,
19/3: 3, 13/2: 27}`, a **ladder excess** (mass − `M`, in quarters) of
`{0: 87, 4/3: 3, 2: 27}`.  Two things are said rather than elided.
**The scope difference from §B2.10 is not bridged:** D65's `2 → 5/2` jump
is a two-actor, delivery-free d42a statement about a 36-state exhaustive
family, while this is transport scope, `M` actors, delivery sector open,
measured per prefix along one record; D65's two values are **not**
reproduced here and are not claimed to be.  The commensurable quantity is
the excess above `M` in quarters, counting extra visible conflict groups,
and it is non-zero exactly where conflicts are open.  **And the ladder
does not hold** — per-actor sums of `13/12` and `19/16` occur, off the
`1 + k/4` ladder — which is exactly the committed exhibit behind *"the
general-depth ladder is FALSE under current pricing"* (§B2.7, §B2.8: a
dead component still inflates a live singleton's view-relative arbitration
denominator), reproduced here at a different scope by an independent
route; nothing about the ladder is claimed.

> **THE LICENSED CLAIM.**  Inside the swept family, at grammar layer:
> **(i)** conflict **tiles at `k = 3` and at `k = 4`** — forced
> propose/arbitrate records run to crystal length with zero refusals at
> the restricted-menu grade (2,325 + 1,380 events), of which **380 steps
> across 5 records** carry D60's C1 grade with **4 of those records
> C1-complete**, and the arbitration share is bounded by `1/(k+1)`,
> saturated at `1/3` by the delivery-free ring, while a bootstrapped
> DOUBLE GRID sits at `1/(g+1)` — `1/4` at `k = 3`, `1/5` at `k = 4` —
> without saturating its own bound of `1/2`; **(ii)** a two-proposer
> conflict ring meets D63's F3 pattern **at
> `d = 2`** with **conflict, not delivery, as its tiling engine** — while
> its *width* half is carried by its delivery wires, so a purely
> conflict-driven F3 pattern is exhibited **nowhere at `d = 2`**;
> **(iii)** chart width past the delivery ceiling of 4 at `d = 2` is
> **realized**, the law is W4c's `|D_e(d)| ≤ Bl^d` with its depth-2
> refinement `|D_e(2)| ≤ Σ_{y ∈ succ(e)} b(y) ≤ k·Bl ≤ k²`
> (exact-containment form and characterised exceptions above), **realized
> at 6, 7, 8 and at `k² = 9, 16, 25, 36` for `k = 3, 4, 5, 6`**, with
> `2k` exposed as the `Bl = 2`
> corner the RING/GRID schedules happen to impose, and W4b's "3+
> registers" corrected to "3+ **PROPOSERS**" by W4c, **proved** from the
> committed layer — the `k = 4` value sitting inside the **hull**
> `[10, 17]` of the sprinkling maxima, which is the hull of an `M21`
> cluster `[10, 11]` and an `M31` cluster `[14, 17]`, so 16 is in the 3+1
> cluster and outside the 2+1 one; **(iv)** the width is a property of
> **the arbitration order meeting a definitional height condition**,
> not of concurrency alone — interleaving row and column arbitrations,
> changing nothing else, collapses 16 to 7 and 9 to 5 — and **phase
> separation is not the general lever**, since `ARBCHAIN**` has none and
> reaches `k²` at every `k` by height-levelling with the grammar's own
> idle; **(v) UNIFORMITY SURVIVES THE WIDTH ON A WHOLE RECORD**:
> `DOUBLE-GRID(4, 4)` is inside **both** `d = 3` sprinkling band columns
> (homogeneity `0.7250`, `|D| ≥ 4` `0.6350`) while carrying
> `max |D| = 16` — more than the `k = 3` flagship, which holds one column
> of two — reported as a **crossing** of a monotone one-parameter family
> rather than as a property of an object, with nothing here in band at
> `d = 2` at either `k`; **(vi)** the wide records' transition class is
> **trivial** at every port convention and by every route, on **both**
> 16-wide substrates as on the `k = 3` ones — the
> non-vacuity carried by PROBE 1's silence at the four zero-cochain
> conventions and by PARITY/FREE at ARBLOSE — so **no non-trivial
> structure group is exhibited by conflict either**; and **(vii)** the
> non-zero port-flip counts — the pair-conflict rings with an **odd**
> number of pairs per round, at five measured ring sizes with magnitude
> `R − 1` and therefore **not a ring quantity**, and the ARBLOSE cells of
> the DOUBLE GRID, which fire at `k = 3` and `k = 4` alike and are
> therefore a property of the schedule and the convention — do **not**
> survive free relabelling, have **no** testable Čech triple behind them,
> and are **reported and not claimed** as `H¹ ≠ 0`.

**Instrument hygiene and scope.**  Grammar layer; the swept
`(M, R, sticky, win, g)` family, the `(g, R, order, boot, level)`
DOUBLE-GRID family and the ARBCHAIN\* / ARBCHAIN\*\* families, and no
wider.  A crystal certifies MECHANISMS, never objects (§D1b).  No measure
claim at transport scope, hence no typicality.  Every width claim carries
the record's own `B`, its live `Bl` and both bounds; every gauge sentence
carries the convention table; transfer to the identified law runs through
the missing map (§B2.9) and is not claimed.  Single sources: the transport
grammar by text-slice from committed `d42b1`; `d47a`, `d55c`, `d58`, D60's
blueprint machinery, D63's `double_ring`/`wide_brick` and **D64's entire
cocycle instrument** by AST extraction, with exit-freedom of the slice and
of every extracted body gated — *the scan is a syntactic check for
`exit`/`quit`/`_exit` in call or bare name form, it decides no
reachability, and it cannot see an exit reached through `getattr` on a
computed string.*  Anchors (exit 1 reserved for them): D63's `DR(8,10,8)`
row exact at both depths; D60's brick event-for-event; eleven genuine
sprinkling configurations reproducing `[77/120, 4/5]` and `[17/40,
13/20]`; D64's C0b instrument validation re-run on every conflict record
(closure of `P` **equals** the committed order everywhere); D64's
committed C7 row; and, for the `k = 4` sweep, the committed `k = 3`
DOUBLE-GRID rows event for event, the sprinklings' **two dimensional
clusters** `M21 [10, 11]` / `M31 [14, 17]`, and the **R-prefix lemma** —
`dgrid` appends rounds, so the `R`-round record is a prefix of the
`R'`-round one, checked event for event at `g = 3` between two separate
builds, which is what lets the 200-event flagship be built once and its
three shorter rows read off its own prefixes.  A hoisted SKY-B
optimisation is gated against the
committed `d47a.sky` **event for event on two whole records at both
depths**, and every chart the unit *exhibits* is read from the committed
`sky` directly.  Determinism gated on a ring, a grid, the `g = 3` DOUBLE
GRID, `ARBCHAIN*(m, 4)` and `ARBCHAIN**(3)/(4)` under `PYTHONHASHSEED`
0/7/999, byte-identical, with the scope of that
gate said aloud: **it does not cover** the `g = 4` DOUBLE-GRID builds
including the flagship, `LEVELLED-DGRID`, `ARBCHAIN**(5)/(6)`, or either
coboundary census.  The exit scan is widened at `k = 4` to report every
top-level body containing a **reflective construct** (`getattr` /
`setattr` / `eval` / `exec` / `__import__` / `compile` / `vars` /
`globals` / `locals`) by name, and to gate that **none of them is a body
this line binds** — every hit lives in committed extraction helpers that
are never called, so the declared hole is not merely disclosed but empty
on the bodies actually run.  One duplicate object is named out loud:
`g = 2` does
**not** reproduce `CONFLICT-RING(4, R)` "exactly" — the event lists differ
by actor naming — and what is gated is the true statement, that the
event-**kind** sequences coincide and every profile column coincides at
both depths.

**Residues.**  (1) **The ceiling is closed at every `k` built; two things
are not.**  A **general-`k` proof** that levelling always meets the height
condition — four data points are not a theorem — and whether a *tiling*
`k ≥ 5` schedule (a `DOUBLE-GRID(5, R)`) exists, forces and reaches 25,
which is out of the receipt's computational reach and untested by the
round as well.  Nothing is known about **whole-record band membership at
`k ≥ 5`** either: the `k = 5` and `k = 6` witnesses are smallest-witness
chains, not tilings, and no band statistic is defined on them.  (2) **The
`d = 2` band is untouched by everything here** — nothing at `k = 3` or
`k = 4`, whole or interior, is inside the `d = 2` homogeneity band while
wide.  (3) **The odd-ring holonomy is a proof problem, not a
sampling problem:** parity confirmed at five ring sizes with the count at
`R − 1` everywhere; what is open is the **proof** that the obstruction is
exactly the parity of `M/2`, and the reading of what it obstructs given a
clean free-relabelling route and no 2-skeleton.  The ARBLOSE parity
obstruction now has a **third** substrate and still no proof of what it
obstructs.  (4) **The free-relabelling
route never fires on real data**: validated to have a true positive on a
constructed inconsistency, it returns 0 at every census cell including the
sprinklings, so its null is weak evidence until something obstructs it.
(5) **No *tiling* record is C1-complete at either `k`** —
`GRID(3,10)` cuts at 108 of 174 steps and `DOUBLE-GRID(4,2)` at 63 of 120;
the C1 grade for a ceiling-carrying record rests on `ARBCHAIN*(4,4)` and
`ARBCHAIN**(5)`, and the restricted-menu drive already establishes
admissibility of every event against the whole prefix.  A C1-complete
`DOUBLE-GRID(4, R)` needs a bigger budget or a cheaper menu enumeration.
(6) **Size, inherited and now dominant** — ~1,164 s for a 200-event record
at 16 actors, on a cost curve of `15.1 → 107.9 → 399.9 → ~1,164` seconds
by round; the cost is dominated by the base count, since every arbitration
mints a version and the layer's menu enumeration grows with the record,
and it now decides which questions can be asked at all.  (7)
**Determinism does not cover the flagship**, for cost.

> **What this section delivers.**  A second certified construction
> mechanism — **crossed conflict** — which generates uniformity and width
> *together*; a **proved** ceiling `k·b ≤ k²` with the necessary condition
> corrected from registers to **proposers**, now **realized at every `k`
> anyone has built — 9, 16, 25, 36 — where transport is capped at four**;
> the mechanism that realizes it named and cheap (**height-levelling**,
> supplied by the grammar's own idle event); a **whole** record that is
> 16 wide *and* inside both `d = 3` sprinkling band columns, so **there is
> no width-uniformity frontier**; and the same honest negative §B8.8
> found, now on the widest substrates that exist.  **The dimension road
> runs through crossed conflict, and its ceiling question is closed at
> every size tried.  The gauge road is still at zero.**

### B8.10 The even Gram — the rank-2 candidate, resurrected and deflated `[D73, LOG #487 → #488 → #491; round 1 TERMINAL]`

*Sources: `note-d73-even-gram-pin.md` (STRICT, FROZEN before any code, naming claim P2, tests 1–3 and falsifiers F1–F4 — and **not rewritten** by the result); `note-d73-even-gram-result.md`; `v10/code/d73_even_gram_exact.py` (**38 PASS / 0 FAIL**, 5 delivered outcomes, exit 0 — a statement about the G0/G1 anchors and not a summary of the FAIL count — 524 s, `python3.13`) + `data/d73_even_gram_exact.out`; `v10/reviews/d73-round1-hostile-review.md` — REVISE, 1 BLOCKER / 4 MAJOR / 5 MODERATE / 5 MINOR.  Parents: D71c, v2 paper 10 Prop 10.6, v6 paper 4 `:1064`, v6 paper 54, D63/D67.*

Width and charts are instruments.  The object arrow 3 is *for* is a
**rank-2 response**, and §B2.12(i) locates the corpus's own split: the
even/real channel carries the metric **diagonal**, the odd/phase channel
carries the **off-diagonal** (v2 p10 Prop 10.6).  D73 asks the even half
directly.

**The object.**  `v7/code/p30_reflection_positive_campaign.py:394-406`
computes, exactly,

```
G^even_{jk} = Σ_R P(R) E_j(R) E_k(R*)
```

prints its seven principal minors — reproduced here **character for
character** against paper 30 `:2991-2997` by AST extraction — and then
**discards the matrix in favour of its trace**, `K(E) = k·E_total`.  P2's
question: promote `K(E) = EᵀNE`; does the even channel host a genuine
rank-2 metric response?  Falsifier `F1` (pinned as an *implication*):
*`G^even` diagonal or `∝ I` ⇒ `E_total` is lossless, `K` is correctly
scalar, and the even channel provably cannot host a metric.*

**THE FIXTURE, first, because it changes what every other number means.**
The three dual pairs the Gram was built on are the ones paper 30 `§26.2`
**audits and falsifies**: they rank **11th** in the `N = 9` frontier, and
`1.67603622405300634803560e-5` — the number that circulates as "the
committed `TV_9`" and as "the family's floor" — is the score the paper prints
for the **loser**, directly above *"the previous theorem target is
falsified if read as a final predictive law."*  `§27` then selects
`{(912,25104), (17288,525076), (24576,540672)}` by a record-intrinsic
admissibility rule at `TV9 = 0` and `rec9 = 0` **exactly**; all four of
`§26.2`'s frontier triples reproduce `TV_9 = 0` here with the paper's own
atom counts `65703 / 65570 / 65544 / 65523`.

> **So `1.676e-5` is not a floor.  It is a sector-selection residual — the
> paper drives it to zero by changing *which flags to look at* — and no
> function whatever of the even 3-vector can reach it.  "Eleven quadratic
> forms and nothing moved" was fixture-guaranteed and discovered nothing
> about the even channel** (§0.3, §B10.15e).

**What survives, on the fixture the paper selects.**

| quantity | falsified `§25` triple | **SELECTED `§27` triple** |
|---|---|---|
| nonzero off-diagonals | 3 / 3 | **3 / 3** (`25.0626 / 29.3697 / 17.3517`) |
| distinct diagonal entries | 3 | **3** |
| eigenvalues | `108.0449 / 45.9226 / 20.8323` | (discriminant `5.840e10 > 0`) |
| anisotropy `‖traceless‖²_F/(tr²/3)` | `0.395835` | **`0.511428`** |
| `S₃` stabiliser | order **1** | order **1** |
| the family's `TV_9` floor | `1.676e-5`, a **sector residual** | **`0` exactly** |

`F1` **does not fire on either fixture**, and P2's factual half — *the
corpus computed a rank-2 object on the even channel and priced its trace*
— is **confirmed, more strongly on the selected fixture**.

**And `F1`'s implication is nowhere violated in the window.**  Run the
refinement comparison at every `N` rather than at `N = 9` alone: the Gram
is exactly `diag(1/20, 1/30, 1/30)` at `N = 5` (the three channel
indicators count 5-element subposets, so their supports are **disjoint**
— 0 of 63 records carry two at once), half-diagonal at `N = 6`, and
off-diagonal from `N = 7`; the trace becomes lossy as a colouring at
`N = 8`.  Where the antecedent holds, the consequent holds — a one-step
**lag**, which is the opposite of the two halves coming apart.

**The promotion, re-posed where it can have an answer.**

| candidate, `§27` fixture | atoms₉ | `TV_9` | `max_R\|h − h_full\|` |
|---|---:|---|---:|
| `k·E_total` (the trace) | 65523 | **0** | 0 |
| componentwise `(E₁,E₂,E₃)` | 65525 | **0** | 0 |
| `N = G^even(SELECTED)` | 65525 | **0** | 0 |
| `K(E) = E₃` only | 65511 | `2.293e-5` | 8/3 |
| `K(E) = (ΣE_j) mod 2` | 65496 | `1.087e-4` | 8/3 |

The floor is `0`; the trace attains it; a wrong `K` is **visibly
punished**.  The mechanism is **not** monotonicity of `TV_9` under
refinement (asserted, never proved, and contradicted by the committed
table's own `agg_linf`/`agg_l1` pair) but the **`h`-weight identity**: a
candidate whose atom-average weight function equals `full`'s at every
record has an identical `forward_tv` by construction — gated as a
biconditional at 18 candidates over two fixtures, zero mismatches.  And
the eleven rows are **two colourings** (9 + 2), computed by canonical
relabelling, not inferred: the table's visual weight overstated the
evidence 5.5×.

**The deflation of "reflection positivity".**  Each `DUAL_PAIRS` member is
gated to be a genuine order-dual pair, from which `E_j(R*) = +E_j(R)` and
`O_j(R*) = −O_j(R)` **identically** (0 violations in 394,578 tests).  So
the *reflected* even Gram **is** the ordinary second-moment matrix
`E[E_jE_k]` and the reflected odd Gram **is** `−E[O_jO_k]`: paper 30
`§25.4`'s positivity results are **algebra, not measurement**, and the
`i`-twist is the sign the grading puts there by construction.

**The `FAILS-FULL-GR` answer, sharper.**  v6 paper 4 `:1064` rejected the
scalar→tensor shortcut on a component count.  Half-cleared: `G^even`
supplies **6** independent components where the trace supplied **1**.
Still failing, three ways: those 6 are **one global form** for the whole
window with no per-atom index (and `789150` is p4's *counting rule*
applied to D73's record count — **not in p4's units**, not commensurable
with p4's `8193`, which was not recomputed); the per-record summand is an
outer product, so rank `≤ 1` — *a triviality true of every second-moment
matrix*, measured as the vanishing of all `2×2` minors at all 131,526
records, with rank 3 appearing **only after averaging**; and, decisively,
**equivariance**: a metric response must transform as `N → A N Aᵀ` under
whatever acts on its index, and nothing does — the order-dual acts
**trivially** on the even index, the `S₃` stabiliser is the identity alone
on **both** fixtures, and every `E_j` is a nonnegative count so the basis
is canonically oriented with no analogue of Prop 10.6's frame flip.

> **A scalar did not become a metric by interpretation.  It became a
> covariance matrix, which is a different thing.**

**The Prop-10.6 relation, stated as a DISTINCTION and not a
counterexample.**  `G^even₁₂ ≠ 0` is **not** a counterexample to Prop
10.6 and must never be cited as one: `G^even` is built *from* the endpoint
measure `P(R)`, so by 10.6's own argument it is invariant under any
representational sign flip.  Its off-diagonal is nonzero because the
channel basis is **canonically oriented by counting**, not because the
shadow recovered an orientation.  What the two share, located exactly:
**the orientation datum sits in the odd sector in both** — the even Gram
is blind to the order-dual, the odd Gram changes sign under it.
`[STATED, not computed]`

**The transfer probe, swept — and the hint INVERTS `[SAMPLED]`.**  The
attractive successor reading was that a rank-2 object belongs on the
generated line's **direction** index rather than v7's channel index.  On
this unit's own evidence, swept over seven blueprints, the direction index
is the **worse** stage:

| blueprint | events | wide charts | distinct matrices | stabiliser census | `∝ I` |
|---|---:|---:|---:|---|---:|
| `DOUBLE-RING(8,10,8)` (D63's winner) | 177 | 59 | **2** | `{(4,8): 59}` | 0 |
| `DOUBLE-RING(6,14,6)` | 181 | 71 | **2** | `{(4,8): 71}` | 0 |
| `DOUBLE-RING(4,26,4)` | 217 | 97 | **2** | `{(4,8): 97}` | 0 |
| `DOUBLE-RING(8,10,2)` | 117 | 8 | 3 | `{(4,8): 8}` | 0 |
| `wide_brick(8,14,2)` | 121 | 12 | 4 | **`{(4,8): 7, (4,2): 5}`** | 0 |
| `brick(8,14)` (narrow control, `\|D\| = 3`) | 65 | 42 | 5 | **`{(3,6): 38, (3,2): 4}`** | **4** |

The winner's 59 charts carry **two** matrices (51 + 8), one `D₄`-invariant
with a repeated eigenvalue and one **block-decomposable** with only two
distinct eigenvalues each doubled — *more* degenerate than v7's three
distinct ones.  Every `DOUBLE-RING` is 100 % stabiliser-8 **because a
double ring is built with cyclic symmetry and the direction index inherits
it**; the first non-ring wide record breaks the uniformity at 5 of 12.
And the narrow control — never actually measured by the census that cited
it — has **4 of 42 charts exactly `(1/4)I`**, `F1`'s literal antecedent
firing on the v10 side, with 38 of 42 at the full `S₃`.  It is also **not
the same treatment**: co-occurrence of 0/1 indicators under a uniform
measure on shadow rows, with **no reflection at all** — three of four
ingredients differ from v7's object, and the missing one is the whole
subject of the deflation above.

> **THE REDIRECTION'S REDIRECTION `[MY READING]`.**  A large stabiliser
> means **fewer** free components: a `D₄`-invariant `4×4` symmetric form
> is confined to a 3-dimensional span inside `Sym²(R⁴)`, where v7's Gram
> is a generic point of the 6-dimensional `Sym²(R³)`.  The receipt's own
> `F1`-instrument control is a `7I` whose stabiliser is the full group.
> **A form with a big stabiliser is a cage, not a metric.  A tensor stage
> needs *generic* — stabiliser-1 — direction geometry: sprinkling-like
> substrates, or crystals with deliberate defects.**

**Licensed, fixture-scoped.**  `[MEASURED, N = 9, BOTH FIXTURES]` `G^even`
is positive-definite with three distinct nonzero off-diagonals, three
distinct diagonal entries and stabiliser 1; `F1` does not fire on either.
`[THEOREM at the fixture, gated]` the `E`/`O` parity identities and hence
the algebraic status of `§25.4`.  `[MEASURED]` the `N = 5` diagonality by
disjoint support; the two-colouring count; the trace lossy only from
`N = 8` while destroying 98.9 % of the even 3-vector's distinctions
(4,505 values → 49) and moving the atom count by two; and the ablation
costs — removing the even coordinate `43.1×`, the odd one `63.7×`, both
`299.7×`, so **the even channel matters and the decomposition beyond its
trace does not**.  `[SAMPLED]` the seven blueprints.

> **D73 no-go (fixture-scoped, two named fixtures).**  *At the `N = 5..9`
> window of v7 paper 30's rooted boundary law, under both the falsified
> `§25` triple and the `§27` SELECTED one, the dual-even channel's
> second-moment form is anisotropic and positive-definite with a trivial
> relabelling stabiliser, and is nonetheless predictively equivalent to
> its trace for the deletion-graph law — on the selected fixture the trace
> attains `TV_9 = 0` exactly, and the reason no promotion improves on it
> is the `h`-weight identity, not a ceiling.  The form carries no atom
> index, has rank 1 locally, and admits no group action on its channel
> index.  **On this substrate the even channel hosts a covariance, not a
> metric response.**  `FAILS-FULL-GR` stands.*

**Explicitly not licensed:** that `G^even₁₂ ≠ 0` evades Prop 10.6; that
anything here is a metric, a response, a field or a graviton; that the
anisotropy survives to any other window, substrate or measure; that the
v10 charts' stabilisers are substrate symmetries; **that the direction
index is the stage**; **that `1.676e-5` is any kind of floor**; and that
`F3` (the anticommutator test) has been decided — it is **OPEN and
explicitly deferred**, since a co-occurrence matrix over chart directions
is not an anticommutator of the generated line's transports under any
reading, and the honest test needs the d42b1 transport pair itself,
symmetrised.

**Residues.**  (1) The `N`-dependence is unexplained — anisotropy rises
monotonically `0.0408 → 0.0882 → 0.1732 → 0.2812 → 0.3958` across
`N = 5..9` with no sign of saturating, and `N = 10` was not attempted.
(2) **The selected fixture's Gram was not swept over `N`, centred or
reweighted** — the cheapest remaining question in the unit.  (3) The
**odd** sector's off-diagonals are unexplored: paper 30 swept 253
*diagonal* `M` and never scanned off-diagonal; measured here they are
mixed-sign (`−0.01220, −5.64990, +0.39107`), one of them large, and the
odd-sector promotion **on the selected fixture** is the obvious successor
now that the ceiling argument against it is retracted.  (4) Two live
routes only, and neither is the direction index: *understand the selected
fixture's structure* — why `§27`'s coarseness rule lands on a triple whose
second moment is *more* anisotropic than the falsified target's — and
*get charts with generic direction geometry*.

---

## B9. The transport wall and the sector crack

*Non-technical twin: Part A, chapter A9.*
*Source: `note-d56-transport-sigma-probe.md` + `v10/code/d56_transport_sigma_probe.py`, LOG #432.*

> **STATUS, binding.**  This is a **PROBE / ADVISORY**, not a pinned unit:
> no pin, and the ledger entry that records it says so.  The **two
> load-bearing claims were independently verified against the committed
> layer** before acceptance (both reproduce exactly).  Everything else must
> be re-derived before any pinned unit relies on it.  The probe's own
> caveats C1–C7 are reproduced in §B9.5.

### B9.1 The obstruction: the self-arbitration ladder `[EXACT, depth-free]`

**Construction.**  `v_0 = genesis`; rung `k+1` is `('p','A',v_k,0)`
followed by the blind self-arb `('r','A',{(A,v_k,0)},{(A,v_k,0)})`, which
mints `v_{k+1} = vname(v_k, {(A,v_k,0)}, 'A')`.

**Mechanically verified for `k = 1..10` in the committed layer `[EXACT]`:**

| rung | `\|holdings(A)\|` | delivery options | weight each | sector total | non-delivery menu = previous? |
|---|---|---|---|---|---|
| 1 | 2 | 2 | `1/8` | `1/4` | — |
| 2 | 3 | 3 | `1/12` | `1/4` | yes |
| 3 | 4 | 4 | `1/16` | `1/4` | yes |
| … | … | … | … | … | yes |
| 10 | 11 | 11 | `1/44` | `1/4` | yes |

Every rung admissible; `|holdings(A)| = k+1` exactly; the ten weights
pairwise distinct; **delivery sector total exactly `1/4` at every rung.**

**The induction `[EXACT, depth-free]`.**  `v_{j+1}` has strictly greater
nesting depth than `v_j`, so `v_0..v_k` are pairwise distinct.  `A`
proposed in every rung's component key, so
`holdings(A) ⊇ {v_0,…,v_k}`.  Only `v_0..v_{k−1}` are superseded, so
`('p','A',v_k,0)` is admissible and the ladder extends for every `k`.
And **`deliver_options_in_view` reads the WHOLE holdings set**, superseded
members included, so A's delivery sector has exactly `k+1` options, each
priced `(1/4)/(k+1)`.

**Therefore** the menu takes infinitely many values — in its *cardinality*
and in its *multiset of rational weights*, neither of which any renaming
can move.  If `sigma` is menu-exact then `sigma(h) ↦ menu(h)` is
well-defined, so `sigma` has at least as many values as there are menus:

> **`[EXACT]` NO BOUNDED MENU-EXACT LOCAL-STATE ABSTRACTION EXISTS AT
> TRANSPORT SCOPE, FOR ANY DESIGN.**  D52's T2 is answered: **blow-up, and
> by an obstruction, not by a growth curve.**

**Why d42a escapes it — and what that says about the prize result.**
Delivery-free, holdings are read only through `prop_options_in_view`,
which **skips superseded versions**, and the non-superseded holding is a
singleton (D44a SG2).  The unbounded coordinate exists there too; it is
simply **invisible to the menu**.  Transport makes it visible.

> **The 36-state closure is a starvation artifact** of the same species as
> the fork-freeness artifact d42b1's P2 already found.

**Width stability `[MEASURED, SAMPLED]`.**  At three actors the ladder has
`(n−1)·|H|` delivery options: **4, 6, 8, 10, 12** options at
`1/16, 1/24, 1/32, 1/40, 1/48`, **sector total exactly `1/4` throughout**.
The two-actor conclusion looks width-stable.

### B9.2 The design that was instructed, and its refutation

D51's four projections on the **full view** were the design this probe was
instructed to use.  Implemented verbatim (`mode='full0'`, same renaming
quotient) and **refuted**: **3,656 violations over 30,454** equal-sigma
pairs.  The minimal counterexample is the W1/W2 witness of §B3.3.

> **`[MEASURED]` D51's four-projection reduction does not lift to transport
> scope.  Any pinned unit that reuses it will be measuring a non-object.**

Hence the forced replacement: the **join-view lattice** of §B3.3, with
`holdings(a)` keeping its **superseded** members (because
`deliver_options_in_view` enumerates over the whole set — this is not
optional, and §B9.1 shows this single fact decides the question).

**What the refined `sigma` drops, exactly:** lineage depth (a version
nothing else references becomes an opaque node with no parent — *this is
the quotient D52's T1 asked for*); superseded marks on unreferenced
versions; the content of opaque nodes; holdings/merge-pairs of non-members
of `S` inside `V_S`; `created` as a separate projection; and all event
indices and order information beyond what survives as component edges and
merge-pair incomparability.  Canonical form: 1-WL colour refinement on the
version layer using only renaming-invariant data, then the lexicographic
minimum over the residual colour classes.  On the whole family to depth 6
the refinement was already discrete (**max colour class 1, max residual
permutations 1, 0 permutation-cap hits** against a printed cap of 720), so
canonicity is not in question on this window and `|Aut| = 1` everywhere.

### B9.3 The refined sigma is menu-exact — and still blows up `[MEASURED]`

| abstraction | classes | equal-sigma pairs checked | violations |
|---|---|---|---|
| `sigma` (join-view lattice) | 541 | 30,188 | **0** |
| `full0` (D51 four projections, full view) | 275 | 30,454 | **3,656** |

Menus compared as **renamed event multisets with exact `Fraction`
weights**.  The `full0` row doubles as the **anti-vacuity control**: the
instrument does detect coarseness when it is there.

**Transition determinism:** `sigma(h+[e])` is a function of
`(sigma(h), renamed e)` — **1,540 (state, event) pairs over 30,728
transitions, depth ≤ 4 exhaustive, 0 nondeterministic pairs.**  So the
D44a BFS method is legitimate here.

**Exhaustive census to depth 6** (anchors reproduced from the committed
census: cumulative `[1, 9, 69, 521, 3969, 30729]`, and **243,769** to
depth 6 — both match):

| depth | histories | distinct `sigma` | NEW |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | 8 | 5 | 4 |
| 2 | 60 | 17 | 12 |
| 3 | 452 | 61 | 44 |
| 4 | 3,448 | 191 | 130 |
| 5 | 26,760 | 541 | 350 |
| 6 | 213,040 | 1,567 | 1,026 |

**Frontier-exhausted BFS, hard cap 20,000 states / 480 s (both printed):**
`5, 17, 61, 191, 541, 1567, 4679, 14413, 20000 (CAP)` at level 9 —
**NOT CLOSED**, with 5,587 unexpanded frontier states at the cap.

**A reading trap this table sets, and it must not be walked into.**
`cumulative == per-depth` does **not** mean "no state ever recurs": the
per-depth state sets are **nested** — appending `('n',a)` changes no
projection whatsoever — so **recurrence is total**.  The only informative
column is **NEW**, which grows by a factor ≈ 2.9 per level with no sign of
turning over.  And the blow-up verdict rests **on the ladder**, not on
this table.

**Growth diagnosis (M4).**  At reachable depths the fastest-growing
component is the **per-view live-proposal / component structure** (284 and
288 distinct values at depth 6) — i.e. **the knowledge lag between the
three views**, precisely the coordinate that does not exist at d42a scope.
The version layer is second (123).  The holdings *counter* is the slowest
(13 distinct count-vectors) — **but at depth-free level the ranking
reverses**: the counter is the one **provably** unbounded; the others are
merely large here.  So a pinned unit must attack **both**.

### B9.4 The crack: aggregation, and where it survives

The menu-exactness no-go bites the **intra-sector split**, not the sector.

> **`[EXACT, verified in-layer]` THE DELIVERY-SECTOR TOTAL IS EXACTLY
> `1/4` AT EVERY RUNG.**  The per-option weights vanish; that aggregate
> is constant.  (This is a property of the **delivery** sector
> specifically, not a law of sectors — §B9.4b.)

**Why that is more than a curiosity.**  D50's round-1 diagnosis (§B6.12)
established independently that the record-level observables are the
**aggregated** ones: what is observable is the probability of moving from
one class of situation to another, and a per-event demand would be a
demand on unobservable event labels.  **So the obstruction kills exactly
the class of description the corpus has separately shown is not the
physical one.**

**Measured consequences that make the escape candidate non-empty:**

- the **non-delivery part of the menu is constant from rung 2 on**;
- define `lump` = `sigma` with each holdings set replaced by (its
  non-superseded part, `min(|holdings|, T)`).  Then on the whole depth-5
  family the **non-delivery menu factors through `lump` exactly**
  (`T = 2`: 0 violations / 30,236 pairs; `T = 3`: 0 / 30,228);
- and the **delivery-LUMPED step distribution** (non-delivery events kept
  individually, the entire delivery sector aggregated by successor
  lump-state) **is a function of the lump state** — 0 violations over
  3,782 same-state pairs at depth ≤ 4, 187 lump states.  That is
  probabilistic bisimulation for the lumped chain, on that window.

**And the lumped chain does not close either, within the caps
`[MEASURED, not decided]`:** BFS at `T = 2`, cap 20,000 / 480 s →
`1, 5, 17, 61, 187, 493, 1223, 3099, 8241, 20000 (CAP)` at level 9.

> **So killing the counter is NECESSARY and demonstrably NOT SUFFICIENT.**
> The residual explosion is the view-product structure of §B9.3.

The natural next move — demand exactness at *sector* rather than per-option
granularity — is the subject of §B9.4b, and it closes.

### B9.4b The sector-exact escape, closed at `(actor, type)` granularity `[D57, LOG #436; batch-round reviewed and repaired]`

Receipt `v10/code/d57_sector_exact_refinement.py`, **3 PASS / 0 FAIL**,
exit 0, caps 3/4/5/6 **exhaustive** (**521 / 3,969 / 30,729 / 243,769**
histories).  The question: does the **coarsest sector-lumpable
partition** — the one induced by the aggregated transfer
`T_s(h, c) = Σ q over sector s landing in class c` — stay finite at
transport scope?  The pin expects sector quantization to hold, as the
**finite-alphabet prerequisite**, and gates it first.  **Both halves are
negative, and each refutes a pre-registered expectation.**

**(1) SECTOR QUANTIZATION — the values are richer than `{0, 1/4}`, but
the alphabet may be COMPLETE, and this ground is WITHDRAWN.**
`{0, 1/4}` does die immediately: **arbitration sectors reach `1/2`** via
subset choices, and `1/8` appears at cap 6.  But the inference from
"three values" to "unboundedly many" does **not** hold at this scope.
The arbitration denominator is `|comps| + |merge_pairs|`, and in the
unit's own exhaustive data **`max |comps| = 1` at every depth**, while at
two-actor scope **`merge_pairs ≤ 1` is proven** — so the observed
`{1/2, 1/4, 1/8}` **may be the complete alphabet**.

> **So §B9.4's `1/4` is a fact about the DELIVERY sector rather than a
> law of sectors — but the finite-alphabet prerequisite is NOT refuted at
> this scope.  The sector verdict rests on ground (2) ALONE.**

**(2) THE COARSEST SECTOR-LUMPABLE PARTITION DOES NOT STABILIZE.**  Read
as lookahead convergence, per-depth fixpoint counts across caps 3/4/5/6:

| depth | cap 3 | cap 4 | cap 5 | cap 6 |
|---|---|---|---|---|
| 3 | 7 | 16 | 16 | **17** |
| 4 | — | 9 | 23 | **27** |
| 5 | — | — | 11 | **33** |

**Even depth 3 creeps at cap 6**, and nothing comparable stabilizes.
`[MEASURED]` — blow-up evidence at this window, not a theorem.  **And a
trivial-boundary control STRENGTHENS it:** the fixpoint counts are
**lower bounds**, so the blow-up reading is the conservative one.

> **VERDICT: the sector-exact escape, at `(actor, type)` granularity, is
> CLOSED — even AGGREGATED bookkeeping at this granularity fails.**  On
> **one** ground, the refinement, measured at caps 3–6 with the counts as
> lower bounds.

**The asymmetry of evidence, respected.**  The verdict rests on ground
(2) alone, and ground (2) is `[MEASURED]` at caps 3–6 — a window result,
not a theorem, though a conservative one given the lower-bound control.
That is a weaker footing than §B9.1's, whose ladder is exact and
depth-free, and it should be quoted as such: **the sector-exact escape is
closed on measured evidence at this granularity, not by an
obstruction.**

**What the crack narrows to** (both untested, both live): **strictly
coarser aggregations** — type-only sectors, total-budget only — and
**abstractions that give up exactness** and target only the completion's
**observable** demands, with the standing warning that the aggregated
reading is the correct one for *stating* demands and is also what makes an
exact aggregated bookkeeping hard to build.  **Residues:** depth 7; an
actor-swap quotient (counts `≤ 2×`, so it cannot rescue the trend alone).

*Status: batch-round reviewed, repaired and delta'd — with the first of
its two published grounds withdrawn in that round, which is why the
verdict above rests on one.*

### B9.5 Caveats, binding

- **C1.** The no-go is about **menu-exact** abstractions — exact weights
  *and* exact renamed event identity.  It does **not** exclude coarser
  objects (sector-level descriptions, lumped chains, level-structured /
  QBD or R-matrix descriptions).  It **does** exclude the finite transfer
  matrix that Perron theory needs at d42a.
- **C2.** `sigma` is menu-exact but **not proved minimal**.  Its measured
  curve is an **upper bound** on the minimal menu-exact state count at
  each depth.  The *lower* bound that matters is the ladder's: infinite.
  **The qualitative verdict is design-independent; the growth numbers are
  not.**
- **C3.** Join-view completeness is `[MEASURED to depth 5]`, 0/243,768
  exceptions.  The arb-renewal register escape is a real structural
  possibility this window did not exhibit; a pinned unit must either rule
  it out or add those views.
- **C4.** The factorization and determinism results are finite-depth
  **evidence, never premises**; the three-actor arm is a **sample**
  (lower bounds only).
- **C5.** Determinism: `PYTHONHASHSEED=0`; every canonical form is a
  post-renaming-**sorted** plain-tuple serialization (no raw `frozenset`
  reprs — the D49 A4 lesson).  All caps printed by the script.
- **C6/C7.** Nothing committed to git as a unit; the script was run twice
  with **every count, curve and violation number byte-identical** — which
  is reproducibility evidence, not a proof of order-independence.

### B9.6 The consequence for the programme

> The method that settled the dichotomy at d42a — **finite menu-exact
> quotient + Perron** — **provably cannot transfer** to the scope where the
> dimension results live, and the convergence question (*does the measure
> prefer 3+1?*) is blocked on exactly this.

The named live routes, from the probe's §7 (what a pinned unit should
gate): the **delivery-lumped chain**, or a **level-structured
(QBD / R-matrix / Martin-boundary)** description with `|holdings|` as the
level — which connects to the **already-built D46b transport-scope
Martin/R-theory machinery** rather than to Perron.  And one thing a pin
should *not* do: pre-register an expectation of closure or non-closure for
a coarser-than-menu-exact object.  *D52 was right to record none; the
ladder decides only the menu-exact question.*

**And the escape candidates that remain** are those §B9.4b leaves: strictly
coarser aggregations, and descriptions that abandon exactness for the
completion's observable demands only.  §B9.7 is the route that has
actually been walked, and it is the one that never asks for a bounded
summary at all.

**For completeness, the transport-scope Martin results already in hand
(D46b, after review — three reversals, and one **forward correction** from
§B9.7):** `root = renewal` **does** transfer at matched horizon (an
earlier "does not transfer" claim was a horizon-mismatch artifact and was
withdrawn); the pinned sector-normalized conditional is **exactly
horizon-stable at the root** — and that is a **symmetry theorem**, not a
measurement (§B9.7); contraction is **true and strengthened** but **not at
a constant rate** — the sequence is `0.738, 0.399, 0.086`, and **MB3-e's
"root drift contracts monotonically to `r = 6`" is FALSE at `r = 7`**, the
absolute root sequence rising by `×7.509` at the sixth step, identically
in all three norms and not a window artifact; and deliveries **REDUCE**
branching (the earlier claim had the sign wrong; peak at `D = 5`, down at
`D = 6`).

### B9.7 The horizon limit — the surviving route, and what remains `[D69 scoping; D70, LOG #482 → #484 → #489; round 1 TERMINAL]`

*Sources: `note-d69-measure-campaign-scoping.md` (the campaign map — a survey, not a pin, every number attributed by file and gate); `note-d70-horizon-limit-pin.md` (STRICT, frozen from the survey's draft unchanged and committed **before** any code, naming this note and the receipt before either existed); `note-d70-horizon-limit-result.md`; `v10/code/d70_horizon_limit_exact.py` (**51 PASS / 0 FAIL**, of which **7 are theorem-passes named by the receipt itself**, 4 delivered outcomes, exit 0, 1,085.8 s) + `data/d70_horizon_limit_exact.out`; `v10/reviews/d70-round1-hostile-review.md` — REVISE, 5 MAJOR / 4 MODERATE / 5 MINOR, arithmetic verdict "I broke nothing in the arithmetic.  I broke the readings."*

**The campaign.** LOG #481 records the frontier synthesis: a space-*making*
mechanism that is engineered rather than emergent; dimensionality
**unselected** (`k` is a dial); typicality **unposable**; the quantum
layer **excluded** at proven scope.  *All four are the same missing
object — a measure at transport scope* — which is precisely what §B9.1's
wall forbids building the naive way.  The campaign is the measure itself,
attacked from what the wall leaves standing.

**The walls, stratified by grade** (the scoping survey's core discipline,
because the campaign mis-plans if they are quoted at one grade):

| wall | content | grade |
|---|---|---|
| **W-A** §B9.1's self-arbitration ladder | no bounded **menu-exact** abstraction, **any** design | `[EXACT, depth-free]`, from an **advisory probe**; two claims re-verified |
| **W-B** menus run on per-actor views | world-state designs dead; join-view menu-exact and merely infinite | `[MEASURED, depth ≤ 5]`, same probe |
| **W-C** §B9.4b | sector-exact closed at `(actor, type)` **only**, one measured ground, counts are lower bounds | `[MEASURED, caps 3–6]`, reviewed unit; finite-alphabet `[OPEN]` |
| **W-D / W-E** | no menu-shape transfer; the intrinsic chain escapes its windows | `[MEASURED]`, terminal units |

W-A kills only finite **menu-determining summaries** — *not* sector
descriptions, lumped chains, inexact abstractions, or non-abstractions.
**Nothing in the corpus forbids a per-history kernel.**  Nine routes were
enumerated and ranked; **R4, the horizon limit, ranks first as the only
route that needs finiteness nowhere**, with R5 (regenerative) as its
proof engine and R1/R2 (type-only, budget-only) as a cheap arm in the same
receipt.

**The object.**  D46b's relative-horizon kernels

```
k_r(e|h) = q(e|h) · G(h + e, r − 1) / G(h, r)
```

extended from a 30,729-history family at `r = 1, 2` to a **243,769**-history
family at `r = 1..7`, at **three actor pools** — the widest built to
**332,697 histories at depth 4** — under **five** declared terminal
conventions, with a symmetry analysis, a renewal analysis, an aggregation
arm, four controls and a wall diagnostic.  **51 PASS / 0 FAIL**, of which
**7 are theorem-passes named as such** by the receipt itself, 1,086 s wall
clock (the campaign's longest; the four-actor depth-4 arm alone is 408 s
serial).  The **pinned object is the sector-normalized conditional**;
absolute completed weights are horizon-bound (D44f) and are **context**,
and that doctrine now runs in **one** direction everywhere including the
outcome decision.

**(1) Properness `[MEASURED → identity]`.**  `Σ_e k_r(e|h) = 1` exactly at
every computable `(h, r)`, `r = 1..7`.  Cut-additivity of the chained
measure follows **by induction from properness** — it is a product of
probability kernels — so HZ-IV was disposed of by construction; the
substantive gate is **strict positivity**, the only way the identity can
break.  New window facts: `G_7 = 2168717/16384`; D46b's committed
four-term family-uniform sup is a **lower bound** on the deeper family and
its fourth term understates by **×1.92**.

**(2) The Cauchy table `[MEASURED]`.**  Pinned object, `L∞`, two actors:

| `L` | `r=1→2` | `r=2→3` | `r=3→4` | `r=4→5` | `r=5→6` |
|---|---|---|---|---|---|
| 1 | 1/18 | 4/171 | 8/741 | 176/32877 | 302623/103087098 |
| 2 | 1/18 | 4/171 | 8/741 | 176/32877 | — |
| 3 | 1/18 | 4/171 | 8/741 | — | — |

**Every off-root row contracts, in all five norms, at two, three AND four
actors.**  The four-actor `L = 1` row — the one an earlier reading
announced as the route's negative — is a row in the **absolute** kernel
with three terms, `29/8288 → 23117/6594399 → 33367649/10728807102`:
`+0.19 %` then **`−11.28 %`**, ending **below its first term**; the
**pinned** row at that pool never rose at all
(`1/102 → 691/89913 → 902551/161966810`, `−21.61 %` then `−27.49 %`).  The
unit's own three-actor **root** row does the same thing (a `×1.50` rise at
step 2, a fall at step 3), so a two-term rise was already known inside the
receipt to be non-diagnostic.  Terminal `0`s in the family-uniform
conditional rows are **root-only window artifacts** — gated, marked, and
struck from every contraction claim.

> **THE VERDICT: contraction at every pool and depth measured**, with the
> two-term rise reported as a blip.  Delivered outcome: **`HZ-III`'s shape
> without `HZ-III`'s licence** — the standing label is *"root-free over
> the computed horizons"*, explicitly **not** a boundary theorem, because
> no bound was exhibited.

**(3) The horn gate `[THEOREM + MEASURED]`.**  Five terminal conventions
(`G(h,0) = 1`; branch count; menu mass; a sector-weighted **equivariant**
one; and a deliberately **non-equivariant** one).  They differ at **every
single history** — the truncation is a choice, not a formality.  But:

> **`[THEOREM, from the committed layer]`** `A ↔ B` and `0 ↔ 1` are exact
> automorphisms (0 violations over 521 histories; `G` invariant), the root
> menu is **one orbit per event kind**, and therefore **every equivariant
> terminal is forced to the same root conditional** — `p: ¼,¼,¼,¼`;
> `d: ½,½`; `n: ½,½` at every horizon.

So D46b's "root drift exactly 0 at `r = 1..6`" and the horn's root leg are
**the same identity**, and neither carries information about horizon
stability or convention independence.  A **non-equivariant** terminal
separates by `1/6` at `r = 1`, which is what makes this a statement about
the terminal's **symmetry class**.  The horn's genuine content is
**off-root**, where the pinned separation shrinks over five terms
(`1/8, 1/12, 487/7790, 40337/800358, 109092211/2569013838`), on a fixed
eight-history window at the deepest rows.

**(4) The lemma slot: no bound, one route closed, one route OPEN.**  Two
renewal ports:

| | count | menu = root's under renaming | re-entered |
|---|---|---|---|
| **R-SIG** (every actor's **non-superseded** holdings a singleton) | **5,161** | 1,365 / 3,796 | **3,796** |
| **R-MENU** (holdings exactly `{v}` for every actor) | **1,365** = `Σ_{n≤5} 4ⁿ` | 1,365 / 0 | **0** |

`[EXACT]` **holdings never shrink** — 0 shrinking transitions,
exhaustively, and a one-line theorem of the layer — so **R-MENU is
absorbing-complement and that route is CLOSED**; by depth 5 the
never-regenerating set carries **`1671053/2168717 ≈ 0.7705`** of
horizon-completed mass.  But the layer *does* have a shrinking set
(`superseded` grows), which is exactly why the argument covers R-MENU and
nothing else.  On **R-SIG** the `N`-step hitting zero-set collapses
`2520 → 84 → 4 → 0` and the 4-step infimum is `118/1455 ≈ 0.0811` on the
window where it is computable — *the shape of a Doeblin condition, not of
a closed route*.

> **NARROWED: the MENU-EXACT ATOM route is closed; the σ-level renewal
> route (R-SIG) is OPEN.**  And classical Doeblin minorization
> `P^N(x, ·) ≥ δ ν(·)` needs **no atom at all**.  **No operator-level
> minorization — Birkhoff / Hilbert-metric contraction of the positive
> backward recursion `G` — has been attempted anywhere.  That is the
> campaign's named successor proof engine and its only surviving
> candidate.**  *(The `N = 4` and `N = 5` windows are 9 and 1 histories.
> This is not a bound and none is claimed.)*

**(5) The aggregation arm `[MEASURED, caps 3–6, LOWER BOUNDS]`.**
Type-only and budget-only lumping both blow up and both fail the
last-two-caps decider at every comparable depth, S4-controlled, with a
depth-3 class of 84 histories splitting 64/20 between caps 5 and 6.
**But they are ONE closed route, not two**: `sec_budget` differs from
`sec_type` only by merging `r` and `m`, `m` events occur only at parent
depth 5–6, and the decider uses depths 0–4 — so the two maps induce the
**identical partition on the decider's whole input**, gated.  Route R1
closes on measurement; **R2's closure is inherited, not measured**, and
extending it to a cap where merges have support is the honest residue.
Finite-alphabet stays `[OPEN]` both ways.

**Controls.**  The instrument can fail: of the two declared **weight-law**
perturbations one (idle `×100` at even depth) breaks contraction, and the
one declared **grammar** perturbation breaks it too — a distinction the
receipt reports by kind, since collapsing the two would let a grammar
change stand in for a weight-law perturbation.  `Ẑ`'s
positive control is exact (`ker(T − 2I)` one-dimensional with generator
`{1, 4/3, 7/3}`).  Determinism byte-identical at three hash seeds, with
the digest widened to cover every arm a defect was found in.  *(A
by-product worth recording: two equal `frozenset`s can carry different
`repr`s in one process, so every menu comparison was converted from a
repr sort to a set comparison.)*  **HZ7, diagnostic only:** the B1 ladder
does **not** survive a restricted delivery enumerator — the committed
layer is unchanged, nothing else in the receipt uses it, and **adopting it
would be a different theory**.

**Licensed, and not.**  Every claim is scoped to transport scope, the
declared families and caps, in exact `Fraction`s, with **no
infinite-volume claim under any outcome** (scanned, not asserted).  Not
licensed: that this is *the* click law's measure (the missing map is
untouched); any dimension, typicality or quantum-layer claim; and — the
lexical prohibition the pin imposed and the receipt enforces on **all 51**
gate labels — the word *converges*.

**Residues.**  (1) The three-actor pool at depth 5 (713,967 more
histories) is the one pool residue left.  (2) The root reversal's
mechanism needs `G_8`, i.e. a depth-7 family (~1.9M histories), to say
whether `r = 6 → 7` is one turn or the onset of oscillation.  (3) A
**systematic family of non-equivariant terminals**, which is what actually
probes the root invariance.  (4) The renewal window is depth ≤ 5 because
the predicate needs full views.  (5) **The successor proof engine**
(above).  (6) Extending R2 to a cap where merges have support.  (7) D57's
own residues, and the join-view lattice completeness caveat, which any
successor building a `σ` on these kernels must re-verify.  (8) The pin's
own gap, recorded: it set **no minimum-evidence bar** on the clause that
fired, and a binary clause that can fire on a two-term row at the
shallowest cap is one a unit can satisfy without learning anything.
*Successor pins should price the evidence as well as the direction.*

---

## B10. The graveyard, itemized

*Non-technical twin: Part A, chapter A10.*

Format: **CLAIMED → KILLED BY → SURVIVED.**  Every entry is a real,
recorded retraction with its ledger location.

### B10.1 Dimension counting as a spacetime-dimension estimator

**Claimed:** order dimension grades how close a record is to 3+1.
**Killed by:** the doctrine of §B7.1 — DM dimension coincides with
Minkowski dimension **only at 2**; every ≥2+1 Minkowski space has infinite
DM dimension; dimension-3 orders exist that embed in no Minkowski space.
Then, from inside, D46d's headline collapse (§B7.2).
**Survived:** order dimension as a **1+1-escape detector** and
**clock-complexity grade**; the corrected typicality reading (order
dimension ≥ 3 is typical-in-the-making, not unbounded dimension); the
calibration horn, which did not fire; and the reframing onto skies.

### B10.2 The `tau` own-view route to (H1) `[D46a, LOG #394–#397]`

**Claimed:** per-actor own-view abstractions `tau_A, tau_B` are functions
of `sigma`, which would discharge (H1).
**Killed by:** its own round.  **`tau` is not an own-view object**: the
menu view strictly exceeds the noop cone on **1,016 of 12,942**
actor-histories (7.9%), max 4 extra events, **all opponent-authored**.
Also withdrawn in the same pass: (H0), wrongly dropped, was restored; and
"(H2) is subsumed" was withdrawn as **inverted**.
**Survived:** the lag measurement itself, now load-bearing everywhere; and
the menu view's idempotence (`0/12,942`).

### B10.3 The wire-closure route to (H1) `[D51, LOG #423/#424]`

**Claimed (pre-registered, by the author):** a candidate touching base `b`
already sees every live proposal on `b` by wire closure, so the lag is
menu-invisible and (H1) follows **at every depth with no induction**.
**Killed by:** measurement — **every event type lags** (`n` 4,606/12,942;
`p` 5,636/12,916; `r` 3,820/8,516), because the projections are the
full four-tuple over **all** bases while a candidate's view need only
cover the base it touches.  Then, worse: **monotonicity fails** — **a
smaller view can yield MORE options.**
**And the mechanism first named for it was itself refuted:** the
own-proposal clause (*"`prop_options_in_view` excludes a base the actor
already has a live proposal on, so a view missing that proposal includes
the base"*) **can never fire** — an actor's own live proposals are always
in its own cone (0 of 68,750 pairs).  MV2's mechanism is **missed
supersession** (9,656 of 9,656 excess options), and the `'r'` arm lags
too.
**And the reduction it offered in place of the refuted route is itself
inverted:** the four projections **REFINE** `sigma` (209 keys against 32
states), so (H1) was **not** reduced in the claimed direction.
**Survived:** three refutations that still bind — every event type lags;
**a smaller view can yield MORE options**; and therefore the general bar
*no depth-free argument may assume view monotonicity*.  **(H1) was
eventually proved by a different route entirely** (§B6.13), through
`sigma` directly, which is why that proof is untouched by this
inversion and does not import the refuted clause.

### B10.4 Circular-ones as the primary sky instrument `[D47a, LOG #409]`

**Claimed:** a two-sided arc-realizability test decides
circle-versus-sphere in both directions.
**Killed by:** the control.  It **rejected 121 of 554 genuine 2+1 skies**
as non-arc (later recounts: 218/397 under one reading — a majority).
**Survived:** shatter-4 alone as the load-bearing instrument; the
**empirical vindication** of the one-sidedness doctrine; and the general
lesson that killed two later headline sentences — *discrete skies of real
Minkowski are not continuum trace systems, so "not realizable as X ⟹ not
that dimension" is not available as a premise.*

### B10.5 Ratio-preserving completions `[paper 30 §5.2]`

**Claimed:** implicitly by "just normalize the weights".
**Killed by:** the theorem of §B6.3 with a **36-of-202** certificate in
**two** diamond-connected components, plus the named mechanism
(double-counting the causally blind join layer).
**Survived:** everything downstream — the impossibility is what makes the
completion question a question.  And a self-correction: "N is NOT
cut-attached" was **false**, withdrawn, and replaced by the **stronger**
statement (cut-attached but not a gradient).

### B10.6 The zero-class counterterm `[note-d42b3… D3]`

**Claimed:** filtering to own-view components restores sums ≡ 1 exactly
and gauge-invariantly, refuting the no-go.
**Killed by:** it **abolishes ALL joint arbitration** `[EXACT]`.
**Survived:** the no-go **narrowed** to support-preserving (strictly
positive) counterterms, by a printed and gated nesting argument, with the
zero class **declared excluded** and the reason stated.

### B10.7 "Sign A, hold B" — the entire laboratory bridge `[d41c, LOG #404/#405]`

**Claimed (2026-07-19, #404):** two platform declarations, with A (a
single-ion hyperfine platform) the strong one and B (a
Talbot–Lau interferometry platform) declared strictly weaker; the
recommendation carried to the user was **"sign A, hold B"**.
**Killed by (2026-07-24, #405):** the author's own objection, quoted
verbatim in the note's §1A and **conceded in full** — *an ion is an
enormous object in record terms*; the corpus has not built the QFT layer;
and the spacetime being constructed is the **background** on which such
fields would live.  Four things recorded:

1. **The scale gap `[ILLUSTRATIVE only, not a corpus claim]`:** at Planck
   spacing `1.62 × 10⁻³⁵ m` against a proton at `~1.7 × 10⁻¹⁵ m` the ratio
   is `~10²⁰`, so rescaling the record spacing to 1 mm puts the proton at
   `~10¹⁷ m` — of order **ten light-years**.
2. **The corpus cannot even fix that scale:** v6 paper 57's unified no-go
   gives exactly **one** record length with Newton's `G` **provably
   un-fixable**, so the record scale is a free parameter and presuming the
   laboratory sits far above it (or at it) is un-derived either way — **a
   second, independent hole in the same slot.**
3. **The layer gap:** records → background → quantum fields → atomic
   structure is at least **three constructed layers, NONE of them built.**
4. **Both readings of every line identification fail:** LITERAL is refuted
   by (1); EFFECTIVE is the only defensible one and has **no
   coarse-graining theorem and no intervening layer** to pass through.

**Then re-founded on firmer ground (2026-07-25, #415, §B1.2):** the
blocker now stands **on LOSS rather than on impossibility**.  A single-line
description of a composite **exists causally**, so the effective reading is
not impossible — but it discards most of the causal structure, so a bound
extracted through it is a bound on the **coarse world**.

**Survived / disposition:** a new item **(0) THE COARSE-GRAINING**,
logically **prior** to the four things a bridge must fix, added and left
**EMPTY**; §§2–3 stamped `[BLOCKED ON §1A]` with their eight
correspondences retained **UNCHANGED as the criticizable record**; §4
`[SUPERSEDED]`; §7 **SEALED, NOT PRESENTED FOR SIGNATURE**, with a ninth
unchecked box.  §1A's own reading: *the laboratory programme is **premature
by at least one constructed layer.*** And the reason blocking beats the
alternative handling (retain as phenomenological ansätze): that handling
needs a label carried at **every** citation, and the corpus's record on
carrying such labels is the d41a error — **blocking is cheaper and cannot
decay.**

`[MY READING]` The practical upshot for anyone looking for a prediction:
**a theory that has not chosen its measure cannot produce a rate.**  The
completion problem is upstream of every empirical claim.

### B10.8 "Infinite clocks, as a theorem via Sperner" `[D54, LOG #428 → #429]`

**Claimed:** the Dilworth gate derives the infinite-clocks doctrine,
because a sphere-like sky shatters at every `m`.
**Killed by:** BLOCKER 1 — **the antecedent is satisfied by no 2-sphere
sky**; caps on `S²` have VC dimension 4 and never shatter 5, certified by
an exact Radon partition `λ = (−23/49, −19/49, −24/49, 17/49, 1)` with
`conv{3,4} ∩ conv{0,1,2} ≠ ∅`; an independent grid search finds 30/32
traces missing exactly that pair.
**Survived:** the conclusion, by **trace counting** with no shattering in
the derivation (`Θ(n³)` traces against `n+1` per actor chain ⟹
`actors ≥ Θ(n²)`); plus the sharpening that **width prices sky size, not
dimension** (a circle also costs unboundedly many actors: `n² − n + 2`
traces ⟹ `≥ n − 2` actors), the dimensional signal being the **shatter
offset** 3 / 6 / 10; and the promotion of the shatter ladder to a
**dimension meter**, which is what made D55 worth running.

### B10.9 "The construction saturates the theorem" `[D54 round 1, MINOR 5]`

**Claimed:** the 20-actor record saturates the `C(4,2) = 6` bound.
**Killed by:** the realized 16-trace **family's** minimum chain cover is
**exactly 6** — so the family is Dilworth-**tight** and the 6-vs-20 gap is
**architectural** (the scheduling cost of backflow), not saturation.
**Survived:** the tightness result, sharper than the claim it replaced,
plus a clean decidable open problem (does backflow force **more** than 6,
or can scheduling reach 6?).

### B10.10 "The admissibility layer does not select 3+1" `[D55, LOG #431 → #433]`

**Claimed:** because the layer admits a sky beyond `S²`.
**Killed by:** BLOCKER 1 — it needs *"not cap-realizable on `S²` ⟹ not a
3+1 sky"*, i.e. the stipulation that discrete 3+1 skies are cap systems —
**the premise class the demotion refutes**, and the same arrow D54's round
had retired one rung down **one day earlier**.
**Survived:** the licensed **capacity** claim (the layer does not **cap**
the shatter ladder at the sphere's rung); the widening of "selection lives
in the measure" to **three** candidate homes; and a named residue (a
full-strength `M^{3+1}` control, the present one being **thin**: 1,351
skies, 33 capable, zero shatter-5).

### B10.10b The empty-trace necessity theorem, and the zero it produced `[D53/D55c as first delivered; both corrected in batch round 1]`

**Claimed:** (i) shattering requires an **empty** trace, so the two
cover-based sky readings can never shatter at any width or depth; and
(ii) downstream of that, genuine `M^{3+1}` records never shatter 4, so
max-shatter reads coordination rather than geometry.
**Killed by:** a one-line counterexample to the lemma it rested on, and
then a measurement.  Shattering `S` needs a row **disjoint from `S`**,
not an empty row (§B5.4), so the two readings excluded as structurally
incapable are live — and with the blinder removed and the density raised,
genuine `M^{3+1}` **does** shatter 4 (0/1/11/30/116/211 across a matched
`N = 150…500` ladder) while `M^{2+1}` never does, size-controlled, with
neither reaching 5 (§B5.7).  The zero that had looked structural was a
**sparse sample read through a blind reading**; and "no sprinkled record
shatters at all" was false on the unit's own data, where shatter-3 fires
1,087 times in 2,151 capable strata.
**Survived, and improved:** in place of the retired negative there is a
**working two-sided dimension discriminator** on sprinklings; the
calibration ladder as an exact continuum statement; the **Dilworth
gate**; the **trace-counting** bound; and the whole capacity result of
§B8.  Also survived: the *discipline* the false theorem was wrapped
around — capacity must be gated before a zero is read as a negative —
with the corrected census (144 of 415 genuinely capable, 2.8×) replacing
the over-strong one.

### B10.10c The sector-exact escape at `(actor, type)` granularity `[D57, LOG #436; batch-round reviewed and repaired]`

**Claimed:** §B9.1's no-go bites per-option descriptions only, since the
delivery-sector total is exactly `1/4` at every rung; so a **sector-exact**
abstraction should stay bounded.
**Killed by:** one ground (§B9.4b): **the coarsest sector-lumpable
partition does not stabilize** — per-depth fixpoint counts creep across
caps 3/4/5/6 (depth 3: 7, 16, 16, **17**), with a trivial-boundary
control showing the counts are *lower bounds*.
*Nearly killed by a second ground that did not hold up.*  Sector
quantization at `{0, 1/4}` does die — arbitration sectors reach `1/2` via
subset choices and `1/8` at cap 6 — but the inference from three values
to unboundedly many fails at this scope: `max |comps| = 1` at every
depth in the unit's own exhaustive data and `merge_pairs ≤ 1` is proven
at two actors, so `{1/2, 1/4, 1/8}` **may be the complete alphabet**.
That ground is **withdrawn**; the `1/4` remains a fact about the
*delivery* sector rather than a law of sectors.
**Survived:** the motivating result — that record-level demands constrain
**sums**, so the physically meaningful objects are the aggregated ones
(§B6.12) — and a narrowed crack: **strictly coarser** aggregations
(type-only, total-budget only) and abstractions that give up exactness for
the completion's **observable** demands.  Both untested.

### B10.11 The two D49 uniqueness claims `[LOG #418 → #419/#420]`

**Claimed (i):** "229 of the 313 boundary dimensions act **trivially** on
the completion; 313 is a **wrong** count of completions."
**Killed by:** BLOCKER B1's perturbation witness, then upgraded by #420
from witness to **theorem** — every nonzero kernel direction changes some
depth-3 transfer, because a depth-3 transfer reads the boundary directly.
**Paper 30 §5.3's 313 stands; the queued erratum was cancelled before it
was applied.**
**Survived:** the real statement — the boundary → interior-**potential**
map has rank exactly **84** (= the number of depth-3 cut classes), so
shallow transfers see the boundary only through an 84-dimensional image
while the depth-3 layer sees all 313; and inside the 84 the
depth-stationary completions form a **single ray** realized by
`b*(t) = 2^(−4) f(class(t))`.

**Claimed (ii):** "Among completions that do not distinguish record points
the law identifies, there is exactly one, and it needs no boundary."
**Killed by:** BLOCKER B2's measurement — renewal-pair agreement leaves
**308/313** free; bisimulation-invariance leaves **137/313**.
**Survived:** the **existence** result entirely untouched (horn (II)
holds), plus the honest replacement: uniqueness comes from **the form**,
and D50 then showed the form is a **choice**.

### B10.12 D50's own pre-registered expectation `[LOG #421 → #422]`

**Claimed (pre-registered, with its argument, before running):**
depth-stationarity forces the form.
**Killed by:** the falsifier — completion dimensions **12, 32, 125**,
growing, and now **constructively**: an exact positive line of distinct
completions satisfying the demand is exhibited.  Plus the diagnosis: the record-level demand is **aggregated**, so
it constrains sums and never obtains the sketch's hypothesis, and *the
aggregated reading is the correct one*.
**Survived:** a **permanent** restriction on every citation of D49; the
measured fact that **foliation-invariance adds nothing**; and the sharp
successor question — *is there any record-level demand that forces the
form?* — with the two strongest candidates and their conjunction now
eliminated.

### B10.13 "The atlas carries a `Z/2` gauge structure" `[D64, LOG #464 → #466]`

**Claimed (green-unreviewed):** the wide crystal's overlapping charts
carry non-identity transitions that satisfy the cocycle and close to
`Z/2 = ⟨τ⟩`, so the atlas carries a genuine gauge structure — and the
inter-ring coupling changed *which* involution it carries.
**Killed by:** a computation the unit never ran, supplied by the round.
The `Z/2`-valued transition cochain is a **COBOUNDARY**: an explicit
per-chart port choice `ε` (32 charts at 0, 28 at 1) turns **all 108**
non-identity length-preserving transitions into identities — 165 of 172
pairs identity, 0 obstructions over 60 charts in 9 components, the Čech
lift clean on 108 triples, and the same at REGA.  **`H¹ = 0`; there is no
structure group to be small.**  Two supporting claims fell with it: the
group **name** was undetermined by the data (0 of 108 transitions
uniquely `τ`; an incomparable `Z/4` passes the same triples; 10 of the 30
subgroups of `S₄` are consistent), and the substrate-versus-control
involution contrast is a **REG-convention** observation that dies at REGA
and COV, is width-confounded, rests on 41 pairs of 126, and describes
controls whose overlap graphs are **perfect matchings** — no composition,
no triples, no closure content at all.  Also corrected: the identity
fraction is exact chart **duplication** (172/172 biconditional), not a
trivializable part; and the pin's coupled-wire lean is **untested**, the
27 both-coupled pairs being exactly the 27 that carry no single-valued
correspondence.
**Survived:** the **instrument** — a transition detector with the
triviality gate it was missing (now C7, both routes, self-verifying on
every rerun), PROBE 2's refusal to read the outcome at a labeling that
forces it, and a validated reading of `event_poset`'s own generating
relation.  And the sharpened successor question: **can any substrate
carry a transition class that is NOT a coboundary?** — with a stated
structural reason to attack the arbitration crystal, since what makes `ε`
available is a two-port symmetry a conflict event does not have (§B8.8).
*That attack has since run and returned zero at all five port conventions
and by all three routes* (§B8.9), so the successor question survives its
own best candidate site and has no named next one.

### B10.14 "The completions are PRECISELY what repairs descent" `[D65, LOG #467 → #468]`

**Claimed (green-unreviewed):** the completions the dichotomy line forced
are exactly the objects that repair the generated law's descent defect —
*the two lines meet*.
**Killed by:** the repair-space computation, again supplied by the round.
At the depth-4 truncation the positive repair cone has dimension **573**
(at `D = 5`, 3,053) against the `(depth, sigma)` family's **28**; the
completions that also **descend** are **205**; and two exact strictly
positive witnesses show the implication fails in *both* directions — one
repairs all 403 commuting squares while its measure splits two record
classes, one is a genuine record-cylinder measure that breaks
`sigma`-commuting squares.  **The hierarchy is `573 ⊃ 205 ⊃ 28 ⊃ 1`, and
the collapse to one ray is D50's form choice, not descent.**  Corrected
in the same round: the load-bearing census is the **refined** sub-census
(**32,256 of 425,334**, since paper 29 §3.1 exempts the wider class, and
a genuine record measure fails that wider test too), and D59's
boundary-state item does **not** move — the generated line's derived
`sigma` statistic is stated *beside* the ledger, not on it.
**Survived:** everything measured — the defect is exactly one mass-ratio
coboundary, `sigma`-functional, zero exceptions, exhaustively over the
whole family — plus two facts the round *added* in the unit's favour and
which are now gated: the raw path weight is constant on all **5,548**
record classes, and **`Zhat`'s measure genuinely descends**, the
strongest descent-side fact the corpus owns.  And the honest replacement:
*the descent defect names the JOB the completions do; it does not single
them out* (§B2.10).

### B10.15 "`max |D| = 2k`" and "the delivery is the crystal's second direction" `[D66, LOG #471 → #472]`

**Claimed (green-unreviewed), first:** *"`max |D| = 2k` at `d = 2` for a
`k`-proposer crystal"* — printed as a law about `k`-proposer crystals with
a mechanism attached (*"each proposer contributes one direction per wire
of its next delivery"*), on the strength of `CONFLICT-GRID(3, ·)` at 6 and
`CONFLICT-GRID(4, 4)` at 8.
**Claimed, second:** *"the delivery is not a tax on the conflict engine;
it is what gives the crystal a second direction"* — and, with it, *"the
schedule that maximises the conflict share is the one that cannot tile
widely"*, on the strength of the `sticky = 0` ring, which is
delivery-free, saturates the conflict share at `1/3`, and collapses to
`max |D| = 2` with homogeneity below band.
**Killed by:** two constructions the round built after reproducing every
published figure of both.  `2k` is a property of the swept **schedules**,
not of `k`: it is the value of the bound when every depth-1 successor of
an arbitration is a two-register **delivery** (`b(y) = 2`), which the
RING/GRID blueprints impose and the grammar does not force — an
arbitration's proposer register may be consumed by **another
arbitration**, since `prop_options_in_view` blocks only a second live
proposal on the *same* base.  The true ceiling is W4c's own `k·Bl ≤ k²`,
and it is **saturated**: `DOUBLE-GRID(3, R)` — rows and columns
conflicting concurrently — carries **nine `|D| = 9` charts** with
successor out-degrees `[3,3,3]`, and the `ARBCHAIN(m, 3)` family occupies
the whole interval `6, 7, 8, 9` as `m` runs `0..3`.  The same object kills
the second claim: it has **zero in-round deliveries**, saturates the
conflict-group share at `1/(k+1) = 1/4`, is the **widest** record in the
unit, and sits **inside the `d = 3` sprinkling homogeneity band** at
0.7833 (its second `d = 3` column is below).  The
`sticky = 0` collapse is the **pair-ring diamond** — one live conflict
lineage per actor makes the propose/propose/arbitrate cycle fan out and
straight back in, so the depth-2 layer is a single event — and has nothing
to do with delivery-freedom.
**Survived:** every number, and the unit's substantive results untouched —
conflict tiles at C1 grade with zero refusals over 2,325 events; the
conflict budget bound `≤ 1/(k+1)` with both readings printed; **W4c**, now
carrying a four-line structural proof quoted against the committed
`d42b1` (payload-vs-register; a recurring `vname` forces causal
comparability, hence refusal) rather than a per-record census; and the
trivial transition class at all five port conventions.  And the
replacement mechanism sentence, which is stronger than the one it
replaces: **the second direction is a second CONCURRENT CONFLICT AXIS** —
rotation buys that consumer with a delivery, concurrency buys it for free,
and a concurrent arbitration is the better consumer (`b = k` against
`b = 2`); transport seeds and rotates, it does not make space (§B8.9).

### B10.15b "No whole `k = 4` record is in band" and "`k²` is unrealized at `k = 5`" `[D67, LOG #475 → #476]`

**Claimed (green-unreviewed), first:** *"Uniformity is the price: no
**whole** `k = 4` record is in band at either depth, though the interior
of `DOUBLE-GRID(4, 2)` is"* — with a FRONTIER box saying that at `k = 4`
width 16 and `d = 3` band membership compose **only on the interior**, and
a receipt gate recording the pin's honest lean as CONFIRMED for whole
records.
**Claimed, second:** *"the ceiling is not reached at `k = 5` by anything
built here"*, `k²` REALIZED at `k = 3, 4` and UNREALIZED at `k = 5`, with
D66's residue 6 **re-opened**.
**Claimed, third:** *"the first sprinkling-grade width in the campaign"*,
as a milestone about the mechanism.
**Killed by:** the unit's own sweep table, one build later, and by one
levelling pass.  The sweep stopped at `R = 3` and printed the trend that
refutes its own conclusion in the same sentence — `d = 3` homogeneity
`0.4625 → 0.5417 → 0.6562` against a floor of `0.6833`, a **monotone
sequence one step below the floor with growing increments** (`+0.0792`,
`+0.1145`).  `DOUBLE-GRID(4, 4)`, the same blueprint with one more round:
200 events, forced, zero in-round deliveries, `max |D| = 16`, `d = 3`
homogeneity `29/40 = 0.7250` **inside** `[41/60, 49/60]` and `|D| ≥ 4`
`0.6350` **inside** `[3/5, 91/120]` — in band **as a whole record and on
both columns**, which is more than the `k = 3` flagship achieves.  In unreduced form the
sequence reads `37/80, 65/120, 105/160, 145/200`, and the trend continued
exactly.  The `k = 5` wall went
the same way: the unit diagnosed the cause correctly — height alignment —
and then filed it as a residue instead of removing it, when the cause is
entirely inside `ARBCHAIN*`'s own bootstrap ordering and one pass of the
grammar's own `('n', a)` idle removes it; `ARBCHAIN**` realizes `k²` at
`k = 3, 4, 5, 6`, and its `k = 5` member is **C1-complete** at 157/157,
widest full menu 2,125 — a higher forcedness grade than any DOUBLE-GRID
record.  **D66's residue 6 stays CLOSED and is not reopened.**  The third
claim overstates a one-column, one-`k` measurement: `[10, 17]` is the hull
of `M21 [10, 11]` and `M31 [14, 17]`, `max` is the only column on which
the record touches the population, and the same mechanism gives 25 and 36
above the whole hull — so 16 is a parameter picked, not a coincidence
discovered.
**Survived:** every published figure — an independent rebuild reproduced
all 554 lines of the receipt byte for byte after normalising timings,
confirmed the `|D| = 16` witness event by event against the committed
`sky` and the committed `event_poset`, and confirmed W4c, the anchors, the
unfilled-successor census, both interleaved controls, the V2 refusal to
the index and the ARBCHAIN correction to D66.  **The arithmetic was
completely sound; what failed was the sentence.**  And the replacement is
the stronger statement: **the width-uniformity frontier at `k = 4` does
not exist**, band membership is a **crossing** of a monotone family read
at a round number, and the `k`-ceiling question is **closed at every `k`
tried** with height-levelling as the mechanism (§B8.9).  Three accounting
sentences went with them, each replaced by a printed number: *"1,040
events, C1-graded"* (the C1 grade covers **380 steps of 1,380**, on five
records, four complete); *"the budget bound SATURATED"* (the record's own
bound is `1/2`, `1/5` is `1/(k_conflict + 1)`, and the conflict share is
`2/15`); and *"three charts of width 16"* (three **bases**, one direction
set).

### B10.15c "The record instrument is the exact boundary of permitted coherence" and "records cannot see a phase" `[D68, LOG #479 → #480]`

**Claimed (green-unreviewed), first:** *"under the only reading that
bites, coherence survives **exactly** between histories whose parents were
already record-identical — killed everywhere else by a **singleton**
cylinder-consistency row"*; *"the record instrument reaches back one step
and decoheres precisely what it could already tell apart at the previous
cut"*; *"the record instrument is the exact boundary of permitted
coherence"*; *"F-II fires at depth 2, and only there"*; *"the record
instrument is part of the click law, and here it is the only thing that
removes a phase"*.
**Claimed, second:** *"a record measure of that shape **cannot see a
phase**, so no amount of C1/C3 could ever select one"*, with a licensed
claim that *"the record demands are blind to the imaginary part"*.
**Claimed, third:** the reach — *"**the generated law** admits a
paper-29-shaped functional level"*, *"the space of functionals **over the
generated law**"*.
**Killed by:** three computations the round ran after reproducing **every
published figure** of the unit and its receipt — the censuses, the 36
states, the `λ = 2` spectrum, `μ_Ẑ`'s descent, the entire 32-row
dimension table including every antisymmetric column and the full-chain
split, the geography counts, the pinned witness to its `5183/67108864`
minor, all five control responses, and 25 PASS / 0 FAIL under three hash
seeds — from its own enumerator, its own `σ` normal form, its own
constraint rows and an elimination pivoting the other way.  **(1)**
Neither of the unit's two C1 readings is paper 29 §4.3's condition: the
**sum** reading never asks the algebra to decohere, and the **block**
reading forbids cancellation entry-by-entry at the *fine* level, which is
strictly stronger than `D̄(r,r') = 0` and forbids by hand exactly what
coarse decoherence permits.  Under the faithful condition **nothing is
forced at any depth**, `cohdim = coh` in every variant, the depth-2 F-II
cell evaporates (`9/9` free, not `0/9`), and an exact PSD member carries
coherence between two histories whose **parents carry different
records** — the entries the headline called killed by a singleton row
(`t = 1/81920`, zero residual against all 3,846 rows).  **(2)** The phase
zero is a **shape tautology**: every sum-reading row is a sum over a
product set, hence swap-symmetric, hence annihilates the antisymmetric
part — for any partition, any measure, any layer, with nothing computed
(gated over a mod-7 partition with a second measure).  Under the faithful
reading the antisymmetric constraint rank is **268** at depth 2 and
**3,739** at depth 3, and C2 bounds `|A_ij|²` by `D_ii D_jj − S_ij²`.
**(3)** The measure appears **only on the right-hand side**: the
coefficient matrix is identical entry for entry under a second,
non-record-constant weight, so the whole table is a fact about `canon`
and the prefix map, true of *every* strictly positive cut-consistent
weight on this layer.  Two further scope corrections went with them: the
`cohdim` identity holds **only** for one-step C3 (full-chain gives
`cohdim` 41 against 50 pinned coordinates at depth 3, and 651 against 744
at depth 4 — cancellations among free coherences, which the "no
conspiracy" story denies), and **no** within-class pair agrees on its
whole ancestor record chain at any depth, so the filtration reading of
the slogan is false outright.
**Survived:** every number, and more of the unit than usual — F-I and
F-IV remain excluded, the classical member is positive definite and
interior in all three readings, the block reading's singleton mechanism
is real *within its convention*, and the faithful reading turns out to be
the only one of the three whose **dimension** is informative at all (rank
296 of 528 at depth 2, against the sum reading's 29).  **And the round's
unasked computation is the better result, twice over:** *consistency does
not structure coherence*, and the **first fair dynamical demand
eliminates it** — `cohdim = 0` at every depth tried, with the
permitted/forbidden split invisible to the closed law's state space
(15/15, 28/28, 32/32 σ-state pairs carrying both kinds).  The corrected
verdict is sharper than the claim it replaced: **at closed scope a
quantum layer cannot be both state-generated and coherent**, and where
superposition enters is the programme's sharpest open question (§B2.11).

### B10.15d "The generated line is flat" `[D72, LOG #488 → #490]`

**Claimed (green-unreviewed):** *"THE GENERATED LINE AT CLOSED SCOPE IS
FLAT — no holonomy exists for the phase to be"*, extended in the same
delivery to *"the generated line is flat"* without the grammar, and to
*"no other section of the phase bundle is reachable by transport"* as a
statement about the process's own kernel; with `F4` recorded as *"not
reached, vacuously"* and a licensed clause asserting d42b1 flatness as
`[MEASURED]`.
**Killed by:** a round that reproduced the arithmetic in full from an
independent rebuild — 6,471 histories with the identical per-depth
profile, 1,565 classes, the deletion graph `V = 1565, E = 2322, C = 1,
rank = 758`, and `2·exp(−3/32)` to all 32 published digits — and then, in
its own words, *"broke the scope, the instrument and the second
grammar."*  **(1)** The d42b1 clause was `[MEASURED]` and **never
measured**; measured, it is **false**: `88` of `1,546` closed exchange
squares carry `dP_AB/dP_BA ∈ {1/2, 2/3, 3/2, 2}` with `40` further
half-open at `±∞`, `12` more at three actors, **all delivery-bearing**,
shallowest at total depth 3.  **(2)** The flatness is **raw-weight
specific**: the normalised kernel `q/M` on the *same* record graph has
holonomy image `⟨5/4⟩ ⊂ R₊` — §B2.10's own mass-ratio coboundary, uncited
in the delivery — so **`F4` FIRES** on two independent objects.  **(3)**
The record-graph census is **blind by construction**: a square closes at
record level exactly when its events are register-disjoint, so the
locality argument and the loop census share a domain and a blind spot,
`0` of `88` defects are visible to either, and the negative control — a
perturbed edge of an exact gradient — **cannot fail** and cannot detect
that class of blindness.  **(4)** The depth-free argument the delivery
sketched covers 61 % of its own squares; the round **closed the proof**
and re-sited the finding, and its last two lemmas are a
**grammar-specific budget coincidence**.  **(5)** The `k = 5` cell —
v7's own five-record type, 2 s of compute — **reverses** the delivery's
proudest self-correction: type-level one-sidedness is `0/1` at `k = 3`
but **`4/4` at `k = 5`**.
**Survived:** every number; the identification leg of the weld; the
carrier construction; the `L_dual` port with its adversarial control; the
`1.82` closed form; the determinism repair; and the pre-registration.
**And the round returned more than it removed, twice:** the closed-scope
statement is now a **`[THEOREM]`** with its scope clause, and **transport
scope is CURVED** — with `2/3` and `3/2` lying **outside** `⟨5/4⟩`, so the
transport holonomy is a **new object** and not the known coboundary in
new clothes.  The graveyard's clearest case of a sentence dying of being
**too wide** (§B2.12, §0.3).

### B10.15e "The direction index is the stage" — and an anchor on a falsified fixture `[D73, LOG #488 → #491]`

**Claimed (green-unreviewed), first:** *"the rank-2 object's stage is the
DIRECTION INDEX of the generated line's wide charts, not v7's channel
index"* — 59 wide charts on `DOUBLE-RING(8,10,8)` all carrying
anisotropic `4×4` circulant Grams with stabiliser 8, offered as the
promising lead.
**Claimed, second:** *"the trace already sits at the family's floor"* —
eleven quadratic promotions of `K(E)` all landing on
`1.67603622405300634803560e-5`, presented as a ceiling result, with the
supporting **monotonicity of `TV_9` under refinement** asserted in prose
and never proved, and the whole thing labelled `[THEOREM at the fixture]`.
**Claimed, third:** that `F1` is refuted *as a biconditional*.
**Killed by:** a round whose author found the BLOCKER by **reading 130
lines further down a paper the unit had already opened**.  **(1)** The
three dual pairs everything was computed on are the ones paper 30 `§26.2`
audits, ranks **11th**, and declares falsified; `1.676e-5` is the loser's
printed score, and the residual it names is a **sector-selection
artefact** no function of the even 3-vector can reach.  `pair_values`,
`colors_for_mode` and `weights_by_mode` all take `pairs` as an argument
precisely so this can be varied — and the unit lifted all three and then
hard-coded `DUAL_PAIRS` at every call site.  **"Nothing moved" was
fixture-guaranteed.**  **(2)** The eleven rows are **two** colourings
(9 + 2), by canonical relabelling; the monotonicity premise is
contradicted by the committed table itself (`agg_linf` has **fewer** atoms
than `agg_l1` and a **better** `TV_9`); the real mechanism is the
**`h`-weight identity**, gated as a biconditional at 18 candidates over
two fixtures.  `[THEOREM at the fixture]` **removed**.  **(3)** `F1` as
pinned is an **implication**; the unit attributed the **converse** to it,
found the converse false, and reported the pin refuted — *a pin frozen
before the code is the one document a unit may not rewrite.*
`[RETRACTED]`  **(4)** The transfer hint **inverts on the unit's own
evidence**: 59 charts are **two** matrices with degenerate spectra, one
block-decomposable; every `DOUBLE-RING` is 100 % stabiliser-8 because a
double ring is *built* with cyclic symmetry; `wide_brick(8,14,2)` breaks
it at 5 of 12; and the narrow control the unit built and never measured
has **4 of 42 charts exactly `(1/4)I`** — `F1`'s literal antecedent firing
on the v10 side.  A large stabiliser is **fewer** free components, and the
receipt's own `F1`-instrument control is a `7I` with the full stabiliser.
**Survived:** every anchor, character for character — the record census,
the seven committed even principal minors, the `i`-twisted minors, the
`§25.3` rows to 24 digits.  **And the replacement is the better object:**
on the fixture paper 30 actually **selects**, where the floor is `0`
exactly and a wrong `K` is visibly punished, the even Gram is **more**
anisotropic (`0.511428` against `0.395835`) with a **trivial stabiliser** —
the genuine rank-2 candidate — while the corrected verdict, *a scalar did
not become a metric by interpretation; it became a covariance matrix*, is
sharper than the one it replaced and leaves `FAILS-FULL-GR` standing
(§B8.10).

### B10.16 Instrument and control failures, itemized

- **TG5's null "cross-actor causation produces the sky"** `[D47 round 1,
  MAJOR R1]` — the null's actor extraction returned the **event type** on
  100% of 720 sampled events, and **no** disjoint-union-of-chains null
  could ever have failed (max sky 1 by construction).  Rebuilt honestly,
  the comparison **reversed**: null 7 directions / 362 decidable triples
  vs transport's 4.  **Transport skies are narrower than chance.**
- **SG10's capacity law** `[D47 round 1, MAJOR R2]` — box extent scaled
  with `N`, confounding count with density; "decidable at `N ≈ 40`"
  withdrawn as stated.
- **D47's SG2 capacity gate** `[D53]` — necessary and not sufficient; 415
  of 554 "decidable" pairs were structurally incapable, so a zero over
    them is a **tautology**.  The corrected condition — four directions and
  sixteen distinct traces — replaces it, and the empty-trace clause is
  **not** part of it (§B5.4).
- **"Width spreads with depth under the theory's own law"** `[D46d]` —
  near-tautology, withdrawn by name; and "the theory's own law" itself
  withdrawn as two different normalizations wearing one name.
- **"All 7,163 co-receivable pairs commute — an abelian monoid"**
  `[D46f]` — true, structural (the committed `View` builds every field
  from a **down-closed** index set, so order-independence is
  **definitional**), not discovered here; withdrawn as a delivered
  finding.  A demonstrably wrong action map still leaves the gate at zero,
  and ACT commutes on **all 170,820** pairs, not just the 7,163.  Also
  withdrawn: "D44f's order-dependence lives in the menus, not the state" —
  the gates do not license the inference (two different notions of order).
- **"The failure is grain, not interaction"** `[D46e]` — reversed once the
  channel family was closed under products of its own labels: **16**
  discriminating pairs collapse at `g = 0` only (the interaction kills the
  ray), **9** at neither.  Two further blockers in the same round: the
  verdict was a **hard-coded string literal** (surviving three mutants
  while its own census contradicted it), and **nothing anchored** the
  interacting identification to the corpus first moment (deleting the
  weight passed 19/19 at exit 0).
- **D52's "no state ever recurs"** `[#425 → #432]` — backwards;
  recurrence is **total** (idle padding), and only the NEW column informs.
- **D60's C5 clause "at `d = 3` the brick's `|D| ≥ 4` sits inside the
  `d = 3` sprinkling band"** `[forward-corrected at D63 round 1]` — false:
  `38/65 = 0.5846` is **below** the floor `0.6000`.  The successor unit's
  own output had printed the contradiction and its prose had not read it.
  Corrected at the parent (§B8.6), which is what "forward corrections
  only" means when the error is in a committed clause rather than in a
  number.
- **D63's first-draft novelty sentence** — *"the brick's `|D| ≥ 4` is 0 at
  every parameter"* carried **no depth label**, and at `d = 3` eleven
  configurations meet the pattern, four of them with zero coupling.  The
  finding is real and is a `d = 2` finding; every headline now says so and
  the census is gated at both depths (§B8.7).
- **D48's CG6 non-surjectivity assertion** — asserted, **failed at exit
  1**, withdrawn; coarse-graining is surjective.
- **Three register-theoretic bridges** `[D44c-P]` — T1 falsified as
  pre-registered (23,016 classes), L3 falsified (23,844), L1 falsified
  (16,842 of 42,144).  Each reported at exit 0 as a **deliverable**, so
  that nobody walks them again.  And a **triple coincidence explained
  rather than shipped**: three independent predicates each returned
  exactly 23,844 — an instrument smell — and it was gated and accounted
  for (all 23,844 violating pairs are purely transitive, zero cover pairs,
  all non-arb-headed).
- **Receipt-level own defects, recorded not hidden:** D49's `frozenset`
  repr determinism defect (7 spurious mismatches at
  `PYTHONHASHSEED=7`, exit 1); D50's run 1 **exiting 0 having run no
  gates**; D44c-P's run-1 unsound dedup key (caught by its own resample
  gate at 2,398 mismatches in 11,664) and its FG8 exit-discipline gate
  that failed precisely **when the falsification discipline was working**;
  D55's silently-capped per-depth table; and the AST scanners that
  **advertised more coverage than they enforced**, promoted to a
  corpus-level obligation after recurring for three rounds.
- **Gate counts that overstate their own evidence** — the recurring
  defect, now caught in three separate receipts.  D49 led with "25 PASS"
  where five gates were theorem-passes; D62's receipt carried **three of
  twenty-four gates that could not fail** (two corollaries of its own
  headline gate, one tautological counter) and a falsifiability sentence
  claiming each mutant fails exactly one gate, which is false for its six
  row mutants.  Repaired by rebuilding the classifier independently and
  publishing an **independent-evidence map** naming which gates can
  genuinely fail (§B6.13b).  *"24 PASS" is not 24 pieces of evidence, and
  the receipt now says so itself.*

### B10.17 The pattern, stated as a statistic

- **Almost every headline correction hit an interpretation sentence, not a
  computation.**  Thirteen independent-model rounds have run (D54, D55,
  D61, D62, D63, D64, D65, D66, D67, D68, D70, D72, D73); **nine** returned
  a BLOCKER and **every one of the nine was in the interpretation layer,
  none in the arithmetic**.  In D54
  and D55 the verdicts were 1 BLOCKER / 2 MAJOR / 8 MINOR / 3 NIT
  **each**, and in D55 everything computational survived including a full
  independent rebuild of a 42-actor, 84-event record that came out
  **identical and forced**.  D64 through D73 are the same failure eight
  times: the referee reproduced *every* number and then ran —
  or built — the one thing the unit had not thought of: the coboundary
  test (§B8.8), the repair-cone dimension (§B2.10), the DOUBLE GRID and
  then **one more round of it** (§B8.9), the parent paper's own
  decoherence condition plus the dynamical demand the unit's own residue
  had named and declined (§B2.11), **the four-actor depth-4 arm the unit
  had named, priced and skipped** (§B9.7), **the second grammar's
  transport census and the normalised kernel** (§B2.12), and **the
  provenance of the unit's own fixture** (§B8.10) — and each refuted the
  headline built on the numbers it had just confirmed.  **A
  verified computation is not a verified claim**, and the corpus's
  standing lesson is to ask what computation would
  *distinguish* the headline from its trivial alternative, before writing
  the headline.  The recent ones also show the upside of that discipline:
  D66's refutation arrived with a
  **better object** attached; D67's killed a **negative** the unit had
  announced — a frontier that did not exist and a ceiling that was
  reached — so the corrected claim is the strongest geometry statement the
  programme has; D68's inverted **both** headline sentences of a unit
  and returned the programme's first hard fact about its own quantum layer
  together with its sharpest open question; D70's ran the deciding
  computation and turned a published negative into the measure route's
  positive; D72's **closed a proof the unit had only sketched** and, in
  the same pass, discovered the transport curvature the unit's headline
  had denied; and D73's re-anchored a whole unit onto the fixture its
  source paper actually selects.  **A unit can be wrong
  pessimistically, and the round that catches it returns more than it
  removes.**
- **Two of the three most recent rounds reversed a headline without
  raising a BLOCKER at all** (D70 and D72 were both `REVISE` on MAJORs).
  The blocker count has stopped being the informative statistic;
  what is informative is that **referees now routinely out-build the
  units** — supplying a theorem (D72's L1–L6), a census the unit's
  instrument was structurally blind to (D72's T6), the computation a unit
  had declined (D70's four-actor arm), and a control a unit had built and
  never read (D73's narrow charts).  This book therefore credits
  round-supplied results as **authorship**, gated like any other number in
  the receipt that carries them, and does not narrate them as a correction
  log.
- **D68 names a distinct failure mode: a CONVENTION wearing the
  clothes of a result.**  Both withdrawn sentences were true of *how the
  unit chose to write its own equations* — one convention forbidding
  cancellation by hand, one row shape symmetric by construction — and
  false of the object under study.  No control would have caught either;
  what caught them was writing the parent paper's demand as the parent
  paper states it.  The obligation this adds is cheap and specific:
  **when a demand is quoted from a source, gate the quotation.**
- **D73 names a fourth: FIXTURE PROVENANCE.**  A unit can be
  arithmetically flawless and still be computing on an example its own
  source paper audits and falsifies a few sections later — in which case
  its central negative is *guaranteed by the fixture* and carries no
  information.  The obligation is now standing and is as cheap as the
  last: **anchor on a paper's own selection, and read what the paper says
  about its own tables afterwards.**  A companion rule from the same
  round: **measure your controls.**  D73 built a comparator, computed its
  Grams and reported only how many there were — so it controlled nothing,
  and the measurement, when taken, fired the unit's own death condition.
- **And one round in this line survived as written.**  D62's cover
  sentence went into an independent round that rebuilt all five update
  rows from the prose alone, swept 4,778,310 transitions two depths past
  the receipt, and returned **zero mismatches and 0 BLOCKER** (§B6.13b).
  The statistic above is not "reviews always find something".
- **Pre-registration is doing real work.**  D55's pin records that **five
  of seven pre-registrations in that campaign were corrected**.  D46's
  three-round sweep produced **five headline reversals** across six units.
  D50's pre-registered expectation was refuted by its own falsifier.
- **The blacklist is empirical.**  Every forbidden sentence in §0.3 is
  forbidden because it was written, believed, and then refuted.

---

## B11. Status, open problems, method

*Non-technical twin: Part A, chapter A11.*
*The **ranked residues of §B11.4 are re-ranked against the destination in
§D4**, which supersedes their ordering (not their content).*

### B11.1 The two lines, scoped

**Measure line — d42a, delivery-free, two actors.**
`Zhat(h) = 2^(−|h|) f(class(sigma(h)))` with `λ = 2`,
`f = (4,4,3,7,3,3)/3` is a completion in the sense of paper 30 §5.2:
positive, per-cut normalized, class-constant, foliation-invariant
directly, support-preserving, a law, a measure, and **root-free** (root and
renewal both `1/16`; the whole 215-node matched subtree identical).
**Horn (II) holds, and RESIDUE 1 IS CLOSED AT THAT SCOPE**: (H0) is
fully discharged and (H1) is a theorem (§B6.13), (H2) is a theorem
(§B6.13b), so D44a's closure is **unconditional** at two-actor
delivery-free d42a scope and `Zhat` holds at every depth there.  Still
**unique only within paper 30 §5.7's stationary FORM, and the form is a
CHOICE** (§B6.12); values **toy-relative**; **three actors out of scope**
— the own-view dichotomy fails there; both proofs prose-over-code, with
Lean-grade mechanization the line's one residue.  **Transport scope
OPEN**, and §B9 shows *this* tool cannot travel.  Two facts are added from
the descent side (§B2.10): `μ_Zhat` is **constant on all 5,548 record
classes**, so the settled completion's measure genuinely descends; and
the *uncompleted* normalized kernel does not, by exactly one mass-ratio
coboundary — with the positive repair cone 573-dimensional against the
`(depth, sigma)` family's 28, so **the collapse to `Zhat` is the form
choice and not descent.**

**Measure line — transport scope, the horizon route.**  A *different*
tool, and the one the wall does not forbid, because it never asks for a
bounded summary (§B9.7).  The relative-horizon kernels are **proper at
every computable `(h, r)` out to `r = 7`** over a 243,769-history family,
the chained measure cut-additive by induction; the pinned
sector-normalized conditional's drift **contracts at every off-root depth
in both conditional norms at two, three and four actors**, the widest arm
enumerating 318,704 histories; the truncation convention is
**convention-protected at the root by a symmetry theorem** (`A ↔ B`,
`0 ↔ 1` exact automorphisms; one orbit per event kind; every equivariant
terminal forced) and measured to shrink off it.  **What remains is THE
BOUND**: the menu-exact renewal atom is **closed** (holdings never shrink,
0 re-entries, 0.7705 of depth-5 completed mass never regenerating), the
**σ-level class R-SIG is OPEN** (re-entered 3,796 times, hitting zero-set
collapsing `2520 → 84 → 4 → 0`, 4-step infimum `118/1455 > 0`), and
**operator-level minorization — Birkhoff / Hilbert-metric contraction of
the positive backward recursion — is the named and unattempted successor
engine.**  Nothing here is a limit claim and the word *converges* is
banned from the receipt's labels.

**Geometry line — transport scope, measure-free.**  Sky size is an
actor-width phenomenon and narrower than chance; **all three sky readings
are live** and residue 2 is reopened (§B5.4); the **Dilworth gate** is an
unconditional theorem of the layer (shatter-`k` costs `≥ C(k, ⌊k/2⌋)`
actors); a 20-actor / 42-event record shatters 4 at depths 4, 5, 6, and a
42-actor / 84-event record shatters 5 at depths 5, 6, 7, **forced** at
every step; the calibration ladder is exact (`B₄` fits `S²`; no five
points ever shatter there; `B₅` fits `S³`) **and is reproduced on genuine
sprinklings** — 2+1 shatters 3 never 4, 3+1 shatters 4 never 5 (§B5.7),
so max-shatter is a working **dimension discriminator** there; the
engineered records sit one rung above the whole sprinkling ladder.  **The
layer does not cap the ladder at the sphere's rung.**  And the grammar
**tiles**: a forced brick-wall record reaches sprinkling-grade
homogeneity with above-sprinkling `ω` and thin charts (§B8.6) — and it
tiles **wide**, a forced 177-event double ring holding the band while
carrying 4-direction charts at `d = 2` (§B8.7), where the **branching
bound** `|D_e(d)| ≤ B^d` then proves 4 is the delivery grammar's ceiling
and width past it must be bought with **arbitration**.  The atlas's
**transition maps are now measured** on that record and are non-identity,
cocycle-clean and **cohomologically trivial** — `H¹ = 0`, an explicit
per-chart port choice removes all 108 of them (§B8.8) — so the delivery
crystal exhibits **no structure group at all**.  **Conflict then tiles
too** (§B8.9): 21 three-proposer configurations over 2,325 events and 11
four-proposer ones over 1,380, all with zero
refusals, the arbitration share bounded by `1/(k+1)` and saturated by the
ring, and
the ceiling refined to W4c's `|D_e(d)| ≤ Bl^d` on the **live** out-degree,
so width past 4 needs 3+ **proposers**, not merely 3+ registers.  The
delivery-free **DOUBLE GRIDs** — rows and columns conflicting
concurrently — **realize `k·Bl = k²` at `k = 3` and `k = 4`** (nine
`|D| = 9` charts; eleven `|D| = 16` ones), and the height-levelled
**`ARBCHAIN**(k)`** carries the same ceiling to **25 at `k = 5` and 36 at
`k = 6`**, the `k = 5` witness C1-complete at 157/157.  **`DOUBLE-GRID(4,
4)` is inside *both* `d = 3` sprinkling band columns as a whole record
while carrying `max |D| = 16`**, so width and uniformity have no frontier
between them; the `k = 3` flagship holds one column of two at
`max |D| = 9`.  Their classes are coboundaries as well, at all five port
conventions and by all three routes, so the
sharp question — can any substrate carry a class that is not a coboundary?
— now has three families answering no, the last of them the widest objects
the corpus owns, **and one candidate answering maybe**: the transport
exchange holonomy of §B2.12, whose values `2/3` and `3/2` lie outside
`⟨5/4⟩`, and which no chart instrument can see.  And the rank-2 question
the whole road serves has its first honest answer (§B8.10): on the
fixture paper 30 itself selects, the even Gram is anisotropic with a
**trivial stabiliser** — a genuine rank-2 candidate — and is nonetheless a
**covariance, not a metric response**: no atom index, rank 1 locally, no
group acting on its channel index, and predictively equivalent to its own
trace.  `FAILS-FULL-GR` stands.

**The map between the lines — three measured segments, all from the
generated side, none transferring.**  §B2.10: the normalized menu
kernel fails Theorem 1's commuting-square identity on 32,256 of 425,334
refined-record-identical ordered pairs, by exactly the coboundary of the
per-state menu mass, zero exceptions — while `μ_Ẑ` is constant on all
5,548 record classes.  §B2.11: over the same layer the space of
paper-29-shaped functionals is exactly counted, and it is **large and
structureless** — under paper 29 §4.3's own condition `cohdim = coh` at
every depth and in every variant (15,058 at `D = 5`), positivity never
binds, the classical member is interior, and the whole table is
**measure-independent**.  One demand changes that completely: require the
coherence excess to be generated by the closed law's own state space —
fair, since the classical member satisfies it — and `cohdim = 0` at every
depth tried.  **At closed scope a quantum layer cannot be both
state-generated and coherent.**  Scope carried at every citation: one
demand, one record functor, one bound of the three C1 readings,
truncation-bound; **DC3(2) is narrowed, not discharged.**  §B2.12: the
segment's *phase* leg, where the corpus's own archaeology supplies a
receipted amplitude form `A(R) ~ e^{−K(E)}e^{iΦ(O)}` (v7, dual-conjugation
error exactly 0, never lifted) and a `U(1)` holonomy theorem (v6 p7 Thm
7.1 / D3) proved in halves that never met — and where the weld's
measurement returns: **raw closed-scope flatness as a `[THEOREM]` with a
budget-coincidence scope clause; the normalised kernel never flat
(`⟨5/4⟩`); transport scope CURVED (88 non-unit squares + 40 half-open, all
delivery-bearing, invisible to the record-graph instrument); and
everything exhibited `R₊`-valued — NO `U(1)` PART ANYWHERE YET.**

### B11.2 The convergence question

> **Does anything in this framework prefer 3+1?**

The admissibility layer does not (§B8.5).  Three candidate homes are
named:

1. **the completed measure** — no *bounded-summary* route exists at
   transport scope (§B9), and the surviving route is the **horizon
   limit** (§B9.7): contracting at every pool and depth measured, awaiting
   its bound;
2. **resource cost** — the ladder's actor price `3 / 6 / 10 / 20 / …`;
   nothing of the kind exists in the corpus;
3. **counting typicality** — unbuilt, and **unposable until home 1
   lands**, since typicality is a statement about a measure.

**And the four frontiers are one object.**  A space-*making* mechanism
that is engineered rather than emergent; dimensionality **unselected**
(`k` is a builder's dial, and nothing in the corpus explains why a record
would have one dispute size rather than another); typicality
**unposable**; the quantum layer **excluded** at the one closed scope.
All four reduce to **a measure at transport scope** — which is why the
programme's current campaign is that measure, and why §B9.7 is the
load-bearing section of this chapter.

**A stale sentence a reader may meet elsewhere:** one result note still
reads *"the only remaining candidate inside the corpus is the completed
measure"*.  That is superseded by the three-way list above, which is the
corpus's current statement.

### B11.3 The economics-of-dimension reading

`[MY READING / SPECULATION — not a corpus claim, and must not be cited as
one]`

Every ingredient of the geometry line is a **supply** statement rather
than a possibility statement.  One actor's worldline can only ever
contribute a nested family of traces, so sky richness is bought with
parallelism and never with history (§B7.3).  The price per rung is a
concrete integer: `3, 6, 10, 20`.  The construction that works is
literally a supply chain — dedicated single-use couriers minted because
re-using a channel contaminates it via backflow (§B8.2).  And the
constraint that binds is **not** an impossibility: the ladder is uncapped
as far as it has been run.

So the shape of a possible answer to "why 3+1?" would not be an
impossibility at rung five.  It would be a **cost**: the rung at which the
marginal price of another dimension stops being worth paying, under
whatever counts as payment.  If that reading is right, candidate home 2 is
under-explored relative to candidate home 1, notwithstanding that home 1
is where the corpus has invested.

**Nothing in the corpus supports this.**  There is no cost principle, no
identified quantity being economized, and no derivation.  This is a
description of the *shape* of a possible answer, not an answer.

### B11.4 Ranked open problems

1. **THE TRANSPORT HOLONOMY, characterised.**  Transport scope is
   **curved** (§B2.12): 88 non-unit closed exchange squares with values
   `{1/2, 2/3, 3/2, 2}` plus 40 half-open ones at two actors and 12 more
   at three, every one delivery-bearing, from depth 3, and **none** of
   them visible to the record-deletion-graph census.  Four questions, in
   order: **(i)** what carries it at record level — either the right
   object is a coarser, delivery-aware record functor, or the holonomy is
   genuinely sequence-level and the record layer loses it; **(ii)** its
   **group**; **(iii)** coboundary or genuine `H¹` — `2/3` and `3/2` lie
   outside `⟨5/4⟩`, which is the first evidence in the corpus that a
   transition class here might not be a coboundary; and **(iv)** the
   **odd-sector `U(1)` search**, the imaginary exponential's last known
   address.  It ranks first because both the phase story and the
   destination's rank-2 completion hang on it.
2. **THE BOUND — the measure's existence theorem.**  §B9.7's horizon route
   contracts at every pool and depth measured and exhibits **no bound**.
   The named and unattempted engine is **operator-level minorization** —
   Birkhoff / Hilbert-metric contraction of the positive backward
   recursion `G`, and/or a genuine Doeblin condition `P^N(x,·) ≥ δν(·)`
   on the σ-level class R-SIG, neither of which needs an atom.  One
   theorem turns a contracting table into a transport-scope measure, which
   is the object §B11.2's four frontiers are jointly waiting on.
3. **A rank-2 response on GENERIC direction geometry.**  §B8.10 leaves
   exactly two live routes and neither is the direction index of a
   hand-built crystal.  *(a)* Understand the **selected** v7 fixture: it is
   the one place in the corpus where a genuinely anisotropic even Gram
   with a trivial stabiliser sits on a law whose forward error is exactly
   zero, and the cheapest open question in the unit is whether its
   `0.511428` survives centring, reweighting and the `N` window.  *(b)*
   Build charts with **stabiliser-1** direction geometry —
   sprinkling-like substrates or crystals with deliberate defects — since
   every `DOUBLE-RING` inherits its blueprint's cyclic symmetry and a form
   with a large stabiliser has *fewer* free components.  `F3` (the
   anticommutator of the generated line's own transports, symmetrised) is
   a unit of work and remains **explicitly deferred, not dropped**.
4. **A bounded description of the theory at transport scope.**  Still the
   route by which a *summary* could reach the scope where the dimension
   results live — noting that item 2's route needs **no** bounded summary,
   so this is no longer the only way through.  **Three granularities are
   now excluded** — menu-exact for *any* design (§B9.1), `(actor, type)`
   sector-exact by the refinement measurement (§B9.4b), and the two cheap
   coarsenings (type-only and total-budget-only), which blow up and which
   turn out to be **one test rather than two** (§B9.7) — and the
   delivery-lumped candidate, though verified exact on the depth-5
   window, **fails to close at 20,000** with the residual explosion in the
   view-product structure.  What remains: abstractions that give up
   exactness for the completion's **observable** demands, and a
   level-structured (QBD / R-matrix / Martin-boundary) description with
   `|holdings|` as the level.  Both untested; the finite-alphabet
   prerequisite is `[OPEN]` both ways.
5. **Residue 2, REOPENED: which sky reading is physically privileged?**
   All three are live (§B5.4), they disagree materially, and the
   dimension discriminator is sharpest under SKY-A while several other
   results were computed under SKY-B.  Nothing justifies a choice.
6. **What is left of the width road: a general-`k` proof, and banding
   above `k = 4`.**  The arbitration crystal that three units converged on
   is **built and terminal** (§B8.9): conflict tiles, the ceiling is
   W4c's `k·b ≤ k²` with "3+ registers" corrected to "3+ **proposers**",
   and it is **realized at `k = 3, 4, 5, 6` — 9, 16, 25, 36** — by forced,
   menu-offered, delivery-free records, with **height-levelling** (the
   grammar's own `('n', a)` idle) as the mechanism.  `DOUBLE-GRID(4, 4)`
   carries `max |D| = 16` **and** sits inside both `d = 3` band columns as
   a whole record, so **there is no width-uniformity frontier**.  Of its
   three motivations, **width
   is discharged**, **gluing came back negative** (the class is a
   coboundary on conflict substrates too, including both 16-wide ones),
   and **the measure is not
   bridged** — the transport-scope menu-mass census measures the
   commensurable excess and explicitly does not reproduce the d42a
   `2 → 5/2` jump.  What is left are two residues, neither of which
   blocks the road: a **general-`k` proof** that levelling always meets
   the height condition (four data points are not a theorem), and whether
   a **tiling** `k ≥ 5` schedule exists at all — with whole-record band
   membership above `k = 4` untested, since the `k = 5` and `k = 6`
   witnesses are chains rather than tilings.  Both are out of the current
   receipts' computational reach.
7. **Is there a record-level demand that forces the stationary form?**
   Two strongest candidates and their conjunction eliminated by
   measurement.  Nobody has a third — and the question now has a number
   attached from the descent side (§B2.10): *is there any record-level
   demand that cuts the 573-dimensional repair cone down to the
   28-dimensional `(depth, sigma)` family?*  Descent itself cuts it only
   to 205.  A depth-free statement of the cone is the same question again.
8. **The missing map's functional segment — MEASURED at closed scope, and
   the residue is now sharp** (§B2.10 residue 1, §B2.11).  The generated
   line still has no *derived* class operators and no *derived* Gram
   functional, so paper 29's decoherence hypothesis remains satisfied for
   the empty reason: **that, not the descent identity, is where the map is
   widest.**  What has changed is that the candidate space is now counted
   exactly, and the count says two things.  Consistency with the records
   does **not** structure coherence — the cone is large, positivity never
   binds, nothing is forced, and the whole table is a fact about `canon`
   and the prefix map rather than about the law.  And the first fair
   **dynamical** demand — that the coherence excess be generated by the
   closed law's own state space — gives `cohdim = 0` at every depth tried.
   So the open question is now specific rather than atmospheric: *is that
   demand unique?*  Two computations settle it and neither has been run —
   the faithful reading against C5 (whose cross-class rows are sums and do
   not force the kernel pointwise), and a second generation ansatz.  Below
   them sits the same question at **transport scope**, where the conflict
   weights, the mass jump and the dimension mechanism all live and where
   nothing of this section transfers.
9. **A Lean-grade mechanization of the delivery-free settlement.**  (H1)
   and (H2) are both prose-over-code — the register geometry and the five
   update rows read off the committed source, gated against it at every
   cached transition and re-derived independently to depth 9, but not
   checked *as* an induction by any machine.  It is the one residue left
   on a line that is otherwise closed at its scope (§B6.13b).
10. **General `m` for the courier builder** — visibly patterned, unrun,
   unclaimed beyond 5.  A receipt at `m = 6` (20 chains, 57 couriers,
   ~66 actors) would strengthen it; a proof of admissibility for every
   `m` would settle it.
11. **Minimality at every `m`** — `C(k,⌊k/2⌋)` versus the builder's spend
   (6 vs 20 at `m = 4`; 10 vs 42 at `m = 5`).  Both gaps architectural,
   both decidable.
12. **Upstream pricing residues**, all carried into the completion problem
   rather than patched: the `h12` dead-component inflation (`23/24`, off
   ladder); the general-depth `1 + k/4` ladder **false** under current
   pricing; the D2H merge priced `1/16` vs `1/24`.
13. **Reading-relativity**, twice: which **sky definition** is physically
    privileged (D47 residue 2, partially answered negatively by D53 — two
    of the three can never fire — but *why* SKY-B is the physical one is
    unanswered); and which **channel reading** is (D46e).  Same class of
    question.
14. **The transport-scope dichotomy itself** — whether a root-free
    completion exists there.  No longer tool-less: item 2's horizon route
    is a candidate answer, root-free by construction over the computed
    horizons and awaiting its bound.
15. **The quantum completion at the arbitration layer** (paper 30 §6.2's
    three-horn pincer) and the fine-versus-coarse sealing question, which
    is **empirical** and has an exact instrument pair waiting for it.
16. **The laboratory bridge** — blocked on an empty coarse-graining slot;
    the sole unblocking condition is *what is a laboratory system in
    record terms?*, filed as an internal derivation question.

### B11.5 What exists

**Papers, all TERMINAL:**

| paper | content |
|---|---|
| **30** — *The generated record and its completion* | §1 the grammar and admission principle; §4 the ladder and the placement problem; §5 the decided trilemma (5.2 the no-go, 5.3 gradient completions, 5.5 the flatness/telescoping theorem, 5.6 rootedness, 5.7 the one-way reduction); §6 where the quantum completion begins |
| **31** — *Four decisions at the joints* | S1 collar-bracket rule-independence (`κ(1/2) = 13/2304`, `κ(1) = −1/72`, a sign flip); S2 the six-state renewal chain and residue 1 on the window; S3 the constructed arbitration operator at fixture scale; S4 transport generates dimension |
| **32** — *The boundary of closure* | §2 residue 1 at every verified depth and its exact boundary; §3 dimension mechanized, ceiling-free and scoped, with the binding doctrine; §4 the quantum layer welded to the completion; §5 the regulator closed for all masses; §6 the residue ledger |

Plus the standalone brief `v10/THE-COMPLETION-DICHOTOMY.md`, the entry
point for the measure line, which chapter 6 compresses.

**Receipts** live in `v10/code/`, outputs in `v10/data/`: exact rational
arithmetic, standard library only, exit 0 required, determinism verified
across hash seeds.  The ones this document leans on most:
`d42b3_placement_exact.py` (the p/r/n admission layer and the completion
decision), `d42b1_transport_exact.py` (delivery and merge; the *"no
measure claim"* disclaimer), `d44a_closure_theorem_exact.py` (the closure
theorem), `d46a_h1_lemma_exact.py`, `d47a_sky_instrument_exact.py` (the
sky definitions and the constructed separator),
`d47b_transport_skies_exact.py`, `d48_composite_line_exact.py`,
`d49_dichotomy_settlement_exact.py`, `d50_form_law_or_choice_exact.py`,
`d51_menu_visibility_exact.py`, `d53_sky_capacity_exact.py`,
`d54_dilworth_gate_exact.py`, `d54b_shatter_construction_exact.py`,
`d55_shatter5_exact.py`, `d55b_sphere_calibration_exact.py`,
`d56_transport_sigma_probe.py`, `d60p_h1_probe.py`,
`d61_h1_closure_exact.py` (the own-view dichotomy and the closed form),
`d62_h2_update_table_exact.py` (the update table),
`d63_wide_crystal_exact.py` (the wide crystal and the branching bound),
`d64_cocycle_exact.py` (the transition census and the coboundary gate
C7), `d65_descent_conditions_exact.py` (the descent conditions and
the repair cone), `d66_arbitration_crystal_exact.py` (the conflict
crystals, W4c, and the DOUBLE GRID) and
`d68_functional_slot_exact.py` (the three C1 readings, the exact
dimension table, the coherence geography and the dynamical demand),
`d70_horizon_limit_exact.py` (the relative-horizon kernels, the Cauchy
table at three actor pools, the root symmetry theorem, the renewal
census and the aggregation arm — **51 PASS / 0 FAIL**, 1,086 s, the
campaign's longest), `d72_weld_exact.py` (the reversal carrier, the
flatness theorem's six lemmas, the normalised holonomy and the
transport-scope census — **77 PASS / 0 FAIL**, 468 s) and
`d73_even_gram_exact.py` (the even Gram on both fixtures, the promoted-`K`
family, the `h`-weight identity and the seven-blueprint transfer sweep —
**38 PASS / 0 FAIL**, 524 s; note that the committed v7 campaign calls
`int.bit_count`, so it needs Python `≥ 3.10` and the receipt carries a
version guard rather than crashing inside a lifted namespace).

**The ledger:** `v10/LOG.md`, append-only, numbered, **forward
corrections only, never silently edited.**  Entries #404–#491 cover
everything in chapters B5, B7, B8, B9, the settlement line of B6, and the
descent, functional-slot and phase segments of B2.

**Review records:** `v10/reviews/*.md`, frozen; a round is followed by
repairs and a **delta appended to the round file**, and only then is a
unit terminal.  (#420 exists because a ledger entry once claimed a delta
that had not landed.)

### B11.6 The method

- **Pin first, strictly.**  The plan, the gates, the falsifier, and the
  **pre-registered expectation with its argument**, committed before any
  code exists.  Where that discipline slipped it was declared (D49's pin
  was written *concurrently* with the receipt, and the pin's §0 now says
  so rather than leaving it implied).
- **Pre-register the boring outcome.**  D47's pin: *"pre-registering the
  boring outcome is the cheapest defence against later talking oneself
  into an exciting one."*  It was realized at the control, before any
  transport data was examined.
- **One-sidedness doctrines, declared in advance.**  D47's (shattering
  rules out, never in) and D50's (a tangent dimension > 1 is rigorous in
  the negative, a dimension of 1 is local evidence only).  Both determined
  which side of the eventual measurement could carry a conclusion, and in
  D50's case the measurement landed on the conclusive side.
- **Instrument before data.**  D47a reads **no** transport data at all;
  its successor imports it by AST extraction from the committed source so
  a silently-changed extraction cannot pass.  This was the direct
  methodological answer to the D46 sweep's five reversals.
- **Capacity gated first.**  A zero over an empty or incapable stratum is
  reported as a **vacuity or an undecidability**, never as a negative.
  D53 exists because that discipline was applied with a *necessary but
  insufficient* condition.
- **Witness branches live and exercised.**  A gate whose failing branch
  has never run is not a gate; the corpus binds successor receipts to
  exercise theirs.
- **Falsified pre-registrations are deliverables at exit 0.**  Only
  anchor breakage and mutant misbehaviour exit 1.
- **Hostile rounds, and now independent-model rounds** — a reviewer with
  no prior context, instructed to recompute rather than trust, writing its
  own code.  Thirteen have run; nine found a BLOCKER; **all nine BLOCKERs
  were in interpretation, none in arithmetic** — and two of the three most
  recent reversed a headline without raising a BLOCKER at all (§B10.17).
- **Ask what would distinguish the headline from its trivial
  alternative** — the lesson D64 through D73 have now taught eight times.
  Every one of those units measured correctly, reported correctly,
  and read
  the numbers as a structure that one computation none of them had run
  would have shown was absent or different (a coboundary test; a
  repair-cone dimension; a schedule whose successors are arbitrations
  rather than deliveries; **one more round of a family whose own printed
  trend was walking into the band**; the parent paper's decoherence
  condition written as the parent paper states it; **a third term on a
  two-term row**; **the same square census one grammar over**; **the
  provenance of the unit's own fixture**).  The obligation is now
  on the pin: *name the
  computation that would make the interesting reading false, and run it in
  the same receipt.*  The recent rounds add the corollary that meeting it
  can **pay**: the construction that refuted D66's headline became the
  campaign's strongest geometric object; the round that refuted D67's
  turned a published *limitation* into the programme's best geometry
  statement; the round that refuted both of D68's spent the ten lines
  that unit's own residue had named and declined, returning the
  programme's first hard fact about its quantum layer; the round that
  refuted D70's spent 408 s of single-core enumeration the unit had priced
  and skipped, returning the measure route's positive; and the round that
  refuted D72's **closed the proof the unit had sketched** and found the
  curvature in the same pass.  **The obligation
  covers negatives too — a limit announced is a claim, and it is cheapest
  to test by extending your own table.**  *And a corollary the pin must
  now carry:* **price the evidence as well as the direction** — a binary
  clause that can fire on a two-term row at the shallowest declared cap is
  a clause a unit can satisfy without learning anything.
- **Gate the quotation, not just the computation.**  D68's two withdrawn
  sentences were properties of *conventions the unit chose* — one
  forbidding cancellation by hand, one row shape symmetric by
  construction — and were false of the object under study.  When a demand
  is imported from a source, the import is a load-bearing step and belongs
  in the gate list beside the arithmetic.
- **Gate the FIXTURE'S PROVENANCE too.**  D73 anchored a whole unit on
  three record pairs its own source paper audits, ranks eleventh and
  declares falsified — so its central negative was guaranteed and
  discovered nothing.  The repair is a text-slice gate on the source's own
  selection sections, and the rule is standing: **before anchoring on a
  published example, read what the paper that published it says about it
  afterwards.**  Its companion: **measure your controls** — D73 built a
  comparator, computed its matrices and reported only how many there were,
  so it controlled nothing until the round measured it and it fired the
  unit's own death condition.
- **Credit the round as authorship.**  When a referee supplies a theorem,
  a census or a computation, the repaired receipt **rebuilds every figure
  in its own process and gates it like any other number** — and the note
  says whose it was.  Recent rounds have supplied a depth-free proof, a
  transport-scope census the unit's instrument could not see, a
  318,704-history arm and a corrected control.  A round that only audits
  is the weaker outcome.
- **Green-unreviewed is not citable**, and terminal papers are **not
  edited on green-unreviewed evidence** — amendments queue behind a round.
  The rule's one recorded breach is instructive: a settlement banner was
  written into the corpus's entry-point document before any round, and
  without scope.  It was caught by the round it had pre-empted.
- **Determinism is a gate, not an assumption.**  A defect that produced
  seven spurious mismatches surfaced only under hash-seed variation, from
  serializing events through a raw `frozenset` repr; it was recorded
  rather than quietly fixed.  And a round once logged as delta'd when the
  frozen file contained no delta — the repairs were real, the record of
  them was not, and the correction went forward with its cause stated.
- **Forward corrections only**, with superseded text preserved verbatim
  beside its replacement.
- **A port check is not an independence check.**  Re-implementing a
  computation from the same description reproduces its errors exactly: a
  ported check once returned a wrong boundary-freedom figure to the
  digit, and the defect surfaced only when a reviewer rebuilt the object
  from the demand rather than from the method (§B6.12).  Independence
  means a different route, not a second author.

That last rule is why this document could be written at all.  Chapter B10
is not reconstructed from memory; it is transcribed from a record designed
to make forgetting impossible.

---
---

# PART C — THE EARLIER CORPUS (v1–v9, the SHARD / ISP arc)

> **Why this part exists.**  Chapters 1–12 describe the **v10 campaign**: a
> generated record grammar, its measure problem, and its geometry.  That is
> roughly two months of a programme that has been running for far longer.
> Before v10 there were nine version lines, several hundred papers and
> notes, and a *different* formalism — one built on **seals** rather than
> on a generated grammar.  A book that covered only v10 would misrepresent
> what the corpus is, and would omit the one piece of Einstein's theory the
> corpus already owns (chapter C2), which matters because the programme's
> standing destination is Einsteinian manifolds (PART D).
>
> **Two registers, kept.**  Each chapter here opens with **① PLAINLY** —
> the non-technical twin, readable on its own with no formulas — and then
> **② THE OBJECTS** — the technical account with numbers and provenance.
> A reader who wants Part A's register throughout can read the ① sections
> of C1–C5 in order and skip the ② sections entirely.
>
> **Scope warning, binding.**  v6 and v7 are **FROZEN research logs**
> (frozen 2026-07-01).  Their authoritative result map is `v8/LEDGER.md`,
> and corrections after that date land in v8 and the ledger **only**.  So a
> v6 file may contain a claim that has since been corrected elsewhere —
> §C1 contains a live instance.  Every citation below names its file, and
> where a frozen file disagrees with the ledger, this document follows the
> ledger and says so.

---

## C1. The sealing premise and the original programme

### ① PLAINLY

The earlier corpus is built on one idea: **the world is a ledger of things
that have been irreversibly written down.**  The technical name for the act
of writing is a **seal**, and the programme is called SHARD — *Sealed
Holonomy And Record Dynamics*.

Three principles govern it, and they are worth stating because they are the
ancestors of everything in Part A:

- **Laws are laws of whole sealed histories**, not of instantaneous states.
- **No distinction without a record.**  If nothing was written down, there
  is no fact of the matter about which alternative happened.
- **Couplings are fixed by self-consistency**: the constants of the theory
  are supposed to be pinned by the demand that the description be
  consistent with itself when you look more finely.

Between two seals, the system carries something the programme calls a
**holonomy** — a coherent, uncommitted relative phase.  Nothing is decided
yet; the alternatives are still live.  At a seal, one of them **commits**,
irreversibly, and the holonomy is destroyed.

That gives a crisp classical/quantum dividing line, which is the whole
point of the formalism.  A *classical* history is one where you could
always have inserted an extra record in the middle without changing
anything — the chain of seals is **refinable**.  A *quantum* history is one
where you cannot: inserting a record in the middle means *sealing* it, and
sealing destroys the phase, so the process you end up describing is a
different one.  In the language of the physicist Jacob Barandes, whose
work this builds on, a quantum process is **indivisible**: its transition
law does not compose through intermediate times.

**The quarter law.**  The most-cited quantitative result of that line is a
short theorem with a memorable shape.  Suppose the environment learns
something about which alternative your system took — it leaks *evidence*.
Two things then happen: the evidence accumulates, and the system's
coherence decays.  The theorem says the coherence decays at **exactly one
quarter of the rate at which evidence leaks**, to leading order, with the
first correction computed exactly.

That is a genuine and pretty result.  It also carries one of the corpus's
cleaner self-corrections, and one of its sharpest warnings.

*The self-correction*: a companion paper had proposed, as a **target** of a
research programme (explicitly not proved), that "the decoherence rate =
the seal rate = the entropy production".  That target was later
**dissolved**: the quarter law is the true relation, and the coefficient
would be one only for a different measure of information.  The frozen file
still contains the old target; only the consolidation ledger records the
dissolution.  This document follows the ledger.

*The warning*, which came from within the programme and is sharper: in the
regime where the leak is weak, the factor of one quarter is **not physics
at all** — it is a general fact about how two nearby probability
distributions relate, true for *any* monitoring scheme.  So a later
project that "confirmed the quarter law" in a new setting would be
confirming a mathematical tautology and calling it a bridge.  The corpus
names this the **universality trap**, in its own design note, before
walking into it.

*And one live erratum, filed and not yet routed*: the overlap quantity the
law is stated in is only a **bound** — it is the Cauchy–Schwarz estimate,
saturated only when a relative phase stays constant.  The correction
exists, in a sibling paper of the same version line, and it never reached
the paper that states the law, the archive status block, or the v10 paper
that cites it.  It is recorded here because a reader will otherwise meet
the uncorrected form in three places (§B2.12).

### ② THE OBJECTS

**The ontology.**  `v6/publishable/paper-Va-foundations-1.md` states the
programme's axioms verbatim: **R** (laws are laws of whole sealed
histories), **S** (no distinction without a record), **C** (couplings are
fixed by self-consistency under refinement); the primitive is *a ledger of
sealed records*; the programme "builds on the stochastic–quantum
correspondence of Barandes' indivisible processes, replacing configuration
trajectories by committed records as the primitive."

**Seal, holonomy, refinability** (`v6/…-paper56-…` §2.2): between record
commitments the system carries a reversible **holonomy** (a closed
exchange-defect phase, no committed value); at a seal a record **commits**,
irreversibly.  The dividing line:

- **Classical:** the history is a *refinable* chain of seals — an
  intermediate conditioning record may be inserted for free.
- **Quantum:** the **sealed holonomy between records carries irreducible
  phase** — one cannot insert an intermediate record without sealing it,
  and sealing destroys the holonomy and changes the process.

The proposed dictionary, stated in that paper as a `[TARGET]` and **not**
as a theorem: *SHARD-unrefinable ≟ Barandes-indivisible*;
*sealed-holonomy-between-seals ≟ the interference cross-term*; *a SHARD
seal ≟ a Barandes division event*.  The **functor** realizing it "is itself
the open obligation, not yet written."

**Barandes' barrier, made explicit** (same paper, §2.1): with
`Γ(t)_{ji} = |U(t)_{ji}|²`,

```
[Γ(t₂)Γ(t₁)]_{ji} = Σ_k |U(t₂)_{jk}|² |U(t₁)_{ki}|²      (sum of path probabilities)
Γ(t₂t₁)_{ji}      = |Σ_k U(t₂)_{jk} U(t₁)_{ki}|²         (probability of the path sum)
```

and the difference is the interference cross-term.  **The barrier is the
gap between `|Σ|²` and `Σ|·|²`.**

**Division events** (`v6/…-paper1-…`): the primitive of the gravity sector
is "the network of **division events** — the records at which an indivisible
stochastic process momentarily factorizes — whose causal order is
Lorentz-invariant and whose counting fixes volume, so that *order + number
= geometry*."

**THE QUARTER LAW `[THEOREM A, v6 paper 26 §3.1, with proof in file]`.**
Setting: one logical qubit, pointer alternatives `χ ∈ {0,1}`; per cycle the
environment draws one record bit from `P_χ`, with the symmetric binary
monitor `P_0 = (½+ε, ½−ε)` and `P_1` mirrored.

> Per cycle the off-diagonal multiplies by the **Bhattacharyya overlap**
> `BC = Σ_b √(P_0(b) P_1(b))`, the leaked evidence is `σ = D(P_0 ‖ P_1)`,
> and
>
> ```
> −ln BC  =  σ/4  +  (ε²/6)·σ  +  O(σ³)
> ```
>
> — coherent record capacity decays at one quarter of the evidence rate to
> leading order, with the first correction explicit.

*Proof (in file).*  The record imprint sends `ρ_01 → ⟨e_1|e_0⟩ ρ_01` with
`|e_χ⟩ = Σ_b √(P_χ(b))|b⟩`, so the multiplier is exactly `BC`.  For the
symmetric monitor `BC = √(1 − 4ε²)`, hence `−ln BC = 2ε² + 4ε⁴ + …`; and
`σ = 2ε ln((1+2ε)/(1−2ε)) = 8ε² + (32/3)ε⁴ + …`.  Dividing gives
`1/4 + ε²/6 + O(ε⁴)`.  ∎

Receipts as printed:

| `ε` | `σ`/step | `−ln BC` | ratio | `1/4 + ε²/6` |
|---|---|---|---|---|
| 0.02 | 0.003202 | 0.000801 | **0.250067** | 0.250067 |
| 0.05 | 0.020067 | 0.005025 | 0.250419 | 0.250417 |
| 0.10 | 0.081093 | 0.020411 | 0.251699 | 0.251667 |
| 0.20 | 0.338919 | 0.087177 | 0.257220 | 0.256667 |
| 0.40 | 1.757780 | 0.510826 | 0.290608 | *(domain boundary)* |

General monitors live in the band **[0.10, 0.49]** — "`σ` is the right
currency within `O(1)` factors."

> **LIVE ERRATUM, filed and unrouted.**  `BC` is only the
> **Cauchy–Schwarz bound** on the off-diagonal multiplier, saturated
> **iff** the relative pointer phase is constant across the record
> alphabet.  The correction is stated in **v6 paper 7 §12** and never
> reached paper 26, the archive status block, or v10 paper 18.  It does
> not move the theorem's leading coefficient; it moves the theorem's
> *hypothesis*, and every citation of the quarter law should carry it
> (§B2.12).

**And the same version line owns the corpus's high-water mark on
phase, which the v10 chapters cite nowhere else.**  v6 paper 7 Thm 7.1
derives that the retained holonomy of a **closed route pair** is
`SO(2) = U(1)`-valued — deriving `C` as the value space and using
**positivity** to select the ordinary circle over its split-complex
impostor — and Thm D3 proves that two-route interference **is** the
loop-phase law `P = |A|² + |B|² + 2|A||B|cos(arg B(loop))` at machine gap
`2.8e-17`.  Its standing is contested inside the corpus and the contest is
unresolved: the submitted batch (paper Va) lists the same result as an
**INPUT**, and v8 paper 2 proves the records cannot **force** it.  §B2.12
carries the whole disagreement, because it is one of the two halves of the
weld the generated line is now testing.

**THE DISSOLVED `[TARGET]`, and a live file-level inconsistency.**  Paper
56 §2.2 proposes *"the decoherence rate = seal rate = `σ`"* as **a proposed
law of that program `[TARGET]`, not automatic** — the paper says so in its
own sentence, and its status block says "**Nothing here is claimed
proved.**"  `v6/ARCHIVE-STATUS.md` then records, at the freeze:

> paper56's `[TARGET]` "decoherence rate = seal rate = σ" was **dissolved**
> (2026-06-17: the quarter law `−ln BC = σ/4` = paper26 Thm A; `κ=1` only
> for the mutual-information measure).  **The v6 file does not record
> this**; the ledger and v8 paper 6 do.

Two further caveats are recorded at the same freeze and are worth carrying:
the 2026-06-16 Renou/real-quantum retirement was propagated through v7 but
**v6 was never swept**, so any v6 line asserting "Renou ruled out real QM"
or "three experiment-fixed inputs" is **stale** (the sweep was later
executed and recorded in `v6/ERRATA.md` E1); and paper 10's T3 "is a
dissolution (not an RP-theorem), per paper10's own reclassification."

**THE UNIVERSALITY TRAP, named by the corpus against its own interest.**
`v9/note-bridge-seal-is-record.md` §3 observes that `−ln BC = D_{1/2}(P₀‖P₁)/2`
*identically* (Rényi-½), and that as `P₀ → P₁` all Rényi orders are
proportional to the shared `χ²`/Fisher term with `D_α ≈ (α/2)χ²`, so

```
(−ln BC)/σ_wp  →  ((1/4)χ²/2) / ((1/2)χ²)  =  1/4     for ANY monitor family
```

— "this is the receipt-carried `κ_α = 1/(4α)` of v8 paper 6 §5, not a new
fact."  Therefore:

> **In the weak-evidence limit the ¼ ratio is measure-theoretic
> universality — confirming it on the web would be a fake bridge.**

The design note accordingly moves the falsifiable content elsewhere (the
Fisher identity, the monitor class, covariant readability — see §C5).  A
programme that noticed its own headline was a tautology in the limit it was
most likely to be tested in, and said so in a pin, is doing the thing this
document keeps pointing at.

**The rest of paper 26, briefly, since it is the corpus's first applied
paper.**  Selective record formation: on the 3-qubit bit-flip code,
`I(logical : syndrome) = 0.00e+00` **exactly** while
`I(error : syndrome) = 0.7705` of `H(error) = 0.8363` — *protection is not
fewer clicks, it is correctly typed clicks*; recovery converts first-order
leakage to second-order failure (`3p² − 2p³`, machine-exact).  The metric:
at matched per-cycle fidelity `0.99336`, a coherent over-rotation recovers
at `1.000000` under echo while the dephasing one sits at **`0.566762`** —
*fidelity is blind, leaked nats are not*.  Threshold ordering by
coordination `z`: honeycomb ≈ 6.7% < square ≈ 10.9% < triangular ≈ 16.4%.
Quantum advantage as cone violation: stabilizer states nonnegative, **the
magic state at `−1/3` exactly**, cost compounding as `(Σ|W|)^{2n}`.  And
pre-click capacity is schedule-invariant: MBQC's clicks are exactly
logical-evidence-free (`p(m) = 1/2` to `4.4e−16`).

> **Cross-reference.**  The seal/holonomy dividing line of this chapter is
> the ancestor of Part A chapter 2's *click*, and the "no distinction
> without a record" axiom is the ancestor of the v10 grammar's insistence
> that admissibility is past-local.  **Whether that ancestry is a formal
> relation or only a family resemblance is exactly the question of §C5, and
> the answer there is uncomfortable.**

---

## C2. Gravity from sealed records

*Source: `v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md`
(127 lines, read in full for this chapter), with the conditionality analysis
from `v7/relativistic-isp-v7-paper17-three-walls-classification-theorem.md`
§4 and `v8/relativistic-isp-v8-paper3-walls-classification.md` §1.*

### ① PLAINLY

This is the chapter where the earlier corpus touches Einstein, and it has a
sharply two-sided result which the paper itself summarizes in one line:

> **SHARD gives gravity's form for free and proves it cannot give gravity's
> scale.**

**The form.**  Following a route opened by Ted Jacobson in 1995, the corpus
derives Einstein's field equations as a *thermodynamic equation of state*.
The ingredients: an accelerating observer sees a temperature (this comes
out as a theorem about the record's own division rate); the entropy of a
horizon is proportional to its **area** with a coefficient that does not
run; and applying the elementary thermodynamic relation *heat = temperature
× change in entropy* to every local horizon then forces the shape of
Einstein's equations.

Two things are *derived* here that the standard version of this argument
**assumes**, and that is the corpus's own contribution: the geometry factor
in the area law (it converges to a known universal constant with no fitted
tail), and the pure-area property of the entropy (no curvature corrections).

**The scale.**  And now the hard result.  Einstein's equations contain
Newton's constant `G`.  The corpus proves it **cannot derive it** — and the
proof is not a list of failed attempts but a single structural theorem.

The idea is a dimensional one and is easy to state.  Everything the records
carry is a *pure number*: a ratio, a count, a dimensionless invariant.  But
`G` requires an absolute **length**, and there is no length in a bare
collection of counts and ratios — you only get one by choosing a
conversion from "one record step" to "one metre", and that conversion is
exactly the thing the records cannot see.  Rescale the record's length unit
and every single sealed observable is unchanged while `G` moves.

Seven independent escape routes were tried — modular time, causal-set
actions, fluid-gravity, holography, shape dynamics, the cosmological
horizon count, the spectral action.  **All seven collapse the same way**,
and the paper's point is precisely the unification: they do not fail for
seven reasons, they fail for one.  Every route that seems to deliver `G`
turns out to have traded it for a cutoff length, which is the same missing
label wearing a different name.

A separate test asked whether a *second* independent scale could be found
somewhere in the theory and used to calibrate the first.  All candidate
second scales turned out to be **the same one record length in disguise**.

**The graviton.**  A further honest split.  The *equation* for the
gravitational field's shape is derived.  But the propagating **graviton** —
the quantum particle of the gravitational field — is not: the corpus's
machinery can price the energy and momentum of matter but is effectively
**blind** to the five components that carry spin-2 content in a universal
way, and four independent obstructions converge on one root, which is that
the needed structure lives only in a continuum algebra that a finite
record lattice cannot host.

**And one honesty constraint that runs through everything.**  The chain
that names the missing quantity "Newton's `G`" rides Jacobson's derivation,
which has its own well-known critics.  The corpus therefore refuses to
present the `G` result as a clean structural no-go.  Its own phrasing:
**the wall stands unconditionally; the `G`-naming of it is conditional.**

### ② THE OBJECTS

**Status tags in that paper:** `[DERIVED]` = established (symbolic or
high-precision numeric); `[NO-GO]` = a proven obstruction; `[OBSTRUCTED]` =
blocked in practice with the obstruction characterized; `[OPEN]`.  All
numeric claims verified at **mpmath dps ≥ 80** (commonly 100), the paper's
own audit noting that float64 produces a **25–32% artifact** on
modular-kernel / near-vacuum quantities.

**C2.1 The derived equation of state.**

- **Temperature `T = a/2π` `[DERIVED, mod axiom (R)]`.**  KMS on the
  accelerated Wightman function, `W(τ − iβ) = W(−τ)` at `β = 2π/a`, holds
  to the iε floor (residual ≈ **3.75×10⁻⁴⁰**); detailed balance
  `F(E)/F(−E) = e^{−E/T}` machine-exact (≈ **10⁻¹⁰¹**); the Rindler identity
  `Δt² − Δx² = (4/a²)sinh²(aΔτ/2)` exact (sympy).  **The honest split:**
  Gibbs thermality at *some* `β` is **unconditional** (record passivity / a
  finite Lenard theorem); the *value* `β = 2π` rests on the one named,
  unproven **axiom (R)** — the Euclidean-rotation / modular-period
  identification, the residue of Bisognano–Wichmann.  *The no-go of §C2.2
  does not depend on (R).*
- **Geometry-universal area density `[DERIVED]`.**  A 3+1 massless scalar
  partial-wave-decomposes into radial chains; the ball entropy's area
  coefficient converges to **Srednicki's 0.295** — `a(l_c = 5120) =
  0.295307`, Richardson `a_∞ = 0.295417`, grid- and box-robust to ~10⁻⁵ —
  **with no fitted tail**.  The ball/planar capacity ratio
  `U_G = ν_sph/ν_planar = 1` to ~10⁻³, and the absolute scale **cancels** in
  it (sympy-confirmed).  *Two caveats stated in file:* `U_G = 1`
  **straddles** unity at that level (the sign of `U_G − 1` is undetermined,
  cutoff-limited — a consistency, not a determination); and flat-screen
  universality is **broken in the angular sector**, the partial-wave
  first-law ratio `q_l` departing from 1 (down to ≈ **0.83** at `l = 1`).
- **Pure-area Wald–Noether charge `[DERIVED, structural]`.**
  `S = σ_A·A + o(A)` with curvature pieces explicitly subleading; the
  apparent curvature-running shrinks monotonically with the mode cutoff
  (`|Δa| = 3.2×10⁻³ → 6.9×10⁻⁴` over `l_max = 40 → 200`), *consistent with*
  an `l`-truncation artifact; the `l = 0` channel completes at `q = 1.000`.
  This **discharges** the "no Wald corrections" precondition **within the
  screen-cell entropy ontology** — a structural property of that ontology,
  explicitly *not* a derivation that an arbitrary higher-curvature action
  generates no Wald corrections.
- **The field equations in form `[DERIVED, mod (R) + gates]`.**  Jacobson's
  Clausius derivation, exact in sympy: Raychaudhuri `θ = −R_kk λ + O(λ²)`;
  heat- and area-side affine moments cancel identically; **the null-cone
  lemma forces a pure-trace tensor `S_ab = Φ g_ab`, fixing all 9 traceless
  components in one geometric step**; contracted Bianchi closes (checked on
  explicit Schwarzschild and on an anisotropic fluid with genuine traceless
  stress); the coefficient match `2π/η = 8πG` forces **`η = 1/4G`**.  The
  Clausius route delivers the full **nonlinear** equation; the modular
  first law gives the **linearized** one.
- **The unimodular fork `[DERIVED]`.**  Trace-free Einstein is a genuine
  9-component equation (traceless on both sides only in `d = 4`); its
  divergence plus contracted Bianchi gives, with
  `Λ := (R + 8πG T)/4`, exactly `∇_b Λ = 8πG η_b` (**residual identically
  0**, sympy).  So the conservation/Bianchi obstruction is *rerouted into a
  dynamical `Λ`*, not evaded; the traceless RHS is homogeneous degree-1 in
  `G` (dps-100: `|RHS(3G) − 3RHS(G)| ≈ 10⁻¹⁰⁹`); the cosmological constant
  becomes a **non-sourced integration constant `Λ₀`**.

**C2.2 The unified no-go on `G` `[NO-GO]`.**

`σ_A` has length-weight **−2** and is in bijection with `G` (weight **+2**)
via

```
G · σ_A = 1/4        (linked, never equal)
```

Under the gauge `A_rec → λ·A_rec` holding all sealed data fixed,
`κ → λκ` and `σ_A → λ⁻¹σ_A`, and the only things fixed are the weight-zero
invariants:

```
κ · σ_A = 2π         and, SEPARATELY,        G · Λ² = const
```

> **A correction this document must make explicitly.**  These are **two
> distinct weight-zero invariants — each a fixed pure number, and they are
> NOT numerically equal.**  The paper says so twice, in the abstract and in
> §2.1 ("*two weight-zero invariants — each a fixed pure number, not
> numerically equal to one another; what they share is the structure, not a
> value*").  A summary of the form "`κ·σ_A = G·Λ² = const`" — which is how
> the result is sometimes compressed — **is wrong as an equality**, and is
> corrected here.  Also: `Λ` here is the inverse-length UV/spectral cutoff,
> **distinct** from the unimodular cosmological constant `Λ₀` of §C2.1.

- **SIGMA-SPLIT.**  The *same* sealed horizon data are consistent with
  `A_rec = 1` **or** `A_rec = 3`, giving `κ = 1` or `3`, with Einstein
  residuals **`0.0` for both**.
- **The G-rescaling test (dps-100):** `s_unit → λ·s_unit` sends `G → G/λ`
  while **every** sealed / order / modular observable is invariant.
- **The single load-bearing premise, isolated as cleanly as axiom (R):**
  **gate G1** — *no sealed law consumes the record area `A_rec` except
  through the continuum labeling map `ℓ`*.  G1 is what makes the corpus
  factor so that Theorem G forces every intrinsic record functional to
  weight 0 while `σ_A` is weight −2.  **The no-go is airtight iff G1
  holds.**
- **The sharpest candidate counterexample CLOSES G1 rather than opening
  it** (sympy-exact + dps-100).  An intrinsic *seal rate* `Γ` carrying an
  absolute scale: record-internal `Γ` is divisions-per-seal `= 1`
  (weight 0); any geometric `Γ` is the seal density `1/l_step` (weight −1,
  verified `g_λ : Γ → Γ/μ` to ~10⁻¹⁰¹); a putative weight-(−2)
  `Γ² = (#²)/A_rec` is a free record number times `1/A_rec` — a relabeling.
  An intrinsic absolute scale would need weight −2 *and* weight 0 at once.
  **So the seal-spacing length `l_step` is provably the unique dimensionful
  primitive and the sole gauge direction.**

**C2.3 The second-scale test — every route collapses onto the one record
length.**  The weight-counting lemma (sympy) settles them at once: *every
dimensionful record quantity is (pure number) × `l^{±k}` — one record
length — and every intrinsic record functional is `g_λ`-invariant, hence
weight-zero.*  Concretely:

- a **mass-gap correlation length** (`ξ_1d = 1/η = 1.641…`,
  `ξ_2d = 23.355`) — both are *lattice units*, `ξ = (#)·l`, not an
  independent length;
- a **transmuted scale from a second marginal sector** — a fixed-point
  coupling is dimensionless, so the ratio ties sectors to each other, never
  to a geometric length;
- an **asymptotic-safety UV fixed point** — `g_* = Gμ² ⇒ G = g_* l²`,
  reproducing SIGMA-SPLIT exactly.

**C2.4 Seven levers, one obstruction `[NO-GO]` each.**

| lever | how it collapses |
|---|---|
| **Tomita–Takesaki / Connes** | the boost-relevant record algebra is forced **commutative**, so modular flow is trivial; Araki relative entropy = KL exactly (`\|diff\| = 0`); the modular-time↔boost-rapidity slope is reparametrization-free (dps-80, invariant to ~10⁻⁸¹) — *it is the free modulus* |
| **Benincasa–Dowker causal-set action** | circular on three counts: the BD constants are pure numbers (d=4 prefactor `4/√6` to 80 digits, `M₀ = O(10⁻⁸⁵)`); EH-matching is one scalar equation `l²/G = 16π ξ₄`; BD adds one equation *and* one unknown `l` — the gauge direction.  Also pathological: action fluctuation std grows as `ρ^{+1.2}` |
| **Fluid/gravity** | `η` and `s` both scale as `1/G`, so `η/s = 1/4π` **cancels** `G` (verified to 10⁻⁷⁰) |
| **Entanglement-wedge / JLMS** | `1/4G` is the *shared* coefficient — a consistency, not a derivation; Brown–Henneaux `c = 3L/2G` needs the AdS radius in record units = the same missing label |
| **Barbour / shape dynamics** | conformal/relational structure generates no length; Weyl invariance actively **removes** the datum `σ_A` needs |
| **de Sitter horizon count** (the sharpest test) | `Λ₀` is a genuine weight-(−2) datum — `σ_A`'s **weight-twin**.  `S_dS = π/(G·Λ₀) = N_dS` fixes only the product; `N_dS = 4π(σ_A/Λ₀)` is a ratio of two weight-(−2) data so `l` cancels (sympy-exact).  Not a second channel — the same collapse with `σ_A` replaced by its twin.  (Undersourcing table: collapse heating undersources `ρ_Λ` by **10–17 orders**; only the *drift* `dΛ = 8πG η` is sourced, never the value) |
| **Chamseddine–Connes spectral action** | `[CONJECTURED]`, not established: the naive collar profile `e^{−2πu}` gives `f₂ = ∫u e^{−2πu} du = 1/(2π)²`, **not** `1/(2π)`, so the often-quoted `G·Λ² = 3π²` does **not** follow; and identifying the spectral test function with the wedge-boost modular profile is an unjustified ansatz.  Either way the cutoff `Λ` is the same missing label |

Further levers collapse identically: the conformal trace-anomaly
coefficients `(a, c)` are weight-zero; Sakharov-induced gravity gives
`G·Λ² = 192π²/N` with `Λ` cancelling; and the strongest *record-unit*
attack (measure a mass in record units, claim `G = c_m/m_rec²`) smuggles in
the record-length↔lab-length conversion the gauge acts on.

> **The unification is the content:** *deriving `1/G` always trades it for a
> labeling-equivalent cutoff; the missing datum is exactly one absolute
> length unit, which no weight-zero record functional can be.*

**C2.5 Graviton spin-2 blindness `[OBSTRUCTED]`.**  Charge pricing is
**4 of 9**: `T_00` (energy, boost-axis first law) and `T_0i` (momentum,
moving-probe first law) are priced at capacity coupling `1/(4ν)`; the five
spatial-stress components `T_⟨ij⟩` are not.

**The obstruction is non-universality, not orthogonality.**  A boosted
wedge reads `T'_00 = cosh²η·ρ + sinh²η·(n_i n_j T_⟨ij⟩)` (sympy-exact), and
a congruence of boosted wedges over `n ∈ S²` has **rank 5 — it spans the
entire traceless spatial-stress space** (augmented `[ρ | 5 TL]` rank 6).  So
the components *are* reachable.  What fails is the coupling: **`χ·sinh²η`,
observer-boost-dependent and second-order**, never the universal `1/(4ν)`.
On the lattice the traceless charge sign-flips and swings two orders of
magnitude with source shape and spacing at fixed dimensionless geometry
(`δK(T_xx − T_yy)` from `−3.3×10⁻³` to `+2.0×10⁻⁴` under matched-depth
refinement).

Four obstructions converge and **reduce to one root**: non-universality;
**type I, no area operator** (the record algebra is finite, so `δÂ` is a
c-number; `‖[Â,a]‖ = 0` against `0.8` for an outer control — and the
SHARD-native rescue, crossing by the entropy-production arrow, is genuinely
outer (`‖[L,a]‖ = 1.76 ≠ 0`) yet its Connes cocycle is **trivial** (ratio
set `{1}`), so the crossed product is semifinite, i.e. type I again —
tracial residual ≈ 10⁻¹⁷, isotropic capacity `c₂/c₀ ≈ 10⁻¹⁶`); **Berry**
(zero `cos 2θ` overlap at first order); and **null-cut** (the null
contraction carries the traceless stress at `O(1)`, coefficient ½, *not*
`sinh²η`-suppressed — but the universal-2π null-cut pricing **is** the
half-sided modular inclusion `[K,P] = iP`, which has **no
finite-dimensional representation**; on the lattice the null-direction
traceless charge sign-flips `−0.19 → +0.58` with 6.3× shape spread).

> **The single root:** every spin-2 / area-operator route needs the
> universal structure — outer modular flow, type III₁, a half-sided
> inclusion — that lives *only* in the continuum local algebra, which the
> finite record lattice cannot host intrinsically.  So **"9/9 in principle"
> is empty**: the principle is exactly the continuum the lattice provably
> lacks.  SHARD's emergent geometry is **spin-2-active but not-a-graviton**
> (3.4× shape spread, axis-locked, refinement-unstable); it evades
> Weinberg–Witten the way induced gravity does — no flat-space graviton
> S-matrix — but no derived graviton exists.

**C2.6 The Jacobson–Clausius CONDITIONAL, and the internal asymmetry.**
From `v7/…-paper17-three-walls-classification-theorem.md` (and restated in
`v8/…-paper3-walls-classification.md` §1), four named premises carry the
equation-of-state route:

1. **the Jacobson–Clausius premise itself** — that `δQ = T dS` over all
   local horizons *is* the equation of state of spacetime; the locus of
   Padmanabhan's "**interpretation, not derivation**" critique;
2. **axiom (R)** — the value `β = 2π`;
3. **local equilibrium `θ = σ = 0`** — Eling–Guedens–Jacobson: dropping it
   forces the dissipative `f(R)`/Lovelock branch, so the premise is
   **load-bearing, not decorative**;
4. **the continuum focusing gate `θ′ = −R_kk`** — reduced to two *native*
   conditional gates (a finite double-null affine-pair readout; cofinal
   tightness / no silent refinement).

> **THE INTERNAL ASYMMETRY, load-bearing.**  The **weight-counting no-go
> depends on NONE of these** — it is the structural half.  What rides the
> Jacobson route is only the **identification** of the missing
> weight-carrying unit with gravity's `G`.  So: *"the `G` **leg of the
> classification** is conditional" is precise — **the wall stands
> unconditionally, the `G`-naming of it is conditional.**"*
>
> The corpus's own headline is therefore **two structural no-gos plus one
> conditional**, "never a clean threefold all-experiment-fixed symmetry".
> (The Verlinde-targeting critiques — Visser, Kobakhidze — **explicitly
> exempt** Jacobson and are *not* the locus of this conditionality.)

**The three walls, for the record** (`v7` paper 17, receipt
`p17_classification.py` **23/23**, sympy-exact + mpmath dps = 140): one
quotient-by-internal-symmetry shape instantiated three times —

| wall | group | residual | epistemic status |
|---|---|---|---|
| **SCALE** | `g_λ`, length relabeling | the absolute length, hence `G` — continuous `ℝ₊` | genuinely **MEASURED**, but the route is **CONDITIONAL** |
| **TENSOR PRODUCT** | `R`, field reduction (complex ↔ real) | the local-tomography bit `∈ {0,+1}` in `ker R` — discrete binary | **CONTESTED** convention, possibly experimentally unfixable |
| **MODE** | cross-sector re-referencing | which-mass-is-which `∈ {1,3,7}` — discrete label | **IMPORT-FIXED** by measured spectra |

with MODE flagged in-file as the **weaker, analogical** member — `G_3`
*fixes* the discrete label and moves only the continuous per-sector zero,
so that identification is `[STRUCTURAL]`, **not a theorem**.

**And one thing the no-go explicitly does NOT forbid**, which matters for
PART D: the dimensionless gravitational coupling-per-species
`c_m = Gm²/ℏc` is **weight-zero and intrinsic**, therefore **eligible** to
be a record output.  *So the records cannot fix the absolute scale of
gravity; whether they fix its dimensionless strength is a separate,
still-open question.*

> **Cross-reference.**  This chapter is why PART D's Einstein-dynamics
> arrow is `[PARTIAL]` rather than `[OPEN]`: **the corpus already owns the
> form**.  It is also why chapter A10 §A10.7's laboratory bridge is
> blocked on a free record scale — the un-fixability proved here is one of
> the four holes in that slot.

---

## C3. Quantum foundations results

### ① PLAINLY

Five results from the earlier corpus, all of them negative or
constraining, and all of them the kind of thing a programme usually does
not advertise.

**1.  Sealed holonomy cannot produce revivals.**  A natural hope: if the
world is made of sparse irreversible commitments rather than continuous
classical noise, then coherence should sometimes *come back* — the
signature that memory is real.  A short calculation kills it.  Any
commitment rule that fires irreversibly, at a rate that does not look at
the system's own coherence, gives a decay that is **monotone** — it can
never come back up.  Revivals require either genuinely reversible dynamics
(nothing committed) or a commitment rule that reads the coherence, which
the programme forbids for independent reasons.

Worse for the hope: the distinctive **Gaussian shape** of the early decay,
widely read as evidence of memory, is reproduced *exactly* by the simplest
memoryless commitment rule with a ramping hazard.  **The shape is not a
signature.**

**2.  Gravitational decoherence does not certify its mechanism.**  Push
this to its sharp form and you get a genuine undecidability theorem.  A
continuous classical-noise picture and a matched sparse-commitment picture
produce **bit-identical** predictions for the standard experiment — not
approximately, identically, at every order.  Multi-time experiments
(echo-type protocols) can probe whether the process is reversible; but the
structural property that would mark a genuinely quantum-gravitational
record process is **invisible to any passive measurement of the system
alone**.  And the obvious fix — an invasive protocol that reconstructs the
transition law directly — inserts a commitment at every conditioning step
and so cannot certify the *un-intervened* process.

**3.  Indivisibility does not evade Bell's theorem.**  The programme's
slogan — "local in space, non-locality in time" — was tested against the
thing it might be hoped to buy.  It does not buy it.  Non-Markovianity is
not a loophole; it is the *mechanism* by which this kind of ontology pays
one specific Bell price: it violates **outcome independence**.  The result
is that the theory sits at exactly orthodox quantum mechanics' locality
status.  That is a genuine interpretive package — but it is a
**relocation** of the non-local content, not an **evasion** of it.  The
paper says so in its status line, against interest.

**4.  Indivisibility is not the resource that makes quantum computers
fast.**  The natural conjecture — that the programme's central structural
property is what quantum computation exploits — was tested and is **false**.
The known resource ("magic") is a *strictly finer* property.  The corpus
lists this as a standing bound on its own thesis.

**5.  Discreteness rescues covariance for the kinematics.**  One place the
earlier corpus wins.  Collapse-type theories usually need a preferred
slicing of spacetime, which is a serious problem in a relativistic world.
If instead the commitment events are *sprinkled* the way causal-set theory
does it — randomly, with a density and no lattice — then the whole
kinematic layer becomes covariant: the sprinkling is statistically
Lorentz-invariant, the arrow of time reads a frame-independent causal
order rather than a slicing, and the classic localization obstruction
dissolves because what is localized is an *event*, not a state.

That is a real conversion of a wall into a residue.  What remains open is
the *dynamics* for interacting fields with variable particle number — and
the corpus adds two sharp obstructions there that are worth knowing.

### ② THE OBJECTS

**C3.1 Sealed holonomy: the revival no-go** (`v6/…-paper56-…`, a
**program/roadmap paper** whose own status line reads "**Nothing here is
claimed proved**", with tags `[TARGET]`/`[BUILD]`/`[CONSTRAINT]`/`[OPEN]`).
Its one **computed** result:

> A state-independent **ramping** seal hazard `λ(t) = a t` reproduces the
> Gaussian onset **exactly** (`|ρ₀₁(T)| = e^{−aT²/2}`), so the Gaussian
> shape is *not* a non-Markovian signature; but **any** state-independent
> irreversible seal gives `|ρ₀₁(T)| = e^{−∫λ}`, monotone, hence
> **CP-divisible — it can never produce revivals.**

Revivals require either reversible information-returning dynamics (no
committed record) or a seal that **reads the coherence** — the forbidden
nonlinear state-dependence.

**The leak is kernel-specific, not Gaussianity-specific.**  The DP-family
Ornstein–Uhlenbeck kernel `K(s) = σ² e^{−|s|/τ_c}` has
`∫₀ᵀK = σ²τ_c(1 − e^{−T/τ_c}) ≥ 0`, so `γ(T) = (2σ²τ_c/ℏ²)(1 − e^{−T/τ_c}) ≥ 0`
— genuinely CP-divisible.  But the equally positive-type **underdamped**
kernel `K(s) = σ²e^{−|s|/τ}cos(ω₀s)` gives `γ(T) < 0` on sub-intervals once
`ω₀τ ≳ 3.64`, producing revivals — with the boundary computed exactly in
Paper X as **`ω₀τ = 3.644173671645632…`**.

**Three inequivalent senses of "Markovian", and they are ORTHOGONAL axes:**
(1) constant-rate semigroup — the DP-family model is *not* this; (2)
**CP-divisible** — it **is** this, hence "Markovian" operationally; (3)
Markov embedding — it **has** one (1-D Ornstein–Uhlenbeck).  Therefore:

> **CP-divisibility and Barandes-indivisibility are independent axes;
> non-CP-divisibility is neither necessary nor sufficient for crossing the
> structural barrier.**  (A closed unitary qubit is Barandes-indivisible
> yet, as a channel, trivial.)

**C3.2 Paper X — the undecidability theorem**
(`v6/publishable/paper-X-gravitational-decoherence.md`, receipt
`code/v6_pX_decoherence_undecidability_receipts.py`, all numerics at
mpmath dps ≥ 80).  Three results `[THEOREM]`:

1. **The Gaussian onset is not a signature** (as above; residual `0`), and
   a *constant* hazard gives the pure exponential semigroup — the most
   Markovian channel there is.
2. **Any state-independent irreversible seal is CP-divisible.**
3. **Operational undecidability from the dephasing curve.**  A continuous
   Ornstein–Uhlenbeck classical-noise ontology and a matched sparse-seal
   record ontology produce **bit-identical** free-induction coherence for
   all `T`: the identity `∫λ_OU = χ` is **sympy-exact**, and an independent
   numerical integration gives
   **`max|C_OU − C_seal| = 7.1×10⁻¹⁰²`**.

Multi-time dynamical decoupling (echo/CPMG) *can* probe reversibility.  But
the genuine content — whether the matter's **closed-system** record process
is indivisible/unrefinable — is **structural** (the off-diagonal support of
the decoherence functional between sparse commitments) and is *invisible to
passive reduced-channel measurement, at every order*, because a bath
dilation is always divisible and a closed unitary system is indivisible yet
a trivial channel.  And an invasive protocol reconstructing `Γ(t)` "would
insert a seal at each conditioning step, and so cannot certify the
unintervened process."

**The Diósi–Penrose reconstruction, for orientation.**  DP gives a
short-time exponential `e^{−T/τ_G}` with `τ_G = ℏ/E_G`; finite-memory
variants give the **Gaussian onset** `e^{−½(T/τ_G)²}` crossing over to the
DP slope at `T ≫ τ_c`, and the division-event model pins
**`τ_c = √e·τ_G ≈ 1.65 τ_G`**.  The paper's verdict on the widely used
kernel: *"one illustrative CP-divisible member of the undecidable class
rather than a discriminating prediction."*

**The Tier-1 structural functor `[OPEN]`.**  Constructible via the
Gell-Mann–Hartle decoherence functional: "Chapman–Kolmogorov ⟺ refinable"
is the medium-decoherence consistency condition, so *SHARD-unrefinable ≡
Barandes-indivisible* is constructible at the kinematic level — **the
gravitational realization is the open part**.  The one genuinely open
question is whether the gravitational decoherence functional has
**non-trivial off-diagonal support between sparse seals** — a computation on
the functional, not on the coherence.  An `O(1)` interference window exists
at the physical closure `κ ~ 1`, "but that closure is an ansatz, not
forced."  One diagnostic worth naming: the bimodal `δE = ±σ_E` limit gives
`C(T) = cos(σ_E T/ℏ)`, a discrete-record oscillation distinct from a smooth
Gaussian echo — *a diagnostic to look for, not a definition of the
barrier*.

**C3.3 The Bell verdict**
(`v5/relativistic-isp-v5-paper14-non-markovianity-and-bell-nonlocality.md`).
Its status line, quoted:

> "This paper investigates a single sharp question — whether the
> non-Markovianity (indivisibility) of ISP lets it *evade* Bell nonlocality
> — and reaches a deliberately honest, two-sided answer.  **It does not
> claim ISP defeats Bell's theorem.**  The conclusion is: non-Markovianity
> is **not** a Bell loophole; it is the *mechanism* by which a
> single-history, configuration-realist, no-collapse ontology pays one
> specific Bell price (violation of **Outcome Independence**).  ISP
> therefore lands at **exactly orthodox quantum mechanics' locality
> status** — no-signalling, parameter-independent, outcome-dependence —
> re-described as 'nonlocality in time.'  That is a genuine and attractive
> interpretive package, but it is a *relocation* of the nonlocal content,
> not an *evasion* of it."

`v6` paper 40 §7 carries it as **standing bound 1** on the whole thesis:
*"indivisibility does not restore outcome independence.  The smooth law is
exactly as Bell-nonlocal as quantum mechanics, because it **is** quantum
mechanics in record form."*

**C3.4 Magic ≠ indivisibility.**  `v6` paper 40 §7, **standing bound 2**:
*"Tested and published: **magic = Wigner negativity is strictly finer than
indivisibility.**  The thesis lives on the dynamics/geometry/thermodynamics
side, not the resource-theory side."*  Paper 26's qutrit receipts carry the
measurement: stabilizer states nonnegative, **the magic state at `−1/3`
exactly**, cost compounding as `(Σ|W|)^{2n}`.

**C3.5 Born = K1, and the Born/signature paper.**
`v6/publishable/paper-Va-foundations-1.md` — *"Quantum theory from sealed
records I: Born composition, Lorentz signature, and the arrow of time"* —
states results **at declared scope and with declared hedging**, quoted:

- **(i) the Born layer** — "record weights compose through square roots,
  and the tame-class reconstruction **is argued to** recover the Weyl
  algebra and to land in the Schrödinger representation via the
  Stone–von Neumann import, from record towers (at tame scope: the
  tame-class definition with its growth constants and the boundary
  classification are corpus-bound `[P]`)";
- **(ii) Lorentz signature** — "the commitment structure of records **is
  argued to select** a Lorentzian `(1,d)` split with derived orientation
  classes (a structural argument from the commit-order asymmetry)".

> **The self-containment caveat, verified by count.**  Paper Va carries
> **22** `[P]` tags — corpus-bound pointers to results that live outside the
> submission (`grep -c "\[P\]"` = 22).  **It is not self-contained**, and
> that is a property a reader must carry when citing it.

**And the v10 echo.**  In v10, paper 31 §4.3 constructs an isometric family
`{V_single, V_pair}` — acceptance composed with the join-typed opening
click — for which **the squared branch amplitudes of `V_pair` are exactly
`1/2`–`1/2`, "the `K1` law on the 2-conflict, recomputed from the layer"**,
`V_single` deterministic, both isometric (defect `0.0`; isometries at
`1e−40`), and the committed menus reconstructed **exactly in rationals** at
both cuts (`1/4` early; `1/4 + 1/8 + 1/8` at the join) from *the same
matrices* at both cuts.  The randomized escape class is excluded by a
visibility theorem.  So "Born = K1" is a phrase that occurs on both sides of
the corpus — **and §C5 is where the honest statement of what that does and
does not establish belongs.**

**C3.6 Covariantization by discreteness** (paper 57 §5.1, verified; the
substrate is `v6/…-paper1-indivisible-causal-set-gravity.md`).

*Discreteness covariantizes the kinematics* — three verified components:

1. A **Poisson sprinkling** of division events is statistically
   Lorentz-invariant (Bombelli–Henson–Sorkin: nearest-neighbour spacing CV
   flat across boosts, **no recoverable frame**, whereas a regular lattice
   **is** frame-recoverable) — with `s²` boost-invariant to **10⁻⁹⁷**.
2. The entropy-production arrow `σ = D(P_AB ‖ P_BA)`, defined as *"what is
   committed at an event = its causal past"*, reads the **frame-invariant
   causal partial order**, not a preferred slicing: **`0/3200` mismatches**
   for the causal past under boosts, while a constant-time-slice past
   changes for **every** event.  **So the arrow needs no foliation.**
3. **Hegerfeldt dissolves** for the free flash: a flash localizes a
   point-*event* sampled from a density, not a positive-energy *state*, and
   Hegerfeldt forbids only the latter.

*The GRW/CSL foliation wall becomes covariant residues.*  Coverage by
regime: free / single-particle-distinguishable — **covariant** (Tumulka
2006); **interacting-distinguishable — solved** (Tumulka 2020); the genuine
open residue is a **covariant interacting *field* (variable particle
number) indivisible beable**, where a Branch-B *candidate* exists (paper 1
§5: a microcausal `Q̂ = ½α:φ²:` collapse model; cf. Bedingham) — so the wall
reduces to the sharp "dangerous pair": whether a state-dependent
mass-localizing seal can be covariant *and* localized enough to source
point-gravity without re-triggering the nonlinear-collapse / Hegerfeldt
no-go at spacelike separation.

**Two further obstructions on the dynamical side, both sharp:**

- **η-exactness ⟺ a preferred foliation exists.**  Curl-freeness of `η` is
  frame-invariant (`dη` is a 2-form), and the physical current
  `η_μ = w·u_μ` is an exact gradient **iff** the flow is irrotational
  (`u ∧ du = 0`) **iff a global preferred foliation exists** (sympy-exact;
  a vortical flow has `u ∧ du ≠ 0` in *every* frame).  So η-exactness does
  not *remove* a preferred foliation — **it is equivalent to having one**,
  and for vortical matter the `Λ`-flow is genuinely multivalued.
- **Exactness and the falsifier are mutually exclusive.**  By Hodge, only
  the exact `dχ` part of `η` feeds `Λ`, while the decoherence source — the
  programme's sole empirical falsifier — is the **co-exact transverse**
  part; exact ⊥ co-exact in `L²`, so **forcing `η` exact zeroes the
  decoherence power identically.**

> **The honest status line, quoted:** *"discreteness covariantizes the
> kinematics outright, the interacting-distinguishable dynamics is done,
> and the interacting-field dynamics is the `[OBSTRUCTED-leaning]` wall —
> SHARD has the thermodynamics of gravity and a covariant kinematics, not
> yet a covariant interacting-field dynamics."*

**C3.7 The publishable batch.**  Four of these results were packaged for
external submission and put through an eight-round hostile-review campaign:
the graded local Weyl law (`paper-IV-graded-weyl.md` — *"Hearing the
regularity of a diffusion coefficient: a graded local Weyl law with a
constructive converse"*), the Born/signature foundations paper (Va), the
gravitational-decoherence undecidability paper (X), and the causal-set
gravity paper.  **Va's 22 corpus-bound tags are the standing caveat on that
batch.**

---

## C4. The consolidations and the spin-offs

### ① PLAINLY

Two things happen to a research corpus that grows fast: it accumulates
results faster than it can keep them consistent, and it accumulates
*claims* that were true when written and have since been narrowed.  The
earlier corpus dealt with both by two large consolidation exercises and by
spinning off the parts that had become independent.

**v7** produced eighteen papers and was then **frozen**: no further
corrections land there.  **v8** did the consolidation proper — fifty-one
papers were rewritten into **six**, plus a single authoritative ledger that
maps every result to its owning paper, its receipt, and its honest status.
The rule adopted at that point is the one this document has been quoting
throughout: *corrections land in the ledger and the new papers only, never
in the frozen log*, because the recurring failure mode was receipt-level
corrections silently drifting out of sync with the papers citing them.

The consolidation was then attacked.  Six independent referees produced
**74 findings** across the six papers — and **zero of them were false
results**.  Every serious finding was a transcription, notation, or
attribution defect.  A follow-up confirmation pass found twelve residual
defects, repaired the same day, and graded the set **CONFIRMATION-PASSED**.

And then the honest coda, recorded in the ledger rather than buried: item-
level fidelity is complete, but the *style* — certainty carried by
receipts rather than by written proofs, sketch-grade arguments for several
core theorems, no displayed-equation-and-lemma structure — **would not pass
a human journal referee**.  A proof-carrying upgrade is described, costed,
and explicitly **not yet approved**.

**The spin-offs.**  Two lines outgrew the physics programme.

The **Yang–Mills** line ran for dozens of papers across two version lines
and produced a standalone construction paper.  Its own status line is the
interesting part: it says, in its header, that it is **not an unconditional
proof** of confinement or of the mass gap, and it isolates the five
clauses that would have to be discharged.  An errata ledger then records
that an earlier "CLOSED" headline was **reopened as conditional** by the
papers that followed it — the reduction now bottoms out in one named open
analytic input, classified as an open research programme.

The **Walsh–delta** line produced something else entirely: a clean, fully
stated combinatorial theorem that has nothing to do with physics, has been
**formally verified in a proof assistant** except for one finite
computation, and now lives in its own repository.  It is the corpus's one
unambiguous mathematical export.

### ② THE OBJECTS

**C4.1 v7 — frozen** (`v7/ARCHIVE-STATUS.md`, quoted):

> "This directory is the v7 research log, **frozen as of 2026-07-01** …
> superseded by the **v8 consolidation**.  The authoritative map of every
> result, receipt, status, and supersession is `../v8/LEDGER.md`.
> Corrections after this date land in v8 and the ledger **only** — not
> here.  (The recurring failure mode this policy ends: receipt-level
> corrections silently desyncing from the papers that cite them.)"

Known text-side items deliberately **not** fixed at the freeze, and
declared: paper 1's abstract premise-ledger; the `σ`/`κ` terminology
unification; the orphaned-receipt homes; paper 18's fresh multi-referee
review.  Eighteen papers are terminal on that line; among them the
three-walls classification theorem of §C2.6.

**C4.2 v8 — the consolidation** (`v8/LEDGER.md`).

- **Target structure:** *"51 papers → 6 + this ledger"* (§ heading,
  verbatim).
- **Objective, redefined 2026-07-01:** v8 must be **fully self-contained
  with respect to v7** — *"v7 is kept for logging only and v8 must be
  usable as if v7 were deleted"*; every worthwhile v7 result, derivation
  and honest negative moves into v8 **at full fidelity — "not compressed,
  just better"**.  v6 is **kept** and may be cited.
- **Phase C:** the cited receipt canon (**66 `.py` + one `.npz`**) copied
  into `v8/code/`, all six papers repointed, canon run green **66/66**.
- **Phase D (the hostile round):** six independent referees; **74 findings
  total (7 MAJOR / 41 MINOR / 26 NIT), ZERO false *results*** — *"every
  MAJOR was a transcription/notation/attribution defect, none a wrong
  theorem"*.  All seven MAJORs hand-verified before applying (standing
  rule); receipts touched by fixes re-run green.
- **Confirmation pass (2026-07-02): COMPLETE, all six papers.**  Six
  focused referees re-verified every applied fix and hunted collateral
  damage; **12 residual defects found, all repaired same date**.  **Set
  grade: CONFIRMATION-PASSED.**
- **The honest coda, verbatim from the ledger:** *"Remaining before external
  use: the user-flagged **referee-grade gap** — item-level fidelity is
  complete, but the corpus style (receipt-carried certainty, sketch-grade
  proofs for several core theorems, v6-resident proofs, no
  displayed-equation/lemma structure) predates v8 and **would not pass a
  human journal referee**; a possible **Phase E** (proof-carrying upgrade …
  papers grow ~2–3×, paper 2 likely splits) is **ON THE TABLE, not yet
  approved**."*

**One clarification a reader will need.**  "51 → 6" is the *consolidation
target structure* — the rewrite of the frozen v6+v7 corpus.  The `v8/`
directory subsequently grew **papers 7–17** as *new* research on top of
that consolidated base, so the directory listing and the headline figure
are not in conflict; the six are the consolidation, the rest are what came
after it.

A second confirmation pass over papers 7–15 (three referees, every receipt
re-run green) records the same shape — *"zero false results, zero broken
receipts; all residual defects transcription/staleness-class"* — plus a
recurring lesson this document has already met once in v10:

> *"fixes claimed in a corrections entry MUST be verified landed in the
> same pass — two items were written to the ledger but not to the files."*

That is the **same defect class as v10's #420** (a ledger entry claiming a
delta that had not landed).  It has now been caught twice, in two different
version lines, by two different mechanisms.

**C4.3 The Yang–Mills line.**  Spanning `v3` papers 11–22 (continuum
Yang–Mills, RG closure, mass-gap gates, confinement area law) and `v4`
papers 28–45.  The standalone artifact is
`v4/relativistic-isp-v4-paper39-standalone-ontology-free-yang-mills-proof.md`
— *"Standalone Record-Complete Yang-Mills Construction And Confinement/Gap
Reduction"* — whose own header states the scope:

> "**Conditional status:** the construction is **not an unconditional proof**
> of four-dimensional Yang-Mills confinement or mass gap.  Subsection
> 10.28g isolates the five C0 clauses: uniform bounds across packets (U),
> large-field control …"

and, on external status: *"Community-level acceptance requires checking the
record-complete construction and the printed margin certificate."*

`v4/ERRATA.md` E1 then records the reopening explicitly:

> The Yang-Mills descent **"CLOSED" claim** of paper 30 is **reopened as
> conditional** by papers 39–45: paper 39 is explicitly "not an
> unconditional proof"; paper 40 **reduces the fixed-IR confinement route
> to the open analytic input `H_3sec(R, ζ_R)`** and "does not prove full
> continuum Yang-Mills confinement"; paper 45 **classifies `H_3sec(R, ζ_R)`
> as an open research program.**

`v3/ERRATA.md` E1 records a structurally identical retreat one line
earlier: paper 23's "clean conditional closure" framing is superseded by
paper 25's **Theorem 16.8** (a five-option truth-status theorem) proving
*"the current v3 corpus supplies **none** of the five same-law sources and
neither proves nor falsifies any of the five Branch-A options"*, with
Corollary 16.10 freezing the reduction to explicit new data.

Both errata ledgers open with the same discipline: *"All entries are
additive; no frozen text has been modified in place."*

**C4.4 Walsh–delta — the mathematical spin-off**
(`~/workspace/walsh-delta/`, its own repository: paper, Lean formalization,
certificates).

- **Setup.**  Fix `n ≥ 2`; `G = {±1}ⁿ`, `N = 2ⁿ`, `U` uniform.  For each
  nonzero `a` there is a Walsh character `χ_a(s) = (−1)^⟨a,s⟩`; an
  **orientation** is a sign choice `ε_a ∈ {±1}` per character, defining the
  Gibbs law `P_ε(s) ∝ exp(Σ_{a≠0} h_a ε_a χ_a(s))` with magnitudes pinned
  by the **self-calibration** fixed point `𝔼_{P_ε}[ε_a χ_a] = e^{−h_a}`.
  The paper proves this system has **exactly one** solution for every sign
  choice, via strict convexity and coercivity of a single objective.
- **Theorem 1.2 (main).**  The relative entropy `m̂(ε) = D(P_ε ‖ U)` is
  minimized — **strictly, and uniquely up to the natural `N`-element
  symmetry orbit** — by the **delta orientations** `ε_a = −χ_a(s⋆)`, whose
  calibrated law is uniform on `N−1` points and nearly extinguishes `s⋆`.
- **The engine (Theorem 6.1, a quantitative dichotomy).**  Any *non*-delta
  calibrated law with `D ≤ 1/60` must extinguish **at least three points**
  down to depth `e⁻⁵`, forcing
  `N·D ≥ 3ψ(e⁻⁵) = 3(1 − 6e⁻⁵) > 2.878716` (with `ψ(x) = x log x − x + 1`),
  while the delta value satisfies `N·D_δ < N/(N−1) ≤ 64/63`.  **For
  `n ≥ 6` (so `N ≥ 64`) the two bounds cross and close the theorem
  analytically**; for `n ≤ 5` the margin is verified by certified
  computation (§8).
- **Not a photo-finish:** the best non-delta family known satisfies
  `N·D → 4 log 4 = 5.545…`, **conjectured** to be the sharp runner-up
  constant.
- **Rigour infrastructure:** the tight constants (`2.878716`, `1.244163`,
  `64/63`) are discharged by **exact interval arithmetic**; the Lean 4 +
  Mathlib formalization has **7 of 8 modules kernel-verified with no
  `sorry`**, and the headline `theorem_1_2` is **proved modulo exactly one
  finite computation**.
- MSC 2020: 94A17 primary.  *"The self-calibration fixed point appears to
  be new; its nearest relatives are Littlewood ±1-polynomials and
  self-consistent-field equations."*

> **Numbering note.**  This result is sometimes referred to inside the ISP
> corpus as "Theorems E + F".  The standalone repository numbers them
> **Theorem 1.2** (the minimizer) and **Theorem 6.1** (the dichotomy
> engine).  This document uses the repository's numbering, since that is
> the artifact a reader would open.

---

## C5. The lineage question, honestly

### ① PLAINLY

Here is the question a careful reader will have been holding since page one
of Part C: **is the v10 theory of Part A and Part B the same theory as the
sealed-record programme of C1–C3, or is it a different theory by the same
author?**

The honest answer has three parts.

**What is established.**  It is one programme, continuously.  Same author,
same ledger discipline, same insistence that a claim is worth what its
receipt and its hostile round are worth.  The vocabulary descends directly:
the earlier corpus's *seal* — an irreversible commitment that destroys a
coherent phase — is manifestly the ancestor of v10's *click*, and the
axiom "no distinction without a record" is manifestly the ancestor of
v10's insistence that what may happen next depends only on what is already
written.  There is also a **formal compatibility ledger** — a document
that goes result by result through the earlier corpus and states, for each
one, what it supplies to the later work and, crucially, **what it does not
supply**.  Themes recur with real content: the Born weights that appear in
the earlier foundations paper reappear in v10 as the arbitration kernel,
computed from v10's own layer.

**What is NOT established, and this is the uncomfortable part.**  A
strategic sweep of the corpus asked directly whether any of the earlier
laws had ever been *measured* on any of the later objects.  Its finding,
recorded verbatim, is: **the bridge is empty.**  No receipt has ever
measured an earlier law on a later structure.  The postulate that would
identify the two ontologies — "a seal *is* a record" — is exactly that, a
**postulate**, and it has never been instantiated.  And a quantity called
`σ` in the earlier line and a quantity called `σ` in the later line turned
out to be **a name collision** — two different functionals of two different
things.

**What is being done about it.**  A design note specifies the first object
that would be *both*, and the first falsifiable measurement that would test
the identification.  It is careful in exactly the way this corpus is
careful: it identifies in advance that the obvious test would confirm a
mathematical tautology (§C1's universality trap), and moves the falsifiable
content to something that could actually fail.  As of the material read for
this document, **that receipt has not been run.**

So: one programme, one lineage, and — between its two halves — **one
postulate and no measurement**.

### ② THE OBJECTS

**C5.1 What is established.**

- **A formal compatibility ledger exists.**
  `v10/note-d12-v6-v10-compatibility-ledger.md` (*"what the corpus already
  fixes"*, completed 2026-07-11) is a clause map with four columns —
  *object* / *strongest earlier result* / *correct D12 use* / **not
  supplied**.  Sample rows, verbatim in substance:

  | object | strongest earlier result | not supplied |
  |---|---|---|
  | primitive record | V6 P3/P4 sealed finite diamond | between-diamond output support |
  | eventless clock | V6 P4 §71: additive RN/KL evidence `I`, `S(I) = exp(−I)` | mapping to external seconds |
  | dense scalar click face | V7 P1: `S(χ) = exp(−κχ)` under dense seals | realized `κ`, content magnitudes |
  | sparse indivisible face | V7 P1: `S(nd) = S(d)ⁿ` | profile and spacing |
  | whole-history law | V6 P4 §40: complete closed-holonomy cochain reconstructs positive finite `P_D^hist` | intrinsic selection of ledger/support |
  | quantum weight | V6 P4/P5: squared norm selected given linear retained-holonomy composition and screen isometry | **derivation of the composition packet itself** |

  It also **resolves apparent conflicts explicitly** — e.g. `exp(−I)` vs
  `exp(−κχ)` (`I` is the self-accounting evidence coordinate, in which the
  coefficient is one; `χ` is a chosen content coordinate, and converting
  requires physical input), and *"Markov collar versus non-Markov record
  law"* (an eventless collar may admit a reversible Markov presentation
  while the sealed sequence remains indivisible — Chapman–Kolmogorov holds
  at commits and may fail across unsealed intervals).

  **This is a real relation and it is exactly the right kind:** it says
  what transfers and, in a dedicated column, what does not.

- **Shared machinery, concretely.**  The `K1` kernel: v10 paper 31 §4.3
  constructs `{V_single, V_pair}` whose Born weights are **exactly the `K1`
  law, recomputed from the v10 layer**, and reconstructs the committed
  menus at both cuts in exact rationals.  The earlier Born layer (paper Va)
  is the same *kind* of statement — record weights composing through square
  roots.

- **Shared discipline.**  Pin → receipt → hostile round → delta → terminal;
  append-only ledgers; forward corrections only; errata ledgers that are
  additive and never modify frozen text.  Both halves run it, and both
  halves have caught the *same* defect class independently (§C4.2).

**C5.2 What is NOT established — the round-36 finding, verbatim scope.**
From `v9/note-bridge-seal-is-record.md` §1:

> **"THE BRIDGE IS EMPTY: zero receipts measure any v6 law on any web; the
> seal-is-record postulate (v8 paper 6 phenomenology §1.2, `[POSITED]`) has
> never been instantiated; and the two `σ`'s are a name collision.  The v6
> side owns laws about *seals* (the quarter law, v6 paper 26 Thm A); the
> v8/v9 side owns theorems about *webs* (click law, churn, dimension).  No
> object has ever been both."**

The name collision is then dissolved by fiat, which is the right move:

- **`σ_wp` (which-path KL)** `= D(P₀ ‖ P₁)` over readout distributions —
  *this* is the `σ` of the quarter law;
- **`σ_arrow` (arrow KL)** `= D(P_fwd ‖ P_rev)` of a marked commit's local
  transition — *this* is the substrate `σ` of the phenomenology text and of
  the covariance argument in §C3.6;
- *"These are different functionals of different pairs.  The corpus's name
  collision dissolves by never again writing either as bare `σ`."*

**C5.3 The first bridge measurement, specified and not yet run.**  The same
design note pins what would actually test the postulate, having first
disqualified the obvious test:

- **Gb1** — the ¼ ratio, gated **only as instrument certification**, and
  explicitly **"not the bridge"**, because §C1's universality argument makes
  it measure-theoretic in the weak limit;
- **Gb2 — THE FISHER IDENTITY, the postulate's actual falsifiable core.**
  Seal-is-record says irreversibility and which-path readout are two faces
  of one record event *sharing one Fisher object `J`*.  Test: on the same
  marked commits measure `J_wp` and `J_arrow` under the same contrast dial.
  **The postulate ⇒ the ratio is a fixed, contrast-independent constant;
  independent objects with no shared `J` ⇒ the ratio drifts.**  Drift ⇒
  *"the postulate is REFUTED-AS-STATED for this class (and the v8 §1.2
  elevation is re-graded)"*;
- **Gb4 — covariant readability**, with explicit **kill semantics**: if the
  covariant readout's evidence ratio → 0 as the window grows, *"the marked
  record's content is relabeling gauge, and the postulate as stated dies on
  the web"*.

Status of that receipt: the note is *"the deliverable; its receipt
(`bridge1`, gates §5) is a **later round**, run only after the §6
obligations clear."*  Nothing in the material read for this document shows
it run.

**C5.4 RELATION UNESTABLISHED — the explicit list.**  The following are
**not** established anywhere the author of this document could verify, and
no bridge should be inferred:

1. **The v10 generated grammar is not derived from the sealing formalism.**
   Paper 30 §1.2 marks the grammar `[POSITED]`, and its kernel laws
   `[POSITED as alternatives]`.  Nothing derives the six event types,
   their carriers, or their quarter-budget pricing from axioms R/S/C.
   **RELATION UNESTABLISHED.**
2. **v10's `click` is not proved to be a `seal`.**  The identification is
   the seal-is-record postulate — `[POSITED]`, never instantiated (§C5.2).
   **RELATION UNESTABLISHED.**
3. **The quarter law is not known to hold in v10.**  It is a theorem about
   a monitored qubit's Bhattacharyya overlap.  v10 has no monitored qubit
   and no receipt has tested it there.  **RELATION UNESTABLISHED.**
4. **The v10 completion dichotomy is not connected to the `G` no-go.**
   Both concern something the theory cannot supply from inside — a measure
   in one case, an absolute length in the other — and both were argued by
   an invariance/weight argument.  **That is a resemblance, not a theorem.**
   No unit relates them.  (PART D §D3 records a *labelled speculation* in
   this vicinity; it is labelled precisely because of this row.)
5. **v10's actors are not v6's division events.**  v6's division-event
   causal set is a Poisson sprinkling with a Lorentz-invariant intensity;
   v10's records are worldline-woven and provably **do not** look like
   sprinklings under the one instrument that has compared them
   (§B5.7).  **RELATION UNESTABLISHED — and there is now
   measured evidence they are different kinds of object.**
6. **v10's `sigma` (the local-state abstraction) has nothing to do with
   either earlier `σ`.**  It is a third use of the letter — a state
   abstraction, not an information quantity.  Named here so nobody
   completes the collision.

> **The honest summary.**  The two halves of this corpus are one programme
> by construction, history, method and vocabulary — and are joined by
> **one postulate and zero measurements**.  The corpus knows this, wrote it
> down as "the bridge is empty", specified the first measurement that could
> fail, and has not yet run it.  A reader should treat Parts A/B and Part C
> as **two bodies of work in one programme**, not as one theory told twice.
>
> **And there is a second one.**  Chapter **C6** describes the v9 line,
> which stands in the *same* relation to Parts A/B as the sealing corpus
> does — a different formalism, no map either way, and in v9's case a
> user directive that **declares** it not to be the interactive click law.
> So the honest count is **three bodies of work in one programme, joined
> by two unbridged postulates and zero cross-measurements.**
>
> **The corpus's fourth relation is of a better kind, and it is worth the
> contrast.**  Between the grammar of Parts A/B and the *identified* law
> of §B2.9 there is no unbridged postulate: there is a **named missing
> map**, stated in a paper, with a partial crossing already proved and
> its failure mode exhibited.  That is what an unestablished relation
> looks like once someone has done the work of stating it — and it is the
> shape the two relations above still lack.
---

## C6. The v9 channel-manifold arc — the other road to the manifold

*Sources: `v8/LEDGER.md` entries **#103–#128** (v9's ledger lives in the v8
file); `v9/LOG.md`; `v9/note-3p1-dimension-ledger.md`,
`note-3p1-cladder.md`, `note-3p1-manifoldweb.md`,
`note-3p1-conservation.md`, `note-3p1-nladder.md`; `v9/PLAN.md`.*

> **TWO STANDING FACTS THAT GOVERN EVERY CLAIM IN THIS CHAPTER.**
>
> **(1) The line's final rounds carry a funded external review, and it
> narrowed them.**  Rounds 46–48d ran in NO-REVIEW MODE and were then
> reviewed (**LEDGER #125**): the headline **PARKED** is graded
> **PARKED-AT-PROTOCOL**, and the word **"ROUND" is corrected**.  Every
> number below is the post-review statement.
>
> **(2) The v9 line is CLOSED, by user directive** (LEDGER #128),
> verbatim: *"stop the v9 review, as v9 actually didn't use a real
> interactive click law."*  The binding scope statement recorded with it:
> **the v9 builders are exploratory record-SUBSTRATE dynamics — they are
> NOT the identified interactive click law**, and the v9 geometry results
> stand as **closed historical measurements about toy record
> substrates**.  The review's O1–O5 queue "remains recorded in this LOG
> but is **NOT scheduled**."
>
> So the mandatory queue this chapter quotes is a queue **nobody is
> working**, on a line that is **closed**, about objects **declared not to
> be the corpus's click law**.  Read every result below through that.

### ① PLAINLY

While the v10 line was building a grammar and worrying about its measure,
a **completely different formalism** was being pushed at the same target
from the other side. It is worth understanding, because on the specific
question of *building something four-dimensional* it went considerably
further than v10 has.

**The objects.** Instead of actors writing versions, v9 has a **fleet of
slots** — thousands of little accumulators. Growth proceeds by
**commits**: at each step one slot fires and **deposits** something into
its accumulator. Periodically a slot is **churned** — its accumulator is
reset, or (later) transferred, or (later still) leaked away gradually.
The causal order is then read off by *dominance*: one commit precedes
another if it is earlier **and** behind on every one of a set of clocks.

**The wall.** That construction has a fatal built-in limit, and it was
proved rather than discovered: if the order is "earlier and behind on
*k* clocks", then it can be reconstructed from *k* linear orders, so its
complexity is bounded by *k*. With two clocks you get exactly
two-dimensional causality — which is exactly flat spacetime with one
space dimension. **Every earlier failure to see higher dimension was
therefore structural**: the instruments were pointed at things that
could not carry it.

**The escape.** So: add clocks. Give each commit several independent
channels, and dominance means behind on all of them. Now the bound grows
with the number of channels. And this is where the arc's real content
begins, because it turned out that **getting a high-dimensional order is
easy and getting a *round* one is very hard.**

Real spacetime's light cone is **round** — a smooth cone of directions.
An order built from a finite set of clocks has a **polyhedral** cone,
with corners. The programme spent five rounds trying to round it off:
more channels, mixing the channels, rotating the frames, tuning dials.
Roughly sixty measured configurations. Every single one either stayed
cornered or paid for roundness by collapsing back to two dimensions.
**No configuration was both.**

**Then someone noticed the target had been impossible all along.** A
round cone with finitely many facets does not exist. The thing being
chased could not be built, and the universal no-go was guaranteed in
advance. That is a genuinely useful discovery: it converts five rounds of
failure from evidence about the theory into evidence about the question.

**The reframe, and it is the chapter's centre.** If a *count* of channels
gives you corners, then the channels should not be indexed by a count —
they should be indexed by a **manifold**. And then the dimension of
spacetime is the dimension of that manifold plus two. For our world the
channel space would be the **sphere of directions** — the celestial
sphere — and the question "why three channels?" is replaced by the much
better question **"why the sphere?"**. A quick probe confirmed the
mechanism works: with clocks pointing in enough directions on a sphere,
the cone reads round.

**Then the hard part: can *growth* get there?** Four rounds, each
isolating exactly one failure mechanism and fixing it:

1. the resets were **starving** the relation — too many independent
   perturbations knocked the structure apart;
2. fixed, but the clock kernel carried **contaminating harmonics** — the
   wrong shape of "how much does this deposit advance that clock";
3. fixed with a pure kernel, and now a **drift** dominated — the total
   content became a redundant second clock;
4. fixed by removing the drift, leaving a genuinely ballistic relation:
   time is birth order, space is a direction-valued content vector,
   worldlines are straight.

That fourth version looked like it had arrived. **It had not**, and the
review caught it: the apparent success was inside the instrument's own
error bars, could be flipped by a convention choice, and was the minimum
of twelve configurations. A pre-registered re-test on fresh seeds sent
the number back up. **NOT PARKED** — honestly, with the regression
predicted in advance by the reviewer.

But the same re-test banked results that survived everything: those grown
webs are **genuinely four-dimensional by volume** on a purpose-built
calibration with no clamping, carry order-complexity of at least five by
explicit witnesses, and are **round to within about six to nine percent**.
The remaining gap is real structure, not instrument error.

**Then a theorem about matter, and it is the deepest thing in the arc.**
Someone asked what a *particle* would be in this picture. The answer
exposed a hole: in the formalism as built, slots **never exchange
content**. So a disturbance to one slot rides exactly one worldline and
influences nothing else, ever. **No collective excitation can exist at
any scale.** There is no sound, because nothing couples.

That is a theorem, it was verified mechanically, and it is a statement
about what matter *requires*: **coupling**. The named minimal fix — make
the resets *transfer* content instead of destroying it — was then built,
and for the first time in the programme's history **a perturbation moved
between slots**: influence spread from one slot to several. Interaction
exists; matter is possible in principle.

**And then the last rounds, which are the most interesting and the least
secure.** Transferring content in jumps did not round the cone — it just
moved the jumps around. So the jumps were removed entirely: content
**leaks** continuously between slots. That did round it. The best
configuration reads round *and* four-dimensional at once — the conjunction
that sixty earlier configurations had excluded.

**With three large caveats, all from the review that followed.** The
volume measurement is instrument-fragile (it flips under reasonable
protocol changes). The word "round" was **overclaimed** — the honest
statement is that the residual dropped by about 45% and the pre-registered
criterion was met, but the number still sits well above a genuinely round
reference. And one of the two statistical legs survives correction for
multiple looks while the other does not.

**And then the line was closed** — on the grounds that these webs were
never the corpus's actual interactive law. The results stand as honest
historical measurements of a toy substrate. The queue of things that would
have secured them is written down and unscheduled.

### ② THE OBJECTS

**C6.1 The formalism, and that it is a DIFFERENT formalism.**

This must be said first and plainly: **the v9 web is not the v10 grammar.**
There are no actors, no versions, no mint chain, no proposals, no
arbitration, no deliveries, no admissibility predicate, no menus and no
weights-summing-to-2. There is:

| object | what it is |
|---|---|
| **slot** | one of `M` accumulators in a fleet; the substrate's unit of locality (typical `(N, M, L) = (2048, 32, 16)` — commits, slots, churn scale) |
| **commit** | one growth step: a chosen slot fires and deposits |
| **deposit** | what a firing adds.  In the channel-manifold builders it is **direction-valued**: slots carry fixed preferred directions `p_s ~ uniform(S²)`; a click draws `u = p_s` with probability `α`, else uniform on `S²`, with magnitude `e ~ Exp(0.109551)` |
| **celestial clock** | one of `K` fixed directions `v_k` on the sphere (a Fibonacci-sphere set).  A deposit advances clock `k` by a kernel of `u · v_k` |
| **churn** | the reset process, rate `1/L` per slot.  Three flavours across the arc: **per-clock** (each clock perturbed independently), **full-vector** (one victim slot's whole vector reset), **conservation** (the victim's accumulator is *added to* a receiver, then zeroed), **diffusion** (a continuous fractional leak, no jumps) |
| **the relation** | dominance: `x ≺ y` iff `b(x) < b(y)` (birth order, strict) and `χ_k(x) ≤ χ_k(y)` for all `K` clocks |
| **`F_iso`** | the shape statistic: standardize, take related pairs, form the transverse cloud `v = w/s`, PCA to an effective 3-frame, take directional supports `h(u)` at `q90` over a pinned 64-direction Fibonacci sphere, and report `mean(top 8 of h) / mean(bottom 8 of h)`.  Round ⇒ ≈ 1 |
| **`d_ball` / `d_MM`** | volume dimension by Myrheim–Meyer, implemented **formula-free** — the ordering-fraction reference curve is *measured* from `M^d` sprinklings and the estimate is interpolation on it.  `d_ball` is the version calibrated against a **dedicated ballistic-class reference** built for the purpose |
| **parking** | the arc's name for the target: **round-occupied AND certified ≥ 4D simultaneously** |

**C6.2 The two-clock wall `[LEMMA, elementary, stated for the record]`.**
From `note-3p1-dimension-ledger.md` §1: if `x ≺ y` iff `f_i(x) < f_i(y)`
for all `i ∈ {1..k}`, then `≺` is the intersection of `k` linear orders,
so **order dimension ≤ k**.  Every corpus web's order was `(b, χ)`-
dominance — `k = 2` — so **`dim ≤ 2` always, by definition**, and 2D
Minkowski *is* exactly two-clock causality.

> **The re-attribution, which is the useful part:** *"every 3+1 readout
> refusal in the T6 track was structural — the instruments were pointed
> at webs that could not carry `d > 2`.  The wall is in the ontology's
> coordinate system, not in the dynamics or the readers."*

The lemma was itself **corrected under review** (round-35, appended not
silently edited): as first stated it covered neither quoted instance,
because the builders' order is `b`-strict ∧ all-`χ`-**weak**, with ties
abundant.  The surviving weak form: *if `x ≺ y` iff `f₀(x) < f₀(y)` and
`f_i(x) ≤ f_i(y)` for all `i`, with `f₀` injective, then `dim(≺) ≤ k+1`*,
with explicit realizers.  `b = arange(N)` is injective in every builder,
so every quoted instance is covered.

**C6.3 The dimension-wall arc and the parking hypothesis (#103–#114).**

The escape route (**R-A**): multi-channel evidence clocks, `dim ≤ C+1`,
**polyhedral** cones.  The registered limit sentence — *"the round Lorentz
cone is the many-channel/mixed limit"* — became the **parking
hypothesis**, user-posed: at large `C`, does *statistical* rounding
(many increments Gaussianize the transverse cloud) let you ride down the
dial to a point that is round **and** ≥ 4D?

The arc, round by round, with its corrections:

- **#103/#104 (round 40).**  The footprint instrument certifies:
  `M4` reads `F ∈ [0.983, 0.999]` against orthant-iid `[1.307, 1.392]`,
  strict 5/5 separation.  Corner webs read `F ∈ [1.949, 2.316]`.
  **Review correction:** the headline "cones have corners / sharper than
  the orthant / slot-chain sharpens" is **SUPERSEDED** — the geometric
  cone is the *same* orthant; what is more corner-concentrated is the
  **occupied cross-section**.  *Occupancy, not geometry.*  Ablation
  (#105): the `α`-preference mechanism is **dominant** (removing it takes
  away ~5/6 of the corner excess); temporal correlation contributes
  nothing (shuffle reads 2.28).
- **#107/#108/#109 (rounds 42/42b).**  The dial sweep: mixing saturates
  at the iid-orthant floor with dimension intact; `α = 1.0` **collapses**
  dimension; **17 dial points**, and the corrected verdict is that the
  trade-off is **continuous** and *"the sweet spot (`F ≤ 1.10` AND
  `win d_MM ≥ 3.7`) is EMPTY across the measured family"*.  Recorded
  honestly: the `d_MM` proxy has **two confound exhibits in opposite
  directions**, so realizer/witness is ground truth and `d_MM` is a
  volume co-signature only.
- **#110/#111/#112 (round 43, the C-ladder).**  New instrument `F_iso`,
  certification-gated (`M4 [1.08, 1.13]` vs orthant-4 `[1.26, 1.34]`).
  **Verdict UNIVERSAL-FRONTIER: no parking at any `C`.**  And the 42b
  "rounding" is **unmasked as cloud collapse** — the transverse cloud's
  `eig3/eig1` falls `0.59 → 0.05` while `F_iso` *rises* `1.82 → 5.26`;
  the native statistic had misread flattening as rounding.  A reference
  card is receipt-carried (Gaussian 1.078 / disk 3.044 / round-plane 2.154
  and 2.584 / simplex-interior 1.557), and equal-split webs sit **between
  Gaussian and simplex-interior: genuinely polyhedral**.  Positive banked:
  **`d = C+1` extends** — `S₅` verified on equal-split `C = 4`, so that
  class has order dimension **exactly 5, witness-grade**.
- **#113/#114 (round 44, rotating frames — the last route).**  The
  pre-registered non-monotone minimum materialized (`F_iso 1.864 → 1.412
  at ω = 1.0 → 1.450 at ∞`) with **no collapse, no sparsification, no
  dimension payment** — the best `(shape, dimension)` point in programme
  history at that time (`1.412` at `d 3.87`).  **THE OBSTRUCTION
  ISOLATED: the conditioning.**  Fixed-frame componentwise dominance
  shapes occupancy to the orthant *regardless of increment law*; round is
  unreachable by increment engineering; changing the **relation** is
  outside the ontology.

**C6.4 The channel-manifold law (#115) — the reframe.**

`v9/note-round-cone-mechanisms.md`, user-directed, rounds stopped:

1. **The target was impossible.**  `M4`'s causal order has **unbounded**
   Dushnik–Miller dimension (`S_n` embeds in `M^{1+d}` for all `n`,
   `d ≥ 2`, by an antipodal construction proved in-note; Meyer 1993:
   Minkowski dimension = order dimension **at `d = 2` only**).  So
   *"round cone AND order-dim exactly 4"* was **a round cone with finitely
   many facets — impossible; the arc's universal no-go was guaranteed.**
   Corrected target: **MM-dim 4 AND round occupancy AND order dimension
   GROWING** — which is what `M4` is.
2. **The mechanism:**

   > **channels indexed by a MANIFOLD, not a count —
   > `d = dim(channel manifold) + 2`; for 3+1 the channel space is `S²`
   > (the celestial sphere), and "why `C = 3`" is superseded by
   > "why `S²`".**

3. **The probe** (analysis-grade, iid, `N = 512`): `K` celestial clocks
   at latent dimension 4 read `F_iso` **1.451 (K=4) → 1.132 (K=8) →
   1.055 (K=16)** against exact-`M4`'s **1.046** — **round by `K ≈ 12–16`.**
   The registered limit sentence becomes true *in corrected form*
   (directional readings of a shared latent space); round 43 falsified
   only the independent one-hot form.

**C6.5 Round 45's four isolated mechanisms (#117/#118), each a controlled
receipt whose wiring byte-reproduces its predecessor before changing one
thing:**

| stage | mechanism found | fix |
|---|---|---|
| **45** | **CLOCK STARVATION** — per-clock churn injects `K` independent perturbations, knocking `χ` off the latent deposit surface; the ordering fraction collapses with `K` (**0.159 → 0.015**; window pairs 2833 → 38) and instruments starve | full-vector churn |
| **45b** | **HARMONIC CONTAMINATION** — the half-cosine kernel `(u·v)₊ = \|u·v\|/2 + (u·v)/2` carries even harmonics `ℓ = 0, 2, 4…` (a 12.5% even tail, confirmed in review), which is latent structure beyond dimension 4; `F_iso` stays flat ~1.7–1.9 | the pure monopole+dipole kernel |
| **45c** | **MONOPOLE DRIFT** — with `χ_k = A + D⃗·v_k`, the accumulated content `A` is a deterministic clock redundant with `b`; occupancy is drift-dominated (`eig3/1` 0.14–0.31, `F_iso` 2.8–3.2 = the card's *collapse* regime, not shape).  *The latent cone theorem holds though:* at `K = ∞`, dominance ⟺ `ΔA ≥ \|ΔD⃗\|` — **the Minkowski cone itself in latent coordinates** | subtract the monopole: `ℓ_k = τ·b + (χ_k − χ̄)` |
| **45d** | **BALLISTIC NEAR-PARKING** — time = birth order, space = the content dipole, matched-variance `τ`; with `α`-persistence, `ΔD⃗ = ΔD⃗₀ + Δw⃗·Δb` — **positions AND velocities, the genuine `M⁴` kinematic form**.  Best point `K=24 / α=.75 / c=.5`: `F_iso 1.267` against a `1.243` parking line | — |

**C6.6 The 45-arc review (#119) — UPHELD AS MEASUREMENT, HEADLINES
CORRECTED.**  All four receipts byte-identical; the wiring chain verified;
all four mechanisms independently re-derived and **upheld**.  Three
corrections:

- **M1 — RETRACTION.  "F IS COVARIANT" is VOID.**  The `ρ = 0.903`
  Spearman that had certified the anisotropy as order-readable was a
  **NaN-rank artifact**: `F_emb` was finite at only 2 of 10 points, and
  the Spearman as coded ranks NaN blocks by index and **returns 0.903
  regardless of the data** — the reviewer reproduced it from an all-NaN
  comparison.  The SVD embedding had never been control-validated.
  **Order-readability of `F` is OPEN, not established** — and it remains,
  per the closing entries, *"the sharpest instrument open"*.
- **M2 — priority claim corrected.**  "First grown webs with witnessed
  order-dim ≥ 5" is **FALSE** — round 43b's equal-split `C = 4` was
  first; and *"growing with `K`"* is **unmeasured** (`S₅` flat at all
  searched `K`, `S₆` unfound, `K < 12` unsearched).
- **M3 — the near-parking headline rescoped.  The 0.024 gap is INSIDE
  systematics.**  (a) the axis convention **flips the verdict** (1.267
  under the dom-diagonal, **1.221 — below the line — under the b-axis**,
  which is the physically natural axis here); (b) it is the minimum of 12
  grid points on shared seeds, at 1.6 SE before multiplicity correction;
  (c) the volume gate was satisfied only by **clamps**.

Also recorded: the **worldline/cone tension** — at the roundest point the
median slot dipole speed is `2.3×` `τ` (worldlines exit the emergent cone)
and 94–95% of same-slot links cross a reset; **and the dials that would
make matter timelike read LESS round.**  This was later **downgraded from
tension to category clarification** by the *particle reframe* (§C6.8): slot
trajectories are the **substrate**, and substrate constituents routinely
move outside an emergent cone with no pathology (the Volovik-class
precedent).

**C6.7 Round 45e (#120) — the pre-registered decision, and what it
banked.**  The arc review's protocol, verbatim.

- **Gate 0** dissolved the convention ambiguity by construction
  (same-pipeline lines: dom 1.236 / m4 1.212).
- **Gate 1, 10 fresh seeds, split-sample `τ`, pre-registered points only:**
  `P0` reads `F_dom = 1.298 ± 0.014` and `F_m4 = 1.237 ± 0.011` —
  **ABOVE both lines at `z = +4.3 / +2.3`.**  The 45d `1.267` was
  **selection plus seed luck — fresh-seed regression, exactly as the arc
  review predicted**; the neighbours confirm.  **Verdict: NOT-PARKED,
  convention-stable, no escape hatches.**
- **The unimpeachable positives:** `d_ball = **3.84 / 3.85**` at `P0/N1`
  **on the dedicated ballistic-class calibration — genuinely
  four-dimensional by volume, no clamps** — with refusals 10/10 and
  `S₄` 10/10.

> **ARC-FINAL:** grown channel-manifold webs are **4D by volume, ≥ 5 by
> witnessed order dimension, and round-coned to within ~6–9%** — and that
> last increment is **real growth structure, not instrument error.**

**C6.8 The free-web influence theorem (#121) — the matter result.**

Exposed by the user's *particle reframe*: particles should be to the web
what **sound is to a gas** — emergent collective excitations propagating
*over* the substrate at scales far above the slot/churn scale — not the
slots themselves.  The corpus "owns fields-ON-webs but has never exhibited
an excitation-OF-the-web."  Then the theorem:

> **THE FREE-WEB INFLUENCE THEOREM.**  The wb-line content dynamics is
> **FREE** — slots never exchange content (deposits are slot-local; churn
> **destroys** rather than transfers; commit choice is exogenous) — so a
> localized perturbation influences **exactly ONE worldline** and **no
> collective excitation can exist at ANY scale** in that ontology.
> **Matter requires slot COUPLING.**

Verified **mechanically** in round 47's control: with destructive churn
and common random numbers, a marked extra deposit alters the snapshots of
**exactly one slot**, on both control seeds.

> **Two scope corrections carried:** the funded review corrected
> *"forever"* — the precise statement is *"influences exactly one
> worldline **until that slot's next reset** (never any other slot)"*
> (restored at LEDGER #127 M1 after being dropped once).  And round 46's
> *"the residual is STRUCTURAL for free webs"* is **power-scoped**: no
> detectable shrink over 16× at ±0.05 power.

**CONSERVATION-CHURN is named as the minimal record-native fix** —
resets that *transfer* content instead of destroying it — which would
simultaneously (i) create interaction/matter, (ii) conserve content, and
(iii) remove the reset-scar residual suspect.  *"The convergence hope and
the matter problem = the same problem."*

**C6.9 Rounds 47–48d (#122–#124), and the review that corrected them
(#125).**

- **#122 (round 47, conservation-churn).**  **PROPAGATION OBSERVED** —
  affected slots `0.6 → 1.2 → 2.2 → 3.6` over `Δb = 64 → 1024`, against a
  control of exactly 1: *"the first time a perturbation has ever moved
  between slots in this framework: interaction exists; matter is possible
  in principle; the influence cone is now a measurable object."*  But the
  cone residual is **INDIFFERENT**: `F_dom 1.344` versus its own
  destructive twin's `1.343` — transfer **redistributes** the jumps
  (the receiver's inward kick replaces the victim's outward loss) rather
  than removing them, exactly as the pin had registered.  **The suspect
  narrows: not destruction but DISCONTINUITY — both churn flavours
  teleport.**
- **#123 (rounds 48/48i, diffusion-churn).**  Jump-free fractional leaks,
  rate-matched: at `g = 0.0625`, `F_dom = 1.197 ± 0.010` — **`z = −3.8`
  below the round line under both conventions** — with healthy
  eigenvalues, refusals 10/10, and **influence reaching all 32 slots
  (full coupling)**.  The scar/discontinuity hypothesis is **confirmed as
  the residual's owner**.  The volume–shape trade along `g`:
  `d_ball 5.65 / 5.25 / 4.70 / 3.92` against `F 1.197 / 1.188 / 1.222 /
  1.255` at `g = .0625/.10/.15/.25` — **round-and-4D bracketed inside
  `g ~ 0.15–0.25`, a one-dial tuning question, unresolved at 5-seed
  power.**
- **#124 (round 48d, the pre-registered decision).**  `g = 0.18`, 10 fresh
  seeds, no re-rolls: `F_dom = 1.203 ± 0.017` (`z = −1.96`),
  `F_m4 = 1.169`, **`d_ball = 4.44 ∈ [3.5, 4.5]`**, refusals 10/10,
  `S₄` 10/10 — **all four conjuncts**.  Graded at the time
  **`[MEASURED, unreviewed]`**, with edges disclosed (`z` and `d_ball`
  near their criteria; the dial value interpolation-informed).

**THEN THE FUNDED REVIEW (#125), which is the authoritative statement:**

> **PARKED is DOWNGRADED to PARKED-AT-PROTOCOL `[MEASURED, reviewed —
> conjunction not instrument-robust]`, and #123/#124's "ROUND" headlines
> are CORRECTED.**

| what the review found | detail |
|---|---|
| **clean** | byte-reproduction ×5; pins and seeds airtight; **the free-web theorem and its control SOUND**; round 47's propagation genuine |
| **the best-supported new result** | *"48's discovery robust — the program's best-supported new result: diffusion collapses the residual `z = −3.8` both conventions"* |
| **volume conjunct INSTRUMENT-SUSPECT** | subsample flip 4.567; window range 4.47–5.71; drift-fair `τ` 3.19; bootstrap `P(in-band) = 0.63`; jackknife **7/10 flips** ⇒ `d_ball = 4.4 ± 0.2`, **protocol-conditional** |
| **an owned failure** | *"the pinned drift disclosure was **NEVER DELIVERED** (owned)"* — `s_D` drifts `1.55×`, the class is **nonstationary**, and that is the mechanism of the volume fragility |
| **"ROUND" overclaimed** | `F_dom` is **`+0.117` (`+6.5σ`) ABOVE the round-reference MEAN**.  *The honest headline: the residual dropped ~45% and the parking criterion was met* |
| **multiplicity** | the `dom` leg passes **only the uncorrected bar** (5th look); **the `m4` leg (`z = −3.24`) survives Bonferroni/5 and is load-bearing** |
| **the queue** | O1–O5 verbatim: **24-seed gated replication; the drift-matched volume instrument, validation-gated; the coupled ladder at `g = 0.18`; the gap-to-mean scan; the bridge pilot** |

**C6.10 The driving chain, and the closure.**

The arc was not planned; it was driven by four questions the author asked
in sequence, and the ledger records the chain explicitly:

> **larger `C`?  →  what is a particle?  →  information can't disappear
> →  are the leaks entanglement / sealing?**

which drove, in order, **the channel-manifold law → the free-web theorem
→ coupling → the jump-free dynamics**.

On the fourth question, `note-3p1-conservation.md` gives a careful
three-layer answer:

1. **Strictly: no bipartite entanglement.**  The webs are classical
   stochastic processes; leaks create correlations-through-shared-history,
   which is classical mutual information.  *"The corpus's own sobriety
   results stand (v5 paper 14's Bell verdict; magic ≠ indivisibility)."*
2. **But leak-to-the-fleet IS the structure of entanglement-with-the-
   ENVIRONMENT — i.e. decoherence — i.e. SHARD's own sealing.**  A slot's
   content dispersing irreversibly into many others is which-path
   information becoming environmental record: **the microscopic mechanism
   of a seal.**  This is *"the missing substrate the round-41 bridge
   design needed"* (§C5.3) — the coupled builder gives the Fisher-identity
   programme its first concrete mechanism.  Graded at #125 as
   **`[POSITED-STRUCTURAL]`**.
3. **The separating signature is MONOGAMY.**  Broadcast/diffusive leaks →
   promiscuous many-party correlations → classical, decoherence-like.
   **Exclusive paired exchange** → the only in-ontology candidate for
   entanglement-like two-party structure.  Named as a fork, with monogamy
   as the printed discriminator.

**And then the closure (#128, 2026-07-12, user directive):**

> *"stop the v9 review, as v9 actually didn't use a real interactive click
> law."*

Recorded as the **binding scope statement**: the v9 builders are
**exploratory record-substrate dynamics**, not the identified interactive
click law; the v9 geometry results stand as **closed historical
measurements about toy record substrates**; the paper-8 review stops at
round 1; **no further v9 review rounds will run**; and *"the funded
review's O1–O5 queue remains recorded in this LOG but is **NOT
scheduled**."*

> **THEREFORE, binding on any citation of this chapter:** rounds 46–48d
> are `[MEASURED, reviewed — PARKED-AT-PROTOCOL]`, **not** "parked", and
> **not** round; their queue is unworked; and the whole line is declared
> not to be the corpus's click law.  **Nothing in C6 is citable as a
> result about the framework of Parts A and B.**

**C6.11 RELATION UNESTABLISHED — v9 webs versus the v10 grammar.**

This is a second instance of §C5's problem, and it must be named as such.

- The v9 web and the v10 grammar are **two different formalisms** (§C6.1),
  and **no unit relates them.**  There is no map from slots to actors, no
  map from deposits to versions, no derivation of either from the other.
  **RELATION UNESTABLISHED.**
- The user directive at #128 is stronger than "unestablished": it
  **declares** that v9 did not use the interactive click law.  Read
  precisely, it disqualifies v9's builders from **both** of the corpus's
  dynamics streams — they are neither the identified law (§B2.9) nor the
  record-closed generated-law line.  **It does not touch the d42 grammar**,
  which *is* that second line, and which remains the only object in the
  corpus that generates causal structure at all (the identified law lives
  **on** a spacetime).
- **They disagree about their own geometry, measurably.**  v9's webs were
  engineered toward *round-cone, Minkowski-like* occupancy and got within
  6–9%; v10's records were measured against genuine Minkowski sprinklings
  and found **sharply unlike them** (§B5.7; and §B5.6's
  "narrower than chance").  These are opposite programmes of resemblance.
- **Two instruments overlap and one of them is retracted.**  Both lines
  use Myrheim–Meyer-style volume dimension and order dimension; v9's
  `F`-covariance certification is **VOID** (§C6.6 M1) and order-readability
  of `F` is open, so no v9 shape claim can currently be re-read as a
  statement about a v10 record's order.
- **What *is* shared, and it is not nothing:** the discipline (pins before
  code, wiring gates, pre-registered decisions, fresh-seed re-tests,
  headline retractions on the record), and two instruments whose
  *definitions* are common property — the two-clock lemma of §C6.2, which
  is the ancestor of §B7.1's doctrine, and the crown/`S_n` machinery that
  both lines use.

> `[MY READING]` The single most transferable thing in this chapter is not
> a number.  It is the **channel-manifold law** — *`d = dim(channel
> manifold) + 2`; the question is not "why three?" but "why the sphere?"*
> — because it is a statement about what kind of object a dimension is,
> and it was reached by proving that the previous target was impossible.
> Whether it says anything about the v10 grammar is **exactly the
> unestablished relation above.**

---
---

# PART D — THE DESTINATION

> **This part is where chapters A11/B11 point.**  Those chapters state the
> position of the two lines; this one states what the open questions are
> *for*.  The destination is a standing user direction (LOG **#436**),
> binding on every unit of this line.
>
> **Same two registers.**  Each section opens **① PLAINLY** and continues
> **② THE OBJECTS**, exactly as PART C.

---

## D1. The destination, stated

### ① PLAINLY

One target this programme does **not** have: *make the records look like
spacetime as physicists usually discretize it* — a random scattering of
points in Minkowski space, with the causal order read off.  The
destination is a different and larger thing:

> **Full Einsteinian manifolds — curved, dynamical spacetime — enriched
> enough that quantum particles can be created in them.**

Not flat spacetime.  Not a discretization that resembles a sprinkling.  A
manifold with genuine curvature, obeying dynamics, carrying fields, and
capable of the one phenomenon that most sharply separates curved-spacetime
physics from flat: **particle creation**.

Two things make this the right target rather than an ambitious one.

First, **the corpus already owns a piece of Einstein**.  Chapter C2's
result is that the earlier line derives Einstein's field equations *in
form*, as the thermodynamics of records, and proves it cannot derive their
scale.  So "Einsteinian manifolds" is not a distant hope in this programme;
it is a partially completed arrow with a precisely known missing piece.

Second, **the evidence points away from the sprinkling target**.  The
measurement that compares the framework's records with genuine sprinkled
Minkowski records finds them sharply unlike: sprinkled records have no
worldline structure at all, while the framework's records are *woven out
of worldlines* (§A5.7, §B5.7).  Resemblance to a sprinkling is the wrong
resemblance to chase.

### ② THE OBJECTS

The destination, as recorded (LOG #436, user direction):

> **"The destination is FULL EINSTEINIAN MANIFOLDS enriched to create
> quantum particles — not Minkowski-sprinkling likeness."**

with the supporting observation from the same entry: *"the grammar's
records are worldline-woven, not sprinkled."*

The supporting measurement is §B5.7: genuine sprinkled `M^{2+1}` shatters
3 and **never 4**, genuine `M^{3+1}` shatters 4 and **never 5** — the
continuum ladder reproduced exactly on discrete data — while the
engineered transport records reach **5**, one rung above every sprinkling
of any tested dimension and above the rung the 2-sphere's own geometry
permits.  So the two object classes separate by a rung, not by the
sprinklings reading nothing.  The `[MY READING]` mechanism note —
that sprinklings have no actor/wire structure, so the Dilworth mechanism
cannot even apply to them — is the structural reason the two object classes
should not have been expected to resemble each other.

**What the destination does NOT mean.**  It does not mean the corpus
claims curved spacetime, particle creation, or any step below.  §D2 is a
roadmap with per-arrow status, and four of its eight arrows are `[OPEN]` or
`[BLOCKED]`.

### The destination's working hypothesis, and its honest state

The destination names the target.  This is the **shape of the answer** the
programme is currently betting on, stated as a hypothesis because that is
what it is — and grounded, because the corpus's own archaeology supplies
the grounding rather than an analogy:

> **The modulus builds space; the phase completes and legislates it.**
>
> The real, reversal-**even** part of the record amplitude is what carries
> lengths and magnitudes — the **diagonal** of a rank-2 object.  The
> reversal-**odd** part, the phase, carries the **off-diagonal**, and with
> it the orientation datum a metric needs to be a metric rather than a
> table.  And the same phase, through **closure** — which loops come back
> unchanged — is what could *select* among the structures the grammar can
> build, where nothing in the corpus currently selects anything.

**Why this is grounded and not a picture.**  v2 paper 10 Prop 10.6 is an
all-order **no-go**: the Born-squared real shadow keeps `|z₁|²` and
`|z₂|²` and **provably loses** `h^{12} = Re(z₁z̄₂)`.  v6 paper 5 states
the same thing from the response side: the tensor's minimal determining
datum is the **oriented** closed-route holonomy, and magnitude-only or
unoriented holonomy forgets the sign.  And the algebra is owned twice:
commutator → antisymmetric → **rotation/phase**; anticommutator →
traceless symmetric **rank-2**; `(1/2){γ^i,γ^j} = h^{ij}I`.  **ODD =
PHASE, EVEN = METRIC** is the corpus's own structure, not a reading
imposed on it (§B2.12).

**And here is the honest current state, which is the part that must travel
with the hypothesis.**

- **Everything the programme has exhibited is modulus.**  The even
  channel's rank-2 object exists, is genuinely anisotropic with a trivial
  stabiliser on the fixture its source paper selects — and is a
  **covariance, not a metric response**: no atom index, rank 1 locally,
  nothing acting on its index, predictively equivalent to its own trace
  (§B8.10).
- **No `U(1)` part has been exhibited anywhere.**  Probability transport
  is flat at closed scope **as a theorem** and **curved at transport
  scope** as a measurement — but every value it returns is a positive
  real number (§B2.12).
- **The phase's last known address is the ODD SECTOR of the curved
  transport loops.**  That is a specific place, not a hope: it is the only
  region of the theory where anything fails to come back unchanged, and
  the odd half of it is the only half that could carry an argument.
- **So the hypothesis has exactly one next move, and it is the era's
  hinge:** characterise the transport holonomy — its carrier at record
  level, its group, whether it is a coboundary, and whether its odd sector
  has an imaginary part.  If it does, the destination's whole chain
  (metric completion, then selection by closure) becomes a research
  programme.  If it does not, the corpus owns a real, phaseless holonomy
  of probability transport and the founding slogan is settled negatively —
  which is publishable either way and was pre-registered as such.

`[MY READING]` on the ranking, and only on the ranking: the reason this
hypothesis sits at the top of §D4 is not that it is likely but that it is
the only place where a **single** measurement moves three separate fronts
— the phase, the metric's off-diagonal, and the gauge question's one
untried candidate.

---

## D1b. The scale doctrine `[BINDING on every destination-line unit, LOG #440]`

### ① PLAINLY

Before any arrow is walked, one constraint governs all of them, and it is
the author's own objection turned into a rule.

A record event is small. A particle is not. If the spacing between
adjacent records were one millimetre, a proton would be about **twenty
light-years across** — something like `10²⁰` record spacings, `10⁶⁰`
record events. Whatever a particle is in this framework, it is **not a
marked vertex, not a slot, not an actor, and not anything a fixture-scale
computation can display.**

So the rule:

> **1. No fixture-scale object may ever be called a particle.** A
> particle, if this framework produces one, is a **collective** structure
> over astronomically many records — the analogue of a soliton or a
> phonon, not of a marked point.
>
> **2. Units certify MECHANISMS, not objects.** A destination unit may
> certify tensorial transition behaviour, mode structure, or
> boundary/vacuum ambiguity — each stated as the **scale-invariant
> mechanism** whose collective, scaled-up form would be the physics — and
> **must say which mechanism it certifies and that it is not exhibiting
> the object.**

Two existing results make this rule consistent rather than merely
cautious. The corpus already proved that **merging records into a
composite is massively lossy** (chapter A1), so "the composite is one
line" was never available. And it already proved that **the record scale
itself is a free parameter** (chapter C2) — so even the twenty-light-year
figure is an illustration, not a corpus number.

**And the doctrine has a direction, not just a prohibition.** If a
particle must be collective, then the readings of "particle" that survive
are the ones where a particle is a **mode** — a delocalized pattern —
rather than a located thing. Which is exactly what the v9 line concluded
from the other end: its free-web theorem says that without coupling there
are **no collective excitations at any scale**, so matter *requires*
coupling and, when it appears, appears as an excitation *of* the substrate
rather than a piece of it.

Two independent lines, one conclusion: **whatever "particle" means here,
it is a mode.**

### ② THE OBJECTS

Recorded at LOG **#440** as **user direction, binding on all
destination-line units**, restating the `d41c` §1A objection as a forward
constraint. The illustrative arithmetic: at a record spacing of 1 mm
(dimensionless, illustratively), a proton is **~20 light-years** — a
particle is **~`10²⁰` spacings across, ~`10⁶⁰` record events**.

The three clauses, verbatim in substance:

1. **No fixture-scale object may ever be called a particle.** *"A
   particle, if this framework produces any, is a COLLECTIVE structure
   over astronomically many records — the analogue of a soliton or phonon,
   not of a marked vertex."*
2. **Units certify MECHANISMS, not objects:** *"tensorial transition
   behavior, mode structure, boundary/vacuum ambiguity — each stated as
   the scale-invariant mechanism whose collective, scaled-up form would be
   the physics. Every destination unit must name which mechanism it
   certifies and say it is not exhibiting the object."*
3. **It composes with the existing walls:** **D48** (a composite is not
   one line — the labelled record does not aggregate, and causal
   aggregation is massively lossy; §B1.2) and **paper 57** (the record
   scale itself is a free parameter, `G` un-fixable; §C2.2), *"so even the
   `10²⁰` figure is illustrative, not corpus-fixed."*

**The consistency note carried with it `[MY READING, per #440]`:** the
doctrine **favours the boundary-freedom ↔ vacuum-ambiguity bridge over
any local-object story** — *"modes of a measure are intrinsically
delocalized, which is the only kind of 'particle' the scale gap
permits."* And tensors enter *"as the transformation behavior of
chart-attached data under transition maps — a mechanism certifiable at
fixture scale under rule 2, since transition COVARIANCE is scale-free even
when the charts are tiny."*  **That slot is empty on the chart side, and
the rule is what makes the emptiness legible**: every substrate whose
transition maps have been measured — delivery crystals, conflict
crystals, and the crossed-conflict double grid built precisely because a
conflict event lacks the symmetry that trivializes a delivery — has a
class that is a **coboundary** (§B8.8, §B8.9), so there is no non-trivial
transformation behaviour to certify there.  **But the slot now has one
candidate, and it is on a different carrier**: probability transport
itself is **curved** at transport scope (§B2.12), by an amount no chart
instrument can see, and two of its four values lie outside the group of
the corpus's known coboundary.  The doctrine names the deliverable; the
chart search for it has failed on the substrate that had the best
structural reason to supply it; and the one live candidate is a
connection on sequences rather than on charts, which is why
characterising it ranks first in §D4.  *(The same doctrine covers the
rank-2 side: §B8.10's even Gram is an ensemble summary statistic on a
channel index nothing acts on, so it certifies no mechanism — which is
exactly what rule 2 is for.)*

> **The convergence worth naming.** Chapter **C6.8**'s free-web influence
> theorem reaches the same place from the substrate side: with no coupling
> a perturbation rides exactly one worldline and **no collective
> excitation can exist at any scale**, so *matter requires coupling* — and
> what coupling then produces is an excitation **of** the web, "a phonon
> of records", expected only at scales far above the substrate's own.
> The scale doctrine forbids the local reading; the free-web theorem says
> the local reading was never dynamically available either. **Two
> independent lines, one conclusion: a particle here is a mode.**
>
> `[MY READING]` That is a genuine convergence and it is also the most
> that can be said. Neither line exhibits an excitation; v9's line is
> closed and declared not to be the click law (§C6.10); and §D3's vacuum
> bridge remains three unbuilt arrows from being a question.

---

## D2. The roadmap, arrow by arrow, with honest status

### ① PLAINLY

Here is the whole route from the primitive to a laboratory, with each step
marked by what the corpus actually has.  Two of the eight steps are done,
two are half-done, three are open, and the last is blocked.

| # | step | plain status |
|---|---|---|
| 1 | records → a causal order | **HAVE** — this is what the grammar builds, and the order is the physical content |
| 2 | causal order → local skies and a dimension *capacity* | **HAVE** — with the meter reading the grammar's coordination, not a record's dimension |
| 3 | skies → charts, gluing → a manifold | **OPEN, four segments done and two of them are negatives** — the grammar **tiles**; it tiles **wide** (a forced 177-event double ring holding the homogeneity band while carrying 4-direction charts); its charts' **transition maps are measured** and are non-identity, consistent around every loop, and **removable by a change of convention**, so the atlas is globally trivializable and carries no structure group; and the **conflict** road past the delivery ceiling is open and walked — delivery-free crossed-conflict crystals tile at cadence and carry **nine**- and **sixteen**-direction charts, with the corrected ceiling reached at every dispute size built (9, 16, 25, 36), and the sixteen-wide record sits inside **both** sprinkling band columns one depth down as a whole record.  Its gluing is trivial too.  What remains: a substrate whose gluing is *not* trivial — and the corpus now has **one candidate**, the curved transport loops of §B2.12, which no chart instrument can see; a general-`k` proof and a tiling above `k = 4`; the **rank-2 object** the arrow is *for*, which on the even channel is a covariance and not a metric (§B8.10); and the second road's unfinished business |
| 4 | manifold → Einstein dynamics | **PARTIAL** — the *form* of the field equations is derived; Newton's constant is provably not derivable from inside |
| 5 | manifold → quantum fields on it | **PARTIAL** — a lift of the record process into Hilbert space exists at fixture scale, and its arbitration layer is where the quantum problem begins |
| 6 | fields → **particle creation** | **OPEN** — the destination's defining phenomenon, with one suggestive structural resemblance that is *labelled speculation* |
| 7 | particles → matter | **OPEN** |
| 8 | matter → a laboratory number | **BLOCKED**, and the block is four-fold |

Three honest points about this table.  **Every arrow is drawn in the
grammar's register**, and the corpus's other stream — the identified law,
which is where measured physics lives — sits on the far side of a **named
missing map** (§A2.6, §B2.9).  Until that map closes, results here
transfer to laboratory clicks through nothing at all.  **The arrows are
also not independent, and four of them are blocked on the same thing** — the programme cannot
currently pose probabilistic questions at the scope where its geometry
lives (chapter 9, §§A9.4/B9.4b) — though for the first time there is a
**route** rather than a wall there, contracting everywhere measured and
waiting on one theorem (§§A9.6/B9.7).  **And one constraint
governs every row**: §D1b's scale doctrine, which forbids calling any
fixture-scale object a particle and requires each unit to name the
scale-invariant *mechanism* it certifies.

### ② THE OBJECTS

**ARROW 1 — records → causal order.  `[HAVE]`**

The event poset is the **carrier-wise wire closure** (§B2.1); causal order
is physical and incomparable order is gauge (§B3.1); admissibility is
past-local and executable, with a single authority (§B2.4).  Load-bearing
downstream: **any two events sharing an actor wire are comparable** — a
theorem of the layer, not an assumption (§B7.3(i)), corroborated over
218,795 pairs with zero violations and re-verified in the round at 226,223.

*Residual defects carried:* the `h12` off-ladder configuration; the
general-depth `1 + k/4` ladder false under current pricing; the D2H merge
priced `1/16` vs `1/24` (§B2.8).  None of these touches the order; all are
pricing.

**ARROW 2 — causal order → local skies and dimension capacity.  `[HAVE]`**

Delivered: the sky instrument with three committed definitions, **all
three live** — the argument that only one could ever fire is refuted, and
which reading is privileged is an open residue (§B5.4); the corrected
capacity condition; the two scaling laws in different variables — Minkowski buys
sky size with **density**, transport buys it only with **actor width**
(§B5.5–§B5.6); transport skies **narrower than chance**; the **Dilworth
gate** as an unconditional theorem of the layer (§B7.3); and constructed
records that pay the price at two rungs, the higher one **forced** at every
one of 84 steps (§B8.4).

**And what it does not deliver (§B5.7):** the shatter number is *not* a
dimension reading for a record.  The calibration ladder (`B₄` fits `S²`; no five
points ever shatter on `S²`; `B₅` fits `S³`) is exact and intact **for
continuum trace systems**; discrete sprinklings read `≈ 0` in every
dimension.  So arrow 2 delivers a **capacity** result — *the layer does not
cap the shatter ladder at the sphere's rung* — and a measure of engineered
coordination.  It does not deliver a dimension for a record.

**ARROW 3 — charts and gluing → a manifold.  `[OPEN — four segments
done: the grammar tiles, it tiles wide, its gluing is TRIVIAL, and
crossed conflict breaks the width ceiling at 9]`**

A causal order is not a manifold.  To get one you need local pieces that
look like patches of `ℝ^d` (**charts**), a rule for saying two patches
overlap and agree (**gluing**, with transition maps), and enough
consistency that the result is one object.  **The corpus is attacking
this from two directions at once, and they have never been compared.**

**ROAD 1 — the v10 atlas / crystal line `[D58 + D60 batch-round reviewed;
D63, D64, D66 round 1 terminal]`.**  Two instruments, built before any data
(`note-d58-atlas-instrument-pin.md`, committed before code): the
**homogeneity profile** — the fraction of events carrying a chart of at
least two directions — and the **chart-size ratio**

```
ω(e, e′) = |D_e(d) ∩ D_{e′}(d−1)| / |D_e(d)|      on cover pairs
```

Both were built assuming **identity** transitions, with the real cocycle
condition declared a later stage.  **That stage has since run** (§B8.8),
and the assumption turns out to be harmless *on this road's substrates*
for a reason nobody could have asserted in advance: the transitions are
not the identity, but their class is a **coboundary**, so a per-chart
relabelling makes them the identity and every `ω` figure below is a
statement about a genuinely trivializable atlas.

> **`ω` is a CHART-SIZE RATIO, not a two-way overlap `[THEOREM, 14,818
> pairs]`.**  On cover pairs the smaller chart is *contained* in the
> larger, so `ω` reduces to the ratio of their sizes — Jaccard similarity
> is identically equal to it.  It therefore **systematically favours
> thin-charted records**, and every `ω` figure below must be read with
> that.

**The measurements** (SKY-B charts, exact Fractions, comparators
recomputed on eleven genuine sprinkling configurations):

| record | homogeneity (`d = 2`) | mean `ω` | `\|D\| ≥ 4` (`d = 2`) |
|---|---|---|---|
| genuine sprinklings (11 configs) | **0.642 – 0.800** | **0.048 – 0.133** | 0.425 – 0.650 |
| the brick crystal (§B8.6) | 0.769 | 0.651 | **0.000** |
| **the wide crystal** DR(8,10,8) (§B8.7) | **0.797** | 0.730 | **0.333** |
| **the double grid** DOUBLE-GRID(3,4) (§B8.9) | 0.517 (`d = 3`: **0.783, in band**) | 0.557 | 0.092 (`d = 3`: 0.325, below) |
| **the `k = 4` double grid** DOUBLE-GRID(4,4) (§B8.9) | 0.485 (`d = 3`: **0.725, in band**) | — | 0.400 (`d = 3`: **0.635, in band**) |
| the shatter-4 courier record | 0.386 | ~0.47 | 0.000 |
| the shatter-5 courier record | 0.357 | — | 0.000 |
| a generic 2-actor walk | 0.067 | 1.000 (2 pairs) | 0.000 |

> **THE HOMOGENEITY GAP IS REAL AND SURVIVES EVERYTHING: engineered
> 0.357–0.386 against a sprinkling band of 0.642–0.800.**  The courier
> records, built to shatter, are **the opposite of atlases**.

**One correction carried, because it reverses a sign.**  The
`M^{2+1}`-vs-`M^{3+1}` overlap comparison had been flagged as a finding
candidate confounded by density.  It closes **sign-flipped**: the earlier
`M^{3+1}` control was a degenerate generator — **32 distinct spacetime
points wearing 120 labels** — and against genuine sprinklings the
`M^{3+1}` ratio is **0.048–0.100**, *below* `M^{2+1}`'s 0.12, not above
it.  Given the containment theorem this is the expected direction: denser
skies have larger charts and smaller size-ratios.

**And the crystal question, which this road posed, is ANSWERED FOUR
TIMES — three yeses and one no.**
*Can the grammar build a record whose events are charted everywhere with
large overlaps — a tiling — the way a courier record carries one rich
sky?*  **Yes**, at sprinkling-grade homogeneity and above-sprinkling `ω`,
**with thin charts** (§A8.6, §B8.6).  *And can that tiling also be wide?*
**Yes, at `d = 2`** — the two mechanisms compose in a forced 177-event
double ring (§A8.7, §B8.7), with band membership largely an ends property
and the depth label part of the claim.  *And do that record's charts glue
non-trivially — is there structure in the overlaps?*  **No** (§A8.8,
§B8.8): 115 of 172 overlapping pairs carry non-identity transitions, all
111 testable triples satisfy the cocycle, and then an explicit per-chart
port choice (32 charts / 28 charts) turns **all 108** of the
length-preserving ones into the identity.  `H¹ = 0`; zero obstructions at
two independent port conventions; **the transitions are pure gauge and no
structure group is exhibited**.  *And can the grammar tile out of
**conflicts**, past the delivery ceiling?*  **Yes** (§A8.9, §B8.9): 32
forced conflict configurations tile with zero refusals, the ceiling is
refined to the **live** branching factor `Bl^d` — so 3+ *proposers*, not
3+ registers — and the delivery-free DOUBLE GRIDs **realize `k·Bl = k²`
at `k = 3` and `k = 4`** (nine- and sixteen-direction charts), while
height-levelled chains carry it to **25 and 36** at `k = 5` and `k = 6`.
`DOUBLE-GRID(4, 4)` sits **inside both** `d = 3` sprinkling band columns
as a whole record while carrying `max |D| = 16`.  Their gluing is a
coboundary as well, at all five port conventions.

> **What that costs, said without softening.**  The tensor/curvature
> programme — the thing a manifold arrow is *for* — starts at **zero** on
> every substrate measured so far, conflict ones included.  Non-identity
> transitions, a clean cocycle, a closure, even a group name if one had
> been determined, are all compatible with `H¹ = 0` and were.  **The test
> is the obstruction count**, and it is now a gate that every successor
> inherits.

**And there is now exactly one place the chart instruments could never
have looked.**  Every triviality verdict above is read off a **chart**
atlas over a **record** graph.  §B2.12 measures a different connection
entirely — probability transport itself, on **sequences** — and finds it
**curved** at transport scope, with the defect living precisely in the
squares that do **not** close at record level.  The blindness is
structural, not incidental: a square closes at record level exactly when
its two events are register-disjoint.  So the corpus's "no structure
anywhere" is a statement about the objects its instruments can see, and
the one object they cannot see is the only one that has ever come back
non-trivial — with two of its four values, `2/3` and `3/2`, lying outside
the group of the corpus's known coboundary.  **That is the gauge road's
only live candidate, and characterising it is the era's next unit.**

**And the rank-2 object the arrow is *for* now has a measured status, not
just a hope** (§B8.10).  The corpus's own earlier hunt was for `h^{ij}`,
and it half-succeeded: the metric's **diagonal** is visible in
endpoint-probability data and its **off-diagonal is provably not**, being
the relative phase (v2 p10 Prop 10.6).  Resurrected on the fixture paper
30 actually selects, the even channel's second-moment form is genuinely
anisotropic with a **trivial stabiliser** — the right starting object —
and is nonetheless a **covariance, not a metric response**: one global
form with no per-atom index, rank 1 before averaging, and **nothing acting
on its index** to transform it.  `FAILS-FULL-GR` stands, sharper.  The
tensor stage this arrow needs is not the direction index of a hand-built
crystal — those inherit their blueprint's symmetry and are *more*
degenerate — but **generic, stabiliser-1 direction geometry**, which
nobody has built.

**And then the road meets a wall it can name exactly — and walks through
the one door the wall leaves.**

> **`[THEOREM]` `|D_e(d)| ≤ B^d`**, `B` the largest register count of any
> event.  Deliveries carry `B = 2`, so **no delivery circuit whatever can
> exceed chart width 4 at `d = 2`** — the sprinklings' 10–17 is not a
> construction target, it is unreachable by transport.  **Width past 4
> must be bought with arbitration over conflicts** (§B8.7).
>
> **`[THEOREM]` and the refinement `|D_e(d)| ≤ Bl^d`**, `Bl` the largest
> **live** out-degree — registers that recur, the minted version wire
> being dead.  So an arbitration branches by its **proposer** count, "3+
> registers" is necessary and not sufficient, and the depth-2 ceiling is
> `k·b ≤ k²`.  **Realized at `k = 3, 4, 5, 6` — 9, 16, 25, 36 — by
> delivery-free crossed-conflict crystals and height-levelled chains
> (§B8.9).**

`[MY READING]` That reshapes this road's remaining story.  The distance
between the grammar's atlases and a sprinkling's read like a quantitative
shortfall to be engineered away; it is a **grammatical** one — and the
grammar's answer is now in hand at every size that has been tried.  The
road to a wide chart, and so
eventually to a 3+1-sized sky at a charted event, runs through **crossed
conflict**: not more plumbing, and not even a single conflict axis, but
two or more concurrent ones, since one dispute per actor makes a chain of
diamonds and carries nothing — with the deeper statement being that what
crossing *buys* is a **height condition**, which the grammar's own idle
event can also supply.  The gluing motivation that pointed the same
way has been **spent** — the conflict substrate glues trivially too — and
the width motivation is **discharged**: sixteen directions inside the
sprinklings' 10–17, on a whole record that also holds both band columns.
What remains on this road is not a construction but two proofs-of-reach: a
general-`k` statement, and a *tiling* above `k = 4`.

**ROAD 2 — the v9 grown-web line `[PART C, chapter C6]`.**  Further along
in one specific sense and further behind in another.  It has **built**
objects that read four-dimensional by volume on a dedicated calibration
(`d_ball = 3.84/3.85`, no clamps), carry order dimension ≥ 5 by explicit
witnesses, and — in the diffusive class — read round-coned and 4D
simultaneously at `g = 0.18`.  It has a **law** for what dimension *is*
(`d = dim(channel manifold) + 2`), reached by proving the previous target
impossible.

**But its review debt is outstanding and its line is closed.**  The
conjunction is `PARKED-AT-PROTOCOL`, not parked: the volume conjunct is
instrument-suspect (jackknife 7/10 flips), *"ROUND" was overclaimed*
(`F_dom` sits `+0.117`, `+6.5σ`, above the round-reference mean), one
statistical leg fails multiplicity correction, and the O1–O5 queue is
**recorded and unscheduled**.  Above all, the user directive at #128
declares that **v9 did not use the interactive click law**, so nothing it
built is an object of the theory Parts A and B describe.

**THE CONVERGENCE OF THE TWO ROADS IS ITSELF AN OPEN QUESTION**, and it is
sharper than either road's own residues:

- Road 1 measures **charts and overlaps** on records of the click law;
  Road 2 measures **cone shape and volume dimension** on webs that are not
  the click law.  **No instrument has been run on both.**
- They are pointed at **opposite resemblances**: Road 2 spent five rounds
  trying to make its objects Minkowski-like, and Road 1's own parent
  measurement found the grammar's records **sharply unlike sprinklings**
  (§B5.7).  Whether "atlas-like" and "round-coned" are the same
  target in different clothing, or genuinely different demands, is
  **unknown**.
- **What Road 1 could borrow immediately** `[MY READING]`: Road 2's
  channel-manifold law says a dimension is the dimension of a *space of
  channels*.  Road 1's chart is a set of *directions at an event*.  Those
  are the same kind of object described in two vocabularies, and the
  translation has never been attempted.
- **What Road 1 must not borrow:** any v9 number.  §C6.10's closure and
  §C6.11's unestablished relation both bind.

**Status, combined: `[OPEN]`.**  The manifold arrow has two instruments
(Road 1's atlas, and a validated transition detector with a triviality
gate), four measured segments — tiling, tiling-with-width, a gluing that
is **trivial**, and conflict crystals that **reach the corrected width
ceiling with no deliveries in them at every dispute size built (9, 16, 25,
36)**, the sixteen-wide one holding **both** band columns one depth down
as a whole record — a **proved ceiling** in two versions telling it which
mechanism each further step must use, **that mechanism now identified and
cheap** (height-levelling, out of the grammar's own idle event), two
proof-shaped residues rather than a next construction (general `k`; a
tiling above `k = 4`),
a parallel body of suggestive-but-closed work (Road 2) that no unit
has connected to it — and, new and unlike anything else on this arrow,
**one measured non-triviality**: the curved transport connection of
§B2.12, which lives outside every chart instrument's domain and is the
only object on the whole road that has ever failed to come back
unchanged.

**ARROW 4 — manifold → Einstein dynamics.  `[PARTIAL]`**

This is where PART C pays off, and the status is precise (all of §C2):

- **Derived `[DERIVED, mod (R) + two gates]`:** the field equations *in
  form*, `G_μν = 8πG T_μν`, as the equation of state of sealed records —
  including the linearized spin-2 (traceless) equation via the null-cone
  lemma, and including two things vanilla Jacobson *assumes*: the geometry
  factor of the area law (Srednicki's 0.295, no fitted tail) and the
  pure-area property of the entropy.
- **Provably not derivable `[NO-GO]`:** Newton's `G`.  One record length,
  weight-counting lemma, `G·σ_A = 1/4`, `κ·σ_A = 2π` and `G·Λ²` as *two
  separate* weight-zero invariants, seven levers collapsing identically,
  and the second-scale attacks closed.
- **Conditional, and the asymmetry matters:** four named premises carry the
  Jacobson route, but **the weight-counting no-go depends on none of them.**
  *The wall stands unconditionally; the `G`-naming of it is conditional.*
- **Obstructed `[OBSTRUCTED → OPEN]`:** the propagating graviton — 4 of 9
  components priced universally, the other 5 spanned but only at a
  boost-dependent second-order coupling, with four convergent obstructions
  reducing to one root (the needed structure lives only in a continuum
  algebra a finite record lattice cannot host).

**The connection to arrow 3, stated exactly.**  Arrow 4's derivation runs
on a *continuum* geometry with local Rindler horizons.  It presupposes the
manifold arrow 3 has not built.  So the two are in the order given, and
arrow 4's `[PARTIAL]` should be read as *"already available once arrow 3
lands, modulo its four named premises and with `G` as an honest
calibration"* — not as *"half-built on the records as they stand"*.

**ARROW 5 — fields on the manifold.  `[PARTIAL]`**

What exists (§B6.6): the endpoint lift assigning `∏√q` to complete
histories, with the Born diagonal on the canonical-class basis equal to
`mu/Z` at `Z = 3`, exact on 253 quadratic ratio pairs; the **kernel-layer
lift exact** at `2/3`–`1/3`; a complete fine-versus-coarse instrument pair
(order coherence `1/6` under coarse sealing, `0` under fine); and, in v10
paper 31 §4.3, a **constructed isometric arbitration family** reproducing
the `K1` Born weights exactly and reconstructing the committed menus at
both cuts in exact rationals.

What is honest about it: **the lift is the classical gradient completion at
one particular boundary "in Hilbert dress"** — Hilbert space supplies no
new resource; and the step operator faces the three-horn pincer at the
arbitration layer, which is exactly where the classical problem stopped.

So arrow 5 is a *field-theoretic* arrow only in the loosest sense: what
exists is a quantum lift of the record process, at fixture scale, on a
grammar with two actors.  **A quantum field on a curved manifold is not
built, and no unit has attempted it.**

**And the arrow now carries one hard negative from the map's side
(§B2.11).**  Asked from below rather than from above — what quantum
layers does the *generated* law admit? — the answer at closed scope is
that consistency with the records permits interference everywhere and
prices it nowhere, while the first fair demand that the interference be
**generated by the law's own state** removes all of it, at every
truncation tried.  So the quantum content of this arrow cannot be
manufactured out of the closed law's own state variables; it must come
from transport scope, from a different joint, or from a demand nobody has
written yet.  That is a constraint on how arrow 5 may be built, not a
piece of arrow 5.

**And it carries one positive that is older than the arrow (§B2.12).**  The
`∏√q` object this arrow is built on is the **right carrier** — square
roots of weights are amplitude moduli — and the corpus already owns, from
an earlier version line, the amplitude form that would make it quantum:
real decay on the reversal-even channel, phase on the reversal-odd one, at
dual-conjugation error exactly zero.  What is missing is the argument.
For the `∏√q` lift as D42b4 defines it the phase slot's value is **forced
to `+1` at closed scope** — the record-graph holonomy is trivial there, so
no other section of the phase bundle is reachable by transport — and that
forcing is *scope-bound*: it says nothing about transport scope, where the
same connection is curved.  **So the honest statement of arrow 5's quantum
gap is now specific: the lift has a carrier and no argument, and the only
place an argument could come from is the odd sector of the curved
transport loops.**

**ARROW 6 — PARTICLE CREATION.  `[OPEN]`** — see §D3, which it deserves.

**ARROW 7 — matter.  `[OPEN]`**

Named, not built.  The one relevant positive is from §C2: the dimensionless
gravitational coupling-per-species `c_m = Gm²/ℏc` is **weight-zero and
intrinsic**, hence **eligible** to be a record output — the no-go does not
forbid it.  *"So the records cannot fix the absolute scale of gravity;
whether they fix its dimensionless strength is a separate, still-open
question."*  The matter-sector hierarchy is that question, and it is
explicitly not engaged.

Related and also open: the three-walls classification's **MODE** wall
(§C2.6) — which-mass-is-which is **import-fixed** by measured spectra, not
derived.

**ARROW 8 — laboratory.  `[BLOCKED]`**

Blocked at `note-d41c-step3-bridge-declarations.md` §1A (§B10.7), on four
independent grounds, of which the second is a *result of arrow 4*:

1. a scale gap of roughly twenty orders of magnitude `[ILLUSTRATIVE]`;
2. **the corpus cannot fix that scale** — arrow 4's own no-go: exactly one
   record length, `G` provably un-fixable, so the record scale is a free
   parameter and any assumption about where the laboratory sits is
   un-derived either way;
3. a **layer gap** — records → background → quantum fields → atomic
   structure, at least three constructed layers, **none built** (they are
   arrows 3, 5, 6/7 of this very table);
4. **aggregation loss** — merging actors is never impossible but is
   massively lossy, so a bound extracted through a single-line description
   of a composite is a bound on the coarse world (§B1.2);
5. and, upstream of all four, **the missing map** (§B2.9): the laboratory's
   clicks are governed by the *identified* law, which the corpus supplies
   rather than derives a record grammar for.  Even a completed arrow 7
   would land on the wrong side of that map.

The slot named **(0) THE COARSE-GRAINING** is logically prior to the four
things a bridge must fix, and is **EMPTY**.  The sign-off block is
**SEALED, NOT PRESENTED FOR SIGNATURE**.

> **Note the structure of the block.**  Ground 3 says the laboratory arrow
> is blocked *by the incompleteness of this very roadmap*.  That is not
> circular — it is the roadmap doing its job: it says exactly which arrows
> must land before arrow 8 can even be posed.  And ground 2 says that even
> when they land, one dimensionful calibration will still have to be
> imported.

---

## D3. Particle creation, and one labelled speculation

### ① PLAINLY

Why is particle creation the destination's chosen endpoint rather than,
say, "recover the Standard Model"?  Because it is the **cheapest genuinely
curved-spacetime quantum phenomenon**, and because of what it reveals about
the structure of the theory that produces it.

In quantum field theory on a curved spacetime, there is no
observer-independent answer to "how many particles are there".  The notion
of *particle* depends on a choice of **vacuum** — of which state counts as
"nothing" — and in a curved or dynamical spacetime there is in general no
preferred such choice.  Different reasonable choices disagree about the
particle content of the *same* state.  That is not a defect; it is the
mechanism.  Hawking radiation and cosmological particle production are both
consequences of it.

So a theory that wants to create particles must confront a very specific
kind of freedom: a choice that is not fixed by the dynamics, that
nevertheless changes what an observer counts.

**And here is the resemblance.**  The v10 measure line ended (chapter 6) at
a structurally similar place.  The record law does not fix its own
probabilities; a **boundary object** must be supplied; the space of such
objects is 313-dimensional; and the one canonical completion that needs no
boundary is unique only *given a postulated shape*, which was then measured
to be a genuine **choice**, not a law.

Two freedoms, in two very different parts of the theory, of the same
*shape*: not fixed by the dynamics, and consequential for what gets
counted.

**This is a resemblance, and this document labels it as one.**  Nobody has
posed it as a question a computation could answer, no unit has tested it,
and the corpus records the same suggestion as an unpinned reading.  It is
written down here because it is the kind of thing that should be written
down *and clearly marked*, not because it is evidence of anything.

### ② THE OBJECTS

**The physics being pointed at** `[LITERATURE, external]`: in QFT on curved
spacetime the particle content of a state is not observer-independent —
inequivalent vacuum choices (equivalently, inequivalent Fock
representations, related by Bogoliubov transformations that mix creation
and annihilation operators) assign different particle numbers to the same
state.  This is the mechanism behind Hawking and cosmological particle
production.  Nothing about that is a corpus result and none of it has been
built in the corpus.

**The corpus-side objects being compared:**

- **313-dimensional boundary freedom** (paper 30 §5.3, `[REFEREE-CARRIED,
  LOG #302]`, and *upheld* against a challenge — §B6.11 BLOCKER B1's
  attempted reduction was refuted and the queued erratum cancelled, with
  #420 upgrading the refutation to a theorem).
- **The form is a CHOICE** (D50, batch-round reviewed, §B6.12): the two
  strongest invariance demands leave the completion dimension **growing**
    (12 → 32 → 125), and adding foliation-invariance leaves it **exactly
  unchanged**.  So the uniqueness of the canonical completion comes from a
  postulate about the shape of `Z`, and the standing restriction on every
  citation is permanent.
- **The Perron tilt** as the exact price (§B6.10): each option re-weighted
  by the record-growth capacity of the state it leads to, and by nothing
  else — gated over 77,541 pairs with zero violations.

**The stated bridge, and its status.**  LOG #436 records, as **user
direction and explicitly `[MY READING]`, unpinned**: a
**boundary-freedom ↔ vacuum-ambiguity** correspondence.

> `[MY READING — this document's own, and it must not be cited as anything
> else]`  The suggestion is at least *well-typed*.  Both are a choice of
> "what the far end / the reference state is"; neither is fixed by the
> local dynamics; both change a count (particle number there, probability
> here) without changing the law that generates the structure.  One could
> even name the sharper form: *is the completion's boundary object the
> record-level shadow of a vacuum choice?*
>
> **Everything about that sentence is unearned.**  There is no field on the
> records, so there is no vacuum to be ambiguous about; the completion
> lives at delivery-free scope, while the geometry lives at transport
> scope, and §B9.4b shows the completion machinery **provably cannot
> travel** there.  §C5.4 row 4 records the general form of this
> caution: resemblance between two "the theory cannot supply this from
> inside" results is **not** a theorem relating them.  As of LOG #436 the
> bridge is unpinned and untested, and nobody has stated it in a form a
> receipt could gate.

**What would make it more than a resemblance** — stated so that the
speculation is at least *costed*: (i) arrow 5 delivering an actual field on
an actual manifold, so that "vacuum" names something; (ii) arrow 3
delivering the manifold; (iii) a transport-scope completion, which chapter
§B9.4b shows is blocked at every granularity anyone has tried.
All three are open.  **The speculation is therefore at least three
unbuilt arrows away from being a question.**

---

## D4. What the destination changes about the open problems

### ① PLAINLY

Read through the destination, the open problems sort differently than
they do from inside either line.

The **manifold** is the programme's first construction target — it is what
the destination's own definition requires, and no other arrow can be posed
without it.  Its first four questions are **answered**, and one of the
four answers is a *no*.  The grammar tiles; it tiles *wide*; the
translation rules between its charts, which are what a manifold's
structure actually lives in, turn out to be **a change of convention and
nothing more** — real as written, and removable all at once by relabelling
each chart's two ports; and the door the width theorem left open has been
walked through.

That door was conflict.  Because a message touches exactly two wires, no
record built out of messages can carry more than four directions in a
shallow chart, while real spacetime carries ten to seventeen — a
*grammatical* gap, not an engineering one.  A record built out of
**disputes** is not bound that way, and the records have been built: rows
and columns quarrelling at the same time, **no messages in them at all**,
tiling at cadence, and carrying **nine**- and **sixteen**-direction
charts — exactly the ceiling for three-way and four-way disputes — with
levelled chains reaching **twenty-five** and **thirty-six** at five and
six.  The ceiling is reached at every size anyone has built.  And the
sixteen-direction record sits *inside* the band real sprinkled records
occupy — as a **whole** record, on **both** ways of measuring the band —
so a record that is at once uniform and spacetime-wide now exists.

Three things about that result set the ranking.  The first is the
mechanism: what buys a second direction is not a message but a **second
concurrent dispute** — messages seed and rotate the disputes, they do not
make the space — and, one level down, what a second dispute *buys* is
that the follow-on events sit one layer down rather than two, which the
framework's own idle event can also arrange.  The second is that **the
frontier this line expected does not exist**: width was supposed to cost
uniformity, and at the sizes built it does not.  The third is what
conflict did *not* buy.  The reason to look at it was double: width, and
the hope that a dispute's lack of a free two-way symmetry would finally
make the gluing non-trivial.  The
width arrived; the gluing did not.  On conflict records too, at every
convention tried, the translation rules relabel away to nothing.  **So
the width leg of the manifold arrow is discharged, and the gauge road is
back to having almost no candidate at all.**

*Almost*, because one thing has never been tried: every record of this
kind crosses **two** disputes at once, and nothing in the grammar forbids
a third.  A three-way crossing is the only place left where a
*construction* could still turn one of this line's negatives positive —
it would say whether depth past the first step is governed by the number
of crossings rather than by the dispute size, whether a third axis
finally gives the translation rules a loop with something in it, and
whether crossing does anything to *select* a dispute size, which nothing
in the corpus currently does.  It is cheap and it is unbuilt, and no
number here is claimed for it.

The **measure at delivery scope** is the other problem near the top, and
for a structural reason: arrows 5 and 6 both need probabilities at the
scope where the geometry lives, §B9.4b closed the route that looked most
likely, and the quantum layer's own elimination (§A2.8) added a third
thing waiting on that same scope.  **What has changed is that it is no
longer only a wall.**  A route exists that never asks for the thing the
wall forbids: look a fixed number of steps ahead and push the horizon out.
That law is a genuine law out to seven steps, its drift **contracts at
every pool and depth measured**, and the truncation choice it depends on
cannot matter at the beginning of a record — a *theorem*, from the
symmetry between the two actors.  What is missing is a **bound**, and the
tool that would supply it is named and unattempted.  The measure has
stopped being a method problem and become a theorem problem, which is a
much better kind of problem to have.

**And what now stands above both of them is smaller and stranger than
either.**  Probability transport in this theory turns out to be **curved
where the geometry lives** — eighty-eight loops that do not come back
where they started, all of them carried by messages, none of them visible
to any instrument the programme had built.  That single object is where
the phase would have to live if the theory has one; it is the only
non-trivial loop structure the corpus owns; and it is the only untried
candidate left for the gauge structure a manifold needs.  Three separate
fronts move on one measurement, which is why characterising it ranks
first.

The **3+1 control** is *finished*, and its answer removed an instrument
rather than supplying one.

The **delivery-free measure** is, at its own scope, **finished**.  The
update rule that stood between "settled at every depth anyone had
checked" and "settled" has been written out case by case, and there are
five cases.  What is left there is not a gap in the argument but a
question about the *kind* of certainty the argument has: it is prose
reasoning checked against the code at scale, not logic a machine has
verified.  That item is cheap, bounded, and no longer blocking anything.

And a front that belongs to neither line remains the **deepest**: **the
missing map** between the grammar and the identified law (§A2.6).  It
used to rank below the construction problems, for the honest reason that
nobody knew how to attack it — and the construction that outranked it has
since been finished.  Everything depends on this one: until it
closes, none of this reaches a laboratory even in principle.  Three of its
segments are no longer names but measurements (§§A2.7–A2.9), and the
second of them changes what the front *is*.  It used to be an emptiness:
the generated line had no interference in it, so the condition asking
whether records decohere was satisfied by having nothing to decohere.
That emptiness has now been measured from the inside — the space of
quantum layers such a law could carry has been counted exactly — and the
answer is the least comfortable of the ones available.  Consistency with
the records permits interference everywhere and organizes none of it; the
first demand that the interference be **generated by the law itself**
leaves none at all.  So at the one scope where the corpus can compute, a
quantum layer over this law cannot be both generated by it and coherent.

**That is a narrowing, not a closing, and it re-points the whole
destination.**  What it removes is the hope that the map's quantum stretch
could be crossed at the closed scope by writing down consistency
conditions; what it leaves is a specific question with a cheap first
move — is the demand that emptied the cone the *only* fair one? — and a
place for the physics to live.  And the place is one the geometry line
has already named independently: **transport scope**.  The dimension
mechanism lives there.  The measure defect points there.  Coherence points
there by elimination.  And the phase, hunted through three version lines
of archaeology, has its **last known address** there too — the odd half of
the curved transport loops.  Four unrelated threads, one address, which is
the most useful thing the destination has learned in this stretch.

**And the phase is the thread that turns the destination from a target
into a chain.**  The corpus's own no-go says the real part of an amplitude
gives a metric's **diagonal** and provably loses the **off-diagonal**,
which is the relative phase; the corpus's own algebra says the symmetric
part of a pair of transports is a rank-2 coupling and the antisymmetric
part is a rotation.  So the working hypothesis of §D1 is not an analogy:
**the modulus builds space, and the phase completes it and legislates
it** — completes it by supplying the off-diagonal, legislates it by
selecting, through which loops close, among structures the grammar cannot
otherwise choose between.  Everything the programme has actually exhibited
is modulus.  Whether there is a phase at all is one measurement away, and
it is the same measurement as the one above.

And **the v9 arc** —
turns out to hold the furthest-advanced construction anyone has of a
four-dimensional grown object, together with an unworked queue of the
checks that would secure it.  That queue enters the ranking near the top,
not because the results are citable (they are not) but because the cost of
not knowing whether they hold is now high.

And a problem that had been quietly filed under "the earlier corpus" —
**the empty bridge** of §C5 — becomes load-bearing, because arrow 4's
Einstein content lives on the far side of it.

### ② THE OBJECTS

**What the construction queue has already delivered**, so that the
ranking below is a ranking of what is *left*: the grammar **tiles**
(§B8.6); it tiles **wide** at `d = 2`, witnessed by the forced 177-event
DOUBLE-RING(8, 10, 8) (§B8.7); its charts' **transition maps are
measured** and their class is a **coboundary**, so the atlas is globally
trivializable and no structure group is exhibited (§B8.8); the **descent
conditions** are gated one by one against the closed generated law, which
fails the commuting-square identity by exactly one mass-ratio coboundary
while the settled completion's measure genuinely descends (§B2.10); and
**conflict tiles and takes the width ceiling at every size built** — the
arbitration crystal is built, the ceiling is refined to the live
out-degree (`k·b ≤ k²`, "3+
registers" corrected to "3+ **proposers**"), delivery-free double grids
**realize it at `k = 3` and `k = 4`** and height-levelled chains at
`k = 5` and `k = 6` (9, 16, 25, 36), and `DOUBLE-GRID(4, 4)` sits inside
**both** `d = 3` sprinkling band columns **as a whole record** while
carrying `max |D| = 16`, with its class a coboundary too (§B8.9); and the
**functional slot** above the closed law is measured by exact rank
(§B2.11) — the consistency cone is large and structureless (`cohdim = coh`
everywhere, 15,058 at `D = 5`, measure-independent, positivity never
binding), and the first fair **dynamical** demand takes `cohdim` to
**zero** at every depth tried, so at closed scope a quantum layer cannot
be both state-generated and coherent; **the measure route** is opened and
measured (§B9.7) — the relative-horizon kernels proper to `r = 7`,
contraction at every pool and depth measured including a 318,704-history
four-actor arm, the root protected by an automorphism **theorem**, the
menu-exact renewal atom closed and the σ-level class open, with
operator-level minorization named as the one surviving proof engine;
**the phase segment** is welded and measured (§B2.12) — closed-scope raw
flatness a **theorem** with a budget-coincidence scope clause, the
normalised kernel never flat, **transport scope CURVED** by 88
delivery-bearing squares invisible to the record-graph instrument, the
transport holonomy a **new object** (`2/3`, `3/2` outside `⟨5/4⟩`), and
everything exhibited `R₊`-valued with **no `U(1)` part anywhere yet**; and
**the rank-2 question** is asked and answered on this substrate (§B8.10) —
the even Gram anisotropic with a trivial stabiliser on the fixture paper
30 selects, and nonetheless a **covariance, not a metric response**, with
`FAILS-FULL-GR` standing.  Most of those are negatives or carry one.  All
are results, all are terminal, and each changed the
ranking — by removing an expected object, by pricing a known one, by
**finishing** the line's top-ranked construction rather than handing it a
successor, by turning the programme's widest gap from an
emptiness into a measured negative with an address, and now by producing
the first non-trivial loop structure the corpus owns.

**Re-ranked against the destination** (superseding §A11.4 / §B11.4's
ordering, not their content):

1. **THE TRANSPORT HOLONOMY, CHARACTERISED — the era's hinge**
   (§B2.12, §B9.7's scope, §B8.10's successor).  Probability transport is
   **curved at transport scope**: `88` of `1,546` closed exchange squares
   at `(A,B)` depth ≤ 4 return `dP_AB/dP_BA ∈ {1/2, 2/3, 3/2, 2}`, with
   `40` further half-open at `±∞` and `12` more at three actors — **every
   one delivery-bearing**, the shallowest at total depth 3, and **`0` of
   them visible** to the record-deletion-graph census, because a square
   closes at record level exactly when its two events are
   register-disjoint.  It ranks first because **one measurement moves
   three fronts**:
   *(i)* **the phase.**  Everything exhibited is `R₊`-valued.  The
   imaginary exponential's last known address is the **odd sector** of
   exactly these loops, and the corpus's own shelved amplitude form
   (`A(R) ~ e^{−K(E)}e^{iΦ(O)}`, dual-conjugation error exactly 0) says
   that is where a phase would sit if there is one.
   *(ii)* **the metric's off-diagonal.**  v2 p10 Prop 10.6 is an all-order
   no-go that the real shadow **loses** `h^{12}`, and §B8.10 confirms
   experimentally that the even channel delivers a covariance, not a
   metric.  If the odd sector carries an argument, the destination's chain
   — modulus builds space, phase completes and legislates it (§D1) —
   becomes a programme; if it does not, the founding slogan is settled
   **negatively**, which was pre-registered as equally publishable.
   *(iii)* **the gauge question.**  `2/3` and `3/2` lie **outside**
   `⟨5/4⟩`, so this is not D65's coboundary family — the first evidence
   anywhere in the corpus that a transition class here might be a genuine
   `H¹`, and the only candidate site the gauge road has that is not a
   hope.
   **The unit's four questions, in order:** what carries it at record
   level (a delivery-aware record functor, or the holonomy is genuinely
   sequence-level and the record layer loses it); the group; coboundary or
   `H¹`; and the odd-sector `U(1)` search.  **Its substrate choices absorb
   the old TRIPLE-GRID item**: a third concurrent conflict axis was the
   one untried construction that might give the nerve loops the chart
   instruments could see, and it is now correctly posed as *one of the
   substrates a transport-holonomy unit may run on* rather than as a
   separate construction — since §B2.12 shows the chart instruments are
   the wrong instrument for this question in the first place.  Its three
   original questions (does the dimension profile past depth 2 depend on
   the number of axes; does a third axis produce loop structure; does
   crossing **select** a `k`) are carried unchanged and unanswered.
   Two structural constraints the unit inherits: `A_D = 0` along the
   one-dimensional commit path, so **any phase must live transverse to
   commit order**; and the `±∞` squares are a **support**-level defect
   that no holonomy formalism in the corpus currently handles.
2. **THE BOUND — the measure's existence theorem** (§B9.7).  The horizon
   route is the only route to a transport-scope measure that needs
   finiteness nowhere, and it is measured rather than hoped: proper at
   every computable `(h, r)` out to `r = 7` over 243,769 histories;
   contraction at **every off-root depth, in both conditional norms, at
   two, three and four actors**, the widest arm 318,704 histories; the
   truncation horn **protected at the root by a symmetry theorem**
   (`A ↔ B` and `0 ↔ 1` exact automorphisms, one orbit per event kind, so
   every equivariant terminal is forced) and measured to shrink off it.
   **What is missing is one theorem.**  The menu-exact renewal atom is
   **closed** — holdings never shrink, 0 re-entries, `0.7705` of depth-5
   completed mass never regenerating — but the **σ-level class R-SIG is
   open**: re-entered 3,796 times, `N`-step hitting zero-set collapsing
   `2520 → 84 → 4 → 0`, 4-step infimum `118/1455 > 0`, *the shape of a
   Doeblin condition*.  The named and unattempted engine is
   **operator-level minorization — Birkhoff / Hilbert-metric contraction
   of the positive backward recursion `G`**, and/or a genuine Doeblin
   condition, neither of which needs an atom.  It ranks second because
   §B11.2's four frontiers — space-making that is engineered rather than
   emergent, unselected dimensionality, unposable typicality, and the
   evicted quantum layer — **are one object, and this is it**.
   *Residues that come with it:* the four-actor depth-5 horizon extension;
   `G_8` (a ~1.9M-history depth-7 family) to say whether the root's
   `×7.509` reversal at `r = 6 → 7` is one turn or an oscillation; a
   systematic family of **non-equivariant** terminals, which is what
   actually probes the root invariance; and R2 at a cap where merges have
   support, since its closure is currently **inherited, not measured**.
3. **A RANK-2 RESPONSE ON GENERIC GEOMETRY** (§B8.10).  Two live routes
   and neither is the direction index of a hand-built crystal.
   *(a) The selected fixture.*  Paper 30 `§27`'s triple is the one place
   in the corpus where a genuinely anisotropic even Gram with a **trivial
   stabiliser** (`0.511428`) sits on a law whose forward error is
   **exactly zero**.  Why `§27`'s coarseness rule lands on a triple whose
   second moment is *more* anisotropic than the falsified target's is a
   question about the **selection rule**, not about the Gram — and the
   cheapest open question in the whole unit is whether that `0.511428`
   survives centring, reweighting and the `N` window, none of which were
   run on it.
   *(b) Sprinkling charts and defected crystals.*  Every `DOUBLE-RING`
   gives 100 % stabiliser-8 and two matrices **because a double ring is
   built with cyclic symmetry**; the narrow control is sometimes exactly
   `(1/4)I`.  A large stabiliser means *fewer* free components, so **a
   form with a big stabiliser is a cage, not a metric**, and a tensor
   stage needs **stabiliser-1** direction geometry.  Nobody has built one.
   Carried with it: `F3` — the anticommutator of the generated line's own
   transports, symmetrised — is **OPEN and explicitly deferred**, and the
   **odd** sector's off-diagonals (`−0.01220, −5.64990, +0.39107`,
   mixed-sign, one large) have never been scanned, the ceiling argument
   that would have made that hopeless having been retracted.
4. **THE MISSING MAP'S FUNCTIONAL LEVEL — THE DEMAND'S UNIQUENESS, AND
   THE SAME SLOT AT TRANSPORT SCOPE** (§B2.9, §B2.10, §B2.11) — the
   corpus's **deepest** named front and still its **widest**, and one of
   the few items on this list whose next two moves are *named computations*
   rather than a method problem.  It ranks below items 1–3 only because
   each of those is a single measurement that would move it, not because
   anything about it has narrowed further: it is still the one
   gap that makes two ledgers out of one programme, and the
   destination's last arrow is unreachable in principle rather than
   merely unbuilt until it closes.
   **What now exists on it:** paper 29's conditional descent theorem
   (decoherence, one atom, positive mass, boundary sufficiency) with its
   exhibited failure mode (erase a setting record and sufficiency
   breaks); the **first measured segment** — the generated law's
   normalized kernel fails the commuting-square identity on 32,256 of
   425,334 refined-record-identical ordered pairs, by exactly the
   coboundary of the per-state menu mass, zero exceptions, nothing
   sampled, while its *unnormalized* weight is order-independent
   everywhere and `Zhat`'s measure descends on all 5,548 record classes;
   and the **second** — the functional slot itself, measured by exact
   rank at closed scope (§B2.11).  That second measurement is what
   re-shaped this item.  **Consistency does not structure coherence:**
   under paper 29 §4.3's own condition `cohdim = coh` at every depth and
   in every variant (15,058 at `D = 5`), nothing is forced, positivity
   never binds, the classical member is interior, coherence survives even
   between different-parent-record histories (exact PSD witness), and the
   entire table is **measure-independent** — a fact about `canon` and the
   prefix map, not about the law.  **And the first fair dynamical demand
   eliminates all of it:** require the coherence excess to be generated
   by the closed law's own state space — the classical member passes, so
   the demand excludes nothing — and `cohdim = 0` at depths 2, 3, 4 and
   5, where consistency alone left `0 / 50 / 744 / 8,074` *(imposed on
   the strictest of the three C1 readings, whose entrywise rows pin the
   generating kernel; the faithful reading's answer to the same demand is
   move (a) below)*; the
   permitted/forbidden split is **invisible** to that state space
   (15/15, 28/28, 32/32 σ-state pairs carry both kinds).  **At closed
   scope a quantum layer cannot be both STATE-GENERATED and COHERENT.**
   **So the two next moves, both computations, both unrun:** *(a)* the
   **demand's uniqueness** — the faithful reading against the same
   dynamical demand (its cross-class rows are sums and do not force the
   kernel pointwise, so the answer is not implied), and then a second
   generation ansatz; *(b)* the **same slot at transport scope**, which
   is where the elimination points and where the conflict weights, the
   mass jump and the whole dimension mechanism already live — and which
   nothing in §B2.11 reaches.  Neither is a method problem; both are
   receipts nobody has written.
   **Still missing, unchanged:** a derivation rather than a supply of the
   identified law's boundary state, measure, record instrument and
   **generated record grammar** — and, on the generated side, a *derived*
   functional level rather than a measured space of candidates.  D65's
   DC3(2) is **narrowed, not discharged.**
5. **Is there a record-level demand that cuts the repair cone?**  The old
   form of this question — *is there a record-level demand that forces
   the stationary form?* — had two strongest candidates and their
   conjunction eliminated by measurement (§B6.12), and nobody has a
   third.  It now has a number on it from the other side (§B2.10): the
   positive repair cone is **573**-dimensional at the depth-4
   truncation, the completions that also **descend** are **205** of
   those, the `(depth, sigma)` family is **28**, and `Zhat` is one ray.
   Descent cuts 573 to 205 and no further; **the collapse to one ray is
   the form choice**.  A depth-free statement of the cone is the same
   question again, and it is the successor D50 and D65 jointly hand
   forward.  And it is doubly interesting for the destination: if the
   answer is permanently no, §D3's resemblance is the *only* interpretive
   home the boundary freedom has — a reason to state it carefully rather
   than a reason to believe it.
6. **WHAT IS LEFT OF THE WIDTH ROAD — two proofs of reach, not a
   construction.**  The arbitration crystal that three units converged on
   is **built and terminal** (§B8.9), and of its three questions it
   settled one, answered one negatively, and left one unbridged.
   *Settled:* conflict **tiles** — 21 three-proposer and 11 four-proposer
   configurations, zero refusals — and the width door is not merely open
   but **walked to its end at every size tried**: §B8.7's
   `|D_e(d)| ≤ B^d` refined by **W4c** to the live out-degree `Bl^d` (the
   minted version register is a **dead wire**), so the depth-2 ceiling is
   `k·b ≤ k²` and D63's "3+ registers" is corrected to **"3+ proposers"**;
   and that ceiling is **realized at `k = 3, 4, 5, 6` — 9, 16, 25, 36** —
   by forced, delivery-free records whose directions are read off the
   committed sky, with **height-levelling** (the grammar's own `('n', a)`
   idle) as the mechanism and the height condition itself definitional.
   `DOUBLE-GRID(4, 4)` carries `max |D| = 16` **and** sits inside both
   `d = 3` sprinkling band columns **as a whole record**, so the expected
   width-uniformity frontier **does not exist**, and 16 lies inside the
   sprinklings' `[10, 17]` — a hull of an `M21` cluster `[10, 11]` and an
   `M31` cluster `[14, 17]`, so inside the 3+1 one and outside the 2+1
   one, on the **maximum** column only.  *Answered negatively:* the
   transition class is a **coboundary** there too, at all five port
   conventions and by all three routes, on both 16-wide substrates, so
   the gluing motivation is spent (item 7 below).  *Unbridged:* the
   transport-scope mass census measures the excess above the actor count
   in quarters — non-zero exactly where conflict groups are open — and
   says plainly that it does **not** reproduce §B2.10's two-actor
   `2 → 5/2` values.
   **What is left are residues, and they are proof-shaped:** a
   **general-`k`** statement that levelling always meets the height
   condition (four sizes measured is not a theorem), and whether a
   **tiling** schedule exists above `k = 4` at all — with whole-record
   band membership at `k ≥ 5` untested, the `k = 5` and `k = 6` witnesses
   being chains rather than tilings.  Both are out of the current
   receipts' computational reach, and neither blocks arrow 3.
   The mechanism to carry forward, in its corrected two-level form: **a
   second direction is a second CONCURRENT CONFLICT AXIS**, and what a
   second axis buys is that the follow-on arbitrations sit at
   **height + 1** — which a levelling pass supplies without any crossing
   at all.  One dispute per actor makes the cycle a chain of diamonds and
   carries nothing; **transport is needed only to seed and rotate, never
   to make space.**
7. **THE GAUGE QUESTION, and its honest state.**  *Can any record at all
   carry a transition class that is not a coboundary?*  The corpus's
   answer is currently **no, everywhere it has looked**, and it has now
   looked in the place it had a structural reason to expect a yes.
   **Three substrate families** — delivery circuits (§B8.8), pair-conflict
   rings, and crossed-conflict double grids (§B8.9) — at **five** port
   conventions and by **three** routes (the `Z/2` cochain, a parity route
   defined on the maps the cochain drops, and free per-chart relabelling,
   the largest possible gauge group): **zero obstructions**, every time.
   The one non-zero count in the corpus is the **odd-ring** port-flip
   residue, and it fails every test of being a class — its magnitude is
   `R − 1`, a count of *rounds* rather than a ring or cohomological
   quantity; free relabelling trivializes it; there is **no Čech
   2-skeleton** for it to live on (zero testable triples); the group name
   is undetermined (10 consistent subgroups of `S₄`, two incomparable
   minimal); and genuine sprinklings obstruct at the same route.  So the
   deliverable §D1b's rule 2 names — *tensorial transition behaviour* — is
   still empty, and the bar a candidate must now clear is explicit: a
   substrate with a **non-zero obstruction count that survives free
   relabelling**, on a nerve with a **non-empty 2-skeleton**, at more than
   one port convention, and with the count identified as an invariant
   rather than a schedule parameter.  Nothing in the corpus is near it,
   and exactly **one** untried site is named on the chart side: a
   **third** concurrent conflict axis, on the thin structural hope that
   crossing three ways gives the nerve loops that crossing two ways does
   not — now folded into item 1's substrate choices, since §B2.12 shows
   the chart instruments are the wrong instrument for this question.
   **The real candidate is item 1 itself:** the transport exchange
   holonomy is non-trivial, lives outside every chart instrument's domain,
   and takes two values outside `⟨5/4⟩`.  It is the first thing in the
   corpus that could clear the bar above, and if it too turns out to be a
   coboundary the gauge road has no candidate site left at all.
8. **A workable BOUNDED description at transport scope** — distinct from
   item 2, which needs none.  Menu-exact is
   impossible for any design (§B9.1); sector-exact at `(actor, type)`
   granularity is closed by the refinement measurement (§B9.4b), on one
   ground rather than the two first published; and the two cheap
   coarsenings (type-only, total-budget-only) both blow up and turn out to
   be **one test rather than two**, since they induce the identical
   partition on the decider's whole input (§B9.7).  The
   surviving candidates are inexact / observable-only abstractions and a
   level-structured description with `|holdings|` as the level — both
   untested, with the finite-alphabet prerequisite `[OPEN]` either way.
9. **The two empty bridges (§C5, §C6.11).**  Arrow 4 —
   the only Einstein content the corpus owns — lives on the v6 side of a
   bridge that has never carried a measurement (the Fisher identity, Gb2,
   specified and unrun).  And v9's webs stand in the same relation to the
   v10 grammar, with the additional twist that a user directive
   *declares* them not to be the click law.  **Two unbridged bodies of
   work, one theory.**
10. **A Lean-grade mechanization of the delivery-free settlement.**  The
   residue-1 line is **closed at its scope** (§B6.13b): the `sigma`
   update is written out event by event — five rows — and its three
   obligations are discharged (the dropped-base token forced up to
   renaming; fresh version-name non-collision by admissibility; Lemma 7b
   feeding the components), so (H0), (H1) and (H2) are all in hand and
   D44a's closure theorem is unconditional there.  What remains is the
   *kind* of certainty: both proofs are prose-over-code, gated against
   the committed source at every cached transition and re-derived
   independently to depth 9, but never checked **as an induction** by a
   machine.  Small, bounded, and no longer blocking anything.  **Three
   actors remain out of scope entirely**, the dichotomy's proposer test
   being the clause that fails there, and transport is untouched.
11. **The `G` calibration.**  Not solvable — that is the theorem — but the
   *dimensionless* question it leaves open (is `c_m = Gm²/ℏc` a record
   output?) is explicitly **eligible** and is the natural arrow-7 target.
12. **The residual pricing defects** (`h12`; the general-depth ladder;
   the `1/16` vs `1/24` merge), unchanged and still carried into the
   completion problem rather than patched.
13. **Residue 2, REOPENED: which sky reading is physically privileged?**
    All three readings are live (§B5.4); the dimension discriminator is
    sharpest under the cover reading while much of the constructions line
    was computed under the antichain reading.  Nothing justifies a choice,
    and several conclusions depend on one.

**One structural observation, and it is the most useful thing in this
part.**  **Everything now points at the same address.**  Arrows 5 and 6
are blocked on a probabilistic description at **transport scope**; arrow
3's dimension mechanism was proved to live at transport scope; the
measure defect's own successor question is a transport-scope one; the
functional slot, having been measured at closed scope and found to
admit no state-generated coherence, hands superposition to transport
scope by elimination; and the **phase**, hunted through three version
lines, has its last known address in the odd sector of the *curved
transport loops* — which are, themselves, the corpus's only non-trivial
loop structure and its only untried gauge candidate.  **Five fronts, one
place** — and that place has just stopped being an analytic void: it has
one measured curvature waiting to be characterised (item 1) and one
measure route waiting on a single theorem (item 2).

Against it, the ledger of moves is short and honest, and for the first
time it is a ledger of **computations** rather than of method problems.
There are **two** measurements that would each move several fronts at
once: characterising the transport holonomy (item 1) and bounding the
horizon limit (item 2).  There is **one** cheap named computation left
from the quantum side, the uniqueness of the dynamical demand (item 4a).
There is **one** unbuilt object with a clear specification, a chart
substrate with generic direction geometry (item 3).  The rest are method
problems rather than build problems: the missing map's derivation side,
with no unit having a method for it, and the width road's proof-shaped
residues (general `k`; a tiling above `k = 4`).  And one front that used
to have a named next move no longer needs one: after the ceiling was taken
at four consecutive sizes, the search for width is finished.

**What is honest to say about the shape of it.**  The programme has
`R₊` everywhere and `U(1)` nowhere.  It has a mechanism that makes space
and no principle that selects one; it has a rank-2 object that is a
covariance; it has a measure route that contracts and does not converge;
and it has, for the first time, a loop that does not close.  **The
destination's whole chain now hangs on whether that loop has an
argument.**

---

## D5. The destination in one paragraph

> The programme's goal is not to make its records resemble a discretized
> flat spacetime — a target the measurements do not support.  It is to
> build **full Einsteinian manifolds, enriched until
> quantum particles can be created in them**.  Of the eight arrows from
> the primitive to a laboratory number, two are in hand (a causal order; a
> local geometry whose complexity is priced in actors), two are half in
> hand (Einstein's equations *in form*, with Newton's constant provably not
> derivable from inside; a quantum lift of the record process at fixture
> scale), three are open (charts and gluing into a manifold — whose first
> four questions are answered, since the grammar demonstrably tiles, tiles
> *wide*, glues its charts **trivially** — the transition maps being real
> but removable by a per-chart change of convention, so no structure group
> is exhibited — and then breaks the delivery width ceiling from the one
> direction a theorem left open: crystals made of **crossed conflicts**,
> with no messages inside their rounds, tile at cadence and carry
> **nine**- and **sixteen**-direction charts, reaching the corrected
> ceiling exactly at every dispute size built (nine, sixteen, twenty-five,
> thirty-six, by height-levelling with the grammar's own idle event), the
> sixteen-wide one sitting inside **both** sprinkling band columns one
> chart depth down **as a whole record**, so there is no
> width-uniformity frontier and real spacetime's ten to seventeen is
> matched on the width statistic; whose remainder is a substrate that
> glues non-trivially — none has been found,
> across three substrate families at five conventions **on the chart
> instruments** — while the one connection those instruments provably
> cannot see, probability transport itself, turns out to be **curved**:
> eighty-eight closed exchange loops returning `1/2`, `2/3`, `3/2` and
> `2`, every one carried by a delivery, two of the four values outside the
> group of the corpus's known coboundary — and two
> proof-shaped residues, a general-`k` statement and a tiling above four
> disputants, plus the rank-2 object the arrow is *for*, which on the even
> channel is an honest anisotropic form with a trivial stabiliser and
> still a **covariance rather than a metric response**; fields on it;
> particle creation),
> and the last is blocked
> at four independent points, one of which is the un-derivability of the
> scale and one of which is the incompleteness of the other arrows.  Governing all of
> it is the scale doctrine: no fixture-scale object is a particle, and
> units certify scale-invariant mechanisms rather than objects — which
> the substrate line reaches independently, since without coupling no
> collective excitation exists at any scale.  The **measure at transport
> scope**, on which four separate frontiers jointly wait, is no longer a
> void: the horizon route needs no bounded summary, is a genuine law out
> to horizon seven, **contracts at every pool and depth measured**, and is
> protected at the root by a symmetry theorem — what it lacks is a
> **bound**, and the operator-level minorization that would supply one is
> named and unattempted.  The **missing map** remains the deepest front,
> all three of whose measured segments are negatives with addresses: the
> generated law's normalized kernel does not descend to a record measure,
> by one repairable mass-ratio defect, while the settled completion's
> measure does; the quantum layer such a law could carry, counted
> exactly at closed scope, is **large and structureless** — consistency
> permits coherence everywhere and prices it nowhere — while the first
> fair demand that the coherence be generated by the law's own state
> leaves **none of it at any depth tried**, so at that scope a quantum
> layer cannot be both state-generated and coherent, and the generated
> line still has no *derived* functional level at all; and the **phase**,
> which the corpus did not lack but found, receipted and shelved three
> version lines ago, is exhibited nowhere in v10 — every loop the theory
> owns returns a **positive real number**.  So what ranks first is a
> single characterisation: **does the curvature of probability transport
> carry an argument?**  The destination's working hypothesis — that the
> modulus builds space and the phase completes and legislates it, the
> corpus's own no-go having proved the real shadow loses the metric's
> off-diagonal — stands or falls on it, as does the last candidate for a
> non-trivial gauge structure and the address to which superposition was
> handed by elimination.
> And one line that has been open since the beginning is now shut: in the
> delivery-free two-actor sub-theory the measure question is **closed**,
> at that scope and inside its postulated shape.
---
---

# GLOSSARY

One line each.  Chapter references are to Part B where the object is
defined precisely, and to Part A where the intuition lives.

| term | definition | where |
|---|---|---|
| **actor** | the primitive holder of history: sequential, with its own version chain, addressable, and the source of width; physically **uninterpreted** by design | B1.1, A1.2 |
| **admissibility** | the past-local relation deciding which events may occur next; complete, executable, exhaustively enumerable | B2.3, A2.2 |
| **A7** | the governing principle: *the opportunity set is the past-local admission relation and nothing else* | B2.4 |
| **A7' (the ladder)** | per-initiator weight sums equal `1 + k/4` at the record points of the enumerated families; **false at general depth** under current pricing | B2.7, A2.3 |
| **arbitration** (`'r'`) | the event that resolves a conflict component and **is** acceptance — it creates the successor version | B2.2, A2.1 |
| **arc / cap** | shadows of a circle sky / a sphere sky; arcs shatter 3 and never 4, caps on `S²` shatter 4 and never 5 | B5.2, B7.5, A5.3 |
| **backflow** | a delivery joins **both** wires, so the sender's line absorbs the receiver's accumulated past | B3.4, A3.4 |
| **bisimulation** | the equivalence "these two states cannot be told apart by any sequence of observations"; *probabilistic* bisimulation also requires matching weights.  The **quotient** is the state space after collapsing bisimilar states | B6.9 |
| **candidates_for** | the single function that returns exactly the admissible next events with exact weights; the sole authority on admissibility, never re-implemented | B2.4, A2.2 |
| **canonical class** | a history identified up to the gauge (order of incomparable events); 427 at depth 4 | B3.1, B4.1 |
| **carrier / wire** | the grammar's primitives are wires (participants and version objects); an event's carriers are the wires it touches, and the event poset is the carrier-wise wire closure | B2.1 |
| **causal order vs gauge** | causal order is **physical**; incomparable order is **GAUGE** | B3.1, A3.1 |
| **causally blind join layer** | a layer where knowledge is transported past a causally blind seal (e.g. a relay delivering a fork branch to a third party); `k` in `1 + k/4` counts these, and this is what the naive normalizer double-counts | B2.7, B6.3, A2.3 |
| **click** | one discrete recorded event; "the click law" is the whole event grammar plus its weights | B2, A2.1 |
| **completion** | strictly positive cut data `Z` with transfer `q'(e\|h) = q(e\|h)·Z(h+e)/Z(h)`; what turns the weight system into a probability law | B6.1, A6.1 |
| **courier** | a freshly minted single-use actor that delivers into an empty receiver, so nothing folds back — the device that makes the shatter constructions work | B8.2, A8.3 |
| **cut** | a slice through a record; a candidate "now" | B3.1, A3.1 |
| **cut complex** | the graph of cuts with single admissible steps as edges; 1,191 histories / 427 classes / 202 diamonds at depth 4 | B4.1, A4.1 |
| **delivery** (`'d'`) | transmission of a version from sender to receiver; carriers `{s,r}`; a **join of knowledge**; re-delivery admissible and physical | B2.2, A2.1 |
| **diamond** | the smallest loop in the cut complex — two independent steps in either order.  **Three senses in this corpus**: (1) cut-complex cells (the 202), (2) paper 3's amalgamation figure, (3) paper 29's action-level flat squares.  **Not** Alexandrov intervals | B4.2, B4.4, A4.5 |
| **dimension meter** | max-shatter read as a dimension signature: 3 = circle-compatible, 4 = sphere, 5 = `S³`, `k` = `S^(k−1)`; a **(record, reading) pair** property.  Exact for **continuum** trace systems; discrete sprinklings read `≈ 0` in every dimension, so for a record it measures engineered coordination, not dimension | B5.7, B7.5, A5.7, A7.2 |
| **Dilworth gate** | `[THEOREM, unconditional at transport scope]` one actor's worldline contributes a **chain** of traces, so a `k`-actor shadow family is a union of ≤ `k` chains, so shatter-`k` costs `≥ C(k, ⌊k/2⌋)` actors | B7.3, A7.3 |
| **direction** | a member of a sky's direction set at an event | B5.1, A5.2 |
| **foliation** | a sequence of cuts, i.e. **one linear extension** of the record's causal order | B3.1, A3.1 |
| **foliation-invariance** | demand (b): the completed conditional is a function of the record alone (class-constant); equivalently chain products agree across every linear extension | B6.2, A6.2 |
| **form (the stationary form)** | paper 30 §5.7's postulated shape `Z(h) = f(state(h))·λ^(−depth(h))`; what delivers uniqueness — **and a CHOICE, not a law**, now priced twice over: no record-level invariance forces it (freedom 12 / 32 / 125, growing), and no descent demand forces it either (573 ⊃ 205 ⊃ 28 ⊃ 1) | B6.11, B6.12, B2.10, A6.8 |
| **frontier sum `N(h)`** | the total raw weight of `h`'s menu; cut-attached (constant on all 427 classes) but **not a discrete gradient** | B6.1, B6.3 |
| **gauge** | see *causal order vs gauge* | B3.1 |
| **genesis** (`'g'`) | the initial version held by all participants — *"the declared supplied boundary"* | B2.2, A2.1 |
| **gradient / Doob `h`-transform completion** | the backward recursion `Z(h) = Σ q(e\|h)Z(h+e)` from a positive terminal boundary; exists at every finite depth, at the cost of within-cut ratio deformation | B6.5, A6.5 |
| **(H0), (H1), (H2)** | the three depth-indexed hypotheses of D44a's conditional theorem: view invariants; **menu factorization from `sigma`**; transition determinism.  None implies another.  At two-actor delivery-free d42a scope **all three are discharged** — (H0) and (H1) via the own-view dichotomy, (H2) via the five-row update table — so the closure theorem is **unconditional there**.  **Three actors remain out of scope**, transport is untouched, and the form remains a choice | B6.9, B6.13, B6.13b, A6.9 |
| **harmonic** | `Z` satisfying the backward recursion exactly; residue 1 asks for a **strictly positive** harmonic function on the infinite-volume state space | B6.9, A6.7 |
| **`h12`** | the one constructed configuration off the `1 + k/4` ladder (per-actor sum `23/24`), caused by a dead component inflating a live denominator | B2.7, A2.3 |
| **holdings** | what an actor holds; propagate only through participation or delivery.  At transport scope the delivery enumerator reads the **whole** set, superseded members included — the fact that decides §B9 | B2.2, B9.1 |
| **join-view lattice** | `V_S = View(h, pred, ⋃_{a∈S} O_a)` for non-empty actor subsets — the object a transport-scope menu is actually a function of | B3.3, A3.3 |
| **kernel (K1 / K2)** | the two posited arbitration winner laws: uniform order-click plus greedy, versus uniform over maximal independent sets; they disagree observably (`2/3` vs `1/2`) | B2.6, A2.5 |
| **ladder excess** | `N − 1`; sits at `k/4`, one quarter per causally blind join layer | B2.7, B6.1 |
| **menu** | the set of admissible next events at a history with their exact rational weights — exactly what `candidates_for` returns | B2.4, A2.2 |
| **menu-exact** | an abstraction determining menus as renamed event multisets **with exact weights**; §B9's no-go is about exactly this class | B9.1, B9.5 |
| **merge** (`'m'`) | local reconciliation by the holder of both versions of a pair; supersession is pair-scoped so reconciliation recurses | B2.2, A2.1 |
| **mint chain** | an actor's versions must descend from that actor's own latest version; the obstruction to actor aggregation | B1.1, B1.2, A1.4 |
| **noop cone** | the set of events an actor could see purely from its own causal past; the **menu view strictly exceeds it** | B3.2, A3.2 |
| **own view / full view** | the sub-record one actor has witnessed / everything in the history.  **Actors act on their own views, which LAG the full view** | B3.2, A3.2 |
| **Perron tilt** | the exact characterization of what the settled completion costs: `q'(e1)/q'(e2) = [q(e1)/q(e2)]·[f(class(h+e1))/f(class(h+e2))]` — each option re-weighted by the record-growth capacity of the state it leads to, and by nothing else | B6.10, A6.9 |
| **proposal** (`'p'`) | a local record event on the proposer's wire referencing a held copy of a base; carrier `{a}` alone, which is what makes conflict grammatically possible | B2.2, A2.1 |
| **record / record line** | the whole generated structure / one actor's succession of versions.  *Actor is to line as particle is to worldline* | B1.1, A1.1 |
| **renewal** | a record point structurally **isomorphic to the root** — event-level bijection, type- and payload-matched with `v0 ↔ v1`, **equal `q` at every matched event**.  "root = renewal" means the root sits in this class | B6.8, A6.7 |
| **residue 1** | *does a strictly positive harmonic function exist on the infinite-volume state space?* — answered YES and **CLOSED at two-actor delivery-free d42a scope**, the scope clause being part of the sentence (§0.3): still inside the stationary form, still delivery-free, three actors out of scope | B6.9, B6.10, B6.13b, A6.7 |
| **the update table** | the five-row `(hold, live, comps, refs, sup∣refs)` update — idle / propose-on-a-held-base / propose-on-a-**dropped** base / self-arb / pair-arb — each row a proof read off the committed layer, with no depth parameter and no read of the history.  It proves (H2); its corollaries are that the arbitration **winner is invisible to `sigma`** and that **every pair-arb renews to the root state** | B6.13b, A6.9 |
| **rootedness** | a completion distinguishing the root from the renewal point, i.e. distinguishing two record points the law identifies; what truncated completions do and `Zhat` does not | B6.8, A6.7 |
| **capacity condition (sky)** | the honest requirement before a shattering test can be read as a measurement: `≥ 4` directions **AND** `≥ 16` distinct traces.  An earlier version added *and the empty trace present*; that clause **false-negatives** and is withdrawn (§B5.4) | B5.4, A5.5 |
| **sector** | one of the four weight budgets (propose / arbitrate-and-merge / deliver / idle), each `1/4` when open, idle absorbing the rest.  The **delivery** sector total is `1/4` at every rung of §B9.1's ladder — but that is **not a law of sectors**: arbitration sectors reach `1/2` and `1/8`, totals live in `{k/(4m)}`, so the sector alphabet is not finite either | B2.6, B9.4, B9.4b, A9.4 |
| **shadow / trace** | the set of directions at or below a given future (or past) event — the objects all the sky geometry is done on | B5.1, A5.2 |
| **shatter** | realizing **all** `2^k` subsets of a `k`-set of directions as traces; requires the **empty** trace | B5.3, B5.4, A5.3 |
| **`sigma`** | the bounded local-state abstraction of the **full view** modulo base renaming: holdings pattern, live-proposal structure with conflict components, superseded marks restricted to referenced bases.  36 values at d42a; **unbounded, menu-exactly, at transport scope** | B6.9, B9.2 |
| **sky** | the direction set at an event, under one of three committed definitions: **SKY-A** covers, **SKY-B** an antichain at a committed height, **SKY-C** the dual past sky.  **All three are live readings** and they disagree materially; which is physically privileged is open (residue 2) | B5.1, B5.4, A5.2 |
| **supersession** | a version is superseded when a later version on the same line replaces it; superseded structure may still be recorded but may no longer be actionable | B2.3, B9.1 |
| **swept corner** | the sub-family of proposal branches where the enumeration is complete and every extension factor is exactly `1/8`, making ratio locality a theorem there | B6.5 |
| **`tau`** | `sigma`'s construction applied to an actor's **own view**; **refuted** as an own-view object (D46a) | B10.2, A10.2 |
| **transport scope (d42b1)** | the grammar with delivery and merge; where the dimension results live, where the measure question is **open** (with the horizon route the only one walked, §B9.7), and where probability transport is **curved** (§B2.12).  Five separate fronts now address it | B2.2, B6.14, B9, B9.7, B2.12 |
| **VC dimension** | the largest set a family of sets can shatter; caps on `S²` have VC dimension **4**, which is why the sphere never shatters 5 | B7.4, A7.2 |
| **version** | the content object a line writes; created only by arbitration or merge | B2.2, A1.1 |
| **view** | see *own view / full view*; a view is a **sub-record**, nothing psychological | B3.2 |
| **`Z`** | the completion's positive cut data; `Zhat = 2^(−\|h\|) f(class(sigma(h)))` is the settled one at d42a scope | B6.1, B6.10 |
| **`Zhat`** | the settled root-free completion: `λ = 2`, `f = (4,4,3,7,3,3)/3`, unique up to scale **within the form** — and the unique positive `λ = 2` harmonic completion of that form whose measure **genuinely descends**, `μ_Zhat` being constant on all 5,548 record classes of the family (gated, and not implied by the square identity) | B6.10, B2.10, A6.7 |
| **action line** | the corpus's *other* dynamics stream (papers 13/15/18/19, D20–D27): quantum-mechanical — amplitudes, class operators, a decoherence functional — with durable clicks only after a record instrument is **supplied**.  It **presupposes spacetime** | B2.9, A2.6 |
| **D15 action** | the Standard Model plus effective gravity at the measured couplings; the conditional measure of the whole-history process it generates **is** the identified click law over the tested energy domain | B2.9 |
| **generated-law line** | the stream of Parts A and B (papers 26–32, D34–D58): record-closed conditional laws on generated carriers, culminating in the d42a/d42b grammar.  Constructed, receipt-anchored, **generates** causal structure, **presupposes no spacetime** | B2.9 |
| **identified law** | the third sense of "the click law": empirically anchored — *identified, not derived* — and **not proved record-closed**.  Distinct from the grammar's admissibility law (complete) and its probability law (not self-normalizing) | B2.8, B2.9, A2.5 |
| **the missing map** | paper 29's name for what stands between the two streams: *"the action line and the generated-law line now meet at one missing map"*.  The corpus **supplies rather than derives** the identified law's boundary state, measure, record instrument and **generated record grammar**, so that law is **not yet proved record-closed**.  Partially bridged by the conditional descent theorem; the corpus's deepest named front.  **Three segments are measured**, all from the generated side only: the descent defect (§B2.10), the **functional slot** (§B2.11) and the **phase** (§B2.12).  The second **narrows and does not discharge** the widest stretch — there are still no *derived* class operators and no *derived* Gram functional, so paper 29's decoherence hypothesis still holds *for the empty reason*, but the space of candidates is now exactly counted and carries one hard negative; the third finds the corpus's own shelved amplitude form and measures the only object that could supply its argument | B2.9, B2.10, B2.11, B2.12, D4 |
| **no silent erasure** | `[POSITED]` every loss of a record-accessible distinction must be **received** by records — total content conserved, sealing = dispersal, never intrinsic destruction.  The principle that closes the action line's coherence clause, with a parameter-free falsifier | B2.9, A2.6 |
| **chart-size ratio (`ω`)** | the atlas instrument's overlap statistic on cover pairs.  `[THEOREM]` the smaller chart is *contained* in the larger, so `ω` is the ratio of their sizes and Jaccard similarity is identically equal to it — it therefore systematically favours **thin-charted** records | D2 (Road 1), B8.6 |
| **crystal** | a record built to **tile** rather than to spike: the brick wall — ring actors, one minted version broadcast, then alternating re-delivery rounds.  Forced by the layer's own menus, sprinkling-grade homogeneity, above-sprinkling `ω`, **thin charts** at `d = 2`; the shortfall from a perfect tiling is entirely boundary.  Coupling two of them gives the *wide* crystal; replacing the deliveries with disputes gives the *arbitration* crystal, and crossing two conflict axes gives the *double grid* | B8.6, B8.7, B8.9, A8.6 |
| **height-levelling** | the cheap mechanism that makes the width ceiling attainable: pad an actor's auxiliary registers with the grammar's own `('n', a)` **idle** events until all `k` depth-1 consumers of an arbitration sit at exactly **height + 1**, where SKY-B(2) counts their own successors rather than only themselves.  No new lineage, delivery or arbitration.  It is what carries `k²` to `k = 5` and `k = 6` (`ARBCHAIN**`), what recovers the depressed first-round chart in `LEVELLED-DGRID(4, 2)`, and what shows phase separation is *a* route to the condition and not the lever | B8.9, A8.9 |
| **`ARBCHAIN*` / `ARBCHAIN**`** | the smallest width witnesses.  `ARBCHAIN*(m, k)`: one `k`-proposer arbitration whose `k` proposer registers are consumed by `m` further `k`-proposer arbitrations and `k − m` deliveries, realizing `k·m + 2(k − m)` — the whole interval `[2k, k²]`.  `ARBCHAIN**(k)` is `ARBCHAIN*(k, k)` **height-levelled**, realizing `k²` at `k = 3, 4, 5, 6` (47/90/157/254 events); its `k = 5` member is the campaign's highest forcedness grade — full-menu replay **157/157**, widest menu **2,125** — and carries **25** directions verified against the committed sky and order.  *(D66's own `arbchain` hardcodes three-proposer secondaries and does not generalize past `k = 3`, where nothing it gated is wrong.)* | B8.9, A8.9 |
| **discriminator (max-shatter)** | `[REFEREE-CARRIED + coordinator-confirmed]` on genuine sprinklings at sufficient density, read under SKY-A, max-shatter reproduces the continuum ladder: `M^{2+1}` shatters 3 never 4; `M^{3+1}` shatters 4 never 5.  Size-controlled two-sided separation | B5.7, A5.7 |
| **disjoint-row lemma** | shattering `S` requires a row **disjoint from `S`**, not an empty row — the two coincide only when `S` is the whole direction set.  Its narrow true corollary: for a reflexive transitive poset a cover sky can never shatter its **full** direction set | B5.4, A5.5 |
| **own-view dichotomy** | `[THEOREM, two actors]` a candidate's own view is **either** the initiator's register cone **or** the FULL view — no third case: register geometry alone *produces* a third case, and `arb_components_in_view`'s **proposer test** removes it.  The engine of (H1)'s proof and of the update table's row preconditions; **fails at three actors**, where the third case is admissible | B6.13, A6.9 |
| **invisible supersession** | an actor's own token is alive in its cone but superseded in the full view, because the opponent self-arbitrated the shared base and the actor has not seen it.  The mechanism behind "a smaller view can yield MORE options", and the content of the update table's row R2′ — the same **9,656** events under three descriptions | B3.2, B6.13b, A3.2 |
| **wide crystal** | the **built** composition of the two certified construction mechanisms — tiling (the brick) and width (the couriers) — in one record.  Witness **DOUBLE-RING(8, 10, 8)**: 177 events, 16 actors, forced with all actors offered at every step; `d = 2` homogeneity `47/59` in band with `\|D\| ≥ 4` at a third of its events.  A `d = 2` statement: at `d = 3` the uncoupled brick already meets the pattern.  It is also the substrate on which the **transition cocycle** is measured, and on which that cocycle's class is found to be a coboundary.  **Superseded as the corpus's widest object** by the delivery-free *double grids* (`max \|D\| = 9` at `k = 3`, **16** at `k = 4`, the latter in band on both `d = 3` columns as a whole record) | B8.7, B8.8, B8.9, A8.7, D2 |
| **transition map** | the translation between two overlapping charts' coordinates — where a manifold's structure lives.  Read here from **wire words**: a direction's label in a chart is the set of register sequences realized by `P`-paths to it, `P` being `event_poset`'s own generating relation.  Every atlas result before D64 assumed these were identities; measured, 115 of 172 overlapping pairs of the wide crystal are not, and each non-identity one is a **partial** map on 2 of 4 fibre points (the 29 total maps are all identities).  On the wide **conflict** records the length-preserving transitions are outright identities at four of the five port conventions, so what carries the non-vacuity there is a probe's failure to fire, not a triple count | B8.8, B8.9, A8.8 |
| **cocycle (transition)** | the consistency condition on transition maps around a triple of overlapping charts.  Satisfied on all 111 testable triples of the wide crystal and on **every** tested triple of every substrate, controls and sprinklings included — 993 triples, zero violations.  *Satisfying it does not make an atlas non-trivial*: it is a precondition, not evidence | B8.8, A8.8 |
| **coboundary / `H¹ = 0`** | a transition class is a **coboundary** when a per-chart relabelling `ε` turns every transition into the identity; then `H¹ = 0`, the atlas is globally trivializable, the holonomy of every loop is trivial and the transitions are **pure gauge**.  On the delivery crystal it **is** one — 0 obstructions over 60 charts in 9 components, `ε` at 32/28, all 108 non-identity transitions relabelled away, at two independent port conventions — **and so is every conflict substrate**, at five port conventions and by three routes (§B8.9).  **The obstruction count is the test**; non-identity transitions, a clean cocycle and a group name are all compatible with triviality.  **And the verdict's domain is the chart atlas over the record graph** — probability transport itself is a different connection on a different carrier, and it is **curved** (see *transport holonomy*) | B8.8, B8.9, A8.8, B2.12, D2 |
| **descent (of a click law)** | the condition that a law's conditionals come from one measure on records, so that `P(a\|H)P(b\|Ha) = P(b\|H)P(a\|Hb)` whenever both orders name the same record.  The generated law's **raw** weights satisfy it everywhere; its **normalized** kernel fails on 32,256 of 425,334 refined-record-identical ordered pairs, by exactly `M(σ(Hb))/M(σ(Ha))` — the coboundary of the per-state menu mass, zero exceptions.  `Zhat`'s measure **does** descend (constant on all 5,548 record classes).  Distinct from **decoherence**, which is a demand on a functional *above* the law (§B2.11) and not on its conditionals | B2.10, A2.7 |
| **repair space** | the completions that annihilate the descent defect.  At the depth-4 truncation the positive cone has dimension **573**; **205** of those also descend; the `(depth, sigma)` family is a **28**-dimensional slice; `Zhat` is one ray.  Repairing the squares and descending imply each other in **neither** direction (two exact positive witnesses).  **The collapse to one ray is D50's form choice, not descent** — and "the completions are precisely the repair" is blacklisted (§0.3) | B2.10, B6.12, A2.7 |
| **the functional slot** | the missing map's *functional* segment made computable: the exact space of Hermitian forms `D(h,h')` over the truncated history layer that reproduce the record measure (C1), are PSD (C2), are cylinder-consistent (C3) and renaming-equivariant (C4).  Measured by exact rational rank at closed scope, depths 2–6.  **Existence is trivial and weak** (the classical diagonal member is positive definite and interior, and `diag(w)` works for *any* strictly positive cut-consistent weight), so the pre-registered outcomes *empty* and *coherence forced* are both excluded.  **A measurement of candidates, never a construction of one** | B2.11, A2.8 |
| **faithful reading (of C1)** | paper 29 §4.3's actual decoherence condition written on the fine layer: `D̄(r,r') = Σ_{h∈r,h'∈r'} D(h,h') = δ_{rr'}·μ_Ẑ(r)` — the **coarse-grained** functional is diagonal with the record measure down it.  The headline of §B2.11 and the only one of three readings that is a stated condition of the parent paper.  Its two bounds: the **sum** reading (`r = r'` only — drops decoherence entirely, and its rows are independent at every depth, so it can reject nothing) and the **block** reading (entrywise zeros across record classes — forbids by hand the cancellations coarse decoherence permits).  **Both bounding readings produced a withdrawn headline** (§0.3, §B10.15c) | B2.11, A2.8 |
| **coherence cone** | the within-class off-diagonal freedom in the functional slot.  Under the faithful reading it is **never priced**: `cohdim = coh` at every depth and in every variant (9 / 134 / 1,491 / 15,058 at `D = 2…5`), positivity never binds, and an exact PSD member carries coherence between histories whose **parents carry different records**.  And the whole table is **measure-independent** — the coefficient matrix never sees `μ_Ẑ`, so it is a fact about `canon` and the prefix map.  **Dimension is not volume**: nothing measures how *much* coherence a member may carry (the witness sits at 1/72 of its own entrywise PSD ceiling) | B2.11, A2.8 |
| **the dynamical demand (C5)** | `D = diag(μ_Ẑ) + E` with `E(h,h') = μ(h)μ(h')·K(σ(h),σ(h'))`, `K` symmetric and zero on the diagonal — *the coherence excess is generated by the closed law's own state space*.  **Fair**: the classical member is `K = 0`.  It gives **`cohdim = 0` at depths 2, 3, 4 and 5**, where C1–C4 alone left `0 / 50 / 744 / 8,074`, because the permitted/forbidden split is **invisible** to `σ` (every σ-state pair carrying a permitted coherence carries a forbidden one: 15/15, 28/28, 32/32).  Hence: **at closed scope a quantum layer cannot be both STATE-GENERATED and COHERENT.**  Imposed on the **block** bound; the faithful reading's answer is unrun, and **the demand's uniqueness is the segment's sharpest residue** | B2.11, A2.8, D4 |
| **the horizon limit** | the route to a transport-scope measure that needs finiteness **nowhere**, and so meets none of §B9's walls: condition on the record having `r` steps of future left, and push `r` out.  `[MEASURED]` proper at every computable `(h, r)` to `r = 7` over 243,769 histories; drift **contracts at every off-root depth in both conditional norms at two, three and four actors** (widest arm 318,704 histories).  **No bound is exhibited and the word *converges* is banned from the receipt's labels** — what is delivered is *"root-free over the computed horizons"*, explicitly not a boundary theorem | B9.7, A9.6 |
| **relative-horizon kernel** | `k_r(e\|h) = q(e\|h)·G(h+e, r−1)/G(h, r)`, `G` the positive backward recursion.  The **pinned object** is its *sector-normalized conditional*; absolute completed weights are horizon-bound (D44f) and are **context** — a doctrine that must run in one direction, since running it per-gate is how a unit selects the object that maximises its own headline | B9.7, A9.6 |
| **the horn (truncation convention)** | the rule for `G(h, 0)`.  The five declared conventions differ at **every single history**, so the truncation is a **choice, not a formality** — but at the **root** they cannot differ at all: `A ↔ B` and `0 ↔ 1` are exact automorphisms of the layer, the root menu is **one orbit per event kind**, and therefore every *equivariant* terminal is forced to the same root conditional.  `[THEOREM]`  A **non-equivariant** terminal separates by `1/6` at `r = 1`, which is what makes this a statement about the terminal's **symmetry class** rather than about horizons.  Off the root the pinned separation is measured to shrink | B9.7, A9.6 |
| **R-SIG / R-MENU** | the two transport renewal classes.  **R-MENU** (holdings exactly `{v}` for every actor) is absorbing-complement — holdings never shrink `[EXACT]`, 0 re-entries — so **the menu-exact atom route is CLOSED**, with `0.7705` of depth-5 completed mass never regenerating.  **R-SIG** (every actor's *non-superseded* holdings a singleton) is **re-entered 3,796 times**, its `N`-step hitting zero-set collapsing `2520 → 84 → 4 → 0` with 4-step infimum `118/1455 > 0` — *the shape of a Doeblin condition*.  **The σ-level renewal route is OPEN** | B9.7, A9.6 |
| **minorization (the named engine)** | the missing bound's only surviving candidate: **Birkhoff / Hilbert-metric contraction** of the positive backward recursion `G`, and/or a genuine Doeblin condition `P^N(x,·) ≥ δν(·)` on R-SIG.  Neither needs an **atom** — the atom version was quoted as if it were the general one.  **Unattempted anywhere in the corpus** | B9.7, D4 |
| **the amplitude form (v7's survivor)** | `A(R) ~ e^{−K(E)}·e^{iΦ(O)}` — real decay on the reversal-**even** channel, phase on the reversal-**odd** one, dual-conjugation error **exactly 0** where the naive `e^{iS}` continuation is falsified.  Receipted in v7 paper 30's complex-amplitude campaign, **never lifted to a theorem**, and cited nowhere in v10 until the archaeology found it | B2.12, A2.9 |
| **order-dual (`*`)** | v7's reversal of a record's own order relations; `E = F + F*` is even under it and `O = F − F*` odd.  On the generated line it coincides with transport-order reversal `AB → BA` **as partial maps on two-event histories and on nothing larger**; the labelled order-dual exists for only 294 of 1,558 v10 record classes, and the *order-type* statistic is different and `k`-dependent | B2.12, A2.9 |
| **the weld** | the one sentence the corpus never wrote: that reversing a record's internal order **is** running a transport loop backwards.  Its two halves are separately proved — v6 paper 7's `U(1)` holonomy theorem and v7 paper 30's receipted conjugation-under-reversal.  **The identification leg survives; the holonomy leg dies at closed scope and revives at transport scope** | B2.12, A2.9 |
| **`A_D` (the exchange defect)** | `A_D = log dP_AB/dP_BA`, the log-holonomy of probability transport around a closed exchange square.  **`≡ 0` at closed scope on the placement grammar, as a `[THEOREM]` at every depth** (L1–L6); **non-zero at transport scope**.  Also `0` along the one-dimensional commit path, so **any phase must live transverse to commit order** | B2.12, A2.9 |
| **budget coincidence** | the scope clause on closed-scope flatness, and the decisive half of it: lemmas L4 and L6 hold because the propose-budget `1/4` and the arbitrate-budget `1/4` are **equal and mutually exclusive** in an actor's own view.  **A tuning of d42b3, not a structure** — change either constant and the register-overlapping squares stop being flat, which is exactly what happens one grammar over | B2.12, §0.3 |
| **transport holonomy** | the corpus's first non-trivial loop structure: at transport scope **88 of 1,546** closed exchange squares return `dP_AB/dP_BA ∈ {1/2, 2/3, 3/2, 2}`, with **40** further half-open at `±∞` and 12 more at three actors — **all delivery-bearing**, from depth 3, and **invisible to the record-graph instrument** (record-closure `⟺` register-disjointness, and `μ` is an exact gradient where the instrument *can* see).  **A NEW object**: `2/3` and `3/2` lie **outside `⟨5/4⟩`**, so it is not D65's coboundary family.  Its characterisation is the era's hinge | B2.12, A2.9, D4 |
| **the odd sector** | the reversal-odd half of a record, and **the imaginary exponential's last known address**.  The corpus's real odd object — `A_D` — is negative-definite in v7's analysis and becomes positive only after the `i`-twist; the even half hosts the metric's diagonal and the odd half the off-diagonal (v2 p10 Prop 10.6).  **Nothing in v10 exhibits a phase**: every holonomy value the programme owns is `R₊`-valued | B2.12, B8.10, A2.9 |
| **even Gram** | `G^even_{jk} = Σ_R P(R) E_j(R) E_k(R*)`, computed exactly by v7's reflection-positivity campaign, its minors printed and **the matrix itself discarded for its trace**.  Resurrected: anisotropic, positive-definite, three distinct diagonal entries, `S₃` stabiliser **order 1** on both fixtures.  And **a covariance, not a metric response** — no atom index, rank 1 locally, nothing acting on its index, predictively equivalent to its own trace.  Its *reflected* form **equals** the ordinary second-moment matrix, so paper 30 §25.4's positivity is algebra, not measurement | B8.10, A8.10 |
| **selected fixture** | paper 30 `§27`'s dual-pair triple `{(912,25104), (17288,525076), (24576,540672)}`, chosen by a record-intrinsic admissibility rule at `TV9 = rec9 = 0` **exactly** — as against the `§25` triple the same paper ranks **11th** and declares falsified, whose `1.676e-5` is the loser's score and a **sector-selection artefact** no function of the even 3-vector can reach.  The general rule: **anchor on a paper's own selection, not on the tables it prints before falsifying them** | B8.10, §0.3, B10.15e |
| **`h`-weight identity** | why every promoted `K` lands on the same `TV_9`: `forward_tv` depends on a colouring **only** through its atom-average weight function `h`, so a candidate whose `h` equals `full`'s at every record has an identical forward error **by construction**.  Gated as a biconditional at 18 candidates over two fixtures, zero mismatches.  It replaces an asserted **monotonicity of `TV_9` under refinement**, which was never proved and which the committed table itself contradicts | B8.10 |
| **stabiliser (as a cage)** | the criterion `F1` actually measures, read correctly: a metric response must **transform** under whatever acts on its index, so what matters is that the stabiliser be **small**.  A `D₄`-invariant `4×4` form is confined to a 3-dimensional span inside `Sym²(R⁴)`, where a stabiliser-1 `3×3` form is a generic point of `Sym²(R³)`.  **A form with a big stabiliser has fewer free components, not more** — which is why hand-built crystals are the wrong tensor stage and stabiliser-1 (sprinkling-like, or defected) geometry is the right one | B8.10, A8.10, D4 |
| **`FAILS-FULL-GR`** | v6 paper 4 `:1064`'s verdict that a scalar response cannot become a two-dimensional symmetric tensor equation by reinterpretation, on a per-atom component count.  **Half-cleared** (6 components against 1) and **still standing**, now on equivariance rather than counting: nothing acts on the channel index.  *(The number `789150` is p4's counting rule applied to D73's record count — **not in p4's units** and not commensurable with p4's `8193`, which was never recomputed.)* | B8.10 |
| **branching bound (W4b)** | `[THEOREM]` `\|D_e(d)\| ≤ B^d`, `B` = the largest register count of any event, proved from `event_poset`'s generating relation.  Deliveries carry `B = 2`, so **chart width 4 is the delivery grammar's ceiling at `d = 2`** and the sprinklings' 10–17 is unreachable by any delivery circuit; width past 4 **requires** arbitration over a multi-proposer conflict — a necessity, not a route, and **necessary but not sufficient** (see *W4c*) | B8.7, A8.7 |
| **W4c (the dead-wire refinement)** | `[THEOREM, proved from the committed layer]` the version register an arbitration mints is a **dead wire** — it occurs in no later event's `regs_of`, because a delivery carries a version in its **payload** rather than on its register, and two arbitrations minting the same `vname` would be causally comparable and the later one inadmissible.  So the operative branching factor is the **live** out-degree `Bl` (registers that recur), the bound is `\|D_e(d)\| ≤ Bl^d`, and an arbitration branches by its **proposer count**.  Hence a two-proposer conflict ring is held to 4 exactly like a delivery circuit, and **"3+ registers" is corrected to "3+ PROPOSERS"** | B8.9, A8.9 |
| **width ceiling (`k·b ≤ k²`)** | W4c's depth-2 form: `\|D_e(2)\| ≤ Σ_{y ∈ succ(e)} b(y) ≤ k·Bl ≤ k²`, on the exact containment `D_e(2) ⊆ succ(e) ∪ ⋃ succ(y)` (gated everywhere, exceptions characterised).  **Tight, and REALIZED at `k = 3, 4, 5, 6` — 9, 16, 25, 36** (double grids at 3 and 4, height-levelled chains at 5 and 6); the sharp form needs the `k` depth-1 consumers at **height + 1**, which is *definitional* (SKY-B counts at exactly height + 2), the empirical content being that the arbitration order decides it (`16 → 7` by re-ordering) and that a schedule can meet it at every `k`.  `2k` is only the `Bl = 2` corner — the value when every successor of an arbitration is a delivery — and `ARBCHAIN*(m, k)` occupies the whole interval `[2k, k²]` | B8.9, A8.9 |
| **double grid** | `DOUBLE-GRID(k, R)`: rows and columns conflicting **concurrently**, so every actor stands in two independent conflict lineages; `2g` lineages are forced by the grammar, since two concurrent groups cannot share a base.  At `k = 3`: zero in-round deliveries, total arbitration share `1/4`, C1-complete replay 72/72, **nine `\|D\| = 9` charts**, `d = 3` homogeneity `47/60 = 0.7833` in band on the homogeneity column only.  At `k = 4`: zero in-round deliveries (24 in the bootstrap), share `1/5`, **`max \|D\| = 16 = k²` at both depths**, and at `R = 4` (200 events) **inside BOTH `d = 3` band columns as a whole record** (`0.7250` / `0.6350`) — so the width-uniformity frontier does not exist.  Their transition classes are coboundaries at all five port conventions | B8.9, A8.9, D2 |
| **conflict budget bound** | `[THEOREM, verified; saturated by the ring]` an arbitration consumes `k` live proposal triples and no triple is consumed twice, so the arbitration share of any record is at most **`1/(k+1)`** with `k` the smallest proposer count in it.  **Three readings, never merged:** the delivery-free ring saturates `1/3` at `k_min = 2`; a double grid's bootstrap makes `k_min = 1`, so its **own** bound is `1/2` and is *not* saturated, while its total share sits exactly at `1/(g+1)` (`1/4`, `1/5`) by a printed coincidence of bootstrap and round; its **conflict** share is a third number (`2/15` at `k = 4`) | B8.9, A8.9 |
| **crossed conflict** | the corrected mechanism for chart width: what buys a second direction is a **second concurrent consumer of a proposer's register**.  Rotation buys one with a **delivery**; a concurrent **arbitration** buys a better one for free (`b = k` against `b = 2`).  One conflict lineage per actor makes the cycle a chain of **diamonds** and carries nothing.  So **transport seeds and rotates; it does not make space** — every ceiling-carrying record in the corpus is delivery-free.  Crossing is the *tiling* route to the height condition, not the condition: **height-levelling** reaches the same ceiling with no crossing at all | B8.9, A8.9, D4 |
| **arbitration crystal** | the successor **three** results named, now **built and terminal**: a crystal made of **conflicts** rather than of deliveries.  *(i)* **Width** — conflict tiles (21 + 11 configurations, 3,705 events, zero refusals) and takes W4c's `k²` at **every `k` built: 9, 16, 25, 36**, with a whole 16-wide record inside both `d = 3` band columns.  *(ii)* **Gluing** — answered **negatively**: the class is a coboundary on conflict substrates too, at every convention and by every route, so the two-port-symmetry motivation is spent.  *(iii)* **The measure** — the `2 → 5/2` jump is a d42a statement and the transport-scope mass census does **not** bridge to it.  What is left are two proof-shaped residues: general `k`, and a *tiling* above `k = 4` | B8.9, B8.7, B8.8, D4 |
| **odd-ring residue** | the campaign's one non-zero obstruction count, on **grammar** records: pair-conflict rings with an **odd** number of pairs per round.  Resolved as **parity** at five ring sizes, with the magnitude `R − 1` — a count of **rounds**, not a ring or cohomological quantity.  Free relabelling trivializes it, there are **zero testable Čech triples** behind it, the group name is undetermined, and genuine sprinklings obstruct at the same route: reported, **not claimed** as `H¹ ≠ 0` | B8.9, A8.9 |
| **axioms R / S / C** | the earlier corpus's three: laws are laws of whole sealed histories; **no distinction without a record**; couplings fixed by self-consistency under refinement | C1 |
| **Barandes-indivisible** | a process whose one-time transition law fails Chapman–Kolmogorov except at sparse **division events**; the barrier is the gap between `\|Σ\|²` and `Σ\|·\|²` — the interference cross-term | C1, C3 |
| **Born = K1** | the statement that a constructed isometric arbitration family's squared branch amplitudes reproduce the committed `K1` kernel exactly (`1/2`–`1/2` on the 2-conflict, recomputed from the layer).  Appears in v10 paper 31 §4.3; the earlier Born layer (paper Va) is the same *kind* of statement — **relation formally unestablished** | C3.5, C5.4 |
| **chart / gluing** | the local-patch and overlap-agreement structure that turns a causal order into a **manifold** — arrow 3 of the destination, still `[OPEN]`, and the first construction the destination newly requires.  Charts exist and tile (`§B8.6`), tile wide (`§B8.7`), their gluing is measured and **trivial** (`§B8.8`), and crossed conflict takes the corrected width ceiling at every size built — **9, 16, 25, 36** — with the 16-wide record also in band (`§B8.9`); what is unbuilt is a substrate whose gluing is *not* trivial, a general-`k` proof, and a tiling above `k = 4` | D2, B8.8, B8.9 |
| **covariantization** | the result that a **Poisson sprinkling** of division events makes the kinematic layer Lorentz-invariant outright (no recoverable frame; arrow in the causal order, not a slicing; Hegerfeldt dissolved for the free flash), converting the GRW/CSL foliation wall into named dynamical residues | C3.6 |
| **CP-divisibility** | an open-system channel property: the dephasing rate stays `≥ 0`, so no information backflow and **no revivals**.  **Orthogonal** to Barandes-indivisibility — neither implies the other | C3.1 |
| **division event** | the record at which an indivisible stochastic process momentarily factorizes; the primitive of the causal-set gravity sector, where *order + number = geometry* | C1, C3.6 |
| **G no-go** | `[NO-GO]` the absolute scale `σ_A` (weight `−2`), in bijection with Newton's `G` (weight `+2`) via `G·σ_A = 1/4`, is not derivable: every intrinsic record functional is weight-zero, so `κ·σ_A = 2π` and `G·Λ²` (two **separate** fixed pure numbers) are all that is fixed | C2.2 |
| **graviton blindness** | 4 of 9 stress components priced universally; the 5 traceless ones spanned but only at a boost-dependent second-order coupling; four obstructions reducing to one root — the needed structure lives only in a continuum algebra a finite record lattice cannot host.  The geometry is **spin-2-active but not-a-graviton** | C2.5 |
| **holonomy (sealed)** | the coherent, uncommitted relative phase a system carries **between** seals; sealing destroys it.  Its irreducibility is the earlier corpus's quantum/classical dividing line.  **Distinguish three things the corpus calls holonomy:** this one; the *chart* holonomy of an atlas, which is trivial on every substrate measured (see *coboundary*); and the *transport* holonomy of probability itself, which is **not** trivial (see *transport holonomy*).  The SHARD↔Barandes dictionary identifying sealed holonomy with the interference cross-term is a `[TARGET]`, not a theorem | C1, B2.12 |
| **Jacobson–Clausius conditional** | the four named premises carrying the equation-of-state route.  **The internal asymmetry:** the weight-counting no-go depends on none of them — *the wall stands unconditionally, the `G`-naming of it is conditional* | C2.6 |
| **quarter law** | `[THEOREM A, v6 paper 26]` `−ln BC = σ/4 + (ε²/6)σ + O(σ³)` — coherent capacity decays at one quarter of the evidence rate, `BC` the Bhattacharyya overlap, `σ` the KL.  **In the weak-evidence limit the ¼ is measure-theoretic universality** (the *universality trap*), so confirming it elsewhere would be a fake bridge | C1 |
| **refinable** | a history in which an intermediate conditioning record could have been inserted for free; **classical**.  Unrefinable = the seal order cannot be refined without changing the process | C1 |
| **seal** | an irreversible record commitment; the earlier corpus's primitive act, ancestor of v10's *click* — **by postulate, never by measurement** (§C5) | C1 |
| **seal-is-record postulate** | the `[POSITED]` identification of the earlier corpus's *seals* with the later corpus's *records*.  **Never instantiated**; "the bridge is empty"; its first falsifiable test (the Fisher identity `J_wp/J_arrow`) is specified and unrun | C5 |
| **SHARD** | *Sealed Holonomy And Record Dynamics* — the earlier programme's name | C1 |
| **the two σ's** | a resolved **name collision**: `σ_wp = D(P₀‖P₁)` (which-path KL, the quarter law's `σ`) versus `σ_arrow = D(P_fwd‖P_rev)` (the arrow KL, the covariance argument's `σ`).  v10's `sigma` is a **third**, unrelated use — a state abstraction | C5.2, B6.9 |
| **three walls** | the classification of what the record law provably cannot supply: **SCALE** (`G`; measured, route-conditional), **TENSOR PRODUCT** (contested convention), **MODE** (import-fixed) — one quotient-by-symmetry shape, three residual types, *two structural no-gos plus one conditional* | C2.6 |
| **vacuum ambiguity** | `[LITERATURE]` in QFT on curved spacetime, particle content depends on a vacuum choice not fixed by the dynamics.  Its **resemblance** to the completion's boundary freedom is recorded as a labelled, costed, untested speculation — *at least three unbuilt arrows away from being a question* | D3 |
| **Walsh–delta** | the corpus's mathematical spin-off (own repository): the delta orientation is the unique entropy minimizer for self-calibrated ±1 Walsh tilts; Theorem 6.1's dichotomy (`N·D > 2.878716` vs `N·D_δ ≤ 64/63`) closes it analytically for `n ≥ 6`; Lean-verified but for one finite computation | C4.4 |
| **weight (length-weight)** | the grading under the gauge `l_step → μ·l_step`.  **Theorem G:** every intrinsic record functional is weight-**0**, while `σ_A` is weight `−2` — the whole `G` no-go in one line | C2.2 |
| **celestial clock** | one of `K` fixed directions `v_k` on `S²` in the v9 web; a deposit advances clock `k` through a kernel of `u·v_k`.  Dominance in all `K` clocks is the causal relation | C6.1 |
| **channel web** | v9's substrate formalism — a fleet of slots growing by commits, ordered by multi-clock dominance.  **A different formalism from the v10 grammar**, and declared by user directive **not** to be the interactive click law | C6.1, C6.11 |
| **channel-manifold law** | `d = dim(channel manifold) + 2` — index the channels by a *manifold* rather than a count; for 3+1 the channel space is `S²`, so *"why `C = 3`"* is superseded by *"why the sphere?"*.  Reached by first proving the previous target impossible | C6.4 |
| **churn** | the v9 reset process at rate `1/L`.  Four flavours across the arc: **per-clock** (starves the relation), **full-vector** (cures it), **conservation** (transfers content — the first coupling), **diffusion** (a continuous jump-free leak — the first significantly-rounder webs) | C6.1, C6.9 |
| **conservation-churn** | the minimal record-native coupling: a churned slot's accumulator is *added to* a receiver rather than destroyed.  Produced the programme's first measured **propagation of influence** (affected slots 0.6 → 3.6 against a control of exactly 1) — but left the cone residual **unchanged** (transfer redistributes the jumps) | C6.9 |
| **`d_ball`** | Myrheim–Meyer volume dimension read against a **dedicated ballistic-class calibration** (no clamps).  `3.84/3.85` at 45e's `P0/N1`; `4.44` at 48d — the latter reviewed down to **`4.4 ± 0.2`, protocol-conditional, instrument-suspect** (jackknife 7/10 flips) | C6.7, C6.9 |
| **deposit** | what one v9 commit adds: **direction-valued** — `u = p_s` with probability `α` else uniform on `S²`, magnitude `e ~ Exp(0.109551)` | C6.1 |
| **`F_iso`** | v9's shape statistic: PCA the transverse cloud to an effective 3-frame, take `q90` directional supports over a pinned 64-direction sphere, report `mean(top 8)/mean(bottom 8)`.  Round ⇒ ≈ 1.  Reference card: Gaussian 1.078, disk 3.044, simplex-interior 1.557 | C6.1, C6.3 |
| **free-web theorem** | with no coupling, slots never exchange content, so a perturbation influences **exactly one worldline** (*until that slot's next reset*) and **no collective excitation can exist at any scale**.  Verified mechanically.  **Matter requires coupling** | C6.8 |
| **parking** | v9's target: **round-occupied AND certified ≥ 4D simultaneously**.  Refused across ~60 dial points for every jump class; 45e's pre-registered re-test read **NOT-PARKED**; the diffusive class reads **PARKED-AT-PROTOCOL**, not parked | C6.3, C6.7, C6.9 |
| **scale doctrine** | `[BINDING, LOG #440]` no fixture-scale object may ever be called a particle (a particle is ~`10²⁰` spacings, ~`10⁶⁰` events); destination units certify **scale-invariant MECHANISMS**, never objects.  Composes with D48 and paper 57's free record scale, and **favours mode readings of "particle"** | D1b |
| **slot** | one of the `M` accumulators in a v9 fleet; the substrate's unit of locality.  **Not** an actor and not related to one by any unit | C6.1, C6.11 |
| **two-clock wall** | `[LEMMA]` an order defined as dominance in `k` clocks has order dimension `≤ k` (weak form: `≤ k+1` with an injective first clock).  Every early corpus web was two-clock, so `dim ≤ 2` **by definition** — the re-attribution that every earlier 3+1 refusal was structural | C6.2 |
| **zero class** | the arbitration-killing counterterm that restores normalization and is **declared excluded**, narrowing the no-go to support-preserving completions | B6.4, A6.4 |

---

# GAPS IN THIS DOCUMENT

What had to be compressed, and where the full account lives.  This list is
part of the document, not an apology for it.

1. **The v10 line's earlier papers are compressed, not absent.**  Of its
   32 papers the book develops 26–32 in full; the **action line** (13/15/
   18/19 and the D20–D27 units) gets one subsection per register
   (§A2.6, §B2.9) rather than a chapter, and paper 29's bridge audit is
   quoted rather than worked through.  Papers 1–12 — the SCIR rulebook
   line, the predictive-record-DAG boundary, the reception theorem —
   appear only where a later result cites them.  The action line's own
   ledger is `v8/LEDGER.md` #126–#130 and a reader wanting that stream in
   depth should go there and to paper 18 directly.

2. **Paper 31's four decisions are summarized in one table row each.**
   S1 (collar-bracket rule-independence, `κ(1/2) = 13/2304`,
   `κ(1) = −1/72`, with the sign flip closing a tempting explanation),
   S3 (the constructed arbitration operator at fixture scale, `V_single` /
   `V_pair`, Born = K1 at both cuts), and paper 32 §5 (the regulator closed
   for all masses) each deserve a chapter and get a line.  They are
   orthogonal to the two lines this document traces.

3. **The quantum layer is compressed.**  Paper 32 §4 (the eleven-type
   record census, foliation as one record datum, the forced weights welded
   to the completion) is mentioned in B6.14's scope statement and not
   developed.  The quantum lift's three-horn pincer is stated but its
   exhibits are not walked through.  And §B2.11's functional slot is
   reported at its two headline results, its three deflations and its
   controls: its full 32-row dimension table across all three C1 readings,
   all four C4/C3 variants and both the real and Hermitian columns is
   **sampled here, not reproduced** — the note and its receipt carry it
   entire.  **And the phase archaeology (§B2.12(i)) is a digest of three
   survey notes** running to some 3,100 lines between them: 24 cited
   appearances of the imaginary exponential across v1–v10, 8 reduction
   points, 5 attachment slots, the four-document disagreement over v6
   paper 7's status, and the full `SU(2)`-versus-spin-2 adjudication are
   compressed to a table and three paragraphs.  Those notes are surveys,
   not receipts, and every claim taken from them is quoted here as
   archaeology of **earlier version lines**.

3b. **The measure campaign's scoping survey is compressed to its
   conclusions.**  The walls-and-routes map (§B9.7's opening) stratifies
   **five** walls by evidential grade and enumerates and ranks **nine**
   routes to a transport-scope measure; this book reports the
   stratification, the fact that W-A kills only finite menu-determining
   summaries, and the top-ranked route.  The other eight routes, their
   rankings and the reasons for them live in the survey note.

4. **D46's six ladder units get one paragraph each at most.**  D46b
   (Martin at transport, three reversals) appears in B9.6; D46c (Minkowski
   certificates) appears only via `W3_CERT` in B5.3; D46d appears in B7.2;
   D46e in B2.8(v); D46f in B10.16; D46g (embedded-head reconciliation)
   only as the `1/16` vs `1/24` wart.  The three-round sweep that produced
   five headline reversals is characterized statistically rather than
   narrated.

5. **The receipt-level detail is sampled, not enumerated.**  Gate names
   are given where they carry a number a reader might want to check
   (`SG3b`, `TG2(c)`, `CG8`, `CG9`, `MV2`, `SF4`, `K11`, `G8`, `F3`,
   `H1`–`H6`).  Many gates in each receipt are not mentioned.

6. **Second-grammar (breadth) results are stated as a discipline, not
   developed.**  D42b7's ternary-payload grammar is cited for the
   two-of-two breadth rule and the toy-relativity of `λ = 2`; its own
   content (no state chain; component-shape-dependent kernel
   discrimination; the dimension pilot's honest null) is not covered.

7. **Two numbers I could not fully reconcile, flagged for the author.**
   (a) The D55 round's *"referee recount one rung down: 17/453 more
   genuine 2+1 skies certified non-arc"* — I could not determine from the
   ledger entry whether 17/453 is a fresh count on a different stratum or
   an increment to the 218/397 recount; I quoted it as a further recount
   and said so (B5.3).  (b) D55's result-note §4 says the completed measure
   is *"the only remaining candidate"* while the same round's MINOR 6
   widened the candidates to three; I used the widened version and flagged
   the conflict (B11.2).

8. **The `1,191` ambiguity is flagged but not chased through every
   citation.**  D50's own defect 3 established that the figure is
   cumulative (976 at the layer).  I note it once (B2.5) and do not audit
   whether every prior use of it in the corpus meant the cumulative
   reading.

9. **Part A's analogies are declared but not systematically stress-tested.**
   The scribes-and-notebooks picture (A1.1) and the supply-chain picture
   (A11.3) each carry one "where this breaks" note.  A more thorough
   treatment would break each analogy at every chapter where it is reused.

10. **No new computation was performed for this document.**  Every number
    is read from a committed source.  Standing of the sources, carried at
    each point of use: **D50, D53, D55c, D57, D58 and D60** are
    batch-round reviewed, repaired and delta'd; **D61** (§B6.13, the
    proof of (H1)) has had its own independent round, which confirmed the
    mathematics to depth 8 on a rebuilt layer and restated the headline;
    **D62** (§B6.13b, the proof of (H2)) likewise, its referee rebuilding
    all five rows from the prose alone and confirming them to depth 9;
    **D63** (§B8.7, the wide crystal and the branching bound) likewise,
    its referee rebuilding all 38 records and reproducing every figure
    exactly; **D64** (§B8.8, the transition cocycle) likewise, its referee
    rebuilding the record, the poset, the sky, the port conventions and
    the cocycle code, confirming every number and then running the
    coboundary computation the unit had not; **D65** (§B2.10, the
    descent conditions) likewise, its referee rebuilding the family, the
    state normal form, the record functor and the pair keys — *"every
    single number reproduces"* — and then computing the repair-cone
    dimension; **D66** (§B8.9, the arbitration crystal) likewise, its
    referee rebuilding all fifteen swept configurations with its own
    driver and its own instrument, reproducing every figure exactly,
    proving W4c's missing step — and then **building two records of its
    own**, one of which takes W4c's true ceiling at 9; and **D67**
    (§B8.9, the `k = 4` double grid) likewise, its referee rebuilding the
    whole family from the note's prose with its own driver, reproducing
    all 554 lines of the receipt byte for byte and the 16-direction
    witness event by event, and then **building three records of its
    own** — one more round of the unit's *own* blueprint, which put a
    whole 16-wide record inside both `d = 3` band columns and so **killed
    the unit's flagship negative**, and a height-levelled chain that
    carried the ceiling to 25 and 36; and **D68** (§B2.11, the functional
    slot) likewise, its referee rebuilding the family, its own `σ` normal
    form, its own constraint rows and an elimination pivoting the other
    way, reproducing *every* published figure — *"the arithmetic is
    flawless"* — and then computing the two things the unit had not: the
    parent paper's own decoherence condition, which **inverted the unit's
    coherence headline**, and the dynamical demand the unit's own residue
    had named and declined, which **inverted its verdict**; **D70**
    (§B9.7, the horizon limit) likewise, its referee rebuilding the
    family, its own backward recursion, its own five norms, its own
    terminal conventions and its own renewal predicates, reproducing
    **every single number** — *"I broke nothing in the arithmetic.  I
    broke the readings."* — and then **running the four-actor depth-4 arm
    the unit had named, priced and declined**, which re-graded the
    headline from a negative to a positive; **D72** (§B2.12, the weld)
    likewise, its referee rebuilding 6,471 histories, the deletion graph
    and the published constant to 32 digits, and then **supplying the
    depth-free theorem the unit had only sketched**, the transport-scope
    census the unit's instrument was structurally blind to, and the
    normalised-kernel computation the unit had not run; and **D73**
    (§B8.10, the even Gram) likewise, its referee reproducing every anchor
    character for character and then finding the **BLOCKER by reading 130
    lines further down a paper the unit had already opened** — the
    fixture's own falsification — plus the inversion of the transfer probe
    inside the unit's own evidence.  All eleven
    round 1 terminal.  **Round-supplied results are carried in this book
    as authorship**: the repaired receipts rebuild every referee figure in
    their own process and gate it, and none of it is copied.
    **D56** (§B9) is an advisory probe whose two load-bearing claims were
    independently re-verified and whose remainder must be re-derived.
    Two figures in §B5.7 and one in §B8.6 are `[REFEREE-CARRIED]`, and the
    discriminator's central comparison was additionally confirmed by the
    coordinator with independent code.

11. **The v1–v9 prehistory is covered in PART C, but unevenly.**  *(This
    item replaces the earlier "absent" note, which PART C discharges.)*
    **v1** (22 papers: collar excision, exchange defects, thin-slab laws,
    the Fock lift) and **v2** (10 papers: stochastic curvature, projective
    kernels, the QFT-reconstruction no-go) are **not covered at all** —
    they are the analytic prehistory of the record ontology and nothing in
    Parts A/B/D depends on them.  **v9**'s earlier rounds appear only through the
    seal-is-record design note (§C5); its own campaign — the churn webs,
    the discharge theorem, the stem spectrum, the round-cone investigation
    and the channel-manifold finding — is **not covered**, and at least one
    of those (the channel manifold: `d = dim(channel manifold) + 2`, with
    `S²` for 3+1) is plainly relevant to PART D's arrow 3 and is omitted
    only for length.  The **Yang–Mills** line (dozens of papers across v3
    and v4) gets one section; the **v6 publishable batch** gets a
    paragraph; **v5**'s quantum-computing arc (papers 3–13) is untouched.

12. **PART C's sourcing is abstract-and-key-section, not whole-file.**
    Paper 57 was read in full (127 lines).  Everything else was read at
    abstract / status-block / cited-section depth, plus targeted greps for
    each quoted number.  Every number in PART C was verified in-file at the
    point of quotation, but I did **not** read papers 26, 56, 1, Va, X, 14,
    39 or the v8 ledger end to end, and a claim of theirs that contradicts
    something I quote could be sitting in a section I did not open.

13. **PART C6's sources are the ledger and the design notes, not the v9
    receipts.**  Every number in C6 was verified in `v8/LEDGER.md`
    (#103–#128), `v9/LOG.md`, or the pinned design notes, but I read **no
    v9 receipt source and no receipt output**.  Where the ledger and a
    design note disagreed I followed the ledger; where a round's own entry
    and its later review disagreed I followed the review, loudly.  The v9
    papers themselves (papers 1–9, including paper 7 on the
    shape–dimension frontier and paper 8) are **not read** — C6 is an arc
    summary, not a reading of the line's own publications.

14. **PART D is mostly a roadmap.**  Arrow 3's first four segments are
    now results (the grammar tiles; it tiles wide at `d = 2`; its charts'
    transition class is a coboundary; crossed conflict reaches the
    corrected width ceiling on delivery-free records at every size built —
    9, 16, 25, 36 — with the 16-wide one inside both `d = 3` band columns
    as a whole record) and what is left of that arrow's width leg is two
    proof-shaped residues rather than an engineering question, but arrows
    6 and 7
    have no corpus content beyond being named, and their entries are
    statements of what is missing.  The `[MY READING]` in §D3 is
    speculation and is marked three times as such.

15. **Eight things this document leaves open, and a reader should not
    mistake for settled.**  (a) The **sky reading** — all three are live,
    the dimension discriminator is sharpest under the cover reading, and
    much of the constructions line was computed under the antichain
    reading; nothing reconciles them.  (b) The **sector closure**
    (§B9.4b) rests on measurement at reachable depths rather than on an
    obstruction, which is a materially weaker footing than §B9.1's.
    (c) **(H1)'s and (H2)'s proofs are prose-over-code** and cover two
    actors only; the book states both as theorems because the corpus does,
    with the Lean-grade mechanization residue and the three-actor failure
    stated every time.  Residue 1 is **closed**, and the sentence is only
    ever true with its scope clause attached (§0.3): two actors,
    delivery-free, inside the stationary form.  (d) The **triviality of
    the atlas** (§B8.8, §B8.9) is a measurement — now across three
    substrate families, at five port conventions and by three routes, all
    agreeing — which makes it a strong measurement and still not a theorem
    about the grammar; the **descent defect** (§B2.10) is exhaustive but
    confined to two-actor delivery-free scope, where the menu mass takes
    exactly two values, and §B8.9's transport-scope mass census does
    **not** bridge to it; and the **width results** (§B8.9) are two
    theorems — W4c and the conflict budget bound — surrounded by
    measurements on two swept families: `k²` is **realized at `k = 3, 4,
    5, 6` and at no size beyond**, which is four data points and not a
    general-`k` theorem; the `k = 5` and `k = 6` witnesses are chains and
    not tilings; and the band verdicts are **crossings** of monotone
    families read at particular round numbers, on populations of events
    rather than on objects.  None of these generalizes by itself.
    (e) The **functional slot** (§B2.11) is the newest and the most
    quotable-out-of-scope: every dimension in it is a **truncation**
    dimension with no proof behind the pattern; the whole table is a fact
    about one record functor and the prefix map rather than about the
    generated law; the verdict that a quantum layer cannot be both
    state-generated and coherent rests on **one** fair dynamical demand
    imposed on **one** of three readings of the record condition, with the
    faithful reading's answer to the same demand **unrun**; and nothing in
    it touches three actors, delivery, transport scope, or the identified
    law's own functional.  It **narrows** the map's functional segment; it
    does not discharge it.
    (f) The **horizon limit** (§B9.7) is a **table over computed
    horizons**, not a limit.  Every positive statement is contraction at
    depths and pools that were enumerated; **no bound was exhibited**, the
    receipt bans the word *converges* from its own gate labels, and the
    route is neither alive nor dead — it is untested at the one place that
    would decide it.  The root's exact `0` is a **symmetry theorem**, not
    evidence of stability, and quoting it as stability is the error the
    unit's own round corrected.  Nothing here is *the* click law's
    measure; the missing map is untouched.
    (g) The **flatness theorem** (§B2.12) is depth-free for **one
    grammar**, and half of its proof is a **budget coincidence** of that
    grammar's own constants.  Its transport-scope failure is `[MEASURED]`
    on two arms.  L6a's induction is verified exhaustively and not
    machine-proved; the `±∞` squares are a **support**-level defect no
    holonomy formalism in the corpus handles; and **no `U(1)` part is
    exhibited anywhere** — the phase is an address, not a result.  The
    archaeology's sources (v6 paper 7, v7 papers 30 and 42, v2 paper 10)
    are **earlier version lines**, cited here as archaeology and not as
    live corpus claims; one of them carries a **live erratum** (the
    quarter law's `BC` is only the Cauchy–Schwarz bound) that has not been
    routed to its dependants.
    (h) The **even Gram** (§B8.10) is fixture-scoped twice over: two named
    dual-pair triples, one window, one measure.  The anisotropy **rises
    monotonically across the whole window with no sign of saturating** and
    nobody knows whether it converges, diverges or is an artefact of `9!`;
    the *selected* fixture's value was never swept over `N`, centred or
    reweighted; the transfer probe is `[SAMPLED]`, seven blueprints at one
    depth; and `F3` — the anticommutator test the pin registered — is
    **open and explicitly deferred**, not decided.  Nothing here is a
    metric, a response, a field or a graviton.

---

*End of document.  `v10/THE-THEORY-SO-FAR.md` — the corpus's single
synthesis, current at the ledger state named in the maintenance stamp.*
