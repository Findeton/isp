# ARE ACTORS DERIVED?  THE IDENTITY-RECONSTRUCTION CENSUS

**AID / paper-33, v14.**  Code `v14/code/aid_exact.py`; transcript
`v14/code/aid_output.txt`; receipt `v14/code/aid_receipt.json`.  Pin
`v14/note-aid-pin.md`.  Parents: paper-19 (the weld dictionary and the
driven records), paper-21 (the window and the R = 6 door), paper-20 (the
coupled walk).

```
AID-STRATIFIED-AT-THE-ROUND-MEET-[IDENTITY FORCED ON 5,852 OF 5,856 COMMITTED HISTORIES, CHART ON 4] -- CENSUS=C1 72 OF 72 TRIVIAL | C2 5,184 OF 5,184 TRIVIAL | C3 596 TRIVIAL AND 4 AT ORDER 216 WITH ORBIT SHAPE 3+3+3 -- ROUTES=THE S_9 FILTER AND THE YOUNG SUBGROUP AGREE AT ORDER ON ALL 41,347 DISTINCT PREFIXES AND AT ELEMENT SET ON 703, 0 MISMATCHES
```
```
CRYSTALLIZATION=EXACTLY 5 ON C1, C2 AND THE 1,944-HISTORY SEED FAN (UNIFORM, NOT AN AVERAGE) | C3 STRATIFIED 5:404|7:36|8:144|11:12|never:4 | NEVER 4 = THE CONSTANT-CLASS QUADRUPLES ANT|ANT|ANT|ANT,COL|COL|COL|COL,DIA|DIA|DIA|DIA,ROW|ROW|ROW|ROW -- PREFIX-LAW=A CONCATENATION CRYSTALLIZES EXACTLY WHEN ITS FIRST FACTOR DOES, 0 DISAGREEMENTS OF 5,184; THE STABILIZER NEVER GROWS, 0 GROWTH EVENTS IN 2,000 PREFIXES
```
```
INVARIANCE=SPLIT -- BLIND-BY-THEOREM: THE CO-DIVISION RELATION (0 VIOLATIONS OVER 121,152 STABILIZER ELEMENTS AT 703 OBJECTS) AND EVERY WELD-DICTIONARY READING (121,152 PARSE COMPARISONS, 0 DIFFERENCES) -- NOT-BLIND-BY-MEASUREMENT: THE RECORD'S ATTRIBUTION (ORBIT-CONSTANT AT 111 OF 703, NAMING-DEPENDENT AT 592) AND THE WALK'S BORN MENU (134,58,58,58,58 BY DEPTH) -- THE WALK STRICTLY REFINES THE RECORD FROM DEPTH TWO: 53 OBJECTS THE RECORD CANNOT SEPARATE AND THE WALK CAN, 23 THE RECORD SEPARATES AND THE ONE-STEP MENU CANNOT
```
```
WALK-SYMMETRIES=EXACTLY THE TRANSLATIONS (813 OF 121,152 ELEMENTS; SHIFT-COMMUTING EQUALS TRANSLATION AT EVERY ONE, 0 DISAGREEMENTS; RECORD-PRESERVING 51,769) -- DEGENERACY=THE RELATION FORGETS WHAT THE SEQUENCE REMEMBERS: AT 24 OF 600 R = 4 HISTORIES THE CO-DIVISION RELATION IS THE CONSTANT COMPLETE GRAPH WITH AUTOMORPHISM GROUP 362,880 WHILE THE STABILIZER OF THE ORDERED HISTORY IS TRIVIAL
```
```
SCOPE=THE GLOBAL-RELABELLING GRAIN ONLY; THE GROUPOID GRAIN REGISTERED AND NOT RUN -- MEASURE=COUNTING-ONLY UNDER TWO DECLARED MEASURES (E-24): THE RECORD'S BLIND FRACTION IS 3/19 BY DISTINCT PREFIX AND 1235/6008 BY CORPUS MULTIPLICITY, THE WALK'S 58/703 AND 2065/24032 -- WINDOWS=W-C1,W-C1FAN,W-C2,W-C3,W-DRIVE,W-AUTC2,W-WALK, FOUR OF THEM ENTIRE CLASSES -- LANGUAGE=FORCED/CHART/STRATIFIED NAME THE STABILIZER AND THE INVARIANCE DATA AND NOTHING ELSE
```

