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
pairs, not only file bytes:** 12 file-bytes anchors, 51 path-value anchors and
22 verbatim-text anchors, 85 anchors in all — each verbatim window pinned by
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
SPC-INVENTORY-22-GROUPS-220-CLASSES-220-SPECIES--SPC-CARRIER-SELECTS-156-OF-246-ROW-SLOTS--SPC-SELECTION-OPEN--SPC-STATISTICS-SPLITS-192|14|9|31 -- INVENTORY=22-GROUPS-AT-18-DISTINCT-ORDERS-1,2,4,8,9,16,18,24,32,108,128,216,1024,4096,4320,8192,32768,362880-OF-WHICH-18-CARRY-A-FULL-EXACT-TABLE-AND-4-STAND-ABOVE-THE-DECLARED-CAP-128-ON-THE-GROUP-THIS-UNIT-ENUMERATES-ELEMENT-BY-ELEMENT;CLASSES=220;SPECIES=220-OVER-THE-22-INVENTORY-GROUPS-COUNTED-ONCE-EACH -- IRREPS=EVERY-TABLE-GATED-BY-TWO-ROUTES-COLUMN-ORTHOGONALITY-AND-ROW-ORTHOGONALITY-AS-SEPARATE-GATES-WITH-THE-CLASS-EQUATION-AND-THE-DEGREE-SUM-BESIDE-THEM-THE-7-STABILIZER-TABLES-GATED-ON-BOTH-ROUTES-TOO;THE-NINE-ACTOR-TABLE-IS-INTEGER-VALUED-WITH-30-CLASSES-AND-30-SPECIES-ITS-DEGREES-RE-DERIVED-BY-THE-HOOK-LENGTH-FORMULA;TWO-ENGINES-AGREE-ON-4-SYMMETRIC-GROUPS -- CARRIER=19-ROWS-OVER-7-DECLARED-CARRIERS;156-OF-246-ROW-SLOTS-FILLED-WHERE-A-SLOT-IS-ONE-SPECIES-AT-ONE-GROUP-CARRIER-ROW-AND-NOT-A-DISTINCT-SPECIES:THE-246-SLOTS-STAND-AT-11-DISTINCT-GROUPS-OVER-133-DISTINCT-SPECIES-OF-WHICH-92-ARE-HOSTED-SOMEWHERE-AND-THE-OTHER-87-INVENTORY-SPECIES-HAVE-NO-CARRIER-ROW-AT-ALL;9-ROWS-LEAVE-A-SPECIES-HOMELESS-THE-WIDEST-ACTOR-9-UNDER-S9-AT-2-OF-30;THE-136-CARRIER-CLASSES-AND-THE-80-AT-THE-EXTENSION-ARE-THE-TRIVIAL-SPECIES-MULTIPLICITY-BY-TWO-ROUTES-AND-THE-WHOLE-MULTIPLICITY-VECTOR-IS-PINNED-BY-THE-ORDERED-PAIR-ROUTE-AT-19-ROWS -- PRICE=ONE-SPECIES:THAT-THE-DISCOUNT-IS-ONE-LABEL-IS-FORCED-BY-INDEX-2-THE-ARENA-GAUGE-GROUP-SITTING-INSIDE-THE-ACTING-GROUP-AT-BOTH-READINGS-WITH-THE-THREE-ROUTES-COINCIDING-AT-300-OF-300-SYNTHETIC-PROBES;WHAT-IS-MEASURED-IS-WHICH-LABEL-AND-WHERE-THE-PARENTS-OBSERVABLE-LIVES:THE-ODD-TWIST-SPECIES-CARRIES-MULTIPLICITY-72-AT-THE-ANCHORED-READING-AND-40-AT-THE-EXTENSION-WHICH-ARE-EXACTLY-THE-PARENTS-IDENTIFIED-ORBIT-PAIRS-AND-IS-THE-SAME-SPECIES-UNDER-THE-STRONGER-SCALAR-READING-AT-ANY-DEGREE;THE-PARENTS-PINNED-OBSERVABLE-OFF-DIAGONAL-QUARTIC-SIGN-IS-NON-ZERO-AT-288-OF-640-POINTS-AND-LIES-IN-1-ISOTYPIC-COMPONENT-AT-THE-ANCHORED-READING;136-OF-136-ORBIT-SUMS-VANISH-AND-ITS-EXPECTATION-AT-EVERY-ONE-OF-THE-136-EXTREME-INVARIANT-MEASURES-IS-0-REPRODUCING-THE-PARENTS-PINNED-[0,0]-AGAINST-THE-OBSERVABLES-OWN-[-2,2] -- IDENTITY=THE-SPECIES-WITH-AN-INVARIANT-VECTOR-ALONG-THE-MEASURED-STABILIZER-LATTICE-ARE-30,29,28,26,22,12,4-OF-30;ALONG-THE-CRYSTALLIZATION-CHAIN-4,12,12,26,30,30-NON-DECREASING-BY-NESTING-AND-ATTAINING-THE-FULL-30-AT-PREFIX-5-AT-1-EXHIBITED-FLAG-OF-AN-UNBOUNDED-FAMILY;BRANCHING-BY-TWO-ROUTES-AT-2610-PAIRS-WITH-0-DISAGREEMENTS-AND-A-TABLEAU-THIRD-ROUTE-AT-210-ROWS -- SELECTION=2154-COMPOSITE-RULES;10-ROWS-CLOSE-AND-9-EXIT;THE-DISTINGUISHED-ROW-ACTOR-9-UNDER-S9-EXITS-TO-2-SPECIES-IT-DOES-NOT-HOST -- STATISTICS=AT-THE-PARENTS-OWN-SELECTION-GRAIN-THE-3-ROWS-THERE-DO-NOT-SPLIT-AT-ALL-29-OF-29-SLOTS-IN-BOTH-SHAPES-AND-0-SYMMETRIC-ONLY-0-ANTISYMMETRIC-ONLY-0-IN-NEITHER;THE-SHAPE-THAT-COMPARISON-NAMES-IS-ANTISYMMETRIC-DERIVED-FROM-0-LEAK-CELLS-AGAINST-81-WHERE-THE-FIRST-COUNT-IS-THE-PARENTS-VACUOUS-ZERO-OVER-AN-EMPTY-FORBIDDEN-SET-AND-THE-PARENTS-SCOPE-IS-THE-CARRIER-GRAIN-ONLY;OVER-ALL-19-DECLARED-ROWS-AS-A-DECLARED-EXTENSION-192-OF-THE-SAME-246-ROW-SLOTS-IN-BOTH-SHAPES,14-SYMMETRIC-ONLY,9-ANTISYMMETRIC-ONLY,31-IN-NEITHER;4-OF-19-ROWS-SPLIT-PROPERLY-AND-ALL-4-LIE-OFF-THAT-GRAIN -- ROUTES=ORBITS-BY-CHARACTER-AND-BY-UNION-FIND-AT-19-ROWS;COMPOSITES-BY-TWO-CONTRACTIONS;SQUARES-BY-FORMULA-AND-BY-COUNTING-ON-THE-PAIR-SET;BRANCHING-BY-RESTRICTION-AND-BY-FROBENIUS-RECIPROCITY;INVARIANTS-BY-TABLEAU-COUNT;ORDERS-BY-CLOSURE-AND-CLASS-EQUATION-AND-ORBIT-STABILIZER;ZERO-DISAGREEMENTS-EVERYWHERE -- CONTROLS=4-SYNTHETIC-ARENAS-THROUGH-THE-SAME-CENSUS-FUNCTIONS-EMITTING-4-DISTINCT-HEADS-WHICH-IS-WHERE-THE-OTHER-WORDS-ARE-WITNESSED;7-OF-8-OUTCOME-ARMS-ARE-WITNESSED-BY-A-DELIVERED-ROW-AT-THE-ROW-LEVEL;AT-THE-ARENA-LEVEL-4-OF-4-HEAD-WORDS-ARE-SETTLED-BEFORE-THE-RUN-3-OF-THEM-BY-ANY-ONE-OF-4-DECLARED-ROWS-INCLUDING-ACTOR-9-UNDER-S9-AND-THE-FOURTH-SINGLE-ARMED-BY-CONSTRUCTION -- SCOPE=THE-KINEMATIC-HALF-ONLY;LABELS-COMPOSITES-AND-STATISTICS-COMPATIBILITY;NO-MASS-NO-SPECTRUM-NO-STABILITY-NO-REALIZED-PARTICLE-CLAIM;NO-STANDARD-MODEL-IDENTIFICATION;NO-SI-NUMBER;NO-CONTINUUM-CLAIM;COUNTS-ARE-COUNTING-ONLY;THE-TABLE-CAP-IS-128-AND-4-ACTING-GROUPS-STAND-ABOVE-IT-WITH-THEIR-ORDERS-RE-DERIVED-AND-THE-CARRIER-SEEING-THEM-THROUGH-A-GROUP-OF-ORDER-8-OR-16-WHICH-CLOSES-THE-HOSTED-SET-AT-THOSE-ROWS-AND-NOT-THE-DENOMINATOR-SINCE-THOSE-4-GROUPS-CARRY-NO-SPECIES-COUNT-HERE-AND-NO-CARRIER-ROW-EITHER;THE-CARRIER-ROW-LIST-IS-A-DECLARATION
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and what could have answered otherwise

