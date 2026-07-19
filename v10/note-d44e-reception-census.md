# D44e (successor 5) — the per-type reception census

**Status:** CAMPAIGN PIN (strict), 2026-07-19.  Parents: the d42b4
terminal round's carried obligation (R6 second arm: "per-type census
a DECLARED carried obligation with the reason (carrier/data
structures differ) printed in the gate label"); D25 reception
theorem, D26 interface note, D27 Busch closure; d43c TERMINAL (#344,
whose R4 re-scope leaned on this obligation remaining open); the
LOG-pinned (actor,base) census-key upgrade.  Receipt:
`v10/code/d44e_reception_census_exact.py`.  Execution gated on
paper-31 terminal.

## 1. The question

The lift campaign gated ONE reception form (basis-copy records) and
declared the rest.  This unit delivers the COMPLETE census at
fixture scope: every record TYPE the (d42a + click + lift) layers
generate, each with its carrier set, its data structure, and its
reception form gated per NSE/D25/D27 — no shared-form shortcuts, no
declared-but-ungated types.  The census TABLE is the deliverable.

## 2. Type inventory (pinned as the enumeration frame; the receipt
## derives it from the grammar, it does not assume it)

From the event grammar: proposal records; arbitration records
(winner + created version); noop/idle (expected receptionless —
gate the expectation); click-chain intermediates (opening click;
acceptance — the d42b2 layer's record forms); version records
(genesis; arb-created; the (actor,base) key structure).  Transport
types (delivery records; merge records; merge-created versions) are
IN SCOPE at the SIG-chain fixture grain if runtime permits, else
declared with their carrier/data rows censused and their isometry
gates named as the residual (the declaration must be printed as its
own gate line, not a footnote).

## 3. Gates (pre-registered)

- **RG0 (completeness by construction):** the type inventory is
  DERIVED from the committed event grammar and gated against the
  enumerated family: every record instance in the depth-4 d42a
  family (and the click-layer fixtures) is an instance of exactly
  one censused type; zero unclassified instances; zero empty types
  (a censused type with no realized instance at the tested depths
  is printed as such).
- **RG1 (the carrier/data table):** per type: carrier set (per
  A1/A6), data structure (the exact tuple shape), and the
  (actor,base) census key [the pinned upgrade, executed here] —
  all EXACT, read from the layer, not hand-written.
- **RG2 (per-type reception gates):** for each type with a record
  side: the reception map's distinguishability-isometry gate on
  that type's OWN carrier/data structure (probe pairs from the
  enumerated instances; distances preserved at 1e-40 where
  amplitudes enter, exact where classical), PLUS a genuinely firing
  lossy control per type (the d42b4 convention: the control must
  fail the gate, proving the gate can fire).
- **RG3 (the d43c cross-check):** the constructed V_single/V_pair
  record sides re-derived as instances of the censused types (the
  operator family consumes/produces censused forms only — gated).
- **RG4 (honesty):** any type whose reception form CANNOT be gated
  at fixture scope (structure reachable only beyond caps) is its
  own printed gate line with the reason — the census is complete
  even where the gating is not, and the two completeness notions
  are kept distinct in the verdict.

## 4. Scope

Fixture scope (the committed depth-4 d42a family + the click-layer
fixtures + SIG-chain grains as declared); the D25/D27 theorems are
cited as the reception REQUIREMENTS, not re-proved.  Exact
arithmetic; mp.dps 50 / 1e-40 only where amplitudes enter.
