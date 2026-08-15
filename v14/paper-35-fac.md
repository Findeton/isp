# FAC — which factorizations does the law admit?

*v14, the limit programme, paper 35. Instrument: `v14/code/fac_exact.py`;
artifacts `fac_output.txt` and `fac_receipt.json`. Exact arithmetic throughout:
Python integers and the ring Z[ω] carried as integer pairs, with the
lumpability test an exact comparison of integer maps; there is no float
anywhere, and an AST scan of the instrument together with a recursive type scan
of the receipt are gates. Pin: `v14/note-fac-pin.md`, sha256-12 11380265fcf3.*

---

**The verdict, in three segments, quoted exactly as the instrument emits it.**
Each segment is a sequence of `LABEL=VALUE` fields built from a declared field
spec whose every field names a receipt path; the second derivation route types
no copy of any of it and is described in §11.

```
FAC-DECOMPOSITION<THESIS=THE-LAW-ADMITS-MORE-THAN-ONE-FACTORIZATION-ONLY-WHERE-THE-HISTORY-REPEATS-A-PARALLEL-CLASS; HISTORIES=5,856; ACTOR-LATTICE=21,147; ACTOR-GRAIN-LAW-COMPATIBLE-PARTITIONS=6; ACTOR-GRAIN-UNIQUE-FACTORIZATION=5,852-OF-5,856-AT-THE-DIRECTIONWISE-IMAGE; ACTOR-GRAIN-UNIQUE-FACTORIZATION-AT-THE-PAIRWISE-IMAGE=5,854-OF-5,856; DIVISION-FORCED-UNDER-EITHER-IMAGE-AT-LEAST=5,852-OF-5,856; CARRIER-WINDOW=42,295; CARRIER-GRAIN-LAW-COMPATIBLE-PARTITIONS=10; CARRIER-GRAIN-UNIQUE-FACTORIZATION=5,810-OF-5,856; COIN-ORDER-DISAGREEMENTS=0>
```

```
FAC-GROUPOID<ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; ATOM-BREAKS=5,852-OF-5,856; COLLAPSE-THRESHOLDS=3,4,5; ARENA-GROUP-ORDER=108>
```

```
FAC-STRATIFIED<BY-GRAIN=ACTOR-5852-OF-5856-UNIQUE-AT-THE-DIRECTIONWISE-IMAGE-vs-CARRIER-5810-OF-5856-UNIQUE; ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; SCOPE=TWO-GRAINS-AS-DECLARED;COUNTS-ARE-COUNTING-ONLY;THE-CARRIER-WINDOW-IS-DECLARED-NOT-COMPLETE;NO-CLAIM-BEYOND-THE-MEASURED-COHERENCE-DEPTH>
```

Between delivery and adjudication every headline here is a **candidate
reading**.

---

## The short of it

Paper 33 asked whether history fixes the NAMES of nine actors already granted,
and found that it does. It said, in its own licensed words, that this leaves
the prior question untouched: which subsystems there are at all. That question
is this unit's, and it is asked in the only form a finite arena can answer it —
as a census.

A candidate factorization here is a PARTITION of a carrier, and the
identifications it induces are law-compatible exactly when the committed
structure survives them. Four things are committed and so four things must
descend: the link geometry, the division events, the record field, and the
coupled step. The criterion is fixed and digested before a single census row
runs.

Three results, and they do not agree with one another, which is the finding.

**At the actor grain the division is unique at all but a handful of
histories, and geometry and participation are what decide it.** Of the
complete lattice of partitions of the nine actors, the geometry leg alone cuts
the field to six — the geometry leg admits 6 of the 21,147 partitions of the
nine actors — and after the history leg the actor-grain factorization is unique
at 5,852 of 5,856 committed histories. The four exceptions are exactly the
histories that repeat one parallel class in every round; there the class
partition joins the discrete one and the inventory has two members, both named.
That count is taken at one of two declared ways of carrying an actor partition
to the carrier, and the other way moves it: §3 publishes both.

**At the carrier grain it is not unique so often.** The carrier — OCC's 27
co-division cells, the grain the excitations actually ride — admits more. On
the declared window the carrier-grain factorization is unique at 5,810 of 5,856
committed histories, and the histories where it is not are a strictly larger
set that contains the actor grain's four and adds 42 more. Same law, same
histories, two grains, two answers: the head word is `FAC-STRATIFIED` and it is
derived, not chosen. The stratification runs deeper than the counts: the LEGS
that bind are different at the two grains too, and §4 measures which.

**And the naming result does not survive the finer grain of identification at
all.** Paper 33's stabilizer quantifies over ONE relabelling required to fix
the whole history — which presupposes that an actor persists across it. Replace
that with a family of local identifications and a declared coherence relation,
and the rigidity evaporates: the global stabilizer is trivial and the
adjacent-coherence groupoid is not at 5,852 histories. It returns only when the
identification is required to cohere across several events at once, and the
depth at which it returns is a measured constant — the collapse thresholds this
corpus carries are 3, 4, 5, and they are WIDTHS in event index, not event
counts. Below that width crystallized identity does not transport. Thread-hood
is not something the census found; it is something the census assumed, in an
amount this unit can now quote.

---

## 1. The arena, the carrier, and what is being partitioned

