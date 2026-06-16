# Gravitational decoherence does not certify its mechanism: the Gaussian onset, CP-divisibility, and an operational undecidability theorem

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-14. Every load-bearing line is tagged by epistemic status: **[THEOREM]** = proved here (symbolic or high-precision numeric); **[RESULT]** = an established external or corpus result used as input; **[OPEN]** = an unsolved obligation. All numeric claims were verified at mpmath `dps ≥ 80` (commonly 100) and symbolically (sympy) where exact; the receipt script is `code/v6_pX_decoherence_undecidability_receipts.py`.

## Abstract

A gravitationally induced loss of matter coherence is the most-discussed empirical window on the quantum–gravity interface, and a recurring claim is that its *shape* — most often a short-time **Gaussian onset** `|ρ₀₁(T)| = e^{−½(T/τ_G)²}`, as in finite-memory variants of the Diósi–Penrose proposal — diagnoses the underlying mechanism (non-Markovianity, state-dependence, or a genuinely quantum-gravitational record process). We prove the opposite, in a sharp and useful form: **the gravitational dephasing curve is mechanism-blind, and the structural distinction that would mark a quantum-gravitational record process is not a function of the reduced channel.** Three results, each computed at high precision. (i) The Gaussian onset is *not a signature*: a state-independent, irreversible record commitment ("seal") firing at a ramping hazard `λ(t) = a t` reproduces it exactly (`|ρ₀₁(T)| = e^{−aT²/2}`, residual `0`), and a constant hazard gives the pure exponential semigroup — the most Markovian channel there is. (ii) Any state-independent irreversible seal is **CP-divisible**: `|ρ₀₁(T)| = e^{−∫₀ᵀλ}` is monotone, so it can *never* produce revivals; revivals occur exactly for Gaussian kernels whose running integral goes negative — the underdamped (still spectrally positive) kernel is the canonical case, with the boundary at `ω₀τ = 3.644173671645632…` — a non-Markovianity **orthogonal** to the structural axis. (iii) **Operational undecidability from the dephasing curve:** a continuous (Ornstein–Uhlenbeck) classical-noise ontology and a matched sparse-seal record ontology produce **bit-identical free-induction coherence** `|ρ₀₁(T)|` for all `T` (the identity `∫λ_OU = χ` is sympy-exact; an independent numerical integration gives the machine-zero residual `max|C_OU − C_seal| = 7.1×10⁻¹⁰²`), so free-induction decay cannot separate them. Multi-time dynamical decoupling (echo/CPMG) *can* probe reversibility — it distinguishes a refocusable noise from an irreversible commitment — but the genuine quantum-gravitational content, whether the matter's *closed-system* record process is *indivisible* in Barandes' sense / *unrefinable* in the sealed-record sense, is **structural** (the off-diagonal support of the decoherence functional between sparse commitments) and is *invisible to passive reduced-channel measurement*, at every order, because a bath dilation is always divisible and a closed unitary system is indivisible yet a trivial channel (an invasive protocol that reconstructs `Γ(t)` would insert a seal at each conditioning step, and so cannot certify the unintervened process — §6, O7). We make the structural axis precise, exhibit the consistent-histories functor that turns "unrefinable ⟺ indivisible" into a theorem at the kinematic level, and isolate the one open obligation (whether the gravitational record process is sparsely or continuously sealing). The widely used finite-memory Diósi–Penrose-family kernel is, on this analysis, *one illustrative CP-divisible member of the undecidable class rather than a discriminating prediction.* The practical upshot is a sharpened no-go: a free-induction onset-shape measurement, however precise, does not distinguish gravitational quantum decoherence from classical gravitational noise — the reversibility of the mechanism is probed only by multi-time decoupling, and the structural indivisibility that would mark a genuinely quantum-gravitational record process is reachable by no reduced-channel measurement at all.

---

## 1. The question, and why the obvious answer is wrong

