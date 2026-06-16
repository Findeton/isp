# Sealing the Gravitational Holonomy: gravitational decoherence as record commitment (the Level-3 program)

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-14. **This is a program / roadmap paper, not a results paper.** Every load-bearing line is tagged by epistemic status: **[TARGET]** = a goal to be achieved; **[BUILD]** = an established corpus or external result to build on; **[CONSTRAINT]** = a result the construction must respect; **[OPEN]** = an unsolved obligation. Nothing here is claimed proved.

## Abstract

The corpus' gravitational-decoherence paper [X] is honest about its own status: it is a finite-memory Diósi–Penrose-family *phenomenology motivated by* indivisible stochastic processes (ISP), not a derived indivisible channel. The reason is sharp. Its concrete model — a renewal-reset noise `δE(t)` with memoryless (Poisson) division events — is **Markovian on the enlarged `(δE, age)` state**, and more strongly the resulting pure-dephasing channel is **CP-divisible** (the dephasing rate `γ(T) = 2χ'(T) = (2σ²τ_c/ℏ²)(1 − e^{−T/τ_c}) ≥ 0` for all `T`): no information backflow, no revivals. By the operational (divisibility) definition that channel is *Markovian*. So the model carries a finite memory *time* but never crosses the non-Markovian *barrier*. The classical noise treats the gravitational mismatch as a value that is recorded at every instant — **continuous sealing** — which is the opposite of a coherent holonomy.

This paper defines the **Level-3 program**: derive gravitational decoherence from the matter's *own* indivisible record process. The gravitational which-path is carried as an **unsealed holonomy** (a coherent, axiom-S-silent relative gravitational phase) *between* division events, and **decoherence = sealing** — a division event committing the gravitational which-path record and destroying the holonomy. The decoherence rate is the **seal (division) rate**; identifying it with the entropy-production rate `σ = D(P_AB ‖ P_BA)` of the arrow-positivity theorem [10] is a *proposed* law, not automatic. The genuine-indivisibility target is the **structural** one — the one-time transition law fails Chapman–Kolmogorov (Barandes) / the seal order is unrefinable (SHARD) — and is sharply distinct from the *operational* (CP-divisibility) axis; we show the two are **orthogonal**.

**A computed result of this paper.** The minimal state-independent sealing toy is settled, with no middle ground. A state-independent *ramping* seal hazard `λ(t) = a t` reproduces [X]'s Gaussian onset *exactly* (`|ρ₀₁(T)| = e^{−aT²/2}`), so the Gaussian shape is *not* itself a non-Markovian signature; but any state-independent irreversible seal gives `|ρ₀₁(T)| = e^{−∫λ}` monotone, hence **CP-divisible — it can never produce revivals**. Revivals (operational non-Markovianity) require either reversible, information-returning dynamics (no committed record) or a seal that reads the coherence (the forbidden nonlinear state-dependence, C5). Genuine indivisibility, if it lives here at all, therefore lives on the Barandes/SHARD *structural* axis and is invisible to the open-channel fingerprint.

We state the barrier in both Barandes' and SHARD's terms (as a *proposed exact dictionary* whose functor is the open obligation), give the construction's moving parts, list the corpus results to build on, and lay out a constraint ledger (ten corpus no-gos plus two of our own). The program is **open**; its honest Branch-A / Branch-B split is inherited from the causal-set gravity paper [1].

---

## 1. The gap this program addresses

The decoherence paper [X] establishes, with verified mathematics, that any finite-memory (no-white-component) gravitational noise replaces the DP exponential with a non-exponential decay whose short-time exponent is **quadratic** — the boxed Gaussian `C(T) = C(0)·exp[−½(T/τ_G)²]` at the rounded closure — crossing over to the DP slope at `T ≫ τ_c`. Its §4.3 division-event model derives the exponential kernel from a renewal-reset process and pins `τ_c = √e·τ_G ≈ 1.65 τ_G`. Its own M3 caveat states the honest scope: the renewal-reset realization is Markovian on `(δE, age)`, the finite memory lives in the reduced (noise-only) description, and the paper does **not** claim the reduced gravitational transition law is Barandes-indivisible. **[BUILD: X]**

The gap is therefore not empirical but structural. For a stationary Gaussian pure-dephasing channel the coherence is `C(T) = exp[−χ(T)]` with `χ(T) = (1/ℏ²)∫₀ᵀ(T−s)K(s)ds`, and the instantaneous rate is `γ(T) = 2χ'(T) = (2/ℏ²)∫₀ᵀ K(s)ds`. The channel is **CP-divisible** (RHP/BLP-Markovian, no information backflow) **iff `∫₀ᵀ K(s)ds ≥ 0` for all `T`** — equivalently `χ` monotone with non-decreasing slope, `|C(T)|` monotone non-increasing. This is *strictly stronger* than the kernel being positive-type (`S(ω) ≥ 0`): spectral positivity guarantees a legitimate Gaussian channel but is governed by the *full-line* Fourier transform of `K`, whereas CP-divisibility is governed by the sign of the *finite running integral* `∫₀ᵀ K`. [X]'s exponential (Ornstein–Uhlenbeck) kernel `K(s) = σ²e^{−|s|/τ_c}` has `∫₀ᵀ K = σ²τ_c(1 − e^{−T/τ_c}) ≥ 0`, so **its channel is genuinely CP-divisible** (`γ(T) = (2σ²τ_c/ℏ²)(1 − e^{−T/τ_c}) ≥ 0`). But a *general* Gaussian noise need not be: the equally positive-type underdamped kernel `K(s) = σ²e^{−|s|/τ}cos(ω₀s)` (a Lorentzian-pair spectrum, `S(ω) ≥ 0`) gives `γ(T) < 0` on sub-intervals once `ω₀τ ≳ 3.64`, producing coherence revivals and breaking CP-divisibility (verified numerically at `ω₀τ = 5, 10`). So the leak is specific to [X]'s *exponential* kernel, not to Gaussianity per se. **[BUILD: this paper, verified numerically]**

