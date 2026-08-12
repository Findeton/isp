# FAC (PAPER-35) — K2 EFFECTUS-LENS REVIEW (verdicts, licensure, meaning)

**Seat:** K2, the effectus lens.  **Posture:** hostile.  **Status:**
CANDIDATE until adjudication.

**Object, verified at open AND at close (all five identical at both):**
paper `v14/paper-35-fac.md` 2e9cbae8a83e · code `v14/code/fac_exact.py`
53e1e2683937 · output `v14/code/fac_output.txt` 43212e390250 · receipt
`v14/code/fac_receipt.json` 240bad74217a · pin `v14/note-fac-pin.md`
11380265fcf3.  Authorities read at their declared digests: AID
adjudication 04cd41ed858b, AID terminal paper ecdd3fbf1d06.  Git strictly
read-only; this file is my sole repo write.  No in-flight sibling was read.

**Recomputations: 128** distinct published or derivable quantities
re-derived independently, on top of two complete re-runs of the
5,856-history census under my own drivers (a rebuilt-corpus route and a
per-grain leg-split route), plus a 40-sample concatenation probe.  The
harness imported the instrument's arena primitives and rebuilt every
census loop, every leg tally, every set comparison and every head input.

---

# GRADE: **AWF** (accept-with-fixes) — repair ordered, no REJECT

**Nothing computed moved.**  Every delivered number reproduces exactly:
5,852 / 4 at the actor grain; 5,810 / 46 at the carrier grain;
cardinalities [1, 2, 3, 9]; 6 of 21,147; 10 of 42,295; 0 coin-order
disagreements; 11,799 LEG-4 passes per order; 5,852 atom breaks; the
thresholds 3, 4, 5 with the distribution 4/521/75 over C3 and 4 at all of
C1 and C2; |Aut| = 108; the whole grain-triangle table; the whole
coherence ladder.  The head word `FAC-STRATIFIED` is **correctly derived**
— `head_law` compares the two non-unique history sets as SETS
(`a == c`), not as counts, exactly as the pin ordered, and my rebuild
confirms 4 ⊊ 46 with 42 carrier-only and 0 actor-only.  The outcome
vocabulary is genuinely parsed from the pin's bytes and constrains the
head.  The AID §2 not-licensed list is respected in the paper's text: I
found no wall hit, no unscoped reality slogan, and no five-resonance
anywhere in paper, code or receipt.

The failures are, once again, **at the binding between measurement and
prose** — plus one place where the paper defines an object the instrument
does not measure.  Eight MAJORs, thirteen MINORs.

---

# MAJORS

## MAJOR-1 — §5 defines the groupoid object the census does NOT measure

§5: "objects are the events, **an arrow is a structure-preserving
bijection between two event footprints**, and a global object is a FAMILY
of local identifications — one per event — subject to a DECLARED
COHERENCE RELATION on the times."

The coherence census does not draw its local identifications from
structure-preserving arrows.  `local_syms(F)` returns **all 3! = 6**
permutations of an event's footprint with no structure condition
whatsoever; `groupoid_arrows` — the only place the structure-preserving
condition lives — feeds the arrow-profile row of §5 and nothing else.

**Establishing measurement (mine).**  The free count of the measured
object is 6^T exactly: γ(w = 0) = 10,077,696 = 6⁹ at C1, 2,176,782,336 =
6¹² at C3, 101,559,956,668,416 = 6¹⁸ at C2 — reproduced at all three.
The structure-preserving groupoid has isotropy order **3** at every event
of all three samples, so the corresponding free product is 3^T: 19,683 /
531,441 / 387,420,489.  The two objects differ by a factor of 2^T.

The measured object is the *right* one — it is the correct groupoid-grain
relaxation of `stab_raw_actor`, which quantifies over all of S₉ with no
structure condition, and it is what makes the complete relation return the
global stabilizer at 5,856 of 5,856.  The **sentence** is wrong.  A reader
who follows §5's definition computes 3^T-sized families and cannot
reproduce a single ladder row.

Worse, the paragraph then joins the two objects with an inference:
"its isotropy orders are 1, 3 and 6 and its connected components run from
1 to 5, **so** the local identifications genuinely differ from event to
event."  The isotropy/component numbers are properties of the
structure-preserving groupoid; the local identifications the ladder counts
are unconstrained permutations.  The "so" crosses two objects.

