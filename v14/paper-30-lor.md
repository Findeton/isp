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
LOR-A-DICTIONARY-SURVIVES-AT-THE-EXTENDED-CARRIER-[ACTOR-PLUS-CO-DIVISION-PAIR-TO-SITE]<9+27=36|DETERMINED-LINKS-54-ARE-THE-54-ACTOR-IN-PAIR-INCIDENCES|FREE-LINKS-54-ARE-3-EACH-INSIDE-THE-18-NON-COLLINEAR-DECLARED-TRIANGLES -- THE-PROCESS-SUPPLIES-BOTH-HALVES:THE-SPLIT-BY-ITS-OWN-SEAM(1-LIVE-CUT-LOCUS-OF-17-AT-5,184-OF-5,184-WITNESSES;SPLIT-1-1-AT-27-OF-27)AND-THE-FREE-HALF-BY-ITS-DIVISION-FOOTPRINTS -- CARRIER-ISOMORPHISM-AT-72-OF-5,184-COUNTING-ONLY-AGAINST-864-WITH-THE-REFINED-LATTICES-EDGE-COUNT:THE-ABSTRACT-STRUCTURE-IS-CHEAPER-THAN-THE-DICTIONARY -- REFINED-WELD=FOUND-candidate@EMBEDDING+QUOTIENT<AUT-432|FIBERS-1/1/1|ZERO-FREE-ITEMS> -- COMPLETION-RELATIVE:PAPER-04S-OWN-DECLARED-MINIMAL-COMPLETION-IS-ADMISSIBLE-36-OF-36-BUT-UNMOTIVATED(FIBERS-24/3-OR-6/2:LABEL-FIBER-BASE-MAP-VARIANT-SPREAD-[3, 6];FREE-AT-EVERY-BASE-MAP-3)>
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
| provenance | 19 hash-pinned sources; 33 (path, value) anchors read out of 6 committed receipts; 26 verbatim anchors |

The base object is d66's `CONFLICT-GRID(g = 3, R)`, driven directly: nine
actors on a 3 × 3 grid, each round spending the committed budget of three
conflict groups of three cells, each running one cycle of the committed
transport grammar. The variable is the schedule. The declared driven window
is disclosed in the head: **W6**, sixteen six-round schedules, six at the
surviving stratum, eight one per measured dead class, two at the declared seed
fan. That sentence is rendered from receipt cells and matched in this paper
with its numerals spelled, so a forged window cannot hide behind a spelling.
Every other column below is exhaustive over an object the window does not
cap — including the census that quantifies over all 5,184 witnesses and the
census that quantifies over all 280 round partitions.

The eight dead strata are exactly the eight dead classes of the 5,184-witness
census, so every one of the nine classes carries at least one schedule shown
reachable by the committed grammar: the census is class-wise grammar-realised,
9 of 9, and not merely combinatorial.

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

**Both facts are FORCED once §3.3 is in hand, and the register matters more
than the result.** At count 2 paper-04's dyadic fiber is a single point, and
paper-06's support is by construction a subset of it; a non-empty subset of a
one-point set is that set. So the agreement at 27 of 27 and the coincidence at
108 of 108 slots could not have come out otherwise, and at this arena
`CONFLICT-FALSE` carries no discriminating content — any non-empty
per-interval law would have agreed. The whole of stage 4 is a corollary of
stage 1. The first arena at which the comparison can fail is n = 4, where
paper-06's invariant simplex has dimension n − 2 = 2 and the dyadic fiber has
three points per interval; that is R = 12, and it is LOR-B's question, not
this unit's.

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
`CO-DIVISION-ACTOR-PAIR -> SITE` one level down.

At the R = 6 welded record (2, 2, 2), the one lawful refinement step inserts
exactly 27 new sites, and those sites are in canonical bijection with the 27
co-division pairs of actors — the coarse record's own links. **The
refinement's new places are the old links.** The old places remain actors: the
refined carrier is ACTOR ⊕ PAIR, 9 + 27 = 36.

