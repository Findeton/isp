# Follow-up to paper 1 (unified): the ISP-derived kernel, and the radiation/viability question

Preprint, not peer reviewed, version 2026-06-04.

**Status:** working note (not a submission). Consolidates the follow-up calculations for paper 1.
Rigor tags: **[DERIVED]**, **[ARGUED]**, **[LITERATURE]**, **[OPEN]**.

**Two orthogonal questions.** Paper 1's reviewers raised two distinct issues, and they sit on
independent axes:

- **Part I — does ISP earn its place?** Paper 1 *posits* an exponential memory kernel and
  `τ_c ∼ τ_G`; critics called it "DP + colored noise wrapped in ISP." Part I *derives* both from
  Barandes' division-event structure — and turns the *discreteness* of division events into a
  positive, **non-Gaussian** coherence signature (I.3) that separates the model from generic colored
  noise, while showing the `τ_c ∼ τ_G` closure is *forced*, not dimensional (I.2′). *(Fixes the ISP
  content; does not decide viability.)*
- **Part II — is the channel viable?** The benchmark closure pins the noise power to the DP value,
  so the model could be excluded by radiation/noise bounds. Part II resolves the X-ray
  spontaneous-emission objection (favorably) and relocates the real constraint. *(Decides the fate;
  is not ISP-specific.)*

Headlines: **Part I —** Poisson division events ⟹ *exactly* paper 1's exponential kernel, with
`τ_c` = the mean division spacing, fixed self-consistently to ≈ 1.65 `τ_G`. **Part II —** the X-ray
emission concern is resolved *against* exclusion (the worrisome `S(0)` term is a known artifact;
emission `∝ S(ω)`, suppressed by `(E_G/ℏω)² ∼ 10⁻³⁶`); the binding constraint instead shifts to
**low-frequency mechanical/heating** bounds on the pinned `S(0)` — a constraint neither paper 1 nor
the external feedback identified, and the genuine open question.

---

# Part I — Making it genuinely ISP: the kernel and `τ_c` from division events

## I.0 The model — an indivisible renewal-reset process

Barandes' processes are indivisible *except* at isolated **division events**, where they momentarily
factorize. We make paper 1's picture concrete:

- between division events the which-record amplitude is held **coherently**, so the gravitational
  mismatch energy `δE(t)` keeps a fixed value;
- at a division event the record **stabilizes**: `δE` is redrawn from a distribution `p(δE)` with
  zero mean and variance `σ_E²` (a nonzero mean is the unitary phase of paper 1 §2);
- division events form a **renewal process** with waiting-time density `ψ(τ)`, mean `⟨τ⟩ = τ_c`.

So `δE(t)` is **piecewise-constant, resetting at division events**. This is *not* a Gaussian colored
noise — it has explicit microstructure, and that microstructure is the ISP content colored CSL lacks.

## I.1 (A) The memory kernel from division statistics  [DERIVED]

The autocovariance of a stationary renewal-reset process is standard: `δE(t)` and `δE(t+s)` are equal
iff no division falls in `(t,t+s)`, independent otherwise, so

```math
K(s) = \sigma_E^2\, P_{\rm same}(s),\qquad
P_{\rm same}(s) = \frac{1}{\tau_c}\int_s^\infty (\tau - s)\,\psi(\tau)\,d\tau .
```

(`P_same(0)=1`, so `K(0)=σ_E²` ✓.) The **kernel shape is fixed by the division-waiting-time law**:

- **Poisson (memoryless) divisions**, `ψ(τ)=(1/τ_c)e^(−τ/τ_c)`:
  `P_same(s)=e^(−s/τ_c)` ⟹ `K(s)=σ_E² e^(−|s|/τ_c)` — **exactly the exponential kernel paper 1
  assumed**, with `τ_c` = the mean inter-division time. Not arbitrary: it is the unique kernel of
  *memoryless* divisions.
- **Regular (deterministic) divisions**, `ψ(τ)=δ(τ−τ_c)`: `K(s)=σ_E²(1−s/τ_c)` for `s<τ_c`
  (triangular).
- **General `ψ` → general `K`.**

Feeding the exponential kernel into the second-cumulant functional reproduces paper 1's closed form
exactly,

```math
\chi(T) = \frac{1}{\hbar^2}\int_0^T (T-s) K(s)\,ds
        = \frac{\sigma_E^2\tau_c^2}{\hbar^2}\Big(\frac{T}{\tau_c}-1+e^{-T/\tau_c}\Big).
```

