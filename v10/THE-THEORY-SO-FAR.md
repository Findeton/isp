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
> as of **LEDGER #447** (v10/LOG.md) / **#130** (v8/LEDGER.md).
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
- **"H1 is discharged"** — it is not.
- **"infinite clocks via Sperner"** — withdrawn; the surviving route is
  trace counting (D54 round 1 BLOCKER 1).

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
   needs no boundary condition at all**, is unique up to scale within a
   postulated shape for it, and prices the beginning of the record
   identically to a later point that the law itself cannot tell from
   the beginning.
7. But that shape is a **choice, not a law**: the two strongest
   invariance demands anyone has written down leave the freedom
   *growing* (10, then 28, then 107 dimensions as depth increases), so
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
    3+1?* needs either a measure at delivery scope (blocked by the
    unbounded-menu theorem), or a resource-cost principle, or a
    counting-typicality argument — and the corpus has **none of the
    three**.
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
    (PART D).

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
  roads** (v10's atlas instrument and its measured gap; v9's grown webs).
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

### A5.7 And a fact about real spacetime that shapes everything after

One measurement belongs here rather than later, because it is about the
instrument rather than about any record.  Run the shattering test on
**genuine sprinkled Minkowski records** — real causal orders of real flat
spacetime, in two space dimensions and in three.

**They never shatter.**  Not in 2+1 (1,925 testable skies, zero), and not
in 3+1 (1,578 testable skies at four directions, zero; 740 at five,
zero).  No sprinkled Minkowski record of any tested dimension shatters at
all.

This is not a defect of the test — it fires perfectly well on the
engineered records of chapter A8, at two different sizes.  It is a fact
about the two kinds of object.  A sprinkling has no worldlines: it is
points scattered at random, with no actor structure whatsoever, so the
mechanism chapter A7 identifies — nested families of shadows swept by
worldlines — has nothing to act on.

> **So shattering separates ENGINEERED COORDINATION from SPRINKLED
> GEOMETRY, not one dimension from another.**  Chapter A7 keeps the
> ladder as an exact statement about continuous shapes, and chapter A8
> reads the framework's records against sprinklings rather than against
> dimensions.

> **What this chapter does NOT claim.**  That any sky *is* a circle or a
> sphere — never licensed.  That absence of shattering is evidence for
> 2+1 — it is not, and §A5.4 is why.  That the arc/cap dichotomy
> exhausts what a discrete sky can be — a discrete sky need be neither.
> And §A5.7's three-space-dimension numbers come from a unit that has not
> yet had a hostile review, so they are reported and not leaned on.

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

There is a tempting way to state §A6.7 that is **false**, and it is worth
naming because it is the natural thing to say: *among completions that
respect the law's own identifications, there is exactly one, and it needs
no boundary.*

The measurements say otherwise:

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

So "the largest set of directions these shadows can fully resolve" is a
number with a dimensional meaning **for continuous shapes**: 3 is
circle-compatible, 4 is sphere, 5 is beyond the sphere.  Every rung of
that table is exact.

**What it is not.**  It is not a dimension reading for a *record*.
Chapter A5 §A5.7 is the reason: genuine sprinkled records of real
spacetime, in every dimension tested, read **zero** on this scale.  So
the number measures how much coordination a record's worldlines have
achieved, not how many dimensions it lives in.  Read it as a **meter of
the framework's own reach**, calibrated against continuous geometry —
which is exactly the use chapter A8 makes of it.

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

**The controls, at full strength.**  Against genuine sprinkled Minkowski
records the separation is complete, and it runs in an unexpected
direction.  In 2+1: 1,925 testable skies at ten different heights,
**zero** shatterings.  In 3+1: 1,578 testable skies at four directions and
740 at five, **zero** shatterings of either — against this record's three
shattering heights.

So the engineered records are sharply separated from real spacetime — but
**from real spacetime of every tested dimension**, not from 2+1
specifically.  What the constructions demonstrate is that the framework
can build coordination that no random causal order of any dimension
exhibits.  That is the capacity claim above, and it is all of it.

**And the meter is a property of a (record, reading) pair, not of a
record.**  The same 42-actor record reads *zero*
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
there, on two independent grounds.**

**First, the quarter is not a law of sectors.**  It is a fact about the
*delivery* sector alone.  The arbitration sector divides its quarter by
the number of live conflict groups, and that number grows without bound
with depth, so sector totals themselves take unboundedly many values.
The aggregated alphabet is no more finite than the per-option one.

**Second, the coarsest possible lumping does not settle down.**  Track how
many distinct lumped situations survive as the enumeration deepens, and
the count keeps creeping upward at every window that can be checked.

The one hopeful measurement — that the non-delivery part of the menu
*does* factor exactly through a lumped summary, and that the lumped step
distribution *is* a function of the lumped state on the tested window — is
real, and it is not enough.  Killing the unbounded counter is
**necessary and demonstrably not sufficient**.

> **The crack narrows rather than closes.**  What survives are strictly
> *coarser* aggregations — grouping by event type only, or by total budget
> only — and descriptions that give up exactness altogether and target
> only what a completion actually has to reproduce.  All untested.

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
> has *no* tractable description — only that no *menu-exact bounded* one
> exists, and that the natural aggregated version is closed too.  Strictly
> coarser objects, level-structured descriptions, and the boundary theory
> the corpus has already imported for a related purpose are untouched by
> both no-gos and are the live routes.  And the standing of the sources
> should be carried: §§A9.2–A9.3 rest on an advisory probe whose two
> load-bearing claims were independently re-verified and whose remainder
> must be re-derived before anything leans on it, while §A9.4's closure
> comes from a pinned unit that has not yet had a hostile review.

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

### A10.10b Max-shatter as a dimension meter for records