So [X]'s "non-Markovian" means only "not a constant-rate semigroup" (a time-dependent but positive rate). That is the weakest of the three inequivalent senses of non-Markovianity (§2.3), and it is *not* the sense in which a process is Barandes-indivisible or SHARD-unrefinable. A classical noise `δE(t)` is, by construction, a definite recorded value at every instant — it seals continuously — and a continuously-sealed process is fully refinable, fully divisible, and carries no holonomy. **The Level-3 program is the project of replacing continuous sealing by sparse sealing of a coherent gravitational holonomy.**

---

## 2. The non-Markovian barrier, made precise

### 2.1 Barandes: the barrier is Chapman–Kolmogorov composition (the interference cross-term) **[BUILD: 11,12]**

Barandes specifies a system by its one-time-conditioned transition matrices `Γ(t)_{ji} = P(j at t | i at 0)`. A process is **divisible** (his Markovian) iff `Γ(t₂,t₀) = Γ(t₂,t₁)·Γ(t₁,t₀)` for *every* intermediate `t₁`; it is **indivisible** iff composition fails except at sparse **division events**. The stochastic-quantum correspondence makes the obstruction explicit: `Γ(t)_{ji} = |U(t)_{ji}|²` for a unitary `U`, and

  `[Γ(t₂)Γ(t₁)]_{ji} = Σ_k |U(t₂)_{jk}|²|U(t₁)_{ki}|²`   (sum of path probabilities)

  `Γ(t₂t₁)_{ji} = |Σ_k U(t₂)_{jk}U(t₁)_{ki}|²`   (probability of the path sum).

The difference is the **interference cross-term** `2 Re Σ_{k<l} (…)` between intermediate "slits" `k`. Divisibility holds iff that cross-term vanishes; a division event is a time where it does (one path dominates, or phases have decohered — where a record may be inserted harmlessly). **The barrier is the gap between `|Σ|²` and `Σ|·|²`.** Two consequences matter here: (i) indivisibility is a property of the *closed system's own* transition law — a bath dilation gives a *divisible* embedding, which is exactly why [X]'s renewal model "leaks"; (ii) it is a strictly *stronger and different* axis than open-system CP-divisibility (a closed unitary qubit is Barandes-indivisible yet, as a channel, trivial).

### 2.2 SHARD: the barrier is the unrefinability of the seal order (unsealed holonomy) **[BUILD: Va, 4, 7, 10]**

SHARD makes the **record/seal** the primitive [4]: between record commitments the system carries a reversible **holonomy** (a closed exchange-defect phase, no committed value); at a seal a record **commits**, irreversibly. The dividing line, in these primitives:

- **Classical:** the history is a *refinable* chain of seals — every instant is (or may be) a committed record and record-to-record transitions compose. An intermediate conditioning record may be inserted for free.
- **Quantum:** the **sealed holonomy between records carries irreducible phase** — one cannot insert an intermediate record without **sealing** it, and sealing destroys the holonomy and changes the process.

So the SHARD barrier is exactly **"the seal order is unrefinable"** — the same property that, in the foundations paper, is argued to select the one timelike direction (the unrefinable order) while relational directions remain refinable [Va, 7 Gate 2a]. And it *is* Barandes' barrier, because **refine ≡ insert an intermediate conditioning record ≡ compose the transition matrices ≡ Chapman–Kolmogorov.** We state this as a *proposed exact dictionary* **[TARGET]** — the **functor** that maps a sealed-record history to Barandes' one-time transition matrices `Γ(t)` and turns "refinable ⟺ Chapman–Kolmogorov holds" into a theorem is itself the open obligation, not yet written:

  SHARD-*unrefinable* ≟ Barandes-*indivisible*;  sealed-holonomy-between-seals ≟ interference cross-term;  a SHARD seal ≟ a Barandes division event (the one place a record commits harmlessly — equivalently where decoherence/classicalization momentarily restores composition).

