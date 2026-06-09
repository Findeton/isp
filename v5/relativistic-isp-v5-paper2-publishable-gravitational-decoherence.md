# Non-Markovian Gravitational Decoherence from Indivisible Stochastic Processes: A Gaussian-Onset Alternative to Diósi–Penrose and a Fit-Free Interferometric Test

**Felix Robles Elvira**

*Manuscript — foundations of quantum mechanics / gravitational decoherence.*

---

## Abstract

Gravitationally induced decoherence, in the Diósi–Penrose (DP) form, predicts that a
spatial superposition of a massive body loses coherence at a rate set by the
gravitational self-energy `E_G` of the mass-density difference between the branches,
with characteristic time `τ_G = ℏ/E_G`. The DP law is exponential in time, a form that
follows from an implicit Markov (memoryless, divisible) assumption about the underlying
stochastic dynamics. We examine gravitational decoherence within the framework of
*indivisible stochastic processes* (ISP) of Barandes, whose defining feature is the
failure of the divisibility (Chapman–Kolmogorov) property. We show that this single
structural feature generically replaces the DP exponential with a **non-exponential
coherence decay whose short-time behaviour is Gaussian**, `C(T) = C(0)·exp[−½(T/τ_G)²]`,
at the *same* energy scale `E_G`, crossing over to an exponential tail beyond a
record-memory time `τ_c`. The Markovian DP law is recovered as the `τ_c → 0` limit. The
distinction is experimentally sharp and requires no fitted constant: the *onset shape* of
the residual gravitational log-coherence is linear in `T` for Markovian collapse (finite
initial slope) and quadratic (zero initial slope, a Zeno-like plateau) for the indivisible
case. We give threshold masses and separations for levitated-nanosphere, matter-wave, and
mechanical-cat-state platforms, analyse what fixes `τ_c`, and address the spontaneous-radiation
bound that already excludes the parameter-free DP model. We are explicit about scope: the
quadratic onset is the generic signature of non-Markovian decoherence and is shared with
other coloured-noise collapse models, so the test falsifies *strict* Markovian
DP/CSL and confirms a non-Markovian fundamental channel consistent with ISP, but does not
by itself single out ISP.

---

## 1. Introduction

The persistence of quantum coherence for increasingly massive systems is one of the
sharpest open questions at the quantum–classical and quantum–gravity interfaces.
Objective-collapse models posit a fundamental, observer-independent mechanism that
suppresses macroscopic superpositions [4–7]. Among them, the proposals of Diósi [2,3]
and Penrose [1] tie this suppression specifically to gravity: a superposition of two
distinct mass distributions is a superposition of two distinct spacetime geometries, and
the gravitational self-energy of their difference sets a decoherence time
`τ_G = ℏ/E_G`. This "Diósi–Penrose" (DP) decoherence is now an active experimental
target, both directly through matter-wave and optomechanical interferometry [16,19,23]
and indirectly through spontaneous-radiation searches [8,9], the latter having already
excluded the simplest, parameter-free DP model [8].

The DP coherence law is exponential, `C(T) = C(0)·exp(−T/τ_G)`. This functional form is
not an independent prediction of gravity; it is a consequence of treating the underlying
collapse noise as *white* (delta-correlated in time), equivalently of assuming the
reduced dynamics forms a Markovian semigroup. Real physical noise is never white [10],
and the open-systems literature shows that non-Markovian (coloured) environments
generically produce non-exponential coherence decay, with a universal quadratic
(Zeno-like) onset at short times [15,21,22].

In this paper we ask what gravitational decoherence looks like when the underlying
dynamics is taken to be *indivisible* in the sense of Barandes' stochastic-quantum
correspondence [11,12]. An indivisible stochastic process is one whose transition law
does **not** factorize through intermediate times,

$$
\Gamma(t_2,t_0) \neq \Gamma(t_2,t_1)\,\Gamma(t_1,t_0),
$$

