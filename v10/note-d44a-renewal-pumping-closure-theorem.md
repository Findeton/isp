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
