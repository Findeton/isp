# SCOUT-BRIDGE — THE SINGLE HOSTILE VERIFIER SEAT (FROZEN)

**Seat:** the pin's promised one verifier seat (v15/note-scout-pin.md,
review plan: orchestrator battery + ONE hostile verifier seat), combining
operator, effectus, and instrument duties at scout scale.  Launched at
ledger #67 on the repaired blob committed at #66.
**Object under review:** v15/note-scout-bridge.md 57177f5bb9b9;
v15/code/scout_exact.py 63bf34c9df62; v15/code/scout_output.txt
04fe8f67f75b; v15/code/scout_receipt.json 9fd9029516f2; snapshots
scout_ecc_paper46_delivered.md 61d330d13fe0 /
scout_ecc_receipt_delivered.json ea24c1fc2340; pin c57a0afffd58 +
addendum 2aa72e566cba.  All eight sha256-12 digests verified against the
working tree and against HEAD/commit-#66 bytes before any other work.
**Discipline:** no unit file was modified; this review file is the seat's
only repository write.  All hostile work ran in git-less rsync mirrors
under the seat's scratchpad; every injection is logged below with
expected gate / observed / tree-intact.

## VERDICT: ACCEPT-WITH-FIXES

Zero false numbers.  Zero gate failures on the committed blob.  The
repaired language complies with the #59 downgrade and the #64
candidate-marking everywhere I probed, including the receipt's outcome
words.  The two new gates (G-NUMERAL-FIELD, G-ENV-EXCLUSION) have real
teeth, proven in both directions.  The fixes owed are wall-side, not
physics-side: the retired kernel-overclaim sentence can be planted back
verbatim and no wall fires (F1); the iteration-order disease registered
at #62 has no in-instrument catcher, only the battery leg (F2); one
primitive-selection table cell quantifies wider than the census it cites
(F3).  No measured number moved anywhere.

## THE RECOMPUTATION LEDGER (operator charge)

All rebuilt in the seat's own exact-arithmetic code (fresh
implementation: own arena constructors, own Z[w] and Q(w) arithmetic,
own rref/rank, own two-phase simplex with phase-one dual extraction),
compared against the committed receipt and note.  121 check-lines
covering ~280 individually compared quantities; **zero discrepancies**.

1. **Arena** (12 quantities): 27 cells with pair bijection, 84 triples,
   27 triangles, writer census (0,3)(2,54)(3,27), 9 declared lines, 12
   cosets, 280 partitions, 36 admissible rounds, every cell in exactly
   3 blocks / 1 declared line / 7 triples.  All equal.
2. **Committed row** (20): q = (1/9, 4/9, 4/9) on cells 0,1,2 rebuilt
   from the walk; all four classes INFEASIBLE with my own phase-one gaps
   4 | 4 | 3 | 7/3; my own Farkas certificates built and verified
   (y.A <= 0 columnwise, y <= 1, y.b = gap); **and the receipt's four
   stored dual vectors verified entrywise against MY OWN incidence
   rebuild** — all four valid at the delivered gaps.  E-TRIPLE solved on
   the full 84-column system.
3. **The 156-row census** (156 + 6 aggregates): every row recomputed by
   my own solver — not a spot check; the full census — including **all 8
   UNIQUE and all 6 MANY rows with the MANY dimension 8 rebuilt
   independently** (relative-interior support growth + rank, not the
   unit's implicit-zero routine); E-TRIPLE rows solved on the full
   84-column system, independent of the unit's deficient-writer
   shortcut, and the shortcut's answers confirmed (dim 8 at E-TRIPLE
   MANY rows too).  156/156 word agreement; 82 target rows, 2 undefined,
   39 distinct targets, ceiling exceptions 0.
4. **S1** (26): pushforward instance (total 1, 9 distinct events,
   occupancy marginal max 1/3, sum 3); scaffold escape (a): joint total
   1, trigger readout = q byte for byte, **7 successors** pairwise
   distinct, inclusion marginal NOT 3q with max 17/27; escape (b) 9
   endpoint pairs; escape (c) class split with ranks (19,20), (9,10),
   (10,11) — augmented rank exceeds by exactly one at each refused
   class — and my own E-TRIPLE signed witness with min entry -2/3;
   escape (d) infeasible at lambda = 1/3, 1/2, 2/3.
5. **S2** (31): group order 108 = 12 x 9 with block closure; orbits
   [27] / [9,18] / [27,54]; cell stabilizer order 4 with incident-block
   orbits [1,2]; **dim 54 -> 1 under equivariance** (81 variables, bare
   nullity 54; two pair orbits, constraint rank 1); **arm-2 EMPTY at
   exact gap 6** with my own verified Farkas certificate on the 54-row,
   81-column system; depth-2 vacuity (11 variants byte-equal,
   single-link mechanism confirmed); **depth-3: 729 rows, 25 distinct
   nonzero polynomials, linear roots exactly {-1, 0, 1}, alpha probes
   0, 1/3, 1 all refused, 8 pure non-line first-step survivors
   extending to 288 pure kernels — the survivor count rebuilt
   independently**; 351 successor pairs, 0 record collisions.
