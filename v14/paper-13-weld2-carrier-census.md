# WELD 2 — THE CARRIER CENSUS: what the transport grammar can and cannot send to the record lattice

**Status:** DELIVERED, awaiting adjudication. Every headline below is a
**CANDIDATE READING** until the panel has run.
**Pin:** `v14/note-weld2-census-pin.md` (`9d19515cb3ae`, ledger #85,
Route A), on the scout report of record
(`v14/note-weld2-referent-scout.md`, `e1f771a9d0ed`, #83).
**Artifacts:** `v14/code/w2_census_exact.py`, `w2_census_output.txt`,
`w2_census_receipt.json`. **47 gates, 0 failures; 14 numeric and 12
verbatim anchors, 0 failures; 4 waivers; 43 declared mutants, each dying
at its named gate with the artifacts untouched; plain run
byte-reproducible.** Exact arithmetic (`fractions.Fraction` and
integers) throughout; every number printed here renders from the
receipt, and the run itself checks that it does.

---

## Abstract

The gravity line counts division events on the links of a record
lattice; the quantum line moves division events through a grammar. This
unit asks whether the second can supply the first: is there a
**motivated** map from the transport grammar's carrier to I7's spatial
record lattice — grammar objects to sites, object-pairs or channels to
links, sets of division events to link counts — where *motivated* means
zero free items at the RSQ standard?

The pin's word is **map**, and a map admits two readings. Both are run.
Under the **embedding** reading a candidate is a bijection from site
objects to sites whose link relation contains the target's incidence;
under the **quotient** reading it is a surjection of realised grammar
objects onto the sites carrying every realised edge to a declared link
displacement. The census is **EMPTY under both**: **120 rows, 60
distinct candidates, 0 FOUND, 0 SMUGGLED**. What differs is *where* the
candidates die, and the difference is the result.

**Under the embedding reading** all 60 rows die at measured type, arity
or structure obstructions, and the structural half is a **theorem**.
Every extension edge raises history length by exactly one — 3968 of
3968, no exceptions — so a length-homogeneous quotient's class graph is
*graded*: acyclic, and bipartite, and therefore carrying no odd cycle.
I7's lattice closes a 3-cycle on 3 distinct sites at 27 of 27 of its
cells. An odd cycle embeds in no bipartite relation, so no restriction
of any size can embed, at any arity, with no enumeration. CONG-185 is
length-homogeneous (0 classes span more than one length) and its blade
is that theorem outright. MENU-113 is not: 45 of its classes span more
than one length, and those are *exactly* its 45 self-loop classes — so
its blade is measured instead, and the declared restriction is
**executed rather than argued**: a complete induced-subgraph search
finds **0 of the $\binom{113}{9}$** restrictions inducing the target,
and 0 of the $\binom{185}{9}$. The other blade is arity: the only link
generator carrying a target-type cycle at this carrier is the actor
pair, and it has exactly 2 site objects.

**Under the quotient reading** acyclicity is no obstruction and the
cells are decided elsewhere. MENU **dies exactly**, with no search: each
of its 45 self-loops demands the zero displacement, and no declared link
displacement is zero, so those domains empty on node consistency alone;
the realised division-event-subset graph dies the same way, 8 rows in
all. CONG **survives** the existence question — a quotient map exists —
and the best of 40 declared solutions leaves 8 of its 27 count cells at
zero. And the Ulam-prefix quotient reaches a **strictly positive count
field at 27 of 27 cells** and dies at the choice standard, with a
site-assignment fiber of 40 — so the three free items the pin
pre-registered *are* reached under this reading, and 8 rows come back
**UNMOTIVATED**. Zero-free-items is never attained; EMPTY stands, and it
now stands for the right reason at every cell.

The detector is two-way and every branch fires. On the committed
arbitration crystals — grammar records that provably carry a lattice —
the same machinery returns **FOUND**, with 72 site assignments all
giving one count field and every inventory fiber 1; withhold one
row-group arbitration and it returns **UNMOTIVATED** with the
site-assignment fiber measured at 6. On D58's generic 2-actor walk it
returns **EMPTY** by two independent falsifiers. At the target the
census actually judges — I7's three-link lattice — no committed grammar
record reaches FOUND at all, and the FOUND branch is exhibited there on
a **declared probe** over the full arena of 15552 configurations.

One measurement came back that neither the pin nor the scout
anticipated. Across the four committed **arbitration** crystals the axis
link counts are homogeneous and strictly positive, and the **diagonal
link count is identically zero at 9 of 9 sites in 5 of 5 crystals**. At
$d=2$ the diagonal count is exactly what fixes $q_{12}$. Pushed through
HA §3.2's own readout this gives $q_{12}=-k$ and hence
$\det = 0$ at every site of every crystal: **no committed crystal
induces an admissible I7 record at all**. The corpus's only
lattice-carrying grammar records supply $q_{11}$ and $q_{22}$ and never
the cross term.

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

### 1.1 The two readings of "a map", declared as an axis

The pin's question (R1) asks for *"a map sending grammar objects to
sites, grammar object-pairs/channels to links, and sets of division
events to link counts."* Nothing in that sentence fixes the direction of
the map or requires injectivity. Two readings are therefore admissible,
and this unit runs both and stamps every row with the one it was decided
under:

| reading | a candidate is | what decides it |
|---|---|---|
| **EMBEDDING** | a bijection from site objects to sites under which the grammar's link relation **contains** the target's incidence | type, arity, and the odd-cycle structure of the link relation |
| **QUOTIENT** | a **surjection** of the realised grammar objects **onto** the sites, every realised edge carrying a declared link displacement | type, arity from below, the map's existence, count positivity, and the choice inventory |

The reading axis is **not the pin's**; it is declared by this unit, and
the verdict string says so. It costs nothing and buys the census its
own scope: a cell that dies under both readings dies for a
reading-independent reason, and a cell that dies only under one is
labelled as such.

### 1.2 One admissibility criterion, on both branches

A link of the target is an **unordered** site pair carrying a label and
a count — orientation is one of the pin's own pre-registered free items
(`I-ORIENT`) — so incidence is undirected, and it is undirected on the
kill side and the admit side alike. That matters, and it is measured:
co-division incidence is symmetric by construction while the target's
directed Cayley relation is antisymmetric, so a *directed* admissibility
criterion returns **0** isomorphisms at the very arena where the
undirected one returns **72**. Adopting the directed reading as the
criterion would make the FOUND branch unreachable in principle at every
co-division arena, which is exactly what HA §14 requirement 3 forbids.
The kill is therefore stated as an odd-cycle argument at the same notion
of incidence the admit test uses, and the directed acyclicity result is
carried as a comparator rather than as the criterion.

---

## 2. The arenas, declared as data

### 2.1 The deformation side — I7's arena

Read as data from the pinned HA receipt (`542b8735daf0`) — consumed
through the pinned-sha reader at the digest the provenance row records,
never from mutable worktree state — and not re-authored:

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

Measured on the target itself, because both readings lean on it: every
one of the **27** (site, link) cells closes a 3-cycle on **3** distinct
sites. Three is prime and no declared displacement is zero.

### 2.2 The grammar side — both quotients

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
| P2 | multi-valued labelled edges | **0 weights / 0 targets** | 0 weights / **4** targets |
| P3 | the 44 curvature squares intact | **44** of 88 defective close; 44 non-unit self-loops $\{1/2{:}26,\,2{:}10,\,3/2{:}6,\,2/3{:}2\}$; obstruction **44**; 1362 of 1546 closed squares close | 44; 1402 of 1546 |
| P4 | $q$-holonomy | primes $\{2,3\}$, **rank 2** | $\{2,3\}$, rank 2 |
| P5 | $k$-holonomy | primes $\{2,3\}$, **rank 2** — collapses onto $q$ | $\{2,3,5,13\}$, rank 3 |
| P6 | exact lumpability | Chapman–Kolmogorov divides at **10 of 10** depth triples | **6 of 10** |

**Six of six hold. There is no derivation mismatch to report.** The
object used in the census below is the one re-derived here. Both columns
of every row are computed, the MENU $q$-reading included.

The square census that feeds P3–P5 reproduces independently:
**1546 closed exchange squares**, of which **88 defective** with
spectrum $\{1/2{:}70,\ 2{:}10,\ 3/2{:}6,\ 2/3{:}2\}$. The comparator
takes a different route entirely — it groups the generated family by
(prefix, unordered last-two events) and counts the groups of size two,
calling no admissibility predicate and doing no Fraction arithmetic —
and returns 1546.

### 2.3 The realised objects, and the grading forcing checked

Three of the site generators are decided under the embedding reading by
a grading *theorem* rather than by enumeration, and the quotient reading
maps the same objects onto the sites. The theorem's hypothesis — that
the grading rises by exactly one along every edge — is a fact about the
realised relation, so it is checked edge by edge rather than assumed:

| generator | realised objects | realised edges | grading | exceptions |
|---|---|---|---|---|
| MENU-CLASS $\times$ EXTENSION-EDGE | 113 | 243 | history length | **45** classes span more than one length |
| CONG-CLASS $\times$ EXTENSION-EDGE | 185 | 376 | history length | **0** |
| EVENT-SUBSET $\times$ EXTENSION-EDGE | **25** | 41 | Boolean-lattice cardinality | **0** |
| ULAM-PREFIX $\times$ EXTENSION-EDGE | 3969 | 3968 | address length | **0** |
| EVENT-SUBSET $\times$ COVER-PAIR | **0** | 0 | — | — |

Reported against interest: the poset **height** grading is *not* strict
— **384** of the family's **10566** covers raise height by more than
one — so the cover row's structural basis is not a grading argument at
all. It is a measurement: **0** of those 10566 covers join two division
events, so the relation on singleton division-event subsets is empty.

The realised counts also retire two arguments the delivered census made
by grading alone. EVENT-SUBSET realises **25** objects against a
declared arity of $2^{20}$, and ULAM-PREFIX realises all 3969; both are
acyclic when materialised, so the fates are unchanged and now measured.
And the one cell the census types out can be materialised too: the
family-wide cover relation pushed to initiators has **2** objects and is
cyclic, which is the actor-pair blade again.

### 2.4 The only motivated ingredient, isolated and gated

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
**0 violations**. The comparator does not re-multiply the builder's own
loop bounds: it re-derives admissibility and splittability from the
record family by its own inline Sylvester test on the $q$-encoding and
counts the cells a refinement of each surviving record would carry,
giving 972; and the constraint cells actually compared inside the census
are counted as a *set of keys* rather than as a product, giving 972.

---

## 3. The candidate family, declared as data

The pin's three generator axes, plus the arity treatment the census
offers each cell and the admissibility reading this unit declares:

- **site** $\leftarrow$ { ACTOR, MENU-CLASS, CONG-CLASS, EVENT-SUBSET, ULAM-PREFIX }
- **link** $\leftarrow$ { ACTOR-PAIR (delivery channel), EXTENSION-EDGE, COVER-PAIR }
- **count** $\leftarrow$ { division-event count on the chosen link object between two declared arbitration cuts }
- **arity treatment** $\leftarrow$ { NONE, DECLARED-RESTRICTION }
- **reading** $\leftarrow$ { EMBEDDING, QUOTIENT } *(declared by this unit, not by the pin)*

$5\times 3\times 1\times 2\times 2$ readings $=$ **60 distinct
candidates**, each stamped at both quotients for **120 rows** —
computed and not typed. Site arities as measured: ACTOR **2**,
MENU-CLASS **113**, CONG-CLASS **185**, EVENT-SUBSET $2^{20}$ =
**1 048 576**, ULAM-PREFIX **3969** (by depth: 1, 8, 60, 452, 3448 —
**no depth gives 9**). EVENT-SUBSET is instantiated as the subsets of
the **20** distinct *division* events the family realises, not of the
**76** distinct events of any kind it realises, nor of the **124** its
menus offer (of which **44** are division events). The narrowing is
harmless to every fate, since the cardinality grading is strict for any
Boolean lattice, and it is stated rather than left to the arity.

A cell is **well-typed** exactly when a pinned, choice-free map carries
the link generator's endpoint type to the site generator's object type:
identity on actors; the event tuple's initiator (`op[1]`, present
in every event kind) for an event to an actor; the two quotient maps
for a history to a class; a history to its own division-event set; an
event to its singleton subset; a history to its Ulam address. There is
no pinned map from a class to an actor, from a single event to a class,
or from an Ulam address to an actor, and each such cell is a **measured
type obstruction with its own row**, never a skipped cell. The type
question is the same in either direction of the map, so it fires
identically under both readings: 36 rows under each.

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

