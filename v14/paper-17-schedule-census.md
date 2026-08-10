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

**Standing.** MOTIVATED at the RSQ choice standard: every choice this
unit makes is declared or forced with its forcing exhibited, and there
are no free items (§9).

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

Both answers came back positive. The first came back with its variable
changed under it, and the second came back with a restriction nobody
asked for.

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
committed schedule. That extension of d66's order from the committed
point to the whole family is a convention, not a derivation, and §9
prices it: the convention has a fiber of 36 per round, and each of those
36 is driven, applied to both rounds, at three declared schedules — 108
records — without changing a fate, an event count or either site field
at any of them.

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
review's CONFLICT-GRID(3,2) row in I7 coordinates, which in that review's
own schema is

```
(n_(1,0), n_(0,1), n_(1,1), q_11, q_22, |q_12|, det) = 1, 1, 0, 1, 1, 1, 0
```

reproduced by this unit's own readout. The sixth entry is the absolute
value: the ASCII fold the read anchor applies does not carry a sign, so
the anchor validates the route up to the sign of q_12, and §5.1's
`q12 = -1` is recovered from the readout rather than from the anchor. A
reader who checks the source row against the tuple above finds a −1 there
and no discrepancy here.

### 2.4 The declared window, disclosed here and in the head

Driving the layer's menus over 57153600 schedules is not affordable.
Grammar-admissibility is therefore decided exhaustively on a **declared
window**: both rounds' groupings drawn from the 4 parallel classes of
AG(2,3) — the resolvable device d66's own constructor uses — with the
seeds free. In numbers, the declared window has 11664 schedules, 1/4900 of the family,
and it contains the committed schedule. The window is named inside
the constructibility verdict string, so no reader can meet the number
without meeting its scope.

**The stabilizer and determinant columns below are exhaustive over the
whole family; constructibility and fragility are window-scoped.** The
stabilizer and the determinant are functions of the schedule alone, so
they are computed over all 57153600 schedules by exact enumeration of the
objects they actually depend on, with no window at all. Constructibility
is measured on the window and on 20 stratum witnesses, 12 of which lie
outside it; fragility is measured on the window's crystals, and §7 then closes it at
family scope by a second, combinatorial route. Every rate quoted in §4 to
§6 is a rate over **declared** schedules — the family is declared as data
in §2.2, and the grammar's verdict on it is an induction from the window
and the witnesses, not a measurement of all of it.

The window is also the most symmetric window available: all-parallel-class
groupings are the resolvable device the constructor itself uses, so
FORCED-everywhere is measured in the most favourable place. The 20 stratum
witnesses are what price that, and 12 of them sit outside it.

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

**The two negative fates are not the same kind of zero, and the paper
says which is which.** REFUSED is genuinely at risk and the instrument
reaches it. BRANCHING is a **structural zero for any schedule of this
family**: every event here is specified by its full tuple, `candidates_for`
generates each event tuple once, so at most one candidate can ever match
and no family schedule can branch. The second control below therefore
establishes instrument sensitivity, not family-level reachability, and
the FORCED reading is a measurement because REFUSED was at risk.

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
under-specified pick and no record is continued past one. That immunity
is what makes this unit's own byte-reproducibility a fact rather than a
hope, and the defect it discloses is registered corpus-wide in
`v14/note-d60-defect-register.md`.

**Twenty strata witnesses, 12 of them outside the window.** The census of §4
to §6 stratifies the whole family by (stabilizer × affine class ×
non-degeneracy). All 20 nonempty strata are given a deterministic
representative — first in a fixed enumeration, no sampling — and every
representative's record is built by driving the menus. All 20 are FORCED.
So the grammar's verdict has been taken at least once in every cell of
the census, and 12 of the 20 representatives have partitions that are not
parallel classes at all, so the verdict has been taken outside the window
as well as inside it.

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
nothing below is read off it.** The line this owes U4's register is
exactly one: U4b measured the constant-field vacuity at family scope —
the footprint field is ≡ R at every schedule the committed budget admits,
so U4's two Z_3^2 entries are budget artifacts, as its adjudication
already said. No erratum is owed and no scope annotation: nothing in U4
is false, and its two entries were annotated vacuous when they were made.