That sentence is **witness-independent**, and so stronger than a statement
about the schedule this section builds on. I7-STRICTness forces every
witness's nine conflict groups to cover each of the 27 declared actor pairs
exactly once — this is the second of §3.1's two routes to 72 — so the
co-division relation is the same 27 objects at every one of the 5,184
witnesses, and the carrier map is the same bijection there. What is
witness-dependent is the *free* half: whether the process realises the 54 free
links as its own division footprints. That is the quantity the head stamps, at
72 of 5,184, and §6.4 censuses it.

**The process-side paraphrase, and the stamp it must travel with.** "The
refinement's new places are the old relationships" is a faithful rendering of
the object — an unordered co-division pair is an element of the co-division
relation, this unit's own arena row — but it is licensed only in the stamped
form: *the refinement's new places are the process's old co-division pairs,
the coarse record's own links, 27 for 27 at this arena; the old places remain
actors, so this is a mixed carrier and not a relational one.* The bare form
invites "places are relations", and the same measurement refutes that at this
very arena: the carrier is ACTOR ⊕ PAIR, three quarters pairs and one quarter
actors. The nine old places are not relations, and nothing measured here makes
them so.

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

**The counting settles it as a theorem, not only as a census.** Every conflict
group of an I7-STRICT triple is a declared triple, so each division event
deposits exactly 3 cell incidences — measured here over every group the 72
triples use — and a cut after k events distributes 3k over the 27 intervals.
Strict positivity of both halves at an all-count-n record needs 1 ≤ a ≤ n − 1
at each of the 27 cells, hence 27 ≤ 3k ≤ 27(n − 1). At n = 2 that is 3k = 27,
so k = 9 alone; at n = 3 it is the ten loci 9 to 18. The exhaustive census over
the 5,184 witnesses confirms the count rather than discovering it.

**And the count is a law of the budget.** Read off the block structure — fewer
than 9 groups cover fewer than 27 distinct declared pairs, so a cut before the
first block closes leaves an empty interval on the left, and symmetrically on
the right — at budget R = 3m the live cut loci are the integers in [9, 9(m -
1)], so their number is 9m - 17: one at m = 2, ten at m = 3 and nineteen at
m = 4. Both routes are computed in the run; the R = 9 control is taken across
a declared family of 1,728 three-block schedules rather than at one witness
and returns the same ten loci at every one of them; and the ladder from m = 2
to m = 6 is checked against the formula at 144 schedules per rung.

The predicate is not vacuous, and that control lies outside this unit's own
arena: at three blocks — R = 9, where the raw split fiber is 134217728 — ten
of the loci are live, so the process-supplied cut selects but does not
determine in general. R = 6 is the arena at which it determines, and the law
sharpens that to a stronger and less flattering statement: R = 6 is the *only*
arena at which it determines, because 9m - 17 = 1 has the single solution
m = 2. The uniqueness here is a boundary effect of the smallest
non-degenerate arena and not a determination property of the process. The
block structure carries it entirely; the count plays no role.

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
class is forced, not fitted. The fraction 72 of 5,184 here, and every other
fraction over the witness space this paper prints, is stamped COUNTING-ONLY:
no measure on the witness space is declared and no typicality claim rests on
any of them.

**And this is the result that was not anticipated.** Two of the dead classes
carry a relation that is *abstractly isomorphic* to the refined lattice — 432
isomorphisms at both readings, fibers 1/1/1, everything the RSQ standard asks
— while the canonical carrier on them is not an isomorphism and the field it
induces carries 27 zero cells at `triangles-9|lines-9` and 18 at
`triangles-12|lines-6`. Structural isomorphism is not the dictionary. A
witness can have the right space and the wrong map onto it, and 792 of the 864
right-shaped witnesses do.

The census behind that sentence is taken per witness and not per
representative. The abstract relation is a function of which declared
triangles and lines the schedule realises and of nothing else, so the 864
witnesses carrying the refined lattice's edge count fall into 12 distinct
shapes; each shape is searched for an isomorphism onto the refined lattice,
and every witness is accounted for. Measured: all 864 of the right-shaped
witnesses are abstractly isomorphic to the refined lattice, and the 792 whose
canonical carrier is not an isomorphism return the RSQ standard's own verdict
— `FOUND-candidate`, 432 isomorphisms, fibers 1/1/1, zero free items. The
class is therefore exactly *right space, wrong map*, with no shape-level
residue left to explain; and the slogan understates what was measured. The
standard by which this corpus has been declaring dictionaries does not
separate the 792 from the real one. Only the canonical, process-supplied
carrier does.

