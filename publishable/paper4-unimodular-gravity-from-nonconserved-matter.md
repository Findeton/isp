# Sourcing classical gravity from non-conserved matter: unimodular gravity, a dynamical cosmological term, and why its magnitude is bounded out

**Author:** Felix Robles Elvira

**Status:** Draft (markdown). PRD / CQG-style paper. Markovian-agnostic: the result holds for any
matter that fails to conserve stress–energy (objective-collapse models, beable ontologies); ISP is
named as one instance, not as a premise.

---

## Abstract

Any matter model that localizes or reduces quantum states — dynamical-collapse theories
(GRW/CSL/Diósi–Penrose) and beable ontologies among them — generically fails to conserve the
expected stress–energy tensor, `∇^μ⟨T_μν⟩ = η_ν ≠ 0`. Coupled naively to general relativity this is
inconsistent: the contracted Bianchi identity `∇^μ G_μν ≡ 0` forces conservation. We show that
**unimodular gravity** (UG) removes the inconsistency without new fields: its trace-free Einstein
equations do not impose conservation, and the non-conservation is rerouted into a *dynamical
cosmological term*, `∇_ν Λ = 8πG η_ν`. Splitting `η_ν` into a homogeneous mean and a fluctuation
gives two faces of the same non-conservation: the mean drives `Λ(t)` (a dark-energy–like term),
the fluctuation drives metric noise and hence gravitational decoherence (the subject of a companion
paper). We then report two clean **negative** results that constrain the construction sharply.
First, the magnitude: for Diósi–Penrose–scale injection with the experimentally allowed
regularization length, the sourced energy density is **12–16 orders of magnitude too small** to be
dark energy, and reaching the observed value would require a regularization length already excluded
by spontaneous-radiation bounds — so the same bound that constrains decoherence forecloses the
dark-energy magnitude. Second, the construction provides **no dark matter**: it is a dynamics, not
a matter content; it gives no extra mean attraction and no modified-gravity (MOND) behaviour, and
any novel sector is bounded out by the same limit and carries the wrong equation of state. The one
clean *positive* falsifiable consequence is that the gravity here is a classical channel, which by
the Kafri–Taylor–Milburn theorem predicts **no gravitationally induced entanglement** (a negative
BMV outcome) together with mandatory decoherence; a positive BMV result falsifies it.

---

## 1. Introduction

Semiclassical and post-quantum gravity must eventually say how matter that does *not* evolve
unitarily couples to spacetime. Objective-collapse models add a stochastic non-unitary term to the
Schrödinger equation [GRW1986, GPR1990, Diosi1989, Penrose1996]; beable reformulations posit a
definite configuration whose dynamics may inject energy. In every such case the expected
stress–energy is not conserved,

```math
\nabla^\mu\langle T_{\mu\nu}\rangle = \eta_\nu \neq 0,
```

and the standard coupling to general relativity becomes inconsistent, because the Einstein tensor
is identically conserved. This paper makes three points: (i) **unimodular gravity** evades the
inconsistency and converts the non-conservation into a dynamical cosmological term; (ii) the
cosmological consequence, though real as a *mechanism*, is **excluded in magnitude** as dark
energy; and (iii) the construction yields **no dark matter**. The one surviving positive prediction
is a negative-BMV / mandatory-decoherence signature characteristic of a classical gravitational
channel. The argument uses only non-conservation; it is **Markovian-agnostic** and applies to
collapse models and beable ontologies alike, with ISP as one instance.

---

## 2. The obstruction

In general relativity the field equation `G_μν = 8πG T_μν` together with the
contracted Bianchi identity gives

```math
\nabla^\mu G_{\mu\nu}\equiv 0 \;\Longrightarrow\; \nabla^\mu T_{\mu\nu}=0.
```

Conservation is not an assumption one may relax inside GR; it is forced by the geometry. Matter
that injects energy (`η_ν≠0`) therefore cannot source the Einstein equations consistently. This is
the obstruction every non-unitary matter model meets at the gravitational interface.

---

## 3. Unimodular gravity evades it

Unimodular gravity [Anderson1971, Henneaux1989, Unruh1989] fixes the determinant `√(−g)` and varies
only the trace-free part of the metric. Its field equations are the **trace-free** Einstein
equations,

```math
R_{\mu\nu}-\tfrac14 g_{\mu\nu}R \;=\; 8\pi G\Big(T_{\mu\nu}-\tfrac14 g_{\mu\nu}T\Big),
```

