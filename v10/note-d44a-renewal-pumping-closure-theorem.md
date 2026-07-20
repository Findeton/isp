# D44a (successor 1) — the renewal-pumping closure theorem

**Status:** CAMPAIGN PIN (strict; the receipt runs only against this
text), 2026-07-19.  Parents: d43b TERMINAL (#344; the six-state
intrinsic chain, decided on the computed window; ingredients
receipt-gated NC3 + MG6); paper 31 §3.5/§7.1.  Receipt:
`v10/code/d44a_closure_theorem_exact.py` + proof note in this file's
§5 at conversion.  Execution gated on paper-31 terminal (program pin).

## 1. The target

**[TARGET] At d42a scope (two actors, events p/r/n, the terminal
admission layer), the intrinsic partition of the FULL unbounded-depth
family has exactly SIX states, the transfer is the committed T, and
the entire Perron package (lambda = 2; f = (4,4,3,7,3,3)/3 unique up
to scale; root = renewal; mass-transport exact) holds at ALL depths.**
This upgrades residue 1 from decided-on-the-window to DECIDED at
d42a scope.  The distance is one induction; its premises are the two
receipt-gated ingredients (pad-shift NC3; renewal subtree isomorphism
+ 144-census MG6).

## 2. The route (pinned)

The depth-free step is a change of enumeration space: BFS on a
bounded LOCAL-STATE ABSTRACTION instead of on histories.  Define
sigma(h) = the abstraction of the full view of h, modulo base
renaming:

- the per-actor holdings pattern (which actors hold which
  non-superseded versions, as a partition-with-multiplicity over
  renamed bases; genesis base and renewal bases are identified by
  the renaming);
- the live-proposal structure (per renamed base: the multiset of
  (proposer, value-bit) triples of live proposals, with the
  edge/conflict structure of their components);
- the superseded-base pattern restricted to bases still carrying
  any of the above (dead structure that no menu can see is dropped —
  this is exactly what the pad-shift and renewal-substitution
  identities license).

sigma is finite-valued by construction if the dropped structure is
truly menu-invisible; that invisibility is what the gates check, not
assume.

## 3. Gates (pre-registered)

- **CG1 (menu factorization):** on the ENTIRE depth-6 cache (34,375
  histories; census re-anchored [1,7,39,215,1191,6471,34375]),
  menu(h) as an event-multiset-up-to-renaming with exact weights is
  a FUNCTION of sigma(h): equal sigma => identical renamed menus,
  entrywise in Fractions.  Zero exceptions.
- **CG2 (transition determinism):** sigma(h + [e]) is a function of
  (sigma(h), e-up-to-renaming) — verified exhaustively on the cache.
- **CG3 (THE DEPTH-FREE CLOSURE):** breadth-first search on
  sigma-SPACE from sigma([]) using the CG2 transition function
  terminates; the reachable set is FINITE; its induced partition on
  the cached histories EQUALS the committed intrinsic partition
  (six classes, blockwise), and the induced transfer EQUALS T_REF.
  The BFS is the all-depth enumeration: no depth cap appears in it.
- **CG4 (the pumping normal form):** every cached history is
  reducible by (i) pad deletion (NC3's identity, re-gated on the
  reduction path) and (ii) renewal truncation (MG6's substitution,
  re-gated) to a representative of length <= 3 with the same sigma;
  the representative map is computed and gated on all 34,375.
- **CG5 (the Perron package on the abstract chain):** the committed
  exact algebra re-run against the CG3-induced transfer: lambda = 2
  (charpoly + eigen-identity), dominant-class uniqueness (det 3/32 +
  nonnegative resolvent), forced extension, root-class = renewal-
  class in sigma-space, pi = (1,1,2)/4 mass transport.  All exact.
- **CG6 (negative controls):** (a) a sigma variant that KEEPS
  menu-invisible dead structure must blow up the BFS past six states
  (the abstraction is not trivially six-valued); (b) a sigma variant
  that drops a menu-VISIBLE component (the conflict edge structure)
  must FAIL CG1; (c) the depth-marked quotient re-cited as the gated
  stratification exhibit.