What SHARD adds over Barandes is the **ontology of the division events**, which Barandes leaves external: a division event *is* a record commitment (a seal) [3,4]; its irreversibility *is* the arrow of time, quantified by the order-evidence identity `σ = 𝔼[A_D] = D(P_AB ‖ P_BA)` [10, T2], with the no-silent-arrow theorem [10, T3] forbidding an eventless arrow and reflection positivity emerging as a theorem of indivisible ordered transports [10, T4]. Record symmetry-breaking — a division event sealing a branch — is the corpus' template for exactly the move this program needs [8]. The order-evidence identity `σ = D(P_AB ‖ P_BA)` is itself a corpus theorem **[BUILD: 10]**; the *further* identification **decoherence rate = seal rate = `σ`** is a proposed law of this program **[TARGET]**, not automatic — it needs a theorem (or explicit model) tying the record-commitment hazard to the thermodynamic entropy production, which the toy of §3/§6 makes concrete as the seal hazard `λ(t)`.

### 2.3 The three senses of "Markovian", and where the genuine fingerprint lives **[BUILD: this paper]**

Three inequivalent notions collide and the model's status flips between them:

1. **Constant-rate semigroup** (time-homogeneous Lindblad): [X] is *not* this (its rate is time-dependent — that *is* the Gaussian onset). This is the only sense in which "[X] is non-Markovian" is unambiguously true.
2. **CP-divisible** (RHP/BLP; time-dependent but positive rate, no information backflow): [X]'s Gaussian channel **is** this — hence "Markovian" operationally (§1).
3. **Markovian embedding** (dilation to a Markov process on a larger space): [X] **has** one (1-D Ornstein–Uhlenbeck) — generic, by Mori–Zwanzig.

The crucial point is that **these three axes are orthogonal**, and all the corners are populated. Escaping (1) is free (the time-dependent rate). Escaping (3) with a heavy-tailed renewal (CTRW) is non-embeddable but kills `τ_c` and introduces unphysical aging; we reject it. Escaping (2) — non-CP-divisibility, i.e. information backflow / revivals — is *not* the same as the Barandes/SHARD barrier and does *not* require non-Gaussianity: as §1 shows, an *oscillatory Gaussian* noise (underdamped kernel) is already non-CP-divisible, yet it remains Markov-embeddable (a 2-D Ornstein–Uhlenbeck on `(x, ẋ)`) and so is *not* Barandes-indivisible. Conversely a closed unitary system is Barandes-indivisible while, as a channel, trivial. So:

  CP-divisibility and Barandes-indivisibility are **independent axes**; non-CP-divisibility is neither necessary nor sufficient for crossing the structural barrier.

What is true — and weaker than a slogan equating them — is that **non-Gaussian revivals are a *stronger, more diagnostic* SHARD-like fingerprint than generic colored-Gaussian backflow**: the bimodal `δE = ±σ_E` limit gives `C(T) = cos(σ_E T/ℏ)`, a discrete-record oscillation distinct from the smooth Gaussian echo. The non-Gaussian fingerprint (Axis 3 of [X]) is therefore a *diagnostic to look for*, not a *definition* of the barrier. The structural target (Chapman–Kolmogorov failure / unrefinable seal order) is what the program must actually deliver; the operational fingerprint is a separate, optional demand — and §3 shows the simplest mechanism cannot meet it.

---

## 3. The Level-3 construction (the fully defined target)

**The object. [TARGET]** Between two coherent branches carrying distinct effective mass-density records, the relative gravitational self-energy accumulates a phase `Φ(t) = (1/ℏ)∫₀ᵗ ΔE_G(t′) dt′`. In DP/[X] this is promoted to a *classical random* `δE(t)` recorded at every instant; here it is instead a **`U(1)` gravitational which-path holonomy** `e^{iΦ}` carried on the record diamond [3,4], **unsealed** — a datum no record yet registers, hence silent under axiom S and gauge until committed — while the branches remain coherent.

**The dynamics. [TARGET]** A **division event** is a gravitational record commitment: a seal that reads out and commits the which-path holonomy, collapsing the coherent superposition of geometries into a committed record and so producing one quantum of decoherence. There is no separate collapse postulate; the seal *is* the record-stabilization of [X §2] given a discrete-event ontology. The reduced gravitational channel `Γ_grav` is built from a *sparse* sequence of such seals (not a continuum), so that between seals the holonomy is coherent (recoverable in principle — revival) and only at seals is it committed.

