# Free-QFT Promotion From ISP Stochastic Curvature

Author: Felix Robles Elvira

V2 Paper 7 investigation draft

Date: 2026-05-16

Status: theorem-framework draft. This paper follows V2 Paper 6 and precedes the
QFT-matching paper now inserted as Paper 8. The metric-data gate is moved to
Paper 9. Paper 7 proves the Gamma-only no-go at the investigation level and
states a conditional free Dirac/CAR promotion theorem, making explicit which
extra structures must be supplied beyond `Gamma`-level stochastic data.

The scope decision is strict:

> Paper 7 is a free-QFT promotion paper, not a metric or gravity paper. It tests
> whether the finite stochastic-curvature benchmark can be lifted, with explicit
> additional hypotheses, into covariance, spectrum, vacuum/Fock sector, and local
> algebra structure.

The honest expectation is mixed:

1. bare stochastic kernels and exchange curvature do not determine a unique QFT;
2. a conditional free-QFT promotion theorem may be possible once the necessary
   lift, one-particle convergence, complex structure, and local algebra data are
   declared and controlled;
3. the value of the paper is to say exactly where the stochastic layer ends and
   the QFT representation layer begins.

## 1. Why Paper 7 Exists

Paper 6 ended with a clear boundary:

```text
finite operational ISP-net reconstruction
!= continuum relativistic QFT reconstruction
```

It also identified the gates needed for QFT promotion:

1. sampling and continuum convergence;
2. covariance;
3. spectrum/positive energy;
4. vacuum or sector selection;
5. local field/algebra net;
6. continuum stability;
7. lift-gauge discipline.

Paper 1 supplies the first real continuum-facing input:

```math
\mathfrak C_a[N,M]\iota_a\phi
\longrightarrow
K_\parallel[N\partial_xM-M\partial_xN]\phi .
```

That is a stochastic-curvature theorem, not a QFT theorem. Paper 7 asks whether
the missing QFT gates can be supplied in the free benchmark without pretending
they came from bare `Gamma` data.

## 2. Ontological Discipline

Paper 7 must keep four layers separate.

1. **Stochastic layer.** Finite configuration spaces, endpoint kernels,
   comparison maps, exchange defects, and operational records.
2. **Lift layer.** A chosen Hilbert-space or unistochastic representation whose
   Born-squared endpoint kernels reproduce the stochastic data.
3. **One-particle QFT layer.** Continuum one-particle Hilbert space, Dirac or
   Klein-Gordon dynamics, covariance, and spectrum information.
4. **Field-theoretic layer.** Fock/CAR/CCR construction, vacuum, local algebras,
   microcausality, and state selection.

Barandes alignment says the stochastic layer is primary. But QFT promotion is
not free: it needs representation data. The theorem must say which data are
extra and which are reconstructed.

## 3. Export Ledger From Papers 1-6

| Source | Exported To Paper 7 | Not Exported |
| --- | --- | --- |
| Paper 1 | `1+1D` free one-particle stochastic-curvature theorem; smooth sampling map; log-smeared finite-slab theorem under explicit scaling. | Fock space, vacuum, local algebra, spectrum condition, full Lorentz covariance. |
| Paper 2 | Projective hypersurface/refinement language and anti-Markov-divisibility discipline. | Continuum QFT functor or Poincare representation. |
| Paper 3 | Locality/inverse-control vocabulary for comparison maps. | Free-field Fock reconstruction. |
| Paper 4 | Operational instruments and phase-completeness discipline. | Unique Hilbert lift or local algebra. |
| Paper 5 | Gauge-sector caution and center resolution. | Free QFT construction. |
| Paper 6 | No-go for Markovized shadows; finite operational reconstruction; QFT-promotion gates; lift-gauge discipline. | Continuum QFT reconstruction. |

Therefore Paper 7 must not silently assume:

1. a unique Hilbert lift from `Gamma`;
2. a canonical complex structure;
3. a vacuum;
4. positive energy;
5. Fock functoriality;
6. local `*`-algebras;
7. microcausality;
8. Lorentz covariance.

Each must be explicitly added, proved from a richer data set, or rejected as
unavailable.

## 4. Central Question

The central question is:

> Given the Paper 1 free one-particle ISP curvature data, what additional
> structures are sufficient and necessary to promote the benchmark to a free
> relativistic QFT representation?

This separates two claims.

**Negative claim.** Gamma-only stochastic curvature does not determine a unique
free QFT.

**Positive conditional claim.** Gamma-level curvature plus a compatible
one-particle Hilbert lift, continuum generator convergence, positive-energy
complex structure, and local algebra assignment can produce a standard free QFT
candidate.

Both are valuable. The negative claim protects the ontology. The positive claim
shows how ISP can interface with ordinary QFT without pretending that all QFT
structure was already present in probabilities alone.

## 5. Gate Q1: One-Particle Continuum Limit

A free-QFT promotion theorem first needs a one-particle continuum theorem
stronger than the Paper 1 curvature statement.

### Required data

1. Lattice one-particle Hilbert spaces `\mathcal H_a`.
2. Sampling maps
   ```math
   \iota_a:C_c^\infty(\mathbb R,\mathbb C^r)\to \mathcal H_a.
   ```
3. A chosen lift `U_a(t)=e^{-itH_a}` whose Born-squared endpoint kernel is the
   declared ISP kernel:
   ```math
   \Gamma_a(t)_{xy}=|[U_a(t)]_{xy}|^2.
   ```
4. A continuum one-particle generator `H`.
5. A convergence topology, for example strong convergence on sampled test
   profiles:
   ```math
   \|U_a(t)\iota_a\phi-\iota_a e^{-itH}\phi\|\to0
   ```
   uniformly for `t` in compact intervals.

### Warning

This lift is extra representation data unless Paper 7 proves it is fixed by the
stochastic connection up to the accepted gauge equivalence. Paper 6 says not to
expect that from bare component shadows.

