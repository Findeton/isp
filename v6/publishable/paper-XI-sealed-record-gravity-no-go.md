# Emergent Einstein equations without an emergent Newton constant: a no-go for sealed-record gravity

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-14. Every load-bearing line is tagged by epistemic status: **[DERIVED]** = established (symbolic or high-precision numeric), with its conditional gates named; **[NO-GO]** = a proved obstruction; **[OBSTRUCTED]** = blocked in practice, with the obstruction characterized; **[OPEN]** = an unsolved obligation. All numeric claims were verified at mpmath `dps ≥ 80` (commonly 100) and symbolically (sympy) where exact; the receipt script is `code/v6_pXI_sealed_record_gravity_nogo_receipts.py`.

## Abstract

Within the sealed-records program — physics as whole histories of committed records rather than instantaneous states — we give the gravity sector its sharp, two-sided verdict. **The records derive gravity's equation of state, and prove they cannot fix its scale.** On the positive side, taking the horizon temperature `T = a/2π` as established elsewhere in this batch (Euclidean-cone regularity and Bisognano–Wichmann modular structure), we show the horizon record entropy is structurally **pure-area** — a curvature-free Wald–Noether charge of the Einstein sector (`dσ_A/dR = 0` by construction) — so that the Clausius relation `δQ = TδS` and the modular first law `δS = δ⟨K⟩` close, yielding the Einstein field equations *in form*. The derivation reaches the **full nonlinear** equation `G_μν + Λg_μν = 8πG T_μν` (here `Λ` is the cosmological constant; the no-go invariant `G·Λ²` below instead uses `Λ` for the inverse-length UV cutoff — a distinct object) — the pointwise null relation `2π T_kk = η R_kk` for the actual Ricci tensor, checked nonlinearly — and its **spin-2 (traceless)** part follows as a one-step geometric identity: a symmetric tensor annihilating every null contraction is pure-trace (`S_ab k^a k^b = 0 ∀` null `k ⇒ S_ab = Φ g_ab`, the constraint having rank `9` on the `10` symmetric components). This is [DERIVED], modulo three named gates — the temperature value (axiom R), Jacobson's local-equilibrium premise `θ = σ = 0`, and one continuum focusing input. On the negative side we prove a **no-go**: the records cannot fix the absolute scale `σ_A` (length-weight `−2`, in bijection with Newton's `G` via `G·σ_A = 1/4`). Under the length-unit gauge `l → μl`, every intrinsic record functional is weight-zero while `σ_A` is weight `−2`; the contradiction is exact (weight-counting lemma), and the SIGMA-SPLIT construction makes it concrete — the *same* sealed horizon data are consistent with `A_rec = 1` or `A_rec = 3`, giving the schematic Clausius coefficient `κ_J ≡ 1/σ_A = 1` or `3` with the Einstein residual `0` for both. Both `κ·σ_A = 2π` (the physical coupling `κ = 8πG`) and `G·Λ²` (with `Λ` the inverse-length UV cutoff, distinct from the unimodular `Λ₀`) are fixed weight-zero invariants (separate pure numbers, not numerically equal), each leaving the absolute scale free. The entire no-go rests on one isolated premise — **gate G1**: no sealed law consumes the record area outside the labeling map — exactly as the temperature value rests on axiom R; its sharpest candidate counterexample, an intrinsic seal rate, closes rather than opens it. We show the obstruction is **the same structural fact as QCD's dimensional transmutation** (a scale-free record ontology predicts every dimensionless ratio and needs one external unit), and we separate the *derived* spin-2 equation from the *obstructed* propagating graviton, which would require a continuum (type III₁) structure the finite record lattice cannot host. The result places sealed-record gravity squarely in the emergent/thermodynamic tradition: **gravity's form for free, its scale and its graviton provably not.**

---

## 1. What is derived: the equation of state

### 1.1 Temperature [DERIVED, mod axiom R — established in the horizon-thermodynamics paper of this batch]

The thermodynamic derivation begins with a temperature. The horizon-thermodynamics paper of this batch establishes it two ways on record lattices: the Euclidean cone is smooth at the unique period `β = 2π/κ` (Gibbons–Hawking regularity, with Bessel-mode matching), and the wedge-reduced record vacuum exhibits Bisognano–Wichmann modular structure `ε_k = 2π ω_k^{boost}` uniformly across resolvable modular levels. We take `T = a/2π` as input. Its value `β = 2π` rests on one named axiom (R) — the Euclidean-rotation / modular-period identification, the residue of Bisognano–Wichmann — and we carry that conditional forward without re-deriving it here. As a high-precision consistency check, the accelerated KMS detailed-balance ratio `F(E)/F(−E) = e^{−2πE/a}` holds identically at `T = a/2π` (residual `0` at `dps = 100`), and the Rindler interval identity `Δt² − Δx² = (4/a²)\sinh²(aΔτ/2)` is exact.

### 1.2 Geometry-universal area density [DERIVED]

The pure-geometry content of the area law is geometry-universal. A `3+1` massless scalar partial-wave-decomposes into radial chains, and the ball entropy `S(R) = Σ_l (2l+1) S_l(R)` gives an area coefficient that Richardson-extrapolates to **Srednicki's `0.295`** [5] with no fitted tail — a genuine universal constant (the spherical-ball partial-wave computation is the program's entanglement-capacity calculation). The ball/planar capacity ratio is `U_G = 1` to `~10⁻³`. Crucially, the absolute scale `σ_A` *cancels* in this ratio (`ν = σ_A·f_geom`, `U_G = f_sph/f_pl`), so the *geometry factor* `f_geom` is record-derived while the overall scale is not. Two caveats are kept honest: `U_G = 1` *straddles* unity at the `~10⁻³` level (the sign of `U_G − 1` is cutoff-limited, a consistency not a sign-determination), and flat-screen universality is *measured to break in the angular sector* (the partial-wave first-law ratio departs from unity for `l ≥ 1`). So [DERIVED] covers the area-coefficient ratio and the scalar (`l = 0`) channel; the angular sector is a measured departure.

