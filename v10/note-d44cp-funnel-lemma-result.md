# D44c-P — result: the promotion is PARTIAL

**Status:** GREEN-UNREVIEWED, 2026-07-24.  Receipt
`v10/code/d44cp_funnel_lemma_exact.py`, output
`v10/data/d44cp_funnel_lemma_exact.out`, 27 PASS / 0 FAIL, exit 0.
Pin: `note-d44cp-funnel-lemma-promotion.md` (LOG #406, committed
before the receipt existed).  Entry condition: LOG #355; target:
paper 32 §6 item 7.

**HEADLINE.**  #355's two entry-condition halves are DISCHARGED —
the sixth clause and up-cone confinement are now receipt-gated
over the three committed exhaustive families.  A scale-free crown
no-go is delivered as a THEOREM WITH A CONSTRUCTIVE CERTIFICATE,
but **ARB-SCOPED ONLY**.  Paper 32 §3.1's FULL-POSET claim is NOT
discharged, and this receipt additionally **falsified its own
proposed route to it**.  Per the pin's decision rule, paper 32 §6
item 7 is therefore **AMENDED TO PARTIAL, not closed.**

## 1. What was gated (the entry condition)

Over the three committed exhaustive families — width 3 to 6 events
full grammar (551,928 histories), width 3 to 7 no-idle (224,580),
width 4 to 6 no-idle (436,864), all three counts reproduced exactly
from D44c —

- **the SIXTH CLAUSE** (incomparable arbs share no common upper
  bound among the arbs): **zero violations over 23,226 live
  incomparable arb pairs.**  No longer referee-carried.
- **UP-CONE CONFINEMENT**: the arb up-sets of incomparable arbs
  are pairwise disjoint, and the whole up-set family is laminar —
  **zero violations of either.**
- the five previously gated clauses (i)-(v) plus the chain law
  reproduce at zero, so the promotion stands on the same ground.

The liveness of the stratum is gated first (pin FG1): had no
incomparable arb pairs occurred, a zero violation count would have
been a vacuity rather than a result.  23,226 pairs occur.

## 2. THEOREM (T2), and its proof

> **Theorem.**  Let P be the event poset of any admissible p/r/n
> history, and let P|_R be its subposet induced on the ARB events.
> If every principal down-set of P|_R is a chain, then P|_R is a
> rooted forest, its order dimension is at most 2, and it contains
> no crown S_n for any n >= 3 — at every width and every depth.

**Proof.**  *(a) Forest.*  If every principal down-set is a chain,
each element x with a non-empty down-set has a unique maximal
predecessor, its parent; elements with empty down-sets are roots.
The parent map is acyclic because parents are strict predecessors.
Hence P|_R is a rooted forest ordered by ancestry.

*(b) Dimension <= 2, constructively.*  Order the roots and each
element's children arbitrarily but fixedly.  Let L1 be the DFS
pre-order taken with roots ascending and children ascending, and
L2 the DFS pre-order taken with roots **descending** and children
**descending**.  Both are linear extensions, since a pre-order
always emits an element before all of its descendants regardless
of child order.  Take x, y distinct.

- If x < y, then x is an ancestor of y, so x precedes y in both.
- If x, y are incomparable and lie in different trees, their roots
  differ; L1 emits the lower-indexed root's tree first and L2 the
  higher-indexed root's tree first, so the two orders disagree.
- If x, y are incomparable and lie in the same tree, their paths
  to the root diverge at a common ancestor into two distinct
  children c_i, c_j.  L1 emits c_i's subtree first, L2 emits
  c_j's, so again the two orders disagree.

Therefore x < y in P|_R exactly when x precedes y in both, i.e.
{L1, L2} is a realizer and dim P|_R <= 2.  ∎

*(c) No crown.*  In a crown, each top dominates two incomparable
bottoms, so its principal down-set is not a chain, contradicting
the hypothesis.  ∎

**The reversal of the ROOT order is load-bearing.**  Reversing
only the child order leaves every cross-tree pair emitted in the
same relative order by both extensions, which would force
spuriously comparable pairs.  The receipt gates this as an
explicit near-miss mutant (FG7(d)): the child-only construction
fails on a two-root forest while the stated construction succeeds.

**Machine verification of the implication, independent of the
grammar (FG9).**  Step (b) is not verified on grammar instances
only.  All **46,233 rooted forests on <= 8 nodes** were enumerated
as parent functions with parent(i) < i or None — a topological
labelling, which every rooted forest admits, so the enumeration is
exhaustive up to isomorphism — and for each the realizer was
constructed and verified to realize the poset **exactly**, with
the g2 oracle cross-checking every forest on <= 6 nodes (873
checks, zero disagreements).  Zero failures.  This is what
licenses the word THEOREM for the implication rather than for a
family of instances.

**Hypothesis status.**  The hypothesis of T2 — every principal
down-set of P|_R is a chain — is gated at zero violations over the
three committed families, and is logically equivalent to the sixth
clause (an element above two incomparable arbs *is* a common upper
bound); the receipt runs both counters independently and they
agree.  **T2 is therefore scale-free in its implication and
family-gated in its hypothesis, and must be stated that way.**  It
is not rounded up to "proved for all histories".

