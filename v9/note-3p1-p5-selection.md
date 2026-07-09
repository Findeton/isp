# 3p1-p5 — the selection question: why C = 3?

**Status:** design note, 2026-07-06 (v9 round 31, batch item v). Receipt: `v9/code/dimwall_selection.py` (pinned here, committed strictly before the receipt). **NO-REVIEW MODE on record. A mapping receipt: verdict CLASSES pinned, not numeric predictions — we have none, and pretending otherwise would be theater. The honest risk, stated: the likely outcome relocates the question to the dials (the Newton-G pattern); the wildcard is a genuine band-closure.**

## Receipt (b): the viability-band closure

For C = 2..6, alpha in {0.5, 0.6, 0.7, 0.8, 0.9, 0.95} (pinned-class webs otherwise: per-channel churn, round-robin prefs, 3 seeds): a cell is VIABLE iff (i) channel-corr < 0.25; (ii) the Delta = 512 windowed fraction is within 2x of the measured (C+1)-orthant anchor at N = 128 (|log2 ratio| <= 1); (iii) the 2-realizer refuses (dim > 2) — (iii) run only on cells passing (i)+(ii) (cost; disclosed). Band width at C = the count of viable alphas (majority over seeds). **Classes: BAND-CLOSES-AT(C*) (width 0 at C* <= 6, nonzero at C* - 1) / BAND-PERSISTS (width >= 1 through C = 6) / NO-BAND.**

## Receipt (a): channel-survival dynamics

C_max = 8 symmetric potential channels; deposits by reinforcement P(k | slot c) prop acc[c, k] + eta (eta in {0.005, 0.05, 0.5} absolute evidence units); per-channel churn; L in {8, 16, 32}; N = 4096 (equilibration), 3 seeds; C_max = 5 spot at center dials. Measured in the last Delta = 512 window: global deposit shares -> C_eff = 1/sum p_k^2; the windowed d_MM (dead channels freeze to near-constant coordinates and drop out of dominance automatically — the dial reads surviving + 1). **Classes: SELECTS (C_eff within +-0.5 of one value across the whole dial grid AND C_max-independent) / DIAL-TRACKING (C_eff spans > 1.5x across dials) / COLLAPSE (C_eff <= 2 everywhere).**

## The adjudication map

BAND-CLOSES-AT(4ish) or SELECTS(3ish) => a genuine selection mechanism (the wildcard — would warrant the next reserved review when budget allows). DIAL-TRACKING and/or BAND-PERSISTS => **C is an input; the framework predicts the LAW d = C + 1, not the constant 4** — the honest ending, same class as the G no-go and the free parity bit; paper 6 states it plainly. Exit 1 only on instrument failure.

## References

r24/r25 (the interior-optimum law — the band's existence at C = 3); r29/r30 (the windowed instrument + the graded d = C + 1 law); LEDGER #83–#89; the G no-go (paper 57) and the parity lean-free (LEDGER #81) as the relocation precedents.
