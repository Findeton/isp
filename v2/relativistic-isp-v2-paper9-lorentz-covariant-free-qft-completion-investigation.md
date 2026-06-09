# Lorentz-Covariant Free-QFT Completion

Author: Felix Robles Elvira

V2 Paper 9 investigation draft

Date: 2026-05-16

Status: Route-B completion draft. The theorem-framework first pass is complete
through the Paper 10 export gate. This paper follows V2 Paper 8 and precedes the
metric-data gate now moved to V2 Paper 10. Paper 8 matched the enriched ISP free
Dirac/CAR candidate to standard massive `1+1D` free QFT on sampled equal-time
local field-polynomial observables. Paper 9 now attempts the stronger,
ISP-native route: construct finite-regulator boost approximants and prove
sampled-sector convergence to the standard Lorentz-covariant free Dirac/CAR
theory.

The scope decision is strict:

> Paper 9 is a Lorentz-covariant free-QFT completion paper, not a metric or
> gravity paper. It must not claim that `Gamma` alone reconstructs QFT. It tests
> whether the enriched Paper 7/8 representation matches standard free Dirac/CAR
> QFT as a spacetime-covariant local theory.

If Paper 9 passes, Paper 10 may ask whether stochastic exchange curvature
contains metric data. If Paper 9 fails, metric reconstruction is premature: the
program would have an equal-time free-QFT match, but not yet a fully
relativistic one.

## 1. Why Paper 9 Exists

Paper 8 proved the right benchmark result at the controlled level:

```text
enriched ISP + lift + polarization + CAR/local net
-> standard free Dirac/CAR matching on sampled equal-time local tests.
```

But Paper 8 explicitly deferred:

1. boost covariance;
2. full Lorentz/Poincare covariance;
3. spacetime local nets;
4. Wightman or Haag-Kastler-level axiom matching;
5. stress-energy;
6. metric extraction.

Paper 9 closes the first four gaps for the free massive `1+1D` Dirac/CAR
benchmark, while keeping stress-energy and metric reconstruction outside scope.

The target statement is:

```text
Paper 8 equal-time QFT matching
+ supplied/controlled boost representation
+ spacetime local-net extension
-> standard Lorentz-covariant free Dirac/CAR QFT matching.
```

It is not:

```text
Gamma alone -> Lorentz-covariant QFT.
```

## 2. Barandes-Compatible Ontological Discipline

The same discipline from Papers 6-8 remains mandatory.

1. **Whole-process stochastic data are primary.** A finite kernel describes a
   declared whole process or protocol, not an arbitrary Markov slice.
2. **Division events require physical records.** Intermediate hypersurfaces,
   detector cuts, or local algebras may be used only as declared structure, not
   as unrecorded stochastic factorizations.
3. **Hilbert and CAR data are representational enrichments.** The boost
   generator, spin representation, field algebra, and Fock vacuum are additional
   QFT-matching data.
4. **Lorentz covariance is a theorem about the enriched representation.** It is
   not a theorem about raw endpoint kernels unless a separate stochastic
   covariance theorem is proved.
5. **Operational equivalence is test-relative.** The paper matches predictions
   for local field-polynomial tests and detector protocols approximating them.

Thus Paper 9 is Barandes-compatible only if it says:

```text
the enriched ISP representation has the same Lorentz-covariant predictions as
standard free QFT on the tested sector.
```

It must never say:

```text
the stochastic kernel by itself contains the Poincare representation.
```

## 3. Export Ledger From Papers 1-8

Paper 9 may use exactly the following.

| Source | Exported To Paper 9 | Not Exported |
| --- | --- | --- |
| Paper 1 | `1+1D` free stochastic-curvature theorem and tested tangential action. | Full Lorentz covariance or stress-energy. |
| Paper 2 | Projective hypersurface-kernel compatibility without Markov divisibility. | Continuum Lorentz functor or metric data. |
| Paper 3 | Comparison-map locality and exchange-corridor control under explicit hypotheses. | General interacting QFT. |
| Paper 4 | Operational instrument discipline: raw maps are not automatically observables. | Raw-to-QFT observability without detector structure. |
| Paper 5 | Gauge-sector warnings and continuum-cutoff discipline. | Non-Abelian or full continuum gauge QFT. |
| Paper 6 | Gamma-only no-go and Barandes alignment. | QFT reconstruction from stochastic shadows alone. |
| Paper 7 | Conditional free Dirac/CAR promotion theorem on sampled sectors. | Standard-QFT equivalence or boosts. |
| Paper 8 | Local correlations, equal-time CAR net, time translations, positive energy, tested curvature response. | Boost covariance, spacetime net, Wightman/Haag-Kastler completeness, stress-energy, metric. |

Therefore Paper 9 must not assume:

1. a finite-regulator boost theorem;
2. all-mode finite lattice Fock convergence;
3. full interacting QFT;
4. stress-energy reconstruction;
5. metric extraction;
6. dynamical geometry.

Each missing item must be proved, added as an explicit hypothesis, or deferred.

## 4. Standard Relativistic Target

The target is the standard massive `1+1D` free Dirac/CAR theory as a
Poincare-covariant local QFT.

One-particle data:

```math
\mathcal H=L^2(\mathbb R,\mathbb C^2),
\qquad
H_D=-i\alpha\partial_x+m\beta,
\qquad
m>0.
```

The standard theory supplies a positive-energy unitary representation
`U(a,\Lambda)` of the proper orthochronous Poincare group, with translations
generated by energy-momentum and boosts generated by a self-adjoint boost
operator on its natural domain.

The CAR field satisfies covariance:

```math
U(a,\Lambda)\psi(f)U(a,\Lambda)^{-1}
=
\psi(S(a,\Lambda)f),
```

where `S(a,\Lambda)` is the standard spinor test-function action.

The spacetime local net is generated by fields smeared with test functions
supported in spacetime regions:

```math
O\mapsto \mathcal A(O).
```

The relativistic target properties are:

1. Poincare covariance of the field algebra;
2. spectrum condition;
3. unique invariant vacuum;
4. spacelike graded locality;
5. equality with the Paper 8 equal-time net on Cauchy slices;
6. finite propagation/time-slice compatibility for the free Dirac equation.

## 5. Route B Decision And Finite Boost Setup

Paper 9 attempts Route B directly, in the scoped sampled-sector sense:

```text
finite regulator boost approximants
-> sampled convergence to the standard Dirac boost
-> CAR/Fock polynomial convergence
-> spacetime-covariant free-QFT matching.
```

It does not attempt exact Lorentz covariance at fixed lattice spacing. A fixed
lattice breaks continuous boosts; the right theorem is regulator convergence on
smooth sampled states.

Use the Paper 7 central-difference one-particle lift

```math
H_a=\alpha P_a+m\beta,
\qquad
P_a=\frac{T_+-T_-}{2ia},
```

on a growing periodic ring or infinite lattice. Let `X_a` be multiplication by
the centered coordinate `an` on the nonwrapping test window. Define the finite
boost generator

```math
K_a=\frac12(X_aH_a+H_aX_a).
```

The continuum target is

```math
H_D=\alpha P+m\beta,
\qquad
P=-i\partial_x,
\qquad
K=\frac12(XH_D+H_DX).
```

With the convention `B(\eta)=e^{-i\eta K}`, the continuum commutators are

```math
[K,H_D]=iP,
\qquad
[K,P]=iH_D.
```

The natural lattice correction operator is

```math
C_a=\frac12(T_++T_-),
```

whose Fourier symbol is `\cos(ap)`. Away from the periodic seam,

```math
[X_a,P_a]=iC_a.
```

Hence the finite boost algebra is not exactly Poincare:

```math
[K_a,H_a]=iC_aP_a,
\qquad
[K_a,P_a]=iC_aH_a.
```

On the low-momentum sampled sector, `C_a\to I`, so these identities converge to
the continuum Poincare algebra. Seam terms are either absent on the infinite
lattice or vanish on the declared nonwrapping/growing-volume test family.

### 5.1 Lattice Convention, Domains, And Seam Policy

Use the shift convention

```math
(T_+\psi)_n=\psi_{n+1},
\qquad
(T_-\psi)_n=\psi_{n-1},
```

so that

```math
P_a=\frac{T_+-T_-}{2ia}
```

has principal Fourier symbol `\sin(ap)/a`. On the infinite lattice
`a\mathbb Z`, let

```math
(X_a\psi)_n=an\,\psi_n.
```

On a periodic ring, `X_a` is not globally periodic. Paper 9 therefore uses the
following seam policy:

1. prove the algebraic identities first on the infinite lattice;
2. transfer them to growing rings only for test families whose sampled mass,
   one finite-difference stencil, and boosted orbit have vanishing tail in the
   seam collar;
3. for compactly supported profiles, require the causal/boosted support window
   to remain a positive lattice distance from the seam;
4. for Schwartz profiles, require a growing half-circumference `R_a^{\rm ring}`
   such that the weighted tails beyond `R_a^{\rm ring}-O(a)` vanish in the
   norms used below.

The core domain is the weighted Schwartz domain

```math
\mathscr S(\mathbb R,\mathbb C^2)
\subset
\mathcal D(K)
```

with seminorms

```math
\|f\|_{s,r}
=
\sum_{j\le s}\|\langle X\rangle^r\partial_x^jf\|_{L^2},
\qquad
\langle X\rangle=(1+X^2)^{1/2}.
```

The lattice analog is

```math
\|\psi\|_{a,s,r}
=
\sum_{j\le s}\|\langle X_a\rangle^rD_a^j\psi\|_{\ell^2_a},
\qquad
D_a=P_a
```

up to harmless constants on the low-momentum sampled sector. The boost
generator convergence theorem uses `r=1` and `s` high enough to control the
third-derivative central-difference truncation error. Finite-rapidity boost
convergence later requires the continuum orbit
`\{B(\eta)f:|\eta|\le\eta_0\}` to remain bounded in the same weighted norm.

### 5.2 Finite Commutator Appendix

On the infinite lattice, the shift convention gives

```math
[X_a,T_+]=-aT_+,
\qquad
[X_a,T_-]=aT_-.
```

Therefore