The corpus has spent many units measuring symmetries. It has never asked
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

**What could have come out otherwise, and at which level.** The pin's
engraving is met at two levels and they must not be conflated. At the ROW
level this arena carries rows on both sides of every question the head asks,
and the table below names the witnessing row for each arm: 7 of the 8 outcome
arms are witnessed by a delivered row, and the one arm no delivered row can
reach is the refusal, which fires only on an instrument fault. That is a
statement about rows and the table's own column says so. At the ARENA
level it does not: the head's words are aggregates over the declared row list,
and once ACTOR-9-UNDER-S9 was in the declared row list all 4 were settled
before the run — its permutation module is the trivial species plus the
standard one, so some species is homeless; the standard species composed with
itself reaches two species the row does not host, so the selection exits; and
the trivial species lies in the symmetric square and not in the antisymmetric
one, so the statistics split properly. Three of the four words are settled by
any of four declared rows, and the fourth is single-armed by construction.
What demonstrates that the census machinery can emit the other words is the
control set and not this arena. Section nine's "adding a row cannot flip a
word" is the same fact recorded as robustness.

| outcome | arm | live at the row level | witnessed by a delivered row |
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
functions, and it is where the other words are witnessed.** 4 synthetic arenas
are built — a cyclic group acting regularly on its own elements, the same
group acting trivially on two points, a cyclic group with two orbits of
coprime size, and a set of permutations that is measured not to close under
composition — and each is put through the same closure test, the same
character engine, the same decomposition, the same composite census and the
same statistics census as the delivered rows. No field of any control row is
written from outside. Each emits its own head, and the four heads are
distinct.

