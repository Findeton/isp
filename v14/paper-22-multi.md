# R4c — two excitations: statistics as a measurement

*v14, the limit programme, paper 22. Instrument:
`v14/code/r4c_multi_exact.py`; artifacts `r4c_multi_output.txt` and
`r4c_multi_receipt.json`. Exact arithmetic throughout: the field is
Q(ζ₈) carried as integer four-tuples over a power-of-two denominator, every
Born shadow and every defect is a dyadic rational, and there is no float
anywhere. Pin: `v14/note-r4c-pin.md`.*

---

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field, and the complete string —
head included — is compared for equality against an *independent
reconstruction* that derives the head by its own copy of the head law, reads
only the serialized receipt, and shares no helper, no input and no typed value
with the builder:

```
R4C-STATISTICS-BOTH-ADMITTED<EXCHANGE=COMMUTES-AT-64-OF-64(FORCED-BY-THE-FREE-LIFT);BOTH-SECTORS-CLOSED-UNITARY-STOCHASTIC=64-OF-64(FORCED-BY-THE-FREE-LIFT);DECOMPOSITION=256=136+120(NO-THIRD-SECTOR-AT-TWO-EXCITATIONS;PERMUTATION-GROUP-ONLY-NO-BRAID-CLAIM)|OCCUPANCY=CEILING-DECLARED-NOT-ANCHORED(STAGE-DECLARES-NO-OCCUPANCY-KEY-IN-27);AT-CEILING-1-SYMMETRIC-LEAKS=48-OF-64-EXACTLY-THE-NON-MONOMIAL(THEOREM-FOR-EVERY-UNITARY-240-WITNESSES+3364-COMPOSITES;THE-48-IS-THE-FAMILY);ANTISYMMETRIC-LEAKS=0-OF-64(FORCED-NO-DOUBLY-OCCUPIED-CONFIGURATION);THE-TWO-CEILINGS-AGREE-AT-ONE-EXCITATION=16-OF-16-CONFIGURATIONS-AND-AS-OBJECTS-AT-64-OF-64-GENERATORS;AND-DIFFER-AT-TWO=136-VS-120;FORCING-THE-CEILING=OPEN|DISCRIMINATION=THE-SHAPES-DIFFER-CELL-BY-CELL-AT-1764-OF-3364-PAIRS=EXACTLY-THE-TWO-EXCITATION-DEFECT-SET(SET-EQUALITY);AGREE-ONLY-WHERE-BOTH-DEFECTS-VANISH=1600;VALUE-MULTISETS-DIFFER-AT-588-OF-3364=EXACTLY-THE-SINGLE-EXCITATION-DEFECT-SET(SET-EQUALITY);MULTISETS-AGREE-AT-2776;AT-THE-LOCAL-GRAIN-SHAPES-DIFFER-AT-240-OF-360-OVERLAP-2-ROWS(SO-THE-COEXTENSION-IS-CIRCULANT-STRATUM-SCOPED);SPECTRA-DIFFER-AT-16-DOUBLED-MOMENTUM-CELLS-AT-58-OF-58-FAMILIES|DEFECT=DOES-NOT-COMPOSE-IT-COMPLETES;NONZERO=1764-OF-3364-IN-BOTH-SHAPES=BOTH-LEGS-NON-MONOMIAL(0-MISMATCHES-OF-6728-PER-PAIR-TESTS;=42-SQUARED);GENUINE-TWO-BODY=1176;LOSSES=0;ORDERED-SECTOR=DERIVATION-LAW-EXACT-3364-OF-3364-AND-NO-GENUINE-TWO-BODY(THEOREM-AT-EVERY-N-BY-TELESCOPING;THE-SPLITTING-HAS-A-ONE-PARAMETER-FIBRE);VALUES=ANTISYMMETRIC-28-DISTINCT+SYMMETRIC-39-DISTINCT-IN-THE-SECTOR(30-ON-THE-HARD-CORE-BLOCK)-ALL-RATIONAL;PARENT-SINGLE-EXCITATION=588-OF-3364-REPRODUCED-WITH-ITS-WHOLE-VALUE-MULTISET|OVERLAP=R5-LAW-SURVIVES-THE-LIFT=NO-DEFECT-AT-OVERLAP-LE-1-AT-42840-OF-42840-ROWS-BOTH-SHAPES;AT-OVERLAP-2=360-OF-360-CARRY;WINDOW=EVERY-2-SITE-SUPPORT-43200-ROWS-EXHAUSTIVE-IN-GEOMETRY;THREE-SITE-FULL-SUPPORT=EMPTY-OVER-THE-ALPHABET-1536-ROWS-SWEPT;COIN-PAIRS=3-DECLARED-SAMPLE-OF-512-INTERFERING-COINS-EACH-GATED-SEPARATELY;R5-18-ROW-SAMPLE=CITED-NOT-RE-RUN|MOTION=EIGENPHASES-ADD-EXACTLY(ANTISYMMETRIC=6960;SYMMETRIC=7888;FAILURES=0)(FORCED-BY-FUNCTORIALITY);SPEED-SPECTRUM=0+1+2-UNCHANGED-AT-TWO-EXCITATIONS(CEILING-FORCED-BY-THE-DUAL-TORUS;ALL-THREE-VALUES-ATTAINED);VELOCITY-DOES-NOT-ADD=7168-OF-29696-CELLS-AT-RAW-ADVANCE-PAIRS-(2,2)-AND-(6,6)-ONLY(THE-4096-CELLS-AT-(4,4)-ARE-EQUAL-AND-NONZERO-AND-DO-NOT-FAIL);CONTACT-HANDLE-MOVES-SYMMETRIC-DEFECT-AT-588-OF-3364-AND-ANTISYMMETRIC-AT-0(THE-MOVED-SET-IS-THE-SINGLE-EXCITATION-DEFECT-SET-BY-SET-EQUALITY);R4B-REPRODUCED=320-TIE-CELLS-IN-19-FAMILIES-OF-58|SCOPE=D=2;L=4;FIELD=Q(ZETA-8);ALPHABET=25;GENERATORS=64;STENCIL=3-TERM-AXIS;EXCITATIONS=2;SECTORS=ORDERED+SYMMETRIC+ANTISYMMETRIC;LIFT=FREE(U-TENSOR-U)-WITH-DISTINGUISHABLE-AND-CONTACT-LIFTS-CENSUSED;OCCUPANCY-CEILING=DECLARED;VERDICT-BEARING-STRATUM=THE-58-CIRCULANTS;VELOCITY-READING=FORWARD-DIFFERENCE-WITH-TIE-AVERAGED-INHERITED-AS-DECLARED;NO-TRANSPORT-NUMBER-INHERITED;CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-PARTICLE-CLAIM;SHAPE-WORDS-ONLY;N=2-ONLY-NO-GENERAL-N-CLAIM;NO-BRAID-CLAIM;NO-CONFIGURATION-SPACE-TOPOLOGY;COUNTS=COUNTING-ONLY-NO-MEASURE-DECLARED;NO-CONFIGURATION-MEASURE;NO-ACTION;NO-COUPLING>
```