### 4.2 The initiator reading

At the initiator reading the field is `1_{S0} + 1_{S1}`, where `S_r` is
the round-r seed set. What licenses this column to be exhaustive over the
family, exactly, is two things and neither of them is a measurement of
the family.

First, a **theorem**: given a record the layer did not refuse, the field
read off the DRIVEN record — initiators from `op[1]`, footprints from
`regs_of` intersected with the actor set — *equals* the field the
combinatorial route computes from the schedule alone. Every event here is
specified by its full tuple, so an appended event is the specified tuple,
and the field is a function of the schedule. The only way the equality
can fail is a refusal. It is checked anyway, per object, on all 11664
window records: zero mismatches.

Second, **constructibility** — the window-scoped thing. If no schedule is
refused, the theorem applies to all of them. That step is verified on
11664 window schedules and on 20 stratum witnesses, 12 of them with
partitions that are not parallel classes, and it is an induction, not a
census. The exhaustive columns inherit the window's induction rather than
its measurement, and this paper says so rather than counting the theorem
as evidence.

Third and separately, every one of the 84 three-element subsets of Z_3^2
is a transversal of exactly 90 of the 280 partitions. That weight is
uniform — measured, not assumed — so the 7056 ordered seed-set pairs
carry the entire census with a single multiplicity.

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

applied to **the co-division adjacency**: for a link l and a site x, the
number of division events whose footprint contains both x and x + l. That
adjacency is a declared choice of this unit, taken from U4's own
definition, and the whole determinant column, both counting theorems and
the POSDEF and I7-STRICT results are relative to it and to the link set
{(1,0), (0,1), (1,1)} — three of the four direction classes of Z_3^2, the
antidiagonal class depositing nothing. §9 carries the row. HA 3.2 says
what the readout is:

> The readout is an invertible linear re-encoding: in count coordinates,
> the record IS the metric.

Every component and every determinant below is an exact `Fraction`. The
route is validated by reproducing the effectus's committed
CONFLICT-GRID(3,2) row at all nine sites, not at the one the anchor
prints: q11 = 1, q22 = 1, q12 = -1 and det = 0, the degenerate form whose
kernel is the diagonal, the same at every site.

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

It is non-degenerate for a specific reason, and the reason is worth
saying because it is the opposite of the one a reader expects. Never
rotating concentrates both rounds' incidences on a single link, which
gives q22 = 2 and det = -1; it is also why its record is one of the 2916
short ones, 24 events with no round-1 conflict supply; and it is why
q11 = 0, so the e1 coordinate direction is **null** in the very form this
paper calls the first non-degenerate carrier. Non-degenerate, here, is a
consequence of dynamical poverty rather than of richness.

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

**It is never positive definite at every site.** Exhaustively over all
78400 partition pairs, the maximum number of positive-definite sites is
3 — never 9. The mechanism is a counting fact about the committed cycle
rather than an accident of these groupings, and it has three steps.

*The budget.* A partition into three triples has 9 within-group pairs,
and a within-group pair contributes at most one link-incidence, because
I7's link set holds exactly one representative of each of three direction
classes and nothing in the fourth. So the two rounds deposit at most 18
link-incidences over the 27 (link, site) cells. That bound is tight and
not an estimate: the maximum total link-incidence over the whole family
is exactly 18, attained at 1296 partition pairs.

*The cost of one positive-definite site.* Positive definiteness at a site
needs q11 > 0 and q22 > 0 — that is n_(1,0) ≥ 1 and n_(0,1) ≥ 1 — and it
also needs n_(1,1) ≥ 1, which the inequality
4·q11·q22 > (n_(1,1) - q11 - q22)^2 does not by itself supply. The step
is short: if n_(1,1) = 0 then q12 = -(q11 + q22) / 2 and
det = -(q11 - q22)^2 / 4 ≤ 0, so the site is not positive definite. Hence
at least 3 incidences at a positive-definite site — measured, the minimum
over every positive-definite cell in the census is exactly 3, and 0 such
cells hold fewer.

*The conclusion.* Nine positive-definite sites would need at least 27
incidences, and 18 < 27. The exhaustive census agrees.