| row | group order | species | hosted | status | emitted |
|---|---|---|---|---|---|
| CTRL-CYCLIC-3-REGULAR | 3 | 3 | 3 | MEASURED | SPC-INVENTORY-1-GROUPS-3-CLASSES-3-SPECIES--SPC-CARRIER-SELECTS-3-OF-3-ROW-SLOTS--SPC-SELECTION-CLOSED-9-RULES--SPC-STATISTICS-SPLITS-3\|0\|0\|0 |
| CTRL-CYCLIC-3-TRIVIAL-ACTION | 3 | 3 | 1 | MEASURED | SPC-INVENTORY-1-GROUPS-3-CLASSES-3-SPECIES--SPC-CARRIER-SELECTS-1-OF-3-ROW-SLOTS--SPC-SELECTION-CLOSED-1-RULES--SPC-STATISTICS-SPLITS-1\|0\|0\|2 |
| CTRL-CYCLIC-6-TWO-ORBITS | 6 | 6 | 4 | MEASURED | SPC-INVENTORY-1-GROUPS-6-CLASSES-6-SPECIES--SPC-CARRIER-SELECTS-4-OF-6-ROW-SLOTS--SPC-SELECTION-OPEN--SPC-STATISTICS-SPLITS-6\|0\|0\|0 |
| CTRL-NOT-A-GROUP | 2 | 0 | 0 | BLOCKED | SPC-BLOCKED-AT-THE-GROUP-CLOSURE |

## 2. The inventory: every measured symmetry group, with its order re-derived