### 1.3 Pure-area Wald–Noether charge [DERIVED, structural]

The record entropy is screen-cell counting, `S = σ_A·A + o(A)`, with curvature pieces explicitly subleading. The Wald density is then `s = σ_A` with `ds/dR = 0` **by construction** — the screen-cell capacity does not couple to a curvature scalar — so this is the *statement* that `σ_A` is curvature-free, a structural property of the screen-cell entropy ontology corroborated by the floor-converged mode-cutoff sweep (the apparent curvature-running shrinks monotonically with the cutoff, consistent with a truncation artifact rather than a Wald coupling). This is **not** a derivation that an arbitrary higher-curvature gravitational action generates no Wald corrections; it is the statement that *this* ontology's entropy is pure-area. The consequence is that `η = 1/4G` is well-defined (not running), keeping the Clausius route in the equilibrium (pure-Einstein) branch rather than the nonequilibrium `f(R)`/Lovelock branch.

### 1.4 The field equations in form [DERIVED, mod R + local-equilibrium + focusing gate]

With a pure-area entropy at temperature `T = a/2π`, two closures deliver the Einstein equation in form.

**Clausius (nonlinear).** The Jacobson construction on local Rindler horizons is exact: Raychaudhuri gives `θ = −R_{kk}λ + O(λ²)`, the heat- and area-side affine moments cancel, and the pointwise null relation `2π T_{kk} = η R_{kk}` holds for the **actual Ricci tensor** — checked nonlinearly on explicit Schwarzschild and on an anisotropic fluid with genuine traceless stress (corpus computations), with contracted Bianchi closing. The coefficient match `2π/η = 8πG` forces `η = 1/4G`. This is the **full nonlinear** equation `G_μν + Λg_μν = 8πG T_μν`, not a linearized truncation.

