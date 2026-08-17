# SCOUT-K — the record-dependent, locally covariant kernel census (report note)

Status: CANDIDATE READINGS until the single hostile verifier seat and the
user read it.  Unit pinned at v15 ledger #60 (pin v15/note-scoutk-pin.md,
FROZEN sha256-12 a1a6ccc61bd4), with the #64 binding addendum folded
(trigger = candidate bridge; the first-event boundary; the
event-selection-only scope sentence), and with the #68 pin addendum
(v15/note-scoutk-pin-addendum.md, FROZEN sha256-12 3a1e5a649537) cited
by digest and CONSUMED by gate [LIC:G-ADDENDUM-68]: the CONDITIONAL
consistency mode named in the D3 verdict words, the pre-registered
proximity predicates, the separate step-1 census, the gated G-fixed
scope wall and the numeral totality are all checked in-run against what
ran.  Scout class: this note +
v15/code/scoutk_exact.py + v15/code/scoutk_output.txt +
v15/code/scoutk_receipt.json.  Exact arithmetic throughout; every
emptiness carries a Farkas certificate; the caps register records zero
engaged caps anywhere in the chain: every constraint row is typed at
its construction site and no capped row exists [LIC:G-CAPS-REGISTER].

## 0. The question and the honest parent scope

The pin's question, verbatim:

> Does any LOCAL, RECORD-DEPENDENT kernel K(e|c,G,R), equivariant in
> the true sense K(ge|gc,gG,gR)=K(e|c,G,R) under SIMULTANEOUS
> relabelling of all four slots, preserve the delivered walk statistics
> at exact multi-step consistency — or is the emptiness of #58's
> narrow family in fact general?

The parent result is cited only in its #59 honest scope, verbatim: the
honest parent scope is quoted and preserved: no record-blind,
fixed-alpha, affine-equivariant kernel preserves the delivered
three-step walk statistics.  The ninth review's reason the general
question was open, verbatim from the ledger:

> true equivariance K(ge|gc,gG,gR)=K(e|c,G,R) admits record-dependent
> kernels that distinguish candidate triples by their RELATION to the
> written record without privileging labels.

THE ANSWER THIS CENSUS DELIVERS: this census answers the general question the ninth review left open: the emptiness GENERALIZES -- no local, record-dependent, truly covariant kernel K(e|c,G,R) preserves the delivered walk statistics at the three-step window, at any declared proximity arm, at any first-step line weight, and not even at the global record reading [SS:TRIPLE-EVENTS]

