# Signature selection: the indefinite region, its floors, and a polarity that is not the dynamics'

**SIG / paper-24.** Pin `v14/note-sig-pin.md` (FROZEN, sha256-12
`ab73239daff5`, ledger #233). Parents, both terminal and both cited at their
pinned bytes: the R = 4 arena (paper-21) and the coupling (paper-20). Code
`v14/code/sig_exact.py`; artifacts `v14/code/sig_output.txt`,
`v14/code/sig_receipt.json`.

**SCOPE (binding, carried verbatim from the pin).** Two constraints were
adopted before this unit was written and they govern every sentence in it.
**(A) REACHABILITY BEFORE POLARITY** — no polarity sentence is licensed
without a Stage-0 census, and `SIG-BLOCKED-AT-REACHABILITY` was a first-class
outcome. **(B) NO SITE-MARGINAL OBSERVABLES** — the GDL blindness theorem
makes any site-marginal record-blind, so this unit's observables read the
record. **This unit measures a region of RECORD space**: the sign of a
two-by-two form built from division counts on a nine-site lattice. It is not
a spacetime signature and no Lorentzian, causal or cosmological reading is
taken or licensed anywhere below.

**Verdict**, in four segments.

```
SIG-STAGE-0-REACHABILITY-[STATIC: THE INDEFINITE REGION IS OCCUPIED AT R=1 UNRESTRICTED (INDEFINITE AT 9 OF 9 SITES), AT R=5 AT A FULL SITE (1,1,5), AT R=6 IN A COVERING RECORD AND AT R=7 IN A STRUCTURALLY LIVE ONE -- THE INHERITED #211 FLOOR R=5 IS NECESSARY AND NOT ATTAINED (16,108,764 MULTISETS SCANNED, MINIMUM UNCOVERED 2) | DEPOSIT THEOREM: 1 PER CELL PER ROUND OVER ALL 280 PARTITIONS, SPECTRUM 0:1,4:27,6:54,7:162,9:36 | DYNAMIC: THE COUPLED WALK OCCUPIES IT AT (A3=1,1,1 AT R=3, T=6) AND (A4=1,1,2 AT R=4, T=5) AND (A5=1,1,3 AT R=5, T=3)]@ARENAS-6-OF-THE-COLLINEAR-FAMILY+HORIZON-5(LADDER-1..5;EXTENSION-6-ON-A3)+COIN-FIBER-5
```

```
SIG-CLEARING-[3 PAIRS CLEAR AND THE CHEAPEST IS ORDER-RELATIVE (WINNERS INCIDENCES:A3,STATIC-FIRST:A3,STEPS:A5); THE UNIQUE PAIR THAT COSTS NO NEW DECLARATION IS A4 = 1,1,2 = G-FLAT AT R=4, HORIZON 5 -- I7'S OWN DECLARED RECORD, PAPER-21'S DRIVEN ARENA, AT PAPER-20'S OWN DECLARED HORIZON; INDEFINITE MASS 146623744/847288609443 AT THE BORN MENU AND 5072320/1162261467 AT THE RECORD MENU; SINGULAR FIRST AT T=3; THE GRAMMAR CANNOT REACH THE REGION BELOW R=6 AT ALL (LIVE R=7) AND THE MECHANISM IS THE DEPOSIT THEOREM THE EMISSION CHANNEL IS FREE OF]
```

```
SIG-POLARITY-[BORN MENU AVOIDED: INDEFINITE MASS 146623744/847288609443 AGAINST 148895641/90632341800 UNDER THE UNIFORM-ON-SUPPORT COUNTING MEASURE ON THE SAME TREE, RATIO 675143691622400/6409469116243161 | RECORD MENU SELECTED: 5072320/1162261467 AGAINST 53/34992, RATIO 81157120/28166373 | BOTH SIGNS ARENA-INVARIANT ACROSS THE ARENAS THAT CLEAR INSIDE THE HORIZON | THE STAGE-FROZEN ARM (NO BACK-REACTION, THE RECORD STILL ACCUMULATING) GIVES 34816/129140163 AND 325184/71744535 | PAPER-20'S FROZEN CONTROL GIVES 0 BY THEOREM AT EVERY HORIZON] -- OBSERVABLES=RECORD-READING(CONSTRAINT B: THE SITE MARGINAL IS SIGNATURE-BLIND, MEASURED IDENTICAL AT A4 AND A7 WHILE THEIR INDEFINITE MASSES ARE 146623744/847288609443 AND 1)
```

```
SIG-BLOCKED-AT-THE-EMISSION-READING-<COIN-FIBER=INVARIANT: ALL 5 S_3-COVARIANT CLASSES EXACTLY UNITARY, ALL 5 AVOIDED AT THE BORN MENU AND ALL 5 SELECTED AT THE RECORD MENU -- THE SIGN IS A FUNCTION OF THE EMISSION READING ALONE AND OF NOTHING ELSE MEASURED HERE | MOD-3 THEOREM=MACHINE-CHECKED(3 ARENA PAIRS AT 12 BRANCH-WEIGHT MAPS COMPARED PATH BY PATH, IDENTICAL AT 12 OF 12 UNDER THE BORN MENU AND AT NONE UNDER THE RECORD MENU: THE BORN BRANCH MEASURE IS A FUNCTION OF n0 mod 3 WHILE THE SIGNATURE IS A FUNCTION OF n0, SO THE ABSOLUTE MASSES ARE REPRESENTATIVE-RELATIVE AND ONLY THE RELATIVE POLARITY CAN BE FORCED) | SCOPE=THIS UNIT MEASURES A REGION OF RECORD SPACE, NOT A SPACETIME SIGNATURE>
```

Between delivery and adjudication every headline reading here is a
**candidate reading**.

---

## 1. The question, and the constraint that had to come first

I7's readout turns the three link counts at a site into a two-by-two form,
and that form has a sign. Nine of I7's records are positive definite; two are
not — `G-SINGULAR` at determinant zero and `G-INDEF` below it. The pin asks
whether the coupled dynamics of paper-20 **selects**, **avoids**, or is
**neutral** toward the indefinite region.

The question could not be asked directly, and the reason is the parents'.
Paper-20 ran the coupled walk to its declared horizon and measured the record
leaving I7's admissible class — but only to the boundary:

> the coupled record leaves I7's admissible class with exact probability
> 927415552/847288609443 at the Born menu

and

> all 1,316 inadmissible leaves carry the excess pattern (0, 0, 3) at exactly
> one site

— every one of them singular, none indefinite. Its own successor register
left the question open in the exact words this unit answers:

> Whether the probability grows, whether the indefinite region is reached at
> all, and whether a halt-on-inadmissibility semantics changes any verdict
> are three separate measurements, none taken here

So Stage 0 gates everything. A polarity sentence about an unreachable region
would be a statement about an empty set, and the pin made
`SIG-BLOCKED-AT-REACHABILITY` a first-class outcome for exactly that case.
The floors this unit inherited from the paper-21 adjudication were R = 5
statically, R = 8 for `G-INDEF`, and horizon at least 6 dynamically — and the
pin's instruction about them was *verify, never assume*. They are verified
below, and one of them turns out to be necessary rather than attained.

## 2. The arena, declared as data

### 2.1 The lattice, the cells and the readout

Nine actors sit on a 3 x 3 grid parsed as Z_3^2. I7's declared link set is
read from its own committed receipt — the two axis directions and the one
positive diagonal — and never re-typed here. A **cell** is a pair (site,
link): the 27 cells are exactly the 27 unordered co-division pairs the
grammar can realise along a declared direction, because the three +l moves
along a line of direction l cover that line's three pairs exactly once.

The readout is I7's, applied unchanged: `q11 = n_1`, `q22 = n_2`,
`q12 = (n_3 - n_1 - n_2)/2`. The three regions follow from I7's own
criterion, carried verbatim from paper-20:

> a record is admissible when q is nonsingular and positive definite at every
> site, by the exact Sylvester criterion

so a site is POSDEF when `q11 > 0` and `det > 0`, SINGULAR at `det = 0` and
INDEFINITE below. Every determinant in this unit is computed by **two routes
that share no expression** — the readout as written in exact Fractions, and
the symmetric integer form `4 det q = 2(n1n2 + n1n3 + n2n3) - (n1^2 + n2^2 +
n3^2)` — and the two are compared over the whole declared code box, 2197
codes, with no disagreement. The symmetric form is Heron's: `4 det q` is
positive exactly when the square roots of the three counts satisfy the strict
triangle inequality, which is why the region is a statement about how
lopsided a site's three counts are and about nothing else.

### 2.2 The arenas, and the horizon

Every arena in this unit is a homogeneous record `(1, 1, c)` — the collinear
family paper-21 named:

> the three link-direction parallel classes of AG(2,3) with the diagonal
> class taken twice

extended along its own diagonal. ROW^a COL^b DIA^c induces `(a, b, c)` at
R = a+b+c, covering and foreign-pair-free at every rung, which section 3
verifies rung by rung. The rungs this unit walks are `A3 = (1, 1, 1)`
(paper-19's welded record, paper-20's own arena), `A4 = (1, 1, 2)` — I7's
declared `G-FLAT` and paper-21's driven record — and `A5 = (1, 1, 3)`, the
cheapest live record one round above it. Three further rungs enter only as
residue partners in section 7: `A6 = (1, 1, 4) = G-SINGULAR`,
`A7 = (1, 1, 5)` and `A8 = (1, 1, 6) = G-INDEF`.

**The declared window is named inside the head**: 6 arenas of that family,
horizon 5 with the whole ladder published, one extension to 6 on A3, and the
5-member coin fiber. Every other column is exhaustive over an object the
window does not cap — by enumeration, or by the deposit theorem of section 3.

## 3. Stage 0A — the static census: what the grammar alone can reach

### 3.1 The deposit theorem

A conflict group's realised co-division pairs are its three site pairs; a
pair along a declared direction lands on one cell, and a pair along the one
direction I7 does not declare is FOREIGN and lands nowhere. Enumerating all
280 partitions of the nine sites into three triples and computing that map
gives the whole round structure at once:

**A round deposits at most 1 incidence on any one cell, measured exhaustively
over all 280 partitions, so a cell's count after R rounds is at most R.**

The same enumeration returns at most two incidences on any one site, and an
incidence spectrum of `0:1, 4:27, 6:54, 7:162, 9:36` — which is paper-21's
own committed row, read from its receipt at run time and reproduced here from
this unit's own deposit map. Paper-21 states the aggregate form of the same
fact:

> no round can deposit more than 9 link incidences

The per-cell form is the one that decides this unit, and it is the sharper
one: a cell can only be fed **once per round**, so concentration costs
rounds.

### 3.2 The floors, and the four nested classes

**At a site whose three cells are all at least one, SINGULAR needs a cell at
4 and INDEFINITE needs a cell at 5.** Both are measured over the declared
box; the cheapest codes are `(1, 1, 4)` — which is `G-SINGULAR` — and
`(1, 1, 5)`, which I7 does not declare. With the deposit theorem this is
immediately a budget statement: an indefinite site whose links are all
occupied needs R >= 5.

That is the inherited floor, and it is **necessary**. Whether it is
**attained** depends entirely on what else is being asked of the record, and
the honest census has four nested classes:

| class | what it requires | first budget |
|---|---|---|
| unrestricted | an indefinite site anywhere | R = 1 |
| full site | that site's three cells all occupied | R = 5 |
| covering | all 27 cells occupied | R = 6 |
| structurally live | covering, and no foreign pair | R = 7 |

The first row is the one nobody had looked at. **One round of the ROW
parallel class induces the code (1, 0, 0) at every one of the nine sites,
with 4 det q = -1: the indefinite region is occupied at R = 1.** A single
round of the committed grammar produces a record that is indefinite at every
site — because a site with two empty link directions is as lopsided as a site
can be. Indefiniteness is not expensive in this arena; **indefiniteness with
all three links occupied** is, and that is the object every later row is
about.

### 3.3 The inherited floor is not attained

At R = 5 an indefinite full site needs a cell at exactly 5, so **all five
rounds must hit that one cell**. That reduces the question to a finite
enumeration, and the enumeration is exhaustive: **No covering record at R = 5
carries an indefinite site: over all 16,108,764 multisets of five rounds that
all hit one cell the least number of uncovered cells is 2.** Two cells always
remain empty, whatever else the five rounds do. The weaker class is attained
there, and the price is visible in the witness: **The full-site class is
attained at R = 5: 2,210,000 multisets of five rounds induce the code
(1, 1, 5) at the target site, and the witness this unit exhibits leaves 13 of
its 27 cells at zero.**

One cell is enough to settle all of them: the linear maps of AG(2,3) that
preserve the declared link set, together with the nine translations, act on
the 27 cells with a **single orbit**, so a census that fixes one cell is a
statement about every cell.

**The covering floor is R = 6, and the structurally live covering floor is
R = 7.** Both are witnessed and both searches are exhaustive under the same
two prunes (the uncovered cells must fit in what the remaining rounds can
deposit; the site's code must still be able to go indefinite):

| R | pool | covering record with an indefinite site |
|---|---|---|
| 4 | ALL | NO |
| 4 | LIVE | NO |
| 5 | ALL | NO |
| 5 | LIVE | NO |
| 6 | ALL | YES |
| 6 | LIVE | NO |
| 7 | ALL | YES |
| 7 | LIVE | YES |

The live row's first YES is the collinear rung `(1, 1, 5)` at R = 7. I7's own
declared `G-INDEF` is `(1, 1, 6)` and costs R = 8, exactly as the adjudication
said. What moves is the middle: **R = 5 is a floor the grammar cannot stand
on.**

Read against paper-21's row one budget down, this is one fact rather than
two. Paper-21 measured

> Across the whole covering class the maximum cell count is 2

at R = 4 and derived its three-valued determinant spectrum from it. That is
the same obstruction this unit meets at R = 5 and R = 6: a round feeds a cell
once, so a covering record's cells cannot be lopsided until the budget is
large enough to pay for both the cover and the concentration.

## 4. Stage 0B — the dynamic census: what the walk reaches

### 4.1 The walk, rebuilt and anchored at five rows

Paper-20's machine is re-implemented here from its declared machinery and
never imported: the site-block-diagonal coin `C(x) = G . D(x)` with
`D(x) = diag(w^{n_l(x)})`, the shift `|x,l> -> |x+l,l>`, one division event
emitted per step with the law-native kernel's own weight, non-selectively, and
the record incremented on the emitted cell. Both of paper-20's declared
emission readings are carried: the **Born menu**, where the weight is the
post-coin Born weight, and the **record menu**, where it is the division
count itself.

The rebuild is bound rather than trusted. From its own arithmetic it
reproduces the parent's committed exit probability at the Born menu
(`927415552/847288609443`) and at the record menu
(`37440224/5811307335`), the branch counts at both (`284078` and `314928`),
the exit census code by code (`466`, `471`, `379`), and the return-time row —
the earliest third visit to a site is step 5 — and it re-measures, as the
parent did, that every inadmissible leaf has exactly one site out. Five
independent rows, one rebuild.

### 4.2 The event budget, and the first horizon of each region

The walk emits exactly one division event per step, so a region that needs
`k` events on one cell cannot be entered before step `k`. From `(1, 1, c)`
the diagonal cell needs `5 - c` events to go indefinite and `4 - c` to go
singular, and every arena's measured first step is checked against its own
bound:

| arena | record | R | events to indefinite | first singular | first indefinite |
|---|---|---|---|---|---|
| A3 | 1, 1, 1 | 3 | 4 | 5 | 6 at the extension |
| A4 | 1, 1, 2 | 4 | 3 | 3 | 5 |
| A5 | 1, 1, 3 | 5 | 2 | 1 | 3 |

Every one of the three arenas reaches the indefinite region, and the third
column says why the horizons differ: the arena pays in rounds what the walk
would otherwise pay in steps.

**The extension row is a measurement, not an extrapolation.** Horizon 6 on
A3 is affordable because a branch that cannot raise any cell to the region
floor within its remaining steps stays positive definite with its whole
subtree, so its mass can be carried in aggregate. That prune is a theorem and
it is checked rather than trusted: the pruned engine must reproduce the full
engine's singular and indefinite masses at **every step of the horizon they
share, on two arenas**, before its extension is read. It does, and at the
extension the indefinite region is first occupied at step 6 — the inherited
dynamic floor, attained exactly where the adjudication predicted.

## 5. Stage 1 — the clearing, and what it costs

**The clearing pair is (A4, horizon 5): I7's own declared G-FLAT at R = 4,
driven by paper-21, walked at paper-20's own declared horizon.**

**At the clearing arena the coupled walk puts exact mass
146623744/847288609443 on records with an indefinite site at the Born menu,
first positive at step 5.**

Three pairs clear, and the cheapest is **order-relative**. Under a cost order
that ranks the static budget first, A3 at horizon 6 wins; under total steps,
A5 wins at 8; under total incidences, A3 wins at 33. The three orders
disagree and this unit publishes the disagreement rather than resolving it by
fiat. What is unique is something else, and it is a measured property rather
than a preference: **A4 is the only pair that costs no new declaration** — a
record I7 itself declares, at a horizon paper-20 itself declared. The polarity
census below runs there, and its sign is re-measured at the other arenas.

**The walk reaches at R = 4 and horizon 5 a region the grammar cannot reach
below R = 6.** That is the sharpest thing Stage 1 says, and the mechanism is
section 3's: the grammar feeds a cell at most once per round, so it buys
lopsidedness only by spending rounds; the emission channel has no such
constraint and can put every event it has on one cell. The back-reaction is
not merely a perturbation of the geometry — **it is a concentration channel
the round structure does not possess.**

## 6. Stage 2 — the polarity census

### 6.1 The three measures, declared

A region mass is a probability and E-24 binds: no count becomes a probability
without a declared measure. Three are declared and all three are carried.

- **BORN** — the coupled emission tree's own branch measure.
- **NULL** — the **uniform-on-support counting measure on the same tree**:
  every branch of a node gets equal weight. It shares the tree exactly and
  differs only in the weights, so a comparison between them is a statement
  about the dynamics and never about the branch set.
- **STAGE-FROZEN** — the same walk on phases that never update, with the
  record still accumulating: the arm that separates the back-reaction from
  the accumulation. Paper-20's own frozen control, whose record never changes
  at all, is carried beside it and gives 0 at every horizon by theorem.

Both probability measures are gated to sum to one at every step of every
reading, per object.

### 6.2 The two readings disagree in sign

**Under the Born menu the indefinite mass is 146623744/847288609443 against
148895641/90632341800 under the uniform-on-support counting measure on the
same tree: AVOIDED.** The Born measure puts roughly a tenth of the counting
measure's mass on the branches that reach the region.

**Under the record menu the indefinite mass is 5072320/1162261467 against
53/34992: SELECTED.** Nearly three times the counting measure's mass.

The mechanism is visible in the two menus themselves. The Born menu's weight
is an interference pattern, and repeatedly feeding one cell requires the walk
to return to a site and keep amplitude on the same link; the coin spreads it
instead. The record menu's weight is the count itself, so an emission on a
cell **raises that cell's own weight** — a rich-get-richer rule, and
concentration is exactly what the indefinite region is made of.

The stage-frozen arm gives `34816/129140163` and `325184/71744535`. Both are
larger than their coupled counterparts, so at this arena the back-reaction
pushes *away* from the region under both readings, while the emission rule
decides which side of the counting measure the whole census sits on.

Both signs are **arena-invariant** across the arenas that clear inside the
horizon.

### 6.3 Constraint B, discharged twice

The pin forbids site-marginal observables, because the GDL delivery proved
that

> a decoherence functional built from the state at a single time, in a basis
> the coin acts on site-locally, is blind to the record it is supposed to be
> a function of

The prohibition is discharged structurally and measured. Structurally, every
observable this unit reads a region with takes the record and nothing else —
an AST scan of their argument lists finds no state and no marginal.

Measured, and this is the sharper half: **the ensemble site marginal is
identical at A4 and A7**, whose records agree modulo three, while their
indefinite masses are `146623744/847288609443` and `1`. The same site
marginal, at both ends of the region census. A site-marginal observable
provably cannot carry this unit's verdict, and the parent's blindness theorem
is exhibited here on the very quantity in question.

## 7. Stage 3 — forcedness, and the mod-3 theorem

### 7.1 The coin fiber

Paper-20's coin was declared under a reality condition with a fiber of six
classes, and it ran the hidden members to the full horizon. All of them run
here, at both readings, to the full horizon, on the clearing arena:

| coin | Born indefinite mass | null mass | Born word | record word |
|---|---|---|---|---|
| `GROVER` | 146623744/847288609443 | 148895641/90632341800 | AVOIDED | SELECTED |
| `W` | 170531816/847288609443 | 94739/62775648 | AVOIDED | SELECTED |
| `MW` | 392/531441 | 10273973819/7653397752000 | AVOIDED | SELECTED |
| `MMW` | 85264186/847288609443 | 74201/49043475 | AVOIDED | SELECTED |
| `M2W` | 478/531441 | 156109153/150124340520 | AVOIDED | SELECTED |

**All 5 members of the S_3-covariant coin fiber are exactly unitary, and all
5 return AVOIDED at the Born menu and SELECTED at the record menu.** The
magnitudes are coin-specific; the sign is not. What is forced at this arena
is the coin-independence. What is not forced is the polarity.

### 7.2 The mod-3 theorem, and what it does to the absolute numbers

The coin reads the record through exactly one channel, and paper-20 declared
its price:

> the walk consumes the count residue n mod 3, not the count

The consequence for a signature question is severe, and it is machine-checked
here rather than argued. **The Born branch measure is a function of the
record modulo three: 3 arena pairs compared path by path agree at 12 of 12
branch-weight maps.** Two arenas whose records differ by three at every cell
generate the *same* measure over emission histories, path for path and weight
for weight — while their region censuses differ completely. `A4` and `A7` are
such a pair: identical measure, and indefinite masses of
`146623744/847288609443` and `1`.

The instrument is two-way, which is what makes it a measurement: the same
comparison under the **record** menu disagrees at every level, because that
menu's weight is the count and not its residue. The record menu breaks the
blindness the Born menu has.

So the absolute region masses of this unit are **representative-relative**:
the same dynamics, at arenas the grammar reaches at different budgets,
carries any of them. What survives the shift is the *relative* polarity — the
comparison of the Born measure against the counting measure on the same tree
— and that is the only quantity this unit reads as a property of the
dynamics.

### 7.3 The outcome

The polarity is invariant across the coin fiber and opposite across the two
emission readings, and paper-20 declared both readings, ran both, and
privileged neither. There is therefore no single polarity word to emit, and
the outcome is the pre-registered `BLOCKED-AT` form with the object named:

**`SIG-BLOCKED-AT-THE-EMISSION-READING`.**

That is a negative about the *question*, not about the measurement. The
reachability census is positive and exhaustive; the polarity numbers are
exact and coin-invariant; what fails is the step from them to a property of
the dynamics, and the thing that fails it is a choice the parent already
declared and priced.

## 8. The walls

**L-1 — argued before any test, then declined.** L-1 records that order-level
covariance is a fourth form outside paper 8's three. Admissibility would
require a group declared to act on the generated causal order and a reason to
read that group as a covariance group. This arena supplies finite records and
a translation action on a nine-site lattice, and this unit constructs no
bridge from Z_3^2 translations to any boost. **The fourth form is not tested
here.** The sentence retracted in 2026 is absent from the object under test,
and the gate that enforces its absence whitespace-normalises, ASCII-folds and
strips markdown prefixes from both sides.

**BHS — no sprinkling-grade test.** The reproduction catalog records that

> a Poisson sprinkling admits no Lorentz-invariant finite-valency graph

and these schedules are finite-valency by construction, so running the test
would manufacture a false negative. None is run, and the abstention is
measured: the gate scans this run's declared measurement surface — every
measured receipt key together with the statement and evidence of every gate
evaluated — and its falsifier writes a sprinkling-grade reading into that
surface and dies there.

**Kleitman-Rothschild — no dimension reading, so no height control is owed.**
No chart width, no Myrheim-Meyer estimate, no max-shatter reading appears
anywhere, and that too is a scan of the same surface rather than a
declaration.

**The signature resonance, NAMED — and this is the sharpest the wall has been
in this line, because a determinant has now gone negative.** Paper-21 could
write that its induced form

> is a positive definite Euclidean form on a nine-site lattice, it is not a
> signature, it is not a metric on any continuum

and this unit has measured records for which the same form is *indefinite*.
The naming sentence is mandatory, is derived from the measured floor code
rather than typed, and a falsifier deletes it from the object under test:

**The indefinite region is NAMED AND NOT READ: a site whose counts are
(1, 1, 5) has 4 det q = -5 < 0, which is a sign of a two-by-two form built
from division counts on a nine-site lattice; it is not a spacetime signature,
not a light cone, not a metric on any continuum, and no Lorentzian, causal,
signature-change or cosmological reading of it is taken here or licensed by
anything measured here.**

**The word "selection" is named too.** SELECTED and AVOIDED in this unit mean
one thing and nothing more: the Born branch measure puts more or less mass on
a declared subset of records than the uniform-on-support counting measure on
the same tree. No dynamical preference, no variational principle and no
cosmological selection is claimed, and section 7 measures why none could be
read off these numbers.

## 9. Choice inventory

| # | item | class | fiber | where it binds |
|---|---|---|---|---|
| 1 | the site carrier and the link set | **forced** | 1 | I7's own receipt, read at run time |
| 2 | the readout and the admissibility criterion | **forced** | 1 | I7's, applied unchanged; two routes |
| 3 | the walk, the coin register and the connection | **forced** | 1 | paper-20's, rebuilt and anchored at five rows |
| 4 | the deposit map | **forced** | 1 | the grammar's own realised pairs |
| 5 | the arena family `(1, 1, c)` | **declared** | 1 | section 2.2; the collinear rungs, all constructed |
| 6 | the horizon and its extension | **declared** | 1 | paper-20's 5, extended once to 6 with the prune gated |
| 7 | the emission reading | **declared, VERDICT-DETERMINING** | 2 | paper-20's own fiber; both run, every row stamped |
| 8 | the coin | **declared** | 5 | paper-20's fiber; every member run at both readings |
| 9 | the NULL measure | **declared** | 1 | uniform on support, on the same tree |
| 10 | the cost order for "cheapest" | **declared** | 3 | all three reported; they disagree |
| 11 | the region trichotomy | **forced** | 1 | I7's Sylvester criterion, two routes |
| 12 | the target cell of the static searches | **measured** | 1 | one orbit under the arena's symmetry |

One declared item is verdict-determining and it is item 7, which is exactly
what the outcome word records.

## 10. Verdict

```
SIG-STAGE-0-REACHABILITY-[STATIC: THE INDEFINITE REGION IS OCCUPIED AT R=1 UNRESTRICTED (INDEFINITE AT 9 OF 9 SITES), AT R=5 AT A FULL SITE (1,1,5), AT R=6 IN A COVERING RECORD AND AT R=7 IN A STRUCTURALLY LIVE ONE -- THE INHERITED #211 FLOOR R=5 IS NECESSARY AND NOT ATTAINED (16,108,764 MULTISETS SCANNED, MINIMUM UNCOVERED 2) | DEPOSIT THEOREM: 1 PER CELL PER ROUND OVER ALL 280 PARTITIONS, SPECTRUM 0:1,4:27,6:54,7:162,9:36 | DYNAMIC: THE COUPLED WALK OCCUPIES IT AT (A3=1,1,1 AT R=3, T=6) AND (A4=1,1,2 AT R=4, T=5) AND (A5=1,1,3 AT R=5, T=3)]@ARENAS-6-OF-THE-COLLINEAR-FAMILY+HORIZON-5(LADDER-1..5;EXTENSION-6-ON-A3)+COIN-FIBER-5
```

```
SIG-CLEARING-[3 PAIRS CLEAR AND THE CHEAPEST IS ORDER-RELATIVE (WINNERS INCIDENCES:A3,STATIC-FIRST:A3,STEPS:A5); THE UNIQUE PAIR THAT COSTS NO NEW DECLARATION IS A4 = 1,1,2 = G-FLAT AT R=4, HORIZON 5 -- I7'S OWN DECLARED RECORD, PAPER-21'S DRIVEN ARENA, AT PAPER-20'S OWN DECLARED HORIZON; INDEFINITE MASS 146623744/847288609443 AT THE BORN MENU AND 5072320/1162261467 AT THE RECORD MENU; SINGULAR FIRST AT T=3; THE GRAMMAR CANNOT REACH THE REGION BELOW R=6 AT ALL (LIVE R=7) AND THE MECHANISM IS THE DEPOSIT THEOREM THE EMISSION CHANNEL IS FREE OF]
```

```
SIG-POLARITY-[BORN MENU AVOIDED: INDEFINITE MASS 146623744/847288609443 AGAINST 148895641/90632341800 UNDER THE UNIFORM-ON-SUPPORT COUNTING MEASURE ON THE SAME TREE, RATIO 675143691622400/6409469116243161 | RECORD MENU SELECTED: 5072320/1162261467 AGAINST 53/34992, RATIO 81157120/28166373 | BOTH SIGNS ARENA-INVARIANT ACROSS THE ARENAS THAT CLEAR INSIDE THE HORIZON | THE STAGE-FROZEN ARM (NO BACK-REACTION, THE RECORD STILL ACCUMULATING) GIVES 34816/129140163 AND 325184/71744535 | PAPER-20'S FROZEN CONTROL GIVES 0 BY THEOREM AT EVERY HORIZON] -- OBSERVABLES=RECORD-READING(CONSTRAINT B: THE SITE MARGINAL IS SIGNATURE-BLIND, MEASURED IDENTICAL AT A4 AND A7 WHILE THEIR INDEFINITE MASSES ARE 146623744/847288609443 AND 1)
```

```
SIG-BLOCKED-AT-THE-EMISSION-READING-<COIN-FIBER=INVARIANT: ALL 5 S_3-COVARIANT CLASSES EXACTLY UNITARY, ALL 5 AVOIDED AT THE BORN MENU AND ALL 5 SELECTED AT THE RECORD MENU -- THE SIGN IS A FUNCTION OF THE EMISSION READING ALONE AND OF NOTHING ELSE MEASURED HERE | MOD-3 THEOREM=MACHINE-CHECKED(3 ARENA PAIRS AT 12 BRANCH-WEIGHT MAPS COMPARED PATH BY PATH, IDENTICAL AT 12 OF 12 UNDER THE BORN MENU AND AT NONE UNDER THE RECORD MENU: THE BORN BRANCH MEASURE IS A FUNCTION OF n0 mod 3 WHILE THE SIGNATURE IS A FUNCTION OF n0, SO THE ABSOLUTE MASSES ARE REPRESENTATIVE-RELATIVE AND ONLY THE RELATIVE POLARITY CAN BE FORCED) | SCOPE=THIS UNIT MEASURES A REGION OF RECORD SPACE, NOT A SPACETIME SIGNATURE>
```

Read out. Stage 0 licenses everything that follows and corrects one inherited
number while it does. Statically, the indefinite region is not expensive at
all if a record may leave links empty — a single ROW round is indefinite at
all nine sites — and it is expensive exactly when every link is occupied: R =
6 to cover, R = 7 to stay structurally live, R = 8 for the one such record I7
declares. The inherited R = 5 floor is necessary and unattained, and the
obstruction is the deposit theorem, which is also paper-21's block
quantisation one budget down.

Dynamically all three walked arenas reach the region, at horizons their own
event budgets predict, and the extension confirms the adjudication's dynamic
floor of 6 on paper-20's own arena. The clearing pair is the one that costs
nothing new — I7's declared `G-FLAT` at paper-20's declared horizon — and
there the walk reaches, with four rounds and five steps, a region the grammar
needs six rounds to reach at all. That gap is this unit's most transportable
result: **the emission channel concentrates where the round structure cannot.**

The polarity census is exact, coin-invariant, arena-invariant, and it splits
on the emission reading: the Born menu avoids the region by about a factor of
ten against the counting measure on its own tree, the record menu selects it
by about three, and the back-reaction pushes away from the region under both.
Behind that stands the mod-3 theorem, which says how little of this can be a
property of the dynamics at all: the Born branch measure is blind to exactly
the part of the record that decides the signature, so the absolute masses are
representative-relative by construction. The outcome word is therefore
`SIG-BLOCKED-AT-THE-EMISSION-READING`, and the block is named rather than
mourned: it says precisely which declaration a successor must derive.

## 11. Deviations, priced

1. **The horizon is 5, with one extension to 6 on one arena.** The emission
   tree multiplies by up to 27 per step. Price: nothing is claimed beyond the
   declared horizon. Mitigation: the whole ladder is published, the extension
   is exact rather than sampled, and the prune that affords it is gated
   against the full engine on two arenas at every shared step.

2. **The extension carries the Born mass only.** The uniform-on-support
   comparator needs the whole unpruned tree, which is precisely what the
   pruning theorem avoids. Price: no polarity word is emitted at the
   extension arena, and none appears.

3. **The static searches fix one cell.** Price: none, and the reason is
   measured rather than assumed — the arena's own symmetry acts on the 27
   cells with a single orbit, and that is a gate.

4. **The R = 6 and R = 7 covering searches are branch-and-bound, not
   enumeration one record at a time.** Both prunes are sound (an uncovered
   cell must fit in the remaining rounds' deposits; a site whose code can no
   longer go indefinite cannot be rescued), so no witness can be missed.
   Price: the searches report existence and a witness, not a count.

5. **The arenas are the collinear family only.** Price: every dynamic
   statement is about homogeneous `(1, 1, c)` records. Mitigation: they are
   the family the parents drove, they include the only declared record in
   range, and the static census that surrounds them quantifies over all
   partitions rather than over the family.

6. **The walk consumes the count residue.** Inherited from paper-20 and not
   mitigated here — it is precisely what section 7 measures the consequences
   of, and it is the first successor item rather than a defect of this run.

7. **`halt-on-inadmissibility` is not run.** Paper-20 declared it as the
   update-semantics fiber; this unit inherits the run-on semantics and does
   not re-open the choice. Price: the third of paper-20's three open
   measurements stays open, and this unit answers the other two.

## 12. The instrument

`v14/code/sig_exact.py`, with the #82 CLI contract: a delivery run that is the
only writer, `--no-write`, `--numbers`, `--selftest`, `--mutant NAME`,
`--break-anchor NAME`, `--verify-paper [PATH]`, `--list-gates` and
`--list-mutants`; every unknown flag, unknown flag argument, missing flag
argument and second mode flag exits 2.

Arithmetic is exact end to end — Python integers, `fractions.Fraction`, and
the cyclotomic ring as integer pairs, so every Born weight is a rational
integer over a power of three — and an AST scan of the file for float
literals and true division, together with a recursive type scan of the
emitted receipt, are gates. Counts are computed, never typed. Gates bind
objects rather than aggregates: the emission law's normalisation is checked
per branch per step, each arena's first-occupancy step against its own event
budget, each coin against its own unitarity, each declared exemption against
its own occurrence.

Provenance is by pinned sha with the products gated: 10 sources are read at
run time, each hash-verified, plus 10 path-value anchors that bind a value at
a path inside a source rather than only the source's bytes, and 10 verbatim
anchors that bind quotation fidelity, each clearing a length floor and each
naming the gate that consumes it. No subprocess of any kind is invoked, so
the run is correct off-tree and with no version control present — which is
also why the GDL blindness theorem is cited from a frozen quotation carrying
its commit rather than read: its working-tree copy is held dirty by a
concurrent sibling, and a committed-sha read would need one.

The expensive objects are memoised on their complete input tuple rather than
on a label, and the memo carries its own liveness gate: two probes with
different keys must return different values and a repeated key must hit, so a
memo keyed on a label dies before any measurement depends on it. The
self-test clears the cache and is required to record misses.

The head is derived a second time by a comparator that re-parses the
serialized receipt, types all four templates itself, and re-derives the
outcome word from the receipt's own reachability and polarity rows through
its own conditional; an AST scan requires the two routines to share no string
constant containing a numeral, with receipt keys excluded as lookups rather
than text. The paper under test is checked in the same run for claim
rendering, table rendering, numeral coverage and claim polarity: every
headline sentence and every row of the three measurement tables is assembled
from this run and required to occur, the tables exactly once each; numeral
coverage scans the whole paper — prose, tables, inline spans and the fenced
verdict blocks — against exactly three declared lists, and the fenced blocks
are matched by multiset against their declared copy count.

The seal is total: every published receipt key is either sealed at the moment
its gate passes or listed as DECLARED-UNSEALED, and the completeness gate
compares the manifest against the declared key set. The artifacts are written
from the sealed payload through `os.replace`; the terminal integrity gate
compares the bytes on disk against the gate-time seal after a deliberately
corrupted probe has been shown to be detected; a run that fails a gate writes
nothing, and the only writer is downstream of a falsifier sweep that actually
ran. Every declared falsifier's published description is verified against its
own code by AST, and a falsifier whose corruption is a constant boolean is
rejected outright.

## 13. The successor register

Registered, not claimed.

**S-1 — the connection is the whole question now.** The Born menu's blindness
to everything but the count residue is what makes the absolute polarity
representative-relative. Paper-20 registered the rational-modulus coupling as
its first successor item; this unit turns it into the *decisive* one, because
a connection that consumes the count itself would make the Born branch
measure a function of the signature-deciding data. Until that is built, no
absolute signature statement at this arena is transportable.

**S-2 — the emission reading needs a derivation, not a declaration.** The two
readings give opposite polarity signs at every coin and every arena measured
here. Nothing in the corpus derives one of them; paper-20 declared both and
ran both. A successor that derives the menu from the law — or that measures a
third reading strictly between them — settles this unit's outcome word.

**S-3 — the concentration channel.** The walk reaches at four rounds and five
steps what the grammar needs six rounds for, and the mechanism is that the
grammar feeds a cell once per round while an emission may feed the same cell
every step. That comparison is a general statement about the two channels and
is measured here only at one arena; a successor should ask whether the gap
grows with the budget, and whether any grammar-side schedule concentrates
faster than one incidence per round at a larger cap.

**S-4 — the singular boundary is crossed, not just reached.** Paper-20 found
the exit going to `det = 0` and stopping there at its horizon. This unit
finds records strictly beyond it at three arenas. What no measurement here
touches is whether the corpus's laws — refinement, stochastic split, renewal
transport — have anything to say about a record with an indefinite site, since
all three were built on the admissible class. That is a scope question for the
law-over-records line and not for this one.

**S-5 — the R = 6 covering witness is not structurally live.** The first
covering record with an indefinite site pays with foreign pairs; the first
live one costs a further round. Whether the weld detector accepts either, and
what the fibers are there, is one census away and is not run here.

**What may not be inherited**, as a standing row: any absolute region mass as
a property of the dynamics rather than of an arena representative; SELECTED
or AVOIDED as anything but a comparison against the declared counting measure
on the same tree; the clearing pair as *the* cheapest one; the R = 1
indefinite row as a statement about admissible records; the extension row as
a statement at any horizon above 6; and any signature, spacetime, causal,
dimensional or cosmological reading whatever.
