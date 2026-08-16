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
CONTRACT-CENSUS-TOTAL<OBJECTS=23; DISTINCT-EXTENTS=20; COMPUTED-HERE=20; CITED=3; ACTORS=9; CELLS=27; EVENTS-REALISED=30; HISTORIES=5784; BLOCKS=27; COUNT-FIELDS=36; MENU=6; CHART-CLASSES=1296>
```

```
CONTRACT-STATE-AT-FIXED-BACKGROUND-AND-INVARIANCE<STATE-COMPONENTS=2; ENSEMBLE-SIDE-BOOKKEEPING=1; BACKGROUND=6; COUNT-FIELDS=36; RESIDUE-FIELDS=24; SUCCESSORS=24; EQUAL-RESIDUE-PAIRS-AGREEING=24-OF-24; DISTINCT-RESIDUE-COLLISIONS-AT-THE-UNIFORM-AMPLITUDE=0-OF-606; DISTINCT-RESIDUE-COLLISIONS-AT-A-SINGLE-CELL-AMPLITUDE=205-OF-606; BORN-MENU-VALUES=4; RELABELLINGS=362880; LAW-STABILIZER=1296; ARENA-STABILIZER=108; DIRECTION-INDEX=12; SPLITTINGS=12; LOCAL-GROUP=6; LOCAL-COLLAPSE-WIDTH=4; HISTORY-EVENT-MULTISETS=136; HISTORIES-SURVIVING=17-OF-136; HISTORIES-ORDER-KEPT-SURVIVING=1067-OF-5784; FIELDS-SURVIVING=12-OF-36; GAUGE-WORD=WITHHELD>
```

```
CONTRACT-CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS-UP-TO-THE-DIRECTION-DECLARATION<CYCLE-LENGTH=3; ACTOR-RECORD-CYCLE-LENGTH=4; CAST-SOLUTIONS=1; RESIDUE=12; ARMS=9; DISTINCT-INPUTS=5; RECOVERING=5; RECOVERING-INPUTS=1; REFUSING=4; REFUSING-INPUTS=4>
```

```
CONTRACT-Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS-ISP-IS-A-FAMILY<DECLARATIONS=23; FREE=15; INVARIANT-IN-THE-SUBSTRATE-CENSUS=2; DERIVED=3; RECONSTRUCTED-CONDITIONALLY=1; INITIAL=2; FREE-ROWS-A-LAW-SELECTS=0; COIN-CLASSES=6; SEAM-KERNEL=4; DIRECTION-CHOICES=4; UNRESOLVED=THE-GAUGE-QUOTIENT+THE-UNIVERSAL-STATE+THE-EXCITATION-CONTENT>
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

The second is what that uniqueness does not fix. The reconstruction returns the
cast and the link structure as sets; it does not return which of the parallel
classes were declared as links. The reconstructed structure offers a family of
splittings into direction classes and the record prefers none of them.

The third is a group. The law that selects an admissible round counts how many
linked pairs sit inside a group, and that count does not know which classes were
declared. So the round law's own stabilizer is strictly larger than the arena's,
by exactly the index the record's residue has -- and the two are the same index
by a theorem, not by coincidence: the stabilizer acts transitively on the
splittings and the stabilizer of the declared one is the arena's own group.
Rebuilding the whole substrate census under each of the four declarations
returns the same numbers, four times over. What that licenses is an invariance
statement, and the paper stops there.

The fourth is a concession, and it is the answer to the question the pin sent
this unit to settle. The reconstruction of actors from records was measured at
one generating mechanism. Run through nine mechanisms, the cast comes back at
five and does not at four: at two the rule ran and its own membership
certificate rejected the cast it built, and at two -- both grains of the
coupled walk's own emission law -- the record carries no co-writing to
threshold, so the rule declines and returns none.

---

## 1. The object census

The pin asks for one row per object, each classed by the five words it declares
and each backed either by a computation this run performs or by a citation to a
sealed unit at its pinned digest. Cardinalities are at the committed corpus, and
the fourth column says what each number counts, because a state-space dimension,
a kernel corank and a scheduling convention are not object counts and are not
summed with them here.