```math
[X_a,P_a]
=
\frac{[X_a,T_+]-[X_a,T_-]}{2ia}
=
\frac{-aT_+-aT_-}{2ia}
=iC_a.
```

Since `C_a`, `P_a`, and the constant matrices `\alpha,\beta` commute where
appropriate, and since `\alpha^2=I` and `\alpha\beta+\beta\alpha=0`,

```math
[X_a,H_a]=i\alpha C_a.
```

With

```math
K_a=\frac12(X_aH_a+H_aX_a),
```

one obtains

```math
\begin{aligned}
[K_a,H_a]
&=\frac12\bigl([X_a,H_a]H_a+H_a[X_a,H_a]\bigr)\\
&=\frac{i}{2}C_a(\alpha H_a+H_a\alpha)\\
&=iC_aP_a,
\end{aligned}
```

because

```math
\alpha H_a+H_a\alpha=2P_a.
```

Similarly,

```math
\begin{aligned}
[K_a,P_a]
&=\frac12\bigl([X_a,P_a]H_a+H_a[X_a,P_a]\bigr)\\
&=\frac{i}{2}(C_aH_a+H_aC_a)\\
&=iC_aH_a.
\end{aligned}
```

These are exact infinite-lattice identities. On periodic rings they hold modulo
seam terms caused by the nonperiodic coordinate `X_a`; the seam terms vanish
under the nonwrapping/growing-volume policy of Section 5.1.

## 6. Theorem 9.1: Sampled Boost-Generator Convergence

**Theorem 9.1: sampled boost-generator convergence.** Let
`\mathscr S(\mathbb R,\mathbb C^2)` be the Schwartz spinor domain, with
sampling maps `\iota_a` extended as in Paper 7. Assume:

1. the Paper 7 sampled Dirac lift hypotheses;
2. the seam policy of Section 5.1;
3. the sampled family has uniformly controlled weighted Sobolev norms
   `\|f\|_{s,1}`;
4. the low-momentum cutoff satisfies `\Lambda(a)\to\infty` and
   `a^2\Lambda(a)^3\to0` (hence also `a\Lambda(a)\to0` after choosing
   `\Lambda(a)` slowly enough);
5. weighted generator consistency holds:
   ```math
   \|\langle X_a\rangle(H_a\iota_ag-\iota_aH_Dg)\|_{\ell^2_a}
   \to0
   ```
   uniformly for `g` in bounded subsets of the same weighted Sobolev class.

Then for every `f\in\mathscr S(\mathbb R,\mathbb C^2)`,

```math
\|K_a\iota_af-\iota_aKf\|_{\ell^2_a}\to0.
```

The convergence is uniform for `f` in bounded subsets of a sufficiently high
weighted Sobolev norm.

**Proof.** Since

```math
K_a\iota_af
=\frac12X_aH_a\iota_af+\frac12H_aX_a\iota_af,
```

and

```math
Kf=\frac12XH_Df+\frac12H_DXf,
```

it is enough to control the two terms separately.

For the first term,

```math
\begin{aligned}
\|X_aH_a\iota_af-\iota_aXH_Df\|
&\le
\|X_a(H_a\iota_af-\iota_aH_Df)\|\\
&\quad+
\|X_a\iota_aH_Df-\iota_aXH_Df\|.
\end{aligned}
```

The second term is zero on the infinite lattice with the sampling convention
`(\iota_af)_n=a^{1/2}f(an)` and is a vanishing seam residual on growing rings.
The first term tends to zero by weighted generator consistency.

For the second boost-generator term, write

```math
H_aX_a\iota_af-\iota_aH_DXf
=
H_a\iota_a(Xf)-\iota_aH_D(Xf)
+s_a(f),
```

where `s_a(f)` is zero on the infinite lattice and is a vanishing seam residual
on admissible growing rings. Since `Xf` lies in the same weighted Sobolev
control class with one fewer power of weight and with one additional derivative
allowed by the choice of `s`, Paper 7's generator consistency applies to `Xf`.
Thus

```math
H_aX_a\iota_af\to\iota_aH_DXf.
```

Averaging the two limits gives the theorem.

For the promised estimate, on the low-momentum sector,

```math
\frac{\sin(ap)}{a}-p=O(a^2|p|^3),
```

so

```math
\|H_a\Pi_a^{\rm low}\iota_ag-\iota_aH_Dg\|
\lesssim
a^2\Lambda(a)^3\|g\|_{3,0}+{\rm samp}_a(g).
```

With one spatial weight inserted, the same Taylor estimate gives

```math
\|\langle X_a\rangle(H_a\Pi_a^{\rm low}\iota_ag-\iota_aH_Dg)\|
\lesssim
a^2\Lambda(a)^3\|g\|_{3,1}+{\rm samp}_{a,1}(g),
```

while the high-momentum sampled tail is super-polynomially small for Schwartz
`g` and controlled by the declared weighted Sobolev bound for the theorem's
uniform version. Since the theorem assumes `a^2\Lambda(a)^3\to0`, the weighted
consistency estimate follows. The seam residual vanishes by Section 5.1.

This theorem is the first genuinely Route-B step: boosts are no longer merely
imported from standard continuum QFT; finite boost approximants are shown to
converge on the sampled sector.