i.e. it violates exactly the divisibility property that underlies the Markovian
semigroup. Our central result is that this single feature replaces the DP exponential
with a non-exponential law whose short-time form is Gaussian, at the same energy scale,
and that the difference is experimentally accessible through a fit-free onset-shape
measurement. We recover DP as the Markovian limit, identify the new time scale `τ_c`
that controls the crossover, and confront the existing spontaneous-radiation bound.

Our claims are deliberately bounded. The mechanism is a *reconstruction* of gravitational
decoherence within a particular stochastic ontology; the new, falsifiable content is the
non-exponential onset, not the energy scale (which is DP's). The quadratic onset is the
generic signature of non-Markovianity and is not unique to ISP. We make these limitations
explicit in Section 9.

## 2. Indivisible stochastic dynamics and the record-stabilization hypothesis

Barandes' stochastic-quantum correspondence [11,12] establishes that a broad class of
quantum systems can be represented as stochastic processes over a configuration space
in which the configuration is a definite quantity ("beable") at all times, with the
unitary, Hilbert-space description emerging as an exact reformulation. The processes that
correspond to generic quantum evolution are *indivisible*: their transition matrices do
not satisfy the Chapman–Kolmogorov composition law except at isolated *division events*,
times at which the process momentarily factorizes and behaves Markovianly. Division
events are the natural locus of effective measurement and record formation.

We adopt the following hypothesis, consistent with this picture and with the
gravitational-decoherence proposals [1–3,20]: when two coherent branches carry distinct
effective mass-density records, the gravitational distinguishability of the corresponding
geometries acts as a channel that *stabilizes* the branches into distinct records. The
stabilization is not a primitive collapse postulate; it is the statement that the
gravitational mismatch supplies a positive, accumulating "cost" that suppresses the
survival of the unstabilized (coherent) alternative. We make this quantitative in the
next two sections and emphasise where the indivisible structure changes the result.

We distinguish three physically separate effects, only the third of which is the subject
of this paper:

1. **Environmental decoherence** — ordinary scattering, gas collisions, thermal emission;
   reducible in principle by better isolation [14,16].
2. **Unitary gravitational phase** — gravity shifts the relative phase of the branches
   without destroying coherence.
3. **Gravitational record stabilization** — the geometric mismatch itself acts as a
   branch-stabilizing (decohering) channel. This is the putative new physics.

## 3. Gravitational mismatch energy and the Markovian (Diósi–Penrose) limit

Let the two branches carry mass densities `ρ_r(x)` and `ρ_{r'}(x)`, with difference
`δρ(x) = ρ_r(x) − ρ_{r'}(x)`. Following Diósi and Penrose [1–3], the gravitational
mismatch energy is the Newtonian self-energy of the difference,

$$
E_G = \frac{G}{2}\int d^3x\,d^3y\;\frac{\delta\rho(x)\,\delta\rho(y)}{|x-y|}.
$$

`E_G` is non-negative once a finite object size is retained; the point-mass limit is not
admissible because it diverges, exactly the regularization issue that the experimental
bounds constrain [8]. Define the dimensionless gravitational action accumulated over a
hold time `T`,

$$
a(T) = \frac{E_G\,T}{\hbar}, \qquad \tau_G = \frac{\hbar}{E_G}.
$$

The standard DP result is the exponential coherence law

$$
C(T) = C(0)\,\exp(-T/\tau_G).
$$

It is instructive to see precisely which assumption produces the exponential. Write the
survival factor `S(E_G,T) = |C(T)|/|C(0)|`. If one assumes (i) time multiplicativity
`S(E_G, T+U) = S(E_G,T)\,S(E_G,U)`, (ii) additivity of independent cost channels
`S(E_1+E_2, T) = S(E_1,T)\,S(E_2,T)`, and (iii) dependence only on the dimensionless
action `a`, then the Cauchy functional equation forces

$$
S = \exp(-\kappa\,a) = \exp(-\kappa\,E_G T/\hbar),
$$

with the coefficient `κ` fixed by normalization. Assumption (i) is the semigroup
(Chapman–Kolmogorov) property: it states that processing over the whole interval
factorizes into independent processing over its parts. **This is the divisibility /
Markov assumption.** The DP exponential is therefore the Markovian special case of a more
general survival functional. We now drop assumption (i), as the indivisible structure
requires.

## 4. Indivisible dynamics and non-exponential decoherence

### 4.1 The general survival functional

For a process that is not divisible, the survival factor is not multiplicative in time
and need not be exponential. The model-independent object is the decoherence functional
[15,21]

$$
\ln\frac{|C(T)|}{|C(0)|} = -\,\Gamma(T), \qquad
\Gamma(T) = \frac{1}{2\hbar^2}\int_0^T\!\!\int_0^T K(t_1 - t_2)\,dt_1\,dt_2,
$$

where `K(s) = \mathrm{Cov}[\delta E(t),\delta E(t+s)]` is the autocorrelation of the
gravitational record-mismatch energy, with fluctuation amplitude `σ_E` and correlation
(record-memory) time `τ_c`. Two limits bracket the behaviour.

**Markovian limit** (`τ_c → 0`, `K ∝ δ`): the double integral is linear in `T`,
`Γ(T) ∝ T`, recovering the DP exponential and identifying `1/τ_G = E_G/ℏ`.

**Maximally indivisible limit** (`τ_c → ∞`, no internal decorrelation — the natural
meaning of a single indivisible transition over the hold): `K ≈ σ_E^2` is constant, so

$$
\Gamma(T) = \tfrac{1}{2}\Big(\frac{\sigma_E T}{\hbar}\Big)^2,
$$

a quadratic exponent and hence a Gaussian coherence decay.

### 4.2 The central result

Taking the natural reading in which the relative which-record amplitude is held
coherently across a single indivisible transition, so that `σ_E` is of order `E_G`, the
shape is fixed and the scale is the *same* `τ_G` as DP:

$$
\boxed{\,C(T) = C(0)\,\exp\!\Big[-\tfrac{1}{2}\,(T/\tau_G)^2\Big], \qquad \tau_G = \hbar/E_G.\,}
$$

For a generic finite `τ_c`, with an exponential memory kernel
`K(s) = σ_E^2\,e^{-|s|/τ_c}` one obtains the closed form

$$
\Gamma(T) = \frac{\sigma_E^2\,\tau_c^2}{\hbar^2}\Big(\frac{T}{\tau_c} - 1 + e^{-T/\tau_c}\Big),
$$

which is Gaussian for `T ≪ τ_c` and crosses over to a linear (exponential) tail for
`T ≫ τ_c`. The DP exponential is the `τ_c → 0` edge; the pure Gaussian is the
`τ_c → ∞` edge. This is the quantitative content of indivisibility for gravitational
decoherence: same energy scale, non-exponential shape, with a single new time scale
`τ_c` controlling the crossover.

The short-time quadratic onset is not an artefact of the exponential kernel; it is the
universal consequence of a finite-correlation-time (smooth) noise, identical in origin to
the quantum-Zeno short-time behaviour of any open system [22], and is required by the
analyticity of `Γ(T)` together with `Γ'(0)=0` whenever the noise has no white (delta)
component.

## 5. A fit-free interferometric discriminator

The practical signature is the *shape* of the decay near `T = 0`, which carries no fitted
constant. Prepare a spatial superposition with fixed gravitational mismatch `E_G` and a
fixed environmental budget `Γ_env`, and measure the interferometric visibility `V(T)`.
Define the residual gravitational log-coherence by subtracting the separately measured
environmental contribution (e.g. by repeating at `E_G → 0`, i.e. negligible separation),

$$
L(T) = \ln\frac{V(T)}{V_{\mathrm{env}}(T)}.
$$

The three hypotheses give qualitatively distinct onsets:

$$
L(T) =
\begin{cases}
0, & \text{ordinary quantum mechanics (no fundamental channel),}\\[2pt]
-\,T/\tau_G, & \text{Markovian DP/CSL: finite initial slope (straight line),}\\[2pt]
-\,\tfrac{1}{2}(T/\tau_G)^2, & \text{indivisible ISP: zero initial slope (parabola tangent to the axis).}
\end{cases}
$$

The discriminator is therefore

$$
\boxed{\;\text{straight line through the origin} \Rightarrow \text{Markovian DP/CSL};\qquad
\text{parabola tangent at the origin} \Rightarrow \text{indivisible ISP}.\;}
$$

Because the *shape* (linear vs quadratic onset) is independent of the overall
coefficient, the test does not require knowing `τ_G` in advance, nor the absolute
collapse strength — only the ability to vary `E_G` while holding the environment fixed,
and to resolve the curvature of `L(T)` at small `T`.

**A second axis: distinguishing ISP from the whole collapse-model family.** The onset shape
separates ISP from any *Markovian* collapse model, but several related theories must be told
apart at once, and they are distinguished by *two* axes — the onset shape and the *scaling of
the rate*. (Both axes are plain, non-relativistic ISP: indivisibility supplies the onset, and the
Newtonian self-energy `E_G` supplies the scaling — the relativistic extension adds nothing here.)
ISP occupies a cell that no other named theory does:

| Theory | Fundamental decay? | Onset shape | Rate scaling |
|---|---|---|---|
| Unitary QM / QFT | no | — (only `Γ_env`) | — |
| Schrödinger–Newton (mean-field) [24] | no — a phase/frequency *shift* | — | gravitational, but a shift, not decay |
| CSL / GRW (Markovian, non-gravitational) [4,5] | yes | exponential | own parameters (`λ, r_C`), *not* `E_G` |
| Diósi–Penrose (Markovian, gravitational) [1,2] | yes | exponential | gravitational `E_G` |
| **ISP (this work)** | **yes** | **Gaussian (non-Markovian)** | **gravitational `E_G`** |

A *two-axis* measurement settles it. **Axis 1 (onset shape)**, above, separates ISP from the
Markovian models (exponential vs Gaussian). **Axis 2 (rate scaling):** vary the mass `M`,
separation `d`, and geometry, and test whether the rate tracks the gravitational self-energy
`E_G` (the Diósi–Penrose form, `∝ G`) or the CSL parameters (`λ, r_C`, with a fixed
`~10^{-7}`-m length scale and a different geometry dependence); the Schrödinger–Newton
alternative appears instead as a deterministic frequency *shift* with no decay, already bounded
by optomechanics [24]. A result in the **(Gaussian onset) × (gravitational `E_G`-scaling)** cell
points at ISP and simultaneously excludes Markovian DP (exponential), CSL/GRW (wrong
scaling), Schrödinger–Newton (shift, not decay), and unitary QM (no decay).

**Honest limits of the two-axis test.** (i) The one construction sharing the ISP cell would be a
*non-Markovian gravitational* collapse — but that is ISP's own content under another name, not a
distinct theory; a *colored* (non-Markovian) CSL [10] can mimic the Gaussian onset but not the
gravitational `E_G`-scaling, so the second axis separates it. (ii) Axis 2 is a *campaign*: the
`E_G`-scaling must be mapped across a range of `M, d`, geometry, not read from one curve. (iii)
The test presupposes the fundamental channel exists at all — if nature is exactly unitary, every
row collapses to "no decay" and ISP is empirically QM. (iv) The regime is at the frontier of
mesoscopic-superposition sensitivity, not yet in hand. Within these limits the two-axis test
upgrades the discriminator from "ISP vs. standard quantum mechanics" to "ISP vs. the entire
collapse/decoherence family."

## 6. Numerical thresholds and experimental platforms

We quote thresholds for a rigid homogeneous sphere of mass `M`, radius `R`, density
`ρ`, coherently separated by `d`. For `d ≪ R` the mismatch energy is harmonic,

$$
E_G \simeq \tfrac{1}{2} M \omega_G^2 d^2, \qquad \omega_G^2 = \frac{4\pi G \rho}{3},
$$

while for object-scale separations it saturates at the self-energy scale

$$
E_G^{\mathrm{sat}} \simeq \frac{6}{5}\frac{G M^2}{R}.
$$

Using `ρ = 2000\ \mathrm{kg\,m^{-3}}`, the saturated threshold mass that decoheres in
time `T` (i.e. `τ_G = T`) is

$$
M_{\mathrm{thr}}^{\mathrm{sat}}(T) =
\left[\frac{\hbar}{\tfrac{6}{5} G\,(4\pi\rho/3)^{1/3}\,T}\right]^{3/5}.
$$

Representative values (saturated regime, `d ≳ R`):

| `T` | `M_thr` (kg) | `M_thr` (amu) | `R_thr` |
|---|---|---|---|
| 1 μs | `3.1×10⁻¹²` | `1.9×10¹⁵` | 7.2 μm |
| 1 ms | `4.9×10⁻¹⁴` | `2.9×10¹³` | 1.8 μm |
| 1 s | `7.7×10⁻¹⁶` | `4.6×10¹¹` | 452 nm |
| 100 s | `4.9×10⁻¹⁷` | `2.9×10¹⁰` | 180 nm |
| 1 h | `5.7×10⁻¹⁸` | `3.4×10⁹` | 88 nm |

These mass and separation windows coincide with the targets of current and proposed
mesoscopic-superposition experiments [16,17,19,23]. Three platform classes are natural
hosts for the onset-shape test:

- **Levitated nanosphere interferometry.** Neutral dielectric nanospheres in ultra-high
  vacuum, prepared in spatial superposition and recombined [16].
- **Mesoscopic matter-wave interferometry.** Large-molecule and cluster interferometers,
  where macroscopicity has been advanced systematically [16,23].
- **Mechanical cat states / optomechanics.** Superpositions of a massive mechanical
  element [19], including the gravity-mediated-entanglement geometries [17,18] in which
  `E_G` can be tuned by separation.

In every case the experimental strategy for the discriminator is identical: hold the
object, temperature, vacuum, and pulse sequence fixed, vary `E_G` (e.g. through the
separation `d`), and examine whether the gravitational contribution to `\ln V` enters
linearly or quadratically in the hold time.

## 7. The record-memory time

The new scale `τ_c` is the autocorrelation time of the gravitational mismatch — in the
ISP language, the mean spacing between division events of the gravitational record
channel. A self-consistency argument fixes its order: in the present setting the division
event *is* the record stabilization, and the stabilization time is `τ_G`, so the memory
time and the stabilization time coincide,

$$
\tau_c \sim \tau_G = \hbar/E_G.
$$

This identification is dimensional rather than unique. The candidate scales and their
consequences are:

| candidate `τ_c` | origin | consequence |
|---|---|---|
| `ℏ/E_G = τ_G` | channel-intrinsic (division = stabilization) | Gaussian onset observable near `T ∼ τ_G` |
| `(3/4πGρ)^{1/2} = 1/ω_G` | gravitational dynamical time (density only) | `∼10³ s` for rock: also observable |
| `R/c` | light-crossing (microphysical floor) | `∼10⁻¹⁵ s`: Markovian, recovers DP |

The honest verdict is that indivisibility *forces* the decay to be non-exponential but
pins `τ_c` only up to which physical scale governs the channel. The channel-intrinsic and
gravitational-dynamical choices both place the crossover within the observable window
(`τ_c` of order seconds to hours for the masses in Section 6), so the Gaussian onset is
accessible; only a fast microphysical floor would Markovianize the channel back to the DP
exponential.

## 8. Spontaneous radiation and existing bounds

The parameter-free DP model is experimentally excluded. Donadi et al. [8] searched
underground at the Gran Sasso laboratory for the spontaneous electromagnetic radiation
that collapse-driven charge diffusion would produce, found no excess, and tightened the
bound on the effective nuclear mass-density size by about three orders of magnitude,
ruling out the simplest DP model.

A non-Markovian gravitational channel is naturally *quasi-static*: with `τ_c` of order
seconds the spectral weight of the noise sits at `1/τ_c ∼ 1\ \mathrm{Hz}`, while the
spontaneous-radiation searches probe X-ray frequencies `ω ∼ 10^{19}\ \mathrm{s^{-1}}`. On
energy-conservation grounds a direct-current-like noise carries no quanta capable of
producing a keV photon, so one expects the radiation to be strongly suppressed.

We caution, however, that whether coloured (non-Markovian) collapse noise evades the
spontaneous-radiation bound is an **open and contested question**, and we do not claim a
clean evasion. Adler, Bassi and Donadi [9] find that the emission rate in collapse models
is controlled by the *zero-frequency* component of the noise spectrum rather than by its
value at the emitted-photon frequency, so that a high-frequency cutoff does not obviously
reduce it; this is countered by calculations using normalizable final states and
spatially bounded noise, in which the extra emission term vanishes [9,10]. The
ISP-Gaussian channel inherits exactly this unresolved issue, in common with other
coloured-noise collapse models [10]. The defensible statement is therefore that the
indivisible version is *plausibly* not excluded by [8] because its noise is quasi-static,
but that settling this requires resolving the same zero-frequency-versus-emitted-frequency
question that is open for coloured CSL.

Two consequences follow. First, the interferometric onset-shape test of Section 5, not
the radiation channel, is the decisive measurement, because radiation neither cleanly
excludes nor confirms the indivisible version. Second, the non-observation of collapse
radiation mildly favours the large-`τ_c` (quasi-static, Gaussian) branch over the
already-excluded Markovian edge — the two analyses point in the same direction.

## 9. Discussion: scope and limitations

We state the boundaries of the result plainly.

- **The energy scale is DP's, not new.** The contribution is the non-exponential *shape*
  and its falsifiable onset, not the magnitude `τ_G = ℏ/E_G`, which is taken over from
  [1–3].
- **The coefficient inherits DP's ansatz dependence.** Whether the Gaussian time equals
  `ℏ/E_G` exactly depends on the fluctuation amplitude `σ_E`; only the quadratic *shape*
  is assumption-light.
- **The quadratic onset is generic to non-Markovianity.** It is shared by coloured-noise
  CSL and by non-Markovian environmental decoherence [10,21,22]. Observing it would
  falsify *strict* Markovian DP/CSL and confirm a non-Markovian fundamental channel
  consistent with ISP, but would not by itself single out ISP among non-Markovian models.
- **`τ_c` is a genuinely new parameter** fixed here only dimensionally (Section 7).
- **Environmental non-Markovianity must be controlled.** Because a non-Markovian
  *environment* can also produce a quadratic onset, the test requires that the residual
  after environmental subtraction be attributable to the gravitational channel — most
  cleanly demonstrated by its scaling with `E_G` at fixed environment.

Within these bounds, the result is a concrete, falsifiable, and motivated alternative to
the Markovian DP law, derived from a specific and independently-motivated stochastic
ontology [11,12], and testable with the same platforms already pursuing DP [16,17,19,23].

## 10. Conclusion

Treating gravitational decoherence as a process in an indivisible (non-Markovian)
stochastic dynamics replaces the Diósi–Penrose exponential with a non-exponential,
Gaussian-onset coherence decay at the same gravitational energy scale, with the Markovian
DP law recovered in the zero-memory limit. The distinction is experimentally sharp and
free of fitted constants: a linear onset of the residual gravitational log-coherence
signals Markovian collapse, a quadratic onset signals the indivisible channel. The new
time scale `τ_c` controlling the crossover is fixed dimensionally to the order of `τ_G`,
placing the effect within reach of mesoscopic-superposition experiments. The
spontaneous-radiation bound that excludes parameter-free DP is plausibly evaded by the
quasi-static non-Markovian noise, though this rests on an unresolved question common to
coloured-noise collapse models. The onset-shape measurement is the decisive test, and it
is accessible now.

---

## References

[1] R. Penrose, *On gravity's role in quantum state reduction*, Gen. Relativ. Gravit. **28**, 581 (1996).

[2] L. Diósi, *Models for universal reduction of macroscopic quantum fluctuations*, Phys. Rev. A **40**, 1165 (1989).

[3] L. Diósi, *A universal master equation for the gravitational violation of quantum mechanics*, Phys. Lett. A **120**, 377 (1987).

[4] G. C. Ghirardi, A. Rimini, T. Weber, *Unified dynamics for microscopic and macroscopic systems*, Phys. Rev. D **34**, 470 (1986).

[5] G. C. Ghirardi, P. Pearle, A. Rimini, *Markov processes in Hilbert space and continuous spontaneous localization of systems of identical particles*, Phys. Rev. A **42**, 78 (1990).

[6] A. Bassi, G. C. Ghirardi, *Dynamical reduction models*, Phys. Rep. **379**, 257 (2003).

[7] A. Bassi, K. Lochan, S. Satin, T. P. Singh, H. Ulbricht, *Models of wave-function collapse, underlying theories, and experimental tests*, Rev. Mod. Phys. **85**, 471 (2013).

[8] S. Donadi, K. Piscicchia, C. Curceanu, L. Diósi, M. Laubenstein, A. Bassi, *Underground test of gravity-related wave function collapse*, Nat. Phys. **17**, 74 (2021).

[9] S. L. Adler, A. Bassi, S. Donadi, *On spontaneous photon emission in collapse models*, J. Phys. A: Math. Theor. **46**, 245304 (2013).

[10] M. Carlesso, L. Ferialdi, A. Bassi, *Colored collapse models from the non-interferometric perspective*, Eur. Phys. J. D **72**, 159 (2018).

[11] J. A. Barandes, *The stochastic-quantum correspondence*, arXiv:2302.10778 (2023).

[12] J. A. Barandes, *The stochastic-quantum theorem*, arXiv:2309.03085 (2023).

[13] E. Nelson, *Derivation of the Schrödinger equation from Newtonian mechanics*, Phys. Rev. **150**, 1079 (1966).

[14] W. H. Zurek, *Decoherence, einselection, and the quantum origins of the classical*, Rev. Mod. Phys. **75**, 715 (2003).

[15] H.-P. Breuer, F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).