| object | class | cardinality | what the number counts | backing | reading |
|---|---|---|---|---|---|
| ACTOR | DECLARED | 9 | actors | COMPUTED-HERE | declared as the points of the arena, and reconstructed from the record inside the triangular class of section five |
| SITE | DECLARED | 9 | sites | COMPUTED-HERE | the same objects as the actors under the weld's dictionary |
| DIRECTION | DECLARED | 3 | declared classes | COMPUTED-HERE | three of the parallel classes of the arena are declared links |
| PARALLEL-CLASS | GENERATED | 4 | resolutions | COMPUTED-HERE | the resolutions of the arena, generated from the field |
| CELL | GENERATED | 27 | cells | COMPUTED-HERE | one per site and declared direction |
| CO-DIVISION-PAIR | GENERATED | 27 | cells | COMPUTED-HERE | the cell is the unordered pair, by the carrier typing |
| DIVISION-EVENT | GENERATED | 84 | actor groups | COMPUTED-HERE | every group of the declared arity; the corpus realises some of them |
| REALISED-EVENT | GENERATED | 30 | events | COMPUTED-HERE | the events the committed corpus actually runs |
| GROUPING | GENERATED | 280 | partitions | COMPUTED-HERE | the partitions of the actors into groups of the declared arity |
| ADMISSIBLE-ROUND | LAW-SELECTED | 36 | partitions | COMPUTED-HERE | the groupings the saturation law admits |
| HISTORY | GENERATED | 5,784 | sequences | COMPUTED-HERE | the distinct sequences of events the committed drivers produce |
| RECORD-BLOCK | GENERATED | 27 | blocks | COMPUTED-HERE | the cells one event writes |
| BARE-RECORD | GENERATED | 5,643 | sequences | COMPUTED-HERE | the sequence of blocks, actor labels erased |
| COUNT-FIELD | GENERATED | 36 | fields | COMPUTED-HERE | the division count on each cell |
| QUANTUM-STATE | DECLARED | 27 | ring coordinates | COMPUTED-HERE | one amplitude per cell, in the ring the field generates |
| MENU | LAW-SELECTED | 6 | coset partitions | COMPUTED-HERE | the coset partitions of the translation subgroups |
| NAMING | RECONSTRUCTED | 1,296 | relabellings | COMPUTED-HERE | the relabellings the record admits of the reconstructed cast |
| DIRECTION-SPLITTING | RECONSTRUCTED | 12 | splittings | COMPUTED-HERE | the ways the reconstructed link structure splits into classes |
| COIN | DECLARED | 6 | classes up to a phase | COMPUTED-HERE | the covariant unitary family, up to a global phase |
| SEAM | DECLARED | 4 | undetermined numbers | COMPUTED-HERE | the undetermined entries the chart leaves at a shared site |
| CHART | DECLARED | 16 | combinatorial types | SEALED-CITATION | the combinatorial types of a two-sector overlap |
| TICK | DECLARED | 1 | sites a tick | SEALED-CITATION | one scheduling convention; the emergent speed is one site a tick |
| CARRIER-CANDIDATE | DECLARED | 27 | cells | SEALED-CITATION | the carrier the exclusion census selected; excitations are not declared until the excitation gate opens |

Three rows are citations rather than computations, and their objects belong to
units this one does not rebuild. That last row is named CARRIER-CANDIDATE and not EXCITATION on
purpose: the programme's dependency gate forbids declaring an excitation before
the excitation unit has run, and what the sealed census selected is a carrier
the exclusion test prefers, not a particle.

No row is classed PRIMITIVE. That is a substantive result of the census and not
an oversight: at this corpus ISP's contract declares nothing primitive -- every
object is declared, generated, law-selected or reconstructed.

The census names twenty-three rows and twenty distinct extents, because the
weld's dictionary identifies the sites with the actors and the carrier typing
identifies the co-division pairs and the carrier candidate with the cells.

The remaining rows are recomputed here from constructors written in the
instrument, and their parents' own sentences are bound to them. The carrier row
is the parent's:

> 27 cells against 27 pairs, two actors in each cell at all of them, six cells
> per actor at all nine

and the same object seen from the exclusion census reads

> CELLS-WITH-EXACTLY-TWO-ACTORS=27-OF-27; ACTORS-IN-EXACTLY-SIX-CELLS=9-OF-9

Both are consumed by the census gate rather than merely quoted: the numerals
they carry are parsed out and compared with the numbers this run computed. They
are two viewpoints on one measurement rather than two measurements -- the
exclusion census measured it and the reconstruction unit quotes that measurement
back -- and only the first supplies the cardinality the row publishes.

The scheduling row is cited to the unit that measured it, whose own title says
what it found:

> The Emergent Speed Is One Site a Tick and It Is Attained

and the overlap row to the unit that censused the glued sectors:

> the family is 45010 gluings in 16 combinatorial types

Both cited cardinalities are parsed out of those located sentences -- the second
from its digits, the first from the numeral the title spells in words -- so
neither is typed here, and a parent that said something else would move the row.

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

One quantity the machine carries is deliberately not on that list, and this is
the one classification it gets. The branch weight travels with a run and is
compared across runs; it is ensemble-side bookkeeping and not a component of
the state at one instant. The screening measurement below never reads it, and
the instrument gates the two tables against each other so that no quantity can
be named in both.

| quantity | shape | what it carries |
|---|---|---|
| THE-BRANCH-WEIGHT | one exact rational | ensemble-side bookkeeping: the weight the emission law multiplies along a branch, carried to compare runs and never read by the one-instant update |

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
| post-coin state vectors | 24 |
| Born-menu values | 4 |
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

Two cautions travel with that table, and both are measured rather than assumed.

The first is that its two legs are not the same kind of fact. Sufficiency --
equal residue, equal successor -- is structural: the update indexes the count
only through its residue, so equal residues give byte-identical successors by
construction, and the row that reports it could not have read otherwise.
Minimality -- distinct residue, distinct successor -- is contentful, and it is
amplitude-relative. The instrument repeats the whole measurement at each of the
declared amplitudes.

| amplitude | one-step successors | equal-residue pairs agreeing | distinct-residue pairs colliding | Born-menu values |
|---|---|---|---|---|
| THE-UNIFORM-AMPLITUDE | 24 | 24 of 24 | 0 of 606 | 4 |
| A-SINGLE-CELL-AMPLITUDE | 3 | 24 of 24 | 205 of 606 | 1 |
| ONE-LINK-DIRECTION-ONLY | 3 | 24 of 24 | 205 of 606 | 1 |
| ALTERNATING-ROOTS | 24 | 24 of 24 | 0 of 606 | 9 |
| THE-ZERO-AMPLITUDE | 1 | 24 of 24 | 606 of 606 | 1 |

Sufficiency holds at every amplitude probed, including the degenerate one.
Minimality does not: at an amplitude supported on one coordinate of the ring,
205 of the 606 distinct-residue pairs share a successor, so a coarser state
would suffice there. The head's zero-of-606 is therefore stamped to the uniform amplitude, and
carries the single-cell figure beside it.

The second is that the Born menu is not the state the update leaves. The row
labelled Born-menu values counts the distinct emission weights, and there are
four of them over the thirty-six count fields; the twenty-four are the distinct
amplitude vectors the same step produces, which is a different quantity. The reading-relativity the
section argues for is wider than the first delivery reported, not narrower:
reading A's emission sees four values where the record menu sees thirty-six.

---

## 3. The invariance census

Q6 asks which transformations a later unit could call redundancy. Q7 asks
whether the symmetric group on the actors is merely relabelling. Q8 asks what the
local group at an event is. Q9 asks what survives the quotient. This section
measures what those groups do to the substrate census, and it stops short of
answering them, because the answer they want is an operational one and the corpus
has no operational observables yet. The status column below says what was
measured and nothing more.

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
search over the whole symmetric group, and it is the automorphism group of the
link structure not merely in order but AS A SET of permutations of the nine
actors, both inclusions checked. The link structure is complete multipartite on
three parts of three, so that order is also the closed form the parts give, and
the instrument gates the two against each other. The arena's own group sits
inside it, and the index is the record's residue. The parent's naming census says
the same from the record's side:

> the record admits 1,296 namings of the derived cast and 108 of them carry the
> declared direction classes

Those two are the record's own numbers, read from its side of the same fact.

**The index is a theorem.** The two twelves -- the index the round law's
stabilizer has over the smaller group, and the number of splittings the record
offers -- are the same twelve by orbit-stabilizer, and the instrument measures
each leg. The link
group's action on the splittings has one orbit, so the action is transitive; the
stabilizer of the declared splitting inside that group is the arena's own group,
again as a set and not only by order; and orbit times stabilizer returns the
order of the whole. The paper's earlier reading -- that the two numbers coincide
-- is weaker than the fact.

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
coherent assignments than global ones; at and above it the two agree. The table
is one history of the strict-cover corpus; the instrument additionally verifies
that the collapse width and the global count are the same at all seventy-two of
that corpus's histories, and the concatenation and window corpora are outside
this sweep. That is a counting fact about window widths, and it is what the
status column reports. What would upgrade it -- for this group and for every
other row of the table -- is the every-observable standard: a set of operational
observables, an experiment for each, and a demonstration that all of them take
identical values across the orbit. The programme does not have that yet.