The arena is the parents': AG(2,3) with nine sites, three declared link
directions of the four parallel classes, 280 groupings of the nine sites into
three triples of which 36 saturate, the 72 I7-STRICT triples at R = 3, the 276
G-FLAT quadruples and paper-21's 600-schedule driven window. Every one is
enumerated by this instrument's own constructor.

The carrier is OCC's. A cell is the unordered co-division pair {*x*, *x* + *l*},
and the instrument verifies this as a bijection rather than inheriting it: 27
cells against 27 pairs, two actors in each cell at all of them, six cells per
actor at all nine. So a partition of the cells IS a partition of the
co-division pairs, and the two grains this unit censuses are the nine actors
and the 27 cells.

The histories are the three committed corpora — 72 strict triples, their 5,184
ordered concatenations and the 600 window schedules, 5,856 in all, of 9, 12 and
18 events. The record is n_l(x), the number of division events containing both
the actor at x and the actor at x + l; the dynamics is paper-20's coupled step,
and because paper-20 declares the coin order a verdict-relevant fiber, both
orders are carried through every evaluation below.

**The corpus is a MULTISET, and every count in this unit is a count over its
SLOTS**, because the 5,856 committed histories are slots carrying 5,784
distinct histories: the strict triples and the concatenations are
duplicate-free, and the driven window's 600 schedules yield 528 distinct
histories, 519 of them once and 9 of them nine times each.

| corpus | slots | distinct histories |
|---|---|---|
| C1 | 72 | 72 |
| C2 | 5,184 | 5,184 |
| C3 | 600 | 528 |

The conversion matters in exactly one place below and it is made there: the
dynamics leg's failures number 378 over the slots and 306 over the distinct
histories, and the difference is the 72 duplicate slots, one failure each.

## 2. The criterion, and why it has four legs

A partition π of a carrier induces identifications: the members of a block
become one object. The partition is LAW-COMPATIBLE at a history exactly when
the committed structure DESCENDS along those identifications — when the
quotient still carries it. Four legs, one per committed structure, each a
per-object predicate:

- **LEG-1 GEOMETRY.** The link (at the actor grain) or the shift (at the
  carrier grain) descends to the blocks.
- **LEG-2 HISTORY.** Every division event is a union of blocks, so it is still
  a well-defined subset after the identification.
- **LEG-3 RECORD.** The record field is block-constant, so n descends to a
  field on the quotient's cells.
- **LEG-4 DYNAMICS.** The coupled step is exactly LUMPABLE for the induced
  carrier partition: the per-exponent integer tallies of the column's entries
  falling into each block agree, cell by cell within a block, at both declared
  coin orders.

That last statement is the IMPLEMENTED predicate, and it is strictly finer than
the block sums the quotient criterion is usually stated with, because
1 + ω + ω² = 0 identifies profiles the tallies distinguish. Both are
implemented and compared on every evaluation of both censuses below: 24,354
comparisons, 0 disagreements. The finer predicate is the one that ran; on this
corpus it is the same predicate.

**LEG-4 is a predicate on a CARRIER partition, so an actor partition reaches it
through a map — and that map is a declared free item.** The carrier window
below names two of them: the DIRECTIONWISE image, which identifies (x, l) with
(y, l) whenever x and y are identified, and the PAIRWISE image, which
identifies two cells when their unordered pairs of blocks agree — the
identification the carrier's own typing suggests, since a cell IS a
co-division pair. The image is therefore a parameter of the criterion, exactly
as the link set is a parameter of LEG-1, and both members are run entire. **The
induced-image fiber is not inert**, and §3 publishes both censuses side by side.

The criterion's eleven functions are located by AST in the instrument's own
source, digested, and gated at a point in the run where no admissible set has
yet been computed. Every free name they reference is then required to lie in a
declared WHITELIST of 26 allowed names — the arena's constants, the folding
helpers, the criterion's own members and the builtins it uses — so no leg can
reach the answer it is deciding by an alias, by a `globals()` lookup or by a
default argument, none of which a list of forbidden spellings can stop. The
whitelist is part of the digest, so widening it moves the digest: the
criterion's combined digest is fde02cc2ed0c.

Two legs have closed forms, and both are measured against them rather than
trusted. LEG-1 at the actor grain admits exactly the coset partitions of the
subgroups of AG(2,3)'s translation group — compared as a SET of partitions, not
as a count, and equal. LEG-2 admits exactly the partitions that refine the
participation-signature partition; and that is the naming grain's own object,
the partition whose Young subgroup is paper 33's stabilizer. The decomposition
question and the naming question meet here, in one object, on one leg.

| grain | candidate set | geometry-leg survivors |
|---|---|---|
| actor | 21,147 | 6 |
| carrier | 42,295 | 10 |

The candidate sets are declared. The actor lattice is COMPLETE: every partition
of the nine actors, no cap and no sampling. The carrier's is not and cannot be
— the declared carrier window carries 42,295 partitions and the geometry leg
admits 10 of them, against a Bell number of 545,717,047,936,059,989,389 for the
27 cells. The window is named in-string: the directionwise image of every actor
partition, the pairwise image of every actor partition, and 12 OCC-typed
natural strata — discrete, trivial, by-direction, by-anchor-site, by-AG-line,
the shift orbits and the six translation-subgroup orbit partitions — which
deduplicate to nine distinct partitions. Everything outside the window is
disclosed as outside it, and §5 prices what the window does.

## 3. The census

