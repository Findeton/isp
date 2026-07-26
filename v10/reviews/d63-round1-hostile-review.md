# D63 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D63 "the wide crystal" — `note-d63-wide-crystal-pin.md`
(STRICT, committed before the receipt), `note-d63-wide-crystal-result.md`
(GREEN-UNREVIEWED), `code/d63_wide_crystal_exact.py` +
`data/d63_wide_crystal_exact.out` (11 PASS / 0 FAIL, exit 0), LOG #458.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to
the unit, recompute-never-trust. Every number below was produced by code
I wrote for this review (`indep.py` / `run1.py` / `run2.py` / `run3.py`,
scratch under `/private/tmp/claude-501/.../scratchpad/d63rev/`): my own
`regs_of`, my own transitive closure of the immediate-predecessor
relation, my own longest-chain heights, my own SKY-B, covers,
homogeneity, `|D| >= 4` and omega, my own sprinkling generator and
Minkowski order, and my own menu driver. The only object I share with
the unit is the layer under test (`d42b1`'s `candidates_for` /
`admissible`). Calibration: `reviews/batch-round1-d50-to-d60.md` (its
D60/D58 findings) and `reviews/d61-round1-hostile-review.md`.

**VERDICT: REVISE. 0 BLOCKER / 4 MAJOR / 8 MINOR / 4 NIT.**

**The arithmetic and the theorem both survive, completely.** I rebuilt
all 38 configurations from the note's blueprint description with my own
driver and measured them with my own instrument: **every figure in every
table of the note and the receipt reproduces exactly** — the `C = 0`
anchor at `10/13, 125/192, 0, 3`; the band `[77/120, 4/5]` and the
`|D| >= 4` band `[17/40, 13/20]`; the winner `DR(8,10,8)` at
`47/59, 1/3, max 4, omega 0.7299` and `0.7740 / 0.6723` at `d = 3`; the
interior `0.8808 / 0.3907`; the in-band 21 / wide 26 / BOTH 14 counts and
the 9-DR/5-WB split; the two `d = 3` both-bands entries. **W4b is a
correct theorem and I could not break it.** I checked every step against
`event_poset`'s committed source, verified independently that my closure
of `P` equals the layer's order on all 38 records, that
`#P-successors(x) <= |regs(x)|` at every event of every record, and that
`|D_e(d)| <= B^d` holds **event by event, at d = 1, 2, 3 and 4, with zero
violations**, `B = 2` measured on every record. The forcedness claim
survives two further full-menu replays the receipt never ran.

**The four MAJORs are all about what the unit says, not what it
computed.** Three headline sentences are true only at `d = 2` and false
or unsupported as written; the two "findings in their own right" of §2
are refuted by the receipt's own rows; the F3 criterion is far more
boundary-dependent than the one record reported; and the unit's own
output silently contradicts a committed clause of its parent.

---

## MAJOR 1 — the novelty comparison is depth-conditional, and at `d = 3` the *unmodified D60 brick* already satisfies the F3 pattern with zero couriers