The structure those groups act on is the one the separation census measured:

> The graph is therefore complete multipartite with those three lines as its
> parts, and every site has degree six

**What survives.** Quotienting by a group is only interesting if something is
left. The instrument counts the orbits of the corpus's own objects under the
arena's automorphisms and under the link structure's -- and it counts them on
one object at a time, which the first delivery did not.

| object | before | modulo the arena | modulo the links |
|---|---|---|---|
| histories, order kept | 5,784 | 3,830 | 1,067 |
| event multisets, order forgotten | 136 | 25 | 17 |
| count fields | 36 | 12 | 12 |

The first row is the object the census defines: a history is a SEQUENCE of
events, and the group acts on it without disturbing the order. The second row is
a different object. Forgetting the order maps the 5,784 histories onto 136 event
multisets, and that step is done by sorting and not by any relabelling; the
automorphisms then carry 136 to 25 and to 17. Crediting the automorphisms with
the whole fall from 5,784 to 17 would credit them with a collapse of which they
supply eightfold.
Both chains are published, and the head carries both.

The count fields collapse to the same number under both groups -- the extra
freedom the link group has over the arena group merges no further count field.
So what the substrate census leaves after the quotient is the link structure
itself, the orbit of the history under it, and the count field up to that orbit.
Whether that is the physical content is exactly what the withheld word withholds.

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
| RECORD-BLOCK | ACTOR | the reconstruction reads a cast off the blocks |

It cannot. The construction is circular, and at the committed corpus the record
admits exactly one cast inside the triangular representation class. Two of the
graph's cycles run through both the cast and the record, and the shorter of them
is the one Q4 names: an actor makes an event, an event makes a history, a history
writes a record block, and the record block hands the actor back. That circle is
four edges long, and the head carries its length under its own name; the
shortest cycle in the graph is a different one, the three-edge dynamical loop
from the count field through the amplitude and the emission and back.

Q5 asks whether that circle closes. Here is the measurement. Strip the labels;
keep only which tokens each event wrote; then ask for every family of token sets
under which each record block is a triangle carrying no foreign token. The search
leaves the number of actors free, introduces a fresh actor whenever the
constraints permit one, and collects solutions as families rather than as
labelled structures, so two that differ by a renaming count once. It returns
exactly one family, and that family is the declared cast, as sets.

The search offers each token after the first only one fresh label, and that is
exhaustive exactly when every token shares a block with one already assigned --
that is, when the record's block hypergraph is connected. The instrument measures
the number of components and gates it at one, so the exhaustiveness claim does
not travel silently to a record where it would fail.

That is uniqueness inside a declared representation class, and it is not a fixed
point of the actor-record-emission dynamics. The class is the one the search
declares -- families of token sets in which every record block is a triangle --
and the result says that inside it the record leaves no choice. It does not say
that the coupled dynamics, run forward from the recovered cast, returns the
record it started from; that composition is the autonomous-update unit's object
and is untouched here.

What the record does not fix is the direction declaration, and the residue is an
index the record offers and does not choose. The reconstructed link structure
admits several splittings into direction classes; the declared splitting is one
of them; the record supplies the structure and leaves the splitting open.

The uniqueness is a corpus fact and not a per-history one, and the sealed unit
that first measured the reconstruction says why:

> no committed history sees more than 18 of the 27 record blocks

---

## 5. Q58: emergence, or identifiability?

The question the pin sends this unit to settle is whether the reconstruction
settles the emergence question in the strong direction, or only shows that latent
actors can be identified in a model that already used them to write its data. The
pin asks for the discriminating measurement: run the same reconstructor on
records written by a different admissible mechanism.

The corpus supplies several. Three committed drivers write the same corpus by
different routes. A grammar-free mechanism writes the blocks of every group whose
members are pairwise linked, with no schedule at all. Another writes the blocks
of every group of the declared arity, admissible round or not. Another writes
only the two-cell blocks. And the coupled dynamics writes its own record: one
emitted cell per step, which is a co-division pair rather than a group of the
declared arity, at two grains -- the emitted cell, and the site menu the emission
law weights.