**Licensed replacement (exact):**
> "Two objects are measured here and they are kept apart.  THE COHERENCE
> CENSUS: a local identification at event *t* is any bijection of that
> event's three-actor footprint to itself — all six — and a coherent
> family is a choice of one per event agreeing, on every pair of times the
> declared relation names, wherever the two footprints meet.  The empty
> relation therefore returns 6^T exactly: 6⁹ = 10,077,696 at every strict
> triple, 6¹² = 2,176,782,336 at every driven-window schedule, 6¹⁸ =
> 101,559,956,668,416 at every concatenation.  This is the groupoid-grain
> relaxation of the global test, which likewise quantifies over all of S₉.
> THE STRUCTURE-PRESERVING GROUPOID, measured separately: objects are the
> events, an arrow is a footprint bijection preserving the internal
> co-division cells with their declared directions, and on the 672
> histories of the C1+C3 sub-window its isotropy orders are 1, 3 and 6 and
> its connected components run from 1 to 5.  Its free product, 3^T at the
> sampled histories, is not the ladder's count and is not used in the atom
> word."

## MAJOR-2 — §3's "precisely when" is FALSE at the delivered numbers (125 vs 2)

§3, glossing the thesis field: "it is a description of the mechanism
rather than a summary of the count: **a coarser subsystem structure is
admissible precisely when the history never distinguishes the actors a
coarsening would merge**."

"The history never distinguishes the actors a coarsening would merge" is
LEG-2 (each event a union of blocks).  "Admissible" is all four legs.
They are not the same predicate.

