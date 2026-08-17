# SCOUT-PSI — the equal-density / different-preparation test

**Unit:** v15/note-scoutpsi.md + v15/code/scoutpsi_exact.py (output
v15/code/scoutpsi_output.txt, receipt v15/code/scoutpsi_receipt.json).
**Authority:** v15/note-scoutpsi-pin.md (FROZEN 8e9fe2448b00), ordered at
ledger #64 as decisive computation (ii), pinned and launched at ledger #65.
Scout class: battery + ONE hostile verifier seat.  Between delivery and that
seat plus the user's read, every reading here is a **candidate reading**.

**The S4 source, stated per the pin, per read.**  The S4 apparatus of the
committed scout is consumed BY ANCHOR AT THE COMMITTED DIGESTS —
v15/note-scout-bridge.md 34f10a6fd494 and v15/code/scout_receipt.json
12bdb7a58909 — the anchors the pin names: the committed witness values are
embedded in the instrument and recomputed against this unit's own machinery
[LIC:G-S4-CONSUMED].  The scout repair landed as commit e8cb399 DURING this
unit's build; the repaired successor's s4_linearity rows are additionally
verified at the value grain against the same embedded committed values —
the witness and its flags are unchanged by the repair — by a live read of
v15/code/scout_receipt.json that serializes no live-file digest (the
G-ENV-EXCLUSION lesson of the repair itself) [LIC:G-S4-REPAIRED].  The pin
note and v14/paper-20-coupling.md are read live and digest-gated
(8e9fe2448b00, 4824d190af73) [LIC:G-PIN-DIGESTS].

Every measured number in this note is bound to the receipt: the instrument
renders the required sentences from its own measurements and refuses the note
if any is absent or altered, and every load-bearing numeral is bound to its
specific receipt field by a gate [LIC:G-NUMERAL-BINDING].  Exact arithmetic
throughout; no number here carries a laboratory unit; every census is finite
and no continuum claim is made.

## The term-binding table (W4-TYPE-IDENTITY)

| term | the one binding |
|---|---|
| CELL-HIT | paper-20's primitive: one Born-selected pair-cell increment per step (the mandatory E-34 rename; the only thing the record counts here) |
| DIVISION-EVENT | paper-19's three-actor grammar object; it does not occur in this unit's measurements and is never conflated with a CELL-HIT |
| PREPARATION | one ensemble of weighted pure states presented to the delivered rule; a preparation is an ensemble, not a density matrix |
| ENSEMBLE | a finite list of (weight, pure state) members with weights summing to one; two ensembles are genuinely distinct when their weighted member density matrices differ as multisets |
| RECORD DISTRIBUTION | the probability law over record n-fields (27-tuples of CELL-HIT counts) at a declared window [SS:RECORD-FIELDS] |

## The object under test (paper-20's delivered rule, quoted from its bytes)

The delivered rule, quoted from the v14/paper-20-coupling.md:633 region:

> The record accumulates the law's own weights and the state is not collapsed
> onto the emitted cell, so the walk stays coherent between division events.

> The selective reading is a different object — a classical Markov chain on
> cells — and it is not run.

As the committed S4 formalizes it: per step, per branch, the one-step
CELL-HIT branch weights are the Born weights of the post-coin state at the
branch's own record [SS:CELLS]; the record leg is per-outcome (n plus one
CELL-HIT on the emitted cell); the state leg is the SAME uncollapsed evolved
state on every outcome of that branch; and the next step's coin consumes the
branch's own record through the count phase.  The propagation here is
per-branch exact — each pure member with its ensemble weight, per the pin.

## S0 — the sample-space spine

Two declared names: [SS:CELLS] for one-step branch weights over the 27
pair-cells, [SS:RECORD-FIELDS] for record distributions over record n-fields
at a window.  Every probability-typed row in the receipt declares its sample
space from these two names [LIC:G-SAMPLE-SPACE], and comparisons order
records as 27-tuples, lexicographically; "first divergence" always means the
lexicographically least diverging record at the earliest diverging window.

## S1 — the preparations (two rhos, five ensembles, mixtures gated equal)

The arena is the committed one, rebuilt from constructors: 27 cells over 9
sites, 3 links, the Grover-over-3 coin with count phase, delivered order
G.D, exactly unitary over Z[w] [LIC:G-ARENA] with squared norm conserved at
every branch of every tree [LIC:G-UNITARITY].

