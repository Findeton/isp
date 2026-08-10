# WELD 2 — THE CARRIER CENSUS: what the transport grammar can and cannot send to the record lattice

**Status:** DELIVERED, awaiting adjudication. Every headline below is a
**CANDIDATE READING** until the panel has run.
**Pin:** `v14/note-weld2-census-pin.md` (`9d19515cb3ae`, ledger #85,
Route A), on the scout report of record
(`v14/note-weld2-referent-scout.md`, `e1f771a9d0ed`, #83).
**Artifacts:** `v14/code/w2_census_exact.py`, `w2_census_output.txt`,
`w2_census_receipt.json`. **32 gates, 0 failures; 7 numeric and 11
verbatim anchors, 0 failures; 3 waivers; 13 declared mutants, each
dying at its named gate; plain run byte-reproducible.** Exact
arithmetic (`fractions.Fraction` and integers) throughout; every number
printed here renders from the receipt.

---

## Abstract

The gravity line counts division events on the links of a record
lattice; the quantum line moves division events through a grammar. This
unit asks whether the second can supply the first: is there a
**motivated** map from the transport grammar's carrier to I7's spatial
record lattice — grammar objects to sites, object-pairs or channels to
links, sets of division events to link counts — where *motivated* means
zero free items at the RSQ standard?

The census is EMPTY, at both carriers, over the pin's declared
generator vocabulary: **60 candidates, 0 FOUND, 0 UNMOTIVATED, 0
SMUGGLED**, all 60 dying at measured type, arity or structure
obstructions. The obstruction is sharper than an absence. It is a pair
of scissors:

> **The one link generator that carries directed cycles at the
> transport carrier is the actor pair, and it has exactly 2 objects.
> Every link generator with 9 or more objects is acyclic. I7's lattice
> needs 9 sites *and* a 3-cycle on 3 distinct sites through every
> generator.**

Both blades are measured. The class-level event-extension graph carries
45 self-loops at MENU and 0 at CONG-185, and after their removal is
acyclic at both — 0 simple directed cycles at every length from 2 to 6,
and a completed topological sort on all 113 and all 185 vertices. The
(A,B) channel carries 336 division events in each direction and exactly
2 site objects.

The detector is two-way and both branches fire. On the committed
arbitration crystals — grammar records that provably carry a lattice —
the same machinery returns **FOUND**, with 72 site assignments all
giving one count field and every inventory fiber 1; withhold one
row-group arbitration and it returns **UNMOTIVATED** with the
site-assignment fiber measured at 6. On D58's generic 2-actor walk it
returns **EMPTY** by two independent falsifiers.

One measurement came back that neither the pin nor the scout
anticipated. Across the whole committed crystal family the axis link
counts are homogeneous and strictly positive, and the **diagonal link
count is identically zero at 9 of 9 sites in 5 of 5 crystals**. At
$d=2$ the diagonal count is exactly what fixes $q_{12}$. The corpus's
only lattice-carrying grammar records supply $q_{11}$ and $q_{22}$ and
never the cross term.

---

## 1. The question, and the standard it is asked at

I7's geometry record is count data on the corpus's own division
structure. The HA paper says so in the sentence this unit carries
verbatim:

> *"$n_\ell(x)$ is the number of division events in the record interval
> between $x$ and $x+\ell$"*

and v11 paper 0 fixes what a division event is:

> *"**[POSIT]** v11's **division events are the renewal events.**"*

Those two rows are the whole of the tie between the two lines. The
scout's sweep (#83, two independent agents) found the corpus pins **what
the counts count** and **nothing about where**, and returned
`NO-SEED-AT-THE-CARRIER`. This unit is the census that confirms,
refutes or scopes that reading, posed at the level BRG explicitly
declined (its §14 open 4).

**Motivated** is the RSQ standard, applied as R6b′ §9 applies it: every
construction choice is classed *declared*, *forced*, or *genuinely
free* with its fiber measured, and a candidate is motivated exactly
when it has **zero free items**.

**EMPTY is a statement about a declared family.** The generator
vocabulary of §3 is the family, declared as data before the census ran.

---

## 2. The arenas, declared as data

### 2.1 The deformation side — I7's arena

Read as data from the pinned HA receipt (`542b8735daf0`), not
re-authored:

| coordinate | value |
|---|---|
| sites | $X=(\mathbb Z_3)^2$, $\lvert X\rvert = 9$ |
| links | $\mathcal L = \{(1,0),\,(0,1),\,(1,1)\}$, $\lvert\mathcal L\rvert = 3$ |
| geometry record | $s$: $n_\ell(x)\in\mathbb Z_{>0}$ at each of the $9\times 3 = 27$ cells |
| record family | 11 declared records, **9** admissible by the exact Sylvester criterion, **6** splittable |
| unsplittable | `G-ANISO`, `G-CURVED`, `G-FLAT` (each carries a count-1 interval) |
| chart group | the $\lvert X\rvert$ translations and the $d!$ direction relabellings |

The readout is HA §3.2's invertible linear re-encoding: $q_{11}=n_{e_1}$,
$q_{22}=n_{e_2}$, $q_{12}=(n_{e_1+e_2}-n_{e_1}-n_{e_2})/2$. Record and
metric are one datum in two coordinate systems, which is why the
no-smuggling gate of §4.4 tests *which function* a candidate computes
rather than *what it can see*.

### 2.2 The grammar side — both carriers

The committed d42b1 transport grammar is rebuilt here from its
definitions; nothing is imported from another unit's code. At the
pinned scope — actor pool $(A,B)$, depth $\le 4$ — the family has
**3969 histories**.

**MENU** is the weighted-menu partition: **113 classes**. An
independent comparator — pairwise equality of menus as mappings
event $\to$ Fraction, sharing no key primitive with the builder —
returns 113.

**CONG-185 is re-derived here, not taken on faith.** Partition
refinement from the menu partition to a fixed point returns **185
classes in 5 rounds**, inside D74's declared 4–6 window; an independent
comparator — the coarsest bisimulation inside the menu partition, found
by explicit pair-splitting on the relation with no signature hashing —
returns 185. Its **six ruling properties are gated before use**:

| # | property | CONG-185 | MENU-113 (the contrast that makes it non-vacuous) |
|---|---|---|---|
| P1 | horizon potential descends at every horizon | **yes**, 0 non-constant classes at every horizon | **no** — $G(\cdot,2)$ takes more than one value on **4** classes |
| P2 | multi-valued labelled edges | **0 weights / 0 targets** | 0 weights / **4 targets** |
| P3 | the 44 curvature squares intact | **44** of 88 defective close; 44 non-unit self-loops $\{1/2{:}26,\,2{:}10,\,3/2{:}6,\,2/3{:}2\}$; obstruction **44**; 1362 of 1546 closed squares close | 44; 1402 of 1546 |
| P4 | $q$-holonomy | primes $\{2,3\}$, **rank 2** | $\{2,3\}$, rank 2 |
| P5 | $k$-holonomy | primes $\{2,3\}$, **rank 2** — collapses onto $q$ | $\{2,3,5,13\}$, rank 3 |
| P6 | exact lumpability | Chapman–Kolmogorov divides at **10 of 10** depth triples | **6 of 10** |

**Six of six hold. There is no derivation mismatch to report.** The
object used in the census below is the one re-derived here.

The square census that feeds P3–P5 reproduces independently:
**1546 closed exchange squares**, of which **88 defective** with
spectrum $\{1/2{:}70,\ 2{:}10,\ 3/2{:}6,\ 2/3{:}2\}$. The comparator
takes a different route entirely — it groups the generated family by
(prefix, unordered last-two events) and counts the groups of size two,
calling no admissibility predicate and doing no Fraction arithmetic —
and returns 1546.

### 2.3 The only motivated ingredient, isolated and gated

**The count semantics.** Every candidate must send a set of grammar
division events to the count register of a specific link.

**The division-event predicate is the arbitration tag**, and it is the
pinned convention rather than this unit's choice: R6b′ §3 records it
`SOURCE-FORCED` from three agreeing rows. Measured: every one of the
**1536** events the predicate selects carries the tag; the family
contains **20** distinct arbitration events of which **8** are pair
arbitrations, so S4's narrower sufficient condition would select a
strict subset. That sensitivity is disclosed, and the forced reading is
the one used.

**Additivity.** R6a's forced part is rebuilt from the pinned record
family: 6 splittable records $\times$ 3 declared split rules $\times$ 2
declared completions = **36 refinements**, and count additivity under
the induced dyadic subdivision holds at **972 of 972** constraints,
**0 violations**. An independent arithmetic comparator, multiplying out
the family cardinalities and sharing no construction with the builder,
gives 972.

---

## 3. The candidate family, declared as data

The pin's generator vocabulary, and the arity treatments the census
offers each cell:

- **site** $\leftarrow$ { ACTOR, MENU-CLASS, CONG-CLASS, EVENT-SUBSET, ULAM-PREFIX }
- **link** $\leftarrow$ { ACTOR-PAIR (delivery channel), EXTENSION-EDGE, COVER-PAIR }
- **count** $\leftarrow$ { division-event count on the chosen link object between two declared arbitration cuts }
- **arity treatment** $\leftarrow$ { NONE, DECLARED-RESTRICTION }

$5\times 3\times 1\times 2\times 2$ carriers $=$ **60 candidates**,
computed and not typed. Site arities as measured: ACTOR **2**,
MENU-CLASS **113**, CONG-CLASS **185**, EVENT-SUBSET $2^{20}$ =
**1 048 576**, ULAM-PREFIX **3969** (by depth: 1, 8, 60, 452, 3448 —
**no depth gives 9**).

A cell is **well-typed** exactly when a pinned, choice-free map carries
the link generator's endpoint type to the site generator's object
type: identity on actors; the event tuple's initiator (`op[1]`, present
in every event kind) for an event to an actor; the two quotient maps
for a history to a class; a history to its own division-event set; an
event to its singleton subset; a history to its Ulam address. There is
no pinned map from a class to an actor, from a single event to a class,
or from an Ulam address to an actor, and each such cell is a **measured
type obstruction with its own row**, never a skipped cell.

