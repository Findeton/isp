# D46a — the H1 structural lemma

**Status:** CAMPAIGN PIN (strict), 2026-07-19.  Parents: D44a
TERMINAL #368 (the closure theorem, all-depth conditional on H1;
note-d44a §7-§8); D44b TERMINAL #374 (the boundary: this lemma is
DELIVERY-FREE-scope only).  Receipt:
`v10/code/d46a_h1_lemma_exact.py` + the proof note in this file at
conversion.  Review deferred per the D46 program pin (green-
unreviewed until the budget reopens; paper-32's round first).

## 1. The statement

**[TARGET — H1; SUPERSEDED AS WRITTEN — §8 B4 refutes the
own-view framing, and H1 is NOT discharged]**  ** At d42a scope (two actors, p/r/n, the committed
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

## 6. First-run amendments (2026-07-19, pre-round; declared
## deviations)  [A1's design choice is now CONTROLLED — see §9]

**A1 (tau's own view = the MENU-VIEW).** tau_a runs on the noop
cone PLUS the cones of a's admissible r-candidates (the pin's
design-care clause: arb_components_in_view runs on the r-event
cone); the bare noop-cone tau is refuted in-corpus (d42b3
G-T1/D3: own views equal, menus differ) and would fail LG2 at
depth 2. Printed as the receipt's [DEF] block.

**A2 (LG4a's variant).** Implements the payload+edge JOINT drop
(the pinned edge-only drop is vacuous at this scope — the d44a
round's own finding, cited in-gate).

**A3 (LG4b's form).** Demonstrated at cache level with anchored
counts + printed witnesses (the pin's scratch-variant clause), not
a full variant BFS.

## 7. The proof note — **[SUPERSEDED — see §8 B1/B2: the assembly
## is INVALID and this section's conclusion is WITHDRAWN. Retained
## verbatim as the superseded first attempt.]**

**The mechanical record (all receipt-gated, zero exceptions):** the
joint (sigma, tau_A, tau_B) BFS closes frontier-exhausted at 36
states / 176 edges with the D44a spectrum, and the projection onto
sigma is INJECTIVE — tau_A/tau_B constant on sigma across all
179,783 histories through depth 7, out-of-sample included; tau
takes 8 values per actor; the layer re-run on the menu-view
sub-history alone reproduces every per-actor menu entrywise
(436,316 comparisons); the 16 (actor, tau) classes carry 10
distinct canonical menus; the joint transition table is sigma-keyed
(176 keys, zero conflicts), so H2 is SUBSUMED — one joint closure
carries both hypotheses.

**The assembly (conditional on two structural facts, both
census-verified exhaustively in-receipt and to be written as
code-reading theorems at the round):** (i) CONE-LOCALITY —
admissible() builds its View from the candidate's past cone only
(LG2a is its census); (ii) THE ABSTRACT-UPDATE LAW — the sigma/tau
raw-data update under one event is a function of the abstract state
and the renamed event (the 176-key table is its census). Given
(i) + (ii): sigma determines (tau_A, tau_B) (LG1 injectivity, now
depth-free via the closed joint system), tau_a determines a's menu
(LG2), hence sigma determines menus at ALL depths — H1 — and H2
rides the same closure. With the D44a §8 assembly: RESIDUE 1
DECIDED OUTRIGHT AT d42a SCOPE. THIS CLAIM IS GREEN-UNREVIEWED:
it must not be cited as review-hardened until the D46a round (after
paper-32's) converts; transport scope remains open (D46b)
regardless.

## 8. Round-1 amendments (2026-07-19; round frozen at
## reviews/d46ac-round1-hostile-review.md: REVISE, 2B/4M/6m/1n).
## §7's ASSEMBLY IS RETIRED — see B1/B2 below; §7 stands only as
## the superseded first attempt.

**B1 (BLOCKER A1 — the assembly was INVALID; owned).** §7 claimed
that two structural facts — (i) cone-locality and (ii) the
abstract-update law — suffice to discharge H1. They do not. (i)
gives only menu(h, a) = menu(own-sub-history, a); (ii) gives only
sigma -> tau. NEITHER gives the second arrow tau -> menus, which
is an UNDECLARED THIRD CONDITIONAL. The referee machine-checked
the gap: a mutant swapping the layer's weight for a different
CONE-LOCAL weight leaves LG1a/b/c, LG2a, LG3a/b passing while
LG2b/LG2c FAIL — so (i) + (ii) do not entail H1. §5's closing
sentence "RESIDUE 1 DECIDED OUTRIGHT AT d42a SCOPE" is WITHDRAWN.

**B2 (BLOCKER A2 — (H0) was silently dropped).** D44a §8's
hypothesis is the conjunction (H0) + (H1) + (H2); §7 listed two
conditionals and lost (H0). The honest hypothesis set after this
round is (H0) + (ii) + (the tau -> menus arrow) — still THREE,
none discharged.

**B3 (MAJOR A3 — "H2 SUBSUMED" was inverted).** The abstract-update
law (ii) IS H2; it is not a consequence of H1, exactly as D44a §8
states. The claim that one joint closure carries both hypotheses
is withdrawn.

**B4 (MAJOR A4 — tau is NOT an own-view object; the pin's target
is REFUTED).** The MENU-VIEW (A1) strictly exceeds the actor's own
(noop) cone on 1,016 of 12,942 histories (7.9%), and in ALL 1,016
the extra events are OPPONENT-AUTHORED — precisely the "join-view
data the actor cannot see" that A1 itself cited from d42b3 G-T1.
Moreover 104 of 2,224 own-view classes carry DIFFERENT menus. So
pin §2's target ("prove tau_a(h) is a function of sigma(h) with
tau an OWN-VIEW abstraction") is refuted as stated: the object
that works is not an own-view object. These counts are now gated
in-receipt.

**B5 (A5/A6 — gate hygiene).** LG2a is a tautology of sub_of's
definition (relabelled/replaced, and A1's design choice given its
missing control); three "independent anchors" were injectivity
restated (relabelled).

**B6 — WHAT SURVIVES, exactly.** The MECHANICAL CORE stands and is
independently confirmed: the joint (sigma, tau_A, tau_B) closure
at 36 states / 176 edges with the D44a spectrum; the INJECTIVE
projection onto sigma (tau constant on sigma) with zero exceptions
over 179,783 histories; menu factorization through tau (436,316
comparisons); cone-locality confirmed a GENUINE code-reading
theorem; the menu view idempotent (0/12,942); all eight cited D44a
anchors verbatim; byte-identical rerun. **What does NOT survive is
the ASSEMBLY**: H1 is NOT discharged, and residue 1 remains
DECIDED AT EVERY VERIFIED DEPTH (D44a #368) — exactly where paper
32 left it — with the H1 gap open and now SHARPER: the missing
piece is the tau -> menus arrow at all depths, plus (H0), plus
(ii). Forward-corrected at LOG #394.

## 9. Round-1 repairs APPLIED (2026-07-19; 21 PASS / 0 FAIL)

The A4 census facts are now GATED, reproducing the referee exactly
over the 12,942 actor-histories at depth <= 5: TG2a the menu view
strictly exceeds the noop cone on 1,016 (7.9%), at most 4 extra
events; TG2b in ALL 1,016 the extra events are OPPONENT-AUTHORED;
TG2c 104 of 2,224 own-view classes carry different menus.  LG2a is
relabelled as the definitional restatement it is (it CANNOT fail,
and its comparison count is not evidence), and the new LG2a-ctl
supplies amendment A1's missing control: the bare-noop-cone
variant breaks with 248 violations in 2,382 comparisons, first at
depth 2 (by depth 8/48/192) — so the menu-view choice is now
justified by a firing gate rather than by assertion.  LG1a/LG1b/
LG3a are relabelled in-gate as COROLLARIES of LG1c's injectivity
rather than independent corroboration.  The verdict text about H1
and the assembly is the author's and is governed by §8.