## 7. Theorem 9.2: Approximate Poincare Algebra

**Theorem 9.2: sampled Poincare commutator convergence.** Under the hypotheses
of Theorem 9.1, for every `f\in\mathscr S(\mathbb R,\mathbb C^2)`,

```math
\|([K_a,H_a]-iP_a)\iota_af\|_{\ell^2_a}\to0,
```

and

```math
\|([K_a,P_a]-iH_a)\iota_af\|_{\ell^2_a}\to0.
```

Equivalently,

```math
[K_a,H_a]\iota_af\to i\iota_aPf,
\qquad
[K_a,P_a]\iota_af\to i\iota_aH_Df.
```

**Proof.** Away from seam terms,

```math
[K_a,H_a]=iC_aP_a,
\qquad
[K_a,P_a]=iC_aH_a.
```

On the low-momentum sector, `C_a` has symbol `\cos(ap)`, so

```math
\|(C_a-I)P_a\Pi_a^{\rm low}\|=O(a^2\Lambda(a)^3),
```

and similarly for `(C_a-I)H_a` on sampled profiles. Since
`a^2\Lambda(a)^3\to0` and sampled Schwartz tails outside the low sector are
super-polynomially small, the correction terms vanish. Paper 7 Theorem 12.1
then identifies `P_a\iota_af` with `\iota_aPf` and `H_a\iota_af` with
`\iota_aH_Df`.

The theorem exposes exactly what the finite lattice gets wrong: the algebra has
a `C_a=\cos(ap)` correction. The correction disappears only in the sampled
continuum limit.

## 8. Theorem 9.3: Finite-Rapidity Boost Convergence

**Lemma 9.3a: compact-rapidity orbit control.** For every
`f\in\mathscr S(\mathbb R,\mathbb C^2)`, every weighted Sobolev seminorm
`\|\cdot\|_{s,r}`, and every compact rapidity interval `|\eta|\le\eta_0`,

```math
\sup_{|\eta|\le\eta_0}\|B(\eta)f\|_{s,r}<\infty.
```

Moreover, on growing rings one may choose the ring half-circumference
`R_a^{\rm ring}` so that the sampled tails of `B(\eta)f` in the seam collar
vanish uniformly for `|\eta|\le\eta_0`.

**Proof.** The continuum boost action on massive free Dirac Cauchy data is a
strongly continuous one-parameter unitary group generated by the essentially
self-adjoint operator `K` on the Schwartz domain. The generator `K` is first
order with coefficients at most linear in `x`, so commutators with
`\langle X\rangle^r\partial_x^j` are finite sums of operators of the same
weighted first-order type. Standard energy estimates for this linear flow give
bounded weighted Sobolev seminorms on compact rapidity intervals.

Equivalently, in rapidity variables on the positive and negative mass shells,
boosts act by translation of rapidity together with the finite spinor
representation; translations preserve Schwartz seminorm boundedness on compact
parameter intervals. Uniform seam-tail decay follows from the resulting uniform
Schwartz bounds by choosing `R_a^{\rm ring}\to\infty` slowly enough compared
with the regulator.

This lemma is why the Route-B boost theorem is naturally a Schwartz or
weighted-Sobolev theorem. Boosts are not being assumed to preserve compact
equal-time support.

**Theorem 9.3: sampled finite-rapidity boost convergence.** Let

```math
B_a(\eta)=e^{-i\eta K_a},
\qquad
B(\eta)=e^{-i\eta K}.
```

Assume the hypotheses of Theorem 9.1 and the compact-rapidity orbit control of
Lemma 9.3a. Then

```math
\sup_{|\eta|\le\eta_0}
\|B_a(\eta)\iota_af-\iota_aB(\eta)f\|_{\ell^2_a}
\to0.
```

**Proof.** Duhamel's formula gives

```math
B_a(\eta)\iota_af-\iota_aB(\eta)f
=
-i\int_0^\eta
B_a(\eta-s)
\bigl(K_a\iota_a-\iota_aK\bigr)B(s)f\,ds
+r_a(\eta),
```

where `r_a` is the sampling/interpolation residual. The finite boosts are
unitary because `K_a` is self-adjoint on the finite regulator Hilbert space.
Theorem 9.1 applies uniformly to the bounded boosted orbit
`\{B(s)f:|s|\le\eta_0\}`. Hence the integral norm tends to zero uniformly on
the compact rapidity interval, and the residual tends to zero by the sampling
hypotheses.

This is still not exact finite Lorentz covariance. It is finite-rapidity
convergence of the regulator boost unitary on sampled smooth states.

## 9. Theorem 9.4: Polarization And CAR/Fock Boost Convergence

**Proposition 9.4a: asymptotic polarization intertwining and vacuum
invariance.** Let `P_{a,+}=1_{(0,\infty)}(H_a)` and
`P_+=1_{(0,\infty)}(H_D)`. Under the Route-B hypotheses, for every
`f\in\mathscr S(\mathbb R,\mathbb C^2)` and every compact rapidity interval,

```math
\sup_{|\eta|\le\eta_0}
\left\|
P_{a,+}B_a(\eta)\iota_af
-
B_a(\eta)P_{a,+}\iota_af
\right\|_{\ell^2_a}
\to0.
```