**Modular first law (linearized) and the spin-2 part.** The relative-entropy first law `δS = δ⟨K⟩` (with `S_rel ≥ 0` strictly second order) yields the linearized equation. Its traceless (spin-2) part follows as a one-step geometric identity: the null-cone lemma — *a symmetric tensor `S_ab` with `S_ab k^a k^b = 0` for every null `k` is pure-trace, `S_ab = Φ g_ab`* — fixes **all 9 traceless components at once** (the constraint over a spanning set of null `k` has rank `9` on the `10` symmetric components; sympy). The same geometric content underlies Jacobson's entanglement-equilibrium derivation; the correct timelike statement of it is that a symmetric `E_ab` whose contraction `E_ab u^a u^b` is the *same* for every unit timelike `u` is `c g_ab` (the naive vanishing condition `E_ab u^a u^b = 0 ∀` unit timelike `u` instead forces `E = 0`, and is *not* the lemma). The traceless projection removes the free proportionality coefficient `c` (the cutoff scale `Λ`), so the **shape** of the spin-2 equation is scale-free; `G` itself remains explicitly, as the coupling on the right-hand side `8πG T_{⟨ab⟩}`.

**Conditionality.** Three named gates carry the form: axiom (R) (§1.1); Jacobson's **local-equilibrium premise** `θ = σ = 0` at the bifurcation — *presumed, not derived* — which selects pure Einstein over the nonequilibrium branch; and the continuum focusing input `θ′ = −R_{kk}`. None of these bears on the no-go of §2.

### 1.5 The unimodular fork [DERIVED]

Trace-free Einstein `R_ab − ¼g_ab R = 8πG(T_ab − ¼g_ab T)` is a genuine 9-component equation in `d = 4`; its divergence plus contracted Bianchi gives, with `Λ := (R + 8πG T)/4`, exactly `∇_b Λ = 8πG η_b` (residual identically `0`, sympy) — the conservation/Bianchi obstruction *rerouted* into a dynamical `Λ`, not evaded, with the *same* `8πG` (no second coupling). The cosmological constant becomes a non-sourced integration constant `Λ₀`, a boundary datum.

So sealed-record gravity reaches the Einstein field equations **as the thermodynamics of the records**, deriving more than the vanilla thermodynamic program assumes (the geometry-universality and the pure-area property are derived here, not posited). The remainder establishes precisely where, and why, the path stops.

---

## 2. The no-go on Newton's constant [NO-GO]

### 2.1 The result and its single premise

The records do not, and provably cannot, fix the absolute scale `σ_A` — which has length-weight `−2` and is in bijection with Newton's `G` (weight `+2`) via `G·σ_A = 1/4` (so fixing one fixes the other; they are linked, never equal). Under the length-unit gauge `g_λ: l → μl` holding all sealed data fixed, the records carry only weight-zero (dimensionless / ratio / conformal) invariants. The degree map `weight(X) = \log[X(μl)/X(l)]/\log μ` gives, sympy-exact (and numerically at `μ = 1.7`, residual `0`):

  `weight(A_rec = l²) = +2`,  `weight(σ_A = 1/l²) = −2`,  `weight(G) = +2`,  `weight(l_step) = +1`,  `weight(\text{pure count}) = 0`,

with the bijection `G·σ_A` of weight `0` and value `1/4`. Both

  `κ·σ_A = 2π`   and (separately)   `G·Λ² = \text{const}`

are fixed weight-zero invariants — *each* a pure number, **not numerically equal to one another** (`κ·σ_A = 2π` follows from `κ = 8πG` and `G·σ_A = 1/4`; `G·Λ²` is a different pure number set by whichever route computes it). What they share is the *structure*: a weight-zero combination is fixed while the absolute scale `σ_A`/`G` is a free modulus. (Two normalizations of the Clausius coefficient appear: the physical `κ = 8πG` in `κ·σ_A = 2π`, and the schematic `κ_J ≡ 1/σ_A` in the SIGMA-SPLIT of §2.2, where `κ_J·σ_A = 1`. Throughout, `Λ` is the inverse-length UV/spectral cutoff, distinct from the unimodular cosmological constant `Λ₀` of §1.5.)

