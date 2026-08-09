# v14 R1 — THE CONTINUUM RUNG (pin)

**Frozen:** 2026-08-09, v14 ledger #2.  **Base:** the R0 founding pin
(v14 #1) and nothing else.  **Paper number:** `paper-01` — deliverables
are `v14/paper-01-continuum-rung.md`, `v14/code/r1_continuum_exact.py`,
`_output.txt`, `_receipt.json`.  **Discipline:** RUNBOOK §13/§14/§15
with every addendum; exact arithmetic only; commit-as-is precedes
verification; single-threaded paper.

## 1. The question (falsifiable, two-sided)

**Does a declared refinement family over the v13 substrate admit a
pre-registered intensive invariant that stabilizes under refinement?**

Both verdicts are first-class and must be reachable by the instrument:

- `R1-STABILIZES-AT-<computed list>` — naming, from measured counts,
  which registered invariants stabilized, at what exact values, over
  how many consecutive family members;
- `R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE-<computed divergence
  qualifier>` — naming each candidate's measured failure mode.

The verdict string is derived inside a gate from the trajectory table,
with flip mutants proving each half and each qualifier can fail (#257,
#234).

## 2. The declared refinement family (data, not discovery — §15)

The family is the corpus's own growth sequence, extended by its stated
rule — DECLARED here, before construction:

- **A₁** = the 9-label arena of I5's construction (rebuild from the
  pinned LCB receipt's own declaration; anchor the rebuild).
- **A₂** = the 16-label arena of I5 (same).
- **A₃** = the 43-label grown arena of I2's control (rebuild from the
  pinned RSQ artifacts; anchor).
- **A₄, A₅** = the next two members of the SAME generator rule the
  A₃ construction states (the rule is data: extract it from the pinned
  artifact, print it, gate that A₃ regenerates from it before A₄ is
  built — the self-test evaluates fresh, §14).
- **Maps**: each Aₖ → Aₖ₊₁ must be the label-embedding the
  construction itself carries; functoriality (composition and identity
  on overlaps) is gated, not assumed.  If the rule yields no canonical
  embedding, that is a measured fact — print it, gate it, and let the
  verdict carry `FAMILY-NON-FUNCTORIAL` as a computed qualifier rather
  than repairing it silently.
- **Cap disclosure**: the target is five members.  If compute
  truncates the family, the cap is printed and gated (no silent caps);
  stabilization claims then carry the family length in the qualifier.

## 3. The registered intensive invariants (all five fixed HERE,
before any is computed; computing one not on this list, or dropping
one on it, is a pin violation)

1. **Overlap-completeness fraction** φₖ = (chart pairs with nonempty
   overlap) / (all chart pairs) at Aₖ.  Intensive by construction.
   **This is also R2's gateway**: any Aₖ with φₖ < 1 unlocks the
   manifold rung and is named in the receipt as R2's arena.
2. **N_coh density**: coherence classes per drawn chart pair at Aₖ
   (exact rational).
3. **Normalized spectral profile of I−E**: at each Aₖ, the multiset
   of I−E eigenvalue multiplicities over the family's readouts,
   normalized by dimension; I2 guarantees the eigenvalue-1 row —
   confirm it as an anchor chain at every member (the walls ride
   along; they are never re-censused).
4. **Per-volume dimension profile**: the link-dimension distribution
   at Aₖ normalized by chart count (the raw estimator is extensive by
   I3 and is EXCLUDED; only the normalized distribution is admitted).
5. **b₂ density**: b₂ per 2-cell at Aₖ (b₁ is trivial by I3's ordered
   measurement and carries no identification content; it is excluded
   as a candidate but printed once as a disclosure).

**Stabilization, operationally** (declared now): a registered
invariant *stabilizes* iff it is exactly constant on the final three
consecutive family members (exact-arithmetic equality; K = 3 declared
here).  The full trajectory of all five invariants over all members is
printed and receipt-recorded regardless of verdict.

## 4. Controls and falsifiers (minimum set; the worker may add,
never remove)

- **Positive control**: a family built to stabilize by construction
  (e.g., a constant-structure sequence) must return STABILIZES.
- **Negative control**: a family built to grow without bound in every
  candidate (e.g., the extensive estimator's own sequence) must return
  NO-CONTINUUM-LIMIT.
- **Scramble control**: invariant trajectories at a label-scrambled
  family member must move exactly the invariants that depend on
  identification data (b₂ density; N_coh) and fix the ones that do
  not (φ; dimension profile) — measured, not assumed.
- Mutants: family-rule corruption, map-functoriality corruption,
  per-invariant computation corruption, trajectory-table row drop,
  verdict flips on each half and each qualifier, stabilization-window
  shrink (K=3 → K=1 must be able to flip a verdict on a crafted
  trajectory), anchor-hash corruption for every I-row used.
- Cell-completeness gates on the trajectory table (#234); no gate
  references mutant identity (#208); comparators independent (#219);
  qualifiers computed (#257); declared-arena data printed and matched
  every coordinate (§15); boundary-parity gate wherever a boolean
  connective enters an incidence construction (2026-08-09 addendum).

## 5. Inheritance discipline

Every v13 number used arrives through an R0 row (I1–I7) with its
sha256-12 verified at run time.  The scale-convergence thesis is
retired; this unit measures trajectories and states no growth
narrative beyond its computed verdict.  The spectral wall is cited
(I2), confirmed per-member as anchors, never re-derived.

## 6. Success and failure are the same deliverable

STABILIZES and NO-CONTINUUM-LIMIT carry equal standing: either
closes R1 TERMINAL and hands R2 its arena (φ < 1 member) or hands the
programme the measured statement that the continuum is effective-only
at this substrate.  What R1 may not do is return a narrative.