## 6. Gate Q2: Covariance

A free relativistic QFT needs more than a Hamiltonian limit. It needs a
representation of spacetime symmetries or a hypersurface-deformation covariance
structure.

At the one-particle level, a minimal target is a projective or unitary
representation

```math
g\mapsto U(g)
```

of the relevant symmetry group on the continuum one-particle space, together
with finite approximants `U_a(g)` such that

```math
U_a(g)\iota_a\phi
\longrightarrow
\iota_a U(g)\phi
```

on the tested domain.

For the current `1+1D` free benchmark, Paper 7 should begin conservatively:

1. spatial translations;
2. time translations;
3. the restricted hypersurface/tangential action already seen in Paper 1;
4. only later, boosts or full Poincare covariance.

Finite stochastic isomorphisms with stochastic inverses are only permutations.
Therefore nontrivial covariance cannot be claimed at fixed finite regulator as a
stochastic isomorphism theorem. It must be a projective/refinement/continuum
statement.

## 7. Gate Q3: Spectrum And Complex Structure

The one-particle Dirac Hamiltonian has both positive and negative spectral
branches. A free QFT needs a sector or complex structure that defines what
counts as particles, antiparticles, and vacuum.

The promotion data must include either:

1. a positive-frequency projection `P_+`;
2. a complex structure `J` compatible with the symplectic or CAR/CCR form;
3. or an equivalent representation-selection principle.

The spectrum gate is:

```math
\operatorname{spec}(H_{\mathrm{phys}})\subset [0,\infty)
```

after the chosen field-theoretic construction and vacuum energy convention.

This is not a `Gamma`-level fact. It belongs to the representation and sector.
Paper 7 must mark it as such.

## 8. Gate Q4: Fock/CAR Or CCR Promotion

For the free Dirac benchmark, the natural field-theoretic promotion is CAR.
Given a one-particle space and a positive-energy/complex-structure choice, build
the CAR algebra

```math
\mathrm{CAR}(\mathcal K)
```

or a Fock representation

```math
\mathcal F_{\mathrm{CAR}}(\mathcal K_+).
```

For a scalar benchmark, the analogous choice would be CCR with a symplectic
space and a positive-frequency complex structure.

Paper 7 should prefer CAR for the current Dirac lineage, but it must state:

> The CAR/Fock functor is not reconstructed from a stochastic transition matrix
> alone. It is a representation-promotion input unless a separate theorem proves
> otherwise.

## 9. Gate Q5: Local Algebra Net

Free QFT reconstruction requires local algebras

```math
I\mapsto \mathcal A(I)
```

for bounded spatial intervals or spacetime regions. For CAR fields, a standard
candidate is generated by smeared field operators with test functions supported
in `I`.

Minimum conditions:

1. **Isotony:** `I\subset J` implies `\mathcal A(I)\subset\mathcal A(J)`.
2. **Adjoint/positivity:** local algebras are `*`-algebras or C*-algebras.
3. **Dynamics:** time evolution maps local algebras into causally enlarged
   regions.
4. **Microcausality:** spacelike separated local algebras commute or graded
   commute.
5. **Continuum stability:** finite-regulator operational nets converge to the
   same local algebraic structure.

Paper 6 already proved that a bare kernel does not determine local
factorization. Paper 7 must therefore supply locality as a representation/net
structure and then prove compatibility with the ISP curvature data.

## 10. No-Go Theorem: Gamma-Only Free-QFT Promotion Fails

Paper 7's first theorem is a precise non-injectivity statement.

### Definition 10.1: Gamma-only stochastic-curvature data

Fix a regulator label `a`. Gamma-only data consist of:

1. finite endpoint sets `X_a`;
2. projective coarse-graining maps between regulators;
3. declared endpoint kernels
   ```math
   \Gamma_a(\lambda):\Delta(X_a)\to\Delta(X_a)
   ```
   for the tested laboratory/deformation parameters `\lambda`;
4. comparison maps and exchange-curvature coefficients obtained by algebraic
   operations on those kernels.

Gamma-only data do **not** include:

1. a chosen complex Hilbert lift `U_a(\lambda)`;
2. relative phases not visible in `|\cdot|^2`;
3. a CAR or CCR choice;
4. a vacuum or positive-energy sector;
5. a local tensor factorization or local algebra net;
6. a rule saying which unrecorded partial kernels may be composed.

Thus a Gamma-only reconstruction rule is any rule whose output is a function
only of the data in items 1-4 above.

### Theorem 10.2: Gamma-only data do not determine a free QFT

The forgetful map

```math
\{\text{free-QFT promotion data}\}/\!\sim
\longrightarrow
\{\text{Gamma-only stochastic-curvature data}\}
```

is not injective. Consequently there is no Gamma-only reconstruction rule that
assigns a unique free relativistic QFT representation to bare endpoint kernels
and their stochastic-curvature coefficients.

More concretely, even if a one-particle Hilbert lift and one-particle endpoint
probabilities are fixed on the tested sector, the following data remain
undetermined:

1. field statistics, `CAR` versus `CCR`;
2. vacuum/Fock representation;
3. positive-frequency or complex-structure choice;
4. local algebra/factorization assignment;
5. phase-sensitive coherent composition outside the declared endpoint tests.

#### Proof, part 1: Fock-statistics ambiguity

Let `\mathcal K` be a nonzero one-particle Hilbert space with a chosen unitary
one-particle evolution `U(t)`. Choose an endpoint basis on the tested
one-particle sector and define

```math
\Gamma(t)_{xy}=|\langle x,U(t)y\rangle|^2 .
```

All Gamma-only comparison maps and stochastic-curvature coefficients computed
from this one-particle endpoint family are fixed by `\Gamma(t)`.

Now build two free field theories from the same one-particle dynamics:

```math
\mathcal F_{\rm CAR}(\mathcal K),
\qquad
\mathcal F_{\rm CCR}(\mathcal K).
```

Both restrict to the same one-particle transition probabilities. Therefore both
export the same tested `\Gamma(t)` and the same one-particle
stochastic-curvature coefficients.

They are not the same free QFT representation. In the one-mode case this is
already visible:

```math
\operatorname{spec}(N_{\rm CAR})=\{0,1\},
\qquad
\operatorname{spec}(N_{\rm CCR})=\{0,1,2,\ldots\}.
```

The fermionic theory has no two-particle occupancy of the same mode; the bosonic
theory does. No unitary equivalence preserving the particle-number observable
and the field algebra can identify these theories. Therefore the one-particle
Gamma-only data do not determine the Fock functor, the multiparticle sector, or
the field statistics.

This example is intentionally elementary. It shows that even perfect
one-particle stochastic-curvature control is not yet QFT reconstruction.

If an external spin-statistics theorem is invoked to rule out one of these
promotions, that theorem is using precisely the extra structure absent from
Gamma-only data: locality, covariance, spectrum, and a field algebra. That does
not weaken the no-go; it identifies the missing hypotheses.

#### Proof, part 2: local-net ambiguity

A free QFT also needs a declaration of which observables are local to which
region. A global endpoint kernel does not contain that declaration.

Take the finite one-particle Hilbert space

```math
\mathcal K=\mathbb C^4
```

with trivial one-particle evolution `U(t)=I`. The tested endpoint kernel is

```math
\Gamma(t)=I
```

for all `t`, and every exchange-curvature coefficient built from this family is
zero.

This is a deliberately minimal regulated sector. If Gamma-only data cannot
select a local net in this zero-curvature subproblem, it cannot select one in a
continuum free QFT without extra locality data.

Now choose the standard two-region factorization

```math
\mathcal K=\mathbb C^2_A\otimes\mathbb C^2_B
```

and local algebra

```math
\mathcal A_A=B(\mathbb C^2_A)\otimes I_B .
```

Let `W` be the controlled-not change of tensor coordinates

```math
W|u,v\rangle=|u,u\oplus v\rangle .
```

Define a second region assignment by

```math
\mathcal A'_A=W\mathcal A_AW^\dagger .
```

The same global endpoint kernel `\Gamma(t)=I` and the same zero curvature data
are compatible with both assignments. But the assignments are not the same
local net relative to the original region labels. For example, `W` maps some
operators that are `A`-local in the primed net to operators that act on both
tensor factors in the unprimed net. Thus Gamma-only data do not determine the
local algebra structure.

Since a relativistic QFT representation includes its local net, the same
Gamma-only data support inequivalent QFT-promotion data.

#### Proof, part 3: conclusion

Parts 1 and 2 produce distinct free-field promotion data with identical
Gamma-only one-particle endpoint statistics and identical derived
stochastic-curvature coefficients on the tested sector. A rule depending only
on the Gamma-only data must assign the same output to both. But a faithful QFT
promotion must distinguish at least field statistics and local algebra
assignment. Contradiction.

Therefore Gamma-only stochastic curvature cannot reconstruct a unique free QFT.
Additional representation data are not optional decoration; they are logically
necessary inputs for QFT promotion.

### Corollary 10.3: what the positive theorem must add

Any positive Paper 7 theorem must explicitly supply or derive:

1. the Hilbert lift and its accepted lift-gauge equivalence;
2. the positive-energy or complex-structure choice;
3. the CAR/CCR field functor;
4. the vacuum or sector-selection rule;
5. the local algebra net and its covariance/locality properties;
6. the refinement stability of all of the above.

This no-go is not anti-ISP. It says exactly where the stochastic layer ends and
where the QFT representation layer begins.

## 11. Minimal Counterexample Laboratory

The no-go should have a toy model so small that the obstruction cannot hide
behind continuum analysis.

### Counterexample 11.1: two-state phase-Hamiltonian ambiguity

Let the endpoint set be

```math
X=\{0,1\}.
```

Declare the Gamma-only endpoint dynamics to be trivial for all tested times:

```math
\Gamma(t)=I_2 .
```

All endpoint probabilities are therefore frozen. If the comparison/exchange
maps are built only from this family, their exchange curvature is also zero.

Now choose the one-particle Hilbert space

```math
\mathcal K=\mathbb C^2,
\qquad
|0\rangle, |1\rangle
```

with endpoint basis matching `X`. The same Gamma-only data admit at least two
inequivalent Hilbert lifts:

```math
U_0(t)=I_2,
\qquad
H_0=0,
```

and

```math
U_\omega(t)=
\begin{pmatrix}
1&0\\
0&e^{-i\omega t}
\end{pmatrix},
\qquad
H_\omega=
\begin{pmatrix}
0&0\\
0&\omega
\end{pmatrix},
\quad \omega>0.
```

Both lifts give the same endpoint transition matrix:

```math
|\langle x,U_0(t)y\rangle|^2
=
|\langle x,U_\omega(t)y\rangle|^2
=
\delta_{xy}.
```

So Gamma-only stochastic data cannot distinguish `H_0` from `H_\omega`.
They are not related by a fixed endpoint-basis rephasing that preserves the
time-translation representation; removing `\omega` would require changing the
time-dependent operational frame itself.

But the lifts are operationally distinct once phase-sensitive preparations and
effects are allowed. Prepare

```math
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt 2}
```

and measure the same `|+\rangle` effect after time `t`. The two predictions are

```math
P_0(+|+;t)=|\langle +|U_0(t)|+\rangle|^2=1,
```

while

```math
P_\omega(+|+;t)
=
|\langle +|U_\omega(t)|+\rangle|^2
=
\cos^2(\omega t/2).
```

The endpoint-basis Gamma data are identical, but the phase-complete operational
predictions differ. Therefore the one-particle Hamiltonian, phase evolution,
and positive-energy scale are not determined by Gamma-only data.