**The single load-bearing premise — gate G1.** The no-go rests on exactly one premise, isolated as cleanly as axiom (R) isolates the temperature value: **gate G1** — *no sealed law consumes the record area `A_rec` (a weight-`±k` dimensionful datum) except through the continuum labeling map `ℓ`.* G1 is what makes the corpus factor as `(R, ℓ)` with `g_λ` the identity on the record sector `R`, so that every intrinsic record functional factors through `R`, is `g_λ`-invariant, and is therefore weight-zero — while `σ_A` is weight `−2`. The no-go is airtight *iff* G1 holds. Its sharpest candidate counterexample, an intrinsic *seal rate* `Γ` (divisions per proper time), **closes** rather than opens it: a record-internal `Γ` is divisions-per-seal `= 1` (weight 0, no scale); any geometric `Γ` is the seal density `1/l_step` (weight `−1`, the gauge/spacing direction itself); and a putative weight-`(−2)` `Γ² = (#²)/A_rec` is a free record number times `1/A_rec` (a relabeling, never the absolute `σ_A`) — an intrinsic absolute scale would need weight `−2` *and* weight `0` at once, which the factorization forbids. So the seal-spacing length is provably the unique dimensionful primitive and the sole gauge direction.

### 2.2 SIGMA-SPLIT: the gauge orbit made concrete [NO-GO]

The mechanism is visible in one construction. The *same* sealed horizon data are consistent with two screen-cell normalizations, `A_rec = 1` or `A_rec = 3`, giving

  `A_rec = 1 ⟹ σ_A = 1, κ_J = 1, G = 1/4`;  `A_rec = 3 ⟹ σ_A = 1/3, κ_J = 3, G = 3/4`,

with `κ_J ≡ 1/σ_A` the schematic Clausius coefficient, `G·σ_A = 1/4` invariant in both, and the Einstein-form residual exactly `0` in both (sympy). The absolute `G` is free; only the gauge-invariant product is fixed. A scale-rescaling check confirms it: `l → μl` sends `G → μ²G` while *every* sealed, order, and modular observable is invariant.

### 2.3 Every lever collapses the same way [NO-GO]

Each candidate route to fix `G` reduces to the same weight-zero invariant. A mass-gap correlation length is `(\#)·l_step` (lattice units, not an independent length); a second marginal sector transmutes a *dimensionless* fixed-point coupling, tying sectors to one another, never to a geometric length; an asymptotic-safety fixed point `g_* = Gμ²` gives `G = g_* l_step²`, reproducing SIGMA-SPLIT; the conformal trace anomaly `(a, c)` fixes dimensionless higher-curvature couplings only; Sakharov-induced gravity gives `G·Λ² = 192π²/N` with `Λ` cancelling. The **de Sitter** route is the sharpest test and still collapses: the unimodular `Λ₀` is itself weight `−2` (the weight-twin of `σ_A`), and the entropy `S_dS = π/(G·Λ₀) = N_dS` (prefactor schematic — the textbook value is `3π/(GΛ₀)`; the weight argument is prefactor-independent) fixes only the weight-zero product `G·Λ₀`, with `N_dS = A_horizon/A_rec = 4π(σ_A/Λ₀)` the ratio of two weight-`(−2)` data — `l`-independent (sympy `d/dl = 0`), so it adds no gauge-eligible datum and `G` stays free. Even the strongest *record-unit* attack fails: measuring a mass in record units smuggles in the record-length↔lab-length conversion that `g_λ` acts on. The unification is the content: *deriving `1/G` always trades it for a labeling-equivalent cutoff; the missing datum is exactly one absolute length unit, which no weight-zero record functional can be.*

### 2.4 The same fact as dimensional transmutation