*Claimed:* the largest set of directions a record's sky can fully resolve
reads its dimension — three for circle-like, four for sphere-like, five
for beyond.
*Killed by:* the controls.  Genuine sprinkled records of real flat
spacetime, in two space dimensions and in three, **never shatter at all**
— zero out of 1,925 testable skies in one case, zero out of 1,578 and 740
in the other.  A scale on which real spacetime of every dimension reads
zero is not reading dimension.
*Survived:* the calibration ladder itself, which is exact and remains a
true statement about *continuous* shapes; the capacity results built on it
(the framework can construct skies at the sphere's rung and one beyond);
and a better reading of what the number measures — **coordination between
worldlines**, which a random scattering of points has none of.  See §A5.7.

### A10.10c A sector-level escape from the delivery-scope wall

*Claimed:* the unbounded-menu theorem kills only per-option descriptions,
because the delivery sector's total is constant; so a description that
tracks sector totals rather than individual options should stay finite.
*Killed by:* two independent facts.  The constant quarter is a property of
the *delivery* sector alone — the arbitration sector divides its quarter
by a count that grows with depth, so sector totals take unboundedly many
values too.  And the coarsest possible lumping does not settle down: the
count of distinct lumped situations creeps upward at every window that
can be checked.
*Survived:* the observation that motivated it — that the physically
meaningful objects are the aggregated ones — which still points at the
right *kind* of description; and a narrower crack, at strictly coarser
aggregations and at descriptions that abandon exactness for what a
completion actually has to reproduce.  See §A9.4.

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
computation.**  Across the reviewed units the computations survive
essentially intact — records rebuilt independently came out
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
*Forward-look **superseded by PART D**: this chapter is accurate as the
state of the two lines, but the destination it gestures at has since been
stated explicitly (LOG #436).  Read PART D for what the open questions are
**for**.*

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

None of the three is more than a name.  The measure is the one the
corpus has invested in, and it is the one that is blocked.

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

1. **A bounded description of the theory at delivery scope.**  The one
   remaining gap in the wall (chapter A9), and what unblocks the
   convergence question.  Exact per-option descriptions are impossible for
   any design; the natural sector-level ones are closed too; what survives
   are strictly coarser aggregations and inexact, observable-only
   descriptions — all untested.

2. **Where is the sprinkling floor?**  Real spacetime records read zero on
   the shatter meter in every dimension tested (§A5.7).  Do they shatter
   *three* — the rung below?  That would locate the floor and calibrate
   whatever replaces the meter.
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

**Point count and density must not be confounded.**  If the box extent is
allowed to scale with `N`, volume grows as `~4N³` while the point count
grows linearly and the sprinkling gets *sparser* as `N` rises — two
variables moving in opposite directions.  Both columns are therefore
reported side by side and **neither is quoted alone**:

| N | growing box: max `|SKY-A|` | fixed box (160): max `|SKY-A|` |
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

**A declared limit:** the null is **crude** (matched on carrier size and
link count, not on the height/width profile), so "narrower than chance"
is established against **that** null and not against every reasonable one.

### B5.7 The sprinkling floor: genuine Minkowski never shatters `[D55c, LOG #435 — GREEN-UNREVIEWED]`

Receipt `v10/code/d55c_m31_control_exact.py`, **4 PASS / 0 FAIL**, exit 0;
`mink4` anchored to the committed `mink` on `z = 0` (identical orders, so
the four-dimensional generator extends the audited one rather than
replacing it).  Four fixed-box records to `N = 200`:

| quantity | value |
|---|---|
| SC5-capable(4) pairs on genuine `M^{3+1}` | **1,578** |
| SC5-capable(5) pairs | **740** |
| shatter-5 found | **ZERO** — the pre-registered halt condition holds |
| shatter-4 found | **ZERO of 1,578 capable pairs** |

Combined with the zero-shattering result on genuine `M^{2+1}` (§B8.5's
1,925-pair control): **no sprinkled Minkowski record of any tested
dimension shatters at all**, while the engineered transport records of §B8 shatter 4 and 5.

> **Therefore max-shatter does NOT separate 2+1 from 3+1 on discrete
> records; it separates ENGINEERED COORDINATION from SPRINKLED GEOMETRY.**

*Scope and status.*  This unit is **green-unreviewed** and therefore not
citable (§0.2); it is reported because it fixes the meaning of the
instrument that §B7 and §B8 use.  It leaves untouched: the exact
calibration ladder for **continuum** trace systems (§B7.5 A2), the
Dilworth gate (§B7.3), the capacity results of §B8, and the
trace-counting bound of §B7.4 — none of which says anything about
sprinklings.

`[MY READING]` The structural reason is that a sprinkling has **no actor
or wire structure**, so the Dilworth mechanism — chains of traces
contributed by worldlines — does not even *apply* to it.  Shattering may
therefore be exactly the signature of **worldline-coordinated knowledge**,
which a sprinkling lacks by construction.  On that reading the geometry
line's real discovery is not about dimension: it is that coordination
leaves a combinatorial fingerprint that random causal structure of the
same size does not have — which sits beside §B5.6's independently measured
"narrower than chance", and is a sharper thing to have found than a
dimension estimator would have been.  Interpretation of a
green-unreviewed unit; not citable.

**Residue named by the unit:** does genuine `M^{2+1}` or `M^{3+1}` shatter
**3** — the rung below, which would locate the *sprinkling floor*?

---

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
   exactly when the blind pair becomes visible.
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
menu-invisible; **that invisibility is checked, never assumed** — and it
is exactly where the remaining gap lives (§B6.13).

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
- **(H2) TRANSITION DETERMINISM at every depth.**  Explicitly **not** a
  consequence of (H1).

> **`[THEOREM, conditional]` Assume (H0)–(H2).  Then residue 1 is DECIDED
> at all depths at d42a scope**: `sigma` takes exactly 36 values at every
> depth; the intrinsic partition is at every depth the pullback of the
> abstract chain's bisimilarity; and the Perron package is the completion
> decision at every depth.  QED (conditional).

**Declared verification scope, which a reader must carry:** blockwise
equality of the pullback with the committed intrinsic partition is
computed **in-receipt at length ≤ 4** and **at length ≤ 5 by the frozen
round's referee** `[REFEREE-CARRIED]`; the **four minlen-6 `sigma`-states
are classified only via the conditional argument.**  No minimality is
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
| bisimulation-invariance of the completed class transfer at every interior cut (I2) | 589 | 194 | **119 of 313** |
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

**MAJOR M4 — a citation-discipline breach, recorded rather than repaired
away.**  #418 amended `THE-COMPLETION-DICHOTOMY.md` — the corpus's
entry-point document — with a banner reading "the dichotomy has been
SETTLED", **in the same ledger entry that created D49, before any hostile
round**, and the banner carried **no scope** (neither "d42a
delivery-free" nor "conditional on (H0)–(H2)" appeared in it).  Repaired:
scope and review status now in the banner.

**Four first-run deviations, all gated:** (A1) the pinned `λ = 1`
eigenvector was hand-computed and **wrong** — replaced by an exact
in-receipt kernel computation; (A2) the pinned rank 114 was wrong and the
true value 84 became the result; (A3) the washout budget was too small —
repaired at certificate level with the iteration extended to `n = 400`;
(A4) **a determinism defect in the receipt itself, caught by seed
variation** — E2 serialized `'r'` events through a raw `frozenset` repr
and reported 7 spurious mismatches at `PYTHONHASHSEED=7`, exit 1, exactly
the warned failure mode; repaired with a recursive deterministic key and
**recorded rather than quietly fixed**.

**A record-keeping correction, #420:** #419 recorded the round as
"repaired and delta'd" while the frozen round file contained **no delta
section at all**.  The repairs were real (independently re-verified at 31
PASS / 0 FAIL from a clean process) but the record of them was missing
from where the discipline puts it.  Same defect class as #390, corrected
the same way: forward, with the cause stated.

### B6.12 D50: the form is a CHOICE `[LOG #421/#422; GREEN-UNREVIEWED]`

> **Discipline note:** D50 has **not** had a hostile round.  It is
> green-unreviewed and therefore **not citable**; it is reported here
> because it is the residue B2 created and because its result is a
> *negative*, which its own pre-registered one-sidedness doctrine makes
> rigorous in a way a positive would not have been.

Pin `note-d50-is-the-form-a-law-pin.md`; receipt
`v10/code/d50_form_law_or_choice_exact.py` (9 PASS / 0 FAIL, exit 0),
importing D49's state by AST-stripping its `check()`/`print()`/`sys.exit`
statements — single source, D49's gates not re-run.

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
depth-stationarity has dimension **10, 28, 107** at truncation depths
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
- **SF6 negative control held:** I1 stays loose (completion dimensions
  22/83/307).

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

### B6.13 (H1): undischarged, with two dead routes

**(H1) is residue 1's final named gap**, and D44a / D49 / D50 all inherit
its conditionality.  Two routes are closed, both with counterexamples on
the record:

- **The `tau` own-view route `[D46a]`.**  `tau` is **not an own-view
  object**: the menu view strictly exceeds the noop cone on 1,016 of
  12,942 actor-histories, all extras opponent-authored (§B3.2).  (H0) is
  an independent hypothesis, not a dispensable one, and (H2) is **not**
  subsumed by (H1) — §B10.2.
- **The wire-closure route `[D51]`.**  Its pinned form: MV-STRONG holds
  for propose/arbitrate and fails only for idles, on the reasoning that a
  candidate touching base `b` already sees every live proposal on `b`.
  Measured: **every event type lags**; and worse, **monotonicity fails** — a smaller view can
  yield more options — so **any depth-free argument built on "the lagged
  view sees a subset" is unsound.**  D51's own pin §5 depth-free sketch is
  recorded as **damaged**, not quietly dropped.

**What D51 leaves as durable content:** (H1) is now **exactly** the
question whether the **four menu-relevant projections**, evaluated on each
candidate's own view, are `sigma`-determined — strictly coarser than the
question that died first.  Plus two finite-depth confirmations (MV3, MV4)
and the settlement of (H2) at the projection level.

**Three gates were mis-specified by the author and were restated, not
weakened:** MV1 and MV2 originally *asserted* the author's expectations
and failed; MV5 demanded that hiding a proposal change the projections in
100% of cases, where the true rate is **3,008/4,760 (63%)** because a
dropped proposal on an unreached base moves nothing — the gate now tests
responsiveness.  *A gate that asserts the author's hypothesis is not a
gate.*

### B6.14 Scope, to be carried at every citation

- **d42a scope, delivery-free, two actors.**  Unconditional at every
  verified depth — exhaustively through depth 7.  Conditional on
  (H0)–(H2) at all depths, **exactly** as D44a's conditional theorem is
  and no more: **(H1) inherits the whole conditionality**, and its
  leverage goes *up*, since it is now the last gap before the dichotomy is
  settled unconditionally rather than merely before residue 1 is decided.
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

> **What the meter reads, stated exactly.**  The calibration ladder above
> is exact and is a statement about **continuum** trace systems.  It is
> **not** a dimension reading for a discrete record: §B5.7 measures
> genuine sprinkled Minkowski records at **zero** in every dimension
> tested.  So a record's max-shatter measures the **coordination its
> worldlines have achieved**, calibrated against continuous geometry — a
> meter of the framework's reach, not of a record's dimension.

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
> including the empty one (SC5 satisfied), realizes ALL 16 subsets, and
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

| control | result |
|---|---|
| genuine `M^{2+1}`, SC5-capable SKY-B pairs at depths 1..10 | **1,925** pairs, **ZERO** shattered 4-sets `[REFEREE-CARRIED]` |
| genuine `M^{3+1}`, SC5-capable pairs at four directions | **1,578** pairs, **ZERO** shattered 4-sets `[D55c, GREEN-UNREVIEWED]` |
| genuine `M^{3+1}`, SC5-capable pairs at five directions | **740** pairs, **ZERO** shattered 5-sets `[D55c, GREEN-UNREVIEWED]` |

against this record's **three** shattering depths.

**The separation is therefore complete and dimension-blind** (§B5.7): the
engineered records are sharply separated from sprinklings of *every*
tested dimension, not from 2+1 specifically.  What is demonstrated is
**capacity for coordination no random causal order exhibits** — which is
the licensed claim below and the whole of it.

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

### B9.4b The sector-exact escape, closed at `(actor, type)` granularity `[D57, LOG #436 — GREEN-UNREVIEWED]`

Receipt `v10/code/d57_sector_exact_refinement.py`, **3 PASS / 0 FAIL**,
exit 0, caps 3/4/5/6 **exhaustive** (**521 / 3,969 / 30,729 / 243,769**
histories).  The question: does the **coarsest sector-lumpable
partition** — the one induced by the aggregated transfer
`T_s(h, c) = Σ q over sector s landing in class c` — stay finite at
transport scope?  The pin expects sector quantization to hold, as the
**finite-alphabet prerequisite**, and gates it first.  **Both halves are
negative, and each refutes a pre-registered expectation.**

**(1) SECTOR QUANTIZATION FAILS — the sector alphabet is not finite.**
`{0, 1/4}` dies immediately: **arbitration sectors reach `1/2`** via
subset choices — the `1 + k/4` ladder appearing at sector level.  The
repaired `k/4` law then dies at cap 6, where **`1/8` appears**, because
the arbitration sector prices `1/4` **divided by the component count** and
components grow with depth.  Totals live in `{k/(4m)}` with `m`
depth-unbounded.

> **So §B9.4's `1/4` is a fact about the DELIVERY sector, not a law of
> sectors**, and the finite-alphabet prerequisite fails **independently of
> the refinement question**.

**(2) THE COARSEST SECTOR-LUMPABLE PARTITION DOES NOT STABILIZE.**  Read
as lookahead convergence, per-depth fixpoint counts across caps 3/4/5/6:

| depth | cap 3 | cap 4 | cap 5 | cap 6 |
|---|---|---|---|---|
| 3 | 7 | 16 | 16 | **17** |
| 4 | — | 9 | 23 | **27** |
| 5 | — | — | 11 | **33** |

**Even depth 3 creeps at cap 6**, and nothing comparable stabilizes.
`[MEASURED]` — blow-up evidence at this window, not a theorem.

> **VERDICT: the sector-exact escape, at `(actor, type)` granularity, is
> CLOSED — a strictly stronger negative than §B9.1's: even AGGREGATED
> bookkeeping at this granularity fails, on two independent grounds
> (alphabet + refinement).**

**The asymmetry of evidence, respected.**  Ground (1) is an **exact
structural** statement about the pricing rule — the arbitration sector
genuinely divides by a depth-unbounded count — and does not depend on the
window.  Ground (2) is `[MEASURED]` at caps 3–6.  The verdict is carried
by (1) with (2) corroborating — the same division of labour §B9.1 uses.

**What the crack narrows to** (both untested, both live): **strictly
coarser aggregations** — type-only sectors, total-budget only — and
**abstractions that give up exactness** and target only the completion's
**observable** demands, with the standing warning that the aggregated
reading is the correct one for *stating* demands and is also what makes an
exact aggregated bookkeeping hard to build.  **Residues:** depth 7; an
actor-swap quotient (counts `≤ 2×`, so it cannot rescue the trend alone).

*Status: green-unreviewed, therefore not citable (§0.2).*

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
> dimension results live.  Whether a root-free completion exists at
> transport scope is **analytically open with no current tool**, and the
> convergence question (*does the measure prefer 3+1?*) is blocked on
> exactly this.

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
completion's observable demands only.

**For completeness, the transport-scope Martin results already in hand
(D46b, after review — three reversals):** `root = renewal` **does**
transfer at matched horizon (an earlier "does not transfer" claim was a
horizon-mismatch artifact and was withdrawn); the pinned sector-normalized
conditional is **exactly horizon-stable at the root** (reported as a
negative before review, corrected to a positive); contraction is **true
and strengthened** but **not at a constant rate** — the sequence is
`0.738, 0.399, 0.086`; and deliveries **REDUCE** branching (the earlier
claim had the sign wrong; peak at `D = 5`, down at `D = 6`).

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
cover the base it touches.  Then, worse: **monotonicity fails** —
`prop_options_in_view` excludes a base the actor already has a live
proposal on, so a view that **misses** that proposal **includes** the base.
**A smaller view can yield MORE options.**
**Survived:** the **reduction** — (H1) is exactly the question whether the
four menu-relevant projections on each candidate's own view are
`sigma`-determined, strictly coarser than the refuted question; MV3 and
MV4 as finite-depth evidence; **(H2) settled at the projection level**;
and a general bar: *no depth-free argument may assume view monotonicity.*

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

### B10.10b Max-shatter as a dimension meter for records `[D55c, LOG #435 — GREEN-UNREVIEWED]`

**Claimed:** a record's max-shatter is its dimension signature —
3 circle-compatible, 4 sphere, 5 beyond.
**Killed by:** the full-strength controls of §B5.7 — **zero shatter-4 of
1,578 SC5-capable pairs and zero shatter-5 of 740 on genuine `M^{3+1}`**,
against zero of 1,925 on genuine `M^{2+1}`.  No sprinkled Minkowski
record of any tested dimension shatters at all; the scale cannot be
reading dimension.
**Survived:** the calibration ladder as an exact statement about
**continuum** trace systems (`B₄` fits `S²`; no five points ever shatter
there; `B₅` fits `S³`); the **Dilworth gate**, which says nothing about
sprinklings; the **trace-counting** bound; and the whole capacity result
of §B8 — the layer does not cap the shatter ladder at the sphere's rung.
What the number measures is **worldline-coordinated knowledge**, which a
sprinkling lacks by construction.

### B10.10c The sector-exact escape at `(actor, type)` granularity `[D57, LOG #436 — GREEN-UNREVIEWED]`

**Claimed:** §B9.1's no-go bites per-option descriptions only, since the
delivery-sector total is exactly `1/4` at every rung; so a **sector-exact**
abstraction should stay bounded.
**Killed by:** two independent grounds (§B9.4b).  **Sector quantization
fails** — arbitration sectors reach `1/2` via subset choices and `1/8` at
cap 6, because the sector prices `1/4` divided by a depth-unbounded
component count, so totals live in `{k/(4m)}` and the **sector alphabet is
not finite**; the `1/4` was a fact about the *delivery* sector, not a law
of sectors.  And **the coarsest sector-lumpable partition does not
stabilize** — per-depth fixpoint counts creep across caps 3/4/5/6 (depth 3:
7, 16, 16, **17**).
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
**308/313** free; bisimulation-invariance leaves **119/313**.
**Survived:** the **existence** result entirely untouched (horn (II)
holds), plus the honest replacement: uniqueness comes from **the form**,
and D50 then showed the form is a **choice**.

### B10.12 D50's own pre-registered expectation `[LOG #421 → #422]`

**Claimed (pre-registered, with its argument, before running):**
depth-stationarity forces the form.
**Killed by:** the falsifier — completion dimensions **10, 28, 107**,
growing.  Plus the diagnosis: the record-level demand is **aggregated**, so
it constrains sums and never obtains the sketch's hypothesis, and *the
aggregated reading is the correct one*.
**Survived:** a **permanent** restriction on every citation of D49; the
measured fact that **foliation-invariance adds nothing**; and the sharp
successor question — *is there any record-level demand that forces the
form?* — with the two strongest candidates and their conjunction now
eliminated.

### B10.13 Instrument and control failures, itemized

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
  them is a **tautology**.  SC5 replaces it.
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

### B10.14 The pattern, stated as a statistic

- **Almost every headline correction hit an interpretation sentence, not a
  computation.**  In the two independent-model rounds (D54, D55), the
  verdicts were 1 BLOCKER / 2 MAJOR / 8 MINOR / 3 NIT **each**; in D54
  *all three top findings hit the interpretation layer* and the
  mathematical core survived everything; in D55 **everything
  computational survived**, including a full independent rebuild of a
  42-actor, 84-event record that came out **identical and forced**.
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
§D4**, which supersedes their ordering (not their content); the two lines
of §B11.1 are unchanged.*

### B11.1 The two lines, scoped

**Measure line — d42a, delivery-free, two actors.**
`Zhat(h) = 2^(−|h|) f(class(sigma(h)))` with `λ = 2`,
`f = (4,4,3,7,3,3)/3` is a completion in the sense of paper 30 §5.2:
positive, per-cut normalized, class-constant, foliation-invariant
directly, support-preserving, a law, a measure, and **root-free** (root and
renewal both `1/16`; the whole 215-node matched subtree identical).
**Horn (II) holds.**  Unconditional at every verified depth (exhaustive
through depth 7); conditional on (H0)–(H2) at all depths with **(H1)
undischarged**; **unique only within paper 30 §5.7's stationary FORM, and
the form is a CHOICE** (D50, green-unreviewed); values **toy-relative**.
**Transport scope OPEN**, and §B9 shows the tool cannot travel.

**Geometry line — transport scope, measure-free.**  Sky size is an
actor-width phenomenon and narrower than chance; SKY-A/C can never
shatter and only SKY-B can, under SC5; the **Dilworth gate** is an
unconditional theorem of the layer (shatter-`k` costs
`≥ C(k, ⌊k/2⌋)` actors); a 20-actor / 42-event record shatters 4 at
depths 4, 5, 6, and a 42-actor / 84-event record shatters 5 at depths
5, 6, 7, **forced** at every step; the calibration ladder is exact
(`B₄` fits `S²`; no five points ever shatter there; `B₅` fits `S³`);
max-shatter is a **(record, reading)** invariant with SUP 5 on that
record.  **The layer does not cap the ladder at the sphere's rung.**

### B11.2 The convergence question

> **Does anything in this framework prefer 3+1?**

The admissibility layer does not (§B8.5).  Three candidate homes are
named:

1. **the completed measure** — blocked at transport scope by §B9;
2. **resource cost** — the ladder's actor price `3 / 6 / 10 / 20 / …`;
   nothing of the kind exists in the corpus;
3. **counting typicality** — unbuilt.

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

1. **A bounded description of the theory at transport scope.**  Highest
   leverage: the only route by which the measure could reach the scope
   where the dimension results live.  **Two granularities are already
   excluded** — menu-exact for *any* design (§B9.1), and `(actor, type)`
   sector-exact on two independent grounds (§B9.4b) — and the
   delivery-lumped candidate, though verified exact on the depth-5
   window, **fails to close at 20,000** with the residual explosion in the
   view-product structure.  What remains: **(i)** strictly coarser
   aggregations — type-only sectors, total-budget only; **(ii)**
   abstractions that give up exactness for the completion's **observable**
   demands; **(iii)** a level-structured (QBD / R-matrix /
   Martin-boundary) description with `|holdings|` as the level, connecting
   to the already-built transport-scope machinery.  All three untested.
2. **The sprinkling floor.**  Genuine Minkowski records read zero on the
   shatter meter in every dimension tested (§B5.7).  Do they shatter
   **3** — the rung below?  Cheap, and it calibrates whatever replaces the
   meter's dimensional reading.
3. **(H1)** — the depth-free menu-factorization lemma.  Two routes closed
   with counterexamples; any third must **not** assume view monotonicity.
   Closing it makes the d42a settlement unconditional.
4. **Is there a record-level demand that forces the stationary form?**
   Two strongest candidates and their conjunction eliminated by
   measurement.  Nobody has a third.
5. **General `m` for the courier builder** — visibly patterned, unrun,
   unclaimed beyond 5.  A receipt at `m = 6` (20 chains, 57 couriers,
   ~66 actors) would strengthen it; a proof of admissibility for every
   `m` would settle it.
6. **Minimality at every `m`** — `C(k,⌊k/2⌋)` versus the builder's spend
   (6 vs 20 at `m = 4`; 10 vs 42 at `m = 5`).  Both gaps architectural,
   both decidable.
7. **Upstream pricing residues**, all carried into the completion problem
   rather than patched: the `h12` dead-component inflation (`23/24`, off
   ladder); the general-depth `1 + k/4` ladder **false** under current
   pricing; the D2H merge priced `1/16` vs `1/24`.
8. **Reading-relativity**, twice: which **sky definition** is physically
   privileged (D47 residue 2, partially answered negatively by D53 — two
   of the three can never fire — but *why* SKY-B is the physical one is
   unanswered); and which **channel reading** is (D46e).  Same class of
   question.
9. **The transport-scope dichotomy itself** — whether a root-free
   completion exists there.  Analytically open, no current tool.
10. **The quantum completion at the arbitration layer** (paper 30 §6.2's
    three-horn pincer) and the fine-versus-coarse sealing question, which
    is **empirical** and has an exact instrument pair waiting for it.
11. **The laboratory bridge** — blocked on an empty coarse-graining slot;
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
`d56_transport_sigma_probe.py`.

**The ledger:** `v10/LOG.md`, append-only, numbered, **forward
corrections only, never silently edited.**  Entries #404–#433 cover
everything in chapters B5, B7, B8, B9 and the settlement line of B6.

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
  own code.  Both such rounds so far found a BLOCKER; both BLOCKERs were
  in interpretation.
- **Green-unreviewed is not citable**, and terminal papers are **not
  edited on green-unreviewed evidence** — amendments queue behind a round
  (paper 32 §6 item 7's amendment did exactly that).
- **Forward corrections only**, with superseded text preserved verbatim
  beside its replacement.

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
   No unit relates them.  (PART D §D6 records a *labelled speculation* in
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
| **45b** | **HARMONIC CONTAMINATION** — the half-cosine kernel `(u·v)₊ = |u·v|/2 + (u·v)/2` carries even harmonics `ℓ = 0, 2, 4…` (a 12.5% even tail, confirmed in review), which is latent structure beyond dimension 4; `F_iso` stays flat ~1.7–1.9 | the pure monopole+dipole kernel |
| **45c** | **MONOPOLE DRIFT** — with `χ_k = A + D⃗·v_k`, the accumulated content `A` is a deterministic clock redundant with `b`; occupancy is drift-dominated (`eig3/1` 0.14–0.31, `F_iso` 2.8–3.2 = the card's *collapse* regime, not shape).  *The latent cone theorem holds though:* at `K = ∞`, dominance ⟺ `ΔA ≥ |ΔD⃗|` — **the Minkowski cone itself in latent coordinates** | subtract the monopole: `ℓ_k = τ·b + (χ_k − χ̄)` |
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
  **declares** that v9 did not use the interactive click law.  So the two
  lines are not merely unrelated — one of them is officially *not the
  theory*.
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

The supporting measurement is §B5.7: across 1,578 SC5-capable genuine
`M^{3+1}` sky pairs, **zero shatter-4 and zero shatter-5**; combined with
the zero-shattering result on genuine `M^{2+1}`, **no sprinkled Minkowski
record of any tested dimension shatters at all**, while the engineered
transport records shatter 4 and 5.  Its `[MY READING]` mechanism note —
that sprinklings have no actor/wire structure, so the Dilworth mechanism
cannot even apply to them — is the structural reason the two object classes
should not have been expected to resemble each other.

**What the destination does NOT mean.**  It does not mean the corpus
claims curved spacetime, particle creation, or any step below.  §D2 is a
roadmap with per-arrow status, and four of its eight arrows are `[OPEN]` or
`[BLOCKED]`.

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
when the charts are tiny."*

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
| 3 | skies → charts, gluing → a manifold | **OPEN** — and being attacked from **two directions at once** (v10's atlas instrument, which now measures a confirmed gap; v9's grown webs, further along but review-indebted and closed).  Their convergence is itself open |
| 4 | manifold → Einstein dynamics | **PARTIAL** — the *form* of the field equations is derived; Newton's constant is provably not derivable from inside |
| 5 | manifold → quantum fields on it | **PARTIAL** — a lift of the record process into Hilbert space exists at fixture scale, and its arbitration layer is where the quantum problem begins |
| 6 | fields → **particle creation** | **OPEN** — the destination's defining phenomenon, with one suggestive structural resemblance that is *labelled speculation* |
| 7 | particles → matter | **OPEN** |
| 8 | matter → a laboratory number | **BLOCKED**, and the block is four-fold |

Two honest points about this table.  **The arrows are not independent, and
three of them are blocked on the same thing** — the programme cannot
currently pose probabilistic questions at the scope where its geometry
lives (chapter 9, §§A9.4/B9.4b).  **And one constraint
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

Delivered: the sky instrument with three committed definitions and the
proof that only one of them can ever fire (§B5.4); the corrected capacity
condition SC5; the two scaling laws in different variables — Minkowski buys
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

**ARROW 3 — charts and gluing → a manifold.  `[OPEN — and there are TWO
roads, neither finished]`**

A causal order is not a manifold.  To get one you need local pieces that
look like patches of `ℝ^d` (**charts**), a rule for saying two patches
overlap and agree (**gluing**, with transition maps), and enough
consistency that the result is one object.  **The corpus is attacking
this from two directions at once, and they have never been compared.**

**ROAD 1 — the v10 atlas / crystal line `[D58, LOG #438–#439]`.**  Pin
before code (`note-d58-atlas-instrument-pin.md`), and the first two
instruments built: the **overlap fraction**
`ω(e, e′) = |D_e(d) ∩ D_{e′}(d−1)| / |D_e(d)|` on cover pairs (charts at
consecutive events share a height layer; identity transitions —
**non-identity transitions and the real cocycle question are DECLARED a
later stage**), and the **homogeneity profile** of `|D_e(d)|` over all
events.  Discipline: instrument first, controls before data.

Receipt `d58_atlas_instrument_exact.py`, **5 PASS / 0 FAIL**.  The gate
**validates on homogeneity and REPORTS overlap** rather than testing
overlap against a threshold — a hard-pinned overlap floor would be an
invented constant, and the measured values (~0.12 on one control) sit
nowhere near any natural one.

The measurements, SKY-B charts, exact Fractions:

| record | events carrying a ≥ 2-direction chart | mean overlap |
|---|---|---|
| `M^{2+1}` sprinkling, `N = 120` | **64%** | ~0.12 |
| `M^{3+1}` sprinkling, `N = 120` | **73%** | ~0.54 (at `d = 3`: ~0.94) |
| the shatter-4 courier record | **38%** | ~0.47 where measurable |
| the shatter-5 courier record | **35%** | — |
| a generic 2-actor walk | **6%** | — |

> **The pre-registered gap, CONFIRMED: sprinkling homogeneity floor 0.64
> vs engineered ceiling 0.39 vs generic walk 0.07 — the grammar's records,
> as built so far, are THE OPPOSITE OF ATLASES.**  They were built to
> shatter, not to tile.

The `M^{2+1}`-vs-`M^{3+1}` overlap difference is flagged **a finding
candidate, CONFOUNDED by differing densities** (box 60 vs 32);
deconfounding is a residue and **no claim is made**.  The successor is
named and sharp — **THE CRYSTAL QUESTION: can the grammar build a record
whose every event carries a wide chart with large overlaps (a tiling), the
way a courier record carries one rich sky?**  That is the next
construction unit on this road.  Residues: the density-deconfounded
comparison; non-identity transitions and the cocycle condition; the depth
profile of overlap.

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

**Status, combined: `[OPEN]`.**  The manifold arrow has an instrument
(Road 1), a measured gap that says the current records fail it, a named
next construction (the crystal question), and a parallel body of
suggestive-but-closed work (Road 2) that no unit has connected to it.

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
   of a composite is a bound on the coarse world (§B1.2).

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
- **The form is a CHOICE** (D50, `[GREEN-UNREVIEWED]`, §B6.12): the two
  strongest invariance demands leave the completion dimension **growing**
  (10 → 28 → 107), and adding foliation-invariance leaves it **exactly
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
without it.

The **measure at delivery scope** holds the other top slot, and for a
structural reason: arrows 5 and 6 both need probabilities at the scope
where the geometry lives, and §B9.4b closes the route that looked most
likely.

The **3+1 control** is *finished*, and its answer removed an instrument
rather than supplying one.

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

**Re-ranked against the destination** (superseding §A11.4 / §B11.4's
ordering, not their content):

1. **Charts and gluing → manifold (arrow 3), on ROAD 1 — the crystal
   question.**  New, and first: the destination's own definition requires
   it, and no other arrow can be posed without it.  The instrument now
   exists and has measured a confirmed gap (homogeneity 0.64 sprinkling /
   0.39 engineered / 0.07 generic walk), so the question is no longer
   "how would we tell?" but **"can the grammar TILE?"**.  Still needs a
   *replacement local instrument* for dimension, since §B5.7 denies the
   meter a dimensional reading for records — and §C6's channel-manifold
   law is the untranslated candidate.
2. **The v9 MANDATORY QUEUE — recorded, unscheduled, and now
   load-bearing.**  New entry, and near the top for a reason that is about
   *cost of ignorance* rather than about citability.  Road 2 has the
   furthest-advanced grown four-dimensional object in the programme's
   history and the only measured *interaction*; its funded review left
   exactly five items (O1–O5): **a 24-seed gated replication; a
   drift-matched, validation-gated volume instrument; the coupled ladder
   at `g = 0.18`; the gap-to-mean scan; the bridge pilot.**  None is
   scheduled (#128 closed the line).  Until they run, "a grown record
   universe was measured round and 4D" is **`PARKED-AT-PROTOCOL`, with
   "round" corrected and the volume conjunct instrument-suspect** — and
   the programme does not know whether it has an existence result or an
   artifact.  *The cheapest of the five (the replication) would settle
   most of it.*
3. **A workable probabilistic description at transport scope.**  Was §B11.4
   item 1; unchanged in importance, worse in prospects: menu-exact is
   impossible for any design (§B9.1), and sector-exact at `(actor, type)`
   granularity is closed on two independent grounds (§B9.4b).  The
   surviving candidates are strictly coarser aggregations (type-only,
   total-budget-only) and inexact / observable-only abstractions — all
   untested.
4. **The empty bridge (§C5) — and now a second one (§C6.11).**  Arrow 4 —
   the only Einstein content the corpus owns — lives on the v6 side of a
   bridge that has never carried a measurement (the Fisher identity, Gb2,
   specified and unrun).  And v9's webs stand in the same relation to the
   v10 grammar, with the additional twist that a user directive
   *declares* them not to be the click law.  **Two unbridged bodies of
   work, one theory.**
5. **(H1)**, unchanged: the last gap before the delivery-free settlement is
   unconditional.
6. **Is there a record-level demand that forces the stationary form?**
   Unchanged, and now doubly interesting: if the answer is permanently no,
   §D3's resemblance is the *only* interpretive home the boundary freedom
   has, which is a reason to state it carefully rather than a reason to
   believe it.
7. **The `G` calibration.**  Not solvable — that is the theorem — but the
   *dimensionless* question it leaves open (is `c_m = Gm²/ℏc` a record
   output?) is explicitly **eligible** and is the natural arrow-7 target.
8. **The residual pricing defects** (`h12`; the general-depth ladder;
   the `1/16` vs `1/24` merge), unchanged and still carried into the
   completion problem rather than patched.
9. **Where is the sprinkling floor?**  D55c's own residue — does genuine
   `M^{2+1}`/`M^{3+1}` shatter **3**? — is cheap, is the natural calibration
   of whatever replaces the meter, and would sharpen §B5.7's reframe from
   "sprinklings read ≈ 0" to a located floor.

**One structural observation, and it is the most useful thing in this
part.**  Arrows 3, 5 and 6 are all blocked, and **two of the three are
blocked on the same object**: a probabilistic description at transport
scope.  Arrow 3 alone is blocked on something genuinely new (a
construction, plus an instrument) — and it is the arrow with **two roads
and no bridge between them**.  So the programme has, at this moment,
exactly **three** independent next moves — build the manifold (Road 1's
crystal question), find the coarser aggregation, or **discharge Road 2's
unworked queue** — and everything else waits on one of them.

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
> scale), three are open (charts and gluing into a manifold — attacked from two
> unbridged directions, one of them measuring a confirmed gap and one of
> them holding a closed, review-indebted 4D construction; fields on it;
> particle creation), and the last is blocked
> at four independent points, one of which is the un-derivability of the
> scale and one of which is the incompleteness of the other arrows.  Governing all of
> it is the scale doctrine: no fixture-scale object is a particle, and
> units certify scale-invariant mechanisms rather than objects — which
> the substrate line reaches independently, since without coupling no
> collective excitation exists at any scale.  The
> three independent next moves are: **build the manifold** (can the
> grammar tile?), **find a coarser aggregation that closes at transport
> scope**, and **discharge the other road's unworked review queue**.
> Everything else in the programme currently waits on one of those three.
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
| **completion** | strictly positive cut data `Z` with transfer `q'(e|h) = q(e|h)·Z(h+e)/Z(h)`; what turns the weight system into a probability law | B6.1, A6.1 |
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
| **form (the stationary form)** | paper 30 §5.7's postulated shape `Z(h) = f(state(h))·λ^(−depth(h))`; what delivers uniqueness — **and a CHOICE, not a law** | B6.11, B6.12, A6.8 |
| **frontier sum `N(h)`** | the total raw weight of `h`'s menu; cut-attached (constant on all 427 classes) but **not a discrete gradient** | B6.1, B6.3 |
| **gauge** | see *causal order vs gauge* | B3.1 |
| **genesis** (`'g'`) | the initial version held by all participants — *"the declared supplied boundary"* | B2.2, A2.1 |
| **gradient / Doob `h`-transform completion** | the backward recursion `Z(h) = Σ q(e|h)Z(h+e)` from a positive terminal boundary; exists at every finite depth, at the cost of within-cut ratio deformation | B6.5, A6.5 |
| **(H0), (H1), (H2)** | the three depth-indexed hypotheses of D44a's conditional theorem: view invariants; **menu factorization from `sigma`**; transition determinism.  None implies another; **(H1) is undischarged** | B6.9, B6.13, A6.9 |
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
| **residue 1** | *does a strictly positive harmonic function exist on the infinite-volume state space?* — answered YES at d42a scope, conditional on (H0)–(H2) | B6.9, B6.10, A6.7 |
| **rootedness** | a completion distinguishing the root from the renewal point, i.e. distinguishing two record points the law identifies; what truncated completions do and `Zhat` does not | B6.8, A6.7 |
| **SC5** | the corrected sky capacity condition: `≥ 4` directions **AND** `≥ 16` distinct traces **AND the empty trace present** | B5.4, A5.5 |
| **sector** | one of the four weight budgets (propose / arbitrate-and-merge / deliver / idle), each `1/4` when open, idle absorbing the rest.  The **delivery** sector total is `1/4` at every rung of §B9.1's ladder — but that is **not a law of sectors**: arbitration sectors reach `1/2` and `1/8`, totals live in `{k/(4m)}`, so the sector alphabet is not finite either | B2.6, B9.4, B9.4b, A9.4 |
| **shadow / trace** | the set of directions at or below a given future (or past) event — the objects all the sky geometry is done on | B5.1, A5.2 |
| **shatter** | realizing **all** `2^k` subsets of a `k`-set of directions as traces; requires the **empty** trace | B5.3, B5.4, A5.3 |
| **`sigma`** | the bounded local-state abstraction of the **full view** modulo base renaming: holdings pattern, live-proposal structure with conflict components, superseded marks restricted to referenced bases.  36 values at d42a; **unbounded, menu-exactly, at transport scope** | B6.9, B9.2 |
| **sky** | the direction set at an event, under one of three committed definitions: **SKY-A** covers, **SKY-B** an antichain at a committed height, **SKY-C** the dual past sky.  SKY-A and SKY-C **can never shatter** | B5.1, B5.4, A5.2 |
| **supersession** | a version is superseded when a later version on the same line replaces it; superseded structure may still be recorded but may no longer be actionable | B2.3, B9.1 |
| **swept corner** | the sub-family of proposal branches where the enumeration is complete and every extension factor is exactly `1/8`, making ratio locality a theorem there | B6.5 |
| **`tau`** | `sigma`'s construction applied to an actor's **own view**; **refuted** as an own-view object (D46a) | B6.13, A10.2 |
| **transport scope (d42b1)** | the grammar with delivery and merge; where the dimension results live and where the measure question is **open** | B2.2, B6.14, B9 |
| **VC dimension** | the largest set a family of sets can shatter; caps on `S²` have VC dimension **4**, which is why the sphere never shatters 5 | B7.4, A7.2 |
| **version** | the content object a line writes; created only by arbitration or merge | B2.2, A1.1 |
| **view** | see *own view / full view*; a view is a **sub-record**, nothing psychological | B3.2 |
| **`Z`** | the completion's positive cut data; `Zhat = 2^(−|h|) f(class(sigma(h)))` is the settled one at d42a scope | B6.1, B6.10 |
| **`Zhat`** | the settled root-free completion: `λ = 2`, `f = (4,4,3,7,3,3)/3`, unique up to scale **within the form** | B6.10, A6.7 |
| **axioms R / S / C** | the earlier corpus's three: laws are laws of whole sealed histories; **no distinction without a record**; couplings fixed by self-consistency under refinement | C1 |
| **Barandes-indivisible** | a process whose one-time transition law fails Chapman–Kolmogorov except at sparse **division events**; the barrier is the gap between `\|Σ\|²` and `Σ\|·\|²` — the interference cross-term | C1, C3 |
| **Born = K1** | the statement that a constructed isometric arbitration family's squared branch amplitudes reproduce the committed `K1` kernel exactly (`1/2`–`1/2` on the 2-conflict, recomputed from the layer).  Appears in v10 paper 31 §4.3; the earlier Born layer (paper Va) is the same *kind* of statement — **relation formally unestablished** | C3.5, C5.4 |
| **chart / gluing** | the unbuilt local-patch and overlap-agreement structure that turns a causal order into a **manifold** — arrow 3 of the destination, `[OPEN]`, the first construction the destination newly requires | D2 |
| **covariantization** | the result that a **Poisson sprinkling** of division events makes the kinematic layer Lorentz-invariant outright (no recoverable frame; arrow in the causal order, not a slicing; Hegerfeldt dissolved for the free flash), converting the GRW/CSL foliation wall into named dynamical residues | C3.6 |
| **CP-divisibility** | an open-system channel property: the dephasing rate stays `≥ 0`, so no information backflow and **no revivals**.  **Orthogonal** to Barandes-indivisibility — neither implies the other | C3.1 |
| **division event** | the record at which an indivisible stochastic process momentarily factorizes; the primitive of the causal-set gravity sector, where *order + number = geometry* | C1, C3.6 |
| **G no-go** | `[NO-GO]` the absolute scale `σ_A` (weight `−2`), in bijection with Newton's `G` (weight `+2`) via `G·σ_A = 1/4`, is not derivable: every intrinsic record functional is weight-zero, so `κ·σ_A = 2π` and `G·Λ²` (two **separate** fixed pure numbers) are all that is fixed | C2.2 |
| **graviton blindness** | 4 of 9 stress components priced universally; the 5 traceless ones spanned but only at a boost-dependent second-order coupling; four obstructions reducing to one root — the needed structure lives only in a continuum algebra a finite record lattice cannot host.  The geometry is **spin-2-active but not-a-graviton** | C2.5 |
| **holonomy (sealed)** | the coherent, uncommitted relative phase a system carries **between** seals; sealing destroys it.  Its irreducibility is the earlier corpus's quantum/classical dividing line | C1 |
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

1. **Papers 1–29 are essentially absent.**  The v10 line has 32 papers;
   this document covers the recent campaign (roughly papers 30–32 and
   ledger entries #404–#433) plus the objects those depend on.  The
   sealed-holonomy line, the SCIR rulebook line, the predictive-record-DAG
   boundary, the reception theorem, the action-cocycle work, and the whole
   v1–v9 prehistory appear only where a later result cites them.  Paper 57
   (v6) appears only as the source of the un-fixable-`G` no-go.

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
   exhibits are not walked through.

4. **D46's six ladder units get one paragraph each at most.**  D46b
   (Martin at transport, three reversals) appears in B9.6; D46c (Minkowski
   certificates) appears only via `W3_CERT` in B5.3; D46d appears in B7.2;
   D46e in B2.8(v); D46f in B10.13; D46g (embedded-head reconciliation)
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
    is read from a committed source.  Where a source is green-unreviewed
    (**D50** §B6.12, **D55c** §B5.7, **D57** §B9.4b) or advisory
    (**D56** §B9) the text says so at the point of use, and those four are
    the only non-terminal sources the book leans on.  None is citable
    until it has had a hostile round, and each says so where it is
    used.

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

14. **PART D is a roadmap, not a result.**  Arrows 3, 6 and 7 have no
    corpus content whatsoever beyond being named; their entries are
    statements of what is missing.  The `[MY READING]` in §D3 is speculation
    and is marked three times as such.  The D58 designation for the
    manifold unit comes from the coordinator's direction, **not** from a pin
    on disk.

---

*End of document.  `v10/THE-THEORY-SO-FAR.md` — the corpus's single
synthesis, current at the ledger state named in the maintenance stamp.*
