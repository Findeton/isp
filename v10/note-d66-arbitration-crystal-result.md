# D66 — result: **A-IIIa. CONFLICT TILES, AND IT BREAKS THE DELIVERY CEILING — `max |D| = 2k` at `d = 2` for a `k`-proposer crystal, against 4 for any delivery circuit. The class is trivial again. And W4b's necessary condition was not sufficient: the mint register is a dead wire.**

**Status: GREEN-UNREVIEWED, 2026-07-26.**  No independent hostile
review has been run on this unit.  Pin
`note-d66-arbitration-crystal-pin.md` (STRICT, FROZEN AND COMMITTED
before the receipt existed).  Receipt
`v10/code/d66_arbitration_crystal_exact.py`, output
`v10/data/d66_arbitration_crystal_exact.out` — **20 PASS / 0 FAIL,
exit 0, 634.6 s wall clock** (run from the repo root).  Parents: D63
(the wide crystal; W4b; residue 1 — the arbitration route to width
past 4), D64 (TERMINAL — the delivery atlas is a coboundary, and its
residue 1: *can any substrate carry a non-coboundary class?*), D65
(the descent defect at conflict-group visibility), D60/D58/D47a/D55c
(the tiling blueprints, the atlas, the sky, the sprinkling controls),
D42b1 (the transport grammar).

---

## 1. Which outcome fired

The pin pre-registered four outcomes and let the sweep decide.

> **A-IIIa FIRED.**  Fifteen conflict configurations — 1,593 events,
> **zero refusals**, every event offered by the committed layer's own
> menu and specified by its FULL EVENT TUPLE — tile at cadence.  The
> pin's **A-I does not fire**: conflicts *can* be re-supplied every
> round.  **The width door OPENS**: `CONFLICT-GRID(3, ·)` carries
> `max |D| = 6` and `CONFLICT-GRID(4, 4)` carries `max |D| = 8` at
> `d = 2`, the first records in this campaign past the delivery
> grammar's ceiling of 4.  And **A4 decides A-IIIa**: on the wide
> record all three coboundary routes return **zero obstructions** at
> all five port conventions and both depths.

The pin's stated lean was that **tiling is the hard part**.  It was
half right, and the half it got wrong is the sharpest thing here: the
schedule that maximises the conflict share is the one that *cannot*
tile widely.

## 2. The design problem the pin named, solved and measured

Arbitrations consume their conflicts, so a conflict crystal must
re-supply a *shared base* every round.  The layer supplies half the
answer for free — `View.holdings` gives the minted version to **every
proposer**, not only the arbitrator — so a pair that arbitrates
together needs **no delivery** to conflict again.  What costs a
delivery is **rotation**: partners that were not together last round
hold different, mutually superseded versions.

**Three schedule variants were built and all three are reported.**

| variant | deliveries | arb share | `d = 2` homogeneity | `max |D|` |
|---|---|---|---|---|
| `sticky = 1` (rotate every round) | 27 | **10/39 ≈ 0.2564** | **0.6923 [in band]** | **4** |
| `sticky = 2` (rotate every 2nd) | 12 | 5/17 ≈ 0.2941 | 0.6471 [in band] | 4 |
| `sticky = 0` (never rotate) | **0** | **1/3 — SATURATED** | 0.6000 [below] | **2** |

*(all at `M = 6, R = 10`; "band" = the re-run sprinkling band
`[77/120, 4/5] = [0.6417, 0.8000]`.)*

> **THE CONFLICT BUDGET BOUND [THEOREM, verified].**  An
> arbitration's `ckey` is a set of `k` live proposal triples and a
> proposal is resolved by at most one arbitration (`View.resolved`),
> so `#proposals ≥ k · #arbs` and the arbitration share of any record
> of this layer is at most `1/(k+1)`, with `k` the smallest proposer
> count in it.  Deliveries only lower it.  **Verified with equality
> `#proposals = Σ k` on all fifteen records, and SATURATED at exactly
> `1/3` by the delivery-free ring.**

And the delivery-free ring — the maximum-conflict record — is exactly
the one whose charts **collapse to `max |D| = 2`** and which falls out
of the homogeneity band.  Its propose/propose/arbitrate cycle is a
diamond: two proposals fan out of an arbitration and fan straight back
into the next one, so the depth-2 layer is a single event.  **The
delivery is not a tax on the conflict engine; it is what gives the
crystal a second direction.**  That is the design finding, and it is
the reason the arb share peaks at 25.6% rather than 33.3% in the
records that tile.