## 1. THE QUESTION, AND THE OBJECT THAT ANSWERS IT

The corpus defines an actor as an identity that recurs in the record.
That definition is a naming convention until something forces it.  The
Barandes-orthodox form of the worry is exact: a decomposition of a
system into subsystems is a factorization CHOICE unless the law picks it
out. Here the question can be asked of a committed object rather than
argued.

A committed history is a sequence of division events, and each division
event is a subset of the actors.  Relabel the actors by a permutation of
the nine and the history becomes another history.  THE STABILIZER of a
history is the subgroup of the symmetric group on the nine actors that
carries the event sequence to itself, event by event and in order.  If
that subgroup is trivial, the labelling is reconstructible from
participation alone and identity is FORCED on that history.  If it is
not, the labelling carries information the history does not, and to that
extent identity is CHART.  The fiber is the stabilizer itself.

Three things follow that make this a measurement rather than a position.
The stabilizer is computable exactly.  It has a closed form, proved in
section 4 and verified against brute force, that turns the question into
a statement about participation patterns.  And the observables the
corpus has already committed -- the record, the weld dictionary's
readings, the coupled walk's Born menu -- can be evaluated ON the
stabilizer, which asks whether any of them depends on the part of the
labelling that is not forced.

Two words are used throughout with exactly one meaning each.  FORCED
names the measured fact that a history's stabilizer is trivial.  CHART
names the measured fact that it is not.  Nothing in this unit asserts
anything further about actors, and the reading walls in section 9 scan
this paper for sentences that would.

## 2. THE CORPORA AND THE DECLARED WINDOWS

The arena is the one the parents committed: the nine sites of AG(2,3),
the three declared link directions, and the 27 cells.  Of the 280
groupings of the nine sites into three triples, 36 saturate the
per-round incidence budget; 72 ordered triples of those are I7-STRICT at
R = 3, 276 ordered quadruples induce I7's G-FLAT row, and paper-21's
driven window carries 600 schedules.  Every one of those numbers is
recomputed in this run and gated against the parent receipt that
published it, row by row.

Three corpora carry the census, and each is a parent's own object: the
three committed corpora carry 72, 5,184 and 600 histories.

The seed fan deserves a word.  Within a round the three conflict groups
enter the history in ascending order of their seed's site index, so a
schedule's seed choice moves the ORDER of the events without moving the
events themselves.  The fan takes the same 72 triples at all 27
canonical transversal triples: 1,944 histories, 432 distinct sequences
over 12 distinct event sets.  It exists so that the order axis is
exhausted rather than fixed.

Because a stabilizer is defined on every prefix and not only on a
completed history, the census runs over 101,160 prefix objects, 41,347
of them distinct.

### 2.1 The windows, declared in-string