22 groups, 18 of which carry a full exact character table and 4 of which — the
acting groups at the plaquette and site grains — stand above the declared cap
of 128 on the group this unit will enumerate element by element. They carry
220 conjugacy classes and 220 species in all — and at the eighteen groups that
carry a table the class count and the species count agree group by group,
which is itself one of the census gates.

**No order in this table is typed.** 10 of the twenty-two groups have their
order re-derived four ways: by the length of their own closed element list, by
the sum of their own conjugacy class sizes, by the sum of the squares of their
species degrees, and by the product of one declared point's orbit with that
point's stabilizer. 8 rows are indexed by partitions rather than enumerated as
permutations — the nine-actor group and the seven Young subgroups — and take
three routes, the first of which is a product of factorials rather than an
element list: the order by construction, the sum of the class sizes, and the
sum of the squares of the degrees; no permutation is ever written down for
them. The 4 acting groups above the table cap take none of those four: their
order is the number of distinct actions on the stencil datum, re-derived below
and gated against the parent's receipt row by row.

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
and it is priced as one; what makes it harmless where it is harmless is a
measurement rather than a promise. At every one of the six (grain, reading)
rows the subgroup of coin maps a uniform configuration can be moved by is the
same group — of order eight at the anchored reading and sixteen at the
extension — it is closed, and the partition it induces on the carrier is
exactly the partition the whole acting group induces there. That is the
mechanism behind the parent's own grain-invariance:

> The partition is the same 136 classes at all three grains

What that measurement closes is the carrier's **orbit structure** and its
**hosted set**: a permutation module that factors through an image of order
eight or sixteen has exactly that image's constituents, inflated, so the
hosted species at a capped row would be the hosted species at the
corresponding uncapped one. What it does not close is the **denominator**. The
four acting groups above the cap carry no table here, so how many species each
of them has — and therefore how many a carrier would leave homeless — is not
measured, and none of the four appears among the nineteen carrier rows; the
two acting groups that do appear are the two at the link grain.

| grain | reading | gauge image order | chart stabilizer order | acting group order | the group the carrier sees | induced classes on the carrier |
|---|---|---|---|---|---|---|
| LINK | ANCHORED | 8 | 1 | 8 | 8 | 136 |
| LINK | EXTENSION | 8 | 4 | 16 | 16 | 80 |
| PLAQUETTE | ANCHORED | 512 | 2 | 1024 | 8 | 136 |
| PLAQUETTE | EXTENSION | 512 | 8 | 4096 | 16 | 80 |
| SITE | ANCHORED | 4096 | 2 | 8192 | 8 | 136 |
| SITE | EXTENSION | 4096 | 8 | 32768 | 16 | 80 |

## 3. The census: two routes, and two engines

Every table this unit publishes is gated twice over, the seven stabilizer
tables among them, and the two gates are separate rows of the ledger because
they are not the same measurement. Row orthogonality says the species are an
orthonormal family. Column orthogonality says something the first cannot: that
the family is **complete**, since a table with a species missing still has
orthonormal rows and immediately fails on its columns. The class equation and
the sum of the squares of the degrees close the arithmetic beside them.

There are two engines. The first takes a group as an explicit element list
with a product, measures its conjugacy classes and its class multiplication
coefficients, splits the common invariant subspaces over a prime field chosen
larger than twice the integer square root of the order, and lifts each value
out of the prime field by a finite Fourier inversion whose coefficients are
integers bounded by the degree. The second never sees a group element: it
recurses on rim hooks. **They are required to agree on every symmetric group
of the declared cross-engine list**, which is a declaration and not a size
limit: the largest of them has fewer elements than the largest group this same
instrument enumerates for its first engine.

| row | order | classes dixon | classes murnaghan nakayama | tables agree |
|---|---|---|---|---|
| S2 | 2 | 2 | 2 | yes |
| S3 | 6 | 3 | 3 | yes |
| S4 | 24 | 5 | 5 | yes |
| S5 | 120 | 7 | 7 | yes |

The nine-actor table is the classical one and carries an independent route of
its own: 30 classes and 30 species, its degrees re-derived by the hook-length
formula, and the squares of its degrees sum to 362880.

## 4. The carrier decomposition — the heart