Every value the detector can return is exhibited in the run — FOUND on a
grammar record, FOUND at the census's own target on a declared probe,
UNMOTIVATED on the declared falsifier, ARITY-DEAD on the walk, and
STRUCT-DEAD on the crystal at I7 — so the requirement is discharged with
measurements rather than with a declaration.

### 4.1 The FOUND-side positive control — the crystal arena

Five crystals are rebuilt from their committed specs and every one is
**FORCED**: every event offered by the committed layer's own menu, every
specification matched by exactly one candidate (`maxhits = 1`), no
refusal anywhere.

| crystal | events | division events | $n_{e_1}$ | $n_{e_2}$ | $n_{e_1+e_2}$ | induced $\det$ |
|---|---|---|---|---|---|---|
| `DOUBLE-GRID(3,2)` | 72 | 18 | 2 at 9/9 | 2 at 9/9 | **0 at 9/9** | 0 |
| `DOUBLE-GRID(3,3)` | 96 | 24 | 3 at 9/9 | 3 at 9/9 | **0 at 9/9** | 0 |
| `CONFLICT-GRID(3,2)` | 30 | 6 | 1 at 9/9 | 1 at 9/9 | **0 at 9/9** | 0 |
| `CONFLICT-GRID(3,4)` | 66 | 12 | 2 at 9/9 | 2 at 9/9 | **0 at 9/9** | 0 |
| `D60-GRID(3,12)` | 46 | 1 | 0 at 9/9 | 0 at 9/9 | **0 at 9/9** | 0 |

