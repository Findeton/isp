# THE THEORY SO FAR

### The record programme explained twice: once for a reader with no mathematics, once for a reader who wants the objects

**Compiled 2026-07-26.**  Corpus: `~/workspace/isp`, v10 line, through
ledger entry **#433**.
Author of the research programme: Felix Robles Elvira (ORCID
0009-0009-2017-4394).
This document is a *brief*, not new research.  Every number in it was
read out of a committed source file while writing; nothing is quoted
from memory.

---

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
"green-unreviewed", and nothing may lean on it.  This rule has been
broken once in the recent record and the breach is itself on the record
(D49 round 1, MAJOR M4: the settlement banner was written into the
corpus's entry-point document in the same ledger entry that created the
unit, before any round).

**(2) Scope labels are part of the claim.**  "At d42a scope",
"delivery-free", "at transport scope", "reading-relative to SKY-B",
"at tested scale" are not hedges.  Dropping one turns a true statement
into a false one.  The single most common failure in the recent
campaign was a *true computation* wearing a *scope-free sentence*.

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
- **"H1 is discharged"** — it is not.
- **"infinite clocks via Sperner"** — withdrawn; the surviving route is
  trace counting (D54 round 1 BLOCKER 1).

---

## 0.4 The whole story in ten sentences

1. The theory posits a world made of **records**: finitely many
   sequential *actors*, each writing versions on its own line, who
   propose values, arbitrate conflicts, deliver knowledge to one
   another, merge divergent versions, and idle.
2. **What may happen next is completely specified** — executable,
   exhaustively enumerable, with one function in a committed program as
   the sole authority — and the *relative weights* of the options are
   specified too.
3. **What actually happens is not specified**: the options at a moment
   sum to 2 or 5/2, not to 1, and the framework's own code says in its
   docstring that it makes *no measure claim*.
4. Turning weights into probabilities is called **completion**, and
   there is a theorem: you cannot have normalization, independence of
   the time-slicing, and untouched relative weights all at once — 36 of
   the 202 elementary loops of the enumerated depth-4 world refute it.
5. Dropping the third demand, completions exist; and in the
   delivery-free two-actor sub-theory a **canonical one exists that
   needs no boundary condition at all**, is unique up to scale within a
   postulated shape for it, and prices the beginning of the record
   identically to a later point that the law itself cannot tell from
   the beginning.
6. But that shape is a **choice, not a law**: the two strongest
   invariance demands anyone has written down leave the freedom
   *growing* (10, then 28, then 107 dimensions as depth increases), so
   "the law completes itself" is true only of the law **plus** the
   shape.
7. Once deliveries are allowed — the scope where spacetime questions
   live — a short exact depth-free construction shows the menu of
   options grows without bound, so **no finite state summary
   reproducing menus exactly can exist, for any design**: the method
   that settled the measure question provably cannot travel there.
8. In parallel, needing no measure at all, the theory has a
   **geometry**: the directions leaving an event form a *sky*, and how
   complicated a sky can be is **priced in actors** — one actor's
   worldline can only ever sweep a nested family of shadows, so
   realizing all subsets of *m* directions costs at least
   *C(m, ⌊m/2⌋)* actors (6 for four directions, 10 for five).
9. Records were then **built** that pay the price: a 20-actor,
   42-event record whose sky no circle can host, and a 42-actor,
   84-event record whose sky no 2-sphere can host — so the
   admissibility layer does **not cap** the dimensional ladder at the
   sphere's rung, and whatever might prefer 3+1 is not in that layer.
10. Both lines therefore arrive at the same wall: *does anything prefer
    3+1?* needs either a measure at delivery scope (blocked by the
    unbounded-menu theorem), or a resource-cost principle, or a
    counting-typicality argument — and the corpus has **none of the
    three**.

---

## TABLE OF CONTENTS

### FRONT MATTER
- §0 What this document is
- §0.1 Provenance labels
- §0.2 The two disciplines
- §0.3 Forbidden sentences
- §0.4 The whole story in ten sentences

