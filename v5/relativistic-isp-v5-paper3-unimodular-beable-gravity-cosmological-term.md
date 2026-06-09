# Relativistic ISP V5 Paper 3: Indivisible Beable Matter as a Source for Unimodular Semiclassical Gravity — Gravitational Decoherence, a Dynamical Cosmological Term, and the Covariance Obstruction

Author: Felix Robles Elvira

Date: June 2026

**Status.** A theoretical investigation, not a finished theory. The mathematical
machinery used here is established: unimodular gravity with non-conserved matter
(Josset–Perez–Sudarsky), beable-sourced Newtonian semiclassical gravity
(Tilloy–Diósi), and the relativistic flash ontology (Tumulka). The contribution of
this paper is a **synthesis**: using Barandes' indivisible-stochastic beable as the
matter source for unimodular semiclassical gravity, showing that the
non-conservation splits cleanly into a mean part (a dynamical cosmological term)
and a fluctuating part (gravitational decoherence), that the Newtonian limit
reproduces the Diósi–Penrose / V5-Paper-2 decoherence, and that the binding open
obstruction is **covariance of the beable dynamics**, not energy conservation.

**Scope note (read once).** The gravity-sourcing results (Results 1–6) use only that the
matter is a *non-conserved source*; they are **Markovian-agnostic** and hold for the ISP
beable treated as a non-relativistic / schematic source, exactly as for ordinary collapse
matter — which is the original setting of Josset–Perez–Sudarsky. The word *indivisible* names
the program's ontology, not a load-bearing property of Results 1–6. Wherever "indivisible" or
"relativistic ISP" appears as a *fully covariant interacting-field beable process*, that object
is the **open** problem of §10 — an aspiration the paper isolates and maps, not an input to the
sourcing results. The non-Markovian content bites in exactly two places: the decoherence
*onset shape* (§5, the Gaussian signature) and the §10 covariant-construction lever.

Claims are marked **[STD]** (established), **[SYN]** (this synthesis), or
**[OPEN]**. Nothing is asserted as a solution of quantum gravity or as an
experimentally confirmed deviation from general relativity.

---

## Abstract

A central obstruction to coupling classical gravity to quantum (beable) matter is
that the contracted Bianchi identity forces covariant conservation of the source,
`∇^μ T_{μν}=0`, whereas a stochastic, indivisible beable process injects
energy–momentum and so violates it. We show that **unimodular gravity removes this
obstruction**: its trace-free field equations do not impose conservation, and the
non-conservation is absorbed into a dynamically generated cosmological term
(Josset–Perez–Sudarsky). Using the indivisible-stochastic-process (ISP) beable of
Barandes as the matter source, the violation current `η_ν = ∇^μ T_{μν}` decomposes
into a **mean** part and a **fluctuating** part. The mean part, homogeneous and
isotropic in the cosmic rest frame, is curl-free and sources a dynamical
cosmological term `Λ(t)`; we find, however, that for Diósi–Penrose-type sourcing this
term is quantitatively *excluded* as dark energy — the same regularization length
that the spontaneous-radiation experiments bound caps the induced `Λ` many orders
below the observed value. The fluctuating part
sources metric noise (an Einstein–Langevin term) that, in the Newtonian limit,
reduces to the Diósi–Penrose / Tilloy–Diósi gravitational decoherence and to the
Gaussian-onset, falsifiable signature of V5-Paper-2. The construction therefore
unifies gravitational decoherence and a cosmological term within one framework and
reduces correctly to the testable non-relativistic physics. The remaining binding
obstruction is **not** energy conservation but the covariance of the beable
dynamics: the curl-free condition selects the cosmic rest frame, reintroducing a
preferred foliation that is observationally hidden if confined to the gravitational
sector and excluded if universal. A fully covariant beable ontology exists for
free particles (Tumulka flashes) but is open for the interacting case required to
source gravity. We resolve the recent dispute over the entanglement signature for
this construction — the beable-sourced field is a classical channel and so predicts a
*negative* Bose–Marletto–Vedral result (falsifiable), with mandatory complementary
decoherence — and we isolate the covariance of the beable dynamics as the single
binding open problem.

---

## 1. Introduction and the three couplings

How a classical spacetime couples to quantum matter admits three structurally
distinct answers, and they are experimentally distinguishable in principle
[Bose2017, Marletto2017, Donadi2021]:

1. **Quantized gravity.** The metric is itself in superposition. Gravity can
   mediate entanglement between masses (BMV-positive).
2. **Mean-field semiclassical gravity** (Schrödinger–Newton): `G_{μν}=8πG⟨T_{μν}⟩`.
   This is pathological — superluminal signalling and a nonlinear self-gravity that
   is experimentally constrained. **[STD]**
3. **Stochastic semiclassical gravity**: the field is classical but sourced by the
   *actual localized* matter, not the mean. Tilloy and Diósi [TilloyDiosi2016]
   showed this is consistent in the Newtonian limit and yields gravitational
   decoherence as a necessary by-product. **[STD]**

The indivisible-stochastic-process (ISP) reformulation of quantum theory
[Barandes2023a, Barandes2023b] is a natural home for option 3: its primitive
ontology is a definite configuration (beable) at all times, which is precisely the
localized source that option 3 needs and that Tilloy–Diósi had to supply by hand
through collapse outcomes. V5-Paper-2 used this in the Newtonian regime to derive a
falsifiable, non-exponential (Gaussian-onset) gravitational decoherence.

This paper asks the relativistic question: **can the ISP beable source classical
gravity covariantly?** The immediate obstruction is energy conservation, and the
main result is that unimodular gravity removes it, at the price of a dynamical
cosmological term and a residual covariance problem that we isolate sharply.

## 2. The obstruction: Bianchi versus beable non-conservation

In general relativity the field equation `G_{μν}=8πG\,T_{μν}` together with the
contracted Bianchi identity `∇^μ G_{μν}≡0` forces

```math
\nabla^\mu T_{\mu\nu} = 0 .
```

An ISP beable process injects energy–momentum: the record-stabilization (the
indivisible analogue of collapse) causes the matter stress–energy built from the
actual configuration to jump and diffuse, so that

```math
\nabla^\mu T_{\mu\nu} = \eta_\nu \neq 0 ,
```

with `η_ν` a stochastic violation current. The left side of Einstein's equation is
identically divergence-free; the right side is not. The naive coupling is
inconsistent. This is the obstruction that has made relativistic collapse / beable
gravity difficult [Bassi2013]. **[STD]**

## 3. Unimodular gravity removes the obstruction

Unimodular gravity (UG) fixes the metric determinant (`\sqrt{-g}` non-dynamical) and
yields the **trace-free** Einstein equations [HenneauxTeitelboim1989, Unruh1989]:

```math
R_{\mu\nu} - \tfrac14 g_{\mu\nu} R = 8\pi G\big(T_{\mu\nu} - \tfrac14 g_{\mu\nu} T\big).
```

Conservation is no longer imposed by the field equations. Taking the divergence and
using the contracted Bianchi identity `∇^μ R_{μν}=\tfrac12∇_ν R`:

```math
\tfrac14 \nabla_\nu R = 8\pi G\big(\nabla^\mu T_{\mu\nu} - \tfrac14 \nabla_\nu T\big)
\;\Longrightarrow\;
\tfrac14\nabla_\nu\big(R + 8\pi G\,T\big) = 8\pi G\,\eta_\nu .
```

Define the scalar `Λ` through `R + 8\pi G\,T \equiv 4\Lambda`. Two cases:

```math
\boxed{
\begin{array}{ll}
\eta_\nu = 0: & \Lambda = \text{const} \quad(\text{the usual UG integration constant}),\\[4pt]
\eta_\nu \neq 0: & \nabla_\nu \Lambda = 8\pi G\,\eta_\nu \quad(\Lambda\text{ becomes dynamical, integrating the violation}).
\end{array}}
```

So in UG the non-conservation is **not** inconsistent: it is absorbed into a
dynamical cosmological term. Consistency requires only that `η_ν` be a gradient
(curl-free), `η_ν=∇_ν φ`, so that `Λ = 8πG\,φ + Λ_0` is a well-defined scalar. This
is exactly the mechanism of Josset–Perez–Sudarsky [Josset2017], who proposed it for
energy violation from nonunitary quantum modifications and Planckian discreteness —
the ISP beable being a concrete realization of the former. **[STD mechanism; [SYN]
applied to ISP.]**