That is weld 2's blade turned around. Weld 2 censused its whole candidate list
and returned no FOUND and no SMUGGLED under either reading on structure alone,
one of its two blades being arity — 2 site objects against 9. Here structure,
up to and including the full zero-free-items verdict, is insufficient to
certify, and the same arity blade falls again one level down: 9 site objects
against 36. Structural shape is a sufficient disqualifier and an insufficient
qualifier. The dictionary was never the shape.

### 6.5 The weld of the refined record

Measured: at the process-supplied completion the refined weld returns
FOUND-candidate with 432 automorphisms and fibers 1/1/1, and under paper-04's
own declared minimal completion the same carrier returns UNMOTIVATED with
fibers 24/3/2.

Those three numbers are not read the same way, and the paper says so because
the receipt does. The site-assignment fiber 24 is a count over all base maps
and the orient fiber is 2 at every one; the label fiber is base-map-variant,
3 at 72 of the 432 base maps and 6 at the other 360, and the run publishes the
spread and the histogram. What is base-map-invariant is the **fate**: all
three inventory items are free at every one of the 432 base maps, so
UNMOTIVATED does not depend on the reading base map. On the process-supplied
side the fibers *are* base-map-invariant, and the run gates that too. The head
carries the spread rather than one base map's reading of it.

The scope of that measurement is also gated rather than left implicit. The
detector is run at one witness, and all 6 driven surviving-stratum schedules
are checked to induce the same process-side relation and the same completion
— so the verdict is a statement about the driven stratum and not about a
single schedule. The census of §6.4 and the cut census of §6.3 quantify over
all 5,184 witnesses independently of it.

The 432 is the automorphism group of the refined arena, and the fiber reading
carries over from paper-21's theorem because the refined relation is measured
here to be vertex- and edge-transitive: a count field invariant under all its
automorphisms is constant, and

> zero free items holds exactly at the link-constant records, and I7 declares
> none of them.

So the survival of the dictionary is **completion-relative**, and the two
declared completions differ exactly where it matters. Paper-04's own minimal
completion was designed to put each completed refined site on the diagonal
locus; measured here it reaches it at 18 of the 27 sites it completes — at the
9 diagonal-midpoint sites the known count is the diagonal one, so the rule's
own third branch returns (2, 2, 1) with $q_{12} = -3/2$ and $c = a + b$ is
arithmetically unreachable, since $a$ and $b$ would have to sum to 1. That is
the det spectrum §6.6 already records, read off the design rather than off the
outcome. It is admissible at all 36 sites and it makes the refined record
inhomogeneous — (1, 1, 1) at 9 sites, (1, 1, 2) at 18 and (2, 2, 1) at 9 — and
the weld on it carries three free items, and all three are free at every one
of the 432 base maps. The completion the **process** supplies is the
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

That agreement is a **forced record-vector identity** — not self-similarity,
and not a coincidence waiting on R = 12. Measured: the step's output is the record
vector (1, 1, 1) on 36 places — the same vector paper-19 committed on 9 places,
hence necessarily the same determinant 3/4. The chain closes at §3.3:
count 2 at every interval forces the split to the single point (1, 1), which
forces the refined record to be link-constant at 1, whose readout is
$[[1, -1/2], [-1/2, 1]]$ with determinant 3/4. Two objects with the same
record vector have the same determinant, so the agreement confirms nothing.
What *is* measured is that the refinement carries the record vector down a
level while quartering the determinant.

**Self-similarity is neither claimed nor licensed.** The refined object is not
isomorphic to the coarse one — 36 places against 9 — and §6.1's scope sentence
is the one that governs. A self-similar tower is a structure the ladder
permits and this unit does not drive: at n = 4 the split fiber has three
points per interval, so a tower would need a selection rule the record layer
has not been shown to carry. That is LOR-B's question.

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