| grain | unique | non-unique | histories |
|---|---|---|---|
| actor | 5,852 | 4 | 5,856 |
| carrier | 5,810 | 46 | 5,856 |

The discrete partition — the nine-fold division itself — is admissible at every
history, checked history by history, so the count is never zero and the
question is always whether anything JOINS it. At the actor grain something
joins it exactly four times, at the four schedules that use a single parallel
class in all four rounds, and the instrument names what joins.

**Both induced images, side by side.** The actor-grain census is taken twice,
changing nothing but the map that carries an actor partition to the carrier:

| induced image | unique | non-unique | histories | class partitions that join the discrete one |
|---|---|---|---|---|
| DIRECTIONWISE | 5,852 | 4 | 5,856 | ANT, COL, DIA, ROW |
| PAIRWISE | 5,854 | 2 | 5,856 | COL, ROW |

The two censuses do not agree, and both are published: at the directionwise
image the actor grain is unique at 5,852, and at the pairwise image the
actor-grain factorization is unique at 5,854 of 5,856 committed histories. The
mechanism is exact. The DIA and ANT class partitions pass the geometry, history
and record legs under both images and fail LEG-4 at both declared coin orders
under the pairwise one, so they leave the inventory and the ROW and COL class
partitions remain. Every actor-grain count in this unit therefore carries the
image it was taken at, in the head's own fields, and the robust reading is the
minimum of the two: **under either image the division is forced at at least
5,852 of 5,856 committed histories** — the fiber moves only which degenerate
histories tie. The verdict word does not move with it: the two grains'
non-unique sets are unequal under both images, so `FAC-STRATIFIED` is returned
by both.

**The thesis field is a one-way conditional and is measured in both
directions.** Every history at which the criterion admits more than one
factorization repeats a parallel class — all 4 at the actor grain and all 46 at
the carrier grain, 0 exceptions — and 348 of the 5,856 committed histories
repeat a parallel class, so the condition is necessary and far from sufficient.
That is what the head's thesis field asserts and no more. At the actor grain a
tight characterization IS available and is measured in both directions: the 4
non-unique histories are exactly the 4 that use one parallel class in EVERY
round, and the partition that joins the discrete one is that class. At the
carrier grain no such biconditional holds: 4 of the 46 are class-constant and
42 are not.

What that tight characterization is NOT is a statement about coarsenings in
general. Among the six partitions the geometry leg admits, the one that joins
the discrete partition is admitted by the history leg and by no further leg: at
each of the four non-unique histories the class partition is the unique
non-discrete geometry survivor whose blocks are unions of every event. That is
a statement about those six. Across the whole lattice the two predicates come
apart, and the receipt carries both counts: at each of those four histories 125
partitions of the nine actors pass the history leg while 2 are admissible, so
"the history never distinguishes the actors a coarsening would merge" and
"admissible" are not the same predicate and this unit does not write them as
one.

The two grains are then compared AS SETS OF HISTORIES, not as counts. The
actor grain's four are contained in the carrier grain's 46; 42 histories are
non-unique at the carrier and unique at the actor grain, and 0 the other way
round. A comparison of the two counts alone would have left the direction
unmeasured.

The coin-order fiber is discharged by running both members rather than choosing
one. Every LEG-4 evaluation is performed at G·D and at D·G — 12,177 evaluations
under each order, of which 11,799 pass and 378 fail — and the two declared coin
orders disagree on 0 census rows, on the failures as on the passes. The fiber
is INERT on every row of this census; that is a measurement, and it is
published beside the counts rather than used to retire the axis. The pass count
is published with its denominator on purpose: LEG-4 is evaluated only on rows
the first three legs admit, so a pass count alone cannot say whether the leg
ever fired.

## 4. Which leg binds, and which does not

Running the complete actor lattice against a declared sub-window — the 72
strict-triple histories plus every history the census found non-unique, 76 in
all, with the remaining 5,780 named as the complement — separates the first
three legs:

- LEG-1 admits 6 partitions at every history in the sub-window.
- LEG-2 admits 1 at the strict triples and 125 at the four non-unique ones, and
  its closed form reproduces the enumeration with 0 mismatches.
- LEG-3 admits all 21,147.

The last of these is a fact about this corpus and it is stated as one: the
record field is site-constant at 5,856 of 5,856 committed histories, so LEG-3
cannot separate anything here. It is **non-binding** on the committed corpus,
which is not the same as vacuous, and the difference is measured on the control
arm rather than asserted: on the declared synthetic histories the record leg
binds at three of the five, cutting the lattice to 1,015 partitions at
X1-ONE-DIVISION-EVENT, 125 at X3-ROW-MULTIPLICITIES-CONGRUENT-MOD-THREE and 104
at X4-THE-OVERLAPPING-CHAIN.

**The fourth leg is separated too, and the answer is itself stratified by
grain.** LEG-4 is a predicate on the induced carrier partition, so it is
measured at both grains over the whole corpus, twice: by counting its failures
among the rows the earlier legs admit, and by re-taking each census with the
leg DELETED.

| grain | LEG-3 failures | LEG-4 evaluations | LEG-4 failures | unique with LEG-4 | unique without LEG-4 |
|---|---|---|---|---|---|
| actor | 0 | 5,860 | 0 | 5,852 | 5,852 |
| carrier | 0 | 6,317 | 378 | 5,810 | 5,478 |