6. **S3** (18): the silence lemma at 4 probed records both sides (pin
   asked >= 2); the committed row's three cuts all zero; the
   permutation countercontrol (qmax 1, LP infeasible with ceiling
   witness, Delta-B exactly zero at every cut); the F3,F3
   countercontrol (**81 nonzero Delta-B entries**, uniform intermediate
   at the cap 1/3, all four class rows infeasible with no ceiling
   witness); two-step step-cut composites zero at R0 / HIT-1 / ROUND-0;
   predictor score 20 of 156.
7. **S4** (4): the closed form -(1/4)(w_c(rho0)-w_c(rho1))(P0-P1)
   verified **entry by entry over Q(omega) at all 27 branch cells x
   27x27 entries, both sides built independently**; the witness at
   branch cell 0, entry (4,4), value 1/36 + 0.w (also re-derived by
   hand: dw = -1/3, (P0-P1)[4][4] = 1/3); joint weights sum 1, records
   pairwise distinct.
8. **Receipt-integrity spot checks**: object_under_test digest = note
   digest; source_hygiene digest = code digest; 182 sample-space
   declarations counted independently; falsifiers 29, gates 37 as
   printed.

One rebuild convention difference surfaced and was resolved against the
seat, not the unit (finding F5 below).

## EFFECTUS (the repaired language)

**(a) Downgrade compliance.**  Grep-hunted all four files plus both
snapshots for the retired forms: "SCOUT-KERNEL-EMPTY-AT-EQUIVARIANT-
RECORD-CONSISTENT" and every "no equivariant record-consistent kernel"
variant — absent everywhere.  Every kernel-emptiness verdict site
carries the record-blind fixed-alpha scope: the note's head words
(note:90), the determination block (note:263-283), the engraved scope
paragraph (note:261), the receipt's s2_determination/word,
s2_arm_c_depth3/word and kernel_family_scope, and the output's gate
lines.  s2_arm_b/word ("EMPTY-AT-ALL-WRITE-ONE-MEASURED") is arm-scoped,
which is correct: arm two is a one-step system at fixed R0, where record
dependence is inert.  The depth-2 "for every kernel" sentence (note:253)
is a theorem at that window, not an overclaim.  SCOUT-K is named at
every open site I checked (note:77, 90, 215, 261, 269, 281, 410, 412,
426, 435).

**(b) Candidate-marking.**  The trigger reading is candidate-marked
exactly once and load-bearingly (note:157, mirrored at
receipt s1_escape_a/trigger_semantics_status): "a CANDIDATE -- not an
established physical mechanism"; no other trigger sentence asserts the
mechanism (all 18 trigger lines audited).  The primitive carries
ADOPTED-BY-PROGRAM-DECISION (note:404;
receipt primitive_selection/adoption_status).  The S4 fork is in the #64
sharpened form — linear-over-ontic-psi, nonlinearity only in the
compressed rho description, the rho-complete-vs-incomplete dichotomy —
with SCOUT-PSI named as the running test (note:368-372;
receipt s4_linearity/ontology_qualification, completeness_dichotomy).

**(c) The 27->7 correction** is disclosed as ordered, twice: at the
point of use (note:171-177) and as deviation 7 with the enabling disease
and the structural repair named (note:516-525).

**(d) The sample-space spine.**  182 declarations counted; every 10th
declaration sampled (19 samples) and type-checked against its object:
census rows and duals TRIPLE-EVENTS, committed_q CELLS, scaled escape-d
rows TRIPLE-EVENTS, s4_joint COMPLETE-SUCCESSOR-CONFIGURATIONS — all
correct; zero invalid names.  The S3 section is clean of
probably/likely/explains.

