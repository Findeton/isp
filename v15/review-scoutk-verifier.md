# SCOUT-K — SINGLE HOSTILE VERIFIER SEAT (FROZEN)

**Seat:** the pin's one hostile verifier (operator + effectus + instrument
combined), v15 ledger #75.  **Unit under review** (committed #74, digests
re-verified at the bytes this review read): v15/note-scoutk.md
573cb2c55e5c; v15/code/scoutk_exact.py 38c3f6cb288e;
v15/code/scoutk_output.txt c37cbd977d57; v15/code/scoutk_receipt.json
5af53face093; parent snapshot v15/code/scoutk_parent_delivered.py
edb60bccd22e.  Pin a1a6ccc61bd4 + #68 addendum 3a1e5a649537 (both
digest-confirmed on disk), parent binding LOG #58/#59.  No unit file was
modified; this review file is the seat's only repo write.  All hostile
work ran in a git-less mirror under the session scratchpad
(`scoutk_verify/`), independent rebuild in `scoutk_verify/work/rebuild.py`
(own arena, own group filtered from all 432 affine maps, own walk typed
from the parent snapshot's declared law, own orbit machinery by
full-orbit-set union — not the unit's min-canonicalization — own
Bland-rule phase-1 simplex with dual extraction, own Farkas checks; the
unit's receipt was read only to COMPARE numbers, never to compute them).

## VERDICT: ACCEPT-WITH-FIXES

Every measured number in the unit reproduces from a fully independent
instrument — 104/104 rebuild checks, zero discrepancies, including all
18 sampled Farkas gaps byte-exact, all 3 branchwise gaps, all 4
identified-run gaps, all 3 published uniform certificates verified
entrywise against MY constraint matrices, both controls, and every
census count.  The depth-3 emptiness is real at every arm and at the
global reading, the uniform affine-endpoint argument is logically sound,
and the mechanism witness stands.  The fixes are compliance-side: the
#68 addendum is nowhere cited or digest-pinned by the unit, no verdict
names its consistency mode, the G-fixed scope-wall sentence is missing,
and the note-verifier's numeral sweep shields every numeral <= 60 behind
a blanket whitelist.  None of these can move a number.

## 1. OPERATOR — recomputation ledger (all from scratch)

Instrument: `rebuild.py`, exact rationals throughout, 104 check lines
comprising ~230 recomputed quantities.  **Zero discrepancies.**

| block | rebuilt independently | result |
|---|---|---|
| arena | 27 cells/bijection, 84 triples, 27 triangles, 9-of-12 declared lines, cell-in-3-blocks | MATCH |
| group | order 108 by an independent filter (all 432 affine maps, keep pair-set preservers), triangle closure, cell stabilizer order 4, stabilizer orbits [1,2] on incident blocks, exactly one incident line fixed, non-lines swapped | MATCH |
| walk | q1 = (1/9, 4/9, 4/9) on cells 0,1,2; q2 support {3,4,5,9,10,11,12,13,14}, unit mass; own Z[w] arithmetic | MATCH |
| blindness | 11 variants, one second-step Born vector; single-link mechanism | MATCH |
| reach | 63 contexts / 189 tuples / 7 first events | MATCH |
| orbits (the heart) | own machinery (orbit sets under all 108 g, union-partition): depth-3 variables 16/16/25/19/25; context classes 6/6/9/7/9; depth-1 = 2 per arm; shared-with-depth-1 = 2/2/0/2/0 | MATCH |
| coincidences | SA==RD and MC==GLOBAL partitions byte-identical as index partitions of the 189 raw tuples; CN distinct from both; **stronger: GLOBAL refines CN refines SA in the refinement order** (the unit measured only inequality) | MATCH+ |
| arm covariance | **all 108 elements x all 8 reached records** (the unit sampled one written record) | HOLDS (stronger) |
| step 1 | 2 orbit variables; the two non-line incident blocks of one trigger lie in ONE orbit — covariance forces equal values, so a deterministic covariant kernel must be (1,0,0) on (line, non-line, non-line): a = 1 is the only deterministic member; the stabilizer-swap argument VERIFIED | MATCH |
| depth 2 | consistency rows vacuous under measured blindness; family = {a + 2b = 1, a,b >= 0}, dim 1 | MATCH |
| depth 3 sampled | all 3 systems x 6 line weights: INFEASIBLE with my OWN Farkas certificates; gap AND deduplicated row count byte-equal to the receipt at all 18 (e.g. SA-RD a=0: 40907/4860 at 89 rows; MC-GLOBAL a=1: 2648/243 at 83 rows) | MATCH x18 |
| branchwise | own systems, own certificates; gaps 22835/1701 (119 rows), 53755/3402 (141), 1598/81 (168) | MATCH x3 |
| uniform certificates | published y-vectors mapped onto MY (A0, A1, b) triples via row_meta; y.A0 <= 0 and y.(A0+A1) <= 0 columnwise, y.b = 1, supports 6/6/7, trip row counts 115/116/118 | VERIFIED ENTRYWISE x3 |
| affine-endpoint logic | audited, sound: every rhs is a-free by construction, every row is affine in a, so y.A(a) is the convex combination of the two verified endpoint inequalities for a in [0,1] and y.b = 1 > 0 refuses EVERY line weight — one certificate genuinely covers the whole segment; the certificate needs no y <= 1 leg | SOUND |
| relaxation lemma | audited, sound: the identified (physically honest) family pins the two empty-pattern orbit variables to the step-1 values, i.e. ADDS rows, so identified solutions solve the relaxed system; relaxed emptiness uniform in a covers the true family; used in the emptiness direction only, so it is conservative and is NOT the addendum-refused history-flow relaxation | SOUND |
| identified runs | 1 empty line + 1 empty non-line orbit at SA-RD and CN; 4 pinned runs INFEASIBLE own-certified, gaps 205192925/16121106, 386831585/30236004, 2924765939/217475280, 101215751/7459128 | MATCH x4 |
| mechanism witness | rows (0,5,14) and (1,11,21) of MC-GLOBAL at a=0: identical covariant coefficient vectors rebuilt; walk masses 16/729 vs 64/729; **also verified it is the FIRST clash in canonical row order** | MATCH |
| fixed-alpha subfamily | 729 rows, 25 distinct nonzero polys, linear roots {-1, 0, +1}, alpha probes 0, 1/3, 1 all fail; orbit-route poly set equals the direct parent-style set; line-ness constant on every orbit at all three systems | MATCH |
| pure census | 8 surviving all-non-line first-step combos extending to 288 pure kernels | MATCH |
| controls | kernel-generated target FEASIBLE with nonnegative witness; shifted target INFEASIBLE at 433415665/29073978, own-certified | MATCH |

Verdict transfer soundness (checked, not assumed): the LP depends on the
orbit partition alone (variables enter only through tuple
identification), so byte-identical partitions carry SA-RD and MC-GLOBAL
exactly; gap values are invariant under my independent variable
indexing, and they still matched byte-for-byte.

## 2. EFFECTUS — compliance audit

**Honest parent scope (#59):** the required sentence is present verbatim
and gated; the parent result is cited nowhere except in its licensed
record-blind fixed-alpha form.  PASS.

**The new verdict's own scope:** hunted every scope-bearing sentence.
The generalization claim carries "at the three-step window, at any
declared proximity arm, at any first-step line weight" — no sentence
claims all depths, sub-normalized kernels, or rejects trigger semantics
as such; depth-4, leaky kernels, trilemma arms (b)/(c) and transport are
registered successors; the candidate-bridge wall and the
event-selection-only scope sentence are present and gated.  PASS.

**Trigger candidate-marking:** maintained (term table, wall, BRIDGE
verdict, kit).  PASS.

**Conditional consistency mode (#68 item 1):** the code was audited —
at fixed first-step weight every constraint is linear in exactly ONE
kernel factor (the second-invocation orbit variable), the first factor
being the step-1 family swept exactly and closed by the uniform
certificate; no bilinear system is solved and no history-flow linear
relaxation is outcome-bearing (the relaxed system is used in the
conservative emptiness direction only, with pinned confirmations).  The
MODE IS the frozen PRIMARY — but see F1: no verdict NAMES it.

**Numeral totality (#68 item 5), measured:** 156 integer numeral
occurrences in the note; 151 resolve against receipt-backed values or
the 23-row binding table (all 23 rows resolve to their claimed values —
re-verified); 5 pass ONLY through the verifier's hard-coded whitelist
(#58, #59, #60 ledger references, "24 gates", seed 424242 — all five
true).  See F3 for the blanket problem.

## 3. INSTRUMENT — injections (git-less mirror, absolute scratchpad path)

Baseline first: with BOTH artifacts deleted, delivery at an alien CWD
under PYTHONHASHSEED=7 regenerated output AND receipt byte-identical to
committed (c37cbd977d57 / 5af53face093) — the #59 root cause is closed
on the real bytes.  Live selftest: 23/23 falsifiers died at their
declared gates with move proofs, artifacts untouched (digests compared
before/after).

| # | injection | expected | observed | tree |
|---|---|---|---|---|
| I1 | forge a Farkas y-vector entry (live, unconditional) | die G-D3-FARKAS | rc 3, GATE FAILURE G-D3-FARKAS | INTACT |
| I2 | forge orbit count SA 16 -> 15 in the census data | die G-REACH | rc 3, G-REACH | INTACT |
| I3 | flip EMPTY -> NONVACUOUS (force FEASIBLE at CN a=1/2) | die G-D3-SAMPLES | rc 3, G-D3-SAMPLES | INTACT |
| I4 | puncture N_recdist (break SA==RD) | die at first RD gate | rc 3, G-ARMS-COVARIANT | INTACT |
| I4b | covariant predicate swap RD := N_causal | die at arm-size leg | rc 3, G-ARMS-COVARIANT | INTACT |
| I5 | corrupt the parent snapshot (append) | die at ITS pin gate | rc 3, G-PIN-DIGESTS | INTACT |
| I6 | forge mechanism-witness mass 16/729 -> 17/729 | die G-CLASH | rc 3, G-CLASH | INTACT |
| I7 | plant the retired overclaim VERBATIM + ontology sentence in the note | die G-NOTE-KIT | rc 3, G-NOTE-KIT | INTACT |
| I8 | record the live LOG digest into the receipt | no in-run gate (registered hazard) | rc 0, receipt MOVED; a one-line LOG append then moved the receipt AGAIN — the #59 disease reproduces exactly; caught only at the battery's committed-byte compare | mirror only |
| I9 | seed-variant variable ordering (string-hash sort of RAW) | no in-run gate (registered) | rc 0 at seeds 1 and 2, receipts DIFFER across seeds (5d43f93a23ae vs 8cdb9c1c3d5d); in-run double-build passes (same-seed); caught only at the battery's multi-seed leg | mirror only |
| I10 | registry MUT-GAMMA | die G-GAMMA | rc 3, died at G-GAMMA | INTACT |
| I11 | registry MUT-REACH | die G-REACH | rc 3, died at G-REACH | INTACT |
| I12 | registry MUT-UNIF | die G-D3-UNIFORM | rc 3, died at G-D3-UNIFORM | INTACT |
| I13 | --selftest write-nothing | rc 0, artifacts untouched | rc 0, 23/23 with move proofs, digests unchanged | INTACT |
| I14 | hostile argv x5: --frobnicate / --mutant / --mutant BOGUS / --no-write --kit / --verify-paper | rc 2 each, nothing written | rc 2 all five, artifacts unmoved | INTACT |

Paraphrase plants (mirror note copies through --verify-paper):

| plant | species | outcome | classification |
|---|---|---|---|
| P1 | kernel-family nonexistence, fresh words ("no equivariant kernel of any kind survives") | SURVIVED | registered fresh-paraphrase condition (#46/#61); cure exists — see F2 |
| P2 | covariance-dead-as-such + all depths | SURVIVED | registered |
| P3 | walk-is-wrong-as-fact | SURVIVED | registered |
| P4 | ontology-deciding ("records do not backreact in nature") | SURVIVED | registered |
| P5 | hyphen-fused retired overclaim ("no-equivariant-record-consistent-kernel-exists") | SURVIVED | registered species; the #78 sibling repair kills exactly this — see F2 |
| P6 | heading-fused licence ("## ... [LIC:G-D3-FARKAS]") | SURVIVED | registered (heading-fused escapes, in-process) |
| P7 | ", being gated," launder + all-depths overreach | SURVIVED | registered (licence-token laundering) |
| P8 | trigger-mechanism-confirmed paraphrase | SURVIVED | registered |

Zero NEW wall-gap species: the #73 F1 replant (verbatim retired
overclaim) now DIES here (I7), which is the one that was NEW last time.
All survivors are the registered syntactic-wall condition.

## 4. Findings

**F1 — MODERATE (compliance).  The #68 addendum is unbound in the
unit.**  The frozen addendum 3a1e5a649537 amends the pin, and LOG #74
says the unit was built under it — but the note cites only "the #64
binding addendum", the PINNED registry carries pin + parent snapshot +
paper-20 and NOT the addendum file, and neither artifact mentions #68 or
its digest.  Two of its textual requirements are unmet: (a) item 1's
"Every verdict names its mode" — no verdict string names CONDITIONAL
(the construction verifiably IS the frozen PRIMARY mode, so this is
naming, not substance); (b) item 4's scope wall — the
event-selection-only sentence is present and gated, but the "G is FIXED
throughout / record backreaction only" sentence appears nowhere in the
note.  Items 2 and 3 are substantively satisfied (predicates declared in
committed objects and measured covariant; the four first-event
requirements all present).  Fix: pin the addendum digest, cite #68 in
the note header, suffix the D3 verdict with its mode, add the gated
G-fixed sentence.  No number moves.

**F2 — MINOR (wall gap with an available cure).**  The retired
overclaim dies verbatim, but its hyphen-fused variant (P5) and
fresh-worded kernel-family nonexistence (P1) survive the note verifier.
The parent scout's #78 micro-repair built exactly the missing wall
(G-KERNEL-WALL: hyphen/spacing-normalized, subject-based, licensed
twins alive).  Fix: port it.

**F3 — MINOR (numeral-totality blanket).**  The note verifier's final
sweep whitelists every integer 0..60 plus 17 hard-coded larger
constants: any FALSE numeral <= 60 outside the 23-row binding table
would pass unopposed — the #59 enabling pattern in residual form.
Today's exposure is nil (all 156 occurrences verified true by this
seat), and the 23 load-bearing bindings all resolve; but #68 item 5
asks for a per-occurrence BOUND/NON-CLAIM classification with reason
classes, and range(0,61) is not a reason class.  Fix: classify the 5
blanket-only occurrences (three ledger references, the gate count, the
seed) and shrink the blanket.

**F4 — NOTE (registered).**  I8/I9 confirm the unit has no IN-RUN
defense against environment-digest or seed-variant mutations; the
battery layer (committed-byte compare, multi-seed) is load-bearing, as
designed after #59.  This seat re-ran that layer live: regeneration
from deleted artifacts at an alien CWD and alien seed is byte-identical,
selftest is write-nothing.  No action.

**F5 — NOTE.**  "Predicates digest-sealed BEFORE any feasibility row
runs" (#68 item 2) is evidenced in-repo only by the single frozen source
digest plus in-run gate order (G-ARMS-COVARIANT precedes every D3
gate); a stronger seal-order proof does not exist and cannot be
reconstructed after the fact.  Consistent with the pin; unverifiable
beyond that.

**F6 — NOTE.**  "no caps were needed anywhere in the chain (no capped
rows exist)" (note §0) is backed by no receipt field.  True as far as
this seat can see (no cap machinery exists in the code), but it is an
unbound negative claim; bind it or drop it.

**Strengthenings found (free of charge):** arm covariance holds at all
108 elements x all 8 reached records (the unit sampled one); the CN
partition sits strictly between in the refinement ORDER (GLOBAL refines
CN refines SA), sharpening "strictly between"; the clash witness pair
is the first clash in canonical row order, so the witness is canonical,
not curated.

## 5. Summary (one paragraph)

The verdict SCOUTK-COVARIANT-EMPTY-AT-3 at every arm including GLOBAL
survives a full hostile rebuild: an independent instrument with its own
arena, group, walk, orbit machinery and simplex reproduced every
committed number byte-for-byte — 104/104 checks, ~230 recomputed
quantities, all 18 sampled gaps, all 3 branchwise gaps, all 4 identified
gaps, the 63/189/7 reach census, the 16/16/25/19/25 orbit dimensions,
the SA==RD and MC==GLOBAL partition coincidences, the 2-variable step-1
collapse with the stabilizer-swap argument, the 729/25/{-1,0,1}
fixed-alpha reproduction, the 8-to-288 pure census, and the 16/729 vs
64/729 mechanism witness — while the three published uniform Farkas
certificates verify entrywise against the rebuilt matrices and the
affine-endpoint argument is sound, so the emptiness genuinely closes the
whole line-weight segment and the trigger-kernel bridge is dead in its
locally covariant record-dependent class at the committed windows.
Eighteen live injections all died at their declared gates or at the
battery layer exactly as the design says they should, with the tree
intact throughout.  The fixes are real but bloodless: bind and obey the
#68 addendum's naming requirements (F1), port the #78 kernel wall (F2),
and retire the numeral blanket (F3).  ACCEPT-WITH-FIXES; no false
number was found anywhere in the unit.