So: the dynamics leg removes no partition the other legs admit at the actor
grain and removes 378 partition-history rows at the carrier grain. At the actor
grain the cardinality profile is unchanged when LEG-4 is deleted, so by this
unit's own rule — a leg that never fails on a corpus is declared non-binding ON
THAT CORPUS — the dynamics leg is non-binding at the actor grain, as the record
leg is at both. **The actor-grain headline, the thesis, and the FORCED and
DECLARED control words are therefore a geometry-plus-history result:
dynamics-blind, on this corpus, at that grain.** At the carrier grain the
dynamics leg is the one that separates: it rejects 378 of the rows the first
three legs pass — 306 of them at distinct histories — and deleting it moves the
carrier census from 5,810 unique to 5,478, with the cardinality profile going
from one, two, three and nine admissible factorizations to one, two, three,
four and ten. Since the STRATIFIED verdict is produced by the carrier grain's
42, the coupled step is load-bearing exactly where the head word comes from.
Which leg binds is itself grain-dependent, and that is a stratification of
MECHANISM rather than of counts.

The record-versus-dynamics wedge is measured too, at both grains and in the
census's own loop rather than typed. The coin reads the record only modulo
three, so a partition merging sites whose records differ by a multiple of three
passes LEG-4 and fails LEG-3. That wedge fires 0 times at the actor grain on the
committed corpus — where it cannot fire, since the record is site-constant — and
44 times at the carrier grain, every one of them on a row the history leg has
already removed, so it moves no admissibility verdict. On the synthetic history
built to carry it the wedge fires 4 times. The record leg is therefore a real
constraint that this corpus happens not to exercise.

## 5. The carrier grain's inventory, enumerated and priced

The head word is STRATIFIED because one grain admits more than one
factorization, so that grain's "more than one" is the thing to price.

| admissible factorizations | histories |
|---|---|
| 1 | 5,810 |
| 2 | 15 |
| 3 | 30 |
| 9 | 1 |

What joins the discrete cell partition is always a coarsening across sites
within a direction. At the 42 histories that are non-unique at the carrier and
unique at the actor grain the admissible sets fall into exactly three profiles,
14 histories each: {discrete, a 9-block, a 6-block}, {discrete, a different
9-block, a different 6-block}, and {discrete, a third 9-block}. The nine-block
partitions cut the 27 cells into nine blocks of three; the six-block ones into
three blocks of six and three of three.

**The single nine-fold row is the ANT-constant schedule** — corpus index 5,511,
the same history that carries the actor grain's ANT inventory row. Its nine
admissible factorizations include the three-block partition and **the one-block
partition of the whole carrier**: at that history alone the committed structure
descends to a quotient with a single object. That is the most consequential
single row of the census and it is published rather than left in the tail of a
distribution.

The ten geometry-leg survivors carry only five distinct block-shape names —
one name denotes five different partitions and another denotes two — so the
receipt lists each survivor by its own BLOCK PARTITION, indexed, with its shape
and the window families that produced it. A name that denotes five objects is
not a referent, and the inventory is keyed by the objects.

Finally, the window is priced. Running the carrier census on each declared
sub-family of the window, and on the window itself:

| declared sub-window | geometry-leg survivors | carrier-grain unique |
|---|---|---|
| THE-STRATA | 8 | 5,810 |
| DIRECTIONWISE-IMAGES | 6 | 5,810 |
| PAIRWISE-IMAGES | 4 | 5,825 |
| THE-DECLARED-WINDOW | 10 | 5,810 |

Three of the four sub-windows return the same headline count, so 5,810 is far
more robust than the window's declared status alone would license. The
cardinality profile is not: it is window-specific, and it is stamped as such.

## 6. The groupoid crystallization

The global grain quantifies over one permutation of a persistent actor set and
asks it to fix every event. The groupoid grain replaces that with a family of
local identifications and a declared coherence relation on the times.

**Two objects sit in this section and neither stands for the other.**

THE COHERENCE CENSUS. A local identification at event *t* is any bijection of
that event's three-actor footprint to itself — all six, with no structure
condition — and a coherent family is a choice of one per event agreeing, on
every pair of times the declared relation names, wherever the two footprints
meet. This is the groupoid-grain relaxation of the global test, which likewise
quantifies over the whole symmetric group; it is what makes the complete
relation return the global stabilizer. The empty relation therefore returns 6^T
exactly — 10,077,696 at every strict triple, 2,176,782,336 at every
driven-window schedule and 101,559,956,668,416 at every concatenation — and the
instrument checks that identity at every history of the corpus, with 0
mismatches.

THE ARROW GROUPOID, measured separately. Its objects are the events, an arrow
is a footprint bijection preserving the internal co-division cells with their
declared directions, and on the declared sub-window of 672 histories — all 72
strict triples and all 600 driven-window schedules — its isotropy orders are 1,
3 and 6 and its connected components run from 1 to 5. Its free product is a
different size at every history: 19,683 at the first strict triple and 531,441
at the first driven-window schedule, against the ladder's 10,077,696 and
2,176,782,336 there. No ladder row counts arrows. Restricting the families to
the arrows would be a different census, and it would not return the global
stabilizer at the complete relation, because a stabilizer element restricts to
an ARBITRARY permutation of an event, not to a direction-preserving one.

The ladder itself:

| corpus | coherence relation | distinct values | minimum | maximum | histories |
|---|---|---|---|---|---|
| C1 | R-ADJACENT | 1 | 124,416 | 124,416 | 72 |
| C1 | R-COMPLETE | 1 | 1 | 1 | 72 |
| C1 | R-EMPTY | 1 | 10,077,696 | 10,077,696 | 72 |
| C1 | R-ROUND | 1 | 10,077,696 | 10,077,696 | 72 |
| C1 | R-WINDOW-2 | 2 | 144 | 288 | 72 |
| C1 | R-WINDOW-3 | 1 | 4 | 4 | 72 |
| C2 | R-ADJACENT | 3 | 859,963,392 | 15,479,341,056 | 5,184 |
| C2 | R-COMPLETE | 1 | 1 | 1 | 5,184 |
| C2 | R-EMPTY | 1 | 101,559,956,668,416 | 101,559,956,668,416 | 5,184 |
| C2 | R-ROUND | 1 | 101,559,956,668,416 | 101,559,956,668,416 | 5,184 |
| C2 | R-WINDOW-2 | 13 | 144 | 41,472 | 5,184 |
| C2 | R-WINDOW-3 | 2 | 4 | 8 | 5,184 |
| C3 | R-ADJACENT | 7 | 1,492,992 | 2,176,782,336 | 600 |
| C3 | R-COMPLETE | 2 | 1 | 216 | 600 |
| C3 | R-EMPTY | 1 | 2,176,782,336 | 2,176,782,336 | 600 |
| C3 | R-ROUND | 1 | 2,176,782,336 | 2,176,782,336 | 600 |
| C3 | R-WINDOW-2 | 22 | 144 | 2,176,782,336 | 600 |
| C3 | R-WINDOW-3 | 9 | 2 | 216 | 600 |

Three facts sit in that table.

**The complete relation is the group, and that is a theorem of the
construction.** A family coherent on every pair determines one map on the
actors restricting to a permutation of every event, and conversely; since each
round partitions the nine actors, that map is a bijection preserving every
event setwise, which is a stabilizer element. So the equality cannot fail on a
history of this shape. The instrument nevertheless computes both sides by
routes that share no code — a backtracking enumeration against the Young order
of the participation signature — and the complete coherence relation returns
the global stabilizer at 5,856 of 5,856 histories. That agreement is a CODE
CHECK, and it is reported as one.

**The atom theorem does not survive the weaker relations.** At every history
the global stabilizer is trivial exactly when the actor-grain factorization is
unique and exactly when the atom breaks — three predicates, one split of the
corpus into 5,852 and 4, verified element by element. So at the actor grain
this unit's answer is extensionally the naming census's; what it adds is the
carrier grain's 42 and the groupoid grain. And at the groupoid grain the answer
changes: the global stabilizer is trivial and the adjacent-coherence groupoid
is not at 5,852 histories, where the surviving families number 124,416 at every
strict triple and run from 859,963,392 to 15,479,341,056 at the concatenations.
The reason is visible in the R-ROUND row: within a round the three division
events are pairwise DISJOINT — which `G-CORPORA-SHAPE` forces, since each round
partitions the nine actors — so a round-local coherence requirement is no
requirement at all and returns the free product exactly. Group-level triviality
does not imply groupoid-level rigidity here, and the word this unit emits,
`FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN`, is computed from that count.

**The tabulated ladder stops below the collapse it reports.** The widest
sliding window in the table is R-WINDOW-3, and 5,852 histories have a collapse
width above it — 5,256 of them in C1 and C2, where the width is 4 at every
history. The widths in §8 are not read off this table: they come from an
uncapped upward search, and the table is the ladder's shape rather than its
answer.

## 7. The grain triangle

The test-declaration duty is discharged by running BOTH declared tests at ALL
THREE grains. TEST-RAW takes the stabilizer inside the grain's full symmetric
group. TEST-REALIZABLE intersects it with the transformations the arena itself
realizes — the affine maps of AG(2,3) that permute the declared link
directions, acting coherently on sites and on cells; the arena's own
automorphism group has order 108.

The measurement runs on the declared sub-window of 672 histories — all 72
strict triples and all 600 driven-window schedules — because a concatenation's
stabilizer is the intersection of its parts' and its arrow groupoid is their
disjoint union, so C2 carries no independent row. The complement is named, and
it is the larger part of the corpus: all of C2 — 5,184 of 5,856 slots — is
outside this window, and §10 repeats the limit.

| corpus | TEST-RAW at ACTOR-S9 | TEST-RAW at CARRIER-S27 | TEST-REALIZABLE at SITE | TEST-REALIZABLE at CARRIER | histories |
|---|---|---|---|---|---|
| C1 | 1 | 10,077,696 | 1 | 1 | 72 |
| C3 | 1 | 512 | 1 | 1 | 48 |
| C3 | 1 | 13,824 | 1 | 1 | 216 |
| C3 | 1 | 10,077,696 | 1 | 1 | 140 |
| C3 | 1 | 16,930,529,280 | 1 | 1 | 150 |
| C3 | 1 | 1,382,912,720,437,248,000 | 1 | 6 | 42 |
| C3 | 216 | 1,382,912,720,437,248,000 | 6 | 6 | 3 |
| C3 | 216 | 10,888,869,450,418,352,160,768,000,000 | 18 | 108 | 1 |

The Young-order route is checked against an explicit filtration of the
symmetric group at 24 histories, with 0 mismatches.

