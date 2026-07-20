# D46a — the H1 structural lemma

**Status:** CAMPAIGN PIN (strict), 2026-07-19.  Parents: D44a
TERMINAL #368 (the closure theorem, all-depth conditional on H1;
note-d44a §7-§8); D44b TERMINAL #374 (the boundary: this lemma is
DELIVERY-FREE-scope only).  Receipt:
`v10/code/d46a_h1_lemma_exact.py` + the proof note in this file at
conversion.  Review deferred per the D46 program pin (green-
unreviewed until the budget reopens; paper-32's round first).

## 1. The statement

**[TARGET — H1] At d42a scope (two actors, p/r/n, the committed
admission layer): for ALL histories h, h' of ANY depth,
sigma(h) = sigma(h') implies menu(h) and menu(h') are identical as
renamed event-multisets with exact weights.**  With the committed
(H0) view invariants and (H2) transition determinism (whose own
depth-free status must be tracked — H2 may reduce to H1 + (H0) or
need its own argument, to be determined and declared), H1 closes
residue 1 outright at d42a scope via the D44a §8 conditional
assembly.

## 2. Why it is nontrivial, exactly

Menus are computed per-actor from OWN views (the sub-history each
actor has witnessed), while sigma abstracts the FULL view.  The
own-view lag exists (the D44a W2 witness); the lemma must show the
lag is MENU-INVISIBLE: whatever full-view data an actor has not yet
witnessed cannot change any candidate it is offered or its weight.

## 3. The candidate routes (pinned; the receipt gates the
## mechanical parts, the proof note carries the argument)

- **R-A (own-view determination):** define per-actor own-view
  abstractions tau_A, tau_B (the sigma construction applied to the
  own view); prove tau_a(h) is a FUNCTION of sigma(h).  Mechanical
  arm: verify exhaustively on the depth-7 cache (179,783) that
  equal sigma implies equal (tau_A, tau_B); structural arm: show
  the admission layer's menu computation factors through
  (tau_A, tau_B) by reading candidates_for/admissible (mentown
  options and arb components are own-view functions — cite the
  layer's own code paths), THEN show the (sigma -> tau) map is
  depth-free by induction on the joint transition system of
  (sigma, tau_A, tau_B): gate that its BFS closes (a finite joint
  abstraction) and that within each closed joint state tau is
  constant on sigma.
- **R-B (lag characterization):** characterize the lag L_a(h) =
  the full-view events not in a's own view; prove every lag event
  at d42a scope is an OPPONENT p/n event whose menu effect on a is
  nil until witnessed... CAUTION: opponent proposals DO change a's
  arb components at joins — the lag's menu-invisibility must be
  argued through the join-visibility structure (an event enters
  a's menu computation exactly when it enters a's own view; sigma
  records the full view, so two sigma-equal histories could a
  priori differ in how much of the shared structure each actor has
  witnessed).  If R-B finds a COUNTEREXAMPLE ROUTE (sigma-equal,
  tau-different, menu-different at some depth), H1 is FALSE and
  the closure theorem's conditional stays conditional — a
  delivered outcome, not a failure.

## 4. Gates (pre-registered)

- **LG0:** re-anchor the D44a objects (36 states; the depth-7 zero
  exceptions — cited counts).
- **LG1 (the joint closure — the depth-free step):** BFS on the
  JOINT abstraction (sigma, tau_A, tau_B) with the R-A transition
  function: gate termination with frontier exhausted; anchor the
  joint state count; gate that tau_A and tau_B are CONSTANT on
  sigma within the closed set (the mechanical core of H1).
- **LG2 (menu factorization through tau):** gate, on the full
  depth-7 cache, that menu(h) restricted to actor a equals the
  layer's computation on tau_a(h) alone (the structural-arm claim
  made mechanical).
- **LG3 (H2's status):** determine and gate whether (H2) follows
  from H1 + (H0) on the closed joint system, or gate its own joint
  closure — DECLARED either way.
- **LG4 (negative controls):** a tau variant dropping a
  menu-visible own-view component must break LG2; a sigma
  coarsening must break LG1's constancy.
- **LG5 (purity/determinism):** allow-list walk (#362); seeds; no
  check(True).

On all-green: the §5 proof note assembles H1 [THEOREM at d42a
scope] — LG1's closed joint system + LG2's factorization + the
D44a §8 assembly => residue 1 DECIDED OUTRIGHT at d42a scope (and
D44f's forced weights all-depth there); transport scope stays open
(D46b).  On the R-B counterexample: the lag structure is the
delivered object and the conditional stands permanently sharpened.

## 5. Scope

d42a scope ONLY.  Exact Fractions; the committed layers exec'd
path-anchored; caps: the depth-7 cache is the mechanical
verification surface; the BFS arms are depth-free by construction.
Green-unreviewed until the review budget reopens (program pin §0).
