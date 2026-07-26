# D61 — CLOSING (H1): mechanizing the one-token induction (PIN)

**Status:** PIN, STRICT, 2026-07-26.  Parents: the D60p probe (#450
— the own-view dichotomy verified independently; menu = G(sigma)
gated entrywise on 930,631 histories; the proof complete EXCEPT that
Lemma 5's induction is machine-checked only in its conclusions),
D44a (the (H0)-(H2) conditional theorem this closes), D51 (whose MV2
obstruction the dichotomy dissolves and whose batch-round inversion
finding does not touch this route — the closure here goes through
sigma directly, not through the projections).

## 1. The one job

Mechanize Lemma 5's INDUCTIVE STEP.  Method: an ABSTRACT INVARIANT
MACHINE in the d44a CG3 architecture — the state carries exactly the
quantities the proof's case analysis reads (per-actor: the alive
singleton X_a, the live-proposal flag, the full-view-supersession
bit; the shared/diverged sector bit), the transition function is
computed from the committed layer, and:

- **N1 (invariant, all instances):** 5a-5e hold at every history of
  the exhaustive cache (depth <= 6), zero exceptions — computed from
  the layer per history, not from the machine.
- **N2 (determinism):** the abstract state of h+e is a function of
  (abstract state of h, renamed event class) — exhaustive, zero
  exceptions.
- **N3 (frontier-exhausted closure):** BFS on abstract states from
  genesis closes at a finite count with no transition leaving the
  set.
- **N4 (the step, per transition):** for EVERY reachable (state,
  event-class) pair, the invariant holds in the successor — this is
  the mechanized inductive step; with N2 it covers every instance at
  every depth, because a deeper history's step IS one of these pairs
  (the dichotomy + Lemma 1's register geometry are why no unseen
  behavior exists, carried from the probe's proof note).
- **N5 (menu law):** menu(h) = G(abstract state), entrywise exact,
  over the cache — the probe's depth-8 gate cited [PROBE-CARRIED]
  for depths 7-8.
- **N6:** the quarter-law derivation re-gated from G.

## 2. Pre-stated consequences of success

**(H1) becomes [THEOREM at d42a two-actor delivery-free scope].**
Then: D44a's closure theorem is UNCONDITIONAL there ((H0) is the
layer's gated invariants; (H2) follows from N2 at machine level);
residue 1 is CLOSED at that scope; D49's root-free completion is
unconditional at every depth AT THAT SCOPE — still within the
stationary form (D50: the form remains a choice), still delivery-free
(transport untouched).  Paper 30/32 and book updates QUEUED behind
this unit's round, per discipline.

## 3. Falsifiers / scope

Any N-gate failure is the deliverable (exit 0 for substantive
negatives; exit 1 only on anchor breakage).  TWO-ACTOR ONLY — the
dichotomy fails at three actors and the pin forbids wider quotation.

## 4. First-run amendment (2026-07-26, recorded not silently fixed)

**A1 — "mechanize the induction" was over-promised, twice.**  Run 1's
hand-rolled abstract state was COARSER than sigma (1,932 menu
mismatches — the machine's state must be sigma itself).  And the
deeper defect: ANY cache-gated state machine leaves the same
depth-gap H1 always had — a machine verified on cached instances
does not prove the step for arbitrary h.  The depth-free force in
the probe's route comes from its Lemmas being PROSE-OVER-CODE proofs
(register geometry read from regs_of/event_poset's source), not from
a sweep.  **The deliverable, restated:** (H1) = [THEOREM at
two-actor d42a scope], carried by the probe's proof note (adopted as
this unit's proof note), with the receipt gating (i) every CASE
CLAIM of Lemma 5's step at every cached instance, (ii) the
CODE-FACTS the proof reads, asserted against the source, (iii) the
conclusion (canon_menu a function of canon_sigma) at depth 6 in this
receipt plus the probe's depth-8 gate [PROBE-CARRIED], (iv) the
quarter law per sigma state.  A Lean-grade mechanization is a
RESIDUE, honestly out of scope here.