**The four pieces to specify. [OPEN]**

1. **The holonomy variable.** Exactly which closed exchange-defect holonomy on the record diamond [4] carries the gravitational which-path — presumably the relative-geometry holonomy whose generator is `ΔE_G`. Its `axiom-S` silence while unsealed is the formal statement that coherent which-path phase is not yet physics.
2. **The seal law (when a division event fires).** A **state-independent** clock (Constraint C5): the seal *rate* may key to the geometric distinguishability `E_G` (a c-number functional of the branch configurations, as in [X]), but the seal must **not** use the relative coherence/amplitude to decide *outcomes*. The natural candidate ties the seal rate to the entropy-production rate `σ` [10, T2], so that `decoherence rate = seal rate = σ(E_G)`.
3. **The record-memory between seals.** The holonomy accumulated since the last seal *is* the memory; the inter-seal interval is the record-memory time `τ_c`, recovering [X]'s `τ_c` as the mean inter-division time but now as a coherence interval rather than a noise correlation time.
4. **Born-weight preservation across seals.** The sealing must compose linearly and preserve the screen norm so that the `q = 2` (unitary) weight calculus survives (Constraint C8; [4 §8], [Va], R5/Banach–Lamperti).

**The success criterion, in two tiers.** *Tier 1 (the actual barrier)* **[TARGET]**: exhibit `Γ_grav(t)` whose one-time transition law **fails Chapman–Kolmogorov** between seals (Barandes-indivisible) / whose seal order is **unrefinable** (SHARD), while satisfying the constraint ledger of §5. This is the structural target and remains open (it needs the functor of §2.2). *Tier 2 (an added, optional operational demand)*: a non-CP-divisible reduced channel (revivals), so the indivisibility is *observable*. Tier 2 is *neither necessary nor sufficient* for Tier 1 (§2.3) — desirable for empirical distinguishability, but a separate ask.

**A computed result: the minimal toy settles Tier 2, and it is a no-go. [BUILD: this paper, verified numerically]** Take the simplest realization — a which-path qubit with deterministic holonomy `Φ(t)` (generator `ΔE_G`) and a *state-independent* irreversible seal firing at hazard `λ(t)`. Then `ρ₀₁(t) = e^{iΦ(t)}·⟨E₀(t)|E₁(t)⟩·ρ₀₁(0)`, and a genuine irreversible seal is exactly the statement that the branch–record overlap `⟨E₀|E₁⟩` is a non-increasing contraction; so `|ρ₀₁(T)| = e^{−∫₀ᵀλ}` with `λ ≥ 0` is **monotone — CP-divisible, never reviving**. Two consequences:

- **(a) the Gaussian onset is reproduced, and is not a signature.** A *ramping* hazard `λ(t) = a t` gives `|ρ₀₁| = e^{−aT²/2}`, so a state-independent seal **reproduces [X]'s Gaussian onset exactly** (C12 met) — and the Gaussian onset is therefore *not by itself* evidence of any non-Markovian or state-dependent mechanism. A constant hazard instead gives the pure exponential semigroup `e^{−λ₀T}` (the *most* Markovian channel).
- **(b) Tier 2 is unreachable by this mechanism, with no middle ground.** A non-monotone `|ρ₀₁|` requires `⟨E₀|E₁⟩` to *grow*, i.e. the record to *return* which-path information — reversible echo / an information-preserving bath, which by definition is *not* a committed seal — or a seal that reads the coherence to engineer refocusing, which is the forbidden state-dependence (C5). So **either state-independent + irreversible ⇒ monotone, CP-divisible, no revival; or revivals ⇒ no committed record or a C5 violation.**

The operational fingerprint cannot certify this program: the genuine indivisibility, if present, is structural (Tier 1) and invisible to the reduced channel. This is the program's first concrete result, and it sharpens — by computation — the Branch-A-may-be-false signal of the residue campaign.

**The Tier-1 functor — a concrete construction. [BUILD/TARGET]** The structural target needs the functor `F` mapping a sealed-record history to Barandes' one-time transition matrices, and it is *constructible* via the consistent-histories / decoherence-functional bridge. A sealed-record history is a finite poset of division events (seals) `{e_k}`, with a unitary holonomy `U_k` (the unsealed coherent evolution generated by the gravitational which-path holonomy) on each inter-seal interval and a pointer-basis commitment `{P_a}` at each seal. Define the **decoherence functional** `D(α, α′)` on coarse-grained (pointer/record) histories `α = (a_1, …, a_n)` in the standard Gell-Mann–Hartle form, `D(α,α′) = Tr[ P_{a_n}^{(n)} … P_{a_1}^{(1)} ρ P_{a′_1}^{(1)} … P_{a′_n}^{(n)} ]` with the projectors evolved by the inter-seal holonomies. Then `F(H)(t) := ` the one-time transition matrix read from the diagonal `Γ(t)_{ji} = D(j;i)` (the Barandes correspondence `Γ = |U|²` on an unsealed interval, diagonalized at each seal).

