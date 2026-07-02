# The record click-law, XIV: owning the gap mechanism, importing the mode — the interacting Ginsparg–Wilson flow, the canonical-mode wall, and forced chiral-gap values with singly-gated species ratios

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-16. Fourteenth paper of the v7 program; the matter-sector entry. It reports a three-part split, each part honestly graded: a **constructive** result (the interacting record Ginsparg–Wilson flow, closing the named-open O8 remainder of v6 Paper 14), a **no-go** (the canonical mode is a third (matter) import-fixed wall), and a **sharpening** (chiral-gap values are record-forced; between-species mass ratios are singly gated). Tags: **[FORCED]** = uniquely required (symbolic / high-precision numeric); **[CONSTRUCTIVE]** = a built mechanism; **[NO-GO]** = a proved impossibility in scope; **[IMPORT]** = an input the records provably cannot supply; **[OPEN]** = a disclosed, unproved obligation. Structural/algebraic identities at mpmath `dps ≥ 120` or sympy-exact; lattice eigenvalue spectra and gap-equation traces are float64/extended, **every such digit flagged lattice-numeric, not high-precision**. Receipts `v7/code/s_igw_production_gap_flow.py` (9 checks), `s_mode_import_wall.py` (16), `s_chiral_gap_ratios.py` (14).

## Scope — four hard guards, stated first [FORCED scope discipline]

Because the words "matter sector" and "mass gap" invite overreach, the boundaries come before the results:

1. **This is the large-N Gross–Neveu *dynamical-mass mechanism*, not the Clay / pure-gauge Yang–Mills mass gap.** The Gross–Neveu four-fermi model is exactly solvable at large `N`; the dynamical mass is a *fermion* mass from chiral-symmetry breaking. The pure-gauge Yang–Mills mass gap (the Millennium problem) is a *different object*, owned separately by the program's Yang–Mills line, where it remains the nonperturbative core open for everyone. This paper does **not** address it.
2. **Large `N` is the controlled regime; finite `N` is open.** The exact solvability — and every claim below — lives in the large-`N` limit. The `1/N` corrections and the loss of exact solvability are not treated.
3. **Two dimensions, quenched / uniform-flux gauge background, small lattices** (`≤ 10×10`, within the v6 Paper 14 ceiling). The gauge field is not dynamical; 4d, unquenched dynamics, and confinement are untouched.
4. **The mass is mode-relative.** The coupling `g` and the absolute mode are *imported*. The mechanism that *gives* mass is owned; **no absolute number** is produced. The canonical-mode wall (§3) stands — and this paper proves it is genuine.

Inside those guards, the three results are machine-verified.

---

## 1. What the matter machinery already is, and what is new

The corpus already owns, as theorems with receipts (v6 Paper 14), the three constructive pieces an "it-from-qubit" picture usually assumes but never builds: an **exact record Ginsparg–Wilson (overlap) operator** `D = 1 + γ₅ sign(H)`, `H = γ₅ D_W` (GW identity `{γ₅, D} = D γ₅ D` an algebraic identity, residual `4.0 × 10⁻¹⁵`, gauge-covariant, exponentially local, a single species — Nielsen–Ninomiya evaded record-natively, 1 zero versus the naive 4); a **lattice index theorem** `index(D) = Q` exact in 14/14 flux sectors; and an **anomaly filter** (`index = qQ`, the minimal chiral stack `{1,4,4|2,2,5}`). The *free* operator and its *quenched* gauge response are built — the latter, a first Banks–Casher-flavoured condensate *signal*, in v6 Paper 22. v6 Paper 14 names the one remaining piece, its **O8 remainder**, precisely: the **interacting** (quartic, four-fermi) record flow. This paper closes it.

The novelty over Paper 22 is exact: Paper 22 exhibited a *quenched condensate signal* and listed the interacting flow as open. Here the interaction is **real** (a self-consistent four-fermi gap equation), the survival of the exact chiral symmetry through the interaction is **proven**, and the dynamical mass `M(g)` is **mapped across flux sectors**.

---

## 2. The constructive win: the interacting Ginsparg–Wilson flow [CONSTRUCTIVE]

### 2.1 The interaction preserves the exact Lüscher chiral symmetry