### PART A — THE THEORY WITHOUT MATHEMATICS

- **A1. The world as a record** — actors, lines, versions; how well
  defined an actor is; what is deliberately *not* claimed; why the
  number of actors is physics and not bookkeeping.
- **A2. The click law** — the six kinds of thing that can happen; what
  is completely settled (what *can* happen), what is settled but odd
  (relative weights), what is not settled at all (what *does* happen);
  the known warts.
- **A3. Relativity without a global now** — cuts, slicings, gauge;
  views that lag; delivery as a two-way join; why every law here must
  be slicing-independent.
- **A4. Diamonds, and the flatness test** — the smallest loops, why
  agreement on them is the whole condition, and the three different
  things the word "diamond" means in this corpus.
- **A5. The sky** — directions, shadows, and the three committed ways
  of saying "the sky at an event"; why two of the three can never
  work; the instrument that was demoted.
- **A6. The measure problem** — the impossibility, the escape, the one
  canonical completion, and why "the law completes itself" needed an
  extra postulate that turned out to be a choice.
- **A7. Buying dimension with actors** — why counting clocks was the
  wrong instrument; the shatter ladder; the theorem that dimension has
  a price in parallelism.
- **A8. Building the witnesses** — couriers, backflow, and the two
  records that pay the price; what they license and what they do not.
- **A9. The wall and the crack** — why the delivery-scope theory has
  no finite summary, and the one thing that survives.
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
  (i)–(v); the `h12` off-ladder configuration; the merge pricing
  divergence.
- **B3. Cuts, foliations, views, transport** — canonical classes; the
  own-view lag with its census; the monotonicity failure; the join-view
  lattice; the two-way join.
- **B4. The cut complex and the flatness ladder** — 1,191 / 427 / 202;
  the telescoping theorem; the three diamond senses disambiguated.
- **B5. The sky instrument** — SKY-A/B/C as the code defines them; the
  empty-trace obstruction; SC5; the capacity laws in their two
  variables; the demotion.
- **B6. The completion dichotomy** — the theorem, its forcing, the
  gradient class, the quantum lift, residue 1, the settlement, the
  form-is-a-choice result, H1 and its two dead routes.
- **B7. The dimension ladder** — the doctrine, the collapse of
  counting, the shatter ladder with its exact certificates, the
  Dilworth gate with proof, trace counting.
- **B8. The constructions** — the courier architecture; the shatter-4
  and shatter-5 records; the generalized builder; what is licensed;
  the controls.
- **B9. The transport wall and the sector crack** — the
  self-arbitration ladder; the design-independent no-go; what remains
  exact; the open sector-exact question.
- **B10. The graveyard, itemized** — claim, killer, survivor, for each
  retired object.
- **B11. Status, open problems, method** — the ranked residues; the
  papers; the review statistics.

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
  *representation choice* nobody has justified.  The clearest case: when
  a certain comparison was run over eleven different reasonable ways of
  grouping the same data, **sixteen** groupings gave one verdict and
  **nine** gave the opposite, and the verdict the corpus had previously
  announced was the wrong one.  Wherever this occurs the corpus now says
  "reading-relative" out loud, and treats "which reading is physically
  privileged?" as an open question rather than an implementation detail.

### A2.5 The one-sentence answer

*How well defined is the interactive click law?*

> **The admissibility layer is complete.  The probabilistic layer is
> provably not self-normalizing.**

Those are not two grades of the same claim; they are different kinds of
statement.  The first is a fact about a finished object.  The second is
a theorem about an unfinished one — and the theorem is what makes the
unfinished part interesting rather than merely incomplete.

> **What this chapter does NOT claim.**  That the weights are
> probabilities, or ratios of probabilities of anything observed.  That
> the quarter ladder holds at all depths.  That the two merge prices
> can be reconciled.  That the choice between the two arbitration
> kernels (two different, equally available rules for who wins a
> dispute) has been made — it has not; both remain posited
> alternatives, and they *disagree observably* on a three-way dispute.

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
options.**  The mechanism is concrete.  A rule says an actor may not
propose again on a version it already has a live proposal against.  If
the actor's view has not yet seen its own earlier proposal, the rule
does not fire — so the option is *open*.  See less, do more.

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

