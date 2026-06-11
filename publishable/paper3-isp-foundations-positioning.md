# Indivisible stochastic processes among their neighbours: what the reformulation buys, what it costs, and where it can differ

Preprint, not peer reviewed, version 2026-06-02.

**Author:** Felix Robles Elvira

**Status:** Draft (markdown). Foundations-venue positioning paper.

---

## Abstract

The indivisible-stochastic-processes (ISP) reformulation of quantum mechanics [Barandes] recovers
the empirical content of quantum theory from a non-Markovian stochastic process over a definite
configuration space. Because it is operationally equivalent to standard quantum mechanics, its
value and its vulnerabilities are not settled by experiment in the usual way; they are settled by
how it sits among its neighbours — Nelson's stochastic mechanics, the de Broglie–Bohm theory, and
the dynamical-collapse models (GRW/CSL/Diósi–Penrose) — and by whether it survives the standard
objections that have shaped that landscape. This paper does that positioning. We argue that ISP is
the non-Markovian generalization of Nelson's diffusion (which it contains as the Markovian special
case); that it removes the equivariance burden that forces a preferred foliation in relativistic
Bohmian mechanics, at the cost of giving up a trans-temporal trajectory; that it is *unitary-
equivalent* to quantum mechanics and therefore distinct in kind from collapse models, which are
not; and that the Wallstrom quantization-condition objection — fatal to naive stochastic mechanics
— does not bite ISP in the same way, because ISP derives the wavefunction from a process built on a
given unitary system rather than positing a velocity potential. We then state plainly what the
reformulation does *not* give: the "category problem" — locality, tensor-product structure, energy,
symmetries — is extra data, not an automatic consequence of a transition matrix. Finally we
identify the single place ISP can empirically differ from quantum mechanics: an optional non-unitary
channel whose most accessible signature is a non-Markovian (Gaussian-onset) gravitational
decoherence, treated quantitatively in a companion paper. The contribution is scholarly placement
and an honest accounting, not new physics.

---

## 1. Introduction

A reformulation of quantum mechanics that reproduces all of its predictions cannot be argued for, or
against, by pointing at an experiment. It must be argued for by what it clarifies and by what it
costs, and against by the objections that have killed or constrained its predecessors. The
indivisible-stochastic-processes program [Barandes2023a, Barandes2023b] is such a reformulation:
its primitive is a stochastic process over a configuration space whose transition structure is
**indivisible** (non-divisible across intermediate times, hence non-Markovian), from which a
Hilbert space, unitary dynamics, and the Born rule are derived. The purpose of this paper is to
locate ISP precisely among its neighbours and to subject it to the standard objections, so that its
genuine content — and its single empirical lever — can be stated without inflation.

We make four positioning claims (Sections 3–6), state the limiting "category problem" honestly
(Section 7), and isolate the one empirical difference (Section 8).

---

## 2. The reformulation in one section

An indivisible stochastic process assigns, to a system with configuration space `C`, time-indexed
distributions and transition matrices `Γ(t,t')` that do **not** satisfy Chapman–Kolmogorov:

```math
\Gamma(t_2,t_0)\neq\Gamma(t_2,t_1)\,\Gamma(t_1,t_0).
```

Barandes' correspondence shows that the unistochastic processes of this class are in
correspondence with unitary quantum systems: writing `Γ_ij = |U_ij|²` for a unitary `U`
reconstructs the transition probabilities, the configurations are the definite beables, and the
wavefunction is a derived bookkeeping device for the non-Markovian memory. The empirical content is
that of quantum mechanics. Two features will matter below: the beable is **definite** (a config at
each time), and the memory is **non-Markovian** (the present does not screen the past).

---

## 3. ISP vs. Nelson: the non-Markovian generalization

Nelson's stochastic mechanics [Nelson1966] reconstructs the Schrödinger equation from a *Markovian*
diffusion — a forward/backward Itô process whose drift is fixed by a velocity potential. Its ground
process is exactly the Euclidean–Markov field reading of the vacuum [GuerraRuggiero1973]. ISP and
Nelson are often grouped together; they should be distinguished by one structural fact:

```math
\boxed{\text{Nelson's diffusion} \;=\; \text{the Markovian special case of the indivisible class.}}
```

Nelson posits a Markov process and recovers QM only with extra conditions; ISP allows the full
non-Markovian class, and the non-Markovianity is what carries the quantum phase information that
Nelson must encode in a drift. This is not a cosmetic difference: it is the same difference that
will (Section 5) decouple ISP from the Wallstrom objection, and (companion paper) generate ISP's
one empirical signature. The price is that ISP gives up the clean diffusion picture; the memory is
the physics.