**The wall does not explain the measured ceiling, and the gap is
registered as an open.** At 3 incidences per positive-definite site, the
same count permits as many as 6 positive-definite sites; the measured
maximum is 3, attained at 252 partition pairs. The finer obstruction is a
measurement here, not a consequence of the counting fact, and anyone
reading "never Riemannian" as fully explained by 18 < 27 is reading past
it.

**Positive-definite sites themselves are common, and the quantifier is
what carries the negative result.** 28404 of the 78400 partition pairs
carry at least one positive-definite site — 20706516 of the 57153600
schedules, 7101/19600 of the family — over 32400 (pair, site) cells in
all. What is empty is the all-sites condition: **no partition pair is
positive definite at every site**, and none has det > 0 at all nine
sites either.

**I7's own admissibility is empty for the same reason:** no partition pair
makes all 27 link counts strictly positive. So no schedule in this
family is an admissible I7 geometry record. The U4 effectus predicted the
renewal-crystal weld census EMPTY from the vanishing diagonal; the census
records it EMPTY, but the cause is larger than the diagonal — it is the
link budget, and it would survive any redistribution of the same 18
incidences. That makes the emptiness a **resource deficit in the
committed cycle** rather than a structural impossibility of the arena;
§13 states the successor's entry criterion and what clearing it does not
buy.

**The signature is not constant across the family, and not always
constant within a schedule.** Of the 747 non-degenerate pairs, 261 carry
det < 0 at all nine sites and 486 carry both signs. Across the cells
of those pairs the determinant takes the value -1 at 855 cells, -1/4 at
5238, 1 at 108 and 3/4 at 522. Where det > 0 the form is positive
definite; that happens, but never at more than 3 sites of one schedule.

In two dimensions a form with det < 0 is indefinite, of signature (1,1).
The corpus's Lorentzian vocabulary is not in play: the two coordinates
are the link directions e1 and e2 of a nine-site lattice, no causal order
is defined on them, no boost group acts, and the sign is not even
constant within a schedule at 486 of the 747 non-degenerate groupings —
so a signature reading of this arena is not merely barred, it is
ill-posed for most of its own carriers. The resonance is named here so
that it is not read.

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
realizing all four order-3 subgroups. In these schedules the field takes
the value 1 on a union of two H-cosets and 0 on the third, while
**neither seed set is a coset of any order-3 subgroup** — measured at all
216, and provable: a coset of a different order-3 subgroup meets each
coset of the period exactly once, so it cannot sit inside the union of
two of them. The two seed sets partition six sites between them without
either one respecting the period. **The period is a property of the pair,
not of either seed** — which is precisely what the affine reading of a
single seed set cannot produce.

That is the measurement. Here is what it is entitled to mean, which is
less than it looks and sharper.

**The carrier is the sum, not the summands.** `Stab(n)` is by construction
a function of the aggregate field `1_{S0} + 1_{S1}`, and the aggregate is
a coset union in every crystalline case: **at 252 of 252 crystalline seed
pairs the field is supported on a union of cosets of its own period**, in
two shapes — 12 pairs whose two seed sets are equal, where the field is 2
on one coset and 0 elsewhere, and 240 pairs where the field is 1 on two
cosets and 0 on the third. So the affine law `n = c + m·1_S` is violated
nowhere in this census. It holds with `S` the **union** of the two seed
sets. What the census establishes is that the constructor-inheritance
argument was stated on the wrong variable — the carrier of the period is
the summed division field's support, not either seed set — and not that a
mechanism outside the affine law exists on this arena.

**The honest headline quantity is a share, not a mechanism.** The
pre-registered per-seed locus contains one seventh of the crystallinity
it was supposed to explain: 1749600 of 2041200 crystalline schedules lie
outside it, so **six sevenths of all crystallinity in the family lies
outside the inherited locus**. One law, seven times the territory.

