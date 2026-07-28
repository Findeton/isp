# v6 — FROZEN RESEARCH LOG (2026-07-01)

This directory is the v6 research log, **frozen as of 2026-07-01**. It is superseded by the **v8
consolidation**; the authoritative result/receipt/status map is `../v8/LEDGER.md`.

Caveats recorded at freeze time (see the ledger's corrections log):
- The 2026-06-16 Renou/meta-result retirement was propagated through v7 but **v6 was not swept** —
  any v6 line asserting "Renou ruled out real QM" or the "three experiment-fixed inputs" is stale.
- paper56's [TARGET] "decoherence rate = seal rate = σ" was **dissolved** (2026-06-17: the quarter
  law −ln BC = σ/4 = paper26 Thm A; κ=1 only for the mutual-information measure). The v6 file does
  not record this; the ledger and v8 paper 6 do.
- paper10's T3 is a dissolution (not an RP-theorem), per paper10's own reclassification.
- paper26's Theorem A holds under a hypothesis it does not state: the coherence multiplier is
  `BC` only when the relative pointer phase is constant across the record alphabet, `BC` being
  the Cauchy-Schwarz bound in general (paper 7 §12 item B1, "Duality law, CORRECTED"). Routed
  in `ERRATA.md` E2; `../v8/LEDGER.md` #498.
Corrections after this date land in v8 and the ledger only.