On `DOUBLE-GRID(3,2)`, at the lattice the record itself carries
($\mathcal L = \{e_1,e_2\}$), the census machinery returns

> **FOUND** — 72 site assignments carry the record's co-division
> incidence onto the target's link structure, **all 72 give one and the
> same count field**, and the inventory is
> `I-SITE-ASSIGNMENT 1, I-DIRECTION-LABEL 1, I-ORIENT 1`: **zero free
> items**.

The record's own structure forces the reading; nothing *the reading
sees* is chosen. The mechanism is homogeneity — every row group and
every column group carries the same number of arbitrations, so the
whole isomorphism orbit collapses to one field.

**The control can fail, and does on demand.** The declared falsifier is
the same crystal with one row-group arbitration withheld. The same
machinery returns **UNMOTIVATED**, with `I-SITE-ASSIGNMENT` fiber **6**
and `I-DIRECTION-LABEL` fiber **2** — two genuinely free items, measured.

**The control's arena of choices is smaller than the census's, and the
gap is priced.** At the crystal-carried 2-link target the inventory
ranges over $72\times 2\times 2 = 288$ configurations; at I7's 3-link
target it would have to range over $1296\times 6\times 2 = 15552$. So
`I-DIRECTION-LABEL = 1` at the control means *"the 2 label permutations
give one field"*, where at the census target it would have to mean *"the
6 do"*.

**And the pin's own named generator never fires.** Pin R5 names the
crystal control's mechanism as the record's own **cover structure**
forcing the lattice. Measured and reported whichever way it lands: that
generator returns STRUCT-DEAD at the 2-link target *and* at I7's. The
delivered control substitutes co-division incidence on the ordered
actor pair for it. The substitution is defensible — it is what the
crystal actually carries — and it is disclosed here rather than left
silent.

### 4.2 The same crystal at I7's own lattice, and the FOUND branch there

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
diagonal count is exactly what fixes $q_{12}$. Push the measured counts
through HA §3.2's own readout: with homogeneous axis counts $k$ and
diagonal 0 the readout gives $q_{12}=-k$, hence
$\det = q_{11}q_{22}-q_{12}^2 = k^2-k^2 = 0$ at **every site of every
crystal**. So **0 of the 5** committed crystals induce an admissible I7
record by the exact Sylvester criterion this unit applies to I7's own
family — a third and independent route to the same STRUCT-DEAD, reached
from the metric side rather than the graph side, and one in which the
failure is *exactly degenerate* rather than merely negative.

So the corpus's best lattice-carrying grammar records supply a
*diagonal metric* and never a cross term — they **do not** express
curvature in the off-diagonal sector, and the cause is the crystals'
declared row/column blueprint (d47 pin §3), which is a construction
choice and not a law of grammar records.

Because no committed grammar record reaches FOUND at the target the
census actually judges, the two-way requirement is discharged there by a
**declared probe**: nine probe objects carrying the target's own Cayley
incidence with a homogeneous count field. It returns **FOUND** at I7's
lattice with **1296** site assignments and every fiber 1, over the full
**15552**-configuration arena. It is not a grammar record, it is not a
weld, and it licenses exactly one thing — that the predicate *can*
return FOUND at this target, at this arena — in the same way the
smuggling classifier's grammar-side probe licenses only reachability.
What is absent is not the branch. It is a grammar record that reaches
it.

### 4.3 The EMPTY-side negative control — the generic walk

D58's generic 2-actor walk (depth 30, seed 4242, its own committed
LCG): **30 events, 4 division events**. Against I7's declared lattice
the census returns **ARITY-DEAD** — 2 site objects against 9 — and
**ARITY-DEAD-BELOW** once the declared restriction is offered, because
a restriction can only shrink a site set. It carries a second,
independent falsifier: **0 of its 4 division events lie on the (A,B)
channel**, so its count register is empty as well.

**The control can return its other value**: the same call with the arena
**and the target** replaced — the crystal record at the lattice that
record carries — returns FOUND. Two coordinates change there, not one,
so the conclusion is licensed by the walk's own fate rather than by the
flip: the walk dies on 2 site objects against 9, which is a property of
the walk and not of the plumbing.

### 4.4 The two classifier probes

**No-smuggling** (pin R6, sharpened). Since record and metric are one
datum in two coordinate systems, the test is which function of grammar
data a candidate computes: its count function is run against two
different declared I7 records, and a candidate whose counts move is
reading $s$ back. A declared probe whose count function reads I7's own
$s$ classifies **SMUGGLED = true**; a grammar-side probe classifies
**false**. The classifier is a measurement, not a label.