Suppose two branches of a massive body's wavefunction carry distinct mass-density configurations, so that a relative gravitational self-energy `ΔE_G` accumulates a relative phase. A gravitationally induced decoherence model posits that this phase is degraded — the off-diagonal `ρ₀₁(T)` of the which-path density matrix decays — and proposes a decay law. The Diósi–Penrose (DP) proposal gives a short-time **exponential** `e^{−T/τ_G}` with `τ_G = ℏ/E_G`; finite-memory variants instead give a **Gaussian onset** `e^{−½(T/τ_G)²}` crossing over to the DP slope at late times. A large experimental program — interferometric and (dominantly) non-interferometric — aims to measure this decay and thereby test "gravitational" collapse against quantum mechanics.

The temptation, repeatedly voiced, is to read the *shape* of the decay as a fingerprint of the mechanism: a Gaussian (rather than exponential) onset is taken as evidence of finite memory / non-Markovianity, and non-Markovianity in turn as a hint of a genuinely quantum-gravitational, non-classical record process. **Each link in that chain fails.** This paper proves three obstructions that, together, say the reduced channel is mechanism-blind, and then locates precisely where the genuine content does live.

The setup is the standard one. For a stationary Gaussian pure-dephasing channel,

  `C(T) ≡ |ρ₀₁(T)|/|ρ₀₁(0)| = e^{−χ(T)}`,  `χ(T) = (1/ℏ²)∫₀ᵀ (T−s) K(s) ds`,

with `K(s) = ⟨δE_G(0) δE_G(s)⟩` the noise autocorrelation, and the instantaneous dephasing rate is `γ(T) = 2χ′(T) = (2/ℏ²)∫₀ᵀ K(s) ds`. The DP-family kernel is the Ornstein–Uhlenbeck (exponential) form `K(s) = σ² e^{−|s|/τ_c}`; we return to it in §5. The point of departure is that the *closed-system* record process underlying such a channel — the sealed-record ontology in which a "division event" commits a which-path record and the gravitational holonomy between events is a coherent, uncommitted phase — is a *different* object from the noise `δE_G(t)`, and the two can be told apart, if at all, only structurally.

---

## 2. Three inequivalent senses of "Markovian", and where the fingerprint lives

The word "Markovian" collides three inequivalent notions, and a given model's status flips between them. Naming them is what dissolves the false chain of §1.

1. **Constant-rate semigroup** (time-homogeneous Lindblad). A finite-memory channel is *not* this: its rate `γ(T)` is time-dependent — that time-dependence *is* the Gaussian onset. This is the only sense in which "the Gaussian-onset channel is non-Markovian" is unambiguously true, and it is the weakest sense.
2. **CP-divisibility** (the RHP/BLP sense: a time-dependent but pointwise-positive rate, no information backflow). A channel is CP-divisible **iff `∫₀ᵀ K(s) ds ≥ 0` for all `T`** — equivalently `γ(T) ≥ 0`, `|C(T)|` monotone non-increasing. This is *strictly stronger* than the kernel being positive-type (spectral density `S(ω) ≥ 0`): positivity of `S` is a statement about the *full-line* Fourier transform of `K`, while CP-divisibility is governed by the sign of the *finite running integral* `∫₀ᵀ K`.
3. **Markov embeddability** (dilation to a memoryless process on a larger space). By Mori–Zwanzig essentially every physical channel has one; the OU kernel is a 1-D Ornstein–Uhlenbeck embedding, the underdamped kernel of §3 a 2-D one.

These three axes are **orthogonal**, and all corners are populated:

- A closed unitary qubit is **indivisible** in Barandes' structural sense (§4) yet, as a channel, *trivial* (no decoherence at all) — structural indivisibility with no operational signature.
- An underdamped Gaussian noise is **non-CP-divisible** (it revives, §3.4) yet **Markov-embeddable** and *not* structurally indivisible — an operational signature with no structural content.

So **CP-divisibility and structural indivisibility are independent axes; non-CP-divisibility is neither necessary nor sufficient for the structural barrier.** The whole of §3 is the consequence of taking this seriously: the things one can measure on `|ρ₀₁|` (rate time-dependence, revivals) live on axes 1–2, while the quantum-gravitational question of interest lives on a fourth, structural, axis that §4 makes precise.

---

## 3. The reduced channel is mechanism-blind: three theorems