**The pre-registered dead list is cited and not re-run**: R6b′'s C1–C5
with free items 6/5/1/4/1, `BRG-EMPTY-AT-CARRIER`, GW1 §2's order-only
spatial instruments, v12's arena-free Γ objects, and the naive 9↔9
whose *"$L\ge 4$ is therefore a measured requirement"* is carried
verbatim. No candidate row re-derives any of them.

---

## 4. The controls, run first

HA §14 requirement 3 is carried verbatim and honoured:

> *"A predicate that cannot return its other value anywhere in the
> declared arena is not a measurement"*

### 4.1 The FOUND-side positive control — the crystal arena

Five crystals are rebuilt from their committed specs and every one is
**FORCED**: every event offered by the committed layer's own menu, every
specification matched by exactly one candidate (`maxhits = 1`), no
refusal anywhere.

| crystal | events | division events | $n_{e_1}$ | $n_{e_2}$ | $n_{e_1+e_2}$ |
|---|---|---|---|---|---|
| `DOUBLE-GRID(3,2)` | 72 | 18 | 2 at 9/9 | 2 at 9/9 | **0 at 9/9** |
| `DOUBLE-GRID(3,3)` | 96 | 24 | 3 at 9/9 | 3 at 9/9 | **0 at 9/9** |
| `CONFLICT-GRID(3,2)` | 30 | 6 | 1 at 9/9 | 1 at 9/9 | **0 at 9/9** |
| `CONFLICT-GRID(3,4)` | 66 | 12 | 2 at 9/9 | 2 at 9/9 | **0 at 9/9** |
| `D60-GRID(3,12)` | 46 | 1 | 0 at 9/9 | 0 at 9/9 | **0 at 9/9** |