For census candidates specifically, the count function is built from the
link relation alone and is therefore a *constant* function of the I7
record it is handed. `SMUGGLED = 0` across the census is consequently
**structural, not measured**: no candidate of this shape can be
S-valued, and the classifier's positive value is exercised only by the
declared probe. The verdict string carries that qualifier rather than
reporting a zero that could not have been anything else.

**Interior position** (pin R2). R6b′'s type census is carried verbatim
— *"the type census proves a leg has no interior division event for a
split to sit at"* — and the classifier is two-valued: a probe reading
that must place a division inside a leg classifies dead-on-arrival,
while the declared count generator does not, because it counts events
*on* a link object and never positions *inside* one. The probe cites
R6b′ C1's type verdict; it does not re-run C1.

---

## 5. The census

**120 rows over 60 distinct candidates. 0 FOUND. 0 SMUGGLED. 8
UNMOTIVATED, all of them at the quotient reading.**

| fate | total | @EMBEDDING | @QUOTIENT |
|---|---|---|---|
| TYPE-DEAD | 72 | 36 | 36 |
| ARITY-DEAD | 16 | 12 | 4 |
| ARITY-DEAD-BELOW | 6 | 2 | 4 |
| STRUCT-DEAD | 10 | 10 | 0 |
| HOM-DEAD | 8 | 0 | 8 |
| UNMOTIVATED | 8 | 0 | 8 |
| FOUND / SMUGGLED / COUNT-DEAD | **0** | 0 | 0 |

**The carrier stamp records what ran.** Both quotients are exercised —
as the `MENU-CLASS` and `CONG-CLASS` *site generators*, and it is there
that their class graphs are built and measured separately (MENU 243
edges and 45 self-loops; CONG 376 edges and 0). The carrier *label*
enters no computation: the link relation is selected by the site
generator, never by the carrier field, so the 120 rows are 60
computations under two labels. Measured field by field with only the two
label fields removed, all 60 cells are byte-identical across the two
labels and 0 disagree. The identical fate distributions are therefore a
fact about the enumeration and **not** an agreement between carriers;
the stamp is `@BOTH-QUOTIENTS-AS-SITE-GENERATORS`, and a gate compares
the two tables cell by cell so that a divergence could not be stamped
`@BOTH` silently.

**The full table** (identical at both stamps; `rep` is the arity
treatment; `E` is the embedding reading, `Q` the quotient reading):

| site | link | rep | arity | fate @E | fate @Q |
|---|---|---|---|---|---|
| ACTOR | ACTOR-PAIR | NONE | 2 | ARITY-DEAD | ARITY-DEAD |
| ACTOR | ACTOR-PAIR | RESTRICTION | 2 | ARITY-DEAD-BELOW | ARITY-DEAD-BELOW |
| ACTOR | EXTENSION-EDGE | NONE / RESTRICTION | 2 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| ACTOR | COVER-PAIR | NONE / RESTRICTION | 2 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| MENU-CLASS | ACTOR-PAIR | NONE / RESTRICTION | 113 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| MENU-CLASS | EXTENSION-EDGE | NONE | 113 | ARITY-DEAD | **HOM-DEAD** |
| MENU-CLASS | EXTENSION-EDGE | RESTRICTION | 113 | **STRUCT-DEAD** | **HOM-DEAD** |
| MENU-CLASS | COVER-PAIR | NONE / RESTRICTION | 113 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| CONG-CLASS | ACTOR-PAIR | NONE / RESTRICTION | 185 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| CONG-CLASS | EXTENSION-EDGE | NONE | 185 | ARITY-DEAD | **UNMOTIVATED** |
| CONG-CLASS | EXTENSION-EDGE | RESTRICTION | 185 | **STRUCT-DEAD** | **UNMOTIVATED** |
| CONG-CLASS | COVER-PAIR | NONE / RESTRICTION | 185 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| EVENT-SUBSET | ACTOR-PAIR | NONE / RESTRICTION | 1 048 576 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| EVENT-SUBSET | EXTENSION-EDGE | NONE | 1 048 576 | ARITY-DEAD | **HOM-DEAD** |
| EVENT-SUBSET | EXTENSION-EDGE | RESTRICTION | 1 048 576 | **STRUCT-DEAD** | **HOM-DEAD** |
| EVENT-SUBSET | COVER-PAIR | NONE | 1 048 576 | ARITY-DEAD | ARITY-DEAD |
| EVENT-SUBSET | COVER-PAIR | RESTRICTION | 1 048 576 | **STRUCT-DEAD** | ARITY-DEAD-BELOW |
| ULAM-PREFIX | ACTOR-PAIR | NONE / RESTRICTION | 3969 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |
| ULAM-PREFIX | EXTENSION-EDGE | NONE | 3969 | ARITY-DEAD | **UNMOTIVATED** |
| ULAM-PREFIX | EXTENSION-EDGE | RESTRICTION | 3969 | **STRUCT-DEAD** | **UNMOTIVATED** |
| ULAM-PREFIX | COVER-PAIR | NONE / RESTRICTION | 3969 | TYPE-DEAD $\times2$ | TYPE-DEAD $\times2$ |

Every one of the 120 rows is bound to its own fate by a gate: the 60
distinct (reading, site, link, repair) cells are declared as data above
the census, and each row's computed fate is compared against its own
declared cell. Aggregates do not stand in for cells.

### 5.1 The embedding reading: the grading theorem and arity

Every `STRUCT-DEAD` above is decided by one exact fact, and most of them
need no enumeration at all.

**The grading theorem.** Measured: every extension edge raises history
length by exactly 1 — **3968 of 3968**, no exceptions. So if every class
of a quotient is length-homogeneous, its class-extension graph is
**graded by length**, and a graded relation is both acyclic and
2-colourable by the grade's parity — that is, **bipartite**, carrying no
odd cycle. Measured: **CONG-185 is length-homogeneous** (0 classes span
more than one length), so the CONG blade is a theorem, not a
measurement; and its class graph is bipartite. **MENU-113 is not**: 45
of its classes span more than one length, and those 45 classes are
*exactly* its 45 self-loop classes. That is why the self-loops are
there.

**The target supplies the odd cycle.** I7's lattice is
$\mathbb Z_3$-periodic and closes a 3-cycle on 3 distinct sites at
**27 of 27** of its cells. Three is odd, so no bipartite relation
carries it — at any size, over every subset at once. That decides all
$\binom{113}{9}$, $\binom{185}{9}$, $\binom{2^{20}}{9}$ and
$\binom{3969}{9}$ restrictions in one step, with no sampling and no cap.