The winner convention is irrelevant: `win = R` and `win = ALT`
reproduce `win = S` in every column of every census.

## 3. The width verdict — and the correction to W4b

**The door is open.**  `|D| ≥ 5` at `d = 2` at four of the fifteen
configurations; `max |D|` by proposer count `k`:

| record | `k` | `B` (regs) | W4b bound `B²` | live `Bl` | **W4c bound `Bl²`** | measured `max |D|` |
|---|---|---|---|---|---|---|
| any delivery circuit (D63) | — | 2 | 4 | 2 | 4 | 4 |
| `CONFLICT-RING(M, R)` | 2 | **3** | **9** | **2** | **4** | **4** |
| `CONFLICT-GRID(3, R)` | 3 | 4 | 16 | 3 | 9 | **6** |
| `CONFLICT-GRID(4, 4)` | 4 | 5 | 25 | 4 | 16 | **8** |

> **W4c — THE MINT-REGISTER REFINEMENT [THEOREM, verified].**  The
> version register an arbitration mints is a **birth wire**: `regs_of`
> places a version name in exactly one event's register set, so it has
> **no P-successor**.  Replacing `|regs(x)|` by the number of registers
> of `x` that RECUR — the live out-degree `b(x)` — in W4b's own proof
> gives `|D_e(d)| ≤ Bl^d` with `Bl = max b(x)`, and for an arbitration
> `b = #proposers = |regs| − 1`.
>
> **CONSEQUENCE.**  A **two-proposer** conflict record has `Bl = 2`
> exactly like a delivery circuit and **cannot exceed 4 at `d = 2`**,
> despite carrying 3-register events.  **D63's "width past 4 at
> `d = 2` requires a 3+-register event" is true but NOT SUFFICIENT:
> what is required is 3+ distinct PROPOSERS.**
>
> Gated, not asserted: across every record built here every version
> register occurs in exactly one event's `regs_of` (12–42 version
> registers per record, zero occurring twice), and both bounds hold
> with zero violations at both depths on all seventeen records
> (fifteen conflict records plus the two delivery controls).

**The witness, exhibited rather than counted** (pin §5's demand that a
width claim not be an instrument artefact):
`CONFLICT-GRID(4, 4)`, base event index 4 — an arbitration by `G00`
over **four distinct proposers**, 5 registers, at height 1.  Its
`SKY-B(d = 2)` chart, read from the **committed `d47a.sky`
directly**, is `|D| = 8`: directions 21, 24, 29, 31, 37, 39, 45, 47,
every one verified to be ordered after the base in the **committed**
`poset_of` order and to sit exactly two height layers above it.  Their
`P`-paths are the eight words `(p, 0)` and `(p, 1)` for `p = 0..3` —
one port per proposer, then the two wires of the delivery that
proposer's next event is.  **The mechanism is legible in the chart
itself: each proposer contributes one direction per wire of its next
delivery, so `max |D_e(2)| = 2k`.**

**What the door does NOT buy.**  Width and tiling homogeneity
*anti-correlate* in this family at `d = 2`: the in-band records are
exactly the `k = 2` rings (homogeneity 0.6522–0.7091, `|D| ≥ 4` at
0.12–0.24, `max |D| = 4`), and every `k ≥ 3` grid sits **below** the
band (0.4483–0.5287) though it carries `|D| = 6` or 8.  **No swept
configuration is both inside the homogeneity band and past the
ceiling.**  So D63's composition claim (tiling + width) is reproduced
here with **conflict as the engine** — the rings meet D63's F3 pattern
at 10 of 15 configurations, with no delivery circuit anywhere in
them — but the *extension* of that composition past `|D| = 4` is not
achieved in this family, and the trade-off is measured rather than
guessed.  The interior control (D60's C7 excision) raises homogeneity
at every controlled record and leaves `max |D|` unchanged, so the wide
charts are the circuit's and not the prefix's; the grids' interiors
stay below the band (0.5646, 0.5263), so their shortfall is **not**
an ends effect the way D63's band membership was.

`ω` is reported per D58's reading (a chart-size ratio along covers,
never a symmetric overlap): 0.75 for every rotating ring, 1.0000 for
the delivery-free ring (thin charts, as the statistic's bias
predicts), 0.44–0.51 for the grids.

## 4. The coboundary gate (A4), and the campaign's first non-zero obstruction