On `DOUBLE-GRID(3,2)`, at the lattice the record itself carries
($\mathcal L = \{e_1,e_2\}$), the census machinery returns

> **FOUND** — 72 site assignments carry the record's co-division
> incidence onto the target's link structure, **all 72 give one and the
> same count field**, and the inventory is
> `I-SITE-ASSIGNMENT 1, I-DIRECTION-LABEL 1, I-ORIENT 1`: **zero free
> items**.

The record's own structure forces the reading; nothing is chosen. The
mechanism is homogeneity — every row group and every column group
carries the same number of arbitrations, so the whole isomorphism orbit
collapses to one field.

**The control can fail, and does on demand.** The declared falsifier is
the same crystal with one row-group arbitration withheld. The same
machinery returns **UNMOTIVATED**, with `I-SITE-ASSIGNMENT` fiber **6**
and `I-DIRECTION-LABEL` fiber **2** — two genuinely free items, measured.

### 4.2 The same crystal at I7's own lattice

Reported whichever way it lands. Against I7's declared **three**-link
lattice the same crystal returns **STRUCT-DEAD**: **0 of the $9!$
bijections** carry the site incidence onto the target's link structure,
because no committed crystal has any event whose register footprint
meets a diagonal pair. Row arbitrations touch a row, column
arbitrations touch a column, and the deliveries stay inside their
group.