The reading the two tests together license is narrow and worth stating exactly.
The raw carrier stabilizer is nontrivial at every row, from 512 upward, and the
largest raw carrier stabilizer this corpus carries is
10,888,869,450,418,352,160,768,000,000, which is 27 factorial: at that one
history the raw carrier test is completely vacuous, the whole symmetric group
on the cells stabilizes the history — its events deposit no declared cell, so
every cell carries the empty signature — and the realizable stabilizer there is
the arena's entire order-108 group. A labelling of the 27 cells is not fixed by
the history in the way a labelling of the nine actors is. But almost none of
that freedom is a symmetry of anything the arena has: the two tests agree at
the actor grain at 668 of 672 rows and at the carrier grain at 0 of 672. The
carrier's excess is freedom to permute cells in ways no transformation in the
arena's declared automorphism group of order 108 realizes, which is a statement
about the size of S₂₇ as much as about the law. What the triangle establishes
is the shape OCC's precedent predicts and no more: the grain at which the
history-stabilizer and the realizable group coincide is the actor and site
grain — at 668 of the 672 rows of the declared sub-window, and at 0 of 672 at
the carrier — and the carrier answer is not the actor answer.

## 8. The persistence presupposition, and transport

A global relabelling is definable only on a persistent actor set. Paper 33's
effectus review says so in its own words, and this unit turns the observation
into a coordinate: the coherence relation of the groupoid grain IS how much
persistence a census assumes.

The global grain asks one permutation of a persistent actor set to fix every
event. Replace it with a family of local identifications — any of the six
permutations of each event's footprint, one per event — required to agree only
where a declared coherence relation on the times says they must, and the answer
moves: identity is forced at the complete relation at 5,852 histories and at
the adjacent relation at 0 of them. The least coherence WIDTH at which the two
meet is derived per history by searching upward without a cap, and it is 3, 4
or 5. A width of w means agreement on every pair of events at index distance at
most w, which is a span of w + 1 consecutive events; the width, not the span,
is the measured constant. It is 4 at every strict triple and at every
concatenation; across the driven window it is 3 at 4 of the 600 schedules, 4 at
521 of them and 5 at 75.

Below that width, crystallized identity **does not transport**: coherent
families other than the identity exist, and the labelling the global test calls
forced is not forced. Thread-hood — the requirement that ONE identification
serve the whole history — is therefore a declaration a census makes and not a
result it obtains, and this corpus states the amount: a coherence width of 3 to
5, which is agreement across spans of four to six consecutive events. Nothing
here is measured about whether actors persist. What is measured is how much
persistence a census must assume before the identity it reports is forced.

The result is reported at every rung the corpus carries, from that rung's own
histories rather than from the corpus aggregate. At R = 3 the actor grain is
unique at all 72 histories under both images, the atom breaks at all 72, and
the width is 4. At R = 4 the actor grain is unique at 596 of 600 at the
directionwise image and at 598 of 600 at the pairwise one, the carrier grain at
554, the atom breaks at 596, and the widths are 3, 4 and 5. At R = 6 the actor
grain is unique at all 5,184 under both images, the atom breaks at all 5,184,
and the width is 4. The break coincides with the actor grain's uniqueness rung
by rung.

**R = 6 is not an independent rung, and is stamped so.** C2 is the set of
ordered pairs of C1 histories; a concatenation's history-leg survivors are the
intersection of its parts' and its stabilizer is the intersection of its parts'
stabilizers. Measured at the parts: all 72 strict triples carry exactly one
history-leg survivor and a trivial stabilizer, so uniqueness and trivial
stabilizer at all 5,184 concatenations follow by theorem and are checked here
rather than discovered. What R = 6 does measure independently is the
adjacent-relation family count, which runs from 859,963,392 to 15,479,341,056,
and the collapse width, which is 4. PER-L closed the L-ladder transport by
theorem and PER-R places its own successor at R = 8, so nothing is claimed here
beyond the rungs measured.

## 9. The control arm

Every pre-registered outcome word must be shown reachable at the declared
arena, and none of the rows below is forged: each is a genuine evaluation of
the SAME criterion and the SAME head law on a declared datum.

| declared arena | histories | actor non-unique | carrier non-unique | head word |
|---|---|---|---|---|
| CTRL-C1-THE-STRICT-TRIPLES | 72 | 0 | 0 | FAC-FACTORIZATION-FORCED |
| CTRL-THE-NON-UNIQUE-HISTORIES | 4 | 4 | 4 | FAC-FACTORIZATION-DECLARED |
| CTRL-C3-THE-DRIVEN-WINDOW | 600 | 4 | 46 | FAC-STRATIFIED |
| CTRL-THE-WHOLE-CORPUS | 5,856 | 4 | 46 | FAC-STRATIFIED |

Three different words on three declared arenas, from one law: the head law
returns FAC-FACTORIZATION-FORCED on the strict triples,
FAC-FACTORIZATION-DECLARED on the four class-repeating histories and
FAC-STRATIFIED on the whole corpus. On the strict triples both grains are
uniformly unique and the head law returns FAC-FACTORIZATION-FORCED; on the four
class-repeating histories both grains are non-unique on the SAME histories and
the inventory is named; on the driven window and on the whole corpus the grains
disagree.