### A5.5 Second negative result: two of the three definitions can never work

This one is structural and even sharper.

To shatter a set of directions, you need *every* combination — including
the **empty** one: some event in the future that lies above *none* of
the chosen directions.

- Under **SKY-A**, the directions are the *immediate* successors.  So
  every event above the base lies above at least one of them, by
  construction.  **The empty shadow can never occur.**
- Under **SKY-C**, the same by duality.

So **SKY-A and SKY-C can never shatter anything, at any width, at any
depth.**  The audit of an earlier unit's own data: SKY-A, 261 skies,
*zero* with the empty shadow, of which 201 had been counted as "test
applies"; SKY-C, 258 skies, zero with the empty shadow, 211 counted.
SKY-B: 235 skies, 225 with the empty shadow, 142 counted, **139
genuinely capable**.

Consequence: of the 554 skies an earlier unit had declared "the test
applies here, and found nothing", only **139** could ever have found
anything.  **415 of them were a tautology, not a measurement.**

The corrected capacity condition — now binding on every later unit — is
threefold: at least four directions, at least sixteen distinct shadows,
**and the empty shadow present**.  On the same Minkowski data it admits
52 skies instead of 554: about a tenfold reduction in what counts as
testable.

And it explains something that had been sitting unexplained: an earlier
unit had noticed that SKY-A "never reached decidability" and could not
say why.  It was doubly disqualified.

**Why did the original validation miss this?**  Because the instrument
was validated on *synthetic* systems — arcs and exact caps — and both of
those contain the empty shadow.  The controls were sound; they were run
on the wrong kind of object.

### A5.6 How big can a sky get?

Two measured scaling laws, and they are in **different variables** —
which is the chapter's real deliverable.

- In a **Minkowski sprinkling** (points scattered in real spacetime),
  sky size grows with **density**.  With the box held fixed, the largest
  cover-sky runs 4, 7, 9, 14 directions as the number of points goes
  20, 40, 80, 160.
  *(An earlier version of this measurement let the box grow with the
  point count, so the sprinkling got sparser as points were added, and
  it reported the wrong variable.  Withdrawn; both columns are now
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

So the original claim ("the law produces sky size") is **withdrawn**,
and the truth is the reverse and more interesting: **transport skies are
narrower than chance.**  The law *constrains* sky size below the generic
value.  That strengthens the width reading rather than weakening it: the
bound is a real restriction, not a by-product of record size.

> **What this chapter does NOT claim.**  That any sky *is* a circle or a
> sphere — never licensed.  That absence of shattering is evidence for
> 2+1 — it is not, and §A5.4 is why.  That the arc/cap dichotomy
> exhausts what a discrete sky can be — a discrete sky need be neither.

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

### A6.7 The escape that worked: a completion with no far end

If the trouble is the imported far-end numbers, the way out is a
completion that has no far end — one defined on the unbounded structure
directly.

The corpus's key move was to stop enumerating records (there are
unboundedly many) and start enumerating **situations**: a bounded
summary of what a record looks like from the point of view of what can
happen next.  In the delivery-free two-actor world, that summary takes
**exactly 36 values**, and the search closes — no situation ever leads
outside the 36.  Collapse situations that no observation can
distinguish, and you get **six**.

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

### A6.8 The catch: the shape is a choice, not a law

This is where the story bends, and it bends because of hostile review.

The first announcement of §A6.7 said, in effect: *among completions that
respect the law's own identifications, there is exactly one, and it needs
no boundary.*  That sentence is **false and was withdrawn**.

What was measured, when the question was asked properly:

- Demand that a completion price the beginning and the renewal point
  alike, and **308 of 313** directions of freedom remain.
- Demand full respect for indistinguishability at every interior now,
  and **119 of 313** remain.
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
dimension **10, then 28, then 107** as you go deeper — it *grows*.  And
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

### A6.9 And all of it is delivery-free