The no-go is not a pathology; it is the gravity-sector face of a familiar fact. A confining gauge theory predicts every dimensionless mass *ratio* and the running of a dimensionless coupling, but **dimensional transmutation does not produce an absolute scale** — `Λ_QCD` in physical units is an external input, and a lattice mass gap comes out as a pure number times the lattice spacing. Sealed-record gravity says the same of `G`: the records fix every dimensionless ratio and the Einstein *form*, and need one external unit to set the scale. What the no-go forbids is *one absolute dimensionful unit* — **not** the dimensionless gravitational coupling-per-species `c_m = Gm²/ℏc`, which is weight-zero, intrinsic, and therefore *eligible* to be a record output (the open hierarchy question, the gravity-sector analog of predicting dimensionless mass ratios). A theory that reconstructed gauge physics up to one scale yet fixed `G` absolutely would be the contradiction; the no-go is the program being consistent with itself.

---

## 3. The tensor sector: the spin-2 equation is derived, the graviton is not

The linearized spin-2 Einstein *equation* `G_{⟨ab⟩} = 8πG T_{⟨ab⟩}` is derived geometrically (§1.4). What is **[OBSTRUCTED]** is the *distinct* claim that the matter modular *currency* independently **prices** the traceless stress `T_{⟨ij⟩}` as a universal first-law charge — i.e. the propagating graviton / quantum spin-2 operator, *not* the equation. The modular currency prices the 4 energy–momentum components (`T_{00}`, `T_{0i}`) at a universal capacity `1/(4ν)`; a congruence of boosted wedges does **span** the 5 traceless spatial-stress components (rank 5), but only at a **non-universal, boost-dependent, second-order** coupling `χ·\sinh²η`, never the single universal capacity that prices energy and momentum.

Four obstructions converge on **one root**. (i) *Non-universality*: the traceless coupling is a second-order susceptibility, not a capacity. (ii) *Type I, no area operator*: the finite record lattice is a type-I algebra with no center-valued area operator; the crossed-product constructions that manufacture a fluctuating area operator from an algebra lacking one are blocked — the modular flow is inner/trivial, and the entropy-production (arrow) flow, though genuinely outer, is a *stationary current* preserving an invariant measure, so its crossed product is semifinite (type I, c-number area), not the type III₁ needed. (iii) *Berry*: the first-order relative modular charge between boosted wedges has zero spin-2 (`\cos 2θ`) overlap. (iv) *Null-cut*: the universal-`2π` null-cut pricing *is* a half-sided modular inclusion `[K,P] = iP`, which has no finite-dimensional representation. The single root: **every spin-2 / quantum-area route needs an outer modular flow, a type III₁ algebra, and a half-sided inclusion — structures that live only in the continuum local algebra, which the finite record lattice cannot host intrinsically.** So sealed-record geometry is spin-2-*active* but not-a-graviton; a genuine propagating spin-2 (the real-time transverse-traceless sector, an emergent holographic bulk) is gated and remains [OPEN].

---

## 4. The open frontiers, and the emergent/intrinsic distinction

Two frontiers remain open; neither bears on the no-go of §2.

**Covariance of the dynamics. [OBSTRUCTED-leaning]** Done the causal-set way, discreteness covariantizes the *kinematics* outright: a Poisson sprinkling of division events is statistically Lorentz-invariant; the entropy-production arrow `σ = D(P_AB‖P_BA)` reads the frame-invariant causal partial order, not a preferred slice; and the free-flash localization dissolves Hegerfeldt's obstruction (a point-event sampled from a density, not a positive-energy state). The interacting-*distinguishable* dynamics is solved (Tumulka 2020 [12]). The genuine residue is a covariant interacting-*field* (variable particle number) record dynamics, which remains [OBSTRUCTED-leaning].

