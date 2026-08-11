# The law over records at R = 6: one lawful refinement step

**LOR-A / paper-30.** Pin `v14/note-lor-pin.md` (FROZEN, sha256-12
`5239c4671f1a`, ledger #233). Code `v14/code/lor_exact.py`; artifacts
`v14/code/lor_output.txt`, `v14/code/lor_receipt.json`.

**Verdict**, in four segments.

```
LOR-A-REFINEMENT-ACTS-[ONE LAWFUL STEP TAKEN AT THE R = 6 WELDED RECORD (2, 2, 2); PLACES 9 -> 36 SITES AND 27 -> 108 INTERVALS; NEW SITES 27 = 9 PER DIRECTION; DETERMINED 54, FREE 54; ADDITIVITY 27 OF 27, RESTRICTION 27 OF 27, READOUT 9 OF 9]@WINDOW-16-DRIVEN-OF-5,184-WITNESSES
```

```
LOR-A-LAWS-2-OF-3-NON-EMPTY-AND-THEY-COMPOSE<PAPER-06=UNIQUE-AT-27-OF-27-INTERVALS(FIBER-1|ORBITS-1|SIMPLEX-DIM-0|PINNED-TRANSITIVE)-AGAINST-9-OF-27-AT-R-4|PAPER-04=DYADIC-LIVE-RAW-FIBER-1-SUBDIVIDES-27-OF-27|PAPER-09=EMPTY-ALL-27-INTERVALS-IN-THE-SUPPORT-HOLE-[1, 2]|COMPATIBILITY=COMPOSE-AND-AGREE(06-SUPPORT-IS-04-WHOLE-FIBER-AT-27-OF-27;THE-TWO-ORDERS-AGREE-AT-108-OF-108-SLOTS;CONFLICT-FALSE)>
```

```
LOR-A-DICTIONARY-SURVIVES-AT-THE-EXTENDED-CARRIER-[ACTOR-PLUS-CO-DIVISION-PAIR-TO-SITE]<9+27=36|DETERMINED-LINKS-54-ARE-THE-54-ACTOR-IN-PAIR-INCIDENCES|FREE-LINKS-54-ARE-3-EACH-INSIDE-THE-18-NON-COLLINEAR-DECLARED-TRIANGLES -- THE-PROCESS-SUPPLIES-BOTH-HALVES:THE-SPLIT-BY-ITS-OWN-SEAM(1-LIVE-CUT-LOCUS-OF-17-AT-5,184-OF-5,184-WITNESSES;SPLIT-1-1-AT-27-OF-27)AND-THE-FREE-HALF-BY-ITS-DIVISION-FOOTPRINTS -- CARRIER-ISOMORPHISM-AT-72-OF-5,184-COUNTING-ONLY-AGAINST-864-WITH-THE-REFINED-LATTICES-EDGE-COUNT:THE-ABSTRACT-STRUCTURE-IS-CHEAPER-THAN-THE-DICTIONARY -- REFINED-WELD=FOUND-candidate@EMBEDDING+QUOTIENT<AUT-432|FIBERS-1/1/1|ZERO-FREE-ITEMS> -- COMPLETION-RELATIVE:PAPER-04S-OWN-DECLARED-MINIMAL-COMPLETION-IS-ADMISSIBLE-36-OF-36-BUT-UNMOTIVATED(FIBERS-24/3/2)>
```

```
LOR-A-CEILING-EXACTLY-1-STEP<FLOOR-LOG2-MIN-N=FLOOR-LOG2-2=1;AFTER-THE-STEP-MIN-N-1-CEILING-0 -- A-SECOND-STEP-NEEDS-MIN-N-4-=(4,4,4)-REACHABLE-ONLY-AT-R-12-BY-THE-BUDGET-LAW-R-3m -- LADDER-L-MAX-3x2^FLOOR-LOG2-m-WITH-EQUALITY-AT-THE-DYADIC-BUDGETS-[3, 6, 12, 24] -- SIG=DET-3-TO-3/4-EXACTLY-2^d-4|SIGNATURE-(+,+)-UNMOVED-36-OF-36|REFINED-DET-IS-PAPER-19S-COMMITTED-3/4 -- DIA=THE-DIAGONAL-BUYS-9-OF-THE-27-NEW-PLACES-AND-WITHOUT-IT-9-REFINED-SITES-LIE-ON-NO-COARSE-INTERVAL-ODD-ODD,PAPER-04S-d-3-MECHANISM-27-OF-216-ONE-DIMENSION-DOWN>
```

Between delivery and adjudication every headline reading here is a
**candidate reading**.

---

## 1. The question

Paper-21 opened a door and did not walk through it. Its R = 4 welded record
was splittable at nine of its twenty-seven intervals, one of the three
terminal refinement laws became non-empty on it — and the one that did was
non-empty at its degenerate end, with nothing to act on. The same paper
measured the rung above and stopped there:

> it is reachable by concatenation.

That rung is R = 6, the link-constant record (2, 2, 2), reached by
concatenating two of the seventy-two R = 3 I7-STRICT triples. Paper-21
established, and this unit rebuilds from nothing, that the weld there carries
zero free items, that paper-04's dyadic raw fiber is a single point, and that
paper-06's law is unique. It also recorded what it had not done:

> Nothing at six or eight rounds is driven here.

So the question the pin asks is the first one that can be asked of a law over
records rather than of a record: **do the refinement laws ACT, and what does
one lawful act produce?** Concretely — and this is the user's question in the
form the arena can answer — can the place-count grow, and if it does, does the
process-to-space dictionary the weld established survive the growth?

The answer is yes to both, with a price that is measured rather than
estimated, and a distinction that was not anticipated: the abstract structure
of the refined arena is much cheaper to reach than the dictionary onto it.

---

## 2. The arena, declared as data (RUNBOOK §15)

| row | value |
|---|---|
| boundary | the 27 (site, link) cells of $(\mathbb Z_3)^2$ with links $e_1$, $e_2$, $e_1+e_2$, and the 108 refined slots the dyadic move creates |
| family | the 5,184 ordered concatenations of two of the 72 R = 3 I7-STRICT triples |
| law | paper-06's per-interval invariant split law and paper-04's DYADIC move, applied once |
| state | the split, and the completion of the free refined links |
| arena | the co-division relation on actors, and its extension to actor pairs |
| provenance | 19 hash-pinned sources; 31 (path, value) anchors; 26 verbatim anchors |

The base object is d66's `CONFLICT-GRID(g = 3, R)`, driven directly: nine
actors on a 3 × 3 grid, each round spending the committed budget of three
conflict groups of three cells, each running one cycle of the committed
transport grammar. The variable is the schedule. The declared driven window
is disclosed in the head: **W6**, sixteen six-round schedules, six at the
surviving stratum, eight one per measured dead class, two at the declared seed
fan. Every other column below is exhaustive over an object the window does not
cap — including the census that quantifies over all 5,184 witnesses and the
census that quantifies over all 280 round partitions.

The unit takes no scaling limit, measures no invariant trajectory, and makes
no claim about a continuum.

---

## 3. Stage 1 — the arena, built from nothing

### 3.1 The substrate, counted twice

The partitions of nine sites into three triples are enumerated exhaustively
and counted a second time by the closed form $9!/(3!^3\,3!)$ built from a
factorial computed in the run; both give 280, which is also the value
paper-21's committed receipt carries. Their incidence spectrum is 1 partition
at 0, 27 at 4, 54 at 6, 162 at 7 and 36 at 9.

> **The budget theorem.** No round deposits more than 9 link incidences, so
> six rounds carry at most 54, and the link-constant record (2, 2, 2) needs
> exactly $6 \times 9 = 54$. Equality forces every round to saturate, and the
> census over the 36 saturating groupings is exhaustive over the whole family.

The R = 3 I7-STRICT triples are then counted by two routes that share no code.
Route one sums the per-round incidence vectors and requires the field to be
identically one at all 27 cells. Route two never forms an incidence vector: it
requires the triple's nine conflict groups to cover each of the 27 unordered
declared actor pairs exactly once. Both return 72, which is what paper-19 and
paper-21 committed.

Concatenating two of them gives the arena. Measured: the concatenated
six-round record carries count 2 at each of the 27 (site, link) cells
individually, and its weld is re-verified zero-free here at 1296 isomorphisms
and 1296 quotient maps with fibers 1/1/1. Every ordered pair of the 72 is run
through the per-cell test independently, and all 5,184 pass.

### 3.2 The window, driven

This is the first driven R = 6 record in the line. Measured: a declared
window of 16
six-round schedules is driven through the committed grammar, and at every one
of them the driven link field agrees with the combinatorial field at all 432
compared cells. Each record carries 18 division events, every footprint is
exactly its conflict group, and record length runs from 99 to 102 events.

The v10-layer tie-break is priced as a gate rather than assumed: d60's `pick`
breaks ties with a hash-seed-dependent sort, so every event of every driven
schedule is specified by its full tuple and the builder's own `maxhits` is
required to read 1 at each of the sixteen, with no refusal anywhere.

### 3.3 The splittable census

Paper-04's identity — an interval carrying only its total $n$ admits exactly
$n-1$ places for one interior boundary — is evaluated at each interval on its
own count. Measured: every one of the 27 intervals is splittable and its fiber is the
single point (1, 1), so the raw product over all 27 slots is 1. At R = 4 the
same product was 0, because a count-1 interval cannot be split into two
strictly positive parts.

---

## 4. Stages 2 and 3 — the two laws, and one lawful step

### 4.1 Which laws are live

2 of the 3 terminal refinement laws are non-empty here, against 1 at R = 4:
paper-06's law is unique at 27 of 27 intervals and paper-04's dyadic move
subdivides 27 of 27, while paper-09's kernel still puts all 27 intervals
inside its support hole.

| law | at R = 4 | at R = 6 |
|---|---|---|
| paper-06, the per-interval invariant split law | non-empty, unique at 9 of 27 intervals; empty at the record level | **unique at 27 of 27, and so at the record level** |
| paper-04, the DYADIC move | empty (raw fiber 0) | **live, raw fiber 1** |
| paper-09, the renewal-grain kernel | empty | **empty**, all counts inside the hole |

Paper-06's committed rows are read at (path, value) and applied to each
interval on that interval's own count: at count 2 the fiber is one point, the
orbit count is 1, the invariant simplex has dimension $0 = n-2$, and the
pinned chart group is transitive. That is the law's own reading of its own
degenerate end — paper-06 called it *uniqueness by triviality, not by
selection* — and at this arena the degenerate end is the whole record.

### 4.2 The step

The step is taken and its forced part verified per constraint, never as a
total: additivity holds at 27 of 27 constraints, the coarse counts are
recovered at 27 of 27 cells and I7's readout at 9 of 9 sites. Record-IS-metric
therefore commutes with this refinement, and is shown to rather than assumed.

### 4.3 The new places

This is the segment the pin makes first-class.

| | before the step | after the step |
|---|---|---|
| sites | 9 | 36 |
| intervals | 27 | 108 |
| intervals the record determines | 27 | 54 |
| intervals left free | 0 | 54 |

Measured: the place-count grows: 9 sites become 36 and 27 intervals become
108, of which 54 are determined by the step and 54 are free, and the 27 new
sites divide 9 to each declared direction.

Every refined site is classified individually as a coarse image or as the
interior of exactly one coarse interval; none is left over. Every refined
slot is classified individually as carrying a half of a coarse interval or as
free. The free half is not new: it is exactly paper-04's own measured
freedom —

> Half the refined arena is invisible to the coarse record: 54 of the 108
> refined links lie on no coarse interval.

**The description stamp, which the pin requires and which a gate enforces
word for word: the new places are refined intervals of the declared record
and the sites the dyadic move inserts into them. No actor is created. Nothing
beyond this measured interval and site structure is claimed, and no reading of
this growth as an expansion of anything is taken or licensed here.**

---

## 5. Stage 4 — compatibility

The two laws are compared on their objects rather than argued about. At each
interval the support of paper-06's unique invariant law is compared as a set
against the whole of paper-04's dyadic split fiber; then the refined record is
built twice, once from each law's output, and the two are compared slot by
slot.

Measured: the support of paper-06's law is exactly paper-04's whole split
fiber at 27 of 27 intervals, and the refined record built from each law's
output agrees slot by slot at 108 of 108 refined slots.

The verdict is `COMPOSE-AND-AGREE`, and the scope difference is worth stating
because it is what came apart one rung down. Paper-04's move is record-level
and needs every interval splittable at once; paper-06's law is per-interval.
At R = 4 that difference was the whole story — 04 empty, 06 non-empty at 9 of
27, and the one law that became non-empty had no move to act through. At R = 6
the difference is invisible, because the arena is where both laws are defined
and their outputs coincide.

---

## 6. Stage 5 — the refined record, and the dictionary

### 6.1 Is it still a record?

I7's own Sylvester criterion is evaluated at each of the 36 refined sites
individually, under both declared completions, and both pass. Under the
process-supplied completion the refined record is (1, 1, 1) at every site.

That vector is paper-19's own landing record, one level up: admissible inside
I7's declared count box, and — like paper-19's — not one of I7's declared
records. The honest scope statement is that I7's admissibility **predicate**
extends to the refined lattice while I7's declared **arena** is $L = 3$: the
refined object is a record by I7's criterion and is not a member of I7's
family.

The link-constant completion is unique, and the reason is measured rather than
asserted: the determined half of the refined record is already 1 at every one
of its 54 slots, so link-constancy leaves the 54 free slots no value but 1.

### 6.2 The carrier: the new places are the old links

The refined arena has 36 sites and the process has 9 actors. The un-extended
carrier is therefore ARITY-DEAD against the refined target, measured, and that
is the whole of the naive answer. The measured answer is different, and it is
a bijection rather than a coincidence:

> the 9 actors and the 27 co-division pairs are exactly the 36 refined sites,
> the 54 determined refined links are exactly the 54 actor-in-pair incidences,
> and the 54 free refined links are exactly 3 inside each of the 18
> non-collinear declared triangles

Each clause is checked per object. The carrier map — actor to its coarse
image, co-division pair to the interior of its own interval — is checked to be
a bijection onto the 36 refined sites. Each determined refined link is checked
individually to join an actor to a pair containing it. Each free refined link
is checked individually to join two co-division pairs whose union is one of the
18 non-collinear declared triangles, three per triangle.

So the dictionary's second clause supplies the carrier its first clause
cannot: `CO-DIVISION-ACTOR-PAIR -> LINK` becomes
`CO-DIVISION-ACTOR-PAIR -> SITE` one level down. **The refinement's new places
are the old links.**

### 6.3 The process supplies the split, and supplies it uniquely

Paper-06 named the object a motivated split needs and recorded that the record
layer does not carry it:

> What a motivated split distribution would require is a joint law for WHERE
> inside a record interval its $n_\ell(x)$ division events fall

The record does not carry it — paper-04's mechanism is exactly that *the
record carries interval totals and not event positions*. The **process** does.
A six-round record has 18 division events and therefore 17 loci at which it
can be cut, and each locus induces a split of every interval.

Measured, by two routes that share no state: of the 17 event-level loci at
which the record can be cut, exactly 1 yields a strictly positive split at
every interval at all 5,184 witnesses, and the split it yields is (1, 1) at
all 27. The live locus is the seam between the two three-round blocks.

The predicate is not vacuous and the run says so with a control outside its
own arena: at three blocks — R = 9, where the raw split fiber is 134217728 —
ten of the loci are live, so the process-supplied cut selects but does not
determine in general. R = 6 is the arena at which it determines.

This does not overturn paper-06. Its finding was about the pinned record
layer, and stands: the layer contains no probabilistic object and no
positional datum. What is added is where the missing datum lives. It is not
missing from the process; it is missing from the record, and the weld is what
makes it available.

### 6.4 The free half, and the census that separates structure from dictionary

The 54 free refined links have a process-side referent too: a pair of
co-division pairs is linked when their union is a **realised division
footprint**, with the count the number of division events carrying it. That
rule uses no lattice coordinate at all.

Whether the process satisfies it is then a property of the schedule, and it is
censused exhaustively. Measured: the canonical carrier is an isomorphism at 72
of the 5,184 witnesses, against 864 whose relation merely carries the refined
lattice's edge count.

| class | witnesses |
|---|---|
| `triangles-0|lines-9|carrier-iso-False` | 36 |
| `triangles-6|lines-3|carrier-iso-False` | 324 |
| `triangles-6|lines-9|carrier-iso-False` | 648 |
| `triangles-9|lines-0|carrier-iso-False` | 72 |
| `triangles-9|lines-9|carrier-iso-False` | 144 |
| `triangles-10|lines-5|carrier-iso-False` | 1944 |
| `triangles-12|lines-3|carrier-iso-False` | 1296 |
| `triangles-12|lines-6|carrier-iso-False` | 648 |
| `triangles-18|lines-0|carrier-iso-True` | 72 |

The mechanism is exact. A conflict group that is a **line** of AG(2, 3)
contributes a pair-of-pairs edge the refined lattice does not carry; an
unrealised triangle leaves three of its edges missing. Eighteen groups can
cover all eighteen triangles only by being them, each once — so the surviving
class is forced, not fitted. The 72 fractions here are stamped COUNTING-ONLY:
no measure on the witness space is declared and no typicality claim rests on
them.

**And this is the result that was not anticipated.** Two of the dead classes
carry a relation that is *abstractly isomorphic* to the refined lattice — 432
isomorphisms at both readings, fibers 1/1/1, everything the RSQ standard asks
— while the canonical carrier on them is not an isomorphism and the field it
induces carries 27 and 18 zero cells respectively. Structural isomorphism is
not the dictionary. A witness can have the right space and the wrong map onto
it, and 792 of the 864 right-shaped witnesses do.

### 6.5 The weld of the refined record

Measured: at the process-supplied completion the refined weld returns
FOUND-candidate with 432 automorphisms and fibers 1/1/1, and under paper-04's
own declared minimal completion the same carrier returns UNMOTIVATED with
fibers 24/3/2.

The 432 is the automorphism group of the refined arena, and the fiber reading
carries over from paper-21's theorem because the refined relation is measured
here to be vertex- and edge-transitive: a count field invariant under all its
automorphisms is constant, and

> zero free items holds exactly at the link-constant records, and I7 declares
> none of them.

So the survival of the dictionary is **completion-relative**, and the two
declared completions differ exactly where it matters. Paper-04's own minimal
completion was designed to put each refined site on the diagonal locus; it is
admissible at all 36 sites and it makes the refined record inhomogeneous —
(1, 1, 1) at 9 sites, (1, 1, 2) at 18 and (2, 2, 1) at 9 — and the weld on it
carries two free items. The completion the **process** supplies is the
link-constant one, and it is the one that keeps the weld motivated. Nothing
here forces a completion; what is measured is that the process's own answer
and the RSQ standard's requirement coincide, and that the predecessor's
declared answer does not.

Every value the detector can return is exhibited in this run — FOUND at the
coarse and refined process-supplied arenas, UNMOTIVATED at paper-04's declared
completion, ARITY-DEAD at the un-extended nine-actor carrier, STRUCT-DEAD and
COUNT-DEAD at this unit's declared falsifier and at the dead witness classes —
so the detector is measuring rather than agreeing. The isomorphism search uses
a connected object order for pruning; the count is recomputed under the plain
name order at the coarse arena and agrees, so the order is not one of the
values the instrument can return.

### 6.6 The signature row (the SIG cross-feed)

Measured: the determinant falls from 3 to 3/4, exactly a factor of 4, and the
signature does not move: positive definite at 36 of 36 refined sites. The
factor is $2^d$ at $d = 2$, formed as an exact ratio of Fractions, and the
refined determinant is the value paper-19 committed for its own landing
record.

Under paper-04's declared completion the determinant spectrum is 3/4, 1 and
7/4 instead of a single value: **the determinant is completion-relative and
the signature is completion-blind** — both completions are positive definite
at every site.

**The induced form is NAMED AND NOT READ: q = [[1, -1/2], [-1/2, 1]] is a
positive definite Euclidean form on a thirty-six-site lattice of counts, it is
not a signature, it is not a metric on any continuum, and no Lorentzian
reading of it is taken here or licensed by anything measured here.**

---

## 7. Stage 6 — the iteration ceiling, as a theorem of the arena

Paper-04's ceiling law is grammar-level:

> No record admits more than $\lfloor\log_2(\min n_\ell)\rfloor$ consecutive
> steps.

Its value here is a property of this arena's counts, and it is computed rather
than quoted. Measured: the minimum count is 2, so the ceiling is 1 and exactly
one step exists; after the step the minimum count is 1 and the ceiling is 0; a
second step needs a minimum count of 4, which the budget law places at R = 12.

> **The arena theorem.** At budget $R = 3m$ a structurally live schedule
> reaches the link-constant record $(m, m, m)$ and no other homogeneous
> record; its refinement ceiling is $\lfloor\log_2 m\rfloor$; and the largest
> refined lattice it can reach has side $3\cdot 2^{\lfloor\log_2 m\rfloor}$,
> which is at most $R$ and equals $R$ exactly at the dyadic budgets.

| m | R = 3m | record | ceiling | refined side | places |
|---|---|---|---|---|---|
| 1 | 3 | (1, 1, 1) | 0 | 3 | 9 |
| 2 | 6 | (2, 2, 2) | 1 | 6 | 36 |
| 3 | 9 | (3, 3, 3) | 1 | 6 | 36 |
| 4 | 12 | (4, 4, 4) | 2 | 12 | 144 |
| 8 | 24 | (8, 8, 8) | 3 | 24 | 576 |

Read plainly, and this is a candidate reading of the ladder rather than a
measurement beyond it: **places are logarithmically expensive.** Each further
level of refinement costs a doubling of the process, and on the dyadic budgets
the largest reachable lattice side is exactly the number of rounds — the
process buys at most one unit of refined lattice length per round.

---

## 8. Stage 7 — the DIA row

Measured: the diagonal buys 9 of the 27 new places, and with the diagonal
withdrawn 9 refined sites lie on no coarse interval at all.

The counterfactual is run on the built site set rather than argued: each
refined site is re-tested individually with the declared link set reduced to
the two axes, and the sites that survive on no coarse interval are exactly the
odd-odd parity class. That is paper-04's own $d = 3$ mechanism —

> at d = 3 the dyadic move leaves 27 of 216 refined sites on no coarse
> interval at all

— reproduced one dimension down, with the missing diagonal playing the role
the missing body diagonal plays there. **At $d = 2$ the diagonal link is what
makes the refinement site-complete**, and it buys exactly as many new places
as each axis: 9, 9 and 9.

The diagonal's other role is the off-diagonal of the readout. At a
link-constant record $q_{12} = -n/2$ identically, so the coarse form is
$[[2,-1],[-1,2]]$ and the refined one $[[1,-1/2],[-1/2,1]]$; the diagonal is
the entire reason the form is not diagonal. It is read as a direction on a
finite lattice of counts and as nothing else. At R = 4 the diagonal was the
direction the budget populated twice and the anisotropy was the whole story;
at R = 6 the record is link-constant and the three directions buy equally.

---

## 9. The walls

**L-1 — argued before any test, then declined.** Order-level covariance would
require a group declared to act on the generated causal order and a reason to
read that group as a covariance group. This arena supplies finite records and
a translation action on a lattice of counts; the corpus contains no bridge
from it to any boost and this unit constructs none. The fourth form is not
tested here. The sentence retracted in 2026 is not reproduced, and the gate
that enforces its absence whitespace-normalises, ASCII-folds and strips
markdown prefixes from both sides.

**BHS — no sprinkling-grade Lorentz-invariance test.** A Poisson sprinkling
admits no Lorentz-invariant finite-valency graph and these records are
finite-valency by construction, so running the test would manufacture a false
negative. None is run, and the abstention is measured on this run's declared
measurement surface — every measured receipt key together with every gate's
statement and evidence — with a falsifier that writes such a reading into that
surface and dies there.

**Kleitman–Rothschild — no dimension reading, so no height control is owed.**
No chart width, no Myrheim–Meyer estimate, no max-shatter reading is taken;
the same surface is scanned and the same kind of falsifier is carried.

**No cosmological reading.** Refinement here is a measured operation on a
pinned record. It is not an expansion narrative, and nothing about the growth
of the place-count licenses one. The surface is scanned for an
expansion-of-space reading and the falsifier that writes one in dies there.

**The Lorentzian resonance, NAMED**, in §6.6, mandatorily and under a gate
whose falsifier deletes the sentence.

---

## 10. Choice inventory

| # | item | class | fiber | where it binds |
|---|---|---|---|---|
| 1 | the base object: `CONFLICT-GRID(3, R)` | **forced** | 1 | the committed constructor |
| 2 | the per-round budget: 3 groups of 3 | **forced** | 1 | the committed cycle, driven |
| 3 | the site carrier: actors to the coarse sites | **forced** | 1 | the constructor's own actor naming |
| 4 | admissibility: the layer's own menu | **forced** | 1 | d42b1 driven directly |
| 5 | I7's readout and criterion | **forced** | 1 | HA, matched verbatim and recomputed |
| 6 | the split | **forced** | 1 | three independent routes agree: paper-04's arithmetic, paper-06's symmetry, the process's own seam |
| 7 | R = 6 rather than R = 4 | **declared, VERDICT-DETERMINING** | 1 | the pin; the R = 4 counterfactual is carried in every law row |
| 8 | the driven window W6 | **declared** | 1 | §2, disclosed in the head; the exhaustive columns do not use it |
| 9 | the seed rule | **declared** | 3 | the canonical transversals; the seed fan measures the record invariant across them |
| 10 | the reading axis (EMBEDDING / QUOTIENT) | **declared** | 2 | weld 2's, carried unchanged; every row stamped |
| 11 | **the completion of the 54 free links** | **measured** | **2 declared** | §6.5 — the process-supplied one is link-constant and keeps the weld motivated; paper-04's own declared minimal one is admissible and does not |
| 12 | the R = 9 cut control | **declared** | 1 | §6.3; outside the arena, two-way coverage only |
| 13 | the declared falsifier (one pair's divisions withheld) | **free** | — | this unit's; supplies STRUCT-DEAD and COUNT-DEAD |

One genuinely free item, instrument-side, touching no verdict; and one
**measured** item — the completion — which is reported as a relativity rather
than resolved.

---

## 11. The verdict

```
LOR-A-REFINEMENT-ACTS-[ONE LAWFUL STEP TAKEN AT THE R = 6 WELDED RECORD (2, 2, 2); PLACES 9 -> 36 SITES AND 27 -> 108 INTERVALS; NEW SITES 27 = 9 PER DIRECTION; DETERMINED 54, FREE 54; ADDITIVITY 27 OF 27, RESTRICTION 27 OF 27, READOUT 9 OF 9]@WINDOW-16-DRIVEN-OF-5,184-WITNESSES
```

```
LOR-A-LAWS-2-OF-3-NON-EMPTY-AND-THEY-COMPOSE<PAPER-06=UNIQUE-AT-27-OF-27-INTERVALS(FIBER-1|ORBITS-1|SIMPLEX-DIM-0|PINNED-TRANSITIVE)-AGAINST-9-OF-27-AT-R-4|PAPER-04=DYADIC-LIVE-RAW-FIBER-1-SUBDIVIDES-27-OF-27|PAPER-09=EMPTY-ALL-27-INTERVALS-IN-THE-SUPPORT-HOLE-[1, 2]|COMPATIBILITY=COMPOSE-AND-AGREE(06-SUPPORT-IS-04-WHOLE-FIBER-AT-27-OF-27;THE-TWO-ORDERS-AGREE-AT-108-OF-108-SLOTS;CONFLICT-FALSE)>
```

```
LOR-A-DICTIONARY-SURVIVES-AT-THE-EXTENDED-CARRIER-[ACTOR-PLUS-CO-DIVISION-PAIR-TO-SITE]<9+27=36|DETERMINED-LINKS-54-ARE-THE-54-ACTOR-IN-PAIR-INCIDENCES|FREE-LINKS-54-ARE-3-EACH-INSIDE-THE-18-NON-COLLINEAR-DECLARED-TRIANGLES -- THE-PROCESS-SUPPLIES-BOTH-HALVES:THE-SPLIT-BY-ITS-OWN-SEAM(1-LIVE-CUT-LOCUS-OF-17-AT-5,184-OF-5,184-WITNESSES;SPLIT-1-1-AT-27-OF-27)AND-THE-FREE-HALF-BY-ITS-DIVISION-FOOTPRINTS -- CARRIER-ISOMORPHISM-AT-72-OF-5,184-COUNTING-ONLY-AGAINST-864-WITH-THE-REFINED-LATTICES-EDGE-COUNT:THE-ABSTRACT-STRUCTURE-IS-CHEAPER-THAN-THE-DICTIONARY -- REFINED-WELD=FOUND-candidate@EMBEDDING+QUOTIENT<AUT-432|FIBERS-1/1/1|ZERO-FREE-ITEMS> -- COMPLETION-RELATIVE:PAPER-04S-OWN-DECLARED-MINIMAL-COMPLETION-IS-ADMISSIBLE-36-OF-36-BUT-UNMOTIVATED(FIBERS-24/3/2)>
```

```
LOR-A-CEILING-EXACTLY-1-STEP<FLOOR-LOG2-MIN-N=FLOOR-LOG2-2=1;AFTER-THE-STEP-MIN-N-1-CEILING-0 -- A-SECOND-STEP-NEEDS-MIN-N-4-=(4,4,4)-REACHABLE-ONLY-AT-R-12-BY-THE-BUDGET-LAW-R-3m -- LADDER-L-MAX-3x2^FLOOR-LOG2-m-WITH-EQUALITY-AT-THE-DYADIC-BUDGETS-[3, 6, 12, 24] -- SIG=DET-3-TO-3/4-EXACTLY-2^d-4|SIGNATURE-(+,+)-UNMOVED-36-OF-36|REFINED-DET-IS-PAPER-19S-COMMITTED-3/4 -- DIA=THE-DIAGONAL-BUYS-9-OF-THE-27-NEW-PLACES-AND-WITHOUT-IT-9-REFINED-SITES-LIE-ON-NO-COARSE-INTERVAL-ODD-ODD,PAPER-04S-d-3-MECHANISM-27-OF-216-ONE-DIMENSION-DOWN>
```

Read as a sentence: **the refinement laws act, exactly once, and what they
produce is the same record on four times as many places.** The step is forced
where the counting semantics forces it and free where paper-04 already
measured it to be free; the two live laws agree everywhere they are both
defined; and the process-to-space dictionary survives the step at an extended
carrier in which the new places are the old links — at a measured minority of
the arena's witnesses, and never merely because the shapes match.

---

## 12. Non-claims

- No continuum limit, no scaling limit, no invariant trajectory.
- **No cosmological or expansion reading of the place-count growth.** The new
  places are refined intervals of a pinned record and the sites inserted into
  them; no actor is created and nothing outside that structure is claimed.
- No claim that the process-supplied completion is *forced*. It is measured to
  exist, to be unique among link-constant completions, and to be the one under
  which the weld carries zero free items. Paper-04's own declared completion is
  equally admissible and does not.
- No claim that paper-06's finding is overturned. The pinned record layer still
  carries no positional datum; this unit locates the datum in the process and
  measures what the weld makes of it.
- The R = 9 cut census is a **control outside the declared arena**, carried for
  two-way coverage of one predicate and for nothing else.
- The ladder of §7 is computed from the ceiling law and the budget law; only
  its R = 6 row is driven, and the "places are logarithmically expensive"
  reading of it is a candidate reading.
- No dimension reading, no signature reading, no Lorentzian reading.
- Nothing here is citable before a hostile round confers terminal.

---

## 13. The successor register

- **LOR-B, the second step.** The arena theorem says a second refinement step
  needs R = 12 and the record (4, 4, 4). Whether the dictionary survives *two*
  steps — and whether the free half is supplied at level 2, where it is four
  times larger — is the next question, and it is posable exactly as this one
  was.
- **The completion, as a declaration.** This unit measures that the process
  supplies a completion and that it is the link-constant one. Whether a
  deeper grammar row *declares* a completion rule, making the choice a
  derivation rather than a coincidence, is a charter question.
- **The 792.** The witnesses with the right space and the wrong map are a
  measured class this unit only counts. What they are records *of* — whether
  the alternative isomorphisms carry any process meaning at all — is open.
- **The seam.** The cut is unique at R = 6 and tenfold at R = 9. Where between
  those the uniqueness fails, and whether it is the block structure or the
  count that carries it, is a one-parameter question.

---

## 14. The instrument

`v14/code/lor_exact.py` emits `lor_output.txt` and `lor_receipt.json`.
Interpreter `/opt/homebrew/bin/python3.13`. Exact arithmetic throughout: `int`
and `fractions.Fraction` only, with an AST scan of the source that admits no
float literal, no float-adjacent import and no true-division operator — the
single exact quotient in the file is formed from numerators and denominators.

Nineteen hash-pinned sources are read at run time and nothing else; no
subprocess is invoked and no repository state outside the declared set is
touched, so the plain run is correct off-tree and with no version control
present. Anchors are of three kinds: file-byte hashes; 31 (path, value) pairs
read out of five committed receipts, so a path drift that changed the arena
while preserving a hash dies by anchor; and 26 verbatim text anchors requiring
each sentence this unit quotes or reimplements to appear word for word in its
pinned source, evaluated before the byte anchors, each naming the gate it
licenses and each gate checked registered.

The falsifier census is a census of measured deaths: every declared mutant is
re-invoked by the delivery run itself, each must exit 1 at exactly the gate its
row declares with both artifacts byte-unchanged, and the survivor count is
computed rather than typed. Each falsifier's hook is located in the file's own
syntax tree, its source published in the receipt, and the object its row names
as corrupted is required to appear in that source; a corruption that is a
constant boolean is rejected. Gates without a declared mutant carry a
machine-readable forcing that says why they cannot fail.

The verdict is compared for complete equality against a reconstruction built
from the **serialized** receipt by a comparator that re-types every template
itself and shares no code and no input object with the builder. The paper
gates run in the plain run: every load-bearing sentence and every table row is
rendered from receipt cells and matched in the paper; the numeral scan covers
the whole object under test including fenced blocks and inline code spans, with
the fenced blocks gated by multiset equality against a declared copy count; the
head is matched verbatim; and a polarity probe searches for the negation of
each measured fate. Every published fraction carries a COUNTING-ONLY stamp.
The seal is total — every published receipt key is digested at the moment its
own gate passes or declared unsealed — the artifacts are written from the
sealed payload through `os.replace`, and integrity is disk-versus-seal with a
deliberately corrupted probe shown to be caught first. A run that fails any
gate writes nothing.

---

*Sources, hash-verified at run time:* `v14/note-lor-pin.md` (`5239c4671f1a`),
`v14/paper-21-r4dec.md` (`ef4a8c35a0c4`), `v14/code/r4dec_exact.py`
(`1958a8cdfe28`), `v14/code/r4dec_receipt.json` (`a4538c7019e6`),
`v14/paper-19-r3-weld.md` (`50bb81e67942`), `v14/code/r3_weld_receipt.json`
(`dfea664f2408`), `v14/paper-04-refinement-grammar.md` (`dfa5090f26b1`),
`v14/code/r6a_refinement_receipt.json` (`856f6e810ab5`),
`v14/paper-06-stochastic-split.md` (`c350caab17ee`),
`v14/code/crb_stochastic_receipt.json` (`5ebeec141303`),
`v14/paper-09-renewal-transport.md` (`006f96aaa2ff`),
`v14/code/r6bp_transport_receipt.json` (`9c8f8af07050`),
`v13/paper-ha-successor.md` (`f286ba10d2d9`),
`v13/code/ha_successor_receipt.json` (`542b8735daf0`),
`v10/code/d42b1_transport_exact.py` (`576275d55ecf`),
`v10/code/d60_crystal_exact.py` (`684cdb76552b`),
`v10/code/d66_arbitration_crystal_exact.py` (`3d0516ab106e`),
`v11/note-L1-lorentz-no-go-lemma.md` (`93ea24591c3c`),
`v11/note-v11p0a-reproduction-catalog.md` (`0cebe543e814`).
