# D44b (successor 2) — invariance at transport scope

**Status:** CAMPAIGN PIN (strict), 2026-07-19.  Parents: d43b
TERMINAL (#344; the relocation clause: "[I1] Martin machinery
relocates to the d42b1 transport grammar — deliveries reopen the
absorbing sector"); the d42b1 terminal layer (#304; events p/r/n +
d delivery + m merge; budgets 1/4 propose | 1/4 arb+merge | 1/4
deliver | idle absorbs; declared caps ARM-1T (A,B) depth <= 4,
ARM-2T (A,B,C) depth <= 3); paper 31 §7 item 8.  Receipt:
`v10/code/d44b_transport_invariance_exact.py`.  Runs LAST in the
campaign (program pin); execution gated on paper-31 terminal.

## 1. The question

Re-pose the d43b program on the transport grammar: what is the
INTRINSIC state object when deliveries and merges exist, and does
the completion core (Perron data, root-free certificate, mass
transport) survive there?  The d43b class structure is expected NOT
to transfer: state 4/5's absorption ("diverged holdings never
reconverge") was an artifact of deliverylessness.  Everything below
is pre-registered OPEN; the honest deliverable may be a
non-stabilization exhibit at the feasible caps.

## 2. Gates (pre-registered)

- **TG0 (layer fidelity):** the d42b1 layer executed from the
  committed receipt (path-anchored); the committed ARM-1T census
  re-anchored before new content.
- **TG1 (the intrinsic partition):** the uniform-lookahead
  probabilistic-bisimulation refinement (the d43b definition,
  verbatim — menu shape; one refinement step; NO truncation marker)
  on the ARM-1T family at its committed cap: |P_t| tables per
  window; stabilization verdict.  If it does not stabilize on the
  computable windows, THAT is the delivered result (with the growth
  table and the first non-stabilizing block exhibited).
- **TG2 (transfer well-definedness):** rows constant per class on
  the deepest well-defined window — or the exhibit of the first
  class whose members disagree (transport may genuinely break
  finite-lookahead factorization; deliver it, do not paper over).
- **TG3 (THE REOPENING PREDICTION):** pre-registered: the
  d43b-absorbing pattern (diverged holdings) is NO LONGER closed —
  exhibit a delivery path reconverging a diverged configuration
  inside the enumerated family, with its exact weight; or refute
  (if the caps cannot reach reconvergence, say so and construct the
  shortest admissible reconverging chain above cap, admission-
  checked event-by-event, as the SIG-chain convention allows).
- **TG4 (Perron data, conditional):** if TG1+TG2 deliver a closed
  exact transfer: Tarjan structure, Perron root (exact if rational,
  else certified bracketing in exact arithmetic), positive-vector
  existence/uniqueness status, root-vs-renewal comparison.
- **TG5 (mass transport, conditional):** the invariance identity
  tested exactly on the dominant structure if TG4 closes.
- **TG6 (negative control):** the six-state d43b classifier applied
  blindly to transport histories must FAIL (a delivery-containing
  history whose menu no d43b class reproduces — gated), so the d42a
  result cannot be silently reused.
- **TG7 (caps and honesty):** all caps printed; every conditional
  gate that does not fire prints its non-firing reason; no
  infinite-volume claim under any outcome ([I1]'s Martin/R-theory
  machinery is the named tool for whatever TG1-TG5 leave open — its
  formal deployment is a successor, not this receipt).

## 3. Scope

ARM-1T at committed caps (ARM-2T only if runtime permits; declared
either way).  Weight-system level; no measure claim.  Exact
Fractions throughout.  This unit CLOSES the campaign: its outcome
states exactly what the closure theorem (D44a) does and does not
cover, and where the imported boundary machinery must enter.

## 4. First-run amendments (2026-07-19, pre-round; declared
## deviations)

**A1 (TG1's third horn).** The pin's stabilize-or-not dichotomy
resolved between its horns: WINDOW-CONSISTENT STABILIZATION WITHOUT
CLOSURE — the per-candidate partition (the d43b operator verbatim;
the #366 per-candidate lesson applied) agrees blockwise at t = 1, 2
on its windows and lands at SIX classes on len <= 2 (a
transport-scope echo of the d42a six, a DIFFERENT object), but the
window chain ESCAPES: 68 transitions from len <= 2 parents land in
5 classes first realized only at len 3. Both the growth table and
the split + escape exhibits are gated deliverables.

**A2 (caps as measured).** ARM-1T at depth 4 (3,969 histories,
cumulative [1,9,69,521,3969]) carries the intrinsic program;
ARM-2T at depth 3 (3,424) runs census + purity + menu-count only
(the intrinsic program not run there — declared). The printed
summary carries a < 600 s boolean instead of wall seconds (byte-
identity); ~7 s measured.

**A3 (TG3's fallback unused).** The reopening witness exists
IN-FAMILY (3 events, weight 1/256; 124 reconverging pairs among
1,044 diverged histories) — the above-cap SIG-chain fallback was
not needed.

## 5. Round-1 amendments (2026-07-19; round frozen at
## reviews/d44b-round1-hostile-review.md: REVISE, 0B/1M/3m/3n; all
## five headlines survived the referee's from-scratch rebuild)

**B1 (F1 MAJOR — the vacuously-satisfiable negative control,
repaired).** TG6b's d42a shape-control set was gated only through
its consequences (a `shapes0 = set()` mutant ran silent-green);
the control-set size is now gated (len == 4).

**B2 (F2 — the print-only counts, anchored).** The diverged census
(1,044), the reconverging-pair count (124), the ARM-2T shape count
(11, now the gate TG1s), and the d42a shape count (4, in B1's
gate) are exact expectations.

**B3 (F3 — the census wording corrected + the decomposition
gated).** "124 reconverging pairs among 1,044 diverged histories"
was FALSE as a subset claim: every reconverging (history, delivery)
pair ENDS non-diverged; 124 carries suffix multiplicity — the
gated decomposition: 84 distinct diverged prefixes; 4 DISTINCT
minimal (3-event) reconverging chains, all at weight 1/256 (44
pairs share them). LOG #371's phrasing forward-corrected at #373.
(One coordinator slip caught by the gate itself during repair: the
minimal-chain conjunct first counted PAIRS (44), not distinct
chains (4) — the receipt failed exit 1 until corrected; recorded.)

**B4 (F4 — the criterion drift, declared).** STAB = two blockwise
agreements (the second on a 9-history window); the d43b F-B5
three-consecutive standard is UNMEETABLE at this cap (only two
nontrivial lookaheads exist) — now declared at the definition site.

**B5 (nits).** The tautological FIRE-conjuncts removed from TG5/TG7
(the definition restated only in detail strings); the split-pair
diagnostic prints a set-symmetric difference while the gate is
multiset-exact (recorded); the per-class-aggregate mutant is
EXTENSIONALLY NULL at this cap (recorded so no successor cites
d44b as proof the per-candidate distinction bites at transport
scope — it does not, here, by measurement).