**(e) The walls, attacked with 16 plants** (mirror copies only; the
committed note was never touched).  See the plant table.  Seven
registered walls fired exactly as declared; nine fresh paraphrases
survived.  Classification: eight survivors are the REGISTERED
fresh-paraphrase condition (engraved at #46 and at full strength at
#61 — syntactic walls do not catch semantics); one survivor is NEW
(finding F1: the retired overclaim replants verbatim).

## FINDINGS

**F1 — MODERATE, NEW.  The retired kernel overclaim can be planted back
verbatim and no wall fires.**  Plant P14 ("So no equivariant
record-consistent kernel exists at the committed arena.") added to a
mirror copy of the note passes --verify-paper rc 0.  FORBIDDEN_GLOBAL
(scout_exact.py:2547-2553) contains no kernel-scope pattern, although
the era's practice is to engrave retired claims as forbidden strings
(the list already carries retired diseases).  The #59/#66 repair made
the four files grep-clean but installed no defense against
re-insertion.  Fix: add "equivariant record-consistent kernel" (and the
retired verdict token) to FORBIDDEN_GLOBAL, or an equivalent scoped
scan.

**F2 — MINOR, REGISTERED SPECIES / NEW ABSENCE.  Iteration-order
nondeterminism has no in-instrument catcher.**  Injection INJ-9: a
mirror whose measure_reads iterates its read set unsorted (two-line
mutation) delivers rc 0 at PYTHONHASHSEED 0, 1, 2 and writes
**seed-variant receipts** (sha256-16 7c733fbbf59e2e6f /
65648927480f32f4 / 9a069a075e724beb) — it varies silently; the
in-process double build shares the seed and cannot see it, and
G-SRC-CLEAN's AST scan (floats, hash, imports) does not scan iteration
discipline.  The catcher is solely the orchestrator battery's
cross-seed regeneration leg (which is also what caught #59's defect).
The species is the one registered at #62 (ARITY-16 K3); the scout pin
froze at #53 and did not owe this wall, so this is filed as an absence,
not a violation.  Fix option: extend the AST scan to flag unsorted
iteration over set displays/comprehensions, or engrave the battery leg
as the designated catcher in the note's instrument section.

**F3 — MINOR.  One primitive-selection cell quantifies wider than its
census.**  note-scout-bridge.md:410 (CRIT-C, mirrored at
receipt primitive_selection/criteria/CRIT-C-walk-preservation): "at the
three-step window only the 288 pure non-line kernels preserve it" — read
literally this quantifies over all kernels, while deviation 3
(note:500-504) states mixed kernels at that window are undecided and the
record-dependent family is SCOUT-K's open question.  The same cell's
next clause and the answer paragraph (note:423-427) carry the correct
scope, so this is a wording ambiguity, not a false claim.  Fix: "only
the 288 pure non-line kernels among the censused deterministic
kernels."

**F4 — NOTE (registered).**  Fresh paraphrases of all five forbidden
claims survive the walls (plants P1-P7, P9b): the general kernel no-go
in fresh words, trigger-as-mechanism, psi-is-ontic asserted,
rho-is-incomplete asserted, Delta-B-"accounts for", the divisibility
determiner-shift, the single-time paraphrase, and a fresh NEG-guard.
This is the REGISTERED condition (#46, #61) and is reported here as its
scout-scale confirmation, not a new disease.  The HYPHEN-EVASION
species (#61) is caught only when the coinage still contains a
registered substring (P8 died; P6's determiner shift walked past —
same registered condition).

**F5 — OBSERVATION, resolved against the seat.**  The census word
UNIQUE at the two fiber rows (THE-UNIFORM-AMPLITUDE, ROUND-27 and
ROUND-30, G.D, class E-LINE-DECLARED) means affine-unique: the equality
system has trivial nullspace (rank 9 = columns), so the one solution is
the unique feasible point, prim row or not.  My first-pass rebuild used
the coarser fiber word there and mismatched 154/156; adopting the
mathematically stronger (and correct, ECC-consistent) convention gives
156/156.  No error in the unit; recorded so the convention is on the
record.

## THE PLANT TABLE (all in mirror copies; --verify-paper per plant)

| plant | content (fresh unless marked verbatim) | expected | observed |
|---|---|---|---|
| P1 | general kernel no-go, fresh words | survive (registered) | SURVIVED |
| P2 | cells-do-trigger as mechanism | survive (registered) | SURVIVED |
| P3 | psi-is-ontic asserted | survive (registered) | SURVIVED |
| P4 | rho-is-incomplete asserted | survive (registered) | SURVIVED |
| P5 | Delta-B "accounts for" the excess (S3) | survive (registered) | SURVIVED |
| P6 | "one divisibility-measure" (hyphen + determiner shift) | survive (registered) | SURVIVED |
| P7 | "no distributions at single times" paraphrase | survive (registered) | SURVIVED |
| P8 | "is a divisibility-detecting" (substring control) | DIE | DIED: forbidden pattern "delta-b is a divisibility" |
| P9 | "No reader will doubt..." NEG-guard verbatim | DIE | DIED: forbidden pattern "no reader will" |
| P9b | "Nobody could doubt..." NEG-guard fresh | survive (registered) | SURVIVED |
| P10 | slash-rational 5/7 in prose | DIE | DIED: not in receipt inventory |
| P11 | ", being gated," | DIE | DIED: forbidden pattern |
| P12 | bare-subject derivation sentence | DIE | DIED: derivation without subject tag |
| P13 | [LIC:G-BOGUS] | DIE | DIED: licence names no registered gate |
| P14 | the OLD OVERCLAIM verbatim | should die | **SURVIVED — finding F1 (NEW)** |
| P15 | "probably" inside S3 | DIE | DIED: S3 language wall |

## THE INJECTION TABLE (git-less rsync mirrors; tree hash checked)

| # | injection | expected | observed | tree |
|---|---|---|---|---|
| INJ-0 | delete both artifacts, regenerate (seed 7) | byte-identical | output AND receipt byte-identical to committed | intact |
| INJ-1 | **append synthetic entry to mirror LOG.md, regenerate** (root-cause probe) | byte-identical | receipt AND output byte-identical — the #59 defect provably closed | intact |
| INJ-2 | MUT-ENV: live-LOG digest into receipt payload | G-ENV-EXCLUSION | died at G-ENV-EXCLUSION, rc 3 | intact |
| INJ-3 | MUT-NUMBIND: field-side 7->27 | G-NUMERAL-FIELD | died at G-NUMERAL-FIELD, rc 3 | intact |
| INJ-4 | prose-side 7->27 in note copy | note verification | died rc 3: "numeral-field context missing (s1_escape_a/successors = 7)" — and 27 IS receipt-backed elsewhere, so the old any-occurrence wall would have passed it; the new gate's teeth confirmed. (First sed attempt failed to land across the line wrap — detected by byte-compare, re-landed with multiline edit; logged for honesty) | intact |
| INJ-5 | MUT-GAP: forge a committed gap | G-COMMITTED-ROW | died at G-COMMITTED-ROW, rc 3 | intact |
| INJ-6 | MUT-CERT: corrupt a Farkas certificate | G-FARKAS | died at G-FARKAS, rc 3 | intact |
| INJ-7 | flip S1 escape name back to the old wrong one | note verification | died rc 3: kit sentence missing (the TRIGGER-MARGINAL verdict) | intact |
| INJ-8 | = plant P14, old overclaim verbatim | a wall | **SURVIVED** -> F1 | intact |
| INJ-9 | seed-variance on set-iteration-mutated mirror | must die | **varied silently**: rc 0 x3 seeds, three distinct receipt digests; caught only by the seat's cross-seed byte comparison (the battery leg) -> F2 | mirror restored |
| INJ-10 | MUT-ARENA | G-ARENA | died at G-ARENA, rc 3 | intact |
| INJ-11 | MUT-SILENCE | G-S3-SILENCE | died at G-S3-SILENCE, rc 3 | intact |
| INJ-12 | MUT-CENSUS | G-CENSUS-REPRO | died at G-CENSUS-REPRO, rc 3 | intact |
| INJ-13 | --selftest write-nothing by WHOLE-TREE hash | rc 0, tree unchanged | 29/29 falsifiers died at declared gates with move proofs; whole-mirror find/sha256 hash identical before/after | intact |
| INJ-14 | hostile argv x6 (--frobnicate; --mutant; --mutant BOGUS; --selftest --kit; --verify-paper; extraword) | rc 2 each | rc 2 all six | intact |
| INJ-15 | corrupt one byte of the pinned ECC receipt snapshot | G-PIN-DIGESTS | died at G-PIN-DIGESTS, rc 3, nothing written | intact, snapshot restored |
| INJ-16 | pristine cross-seed regeneration (seeds 1, 42) | byte-identical | receipt AND output byte-identical both seeds | intact |

17 discrete injections + 16 plants = 33 hostile events; every
death-expected event died at its declared gate with the tree intact;
the two survivals are findings F1 and F2.

## SUMMARY (one paragraph)

The repaired SCOUT-BRIDGE unit survives a full hostile rebuild: ~280
quantities recomputed in the seat's own exact-arithmetic code — the
complete 156-row census with all UNIQUE/MANY words and the MANY
dimension 8, all four committed Farkas certificates verified both as
rebuilt and as delivered against an independent incidence, the S2
ladder 54->1 / gap-6 / 729-25-roots{-1,0,1} / 8->288 with the survivor
count rebuilt, the S3 all-zero data with both countercontrols killing
in opposite directions, the S4 closed-form witness entry-by-entry over
Q(omega), and the scaffold's 7 successors — with zero discrepancies and
zero false numbers; the #59 downgrade and #64 candidate-marking hold at
every probed site including the receipt's outcome words; the
numeral-field and env-exclusion gates kill in both directions; the
ledger-self-reference defect is byte-provably closed (regeneration
after an in-mirror LOG append is identical); the verdict is
ACCEPT-WITH-FIXES on three wall-side findings — the retired overclaim
replants verbatim unchallenged (F1, moderate), iteration-order
nondeterminism is caught only by the battery leg (F2, minor,
registered species), and one CRIT-C cell wants a three-word scope
qualifier (F3, minor) — none of which moves a measured number.

**FROZEN.  The seat's only repository write.  2026-08-17.**
