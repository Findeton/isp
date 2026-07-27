# D66 — result: **A-IIIa. CONFLICT TILES; the width ceiling is `k·b ≤ k²`, SATURATED by a delivery-free DOUBLE GRID that is in-band at `d = 3` while `max |D| = 9`; the class is trivial at every convention; W4c is PROVED.**

**Status: ROUND-1 REVIEWED AND REPAIRED, 2026-07-27.**  An independent
hostile review — `v10/reviews/d66-round1-hostile-review.md`, a worker
with no prior context and no loyalty to the unit, every number
recomputed with its own driver and its own instrument — returned
**REVISE: 1 BLOCKER / 5 MAJOR / 8 MINOR / 4 NIT**, reproduced every
published figure of the first version exactly, and then **broke the
unit's headline with two constructions of its own**.  All eighteen
findings are carried below; §9 is the corrections section and names
the two mechanism sentences that are **REFUTED**.  Pin
`note-d66-arbitration-crystal-pin.md` (STRICT, FROZEN AND COMMITTED
before the receipt existed).  Receipt
`v10/code/d66_arbitration_crystal_exact.py`, output
`v10/data/d66_arbitration_crystal_exact.out` — **29 PASS / 0 FAIL,
exit 0, 962.3 s wall clock** (run from the repo root; 20 PASS before
the repair, and nine of the twenty-nine gates are new).
Parents: D63 (the wide crystal; W4b; residue 1 — the arbitration route
to width past 4), D64 (TERMINAL — the delivery atlas is a coboundary,
and its residue 1: *can any substrate carry a non-coboundary class?*),
D65 (the descent defect at conflict-group visibility),
D60/D58/D47a/D55c (the tiling blueprints, the atlas, the sky, the
sprinkling controls), D42b1 (the transport grammar).

---

## 1. Which outcome fired

The pin pre-registered four outcomes and let the sweep decide.

> **A-IIIa FIRED.**  Twenty-one conflict configurations, 2,325
> events — **zero refusals**, every event offered by the committed
> layer's own menu and specified by its FULL EVENT TUPLE — tile at
> cadence.  The pin's
> **A-I does not fire**: conflicts *can* be re-supplied every round.
> **The width door OPENS**: `CONFLICT-GRID(3, ·)` carries
> `max |D| = 6`, `CONFLICT-GRID(4, 4)` carries `max |D| = 8`, and
> **`DOUBLE-GRID(3, R)` carries `max |D| = 9 = k²` — W4c's own ceiling,
> SATURATED** — all at `d = 2`, the first records in this campaign past
> the delivery grammar's ceiling of 4.  And **A4 decides A-IIIa**: on
> the wide record all three coboundary routes return **zero
> obstructions** at all five port conventions and both depths.

The pin's stated lean was that **tiling is the hard part**.  It was
half right.  The half it got wrong was first read as "the schedule that
maximises the conflict share is the one that cannot tile widely" — and
round 1 **refuted that reading** (§2, §9).

## 2. The design problem the pin named, solved and measured

Arbitrations consume their conflicts, so a conflict crystal must
re-supply a *shared base* every round.  The layer supplies half the
answer for free — `View.holdings` gives the minted version to **every
proposer**, not only the arbitrator — so a pair that arbitrates
together needs **no delivery** to conflict again.  What costs a
delivery is **rotation**: partners that were not together last round
hold different, mutually superseded versions.

> **THE CONFLICT BUDGET BOUND [THEOREM, verified].**  An arbitration's
> `ckey` is a set of `k` live proposal triples and a proposal is
> resolved by at most one arbitration, so `#proposals ≥ k · #arbs` and
> the arbitration share of any record of this layer is at most
> `1/(k+1)`, with `k` the smallest proposer count in it.  Deliveries
> only lower it.
>
> **THE STEP THE PRINTED PROOF SKIPPED (round-1 MINOR 3).**
> `View.resolved` is **view-relative** — rebuilt from the arbitrations
> in one event's causal past — so by itself it does not exclude two
> causally *incomparable* arbitrations each seeing the same triple
> live.  The register argument closes it: two arbitrations consuming
> the same proposal triple both carry that proposer's register in
> `regs_of`, and `event_poset` makes every later event touching a
> register inherit the whole past of the previous one, so they are
> **causally comparable**; the later one's `View` has the triple in
> `resolved`, its component is gone from `arb_components_in_view`, and
> `admissible` returns `False`.
>
> **Gated with the equality `#proposals = Σ k` and "no consumed triple
> occurs twice" on every swept record** (round-1 NIT 2: the gate
> measures the *stronger* per-arbitration equality, not the prose
> inequality, and is now labelled for it).
>
> **TWO BOUNDS, AND WHICH ONE A RECORD SATURATES — said precisely.**
> `k_min` is the smallest proposer count *anywhere* in the record and
> `1/(k_min + 1)` is the only **general** bound.  The delivery-free
> ring saturates it exactly at `1/3` (`k_min = 2`).  The DOUBLE GRID
> mints its six base lineages with **single-proposer** arbitrations in
> its bootstrap, so its `k_min` is 1 and its general bound is `1/2` —
> but **all of its conflict groups have `k = 3` and its arbitration
> share is exactly `1/(3+1) = 1/4`**: the rounds saturate the conflict
> bound and the bootstrap spends none of the slack.  Both readings are
> printed per record and the receipt gates both lists.