The Tier-1 biconditional is then **exactly the consistency condition**, hence a theorem in this framework rather than a slogan:

  *Chapman–Kolmogorov holds across `t′` (`Γ(t_2,t_0) = Γ(t_2,t′)Γ(t′,t_0)` for all `t_0 ≤ t′ ≤ t_2`) ⟺ the off-diagonal (interference) part of `D` vanishes at `t′` (medium decoherence) ⟺ `t′` is a seal (a refinement point of the seal order).*

Forward: a projective record commitment diagonalizes `D` at `t′`, which is precisely the statement that the probability sum rules (Chapman–Kolmogorov for the pointer histories) hold there. Reverse: if `Γ` composes across `t′` for *all* boundary conditions, the interference terms of `D` must vanish at `t′`, i.e. the record is committed (sealed). So **SHARD-unrefinable ≡ Barandes-indivisible is a theorem of consistent-histories consistency**, with the seals = the decoherence (consistency) points and the unsealed holonomy = the surviving off-diagonal interference. The functor obligation of §2.2 is thereby discharged **for a chosen projective seal-history model** — at the kinematic level only: it is *not yet* an intrinsic theorem that the SHARD *gravitational* record process supplies these very seals/projectors (that is the open gravitational content immediately below, not something this construction settles).

What remains genuinely open is the *gravitational content*, and it has a sharp form: **is gravitational record commitment sparse?** If the gravitational records decohere the which-path *continuously* (medium decoherence at all times — the continuous-sealing limit of §1), then `D` is diagonal everywhere, the seal order is fully refinable, and the process is Barandes-*divisible* (classical) — the same leak as [X]. Genuine Tier-1 indivisibility requires *intervals on which `D` is non-diagonal* (interference survives between sparse gravitational seals). The Level-3 question is therefore neither the dephasing curve (a no-go, §3) nor the existence of the functor (constructed here) but **whether the gravitational decoherence functional has non-trivial off-diagonal support between commitments** — a computation on `D`, not on `|ρ_{01}|`, and the correct target for the investigation below.

---

## 4. Ideas to build upon

**Internal (corpus).**

- **[4] Paper 4 (v6), *SHARD: Sealed Holonomy And Record Dynamics*** — supplies the *primitive object*: a sealed finite record diamond carrying an internal exchange-defect holonomy, with an indivisible whole-history record law and an intrinsic division-event commitment. This is literally the "unsealed holonomy between division events" the program needs; build the gravitational which-path on this diamond. Its conditional Born `p = 2` selection under linear holonomy composition + screen invariance is the template for C8.
- **[10] Paper 10 (v6), *The Arrow-Positivity Theorem and the Record Renormalization Group*** — `σ = 𝔼[A_D] = D(P_AB ‖ P_BA)` (T2), no-silent-arrow (T3), RP-as-theorem (T4). Use to *identify the decoherence rate with the seal rate*: the seal is entropy production, so `γ_dec = σ`. The interpolating-family result (oscillating non-RP sectors are powered by `σ > 0`) is the toy in which revivals and committed evidence trade off — the right laboratory for non-CP-divisibility.
- **[8] Paper 8 (v6), *The Tractable Frontier Campaign*** — "record-SSB is a division event sealing a branch", with the bimodal sealed collective coordinate. This is the discrete-record analogue of the which-path seal; build the gravitational seal as a record-SSB event.
- **[Va, Vb] Foundations I & II** — axiom S (silent-seam exclusion) makes unsealed which-path holonomy *not yet physics* (the formal floor for "coherent = unsealed"); sealed positivity makes the *wrong* alternative carry strictly negative weight (the mechanism by which a seal excludes the un-committed branch — a direct template for "decoherence = sealing"). Lorentzian signature from unrefinable commit order ties the seal order to time itself.
- **[X] Non-Markovian Gravitational Decoherence** — the finite-memory machinery (`χ(T)`, `τ_c`, the √e fixed point), and crucially the `T⁴`/higher-cumulant *non-Gaussian* corrections, which are exactly where genuine (revival) non-Markovianity already appears. Build the indivisible channel so that [X] is its dense-seal Gaussian shadow.
- **[1] Indivisible Causal-Set Gravity** — the division-event substrate, the covariant memory `f(s²)` of quartic-damped positive-type class, and the explicit Branch-A (derive the memory) vs Branch-B (postulate it) split, which this program inherits verbatim.
- **R5 (Banach–Lamperti `q = 2` forcing)** — the quadratic weight calculus is forced by linear, transitive (continuously reversible) screen transports; verify the seal preserves this (C8).