| mechanism | kind | the record it hands over | actors per event | blocks | block sizes | certificate | cast recovered |
|---|---|---|---|---|---|---|---|
| THE-COMMITTED-GRAMMAR | GRAMMAR | RECORD-1 | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-STRICT-COVER-DRIVER | GRAMMAR | RECORD-1 | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-CONCATENATION-DRIVER | GRAMMAR | RECORD-1 | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-DRIVEN-WINDOW | GRAMMAR | RECORD-1 | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-PAIRWISE-LINKED-GROUPS | GRAMMAR-FREE | RECORD-1 | 3 | 27 | 27 x 3 | CERTIFIED | yes |
| THE-UNRESTRICTED-GROUPS | GRAMMAR-FREE | RECORD-2 | 3 | 81 | 54 x 2+27 x 3 | TOKEN-NOT-IN-EXACTLY-TWO | no |
| THE-NON-COLLINEAR-GROUPS | GRAMMAR-FREE | RECORD-3 | 2 | 54 | 54 x 2 | TOKEN-NOT-IN-EXACTLY-TWO | no |
| THE-COUPLED-WALK-EMISSION | DYNAMICS | RECORD-4 | 2 | 27 | 27 x 1 | THRESHOLD-UNDETERMINED | no |
| THE-COUPLED-WALK-SITE-MENU | DYNAMICS | RECORD-5 | 2 | 9 | 9 x 3 | THRESHOLD-UNDETERMINED | no |

**The probe's width.** The reconstructor reads its block set and nothing else --
no schedule, no grammar, no corpus label -- so the column that matters is the
third. The nine arms hand the reconstructor five distinct block sets between
them, of which one recovers the cast and four refuse. The five recovering rows are identical in every column
because they are one measurement: four schedules and one grammar-free rule write
the same record, the twenty-seven triangles, and the reconstructor cannot tell
them apart. What was measured is therefore a criterion separating one recovering
input from four refusing ones, and the head carries the arm count and the input
count side by side.

**Two refusals, not one.** The four refusing arms fail in two different ways,
and the summary above says which. Where the two-cell blocks are present the
rule runs and its own membership certificate rejects the cast it built. Where
the emitted blocks are single cells there is no co-writing at all, so the rule
has no meet to threshold and declines to invent one; where the blocks are stars
at a site the same thing happens for a different reason. Those last two are
both grains of one dynamics, and the word refuse is the reconstructor's own
declared branch for them -- it returns no cast rather than choosing one -- so
it may not be read as saying that the cast is unidentifiable from the coupled
walk's record, only that this rule cannot act on a record with no co-writing.

Block size alone is not the criterion, and the instrument gates that it is not:
one refusing arm writes blocks of the declared arity and still refuses, because
its blocks are stars at a site rather than triangles among three actors.
Triangularity with every token covered is what separates these arms.

**And it is not sufficient off them.** The instrument does not stop at the arms.
It runs the same reconstructor over a declared family of block sets built from
the record's own triangles, and measures what the criterion does there.

| block set | blocks | all blocks triangular | tokens covered | certificate | cast recovered |
|---|---|---|---|---|---|
| all the triangles | 27 | yes | 27 | CERTIFIED | yes |
| the smallest covering prefix | 23 | yes | 27 | TOKEN-IN-NO-ACTOR | no |
| the triangles less the first block | 26 | yes | 27 | TOKEN-IN-NO-ACTOR | no |
| the triangles less a middle block | 26 | yes | 27 | TOKEN-IN-NO-ACTOR | no |
| the triangles less the last block | 26 | yes | 27 | TOKEN-IN-NO-ACTOR | no |
| a prefix of 4 triangles | 4 | yes | 9 | TOKEN-IN-NO-ACTOR | no |
| a prefix of 8 triangles | 8 | yes | 14 | TOKEN-NOT-IN-EXACTLY-TWO | no |
| a prefix of 12 triangles | 12 | yes | 19 | TOKEN-IN-NO-ACTOR | no |
| a prefix of 16 triangles | 16 | yes | 24 | TOKEN-IN-NO-ACTOR | no |
| a prefix of 20 triangles | 20 | yes | 25 | TOKEN-IN-NO-ACTOR | no |
| a prefix of 22 triangles | 22 | yes | 26 | TOKEN-IN-NO-ACTOR | no |
| the triangles and one two-cell block | 28 | no | 27 | CERTIFIED | yes |

The reconstruction is not generator-independent. Of the mechanisms the corpus
supplies, those whose blocks are triangles covering every token recover the
cast and the others do not, so triangularity with total cover decides every
arm. It is not a sufficient condition beyond them: the domain probe exhibits
triangle-writing block sets at total cover on which the rule does not return
the declared cast, and one non-triangular block set on which it does, so the
criterion is stated as what separates these arms and not as a property of
mechanisms.

