# D44c-P — the funnel lemma's paper-grade promotion (PIN)

**Status:** PIN, STRICT, 2026-07-24.  Committed BEFORE any receipt
code exists (pin-before-receipt discipline).  Successor 1 of the
user's six.  Parent: D44c TERMINAL (LOG #354/#355); entry
condition stated at LOG #355 and restated in paper 32 §6 item 7.

## 1. Why this unit exists

Paper 32 §3.1 leans on a SCALE-FREE no-go for the crown pattern
that is **REFEREE-CARRIED**: the D44c receipt gates five
confinement clauses mechanically, while the SIXTH clause
("incomparable arbs share no common upper bound") and the funnel
lemma itself live only in the frozen round-1 review.  Paper 32
therefore had to demote the lemma mid-round and record the
multi-author corner as decided AT TESTED SCALE with the crown case
referee-carried.

LOG #355's promotion condition, verbatim in substance: **an
in-receipt gate of the sixth clause and of up-cone confinement
over the committed families, plus the lemma written as a
theorem-with-proof-note.**

## 2. The pre-registration problem, and how it is handled

The honest difficulty: the round's route from the clauses to the
lemma is recorded as prose, and reconstructing it *after* seeing
the data is exactly the failure mode that produced five headline
reversals in the D46 sweep (LOG #394-#403).  A promotion receipt
that picks its theorem after looking is worthless.

**Therefore this pin PRE-REGISTERS THREE CANDIDATE THEOREM FORMS
AND A DECISION RULE.**  The receipt measures the hypotheses; the
decision rule — fixed here, before any code — selects which forms
may be claimed.  A form whose hypothesis fails is reported as
FALSIFIED, not quietly dropped, and its falsification is a
deliverable.

- **T1 (strongest).**  The FULL event poset of every p/r/n history
  is a rooted forest — every principal down-set is a chain —
  hence has order dimension <= 2 at every width and depth.
  *Pre-registered expectation: FALSE.*  An arb consumes a
  component of mutually conflicting proposals, so an arb should
  dominate two incomparable proposals.  Stated so the expectation
  is on the record before the measurement.
- **T2 (arb-scoped).**  The ARB-INDUCED subposet of every p/r/n
  history is a rooted forest, hence has order dimension <= 2, and
  contains no crown, at every width and depth.
- **T3 (pool-laminarity route — the round's own).**  S3 is
  impossible as an INDUCED subposet of the full event poset at
  every width and depth, via: (L1) every element dominating two
  incomparable elements is an arb, so all three crown tops are
  arbs; (L2) the pool-overlap pattern a crown forces is
  non-laminar, contradicting clause (i)+(iv).

**DECISION RULE (binding).**  A form may be stated as a THEOREM
only if BOTH its hypothesis is gated at zero violations over the
three committed exhaustive families AND its implication is
independently machine-verified (§4 FG9).  A form with a gated
hypothesis but an unverified implication is reported
`[HYPOTHESIS GATED, IMPLICATION OPEN]`.  A form with a failing
hypothesis is reported `[FALSIFIED]` with the counterexample
printed.  **No form may be upgraded after the fact by re-reading
the data.**

## 3. Scope, stated before measurement

The five gated clauses are about ARB events.  Clause (vi) is
likewise about arbs.  It therefore does NOT follow automatically
that a scale-free arb-level result transfers to the FULL event
poset, and the receipt must not blur the two.  Every gate below is
labelled ARB-SCOPED or FULL-POSET.  Paper 32's §3.1 claim is a
FULL-POSET claim; only T3 (or a gated T1) can discharge it.  **If
only T2 survives, the promotion is PARTIAL and paper 32's §6 item
7 must be updated to say so rather than closed.**

## 4. Gates (FG-series), fixed here

- **FG0 PORT FIDELITY [anchor].**  The d42a admission layer exec'd
  path-anchored from the committed `d42b3_placement_exact.py`, the
  dim<=2 oracle and width diagnostic ported code-faithfully from
  `d43d_dstar_generated_exact.py`, exactly as D44c does.
  Reproduce D44c's three exhaustive family counts (551,928 /
  224,580 / 436,864) and zero violations of clauses (i)-(v).  Any
  mismatch is anchor breakage: exit 1.
- **FG1 CAPACITY / ANTI-VACUITY [both scopes].**  The strata on
  which (vi) is a live question must be NON-EMPTY and their sizes
  printed: (a) histories containing at least two pairwise-
  incomparable arbs; (b) elements possessing at least two
  pairwise-incomparable elements strictly below them.  **If (a) is
  empty, clause (vi) is vacuously true and the promotion is
  VOID** — that outcome exits 0 with a VOID verdict, it is not a
  pass.
- **FG2 CLAUSE (vi) GATED IN-RECEIPT [arb-scoped].**  Over the
  three committed families: zero pairs of incomparable arb events
  possessing a common upper bound among the arbs.  Pairs checked
  printed.
- **FG3 UP-CONE CONFINEMENT [arb-scoped].**  The up-sets (within
  the arbs) of incomparable arbs are pairwise disjoint, and the
  up-set family is laminar.  Zero violations, count printed.
  This is the second half of #355's entry condition.
- **FG4 THE FOREST PROPERTY [both scopes].**  Every principal
  down-set is a chain — gated separately for the FULL poset (T1's
  hypothesis, expected to fail) and for the ARB-INDUCED subposet
  (T2's hypothesis).  Failures are counted and one witness of each
  kind is printed.
- **FG5 CONSTRUCTIVE 2-REALIZER [arb-scoped].**  Where the forest
  property holds, build the realizer explicitly — DFS pre-order
  with children in the canonical order, and DFS pre-order with
  children reversed — and verify it realizes the poset EXACTLY
  (x < y iff x precedes y in both).  This replaces an oracle
  verdict with a certificate.
- **FG6 ORACLE CROSS-CHECK.**  The constructive realizer's verdict
  agrees with the ported g2 `dim_le_2` oracle on every poset
  checked; zero disagreements.
- **FG7 MUTANTS (in-process, must all behave as declared).**
  (a) the S3 crown: must FAIL the forest property and the realizer
  must REFUSE; (b) the V poset (two incomparable elements below a
  common top): must FAIL clause (vi); (c) a genuine rooted forest:
  must PASS with a verified realizer; (d) the S3 crown against the
  g2 oracle: dim > 2, agreeing with the refusal.  A mutant that
  does not behave as declared is instrument breakage: exit 1.
- **FG8 THE WITNESS BRANCH IS LIVE [BINDING, LOG #354 F1].**  D44c
  shipped a witness horn that was UNREACHABLE at exit 0 — a
  witness would have tripped the census conjuncts and exited 1
  mislabeled as breakage, and the verdict print was dead code.
  That defect is BINDING on successor dimension receipts.  This
  receipt therefore (a) wires the witness horn as a genuine exit-0
  outcome, and (b) EXERCISES it: the FG7(a) mutant is driven
  through the SAME reporting code path, so the branch is
  demonstrated reachable rather than asserted to be.
- **FG9 THE IMPLICATION, MACHINE-VERIFIED [grammar-independent].**
  The step "rooted forest => dimension <= 2" is verified
  independently of the grammar by exhaustive enumeration of ALL
  rooted forests on <= 8 nodes: for each, construct the realizer
  of FG5 and verify it realizes the poset exactly, and cross-check
  against the g2 oracle.  This is what licenses the word THEOREM
  for the implication rather than for a family of instances.
- **FG10 ANTI-VACUITY OF THE GATES THEMSELVES.**  An AST scan of
  every `check()` predicate in this receipt confirming each
  references at least one run-bound name.  **Label discipline (LOG
  #403 MA-2): this scan enforces exactly that and nothing more —
  it does NOT catch a vacuous gate in arbitrary syntactic form,
  and must not be described as if it did.**

## 5. Falsifier

The promotion FAILS, and must be reported as failing, if any of:
FG1(a) is empty (the question was vacuous); FG2 or FG3 records a
violation (clause (vi) is false, and D44c's round-1 upgrade with
it); FG4's arb-scoped gate fails (T2 dies); FG9 finds a rooted
forest the realizer does not realize (the implication is false and
the proof note is wrong).  Any of these is a real result and is
reported as such at exit 0; only anchor/port breakage and
mutant misbehaviour exit 1.

## 6. Deliverable

A receipt discharging #355's entry condition, plus a
theorem-with-proof-note stating exactly the forms the decision
rule of §2 permits — and an explicit instruction for paper 32 §6
item 7: CLOSE if T3 or T1 survives, AMEND TO PARTIAL if only T2
does.