We take the closed-system object seriously: a which-path qubit whose branches carry distinct gravitational records, with a deterministic holonomy `Φ(t) = (1/ℏ)∫₀ᵗ ΔE_G dt′` between **division events** (seals), and a **state-independent** irreversible seal firing at hazard `λ(t) ≥ 0`. A seal commits the which-path record; irreversibility means the branch–record overlap `⟨E₀(t)|E₁(t)⟩` is a non-increasing contraction. Then

  `ρ₀₁(T) = e^{iΦ(T)} ⟨E₀(T)|E₁(T)⟩ ρ₀₁(0)`,  `|ρ₀₁(T)| = e^{−∫₀ᵀ λ(t) dt}`.

### 3.1 The Gaussian onset is not a signature [THEOREM]

A **ramping** hazard `λ(t) = a t` gives `∫₀ᵀ λ = aT²/2`, hence

  `|ρ₀₁(T)| = e^{−aT²/2}`,

which is *exactly* the Gaussian onset with `a = 1/τ_G²` (symbolic identity; numeric residual `0.0` at every `T` on the grid `{0.1,…,7}`, `dps = 100`; e.g. `e^{−a·3.5²/2} = 2.1874911181828851…×10⁻³`, residual `0`). The initial slope `d/dT ln|ρ₀₁|` vanishes at `T = 0` — the quadratic (Zeno-like) onset — with no fine-tuning. A *constant* hazard `λ ≡ λ₀` instead gives the pure exponential semigroup `e^{−λ₀T}`, the most Markovian channel of all. **The onset shape is set by the time-profile of a state-independent commitment rate, and carries no information about whether the underlying process is classical noise or a quantum record process.** The Gaussian is the ramp; the exponential is the constant; neither is a fingerprint of anything but `λ(t)`.

### 3.2 State-independent irreversible sealing is CP-divisible — it cannot revive [THEOREM]

Because `λ(t) ≥ 0`, the coherence `|ρ₀₁(T)| = e^{−∫₀ᵀ λ}` is **monotone non-increasing**: the channel is CP-divisible, with no information backflow and no revivals, for *every* state-independent irreversible seal. For the DP-family OU kernel this is explicit: `∫₀ᵀ K = σ²τ_c(1 − e^{−T/τ_c}) ≥ 0`, so `γ(T) = (2σ²τ_c/ℏ²)(1 − e^{−T/τ_c}) ≥ 0` (the rate minimum over a wide grid is `0.0`, attained at `T = 0`). A non-monotone `|ρ₀₁|` would require `⟨E₀|E₁⟩` to *grow* — the record returning which-path information, i.e. reversible echo / an information-preserving bath (by definition *not* a committed record), or a seal reading the coherence to engineer refocusing (the forbidden nonlinear state-dependence; §6, O2). Hence the dichotomy, with no middle ground:

  **state-independent + irreversible ⟹ monotone, CP-divisible, no revival;  revivals ⟹ no committed record, or state-dependence.**

### 3.3 Operational undecidability: continuous noise and sparse sealing give identical free-induction decay to all orders (in T) [THEOREM]

The decisive obstruction. Take the DP-family OU dephasing curve `C_OU(T) = e^{−χ(T)}`. Its CP-divisibility (§3.2) means its equivalent instantaneous hazard `λ_OU(t) = χ′(t) = (σ²τ_c/ℏ²)(1 − e^{−t/τ_c})` is globally `≥ 0` — hence `λ_OU` is *itself* a legitimate state-independent irreversible-seal hazard. A sparse-seal record process with that hazard therefore reproduces the continuous-noise coherence **to all orders**:

  `∫₀ᵀ λ_OU(t) dt = χ(T)` identically (sympy-exact), so `C_seal(T) = e^{−∫λ_OU} = e^{−χ(T)} = C_OU(T)` for all `T`.

