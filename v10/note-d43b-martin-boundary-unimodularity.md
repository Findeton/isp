# D43b (N2) — residue 1 via the intrinsic state chain: Perron-
# Frobenius, the Martin/renewal structure, and the unimodularity face

**Status:** CAMPAIGN PIN (strict), 2026-07-19. Parents: D43 #327
(import I1 [POSITED]); paper 30 residue 1; d42b56 #321 (the 17-state
bisimulation quotient, trajectory 4-9-14-16-17, referee-identical
partition). Receipt: `v10/code/d43b_state_chain_exact.py`.

## 1. The reduction strategy (pinned)

Residue 1 asks for a positive harmonic completion at infinite volume:
Z(h) = Σ q·Z(h+e), Z > 0, depth-stationary (root-free). On a state
quotient with transfer T, stationarity means λ·f(s) = (T f)(s), f > 0
— a Perron-Frobenius eigenproblem. THE DECISIVE QUESTION: does the
quotient STABILIZE under depth growth? If a finite intrinsic state
space closes under reachability, residue 1 REDUCES EXACTLY to finite
Perron-Frobenius and is DECIDED (existence by Perron theory on the
recurrent core; uniqueness by dominant-class count). If it grows, the
growth structure (the renewal decomposition) is the Martin-boundary
datum [import I1] and the receipt delivers the measured growth
instead. Either outcome is a result; neither is pre-committed.

## 2. The intrinsic state map [POSITED; gated against the committed
## partition]

state(h) := the isomorphism class of h's LIVE FRONTIER: per actor,
the set of held unsuperseded versions with their proposal-block
status; the live proposals with payloads; the conflict-component
structure with base identifications — all up to the actor-exchange /
payload-flip / version-relabeling symmetries (the d42b56-gated
covariances). The map must REFINE TO EXACTLY the committed 17-state
bisimulation partition on the depth-4 family (the referee-identical
anchor) — if it is coarser or finer there, the receipt fails and the
map is wrong, not the quotient.

## 3. Gates

- **MG1 (anchor):** intrinsic states on the depth-4 family == the
  committed 17-state partition exactly (same blocks).
- **MG2 (the stabilization question, pre-registered open):**
  reachability closure over intrinsic states from genesis (expand
  one representative history per new state; deterministic BFS). IF
  the closure terminates at k states: print k, the closure depth,
  and the exact rational k x k transfer T (successor-state weight
  sums — well-defined by MG1's bisimulation property, gated per
  state). IF new states persist to the declared budget (state count
  or representative depth cap, printed): deliver the growth
  trajectory + the renewal decomposition (which states recur; the
  first-return structure) as the Martin datum. No silent cap.
- **MG3 (on closure only — the decision):** the exact
  characteristic polynomial of T (Fraction arithmetic,
  Faddeev-LeVerrier); the irreducible-class decomposition
  (Tarjan on the support digraph); Perron theory applied per class:
  EXISTENCE of a positive eigenvector for the spectral radius on
  the recurrent core (structural, not numeric: irreducibility +
  nonnegativity ⇒ Perron vector > 0); UNIQUENESS verdict by
  dominant-class count. λ certified by exact sign changes of the
  characteristic polynomial (rational interval bisection, no
  floats).
- **MG4 (the root-free certificate):** with the Perron f, the
  completed transfer q'_f(e|s) = q·f(s')/(λ·f(s)) must be exactly
  equal at the root state and at the post-arb renewal state (the
  d42b56 S2 non-stationarity healed by the eigenvector — the
  root-free existence exhibit); per-state normalization Σ q'_f = 1
  exact on every state.