**And where the grading does not apply, the restriction is executed.**
The MENU class graph is not bipartite, so its blade cannot be the
theorem. It is instead a complete induced-subgraph search: every vertex
of an admissible restriction carries at least the target's minimum
degree inside the restriction, hence at least that degree in the whole
graph, and the search over that set is exhaustive. It finds **0** of the
$\binom{113}{9}$ restrictions inducing the target, in 14246 search
nodes, and **0** of the $\binom{185}{9}$ in 17388. The declared
restriction is no longer an axis that is offered and never taken.

Measured, on both blades:

| link generator | site objects available | carries the target's odd cycle? |
|---|---|---|
| ACTOR-PAIR | **2** | **yes** — a symmetric relation on 2 objects, 336 co-division occurrences |
| EXTENSION-EDGE @MENU | 113 | **no** — 45 self-loops, not bipartite, and 0 of $\binom{113}{9}$ restrictions induce the target |
| EXTENSION-EDGE @CONG | 185 | **no** — bipartite by the grading theorem, 0 self-loops |
| EXTENSION-EDGE on subsets / addresses | $2^{20}$ / 3969 | **no** — graded by cardinality and by address length, both strict |
| COVER-PAIR on singleton subsets | $2^{20}$ | **no** — the realised relation is empty |
| COVER-PAIR at the carrier | — | not posed: the carrier is a family, not a record, so the event poset's cover relation has no family-level referent (TYPE-DEAD) |

The acyclicity of the class graphs is measured three ways and reported
at every length, not only up to 6: a completed topological sort on all
113 and all 185 vertices after self-loop removal, **0 non-trivial
strongly connected components** at both by Tarjan's algorithm — which
decides cyclicity at every length at once — and an independent
comparator that enumerates simple directed cycles up to length 6 and
finds none. **A self-loop is not a generator cycle** — a bijection sends
distinct sites to distinct objects, so a loop is unusable.

The scissors close like this. The grammar *does* have a cyclic
structure: two actors talking to each other, with **336** co-division
occurrences on the channel. Those 336 are **one** set of **8** distinct
pair arbitrations entered in both directions — the relation is symmetric
by construction, so every realised edge is a 2-cycle and $A\to B$ and
$B\to A$ are the same events counted once, not two disjoint
populations. The grammar has no shortage of
*objects* either: 185 congruence classes, 3969 addresses, a million
event subsets. What it does not have is both at once. **Its cycles live
where it has two objects, and its objects live where it has none.**

That is why the crystals work and the transport carrier does not. A
crystal has nine actors, so its one cyclic generator has nine objects.
The transport carrier has two.

### 5.2 The quotient reading: the wipeout, and the free items reached

Under the quotient reading a candidate is a surjection of realised
objects onto the sites with every realised edge carrying a declared
displacement, and acyclicity is no obstruction to one. The cells are
decided further down, and three things happen.

**MENU dies exactly, with no search.** A self-loop demands the zero
displacement, and no declared link displacement is zero, so node
consistency empties the domain of every self-loop class outright: 45 of
them at MENU, and 13 at the realised division-event-subset graph, which
dies the same way. **8 rows** are HOM-DEAD, and the kill is exact rather
than searched.

**CONG survives the existence question and dies below it.** Arc
consistency over the nine sites does not wipe out, and the declared
search — a topological-order sampler under a declared linear congruential
stream, falling back to maintained arc consistency with
minimum-remaining-values, at seed 20260810 and a cap of 40 solutions —
returns 40 quotient maps. The best of them leaves 8 of the 27 count
cells at zero (**19** strictly positive), so no searched map yields the
strictly positive count field HA §3.1 requires. And the choice inventory
is free: **17** distinct induced count fields over the 40 solutions,
**6** under the direction relabellings and **2** under orientation. The
fiber counts are *lower bounds* over a declared search — more search can
only add fields, never remove one — so a free item stays free, and the
fate is UNMOTIVATED for good.

**And the pre-registered free items are reached.** The Ulam-prefix
quotient attains a strictly positive count field at **27 of 27** cells —
it passes every gate the embedding reading killed it at — and then dies
at the choice standard, with a site-assignment fiber of **40**, a
direction-label fiber of 6 and an orientation fiber of 2. This is the
first place in the unit where `I-ORIENT` returns a value other than 1.

So the honest statement about the inventory is not that nothing reaches
it. Under the embedding reading nothing does. Under the quotient reading
the inventory is exactly where 8 of the 120 rows are decided, and they
are decided against: a map exists, and it is not forced.

---

## 6. The choice inventory

`MOTIVATED` $\iff$ zero free items. The three items the pin
pre-registered are the ones the census measures, and their fibers are
computed as the number of **distinct count fields** the choice produces
— not as the number of choices, which would over-count symmetries the
reading does not see.

| item | crystal (FOUND) | crystal falsifier | probe @ I7 | census @ QUOTIENT, CONG | census @ QUOTIENT, ULAM |
|---|---|---|---|---|---|
| `I-SITE-ASSIGNMENT` | **1** (72 isomorphisms, one field) | **6** | **1** (1296 isomorphisms, one field) | **17** | **40** |
| `I-DIRECTION-LABEL` | **1** | **2** | **1** | **6** | **6** |
| `I-ORIENT` | **1** | 1 | **1** | **2** | **2** |
| **free items** | **0** → FOUND | **2** → UNMOTIVATED | **0** → FOUND | **3** → UNMOTIVATED | **3** → UNMOTIVATED |

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

Under the embedding reading nothing in the census reaches the inventory,
because nothing survives the type, arity and structure gates. Under the
quotient reading the inventory is where 8 of the rows are decided, and
this unit decides them. The two facts belong together: the EMPTY is
structural at one reading and choice-theoretic at the other, and it is
EMPTY at both.

---

## 7. The verdict

