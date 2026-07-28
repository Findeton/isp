# v7 — FROZEN RESEARCH LOG (2026-07-01)

This directory is the v7 research log, **frozen as of 2026-07-01** after the Phase-0 archive fixes
(see `../v8/LEDGER.md` §"Phase-0 fix log"). It is superseded by the **v8 consolidation**:

- The authoritative map of every result, receipt, status, and supersession is `../v8/LEDGER.md`.
- Corrections after this date land in v8 and the ledger **only** — not here. (The recurring failure
  mode this policy ends: receipt-level corrections silently desyncing from the papers that cite them.)
- Receipts in `code/` remain live and version-independent; v8 papers cite them directly.
- Known text-side items NOT fixed here (deferred to the v8 rewrite by design): paper 1's abstract
  premise-ledger, the σ/κ terminology unification, the orphaned-receipt homes, paper 18's fresh
  multi-referee review.

Caveats recorded after freeze (added 2026-07-27, v11 H1 erratum-routing unit; see the ledger's
corrections log):
- paper 30's receipt output at line 2833 (`max dual-conjugation error =
  1.8210207227600682556870097725525`) prints a **superseded** figure's status, not its value: the
  `1.82` is a closed-form constant of the ansatz, **not a measurement**. The downgrade is carried
  at `../v10/note-d72-weld-result.md` §5(a) (line 308): *"v7's `1.82` is a constant of the ansatz,
  not a measurement … The only information the `1.82` carries about the `N = 9` universe is that
  **some record has `E = 3`**. D71b Clause 2's 'strongest single piece of bridge evidence in the
  corpus' should be downgraded accordingly."* Recorded at `../v8/LEDGER.md` #498. (Note: d72 §5(a)
  cites the digits as `paper30:2838`; the receipt line is **2833** — 2838 is the corrected
  expression `L_dual = e^{-kE}e^{i\theta O}`.)