[16] M. Arndt, K. Hornberger, *Testing the limits of quantum mechanical superpositions*, Nat. Phys. **10**, 271 (2014).

[17] S. Bose et al., *Spin entanglement witness for quantum gravity*, Phys. Rev. Lett. **119**, 240401 (2017).

[18] C. Marletto, V. Vedral, *Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity*, Phys. Rev. Lett. **119**, 240402 (2017).

[19] W. Marshall, C. Simon, R. Penrose, D. Bouwmeester, *Towards quantum superpositions of a mirror*, Phys. Rev. Lett. **91**, 130401 (2003).

[20] A. Bassi, A. Großardt, H. Ulbricht, *Gravitational decoherence*, Class. Quantum Grav. **34**, 193002 (2017).

[21] H.-P. Breuer, E.-M. Laine, J. Piilo, B. Vacchini, *Colloquium: Non-Markovian dynamics in open quantum systems*, Rev. Mod. Phys. **88**, 021002 (2016).

[22] B. Misra, E. C. G. Sudarshan, *The Zeno's paradox in quantum theory*, J. Math. Phys. **18**, 756 (1977).

[23] S. Nimmrichter, K. Hornberger, *Macroscopicity of mechanical quantum superposition states*, Phys. Rev. Lett. **110**, 160403 (2013).

[24] A. Großardt, J. Bateman, H. Ulbricht, A. Bassi, *Optomechanical test of the Schrödinger-Newton equation*, Phys. Rev. D **93**, 096003 (2016); arXiv:1510.01696.
