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
no copy of any of it and is described in §10.

```
FAC-DECOMPOSITION<THESIS=THE-LAW-ADMITS-MORE-THAN-ONE-FACTORIZATION-ONLY-WHERE-THE-HISTORY-REPEATS-A-PARALLEL-CLASS; HISTORIES=5,856; ACTOR-LATTICE=21,147; ACTOR-GRAIN-LAW-COMPATIBLE-PARTITIONS=6; ACTOR-GRAIN-UNIQUE-FACTORIZATION=5,852-OF-5,856; CARRIER-WINDOW=42,295; CARRIER-GRAIN-LAW-COMPATIBLE-PARTITIONS=10; CARRIER-GRAIN-UNIQUE-FACTORIZATION=5,810-OF-5,856; COIN-ORDER-DISAGREEMENTS=0>
```

```
FAC-GROUPOID<ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; ATOM-BREAKS=5,852-OF-5,856; COLLAPSE-THRESHOLDS=3,4,5; ARENA-GROUP-ORDER=108>
```

```
FAC-STRATIFIED<BY-GRAIN=ACTOR-5852-OF-5856-UNIQUE-vs-CARRIER-5810-OF-5856-UNIQUE; ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; SCOPE=TWO-GRAINS-AS-DECLARED;COUNTS-ARE-COUNTING-ONLY;THE-CARRIER-WINDOW-IS-DECLARED-NOT-COMPLETE;NO-CLAIM-BEYOND-THE-MEASURED-COHERENCE-DEPTH>
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

**At the actor grain the division is essentially rigid.** Of the complete
lattice of partitions of the nine actors, the geometry leg alone cuts the field
to a handful — the geometry leg admits 6 of the 21,147 partitions of the nine
actors — and after the history leg the actor-grain factorization is unique at
5,852 of 5,856 committed histories. The four exceptions are exactly the
histories that repeat one parallel class in every round; there the class
partition joins the discrete one and the inventory has two members, both named.

**At the carrier grain it is not.** The carrier — OCC's 27 co-division cells,
the grain the excitations actually ride — admits more. On the declared window
the carrier-grain factorization is unique at 5,810 of 5,856 committed
histories, and the histories where it is not are a strictly larger set that
contains the actor grain's four and adds 42 more. Same law, same histories, two
grains, two answers: the head word is `FAC-STRATIFIED` and it is derived, not
chosen.

**And the naming result does not survive the finer grain of identification at
all.** Paper 33's stabilizer quantifies over ONE relabelling required to fix
the whole history — which presupposes that an actor persists across it. Replace
that with a family of local identifications and a declared coherence relation,
and the rigidity evaporates: the global stabilizer is trivial and the
adjacent-coherence groupoid is not at 5,852 histories. It returns only when the
identification is required to cohere across several events at once, and the
depth at which it returns is a measured constant — the collapse thresholds this
corpus carries are 3, 4, 5. Below that depth crystallized identity does not
transport. Thread-hood is not something the census found; it is something the
census assumed, in an amount this unit can now quote.

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
  carrier partition: for any two cells of a block the sums of the column's
  entries falling into each block agree, exactly, in Z[ω] — the standard
  quotient criterion, run at both declared coin orders.

The criterion's ten functions are located by AST in the instrument's own
source, digested, and gated at a point in the run where no admissible set has
yet been computed; the free names each leg references are extracted and
required to contain no census product, so no leg can consult the answer it is
deciding. The combined digest is 0019d84588bb.

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
partition, the pairwise image of every actor partition (a cell IS a pair, so
the pair-image is the identification the carrier's own typing suggests), and 12
OCC-typed natural strata — discrete, trivial, by-direction, by-anchor-site,
by-AG-line, the shift orbits and the six translation-subgroup orbit partitions
— deduplicated as partitions. Everything outside it is disclosed as outside it.

## 3. The census

| grain | unique | non-unique | histories |
|---|---|---|---|
| actor | 5,852 | 4 | 5,856 |
| carrier | 5,810 | 46 | 5,856 |

The discrete partition — the nine-fold division itself — is admissible at every
history, checked history by history, so the count is never zero and the
question is always whether anything JOINS it. At the actor grain something
joins it exactly four times, and the instrument names what: the ROW, COL, DIA
and ANT parallel-class partitions, one each, at the four schedules that repeat a
single class in all four rounds. That is the thesis field of the first verdict
segment, and it is a description of the mechanism rather than a summary of the
count: a coarser subsystem structure is admissible precisely when the history
never distinguishes the actors a coarsening would merge.

The two grains are then compared AS SETS OF HISTORIES, not as counts. The
actor grain's four are contained in the carrier grain's 46; 42 histories are
non-unique at the carrier and unique at the actor grain, and 0 the other way
round. A comparison of the two counts alone would have left the direction
unmeasured.

The coin-order fiber is discharged by running both members rather than choosing
one. Every LEG-4 evaluation is performed at G·D and at D·G — 11,799 passes
under each — and the two declared coin orders disagree on 0 census rows. The
fiber is INERT on every row of this census; that is a measurement, and it is
published beside the counts rather than used to retire the axis.

## 4. Which leg binds, and which does not

Running the complete actor lattice against a declared sub-window — the 72
strict-triple histories plus every history the census found non-unique, 76 in
all, with the remaining 5,780 named as the complement — separates the legs:

- LEG-1 admits 6 partitions at every history in the sub-window.
- LEG-2 admits 1 at the strict triples and 125 at the four non-unique ones, and
  its closed form reproduces the enumeration with 0 mismatches.
- LEG-3 admits all 21,147.

The last of these is a fact about this corpus and it is stated as one: the
record field is site-constant at 5,856 of 5,856 committed histories, so LEG-3
cannot separate anything here. It is **non-binding** on the committed corpus,
which is not the same as vacuous, and the difference is measured on the control
arm rather than asserted: on the declared synthetic histories the record leg
binds at three of the five, cutting the lattice to 1,015, 125 and 104
respectively. The record-versus-dynamics wedge is measured too. The coin reads
the record only modulo three, so a partition merging sites whose records differ
by a multiple of three passes LEG-4 and fails LEG-3. That wedge is empty on the
committed corpus and fires 4 times on the synthetic history built to carry it.
The record leg is therefore a real constraint that this corpus happens not to
exercise, and the binding here is done by geometry and history.

## 5. The groupoid crystallization

The global grain quantifies over one permutation of a persistent actor set and
asks it to fix every event. The groupoid grain replaces that with the groupoid
of partial identifications: objects are the events, an arrow is a
structure-preserving bijection between two event footprints, and a global
object is a FAMILY of local identifications — one per event — subject to a
DECLARED COHERENCE RELATION on the times. Where two times are related, their
identifications must agree wherever their domains meet. The complete relation
recovers the group; the empty relation imposes nothing; everything between is a
coordinate.

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

Two facts sit in that table.

**The complete relation is the group, and it is measured to be.** Gluing
pairwise-coherent local identifications returns a global relabelling, and the
complete coherence relation returns the global stabilizer at 5,856 of 5,856
histories — counted by a backtracking enumeration that shares no code with the
sliding-window dynamic programme, so the identification is a measurement rather
than a definition.

**The atom theorem does not survive the weaker relations.** Paper 33's
5,852 histories with trivial stabilizer are exactly the histories where the
global stabilizer is trivial and the adjacent-coherence groupoid is not at
5,852 histories: at the adjacent relation the surviving families number
124,416 at every strict triple and run from 859,963,392 to 15,479,341,056 at
the concatenations. The reason is
visible in the R-ROUND row: within a round the three division events are
pairwise DISJOINT, so a round-local coherence requirement is no requirement at
all and returns the free product exactly. Group-level triviality does not imply
groupoid-level rigidity here, and the word this unit emits,
`FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN`, is computed from that count.

The groupoid itself is measured, not merely used: on the 672 histories of the
declared sub-window its isotropy orders are 1, 3 and 6 and its connected
components run from 1 to 5, so the local identifications genuinely differ from
event to event.

## 6. The grain triangle

The test-declaration duty is discharged by running BOTH declared tests at ALL
THREE grains. TEST-RAW takes the stabilizer inside the grain's full symmetric
group. TEST-REALIZABLE intersects it with the transformations the arena itself
realizes — the affine maps of AG(2,3) that permute the declared link
directions, acting coherently on sites and on cells; the arena's own
automorphism group has order 108.

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
The raw carrier stabilizer is nontrivial at every row, from 512 up to
10,888,869,450,418,352,160,768,000,000 — a labelling of the 27 cells is not
fixed by the history in the way a labelling of the nine actors is. But almost
none of that freedom is a symmetry of anything the arena has: the two tests
agree at the actor grain at 668 of 672 rows and at the carrier grain at 0 of
672. The carrier's excess is freedom to permute cells in ways no arena
transformation realizes, which is a statement about the size of S₂₇ as much as
about the law. What the triangle establishes is the shape OCC's precedent
predicts and no more: the grain at which the history-stabilizer and the
realizable group coincide is the actor and site grain, not the carrier, and the
carrier answer is not the actor answer.

## 7. The persistence presupposition, and transport

A global relabelling is definable only on a persistent actor set. Paper 33's
effectus review says so in its own words, and this unit turns the observation
into a coordinate: the coherence relation of the groupoid grain IS how much
persistence a census assumes.

The measurement is then a single sentence. Identity is forced at the complete
relation at 5,852 histories and at the adjacent relation at 0 of them, and the
depth at which the two meet is derived per history by searching upward, never
capped: the collapse thresholds this corpus carries are 3, 4, 5, distributed as
4 at every strict triple and every concatenation, and 3, 4 or 5 across the
driven window at 4, 521 and 75 histories respectively.

So crystallized identity **does not transport** below the measured coherence
depth. That is the licensed form of the question the pin allows this unit to
pose for the first time: thread-hood — the requirement that one identification
serve the whole history — is a declaration, and this corpus prices it at three
to five events of coherence. Nothing here says whether the declaration is
right; it says what it costs and where it is being made.

The result is reported at every rung the corpus carries, from that rung's own
histories rather than from the corpus aggregate.
At R = 3 the actor grain is unique at all 72 histories, the atom breaks at all
72, and the threshold is 4. At R = 4 the actor grain is unique at 596 of 600,
the carrier grain at 554, the atom breaks at 596, and the thresholds are 3, 4
and 5. At R = 6 the actor grain is unique at all 5,184, the atom breaks at all
5,184, and the threshold is 4. The break coincides with the actor grain's
uniqueness rung by rung. PER-L closed the L-ladder transport by theorem and
PER-R places its own successor at R = 8, so nothing is claimed here beyond the
rungs measured.

## 8. The control arm

Every pre-registered outcome word must be shown reachable at the declared
arena, and none of the rows below is forged: each is a genuine evaluation of
the SAME criterion and the SAME head law on a declared datum.

| declared arena | histories | actor non-unique | carrier non-unique | head word |
|---|---|---|---|---|
| CTRL-C1-THE-STRICT-TRIPLES | 72 | 0 | 0 | FAC-FACTORIZATION-FORCED |
| CTRL-THE-NON-UNIQUE-HISTORIES | 4 | 4 | 4 | FAC-FACTORIZATION-DECLARED |
| CTRL-C3-THE-DRIVEN-WINDOW | 600 | 4 | 46 | FAC-STRATIFIED |
| CTRL-THE-WHOLE-CORPUS | 5,856 | 4 | 46 | FAC-STRATIFIED |

The head law returns a different word on each of the first three arenas, so no
pigeonhole decided the verdict before the run. On the strict triples both
grains are uniformly unique and the law returns the forced word; on the four
class-repeating histories both grains are non-unique on the SAME histories and
it returns the declared word, with the inventory named; on the driven window
and on the whole corpus the grains disagree and it returns the stratified word.

| synthetic history | events | distinct record rows | LEG-3 passers | wedge | global stabilizer | adjacent families | atom word |
|---|---|---|---|---|---|---|---|
| X1-ONE-DIVISION-EVENT | 1 | 2 | 1,015 | 0 | 4,320 | 6 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN |
| X2-ONE-FULL-ROW-ROUND | 3 | 1 | 21,147 | 0 | 216 | 216 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN |
| X3-ROW-MULTIPLICITIES-CONGRUENT-MOD-THREE | 12 | 3 | 125 | 4 | 216 | 216 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN |
| X4-THE-OVERLAPPING-CHAIN | 7 | 4 | 104 | 0 | 1 | 1 | FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN |
| X5-A-ROW-ROUND-THEN-A-COLUMN-ROUND | 6 | 1 | 21,147 | 0 | 1 | 5,184 | FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN |

Both atom words are emitted by the same law on declared data. X4 is the
decisive one: a chain of events overlapping in two actors at a time forces the
identification already at the adjacent relation, so a corpus of such histories
would have returned the other word. The corpus does not consist of such
histories, and that — not the law — is why the atom breaks here. The blocked
word is reachable only from an instrument fault, which is what that word is
for.

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

## 9. What this does not say

Every count in this unit is a count over a declared window and is stamped
COUNTING-ONLY. This unit declares no measure on partition lattices, so none of
its fractions may be read as a frequency or a likelihood; the six published
ratios each carry their window's name beside them.

The census ranges over PARTITIONS of two declared carriers. A factorization
that is not a partition of either — a change of basis on the coupled step's
state space, for instance — is outside the question as posed, and the unit does
not speak to it. The carrier window is declared and is not the carrier's whole
lattice. The corpus is the parents' corpus and the rungs are R = 3, R = 4 and
R = 6.

No sentence of this unit assigns identity to one kind of thing and chart to
another; that reading was refused on the record by paper 33's adjudication and
is a wall this instrument scans this paper for. Nothing here is a claim about
what actors are. The unit measures which decompositions the committed law
admits, at which grain, under which coherence, and reports that the answer
depends on all three.

## 10. The instrument

Ten committed files are read as sources at pinned digests, plus this paper as
the object under test; no other repository state is read and no subprocess is
invoked, so the run is correct off-tree and with no version control present. 13
verbatim anchors are matched in their sources' bytes, each named with the gate
that consumes it. The pre-registered outcome vocabulary is PARSED OUT OF THE
PIN'S OWN BYTES — 5 strings reduced to 5 families — and the head law is
required to return words from that set and from no other.

The head is derived twice by routes that share no dispatcher and no census
loop. The second calls neither admissibility dispatcher and reads none of the
first's rows: it rebuilds every admissible set from the raw leg predicates,
recounts the atom breaks from the coherence relation directly rather than from
the ladder's cache, and re-applies the head law to its own numbers. What the
two share is the four leg predicates themselves, which are the object under
test and are de-twinned by their own closed-form gates rather than by
duplication; the two agree on the head word, the atom word and all three
counts.

6 windows are declared with their bounds. 5 walls carrying 15 banned assertive
sentences are scanned against this paper's own bytes — the leg the wall is owed
— and the falsifier for that gate plants every banned sentence into exactly
that text. 36 falsifiers are declared, each naming the gate it must die at and
each carrying a source fragment located in the instrument by AST and matched
against the statement that actually carries the hook, so a description-inverted
falsifier cannot pass. 39 seals are taken at gate time and the manifest is
required to be total. Every table above is rendered from the receipt with its
HEADERS INCLUDED, so a header swap that leaves every number correct dies at a
gate; every printed class-word is recomputed from its predicate; every ratio of
the form `N of M` is resolved against the receipt and both members required to
be carried by one common member of the 18 declared referent universes, the
aggregate keys excluded by declaration because a universe carrying every number
binds nothing; and 5 polarity axes are checked in both directions. The bytes are read back from staging and compared with the
gate-time seal BEFORE `os.replace` promotes anything.

---

```
FAC-DECOMPOSITION<THESIS=THE-LAW-ADMITS-MORE-THAN-ONE-FACTORIZATION-ONLY-WHERE-THE-HISTORY-REPEATS-A-PARALLEL-CLASS; HISTORIES=5,856; ACTOR-LATTICE=21,147; ACTOR-GRAIN-LAW-COMPATIBLE-PARTITIONS=6; ACTOR-GRAIN-UNIQUE-FACTORIZATION=5,852-OF-5,856; CARRIER-WINDOW=42,295; CARRIER-GRAIN-LAW-COMPATIBLE-PARTITIONS=10; CARRIER-GRAIN-UNIQUE-FACTORIZATION=5,810-OF-5,856; COIN-ORDER-DISAGREEMENTS=0>
```

```
FAC-GROUPOID<ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; ATOM-BREAKS=5,852-OF-5,856; COLLAPSE-THRESHOLDS=3,4,5; ARENA-GROUP-ORDER=108>
```

```
FAC-STRATIFIED<BY-GRAIN=ACTOR-5852-OF-5856-UNIQUE-vs-CARRIER-5810-OF-5856-UNIQUE; ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN; SCOPE=TWO-GRAINS-AS-DECLARED;COUNTS-ARE-COUNTING-ONLY;THE-CARRIER-WINDOW-IS-DECLARED-NOT-COMPLETE;NO-CLAIM-BEYOND-THE-MEASURED-COHERENCE-DEPTH>
```