**External (verbatim corpus citations to reuse).**

- **[11,12] Barandes** — the divisibility / division-event definition; the `Γ = |U|²` correspondence is the formal statement of the barrier (§2.1).
- **[10ext] Carlesso, Ferialdi, Bassi, colored collapse models** — the closest existing *non-Markovian collapse* construction; the classical-noise foil to be upgraded to a holonomy-sealing channel.
- **[15,21] Breuer–Petruccione; Breuer, Laine, Piilo, Vacchini** — open-systems theory and the non-Markovianity (RHP/BLP) measures used to *certify* non-CP-divisibility / information backflow — the instrument that decides whether the barrier was crossed.
- **[22] Misra–Sudarshan** — the Zeno quadratic onset; the dense-seal limit must reproduce it.
- **Collisional / repeated-interaction models** (open-systems literature) — the canonical *Markovian-embedding* picture to consciously *avoid* (a collision per instant = continuous sealing); useful as the explicit classical shadow and as the structure whose sparsification is the program.

**Methodological.** Treat the **non-Gaussian revival sector as a Tier-2 *diagnostic*** — an observable handle on non-CP-divisibility, *not* the definition of indivisibility (which is structural/Tier-1, §2.3) and not even a reliable witness of it (revivals are neither necessary nor sufficient for Tier-1, and §3 proves a committed state-independent seal cannot revive at all) — and build toward the channel with it in view, rather than complicating the Gaussian noise; certify with an RHP/BLP measure; and keep the classical [X] channel as the provable dense-seal limit so no empirical ground is lost.

---

## 5. The constraint ledger

A genuinely indivisible gravitational channel must satisfy every entry. Ten are corpus no-gos; the last two are this program's own. **[CONSTRAINT] throughout.**

| # | Constraint | Source | Precise statement | Design rule it imposes |
|---|-----------|--------|-------------------|------------------------|
| **C1** | Bell non-evasion | v5 paper 14 (*Non-Markovianity and Bell nonlocality*) | "ISP is exactly as Bell-nonlocal as quantum mechanics, no more and no less"; forced by Tsirelson, ISP gives up **outcome independence**, keeps parameter independence, measurement independence, single outcomes; no-signalling. | The seal/holonomy memory may **not** be used to evade Bell or signal superluminally. Keep PI; the nonlocality is relocated to memory, not removed. |
| **C2** | Hegerfeldt / covariant localization | [1] §6 (Q3) | Covariant (frame-independent) localization of positive-energy states on `dp/2ω` is non-sharp — superluminal tails; Newton–Wigner is sharp but frame-dependent. | The **seal cannot be a sharp covariant point**; the division event's localization is the live Q3 obstruction. A point gravity source and a covariant seal are in tension. |
| **C3** | White-noise energy catastrophe | [2 (v6)] §1.2; [1] §4 | White (δ-correlated) collapse noise heats a quantum field at a UV-divergent rate (relativistic-CSL catastrophe). | The seal memory **must** be a smooth, Lorentz-invariant, microcausal interval correlation `f(s²)` with strong spectral falloff (e.g. quartic `ĝ(q²) = e^{−q⁴/β⁴}`, positive-type). No white sealing. |
| **C4** | Tomonaga–Schwinger integrability | [1] §1,§4 (residue R4) | The interacting reconstruction must realize a microcausal `[ℌ(x),ℌ(y)] = 0` (spacelike) evolution; constructing one is the open relativistic-collapse problem. | The interacting seal law must be TS-integrable — **Clay-hard, open**. A non-relativistic toy may sidestep this; the relativistic channel cannot. |
| **C5** | Nonlinear-collapse no-go | [1] §6 | State-dependent modifications break TS-integrability at spacelike separation; whether the `Q̂ = ½α:φ²:` coupling reintroduces effective spacelike state-dependence is itself open. | The **seal criterion must be state-independent**: the seal *rate* may depend on the geometric distinguishability `E_G` (a c-number), but the seal must not use the relative coherence/amplitude to choose outcomes. |
| **C6** | Do-delete observational no-go | [3 (v6)] §19 | Two distinct lower-level mechanisms give the same observed whole-history law but different intervention/`do-delete` semantics; the intervention structure is *not* an observational statistic. | The seal rule **cannot be derived from observed statistics alone** — either supply a Branch-A repair/uniqueness principle, or accept it as a Branch-B input (honest split inherited from [1]). |
| **C7** | magic ≠ indivisibility | [40 (v6)] | Indivisibility is necessary but **not** sufficient for nonclassicality; magic = Wigner negativity is strictly finer (tested, published). | Do **not** claim the sealed-holonomy channel is a nonclassical *resource*. The claim is dynamics / geometry / thermodynamics, not resource theory. |
| **C8** | Born composition | [4 (v6)] §8; [Va]; R5 | `q = 2` is selected only if retained holonomy amplitudes add linearly and sealed screen transports preserve total event weight under (Hadamard / unitary) screen changes. | The seal must compose linearly and be weight-preserving (screen-isometric) or the reconstructed Born rule is lost. Sealing is not allowed to be lossy on the screen. |
| **C9** | Markovization no-go | v2 paper 6 (*QFT reconstruction no-go*) | Markovized component-shadow transition data cannot reconstruct QFT; factorizing the process at events destroys the entanglement information QFT needs. | Sealing at a division event **must keep the process globally indivisible** — a seal is not a license to factorize the joint law into local sub-processes. |
| **C10** | All discreteness is ledgered | [40 (v6)] | "Every discrete act in nature is a record; the law layer is smooth. Nature makes no jumps except written ones." | The seal **must be a recorded event**, not a hidden law-layer discontinuity. The commitment is observable as a record; the smooth law layer carries no unledgered jump. |
| **C11** | Operational fingerprint (own; **now a no-go for the minimal mechanism**) | this paper §3 | Non-CP-divisibility (revivals) would make the indivisibility *observable*, but it is a separate axis from the Barandes barrier (§2.3). | **Demoted from a requirement to an optional target.** §3 proves a state-independent irreversible seal is *always* CP-divisible (no revivals), so Tier 1 cannot be certified by this fingerprint and demanding it would force reversibility (no record) or a C5 violation. Do **not** require it. |
| **C12** | Recover [X] (own; **verified**) | this paper §3 | The empirical content (quadratic onset, `E_G`-scaling) must survive. | **Met.** A state-independent ramping seal hazard `λ(t) = a t` gives `|ρ₀₁| = e^{−aT²/2}`, reproducing [X]'s Gaussian onset exactly; the indivisible channel is the sparse-seal completion of [X], and the Gaussian onset is *not* itself evidence of indivisibility. |