**What was actually at stake at THIS corpus is narrower than that, and the
unit owns it.** The pin's feasibility line for the forced word argued against
the arena's abstract ranges. Argued against the committed corpus it is
narrower: the driven window enumerates all 256 class quadruples by
construction, so the four class-constant schedules are in the corpus by
construction; at each of them the matching class partition is admitted by the
geometry leg's closed form and by the history leg's closed form, and the record
leg cannot fire because the record is site-constant everywhere. Only a
dynamics-leg failure at those four could have returned the forced word at this
corpus — and the dynamics leg fails 0 times in 5,860 actor-grain evaluations at
the directionwise image. What the run decided at the corpus was DECLARED
against STRATIFIED, and it turned on the 42 carrier-only histories, which is a
genuine dynamics-leg measurement. The three-word control arm is evidence about
the LAW; this paragraph is the evidence about the CORPUS, and the #299
engraving as sharpened asks for the second.

| synthetic history | events | distinct record rows | LEG-3 passers | wedge | global stabilizer | adjacent families | atom word | atom row |
|---|---|---|---|---|---|---|---|---|
| X1-ONE-DIVISION-EVENT | 1 | 2 | 1,015 | 0 | 4,320 | 6 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN | VACUOUS-STABILIZER-NONTRIVIAL |
| X2-ONE-FULL-ROW-ROUND | 3 | 1 | 21,147 | 0 | 216 | 216 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN | VACUOUS-STABILIZER-NONTRIVIAL |
| X3-ROW-MULTIPLICITIES-CONGRUENT-MOD-THREE | 12 | 3 | 125 | 4 | 216 | 216 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN | VACUOUS-STABILIZER-NONTRIVIAL |
| X4-THE-OVERLAPPING-CHAIN | 7 | 4 | 104 | 0 | 1 | 1 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN | DECISIVE |
| X5-A-ROW-ROUND-THEN-A-COLUMN-ROUND | 6 | 1 | 21,147 | 0 | 1 | 5,184 | FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN | DECISIVE |

Both atom words are emitted by the same law on declared data, and the last
column says which rows can carry the question. The atom question is whether a
TRIVIAL-STABILIZER history stays rigid at a weaker coherence, so at the three
rows whose global stabilizer is already nontrivial it is not posed: the law
returns its other word for want of a candidate, and those rows are stamped
vacuous. X4 is the decisive one: a chain of events overlapping in two actors at
a time forces the identification already at the adjacent relation with a
trivial global stabilizer, so a corpus of such histories would have returned
the other word. The corpus does not consist of such histories, and that — not
the law — is why the atom breaks here.

Four of the pin's five outcome families are reached by a declared arena. The
fifth is the blocked family, and it is reached only by EVALUATING the atom law
at a state the ladder gate excludes at 5,856 of 5,856 histories, which is what
an instrument-fault word is for; the receipt lists arena-reached and
law-evaluated words separately rather than in one set.

| synthetic arena | declared links | geometry-leg survivors |
|---|---|---|
| L1-ONE-DIRECTION | 1 | 42 |
| L2-TWO-DIRECTIONS | 2 | 6 |
| L4-EVERY-DIRECTION | 4 | 6 |

The geometry leg takes its link set as a parameter, so a synthetic arena runs
through the same predicate. With one declared direction the leg admits 42
partitions; with two or four it admits 6. The rigidity of §2 is therefore a
property of the declared arena and not of the code, and it saturates as soon as
the declared directions generate the translation group.

## 10. What this does not say

Every count in this unit is a count over a declared window and is stamped
COUNTING-ONLY. This unit declares no measure on partition lattices, so none of
its fractions may be read as a frequency or a likelihood; the 14 published
ratios each carry the window their numerator and their denominator both range
over.

The census ranges over PARTITIONS of two declared carriers. A factorization
that is not a partition of either — a change of basis on the coupled step's
state space, for instance — is outside the question as posed, and the unit does
not speak to it. The carrier window is declared and is not the carrier's whole
lattice. The corpus is the parents' corpus, it is a multiset of 5,856 slots
carrying 5,784 distinct histories, and the rungs are R = 3, R = 4 and R = 6, of
which R = 6 is theorem-forced by R = 3. The stabilizer, arrow and
raw-versus-realizable measurements of §7 run on 672 of those slots, with all of
C2 — 5,184 histories — outside that window.

No sentence of this unit assigns identity to one kind of thing and chart to
another; that reading was refused on the record by paper 33's adjudication and
is a wall this instrument scans this paper for. Nothing here is a claim about
what actors are. The unit measures which decompositions the committed law
admits, at which grain, under which coherence, and reports that the answer
depends on all three.

## 11. The instrument

Ten committed files are read as sources at pinned digests, plus this paper as
the object under test; no other repository state is read and no subprocess is
invoked, so the run is correct off-tree and with no version control present. 13
verbatim anchors are matched in their sources' bytes, each named with the gate
that consumes it, and every gate NAMED anywhere in the receipt — by an anchor
as its consumer, by a seal as the gate that established it, or by a falsifier
as the gate it must die at — is required to EXIST, since a name that is merely
non-empty is not a consumer. The pre-registered outcome vocabulary is PARSED
OUT OF THE PIN'S OWN BYTES — 5 strings reduced to 5 families — and the head law
is required to return words from that set and from no other.