which do **not** carry the contracted Bianchi identity as a conservation constraint on `T`. Taking
the divergence and using Bianchi on the geometric side yields, instead,

```math
\tfrac14\,\nabla_\nu\big(R+8\pi G\,T\big)=8\pi G\,\nabla^\mu T_{\mu\nu}=8\pi G\,\eta_\nu,
```

i.e. the non-conservation is absorbed into the gradient of a scalar that plays the role of a
cosmological term:

```math
\boxed{\;\nabla_\nu \Lambda \;=\; 8\pi G\,\eta_\nu\;.}
```

When `η_ν=0` this returns `Λ = const` and the theory is GR with a cosmological constant
(Λ as an integration constant). When `η_ν≠0`, **Λ becomes dynamical, sourced by the
non-conservation** — the Josset–Perez–Sudarsky mechanism [JPS2017]. No new fields are introduced;
the cosmological term is the bookkeeping device for energy the matter sector does not conserve.

---

## 4. Two faces of the non-conservation

Split `η_ν` into a homogeneous, isotropic mean (in the cosmic rest frame) and a fluctuation:

```math
\eta_\nu = \bar\eta_\nu + \delta\eta_\nu .
```

- **Mean → dark-energy–like term.** A curl-free homogeneous `η̄_ν` integrates to
  `Λ(t) = Λ₀ + 8πG ∫ w̄ dt`, a slowly varying cosmological term. (This is the mechanism
  level only; the magnitude is settled negatively in Section 6.)
- **Fluctuation → metric noise → decoherence.** The non-curl-free `δη_ν` sources a
  stochastic metric (an Einstein–Langevin equation [HuVerdaguer2008]), which decoheres matter
  superpositions. In the Newtonian limit this reduces to the Tilloy–Diósi gravitationally induced
  decoherence [TilloyDiosi2016], the quantitative subject of the companion decoherence paper.

So a single quantity — the matter sector's failure to conserve stress–energy — appears as **both**
a cosmological term and a gravitational-decoherence channel. That unification is the conceptual
content of the construction.

---

## 5. A clean positive prediction: negative BMV + mandatory decoherence