THE PRECISE ESTABLISHED FORMULATION (#82, the thirteenth review's words, gated): at this arena, no normalized covariant conditional kernel K(e|c,G,R) with fixed geometry, the trigger factorization P(c,e) = q(c) K(e|c,G,R), and exact preservation of the delivered cell-walk's conditional statistics, works through window 3 -- even with the entire record; it does NOT kill the triple ontology, covariance, locality generally, kernels with additional state or history, changing geometry, non-trigger-factorized bridges, history-level indivisible processes, or agreement at the observable-history level only [SS:TRIPLE-EVENTS]

## 1. The terminology box (W4 term-binding table, E-34)

| term | binding |
|---|---|
| CELL-HIT | paper-20's primitive: one Born-selected pair-cell increment per step (the mandatory rename) |
| DIVISION-EVENT | paper-19's three-actor conflict group whose footprint writes all three pair-relations; the only object this note calls a division event |
| TRIPLE-EVENT | a division event carried as one probabilistic alternative |
| TRIGGER | the cell the quantum menu selects; the conditional seat of q(c) under the ADOPTED CANDIDATE bridge P(c,e|X) = q(c|X) K(e|c,G,R) -- a candidate this census tests, never an established physical mechanism |
| SUCCESSOR | a COMPLETE-SUCCESSOR-CONFIGURATION X'_e = (G'_e, R'_e, rho'_e, event data): one outcome of the E-34.4 normalization rule |
| RECORD | the co-division relation with its multiplicities (ECC's sense, unchanged) |
| KERNEL CONTEXT | the localized pair (R restricted to the arm's neighborhood of the trigger, the trigger cell), up to simultaneous relabelling |
| ORBIT VARIABLE | one free kernel weight per relabelling orbit of localized (record, trigger, candidate event) tuples -- record-dependence through orbit structure only |

The bound sources, verbatim:

> A division event on cell (x, l) increments n_l(x) by one.

> The menu at site x is the three link traversals and the weight
> q(l|x) is the post-coin Born weight |(Cψ)(x,l)|².

> The record accumulates the law's own weights and the state is not
> collapsed onto the emitted cell, so the walk stays coherent between
> division events.

> at this generator a division event's footprint **is** its conflict
> group, so the geometry is a function of the groupings by
> construction

The sample-space spine: kernel weights are conditional distributions
over [SS:TRIPLE-EVENTS] given a trigger and a kernel context; walk
statistics are distributions over [SS:CELLS]; the successor ontology's
outcomes are [SS:COMPLETE-SUCCESSOR-CONFIGURATIONS].  Every
probability-typed receipt row declares one of these three names — 38
declarations, audited by gate [LIC:G-SAMPLE-SPACE].

THE CANDIDATE-BRIDGE WALL (#64, binding): the trigger semantics P(c,e|X) = q(c|X) K(e|c,G,R) is an ADOPTED CANDIDATE bridge, not a theorem; what is proven is that q(c) is the probability of paper-20's mutually exclusive CELL-HIT alternatives; this census REJECTS the candidate in its locally covariant record-dependent class at the committed windows [SS:TRIPLE-EVENTS]

THE SCOPE SENTENCE (#64, binding, gated): even a SCOUTK-NONVACUOUS or
SCOUTK-UNIQUE outcome would have closed EVENT SELECTION ONLY: quantum
transport onto created cells remains an independent missing law.

THE G-FIXED SCOPE WALL (#68 item 4, binding, gated): G is FIXED
throughout — this unit tests RECORD backreaction only; transport across
created cells and any G-to-G-prime remain independent missing laws.

## 2. Sources, parent binding, and disclosed deviations

The parent apparatus is v15/code/scout_exact.py at its DELIVERED digest
edb60bccd22e (ledger #58).  The live file is held by the scout repair
worker mid-flight and had already diverged when this unit launched, so
the parent is bound through the byte-verified snapshot
v15/code/scoutk_parent_delivered.py (digest-gated equal to the
delivered bytes; the scout's own ECC-snapshot precedent).  The reused
walk builder, relabelling group and three-step machinery are re-typed
with ANCHORED-REUSE comments and bound three ways: the snapshot digest
[LIC:G-PIN-DIGESTS], verbatim parent-line anchors [LIC:G-ANCHORS]
including the fixed-alpha kernel definition, quoted:

> K_alpha: alpha on the line block, (1-alpha)/2 on each non-line

and the mandatory consistency check of section 7, which [BY:G-SUBFAM] re-derives the parent's fixed-alpha refusal inside this census's own orbit family.

Disclosed deviations, counted: (1) the snapshot is a fifth committed
file beyond the pin's four deliverables — an input snapshot, not a
deliverable, forced by the live repair and disclosed here; (2) LOG.md
is anchor-only and no unpinned file's digest enters the receipt (the
receipt hazard: the parent's double_build_digest defect is the named
precedent; an append-only file's digest is an environment/time value),
now machine-checked in-run by [LIC:G-ENV-EXCLUSION] — the serialized
receipt provably carries no unpinned live-read digest, so it is
LOG-append-independent by construction;
(3) the pin names the scout's ECC snapshots for any LP reads — this
unit consumes no ECC LP values, so they are unread, and that is said
rather than silently true; (4) the SA and RD arms, and the MC and
GLOBAL arms, induce measurably identical orbit partitions, so three
distinct constraint systems were solved and the verdicts transfer by
the measured coincidence [LIC:G-COINCIDE]; (5) the depth-3 systems are
solved in a relaxed form (step-1 variables free) plus pinned
confirmation runs; the relaxation lemma below makes the emptiness
transfer exact; (6) the declared first-step samples are a = 0, 1/6,
1/3, 1/2, 2/3, 1, and the uniform certificate then closes the whole
segment, so nothing rests on the sample choice.

## 3. The arena, the group, the walk, the blindness licence

The committed chart is rebuilt from constructors [LIC:G-ARENA]: 27
cells in bijection with the linked actor pairs, 27 triangles among 84
triples, 9 declared lines of 12.  The relabelling group is the affine
stabilizer of the declared direction set, order 108 (12 linear x 9
translations), closed on the block class [LIC:G-GAMMA]; the cell
stabilizer (order 4) swaps the two non-line incident blocks — the
measured fact behind the first-event boundary.  The delivered walk is
rebuilt [LIC:G-WALK]: first-trigger weights (1/9, 4/9, 4/9) on cells
0, 1, 2; second-trigger support the 9 cells of the three shifted
sites.  The depth-2 blindness licence is re-measured [LIC:G-BLIND]:
the second-step Born vector is byte-identical across 11 record
variants (the initial record, all 3 cell-hit increments, all 7
incident triple-writes), mechanism single-link site support; this is
what lets every consistency equation condition on the second trigger
without a second-step correction factor.

## 4. The proximity fork (declared, run, and closed by measurement)

Each arm is a declared neighborhood map N(c,R), measured
relabelling-covariant at all 108 group elements x all 8 reached
records — the unwritten start record and the 7 written first-triple
records, the M6 strengthening re-measured by this instrument
[LIC:G-ARMS-COVARIANT].
The kernel reads R restricted to N(c,R); record-dependence enters
through orbit structure only.

| arm | declaration | N size at a cell | depth-3 orbit variables | verdict at depth 3 |
|---|---|---|---|---|
| SHARED-ACTOR (SA) | cells sharing an actor with the trigger | 11 | 16 | SCOUTK-COVARIANT-EMPTY-AT-3-SA-AT-CONDITIONAL-CONSISTENCY |
| RECORD-DISTANCE (RD) | the recorded cluster reachable through actor-sharing recorded cells | 1 at the zero record, 3 at a written triangle | 16 | SCOUTK-COVARIANT-EMPTY-AT-3-RD-AT-CONDITIONAL-CONSISTENCY |
| METRIC-COUNT (MC) | cells with an actor within declared-direction distance one | 27 | 25 | SCOUTK-COVARIANT-EMPTY-AT-3-MC-AT-CONDITIONAL-CONSISTENCY |
| CAUSAL-NEIGHBORHOOD (CN) | cells whose actors or one-step shift images meet the trigger's actors | 15 | 19 | SCOUTK-COVARIANT-EMPTY-AT-3-CN-AT-CONDITIONAL-CONSISTENCY |
| GLOBAL-REFERENCE | the whole record, no locality leg | 27 | 25 | EMPTY (reference) |

The fork's cost accounting and its closure, measured: proximity was a declared fork, and the fork closed by measurement: shared-actor and record-distance induce the same orbit partition, metric-count coincides with the global reading at this arena, and the three distinct partitions stand in the measured refinement order -- the global partition refines the causal-neighborhood partition, which refines the shared-actor partition, both refinements strict -- so causal-neighborhood sits strictly between, and all three distinct systems are empty.  And the reference row is the sharp point: locality is not the obstruction: the global reference family (25 orbit variables, no locality leg) is empty by the same certificates.

## 5. The reach census (depths 2 and 3; step 1 separately, per #64)

The pin's method, verbatim:

> Form the ORBITS of (G,R,c,e) under simultaneous relabelling; ONE
> FREE VARIABLE PER ORBIT.

The geometry slot G is the committed chart, fixed by every relabelling,
so the orbits are carried by (R, c, e).  Reached from the delivered
start [LIC:G-REACH]: 63 raw kernel contexts and 189 raw candidate
tuples over 7 distinct first events.  The honest dimension of the
covariant family, against the fixed-alpha family's single parameter:

| arm | context classes | tuple orbit variables | orbits shared with depth 1 |
|---|---|---|---|
| SA | 6 | 16 | 2 |
| RD | 6 | 16 | 2 |
| MC | 9 | 25 | 0 |
| CN | 7 | 19 | 2 |
| GLOBAL | 9 | 25 | 0 |

Context-class descriptors (pattern size, trigger-recorded, recorded
cells sharing an actor with the trigger, first-event line-ness) are
published per arm in the receipt's reach/depth3 classes.  At depth 2
every localized pattern is empty, so all five arms coincide by
construction — 1 context class, 2 tuple orbits per arm.

THE STEP-1 CENSUS, SEPARATE (#64's first-event boundary)
[LIC:G-STEP1]: the first-event boundary: the completely symmetric initial state cannot use an unwritten record to select the first event; step 1 collapses to 2 orbit variables (dim 1), and the measured family realizes only the symmetric stochastic tie-break -- a declared initial asymmetry or an extra tie-breaking state variable lies outside K(e|c,G,R) and is priced as a new declaration [SS:TRIPLE-EVENTS]
The collapse size is itself the result: from 16, 16, 25, 19, 25
depth-3 variables per arm down to 2 at the symmetric start.  The
tie-break trilemma as measured constraints: (a) a symmetric stochastic
initial kernel IS what the measured family realizes — the dim-1
line-weight segment, whose only deterministic covariant member is the
line selection a = 1, because the stabilizer swap forbids a
deterministic non-line pick; (b) a physically meaningful declared
initial asymmetry is NOT realizable inside the covariant family —
privileging a label breaks the equivariance identity and is priced as
a declared exit; (c) another tie-breaking state variable is NOT
realizable inside the declared kernel signature — it would be a new
law, registered as a successor.

## 6. The depth-2 and depth-3 systems, with certificates

Depth 2 [LIC:G-D2]: under the measured blindness the consistency rows
are vacuous and the covariant family is the one-parameter line-weight
segment — SCOUTK-NONVACUOUS-1-AT-2 at every arm, dimension 1, arms
coinciding at the zero record.

THE CONSISTENCY MODE (#68 item 1, gated): the consistency mode is the #68 addendum's frozen PRIMARY -- CONDITIONAL transition agreement at every reached state: at fixed first-step weight each depth-3 constraint is linear in exactly one kernel factor (the second-invocation orbit variable), the first factor is swept exactly and closed by the uniform certificate, no bilinear system is solved, and the only relaxation used runs in the conservative emptiness direction with pinned confirmations -- and the D3 verdict names the mode in its words [LIC:G-ADDENDUM-68]

Depth 3: the walk statistics to be preserved are the delivered
conditional third-trigger profiles over [SS:CELLS], branch by branch
across the 3 first triggers and 9 second triggers; the kernel's two
invocations contribute a first-step weight (line weight a, non-line
weight (1-a)/2 each — forced one-dimensional by the step-1 collapse)
and one orbit variable per reached localized tuple class at the
written record.  The mixture equations are affine in a with the orbit
variables entering linearly, plus per-context normalization.  Three
distinct systems (SA-RD, CN, MC-GLOBAL) were each refused four ways:

1. SAMPLED: INFEASIBLE at all 6 declared samples of a, 18 exact
   refusals [LIC:G-D3-SAMPLES], each with a verified exact Farkas
   certificate (y.A <= 0 columnwise, y <= 1, y.b = gap)
   [LIC:G-D3-FARKAS].

| system | a = 0 | a = 1/6 | a = 1/3 | a = 1/2 | a = 2/3 | a = 1 |
|---|---|---|---|---|---|---|
| SA-RD (16 vars) | 40907/4860 | 146376256/12571605 | 43086727/3537837 | 148923404/12310623 | 13812206/1162755 | 5108/567 |
| CN (19 vars) | 141977/15552 | 1394818199/113067900 | 2676748303/207170136 | 227934907/17676792 | 41613199/3367980 | 5108/567 |
| MC-GLOBAL (25 vars) | 141977/15552 | 938664259/72684945 | 404341687/29073978 | 204275030/14536989 | 26482327/1959552 | 2648/243 |

2. UNIFORM: one uniform Farkas certificate per system closes the whole segment: y.A(a) is affine in the first-step line weight, both endpoint checks verify, and y.b = 1, so emptiness holds at EVERY a in [0,1].  The certificates are small — supports 6, 6 and 7 rows, all
   mixture rows — and published in full in the receipt
   [LIC:G-D3-UNIFORM].

3. BRANCHWISE: the branchwise lemma is stronger than the mixture refusal: even conditioning on each written first triple separately, no covariant second-invocation kernel matches the delivered third-step profiles.  Gaps 22835/1701, 53755/3402 and 1598/81
   [LIC:G-D3-BW].

4. IDENTIFIED: for SA-RD and CN, 2 depth-3 orbits localize to the
   empty pattern and are therefore the SAME orbits as the step-1
   classes; locality plus covariance pin those variables to the
   step-1 kernel values.  The relaxation lemma: the identified family
   adds pin rows to the relaxed system on the same variables, so every
   identified solution solves the relaxed system and the uniform
   emptiness already covers it; the four pinned confirmation runs are
   INFEASIBLE with certificates (gaps 205192925/16121106,
   386831585/30236004, 2924765939/217475280, 101215751/7459128)
   [LIC:G-D3-IDENT].

THE MECHANISM, measured, not narrated [LIC:G-CLASH]: the mechanism witness: at a = 0 the branch rows (0,5,14) and (1,11,21) carry identical covariant coefficient vectors while the delivered walk assigns 16/729 against 64/729 -- covariance identifies what the anchored start state distinguishes; the witness is the FIRST clash in canonical row order -- canonical, not curated.  This is the same death mode the
parent met on the fixed-alpha line — overdetermination by symmetry —
now closing over the full record-dependent family.

THE TRIGGER-ERASURE MECHANISM (#82, the thirteenth review, verified at the bytes): the kernel construction builds the available record from the whole triple footprint while the target walk depends on the individual cell-trigger history -- the bridge lets one cell trigger a three-cell event, the triple record forgets which cell was the trigger, and the walk remembers and uses it; global access cannot recover information the bridge erased at write-time.  That is why the
global-reference family fails with everything visible: the missing
datum was never written.

## 7. The binding consistency check and the priced pure kernels

The fixed-alpha family re-derived as a subfamily [BY:G-SUBFAM]: tying
every orbit variable record-blind (line orbits to alpha, non-line
orbits to half the complement — line-ness is orbit-invariant, gated)
inside this census's own mixture rows yields 729 row polynomials
reducing to 25 distinct nonzero ones, whose linear members force
alpha = -1, 0 and +1 simultaneously — the same refusal, byte-equal to
the direct parent-style construction re-typed here, and matching the
parent gate line quoted in the anchors.  The alpha probes 0, 1/3 and 1
all fail.  This binds the unit to its parent: #58's numbers reproduce
inside the new instrument before the new question is answered.

The parent's pure census reproduces [LIC:G-PURE] and is priced: the 288 pure kernels the parent counted survive pointwise and are now priced: none is realizable by any covariant assignment, so every survivor breaks relabelling symmetry.  (8 all-non-line first-step
selections extend to 288 pure kernels on the reached cells.)

## 8. Controls

Both synthetic controls run through the real builder and solver
[LIC:G-CONTROLS]: a target generated by a declared covariant
record-dependent kernel (uniform thirds, a = 1/3) is FEASIBLE with a
nonnegative witness; a target with one delivered branch value shifted
by one is INFEASIBLE at gap 433415665/29073978 with a verified
certificate.  The forced-nonvacuous system also serves as the negative
control for the certificate search: no uniform certificate can exist
for it, and none is found.

## 9. Verdicts

SCOUTK-REACH-CENSUS-PUBLISHED<63-CONTEXTS-189-TUPLES-7-FIRST-EVENTS; ORBIT-VARIABLES-16-16-25-19-25-PER-ARM; STEP-1-COLLAPSES-TO-2-VARIABLES-DIM-1>

SCOUTK-NONVACUOUS-1-AT-2-ALL-ARMS<BLINDNESS-11-VARIANTS; ARMS-COINCIDE-AT-THE-ZERO-RECORD>

SCOUTK-COVARIANT-EMPTY-AT-3-SA-AT-CONDITIONAL-CONSISTENCY; SCOUTK-COVARIANT-EMPTY-AT-3-RD-AT-CONDITIONAL-CONSISTENCY; SCOUTK-COVARIANT-EMPTY-AT-3-MC-AT-CONDITIONAL-CONSISTENCY; SCOUTK-COVARIANT-EMPTY-AT-3-CN-AT-CONDITIONAL-CONSISTENCY<GLOBAL-REFERENCE-ALSO-EMPTY-SO-LOCALITY-IS-NOT-THE-OBSTRUCTION; UNIFORM-IN-THE-FIRST-STEP-LINE-WEIGHT; BRANCHWISE-ALSO-EMPTY; CERTIFICATES-PUBLISHED-AND-VERIFIED>

SCOUTK-FIXED-ALPHA-SUBFAMILY-REPRODUCES-58<729-ROWS-25-POLYS-LINEAR-ROOTS-MINUS1-0-PLUS1; PURE-CENSUS-8-TO-288-REPRODUCED>

SCOUTK-CANDIDATE-BRIDGE-REJECTED-IN-ITS-COVARIANT-CLASS<THE-TRIGGER-SEMANTICS-REMAINS-A-CANDIDATE-NEVER-A-THEOREM; EVENT-SELECTION-ONLY-TRANSPORT-STILL-OPEN>

SCOUT-K verdicts: the five lines above; the reading in one sentence:
the record-dependence the ninth review asked for was granted in full —
16 to 25 orbit variables against the fixed-alpha family's one — and
the delivered walk refuses all of it at the first window with teeth.

## 10. Registered successors (not claimed)

The depth-4 window; sub-normalized / leaky kernels outside the
per-trigger normalization leg; kernels with an additional tie-breaking
state slot (trilemma arm c); declared-asymmetry non-equivariant
kernels (trilemma arm b, a priced exit from covariance); and the
quantum transport law rho'_e onto created cells — open regardless of
any kernel outcome.  The trace fork now has its named successor:
SCOUT-T (v15/note-scoutt-pin.md, FROZEN sha256-12 3f35573d88d8,
pinned at v15 ledger #82) tests fork
arm 1 (kernels carrying the ordered trigger trace) and fork arm 2 (the
marginal-history secondary mode — the #68 addendum's frozen SECONDARY)
on this unit's committed apparatus.

## 11. The numeral-binding registry (every load-bearing numeral bound)

| numeral | receipt field |
|---|---|
| 108 | gamma/order |
| 27 | arena/cells |
| 189 | reach/raw_tuples |
| 63 | reach/raw_contexts |
| 7 | reach/distinct_first_events |
| 16 | reach/depth3/SA/tuple_orbit_variables |
| 16 | reach/depth3/RD/tuple_orbit_variables |
| 25 | reach/depth3/GLOBAL/tuple_orbit_variables |
| 19 | reach/depth3/CN/tuple_orbit_variables |
| 6 | reach/depth3/SA/context_classes |
| 9 | reach/depth3/GLOBAL/context_classes |
| 2 | step1/orbit_variables |
| 1 | d2/polytope_dim |
| 11 | blindness/variants |
| 729 | subfamily/rows |
| 25 | subfamily/distinct_nonzero_polys |
| 8 | pure/surviving_first_step_combos |
| 288 | pure/pure_kernels_total |
| 38 | sample_spaces/declared |
| 6 | d3/SA-RD/uniform_certificate/certificate_support |
| 7 | d3/MC-GLOBAL/uniform_certificate/certificate_support |
| 16/729 | clash/witness/rhs_a |
| 64/729 | clash/witness/rhs_b |
| 30 | regime/gates_in_ledger |
| 29 | regime/falsifiers_registered |

## 12. Verification regime

The instrument carries 30 gates and 29 registered falsifiers, each
falsifier required to die at its declared gate with a digest move
proof; the selftest writes nothing; hostile argv exits 2; every
failure path writes nothing; the note's kit sentences, anchors,
sample-space tags, licence tokens, subject tags, slash rationals and
integer numerals are machine-verified against the receipt; every
integer numeral occurrence in this note is classified BOUND (a
specific receipt field) or NON-CLAIM (a declared reason class), the
classification total and serialized in the receipt — the former
blanket whitelist is retired; the kernel-scope wall
[LIC:G-KERNEL-WALL] refuses the retired overclaim family subject-based
(hyphen and spacing normalized) with permanent dead plants and
licensed record-blind alive twins; bare set-iteration and unsorted
directory listing are refused syntactically [LIC:G-AST-DETERMINISM];
the note's digest is the object under test in both artifacts.  The
hostile verifier's independent rebuild is archived at
v15/verify/scoutk-verifier-rebuild.py with its regenerated check
ledger v15/verify/scoutk-verifier-rebuild-output.txt, both read at
their pinned digests [LIC:G-PIN-DIGESTS].  The out-of-harness battery
(falsifier sweep at the declared gates tree-intact, the write-nothing
selftest, byte-identical regeneration of BOTH artifacts from deleted
artifacts in a git-less mirror at alien working directories under
PYTHONHASHSEED 0, 1 and 424242, and the LOG-append regeneration probe
— the receipt byte-identical after a ledger append) is run before
reporting and its results are reported to the orchestrator with this
note.
