# D44c (successor 3) — the multi-author-arbitration dimension corner

**Status:** CAMPAIGN PIN (strict), 2026-07-19.  Parents: d43d
TERMINAL (#342: transport generates dimension at actor-width >= 4;
the untested corner PROVABLY MINIMAL — vname-recurrence mechanically
vacuous, so "multi-author arbitrations" is exactly the residual
scope); the d42a admission layer; the ported g2 oracle + exact D*.
Receipt: `v10/code/d44c_arb_dimension_exact.py`.  Execution gated on
paper-31 terminal.

## 1. The question

Can ARBITRATION STRUCTURE ALONE — no deliveries, no merges — push a
generated event poset out of dimension <= 2?  "Multi-author" means
the channel d43d left open: r-events over pools spanning >= 2
proposers (the wkey-authors structure), at actor widths 3..6.
Pre-registered OPEN; either answer is a result:

- a WITNESS: an admissible p/r/n-only configuration whose event
  poset fails dim <= 2 — arbitration is a SECOND dimension
  mechanism, and S4's "transport generates dimension" widens to
  "transport or cross-authored arbitration";
- an OBSTRUCTION: a structural argument (gated mechanically at the
  tested widths) that arb predecessor structure cannot realize the
  crown — transport's mechanism status sharpens toward uniqueness.

## 2. The structural fork (pinned before the run)

The three-crown S3 needs three mid-elements each covering exactly
two of three pairwise-incomparable minimal elements.  Arb events
naturally cover their pool's proposals — cover-two structure is
native.  The obstruction candidate is the COMPONENT LAW: three
mutually conflicting live proposals on one base form ONE component
of size 3 (not three pairs), and an arb consumes its component,
so realizing three DISTINCT pair-covering arbs may be inadmissible
by construction.  Whether value-bit structure (conflict edges exist
only between equal-base, unequal-bit proposals), multi-base layouts,
or supersession timing evade the component law is exactly what the
receipt must decide.  Both horns are pre-registered; the receipt
delivers whichever the enumeration proves.

## 3. Gates (pre-registered)

- **AG0 (port re-anchor):** the g2 oracle + exact D* re-anchored
  (S3 rejected; 219/4,231 all-pass; W6 regression = S3, fails
  dim <= 2) before new content.
- **AG1 (exhaustive small widths):** ALL admissible p/r/n
  configurations at width 3 to the declared event cap (>= 8 events
  if runtime permits; cap printed): dim <= 2 verdict each; count
  censused.  Any failure is a witness and stops the hunt.
- **AG2 (guided width 4..6):** constructor search over admissible
  configurations with >= 2 cross-authored arbs (multi-base layouts
  included; every candidate admission-checked event-by-event with
  exact weights, the SIG-chain convention): first dim > 2 witness
  gated with its poset, weights, and the S3-embedding exhibited —
  or the search space censused and exhausted at the declared caps.
- **AG3 (the component-law theorem test):** the pinned obstruction
  candidate made mechanical: gate whether every admissible
  arb-containing poset at the tested scales has its incomparability
  structure confined by component consumption (the exact confinement
  statement to be fixed from AG1's data and gated at AG2's scales —
  the statement is the deliverable if no witness exists).
- **AG4 (width discipline):** the d43d width diagnostic on every
  candidate (no width-blind repeats: a dim <= 2 pass at width <= 2
  is a theorem, not evidence).
- **AG5 (honest floor):** the n < 6 vacuity re-cited; no
  manifoldlikeness claims; descriptors labeled MEASURED.

## 4. Scope

p/r/n events only (the d42a layer; transport events excluded by
construction — that mechanism is S4's, already decided).  Widths
3..6, caps declared and printed.  Exact Fractions; the oracle exact.

## 5. First-run amendments (2026-07-19, pre-round; the receipt's
## declared deviations, owned as pin gaps)

**A1 (AG1 cap 6, not 8).** Measured growth ~9.0x/level
(9/75/639/5,865/54,489/490,851; depth 7 ~ 4.4M ~ 45 min enumeration
alone). Declared in-receipt with the table; compensated by the
declared exhaustive subfamilies AG1b (no-idle width 3, depth 7;
depth 8 declined and declared) and AG2b (no-idle width 4, depth 6).

**A2 (register-word dim-dedup).** Dimension checked once per
actor-register-word class; sound because vname registers are
single-writer (the law's clause (v)) hence pred-inert; soundness
re-sampled every 97th arb-containing history against the full
committed builder (11,664 recomputations, zero mismatches); both
canon() and label-level censuses printed.

**A3 (AG2c single-universe design).** The main F-CROSS sweep runs
the 6-actor universe over all 840 ordered overlapping non-nested
pool pairs, subsuming width 3..5 patterns via the mechanical
universe-independence of the committed 2-arg admissible(); gated by
the width-3 dual-universe re-run (the 'global' context excluded from
the identity gate — universe-dependent by content). The at-state
candidates_for census runs on non-interleaved states only
(interleaved states are per-pair; their crossing potential IS the
Y-attempt) — declared.

**A4 (constructed arbs).** AG2 candidates built via admissible()
with the full wkey-subset sweep (the pin's SIG-chain convention);
lex-min connected bit rule declared (wkey/bits never affect holders
or the poset); full bit sweep at width 4 (1,920 attempts).

**A5 (F-LAM caps).** Laminar layouts capped at <= 3 pools, sizes
{2, 3, w-root}, n <= 14; dim/width memoized by exact C-matrix
equality (no symmetry assumption).

**A6 (AG0b).** The LOG #348-assigned d43d print repair executed by
REPRODUCING the full NG2 computation in this receipt (below = 8,
wsum = 1037/64, ratio = 512/1037 ~ 0.4937; all committed anchors
exact); the terminal d43d receipt untouched.