Numerically, integrating `λ_OU` independently and comparing, `max|C_OU(T) − C_seal(T)| = 7.1×10⁻¹⁰²` across `T ∈ {0.1,…,10}` at `dps = 100` (machine zero). The "order of first disagreement" between a *truncated* seal model and OU (`O(T³)` for a ramp, `O(Tⁿ)` for an `n`-term hazard) is a free truncation knob, not physics; at full resolution the two coincide exactly. So **free-induction decay does not separate the continuous-noise ontology (gravity as a classical stochastic field) from the matched sparse-seal ontology (gravity as a discrete record process)** — the single-time curve, and the Gaussian-equivalent two-time function it implies, are shared (the genuine multi-time statistics differ, as the next paragraph notes).

This is a statement about *free induction*, and that is where to be careful. A multi-time **dynamical-decoupling** sequence (spin echo, CPMG) is *not* a function of `|ρ₀₁(T)|` alone: it refocuses reversible phase accumulation, so it *can* separate a refocusable noise (whose coherence echo restores) from an irreversible commitment (whose committed records echo cannot undo), and it is sensitive to the non-Gaussian higher cumulants by which the two models differ. So *reversibility is an accessible discriminant.* What is *not* accessible at any order is the **structural** axis of §4 — whether the matter's *closed-system* record process is indivisible: a bath dilation is always divisible (§4.1) and a closed unitary system is indivisible yet a trivial channel (§2), so no *passive* reduced-channel measurement, free-induction or multi-time, is a function of it; an *invasive* protocol that reconstructs `Γ(t)` requires intermediate conditioning measurements, but each such measurement inserts a seal, so it cannot certify the *unintervened* process's indivisibility (the do-delete obstruction; §6, O7). The dephasing curve hides the mechanism; the whole channel hides the structure.

### 3.4 What a revival would, and would not, buy you [THEOREM]

Revivals (operational non-Markovianity, axis 2) are reachable — but only off the committed-seal class, and they still do not reach the structural axis. The equally positive-type **underdamped** kernel `K(s) = σ² e^{−|s|/τ} cos(ω₀ s)` (a Lorentzian-pair spectrum, `S(ω) ≥ 0`) has running integral

  `∫₀ᵀ K = σ²τ · [1 + e^{−T/τ}(ω₀τ sin ω₀T − cos ω₀T)] / (1 + (ω₀τ)²)`,

whose minimum over `T` first dips below zero at

  `(ω₀τ)_* = 3.644173671645632136171…`

(the value where the running integral becomes tangent to zero; `dps = 80`), and is negative for `ω₀τ > (ω₀τ)_*` — verified revivals at `ω₀τ = 5` (`γ_min = −0.0729` at `T_* = 0.9425`) and `ω₀τ = 10` (`γ_min = −0.1038` at `T_* = 0.4712`). So revivals are a property of the *kernel's oscillation*, available within Gaussian noise, and they certify only non-CP-divisibility. A sharper, genuinely discrete fingerprint is the bimodal limit `δE_G = ±σ_E`, giving `C(T) = cos(σ_E T/ℏ)` (symbolic; `max` residual `5.5×10⁻¹⁰²`) — a hard which-path oscillation with `C(π) = −1`, distinct from the smooth Gaussian echo. This is the most diagnostic *observable* of discreteness, but it is a **diagnostic, not a definition**: it is neither necessary nor sufficient for the structural barrier (§2), and §3.2 shows a committed seal cannot produce it at all.

---

## 4. Where the content actually lives: the structural (indivisibility) axis

The quantum-gravitational question that the reduced channel cannot answer is whether the matter's gravitational record process is **indivisible**.

### 4.1 The barrier in two languages [RESULT: Barandes; sealed-record program]

Barandes specifies a process by its one-time-conditioned transition matrices `Γ(t)_{ji} = P(j\ \text{at}\ t \mid i\ \text{at}\ 0)`. The process is **divisible** (his Markovian) iff `Γ(t₂,t₀) = Γ(t₂,t₁)Γ(t₁,t₀)` for *every* intermediate `t₁`, and **indivisible** iff composition fails except at sparse **division events**. The stochastic–quantum correspondence makes the obstruction explicit, `Γ(t)_{ji} = |U(t)_{ji}|²`:

  `[Γ(t₂)Γ(t₁)]_{ji} = Σ_k |U(t₂)_{jk}|² |U(t₁)_{ki}|²`  (sum of path probabilities),

  `Γ(t₂t₁)_{ji} = |Σ_k U(t₂)_{jk} U(t₁)_{ki}|²`  (probability of the path sum),

