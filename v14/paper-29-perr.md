# The R = 5 rung: the slack censused, and where the covering class leaves the positive-definite class

**PER-R / paper-29.** Pin `v14/note-perr-pin.md` (FROZEN, sha256-12
`6339ba42f354`, ledger #233). Code `v14/code/perr_exact.py`; artifacts
`v14/code/perr_output.txt`, `v14/code/perr_receipt.json`.

**Verdict**, in four segments. The first is the SIG feed, stated separately
because another unit's Stage 0 consumes it.

```
PERR-SIG-FEED-AT-R=5-[COVERED CODES 90 = 84 POSDEF + 3 SINGULAR + 3 INDEFINITE; THE INDEFINITE REGION OPENS HERE, AT 4det [-5]; COVERING-CLASS CODES 32, MAX CELL COUNT 4, 4det SUPPORT [0, 3, 4, 7, 8, 11, 12, 15]] -- INSIDE THE COVERING CLASS: THE SINGULAR BOUNDARY IS REACHABLE (WITNESS [1, 1, 4] AT EXACTLY 1 OF 9 SITES, 41 INCIDENCES, 3 OF 5 ROUNDS SATURATING) AND THE INDEFINITE REGION IS NOT (THE LOCKING THEOREM: NO COVERING QUINTUPLE CARRIES A CELL COUNT OF 5) -- SO COVER=POSDEF BREAKS AT R=5 AFTER HOLDING AT R=3 AND R=4 -- RECORD FLOORS: G-SINGULAR R=6, G-INDEF R=8@EXHAUSTIVE-OVER-1,721,036,800,000-ORDERED-GROUPING-QUINTUPLES
```

```
PERR-PREDICTIONS-3-OF-3-PASS-[(a) NO DECLARED RECORD AT COUNT-SUM 5: I7'S OWN BOX HOLDS 6 ADMISSIBLE POINTS THERE, THE STRATUM REACHES ALL 6 AND 0 ARE DECLARED -- AND EVERY DECLARED HOMOGENEOUS RECORD OF I7'S 9 HAS AN EVEN COUNT SUM, THE INTEGER-q12 SUBLATTICE, AGAINST ITS OWN BOX'S 181 EVEN AND 180 ODD | (b) ZERO-FREE-ITEMS IMPOSSIBLE: A LIVE R-TUPLE SPENDS 9 PER ROUND OVER 27 CELLS SO LINK-CONSTANCY NEEDS R=0 MOD 3, AND THE ARENA'S OWN LINK-CONSTANT CONTROL DIES STRUCT-DEAD ON 18 FOREIGN PAIRS | (c) STRICTLY WEAKER IN BOTH CURRENCIES: DECLARED YIELD 276 AT R=4 AND 0 HERE, MOTIVATED AT NEITHER, WHILE R=6 BUYS BOTH -- AND STRICTLY RICHER IN EVERY SLACK COLUMN]
```

```
PERR-SLACK-18-AT-R=5-[= 9(R-3), THE PARENT'S FORMULA; BINDING=THE COVER (45 > 27); THE SEQUENCE GAINS A ROW AND NO CONDITION] -- WHAT THE SLACK BUYS ALONG R=3/4/5: SITE CODES 54/105/181 | COVERING-CLASS CODES 1/7/32 | MAX CELL COUNT 1/2/4 (BLOCK QUANTISATION BREAKS) | 4det SUPPORT 1/3/8 | COVER=POSDEF True/True/False
```

```
PERR-DICTIONARY-[WELD FIBERS 1/1/1(R=3) -> 36/3/1(R=4) -> 36/3/1(R=5) -> 1/1/1(R=6), FOUND EXACTLY AT THE LINK-CONSTANT RECORDS AND UNMOTIVATED EVERYWHERE ELSE; THE R=5 SIGNATURE IS THE R=4 SIGNATURE] -- DRIVEN: THE COMMITTED GRAMMAR DRIVES 19 SCHEDULES OVER BUDGETS 4/5/6 WITH 19 OF 19 DRIVEN FIELDS EQUAL TO THEIR GROUPINGS' FIELD, ANCHORED AT d66's OWN COMMITTED R=4/6 ROWS -- THE R=6 DOOR CENSUSED EXACTLY: [2, 2, 2] AT 48,600 AND I7'S DECLARED G-SINGULAR AT 1,350 ORDERED SATURATING SEXTUPLES -- DIA: A PARALLEL CLASS IS COMPULSORY EXACTLY WHEN THE RECORD COUNTS ITS LINK MORE THAN ONCE AND COUNTS SOME LINK EXACTLY ONCE, ON 13 OF 13 ROWS; THE COUNT CLAUSE ALONE IS FALSIFIED AT [[2, 2, 2]]
```

Between delivery and adjudication every headline reading here is a
**candidate reading**.

---

## 1. The question

Paper-21 (terminal at v14 #232, adjudicated at #211) closed the R = 4 arena
with a sequence rather than a fact. Its three
price rows — the budget at R = 2, the perfect matching at R = 3, the cover at
R = 4 — are the three branches of one comparison, and its own sentence says
what follows:

> The three rows are the three branches of one comparison, 9R against 27, so
> for every R ≥ 4 the cover binds, with slack 9(R − 3)

so a successor's fourth row is a **slack census** and not a fourth binding
condition. Beside that it registered three falsifiable predictions about the
next budget and a saturation theorem to be re-proved as a schema rather than
inherited, and it left one question open in as many words:

> What remains open is not the absence but its persistence: whether the
> maximum cell count stays at 2 when the slack grows

This unit runs that rung. It answers, in order: the record-class structure at
R = 5 — computed first and stated separately, because the signature unit's
Stage 0 consumes it; the three predictions, each with its own witness; the
slack census; the weld fibers along the whole ladder; and which parallel
classes are compulsory. One census the pin names is **not** run: the
interference census, which PER-L's adjudicated corollary (paper-28, v14 #228) closes
by theorem for every rung of this ladder.

## 2. The arena, declared as data (RUNBOOK §15)

The base object is d66's `CONFLICT-GRID(g = 3, R)`. Nine actors sit on a
3 × 3 grid, the actor names parse as a bijection onto Z_3^2, and each round
spends the committed budget: three conflict groups of three cells each,
partitioning the grid, each running one cycle of the committed transport
grammar. The variable is the schedule. A round is a partition of the nine
sites into three triples with a seed chosen in each, and the partition count
is computed by two routes that share no code — exhaustive enumeration and the
closed form 9!/(3!^3 · 3!) — which agree. Measured: **280 partitions, 36 of
them saturating, and a family of 1,721,036,800,000** ordered grouping
quintuples at this budget.

A round's incidence spectrum on I7's own 27 cells is 1 partition at 0, 27 at
4, 54 at 6, 162 at 7 and 36 at 9, so no round deposits more than 9. The
saturating stratum is exactly the top of that spectrum.

### 2.1 The alphabet, and the code space

A conflict group holds three sites, so one round can co-group a site with at
most two of its three declared partners. The per-round site-code alphabet is
therefore every 0/1 code of weight at most 2 — seven of them — and the run
measures that the same seven are realised at each of the nine sites
separately. The rounds are independent at a fixed site, so the codes a budget
reaches are the R-fold sumset of that alphabet.

That identity is not asserted. Run at the two budgets whose answers are
committed it returns paper-21's own counts, read from that unit's receipt:
**54** reachable site codes at R = 3 and **105** at R = 4. At R = 5 it returns
**181**.

The census below is taken at one site and speaks about all nine, and that too
is measured: each of the nine chart translations is applied to each of the 280
partitions and the translate's own cell mask is compared against the image of
the original's mask, cell by cell — 2,520 pairs, no mismatch.

## 3. Stage 0 — THE SIG FEED

*This section is the signature unit's Stage-0 input and is stated separately
from everything below it.*

### 3.1 The covered codes, split by their own Sylvester value

A site code is COVERED when all three of its counts are at least 1, and its
class is read off its own determinant by I7's own criterion — a record is
admissible when q is nonsingular and positive definite at every site, by the
exact Sylvester criterion. Measured: **90 covered site codes at this budget:
84 positive definite, 3 singular and 3 indefinite**.

At R = 4 the same census returns 44 covered codes, 41 of them positive
definite and 3 singular — exactly paper-21's three identity-breaking codes,
(1, 1, 4), (1, 4, 1) and (4, 1, 1) — and **none** indefinite. So det ≥ 0 is
forced at R = 4 by arithmetic, and **the indefinite region opens at R = 5**,
at three codes, (1, 1, 5), (1, 5, 1) and (5, 1, 1), every one of them at
4det = −5.

### 3.2 The covering class, censused exhaustively over the whole family

The sharper question is not which codes exist but which occur at a site of a
quintuple that covers all 27 cells. That census is exhaustive over all
1,721,036,800,000 ordered grouping quintuples: a tuple's site code is the sum
of its rounds' local types there, so every tuple with a given code lies in
exactly one type multiset, and within a multiset the set of achievable unions
is carried forward in full.

| R | site codes | covering-class codes | max cell count | cover = posdef |
|---|---|---|---|---|
| 3 | 54 | 1 | 1 | yes |
| 4 | 105 | 7 | 2 | yes |
| 5 | 181 | 32 | 4 | **no** |

Run one round down the same instrument returns paper-21's committed covering-
class row exactly — 7 site codes, all inside {1, 2}³, maximum cell count 2,
determinant support {3, 4, 7} — by a route that unit did not use. Here
**32 of the 90 covered codes occur at a site of a covering quintuple**, the
determinant support is {0, 3, 4, 7, 8, 11, 12, 15}, and **the covering class's
maximum cell count is 2 at R = 4 and 4 here**: block quantisation does not
survive the slack.

### 3.3 The locking theorem

A cell carrying count R forces its two sites into one conflict group in every
round. The union of five such rounds is searched exhaustively at each of the
three declared links, and it never reaches all 27 cells: **no covering
quintuple carries a cell count of 5**. The mechanism is counted beside the
search. The cells whose covering pair contains one of the two locked sites
demand 7 distinct third members, and five rounds supply at most five, so the
count decides it before any search does.

Every covered indefinite code at this budget carries a 5. The theorem
therefore says that **the indefinite region is unreachable inside the covering
class** at R = 5 — the COVERING-RECORD class of §3.6 — while the
COVERED-SITE-CODE class says it exists there.

### 3.4 The witness, exhibited round by round

The singular codes carry a 4, and 4 is reachable. The receipt exhibits, round
by round, one covering quintuple with 41 incidences, 3 of its five rounds
saturating, and exactly one singular site. Its nine site codes are
read one at a time; eight are positive definite and the remaining one is
(1, 1, 4) at 4det = 0 — I7's own declared `G-SINGULAR` count vector. So **the singular
boundary is reachable inside the covering class** — the COVERING-RECORD class
of §3.6 — and the identity that held
at the two budgets below breaks here: the covering class and the positive-
definite class coincide at R = 3 and at R = 4 and part company at R = 5.

It is not a saturating quintuple, and that is why the stratum census of §5
cannot see it: 41 incidences, not 45.

### 3.5 The record floors

As RECORDS — the same count vector at every one of the nine sites — I7's
declared family sits at the budgets its own count vectors sum to, by the
ladder law of §4.2:

| record | counts | budget | class |
|---|---|---|---|
| G-ANISO | [1, 4, 5] | 10 | POSDEF |
| G-ANISO2 | [4, 9, 13] | 26 | POSDEF |
| G-DIAG2 | [2, 2, 4] | 8 | POSDEF |
| G-FLAT | [1, 1, 2] | 4 | POSDEF |
| G-INDEF | [1, 1, 6] | 8 | INDEFINITE |
| G-OFFDIAG | [2, 2, 6] | 10 | POSDEF |
| G-OFFDIAG2 | [3, 5, 12] | 20 | POSDEF |
| G-OFFNEG | [3, 5, 4] | 12 | POSDEF |
| G-SINGULAR | [1, 1, 4] | 6 | SINGULAR |

### 3.6 The reachability ladder, class by class

A determinant sign is not reachable at one budget. It is reachable at four
different budgets depending on WHICH class is being asked about, and a floor
for one class is not a floor for another. The four classes are named here
exactly as the instrument names them: a COVERED SITE CODE is a site code with
all three links present, with no condition on the rest of the record; a
COVERING RECORD covers all 27 cells; a STRUCTURALLY LIVE RECORD carries no
foreign pair, so every one of its rounds saturates; an I7-DECLARED RECORD is
one of I7's own eleven. Each floor is computed separately and the nesting is
checked rather than assumed.

| polarity | covered site code | covering record | structurally live record | I7-declared record |
|---|---|---|---|---|
| SINGULAR | 4 | 5 | 6 | 6 |
| INDEFINITE | 5 | 6 | 7 | 8 |

Measured: **the indefinite region is attained at R = 5 as a covered site code,
at R = 6 as a covering record, at R = 7 as a structurally live record and at
R = 8 as one of I7's declared records**. The singular boundary runs one rung
ahead of it in the first three classes and two in the fourth, because I7's
declared list is not a lattice of everything admissible.

### 3.7 The feed, in one place

> At R = 5 the singular boundary is REACHABLE in the COVERING-RECORD class, at
> a named witness, and the indefinite region is NOT — it is reachable there
> only as a COVERED SITE CODE, and its covering-record floor is R = 6. In the
> STRUCTURALLY LIVE class both floors are one rung higher again, R = 6 and
> R = 7, and I7's own declared `G-SINGULAR` and `G-INDEF` arrive as whole
> records at R = 6 and R = 8. A polarity census run at R = 5 over covering
> records can therefore see det = 0 and can never see det < 0; one run at
> R = 4 can see neither; and one run over structurally live records at R = 5
> can see neither.

## 4. Stage 1 — the three predictions

### 4.1 Prediction (a): no declared record at this budget

**Prediction (a) PASSES**, and on the strongest witness available. I7's
committed count box is walked point by point rather than searched: **I7's box
holds 6 admissible count vectors summing to 5, the stratum reaches every one
of them, and 0 are declared**. The prediction is confirmed by exhaustion, not
by an absence of search.

Why it holds is not an accident of this budget. Measured: **all 9 of I7's
homogeneous declared records carry an even count sum, while its own admissible
box splits 181 even and 180 odd**. The mechanism is checked record by record:
the sum is even exactly when q12 = (n_diag − n_e1 − n_e2)/2 is an integer, so
the declared family lies inside the integer-off-diagonal sublattice while its
own box does not. Every odd budget of this ladder is declared-record-empty,
and R = 5 is the first one the ladder reaches above the rigidity floor.

### 4.2 Prediction (b): zero free items is impossible here

**Prediction (b) PASSES**, proved in the arena rather than by citation. The
standard is paper-21's theorem — zero free items holds exactly at the
link-constant records, and I7 declares none of them — and the arithmetic is
this unit's. A structurally live R-tuple spends 9 incidences a round over 27
cells, so a field constant on all three links needs 27 to divide 9R: **a
link-constant field needs 27 to divide 9R, so R must be divisible by 3**. The
ladder's rows are computed one at a time, and the residue at this budget is
not zero.

The premise is not vacuous, and the run shows why. This arena's own R = 5
link-constant control — the three declared classes with the undeclared
direction taken twice — carries a field identically 1 and dies at STRUCTURE:
**the link-constant control at this budget dies STRUCT-DEAD on 18 foreign
pairs**. Link-constancy is reachable at R = 5; it is not reachable *live*.

### 4.3 Prediction (c): strictly weaker than the rung below

**Prediction (c) PASSES** in the ladder's two currencies, and the
counter-column is published beside it. The currencies are a DECLARED RECORD
and a MOTIVATED WELD, and each budget's yield is computed from the records'
own count vectors: **the declared-record yield is 276 at R = 4 and 0 here, and
1350 at R = 6**, while a motivated weld is possible only at the budgets
divisible by 3. R = 4 buys one currency, R = 6 buys both, and R = 5 buys
neither.

In every slack column the same budget is strictly RICHER, and those columns
are reported here rather than suppressed: site codes 105 → 181, covering-class
codes 7 → 32, maximum cell count 2 → 4, determinant support 3 → 8 values, and
the covering class inside the saturating stratum 9,936 → 1,842,120. The
prediction is about what the rung BUYS, not about how big it is.

## 5. Stage 2 — the slack census

### 5.1 The saturation schema, re-proved at this rung

No round deposits more than 9 link incidences, so five rounds carry at most
45; a homogeneous record whose counts sum to 5 needs 9 × 5 = 45, and each
target's requirement is recomputed from its own count vector. Equality forces
every round to saturate, so a census over the 60,466,176 saturating quintuples
is exhaustive over all 1,721,036,800,000 for these targets. The schema is
re-proved here, not inherited.

Inside that stratum, **1,842,120 of the 60,466,176 ordered saturating
quintuples cover all 27 cells**, over 619,092 distinct induced fields. Run at
R = 3 the same census returns paper-21's committed I7-STRICT count of 72, and
at R = 4 every homogeneous record it reaches matches that unit's committed row
— 276 each at (1, 1, 2), (1, 2, 1) and (2, 1, 1).

### 5.2 The slack, and what it buys

Measured: **the slack is 18 = 9(R - 3) and what binds is the cover** — 45
incidences over 27 cells. The sequence therefore gains a ROW and no condition, exactly as
the parent said it would. What the slack buys is the content of the rung, and
it is measured column by column in the table of §3.2 and in the head:
site codes 54/105/181, covering-class codes 1/7/32, maximum cell count 1/2/4,
determinant support 1/3/8 values, and the cover-equals-positive-definite
identity true, true, false.

The one column that closes rather than opens is the last, and it closes
against the direction of the others: the covering class grows and stops being
a positive-definite class in the same step.

## 6. Stage 3 — the dictionary row

Weld 2's detector is carried unchanged at both of its declared readings, with
the fibers computed as the number of distinct count fields each choice
produces. Every arena here is the collinear arrangement of a homogeneous
record, and every row is stamped with its reading.

| arena | budget | fibers (site/label/orient) | fate | link-constant |
|---|---|---|---|---|
| R3-SAT(1,1,1) | 3 | 1/1/1 | FOUND | yes |
| R4-FLAT(1,1,2)=G-FLAT | 4 | 36/3/1 | UNMOTIVATED | no |
| R5-COLLINEAR(1,1,3) | 5 | 36/3/1 | UNMOTIVATED | no |
| R5-(1,2,2) | 5 | 36/3/1 | UNMOTIVATED | no |
| R6-(2,2,2) | 6 | 1/1/1 | FOUND | yes |
| R6-(1,1,4)=G-SINGULAR | 6 | 36/3/1 | UNMOTIVATED | no |

At R = 4 the instrument returns paper-21's committed fibers and its 1296
isomorphisms exactly; at R = 6 the link-constant record returns zero free
items. The R = 5 rung returns 36/3/1 at both of its records and at both
readings: the ladder law predicted an imperfect weld here, and the price is
2 free items — **the same signature the rung below carries**. The imperfection
neither grows nor shrinks with the slack.

The law behind the column is measured per arena rather than assumed: the three
fibers are all 1 exactly at the link-constant records. And the last row is a
result rather than a repetition — I7's own declared `G-SINGULAR` is reachable
at R = 6, one rung below the declared record paper-21 registered, and the weld
there is UNMOTIVATED for the same reason every non-link-constant record's is.
The stratum census counts that rung exactly, where the parent could give a
constructive lower bound of 5,184: **(2, 2, 2) at 48,600 ordered saturating
sextuples and G-SINGULAR at 1,350**.

### 6.1 Driven, not only counted

Nothing at R = 5 or R = 6 had been driven before this unit. Here the committed
grammar drives both: **19 schedules driven over budgets 4, 5, 6, with 19 of 19
driven fields equal to their groupings' field**, cell by cell, with the
footprints taken from the layer's own register reader. The parent's registered
question was whether the committed grammar drives a concatenation, with the
conflict-supply question re-asked two (resp. four) rounds wider: **the
committed grammar drives it**, at maxhits 1 and with no refusal anywhere in
the window.

The driver is anchored twice, and one anchor is wider than this unit's own
budget: d66's committed constructor is re-run in-process at R = 4 and at R = 6
and emits event lists identical to the schedule-driven builder's, and each
driven profile matches d66's own committed output row read from its pinned
bytes — (66, 12, 18) and (102, 18, 30).

### 6.2 The declared driven window W5

The window is 19 schedules and is named in the head. W5-LADDER is the
collinear arrangement of every homogeneous record the R = 5 stratum reaches —
all six, none sampled; W5-SEEDFAN is the (1, 1, 3) arrangement at all nine
canonical transversal choices of its first two rounds; W5-CTRL and W6-CTRL are
d66's own R = 5 and R = 6 points; W6-DOOR is the link-constant concatenation
and I7's declared `G-SINGULAR` arrangement. Every combinatorial column of this
paper is exhaustive over an object the window does not cap; what the equality
above licenses is reading those columns as statements about driven records.

## 7. Stage 4 — the DIA row

Paper-21 measured that the diagonal class is compulsory in all 276 of its
G-FLAT quadruples and read it no further, calling the agreement with the
doubly-counted link a coincidence it did not read. It is not a coincidence,
and it is not quite a count law either.

| record | budget | witnesses | compulsory classes | multisets |
|---|---|---|---|---|
| [1, 1, 2] | 4 | 276 | DIA | 12 |
| [1, 2, 1] | 4 | 276 | ROW | 12 |
| [2, 1, 1] | 4 | 276 | COL | 12 |
| [1, 1, 3] | 5 | 680 | DIA | 12 |
| [1, 2, 2] | 5 | 1,350 | DIA, ROW | 12 |
| [1, 3, 1] | 5 | 680 | ROW | 12 |
| [2, 1, 2] | 5 | 1,350 | COL, DIA | 12 |
| [2, 2, 1] | 5 | 1,350 | COL, ROW | 12 |
| [3, 1, 1] | 5 | 680 | COL | 12 |
| [2, 2, 2] | 6 | 48,600 | none | 78 |
| [1, 1, 4] | 6 | 1,350 | DIA | 12 |
| [1, 2, 3] | 6 | 4,020 | DIA, ROW | 12 |
| [3, 2, 1] | 6 | 4,020 | COL, ROW | 12 |

Every witness of every row is enumerated and every class is counted against
its own record. Measured: **a parallel class is compulsory exactly when the
record counts its link more than once and counts some link exactly once, and
the count clause alone is falsified at the link-constant record**. At
(2, 2, 2) every link is counted twice and NO class is compulsory at all, in
48,600 witnesses — so the compulsion is carried by the scarce link, and it
vanishes at exactly the record where the weld turns motivated. The undeclared
direction appears in no witness of any row.

## 8. The census not run

The interference census is **not run here**, and the abstention is measured
rather than declared. PER-L's adjudication (v14 #228, on paper-28) records the corollary that closes
it for this whole ladder — its transport is closed by theorem, so PER-R
inherits it and one census is cancelled. A gate scans this run's declared
measurement surface — every published receipt key together with the statement
and evidence of every gate evaluated — and finds no interference reading in
it; the falsifier writes one in and dies there.

## 9. The walls

**L-1 — argued before any test, then declined.** Order-level covariance is a
fourth form outside paper 8's three, and its admissibility is v11's to argue.
Admissibility would require a group declared to act on the generated causal
order and a reason to read that group as a covariance group. This arena
supplies finite records and a translation action on their site lattice; the
corpus contains no bridge from Z_3^2 translations to any boost, and this unit
constructs none. **The fourth form is not tested here.** The sentence
retracted in 2026 is not reproduced, and the gate that enforces its absence
whitespace-normalises, ASCII-folds and strips markdown prefixes from both
sides.

**BHS — no sprinkling-grade Lorentz-invariance test.** A Poisson sprinkling
admits no Lorentz-invariant finite-valency graph, and these schedules are
finite-valency by construction, so running the test would manufacture a false
negative. None is run, and the abstention is a scan of the declared surface.

**Kleitman–Rothschild — every dimension reading carries a height control.**
This unit takes no dimension reading at all: no chart width, no Myrheim–Meyer
estimate, no max-shatter reading. The height control is therefore not owed and
not manufactured.

**The Lorentzian resonance, NAMED.** A reader arriving from the relativity
line will hear "signature" in a paper whose central measurement is a
determinant changing sign class. The naming sentence is mandatory: **the
induced form is NAMED AND NOT READ: q = [[1, 1/2], [1/2, 1]] at this rung's
first record is a positive definite Euclidean form on a nine-site lattice, it
is not a signature, it is not a metric on any continuum, and no Lorentzian
reading of it is taken here or licensed by anything measured here.** The
singular and indefinite classes of §3 are classes of an integer count code
under I7's own Sylvester criterion, and nothing else.

**The diagonal — measured, and read no further.** The diagonal is one of three
declared directions on a nine-site lattice, and §7's compulsion is a statement
about parallel classes of AG(2,3). No cosmological or continuum reading is
taken.

## 10. Choice inventory

| # | item | class | fiber | where it binds |
|---|---|---|---|---|
| 1 | the base object: CONFLICT-GRID(3, R) | **forced** | 1 | pin, from the committed constructor |
| 2 | the per-round budget: 3 groups of 3 | **forced** | 1 | the committed cycle, anchored event for event at two budgets |
| 3 | the site carrier: actors to Z_3^2 | **forced** | 1 | the constructor's own actor naming |
| 4 | admissibility: the layer's own menu | **forced** | 1 | d42b1 driven directly |
| 5 | the I7 readout, links and record family | **forced** | 1 | I7's own receipt, compared coordinate by coordinate |
| 6 | R = 5 rather than R = 4 or R = 6 | **declared, VERDICT-DETERMINING** | 1 | the pin; both neighbours are measured in-unit |
| 7 | the driven window W5 | **declared** | 1 | §6.2, disclosed in the head |
| 8 | the site the local-type census is taken at | **forced** | 1 | §2.1, by measured translation invariance |
| 9 | the reading axis (EMBEDDING / QUOTIENT) | **declared** | 2 | weld 2's, carried unchanged |
| 10 | `I-SITE-ASSIGNMENT` | **measured** | **36** | §6, at every arena above the floor |
| 11 | `I-DIRECTION-LABEL` | **measured** | **3** | §6 |
| 12 | `I-ORIENT` | **measured** | **1** | §6 |
| 13 | the declared falsifier (one division withheld) | **free** | — | a division-set edit on the driven record |

## 11. Verdict

```
PERR-SIG-FEED-AT-R=5-[COVERED CODES 90 = 84 POSDEF + 3 SINGULAR + 3 INDEFINITE; THE INDEFINITE REGION OPENS HERE, AT 4det [-5]; COVERING-CLASS CODES 32, MAX CELL COUNT 4, 4det SUPPORT [0, 3, 4, 7, 8, 11, 12, 15]] -- INSIDE THE COVERING CLASS: THE SINGULAR BOUNDARY IS REACHABLE (WITNESS [1, 1, 4] AT EXACTLY 1 OF 9 SITES, 41 INCIDENCES, 3 OF 5 ROUNDS SATURATING) AND THE INDEFINITE REGION IS NOT (THE LOCKING THEOREM: NO COVERING QUINTUPLE CARRIES A CELL COUNT OF 5) -- SO COVER=POSDEF BREAKS AT R=5 AFTER HOLDING AT R=3 AND R=4 -- RECORD FLOORS: G-SINGULAR R=6, G-INDEF R=8@EXHAUSTIVE-OVER-1,721,036,800,000-ORDERED-GROUPING-QUINTUPLES
```

```
PERR-PREDICTIONS-3-OF-3-PASS-[(a) NO DECLARED RECORD AT COUNT-SUM 5: I7'S OWN BOX HOLDS 6 ADMISSIBLE POINTS THERE, THE STRATUM REACHES ALL 6 AND 0 ARE DECLARED -- AND EVERY DECLARED HOMOGENEOUS RECORD OF I7'S 9 HAS AN EVEN COUNT SUM, THE INTEGER-q12 SUBLATTICE, AGAINST ITS OWN BOX'S 181 EVEN AND 180 ODD | (b) ZERO-FREE-ITEMS IMPOSSIBLE: A LIVE R-TUPLE SPENDS 9 PER ROUND OVER 27 CELLS SO LINK-CONSTANCY NEEDS R=0 MOD 3, AND THE ARENA'S OWN LINK-CONSTANT CONTROL DIES STRUCT-DEAD ON 18 FOREIGN PAIRS | (c) STRICTLY WEAKER IN BOTH CURRENCIES: DECLARED YIELD 276 AT R=4 AND 0 HERE, MOTIVATED AT NEITHER, WHILE R=6 BUYS BOTH -- AND STRICTLY RICHER IN EVERY SLACK COLUMN]
```

```
PERR-SLACK-18-AT-R=5-[= 9(R-3), THE PARENT'S FORMULA; BINDING=THE COVER (45 > 27); THE SEQUENCE GAINS A ROW AND NO CONDITION] -- WHAT THE SLACK BUYS ALONG R=3/4/5: SITE CODES 54/105/181 | COVERING-CLASS CODES 1/7/32 | MAX CELL COUNT 1/2/4 (BLOCK QUANTISATION BREAKS) | 4det SUPPORT 1/3/8 | COVER=POSDEF True/True/False
```

```
PERR-DICTIONARY-[WELD FIBERS 1/1/1(R=3) -> 36/3/1(R=4) -> 36/3/1(R=5) -> 1/1/1(R=6), FOUND EXACTLY AT THE LINK-CONSTANT RECORDS AND UNMOTIVATED EVERYWHERE ELSE; THE R=5 SIGNATURE IS THE R=4 SIGNATURE] -- DRIVEN: THE COMMITTED GRAMMAR DRIVES 19 SCHEDULES OVER BUDGETS 4/5/6 WITH 19 OF 19 DRIVEN FIELDS EQUAL TO THEIR GROUPINGS' FIELD, ANCHORED AT d66's OWN COMMITTED R=4/6 ROWS -- THE R=6 DOOR CENSUSED EXACTLY: [2, 2, 2] AT 48,600 AND I7'S DECLARED G-SINGULAR AT 1,350 ORDERED SATURATING SEXTUPLES -- DIA: A PARALLEL CLASS IS COMPULSORY EXACTLY WHEN THE RECORD COUNTS ITS LINK MORE THAN ONCE AND COUNTS SOME LINK EXACTLY ONCE, ON 13 OF 13 ROWS; THE COUNT CLAUSE ALONE IS FALSIFIED AT [[2, 2, 2]]
```

### 11.1 The persistence table

Every invariant paper-21 delivered is re-measured here, and each row's verdict
is read off its own pair of measurements rather than assigned. Measured:
**8 invariants re-measured: 3 BREAKS-AT-R=5, 4 PERSISTS, 1 TRANSFORMS**.

| invariant | at the rung below | here | verdict |
|---|---|---|---|
| the binding constraint of the price law | THE COVER | THE COVER | PERSISTS |
| the saturation schema | every round forced to saturate | every round forced to saturate | PERSISTS |
| the weld fiber signature | 36/3/1 | 36/3/1 | PERSISTS |
| the fiber law (all ones iff link-constant) | holds | holds | PERSISTS |
| cover = positive definite | True | False | BREAKS-AT-R=5 |
| block quantisation (the covering class's cell ceiling) | 2 | 4 | BREAKS-AT-R=5 |
| the compulsory parallel class | compulsory when the link is counted more than once | and only when some link is counted exactly once | TRANSFORMS |
| the declared-record yield | 276 | 0 | BREAKS-AT-R=5 |

Read out. The three breaks are the content of the rung.

**PERSISTS.** The price law's binding constraint: the cover binds here as it
binds at R = 4, with the slack the parent's formula gives. The weld's fiber
signature: 36/3/1, the R = 4 value, at every R = 5 record and at both
readings — and the fiber law itself, all-ones exactly at the link-constant
records, holds at every rung measured. The saturation schema: re-proved rather
than inherited, and exact.

**TRANSFORMS.** The DIA row. Paper-21's coincidence is a law, but not the one
the count alone suggests: compulsion needs a scarce link, and at the
link-constant record it disappears entirely.

**BREAKS.** Block quantisation: the covering class's maximum cell count rises
from 2 to 4, so the mechanism that kept R = 4's empty cell empty does not
survive the slack. And with it the identity that mechanism protected — the
covering class and the positive-definite class part company at exactly this
budget, at a witness with one singular site carrying I7's own declared
`G-SINGULAR` code.

The three predictions all pass, and two of them pass in a stronger form than
they were posed: (a) because the stratum reaches every admissible box point at
this count sum and none is declared, with the parity law behind it; (c)
because the counter-column is measured rather than conceded. The rung buys
neither of the ladder's currencies and is richer than its predecessor in every
other column — which is what a slack census is for.

## 12. Deviations, priced

1. **The covering-class census is exhaustive by local type, not by
   enumeration of all 1,721,036,800,000 quintuples one at a time.** The
   quantifier is complete and the pruning is the budget theorem alone, but the
   census answers an EXISTENCE question per code — which codes occur — and not
   a counting question. Price: this unit publishes no weighted determinant
   spectrum over the whole covering class at R = 5, where paper-21 published
   one at R = 4. Mitigation: the weighted spectrum IS published over the
   saturating stratum, where the census is a count.

2. **The stratum census is a window on the covering question and an
   exhaustive census on the record question.** Every homogeneous record whose
   counts sum to the budget forces every round to saturate, so the stratum is
   the whole family for those targets; it is not the whole family for the
   covering class, and the singular witness of §3.4 lies outside it. Both
   scopes are named wherever a number from them appears.

3. **The driven window is 19 schedules.** Driving is hundreds of milliseconds
   a record and grows with the budget. Price: the FORCED reading is exhaustive
   on W5 and not on the family. Mitigation: the window contains the collinear
   arrangement of every homogeneous record this budget reaches, the driven-
   versus-combinatorial equality is measured on all 19, and every other column
   is exhaustive over an object the window does not cap.

4. **The R = 6 rows are a census, not a drive of the whole stratum.** The
   48,600 and the 1,350 are exact counts over the saturating stratum at that
   budget; two of those sextuples are driven, and no claim is made about the
   rest beyond the equality the window measures.

5. **The falsifier is a division-set edit, not a re-drive**, following
   paper-19's and paper-21's precedent: one division event is withheld from
   the driven record's own footprint list, and it is labelled a falsifier
   everywhere it appears.

6. **The det spectrum is published as 4·det**, an integer, so that every
   census runs in integers; the Fraction is formed only where a form is
   printed.

## 13. The instrument

`v14/code/perr_exact.py`, with the #82 CLI contract: a delivery run that is
the only writer, `--no-write`, `--numbers`, `--selftest`, `--mutant NAME`,
`--break-anchor NAME`, `--verify-paper [PATH]`, `--list-gates` and
`--list-mutants`; every unknown flag, unknown flag argument, missing flag
argument and second mode flag exits 2.

Arithmetic is exact end to end: an AST scan of the file finds no float literal
and no true division, and a recursive type scan of the emitted receipt finds
no float. Counts are computed, never typed. Gates bind objects rather than
aggregates (#87): the alphabet is measured at every site separately, every
covered code is classified against its own Sylvester value, every declared
record's budget is recomputed from its own count vector, every driven field is
compared cell by cell, and every table row is rendered from the receipt and
required to occur exactly once.

Provenance is by pinned sha with the products gated (#46/#91): 14 sources are read
at run time, the set of reads is required to be exactly the declared set, and
every reader records its category — SOURCE, OBJECT-UNDER-TEST, SELF or the
run's own staged artifacts. No subprocess of any kind is invoked, so the run
is correct off-tree and with no version control present. The #62 verbatim anchors
each clear a length floor and each name the gate that consumes them, and every
text gate whitespace-normalises, ASCII-folds and strips markdown line prefixes
(#125).

Eight columns are back-validated against numbers this unit did not produce,
read from paper-21's committed receipt and from d66's committed output rather
than re-typed: the reachable site-code counts at R = 3 and R = 4; the
covering-class row at R = 4 — its code count, its maximum cell count and its
determinant support; the identity-breaking codes at R = 4; the saturating
stratum's covering class at R = 3 and its homogeneous records at R = 4; the
weld fibers and isomorphism count at R = 4; the DIA row at R = 4; the
constructive lower bound at R = 6; and d66's own event profiles at R = 4 and
R = 6. An error in this unit's machinery would have to reproduce all of them
to survive.

The coverage ledger is honest (#34): every gate is either falsified by a
declared mutant or waived with a forcing that says why it cannot fail, the
denominator is the gate count of the run, and every falsifier is checked
against its own code — each declares the object it corrupts, the run locates
every hook by AST, publishes the source of the statement carrying it, and
rejects outright any corruption that is a constant boolean (E-23).

The seal is TOTAL (#119, #148): every published receipt key — the measured
layer and the vouching layer alike — is either sealed at the moment its gate
passes or listed as DECLARED-UNSEALED, and the completeness gate compares the
manifest against the declared key set. The artifacts are written from the
sealed payload through `os.replace`; the terminal integrity gate compares the
bytes on disk against the gate-time seal after a deliberately corrupted probe
has been shown to be detected; a run that fails a gate writes nothing.

The head is derived a second time by a comparator that shares no code, no
input and no typed value with the builder: an AST scan reads the string
constants of both routines, requires them to be disjoint, and requires that
once the declared object names are removed no numeral and no number-word
survives in either. The paper under test is checked in the same run for claim
rendering, table rendering, numeral coverage — prose, tables, inline code
spans and the fenced verdict blocks alike — and claim polarity, with the
fenced blocks gated by MULTISET equality against the declared copy count
rather than by containment (E-22). Every fraction this unit publishes is a
cardinality over an exhaustively enumerated finite set and is stamped
COUNTING-ONLY; no typicality claim rests on any of them (E-24).

## 14. The successor register

Registered, not claimed.

**S-1 — the weighted covering census at R = 5.** This unit decides WHICH codes
occur in the covering class over the whole family and counts the class only
inside the saturating stratum. The weighted determinant spectrum over the full
covering class at R = 5 — and with it the measure-stability row paper-21
published at R = 4 — is one algorithm away and is not run here.

**S-2 — the singular rung, driven.** `G-SINGULAR` is a DECLARED record
reachable at R = 6, and this unit drives its collinear arrangement. What it
does not do is ask what a singular record means for the refinement laws: R6a's
split fiber, CR-B's per-interval law and R6b′'s kernel are all defined on it.
R6b′'s measured support hole is at counts 1 and 2:
G-FLAT's counts and the link-constant record's lie entirely inside it, while
three of the six records this rung reaches carry a count of 3 and G-SINGULAR
carries a 4. Those are the first welded records in this line with an interval
outside that hole. Whether the kernel is non-empty on them is a reading of
that unit's committed rows and is not taken here — it is the first place
these rungs could buy a law over records rather than a map.

**S-3 — the locking theorem's general form.** The theorem proved here is that
no covering quintuple carries a cell count of 5. The counting mechanism —
seven required third members against R available rounds — is budget-independent
in form, and whether it gives the exact ceiling at every budget (the observed
sequence is 1, 2, 4) is open and cheap.

**S-4 — the parity law's scope.** All nine declared homogeneous records have
an even count sum and the mechanism is integrality of q12. Whether that is a
choice of I7's or a constraint of its construction is a question for the unit
that declared the family, not for this one.

**What may not be inherited**, as a standing row: the covering-class code
census as a COUNT rather than an existence census; the stratum as the family
outside the record targets the schema licenses; "the indefinite region is
unreachable" without its budget; the singular witness as a driven record; the
DIA law without its scarce-link clause; the parity law as anything but a
statement about I7's declared list; and any dynamics, signature, dimension,
cosmological or continuum reading whatever.