A species is **hosted** on a carrier when it appears with non-zero
multiplicity in that carrier's permutation module, and **homeless** when its
multiplicity there is zero. Both words are statements about the decomposition
of a finite-dimensional module and about nothing else. Neither asserts nor
implies that any state exists, that anything occupies a carrier, or that any
species is realized in any sense beyond appearing in a decomposition: where
this paper writes that a carrier hosts a species, it means multiplicity
greater than zero and it means nothing else.

A carrier is a finite set the corpus committed and a group that acts on it.
Its permutation module decomposes into species exactly, and the multiplicity
of the trivial species is the orbit count — which is the characterisation the
parent states and this unit turns into a measurement:

> A measure is invariant under a group acting on a finite set if and only if
> it is constant on the orbits.

So the parent's own carrier numbers come back here as **multiplicities**, and
each is computed twice: once as a character inner product and once by a
union-find pass that never evaluates a character. The whole multiplicity
vector carries a route of its own beside them: for a permutation module the
sum of the squared multiplicities is the number of orbits on ordered pairs of
carrier points, and that count is taken at every row by flooding the pair set
with no character in sight.

**The census runs at two counts, and they are not the same count.** It runs
at 19 carrier rows over 7 declared carriers — 19 (group, carrier) pairings
over 11 of the 22 inventory groups, six of which are censused on more than one
carrier —
so the nineteen rows offer 246 species-slots — the row-sum of each row's own
irrep count, a slot per (species, carrier) pairing and not a count of distinct
species — and 156 of those slots are filled. Behind the 246 slots stand 133
distinct species; the remaining 87 species of the inventory belong to the 11
groups that have no carrier row here at all. Because a species can be hosted
on one carrier and homeless on another, the filled-slot count is not a species
count and must not be read as one: taken as a union of characters group by
group, 92 distinct species are hosted somewhere in this table.

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
actors under the whole symmetric group host 2 of 30 species, and the other 28
are homeless there. 9 of the 19 rows leave at least one species homeless.

**Homelessness is a property of the pair and not of the group.** The same
chart group of order 128 hosts 10 of its twenty species on the thirty-two
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

This unit resolves both into a single label, and **the price is one species**.
The sentence needs grading, because half of it is a theorem and half of it is
a measurement.

**That the discount is ONE label is forced; which label it is, is measured.**
The arena's own gauge group has index two in the acting group at both
readings — four inside eight anchored and eight inside sixteen at the
extension, both containments measured here — and for an index-two pair acting
on any finite set three quantities coincide by theorem: the drop in the orbit
count, the number of merged orbit pairs, and the multiplicity of the unique
character trivial on the subgroup. That is demonstrated here on synthetic sets
sharing nothing with this arena — cyclic groups of even order acting on
disjoint unions of cycles, enumerated by cycle type, with the three quantities
computed by three separate routes — and the identity held at 300 of 300
synthetic probes. So 72 and 40 were going to agree with the parent's
identified-pair counts whatever this arena had been. What could have come out
otherwise, and did not, is the identity of that character: it is the one on
which the odd twist acts by minus one while every twist the torus itself
carries acts trivially, and it carries multiplicity 72 at the anchored reading
and 40 at the extension, which is the drop in the trivial multiplicity between
the arena's own gauge group and the acting group. The filter that names it is
run twice, and the stronger reading returns the same species: not only the
one-dimensional species with those two values, but any species on which the
odd twist acts by the scalar minus one at any degree at all.

| row | the species index | multiplicity | the arena groups orbit count | the acting groups orbit count | the parents identified orbit pairs |
|---|---|---|---|---|---|
| COIN-640-UNDER-ACTING-LINK-8 | 0 | 72 | 208 | 136 | 72 |
| COIN-640-UNDER-GAMMA-16 | 1 | 40 | 120 | 80 | 40 |

The species index is this unit's own table row index for that group and is
engine-relative; the species itself is fixed without reference to any ordering
as the unique one-dimensional species with the value minus one at the odd
twist and plus one at the twist the torus carries, and plus one at the swap at
the extension.

