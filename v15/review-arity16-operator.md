# ARITY-16 (PAPER-50) — OPERATOR REVIEW (K1) — FROZEN

**Seat:** K1 / OPERATOR (hostile panel, v15 ledger #51).  **Unit under
review:** v15/paper-50-arity16.md `c86ea5edcfec`; v15/code/arity16_exact.py
`613e05fc7ff0`; v15/code/arity16_output.txt `837333a85fcb`;
v15/code/arity16_receipt.json `52f600389933`.  Pin v15/note-arity16-pin.md
`1dac6a35ddc5`.  Parents: v15/paper-44-arity.md `0d677a4cbe97` (+
arity_receipt.json `e90a41eed544`), v14/paper-39-ndep.md `e2293b8c3858` (+
ndep_receipt.json `29216cea946f`).  All seven digests re-hashed and matched
before any byte was used.

**Continuation record.**  This seat is a continuation: the original K1 was
killed by a session limit mid-rebuild (v15 LOG #54) with no frozen review.
Its scratch directory (`a16_k1/`) exists and is EMPTY — nothing was
inherited, nothing re-verified from it, and every number below was rebuilt
from scratch in a fresh scratch (`a16_k1b/`), from the declared definitions,
in independent code, exact integer arithmetic only (zero floats anywhere in
my rebuild; the committed receipt also scans float-free).

## VERDICT: ACCEPT-WITH-FIXES

No false number found.  996 independent recomputations (676 substantive
values plus the parent's 320-pair identity sweep), **zero discrepancies**;
every claimed measurement I rebuilt is EXACT, including the complete
substrate census, the 307-survivor closure, the full 1,872,400-comparison
naming census, the complete 65,536-pair schedule sweep, the SEC-2 union
census, all floor certificates and witnesses, both transport tables under
all four rules and both readings, and the 6x16 principle census.  The fixes
are two evidence-alignment minors (published sentences that are TRUE — I
verified both by exhaustive computation — but that the unit's own
instrument did not establish) and three presentation minors, one of them
made concrete by this seat's full-pool ladder closures (F5).  No measured
number, head segment, or verdict word needs repair.

## 1. What this seat rebuilt, and how

Independent implementation (shared arena module + four workers + two
verification scripts, `a16_k1b/rb_*.py`): GF(4) rebuilt from polynomial
arithmetic over F2 mod x^2+x+1 (the unit's hard-coded multiplication table
is CONFIRMED against it); the arena, both subgroup lattices, and all coset
windows re-derived by closure; the substrate censused by my own
subset-lattice DP at ALL sixteen arities; saturating pools re-enumerated
complete at a = 2, 8, 9 and re-sampled at the unit's declared 4000-round
canonical windows at a = 3, 5, 6, 7; the survivor set re-enumerated by my
own union-find closure BFS; the forcing census re-run with my own
implementations of legs 2/3/4 at both coin orders across the full modulus
fork; the naming census re-run in full with a route-A-literal
(mask-transport) subsample cross-check; the schedule sweeps re-run
complete; SEC-2 re-censused by brute force over all C(28,a) groups; the
floors re-certified with my own witness searches AND the unit's published
witnesses re-verified directly; the transport words re-derived from the
anchored receipt values under all four declared rules.  Both committed
parent receipts were re-read at every anchored path; all 13 verbatim
needles located (each exactly once) in their pinned sources; the paper's 10
fences compared against the transcript's verdict block; receipt-vs-
transcript evidence compared byte-for-byte at eleven measurement gates.

## 2. Recomputation ledger (claimed vs rebuilt)

Status is EXACT unless stated.  Charge items (1)-(9) in order.

**(1) The two lattices.**
| object | claimed | rebuilt | status |
|---|---|---|---|
| abstract subgroups of C2^4 | 67 | 67 | EXACT |
| abstract order counts | 1:1, 2:15, 4:35, 8:15, 16:1 | same | EXACT |
| F4-linear subspaces | 7 | 7 | EXACT |
| linear order counts | 1:1, 4:5, 16:1 | same | EXACT |
| abstract orders = divisors of 16 | 1,2,4,8,16 | same | EXACT |
| proper nontrivial coset sizes | {4} vs {2,4,8} | same | EXACT |
| conditional: linear selects | a = 4 = q | 4 | EXACT |
| abstract proper sizes all divide n | yes | yes | EXACT |
| characteristic (from addition) / links' span | 2 / 8 | 2 / 8 | EXACT |

**(2) The 6-principle x 16-size census.**  All 96 cells of the section-11
table rebuilt: divides-n at {1,2,4,8,16}; saturation-at-the-budget at
{2..9} (my DP: saturating pools 256 / 436,992 / 334,761 / 374,784 /
180,264 / 15,552 / 18 / 1,824 at a = 2..9, zero at a = 1 and a >= 10);
saturation-is-maximality at 2 ALONE (max weight 16 = budget only at a = 2);
linear row at {1,4,16}, abstract row = divisors; cover column YES-WITNESS at
{2,4,9}, NOT-WITHIN-CAP at {3,5,6,7}, NO-COMPLETE at 8, NO-SATURATING-ROUND
elsewhere.  Unique nontrivial selectors: linear -> 4, satmax -> 2 (the
characteristic), all others none.  EXACT, every cell.  The parent's n = 9
column cross-checked in its committed receipt: exactly three unique
selectors (round-completeness, saturation-is-maximality,
subgroup-order-available), each admitting a = 3 alone — the section-11
tie-break sentence is faithful.

**(3) The modulus rows.**
| object | claimed | rebuilt | status |
|---|---|---|---|
| identity nL/gcd(nL,n)=L at the parent's declared pairs | 320/320 | 320/320 (n<=40, L<=8) | EXACT |
| arena instance | 4 | 4 | EXACT |
| impossible budgets in R<=8 | 1,2,3,5,6,7 | same (16R mod 64) | EXACT |
| found rungs | (2,4),(4,4),(9,4) | witnesses rebuilt at all three | EXACT |
| every found set = multiples of L=4 | {4,8} | {4,8} (4-cover + doubling) | EXACT |
| mod-a rows | at a=4 only; absent at 2,9 | same | EXACT |
| a=8 pool complete | 18 | 18 (of 6,435 splits) | EXACT |
| a=8 refuses every cover | none in R<=8 | R=4 exact cover: NONE (exhaustive); R=8 multiplicity-2 cover: NONE (my exhaustive search — the unit never ran this leg; see minor F1) | EXACT (claim), GAP (evidence) |
| a=9 pool | 1,824 | 1,824 (of 11,440) | EXACT |
| capped rows 3,5 | NOT-FOUND-WITHIN-CAP, nodes 4001 | my rebuild of the same 4000-round canonical windows: NO two masks even pairwise disjoint, at 3, 5 (and also 6, 7) — the caps are honest and the 4001-node counts are exactly what that implies | EXACT |
| unit's published cover witnesses (a=2,4,9) | 4 rounds each | each verified: valid a-blocks, mass 16, pairwise-disjoint cell masks, full 64-cell cover | EXACT |

**(4) The substrate DP** (both readings of every number re-derived by my own
DP and checked against my own closed forms):
| a | groupings | idle | budget-saturating | max incidence | at max | odd weights |
|---|---|---|---|---|---|---|
| 2 | 2,027,025 | 0 | 256 | 16 | 256 | 0 |
| 3 | 22,422,400 | 1 | 436,992 | 26 | 256 | 0 |
| 4 | 2,627,625 | 0 | 334,761 | 48 | 1 | 0 |
| 5 | 2,018,016 | 1 | 374,784 | 38 | 96 | 0 |

All EXACT, totals = multinomial closed forms; NDEP's out-of-scope constant
2,627,625 and anchored witness incidence 48 both reproduced; "attained by
exactly one grouping" confirmed (weight-48 count = 1); every weight even at
every declared arity; parent's anchored n=9 column (945/280/315/126,
0/36/81/0) re-read at its receipt paths.

**(5) Transport.**  Statements: linear 3 LAW-IN-A / 3 BREAKS, abstract 2/4,
parent (anchored) 4/2; the split row is division-forcing — all EXACT, and
every one of the twelve per-law statement words matches.  Numerals: the
declared a-only rule returns 0/0/7 under BOTH readings; a-itself 1/0/6
linear (the naming row) and 0/0/7 abstract; blocks-per-round the same; the
parent's closed form 2/0/5 linear (obstruction + naming) and 1/0/6 abstract
(obstruction) — all 56 per-row rule words rebuilt from the anchored parent
values and the declared procedure, EXACT.  Both-arena words: the parent's
two NEEDS-3 rows (menu, first rung) are exactly the two that move; five of
seven keep their word.  The six synthetic controls come out as forced (by
re-derivation).  Parent word/value anchors (7 values, 7 words, 5
aggregates) re-read at the receipt paths.

**(6) The survivor set.**  307 invariant partitions by my own closure BFS
(EXACT); leg-1 verified on all 307; all 67 abstract and all 7 linear coset
partitions among them; 156 mixed-block; the 11 block-size profiles match
the receipt profile-for-profile (sum 307); closure escapes 0 (the set is
merge-closed, supporting completeness of the enumeration).

**(7) Floors and schedules.**  Certified floors 10/8/6/5 with my own
witnesses AND the unit's published witness tables verified (16 distinct
signatures, width = floor, every column summing to a, at all four
arities); every refusal row matches (TOO-FEW-SIGNATURES at k<=3 with
2/4/8 available; WEIGHT-INFEASIBLE with lightest totals 32/25/24/23/22/21
against budgets 8..18 at a=2, and the a=3/4/5 tables likewise).  NDEP's
sharpened floor, read in the event size, reproduces all four (10/8/6/5);
counting bound 4; closed form 2(a-1) agrees at a=4 only (and at the parent
arena at a=3 only — confirmed in its receipt).  Schedule: pool 256 =
matchings of the link graph (EXACT), 65,536 ordered pairs swept complete,
minimum 14, round-one discreteness impossible, and the witness pair (4,82)
is not merely valid — it is the FIRST minimal pair in the canonical pool
order (my sweep: 4,104 of 65,536 ordered pairs attain 14).  a=4 window:
256 class tuples, 24 covering (= the permutations), crystallization time 7
at all 24, min separating subset 6 at all 24, window minimum 7.  Offsets
4|1.  All EXACT.

**(8) SEC-2.**  Union: 28 carriers, 64 realised pairs, 0 doubled, seam (a
CL4 line) carries 0 declared links; 32 link edges vs 96 off-span pairs,
tripartite characterisation FALSE — all EXACT.  Census (brute force over
all C(28,a) groups): groups 378/3,276/20,475/98,280; seam-spanning
144/2,160/16,836/89,544; opens-no-pair 144/448/448/196;
opens-no-pair-and-doubles-nothing 144/0/0/0; measured minima 0/1/2/4 =
closed form C(a,2)-floor(a^2/4) = the parent's anchored column; identity
|foreign|+|within|+|doubled| = C(a,2) and |foreign| <= floor(a^2/4) checked
at every group, 0 violations.  All EXACT.

**(9) Naming.**  Full independent re-census: a=2 (15 singles + 24 covering
tuples): 1,149,480 comparisons, 121,264 positive, 48,360 at the empty
prefix; a=4 singles: 217,000 / 71,400 / 43,400; fidelity (NDEP's 24 class
tuples): 505,920 / 49,536 / 29,760 — NDEP's committed census reproduced
from scratch, independent of both units.  Totals 1,872,400 / 242,200 inside
/ 1,630,200 outside; window 1,240; linear share 31,000 over 5 singles;
mismatches 0 everywhere, with the route-A mask-transport literal re-run on
a deterministic 35-state subsample (43,400 comparisons) against the
signature route — zero disagreements.  Forcing numerals: linear 5 rounds /
5 non-unique / 5 parallel classes (thesis holds); abstract 35/35/5 (thesis
false); a=2 abstract 15/15/0; joiner counts {24:7, 6:28} at a=4 and {3:7,
1:8} at a=2; the section-9 mechanism VERIFIED OBJECT-FOR-OBJECT: the 7
rounds with 24 joiners are exactly the order-4 subgroups inside the links'
order-8 span, the 28 outside carry 6 (and at a=2 the same split gives 3
vs 1, unpublished but consistent).  Every covering tuple unique at both
arities.  All EXACT.

**Artifact self-consistency.**  All 43 ledger gates PASS; the receipt's
evidence is byte-identical to the transcript's at all eleven measurement
gates I compared; the paper's 10 fences equal the transcript's verdict
segments; the receipt's transcript-head hash matches the committed output
file; the anchored totals (5 sources / 54 path anchors / 13 verbatim / 43
gates / 43 falsifiers) all count out; zero floats in the receipt.

## 3. Findings

**Discrepancies (claimed vs rebuilt): NONE.**  Every one of the 996
comparisons is EXACT; no claimed number, table cell, word, or verdict
segment disagrees with my rebuild at any location.

**Majors: none.**

**F1 (minor, evidence alignment).**  The a=8 row publishes
`achievable_budgets: []` and the head says "THE COMPLETE POOL OF 18
SATURATING ROUNDS REFUSES EVERY COVER"; the paper's section-8 table says
"achievable budgets within the bound: none".  Within R<=8 the only
arithmetic-eligible budgets are 4 and 8, and the unit's search space is
R=4 exact covers only (a found R=4 witness is doubled to R=8; the code
never searches multiplicity-2 covers).  An R=8 homogeneous record — every
cell covered exactly twice — need not split into two R=4 covers, so the
R=8 half of "none" was asserted without evidence.  I ran the exhaustive
multiplicity-2 search over the complete 18-round pool: NO R=8 record
exists.  The published claim is therefore TRUE, but the unit's own run did
not establish it.  Fix: add the R=8 leg (or the argument) at a=8; no
number changes.

**F2 (minor, evidence alignment).**  The head and section 9 say "the
census is blind across the declared modulus fork 2|3|4".  The instrument
sweeps the fork at the single-round windows only; the covering-tuple leg
runs at the primary modulus alone — and the tuples are exactly where
records reach 4 and the three moduli genuinely differ.  I swept the
48 tuple histories at m = 2, 3, 4 against the full survivor set: the
admissible sets are identical at every history, so the sentence is TRUE as
published — but its tuple half was not the unit's own measurement.  Fix:
extend the fork sweep to the covering-tuple leg; no number changes.

**F3 (minor, wording).**  Section 6 and the crystallization fence say the
offsets 4|1 read "against the parent's constant 1."  The parent's own
along-a offset column is 0|1|1|0 (its committed receipt; its paper says in
terms "on this axis the offset is not constant").  The "constant 1" has a
true referent — the anchored parent value, i.e. the committed-arity offset
that is constant 1 along the NDEP arena line (floors 2/4/6 against times
3/5/7 at n = 4/9/16) — and the very next sentence of section 6 correctly
recalls the parent's non-constancy, but the fence phrase alone invites the
false reading "the parent's table was constant along a."  Fix: one
clarifying word (e.g. "the parent line's constant committed-arity 1"); no
number changes.

**F4 (minor, wording).**  The transport fence compresses two true claims
into one clause: "UNDER THE PARENT'S CLOSED-FORM RULE THE OBSTRUCTION ROW
ALONE TRANSPORTS: 2 LAW-IN-A, 0 NEEDS-3 AND 5 BREAKS, AT BOTH ARENAS."
The 2/0/5 is THIS arena's linear closed-form tally (obstruction + naming);
the parent's closed-form tally was 1 LAW-IN-A (anchored, P-AGG-CF); "alone
... at both arenas" is the cross-arena intersection.  Section 12's prose
states all three precisely (including the single-feasible-row disclosure
for the naming row); the fence alone could be misread as "2/0/5 at both
arenas."  Wording only; every numeral is licensed.

**F5 (minor, made concrete by this review).**  The section-8 ladder
table's column is headed "achievable budgets within the bound" and its
a = 3 and a = 5 cells read "none".  My full-pool closures (B1) exhibit
verified R = 4 covers at BOTH arities, so under the column header's
literal reading those two cells are false about the arena — budgets
{4, 8} exist at a = 3 and a = 5.  The unit is guarded everywhere else:
the same rows carry witness status NOT-FOUND-WITHIN-CAP, the prose says
"the rows at 3 and 5 ended at their declared windows and are published as
capped, never as empty", the head fence says "CAPPED ROWS ARE PUBLISHED
AS CAPPED AND NEVER AS EMPTY", and the successor register names the
question undecided; the receipt's empty `achievable_budgets` follows
NDEP's committed field convention (found-within-the-declared-procedure).
The defect is the table presentation only, and the fix is now mandatory
rather than cosmetic: retitle the column (e.g. "found within the declared
window") or stamp the two cells, since the literal cells are now known
false.  No measured number of the unit's moves.

## 4. Reviewer closures beyond the unit's scope

**B1 (three of the four capped ladder rows closed: ACHIEVABLE).**  I
enumerated the FULL saturating pools at the capped arities (each pool
count equal to my DP's census, cross-validating the enumerators),
deduplicated cell masks, and ran the exhaustive 4-mask exact cover:

| a | full pool | distinct cell masks | full-pool R=4 cover | witness |
|---|---|---|---|---|
| 3 | 436,992 | 83,664 | EXISTS | exhibited, re-verified |
| 5 | 374,784 | 96,336 | EXISTS | exhibited, re-verified |
| 7 | 15,552 | 8,928 | EXISTS | exhibited, re-verified |
| 6 | 180,264 | — | still computing at freeze | — |

Each witness was verified explicitly (correct block sizes with the idle
remainder, mass 16 per round, pairwise-disjoint cell masks, full 64-cell
cover; rounds printed in scratch `a16_k1b/`).  So budgets {4, 8} exist at
a = 3, 5 and 7: three of the successor register's four undecided ladder
rows close as ACHIEVABLE, and the first rung at every closed row is
4 = L at rows with a != L — mod-a is absent at all three, so each closure
CONFIRMS the mod-a-iff-a=L half at rows the unit could not reach.  The
modulus theorem survived three live falsification chances it never faced
in the unit.  The a = 6 decision was still computing when this review
froze and remains with the successor.  The unit's published rows are
correct as published under their own stamps: NOT-WITHIN-CAP is a window
verdict, and my sample-level rebuild confirms no witness exists inside
its declared 4000-round canonical windows at any of 3, 5, 6, 7 — no two
window masks are even pairwise disjoint, which also explains the
receipt's 4001-node counts exactly (but see F5 for the table cell the
closures now expose).

**B2.**  NDEP's committed n=16 window census (256 / 24 / 1,240 / 505,920 /
0 / 49,536 / 29,760 / 24 / 24 / 4) now stands reproduced by a THIRD
independent implementation.

**B3.**  The schedule witness (4,82) shown to be the first minimal pair in
canonical order, with the attainment count (4,104 of 65,536) measured.

## 5. Recomputation count

| block | comparisons |
|---|---|
| file digests (7) + path anchors (54) + verbatim needles (13) | 74 |
| arena, lattices, conditional | 22 |
| windows / corpus table | 30 |
| fidelity rows | 10 |
| substrate (a=2..5 full + a=1..16 census columns) | 70 |
| naming census | 20 |
| floors (certificates, refusals, witnesses both ways) | 58 |
| schedules | 13 |
| menu / survivors | 17 |
| ladder (pools, statuses, witnesses, caps, R=8) | 39 |
| modulus sweep + instance | 322 |
| forcing census | 30 |
| SEC-2 | 36 |
| principle census (96 cells + selectors + parent column) | 110 |
| transport (words, rules, aggregates, controls) | 111 |
| text/artifact consistency (fences, evidence identity, totals, numeral sweep) | 34 |
| **total** | **996, zero discrepancies** |

(Counting convention: one comparison per claimed-vs-rebuilt value or
verified predicate; the 320 modulus-identity pairs counted individually as
the parent's sweep does.  Excluding them: 676 substantive comparisons.
The paper's every numeral above 20 was additionally swept against the
rebuilt set; the only residuals are digest fragments and the quoted
registration lists.)

## 6. Summary

The operator seat rebuilt every load-bearing number of ARITY-16 from
scratch — arena, lattices, substrate, windows, all six laws, the principle
census, the conditional, and both transport tables — in independent code
with exact arithmetic, and found the unit numerically flawless: 996
recomputations, zero discrepancies, with the unit's own published
witnesses (floor signature tables, ladder covers) independently valid, its
receipt, transcript and paper mutually consistent, and its two headline
splits (the reading-dependent conditional; saturation-is-maximality
deserting the field order for the characteristic) confirmed cell-for-cell.
The five findings are two evidence-alignment minors — the a=8 "refuses
every cover" sentence and the "blind across the fork" sentence are both
TRUE (I verified each exhaustively) but outran the unit's own instrument,
which searched only R=4 covers and swept the fork only at singles — and
three presentation minors ("the parent's constant 1"; the compressed
closed-form clause in the transport fence; and the section-8 "achievable
... none" cells at a=3/5, whose literal reading this seat's full-pool
closures now prove false while every guarded stamp around them stays
true).  Beyond the review, this seat closed three of the register's four
undecided ladder rows — full-pool R=4 covers EXIST at a = 3, 5 and 7,
every rung again 4 = L at rows with a != L, three fresh confirmations of
mod-a-iff-a=L.  No measured number needs repair, so the verdict is
ACCEPT-WITH-FIXES: align the two instrument legs with their sentences,
touch the three presentations, and the unit stands.