This is the unit's unanticipated measurement, and it deserves its own
sentence. **Across the committed crystal family the diagonal link count
is identically zero at 9 of 9 sites in 5 of 5 crystals.** At $d=2$ the
diagonal count is exactly what fixes $q_{12}$. So even the corpus's
best lattice-carrying grammar records supply a *diagonal metric* and
never a cross term — they cannot express curvature in the off-diagonal
sector at all.

The crystal control therefore demonstrates the detector's FOUND branch
and **does not deliver a weld**; §7 prices that plainly.

### 4.3 The EMPTY-side negative control — the generic walk

D58's generic 2-actor walk (depth 30, seed 4242, its own committed
LCG): **30 events, 4 division events**. Against I7's declared lattice
the census returns **ARITY-DEAD** — 2 site objects against 9 — and
**ARITY-DEAD-BELOW** once the declared restriction is offered, because
a restriction can only shrink a site set. It carries a second,
independent falsifier: **0 of its 4 division events lie on the (A,B)
channel**, so its count register is empty as well.

**The control can return its other value**: the identical call on the
crystal record returns FOUND, so EMPTY at the walk is a property of the
walk and not of the plumbing.

### 4.4 The two classifier probes

**No-smuggling** (pin R6, sharpened). Since record and metric are one
datum in two coordinate systems, the test is which function of grammar
data a candidate computes: its count function is run against two
different declared I7 records, and a candidate whose counts move is
reading $s$ back. A declared probe whose count function reads I7's own
$s$ classifies **SMUGGLED = true**; a grammar-side probe classifies
**false**. The classifier is a measurement, not a label.

**Interior position** (pin R2). R6b′'s type census is carried verbatim
— *"the type census proves a leg has no interior division event for a
split to sit at"* — and the classifier is two-valued: a probe reading
that must place a division inside a leg classifies dead-on-arrival,
while the declared count generator does not, because it counts events
*on* a link object and never positions *inside* one. The probe cites
R6b′ C1's type verdict; it does not re-run C1.

---

## 5. The census

**60 candidates. 0 FOUND. 0 UNMOTIVATED. 0 SMUGGLED.**

| fate | total | @MENU | @CONG |
|---|---|---|---|
| TYPE-DEAD | 36 | 18 | 18 |
| ARITY-DEAD | 12 | 6 | 6 |
| ARITY-DEAD-BELOW | 2 | 1 | 1 |
| STRUCT-DEAD | 10 | 5 | 5 |
| FOUND / UNMOTIVATED / SMUGGLED / COUNT-DEAD | **0** | 0 | 0 |

The two carriers return identical fate distributions. The verdict is
carrier-stamped `@BOTH` for that reason, and not because the carriers
were assumed interchangeable: the link relations were built separately
on each carrier's own class graph.

**The full table** (identical at both carriers; `rep` is the arity
treatment):

| site | link | rep | arity | fate |
|---|---|---|---|---|
| ACTOR | ACTOR-PAIR | NONE | 2 | ARITY-DEAD |
| ACTOR | ACTOR-PAIR | RESTRICTION | 2 | ARITY-DEAD-BELOW |
| ACTOR | EXTENSION-EDGE | NONE / RESTRICTION | 2 | TYPE-DEAD $\times2$ |
| ACTOR | COVER-PAIR | NONE / RESTRICTION | 2 | TYPE-DEAD $\times2$ |
| MENU-CLASS | ACTOR-PAIR | NONE / RESTRICTION | 113 | TYPE-DEAD $\times2$ |
| MENU-CLASS | EXTENSION-EDGE | NONE | 113 | ARITY-DEAD |
| MENU-CLASS | EXTENSION-EDGE | RESTRICTION | 113 | **STRUCT-DEAD** |
| MENU-CLASS | COVER-PAIR | NONE / RESTRICTION | 113 | TYPE-DEAD $\times2$ |
| CONG-CLASS | ACTOR-PAIR | NONE / RESTRICTION | 185 | TYPE-DEAD $\times2$ |
| CONG-CLASS | EXTENSION-EDGE | NONE | 185 | ARITY-DEAD |
| CONG-CLASS | EXTENSION-EDGE | RESTRICTION | 185 | **STRUCT-DEAD** |
| CONG-CLASS | COVER-PAIR | NONE / RESTRICTION | 185 | TYPE-DEAD $\times2$ |
| EVENT-SUBSET | ACTOR-PAIR | NONE / RESTRICTION | 1 048 576 | TYPE-DEAD $\times2$ |
| EVENT-SUBSET | EXTENSION-EDGE | NONE | 1 048 576 | ARITY-DEAD |
| EVENT-SUBSET | EXTENSION-EDGE | RESTRICTION | 1 048 576 | **STRUCT-DEAD** |
| EVENT-SUBSET | COVER-PAIR | NONE | 1 048 576 | ARITY-DEAD |
| EVENT-SUBSET | COVER-PAIR | RESTRICTION | 1 048 576 | **STRUCT-DEAD** |
| ULAM-PREFIX | ACTOR-PAIR | NONE / RESTRICTION | 3969 | TYPE-DEAD $\times2$ |
| ULAM-PREFIX | EXTENSION-EDGE | NONE | 3969 | ARITY-DEAD |
| ULAM-PREFIX | EXTENSION-EDGE | RESTRICTION | 3969 | **STRUCT-DEAD** |
| ULAM-PREFIX | COVER-PAIR | NONE / RESTRICTION | 3969 | TYPE-DEAD $\times2$ |

