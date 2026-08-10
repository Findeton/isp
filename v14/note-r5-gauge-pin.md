# R5 — THE GAUGE RUNG (paper-18) — PIN (FROZEN)

**Frozen:** 2026-08-10, v14 ledger #129.  **Parents (both
terminal):** R4 (#103; paper `1063401c7bb5`, code
`2959c5a6a84b`, receipt `3dc1393b0df8`, commit 583cae7) and R4b
(#128; paper `89c636906061`, receipt `562e2a3d4d85`, commit
6d32993).  **Authority for the design:** the frozen R4 effectus
review's R5 recommendation (v14/review-r4-effectus.md, "THE R5
RECOMMENDATION" through "What R5 must not do") — G1–G7 lifted
below verbatim-in-structure; the R4 adjudication §2
(`3b00a9481b28`).  **Unit:** paper-18-gauge-rung; code
v14/code/r5_gauge_exact.py (+ output + receipt).

## THE OPENING DATUM (stated first, per the ruling)

R4's verdict-bearing stratum is ABELIAN: 0 of 3,364 commutators
nonzero; every plaquette holonomy and Wilson loop is the
identity BY THEOREM; the only non-commuting generators on the
stage are the 4 brickwork generators — exactly the ones R4's
mandatory realization gate excludes.  A gauge rung built on
R4's FULL stratum is pre-committed to flat abelian holonomy and
could not be falsified.  R5 therefore builds on the EXCLUDED
sub-maximal stratum, with FULL as the provably-flat negative
control.

## THE ARENA (declared as data, §15)

Link-indexed unitaries on the L=4 torus: a coin per link (32
links, 16 plaquettes), from a DECLARED coin alphabet, applied
in declared parity strata (the brickwork/Floquet shape,
generalised so the coin may vary link to link).  Boundary =
(Z₄)² with its links and plaquettes; law = Barandes' Γ = |Θ|∘²;
state = single occupation, with ONE declared two-excitation
extension pre-registered (G3); the order-32 chart group and
order-128 extension censused per R4.  The connective clause
inherited verbatim
(CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))).  The R4b
handoffs carried: NOT-BLOCH-DIAGONAL is a THEOREM (index-two
stabiliser) for the brickwork classes; NO transport number is
inherited from R4b (single-occupation uniform-average scope).

## THE QUESTION

Does the declaration-connection on the record stage carry a
NON-ABELIAN holonomy group, does it survive one refinement
step, and does its curvature couple to Δᴮ?

## THE GATES (G1–G7, lifted)

- **G1 — NON-ABELIAN NON-VACUITY (decisive):** the
  plaquette-holonomy group MEASURED; its commutator subgroup
  gated nontrivial; the group reported as an ISOMORPHISM CLASS
  with rank, never as matrices.  R4's FULL stratum is the
  MANDATORY NEGATIVE control and must return the trivial group.
- **G2 — GATE-INHERITANCE AUDIT (binding):** the
  realization-census gate may NOT be inherited unmodified; R5
  states at construction whether "maximal declared transport"
  is compatible with non-abelian holonomy ON ITS ARENA and
  censuses which transport level each link-local generator
  attains.  If the maximal level again selects a commuting
  sub-family: `R5-BLOCKED-AT-THE-GATE` — first-class.
- **G3 — CURVATURE ⟺ DEFECT AT MATCHED COORDINATES (§15):**
  nonzero plaquette commutator vs nonzero Δᴮ across the same
  cut, all coordinates held equal; the matched table primary.
  Three outcomes pre-registered: CURVATURE-CARRIES-DEFECT /
  CURVATURE-DEFECT-INDEPENDENT / DEFECT-WITHOUT-CURVATURE (R4
  supplies the third as the measured baseline: 588 defects at
  identically zero curvature).
- **G4 — GAUGE SELF-TEST BOTH DIRECTIONS:** site-diagonal gauge
  action; Wilson traces invariant; a declared handle that moves
  the untraced holonomy at every checked loop; holonomy enters
  claims only as a conjugacy class.  R4's projective-period
  self-test cited as the template.
- **G5 — DECLARATION SEGMENTS:** CONNECTIVE, LINK-SET/STENCIL,
  SECTOR, SWEPT-RANGE, INDIVISIBILITY=DECLARED|MEASURED as
  explicit segments; any quantity not gated invariant across
  the declared free axes entered arena-relative or not at all.
- **G6 — REFINEMENT (the charter's question):** the holonomy
  group at L=4 vs the declared doubling to L=8 (or a declared
  window with pinned precedent if the doubling is infeasible —
  disclosed, never silent); the ISOMORPHISM CLASS is the
  invariant, the plaquette count the extensive control;
  NO-STABLE-GROUP first-class; the group reported against
  CR-D's ladder (the programme's group-family prior).
- **G7 — THE SCRAMBLE CAVEAT (inherited from Γ-main):** the
  holonomy group must SEPARATE the physical case from a
  scrambled control before any group-theoretic claim is
  entered.

## MUST-NOTS (lifted verbatim-in-substance)

No confinement-analog language before G1 passes.  No silent
inheritance of the maximal-transport gate.  No matrix-valued
holonomy reported as physics.  No claim that curvature implies
quantum character (R4's 588-at-zero-curvature settles the
implication negative on this stage).

## STANDARDS AT CONSTRUCTION

Full era: the #82 CLI; the head DERIVED independently; #87
per-object gates (per-plaquette, per-link-generator); **the
gate-to-disk SEAL from birth (#119)**; text gates
whitespace-normalised (#125); #91 off-tree/git-less tested;
#24; #34 (no cannot-fail gates without waivers-with-forcings);
#62 with the length floor; verify-paper in-run with polarity;
failing runs write nothing; exact arithmetic; byte ×2.
Outcomes: `R5-NON-ABELIAN-<class;rank;refinement>` /
`R5-BLOCKED-AT-THE-GATE` / `R5-NO-STABLE-GROUP` /
`R5-BLOCKED-AT-<object>`, with the G3 segment and the G5
declaration segments.  Between delivery and adjudication every
headline reading is a candidate reading.