Give the overlap operator a mass the Lüscher-correct way, `D(M) = D + M(1 − D/2)`, with the deformed chiral generator `γ̂₅ = γ₅(1 − D)`. The chiral structure is **exact and survives the deformation**, by a backbone that is sympy-exact: writing `s = sign(H_W)` (so `s² = 1`, `γ₅² = 1`), the GW identity `{γ₅, D} − D γ₅ D = 0`, the Lüscher Ward identity `D γ̂₅ + γ̂₅^† D = 0` at `M = 0`, and the massive-Ward breaking `= M(γ₅ − s)` all reduce symbolically to identities. Numerically (mpmath `dps = 120`, the matrix sign computed by a structure-preserving scaled-Newton iteration that drives `‖s² − 1‖` to `< 10⁻¹²¹`; a naive `mpmath` eigendecomposition also reaches `< 10⁻⁹⁰` at this working precision and only floors near `10⁻⁶²` at low `dps ≤ 70`, so the scaled-Newton is a structure-preserving alternative, not a necessity), the GW and Lüscher residuals land `< 10⁻⁹⁰` in **all three** flux sectors `Q = 0, 1, 2` (e.g. `Q = 0`: `‖{γ₅,D} − Dγ₅D‖ = 4.8 × 10⁻¹²²`, `‖Dγ̂₅ + γ₅D‖ = 1.9 × 10⁻¹²¹`). The chiral-symmetry breaking is therefore **strictly `O(M)`**, with an `M`-*independent* coefficient `C = ‖γ₅ − s‖ = O(1)` (`0.507 / 0.582 / 0.648` for `Q = 0/1/2`): soft, with **no hard doubler**. The interaction does not spoil the record-native single species.

### 2.2 The gap equation: a dynamical mass from chiral-symmetry breaking

The large-`N` Gross–Neveu four-fermi interaction is exactly resummed by an auxiliary field into the self-consistent **gap equation**

`M = g²·Σ(M)`, `Σ(M) = (1/V)·Tr[(1 − D/2)·D(M)⁻¹]`.

Solving it (the self-consistency root at `dps ≥ 110`; the trace `Σ(M)` from the overlap spectrum is **lattice-numeric, float64-flagged**) yields a dynamical mass that is genuinely **interaction-driven**, not a free or Wilson-remnant mass: `M(g) = 0` identically below a sector-dependent threshold `g_c`, then turns on and grows **monotonically** (`Q = 0`: `M = 0.297, 0.762, 1.385, 1.907` at `g² = 3, 4, 6, 8`; `M(g² = 10⁻⁴) = 0` exactly). The anchor values are `M(g² = 4) = 0.762447 / 0.885544 / 0.786694` for `Q = 0/1/2`. The threshold `g_c²` **decreases with lattice size** (`3.63 → 2.79 → 2.35` for `L = 6, 8, 10`), the expected 2d trend toward chiral-symmetry breaking for any `g > 0` in the continuum.

### 2.3 The record topology in the order parameter