**Reading of the ledger.** C2 + C5 are the dangerous pair: a seal sharp and covariant enough to source point gravity (C2) without using the coherence to fire (C5) is exactly the smooth-versus-sharp tension Q3 flags as possibly *obstructed*, not merely open. C6 is why the program inherits an honest Branch-A/Branch-B fork. C11 is demoted to an optional operational target that §3 shows is *unreachable* by state-independent irreversible sealing; C12 is met by a ramping seal hazard (§3). C3/C4/C8/C9 constrain the *form* of the seal memory and composition tightly enough that the construction is far from free.

---

## 6. Decisive sub-targets (what would count as progress, success, or refutation)

- **[DONE — no-go] Minimal toy, operational axis.** The minimal state-independent irreversible-sealing toy is computed (§3): it reproduces [X]'s Gaussian onset (ramping hazard) but is monotone / CP-divisible and *cannot* produce revivals. The operational fingerprint (C11) is therefore unreachable by this mechanism — a clean no-go with no middle ground. This *confirms, by computation*, the Branch-A-may-be-false signal of the residue campaign and the do-delete no-go [3 §19]: an observable non-Markovian fingerprint here costs either the committed record (reversibility) or a C5 violation.
- **[OPEN — the real target] Tier 1: the structural functor.** What remains open is the *structural* criterion: construct the functor (sealed-record history → Barandes `Γ(t)`) and exhibit a `Γ_grav` that fails Chapman–Kolmogorov / is unrefinable while obeying the ledger. This is the genuine barrier crossing, it is invisible to the reduced channel, and it cannot be settled by a dephasing-curve calculation.
- **[TARGET — diagnostic only] Non-Gaussian fingerprint.** Distinct from a *seal* revival (ruled out above), the discrete-record (jump) statistics of [X]'s Axis 3 give a non-Gaussian `T⁴` correction even within the CP-divisible regime. It is a *weaker, diagnostic* signature of discreteness (not of barrier-crossing); quantify it for a candidate jump law and compare to the (negligible-but-structured) `T⁴` term of [X], without over-reading it as non-Markovianity.

---

## 7. What this program does not claim

It does not derive general relativity, a graviton, an area law, or the Born rule from nothing; it does not solve Tomonaga–Schwinger integrability (C4) or the Hegerfeldt obstruction (C2); it does not claim indivisibility is a nonclassical resource (C7); and it does not exhibit a channel that crosses the *structural* (Tier 1) barrier. It does not claim an observable non-Markovian fingerprint from sealing — §3 *rules that out* for the minimal mechanism. What it does establish is the target, the object, the constraint ledger, and one concrete result: state-independent irreversible sealing reproduces [X]'s Gaussian onset yet is CP-divisible, so the genuine-indivisibility question is structural and presently open. The construction inherits the causal-set paper's honest fork: **Branch B** would *postulate* a covariant seal memory `f(s²)` with free parameters and report the resulting channel; **Branch A** would *derive* the seal law and memory from the record dynamics alone — and Branch A is open, possibly obstructed.

