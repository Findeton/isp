# u-line results memo — design note 8 executed through G0/G1 and the G2 pilot

**Status:** results memo, 2026-07-04. Receipts `u1` (5/5), `u2` (10/10), `u3` (8/8), all on `default_rng(20260703)`, all runnable verbatim against the j1/j3/j2/i2 machinery in `v8/code/`. Gate discipline: pre-registered predictions recorded in receipt docstrings before first execution; gates marked [pinned-post-exploration] set from the disclosed same-date single exploration pass (note 8 §4's pre-authorization); two main-loop corrections and one refuted prediction recorded below, not silently rewritten.

## 1. G0 — the positive control [u1, 5/5]

The instrument stack reproduces on a fresh stream (pooled band `0.0271 ± 0.0044` at N = 512, inside paper 13's `0.0263 ± 0.0047`). The trivial-Φ endpoint reproduces paper 16 §4's cell membership at N = 2048 on all three layers, and — the check u2 actually needed — the **uniform-victim growth kernel** (churn events at rate 1/L per commit, victim uniform) is itself in the corner's range (`1.32×`, z = 2.4 at N = 2048), with the kernel-equivalence identity measured (`L_eff = 1.86` vs L = 2). Disclosure: the strict corner came in at `1.60×` at N = 512 on this stream, above paper 16's quoted 1.2–1.5×; the N = 2048 headline (1.18×) reproduces cleanly, and the N-dependence reappears as signal in §3.

## 2. G1 — growth vs equilibrium [u2, 10/10]

**The telescope lemma [DERIVED, one line, load-bearing].** Under irreversible growth every element is maximal at arrival, so a related pair's interval is complete when its top element lands and its action charge never changes: `S` telescopes exactly over arrivals (CHECK 1 verifies to 1e-6 against j2's `action()` verbatim). The misfit-increment functional of note 8 §3(a) is therefore exact and cheap — no surrogate was needed, and the growth mode is a *cheaper* test bench for action-family work than equilibrium search.

**The pre-registered prediction held at full strength.** The bare r+link action's global minimum is degenerate — `S(antichain) = 0` identically, since both terms charge only related pairs — and growth finds it: at n = 64, β = 1 already collapses to `r = 0.059`, β* = 16 ln 2 gives a near-antichain, and β = ∞ reaches the **literal antichain** (`S = 0.000, r = 0.000, H = 1`). The G1 trichotomy resolves to the third outcome: **no ESCAPE, no CAPTURE, sparse PATHOLOGY** — and no arm anywhere on the grid reproduces j2's dense attractor. The kernel ablation (empty candidate removed) does not rescue it (`r = 0.017`): the pull is the action's.

**The structural claim this buys, stated once:** the two sampling modes fail in *opposite directions* — equilibrium parks at the dense compromise (`r ≈ 0.78`, the kernel's densification moderated by the action, j2), growth falls into the sparse degeneracy (the action's own minimum, unmoderated because monotone growth carries no rearrangement entropy). The missing comparability/abundance term is now localized **from both sides**: any action that is to select geometry under *any* sampling mode must charge under-comparability (faithful orders have `r → ½` with Θ(N²) related pairs), and paper 13 §3's "measured attractor to beat" acquires a sparse twin. This is the sharpest available specification for the abundance-term extension paper 11 named — and the telescope makes growth the cheap place to test it.

**Arm B — the first β_v > 0 selection signal [directional].** In the record-native frame (victim-selection over the u1-validated kernel), kill-the-leader improves **every** layer over uniform at N = 512: D* `1.50× → 1.29×`, |ρ| `0.122 → 0.057`, dispersion z `1.9 → 0.6`. Magnitude ~1 band-sd on D* at 6 seeds — directional grade, certification retest named.

**Main-loop correction (G3).** The note's "endogenous L" over-claimed for fixed-event-rate laws: with churn events at rate 1/L per commit, the *mean* lifetime is budget-pinned by accounting (`E[L_eff] ≈ L/(1 + LM/N)`; measured 1.73 and 1.92 against the identity's 1.78) for **every** victim law. The victim law shapes the lifetime *distribution* at fixed mean. Rate-level endogenization is a different, C1-adjacent design — deferred and named.

## 3. G2 pilot — the determinism axis [u3, 8/8]