**And the mechanism needs no census at all: it closes in closed form.**
For each of the 4 order-3 subgroups and each of its 3 cosets to leave
empty, the remaining 6 sites split into ordered (S0, S1) in C(6,3) = 20
ways, 2 of them coset-to-coset. So 4 × 3 × 18 = 216 beyond-coset pairs,
4 × 3 × 2 + 12 = 36 coset-union pairs, 252 = 4 × 63 in all — every one of
those numbers the census's own. A unit dedicated to the pair mechanism
would be measuring a closed form; §13 registers the open that is not
closed instead.

One reading is **not** licensed and this paper bars it. A category of
"relational order" — order that lives in the relation and in neither part
— would need a carrier that is *not* a function of the aggregate field.
This census exhibits the opposite at every one of its 252 crystalline
pairs. The finding is a statement about which variable was
pre-registered, and it may not be promoted to an ontological category.

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
period. That argument proves the original period is not preserved. It
leaves open something a reader would want closed: an edit might land on a
*different* nontrivial period, in which case the crystal would be rotated
rather than destroyed, and "fragile" would be the wrong word.

It does not. Over all 252 crystalline seed pairs and all single-point
re-seatings of either seed to any other site — a strict superset of the
admissible re-seatings of *any* partition, not just the window's — the
edited field's stabilizer is trivial every time: **at all 9072
single-point re-seatings of one seed of a crystalline pair, the edited
field's stabilizer is trivial**. Not one lands on any nontrivial period.
So the fragility is a family-scope combinatorial theorem, and the window
carries only the admissibility half of it.

**The crystal is destroyed by the minimal admissible edit, wherever it
occurs.** Read with §6 this is the census's sharpest statement about the
object: the crystallinity that the inherited locus does not contain is
not robust either — it is a coincidence of two seed sets that a single
re-seating destroys. What that may not mean is that the crystalline
*class* is unstable or special: the class is 1/28 of the family, exactly
uniform across the four directions, and closed under nothing tested here.
Brittleness is a property of each crystal, not of the phenomenon.

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
reproduced, and the gate that enforces its absence ASCII-folds both
sides, strips leading markdown line-decorations and only then
whitespace-normalises, so a line-wrapped injection dies and so does a
blockquoted one — which matters, because the blockquote is the form this
corpus actually writes when it quotes a prior unit.

**BHS — no sprinkling-grade Lorentz-invariance test.** The reproduction
catalog (`0cebe543e814`) records that

> a Poisson sprinkling admits **no Lorentz-invariant finite-valency
> graph** (BHS)

and these schedules are finite-valency by construction, so running the
test would manufacture a false negative. None is run, and the gate that
says so measures rather than declares it: an AST scan of the instrument's
own source finds no identifier — no function, no variable, no attribute,
no argument — named for a sprinkling, a boost, a rapidity, a Poisson
process, a Lorentz transformation or a frame. The words occur in the
file, in prose, which is exactly why the gate scans names and not text.

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
varies that choice and separates them. The two objects are **separately
carried and neither determines the other** — the period is a seed
property, the diagonal link count a grouping property — and the marginal
is exactly uniform: 510300 crystalline schedules in each of the four
period directions, no direction preferred.

They are **not** independent, and the departure is exactly at the
diagonal. The diagonal link count is populated at 503388 of the 510300
crystalline schedules in each of the three non-diagonal directions —
4661/4725 — but at only 490860, or 101/105, when the period *is* the
diagonal. Conditionally the coupling is large: among the 40176
crystalline schedules whose diagonal link count is empty, **the period is
the diagonal at 15/31 of them, against 1/4 under independence**. The
residual coupling is a transversal constraint between seed sets and
groupings — a seed set must be a transversal of its round's partition —
and it is read as nothing else. Saying it is what keeps the bar honest:
the diagonal is still special in the joint. The bar is respected as a bar
on the READING: the four directions above are directions on a nine-site
lattice and are read as nothing else. The word "cosmological" appears in
this section, in the bar; no cosmological claim phrase appears anywhere
in this paper, and that is what the gate tests.

## 9. Choice inventory

