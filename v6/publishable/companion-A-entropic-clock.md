# The forced survival law on an internal entropic clock: the dynamical layer of the sealed-records program

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, companion to publishable Paper Va (foundations), version 2026-06-15.

## Abstract

The foundational layer of the sealed-records program (Paper Va) supplies the *kinematics* of records — Born composition, the Lorentzian signature, and the arrow of time, the last of these via the classical entropy-production identity `σ = D(P_AB‖P_BA)`. This companion adds the *dynamical* layer: a record-commitment **survival law** and the **clock** it runs on, derived under the program's pre-geometric discipline (records and the commit order only; no spacetime, metric, light cone, or interval `s²`). The result is a single shape. With the clock taken to be the accumulated entropy production `χ` (an internal, relational content-time, not a length or a proper time) and the increment `dχ ≥ 0` a forced odometer (vanishing only at detailed balance, which is eventless — no event, no time advance), self-consistency under refinement forces the survival law by regime: in the divisible (dense-seal) regime the multiplicativity `S(χ₁+χ₂)=S(χ₁)S(χ₂)` forces the unique `S(χ)=exp(−κχ)`, constant hazard per unit content; in the genuinely-indivisible (sparse-seal) regime only the lattice skeleton `S(nd)=S(d)ⁿ` is forced, with a free inter-seal profile. The single rate `κ` is the one free scale, and the per-seal content obeys a forced capacity ceiling `d ≤ W_*`. We state plainly what is external and what is the program-internal contribution. **External (inherited, not re-derived):** the exponential-from-multiplicativity step is the textbook Aczél/memorylessness theorem; `χ = D(P_AB‖P_BA)` is classical stochastic thermodynamics (Schnakenberg and successors), already imported in Paper Va; and reading entropy/distinguishability as an internal clock is the problem-of-time / Page–Wootters tradition, now experimentally realized (Barontini *et al.* 2026). **Program-internal contribution (a positioning, not a new mainstream theorem):** *on this program's own weight-zero entropy-production content clock, the record click-law shape is forced — exponential where divisible, a geometric lattice skeleton where indivisible — up to exactly one scale `κ` that the program's substrate provably cannot supply.* The contribution is therefore a conditional-plus-no-go statement *about the records*, not a standalone result in functional equations or in thermodynamics.

---

## 1. What is external, and what this companion contributes

This is a companion note, and the strip test for standalone novelty has already been run; we will not pretend otherwise. Three of the ingredients are entirely external and are used as imports, with the program adding no mainstream theorem to any of them.

- **The exponential is the textbook memorylessness theorem.** That a monotone, measurable survival function obeying `S(χ₁+χ₂)=S(χ₁)S(χ₂)` with `S(0)=1` is uniquely `exp(−κχ)` is the Cauchy multiplicative functional equation, solved (under exactly these regularity conditions, excluding the non-measurable Hamel pathologies) in Aczél's standard reference [A]. This is the same fact that makes the exponential the unique memoryless waiting-time distribution. We import it; we do not claim it.
- **The clock `χ = D(P_AB‖P_BA)` is classical stochastic thermodynamics.** Entropy production as the Kullback–Leibler divergence between forward and time-reversed path measures is Schnakenberg's and its successors' result (Gaspard; Kawai–Parrondo–Van den Broeck; Roldán–Parrondo) [S]. Paper Va already imports exactly this identity (its §4 audit types it as a classical import); this companion inherits it unchanged and simply *uses* it as the clock variable.
- **Entropy/distinguishability as an internal time is the problem-of-time / Page–Wootters tradition.** Reading an internal, relational quantity rather than an external parameter as "time" is the Page–Wootters conditional-probability construction and its entropic-clock descendants — a tradition now carried into the laboratory: a relational/entropic internal clock has been experimentally realized (Barontini *et al.*, *Phys. Rev. Research* **8**, L022047, 2026) [B]. We adopt the framing; we did not invent it and we make no experimental claim of our own.

**What is program-internal — and its honest type.** The contribution is not a new theorem in any of those three areas. It is a *statement about the program's records*: a conditional plus a no-go. On the program's own pre-geometric clock — the **weight-zero** entropy-production content `χ` — the record click-law's *shape* is forced: `exp(−κχ)` in the divisible regime, the geometric lattice skeleton `S(nd)=S(d)ⁿ` in the indivisible regime, with `dχ ≥ 0` a forced odometer and `d ≤ W_*` a forced capacity ceiling. And the forcing stops at exactly one place: the single rate `κ` that converts the weight-zero content into a commit-order rate carries one absolute unit the substrate provably cannot carry (the program's scale no-go). So the contribution is "the survival shape is forced on *our* clock, up to one scale *we* cannot supply" — a positioning of inherited mathematics inside the sealed-records ontology, not a result that would stand outside it.

