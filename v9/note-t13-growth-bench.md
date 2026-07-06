# T1.3 — the S_aug growth bench: does Row C break the sparse degeneracy, and does Row A steer?

**Status:** design note + pre-registration, 2026-07-05 (PLAN.md T1.3; round 2). Gates pinned here and from the β = 0 control's own trajectory at first execution (the note-8 §4 registration, executed as registered this time). Receipt: `v9/code/s1_growth_bench.py` (6/6). **[EXECUTED same-date, all three predictions CONFIRMED: P1 — A1's argmin endpoints r = 0.43–0.45, the antichain degeneracy broken by Row C (A0 control reproduces r = 0.000 on this stream); P2 — 6/6 A1 endpoints at β ∈ {β*, ∞} land MIDDLE-sprinkling-band (r ≈ 0.44 with height inside the 2√n band), replicated at n = 128 (4/4; H/2√n = 1.06–1.28); the β = 0 control's OWN endpoints classify MIDDLE-sprinkling-band under this receipt's classifier (r = 0.555/0.649, H-band 1.21/1.49, the n = 128 values boundary-grazing) — the kernel reaches the band with random picks, DISCLOSED; the action's specific contributions are the argmin escape from A0's antichain and the centering/holding at r ≈ 0.44 against the control's DENSE-ward drift with scale; P3 — A2's top-interval abundance misfit 0.284 vs A1's 0.929 (3.3× steering) — Row A steers under growth; paper 14's "pricing without steering" was drift-mode-specific per the reconciliation clause. All [directional, 3 reps, n = 64–128, sub-onset — classification only, no cell claims]. The first derived action whose growth endpoints leave both walls.]**

## 1. The arms

Sequential irreversible growth with `u2`'s kernel family (12 transitive-percolation candidate down-sets + the always-included empty candidate — one more percolation candidate per arrival than `u2`'s 11+empty, disclosed; the kernel's own bias attributed by the β = 0 control, the j2 lesson). Three actions, increments exact:

- **A0 (control):** paper 11's `S_r + link` (`m₀ = 8`) — `u2`'s bare action; its β = ∞ endpoint is the antichain by the degeneracy (paper 17 §4).
- **A1:** `A0 + S_comp`, `S_comp = (n(n−1)/2)·(r − ½)²` (note-t11 Row C). Not interval-local; its increment is exact from the running relation count. `S_comp(antichain) = n(n−1)/8`, so the empty move is no longer free — the argmin trade-off is now real.
- **A2:** `A1 + S_ab` (note-t11 Row A, `J = 2`, `m₀ = 8`, unit weight, disclosed) with the **exact** `E[A_j(k)]` reference (the note-t11 trap honored: no asymptotic substitute).

β grid `{0 (control), 1, β* = 16 ln 2, ∞ (argmin)}`; `n ∈ {64, 128}`, 3 replicates/arm (matching `u2`; [directional] at this count, stated); V-cov primary — all three actions are label-invariant by construction; the V-lab fork stays re-owed at `u4` (paper 17 §9 item 1).

## 2. Screens and classification (as registered)

The β = 0 control's trajectories — `r(t)`, height `H(t)`, frontier fraction `f(t) = |maximal|/t` — are logged per run, and the pathology gates are pinned at first execution *from the control*: sparse-pathology if endpoint `r < 0.3·r_ctrl`; dust if `f_end > 3·f_ctrl`; originary if `H_end > 3·H_ctrl`. Endpoint classes: SPARSE (`r < 0.2`), DENSE (`r ≥ 0.7`, the attractor class), MIDDLE (`0.35 ≤ r ≤ 0.65` — the S_comp target zone, subdivided by height band `H/2√n ∈ (0.5, 1.5)` into sprinkling-candidate vs forgery-shaped), else BOUNDARY. Scale disclosure: `n = 64–128` is below the link-term crossover and the onset floor — endpoint *classification*, no cell claims (those are the paper-1 follow-up at scale).

## 3. Predictions (pre-registered, both directions live)

- **P1:** A1's `β = ∞` endpoint is **not** the antichain (`r > 0.2`) — Row C's wall makes the empty-move argmin false. Refutation direction: the kernel's candidate menu might not offer relation-rich-enough moves for S_comp's pull to act (a kernel confound, attributable via the control).
- **P2:** A1 endpoints land in the MIDDLE class (`r ∈ [0.35, 0.65]`) at `β ∈ {β*, ∞}` — the escape-from-sparse. Both directions: overshoot to DENSE would say S_comp's pull needs damping; landing MIDDLE-forgery-shaped (height off-band) is the expected *partial* success that hands the steering question to A2.
- **P3 (the steering test):** A2's endpoints carry smaller mean per-interval abundance misfit than A1's on their top intervals (`k ≥ m₀`) — Row A steers interiors toward Poisson profiles under growth, the direct counter-test of paper 14's drift-mode "pricing without steering" verdict. **Reconciliation clause (the PLAN's requirement):** paper 14's verdict was measured in *drift mode* at one λ, kernel, and scale; growth is a different sampling mode — monotone, no rearrangement entropy, exact increments (paper 17 §2/§4) — so a steering success here does not contradict it, and a steering failure localizes the "no steering" phenomenon as mode-independent, which would be the sharper negative.

**Kill:** if A1 and A2 endpoints stay SPARSE at every β, Row C's pull is insufficient against this kernel — the failure localizes to the move menu (kernel confound) or the weight, both named; redirect per PLAN T1's kill text after a kernel ablation.

Conventions: `default_rng(20260706)`; float64; `dps = 60` for the cached exact references; every gate quoted in the receipt docstring.