**The instrument is D64's, unmodified, and it is anchored.**  This
receipt re-runs D64's own `reg_tuple` / `out_reg` / `words_from` /
`fibermap` / `classify` / `measure` / `cochain` / `extension_census`
by AST extraction, and gates that on `DOUBLE-RING(8, 10, 8)` at REG
and `d = 2` it reproduces **every** committed figure: 60 charts, 138
labelled overlaps, 9 components, **0 obstructions**, `ε` = 32/28, 0
survivors, Čech 108 triples / 0 violations, split 57/115, REGA
`ε` = 40/20.  **So the same instrument produces every number below.**

**The port conventions for 3+-register events (the pin's ask),
defined and printed.**  An arbitration's registers are its proposers
plus the minted version; five instruments are run at every cell:

| instrument | port order for an arbitration |
|---|---|
| **REG** | D64's canonical: proposers sorted, then the version |
| **REGA** | every register sorted by name |
| **ARBLOSE** | losers, then winners, then the version |
| **ARBVFIRST** | the version first, then the proposers sorted |
| **COV** | register-free surrogate (covers, cover-index ports) |

*Initiator-first and winner-first coincide with REG on this family,
because the schedule always makes the initiator the sorted-first
proposer; that is printed as a fact about the blueprint rather than
hidden in a choice.*

**Two routes are added and both are validated before use** (d47a's
doctrine — a true positive AND a true negative, constructed): a
**PARITY** route (`g = 1` on any non-identity length-preserving
transition, including the ones D64's `cochain` drops as `other`, so it
is never vacuous) and a **FREE-RELABELLING** route (identify
`(chart, word)` with `(chart', m(word))` and ask whether any class
contains two distinct words of one chart — the same question for the
largest possible gauge group, arbitrary per-chart bijections).

### 4.1 The wide record: A-IIIa

`CONFLICT-GRID(3, 10)` at `d = 2`: 92 charts, 27 wide, 90 overlapping
pairs, 61 triples.

| convention | classes of the transitions | C7 obs | PARITY obs | FREE obs | Čech |
|---|---|---|---|---|---|
| REG | identity 63, length-changing 27 | 0 | 0 | 0 | 52 / 0 |
| REGA | identity 63, length-changing 27 | 0 | 0 | 0 | 52 / 0 |
| **ARBLOSE** | identity 22, **other 41**, length-changing 27 | 0 | **0** | 0 | 2 / 0 |
| ARBVFIRST | identity 63, length-changing 27 | 0 | 0 | 0 | 52 / 0 |
| COV | identity 63, length-changing 27 | 0 | 0 | 0 | 52 / 0 |

**The triviality is not vacuous.**  At four conventions every
length-preserving transition is outright the identity, with 52
testable Čech triples; at ARBLOSE **41 of the 90 pairs carry a
non-identity map and the class is a coboundary anyway**.  PROBE 1
(a blind labeling would make a flat reading an artefact) does **not**
fire at any wide-record cell.  So: **conflict bought WIDTH and bought
no gauge.  D64's successor question is answered NEGATIVELY on the
first substrate that could have answered it positively.**

### 4.2 The pair-conflict ring: the first non-zero obstruction anywhere

And then the *narrow* object did something no object in this campaign
has done.

| record, `d = 2` | REG | REGA | ARBLOSE | ARBVFIRST | COV | Čech triples | non-identity pairs |
|---|---|---|---|---|---|---|---|
| **`RING(M=6, R=6)`** | **5** | **5** | **5** | 0 *(τ route vacuous)* | **5** | **0** | 11 τ |
| **`RING(M=6, R=10)`** | **9** | **9** | **9** | 0 *(vacuous)* | **9** | **0** | 19 τ |
| `RING(M=4, R=10)` | 0 | 0 | 0 | 0 | *blind* | 16 / 0 | 25 (5 τ, 20 other) |
| `RING(M=8, R=10)` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `RING(M=6, R=10, sticky=0)` | *blind* | *blind* | *blind* | *blind* | *blind* | 0 | 0 |
| `DR(8,10,8)` (D64's) | 0 | 0 | 0 | 0 | 0 | 108 / 0 | 115 |

*(C7 obstruction counts; "blind" = a cell PROBE 1 rejects, excluded by
name.  The **PARITY** route — which never goes vacuous — returns the
SAME counts, 5 and 9, at **all five** conventions including ARBVFIRST,
and 20 and 36 at `d = 3`.  `RING(M = 4)` is the sharpest control: it
HAS non-identity transitions, 25 of 63 pairs, and is a coboundary
anyway.)*

The obstruction is real at the graph level: an explicit witness edge
is printed (`RING(6,10)` REG `d = 2`, charts 100 and 104, both
arbitrations at height 25, both of width 4, transition
`((1,0)→(0,0), (1,1)→(0,1))` = τ), and D64's route (c) confirms it by
re-running the census under the best `ε` and finding 9 surviving
non-identity transitions.

**And it is NOT claimed as `H¹ ≠ 0`.**  Four things, each measured,
each cutting against the claim, and the pin requires survival of all
of them:

1. **The free-relabelling route trivializes every one of those
   cells** (0 obstructions, 0 survivors, at every cell of the entire
   census).  What is obstructed is the *port* gauge group, not the
   existence of a global labelling.
2. **There is no Čech 2-skeleton to carry a class.**  On the rings at
   `d = 2` **every** chart triple with pairwise overlaps has an
   **empty** triple intersection — zero testable triples — so the
   cocycle condition is vacuous and "the class" lives in the cycle
   space of a graph, not in `H¹` of a covering with 2-cells.  (The
   delivery crystal, by contrast, had 108 testable triples and was
   *still* a coboundary.)
3. **The group name is a convention here exactly as in D64**: D64's
   own C4b extension census, run on the ring, finds 10 subgroups of
   `S₄` consistent with every observed map, **two incomparable minimal
   ones**, and **0 of 19** τ-classified pairs uniquely τ.
4. **The controls put the ring on the wrong side of the interesting
   line.**  Genuine sprinklings carry non-zero PARITY obstructions too
   (M21 10 and 2; M31 19 and 34) while the delivery crystal carries
   zero everywhere.  On this statistic the conflict ring sits *with
   the sprinklings*, which is as much a finding about the statistic's
   discriminating power as about the ring.

**The pattern, printed as an observation and not as a claim** (and
the receipt computes its lists from the census rather than typing
them): the rotating `M = 6` rings — **three** pairs per round, an ODD
cycle in the nerve — obstruct at both `R = 6` and `R = 10` and under
both winner conventions; the rotating `M = 4` and `M = 8` rings (two
and four pairs, EVEN cycles) are clean, `M = 4` *despite* carrying 25
non-identity transitions; and the delivery-free ring is clean and
blind.  A **Z/2 holonomy around an odd conflict
ring** is the natural reading, and **three sizes do not establish
it** — it is residue 1 below, not a result.

**PROBE 1 fires and is acted on.**  Seven ROLE cells are blind — all
five instruments on the **delivery-free** ring at `d = 2`, and COV on
`RING(4, 10)` at both depths — so those flat readings are artefacts of
the labeling and are **excluded by name** from every
convention-robustness sentence above (both cells read 0 obstructions
either way).  No outcome anywhere is read at RAW (PROBE 2's censuses are
printed per substrate).

## 5. The mass census (A5), labelled

d42b1 prices each actor's menu at `1 + (m − 1)/4`.  Measured along the
replayed prefixes: the total menu mass sits at `M` (the actor count)
at most prefixes and rises where an unarbitrated conflict group is
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
  counting extra visible conflict groups — is what is censused, and
  it is non-zero exactly where conflicts are open.
- **The ladder does not hold, and that is d42b1's own declared
  leak.**  Per-actor sums of `13/12` and `19/16` occur — off the
  `1 + k/4` ladder — which is exactly d42b1's committed **N1** exhibit
  ("the general-depth ladder is FALSE under current pricing; a dead
  component still inflates the live singleton's view-relative arb
  denominator").  This unit reproduces N1 at a different scope by an
  independent route and claims nothing about the ladder.

## 6. Forcedness, instrument hygiene, scope

- **A1 forcedness at D60's C1 grade.**  Restricted-menu drive: 1,593
  events, **0 refusals**, max menu hits per specification = **1** over
  every step of every record.  Uniqueness is structural (menu events
  are pairwise distinct and a specification is a full event tuple, so
  the winner choice `W` and the `ckey` are part of it); the gated
  content is that the event is OFFERED.  **Full-menu replay** (all
  actors offered at every step): `RING(4,6)` 46/46 (widest menu 126),
  `RING(6,6)` 69/69 (301), `GRID(3,4)` 66/66 (530) and **the headline
  `RING(6,10)` 117/117 (481 candidates, 124 s)** all complete; the
  wide `GRID(3,10)` is **BUDGET-CUT at step 108/174** (widest menu
  810) against a printed 120 s budget, and every step it reached was
  offered and unique.
- **Single sources, gated.**  The transport grammar by text-slice from
  committed d42b1; d47a, d55c, d58, D60's blueprint machinery, D63's
  `double_ring`/`wide_brick` and **D64's entire cocycle instrument**
  by AST extraction, with exit-freedom of the slice and of every
  extracted body gated (syntactic scan for `exit`/`quit`/`_exit`;
  scope stated).
- **Anchors (exit 1 reserved for these five).**  D63's `DR(8,10,8)`
  row exact at both depths; D60's brick event-for-event; the eleven
  genuine sprinkling configurations reproducing `[77/120, 4/5]` and
  `[17/40, 13/20]`; D64's C0b instrument validation re-run on every
  conflict record (closure of `P` **equals** the committed order
  everywhere); D64's committed C7 row.
- **Determinism gated** (D63's W6b): a ring and a grid rebuilt under
  `PYTHONHASHSEED` 0/7/999, byte-identical stdout — with the scope
  said aloud (it does not cover the sweep's larger records or the A4
  census).
- **Scope (pin §5).**  Grammar layer; the swept
  `(M, R, sticky, win, g)` family and no wider.  A crystal certifies
  MECHANISMS, never objects (#440).  No measure claim at transport
  scope (B1) and therefore no typicality.  Every width claim carries
  the record's own `B`, its live `Bl` and W4b's bound; every gauge
  sentence carries the convention table.  Transfer to the identified
  interactive click law runs through paper 29's missing map (D59) and
  is not claimed; the missing map is not touched.

## 7. The licensed claim

> **THE LICENSED CLAIM.**  Inside the swept family, at grammar layer:
> **(i)** conflict tiles — forced propose/arbitrate records run to
> crystal length with zero refusals, at an arbitration share bounded
> by `1/(k+1)` and saturating it when no rotation is required;
> **(ii)** a two-proposer conflict ring meets D63's F3 pattern at
> `d = 2` (inside the sprinkling homogeneity band **and** carrying
> 4-direction charts) with **conflict, not delivery, as its engine**;
> **(iii)** chart width past the delivery ceiling of 4 at `d = 2` is
> **realized**, at `max |D| = 2k` for a `k`-proposer crystal (6 at
> `k = 3`, 8 at `k = 4`), and W4b's "3+ registers" is corrected to
> "3+ PROPOSERS" by W4c, because the minted version register is a dead
> wire; **(iv)** the wide record's transition class is **trivial** at
> every port convention and by every route, so **no non-trivial
> structure group is exhibited by conflict either**; and **(v)** the
> pair-conflict ring at `M = 6` carries the campaign's **first
> non-zero port-flip obstruction count**, which does **not** survive
> the free-relabelling test, has **no** testable Čech triple behind
> it, and is therefore reported and **not** claimed as `H¹ ≠ 0`.

## 8. Residues

1. **The odd-ring holonomy.**  `M = 6` obstructs at 5 (R = 6) and 9
   (R = 10) at four conventions and at all five under the parity
   route; `M = 4` and `M = 8` do not.  Whether the obstruction is
   exactly the parity of `M/2` — a Z/2 holonomy around the ring — is
   the sharp open question, and it needs `M = 10, 12, 14` and a
   proof, not three sizes.  If it *is* the ring parity, then the
   obstruction is a topological fact about the schedule and not about
   arbitration, which would close the question the other way.
2. **Width and tiling do not compose past 4.**  Every `k ≥ 3` grid is
   below the homogeneity band at `d = 2` and stays below under the
   interior excision — unlike D63's ends effect.  Whether a schedule
   exists with `k ≥ 3` arbitrations at in-band homogeneity (aligning
   the group's proposals to one height layer is the obvious lever; an
   idle-padded variant was tried and cost more than it bought) is
   open.
3. **The free-relabelling route never fires on real data.**  It is
   validated to have a true positive on a constructed inconsistency,
   and returns 0 at all 114 census cells including the sprinklings.
   Whether any grammar or sprinkled record can obstruct it is
   unmeasured, and until one does, its null is weak evidence.
4. **The wide record's full-menu replay is a prefix.**  108 of 174
   steps at a printed budget; the C1 grade for a complete WIDE record
   rests on `GRID(3, 4)` (66 events) instead.
5. **`ARBLOSE` is the convention that behaves differently** (41
   non-identity maps on the wide record where the other four see
   none), and it is the one whose port order is read off the
   conflict's own winner/loser asymmetry — the very asymmetry D64's
   residue 1 said an arbitration has and a delivery lacks.  That the
   class is a coboundary there anyway is the strongest single line in
   §4.1, and it deserves its own sweep.
6. **Size.**  174 events against 120-point sprinklings; D60/D63's size
   residue is inherited, and the cost is now dominated by the base
   count — every arbitration mints a version, so the layer's own menu
   enumeration grows with the record.