---

## 2. The clock: an internal entropic content-time with a forced odometer

The only state variable available pre-geometrically is the record-internal content

  `χ = D(P_AB ‖ P_BA)`,

the relative entropy between the forward and reverse holonomy-transport laws — the accumulated distinguishability the holonomy has built up since the last commitment. It is **not** a length, a proper time, or an external parameter; it is an internal, relational content-time, in exactly the sense the problem-of-time / Page–Wootters tradition gives to such variables [B]. The survival functional `S(χ) ∈ [0,1]` is the probability the holonomy has not yet committed after accumulating content `χ`, with `S(0)=1`, and the hazard is `λ(χ) = −d log S/dχ`.

This clock is an **odometer**: it advances with every event and never runs backward. The increment is `dχ = σ_step = D(P_AB‖P_BA) ≥ 0` by the Gibbs/arrow-positivity inequality that Paper Va already establishes — and it is **exactly zero only at a detailed-balance step**, which is eventless and therefore *not a seal*. So `dχ = 0` means "no event, no advance of the clock," which is the precise sense in which this internal time is generated by, and only by, record commitment. The structure of the odometer — the sign `dχ ≥ 0` and the concatenation-additivity `χ(seg₁ then seg₂) = χ(seg₁) + χ(seg₂)` along the commit order — is forced, not assumed: on the eventless inter-seal stretch the trajectory action telescopes into a sum of per-step increments, so additivity holds for any starting segment, verified on a *driven* (non-equilibrium, `σ_step > 0`) chain with concatenation gap `7.7×10⁻¹²¹` and per-step `σ_step ≥ 0` by arrow-positivity (receipt `f3c_sequential_odometer.py`, mpmath `dps ≥ 100`). What the odometer's structure does **not** fix is the *magnitude* of each increment; that is configuration-dependent physical input (Paper II of the source line; here noted, not claimed).

---

## 3. The forced survival shape, by regime

A seal is a refinement point of the commit order. Self-consistency under refinement — that inserting an intermediate seal must compose — forces the survival shape, and the answer splits by whether seals are dense or sparse in the content `χ`.

### 3.1 Divisible (dense-seal) regime: the forced exponential

If refinement points are dense in `χ` — the divisible (CP-divisible, Barandes-divisible) regime — every insertion composes and survival is multiplicative for *all* splits,

  `S(χ₁ + χ₂) = S(χ₁)·S(χ₂)`  (the Cauchy multiplicative equation),

whose unique solution under `S(0)=1`, monotonicity, and measurability is

  `S(χ) = exp(−κχ)`,  constant hazard per unit content,  `λ(χ) = κ`.

The exponential step here is the textbook Aczél/memorylessness theorem [A] — we import it (§1). The program-internal part is only that the equation holds *on this program's content clock* and is fixed there by refinement self-consistency: among `S = exp(−κχ^p)`, only `p = 1` is refinement-consistent (`2^p − 2 = 0 ⟺ p = 1`; `p = ½, 3⁄2, 2` fail), and the exponential is reached as the product limit `lim_m (f(χ/m))^m = exp(χ·(log f)′(0))` for *any* stationary per-step contraction `f`, so it is not assumed exponential at finite step (receipt `f3_self_consistency.py`, mpmath `dps = 120`; balance residual of the underlying one-diamond root `9.7×10⁻¹²²`). The orthogonal-projection character of the seal that licenses the single-channel, stationary screen behind this step is a separate sympy-exact algebraic fact (receipt `f1_born_projection_q2.py`); that screen-channel premise is itself receipted (`f3e_history_independence.py`: multiplicative for one channel, history-dependent gap `0.317` for a mixed multi-channel block). The weight/scale bookkeeping that makes `χ` weight-zero is in `f4_variational_rate.py`.

`κ ≥ 0` (no revival of the *committed* survival) is the corollary that a non-composing point — one where `S(χ₁+χ₂) > S(χ₁)S(χ₂)` — simply is not a seal. No geometry, no noise spectrum, no `s²` enters: it is a structural fact about the seal order.

