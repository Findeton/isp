# D57 — the SECTOR-EXACT question (PIN)

**Status:** PIN, STRICT, 2026-07-26.  Parents: B1/D56 probe (#432,
verified: NO bounded MENU-exact abstraction exists at transport scope
— the self-arbitration ladder makes menu cardinality and per-option
weights unbounded), D50 (the record-level observables are AGGREGATED),
my verified in-layer observation that the delivery-sector TOTAL is
constant 1/4 at every ladder rung.

## 1. The question

The ladder kills PER-OPTION exactness.  It does not touch SECTOR
aggregation.  **Does a FINITE sector-exact abstraction exist at
transport scope?**  Formally: the COARSEST partition R of histories
such that equal-class histories agree, for every sector s = (actor,
event-type) and every class c, on the aggregated transfer
`T_s(h, c) = Σ{ q(e|h) : e ∈ s, class(h+e) = c }`.
This is coarsest sector-lumpability (aggregated probabilistic
bisimulation).  If R is finite, the Perron/completion machinery
reopens at transport scope in sector-aggregated form; if even the
COARSEST such partition blows up, sector-exactness dies too — a
strictly stronger negative than B1's (which killed one granularity).

## 2. Pre-registrations

- **SECTOR QUANTIZATION [expected TRUE, gated first]:** every
  sector total is 0 or exactly 1/4 (verified at delivery rungs;
  to be gated across the whole family, all five event types).
  If true, sector signatures are finite alphabet — necessary for
  any finite R.
- **THE MAIN QUESTION [lean: BLOW-UP, weakly].**  For: the probe's
  delivery-lumped attempt still failed to close, with the residual
  explosion in per-view knowledge lag, and knowledge-lag classes
  plausibly bleed into successor-class distinctions.  Against: the
  coarsest object has never been computed, and lumping successor
  classes (not just options) is genuinely coarser than anything
  tried.  Both outcomes are first-class deliverables.

## 3. Method + decision rule

Exhaustive 2-actor family at caps 3, 4, 5 (6 if feasible; caps
printed).  Fixpoint refinement from the sector-signature partition;
cap layer closed by signature (declared boundary treatment).  The
DECIDER: per-depth class counts of the fixpoint, compared ACROSS
caps — cap-stable counts at matched depths = closure evidence
(then a direct BFS attempt); growing = blow-up, reported with the
component census (which distinction drives growth).  Exact
Fractions; no silent caps; witness pair printed for the first
refinement at each iteration.
