# w1 — the washout theorem hardened: churn growth forces D* → 0 (the discharge assembly's pillar two)

**Status:** theorem note, 2026-07-05 (v9 round 12). Receipt: `v9/code/w1_washout_intermediates.py` (gates pinned in §4, pre-run). Target grade this round: **[THEOREM-track: statement + proof skeleton with every measurable joint verified; the formal write-up = the assembly paper's job]**. The discharge chain this note serves: churn growth ⇒ dim ≤ 2 (DONE — Theorem U's support leg, constructive + the census set-equality, LEDGER #57–#58) ∧ **D*_N → 0** (this note) ⇒ volume-faithful, by paper 12's sufficiency theorem (volume-faithful ⟺ dim ≤ 2 + canonical D* ≤ 3ε) and paper 7's quantitative bridge (|r − ½| ≤ 12·(N/(N−1))·D*_N + 1/(2(N−1))).

## 1. The object and the statement

The churn web's canonical embedding is the rank pair `P_t = (t/N, rank(χ_t)/N)` for commits t = 1..N (paper 12's instrument; u1's `rank_embed2`). **Theorem W (statement).** For the churn class at fixed fleet M and lifetime L (j3 corner; D1; the kernel variant — any law whose slot choice, content increments, and resets read only the fleet state), the star discrepancy of the rank embedding vanishes almost surely,

  `D*_N → 0`, with rate `D*_N = O( sqrt( (τ_mix + log N) · log N / N ) )`, `τ_mix = O(L·M)`,

matching the measured q2 law `C(L, M) · sqrt(log N / N)` with `C` absorbing the mixing constant.

## 2. The proof skeleton (four lemmas)

**Lemma W1 (ergodicity of the fleet).** The fleet state (the M slots' accumulated contents and ages) is a Markov process; the reset mechanism (probability 1/L per own-commit) regenerates each slot geometrically, so the process has a stationary law and is uniformly geometrically ergodic with mixing time `τ_mix = O(L·M)` global commits (a slot is touched every ~M commits; its life ends after ~L touches; after every slot has regenerated once — coupon-collector `O(L·M·log M)`, and `O(LM)` for the correlation-decay version — the process forgets its start). *Geometric resets are exactly what kills slow variation: no χ value survives more than Geometric(1/L) touches.* [Standard regeneration-argument grade; the receipt measures τ_mix.]

**Lemma W2 (window-wise Glivenko–Cantelli — the key lemma).** Split the commit axis into K windows of length N/K ≫ τ_mix. Within each window, the empirical distribution of χ values converges to the SAME stationary marginal F (stationarity ⇒ same F per window; ergodicity + window length ≫ τ_mix ⇒ GC per window; the cold-start window differs by the O(τ_mix)-commit transient only). Hence the empirical joint law of `(t/N, χ_t)` converges to the product `Lebesgue × F`. [DKW-for-mixing-sequences grade; the receipt measures per-window KS distances and their N-decay.]

**Lemma W3 (ranks).** Applying the monotone map F (and then the empirical rank map, which converges to F uniformly by W2 pooled) sends the joint limit `Lebesgue × F` to `Lebesgue × Lebesgue` on the unit square: the rank embedding's empirical measure converges to uniform. Rank-vs-value substitution costs a uniform `o(1)` (GC pooled). [Deterministic given W2.]

**Lemma W4 (from measures to the sup-norm, with rate).** D* is the sup over anchored rectangles of the empirical-vs-uniform gap. A β-mixing empirical process indexed by rectangles (VC class, dimension 2) obeys the mixing-DKW bound: `D*_N ≤ c · sqrt( (τ_mix + log N) · log N / N )` with high probability. [Imported concentration grade — Rio/Doukhan-class; the receipt verifies the collapse at fixed (M, L); the L, M dependence is q2's measurement — which found C M-flat, so the √(L·M) bound is loose in M (disclosed).]

**Corollary (the discharge form).** W1–W4 + Theorem U (dim ≤ 2, by construction) + paper 12's sufficiency ⇒ churn growth produces volume-faithful webs in the limit, with the finite-N certificate `|r − ½| ≤ 14·D*_N + 1/(N−1)` (paper 7, for N ≥ 7) quantifying the approach.

## 3. The honest gap list (what the assembly paper must still do)

1. **W1's constant**: the `O(LM)` mixing time is regeneration-heuristic here; the formal version needs a drift/minorization argument (standard machinery, not yet written). The receipt *measures* τ_mix's L·M scaling.
2. **W2 across the growing axis**: the process is not started at stationarity; the cold-start transient must be shown `O(τ_mix)` in total-variation contribution (the receipt measures it).
3. **W4's import**: the mixing-DKW constant for VC-2 rectangle classes is imported, not re-proved; the citation and its conditions (β-mixing with geometric rate — supplied by W1) go into the assembly paper.
4. **The stationary marginal F is continuous** (no atoms — needed for W3's rank map): true for continuous increments (route B); the atoms arm FAILS this hypothesis — consistent with the atoms pathology (TV 0.5694): **Theorem W's hypothesis excludes the atomic corner by construction, and honestly so.**
5. Theorem W is a *law-class* statement at fixed (M, L); the physical reading (fleets and lifetimes from the derived supply) inherits paper 16's parameter ledger.

## 4. Receipt w1 — the measurable joints, gates pinned

Instruments: u1's `star_disc`/`rank_embed2` verbatim; the s8-ported `web_j3`. Seed `default_rng(20260719)`. Float64 (measurement landscapes; no near-vacuum quantities). M = 32, L = 2 primary; the L, M sweeps as marked.

- **V1 (window GC, Lemma W2):** N = 4096, K = 8 windows: per-window KS distance of χ-values against the pooled df, 6 reps. Pinned: mean per-window KS at N = 4096 < 2× the iid reference `sqrt(ln(2/α)·K/(2N))`-scale benchmark measured on L = 1 (the singleton control, same instrument); and the window-KS mean decays with N across {1024, 4096} by ≥ 1.5× (the √-law expectation ≈ 2×).
- **V2 (mixing time, Lemma W1):** the lag-autocorrelation of the slot-content functional (mean fleet χ) at N = 8192: the fitted e-folding lag τ̂ scales with L·M across (L, M) ∈ {(2,32), (4,32), (2,64)} — pinned: τ̂(4,32)/τ̂(2,32) ∈ [1.4, 3.0] and τ̂(2,64)/τ̂(2,32) ∈ [1.4, 3.0] (the ×2 predictions with generous bands, 6 reps each, [directional]).
- **V3 (the rate law, Lemma W4):** D*·sqrt(N/log N) flat across N ∈ {512, 1024, 2048, 4096} (re-verifying q2 on this stream): pinned max/min ≤ 1.35 over the N-range (q2's measured flatness band), 6 reps per N.
- **V4 (cold start, gap 2):** D* computed on the first W commits vs a stationary window of the same length (W ∈ {64, 256, 1024} at N = 8192): pinned — the cold/stationary ratio exceeds 1.15 only at W ≲ 4·L·M and is ≤ 1.15 at W = 1024 (the transient is O(τ_mix), 6 reps).
- **V5 (the discharge certificate, paper 7's bridge):** at N = 4096, `|r − ½|` measured ≤ `14·D* + 1/(N−1)` on every rep (the inequality is a theorem — this is an instrument-integrity check, must hold 6/6).

Refusals print the ledger and exit 1 by design; [directional] tags on the 6-rep band reads.

## 5. First-run refusals, diagnosis, and amended pins (2026-07-05 — recorded per the house convention; the first-run ledger stands)

**First run: V1 HELD (the key lemma — window-KS 0.0392 = the L = 1 control's 0.0391, decay 1.90× ≈ the √-law's 2×), V5 HELD 6/6 (worst ratio 0.070 — the bridge is slack by 14×), V2/V3/V4 REFUSED.** Diagnosis before any verdict prose:

- **V2 (instrument bug, not physics):** the receipt measured the *committed-output* series χ_t — consecutive commits hit different slots, so the output series is near-white (τ̂ = 1 at every (L, M): the failure is exact and diagnostic). The note's Lemma W1 functional is the **fleet state**; the amended receipt measures the fleet-total series Σ_slots χ_acc(t) (a genuine Markov functional whose relaxation is the content-replacement time ≈ L·M). Same pinned bands.
- **V3 (the transient contaminates the small-N end):** the collapse declines monotonically (0.335 → 0.242), exactly what an O(L·M·log M) cold-start segment does to N = 512 (it is ~40% of the series there, ~5% at 4096). Theorem W's statement is about the stationary process; gap 2 handles cold start separately. Amended pin: the collapse is computed on **stationary-start segments** (trim 4·L·M = 256 commits before measuring; disclosed), same 1.35 band.
- **V4 (pin mis-calibrated — the honest diagnosis, corrected by the round-12 review m1):** the first-run full row was **1.031 / 1.144 / 1.153** at W = 64/256/1024 (the small-W values, initially under-quoted here — review M3 — show no elevation at W = 64, already a hint the 6-rep read was noise-grade). The first amendment's "log M factor" story was arithmetically specious (L·M·ln M ≈ 222 < the original pin's own 4·L·M = 256 — it could not explain the miss); the pin's true defect was the unexamined contamination→excess constant (measured ≈ 0.7) and, deeper, that the statistic carries ±0.1-class noise at 6–12 reps — the review's replication showed BOTH the original refusal (margin 0.003) and the first amended pass to be seed-grade. **Third-form pin (review M1's prescription): 48 reps, mean ± SE printed, [directional]; gate = ratio(4096) − 1 ≤ 3·SE ∧ interior peak; and gap 2's PRIMARY evidence is re-assigned to the V3 untrimmed-vs-trimmed contrast (receipted as V4b), which is seed-robust per the review's own replication.** Third-run result: profile 1.141±0.045 / 1.250±0.049 / 1.124±0.048 / 1.024±0.042 — peak interior at the transient scale, terminal ratio within errors of 1; V4b contrast 1.340 vs 1.254.

The amendments change no theorem statement; they align the instruments with the objects the lemmas actually name (W1: the fleet, not the output; W4: the stationary law; gap 2: the log M factor now stated in §2's Lemma W1).

## References

v8 paper 16 (§2 the washout theorems — the τ-decay this note extends to the sup-norm; §4 the cell; the renewal ledger); v8 paper 12 (the sufficiency theorem; the canonical instrument); v8 paper 7 (§II the discrepancy–r bridge, the exact constants); q2/note-q2 (the measured rate law C(L,M)·√(logN/N)); u1 (`star_disc`, `rank_embed2` — the instruments, verbatim); LEDGER #57–#58 (Theorem U's census half); u4b/LEDGER #59–#60 (the ensemble leg; the L-sweep this note's W1 explains); Dvoretzky–Kiefer–Wolfowitz (1956); P. Doukhan, *Mixing* (1994) / E. Rio (2000) — the W4 import class; W. Hoeffding (1948).