**Placement determinism (D1) is not just invisible — it is beneficial.** Kill-the-oldest (fully deterministic victim) concentrates the lifetime law (sd `2.13 → 1.41`; P3 held) and *improves* all three layers at N = 512 (`1.72× → 1.15×`, |ρ| `0.132 → 0.048`, dispersion z `+5.0 → +1.3`). On the rich 128-atom menu at N = 1024, **D1+atoms reaches the band itself: `0.96×`, z = −1.3** — the closest approach to ratio 1.0 measured in the corner family so far [directional, 4 seeds].

Two identifications ride this. First, the corner's dispersion excess is larger at N = 512 (+5.0) than at N = 2048 (+2.4, u1) — a finite-N staircase, consistent with paper 16's reading. Second, and more useful: **the staircase residual is lifetime-tail-driven** — concentrating the lifetime distribution cures most of it. Paper 16's named `z_comb = +2.3` residual now has a *law-shaped* fix candidate rather than a tuning: a placement law with sub-geometric lifetime tails.

**Sequencing determinism (D2) is marginal-visible but geometry-laundered.** Both tested deterministic committers deviate from the race's `Geometric(1/M)` sequencing marginal by ≫ 5× the calibration distance (round-robin 0.63, argmin-χ 0.23, calibration 0.007; powered gate). But geometrically:

**P1 REFUTED — recorded, with the mechanism found.** The prediction (argmin-χ water-filling rebuilds the clock correlation, ρ → +1) was wrong at the churn corner: measured ρ = +0.06, web band-adjacent at 1.29×. The mechanism control explains it: a freshly reset slot *is* the argmin and monopolizes commits during catch-up, sweeping χ across [0, level] — **churn launders the lockstep**. Remove churn and P1's mechanism is real: ρ rises monotonically along the laundering axis, `+0.15 (L = 2) → +0.49 (L = 8) → +0.98 (no churn)` — the O1 obstruction reborn exactly as reasoned, but only where churn is absent. The same churn that cures O1 (paper 16) also launders a determinized committer. Geometric visibility of sequencing determinism is controlled by L, not by determinism per se.

**Where the G2 conjecture now stands, honestly:** every tested arm retained at least one random layer (event timing, content, or the race), so the note's strict conjecture — irreducible click randomness is *necessary* for Poisson-typicality — is **untested in its strict form**. What the pilot established: the randomness the statistical layer needs is not supplied by the placement layer (determinize it freely — it helps) and not detectably by the committer at the churn corner. The next rung is the fully determinized stack: periodic churn events + deterministic content cycling + D1 + a D2 committer — one receipt, and the strict conjecture gets its first real test.

## 4. Corrections ledger

(a) u2 CHECK 7: mean-lifetime accounting identity — "endogenous L" downgraded to distribution-level for fixed-event-rate laws. (b) u3 P1: refuted, mechanism localized (churn laundering), prediction retained in the text with its verdict. (c) u2 CHECK 6 first-draft "mild axis" wording replaced by the measured directional improvement (caught at the exploration pass). (d) u1: N = 512 strict corner at 1.60× vs paper 16's 1.2–1.5× quote, disclosed; N = 2048 reproduces.

## 5. The queue, reordered by what was learned

1. **The abundance term, growth-bench first** — the only item both failure modes now demand; the telescope makes candidate terms cheap to price. Target: an augmented action whose growth endpoints leave the sparse class without entering the dense one.
2. **The staircase-cure certification retest** — D1-type laws at N = 2048, ≥ 12 seeds, both content readings; if `0.96×`/z-reduction certifies, paper 16's named residual closes by a law.
3. **The fully determinized stack** (G2 strict form) — one receipt, described above.
4. **The D2 proof target, sharpened by u3:** can any history-measurable committer reproduce the `Geometric(1/M)` marginal? The enumerative evidence (two candidates, both visible at ≫ 5×) suggests no; a proof would establish that the click law's sequencing randomness is irreducible *by the corpus's own arithmetic*.
5. **u4 (G4 census)** as reserved; **G5** (initial-condition-freeness / relaxation from adversarial fleets, the arrow-of-time experiment) rides u1's machinery.
6. **Design note 1's ladder (n1/n2)** — unchanged as the top cross-program unblock for 3+1; nothing in the u-line touched it.

## Receipts

`u1_growth_positive_control.py` (G0, 5/5); `u2_growth_vs_equilibrium.py` (G1 + G3, 10/10, telescope lemma + both-sides localization + the accounting correction); `u3_determinism_axis.py` (G2 pilot, 8/8, P1-refuted with mechanism + the staircase identification + the band-reaching D1+atoms arm). All self-contained, corpus conventions throughout.