**The propagating graviton and the real-time dynamics. [OPEN]** Beyond the static modular-currency program lies the real-time transverse-traceless sector — the radiative, propagating content of gravity, whose quantum is the graviton. The split is sharp: an *intrinsic finite-record* graviton is obstructed (§3, the type-I/type-III₁ wall), while an *emergent continuum* graviton — gravity as an effective field theory of the coarse-grained metric, reached in a scaling limit — is open, not obstructed, and is the same continuum-limit program as reconstructing continuum field theory from the finite lattice. So the records carry the *equation of state* of gravity, and the *dynamics* of gravity (its radiative, propagating sector) is the emergent-continuum-limit frontier, not an intrinsic finite-record object.

The observability counterpart of these frontiers — whether the gravitational record process is genuinely indivisible, and whether that is measurable — is treated in the companion decoherence paper of this batch, which proves it is structural and not certifiable from the reduced channel.

---

## 5. Status ledger

| Object | Status | Statement |
|---|---|---|
| Temperature `T = a/2π` | **[DERIVED, mod R]** | established in the horizon paper; value rests on axiom (R) |
| Geometry factor `f_geom` (area coeff. + `l=0`) | **[DERIVED]** | `U_G = 1` to `~10⁻³` (straddles); Srednicki `0.295`, no fit |
| Angular first-law universality | **[OPEN]** | departs for `l ≥ 1`; measured, not closed |
| Horizon entropy = pure-area Wald charge | **[DERIVED, structural]** | `ds/dR = 0` by construction; corroborated by the floor-converged sweep |
| Clausius / modular first law → Einstein *form* | **[DERIVED, mod R + θ=σ=0 + focusing]** | full nonlinear via Clausius; linearized via `δS = δ⟨K⟩`; `η = 1/4G` |
| Cosmological constant `Λ₀` (unimodular) | **[DERIVED]** | non-sourced integration constant; Bianchi rerouted |
| Absolute scale `σ_A` ↔ `G` | **[NO-GO]** | `κ·σ_A` and `G·Λ²` fixed weight-zero invariants, scale free; weight-counting lemma; SIGMA-SPLIT; single premise gate G1 (seal-rate attack closes it); at audited scope |
| Linearized spin-2 (traceless) Einstein *equation* | **[DERIVED, mod R + gates]** | null-cone lemma fixes all 9 traceless comps; traceless *shape* scale-free (`G` remains on the RHS) |
| Spin-2 matter *charge* / propagating graviton | **[OBSTRUCTED → OPEN]** | non-universal + type-I + Berry + half-sided-inclusion; real-time TT sector gated |
| Covariant interacting *field* dynamics | **[OBSTRUCTED-leaning]** | kinematics covariantized; interacting-distinguishable solved; field case open |

---

## 6. What this paper does and does not claim

It **claims**: a derivation, from the sealed-record ontology, of the gravitational field equations as an equation of state (temperature + pure-area geometry-universal entropy + modular/Clausius first law), including the full nonlinear form and the linearized spin-2 (traceless) equation as a geometric identity, modulo the three named gates; and a no-go (at audited corpus scope, with gate G1 as its single load-bearing premise) that the absolute coupling `G` is not encoded in the records (`κ·σ_A` and `G·Λ²` weight-zero invariants; the weight-counting lemma; SIGMA-SPLIT).

It does **not** claim: a derivation of Newton's `G` (proved impossible, modulo the audit scope); a propagating graviton / quantum spin-2 charge (obstructed — the type-I/type-III₁ wall — and distinct from the derived equation); the real-time/radiative dynamics of gravity (open, the emergent-continuum frontier); a covariant interacting-field dynamics (open, with the kinematics covariantized); or the matter-sector hierarchy `c_m` (a separate, intrinsic, still-open dimensionless quantity the no-go does *not* forbid). The framing is thermodynamic: gravity as the equation of state of records, with the entropy-area density a calibration — and the theorem (at audited scope) that the missing datum is exactly *one absolute unit*. The honest one-line summary: **the records give gravity's form for free and prove they cannot give gravity's scale.**

---

## 7. Precision discipline