> **`WELD2-EMPTY-AT-THE-DECLARED-FAMILY-READING-STRATIFIED-THE-GRADING-THEOREM-AND-THE-SELF-LOOP-WIPEOUT@BOTH-QUOTIENTS-AS-SITE-GENERATORS:MENU-113+CONG-185(CARRIER-AXIS-INERT:60-DISTINCT-CELLS-x2-STAMPS)`**
> `<ROWS=120|READINGS=EMBEDDING+QUOTIENT|FOUND=0|SMUGGLED=0(STRUCTURAL-NOT-MEASURED-FOR-CANDIDATES)|UNMOTIVATED=8(ALL-AT-QUOTIENT)|ARITY-DEAD=16|ARITY-DEAD-BELOW=6|HOM-DEAD=8|STRUCT-DEAD=10|TYPE-DEAD=72`
> ` -- MECHANISM@EMBEDDING=THE-GRADING-THEOREM(EVERY-EXTENSION-EDGE-RAISES-LENGTH-BY-1:3968-OF-3968|CONG-LENGTH-HOMOGENEOUS-SO-GRADED-AND-BIPARTITE|MENU-NOT:45-MULTI-LENGTH-CLASSES=EXACTLY-ITS-45-SELF-LOOPS|TARGET-CLOSES-A-3-CYCLE-ON-3-DISTINCT-SITES-AT-27-OF-27-CELLS)-AND-THE-DECLARED-RESTRICTION-EXECUTED(INDUCED-SUBGRAPH-SEARCH-COMPLETE:0-OF-C(113,9)|0-OF-C(185,9))-AND-ARITY(THE-ONLY-GENERATOR-CARRYING-A-TARGET-TYPE-CYCLE-IS-THE-ACTOR-PAIR-WITH-2-OBJECTS:336-CO-DIVISION-OCCURRENCES-OF-8-DISTINCT-EVENTS-THE-SAME-SET-BOTH-WAYS)`
> ` -- MECHANISM@QUOTIENT=MENU-SELF-LOOP-WIPEOUT-EXACT(45-SELF-LOOPS-DEMAND-DISPLACEMENT-0-AND-NO-DECLARED-LINK-IS-0;8-ROWS-HOM-DEAD)|CONG-COUNT-POSITIVITY-19-OF-27-AT-40-DECLARED-SOLUTIONS|THE-PRE-REGISTERED-FREE-ITEMS-ARE-REACHED(ULAM-COUNT-FIELD-POSITIVE-AT-27-OF-27-AND-UNMOTIVATED-AT-THE-CHOICE-STANDARD)`
> ` -- CONTROLS=FOUND-AT-CRYSTAL@CRYSTAL-CARRIED-L2(FOUND-candidate,ISOS=72,FIBERS-ALL-1,CONFIGS=288)|FALSIFIER-FLIPS(UNMOTIVATED,I-SITE-ASSIGNMENT-FIBER=6)|EMPTY-AT-WALK(ARITY-DEAD)|CRYSTAL-AT-I7(STRUCT-DEAD)|PIN-NAMED-COVER-GENERATOR-NEVER-FIRES(STRUCT-DEAD-AT-BOTH-TARGETS)|FOUND-AT-I7-TARGET=NO-COMMITTED-GRAMMAR-RECORD;REACHABLE-AT-A-DECLARED-PROBE(FOUND-candidate,ISOS=1296,CONFIGS=15552)`
> ` -- INGREDIENT=COUNT-SEMANTICS-INTACT(ADDITIVITY-972-OF-972|DIVISION=ARBITRATION-TAG-FORCED)`
> ` -- CARRIER-RE-DERIVATION=CONG-185-6-OF-6`
> ` -- CRYSTALS=DIAGONAL-EMPTY-AT-9-OF-9-IN-5-OF-5|INDUCED-DET=0-AT-EVERY-SITE-OF-EVERY-CRYSTAL|ADMISSIBLE-I7-RECORDS-INDUCED=0`
> ` -- SCOPE=(A,B)-D<=4-CARRIER|I7-d2-L3-9-SITES-3-LINKS|DECLARED-WINDOW=FIRST-TO-LAST-ARBITRATION-CUT|READING-AXIS-DECLARED-BY-THIS-UNIT-NOT-BY-THE-PIN>`

The head is **derived, not typed**: a second reconstruction reads only
the receipt payload, rebuilds every segment — the outcome word included
— from the measured fate multiset and the measured controls, and the two
strings are compared complete, all 2032 characters of them.

The scout's `NO-SEED-AT-THE-CARRIER` is **confirmed and sharpened**.
The census does not find that the grammar is geometry-blind; it finds
exactly which properties the transport carrier fails to hold
simultaneously under each reading of the pin's question, and it exhibits
a grammar arena — the arbitration crystals — where they *are* held
simultaneously and the detector fires.

**Between delivery and adjudication this is a candidate reading.**

---

## 8. Deviations, priced

1. **The reading axis is this unit's, not the pin's.** The pin declares
   three generator axes; the census adds the arity treatment the pin's
   own sentence about measured arity obstructions licenses, and adds the
   admissibility reading outright. Both widenings are conservative — an
   extra axis can only add candidates and can never hide a FOUND — and
   both are stamped in the verdict rather than folded into the pin's
   vocabulary.

2. **The crystal control fires at the lattice the record carries, not
   at I7's**, and the FOUND branch at I7's own target is demonstrated on
   a declared probe rather than on a grammar record. The control's job
   is to show the FOUND branch is reachable by this machinery, and it
   does that at both targets; the probe is not a weld and no verdict
   segment treats it as one. The crystal's own disqualification as a
   seed is cited from the scout, not re-derived: its actor arrangement
   is a declared blueprint, its direction set is a construction choice
   (d47 pin §3), and the transfer runs through paper 29's named missing
   map. The pin's named control generator — the record's own cover
   structure — returns STRUCT-DEAD at both targets and is reported.

3. **Two site generators are not materialised at full declared arity.**
   EVENT-SUBSET ($2^{20}$) and ULAM-PREFIX (3969) are decided under the
   embedding reading by a **grading theorem** — the subset-extension
   relation is graded by cardinality and the prefix relation by address
   length, both strict along every realised edge with 0 exceptions, so
   both are bipartite by an identity of the definition. That is exact
   and covers every subset at once. It is an argument rather than an
   enumeration, and the receipt marks it per row in the
   `acyclicity_basis` field of the census rows, which names the grading
   that forces each row. The realised objects are materialised
   alongside — 25 and 3969 — so the argument is checked against a
   measurement rather than standing alone. The poset-height grading is
   **not** strict and is not used: the cover row's basis is the measured
   emptiness of its realised relation.