> **Result 1 [SYN].** The conservation-vs-Bianchi obstruction to sourcing relativistic
> gravity from *any* non-conserved matter (the ISP beable being one instance) is *not*
> fatal. Unimodular gravity evades it, converting the violation into a dynamical
> cosmological term, provided the violation current is curl-free. The mechanism uses only
> non-conservation — it is **Markovian-agnostic**, holding equally for ordinary collapse
> matter (the original setting of [Josset2017]); indivisibility is not used here.

## 4. The mean/fluctuation split

The violation current of a stochastic beable decomposes into ensemble mean and
fluctuation,

```math
\eta_\nu = \langle\eta_\nu\rangle + \delta\eta_\nu .
```

**The mean — a dynamical cosmological term.** For a record-stabilization process
that is homogeneous and isotropic in the cosmic rest frame, the mean violation has
no preferred spatial direction: `⟨η_i⟩ = 0`, while `⟨η_0⟩ = w(t)` is a net
energy-density injection rate. Then `⟨η_ν⟩ = (w(t),\mathbf 0)` **is curl-free**,
`⟨η_ν⟩ = ∇_ν φ` with `φ(t)=∫ w\,dt`, and from Result 1

```math
\Lambda(t) = \Lambda_0 + 8\pi G \int^t w(t')\,dt' .
```

The accumulated mean violation is a cosmological term. This is the same structure
Josset–Perez–Sudarsky identified; here it is sourced by the ISP record-stabilization
rate. **[SYN]**

**The fluctuation — gravitational decoherence.** The fluctuating part `δη_ν` is
*not* curl-free; it cannot be absorbed into `Λ`. Instead it sources metric
fluctuations through the trace-free equations — an Einstein–Langevin noise term in
the sense of stochastic gravity [HuVerdaguer2008]. A massive system in spatial
superposition is dephased by this gravitationally-sourced noise. This is the
relativistic origin of the gravitational decoherence channel. **[SYN]**

> **Result 2 [SYN].** The single ISP non-conservation splits into a **mean** part
> (curl-free, in the cosmic rest frame) sourcing a dynamical cosmological term, and
> a **fluctuating** part sourcing metric noise and hence gravitational decoherence.
> Dark-energy-like behaviour and gravitational decoherence are two faces of the same
> beable non-conservation.

## 5. The Newtonian limit: recovery of V5-Paper-2 and the entanglement question

In the weak-field, non-relativistic limit UG reduces to the Poisson equation
`∇²Φ = 4πG ρ`, sourced by the beable mass density `ρ` (which is non-negative and
needs no conservation constraint — the obstruction is absent precisely because there
is no Bianchi identity in the Newtonian limit). The fluctuating source then
reproduces, term for term, the Tilloy–Diósi beable-sourced gravity [TilloyDiosi2016]:
the Newtonian pair potential up to a short-distance cutoff, plus a gravitational
decoherence term. With the **indivisible** (non-divisible) survival law of
V5-Paper-2, the decoherence is non-exponential, with the falsifiable Gaussian onset

```math
C(T) = C(0)\,\exp\!\big[-\tfrac12 (T/\tau_G)^2\big], \qquad \tau_G = \hbar/E_G,
```

`E_G` the Diósi–Penrose self-energy of the mass-density difference [Diosi1989,
Penrose1996]. So the relativistic construction reduces correctly to the testable
non-relativistic physics. **[SYN; reduces to STD]**

**The entanglement signature — resolved for the ISP construction.** The
ISP-beable-sourced field is, by construction, a *classical channel*: gravity is
sourced by the definite beable configuration (one value per mass), not by the
superposed wavefunction. Kafri, Taylor and Milburn [KTM2014] proved that a
classically-mediated gravitational interaction — which they showed is *equivalent to
Diósi's model*, and hence to the present construction — **cannot create
entanglement** (it can never entangle Gaussian systems), while necessarily producing
decoherence equivalent to Diósi's. Entanglement cannot increase under local
operations and classical communication, and the beable-sourced field carries only
classical information about the actual configuration. Therefore:

> **Result 4 [SYN].** The ISP-beable-sourced construction predicts a **negative**
> BMV result (no gravitationally-induced entanglement) together with mandatory,
> complementary gravitational decoherence; the two are linked by the
> classical-channel structure [KTM2014]. A *positive* BMV result would falsify the
> ISP-sourced construction.

This resolves the 2025 literature dispute as a model-definition issue. The analyses
finding entanglement [Trillo2025] treat the gravitational interaction as a quantum
two-body potential acting on superposed positions (with Diósi–Penrose decoherence
added on top); those finding none [Collapse2025, KTM2014] treat gravity as a
classical channel sourced by the localized matter. The ISP ontology falls
unambiguously on the classical-channel side, because its field sees the *beable*, not
the wavefunction. (Such a channel can still generate quantum *discord* short of
entanglement [Discord2022]; BMV witnesses entanglement specifically, so the negative
prediction stands.) **[SYN]**

## 6. Magnitudes

**Decoherence.** The Newtonian-limit decoherence scale is the Diósi–Penrose
`τ_G=ℏ/E_G`, with the V5-Paper-2 thresholds (object-scale superpositions of
`10^{10}`–`10^{12}` amu over second-to-hour holds). **[STD/SYN]**

**Cosmological term — quantitatively excluded for Diósi–Penrose sourcing.**
Matching the observed dark-energy density `ρ_Λ c² ≈ 6×10^{-10}\,\mathrm{J\,m^{-3}}`,
accumulated over a Hubble time `t_H ≈ 4×10^{17}\,\mathrm{s}`, requires a mean
energy-injection rate density

```math
\langle w\rangle \sim \frac{\rho_\Lambda c^2}{t_H} \sim 1.5\times10^{-27}\,\mathrm{J\,m^{-3}\,s^{-1}} .
```

The Diósi–Penrose injection rate is *not* free once the regularization length `R_0`
is fixed: the per-nucleon energy-injection (momentum-diffusion) rate is

```math
\frac{dE}{dt} \sim \frac{3}{2}\,\frac{\hbar\,G\,m_N}{R_0^{3}} .
```

Using the experimentally-allowed `R_0 ≳ 0.5`–`4\,\text{Å}` (the Donadi bound
[Donadi2021]) and `m_N` the nucleon mass gives `dE/dt ∼ 10^{-41}`–`10^{-43}\,\mathrm{W}`
per nucleon. Times the cosmic baryon number density (`n_N ∼ 0.25\,\mathrm{m^{-3}}`),

```math
w_{\rm DP} \sim n_N\,\frac{dE}{dt} \sim 10^{-42}\text{–}10^{-44}\,\mathrm{J\,m^{-3}\,s^{-1}},
```

which is **12–16 orders of magnitude below** the required `⟨w⟩`. An early-universe
enhancement (`∝(1+z)^{3/2}` integrated, `∼10^{4}`–`10^{5}`) does not close the gap.
Equivalently, reaching `ρ_Λ` would require `R_0 ∼ 10^{-15}\,\mathrm{m}` (femtometre
scale), which the Donadi spontaneous-radiation bound **excludes by ~5 orders of
magnitude**.

> **Result 5 [SYN].** Diósi–Penrose-type ISP sourcing is *not* a viable dark-energy
> mechanism: the **same regularization length `R_0`** that the spontaneous-radiation
> experiments bound also fixes the cosmological injection, and the allowed `R_0`
> makes the induced `Λ` many orders too small. The decoherence/radiation bound
> forecloses the cosmological-term magnitude. The unimodular mechanism of §3–§4 is
> real, but **for DP-type sourcing its dark-energy realization is quantitatively
> excluded** — the honest statement is: a correct mechanism with an excluded
> magnitude. **[SYN]**