In this construction gravity sees the **definite/decohered** matter configuration, not the coherent
wavefunction — a *classical channel*. By the Kafri–Taylor–Milburn theorem [KTM2014] a classical
gravitational channel (equivalently, Diósi's model) **cannot create entanglement** between two
masses and necessarily induces a complementary decoherence. Hence the construction predicts a
**negative** result for the Bose–Marletto–Vedral gravitationally induced entanglement experiment
[Bose2017, MarlettoVedral2017], together with mandatory decoherence. This is falsifiable: a
*positive* BMV detection of gravitationally induced entanglement would rule the construction out.

The recent dispute over whether collapse/classical gravity entangles [TrilloNavascues2024] is a
matter of model definition — a quantum two-body Newtonian potential entangles, a genuine classical
channel does not — and the construction here is unambiguously the classical-channel case by
ontology. (A classical channel still produces quantum discord, but BMV witnesses entanglement, so
the negative prediction stands.)

---

## 6. Negative result I: the magnitude is not dark energy

Take the injection scale from the Diósi–Penrose regularization. Per nucleon,

```math
\frac{dE}{dt}\sim \frac{3}{2}\,\frac{\hbar G m_N}{R_0^{3}},
```

with `R₀` the regularization length. The spontaneous-radiation bound [Donadi2020] requires
`R₀ ≳ 0.5–4` Å, giving `dE/dt ~ 10⁻⁴¹–10⁻⁴³` W and a sourced density
`w̄ ~ 10⁻⁴²–10⁻⁴⁴` J m⁻³ s⁻¹, against the `~1.5×10⁻²⁷` J m⁻³ s⁻¹
needed to build the observed dark-energy density over a Hubble time:

```math
\boxed{\;\text{DP-scale sourcing is }10^{12}\text{--}10^{16}\text{ times too small to be dark energy.}\;}
```

Reaching the observed `ρ_Λ` would require `R₀ ~ 10⁻¹⁵` m (fm scale), which is excluded by the
same spontaneous-radiation bound by roughly five orders of magnitude. **The bound that constrains
the decoherence channel also forecloses the dark-energy magnitude.** The mechanism (Section 4) is
real; the DP-scale magnitude is excluded.

---

## 7. Negative result II: no dark matter

The construction provides no dark-matter candidate, for independent reasons:

- **It is a dynamics, not a content.** Dark matter is a missing-mass (content) problem; a
  modification of how matter sources gravity does not add mass.
- **No extra mean attraction.** To linear order `⟨g(T[q])⟩=g(⟨T⟩)`: the beable/collapse sourcing
  reproduces the Newtonian field of the mean stress–energy at galactic scales, with no MOND-like
  modification.
- **Bounded out and wrong equation of state.** Any novel sourced sector is limited by the same
  `R₀` bound to `≳12` orders below `ρ_Λ` (hence far below `ρ_DM ~ 2ρ_Λ`), and carries
  the wrong equation of state (heating `w>0`, or metric-noise `w ≈ 1/3`, versus pressureless
  `w ≈ 0`).
- **Lensing.** The Bullet-Cluster separation of mass from baryons rules out the modified-gravity
  route generally.

So the construction addresses **neither** dark-sector component; both remain content/cosmological
problems outside its scope.

---

## 8. Scope and what is Markovian-agnostic

Every step above uses only `∇^μ T_μν = η_ν ≠ 0`. It does **not** use indivisibility, non-Markovianity,
or any ISP-specific structure: the UG evasion, the dynamical `Λ`, the mean/fluctuation split, and
both negative results hold for *any* non-conserving matter — GRW, CSL, DP, or a beable ontology.
ISP enters only as one instance whose non-conservation arises from an optional non-unitary channel,
and whose Newtonian-limit decoherence (Section 4) acquires the non-Markovian onset analyzed in the
companion paper. The treatment here is **semiclassical**: gravity is classical and sourced; the
full quantum-gravitational constraint algebra is out of scope.

---

## 9. Conclusion

Unimodular gravity lets non-conserving matter source classical gravity consistently, rerouting the
energy it fails to conserve into a dynamical cosmological term — a single mechanism that surfaces as
both a dark-energy–like `Λ(t)` and a gravitational-decoherence channel. The construction makes one
clean, falsifiable positive prediction (negative BMV with mandatory decoherence, from the classical
channel) and two clean negatives (the Diósi–Penrose magnitude is 12–16 orders too small to be dark
energy and is foreclosed by the spontaneous-radiation bound; there is no dark-matter candidate).
The honest balance is a consistent coupling and a definite falsification target, with the
cosmological ambitions bounded out rather than realized — which is itself a useful constraint on the
whole class of non-unitary matter models at the gravitational interface.

---

## References

- [GRW1986] G. C. Ghirardi, A. Rimini, T. Weber, Phys. Rev. D **34**, 470 (1986).
- [GPR1990] G. C. Ghirardi, P. Pearle, A. Rimini, Phys. Rev. A **42**, 78 (1990).
- [Diosi1989] L. Diósi, Phys. Rev. A **40**, 1165 (1989).
- [Penrose1996] R. Penrose, Gen. Rel. Grav. **28**, 581 (1996).
- [Anderson1971] J. L. Anderson, D. Finkelstein, Am. J. Phys. **39**, 901 (1971).
- [Henneaux1989] M. Henneaux, C. Teitelboim, *The cosmological constant and general covariance*, Phys. Lett. B **222**, 195 (1989).
- [Unruh1989] W. G. Unruh, *Unimodular theory of canonical quantum gravity*, Phys. Rev. D **40**, 1048 (1989).
- [JPS2017] T. Josset, A. Perez, D. Sudarsky, *Dark energy from violation of energy conservation*, Phys. Rev. Lett. **118**, 021102 (2017).
- [HuVerdaguer2008] B. L. Hu, E. Verdaguer, *Stochastic gravity: theory and applications*, Living Rev. Relativity **11**, 3 (2008).
- [TilloyDiosi2016] A. Tilloy, L. Diósi, *Sourcing semiclassical gravity from spontaneously localized quantum matter*, Phys. Rev. D **93**, 024026 (2016).
- [KTM2014] D. Kafri, J. M. Taylor, G. J. Milburn, *A classical channel model for gravitational decoherence*, New J. Phys. **16**, 065020 (2014).
- [Bose2017] S. Bose et al., *Spin entanglement witness for quantum gravity*, Phys. Rev. Lett. **119**, 240401 (2017).
- [MarlettoVedral2017] C. Marletto, V. Vedral, *Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity*, Phys. Rev. Lett. **119**, 240402 (2017).
- [TrilloNavascues2024] D. Trillo, M. Navascués, arXiv:2411.02287.
- [Donadi2020] S. Donadi et al., *Underground test of gravity-related wave function collapse*, Nat. Phys. **17**, 74 (2021).

*Reference volume/page/arXiv details to be re-verified against primary sources before submission.*