and the gap between them is the **interference cross-term**. Divisibility holds exactly where that cross-term vanishes — a division event. In the sealed-record language the same line is the **unrefinability of the seal order**: between commitments the system carries a reversible holonomy (a closed phase, no committed value); one cannot insert an intermediate conditioning record without *sealing* it, and sealing destroys the holonomy and changes the process. *Refine ≡ insert an intermediate conditioning record ≡ compose the transition matrices ≡ Chapman–Kolmogorov*, so the two barriers are the same barrier. Two features matter here: (i) indivisibility is a property of the *closed system's own* transition law — a bath dilation always gives a *divisible* embedding, which is exactly why a noise model is structurally silent; (ii) it is a strictly *different* axis from open-system CP-divisibility (the closed unitary qubit is indivisible yet a trivial channel).

### 4.2 The functor: "unrefinable ⟺ indivisible" is a theorem at the kinematic level [THEOREM, kinematic; gravitational realization OPEN]

The bridge is the Gell-Mann–Hartle decoherence functional. A sealed-record history is a finite poset of seals `{e_k}` with a unitary holonomy `U_k` on each inter-seal interval and a pointer-basis commitment `{P_a}` at each seal. Define

  `D(α, α′) = Tr[ P_{a_n}^{(n)} ⋯ P_{a_1}^{(1)} ρ P_{a′_1}^{(1)} ⋯ P_{a′_n}^{(n)} ]`

on coarse-grained pointer histories, with the projectors evolved by the inter-seal holonomies, and read the one-time matrix from its diagonal, `Γ(t)_{ji} = D(j;i)`. Then the Tier-1 biconditional *is* the consistent-histories consistency condition:

  *Chapman–Kolmogorov holds across `t′` ⟺ the off-diagonal (interference) part of `D` vanishes at `t′` (medium decoherence) ⟺ `t′` is a seal.*

Forward: a projective commitment diagonalizes `D` at `t′`, which is exactly the probability sum rule (Chapman–Kolmogorov) for the pointer histories. Reverse: if `Γ` composes across `t′` for *all* boundary conditions, the interference terms must vanish at `t′`, i.e. the record is committed. So **unrefinable ≡ indivisible is a theorem of consistency** — *for a chosen projective seal-history model.* What is **not** thereby settled, and is the one open obligation, is whether the *gravitational* record process supplies these very seals; that is §4.3, not something the functor decides.

### 4.3 The one open question, sharply posed [OPEN]

  **Is gravitational record commitment sparse or continuous?**

If the gravitational records decohere the which-path *continuously* (medium decoherence at all times — the continuous-sealing limit), `D` is diagonal everywhere, the seal order is fully refinable, and the process is **divisible** (classical), with the dephasing curve of §5 its complete content. Genuine indivisibility requires *intervals on which `D` is non-diagonal* — interference surviving between sparse gravitational seals. This is a computation on the off-diagonal support of `D`, not on `|ρ₀₁|`, and by §3 it cannot be read off any coherence-decay measurement. It is the correct target, and it is open.

---

## 5. The Diósi–Penrose-family kernel, in its true status

The widely used finite-memory channel is a fully legitimate, empirically anchored member of the undecidable class — and nothing more. With the OU kernel,

  `χ(T) = (σ²τ_c²/ℏ²)(T/τ_c − 1 + e^{−T/τ_c})`,

which is quadratic at short times (`χ ≈ (σ²/2ℏ²)T²`, the Gaussian onset) and crosses over to the linear DP slope at `T ≫ τ_c`. Matching the onset to the DP scale `τ_G = ℏ/E_G` and the curvature condition `χ(τ_c) = 1` fixes the single internal time,

  `τ_c = √e · τ_G = 1.6487212707001281468486507878141635716537761007101 · τ_G`