So the answer to the emergence question is identifiability within a generative
class. The class is not the committed schedule -- the record the four other
mechanisms write is the one the committed grammar writes, and one of them has no
grammar at all -- but it is a class, and its boundary is measured rather than
assumed. The corpus's one autonomous dynamics is outside it. And the standing
wall applies with full force here: every record these arms read was written by a
mechanism that already had the cast in hand, so what is measured is how widely
the cast can be identified, never that the cast was selected among worlds that
lacked it.

---

## 6. The parameters

Q10 asks whether ISP is one theory or a family. Q24 asks whether, if nothing
selects its quantities, the theory can say so cleanly. Here is the clean saying:
every declaration this census reaches -- including the scheduling convention and
the chart type, which section one classes declared and the first delivery did not
price -- its fiber where a fiber has been measured, its class, and whether any
measured law selects it.

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
| the tick | the scheduling convention | DECLARED | FREE | NO | HOR |
| the chart | the two-sector overlap type | SEALED-CITATION | FREE | NO | SEC |
| L | which classes are declared links | COMPUTED-HERE | INVARIANT-IN-THE-SUBSTRATE-CENSUS | NO | AID |
| the coordinate | the naming of the record tokens | ANY-BIJECTION | INVARIANT-IN-THE-SUBSTRATE-CENSUS | NO | REC |
| n | the actor count | COMPUTED-HERE | RECONSTRUCTED-CONDITIONALLY | NO | THIS-UNIT |
| the cell count | the carrier size | COMPUTED-HERE | DERIVED | YES | THIS-UNIT |
| the connection | the group the walk's phases live in | DECLARED | DERIVED | YES | COUPLING |
| the menu | the admissible actor grains | COMPUTED-HERE | DERIVED | YES | FAC |
| the state | the initial amplitude | AN-INITIAL-CONDITION | INITIAL | NO | COUPLING |
| the record | the initial count field | AN-INITIAL-CONDITION | INITIAL | NO | COUPLING |

Three rows are DERIVED and say so, each carrying the measured predicate that
selects it; two are invariant in the substrate census; one is reconstructed
conditionally; two are initial conditions; and the rest are free.

The selection column is not a label. Each row that reads YES names a predicate
this run evaluates -- the carrier size against the product of the actor count and
the link count, the walk's phase group against the field's own roots of unity,
the admissible grains against the translation subgroups -- and the gate requires
the DERIVED count and the number of satisfied predicates to be the same number.
A row that reads NO names no predicate, and that is the honest content of the
word free: not that no law could select it, but that no law the sealed corpus has
measured does.

One row is RECONSTRUCTED-CONDITIONALLY, and it is the actor count. It is not
derived and no law selects it: it can be read back off records written inside the
triangular class of section five, and outside that class it cannot, so its status
is conditional on the mechanism that wrote the record. The two invariant rows are
the direction declaration, priced in section three, and the coordinate on the
record's tokens -- and the coordinate is priced here rather than cited: the
record is re-emitted in a second, unrelated naming of its tokens and the
reconstruction is run again, returning the same cast under that naming.

The verdict word follows from the count and not from a judgement: with a positive
free count the comparator writes the family word. That is the honest statement
Q24 asks for. It is not a defeat and it is not a boast; it is the inventory. What
the table's own authorship contributes is the row list and the fiber column;
the class column and the selection column are computed from the predicates named
above, and the census-to-table reconciliation is gated, so no object the census
calls declared can go unpriced here.

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
than to a sentence boundary. The parent that swept the arena size says as much of
its own numerals, and its sentence carries no numeral at all, which is why the
census gate does not let it back a cardinality:

> NO TESTED NUMERAL IS REPRODUCED BY THE DECLARED n-ONLY READING

That is the parent's word, and it is a word and not a count.

---

## 7. What this does not say

The census is at one arena and over the committed corpus. Nothing here is a
theorem about records, casts or theories at large, and the uniqueness result in
particular is a statement about this record inside this representation class.

The census counts named rows. Three of its rows are re-descriptions the weld's
dictionary and the carrier typing identify with rows already present, so the
extents behind the names are fewer than the names, and both numbers are in the
head.

The state list is the list the committed machine needs. A unit that declared a
different dynamics would owe its own list, and the sufficiency measurement would
have to be redone; what transfers is the method, which is that a list earns the
word sufficient by screening the history off the update. The screening table's
minimality leg is stamped to the uniform amplitude and measured to fail
elsewhere in the declared state space; its sufficiency leg is structural and
holds everywhere probed.