The head is derived twice by routes that share no dispatcher and no census
loop. The second calls neither admissibility dispatcher and reads none of the
first's rows: it rebuilds every admissible set from the raw leg predicates,
recounts the atom breaks from the coherence relation directly rather than from
the ladder's cache, re-derives the complete-relation comparison from its own
enumeration rather than carrying it in as a literal, and re-applies both laws
to its own numbers. What the two share is the four leg predicates themselves,
which are the object under test and are de-twinned by their own closed-form
gates rather than by duplication; the two agree on the head word, the atom word
and all four counts.

20 closing gates are declared, 6 of which necessarily run after the ledger
snapshot, and 47 seals are taken at gate time over a manifest required to be
total. The totality is computed from the SERIALIZED
PAYLOAD rather than from the in-memory object, so a receipt key forged after
the manifest is assembled is caught rather than published unsealed; the
integrity gate reads the staged bytes back and compares them with the gate-time
seal BEFORE `os.replace` promotes anything, and the staging files are removed
on refusal. The transcript is sealed WHOLE, and its `[PASS]` lines are
reconciled against the sealed gate ledger as multisets, so a forged pass line
for a gate that never ran fails.

7 windows are declared with their measured bounds and none of them publishes a
placeholder; the three that are sub-windows of the corpus publish their
complements. 6 walls carrying 20 banned assertive sentences are scanned against
this paper's own bytes — the leg the wall is owed — and the falsifier for that
gate plants every banned sentence into exactly that text; the needles are
listed variants under a strong normalisation and not an invariance under
paraphrase, so the wall is a check on the sentences it names and not a
guarantee about every rephrasing of them. 54 falsifiers are declared, each
naming the gate it must die at and each
carrying a source fragment located in the instrument by AST and matched against
the statement that actually carries the hook, so a description-inverted
falsifier cannot pass; 42 of the gates carry one and the remaining 9 are named
in the receipt, guarded by construction or by argument rather than by a mutant.

20 claim sentences are rendered from the receipt and matched against this
paper's bytes — the criterion's own digest and this paper's stated pin digest
among them, so a provenance token quoted here cannot drift from the one this
run measured. Every table above is
rendered from the receipt with its HEADERS INCLUDED — 12 tables, 57 data rows
and 12 header rows — and the binding runs BOTH WAYS: the multiset of this
paper's markdown table rows must equal the multiset rendered, so a forged
surplus row, a restated table with its headers exchanged and a fourth verdict
fence all fail. Every printed class-word is recomputed from its predicate.
Every numeral is scanned — prose, tables, inline code spans and the fenced
verdict blocks alike — against the run's own registry, with the scan's totality
checked by arithmetic; spelled numerals are scanned on the same terms, with
adjacent number-words parsed as COMPOUNDS so that a compound built from backed
atoms cannot ride in, and with a totality reference of its own. The normaliser
that feeds those scans is itself gated: the paper's numeral multiset before and
after canonization must be equal, on a text carrying a declared fixture of the
pathology, because a markdown stripper that eats a line-initial numeral hides
the relation that numeral belonged to.

Every relation of the forms `N of M` and `N against M` is resolved against the
receipt and both members are required to be carried by one common member of the
10 DECLARED QUANTITY AXES — 171 receipt paths in all, each axis counting one
kind of thing, because a top-level receipt key that carries a history axis and
a partition axis at once will bind a false relation between them. The number of
relations the scan saw is compared with the number this paper's own bytes
carry. 9 polarity axes are checked in both directions, one of them over the
paper's prose alone so that a word which is legitimate DATA in a table cannot
mask its own inversion in a sentence, and an axis whose asserted form has
vanished fails too.

---

```
FAC-DECOMPOSITION<THESIS=THE-LAW-ADMITS-MORE-THAN-ONE-FACTORIZATION-ONLY-WHERE-THE-HISTORY-REPEATS-A-PARALLEL-CLASS; HISTORIES=5,856; ACTOR-LATTICE=21,147; ACTOR-GRAIN-LAW-COMPATIBLE-PARTITIONS=6; ACTOR-GRAIN-UNIQUE-FACTORIZATION=5,852-OF-5,856-AT-THE-DIRECTIONWISE-IMAGE; ACTOR-GRAIN-UNIQUE-FACTORIZATION-AT-THE-PAIRWISE-IMAGE=5,854-OF-5,856; DIVISION-FORCED-UNDER-EITHER-IMAGE-AT-LEAST=5,852-OF-5,856; CARRIER-WINDOW=42,295; CARRIER-GRAIN-LAW-COMPATIBLE-PARTITIONS=10; CARRIER-GRAIN-UNIQUE-FACTORIZATION=5,810-OF-5,856; COIN-ORDER-DISAGREEMENTS=0>
```

```
FAC-GROUPOID<ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; ATOM-BREAKS=5,852-OF-5,856; COLLAPSE-THRESHOLDS=3,4,5; ARENA-GROUP-ORDER=108>
```

```
FAC-STRATIFIED<BY-GRAIN=ACTOR-5852-OF-5856-UNIQUE-AT-THE-DIRECTIONWISE-IMAGE-vs-CARRIER-5810-OF-5856-UNIQUE; ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; SCOPE=TWO-GRAINS-AS-DECLARED;COUNTS-ARE-COUNTING-ONLY;THE-CARRIER-WINDOW-IS-DECLARED-NOT-COMPLETE;NO-CLAIM-BEYOND-THE-MEASURED-COHERENCE-DEPTH>
```