| window | declaration |
|---|---|
| W-C1 | THE 72 R = 3 I7-STRICT TRIPLES, ENTIRE.  Every ordered triple of saturating groupings whose summed link field covers all 27 cells; driven at the FIRST canonical transversal of each round.  No sampling: the corpus is the whole class. |
| W-C1FAN | THE SEED FAN OVER W-C1, ENTIRE.  The same 72 triples at ALL 27 canonical transversal triples, so the seed axis -- the only coordinate that moves the WITHIN-ROUND event order -- is exhausted rather than fixed. |
| W-C2 | THE 5,184 ORDERED R = 6 CONCATENATIONS, ENTIRE.  Every ordered pair of W-C1 triples, concatenated -- paper-21's own R = 6 door, at its own ordered-witness count. |
| W-C3 | PAPER-21's DRIVEN WINDOW W4, ENTIRE.  All 600 committed schedules -- W4-CLASS, W4-FLAT, W4-SEEDFAN and W4-CTRL -- reconstructed here by paper-21's own constructor and gated against its committed window size. |
| W-DRIVE | THE DRIVEN VERIFICATION SET.  The committed v10 layers are expensive to drive, so the driven leg is taken on a DECLARED set: the first 9 W-C1 triples in enumeration order, the four constant-class W-C3 quadruples together with d66's own committed R = 4 point and the collinear arrangement, and the first 2 W-C2 concatenations.  Each is compared event by event against the combinatorial route, and the structural leg carries the rest. |
| W-AUTC2 | THE AUTOMORPHISM WINDOW OVER W-C2.  The co-division automorphism group is enumerated on the 72 DIAGONAL concatenations (T, T) -- paper-21's own R = 6 witness form -- rather than on all 5,184. |
| W-WALK | THE WALK'S DEPTH.  Paper-20's coupled step is re-implemented here and run to depth 5 from the S_9-symmetric start; every depth is published, so the depth is not a hidden cap. |

### 2.2 The corpora

| corpus | histories | events per history | window |
|---|---|---|---|
| C1-R3-TRIPLES | 72 | 9 | W-C1 |
| C1FAN-SEED-FAN | 1,944 | 9 | W-C1FAN |
| C2-R6-CONCATENATIONS | 5,184 | 18 | W-C2 |
| C3-R4-WINDOW | 600 | 12 | W-C3 |

## 3. THE DRIVEN LEG

Nothing above is licensed until the combinatorial history is shown to be
the DRIVEN one.  The unit therefore drives the committed v10 layers
directly -- d42b1's menu, d60's builder, d66's conflict-grid cycle -- on
a declared verification set, and compares the register footprints of the
division events, event by event and in order, with the combinatorial
group sequence.  This is strictly stronger than the licence paper-21
took, which compared the summed link field: here the SEQUENCE is the
object, and the sequence is what a stabilizer acts on.

The structural leg runs first.  d42b1's `regs_of` is parsed and its
arbitration branch read off its own source: the register set of a
division event is the union of the proposer names in the conflict key
with one derived value name, and the proposers of an arbitration are
exactly the conflict group.  Paper-19's `record_of` cuts the value name
away by restricting to the nine actor objects, so the footprint is the
group.  The empirical leg then confirms it at every schedule of the
drive set, with `maxhits` equal to 1 everywhere: every event is
specified by its full tuple, so the layer's tie-break -- which is
hash-seed dependent and the subject of the v10 defect register -- is
never consulted.  The negative fate is exercised too: with its first
conflict-supply delivery withheld the collinear arrangement is REFUSED
by the committed layer, at ('propose G10', 14), so "no refusals" above
is a measurement.

| window | rounds | events | divisions | maxhits | footprints equal groups |
|---|---|---|---|---|---|
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C1 | 3 | 48 | 9 | 1 | True |
| W-C3 | 4 | 48 | 12 | 1 | True |
| W-C3 | 4 | 48 | 12 | 1 | True |
| W-C3 | 4 | 48 | 12 | 1 | True |
| W-C3 | 4 | 48 | 12 | 1 | True |
| W-C3 | 4 | 66 | 12 | 1 | True |
| W-C3 | 4 | 60 | 12 | 1 | True |
| W-C2 | 6 | 102 | 18 | 1 | True |
| W-C2 | 6 | 102 | 18 | 1 | True |

## 4. THE STABILIZER, BY TWO ROUTES

Route A knows nothing but the definition.  It holds the 362,880 elements
of the symmetric group on nine letters and filters them: an element
survives an event when it maps that event's actor set to itself.  Route
B computes the PARTICIPATION SIGNATURE of each actor -- the pattern of
events it belongs to -- and returns the Young subgroup of the partition
into equal signatures, the product of the symmetric groups on its
blocks.

