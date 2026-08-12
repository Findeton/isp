# SPC — the species table: which labels the measured symmetries carry, and which of them the carriers can host

**Status:** `DELIVERED` — built against the frozen pin `v14/note-spc-pin.md`
(`7f0b1e9d5071`), the kinematic half of the species question. Verified to run:
two plain runs byte-identical, every gate passed, every declared mutant dead
at its declared target, the falsification self-test fatal at every anchor
class and writing nothing. Between delivery and adjudication every headline
below is a **candidate reading**.

**Unit:** SPC, v14, paper thirty-seven.
**Instrument:** `v14/code/spc_exact.py`.
**Artifacts:** `v14/code/spc_output.txt`, `v14/code/spc_receipt.json`.

**Inheritance, hash-verified at run time and by no other route.** The gauge
arena, the acting groups at the three grains, the carrier classes and the
price come from ACT, `v14/paper-34-act.md` (`d933221780ed`), with its
instrument `v14/code/act_exact.py` (`a90559ee0e0f`) and its receipt
`v14/code/act_receipt.json` (`7fd1267bddc7`); the identity lattice comes from
AID, `v14/paper-33-aid.md` (`ecdd3fbf1d06`), with its receipt
`v14/code/aid_receipt.json` (`2dd2a9879984`); the cell carrier and the shape
its exclusion census selected come from OCC, `v14/paper-31-occ.md`
(`0092caa4d9ad`), with its receipt `v14/code/occ_receipt.json`
(`455ddec78dda`); the invariant simplexes come from SMU,
`v14/paper-27-smu.md` (`6df0db523d32`); the lattice and its chart group come
from R5, `v14/paper-18-gauge-rung.md` (`62cfe5689d2c`); and the identity
arena's own symmetry inventory comes from the stochastic-split terminal,
`v14/paper-06-stochastic-split.md` (`c350caab17ee`), with its instrument
`v14/code/crb_stochastic_exact.py` (`5f2a54ea8a98`). Every object below is
**reimplemented** from those definitions; nothing is imported from any other
unit's program. **Anchors are (path, value) pairs and (context, consumer)
pairs, not only file bytes:** 12 file-bytes anchors, 43 path-value anchors and
19 verbatim-text anchors, 74 anchors in all — each verbatim window pinned by
the digest of its own bytes, by its own character count and by a declared
length floor, each located exactly once, each perturbed at a content-bearing
token and required to stop being locatable, and each bound to the gate that
consumes it, where the consumer is checked against this run's own ledger.

**Exact arithmetic only.** Character values live in the cyclotomic field
carried as tuples of exact fractions in the power basis, reduced modulo a
cyclotomic polynomial that is itself derived by exact integer division of
`x^n - 1` by every proper divisor's polynomial, so tuple equality is field
equality. The symmetric-group tables are integer-valued by the rim-hook
recursion. An abstract syntax scan of the instrument's own tree is a gate and
it finds 0 float literals; no logarithm, exponential or square root is called
anywhere, and the integer square root a degree is recovered by is written out
in integers and bisects.

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field; the complete string —
head included — is compared for equality against an independent
reconstruction that reads only the serialized receipt, derives the head by a
second head law of its own, and re-renders every segment from the primitive
measured tables, reading neither the builder's segments nor the builder's
aggregates and sharing no format string with it; and the block below is
compared, character for character under whitespace normalisation, against the
string this run emits — and the paper's fenced blocks are compared as a
**multiset** against the single block this run licenses, so neither a stale
verdict nor a forged twin beside the clean one can be delivered:

```
SPC-INVENTORY-22-GROUPS-220-CLASSES-220-SPECIES--SPC-CARRIER-SELECTS-156-OF-246--SPC-SELECTION-OPEN--SPC-STATISTICS-SPLITS-192|14|9|31 -- INVENTORY=22-GROUPS-AT-ORDERS-1,2,4,8,9,16,18,24,32,108,128,216,1024,4096,4320,8192,32768,362880-OF-WHICH-18-CARRY-A-FULL-EXACT-TABLE-AND-4-STAND-ABOVE-THE-DECLARED-CAP-128;CLASSES=220;SPECIES=220 -- IRREPS=EVERY-TABLE-GATED-BY-TWO-ROUTES-COLUMN-ORTHOGONALITY-AND-ROW-ORTHOGONALITY-AS-SEPARATE-GATES-WITH-THE-CLASS-EQUATION-AND-THE-DEGREE-SUM-BESIDE-THEM;THE-NINE-ACTOR-TABLE-IS-INTEGER-VALUED-WITH-30-CLASSES-AND-30-SPECIES-ITS-DEGREES-RE-DERIVED-BY-THE-HOOK-LENGTH-FORMULA;TWO-ENGINES-AGREE-ON-3-SYMMETRIC-GROUPS -- CARRIER=19-ROWS-OVER-7-DECLARED-CARRIERS;156-OF-246-SPECIES-HOSTED;9-ROWS-LEAVE-A-SPECIES-HOMELESS-THE-WIDEST-ACTOR-9-UNDER-S9-AT-2-OF-30;THE-136-CARRIER-CLASSES-AND-THE-80-AT-THE-EXTENSION-ARE-THE-TRIVIAL-SPECIES-MULTIPLICITY-BY-TWO-ROUTES -- PRICE=ONE-SPECIES:THE-ODD-TWIST-SPECIES-CARRIES-MULTIPLICITY-72-AT-THE-ANCHORED-READING-AND-40-AT-THE-EXTENSION-WHICH-ARE-EXACTLY-THE-PARENTS-IDENTIFIED-ORBIT-PAIRS;THE-PARENTS-PINNED-OBSERVABLE-OFF-DIAGONAL-QUARTIC-SIGN-IS-NON-ZERO-AT-288-OF-640-POINTS-AND-LIES-IN-1-ISOTYPIC-COMPONENT;136-OF-136-ORBIT-SUMS-VANISH -- IDENTITY=THE-SPECIES-WITH-AN-INVARIANT-VECTOR-ALONG-THE-MEASURED-STABILIZER-LATTICE-ARE-30,29,28,26,22,12,4-OF-30;ALONG-THE-CRYSTALLIZATION-CHAIN-4,12,12,26,30,30-SO-CRYSTALLIZATION-RESTORES-THE-INVENTORY-AT-PREFIX-5;BRANCHING-BY-TWO-ROUTES-AT-2610-PAIRS-WITH-0-DISAGREEMENTS-AND-A-TABLEAU-THIRD-ROUTE-AT-210-ROWS -- SELECTION=2154-COMPOSITE-RULES;10-ROWS-CLOSE-AND-9-EXIT;THE-DISTINGUISHED-ROW-ACTOR-9-UNDER-S9-EXITS-TO-2-SPECIES-IT-DOES-NOT-HOST -- STATISTICS=THE-SELECTED-SHAPE-IS-ANTISYMMETRIC-DERIVED-FROM-0-LEAK-CELLS-AGAINST-81;192-SPECIES-IN-BOTH-SHAPES,14-SYMMETRIC-ONLY,9-ANTISYMMETRIC-ONLY,31-IN-NEITHER;4-OF-19-ROWS-SPLIT-PROPERLY -- ROUTES=ORBITS-BY-CHARACTER-AND-BY-UNION-FIND-AT-19-ROWS;COMPOSITES-BY-TWO-CONTRACTIONS;SQUARES-BY-FORMULA-AND-BY-COUNTING-ON-THE-PAIR-SET;BRANCHING-BY-RESTRICTION-AND-BY-FROBENIUS-RECIPROCITY;INVARIANTS-BY-TABLEAU-COUNT;ORDERS-BY-CLOSURE-AND-CLASS-EQUATION-AND-ORBIT-STABILIZER;ZERO-DISAGREEMENTS-EVERYWHERE -- CONTROLS=4-SYNTHETIC-ARENAS-THROUGH-THE-SAME-CENSUS-FUNCTIONS-EMITTING-4-DISTINCT-HEADS;7-OF-8-OUTCOME-ARMS-ARE-LIVE-AT-THIS-ARENA-EACH-WITNESSED-BY-A-DELIVERED-ROW -- SCOPE=THE-KINEMATIC-HALF-ONLY;LABELS-COMPOSITES-AND-STATISTICS-COMPATIBILITY;NO-MASS-NO-SPECTRUM-NO-STABILITY-NO-REALIZED-PARTICLE-CLAIM;NO-STANDARD-MODEL-IDENTIFICATION;NO-SI-NUMBER;NO-CONTINUUM-CLAIM;COUNTS-ARE-COUNTING-ONLY;THE-TABLE-CAP-IS-128-AND-4-ACTING-GROUPS-STAND-ABOVE-IT-WITH-THEIR-ORDERS-RE-DERIVED-AND-THE-CARRIER-SEEING-THEM-THROUGH-A-GROUP-OF-ORDER-8-OR-16;THE-CARRIER-ROW-LIST-IS-A-DECLARATION
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and what could have answered otherwise

The corpus has spent fourteen units measuring symmetries. It has never asked
what those symmetries *label*. That is the question here, and it has an exact
answer: the irreducible representations of a finite group are its complete
inventory of labels, they are computable exactly, and a carrier either hosts
one or it does not.

The pin puts the census standard in one sentence, quoted from its own pinned
bytes:

> for each inventory group, the full character table computed exactly and
> gated by two routes (column orthogonality AND row orthogonality as separate
> gates; class equation verified)

and the heart of the unit in another:

> the 136 carrier classes (80 at the extension) as permutation modules over
> the acting groups — decomposed into irreps EXACTLY

with the question that makes it a measurement rather than a catalogue:

> which irreps of the abstract groups have NO carrier realization
> (label-possible but carrier-homeless — measured, not argued)

**Every pre-registered word could have come out otherwise here.** The pin's
own engraving demands a feasibility line; here it is a measurement, because
the arena carries rows on both sides of every question the head asks:
7 of the 8 outcome arms are live at this arena, each of them witnessed by a
delivered row rather than by a control. The one arm no delivered row can
reach is the refusal, which fires only on an instrument fault.

| outcome | arm | live at this arena | witnessed by a delivered row |
|---|---|---|---|
| SPC-INVENTORY | THE-COUNTS | yes | COIN-640-UNDER-RESIDUAL-GAUGE-4 |
| SPC-CARRIER-SELECTS | EVERY-SPECIES-HOSTED | yes | COIN-640-UNDER-RESIDUAL-GAUGE-4 |
| SPC-CARRIER-SELECTS | SOME-SPECIES-HOMELESS | yes | SITE-16-UNDER-CHART-32 |
| SPC-SELECTION-CLOSED | THE-COMPOSITES-STAY | yes | COIN-640-UNDER-RESIDUAL-GAUGE-4 |
| SPC-SELECTION-OPEN | THE-COMPOSITES-EXIT | yes | SITE-16-UNDER-CHART-32 |
| SPC-STATISTICS-SPLITS | ALL-IN-BOTH-SHAPES | yes | COIN-640-UNDER-RESIDUAL-GAUGE-4 |
| SPC-STATISTICS-SPLITS | A-PROPER-SPLIT | yes | SITE-16-UNDER-CHART-128 |
| SPC-BLOCKED-AT | INSTRUMENT-FAULT | no |  |

**The control arm is a set of synthetic arenas through the real census
functions.** 4 synthetic arenas are built — a cyclic group acting regularly
on its own elements, the same group acting trivially on two points, a cyclic
group with two orbits of coprime size, and a set of permutations that is
measured not to close under composition — and each is put through the same
closure test, the same character engine, the same decomposition, the same
composite census and the same statistics census as the delivered rows. No
field of any control row is written from outside. Each emits its own head,
and the four heads are distinct.

| row | group order | species | hosted | status | emitted |
|---|---|---|---|---|---|
| CTRL-CYCLIC-3-REGULAR | 3 | 3 | 3 | MEASURED | SPC-INVENTORY-1-GROUPS-3-CLASSES-3-SPECIES--SPC-CARRIER-SELECTS-3-OF-3--SPC-SELECTION-CLOSED-9-RULES--SPC-STATISTICS-SPLITS-3|0|0|0 |
| CTRL-CYCLIC-3-TRIVIAL-ACTION | 3 | 3 | 1 | MEASURED | SPC-INVENTORY-1-GROUPS-3-CLASSES-3-SPECIES--SPC-CARRIER-SELECTS-1-OF-3--SPC-SELECTION-CLOSED-1-RULES--SPC-STATISTICS-SPLITS-1|0|0|2 |
| CTRL-CYCLIC-6-TWO-ORBITS | 6 | 6 | 4 | MEASURED | SPC-INVENTORY-1-GROUPS-6-CLASSES-6-SPECIES--SPC-CARRIER-SELECTS-4-OF-6--SPC-SELECTION-OPEN--SPC-STATISTICS-SPLITS-6|0|0|0 |
| CTRL-NOT-A-GROUP | 2 | 0 | 0 | BLOCKED | SPC-BLOCKED-AT-THE-GROUP-CLOSURE |

## 2. The inventory: every measured symmetry group, with its order re-derived

22 groups, 18 of which carry a full exact character table and 4 of which
stand above the declared cap of 128. They carry 220 conjugacy classes and 220
species in all — the class count and the species count agree group by group,
which is itself one of the census gates.

**No order in this table is typed.** Every group's order is re-derived by the
length of its own closed element list, by the sum of its own conjugacy class
sizes, and by the sum of the squares of its species degrees; and, wherever the
elements are enumerable, by the product of one declared point's orbit with
that point's stabilizer. The three symmetric-group rows take the first three
routes only, because their element lists are not enumerated at all: the
partitions index both the classes and the species, and no permutation is ever
written down.

| group | order | classes | species | engine | carrier it is censused on |
|---|---|---|---|---|---|
| RESIDUAL-GAUGE-4 | 4 | 4 | 4 | DIXON | COIN-640 |
| ACTING-LINK-8 | 8 | 8 | 8 | DIXON | COIN-640 |
| RESIDUAL-GAUGE-8 | 8 | 5 | 5 | DIXON | COIN-640 |
| GAMMA-16 | 16 | 7 | 7 | DIXON | COIN-640 |
| CHART-32 | 32 | 14 | 14 | DIXON | LINK-32 |
| CHART-128 | 128 | 20 | 20 | DIXON | LINK-32 |
| TORUS-TRANSLATIONS-16 | 16 | 16 | 16 | DIXON | LINK-32 |
| TRANS-9 | 9 | 9 | 9 | DIXON | CELL-27 |
| CHART-18 | 18 | 9 | 9 | DIXON | CELL-27 |
| EXT-108 | 108 | 11 | 11 | DIXON | CELL-27 |
| S9 | 362880 | 30 | 30 | MURNAGHAN-NAKAYAMA | ACTOR-9 |
| ACTING-PLAQUETTE-ANCHORED | 1024 | 0 | 0 | ABOVE-THE-TABLE-CAP | COIN-640 |
| ACTING-PLAQUETTE-EXTENSION | 4096 | 0 | 0 | ABOVE-THE-TABLE-CAP | COIN-640 |
| ACTING-SITE-ANCHORED | 8192 | 0 | 0 | ABOVE-THE-TABLE-CAP | COIN-640 |
| ACTING-SITE-EXTENSION | 32768 | 0 | 0 | ABOVE-THE-TABLE-CAP | COIN-640 |
| FORCED-TRIVIAL | 1 | 1 | 1 | MURNAGHAN-NAKAYAMA-PRODUCT | ACTOR-9 |
| YOUNG-2 | 2 | 2 | 2 | MURNAGHAN-NAKAYAMA-PRODUCT | ACTOR-9 |
| YOUNG-4 | 4 | 4 | 4 | MURNAGHAN-NAKAYAMA-PRODUCT | ACTOR-9 |
| YOUNG-8 | 8 | 8 | 8 | MURNAGHAN-NAKAYAMA-PRODUCT | ACTOR-9 |
| YOUNG-24 | 24 | 12 | 12 | MURNAGHAN-NAKAYAMA-PRODUCT | ACTOR-9 |
| YOUNG-216 | 216 | 27 | 27 | MURNAGHAN-NAKAYAMA-PRODUCT | ACTOR-9 |
| YOUNG-4320 | 4320 | 33 | 33 | MURNAGHAN-NAKAYAMA-PRODUCT | ACTOR-9 |

**The gauge arena, rebuilt.** The coefficient alphabet returns twenty-five
elements and the coin family, enumerated exhaustively over the admissible
rows, returns 640 coins, splitting into 64 diagonal, 64 antidiagonal and 512
balanced. The carrier is the parent's own primary carrier, and the parent's
sentence for it is quoted here:

> The uniform configurations — one coin repeated on every link — are swept
> **exhaustively** over the coin alphabet

**The identity arena, rebuilt.** 9 sites, 3 declared link directions and 27
cells, one cell per co-division pair, at the count the occupancy terminal
published. Its point group is built as the maximal set of matrices carrying
the declared link set into its own signed closure — a point group of order
twelve — and the arena group is that point group times the translations: the
arena group has order 108 and the pinned chart group 18, which is what the
terminal that measured them says:

> the pinned chart group has order 18; the largest group the declared link
> set admits has order 108

**Four acting groups stand above the table cap, and the carrier cannot tell
them apart from two that do not.** The declared cap is a construction choice
and it is priced as one; what makes it harmless is a measurement rather than
a promise. At every one of the six (grain, reading) rows the subgroup of coin
maps a uniform configuration can be moved by is the same group — of order
eight at the anchored reading and sixteen at the extension — it is closed,
and the partition it induces on the carrier is exactly the partition the whole
acting group induces there. That is why the species census on this carrier is
complete at all six rows although four of the six acting groups have no table
here, and it is the mechanism behind the parent's own grain-invariance:

> The partition is the same 136 classes at all three grains

| grain | reading | gauge image order | chart stabilizer order | acting group order | the group the carrier sees | induced classes on the carrier |
|---|---|---|---|---|---|---|
| LINK | ANCHORED | 8 | 1 | 8 | 8 | 136 |
| LINK | EXTENSION | 8 | 4 | 16 | 16 | 80 |
| PLAQUETTE | ANCHORED | 512 | 2 | 1024 | 8 | 136 |
| PLAQUETTE | EXTENSION | 512 | 8 | 4096 | 16 | 80 |
| SITE | ANCHORED | 4096 | 2 | 8192 | 8 | 136 |
| SITE | EXTENSION | 4096 | 8 | 32768 | 16 | 80 |

## 3. The census: two routes, and two engines

Every table this unit publishes is gated twice over, and the two gates are
separate rows of the ledger because they are not the same measurement. Row
orthogonality says the species are an orthonormal family. Column
orthogonality says something the first cannot: that the family is
**complete**, since a table with a species missing still has orthonormal rows
and immediately fails on its columns. The class equation and the sum of the
squares of the degrees close the arithmetic beside them.

There are two engines. The first takes a group as an explicit element list
with a product, measures its conjugacy classes and its class multiplication
coefficients, splits the common invariant subspaces over a prime field chosen
larger than twice the integer square root of the order, and lifts each value
out of the prime field by a finite Fourier inversion whose coefficients are
integers bounded by the degree. The second never sees a group element: it
recurses on rim hooks. **They are required to agree wherever both can run.**

| row | order | classes dixon | classes murnaghan nakayama | tables agree |
|---|---|---|---|---|
| S2 | 2 | 2 | 2 | yes |
| S3 | 6 | 3 | 3 | yes |
| S4 | 24 | 5 | 5 | yes |

The nine-actor table is the classical one and carries an independent route of
its own: 30 classes and 30 species, its degrees re-derived by the hook-length
formula, and the squares of its degrees sum to 362880.

## 4. The carrier decomposition — the heart

A carrier is a finite set the corpus committed and a group that acts on it.
Its permutation module decomposes into species exactly, and the multiplicity
of the trivial species is the orbit count — which is the characterisation the
parent states and this unit turns into a measurement:

> A measure is invariant under a group acting on a finite set if and only if
> it is constant on the orbits.

So the parent's own carrier numbers come back here as **multiplicities**, and
each is computed twice: once as a character inner product and once by a
union-find pass that never evaluates a character.

19 carrier rows over 7 declared carriers, and 156 of 246 species are hosted.

| row | group order | carrier points | classes | irreps | hosted | homeless | orbits by the character |
|---|---|---|---|---|---|---|---|
| COIN-640-UNDER-RESIDUAL-GAUGE-4 | 4 | 640 | 4 | 4 | 4 | 0 | 208 |
| COIN-640-UNDER-ACTING-LINK-8 | 8 | 640 | 8 | 8 | 8 | 0 | 136 |
| COIN-640-UNDER-RESIDUAL-GAUGE-8 | 8 | 640 | 5 | 5 | 5 | 0 | 120 |
| COIN-640-UNDER-GAMMA-16 | 16 | 640 | 7 | 7 | 7 | 0 | 80 |
| LINK-32-UNDER-CHART-32 | 32 | 32 | 14 | 14 | 14 | 0 | 1 |
| SITE-16-UNDER-CHART-32 | 32 | 16 | 14 | 14 | 10 | 4 | 1 |
| PLAQUETTE-16-UNDER-CHART-32 | 32 | 16 | 14 | 14 | 10 | 4 | 1 |
| LINK-32-UNDER-CHART-128 | 128 | 32 | 20 | 20 | 10 | 10 | 1 |
| SITE-16-UNDER-CHART-128 | 128 | 16 | 20 | 20 | 6 | 14 | 1 |
| PLAQUETTE-16-UNDER-CHART-128 | 128 | 16 | 20 | 20 | 6 | 14 | 1 |
| LINK-32-UNDER-TORUS-TRANSLATIONS-16 | 16 | 32 | 16 | 16 | 16 | 0 | 2 |
| SITE-16-UNDER-TORUS-TRANSLATIONS-16 | 16 | 16 | 16 | 16 | 16 | 0 | 1 |
| CELL-27-UNDER-TRANS-9 | 9 | 27 | 9 | 9 | 9 | 0 | 3 |
| SITE-9-UNDER-TRANS-9 | 9 | 9 | 9 | 9 | 9 | 0 | 1 |
| CELL-27-UNDER-CHART-18 | 18 | 27 | 9 | 9 | 9 | 0 | 2 |
| SITE-9-UNDER-CHART-18 | 18 | 9 | 9 | 9 | 6 | 3 | 1 |
| CELL-27-UNDER-EXT-108 | 108 | 27 | 11 | 11 | 6 | 5 | 1 |
| SITE-9-UNDER-EXT-108 | 108 | 9 | 11 | 11 | 3 | 8 | 1 |
| ACTOR-9-UNDER-S9 | 362880 | 9 | 30 | 30 | 2 | 28 | 1 |

**The first headline is a contrast between two sides of the corpus, and it is
measured at every row.** On the gauge arena's own carrier the answer is total:
the coin carrier hosts every species of every group that acts on it, at all
four groups, from the arena's own residual gauge group of order four to the
coin-map group of order sixteen. On the identity side it is not: the nine
actors under the whole symmetric group host 2 of 30 species, and 28 have no
realization there at all. 9 of the 19 rows leave at least one species
homeless.

**Homelessness is a property of the pair and not of the group.** The same
chart group of order 128 hosts ten of its twenty species on the thirty-two
links and six of them on the sixteen sites; the same nine sites host all nine
species of the translation group, six of the nine of the chart group, and
three of the eleven of the arena group. **So the species inventory is not
carrier-independent**: what a group can label is fixed by the group, and what
is actually labelled is fixed by the carrier it is asked to label.

## 5. The price is one species

The parent measured two things about the odd twist. Its own sentence for the
first:

> The odd twist is not realisable on this torus

and for the second:

> 72 pairs of gauge orbits at the anchored reading and 40 at the extension
> are identified by every admissible weight system

This unit resolves both into a single label. There is exactly one species on
which the odd twist acts by minus one while every twist the torus itself
realises acts trivially, and **the price is one species**: it carries
multiplicity 72 at the anchored reading and 40 at the
extension, which is the drop in the trivial multiplicity between the arena's
own gauge group and the acting group, and which is the parent's own count of
identified orbit pairs at both readings. The whole of the parent's discount
sits in one label.

| row | the species index | multiplicity | the arena groups orbit count | the acting groups orbit count | the parents identified orbit pairs |
|---|---|---|---|---|---|
| COIN-640-UNDER-ACTING-LINK-8 | 0 | 72 | 208 | 136 | 72 |
| COIN-640-UNDER-GAMMA-16 | 1 | 40 | 120 | 80 | 40 |

**And the parent's one pinned observable lives there.** Rebuilt here from its
own definition, it is non-zero at 288 of the 640 coins, and its component in
every other species vanishes identically: **the observable lies in that
species and in no other**. What follows is the parent's measured result,
re-derived as a statement about labels rather than about ranges — an
admissible weight system is an invariant vector, an invariant vector lies in
the trivial species, and the pairing of the trivial species with any other is
zero, so the expectation is a single value. The same fact is measured
directly on the orbits: 136 of the 136 orbit sums vanish.

## 6. The identity layer: what the stabilizer lattice does to the inventory

The identity side's lattice is not this unit's invention. The parent proved
and measured it:

> the stabilizer is the Young subgroup, its order is the product of the block
> factorials, and identity crystallizes exactly when every actor has its own
> signature.

Each of the six nontrivial shapes is read from the parent's receipt at its own
named path together with the number of prefixes carrying it, and the subgroup
each shape names is built here. Restricting the nine-actor species along that
lattice is a two-route computation — an inner product inside the subgroup, and
an inner product inside the big group between its species and the character
induced from the subgroup — and the invariant dimension carries a third route
of its own in a tableau count that shares no code with either engine.
Measured: 2610 branching multiplicities by both routes, at 0 disagreements,
and 210 tableau counts, at 0 disagreements.

| row | orbit shape | order by construction | classes | species of its own | prefixes the parent measured here | species with an invariant vector |
|---|---|---|---|---|---|---|
| FORCED-TRIVIAL | 1+1+1+1+1+1+1+1+1 | 1 | 1 | 1 | 5852 | 30 |
| YOUNG-2 | 1+1+1+1+1+1+1+2 | 2 | 2 | 2 | 60 | 29 |
| YOUNG-4 | 1+1+1+1+1+2+2 | 4 | 4 | 4 | 108 | 28 |
| YOUNG-8 | 1+1+1+2+2+2 | 8 | 8 | 8 | 270 | 26 |
| YOUNG-24 | 1+1+2+2+3 | 24 | 12 | 12 | 66 | 22 |
| YOUNG-216 | 3+3+3 | 216 | 27 | 27 | 181 | 12 |
| YOUNG-4320 | 3+6 | 4320 | 33 | 33 | 18 | 4 |

**The inventory collapses as the stabilizer grows.** Thirty species carry an
invariant vector where identity is forced, twelve where the stabilizer is the
three-block subgroup the parent's four chart histories carry, and four at the
largest measured stabilizer.

The parent's crystallization profile is realised here by an exhibited flag of
partitions of the nine actors, each step refining the one before, so the
stabilizers are genuinely nested and the sequence is a restriction chain
rather than six unrelated subgroups. Along it the inventory runs from 4 at
the largest measured stabilizer to 30 at crystallization. Read in the
direction the schedule runs, **crystallization does not destroy the
inventory, it restores it**: the labels a history can carry are fewest at its
first event and complete at the fifth, and the admissibility axis is where
that matters, because the parent measured that

> Every admissible history of this census forces identity

| prefix length | stabilizer order | the parents order | orbit shape | species with an invariant vector |
|---|---|---|---|---|
| 1 | 4320 | 4320 | 3+6 | 4 |
| 2 | 216 | 216 | 3+3+3 | 12 |
| 3 | 216 | 216 | 3+3+3 | 12 |
| 4 | 8 | 8 | 1+1+1+2+2+2 | 26 |
| 5 | 1 | 1 | 1+1+1+1+1+1+1+1+1 | 30 |
| 6 | 1 | 1 | 1+1+1+1+1+1+1+1+1 | 30 |

The full branching at the distinguished stabilizer — the three-block shape
the chart histories carry — is published species by species. The
constituents column counts how many of the subgroup's own species the
restriction meets; the invariant dimension is the multiplicity of the
subgroup's trivial species, which is the tableau count.

| species | degree | constituents | invariant dimension |
|---|---|---|---|
| 9 | 1 | 1 | 1 |
| 8+1 | 8 | 4 | 2 |
| 7+2 | 27 | 7 | 3 |
| 7+1+1 | 28 | 10 | 1 |
| 6+3 | 48 | 8 | 4 |
| 6+2+1 | 105 | 17 | 2 |
| 6+1+1+1 | 56 | 16 | 0 |
| 5+4 | 42 | 8 | 2 |
| 5+3+1 | 162 | 20 | 3 |
| 5+2+2 | 120 | 20 | 1 |
| 5+2+1+1 | 189 | 22 | 0 |
| 5+1+1+1+1 | 70 | 19 | 0 |
| 4+4+1 | 84 | 14 | 1 |
| 4+3+2 | 168 | 20 | 2 |
| 4+3+1+1 | 216 | 22 | 0 |
| 4+2+2+1 | 216 | 22 | 0 |
| 4+2+1+1+1 | 189 | 22 | 0 |
| 4+1+1+1+1+1 | 56 | 16 | 0 |
| 3+3+3 | 42 | 9 | 1 |
| 3+3+2+1 | 168 | 20 | 0 |
| 3+3+1+1+1 | 120 | 20 | 0 |
| 3+2+2+2 | 84 | 14 | 0 |
| 3+2+2+1+1 | 162 | 20 | 0 |
| 3+2+1+1+1+1 | 105 | 17 | 0 |
| 3+1+1+1+1+1+1 | 28 | 10 | 0 |
| 2+2+2+2+1 | 42 | 8 | 0 |
| 2+2+2+1+1+1 | 48 | 8 | 0 |
| 2+2+1+1+1+1+1 | 27 | 7 | 0 |
| 2+1+1+1+1+1+1+1 | 8 | 4 | 0 |
| 1+1+1+1+1+1+1+1+1 | 1 | 1 | 0 |

## 7. Selection rules: which composites the carriers reach

A composite of two species is their tensor product, decomposed. The census is
exact at every entry and carries a second route: the multiplicity of a third
species in the product of the first two is also the multiplicity of the first
in the product of the third with the second's conjugate. The pin asks the
question this way:

> tensor-product decompositions among the carrier-realized species — which
> composites are reachable

Measured: 2154 composite rules, and 10 rows close and 9 exit.

| row | hosted | composite rules | species the composites exit to | selection closes |
|---|---|---|---|---|
| COIN-640-UNDER-RESIDUAL-GAUGE-4 | 4 | 16 | 0 | yes |
| COIN-640-UNDER-ACTING-LINK-8 | 8 | 64 | 0 | yes |
| COIN-640-UNDER-RESIDUAL-GAUGE-8 | 5 | 28 | 0 | yes |
| COIN-640-UNDER-GAMMA-16 | 7 | 64 | 0 | yes |
| LINK-32-UNDER-CHART-32 | 14 | 256 | 0 | yes |
| SITE-16-UNDER-CHART-32 | 10 | 160 | 4 | no |
| PLAQUETTE-16-UNDER-CHART-32 | 10 | 160 | 4 | no |
| LINK-32-UNDER-CHART-128 | 10 | 271 | 10 | no |
| SITE-16-UNDER-CHART-128 | 6 | 90 | 12 | no |
| PLAQUETTE-16-UNDER-CHART-128 | 6 | 90 | 12 | no |
| LINK-32-UNDER-TORUS-TRANSLATIONS-16 | 16 | 256 | 0 | yes |
| SITE-16-UNDER-TORUS-TRANSLATIONS-16 | 16 | 256 | 0 | yes |
| CELL-27-UNDER-TRANS-9 | 9 | 81 | 0 | yes |
| SITE-9-UNDER-TRANS-9 | 9 | 81 | 0 | yes |
| CELL-27-UNDER-CHART-18 | 9 | 99 | 0 | yes |
| SITE-9-UNDER-CHART-18 | 6 | 54 | 3 | no |
| CELL-27-UNDER-EXT-108 | 6 | 100 | 5 | no |
| SITE-9-UNDER-EXT-108 | 3 | 21 | 7 | no |
| ACTOR-9-UNDER-S9 | 2 | 7 | 2 | no |

**Where a carrier hosts everything, the composites cannot leave; where it
does not, they usually do.** The rows that close are exactly the rows with no
homeless species, and the reason is arithmetic rather than deep: a complete
hosted set has nowhere to exit to. What makes the census a measurement is the
other side. At the actor row the hosted set is the trivial species and the
standard one, and **the composites do not close**: the standard species
composed with itself reaches four species, of which two are hosted and two
are not.

| left | right | composite species | multiplicities | exits the hosted set |
|---|---|---|---|---|
| 0 | 0 | [0] | [1] | no |
| 0 | 1 | [1] | [1] | no |
| 1 | 0 | [1] | [1] | no |
| 1 | 1 | [0, 1, 2, 3] | [1, 1, 1, 1] | yes |

The species are indexed in the order the branching table of section six lists
them, so index zero is the trivial species and index one the standard one; the
two the composite reaches and the carrier does not host are the third and
fourth rows of that table.

## 8. Statistics: which species the selected shape can carry

The occupancy terminal measured the exclusion question at the carrier's own
pair grain, and its sentence is quoted here:

> the symmetric shape leaks at 81 cells at 5 of the 6 coin classes and the
> antisymmetric shape leaks at 0, so a hard core there would select

Which shape that selects is **derived** here from those two counts and not
typed: the shape that leaks at 0 cells against 81 is the antisymmetric one.
The compatibility census then asks, at every carrier row, which species the
two squares of the module can carry — the symmetric square, the antisymmetric
square, both, or neither — with the split computed twice at every class, once
by the character formula and once by counting fixed pairs on the pair set
itself.

| row | species | in both shapes | symmetric only | antisymmetric only | in neither shape |
|---|---|---|---|---|---|
| COIN-640-UNDER-RESIDUAL-GAUGE-4 | 4 | 4 | 0 | 0 | 0 |
| COIN-640-UNDER-ACTING-LINK-8 | 8 | 8 | 0 | 0 | 0 |
| COIN-640-UNDER-RESIDUAL-GAUGE-8 | 5 | 5 | 0 | 0 | 0 |
| COIN-640-UNDER-GAMMA-16 | 7 | 7 | 0 | 0 | 0 |
| LINK-32-UNDER-CHART-32 | 14 | 14 | 0 | 0 | 0 |
| SITE-16-UNDER-CHART-32 | 14 | 14 | 0 | 0 | 0 |
| PLAQUETTE-16-UNDER-CHART-32 | 14 | 14 | 0 | 0 | 0 |
| LINK-32-UNDER-CHART-128 | 20 | 20 | 0 | 0 | 0 |
| SITE-16-UNDER-CHART-128 | 20 | 11 | 5 | 2 | 2 |
| PLAQUETTE-16-UNDER-CHART-128 | 20 | 11 | 5 | 2 | 2 |
| LINK-32-UNDER-TORUS-TRANSLATIONS-16 | 16 | 16 | 0 | 0 | 0 |
| SITE-16-UNDER-TORUS-TRANSLATIONS-16 | 16 | 16 | 0 | 0 | 0 |
| CELL-27-UNDER-TRANS-9 | 9 | 9 | 0 | 0 | 0 |
| SITE-9-UNDER-TRANS-9 | 9 | 9 | 0 | 0 | 0 |
| CELL-27-UNDER-CHART-18 | 9 | 9 | 0 | 0 | 0 |
| SITE-9-UNDER-CHART-18 | 9 | 9 | 0 | 0 | 0 |
| CELL-27-UNDER-EXT-108 | 11 | 11 | 0 | 0 | 0 |
| SITE-9-UNDER-EXT-108 | 11 | 4 | 2 | 4 | 1 |
| ACTOR-9-UNDER-S9 | 30 | 1 | 2 | 1 | 26 |

Measured: 192 species in both shapes, 14 in the symmetric shape alone, 9 in
the antisymmetric shape alone and 31 in neither, and 4 of the 19 rows split
properly. On every row of the gauge arena the two shapes carry the same
species, so exclusion costs no label there. The split is on the other side,
and the sharpest instance is the actor row: **the trivial species is not
compatible with the selected shape at the actor row**, and of the two species
that carrier hosts only one survives into the exclusion-selected square. The
pin's question is answered in that one line, and its scope is exactly the pair
grain the parent's census selected at.

## 9. What this decides, and what it does not

**Decided, at the declared scope.**

- **The inventory exists and is exact.** Twenty-two measured groups, their
  classes and their species, every table gated twice over and two engines
  agreeing wherever both run.
- **Hosting is a property of the pair.** A group's species are fixed by the
  group; which of them a carrier realizes is fixed by the carrier, and the
  corpus's two sides sit at opposite ends of that scale.
- **The parent's discount and its pinned observable are one label.** The
  count of identified orbit pairs is a multiplicity, the observable is a
  vector in that species, and the pinning follows from orthogonality.
- **The identity lattice acts on the inventory monotonically**, and the
  crystallization chain reads it in the restoring direction.
- **The composites close exactly where the hosted set is complete.**
- **Exclusion is free on the gauge arena and costly on the identity arena**,
  at the grain the occupancy census selected.

**Not decided, and named.**

- **Which species are realized.** This is the kinematic half only: no mass, no
  spectrum, no stability and no realized-particle claim is made here. That
  question belongs to this unit's successor and waits behind the potential
  unit's gate.
- **The four acting groups above the cap.** Their orders are re-derived here
  and their own species censuses are not computed. What is measured is that
  the carrier sees them through a group whose table is computed, so no carrier
  row is affected; their abstract inventories remain open.
- **The carrier row list.** It is a declaration with an unbounded fibre, and
  the head's counts move with it. Both arms of every outcome word are
  populated by delivered rows, so adding a row cannot flip a word, but it
  moves the numbers.
- **The decomposition grain.** The nine-actor grain is granted by the parent;
  which subsystems there are is another unit's question and the actor row's
  species count would move with it.
- **The glued-world census.** The sector union's automorphism group is larger
  than any single sector's, which at the label level implies an exchange
  parity no single sector has. That census belongs to a successor chartered
  after both panels rule, and nothing here is claimed for it.

## 10. The instrument

The instrument is `v14/code/spc_exact.py`, and its contract is the era's
minimum: a delivery run that is the only writer, a `--no-write` twin, a
falsification self-test that corrupts one anchor class in memory and must die
writing nothing, a per-mutant runner, an all-mutants sweep, gate and mutant
listings, and a `--verify-paper` mode. Unknown flags exit 2. The exit
conventions invert the usual reading and are therefore disclosed in the usage
string, in the receipt and here: the delivery run exits 0 on success and 1 on
any refusal, writing nothing; `--selftest` exits 0 when every anchor class is
fatal; `--mutant` exits 0 when the named mutant *dies* on its declared target.

The gate ledger is chained row by row and that chain is verified, in the run
and again at the disk boundary from the bytes read back. 39 gates close
before the paper gates, and 7 paper gates, 1 receipt-wall gate and 2 closing
gates follow — the last two being the seal and the artifact integrity check,
which cannot be inside the ledger they close over. 25 objects are sealed
before the paper gates and the manifest is total: every other top-level key is
named in the declaration with the reason it cannot be sealed, and the receipt
crosses the disk boundary under a total byte comparison so that the unsealed
keys are guarded too.

55 declared mutants, each dying at the gate it was declared to falsify. The
registry is checked total against the instrument's own syntax tree, so a
falsifier cannot exist as an unswept branch and a switch the scan cannot read
is fatal rather than forgiven; the function inventory is checked total the
same way. Each mutant's published description names the exact token it plants
and that token is located in the source text. One of them is worth naming
here because it is what makes the two orthogonality gates independent rather
than duplicated: a falsifier that drops one species from the nine-actor table
leaves row orthogonality intact and dies on the column route alone.

12 file-bytes anchors, 43 path-value anchors and 19 verbatim-text anchors, 74
anchors in all, each window pinned by its own digest and its own character
count against a declared floor, each located exactly once under whitespace and
markdown-prefix normalisation, each perturbed at a content-bearing token and
required to stop being locatable, and each bound to the gate that consumes it.

**The choice inventory.** 12 construction choices are inventoried, of which 5
are verdict-determining, each with its fibre and the instances this unit
built; the instance counts are recounted from the objects they describe.

| choice | class | fibre | instances built | verdict determining | measured |
|---|---|---|---|---|---|
| THE-GROUP-INVENTORY-LIST | DECLARED-AND-DISCLOSED | UNBOUNDED | 22 | yes | yes |
| THE-CARRIER-ROW-LIST | DECLARED-AND-DISCLOSED | UNBOUNDED | 19 | yes | yes |
| THE-TABLE-CAP | DECLARED-AND-SWEPT | UNBOUNDED | 1 | no | yes |
| THE-CHART-READING | DECLARED-AND-SWEPT | 2 | 2 | no | yes |
| THE-LOCALITY-GRAIN | DECLARED-AND-SWEPT | 3 | 3 | no | yes |
| THE-COIN-FAMILY-AND-THE-LATTICE | FORCED | 1 | 1 | no | yes |
| THE-NINE-ACTOR-GRAIN | GRANTED-BY-THE-PARENT | 1 | 1 | yes | no |
| THE-STABILIZER-LATTICE | INHERITED | 1 | 7 | yes | yes |
| THE-CRYSTALLIZATION-FLAG | EXHIBITED | UNBOUNDED | 1 | no | yes |
| THE-SELECTED-SHAPE | DERIVED | 1 | 1 | yes | yes |
| THE-DISTINGUISHED-COMPOSITE-ROW | DECLARED-AND-DISCLOSED | 19 | 1 | no | yes |
| THE-SYNTHETIC-CONTROL-ARENAS | DECLARED-AND-DISCLOSED | UNBOUNDED | 4 | no | yes |

## 11. The walls

Each wall has two legs. The first is a list of banned forms, matched at word
boundaries over this paper's own characters with the declaring sentences
removed first, and every declaring sentence the sweep may remove must itself
be located here — an exemption carried and never used is a hole rather than a
courtesy. The second leg is positive, because a ban list refuses only what it
lists and a paraphrase walks past it: every sentence putting a species word
beside a word of the declared outside register must be one of the wall
statements themselves. A falsifier that plants an identification-shaped
sentence carrying no banned token at all proves that the positive leg fires.

| wall | banned forms | found | statement |
|---|---|---|---|
| WALL-DYNAMIC | 16 | 0 | THE DYNAMIC VOCABULARY IS BEHIND ANOTHER DOOR.  This unit measures which species can exist -- labels, composites, statistics compatibility -- and nothing about which are realized or with what values.  That question is its successor's and waits on the potential unit's gate. |
| WALL-IDENTIFICATION | 17 | 0 | NO OUTSIDE IDENTIFICATION IS MADE.  No sentence of this paper names an outside theory's particle as an identification of any species it measures.  The pin licenses structural comparisons stamped ANALOGY; this paper draws none, so the licence is registered and unused and the wall's positive leg is total. |
| WALL-SI | 16 | 0 | NO SI NUMBER APPEARS.  Every number in this paper is a count, a group order, a degree, a multiplicity or an exact rational; none carries a unit. |
| WALL-LIMIT | 7 | 0 | NO LIMIT CLAIM IS MADE.  Every group here is finite, every carrier is finite, and no statement is made about any limit. |

The same vocabulary is swept over the serialized receipt as well as over this
paper, with the withholding strings the unit publishes removed first and every
one of them required to be located there.

## 12. The scope of every count

Every integer in this paper is a count, a group order, a degree or a
multiplicity. No count here becomes a probability: no measure over any
configuration space is declared and none is used, so every fraction in this
paper is stamped counting-only and is a ratio of two counts over the same
declared list. The lists are the declared ones: 19 carrier rows, 22 groups,
6 stabilizer shapes and one chain, each named in the choice inventory with
its class and its fibre.