**RHO1** is the equal mixture of cells 0 and 1 (site (0,0), links (1,0) and
(0,1)).  Its three ensembles, all weights 1/2:

| ensemble | members (unnormalized amplitudes, scale2 declared) |
|---|---|
| D1A | e0 ; e1 |
| D1B | e0 + e1 ; e0 - e1 (scale2 2 each) |
| D1C | e0 + w e1 ; e0 - w e1 (scale2 2 each) |

**RHO2** is the equal mixture of cells 0 and 5 (sites (0,0) and (0,1), links
(1,0) and (1,1)); its ensembles are D2A (e0 ; e5) and D2B (e0 + e5 ;
e0 - e5, scale2 2 each).

Within each rho, every ensemble's weighted mixture is the same density
matrix over Q(w), entry by entry [LIC:G-RHO-EQUAL], and the ensembles are
genuinely distinct as ensembles — their weighted member density matrices
differ as multisets, pairwise [LIC:G-DISTINCT].  All six member rays of
RHO1's three ensembles are pairwise distinct.  Every ensemble record
distribution carries total mass exactly 1 at every window [LIC:G-MASS].

## S2 — the measurement (windows 1, 2, 3; exact comparison over Q(w))

window 1 is BLIND at every decomposition pair of both committed rhos: the
one-step CELL-HIT branch weights enter the ensemble record marginal
linearly, and all 4 pairwise comparisons agree record by record
[SS:RECORD-FIELDS] [LIC:G-WINDOW1-BLIND]

The window-1 mechanism, as bookkeeping: each member's one-step weight vector
is a ratio of quadratic forms in the member state whose denominator is fixed
by exact unitarity at 9 times the declared scale2 [SS:CELLS]
[LIC:G-UNITARITY], so the ensemble marginal — by the delivered rule's own
per-branch form, the weighted sum of the members' Born vectors — is a linear
functional of the mixture and cannot separate equal-mixture ensembles at one
step.  From window 2 the branch weights multiply across steps and the
product is quadratic in the member state; the S4 nonlinearity witness is
exactly this obstruction at mixture level.

the first divergence is at window 2: preparations D1A and D1B of the same
rho assign masses 16/729 and 32/729 to the record {2:1,14:1}, difference
-16/729, and 27 records diverge at that window [SS:RECORD-FIELDS]
[LIC:G-SENSITIVE]

The witness record read out: one CELL-HIT on cell 2 (site (0,0), link (1,1))
and one CELL-HIT on cell 14 (site (1,1), link (1,1)).  Both full window-1
and window-2 record distributions of D1A and D1B are published in the
receipt (witness_distributions), 27 records each at window 2; window-3
distributions are published as digests with their record counts.

every measured decomposition pair of both rhos diverges first at window 2,
and window 3 diverges at every pair as well; windows beyond 3 are
registered, not claimed

## S3 — the controls, both through the real machinery, both gated

the declared genuinely linear completion -- the selective collapse reading
paper-20 names as not run -- is BLIND at windows 1, 2 and 3 on the same
decompositions, record by record [SS:RECORD-FIELDS] [LIC:G-NULL-BLIND]

The null is declared exactly: record the emitted cell and collapse the state
onto the shifted emitted cell — a projective cell-basis instrument composed
with the walk unitary, a completely positive trace-preserving completion of
the record leg, and paper-20's own named-but-not-run selective reading.  It
runs on the SAME five ensembles through the same tree engine.

the synthetic decomposition-sensitive control reads SENSITIVE at window 1:
on the witness pair it assigns masses 16/33 and 64/129 to its first
diverging record {2:1} [SS:RECORD-FIELDS] [LIC:G-POSITIVE-SENSITIVE]

The positive is declared exactly: branch weights proportional to the SQUARES
of the Born weights (state leg uncollapsed) — quadratic in the state by
construction, so it must and does separate the ensembles immediately.

## S4 — the weld to the committed apparatus

the S4 apparatus is consumed at the committed digests 34f10a6fd494 and
12bdb7a58909, and the committed nonlinearity witness is recomputed exactly:
branch cell 0, entry (4, 4), value 1/36