- **MG5 (the unimodularity/mass-transport face):** the stationary
  measure π (the left Perron vector) satisfies the mass-transport
  identity on the state chain: for the transport function
  g(s, s') = π(s)·q'_f(s→s'), Σ_out == Σ_in per state (invariance)
  — the discrete mass-transport check [import I1's unimodularity
  face at state-chain scope; the FULL rooted-graph unimodularity is
  declared the continuum successor, not claimed].

## 4. Scope

The state chain is the d42a-terminal grammar's (2 actors, binary);
the extended transport grammar's chain is the named successor. A
closure result decides residue 1 AT THIS GRAMMAR'S SCOPE (two-of-two
breadth discipline applies); the infinite-volume claim for the
physical law inherits only the FORM. Hegerfeldt untouched.

## 5. Round-1 amendments (2026-07-19; round frozen at LOG #339;
## report: reviews/d43bc-round1-hostile-review.md)

**A1 (F-B1, BLOCKER — owned): the pinned §2 map was never built,
and fails its own anchor clause.** The receipt substituted the
boundary-marked truncation refinement (the d42b56-S3 algorithm
re-run at depths 4/5/6) for §2's intrinsic frontier map, so MG1
gated the algorithm's self-reproduction — circular as an anchor.
And §2's anchor clause is UNSATISFIABLE for the pinned map,
provably from the committed data: by the pad-shift theorem
(appending a noop leaves the candidate menu identical — events and
weights — family-wide; 12,942 checks, 0 violations) any
horizon-free map puts [], [n], [nn], [nnn], [nnnn] in ONE state
where the committed 17 assigns FIVE distinct blocks, and co-classes
H3 with [nnn] (equal remaining horizon, not equal structure) — so
the pinned map is COARSER than the 17 there; simultaneously the 17
merges structurally distinct states in three mixing blocks ({0,4}
x2, {1,5} x1) — FINER there. Forward correction to §2 and LOG #330:
the committed 17 is a truncation-stratified object of the depth-4
complex — the intrinsic map must NOT reproduce it. The 17 remains
the REGRESSION anchor for the truncation algorithm (d42b56-S3's own
scope and its gated split witness survive untouched — the split is
a genuine intrinsic split, classes 1 vs 5).

**A2 (F-B2 — the round's central result reversed): the 17/23/29
growth was HORIZON STRATIFICATION, not the Martin datum.** All nine
run-6 states realized only at len >= 5 are noop-padded copies of
len<=4 structures (the pad-shift theorem); the boundary-coarse
counts grow +6 per depth — exactly one new stratum per intrinsic
class per level. The TRUE object is the referee's UNIFORM-LOOKAHEAD
INTRINSIC partition (P_0 = menu shape; P_{t+1} = one probabilistic-
bisimulation refinement; NO boundary marker; horizon uniform in h):
it STABILIZES AT SIX STATES at lookahead t = 2 on every window
computable from the receipt's own cache (|P_t| tables [4,4,5,5,5] /
[4,5,6,6] / [4,5,6] at cutoffs 2/3/4; P_t = P_{t+1} blockwise for
t >= 2), with depth-7 confirmation (179,783 histories; P_3 == P_2
on len<=4, still six). The six states, by shortest representatives:
0 quiescent/shared base (root, all pads, H3, renewals); 1 one live
proposal; 2 two non-conflicting live proposals; 3 THE CONFLICT PAIR
([pA0, pB1]); 4 diverged holdings, quiescent; 5 diverged holdings,
one live proposal.

**A3 (supersession of the delivered MG2 verdict): on the six-state
object MG3-MG5 DECIDE residue 1 on the window.** The exact 6x6
transfer is well-defined per state (rows constant on all 215 len<=3
members; row sums = the per-cut N, 5/2 at the conflict state);
lambda = 2 EXACTLY (u = lambda - 3/2 satisfies u^2 = 1/4 — rational
spectrum); ONE dominant class {2,4,5} (Tarjan; the transient radius
3/2 + (1/32)^(1/3) ~ 1.815 < 2, certified exactly by the
nonnegative resolvent (2I - M_t)^{-1}); positive eigenvector
f = (4,4,3,7,3,3)/3 with the transient extension FORCED by the
resolvent — existence AND uniqueness up to scale; ROOT = RENEWAL
STATE (MG4 = YES: P_t([]) = P_t(H3) at every t — the boundary-
frozen split was the truncation marker's artifact); the completed
transfer per-state normalized exactly (conflict row {1/7, 3/4,
3/28}); mass-transport EXACT with pi = (1,1,2)/4 on the dominant
class — no residual (MG5). Scope, stated honestly: closure is
VERIFIED on every computed window; the all-depth closure statement
awaits the RENEWAL-PUMPING CLOSURE THEOREM — the named successor —
whose two ingredients are now exhibited exactly: (i) the pad-shift
identity (gated in-receipt, 12,942/0) and (ii) the renewal subtree
isomorphism (H3's subtree isomorphic to the root tree to depth 3
under base substitution, 215 nodes, with the 144-point clean-slate
renewal census — referee-verified). Residue 1's Perron reduction is
DECIDED at this grammar's scope on that window; the Martin-boundary
import [I1] machinery is not needed here — it relocates to the
d42b1 transport grammar, where deliveries reopen the absorbing
sector and the class structure will change.

**A4 (F-B3/F-B5/F-B6 — the gate discipline): the previously-
check(True) gates are replaced by mechanical ones.** Round 1 proved
the delivered datum was ungated (MG2 and MG2-outcome were
unconditional passes; a one-character cutoff mutant printed
corrupted counts inside a self-contradictory verdict and exited
green; MG4 in the unreached branch was check(True)). The rebuilt
receipt anchors every delivered count as an expectation (17/23/29;
induced 19/20/25), gates refinement monotonicity, codes THREE
consecutive intrinsic agreements (t = 2, 3, 4) in place of the
half-coded margin-1 criterion, gates MG4 as a real state equality,
re-gates gauge constancy at the new depths (5,548 canonical classes
at depth 6, 1,565 at depth 5, 0 violations), and retains the old
label-blind computation only as the documented NEGATIVE CONTROL
with the 17 -> 6 stratification map gated (14 pure blocks + the
three mixing blocks, onto all six). No check(True) remains.

**A5 (delta verdict, 2026-07-19): DELTA-CLEAN; D-r1 applied — both
closure-theorem ingredients now receipt-carried.** The combined
delta on the rebuilt d43b+d43c came back 0 blocking / 1
recommendation / 2 nits: the referee re-derived the partition
blockwise from scratch (block-identical, six classes in round-1
order), recomputed the transfer rows from the raw cache q's against
T_REF, INDEPENDENTLY re-proved the dominant-class certificate by
cofactor determinant 3/32 + entrywise-nonnegative adjugate
resolvent, confirmed root == renewal at every t and the exact
mass-transport identity, and killed the round-1 slip-through mutant
class (the one-character cutoff mutant now fails NC1+NC2, exit 1; a
transfer tilt fails MG2d; the one green mutant is PROVEN
semantics-preserving). The single recommendation D-r1 — ingredient
(ii) referee-carried while (i) was receipt-gated — is applied here:
the new MG6 gates the renewal subtree isomorphism (base
substitution v0 -> v1 maps the root tree ONTO the H3 subtree, 215
== 215 nodes, menus event-bijective and q-equal at every node
including the depth-3 shell) and the 144-point clean-slate renewal
census (every class-0 point carrying an arb at len <= 4 has a
unique shared non-superseded base and root-identical one-step menus
under its own base substitution). 18 PASS / 0 FAIL; seeds
0/7/11/61 byte-identical; a non-recursing-substitution mutant fails
MG6 exit 1 (the subtree arm catches it — nested bases appear only
in deep continuations; the census arm alone would not, which is why
both arms are conjoined). TERMINAL as endorsed: residue 1 decided
on the computed window (lambda = 2 exact; root-free certificate
YES) at d42a scope, pending the renewal-pumping closure theorem
(both ingredients exhibited AND gated; [I1] relocates to the
transport grammar).