**67,403** arb subposets — every class of every family — were
additionally certified by producing the realizer and checking it
exactly, with the g2 oracle agreeing on all 67,403 and zero
disagreements, so dim <= 2 holds there **by certificate, not by
oracle verdict**.

## 3. What was FALSIFIED — three pre-registered items

The pin fixed three candidate forms and forbade post-hoc
selection.  Three items came back negative, and each is a
deliverable.

**T1 [FALSIFIED — as pre-registered].**  The FULL event poset is
NOT a rooted forest: 23,016 classes carry an element whose
principal down-set is not a chain.  The mechanism is the intended
one and was written down before the measurement: an arb consumes a
component of mutually conflicting proposals, hence dominates two
incomparable proposals.

**L3 [FALSIFIED, 23,844 counterexamples].**  The pin proposed
that x < y forces the actor-register sets of x and y to intersect.
It does not.  A causal link can be carried entirely through a
minted vname register, and — more sharply — **every one of the
23,844 violating pairs is PURELY TRANSITIVE: zero of them are
cover pairs.**

**L1 [FALSIFIED, 16,842 of 42,144 dominators].**  The pin proposed
that every element dominating two incomparable elements is an arb.
It is not.  Domination is transitive, so a proposal that reads a
minted vname inherits the whole down-set of the arb that minted
it, and thereby dominates the incomparable proposals that arb
consumed.

**The identical counts are explained, not left standing.**  Three
independent predicates — actor-projection, full-register, and the
restricted `aset(x) <= aset(y)` form — each returned exactly
23,844.  That coincidence is gated and accounted for: every
violating pair is transitive (so it shares no register at all,
actor or vname, making the full-register form coincide with the
actor form) and every one is headed by a non-arb (so by L5, which
HOLDS, singleton actor sets make containment equivalent to
intersection).  A triple coincidence left unexplained in a receipt
is an instrument smell; this one is a structural fact.

## 4. What is NOT falsified — a distinction that must be carried

**This receipt falsified ITS OWN RECONSTRUCTION of the round's
argument, not the round's argument.**  The D44c round-1 route to
the funnel lemma goes through POOL LAMINARITY (the AG3 CONSEQUENCE
text: a top sharing an actor with a bottom has a nested pool, and
the crown's required overlap pattern is non-laminar).  That route
was never written in gateable form, and **it is not tested here.**

Nothing above impugns the referee's claim.  What is established is
narrower and still useful: **the obvious register-theoretic route
to a full-poset crown no-go does not exist**, so a future attempt
must go through pool laminarity or something new, and must not
re-walk L1/L3.  Recording a dead route is the point of recording
it.

## 5. Disposition for paper 32

**§6 item 7 — AMEND TO PARTIAL.  Do not close.**  The amendment
must say all of:

1. The two halves of #355's entry condition (the sixth clause,
   up-cone confinement) are now RECEIPT-GATED at
   `v10/code/d44cp_funnel_lemma_exact.py`.
2. The scale-free crown no-go is delivered ARB-SCOPED, as T2, with
   a constructive certificate and a grammar-independent
   verification of its implication.
3. §3.1's FULL-POSET claim remains REFEREE-CARRIED and decided at
   TESTED SCALE.  Its status is unchanged by this unit.
4. The register-theoretic route to (3) is DEAD, with the
   counterexample classes named.

**Paper 32 is TERMINAL and is not edited on green-unreviewed
evidence.**  Per the discipline that protected papers 30/31/32
through the D46 sweep, this unit is GREEN-UNREVIEWED; the
amendment is queued and applies only after a hostile round.

## 6. Defects owned in this receipt's own construction

- **Run 1 dedup key was UNSOUND.**  D44c deduplicates structural
  work by the register-word class, sound there because every
  cached quantity is poset-derived.  It is not sound for
  ARB-SCOPED quantities: the actor-register projection does not
  determine which events are arbs (a propose by A and an arb with
  pool {A} share the letter {A}).  **The receipt's own resample
  gate caught this at 2,398 mismatches in 11,664 resamples**; the
  key now carries the event-type sequence and the gate reads zero.
  All counts in this note are from the corrected run.
- **Run 1's FG8 exit-discipline gate was self-defeating**: it
  conjoined `FAIL == 0`, so it failed precisely when the
  falsification discipline was working as designed.  Restated to
  assert what it means.
- The witness horn is wired as a genuine exit-0 outcome and
  **exercised** — four invocations this run (T1, L3, L1, and the
  crown-mutant exercise) — discharging the defect owned at LOG
  #354 F1, which is BINDING on successor dimension receipts.

## 7. Residues / successors

1. **The full-poset crown no-go** remains open.  The only live
   route is pool laminarity; it needs stating in gateable form
   before it can be gated.
2. **T2's hypothesis at unbounded scale.**  The sixth clause is
   family-gated, not proven.  Proving it from the grammar would
   make T2 unconditional.
3. The FG10 scanner-coverage obligation (LOG #403 MA-2) is
   carried, with its label scoped to what it enforces.