(the fixed point `(τ_c/τ_G)² = e` is exact; residual `|χ(τ_c) − 1| = 7.1×10⁻¹⁰²` at `dps = 100`). The energy scale `E_G` is inherited from the DP geometric self-energy and is *not* derived here; the model is **rate-robust, not fit-free**. Its empirical content — the quadratic onset against the DP exponential, the `E_G`-scaling, the crossover, the small higher-cumulant (non-Gaussian) correction — is exactly what a free-induction experiment can access, and §3.3 is the statement that *the free-induction content is shared with the classical-noise ontology.* The kernel is therefore the program's **dense-seal Gaussian shadow** — it recovers the phenomenology and loses no empirical ground — and is, correctly, one illustrative CP-divisible member of the undecidable class, not the discriminating prediction the onset shape is often read as.

**[RESULT: DP-family phenomenology, ref. [11,12].]** In the large-object, large-displacement regime relevant to the experiments [11, 12], the finite-memory modification constrains only the model's regularization length `R_0` (per-nucleon emission `∝ 1/R_0³`) and decouples from the collective decoherence the interferometer measures (`∝ GM²/R`, `R_0`-independent); it does not *worsen* the radiation/heating bounds and in fact *suppresses* high-frequency (keV) emission. So the kernel survives the laboratory bounds — which is exactly why it is a viable member of the undecidable class, not a falsified one.

---

## 6. The observability ledger: what a measurement can and cannot decide

A coherence-decay experiment is a measurement of `C(T) = e^{−χ(T)}` and its statistics. The following constrain what such a measurement can certify; each is a [RESULT] (corpus or external) used as a constraint on the *interpretation*, not a new claim.

| # | Constraint | Consequence for a decoherence test |
|---|-----------|-------------------------------------|
| **O1** | The Gaussian onset is reproduced by a state-independent ramp (§3.1) | The onset *shape* certifies neither non-Markovianity in any strong sense nor a quantum-gravitational mechanism. |
| **O2** | State-independent irreversible sealing is CP-divisible (§3.2) | A revival, if seen, *rules out* a committed-record interpretation of that channel (forces reversibility or state-dependence); its absence certifies nothing. |
| **O3** | OU-noise and matched sparse-seal share the free-induction curve (§3.3) | Free-induction decay does not distinguish classical gravitational noise from a discrete record process; multi-time decoupling probes reversibility, but the *structural* axis (O4–O5) is invisible to the whole channel. |
| **O4** | Bath dilations are always divisible (§4.1) | Fitting an open-system (master-equation) model can never exhibit the closed-system indivisibility, by construction. |
| **O5** | A closed unitary system is indivisible yet a trivial channel (§2) | The structural axis is not a channel property; it cannot be the output of any reduced-channel tomography. |
| **O6** | Bell non-evasion [RESULT: corpus] | The memory may not be used to signal or to evade Bell; the channel's non-Markovianity relocates nonlocality into memory, it does not remove it. |
| **O7** | Reconstructing `Γ(t)` needs intermediate conditioning [RESULT: do-delete] | An *invasive* multi-time protocol can reconstruct Barandes' `Γ(t)`, but each conditioning measurement inserts a seal (commits a record), so it cannot certify the *unintervened* process's indivisibility — the intervention is not an observational statistic. |

The reading is uniform: *every* discriminating question about the mechanism lives on the structural axis (§4), and the structural axis is provably not a function of the reduced channel. The one thing a measurement *can* do is constrain `E_G` and the onset time within the shared phenomenology — useful, but mechanism-blind.

---

## 7. What this paper does and does not claim

It **claims**, with verified mathematics: the Gaussian onset is reproduced exactly by a state-independent ramping seal and is not a mechanism signature (§3.1); any state-independent irreversible seal is CP-divisible and cannot revive (§3.2); continuous classical noise and sparse sealing produce identical reduced coherence to all orders, so the mechanism is operationally undecidable from the channel (§3.3); revivals are a separate, orthogonal axis reachable only off the committed-seal class (§3.4); and the structural (indivisibility) question is well-posed, reduces at the kinematic level to a consistency theorem via the decoherence functional (§4.2), and is invisible to `|ρ₀₁|`.