**Dark matter — no mechanism.** Dark matter is a *content* problem (missing
gravitating mass: rotation curves, lensing, the CMB third peak, structure formation,
and the Bullet Cluster's lensing/gas offset), and the construction offers nothing for
it. It adds no matter content; in the Newtonian limit the beable-sourced field
*reproduces* Newtonian gravity up to the short-distance cutoff `R_0 ∼ Å`
[TilloyDiosi2016], so there is no galactic-scale (MOND-like) modification. At linear
order the mean field sourced by the fluctuating beable equals the mean-field result,
`⟨g(T[q])⟩ = g(⟨T⟩)`, so beable-sourcing adds no extra mean attraction; only the
*fluctuations* differ, and they source decoherence, not gravitating mass. The energy
budget of the entire ISP-novel sector (injection plus fluctuation back-reaction) is
bounded, by the same `R_0` decoherence/radiation limit as in Result 5, to `≳12`
orders of magnitude below `ρ_Λ`, hence far below `ρ_{DM} ∼ 2ρ_Λ`; and its equation of
state (heating, `w>0`; metric noise, `w≈1/3`) is not that of pressureless matter
(`w≈0`). The Bullet Cluster independently excludes the only conceivable route
(modified gravity). **[SYN/STD]**

> **Result 6 [SYN].** The ISP-sourced construction provides no dark-matter mechanism:
> it adds no mass content, reduces to Newtonian gravity at galactic scales, and its
> novel sector is both far too small and of the wrong equation of state. Together with
> Result 5, **ISP/RISP gravity addresses neither component of the dark sector** — both
> are content / cosmological-gravity problems, while ISP reformulates dynamics.

## 7. The binding obstruction: covariance of the beable dynamics

Unimodular gravity solves the *conservation* problem but not the *covariance*
problem. Two features of the construction expose a preferred frame:

1. The mean violation `⟨η_ν⟩` is curl-free **only in the frame where it carries no
   net momentum** — the cosmic (matter) rest frame. The well-definedness of `Λ(t)`
   therefore selects a preferred foliation.
2. The beable is a configuration defined on a spatial slice; its indivisible
   stochastic evolution presupposes a notion of simultaneity.

The status of this preferred frame was analysed in the companion calculation:

```math
\boxed{
\begin{array}{ll}
\text{universal foliation:} & \text{anisotropies }\sim\beta^2\sim10^{-6}\ \text{excluded by Lorentz tests at }\sim10^{-18},\\
\text{foliation confined to the gravity/decoherence sector:} & \text{evades bounds, but its signatures are }\lesssim10^{-7}\ \text{(unobservable)}.
\end{array}}
```

So a preferred-frame RISP gravity is consistent only if the frame is confined to
the non-unitary sector, where it is empirically hidden (**Route A**). The covariant
alternative — a beable ontology with no preferred slicing (**Route B**) — is more
advanced than a free-particle construction. Tumulka realizes a Lorentz-invariant
flash collapse not only for non-interacting particles [Tumulka2006] but for
interacting **distinguishable** particles [Tumulka2020], by inserting flashes into a
Tomonaga–Schwinger evolution between arbitrary spacelike hypersurfaces — manifestly
foliation-independent, non-local but no-signaling, reducing to non-relativistic GRW,
and valid in curved spacetime. The genuine remaining gap is his own stated
limitation: the construction is *not* known for indistinguishable particles or
variable particle number — i.e. for a **quantum field**, which is exactly what
sourcing gravity requires. So the binding obstruction is sharper than "covariance of
the beable dynamics" in general: it is the **covariant interacting beable dynamics of
a quantum field**.

Any candidate must thread established no-go results. A relativistically-invariant
**Markovian** collapse in standard QFT cannot satisfy vacuum stability and
no-signaling without nonstandard degrees of freedom; a Lorentz-covariant
mass-coupled collapse cannot simultaneously avoid a divergent energy-production rate
and prevent superluminal signaling [MassCoupled2020]; and Gisin's theorem
[Gisin1989] forbids nonlinear (hence signaling) ensemble dynamics. Together these say
that one of {strict Lorentz invariance, Markovian dynamics, standard field ontology}
must be abandoned. **The ISP beable is non-Markovian (indivisible) *and* non-standard
(a beable ontology) — it abandons two of the three** — so it has, in principle, more
structural room than any Markovian collapse model to thread the no-go. Whether that
room suffices to build a covariant interacting *field* beable dynamics is the binding
open question (§9). **[OPEN]**

> **Result 3 [SYN/OPEN].** The binding obstruction to relativistic ISP gravity is
> not energy conservation (solved by UG) but the covariance of the beable dynamics
> for a **quantum field**. A covariant interacting flash dynamics already exists for
> *distinguishable* particles [Tumulka2020]; the field / variable-particle-number case
> required to source gravity is open. Because the ISP beable is both non-Markovian and
> of non-standard ontology, it forgoes two of the three properties that the
> relativistic-collapse no-go theorems force one to abandon — giving it, in principle,
> the room to thread them.

## 8. Falsifiable content and honest scope

**What is testable.** (i) Gravitational decoherence with a non-exponential
(Gaussian) onset at the Diósi–Penrose scale, in matter-wave / levitated /
optomechanical interferometry — the V5-Paper-2 discriminator. (ii) The
classical-vs-quantum-gravity fork via BMV: the ISP construction is a classical
channel, so it predicts **no** gravitationally-induced entanglement, and a *positive*
BMV result would falsify it (§5, Result 4). (iii) A preferred-frame modulation of the
decoherence rate at the `≲10^{-7}` level (unobservable for the foreseeable future,
but constrained from above by Lorentz tests if the frame is universal).

**What is not a prediction.** The cosmological term is a real *mechanism* but **not**
a dark-energy prediction: for Diósi–Penrose-type sourcing its magnitude is
quantitatively excluded by the same `R_0` bound that constrains the decoherence
(Section 6, Result 5). The decoherence scale is Diósi–Penrose's, not new; the
contribution is the non-exponential shape (indivisibility) and the unified
relativistic framing.

**Relation to existing work.** The unimodular-violation mechanism is
Josset–Perez–Sudarsky [Josset2017]; the Newtonian beable-sourced gravity and its
decoherence are Tilloy–Diósi [TilloyDiosi2016]; the covariant flash ontology is
Tumulka [Tumulka2006]; the stochastic ontology is Barandes [Barandes2023a,
Barandes2023b]. This paper's contribution is the **synthesis** — ISP beables as the
unimodular source, the mean/fluctuation split unifying dark energy and decoherence,
the correct Newtonian reduction, and the sharp isolation of covariance as the
binding obstruction. It is incremental and synthetic, not a new framework.

**Known-address caveat.** As with the Bell-locality and frame-dependence analyses
of this program, the distinctive signatures here (classical-gravity BMV behaviour,
non-Markovian onset) are shared with other collapse / classical-gravity models. ISP
provides a principled ontology and a unifying frame, not a unique fingerprint.

## 9. Open problems

1. **Covariant interacting *field* beable dynamics — the binding problem [OPEN].**
   Precisely: *construct a Lorentz-covariant, foliation-independent ISP beable
   dynamics for a quantum field (indistinguishable particles / variable particle
   number) that sources gravity.* The distinguishable-particle case is solved
   (Tumulka, Tomonaga–Schwinger + flashes [Tumulka2020]); the field case — required
   for a stress-energy source — is not. Any solution must thread three established
   no-go constraints:
   (a) a relativistic **Markovian** collapse in standard QFT cannot keep both vacuum
   stability and no-signaling without nonstandard degrees of freedom;
   (b) a Lorentz-covariant mass-coupled collapse cannot both avoid divergent energy
   production and forbid superluminal signaling [MassCoupled2020];
   (c) nonlinear ensemble dynamics signal (Gisin) [Gisin1989].
   These force abandoning one of {strict Lorentz invariance, Markovian dynamics,
   standard field ontology}. **The ISP beable already abandons two** (it is
   non-Markovian and non-standard-ontology), so the sharp, genuinely ISP-specific
   question is: *does that non-Markovianity provide enough room to build the covariant
   interacting field dynamics that Markovian collapse provably cannot?* A positive
   answer makes relativistic ISP gravity a consistent theory; a clean negative
   converts Route A (a hidden cosmic-rest-frame) from retreat into theorem. Either
   outcome is a result.
2. **Curl-free violation beyond the mean [OPEN].** We showed the *mean* violation is
   curl-free in the cosmic rest frame; characterize the conditions under which the
   coarse-grained violation remains curl-free, and the back-reaction of `δη_ν`.
3. **Cosmological magnitude of `Λ` [RESOLVED, negative].** Computed (§6, Result 5):
   Diósi–Penrose-type sourcing with the experimentally-allowed `R_0` gives `Λ` 12–16
   orders of magnitude too small; the dark-energy realization is excluded. Residual
   open question: whether a *non*-DP record-stabilization law (an `R_0`-independent
   injection) could evade this without conflicting with the decoherence bounds.
4. **BMV entanglement [RESOLVED for this construction].** Settled (§5, Result 4): the
   beable-sourced field is a classical channel, so it does not entangle [KTM2014];
   the 2025 dispute is a model-definition issue. Residual open question: whether a
   covariant interacting version (open problem 1) preserves the classical-channel
   no-entanglement property.

## 10. Investigating the binding obstruction: relativistic stochastic field theory and a free-field testbed

This section develops open problem 1 from the properties of the indivisible ontology,
locates it within the fifty-year literature on relativistic stochastic field theory,
and proposes a concrete first attack. The conclusion is that the obstruction is
precise and well-posed, that ISP's non-Markovianity is the right tool for a structural
reason, and that the free scalar field is the right testbed — but the problem is
genuinely open.

### 10.1 The reduction

Stripped of the gravitational coupling (which is only the source term), open problem 1
is: construct a **Lorentz-covariant, real-time stochastic process, with genuine
non-negative probabilities, over field configurations, that reconstructs the unitary
QFT**. This is relativistic stochastic mechanics for fields done with honest
probabilities — the field-theoretic Nelson/Barandes problem. The beable is a field
configuration `φ` on a slice, so the foliation enters; the indivisible (non-Markovian)
law is the candidate escape from the relativistic-collapse no-go (§7).

### 10.2 The covariant stochastic structure exists — in Euclidean signature

A relativistic QFT carries a genuine, manifestly covariant probability measure over
field configurations: the **Euclidean measure** (`e^{-S_E}` is a positive weight; a
bona fide random field whose Euclidean rotation invariance becomes Lorentz invariance
after Wick rotation), with the Osterwalder–Schrader reconstruction recovering the
Lorentzian theory via reflection positivity. Guerra and Ruggiero proved that this
**Euclidean–Markov field is precisely the ground-state stochastic process of Nelson's
stochastic mechanics** for the field [GuerraRuggiero1973, Nelson1973]. The Markov
structure is diagnostic:

```math
\boxed{
\begin{array}{ll}
\text{free field:} & \text{Euclidean field is Markov (Nelson)},\\
\text{interacting field:} & \text{Euclidean field is generically non-Markov}.
\end{array}}
```

So non-Markovianity is not an exotic ISP add-on — it is the generic structure of
interacting relativistic random fields. **[STD]**

### 10.3 The apparent process-level sign problem (refined by Result 10)

The covariant measure of §10.2 is *Euclidean*. The **real-time** (Lorentzian) path
integral has oscillatory `e^{iS}` weights — not a probability measure (the sign
problem). The precise statement is that the *result* of a real-time path integral is
covariant, but its *time-sliced, intermediate-stage* expressions are not. A stochastic
**process** lives exactly at that intermediate, time-sliced level, so covariantizing
the process is the hard part **even though the final QFT is covariant**. Hence a
genuine-probability, real-time, covariant process must encode the quantum phase — the
source of the oscillation — in something other than the weights. **[STD framing]**

### 10.4 Why indivisibility is the right tool

The ISP mechanism is exactly this: in Barandes' construction the quantum phase is
encoded in the **non-Markovian memory** of the indivisible process, not in complex
weights, so the real-time transition probabilities stay genuine [Barandes2023a,
Barandes2025]. This identifies the structural reason ISP can hope to succeed where the
classic attempt failed:

```math
\boxed{
\text{Nelson's stochastic mechanics} \;=\; \text{the Markovian-diffusion special case of the indivisible class.}
}
```

Nelson's process is a specific Markov diffusion, and that Markov-diffusion structure
is exactly what selects a time direction and resists covariantization (the fifty-year
obstruction, studied even for the free scalar field [FenyesNelsonCov]). Barandes'
indivisible processes are the **general non-Markovian class** containing Nelson's as
one member. The sharp, genuinely ISP-specific question is therefore:

> **Does the general indivisible (non-Markovian) class contain a Lorentz-covariant,
> interacting-field member — precisely because non-Markovianity supplies the freedom
> that Nelson's Markov diffusion lacked?**

Three structural facts make this the right question rather than wishful thinking:
(i) interacting Euclidean fields are *already* non-Markov (§10.2), so the Markov
restriction was wrong for the interacting/covariant case from the start; (ii) the
relativistic-collapse no-go is for *Markovian* dynamics (§7), so the same property
that resists the no-go is the one Nelson lacked; (iii) it localizes the obstruction to
a single object — a covariant, memory-encoded (non-Markovian) real-time process whose
`c→∞` and free-field limits are controlled. **[SYN]**

*Caveat (established in §10.5): the free-field test below shows this reading needs
correction — the free field is covariant while remaining Markov, so non-Markovianity is
not what buys covariance per se; it is implicated only in the interacting,
Wigner-negative case. The sharpened question is therefore not "does non-Markovianity
covariantize?" but "can a non-Markovian configuration-space process give a covariant
genuine-probability description of an interacting field, where Gaussianity (Hudson) is
lost?"*

### 10.5 The free-scalar-field testbed: a worked result (and a correction)

We carried out the test. **Outcome: a covariant genuine-probability ISP exists for the
free field — but it works through Gaussianity, not non-Markovianity, which
*disconfirms* the §10.4 reading.**

Explicitly, the free field is one decoupled oscillator per spatial mode `k` with
frequency `ω_k=√(k²+m²)`; Nelson's process makes each an independent
Ornstein–Uhlenbeck (Markov) process with correlation

```math
\langle \tilde\varphi(k,t)\,\tilde\varphi(-k,t')\rangle = \frac{1}{2\omega_k}\,e^{-\omega_k|t-t'|},
```

which is exactly the Euclidean propagator in the mixed `(k,τ)` representation
[GuerraRuggiero1973]. A covariant genuine-probability description exists in two
independent ways:

```math
\boxed{
\begin{array}{ll}
\text{(A) Euclidean random field:} & e^{-S_E}\ \text{is a genuine } O(4)\text{-invariant probability measure on 4D configs;}\\
\text{(B) phase space (Wigner):} & \text{the Gaussian vacuum has a positive Wigner functional [Hudson1974],}\\
 & \text{giving a genuine phase-space probability under classical Liouville flow.}
\end{array}}
```

So relativistic ISP **exists for the free scalar field** — the proof of concept
succeeds. But two honest caveats gut its bearing on the hard problem:

1. **It works via Gaussianity, not non-Markovianity.** The free-field process is
   *Markov*; no memory kernel was needed. Covariance came from Gaussianity and the
   Euclidean-field structure. This **disconfirms the §10.4 reading** that
   non-Markovianity is what buys covariance: here the process is Markov *and*
   covariant. The free field is the wrong testbed for the mechanism the hard case
   needs.
2. **Hudson's theorem turns the interacting wall into a theorem.** A pure state has a
   non-negative Wigner function *iff* it is Gaussian [Hudson1974]. So any interaction
   (non-Gaussian state) makes the phase-space distribution **negative** — the sign
   problem, as a theorem — and route (B) dies at the first interaction. Route (A)'s
   configuration-space marginal `|Ψ[φ]|²` stays positive, but the interacting
   Euclidean field is then non-Markov and its covariant *real-time* genuine-probability
   process is exactly what is unestablished.

> **Result 7 [SYN].** Relativistic ISP exists for the *free* scalar field (Gaussian,
> integrable: positive Wigner [Hudson1974] / Euclidean–Markov field
> [GuerraRuggiero1973]) — but for the trivial reason (Gaussianity) and *without*
> non-Markovianity, so it neither advances nor is evidence for the interacting
> conjecture, and it corrects §10.4. Hudson's theorem makes the interacting obstruction
> precise: positive phase-space probability is Gaussian-only, so the
> genuine-probability description of an interacting field must abandon the
> phase-space-positive form — which is where, and only where, the non-Markovian
> configuration-space mechanism would have to do its (open) work.

### 10.6 Beyond the free field: the case map and the reduction to pure foliation-independence

Surveying the other cases sharpens which obstruction is real. Arrange them by
(free vs interacting) × (non-relativistic QM vs relativistic field):

```math
\boxed{
\begin{array}{l|cc}
 & \text{non-rel.\ QM} & \text{relativistic field}\\
\hline
\text{free / Gaussian} & \text{Barandes ISP } \checkmark & \text{Result 7 } \checkmark\\
\text{interacting} & \text{Barandes ISP } \checkmark & \textbf{open}
\end{array}}
```

Three of the four cells are settled, and inspecting them removes two candidate
obstructions and demotes a third:

- **Interacting QM is already an ISP (Barandes).** His theorem builds an indivisible
  configuration-space process for *any* unitary system, including Wigner-negative
  (anharmonic, interacting) states; the configuration-space probability `|Ψ|²` stays
  positive regardless, and the Wigner-negativity is carried by the non-Markovian
  structure. **So Hudson's theorem (Result 7) is a *phase-space* obstruction that does
  not block configuration-space ISP** — it bars route (B), not the ISP route.
  Wigner-negativity is therefore *not* the core difficulty.
- **The covariant genuine-probability *measure* exists for interacting fields.**
  Constructive QFT rigorously builds the Euclidean measures of interacting
  two-dimensional models (`P(φ)₂`, `φ⁴₂`; Glimm–Jaffe [GlimmJaffe1987]) as genuine
  `O(2)`-invariant probability measures. So the existence of a covariant probability
  structure over interacting-field configurations is not the obstruction either.
- **Special interacting fields inherit a covariant ISP by duality.** Two-dimensional
  models dual to free theories — Thirring and sine-Gordon via bosonization
  [Coleman1975], the Ising model via its free-Majorana equivalent — reproduce their
  correlators through a free theory, hence through the free covariant ISP of Result 7.
  A genuine second proof of concept beyond Gaussian, with the honest caveat that it is
  duality-dependent and the beable lives in the dual variables.

What remains is *not* the existence of an interacting-field ISP and *not*
Wigner-negativity. Formally, Barandes' construction applied to the (interacting) QFT
Hilbert space and its `U(t)` already yields a configuration-space ISP **in a chosen
frame** — so the residue is purely **foliation-independence**: making that
frame-dependent process manifestly covariant.

> **Result 8 [SYN].** Surveying the other cases removes the candidate obstructions one
> by one: interacting QM is already an ISP (so Wigner-negativity, Result 7, is a
> phase-space issue that configuration-space ISP evades); the covariant interacting
> probability *measure* exists (constructive QFT in 2D); and 2D dualities give covariant
> interacting ISPs via free duals. The binding obstruction therefore narrows to its
> purest form — **foliation-independence of the (frame-dependently existing) interacting
> field process** — subject to one further open sub-issue: the rigorous extension of
> Barandes' construction to interacting QFT, which must contend with Haag's theorem and
> inequivalent representations [StreaterWightman1964].

Honest caveats: the 2D constructive and duality results are special (low dimension,
integrability); they show the covariant structure *can* exist for interacting fields,
not that the general four-dimensional case does. And the reduction to "pure foliation"
holds *modulo* the rigorous QFT extension of Barandes (Haag's theorem), itself
unestablished. **[SYN/OPEN]**

### 10.7 Does Haag's theorem obstruct the covariant interacting ISP, or merely complicate it?

The §10.6 residue carried one caveat — extending Barandes' construction to interacting
QFT against Haag's theorem. Its status: **Haag's theorem complicates, but does not
forbid, the interacting-field ISP; it does, however, close the manifestly-covariant
route that solved the distinguishable-particle case.** Three established facts settle
it.

- **Haag forbids only the interaction picture.** No unitary operator relates the free
  and interacting representations; the interaction picture does not exist for fields.
  But the theorem does *not* forbid the interacting theory itself — an interacting QFT
  exists as a Poincaré-covariant theory in its *own* representation (Wightman axioms),
  and constructive QFT builds it for `P(φ)₂`, `φ⁴₂` [GlimmJaffe1987] precisely by
  abandoning the equal-time-CCR / interaction-picture assumption of Haag's reductio.
- **The configuration-space representation ISP needs exists for interacting fields.**
  The **Schrödinger functional representation** — states as functionals `Ψ[φ]` of field
  configurations, evolved by `U(t)=e^{-iHt}` with the full interacting `H` — describes
  interacting fields without the free↔interacting unitary that Haag forbids, and is
  renormalizable (Symanzik [Symanzik1981]). That is exactly the configuration basis
  `{|φ⟩}` and dynamics Barandes' construction requires, in the interacting theory's own
  Haag-evading representation. **So a frame-dependent interacting-field ISP exists** —
  Haag merely complicates it (one must work in the interacting representation, not the
  free Fock space).
- **But the Schrödinger functional is *not manifestly Lorentz invariant*, and the
  manifestly-covariant route is Haag-blocked.** The covariant interaction picture is
  precisely the **Tomonaga–Schwinger** functional evolution between hypersurfaces — the
  tool that made Tumulka's *distinguishable-particle* construction covariant — which
  Haag's theorem says does not exist for fields. So Haag **closes the bridge** from the
  solved distinguishable-particle case to the field case. The interacting theory is
  covariant in its own representation, but that covariance is *non-manifest* in the
  config-space (Schrödinger-functional) presentation the beable lives in — which is the
  foliation residue, now identified concretely.

> **Result 9 [SYN].** Haag's theorem does **not** obstruct the *existence* of an
> interacting-field ISP: the Schrödinger functional representation [Symanzik1981]
> supplies the configuration basis and dynamics in the interacting theory's own,
> Haag-evading representation, so a *frame-dependent* interacting-field ISP exists. Haag
> **does** obstruct the manifestly-covariant interaction-picture / Tomonaga–Schwinger
> route — the exact tool that made the distinguishable-particle case (Tumulka)
> covariant — which is why that success does not transfer to fields. The binding residue
> is therefore sharp and non-Haag: promote the *non-manifest* Lorentz covariance of the
> Schrödinger-functional interacting theory to a *manifestly covariant* configuration-space
> ISP **without** the interaction picture. A prior covariant beable-QFT attempt —
> Nikolić's many-fingered-time / Tomonaga–Schwinger Bohmian QFT [Nikolic2006] — *claims*
> exactly this (a covariant beable QFT with no preferred foliation), but at a formal level
> whose rigorous status against Haag's theorem is itself the open question.

Honest caveats: that a manifestly covariant configuration-space ISP can be built by some
non-interaction-picture route (algebraic, Euclidean-reconstruction, or non-Markovian
memory) is **neither proven nor excluded** — no no-go, but no construction either; and the
prior Bohmian attempts remain debated as to whether they achieve manifest covariance or
smuggle in a preferred foliation. **[SYN/OPEN]**

### 10.8 Attempting the residue (route a): a four-way no-free-lunch

We attempted the residue of Result 9 along the most tractable route — Euclidean
(Osterwalder–Schrader) reconstruction — and the honest outcome is a structured
obstruction, not a construction. Four desiderata are in play for a relativistic ISP:
**(C)** manifest Lorentz covariance, **(R)** real (Lorentzian) time, **(P)** genuine
non-negative probability, **(E)** a beable that evolves in physical time. The natural
constructions each achieve three and sacrifice one:

```math
\boxed{
\begin{array}{l|cccc|l}
\text{route} & \text{C} & \text{R} & \text{P} & \text{E} & \text{sacrifices}\\
\hline
\text{Barandes }|U|^2 & - & \checkmark & \checkmark & \checkmark & \text{manifest covariance (}U(t)\text{ needs a frame)}\\
\text{Euclidean / OS} & \checkmark & - & \checkmark & - & \text{real time \& process (gives a Hilbert space, not a process)}\\
\text{stochastic quantization} & \checkmark & - & \checkmark & \checkmark & \text{physical-time evolution (fictitious Langevin time)}\\
\text{complex Langevin} & \checkmark & \checkmark & - & \checkmark & \text{positivity (complex weights: the sign problem)}
\end{array}}
```

- **Barandes `|U|²`.** The transition probabilities `p(q',t'|q,t)=|⟨q'|U(t'-t)|q⟩|²` are
  genuinely non-negative and normalized — *no sign problem at the pairwise level*. The
  quantum-ness lives in the non-Markovian incompatibility of the multi-time joint
  distributions, not in any negativity of the pairwise probabilities. (This corrects the
  "process-level sign problem" language of §10.3: the binding obstruction for ISP is
  covariance, not positivity, since `U(t)=e^{-iHt}` requires a time.)
- **Euclidean / OS reconstruction.** The Euclidean measure `e^{-S_E}` is a genuine,
  manifestly covariant probability measure — but over *Euclidean* (imaginary-time) field
  histories. OS reconstruction yields the Lorentzian Hilbert space, Hamiltonian, and
  real-time *correlation functions* by analytic continuation — but **not a real-time
  stochastic process**: the continued object is a set of correlators, not a
  genuine-probability process over real-time histories.
- **Stochastic quantization (Parisi–Wu).** A genuinely covariant, genuine-probability
  *process* — but parametrized by a fictitious Langevin time, with the beable a 4D
  (block-universe) field history sampled in that unphysical parameter rather than a
  configuration evolving in physical time.
- **Real-time stochastic quantization (complex Langevin).** Restores real time and a
  process, but the weights are complex — the sign problem returns as a non-positivity /
  convergence pathology.

The deep tension: **manifest covariance pulls toward a 4D block-universe (history) object
with no preferred-time evolution, while Barandes' ISP wants a beable evolving in physical
time.** These oppose each other. So the residue forces a fork — either give up manifest
covariance (**Route A**: a hidden cosmic-rest frame, §7), or give up physical-time
evolution for a probability measure over 4D field histories (a block-universe beable,
Euclidean / Parisi–Wu flavour). Neither is what naive "relativistic ISP" wanted.

> **Result 10 [SYN/OPEN].** The Euclidean-reconstruction attempt at the residue does not
> close it; with its siblings it reveals a four-way *no-free-lunch* among {manifest
> covariance, real time, genuine probability, physical-time-evolving beable} — every known
> construction sacrifices exactly one. Manifest covariance specifically favours a 4D
> block-universe (history) ontology and opposes Barandes' physical-time process, so a
> manifestly covariant relativistic ISP appears to require either a hidden preferred frame
> (Route A) or the abandonment of physical-time evolution for a 4D-history beable. This is
> a structured map of the obstruction, not a no-go: no theorem forbids a fifth route, but
> none of the standard four delivers all four desiderata.

Honest caveat: the table's tradeoffs are individually standard; the four-way framing and
the "covariance ⇒ block-universe vs. physical-time process" fork are this paper's
synthesis, not theorems, and a construction evading the fork is not excluded. **[SYN/OPEN]**

### 10.9 Working the residue: the many-fingered-time route and the foliation-relative-beable condition

A direct attack on the residue identifies a fifth route that the Result-10 table omits, and
the precise condition under which it threads the no-free-lunch.

**The fifth route — many-fingered time.** Replace evolution in a single time by the
Tomonaga–Schwinger functional evolution of a Schrödinger-functional state `ψ[Σ,φ]` over all
spacelike hypersurfaces `Σ`, with the *full* interacting Hamiltonian density (not the
interaction picture). This is manifestly covariant (no preferred `Σ`), real-time,
config-space-positive (`|ψ[Σ,φ]|²`), and carries a beable on each slice — formally all four
desiderata — and it **evades Haag** (full `H` in the interacting theory's own
Schrödinger-functional representation [Symanzik1981], not the free↔interacting intertwiner).
It is the construction Nikolić's covariant Bohmian QFT [Nikolic2006] targets.

**The wall — foliation-independent equivariance.** A beable theory requires the Born
distribution `|ψ[Σ]|²` to hold *on the beable*. Demanding it on every `Σ` simultaneously
over-determines a single 4D beable history `φ(x)` (the field value at a spacetime point,
shared by all slices through it): the marginals on crossing slices cannot all be Born for one
history except in special (free/Gaussian) cases. This is the standard, debated obstruction to
covariant Bohmian QFT.

**The ISP-specific lever.** Indivisibility commits only to single-slice Born marginals plus a
non-divisible within-foliation transition structure; it does *not* posit a consistent
trans-foliation (or even multi-time) joint history. The over-determination constrains a *joint
history*, which indivisibility does not require — so an indivisible process can, in principle,
carry Born marginals on every `Σ` without contradiction, where a Bohmian single trajectory
cannot.

**The precise enabling condition (and its cost).** This works iff one accepts a
**foliation-relative beable**: a field configuration defined on each slice, with no
foliation-independent value `φ(x)` at a spacetime point. If instead the beable is a 4D field
with point-values, the over-determination bites and the route collapses to the block-universe
(Euclidean) option. The foliation-relative reading is arguably the relativistically-natural one
(no absolute simultaneity ⇒ no absolute "configuration now"), but whether it is a coherent
ontology — and whether it still counts as "a beable" — is the new open question.

> **Result 11 [SYN/OPEN].** A fifth route to the residue exists that the Result-10 table
> omits: a many-fingered-time, Schrödinger-functional, *indivisible* process. It evades Haag
> (full `H`) and would thread the four-way no-free-lunch — *provided* a foliation-relative
> beable (single-slice configs with no trans-slice point-value) is a coherent ontology, which
> is exactly the condition under which indivisibility evades the equivariance over-determination
> that sinks covariant Bohmian QFT. So the residue sharpens to a precise, ISP-specific, open
> ontological question: *are foliation-relative indivisible beables coherent?* Two technical
> open issues remain even then: Tomonaga–Schwinger integrability against Schwinger-term
> anomalies in `[H(x),H(y)]`, and a rigorous construction. A structured advance, not a solution.

Honest caveat: every step here is [SYN/OPEN]. The fifth route, the
indivisibility-evades-over-determination claim, and the foliation-relative-beable ontology are
this paper's synthesis and conjecture, not theorems; the ontology may prove incoherent, and the
Tomonaga–Schwinger integrability anomaly may obstruct the construction outright. **[SYN/OPEN]**

### 10.10 Is the foliation-relative beable coherent? A positive case

We can now advance on the question Result 11 isolated. The verdict is a qualified **yes**:
the technical incoherence-candidates dissolve, and the residue is a single defensible
interpretive commitment, not a contradiction.

**Established precedent.** Aharonov and Albert [AharonovAlbert1980] proved that in
relativistic quantum theory the state is genuinely hypersurface-relative — *the covariance
resides exclusively in the experimental probabilities, not in the underlying states.* A
foliation-relative *description* is therefore already established as consistent.
Relativistic Bohmian mechanics likewise admits *an entire class of empirically equivalent
probability spaces, one for every foliation* [DurrEtAl2014]. The foliation-relative
indivisible beable is the beable-ontology analogue of these.

**The beable is `φ(x,n)`.** Slice-locality forces the beable to be a field value at each
point *relative to a local timelike direction* `n` (the slice normal), `φ(x,n)`, with a
foliation assigning `n(x)`. This is a coherent, manifestly covariant object and — unlike a
single-valued `φ(x)` — it is *not* over-determined: different foliations read off different
`n`-components, so the Born-on-every-slice constraint no longer collides.

**The technical incoherence-candidates dissolve via microcausality.**
- *Crossing/shared slices.* If `Σ₁,Σ₂` share a region `R`, the Born marginal on `R` is set
  by the local algebra `A(D(R))`, identical for both, so per-slice marginals agree on shared
  regions; slices agreeing near `x` give the same `φ(x,n)`.
- *Records and observer agreement.* A record/outcome is a *localized* field configuration,
  its value fixed by the local algebra, hence foliation-independent. Observers in relative
  motion agree on all records. Foliation-relativity is confined to the *unobservable global*
  structure — exactly as relativity confines frame-relativity to simultaneity.
- *Bell correlations.* The joint of two spacelike-separated outcomes is fixed by
  `A(A)∨A(B)`, foliation-independent and equal to QM's; the "which-caused-which" narrative is
  frame-relative, the correlation invariant. No contradiction (the program's Bell verdict, at
  the beable level).

**Indivisibility is what makes it work where Bohmian struggles.** A deterministic Bohmian
trajectory must *dynamically preserve* equivariance (`|ψ|²`) on each foliation — provable
cleanly only on a preferred foliation, which is why relativistic Bohmian tends to reintroduce
one [DurrEtAl2014]. The indivisible process has no determining trajectory; it *posits* the
Born marginal on each slice, with no preservation burden. Indivisibility removes precisely
the structure that forces Bohmian toward a preferred frame.

> **Result 12 [SYN/OPEN].** Foliation-relative indivisible beables are *tentatively coherent*.
> Every technical incoherence-candidate (crossing-slice consistency, record/observer
> agreement, Bell correlations) dissolves via microcausality: local facts are
> foliation-independent, only the global beable structure is foliation-relative — the same
> structure Aharonov–Albert established for relativistic states [AharonovAlbert1980] and
> relativistic Bohmian mechanics realizes as a per-foliation class [DurrEtAl2014].
> Indivisibility removes the equivariance-preservation burden that forces Bohmian toward a
> preferred foliation. What remains is not a contradiction but one explicit, defensible
> interpretive commitment — that the *beable* (reality), not merely the description, can be
> frame-relative — coherent by parallel to relativity's frame-relative simultaneity, but a
> genuine ontological postulate.

Honest caveats: (i) coherence by dissolution-of-objections plus established parallels, not a
from-scratch theorem — a subtler incoherence is not excluded; (ii) the leap from
Aharonov–Albert's frame-relative *state* to a frame-relative *beable* (reality) is the
substantive step, and the adequacy of frame-relative reality is a real debate, not settled
here; (iii) coherence of the ontology is separate from *existence* of the construction
(Result 11: Tomonaga–Schwinger integrability vs.\ Schwinger-term anomalies, plus a rigorous
build), which remains open. **[SYN/OPEN]**

### 10.11 The technical move: Tomonaga–Schwinger integrability and the Schwinger anomaly

The remaining outright-killer for the fifth route (Result 11) is whether the full-`H`
Tomonaga–Schwinger evolution `i δψ[Σ]/δσ(x) = 𝓗(x) ψ[Σ]` is *integrable* (path-independent in
the space of hypersurfaces) for an interacting field. The verdict is **favorable in the
semiclassical setting**: the anomaly that could obstruct it is a phase, and the beable is a
modulus.

**Distinct-point integrability holds by microcausality.** Path-independence requires
`[𝓗(x),𝓗(y)]` to be consistent for deformations at two points `x≠y` on a spacelike `Σ`. The
renormalized energy density `𝓗(x)=T⁰⁰(x)` is a local operator, and renormalized microcausality
gives `[𝓗(x),𝓗(y)]=0` for `x≠y` spacelike — for the *full* interacting density (the interacting
fields are local). So the distinct-point condition holds.

**The coincidence anomaly is a phase that cancels in the beable.** The deformation algebra
carries Schwinger terms supported at `x=y`: the classical part (`∝ T⁰ᵏ∂ₖδ`, the
tangential/momentum generator) is the correct hypersurface-deformation (Dirac) algebra and is
represented faithfully; the *anomalous* part is a **c-number** central extension (the
conformal/Schwinger anomaly, e.g. the 2D central charge). Two facts make it harmless for the
beable:
- for Hermitian `𝓗`, `[𝓗(x),𝓗(y)]` is anti-Hermitian, so its c-number part is *purely
  imaginary* — it enters the TS connection as a phase, not a norm change;
- being a c-number it is *field-configuration-independent*, so the cocycle is a global phase
  `e^{iα[Σ]}` on `ψ[Σ,φ]`.

Either way the anomaly **cancels in the Born-marginal beable** `|ψ[Σ,φ]|²`. The TS evolution of
the *state* may be path-dependent up to a phase, but the *beable distribution* is path-independent
and well-defined. Indivisibility helps again: the beable being a modulus is exactly what makes it
immune to the phase anomaly that complicates the state.

> **Result 13 [SYN/OPEN].** In the semiclassical (classical-metric) setting, the
> Tomonaga–Schwinger integrability worry does *not* kill the fifth route. Distinct-point
> integrability holds by renormalized microcausality (`[𝓗(x),𝓗(y)]=0`, `x≠y`); the
> coincidence-limit Schwinger anomaly is an anti-Hermitian c-number — a global phase cocycle on
> `ψ[Σ]` — which cancels in the Born-marginal beable `|ψ[Σ,φ]|²`. So the beable is integrable even
> when the state's phase is anomalous. Holds provided the `[𝓗,𝓗]` anomaly is c-number (no
> anomalous *operator* terms beyond the classical deformation algebra) — true for standard
> renormalizable QFT — and in the semiclassical setting; full dynamical-gravity constraint-algebra
> anomalies are out of scope.

Honest caveat: defusing this obstruction is *necessary, not sufficient*. A rigorous construction of
the covariant indivisible field process — gluing the per-foliation Barandes ISPs into one object with
consistent all-foliation Born marginals — remains undone; the operator-anomaly loophole must be
excluded for the specific theory; and a subtler obstruction is not ruled out. **[SYN/OPEN]**

### 10.12 Honest status

This converts open problem 1 from an aspiration into a well-posed problem with a
fifty-year literature, a known covariant structure (Euclidean–Markov), and a named
obstruction. The worked free-field testbed (§10.5) settles the easy case — relativistic
ISP *exists* for the free scalar field — but does so through Gaussianity, not
non-Markovianity, and so corrects the §10.4 reading and provides no evidence for the
interacting conjecture. Hudson's theorem sharpens the wall to a precise statement:
positive *phase-space* probability is Gaussian-only, so every interaction breaks the
easy route, and the surviving configuration-space route requires the unestablished
covariant real-time non-Markovian construction. So the honest status is: **necessary
and natural, not sufficient; the easy (free) case is solved trivially; the interacting
case is bounded by a theorem (Hudson) and remains open.** No one — Nelson,
Guerra–Ruggiero, or Barandes — has produced a covariant real-time genuine-probability
process for an *interacting* field. Working the residue directly (§10.9) does, however,
isolate a fifth route the no-free-lunch missed — a many-fingered-time indivisible process —
and reduces the whole problem to two residues, *both of which the subsequent analyses find
tentatively favorable rather than fatal*: (1) the interpretive question — *are
foliation-relative indivisible beables coherent?* — argued tentatively **yes** (Result 12:
the technical incoherence-candidates dissolve via microcausality; the residue is one explicit
ontological postulate, frame-relative reality, coherent by parallel to relativity's
simultaneity); and (2) the technical question — Tomonaga–Schwinger integrability — found
**not fatal** (Result 13: the Schwinger anomaly is an anti-Hermitian c-number, a global phase
that cancels in the Born-marginal beable). So neither identified killer kills the fifth route.
What is *not* done is the positive step: a rigorous construction gluing the per-foliation
Barandes ISPs into one covariant object with consistent all-foliation Born marginals. Defusing
the two obstructions is necessary, not sufficient; a subtler obstruction is not excluded; and
all of Results 11–13 are [SYN/OPEN], not theorems. Honest status: the binding problem is
reduced to a single well-posed construction, with both of its identified would-be-killers
tentatively cleared. Realistically a decade-scale problem in mathematical physics, now stated
correctly and with its obstruction map filled in. **[OPEN]**

## 11. Epistemic status and route to acceptance

This paper, like the program, offers RISP **no unique measurable prediction**: §3–§9 reproduce the
observables of QFT+GR, the one measurable deviation (the gravitational decoherence of V5-Paper-2) is
*non-relativistic* ISP shared with the collapse-model family, and the genuinely relativistic content
(the foliation-relative beable) is, by Result 12 and the unobservability argument, observationally
hidden. It is therefore worth stating plainly *why* the relativistic construction is worth pursuing,
and *how* such a theory could ever be accepted.

**The value is ontological unification, not unique prediction.** Ontologies are routinely adopted for
explanatory scope and unification rather than by crucial experiments — atomism before atoms were
resolved, the reality of fields, of spacetime curvature. RISP's claim is of that kind: *the coherent
relativistic ontology that a confirmed ISP would generalize to.* Its route to acceptance is
inference-to-the-best-explanation, not a RISP-specific test — a legitimate but non-empirical path,
which we name as such.

**Three conditions, one of them binding.**
1. **ISP must be empirically confirmed** — the optional non-unitary channel must exist, and the
   two-axis test (V5-Paper-2) must land in the ISP cell. Even then, what is confirmed is the *class*
   "non-Markovian gravitational objective-collapse"; selecting Barandes' ISP within it is itself a
   coherence judgement.
2. **RISP must exist as a constructed, coherent theory — the binding condition.** One cannot
   generalize a confirmed ISP *to* RISP if the covariant interacting beable dynamics (§10) is not
   built. This paper cleared that construction's would-be-killers (Results 11–13) but did not build
   it. So far from lowering the §10 burden, the acceptance route *rests* on it: no construction, no
   ontology to generalize to.
3. **RISP must win the ontology competition** — against other relativistic completions (Tumulka's
   relativistic flash GRW, Bohmian QFT, the spacetime-from-entanglement program), on coherence and
   naturalness, since these are roughly empirically equivalent. RISP's case is that indivisibility is
   the *confirmed* ISP feature and the foliation-relative beable its natural relativistic completion —
   an argument to be made, not an automatic victory.

**The historical caveat.** Confirmation of a *dynamics* underdetermines its *ontology*. Quantum
mechanics has been confirmed for a century and its ontology remains contested (Copenhagen, Bohm,
Everett, collapse, ISP all coexist); the luminiferous aether was the "natural" ontology for confirmed
wave optics and was wrong. So even a confirmed ISP may leave the relativistic ontology as unsettled
as QM's interpretation is today; predicting that RISP *would* be widely adopted is itself an overclaim.

**Honest route to acceptance (one line).** RISP is adopted, if at all, by *ontological unification* of
a confirmed ISP — contingent on (1) ISP confirmed, (2) RISP *constructed* (§10, the linchpin), and
(3) RISP winning on coherence against rival relativistic ontologies — none guaranteed, since confirmed
dynamics underdetermines ontology.

**Program priorities follow.** (i) Get ISP confirmed (the two-axis decoherence test, V5-Paper-2);
(ii) *build* RISP (complete the §10 construction — the linchpin); (iii) argue RISP's coherence against
rival relativistic ontologies. If all three hold, RISP could become the accepted QFT+GR ontology by
the unification route — and it should be presented as inference-to-the-best-explanation, named as
such, never as a crucial-experiment result. **[meta / epistemic]**

## 12. Conclusion

Non-conserved matter — of which the indivisible beable is one instance — can source
classical gravity relativistically once one adopts unimodular gravity: the
energy–momentum non-conservation that ordinarily obstructs the coupling is absorbed
into a dynamical cosmological term, and it splits into a mean part (dark-energy-like)
and a fluctuating part (gravitational decoherence). This unimodular sourcing is
Markovian-agnostic; making the *source itself* a genuinely relativistic indivisible
beable is the separate open problem of §10. The framework reduces, in the Newtonian limit, to the
Diósi–Penrose / Tilloy–Diósi physics and to the falsifiable Gaussian-onset
decoherence of V5-Paper-2. The conservation obstruction is therefore not fatal; the
binding open problem is the covariance of the beable dynamics, which most naturally
introduces an observationally hidden cosmic-rest-frame foliation, with a fully
covariant interacting beable ontology remaining to be constructed. Two of the
program's quantitative questions are now settled: the construction is a classical
channel, so it predicts a *negative* gravitationally-induced-entanglement (BMV)
result and would be falsified by a positive one; and the dynamical cosmological term,
while a genuine consequence of the unimodular mechanism, is quantitatively *excluded*
as dark energy for Diósi–Penrose-type sourcing, since the regularization length the
spontaneous-radiation experiments bound makes it many orders too small. The testable
content therefore lives in gravitational decoherence (Gaussian onset) and in the BMV
no-entanglement prediction; the cosmological term is a mechanism, not a dark-energy
solution.

---

## References

[Barandes2023a] J. A. Barandes, *The stochastic-quantum correspondence*, arXiv:2302.10778 (2023).

[Barandes2023b] J. A. Barandes, *The stochastic-quantum theorem*, arXiv:2309.03085 (2023).

[Barandes2025] J. A. Barandes, *Quantum systems as indivisible stochastic processes*, arXiv:2507.21192 (2025).

[Penrose1996] R. Penrose, *On gravity's role in quantum state reduction*, Gen. Relativ. Gravit. **28**, 581 (1996).

[Diosi1989] L. Diósi, *Models for universal reduction of macroscopic quantum fluctuations*, Phys. Rev. A **40**, 1165 (1989).

[TilloyDiosi2016] A. Tilloy and L. Diósi, *Sourcing semiclassical gravity from spontaneously localized quantum matter*, Phys. Rev. D **93**, 024026 (2016); arXiv:1509.08705.

[KTM2014] D. Kafri, J. M. Taylor, and G. J. Milburn, *A classical channel model for gravitational decoherence*, New J. Phys. **16**, 065020 (2014); arXiv:1401.0946.

[Discord2022] *Quantum correlations beyond entanglement in a classical-channel model of gravity*, arXiv:2205.15333 (2022). *(authors to verify)*

[Josset2017] T. Josset, A. Perez, and D. Sudarsky, *Dark energy from violation of energy conservation*, Phys. Rev. Lett. **118**, 021102 (2017); arXiv:1604.04183.

[Tumulka2006] R. Tumulka, *A relativistic version of the Ghirardi–Rimini–Weber model*, J. Stat. Phys. **125**, 821 (2006); arXiv:quant-ph/0406094.

[Tumulka2020] R. Tumulka, *A relativistic GRW flash process with interaction*, in *Do Wave Functions Jump?* (Springer, 2021), p. 321; arXiv:2002.00482 (2020).

[MassCoupled2020] *Mass-coupled relativistic spontaneous collapse models*, arXiv:2012.02627 (2020). *(authors to verify)*

[Gisin1989] N. Gisin, *Weinberg's non-linear quantum mechanics and supraluminal communications*, Phys. Lett. A **143**, 1 (1990). *(reference to verify)*

[Nelson1973] E. Nelson, *Construction of quantum fields from Markoff fields*, J. Funct. Anal. **12**, 97 (1973). *(reference to verify)*

[GuerraRuggiero1973] F. Guerra and P. Ruggiero, *New interpretation of the Euclidean–Markov field in the framework of physical Minkowski space-time*, Phys. Rev. Lett. **31**, 1022 (1973).

[Hudson1974] R. L. Hudson, *When is the Wigner quasi-probability density non-negative?*, Rep. Math. Phys. **6**, 249 (1974). *(reference to verify)*

[GlimmJaffe1987] J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View*, 2nd ed. (Springer, 1987).

[Coleman1975] S. Coleman, *Quantum sine-Gordon equation as the massive Thirring model*, Phys. Rev. D **11**, 2088 (1975). *(reference to verify)*

[StreaterWightman1964] R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964). [for Haag's theorem]

[Symanzik1981] K. Symanzik, *Schrödinger representation and Casimir effect in renormalizable quantum field theory*, Nucl. Phys. B **190**, 1 (1981). *(reference to verify)*

[Nikolic2006] H. Nikolić, *Covariant many-fingered time Bohmian interpretation of quantum field theory*, Phys. Lett. A **348**, 166 (2006); arXiv:hep-th/0501046.

[AharonovAlbert1980] Y. Aharonov and D. Z. Albert, *States and observables in relativistic quantum field theories*, Phys. Rev. D **21**, 3316 (1980); and *Can we make sense out of the measurement process in relativistic quantum mechanics?*, Phys. Rev. D **24**, 359 (1981).

[DurrEtAl2014] D. Dürr, S. Goldstein, T. Norsen, W. Struyve, and N. Zanghì, *Can Bohmian mechanics be made relativistic?*, Proc. R. Soc. A **470**, 20130699 (2014); arXiv:1307.1714. *(author list to verify)*

[FenyesNelsonCov] M. Davidson (attrib.), *Lorentz covariance of the generalized Fényes–Nelson stochastic model for the free scalar field*, arXiv:quant-ph/0211097. *(authors/details to verify)*

[HenneauxTeitelboim1989] M. Henneaux and C. Teitelboim, *The cosmological constant and general covariance*, Phys. Lett. B **222**, 195 (1989). *(reference to verify)*

[Unruh1989] W. G. Unruh, *Unimodular theory of canonical quantum gravity*, Phys. Rev. D **40**, 1048 (1989). *(reference to verify)*

[HuVerdaguer2008] B. L. Hu and E. Verdaguer, *Stochastic gravity: theory and applications*, Living Rev. Relativ. **11**, 3 (2008). *(reference to verify)*

[Bose2017] S. Bose et al., *Spin entanglement witness for quantum gravity*, Phys. Rev. Lett. **119**, 240401 (2017).

[Marletto2017] C. Marletto and V. Vedral, *Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity*, Phys. Rev. Lett. **119**, 240402 (2017).

[Donadi2021] S. Donadi et al., *Underground test of gravity-related wave function collapse*, Nat. Phys. **17**, 74 (2021).

[Bassi2013] A. Bassi, K. Lochan, S. Satin, T. P. Singh, and H. Ulbricht, *Models of wave-function collapse, underlying theories, and experimental tests*, Rev. Mod. Phys. **85**, 471 (2013).

[Trillo2025] D. Trillo and M. Navascués, *The Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement*, Phys. Rev. D **111**, L121101 (2025); arXiv:2411.02287.

[Collapse2025] *Collapse-based models for gravity do not violate the entanglement-based witness of non-classicality*, arXiv:2503.19774 (2025). *(authors to verify)*
