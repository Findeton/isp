# SCOUT-PSI — the equal-density / different-preparation test (repaired)

**Unit:** v15/note-scoutpsi.md + v15/code/scoutpsi_exact.py (output
v15/code/scoutpsi_output.txt, receipt v15/code/scoutpsi_receipt.json).
**Authority:** v15/note-scoutpsi-pin.md (FROZEN 8e9fe2448b00), ordered at
ledger #64 as decisive computation (ii), pinned and launched at ledger #65;
the pin addendum v15/note-scoutpsi-pin-addendum.md (FROZEN e717d3bbc1df at
ledger #68), consumed by gate [LIC:G-ADDENDUM-CONSUMED]; the verifier review
v15/review-scoutpsi-verifier.md (FROZEN 7590f2c7abc1 at ledger #76); the
repair orders Z1-Z8 of ledger #76, the routing erratum of ledger #77, and
the ledger #80 sharpening.  Scout class: battery + ONE hostile verifier
seat.  Between delivery and that seat plus the user's read, every reading
here is a **candidate reading**.

**The S4 source, stated per the pin, per read.**  The S4 apparatus of the
committed scout is consumed BY ANCHOR AT THE COMMITTED DIGESTS —
v15/note-scout-bridge.md 34f10a6fd494 and v15/code/scout_receipt.json
12bdb7a58909 — the anchors the pin names: the committed witness values are
embedded in the instrument and recomputed against this unit's own machinery
[LIC:G-S4-CONSUMED].  The scout repair landed as commit e8cb399 DURING the
original build; the repaired successor's s4_linearity rows are additionally
verified at the value grain against the same embedded committed values —
the witness and its flags are unchanged by the repair — by a live read of
v15/code/scout_receipt.json that serializes no live-file digest (the
G-ENV-EXCLUSION lesson of the repair itself) [LIC:G-S4-REPAIRED].  The pin
note, the pin addendum, the DC bipartite-causality addendum v2 and
v14/paper-20-coupling.md are read live and digest-gated (8e9fe2448b00,
e717d3bbc1df, ca713e89633b, 4824d190af73) [LIC:G-PIN-DIGESTS].

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
| EMISSION HISTORY | the ordered tuple of emitted cells along one branch, window by window [SS:EMISSION-HISTORIES] |

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

Three declared names: [SS:CELLS] for one-step branch weights over the 27
pair-cells, [SS:RECORD-FIELDS] for record distributions over record n-fields
at a window, and [SS:EMISSION-HISTORIES] for distributions over complete
ordered CELL-HIT emission histories at a window.  Every probability-typed
row in the receipt declares its sample space from these names
[LIC:G-SAMPLE-SPACE], and comparisons order records as 27-tuples,
lexicographically; "first divergence" always means the lexicographically
least diverging record at the earliest diverging window.

## S1 — the preparations (three rhos, seven decompositions, mixtures gated)

The arena is the committed one, rebuilt from constructors: 27 cells over 9
sites, 3 links, the Grover-over-3 coin with count phase, delivered order
G.D, exactly unitary over Z[w] [LIC:G-ARENA] with squared norm conserved at
every branch of every tree [LIC:G-UNITARITY].

**RHO1** is the equal mixture of cells 0 and 1 (site (0,0), links (1,0) and (0,1)).
**RHO2** is the equal mixture of cells 0 and 5 (sites (0,0) and (0,1), links (1,0) and (1,1)).
**RHOSTAR** is the frozen secondary of the #68 addendum: the maximally
mixed state on the S4 carrier, equal to I/27 entry by entry from both of
its frozen decompositions [LIC:G-MAXMIX].

| ensemble | members (unnormalized amplitudes, scale2 declared) | frozen status |
|---|---|---|
| D1A | e0 ; e1 | FROZEN (addendum item 1, primary) |
| D1B | e0 + e1 ; e0 - e1 (scale2 2 each) | FROZEN (addendum item 1, primary) |
| D1C | e0 + w e1 ; e0 - w e1 (scale2 2 each) | unfrozen extension, disclosed |
| D2A | e0 ; e5 | unfrozen extension, disclosed |
| D2B | e0 + e5 ; e0 - e5 (scale2 2 each) | unfrozen extension, disclosed |
| D1S | the 27 computational basis states, uniform weights 1/27 | FROZEN (addendum item 1, secondary) |
| D2S | the 27 F3-character states, uniform weights 1/27, scale2 27 | FROZEN (addendum item 1, secondary) |

All D1-family and D2-family weights are 1/2; the secondary's weights are
1/27.  Within each rho, every ensemble's weighted mixture is the same
density matrix over Q(w), entry by entry [LIC:G-RHO-EQUAL], and the
ensembles are genuinely distinct as ensembles — their weighted member
density matrices differ as multisets, pairwise, with the receipt field
wired to the computed value [LIC:G-DISTINCT].  All six member rays of
RHO1's three ensembles are pairwise distinct.  Every ensemble record
distribution carries total mass exactly 1 at every window [LIC:G-MASS].

The primary pair is the canonical steerable pair, verified in-run: both
ensembles are internally orthogonal and mutually unbiased at exact overlap
ratio 1/2 — the Z-basis and X-basis ensembles of the span
[LIC:G-HJW-PAIR].

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

The witness record read out: one CELL-HIT on cell 2 and one CELL-HIT on cell 14.
Both full window-1 and window-2 record distributions of D1A and D1B are
published in the receipt (witness_distributions), 27 records each at window 2;
window-3 distributions are published as digests with their record counts.

every measured decomposition pair of both rhos diverges first at window 2,
and window 3 diverges at every pair as well; windows beyond 3 are
registered, not claimed

## Z1 — the frozen secondary, run through this unit's own instrument

the frozen secondary rho** -- the maximally mixed state on the S4 carrier
-- is BLIND at window 1 and SENSITIVE at window 2 on its frozen pair
D1S|D2S (computational basis uniform vs F3-character basis uniform): 378
records diverge at window 2, first diverging record {26:2} with masses 0
and 1/729 [SS:RECORD-FIELDS]

This is the leg the original delivery never ran (verifier finding F1); the
verifier's own measurement of it (review row R16) is embedded in the
instrument as a gated expectation and re-derived [BY:THIS-INSTRUMENT] by
this unit's own walk, never copied [LIC:G-SECONDARY-EXPECT].  The frozen
secondary's window-1 and window-2 distributions and window-3 digests are
published in the receipt (secondary_distributions).

## Z2 — the four frozen comparison rows, per-row verdicts, named groups

The addendum's four frozen rows are {complete ordered CELL-HIT emission
histories, final count field} x {raw labels, relabelling-quotiented}.  The
addendum never named its relabelling group (the verifier's residual freeze
defect); this repair names two and publishes both, so the quotient rows
appear at both grains: **T9**, the Z3xZ3 site-translation subgroup — a
symmetry of the arena's constructors — and **S27**, the full simultaneous
relabelling group Sym(27) on cell labels, the coarsest label quotient (a
count field keeps only its multiset of counts; an ordered history keeps
only its equality pattern).  No quotient row diverges where its raw row is
equal: label aggregation never manufactures a difference
[LIC:G-QUOT-CONSISTENT].

all four frozen comparison rows are measured with per-row verdicts at
every pair: at the raw and translation-quotient grains every measured pair
of all three rhos diverges first at window 2; at the coarsest
simultaneous-relabelling quotient the witness pair is BLIND at window 2
and first diverges at window 3, in 2 classes [SS:RECORD-FIELDS]

under the site-translation quotient (the Z3xZ3 subgroup) the witness pair
stays SENSITIVE at window 2 with 27 diverging classes, and the class of
{23:1,26:1} carries masses 40/729 and 8/729 [SS:RECORD-FIELDS]

The full per-row verdict table, delivered rule, all pairs (gated verdict
by verdict [LIC:G-GRAIN-VERDICTS]; the verifier's class masses
re-derived [BY:THIS-INSTRUMENT] at [LIC:G-VERIFIER-CLASS]):

| family | rho | pair | row | verdict |
|---|---|---|---|---|
| GRAIN | RHO1 | D1A vs D1B | ordered-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1B | ordered-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1B | ordered-quotient-S27 | BLIND-AT-1-2-SENSITIVE-AT-3 |
| GRAIN | RHO1 | D1A vs D1B | count-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1B | count-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1B | count-quotient-S27 | BLIND-AT-1-2-SENSITIVE-AT-3 |
| GRAIN | RHO1 | D1A vs D1C | ordered-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1C | ordered-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1C | ordered-quotient-S27 | BLIND-AT-1-2-SENSITIVE-AT-3 |
| GRAIN | RHO1 | D1A vs D1C | count-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1C | count-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1A vs D1C | count-quotient-S27 | BLIND-AT-1-2-SENSITIVE-AT-3 |
| GRAIN | RHO1 | D1B vs D1C | ordered-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1B vs D1C | ordered-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1B vs D1C | ordered-quotient-S27 | BLIND-AT-1-2-SENSITIVE-AT-3 |
| GRAIN | RHO1 | D1B vs D1C | count-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1B vs D1C | count-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO1 | D1B vs D1C | count-quotient-S27 | BLIND-AT-1-2-SENSITIVE-AT-3 |
| GRAIN | RHO2 | D2A vs D2B | ordered-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO2 | D2A vs D2B | ordered-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO2 | D2A vs D2B | ordered-quotient-S27 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO2 | D2A vs D2B | count-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO2 | D2A vs D2B | count-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHO2 | D2A vs D2B | count-quotient-S27 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHOSTAR | D1S vs D2S | ordered-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHOSTAR | D1S vs D2S | ordered-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHOSTAR | D1S vs D2S | ordered-quotient-S27 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHOSTAR | D1S vs D2S | count-raw | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHOSTAR | D1S vs D2S | count-quotient-T9 | BLIND-AT-1-SENSITIVE-AT-2 |
| GRAIN | RHOSTAR | D1S vs D2S | count-quotient-S27 | BLIND-AT-1-SENSITIVE-AT-2 |

Diverging-class counts on the witness pair and the secondary (window 2 /
window 3), from the same gated rows:

| family | pair | row | window 2 | window 3 |
|---|---|---|---|---|
| GRAIN | D1A vs D1B | ordered-raw | 27 | 486 |
| GRAIN | D1A vs D1B | count-raw | 27 | 477 |
| GRAIN | D1A vs D1B | count-quotient-T9 | 27 | 240 |
| GRAIN | D1A vs D1B | count-quotient-S27 | 0 | 2 |
| GRAIN | D1S vs D2S | ordered-raw | 729 | 19683 |
| GRAIN | D1S vs D2S | count-raw | 378 | 3654 |
| GRAIN | D1S vs D2S | count-quotient-T9 | 42 | 414 |
| GRAIN | D1S vs D2S | count-quotient-S27 | 2 | 3 |

Read honestly, the coarse blindness is a property of the RHO1 witness
family at these windows, not a universal: RHO2's pair and the secondary
stay sensitive at window 2 even under the coarsest quotient.  The verdict
word carries its grain everywhere in this note.

## S3 — the controls, both through the real machinery, both gated

the declared genuinely linear completion -- the selective collapse reading
paper-20 names as not run -- is BLIND at windows 1, 2 and 3 on the same
decompositions, record by record [SS:RECORD-FIELDS] [LIC:G-NULL-BLIND]

the null is blind at all four comparison rows and both quotient groups,
and its Kraus completeness sum K-dagger K = I verifies exactly
[SS:RECORD-FIELDS]

The null is declared exactly, per addendum item 3: record the emitted cell
and collapse the state onto the shifted emitted cell — a projective
cell-basis instrument composed with the walk unitary, a completely
positive trace-preserving completion of the record leg, and paper-20's own
named-but-not-run selective reading.  Its Kraus form is
K_c = (1/3) |e_SHIFT[c]> <row c of C(n)|, complete over Z[w] at the probe
records [LIC:G-NULL-KRAUS].  It runs on the SAME seven decompositions
through the same tree engine.

the synthetic decomposition-sensitive control reads SENSITIVE at window 1:
on the witness pair it assigns masses 16/33 and 64/129 to its first
diverging record {2:1} [SS:RECORD-FIELDS] [LIC:G-POSITIVE-SENSITIVE]

The positive is declared exactly: branch weights proportional to the SQUARES
of the Born weights (state leg uncollapsed) — quadratic in the state by
construction, so it must and does separate the ensembles immediately.

## S4 — the weld to the committed apparatus

the S4 apparatus is consumed at the committed digests 34f10a6fd494 and
12bdb7a58909, and the committed nonlinearity witness is recomputed
exactly: branch cell 0, entry (4, 4), value 1/36

The committed closed form -(1/4)(w_c(rho0)-w_c(rho1))(P0-P1) verifies entry
by entry on this instrument's own machinery [LIC:G-CLOSED-FORM], and the
recomputed witness equals the embedded committed values [LIC:G-S4-CONSUMED].
The repaired successor carries the identical s4_linearity witness rows,
verified at the value grain [LIC:G-S4-REPAIRED].  The delivered-rule
sentences quoted above are verified verbatim against the live paper-20
bytes [LIC:G-P20-ANCHOR].

## The verdict, grain-indexed

```
SCOUTPSI-DECOMPOSITION-SENSITIVE-AT-2-AT-THE-FINE-GRAINS<WINDOW-1-BLIND-AT-EVERY-PAIR-BY-MEASUREMENT; FIRST-DIVERGENCE-AT-WINDOW-2-ON-RHO1-D1A-VS-D1B-AT-RECORD-2x1-14x1-MASSES-16-OVER-729-VS-32-OVER-729; EVERY-MEASURED-PAIR-OF-ALL-THREE-RHOS-DIVERGES-FIRST-AT-WINDOW-2-AT-THE-RAW-AND-TRANSLATION-GRAINS; SECONDARY-MAXIMALLY-MIXED-BLIND-AT-1-SENSITIVE-AT-2-AT-378-DIVERGING-RECORDS; BLIND-AT-2-SENSITIVE-AT-3-AT-THE-COARSEST-QUOTIENT-ON-THE-WITNESS-PAIR; NULL-SELECTIVE-COMPLETION-BLIND-AT-ALL-THREE-WINDOWS-AT-ALL-FOUR-ROWS; POSITIVE-SYNTHETIC-MAP-SENSITIVE-AT-WINDOW-1; WINDOWS-BEYOND-3-REGISTERED-NOT-CLAIMED>
```

## Z3 — the operational qualification, gated

a SENSITIVE verdict proves rho is not a sufficient state descriptor FOR
THE DELIVERED CELL-HIT RULE on pure-state ensembles

it becomes an experimental distinction only if ISP can operationally
prepare both decompositions -- preparation and intervention protocols are
UNBUILT, and no experimental distinction is claimed

a future triple-event law with a different state update may remove or
change the sensitivity, and no sentence here reads the verdict as deciding
the psi-ontology

the tested primary pair is the canonical remotely-steerable decomposition
pair: D1A and D1B are the Z-basis and X-basis ensembles of the
two-dimensional span (Hughston-Jozsa-Wootters), exactly the two ensembles
a remote party could prepare by measuring her half of a Bell pair in
either basis, so the sensitivity is a hard compatibility gate on any
future ISP composite dynamics (the DC bipartite-causality addendum v2,
digest ca713e89633b, is the standing obligation)

non-collapse is not presented as a safety property against steering,
steering-unphrasability is incompleteness rather than safety, and
paper-38's zero is scoped as a reading of an unchanged record, not a wall
against a future steering test

These sentences are the addendum's item 4 wall, sharpened by ledger #80,
and the instrument refuses this note without them [LIC:G-QUAL-GATED].

## The walls, consumed

this unit decides no ontology: it measures a property of the delivered rule,
and the fork's resolution is a program decision informed by this measurement

the machine ontology wall is a literal pattern blacklist, not a semantic
classifier: the enforcement is the blacklist plus the verifier seat and
the candidate-reading discipline; the seat's passing paraphrases are
embedded as permanent plants that die at the wall, and the general
fresh-paraphrase condition stays registered, not claimed

Per the pin, what is measured is the operational content of the #64
dichotomy at the measured windows: under the delivered rule as formalized at
the committed S4, the future record distributions of two genuinely distinct
preparations of one density matrix are NOT equal from window 2 on at the
fine grains, and are exactly equal at window 1.  Which branch of the #64
fork the program takes — replacing the rule, or treating the compressed
description as an insufficient summary of a preparation — is the user's
decision, not this unit's.  Per the W-REPRESENTATION wall, psi, rho,
kernels and Hamiltonians are representations here; no sentence in this
note promotes any of them to ontology, and the fork stays open in both
directions.  E-34 is respected throughout: the record counts CELL-HITs,
and no CELL-HIT is called a division event.

## The breach and its repair, disclosed (Z4, Z8)

The original delivery of this unit (ledger #70) was in breach of its own
pre-registration, and the fault chain is owned on the record: the #68 pin
addendum (e717d3bbc1df) froze the secondary preparation, the four
comparison rows, the null instrument and the qualification sentences
MID-BUILD, and it was never routed to the running worker — the
orchestrator's own erratum at ledger #77 traces this and owns the breach
(a pin addendum uncommunicated to a running worker does not bind the
worker).  The delivered unit ran unfrozen ensembles (D1C and the RHO2
family) in place of the frozen secondary, published one comparison row of
four, carried none of the qualification sentences, and neither cited nor
gated the addendum; ledger #70's sentence "the pre-registered preparations
run exactly as frozen" was the worker's compliance claim engraved as fact,
and it is FALSE — the erratum stands at ledger #76.  The verifier seat
(review 7590f2c7abc1, findings F1-F9) measured the mitigation itself: the
frozen legs, run at the seat, return the same row verdict.  Order of
events, disclosed: the original unit had already built and inspected the
primary, D1C and RHO2 computations before any addendum text reached it.
This repair received the addendum text and the verifier's measured
expected values in its launch order (ledger #77), consumed the addendum at
its frozen digest by gate [LIC:G-ADDENDUM-CONSUMED], and
re-derived [BY:THIS-INSTRUMENT] every frozen leg with the seat's values
as gated expectations rather than copied results [LIC:G-SECONDARY-EXPECT]
[LIC:G-GRAIN-VERDICTS] [LIC:G-VERIFIER-CLASS].  No committed measured
value moved: the witness row, all four committed first-divergence windows,
the positive-control row and all five committed window-3 digests
re-derive byte-identically [BY:THIS-INSTRUMENT], and the repair only adds
rows [LIC:G-NO-VALUE-MOVED].

## Numeral totality (Z5)

numeral totality: 616 numeral occurrences in this note; 443 bound to receipt fields; 173 non-claim with reason classes; every occurrence classified

Every numeral occurrence — every maximal digit run — is classified
per-occurrence, BOUND to a specific receipt field or NON-CLAIM with a
declared reason class, by an ordered rule table in the instrument; the
full per-occurrence table is serialized in the receipt
(numeral_totality.rows) and the classification is gated total
[LIC:G-NUMERAL-TOTALITY].  This replaces the original delivery's integer
whitelist entirely (verifier finding F5).

## Deviations, disclosed

1. **The S4 source is dual-anchored across the repair's landing.**  The
   consumption anchor is the committed digests (34f10a6fd494, 12bdb7a58909)
   via embedded, recomputed values; the scout repair landed as commit
   e8cb399 during the original build, and the repaired successor's
   s4_linearity rows are verified identical at the value grain by a live
   read that serializes no live-file digest.  If a later repair moves those
   rows, G-S4-REPAIRED is the tripwire to re-run.
2. **The coin order is the delivered G.D only.**  The alternative order is
   registered, not measured; the committed S4 apparatus is G.D.
3. **Windows.**  Claims are exact at windows 1, 2, 3; windows 4 and deeper
   are registered, not claimed.
4. **Decomposition scope, corrected (Z6).**  The original sentence here —
   that unequal-weight decompositions would need amplitudes outside Q(w)
   at this rho family — was false in both directions (verifier finding
   F7).  The truth, verified in-run: two-member unequal-weight pure
   decompositions of these rank-2 equal-eigenvalue rhos are impossible
   over EVERY field — the Bloch balance rho.rho = rho/2 forces weights
   1/2 and 1/2 [LIC:G-DEV4-WITNESS] — while unequal-weight FOUR-member
   decompositions exist entirely inside Z[w]: the witness
   {1/3 e0; 1/3 e1; 1/6 (e0 + e1); 1/6 (e0 - e1)} mixes exactly to RHO1,
   verified entry by entry [LIC:G-DEV4-WITNESS].  Sensitivity
   measurements on such larger ensembles are a registered successor, not
   measured here.
5. **Unfrozen extensions.**  D1C and the RHO2 family are unfrozen
   extensions beyond the addendum's preparations, disclosed as such
   (verifier finding F1); the frozen primary and the frozen secondary
   both run, and the headline stands on frozen ground.
6. **The relabelling groups are this repair's naming.**  The addendum
   froze "relabelling-quotiented" without naming a group; T9 and S27 are
   declared here and published per row (the freeze defect is the
   addendum's, disclosed by the verifier).
7. **The primary-support anchor is an embedded constant.**  The committed
   scout receipt carries no support field to anchor, so the frozen
   deterministic rule could not be executed as written; the embedded
   cells 0 and 1 match the committed s4_map bases (verifier finding F8).
8. **Chain time.**  The delivery chain (double build, note verification,
   write) runs in under a minute; the falsifier sweep re-runs the full
   pipeline fresh per mutant.
9. **Review shape.**  Orchestrator battery + ONE hostile verifier seat,
   per the pin; the smallness is the pin's order.

## The instrument

v15/code/scoutpsi_exact.py: delivery is the only writer and a failing run
writes nothing; --no-write, --numbers, --kit, --selftest, --mutant NAME,
--verify-paper PATH, --list-gates, --list-mutants; unknown or conflicting
argv exits with the usage code.  33 gate names; 28 registered falsifiers,
each naming the measured object it corrupts and the gate it must die at,
each verified by a fresh full run with a digest move proof and the artifacts
byte-untouched.  The abstract-syntax self-scan bans float literals, the
builtin hash and undeclared imports; nothing serialized is fed from a bare
set or dict iteration (sorted() discipline); the artifacts carry no
environment-dependent bytes.  The note is the object under test: its digest
is written into both artifacts, every required sentence above is rendered
from the measurements and matched whitespace-collapsed, every slash rational
is checked against the receipt's inventory, every numeral occurrence is
classified per-occurrence, and the walls are scanned hyphen-robust and
heading-aware.

the pin addendum is consumed at its frozen digest e717d3bbc1df: the frozen
preparations, the four comparison rows, the frozen null instrument and the
qualification sentences are checked in-run against what ran