The invariance census measures invariance of the substrate census. It does not
license a gauge quotient, it does not say which relabellings are unobservable in
any operational sense, and it does not say that the symmetric group's other
elements are observable either. Those are operational questions, and the corpus
reaches them only when an observable and an experiment exist to ask them of. The
local-group table is one history of one committed corpus, uniform across that
corpus's seventy-two histories and not swept over the other two.

The saturation predicate compares the covered-cell count with the actor count,
and that comparison is an identity only at the declared arity; what the law says
structurally is that every group is a triangle, and the instrument gates the two
readings against each other so that the coincidence is not carried to another
arity as a formula.

The parameter table's fibers are measured where the fiber column says computed
and declared where it says declared. An unswept row is unswept: it is not a claim
that the quantity could not be swept, only that the sealed corpus has not swept
it, and two of those rows are the charter of the next unit.

The mechanism arms are a domain probe, not a classification of mechanisms. Nine
were run because nine are in the corpus; they hand the reconstructor five
distinct records between them; and the criterion they suggest is stated as what
separates those records, with a measured family of counterexamples showing it is
not sufficient beyond them.

The instrument ships a paper-free diagnostic mode. It skips the four gates whose
object is the paper, writes nothing, prints a banner saying so on both streams
and exits with a code of its own, so no run of it can be scored as a delivery.

---

## 8. The instrument

`v15/code/contract_exact.py`. Five code regions -- builder, stripper,
reconstructor, comparator, and the unprefixed plumbing -- and three machine
checks over them. The first is a reach audit: no reconstructor and no comparator
function reaches a builder or a stripper at any depth, and the walk is transitive
through the plumbing, so a route by way of a helper is still an offence. The
second closes the routes that leave no call edge at all: inside any stripper,
reconstructor or comparator, name assembly through `globals()`, `getattr`,
`sys.modules` or `importlib`, the two evaluators, and any string constant
spelling a builder's or a stripper's name are forbidden outright. The third
names every declared-side constant this module carries and forbids the three
non-builder regions from mentioning one, case-insensitively, so a shouted
constant cannot pass as plumbing. The plumbing is not policed for reach and holds
most of the module's functions; that is why the reach audit runs through it
rather than around it. That is the corpus's registered S-1 family, answered by
construction rather than by promise, and the reconstructor is shown to have teeth
by refusing four of the nine mechanisms, the comparator by rebuilding the verdict
from the serialized receipt alone.

The head is not trusted to its renderer, and the check is total by construction.
Every `KEY=` position present in the emitted string is parsed back out by a
reader that shares no code and no literal with the builder, and compared, as an
integer, against the receipt leaf it names -- including both halves of every
compound `A-OF-B` value, which the first reader stopped at the hyphen and never
saw. A position the string carries and the field table does not name is a stray
and fails the gate, so the count of positions parsed is a measurement of the
string and not the size of the expectation table.

The pre-registered outcome words are all reachable, and reachability is
demonstrated in the delivery run rather than argued: each word is emitted by the
real comparator on an input this run computed, and each row says in its own
words what would make this corpus read it.

| pre-registered word | witness | what would make this corpus read it |
|---|---|---|
| CENSUS-TOTAL | MEASURED-HERE | the delivered census: every row's cardinality key is carried by this run, so no row resolves NONE |
| CENSUS-PARTIAL | MEASURED-HERE | the same builder over a payload from which one cited cardinality has been withheld: that row resolves NONE and the word falls |
| ACYCLIC | MEASURED-HERE | the same dependency graph with its two feedback edges cut has no cycle at all, so a corpus that never wrote a record back would read here |
| CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS | MEASURED-HERE | one declared direction class of the same record offers exactly one splitting, so a record with no direction residue reads here |
| CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS-UP-TO-THE-DIRECTION-DECLARATION | MEASURED-HERE | the delivered measurement: one cast family and a direction residue above one |
| CIRCULAR-BLOCKED-AT-THE-CAST | MEASURED-HERE | the covering-prefix probe of section five does not return the declared cast, and a corpus whose whole record read like it would read here |
| Q58-EMERGENCE-GENERATOR-INDEPENDENT | MEASURED-HERE | restricted to the arms that write triangles the corpus already shows no refusal, so a corpus whose every mechanism wrote triangles would read here |
| Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS | MEASURED-HERE | the delivered measurement: more than one arm recovers and at least one refuses |
| Q58-UNDECIDED-NO-SECOND-MECHANISM | MEASURED-HERE | restricted to the arms that do not write triangles no arm recovers, so a corpus supplying only those would leave the question open |
| ISP-IS-ONE-THEORY | MEASURED-HERE | the word reads at a free count of zero; the free count is computed from the selection predicates, of which this corpus satisfies every one it declares and declares none for the rows that stay free |
| ISP-IS-A-FAMILY | MEASURED-HERE | the delivered measurement: the free count is positive |