### 5.1 The mechanism: the arity–cyclicity scissors

Every `STRUCT-DEAD` above is decided by one exact fact, and it needs no
enumeration.

I7's lattice is $\mathbb Z_3$-periodic: **every generator closes a
3-cycle on 3 distinct sites** ($3$ is prime and every declared link
displacement is non-zero). An embedding must carry those cycles into
the candidate's link relation. So a link relation with **no directed
cycle on distinct vertices** admits no embedding — at any size, over
every subset at once. That decides all $\binom{113}{9}$,
$\binom{185}{9}$, $\binom{2^{20}}{9}$ and $\binom{3969}{9}$
restrictions in one step, with no sampling and no cap.

Measured, on both blades:

| link generator | site objects available | directed cycle on distinct vertices? |
|---|---|---|
| ACTOR-PAIR | **2** | **yes** — $A\to B$ (336 division events) and $B\to A$ (336) |
| EXTENSION-EDGE @MENU | 113 | **no** — 45 self-loops; acyclic after their removal; 0 simple cycles at lengths 2–6 |
| EXTENSION-EDGE @CONG | 185 | **no** — 0 self-loops; acyclic outright; 0 simple cycles at lengths 2–6 |
| EXTENSION-EDGE on subsets / addresses | $2^{20}$ / 3969 | **no** — graded by cardinality and by address length |
| COVER-PAIR on singleton subsets | $2^{20}$ | **no** — graded by poset height |
| COVER-PAIR at the carrier | — | not posed: the carrier is a family, not a record, so the event poset's cover relation has no family-level referent (TYPE-DEAD) |

The acyclicity of the class graphs is measured two ways: a completed
topological sort on all 113 and all 185 vertices after self-loop
removal, and an independent comparator that enumerates simple directed
cycles up to length 6 and finds none. **A self-loop is not a generator
cycle** — the declared link displacements are non-zero, so a site never
maps to itself in one step.

The scissors close like this. The grammar *does* have a cyclic
structure: two actors talking to each other, with 336 division events
on each direction of the channel. It has no shortage of *objects*:
185 congruence classes, 3969 addresses, a million event subsets. What
it does not have is both at once. **Its cycles live where it has two
objects, and its objects live where it has no cycles.**

That is why the crystals work and the transport carrier does not. A
crystal has nine actors, so its one cyclic generator has nine objects.
The transport carrier has two.

---

## 6. The choice inventory

`MOTIVATED` $\iff$ zero free items. The three items the pin
pre-registered are the ones the census measures, and their fibers are
computed as the number of **distinct count fields** the choice produces
— not as the number of choices, which would over-count symmetries the
reading does not see.

| item | crystal (FOUND) | crystal falsifier | census candidates |
|---|---|---|---|
| `I-SITE-ASSIGNMENT` | **1** (72 isomorphisms, one field) | **6** | not reached — no candidate survives to the inventory |
| `I-DIRECTION-LABEL` | **1** | **2** | not reached |
| `I-ORIENT` | **1** | 1 | not reached |
| **free items** | **0** → FOUND | **2** → UNMOTIVATED | — |