**Four schedule variants, all reported.**

| variant | in-round deliveries | arb share | `d = 2` homog | `d = 3` homog | `max |D|` |
|---|---|---|---|---|---|
| `RING(6,10)` `sticky = 1` (rotate every round) | 27 | 10/39 ≈ 0.2564 | 0.6923 [in band] | 0.8974 [ABOVE] | 4 |
| `RING(6,10)` `sticky = 2` | 12 | 5/17 ≈ 0.2941 | 0.6471 [in band] | 0.5882 [below] | 4 |
| `RING(6,10)` `sticky = 0` (never rotate) | 0 | **1/3 — SATURATED** | 0.6000 [below] | 0.2667 [below] | **2** |
| **`DOUBLE-GRID(3,4)`** (two concurrent conflicts per actor) | **0** | **1/4 — SATURATED** | 0.5167 [below] | **0.7833 [IN BAND]** | **9** |

*("band" = the re-run sprinkling bands `[77/120, 4/5]` at `d = 2` and
`[41/60, 49/60]` at `d = 3`.)*

**The corrected design finding (round-1 MAJOR 1).**  The `sticky = 0`
ring is delivery-free *and* collapses to `max |D| = 2` — but that
collapse is a property of **one live conflict lineage per actor**, not
of delivery-freedom.  With one lineage the propose/propose/arbitrate
cycle is a **diamond**: two proposals fan out of an arbitration and fan
straight back into the next one, so the depth-2 layer is a single
event.  Give each actor **two standing conflicts** and the deliveries
vanish, the share still saturates, and the width comes back — nine
times over.  So:

> **THE DESIGN FINDING, RESTATED.**  What a crystal needs for a second
> direction is a **second concurrent consumer of the proposer's
> register**.  Rotation buys that consumer with a **delivery**;
> concurrency buys it for **free**, and a concurrent **arbitration** is
> a better consumer than a delivery — `b = k` instead of `b = 2`.  The
> maximum-conflict schedule is *not* the one that cannot tile widely:
> the widest record in this unit has **zero in-round deliveries**.

The winner convention is irrelevant: `win = R` and `win = ALT`
reproduce `win = S` in every column of every census.

## 3. The width verdict, the corrected width law, and W4c

**The door is open.**  `max |D|` at `d = 2` by proposer count `k` and
by live branching `Bl`:

| record | `k` | `B` (regs) | W4b `B²` | live `Bl` | W4c `Bl²` | measured `max |D|` at `d = 2` |
|---|---|---|---|---|---|---|
| any delivery circuit (D63), **at `d = 2`** | — | 2 | 4 | 2 | 4 | 4 |
| `CONFLICT-RING(M, R)` | 2 | **3** | **9** | **2** | **4** | **4** |
| `CONFLICT-GRID(3, R)` | 3 | 4 | 16 | 3 | 9 | **6** |
| `CONFLICT-GRID(4, 4)` | 4 | 5 | 25 | 4 | 16 | **8** |
| **`DOUBLE-GRID(3, R)`** | **3** | 4 | 16 | **3** | **9** | **9 — SATURATED** |