| # | item | class | fiber | where it binds |
|---|---|---|---|---|
| 1 | the base object: CONFLICT-GRID(3,2) | **forced** | 1 | pin R1, from the committed constructor |
| 2 | the per-round budget: 3 groups of 3 | **forced** | 1 | the committed cycle, reproduced event for event |
| 3 | the site carrier: actors to Z_3^2 | **forced** | 1 | the constructor's own actor naming |
| 4 | admissibility: the layer's own menu | **forced** | 1 | d42b1 driven directly, no menu law re-typed |
| 5 | the site reading (initiator / footprint) | **declared** | 2 | both run; §4 is per reading |
| 6 | the I7 readout | **forced** | 1 | HA 3.2 as the U4 effectus evaluated it |
| 7 | the co-division adjacency, and I7's link set | **declared** | ≥ 2 | U4's own definition, anchored here by reproducing one committed row at all nine sites; §5.1 |
| 8 | the grammar window | **declared** | ≥ 2 | §2.4, disclosed in the head; the pin names at least one other admissible shape |
| 9 | the affine classification (three-valued) | **forced** | 1 | pin R3, plus the order-3 subgroup structure |
| 10 | the fragility edit: single-arbitration re-seating | **declared** | 2 | event-level re-seating vs group-level re-partition; §7's own first sentence forces the event-level form to the 12 counted here |
| 11 | the group and member processing order | **declared** | 36 per round | d66's order at the committed point, extended by convention; the fiber is driven where it is applied uniformly across the rounds, and inert there (§2.1) |
| 12 | the 20-stratum representative rule | **declared** | 1 | first in a fixed enumeration, no sampling; deterministic |

**Zero free items: MOTIVATED at the RSQ standard.** The one item this
unit could have left free is the fragility edit, and it does not need to
be: §7's own definition forces the event-level edit to exactly 12 forms
per schedule, so the choice is between event-level and group-level and
the fiber is 2, printed. A partition-level fragility is a different
quantity and is not reported. The two ≥ 2 fibers are lower bounds: the
pin names at least one further admissible window shape, and the
co-division adjacency admits at least one alternative — the same count
taken at the initiator reading rather than the footprint reading, which
§4 shows are different objects.

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
pair of seed sets rather than in either one. GENERIC is the
pre-registered branch name for that outcome and carries its own fraction;
what it names is NOT-CONFINED-TO-THE-SEEDED-LOCUS, and the rate is a
minority of the family either way.

That is the first crystallinity on this arena that the pre-registered
per-seed locus does not contain — and it is still the affine law, taken
on the union of the two seed sets rather than on either one. The honest
size of the finding is the share: six sevenths of the family's
crystallinity sits outside the locus that was supposed to explain all of
it. §7 immediately prices it, because every one of those crystals dies to
a single re-seating, and that now holds at family scope.

The determinant segment answers the weld-arena scout. A non-degenerate
grammar-generated induced form EXISTS, at 747 of 78400 groupings, and the
simplest witness is the schedule that never rotates. It is **never
positive definite at every site**, anywhere in the family, for a reason
that is a counting fact about the committed cycle rather than an accident
of these groupings, and I7's strict-positivity criterion is empty for the
same reason. Positive-definite sites are not rare; nine of them at once
are impossible. The renewal-crystal weld census the effectus predicted
empty is recorded empty, with a larger cause than the one predicted — and
a cause that a bigger budget could clear, which is the successor's whole
opening.

The constructibility census is uniform on the declared window and on
every stratum witness outside it. It is a measurement rather than a
tautology because the REFUSED fate was genuinely at risk and a declared
control reached it; the BRANCHING zero is structural, and §3 says so.

## 11. Deviations, priced

1. **The grammar window is 1/4900 of the family.** Driving 57153600
   records is not affordable at tens of milliseconds each. Price: the
   FORCED reading is exhaustive on the resolvable window and on 20
   stratum representatives, not on the family, and the exhaustive columns
   inherit that induction (§4.2). Mitigation: the window is named in the
   verdict string; the strata sweep puts a driven witness in every census
   cell, including cells whose groupings are not parallel classes; and
   the window is the most symmetric one available, which the 12
   out-of-window witnesses are what price.