**And the parent's one pinned observable lives in that same block, which is
not forced by anything.** Rebuilt here from its own definition, it is non-zero
at 288 of the 640 coins, and — measured at the anchored reading — its
component in every other species vanishes identically: **the observable lies
in that species and in no other**. Its three declared invariance properties
hold pointwise on the rebuild: it is unmoved by the even twist, unmoved by the
swap, and reversed at every one of the 640 coins by the odd twist. The
parent's pinning follows, and the derivation is carried here to the value it
reproduces: an admissible weight system is an invariant vector, an invariant
vector is constant on the orbits, and 136 of the 136 orbit sums vanish, so the
expectation is the same number at every extreme point of the invariant
simplex, and that number is zero — the parent's [0, 0] against the
observable's own range [-2, 2]. The same conclusion follows from orthogonality
alone, since an invariant vector lies in the trivial species and distinct
isotypic blocks pair to zero.

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
largest measured stabilizer. That direction is a theorem and not a
coincidence: an invariant vector for a larger stabilizer is an invariant
vector for every smaller one. What is measured is the seven values.

The parent's crystallization profile is rebuilt here by an exhibited flag of
partitions of the nine actors, each step refining the one before, so the
stabilizers are genuinely nested and the sequence is a restriction chain
rather than six unrelated subgroups. The chain runs from 4 at the largest
measured stabilizer to 30 at crystallization, and the count never falls along
it — it never falls by the same theorem, since the flag refines at every step.
The chain is a nesting of subgroups indexed by prefix length and not a process
in time: **nothing is destroyed at the first prefix and nothing is returned at
the fifth**, and the count at each prefix is a function of that prefix's
stabilizer alone. Read from the largest measured stabilizer down to the
trivial one the count rises to the full thirty and attains it at prefix five;
read the other way, which is the reading this section's first table takes, it
falls. Both readings are of the same six numbers. The flag is one exhibit from
an unbounded family and the six counts move with it; what does not move is the
theorem that they cannot fall. The admissibility axis is where the chain
matters, because the parent measured that

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
homeless species, and the two directions of that correspondence are not
equally deep. Forward it is arithmetic: a complete hosted set has nowhere to
exit to, and that half could not have come out otherwise. The converse is the
measured half — that a row with a homeless species does have some composite
leaving its hosted set — and it holds at every one of the nine rows where it
is tested. At the actor row the hosted set is the trivial species and the
standard one, and **the composites do not close**: the standard species
composed with itself reaches 4 species, of which 2 are hosted and 2 are not.

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

The occupancy terminal selected a shape, and it selected it under three
conditions this unit must carry. It selected at **its own carrier grain**, and
its sentence for the comparison is quoted here:

> the symmetric shape leaks at 81 cells at 5 of the 6 coin classes and the
> antisymmetric shape leaks at 0, so a hard core there would select

The first of those two counts is a **vacuous** zero and the parent published
it as one:

> the wedge has no doubly occupied configuration to leak into at all — its
> forbidden set is empty, which is why its 0 is a vacuous zero and is
> published as one.

At the actor's grain it measured the opposite of a selection, at 6 of 6 coin
classes:

> At the actor's grain, both shapes leak, and neither is a law.

and its own verdict on the shape at this arena is that it is a declaration and
not a theorem of the coupled theory:

> it is a declaration, made at a grain the committed dictionary names and
> never measures.

Which shape that comparison names is **derived** here from those two counts
and not typed: the shape that leaks at 0 cells against 81 is the antisymmetric
one. The compatibility census then asks, at every carrier row, which species
the two squares of the module can carry — the symmetric square, the
antisymmetric square, both, or neither — with the split computed twice at
every class, once by the character formula and once by counting fixed pairs on
the pair set itself.

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

**The on-grain result is empty.** The rows at the parent's own selection grain
are found here by the parent's own published cell count rather than named, and
there are three of them. At the 3 rows at that grain the two squares carry the
same 29 species and the split is empty — no species is symmetric-only, none
antisymmetric-only, none in neither — so the selection costs no label where
the parent selected it.

**The rest of the table is a declared extension of the parent's comparison to
grains its selection does not reach.** Over all 19 declared rows: 192 species
in both shapes, 14 in the symmetric shape alone, 9 in the antisymmetric shape
alone and 31 in neither, and 4 of the 19 rows split properly — and all 4 rows
that split lie at grains the selection does not reach: two lattice rows under
the chart group of order 128, the nine sites under the arena group, and the
actor row. On every row of the gauge arena the two shapes carry the same
species, so exclusion costs no label there.