If the operational family is restricted to endpoint-basis preparations and
endpoint-basis effects, the two lifts are deliberately indistinguishable. That
is not a rescue of Gamma-only reconstruction; it is the counterexample's point.
The missing information is exactly the phase-complete operational or lift data
needed before one can claim a QFT representation.

This is the smallest useful counterexample:

```text
same endpoint Gamma
same zero stochastic exchange curvature
different phase-sensitive one-particle physics.
```

### Counterexample 11.2: same one-particle data, different field promotion

Now take the nontrivial lift `U_\omega(t)` as fixed. Even then, the one-particle
Gamma data still do not determine the field theory.

Use the one-dimensional positive-energy mode generated by `|1\rangle`. A
fermionic promotion gives the one-mode CAR Fock space

```math
\mathcal F_{\rm CAR}=\operatorname{span}\{|0\rangle_{\rm vac},|1\rangle_{\rm f}\},
\qquad
\operatorname{spec}(N_{\rm CAR})=\{0,1\}.
```

A bosonic promotion gives the one-mode CCR Fock space

```math
\mathcal F_{\rm CCR}=\operatorname{span}\{|n\rangle_{\rm b}:n\ge 0\},
\qquad
\operatorname{spec}(N_{\rm CCR})=\{0,1,2,\ldots\}.
```

On the one-particle sector, both carry the same phase `e^{-i\omega t}` and hence
the same endpoint-basis Gamma data. But the number-two test separates them:

```math
\Pr_{\rm CAR}(N=2)=0
```

for every state, whereas the CCR theory has a valid state `|2\rangle_{\rm b}`
with

```math
\Pr_{\rm CCR}(N=2)=1 .
```

Thus even after the one-particle phase lift is supplied, the field functor is
still additional structure. Gamma-only data do not tell us whether the mode is
fermionic or bosonic.

### Counterexample 11.3: same finite dynamics, different local split

The minimal local-net ambiguity needs four endpoint labels rather than two. Let

```math
\mathcal K=\mathbb C^4,
\qquad
U(t)=I_4,
\qquad
\Gamma(t)=I_4 .
```

With the standard two-qubit split,

```math
\mathcal K=\mathbb C^2_A\otimes\mathbb C^2_B,
```

the `A`-local algebra is

```math
\mathcal A_A=B(\mathbb C^2_A)\otimes I_B .
```

Conjugating the split by controlled-not,

```math
W|u,v\rangle=|u,u\oplus v\rangle .
```

gives a second admissible local algebra

```math
\mathcal A'_A=W\mathcal A_AW^\dagger .
```

Both local assignments export the same global endpoint Gamma data and the same
zero curvature. They differ only in locality structure. Since QFT is a local
algebraic theory, this again proves that Gamma-only data are not enough.

### Lesson

The counterexample has three nested morals:

1. endpoint probabilities do not determine phase-sensitive one-particle
   dynamics;
2. one-particle dynamics do not determine the Fock/statistics functor;
3. global dynamics do not determine local algebra assignments.

Therefore the positive theorem cannot be "QFT from Gamma." It must be:

```text
Gamma data
+ phase-complete operational/lift data
+ field-statistics choice
+ local-net structure
-> conditional free-QFT promotion.
```

## 12. Positive Benchmark And Conditional Free-Fermion Promotion

The positive side of Paper 7 should be narrow, explicit, and honest. The first
benchmark is:

```text
massive 1+1D free Dirac one-particle limit
plus CAR field promotion
plus compactly supported equal-time local net.
```

Not scalar/CCR first. Not interacting QFT. Not full curved spacetime. Not
metric reconstruction. This choice matches Paper 1's free Dirac
stochastic-curvature theorem and avoids adding bosonic infrared/domain issues
before the fermionic benchmark is understood.

### 12.1 Benchmark data: massive Dirac/CAR

Use units `c=\hbar=1`. The continuum one-particle space is

```math
\mathcal H=L^2(\mathbb R,\mathbb C^2)
```

with Dirac Hamiltonian

```math
H_D=-i\alpha\partial_x+m\beta,
\qquad
\alpha=\sigma_x,\quad \beta=\sigma_z,\quad m>0,
```

on domain `H^1(\mathbb R,\mathbb C^2)`. The mass assumption gives a clean
spectral gap at zero. The massless benchmark can be handled later with an
explicit zero-mode/infrared convention.

At regulator spacing `a`, use the Paper 1 lattice spinor space

```math
\mathcal H_a=\ell^2(\Lambda_a,\mathbb C^2),
\qquad
(\iota_a\phi)_{n,s}=a^{1/2}\phi_s(an),
```

with `\Lambda_a` a large periodic ring satisfying `a|\Lambda_a|\to\infty` and
with all tested supports away from the periodic seam. The chosen lift is a
self-adjoint finite Dirac generator `H_a`, for example the central-difference
Paper 1 generator on the sampled smooth sector:

```math
H_a=-\frac{i}{2a}\alpha(T_+-T_-)+m\beta.
```

The ISP endpoint kernel exported by this lift is

```math
\Gamma_a(t)_{xy}=|\langle x,e^{-itH_a}y\rangle|^2.
```

This is an additional lift datum. Gamma-only data do not select `H_a`.

### 12.2 Sampled one-particle convergence theorem

Paper 7 should not claim a full finite-lattice one-particle theorem over every
regulator mode. The honest positive statement is a sampled smooth-sector
theorem.

Choose a momentum cutoff `\Lambda(a)` satisfying

```math
\Lambda(a)\to\infty,
\qquad
a\Lambda(a)\to0.
```

Let `\Pi_a^{\rm low}` be the lattice Fourier projection onto
`|p|\le\Lambda(a)`. For every `\phi\in C_c^\infty(\mathbb R,\mathbb C^2)`,
smooth sampling obeys the high-momentum tail estimate