Every modular-kernel, near-vacuum, and weight-bookkeeping quantity was computed in mpmath at `dps ≥ 80` (commonly 100), with exact algebra (the weight degree map, SIGMA-SPLIT, the null-cone lemma, the trace-free / Bianchi identities, the de Sitter `l`-cancellation, the KMS detailed-balance and Rindler identities) in sympy. The receipt script `code/v6_pXI_sealed_record_gravity_nogo_receipts.py` reproduces the no-go and equation-of-state numbers below (the §1.2 geometry-universality constants — Srednicki's `0.295` [5] and the `U_G` ratio — are the corpus's spherical-ball partial-wave computation, separate from this receipt): the weight map (residuals `0`), the bijection `G·σ_A = 1/4` (weight `0`), SIGMA-SPLIT (`κ = 1` vs `3`, residual `0`), the two separate invariants `κ·σ_A = 2π` and `G·Λ²`, the de Sitter weight-twin (`N_dS` `l`-independent), the null-cone lemma (rank 9; pure-trace solution) together with the correct-versus-naive timelike statement, the spectral-action honesty check (the naive collar profile gives `f₂ = 1/(2π)² = 0.025330…`, *not* `1/(2π)`, so `G·Λ² = 3π²` does not follow), and the KMS/Rindler identities. Never float64 for the modular-kernel or near-vacuum quantities, where the corpus audit shows a 25–32% artifact.

---

## References

**Companion papers.**

[V] *Quantum theory from sealed records I–II*, companion papers (`paper-Va-foundations-1`, `paper-Vb-foundations-2`) — axioms R, S, C; the `q = 2` weight calculus; Lorentz signature from commitment order.
[VIII] *Horizon thermodynamics on record lattices*, companion paper (`paper-VIII-horizons`) — temperature two ways (Euclidean cone `β = 2π/κ` and Bisognano–Wichmann modular structure), censorship, greybody impedance, capacity; the input for §1.1.
[X] *Gravitational decoherence does not certify its mechanism*, companion paper (`paper-X-gravitational-decoherence`) — the operational-undecidability counterpart of the open covariance/indivisibility frontier of §4.

**External.**

[1] T. Jacobson, *Thermodynamics of spacetime: the Einstein equation of state*, Phys. Rev. Lett. **75**, 1260 (1995).
[2] T. Jacobson, *Entanglement equilibrium and the Einstein equation*, Phys. Rev. Lett. **116**, 201101 (2016).
[3] C. Eling, R. Guedens, T. Jacobson, *Nonequilibrium thermodynamics of spacetime*, Phys. Rev. Lett. **96**, 121301 (2006).
[4] R. M. Wald, *Black hole entropy is the Noether charge*, Phys. Rev. D **48**, R3427 (1993).
[5] M. Srednicki, *Entropy and area*, Phys. Rev. Lett. **71**, 666 (1993).
[6] A. D. Sakharov, *Vacuum quantum fluctuations in curved space and the theory of gravitation*, Sov. Phys. Dokl. **12**, 1040 (1968).
[7] T. Padmanabhan, *Thermodynamical aspects of gravity: new insights*, Rep. Prog. Phys. **73**, 046901 (2010).
[8] E. Verlinde, *On the origin of gravity and the laws of Newton*, JHEP **04**, 029 (2011).
[9] H.-J. Borchers, *On revolutionizing quantum field theory with Tomita's modular theory*, J. Math. Phys. **41**, 3604 (2000).
[10] V. Chandrasekaran, R. Longo, G. Penington, E. Witten, *An algebra of observables for de Sitter space*, JHEP **02**, 082 (2023).
[11] N. Lashkari, J. Lin, H. Marrochio, R. Myers, R. C. Myers — *modular/relative-entropy first law and gravitational dynamics* (entanglement-equilibrium and JLMS lineage).
[12] R. Tumulka, *A relativistic version of the GRW flash model*, J. Stat. Phys. **125**, 825 (2006); and the interacting-distinguishable extension (2020).