Route B is a theorem, and the theorem is the content of this section.
Fixing every event setwise is the same as fixing every atom of the
Boolean algebra the events generate, because an atom is an intersection
of events and complements and a permutation that fixes each of those
fixes their intersection; conversely every event is a union of atoms.
The atoms are exactly the signature blocks.  So the stabilizer is the
Young subgroup, its order is the product of the block factorials, and
identity crystallizes exactly when every actor has its own signature.

The two routes are compared per object rather than in aggregate: at
order on all 41,347 distinct prefixes of the four corpora, and at
element set -- the actual subgroups, compared as sets of permutations --
on the 703 where the group is nontrivial.  Measured, the two stabilizer
routes disagree at 0 objects.

| order | distinct prefixes |
|---|---|
| 2 | 60 |
| 4 | 108 |
| 8 | 270 |
| 24 | 66 |
| 216 | 181 |
| 4320 | 18 |

| orbit shape | distinct prefixes |
|---|---|
| 1+1+1+1+1+1+1+2 | 60 |
| 1+1+1+1+1+2+2 | 108 |
| 1+1+1+2+2+2 | 270 |
| 1+1+2+2+3 | 66 |
| 3+3+3 | 181 |
| 3+6 | 18 |

The orbit shapes are the partition of the nine actors into
indistinguishable classes, and the cycle types of the stabilizer
elements are published in the receipt: 23 distinct types over 121,152
elements.

## 5. THE CRYSTALLIZATION TIME

The answer is stratified rather than uniform: identity is forced on
5,852 histories and chart on 4.  The four exceptions are not scattered.
They are characterised and not merely counted: 4 histories never
crystallize, and they are the constant-class quadruples ANT|ANT|ANT|ANT,
COL|COL|COL|COL, DIA|DIA|DIA|DIA, ROW|ROW|ROW|ROW.

The R = 3 and R = 6 corpora return a CONSTANT.  Measured, the
crystallization time is exactly 5 on C1, C2 and the seed fan -- not the
third event, which would be the end of the first round, and not the
ninth, which is the end of the history.  The route to it is the same at
every history of both corpora, and it is the route rather than any
geometric special case that explains the constant.  The stabilizer order
by prefix length is [4320, 216, 216, 8, 1, 1] at all 72 R = 3 triples
and at all 5,184 concatenations.  The first event leaves the Young
subgroup of a three-set and its complement. The second cuts it to three
blocks of three.  The THIRD ADDS NOTHING: a round's last group is the
complement of its first two, so it separates nothing the round has not
already separated.  The fourth leaves three singletons and three pairs,
and the fifth splits all three pairs at once.  The mechanism is measured
and not assumed: at every history of the corpus the fourth and fifth
events each meet every first-round group exactly once -- they are
transversals of the first round -- which is what makes the drop from 216
to 8 to 1 happen where it does.

The remaining four events of an R = 3 history, and all nine of the
second factor of an R = 6 one, add nothing to identity.  That is the
prefix law: a stabilizer can only shrink when an event is appended, so
the crystallization time is decided by the earliest prefix that reaches
triviality.  Measured, the stabilizer never grew at any of the 2,000
prefixes checked, and each of the 5,184 concatenations crystallized
exactly when its first factor did.  The R = 6 corpus is therefore not a
second sample of the same quantity; it is a test of the law, and it
passes.

| corpus | 5 | 7 | 8 | 11 | never |
|---|---|---|---|---|---|
| C1-R3-TRIPLES | 72 | 0 | 0 | 0 | 0 |
| C1FAN-SEED-FAN | 1,944 | 0 | 0 | 0 | 0 |
| C2-R6-CONCATENATIONS | 5,184 | 0 | 0 | 0 | 0 |
| C3-R4-WINDOW | 404 | 36 | 144 | 12 | 4 |