The committed closed form -(1/4)(w_c(rho0)-w_c(rho1))(P0-P1) verifies entry
by entry on this instrument's own machinery [LIC:G-CLOSED-FORM], and the
recomputed witness equals the embedded committed values [LIC:G-S4-CONSUMED].
The repaired successor carries the identical s4_linearity witness rows,
verified at the value grain [LIC:G-S4-REPAIRED].  The delivered-rule
sentences quoted above are verified verbatim against the live paper-20
bytes [LIC:G-P20-ANCHOR].

## The verdict

```
SCOUTPSI-DECOMPOSITION-SENSITIVE-AT-2<WINDOW-1-BLIND-AT-EVERY-PAIR-BY-MEASUREMENT;
FIRST-DIVERGENCE-AT-WINDOW-2-ON-RHO1-D1A-VS-D1B-AT-RECORD-2x1-14x1-MASSES-16-OVER-729-VS-32-OVER-729;
EVERY-MEASURED-PAIR-OF-BOTH-RHOS-DIVERGES-FIRST-AT-WINDOW-2;
NULL-SELECTIVE-COMPLETION-BLIND-AT-ALL-THREE-WINDOWS;
POSITIVE-SYNTHETIC-MAP-SENSITIVE-AT-WINDOW-1;
WINDOWS-BEYOND-3-REGISTERED-NOT-CLAIMED>
```

## The walls, consumed

this unit decides no ontology: it measures a property of the delivered rule,
and the fork's resolution is a program decision informed by this measurement

Per the pin, what is measured is the operational content of the #64
dichotomy at the measured windows: under the delivered rule as formalized at
the committed S4, the future record distributions of two genuinely distinct
preparations of one density matrix are NOT equal from window 2 on, and are
exactly equal at window 1.  Which branch of the #64 fork the program takes —
replacing the rule, or treating the compressed description as an
insufficient summary of a preparation — is the user's decision, not this
unit's; no sentence here asserts an ontology, and the instrument scans this
note for the offending forms.  E-34 is respected throughout: the record
counts CELL-HITs, and no CELL-HIT is called a division event.

## Deviations, disclosed

1. **The S4 source is dual-anchored across the repair's landing.**  The
   consumption anchor is the committed digests (34f10a6fd494, 12bdb7a58909)
   via embedded, recomputed values; the scout repair landed as commit
   e8cb399 during this unit's build, and the repaired successor's
   s4_linearity rows are verified identical at the value grain by a live
   read that serializes no live-file digest.  If a later repair moves those
   rows, G-S4-REPAIRED is the tripwire to re-run.
2. **The coin order is the delivered G.D only.**  The alternative order is
   registered, not measured; the committed S4 apparatus is G.D.
3. **Windows.**  Claims are exact at windows 1, 2, 3; windows 4 and deeper
   are registered, not claimed.
4. **Decomposition scope.**  Five ensembles, all with weights 1/2 and
   members inside Z[w]; unequal-weight decompositions would need amplitudes
   outside Q(w) at this rho family and are registered, not measured.  The
   ensembles are two-member; larger ensembles are registered, not measured.
5. **Chain time.**  The delivery chain (double build, note verification,
   write) runs in a few seconds; the falsifier sweep re-runs the full
   pipeline fresh per mutant.
6. **Review shape.**  Orchestrator battery + ONE hostile verifier seat, per
   the pin; the smallness is the pin's order.

## The instrument

v15/code/scoutpsi_exact.py: delivery is the only writer and a failing run
writes nothing; --no-write, --numbers, --kit, --selftest, --mutant NAME,
--verify-paper PATH, --list-gates, --list-mutants; unknown or conflicting
argv exits with the usage code.  20 gate names; 14 registered falsifiers,
each naming the measured object it corrupts and the gate it must die at,
each verified by a fresh full run with a digest move proof and the artifacts
byte-untouched.  The abstract-syntax self-scan bans float literals, the
builtin hash and undeclared imports; nothing serialized is fed from a bare
set or dict iteration (sorted() discipline); the artifacts carry no
environment-dependent bytes.  The note is the object under test: its digest
is written into both artifacts, every required sentence above is rendered
from the measurements and matched whitespace-collapsed, every slash rational
and integer numeral is checked against the receipt's inventories, and the
walls are scanned hyphen-robust and heading-aware.