The mechanism carries the topology with it. As `M → 0` the condensate's zero-mode contribution diverges, `M·V·Σ(M) → n_zero` — where `n_zero` is the **total zero-mode count** (`n₊ + n₋ = 2 / 1 / 2` for `Q = 0/1/2`, residual `~10⁻⁵⁴`; every exact zero mode contributes `1/M`, *both chiralities*). The topological **index** is the *signed* part, `index(D) = n₋ − n₊ = Q` (`0 / 1 / 2`), and it equals the count **only in mono-chiral sectors**: at `Q = 1, 2` all zeros share one chirality so `n_zero = |index| = Q`, while at `Q = 0` the two zeros are an accidental **vector-like pair** (`n₊ = n₋ = 1`, so `index = 0` but `count = 2`) — exactly as v6 Paper 14 records (`"Q = 0 … index 0, accidental vector-like pair"`). So what is live in the order parameter is the record **topology** — the index theorem's zero modes appearing in the condensate, with the *count* in the divergence and the *index* as its signed/topological part. This is *not* the continuum Banks–Casher `ρ(0)` density, which **excludes** these zero modes; it is the finite-volume topological zero-mode term in a fixed sector. (The eigenvalues' float64 residue `~10⁻¹⁵` is roundoff; snapping the zeros to exact — the index-theorem statement, v6 Paper 14 — is a precision device to reach `M < 10⁻¹⁵`, not the source: *unsnapped*, `M·V·Σ` already equals `n_zero` to eight digits at `M = 10⁻⁶`.)

So the interacting record flow is a **record-native dynamical-mass mechanism**: it realises, entirely from the record overlap operator, the same chiral-symmetry-breaking mechanism that *in QCD* gives light fermions a constituent mass — with the topology in the condensate — here in the 2d large-`N` Gross–Neveu toy, inside the four guards of the scope block.

---

## 3. The canonical mode is a third (matter) import-fixed wall [NO-GO]

The mechanism gives `M` *relative to a mode and a coupling*. Can the records select the absolute mode — which ledger rank is physical? They cannot, and the no-go is now decisive.

### 3.1 The rank is a superselection invariant

A seal mode is a ledger of orthogonal primitive characters of the parity group `(ℤ/2)ⁿ`; its **rank** (`= 2ⁿ − 1`, the number of such characters, `1/3/7` for `n = 1, 2, 3`) is a **superselection invariant** — the characters are orthonormal (Gram `= I`, sympy-exact) and the rank is preserved by every record-internal move (sign-flip, permutation, the firing map). Distinct ranks are gauge-*inequivalent* sectors — the Wen-PSG hallmark.

### 3.2 The common-zero obstruction

The "sole escape" Paper VIII left — a matter Hamiltonian energetically selecting a rank — requires a **cross-sector ground-energy comparison**, hence a **common energy zero** across the gauge-inequivalent sectors. The records supply no such zero. Each sector measures its content only against *its own* uniform reference `U_r` of dimension `2ⁿ`: re-referencing across sectors shifts the content by exactly `(n′ − n) ln 2`, **independent of the state** (sympy-exact: the entropy `H(P)` cancels identically). So each sector's zero is free up to an independent additive constant the records never fix, and the cross-sector comparison the selector needs does not exist record-internally.

### 3.3 The choice relocates, never closes

Concretely, the simplest free-energy `F_α = C_ext − α·\ln(\text{modes} + 1)`, with `C_ext = m·C` the *extensive* (summed) content (distinct from the per-sector joint relative entropy `D(P_r‖U_r)` of §3.2 — the common-zero core is independent of which is used), has an argmin that **switches rank** across level-crossings as `α` sweeps (`α = 0.168, 0.207, 0.247`), and **no crossing equals any forced click-law constant**: the nearest forced constant to any crossing is `W = 0.1561` at distance `0.012` (`η_B = 0.6094` is `0.44` away). Even `α = 0` is convention/Hamiltonian-form dependent. The switching is *structural* — it happens for **every** monotone multiplicity reward (log, linear, spin, √, squared), not a rigged form. So a mode-selecting Hamiltonian does not *break* the wall; it *relocates* the undetermined choice into its own free coupling.

### 3.4 The matter member of the import family

The canonical mode therefore passes all the weight-`0` import diagnostics — the form is forced in *every* sector, the cross-sector selector needs an import, and no forced constant lands it — and joins the program's **three SHARD-specific last inputs**: the absolute scale `l_step`/`G`, the composite tensor product `χ_AB`, and now the **canonical mode**. Three orthogonal last-input walls of **different grade and epistemic status** — the scale a weight-`(+1)` grading obstruction (genuinely measured), `χ_AB` a weight-`0` field/symmetry obstruction (a now-contested composition-rule convention), the mode a weight-`0` relocation obstruction (import-fixed by measured spectra); the canonical mode is the *matter* member. (Paper VIII named it the "fifth wall" in its broader enumeration of named obstructions; here it is the third last input, the second *weight-`0`* member.)

---

## 4. Chiral-gap values are forced; species ratios are singly gated [FORCED + sharpening]

What, then, *is* record-forced about masses? The gap *values*, but not the species *assignment*.

**The values are forced pure numbers.** Each oriented/chiral minimum gap (Paper IX) `m_min(n) = −ln(1 − 2⁻ⁿ) − δ_n` is a record-forced number in nats, a function of the spin-count `n` *alone*, whose **value is free of all three gated inputs**: `l_step` (it is dimensionless), `χ_AB` (a single-party KL number, no tensor split), and the chirality bridge *in value* (handedness-blind; the bridge enters only the species *name*, §4 below). The anchors are computable to 100+ digits (`m_min(3) = 0.13353098207247…`, `m_min(4) = 0.06453852113757…`, `m_min(5) = 0.03174869831458…`, dps 140), the prefactor `m·2ⁿ` decreases to `1` from above (`1.068, 1.033, 1.016, 1.008, …`), and the adjacent ratios decrease toward `2` (`2.0690, 2.0328, …`). Any **within-pair** ratio `m_min(n)/m_min(n′)` is therefore a forced pure number, computable to 100+ digits.

**The species ratio is singly gated.** A *physical* between-species mass ratio is `m_min(n_1)/m_min(n_2)` for the two species' ranks — and it is gated by **one** import alone: the **rank assignment** (which `n` ↔ which physical species), which is exactly the mode wall of §3. Because the ratio is `n`-dependent (the menu spreads by `0.067`), the assignment is load-bearing: it *changes the number*. This **sharpens** Paper VIII's "doubly gated" to **singly gated** — the chirality bridge (Paper IX's handedness no-go) and the Wen-PSG cohomology (Paper IX's no-Wen-PSG-without-geometry) both collapse *into the assignment*: they fix the species *name*, not the gap *value*; and the `n → ∞` asymptotics are now theorems (Paper IX). The only **assignment-free** numbers are *limits*, not species ratios: `lim_{n→∞} m_min(n)/m_min(n+1) = 2` and the prefactor `→ 1`.

---

## 5. The matter-sector verdict

Put the three parts together and the matter sector resolves cleanly, with no overclaim:

> **"Build the matter sector" = "own the gap mechanism, import the mode-selector."** The interacting record Ginsparg–Wilson flow *owns* the dynamical mass-gap mechanism (chiral-symmetry breaking with the record topology — the index theorem's zero modes — in the order parameter, large-`N`, the exact Lüscher symmetry intact). The canonical mode is the third (matter) last-input wall — weight-`0` like `χ_AB` (unlike the weight-`(+1)` scale/`G`), import-fixed by the measured spectra. And the chiral-gap *values* are record-forced pure numbers, while every between-species mass *ratio* is *singly* gated by the rank assignment alone.

This is why no single physical mass ratio is computable now, stated precisely: not because the gap is unknown (it is a forced number to 100+ digits), but because *which* gap belongs to *which* particle is the one import the records cannot supply — the mode. The meta-pattern is complete on the matter axis: the records force the *mechanism and the values*, and import the *one last assignment*.

---

## 6. Open residues [OPEN]

Listed prominently, not buried:

1. **Finite `N`.** The entire constructive win is the large-`N` (exactly solvable) Gross–Neveu mechanism; the `1/N` corrections and the loss of exact solvability are open.
2. **Dimension and background.** 2d, quenched / uniform-flux (the gauge field is *not* dynamical); 4d, unquenched dynamics, and the area-law / confinement question are untouched.
3. **The Clay gap.** The pure-gauge Yang–Mills mass gap is explicitly *not* addressed — a different object, owned separately by the program's Yang–Mills line, and the nonperturbative core open for everyone. The Gross–Neveu mass is a *dynamical fermion* mass from chiral-symmetry breaking, not the pure-gauge gap.
4. **The mode import.** The canonical mode is proven un-supplied internally (§3); a mode-selecting matter Hamiltonian relocates rather than closes the choice. Closing it requires an external input — like `G` (genuinely measured); unlike `χ_AB`, whose closure is itself a now-contested composition-rule convention, possibly unfixable in principle.

None of these weakens the three results inside their stated scope; they are the boundary of the matter-sector claim.

---

## Reproducibility

Three receipts in `v7/code/`, deterministic, single-threaded, exit `0`, **39 machine checks total**, with an explicit per-check precision ledger (structural/algebraic high-precision or sympy-exact; lattice spectra float64-flagged).

- **`s_igw_production_gap_flow.py`** (9/9). The interacting GW flow. The sympy-exact backbone (`{γ₅,D} = Dγ₅D`, the Lüscher Ward, breaking `= M(γ₅ − s)`, `γ̂₅ = −s`); the GW/Lüscher/involution residuals `< 10⁻¹²¹` (dps 120, scaled-Newton matrix sign; a naive `mpmath` eig also reaches `< 10⁻⁹⁰` at dps 120) in `Q = 0,1,2`; the gap equation `M(g²)` (root dps ≥ 110, trace float64-flagged) with `M(g²=4) = 0.762447/0.885544/0.786694`, `M = 0` below `g_c`, monotone above, `g_c²` decreasing `3.63 → 2.35` with `L`; the topology in the order parameter `M·V·Σ → n_zero` (the total zero-mode **count** `2/1/2`, residual `~10⁻⁵⁴`), with an explicit chirality split (`count = n₊+n₋` vs `index = n₋−n₊ = Q = 0/1/2`; `count = |index|` only for mono-chiral `Q = 1,2`; `Q = 0` is a vector-like pair, count 2 > index 0). The zero-snap is the index theorem (v6 Paper 14); the unsnapped trace already shows `n_zero` at `M = 10⁻⁶`.
- **`s_mode_import_wall.py`** (16/16; 2 sympy-exact, 11 mpmath `dps = 120`, 3 structural, 0 lattice-numeric). The rank superselection invariant (Gram `= I`); the common-zero obstruction (cross-sector shift `= (n′−n)\ln 2`, state-independent, sympy-exact `H(P)` cancellation); the argmin switching (crossings `0.168/0.207/0.247` of the extensive content `m·C`; the nearest forced constant to any crossing is `W = 0.1561` at distance `0.012`, `η_B` is `0.44` away — no crossing equals any forced constant) for every monotone reward; `η_B = 0.6093778634360062` (residual `9.2 × 10⁻¹²⁸`), `W = 0.1561092001572401`.
- **`s_chiral_gap_ratios.py`** (14/14, dps 140). The forced gap values (`m_min(3,4,5)` to 40+ digits, computable to 100+), free of all three gates; the decreasing prefactor `→ 1` and adjacent ratios `→ 2`; the within-pair forced ratios; the between-species singly-gated result (the doubly-`→`-singly sharpening); the assignment-free limits. `δ_n > 0` is structural (the upper-value argument), with the `n ≥ 7` precision underflow at `|δ| ~ 10⁻¹³⁰` honestly flagged (strict positivity verified `n ≤ 6`).

Never float64 for the algebraic GW/Lüscher identities, the KL contents, or the chiral-gap values; the lattice eigenvalue spectra and gap-equation traces are float64/extended and flagged as such.

## References

**This program.**
- *Relativistic ISP v6, Paper 14* — the record Ginsparg–Wilson operator, the lattice index theorem, the anomaly filter, and the **O8 remainder** (the interacting flow) closed here.
- *Relativistic ISP v6, Paper 22* — the prior art: the quenched record-GW condensate signal (Banks–Casher-flavoured), over which this paper's interacting self-consistent gap and Lüscher-survival proof are the novelty.
- *The record click-law, VIII* (v7 paper 8) — the matter-sector synthesis and the mode-canonicalisation wall (M2), here proven a third (matter) import-fixed wall.
- *The record click-law, IX* (v7 paper 9) — the closed chiral-gap law `m_min(n) = −ln(1−2⁻ⁿ)−δ_n`, the PSG-ingredient functor, and the chirality no-go; the species-naming gates that collapse into the assignment.
- The program's Yang–Mills line — the pure-gauge / Clay mass gap, owned separately and explicitly not closed here.
- *Emergent Einstein equations without an emergent Newton constant* (Paper 57) and *The record click-law, XII–XIII* — the other two import-fixed walls (`l_step`/`G`; the tensor product `χ_AB`) the canonical mode joins.

**External (invoked, not re-derived).**
- P. H. Ginsparg, K. G. Wilson, *A remnant of chiral symmetry on the lattice*, Phys. Rev. D **25**, 2649 (1982); H. Neuberger, *Exactly massless quarks on the lattice*, Phys. Lett. B **417**, 141 (1998); M. Lüscher, *Exact chiral symmetry on the lattice and the Ginsparg–Wilson relation*, Phys. Lett. B **428**, 342 (1998).
- D. J. Gross, A. Neveu, *Dynamical symmetry breaking in asymptotically free field theories*, Phys. Rev. D **10**, 3235 (1974) — the large-`N` four-fermi dynamical-mass mechanism.
- T. Banks, A. Casher, *Chiral symmetry breaking in confining theories*, Nucl. Phys. B **169**, 103 (1980) — `ρ(0) ∝ ⟨ψ̄ψ⟩`.
- H. B. Nielsen, M. Ninomiya, *Absence of neutrinos on a lattice*, Nucl. Phys. B **185**, 20 (1981) — the no-go the record overlap evades.
- X.-G. Wen, *Quantum orders and symmetric spin liquids*, Phys. Rev. B **65**, 165113 (2002) — the projective symmetry group / superselection structure the rank invariant instantiates.