The two standing walls are built as walls and not as prose. Their patterns are
frame-general regular expressions over the canonicalised paper -- a subject
class, a bounded gap, a verb class, a bounded gap, an object class -- so a
paraphrase has to change what the sentence says to get past them. Their standing
sentences must be carried or the run fails. Beyond the patterns, all seven walls
switch on the licence leg the template ships: each wall declares a promotion
vocabulary, and any sentence of the paper carrying one of those words must also
carry a rendered claim, which is a gated string. No wall may license its own
policed word, so each wall's licence pool is the claim set minus every claim
carrying that vocabulary, and the gate requires the pool to be non-empty. The
walls' controls are eighteen sentences drafted from the violation rather than
from the pattern list -- the sixteen paraphrase families and the two re-voicings
the hostile round planted -- and each is planted into the delivered paper, one at
a time, and required to die at the wall it names. The unit's own falsifier for
this gate shares no literal phrase with any pattern and dies at the licence leg.
The programme's own engraving is read at its pinned bytes and consumed by the
wall gate, which parses the engraved indices out of the located text and compares
their number with the standing walls this run built:

> **W1**: reconstruction is never promoted to derivation. **W2**: invariance is
> never promoted to gauge or physical meaning before operational observables
> exist

The programme's third wall is engraved for the units from event-and-carrier
closure onward, and this unit makes no family-level prediction to instrument it
against.

The nine template families are imported from the era's reference implementation
and USED: each family's entry point is counted at its own call site as the run
executes, and the gate compares that execution census with the families the mode
is expected to exercise -- not a regular expression over this module's source,
which a class that is never instantiated or a token left in a comment can
satisfy. The falsifier family is exercised on the delivery path itself: the
template's harness is handed a copy of this run's payload and a real recipe, and
the harness, not this module, checks that the recipe moved its declared target
and died at its declared gate. In the paper-free mode the four families whose
object is the paper are declared out of mode and counted as such.

Gate-time seals verified at the door with totality recomputed there, each key
sealed at the gate whose predicate reads it, over a seal partition the run proves
total; the transcript reconciled with the ledger by content, its stray and
missing counts measured from the multiset difference rather than typed, its
digest sealed as a payload leaf and the promoted bytes re-read from disk and
compared against that seal, so a transcript edited after binding cannot reach the
tree; verbatim anchors consumed by their named gates, all but one of them with a
numeral parsed out of the located text -- nine in digits, two spelled in words,
one an engraved index -- and the last declared word-bound and gated so that it
backs no published cardinality; claims, tables and fenced blocks by two-way
equality keyed by table, with the sentences whose count is written in words
rendered from the payload so that inverting the words fails there; referent
binding per occurrence over prose, run twice, once on the digits and once on the
same prose with its spelled numerals rewritten as digits, and a third leg that
scores every universe a sentence names and requires its numerals to belong to all
of them; no typed numeral anywhere in the subtree of a sentence builder, with
three scans -- the direct one, the one for a numeral reaching a builder through a
format string or an integer offset, and one for an integer-valued module constant
reaching a builder at one remove; falsifiers that must move the measured key they
name and die at the gate they name, one per gate, with a single waiver whose
forcing is machine-checked; and the read set recorded at an audit hook on the
open event, reconciled at the last gate and re-evaluated once more at the door.

The falsifier denominator is stated rather than folded: thirty-four recipes cover
the thirty-four ledger gates, the coverage check itself is the one waiver, and
the nine template checks are load-bearing kill paths outside this ledger, so the
honest denominator is forty-four and the era's own reference demos falsify the
nine.

The command line is strict at every position: each flag's operand arity is
declared and an argument list longer than its flag allows exits two, so a mutant
name after a mode flag cannot yield a clean delivery.

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
| v15/PLAN.md | 754e075c4a0e |
| v15/note-contract-pin.md | 438586c11db5 |

The two objects that cannot be pinned against themselves are the instrument,
whose own syntax tree its gates audit, and this paper, which is the object under
test.