```math
\|(1-\Pi_a^{\rm low})\iota_a\phi\|_{\ell^2_a}=O_N(a^N)
```

for every fixed `N`, after choosing `\Lambda(a)` to grow slowly enough.

**Theorem 12.1: sampled Dirac lift convergence.** Assume:

1. `\iota_a` is the isometric sampling convention above on smooth compactly
   supported spinors.
2. The supports of all tested profiles remain away from the periodic seam for
   small `a`.
3. The selected finite generators are self-adjoint and agree with the Paper 1
   central-difference Dirac generator on the sampled smooth sector.
4. On the low-momentum sector,
   ```math
   \sup_{|p|\le\Lambda(a)}
   \left\|
   \alpha\frac{\sin(ap)}{a}+m\beta
   -
   \bigl(\alpha p+m\beta\bigr)
   \right\|
   \to0.
   ```
5. The high-momentum tail of sampled smooth profiles is negligible after
   applying `H_a` on compact time intervals.

Then, for every `\phi\in C_c^\infty(\mathbb R,\mathbb C^2)` and every compact
time interval `[-T,T]`,

```math
\sup_{|t|\le T}
\|e^{-itH_a}\iota_a\phi-\iota_a e^{-itH_D}\phi\|_{\ell^2_a}
\to0.
```

Moreover the convergence is uniform for `\phi` in bounded subsets of a fixed
Sobolev norm high enough to control the stated sampling tails.

**Proof.** In Fourier variables, the continuum symbol is

```math
h(p)=\alpha p+m\beta,
```

while the central-difference lattice symbol on the principal Brillouin branch is

```math
h_a(p)=\alpha\frac{\sin(ap)}{a}+m\beta.
```

On `|p|\le\Lambda(a)`,

```math
\frac{\sin(ap)}{a}-p=O(a^2|p|^3),
```

and `a\Lambda(a)\to0`, so `h_a(p)\to h(p)` uniformly on the low sector. The
sampled smooth vector has super-polynomially small complement outside the low
sector. Hence

```math
\|H_a\iota_a\phi-\iota_a H_D\phi\|_{\ell^2_a}\to0.
```

The free Dirac evolution preserves smooth compact support up to finite-speed
causal enlargement, so the same generator-consistency estimate is uniform for
`e^{-isH_D}\phi`, `|s|\le T`. Duhamel's formula gives

```math
e^{-itH_a}\iota_a\phi-\iota_a e^{-itH_D}\phi
=
-i\int_0^t e^{-i(t-s)H_a}
\bigl(H_a\iota_a-\iota_aH_D\bigr)e^{-isH_D}\phi\,ds
+r_a(t),
```

where `\sup_{|t|\le T}\|r_a(t)\|\to0` is the sampling/interpolation residual.
The unitary bound on `e^{-i(t-s)H_a}` then proves the claim.

### 12.3 Doubler policy

Theorem 12.1 deliberately avoids claiming a full all-mode lattice Fock theorem.
The central-difference lattice Dirac operator has high-momentum branches that
are invisible to smooth low-momentum sampling but would matter if one tried to
second-quantize the entire finite lattice Hilbert space.

Paper 7 therefore adopts the following scope rule:

> The positive theorem is a sampled-sector free-QFT promotion theorem. A full
> finite-regulator Fock theorem over all modes requires either a Wilson/admissible
> doubler-control lift or a proved low-energy sector projection. That stronger
> theorem is not claimed here.

This is not a weakness to hide. It is exactly the disciplined boundary between
the free continuum benchmark and a complete lattice-fermion construction.

### 12.4 Spectral projection convergence

The continuum Dirac Hamiltonian has positive and negative branches. The field
promotion therefore requires a polarization:

```math
P_+=1_{(0,\infty)}(H_D),
\qquad
P_-=1_{(-\infty,0)}(H_D),
```

and the corresponding complex/polarization datum

```math
J_D=i(P_+-P_-).
```

For the finite lifts, define spectral projections on the selected sampled sector:

```math
P_{a,+}=1_{(0,\infty)}(H_a),
\qquad
P_{a,-}=1_{(-\infty,0)}(H_a).
```

**Proposition 12.2: sampled spectral projection convergence.** Under the
hypotheses of Theorem 12.1 and the mass-gap assumption `m>0`, for every
`\phi\in C_c^\infty(\mathbb R,\mathbb C^2)`,

```math
\|P_{a,+}\iota_a\phi-\iota_a P_+\phi\|\to0,
\qquad
\|P_{a,-}\iota_a\phi-\iota_a P_-\phi\|\to0.
```

Here `\iota_a` is extended by the same sampling formula to the Schwartz/Sobolev
class containing `P_\pm\phi`. This extension is harmless in the massive free
case because the Fourier multipliers `P_\pm(p)` are smooth and bounded.

**Proof.** For the free massive Dirac operator the projections are explicit
Fourier multipliers. Let

```math
h(p)=\alpha p+m\beta,
\qquad
E(p)=\sqrt{p^2+m^2}.
```

Then

```math
P_+(p)=\frac12\left(I+\frac{h(p)}{E(p)}\right),
\qquad
P_-(p)=\frac12\left(I-\frac{h(p)}{E(p)}\right).
```

On the lattice low sector,

```math
h_a(p)=\alpha\frac{\sin(ap)}{a}+m\beta,
\qquad
E_a(p)=\sqrt{\left(\frac{\sin(ap)}{a}\right)^2+m^2},
```

and

```math
P_{a,+}(p)=\frac12\left(I+\frac{h_a(p)}{E_a(p)}\right),
\qquad
P_{a,-}(p)=\frac12\left(I-\frac{h_a(p)}{E_a(p)}\right).
```

