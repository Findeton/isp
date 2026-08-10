# The schedule census

**U4b / paper-17.** Pin `v14/note-u4b-pin.md` (FROZEN, sha256-12
`d2cff9a274a8`, ledger #126, frozen at commit `42417f6`). Code
`v14/code/u4b_schedule_exact.py`; artifacts
`v14/code/u4b_schedule_output.txt`, `v14/code/u4b_schedule_receipt.json`.

**Verdict.**

```
U4B-CRYSTAL-GENERIC-[beyond-coset 1/32; 1749600 of 55987200; <(0,1)>|<(1,0)>|<(1,1)>|<(1,2)>]
```

**Determinant segment**, independent of the first.

```
DET-NONZERO-EXISTS-[ROW|ROW/DIAG: det=-1 at 9 of 9; 747 of 78400 pairs; POSDEF-EMPTY; I7-STRICT-EMPTY]
```

**Constructibility census.**

```
CONSTRUCTIBILITY-[FORCED 11664 of 11664; BRANCHING 0; REFUSED 0]@WINDOW-11664-OF-57153600+20-STRATUM-WITNESSES
```

Between delivery and adjudication every headline reading here is a
candidate reading.

---

## 1. The question

U4 measured the division-event crystal TRUE, and its panel then proved
the periodicity constructor-inherited. The U4 adjudication (`fa991e19ae54`,
ledger #125) states the mechanism verbatim:

> at all ten cells the division field is affine in the constructor's seed
> set — n = c + m·1_S — so Stab(n) = Stab(1_S)

with S a union of full ⟨(1,1)⟩ cosets because the committed constructor
seats its seeds at a uniform column offset. The diagonal was d66's seed
rule, not a property of division events.

This unit turns the constructor into a variable. Over the declared family
of admissible arbitration schedules on the committed grid — the
diagonal-coset seed one point in that family, not its generator — does
crystallinity survive only at coset-union seeds, or does it appear at
seeds that are not coset unions at all? And does any schedule in the
family induce a non-degenerate metric?

Both answers came back positive, and the second came back with a
restriction nobody asked for.

## 2. The family, declared as data (RUNBOOK §15)

### 2.1 The base structure, taken from the committed constructor

The base object is d66's `CONFLICT-GRID(g = 3, R = 2)` (`3d0516ab106e`).
Nine actors sit on a 3 × 3 grid, so the actor names parse as a bijection
onto Z_3^2 and this unit assigns no site. There are 2 rounds. Each round
spends the committed budget: 3 conflict groups of 3 cells each,
partitioning the grid. Each group runs one cycle of the committed
transport grammar — the conflict-supply deliveries from the group's seed
to any member that does not already hold the base, then 3 proposals (0
for the seed, 1 for the rest), then one 3-proposer arbitration won by the
seed. d66 says of this cycle:

> each group is a g-PROPOSER conflict (g + 1 registers) whose base is
> supplied by g - 1 deliveries from the group's diagonal seed

Groups are processed in ascending order of their seed's site index and
members in ascending site index, which is d66's own order at the
committed schedule.

### 2.2 The variable

The pin's family is

> all grammar-admissible choices of which cell-pairs arbitrate per round,
> at the committed budget

and at this budget the co-arbitration relation of a round is exactly a
partition of the 9 cells into three triples. A schedule is therefore a
pair of such partitions, one per round, each with a seed chosen in each
of its groups.

The count is computed, not asserted, by two routes that share no code:
enumeration returns 280 partitions of the nine sites into three triples,
27 seed assignments per partition, hence 7560 schedules per round; the
closed form 9!/(3!^3 · 3!) × 3^3 returns the same. Squared over the two
rounds, the family has 57153600 schedules. The committed schedule — round
0 on the row class, round 1 on the column class, diagonal seeds in both —
is one of them.

### 2.3 The generalized driver is the committed constructor

Admissibility is never decided by fiat here. The committed d42b1
transport layer (`576275d55ecf`) enters this program as a single source —
a text slice cut at the layer's own banner print — and `candidates_for`,
the layer's own menu function, is what decides every event. d60's builder
and d66's `conflict_grid` enter by AST extraction of their def and class
bodies, so no module-level statement of theirs can run, and the strip is
gated rather than asserted.

The generalized driver is then anchored against the object it
generalizes: at the committed schedule it and d66's own
`conflict_grid(3, 2)`, re-run in this process, emit **identical event
lists** — 30 events, 6 division events, every specification matched by
exactly one menu candidate, no refusal. Three further numbers are READ
from committed files at run time and reproduced rather than re-typed:
d66's own output rows for GRID(g=3,R=4) and GRID(g=3,R=6) — 66 events, 12
arbitrations, 18 deliveries; and 102, 18, 30 — and the U4 effectus
review's CONFLICT-GRID(3,2) row in I7 coordinates, 1, 1, 0, 1, 1, 1, 0,
reproduced by this unit's own readout.

### 2.4 The declared window, disclosed here and in the head

Driving the layer's menus over 57153600 schedules is not affordable.
Grammar-admissibility is therefore decided exhaustively on a **declared
window**: both rounds' groupings drawn from the 4 parallel classes of
AG(2,3) — the resolvable device d66's own constructor uses — with the
seeds free. In numbers, the declared window has 11664 schedules, 1/4900 of the family,
and it contains the committed schedule. The window is named inside
the constructibility verdict string, so no reader can meet the number
without meeting its scope.

**Every other column below is exhaustive over the whole family.** The
stabilizer and the determinant are functions of the schedule alone —
§4.2 gates that equality against the driven records — so they are
computed over all 57153600 schedules by exact enumeration of the objects
they actually depend on, with no window at all.

## 3. Constructibility

Each of the 11664 window schedules is built by driving the menus and is
scored against its own record, not against an aggregate.

| fate | count |
|---|---|
| FORCED | 11664 |
| BRANCHING | 0 |
| REFUSED | 0 |

Every record carries exactly 6 division events, every specification is
offered exactly once, and no step anywhere is refused. The record length
is a clean dichotomy: 2916 schedules of 24 events and 8748 of 30. The
reason is measured, not assumed — a round-1 group needs no conflict
supply exactly when its three members already share a base, i.e. exactly
when it repeats a round-0 group, which happens for the 4 class pairs that
use the same class twice.

**The two negative fates are reachable, and the instrument sees them.**
Without controls, "FORCED everywhere" would be a structural tautology
rather than a measurement, so two are declared and run.

- *The no-supply control.* The committed schedule with its
  conflict-supply deliveries suppressed. The layer refuses the first
  round-1 proposal by an actor that does not hold the base: refusal
  `propose G10` at prefix 13, after 13 events. A refusal is recorded,
  never patched.
- *The under-specified control.* The committed record replayed to prefix
  3, where d60's `pick` is asked for an arbitration by G00 without naming
  its conflict key and winner key. 7 menu candidates match, so the
  builder's own maxhits reads 7 and the fate is BRANCHING.

Only the candidate COUNT is reported for the second control, and that is
deliberate. d60's `pick` breaks ties with `sorted(key=repr)`, and the
`repr` of a frozenset depends on the interpreter's per-process string
hashing, so *which* candidate an under-specified pick selects is not
reproducible across runs. Every event of every schedule in this census is
specified by its full tuple, where at most one candidate can match and
the tie-break is never consulted; the control stops at its first
under-specified pick and no record is continued past one.

**Twenty strata witnesses, driven outside the window.** The census of §4
to §6 stratifies the whole family by (stabilizer × affine class ×
non-degeneracy). All 20 nonempty strata are given a deterministic
representative — first in a fixed enumeration, no sampling — and every
representative's record is built by driving the menus. All 20 are FORCED.
So the grammar's verdict has been taken at least once in every cell of
the census, including cells whose partitions are not parallel classes at
all.

## 4. The stabilizer column

The division-event field is `n : Z_3^2 → Z≥0`, and its translation
stabilizer is `Stab(n) = { t : n(x + t) = n(x) for every x }`. Both site
readings U4 declared are run.

### 4.1 The footprint reading is a census artifact

At the footprint reading — every actor in the arbitration's register
footprint — the footprint field is the constant 2 at every site of every
schedule, checked on each of the 11664 driven records separately. Its
stabilizer is Z_3^2 identically, for the whole family.

The reason is the budget itself: each round's three conflict groups
partition the nine cells, so every cell lies in exactly one footprint per
round. This is the constant-field vacuous positive the U4 adjudication
named at two of its ten cells, and the census shows it is not a property
of those two crystals but of every schedule the committed budget admits.
**The footprint reading carries no information about the schedule, and
nothing below is read off it.**

### 4.2 The initiator reading

At the initiator reading the field is `1_{S0} + 1_{S1}`, where `S_r` is
the round-r seed set. Two facts make the column exhaustive over the whole
family without a window.

First, for every one of the 11664 window schedules the field read off the
DRIVEN record — initiators from `op[1]`, footprints from `regs_of`
intersected with the actor set — equals the field the combinatorial route
computes from the schedule alone. Zero mismatches.

Second, every one of the 84 three-element subsets of Z_3^2 is a
transversal of exactly 90 of the 280 partitions. That weight is uniform —
measured, not assumed — so the 7056 ordered seed-set pairs carry the
entire census with a single multiplicity.

| Stab | seed pairs | schedules |
|---|---|---|
| 1 | 6804 | 55112400 |
| ⟨(1,0)⟩ | 63 | 510300 |
| ⟨(0,1)⟩ | 63 | 510300 |
| ⟨(1,1)⟩ | 63 | 510300 |
| ⟨(1,2)⟩ | 63 | 510300 |

So 2041200 of 57153600 schedules are crystalline at the initiator
reading, a rate of 1/28. The full group never occurs: 6 division events
cannot spread evenly over 9 sites.

Each stabilizer is computed three times by routes sharing no code and no
typed constant — translation of the field; the annihilator of the support
of the exact Z_3^2 Fourier transform in `Z[w] = Z[t]/(t^2 + t + 1)`,
running over the dual group; and a walk of the subgroup lattice taking
the largest H on whose cosets the field is constant. The three agree
element for element at all 7056 objects.

## 5. The determinant column

The pin makes this a first-class outcome segment:

> any schedule with det ≠ 0 at all sites is the corpus's first
> non-degenerate grammar-generated geometry carrier

### 5.1 The readout

The route is the U4 effectus review's (`61fb7d9e8471`), which evaluates
U4's bridges in I7's coordinates (paper-13 SEC 2.1): sites Z_3^2, links
{(1,0), (0,1), (1,1)}, and HA 3.2's declared readout

> `q₁₁ = n_{e₁}`, `q₂₂ = n_{e₂}`, `q₁₂ = (n_{e₁+e₂} − n_{e₁} − n_{e₂})/2`

applied to the co-division adjacency — for a link l and a site x, the
number of division events whose footprint contains both x and x + l. HA
3.2 says what that readout is:

> The readout is an invertible linear re-encoding: in count coordinates,
> the record IS the metric.

Every component and every determinant below is an exact `Fraction`. The
route is validated by reproducing the effectus's committed
CONFLICT-GRID(3,2) row exactly: at the committed schedule q11 = 1,
q22 = 1, q12 = -1 and det = 0, the degenerate form whose kernel is the
diagonal.

### 5.2 The answer

Over the whole family, 747 of the 78400 partition pairs carry det ≠ 0 at
all nine sites — 544563 of 57153600 schedules. The determinant column
depends on the groupings only — the seeds move the initiators, not the
footprints — which is why it is counted on partition pairs, each carrying
729 seed choices.

**The witness, by name.** In the head, the named witness is ROW|ROW/DIAG
— the committed constructor with round 1's column class replaced by the
row class again, i.e. **the schedule that never rotates its conflict
groups**, with the committed diagonal seeds. It induces

```
q = [[ 0, -1],
     [-1,  2]]      det = -1   at 9 of 9 sites
```

the same form at every site. It lies in the declared window and its
record is FORCED. This is the corpus's first non-degenerate
grammar-generated geometry carrier.

The sixteen resolvable class pairs are all homogeneous, and each row's
non-degeneracy count is required to equal the number the exhaustive
78400-pair census independently assigns to that pair:

| round 0 | round 1 | q11 | q22 | q12 | det | non-degenerate sites |
|---|---|---|---|---|---|---|
| ROW | ROW | 0 | 2 | -1 | -1 | 9 |
| ROW | COL | 1 | 1 | -1 | 0 | 0 |
| ROW | DIA | 0 | 1 | 0 | 0 | 0 |
| ROW | ANT | 0 | 1 | -1/2 | -1/4 | 9 |
| COL | ROW | 1 | 1 | -1 | 0 | 0 |
| COL | COL | 2 | 0 | -1 | -1 | 9 |
| COL | DIA | 1 | 0 | 0 | 0 | 0 |
| COL | ANT | 1 | 0 | -1/2 | -1/4 | 9 |
| DIA | ROW | 0 | 1 | 0 | 0 | 0 |
| DIA | COL | 1 | 0 | 0 | 0 | 0 |
| DIA | DIA | 0 | 0 | 1 | -1 | 9 |
| DIA | ANT | 0 | 0 | 1/2 | -1/4 | 9 |
| ANT | ROW | 0 | 1 | -1/2 | -1/4 | 9 |
| ANT | COL | 1 | 0 | -1/2 | -1/4 | 9 |
| ANT | DIA | 0 | 0 | 1/2 | -1/4 | 9 |
| ANT | ANT | 0 | 0 | 0 | 0 | 0 |

Nine of the sixteen are non-degenerate everywhere, which is why 6561 of
the 11664 window schedules are.

### 5.3 What the carrier is not

**It is never Riemannian.** Exhaustively over all 78400 partition pairs,
the maximum number of positive-definite sites is 3 — never 9. The
mechanism is a budget, and it is worth stating because it is a property
of the committed cycle rather than of these particular groupings: a
partition into three triples has 9 within-group pairs, and only those
whose difference direction lies in I7's link set contribute, so the two
rounds deposit at most 18 link-incidences over the 9 sites. Positive
definiteness at a site needs q11 > 0, q22 > 0 and
4·q11·q22 > (n_(1,1) - q11 - q22)^2, hence at least 3 incidences at that
site, hence at least 27 in all. 18 < 27, and the exhaustive census agrees.

**I7's own admissibility is empty for the same reason:** no partition pair
makes all 27 link counts strictly positive. So no schedule in this
family is an admissible I7 geometry record. The U4 effectus predicted the
renewal-crystal weld census EMPTY from the vanishing diagonal; the census
records it EMPTY, but the cause is larger than the diagonal — it is the
link budget, and it would survive any redistribution of the same 18
incidences.

**The signature is not constant across the family, and not always
constant within a schedule.** Of the 747 non-degenerate pairs, 261 carry
det < 0 at all nine sites and 486 carry both signs. Across the cells
of those pairs the determinant takes the value -1 at 855 cells, -1/4 at
5238, 1 at 108 and 3/4 at 522. Where det > 0 the form is positive
definite; that happens, but never at more than 3 sites of one schedule.

## 6. The affine null, and what survives it

The pin supplies the null hypothesis: a schedule whose seed sets are
coset unions is crystalline by the affine law and carries no emergence
information. Since a seed set has 3 elements and the nontrivial subgroups
of Z_3^2 have order 3, "coset union" means "a line of AG(2,3)", and the
classification is three-valued.

| class | schedules | crystalline | rate |
|---|---|---|---|
| CU-JOINT (both seed sets cosets of one H) | 291600 | 291600 | 1 |
| CU-SPLIT (both cosets, different H) | 874800 | 0 | 0 |
| BEYOND-COSET (at least one not a coset) | 55987200 | 1749600 | 1/32 |

**The null holds exactly where it is predicted to:** every one of the 36
CU-JOINT seed pairs is crystalline, evaluated on its own field, with Stab
containing the common H. That is the U4 adjudication's mechanism
read as a prediction and confirmed.

**It holds nowhere else among the coset seeds:** none of the 108 CU-SPLIT
seed pairs is crystalline. Two lines of different directions meet in
exactly one point, so the field takes the value 2 at a single site, and
no order-3 period can carry a value that occurs once.

**And crystallinity is not confined to the inherited locus.** 216 of the
6912 beyond-coset seed pairs carry a nontrivial stabilizer: 1749600 of
the 55987200 beyond-coset schedules are crystalline, a rate of 1/32,
realizing all four order-3 subgroups. The mechanism is measured rather
than inferred. In these schedules the field takes the value 1 on a union
of two H-cosets and 0 on the third, while neither seed set is an H-coset;
the two seed sets partition six sites between them without either one
respecting the period. **The period is a property of the pair, not of
either seed** — which is precisely what the affine reading of a single
seed set cannot produce.

The strongest cell is the intersection: 19791 schedules are both
crystalline and non-degenerate at all nine sites, and 17118 of those are
beyond-coset.

## 7. Fragility

A single-arbitration re-seating moves exactly one division event to
another cell of its own conflict group. It is the smallest edit that
keeps the schedule inside the family, and there are 12 of them at every
schedule — 6 arbitrations by 2 alternative seats — each itself an
admissible member of the window whose record has been driven.

Measured on the 540 crystalline schedules of the window, each against its
own edits: all 12 admissible single-arbitration re-seatings break the
stabilizer, at every one of them. The census is a single cell.

The mechanism is one line. The edit changes the field by
`1_new - 1_old`, and a difference of two distinct point masses is never
constant on the cosets of an order-3 subgroup, so no edit can preserve a
period. **The crystal is maximally fragile wherever it occurs.** Read
with §6 this is the census's sharpest statement about the object: the
crystallinity that is not constructor-inherited is not robust either — it
is a coincidence of two seed sets that a single re-seating destroys.

## 8. The walls

The pin inherits four walls from U4 verbatim. Violations of them would be
construction errors, not findings.

**L-1 — argued before any test, then declined.** L-1 (`93ea24591c3c`)
records that order-level covariance is a

> fourth form, outside paper 8's three**, and its admissibility is v11's
> to argue when U4 runs

The argument owed is prior to any test and it is this. Admissibility
would require a group declared to act on the generated causal order and a
reason to read that group as a covariance group. This arena supplies
finite records and a translation action on their *site lattice*; the
corpus contains no bridge from Z_3^2 translations to any boost, and this
unit constructs none. **The fourth form is not tested here.** What is
measured falls inside L-1's own scope guard: the Z_3^2 translation
stabilizer is a permutation action on the actor set, which needs no
fourth-form argument at all. The sentence retracted in 2026 is not
reproduced, and the gate that enforces its absence whitespace-normalises
and ASCII-folds both sides, so a line-wrapped injection dies.

**BHS — no sprinkling-grade Lorentz-invariance test.** The reproduction
catalog (`0cebe543e814`) records that

> a Poisson sprinkling admits **no Lorentz-invariant finite-valency
> graph** (BHS)

and these schedules are finite-valency by construction, so running the
test would manufacture a false negative. None is run: no sprinkling, no
boost, no rapidity, no frame appears in any measurement above.

**Kleitman–Rothschild — every dimension reading carries a height
control.** The catalog's carry is that

> a dimension reading without a height control is worthless

and this unit takes no dimension reading at all: no chart width, no
Myrheim–Meyer estimate, no max-shatter dimension. Its three columns are a
translation stabilizer, a determinant and a constructibility fate, none
of them dimension-adjacent. The height control is therefore not owed and
not manufactured, and the gate that says so is the conjunction — a paper
that took a dimension reading would have to carry one.

**The diagonal — measured here, and read no further.** The pin licenses
exactly this:

> the diagonal counterpoint may be MEASURED here -- that is this unit's
> point -- but cosmological readings stay barred

The U4 panel found the division field's period ⟨(1,1)⟩ and the vanishing
diagonal link count *jointly forced by one design choice*. This census
varies that choice and separates them: the period direction now ranges
over all four order-3 subgroups with no direction preferred, and the
diagonal link count is populated whenever a round groups along the
diagonal class. The two objects that looked like one cause at the
committed point are independent across the family. The bar is respected
as a bar on the READING: the four directions above are directions on a
nine-site lattice and are read as nothing else.

## 9. Choice inventory

| # | item | class | fiber | where it binds |
|---|---|---|---|---|
| 1 | the base object: CONFLICT-GRID(3,2) | **forced** | 1 | pin R1, from the committed constructor |
| 2 | the per-round budget: 3 groups of 3 | **forced** | 1 | the committed cycle, reproduced event for event |
| 3 | the site carrier: actors to Z_3^2 | **forced** | 1 | the constructor's own actor naming |
| 4 | admissibility: the layer's own menu | **forced** | 1 | d42b1 driven directly, no menu law re-typed |
| 5 | the site reading (initiator / footprint) | **declared** | 2 | both run; §4 is per reading |
| 6 | the I7 readout | **forced** | 1 | HA 3.2 as the U4 effectus evaluated it |
| 7 | the grammar window | **declared** | 1 | §2.4, disclosed in the head |
| 8 | the affine classification (three-valued) | **forced** | 1 | pin R3, plus the order-3 subgroup structure |
| 9 | the fragility edit: single-arbitration re-seating | **free** | — | this unit's; the minimal edit that stays in the family |
| 10 | the group and member processing order | **forced** | 1 | d66's own order at the committed schedule |

One free item. It is instrument-side, it is deterministic, and its
outcome is a single cell.

## 10. Verdict

```
U4B-CRYSTAL-GENERIC-[beyond-coset 1/32; 1749600 of 55987200; <(0,1)>|<(1,0)>|<(1,1)>|<(1,2)>]
```

```
DET-NONZERO-EXISTS-[ROW|ROW/DIAG: det=-1 at 9 of 9; 747 of 78400 pairs; POSDEF-EMPTY; I7-STRICT-EMPTY]
```

```
CONSTRUCTIBILITY-[FORCED 11664 of 11664; BRANCHING 0; REFUSED 0]@WINDOW-11664-OF-57153600+20-STRATUM-WITNESSES
```

Read out. The pre-registered alternative, in which only coset-union
schedules are crystalline and the whole phenomenon is the constructor's
own seed rule seen twice, **does not fire**: crystallinity appears at
seed sets that are not coset unions, at 216 of the 6912 beyond-coset seed
pairs, in all four available directions, by a mechanism that lives in the
pair of seed sets rather than in either one. That is the emergence
question's first positive datum on this arena — and §7 immediately prices
it, because every one of those crystals dies to a single re-seating.

The determinant segment answers the weld-arena scout. A non-degenerate
grammar-generated induced form EXISTS, at 747 of 78400 groupings, and the
simplest witness is the schedule that never rotates. It is never positive
definite anywhere in the family, for a reason that is a counting fact
about the committed cycle rather than an accident of these groupings, and
I7's strict-positivity criterion is empty for the same reason. The
renewal-crystal weld census the effectus predicted empty is recorded
empty, with a larger cause than the one predicted.

The constructibility census is uniform on the declared window and on
every stratum witness outside it, and it is a measurement rather than a
tautology because both other fates were exhibited by declared controls in
the same run.

## 11. Deviations, priced

1. **The grammar window is 1/4900 of the family.** Driving 57153600
   records is not affordable at tens of milliseconds each. Price: the
   FORCED reading is exhaustive on the resolvable window and on 20
   stratum representatives, not on the family. Mitigation: the window is
   named in the verdict string; the two other columns are exhaustive over
   the family; and the strata sweep puts a driven witness in every census
   cell, including cells whose groupings are not parallel classes.
2. **The U4 delivery artifacts are cited and not read.** A repair worker
   holds `paper-14` and `u4_crystals_*` under rewrite, and rule #91
   forbids reading a live worktree state; they are frozen and readable at
   commit `06b89fe`. The cross-unit anchor is taken instead from the
   FROZEN effectus review at its pinned sha, whose CONFLICT-GRID(3,2) I7
   row this unit reproduces exactly, and from d66's own committed output.
   Price: no U4 artifact is a witness here. The substitute is strictly
   older and strictly more anchored.
3. **Weld 2's SEC 6 rebuild, named in the pin as a cross-check route, is
   not read** (readable at commit `58195da`), for the same reason. Its
   role — an independent constructor for the committed grid — is filled
   by d66's own function object, re-run in this process.
4. **The fragility column is window-scoped.** The edit's admissibility is
   a grammar fact and is taken from the driven window. The combinatorial
   half of the same computation would extend to the family, but a
   fragility number whose admissibility is not driven is a different
   quantity and is not reported.
5. **The pin's `U4B-CRYSTAL-SEEDED` branch is not emitted**, and its
   `<the-locus>` slot is therefore unused. The branch was reachable: had
   the 216 beyond-coset pairs been 0, the run would have emitted it. A
   declared mutant drives the instrument onto it and dies at the gate
   that measures the beyond-coset population.
6. **"Crystalline" is read at the initiator site reading only.** The
   footprint reading is universally positive and §4.1 shows why that is a
   census artifact of the budget rather than a finding. Reporting a
   two-reading verdict string would have made a vacuous positive look
   like corroboration.

## 12. The instrument

The program is `v14/code/u4b_schedule_exact.py`, with the #82 CLI
contract: a delivery run that is the only writer, `--no-write`,
`--numbers`, `--selftest`, `--mutant NAME`, `--break-anchor NAME` and
`--verify-paper [PATH]`; every unknown flag, unknown flag argument and
missing flag argument exits 2, and the registered permissive shape is
present only as the CLI gate's own falsifier.

Arithmetic is exact end to end: an AST scan of the file and a recursive
type scan of the receipt are gates. Counts are computed, never typed
(#24). Gates bind objects rather than aggregates (#87): the
constructibility, footprint, driven-field, class-pair, affine and
fragility gates each evaluate every object against its own invariant.
Provenance is by pinned sha with the products gated (#91): 10 sources are
read at run time and the set of hash-pinned reads is required to be
exactly the declared set, with no subprocess of any kind, so the run is
correct off-tree and with no version control present. The verbatim
anchors (#62) each clear a length floor and each name the gate that
consumes them; text gates whitespace-normalise and ASCII-fold both sides
(#125). The coverage ledger is honest (#34): every gate is either
falsifiable by a declared mutant or waived with a forcing that says why
it cannot fail.

The gate-to-disk seal (#119) is disciplined from birth: every published
object is digested at the moment its gate passes, the payload may only be
sealed if every earlier seal still verifies, the artifacts are written
from the sealed payload, and the terminal integrity check compares the
bytes on disk against the gate-time seal after a deliberately corrupted
probe has been shown to be detected. The seal earned its keep during
construction: it caught a published row appended to a sealed object one
statement too late, which is exactly the failure #119 was engraved for.

The head is derived a second time by a comparator that shares neither
code nor input nor typed literal with the builder: it reads the receipt's
own census rows, recomputes the beyond-coset rate as a Fraction from the
two counts it finds there, and rebuilds all three verdict strings from
its own templates. The paper under test is checked in the same run for
claim rendering, numeral coverage and claim polarity; the delivery run is
byte-reproducible.

Registered siblings, cited and not run: the law-side
stochastic-crystallization unit, and the diagonal-populating constructor
(the K9/S1 four-direction fact) named in the pin as the weld arena should
the determinant column have come back empty. It did not come back empty,
which changes that successor's standing and is left to the adjudication.