4. **Scope.** The carrier is $(A,B)$ at depth $\le 4$; I7 is read at
   $d=2$, $L=3$. Deeper carriers are cited, not run: D74's committed row
   for $(A,B)$ at depth $\le5$ carries 265 MENU and 462 CONG classes,
   and this run binds that row's bytes verbatim rather than printing the
   two numbers unsourced. Wider actor pools are not run. The scissors
   argument is a statement about *this* carrier; §9 registers the tests
   that would move it.

5. **The window and the division predicate are declared**, with their
   sensitivities disclosed in §6 rather than folded into the free-item
   count. Under the embedding reading a reader who classes either as
   free reads the same census with the same fates, since no candidate
   reaches the inventory; under the quotient reading the 8 UNMOTIVATED
   rows are already free at three items, so neither reclassification
   changes a fate.

6. **The scout note of record was amended after the pin froze.** Ledger
   #89 added an addendum ("**No reversal — every verdict stands**";
   three further register hits, all binned to existing rows). This unit
   reads the pinned bytes at commit `95c3b77`. Two of the 24 pinned
   sources carry different working-tree bytes — the repo has live
   concurrent writers — and both are read through `git show 95c3b77:`
   rather than from mutable worktree state. The routes are recorded per
   file in the receipt. Both declared pin commits carry the pinned bytes
   for `paper-12-gamma-main.md`; the run takes the first that resolves.

   **The git-less leg cannot byte-reproduce while that is true, and the
   failure is the designed one.** Run with no `git` on the path, 22 of
   the 24 pinned sources resolve, `G-PROVENANCE` **fails**, the run exits
   1 — and it writes nothing, so the delivered artifacts are untouched.
   That is a scoped compliance note rather than a defect of
   construction: the two unresolvable sources are unresolvable because
   another agent is mid-repair on them, and the unit refuses rather than
   substituting whatever the worktree happens to hold.

7. **Disclosed because it was measured**: at this scope the *unweighted*
   partition — on the event set alone, ignoring the weights — also
   returns 113 classes. The carrier is the coarser object it looks
   like, and the weights add no refinement here.

8. **`D60-GRID(3,12)` carries one division event**, so its count field
   is zero on every link, and it is the reason the strict-positivity
   claim is stamped to the four arbitration crystals rather than to the
   family. It is reported in the crystal table rather than dropped: the
   delivery grid is a delivery crystal, not a division crystal, and the
   distinction is exactly what U4 is about.

9. **The quotient reading's search is declared, and its numbers are
   search-relative in one direction only.** The 40 solutions come from a
   declared deterministic search at a declared seed; the count-positivity
   maximum over them is an upper bound on nothing — a wider search could
   find a better field — while the inventory fibers are lower bounds
   that a wider search can only raise. The UNMOTIVATED fates therefore
   stand under any extension of the search; the "19 of 27" does not, and
   is stamped with its search.

---

## 9. The successor register

Registered, not claimed.

### 9.1 S1 — the $\ge 9$-actor unit is NOT launched as posed

The scout report of record (`v14/note-routeA-successor-scout.md`,
`88375db9cec2`) proves the symmetric-family form of the question is
pre-determined: actor-relabelling equivariance from the empty history
makes the family $S_n$-invariant, so a symmetric 9-actor carrier's
co-division ACTOR-PAIR relation is $K_9$, 8-regular, with a constant
count field — 0 isomorphisms into I7's 3-link lattice and 0 into the
2-link crystal lattice, and a declared restriction cannot repair it
because every induced subgraph of $K_9$ is a $K_9$. Posed that way the
unit would re-derive EMPTY by over-connection. Its content is registered
instead:

> **The obstruction at 9 actors is a LINK-COUNT MISMATCH, not an
> absence.** $K_9$ *is* a Cayley graph of $(\mathbb Z_3)^2$ — on the
> four generators $\{e_1, e_2, e_1+e_2, e_1-e_2\}$, with all $9!$
> isomorphisms — while I7 declares **three** links. The grammar offers
> four directions and the lattice declares three. **The diagonal is
> absent from the crystals, not from the grammar**: the crystals'
> arbitration groups are rows and columns, and diagonal pairs share
> neither. A $\ge 9$-actor carrier would be the corpus's first
> construction populating a diagonal pair, and so the first grammar-side
> $q_{12}$ — but only through a **declared channel sub-grammar** that
> breaks $S_9$ to a 3- or 4-regular incidence, or through Route B. It is
> reachable by a declaration, not by a derivation, and the structure
> gate fires first.

That row is a standing datum for any Route-B pricing.

### 9.2 U4 is the next Route-A unit

v11 paper 0 §7: *"the division events of a crystal form a crystal"*.
Rebuilding the crystals with renewal-only records makes the renewal
sublattice the **generated** carrier of this unit's FOUND control,
rather than a lattice read off a declared actor blueprint. It is the
only successor that repairs the blueprint half of the control question
and it must be run against the 3-link target, where it must produce a
strictly positive diagonal count; if it cannot, the empty diagonal is
promoted from a property of five committed records to a property of the
crystal *construction*, which is a stronger and citable result.

The scout's ingredient table is handed over with it: the constructors
are committed twice; the division-event yields are 18/72, 24/96, 6/30,
12/66 and 1/46, so the renewal sublattice is non-degenerate for the four
arbitration crystals and degenerate for the delivery grid — §8.8's
distinction is exactly U4's question and should open its pin. The
preliminary translation-stabilizer measurement is $\langle(1,1)\rangle$
on all four arbitration crystals and trivial on the delivery grid, and
is to be made corpus-grade two-way before it is used.

**Declared data the U4 pin must fix**, because none of it is pinned
anywhere: the **site reading** (initiator versus register footprint —
the supports differ, the stabilizers agree); the **renewal-only
operationalization**, which has three candidates (filter the record to
arbitration events, re-run the builder on a restricted candidate stream,
or quotient by non-arbitration events) and is nowhere committed; and the
**scope**, which is the arbitration crystals, with the delivery crystal
as the named counterexample.