Since `m>0`, the denominator is uniformly bounded below by `m`. The low-sector
symbol convergence from Theorem 12.1 therefore gives
`P_{a,\pm}(p)\to P_\pm(p)` uniformly on `|p|\le\Lambda(a)`. The sampled smooth
high-momentum tail is negligible, so the multiplier convergence implies
`P_{a,\pm}\iota_a\phi\to\iota_aP_\pm\phi`.

This remains representation-sector input. Gamma-only data do not select
`P_{a,+}`, `P_{a,-}`, or the vacuum. The theorem only says that, once the lift
and mass-gapped polarization are supplied, the finite projections converge on
the sampled smooth sector.

### 12.5 CAR local net and vacuum correlation convergence

Given the polarization, define the Dirac CAR field by

```math
\psi(f)=a(P_+f)+b^\dagger(CP_-f),
\qquad
f\in C_c^\infty(\mathbb R,\mathbb C^2),
```

where `C` is the charge-conjugation identification for the antiparticle space.
The vacuum `\Omega` is the quasifree Fock vacuum annihilated by the particle and
antiparticle annihilation operators.

For a bounded spatial interval `I`, define the equal-time local algebra

```math
\mathcal A(I)
=C^*\{\psi(f),\psi(f)^*: \operatorname{supp}f\subset I\}.
```

The required properties are standard once this structure is supplied:

1. **Isotony:** if `I\subset J`, then `\mathcal A(I)\subset\mathcal A(J)`.
2. **Graded locality:** if `I\cap J=\varnothing`, then odd fields anticommute
   and even subalgebras commute.
3. **Time evolution:** `\alpha_t(\psi(f))=\psi(e^{-itH_D}f)`.
4. **Causal propagation:** because the Dirac equation is first-order hyperbolic,
   the support of `e^{-itH_D}f` lies in the causal enlargement of
   `\operatorname{supp}f`.

Finite approximants are built from

```math
\mathcal K_a(I)=\operatorname{span}\{|n,s\rangle: an\in I,\ s=\uparrow,\downarrow\}
```

and the finite CAR algebra `\mathrm{CAR}(\mathcal K_a)`. The finite local
algebra is

```math
\mathcal A_a(I)=\mathrm{CAR}(\mathcal K_a(I)).
```

The finite-to-continuum local-net gate is convergence of vacuum `n`-point
functions for sampled test functions.

Let `\omega_a` and `\omega` be the finite and continuum quasifree vacuum states
determined by `P_{a,+}` and `P_+`. Their two-point functions are determined by
the corresponding one-particle projections. For example, in a convention where
the field covariance is written abstractly as `Q`, require

```math
\langle \iota_af,Q_a\iota_ag\rangle_{\ell^2_a}
\to
\langle f,Qg\rangle_{L^2}.
```

Here `Q_a` is the finite one-particle covariance built from `P_{a,+}` and `Q` is
the continuum covariance built from `P_+`.

**Proposition 12.3: CAR vacuum correlation convergence.** If the sampled
projection convergence of Proposition 12.2 holds, then for any fixed `k`, any
test spinors `f_1,\ldots,f_k\in C_c^\infty`, and any choices
`\#_j\in\{\emptyset,*\}`,

```math
\omega_a\!\left(
\psi_a(\iota_af_1)^{\#_1}\cdots\psi_a(\iota_af_k)^{\#_k}
\right)
\to
\omega\!\left(
\psi(f_1)^{\#_1}\cdots\psi(f_k)^{\#_k}
\right).
```

**Proof.** Quasifree CAR states are determined by their two-point functions.
Proposition 12.2 gives convergence of the one-particle covariances on sampled
test functions. Wick/Pfaffian expansion expresses each fixed `k`-point function
as a finite polynomial in the two-point functions. Therefore all fixed local
vacuum correlations converge.

### 12.6 Stochastic curvature as a local-net covariance generator

Paper 1 supplies a one-particle stochastic-curvature limit:

```math
R_a c_\lambda^{-2}\mathcal C_a^{(\lambda)}[N,M]\iota_a f
\to
\iota_a K_\parallel[\xi]f,
\qquad
\xi=N\partial_xM-M\partial_xN,
```

with

```math
K_\parallel[\xi]
=
\left(\xi\partial_x+\frac12\partial_x\xi\right)(I-\alpha).
```

Paper 7's covariance claim should be exactly this and no more:

> the stochastic exchange curvature converges to the one-particle infinitesimal
> operator that induces the corresponding tested derivation on the CAR net.

At the field level define the candidate infinitesimal action on smeared fields by

```math
\delta_\xi(\psi(f))=\psi(K_\parallel[\xi]f)
```

on the compactly supported test domain where `K_\parallel[\xi]f` is defined. For
real compactly supported `\xi`, the scalar operator
`\xi\partial_x+\frac12\partial_x\xi` is formally skew-symmetric, and it commutes
with the constant projector `(I-\alpha)`. Thus this is the right infinitesimal
CAR-field action on the tested domain.

**Proposition 12.4: finite-polynomial curvature response.** Define finite
actions on sampled fields by

```math
\delta_{a,N,M}(\psi_a(\iota_af))
=
\psi_a(R_a c_\lambda^{-2}\mathcal C_a^{(\lambda)}[N,M]\iota_af).
```

Assume the Paper 1 stochastic-curvature convergence and Proposition 12.3. Then,
for every fixed finite field polynomial `B` built from compactly supported
sampled test fields,

```math
\omega_a(\delta_{a,N,M}B)\to\omega(\delta_\xi B),
```

where `\delta_\xi` acts by the Leibniz rule on the finite polynomial algebra.

**Proof.** Apply Paper 1's one-particle convergence to each test function
appearing in `B`. CAR relations reduce the result to a finite linear
combination of quasifree vacuum correlations, and Proposition 12.3 passes those
correlations to the continuum limit.