**Where.** Note §1 witness box ("`|D| >= 4` at 1/3 of its events **(the
brick's is 0 at every parameter)**"); note §3's licensed-claim box, which
carries **no depth label at all** ("a delivery circuit can tile at
sprinkling-band homogeneity while carrying 4-direction charts at a third
of its events"); receipt's licensed-claim gate ("…which the brick never
did at any parameter"); LOG #458.

**Defect.** Those clauses are `d = 2` statements presented without the
label, in a unit whose parent was convicted in the batch round for
exactly this (D60 MINOR 4, "the depths disagree"). At `d = 3` the
`C = 0` WIDE-BRICK — which is D60's `brick(8,14)` event for event, no
couriers, no coupling — sits **inside** the `d = 3` homogeneity band and
carries `|D| >= 4` at **0.5846** with `max |D| = 4`. That is the F3
pattern ("in the band AND carries `|D| >= 4` charts") satisfied by the
object the unit says never did it. The receipt *prints* this row (W2,
"C=0 anchor d=3: homog 0.7385 [IN BAND] |D|>=4 0.5846") and then the
same run's gate label says the brick "never did [it] at any parameter".
The note omits the row entirely.

**Recomputation (mine).** The F3 predicate evaluated at `d = 3` over the
whole sweep, my own instrument, `d = 3` bands `[41/60, 49/60]` and the
`h4 > 0` clause:

```
  F3 pattern at d = 3 holds at 11 of the 38 configurations, and FOUR of
  them have ZERO coupling:
    WB(8,14,C=0)  homog 0.7385 [in band]  |D|>=4 0.5846   <- D60's brick
    WB(10,14,C=0) homog 0.7160 [in band]  |D|>=4 0.5556
    DR(6,14,cpl=0) homog 0.7526 [in band] |D|>=4 0.0103
    DR(4,14,cpl=0) homog 0.7692 [in band] |D|>=4 0.0154
  and the brick's d = 3 max |D| is 4 — the number the unit reports as
  its own new ceiling at d = 2.
```

The finding itself is real and is a `d = 2` finding; the pin asks a
`d = 2` question and the sweep answers it. What must change is the
prose: every occurrence of "the brick's is 0 at every parameter",
"which the brick never did", "max |D| = 3 was the 1+1 brick's cone" and
the §3 licensed-claim box must carry `d = 2`, and the note must report
that at `d = 3` uncoupled configurations — D60's own brick among them —
already meet the pattern. Otherwise the unit's stated novelty is an
artefact of the depth it chose to headline.

---

## MAJOR 2 — §2's two "findings in their own right" state mechanisms that the receipt's own rows refute

**Where.** Note §2, numbered findings 1 and 2, and note §1 ("the coupled-
ring route buys width while homogeneity *rises*, **provided the coupling
is complete**").

**Defect (a) — "a complete coupling restores it and buys the
direction".** Under the receipt's *own* definition of completeness
(`chords()` docstring: "At `C = M` every ring actor is a chord endpoint
exactly twice, at `C = M/2` exactly once; below that the coupling is
PARTIAL"), the complete WIDE-BRICK settings are the **worst** points in
their families, not the recovery:

```
  M = 6:  C = 2 (PARTIAL)  homog 0.8182   ->  C = 3 (COMPLETE) homog 0.5258
                                              — below C = 0's 0.7027 and
                                                below the band floor
  M = 8:  C = 3 (PARTIAL)  homog 0.8658   ->  C = 4 (COMPLETE) homog 0.7062
  M = 10: the complete setting is C = 5 and was NEVER SWEPT (C = 0..3)
```

So "only recovers from 2 upward" and "a complete coupling restores it"
are false in the wide-brick family; the sweep's own best wide-brick
points are *partial* couplings, and the one family where the maximum
sits at full coupling is the double ring. The claim is family-specific
and is stated as general.

**Defect (b) — "the width column jumps from 0 to positive exactly when
the second direction becomes available at every wire — `C = 2` on an
8-ring, `cpl = 2` on a coupled pair".** At those two jump points the
second direction is available at a *minority* of wires, and the wide
charts sit at exactly that minority:

```
  WB(8,14,C=2): chords [(0,4),(1,5)] — 4 of 8 ring actors are endpoints.
      12 wide events, carried by exactly R0, R1, R4, R5.
  DR(8,10,cpl=2): positions 0,1 coupled — 4 of 16 ring actors.
      8 wide events of 117, carried by exactly A0,A1,B0,B1
      (senders/receivers A0->A1, A1->A0, B0->B1, B1->B0 and no others).
  DR(8,10,cpl=8): 16 of 16 ring actors carry a wide chart — this is the
      only setting where "every wire" is true, and it is not the jump.
```

The true statement — width appears exactly at the wires that have a
second direction, and nowhere else — is sharper and is what the data
show. "At every wire" is refuted at both quoted jump points.

**Defect (c) — internal contradiction.** §2 finding 1 offers the height-
regularity mechanism as an explanation; §8 residue 3 says "The `cpl = 1`
dip is **unexplained** beyond 'partial coupling breaks height
regularity'; a height-layer census would decide it". The same note both
asserts and disclaims the mechanism. The census is one loop away and was
not run.

---

## MAJOR 3 — "inside the band" is an ENDS property for most of the F3 set, and the unit measures it on one record

**Where.** Note §5 and the receipt's W5 (interior control on 5 records);
note §1's headline ("14 sit INSIDE the recomputed sprinkling homogeneity
band"); note §3's licensed claim ("tile at sprinkling-band
homogeneity").

**Defect.** Band membership is the F3 criterion, and under D60's own C7
excision (bottom two, top three height layers — the receipt's
`interior_of` is exactly D60's) most of the F3 set leaves the band. The
note reports this for the winner alone and calls it "in part a property
of the record's ENDS"; the honest quantity is much larger, and the
receipt never computes it because W5 runs on 5 of 38 records.

**Recomputation (mine) — the interior control on EVERY F3 member:**

```
  DR(8,10,8) 0.7966 -> 0.8808 ABOVE      DR(6,14,5) 0.7844 -> 0.8523 ABOVE
  DR(8,10,6) 0.7261 -> 0.8148 ABOVE      DR(6,14,4) 0.7647 -> 0.8394 ABOVE
  DR(8,10,7) 0.7485 -> 0.8322 ABOVE      DR(4,14,3) 0.7383 -> 0.8105 ABOVE
  DR(8,10,5) 0.6735 -> 0.7480 in         DR(6,14,3) 0.6763 -> 0.7360 in
  DR(4,14,2) 0.7204 -> 0.8072 ABOVE      WB(10,14,3) 0.7758 -> 0.8389 ABOVE
  WB(8,14,4) 0.7062 -> 0.7576 in         WB(8,14,2) 0.7355 -> 0.8165 ABOVE
  WB(10,14,2) 0.6788 -> 0.7339 in        WB(8,14,2,cad2) 0.7849 -> 0.8780 ABOVE

  F3 members whose INTERIOR leaves the band through the top: 10 of 14.
  (The |D| >= 4 fraction rises at all 14 — the width half of W5 is
   confirmed and is the durable part.)
```

The mechanism-level reading is D60's — homogeneity tends to 1, i.e.
*above* the band — so "the mechanism composes tiling at sprinkling-band
homogeneity" is, for 10 of the 14 witnesses, a statement about finite
records with ends and not about the mechanism. The width claim is
untouched by this; the band claim must be restated with the 10-of-14
number, and W5 should run on the F3 set rather than on five hand-named
records.

---

## MAJOR 4 — the unit's own re-run contradicts a committed clause of D60's C5, and says nothing

**Where.** Receipt W2 output line for the anchor at `d = 3` ("|D|>=4
0.5846 **[below the sprinkling |D|>=4 band]**") against the committed
`d60_crystal_exact.out` C5 gate label: "at d = 3 the brick DOES reach
|D| >= 4 (38/65), **inside the d = 3 sprinkling band**".

**Defect.** `38/65 = 0.5846`; D60's own printed `d = 3` sprinkling
`|D| >= 4` band is `[3/5, 91/120] = [0.6000, 0.7583]`. The brick is
**below** it, not inside it. D60's C5 clause is false, in a unit that has
already been through a round-1 repair, and D63 — which re-runs the same
comparator with the same instrument and prints the correct verdict — does
not flag the discrepancy anywhere in the receipt, the note or LOG #458.
The batch round's discipline is that a corrected parent number is
forward-corrected where it is quoted; this is a parent number corrected
in silence.

**Recomputation (mine).** My own instrument, my own generators:
`d = 3` sprinkling `|D| >= 4` band `[3/5, 91/120]`; brick `d = 3`
`|D| >= 4 = 38/65 = 0.5846` (below), homogeneity `48/65 = 0.7385`
(inside `[41/60, 49/60]`). D60's C5 predicate is unaffected (it gates
`d = 2` quantities); the damage is the label, which is exactly the class
the batch round told this corpus to forward-correct.

---

## MINOR 1 — pin W2's "at d = 2 AND d = 3, per record" is delivered for 4 of 38 records

Pin W2: "the atlas census per record: homogeneity, mean omega, `|D| >= 4`
fraction, `max |D|` — at d = 2 AND d = 3". Every frontier table in the
receipt and in note §2/§5 is `d = 2` only; `d = 3` appears for four named
records. The depths disagree materially across the sweep, so this is not
a formality: my full `d = 3` census shows band membership flipping in
both directions and `max |D|` exceeding 4 at **18 of the 38**
configurations — **5** at fourteen of them (WB(8,14,C=2/3/4),
WB(8,14,2,cad2), DR(8,10,cpl=0/3/4/5/6/7), DR(6,14,cpl=0/3/4/5)) and
**6** at four (WB(10,14,C=2/3), DR(8,10,2), DR(6,14,2)). None of that is
in the unit.

## MINOR 2 — "its `max |D|` does not move at all — W4b says why" is wrong

Receipt W2 gate label. W4b's bound at `d = 3` is `B^3 = 8`, so it says
nothing about a `max |D|` that stays at 4 — and six of the unit's own
records **do** move, to 5 and 6, at `d = 3` (list in MINOR 1). W4b
explains the `d = 2` ceiling and only that.

## MINOR 3 — "width past 4 is BOUGHT with arbitration" is a necessity claim sold as a route

Note §4 box and LOG #458. What W4b licenses is: `max |D| >= 5` at
`d = 2` **requires** an event with `>= 3` registers, hence (given
`regs_of`) an arbitration over `>= 2` distinct proposers. That such a
record exists at all — let alone "at tiling cadence" — is not shown; the
receipt exhibits one admissible 3-register *event*, not a record with a
5-direction chart. §8 residue 1 states this correctly; the §4 box and the
LOG do not, and "is bought with" reads as a construction. My own hunt
(220 randomized 4-actor histories to 11 events, biased toward
multi-proposer arbitrations, `B` reaching 5) found **max |D_e(2)| = 2 and
no `|D| >= 5` witness** — inconclusive, but nothing supports the stronger
reading.

## MINOR 4 — W1/W1b gate less than their labels claim

A delivery specification is the full tuple `('d', s, r, v)` and
`candidates_for` returns pairwise-distinct events (I checked: no
duplicate events in the menus), so "matched by EXACTLY ONE candidate"
**cannot exceed 1** — the quantity actually gated is *admissibility of
the specified event against the offered menu*, not the absence of
tie-breaking. The same holds for W1b, whose `n_hit` is `0` or `1` by
construction. Note §6 explains precisely this ("a delivery is specified
by its full tuple, so a matching menu entry is unique whenever it
exists") — which is to the unit's credit — but the gate labels
("nothing anywhere in the frontier was tie-broken", "the pre-registered
hard part did not bite") sell a discovered property. House style (D58 A3)
is to label a gate for what it measures.

## MINOR 5 — determinism is asserted in the note and gated nowhere

Note §6: "the run is deterministic across `PYTHONHASHSEED`". No gate in
the receipt tests it (D50 MINOR-4 class; `regs_of` for `'r'` events does
read `next(iter(frozenset))`, so the claim is not idle). I verified it
externally: `PYTHONHASHSEED=999` reproduces the committed `.out`
identically apart from the three timing figures.

## MINOR 6 — "B = 2 throughout" is in the W4b label and in no predicate

`wall_ok` compares `pr[d]['max']` against each record's **own** `Bmax`,
so the gate would pass unchanged if some record carried a 3-register
event (the bound would simply become 9). The claim that these are
`B = 2` circuits — which is what makes "the ceiling is 4" follow — is
asserted only. It is true: I measured `max |regs_of(e)| = 2` on all 38
records (species `{p, r, d}`; the single mint arbitration has one
proposer, hence 2 registers). One line would gate it.

## MINOR 7 — the F2 branch does not print the pre-registered F2

`VERDICT = 'F3' if BOTH else ('F2' if WIDE else 'F1')`, and the F2 branch
prints "width is reached only **below** the band at every swept
configuration". But `WIDE and not BOTH` also covers the case where every
wide configuration sits **above** the band — in which case the printed
sentence would be false while the gate passed. Counterfactual only (F3
fired), but W4's label advertises "the predicate is the pre-registered
disjunction itself", and for F2 it is not.

## MINOR 8 — the cadence probe is counted as a separate configuration

"38 swept configurations" and "5 wide bricks" in the F3 set both count
`WB(8,14,C=2)` twice, at cadence 1 and cadence 2. The F3 set therefore
contains **4 distinct `(M, R, C)` wide-brick settings** plus one cadence
variant of one of them. Cheap to say.

## NIT 1 — the anchor's atlas-agreement check omits `h4`

W0 compares `h2`, `om` and `max` between `profile` and D58's `atlas`, and
not `h4` — the column this whole unit is about (it is 0 at the anchor, so
nothing turns on it).

## NIT 2 — the exit-freedom gate is narrower than its label

`_no_exit` matches `ast.Call` with `func.attr == 'exit'`, so a bare
`exit()`/`quit()` (an `ast.Name` call) or `os._exit` would survive; the
slice check is the textual `'sys.exit' not in _slice`. Both are clean
here, and `_ext` keeps only defs/classes so module-level statements
cannot run in any case — but the gate is weaker than "no `sys.exit`
survives".

## NIT 3 — the anti-vacuity scan is the weak form

W6 flags only `isinstance(c.args[1], ast.Constant)`; d47a's SG8 also
requires each predicate to reference a run-bound name. The scope caveat
(#403 MA-2) is carried, so this is a note, not a defect.

## NIT 4 — width does not "follow that shape"

Note §2 finding 1: "Width, homogeneity and overlap all follow that
shape". Width is `0` at `C = 0` and `0` at `C = 1`; it cannot dip. Only
homogeneity and omega dip.

---

## Checked and CLEAN (D63)

Everything below is my own recomputation unless stated.

**A. Receipt rerun.** `11 PASS / 0 FAIL`, exit 0, 335 s. Output identical
to the committed `.out` apart from the three timing figures. Identical
again under `PYTHONHASHSEED=999`.

**B. The instrument, rebuilt from the committed definitions.** My own
`regs_of` agrees with `d42b1`'s on every event of every record; my own
DFS transitive closure of the immediate-predecessor-on-a-register
relation **equals** `event_poset` exactly on all 38 records (brick:
1,830 ordered pairs); my heights are a strict grading
(`C[i][j] => h[i] < h[j]`) everywhere.

**C. The anchor.** My own build of `brick(8,14)` from the blueprint: 65
events, no refusal, every specification matching exactly one candidate;
`d = 2` homogeneity `10/13`, omega `125/192`, `|D| >= 4 = 0`,
`max |D| = 3`. Exactly the committed row.

**D. The comparators, my own generator and my own Minkowski order.**
All eleven configurations reproduce to the last Fraction, and the bands
come out `[77/120, 4/5]` and `[17/40, 13/20]` at `d = 2`,
`[41/60, 49/60]` and `[3/5, 91/120]` at `d = 3`. I also tested the one
comparator drawn from `d47a`'s *unrepaired* low-bit generator (the band
**floor**, `77/120`): it is **not** degenerate — 119 distinct points of
120, 53/52 distinct spatial values per axis, 95 distinct times — so the
D58 BLOCKER-1 pathology does not reach into this unit's band.

**E. The winner, rebuilt independently.** `DR(8,10,cpl=8)`: 177 events
over 16 actors, no refusal, every specification matching exactly one
candidate. `d = 2`: `47/59 = 0.7966` (in band), `|D| >= 4 = 1/3`,
`max 4`, mean 2.31, omega `0.7299`. `d = 3`: `137/177 = 0.7740` (in the
`d = 3` band) and `119/177 = 0.6723` (inside the `d = 3` `|D| >= 4`
band). Interior: 151 of 177 events, `0.8808 / 0.3907`. Every figure in
the note's §1 box, §2 tables and §5 table reproduces exactly.

**F. The whole frontier.** All 38 configurations rebuilt and remeasured:
**every one of the 38 rows matches the receipt**, including the `cpl = 1`
dip points (0.6022 / 0.3645 / 0.4054 / 0.5570 / 0.6491 / 0.5138), the
cadence probe (0.7849 / 0.0538 / 4) and the rounds sweep
(0.8315 / 0.8760 / 0.9112 / 0.9309 with `|D| >= 4` 0.3708 / 0.4050 /
0.4320 / 0.4470). My independent counts: **in band 21, wide 26, BOTH 14
(9 DR + 5 WB), winner `('DR', 8, 10, 8, 1)` under the receipt's stated
rule, saturating 26, reaching the sprinkling `|D| >= 4` band at `d = 2`
exactly 2, inside both `d = 3` bands exactly 2** — every published count
confirmed. Events built 4,604; largest record 217; no refusals anywhere.

**G. W4b, attacked at every joint and standing.**
* The order *is* the transitive closure of `P` (verified, B above).
* Each `P`-step raises height by at least 1 — automatic for
  longest-chain heights on a transitively closed order, and verified.
* "At most one `P`-successor per register": `event_poset` sets
  `last[r] = j` for **every** `r in regs_of(j)` after computing `pred[j]`,
  so once an event consumes a register it becomes that wire's `last`;
  two later events cannot both have `x` as immediate predecessor on the
  same register. Verified numerically:
  `#P-successors(x) <= |regs_of(x)|` at every event of every record.
* An event whose registers are all fresh (`last[r]` empty) simply gets
  `pred = {}` and height 0 — it weakens nothing in the bound.
* SKY-B is `{f : C[e][f] and h[f] - h[e] == d}` — strictly the future,
  reachability included, no `CYCLIC_CAP` involved (the cap lives only in
  `circular_ones`, which this unit never calls). So `D_e(d) = R_e(d)` for
  `d >= 1` as the proof requires, and `R_e(0) = {e}` because heights
  strictly increase.
* The induction is sound (`|R_y(k')| <= B^{k'} <= B^{k-1}` needs only
  `B >= 1`), and the union identity is an equality in both directions.
* **Verified event by event, not just at the max**, at `d = 1, 2, 3, 4`
  across all 38 records: **0 violations**.
* `regs_of` audited for every species: `p`/`n` 1, `d` 2, `m` 2,
  `r` = #proposers + 1. The `'r'` species is the only one that can exceed
  2, and only with `>= 2` distinct proposers — the note's claim is right.
  Mint events in these records are `('p', ...)` + a one-proposer `('r',
  ...)`, both `<= 2` registers, so `B = 2` genuinely holds for the whole
  record and not merely for its deliveries.
* The 3-register exhibit is sound and I checked more than the receipt
  did: the prefix `[('p','A',V0,0), ('p','C',V0,1)]` is itself a legal
  history (both events admissible in sequence and present in the layer's
  own menus), and the two-proposer arbitration is in
  `candidates_for(prefix)` with `q = 1/8` and 3 registers.

**H. Forcedness, tested beyond the receipt.** Every one of the 38 records
was built with *minimum* as well as maximum menu hits equal to 1 (no step
had zero or two matches). I then ran two **additional** full-menu replays
the receipt never ran — `DR(4,14,4)` (121 events, 8 actors, widest menu
136) and `DR(6,14,6)` (181 events, 12 actors, widest menu 300) — with all
actors offered at every step: both `OK`, hits 1 at every step. The
receipt's three replays therefore under-report a property that holds more
widely.

**I. The interior excision is D60's.** `interior_of` reproduces C7's
`lo + 2 <= h[e] <= hi - 3` exactly, and the five published FULL ->
INTERIOR rows reproduce to four decimals. The width half of the control
is confirmed on the whole F3 set, not just the five (MAJOR 3).

**J. The band is computed in-process from the re-run comparators.**
`BAND`/`W4B`/`MXB`/`OMB` are all derived from `SPR`, which is D58's
`atlas` called on freshly generated sprinklings inside this run; no
threshold anywhere in the receipt is a typed constant. The batch round's
D60 MINOR 1 is fully discharged.

**K. Statistic identity.** D60's `profile` with the population set to
everything is D58's `atlas` on `h2`/`h4`/`max`/`om` (I re-derived both
and they agree), so the `|D| >= 4` column compared against the
sprinklings is the same statistic on the same population with the same
depth semantics.

**L. Instrument hygiene.** The `d42b1` text slice cuts at the receipt's
own banner and contains no `sys.exit`; `_ext` keeps only defs/classes and
named constants, so no imported module-level gate or print can fire; the
extracted-body counts printed in W0a match the files. The declared
exit-protocol deviation is exactly what the code does (`anchor=True` on
W0a, W0 and W3 only; `sys.exit(1 if ANCHOR_FAIL else 0)`), and it is
printed on the exit line. No silent caps: the SKY-B depths, cadence,
chord rule, coupling rule, replay budget (300 s, never hit — worst replay
84.9 s) and every swept range are printed, and no sweep was truncated.

**M. Scope.** Pin §5 and note §7 carry all four required clauses —
grammar layer, no measure (B1), no typicality, no physical-object claim
(#440) — plus the D59 transfer caveat and D58 MAJOR-2's omega reading.
The universal statement (W4b) is the only one that exceeds the swept
family and it is a theorem whose hypothesis is stated in §4 and again in
§7. LOG #458 states the hypothesis too ("Deliveries carry `B = 2`").
Subject to MAJOR 1's missing depth labels, no claim exceeds the sweep.

**N. Provenance.** Pin (98 lines, `STRICT`) is committed before the
result note and the receipt, and the pin's F1/F2/F3 disjunction is the
frontier gate's actual predicate. The pre-registered lean is reported as
having *partly* failed (the cost was smaller than leaned) rather than
quietly dropped, and the three limits in §3 are all reported against the
unit's interest.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-26)

All four MAJORs and every MINOR/NIT verified against the receipt's own
printed rows before repair (the reviewer's numbers reproduced; MAJOR
1/2's refuting rows are the receipt's own tables).  Repairs applied,
receipt rerun green — **12 PASS / 0 FAIL** (one new gate):

1. **MAJOR 1:** every novelty sentence now carries **d = 2** (note §1
   headline/witness box, §3 licensed-claim box, W4/licensed-claim gate
   labels, the verdict block), and the d = 3 F3-pattern census is
   PRINTED AND GATED (W2: 11 configurations meet the pattern at d = 3,
   4 with zero coupling, D60's brick among them; at d = 2, zero).
2. **MAJOR 2:** §2's findings rewritten — the recovery is
   family-specific (double rings peak at full coupling, wide bricks at
   partial; the complete wide-brick settings are their families' worst
   points); "every wire" replaced by the per-wire statement (width at
   exactly the coupled wires); and the **height-layer census the
   review called one-loop-away is now IN the receipt**: (8,10) cpl=0
   27 layers, cpl=1 36 ragged layers, cpl=8 37 layers with a
   constant-8 tail — partial coupling desynchronises the height
   structure, full coupling restores layer regularity.  §8 residue 3
   updated from "unexplained" to "measured; the proof is the residue".
3. **MAJOR 3:** W5 now runs on **every F3 member** (14/14): width
   rises under excision at all 14 (the durable half); **10 of 14
   interiors leave the band through the top** — gated, in the note's
   §3 limits and §5, and the licensed claim restated ("the width
   mechanism does not destroy the tiling mechanism; band membership
   is a finite-record ends statement").
4. **MAJOR 4:** D60's C5 label forward-corrected in the committed
   receipt and result note (38/65 = 0.5846 is BELOW the d = 3 band
   floor 0.6000, not "inside"); d60 receipt rerun.
5. **MINORs:** full both-depth census for all 38 records in W2 incl.
   the d = 3 max census (18 exceed 4: fourteen 5s, four 6s — within
   W4b's bound 8); "max |D| does not move — W4b says why" corrected
   to a measurement statement; §4 restated as NECESSITY not route
   (+ the round's inconclusive 220-history hunt recorded); W1/W1b
   relabelled (admissibility, tie-freedom structural); determinism
   GATED (W6b: probe rebuild of anchor + winner under three seeds,
   byte-identical); B = 2 gated in W4b's predicate; the F2 branch
   text made the pre-registered disjunction; the cadence probe
   counted as a variant (37 + 1); h4 added to the anchor
   atlas-agreement; exit-scan widened to Name-call exits; "width
   follows that shape" dropped (width cannot dip).

**Verdict after repairs: F3 stands as a d = 2 statement; W4b stands
as proved; the unit is TERMINAL for round 1.**  The substrate for the
cocycle unit remains DOUBLE-RING(8, 10, 8) with the ends caveat
attached.