---

## References

**Internal (corpus).**

[1] *Indivisible Causal-Set Gravity: the division-event substrate and its open covariance residues*, v6 (`relativistic-isp-v6-paper1-indivisible-causal-set-gravity.md`).
[2 (v6)] *Spatial direction and interacting integrability*, v6 (`relativistic-isp-v6-paper2-spatial-direction-and-interacting-integrability.md`) — white-noise energy catastrophe.
[3 (v6)] *Modular Record Diamonds and the Sealed-Deletion Equivalence Principle*, v6 (`relativistic-isp-v6-paper3-modular-record-diamonds.md`) — do-delete no-go (§19).
[4 (v6)] *SHARD: Sealed Holonomy And Record Dynamics*, v6 (`relativistic-isp-v6-paper4-sealed-record-events-and-born-composition.md`).
[7 (v6)] *SHARD: The Five Gates, the Dilation Theorems, Matter and Gauge Structure, Lambda, and the Kernel Frontier*, v6 (`relativistic-isp-v6-paper7.md`) — Lorentzian signature from commitment order (Gate 2a).
[8 (v6)] *SHARD: The Tractable Frontier Campaign*, v6 (`relativistic-isp-v6-paper8.md`) — record-SSB = division event sealing a branch.
[9 (v6)] *SHARD: The Fermion Route*, v6 (`relativistic-isp-v6-paper9.md`).
[10 (v6)] *SHARD: The Arrow-Positivity Theorem and the Record Renormalization Group*, v6 (`relativistic-isp-v6-paper10.md`) — `σ = 𝔼[A_D] = D(P_AB ‖ P_BA)`; no-silent-arrow; RP as theorem.
[40 (v6)] *All discreteness is ledgered* thesis paper, v6 (`relativistic-isp-v6-paper40.md`) — magic ≠ indivisibility; Markovization no-go pointer.
[Va] *Quantum theory from sealed records I: Born composition, Lorentz signature, and the arrow of time* (`v6/publishable/paper-Va-foundations-1.md`) — axioms R, S, C.
[Vb] *Quantum theory from sealed records II: fermions, statistics, and internal symmetry groups as outputs* (`v6/publishable/paper-Vb-foundations-2.md`).
[X] *Non-Markovian Gravitational Decoherence: A Gaussian-Onset Alternative to the Diósi–Penrose Exponential* (`v6/publishable/paper-X-gravitational-decoherence.md`).
[v5p14] *Non-Markovianity and Bell nonlocality*, v5 (`relativistic-isp-v5-paper14-non-markovianity-and-bell-nonlocality.md`).
[v2p6] *QFT reconstruction no-go investigation*, v2 (`relativistic-isp-v2-paper6-qft-reconstruction-no-go-investigation.md`).

**External.**

[11] J. A. Barandes, *The stochastic-quantum correspondence*, arXiv:2302.10778 (2023).
[12] J. A. Barandes, *The stochastic-quantum theorem*, arXiv:2309.03085 (2023).
[1ext] R. Penrose, *On gravity's role in quantum state reduction*, Gen. Relativ. Gravit. **28**, 581 (1996).
[2ext] L. Diósi, *Models for universal reduction of macroscopic quantum fluctuations*, Phys. Rev. A **40**, 1165 (1989).
[3ext] L. Diósi, *A universal master equation for the gravitational violation of quantum mechanics*, Phys. Lett. A **120**, 377 (1987).
[10ext] M. Carlesso, L. Ferialdi, A. Bassi, *Colored collapse models from the non-interferometric perspective*, Eur. Phys. J. D **72**, 159 (2018).
[15ext] H.-P. Breuer, F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).
[21ext] H.-P. Breuer, E.-M. Laine, J. Piilo, B. Vacchini, *Colloquium: Non-Markovian dynamics in open quantum systems*, Rev. Mod. Phys. **88**, 021002 (2016).
[22ext] B. Misra, E. C. G. Sudarshan, *The Zeno's paradox in quantum theory*, J. Math. Phys. **18**, 756 (1977).
[8ext] S. Donadi et al., *Underground test of gravity-related wave function collapse*, Nat. Phys. **17**, 74 (2021).
[25ext] M. Carlesso, S. Donadi, L. Ferialdi, M. Paternostro, H. Ulbricht, A. Bassi, *Present status and future challenges of non-interferometric tests of collapse models*, Nat. Phys. **18**, 243 (2022); arXiv:2203.04231.
[T] R. Tumulka, *A relativistic version of the GRW flash model* (2006) and its interacting extension (2020).