**Establishing measurement (mine, and the unit's own receipt agrees).**
At each of the four non-unique histories — C3 #0/#85/#170/#255, global
indices 5256/5341/5426/5511 — the number of partitions of the nine actors
passing LEG-2 is **125**; the number admissible is **2**.  The receipt
already carries both:
`leg_binding.profiles[1] = {leg1: 6, leg2: 125, leg3: 21147, all_three: 2,
histories: 4}`.  A biconditional whose two sides are 125 and 2 is not a
biconditional.

Restricted to the six geometry-leg survivors the counts do coincide (2 =
2) — but only because LEG-3 and LEG-4 never bind at the actor grain on
this corpus (MAJOR-3), and the unit's own control arm shows LEG-3 binds at
three of five synthetic arenas.  So the sentence is neither true as
written nor "a description of the mechanism": it is a fact about six
partitions on one corpus where two of four legs happen to be inert.

**Licensed replacement (exact):**
> "Among the six partitions the geometry leg admits, the one that joins the
> discrete partition is admitted by the history leg and no other leg: at
> each of the four non-unique histories the class partition is the unique
> non-discrete geometry survivor whose blocks are unions of every event.
> This is a statement about those six, not about coarsenings in general —
> 125 partitions of the nine actors pass the history leg at each of those
> four histories and 2 are admissible."

## MAJOR-3 — the per-grain leg-binding asymmetry is never measured, and §4's closing sentence is false at the carrier grain

§4 declares LEG-3 non-binding and closes: "The record leg is therefore a
real constraint that this corpus happens not to exercise, and **the
binding here is done by geometry and history**."  LEG-4 appears nowhere in
the per-leg sweep — not in §4's bullets, not in `leg_binding`, which
carries `binding_legs: [LEG-1, LEG-2]` and `non_binding_legs: [LEG-3]`
and simply omits LEG-4.  The unit's own rule (G-WHICH-LEG-BINDS) is "A leg
that never fails on a corpus is declared non-binding ON THAT CORPUS and is
exercised on the control arm instead."  It is not applied to LEG-4.

**Establishing measurement (mine).**  Splitting every LEG-4 evaluation of
both censuses by grain:

| grain | LEG-4 evaluations | LEG-4 failures | verdict |
|---|---|---|---|
| actor (induced cell partition) | 5,860 | **0** | NON-BINDING on this corpus |
| carrier | 6,317 | **378** | BINDING |
| both | 12,177 | 378 | passes 11,799 ✓ |

11,799 = 12,177 − 378, which is exactly the published pass count at each
order, so the arithmetic ties out.  Additionally LEG-3 fails **0** times
after LEG-2 at *both* grains (35,136 actor evaluations swept).

Two consequences the paper does not state and must:

1. **The actor-grain result is dynamics-blind.**  The headline 5,852, the
   thesis, the FORCED and DECLARED control words and half the STRATIFIED
   slot are, as measured, purely LEG-1 ∧ LEG-2 — geometry and
   participation.  Paper-20's coupled step never excluded a single
   actor-grain factorization.  §"The short of it" happens to say the right
   thing ("after the history leg the actor-grain factorization is unique
   at 5,852") but the paper nowhere states this as the measured fact it
   is, and §4 asserts it without measuring it (that sweep never evaluates
   LEG-4).
2. **At the carrier grain the sentence is false.**  There the binding legs
   are LEG-1, LEG-2 **and LEG-4**; LEG-4 is the only leg that separates
   anything the first two do not, 378 times.  Since the STRATIFIED verdict
   is produced entirely by the carrier grain, the dynamics leg is
   load-bearing for the head word and is reported as if it were not in
   the picture at all.

Also: 11,799 is published as a bare numerator (§3).  Its denominator
(12,177) and its complement (378) are not published, so a reader cannot
tell that the leg ever fired.

**Licensed replacement (exact), as a table plus one sentence:**
> | grain | LEG-1 | LEG-2 | LEG-3 | LEG-4 |
> |---|---|---|---|---|
> | actor | binds | binds | 0 failures in 35,136 | 0 failures in 5,860 |
> | carrier | binds | binds | 0 failures | **378 failures in 6,317** |
>
> "On the committed corpus the record leg never fires at either grain and
> the dynamics leg never fires at the actor grain: the actor-grain census
> — and therefore the thesis, and therefore the FORCED and DECLARED
> control words — is decided by geometry and participation alone, with the
> coupled step admitting all 5,860 induced partitions it was offered.  At
> the carrier grain the dynamics leg is the one that separates: it rejects
> 378 of the 6,317 partitions the first three legs pass, at both declared
> coin orders, and without it the carrier census would not return the
> counts published here."

## MAJOR-4 — the 672-history sub-window is used twice and declared nowhere in the paper; "the declared sub-window" denotes two different objects

§4 declares a sub-window properly: "the 72 strict-triple histories plus
every history the census found non-unique, 76 in all, with the remaining
5,780 named as the complement."  Good.

§5 then writes "on the 672 histories of **the declared sub-window**" and
§6 writes "at 668 of 672 rows and at the carrier grain at 0 of 672."  The
672-history sub-window is never declared in the paper — not its
membership, not its complement, not in §9's limits section.  A reader
arriving at §5 binds "the declared sub-window" to the 76 just declared;
it is a different object.

**Establishing measurement (mine):** the 672 sub-window is C1 (72) + C3
(600); its complement is **all of C2, 5,184 histories — 88.5 % of the
corpus**.  The §6 table's history column sums to 672 (72+48+216+140+150+
42+3+1), so the size is recoverable; the identity is not.  The receipt
knows (`grain_triangle.sub_window 672, complement 5184`); the paper does
not say.

This is a limit that bites where it is not stated: §6's two headline
readings — "the two tests agree at the actor grain at 668 of 672 rows and
at the carrier grain at 0 of 672" and "the carrier answer is not the actor
answer" — are measured on a window from which the corpus's largest corpus
is absent.  §9 does not mention it.

**Licensed replacement (exact), to stand at first use in §5 and be
referenced in §6 and §9:**
> "The stabilizer and arrow measurements below run on a declared
> sub-window of 672 histories — all 72 strict triples and all 600 driven
> window schedules — because the 5,184 concatenations are pairwise
> concatenations of the strict triples and their stabilizers are the
> intersections of their parts'.  The complement is named: C2, 5,184
> histories, is outside this window."

## MAJOR-5 — the carrier grain's inventory, which IS the STRATIFIED verdict, is neither enumerated nor priced; the nine-fold row is unpublished; and the carrier names are not referents

The pin: "> 1 → the division is DECLARED, **with the full inventory
enumerated and priced**."  The paper discharges this at the actor grain
("the class partition joins the discrete one and the inventory has two
members, both named") and not at all at the carrier grain, where §3 stops
at "a strictly larger set that contains the actor grain's four and adds 42
more."

**Establishing measurements (mine).**

- Carrier cardinality distribution: **{1: 5,810, 2: 15, 3: 30, 9: 1}**
  (the receipt carries it; the paper publishes none of it).
- The single 9-cardinality history is **C3 #255, the ANT-constant
  schedule** — the same history that carries the actor grain's ANT
  inventory row.  Its nine admissible carrier factorizations include the
  **1-block partition of all 27 cells** and the 3-block (3 × 9) partition.
  At that one history the committed law admits a factorization with ONE
  subsystem.  That is the most consequential single row in the unit and it
  is unpublished.
- The 42 carrier-only histories fall into exactly three admissible-set
  profiles, 14 histories each: {discrete, a 9-block, a 6-block},
  {discrete, a different 9-block, a different 6-block}, {discrete, a third
  9-block}.  So what "joins" at the carrier grain and nowhere else is a
  coarsening of the 27 cells into nine blocks of three, sometimes together
  with a 3×6 + 3×3 coarsening.  None of this is in the paper.
- **The carrier names are not injective.**  The 10 geometry-leg survivors
  carry only **5 distinct names**: `CP-9-BLOCKS-9x3-WITHIN-ONE-DIRECTION-
  ACROSS-SITES` denotes **five different partitions** and `CP-6-BLOCKS-
  3x6-3x3-ACROSS-DIRECTIONS-ACROSS-SITES` denotes two.  The receipt's
  `cell_census.inventory` therefore reports `{...9x3...: 49}` as a sum
  over five distinct objects under one key, and the 38-row class-binding
  ledger passes precisely because it recomputes the (colliding) name from
  the object.  Under the pin's "REFERENT-BOUND gates (names bound to
  objects measured)", a name denoting five objects is not a referent.

The head word is STRATIFIED, not DECLARED, so the pin's inventory clause
is arguably addressed to a word not emitted — but STRATIFIED is *defined*
by one grain admitting more than one, and the paper prices that grain's
"more than one" at zero.

**Licensed replacement (exact):**
> "At the carrier grain the admissible set has cardinality 1 at 5,810
> histories, 2 at 15, 3 at 30 and 9 at one.  What joins the discrete cell
> partition is always a coarsening across sites within a direction: at 42
> of the 46 it is one or two of the nine-block (9 × 3) partitions, twice
> accompanied by a 3 × 6 + 3 × 3 partition; at the four class-constant
> schedules the actor grain's class partition appears in its directionwise
> image as well.  The single nine-fold row is the ANT-constant schedule,
> and its nine admissible factorizations include the three-block partition
> and the one-block partition of the whole carrier: at that history alone
> the committed structure descends to a quotient with a single object.
> Each of the ten geometry-leg survivors is listed in the receipt by its
> block partition, since the block-shape names collide (five of the ten
> share one name)."

## MAJOR-6 — the R = 6 rung is theorem-forced by the R = 3 rung; AID's adopted "5,184-theorem-forced disclosure" is repeated undischarged

§7: "The result is reported at every rung the corpus carries, **from that
rung's own histories rather than from the corpus aggregate**. ... At R = 6
the actor grain is unique at all 5,184, the atom breaks at all 5,184, and
the threshold is 4."

C2 *is* the set of ordered pairs of C1 histories.  Stab(H₁+H₂) =
Stab(H₁) ∩ Stab(H₂), and the LEG-2 survivor set of a concatenation is the
intersection of the parts'.

**Establishing measurement (mine).**  At all 72 strict triples the LEG-2
survivor count among the six geometry survivors is **1** and the raw actor
stabilizer is **1** — no exceptions.  Therefore every one of the 5,184
concatenations has LEG-2 survivor set = {discrete} and trivial stabilizer,
*before any census runs*.  Verified on a 40-concatenation sample: LEG-2 =
1 and stab = 1 at all 40.  What is NOT forced at R = 6 is the
adjacent-relation family count (859,963,392 to 15,479,341,056), so the
atom BREAK at R = 6 does carry one independent measurement; the
uniqueness and the stabilizer triviality do not.

AID's adjudication §6 already adopted "the 5,184-theorem-forced
disclosure" as a repair item.  The same disclosure is owed here and is
absent, and it is what turns "three rungs, and it transports" into "two
independent rungs and one forced one."

**Licensed replacement (exact):**
> "R = 6 is not an independent rung.  C2 is the set of ordered pairs of C1
> histories; the stabilizer of a concatenation is the intersection of the
> parts' stabilizers and its history-leg survivors are the intersection of
> the parts', so uniqueness at all 5,184 and trivial stabilizer at all
> 5,184 follow from the R = 3 row by theorem and are checked, not
> discovered.  What R = 6 measures independently is the adjacent-relation
> family count, which runs from 859,963,392 to 15,479,341,056, and the
> collapse threshold, which is 4."

## MAJOR-7 — "three to five events of coherence" converts a window width into an event count without naming the conversion

The declared relation is R-WINDOW-w = {(t, s) : t − s ≤ w}, an index
distance.  A threshold w* = 4 says the identification must agree on every
pair of events at distance at most 4 — i.e. across every **five**
consecutive events; w* = 3 spans four events, w* = 5 spans six.

§7 prices thread-hood at "**three to five events of coherence**", which
reads as an event count and is the window-width parameter.  The corpus has
an engraving on exactly this shape: AID §4 reconciled a five and a four
that were two objects in two units (schedule packing vs information), and
ordered both rendered with their objects named.

**Establishing measurement (mine):** `coherence_pairs` returns
`[(t, s) : t − s <= w]`; `collapse_threshold` searches w upward from 0
against the complete-relation target.  Thresholds {3, 4, 5} are widths,
distributed 4 at all 72 strict triples and all 5,184 concatenations, and
3/4/5 at 4/521/75 of the 600 driven-window schedules.

**Licensed replacement (exact):**
> "This corpus prices thread-hood at a coherence WIDTH of 3, 4 or 5 in
> event index: the identification must agree on every pair of events whose
> indices differ by at most w*, which is a span of four, five or six
> consecutive events.  The width, not the span, is the measured constant."

## MAJOR-8 — the corpus-level reachability of FORCED is narrower than the pin's feasibility line and than §8's pigeonhole sentence imply

§8: "The head law returns a different word on each of the first three
arenas, **so no pigeonhole decided the verdict before the run**."  That
inference is about the LAW across arenas.  It is true and it is not the
question the #299 engraving asks, which is whether each word was reachable
**at the delivered arena**.  The three control arms that emit FORCED and
DECLARED are sub-corpora (72 and 4 histories); the whole-corpus arm emits
STRATIFIED.

**Establishing measurement (mine).**  At the whole corpus, FORCED requires
both non-unique sets empty.  The 600-schedule window enumerates all 4⁴ =
256 class quadruples by construction, so the four class-constant schedules
are in the corpus by construction; at each, the matching class partition
passes LEG-1 (it is one of the six coset partitions — a closed form the
unit proves) and LEG-2 (its blocks are exactly the events — the signature
refinement closed form the unit proves), and LEG-3 cannot fail because the
record is site-constant at 5,856 of 5,856.  So at the delivered corpus the
FORCED word hung entirely on LEG-4 failing at those four induced
partitions — and LEG-4 fails **0 times in 5,860 actor-grain evaluations**.
That is a much narrower reachability than the pin's line
("nothing in the arena pre-decides it").  The live discrimination at the
corpus was DECLARED-vs-STRATIFIED, and it turned on the 42 carrier-only
histories, which is a genuine LEG-4 measurement.

This is partly a **pin-design item and therefore the adjudicator's**, on
the AID §7 precedent: the pre-registered feasibility line for
`FAC-FACTORIZATION-FORCED` asserts corpus-level reachability that the
arena's own construction plus two of the unit's own closed-form theorems
substantially foreclose.  The unit should say so rather than let §8's
sentence stand for it.

**Licensed replacement (exact):**
> "The head law is multi-way and its three substantive words are emitted by
> three declared arenas through the same criterion.  At the committed
> corpus specifically, the discrimination was between DECLARED and
> STRATIFIED: the four class-constant schedules are in the driven window by
> construction, and at each of them the matching class partition is
> admitted by the geometry leg's closed form and the history leg's closed
> form with the record leg unable to fire, so only a dynamics-leg failure
> at those four could have returned the forced word.  The dynamics leg
> fails 0 times in 5,860 actor-grain evaluations.  What the run decided at
> the corpus was whether the two grains' non-unique sets are equal — and
> they are not, by 42 histories."

---

# MINORS

**MINOR-1 — §6 drops the four exceptions.**  "the grain at which the
history-stabilizer and the realizable group coincide is the actor and site
grain, not the carrier" follows a sentence giving 668 of 672 and then
states the coincidence unqualified.  Licensed: "…coincide at 668 of the
672 rows of the declared sub-window, and at 0 of 672 at the carrier."

**MINOR-2 — route B hard-codes one of the atom law's two inputs.**
`independent_head` returns `atom_law(ab, True)`; the `holds_at_complete`
argument is the literal `True`, not re-derived.  §10's "re-applies the
head law to its own numbers" is therefore true of the head word and only
half true of the atom word.  Repair: re-derive the complete-relation
comparison in route B, or scope §10's sentence to the head word and say
the atom word's second input is carried from the ladder gate.

**MINOR-3 — the output's own sentence is false as to one family.**
G-EVERY-OUTCOME-WORD-EMITTABLE prints "5 of the pin's 5 families are
reached by an arena: none unreached."  `FAC-BLOCKED-AT-THE-GROUPOID-
COMPLETE-RELATION` is reached by a direct call `atom_law(1, False)` at
line 2438, not by any arena, and `controls.words_emitted` conflates
arena-emitted with law-evaluated words in one list.  The paper §8 is
correct ("reachable only from an instrument fault"); the delivered output
artifact is not.  Repair: split the list, or print "4 of 5 families reached
by an arena; the blocked family reached by evaluating the law at a state
the ladder gate excludes at 5,856 of 5,856 histories."

**MINOR-4 — §5's Paper-33 sentence is circular as written and understates
what is true.**  "Paper 33's 5,852 histories with trivial stabilizer are
exactly the histories where the global stabilizer is trivial and the
adjacent-coherence groupoid is not at 5,852 histories" says, in its first
clause, that the histories with trivial stabilizer are the histories with
trivial stabilizer.  The available stronger statement, which I measured:
**{actor-grain non-unique} = {nontrivial global stabilizer} = {no atom
break}, as SETS, all three coinciding at the same 4 histories** — and the
containment `carrier-unique ⊂ actor-unique` also holds as sets.  Licensed:
"At every history the global stabilizer is trivial exactly when the
actor-grain factorization is unique and exactly when the atom breaks —
three predicates, one partition of the corpus into 5,852 and 4, verified
element by element.  On this corpus the decomposition census at the actor
grain returns the same split as the naming census; what it adds is the
carrier grain's 42 and the groupoid grain."  (This also states plainly a
fact the paper currently leaves to inference: at the actor grain, this
unit's answer is extensionally AID's.)

**MINOR-5 — a numeral collision inside one clause.**  §7: "3, 4 or 5
across the driven window at 4, 521 and 75 histories respectively" — the
first `4` is a threshold value and the second `4` a history count, in one
breath.  Both true; the sentence invites the LOR reading.  Repair: "…at
widths 3, 4 and 5 respectively at 4, 521 and 75 of the 600 schedules."

**MINOR-6 — the published ladder cannot show the collapse it reports.**
§5's table tops out at R-WINDOW-3, but the threshold is 4 at all 72 strict
triples and all 5,184 concatenations — 5,256 of 5,856 histories, where the
collapse row simply is not tabulated.  The window declaration in the
receipt is honest about this ("w = 0, 1, 2, 3 … the threshold is derived by
increasing w"); the paper is not.  Repair: one sentence saying the
tabulated ladder stops below the threshold for C1 and C2 and that §7's
thresholds come from the uncapped upward search.

**MINOR-7 — the AID not-licensed list is walled 4 of 5.**  Walls cover
items 1–4 (identity-to-matter, unscoped record-not-a-thread,
actor-factorization-forced, the five-resonance).  Item 5 — "the weld's
freedom and identity's freedom are disjoint (it is containment, with an
index)" — is unwalled.  It is arguably inapplicable (no weld here), but
its *shape* is this unit's central structure: 4 ⊂ 46 is containment with
index 42, and the paper renders it correctly.  Note the item as
inapplicable rather than leave it unaccounted.

**MINOR-8 — a false code comment.**  SECTION 9's header says of the head
law "**It types no word**: the outcome vocabulary is parsed from the pin."
`head_law` returns three string literals.  What is parsed from the pin is
the family set those returns are *checked against*, which is the real and
sufficient guarantee.  The paper §10 states it correctly; the code comment
does not.

**MINOR-9 — an unquantified strength word as a bolded claim.**  "**At the
actor grain the division is essentially rigid.**"  Under #267 a bolded lead
is a claim.  "Essentially" is doing work the next sentence does properly
(5,852 of 5,856).  Given MAJOR-3, the accurate lead is "At the actor grain
the division is unique at all but four histories, and geometry and
participation decide it."

**MINOR-10 — "respectively" without an antecedent.**  §4: "the record leg
binds at three of the five, cutting the lattice to 1,015, 125 and 104
respectively."  The list those correspond to (X1, X3, X4) is in §8's table,
four sections later.  Name them inline.

**MINOR-11 — the referent-binding gate covers only the `N of M` form.**
The E-24 ledger publishes 6 ratios; G-SENTENCE-REFERENT-BINDING checks 5.
The uncovered one is 42,295 against Bell(27), which the paper writes with
"against" rather than "of" and which therefore escapes a syntactic scan.
Both members are in fact in one universe (`windows`), so nothing is wrong;
the gate's coverage is narrower than the duty, and the duty as the pin
states it is about *sentences pairing numerals*, not about `N of M`.  I
swept all 36 prose sentences of this paper carrying two or more numerals
by hand and found no cross-universe pairing beyond those already listed as
MAJORs; the gate should nonetheless be widened or its scope stated.

**MINOR-12 — scope "no arena transformation".**  §6: "The carrier's excess
is freedom to permute cells in ways no arena transformation realizes."
The realizable group is the declared order-108 group of affine maps
permuting the three declared link directions; |AGL(2,3)| = 432, so the
declared group has index 4 in the full affine group.  Defensible, since
the links are part of the declared arena — but say "no transformation in
the arena's declared automorphism group (order 108)".  The
size-of-S₂₇ caveat IS present at this, the only, use.

**MINOR-13 — the top of the grain-triangle range is |S₂₇| and the paper
does not say so.**  §6 publishes "from 512 up to
10,888,869,450,418,352,160,768,000,000".  That number is exactly **27!**
(verified).  At that one history the raw carrier test is completely
vacuous: the entire symmetric group on the cells stabilizes the history.
That is the direct, quotable evidence for the paper's own "which is a
statement about the size of S₂₇ as much as about the law", and leaving it
as a bare 29-digit numeral wastes the unit's best line.  Licensed: "…up to
10,888,869,450,418,352,160,768,000,000, which is 27! — at that history the
raw test is vacuous, the whole symmetric group on the cells stabilizes it,
and the realizable stabilizer there is the arena's entire order-108 group."

---

# THE TWO RULINGS THIS SEAT WAS ASKED FOR

## RULING A — THE THESIS SENTENCE: **licensed as stated, one-directional; §3's binding of it is not**

The head field
`THESIS=THE-LAW-ADMITS-MORE-THAN-ONE-FACTORIZATION-ONLY-WHERE-THE-HISTORY-REPEATS-A-PARALLEL-CLASS`
is an "only where" — a necessary condition — and I measured it in both
directions at both grains:

| predicate | extension | actor non-unique inside it | carrier non-unique inside it |
|---|---|---|---|
| repeats a parallel class (some class in ≥ 2 rounds) | **348** of 5,856 | 4 of 4 | **46 of 46** |
| one parallel class in EVERY round (class-constant) | **4** of 5,856 | 4 of 4 | 4 of 46 |

**The necessary direction holds, and at BOTH grains** — all 4 actor
non-unique and all 46 carrier non-unique histories repeat a parallel
class, 0 exceptions.  The head sentence is therefore true as written and
must remain one-directional: the sufficient direction fails badly (348 →
4 at the actor grain, 348 → 46 at the carrier).  The paper-23 iff lesson
is satisfied by leaving "only where" alone.

**What is NOT licensed is §3's identification of that field with the
class-constant description.**  §3 writes "…at the four schedules that
repeat a single class in all four rounds.  **That is the thesis field**" —
binding a field whose predicate has extension 348 to a description whose
extension is 4.  At the actor grain the tight characterization is measured
in both directions and should be stated as such; at the carrier grain it
is not available, since only 4 of the 46 are class-constant.

**Exact licensed rendering:**
> "Every history at which the criterion admits more than one factorization
> repeats a parallel class — all 4 at the actor grain and all 46 at the
> carrier grain — and 348 of the 5,856 histories repeat one, so the
> condition is necessary and far from sufficient; that is what the head's
> thesis field asserts and no more.  At the actor grain the tight
> characterization is measured in both directions: the 4 non-unique
> histories are exactly the 4 that use one parallel class in EVERY round,
> and the partition that joins the discrete one is that class.  At the
> carrier grain no such biconditional is measured: 4 of the 46 are
> class-constant and 42 are not."

## RULING B — THE ATOM WORD AND THE THREAD QUESTION

**What breaks.**  `FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN` is computed from
two facts, both of which I reproduced: the complete coherence relation
returns the global stabilizer at 5,856 of 5,856 histories (so the grain is
calibrated), and at 5,852 of those the global stabilizer is trivial while
the adjacent-coherence count exceeds 1 (124,416 at every strict triple;
859,963,392 to 15,479,341,056 at the concatenations).  What breaks is the
INFERENCE from group-level triviality to groupoid-level rigidity — nothing
about actors.  The mechanism the paper gives is right and is measured:
within a round the three events are pairwise disjoint, so R-ROUND imposes
nothing and returns the free product exactly (R-ROUND = R-EMPTY at all
three corpora, verified).

**The wall is respected.**  No sentence of the paper asserts or denies that
actors are threads.  I scanned for the AID §2 items and for paraphrases in
paper, code and receipt: no hit, no five-resonance anywhere (the only
"horizon" in the unit is the wall needle itself and one coin-order
docstring; the only "resonance" is the wall's name).  §9's "Nothing here
is a claim about what actors are" is accurate.

**Exact licensed sentence for the thread question** (this replaces the
run of sentences from "Thread-hood is not something the census found…"
through "…what it costs and where it is being made", and folds in MAJOR-7
and MAJOR-1):

> "The global grain asks one permutation of a persistent actor set to fix
> every event.  Replace it with a family of local identifications — any of
> the six permutations of each event's footprint, one per event — required
> to agree only where a declared coherence relation on the times says
> they must, and the answer moves: identity is forced at the complete
> relation at 5,852 of 5,856 histories and at the adjacent relation at 0
> of them.  The least coherence WIDTH at which the two meet is derived per
> history by searching upward without a cap and is 3, 4 or 5 — a width of
> w means agreement on every pair of events at index distance at most w,
> a span of w + 1 consecutive events — distributed as 4 at all 72 strict
> triples and all 5,184 concatenations, and 3, 4 and 5 at 4, 521 and 75 of
> the 600 driven-window schedules.  Below that width, crystallized
> identity does not transport: coherent families other than the identity
> exist, and the labelling the global test calls forced is not forced.
> Thread-hood — the requirement that ONE identification serve the whole
> history — is therefore a declaration a census makes and not a result it
> obtains, and this corpus states the amount: a coherence width of 3 to 5.
> Nothing here is measured about whether actors persist.  What is measured
> is how much persistence a census must assume before the identity it
> reports is forced."

**On the pin's question 4 ("state the presupposition as a measured
fact").**  Discharged, and correctly: `persistence.presupposition` and
G-PERSISTENCE-PRESUPPOSITION render it with the two counts and the derived
widths rather than as a reading.  §7's opening ("A global relabelling is
definable only on a persistent actor set") is a definitional remark, not a
claim, and it is immediately turned into the coordinate.  Accepted.

**On the pin's question 3 ("which grain does the law type its objects
at?").**  §6 answers narrowly and, apart from MINOR-1 and MINOR-13, well:
"the grain at which the history-stabilizer and the realizable group
coincide is the actor and site grain, not the carrier, and the carrier
answer is not the actor answer."  The answer is measured, the two tests
run at all three grains, the test-declaration duty is discharged
explicitly, and the OCC precedent is invoked without being borrowed from.
It must, however, carry MAJOR-4's window (C1+C3, C2 absent) and MINOR-1's
668 of 672.

---

# THE DUTIES — SWEPT

- **Test-declaration duty (AID MAJOR-1):** DISCHARGED.  TEST-RAW and
  TEST-REALIZABLE are both declared and both run at all three grains; the
  contrast is the claim and neither object is measured under one test
  only.  §6 states the duty in-paper.
- **Coin-order duty (#293):** DISCHARGED, and honestly.  Both declared
  orders run at every LEG-4 evaluation; 0 disagreements — and I confirm
  the fiber is inert not only on passes but on failures (378 failures at
  each order, same rows).  Published, not retired.  One gap: the pass
  count is published without its denominator (MAJOR-3).
- **Sentence-level referent binding (18 universes):** gate passes 5 of 5
  checked; I swept all 36 prose sentences carrying ≥ 2 numerals by hand.
  Cross-universe pairings found: MAJOR-2 (125 vs 2, LEG-2 universe joined
  to the admissibility universe by "precisely when"), MAJOR-1 (isotropy
  universe joined to the coherence-family universe by "so").  Gate
  coverage is narrower than the duty (MINOR-11).
- **Class/predicate binding (#295):** 38 rows, 0 mismatches, reproduced.
  The gate is sound; what it cannot catch is that five of the ten carrier
  rows recompute the SAME name from five different objects (MAJOR-5).
- **E-24 / counting-only:** 6 ratios, each windowed and stamped; the head's
  SCOPE field carries COUNTING-ONLY and the not-complete carrier window.
  No fraction is read as a frequency anywhere.  Accepted.
- **#267 paper-scanning:** 403 numerals and 97 spelled numerals scanned
  with 0 exemptions and 0 unbacked; 7 tables with headers, 42 rows; fences
  gated by multiset.  Totals cross-check: 39 sealed gates + 4 after the
  snapshot = 43 = 34 with a falsifier + 9 named without.  All reproduced.

---

# WHAT I CERTIFY

1. **Zero delivered computed numbers moved** under 128 independent
   recomputations and two full independent census re-runs.
2. **The head word is derived, not chosen.**  `head_law` is a genuine
   three-way selector over the two non-unique history SETS; STRATIFIED is
   returned because the sets are unequal (4 ⊊ 46, 42 carrier-only, 0
   actor-only), which I verified element by element.  The vocabulary is
   parsed from the pin's bytes and constrains the return.
3. **The two closed forms are real.**  LEG-1 = the six coset partitions of
   the translation subgroups, compared as a set and equal (I rebuilt the
   six and named them).  LEG-2 = refinement of the participation-signature
   partition, 0 mismatches on the sub-window — and it is the naming
   grain's own object, so the paper's "the decomposition question and the
   naming question meet here, in one object, on one leg" is exactly right.
4. **The AID §2 wall holds in the paper.**  Including the refused
   five-resonance, which is absent from paper, code comments and receipt
   alike.
5. **The atom word is genuinely at risk.**  Both substantive words are
   emitted by declared synthetic arenas through the real law, X4 being the
   decisive non-vacuous HOLDS (global stabilizer 1, adjacent families 1),
   and the paper says so.

**Repair order, in dependency order:** MAJOR-1 and MAJOR-3 first (they
change what §5 and §4 are about); then MAJOR-5 (new published rows);
then MAJOR-2, MAJOR-4, MAJOR-6, MAJOR-7; MAJOR-8 with the pin-ownership
note routed to the adjudicator; MINORs last.  No delivered number needs to
move; every repair above is a sentence, a scope, or a table the receipt
already knows or that my measurements supply verbatim.

*Candidate reading until adjudication.*
