# Can merging be a process?

**SEC-2 / paper-40.** Pin `v14/note-sec2-pin.md` (FROZEN, sha256-12
`bfe5c66be9ec`, ledger #332). Code `v14/code/sec2_exact.py`; artifacts
`v14/code/sec2_output.txt`, `v14/code/sec2_receipt.json`.

**Verdict**, in four segments.

```
SEC2-SEAM-DECLARATION-IRREDUCIBLE-[49 SEAM TYPES OVER 132273 SHARED SITES; THE COMPLETION SPACE IS 4-PARAMETER AT EVERY ONE, RANK 6 ON 10 BY THE CHART ALONE; AT THE ALL-SIMPLE SEAM 31 COMPLETIONS ASSIGN ADMISSIBLE COUNTS TO EVERY CROSS DIRECTION AND ALL 31 ARE POSITIVE DEFINITE] -- POSITIVITY SELECTS NOTHING; THE CONVENTION-FREE PRICE IS CONSTANT ON THE WHOLE SPACE AND THE ONE-SIDED READING'S MINIMISER MOVES WITH THE CONVENTION; REFINEMENT STABILITY IS EMPTY AT THIS RECORD BY THE CEILING LAW (MIN COUNT 1, CEILING 0) AND, GRANTED AS A HYPOTHETICAL, IS EMPTY AT 48 OF 49 SEAM TYPES AND SELECTS THE DIRECT SUM AT THE 49TH -- THE ONE PRINCIPLE THAT DOES SELECT, MAXIMUM DETERMINANT, IS NAMED AND NOT LICENSED
```

```
SEC2-GLUING-EVENT-LAWFUL-AT-THE-MATCHED-CROSS-LINK-EXTENSION-[THE WINDOW: TARGET x READING x COUNT LEG, 30 CELLS, CARRIER AND LINK INDIVIDUATION HELD AT THE DELIVERED VALUES; 455 THREE-ACTOR GROUPS IN 9 ORBITS, 288 OF THEM SEAM-SPANNING AND EVERY ONE DEAD AT THE DELIVERED TARGET] -- LAWFUL AT 216 OF 288 ONCE THE TARGET DECLARES THE CROSS LINKS THE EVENT REALISES, BOTH DRIVEN SPECIFICATIONS AMONG THEM, AND MOTIVATED AT 0 OF 216: THE PRICE IS THE WELD ITSELF, FREE ITEMS 0 -> 3 AT THE SHARED-SEEDED CROSSING AND 0 -> 2 AT THE B-SEEDED ONE, WHILE THE CROSSING TAKEN ALONE COSTS NOTHING AND NO THREE-ACTOR GROUP CAN DELIVER IT ALONE
```

```
SEC2-COMPOSITE-PRICE-SPLITS-[FIVE CURRENCIES ON ALL 45010 COMPOSITES AGAINST THE LONE SECTOR, ZERO VIOLATIONS: RECORD 54 = 27 + 27 IGNORES COMPOSITION; CARRIERS 18 - k AND LINKS 54 - d FAVOUR IT; THE GEOMETRY'S BUDGET 54 + 2d AND THE DECLARATION PRICE 4k PENALIZE IT] -- AND THE EXCESS IS SEAM-CONFINED: EVERY UNSHARED SITE'S FORM IS DETERMINED EXACTLY AS IN A LONE SECTOR AND THE WHOLE SURCHARGE SITS ON THE SHARED SITES, FOUR NUMBERS EACH
```

```
SEC2-THE-EXTENDED-DICTIONARY-IS-BLIND-AT-ONE-CROSSING-AND-SIGHTED-AT-TWO-[36 PLACEMENTS IN 1 ARENA AT ONE CROSSING AND 36 OF 36 ADMITTED BY THE DETECTOR; 630 PLACEMENTS IN 5 ARENAS AT TWO AND 108 OF 630 ADMITTED; 7140 IN 15 AT THREE] -- SO THE PLACEMENT OF A SINGLE CROSS LINK IS A GAUGE AND NOT A DATUM, AND THE RECORD-FITTED OBJECTION DOES NOT BITE AT ONE CROSSING BECAUSE EVERY PLACEMENT GIVES THE SAME ARENA
```

Between delivery and adjudication every headline reading here is a
**candidate reading**.

---

## 1. The question

SEC glued two driven sectors and found that geography composes: the union
carries a dictionary at every one of its combinatorial types. It also found
two things it could not finish. The seam's own form was six equations short
of determined — the direct sum a declaration, not a measurement — and the
committed grammar turned out to ADMIT division events spanning the two
sectors, which then killed the dictionary at structure. So gluing was left as
a boundary condition: something a modeller does between records, never
something the process does inside one.

The pin asks whether that can be reversed. Its three measurements are asked
here in its own words.

> the 4-parameter completion space at each seam

is measured over its whole admissible lattice, not sampled; the extension
window is enumerated and every relaxation is priced; and

> evaluated on composites vs lone sectors — does the price favor,
> penalize, or ignore composition?

is instantiated in five currencies at once, because a price that is
conserved in one and not in another is the only honest answer to a question
about composition.

Nothing about the record, the grammar, the actor set or the readout law is
touched. The one thing this unit adds to the delivered picture is the
question *what would the target have to carry* — and it answers it by
measurement, at a price the paper states rather than absorbs.

The SEC adjudication is carried, not re-litigated. Its ruling is that the
union's geometry changes only on links both sectors jointly own; the finding
is SEAM-CONFINED compositionality, and every sentence below respects it.
Its arena count is re-measured here rather than inherited.

## 2. The arena, declared as data (RUNBOOK section 15)

| row | value |
|---|---|
| boundary | the 54 (chart, site, link) cells of two copies of AG(2, 3) with links (1, 0), (0, 1) and (1, 1), plus the declared cross links of each extension |
| family | the 45,010 gluings in 16 combinatorial types on 12 union arenas; the 455 three-actor groups of the k = 3 aligned union in 9 orbits |
| law | the co-division relation of the saturating arrangement, I7's readout (a count is the squared length of its link direction), HA's admissibility, paper-04's ceiling law |
| state | the completion of the seam's four undetermined entries |
| arena axes | the five declared window axes: target, reading, count leg, and (held fixed here) carrier and link individuation |
| provenance | 5 sources read at pinned shas; the 4 #301 SEC objects declared at commit 88e4a83 and bound by reproduction |

### 2.1 What is read, and what is declared

Five sources are read at run time and authenticated, and the read set
recorded at the I/O layer is gated to be exactly this set.

| id | path | sha256-12 |
|---|---|---|
| A-PIN | v14/note-sec2-pin.md | bfe5c66be9ec |
| A-ADJ | v14/note-sec-adjudication.md | 7a82ffe7168a |
| A-P19 | v14/paper-19-r3-weld.md | 50bb81e67942 |
| A-SMU | v14/paper-27-smu.md | 6df0db523d32 |
| A-LOR | v14/paper-30-lor.md | 0a08203b7e99 |

The four #301 SEC objects are **not read**. Their worktree copies are under
repair and the pin forbids reading them; a committed object cannot be read
at all in a run that must reproduce byte for byte off-tree and with no
version control present. So every value this unit inherits from SEC is
carried as a DECLARED row and bound by REPRODUCTION: this unit recomputes it
from its own arena, and the run dies on any mismatch. Twenty-two such values
are declared and all twenty-two reproduce.

| DECLARED, NOT READ | v14/paper-32-sec.md | cfe0825d67b2 |
|---|---|---|
| DECLARED, NOT READ | v14/code/sec_exact.py | 6481a8706503 |
| DECLARED, NOT READ | v14/code/sec_output.txt | e80d2f08a257 |
| DECLARED, NOT READ | v14/code/sec_receipt.json | fdf66d990dbf |

### 2.2 The extension window, named

The window is the axes along which the delivered reading legs may be
relaxed, and it is fixed before anything is measured.

| axis | members | the delivered value |
|---|---|---|
| TARGET | NONE, ONE-AT-ONE-SEAM, ONE-AT-EVERY-SEAM, SEAM-MAP, FULL-CROSS | NONE |
| READING | EMBEDDING, QUOTIENT, LAX | EMBEDDING and QUOTIENT |
| COUNT LEG | POSITIVE, NON-NEGATIVE | POSITIVE |
| CARRIER | BARE | BARE, held fixed |
| LINK INDIVIDUATION | SIMPLE | SIMPLE, held fixed |

Outside the window, and named as outside it: the record itself, the
committed grammar, the actor set, the arrangement, and the readout law. A
unit that moved any of those would not be extending this dictionary; it
would be writing another one.

## 3. Measurement one — seam selection

### 3.1 The seam census

A seam is a shared site, and its type is the pair of count vectors its two
charts carry on their three declared links. Every shared site of every one
of the 45,010 gluings is classified: **49 seam types over 132,273 shared
sites**. Seven of the eight possible count vectors occur on each side, and
the one that never occurs is (2, 2, 2) — a shared site has at most two other
shared actors, so its three links cannot all be doubled.

At every one of the 49 the six declared links give rank 6 on the ten entries
of the symmetric square of the direct-sum chart, so the kernel is 4. That is
taken on the coefficient matrix alone, with no right-hand side in it, so it
is a property of the chart rather than of any record: the completion space
is 4-parameter at every seam type, whatever the counts.

### 3.2 The completion lattice

The corpus's own readout makes the completion space discrete. A completion
assigns a count to every direction of the chart, including the cross
directions joining an A-neighbour of the shared site to a B-neighbour of it;
those counts must be positive integers. That is I7's readout and HA's
admissibility carried from the declared links to every direction of the
chart, and carrying them there is a DECLARED reading, named here as one. The
enumeration box is then derived from the cross counts themselves — the
(i, j) cross count forces the cross entry into an interval of its own — and
that the box is not binding is measured rather than asserted: the census is
run a second time with the box widened, and the two return the same set.

**The verdict does not rest on the reading.** Drop it, and the completion
family is the whole 4-parameter rational affine space: two completions at a
cross entry no half-integer lattice contains are exhibited, both reproducing
all six declared counts and both positive definite. On an infinite family no
criterion selects either, so the finite reading is the stronger one — which
is why it is the one published.

| the A side | the B side | shared sites | admissible completions | positive definite | parity-stable |
|---|---|---|---|---|---|
| (1, 1, 1) | (1, 1, 1) | 42606 | 31 | 31 | 1 |
| (1, 1, 1) | (1, 1, 2) | 7533 | 49 | 49 | 0 |
| (1, 1, 1) | (1, 2, 1) | 7533 | 49 | 49 | 0 |
| (1, 1, 1) | (1, 2, 2) | 486 | 103 | 103 | 0 |
| (1, 1, 1) | (2, 1, 1) | 7533 | 49 | 49 | 0 |
| (1, 1, 1) | (2, 1, 2) | 486 | 103 | 103 | 0 |
| (1, 1, 1) | (2, 2, 1) | 486 | 103 | 103 | 0 |
| (1, 1, 2) | (1, 1, 1) | 7533 | 49 | 49 | 0 |
| (1, 1, 2) | (1, 1, 2) | 3483 | 79 | 73 | 0 |
| (1, 1, 2) | (1, 2, 1) | 3483 | 79 | 73 | 0 |
| (1, 1, 2) | (1, 2, 2) | 486 | 155 | 141 | 0 |
| (1, 1, 2) | (2, 1, 1) | 3483 | 79 | 73 | 0 |
| (1, 1, 2) | (2, 1, 2) | 486 | 155 | 141 | 0 |
| (1, 1, 2) | (2, 2, 1) | 486 | 155 | 141 | 0 |
| (1, 2, 1) | (1, 1, 1) | 7533 | 49 | 49 | 0 |
| (1, 2, 1) | (1, 1, 2) | 3483 | 79 | 73 | 0 |
| (1, 2, 1) | (1, 2, 1) | 3483 | 79 | 73 | 0 |
| (1, 2, 1) | (1, 2, 2) | 486 | 155 | 141 | 0 |
| (1, 2, 1) | (2, 1, 1) | 3483 | 79 | 73 | 0 |
| (1, 2, 1) | (2, 1, 2) | 486 | 155 | 141 | 0 |
| (1, 2, 1) | (2, 2, 1) | 486 | 155 | 141 | 0 |
| (1, 2, 2) | (1, 1, 1) | 486 | 103 | 103 | 0 |
| (1, 2, 2) | (1, 1, 2) | 486 | 155 | 141 | 0 |
| (1, 2, 2) | (1, 2, 1) | 486 | 155 | 141 | 0 |
| (1, 2, 2) | (1, 2, 2) | 162 | 275 | 267 | 0 |
| (1, 2, 2) | (2, 1, 1) | 486 | 155 | 141 | 0 |
| (1, 2, 2) | (2, 1, 2) | 162 | 275 | 267 | 0 |
| (1, 2, 2) | (2, 2, 1) | 162 | 275 | 267 | 0 |
| (2, 1, 1) | (1, 1, 1) | 7533 | 49 | 49 | 0 |
| (2, 1, 1) | (1, 1, 2) | 3483 | 79 | 73 | 0 |
| (2, 1, 1) | (1, 2, 1) | 3483 | 79 | 73 | 0 |
| (2, 1, 1) | (1, 2, 2) | 486 | 155 | 141 | 0 |
| (2, 1, 1) | (2, 1, 1) | 3483 | 79 | 73 | 0 |
| (2, 1, 1) | (2, 1, 2) | 486 | 155 | 141 | 0 |
| (2, 1, 1) | (2, 2, 1) | 486 | 155 | 141 | 0 |
| (2, 1, 2) | (1, 1, 1) | 486 | 103 | 103 | 0 |
| (2, 1, 2) | (1, 1, 2) | 486 | 155 | 141 | 0 |
| (2, 1, 2) | (1, 2, 1) | 486 | 155 | 141 | 0 |
| (2, 1, 2) | (1, 2, 2) | 162 | 275 | 267 | 0 |
| (2, 1, 2) | (2, 1, 1) | 486 | 155 | 141 | 0 |
| (2, 1, 2) | (2, 1, 2) | 162 | 275 | 267 | 0 |
| (2, 1, 2) | (2, 2, 1) | 162 | 275 | 267 | 0 |
| (2, 2, 1) | (1, 1, 1) | 486 | 103 | 103 | 0 |
| (2, 2, 1) | (1, 1, 2) | 486 | 155 | 141 | 0 |
| (2, 2, 1) | (1, 2, 1) | 486 | 155 | 141 | 0 |
| (2, 2, 1) | (1, 2, 2) | 162 | 275 | 267 | 0 |
| (2, 2, 1) | (2, 1, 1) | 486 | 155 | 141 | 0 |
| (2, 2, 1) | (2, 1, 2) | 162 | 275 | 267 | 0 |
| (2, 2, 1) | (2, 2, 1) | 162 | 275 | 267 | 0 |

Read the first row first, because it carries 42,606 of the 132,273 shared
sites. At the all-simple seam there are 31 completions the record's own
readout admits, and **all 31 are positive definite**.

### 3.3 The three criteria, measured

**Positivity.** It is the criterion SEC's own segment leaned on, and here it
selects nothing: at every one of the 49 seam types the admissible lattice
carries at least 31 positive-definite completions. At 13 of the 49 — every
seam type with an all-simple side, where the admissible count and the
positive-definite count coincide — positivity is not merely unselective, it
is implied by admissibility and therefore carries no information at all.
**positivity selects no completion**.

**Price minimisation.** The price this corpus charges for geometry is
counts: a link costs the division events that realise it. So the price of a
completion is the total count on the cross directions it licenses. Summed
over both signs of every cross direction — the only
convention-free reading, since a chart's neighbour x + a and its neighbour
x - a are both declared — the budget is **constant on the whole completion
space**, at every seam type. One may instead sum over the forward directions
only; then the minimum is attained, but at eight completions rather than
one, and reversing the sign convention moves the minimising set to a
disjoint set of eight. A criterion whose argument moves with a convention
does not select.

**Refinement stability.** LOR carries paper-04's ceiling law in its own
bytes:

> No record admits more than $\lfloor\log_2(\min n_\ell)\rfloor$ consecutive
> steps.

The union's minimum count is 1 at every gluing in the family, so the ceiling
is 0 and the refinement laws have nothing to act on. That is the honest
answer: the criterion is empty at this record. Granted anyway as a
hypothetical — would a completion's cross counts survive one dyadic halving
— it is empty at 48 of the 49 seam types, because the halving conditions are
over-determined the moment the two sides carry different parities, and it
selects exactly one completion, the direct sum, at the 49th, which is the
all-simple seam.

### 3.4 The verdict, and the principle that would break it

So **the freedom is irreducible** relative to the declared laws:
`SEAM-DECLARATION-IRREDUCIBLE`. It is not irreducible in principle, and
this paper says which principle would break it rather than leaving the
result looking stronger than it is. One extremal principle does select,
uniquely, at all 49 seam types: maximising the determinant of the
form returns the direct sum and nothing else. That is Fischer's inequality
doing the work, and nothing in this corpus declares it. It is named here and
not licensed; a unit that adopted it would be making a declaration, not
reporting a measurement.

### 3.5 Two sharpenings of the delivered picture

SEC exhibited an exact rational completion, reproducing all six measured
counts, that is negative on an exhibited vector. Rebuilt here from its
declared entries, it returns all six counts and its own value on its own
vector. It is then placed: it assigns count 0 to four of the chart's cross
directions, so **it lies outside the admissible lattice**. The affine family
does contain indefinite points, exactly as delivered; the admissible lattice
at the all-simple seam does not.

And the crossing the grammar actually drives cuts the space. Its co-division
pair joins the shared site's third A-neighbour to its third B-neighbour, so
it carries one more equation: the kernel falls from 4 to 3, the admissible
lattice falls from 31 completions to 8, every one of the 8 is still positive
definite, and the direct sum is **not** among them. The completion SEC
declared is the one completion the measured crossing forbids.

## 4. Measurement two — the dictionary extension

### 4.1 What a division event can do to a union

Paper-19's legs are read out of its own bytes: site from the actor, link
from the co-division actor pair, count from the division events on that
pair. A conflict group at this arena has three actors, so a division event
deposits exactly three incidences. Every three-actor group of the k = 3
aligned union is censused — 455 of them — and reduced by the union's own
automorphism group to 9 orbits.

| orbit size | charts | crossings | within-sector new pairs | doublings | at the delivered target | at the matched extension |
|---|---|---|---|---|---|---|
| 108 | (('A', 2), ('B', 1)) | 2 | 0 | 1 | STRUCT-DEAD | ALIVE |
| 72 | (('A', 2), ('B', 1)) | 2 | 1 | 0 | STRUCT-DEAD | STRUCT-DEAD |
| 108 | (('A', 1), ('B', 1), ('S', 1)) | 1 | 0 | 2 | STRUCT-DEAD | ALIVE |
| 54 | (('A', 2), ('S', 1)) | 0 | 0 | 3 | ALIVE | NOT-APPLICABLE |
| 36 | (('A', 1), ('S', 2)) | 0 | 1 | 2 | STRUCT-DEAD | NOT-APPLICABLE |
| 36 | (('A', 2), ('S', 1)) | 0 | 1 | 2 | STRUCT-DEAD | NOT-APPLICABLE |
| 36 | (('A', 3),) | 0 | 1 | 2 | STRUCT-DEAD | NOT-APPLICABLE |
| 4 | (('A', 3),) | 0 | 3 | 0 | STRUCT-DEAD | NOT-APPLICABLE |
| 1 | (('S', 3),) | 0 | 3 | 0 | STRUCT-DEAD | NOT-APPLICABLE |

The charts column names the representative's own composition; the orbit
contains its mirror as well, so the column is a property of the
representative and the orbit size is the property of the orbit.

Two readings come straight off it. First, **every seam-spanning group is dead
at the delivered target** — 288 of them, exhaustively, where SEC had three
chosen specifications. Second, the detector is not a machine that kills
whatever it is handed: 54 groups leave the dictionary ALIVE at the delivered
target, and they are exactly the groups that cross nothing and open no new
within-sector pair. The control fires in both directions inside one census.

### 4.2 The window, cell by cell

| target | declared links | declaration fiber | reading | count leg | the baseline record | with the driven crossing |
|---|---|---|---|---|---|---|
| NONE | 0 | 1 | EMBEDDING | POSITIVE | ALIVE | STRUCT-DEAD |
| NONE | 0 | 1 | EMBEDDING | NON-NEGATIVE | ALIVE | STRUCT-DEAD |
| NONE | 0 | 1 | QUOTIENT | POSITIVE | ALIVE | STRUCT-DEAD |
| NONE | 0 | 1 | QUOTIENT | NON-NEGATIVE | ALIVE | STRUCT-DEAD |
| NONE | 0 | 1 | LAX | POSITIVE | ALIVE | ALIVE |
| NONE | 0 | 1 | LAX | NON-NEGATIVE | ALIVE | ALIVE |
| ONE-AT-ONE-SEAM | 1 | 27 | EMBEDDING | POSITIVE | STRUCT-DEAD | ALIVE |
| ONE-AT-ONE-SEAM | 1 | 27 | EMBEDDING | NON-NEGATIVE | STRUCT-DEAD | ALIVE |
| ONE-AT-ONE-SEAM | 1 | 27 | QUOTIENT | POSITIVE | COUNT-DEAD | ALIVE |
| ONE-AT-ONE-SEAM | 1 | 27 | QUOTIENT | NON-NEGATIVE | ALIVE | ALIVE |
| ONE-AT-ONE-SEAM | 1 | 27 | LAX | POSITIVE | STRUCT-DEAD | ALIVE |
| ONE-AT-ONE-SEAM | 1 | 27 | LAX | NON-NEGATIVE | STRUCT-DEAD | ALIVE |
| ONE-AT-EVERY-SEAM | 3 | 9 | EMBEDDING | POSITIVE | STRUCT-DEAD | STRUCT-DEAD |
| ONE-AT-EVERY-SEAM | 3 | 9 | EMBEDDING | NON-NEGATIVE | STRUCT-DEAD | STRUCT-DEAD |
| ONE-AT-EVERY-SEAM | 3 | 9 | QUOTIENT | POSITIVE | COUNT-DEAD | COUNT-DEAD |
| ONE-AT-EVERY-SEAM | 3 | 9 | QUOTIENT | NON-NEGATIVE | ALIVE | ALIVE |
| ONE-AT-EVERY-SEAM | 3 | 9 | LAX | POSITIVE | STRUCT-DEAD | STRUCT-DEAD |
| ONE-AT-EVERY-SEAM | 3 | 9 | LAX | NON-NEGATIVE | STRUCT-DEAD | STRUCT-DEAD |
| SEAM-MAP | 6 | 6 | EMBEDDING | POSITIVE | STRUCT-DEAD | STRUCT-DEAD |
| SEAM-MAP | 6 | 6 | EMBEDDING | NON-NEGATIVE | STRUCT-DEAD | STRUCT-DEAD |
| SEAM-MAP | 6 | 6 | QUOTIENT | POSITIVE | COUNT-DEAD | COUNT-DEAD |
| SEAM-MAP | 6 | 6 | QUOTIENT | NON-NEGATIVE | ALIVE | ALIVE |
| SEAM-MAP | 6 | 6 | LAX | POSITIVE | STRUCT-DEAD | STRUCT-DEAD |
| SEAM-MAP | 6 | 6 | LAX | NON-NEGATIVE | STRUCT-DEAD | STRUCT-DEAD |
| FULL-CROSS | 24 | 1 | EMBEDDING | POSITIVE | STRUCT-DEAD | STRUCT-DEAD |
| FULL-CROSS | 24 | 1 | EMBEDDING | NON-NEGATIVE | STRUCT-DEAD | STRUCT-DEAD |
| FULL-CROSS | 24 | 1 | QUOTIENT | POSITIVE | COUNT-DEAD | COUNT-DEAD |
| FULL-CROSS | 24 | 1 | QUOTIENT | NON-NEGATIVE | ALIVE | ALIVE |
| FULL-CROSS | 24 | 1 | LAX | POSITIVE | STRUCT-DEAD | STRUCT-DEAD |
| FULL-CROSS | 24 | 1 | LAX | NON-NEGATIVE | STRUCT-DEAD | STRUCT-DEAD |

Three facts, in the order they matter.

**The count leg is not an axis.** Under the QUOTIENT reading, requiring every
declared cell to carry a positive count is requiring every declared link to
be realised, which with containment one way is the EMBEDDING reading. The
two agree on liveness at every target. They die differently when they die —
at structure under EMBEDDING, at count positivity under QUOTIENT — which is
paper-19's own signature for the two readings, reproduced here without being
aimed at.

**LAX buys the crossing by ceasing to be a test.** Relaxing the reading so
that the target's incidence merely sits inside the realised relation makes
the driven crossing lawful at the delivered target immediately, and makes
every one of the 36 possible crossings lawful too. What it costs is the
weld's whole content: the record then carries a pair the geometry does not
represent, and the dictionary stops being a claim about the record.

**The target extension buys it selectively.** Declaring one cross link, at
one shared site, in one direction, leaves all three delivered legs intact:
the driven crossing is ALIVE under EMBEDDING with positive counts. Declaring
one at *every* shared site does not, because the record realises one crossing
and the target then demands three.

And the extension is not conservative, which the same table says in its own
baseline column. At that one-link target the union WITHOUT the crossing is
STRUCT-DEAD: the geometry now carries a link no division event realises, and
the record that never crosses no longer welds onto it. A declared cross link
is a demand rather than an option — the target that can host a crossing
cannot host the process that declines to make one.

### 4.3 The price, read where the RSQ standard reads it

| arena | declared cross links | maps | I-SITE-ASSIGNMENT | I-DIRECTION-LABEL | I-ORIENT | free items | fate |
|---|---|---|---|---|---|---|---|
| the union, no crossing | 0 | 62208 | 1 | 1 | 1 | 0 | MOTIVATED |
| the crossing alone, NOT DRIVEN | 1 | 1728 | 1 | 1 | 1 | 0 | MOTIVATED |
| SHARED-SEEDED, driven | 1 | 1728 | 3 | 9 | 4 | 3 | UNMOTIVATED |
| B-SEEDED-PURE, driven | 2 | 576 | 1 | 3 | 2 | 2 | UNMOTIVATED |

This is the unit's sharpest row and it was not the expected one. **the
crossing itself is free**: a union whose relation carries one extra
co-division pair between the sectors, against a target carrying one extra
link, welds with zero free items exactly as the plain union does. What costs
is everything else the event brings. A conflict group has three actors, so a
seam-spanning event deposits two further incidences, and those are either
doublings of links the seam already carries or new pairs inside one sector.
The shared-seeded crossing doubles two seam links and the weld's free items
go from 0 to 3 — the site assignment among them, which was 1 at every one of
SEC's 16 types and 1 at paper-19's single sector. The crossing driven from
inside the second sector doubles one link and costs 2.

The second row is a control and is stamped as one: no three-actor group can
produce it. It is in the table to isolate the mechanism, and it does — the
price is not paid by the crossing, it is paid by the company the crossing is
forced to keep.

### 4.4 What the extended dictionary can testify to

THE TEST, DECLARED. A declared cross link has to be placed somewhere, and
the question is whether the placement is a datum. The test is run twice, by
two instruments that share nothing: the placements are reduced by the
union's own automorphism group, and the same question is put through the
detector itself. Blindness would show as one arena and every placement
admitting the event; sightedness as many arenas and a strict sub-count. Both
outcomes are reachable and both occur.

| crossings | declared placements | arenas up to the union's own symmetry | admitted by the detector | verdict |
|---|---|---|---|---|
| 1 | 36 | 1 | 36 | BLIND |
| 2 | 630 | 5 | 108 | SIGHTED |
| 3 | 7140 | 15 | not run | SIGHTED |

At one crossing the geometry cannot say where the crossing happened: all 36
placements give the same arena, and the detector admits the event at every
one of them. At two it can: 630 placements fall into 5 arenas and exactly
108 admit the event, which is the orbit the record's own placement lies in.
The detector's count and the orbit's size agree without being compared into
agreement — they are computed by different machinery.

One consequence deserves its own sentence, because it disarms the obvious
objection. A target extension that carries exactly the links the record
realises looks like a target fitted to its record. At one crossing it cannot
be: every placement gives the same arena, so there is nothing to fit. At two
crossings it can be, and there the fiber is published.

### 4.5 The outcome

`GLUING-EVENT-LAWFUL-AT-THE-MATCHED-CROSS-LINK-EXTENSION`. Of the 288
seam-spanning groups, 216 leave the dictionary alive once the target
declares the cross links the event realises, and both specifications the
committed grammar was measured to admit are among them. The 72 that stay
dead are the groups that also open a pair inside one sector: no cross-link
declaration repairs a lattice that has lost a link of its own.

And not one of the 216 is MOTIVATED. Gluing can be an event in this theory,
at a target that declares the seam it crosses; what it cannot be is a free
one.

## 5. Measurement three — the composite price

SMU measured its price in the currency of independent numbers a declaration
must supply, and found it conserved across the axis it varied — in its own
words,

> declaring a covariant irreducible dynamics on this carrier still supplies

exactly the count of independent numbers its parent already owed, unchanged.
The composition axis is a different axis, and the answer is not one word.
Five currencies are evaluated on every one of the 45,010 composites and on
the lone sector, and each obeys an exact law with zero violations.

| currency | a lone sector | the composite | excess over the two sectors | verdict |
|---|---|---|---|---|
| the record (division incidences) | 27 | 54 | none | IGNORES |
| the carrier (site objects) | 9 | 18 - k | k fewer | FAVOURS |
| the link objects | 27 | 54 - d | d fewer | FAVOURS |
| the geometry's budget (counts over cells) | 27 | 54 + 2d | 2d more | PENALIZES |
| the declaration (independent numbers) | 0 | 4k | 4k more | PENALIZES |

Here d is the number of pairs the union carries twice and k is the number of
shared actors. The two are not independent of the gluing's type, and the
census that fixes them is SEC's, reproduced here from this unit's own
construction:

| type | gluings | carriers | realised pairs | doubled |
|---|---|---|---|---|
| (0,) | 1 | 18 | 54 | 0 |
| (1, (0, 0, 1)) | 81 | 17 | 54 | 0 |
| (2, (0, 0, 1), (0, 1, 1)) | 486 | 16 | 54 | 0 |
| (2, (0, 0, 1), (1, 0, 1)) | 486 | 16 | 54 | 0 |
| (2, (0, 0, 1), (1, 1, 1)) | 1458 | 16 | 53 | 1 |
| (2, (0, 0, 2)) | 162 | 16 | 54 | 0 |
| (3, (0, 0, 1), (0, 1, 1), (0, 2, 1)) | 486 | 15 | 54 | 0 |
| (3, (0, 0, 1), (0, 1, 1), (1, 0, 1)) | 11664 | 15 | 53 | 1 |
| (3, (0, 0, 1), (0, 1, 1), (1, 2, 1)) | 8748 | 15 | 52 | 2 |
| (3, (0, 0, 1), (0, 1, 2)) | 972 | 15 | 54 | 0 |
| (3, (0, 0, 1), (1, 0, 1), (2, 0, 1)) | 486 | 15 | 54 | 0 |
| (3, (0, 0, 1), (1, 0, 1), (2, 1, 1)) | 8748 | 15 | 52 | 2 |
| (3, (0, 0, 1), (1, 0, 2)) | 972 | 15 | 54 | 0 |
| (3, (0, 0, 1), (1, 1, 1), (2, 2, 1)) | 4374 | 15 | 51 | 3 |
| (3, (0, 0, 1), (1, 1, 2)) | 5832 | 15 | 52 | 2 |
| (3, (0, 0, 3)) | 54 | 15 | 54 | 0 |

Read the answer as three sentences, because the pin's three words are all
realised at once.

**the record's own price is exactly additive**: two sectors deposit 27
incidences each and their union carries 54 at every one of the 45,010
gluings, however they are glued. Composition is free to the process.

Composition is *cheaper* in objects: sharing k actors saves k carriers and d
link objects outright. A composite is a smaller thing than two sectors, not
a larger one.

And composition is dearer where the geometry lives. The budget the geometry
must supply over its own cells is 54 + 2d, so every doubled link costs two;
and the declaration price — SMU's own currency, the count of independent
numbers the record does not fix — is 0 for a lone sector and 4k for the
composite.

That last excess is **SEAM-CONFINED**, and the confinement is the point.
Every unshared site's form is determined by its own three links exactly as
in a lone sector; the whole surcharge sits on the shared sites, four numbers
each, twelve at a k = 3 seam. The price of composition is not distributed
over the union. It is a property of the join.

## 6. The walls

**No extension measured here is claimed to be the theory.** Every target in
the window carries its declaration fiber in the row that reports it, and
every lawful cell is lawful AT a declaration. An extension is a declaration,
priced; it is not a discovery about the process.

**The adjudication's ruling is carried.** The union changes geometry only
on links both sectors jointly own; nothing here says otherwise, and the
reversed
wording the adjudication struck does not occur in this paper. The gate that
enforces its absence whitespace-normalises, ASCII-folds and strips markdown
prefixes from both sides.

**No sector narrative, and no reading of the union as anything larger.** The
paper is scanned for the terms whose presence would mean such a reading had
been taken, and none occurs.

**The seam's indefinite completions, still named and still not read.** That
the affine family admits completions of mixed sign is a statement about what
the record fails to fix. This unit adds that they are inadmissible at the
all-simple seam under the corpus's own count law, which narrows the family;
it takes no Lorentzian, causal or dimensional reading of any of it, and
nothing measured here licenses one.

## 7. Every ratio here is COUNTING-ONLY

No measure is declared on the gluing family, on the group family or on the
placement family. Every ratio in this paper — lawful groups of seam-spanning
groups, admitted placements of declared placements, admissible completions
of the enumeration box — is a count over an exhaustive enumeration with its
denominator beside it, and it is stamped COUNTING-ONLY in the receipt. The
orbits differ in size by two orders of magnitude, and nothing here may be
read as a likelihood that a crossing is lawful.

## 8. Choice inventory

| item | class | fiber | where it binds |
|---|---|---|---|
| the base object: two driven R = 3 saturating sectors | forced | 1 | paper-19's own arena, inherited at its pinned sha |
| the gluing, and k | declared, the axis | 45010 | every member enumerated |
| the seam chart: the direct sum | declared | 1 | M1, and the whole completion question lives inside it |
| the completion of the seam's four entries | declared, MEASURED IRREDUCIBLE | 31 at the all-simple seam | M1 |
| the extension window's target axis | declared | 5 | M2 |
| the extension window's reading axis | declared | 3 | M2 |
| the extension window's count leg | declared, MEASURED DEPENDENT | 2 | M2, and it collapses onto the reading axis |
| the carrier and the link individuation | held at the delivered values | 1 | outside this unit's window, named |
| the placement of a declared cross link | declared, MEASURED INERT AT ONE CROSSING | 36 | M2's blindness census |
| I-SITE-ASSIGNMENT | measured | 1 or 3 | M2's inventories |
| I-DIRECTION-LABEL | measured | 1, 3 or 9 | M2's inventories |
| I-ORIENT | measured | 1, 2 or 4 | M2's inventories |
| the cross-direction admissibility reading | declared, VERDICT-ROBUST | 2 | M1, and the verdict is the same at both readings |
| the price currencies | declared | 5 | M3, all five published |
| the three-actor group as the unit of a division event | forced | 1 | d66's committed conflict-group size |

Three items are declared and measured to be inert or dependent, and the
paper says which: the count leg collapses onto the reading axis, the
placement of a single cross link is a gauge, and the completion is
irreducible rather than free in the pejorative sense — it is a declaration
the laws do not narrow.

## 9. Verdict

```
SEC2-SEAM-DECLARATION-IRREDUCIBLE-[49 SEAM TYPES OVER 132273 SHARED SITES; THE COMPLETION SPACE IS 4-PARAMETER AT EVERY ONE, RANK 6 ON 10 BY THE CHART ALONE; AT THE ALL-SIMPLE SEAM 31 COMPLETIONS ASSIGN ADMISSIBLE COUNTS TO EVERY CROSS DIRECTION AND ALL 31 ARE POSITIVE DEFINITE] -- POSITIVITY SELECTS NOTHING; THE CONVENTION-FREE PRICE IS CONSTANT ON THE WHOLE SPACE AND THE ONE-SIDED READING'S MINIMISER MOVES WITH THE CONVENTION; REFINEMENT STABILITY IS EMPTY AT THIS RECORD BY THE CEILING LAW (MIN COUNT 1, CEILING 0) AND, GRANTED AS A HYPOTHETICAL, IS EMPTY AT 48 OF 49 SEAM TYPES AND SELECTS THE DIRECT SUM AT THE 49TH -- THE ONE PRINCIPLE THAT DOES SELECT, MAXIMUM DETERMINANT, IS NAMED AND NOT LICENSED
```

```
SEC2-GLUING-EVENT-LAWFUL-AT-THE-MATCHED-CROSS-LINK-EXTENSION-[THE WINDOW: TARGET x READING x COUNT LEG, 30 CELLS, CARRIER AND LINK INDIVIDUATION HELD AT THE DELIVERED VALUES; 455 THREE-ACTOR GROUPS IN 9 ORBITS, 288 OF THEM SEAM-SPANNING AND EVERY ONE DEAD AT THE DELIVERED TARGET] -- LAWFUL AT 216 OF 288 ONCE THE TARGET DECLARES THE CROSS LINKS THE EVENT REALISES, BOTH DRIVEN SPECIFICATIONS AMONG THEM, AND MOTIVATED AT 0 OF 216: THE PRICE IS THE WELD ITSELF, FREE ITEMS 0 -> 3 AT THE SHARED-SEEDED CROSSING AND 0 -> 2 AT THE B-SEEDED ONE, WHILE THE CROSSING TAKEN ALONE COSTS NOTHING AND NO THREE-ACTOR GROUP CAN DELIVER IT ALONE
```

```
SEC2-COMPOSITE-PRICE-SPLITS-[FIVE CURRENCIES ON ALL 45010 COMPOSITES AGAINST THE LONE SECTOR, ZERO VIOLATIONS: RECORD 54 = 27 + 27 IGNORES COMPOSITION; CARRIERS 18 - k AND LINKS 54 - d FAVOUR IT; THE GEOMETRY'S BUDGET 54 + 2d AND THE DECLARATION PRICE 4k PENALIZE IT] -- AND THE EXCESS IS SEAM-CONFINED: EVERY UNSHARED SITE'S FORM IS DETERMINED EXACTLY AS IN A LONE SECTOR AND THE WHOLE SURCHARGE SITS ON THE SHARED SITES, FOUR NUMBERS EACH
```

```
SEC2-THE-EXTENDED-DICTIONARY-IS-BLIND-AT-ONE-CROSSING-AND-SIGHTED-AT-TWO-[36 PLACEMENTS IN 1 ARENA AT ONE CROSSING AND 36 OF 36 ADMITTED BY THE DETECTOR; 630 PLACEMENTS IN 5 ARENAS AT TWO AND 108 OF 630 ADMITTED; 7140 IN 15 AT THREE] -- SO THE PLACEMENT OF A SINGLE CROSS LINK IS A GAUGE AND NOT A DATUM, AND THE RECORD-FITTED OBJECTION DOES NOT BITE AT ONE CROSSING BECAUSE EVERY PLACEMENT GIVES THE SAME ARENA
```

Read out. Merging can be a process in this theory, and the price is exact.
The seam the merge creates is a declaration the declared laws do not narrow:
its completion space is 4-parameter at every seam type, and every criterion
the pin named leaves it open — positivity trivially, price minimisation
because the convention-free price is flat, refinement because the record is
too coarse to refine. A seam-spanning division event is admitted by the
committed grammar and becomes lawful the moment the geometry declares the
link it crosses, which it can do without moving any leg of the dictionary.
But the crossing never arrives alone: a conflict group has three actors, so
it comes with doublings or with a new pair inside a sector, and those are
what take the weld's forcing away. And the whole surcharge — geometric and
declarational — sits on the shared sites and nowhere else.

## 10. Deviations, priced

1. **The #301 objects are declared, not read.** Price: this unit's
   inheritance is bound by reproduction rather than by bytes. Mitigation:
   the commit and the four digests are published, twenty-two inherited
   values are recomputed from this unit's own construction and gated
   exit-1-only, and a `--verify-sec` mode checks the declaration against
   copies of the committed objects.
2. **The extension census is run at one union arena**, the k = 3 aligned
   one. Price: the group census, the blindness census and the inventories
   are properties of that arena. Mitigation: the seam census and all five
   price currencies are exhaustive over all 45,010 gluings, and the arena
   chosen is the one SEC's own contrast row uses.
3. **The grammar is not re-driven here.** The two admitted cross-sector
   specifications are taken from SEC's declared rows and reconstructed as
   arena objects; their deposited pairs reproduce SEC's driven counts, which
   is what binds the combinatorial route to the driven one. Which of the
   other seam-spanning groups the grammar admits is not decided here and
   is not claimed.
4. **The carrier and the link individuation are held fixed.** They are axes
   of the window in principle and are named as held. Price: the extended
   carriers SEC ran are not re-run, and no claim about them is inherited.
5. **The blindness census is not swept by the detector at three crossings.**
   The orbit count is measured; the detector's own sweep is run at one and
   at two crossings only, and the table says so in its own cell.
6. **The hypothetical refinement reading is a hypothetical**, and it is
   labelled one everywhere it appears: the ceiling law grants zero steps at
   this record, so no completion of this arena is ever actually refined.

## 11. The instrument

`v14/code/sec2_exact.py`, with the era's CLI contract: a delivery run that is
the only writer, `--no-write`, `--numbers`, `--selftest`, `--mutant NAME`,
`--break-anchor NAME`, `--verify-paper [PATH]`, `--verify-sec DIR`,
`--list-gates` and `--list-mutants`; every unknown flag, unknown flag
argument, missing flag argument and second mode flag exits 2.

Arithmetic is exact end to end, and an AST scan of the file is a gate: no
float constant, no call to float or eval, no subprocess or network import,
so the run is correct off-tree and with no version control present. The
seam's forms are carried as doubled integer Gram matrices, which makes
Sylvester positivity and the determinant order integer predicates without
changing either.

Five sources are read at run time, sha-pinned, with the read set recorded at
the I/O layer and gated to be exactly the declared set; eight verbatim
anchors are each located exactly once in their own pinned source under the
whitespace-and-markdown normaliser, cleared against a character floor, and
bound to the gate that consumes them.

The automorphism machinery is this unit's own: an equitable-refinement
backtracking search, exhaustive and uncapped below a declared cap, whose
completeness is gated at every inventory row. The count leg's positivity is
carried into a separate search mode rather than tested on one arbitrary map,
so the reading-collapse gate compares two procedures rather than an object
with itself. Every cell of the window additionally carries an edge-count
necessary condition computed from the two edge sets alone, so a forged
liveness dies without the search being consulted.

Coverage is honest. Every gate is falsified by one of the declared mutants,
each dying at its own named gate, or waived with a machine-checked forcing;
every declared mutant's target gate exists in the run; and every declared
mutant is verified to have an injection site in the source, so a falsifier
that could not fire is a failure rather than a badge. The head is derived a
second time by a comparator that types all four templates itself and rereads
every value from the receipt's own rows. The seal is total — every published
receipt key sealed at the gate that vouched its values or declared unsealed
with its reason — the artifacts are written through a staged replace from
the sealed payload, and the integrity check compares the disk bytes against
the gate-time seal. The paper under test is checked in the same run: every
data row and every header row of every table above is a rendered claim of
the receipt, compared as a multiset in both directions; numeral coverage
includes fenced blocks and inline code spans; the fenced blocks are matched
against this run's own verdict strings; claim polarity is checked against
each row's own negation; and spelled numerals above twelve are scanned.

## 12. The successor register

Registered, not claimed.

**S-1 — which crossings the grammar admits.** The arena census here is
exhaustive over the 455 groups; the grammar's admission is known at three
specifications. A driven census over the version lineage would turn 216 of
288 into a statement about the process rather than about the arena.

**S-2 — the seam at more than two crossings.** Blindness at one and sight at
two is measured. Whether the sighted regime has a law — which orbits a
lawful record can land in — is open, and the orbit counts 5 and 15 are where
it starts.

**S-3 — the completion under a second seam.** The declaration price is 4k
and the completions are censused per seam independently. Whether two seams
of one union constrain each other, and whether the 4k is ever less than the
sum of its seams, is not run.

**S-4 — the price at other budgets.** Every currency here is a law in d and
k at R = 3. What 54 + 2d becomes at R = 6, where a link may carry 2 before
any gluing and the ceiling law is no longer 0, is the first place the
refinement criterion could stop being empty.

**What may not be inherited**, as a standing row: any lawful extension as
the theory rather than as a declaration; the blindness result at any other
arena; the crossing-alone control as a driven object; the determinant
principle as a law of this corpus; and the 216 of 288 as a statement about
the grammar rather than about the arena.