**Net (A): the kernel shape is derived from the division statistics, not posited.**

## I.2 (C) Fixing `τ_c` self-consistently  [DERIVED, fixed-point]

A division event **commits a record** once the channel has accumulated order-unity decoherence,
`χ(τ_c) ≈ 1`. With `σ_E ∼ E_G`,

```math
\chi(\tau_c)=\frac{\sigma_E^2\tau_c^2}{\hbar^2}e^{-1}=\Big(\frac{\tau_c}{\tau_G}\Big)^2 e^{-1}=1
\;\Longrightarrow\; \tau_c \approx 1.65\,\tau_G .
```

So `τ_c ∼ τ_G` is not merely dimensional — it is a self-consistent fixed point (the record-commitment
time equals the decoherence-stabilization time), with an O(1) coefficient (threshold-ambiguous between
≈1.2 and 1.7). **The formerly free `τ_c` is pinned to `τ_G`.**

## I.2′ Why the memory time tracks the stabilization time, not a microphysical floor  [ARGUED + DERIVED]

The fixed point above invites the objection that `τ_c ∼ τ_G` is a dimensional convenience: if the
division spacing were instead set by a microphysical clock — the light-crossing time `R/c ∼ 10⁻¹⁵ s`,
say — the channel would Markovianize, the Gaussian window would close, and the model would collapse to
white-noise DP. Two independent arguments show that corner is not generic but unphysical, and that
`τ_c ≳ τ_G` is *forced*.

**(i) Records are information-gated  [ARGUED].** A division event is the gravitational field
*committing to a which-branch record*. A record of *which* branch cannot form before the two branch
geometries are physically distinguishable by the field — and the field's accumulated distinguishing
information is exactly the decoherence already accrued, `χ(t) ≈ (t/τ_G)²`. At the light-crossing time
`χ(R/c) ∼ (R/c τ_G)² ∼ 10⁻³⁰`: the branches are utterly indistinguishable, so there is *nothing to
record* — the field cannot localize a branch about which it has acquired ≈ 0 information. The
record-commitment time is therefore bounded below by the time to reach order-unity distinguishability,
`τ_c ≳ τ_G`. This is standard decoherence physics applied to the gravitational channel: the
environment-record time equals the time for the environment-conditioned states to become orthogonal,
which *is* the decoherence time. `R/c` is a red herring — far faster than the information it would have
to encode.

**(ii) A fast clock at physical amplitude gives Zeno freezing, not DP  [DERIVED].** Even granting a
fast division clock `τ_c ∼ R/c`, at the physical fluctuation amplitude `σ_E ∼ E_G` the result is *not*
DP. The late-time (linear) slope is `σ_E²·τ_c/ℏ²`; relative to the DP slope `1/τ_G = E_G/ℏ`,

```math
\frac{\sigma_E^2\,\tau_c/\hbar^2}{E_G/\hbar}\Big|_{\sigma_E\sim E_G}
=\frac{E_G\,\tau_c}{\hbar}=\frac{\tau_c}{\tau_G}\sim10^{-15},
```

i.e. decoherence is *suppressed* by ~15 orders — the quantum-Zeno freeze of a rapidly re-drawn record,
not the DP exponential. Recovering the DP slope at `τ_c ∼ R/c` requires holding the *power*
`σ_E²·τ_c = ℏE_G` fixed, hence `σ_E = √(ℏE_G/τ_c) ≫ E_G` — an unphysically large per-division
fluctuation. The white-noise (DP) limit is the `σ_E → ∞` corner; at any finite, physical amplitude a
fast clock yields a *quadratic* (Zeno) onset, never the DP line.