2. **The U4 delivery artifacts are cited and not read.** A repair worker
   holds `paper-14` and `u4_crystals_*` under rewrite, and rule #91
   forbids reading a live worktree state; they are frozen and readable at
   commit `06b89fe`. The cross-unit anchor is taken instead from the
   FROZEN effectus review at its pinned sha, whose CONFLICT-GRID(3,2) I7
   row this unit reproduces exactly — up to the sign of q_12, which that
   review's ASCII table does not carry (§2.3) — and from d66's own
   committed output. Price: no U4 artifact is a witness here. The
   substitute is strictly older and strictly more anchored.
3. **Weld 2's SEC 6 rebuild, named in the pin as a cross-check route, is
   not read** (readable at commit `58195da`), for the same reason. Its
   role — an independent constructor for the committed grid — is filled
   by d66's own function object, re-run in this process.
4. **The fragility column's admissibility half is window-scoped.** The
   edit's admissibility is a grammar fact and is taken from the driven
   window. The combinatorial half extends to the family and §7 now runs
   it there, as a separate and clearly labelled computation: the 9072
   family-scope re-seatings are not driven records, and the two halves
   are not merged into one number.
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
7. **The R = 3 arrangement in §13 is outside this unit's declared
   family.** It is computed here and used in no measurement above: no
   record is driven for it, and nothing is claimed about whether it is
   grammar-admissible. It is the successor's entry datum and is labelled
   as one.

## 12. The instrument

The program is `v14/code/u4b_schedule_exact.py`, with the #82 CLI
contract: a delivery run that is the only writer, `--no-write`,
`--numbers`, `--selftest`, `--mutant NAME`, `--break-anchor NAME` and
`--verify-paper [PATH]`; every unknown flag, unknown flag argument,
missing flag argument and repeated flag exits 2, a `--verify-paper` path
that is not a file exits 2, `--selftest --mutant` is honoured rather than
inert, and the registered permissive shape is present only as the CLI
gate's own falsifier.