## 6. THE PHYSICS-INVARIANCE CENSUS

Where the stabilizer is nontrivial there are two namings of the same
history, and the question is whether any committed observable can tell
them apart.  The census is taken on every prefix whose stabilizer is
nontrivial -- 703 of them, carrying 121,152 stabilizer elements between
them -- because a history that crystallizes at its fifth event still has
four prefixes at which identity is not yet forced.

The distinction that organises the whole section is between an
observable as a FIELD over the arena and the same observable as a
PROPERTY OF A THREAD.  Two namings that differ by a stabilizer element
produce the same labelled history, so any field computed from the
history is literally the same object under both.  What differs is which
thread sits at which site.  A field is therefore always invariant; an
attribution is well defined only when the field is constant on the
stabilizer's orbits.

### 6.1 The weld's link generator is blind, by theorem

Paper-19's dictionary reads site from ACTOR, link from the co-division
actor pair, count from the division count.  Its link generator is the
co-division relation: the number of division events whose footprint
meets both endpoints of a pair.  A stabilizer element fixes every event
setwise, so an actor belongs to an event exactly when its image does,
and the co-division count of a pair is carried unchanged.  Measured, the
co-division relation is preserved by every one of the 121,152 stabilizer
elements, at 0 violations.

The same argument closes the dictionary's readings.  The induced count
field reads the co-division relation through a parse; precomposing that
parse with a stabilizer element leaves the field entry for entry,
because the element is an automorphism of the relation the field reads.
Measured, the weld dictionary's readings agree under precomposition at
121,152 comparisons with 0 differences.  The stabilizer contributes
nothing to the weld's site-assignment fiber: the freedom the dictionary
declares and the freedom identity leaves are different freedoms.

### 6.2 The record's attribution is not blind, by measurement

The record n_l(x) counts the division events containing both the actor
at site x and the actor at site x + l.  The link is a displacement in
the arena's own group structure, which lives on the LABELS; so the
record reads a pair the event sequence never names.  Measured, the
record's attribution is orbit-constant at 111 of 703 objects and
naming-dependent at 592.  The consequence is exact: the record is well
defined as a field over the arena and is not well defined as a property
of a thread.

### 6.3 The walk sees more than the record

Paper-20's coupled step is the site-block-diagonal coin C(x) = G.D(x)
with D(x) = diag(w^{n_l(x)}), then the shift.  It is re-implemented here
over Z[w], with the start taken to be the all-ones state, which is
symmetric under every relabelling; every asymmetry in the published menu
is therefore carried by the record and the shift and never by the start.
Measured, the Born menu is orbit-constant at 134,58,58,58,58 objects by
depth.

Two facts fall out.  A stabilizer element is a symmetry of the whole
coupled step exactly when it commutes with the shift and with the coin;
commuting with the shift forces it to be a translation of AG(2,3), and
commuting with the coin is exactly record-preservation.  Measured, 813
of the 121,152 stabilizer elements are symmetries of the coupled step,
exactly the translations.  Both tests are computed independently -- the
shift cell by cell, the translation against the nine translations -- and
they agree at every element.

And the depths separate.  At depth one the menu depends only on each
site's own record row, through w to that power, so it is blind wherever
the record is and at a few sites more.  From depth two the shift has
carried amplitude across links and the menu reads the arena's
displacement structure directly, at which point it is blind at strictly
fewer objects than the record.  The cross-tabulation is the sharpest
statement this unit makes about the walk.

| observable | verdict | blind at | of | basis |
|---|---|---|---|---|
| co-division relation | BLIND BY THEOREM | 703 | 703 | 121,152 element checks |
| weld dictionary readings | BLIND BY THEOREM | 703 | 703 | 121,152 parse comparisons |
| record attribution n_l(x) | NAMES | 111 | 703 | orbit-constancy per object |
| Born menu, depth 1 | NAMES | 134 | 703 | exact Z[w], symmetric start |
| Born menu, depth 2 | NAMES | 58 | 703 | exact Z[w], symmetric start |