### 3.2 Indivisible (sparse-seal) regime: the forced lattice skeleton

If seals are sparse — at a sub-semigroup `L = {nd}` of content, the holonomy left uncommitted between commitments — composition is available only on `L`, and with the per-seal survival constant across seals the Cauchy equation restricts to `(ℕ,+)`. There it is rigid with no further regularity assumption (finite induction suffices), and the seal-lattice **skeleton is forced** to a geometric progression (geometric in the *sequence* sense, not spacetime),

  `S(nd) = S(d)ⁿ`  (receipt `f3b_sparse_seal_shape.py`, lattice-composition residual `1.2×10⁻¹²²`, mpmath `dps ≥ 100`),

while the **inter-seal coherence profile** (an infinite-dimensional functional degree of freedom) and the **spacing `d`** remain free — and that free profile *is* the genuinely-quantum (Barandes-indivisible) content the dense limit annihilates. The two regimes are one statement under a single limit: `S(d)^{χ/d} = exp(−κχ)` holds on `L` for every `d` (with `κ = −log S(d)/d`), and as `d → 0` the free profile is squeezed to zero amplitude, recovering the unique dense exponential of §3.1 (same receipt `f3b_sparse_seal_shape.py`). So the dense exponential is the `d → 0` limit of the sparse law, and genuine indivisibility is exactly the inter-seal freedom the dense (continuous-sealing, classical) limit removes. The kinematic identity behind "seal ⟺ composition" (the Chapman–Kolmogorov defect equals the interference cross-term, gap `0.329` across an unsealed interval and `0.0` at a seal) is in `f3d_foundational_supports.py`.

---

## 4. The two scales: a free rate `κ` and a forced ceiling `d ≤ W_*`