Two further items are **declared**, not free, and are stamped into the
verdict with their sensitivity disclosed:

- **the window.** The count generator's own wording is *"between two
  declared arbitration cuts"*; the declared window is first-to-last
  arbitration cut, and it appears in the verdict string. Disclosed:
  sub-windows of `DOUBLE-GRID(3,2)` give $s\equiv 1$ where the full
  window gives $s\equiv 2$, so the window moves the record it produces
  while leaving the map's structure fixed.
- **the division predicate.** Forced to the arbitration tag by R6b′ §3;
  S4's pair-arbitration reading would select 8 of the 20 distinct
  arbitrations, and that is disclosed rather than adopted.

Nothing in the census reaches the inventory, because nothing survives
the type, arity and structure gates. **The EMPTY is structural, not a
matter of accumulated freedom.** That is a stronger negative than the
five UNMOTIVATED identifications R6b′ recorded: those failed at the
choice standard; these fail before a choice can be made.

---

## 7. The verdict

> **`WELD2-EMPTY-AT-THE-DECLARED-FAMILY-THE-ARITY-CYCLICITY-SCISSORS@BOTH:MENU-113+CONG-185`**
> `<CANDIDATES=60|FOUND=0|SMUGGLED=0|UNMOTIVATED=0|TYPE-DEAD=36|ARITY-DEAD=12|ARITY-DEAD-BELOW=2|STRUCT-DEAD=10`
> ` -- MECHANISM=THE-ONLY-CYCLIC-LINK-GENERATOR-HAS-2-OBJECTS(336-DIVISION-EVENTS-ON-THE-(A,B)-CHANNEL)-AND-EVERY-LINK-GENERATOR-WITH-9-OR-MORE-IS-ACYCLIC(MENU-SELFLOOPS=45|CONG-SELFLOOPS=0|SIMPLE-CYCLES-LEN-2..6=0-AT-BOTH)`
> ` -- CONTROLS=FOUND-AT-CRYSTAL(FOUND-candidate,ISOS=72,FIBERS-ALL-1)|FALSIFIER-FLIPS(UNMOTIVATED,I-SITE-ASSIGNMENT-FIBER=6)|EMPTY-AT-WALK(ARITY-DEAD)|CRYSTAL-AT-I7(STRUCT-DEAD)`
> ` -- INGREDIENT=COUNT-SEMANTICS-INTACT(ADDITIVITY-972-OF-972|DIVISION=ARBITRATION-TAG-FORCED)`
> ` -- CARRIER-RE-DERIVATION=CONG-185-SIX-OF-SIX`
> ` -- SCOPE=(A,B)-D<=4-CARRIER|I7-d2-L3-9-SITES-3-LINKS|DECLARED-WINDOW=FIRST-TO-LAST-ARBITRATION-CUT>`

The scout's `NO-SEED-AT-THE-CARRIER` is **confirmed and sharpened**.
The census does not find that the grammar is geometry-blind; it finds
exactly which two properties the transport carrier fails to hold
simultaneously, and it exhibits a grammar arena — the arbitration
crystals — where they *are* held simultaneously and the detector fires.

**Between delivery and adjudication this is a candidate reading.**

---

## 8. Deviations, priced

1. **The crystal control fires at the lattice the record carries, not
   at I7's.** The positive control runs at $\mathcal L=\{e_1,e_2\}$;
   against I7's three-link lattice the same crystal is STRUCT-DEAD. The
   control's job is to show the FOUND branch is reachable by this
   machinery, and it does that; it is **not** a weld and no verdict
   segment treats it as one. The crystal's own disqualification as a
   seed is cited from the scout, not re-derived: its actor arrangement
   is a declared blueprint, its direction set is a construction choice
   (d47 pin §3), and the transfer runs through paper 29's named missing
   map.

2. **Two site generators are not materialised at full arity.**
   EVENT-SUBSET ($2^{20}$) and ULAM-PREFIX (3969) are decided by a
   **grading theorem** — the subset-extension relation is graded by
   cardinality, the prefix relation by address length, the cover
   relation by poset height, so all three are acyclic by an identity of
   the definition. That is exact and covers every subset at once. It is
   an argument, not an enumeration, and it is marked as such in the
   receipt's waiver census.

3. **Scope.** The carrier is $(A,B)$ at depth $\le 4$; I7 is read at
   $d=2$, $L=3$. Deeper carriers ($(A,B)$ $d\le5$: 265 MENU / 462 CONG
   classes) and wider actor pools are not run. The scissors argument is
   a statement about *this* carrier; §9 registers the test that would
   move it.