**The comparator row is depth-labelled (round-1 MINOR 7).**  "`max
|D| = 4` for any delivery circuit" is a **`d = 2`** statement.  D63's
own committed note reports that at `d = 3` its `max |D|` reaches 5 at
14 records and 6 at 4 more — **18 of its 38 delivery configurations
exceed 4 at `d = 3`** — and the receipt reprints `DR(8,10,8)`'s and the
brick's own `d = 3` rows beside the claim.

> **W4c — THE MINT-REGISTER REFINEMENT [THEOREM, PROVED].**  The
> version register an arbitration mints is a **birth wire**: it has no
> `P`-successor.  Replacing `|regs(x)|` by the number of registers of
> `x` that RECUR — the live out-degree `b(x)` — in W4b's own proof
> gives `|D_e(d)| ≤ Bl^d` with `Bl = max b(x)`, and for an arbitration
> `b ≤ #proposers = |regs| − 1`.
>
> **THE PROOF (round-1 MAJOR 3).**  The first version tagged this
> `[THEOREM, verified]` while its warrant was a per-record census — a
> *measurement* — and its printed reason ("`regs_of` places a version
> name in exactly one event's register set") was at the wrong level,
> since `regs_of` is a function of ONE event while "occurs once" is a
> property of the RECORD.  Four steps, each checked against the
> committed `d42b1` source, whose lines the receipt quotes verbatim and
> gates:
>
> 1. **A version occupies a register only where it is born.** `regs_of`
>    returns `{a}` for `p`/`n`, `{sender, receiver}` for `d`,
>    `{a, ('mw', a, pk)}` for `m`, and `props ∪ {vname(base, op[3],
>    op[1])}` for `r`.  **A delivery of version `v` therefore carries
>    `v` in its PAYLOAD `op[3]` and does NOT occupy `v`'s register** —
>    which is exactly why the minted wire is dead.  Merge-created names
>    (`mname`) never appear in any `regs_of` at all.
> 2. So a version register can recur only if **two distinct
>    arbitrations mint the same `vname`** — i.e. share the base, the
>    winner key's value tuple, its author tuple, and the initiator.
> 3. Two such arbitrations share at least one **proposer register**
>    (the winner authors, and the initiator, are proposers of both).
>    In `event_poset`, once an event touches register `r` it becomes
>    `last[r]` and every later event touching `r` inherits its whole
>    past — so the two are **causally comparable**.
> 4. The later one's `View` therefore contains the earlier
>    arbitration, so `base ∈ view.superseded`;
>    `arb_components_in_view` **skips** components whose base is
>    superseded, `admissible` finds no matching component and returns
>    `False`.  **The second arbitration is inadmissible. ∎**
>
> **CONSEQUENCE.**  A **two-proposer** conflict record has `Bl = 2`
> exactly like a delivery circuit and **cannot exceed 4 at `d = 2`**,
> despite carrying 3-register events.  **D63's "width past 4 at
> `d = 2` requires a 3+-register event" is true but NOT SUFFICIENT:
> what is required is 3+ distinct PROPOSERS.**
>
> The per-record census is kept beside the proof as evidence, not as
> its warrant: every version register occurs in exactly one event's
> `regs_of` on every record built here, and both bounds hold with zero
> violations at both depths.  **Round-1 NIT 1:** "an arbitration's live
> out-degree IS its proposer count" is an **inequality** `b ≤ k` — the
> last arbitration of each group at a record's end has `b = 0` — and
> the receipt prints the per-record count of arbitrations with `b < k`.
> Nothing turns on it (the bound uses the maximum), but the gate is
> labelled for what it measures.

> ### **THE WIDTH LAW, CORRECTED (round-1 BLOCKER 1).**
>
> The first version of this unit read `max |D| = 2k` off two schedules
> and printed it as **a law about `k`-proposer crystals** and as a
> mechanism ("each proposer contributes one direction per wire of its
> next delivery").  **That is false.**  `2k` is the value of the bound
> when every depth-1 successor of an arbitration is a **two-register
> event — a delivery** — which is what the RING and GRID blueprints
> impose and **nothing in the grammar forces**.  An arbitration's
> proposer register can be consumed by **another arbitration**: an
> actor may hold two live proposals on two distinct unsuperseded bases
> (`prop_options_in_view` blocks only a second live proposal on the
> *same* base).
>
> **The refinement, from W4c's own proof.**  Every `P`-edge raises the
> height by at least 1, so a depth-2 direction is reached from `e` by a
> `P`-path of length 1 or 2 — an **exact containment**, gated at every
> event of every record with zero violations:
>
> `D_e(2) ⊆ succ(e) ∪ ⋃_{y ∈ succ(e)} succ(y)`.
>
> When `e` has at least one successor at height `h(e) + 1` — i.e. when
> no `P`-edge out of `e` skips a layer — the first term contributes
> nothing at depth 2 and the bound is the sharp
> `|D_e(2)| ≤ Σ_{y ∈ succ(e)} b(y) ≤ b(e)·Bl ≤ k·Bl ≤ k²`.  **The
> exceptions to the sharp form are counted AND characterised rather
> than waved through**: they are exactly the events *all* of whose
> `P`-successors sit two or more layers above them (a height-skipping
> edge into a terminal arbitration at a record's end), and at every one
> of them `|D_e(2)| ≤ 1`.  The ceiling itself is W4c's `Bl^d`, gated
> with zero violations on every record — and it is **REALIZED AND
> SATURATED at `Bl² = k² = 9`**.
>
> **`2k` is the `Bl = 2` corner, not the law.  W4c's bound is TIGHT,
> and the widest chart in the campaign is 9.**

**The witnesses, exhibited rather than counted** (pin §5's demand that
a width claim not be an instrument artefact).  Both are read from the
**committed `d47a.sky`** directly, with every direction verified to be
ordered after the base in the **committed** `poset_of` order and to sit
exactly two height layers above it:

- `CONFLICT-GRID(4, 4)`, base event 4 — an arbitration by `G00` over
  **four distinct proposers**, 5 registers, height 1, live out-degree
  4; `|D| = 8` at directions 21, 24, 29, 31, 37, 39, 45, 47, all at
  height 3, role words `(p, 0)` and `(p, 1)` for `p = 0..3`.  (The
  round-1 review re-verified this witness event by event and confirmed
  it.)  This is the `2k` case: each successor is a **delivery**,
  `b(y) = 2`.
- **`DOUBLE-GRID(3, 4)`, nine bases** — three per round — each an
  arbitration over **three distinct proposers** whose three depth-1
  successors are themselves **three-proposer ARBITRATIONS**
  (out-degrees 3, 3, 3), giving `|D| = 9 = Σ b(y) = k·Bl = k²`.

**The smallest witnesses (`ARBCHAIN(m, k = 3)`).**  One `k`-proposer
arbitration whose `k` proposer registers are consumed by `m` further
`k`-proposer arbitrations and `k − m` deliveries gives
`|D_e(2)| = k·m + 2(k − m)` exactly:

| `m` | successor kinds | successor out-degrees | `|D_e(2)|` |
|---|---|---|---|
| 0 | `d, d, d` | 2, 2, 2 | **6 = 2k** (the RING/GRID case) |
| 1 | `r, d, d` | 3, 2, 2 | **7** |
| 2 | `r, r, d` | 3, 3, 2 | **8** |
| 3 | `r, r, r` | 3, 3, 3 | **9 = k²** (W4c's bound) |

So `2k` is not a law, not a ceiling and not even a typical value — it
is the `m = 0` corner of a one-parameter family whose other corner is
`k²`.  (These reproduce the **structure and the values** of the two
small witnesses the round-1 review built — its `|D| = 7` record had
successors `r, d, d` at out-degrees 3, 2, 2; its `|D| = 9` record had
three arbitration successors — with this unit's own blueprint.  They
are not the review's exact scripts and their event counts differ; the
review's were 26 events / 17 actors and 44 / 24.)

**What the door does NOT buy — restated with its depth label (round-1
MAJOR 2).**  The first version wrote "**No swept configuration is both
inside the homogeneity band and past the ceiling**" without a depth,
and inferred a mechanism ("the grids' shortfall is **not** an ends
effect") from an interior control run on **5 of 15** records at **one**
depth.  The receipt now runs D60's `C7` excision on **every** swept
record at **both** depths.  Corrected:

- **At `d = 2`**, in this family, width and tiling homogeneity do
  anti-correlate: the in-band-and-wide set has ten members, **every one
  of them `k = 2`** (round-1 MINOR 5: they are not all *rings* —
  `GRID(g=2, R=10)` is one of them, and by the receipt's A1(d) gate it
  is the `M = 4` ring under another name), while every `k ≥ 3` record
  sits below the band.
- **At `d = 3` the anti-correlation fails.**  The interior excision
  carries `GRID(3,6)` and `GRID(3,10)` **into** the `d = 3` band while
  they still carry `max |D| = 6` — exactly D63's ends effect — and
  `DOUBLE-GRID(3,4)` is **in the `d = 3` band outright** (0.7833) while
  carrying `max |D| = 9`.  **In-band and past the ceiling, at once.**
- Symmetrically, the rings' in-band property is a **`d = 2`** property:
  their `d = 3` homogeneity is 0.83–0.93, **above** the band, and their
  interiors are at 1.0000.

`ω` is reported per D58's reading (a chart-size ratio along covers,
never a symmetric overlap): 0.75 for every rotating ring, 1.0000 for
the delivery-free ring (thin charts, as the statistic's bias predicts),
0.44–0.51 for the grids, 0.5566 for the DOUBLE GRID.

## 4. The coboundary gate (A4), and the first non-zero obstruction

**The instrument is D64's, unmodified, and it is anchored.**  This
receipt re-runs D64's own `reg_tuple` / `out_reg` / `words_from` /
`fibermap` / `classify` / `measure` / `cochain` / `extension_census` by
AST extraction, and gates that on `DOUBLE-RING(8, 10, 8)` at REG and
`d = 2` it reproduces **every** committed figure: 60 charts, 138
labelled overlaps, 9 components, **0 obstructions**, `ε` = 32/28, 0
survivors, Čech 108 triples / 0 violations, split 57/115, REGA
`ε` = 40/20.  **So the same instrument produces every number below.**

**The port conventions for 3+-register events (the pin's ask), defined
and printed.**  An arbitration's registers are its proposers plus the
minted version; five instruments are run at every cell: **REG** (D64's
canonical tuple order), **REGA** (all registers sorted by name),
**ARBLOSE** (losers, winners, version), **ARBVFIRST** (version first),
**COV** (register-free surrogate — the only one also defined on
sprinklings).  *Initiator-first and winner-first coincide with REG on
this family because the schedule always makes the initiator the
sorted-first proposer; that is printed as a fact about the blueprint.*

Two routes are added and **both are validated before use** (d47a's
doctrine — a constructed true positive AND true negative): a **PARITY**
route (`g = 1` on any non-identity length-preserving transition,
including the ones D64's `cochain` drops as `other`) and a
**FREE-RELABELLING** route (arbitrary per-chart bijections — the
largest possible gauge group).

### 4.1 The wide record: A-IIIa

`CONFLICT-GRID(3, 10)` at `d = 2`: 92 charts, 27 wide, 90 overlapping
pairs, 61 triples.  **All three routes return zero obstructions at all
five conventions and both depths**, and PROBE 1 does not fire at any
wide-record cell.

**Where the non-vacuity actually lives (round-1 MAJOR 4).**  The first
version's strongest line credited the **wrong column**.  C7's `Z/2`
cochain is the **ZERO COCHAIN at all five conventions** — but for two
different reasons:

- At **REG, REGA, ARBVFIRST and COV** it is zero **on the full
  length-preserving domain**: every such transition is outright the
  identity.  There is nothing to trivialize, and the 52 Čech triples
  test `0 = 0 + 0`.  Citing the triple count as evidence of
  non-vacuity is exactly the move D64's round-1 MINOR 1 struck out.
  What **is** non-vacuous there is **PROBE 1's failure to fire**: the
  labeling could have shown a transition and did not.
- At **ARBLOSE** it is zero only because D64's `cochain` **drops the
  `other` class by construction**: its domain shrinks from 63 edges to
  22, discarding **exactly the 41 non-identity maps the old sentence
  invoked**.  The routes that actually trivialize a cochain that is
  **not** identically zero on this record are **PARITY** (63 edges, 41
  of them `g = 1`, obstruction 0) and, independently, **FREE**.

The receipt prints, per convention, C7's own cochain domain and its
non-identity count beside PARITY's.  **The A-IIIa verdict is
unaffected; the credit is corrected.**

**How many distinct readings the five conventions give (round-1
MINOR 6).**  The conventions *are* genuinely distinct labelings — the
receipt counts the `(chart, direction)` cells at which each disagrees
with REG on the ROLE label — but on the wide record REG, REGA,
ARBVFIRST and COV return the **same number in every column**.  So the
robustness sentence is that the wide record admits **two** distinct
readings, not five.

> **Conflict bought WIDTH and bought no gauge.  D64's successor
> question is answered NEGATIVELY on the first substrate that could
> have answered it positively.**

### 4.2 The pair-conflict ring, and the odd-ring reading — now DECIDED at five sizes

The *narrow* object did something no object in this campaign has done:
`RING(M = 6)` carries a **non-zero** C7 obstruction count.  The
round-1 review's own experiment costs seconds; the receipt now **runs
it instead of filing it** (round-1 MAJOR 5).  REG, `d = 2`:

| ring | pairs/round | `M/2` | parity edges | non-identity | C7 obs | PARITY obs | `R − 1` |
|---|---|---|---|---|---|---|---|
| `RING(4, 6)` | 2 | EVEN | 35 | 15 | **0** | **0** | 5 |
| `RING(6, 6)` | 3 | ODD | 30 | 11 | **5** | **5** | 5 |
| `RING(8, 6)` | 4 | EVEN | 40 | 16 | **0** | **0** | 5 |
| `RING(10, 6)` | 5 | ODD | 50 | 21 | **5** | **5** | 5 |
| `RING(12, 6)` | 6 | EVEN | 60 | 26 | **0** | **0** | 5 |
| `RING(6, 10)` | 3 | ODD | 54 | 19 | **9** | **9** | 9 |
| `RING(10, 10)` | 5 | ODD | 90 | 37 | **9** | **9** | 9 |

**The parity reading survives at five ring sizes, not three**, and
`M = 12` is the clean row that could have killed it.  **And the
magnitudes are not a ring quantity**: the count is `5` at `R = 6` and
`9` at `R = 10` **for both `M = 6` and `M = 10`** — it is `R − 1`, a
count of **rounds**, independent of the ring.  Presenting "5 (R = 6)
and 9 (R = 10)" as *the ring's* obstruction invites reading a magnitude
that is neither a ring quantity nor a cohomological one; **the only
invariant statement available is `≠ 0`.**

*(One row of the review's own table does not reproduce: it reports
`RING(4, 6)` at "edges 23, non-id 3", where this unit's instrument
measures 35 and 15.  The **obstruction count agrees (0 both ways)** and
every other row reproduces to the digit; the discrepancy is disclosed
rather than smoothed and does not touch the parity reading.)*

**And it is still NOT claimed as `H¹ ≠ 0`.**  Four things, each
measured, each cutting against the claim, and the pin requires survival
of all of them:

1. **The free-relabelling route trivializes every one of those cells**
   (0 obstructions, 0 survivors, at every cell of the entire census).
   What is obstructed is the *port* gauge group, not the existence of a
   global labelling.  (The round-1 review supplies the mechanism that
   makes this consistent with route (b): the fibre maps are *partial*,
   and with no 2-skeleton the odd cycle's composite has empty domain.)
2. **There is no Čech 2-skeleton to carry a class.**  On the rings at
   `d = 2` **every** chart triple with pairwise overlaps has an
   **empty** triple intersection — zero testable triples.  (The
   delivery crystal, by contrast, had 108 testable triples and was
   *still* a coboundary.)
3. **The group name is a convention here exactly as in D64**: D64's own
   C4b extension census, run on the ring, finds 10 subgroups of `S₄`
   consistent with every observed map, **two incomparable minimal
   ones**, and **0 of 19** τ-classified pairs uniquely τ.
4. **The controls put the ring on the wrong side of the interesting
   line.**  Genuine sprinklings carry non-zero PARITY obstructions too
   while the delivery crystal carries zero everywhere.  **Round-1
   MINOR 8: that comparison is COV-only** — a sprinkling has no `H`, so
   only the register-free COV instrument is defined on it, and the
   ring's other four conventions have no sprinkling counterpart.  The
   receipt now makes the comparison at COV and says so.

Also corrected: **"the campaign's first non-zero obstruction" is a
heading the data does not support as stated** — in the same run the
genuine sprinklings carry non-zero parity obstructions.  What is first
is the first non-zero obstruction **on a grammar record**.

**PROBE 1 fires and is acted on.**  The blind ROLE cells — all five
instruments on the **delivery-free** ring at `d = 2`, and COV on
`RING(4, 10)` — are **excluded by name** from every
convention-robustness sentence.  No outcome anywhere is read at RAW.

## 5. The mass census (A5), labelled

d42b1 prices each actor's menu at `1 + (m − 1)/4`.  Measured along the
replayed prefixes: the total menu mass sits at `M` (the actor count) at
most prefixes and rises where an unarbitrated conflict group is
visible — e.g. `RING(6, 10)`: total mass `{6: 87 prefixes, 19/3: 3,
13/2: 27}`, i.e. a **ladder excess** (mass − M, in quarters) of
`{0: 87, 4/3: 3, 2: 27}`.

**Two things are said rather than elided.**

- **The scope difference from D65 is not bridged.**  D65's `2 → 5/2`
  jump is a **two-actor, delivery-free d42a** statement about a
  36-state exhaustive family; this is transport scope, `M` actors,
  delivery sector open, measured per PREFIX along one record.  D65's
  two values are **not** reproduced here and are not claimed to be.
  The commensurable quantity — the excess above `M` in quarters,
  counting extra visible conflict groups — is what is censused, and it
  is non-zero exactly where conflicts are open.
- **The ladder does not hold, and that is d42b1's own declared leak.**
  Per-actor sums of `13/12` and `19/16` occur — off the `1 + k/4`
  ladder — which is exactly d42b1's committed **N1** exhibit ("the
  general-depth ladder is FALSE under current pricing; a dead component
  still inflates the live singleton's view-relative arb denominator").
  This unit reproduces N1 at a different scope by an independent route
  and claims nothing about the ladder.

## 6. Forcedness, instrument hygiene, scope

- **A1 forcedness at D60's C1 grade.**  Restricted-menu drive over the
  whole sweep: **0 refusals**, max menu hits per specification = **1**
  at every step of every record.  Uniqueness is structural (menu events
  are pairwise distinct and a specification is a full event tuple); the
  gated content is that the event is OFFERED.  **Full-menu replay**
  (all actors offered at every step): `RING(4,6)` 46/46 (widest menu
  126), `RING(6,6)` 69/69 (301), `GRID(3,4)` 66/66 (530),
  **`DOUBLE-GRID(3,2)` 72/72 (536)** and the headline `RING(6,10)`
  117/117 (481) all complete; the wide `GRID(3,10)` is **BUDGET-CUT at
  step 108/174** (widest menu 810) against a printed budget, and every
  step it reached was offered and unique.
- **Where the prefix bites (round-1 MINOR 1).**  The A-IIIa verdict is
  read on `GRID(3,10)` (replay budget-cut), `GRID(3,6)` and
  `GRID(4,4)` (never full-menu replayed).  The complete WIDE records
  that *are* replayed end to end are `GRID(3,4)` and
  `DOUBLE-GRID(3,2)`, and **`GRID(3,4)` is now in the A4 census**, so
  the decisive computation has a C1-complete member.  Mitigation, in
  the unit's favour: the restricted-menu drive already establishes
  admissibility of every event against the whole prefix, so the
  untested tail lacks only the "offered among all actors" property —
  which is precisely what D60's C1 grade *is*.
- **The duplicate object, said out loud (round-1 MINOR 4 / NIT 3).**
  The receipt used to claim "`g = 2` reproduces `CONFLICT-RING(4, R)`
  exactly (gated)"; **no predicate tested it and the strong form is
  false** — the event lists differ by actor naming (`G00…` vs `C0…`).
  What is now GATED is the true statement: the event-KIND sequences
  coincide and **every profile column coincides at both depths**, so
  the sweep contains one duplicate object under two names.
- **Single sources, gated.**  The transport grammar by text-slice from
  committed d42b1; d47a, d55c, d58, D60's blueprint machinery, D63's
  `double_ring`/`wide_brick` and **D64's entire cocycle instrument** by
  AST extraction, with exit-freedom of the slice and of every extracted
  body gated.  **Round-1 NIT 4, scope restated:** the scan is a
  syntactic check for `exit`/`quit`/`_exit` in CALL or bare
  NAME/ATTRIBUTE form; it decides no reachability and **cannot see an
  exit reached through `getattr` on a computed string**.
- **A hoisted SKY-B, gated against the committed one.**  The bulk
  bound-checking reads SKY-B with the height vector computed once per
  record instead of once per event; that optimisation is gated to agree
  with the committed `d47a.sky` **event for event on two whole records
  at both depths**.  Every chart the unit EXHIBITS is still read from
  the committed `sky` directly.
- **Anchors (exit 1 reserved for these).**  D63's `DR(8,10,8)` row
  exact at both depths; D60's brick event-for-event; the eleven genuine
  sprinkling configurations reproducing `[77/120, 4/5]` and
  `[17/40, 13/20]`; D64's C0b instrument validation re-run on every
  conflict record (closure of `P` **equals** the committed order
  everywhere); D64's committed C7 row.
- **Determinism gated** (D63's W6b): a ring, a grid **and the
  DOUBLE GRID** rebuilt under `PYTHONHASHSEED` 0/7/999, byte-identical
  stdout — with the scope said aloud (it does not cover the sweep's
  larger records or the A4 census).
- **Scope (pin §5).**  Grammar layer; the swept
  `(M, R, sticky, win, g)` family, now including the DOUBLE-GRID
  schedule, and no wider.  A crystal certifies MECHANISMS, never
  objects (#440).  No measure claim at transport scope (B1) and
  therefore no typicality.  Every width claim carries the record's own
  `B`, its live `Bl` and both bounds; every gauge sentence carries the
  convention table.  Transfer to the identified interactive click law
  runs through paper 29's missing map (D59) and is not claimed; the
  missing map is not touched.

## 7. The licensed claim

> **THE LICENSED CLAIM.**  Inside the swept family, at grammar layer:
> **(i)** conflict tiles — forced propose/arbitrate records run to
> crystal length with zero refusals, at an arbitration share bounded by
> `1/(k+1)`, saturated at `1/3` by the delivery-free ring, and with the
> delivery-free DOUBLE GRID's share sitting exactly at `1/(k+1)` for
> the `k = 3` of its conflict groups; **(ii)** a two-proposer conflict ring
> meets D63's F3 pattern **at `d = 2`** (inside the sprinkling
> homogeneity band **and** carrying 4-direction charts) with
> **conflict, not delivery, as its tiling engine** — while its *width*
> half is carried by its delivery wires, so a purely conflict-driven F3
> pattern is exhibited **nowhere** in this unit; **(iii)** chart width
> past the delivery ceiling of 4 at `d = 2` is **realized**, and the
> law is W4c's `|D_e(d)| ≤ Bl^d` with its depth-2 refinement
> `|D_e(2)| ≤ Σ_{y ∈ succ(e)} b(y) ≤ k·Bl ≤ k²` (exact containment
> form and its characterised exceptions in §3), **realized at 6, 7, 8
> and SATURATED at 9 = k²**, with `2k` exposed as
> the `Bl = 2` corner that the RING/GRID schedules happen to impose;
> W4b's "3+ registers" is corrected to "3+ PROPOSERS" by W4c, which is
> **proved** from the committed layer; **(iv)** the wide record's
> transition class is **trivial** at every port convention and by every
> route — with the non-vacuity carried by PROBE 1's silence at the four
> zero-cochain conventions and by the PARITY/FREE routes at ARBLOSE —
> so **no non-trivial structure group is exhibited by conflict
> either**; and **(v)** the pair-conflict rings with an **odd** number
> of pairs per round carry a non-zero port-flip obstruction count at
> five measured ring sizes, whose magnitude is `R − 1` and therefore
> **not a ring quantity**, which does **not** survive the
> free-relabelling test, has **no** testable Čech triple behind it, and
> is therefore reported and **not** claimed as `H¹ ≠ 0`.

## 8. Residues

1. **The odd-ring holonomy — now a proof problem, not a sampling
   problem.**  The parity of `M/2` is confirmed at **five** ring sizes
   (`M = 4, 6, 8, 10, 12`), with `M = 12` the row that could have
   killed it, and the obstruction count is `R − 1` at every obstructing
   cell — a count of rounds, not of the ring.  What remains open is the
   **proof** that the obstruction is exactly the parity of `M/2`, and
   the reading of what it is an obstruction *of* given that the
   free-relabelling route is clean and there is no 2-skeleton.
2. **~~Width and tiling do not compose past 4~~ — ANSWERED, by the
   round's own construction.**  `DOUBLE-GRID(3,4)` is **inside the
   `d = 3` homogeneity band while carrying `max |D| = 9`**, and the
   unit's own `k = 3` grids move into the `d = 3` band under its own
   interior control.  The anti-correlation is a **`d = 2`** property of
   this family and is restated as such.  What stays open is whether any
   schedule is in-band **at `d = 2`** while past the ceiling.
3. **The free-relabelling route never fires on real data.**  Validated
   to have a true positive on a constructed inconsistency; returns 0 at
   every census cell including the sprinklings.  Whether any grammar or
   sprinkled record can obstruct it is unmeasured, and until one does,
   its null is weak evidence.
4. **The wide record's full-menu replay is still a prefix.**
   `GRID(3,10)` cuts at 108 of 174 steps; the C1 grade for a complete
   WIDE record rests on `GRID(3,4)` and `DOUBLE-GRID(3,2)`, both of
   which are now in the decisive censuses.
5. **`ARBLOSE` is the convention that behaves differently** (41
   non-identity maps on the wide record where the other four see none),
   and it is the one whose port order is read off the conflict's own
   winner/loser asymmetry — the very asymmetry D64's residue 1 said an
   arbitration has and a delivery lacks.  That the class is trivial
   there anyway is carried by the **PARITY and FREE** routes (not by
   C7, which drops those maps), and it deserves its own sweep.
6. **Is `k·Bl` attained above `k = 3`?**  `k² = 9` is saturated at
   `k = 3`.  Whether a `k = 4` schedule can reach 16 — it needs four
   concurrent conflict axes per actor — is unbuilt.
7. **Size.**  The largest record here is 195 events against 120-point
   sprinklings; D60/D63's size residue is inherited, and the cost is
   now dominated by the base count — every arbitration mints a version,
   so the layer's own menu enumeration grows with the record.

## 9. Corrections — what round 1 refuted, verbatim

Round 1 reproduced **every published figure** of the first version of
this note and of its receipt, byte for byte apart from timings, and
confirmed the `|D| = 8` witness event by event, W4c's bound, the A4
census, the ring obstruction counts, the mass census and the anchors.
It then **broke two sentences with constructions of its own**.  Both
constructions are credited to the round, **rebuilt here with this
unit's own driver, and gated** — the DOUBLE GRID reproduces the
review's figures exactly (72 and 120 events, hits 1, no refusal, arb
share 1/4, 12 bootstrap deliveries and zero in-round, `d = 2`
homogeneity 31/60, `|D| ≥ 4` at 11/120, `ω` 0.5566, `d = 3` homogeneity
47/60 and `|D| ≥ 4` at 13/40, `max |D| = 9`, width histogram
`{0:10, 1:48, 2:5, 3:46, 4:2, 9:9}`, full-menu replay 72/72 at widest
menu 536).

**REFUTED 1 — the width law and its mechanism (BLOCKER 1).**

> ~~"`max |D| = 2k` at `d = 2` for a `k`-proposer crystal … **The
> mechanism is legible in the chart itself: each proposer contributes
> one direction per wire of its next delivery, so
> `max |D_e(2)| = 2k`.**"~~

is **false as a law**.  It is a property of the RING and GRID
*schedules*, in which every depth-1 successor of an arbitration is a
delivery (`b(y) = 2`).  Replaced by the refinement
`|D_e(2)| ≤ Σ_{y ∈ succ(e)} b(y) ≤ k·Bl ≤ k²`, gated at every event of
every record and **saturated at `k² = 9`** (§3).  **LOG #471's headline
("THE WIDTH DOOR OPENS: max |D| = 2k at d = 2 for a k-proposer
crystal") is superseded by this note; the corrected headline is: W4c's
bound is TIGHT, and the widest chart in the campaign is 9.**

**REFUTED 2 — the design finding (MAJOR 1).**

> ~~"**The delivery is not a tax on the conflict engine; it is what
> gives the crystal a second direction.**"~~  and  ~~"the schedule that
> maximises the conflict share is the one that *cannot* tile widely"~~

are **false**.  The evidence was a single schedule (`sticky = 0`), in
which each actor has exactly **one** conflict lineage, so its cycle is
a chain of diamonds; the collapse is a property of **one live conflict
per actor**, not of delivery-freedom.  The delivery-free DOUBLE GRID
gives each actor two standing conflicts, saturates the arbitration
share, has **zero in-round deliveries**, and is the **widest record in
the unit**.  Replaced by: what a second direction needs is a **second
concurrent conflict axis**, which either deliveries or crossed
conflicts supply — and a concurrent arbitration supplies a better one
(§2).

**Round-1 findings carried without refutation:** MAJOR 2 (depth labels;
residue 2 answered), MAJOR 3 (W4c's proof written in and gated against
the committed source), MAJOR 4 (the non-vacuity re-attributed from C7
to PARITY/FREE and to PROBE 1's silence), MAJOR 5 (the odd-ring
experiment run at five sizes; the count re-read as `R − 1`), MINOR 1–8
and NIT 1–4 as marked in §2–§6.  **No finding of round 1 was rejected.**