The content `χ` is a weight-zero, record-intrinsic relative-entropy number. The *only* freedom in `S(χ) = exp(−κχ)` is the single constant `κ`, the conversion from intrinsic content to a commit-order *rate*. Refinement fixes the form and never this rate; converting a weight-zero number into a rate requires one absolute unit the records provably do not carry. So the click-law shape is **forced up to exactly one calibration `κ`** — the program-internal positioning of §1, stated precisely. (Whether `κ` is *the same* missing scale the program's gravitational no-go isolates is argued by structural analogy in the source line, not proven, and is not claimed here.)

The companion *spacing* `d` of the sparse regime, by contrast, gets a genuine forced bound. The one-diamond self-consistency law `KL content = Fisher capacity` fixes the saturation constant

  `W_* = 1 − tanh²η_* = 0.364784952089976…`,  `η_* = 1.090344354879492…`

(receipt `f3_self_consistency.py`; balance residual `9.7×10⁻¹²²` at `dps = 120`). Because accumulated content rises while Fisher capacity falls — crossing once at `η_*` — the per-diamond content cannot exceed `W_* = max_η min(C(η), J(η))`: an over-saturated commitment is self-inconsistent. Hence **`d ≤ W_*` is forced**, given only that a committed record is a non-over-saturated diamond — a bound the composition self-consistency of §3 could not supply (it leaves `d ∈ (0,∞)`). The *equality* `d = W_*` is **not** forced: the corpus's own seal-firing law commits strictly below capacity (sub-capacity, mode-dependent content, on a random evidence clock), so what fixes the exact spacing remains the open obligation of the source line. We report `d ≤ W_*` as the forced ceiling and nothing stronger.

---

## 5. What this companion does and does not claim

It **claims**, on the program's records and with the receipts named: that the program's pre-geometric clock is the internal entropic content `χ` with a forced odometer `dχ ≥ 0` (zero only at the eventless detailed-balance step, so no-event-no-time; §2); that self-consistency under refinement forces the survival *shape* — `exp(−κχ)` where divisible, the geometric lattice skeleton `S(nd)=S(d)ⁿ` where indivisible, the latter recovering the former as `d → 0` (§3); and that the forcing stops at exactly one free scale `κ` the substrate cannot supply, with the companion spacing obeying the forced ceiling `d ≤ W_*` (§4).

It does **not** claim novelty in any inherited piece: the exponential is the textbook Aczél/memorylessness theorem [A]; `χ = D(P_AB‖P_BA)` is classical stochastic thermodynamics [S], already imported in Paper Va; the entropy-as-internal-time framing is the problem-of-time / Page–Wootters tradition, now experimentally realized [B]. It does not claim a value for `κ`, a magnitude for the content increment, a fixed spacing `d` (only the ceiling), the identity of `κ` with the gravitational scale (argued by analogy in the source line, not here), or any geometric/relativistic content as an axiom. The honest one-line summary: **on the sealed-records program's own weight-zero entropy-production clock, the record survival law's shape is forced — exponential (divisible) or a geometric lattice skeleton (indivisible) — up to exactly one rate `κ` the substrate provably cannot supply; that conditional-plus-no-go statement about the records is the contribution, the underlying mathematics being entirely standard.**

---

## Reproducibility

Every numeric claim above cites a receipt in `v7/code/`, each a deterministic fixed-seed script run at mpmath `dps ≥ 100` (commonly 120–140) and sympy-exact where the structure permits; never float64 for the cancellation-heavy self-consistency balance or the near-`S=1` survival quantities. The receipts:

- `f1_born_projection_q2.py` — the seal as an orthogonal projection (sympy-exact algebraic check), licensing the single-channel screen behind §3.1.
- `f3_self_consistency.py` — the Cauchy-equation uniqueness, the `p=1`-only refinement check (`2^p − 2 = 0 ⟺ p = 1`), the product-limit forcing of the exponential, and the one-diamond root `W_* = 0.364784952089976…` (balance residual `9.7×10⁻¹²²`).
- `f3b_sparse_seal_shape.py` — the forced geometric lattice skeleton `S(nd)=S(d)ⁿ` (residual `1.2×10⁻¹²²`) and the monotone `d → 0` → exponential squeeze.
- `f3c_sequential_odometer.py` — the sequential (commit-order) content-additivity (concatenation gap `7.7×10⁻¹²¹` on a *driven* chain) and `dχ = σ_step ≥ 0`.
- `f3d_foundational_supports.py` — the kinematic seal ⟺ composition identity (Chapman–Kolmogorov defect = interference cross-term; gap `0.329` unsealed, `0.0` at a seal).
- `f3e_history_independence.py` — the single-scalar-channel premise behind the dense step (multiplicative for one channel; history-dependent gap `0.317` for a mixed multi-channel block).
- `f4_variational_rate.py` — the weight/scale bookkeeping making `χ` weight-zero and `κ` the one free rate.
- `p2a_content_supply.py`, `p2b_event_law_saturation.py`, `p2c_vector_ledger_roots.py` — the capacity ceiling `d ≤ W_*` and the sub-capacity seal-firing roots referenced in §4.

## References

**Companion (this program).**

[Va] *Quantum theory from sealed records I: Born composition, Lorentz signature, and the arrow of time* (`v6/publishable/paper-Va-foundations-1`) — the parent foundational layer; the `σ = D(P_AB‖P_BA)` import and the arrow-of-time theorem this companion's clock inherits.
[I] *The record click-law, I: a self-consistent pre-geometric sealing law and its emergent thermodynamic limit* (`v7/relativistic-isp-v7-paper1-record-click-law`) — the forced survival shape, the odometer, the divisible exponential and indivisible lattice skeleton, the single free `κ`.
[II] *The record click-law, II: the content supply* (`v7/relativistic-isp-v7-paper2-content-supply`) — the forced coboundary clock and the forced capacity ceiling `d ≤ W_*` (and the open spacing question).

**External.**

[A] J. Aczél, *Lectures on Functional Equations and Their Applications* (Academic Press, 1966) — the Cauchy multiplicative equation and its unique monotone/measurable solution (the memorylessness theorem).
[S] J. Schnakenberg, *Network theory of microscopic and macroscopic behavior of master equation systems*, Rev. Mod. Phys. **48** (1976) 571; P. Gaspard, *J. Stat. Phys.* **117** (2004) 599; R. Kawai, J. M. R. Parrondo, C. Van den Broeck, *Phys. Rev. Lett.* **98** (2007) 080602; É. Roldán, J. M. R. Parrondo, *Phys. Rev. Lett.* **105** (2010) 150607 — entropy production as path-measure relative entropy.
[B] G. Barontini *et al.* (2026); arXiv:2509.07745 (*Phys. Rev. Research*, 2026) — experimental realization of a relational/entropic internal clock (the Page–Wootters / problem-of-time tradition). (Cited by arXiv; confirm the journal volume/article locator against the published record before submission.)