---

## 4. ISP vs. Bohm: trading the trajectory for the marginal

The de Broglie–Bohm theory keeps a deterministic configuration trajectory guided by the
wavefunction, with the `|ψ|²` distribution preserved dynamically (equivariance). In the
non-relativistic theory this is unproblematic. Relativistically it is the locus of difficulty:
preserving equivariance on every spacelike slice clean*ly* requires a preferred foliation, and the
attempts to avoid one [DurrEtAl2014, Nikolic2006] are exactly where covariant Bohmian mechanics
struggles.

ISP makes a different trade. It does **not** carry a trans-temporal trajectory or an equivariance-
preservation burden; it posits Born *marginals* slice-by-slice and non-divisible transitions within
a foliation. This removes the structure that forces Bohm's preferred frame — at the cost of
denying a single joint history across times. The reformulations are empirically identical
non-relativistically; the difference is ontological and becomes a *relativistic* difference (treated
in the companion obstruction-map paper). The honest summary: ISP buys freedom from the equivariance
burden by giving up the trajectory; whether that freedom is coherent at the relativistic level is an
open ontological question, not a settled advantage.

---

## 5. ISP vs. collapse models: a reformulation, not a modification

GRW, CSL, and Diósi–Penrose [GRW1986, GPR1990, Diosi1989, Penrose1996] *modify* quantum mechanics:
they add a stochastic non-unitary term that localizes the wavefunction, breaking unitarity and
predicting deviations (spontaneous localization, heating, spontaneous radiation). ISP, by contrast,
is *unitary-equivalent* to quantum mechanics: in its faithful form it adds nothing and predicts
nothing new. This is a difference in kind, and it cuts both ways:

- It makes ISP safe from the experimental bounds that constrain and (parameter-free) exclude DP/CSL
  [Donadi2020] — the faithful theory has no free parameters to bound.
- It also means ISP, *as a faithful reformulation*, makes **no** new prediction. Any empirical
  difference must come from an *optional* added channel (Section 8), at which point ISP enters the
  collapse-model family's territory and inherits its constraints.

So ISP is not a rival *to* collapse models in the faithful regime; it is a rival *interpretation*
that becomes a rival *theory* only when the optional channel is switched on.

---

## 6. The Wallstrom objection

The decisive objection to stochastic-mechanics reconstructions is Wallstrom's [Wallstrom1994]: a
real diffusion with a velocity potential reproduces the Schrödinger equation only if one *imposes*
the quantization condition `∮∇S·dl = 2πnℏ` (single-valuedness of the wavefunction), which does not
follow from the stochastic dynamics and must be added by hand — and without which the reconstruction
yields too many solutions. This sinks naive Nelson-type programs unless supplemented.

ISP's relationship to Wallstrom is different, and this is a load-bearing point for the program's
credibility:

```math
\boxed{
\begin{array}{l}
\text{ISP does not posit a velocity potential and then seek a wavefunction.}\\
\text{It builds the process from a given unitary } U \text{; the single-valued, properly}\\
\text{quantized wavefunction is an input to the correspondence, not an output that}\\
\text{must be constrained after the fact.}
\end{array}}
```

In other words, the quantization condition that Wallstrom must impose on a diffusion is, in ISP,
already encoded in the unitarity of the `U` from which `Γ=|U|²` is built. ISP therefore does not
face Wallstrom's problem in its original form. The honest residue: this shifts the question rather
than dissolving it — *which* indivisible processes correspond to *physically admissible*
(local-Hamiltonian, single-valued) unitary systems is itself a constraint, and stating that
constraint intrinsically at the process level (without importing the answer from `U`) is not fully
worked out. We flag this as the program's analogue of Wallstrom, in a milder form: not "too many
solutions," but "the admissible subclass is currently characterized by reference to `U`, not
intrinsically."

---

## 7. The category problem: what reformulation does *not* deliver

A transition matrix is not by itself physics. The structures that make a quantum theory *physical*
— a tensor-product decomposition into subsystems, a notion of locality, a Hamiltonian and hence
energy, symmetry groups, and a measurement interface — are **extra data**, not automatic
consequences of `Γ` or of the dilation to a Hilbert space. This is the program's own "category
problem," and it must be stated rather than glossed:

- A freely enlarged Hilbert-space dilation can make almost any process "unitary"; the physically
  meaningful claim requires a *local, covariant, natural* dilation, not merely *some* dilation.