**Four walls, to be engraved in the pin.** L-1: U4 may test only
order-level covariance, a **fourth** form whose admissibility must be
**argued before testing** — the retracted "weaker form" wording is
banned. BHS: finite valency makes sprinkling-grade Lorentz invariance
provably unavailable, so testing it manufactures a false negative.
Kleitman–Rothschild height control is mandatory — a dimension reading
without a height control is worthless. And $q_{12}\equiv 0$ is inherited
unchanged from the rook's graph: diagonal pairs share neither row nor
column.

### 9.3 The four consumers

- **To the Γ-iteration.** CONG-185 is re-derived here six of six by a
  construction independent of the review's, and the *unweighted*
  partition at AB4 also returns 113 — so any Γ claim that loads on
  "weighted" at this scope is untested. Freshly measured: MENU 113 nodes
  / 243 edges / 45 self-loops, CONG 185 / 376 / 0; both acyclic by three
  independent methods; the CONG class graph admits a level grading and
  the MENU one admits none, exactly, because of its self-loops. And a
  correction: **carrier-relativity is NOT-MEASURED here, not agreement**
  — the carrier coordinate was never varied, so this unit adds no
  evidence either way to the Γ-main adjudication's carrier-relativity
  open, and the identical fates must not be read as one.

- **To any Route-B declaration.** The scout's own named Route-B map does
  not type-check at this carrier: "site ← actor, link ← delivery
  channel" is ARITY-DEAD at 2 objects against 9, and a restriction can
  only shrink. What a declaration must supply, itemised by this census:
  a nine-element site set; a direction labelling over 3 links and an
  orientation; a link relation realising all three declared
  displacements, where the best of 40 declared quotient maps on CONG-185
  covers 19 of 27 cells; and a strictly positive diagonal count, which
  no committed crystal supplies. It should be priced at its true arity —
  `DECLARATION-RELATIVE(SITE-SET+DIRECTION-LABEL+ORIENT+WINDOW)`, not a
  flat `DECLARATION-RELATIVE`. This census does not foreclose it; it
  establishes what a *derivation* would have to supply.

- **To the diagonal question, the sharpest new one.** Does *any* grammar
  record supply a co-division incidence on a diagonal pair? Measured
  across the committed crystal family: no, at 9 of 9 sites in 5 of 5,
  and the induced determinant is 0 at every site of every one of them.
  A construction that did would be the first grammar-side $q_{12}$ and
  the first record able to carry off-diagonal curvature. This unit found
  the question; it did not answer it.

- **To R4.** R4's adjudication relocated its headline onto the declared
  diagonal: `G-LINKS-IN-BALL` is decided by the anchored link $(1,1)$
  having sum-norm 2, so R4's connective — and with it its unique
  locality scale — is forced by I7's *declared* link set. Read with this
  unit's measurement, one sentence is licensed by both artifacts
  together: **the declared link that forces R4's connective is the one
  link no committed grammar record writes.** Licensed with it: that both
  results rest on the same declaration, so a future change to I7's
  declared link set moves both, and the corpus has one declaration doing
  double duty. Not licensed: that R4's theorem is threatened, weakened
  or conditional on the crystals; that the $(1,1)$ link should be
  dropped; or any inference from the crystals (2-link,
  blueprint-declared, $d=2$) to I7's record family (declared data,
  3-link). The two arenas share a coordinate label and no object.

### 9.4 What would move this verdict

- **Depth.** Does the class-extension graph acquire directed cycles on
  distinct vertices, or lose its length grading, at depth $\ge 5$? At
  CONG the answer is already no by the grading theorem, which is
  depth-free; only MENU is live there, and the test should measure
  self-loops as well as cycles.
- **The quotient reading's remaining freedom.** The 8 UNMOTIVATED rows
  die at a choice standard, not at a structure. What would make one of
  them motivated is a *forcing* argument on the induced count field —
  which is exactly what the crystal falsifier isolates: withdraw one
  arbitration and the isomorphism count does not move while the fibers
  do, so forcing is a property of the count field and not of the graph.
  That is the successor experiment, and the crystal falsifier is its
  prototype.

---

## 10. The receipt

`v14/code/w2_census_exact.py` — one self-contained program.
`--selftest` corrupts each of the 26 anchors individually in memory —
each numeric anchor on its computed side, each verbatim anchor both by
corruption and by truncation to a common substring — confirms all 26
would fail the run, exercises the real exit path with an injected
failure and confirms it returns 1, and writes nothing; 0 vacuous
anchors. `--mutant NAME` runs any of **43 declared mutants**, each of
which dies at its named gate with artifacts untouched. `--list-mutants`
prints the mutant registry and `--list-gates` the gate registry, so the
gate count is checkable without reading the source. Unknown flags exit
2, abbreviations are not accepted, and `--help` exits 0. **A run that
fails a gate writes nothing**, so the delivered artifacts are never
overwritten by a run that does not stand up; and after writing, both
artifacts are read back from disk and compared field by field against
the run that produced them, so a receipt that contradicts its own output
text cannot ship. The plain run writes `w2_census_output.txt` and
`w2_census_receipt.json` and is **byte-reproducible** — run twice,
verified identical, and identical again from a foreign repo root.

Every verdict-bearing number carries a comparator built from
primitives its builder does not share: the menu partition by mapping
equality against frozenset keys; the congruence by relation-splitting
bisimulation against signature refinement; the square census by
family grouping against admissibility pairs; acyclicity by strongly
connected components and by enumerated simple cycles against a
topological sort; additivity by a re-derived family test and by a
distinct-key count against the refinement construction.

Every number printed in this paper is checked **inside the run** against
the receipt: the paper's numerals are extracted and each must occur in
the receipt as a delimited number — not as a substring of some larger
one — or in a declared allow-list of ledger references and section
numbers. The head is protected twice over: a second reconstruction from
the payload alone must reproduce it as a complete string, and the
obstruction it names is checked substring by substring against the
measurements rather than against the function that produced the name.
No numeric anchor's computed side may be a typed literal — the unit
parses its own source and refuses one — because an anchor typed on both
sides passes its own comparison by arithmetic and no corruption of
either side could catch it. 12 verbatim anchors bind the quotations here to their pinned
bytes, each named to the gate that consumes it, each carrying its
committed byte length and occurrence count so that a truncation to a
common substring fails, and **each falsified by its own declared
mutant**. 4 waivers are declared, all of class DECLARATION-CARRIED or
REGISTER-ONLY, and all named in the receipt's waiver census.