(The string is one line; the gate compares that complete string, and the
paper's fenced blocks are compared to it as a multiset.)

---

## The Composition Law Cannot Choose a Statistics, and the Defect Can Read One

**The parent unit named the way out of its own arena and did not take it.** R4's
terminal register lists exactly three routes off its frozen single-occupation
stage, and the cheapest is a two-excitation sector. R5 declared one — the
antisymmetric sector, on 120 two-excitation states — carried it in its choice
inventory as a free axis with fibre two, and ran it as an eighteen-row sample.
Neither unit asked which sector the substrate itself allows. This unit asks, and
the answer has three parts.

**First: the composition law admits both shapes and selects neither.** The
substrate's own lift of a generator to two excitations acts on each excitation
separately, and the exchange operator commutes with that lift at every
generator in the pool. Both exchange sectors are invariant, the restriction is
unitary in both, and its Born shadow is stochastic in both. The ordered sector
splits as 256 = 136 + 120 and into nothing else, so at two excitations there is
no third, parastatistics-shaped place to stand. The composition law is silent
— and it is silent for a reason stronger than a census: the free lift commutes
with exchange identically, so no substrate that lifts freely can select an
exchange shape.

**Second: what selects is the occupancy ceiling, and the stage anchors none.**
Declare that a site may hold two excitations and both shapes survive. Declare a
hard core — at most one — and the symmetric shape leaks at 48 of the 64 generators,
which are exactly the non-monomial ones, while the antisymmetric shape closes at
every generator because it has no doubly occupied configuration to leak into.
That split is a theorem about the symmetric square of *any* unitary, not a
property of this family; what this family contributes is its size. The ceiling
is therefore the coordinate that decides, and it is *not* anchored: the record
layer declares the site lattice, the link set, the chart group and the lapse
family, with 27 declaration keys, not one of them occupancy-shaped. Worse for
anyone hoping the parent decided it: the two ceilings have the *same*
one-excitation restriction, configuration for configuration and matrix for
matrix, so no single-excitation measurement whatever — not one of R4's, not one
of R4b's — could have told them apart. The parent's whole arena is a fixed
point of both.

**Third, and this is the unit's finding: the two shapes are told apart by the
composition defect, cell by cell, at exactly the pairs whose two legs are both
non-monomial.** At two excitations the defect does not compose. It *completes*:
1764 of the 3364 ordered pairs carry a nonzero two-excitation defect, against
588 at one excitation, with 1176 pairs that are genuinely two-body — pairs whose two legs compose
without interference at one excitation and interfere at two — and zero losses.
The two-excitation defect is nonzero at exactly the pairs whose legs are both
non-monomial, with no mismatch over the 6728 per-pair tests, so the count is the
square of the non-monomial population and the Markovian control survives the
lift untouched. On the *ordered* sector the defect composes exactly, by a
derivation law, and carries no genuine two-body defect at all: the whole excess
is carried by the exchange symmetrisation and by nothing else. And on the same
shared block, in the same row and column ordering, the two shapes' defects
**differ cell by cell at 1764 of the 3364 ordered pairs and agree at 1600** —
they agree only where both defects vanish. The differing set is the two-excitation
defect set itself. Statistics is not fixed by this substrate; it is measurable
on it, wherever the two-excitation defect lives at all.

A coarser reading of the same comparison is confined to a smaller set, and it
is that reading which lines up with the substrate's own interference. Compared
as **value multisets** — the relabelling-invariant comparison — the two shapes'
value multisets differ at 588 of those 3364 ordered pairs, and that is not
merely the same count as the single-excitation defect set but *that set*, element for
element. A third probe lands on the same set again. The declared contact
interaction — a phase on the doubly occupied configurations, invisible to the
antisymmetric shape entirely — moves the symmetric shape's two-excitation
defect at exactly those pairs, again as a gated set equality. Three ways of
asking about the doubly occupied channel; one answer, and one set. That
coextension is a statement about the circulant stratum: the unit's own local
window carries interfering rows on which the two shapes agree, and section 7
measures them.

---

## 1. The question, and what would have answered it the other way

The pin asks which exchange symmetry the substrate's composition law forces or
admits on two-excitation states, whether the defect composes, and how the motion
composes. Four outcomes are pre-registered, and the instrument parses their
names from the pin's own bytes rather than typing them:
`R4C-STATISTICS-FORCED-ANTISYMMETRIC`, `R4C-STATISTICS-FORCED-SYMMETRIC`,
`R4C-STATISTICS-BOTH-ADMITTED`, `R4C-STATISTICS-NEITHER-...`, together with
`R4C-BLOCKED-AT-...`.

The head is derived from two measured predicates — does the antisymmetric sector
live, does the symmetric one — and cannot be typed. It is exercised on four
arenas, and it returns a *different* pre-registered name on each. That is what
makes the reachability requirement honest here: every branch is reached on a
constructed arena, not on a synthetic census.

| arena | antisymmetric | symmetric | the head the law returns |
|---|---|---|---|
| `A1-FREE-LIFT-CEILING-2` | lives | lives | `R4C-STATISTICS-BOTH-ADMITTED` |
| `A2-FREE-LIFT-CEILING-1-HARD-CORE` | lives | dies | `R4C-STATISTICS-FORCED-ANTISYMMETRIC` |
| `A3-ONE-SITE-LATTICE` | dies | lives | `R4C-STATISTICS-FORCED-SYMMETRIC` |
| `A4-DISTINGUISHABLE-LIFT` | dies | dies | `R4C-STATISTICS-NEITHER-INVARIANT` |

The first row is the declared verdict arena. The second is the same lift under a
tighter occupancy declaration. The third is a degenerate control, declared as
such, and it is the exclusion read as a dimension count: the antisymmetric
sector on *n* sites has dimension *n*(*n*−1)/2, which is zero at one site, while
the symmetric sector has dimension one there. The fourth gives each excitation
its own generator; the exchange operator then fails to commute with the lift at
3306 of 3306 ordered pairs of distinct generators, and both off-block matrix
elements are measured there, so that **neither sector is invariant at 3306 of
3306** is a second measurement and not the first one read twice.

A word on what this unit does not buy. Reading a statistics is not building a
particle. The words *fermionic-shape* and *bosonic-shape* are shape words for
the antisymmetric and symmetric sectors, and the paper says nothing past them.
No state is prepared, no configuration measure exists, and the sector is two
excitations — the argument that forbids a third shape is an argument about two.

## 2. The arena, inherited and rebuilt

Everything about the stage is inherited at hash-pinned paths and nothing about
it is retyped. The spatial dimension is read from the record layer's own
declarations; the lattice size is read from the parent's measured admissible
set; the alphabet, the pool, the stencil, the sector, the Markovian control and
the connective come from the parent's receipt. The connective clause travels
verbatim, as the parent's adjudication requires, and the three copies of it —
the parent's bytes, this unit's scope segment and this span — are compared:
`CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))`. R4b's velocity convention
is inherited **as declared** — the forward difference with the antipodal tie
averaged, derived from R4b's own anchored values rather than retyped — and no
new selection claim is made about it; the R4b scope stamp binds, and **no
transport number is inherited**. R5's eighteen-row two-excitation table is
cited and not re-run, and the row count is parsed from R5's own sentence.

The family is **rebuilt, not imported**. The parents' programs are read as bytes
for their digests and are never imported and never executed. The coefficient
alphabet, the nine axes, the unitarity criterion, the gauge quotient and the six
controls are reimplemented here from the definitions in the parents' papers,
over an independent exact representation of the same field, and the rebuild is
then gated against the parent's rows object by object: a bijection in both
directions between the rebuilt coefficient maps and the parent's 58 circulant
rows, agreement on axis, axis order, support, radius and monomiality for every
matched pair, the six controls in the parent's construction order, and the
monomial sub-family equal to the parent's declared Markovian set name for name.

**The two-excitation sectors.** Three are built over the same single-excitation
stage. The ordered sector carries |X|² = 256 configurations; the symmetric
sector, in the normalised basis, carries 136; the antisymmetric sector carries
120. The free lift of a generator *U* is *U* ⊗ *U*, and each sector carries its
restriction. All three restrictions are functors, which is what makes the
composed segment well defined in each.

## 3. The exchange census

The census is taken per generator, and the gate binds generators rather than the
tally.

The exchange operator commutes with the free lift at 64 of 64 generators; both
sectors are invariant, the restriction is unitary and its Born shadow
stochastic in both, at every one of them. **The commutation is forced**, and the
paper says so rather than reporting it as a finding: *P*(*U* ⊗ *U*)*P*⁻¹ =
*U* ⊗ *U* holds for every *U* whatever, so it is an identity of the free lift
and not a property of this family. So are its corollaries — the restriction of
a unitary to an invariant subspace is unitary, and the Born shadow of a unitary
is stochastic — and the head clause that reports them carries the same tag. The
whole of this section is registered as a disclosure with its forcing named, and
the measured content of the unit lives in sections 5 to 9.

The decomposition into a 136-dimensional symmetric sector and a
120-dimensional antisymmetric one is likewise structural and is reported as
such. It has one consequence worth stating plainly: at two excitations the
symmetric group on the excitation labels has exactly two irreducible characters,
so the `NEITHER` outcome cannot arise here as a *third sector*. It arises only
as a failure of invariance — which is what the distinguishable arena exhibits.
What excludes a third shape here is that exchange is implemented by a single
finite operator with square the identity, on a discrete lattice with no exchange
paths at all; that is an argument about the permutation group and nothing wider.

## 4. The occupancy ceiling: the coordinate that decides

Under the hard core the symmetric sector's dynamics is no longer closed. The
cells that carry a hard-core configuration into a doubly occupied one are
counted per generator: the symmetric sector leaks at 48 of 64 generators and
closes at 16, and the leaking set is exactly the non-monomial set, with no
mismatches. The antisymmetric sector's leak is measured too, per generator, and
is zero at every one of them.

**And that split is not a discovery about this substrate — it is a one-line
theorem about every unitary.** In the normalised symmetric square the only cell
from a hard-core configuration {*x*, *y*}, *x* ≠ *y*, into a doubly occupied
one {*a*, *a*} is proportional to *U*ₐₓ·*U*ₐᵧ: a single product, in a domain,
so it vanishes exactly when a factor does. The symmetric square therefore leaks
out of the hard core if and only if some row of *U* carries two nonzero entries
— if and only if *U* is not monomial. The wedge has no doubly occupied
configuration to leak into at any dimension, so it never leaks. The instrument
gates this as a theorem rather than citing it: 240 constructed witnesses and
3364 composites out of family, monomial and not, in dimensions three, four and
five and at column supports this pool never reaches, with no mismatch anywhere.
What *this* family contributes is the size of the split — 48 against 16 — and
that size is the parent's monomial classification, inherited, not a
two-excitation measurement.

The consequence is the honest form of the result. Under the hard core the
symmetric shape does not give a stochastic law on the declared configuration
space at 48 of its 64 generators; on the 16 monomial ones it still does. Under
the ceiling of two it does everywhere. Both shapes are laws; which of them is
*this* substrate's law is a question the composition law does not answer and the
occupancy declaration does. The implication runs one way only: a declaration
that *forbids* double occupation selects the antisymmetric shape, while a
declaration that *permits* it selects nothing, since both shapes survive.

And the declaration is not the stage's, which is measured rather than argued.
The anchored record layer's declarations are enumerated: **27 declaration keys
and none of them occupancy-shaped**. Its two integer count registers are *link*
registers — the swept box of division-count vectors, by the stage's own
description — and its one site-indexed register is binary, so neither of its
integers argues either way. The stage is silent on site occupancy. The two
ceilings agree at one excitation, configuration for configuration and generator
by generator as objects, and differ at two — 136 against 120 — which is exactly
why the parent could not have decided this and did not claim to. Whether a
deeper layer can be made to *force* a ceiling is open, and it is the successor
question this unit hands on.

## 5. The defect at two excitations

### The object, and the routes to it

The composition defect is reimplemented from the anchored definition,
Δᴮ(*U*₂, *U*₁) = *B*(*U*₂*U*₁) − *B*(*U*₂)*B*(*U*₁), with the parent's declared
division-event times and the declared leg at the cut, and it is applied to the
*lifted* generators in each sector. The definition is consumed rather than
quoted: the measured object is compared to it, and the other leg order is
exhibited as a different object, which is why the declaration matters.

Three routes compute it, and they are structurally unlike. The definitional one
composes the lifted generators. The second lifts the *composed* generator
instead — the wedge of the composite against the composite of the wedges — so it
never forms the first route's product and never re-reads it; the **whole**
antisymmetric value multiset is recomputed through it and agrees value for
value, which binds functoriality over the entire census rather than over a
sample. The third forms no composite matrix and no product of Born shadows at
all: it sums the interference cross terms directly over ordered pairs of
distinct intermediate configurations. That route is quadratic in the
intermediate support, so it runs on a declared window — the first twelve
generators in the parent's own naming, 144 ordered pairs — and agrees there. The
window is gated to bite: it carries generators of both predicate classes and
pairs of both outcomes, so its agreement is not an agreement about an empty set.

Before anything new is measured, the parent is reproduced. The single-excitation
census returns 588 of 3364 ordered pairs, and its **whole** value multiset —
eight distinct values, cell count for cell count in the parent's own
separation-indexed form — is reproduced by a program sharing no code and no
field representation with the parent's. Every single-excitation defect table
folds without conflict on every column of every pair, which is what makes the
two censuses the same object read twice.

### The census

1764 of 3364 ordered pairs carry a nonzero two-excitation defect, in the
antisymmetric shape and in the symmetric shape alike, against 588 at one
excitation.

| sector | ordered pairs | nonzero |
|---|---|---|
| one excitation | 3364 | 588 |
| ordered, labelled configurations | 3364 | 588 |
| symmetric | 3364 | 1764 |
| antisymmetric | 3364 | 1764 |

**The two-excitation defect has an exact per-pair law: it is nonzero precisely
when both legs are non-monomial.** That is discharged pair by pair in both
sectors — 0 mismatches over 6728 per-pair tests — and the count it implies is
42², the square of the non-monomial population of the verdict-bearing circulant
stratum. The parent's Markovian control therefore survives the lift in the
strong form: a monomial generator annihilates the defect against everything at
two excitations as well as at one, because its lift is again monomial. That the
losses are zero is entailed by the same law rather than measured beside it: a
single-excitation defect forces both legs non-monomial, and the per-pair law
then carries the pair to two. What does *not* survive is the converse gap. At
one excitation most non-monomial pairs carried no defect; at two excitations
none of them fails to.

**So the defect does not compose. It completes.** The two-excitation defect set
strictly contains the single-excitation one: 1176 genuine two-body pairs, and no
pair anywhere loses its defect on the way up. The law is a statement about the
full-support circulant stratum, where every pair of generators shares every
site; section 7 exhibits non-monomial pairs elsewhere in this same arena that
carry no defect at all.

### Where the excess comes from, exactly

On the ordered sector the Born shadow is multiplicative over the tensor product,
*B*(*U* ⊗ *U*) = *B*(*U*) ⊗ *B*(*U*), and the defect obeys an exact derivation
law:

$$
\Delta^{B}(U_2\otimes U_2,\;U_1\otimes U_1)\;=\;\Delta^{B}\otimes X\;+\;Y\otimes\Delta^{B},
\qquad X=B(U_2U_1),\quad Y=B(U_2)B(U_1).
$$

Both sides are built and compared at every pair, with zero failures — and the
consequence is not merely measured but **forced**. Summing the entrywise
identity over a free index gives *X* ⊗ *X* = *Y* ⊗ *Y* only when *X* = *Y*, for
any row-stochastic *X* and *Y* whatever, so the ordered sector's defect set is
the single-excitation set for every unitary family and not only for this one;
and the telescoping identity carries both statements to every excitation number.
**Excitations that carry labels carry no genuine two-body defect whatever**,
even under one and the same generator. The entire excess of 1176 pairs is
created by erasing those labels — by exchange symmetrisation — and by nothing
else in the construction. (The distinguishable *arena* of section 1 is a
different object: there the two excitations are given different generators, and
the exchange symmetry is broken rather than dropped.)

The splitting is not unique, and the paper does not claim it is. Δᴮ ⊗ *Y* +
*X* ⊗ Δᴮ is an equally exact derivation law, and so is every affine mixture of
the two legs; the instrument checks the fibre at every pair alongside the law.
"*X* the coherent and *Y* the restarted composite" is one point on a line of
exact readings.

The mechanism is visible in the entries. In the antisymmetric shape the
amplitude for a pair of configurations is a difference of two products and in
the symmetric shape a sum of the same two, so a two-excitation transition has a
second route through the intermediate cut that a one-excitation transition does
not have. That second route is not a second path through space. It is the
exchange of the two excitations. Where the two legs move on different axes, the
spatial routes do not collide and the one-excitation defect vanishes; the
exchange route is there anyway, and it interferes.

### The values

Every two-excitation defect value is rational in both shapes, although the field
carries irrational elements and the Born projection is never coerced out of it.
There are 28 distinct values in the antisymmetric shape and 30 on the hard-core
block in the symmetric, against the parent's eight at one excitation, and the
denominators are finer: the single-excitation census lives on eighths and the
two-excitation censuses reach 1/128.

The comparison published above is taken on the 120×120 hard-core block that
*both* sectors carry, which is the like-for-like object; the symmetric sector
itself is 136-dimensional and its own census is published beside it. It carries
**39 distinct values in the symmetric sector, of which 9 are never seen on the
block** — and the rationality gate reaches all of them.

## 6. The shapes, discriminated, at two granularities

The two shapes agree on *where* the defect is — both give 1764 — and disagree on
what it is. The comparison has two granularities, and the unit states both.

**Entrywise.** Compared cell by cell, on the shared hard-core block, in the same
row and column ordering and at a common denominator, the two shapes' defects
**differ cell by cell at 1764 of 3364 ordered pairs and agree at 1600**. The
differing set is exactly the set on which the two-excitation defect is nonzero —
exactly the pairs whose two legs are both non-monomial — and the shapes agree
only where both defects vanish. So sections 5 and 6 collapse into one law
rather than two: wherever the two-excitation defect lives, the exchange shape is
readable from it.

The witness is a pair that carries no single-excitation defect at all. On the
declared witness pair the two shapes' two-excitation defects **differ at 576
cells**:

| row | column | symmetric | antisymmetric |
|---|---|---|---|
| {0,4} | {0,1} | 1/32 | -1/32 |
| {0,4} | {0,5} | -1/32 | 1/32 |

**As value multisets.** The coarser, relabelling-invariant comparison — the one
that forgets which cell a value sits in — is confined to a strictly smaller set:
the two shapes' **value multisets differ at 588 of the 3364 ordered pairs**, and
that set is exactly the single-excitation defect set, element for element, gated
as a set equality. On the witness pair above the two multisets are equal, which
is precisely why the coarser comparison does not fire there.

That is the unit's title made a measurement, and the two granularities say
different things. The exchange shape is not a convention here and it is not
free: it has Born-level consequences at every pair where the two-excitation
defect lives, including all 1176 of the genuine two-body pairs, where the
substrate's
one-excitation composition does not interfere at all. What is confined to the
ordered pairs at which the substrate is already non-Markovian across the cut is
the *relabelling-invariant* signature — the coarser reading, which cannot see a
difference that moves a value from one cell to another.

The coarser reading survives a second scope as well as the whole census. On a
declared stride window — every thirteenth ordered pair of the census's own
enumeration — the single-excitation set, the multiset-differing set and the
contact handle's moved set coincide again, on **43 of the 259 pairs of the
declared stride window**, so the identity is not an artifact of reading the
census whole.

The spectra say the same thing in the other basis, and section 8 gives them.

## 7. The support-overlap law, generalised and lifted

R5's terminal gauge rung proved a support-overlap law at link grain — no defect
when two operators' site supports meet in at most one site — and ran its one
declared two-excitation extension as a sample of 18 rows, six named coins
against three relations, disclosed as a sample and not a sweep. The pin asks for
the general census at a declared window. The window here is every 2-site support
on the lattice, not only the adjacent ones the link grain could reach,
exhaustive in the geometry, against each of three declared coin pairs — one of
them a coin against itself — at one excitation and at two, in both shapes. The
geometry is exhaustive and the coin axis is a declared sample of the 512
interfering coins, each pair gated separately.

The local-operator alphabet is rebuilt and matches R5's anchored counts: 640
coins, 512 of them interfering, on 32 links, and 120 two-site supports in all.

| overlap | rows | one excitation | antisymmetric | symmetric |
|---|---|---|---|---|
| 0 | 32760 | 0 | 0 | 0 |
| 1 | 10080 | 0 | 0 | 0 |
| 2 | 360 | 360 | 360 | 360 |

**R5's law survives the lift, and survives the generalisation.** There is no
defect at 42840 of the 42840 rows at overlap at most one, at either excitation
number and in either shape. The zero is a measurement and not a blindness: the
same window carries a defect at every one of the 360 rows at overlap two, at
all three levels. And it is not one coin's accident: the gate binds each declared coin
pair separately, and each of the three gives that table on its own.

**And the shape discrimination is taken here too, which decides the scope of
section 6.** Every overlap-2 row is a row on which the substrate demonstrably
interferes at one excitation. Compared at both granularities, the two shapes
**differ at 240 of the 360 rows at overlap two** — at every row of each declared
pair of *distinct* coins, and at no row of the coin composed with itself. So
interference at one excitation does not by itself imply that the shapes can be
told apart: this arena carries 120 interfering rows on which they agree. The
coextension of section 6 — three probes, one set — **is a statement about the
circulant stratum**, and this unit scopes it there rather than claiming the
arena.

Read together with section 5 this closes a question the two results might
otherwise have seemed to open against each other. The circulant generators of
the main census are supported on the whole lattice, so every circulant pair
overlaps in every site; the exchange route exists there and fires. Two-site
operators meeting in at most one site have no shared configuration for the
exchange route to run through, and it does not fire. **Exchange does not widen
the region in which a defect can live; it fills that region in.** R5's terminal
finding that the fibre-2 choice is not load-bearing was a statement at link
grain about whether a defect exists at all, and it is untouched: what varies
with the fibre here is *which* defect, not whether there is one.

The 2-site window is the complete interfering local window on this stage rather
than a slice of a larger one, and that is measured: over the declared alphabet
no three-site local unitary has full support. Every full-support unit row is
enumerated — 1536 of them — and none completes to a unitary. The reason is the
sweep itself: over this alphabet the only full-support unit row has squared
moduli (1/2, 1/4, 1/4), and no two further alphabet rows are orthogonal to it
and to each other. Three-site and larger supports are therefore not censused,
and the reason is a property of the alphabet rather than a budget.

## 8. Motion at two excitations

**The eigenphases add, exactly.** For a circulant family with symbol λ, the
wedge and the symmetric square of a pair of characters is an eigenvector of the
lifted generator with eigenvalue the product of the two symbols, so the exact
eigenphase in Z/8 is the sum. This is verified as an exact matrix identity, cell
by cell, at 6960 antisymmetric and at 7888 symmetric cells, with zero failures. It
is forced — the sectors are functors — and is registered as a disclosure with
the measurement that carries content named beside it.

R4b's single-excitation reading is reproduced independently on the way past: the
same speed spectrum {0, 1, 2}, the same 1856 cells, and the same 320
antipodal-tie cells in the same 19 families, under R4b's own convention,
inherited as declared. No transport number is taken.

**The spectra separate the shapes.** The symmetric two-excitation spectrum is
the antisymmetric one together with the sixteen doubled-momentum cells the wedge
cannot hold, at every one of the 58 families. Those are the cells where a
momentum is paired with itself, and the wedge of a character with itself is
zero.

There are as many of them as there are configurations the hard core forbids —
sixteen either way, because both are the dimension by which the symmetric sector
exceeds the antisymmetric one. They are the same *number* in two bases and not
the same subspace, and the paper claims only the number: the doubly occupied
site states and the doubled-momentum states are different sixteen-dimensional
complements of the wedge inside the symmetric square. The shapes are therefore
distinguishable in the spectrum as well as in the defect, and by a gap of the
same size in both readings.

**The velocities do not add.** Under the inherited convention the group velocity
is a lift of the phase difference, and the lift of a sum is not the sum of the
lifts. Advancing both momenta together, the composition fails at 7168 of the 29696
cells, and the failure is confined to a single mechanism — but the mechanism is
a statement about the *raw* advances and not about their lifts, because the lift
sends both 0 and 4 to 0 and would hide the distinction. Measured, the failing
raw advance pairs are exactly (2, 2) and (6, 6): a phase advance of exactly
π/2 per momentum step in both legs, whose sum reaches the antipodal tie, which
the torus cannot orient. Two equal nonzero advances are not enough on their own:
**4096 cells carry two equal nonzero advances and do not fail**, being the cells
where both advances are the tie itself and their sum is zero.

This is an **aliasing** signature and the paper declines to dress it as an
interaction. It is a property of the declared reading of the velocity on a
finite dual torus, it lives in the convention R4b selected and this unit
inherited without re-selecting, and it would be there for two non-interacting
excitations of any kind. What it does show is that additivity of the *phase*
and additivity of the *velocity* are different statements on a lattice, and only
the first is exact.

**And two excitations move no faster than one.** The two-excitation speed
spectrum is the single-excitation speed spectrum. That ceiling is *forced*: the
declared speed is the branch-free circle distance on the dual torus, halved,
whose range is {0, 1, 2} for every argument at this lattice size, so no family
and no excitation number could widen it. What is measured is that all three
values are attained at two excitations as well as at one.

## 9. An interaction, and who can see it

One more lift is declared and run: the free lift followed by a phase on the
doubly occupied configurations. It is diagonal in the configuration basis and
exchange invariant, so it is unitary and preserves both sectors, and it is the
cheapest contact-shaped handle this arena admits.

It moves the symmetric sector's operator at 58 of 58 families and the
antisymmetric sector's at none, because the wedge has no doubly occupied
configuration for it to act on. At the level of the composition defect it
**moves it at 588 of the 3364 ordered pairs and the antisymmetric one at 0**.

The self-test is two-way and its negative direction fires where it can, so the
zero is a measurement of the shape and not a vacuity *of the handle*; the
antisymmetric zero itself is forced, and generalises to every excitation number,
since the wedge has no repeated site at any *n*. **A contact interaction is
invisible to the antisymmetric shape and visible to the symmetric one**, on this
arena, at the declared handle — which is the sixteen-dimensional gap between the
two sectors met for a third time, here in the site basis, where it is the doubly
occupied configurations themselves.

**And the pairs at which it is visible are, again, that set.** The ordered pairs
whose symmetric-sector defect the handle moves are exactly the ordered pairs
carrying a single-excitation defect — the same 588, element for element, gated
as a set equality and not as a count, and the same set on which the two shapes'
value multisets are discriminated.

The mechanism is one line. The handle is a phase on the doubly occupied
configurations; a phase is invisible to a single Born shadow, since it has unit
modulus, and becomes visible only across the cut, where a doubly occupied
intermediate configuration can interfere with one that is not. That is the same
condition that makes the one-excitation composition interfere in the first
place. So the unit closes on one statement rather than three: on the
verdict-bearing circulant stratum, everything that can see the doubly occupied
channel — the choice of exchange shape read invariantly, and a contact
interaction — sees it exactly where the substrate's one-excitation composition
already fails to restart at the cut, and is blind everywhere else. Section 7
measures the same question at the local grain and answers it differently, which
is what fixes the scope.

## 10. What this decides, and what it does not

**Decided, at the declared scope.**

- The substrate's composition law admits both exchange shapes and selects
  neither: the exchange operator commutes with the free lift at every generator,
  both sectors are closed, unitary and stochastic at all of them, and the
  ordered sector decomposes into those two sectors and nothing else, with no
  third place to stand at two excitations. All of that is forced by the free lift rather than found.
- The coordinate that selects is the occupancy ceiling, and the stage anchors
  none. Under the hard core the symmetric shape fails to close at 48 of its 64
  generators, exactly the non-monomial ones — a theorem about every unitary,
  gated on **240 constructed witnesses and 3364 out-of-family composites** — and
  the antisymmetric shape does not leak at all. The two ceilings have the same
  one-excitation restriction as an object, so no single-excitation measurement
  could have decided this. Exclusion can select a shape; permission cannot.
- The defect does not compose; it completes. 1764 of the 3364 ordered pairs
  carry one against 588 at one excitation, with 1176 of them genuinely
  two-body and no losses, and the nonzero set is exactly the
  pairs whose legs are both non-monomial — on the full-support circulant
  stratum.
- On the ordered sector the defect composes by an exact derivation law and there
  is no genuine two-body defect at all: the excess is carried entirely by
  exchange symmetrisation. That is a theorem about every unitary family and at
  every excitation number, not a census of this one.
- The two shapes are discriminated by the defect at two granularities: cell by
  cell at the whole two-excitation defect set, and as value multisets at exactly
  the single-excitation defect set.
- R5's support-overlap law survives the lift and the generalisation to every
  2-site support: no defect at **42840 of 42840 rows at overlap at most one**,
  and a defect at **360 of 360 rows at overlap two**, at each declared coin pair
  separately — and at the local grain the two shapes are discriminated on some
  of those rows and not others, which scopes section 6 to the circulant stratum.
- The eigenphases add exactly at **6960 antisymmetric and 7888 symmetric
  cells**; the velocities do not, failing at **7168 of 29696 cells** and only at
  the antipodal tie; the speed ceiling does not widen, and is forced not to.
- A declared contact interaction is invisible to the antisymmetric shape, and
  the pairs at which it is visible to the symmetric shape are again exactly the
  single-excitation defect set.

**The choices, and which of them decide.**

| item | fibre | class | verdict-determining |
|---|---|---|---|
| the occupancy ceiling | 2 | GENUINELY-FREE | YES |
| the lift | 3 | GENUINELY-FREE | YES |
| the lattice: the verdict arena against the one-site control | 2 | DECLARED-CONTROL | no |
| the division-event times and the leg at the cut | 1 | INHERITED-AS-DECLARED | no |
| the velocity convention | 2 | INHERITED-AS-DECLARED | no |
| the third route's window | 1 | GENUINELY-FREE | no |
| the local window's coin pairs | 3 | GENUINELY-FREE | no |
| the contact phase | 8 | GENUINELY-FREE | no |
| the stride window for the coarser reading of the triple identity | 1 | GENUINELY-FREE | no |
| d, L, the alphabet, the stencil, the axes, the connective, the symmetrised basis | 1 | FORCED | no |

Two items are verdict-determining, and the unit's whole thesis is that one of
them is the story.

**Not decided, and not attempted.**

- The occupancy ceiling is DECLARED. This unit measures what each declaration
  costs and does not claim to have found the substrate's own. Whether the record
  layer can be made to force one is open, and it is the successor question this
  unit hands on; it is the first obligation of anyone who wants a statistics
  rather than a pair of them.
- The discrimination is between two DESCRIPTIONS, and it is not a
  determination. What is shown is that the two shapes make different Born-level
  predictions; what is *not* shown is which of them this substrate makes,
  because that is what the occupancy ceiling decides and the ceiling is
  declared. A statistics that is measurable is not thereby measured.
- Nothing here is about *n* excitations at the level of sectors. The two-irrep
  argument that forbids a third shape is an argument about two, and the
  general-*n* sector — where parastatistics-shaped representations genuinely
  exist — is not built. The two theorems above do run at every *n*; the sector
  count does not.
- Nothing here bears on braid statistics. Exchange is implemented by a single
  finite operator whose square is the identity, on a discrete lattice; the
  configuration space of indistinguishable points, whose topology is what admits
  braid-group representations in two dimensions, is never built. The two-irrep
  argument constrains representations of the permutation group and no more —
  and this arena is two-dimensional, so the omission is not idle.
- No particle is named. *Fermionic-shape* and *bosonic-shape* are shape words
  for the antisymmetric and symmetric sectors, and every claim above is a claim
  about a sector of a finite lattice model.
- Indivisibility remains DECLARED, by the parent's division-event times, and is
  never measured. A nonzero defect does not imply stochastic indivisibility, and
  no divisor search is run.
- No transport number is inherited from R4b, and none is produced. The velocity
  convention is inherited as declared and is not re-selected; the residual fibre
  R4b measured inert is not re-examined.
- No configuration measure, no action, no coupling and no dynamics over
  configurations. The contact handle is a declared operator, not a theory.
- Three-site and larger local supports are not censused. The reason is measured
  — the alphabet admits no full-support three-site unitary — but a wider
  alphabet would reopen it.
- The distinguishable arena is exhibited, not developed: it says the exchange
  symmetry can be broken by the law, not what a broken-symmetry sector would do.
- No continuum or infinite-volume limit is taken, and the lattice has sixteen
  sites throughout.

## 11. The instrument

The instrument rebuilds the arena from the definitions, gates the rebuild
against the parents object by object, and measures. Gates that discharge a
per-object obligation bind objects and not cardinalities: the exchange census
binds every generator's own predicate, the hard-core census binds every
generator's own leak, the two-excitation predicate is discharged pair by pair in
both sectors, the shape-discrimination gates bind set equalities rather than
counts, and the two ceilings are compared as objects — configuration set,
transition matrix and Born shadow — rather than as a cardinality compared with
itself.

Gates whose clause is analytically forced are registered as disclosures with
their forcing named and with the gate that carries the measured content in their
place. Six are: the exchange commutation, the antisymmetric sector's closure,
the hard-core split, the ordered-sector derivation law, the additivity of the
eigenphases, and the speed ceiling. Two of those are theorems this unit proves
and gates rather than facts it found, and the paper says which measured content
stands beside each of them.

Every quantum-layer claim carries a description stamp naming the sector, the
lift, the occupancy ceiling, the granularity of the comparison and the stratum
it was measured on. Every fraction in this paper is a count over a declared
enumeration and is not a probability; no measure on generator pairs,
configurations or rows is declared. The choice inventory is published as data
with its fibres and its verdict-determining flags.

The head is derived from measured predicates, rendered from the receipt, and
compared for string equality against an independent reconstruction that reads
only the serialized receipt and derives the head by its own copy of the head
law. Every object the unit vouches for — the measurements, the theorems, the
anchors, the schema, the provenance and the paper's own claims and tables — is
digested on the line after its own gate passes, and every seal's provenance
column is checked against the run's ledger: the gate it names must exist, must
have been evaluated, and must have been evaluated before the digest was taken.
The artifacts are written from the sealed payload, both are verified against the
gate-time seal before either is promoted to its final path, and integrity is
disk-against-seal rather than re-derivation from disk.

The paper is verified inside the run. Every numeral in it — prose, inline spans,
tables and the fenced verdict block alike — is licensed by a measured receipt
value or by a declared structural numeral, and no numeral is licensed by a
digest string. Every claim about a measured quantity renders from a receipt key
and must occur exactly once, an occurrence count rather than a containment test.
Every row of every table above renders from this run's own measurements and must
occur exactly once. The fenced blocks are compared to the derived verdict as a
multiset, so a second fence cannot hide behind a clean twin. The load-bearing
sentences carry polarity, so an inverted headline or an inverted wall dies. And
the walls are instruments: the paper is scanned word by word against a declared
banned list, with the shape words surviving only as the compounds the pin
licenses. The verification is non-destructive, and that too is gated: the state
is digested before and after, and a perturbation that is not restored is caught.

The run shells out to nothing and consults no version-control state: every input
is read by path and by hash, so the instrument reproduces off-tree and on a
machine with no git, and an added subprocess or socket import dies at a gate.
The payload is a pure function of the measurements — byte identical across
serializations and free of this machine's absolute paths — so the artifact
reproduces byte for byte wherever the pinned inputs are.

The heavy censuses are memoised so that the mutant sweep is a sequence of
independent runs rather than one long one, and the memo is proved clean: every
cache hands back a defensive copy, and every cache family is fingerprinted over
its whole contents at creation and re-checked on every build, so no injection,
this run's or an earlier run's, can reach the next run through it.
