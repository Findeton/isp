# 3p1-openings — the openings pass: the reserved review's leftovers + all why-C=3 routes

**Status:** design note, 2026-07-06 (committed 2026-07-09) (v9 round 35). Receipt: `v9/code/openings_pass.py` (pinned strictly before). **REVIEWS RESTORED — this receipt's results feed paper 6 BEFORE its review.**

## Parts (all measured; directional registrations noted)

- **A (MM association-dependence, MAJOR-2 formalized):** d_MM(C = 3 windowed) vs the channel-shuffled control (marginals kept) — one pinned row, 3 seeds (the referee's 4.04-vs-3.4 gap, receipt-carried).
- **B (witness density):** an in-repo randomized S4 searcher (validated against iid 4-orthant/3-orthant positives/negatives in-receipt); hit-rate over 10 window draws x 5 seeds at C = 3 — a LOWER bound (searcher power disclosed).
- **C (the frozen reference):** the M2..M5 fractions computed once and committed as `v9/data/mm_reference.json`; future receipts load it (the byte-stability fix).
- **O1 (the capacity ceiling's scale law) [directional: ceiling grows ~ log n]:** viability (corr < 0.25, volume within 2x of the (C+1)-orthant anchor at matched n, realizer refusal) at the pinned alpha = 0.75, per-channel churn, for C in {4..8} x observation size n in {96, 144, 216}. The ceiling C*(n) = the largest viable C. If C* grows with n: the capacity route predicts d_max ~ log(observable record count) — no constant selection, a LAW instead.
- **O2 (comparability percolation — the seal-topology route's core) [directional: threshold grows ~ log N]:** the largest weakly-connected component of the comparability graph, full webs, C in {2..9} x N in {1024, 2048, 4096}; the disconnection threshold C*_perc(N).
- **Disclosed, designed-not-run:** utility/energetic-cost selection functionals — any such functional risks smuggling the answer through its own choice (the mode-import analog); ledgered for a future user decision.

## References
LEDGER #89 (the openings), #90 (the environmental ending + undesigned routes), #92 (the band mis-pin lesson: anchors measured at matched n, in-receipt).

## Round-35 correction (the paper-6 hostile review, NIT-2 — appended, not silently edited)

The final Parts bullet's "Disclosed, designed-not-run" misstates the record: no such design exists in any artifact — read "undesigned by choice, ledgered" (the paper's and the receipt-1 LOG entry's wording, now tidied there too). The bullet above is left as committed; this section is the correction.
