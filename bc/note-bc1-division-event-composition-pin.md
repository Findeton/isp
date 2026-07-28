# BC1 — DIVISION-EVENT COMPOSITION CONSISTENCY (PIN)

**Status:** PIN, STRICT, 2026-07-28.  **Program:** BC — the Barandes
consistency program (bc/LOG.md #1): from-scratch consistency tests of
the indivisible-stochastic-process framework [B3] (arXiv 2507.21192),
WITHOUT the record substrate.  This program tests Barandes' framework
on its own terms; it makes no claim about the v11 record program
(halted, untouched).

## The question

[B3] p.10 makes division events SYSTEM-CENTRIC: a division event for a
composite system need not be a division event for its subsystems, and
vice versa.  Is that assignment internally consistent across the
subsystem lattice — and does it have the structure of a marginal
problem with obstructions (the contextuality genre)?

## The unit

- **The operational predicate.**  For a finite composite with
  unistochastic dynamics (given exactly: small unitaries over exact
  algebraic entries; dims 2–8), define for each subsystem S and each
  time t₀ the predicate DIV_S(t₀): the reduced/conditional process of
  S factorizes through t₀ with a genuine (column-)stochastic bridge on
  every spanning pair (the interpolant instrument — REUSE the
  committed exact LP + Farkas machinery from
  ../v11/code/u1_indivisibility_census_exact.py, program-independent,
  cited; anchors on its known-answer behavior).  Both readings where
  they differ: the marginal (trace-out) process and the
  conditional-on-outcome process — declared, both censused.
- **The lattice census.**  For tripartite models (qubits; at least
  three distinct dynamics: product, GHZ-generating, W-generating, plus
  one Haar-free algebraic generic), compute DIV_S(t) for every S in
  the subsystem lattice {A, B, C, AB, AC, BC, ABC} at every step of a
  declared time grid.  The full containment table: is DIV_ABC ⊆
  DIV_A ∩ DIV_B ∩ DIV_C?  Any containment at all?  Census every
  crossing with exact witnesses.
- **The obstruction probe.**  State a minimal set of natural
  consistency axioms for a global division-event assignment (e.g.,
  restriction-compatibility on nested subsystems; agreement on
  overlaps for AB vs BC at B).  Test on every model whether a global
  section exists; a model with NO consistent global assignment is the
  strong finding (the contextuality analogy made exact — state the
  sheaf structure explicitly).
- **Sanity anchors:** for product dynamics on product states,
  everything must divide everywhere (the classical control); a
  known-indivisible single-system example ([B3]'s own two-level
  example if it carries one, else a constructed 3-level with the U3
  criterion) must show a non-trivial DIV set.

## Pre-registered outcomes (lean NONE)

- **C-CONSISTENT:** natural containments hold on all tested models —
  system-centricity is tame; the containment table is the deliverable.
- **C-CROSS:** containments fail with exact witnesses —
  system-centricity is real and quantified; census by model/dynamics.
- **C-OBSTRUCTION:** a model admits no consistent global assignment
  under the stated axioms — the framework's division-event ontology
  has a marginal-problem obstruction; the witness is the deliverable.

## Gates

Exact arithmetic end-to-end (rationals + declared algebraic
extensions; no floats in substantive computation); the reused
instruments anchored (exit 1 only on anchor mismatch); substantive
negatives exit 0; both-ways censuses; determinism; caps printed;
runtime < ~30 min, section progress printed (no silent interval
> 8 min).  House style: STRICT, present tense, no leans, no process
narration; status GREEN-UNREVIEWED (terminal is conferred by a
hostile round).

## Scope

Finite toy scale only; [B3]'s framework as written (quote every axiom
used, file/page-cited); no claim about nature, about QFT, or about the
record program; findings are formal properties of the framework at the
tested dimensions and dynamics.