| record blind | menu blind at depth 1 | menu blind at depth 2 | objects |
|---|---|---|---|
| False | False | False | 569 |
| False | True | False | 23 |
| True | True | False | 53 |
| True | True | True | 58 |

### 6.4 The relation forgets what the sequence remembers

The extreme case is a class of its own: at 24 of the 600 R = 4 histories
the co-division relation is the constant complete graph while the
stabilizer is trivial.  Those are exactly the schedules that use all
four parallel classes once each: any two distinct sites lie on exactly
one line, that line belongs to exactly one class, so every pair
co-divides exactly once and the relation is the constant complete graph.
Its automorphism group is the whole symmetric group on the nine actors.
The ordered history, by contrast, forces the labelling completely.

The general shape of that gap is the index of the stabilizer in the
automorphism group of the co-division relation, and it is published in
full.  At every R = 3 history and every diagonal R = 6 concatenation the
relation's automorphism group has order 1,296 while the stabilizer is
trivial.

| stabilizer order | co-division automorphism order | index | objects |
|---|---|---|---|
| 2 | 2 | 1 | 48 |
| 2 | 8 | 4 | 12 |
| 4 | 4 | 1 | 47 |
| 4 | 8 | 2 | 25 |
| 4 | 16 | 4 | 36 |
| 8 | 8 | 1 | 12 |
| 8 | 48 | 6 | 258 |
| 24 | 24 | 1 | 44 |
| 24 | 96 | 4 | 22 |
| 216 | 432 | 2 | 98 |
| 216 | 1,296 | 6 | 83 |
| 4,320 | 4,320 | 1 | 18 |

## 7. THE MEASURE-RELATIVITY OF THE COUNTS

No count becomes a probability without a declared measure.  This unit's
headline fraction moves when the measure does: measured, the record's
blind fraction is 3/19 by distinct prefix and 1235/6008 by corpus
multiplicity.  Both are stamped COUNTING-ONLY and both are published
with the measure they were taken under.

| quantity | distinct-prefix measure | corpus-multiplicity measure |
|---|---|---|
| nontrivial-stabilizer objects | 703 | 24,032 |
| record blind | 111 | 4,940 |
| walk blind at depth 2 | 58 | 2,065 |
| fraction, record | 3/19 | 1235/6008 |

## 8. THE GRAIN

The pin confines this unit, and the confinement is a published fact: the
groupoid grain is registered and not run.  Everything above is taken at
the global-relabelling grain: one permutation of the nine actors,
applied to every event at once.  The finer question -- whether a thread
may be re-identified BETWEEN events, which replaces the stabilizer
subgroup by a set of composable local isomorphisms -- is the successor,
and it is named here with its object so that the scope of every result
above is exactly the stabilizer grain.  No verdict segment of this unit
quantifies over it.

## 9. WHAT THE UNIT DOES NOT SAY

Four reading walls are evaluated against this paper's own characters,
not against a label.  The first confines the reality language: the unit
publishes a stabilizer census and an invariance census and draws no
conclusion beyond them.  The second holds the grain: no result at the
mid-history thread-swap grain is reported.  The third holds E-24: every
fraction carries its measure or the COUNTING-ONLY stamp.  The fourth
holds the scope: the corpora are committed objects, not a sample of
physics, and no sentence generalises the census beyond the declared
windows.

The instrument is the era's: 47 falsifiers, each naming the object it
corrupts and each verified against its own code; 13 pinned sources whose
bytes are digest-checked before anything is read; 10 quote anchors bound
to consumer gates; 10 tables, all rendered above; 7 declared windows;
and a numeral scan that covers prose, tables, inline spans and fenced
blocks alike.  The gate ledger, its totals and its seal manifest are in
the receipt.