## 4. Failure modes (pre-registered, each a delivered outcome)

- CG1 fails: sigma too coarse — report the splitting pair; refine
  and re-pin (forward correction).  The window decision (#344)
  stands regardless.
- CG3 reaches > 6 states: the window was NOT closed — this REVERSES
  d43b's decided-on-window reading beyond the window and must be
  logged as a reversal, with the seventh state exhibited.
- CG4 fails on some history: the pumping lemma's premises do not
  compose as claimed; exhibit the irreducible history — the closure
  theorem is then FALSE as routed and the failure is the result.

On all-green: §5 of this note receives the assembled proof
[THEOREM at d42a scope]: CG1+CG2 (bisimulation) => the intrinsic
partition refines the sigma-partition; the committed window
separation (six distinct classes at t = 2) => equality on the
window; CG3 => sigma-reachability is exactly six at every depth;
CG4 => every history's class is realized on the window; hence the
intrinsic object at all depths IS the six-state chain and CG5's
package is the all-depth decision.

## 5. Scope

d42a scope ONLY (no transport: deliveries reopen the absorbing
sector and the class structure changes — that is D44b's problem, not
a gap here).  Two actors; the committed admission layer executed
from the committed receipt; exact Fractions throughout; determinism
gated.

## 6. First-run amendments (2026-07-19, pre-round; both deviations
## are GATED obstructions, nothing silently weakened)

**A1 (CG3's pinned landing was provably unsatisfiable; the repaired
route lands the theorem).** "BFS reaches exactly 6" is impossible
for ANY CG1-sound sigma: menu-exactness forces sigma to separate
histories that are probabilistically BISIMILAR but menu-distinct —
the gated witness CG3b: [pA0, pB0] and [pA0, pB0, selfA, pA(v1,0)]
are both intrinsic class 2 with different renamed menus (one vs two
base tokens from self-arbs). NOT the pin-§4 reversal mode (no
seventh intrinsic state). The repaired route: the depth-free BFS
CLOSES AT 36 sigma-states (max representative length 6; reachable
set == cache-realized set exactly); the EXACT bisimulation quotient
of the closed 36-state chain has SIX classes, blockwise equal to
the committed intrinsic partition, with induced transfer == T_REF
(rows constant across all 36). By CG1 + CG2 the intrinsic partition
at EVERY depth is the pullback of the abstract chain's bisimilarity
— the all-depth six-state statement, through the quotient.

**A2 (CG4's "length <= 3" clause false as written; the surviving
pumping content gated).** 17/36 sigma-states have NO realization
below length 4 (divergence needs two arbs + two proposals; the
diverged sector has no renewal points at d42a scope — no
deliveries), witness [pB1, selfB, pB(v1,1), pA0] = its own
reduction; 1,832 histories in <=3-realizable states cannot be
carried there by pad+renewal moves alone. What the theorem needs
survives and is gated: the reduction mechanism (pad deletion +
renewal truncation with MG6-style back-substitution) is valid,
sigma-preserving, and idempotent on ALL 34,375 (0 failures), and
every INTRINSIC CLASS is realized on the len <= 3 window.

**A3 (minor).** CG6a's baseline reads against the delivered closure
(dead-keeping sigma: 67 cache values, no closure within a 61-state
budget vs the delivered 36); CG6b's variant drops the component
data jointly with the payload distinction that generates it (at
this scope conflict edges are payload-generated — SG2's
incomparability invariant).

## 7. Round-1 amendments (2026-07-19, post-round; frozen review
## `v10/reviews/d44a-round1-hostile-review.md` — REVISE, 0 blocker /
## 2 major; every number in the receipt reproduced by the referee)

**F1 (MAJOR — the all-depth quantifier was NOT discharged as
committed; route R2 applied, depth-7 now receipt-carried).** The
delivered proof consumed CG1/CG2 as universally quantified premises,
but they were verified exhaustively on the depth-6 cache only, and
the pumping engine the pin designed to discharge the quantifier
(CG4) was — correctly — killed by deviation A2 and replaced by
nothing: "ALL DEPTHS / OUTRIGHT" was an extrapolation, not a theorem
as delivered. Repair (R2 + the referee's depth-7 sweep carried
in-receipt as CG7a–CG7e): the enumeration is extended one full
level — all 145,408 depth-7 histories (children of the 27,904
depth-6 cache members) — and gated: ZERO new sigma-states (closure
holds out-of-sample), ZERO CG1 exceptions (menu factorization) and
ZERO CG2 exceptions (transition determinism) on the extended set
with the 16 new abstract keys anchored (176 total — the committed
CG2 provably did NOT cover this level), every one of the 36 states
carried by >= 2 witnesses (min 1,200), and sigma-row constancy
covering ALL 36 states from their full len-6 instance sets. The
verdict is rescoped to the honest form: residue 1 is decided at
EVERY VERIFIED DEPTH (exhaustive through depth 7 in-receipt); the
depth-free STRUCTURAL LEMMA — menu factorization from sigma at all
depths — is the NAMED RESIDUAL and successor target (F1-R1). The
lemma is nontrivial precisely because admissibility runs on OWN
views that LAG the full view sigma is built from (witness W2: B's
own view still holds V0 unsuperseded with pB0 live while the full
view has V0 superseded); nothing yet proves the own-view lag is
sigma-recoverable at depth 8+. The conditional assembly statement
stands as a conditional: IF the lemma holds, CG1/CG2 become
depth-free laws and the pullback argument delivers the six-state
chain, transfer T, and the Perron package at ALL depths.

**F2 (MAJOR — the quotient operator was not the committed one).**
CG3c's "same operator" label was false: the committed intrinsic
partition refines by PER-CANDIDATE (weight, successor-class)
multisets (d43b lines 92–100; the receipt's own §B port), while
CG3c aggregates weight per class — finer-or-equal per step, and the
theorem needs the per-candidate fixed point. Repaired: CG3c's label
corrected, and the committed per-candidate operator is now gated on
the same 36-chain (CG3f): trajectory [4, 5, 6, 6], blocks IDENTICAL
to CG3c's QPART — the two fixed points coincide here, closing the
identification in-receipt rather than in the review.

**F3 (minor — sigma is over-specified; recorded, not repaired).**
The referee's mutation battery proved three briefed corruption
classes extensionally NULL on the cache: dropping the post-renaming
sort in ser's live entry (m1), dropping the superseded marks
entirely (m2), and dropping the previous-class component from the
quotient refinement tuple (m4) each leave the induced sigma
partition and quotient pullback blockwise IDENTICAL to the
committed ones. So §2 bullet-3's marks and the serialization
discipline are DEFENSIVE OVER-SPECIFICATION at d42a scope on the
cache — finer-or-equal data, same blocks, harmless for soundness
but not load-bearing there; the silent-green mutants are
demonstrated-null, not missed tripwires. Recorded as committed
corpus fact; sigma is NOT slimmed (the marks may matter beyond this
scope, and the genuine corruptions of the same machineries — m10
kill-the-minimization, m9 merge-two-states — fail 7 and 10 gates
respectively).

**F4 (minor — the closure gate was outcome-anchored).** A capped
BFS (mutant m6: representatives below length 6 never expanded —
deleting the receipt's only beyond-cache verification) passed every
gate silently. Repaired: CG3a now gates FRONTIER EXHAUSTION
explicitly — every one of the 36 reachable representatives expanded,
empty frontier at termination (not a budget stop) — and anchors the
representative-length spectrum {0:1, 1:4, 2:6, 3:8, 4:9, 5:4, 6:4}
(max 6) plus prints the traversed edge count (176).

**F5 (minor — CG4 relabeled honestly).** The delivered assembly
uses CG4a/CG4b nowhere; the pin's pumping route was superseded by
the quotient route (§6 A1/A2). CG4a/CG4b are now labeled MECHANISM
EXHIBITS off the assembly route (the reduction's validity + the A2
obstruction), CG4b's "maximum 6" spectrum is marked as a CACHE
artifact (over the unbounded family the reduction has unbounded
image — the diverged sector admits no clean-slate truncation
points, which is exactly why the pumping route could not power the
all-depth step), and CG4c alone carries the assembly load (the
window-realization leg).

**F7 (pin correction).** Pin §4's sketch inverted the refinement
direction: CG1+CG2 imply sigma-equal histories are intrinsically
equal, i.e. SIGMA REFINES THE INTRINSIC partition (as the receipt's
SB3 states correctly), not the converse. The delivered route
depends on the correct direction throughout.

**Nits.** CG6a's budget raised to 200: the dead-keeping variant is
STILL OPEN at 201 states — cut at budget, not tuned (referee-
verified; the old 61 was cap+1, a budget artifact). The vestigial
`sys.setrecursionlimit(400000)` removed. CG6b stands as delivered —
§6 A3 owns the substitution (the pinned edge-only drop was vacuous
as specified: at this scope the edges are derivable from the live
triples plus SG2's incomparability invariant; N1 recorded).

Post-repair receipt: 30 PASS / 0 FAIL (24 committed gates untouched
+ CG3f + CG7a–e), exit 0, deterministic (two runs + PYTHONHASHSEED
0/7 byte-identical), ~2 min single-threaded.

## 8. The conditional-assembly proof note (at conversion; per the
## delta's guidance)

**THE HYPOTHESIS is a conjunction of three depth-indexed laws** (none
implies another; the receipt verifies all three exhaustively through
depth 7, 179,783 histories, zero exceptions — that verification is
EVIDENCE for the hypothesis, never a premise of this argument):
- **(H0)** the SG2 view invariants hold at every depth (own-view
  alive holding a singleton; non-superseded holdings inside it; live
  proposals on the proposer's base; conflicting live pairs
  incomparable);
- **(H1)** menu factorization: menu(h), as a renamed event-multiset
  with exact weights, is a function of sigma(h) at every depth —
  nontrivial because admissibility runs on OWN views that lag the
  full view sigma records (the W2 witness exhibits the lag);
- **(H2)** transition determinism: sigma(h + [e]) is a function of
  (sigma(h), renamed e) at every depth — NOT a consequence of (H1).

**THE CONDITIONAL THEOREM.** Assume (H0)-(H2). Then: (i) by the
gated frontier-exhausted BFS (CG3a: 36 states, 176 edges), sigma
takes exactly 36 values on ALL histories of every depth — the step
at depth D consumes (H1)/(H2) at depth D: a depth-D history's sigma
is reached from a depth-(D-1) sigma by one (H2)-determined
transition, and no transition leaves the closed set. (ii) The
intrinsic partition (P_0 = menu shape; P_{t+1} = one
probabilistic-bisimulation refinement; the committed PER-CANDIDATE
(weight, target-class)-multiset operator, whose fixed point on the
abstract chain is gated at CG3f: trajectory [4,5,6,6], blocks ==
QPART) is, at every depth, the pullback of the abstract chain's
bisimilarity: by induction on lookahead t — base: (H1) gives
sigma-equal => equal menu shape; step: (H1)+(H2) give sigma-equal
=> equal per-candidate (weight, class_t)-multisets — sigma-equal
histories are intrinsically equivalent at every t; and the abstract
fixed point (reached at t = 2, stable thereafter — the
uniform-lookahead fact) has SIX classes with transfer T_REF.
(iii) The Perron package on the quotient (lambda = 2; unique
dominant class; f unique up to scale; root = renewal as one
sigma-state; pi mass transport exact — all gated at CG5) is then
the completion decision at every depth. QED (conditional).

**Direct-verification scope, declared:** blockwise equality of the
pullback with the committed intrinsic partition is COMPUTED at
len <= 4 in-receipt and len <= 5 by the frozen round's referee; the
four minlen-6 sigma-states are classified only via the conditional
argument. The pumping route is NOT a mechanism of this proof (it is
retired as the §6-A2-gated obstruction exhibit); no minimality is
claimed for sigma's superseded marks or serialization (the §7 F3
nullity records stand). The all-depth conclusion is EXACTLY as
conditional as (H0)-(H2); discharging (H1) — the depth-free
structural lemma — is residue 1's final named gap.
