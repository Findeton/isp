# SIG (paper-24) — WHY LORENTZIAN: SIGNATURE SELECTION — PIN (FROZEN)

**Frozen:** 2026-08-11, v14 ledger #233.  **Authority:** THE
STRATEGIC PLAN (#193, Wave A) + TWO BINDING PANEL CONSTRAINTS
adopted before this pin: **(A) REACHABILITY BEFORE POLARITY**
(the paper-21 adjudication #211: at R=4 det ≥ 0 is forced by
arithmetic — the floors are R=5 statically, R=8 for G-INDEF,
horizon ≥ 6 dynamically; a polarity verdict about an
unreachable region is forbidden); **(B) NO SITE-MARGINAL
OBSERVABLES** (the GDL effectus #224: any block-diagonal coin
makes the site marginal record-blind by theorem — SIG's
observables must be off-diagonal or record-reading).
**Parents (terminal):** paper-21 at #232 (paper ef4a8c35a0c4:
the R=4 covering machinery, the det spectrum, block
quantisation, the R=6 door) and paper-20 at #204 (the coupled
machine, the coin fiber, the exit census).  **Unit:**
paper-24-sig; code v14/code/sig_exact.py (+ output +
receipt).

## THE QUESTION

Does the coupled dynamics SELECT, AVOID, or remain NEUTRAL
toward the indefinite-signature region of record space — or
is the region unreachable at every honest parameter choice?

## THE STAGES (reachability first, by order A)

1. **STAGE 0 — THE REACHABILITY CENSUS (gates everything):**
   at each candidate arena (the R=3 welded record; the R=4
   G-FLAT record; the R=5 stratum; horizons 5–8 as feasible,
   windows declared), compute EXACTLY which det values /
   signature classes are reachable (a) statically (which
   records exist in the stratum) and (b) dynamically (which
   the coupled walk's emissions can produce from the declared
   start).  **If the indefinite region is unreachable at
   every declared parameter set, the head is
   SIG-BLOCKED-AT-REACHABILITY with the floor census — a
   first-class outcome; no polarity sentence may be
   emitted.**
2. **STAGE 1 — THE ARENA THAT CLEARS THE FLOORS:** the
   cheapest declared (arena, horizon) pair whose reachability
   census shows the indefinite region live on BOTH arms or
   demonstrably on the coupled arm (the floors from #211 are
   the starting candidates, not assumptions — they are
   VERIFIED in Stage 0).
3. **STAGE 2 — THE POLARITY CENSUS:** on the clearing arena,
   the exact exit/occupation probabilities of the three
   regions (posdef / singular boundary / indefinite), per
   step, per branch class — with observables obeying
   constraint B; the Born and record readings both carried.
4. **STAGE 3 — FORCEDNESS:** the polarity signature censused
   across the coin fiber (the paper-20 witnesses); the frozen
   control carries only the static half (stated).  A
   selection invariant across the fiber is
   FORCED-AT-THIS-ARENA; else coin-relative, priced.

## OUTCOMES (pre-registered)

`SIG-SELECTED-<region;numbers>` / `SIG-AVOIDED-<numbers>` /
`SIG-NEUTRAL` / `SIG-BLOCKED-AT-REACHABILITY-<the floor
census>` / `SIG-BLOCKED-AT-<object>` — every polarity word
conditional on Stage 0's license.

## STANDARDS

The full era per HANDOFF-PROMPT.md §4 + E-22 + E-23 + E-24;
exact arithmetic; description-stamps; the four walls (NO
cosmological reading of signature selection); windows
declared and licensed; the derived+rendered head; the total
seal; failing runs write nothing; byte ×2.  Candidate
readings until adjudication.
