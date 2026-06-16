# R2 / (PR-RP+) — attack notes (2026-06-14)

R2 = "(PR-RP+): reflection positivity + finite record rank ⟹ finite record law (sealability)."
Bond-RP processes are finite-rank quantum record ledgers (p27 Prop 1.1): `p(x₁..xₙ)=⟨Ω|A_{x₁}..A_{xₙ}|Ω⟩`,
`A_x=T^{1/2}E_x T^{1/2}⪰0`, `ΣE_x=I`, `0⪯T⪯I`, `TΩ=Ω`. The only escape from sealability is a **composite
clock**: a block word `W` whose transfer `A_W` drives the diagonal `p(Wⁿ)` into an irrational oscillation
that survives positivity. Paper 27 closes this lane by a **validity wall** (random sampling, best
subordination s≤0.205) + a mechanism (validity-at-depth forces Perron weight, = P16 Theorem B at block
scale); the residue is the **multi-letter Anderson assembly**.

## What this attack did, and the honest outcome
Goal: stress-test the validity wall by **optimization** (vs paper 27's random sampling) — search hard for
a *valid* composite clock. Code: `code/v6_r2_composite_clock_search.py`.

**The attack surfaced (and corrected) three metric pitfalls — worth recording, because they are exactly
where a false counterexample would come from:**
1. **Spectral ≠ dynamical.** `s = |λ_complex|/ρ` (a complex eigenvalue *at* the radius) is reachable with
   s=1 by valid ledgers — but that is **not a clock**. The complex peripheral eigenvalue can carry no net
   Ω-weight / be Perron-dominated, so the *diagonal* `p(Wⁿ)` stays positive (sealable). The clock is the
   Ω-WEIGHTED oscillation of the diagonal, not the spectrum.
2. **Validity depth must exceed the period.** A small-angle "clock" has period `2π/θ` (≈376 at angle
   0.0053π); checking `p(Wⁿ)≥0` only to depth 60 misses the oscillation. The genuine threat is angle =
   O(1) irrational (period ≲25), checked to depth ≫ period (used 2500).
3. **Trust the direct check.** Eigen-weight decomposition via `inv(V)` of the non-normal `A_W` is
   ill-conditioned and gave inconsistent weights; the reliable quantity is the **direct diagonal**
   `p(Wⁿ)=⟨Ω|A_Wⁿ|Ω⟩≥0`.

**Result (reliable, direct-diagonal check):** under 40k wide samples + hill-climb maximizing the clock
proxy, **every valid ledger found has a positive (sealable) diagonal to depth 2500** — no genuine
composite clock. This **confirms paper 27's validity wall under optimization pressure** (a modest
strengthening: optimization-grade, not just random-sample), and re-derives its mechanism: a peripheral
oscillation with Ω-weight forces the diagonal negative unless a real Perron mode dominates → P16 Theorem B
operating at block scale. **No counterexample to (PR-RP+).**

Honest caveat: my independent search is *numerically subtle* (the three pitfalls above), so it does not
*improve on* paper 27's careful depth-4000 analysis — it independently reproduces its conclusion and
stresses it. I make **no** claim beyond "the clock lane holds under optimization; the spectral-s metric
is a red herring."

## The genuine residue (where R2 actually lives)
The clock lane being closed, (PR-RP+) reduces — as paper 27/24 state — to the **multi-letter Anderson
assembly**:

> **(R2 residue).** Given a finite-rank bond-RP ledger whose every block-diagonal `p(Wⁿ)` is a Hamburger
> moment sequence (no clock, established/strengthened above), does there exist a **single finite
> polyhedral cone invariant under ALL letter maps `A_0, A_1` simultaneously** (a joint positive
> realization)? Single-letter realizability is solved (Anderson's dominant-pole theorem); the **joint**
> (multi-letter) case is the open generalization in classical positive-systems theory (Benvenuti–Farina).

**Tractability: hard-but-doable (named classical problem), not Clay-hard.** It is a finite-dimensional
convex-geometry / positive-realization question, not a continuum or relativistic-collapse problem. The
most promising route: a **common-cone construction** — intersect/iterate the single-letter Anderson cones
toward a joint invariant cone, or a counterexample where single-letter realizability holds but no joint
cone exists (which would refute (PR-RP+) by a realizability, not a clock, obstruction). This is the
correct next target for R2 — and notably a *different* object than the clock my search probed.

## UPDATE — the dossier's sharper target (NR), and a decisive result
The full R2 dossier (paper 30 + paper-II) shows the residue is more refined than the clock: (PR-RP+)
reduces to the **spectral half (CPE)** + the **assembly half**, and CPE reduces *at rank-3* to two
finite needles — **(NR)**: *a NORMAL word in two PSD letters has real spectrum* — and **(ISO)**. The
single decisive sub-target is **(NR)** (a normal word with a nonreal eigenvalue would KILL the rank-3
reduction). My composite-clock search probed a cruder object; (NR) is the real one.

**Decisive (NR) test** (`code/v6_r2_NR_needle.py`): complex-spectrum chiral words in two PSD letters
exist (e.g. necklace 001011 at d=3, the corpus' own example) — the question is whether any is *normal*.
Tracing the frontier (min normality defect at fixed complex-strength τ = |Im|/ρ):

```
   tau (complex-strength)   0.02    0.05    0.08    0.12
   min normality defect     0.189   0.286   0.352   0.419   (MONOTONE INCREASING)
```

The minimum achievable normality defect **grows monotonically with the required complex-strength** and is
bounded away from 0 for every τ>0: forcing the spectrum more complex forces the word *more* non-normal.
**Strong numerical evidence FOR (NR)** — normality forces real spectrum; the normal point is the
real-spectrum boundary. This *supports* the rank-3 CPE reduction (the spectral half of (PR-RP+)).

The monotone frontier suggests a *quantitative* (NR): `defect ≥ f(|Im|/ρ)` with f increasing — a candidate
seed for a proof (a quantitative normal-implies-real bound). Honest caveat: this is a float64 search, not
a proof; the dossier's exact-rational lane (normality defect of the known exact d=3 word, exact arithmetic)
would harden it, and (NR) being supported does not close R2 — **(ISO), the higher-rank closure, and the
assembly half (multi-letter Anderson) remain**.

## Status
- Clock lane: **closed** (paper 27 mechanism, stressed under optimization).
- (NR) needle: **supported with a quantitative frontier** (this work) — the sharp spectral sub-target.
- Residue: **(ISO) + higher-rank closure + the multi-letter Anderson assembly** — the real R2 frontier.