Every result in §A6.7 and §A6.8 lives in the **two-actor, delivery-free**
sub-theory.  It is unconditional at every depth actually verified
(exhaustively through depth seven), and conditional at all depths on
three structural hypotheses of which one — the corpus calls it **H1** —
is **not proved**.  Two serious attempts on H1 have failed, and both
failures are on the record with their counterexamples (chapter A10).

At delivery scope — which is where all the geometry of chapters A5, A7,
A8 lives — **the whole question is open**, and chapter A9 explains why
the method that settled it cannot travel.

Also, the specific numbers (the factor of two, the six weights) are
**toy-relative**.  A second grammar was tested and has no such state
chain at all.  What is claimed to generalize is the *form* — a unique
completion of this type — never the numbers.

> **What this chapter does NOT claim.**  That "the record law is
> forward-complete" full stop — only with the form.  That the tilt is
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

So "the largest set this record's sky can shatter" is a number with a
dimensional meaning: 3 is circle-compatible, 4 is sphere, 5 is beyond
the sphere.

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
working around backflow, not slack in the family.  (An earlier draft
said the construction "saturates" the theorem; that was wrong and was
replaced.)

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

The empirical separation from real spacetime is genuine but **thin**, and
labelled thin.  Against real 2+1 Minkowski records, the control is
strong: 1,925 testable skies at ten different heights, **zero**
shatterings, against this record's three shattering heights.  Against
real 3+1 records, the control is much weaker: 1,351 skies examined, only
33 of them even *capable* of shattering (most fail the empty-shadow
requirement of chapter A5), and zero shatter-fives among them.  A
full-strength 3+1 control is a named, unbuilt residue.

One more honest correction: **the meter is a property of a (record,
reading) pair, not of a record.**  The same 42-actor record reads *zero*
under the two disqualified sky definitions and reads 1 through 5 under
SKY-B depending on the height chosen.  Its value is the largest over the
committed readings: five.

> **What this chapter does NOT claim.**  Any positive 3+1 claim.  Any
> statement about typical records — one engineered record per rung, no
> genericity, and genericity is *not even posable* at delivery scope
> (chapter A9).  Anything for six directions or beyond: the builder
> visibly generalizes and has not been run, and unrun is unclaimed.

---

## A9. The wall and the crack

*Technical twin: Part B, chapter B9.*

### A9.1 The two lines and where they meet

By now the programme has two lines running:

- The **measure line** (chapters A4, A6) is deepest in the
  **delivery-free** sub-theory, where it has a settled answer modulo one
  unproved lemma and one postulated shape.
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

### A9.4 The crack

Now the good news, and it is genuinely a crack in the wall rather than a
consolation.

Look again at the ladder of §A9.2.  The individual delivery options get
smaller and smaller: a quarter split *k+1* ways.  But:

> **The delivery sector's TOTAL is exactly one quarter at every rung.**

The per-option weights vanish; the aggregate does not move.  So the
no-go bites **per-option** descriptions and leaves **sector-level**
descriptions untouched.

That matters because of a result from an entirely different direction —
chapter A6's finding that a demand stated on the record can only
constrain **sums**, since what is observable is the probability of moving
from one kind of situation to another, not which labelled event carried
it.  **The corpus has already established that the physically meaningful
objects are the aggregated ones.**

So the escape candidate is sharp and stated: **does a bounded
sector-exact summary exist at delivery scope?**  Two measured facts about
it: the non-delivery part of the menu *does* factor exactly through a
lumped summary, and the lumped step distribution *is* a function of the
lumped state on the tested window — so the idea is not empty.  But the
lumped search also failed to close within its cap (1, 5, 17, 61, 187,
493, 1223, 3099, 8241, then the cap), with the remaining explosion
coming from the knowledge-lag structure of §A9.3.

> **The candidate is live, and it is not easy.**  Killing the unbounded
> counter is necessary and demonstrably not sufficient.

### A9.5 What this costs the programme

Stated without softening:

> The method that settled the measure question at delivery-free scope —
> a finite exact quotient plus classical eigenvalue theory — **provably
> cannot transfer** to the scope where the dimension results live.
> Whether a boundary-free measure exists at delivery scope is
> analytically open, with **no current tool**.  And the convergence
> question of chapter A11 — "does the measure prefer 3+1?" — is blocked
> on exactly this.

> **What this chapter does NOT claim.**  That the delivery-scope theory
> has *no* tractable description — only that no *menu-exact bounded*
> one exists.  Coarser objects, level-structured descriptions, and the
> boundary theory the corpus has already imported for a related purpose
> are all untouched by the no-go and named as the live routes.  Also:
> nothing in this chapter is a pinned corpus unit.  It is an advisory
> probe whose two load-bearing claims were independently re-verified;
> the rest of it must be re-derived before anything leans on it.

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
of chapter A3 and the standing obstacle for every future attempt.

### A10.3 The wire-closure route to H1

*Claimed:* a candidate event touches a wire and therefore already sees
everything relevant on it, so the lag is menu-invisible, so the lemma
follows at every depth without induction.
*Killed by:* measurement, and then something worse.  Every event type
lags, not only the one predicted.  And **a smaller view can yield MORE
options** (chapter A3), so any argument built on "the lagged view sees a
subset" is unsound — which rules out a whole family of attempts,
including this one.
*Survived:* a genuine **reduction** — the lemma is now known to be
exactly a question about four specific projections of a view, which is
strictly coarser than the question that died first.  Plus a settled
answer to a *second* hypothesis that had been left dangling.

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
free; the stronger indistinguishability demand leaves 119.
*Survived:* the **existence** result untouched, and the honest
replacement statement of chapter A6 §A6.8: uniqueness comes from a
postulated shape, and the shape is a choice.

### A10.12 Smaller retirements, for completeness

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
- **"H2 is subsumed by H1"** — inverted, withdrawn; later settled
  properly at the projection level.
- **Three register-theoretic bridges** to a full-poset structural no-go —
  all falsified, each at exit zero as a deliverable, so that nobody
  walks them again.

### A10.13 The pattern

Two observations about the list, which are the reason it is here.

**First: almost every correction hit an interpretation sentence, not a
computation.**  In the recent campaign, the reviewed units' computations
survived essentially intact — records rebuilt independently came out
identical, exact numbers reproduced, certificates re-derived by
different methods.  What failed, repeatedly, was the *sentence the
result was sold with*: a missing scope label, an arrow borrowed from a
premise class that had already been refuted, an antecedent nobody
checked was non-empty.

**Second: pre-registration is doing real work.**  The corpus writes down
what it expects *before* running, with the argument, and then reports
what happened.  In one recent unit's own accounting, **five of seven
pre-registrations in a campaign were corrected**.  A programme that only
recorded its confirmations would look far better and be worth far less.

---

## A11. Where we are, and what would decide it

*Technical twin: Part B, chapter B11.*

### A11.1 The state of the two lines

**The measure line.**  In the delivery-free, two-actor sub-theory the
completion question is *settled*: there is a boundary-free completion,
it is unique up to scale within a postulated shape, it prices the
beginning of the record and the renewal point identically, and its cost
is exactly one named tilt.  Three qualifications, all permanent until
someone does work: the shape is a **choice**; the all-depth statement
rests on an **unproved lemma** (H1) with two failed attacks on record;
and the specific numbers are **toy-relative**.  At delivery scope the
question is **open**, and chapter A9 shows the tool cannot travel.

**The geometry line.**  At delivery scope, measure-free: the sky is an
actor-width phenomenon; sky richness has an exact price in actors; the
shatter ladder is a dimension meter; and the framework admits records
whose skies sit at the sphere's rung *and one rung beyond*, with the
higher one **forced** by the menus at every step of its construction.
So the admissibility layer does not cap the ladder.

### A11.2 The convergence question

Put them together and one question remains, and it is now the
programme's centre of gravity:

> **Does anything in this framework prefer 3+1?**

