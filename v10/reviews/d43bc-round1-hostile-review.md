# D43b + D43c round 1 — hostile review (pins + receipts + outs)

**Reviewer round:** 2026-07-19, against HEAD d26770f. ONE round, TWO
sibling N-program receipts on the same committed d42b3 layer.

- **Object A (D43b, N2):** pin `v10/note-d43b-martin-boundary-unimodularity.md`
  (#330), receipt `v10/code/d43b_state_chain_exact.py`, out
  `v10/data/d43b_state_chain_exact.out` (#334: 3/3; NO STABILIZATION
  17/23/29; induced-on-4 19 by-5, 20 by-6).
- **Object B (D43c, N3):** pin `v10/note-d43c-pincer-vs-escape-classes.md`
  (#331), receipt `v10/code/d43c_pincer_escapes_exact.py`, out
  `v10/data/d43c_pincer_escapes_exact.out` (#335: 4/4; E-A fails by
  visibility; E-B passes R1-R5 — "the fourth door"; "the two residues
  are now one").

Read against: `v10/code/d42b3_placement_exact.py` (the exec'd layer),
`v10/code/d42b56_rootfree_action_exact.py` + its committed .out (the
17-state quotient, trajectory 4-9-14-16-17), note-d42b4 §4 E1 (the
pincer), note-d42b2 §5 B1 (the join-typed opening click),
`v10/reviews/d42b4-round1-hostile-review.md` (the pincer's original
three-horn analysis + delta), LOG #327/#330/#331/#334/#335. Method:
byte-identity reruns on 4 hash seeds per receipt; a full independent
reimplementation of the d43b refinement (blockwise cross-checked
against the exec'd receipt's own partitions); a margin/lookahead
instrument suite the receipt does not have (uniform-lookahead
partitions, pad-shift and renewal-isomorphism theorems, a depth-7
run); an exact Perron-Frobenius execution on the corrected object;
extensional-identity and mutation batteries on scratch copies; the
E-B operator family pre-built from committed machinery. Scripts in
the session scratchpad (`verify_d43b.py`, `verify_d43b_perron.py`,
`verify_d43b_eigen.py`, `verify_d43b_depth7.py`, `verify_d43c.py`,
`bmut1/2.py`, `cmut1/3/4.py`). Nothing in the repo modified except
this file.

## VERDICT

- **D43b: 2 BLOCKER / 2 MAJOR / 2 minor / 2 nit.** Every printed
  number reproduces exactly (blockwise, not just counts). The round's
  headline — "NO STABILIZATION, the growth trajectory = the Martin
  datum" — is REVERSED on the round's own pinned question: the
  receipt substituted a boundary-marked truncation quotient for the
  pinned intrinsic map, and the growth it measured is horizon
  stratification. The intrinsic (uniform-lookahead) chain CLOSES at
  SIX states on every window computable from the receipt's own data
  (and at depth 7), the exact 6x6 transfer is well-defined, and the
  full MG3-MG5 program the receipt declared "awaiting closure"
  executes with rational answers: lambda = 2 EXACTLY, unique dominant
  class, explicit positive eigenvector, root = renewal state,
  mass-transport exact. Residue 1's Perron reduction is DECIDED
  (existence + uniqueness up to scale) at this grammar's scope on the
  computed window — the opposite of the delivered verdict.
- **D43c: 1 BLOCKER / 1 MAJOR / 2 minor / 2 nit.** PG1/PG2 are real
  and verified; the E-A exclusion is a genuine small theorem and the
  FLP-partial scoping is correct. PG3 — the round's flagship — never
  constructs the operator it announces: R1 is literally x == x
  (proven extensionally and by byte-identical mutation), R2/R5 are
  regs_of/admissible restatements, R4 is the d42b4 NSE toy rerun
  verbatim. "The arb-layer operator EXISTS at fixture scale" and "the
  two residues are now ONE" are claim-wider-than-computation — the
  standing conviction class, recurring at the exact front (d42b4-F2)
  whose round-1 conviction was "no operator is ever applied". The
  repair is cheap and is PRE-VERIFIED below (the {V_C} family built
  from committed machinery, 15/15 green).

Zero false internal numbers in either object — the streak holds. Both
convictions are at the claims/object layer.

---

# OBJECT A — D43b

## Reproduction (all green)

- Reruns PYTHONHASHSEED 0/7/11/61: byte-identical to the committed
  .out, exit 0 (LOG "0/7" consistent), ~18 s.
- Independent reimplementation (own data structures and relabeling):
  family sizes 1/7/39/215/1191/6471/34375 (depths 0-6); run-4
  trajectory [4,9,14,16,17] and 17 states; run-5 23; run-6 29;
  induced-on-4 by-5 = 19, by-6 = 20; induced-on-5 by-6 = 25; by-6
  refines by-5 refines run-4 (monotone). BLOCKWISE equality with the
  exec'd receipt's S4/S5/S6 and p5_on4/p6_on4 verified, and with the
  committed d42b56 trajectory [4,9,14,16,17,17].
- Gauge re-check the receipt omits: run-5/run-6 states are constant
  on all 5548 canonical classes (0 violations) — holds, referee-
  verified (F-B6).

## F-B1 — BLOCKER (CONFIRMED): the pinned intrinsic map was never
## built; MG1 gates algorithm self-reproduction; the pinned map, had
## it been built, FAILS the pin's own anchor clause

Pin §2 pins a specific object: state(h) = the isomorphism class of
h's LIVE FRONTIER up to the gated covariances, with the anchor clause
"the map must REFINE TO EXACTLY the committed 17-state partition ...
if it is coarser or finer there, the receipt fails and the map is
wrong, not the quotient." Pin §3 MG2 pins the algorithm: reachability
BFS over intrinsic states, one representative per new state. The
receipt does neither: its docstring already re-states the strategy as
"bisimulation partitions at depths 4, 5, 6" — the SAME
boundary-marked partition-refinement that produced the 17 in
d42b56-S3, re-run at three depths. MG1 therefore gates that the
algorithm reproduces itself (verified: it does, blockwise) — not
that any intrinsic map refines to the committed partition. Circular
as an anchor.

And the pin's anchor clause is UNSATISFIABLE for the pinned map —
provable from the committed data alone:

- **Pad-shift theorem (referee, new):** appending a noop leaves the
  candidate menu IDENTICAL — events and weights — family-wide
  (12,942 pad histories checked, 0 violations). So [], [n], [nn],
  [nnn], [nnnn] have literally identical subtrees, and any
  horizon-free map (frontier or behavioral) puts them in ONE state.
  The committed 17 assigns them FIVE distinct blocks (ids 16, 10, 0,
  1, 2) — and co-classes H3 (the post-arb renewal point, len 3) with
  [nnn] (block 1): equal remaining horizon, not equal structure.
  The pinned map is therefore COARSER than the 17 here.
- Simultaneously the 17 is TOO COARSE elsewhere: it merges
  structurally distinct states in three blocks (the {0,4}x2 and
  {1,5}x1 mixing blocks of the stratification table below) — the
  clean one-live-proposal state with the diverged
  zombie-live-proposal state, etc. The pinned map is FINER than the
  17 there.

Coarser somewhere and finer elsewhere ⇒ by pin §2's own clause the
receipt fails with the pinned map. The green MG1 was purchased by the
substitution. The committed 17 is a legitimate quotient OF THE
TRUNCATED depth-4 complex (d42b56-S3's own scope — untouched, and
its gated split witness [pA0] vs [pA0,selfA,pv1] survives as a
GENUINE intrinsic split, classes 1 vs 5 below); what fails is D43b's
promotion of it to the intrinsic anchor (pin §2, LOG #330 "the
intrinsic map must reproduce the committed 17-state partition
exactly").

## F-B2 — BLOCKER (CONFIRMED, the round's central result reversed):
## the delivered "growth/Martin datum" is horizon stratification; the
## intrinsic chain CLOSES at six states on every computed window; the
## Perron program executes exactly

**(i) The margin anatomy.** Induced-partition counts (rows = run
depth, cols = cutoff; margin m = run − cutoff):

    run-4: [1, 3, 8, 13, 17]
    run-5: [1, 3, 8, 14, 19, 23]
    run-6: [1, 3, 8, 14, 20, 25, 29]
    run-7: cutoff-4 = 20, cutoff-5 = 26  (referee, 179,783 histories)

Same-cutoff agreements: cutoffs 0-2 agree at every margin; cutoff 3:
m=1 (13) disagrees, m=2 vs m=3 AGREE (14, blockwise); cutoff 4: m=0
(17), m=1 (19), m=2 (20), m=3 (20) — **run-7's induced partition on
the depth<=4 family is blockwise IDENTICAL to run-6's.** The pattern
is uniform: margin-1 objects are always one refinement short;
margin>=2 objects agree wherever computable. The receipt's MG2
criterion compares a margin-1 object with a margin-2 object (p5_on4
vs p6_on4) — the one comparison its own cutoff-3 row already shows to
be margin-dominated — and its .out label calls this "the
stabilization criterion at margin 1" while claiming "two consecutive
agreements" (only ONE comparison is coded; see F-B5). The depth-7
probe (LOG #334's own named successor; ~3 min) settles it: the
induced object STABILIZES at margin >= 2. "NO STABILIZATION" is the
boundary talking.

**(ii) The "new states" are padding copies.** All 9 run-6 states
realized only at len >= 5 have n-padded representatives of len<=4
structures ([nnnnp], [nnnnn], [nnnnpp], [nnppr], ...) — by the
pad-shift theorem their subtrees are IDENTICAL to their unpadded
twins'; they are new horizon strata, not new frontier structure. The
boundary-coarse counts grow as 17, 23, 29, 35 (run-7): **+6 per
depth, exactly one new stratum per intrinsic class per level** — the
arithmetic signature of pure stratification (6 = the intrinsic class
count below).

**(iii) The intrinsic instrument and its verdict.** The
uniform-lookahead partitions P_t (P_0 = menu shape; P_{t+1} = one
probabilistic-bisimulation refinement; NO boundary marker; horizon
uniform in h — computable from the receipt's own depth-6 cache at
zero extra enumeration cost):

    cutoff 2: |P_t| = [4, 4, 5, 5, 5]
    cutoff 3: |P_t| = [4, 5, 6, 6]
    cutoff 4: |P_t| = [4, 5, 6]   -> depth-7: P_3 == P_2, still 6
    P_t vs P_{t+1}: DIFFER at t=0,1; AGREE at t=2,3,4,5 (all windows)

**The intrinsic partition stabilizes at lookahead 2 with SIX
classes.** Transfer rows are constant on all 215 len<=3 members
(depth-6 data) and on all 1,191 len<=4 members (depth-7 data) — the
probabilistic-bisimulation property, gated by this review. The six
states, with shortest representatives:

    0  quiescent, shared base           ([]; all pads; H3; renewals)
    1  one live proposal, shared base   ([pA0])
    2  two non-conflicting live props   ([pA0, pB0])
    3  THE CONFLICT PAIR (edge)         ([pA0, pB1])   <- the 5/4 state
    4  diverged holdings, quiescent     ([pA0, selfA])
    5  diverged holdings, one live prop ([pA0, pB0, selfA])

The exact transfer (Fractions; row sums = the per-cut N):

    T[0] = {0: 3/2, 1: 1/2}                          sum 2
    T[1] = {1: 3/2, 2: 1/8, 3: 1/8, 4: 1/4}          sum 2
    T[2] = {2: 3/2, 5: 1/2}                          sum 2
    T[3] = {0: 1/2, 3: 3/2, 5: 1/2}                  sum 5/2
    T[4] = {4: 3/2, 5: 1/2}                          sum 2
    T[5] = {2: 1/4, 4: 1/4, 5: 3/2}                  sum 2

Structure: two nontrivial classes — {0,1,3} (the shared/conflict
sector, TRANSIENT, containing the renewal loop 3 -> 0) and {2,4,5}
(the no-conflict-possible sector, ABSORBING at this grammar's scope:
d42a-terminal has no delivery events, so diverged holdings never
re-converge; d42b1's transport grammar is the named successor scope).

**(iv) MG3-MG5, executed exactly (the receipt's unreached closure
arm, on the correct object; all Fraction, no floats):**

- Perron root of the dominant class {2,4,5}: **lambda = 2 EXACTLY**
  (u = lambda − 3/2 satisfies u^2 = 1/4). Transient-class radius
  3/2 + (1/32)^(1/3) ~ 1.81498 < 2 strictly ⇒ dominant class UNIQUE.
- Positive harmonic vector, exact: **f = (4/3, 4/3, 1, 7/3, 1, 1)**;
  T f = 2 f verified in Fractions. The transient extension is FORCED
  ((2I − M_transient)^{-1} applied to the cross-flow returns exactly
  (4/3, 4/3, 7/3)) ⇒ **the positive 2-harmonic function is unique up
  to scale on the whole chain** — existence AND uniqueness, the
  MG3 decision, delivered.
- The completed transfer q'(i->j) = T[i][j] f_j / (2 f_i) is per-state
  normalized EXACTLY (all six rows sum to 1); e.g. the conflict state's
  row: {0: 1/7, 3: 3/4, 5: 3/28}.
- **MG4 (root-free certificate): YES.** Root and H3 are the SAME
  intrinsic state (class 0): P_t([]) = P_t(H3) for every t; the
  subtree below H3 is isomorphic to the root tree to depth 3 under
  base substitution v0 -> v1 — 215 nodes, menus event-bijective with
  equal q at every node (extending d42b56-S2's one-step bijection
  two levels). All 144 clean-slate renewal points at len<=4 have
  root-identical one-step menus under base substitution. The
  boundary-frozen runs split root from H3 at EVERY depth (4, 5, 6) —
  the receipt's object would have delivered MG4's "obstruction datum"
  arm; the obstruction is an artifact of its own truncation marker.
- **MG5 (mass-transport): EXACT.** Left vector pi = (1/4, 1/4, 1/2)
  on {2,4,5} (pi T = 2 pi in Fractions); the pi.f-weighted law is
  invariant under q' exactly — no residual, no approximate-witness
  caveat (the receipt's power-iteration + 1e-6 tolerance design is
  unnecessary on the true object; the spectrum is rational).

**Scope, stated honestly:** closure at six states is VERIFIED on
every window this review computed (transfer rows constant through
len<=4; P_2 = P_3 at depth 7; induced margins >= 2 stable at cutoffs
<= 4; intrinsic count on the depth<=5 family still 6). The all-depth
closure statement needs a renewal/pad self-similarity pumping
argument — both ingredients are now exhibited exactly (pad-shift
identity; renewal subtree isomorphism) — a small successor theorem,
not an open-ended hunt. Residue 1 at this grammar's scope reduces to
the exhibited finite Perron data; the Martin-boundary import [I1]
machinery is NOT needed here — it relocates to the extended
(transport) grammar, where the absorbing/transient structure will
change.

**(v) The assigned label-translation-quotient question, answered.**
The pure version-relabeling (renewal-translation) quotient of the
induced partitions does NOT stabilize by itself: |quot by-5| = 15 vs
|quot by-6| = 16 (it heals renewal copies but not pad strata; and
the margin-1 object is additionally under-split — its unsplit
mixing block bridges intrinsic classes 0/4, collapsing the healed
by-5 to 5 blocks in the full-healing variant). The FULL horizon
healing (pad-shift + renewal translation) of the margin-2 object
lands EXACTLY on the six-class intrinsic partition (healed by-6 ==
P_2, verified blockwise). So: the receipt's own hypothesis
("renewal-isomorphic states split by distance-to-boundary") is the
right diagnosis for the [] / H3 / pad splits, but the TRUE intrinsic
map does not merely re-merge those — it also SPLITS the committed
17's three mixing blocks (the zombie/diverged-base structure the
margin-0 anchor cannot see: 17 -> 19 -> 20 induced growth is
precisely these GENUINE splits arriving). Both defects of the
committed anchor are real; the intrinsic map closes; see the
stratification table:

    intrinsic class {0}:    3 pure blocks of the 17   (horizon strata)
    intrinsic class {1}:    3 pure blocks
    intrinsic class {2}:    3 pure blocks
    intrinsic class {3}:    3 pure blocks
    intrinsic class {4}:    1 pure block
    intrinsic class {5}:    1 pure block
    MIXED {0,4}:            2 blocks   <- under-split (genuine merge defect)
    MIXED {1,5}:            1 block    <- under-split

## F-B3 — MAJOR (CONFIRMED, mutation-proven): the entire delivered
## datum is ungated; MG2 and MG2-outcome are check(True); MG1 is the
## receipt's only real gate

The committed run's "3/3" = 1 real gate (MG1) + 2 unconditional
PASSes. Mutation bmut2 (one character: the induced_partition cutoff
`<=` -> `<`) prints a corrupted datum — "induced-on-4: by-5 = 14,
by-6 = 14 ... agree = True" — INSIDE the "NO STABILIZATION" outcome
label, and exits 0 GREEN, 3/3. The receipt cannot detect wholesale
corruption of the numbers it delivers as the round's result, and can
print a self-contradictory verdict line (headline "NO STABILIZATION",
detail "AGREE = True") without failing. MG4 in the unreached branch
is also check(True). bmut1 (MG1 expectation 17 -> 18) fails and exits
1 — the plumbing works; the gates just do not gate the claim (the
d42b3-F1 / d42b4-F2 gate-theater class, third recurrence).
Mechanical form prescribed in R-B3.

## F-B4 — MAJOR (CONFIRMED): pin §3's else-arm deliverable is half
## missing; LOG #334's "Delivered per pin §3" is false as to the half

Pin MG2, else-arm: "deliver the growth trajectory + THE RENEWAL
DECOMPOSITION (which states recur; the first-return structure) as the
Martin datum." The receipt delivers counts only: no recurrence
analysis, no first-return structure, no renewal decomposition
anywhere in receipt or .out. (This review's SCC decomposition,
renewal-point census — 144 clean-slate points — and subtree
isomorphism are exactly the missing half, now referee-anchored.)

## F-B5 — minor (CONFIRMED): the criterion sentence overstates the
## design; fossil variables mark the uncoded half

"Two consecutive agreements = the stabilization criterion" — one
comparison is coded (p5_on4 vs p6_on4). The dead assignments
`p5_on5cut` and `n5_int` (both = the by-5 induced object, never used)
are fossils of the uncoded first comparison. The closure-branch
predicate `stab_4 and len(p6_on4) == n6_int5` compares partitions of
different families by cardinality — opaque; under bmut2 it routes the
self-contradictory print.

## F-B6 — minor (CONFIRMED, repaired-by-review): gauge
## well-definedness at the new depths never re-gated

d42b56 gated state-constancy on canonical classes at depth 4 only;
d43b extends the object to depths 5/6 without re-gating it. Referee:
0 violations over 5,548 canonical classes at both depths — holds, but
it was a free tripwire the receipt skipped.

## F-B7 — nit: dead code and latent hazards

Six dead symbols: `interior_states`, `state_key_map` (defined, never
called), `p5_on5cut`, `n5_int` (assigned, never read), `import sys as
_s` (unused alias), `lam_mid` (assigned, never read — in the
unreached branch). The entire closure branch (lines ~150-322) is
unreached in the committed run and contains a latent zero-guard
hazard (the vR recompute's power iteration divides by max(w) without
the m == 0 break the first loop has). FAM4/FAM5 are enumerated
separately although FAM6 contains both (pure waste, ~25% of runtime).

## F-B8 — nit: cwd-dependent exec (third recurrence)

`open('v10/code/d42b3_placement_exact.py')` — runs only from the repo
root; FileNotFoundError, exit 1 from `v10/` (fail-safe, verified).
The d42b4-delta D-n2 one-line `__file__`-anchor repair remains
unapplied in both new receipts.

---

# OBJECT B — D43c

## Reproduction (all green)

- Reruns PYTHONHASHSEED 0/7/11/61: byte-identical, exit 0, ~0.13 s
  (LOG "0/11" consistent).
- PG1 ground truth from the committed layer, independently: A's menus
  {selfA 1/4, idle 3/4} sum 1 at [pA0] vs {selfA 1/4, pairA 1/8,
  pairB 1/8, idle 3/4} sum 5/4 at [pA0,pB1]; both pair winners
  inadmissible early; B's sums 1 and 5/4. PG2's two facts: own-view
  canonical DAGs identical; supports differ. R3's kernel facts: PK1 =
  1/2-1/2 on the 2-conflict; 1/4 x 1/2 = 1/8. R4's control =
  |1/sqrt2 − 1/sqrt5| = 0.2598931856865895851... reproduced.

## F-C1 — BLOCKER (CONFIRMED): the operator family {V_C} is never
## constructed; the PG3 gates are grammar restatements; "the
## arb-layer operator EXISTS at fixture scale" is unsupported as
## computed

The pin's PG3 test is explicit: "the isometry V_C built from the
d42b2 chain: opening click + continuations + acceptance, now as ONE
typed higher-order operation." The receipt builds no such object — no
matrix or isometry indexed by C, no composition, no operator applied
to any state. What each R-gate actually is:

- **R1 is x == x.** `comb_menu(h)` and `dict(arb_menu(h))` are the
  identical filter (`e[1]=='A' and e[0]=='r'`) of the identical
  source (`candidates_for`). Extensional identity verified on all 215
  depth<=3 histories; mutation cmut3 (replace comb_menu's body with
  `return dict(arb_menu(h))`) produces a BYTE-IDENTICAL .out. The
  "reproduces both menus exactly from the admission relation" gate
  cannot fail under any sabotage of the layer (cmut1's PK1 tilt
  passes R1 while R3 catches it). The receipt's own comment concedes
  the method: "computed FROM THE ADMISSION RELATION ONLY".
- **R2** checks two `regs_of` facts (selfA's carriers; B in the pair
  event's carriers) — the committed A6 convention restated; no
  operator support is examined.
- **R3** is the one real new-ish gate (kernel weights 1/8-1/8-1/4 at
  the menus; mutation cmut1, PK1 tilted to 1/3-2/3, fails R3 and
  exits 1 — while PG1's sums are tilt-blind: 1/4 x (1/3 + 2/3) is
  still 1/4). It re-gates committed d42b2/d42b3 numbers at the
  fixture.
- **R4** is the d42b4-QG4 basis-copy toy VERBATIM (same probes, same
  lossy control, same 0.2599 value = 1/sqrt2 − 1/sqrt5) — a 3-dim
  copy reception with no relation to any component index, comb wire,
  or winner record; d42b4-F5 already convicted this map as "the
  trivial common denominator". Its label here ("the comb's record
  side") attributes it to an object that does not exist in the code.
- **R5** checks two `admissible()` outcomes (real facts; the
  past-locality of the index is by code-structure argument — true,
  but prose).

So PG3's PASS establishes: the committed grammar data is consistent
with the comb TYPE. The .out and LOG #335 say more: "the arb-layer
operator EXISTS at fixture scale as a past-local-indexed comb" /
"PASSES R1-R5" with R1-R5 named as if they tested an operator. This
is the d42b4-F2 conviction class recurring at the same front one
round later, after that round's repair prescription (d42b4-R1:
"exhibit a joint-carrier commuting isometry family reproducing the
d42a measure ... none is known to this referee; nothing in the
receipt attempts it") — still unattempted. The honest deliverable
was: "E-A is excluded (theorem); the comb TYPE is well-posed and
consistent with the record; the operator itself remains
unconstructed."

**The repair is cheap and is PRE-VERIFIED (15/15 green,
`verify_d43c.py` E1-E5):** from committed machinery only —

- V_single (|C| = 1): the deterministic winner-record isometry.
  V_pair (|C| = 2): |rec> -> sum_w sqrt(1/2) |rec, w, v(C,w)> built
  as Acceptance ∘ OpeningClick (the d42b2-B1 chain composed as ONE
  typed operation; for |C| = 2 the chain is one click + acceptance);
  matrix product verified; V^T V = I at 1e-40 for V_pair, V_single,
  and both factors.
- Born branch weights == the committed K1 kernel (1/2, 1/2;
  deterministic singleton) at 1e-40.
- **Menu reconstruction:** (classical past-local index set + sector
  mass, read from `admissible`/`candidates_for`) x (V_C Born weights)
  == the committed menus at BOTH cuts, exactly, in Fractions — the
  non-tautological form of R1.
- **Cut-independence where it belongs:** the SAME V matrices serve at
  both cuts; only the classical index set differs ({singleton} early;
  {singleton, pair} at the join), and the index is computed by
  `admissible()` from the event's own past cone.
- The horn-2 price, stated: V_pair acts on BOTH proposers' records
  (licensed join carriers per A4/A6) — commutation-by-disjointness is
  forfeited at joins; concurrent arb operations exist only on
  disjoint components (where commutation is trivial); the
  foliation-invariance face at overlapping-visibility scale remains
  the successor problem. A receipt containing exactly these gates
  plus the receipt's current PG1/PG2/R3/R5 would support the
  fourth-door existence sentence at fixture scale.

## F-C2 — MAJOR (CONFIRMED): "the two residues are now ONE" /
## "residue 2's operator question is answered at this scope" —
## overclaims riding on F-C1

Two independent defects in the verdict sentence (and LOG #335):

1. With no operator constructed, nothing was "answered" — a reduction
   PLAN was typed. (Dischargeable by R-C1; the pre-verification above
   shows the reduced claim would then be true at fixture scale.)
2. Even granting the exhibit, "ONE" over-merges: residue 2 carries,
   besides the operator-existence face, the foliation/commuting-
   family face at overlapping visibility (the price horn 2 named;
   d42b4-R1's explicit OPEN arm) — which does NOT relocate to residue
   1's measure question. The receipt's own PG4 paragraph is more
   accurate than its verdict line ("what is new is the higher-order
   TYPING + the mechanical R1-R5 discharge" — the second half of
   which F-C1 refutes). The pin's own PG3 wording ("A PG3 pass is an
   existence exhibit ... not the full quantum completion") was the
   right scope; the verdict line outran it.

## F-C3 — minor (CONFIRMED): "the fourth door" vs the record — the
## door walked through was horn 2's OPEN interior, and the receipt's
## framing half-says so

Checked against what the d42b4 round actually proved: the pincer
closed only the cut-INDEPENDENT single-operator arm by arithmetic
(menus 1 vs 5/4; branch sets differ); the cut-DEPENDENT arm was left
explicitly OPEN ("disjointness gone and the commuting-family
existence question is OPEN — the successor problem, not a discharged
one" — d42b4 review F2/R1; the note's E1 "carrier structure breaks"
phrasing is harder than the review's, and d43c inherits the note's
version). The comb is a horn-2 object whose carrier overlap is
LICENSED (A4/A6) and whose cut-dependence factors through past-cone
data — a genuine and valuable typing distinction (cut-attached =
foliation data vs past-local = covariant data, in the program's own
terms), but "the fourth door EXISTS" + "the three horns stand
unrefuted" reads as a trichotomy of closed doors evaded, where the
record shows a trichotomy with one door closed, one dilation arm
closed, and one arm always open pending the operator exhibit. PG4's
"the door was in the grammar since A6" concedes the substance; the
headline vocabulary does not. One-sentence repair (R-C2).

## F-C4 — minor (CONFIRMED as stated; theorem itself verified and
## strengthened): PG2's candidate class is prose-level, and the pin's
## second arm is silently dropped

The E-A exclusion argument is sound and this review strengthens it:
the two gated facts imply the DISTRIBUTIONAL form (any family
measurable in (own view, private randomness) has the same output
distribution at both cuts, while the required supports differ — the
pair branches are inadmissible early and required at weight 1/8 at
the join), which covers coins, local clocks, counters, and any data
on the initiator's wire (verified: own views remain identical across
cuts with extra A-ticks inserted). Two scoping defects: (a) no
formalized candidate class appears in the receipt (the "family" is
quantified only in the gate label's prose — acceptable for a
two-fact theorem, but the pin promised a "formalize[d] ...
click-conditioned family"); (b) pin PG2's pre-registered second arm
("or does the d42b2 join-typed opening click license the visibility
(then E-A reduces to E-B's typed-input form)") is not addressed in
the receipt or .out — the delivered "any repair reads the join" is
arm 1's phrasing, and arm 2 is arguably what PG3 then instantiates;
the reduction sentence is missing. The FLP-partial finding
(obstruction = VISIBILITY, not adversarial scheduling) is verified
correct and correctly scoped as refining import I2: FLP's quantifier
structure (termination under adversarial asynchrony) is not this
pincer's (a single step operator vs cut-relative menus), so Ben-Or's
measure-zero-adversary escape has no purchase — the analogy is
partial exactly as printed.

## F-C5 — nit: PG1's sums are tilt-blind by construction

cmut1 proves PG1 passes under a PK1 tilt (count- and sum-preserving);
R3 is the load-bearing weight gate. Fine division of labor — worth
one label clause so PG1 is not read as gating the kernel.

## F-C6 — nit: PG4 is check(True); cwd; label slivers

PG4 is a scope declaration wearing a gate (corpus-tolerated for
honesty gates, but it inflates "4/4"). Same cwd-dependent exec as
F-B8 (fail-safe, verified exit 1 from v10/). R4's "comb's record
side" label (see F-C1). The receipt's banner "PG2/PG3 verdicts
PRE-REGISTERED" is accurate and honored — both outcomes were genuinely
open in the pin; no complaint.

---

# WHAT SURVIVES (verified)

- **Every internally printed number, both objects** — reproduced
  exactly, blockwise where partitions are concerned; byte-identical
  reruns on 4 seeds each; exit-1 plumbing fires on real anchor breaks
  (bmut1, cmut1, cmut4). Zero false numbers.
- **D43b's raw deliverables as FACTS about the truncation object:**
  17/23/29 boundary-coarse counts, 19/20/25 induced counts, the
  trajectory, monotone refinement — all real (and now explained:
  +6/level stratification; margins >= 2 stable).
- **MG1's reproducibility content:** d42b56-S3's partition is exactly
  reproducible (algorithm-stable, blockwise). d42b56-S3's OWN gated
  claims survive untouched — including its split witness, which this
  review confirms as a genuine intrinsic split (classes 1 vs 5).
- **D43c PG1** (the pincer baseline re-gated from the layer) and
  **PG2** (the E-A exclusion theorem — real, new, and strengthened
  here to the distributional form with clock robustness); the
  FLP-partial refinement of import I2.
- **The comb TYPE observation** — past-local (covariant) indexing vs
  cut-attached data is a real distinction in the program's own
  vocabulary, and the A6/d42b2-B1 structures do carry it; PG4's
  honesty paragraph.
- **R3's kernel re-gate and R5's admissibility facts.**
- **The committed d42b3 layer** re-verified once more (menus, sums,
  PK1, admissibility, own-view facts — all exact).
- **Referee-computed, offered to the program:** the pad-shift
  self-loop theorem (12,942 checks); the renewal subtree isomorphism
  to depth 3 (215 nodes) + the 144-point clean-slate census; the
  six-state intrinsic chain with exact transfer, lambda = 2, f =
  (4,4,3,7,3,3)/3, pi = (1,1,2)/4, uniqueness, per-state-normalized
  completed transfer, exact mass-transport; the root = renewal
  identity; the 17-into-6 stratification table (3 mixing blocks); the
  depth-7 anchors (family 179,783; run-7 count 35; induced-on-4 = 20
  blockwise-stable; induced-on-5 = 26); the {V_C} operator family
  construction (isometries, K1 Born match, menu reconstruction,
  cut-independent matrices).

# PRESCRIBED REPAIRS (pre-verified where stated)

- **R-B1 (F-B1+F-B2, the flagship).** Rebuild d43b on the intrinsic
  object: the uniform-lookahead bisimulation (P_t from the SAME
  depth-6 cache; stabilization gate P_t == P_{t+1} on the maximal
  common window, margins >= 2 policy for any induced comparison), or
  equivalently the horizon-healed quotient (pad-shift + renewal
  translation — verified equal to P_2). Keep the 17 as a REGRESSION
  anchor for the truncation algorithm, relabeled as such; add a
  forward-correction note to pin §2's anchor clause and LOG #330
  (the committed 17 is a truncation-stratified object — the intrinsic
  map must NOT reproduce it; witness: five pad blocks, three mixing
  blocks). Deliver the closure arm with the exact objects above
  (k = 6, T, lambda = 2, f, pi, uniqueness, MG4 = YES, MG5 exact —
  all pre-verified in Fractions this round); state the window scope
  and name the renewal-pumping closure theorem as the successor
  (ingredients exhibited). Named successor grammar scope: d42b1
  transport (deliveries reopen the absorbing sector).
- **R-B2 (F-B4).** If any Martin/renewal framing is retained for the
  extended grammar, deliver pin §3's actual else-arm content
  (recurrence structure; the SCC decomposition and first-return data
  are in this review for the current grammar).
- **R-B3 (F-B3+F-B5).** Gate the datum: anchor the delivered counts
  as expectations (the campaign's standing anchor discipline — MG1
  already does this for 17); gate refinement monotonicity (by-(D+1)
  refines by-D — can fail on regression); code BOTH consecutive
  comparisons or drop the "two consecutive agreements" clause; make
  any outcome branch print its predicate's operands from one
  computation (bmut2's self-contradictory print becomes impossible);
  delete the fossils; convert MG4's check(True) to a real gate on the
  intrinsic chain.
- **R-B4 (F-B6-F-B8).** Re-gate gauge constancy at every new depth
  (anchors: 0 violations / 5,548 classes); delete the six dead
  symbols; guard or excise the unreached branch's vR iteration;
  enumerate once (FAM6 contains FAM4/FAM5); anchor the exec path
  from __file__ (both receipts).
- **R-C1 (F-C1).** Build {V_C} per the pin's own PG3 sentence — the
  E1-E5 construction above is the pre-verified core (~40 lines,
  mp.dps 50 suffices; all rationals dyadic). Replace R1 with the menu
  RECONSTRUCTION gate (index x V_C-Born x sector mass == committed
  menus, Fractions); keep R3/R5; re-scope R4 to the comb's actual
  record side (the winner/version registers of V_C — orthogonal
  outputs, distances preserved by construction; state it) or drop it;
  add the E5 price sentence to PG4.
- **R-C2 (F-C2+F-C3).** Verdict/LOG language: "residue 2's
  OPERATOR-EXISTENCE face is discharged at fixture scale by the
  exhibited family; its foliation/commuting-family face at
  overlapping visibility remains open (horn 2's standing arm); the
  comb's weight/measure side is residue 1" — replacing "the two
  residues are now ONE" and "the fourth door EXISTS" with "the
  fourth door is horn 2's open arm, now typed past-locally and
  exhibited" (after R-C1). Add pin-PG2-arm-2's one sentence: E-A's
  only repair route is the join-licensed visibility, i.e. E-A
  reduces to E-B — which PG3 then adjudicates.
- **R-C3 (F-C4-F-C6).** One clause formalizing the E-A family class
  (functions of (own view, private randomness) — the distributional
  form is two lines and referee-verified); a PG1 label clause on the
  tilt-blindness; __file__ anchor.

# Reproduction inventory

- Reruns: `PYTHONHASHSEED={0,7,11,61} python3 v10/code/d43b_state_chain_exact.py`
  (~18 s) and `...d43c_pincer_escapes_exact.py` (~0.13 s) from the
  repo root -> byte-identical to the committed .outs, exit 0.
- `verify_d43b.py` (19 ok / 1 by-design XX = the naive translation
  quotient's non-stabilization): sizes 1/7/39/215/1191/6471/34375;
  blockwise receipt cross-check (S4/S5/S6, p5_on4/p6_on4); the
  margin table; refinement chain; P_t table; renewal subtree iso
  (215 nodes); P_t root = H3; 144 renewal points; quotients 15/16;
  split diagnosis (three splits, reps printed); 9 padded new states;
  gauge 0/5,548.
- `verify_d43b_perron.py` (6 ok / 3 interpretive XX, all explained in
  text): pad-shift 12,942/0; the six classes + reps; transfer
  well-defined on 215; T extracted; SCCs {0,1,3}/{2,4,5}; char poly;
  root 2 by rational probe; positive vector; root = renewal; healed
  by-6 == P_2 (healed by-5 = 5, margin-1 under-split); the
  stratification table (3 mixing blocks).
- `verify_d43b_eigen.py` (6/6): T f = 2 f exact; pi T = 2 pi; cycle
  product 1/32 => dominant-class uniqueness; forced transient
  extension (4/3, 4/3, 7/3); completed rows sum 1; exact
  stationarity.
- `verify_d43b_depth7.py` (3 ok / 1 domain-artifact XX): 179,783
  histories (~3 min); run-7 = 35, traj [4,9,15,21,27,32,34,35];
  **induced-on-4 by-7 == by-6 BLOCKWISE (20)**; induced-on-5 by-7 =
  26; P_3 == P_2 on len<=4; rows constant on all 1,191.
- `verify_d43c.py` (15/15): PG1/PG2 ground truth; distributional
  form + clock robustness; R1 extensional identity (215 histories);
  R3/R2 independent recomputation; control = 1/sqrt2 − 1/sqrt5; the
  {V_C} construction E1-E5.
- Mutations: `bmut1` (17 -> 18): FAIL, exit 1. `bmut2` (cutoff
  off-by-one): **exit 0 GREEN with corrupted datum 14/14/20 and
  "agree = True" inside the NO-STABILIZATION label** — the F-B3
  proof. `cmut1` (PK1 -> 1/3-2/3): PG1 PASS, R3 False, exit 1.
  `cmut3` (comb_menu := dict(arb_menu)): **byte-identical .out** —
  the R1 tautology proof. `cmut4` (lossy reception): exit 1. Cwd
  probes: both receipts FileNotFoundError / exit 1 from `v10/`
  (fail-safe).

**Disposition.** Neither round is terminal-fit as committed. D43b's
computations are all correct and its hedges name the right suspicion
(LOG #334's "may be separating renewal-isomorphic states ...
undecided"), but the round delivered the truncation object's growth
as the pinned question's answer, left the entire delivered datum
ungated, and never built the pinned map — while the intrinsic answer
was computable from its own in-memory cache and REVERSES the
headline: the chain closes at six states on every computed window,
with lambda = 2 and a unique positive completion, deciding residue 1
at this grammar's scope pending a small closure theorem. D43c's E-A
theorem and typing observation are real assets; its flagship
operator-existence sentence names an object the receipt never
constructs, with its central gate literally unfalsifiable — the same
front's round-1 conviction class, one round later. Both repairs are
small and pre-verified here: d43b's closure arm executes with
rational answers; d43c's {V_C} family is ~40 lines from committed
machinery. On R-B1-R-B4 / R-C1-R-C3 and green reruns, both fronts
return strengthened: residue 1 DECIDED at d42a scope (with the
transport-grammar successor named), and the fourth door an actual
exhibited operator family instead of a type annotation.