In the continuum,

```math
P_+B(\eta)=B(\eta)P_+.
```

**Proof.** In the standard massive continuum Dirac representation, boosts
preserve the positive-energy mass shell, so `P_+` commutes with `B(\eta)`. For
the finite expression, add and subtract the continuum sampled terms:

```math
\begin{aligned}
&P_{a,+}B_a(\eta)\iota_af-B_a(\eta)P_{a,+}\iota_af\\
&=
P_{a,+}(B_a(\eta)\iota_af-\iota_aB(\eta)f)\\
&\quad+
(P_{a,+}\iota_a-\iota_aP_+)B(\eta)f\\
&\quad+
(\iota_aB(\eta)P_+f-B_a(\eta)\iota_aP_+f)\\
&\quad+
B_a(\eta)(\iota_aP_+f-P_{a,+}\iota_af).
\end{aligned}
```

The first and third terms vanish uniformly in `\eta` by Theorem 9.3 applied to
`f` and `P_+f`. The second and fourth terms vanish by Paper 7 Proposition 12.2,
uniformly on the compact boosted orbit controlled by Lemma 9.3a. The finite
boosts and projections are norm-one operators, so no additional growth is
introduced.

Let `\omega_a` be the finite quasifree state determined by `P_{a,+}` and
`\omega_{\rm std}` the continuum quasifree vacuum determined by `P_+`. The
intertwining estimate implies that boosted finite two-point functions converge
to the standard boost-invariant two-point function:

```math
\omega_a\bigl(\beta_{a,\eta}(\psi_a(\iota_af)^*\psi_a(\iota_ag))\bigr)
\to
\omega_{\rm std}\bigl(\beta_\eta(\psi(f)^*\psi(g))\bigr)
=
\omega_{\rm std}\bigl(\psi(f)^*\psi(g)\bigr).
```

Thus finite vacuum invariance is asymptotic on sampled fields, while continuum
vacuum invariance is exact.

**Theorem 9.4: sampled CAR boost covariance.** Define the finite boost action on
sampled CAR generators by

```math
\beta_{a,\eta}(\psi_a(\iota_af))
=
\psi_a(B_a(\eta)\iota_af),
```

and the continuum boost action by

```math
\beta_\eta(\psi(f))=\psi(B(\eta)f).
```

For every fixed finite local field polynomial `B_{\rm poly}` built from
Schwartz test spinors and every compact rapidity interval,

```math
\omega_a(\beta_{a,\eta}(B_{{\rm poly},a}))
\to
\omega_{\rm std}(\beta_\eta(B_{\rm poly}))
```

uniformly for `|\eta|\le\eta_0`.

**Proof.** Theorem 9.3 gives convergence of every boosted one-particle test
function appearing in the fixed polynomial. The CAR norm bound
`\|\psi(f)\|\le\|f\|` controls the fixed words. Proposition 9.4a identifies the
finite boosted covariance with the continuum boost-invariant positive-energy
covariance in the limit. Fixed CAR `k`-point functions are finite
Wick/Pfaffian polynomials in the two-point covariance, so every fixed boosted
field-polynomial vacuum expectation converges uniformly on compact rapidity
intervals.

At finite `a`, the finite quasifree vacuum need not be exactly invariant under
`B_a(\eta)` because the lattice boost algebra has `C_a` corrections and possible
seam terms. The theorem claims convergence of boosted finite correlations, not
exact finite-regulator boost invariance.

The theorem is deliberately fixed-polynomial. It does not construct an
all-modes finite-lattice Fock-space boost representation and does not claim
operator-norm convergence of the quasilocal CAR algebra.

## 10. Theorem 9.5: Spacetime Local Net And Microcausality

### 10.1 Equal-Time Cauchy Data Versus Spacetime Support

There are two different notions of localization in this paper.

1. **Boost-convergence localization.** The Route-B boost theorems act on
   equal-time Cauchy data in Schwartz or weighted Sobolev spaces. A boosted
   equal-time Cauchy profile need not remain compactly supported on the same
   equal-time slice. Paper 9 therefore does not claim compact-support
   preservation for boosted Cauchy data.
2. **Spacetime-local QFT localization.** The local net is defined by compactly
   supported spacetime test functions `F\in C_c^\infty(\mathbb R^{1+1},
   \mathbb C^2)`. The free Dirac causal propagator maps these spacetime
   smearings to equal-time Cauchy data in the one-particle test domain.

The bridge is the free Dirac causal propagator `E_D`. If `F` is compactly
supported in a spacetime region `O`, define the corresponding Cauchy datum on
`t=0` by

```math
f_F=\rho_0 E_D F,
```

where `\rho_0` is restriction to the Cauchy surface. The field smeared over
spacetime is represented by the equal-time CAR field

```math
\psi(F)=\psi(f_F).
```

Thus compact spacetime locality lives in the support of `F`, while the sampled
boost convergence theorem lives on the resulting Cauchy data `f_F`. These are
compatible, but not the same statement.

**Theorem 9.5: spacetime local-net completion.** Under Paper 8 Theorem 8.5 and
Theorems 9.1-9.4, define the continuum spacetime free Dirac net by