*Structurally live* means every round saturating — depositing the maximum 9
link incidences, which §3.1 measures exhaustively over all 280 round
partitions, so the bound binds at every $R$. The second clause then costs one
line: $m$ saturating rounds deposit $27m$ incidences and a homogeneous
$(n, n, n)$ needs $27n$, so $n = m$.

| m | R = 3m | record | ceiling | refined side | places |
|---|---|---|---|---|---|
| 1 | 3 | (1, 1, 1) | 0 | 3 | 9 |
| 2 | 6 | (2, 2, 2) | 1 | 6 | 36 |
| 3 | 9 | (3, 3, 3) | 1 | 6 | 36 |
| 4 | 12 | (4, 4, 4) | 2 | 12 | 144 |
| 8 | 24 | (8, 8, 8) | 3 | 24 | 576 |

Read plainly, and this is a candidate reading of the ladder rather than a
measurement beyond it: **refinement DEPTH is exponentially expensive and
PLACES are quadratically cheap.** Concretely: each further level of refinement
costs a doubling of the process — k levels need R = 3 × 2^k rounds — while at the
dyadic budgets the reachable place-count is exactly R^2: 9 at R = 3, 36 at
R = 6, 144 at R = 12, 576 at R = 24. The process buys at most one unit of
refined lattice length per round; the logarithm governs the depth and never
the places.

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
that enforces its absence whitespace-normalises, ASCII-folds, case-folds and
strips markdown prefixes from both sides — as does the polarity probe, since
both are constraints on a *forbidden* string and a sentence-initial capital
would otherwise walk through either.

**BHS — no sprinkling-grade Lorentz-invariance test.** A Poisson sprinkling
admits no Lorentz-invariant finite-valency graph and these records are
finite-valency by construction, so running the test would manufacture a false
negative. None is run, and the abstention is measured on **two legs**: this
run's declared measurement surface — every measured receipt key together with
every gate's statement and evidence — and the object under test itself, both
scanned with the same declared needles, with a falsifier that writes such a
reading into the paper leg and dies there.

**Kleitman–Rothschild — no dimension reading, so no height control is owed.**
No chart width, no Myrheim–Meyer estimate, no max-shatter reading is taken;
the same two legs are scanned and the same kind of falsifier is carried.

**No cosmological reading.** Refinement here is a measured operation on a
pinned record. It is not an expansion narrative, and nothing about the growth
of the place-count licenses one. Both legs are scanned for an
expansion-of-space reading; one falsifier writes one into this paper and
another writes one into the surface, and both die there.