Arithmetic is exact end to end: an AST scan of the file and a recursive
type scan of the receipt are gates. Counts are computed, never typed
(#24). Gates bind objects rather than aggregates (#87), and each
published row is built **before** the gate that certifies it, so the gate
reads the row a reader will hold rather than a live variable that the row
is assembled from afterwards. Provenance is by pinned sha with the
products gated (#91): 10 sources are read at run time and the set of
hash-pinned reads is required to be exactly the declared set, with no
subprocess of any kind, so the run is correct off-tree and with no
version control present. The verbatim anchors (#62) each clear a length
floor and each name the gate that consumes them; text gates ASCII-fold
both sides, strip leading markdown line-decorations and then
whitespace-normalise (#125).

The coverage ledger is honest (#34) in three respects. Every gate is
either falsifiable by a declared mutant or waived with a forcing that
says why it cannot fail. The **denominator** is the declared gate
universe — every gate emitted, plus the gates still to come in the run's
own tail, plus those evaluated only in the mutant, self-test and writing
paths — and a gate cannot be counted by the instrument and missed by its
own coverage row. And every FALSIFIABLE row's named falsifier is checked
for **reachability**: the mutant's measured `killed_at` must equal that
row's own gate, not merely be non-null, so a gate credited to a mutant
that dies earlier, or that reaches the gate and passes it, is caught.

The gate-to-disk seal (#119, with the #148 totality addendum) is total.
Every published object is digested at the moment its gate passes; a
declared seal that was never taken counts as broken rather than absent,
so a seal cannot be dropped without trace; the completeness gate compares
the manifest against the DECLARATION rather than against its own
contents; and the closing gate requires every published receipt key to be
either sealed or on a declared-unsealed manifest that is itself
published. The seal covers what this instrument **vouches for** as well
as what it measured — its provenance rows, its claims about its own
paper, its coverage and polarity rows — because those are precisely the
rows a reader cannot recompute. The gate ledger is not sealed once but
chained, one rolling digest step per row at the moment that row passes;
the transcript is chained line by line as it is written and re-checked at
close, so the two artifacts cannot state opposite things; and the closing
counts are re-derived from the sealed rows rather than carried in a
counter. The artifacts are written from the sealed payload, the terminal
integrity check compares the bytes on disk against the gate-time seal
after a deliberately corrupted probe has been shown to be detected, and a
failure after the replace restores the previous artifacts rather than
leaving a corrupt one in place. The seal earned its keep during
construction: it caught a published row appended to a sealed object one
statement too late, which is exactly the failure #119 was engraved for.

The head is derived a second time by a comparator that shares no code and
no typed literal with the builder and is handed the receipt **serialized
to JSON and parsed back**, which is the write path's own route, so not
one live object crosses: it reads the receipt's own census rows,
recomputes the beyond-coset rate as a Fraction from the two counts it
finds there, and rebuilds all three verdict strings from its own
templates. The paper under test is checked in the same run for claim
rendering, numeral coverage and claim polarity: two dozen headline claims
are formatted from the receipt's own rows and required to appear in this
paper by string equality after the declared fold, every numeral occurring
here must be a number this run computed and registered or one of the
declared in-text residues, and every declared residue must actually occur
so the list cannot be padded. The delivery run is byte-reproducible.

## 13. The successor register

**The weld route, and its entry criterion.** The obstruction §5.3
measures is a resource deficit, so the successor's pin must demand, as an
**entry criterion and not an outcome**, a budget depositing at least 27
link-incidences on I7's link set. The minimal saturating structure is
exhibited: R = 3, the three rounds grouped on the three link-direction
parallel classes, gives n = 1 at all 27 (link, site) cells,
q = [[1, -1/2], [-1/2, 1]], det = 3/4 at all nine sites, positive
definite at all nine, and I7's strict criterion satisfied for the first
time. Four demands ride on top. Constructibility must be **driven**,
because at R = 3 the round-2 conflict-supply question is new. The affine
null must be **re-pre-registered**, because at R = 3 the field sums to 9
over 9 sites, the shape (1,1,1) exists and the full group Z_3^2 becomes
reachable — this unit's "the full group never occurs" is a budget fact
that dies there. The null must be stated on the **summed field**, per §6.
And it must be said explicitly that 27 incidences is necessary, not
sufficient: I7 strict positivity is one of the weld census's conditions,
not all of them.

**What the coupling unit inherits, and what it must not.** Taking
ROW|ROW/DIAG as the first candidate shared arena is premature on three
measured grounds: 486 of the 747 non-degenerate groupings carry
site-varying determinant sign, so "the arena's signature" is undefined
for most of them; the witness has a null coordinate direction and is the
dynamically poorest schedule in the family; and no selection criterion
among the 747 has been declared. What it should inherit is the **pool and
the wall** — the 19791 schedules that are crystalline *and* non-degenerate
at all nine sites, 17118 of them beyond-coset, as the candidate pool, and
the budget wall as a resource criterion on any shared arena it proposes —
together with the structural fact that non-degeneracy is a function of
the groupings alone, so the seeds stay free inside it.

**The positive-definite ceiling: open.** The wall permits 6
positive-definite sites and the census attains 3, at 252 partition pairs.
Either derive the finer obstruction or register the ceiling as
measurement-only.

**No pair-mechanism unit; a theorem is registered instead.** The
mechanism closes in closed form (§6). The open worth pinning is the
general (g, R) law: does the union-carrier statement, the exact
uniformity across the four directions, and a closed-form rate survive
other budgets?

**The law-side stochastic sibling, registered and not run.** It inherits
three numbers as its null — the family rate 1/28, the beyond-coset rate
1/32, and the exact uniformity across the four directions at 63 seed
pairs each. A stochastic crystallization claim on this arena must beat a
base rate, not merely exhibit crystals. It inherits the carrier finding
too: randomizing seeds and randomizing the field are different
experiments, and only the second addresses the period. And it must
survive §7, where no deterministic crystal survives one edit.

**The diagonal-populating constructor** (the K9/S1 four-direction fact)
was named in the pin as the weld arena should the determinant column have
come back empty. It did not come back empty, which changes that
successor's standing and is left to the adjudication.

**Two registrations owed elsewhere.** One cross-reference line to U4's
register, quoted in §4.1; and the d60 tie-break defect, registered
corpus-wide in `v14/note-d60-defect-register.md`, which is about a
committed v10 constructor and not about this unit — U4b's every record is
fully specified, so the tie-break is never consulted here.
