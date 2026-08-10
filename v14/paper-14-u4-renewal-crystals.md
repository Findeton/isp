# Renewal-only crystals

**U4 / paper-14.** Pin `v14/note-u4-pin.md` (FROZEN, sha256-12
`06b62ecb60a9`, ledger #105). Code `v14/code/u4_crystals_exact.py`;
artifacts `v14/code/u4_crystals_output.txt`,
`v14/code/u4_crystals_receipt.json`.

**Verdict.**

```
U4-THE-DIVISION-EVENTS-FORM-A-CRYSTAL-CONSTRUCTOR-INHERITED-[DG32:<(1,1)>/<(1,1)>|DG33:<(1,1)>/<(1,1)>|CG32:<(1,1)>/Z3^2|CG34:<(1,1)>/Z3^2|CTRL:1/1]
```

**Geometry segment.**

```
GEOMETRY-INVARIANT-AT-THE-CONTROLLED-ROW-REST-BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL
```

---

## 1. The question

v11 paper 0 §7 (`37a428321f46`), verbatim:

> **U4 — SPARSE RECORDS ON THE CRYSTALS.** The conflict crystals
> rebuilt with renewal-only records: geometry should be invariant
> (it is kinematic — paper 0 §10's third falsifier if not); the
> bridges between the renewal sublattice — itself periodic: *the
> division events of a crystal form a crystal* — are probed for
> indivisible structure.

The italicised clause has never been checked anywhere in the corpus. It
was registered-unrun in weld 2's committed gate `G-U4-REGISTERED`, which
states of itself that "this unit builds the committed crystals and reads
their division events, it does not rebuild the crystals with
renewal-only records". This unit checks it, and finds it true and
**inherited**: the periodicity is the constructors' own, carried into
the division events by a seed rule, and §5.1 measures the mechanism that
carries it.

## 2. The arena, declared (§15)

Five records, all FORCED — every event taken from the committed layer's
own menu, specified by its full event tuple, and matched by exactly one
candidate (`maxhits = 1`), with no refusal anywhere.

| crystal | kind | events | division events | maxhits | refusal |
|---|---|---|---|---|---|
| DOUBLE-GRID(3,2) | arbitration | 72 events, 18 division events | 18 | 1 | none |
| DOUBLE-GRID(3,3) | arbitration | 96 events, 24 division events | 24 | 1 | none |
| CONFLICT-GRID(3,2) | arbitration | 30 events, 6 division events | 6 | 1 | none |
| CONFLICT-GRID(3,4) | arbitration | 66 events, 12 division events | 12 | 1 | none |
| D60-GRID(3,12) | **control** | 46 events, 1 division event | 1 | 1 | none |

`D60-GRID(3,12)` is the pin's **DECLARED COUNTEREXAMPLE CONTROL**: every
periodicity claim below must return its other value there, and every
two-way pair is gated per crystal and per reading, never in aggregate.

The constructors are rebuilt from their definitions rather than
imported: D60's `B` and CRYSTAL-2D (`684cdb76552b`), D66's `double_grid`
and `conflict_grid` (`3d0516ab106e`), over the D42b1 transport grammar
(`576275d55ecf`). The rebuild is cross-checked against the v10
originals' own committed output at **the atlas rows and counts
enumerated here** — the control's full profile at both depths, and the
two swept crystals' widths, homogeneities, mean chart sizes, overlaps,
arbitration shares, version-register counts and event counts. Forty-two
committed-number anchors reproduce, none moves; each is *read* at run
time out of the v10 output line it cites, by a context-keyed regex, and
it is the extracted value — not a typed rendering — that the computed
number is compared against.

The cross-check is not exhaustive of what v10 printed for these
crystals, and the rows it does not carry are named rather than left
implicit: DOUBLE-GRID(3,2)'s depth-3 mean chart size, the depth-2 width
histograms of DOUBLE-GRID(3,2) and CONFLICT-GRID(3,4), DOUBLE-GRID(3,2)'s
tag census and its arbitrations by proposer count, and the excision row.
Those are outside the gated set and this unit makes no claim about them.

The two crystals v10 never swept — DOUBLE-GRID(3,3) and
CONFLICT-GRID(3,2) — carry no committed row anywhere, so they are
cross-checked instead by a closed-form event-count law fitted to nothing
and verified at every committed member of its own family: DOUBLE-GRID at
R = 2 and R = 4 (72 and 120), CONFLICT-GRID at R = 4, 6 and 10 (66, 102,
174). The law then predicts 96 and 30, and the rebuilds carry 96 and 30.

## 3. The renewal marking, re-derived and scoped

The marking is not this unit's to choose. v11 paper 0 §4's `[POSIT]` —
"v11's **division events are the renewal events**" — identifies the two,
and paper-09 §3 (`006f96aaa2ff`) forces the reading from three agreeing
source rows: S1's code (`REN = [h for h in FAM if len(h) <= 4 and
CLS[tuple(h)] == 0 and any(e[0] == 'r' for e in h)]`), S1's own gate, and
S4's theorem that every pair arbitration is a renewal to the root.

**Of the three rows, exactly one reaches this arena, and the unit says
so.** The class-0 clause is a two-actor delivery-free *state-space*
notion; the corpus defines its congruence classes on that family and
nowhere else, so at nine actors the clause has no committed referent.
S4's narrower sufficient condition is *pair* arbitration, and every
conflict key on these five crystals has size 1 or 3 — measured: **0 pair
arbitrations among the 61 marked events across all five crystals.** What
transports is the arbitration tag, which is exactly the ingredient weld 2
measured source-forced at 1536 of 1536 tagged instances.

Two independent checks stand in for the two silent rows.

**The marking is not carried by the tag alone.** A second predicate,
written from the grammar's tuple *shapes* rather than its tags — an
arbitration is the unique four-tuple whose third slot is a conflict key,
where proposals carry a value tuple, deliveries an actor name, merges a
pair of values, and idles are two-tuples — selects the identical event
set on every crystal, index for index: 18, 24, 6, 12, 1.

**S4's content transports even though its hypothesis does not.** At
61 of 61 marked events, re-derived event by event from the grammar's own
`View`, every proposer named in the conflict key holds the newly minted
value immediately afterwards and the superseded base is retired. The
marked events are exactly the events that reset their conflict group to
one shared value with no delivery — which is what "a renewal to the root"
says at this arena.

## 4. Declared data, with fibers

Two data declarations are needed and neither is pinned anywhere. Both are
run as arms; the pin requires it.

**(D1) The site reading — fiber 2, both arms run.** A division event has
to be attached to a site of Z₃².
(a) *initiator*: the arbitrating actor, `op[1]`.
(b) *footprint*: every actor in the event's register footprint,
`regs_of(op)`.
Which of the two the corpus means is not settled anywhere. Agreement or
divergence between them is a measured output of §5, not an assumption of
it.

**(D2) The renewal-only operationalization — fiber 3, two arms run, one
registered.**
(a) *FILTER*: reduce the forced record to its arbitration events. This
is the primary arm because it introduces no new grammar law. It is itself
ambiguous, so its own fiber is 2 and both sub-readings run: **POP**, D60's
own committed device, where "the poset is left whole; only the metric
population changes"; and **SUB**, the literal sparse record, whose event
poset is recomputed from the marked events alone.
(b) *BUILDER-RERUN*: re-run the Builder on a restricted candidate stream.
The restriction is a declared sub-grammar in D74's shape
(`bb852161aced`) — "the support is restricted, the committed weights are
untouched".
(c) *QUOTIENT* by non-arbitration events: **registered, not run.** Nothing
in the verdict descends from it.

The carrier of the site reading is not a declaration: every constructor
names its actors on a 3 × 3 grid, so the actor names parse as a bijection
onto Z₃² and this unit assigns no site.

## 5. The headline — the division-event field's translation stabilizer

The division-event field is `n : Z₃² → Z≥0`, `n(x)` counting the division
events attached to site `x` at the declared reading. Its translation
stabilizer is `Stab(n) = { t ∈ Z₃² : n(x + t) = n(x) for every x }`, a
subgroup of the elementary abelian group of order 9.

| crystal | reading | field over the nine sites | support | stabilizer | order |
|---|---|---|---|---|---|
| DOUBLE-GRID(3,2) | initiator | 3, 3, 0, 0, 3, 3, 3, 0, 3 | 6/9 | `<(1,1)>` | 3 |
| DOUBLE-GRID(3,2) | footprint | 5, 5, 4, 4, 5, 5, 5, 4, 5 | 9/9 | `<(1,1)>` | 3 |
| DOUBLE-GRID(3,3) | initiator | 4, 4, 0, 0, 4, 4, 4, 0, 4 | 6/9 | `<(1,1)>` | 3 |
| DOUBLE-GRID(3,3) | footprint | 7, 7, 6, 6, 7, 7, 7, 6, 7 | 9/9 | `<(1,1)>` | 3 |
| CONFLICT-GRID(3,2) | initiator | 2, 0, 0, 0, 2, 0, 0, 0, 2 | 3/9 | `<(1,1)>` | 3 |
| CONFLICT-GRID(3,2) | footprint | 2, 2, 2, 2, 2, 2, 2, 2, 2 | 9/9 | `Z3^2` | 9 |
| CONFLICT-GRID(3,4) | initiator | 4, 0, 0, 0, 4, 0, 0, 0, 4 | 3/9 | `<(1,1)>` | 3 |
| CONFLICT-GRID(3,4) | footprint | 4, 4, 4, 4, 4, 4, 4, 4, 4 | 9/9 | `Z3^2` | 9 |
| **D60-GRID(3,12)** | initiator | 1, 0, 0, 0, 0, 0, 0, 0, 0 | 1/9 | `1` | 1 |
| **D60-GRID(3,12)** | footprint | 1, 0, 0, 0, 0, 0, 0, 0, 0 | 1/9 | `1` | 1 |

**The claim reads TRUE, two-way, at every one of the ten cells.** On all
four arbitration crystals, under both site readings, the field has a
nontrivial translation stabilizer: the division events of a conflict
crystal do form a crystal. On the declared counterexample control, under
both readings, the stabilizer is trivial: the division events of a
delivery crystal do not.

Two of the ten cells carry that positive on a **constant** field. At both
CONFLICT-GRID footprint cells the field is 2 everywhere and 4 everywhere;
a constant field on any finite group is stabilised by the whole group,
whatever record produced it, so those two cells are uninformative about
periodicity beyond the construction's own partition. The informative
arbitration cells are six of eight.

The control's other value is likewise forced rather than found. If
`H ≤ Z₃²` is nontrivial, the support of an `H`-invariant field is a union
of `H`-cosets, so its size is divisible by `|H|`; the control's support
is 1, which forbids any nontrivial `H` at either reading. What the
control demonstrates is that a delivery crystal has too few division
events to carry any spatial structure. The instrument's power to detect
*aperiodicity* is demonstrated separately, by the planted-aperiodic
mutant.

Each stabilizer is computed twice — once by translating the field
directly, once as the annihilator of the support of the exact Z₃² Fourier
transform in `Z[ω] = Z[t]/(t² + t + 1)`, running over the dual group. The
two agree element for element in all ten cells. That is the same field by
two **algorithms**, not two data routes: both consume the field and the
subgroup-naming function. The field-level independence is delivered one
gate later, by the head-equality gate, whose reconstruction rebuilds the
record, the marking and the site map.

**The site reading is not neutral, and the scout of record is corrected
where it spoke.** The scout's declared-data obligations paragraph
recorded "stabilizers AGREE, supports differ (6/9 vs 9/9)"; its own
PRELIMINARY, four lines earlier, had already flagged CONFLICT-GRID(3,2)'s
footprint field as constant at order 9, and it was silent on
CONFLICT-GRID(3,4). Measured: the two readings agree at 2 of the 4
arbitration crystals and **diverge at the other 2** — at both
CONFLICT-GRIDs the footprint field is constant and its stabilizer is the
whole group — and the supports are 6/9 against 9/9 only on the
DOUBLE-GRIDs, 3/9 against 9/9 on the CONFLICT-GRIDs. The relation between
the two readings is **containment**: the footprint stabilizer contains
the initiator stabilizer at all five records, strictly at the two
CONFLICT-GRIDs. "Never shrinks" is the measurement; "enlarges" would not
be. And `<(1,1)>` lies inside all eight arbitration cells, so the
invariance direction the four crystals share is the diagonal, at both
readings.

### 5.1 Where the periodicity comes from

The ten-cell table has a one-line mechanism and it is the constructors'.
On every crystal and at both readings the division field is **affine in
the indicator of the constructor's own seed set**:

```
n = c + m·1_S
```

where `S` is the set of sites the constructor seats its arbitrations on.
`S` is re-derived here from the seed rule in the committed constructor —
`double_grid` seats its row groups at `ac[i][i]` and its column groups at
`ac[(j+2)%g][j]`, `conflict_grid` seats both parities at `ac[i][i]`, the
control mints and arbitrates at `GRID[0]` alone — and never read off the
measured field. Measured, at all ten cells:

| crystal | reading | c | m | \|S\| | Stab(1_S) | Stab(n) |
|---|---|---|---|---|---|---|
| DOUBLE-GRID(3,2) | initiator | 0 | 3 | 6 | `<(1,1)>` | `<(1,1)>` |
| DOUBLE-GRID(3,2) | footprint | 4 | 1 | 6 | `<(1,1)>` | `<(1,1)>` |
| DOUBLE-GRID(3,3) | initiator | 0 | 4 | 6 | `<(1,1)>` | `<(1,1)>` |
| DOUBLE-GRID(3,3) | footprint | 6 | 1 | 6 | `<(1,1)>` | `<(1,1)>` |
| CONFLICT-GRID(3,2) | initiator | 0 | 2 | 3 | `<(1,1)>` | `<(1,1)>` |
| CONFLICT-GRID(3,2) | footprint | 2 | **0** | 3 | `<(1,1)>` | `Z3^2` |
| CONFLICT-GRID(3,4) | initiator | 0 | 4 | 3 | `<(1,1)>` | `<(1,1)>` |
| CONFLICT-GRID(3,4) | footprint | 4 | **0** | 3 | `<(1,1)>` | `Z3^2` |
| **D60-GRID(3,12)** | initiator | 0 | 1 | 1 | `1` | `1` |
| **D60-GRID(3,12)** | footprint | 0 | 1 | 1 | `1` | `1` |

The decomposition holds exactly at all nine sites of all ten cells, so
the stabilizer is forced arithmetic: `Stab(n) = Stab(1_S)` wherever
`m ≠ 0`, and the whole group wherever `m = 0` — which is the same two
cells the constant fields sit at, now identified as vacuous positives by
their mechanism and not only by inspection.

And on all eight arbitration cells `S` is a union of **full** `<(1,1)>`
cosets: the residues of `j − i` over `S` are {0, 1} on the DOUBLE-GRIDs
and {0} on the CONFLICT-GRIDs, every class complete, because d66 seats
its seeds at a uniform column offset. A seed set that is a union of
cosets of a nontrivial subgroup *cannot* fail to put that subgroup in the
stabilizer. On the control `S` is a single site, an incomplete residue
class, which is exactly why the control returns order 1.

So the claim is **TRUE and CONSTRUCTOR-INHERITED**, and the head says so.
Read with the mechanism, "the division events of a conflict crystal form
a crystal" says, on this arena: *these constructors seat their
arbitrations on a union of full diagonal cosets and schedule them
uniformly across rounds.* That the shared direction is the diagonal is
therefore d66's seed rule and not a property of division events — which
also settles §8's counterpoint, and is why §7.1 can say what the two
diagonals have to do with each other.

Whether any conflict-crystal constructor seats its arbitration seeds on
something *other* than a coset union is the open question, and it is not
asked here: it is S-U4-8, and it is the census U4b runs.

## 6. Geometry invariance

The geometry rows are D66's, over D58's atlas and D47a's `sky` kind B:
the chart width `max|D|`, the homogeneity fractions `|D| ≥ 2` and
`|D| ≥ 4`, the mean chart size, the mean overlap ω, each at depths 2 and
3, with the poset's longest chain as the height statistic. The
full-record rows reproduce v10's committed output exactly wherever v10
printed it.

### 6.1 The height control fires first, and it is empty

Two different objects go by the name "height control", and this section
separates them.

- **The KR discriminator** — the longest chain, reported alongside any
  dimension reading so that a Kleitman–Rothschild order is unmasked. The
  catalog's engraved requirement for this unit is that one, and it is
  met: the longest chain of every population this unit reads, full and
  sparse, is reported here and at §8.
- **The height-matched control population** — same size, same height
  histogram, drawn from unmarked events. That object is this unit's own
  (choice inventory row 10, class **free**), it is stricter than the
  wall demanded, and it is what is empty.

**Measured: the division events of every crystal are height-pure.** They
occupy whole height layers of the event poset and share those layers with
nothing else.

| crystal | division layers | longest chain | mixed layers | height-matched control |
|---|---|---|---|---|
| DOUBLE-GRID(3,2) | 1, 8, 9, 12, 13 | 14 | 0 | empty, deficit 18 of 18 |
| DOUBLE-GRID(3,3) | 1, 8, 9, 12, 13, 16, 17 | 18 | 0 | empty, deficit 24 of 24 |
| CONFLICT-GRID(3,2) | 1, 5 | 6 | 0 | empty, deficit 6 of 6 |
| CONFLICT-GRID(3,4) | 1, 5, 9, 13 | 14 | 0 | empty, deficit 12 of 12 |
| D60-GRID(3,12) | 1 | 21 | 0 | empty, deficit 1 of 1 |

A height-matched control therefore **cannot be built at any crystal**:
there is no unmarked event at any marked height. The obstruction is not
an artefact of matching within a record. Pooling the unmarked events of
all five records, 7 of the 8 marked heights are available somewhere, but
height 1 is available nowhere: layer 1 is marked-only on every one of the
five records, carrying 6, 6, 3, 3 and 1 marked events against 0 unmarked,
and every record has marked events there. Even a cross-record
height-matched control is unbuildable.

Every population-averaged row is consequently confounded with a height
shift for which this unit's control cannot be built, and it certifies
none of them. The KR wall is not what forbids those rows — the wall's own
discriminator is carried; what forbids them is the stricter control this
unit requires of itself, and its emptiness is a theorem given purity, not
a failure to look.

### 6.2 The row that survives the confound

A maximum over a subset equals the maximum over the whole set exactly
when the maximum is attained on the subset. The chart-width row is
therefore not a population average at all but an attainment statement,
which is why the empty height-matched control does not reach it: it says
which events carry the record's widest charts, not what a height-biased
population averages to. It is the row this section can carry.

| crystal | depth | full max\|D\| | attained at | of which marked | restricted max\|D\| | |
|---|---|---|---|---|---|---|
| DOUBLE-GRID(3,2) | 2 | 9 | 3 | 3 | 9 | INVARIANT |
| DOUBLE-GRID(3,2) | 3 | 9 | 9 | 3 | 9 | INVARIANT |
| DOUBLE-GRID(3,3) | 2 | 9 | 6 | 6 | 9 | INVARIANT |
| DOUBLE-GRID(3,3) | 3 | 9 | 21 | 6 | 9 | INVARIANT |
| CONFLICT-GRID(3,2) | 2 | 6 | 1 | 1 | 6 | INVARIANT |
| CONFLICT-GRID(3,2) | 3 | 6 | 6 | 3 | 6 | INVARIANT |
| CONFLICT-GRID(3,4) | 2 | 6 | 3 | 3 | 6 | INVARIANT |
| CONFLICT-GRID(3,4) | 3 | 6 | 16 | 9 | 6 | INVARIANT |
| **D60-GRID(3,12)** | 2 | 3 | 8 | 0 | 1 | **VARIES** |
| **D60-GRID(3,12)** | 3 | 3 | 12 | 0 | 2 | **VARIES** |

The row is invariant at 4 of 4 arbitration crystals at both depths and
varies at the control at both depths, so the segment's two-way
requirement is discharged on the row that carries it. At depth 2 the
statement is sharper than survival: on all four arbitration crystals the
widest charts in the record are centred *exclusively* on division events
(3 of 3, 6 of 6, 1 of 1, 3 of 3), while on the control not one of the
widest charts is (0 of 8). The sharpening is confined to depth 2; at
depth 3 the widest charts are not exclusively marked.

### 6.3 The rows that are reported and not certified

Printed exactly, at depth 2, full → restricted:

| crystal | \|D\| ≥ 2 | \|D\| ≥ 4 | mean \|D\| | mean ω |
|---|---|---|---|---|
| DOUBLE-GRID(3,2) | 4/9 → 1/3 | 5/72 → 1/6 | 47/24 → 7/3 | 92/165 → 1/3 |
| DOUBLE-GRID(3,3) | 47/96 → 1/2 | 1/12 → 1/4 | 71/32 → 13/4 | 137/246 → 1/3 |
| CONFLICT-GRID(3,2) | 2/5 → 1/2 | 1/10 → 1/2 | 3/2 → 5/2 | 113/210 → 23/90 |
| CONFLICT-GRID(3,4) | 16/33 → 3/4 | 3/22 → 3/4 | 41/22 → 15/4 | 299/590 → 23/90 |
| D60-GRID(3,12) | 1/2 → 0 | 0 → 0 | 67/46 → 1 | 101/258 → none |

Every one of these movements is inseparable from the height shift of
§6.1. `BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL` is this unit's reading of
them — neither INVARIANT nor VARIES.

### 6.4 The sparse record is a different object

Arm (a)'s second sub-reading rebuilds the poset on the marked events
alone. It is reported as data and no invariance claim is made across the
two posets: at depth 2 `max|D|` reads 3, 3, 0, 3, 0 against the full
records' 9, 9, 6, 6, 3, and the longest chain reads 5, 7, 2, 4, 1 against
14, 18, 6, 14, 21. Two features are worth a successor's attention: the
sparse width is exactly 3 on every crystal whose sparse record has a
nonzero one, and the mean overlap ω is exactly 1 wherever the sparse
record has a cover to average over — on those records every cover's chart
is contained in its successor's. CONFLICT-GRID(3,2) and the control have
no cover whose chart carries two or more directions, so no value is
averaged and none is reported.

### 6.5 Arm (b): the renewal-only rebuild is not constructible

The declared sub-grammar keeps the two record-bearing tags and drops the
two the `[POSIT]` calls kinematics. Under it **no crystal can be
rebuilt**, and every refusal is located:

| crystal | events before the refusal | refusal |
|---|---|---|
| DOUBLE-GRID(3,2) | 12 | `D00->D01` at prefix 12 |
| DOUBLE-GRID(3,3) | 12 | `D00->D01` at prefix 12 |
| CONFLICT-GRID(3,2) | 12 | `G00->G10` at prefix 12 |
| CONFLICT-GRID(3,4) | 12 | `G00->G10` at prefix 12 |
| D60-GRID(3,12) | 2 | `spread G00->G01` at prefix 2 |

Each stops at its first delivery. A refusal is recorded, never patched.

The isolation control settles which tag is load-bearing: dropping *only*
the idle tag rebuilds every crystal **event for event** — 72, 96, 30, 66,
46 events, records identical to the committed ones. The crystals need no
idles at all. Exactly one kinematic tag blocks the renewal-only rebuild,
and it is the delivery.

### 6.6 What the falsifier does and does not say

paper 0 §10's third falsifier reads: "If U4 shows sparse records destroy
the geometry, kinematics and law are not separable as posited". **It does
not fire.** Nothing here shows sparse records destroying a geometry.

Nor does anything here show them preserving one. On this arena the
falsifier is **not evaluable**: under arm (a)-POP the poset is held whole
by construction, so no geometry could vary; under arm (a)-SUB the
geometry does change substantially, but the two posets are different
objects and the comparison is refused (§6.4); under arm (b) the object
does not exist. Three sub-readings, no evaluable test. The falsifier does
not fire because it cannot be evaluated here, not because it was tested
and returned negative — and a reader must not take its silence for
support in either direction.

What fires is a prior obstruction the falsifier does not name: on this
arena the sparse record is not *constructible*, because the crystals'
construction consumes deliveries. That is a weaker and different
statement than the falsifier's, and it is not evidence that kinematics
and law fail to separate — it is evidence that the kinematic layer is a
necessary scaffold for building this particular record, which the
constructors already said in prose ("delivery-free *after the
bootstrap*"). The unit declines to route it into §10.

The spatial rows of §7 — the co-division link counts — are functions of
the marked events alone and are therefore invariant under every
renewal-only operationalization that preserves the marking. That is a
tautology of the definition. It is stated here so that it is never
counted as evidence, and it is excluded from the geometry verdict.

## 7. The bridges, at declared scope

Three bridge objects are measurable on this arena, and no more.

**The co-division adjacency.** For a link `l` and a site `x`, the number
of division events whose footprint contains both `x` and `x + l`.

| crystal | axis (1,0) | axis (0,1) | diagonal (1,1) | diagonal (1,2) |
|---|---|---|---|---|
| DOUBLE-GRID(3,2) | 2 at every site | 2 at every site | 0 at 9 of 9 | 0 at 9 of 9 |
| DOUBLE-GRID(3,3) | 3 at every site | 3 at every site | 0 at 9 of 9 | 0 at 9 of 9 |
| CONFLICT-GRID(3,2) | 1 at every site | 1 at every site | 0 at 9 of 9 | 0 at 9 of 9 |
| CONFLICT-GRID(3,4) | 2 at every site | 2 at every site | 0 at 9 of 9 | 0 at 9 of 9 |
| **D60-GRID(3,12)** | 0 at every site | 0 at every site | 0 at 9 of 9 | 0 at 9 of 9 |

The axis counts are homogeneous and strictly positive on all four
arbitration crystals — the bridges are the rook's graph's rows and
columns — and identically zero on the control, which carries no bridges
at all.

**The support's coset structure.** At the initiator reading the
sublattice's support is a union of full `<(1,1)>` cosets: two cosets on
the DOUBLE-GRIDs (the residues 0 and 1 of j − i), one on the
CONFLICT-GRIDs (residue 0). The control's support is a single site, whose
residue class is not filled and which is therefore no coset union. This
is the sublattice-is-a-crystal statement read on the set rather than on
the counts, and it agrees with §5.

**The record-order legs.** The gaps between consecutive marked events:

| crystal | leg multiset |
|---|---|
| DOUBLE-GRID(3,2) | 1 × 10, 2 × 5, 19 × 1, 31 × 1 |
| DOUBLE-GRID(3,3) | 1 × 15, 2 × 5, 19 × 2, 31 × 1 |
| CONFLICT-GRID(3,2) | 4 × 2, 6 × 3 |
| CONFLICT-GRID(3,4) | 4 × 2, 6 × 9 |
| D60-GRID(3,12) | empty |

paper-09 §4's support holes — no inter-renewal leg of length one or two —
carry a two-actor *delivery-free* scope tag, and this arena is neither
two-actor nor delivery-free. The DOUBLE-GRIDs' legs of length 1 and 2 are
therefore a **comparison across scopes, not a test** of that law, and are
reported so a successor at matched scope can use them. The CONFLICT-GRIDs
are supported on exactly two leg lengths.

**No indivisibility claim is made, and on this arena none is definable.**
The pin scopes this section to what the arena can measure, and none of
the three objects is a transition kernel. The reason is structural rather
than circumstantial: all five records are FORCED, `maxhits = 1` at every
one, so the menu never offers a choice and there is no branching for a
kernel to describe. The founding spec's own clause — that the bridges are
"probed for indivisible structure" — is therefore not merely unrun here
but **unposable as the arena is declared**. Where the geometry is
cleanest, the stochasticity is gone. The candidate readings are named and
left as candidates: (i) the axis link counts as the crystal's own `q₁₁`
and `q₂₂`; (ii) the leg multiset as a crystal-scope analogue of
paper-09 §4's `g(n)`; (iii) the coset support as the renewal sublattice's
own period lattice.

### 7.1 The diagonal, unified

Before U4 the crystal side of the weld-2 question was an event record.
This unit delivers, for the first time, an object of the same species as
the deformation side's: a site set Z₃², a link-indexed count field and a
measured symmetry group. So the comparison can be made like for like, and
it is made here — once, to record what it returns.

I7's arena, read as data from weld 2 (`9cdb10472953`) and not
re-authored: sites Z₃²; links {(1,0), (0,1), (1,1)}; a geometry record
`n_ℓ(x)` strictly positive at each of the 9 × 3 = 27 cells; and the
readout `q₁₁ = n_{e₁}`, `q₂₂ = n_{e₂}`,
`q₁₂ = (n_{e₁+e₂} − n_{e₁} − n_{e₂})/2`. **I7's third link is the
diagonal.** Evaluating this unit's bridges on those coordinates:

| crystal | n(1,0) | n(0,1) | n(1,1) | q₁₁ | q₂₂ | q₁₂ | det | cells > 0 |
|---|---|---|---|---|---|---|---|---|
| DOUBLE-GRID(3,2) | 2 | 2 | 0 | 2 | 2 | −2 | **0** | 18 of 27 |
| DOUBLE-GRID(3,3) | 3 | 3 | 0 | 3 | 3 | −3 | **0** | 18 of 27 |
| CONFLICT-GRID(3,2) | 1 | 1 | 0 | 1 | 1 | −1 | **0** | 18 of 27 |
| CONFLICT-GRID(3,4) | 2 | 2 | 0 | 2 | 2 | −2 | **0** | 18 of 27 |
| **D60-GRID(3,12)** | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0 of 27 |

Three things follow, and none of them is a new physical claim.

**The renewal sublattice fills 18 of I7's 27 cells and fails exactly the
9 diagonal ones.** The axis cells are strictly positive and
translation-homogeneous; the diagonal cells are zero. By I7's own
strict-positivity criterion the FOUND-side arena is inadmissible there,
at the same link, for the same reason that decided the crystals on the
deformation side.

**The induced form is degenerate at every site of every crystal.** With
the diagonal count zero and the two axis counts equal and homogeneous the
form is `c·[[1,−1],[−1,1]]`, whose determinant is identically zero — an
independent reproduction, from the FOUND side, of weld 2's committed
`INDUCED-DET=0-AT-EVERY-SITE-OF-EVERY-CRYSTAL`, by a route weld 2 did not
have. Its kernel is spanned by `(1,1)`: the direction the induced metric
is blind along is the direction §5 measures as the division field's
period.

**Both appearances of (1,1) are one cause, not two witnesses.** §5.1
measured why the count field is `<(1,1)>`-periodic: d66 seeds conflict on
`<(1,1)>`-cosets. The same constructor groups by rows and columns, which
makes the link set the two axes and leaves the diagonal empty. One design
choice, two shadows. A successor must not count them as independent
evidence, and the "counterpoint" of §8 is not a coincidence needing an
explanation — it is the same fact seen twice.

The consequence for the successor line is that the renewal-crystal weld
census is **predictably empty at this family**: 18 of 27 positive and
homogeneous, 9 diagonal cells zero, determinant identically zero, kernel
`<(1,1)>`, at every one of the four arbitration crystals. This unit does
not run that census — running it would record a verdict already
determined — and the question that remains live is not "what does the
census return here" but "does any admissible schedule move the
determinant off zero". That is a column of U4b's table (§12), and it is
where the weld arena would have to be found if it exists.

## 8. The walls

The pin engraves four. Violations of them would be construction errors,
not findings.

**L-1 — the fourth form, argued before any test, and then declined.**
L-1 (`93ea24591c3c`) records that order-level covariance "is a **fourth
form, outside paper 8's three**, and its admissibility is v11's to argue
when U4 runs". The argument owed here is therefore prior to any test, and
it is this. Admissibility would require two things: a group declared to
act on the *generated causal order*, and a reason to read that group as a
covariance group. This arena supplies five finite records and a
translation action on their *site lattice*; the corpus contains no bridge
from Z₃² translations to any boost, and this unit constructs none. **The
fourth form is therefore not tested here.** It remains unargued and
untested and is registered for a successor.

The sentence retracted on 2026-07-28 is not reproduced, and the program
gates its absence from both this paper and its own source **as prose is
written**: two needles — the retracted sentence and the corpus's own
canonical short fragment, the one v11's text-anchor unit registers as
L1-A16 — are matched with whitespace normalised on both sides, so a
line-wrapped reproduction is caught exactly as a contiguous one is. Each
needle is itself anchored against the pinned paper-0 erratum that carries
the retracted wording, so a mis-transcribed needle cannot pass the gate
vacuously.

What *is* measured falls inside L-1's own scope guard, which states that
the lemma "does **not** forbid a permutation action". The Z₃²
translation stabilizer of §5 is a permutation action on the actor set —
measured as such: each of the nine translations acts on the nine sites as
a bijection, and each crystal's actor-to-site map is gated a bijection.
It needs no fourth-form argument at all, and that is why it is the
measurement this unit runs.

**BHS — no sprinkling-grade Lorentz-invariance test.** The catalog
records that v11's "crystals are finite-valency by construction, so BHS
says their renewal sublattice **cannot** be statistically
Lorentz-invariant in the sprinkling sense". Running the test would
manufacture a false negative. None is run, and the absence is measured
rather than declared: every measurement row this unit computed is scanned
for the tokens that would betray such a test — sprinkling, boost,
rapidity, frame, Lorentz — and carries none of them. (The scan excludes
the pinned-source list, which names L-1's own filename and is provenance
rather than measurement.) paper 0 §7 attaches two
catalog tests to U4 as riding along; this is the one that does not ride.

**Kleitman–Rothschild — every dimension reading carries its height
statistic.** The only dimension-adjacent row read here is the chart
width, and §6.1 and §6.2 report it with the longest chain of every
population it is read on, full and sparse. The KR discriminator is the
longest chain — KR orders return 3 where a sprinkling of comparable size
returns tens — and no population here returns 3. No Myrheim–Meyer
estimate is run at all. The second catalog test paper 0 §7 attaches to
U4, the max-shatter dimension meter as acceptance gauge, is **not** run,
and not because the KR discriminator is missing — it is carried. It is
not run for two other reasons: the catalog grades max-shatter a
1+1-escape detector and explicitly *not* a dimension estimator, and at
n ≤ 24 marked events with heights ≤ 7 no acceptance gauge on these sparse
posets could discriminate anything. The object that is empty in §6.1 is
this unit's own stricter height-matched control population.

**The diagonal — `q₁₂ ≡ 0` is inherited, and the question is not answered
here.** The co-division graph is the rook's graph; diagonal pairs share
neither row nor column, and §7 measures the diagonal link count
identically zero at 9 of 9 sites on every crystal. That is inherited, not
found. §7.1 assembles I7's coordinates for one purpose only — to record
that the induced form is degenerate at every site of every crystal, so
that no metric is read off it here and the census that would read one is
answered before it is posed. The apparent counterpoint — the field's
invariance direction is the diagonal `<(1,1)>` while the diagonal link
count is identically zero — is not read as a tension: §7.1 measures that
both descend from the same constructor choice. Whether a carrier exists
that *populates* a diagonal pair is the scout's S1, which belongs to the
≥9-actor line, not to this one.

## 9. Choice inventory

Classified at the RSQ standard; fibers computed, not asserted.

| # | item | class | fiber | where it binds |
|---|---|---|---|---|
| 1 | the arena: which five crystals | **forced** | 1 | pin R1, from the committed constructors |
| 2 | the control's identity | **forced** | 1 | pin R1 names D60-GRID(3,12) |
| 3 | the marking: division = arbitration tag | **forced** | 1 | paper-09 §3, three rows, one reaching this arena (§3) |
| 4 | the site carrier: actors → Z₃² | **forced** | 1 | the constructors' own actor naming, gated as a bijection |
| 5 | the site reading (initiator / footprint) | **declared** | 2 | both arms run; §5's table is per reading |
| 6 | the renewal-only operationalization | **declared** | 3 | (a) and (b) run, (c) registered |
| 7 | arm (a)'s sub-reading (POP / SUB) | **declared** | 2 | both run; §6.2–§6.4 are per sub-reading |
| 8 | arm (b)'s sub-grammar shape | **declared** | 1 | D74's `filt` shape, support-restricting only |
| 9 | the geometry row set | **forced** | 1 | D66's rows over D58/D47a, reproduced at v10's numbers |
| 10 | the height-matched control's construction | **free** | — | this unit's, and stricter than the wall requires; deterministic, and it returns empty everywhere |
| 11 | the stabilizer as the periodicity measure | **free** | — | this unit's; the pin names the stabilizer, not its algorithm |

Two free items, both instrument-side and both two-way-gated. No free item
enters the verdict's data — though free item 10's *name* is the one the
geometry verdict string carries, which §6.1 and §10 gloss.

## 10. Verdict

```
U4-THE-DIVISION-EVENTS-FORM-A-CRYSTAL-CONSTRUCTOR-INHERITED-[DG32:<(1,1)>/<(1,1)>|DG33:<(1,1)>/<(1,1)>|CG32:<(1,1)>/Z3^2|CG34:<(1,1)>/Z3^2|CTRL:1/1]
```

```
GEOMETRY-INVARIANT-AT-THE-CONTROLLED-ROW-REST-BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL
```

Read out: **the division events of a conflict crystal do form a crystal,
at both site readings, on all four arbitration crystals, and do not on
the declared counterexample control — and the periodicity is inherited
from the constructors, not emergent from the dynamics.** The field is
affine in the constructor's seed indicator at all ten cells, so the
stabilizer is the seed set's; at the two CONFLICT-GRID footprint cells
the field is constant, every actor sitting in exactly one arbitration
footprint per round, and the whole-group stabilizer there is less
structure rather than more. The shared invariance direction is the
diagonal `<(1,1)>`, and it is d66's seed offset. The footprint stabilizer
contains the initiator's at all five records and is strictly larger at
the two CONFLICT-GRIDs.

The geometry is invariant on the one row a population restriction cannot
confound and blocked on every row it can, because the *height-matched
control population* — this unit's own object, not the KR discriminator,
which is carried — is provably empty on this arena; and the renewal-only
*rebuild*, as opposed to the renewal-only *reading*, is not constructible
in the committed grammar at all.

**What this unit does not deliver.** Of the five things paper 0 §7
attaches to U4, this unit discharges one — the crystal claim — blocks the
geometry at every row a population restriction can confound, and refuses
three. The indivisibility probe is refused because it is undefinable
here: on a forced, unbranched record there is no transition kernel to
probe (§7). Sprinkling-grade statistical Lorentz invariance and the
max-shatter dimension meter are refused under the pin's own walls (§8).
**Phase III's relativity test has not been run here, and nothing in this
unit bears on relativity.**

Between delivery and adjudication every headline reading here is a
candidate reading.

## 11. Deviations, priced

1. **The pin names weld 2's SEC 6 as the primary constructor route
   (`290149118b9d`); this unit does not read that file.** A weld-2 repair
   worker held it under concurrent rewrite when this unit was built, and
   rule #91 forbids reading a live worktree state. The constructors are
   rebuilt from the v10 originals' definitions instead, at their pinned
   shas, and gated against the v10 originals' *committed output*. Price:
   the v14 self-contained route is not this unit's witness. Mitigation:
   the substitute provenance is strictly older and strictly more anchored
   — forty-two committed numbers reproduce, each read out of the line it
   cites, against the zero that reading a rewritten file would have
   carried. The pin's cross-check obligation is met in full.

2. **The head's outcome NAME is extracted from the pin by both paths, and
   its QUALIFIER from the adjudication by both paths, so the two paths
   share two inputs.** A pre-registered outcome name has nowhere else to
   come from, and neither does a qualifier a ruling fixes. The four
   extractors are pairwise different (a whole-file backtick span scan; a
   section-scoped character scan that rejoins hyphenated line breaks; two
   regexes keyed on different sentences in different sections), and the
   head's *data* — the ten-cell stabilizer table — shares no code, no
   derived input and no typed literal between them.

3. **The reconstruction shares the arena, and one function.** The five
   records are the object of study, not the instrument; there is no second
   constructor for them in the corpus. Downstream of the record the two
   paths share exactly one thing and it is named: `regs_of`, which *is*
   the footprint reading. The marking predicate, the site map, the field
   and the stabilizer algorithm are unshared. Within §5 the two
   stabilizer routes additionally share the field and the subgroup-naming
   function, so that pair is an algorithm cross-check and is described as
   one.

4. **Arm (a)-SUB is reported and not certified**, because the sparse
   record's poset is a different object from the crystal's and no
   invariance claim can cross the two.

5. **The pin's `GEOMETRY: INVARIANT / VARIES-<witness>` pair does not fit
   the measurement.** A third value is emitted, and it is the corpus's
   standard third value: BLOCKED, at a named object. The pre-registered
   VARIES path is not thereby unreachable, and the demonstration is at
   segment level: under the registered geometry mutant the segment
   verdict itself is emitted as `GEOMETRY-VARIES-<witness>` before the
   gates kill the run. The witness list is bound to the verdict by its own
   gate, and the control's *required* variation is carried in a separate
   field so that it can never be mistaken for a falsifier witness.

6. **Two catalog tests that paper 0 §7 attaches to U4 are not run** —
   sprinkling-grade statistical Lorentz invariance, and the max-shatter
   dimension meter. Both are refusals under the pin's own walls (§8), and
   both are registered below rather than silently dropped.

7. **Pin R2 asks the marking to be gated against the source *rows*,
   plural; only one row has a referent at nine actors.** §3 discloses
   this: the class-0 clause is a two-actor delivery-free notion, and S4's
   pair hypothesis is vacuous here — 0 pair arbitrations of 61. Price:
   the marking is corpus-anchored at one row. Mitigation: the two silent
   rows are discharged by two independent re-derivations that share no
   code with the tag — a tag-free shape predicate selecting the identical
   set index for index, and the renewal-to-root property at 61 of 61.

## 12. Successor register

- **S-U4-1.** The fourth form — order-level covariance on a generated
  causal order — remains unargued and untested. Its admissibility
  argument is still owed, and this unit's decision not to supply it is
  scoped to this arena, not general. Separately, paper 8's admissible
  form 2 — projective compatibility of different finite batteries —
  survives both L-1 and the BHS block by L-1's own record and is neither
  run nor argued here; it remains the one admissible covariance form
  available to a successor on this carrier without a fourth-form
  argument.
- **S-U4-2.** The max-shatter dimension meter as acceptance gauge is
  posable once a carrier's sparse posets are large enough for the meter
  to discriminate, and — for any *population* comparison against the full
  record — once its division events are not height-pure. The KR height
  statistic itself is available already; it is not the obstruction.
- **S-U4-3.** Height purity is the sharpest structural fact this unit
  found and it was not predicted anywhere: the division events fill whole
  height layers of the event poset and share them with nothing else, on
  all five records including the control, and layer 1 is marked-only
  across all five pooled. Whether that is a theorem about the grammar or
  an artefact of these five schedules is open.
- **S-U4-4.** The sparse record's chart width is exactly 3 on every
  crystal whose sparse record has a nonzero one, and its mean overlap ω is
  exactly 1 wherever it is defined. Neither is explained here.
- **S-U4-5. Answered, and closed.** The reading divergence is
  one-directional because the footprint field is `(group multiplicity) +
  1_S` while the initiator field is `m·1_S`, and the group system carries
  at least the seed set's symmetry, so the footprint stabilizer contains
  the initiator's. What remains open is narrower and is folded into
  S-U4-8: whether it holds for a constructor whose group system is *less*
  symmetric than its seed set.
- **S-U4-6.** The renewal-only *rebuild* is blocked at the delivery on
  every crystal. Whether any conflict crystal is constructible
  delivery-free from the empty history is a well-posed successor question
  and this unit did not ask it.
- **S-U4-7.** The diagonal counterpoint is dissolved rather than left
  standing (§7.1): the field's period direction and the link structure's
  empty diagonal are one constructor choice seen twice. What remains is
  the scout's S1 — a carrier that *populates* a diagonal pair — and it is
  the single unblocking move for both weld 2 and the renewal census.
- **S-U4-8. The census that turns the constructor into a variable**, and
  the reason this unit's headline is qualified rather than emergent:
  whether any admissible arbitration schedule seats its seeds on
  something other than a coset union, and what happens to the stabilizer,
  the forcedness and the induced determinant when it does. The affine
  mechanism supplies the null hypothesis — any coset-union seed yields
  `Stab ⊇ H` by arithmetic — so the information is in the beyond-coset
  schedules. Ruled next and pinned as **U4b (paper-17)**, with the
  induced-metric determinant column carrying the weld-arena question
  §7.1 hands forward.
- **S-U4-9.** Registered siblings, not part of U4b: the law-side
  stochastic-crystallization unit (compute-windowed), and the
  diagonal-populating constructor of the scout's S1 as the weld arena, if
  U4b's determinant column comes back empty.

## 13. Instrument and reproduction

One self-contained program, `v14/code/u4_crystals_exact.py`, at the #82
CLI contract: no arguments is the plain run; `--selftest`, `--numbers`
and `--mutant NAME` are the whitelist; every other argv, and every
unregistered mutant name, exits 2.

- **Exact arithmetic** throughout — `fractions.Fraction` and integers, no
  float anywhere, including the Fourier reconstruction, which runs in
  `Z[ω]` by integer coefficient reduction.
- **Provenance.** Nineteen pinned sources, each read at its sha256-12 and
  gated per file; a run that cannot reach them fails loudly at
  `G-PROV-ROOT` and writes nothing. Eighteen verbatim anchors (#62), each
  bound by name to the gate that consumes it and each gated for length,
  so that a quote truncated to a fragment that trivially occurs cannot
  pass as an anchor.
- **Committed numbers are read, not typed.** Each of the forty-two
  committed-number anchors resolves its own citation to a line of the
  pinned v10 output and extracts the committed value from that line by a
  context-keyed regex; the extraction, not the typed rendering, is what
  the computed value is compared against, and the typed rendering
  survives as a third check per row.
- **Per-object gates (#87)** throughout: per crystal, per reading, per
  arm, per depth. No aggregate predicate carries a verdict.
- **The head is derived, not typed**, and passes a complete-string
  equality gate against the independent reconstruction described in §5
  and priced in §11.
- **A gate's words are bound to its own boolean.** Gates whose statement
  carries a polarity — forced or refused, pure or mixed, invariant or
  varying, zero or populated, inherited or independent — declare the
  fragment their verdict requires and the fragment it forbids, and a
  statement inverted while its number is left intact cannot ship.
- **The published object is sealed at gate time.** Every gate, anchor,
  verbatim anchor, waiver and payload row is digested when it is created;
  the artifacts are rendered from those sealed copies rather than from
  live memory; the emitted output is folded into a byte seal as it is
  emitted; and the integrity gate recomputes every digest **from the
  bytes on disk** and compares them against the gate-time seal. Anything
  altered between a gate and the disk — an output line, a gate row, a
  gate's passed flag, a payload row, a published table cell — fails there
  and nothing is written.
- **Failing runs write nothing.** Artifacts are written to temporaries,
  re-read from disk, and only then renamed.
- **verify-paper runs inside the plain run.** Every numeral in this paper
  is checked against numbers the run computed, after masking seven named
  identifier classes; the meaning-binding half checks that the per-crystal
  counts, every stabilizer name, the head and the geometry verdict occur
  verbatim here.
- **Reproduction.** The plain run is byte-reproducible; it was run twice
  and the artifacts compared byte for byte. It was also run from a copy of
  the repository with `.git` removed, reproducing byte for byte, and from
  a location outside the repository, where it fails loudly at
  `G-PROV-ROOT` and writes nothing — the two halves of #91's off-tree and
  git-less requirement.
- **Mutants, and the honest denominator (#34).** Twenty-six registered,
  each naming the gate it must die at; those names resolve to nineteen
  distinct gate instances, every one of them verified to exist in the run
  and to appear in the receipt, and each mutant run refuses unless the
  gates it actually died at include its registered target. Two gate
  instances in the run carry a declaration rather than a measurement and
  are labelled `DECLARED` in every row; every other gate's verdict
  argument is a measured quantity. The suite includes the two the pin
  requires — a planted aperiodic division, which kills the crystal claim
  at its own crystal's stabilizer gate, and a planted full-period field
  on the control, which kills the control — one that drives the geometry
  **segment verdict** onto the VARIES path, one that reproduces the
  retracted sentence in this paper's own line wrapping, one that inverts
  a gate's prose while leaving its number, one that truncates a verbatim
  anchor, one that perturbs a single stabilizer route without the other,
  one that reports a tie-broken record, one that transposes two actors in
  the site map without breaking its bijectivity, and six that tamper with
  a published row after its gate has fired.