At the actor row the trivial species lies in the symmetric square and not in
the antisymmetric one, so of the two species that carrier hosts only one
survives into the antisymmetric square. That is a statement about the
antisymmetric square at the actor grain. **It is not an application of the
parent's selection there**, and the parent measured that its selection does
not reach that grain.

## 9. What this decides, and what it does not

**Decided, at the declared scope.**

- **The inventory exists and is exact.** Twenty-two measured groups, their
  classes and their species, every table gated twice over and two engines
  agreeing on every symmetric group of the declared list.
- **Hosting is a property of the pair.** A group's species are fixed by the
  group; which of them a carrier hosts is fixed by the carrier, and the
  corpus's two sides sit at opposite ends of that scale.
- **The parent's discount and its pinned observable are one label.** That the
  discount is one label is forced by index two; which label it is, and that
  the observable lies in that label alone, are the measurements, and the
  expectation they force is the parent's own value.
- **The identity lattice acts on the inventory monotonically** — measured at
  seven values, monotone by theorem — and the crystallization chain never
  falls along the flag that exhibits it.
- **The composites close exactly where the hosted set is complete.**
- **Exclusion costs no label at the parent's own grain.** It costs none at any
  of the four coin rows either, nor at any row under a chart or translation
  group of order at most thirty-two; the four rows where the two squares carry
  different species are the two lattice rows under the chart group of order
  128, the nine sites under the arena group, and the actor row.

**Not decided, and named.**

- **Which species are realized.** This is the kinematic half only: no mass, no
  spectrum, no stability and no realized-particle claim is made here. That
  question belongs to this unit's successor and waits behind the potential
  unit's gate.
- **The four acting groups above the cap.** Their orders are re-derived here
  and their own species censuses are not computed. What is measured is that
  the carrier sees them through a group whose table is computed, which closes
  the hosted set at those rows and not the denominator; none of the four is a
  carrier row here, so no carrier row is affected, and their abstract
  inventories remain open.
- **The carrier row list.** It is a declaration with an unbounded fibre, and
  the head's counts move with it. Both arms of every outcome word are
  populated by delivered rows, so adding a row cannot flip a word, but it
  moves the numbers — and, as section one says, the words were settled by the
  list before the run.
- **The decomposition grain.** The nine-actor grain is granted by the parent;
  which subsystems there are is another unit's question and the actor row's
  species count would move with it.
- **The glued-world census.** The sector union's automorphism group is larger
  than any single sector's, which the pin's successor note registers as
  implying an exchange parity no single sector has. That census belongs to a
  successor chartered after both panels rule; it is not run here and this unit
  measures nothing about it.

## 10. The instrument

The instrument is `v14/code/spc_exact.py`, and its contract is the era's
minimum: a delivery run that is the only writer, a `--no-write` twin, a
falsification self-test that corrupts one anchor class in memory and must die
writing nothing, a per-mutant runner, an all-mutants sweep, gate and mutant
listings, and a `--verify-paper` mode. Unknown flags exit 2, and so does a
repeated `--mutant`. The exit conventions invert the usual reading and are
therefore disclosed in the usage string, in the receipt and here: the delivery
run exits 0 on success and 1 on any refusal, writing nothing; `--selftest`
exits 0 when every anchor class is fatal; `--mutant` exits 0 when the named
mutant *dies* on its declared target.

The gate ledger is chained row by row and that chain is verified, in the run
and again at the disk boundary from the bytes read back. 45 gates close before
the paper gates, and 8 paper gates, 1 receipt-wall gate and 3 closing gates
follow — the last three being the seal, the recomputation of the manifest's
totality at promotion time, and the artifact integrity check, none of which
can be inside the ledger they close over. 28 objects are sealed when the
ledger shape is taken, and the manifest is total: every other top-level key is
named in the declaration with the reason it cannot be sealed. Totality is not
computed once and trusted afterwards. It is **recomputed from the bytes that
will cross the disk boundary**, after every insertion into the receipt is
finished, and again from the bytes read back — because a key added after the
seal gate is invisible both to that gate and to a byte comparison of the
receipt against itself. The declaration is checked in the other direction too:
every key it exempts must actually be published.