```math
\mathcal A(O)
=
C^*\{\psi(F):\operatorname{supp}F\subset O\},
```

where spacetime smearing is identified with Cauchy data through the free Dirac
causal propagator. Then:

1. `\mathcal A(O)` restricts on equal-time regions to the Paper 8 CAR local
   net;
2. the net is isotonic;
3. the net is covariant under time translations, spatial translations, and
   boosts in the sampled regulator limit;
4. odd fields graded-commute at spacelike separation;
5. even local observables commute at spacelike separation;
6. detector protocols approximating even local observables in spacelike
   separated regions are order-independent at the standard free-QFT benchmark
   level.

**Proof.** First, the free Dirac equation is Green-hyperbolic. Its causal
propagator `E_D=E_D^{\rm ret}-E_D^{\rm adv}` sends compact spacetime test
functions to smooth solutions whose Cauchy data are in the one-particle test
domain used above. The assignment

```math
F\mapsto f_F=\rho_0E_DF
```

turns spacetime-smeared fields into equal-time CAR fields. If `O_1\subset O_2`,
then the generating test functions for `O_1` are a subset of those for `O_2`,
so isotony follows.

Second, Paper 8 identifies the equal-time CAR net and time evolution. Theorem
9.3 gives sampled boost convergence on the Cauchy-data side, while Theorem 9.4
lifts the boost convergence to fixed field-polynomial vacuum predictions.
Therefore the spacetime net is covariant under the declared time translations,
spatial translations, and sampled boost limit.

Third, the CAR relation for spacetime-smeared Dirac fields is controlled by the
causal pairing:

```math
\{\psi(F),\psi(G)^*\}
=
\langle F,E_DG\rangle.
```

If `\operatorname{supp}F` and `\operatorname{supp}G` are spacelike separated,
the support property of `E_D` gives

```math
\langle F,E_DG\rangle=0.
```

Thus odd fields graded-commute at spacelike separation. Even local polynomials
are built from an even number of odd generators, so the graded commutation law
reduces to ordinary commutation for even observables:

```math
[A,B]=0,
\qquad
A\in\mathcal A(O_1)_{\rm even},
\quad
B\in\mathcal A(O_2)_{\rm even},
```

whenever `O_1` and `O_2` are spacelike separated.

Finally, detector order-independence is an operational corollary only for
declared detector instruments whose effects approximate these even local
observables. It is not a statement that raw stochastic subprocesses factor or
commute without records.

This is a local-net theorem for the enriched continuum/free benchmark and its
sampled regulator approximants. It is not a Markov factorization theorem for
unrecorded stochastic subprocesses.

## 11. Theorem 9.6: Tested Tangential-Action Compatibility

Paper 1 and Paper 8 control a tested stochastic-curvature action:

```math
\delta_\xi^{\rm test}(\psi(f))=\psi(K_\parallel[\xi]f).
```

**Theorem 9.6: tangential local-net action matching.** On the common
finite-polynomial test domain,

```math
\omega_a(\delta_{a,N,M}B)
\to
\omega_{\rm std}(\delta_{\xi}^{\rm tangential}B),
\qquad
\xi=N\partial_xM-M\partial_xN,
```

and the limiting derivation is the standard infinitesimal tangential action on
the free Dirac local field algebra.

**Proof.** Paper 8 Theorem 8.4 already identifies the tested
stochastic-curvature response with the standard field-polynomial action
generated by `K_\parallel[\xi]`. The spacetime local-net completion of Theorem
9.5 identifies the same finite-polynomial domain as a domain in the standard
relativistic free Dirac net. Therefore the curvature response is compatible
with the standard tangential local-net action.

This does not reconstruct stress-energy, the full hypersurface-deformation
algebra, or metric structure functions. Paper 10 may use this theorem only as a
tangential-action input.

## 12. Wightman/AQFT Axiom Audit

Paper 9 includes a precise audit rather than a vague "Lorentz covariance
recovered" claim.

| Relativistic QFT Property | Status In Paper 9 |
| --- | --- |
| Time translations | matched from Paper 8 |
| Spatial translations | matched on sampled smooth sectors by the lattice shift/Fourier representation |
| Boosts | regulator boost approximants converge on sampled sectors by Theorems 9.1-9.3 |
| Poincare algebra | converges on sampled sectors; not exact at finite `a` |
| Spectrum condition | matched from the supplied positive-energy polarization |
| Vacuum invariance | exact in the standard continuum limit; finite-regulator invariance asymptotic by Proposition 9.4a |
| Equal-time CAR net | matched by Paper 8 |
| Spacetime local net | matched after causal-propagator completion in Theorem 9.5 |
| Spacelike graded locality | matched in Theorem 9.5 |
| Wightman distributions | matched for finite field-polynomial tests |
| Haag-Kastler net | matched for the standard free spacetime net on the declared benchmark, not reconstructed from Gamma alone |
| Reeh-Schlieder | may be cited as a standard theorem if needed, not derived from ISP data |
| Stress-energy | deferred |
| Metric extraction | deferred to Paper 10 |
| Interactions | deferred |

The key finite-regulator warning is:

```text
finite lattice boosts are approximants, not exact Lorentz symmetries.
```