## 10. THE VERDICT

```
AID-STRATIFIED-AT-THE-ROUND-MEET-[IDENTITY FORCED ON 5,852 OF 5,856 COMMITTED HISTORIES, CHART ON 4] -- CENSUS=C1 72 OF 72 TRIVIAL | C2 5,184 OF 5,184 TRIVIAL | C3 596 TRIVIAL AND 4 AT ORDER 216 WITH ORBIT SHAPE 3+3+3 -- ROUTES=THE S_9 FILTER AND THE YOUNG SUBGROUP AGREE AT ORDER ON ALL 41,347 DISTINCT PREFIXES AND AT ELEMENT SET ON 703, 0 MISMATCHES
```
```
CRYSTALLIZATION=EXACTLY 5 ON C1, C2 AND THE 1,944-HISTORY SEED FAN (UNIFORM, NOT AN AVERAGE) | C3 STRATIFIED 5:404|7:36|8:144|11:12|never:4 | NEVER 4 = THE CONSTANT-CLASS QUADRUPLES ANT|ANT|ANT|ANT,COL|COL|COL|COL,DIA|DIA|DIA|DIA,ROW|ROW|ROW|ROW -- PREFIX-LAW=A CONCATENATION CRYSTALLIZES EXACTLY WHEN ITS FIRST FACTOR DOES, 0 DISAGREEMENTS OF 5,184; THE STABILIZER NEVER GROWS, 0 GROWTH EVENTS IN 2,000 PREFIXES
```
```
INVARIANCE=SPLIT -- BLIND-BY-THEOREM: THE CO-DIVISION RELATION (0 VIOLATIONS OVER 121,152 STABILIZER ELEMENTS AT 703 OBJECTS) AND EVERY WELD-DICTIONARY READING (121,152 PARSE COMPARISONS, 0 DIFFERENCES) -- NOT-BLIND-BY-MEASUREMENT: THE RECORD'S ATTRIBUTION (ORBIT-CONSTANT AT 111 OF 703, NAMING-DEPENDENT AT 592) AND THE WALK'S BORN MENU (134,58,58,58,58 BY DEPTH) -- THE WALK STRICTLY REFINES THE RECORD FROM DEPTH TWO: 53 OBJECTS THE RECORD CANNOT SEPARATE AND THE WALK CAN, 23 THE RECORD SEPARATES AND THE ONE-STEP MENU CANNOT
```
```
WALK-SYMMETRIES=EXACTLY THE TRANSLATIONS (813 OF 121,152 ELEMENTS; SHIFT-COMMUTING EQUALS TRANSLATION AT EVERY ONE, 0 DISAGREEMENTS; RECORD-PRESERVING 51,769) -- DEGENERACY=THE RELATION FORGETS WHAT THE SEQUENCE REMEMBERS: AT 24 OF 600 R = 4 HISTORIES THE CO-DIVISION RELATION IS THE CONSTANT COMPLETE GRAPH WITH AUTOMORPHISM GROUP 362,880 WHILE THE STABILIZER OF THE ORDERED HISTORY IS TRIVIAL
```
```
SCOPE=THE GLOBAL-RELABELLING GRAIN ONLY; THE GROUPOID GRAIN REGISTERED AND NOT RUN -- MEASURE=COUNTING-ONLY UNDER TWO DECLARED MEASURES (E-24): THE RECORD'S BLIND FRACTION IS 3/19 BY DISTINCT PREFIX AND 1235/6008 BY CORPUS MULTIPLICITY, THE WALK'S 58/703 AND 2065/24032 -- WINDOWS=W-C1,W-C1FAN,W-C2,W-C3,W-DRIVE,W-AUTC2,W-WALK, FOUR OF THEM ENTIRE CLASSES -- LANGUAGE=FORCED/CHART/STRATIFIED NAME THE STABILIZER AND THE INVARIANCE DATA AND NOTHING ELSE
```