This is a finite-polynomial linear-response theorem. To upgrade it to a
closed `*`-derivation on the C*-local net, the final paper must prove the
closability/core statement for `K_\parallel[\xi]` and its second-quantized CAR
implementation. Until that is done, Paper 7 should use the phrase
"tested local-net response" rather than full Lorentz covariance.

This is not yet full Lorentz covariance. It is the controlled bridge between
ISP stochastic curvature and the tested infinitesimal local-net action.

### 12.7 Conditional free-Dirac/CAR promotion theorem

**Theorem 12.5: conditional free-fermion QFT promotion.** Suppose the enriched
ISP/free benchmark supplies:

1. the Paper 1 coefficient-level stochastic-curvature theorem for the
   `1+1D` free Dirac benchmark;
2. chosen finite Hilbert lifts `U_a(t)=e^{-itH_a}` whose Born-squared endpoint
   kernels are the declared ISP kernels;
3. the sampled one-particle convergence theorem, Theorem 12.1;
4. the sampled spectral-projection convergence theorem, Proposition 12.2;
5. the CAR field functor, quasifree vacuum, and local net from Section 12.5;
6. finite local CAR nets `I\mapsto\mathcal A_a(I)` converging in vacuum
   correlation functions as in Proposition 12.3;
7. the stochastic-curvature finite-polynomial response theorem,
   Proposition 12.4;
8. the sampled-sector doubler policy of Section 12.3;
9. all products of finite comparison maps used in the proof are algebraic
   endpoint/lift operations or declared operational compositions, not
   Markovized unrecorded partial-kernel compositions.

Then the enriched data determine a free massive Dirac/CAR QFT candidate

```math
\left(
\mathcal F_{\rm CAR},
\Omega,
I\mapsto\mathcal A(I),
t\mapsto\alpha_t,
\delta_\xi^{\rm test}
\right)
```

up to the declared unitary, CAR, polarization, and lift-gauge equivalences.
Moreover:

1. `\alpha_t` is the free Dirac time evolution;
2. `I\mapsto\mathcal A(I)` is isotonic and graded-local;
3. finite regulator vacuum correlations converge to continuum vacuum
   correlations on compactly supported test fields;
4. the stochastic-curvature action converges to the tested local-net
   finite-polynomial response `\delta_\xi^{\rm test}`;
5. no claim is made that Gamma-only data determine this QFT candidate.

The theorem's output is:

```text
Gamma-level stochastic curvature
+ chosen Hilbert lift
+ sampled one-particle convergence
+ positive-energy polarization
+ CAR/vacuum/local-net data
-> conditional free Dirac QFT candidate.
```

It is not:

```text
Gamma alone -> QFT.
```

**Proof sketch.** Theorem 12.1 gives the continuum one-particle dynamics on the
sampled smooth sector. Proposition 12.2 gives the polarization on sampled test
fields. The CAR functor turns the one-particle space and polarization into the
Fock representation; support orthogonality gives graded locality at equal time,
while finite propagation for the Dirac equation gives causal time evolution of
local algebras. Proposition 12.3 gives convergence of local vacuum
correlations. Paper 1's curvature theorem and Proposition 12.4 give the tested
field-polynomial response to the stochastic-curvature operator.

The proof uses enriched representation data throughout. That is precisely why
it does not contradict the Gamma-only no-go.

## 13. Theorem Ledger

| Item | Status | Depends On | Output |
| --- | --- | --- | --- |
| Theorem 10.2 | no-go theorem stated and proved by non-injectivity examples | Gamma-only definition | `Gamma` and stochastic curvature do not determine free QFT |
| Section 11 | minimal counterexample laboratory | finite endpoint models | phase lift, Fock/statistics, and local-net ambiguity |
| Theorem 12.1 | sampled-sector theorem | chosen Hilbert lift and smooth sampling | one-particle Dirac dynamics on sampled test states |
| Proposition 12.2 | sampled-sector theorem | Theorem 12.1 and mass gap | positive/negative spectral projections converge |
| Proposition 12.3 | sampled-sector theorem | Proposition 12.2 and CAR quasifree construction | local vacuum correlations converge |
| Proposition 12.4 | finite-polynomial response theorem | Paper 1 curvature theorem and Proposition 12.3 | tested stochastic-curvature response on CAR field polynomials |
| Theorem 12.5 | conditional theorem | all Section 12 inputs | enriched ISP data promote to a free Dirac/CAR QFT candidate |

This ledger is also the honesty ledger: each positive theorem is conditional on
representation data that Gamma-only stochastic curvature does not determine.

## 14. Scope Box

Paper 7 proves neither too little nor too much.

It **does** claim:

1. Gamma-only stochastic-curvature data do not determine a unique free QFT.
2. A massive `1+1D` free Dirac/CAR benchmark can be conditionally promoted from
   enriched ISP data.
3. The positive theorem is valid on sampled smooth sectors with controlled
   low-momentum limits.
4. Finite vacuum field correlations converge on compactly supported sampled test
   fields.
5. Stochastic curvature has a tested finite-polynomial local-net response.

It **does not** claim:

1. `Gamma` alone reconstructs QFT.
2. The entire finite lattice Fock space converges mode-by-mode.
3. Fermion doubling is solved without a Wilson/admissible lift or a proved
   low-energy projection.
4. Full Lorentz covariance is proved.
5. The stochastic-curvature response is already a closed C*-local-net
   derivation.
6. Stress-energy, metric data, curved backgrounds, or dynamical geometry have
   been reconstructed.

## 15. Paper 8 Export Box

Paper 8 is now the QFT-matching paper, not the metric paper. It may use exactly
the following from Paper 7:

1. **No-go discipline:** free QFT is not reconstructed from `Gamma` alone.
2. **Enriched input list:** Hilbert lift, sampled convergence, polarization,
   CAR functor, vacuum, and local net are representation data.