It does **not** claim: that the sealed-record/indivisible ontology is the *unique* mechanism (the undecidability cuts both ways — it equally forbids certifying *classical* noise); that the gravitational record process *is* indivisible (whether it is sparsely or continuously sealing is [OPEN], §4.3); that any observable non-Markovian fingerprint of indivisibility exists (§3.2 rules it out for the committed-record class); a derivation of general relativity, a graviton, or the Born rule; or a solution of the relativistic-collapse (Tomonaga–Schwinger) and covariant-localization (Hegerfeldt) obstructions, which bound any concrete realization. The finite-memory DP-family kernel is presented as one CP-divisible member of the undecidable class, not as a prediction.

The honest one-line summary: **gravitational decoherence has a shape, and the shape does not know its own cause; the cause is structural, and the structure does not show up in the decay curve.**

---

## 8. Precision discipline

Every quantity was computed in mpmath at `dps ≥ 80` (commonly 100), with sympy used for the exact identities (the Gaussian-onset integral, the OU running integral, the `λ_OU = χ′` all-orders identity, the underdamped running integral, the bimodal cosine). Float-safe small quantities are stated as such. The receipt script `code/v6_pX_decoherence_undecidability_receipts.py` reproduces every number in the canonical output block: the Gaussian onset (residual `0`), the CP-divisible OU rate (`γ_min = 0`), `√e = 1.6487212707…` (50 digits), the revival threshold `(ω₀τ)_* = 3.644173671645632…`, the all-orders identity `max|C_OU − C_seal| = 7.1×10⁻¹⁰²`, and the bimodal cosine (`max` residual `5.5×10⁻¹⁰²`). Never float64 for the kernel running-integrals or the all-orders comparison, where cancellation makes double precision unreliable.

---

## References

**External.**

[1] J. A. Barandes, *The stochastic-quantum correspondence*, arXiv:2302.10778 (2023).
[2] J. A. Barandes, *The stochastic-quantum theorem*, arXiv:2309.03085 (2023).
[3] R. Penrose, *On gravity's role in quantum state reduction*, Gen. Relativ. Gravit. **28**, 581 (1996).
[4] L. Diósi, *Models for universal reduction of macroscopic quantum fluctuations*, Phys. Rev. A **40**, 1165 (1989).
[5] L. Diósi, *A universal master equation for the gravitational violation of quantum mechanics*, Phys. Lett. A **120**, 377 (1987).
[6] M. Carlesso, L. Ferialdi, A. Bassi, *Colored collapse models from the non-interferometric perspective*, Eur. Phys. J. D **72**, 159 (2018).
[7] H.-P. Breuer, E.-M. Laine, J. Piilo, B. Vacchini, *Colloquium: Non-Markovian dynamics in open quantum systems*, Rev. Mod. Phys. **88**, 021002 (2016).
[8] Á. Rivas, S. F. Huelga, M. B. Plenio, *Quantum non-Markovianity: characterization, quantification and detection*, Rep. Prog. Phys. **77**, 094001 (2014).
[9] B. Misra, E. C. G. Sudarshan, *The Zeno's paradox in quantum theory*, J. Math. Phys. **18**, 756 (1977).
[10] M. Gell-Mann, J. B. Hartle, *Classical equations for quantum systems*, Phys. Rev. D **47**, 3345 (1993).
[11] S. Donadi et al., *Underground test of gravity-related wave function collapse*, Nat. Phys. **17**, 74 (2021).
[12] M. Carlesso, S. Donadi, L. Ferialdi, M. Paternostro, H. Ulbricht, A. Bassi, *Present status and future challenges of non-interferometric tests of collapse models*, Nat. Phys. **18**, 243 (2022).

**Companion papers.**

[V] *Quantum theory from sealed records I–II*, companion papers (`paper-Va-foundations-1`, `paper-Vb-foundations-2`) — axioms R, S, C; the `q = 2` weight calculus.
[XI] *Emergent Einstein equations without an emergent Newton constant*, companion paper (`paper-XI-sealed-record-gravity-no-go`) — the gravitational equation of state and the scale no-go; the indivisibility question of §4 is the observability counterpart of its open covariance frontier.
