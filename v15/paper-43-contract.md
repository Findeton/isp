# The theory contract: what ISP has, what fixes it, and what is still declared

**CONTRACT / paper-43, the first unit of v15.** Pin `v15/note-contract-pin.md`
(FROZEN, sha256-12 `438586c11db5`, v15 ledger #1); questions Q1-Q10, Q24 and
Q58, with Q4 and Q5 the actors-and-records circularity. Instrument
`v15/code/contract_exact.py`; artifacts `v15/code/contract_output.txt` and
`v15/code/contract_receipt.json`. Exact arithmetic throughout: Python integers
and `fractions.Fraction`, no float anywhere, with an abstract-syntax scan of the
instrument and a recursive type walk of the receipt among the gates. The sealed
v14 corpus is read at pinned digests and at no other route; every row below is
either recomputed here from constructors re-implemented in the instrument or
cited to a sealed unit, and every row says which.

**THE DEFENSIBLE SENTENCE.** ISP is a parameterized family; actor cardinality is
identifiable from records in a measured triangle-writing class; the full gauge
quotient, universal state and physical excitation content remain unresolved.
Everything below is the evidence for that sentence and the scope on it.

**SCOPE (binding).** This is a synthesis-with-measurements unit. It works at
one arena, the committed corpus, and no claim beyond the committed corpus is
made anywhere here. Its counts are counting-only, and no fraction in this paper
is a probability. And no new physics claim is made beyond the census's own
measurements. What is new here is the bookkeeping, stated once and gated.

**THE TWO STANDING WALLS,** engraved for the whole programme and enforced on
these bytes. Recovering a datum from records that were generated with it is
identifiability and not derivation, and this paper never promotes the one to the
other. The gauge word is withheld here: an invariance becomes a gauge redundancy
only when every physical observable and every experiment take identical values
across the orbit, and this corpus has no operational observables to test that
with.

**Verdict**, in four segments, quoted exactly as the instrument emits them.

```
CONTRACT-CENSUS-TOTAL<OBJECTS=23; COMPUTED-HERE=20; CITED=3; ACTORS=9; CELLS=27; EVENTS-REALISED=30; HISTORIES=5784; BLOCKS=27; COUNT-FIELDS=36; MENU=6; CHART-CLASSES=1296>
```

```
CONTRACT-STATE-AT-FIXED-BACKGROUND-AND-INVARIANCE<STATE-COMPONENTS=3; BACKGROUND=6; COUNT-FIELDS=36; RESIDUE-FIELDS=24; SUCCESSORS=24; EQUAL-RESIDUE-PAIRS-AGREEING=24-OF-24; DISTINCT-RESIDUE-COLLISIONS=0-OF-606; RELABELLINGS=362880; LAW-STABILIZER=1296; ARENA-STABILIZER=108; DIRECTION-INDEX=12; SPLITTINGS=12; LOCAL-GROUP=6; LOCAL-COLLAPSE-WIDTH=4; HISTORIES-SURVIVING=17-OF-5784; FIELDS-SURVIVING=12-OF-36; GAUGE-WORD=WITHHELD>
```

```
CONTRACT-CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS-UP-TO-THE-DIRECTION-DECLARATION<CYCLE-LENGTH=3; CAST-SOLUTIONS=1; RESIDUE=12; ARMS=9; RECOVERING=5; REFUSING=4>
```

```
CONTRACT-Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS-ISP-IS-A-FAMILY<DECLARATIONS=21; FREE=13; INVARIANT-IN-THE-SUBSTRATE-CENSUS=2; DERIVED=3; RECONSTRUCTED-CONDITIONALLY=1; INITIAL=2; FREE-ROWS-A-LAW-SELECTS=0; COIN-CLASSES=6; SEAM-KERNEL=4; DIRECTION-CHOICES=4; UNRESOLVED=THE-GAUGE-QUOTIENT+THE-UNIVERSAL-STATE+THE-EXCITATION-CONTENT>
```

Between delivery and adjudication every headline here is a **candidate
reading**.

---

## The short of it

The corpus has been asked, unit by unit, what it can measure. It has never been
asked what it *has*. This paper writes the inventory: one row per object, one
statement of the instantaneous state the committed machine needs, one measured
status per relabelling group, one dependency graph, and one count of the
declarations that no measured law selects.

Four things came out of the writing that the corpus had not recorded.

The first is that the construction really is circular, and that at this corpus
the circle closes inside a stated class. The construction defines a cell as a
pair of actors and then recovers the actors from the cells the record carries.
That is a genuine loop, and it is not vicious here: searched exhaustively, over
families of token sets with the actor count left free, exactly one cast survives
the record's own triangles.

The second is what that uniqueness does not fix. The record fixes the cast and
the link structure as sets; it does not fix which of the parallel classes were
declared as links. The derived structure offers a family of splittings into
direction classes and the record prefers none of them.

The third is a group. The law that selects an admissible round counts how many
linked pairs sit inside a group, and that count does not know which classes were
declared. So the round law's own stabilizer is strictly larger than the arena's,
by exactly the index the record's residue has; and rebuilding the whole
substrate census under each of the four declarations returns the same numbers,
four times over. What that licenses is an invariance statement, and the paper
stops there.

The fourth is a concession, and it is the answer to the question the pin sent
this unit to settle. The reconstruction of actors from records was measured at
one generating mechanism. Run through nine, it holds at five and refuses at
four, and what separates them is measured rather than argued.

---

## 1. The object census

The pin asks for one row per object, each classed by the five words it declares
and each backed either by a computation this run performs or by a citation to a
sealed unit at its pinned digest. Cardinalities are at the committed corpus.

| object | class | cardinality | backing | reading |
|---|---|---|---|---|
| ACTOR | DECLARED | 9 | COMPUTED-HERE | declared as the points of the arena, and derived back from the record |
| SITE | DECLARED | 9 | COMPUTED-HERE | the same objects as the actors under the weld's dictionary |
| DIRECTION | DECLARED | 3 | COMPUTED-HERE | three of the parallel classes of the arena are declared links |
| PARALLEL-CLASS | GENERATED | 4 | COMPUTED-HERE | the resolutions of the arena, generated from the field |
| CELL | GENERATED | 27 | COMPUTED-HERE | one per site and declared direction |
| CO-DIVISION-PAIR | GENERATED | 27 | COMPUTED-HERE | the cell is the unordered pair, by the carrier typing |
| DIVISION-EVENT | GENERATED | 84 | COMPUTED-HERE | every group of the declared arity; the corpus realises some of them |
| REALISED-EVENT | GENERATED | 30 | COMPUTED-HERE | the events the committed corpus actually runs |
| GROUPING | GENERATED | 280 | COMPUTED-HERE | the partitions of the actors into groups of the declared arity |
| ADMISSIBLE-ROUND | LAW-SELECTED | 36 | COMPUTED-HERE | the groupings the saturation law admits |
| HISTORY | GENERATED | 5,784 | COMPUTED-HERE | the distinct sequences of events the committed drivers produce |
| RECORD-BLOCK | GENERATED | 27 | COMPUTED-HERE | the cells one event writes |
| BARE-RECORD | GENERATED | 5,643 | COMPUTED-HERE | the sequence of blocks, actor labels erased |
| COUNT-FIELD | GENERATED | 36 | COMPUTED-HERE | the division count on each cell |
| QUANTUM-STATE | DECLARED | 27 | COMPUTED-HERE | one amplitude per cell, in the ring the field generates |
| MENU | LAW-SELECTED | 6 | COMPUTED-HERE | the coset partitions of the translation subgroups |
| NAMING | RECONSTRUCTED | 1,296 | COMPUTED-HERE | the relabellings the record admits of the derived cast |
| DIRECTION-SPLITTING | RECONSTRUCTED | 12 | COMPUTED-HERE | the ways the derived link structure splits into classes |
| COIN | DECLARED | 6 | COMPUTED-HERE | the covariant unitary family, up to a global phase |
| SEAM | DECLARED | 4 | COMPUTED-HERE | the undetermined entries the chart leaves at a shared site |
| CHART | DECLARED | 16 | SEALED-CITATION | the combinatorial types of a two-sector overlap |
| TICK | DECLARED | 1 | SEALED-CITATION | one scheduling convention; the emergent speed is one site a tick |
| CARRIER-CANDIDATE | DECLARED | 27 | SEALED-CITATION | the carrier the exclusion census selected; excitations are not declared until the excitation gate opens |

Three rows are citations rather than computations, and they are the three whose
objects belong to units this one does not rebuild: the overlap types of two
glued sectors, the scheduling convention, and the carrier an exclusion census
selected. That last row is named CARRIER-CANDIDATE and not EXCITATION on purpose:
the programme's dependency gate forbids declaring an excitation before the
excitation unit has run, and what the sealed census selected is a carrier the
exclusion test prefers, not a particle.

The remaining rows are recomputed here from constructors written in the
instrument, and their parents' own sentences are bound to them. The carrier row
is the parent's:

> 27 cells against 27 pairs, two actors in each cell at all of them, six cells
> per actor at all nine

and the same object seen from the exclusion census reads

> CELLS-WITH-EXACTLY-TWO-ACTORS=27-OF-27; ACTORS-IN-EXACTLY-SIX-CELLS=9-OF-9

Both are consumed by the census gate rather than merely quoted: the numerals
they carry are parsed out and compared with the numbers this run computed.

The scheduling row is cited to the unit that measured it, whose own title says
what it found:

> The Emergent Speed Is One Site a Tick and It Is Attained

and the overlap row to the unit that censused the glued sectors:

> the family is 45010 gluings in 16 combinatorial types

The row worth pausing on is the first. An actor is classed DECLARED, because the
constructors declare it. Section four measures the sense in which the record
hands the same object back, and section five measures how far that recovery
travels. Neither section upgrades the census row, because the record it reads
was written by a mechanism that already used the cast.

---

## 2. The instantaneous state of the committed machine

Q2 asks what the state at one instant is, stated once. The state below is
sufficient for the committed machine at fixed background, and the universal state
waits on the autonomous-update unit. That unit is chartered to build an update
in which geometry, record and state move together without a pre-declared target,
and until it runs a state list is a list for a machine, not for the theory.

| component | shape | what it carries |
|---|---|---|
| THE-COUNT-FIELD | one non-negative integer per cell | the geometry: the division count the weld identifies with the metric |
| THE-AMPLITUDE | one ring element per cell | the quantum state the coin and the shift act on |
| THE-BRANCH-WEIGHT | one exact rational | the bookkeeping weight the emission law multiplies |

Everything else the update reads is background: fixed before the first step,
never moved by any step.

| declaration | what it fixes |
|---|---|
| THE-ACTOR-SET | the cast the arena declares |
| THE-DIRECTION-DECLARATION | which classes are links |
| THE-COIN | the covariant unitary chosen from its family |
| THE-ORDER | coin before or after the residue |
| THE-ORIENTATION | the sign of the shift |
| THE-READING | the Born menu or the record menu |

**Sufficiency, measured.** A state list is sufficient when it screens the history
off the update: two runs agreeing on the list must have the same successor. The
instrument measures that directly. It collects every count field the corpus
realises, applies one coupled step to a common amplitude under each, and
compares.

| quantity | value |
|---|---|
| count fields over the corpus | 36 |
| residue fields | 24 |
| one-step successors | 24 |
| equal-residue field pairs | 24 |
| of which the successor agrees | 24 |
| distinct-residue field pairs | 606 |
| of which the successor agrees | 0 |
| Born-menu values | 24 |
| record-menu values | 36 |

The count field enters the quantum update only through its residue, and enters
the record menu whole, so what the state must carry is reading-relative. The
parent says the same thing in its own voice:

> the walk consumes the count residue n mod 3, not the count.

Under the Born-menu reading the update is a function of the amplitude and the
residue alone: every pair of count fields with equal residues has the same
successor, and no pair with different residues shares one. Under the record-menu
reading the weights are the counts themselves, and the fields separate. So the
minimal sufficient state is reading-relative, while the state as listed above --
which carries the count field whole -- is sufficient under both. That is why the
list carries the field and not the residue.

---

## 3. The invariance census

Q6 asks which transformations are redundancy. Q7 asks whether the symmetric
group on the actors is merely relabelling. Q8 asks what the local group at an
event is. Q9 asks what survives the quotient. This section measures what those
groups do to the substrate census, and it stops short of answering them, because
the answer they want is an operational one and the corpus has no operational
observables yet. The status column below says what was measured and nothing more.

| group | order | what it preserves | measured status |
|---|---|---|---|
| all relabellings | 362,880 | nothing of the arena | MOVES-THE-SUBSTRATE-CENSUS |
| the round law's stabilizer | 1,296 | which groups the law admits | SUBSTRATE-CENSUS-INVARIANT |
| the link structure's automorphisms | 1,296 | which pairs are linked | SUBSTRATE-CENSUS-INVARIANT |
| the arena's automorphisms | 108 | the link structure and the direction classes | SUBSTRATE-CENSUS-INVARIANT |
| the local relabellings at one event | 6 | nothing beyond the event's own order | COUNT-INVARIANT-AT-AND-ABOVE-THE-WIDTH |

The line to read is the second. The law that decides whether a grouping is an
admissible round counts the linked pairs inside its groups; it never asks which
direction a link carries. Its stabilizer was computed by an exhaustive pruned
search over the whole symmetric group, and it is exactly the automorphism group
of the link structure -- larger than the arena's own group, and larger by the
index the record's residue has. The parent's naming census says the same from
the record's side:

> the record admits 1,296 namings of the derived cast and 108 of them carry the
> declared direction classes

**The direction declaration, priced.** The round law is blind to which classes
are declared, and the four declarations return the same substrate census. That is
measured by rebuilding the arena, the admissible rounds, the covering triples,
the saturating quadruples, the footprint spectrum, the block set and the actor
stars under each of the four choices and comparing the results. One instance of
this was already measured by hand, and its three counts are the arena's own:

> rebuilt with ANT in place of DIA the substrate returns 36 saturating, 72
> I7-STRICT triples and 276 G-FLAT quadruples

and this run completes the sweep. That blindness is measured on the substrate
census alone; the coupled dynamics, the readings, the orientation and any
interaction a later unit builds are outside the sweep.

**The local group.** At one event the actors carry an order, and the group that
permutes it acts locally. The instrument counts the locally coherent assignments
of that group over a committed history at each sliding window width, against the
assignments that are globally coherent.

| window width | locally coherent assignments |
|---|---|
| 0 | 10,077,696 |
| 1 | 124,416 |
| 2 | 144 |
| 3 | 4 |
| 4 | 1 |
| 5 | 1 |

The global count is one: on this history the only globally coherent assignment
is the identity. Below the collapse width there are strictly more locally
coherent assignments than global ones; at and above it the two agree. That is a
counting fact about window widths, and it is what the status column reports. What
would upgrade it -- for this group and for every other row of the table -- is the
every-observable standard: a set of operational observables, an experiment for
each, and a demonstration that all of them take identical values across the
orbit. The programme does not have that yet.

The structure those groups act on is the one the separation census measured:

> The graph is therefore complete multipartite with those three lines as its
> parts, and every site has degree six

**What survives.** Quotienting by a group is only interesting if something is
left. The instrument counts the orbits of the corpus's own objects under the
arena's automorphisms and under the link structure's.

| object | before | modulo the arena | modulo the links |
|---|---|---|---|
| histories | 5,784 | 25 | 17 |
| count fields | 36 | 12 | 12 |

The histories collapse hard and the count fields collapse harder, and the count
fields collapse to the same number under both groups -- the extra freedom the
link group has over the arena group merges no further count field. So what the
substrate census leaves after the quotient is the link structure itself, the
orbit of the history under it, and the count field up to that orbit. Whether
that is the physical content is exactly what the withheld word withholds.

---

## 4. The circularity, and what closes it

Q4 asks whether the dependency structure can be written without circularity.
Here is the structure, edge by edge.

| from | to | the edge |
|---|---|---|
| ACTOR | CELL | a cell is an unordered pair of actors |
| DIRECTION | CELL | a cell carries one declared direction |
| ACTOR | DIVISION-EVENT | an event is a set of actors |
| CELL | ROUND-LAW | saturation counts the cells a grouping covers |
| ROUND-LAW | HISTORY | a history is a sequence of admissible rounds |
| DIVISION-EVENT | HISTORY | a history is a sequence of events |
| HISTORY | RECORD-BLOCK | an event writes the cells inside it |
| RECORD-BLOCK | COUNT-FIELD | the count field tallies the blocks |
| COUNT-FIELD | QUANTUM-STATE | the coin reads the count residue |
| QUANTUM-STATE | EMISSION | the menu weights the next division event |
| EMISSION | COUNT-FIELD | an emission increments the count field |
| RECORD-BLOCK | ACTOR | the reconstruction derives the cast |

It cannot. The construction is circular, and at the committed corpus the record
admits exactly one cast inside the triangular representation class. Two of the
graph's cycles run through both the cast and the record, and the shorter of them
is the one Q4 names: an actor makes an event, an event makes a history, a history
writes a record block, and the record block hands the actor back.

Q5 asks whether that circle closes. Here is the measurement. Strip the labels;
keep only which tokens each event wrote; then ask for every family of token sets
under which each record block is a triangle carrying no foreign token. The search
leaves the number of actors free, introduces a fresh actor whenever the
constraints permit one, and collects solutions as families rather than as
labelled structures, so two that differ by a renaming count once. It returns
exactly one family, and that family is the declared cast, as sets.

That is uniqueness inside a declared representation class, and it is not a fixed
point of the actor-record-emission dynamics. The class is the one the search
declares -- families of token sets in which every record block is a triangle --
and the result says that inside it the record leaves no choice. It does not say
that the coupled dynamics, run forward from the recovered cast, returns the
record it started from; that composition is the autonomous-update unit's object
and is untouched here.

What the record does not fix is the direction declaration, and the residue is an
index the record offers and does not choose. The derived link structure admits
several splittings into direction classes; the declared splitting is one of them;
the record supplies the structure and leaves the splitting open.

The uniqueness is a corpus fact and not a per-history one, and the sealed unit
that first measured the reconstruction says why:

> no committed history sees more than 18 of the 27 record blocks

---

## 5. Q58: emergence, or identifiability?

The question the pin sends this unit to settle is whether the reconstruction
demonstrates that actors arise from records, or only that latent actors can be
identified in a model that already used them to write its data. The pin asks for
the discriminating measurement: run the same reconstructor on records written by
a different admissible mechanism.

The corpus supplies several. Three committed drivers write the same corpus by
different routes. A grammar-free mechanism writes the blocks of every group whose
members are pairwise linked, with no schedule at all. Another writes the blocks
of every group of the declared arity, admissible round or not. Another writes
only the two-cell blocks. And the coupled dynamics writes its own record: one
emitted cell per step, which is a co-division pair rather than a group of the
declared arity, at two grains -- the emitted cell, and the site menu the emission
law weights.

| mechanism | kind | actors per event | blocks | block sizes | certificate | cast recovered |
|---|---|---|---|---|---|---|
| THE-COMMITTED-GRAMMAR | GRAMMAR | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-STRICT-COVER-DRIVER | GRAMMAR | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-CONCATENATION-DRIVER | GRAMMAR | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-DRIVEN-WINDOW | GRAMMAR | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-PAIRWISE-LINKED-GROUPS | GRAMMAR-FREE | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-UNRESTRICTED-GROUPS | GRAMMAR-FREE | 3 | 81 | 54 x 2+27 x 3 | TOKEN-NOT-IN-EXACTLY-TWO | no |
| THE-NON-COLLINEAR-GROUPS | GRAMMAR-FREE | 2 | 54 | 54 x 2 | TOKEN-NOT-IN-EXACTLY-TWO | no |
| THE-COUPLED-WALK-EMISSION | DYNAMICS | 2 | 27 | 27 x 1 | THRESHOLD-UNDETERMINED | no |
| THE-COUPLED-WALK-SITE-MENU | DYNAMICS | 2 | 9 | 9 x 3 | THRESHOLD-UNDETERMINED | no |

The reconstruction is not generator-independent: it holds across every mechanism
that writes triangles and refuses on every mechanism that does not. Block size
alone is not the criterion, and the instrument gates that it is not: one refusing
arm writes blocks of the declared arity and still refuses, because its blocks are
stars at a site rather than triangles among three actors. Triangularity with
every token covered is the criterion, and it decides all nine arms.

The refusals are the reconstructor's own, and they name their leg. Where the
emitted blocks are single cells there is no co-writing at all, so the rule has no
meet to threshold and declines to invent one. Where the blocks are stars the same
thing happens for a different reason. Where the two-cell blocks are present the
rule runs and its answer fails its own membership certificate.

So the answer to the emergence question is identifiability within a generative
class. The class is not the committed schedule -- four mechanisms outside it
recover the cast exactly, one of them with no grammar at all -- but it is a
class, and its boundary is measured rather than assumed. The corpus's one
autonomous dynamics is outside it. And the standing wall applies with full force
here: every record these arms read was written by a mechanism that already had
the cast in hand, so what is measured is how widely the cast can be identified,
never that the cast was selected among worlds that lacked it.

---

## 6. The parameters

Q10 asks whether ISP is one theory or a family. Q24 asks whether, if nothing
selects its quantities, the theory can say so cleanly. Here is the clean saying:
every declaration the corpus makes, its fiber where a fiber has been measured,
its class, and whether any measured law selects it.

| declaration | what it fixes | fiber | class | a measured law selects it | where it is measured |
|---|---|---|---|---|---|
| d | the spatial dimension | UNSWEPT | FREE | NO | NDEP |
| q | the field order | SWEPT-AT-THREE-POINTS | FREE | NO | NDEP |
| a | the division-event arity | UNSWEPT | FREE | NO | ARITY-CHARTERED |
| R | the depth in rounds | SWEPT-ALONG-THE-LADDER | FREE | NO | PERR |
| the window | the driven schedule set | DECLARED-WINDOW | FREE | NO | R4DEC |
| the coin | the S_3-covariant unitary | COMPUTED-HERE | FREE | NO | COUPLING |
| the coin order | coin before or after the residue | DECLARED-PAIR | FREE | NO | COUPLING |
| the orientation | the sign of the shift | DECLARED-PAIR | FREE | NO | COUPLING |
| the horizon | the number of coupled steps | DECLARED | FREE | NO | COUPLING |
| the reading | the Born menu or the record menu | DECLARED-PAIR | FREE | NO | COUPLING |
| the seam | the completion at a shared site | COMPUTED-HERE | FREE | NO | SEC-2 |
| the ceiling | the occupancy ceiling | DECLARED | FREE | NO | OCC |
| the measure | the measure over configurations | A-SIMPLEX | FREE | NO | R5M |
| L | which classes are declared links | COMPUTED-HERE | INVARIANT-IN-THE-SUBSTRATE-CENSUS | NO | AID |
| the coordinate | the naming of the record tokens | ANY-BIJECTION | INVARIANT-IN-THE-SUBSTRATE-CENSUS | NO | REC |
| n | the actor count | COMPUTED-HERE | RECONSTRUCTED-CONDITIONALLY | NO | THIS-UNIT |
| the cell count | the carrier size | COMPUTED-HERE | DERIVED | YES | THIS-UNIT |
| the connection | the group the walk's phases live in | DECLARED | DERIVED | YES | COUPLING |
| the menu | the admissible actor grains | COMPUTED-HERE | DERIVED | YES | FAC |
| the state | the initial amplitude | AN-INITIAL-CONDITION | INITIAL | NO | COUPLING |
| the record | the initial count field | AN-INITIAL-CONDITION | INITIAL | NO | COUPLING |

Three rows are DERIVED and say so: the carrier size follows from the actor count
and the link count, the walk's phase group from the field, and the admissible
grains from the translation subgroups. One row is
RECONSTRUCTED-CONDITIONALLY, and it is the actor count. It is not derived and no
law selects it: it can be read back off records written inside the triangular
class of section five, and outside that class it cannot, so its status is
conditional on the mechanism that wrote the record. Two rows are invariant in the
substrate census: the direction declaration, priced in section three, and the
coordinate on the record's tokens, which the sealed reconstruction unit prices at
random relabellings. Two are initial conditions. The rest are free, and none of
them is selected by anything the corpus has measured. The parent that swept the
arena size says as much of its own numerals:

> NO TESTED NUMERAL IS REPRODUCED BY THE DECLARED n-ONLY READING

The verdict word follows from the count and not from a judgement: with a positive
free count the comparator writes the family word. That is the honest statement
Q24 asks for. It is not a defeat and it is not a boast; it is the inventory.

Two of the free rows are worth naming because their fibers were computed here
rather than cited. The coin family is enumerated exactly over the ring the field
generates: the covariant unitarity conditions have a finite solution set, which
falls into classes up to a global phase, of which one is the coin the corpus
delivered. The parent's sentence is bound to that count:

> falling into 6 classes up to a global phase, of which exactly 1 is +/- Grover

And the seam's undetermined entries are counted by rank rather than asserted: the
declared directions at a shared site span a proper subspace of the symmetric
square of the doubled tangent space, and the corank is the number of numbers the
gluing must declare. The sealed unit's own sentence:

> The seam's own system is rank 6 on 10 by the chart alone, kernel 4; an
> unshared site's system is three equations on

The window closes mid-clause because it is pinned to its parent's bytes rather
than to a sentence boundary.

---

## 7. What this does not say

The census is at one arena and over the committed corpus. Nothing here is a
theorem about records, casts or theories at large, and the uniqueness result in
particular is a statement about this record inside this representation class.

The state list is the list the committed machine needs. A unit that declared a
different dynamics would owe its own list, and the sufficiency measurement would
have to be redone; what transfers is the method, which is that a list earns the
word sufficient by screening the history off the update.

The invariance census measures invariance of the substrate census. It does not
license a gauge quotient, it does not say which relabellings are unobservable,
and it does not say that the symmetric group's other elements are observable
either. Those are operational questions, and the corpus reaches them only when an
observable and an experiment exist to ask them of.

The parameter table's fibers are measured where the fiber column says computed
and declared where it says declared. An unswept row is unswept: it is not a claim
that the quantity could not be swept, only that the sealed corpus has not swept
it, and two of those rows are the charter of the next unit.

The mechanism arms are a domain probe, not a classification of mechanisms. Nine
were run because nine are in the corpus; the criterion they suggest is stated as
what separates these nine.

---

## 8. The instrument

`v15/code/contract_exact.py`. Four code regions -- builder, stripper,
reconstructor, comparator -- are disjoint by machine check: no reconstructor and
no comparator function reaches a builder or a stripper at any depth, through an
alias or through a helper. That is the corpus's registered S-1 family, answered
by construction rather than by promise, and the comparator is shown to have teeth
by refusing four of the nine mechanisms and by rebuilding the verdict from the
serialized receipt alone.

The head is not trusted to its renderer. Every numeral position in the four
segments is parsed back out of the emitted string by a reader that shares no code
and no literal with the builder, and compared, as an integer, against the receipt
leaf it names.

The pre-registered outcome words are all reachable, and reachability is
demonstrated in the delivery run rather than argued: each word is emitted by
handing the comparator a declared input it did not measure here.

| pre-registered word | the control that emits it |
|---|---|
| CENSUS-TOTAL | a declared input handed to the comparator |
| CENSUS-PARTIAL | a declared input handed to the comparator |
| ACYCLIC | a declared input handed to the comparator |
| CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS | a declared input handed to the comparator |
| CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS-UP-TO-THE-DIRECTION-DECLARATION | a declared input handed to the comparator |
| CIRCULAR-BLOCKED-AT-THE-CAST | a declared input handed to the comparator |
| Q58-EMERGENCE-GENERATOR-INDEPENDENT | a declared input handed to the comparator |
| Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS | a declared input handed to the comparator |
| Q58-UNDECIDED-NO-SECOND-MECHANISM | a declared input handed to the comparator |
| ISP-IS-ONE-THEORY | a declared input handed to the comparator |
| ISP-IS-A-FAMILY | a declared input handed to the comparator |

The two standing walls are built as walls and not as prose. Their patterns are
voice-normalised regular expressions over the canonicalised paper, their standing
sentences must be carried or the run fails, and their positive controls are
written as a paper would write the violation rather than derived from the
patterns. The programme's own engraving is read at its pinned bytes and consumed
by the wall gate:

> W1: reconstruction is never promoted to derivation. W2: invariance is never
> promoted to gauge or physical meaning before operational observables exist

The nine template families are imported from the era's reference implementation
and used rather than copied: each family's check identifier is matched to a live
call in this module and that match is gated. Gate-time seals verified at the door
with totality recomputed there, over a seal partition the run proves total;
the transcript reconciled with the ledger by content; verbatim anchors consumed
by predicates that take numerals out of the located text and compare them with
measurements; claims, tables and fenced blocks by two-way equality keyed by
table; referent binding per occurrence over prose with the rendered tables
removed; no typed numeral anywhere in the subtree of a statement builder, with
the two subspecies the era registered -- a numeral reaching a builder through a
format string, and an integer offset -- caught by a second scan this unit adds;
falsifiers that must move the measured key they name and die at the gate they
name, one per gate, with a single waiver whose forcing is machine-checked; and
the read set recorded at an audit hook on the open event and reconciled at the
last gate of all.

Every repository read is at a pinned digest.

| path | sha256-12 |
|---|---|
| v14/TEMPLATE.md | 809ebe3514ad |
| v14/code/era_template.py | d04a3eb58fbc |
| v14/paper-19-r3-weld.md | 50bb81e67942 |
| v14/paper-20-coupling.md | 4824d190af73 |
| v14/paper-21-r4dec.md | ef4a8c35a0c4 |
| v14/paper-31-occ.md | 0092caa4d9ad |
| v14/paper-32-sec.md | f3f43d94cd75 |
| v14/paper-33-aid.md | ecdd3fbf1d06 |
| v14/paper-35-fac.md | 281289a615ad |
| v14/paper-38-epr.md | 22beb6696223 |
| v14/paper-39-ndep.md | e2293b8c3858 |
| v14/paper-40-sec2.md | 4fe88602280c |
| v14/paper-41-rec.md | c5fbc9acbd76 |
| v14/paper-42-hor.md | 164aa0d755bc |
| v15/PLAN.md | 6ba8621d4ec7 |
| v15/note-contract-pin.md | 438586c11db5 |

The two objects that cannot be pinned against themselves are the instrument,
whose own syntax tree its gates audit, and this paper, which is the object under
test.