The rules about what may happen do not — that is chapter A8's licensed
result.  So if anything does, it is elsewhere, and there are exactly
three named candidate homes:

1. **The measure.**  A completed law might assign the wide,
   courier-heavy records that buy high shatter numbers negligible
   weight.  This is currently **not even posable** at delivery scope
   (chapter A9), and unblocking it is the highest-leverage open problem
   in the corpus.
2. **Resource cost.**  Dimension is priced in actors, and the price
   grows.  Perhaps something like a cost principle selects a rung.
   Nothing of the kind exists in the corpus.
3. **Counting typicality.**  Perhaps among all records of a given size,
   the ones with sphere-like skies dominate combinatorially without any
   measure at all.  Also unbuilt.

The corpus's own statement was originally that the measure was the only
candidate; that was **widened** in review to these three.

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

1. **A bounded sector-exact abstraction at delivery scope.**  The one
   crack in the wall (chapter A9).  Unblocks the convergence question.
   Live and not easy: the obvious lumping is verified exact on the
   window and still fails to close.
2. **A full-strength 3+1 control** for the shatter meter.  The current
   one is thin: 1,351 skies, 33 capable, zero shatter-fives.
3. **H1** — the unproved structural lemma the whole delivery-free
   settlement is conditional on.  Two routes are closed with
   counterexamples; a third needs to avoid assuming that a lagged view
   sees a subset, since that is false.
4. **Is there a record-level demand that forces the shape?**  The two
   strongest candidates and their conjunction are eliminated by
   measurement.  Nobody has a third.
5. **General rungs of the ladder.**  The builder visibly generalizes
   past five; it has not been run, and unrun is unclaimed.
6. **Minimality.**  Six actors are necessary for shatter-four and twenty
   were spent; ten are necessary for shatter-five and forty-two were
   spent.  Both gaps are architectural and both are decidable.
7. **The residual pricing defects.**  The off-ladder configuration; the
   general-depth ladder being false under current pricing; the one
   merge priced two ways.  All carried forward into the completion
   problem rather than patched.
8. **The reading-relativity questions.**  Which sky definition is
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
- **Hostile rounds, and recently independent-model rounds** — a
  reviewer with no prior context, instructed to recompute rather than
  trust, writing its own code.  Both recent rounds of this kind found a
  blocker.  Both blockers were in interpretation, not arithmetic.
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

**Round-1 MAJOR D1 — the headline was narrowed.**  CG3 decides
admissibility of the *literal renamed event sequence* — bookkeeping —
whereas the programme's own thesis is that the physics is the causal
order.  New gate CG8: of the records whose literal merged image is
inadmissible, how many have a causal poset realized by *some* admissible
coarse record?  **All of them: 10,608 / 10,608 at cap 4 (in-receipt) and
196,304 / 196,304 at cap 5 `[REFEREE-CARRIED]`** — zero exceptions in
206,912 cases.  Headline restated: **the labelled record does not
aggregate, but the causal order does.**

**Round-1 MAJOR D2 — the real obstruction is LOSS, and it had not been
measured.**  Gate CG9: causal-poset isomorphism classes.

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