- Locality and subsystem structure are imposed by choosing how `C` factorizes, not derived.
- Dynamical symmetries at the `Γ` level can be far weaker than symmetries of a Hamiltonian or a
  local field theory.

Acknowledging this is what keeps the reformulation honest: ISP reorganizes the kinematics of
quantum theory around a definite beable and non-Markovian memory; it does not *derive* the
locality/energy/symmetry scaffolding, which is supplied alongside.

---

## 8. The one empirical lever

If the faithful reformulation predicts exactly quantum mechanics, where can ISP ever be tested?
Only through an *optional* departure from unitarity. The most principled and most accessible such
departure is in **gravitational decoherence**: dropping the divisibility (Markov) assumption that
silently underlies the Diósi–Penrose exponential decay law, indivisibility yields a *non-Markovian*
decoherence functional whose onset is **Gaussian**,

```math
C(T)=\exp\!\Big[-\tfrac12\,(T/\tau_G)^2\Big],\qquad \tau_G=\hbar/E_G,
```

rather than exponential, at the same Diósi–Penrose scale `E_G`. The fit-free signature is the
*onset shape* (a quadratic, zero-initial-slope plateau vs. a finite-slope exponential), and a
second axis — whether the rate scales with the gravitational self-energy `E_G` — separates it from
the non-gravitational collapse models. This is developed quantitatively in the companion paper. Two
honest qualifiers belong here: the signature requires the optional channel to exist at all (if
nature is exactly unitary, there is nothing to see), and a non-Markovian onset is shared with the
broader collapse/decoherence family — it identifies the *class*, with ISP selected within it on the
grounds of this paper, not fingerprinted uniquely.

---

## 9. Conclusion

Placed among its neighbours, ISP is the non-Markovian generalization of Nelson's diffusion; it
trades Bohm's trajectory and equivariance burden for slice-wise Born marginals; it is unitary-
equivalent to quantum mechanics and so distinct in kind from collapse models; and it escapes
Wallstrom's objection in its original form, while inheriting a milder intrinsic-characterization
residue. It does not solve the category problem — locality, energy, and symmetry are supplied, not
derived — and as a faithful reformulation it predicts nothing new, with its single empirical lever
confined to an optional, collapse-family-shared gravitational-decoherence channel. The reformulation
is, on this accounting, a genuine and clarifying reorganization of quantum kinematics with one
testable consequence — neither more nor less. Stating it at that level is what allows the testable
consequence to be taken seriously.

---

## References

- [Barandes2023a] J. A. Barandes, *The Stochastic-Quantum Correspondence*, arXiv:2302.10778.
- [Barandes2023b] J. A. Barandes, *Quantum Theory as a Theory of Indivisible Stochastic Processes*, arXiv:2309.03085.
- [Nelson1966] E. Nelson, *Derivation of the Schrödinger Equation from Newtonian Mechanics*, Phys. Rev. **150**, 1079 (1966).
- [GuerraRuggiero1973] F. Guerra and P. Ruggiero, Phys. Rev. Lett. **31**, 1022 (1973).
- [DurrEtAl2014] D. Dürr, S. Goldstein, T. Norsen, W. Struyve, N. Zanghì, Proc. R. Soc. A **470**, 20130699 (2014); arXiv:1307.1714.
- [Nikolic2006] H. Nikolić, Phys. Lett. A **348**, 166 (2006); hep-th/0501046.
- [GRW1986] G. C. Ghirardi, A. Rimini, T. Weber, *Unified dynamics for microscopic and macroscopic systems*, Phys. Rev. D **34**, 470 (1986).
- [GPR1990] G. C. Ghirardi, P. Pearle, A. Rimini, *Markov processes in Hilbert space and continuous spontaneous localization of systems of identical particles*, Phys. Rev. A **42**, 78 (1990).
- [Diosi1989] L. Diósi, *Models for universal reduction of macroscopic quantum fluctuations*, Phys. Rev. A **40**, 1165 (1989).
- [Penrose1996] R. Penrose, *On gravity's role in quantum state reduction*, Gen. Rel. Grav. **28**, 581 (1996).
- [Donadi2020] S. Donadi et al., *Underground test of gravity-related wave function collapse*, Nat. Phys. **17**, 74 (2021).
- [Wallstrom1994] T. C. Wallstrom, *Inequivalence between the Schrödinger equation and the Madelung hydrodynamic equations*, Phys. Rev. A **49**, 1613 (1994).

*Reference volume/page/arXiv details to be re-verified against primary sources before submission.*
