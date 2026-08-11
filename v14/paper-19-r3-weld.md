# The R = 3 arena and the weld

**R3-WELD / paper-19.** Pin `v14/note-r3weld-pin.md` (FROZEN, sha256-12
`20fba9b15f5e`, ledger #154). Code `v14/code/r3_weld_exact.py`; artifacts
`v14/code/r3_weld_output.txt`, `v14/code/r3_weld_receipt.json`.

**Verdict**, in three segments.

```
R3-ARENA-UNIT-GRADE-[n=1 at 27 of 27; det=3/4 at 9 of 9; POSDEF 9 of 9; FORCED 1040 of 1040; FULL-GROUP REACHABLE 1680]@WINDOW-1040-OF-432081216000+31-STRATUM-WITNESSES
```

```
POSITIVE-GEOMETRY-[CEILING 9 ATTAINED at 72 of 21952000 GROUPING TRIPLES; 8 NEVER ATTAINED; I7-STRICT=POSDEF-9=FIELD-IDENTICALLY-1 (SITEWISE: POSDEF(x) IFF min_l n_l(x)>=1, AT ALL 64 REACHABLE SITE CODES); DET-SPECTRUM 9 VALUES ON 197568000 CELLS]
```

```
WELD3-FOUND-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT<ISOS=1296=|AUT(K333)||QUOTIENT-MAPS=1296|FIBERS=1/1/1(SITE/LABEL/ORIENT,BASE-MAP-INVARIANT)|INDUCED-RECORD=(1,1,1):q=[[1, -1/2], [-1/2, 1]]:det=3/4:ADMISSIBLE-BY-HA-SYLVESTER:INSIDE-I7'S-OWN-361-POINT-DECLARED-BOX:NOT-ONE-OF-ITS-11-DECLARED-RECORDS:THE-WELD-IS-TO-I7'S-RECORD-SPACE(WELD-2'S-OWN-FOUND-AT-I7-WITNESS-(2,2,2)-WAS-ADMISSIBLE-AND-UNDECLARED-TOO) -- SCOPE=THE-SATURATING-STRATUM(72-OF-21952000-GROUPING-TRIPLES-IN-THE-COMMITTED-NAMING;288-UP-TO-THE-SITE-ASSIGNMENT-THE-READING-DECLARES-FREE;STRATUM-WIDE-BY-THEOREM:ALL-72-CARRY-ONE-ARENA-IN-12-MULTISETS-EACH-WITNESSED)|GRAMMAR-ADMISSIBLE-NOT-COMMITTED(d66'S-OWN-R=3-POINT-SPENDS-27-INCIDENCES-ON-18-OF-27-CELLS-AND-IS-COUNT-DEAD)|COVERAGE-NOT-COUNT(46656-TRIPLES-PAY-THE-FULL-27;72-WELD;1-IN-648)|ROUTE-B-MOOTED-AT-THIS-TARGET-AND-CARRIER -- CONTROLS=FOUND-AT-CRYSTAL@L2(ISOS=72,FIBERS-ALL-1)|FALSIFIER-FLIPS(UNMOTIVATED,SITE-FIBER=6)|EMPTY-AT-WALK(ARITY-DEAD:2-OBJECTS-AGAINST-9)|CRYSTAL-AT-I7(STRUCT-DEAD:DIAGONAL-0-AT-9-OF-9)|R3-FALSIFIER(STRUCT-DEAD) -- READINGS-DIFFER=DEAD-ROWS-DIE-AT-STRUCTURE-UNDER-EMBEDDING-AND-AT-COUNT-POSITIVITY-UNDER-QUOTIENT|DIRECTED-COMPARATOR=0-AT-ALL-8-ARENAS|STRICTEST-READING(SITE-CARRIER-FIXED)=R3-SAT-SURVIVES-AT-n=1;R3-ROW|COL|ANT-DIES-AT-9-ZERO-CELLS>
```

Between delivery and adjudication every headline reading here is a
**candidate reading**.

---

## 1. The question

Weld 2 asked whether the transport grammar can supply the gravity line's
record lattice and found the census EMPTY, at both readings of "a map". Its
sharpest datum was not the emptiness but its cause: across the committed
crystal family the diagonal link count is identically zero, so

> the diagonal link count is identically zero at 9 of 9 sites in 5 of 5
> crystals

and the induced determinant vanishes at every site of every one of them. No
committed grammar record induced an admissible I7 geometry record at all, and
the FOUND branch at I7's own three-link target could be exhibited only on a
declared probe.

U4 and U4b then turned the constructor into a variable and found the cause
was arithmetic rather than blueprint. A round of `CONFLICT-GRID(3, R)`
deposits at most 9 link incidences on I7's link set; positive definiteness at
a site needs 3; nine sites therefore need 27, and two rounds have 18. U4b's
census measured the consequence exhaustively — positive-definiteness ceiling
3, I7-strict criterion empty — and its effectus review named the way out:

> The emptiness is a **resource deficit in the committed cycle**, not a
> structural impossibility of the arena.

with the minimal saturating configuration exhibited by hand:

> three rounds grouped on the three link-direction parallel classes give
> `n_l(x) = 1` at all 27 cells, `q = [[1, -1/2], [-1/2, 1]]`, det = 3/4 > 0,
> **positive definite at all nine sites**, and I7's strict criterion satisfied
> for the first time.

The U4b adjudication entered that computation into the successor register as
this unit's exact demand —

> THE R=3 SATURATION enters the successor register as the weld route's exact
> demand (reviewer-grade: R=3 on the three link classes -> n = 1 at all 27
> cells, det = 3/4, posdef 9/9 -- to be made unit-grade by the successor)

— and the effectus attached four conditions: constructibility **driven**,
because at R = 3 the round-2 conflict-supply question is new; the affine null
re-pre-registered on the summed field, because the full group becomes
reachable; and an explicit statement about what 27 incidences do and do not
buy.

This unit runs those three stages. **For the first time neither degeneracy
nor budget forecloses the answer.**

## 2. The arena, declared as data (RUNBOOK §15)

### 2.1 The base object and the variable

The base object is d66's `CONFLICT-GRID(g = 3, R = 3)`. Nine actors sit on a
3 × 3 grid, so the actor names parse as a bijection onto Z_3^2 and this unit
assigns no site. Each round spends the committed budget: three conflict
groups of three cells each, partitioning the grid, each running one cycle of
the committed transport grammar — the conflict-supply deliveries from the
group's seed to any member that does not already hold the base, then three
proposals, then one 3-proposer arbitration won by the seed. d66 says of that
cycle:

> each group is a g-PROPOSER conflict (g + 1 registers) whose base is supplied
> by g - 1 deliveries from the group's diagonal seed

The variable is the schedule: which cell-triples arbitrate per round, and
which member seeds each group. At this budget a round is a partition of the
nine sites into three triples with a seed chosen in each. The count is
computed by two routes that share no code — exhaustive enumeration returns
280 partitions, the closed form 9!/(3!^3 · 3!) returns 280 — so a round has
280 × 27 = 7560 schedules and the R = 3 family has **432,081,216,000**.

### 2.2 The generalized driver is the committed constructor

Admissibility is never decided by fiat. The committed d42b1 transport layer
enters as a single source, cut at the layer's own banner print, and
`candidates_for`, the layer's own menu function, decides every event. d60's
builder, d66's `conflict_grid` and `double_grid`, and d58's `walk2` enter by
AST extraction of their definitions, so no module-level statement of theirs
can run. The driver is then anchored against the object it generalizes: at
the committed R = 2 schedule it and d66's own `conflict_grid(3, 2)`, re-run in
this process, emit **identical event lists**. Three further numbers are read
from committed files at run time and reproduced rather than re-typed — d66's
own `GRID(g=3,R=4)` and `GRID(g=3,R=6)` rows — 66, 12, 18 and 102, 18, 30 — and
I7's own admissible-point count for its declared count box.

The menu is memoised on (history, initiators) and the memo is gated rather
than trusted: 24 declared window schedules are re-driven with the memo
disabled and their records compared event for event.

### 2.3 The declared window, disclosed here and in the head

Driving 432,081,216,000 records is not affordable. The **declared driven
window W3** is the union of two families, and it is named inside the arena
verdict string so no reader can meet the number without meeting its scope:

- **W3-CLASS** — all 4^3 = 64 ordered triples of the parallel classes of
  AG(2,3), d66's own resolvable device extended one round;
- **W3-SAT** — **all 72** I7-STRICT grouping triples, exhaustive: the pin's
  primary object is inside the window entire, not sampled;

each at the first two canonical transversals of every round's grouping. That
is **1040 driven schedules**, one in 415,462,707 of the family.

**Every other column below is exhaustive over an object the window does not
cap.** The geometry census runs over all 21,952,000 ordered grouping triples;
the crystallinity census over all 592,704 ordered seed-set triples; the
fragility census over all 1,417,176 schedules of the saturating stratum. What
licenses that is the same equality U4b used, re-measured here: for every one
of the 1040 driven records the link field read off the DRIVEN record — the
footprints taken from the layer's own `regs_of` — equals the field the
combinatorial route computes from the schedule alone, and so does the
initiator field. **1040 records compared, 0 mismatches.** Those 1040 records
span **130 distinct grouping triples** of the 21,952,000 — the object the
exhaustive columns quantify over — and the 130 include all 72 that carry the
verdict.

## 3. Stage 1 — the arena, unit-grade

### 3.1 The reviewer-grade computation, confirmed

The uniform arrangement — three rounds grouped on ROW, COL and DIA, the three
parallel classes whose directions are I7's three links — is built by driving
the menus, every specification matched by exactly one menu candidate and no
refusal anywhere. Measured cell by cell: **the uniform R = 3 arrangement runs
to 48 events with 9 division events and its driven link field is 1 at every
one of the 27 cells**, so **det = 3/4 at all nine sites and the form is
positive definite at 9 of 9**.

| quantity | measured |
|---|---|
| cells with n = 1 | **27 of 27** |
| link incidences deposited | **27 of 27** available |
| q at every site | `[[1, -1/2], [-1/2, 1]]` |
| det at every site | **3/4** |
| positive definite sites | **9 of 9** |

Every cell and every site is checked against its own value, not against an
aggregate. The pin's Stage-1 demand is confirmed **unit-grade and driven**.

### 3.2 Forcedness

| fate | count |
|---|---|
| FORCED | **1,040** |
| BRANCHING | 0 |
| REFUSED | 0 |

The record is **FORCED at 1,040 of 1,040 driven window schedules**.

Every record carries exactly 9 division events and every specification is
offered exactly once. Record length is a clean trichotomy — 32 schedules of
36 events, 192 of 42 and 816 of 48 — and the reason is the conflict supply: a
round needs no supply for a group whose members already share a base, which
happens exactly when the round repeats an earlier grouping.

**Both negative fates are reachable, and the instrument sees them.** Two
controls are declared and run. *The no-supply control*: the uniform
arrangement with its first conflict-supply delivery withheld. The layer
refuses the first proposal by an actor that does not hold the base —
`propose G10` at prefix 14 — and a refusal is recorded, never patched. *The
under-specified control*: the committed R = 2 record replayed to prefix 3,
where an arbitration by `G00` is asked for without its conflict key and winner
key; **7** menu candidates match, so the builder's own `maxhits` reads 7 and
the fate is BRANCHING.

Only the candidate COUNT is reported, and the control **stops there**. d60's
`pick` breaks ties with `sorted(key=repr)`, and a frozenset's repr depends on
the interpreter's per-process string hashing, so *which* candidate an
under-specified pick selects is not reproducible across runs — and a control
that continued past one would carry that irreproducibility into every later
menu size. This unit learned that the hard way: an earlier construction drove
the whole schedule under-specified and its reported count moved between runs
at a fixed input. Every event of every schedule in this census is specified by
its full tuple, where at most one candidate can match and the tie-break is
never consulted.

**Thirty-one strata, each with a driven witness.** The census stratifies by
(stabilizer × affine class × geometry class). The declared stratum scan — 136
grouping triples at all 19,683 of their seed triples each — realises 31 cells,
and every one is given a deterministic representative whose record is built by
driving the menus. All 31 are FORCED.

### 3.3 Homogeneity, and where the geometry lives

All **576** driven saturating records are homogeneous — one and the same
(n_(1,0), n_(0,1), n_(1,1)) at all nine sites — and all of them carry the
**same** field. The geometry is a function of the groupings alone: the
saturating slice spans many seed triples and induces exactly **1** distinct
count field.

### 3.4 Crystallinity, re-pre-registered on the summed field

The effectus's demand (iii) was that the affine null be stated on the summed
field rather than on a seed set, and its demand (ii) was that the null be
re-pre-registered at all, because at R = 3 the field sums to 9 over 9 sites,
the shape (1, 1, 1) exists, and

> the full group Z32 becomes reachable

U4b's "the full group never occurs" is a budget fact about R = 2 and it dies
here. Over all **592,704** ordered seed-set triples:

| Stab | seed-set triples |
|---|---|
| 1 | 588,780 |
| ⟨(1,0)⟩ | 561 |
| ⟨(0,1)⟩ | 561 |
| ⟨(1,1)⟩ | 561 |
| ⟨(1,2)⟩ | 561 |
| **Z_3^2** | **1,680** |

3,924 triples are crystalline. The four directions carry exactly equal weight,
as at R = 2, and **the full group Z_3^2 is reachable at R = 3, at 1,680 of
the 592,704 ordered seed-set triples** — a cell that is exactly the ordered
partitions of the nine sites into three seed sets: 1,680 measured, and
9!/(3!)^3 = 1,680 counted a second way from the closed form.

The null is not violated anywhere. At every one of the 3,924 crystalline
triples the summed field is a non-negative integer combination of the period's
coset indicators — **the affine law taken on the union** — and the shape over
the three cosets is one of (3, 0, 0), (2, 1, 0) and (1, 1, 1), the last being the
full group. No CU-SPLIT triple is crystalline. And crystallinity is not
confined to the inherited locus at R = 3 either: **3,816 of the 3,924
crystalline seed-set triples are beyond-coset**, and 1,656 of the 1,680
full-group triples are.

Each stabilizer is computed three times by routes sharing no code and no typed
constant — translation of the field, the annihilator of the support of the
exact Z_3^2 Fourier transform in Z[w] = Z[t]/(t^2 + t + 1), and a walk of the
subgroup lattice. The three agree at all **13,051** distinct fields.

### 3.5 Fragility, on both variables — and the contrast

A single-arbitration **re-seating** moves one division event to another cell
of its own conflict group: 9 arbitrations by 2 alternative seats, 18 per
schedule. Measured exhaustively on the weld's own stratum — all 1,417,176
schedules on the 72 I7-STRICT grouping triples with every one of their 19,683
seed triples — **8,424** are crystalline, and **every one of the 151,632
single-arbitration re-seatings of a crystal breaks the period**. The
mechanism is one line: an edit changes the
field by 1_new − 1_old, a difference of two distinct point masses is never
constant on the cosets of an order-3 subgroup, and it is never constant at
all, so the full-group crystals die with the rest. The edits'
grammar-admissibility is driven for the first 8 crystalline schedules of the
stratum enumeration and all 144 of their re-seatings, every one FORCED.

A single **grouping transposition** — swapping two sites between two conflict
groups of one round — is the geometry's own minimal edit. Over the 72
I7-STRICT triples every such edit is taken, and **none of the 5,832
single-transposition grouping edits leaves the triple I7-STRICT**.

Read together these are the arena's sharpest structural statement. **Each
saturation is destroyed by the edit that moves its own variable.** The crystal
is a property of the seeds and dies to a re-seating while the groupings are
held; the geometry is a property of the groupings and dies to a transposition
while the seeds range over all 19,683 choices without moving it by one cell.

Three of the four cells are measured — 151,632 of 151,632, 5,832 of 5,832, and
the 19,683-fold seed invariance. The fourth is not run and is not claimed: a
grouping transposition can move a seed out of its own group, so the edited
schedule is not always well formed, and the sense in which the crystal is
untouched by it is that the seed *sets* are held fixed as sets. And the
content of the contrast is in the two destruction columns, not in the
invariances: at this generator a division event's footprint **is** its
conflict group, so the geometry is a function of the groupings by
construction and the period a function of the seed sets, and the measurements
confirm that rather than discover it. A successor that changes the count
generator loses both invariances.

## 4. Stage 2 — the positive-geometry census

Exhaustive over **all 21,952,000 ordered grouping triples**; no window.

### 4.1 The attained ceiling, and an empty cell

| positive-definite sites | ordered triples |
|---|---|
| 0 | 4,341,196 |
| 1 | 8,655,660 |
| 2 | 6,350,724 |
| 3 | 2,177,064 |
| 4 | 384,318 |
| 5 | 38,286 |
| 6 | 4,410 |
| 7 | 270 |
| **8** | **0** |
| **9** | **72** |

U4b measured 3 at R = 2 against a wall that permitted 6. At R = 3 the wall
permits 9 and 9 is attained: **the attained positive-definiteness ceiling is
9, at 72 of the 21,952,000 ordered grouping triples**. The distribution also
carries a result nobody asked for — **8 positive-definite sites never occur**
— so the ceiling is attained or missed by at least two.

### 4.2 The rigidity theorem, and the sitewise identity under it

A round deposits at most 9 link incidences and a positive-definite site needs
3, so 9 positive-definite sites need all 27 — every round saturating, every
cell covered exactly once. Hence the field is identically 1 and det = 3/4 at
every site. The three classes therefore **coincide**:

> I7-STRICT = POSDEF-9 = FIELD-IDENTICALLY-1

and the census confirms it at every object: the I7-STRICT class has exactly
**one** distinct field across its whole population, and the ceiling
population equals the strict population. So **I7-STRICT, POSDEF-9 and
field-identically-1 are the same class, and it has 72 ordered grouping
triples in 12 multisets** — counted by two routes that share no code, the
packed exhaustive census over all 21,952,000 triples and a direct search over
the 36 saturating partitions alone — carrying **1,417,176** schedules.

Of those 12 multisets exactly **one** is the three link-direction parallel
classes the effectus exhibited; the other **11** each contain conflict groups
that are not lines of AG(2,3). The exhibited configuration is one arrangement
in twelve, not the arrangement.

The theorem is stronger than the budget argument that reaches it, and the
census measures the stronger form. Write n_(1,0), n_(0,1), n_(1,1) for the
three link counts at a site; three rounds deposit at most one incidence per
cell, so no count exceeds 3 and a site's whole state is one of 64 codes. Over
all 64 the form is **positive definite at a site if and only if all three link
counts are at least 1 there, at every one of the 64 site codes this family can
reach** — checked code by code, no counterexample. So POSDEF and I7-STRICT are
not two predicates that happen to coincide at the top of the ladder: they
coincide **sitewise**, at every site of every one of the 21,952,000 triples,
and the whole positive-definite distribution above is therefore also the whole
strict distribution. The 27-incidence budget is how the ceiling is *reached*;
the sitewise identity is why the ceiling *is* the strict class.

### 4.3 The determinant spectrum

Over every site of every ordered triple — 197,568,000 cells, a count computed
rather than typed:

| det | cells |
|---|---|
| −9/4 | 3,375,000 |
| −1 | 24,300,000 |
| −1/4 | 77,760,000 |
| 0 | 62,487,000 |
| **3/4** | **15,660,000** |
| 1 | 11,745,000 |
| 7/4 | 2,025,000 |
| 2 | 162,000 |
| 3 | 54,000 |

Nine values. 328 triples are homogeneous.

### 4.4 The coordinate-free class, and why the two numbers differ

I7-STRICT is a statement in the **committed actor naming**. The weld's site
assignment is free — it is one of the pin's own inventory items — so the
detector of §5 sees a coarser object: the covered unordered pair set, which
must be the complement of *some* parallel class with every pair covered
exactly once. Counted exhaustively for each of the four classes in turn, the
answer is **72 each**: **the coordinate-free saturating class is 288 ordered
grouping triples, exactly four times the 72 that are I7-STRICT in the
committed naming**.

The 216 extra triples are the ones whose conflict groups run along a direction
I7 does not declare — the ANT class contributes nothing to any I7 link count
in fixed coordinates — and which nevertheless carry the target's incidence
once the site assignment is used. Every fixed-coordinate measurement in this
unit carries 72; the weld carries 288; and the difference is the site
assignment, priced in §5.4 rather than hidden.

### 4.5 The pipeline, validated against a committed result

Before being used one round wider, the geometry census is run at R = 2 over
all 78,400 ordered partition pairs. It reproduces U4b's committed row exactly:
positive-definiteness ceiling **3** against a wall of 18 // 3 = **6**,
I7-STRICT **empty**, maximum incidences **18**, and **747** pairs
non-degenerate at all nine sites. The wall and ceiling numbers are read from
the U4b adjudication at run time, not typed here.

## 5. Stage 3 — the weld, re-posed

### 5.1 The machinery, and what is cited rather than re-run

Weld 2's detector is used unchanged, at both of its declared readings.
Under the **embedding** reading a candidate is

> a bijection from site objects to sites under which the grammar's link
> relation **contains** the target's incidence

and under the **quotient** reading a surjection of the realised objects onto
the sites carrying every realised edge onto a declared displacement. Every
row below is stamped with the reading it was decided under. Admissibility is
undirected on the kill side and the admit side alike, for weld 2's reason; the
directed comparator is carried, and here is its number — **the directed
comparator returns 0 at every one of the 8 arenas where it is defined**, the
two FOUND rows included. It separates nothing anywhere, which is exactly why
HA §14 requirement 3 forbids it as the admit test, and it is also why
reporting it moves no verdict: FOUND holds at the undirected reading, and the
number that would have made the directed one an alternative is zero.

The site and link generators are the one cell weld 2 left live at a record
arena — site ← ACTOR, link ← the co-division actor pair, count ← the division
events on that pair inside the declared window. **The pre-registered dead
list is cited and not re-run**: R6b′'s C1–C5 with free items 6/5/1/4/1,
`BRG-EMPTY-AT-CARRIER`, GW1 §2's order-only spatial instruments, v12's
arena-free Γ objects, the naive 9↔9, weld 2's scissors scope — the (A,B)
carrier at depth ≤ 4 — and weld 2's transport-carrier cells. No row of this
census re-derives one.

### 5.2 One arena, measured rather than assumed — and the verdict is stratum-wide

All **72** I7-STRICT grouping triples are driven, and every one of them
carries the **identical** co-division arena: the same nine site objects, the
same 27 unordered realised pairs, the same count 1 on every one of them. The
census below therefore has one arena and not seventy-two, and that is a
measurement.

It is also the reason the FOUND row below is not a property of the one
arrangement the effectus exhibited. The 72 fall into 12 multisets and every
one of the 72 is driven, so every multiset carries a driven witness; and
§4.2's rigidity theorem says why the measurement could not have come out any
other way. Any I7-STRICT triple covers all 27 cells exactly once, so its
realised co-division relation is forced to be exactly the target's own Cayley
incidence — window or no window, driving or no driving. **FOUND at this arena
is stratum-wide by theorem, not window-relative**, and the window's job is
only to show that the grammar drives the schedules that realise it.

### 5.3 The census

Nine declared arenas at both readings; each row's fate is compared against the
fate declared for its own cell before the run.

| arena | @EMBEDDING | @QUOTIENT |
|---|---|---|
| **R3-SAT** (the saturating record) | **FOUND** | **FOUND** |
| R3-ROW\|COL\|ANT (saturating after relabelling) | **FOUND** | **FOUND** |
| R3-COMMITTED-GRID(3,3) — d66's own R = 3 point | STRUCT-DEAD | COUNT-DEAD |
| R3-SAT-FALSIFIER (one arbitration withheld) | STRUCT-DEAD | COUNT-DEAD |
| R2-COMMITTED-GRID(3,2) | STRUCT-DEAD | COUNT-DEAD |
| CRYSTAL/DOUBLE-GRID(3,2) @ its own 2-link lattice | **FOUND** | **FOUND** |
| CRYSTAL/DOUBLE-GRID(3,2) @ I7 | STRUCT-DEAD | COUNT-DEAD |
| CRYSTAL-INHOMOGENEOUS @ 2-link (the falsifier) | UNMOTIVATED | UNMOTIVATED |
| D58-GENERIC-2-ACTOR-WALK @ I7 | ARITY-DEAD | ARITY-DEAD |

**The readings differ, and the difference is the result.** The dead rows die
at *structure* under the embedding reading and at *count positivity* under the
quotient reading: the rook's graph a row/column schedule realises is not
isomorphic to I7's link structure, but it does embed in it, so the quotient
maps exist and are then killed by the nine cells the missing diagonal leaves
at zero.

### 5.4 The weld, and the choice standard

At the saturating arena the detector returns **FOUND** at both readings.

- **1,296 site assignments carry the record's co-division incidence onto
  I7's link structure and every one of them gives the same count field** —
  the same number weld 2 could reach only with a declared probe, read here
  from weld 2's pinned bytes and reproduced by this unit's own exhaustive
  enumeration on a driven grammar record. The quotient reading returns the
  same 1,296 maps.
- The choice inventory, with the fibers computed as the number of **distinct
  count fields** each choice produces: `I-SITE-ASSIGNMENT` **1**,
  `I-DIRECTION-LABEL` **1**, `I-ORIENT` **1**. **Zero free items** — the RSQ
  standard's definition of MOTIVATED. The mechanism is measured and it is
  homogeneity: the field is identically 1, so the whole isomorphism orbit, all
  six direction relabellings and both orientations collapse to one field.
- The standard is not vacuous here, because the declared falsifier's
  site-assignment fiber is **6** and its direction-label fiber is **2**.
- The label and orient fibers are read at the base map the actor-name order
  fixes, so their independence of that choice is measured rather than assumed:
  both are re-read at every one of the 1,296 base maps and both are constant.

**Where the 1,296 comes from, said plainly.** The two readings are opposite
inclusions — the embedding reading asks that the realised relation *contain*
the target's incidence, the quotient reading that it be *contained in* it — so
FOUND at both means the driven record's co-division relation **is** I7's own
Cayley incidence, at equality. That incidence is the complete tripartite graph
on three parts of three, whose automorphism group has order 3! × (3!)^3 =
1,296. The map count is therefore the target's own symmetry, forced once
equality holds, and the three fibers are 1 for the same reason. It is one
datum presented three ways, not three independent measurements agreeing; what
is new is that a **driven** record realises the equality.

**And FOUND at the primary arena does not need the site assignment to be free
at all.** Under the strictest reading available — the site carrier fixed to
the constructor's own actor → Z_3^2 parse, which is inventory item 3 and which
this unit calls forced — the saturating record still induces a strictly
positive field, 1 at every one of the 27 cells. The same reading kills the
relabelling row: **R3-ROW|COL|ANT leaves 9 of the 27 cells at zero**, because
the ANT class deposits nothing on any I7 link in fixed coordinates. The free
site assignment carries the second FOUND row and nothing else, exactly as
§4.4 and deviation 6 price it.

### 5.5 What the weld lands on

The induced record is n_l(x) = 1 at all 27 cells, hence
q = [[1, −1/2], [−1/2, 1]] with det = 3/4.

- Measured at every site against I7's own sentence, **the induced record is
  admissible by I7's own exact Sylvester criterion and lies inside I7's
  declared count box, whose 361 admissible points this run recomputes**:
  > A record is **admissible** when $q$ is nonsingular and positive definite
  > at every site, by the exact Sylvester criterion
- And **it is not one of I7's 11 declared records**. Each declared record —
  the nine homogeneous ones in I7's own receipt and the two site-dependent
  ones — is compared against the induced vector's whole chart orbit, so the
  comparison is per record and not by name.

That distinction is the honest scope of this result. **The weld lands inside
I7's admissible class and outside its declared list.** The corpus's first
grammar record to induce an admissible I7 geometry induces a record I7 never
wrote down.

**What that distinction is worth is settled by the precedent, and the
precedent is measured, not argued.** The object which fixed what reaching
FOUND at this target means is the one weld 2 reached it on: its declared
probe. Weld 2's committed receipt is a pinned source here, and its probe's
count field is read from those bytes and put through this unit's own readout.
Measured: **weld 2's own FOUND-at-I7 witness is the declared probe whose
induced record is (2, 2, 2), admissible by the same criterion, inside the same
box, and not one of the 11 either.** So the branch weld 2 reserved was never a
branch onto
a declared record. **The weld is to I7's record space — its lattice, its
positivity axiom and its Sylvester criterion — and the eleven are named
witnesses inside that space rather than the gate.** This unit lands the same
species of object, on a driven grammar record instead of a probe.

What the undeclaredness costs is downstream and should travel with the result.
`(1,1,1)` is the minimal interior point of the box: every one of its 27
intervals carries count 1, and by paper-04's own split fiber ∏(n_l − 1) a
count-1 interval cannot be split into two strictly positive parts. The landing
record is therefore **unsplittable, split fiber 0 at all 27 intervals**, so
the refinement grammar, the stochastic split and the renewal-transport kernel
are empty on it. **The weld reaches a record; it does not yet reach a law over
records.**

**The induced form is NAMED AND NOT READ: q = [[1, -1/2], [-1/2, 1]] is a
positive definite Euclidean form on a nine-site lattice, it is not a
signature, and no Lorentzian reading of it is taken here or licensed by
anything measured here.**

### 5.6 The controls, two-way and falsified

HA §14 requirement 3 is carried verbatim and honoured:

> A predicate that cannot return its other value anywhere in the declared
> arena is not a measurement

Every value this detector can return is exhibited in this run. **FOUND** on
the R = 3 saturating record and on d66's own `DOUBLE-GRID(3,2)` at the lattice
that record carries, with **72** site assignments all giving one count field —
weld 2's committed number for the same object, read and reproduced.
On the declared falsifier — the same crystal with one row-group arbitration
withheld — **the declared falsifier returns UNMOTIVATED with a site-assignment
fiber of 6**, weld 2's committed value for the same object.
**STRUCT-DEAD** on the crystal at I7 — weld 2's unanticipated measurement
reproduced, diagonal co-division count zero at **9 of 9** sites — and on this
unit's own falsifier, the uniform record with one arbitration withheld, whose
co-division relation loses one triangle. **COUNT-DEAD** on the committed
R = 3 grid. **ARITY-DEAD** on d58's generic 2-actor walk, re-run at its
committed depth 30 and seed 4242: **2 site objects against 9**, which is a
property of the walk and not of the plumbing. **SMUGGLED** on the declared
S-valued probe.

The no-smuggling classifier is reported with its qualifier: every census
candidate's count function is built from the link relation alone and is a
*constant* function of the I7 record it is handed, so `SMUGGLED = 0` across
the census is **structural, not measured**, and the classifier's positive
value is exercised only by the declared probe.

### 5.7 Necessary, not sufficient — and what is sufficient is coverage

The effectus's demand (iv) asked for an explicit statement that

> (iv) an explicit statement that >= 27 incidences is necessary, not
> sufficient, for the weld.

**Necessity is a theorem and it is measured**: all 72 I7-STRICT triples carry
exactly 27 incidences, and no schedule of this budget can carry more.

**The count alone is not sufficient, and the census contains the
counterexample.** Every triple of saturating partitions pays in full:
**46,656 ordered grouping triples deposit the full 27 incidences and exactly
72 of them weld, one in 648**. d66's own R = 3 point is one of the others. It
does not deposit fewer than 27 — it **spends all 27 of its incidences on 18 of
the 27 cells**, doubling nine row cells and leaving the nine diagonal cells at
zero, and it is COUNT-DEAD for exactly that reason.

**What is necessary and, at this candidate family and this target, sufficient
is the coverage condition: every one of the 27 cells covered at least once.**
That condition is I7-STRICT itself, and §4.2's rigidity theorem then forces
the field to be identically 1, the co-division relation to be the target's own
Cayley incidence, and every fiber to be 1.

Read that way the sequence the two budgets make is the result. At R = 2 the
**budget** was binding: 18 incidences against a requirement of 27, a genuine
resource deficit, and the class is empty. At R = 3 the budget stops binding —
46,656 triples pay it in full — and the binding constraint becomes a perfect
matching of incidences onto cells. That is what the third round actually buys,
and it is what makes the 72 meaningful. Nothing measured here says coverage is
sufficient at any other carrier, at any other target, or for any candidate
family with a generator this census does not run; §5.1's dead list is the
record of what is not being claimed.

## 6. The walls

**L-1 — argued before any test, then declined.** L-1 records that order-level
covariance is a

> fourth form, outside paper 8's three**, and its admissibility is v11's to
> argue when U4 runs

The argument owed is prior to any test and it is this. Admissibility would
require a group declared to act on the generated causal order and a reason to
read that group as a covariance group. This arena supplies finite records and
a translation action on their *site lattice*; the corpus contains no bridge
from Z_3^2 translations to any boost, and this unit constructs none. **The
fourth form is not tested here.** The sentence retracted in 2026 is not
reproduced, and the gate that enforces its absence whitespace-normalises,
ASCII-folds and strips markdown prefixes from both sides, so a line-wrapped or
blockquoted injection dies too.

**BHS — no sprinkling-grade Lorentz-invariance test.** The reproduction
catalog records that

> a Poisson sprinkling admits **no Lorentz-invariant finite-valency graph**
> (BHS)

and these schedules are finite-valency by construction, so running the test
would manufacture a false negative. None is run — and the abstention is
measured rather than asserted. The gate scans this run's whole measurement
layer, every measured receipt key together with the statement and evidence of
every non-wall gate the run evaluated, for `boost`, `rapidity`, `sprinkl` and
`frame`, and finds none of them; its falsifier writes a sprinkling-grade boost
reading into that layer and dies there.

**Kleitman–Rothschild — every dimension reading carries a height control.**
The catalog's carry is that

> a dimension reading without a height control is worthless

and this unit takes no dimension reading at all: no chart width, no
Myrheim–Meyer estimate, no max-shatter dimension. The height control is
therefore not owed and not manufactured — and, as at the BHS wall, that is a
scan of the same measurement layer rather than a declaration: none of
`myrheim`, `meyer`, `shatter`, `chart width`, `dimension` or `height` occurs
in it, so there is no reading for a height control to be owed against.

**The diagonal — measured here, and read no further.** The (1,1) link is
populated by every saturating arrangement and is exactly what lifts the
determinant off zero; that is this unit's point. It is read as a direction on
a nine-site lattice and as nothing else. Cosmological readings stay barred and
no continuum claim is made anywhere in this unit — again measured on the same
surface, which contains none of `cosmolog`, `continuum`, `horizon`,
`redshift`, `universe` or `expansion`.

**The Lorentzian resonance, NAMED.** A reader arriving from the relativity
line will hear "signature" in a determinant that has just gone positive. The
naming sentence in §5.5 is mandatory and a gate requires it to be present:
silence is how a resonance becomes governance. The falsifier deletes the
sentence from the object under test, and the L-1 falsifier injects the
retracted sentence into it line-wrapped and blockquoted, so both wall gates
are exercised against the text they police rather than against a flag.

## 7. Choice inventory

| # | item | class | fiber | where it binds |
|---|---|---|---|---|
| 1 | the base object: CONFLICT-GRID(3, R) | **forced** | 1 | pin, from the committed constructor |
| 2 | the per-round budget: 3 groups of 3 | **forced** | 1 | the committed cycle, reproduced event for event |
| 3 | the site carrier: actors to Z_3^2 | **forced** | 1 | the constructor's own actor naming |
| 4 | admissibility: the layer's own menu | **forced** | 1 | d42b1 driven directly, no menu law re-typed |
| 5 | the I7 readout | **forced** | 1 | HA §3.2, matched verbatim and recomputed |
| 6 | R = 3 rather than R = 2 | **declared, VERDICT-DETERMINING** | 1 | the pin; the demand the U4b adjudication registered — the counterfactual is measured in-unit at §4.5, where the same pipeline returns I7-STRICT empty |
| 7 | the driven window W3 | **declared** | 1 | §2.3, disclosed in the head |
| 8 | the seed menu: two canonical transversals | **declared** | 1 | §2.3; the exhaustive columns do not use it |
| 9 | the reading axis (EMBEDDING / QUOTIENT) | **declared** | 2 | weld 2's, carried unchanged; every row stamped |
| 10 | `I-SITE-ASSIGNMENT` | **measured** | **1** | §5.4 |
| 11 | `I-DIRECTION-LABEL` | **measured** | **1** | §5.4 |
| 12 | `I-ORIENT` | **measured** | **1** | §5.4 |
| 13 | the fragility edits (re-seating, transposition) | **free** | — | this unit's; the minimal edit on each variable |
| 14 | the declared driven-crystal set (first 8) | **free** | — | this unit's; admissibility only, deterministic |

Two free items, both instrument-side, both deterministic, and neither of them
touching a verdict: item 13 sets the fragility column's edit, and its outcome
is a single cell at every object; item 14 chooses which crystals have their
edits driven, and every choice would return FORCED because all 1040 window
records and all 31 stratum witnesses do.

## 8. Verdict

```
R3-ARENA-UNIT-GRADE-[n=1 at 27 of 27; det=3/4 at 9 of 9; POSDEF 9 of 9; FORCED 1040 of 1040; FULL-GROUP REACHABLE 1680]@WINDOW-1040-OF-432081216000+31-STRATUM-WITNESSES
```

```
POSITIVE-GEOMETRY-[CEILING 9 ATTAINED at 72 of 21952000 GROUPING TRIPLES; 8 NEVER ATTAINED; I7-STRICT=POSDEF-9=FIELD-IDENTICALLY-1 (SITEWISE: POSDEF(x) IFF min_l n_l(x)>=1, AT ALL 64 REACHABLE SITE CODES); DET-SPECTRUM 9 VALUES ON 197568000 CELLS]
```

```
WELD3-FOUND-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT<ISOS=1296=|AUT(K333)||QUOTIENT-MAPS=1296|FIBERS=1/1/1(SITE/LABEL/ORIENT,BASE-MAP-INVARIANT)|INDUCED-RECORD=(1,1,1):q=[[1, -1/2], [-1/2, 1]]:det=3/4:ADMISSIBLE-BY-HA-SYLVESTER:INSIDE-I7'S-OWN-361-POINT-DECLARED-BOX:NOT-ONE-OF-ITS-11-DECLARED-RECORDS:THE-WELD-IS-TO-I7'S-RECORD-SPACE(WELD-2'S-OWN-FOUND-AT-I7-WITNESS-(2,2,2)-WAS-ADMISSIBLE-AND-UNDECLARED-TOO) -- SCOPE=THE-SATURATING-STRATUM(72-OF-21952000-GROUPING-TRIPLES-IN-THE-COMMITTED-NAMING;288-UP-TO-THE-SITE-ASSIGNMENT-THE-READING-DECLARES-FREE;STRATUM-WIDE-BY-THEOREM:ALL-72-CARRY-ONE-ARENA-IN-12-MULTISETS-EACH-WITNESSED)|GRAMMAR-ADMISSIBLE-NOT-COMMITTED(d66'S-OWN-R=3-POINT-SPENDS-27-INCIDENCES-ON-18-OF-27-CELLS-AND-IS-COUNT-DEAD)|COVERAGE-NOT-COUNT(46656-TRIPLES-PAY-THE-FULL-27;72-WELD;1-IN-648)|ROUTE-B-MOOTED-AT-THIS-TARGET-AND-CARRIER -- CONTROLS=FOUND-AT-CRYSTAL@L2(ISOS=72,FIBERS-ALL-1)|FALSIFIER-FLIPS(UNMOTIVATED,SITE-FIBER=6)|EMPTY-AT-WALK(ARITY-DEAD:2-OBJECTS-AGAINST-9)|CRYSTAL-AT-I7(STRUCT-DEAD:DIAGONAL-0-AT-9-OF-9)|R3-FALSIFIER(STRUCT-DEAD) -- READINGS-DIFFER=DEAD-ROWS-DIE-AT-STRUCTURE-UNDER-EMBEDDING-AND-AT-COUNT-POSITIVITY-UNDER-QUOTIENT|DIRECTED-COMPARATOR=0-AT-ALL-8-ARENAS|STRICTEST-READING(SITE-CARRIER-FIXED)=R3-SAT-SURVIVES-AT-n=1;R3-ROW|COL|ANT-DIES-AT-9-ZERO-CELLS>
```

Read out. The weld route's exact demand is met: a schedule the committed
grammar admits — driven, forced, one menu candidate per specification —
induces a positive definite I7 geometry record, and weld 2's detector, used
unchanged and controlled two ways, returns FOUND at both readings with zero
free items.

Three qualifications travel with it and none of them is optional. The
schedule is **grammar-admissible, not committed**: d66's own R = 3 point
alternates row and column, spends all 27 of its incidences on 18 of the 27
cells and is COUNT-DEAD; the saturating stratum is 72 grouping triples of
21,952,000 in the committed naming and 288 up to the site assignment the
reading itself declares free. The record it induces is **admissible but
undeclared**: inside I7's own 361-point box, outside its 11-record list — as
weld 2's own FOUND-at-I7 witness was, which is why the weld is to I7's record
space rather than to its list. And the geometry, unlike the crystal, is **not
a property of the whole schedule but only of its groupings** — untouched by
all 19,683 seed choices and destroyed by every one of the 5,832 minimal
grouping edits.

FOUND is not a property of the arrangement the effectus exhibited. All 72
I7-STRICT triples are driven and every one of them carries the identical
co-division arena, in 12 multisets each of which is given a driven witness, so
the verdict is **stratum-wide by theorem** rather than window-relative: the
rigidity theorem forces any I7-STRICT triple to realise exactly the target's
own Cayley incidence, and the detector cannot then return anything but FOUND.

**Route B is mooted at this target and this carrier — dominated, not
refuted.** Weld 2 priced a Route-B declaration at a site set, a direction
labelling, an orientation and a strictly positive diagonal count that no
committed crystal supplies. All four are supplied here by derivation from a
driven record, with the label and orientation fibers measured at 1 rather than
declared, so no successor buys the more expensive object at this target. Route
B stays live where this unit does not reach: I7's eleven declared records at
R = 3, the arity-dead carriers, and the committed constructions.

What has changed since weld 2 is precise. Weld 2 found no grammar record that
reaches FOUND at I7's target and had to exhibit that branch on a declared
probe. This unit exhibits it on a driven grammar record with the same 1296
site assignments the probe had — which is the target's own automorphism count
and is forced once the two readings meet at equality. The obstruction weld 2
measured was real and it was arithmetic; three rounds pay the **budget**, and
only the saturating groupings pay the **coverage**.

## 9. Deviations, priced

1. **The driven window is 1040 of 432,081,216,000.** Driving the family is
   not affordable at hundreds of milliseconds a record. Price: the FORCED
   reading is exhaustive on W3 and on 31 stratum witnesses, not on the family.
   Mitigation: the window contains the whole I7-STRICT stratum, the window is
   named in the arena verdict string, every other column is exhaustive over an
   object the window does not cap, and the driven-vs-combinatorial equality
   that licenses those columns is measured on all 1040 records.

2. **The seed menu inside the window is two canonical transversals per
   round.** Price: the driven slice contains no crystalline schedule, so the
   fragility column's *admissibility* leg is taken on a declared set — the
   first 8 crystalline schedules of the stratum enumeration and all 144 of
   their re-seatings — rather than on the window. The *stabilizer* half of the
   same column is exhaustive over all 1,417,176 schedules of the stratum.

3. **The U4b delivery artifacts are cited and not read.** A repair worker
   holds `paper-17` and `u4b_schedule_*` under rewrite, and rule #91 forbids
   reading a live worktree state. The cross-unit anchors are taken instead
   from the FROZEN U4b adjudication and effectus review at their pinned shas,
   and the R = 2 numbers this unit needs — ceiling 3, wall 6, I7-STRICT empty,
   747 non-degenerate pairs — are **recomputed here** rather than quoted, by
   the same machinery, and compared against the adjudication's own bytes.

4. **The crystal falsifier is a division-set edit, not a re-drive.** Weld 2
   built it by withholding one row-group arbitration during construction; at
   R = 2 that arbitration is the last of its group's rounds, so withholding it
   from the record and withholding it from the division set are the same
   object for a detector that consumes footprints. It is declared as a
   falsifier and not as a grammar record.

5. **`SMUGGLED = 0` is structural for census candidates**, as in weld 2, and
   the verdict carries that qualifier rather than reporting a zero that could
   not have been anything else.

6. **The coordinate-free class is this unit's, not the pin's.** The pin names
   the I7-STRICT stratum; the census of §4.4 measures the larger class the
   detector actually sees once the site assignment is used, and both numbers
   travel in the verdict. Reporting only 72 would have understated the weld's
   reach and hidden the site assignment's role.

7. **One arena, not seventy-two.** The weld census runs one detector call for
   the saturating stratum because all 72 driven arenas are byte-identical as
   relations. That identity is gated, not assumed.

8. **The off-tree leg, disclosed and now discharged.** The structural claim
   that this run is correct off-tree and with no version control present is
   sound by construction — every source path is resolved from the module's own
   location and never from the working directory, no subprocess is invoked,
   and the read set is gated — but an earlier off-tree execution of a
   pre-final code state failed on an accounting defect and was disclosed
   rather than repaired in place. The leg has since been executed twice, once
   by an external reviewer against the code state that reviewer held and once
   for this delivery: in a mirror holding only the pinned sources and the
   paper, with no version control anywhere on the path, on a hostile PATH and
   under a different hash seed. Both runs passed every gate and reproduced
   their delivered artifacts byte for byte. The leg is cited here rather than
   left in the ledger, because the paper is the citable artifact.

9. **The R = 4 register probe is this unit's, not the pin's, and it is
   combinatorial only.** §11 registers the successor question with a number on
   it — G-FLAT reached at 276 of the 1,679,616 ordered quadruples of
   saturating partitions — because a successor inheriting an open question
   should inherit its size. Price: no menu is driven at four rounds, so
   nothing there is claimed constructible, and the row is stamped
   REGISTERED-NOT-CLAIMED in the receipt as well as in §11.

## 10. The instrument

`v14/code/r3_weld_exact.py`, with the #82 CLI contract: a delivery run that is
the only writer, `--no-write`, `--numbers`, `--selftest`, `--mutant NAME`,
`--break-anchor NAME`, `--verify-paper [PATH]`, `--list-gates` and
`--list-mutants`; every unknown flag, unknown flag argument and missing flag
argument exits 2, and the registered permissive shape is present only as the
CLI gate's own falsifier.

Arithmetic is exact end to end: an AST scan of the file and a recursive type
scan of the emitted receipt are gates. Counts are computed, never typed.
Gates bind objects rather than aggregates: the constructibility, driven-field,
unit-grade, homogeneity, affine, fragility, rigidity, sitewise and census-row
gates each evaluate every object against its own invariant. Provenance is by
pinned sha with the products gated: 14 sources are read at run time, the set
of reads is required to be exactly the declared set, and no subprocess of any
kind is invoked, so the run is correct off-tree and with no version control
present. The verbatim anchors each clear a length floor and each name the gate
that consumes them, and each named gate is required to be in the declared
registry **and** in this run's own evaluated ledger, so the naming cannot
drift into a gate that was removed or never reached. Every text gate
whitespace-normalises, ASCII-folds **and strips markdown line prefixes**, so a
needle spanning a block quote or a numbered list cannot be evaded by
re-wrapping.

The four inherited walls are measurements rather than declarations. The two
that read the paper — the retracted L-1 sentence's absence and the naming
sentence's presence — carry falsifiers that edit the paper under test rather
than the gate's boolean. The three abstention walls scan this run's whole
measurement layer, every measured receipt key together with the statement and
evidence of every non-wall gate evaluated, for the terms whose presence would
mean the reading was taken.

The coverage ledger is honest: every gate is either falsified by a declared
mutant or waived with a forcing that says why it cannot fail, the denominator
is the gate count of the run rather than a hand-kept number, and every
declared falsifier is checked to reach its gate — with the gates that run
after the check named as declared-later and their presence verified at the
last gate rather than assumed. The mutant sweep's *execution* is bound and not
merely declared: a delivery-level run must carry one sweep row per declared
mutant, every row on target, and must have evaluated the sweep gate itself,
and the same conjunction is re-taken at the terminal integrity gate — so the
only writer in this file is downstream of a sweep that actually ran.

The seal is **total**: every published receipt key — the measured layer and
the vouching layer alike, schema, provenance, paper claims, coverage,
polarity, reachability, gates, totals and the transcript head — is either
sealed at the moment its gate passes or listed as DECLARED-UNSEALED, and the
completeness gate compares the manifest against the declared key set rather
than against the seals that happened to be taken. The unsealed declaration is
itself frozen by content and by length and may name no key that carries a
measurement, so the coherent drop — remove the seal row, remove the
declaration and declare the key unsealed — has no surface either. The
artifacts are written from the sealed payload through `os.replace`; the
terminal integrity gate compares the bytes on disk against the gate-time seal
after a deliberately corrupted probe has been shown to be detected; a run that
fails a gate writes nothing. The archived transcript therefore carries
G-SEAL-COMPLETE's row and not the integrity gate's, which is emitted after the
transcript string is serialized; that verdict is recorded by the artifacts'
existence instead.

The head is derived a second time by a comparator that shares neither code nor
input nor typed literal with the builder: it reads the serialized receipt,
**types all three verdict templates itself** — the weld segment included, which
carries the outcome word — and re-derives that word from the receipt's own
fate rows, cross-checked against the published fate multiset. A one-line
forgery of the builder's outcome word therefore moves the builder alone and
dies at the reconstruction gate. The paper under test is checked in the same
run for claim rendering, numeral coverage, head-verbatim rendering and claim
polarity. Numeral coverage now scans the **fenced verdict blocks**: the old
scan removed every backticked span before scanning and so never read the
head's numbers at all, and a fenced numeral is allow-listed only against the
receipt, the run's own verdict strings included. On top of that each of the
three derived segments is matched into the paper character for character, so
the blocks a reader will quote are bound to the receipt as strings and not
merely as numbers. The delivery run is byte-reproducible.

## 11. The successor register

Registered, not claimed.

**S-1 — the coupling unit, and the scope it must open with.** It inherits four
things by citation and re-derives none of them: the arena (the 72 I7-STRICT
grouping triples, 288 coordinate-free, all carrying one co-division arena);
the record `(1,1,1)` with its `q` and its determinant; the map (FOUND at both
readings, fibers 1/1/1, the count being the target's own automorphism number);
and the equality that explains all three — the realised relation **is** the
target's incidence, which is why the two readings agree and why a coupling
arena that does not reach equality will split them again. Two conditions bind
it. First, the welded record is **unsplittable**, split fiber 0 at all 27
intervals, so paper-04's refinement grammar, paper-06's stochastic split and
paper-09's renewal-transport kernel are empty on it: the coupling unit reaches
a record, not yet a law over records, and any coupling that needs a refinement
must first say which record it couples at. Second, every budget argument it
carries to another budget must be restated as a **coverage** argument — at
R = 2 the budget bound, at R = 3 it does not.

**S-2 — the R = 4 question, and it is the sharpest one this unit creates.** At
R = 3 the rigidity theorem makes `(1,1,1)` the only reachable I7-STRICT
record, so no R = 3 schedule can reach a declared record at all: the
undeclaredness is a budget fact and not a verdict about the grammar. One round
later the budget is 36 and I7's own `G-FLAT` = (1, 1, 2) needs exactly 36. The
combinatorial side is measured here and nothing more: over all 1,679,616
ordered quadruples of saturating partitions, G-FLAT's chart orbit is reached
at **276**. Nothing is driven, and constructibility at four rounds is neither
run nor claimed. The successor question is whether the committed grammar
drives one of the 276, with the seed and supply questions re-asked one round
wider. If it does, the second qualification dissolves into a budget statement
and the weld lands on declared corpus physics; if it does not, the
undeclaredness is promoted from an accident of R = 3 to a property of the
construction, which is the stronger result either way.

**S-3 — the 288 and the naming question with teeth.** The weld's own class is
288 and the difference from 72 is exactly the site assignment. Whether the 216
extra triples — whose groups run along the one direction I7 does not declare —
are *the same weld* or four welds related by a relabelling the corpus has
never declared is a naming question, and the corpus has a precedent for
treating those seriously rather than by fiat.

**S-4 — the eleven non-collinear multisets.** Of the 12 multisets exactly one
is the three parallel classes; the other 11 each contain conflict groups that
are not lines of AG(2,3). At the detector they are identical, and that is
gated. Whether they are identical *as processes* — record length, event count,
crystallinity profile — is open and cheap.

**S-5 — Route B, rescoped rather than retired.** Mooted at this target and
this carrier, per §8. It stays live for I7's eleven declared records at R = 3,
for the arity-dead carriers, and for the committed constructions; any future
Route-B pricing must now beat the derived price paid here, and weld 2's
dead-list rows stay cited and never re-run.

**S-6 — the instrument rows.** Two are registered against this unit's own
machinery. The #125 normaliser is complete against everything markdown can do
to a needle — line wrapping, block quotes, nested quotes, bullets, numbering,
bolding, back-ticking, table cells, headings, indentation, tabs, non-breaking
spaces, em-dash folding, curly apostrophes — and stops at the markdown layer:
zero-width characters, soft hyphens, interleaved inline HTML, HTML comments,
HTML entities, backslash escapes and footnote markers are outside it. That is
a corpus-wide instrument row rather than a defect of this unit, and it is
registered so the next unit that hardens `canon` does it once for everybody.
And the self-test's writes-nothing falsifier still sets its gate's boolean
rather than moving a writer, which is disclosed here rather than repaired,
because a falsifier that genuinely reached a writer would be a falsifier that
writes.

**S-7 — the second resonance, named before it is heard.** The Lorentzian
resonance is named in §5.5 and gated. The next one a reader will hear at
`q = [[1, -1/2], [-1/2, 1]]` is the hexagonal one: unit lengths meeting at one
hundred and twenty degrees. No such reading is taken here and the sweep is
clean,
so this is not a violation — it is a wall row the coupling unit should inherit
before it writes the word "triangular".

**What may not be inherited**, as a standing row: the schedule as a committed
object; count-sufficiency as a statement about counts; the fragility
invariances as measured independence; the 1,296 as three agreeing
measurements; the word "rare" as anything but a cardinality ratio over a
declared arena; and any dynamics, signature, dimension, cosmological or
continuum reading whatever.
