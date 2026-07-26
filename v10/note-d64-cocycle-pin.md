# D64 — THE COCYCLE: do the wide crystal's charts carry non-identity transitions? (PIN)

**Status:** PIN, STRICT, 2026-07-26.  Parents: D63 (TERMINAL — the
wide crystal DOUBLE-RING(8, 10, 8): 177 events / 16 actors, forced,
in-band homogeneity at d = 2 with `|D| ≥ 4` at 1/3 of events, max
`|D|` = 4 = the delivery ceiling; ends caveat: band membership is
partly an ends property), D58 (the atlas; **the containment theorem:
ω-overlaps are NESTED**, so chart-pair inclusions are identity as set
maps — the non-identity, if any, must live in COORDINATES), W4b (the
branching bound: every direction of a delivery record is reached by
P-paths over ≤ 2 registers), the user's construction order (wide
crystal → COCYCLE → descent-conditions).

## 1. The question

A manifold needs more than charts: it needs transition functions on
overlaps, and they must satisfy the cocycle identity
`g_ik = g_ij ∘ g_jk`.  At grammar layer the charts exist (D63) and
their overlaps are events shared between nearby skies — but as SET
maps the overlaps are inclusions (D58's containment).  **The
transition content must therefore be in the per-chart LABELING of
directions.**  The question: when two wide charts see the same
direction, do their local labels for it differ by a NON-IDENTITY
map — and if so, do those maps compose (cocycle) and what group do
they generate?

## 2. The objects, read from the committed layer only

- **Substrate:** DOUBLE-RING(8, 10, 8) exactly as D63's blueprint
  builds it (import by AST from the committed d63 receipt; the record
  must reproduce D63's committed profile row exactly — anchor).
  Comparator substrates: at least two genuine sprinklings (M²⁺¹ and
  M³⁺¹ at matched size, via the committed d55c generator) and one
  uncoupled brick — the POSITIVE/NEGATIVE controls for whatever
  transition structure is found.
- **Charts:** per base event `e`, the SKY-B direction set `D_e(d)` at
  d = 2 (primary; d = 3 reported), with `|D_e| ≥ 2` (and the wide
  subatlas `|D_e| ≥ 4` reported separately).
- **Coordinates (the committed-layer labeling):** each direction
  `f ∈ D_e(d)` is reached from `e` by P-paths (W4b's relation: x P y
  iff x is the immediately preceding event on some register of y).
  The label of `f` in chart `e` is the SET of register sequences
  (wire words, length d over the record's register alphabet) realized
  by P-paths from `e` to `f`.  This is a reading of `event_poset`'s
  own generating relation — no invented structure.
- **Transitions:** for an overlapping chart pair `(e, e')` (charts
  sharing ≥ 2 directions), the transition is the induced
  correspondence between the two label sets over the SHARED
  directions.  It is IDENTITY iff every shared direction carries the
  same wire-word set in both charts (after the canonical
  actor-relabeling that identifies the two base events' register
  neighborhoods, stated in the receipt).  Orderings and definitional
  choices printed; if a second natural labeling is tried (e.g.
  first-step register only), BOTH are reported.

## 3. Gates

- **C0** anchors: committed layers by AST/text-slice (d63 blueprint,
  d47a sky, d58 atlas machinery, d42b1 grammar); the substrate
  reproduces D63's committed row exactly (exit 1 on breakage).
- **C1** the chart census: overlapping pairs counted (by shared-
  direction count ≥ 2), on the substrate AND the comparators.
- **C2** THE TRANSITION CENSUS: identity vs non-identity per
  overlapping pair, both at d = 2 and d = 3, substrate and
  comparators, wide subatlas separately.
- **C3** THE COCYCLE TEST: over all chart triples with pairwise
  overlaps (on shared triple-intersections ≥ 1 direction), does the
  composed correspondence agree with the direct one?  Violations
  are the deliverable, not a failure.
- **C4** the group census (only if non-identity transitions exist):
  the set of transition maps on 4-direction charts, closed under
  composition where defined — enumerate and name it (subgroup of
  S₄ × wire-relabelings, or whatever it is).
- **C5** controls: the same instrument on the sprinklings and the
  brick.  A transition structure that appears ONLY on the engineered
  substrate and never on sprinklings (or vice versa) is a first-class
  finding either way and must be reported with both columns.
- **C6** no invented thresholds; every census printed; exit 0 for
  substantive negatives, exit 1 only on C0.

## 4. Pre-registered outcomes (any is the result)

- **G1 (flat):** all transitions are identity — the wide crystal's
  atlas is globally trivializable at this labeling; the tensor seed
  is NOT in the delivery crystal, and the arbitration-crystal
  successor inherits the question.
- **G2 (obstruction):** non-identity transitions exist but the
  cocycle fails — the labeling does not glue; the failure pattern is
  the deliverable (it localizes where a finer chart notion is
  needed).
- **G3 (a G-structure):** non-identity transitions satisfying the
  cocycle — the atlas carries a genuine structure group; name it,
  and the tensor/curvature program has its object.

**Lean, stated in advance:** the double ring's inter-ring coupling
alternates direction with round parity, so chart neighborhoods at
even vs odd heights are NOT congruent; a non-identity wire
transposition at coupled wires is plausible (G2 or G3).  No outcome
sentence may exceed the measured census; "the group is X" requires
the closure computation, not an example.

## 5. Scope

Grammar layer; the swept substrates only.  No measure, no
typicality, no physical-object claim (#440).  Chart width is capped
at 4 by W4b on every delivery substrate — any tensor statement is a
width-≤ 4 statement and must say so.  Transfer to the identified
click law runs through the missing map (D59) and is not claimed.
The ends caveat (D63) applies to any band-membership sentence.