4. **The window and the division predicate are declared**, with their
   sensitivities disclosed in §6 rather than folded into the free-item
   count. A reader who classes either as free reads the same census
   with the same fates, since no candidate reaches the inventory.

5. **The scout note of record was amended after the pin froze.** Ledger
   #89 added an addendum ("**No reversal — every verdict stands**";
   three further register hits, all binned to existing rows). This unit
   reads the pinned bytes at commit `95c3b77`. Two of the 24 pinned
   sources carry different working-tree bytes — the repo has live
   concurrent writers, and `paper-12-gamma-main.md` is mid-repair — and
   both are read through `git show 95c3b77:` rather than from mutable
   worktree state. The routes are recorded per file in the receipt.

6. **Disclosed because it was measured**: at this scope the *unweighted*
   partition — on the event set alone, ignoring the weights — also
   returns 113 classes. The carrier is the coarser object it looks
   like, and the weights add no refinement here.

7. **`D60-GRID(3,12)` carries one division event**, so its count field
   is zero on every link. It is reported in the crystal table rather
   than dropped: the delivery grid is a delivery crystal, not a
   division crystal, and the distinction is exactly what U4 is about.

---

## 9. The successor register

Registered, not claimed.

- **U4 — the renewal-only crystal.** v11 paper 0 §7: *"the division
  events of a crystal form a crystal"*. Rebuilding the crystals with
  renewal-only records makes the renewal sublattice the **generated**
  carrier of this unit's FOUND control, rather than a lattice read off
  a declared actor blueprint. It is pinned and never run. It is the
  strongest available form of the positive control and the natural
  successor to this unit.

- **The diagonal question — the sharpest new one.** Does *any* grammar
  record supply a co-division incidence on a diagonal pair? Measured
  across the committed crystal family: no, at 9 of 9 sites in 5 of 5.
  A construction that did would be the first grammar-side $q_{12}$, and
  the first record able to carry off-diagonal curvature. This unit
  found the question; it did not answer it.

- **The scissors test.** Both blades are properties of the declared
  scope. Two experiments would move the verdict rather than repeat it:
  (i) does the class-extension graph acquire directed cycles on
  distinct vertices at depth $\ge 5$, where classes span more depths?
  (ii) does a transport carrier over $\ge 9$ actors — which the
  crystals show the layer supports — give the cyclic generator enough
  objects? A positive answer to (ii) is the first place a motivated
  weld could exist, and it is posable now.

- **Route B remains the user's call.** Declaring the map (site ←
  actor, link ← delivery channel, $n_\ell$ ← division-event count on
  that channel) and naming it a declaration in the verdict string
  remains available at the price the scout priced it: every downstream
  QFT-rung result inherits `DECLARATION-RELATIVE`, permanently. This
  census does not foreclose it; it establishes what a *derivation*
  would have to supply.

- **Carrier-relativity.** The two carriers returned identical fates
  here, so this unit adds no evidence either way to the Γ-main
  adjudication's carrier-relativity open. That silence is a result and
  is recorded as one.

---

## 10. The receipt

`v14/code/w2_census_exact.py` — one self-contained program.
`--selftest` corrupts each of the 18 anchors individually in memory,
confirms all 18 would fail the run, exercises the real exit path with
an injected failure and confirms it returns 1, and writes nothing;
0 vacuous anchors. `--mutant NAME` runs any of **13 declared mutants**,
each of which dies at its named gate with artifacts untouched.
`--list-mutants` prints the registry. Unknown flags exit 2. The plain
run writes `w2_census_output.txt` and `w2_census_receipt.json` and is
**byte-reproducible** — run twice, verified identical.

Every verdict-bearing number carries a comparator built from
primitives its builder does not share: the menu partition by mapping
equality against frozenset keys; the congruence by relation-splitting
bisimulation against signature refinement; the square census by
family grouping against admissibility pairs; the acyclicity by
enumerated simple cycles against topological sort; additivity by family
arithmetic against the refinement construction.

11 verbatim anchors bind the quotations in this paper to their pinned
bytes, each named to the gate that consumes it, and each falsified by a
mutant. 3 waivers are declared, all of class DECLARATION-CARRIED or
REGISTER-ONLY, and all named in the receipt's waiver census.