73 declared mutants, each dying at the gate it was declared to falsify. The
registry is checked total against the instrument's own syntax tree, so a
falsifier cannot exist as an unswept branch and a switch the scan cannot read
is fatal rather than forgiven; the function inventory is checked total the
same way. Each mutant's published description names the exact token it plants
and that token is located in the source text. Three of them are worth naming
here. One drops a species from the nine-actor table, which leaves row
orthogonality intact and dies on the column route alone — that is what makes
the two orthogonality gates independent rather than duplicated. One shifts a
non-identity value of a stabilizer table by one, leaving its degrees, its
class sizes and the branching engine's own character untouched, so only those
same two routes can catch it. One inserts a top-level key into the receipt
after the seal gate has computed totality, and dies where totality is
recomputed.

12 file-bytes anchors, 51 path-value anchors and 22 verbatim-text anchors, 85
anchors in all, each verbatim window pinned by its own digest and its own
character count against a declared floor, each located exactly once under
whitespace and markdown-prefix normalisation, each perturbed at a
content-bearing token and required to stop being locatable, and each bound to
the gate that consumes it. Every quotation this paper makes is bound twice
over: to the pinned window it must lie inside, and to the position in the
declared attribution order it must occupy, so two parents' sentences exchanged
under each other's introductions stop matching.

**The referent gate.** A numeral-coverage gate cannot bind a numeral to its
subject: its pool is every integer the run computed anywhere, so a true number
re-paired with the wrong universe passes it. This unit therefore registers the
universes its headline numerals count in — species of the inventory counted
once per group, slots over the declared rows, distinct species behind those
slots — and requires that a sentence carrying numerals from two of them be a
claim rendered from the receipt, and that every "A of B" the paper writes be a
part-and-whole pair the run actually measured.

**The choice inventory.** 14 construction choices are inventoried, of which 5
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
| THE-CROSS-ENGINE-LIST | DECLARED-AND-DISCLOSED | UNBOUNDED | 4 | no | yes |
| THE-INDEX-TWO-PROBE-FAMILY | DECLARED-AND-DISCLOSED | UNBOUNDED | 300 | no | yes |

## 11. The walls

Each wall has two legs. The first is a list of banned forms, matched at word
boundaries over this paper's own characters with the declaring sentences
removed first, and every declaring sentence the sweep may remove must itself
be located here — an exemption carried and never used is a hole rather than a
courtesy. The second leg is positive, because a ban list refuses only what it
lists and a paraphrase walks past it: every sentence putting a species word
beside a word of the declared outside register must be one of the wall
statements themselves. A falsifier that plants an identification-shaped
sentence carrying no banned token at all proves that the positive leg fires,
and two more plant the upgrade this unit's own vocabulary invites — one
carrying the word the ban list was built around, one carrying none of it and
saying the same thing another way — and both die on the first leg, which is
why that wall bans a family of forms and not a single word.

| wall | banned forms | found | statement |
|---|---|---|---|
| WALL-DYNAMIC | 35 | 0 | THE DYNAMIC VOCABULARY IS BEHIND ANOTHER DOOR, AND SO IS THE WORD THIS WALL WILL NOT WRITE.  This unit measures which species a carrier can HOST -- labels, composites, statistics compatibility -- where hosted means multiplicity greater than zero in a permutation module and means nothing else.  Whether a species is anything more than that is its successor's question and waits on the potential unit's gate; the whole family of words that would say so is on this wall's own ban list, and every sentence of this paper carrying one of them is a declared exemption located there. |
| WALL-IDENTIFICATION | 24 | 0 | NO OUTSIDE IDENTIFICATION IS MADE.  No sentence of this paper names an outside theory's particle as an identification of any species it measures.  The pin licenses structural comparisons stamped ANALOGY; this paper draws none, so the licence is registered and unused and the wall's positive leg is total. |
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
declared list, and the stamp is a gate rather than a string in a receipt. The
lists are the declared ones: 19 carrier rows, 22 groups, 7 stabilizer shapes —
the six nontrivial ones the parent measured and the forced-trivial one — and
one chain, each named in the choice inventory with its class and its fibre.