> **The one-sentence answer to "how well defined is the interactive click
> law?":** the **admissibility** interactive law is **complete**; the
> **probabilistic** interactive law is **provably not self-normalizing**
> (§B6).

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
True)` and `(True, False)`.  Mechanism, exhibited:
`prop_options_in_view` **excludes** a base on which the actor already has
a live proposal, so **a view that misses that proposal INCLUDES the base
— a smaller view can yield MORE options.**

> **Any depth-free argument built on "the lagged view sees a subset" is
> therefore unsound**, which rules out a whole family of attempts
> including D51's own pinned route (§B10.3).

**What did hold (D51) `[EVIDENCE]`:** MV3 — equal full-view projections
imply equal menus with exact weights, across all **6,471** histories over
**209** distinct projection keys, **zero** violations; and since `sigma`
is an abstraction of exactly those projections, menus are
sigma-determined on this family.  MV4 — **(H2) settled at the projection
level**: the successor projection-state is a function of
`(projection-state, event)`, **498** pairs, zero violations.  D44a had
left (H2) undetermined; at this scope it does **not** need a separate
argument.

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
on the cut complex.

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

### B5.4 D53: the empty-trace obstruction, and SC5 `[EXACT]`

Receipt `v10/code/d53_sky_capacity_exact.py` (6 PASS / 0 FAIL); the
instrument imported from the committed D47a by **AST extraction** — D47's
own object, not a re-implementation.

**The defect.**  Shattering a `k`-set requires all `2^k` traces, and the
**empty trace** is one of them; a system without it cannot shatter any set
for any `k ≥ 1`.  D47's capacity gate SG2 admitted a sky as "shatter-4
decidable" on `|directions| ≥ 4` and `|rows| ≥ 2` — **necessary and NOT
sufficient.**

**The audit of D47's own strata:**

| reading | skies | with empty trace | counted decidable | actually capable |
|---|---|---|---|---|
| SKY-A | 261 | **0** | 201 | **0** |
| SKY-C | 258 | **0** | 211 | **0** |
| SKY-B | 235 | 225 | 142 | **139** |

> **Of D47's 554 "decidable" pairs only 139 could EVER have shattered;
> 415 were structurally incapable, so its zero-shattering result over
> those is a TAUTOLOGY, not a measurement.**

**And the reason is structural, not statistical.**  SKY-A takes the
directions to be the **covers** of the base event, so every event
strictly above it lies above at least one cover and the empty trace
**cannot** occur; SKY-C is the dual and fails identically.  Only SKY-B,
whose directions form an antichain at fixed height, admits an event above
the base lying above **no** direction.

> **SKY-A and SKY-C can never shatter at any width or depth.**  This is
> stronger than "they did not fire", and it explains D47b's previously
> unexplained observation that SKY-A never reached decidability: it was
> doubly disqualified.

**The corrected capacity condition (SC5), binding on every future sky
unit:** `≥ 4` directions **AND** `≥ 16` distinct traces **AND the empty
trace present.**  On the same Minkowski records it admits **52** skies
against D47's 554 — a **10.7×** reduction.

**Why the defect survived D47's own validation:** SG1 validated the
instrument on **synthetic** set systems (arcs, exact-rational caps), and
**both contain the empty trace**, so the instrument passed honestly on
objects that were capable, and the incapacity of real cover-skies was
never in the validation's field of view.  *The controls were sound and
were run on the wrong object.*

**Damage bounded and stated — UNTOUCHED by D53:** D47a's constructed
separator; the instrument validation on synthetic systems; the demotion
of circular-ones (which never used shatter-4); and D47b's actor-width
result (which measures sky **size** and does not invoke shattering).

### B5.5 Capacity in Minkowski: density, not count `[EXACT]`

**Round-1 MAJOR R2 — SG10 confounded point count with density.**  The
original point generator let the box extent scale with `N`, so volume
grew as `~4N³` while `N` grew linearly and the sprinkling got *sparser*
as `N` rose.  Both columns are now reported side by side and **neither is
quoted alone**:

| N | growing box: max `|SKY-A|` | fixed box (160): max `|SKY-A|` |
|---|---|---|
| 20 | 3 | **4** |
| 40 | 8 | 7 |
| 80 | 10 | 9 |
| 160 | 14 | 14 |

Growing box: first decidability at `N ≈ 40` (decidable base events
0/23/58/120).  Fixed box: **decidable already at `N = 20`.**  **The
headline "shatter-4 first becomes decidable at N ~ 40" is WITHDRAWN AS
STATED.  The correct Minkowski variable is DENSITY.**

### B5.6 Capacity in the record: actor width `[MEASURED]`

D47b, 400 deterministic deep walks per width to depth 20:

| width | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|---|
| max `|directions|` | 2 | 3 | 4 | 4 | 4 | 4 |

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

**New residue from the round:** the rebuilt null is **crude** (matches
carrier size and link count but not the height/width profile), so
"narrower than chance" is established against **that** null and not
against every reasonable one.

