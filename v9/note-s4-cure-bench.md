# note-s4 — the cure bench: does charge-rate selection un-forge the endpoints?

**Status:** design note + pre-registration, 2026-07-05 (round 5). ALL thresholds pinned here BEFORE first execution (#45's lesson). Receipt: `v9/code/s4_cure_bench.py`.

**The rule under test.** `Φ_rate`: at each arrival pick `argmin ΔS/max(|D|, 1)` — cost per new pair (a move functional in note 8's class C4; corpus-legal). Wrinkles stated at registration (round-4 review m9): the empty candidate has `|D| = 0` (rate = its raw `ΔS_comp`, positive at `r < ½`); negative increments re-rank toward small `|D|` under this form — both disclosed, the endpoints decide.

**Arms (n = 512 — the forgery's own scale — plus an n = 256 continuity grid):** A1-rate (4 reps @512; 3 @256), A1-argmin (2 reps @512 — the myopic control, fresh stream), β = 0 kernel control (2 reps @512, **with its own interior baseline printed** — the M3 lesson: the kernel defaults to chain-heavy interiors, r_I ≈ 0.73–0.79, m_ab ≈ 10–14×).

**Pinned gates (both directions live):**
- **P1 (the cure, primary):** A1-rate's heredity axis (mean interior `r_I`, largest intervals) lands in the faithful band `[0.35, 0.65]` (note-s2's P3 band, cited) in **≥ 3/4 reps at n = 512** — vs argmin's measured `0.69–0.88`.
- **P2:** `m_ab`(A1-rate) `< 0.5 ×` `m_ab`(A1-argmin) at 512 (factor pinned now).
- **P3 (no wall resurrected):** global `r ∈ [0.35, 0.55]` every rep.
- **Verdicts:** all three ⇒ CURE-SUPPORTED (myopia was the mechanism's operative face); P2 without P1 ⇒ PARTIAL (fine structure improves, interiors stay forged — the multiplicity route promotes to primary); otherwise ⇒ CURE-REFUTED (myopia insufficient — the mechanism hunt reopens with the round-4 demotions as the map).

Seed `default_rng(20260709)`; float64; machinery = s1/s2 verbatim; faithful baselines per s2's convention.
