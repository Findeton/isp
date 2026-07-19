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