## 13. Theorem 9.7: Final Route-B Relativistic Free-QFT Completion

**Theorem 9.7: sampled-sector Lorentz-covariant free-QFT completion.** Under
Paper 8 Theorem 8.5 and the Route-B boost hypotheses of Sections 5-9, the
enriched relativistic ISP free Dirac/CAR candidate matches standard massive
`1+1D` free Dirac/CAR QFT as a spacetime-covariant local theory on the declared
sampled/finite-polynomial sector.

The matching includes:

1. local field-polynomial vacuum correlations;
2. equal-time CAR local net;
3. time translations and positive energy;
4. sampled regulator convergence of finite boost approximants;
5. sampled Poincare commutator convergence;
6. asymptotic polarization/vacuum invariance;
7. boost covariance of finite local field-polynomial predictions in the limit;
8. spacetime local net and spacelike graded locality;
9. tested stochastic-curvature tangential response.

The matching excludes:

1. Gamma-only reconstruction;
2. exact finite-lattice Lorentz covariance;
3. all-mode finite-lattice Fock convergence;
4. stress-energy reconstruction;
5. metric extraction;
6. interacting QFT;
7. dynamical geometry.

**Proof.** Combine Paper 8 Theorem 8.5 with Theorems 9.1-9.6. Paper 8 supplies
the equal-time free-QFT match. Theorem 9.1 constructs sampled boost-generator
convergence. Theorem 9.2 identifies the continuum Poincare algebra as the
sampled limit of the lattice-corrected finite algebra. Theorem 9.3 upgrades
generator convergence to finite-rapidity boost convergence. Theorem 9.4 lifts
the boost convergence to the polarization/vacuum covariance level and then to
CAR field-polynomial predictions. Theorem 9.5 supplies
the spacetime net and microcausality. Theorem 9.6 identifies the tested
tangential action. The exclusions are exactly the structures not proved by
these steps.

## 14. Failure Modes

Paper 9 should fail cleanly if any of the following occur.

### Failure A: boost generator convergence fails

If

```math
K_a\iota_af\not\to \iota_aKf,
```

then Paper 9 can fall back to Route A, but it must label the result as standard
continuum completion rather than regulator-level ISP boost convergence. Metric
reconstruction would then have to cite only the weaker continuum-completion
fact, not a finite-regulator Lorentz theorem.

### Failure B: seam terms survive

If the nonperiodic coordinate `X_a` leaves nonvanishing periodic seam terms,
then the growing-volume/nonwrapping hypothesis is insufficient. The boost
commutator identities become regulator-artifact dependent, and the Route-B
boost theorem is not stable. The cure would be either an infinite-lattice-first
proof with a separate thermodynamic limit or a better finite-volume coordinate
regularization.

### Failure C: doubler leakage enters boosted states

The central-difference Dirac lift has high-momentum branches. If
`B_a(\eta)` moves sampled low-momentum states into doubler sectors at nonvanishing
weight, then the sampled boost theorem fails even if time-evolution convergence
survives. In that case Paper 9 must add a Wilson/admissible doubler-control lift
or restrict the theorem to a rigorously invariant low-energy sector.

### Failure D: weighted domain is too narrow

If the theorem works only on Schwartz Cauchy data and cannot be connected to
compact spacetime smearings through the causal propagator, then Paper 9 proves a
boost-domain theorem but not a local-QFT theorem. Section 10.1 is the bridge
that must remain valid: compact spacetime support is carried by `F`, while
boost convergence is controlled on `f_F=\rho_0E_DF`.

### Failure E: finite polarization fails asymptotically

If

```math
P_{a,+}B_a(\eta)\iota_af
-
B_a(\eta)P_{a,+}\iota_af
\not\to0,
```

then the finite boost action does not preserve the finite quasifree vacuum even
asymptotically. The CAR/Fock boost theorem then fails at the sampled vacuum
level, and Paper 9 cannot claim boosted local field-polynomial predictions
match standard free QFT.

### Failure F: detector protocols are not phase-complete

The operational order-independence statement in Theorem 9.5 applies only to
declared detector instruments approximating even local QFT observables. If a
protocol sees only endpoint-basis `Gamma` data, Paper 6 and Paper 7
counterexamples apply: it need not detect the phase/polarization/local-net data
required for Lorentz-covariant QFT matching.

### Failure G: stochastic curvature does not match tangential action

If the Paper 1/Paper 8 stochastic-curvature generator does not match the
standard tangential local-net action, then Paper 10 cannot use Paper 9 as a
metric-data input. The program would still have a free-QFT matching theorem, but
not a bridge from stochastic exchange curvature to the hypersurface-deformation
structure.

## 15. Paper 10 Export Box

Paper 10 may use:

1. Paper 8's sampled free-QFT matching theorem;
2. Theorem 9.7: sampled-sector Lorentz-covariant free-QFT completion;
3. finite-regulator boost approximants converging to standard boosts on
   sampled smooth sectors;
4. sampled Poincare commutator convergence with lattice correction `C_a`;
5. asymptotic finite polarization/vacuum invariance;
6. the spacetime local-net and microcausality audit;
7. the tested tangential-action match.

Paper 10 may not use:

1. metric extraction;
2. stress-energy reconstruction;
3. interacting QFT;
4. dynamical geometry;
5. exact finite-lattice Lorentz covariance;
6. all-mode finite-lattice Fock convergence.

The export is also topology-sensitive. Paper 10 may use compact spacetime test
functions for the local-net side,

```math
F\in C_c^\infty(\mathbb R^{1+1},\mathbb C^2),
```

and may use their Cauchy data

```math
f_F=\rho_0E_DF
```

inside the weighted Schwartz/Sobolev boost domain. It may not silently replace
these two domains by an unspecified completed test-function space. Any stronger
completion, such as a full Wightman-distribution topology or an all-mode
quasilocal CAR completion, is a later analytic theorem rather than a Paper 9
export.

## 16. Initial Work Plan

1. Choose Route B as the primary target. Done in Section 5.
2. Define finite boost generators `K_a`. Done in Section 5.
3. Add the weighted domain and nonwrapping/seam policy. Done in Section 5.1.
4. Derive the finite commutator identities. Done in Section 5.2.
5. Prove sampled boost-generator convergence with explicit weighted estimates.
   Done in Section 6.
6. Prove sampled Poincare commutator convergence. Done in Section 7.
7. Prove finite-rapidity boost convergence with compact-rapidity orbit control.
   Done in Section 8.
8. Prove asymptotic polarization/vacuum invariance. Done in Section 9.
9. Lift boosts to CAR/Fock local field polynomials. Done in Section 9.
10. Build the spacetime CAR net and microcausality theorem. Done in Section 10.
11. Match the tested stochastic-curvature tangential action. Done in Section 11.
12. Add the Wightman/Haag-Kastler audit. Done in Section 12.
13. State the final Route-B completion theorem. Done in Section 13.
14. Export only these facts to Paper 10. Done in Section 15.

## 17. Completion Gate And Readiness For Paper 10

Paper 9 is complete enough for Paper 10 only in the following precise sense.

### Theorem status ledger

| Item | Paper 9 Status | Remaining Limitation |
| --- | --- | --- |
| Finite boost generator | Constructed as `K_a=(X_aH_a+H_aX_a)/2`. | Depends on low-momentum sampling, weighted domains, and seam control. |
| Poincare algebra | Recovered on sampled sectors as `C_a=\cos(aP)` tends to `I`. | Not exact at finite lattice spacing. |
| Finite rapidity boosts | Converge on compact rapidity intervals for sampled smooth data. | No all-mode Fock-space convergence theorem. |
| Polarization/vacuum | Asymptotically intertwined on sampled test fields. | Finite quasifree vacuum need not be exactly boost invariant. |
| Spacetime net | Built with compact spacetime smearings and the Dirac causal propagator. | It is the standard free net transported through the enriched representation, not reconstructed from `Gamma` alone. |
| Microcausality | Holds for the free spacetime net and even detector approximants. | Does not imply stochastic Markov factorization through unrecorded intermediate cuts. |
| Tangential curvature action | Matched on the common finite-polynomial domain. | Does not reconstruct stress-energy or metric structure functions. |

### Test-function decision

Paper 9 deliberately uses two test-function levels.

1. Boost convergence is proved on Schwartz or weighted Sobolev equal-time
   Cauchy data. This is the correct domain for `K`, `K_a`, and compact-rapidity
   orbit estimates.
2. Local QFT is stated with compact spacetime test functions
   `C_c^\infty(\mathbb R^{1+1},\mathbb C^2)`. The causal propagator maps these
   smearings into the boost domain through `f_F=\rho_0E_DF`.

This is enough for the declared finite-polynomial spacetime-local benchmark.
It is not a claim of full Wightman-space reconstruction, nuclear-test-space
reconstruction, or quasilocal CAR norm convergence from finite stochastic data.

### Paper 10 readiness condition

Paper 10 may start only as a metric-data gate. It may cite Paper 9 for:

```text
sampled Lorentz-covariant free-QFT matching
+ spacetime local-net/microcausality benchmark
+ tested tangential-action compatibility.
```

It may not cite Paper 9 for:

```text
metric, stress-energy, dynamical geometry, exact finite Lorentz symmetry,
interacting QFT, or Gamma-only QFT reconstruction.
```

Thus Paper 10's first legitimate question is not "what metric has Paper 9
found?" but:

> Given the tested tangential exchange-curvature action now placed inside a
> Lorentz-covariant free-QFT benchmark, can the coefficient of the
> multi-dimensional tangential vector field satisfy the independent criteria
> required to be inverse spatial metric data?

## 18. Current Verdict

Paper 9 now attempts the stronger Barandes-aligned route: finite enriched ISP
boost approximants are constructed and shown, conditionally, to converge to the
standard Dirac boost on sampled sectors.

The strongest honest claim is:

> enriched relativistic ISP, with the Paper 7/8 lift, polarization, and CAR
> data, reproduces standard massive `1+1D` Lorentz-covariant free Dirac/CAR QFT
> on sampled finite-polynomial tests, including sampled regulator convergence of
> boost approximants.

The central caution remains:

> this is not exact finite-lattice Lorentz covariance and not Gamma-only QFT
> reconstruction.