3. **Theorem 12.1:** sampled one-particle Dirac convergence.
4. **Proposition 12.2:** sampled spectral projection convergence.
5. **Proposition 12.3:** CAR vacuum correlation convergence.
6. **Proposition 12.4:** finite-polynomial stochastic-curvature response.
7. **Theorem 12.5:** conditional free Dirac/CAR promotion theorem.
8. **Scope limits:** sampled-sector status, no all-mode Fock theorem, no full
   Lorentz covariance, no metric or stress-energy reconstruction.

Paper 8 must not treat Paper 7 as having proved:

1. full standard QFT equivalence;
2. all Wightman/Haag-Kastler axioms;
3. all-mode lattice Fock convergence;
4. stress-energy conservation or renormalized stress tensor;
5. fixed metric extraction;
6. dynamical geometry.

The task of Paper 8 is therefore precise:

```text
conditional free Dirac/CAR candidate
-> explicit matching with standard massive 1+1D free QFT observables,
   local algebras, vacuum correlations, spectrum, and tested covariance.
```

## 16. Failure Appendix

Paper 7 should fail cleanly, not ambiguously. There are four different failure
modes.

### Failure A: ISP lacks required QFT data

This occurs if the stochastic/operational ISP stack supplies only endpoint
kernels, comparison maps, and exchange curvature, but no phase-complete lift,
polarization, CAR/CCR choice, vacuum, or local algebra. This is not a
contradiction. It means ISP remains a probability-first finite/operational
dynamics framework, while QFT requires additional representation structure.

Diagnostic:

```text
Gamma and exchange curvature are controlled,
but no canonical Hilbert lift / vacuum / local net exists.
```

### Failure B: the chosen Hilbert lift is incomplete or wrong

This occurs if a specific lift `H_a` fails sampled convergence, fails spectral
projection convergence, excites unwanted high-momentum sectors, or gives local
correlations that do not match the intended Dirac/CAR benchmark. In that case
the failure belongs to the lift choice, not automatically to ISP.

Diagnostic:

```text
the stochastic substrate may be viable,
but this representation does not promote it to free QFT.
```

### Failure C: sampled-sector success does not become all-mode QFT

This is the expected residual limitation. Paper 7 may succeed on smooth sampled
sectors while still failing to control the whole finite lattice Fock space. A
full all-mode theorem would need Wilson/admissible doubler control, a stable
low-energy projection theorem, or a different regulator.

Diagnostic:

```text
continuum test fields match free QFT,
but regulator-scale modes remain outside the theorem.
```

### Failure D: curvature response remains only linear response

If `K_\parallel[\xi]` does not yield a closable/core-controlled derivation of the
local C*-net, Proposition 12.4 remains a finite-polynomial response theorem. That
is enough for Paper 8 matching tests on local field polynomials, but not enough
for claiming full local covariance.

Diagnostic:

```text
stochastic curvature acts on tested field polynomials,
but not yet as a closed local-net derivation.
```

## 17. What Would Count As Success

Paper 7 passes if it delivers both:

1. a precise no-go locating why Gamma-only stochastic curvature cannot uniquely
   reconstruct free QFT;
2. a conditional free-QFT promotion theorem with explicit hypotheses and a
   worked free Dirac benchmark.

The strongest reasonable claim is:

> Relativistic ISP can supply the stochastic-curvature and operational finite-net
> substrate for free QFT, but free QFT itself emerges only after adding compatible
> lift, sector, vacuum/Fock, and local algebra data.

## 18. Relation To Papers 8, 9, And 10

The corrected order is now:

```text
Paper 6: no-go plus finite operational reconstruction
Paper 7: conditional free-QFT promotion
Paper 8: free-QFT matching and equivalence benchmarks
Paper 9: Lorentz-covariant free-QFT completion
Paper 10: metric-data gate, not gravity
```

Paper 8 depends on Paper 7 because it asks whether the promoted candidate truly
matches standard free Dirac QFT. Paper 9 depends on Papers 7 and 8 because
Lorentz-covariant spacetime QFT matching should not be assumed from an
equal-time CAR match alone. Paper 10 depends on Papers 7-9 because metric
reconstruction should not precede the free-QFT and covariance matching audits.

Only after Paper 10 should fixed curved backgrounds, stress-energy response, or
dynamical geometry be attempted.

## 19. Initial Work Plan

1. Prove the Gamma-only free-QFT promotion no-go. Done in Section 10.
2. Build the minimal counterexample laboratory. Done in Section 11.
3. Choose the exact free benchmark: Dirac/CAR first, scalar/CCR later if useful.
   Done in Section 12.1.
4. State the one-particle lift convergence theorem needed beyond Paper 1. Done
   in Section 12.2.
5. Decide the doubler strategy. Done in Section 12.3.
6. Define and prove sampled positive-energy/spectral projection convergence.
   Done in Section 12.4.
7. Prove CAR vacuum correlation convergence. Done in Section 12.5.
8. Build the local CAR net and list its finite-regulator approximants. Done in
   Section 12.5.
9. Tighten the stochastic-curvature tangential action as a tested local-net
   response theorem. Done in Section 12.6.
10. State the conditional free-fermion promotion theorem. Done in Section 12.7.
11. Add a failure appendix distinguishing "ISP lacks QFT data" from "the chosen
   lift was incomplete." Done in Section 16.
12. Add scope box, theorem ledger, and Paper 8 export box. Done in Sections
   13-15.

## 20. Current Verdict

Paper 7 should be a QFT-promotion audit, not a triumphant reconstruction paper.
It should be explicit that bare stochastic kernels do not determine all free-QFT
structure. But it should also show that the ISP stack is not irrelevant to QFT:
it supplies a controlled stochastic-curvature substrate and a disciplined
operational reconstruction layer.

The correct thesis is:

> Free QFT is not reconstructed from `Gamma` alone; it is conditionally promoted
> from ISP stochastic curvature once compatible lift, spectrum, vacuum/Fock, and
> local algebra data are supplied and shown stable.