**Synthesis.** The two arguments converge: requiring the decoherence to be DP-*sized* at the physical
amplitude `σ_E ∼ E_G` *forces* `τ_c ≳ τ_G`. The onset curvature `χ ≈ ½(σ_E T/ℏ)²` reaches order unity
at `T ∼ ℏ/σ_E ∼ τ_G` only if the crossover `τ_c` has not already turned the decay into its slow linear
tail — i.e. only if `τ_c ≳ τ_G`. So the Gaussian window is not assumed open; it is forced open by the
demand that the effect exist at the gravitational scale at all, and the DP-Markovian limit is reachable
only by sending the amplitude to infinity. *Caveat:* this concerns the **gravitational** channel's
intrinsic record time; faster non-gravitational decoherence (EM, gas collisions) is environmental
(paper 1 §2, effect #1), separately controlled, and does not set `τ_c`.

## I.3 (B) The ISP fingerprint: non-Gaussian coherence  [DERIVED, with [ARGUED] amplitude]

This is the signature the latest feedback asks for: one that separates the division-event model not
merely from white-noise DP (the quadratic onset of paper 1 already does that, but it is shared by *any*
finite-memory channel) but from the skeptic's natural alternative — *generic Gaussian colored noise*
(colored CSL, an Ornstein–Uhlenbeck mismatch). The discriminator is **non-Gaussianity**, and it is
intrinsic to the *discreteness* of division events.

**The principle.** Generic colored noise is Gaussian *by construction*, so its coherence is *exactly*
the second-cumulant result, `C(T) = exp[−χ(T)]` with `χ` built from the two-point function alone — a
monotone, log-convex decay. The renewal-reset process is a *jump* process (`δE` is piecewise constant,
redrawn at discrete events): it is **non-Gaussian**, so

```math
\ln C(T)=\sum_{n\ge1}\frac{i^{\,n}}{n!}\,\kappa_n(T),\qquad
\ln|C(T)|=-\chi(T)+\frac{\kappa_4(T)}{24}-\cdots ,
```

with `κ_n(T)` the cumulants of the accumulated phase `φ(T)=∫₀ᵀ δE dt/ℏ`. The Gaussian alternative has
`κ_n = 0` for all `n ≥ 3` identically. **Any non-Gaussian feature in the measured coherence — a `T⁴` correction to
the log-coherence, or outright non-monotonicity — cannot come from Gaussian colored noise; it requires
discrete record-formation events.**

**The long-memory limit is the sharpest  [DERIVED].** For `T ≪ τ_c` (memory outlasts the run, the
single-record regime) no division typically occurs, `φ = δE·T/ℏ`, and

```math
C(T)=\langle e^{i\delta E\,T/\hbar}\rangle=\Phi_{\delta E}(T/\hbar)
\quad\text{— the characteristic function of } p(\delta E).
```

The coherence decay then *images the per-division energy distribution directly*:

- Gaussian `p(δE)` ⟹ paper 1's Gaussian onset `exp[−½(σ_E T/ℏ)²]`;
- a discrete, branch-selecting `δE = ±σ_E` ⟹ `C(T) = cos(σ_E T/ℏ)` — coherence **zeros and full
  revivals**, impossible for any monotone `exp[−χ]`.

This is *not* a small effect. With `σ_E ∼ E_G` the leading non-Gaussian term at `T ∼ τ_G` is
`κ_4(δE)·(T/ℏ)⁴/24 ∼ γ₂/24`, where `γ₂ = κ_4/σ_E⁴` is the excess kurtosis of `p(δE)`: `γ₂ = −2` for
the two-point distribution — an ≈ 8% shift of the onset exponent, comparable to the few-percent
visibility resolution the onset test already demands — rising to qualitative revivals as `p` becomes
more discrete.

**Why `p(δE)` should be non-Gaussian  [ARGUED].** If a division genuinely *commits* the record to one
branch (the ISP picture of division events as effective measurements), the per-division mismatch energy
reflects a **discrete selection**, hence a bimodal/discrete `p(δE)` with `γ₂ < 0` — possibly revivals.
Only if record-formation were a sum of many independent micro-contributions would the central limit
theorem Gaussianize `p` and erase the signature. So the *discreteness of division events* — the ISP
ontology itself — is what predicts the non-Gaussian coherence; a continuum theory predicts its absence.

**Regime structure — the signature lives where the experiment is.** Non-Gaussianity is strongest at
long memory (few divisions) and is washed out by the central limit theorem as `τ_c → 0` (many divisions
per run) — exactly the white-noise/DP limit where the onset also linearizes. So the non-Gaussian
fingerprint and the quadratic onset occupy the *same* observable window `T ≲ τ_c ∼ τ_G`, and both
vanish together in the Markovian limit. Measuring the coherence across that window and testing whether
it has the pure form `exp[−χ(T)]` (monotone, no `T⁴` excess) is a clean Gaussian-vs-discrete test.

**A finer, two-point-level signature — the kernel shape.** The division-waiting-time law `ψ` also
shapes the kernel (Poisson ⟹ exponential `K`, Lorentzian `S(ω)`; regular ⟹ triangular `K`,
`sinc²`-type `S(ω)`), visible in the crossover region of `χ(T)` and in the high-frequency emission tail
(II.2). This is weaker than the non-Gaussian test — it is a two-point effect, and the candidate laws
agree to `O(T³)`, differing only near the crossover — but it is a second, independent read-out of the
division statistics.

**Discriminator hierarchy.** The tests nest, each falsifying a wider class than the last:

1. **onset shape** (quadratic vs linear) — falsifies *strict-Markovian* DP/CSL; generic to all
   finite-memory channels. *(paper 1)*
2. **non-Gaussianity** (`T⁴` kurtosis term, up to revivals) — falsifies *generic Gaussian colored
   noise*; requires discrete record events. *(this section — the division-event fingerprint)*
3. **kernel/timing shape** (exponential vs triangular) — reads out the division-waiting-time law. *(finest)*

Level 2 is the answer to the feedback: a *positive* signature of the renewal-reset structure, not
merely "non-white." **Honest caveats:** the magnitude of (2) rides on `p(δE)`'s departure from
Gaussian, which is **[OPEN]** (unpredicted from Barandes' formalism); the `T⁴` term needs higher
precision than the onset except near the revival limit; and (2) narrows the field to *discrete-record*
models — it does not single out Barandes-ISP uniquely among them.

## I.4 Honest assessment of Part I

Paper 1 had two free posits; A and C derive both from one structural assumption (Poisson division
events). That removes the "phenomenological hand-off" and is content DP-plus-colored-noise cannot
claim — genuinely ISP. And B (I.3) turns the same discreteness into a *positive* signature —
non-Gaussian coherence (a `T⁴` kurtosis term, up to revivals) that no Gaussian colored-noise model can
produce — the discriminator the "just colored noise" critique demanded; while I.2′ shows the `τ_c ∼ τ_G`
closure is forced by record information-gating and by the requirement of DP-scale decoherence at
physical amplitude, not a dimensional convenience. **Cost [ARGUED]:** the renewal-reset dynamics is itself a *model of* the
division structure, one level short of deriving it from Barandes' config-space formalism for a
gravitationally-coupled system — so the hand-off is moved deeper, not eliminated. **[OPEN]:** connect
the renewal rate to Barandes' actual transition matrices; derive `p(δE)` from first principles.

---

# Part II — Is the channel viable: the radiation/noise bounds

## II.0 The decisive question

Matching the DP late-time slope pins the noise power to the DP value,

```math
S(0) = 2\sigma_E^2\,\tau_c = 2\hbar E_G \quad\text{(same zero-frequency weight as white-noise DP).}
```

Gran Sasso [8] excludes parameter-free DP via keV emission. So the channel is excluded **if** the
emission rate is set by `S(0)`, and evades **if** it is set by `S(ω)` at the emitted (keV) frequency.

## II.1 (#1) Adiabatic / golden-rule argument  [DERIVED, leading order]

To leading order in the collapse coupling, Fermi's golden rule / linear response gives the
photon-emission rate at energy `ℏω` as `Γ_emit(ω) ∝ |matrix element|² · S(ω)` — set by the noise
power **at the emitted frequency**. Physically it is the adiabatic theorem: a noise band-limited to
`1/τ_c ≪ ω` is slow on the photon timescale and cannot deposit `ℏω ∼ keV` into a photon (energy
balance: the slow noise has no keV quanta to give). Any `S(0)` contribution must be a breakdown of
this structure.

## II.2 (#2) The suppression factor from the division-event cusp  [DERIVED] (links to Part I)

The high-frequency tail of a spectrum is fixed by the short-time non-analyticity of its correlation.
From Part I, the renewal-reset kernel has a **cusp** at the origin with slope = the division rate,

```math
K(s)\approx \sigma_E^2\big(1-|s|/\tau_c\big),\qquad K'(0^+)=-\sigma_E^2/\tau_c\ \text{(any }\psi),
```

so `S(ω) = S(0)/[1+(ωτ_c)²] → S(0)/(ωτ_c)²`. The keV-emission suppression relative to white DP is then

```math
\frac{\Gamma_{\rm emit}(\omega_{\rm keV})}{\Gamma_{\rm emit}^{\rm DP}}
= \frac{1}{1+(\omega_{\rm keV}\tau_c)^2}
\xrightarrow{\ \tau_c\sim\tau_G\ }\Big(\frac{E_G}{\hbar\omega_{\rm keV}}\Big)^2 \sim 10^{-36}.
```

**The gravitational mismatch energy is the natural emission cutoff**, and keV `≫ E_G`. Two
ISP-specific points: (i) the *discreteness* of division events makes the cusp, hence the *polynomial*
`(E_G/ℏω)²` suppression (the "worst," least-suppressed case — yet still `10⁻³⁶`); a smooth-reset model
would give exponential suppression. So the emission margin reads out the division microstructure of
Part I.

## II.3 (#4) Reconciliation with the collapse-model literature  [LITERATURE]

**(a) The `S(0)` emission term is a known artifact — emission `∝ S(ω)`.** Bassi, Donadi and Adler [9]
found the emission rate has an `S(ω)` term and an `S(0)` term; the `S(0)` term's coefficient is the
zero-frequency Fourier component, and "when the calculation is repeated with the final electron in a
wave packet and with the noise confined to a bounded region, the extra term **vanishes** … and the
Golden-Rule result is recovered." So physical emission `∝ S(ω)`, and paper 1's Hz-scale channel
**evades the Gran Sasso X-ray bound** by `∼(E_G/ℏω)² ∼ 10⁻³⁶`. *The external feedback's "excluded via
`S(0)` emission" reading is resolved against exclusion by the collapse community's own work.*

**(b) Lowering the cutoff moves the binding constraint to low-frequency mechanics.** The colored-CSL
analyses [10] and the 2022 status review [25] find a frequency cutoff does **not** free the model:
X-ray bounds are robust for *reasonable* (high) cutoffs, and as the cutoff is lowered the binding
constraint shifts to **"low-frequency purely mechanical experiments,"** which "provide the most
stable and strongest bounds." Paper 1 lives at the extreme low-cutoff end (`1/τ_c ∼` Hz), where
`S(ω) ≈ S(0)` across the mechanical band — maximally exposed to exactly these bounds. The pinned
`S(0) = 2ℏE_G` is a *low-frequency* power, probed by force-noise / heating experiments (ultracold and
levitated oscillators, bulk heating, LISA-Pathfinder-class).

## II.4 Net effect, and the calculation that now matters

- **Resolved (favorably):** the X-ray / spontaneous-emission concern — `S(0)` term is an artifact [9];
  emission `∝ S(ω)`; evades by `(E_G/ℏω)² ∼ 10⁻³⁶`. Paper 1 §8's "unresolved, no-exclusion-claim"
  framing is now *too agnostic*.
- **The new decisive question [OPEN]:** does the pinned low-frequency `S(0)=2ℏE_G` violate
  **low-frequency mechanical/heating bounds**? Well-posed and quantifiable via the colored-CSL
  machinery [10,25] mapped to the gravitational (mass-coupled) case. *This is the next calculation to
  do — and, unlike the X-ray question, it is not already resolved in the literature.*
- **The squeeze — milder than it looked (see II.5):** an *observable* onset needs `σ_E ∼ E_G` (large
  `S(0)`), and the same `S(0)` drives the low-frequency noise. The worry was that this squeezes the
  channel out; II.5 shows it does not, because the binding white-DP bound is exactly the one the
  cutoff evades.

## II.5 Advancing the open problem: a viable `R_0` window  [LITERATURE + DERIVED]

The temporal cutoff suppresses only frequency-*resolved* high-frequency probes; every `S(0)`-set
observable — decoherence, heating (momentum diffusion `D_pp = S_F(0)`), and DC/sub-Hz force noise — is
unchanged. So the cutoff helps against exactly one class of bound, and the question is whether that
class contains the *binding* one. The DP literature answers this directly: the regularization length
`R_0` is bounded **hierarchically**, and the strongest bound is the non-robust one.

- **X-ray spontaneous radiation** (Donadi et al. [8]): `R_0 ≳ 0.5 Å ≈ 5×10⁻¹¹ m` — the **strongest**
  bound, but a high-frequency (keV) probe. The bounds review explicitly notes the heating bound "has
  the merit to be more robust to possible non-Markovian generalizations of the DP model"
  (arXiv:2109.14980) — i.e. **the radiation bound is the one a colored/non-Markovian DP evades.**
- **Spontaneous heating** (a DC effect, `dE/dt = Gℏm/(4√π R_0³)`): `R_0 ≳ ~5×10⁻¹³ m` (≈ two orders
  weaker than radiation), **robust** to non-Markovian generalization (arXiv:2109.14980).
- **LISA Pathfinder / GW-detector force noise** (mHz–sub-Hz): `R_0 ≳ 4×10⁻¹⁴ m` (arXiv:1606.03637).

Paper 1's channel is exactly such a non-Markovian DP: it **evades the strong (non-robust) X-ray bound**
while the **weaker (robust) heating bound remains binding**. That opens a window

```math
5\times10^{-13}\,\text{m} \;\lesssim\; R_0 \;\lesssim\; 5\times10^{-11}\,\text{m}
\qquad (\approx 2\ \text{orders of magnitude}),
```

forbidden to white DP (by X-ray) but **open to the colored channel**. Since the DP effect grows as
`R_0` shrinks, operating at the lower (heating-limited) edge instead of the X-ray edge enhances the
decoherence by orders of magnitude — the exact factor set by the `R_0`-scaling of the chosen
experiment — plausibly turning the otherwise-unobservable DP decoherence **observable**, while heating
and DC force-noise stay within the robust bounds *by construction* (they are `S(0)`-set and the cutoff
does not touch them).

**This revises the earlier "squeeze" verdict toward viability.** The binding white-DP bound (X-ray) is
precisely the one the temporal cutoff removes; the bounds it cannot remove (heating, DC force noise)
are ~2 orders weaker, leaving real room. Caveats **[OPEN]**: (i) compute the precise `R_0`-scaling of
the observable decoherence to fix the enhancement and confirm it reaches observability at accessible
masses; (ii) the heating bound is `S(0)`-set, so its robustness should carry to paper 1's kernel, but
this should be checked explicitly; (iii) heating (DC) is never evaded and is the truly-binding robust
bound — force-noise sensors are evaded only if their measurement band lies above `1/τ_c`.

**Net:** a viable `R_0` window exists in which the channel evades the only bound that kills white DP
(X-ray) while satisfying the robust heating/mechanical bounds. *[Correction: §II.6 below carries out
the calculation and finds the "decoherence enhanced toward observability" clause **wrong** — the
observable decoherence is `R_0`-independent, so the window, though real, is observationally irrelevant.
Read §II.6 as the corrected conclusion.]*

## II.6 Doing the calculation — decoherence and emission decouple (corrects II.4–II.5)  [DERIVED]

Carried out properly, the comparison overturns the framing of II.4–II.5 (and of the external
feedback): **decoherence and the X-ray/heating emission are set by different length scales and
decouple**, so there is no `S(0)`-pinning between them and no squeeze.

Decompose the DP mismatch energy of a rigid body displaced by `d` into nucleon pairs (smeared
nucleons `ρ = Σ_i g(r−r_i)` of width `R_0`):

```math
E_G = \frac{G}{2}\sum_{i,j}\big[\,2W(a_{ij}) - W(a_{ij}-d) - W(a_{ij}+d)\,\big],\qquad a_{ij}=r_i-r_j,
```

with `W(a)` the gravitational energy of two smeared nucleons a distance `a` apart. Two pieces:

- **Diagonal (`i=j`, per-nucleon):** `≈ N·Gm²/R_0` for `d ≫ R_0` — the per-nucleon self-energy,
  **`R_0`-dependent**; this is what drives heating (`∝1/R_0³`) and X-ray emission.
- **Off-diagonal (`i≠j`, structural):** `≈ (6/5)GM²/R` for `d ≳ R` — set by the **object size `R`,
  not `R_0`** (every nucleon separation exceeds `R_0` throughout the window, so `W≈Gm²/a`, unsmeared).

For any nanoscale object the structural term dominates overwhelmingly. A 100-nm silica sphere
(`M ≈ 8.4×10⁻¹⁸ kg`, `N ≈ 5×10⁹`): structural `E_G ≈ 5.6×10⁻³⁸ J` versus per-nucleon `≈ 1.9×10⁻⁴² J`
at `R_0=5×10⁻¹³ m` — ratio `≈ 3×10⁴` (and `≈3×10⁶` at `R_0=0.5 Å`). **So `E_G` is structural and
`R_0`-independent**, while the per-nucleon heating is a separate, `R_0`-set quantity (`~10⁻⁴¹` W per
nucleon at `R_0=0.5 Å`). The decoherence magnitude/observability is then paper 1 §6's — `R_0`-independent
— and its only honest novelty is the onset *shape*.

Consequences — correcting II.4–II.5 and the feedback:
- **No pinning, no squeeze.** Matching the collective, structural decoherence does *not* fix the
  per-nucleon, `R_0`-set emission. The feedback's "pinned `S(0)` ⟹ emission inherited," and my II.4–II.5
  reasoning built on it, conflated the two. Physically: a neutral object's collective (centre-of-mass)
  jiggle does not radiate — only the per-nucleon charge jiggle does, and that is set by `R_0`.
- **The II.5 "enhancement" is void.** Since the observable decoherence is `R_0`-independent, smaller
  `R_0` does not enhance it; the `R_0` window is real but observationally irrelevant (it concerns the
  model's regularization, not the measured signal).
- **No viability crisis to rescue.** White DP at `R_0 ≳ 0.5 Å` already satisfies the per-nucleon
  emission/heating bounds *and* predicts the (R_0-independent) decoherence; the colored cutoff merely
  relaxes the regularization bound to `R_0 ≳ 5×10⁻¹³ m`, with no observable consequence.

**Net (corrected):** the radiation/heating worry dissolves — not via a window, but because decoherence
(`∝GM²/R`, collective, `R_0`-independent) and emission (`∝1/R_0³`, per-nucleon) were never coupled.
Paper 1 predicts the standard DP decoherence magnitude with a modified onset *shape*; the model's
consistency with bulk-matter bounds is the ordinary DP requirement on `R_0`, independent of the
interferometric prediction. This **supersedes** the `S(0)`-pinning / low-frequency-squeeze framing of
II.4, II.5, and the III.2 merge text — the most favorable *and* most correct resolution. It also
sharpens the honest verdict on the whole paper: the only thing the channel adds to standard DP is the
onset *shape* (Part I makes that shape genuinely ISP); it neither rescues nor threatens viability,
because the testable decoherence is plain DP and the bulk-matter bounds touch only `R_0`.

---

# Part III — Ready-to-merge text for paper 1 (NOT yet applied)

If/when Part II is folded in, the following replace the corresponding passages. Kept here so the
manuscript stays unchanged until you decide; render-clean, paper-1 voice; the LaTeX mirrors verbatim.

## III.1 Abstract — replacement for the radiation sentence
> We give threshold masses and separations for levitated-nanosphere, matter-wave, and
> mechanical-cat-state platforms, set out differential strategies (notably a density lever and
> common-mode subtraction) to separate the gravitational onset from environmental backgrounds, and
> confront the radiation bounds: the channel **evades** the X-ray spontaneous-emission limit —
> emission follows the noise at the photon frequency, suppressed by `(E_G/ℏω)²` — so its viability
> instead hinges on **low-frequency mechanical/heating** bounds on the DP-pinned noise power, which
> we identify as the decisive test.

## III.2 §8 — full replacement ("Spontaneous radiation and low-frequency bounds")
> The parameter-free DP model is experimentally excluded. Donadi et al. [8] searched underground at
> Gran Sasso for the spontaneous electromagnetic radiation that collapse-driven charge diffusion would
> produce, found no excess, and tightened the bound on the effective nuclear mass-density size by about
> three orders of magnitude; current bounds on the wider collapse-model family are reviewed in [25].
>
> The benchmark closure pins the noise power to the DP value, `S(0) = 2σ_E²·τ_c = 2ℏE_G`, so whether
> the channel inherits DP's excluded X-ray emission turns on whether the rate is set by `S(0)` or by
> `S(ω)` at the emitted (keV) frequency. This is settled in the collapse-model literature: the rate
> has both terms, and Bassi, Donadi and Adler [9] showed the `S(0)` term is an artifact of
> non-normalizable intermediate states that vanishes for normalizable wave packets, leaving the
> Golden-Rule result `∝ S(ω)`. For the finite-memory kernel, whose short-time cusp gives a Lorentzian
> tail `S(ω) = S(0)/[1+(ω·τ_c)²]`, the keV suppression relative to white-noise DP is
> `(ω_keV·τ_c)⁻² → (E_G/ℏω_keV)² ∼ 10⁻³⁶` for `τ_c ∼ τ_G`. The gravitational mismatch energy is the
> natural emission cutoff, and since keV `≫ E_G` the channel **evades the Gran Sasso X-ray bound** by
> a wide margin.
>
> Evading the X-ray bound by pushing the noise to low frequency does not make the channel safe. The
> pinned `S(0)` is a *low-frequency* power, and the colored-collapse analyses [10,25] find that as the
> cutoff is lowered the binding constraint shifts to **low-frequency mechanical and heating
> experiments** (force noise on ultracold and levitated oscillators, bulk heating), which give the
> strongest, most stable bounds. The present channel sits at the extreme low-cutoff end (`1/τ_c ∼`
> Hz), where `S(ω) ≈ S(0)` across the mechanical band, so it is maximally exposed to exactly these
> bounds. The decisive viability test is therefore whether the pinned `S(0)` violates the
> low-frequency mechanical/heating limits — a quantitative comparison made well-posed by the
> colored-CSL machinery of [10,25] mapped to the gravitational (mass-coupled) case. We do not carry it
> out here; it is the open question on which the channel's existence turns.
>
> A built-in tension sharpens this: an *observable* onset at the `τ_G` scale requires `σ_E ∼ E_G`,
> hence a large `S(0)`, and the same `S(0)` drives the low-frequency noise these experiments bound.
> Whether a viable window survives is a numerical question. Two claims separate cleanly: the
> onset-shape test of Section 5 decides whether the DP exponential is a Markovian idealization — the
> robust content of this paper, independent of the above — while the low-frequency mechanical bound
> decides whether this *specific* gravitational channel exists.

## III.3 Knock-on edits (merge only together with III.1–III.2)
- §1 "two claims of very different security": "survives the spontaneous-radiation bound" →
  "survives the low-frequency mechanical/heating bound."
- §9 limitations: the radiation bullet should name the low-frequency mechanical constraint as binding
  (not X-ray).
- Conclusion: "does its (DP-pinned) low-frequency noise drive spontaneous emission … high-frequency
  spectrum" → "X-ray emission is suppressed by `(E_G/ℏω)²` and evaded; whether the channel exists
  turns on low-frequency mechanical/heating bounds on the same DP-pinned noise power."
- (Optionally add a "microscopic model" subsection in §4 from Part I: Poisson divisions ⟹ exponential
  kernel, `τ_c` = mean division spacing, fixed by `χ(τ_c)∼1` to ≈ 1.65 `τ_G` — directly answers the
  "phenomenological hand-off" critique.)

---

# Overall honest status

- **Part I** makes the ISP framing earn its place: the kernel and `τ_c` are derived from division-event
  statistics, answering the central "DP-in-disguise" critique — at the cost of one explicit
  (renewal-reset) modeling assumption that is itself short of Barandes' full formalism. The discreteness
  of division events further predicts a **non-Gaussian** coherence signature (I.3: a `T⁴` kurtosis term,
  up to revivals) that separates the model from generic *Gaussian* colored noise — the positive
  discriminator the "just colored noise" critique asked for; and the `τ_c ∼ τ_G` closure is shown
  *forced*, not dimensional, by record information-gating and by the requirement of DP-scale decoherence
  at physical amplitude (I.2′ — the DP-Markovian limit is the unphysical `σ_E → ∞` corner).
- **Part II** dissolves the headline viability worry, but on doing the calculation (II.6) the reason is
  cleaner than II.4–II.5 supposed: **decoherence (collective, `∝GM²/R`, `R_0`-independent) and the
  X-ray/heating emission (per-nucleon, `∝1/R_0³`) are set by different scales and decouple.** There is
  no `S(0)`-pinning and no squeeze. Paper 1 predicts the standard (`R_0`-independent, frontier-observable)
  DP decoherence with a modified onset *shape*; the emission/heating bounds touch only the model's
  regularization `R_0` (white DP fine at `R_0 ≳ 0.5 Å`; the colored cutoff relaxes this to
  `≳ 5×10⁻¹³ m`, observationally moot). The `S(0)`-pinning framing of II.4, the II.5 "window enhancement,"
  and the external feedback all rested on conflating collective and per-nucleon noise.
- So the honest scope sharpens: the *only* thing the channel adds to standard DP is the onset shape
  (Part I makes that shape genuinely ISP); it neither rescues nor threatens viability. The one genuine
  remaining physics step is **Part I** — deriving the renewal-reset division dynamics from Barandes'
  config-space formalism (Part II's viability question is, on this analysis, no longer open).

*References as in paper 1: [8] Donadi et al., Nat. Phys. 17, 74 (2021); [9] Adler–Bassi–Donadi /
Bassi–Donadi, J. Phys. A 46, 245304 (2013) and Phys. Lett. A (arXiv:1307.1021, 1011.3941); [10]
Carlesso–Ferialdi–Bassi, EPJD 72, 159 (2018) / arXiv:1805.10100; [25] Carlesso et al., Nat. Phys. 18,
243 (2022) / arXiv:2203.04231; [11,12] Barandes, arXiv:2302.10778, 2309.03085. DP `R_0`-bound
hierarchy (II.5): spontaneous-heating bounds revisited, arXiv:2109.14980; LISA Pathfinder constraint
on collapse models, arXiv:1606.03637. Methods: stationary renewal-process autocovariance;
second-cumulant decoherence functional; Fermi golden rule / Larmor radiation theory; DP momentum
diffusion `D_pp=S_F(0)`.*