**How the paper leg reads a wall's own denial.** A wall necessarily names the
topic it declines, so the three paragraphs above and the matching non-claim in
§12 are declared to the instrument as **abstention windows**: each must be
present in this paper word for word, each has its occurrence count published,
and they are the only text removed before the needles are run over everything
else. No other strip exists. A banned reading written anywhere outside those
four windows dies at the wall that owns it — which is what a constraint on the
artifact a reader actually reads has to mean.

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
| 11 | **the completion of the 54 free links** | **measured** | **2 declared** | §6.5 — the process-supplied one is link-constant and keeps the weld motivated; paper-04's own declared minimal one is admissible at 36 of 36 and does not, and its label fiber is base-map-variant with spread [3, 6] while all 3 inventory items are free at every one of the 432 base maps |
| 12 | the R = 9 cut control | **declared** | 1 | §6.3 — run across 1,728 three-block schedules, outside the arena |
| 13 | the declared falsifier (one pair's divisions withheld) | **free** | — | this unit's; supplies STRUCT-DEAD and COUNT-DEAD |
| 14 | **the extended carrier `SITE <- ACTOR (+) CO-DIVISION-PAIR`** | **declared, VERDICT-DETERMINING** | **1 tried; alternative 36-object carriers uncensused** | §6.2 — the necessity is forced (the 9-actor carrier is ARITY-DEAD against 36 sites); the objects are the committed dictionary's second clause re-typed, not invented |

Every row above is rendered from a receipt cell and matched in this paper, so
the RSQ standard's own instrument is no longer unrendered prose.

Three classes, not two. One genuinely **free** item, instrument-side, touching
no verdict; one **measured** item — the completion — reported as a relativity
rather than resolved; and one **declared and verdict-determining** item, the
extended carrier of §6.2. Its *necessity* is forced and measured: nine actors
cannot carry thirty-six sites, and the detector's own reason is structural — a
declared restriction can only shrink a site set — so the death of the bare
carrier is not a failed search. Its *choice* is not: exactly one 36-object
carrier was constructed and tested, and no census of alternative extensions
exists anywhere in this run. What makes the extension canonical rather than
arbitrary is that its objects are not invented here — they are the committed
dictionary's own second clause, `CO-DIVISION-ACTOR-PAIR -> LINK`, re-typed
onto sites one level down. That makes it canonical. It does not make it
censused, and no uniqueness is claimed for it.

---

## 11. The verdict

```
LOR-A-REFINEMENT-ACTS-[ONE LAWFUL STEP TAKEN AT THE R = 6 WELDED RECORD (2, 2, 2); PLACES 9 -> 36 SITES AND 27 -> 108 INTERVALS; NEW SITES 27 = 9 PER DIRECTION; DETERMINED 54, FREE 54; ADDITIVITY 27 OF 27, RESTRICTION 27 OF 27, READOUT 9 OF 9]@WINDOW-16-DRIVEN-OF-5,184-WITNESSES
```

```
LOR-A-LAWS-2-OF-3-NON-EMPTY-AND-THEY-COMPOSE<PAPER-06=UNIQUE-AT-27-OF-27-INTERVALS(FIBER-1|ORBITS-1|SIMPLEX-DIM-0|PINNED-TRANSITIVE)-AGAINST-9-OF-27-AT-R-4|PAPER-04=DYADIC-LIVE-RAW-FIBER-1-SUBDIVIDES-27-OF-27|PAPER-09=EMPTY-ALL-27-INTERVALS-IN-THE-SUPPORT-HOLE-[1, 2]|COMPATIBILITY=COMPOSE-AND-AGREE(06-SUPPORT-IS-04-WHOLE-FIBER-AT-27-OF-27;THE-TWO-ORDERS-AGREE-AT-108-OF-108-SLOTS;CONFLICT-FALSE)>
```

```
LOR-A-DICTIONARY-SURVIVES-AT-THE-EXTENDED-CARRIER-[ACTOR-PLUS-CO-DIVISION-PAIR-TO-SITE]<9+27=36|DETERMINED-LINKS-54-ARE-THE-54-ACTOR-IN-PAIR-INCIDENCES|FREE-LINKS-54-ARE-3-EACH-INSIDE-THE-18-NON-COLLINEAR-DECLARED-TRIANGLES -- THE-PROCESS-SUPPLIES-BOTH-HALVES:THE-SPLIT-BY-ITS-OWN-SEAM(1-LIVE-CUT-LOCUS-OF-17-AT-5,184-OF-5,184-WITNESSES;SPLIT-1-1-AT-27-OF-27)AND-THE-FREE-HALF-BY-ITS-DIVISION-FOOTPRINTS -- CARRIER-ISOMORPHISM-AT-72-OF-5,184-COUNTING-ONLY-AGAINST-864-WITH-THE-REFINED-LATTICES-EDGE-COUNT:THE-ABSTRACT-STRUCTURE-IS-CHEAPER-THAN-THE-DICTIONARY -- REFINED-WELD=FOUND-candidate@EMBEDDING+QUOTIENT<AUT-432|FIBERS-1/1/1|ZERO-FREE-ITEMS> -- COMPLETION-RELATIVE:PAPER-04S-OWN-DECLARED-MINIMAL-COMPLETION-IS-ADMISSIBLE-36-OF-36-BUT-UNMOTIVATED(FIBERS-24/3-OR-6/2:LABEL-FIBER-BASE-MAP-VARIANT-SPREAD-[3, 6];FREE-AT-EVERY-BASE-MAP-3)>
```

```
LOR-A-CEILING-EXACTLY-1-STEP<FLOOR-LOG2-MIN-N=FLOOR-LOG2-2=1;AFTER-THE-STEP-MIN-N-1-CEILING-0 -- A-SECOND-STEP-NEEDS-MIN-N-4-=(4,4,4)-REACHABLE-ONLY-AT-R-12-BY-THE-BUDGET-LAW-R-3m -- LADDER-L-MAX-3x2^FLOOR-LOG2-m-WITH-EQUALITY-AT-THE-DYADIC-BUDGETS-[3, 6, 12, 24] -- SIG=DET-3-TO-3/4-EXACTLY-2^d-4|SIGNATURE-(+,+)-UNMOVED-36-OF-36|REFINED-DET-IS-PAPER-19S-COMMITTED-3/4 -- DIA=THE-DIAGONAL-BUYS-9-OF-THE-27-NEW-PLACES-AND-WITHOUT-IT-9-REFINED-SITES-LIE-ON-NO-COARSE-INTERVAL-ODD-ODD,PAPER-04S-d-3-MECHANISM-27-OF-216-ONE-DIMENSION-DOWN>
```

Read as a sentence: **the refinement laws act, exactly once, and what they
produce is the same record on four times as many places.** The step is forced
where the counting semantics forces it and free where paper-04 already
measured it to be free; the two live laws agree everywhere they are both
defined — forced here by the point fiber, and so without discriminating
content at this arena (§5); and the process-to-space dictionary survives the
step at an extended carrier in which the new places are the old links — at a
measured minority of the arena's witnesses, and never merely because the
shapes match.

And the register of the whole unit is worth stating plainly, because
everything that comes out forced at R = 6 is forced by the same smallness:
n = 2 makes the split a point and paper-06 unique by triviality, and m = 2
makes the seam unique. What is achieved here is that the refinement *acts at
all* and that the dictionary survives at an extended carrier — not that the
acting is uniquely determined by the law. The first arena at which any of
these has a fiber to choose from is R = 12.

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
  its R = 6 row is driven, and the depth/places scaling read off it — depth
  exponential in the budget, places quadratic — is a candidate reading.
- No discriminating content is claimed for `CONFLICT-FALSE`. At this arena the
  agreement of the two laws is forced by the point fiber (§5); the first arena
  at which it could fail is R = 12.
- No uniqueness is claimed for the extended carrier, and no alternative
  36-object carrier is censused (§10, row 14).
- No dimension reading, no signature reading, no Lorentzian reading.
- Nothing here is citable before a hostile round confers terminal.

---

## 13. The successor register

- **LOR-B, the second step.** The arena theorem says a second refinement step
  needs R = 12 and the record (4, 4, 4). Whether the dictionary survives *two*
  steps — and whether the free half is supplied at level 2, where it is four
  times larger — is the next question, and it is posable exactly as this one
  was. Its arity bookkeeping is already forced: at level k the lattice has
  side $3\cdot 2^k$, so sites are $(3\cdot 2^k)^2$ and links are 3 times the
  sites, hence sites at level k+1 equal sites plus links at level k exactly —
  36 = 9 + 27 here, and 144 = 36 + 108 at R = 12. *If* a carrier exists at
  every level it must be `SITE_(k+1) <- SITE_k (+) LINK_k`. The arity is a
  theorem; the dictionary's survival is not.
- **The completion, as a declaration.** This unit measures that the process
  supplies a completion and that it is the link-constant one. Whether a
  deeper grammar row *declares* a completion rule, making the choice a
  derivation rather than a coincidence, is a charter question.
- **The 792.** §6.4 now measures that all 864 right-shaped witnesses are
  abstractly isomorphic to the refined lattice, so the class is exactly *right
  space, wrong map* with no shape-level residue to explain; what distinguishes
  them is the process fact of which conflict groups are lines, and that
  mechanism is already exact. What they are records *of* — whether the
  alternative isomorphisms carry any process meaning at all — is open.
- **The seam — CLOSED, at §6.3.** There is no interior, because m is an
  integer: the live loci are the integers in [9, 9(m - 1)] and their number is
  9m - 17. The block structure carries it entirely and the count plays no
  role, so the uniqueness at R = 6 is a boundary effect of the smallest
  non-degenerate arena. The successor question is the next one: when the
  process supplies nineteen live loci at R = 12, does it still supply a
  *canonical* one — is the balanced cut distinguished by anything the record
  layer carries?

---

## 14. The instrument

`v14/code/lor_exact.py` emits `lor_output.txt` and `lor_receipt.json`.
Interpreter `/opt/homebrew/bin/python3.13`. Exact arithmetic throughout: `int`
and `fractions.Fraction` only, with an AST scan of the source that admits no
float literal, no float-adjacent import and no true-division operator — the
single exact quotient in the file is formed from numerators and denominators.

Nineteen hash-pinned sources are read at run time; besides them the run reads
only this file itself, the object under test, and the two files it stages for
writing — and every read is categorised at its call site, with the whole
category set held against its own declaration at the end of the run, so a read
of mutable repository state added anywhere in the file cannot survive. No
subprocess is invoked, so the plain run is correct off-tree and with no version
control present. Anchors are of three kinds: file-byte hashes; 33 (path, value)
pairs read out of 6 committed receipts, so a path drift that changed the arena
while preserving a hash dies by anchor; and 26 verbatim text anchors requiring
each sentence this unit quotes or reimplements to appear word for word in its
pinned source, evaluated before any source byte is used for a measurement,
each naming the gate it licenses and each gate checked registered.

The falsifier census is a census of measured deaths: every declared mutant is
re-invoked by the delivery run itself, each must exit 1 at exactly the gate its
row declares, and the survivor count is computed rather than typed. The
in-process sweep never writes, so byte-unchangedness under mutation is asserted
there and measured out of harness, one process per mutant. Each falsifier's
hook is located in the file's own syntax tree, its source published in the
receipt, and the object its row names as corrupted is required to appear in
that source; a corruption that is a constant boolean is rejected. Gates without
a declared mutant carry a machine-readable forcing that says why they cannot
fail.

Every published total is held against its own registry's length — gates
against the declared registry, seals against the declared seal set, sources,
mutants, verbatim and (path, value) anchors against their own declarations — so
no typed count and no typed offset survives. Every gate this run evaluates
publishes its own row in the receipt except the two that structurally cannot,
the gate that closes the seal and the gate that checks the bytes the receipt
becomes; those two are declared and the difference is measured against the
declaration.

The verdict is compared for complete equality against a reconstruction built
from the **serialized** receipt by a comparator that re-types every template
itself and shares no code and no input object with the builder. The paper
gates run in the plain run: every load-bearing sentence and every row of all
six tables is rendered from receipt cells and matched in the paper; the numeral
scan covers the whole object under test — prose, tables, inline code spans,
section references, heading numbers and the fenced verdict blocks, the fenced
blocks gated by multiset equality against a declared copy count, the spelled
numerals read through nineteen and through the hyphenated compounds — and the
only text removed before the scan is the backticked sha256-12 spans, every one
of which must be one of the declared source digests. The head is matched
verbatim; a polarity probe searches for the negation of each measured fate;
the reading walls scan the declared measurement surface **and this paper**,
with the walls' own denials declared as abstention windows that must be present
and must fire; and every fraction over a declared configuration space is
scanned for in the paper and required to carry a COUNTING-ONLY stamp, with the
assertive typicality words searched for directly.

The seal is total — every published receipt key is digested at the moment its
own gate passes or declared unsealed — the artifacts are written through
`os.replace` from an object identical to the sealed payload but for the one key
carrying the payload's own digest, and integrity is disk-versus-seal: the
receipt is read back and every sealed object compared against its gate-time
digest, and the transcript is split at its sealed prefix, whose digest must
match, with the remainder required to equal the closing gates' lines
re-rendered from the ledger — so every line of both artifacts is covered, with
a deliberately corrupted probe of each shown to be caught first. A run that
fails any gate writes nothing.

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
