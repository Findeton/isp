# The hypersurface-deformation obstruction to a relativistic indivisible reconstruction of field theory and geometry

**Author:** Felix Robles Elvira

**Status:** Draft (markdown). Foundations-venue obstruction-map paper. This is a map of two *open* reconstruction problems unified by a single obstruction — it is explicitly **not** a reconstruction result.

---

## Abstract

Barandes' indivisible stochastic processes (ISP) reformulate non-relativistic quantum
mechanics as a class of non-Markovian stochastic processes over a definite configuration
space, with the wavefunction derived rather than postulated. A natural question is whether the
same reformulation extends to relativistic physics — to interacting quantum field theory (QFT)
and to the geometry of general relativity (GR). We do **not** answer that question. Instead we
map the obstruction, and we report a structural finding: the binding obstruction is *the same*
in both cases. Reconstructing interacting QFT from an indivisible process and reconstructing
effective-GR kinematics from a finite-record "stochastic-curvature" process both reduce to one
problem — the **foliation-independent representation of the hypersurface-deformation (Dirac–
Schwinger) algebra on a frame-dependent, indivisible stochastic substrate**. We show that the
candidate would-be-killers of the field-theory branch (energy non-conservation, Wigner
negativity, Haag's theorem, Tomonaga–Schwinger integrability) are each clearable, leaving a
single residue, and that indivisibility — the absence of a required trans-foliation joint
history — is the one lever that distinguishes this residue from the analogous obstruction that
blocks covariant Bohmian field theory. We then show that the geometry branch reduces to the
*same* covariance residue **plus** two obstructions the field-theory branch does not carry: the
non-derivation of the Einstein coupling (dynamics, as opposed to kinematics) and a methodological
circularity in its admissibility gates. We separate these explicitly. Neither branch is solved.
The contribution is a sharp, honest localization of a fifty-year-old problem and the
identification of one genuinely ISP-specific angle on it.

**What this paper does not claim:** it does not reconstruct interacting QFT; it does not derive
GR; it does not claim that the residue is dischargeable. The gravity-*sourcing* problem (how
beable matter couples to a classical metric) is a different question, treated in a companion
paper and excluded here.

---

## 1. Introduction

The indivisible-stochastic-processes (ISP) program [Barandes2023a, Barandes2023b, Barandes2025]
reformulates ordinary quantum mechanics without a fundamental wavefunction: the primitive object
is a stochastic process over a configuration space that is **indivisible** — its transition
structure does not factorize across intermediate times,

```math
\Gamma(t_2,t_0)\;\neq\;\Gamma(t_2,t_1)\,\Gamma(t_1,t_0),
```

so the Chapman–Kolmogorov equation fails and the process is genuinely non-Markovian. From such a
process one *derives* a Hilbert space, a unitary group, and the Born rule; conversely every
unitary quantum system of the relevant class arises from such a process. At the level of
non-relativistic quantum mechanics the reformulation is operationally complete.

It is tempting to conclude that the program therefore "reconstructs" quantum field theory and,
through a suitable geometric reading, general relativity. It does not — at least not yet, and not
in the literature, including Barandes' own work, which remains non-relativistic configuration-
space quantum mechanics. The honest situation is that two relativistic reconstruction problems
are **open**:

- **(QFT)** Is there a Lorentz-covariant, real-time, genuine-probability indivisible process over
  *field* configurations that reconstructs an interacting quantum field theory?
- **(GR)** Can the finite-record "stochastic-curvature" data of such a process reproduce the
  kinematics and dynamics of general relativity?

This paper is a map of these two obstructions. Its one substantive thesis is that they are
**the same obstruction**, seen from two sides, and that this shared obstruction is the
foliation-independent representation of the hypersurface-deformation algebra on an indivisible
substrate. We make the field-theory branch's residue sharp by clearing its apparent killers, we
make the geometry branch's *extra* residues explicit so the two are not conflated, and we name
the one ISP-specific lever. We claim no solution.

Throughout, results we have established elsewhere [RE-curvature, RE-descent] are restated and
cited; the contribution here is the unification and the honest residue separation.

---

## 2. The shared object: the hypersurface-deformation algebra

A relativistic theory has no preferred time. Its dynamics is the statement that evolving the
state from one spacelike Cauchy surface `Σ` to another can be decomposed into local deformations
of the surface, and that the result is independent of the intermediate foliation. The generators
of these deformations — the Hamiltonian density `𝓗(x)` (normal deformations) and the momentum
density `𝓗_k(x)` (tangential deformations) — close under the **hypersurface-deformation (Dirac–
Schwinger) algebra** [Dirac1958, Schwinger1962, HKT1976]:

```math
[\,\mathcal H(x),\mathcal H(y)\,] = \big(\mathcal H^k(x)+\mathcal H^k(y)\big)\,\partial_k\delta(x-y),
\qquad
[\,\mathcal H(x),\mathcal H^k(y)\,]=\dots,\qquad
[\,\mathcal H^k(x),\mathcal H^l(y)\,]=\dots
```

Two facts make this algebra the centre of gravity for the present paper.

1. **It is the integrability condition for foliation-independent evolution.** A many-fingered-time
   (Tomonaga–Schwinger) evolution `ψ[Σ]` is path-independent — i.e. defines a relativistic theory
   rather than a frame-bound one — precisely when this algebra is faithfully represented.

2. **It is what a "stochastic curvature" computes.** In the finite-record / ISP setting the
   leading exchange-defect of localized comparison maps converges, in the simplest free case, to
   a tangential operator that is *a stochastic analogue of the hypersurface-deformation curvature*
   [RE-curvature]. The geometric content of the program lives on this algebra.

So both the field-theory question (can the algebra be represented foliation-independently by an
indivisible process?) and the geometry question (can the algebra's stochastic-curvature
realization be promoted to covariant dynamics?) are questions *about the same algebra*. This is
not a metaphor; it is the technical reason the two branches share a residue (Sections 4–6).

---

## 3. What is already settled (and what that does and does not buy)

Before the obstruction, the established footholds — none of which is new physics:

- **Non-relativistic QM is an ISP** [Barandes2023a]. Table-stakes for any reconstruction; every
  serious interpretation reproduces QM.
- **The free relativistic field is an ISP**. The Euclidean–Markov field equals the ground-state
  Nelson diffusion [Nelson1966, Nelson1973, GuerraRuggiero1973]; the Gaussian vacuum has a
  positive Wigner functional [Hudson1974], so a genuine phase-space probability exists. Both are
  fifty-year-old facts and both are *Gaussian-trivial*: they do not exercise non-Markovianity.
- **The free 1+1D stochastic-curvature theorem** [RE-curvature]: the finite exchange-defect
  algebra contains a stochastic analogue of the hypersurface-deformation curvature in the free
  one-particle lattice-Dirac setting. Genuine, but explicitly *not* a field theory, not gauge
  coupling, not interacting, not gravity (the theorem says so in its own non-claims).

The interacting and geometric cases — where the content is — are the open ones.

---

## 4. Branch 1 — the field-theory reconstruction: one residue

### 4.1 The goal

A Lorentz-covariant, real-time, genuine-probability indivisible process over field configurations
reconstructing an *interacting* QFT. Equivalently: a relativistic stochastic mechanics for fields
with honest probabilities (not complex weights, not a fictitious diffusion time).

### 4.2 Four would-be-killers, each clearable

A reconstruction of this kind appears to be blocked at four points. We argue each is not fatal.

**(K1) Energy non-conservation / the Bianchi obstruction.** If a beable injects energy, then
`∇^μ T_μν = η_ν ≠ 0`, which is inconsistent with `∇^μ G_μν ≡ 0`. *Cleared:* this concerns coupling
to gravity, not the field reconstruction itself; and where it does arise it is evaded by
unimodular gravity (companion paper). The faithful reconstruction is unitary and conserves energy.

**(K2) Wigner negativity.** Hudson's theorem [Hudson1974] says a positive Wigner function forces
Gaussianity, so any interaction makes the phase-space route fail. *Cleared:* Barandes'
construction is **configuration-space**, not phase-space; `|Ψ[φ]|²` stays positive for interacting
fields, with the negativity carried by the non-Markovian transition structure, not by a signed
"probability." Hudson obstructs the phase-space route, not the config-space ISP.

**(K3) Haag's theorem.** There is no unitary intertwiner between free and interacting fields, so
the interaction picture does not exist. *Cleared:* Haag forbids the interaction picture, not the
interacting theory, which exists Poincaré-covariantly in its own representation; and the
configuration-space representation ISP needs — the **Schrödinger functional** `Ψ[φ]` with the full
interacting Hamiltonian — exists and is renormalizable [Symanzik1981]. Barandes' construction
applies there. Haag merely closes the *bridge* from the solved distinguishable-particle case
[Tumulka2006, Tumulka2020] to the field case, explaining why that construction does not transfer.

**(K4) Tomonaga–Schwinger integrability.** Is full-`H` many-fingered evolution path-independent
for interacting fields? *Cleared for the beable:* at distinct points `[𝓗(x),𝓗(y)]=0` by
renormalized microcausality; the coincidence (Schwinger) anomaly is a c-number central extension,
hence — for Hermitian `𝓗` — a pure imaginary phase that is *field-configuration-independent* and
therefore **cancels in the Born-marginal beable** `|ψ[Σ,φ]|²`. The state's phase may be
path-dependent; the beable distribution is not. (Caveat: holds when the anomaly is a c-number,
i.e. for standard renormalizable QFT; an operator anomaly would be a genuine loophole.)

### 4.3 The residue and the lever

What survives all four is a single residue:

```math
\boxed{\;\text{the foliation-independent (manifestly covariant) representation of the}
\;\text{interacting-field config-space indivisible process.}\;}
```

Barandes' construction yields such a process **in a frame**, given a Hilbert space and `U(t)`;
the residue is purely promoting it to be foliation-independent. The obstacle is *equivariance
over-determination*: demanding the Born marginal `|ψ[Σ]|²` on *every* `Σ` over-determines a single
4D beable history — the standard wall that sinks covariant Bohmian field theory [Nikolic2006,
DurrEtAl2014].

The ISP-specific lever: indivisibility commits only to single-slice Born *marginals* and to
non-divisible *within-foliation* transitions — **not** to a trans-foliation joint history. A
single Bohmian trajectory cannot carry Born marginals on all `Σ` at once; an indivisible process,
having no required joint history, *can* — provided one accepts a **foliation-relative beable**
(field values relative to a local timelike normal, `φ(x,n)`, with no foliation-independent
point-value). That this beable is *coherent* is argued by parallel to the hypersurface-relativity
of relativistic quantum states [AharonovAlbert1980, AharonovAlbert1981]; it is, however, a genuine
ontological postulate, not a theorem. **Status: OPEN; one residue; one lever; one postulate.**

---

## 5. Branch 2 — the geometry reconstruction: the same residue, plus two more

### 5.1 What is proven (kinematics, conditionally)

The free stochastic-curvature theorem (Section 3) is promoted, in [RE-descent], to a *conditional*
reconstruction of effective-GR **kinematics**: under a stack of admissibility hypotheses
(metric-coefficient fixing, a finite Levi-Civita transport, a pre-fixed geodesic law, a
divergence-admissible matter complex), the finite-record data satisfy effective metric, transport,
and free-fall gates. This is real, and it is *conditional and kinematic* — its own statement
declines to claim "Lorentzian signature, a Levi-Civita transport, or Einstein dynamics" as
automatic.

### 5.2 The three residues — separated

The geometry branch reduces to the field-theory residue **plus** two obstructions the field-theory
branch does not have. Keeping them separate is what prevents the false impression that GR is "as
close" as QFT.

- **(R-a) The shared covariance residue.** The finite-record "covariance" used so far is, on a
  finite configuration set, a relabeling (a permutation), not a boost; continuum Lorentz covariance
  is a separate, unproven theorem. *This is exactly the Branch-1 residue* (Section 4.3): a
  foliation-independent representation of the (here, stochastic-curvature) hypersurface-deformation
  algebra. Branch 1 and Branch 2 meet here.

- **(R-b) Einstein dynamics / coupling uniqueness.** Kinematics is not dynamics. The stress–
  curvature coupling (Einstein's equations) does **not** follow from the kinematic gates: energy
  conservation is necessary but not sufficient, and fixing the coupling uniquely requires an
  additional low-energy/Lovelock input. *This residue is GR-specific and is not reducible to the
  covariance residue.*

- **(R-c) Circularity of the admissibility gates.** The conditional descent depends on
  admissibility principles whose status is genuinely in question: are they real finite-record laws,
  or the desired geometry encoded as gate language? Until each gate has an independent finite-record
  derivation, the descent risks assuming what it reconstructs. *This is a methodological residue
  with no Branch-1 analogue.*

**Status: OPEN; three residues, of which one (R-a) is shared with Branch 1 and two (R-b, R-c) are
GR-specific.**

---

## 6. The shared root

Collecting Sections 4 and 5: after the clearable obstructions are cleared, the field-theory
reconstruction reduces to (R-a), and the geometry-kinematics reconstruction reduces to (R-a) plus
(R-b) and (R-c). The common factor (R-a) is, in both, the foliation-independent representation of
the hypersurface-deformation algebra — built as an interacting-field process in Branch 1, as a
stochastic-curvature realization in Branch 2. We therefore advance, as the paper's thesis:

```math
\boxed{
\begin{array}{l}
\text{The binding obstruction to a relativistic indivisible reconstruction of}\\
\text{both interacting QFT and effective-GR kinematics is one and the same:}\\
\text{the foliation-independent representation of the hypersurface-deformation}\\
\text{algebra on a frame-dependent, indivisible stochastic substrate.}\\
\text{Indivisibility (no required trans-foliation joint history) is the shared lever.}
\end{array}}
```

We advance "*the same* obstruction" as an explicit synthesis/conjecture: the two residues are the
same *structure* (the Dirac–Schwinger algebra) in both branches, which we have shown; proving they
are the same *problem* — that discharging one discharges the other — is itself open work, and we
flag it as such.

---

## 7. What is deliberately not in this map

- **Gravity sourcing.** How non-conserved (beable) matter couples to a *classical* metric — the
  unimodular-gravity route, its dynamical cosmological term, and the bounds that exclude it as dark
  energy or dark matter — is a different problem (the matter↔gravity interface, and it is
  Markovian-agnostic, broader than ISP). It is treated in a companion paper and excluded here to
  avoid conflating "reconstructing geometry" with "coupling to geometry."

- **A reconstruction claim.** Nothing here reconstructs QFT or derives GR. The map locates the
  open problem; it does not close it.

---

## 8. Status ledger

| Item | Status |
|---|---|
| Non-relativistic QM as ISP | established (Barandes), table-stakes |
| Free relativistic field as ISP | established (Nelson/Guerra–Ruggiero/Hudson), Gaussian-trivial |
| Free 1+1D stochastic-curvature theorem | established, narrow, explicitly not gravity |
| QFT: energy/Bianchi killer (K1) | cleared (unimodular; faithful = unitary) |
| QFT: Wigner-negativity killer (K2) | cleared (config-space, not phase-space) |
| QFT: Haag killer (K3) | cleared (Schrödinger-functional rep) |
| QFT: TS-integrability killer (K4) | cleared for the beable (modulus argument); operator-anomaly loophole |
| QFT residue (R-a covariance) | OPEN — one residue, one lever, one postulate |
| GR kinematics (conditional) | established conditionally; admissibility-gate dependent |
| GR residue (R-a covariance) | OPEN — shared with QFT |
| GR residue (R-b Einstein dynamics) | OPEN — GR-specific |
| GR residue (R-c gate circularity) | OPEN — GR-specific, methodological |
| Shared-root thesis (same structure) | shown (same algebra); "same problem" = conjecture |

---

## 9. Conclusion

The relativistic extension of the indivisible-stochastic program is not a reconstruction; it is
an obstruction with a precise shape. We have argued that the field-theory and geometry branches,
after their clearable obstacles are removed, meet at a single residue — the foliation-independent
representation of the hypersurface-deformation algebra on an indivisible substrate — and that the
distinctive feature of indivisibility, the absence of a required trans-foliation joint history, is
the one lever that separates this residue from the over-determination that blocks covariant
Bohmian field theory. The geometry branch carries, in addition, a dynamics residue and a
methodological circularity that the field-theory branch does not, and we have kept these separate
so that the two branches are not mistaken for being equally near completion. The honest yield is a
map: of what is settled (little, and old), what is clearable (four apparent killers), and what is
genuinely open (one shared residue and two geometry-specific ones). Whether the shared residue is
dischargeable — and whether indivisibility's lever is decisive or merely suggestive — is left
open. It is, on the present evidence, a decade-scale problem in mathematical physics, now stated
correctly.

---

## References

- [Barandes2023a] J. A. Barandes, *The Stochastic-Quantum Correspondence*, arXiv:2302.10778.
- [Barandes2023b] J. A. Barandes, *Quantum Theory as a Theory of Indivisible Stochastic Processes*, arXiv:2309.03085.
- [Barandes2025] J. A. Barandes, arXiv:2507.21192.
- [Nelson1966] E. Nelson, *Derivation of the Schrödinger Equation from Newtonian Mechanics*, Phys. Rev. **150**, 1079 (1966).
- [Nelson1973] E. Nelson, *Construction of quantum fields from Markoff fields*, J. Funct. Anal. **12**, 97 (1973).
- [GuerraRuggiero1973] F. Guerra and P. Ruggiero, *New Interpretation of the Euclidean–Markov Field in the Framework of Physical Minkowski Space–Time*, Phys. Rev. Lett. **31**, 1022 (1973).
- [Hudson1974] R. L. Hudson, *When is the Wigner quasi-probability density non-negative?*, Rep. Math. Phys. **6**, 249 (1974).
- [Dirac1958] P. A. M. Dirac, *The Theory of Gravitation in Hamiltonian Form*, Proc. R. Soc. A **246**, 333 (1958).
- [Schwinger1962] J. Schwinger, *Quantized Gravitational Field*, Phys. Rev. **130**, 1253 (1962).
- [HKT1976] S. A. Hojman, K. Kuchař, C. Teitelboim, *Geometrodynamics Regained*, Ann. Phys. **96**, 88 (1976).
- [Symanzik1981] K. Symanzik, *Schrödinger representation and Casimir effect in renormalizable quantum field theory*, Nucl. Phys. B **190** [FS3], 1 (1981).
- [Tumulka2006] R. Tumulka, *A Relativistic Version of the Ghirardi–Rimini–Weber Model*, J. Stat. Phys. **125**, 821 (2006).
- [Tumulka2020] R. Tumulka, *A Relativistic GRW Flash Process with Interaction*, arXiv:2002.00482.
- [Nikolic2006] H. Nikolić, *Relativistic quantum mechanics and the Bohmian interpretation*, Phys. Lett. A **348**, 166 (2006); hep-th/0501046.
- [AharonovAlbert1980] Y. Aharonov and D. Z. Albert, *States and observables in relativistic quantum field theories*, Phys. Rev. D **21**, 3316 (1980).
- [AharonovAlbert1981] Y. Aharonov and D. Z. Albert, Phys. Rev. D **24**, 359 (1981).
- [DurrEtAl2014] D. Dürr, S. Goldstein, T. Norsen, W. Struyve, N. Zanghì, *Can Bohmian mechanics be made relativistic?*, Proc. R. Soc. A **470**, 20130699 (2014); arXiv:1307.1714.
- [RE-curvature] F. Robles Elvira, *The Free Stochastic-Curvature Theorem for Relativistic ISP* (companion preprint).
- [RE-descent] F. Robles Elvira, *Finite Descent Reconstruction of Effective GR* (companion preprint).

*Reference volume/page/arXiv details to be re-verified against primary sources before submission.*
