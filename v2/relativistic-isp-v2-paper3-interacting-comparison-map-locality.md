# Quasilocality and Inverse Control for Interacting ISP Comparison Maps

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

V2 Paper 3 consolidated draft

Date: 2026-05-13

Status: theorem-framework and no-go draft. This paper continues the V2 sequence after the free stochastic-curvature theorem and the projective hypersurface-kernel framework. It proves a global-norm obstruction, records the fixed finite inverse theorem that the current benchmark stack already supports, and isolates the exact local inverse hypothesis needed to turn interacting finite-range dynamics into regulator-stable comparison-map and exchange-defect control.

## Abstract

Relativistic ISP uses exact stochastic endpoint kernels, localized comparison maps, and exchange defects rather than infinitesimal Markov generators. In the free one-particle benchmark, these objects have a controlled stochastic-curvature limit. In the projective framework, refinement errors propagate through `Gamma_0^{-1}`, `J_R`, and `J_R^{-1}`. The first interacting viability question is therefore not whether the Hamiltonian is local, but whether the Born-squared kernels and their algebraic inverses preserve locality in a topology suitable for refinement.

This paper makes that question precise. First, we show by an explicit product benchmark that global matrix-norm inverse control is the wrong continuum-facing criterion: even independent on-site dynamics force `\|\Gamma_0(\Delta)-I\|` to grow like volume for small `Delta`, so a global Neumann argument requires `Delta^2|\Lambda| << 1`. Second, we show in exact product and finite-depth circuit laboratories that the same large exterior inverse can cancel exactly in the relative map `J_R`. Third, we build an anchored tree-polymer algebra and prove fixed-order LC-log locality. Fourth, for bounded finite-range Hamiltonians with uniformly finite local dimension and a common-support anchored collar deformation, we prove a paired-word Born-squared activity theorem; the resulting KP bounds imply finite-slab LC-log locality. Fifth, we record the fixed finite inverse theorem available on every finite benchmark and explain why it is insufficient by itself for V2. Sixth, we define anchored quasilocal inverse-control consequences under which `J_R`, `J_R^{-1}`, and `E_{R,S}` obey local support/window bounds and inherit Paper 2 projective refinement compatibility. Seventh, we prove the corresponding sectorwise theorem for invariant common-collar fibers, with uniform constants only over explicitly named sector families.

The main finite-slab result is positive within that bounded finite-range/common-collar class. The paper recasts inverse locality as a relative/cumulant problem: prove convergent locality of the connected logarithmic defect `log J_R`, then `J_R`, `J_R^{-1}`, and exchange-defect locality follow by local algebra. The paired-word activity theorem supplies the needed coefficient-majorant estimates: connected logarithmic coefficients grow at most exponentially in order, uniformly in total volume. Outside the finite-local-dimension common-collar class, especially in reduced nonlocal gauge coordinates or cutoff-removal limits, the theorem remains a named hypothesis rather than an automatic consequence of Hamiltonian locality.

## 1. Scope And Non-Claims

Established here:

1. global matrix norms are too strong for continuum-facing interacting inverse control;
2. exact product and finite-depth circuit laboratories satisfy linked-cluster cancellation exactly;
3. pure diagonal interactions are invisible to primitive `Gamma` kernels unless combined with local moves;
4. the logarithmic/cumulant defect `L_R=\log J_R` is the cleanest proof target for linked-cluster cancellation;
5. an anchored tree-polymer algebra gives a concrete Banach-algebra topology for relative defects;
6. LC-log locality holds at every fixed formal order for bounded finite-range Hamiltonians;
7. finite-slab LC-log locality holds for bounded finite-range Hamiltonians with uniformly finite local dimension and common-support anchored collar deformations, by a paired-word activity/KP theorem;
8. fixed finite inverse control follows from finite-dimensional analyticity but has volume/cutoff-dependent constants;
9. anchored or cylinder-effect topologies are the right candidates for interacting comparison-map locality;
10. if `J_R-I` has anchored quasilocal control, then `J_R^{-1}-I` has the same type of control by a local Neumann argument;
11. if comparison maps and their inverses are anchored quasilocal, then exchange defects obey two-anchor corridor/window bounds with exponential tails and separated-support onset;
12. Paper 2's refinement theorem transfers to interacting systems only in the same local topology in which inverse control is proved;
13. gauge-sector variants hold sectorwise for invariant common-collar fibers,
    with uniform constants only over explicitly named sector families.

Not established here:

1. finite-slab convergent linked-cluster control beyond the bounded finite-range, uniformly finite local-dimension, common-collar class proved here;
2. volume-independent inverse control in ordinary global matrix norms;
3. `K -> infinity` compact-rotor control for truncated compact `U(1)`;
4. interacting stochastic curvature;
5. operational observable reconstruction;
6. continuum QFT reconstruction;
7. Lorentz covariance, non-Abelian gauge theory, metric reconstruction, or gravity.

This paper is therefore an inverse-locality gate. It tells later papers exactly what must be proved before interacting ISP can be treated as a continuum-directed relativistic dynamics.

## 2. Dependency Ledger

The paper uses the following V2 and finite-benchmark inputs.

1. V2 Paper 1 proves a free one-particle stochastic-curvature theorem.
2. V2 Paper 2 proves projective naturality and the error identity

```math
P_1J_R^{a'}-J_R^aP_1
=
(R_R-J_R^aR_0)(A^{a'})^{-1}.
```

3. The dynamical Abelian finite-link benchmark proves sectorwise fixed finite inverse control and a mixed quasilocal coefficient filtration at fixed lattice size and fixed link cutoff.
4. The finite `Z_2` and truncated compact `U(1)` gauge-matter benchmarks prove exact interacting reduced blocks and first interaction-sensitive exchange coefficients.
5. The reduced-strip companion papers organize finite coefficient channels but do not provide volume/cutoff-stable inverse control.

The conclusion is already visible: finite exactness is real, but V2 Paper 3 needs local analytic estimates stable under regulator growth.

## 3. Setup

Let `Lambda` be a finite bounded-degree graph or cell complex. In the unconstrained case, the configuration set is

```math
C_\Lambda=\prod_{x\in\Lambda}C_x,
```

with uniformly finite local configuration spaces. In gauge systems one should use the full matter-link configuration space, or else a center-resolved physical sector. Reduced matter-only coordinates after Gauss-law elimination may be useful for coefficient calculations, but they are often nonlocal and should not be the primitive locality arena.

Let the Hamiltonian be a bounded finite-range sum

```math
H_\Lambda=\sum_{X\subset\Lambda}h_X,
```

with:

1. `diam(X)<=r`;
2. `\|h_X\|\le J`;
3. each cell belongs to at most `b` interaction supports;
4. local dimension bounded independently of `|\Lambda|`;
5. sector or center labels fixed when constraints are present.

For a support region `R`, let `C_R` be the collar term associated with the localized deformation and set

```math
H_{R,\Lambda}=H_\Lambda-C_R.
```

The primitive kernels are

```math
\Gamma_0^\Lambda(\Delta)
=
\left|e^{-i\Delta H_\Lambda}\right|^2,
\qquad
\Gamma_R^\Lambda(\Delta)
=
\left|e^{-i\Delta H_{R,\Lambda}}\right|^2,
```

where absolute value is entrywise squared modulus in the chosen configuration basis. When `\Gamma_0^\Lambda(\Delta)` is invertible, define

```math
J_R^\Lambda(\Delta)
=
\Gamma_R^\Lambda(\Delta)
\left(\Gamma_0^\Lambda(\Delta)\right)^{-1}.
```

`J_R` preserves normalization but is generally pseudo-stochastic, not stochastic.

## 4. Global Matrix Norms Fail As A Continuum Criterion

### Proposition 1: volume obstruction for global Neumann control

Consider `N` independent two-state cells with Hamiltonian

```math
H_N=g\sum_{x=1}^N\sigma_x^{(x)}.
```

In the product configuration basis, the one-cell primitive kernel is

```math
T(\Delta)=
\begin{pmatrix}
\cos^2(g\Delta)&\sin^2(g\Delta)\\
\sin^2(g\Delta)&\cos^2(g\Delta)
\end{pmatrix},
```

and the `N`-cell primitive kernel is

```math
\Gamma_N(\Delta)=T(\Delta)^{\otimes N}.
```

In the induced column-sum norm,

```math
\|\Gamma_N(\Delta)-I\|_1
=
2\left(1-\cos^{2N}(g\Delta)\right)
=
2Ng^2\Delta^2+O(N^2\Delta^4)
```

whenever `N\Delta^2` is small. Therefore a global Neumann-series condition

```math
\|\Gamma_N(\Delta)-I\|_1<1
```

forces `N\Delta^2=O(1)`.

Moreover, whenever `\cos(2g\Delta)\ne0`,

```math
\left\|\Gamma_N(\Delta)^{-1}\right\|_1
=
\left|\cos(2g\Delta)\right|^{-N}
=
\exp\left(2Ng^2\Delta^2+O(N\Delta^4)\right)
```

for small `Delta`. Thus the actual global inverse norm also grows with volume unless `N\Delta^2` is controlled.

Proof. For each input configuration, the probability of no bit flip is `\cos^{2N}(g\Delta)`. The column of `\Gamma_N-I` therefore has negative diagonal mass `1-\cos^{2N}(g\Delta)` and the same total positive off-diagonal mass. The column-sum norm is twice that quantity. For the inverse, the one-site inverse has column-sum norm `|\cos(2g\Delta)|^{-1}`, and tensor-product multiplicativity of the induced column-sum norm gives the `N`th power. Taylor expansion gives the displayed small-`Delta` behavior. `square`

This example is not interacting, which makes the obstruction stronger. If global norms already fail for independent local dynamics, they are not the correct topology for an interacting continuum theorem.

## 5. First-Principles Meaning Of Hypothesis LC

The global inverse obstruction does not mean locality is impossible. It means the wrong object has been normed. The local object is not the reference inverse by itself; it is the relative deformation

```math
J_R=\Gamma_R\Gamma_0^{-1}.
```

This is the stochastic-kernel analogue of a Radon-Nikodym derivative or a relative Gibbs weight. A Gibbs measure on a large lattice can have a partition function that grows exponentially with volume, but the ratio of two Gibbs weights whose actions differ only in a local region is local. The same first-principles idea should guide Paper 3: exterior reference propagation may be large globally, but it should cancel in the relative map if it is not linked to the collar where `H_R` differs from `H`.

There are three complementary ways to view Hypothesis LC.

1. **Relative-law view.** `J_R` compares two endpoint laws that differ only by a local deformation. It should measure the local response to that deformation, not the absolute size of the full reference law.
2. **Connected-cluster view.** Terms in `J_R-I` should be connected to the collar. Disconnected vacuum/reference pieces should cancel between `\Gamma_R` and `\Gamma_0^{-1}`.
3. **Logarithmic cumulant view.** The clean object may be

```math
L_R:=\log J_R.
```

If `L_R` is an anchored quasilocal element, then

```math
J_R=e^{L_R},
\qquad
J_R^{-1}=e^{-L_R},
```

and exchange defects can be analyzed by the Baker-Campbell-Hausdorff expansion

```math
\log E_{R,S}
=
[L_R,L_S]
+\frac12[L_R+L_S,[L_R,L_S]]
+\cdots .
```

This is the exact analogue of connected diagrams in perturbation theory. Hypothesis LC should therefore be attacked either directly for `J_R-I` or, more naturally, for the connected logarithmic defect `L_R`.

## 6. Concrete Laboratories For Hypothesis LC

The following simple scenarios are not substitutes for the full interacting theorem. They are laboratories that identify the cancellation mechanism.

### Proposition 2: exact product cancellation

Suppose the configuration space factors as

```math
C=C_A\times C_B,
```

and the reference and localized kernels factor as

```math
\Gamma_0=\Gamma_A\otimes\Gamma_B,
\qquad
\Gamma_R=\Gamma_A^R\otimes\Gamma_B,
```

with `\Gamma_A` and `\Gamma_B` invertible. Then

```math
J_R
=
\Gamma_R\Gamma_0^{-1}
=
\left(\Gamma_A^R\Gamma_A^{-1}\right)\otimes I_B.
```

Thus the exterior inverse cancels exactly, even if `\|\Gamma_B^{-1}\|` is very large in a global norm.

Proof. Use `(X\otimes Y)^{-1}=X^{-1}\otimes Y^{-1}`:

```math
(\Gamma_A^R\otimes\Gamma_B)
(\Gamma_A^{-1}\otimes\Gamma_B^{-1})
=
(\Gamma_A^R\Gamma_A^{-1})\otimes I_B.
```

`square`

This proposition is the simplest mathematical picture of Hypothesis LC. The problem is not that `\Gamma_0^{-1}` is globally harmless; it is not. The problem is to prove that the nonlocal exterior part cancels in the relative map.

### Warning: the primitive difference need not be anchored

The same product example also shows why a tempting proof strategy fails. In the setting of Proposition 2,

```math
\Gamma_R-\Gamma_0
=
(\Gamma_A^R-\Gamma_A)\otimes\Gamma_B
=
(\Gamma_A^R-\Gamma_A)\otimes I_B
+
(\Gamma_A^R-\Gamma_A)\otimes(\Gamma_B-I_B).
```

If `B` is far from `R` and `\Gamma_B-I_B=O(\Delta^2)`, the second term contains far-away exterior transitions at order `O(\Delta^4)`. Thus `\Gamma_R-\Gamma_0` is not anchored-local in the naive entrywise sense, even though

```math
J_R
=
(\Gamma_A^R\Gamma_A^{-1})\otimes I_B
```

is exactly anchored-local. The proof of Hypothesis LC therefore cannot rest on primitive-difference support alone. It must use relative cancellation, equivalently a connected-cluster or logarithmic-cumulant argument.

### Proposition 3: finite-depth circuit light-cone cancellation

Consider a finite-depth local circuit representation of the endpoint unitary. Suppose the localized deformation modifies only gates whose circuit light cone is contained in a finite cell region `\mathcal C_d(R)`. After grouping degrees of freedom into the cone and its complement, assume the reference and localized unitaries factor as

```math
U_0=U_{\mathcal C}\otimes U_{\mathcal C^c},
\qquad
U_R=U_{\mathcal C}^R\otimes U_{\mathcal C^c}.
```

Then the primitive kernels factor in the same way,

```math
\Gamma_0=\Gamma_{\mathcal C}\otimes\Gamma_{\mathcal C^c},
\qquad
\Gamma_R=\Gamma_{\mathcal C}^R\otimes\Gamma_{\mathcal C^c},
```

and

```math
J_R
=
\left(\Gamma_{\mathcal C}^R\Gamma_{\mathcal C}^{-1}\right)
\otimes I_{\mathcal C^c}.
```

Therefore Hypothesis LC holds exactly with support inside the circuit light cone.

Proof. A tensor-factorized unitary has entrywise squared-modulus kernel equal to the tensor product of the factor kernels. Proposition 2 then applies. `square`

This is the most useful clean circuit laboratory. A generic Trotterized finite-range Hamiltonian has finite-depth local circuit approximants, but it need not factor across the cone boundary without a buffer or an additional cancellation argument.

Barandes/ISP caveat. This proposition is a representation-level endpoint
factorization laboratory. It does not say that the stochastic process is
Markov-divisible through each circuit layer. The allowed product is either a
tensor factorization of the whole endpoint lift after grouping cone and exterior
degrees of freedom, or a declared circuit approximation used as an auxiliary
proof device before taking the endpoint Born-squared kernel. It must not be
read as permission to compose arbitrary partial stochastic shadows through
unrecorded intermediate stages.

The possible proof route for the full finite-slab theorem is:

1. prove exact LC for buffered factorized circuit approximants, or prove a circuit-level anchored LC estimate for generic Trotter approximants;
2. establish anchored-norm convergence of the approximants to the continuous-time primitive kernels;
3. pass the local cancellation to the limit.

The third step is exactly where a real proof must control interference and the Born-squared projection.

### Proposition 4: pure diagonal interactions are Gamma-invisible

If `H=D` is diagonal in the configuration basis, then

```math
e^{-i\Delta D}_{c',c}
=
e^{-i\Delta D(c)}\delta_{c',c},
```

so

```math
\Gamma_0(\Delta)=I.
```

If a localized deformation only changes the diagonal interaction, then also `\Gamma_R(\Delta)=I`, hence

```math
J_R=I,
\qquad
E_{R,S}=I.
```

Proof. Entrywise squared modulus removes diagonal phases. `square`

This explains a feature of the finite interacting gauge benchmarks: interaction-sensitive coefficients appear only when diagonal interaction data are sampled by local moves or hopping paths. The interaction enters through local path gaps, not through diagonal phases alone.

### Path picture for local hopping plus diagonal interaction

For Hamiltonians of the schematic form

```math
H=T+V,
```

where `T` is a sum of finite-range local moves and `V` is a finite-range diagonal interaction, a Dyson word contributing to an amplitude from `c` to `c'` is a path in configuration space. Each off-diagonal `T` changes configuration only locally, and each diagonal `V` decorates an intermediate configuration by a local energy. If no path segment enters the collar where `H_R` differs from `H`, then the corresponding word is identical in the reference and localized dynamics.

Thus every reference/localized difference word contains at least one collar-linked component. But, as the product warning shows, disconnected exterior reference components may accompany that collar component in `\Gamma_R-\Gamma_0`. The remaining question is exactly whether those disconnected exterior pieces cancel in the relative object. The logarithmic/cumulant formulation says what must happen: disconnected path pieces should exponentiate and cancel, leaving only connected collar-linked polymers.

This path picture is the closest first-principles route to proving Hypothesis LC in realistic interacting benchmarks.

## 7. Fixed Finite Inverse Control

### Theorem 1: fixed finite analytic inverse control

For every fixed finite configuration space, fixed sector block, and fixed localized support `R`, there exists `Delta_*(R,\Lambda)>0` such that, for `|\Delta|<Delta_*`,

```math
\Gamma_0^\Lambda(\Delta),\quad
J_R^\Lambda(\Delta),\quad
\left(J_R^\Lambda(\Delta)\right)^{-1}
```

exist and are finite matrices with finite norm bounds.

Moreover, for any chosen finite family of sector blocks, one may choose `Delta_*` and constants uniformly over that finite family.

Proof. At `Delta=0`, both primitive kernels are the identity matrix. Their entries are real analytic in `Delta`, and the Born-squared form removes the linear term:

```math
\Gamma_0^\Lambda(\Delta)=I+O(\Delta^2),
\qquad
\Gamma_R^\Lambda(\Delta)=I+O(\Delta^2).
```

In any fixed finite matrix norm, these estimates imply invertibility by a Neumann argument for sufficiently small `Delta`. Since a finite sector family has only finitely many finite matrices, the minimum of the allowed neighborhoods and the maximum of the constants give a common finite-family bound. `square`

This theorem explains why the existing fixed finite benchmarks are legitimate. It also explains why they are not enough: `Delta_*` and the constants may shrink or grow with volume, cutoff, support size, or sector family.

## 8. Anchored Quasilocal Topology

For configurations `c,c'`, define the changed-cell set

```math
\operatorname{chg}(c,c')
=
\{x\in\Lambda:c_x\ne c'_x\}.
```

For a region `R`, define

```math
d_R(c,c')
=
\operatorname{dist}(\operatorname{chg}(c,c'),R),
\qquad
d_R(c,c)=0.
```

A simple anchored entrywise norm for a map `K` is

```math
\|K\|_{\mu,R}^{(1)}
=
\sup_c\sum_{c'}|K_{c',c}|e^{\mu d_R(c,c')}.
```

This norm is useful for detecting tails, but it may still be too crude for many-body finite-slab products because disconnected extensive changes can accumulate. The more robust object is an admissible anchored quasilocal norm `\|\cdot\|_{\mathcal A_{\mu,R}}` with the following properties:

1. it is a Banach algebra norm on anchored pseudo-stochastic defects;
2. if `K` is supported in `N_\ell(R)`, then `\|K\|_{\mathcal A_{\mu,R}}` is finite with constants depending on `\ell`, local dimension, and bounded degree but not on total volume;
3. products of anchored defects have support growth controlled by the sum of their radii;
4. exponential tails remain exponential under products, possibly with a smaller decay rate;
5. sectorwise or center-resolved restrictions inherit the same norm properties.

Paper 3 does not need a unique canonical choice at this stage. It needs a topology with these properties and a proof that the ISP comparison maps live in it.

### Concrete candidate: anchored tree-polymer norm

The cleanest candidate for item 3 is not the entrywise norm alone, but a polymer norm that charges disconnected exterior pieces for the tree needed to connect them back to the collar.

Let `R_*` denote the collar where `H_R` differs from `H`, together with a fixed bounded connecting scaffold if `R_*` has several components. For genuinely disconnected supports one can equivalently use one anchored norm per component. A map `K_X` is supported in a finite cell set `X` if

```math
(K_X)_{c',c}=0
\quad\text{unless}\quad
c'|_{X^c}=c|_{X^c},
```

and its value depends only on `c|_X` and `c'|_X`. For defects one also imposes zero column sums. Let `\|K_X\|_{1,X}` be the induced column-sum norm of the corresponding local matrix on `C_X`.

For a finite set `X`, define `\ell_R(X)` as the extra graph length of the smallest connected cell subgraph containing `X\cup R_*`, beyond the fixed scaffold for `R_*`; set `\ell_R(\emptyset)=0`. For a defect `K`, define

```math
\|K\|_{\mu,R}^{\mathrm{tree}}
=
\inf_{K=\sum_X K_X}
\sum_X e^{\mu\ell_R(X)}\|K_X\|_{1,X},
```

where the infimum is over local decompositions into supported defects.

This norm has the right diagnostic behavior:

1. if `K` is supported in `N_\ell(R_*)` for bounded `R_*`, then `\|K\|_{\mu,R}^{\mathrm{tree}}` is bounded by a constant depending on `\ell`, local dimension, bounded degree, and the fixed scaffold size, not on total volume;
2. a disconnected exterior factor at distance `d` from `R_*` pays at least `e^{\mu d}`;
3. if `K_X` and `L_Y` are local pieces, then `K_XL_Y` is supported in `X\cup Y` and

```math
\ell_R(X\cup Y)\le \ell_R(X)+\ell_R(Y),
```

so the norm is submultiplicative after adjoining the identity:

```math
\|KL\|_{\mu,R}^{\mathrm{tree}}
\le
\|K\|_{\mu,R}^{\mathrm{tree}}\|L\|_{\mu,R}^{\mathrm{tree}}.
```

This is the topology in which the product warning is visible: `\Gamma_R-\Gamma_0` may fail the tree norm because it contains uncancelled exterior factors, while `J_R-I` may still satisfy it after relative cancellation.

For the reference logarithm `W_0=\log\Gamma_0`, one should use the matching bulk polymer norm

```math
\|W\|_{\mu}^{\mathrm{bulk}}
=
\sup_{x\in\Lambda}
\inf_{W=\sum_X W_X}
\sum_{X\ni x} e^{\mu\operatorname{diam}(X)}\|W_X\|_{1,X}.
```

The intended LC-log theorem should therefore be stated with `W_0` controlled in the bulk norm and `D_R`, `L_R` controlled in the anchored tree norm.

### Proposition 5: tree-polymer Banach algebra calculus

Fix a finite regulator `\Lambda`, bounded local dimensions, bounded degree, and a bounded collar scaffold `R_*`. Let `\mathfrak P_{\mu,R}` be the weighted direct sum of local zero-column-sum pieces

```math
\mathfrak P_{\mu,R}
=
\left\{(K_X)_X:
\sum_X e^{\mu\ell_R(X)}\|K_X\|_{1,X}<\infty\right\}.
```

Let

```math
\pi((K_X)_X)=\sum_X K_X
```

be the induced global defect. Define the anchored tree-polymer defect space as the quotient

```math
\mathcal A_{\mu,R}^{\mathrm{tree}}
=
\mathfrak P_{\mu,R}/\ker\pi
```

with the quotient norm. Then `\mathcal A_{\mu,R}^{\mathrm{tree}}` is a Banach algebra under composition of defects, and the norm agrees with the infimum formula above.

After adjoining the identity,

```math
\mathcal A_{\mu,R}^{\mathrm{tree},+}
=
\mathbb R I\oplus\mathcal A_{\mu,R}^{\mathrm{tree}},
\qquad
\|\alpha I+K\|_+
=
|\alpha|+\|K\|_{\mu,R}^{\mathrm{tree}},
```

the following estimates hold:

1. if `\|K\|_{\mu,R}^{\mathrm{tree}}<1`, then

```math
(I+K)^{-1}-I
=
\sum_{n\ge1}(-K)^n,
\qquad
\|(I+K)^{-1}-I\|_{\mu,R}^{\mathrm{tree}}
\le
\frac{\|K\|_{\mu,R}^{\mathrm{tree}}}
{1-\|K\|_{\mu,R}^{\mathrm{tree}}};
```

2. if `L\in\mathcal A_{\mu,R}^{\mathrm{tree}}`, then

```math
e^L-I\in\mathcal A_{\mu,R}^{\mathrm{tree}},
\qquad
\|e^L-I\|_{\mu,R}^{\mathrm{tree}}
\le e^{\|L\|_{\mu,R}^{\mathrm{tree}}}-1;
```

3. if `\|K\|_{\mu,R}^{\mathrm{tree}}<1`, then

```math
\log(I+K)
=
\sum_{n\ge1}\frac{(-1)^{n+1}}{n}K^n
\in
\mathcal A_{\mu,R}^{\mathrm{tree}},
```

with

```math
\|\log(I+K)\|_{\mu,R}^{\mathrm{tree}}
\le
-\log(1-\|K\|_{\mu,R}^{\mathrm{tree}});
```

4. for `K,L\in\mathcal A_{\mu,R}^{\mathrm{tree}}`,

```math
\|[K,L]\|_{\mu,R}^{\mathrm{tree}}
\le
2\|K\|_{\mu,R}^{\mathrm{tree}}\|L\|_{\mu,R}^{\mathrm{tree}}.
```

Proof. The weighted direct sum `\mathfrak P_{\mu,R}` is complete. The quotient by `\ker\pi` is therefore complete, and its quotient norm is exactly the infimum over local decompositions. If `K_X` and `L_Y` are local pieces, then `K_XL_Y` is supported in `X\cup Y`, and the local column-sum norm is submultiplicative:

```math
\|K_XL_Y\|_{1,X\cup Y}
\le
\|K_X\|_{1,X}\|L_Y\|_{1,Y}.
```

The tree length is subadditive,

```math
\ell_R(X\cup Y)\le \ell_R(X)+\ell_R(Y),
```

so summing over decompositions gives

```math
\|KL\|_{\mu,R}^{\mathrm{tree}}
\le
\|K\|_{\mu,R}^{\mathrm{tree}}
\|L\|_{\mu,R}^{\mathrm{tree}}.
```

The inverse, exponential, logarithm, and commutator estimates are the standard Banach-algebra series estimates in the unitization. `square`

This proposition closes the abstract algebraic part of item 3. What remains nontrivial is not the algebra calculus; it is proving that the actual Born-squared comparison objects have finite tree-polymer norm with regulator-stable constants.

### Proposition 6: bulk-local generators act on anchored defects

The LC-log proof also needs a mixed estimate, because `W_0=\log\Gamma_0` is bulk-local rather than anchored at `R`.

Let `0<\nu<\mu`. Suppose a bulk-local map `W` has finite bulk norm `\|W\|_{\mu}^{\mathrm{bulk}}`, and an anchored defect `D` has finite tree norm `\|D\|_{\mu,R}^{\mathrm{tree}}`. Then there is a constant

```math
C_{\mu,\nu,b,d_{\mathrm{loc}},R_*}<\infty
```

depending on the decay loss, graph degree, local dimension bound, and fixed collar scaffold, but not on total volume, such that

```math
\|[W,D]\|_{\nu,R}^{\mathrm{tree}}
\le
C_{\mu,\nu,b,d_{\mathrm{loc}},R_*}
\|W\|_{\mu}^{\mathrm{bulk}}
\|D\|_{\mu,R}^{\mathrm{tree}}.
```

Consequently, every nested commutator containing at least one anchored factor remains anchored, with a possible loss of exponential rate.

The same overlapping-support proof gives the companion bulk estimate

```math
\|[W,W']\|_{\nu}^{\mathrm{bulk}}
\le
C_{\mu,\nu,b,d_{\mathrm{loc}}}
\|W\|_{\mu}^{\mathrm{bulk}}
\|W'\|_{\mu}^{\mathrm{bulk}}.
```

Thus, after a fixed decay loss, bulk polymers form a Banach-Lie algebra and anchored tree polymers form a Banach-Lie ideal for the bulk action.

Proof sketch. Decompose

```math
W=\sum_X W_X,
\qquad
D=\sum_YD_Y.
```

If `X\cap Y=\emptyset`, then the lifted local maps commute. Hence only overlapping pairs contribute to `[W,D]`. For overlapping `X,Y`,

```math
\operatorname{supp}[W_X,D_Y]\subseteq X\cup Y,
\qquad
\ell_R(X\cup Y)\le \ell_R(Y)+\operatorname{diam}(X)+O(1).
```

The local column-sum norm gives

```math
\|[W_X,D_Y]\|_{1,X\cup Y}
\le
2\|W_X\|_{1,X}\|D_Y\|_{1,Y}.
```

The number of bulk polymers `X` of a given diameter touching a fixed `Y` grows at most exponentially with a rate fixed by bounded degree; the loss from `\mu` to `\nu` absorbs this growth and any polynomial factor in the size of `Y`, since `\ell_R(Y)` controls the tree size of anchored polymers. Taking infima over decompositions gives the displayed bound. `square`

This proposition is the missing algebraic bridge in the LC-log ladder: bulk reference propagation may surround the collar, but commutators with an anchored defect cannot create an unanchored connected component.

## 9. The Missing Linked-Cluster Input

The hard analytic input can be stated cleanly.

### Hypothesis LC: anchored linked-cluster comparison-map locality

For bounded finite-range Hamiltonians in the class above, the localized comparison map has an expansion

```math
J_R^\Lambda(\Delta)-I
=
\sum_{m\ge2}\Delta^m A_{R,m}^\Lambda
```

whose coefficients are anchored local:

```math
\operatorname{supp} A_{R,m}^\Lambda
\subseteq
N_{v m}(R)
```

for some finite velocity `v`, or more generally satisfy a volume-independent anchored quasilocal bound.

Equivalently, disconnected reference-propagation pieces in

```math
\Gamma_R^\Lambda(\Delta)
\left(\Gamma_0^\Lambda(\Delta)\right)^{-1}-I
```

cancel unless they are linked to the collar where `H_R` differs from `H`.

This is not a cosmetic hypothesis. It is the interacting replacement for the exact free quasilocal filtration. Proving or refuting it is the core burden of V2 Paper 3.

### Stronger proof target: Hypothesis LC-log

A sharper target is to prove locality of the connected logarithmic defect. For sufficiently small `Delta`, suppose there is an anchored quasilocal element

```math
L_R^\Lambda(\Delta)\in\mathcal A_{\mu,R}
```

such that, at the finite matrix level,

```math
J_R^\Lambda(\Delta)=\exp L_R^\Lambda(\Delta),
```

and

```math
\|L_R^\Lambda(\Delta)\|_{\mathcal A_{\mu,R}}
\le C\Delta^2
```

with constants independent of total volume.

Then Hypothesis LC follows in the same anchored algebra, because

```math
J_R-I
=
\sum_{n\ge1}\frac{L_R^n}{n!},
\qquad
J_R^{-1}-I
=
\sum_{n\ge1}\frac{(-L_R)^n}{n!}.
```

The Banach-algebra product property keeps these series anchored at `R`, with only controlled support growth or exponential-tail loss. At coefficient level, this says the primitive object to prove local is not the full inverse and not even `J_R-I`, but the connected cumulant generator `L_R`.

This is the most direct route to unlocking LC: prove that disconnected reference pieces contribute only to disconnected logarithms, hence disappear from the connected collar-anchored generator.

### Lemma ladder needed to prove LC-log

LC-log is not a single estimate. It splits into four concrete proof obligations.

1. **Reference-log locality.** Define

```math
W_0^\Lambda(\Delta):=\log\Gamma_0^\Lambda(\Delta).
```

One must prove that `W_0^\Lambda` has a connected quasilocal expansion in the chosen polymer or anchored algebra, with constants independent of total volume.

2. **Anchored log-difference locality.** Define

```math
D_R^\Lambda(\Delta)
:=
\log\Gamma_R^\Lambda(\Delta)-\log\Gamma_0^\Lambda(\Delta).
```

One must prove that every connected component of `D_R^\Lambda` touches the collar where `H_R` differs from `H`, again with volume-independent bounds.

3. **BCH anchoring.** Since

```math
J_R^\Lambda
=
\exp(W_0^\Lambda+D_R^\Lambda)\exp(-W_0^\Lambda),
```

the desired logarithm is

```math
L_R^\Lambda
=
\log\left(\exp(W_0^\Lambda+D_R^\Lambda)\exp(-W_0^\Lambda)\right).
```

The Baker-Campbell-Hausdorff expansion contains nested commutators with at least one `D_R^\Lambda`. Proposition 6 is the needed algebraic estimate: bulk-local commutators with anchored defects remain anchored, possibly with a smaller exponential rate. Thus every BCH term remains anchored to `R`.

4. **Small-slab convergence.** The connected polymer norm must make the logarithm and BCH series converge for a `Delta_*` independent of volume, or else the result remains only a fixed-order formal theorem.

This ladder is the precise content hidden inside Hypothesis LC. The existing draft proves the algebraic consequences once these four steps hold, proves the linked-cluster cancellation at fixed formal order, and reduces the finite-slab upgrade to coefficient-majorant estimates. Proposition 10 below proves those majorants for bounded finite-range Hamiltonians with uniformly finite local dimension and common-support anchored collar deformations, using a paired-word Born-squared activity expansion and KP smallness.

After Propositions 5 and 6, the purely algebraic part of step 3 is controlled. Proposition 10 supplies the convergent versions of steps 1, 2, and 4 for the common-collar finite-range class. Outside that class, especially in reduced gauge coordinates or cutoff-removal limits, these steps remain hypotheses to be checked.

### Proposition 7: LC-log reduction to bulk and anchored logarithms

Assume `0<\nu<\mu`. Suppose

```math
W_0^\Lambda=\log\Gamma_0^\Lambda
\in\mathcal B_\mu^{\mathrm{bulk}},
\qquad
D_R^\Lambda
=
\log\Gamma_R^\Lambda-\log\Gamma_0^\Lambda
\in\mathcal A_{\mu,R}^{\mathrm{tree}},
```

with volume-independent bounds

```math
\|W_0^\Lambda\|_{\mu}^{\mathrm{bulk}}\le M,
\qquad
\|D_R^\Lambda\|_{\mu,R}^{\mathrm{tree}}\le \eta,
```

and suppose the BCH series for

```math
L_R^\Lambda
=
\log\left(\exp(W_0^\Lambda+D_R^\Lambda)\exp(-W_0^\Lambda)\right)
```

converges in the `\nu`-tree norm. Then

```math
L_R^\Lambda\in\mathcal A_{\nu,R}^{\mathrm{tree}},
```

and there is an increasing analytic majorant `F_{\mu,\nu}` such that

```math
\|L_R^\Lambda\|_{\nu,R}^{\mathrm{tree}}
\le
F_{\mu,\nu}(M,\eta)\,\eta,
```

with constants independent of total volume. In particular, if `\eta=O(\Delta^2)` and `M` is bounded in the small-slab window, then `L_R^\Lambda=O(\Delta^2)` in the anchored tree norm.

Proof sketch. The BCH series for `log(exp(W_0+D_R)exp(-W_0))` vanishes when `D_R=0`; therefore every nonzero BCH monomial contains at least one occurrence of `D_R`. Products and commutators among anchored factors are controlled by Proposition 5. Commutators between bulk-local `W_0` factors and anchored factors are controlled by Proposition 6, with decay loss from `\mu` to `\nu`. The scalar BCH majorant gives the analytic function `F_{\mu,\nu}` in the stated convergence domain. `square`

### Proposition 8: fixed-order LC-log locality

For bounded finite-range Hamiltonians with uniformly finite local configuration spaces, LC-log holds at every fixed formal order.

More precisely, write

```math
\Gamma_0^\Lambda(\Delta)
=
I+\sum_{m\ge2}\Delta^mG_{0,m}^\Lambda,
\qquad
W_0^\Lambda(\Delta)
:=
\log\Gamma_0^\Lambda(\Delta)
=
\sum_{m\ge2}\Delta^mW_{0,m}^\Lambda.
```

Then each coefficient has a connected polymer decomposition

```math
W_{0,m}^\Lambda
=
\sum_{\substack{X\subset\Lambda\\X\ \mathrm{connected}\\\operatorname{diam}(X)\le v m}}
W_{0,m,X}^\Lambda,
```

with `W_{0,m,X}^\Lambda` supported in `X`. For each fixed `m`, the number and size of terms touching any fixed cell are bounded by constants depending on `m`, the interaction range, the degree bound, and the local dimension, but not on `|\Lambda|`.

Similarly, for the localized kernel,

```math
W_R^\Lambda(\Delta):=\log\Gamma_R^\Lambda(\Delta),
\qquad
D_R^\Lambda(\Delta):=W_R^\Lambda(\Delta)-W_0^\Lambda(\Delta)
=
\sum_{m\ge2}\Delta^mD_{R,m}^\Lambda,
```

one has

```math
D_{R,m}^\Lambda
=
\sum_{\substack{X\subset\Lambda\\X\ \mathrm{connected}\\X\cap N_{v m}(R_*)\ne\emptyset\\
\operatorname{diam}(X)\le v m}}
D_{R,m,X}^\Lambda.
```

Thus `D_{R,m}^\Lambda` is anchored-tree local at fixed order. By Proposition 7, the formal coefficient of

```math
L_R^\Lambda
=
\log\left(\exp(W_0^\Lambda+D_R^\Lambda)\exp(-W_0^\Lambda)\right)
```

is also anchored-tree local at every fixed order.

Proof. The order-`m` coefficient of `e^{-i\Delta H_\Lambda}` is a finite sum of ordered words with at most `m` local Hamiltonian terms. Each word has a support hypergraph built from the supports of those local terms. Because the interaction range is finite and the graph degree is bounded, any connected component generated by a word of total order `m` has diameter at most `v m` for a velocity `v` depending only on the interaction range.

Passing to `\Gamma_0=|U|^2` pairs two amplitude words whose orders add to `m`; the active support is the union of their word supports and obeys the same `O(m)` connected-component bound. If the underlying cell graph splits into two disconnected components `A\sqcup B` and the Hamiltonian splits as `H_A+H_B`, then

```math
\Gamma_{A\sqcup B}(\Delta)
=
\Gamma_A(\Delta)\otimes\Gamma_B(\Delta).
```

For matrices near the identity, the logarithm respects this product because

```math
\Gamma_A\otimes\Gamma_B
=
(\Gamma_A\otimes I)(I\otimes\Gamma_B)
```

and the two tensor factors commute. Hence

```math
\log(\Gamma_A\otimes\Gamma_B)
=
\log\Gamma_A\otimes I
+
I\otimes\log\Gamma_B.
```

Therefore the coefficients of `W_0=\log\Gamma_0` have no disconnected polymer contribution. Equivalently, the logarithm is the cumulant/Mobius transform of the primitive kernel coefficients, and disconnected products cancel. This gives the connected decomposition of `W_{0,m}`.

For `D_R`, observe that `H_R` and `H` agree on every connected cluster whose `m`-step interaction neighborhood does not meet `R_*`. The corresponding connected log coefficient is therefore identical in `W_R` and `W_0`, and cancels in the difference. Only connected clusters linked to `N_{v m}(R_*)` remain. The final statement for the formal coefficients of `L_R` follows from Proposition 7 at the coefficient level: each BCH monomial contains at least one anchored `D_R` coefficient, and commutators with bulk-local `W_0` coefficients preserve anchoring. `square`

This proposition is a real partial proof of item 4: the linked-cluster cancellation is established order by order. Proposition 10 is the finite-slab upgrade for the bounded finite-range common-collar class.

### Proposition 9: coefficient-majorant criterion for finite-slab LC-log

The finite-slab convergence problem is now precise. Let the connected coefficients from Proposition 8 be written as

```math
W_{0,m}^\Lambda=\sum_X W_{0,m,X}^\Lambda,
\qquad
D_{R,m}^\Lambda=\sum_X D_{R,m,X}^\Lambda.
```

Assume there exist constants `A_0,A_R,B,\mu>0`, independent of total volume, such that for every `m>=2`,

```math
\sup_{x\in\Lambda}
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{\mu\operatorname{diam}(X)}
\|W_{0,m,X}^\Lambda\|_{1,X}
\le
A_0B^m,
```

and

```math
\sum_{\substack{X\ \mathrm{connected}}}
e^{\mu\ell_R(X)}
\|D_{R,m,X}^\Lambda\|_{1,X}
\le
A_RB^m.
```

Then for every `|\Delta|<B^{-1}` the formal series

```math
W_0^\Lambda(\Delta)
=
\sum_{m\ge2}\Delta^m W_{0,m}^\Lambda,
\qquad
D_R^\Lambda(\Delta)
=
\sum_{m\ge2}\Delta^mD_{R,m}^\Lambda
```

converge in the bulk-polymer and anchored tree-polymer norms, respectively, with bounds independent of total volume:

```math
\|W_0^\Lambda(\Delta)\|_{\mu}^{\mathrm{bulk}}
\le
A_0\frac{(B|\Delta|)^2}{1-B|\Delta|},
```

and

```math
\|D_R^\Lambda(\Delta)\|_{\mu,R}^{\mathrm{tree}}
\le
A_R\frac{(B|\Delta|)^2}{1-B|\Delta|}.
```

The BCH convergence condition is then a small-norm Banach-Lie condition, not a separate linked-cluster combinatorial assumption. The bulk norm has the same local commutator estimate as the anchored norm, and Proposition 6 says the bulk action preserves the anchored ideal after a decay loss. Thus the bulk-plus-anchored logarithms form a semidirect Banach-Lie system. After possibly reducing the decay rate from `\mu` to `\nu` and shrinking the small-slab window so the standard BCH majorant is inside its convergence radius, finite-slab LC-log holds:

```math
L_R^\Lambda(\Delta)
\in
\mathcal A_{\nu,R}^{\mathrm{tree}},
\qquad
\|L_R^\Lambda(\Delta)\|_{\nu,R}^{\mathrm{tree}}
=
O(\Delta^2),
```

with constants independent of total volume. Consequently `J_R-I`, `J_R^{-1}-I`, and the exchange-defect bounds of Section 10 hold in the same finite-slab window.

Proof. The first two estimates are direct summations of the assumed coefficient majorants:

```math
\sum_{m\ge2}|\Delta|^mA_0B^m
=
A_0\frac{(B|\Delta|)^2}{1-B|\Delta|},
```

and similarly for `D_R`. Since both bounds are `O(\Delta^2)`, choosing `|\Delta|` smaller if necessary puts the semidirect Banach-Lie norm inside the BCH convergence radius used in Proposition 7. Proposition 7 then turns these convergent log estimates into an anchored bound for `L_R`. The exponential calculus in Proposition 5 gives `J_R=e^{L_R}` and `J_R^{-1}=e^{-L_R}` in the same tree-polymer algebra, and Theorem 4 gives the exchange-defect window estimate. `square`

Thus the remaining analytic task is a growth theorem for the connected log coefficients:

```math
\text{connected coefficient size at order }m
\le
\text{const}\cdot B^m
```

in the bulk and anchored tree norms. Exponential growth in `m` is harmless for sufficiently small `Delta`; factorial growth would block this route.

The convergence problem is therefore concentrated in one place. One must prove the two displayed coefficient-majorant estimates, not a global Neumann bound for `\Gamma_0^{-1}`. Proposition 10 proves those estimates for the bounded finite-range common-collar class. The proof has three ingredients: Duhamel words for `e^{-i\Delta H}` have connected support growing at bounded speed; the Born-squared projection pairs two such words and preserves finite-speed support control up to constants depending on local dimension; and the logarithm is controlled by a tree-graph or Kotecky-Preiss estimate so the cumulant combinatorics is exponential in the order rather than factorial.

### Operator-valued KP logarithm used below

The finite-slab theorem uses the following operator-valued version of the
compatible-polymer cluster expansion. Let `\mathfrak B_\Lambda` be the
complexified finite matrix algebra on `C_\Lambda`, with local column-sum norms.
For each connected polymer `X`, let `\mathfrak B_X` be the subalgebra of maps
supported in `X`, embedded into `\mathfrak B_\Lambda` by tensoring with the
identity outside `X`. If `X\cap Y=\emptyset`, elements of `\mathfrak B_X` and
`\mathfrak B_Y` commute.

Given holomorphic activities `\zeta_X(z)\in\mathfrak B_X`, define the
operator-valued polymer gas

```math
\mathcal Z_\Lambda(\zeta)
:=
\sum_{\mathcal F\ \mathrm{compatible}}
\prod_{X\in\mathcal F}^{\uparrow}\zeta_X,
```

where compatibility means pairwise disjoint support, the empty family
contributes `I`, and `\uparrow` denotes any fixed deterministic ordering of
polymers. The product is independent of the chosen ordering inside a compatible
family because disjoint activities commute.

For `0<\mu'<\mu`, choose `a` large enough that the bounded-degree lattice-animal
constant

```math
\mathfrak N_{a,\mu-\mu'}
:=
\sup_{x\in\Lambda}
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{-a|X|-(\mu-\mu')\operatorname{diam}(X)}
```

is finite uniformly in `\Lambda`. There are constants

```math
\varepsilon_{\mathrm{KP}}
=
\varepsilon_{\mathrm{KP}}(a,\mu,\mu',b,d_{\mathrm{loc}})>0,
\qquad
C_{\mathrm{KP}}
=
C_{\mathrm{KP}}(a,\mu,\mu',b,d_{\mathrm{loc}})<\infty,
```

for example any sufficiently small multiple of
`\mathfrak N_{a,\mu-\mu'}^{-1}` is an admissible threshold, such that the
following holds. If

```math
\mathfrak a_\mu(\zeta)
:=
\sup_x
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{a|X|+\mu\operatorname{diam}(X)}
\|\zeta_X\|_{1,X}
\le
\varepsilon_{\mathrm{KP}},
```

then `\mathcal Z_\Lambda(t\zeta)` is invertible for `0\le t\le1` and the
cluster logarithm

```math
\operatorname{Log}_{\mathrm{KP}}\mathcal Z_\Lambda(\zeta)
:=
\int_0^1
\mathcal Z_\Lambda(t\zeta)^{-1}
\frac{d}{dt}\mathcal Z_\Lambda(t\zeta)\,dt
```

exists in the bulk polymer norm. Equivalently,

```math
\operatorname{Log}_{\mathrm{KP}}\mathcal Z_\Lambda(\zeta)
=
\sum_{n\ge1}\frac1{n!}
\sum_{\substack{X_1,\ldots,X_n\\
\mathcal G_{\mathrm{inc}}(X_1,\ldots,X_n)\ \mathrm{connected}}}
\mathcal U(X_1,\ldots,X_n;\zeta),
```

where `\mathcal G_{\mathrm{inc}}` is the incompatibility graph
`X_i\cap X_j\ne\emptyset`, and

```math
\mathcal U(X_1,\ldots,X_n;\zeta)
:=
\left.
\partial_{t_1}\cdots\partial_{t_n}
\operatorname{Log}_{\mathrm{KP}}
\mathcal Z_\Lambda\!\left(\zeta^{(t)}\right)
\right|_{t=0}
```

with `\zeta_Y^{(t)}=\sum_{i:X_i=Y}t_i\zeta_Y` and all other activities set to
zero. This is a Banach-valued multilinear cluster coefficient. This formula is
the exact noncommutative substitute for the scalar Ursell expansion:
overlapping activities need not commute, and all products are controlled in
the Banach algebra norm.

The bound is volume-uniform:

```math
\left\|
\operatorname{Log}_{\mathrm{KP}}\mathcal Z_\Lambda(\zeta)
\right\|_{\mu'}^{\mathrm{bulk}}
\le
C_{\mathrm{KP}}\mathfrak a_\mu(\zeta).
```

If the activities depend holomorphically on an external parameter `z` and the
same KP smallness bound holds uniformly for `|z|\le\rho`, then
`\operatorname{Log}_{\mathrm{KP}}\mathcal Z_\Lambda(\zeta(z))` is holomorphic
as a map into the bulk polymer Banach space on `|z|<\rho`.

If `\widetilde\zeta_X=\zeta_X+\delta\zeta_X` also satisfies the same bulk
smallness condition and

```math
\mathfrak a_{\mu,R}(\delta\zeta)
:=
\sum_{X\ \mathrm{connected}}
e^{a|X|+\mu\ell_R(X)}
\|\delta\zeta_X\|_{1,X}
<\infty,
```

then the marked-cluster difference satisfies

```math
\left\|
\operatorname{Log}_{\mathrm{KP}}\mathcal Z_\Lambda(\widetilde\zeta)
-
\operatorname{Log}_{\mathrm{KP}}\mathcal Z_\Lambda(\zeta)
\right\|_{\mu',R}^{\mathrm{tree}}
\le
C_{\mathrm{KP}}\mathfrak a_{\mu,R}(\delta\zeta),
```

after the same decay loss from `\mu` to `\mu'`. Its expansion is the cluster
expansion above with at least one marked activity `\delta\zeta`.

This logarithm is the analytic branch obtained by continuation from
`\mathcal Z_\Lambda(0)=I`; it is not a global Neumann logarithm in volume norm.
At a fixed finite volume it agrees with the usual matrix logarithm on that
branch. The theorem is purely complex Banach-algebraic: it does not use
positivity, stochasticity, or scalar commutativity beyond disjoint-support
commutation.

### Proposition 10: paired-word activity theorem for Born-squared kernels

Proposition 9 is stated directly at the level of logarithmic coefficients. The more primitive estimate should not be a bound on `\Gamma_0-I` in a connected polymer norm. That bound already fails in the exact product benchmark, because `\Gamma_0-I` contains products of arbitrarily far independent local defects. The correct finite-slab theorem is a multiplicative polymer-activity theorem for `\Gamma_0` itself.

Let `\Lambda` be a bounded-degree finite cell graph with uniformly finite local configuration spaces. Let

```math
H_\Lambda=\sum_{Y\in\mathcal E_\Lambda}h_Y
```

be a Hermitian finite-range Hamiltonian satisfying:

1. each `Y` is connected, `|Y|\le s`, and `\operatorname{diam}(Y)\le r`;
2. each cell belongs to at most `b` supports in `\mathcal E_\Lambda`;
3. `\|h_Y\|_{1,Y}\le J_1`;
4. the constants `r,s,b,J_1` are independent of total volume.

Let the localized deformation be written on the same support family,

```math
H_{R,\Lambda}
=
\sum_{Y\in\mathcal E_\Lambda}(h_Y+c_{R,Y}),
```

with Hermitian `c_{R,Y}`, and suppose that for some `\mu>0` and for some
polymer size weight `a` above the bounded-degree lattice-animal threshold used
in the operator-valued KP lemma,

```math
\|h_Y+c_{R,Y}\|_{1,Y}\le J_{\mathrm{def}},
\qquad
\sum_Y e^{a|Y|+\mu\ell_R(Y)}\|c_{R,Y}\|_{1,Y}\le C_R,
```

where `C_R,J_{\mathrm{def}}` are independent of total volume. Equivalently, the deformation has a fixed anchored collar scaffold in the weighted support norm. If the reference and deformed Hamiltonians are initially written on different finite-range support families, refine to their finite union and insert zero local terms.

For complex `z`, define the holomorphic Born-squared extension

```math
\Gamma_H^\Lambda(z)
:=
e^{-izH_\Lambda}\odot e^{iz\overline{H_\Lambda}},
```

where `\odot` is entrywise product and `\overline{H}` is entrywise complex conjugation. For real `z=\Delta`, this is exactly `|e^{-i\Delta H_\Lambda}|^2`.
For nonreal `z`, the entries are complex and need not be positive. The
complex extension is used only as a holomorphic majorant device in the
complexified local matrix algebra. Since `H_\Lambda` is Hermitian,
`1^T\Gamma_H^\Lambda(z)=1^T` still holds by analytic continuation, but no
stochastic positivity is claimed away from the real axis. The zero-column-sum
pseudo-stochastic defect interpretation is recovered for the real comparison
maps and their logarithmic branch.

Then there exist constants `C_2,C_3<\infty`, depending only on the bounded-geometry data and the uniform local dimension bound, such that the following hold.

First, `\Gamma_H^\Lambda(z)` and `\Gamma_{H_R}^\Lambda(z)` have compatible connected-polymer activity expansions

```math
\Gamma_H^\Lambda(z)
=
\sum_{\mathcal F\ \mathrm{compatible}}
\prod_{X\in\mathcal F}\zeta_X^\Lambda(z),
\qquad
\Gamma_{H_R}^\Lambda(z)
=
\sum_{\mathcal F\ \mathrm{compatible}}
\prod_{X\in\mathcal F}\zeta_{R,X}^\Lambda(z),
```

where `X` ranges over connected polymers, compatibility means disjoint support, and the empty family contributes `I`.

Second, if

```math
\alpha_0(z):=C_2J_1e^{as+\mu r}|z|<1,
\qquad
\alpha_R(z):=C_3J_{\mathrm{def}}e^{as+\mu r}|z|<1,
```

then the activities obey the volume-independent bounds

```math
\sup_{x\in\Lambda}
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{a|X|+\mu\operatorname{diam}(X)}
\|\zeta_X^\Lambda(z)\|_{1,X}
\le
\frac{\alpha_0(z)^2}{1-\alpha_0(z)},
```

and

```math
\sum_{\substack{X\ \mathrm{connected}}}
e^{a|X|+\mu\ell_R(X)}
\|\zeta_{R,X}^\Lambda(z)-\zeta_X^\Lambda(z)\|_{1,X}
\le
C_R\frac{\alpha_R(z)^2}{1-\alpha_R(z)}.
```

Let `\varepsilon_{\mathrm{KP}}(a,\mu,\mu')` and `C_{\mathrm{KP}}(a,\mu,\mu')`
be the operator-valued KP constants from the preceding lemma, with dependence
only on bounded geometry and the uniform local dimension bound. Choose
`\rho_0>0` so that `\alpha_0(\rho_0),\alpha_R(\rho_0)<1` and both activity
right-hand sides above are at most `\varepsilon_{\mathrm{KP}}`. Then, for every
`|z|\le\rho_0` and every `0<\mu'<\mu`, the analytic cluster logarithms

```math
W_0^\Lambda(z):=\log\Gamma_H^\Lambda(z),
\qquad
D_R^\Lambda(z):=\log\Gamma_{H_R}^\Lambda(z)-\log\Gamma_H^\Lambda(z)
```

exist in the corresponding polymer algebras on the branch continued from
`z=0` and satisfy

```math
\|W_0^\Lambda(z)\|_{\mu'}^{\mathrm{bulk}}
\le
C_{\mathrm{KP}}\frac{\alpha_0(z)^2}{1-\alpha_0(z)},
```

and

```math
\|D_R^\Lambda(z)\|_{\mu',R}^{\mathrm{tree}}
\le
C_{\mathrm{KP}}C_R\frac{\alpha_R(z)^2}{1-\alpha_R(z)}.
```

Consequently the coefficient-majorant hypotheses of Proposition 9 hold, with constants independent of total volume. Hence finite-slab LC-log holds for this bounded finite-range common-collar class after possibly shrinking the small-slab radius.

Proof. Expand the two exponentials in `\Gamma_H^\Lambda(z)` into paired Duhamel words

```math
\Omega=(Y_1,\ldots,Y_p;Z_1,\ldots,Z_q)
```

with contribution

```math
K_\Omega(z)
=
\frac{(-iz)^p(iz)^q}{p!\,q!}
\left(h_{Y_p}\cdots h_{Y_1}\right)
\odot
\left(\overline h_{Z_q}\cdots\overline h_{Z_1}\right).
```

The entrywise product is submultiplicative in local column-sum norm. For local matrices on the same finite configuration set,

```math
\|A\odot B\|_1
=
\max_j\sum_i |A_{ij}B_{ij}|
\le
\|A\|_1\|B\|_1.
```

Together with `\|A\otimes B\|_1=\|A\|_1\|B\|_1`, this gives

```math
\|K_\Omega(z)\|_{1,\operatorname{supp}\Omega}
\le
\frac{|z|^{p+q}}{p!\,q!}J_1^{p+q}.
```

The support hypergraph of `\Omega` has hyperedges `Y_i` and `Z_j`. Define, for connected `X`,

```math
\zeta_X^\Lambda(z)
:=
\sum_{\substack{\Omega:\ \operatorname{supp}\Omega=X\\
\operatorname{supp}\Omega\ \mathrm{connected}}}
K_\Omega(z).
```

Here `\operatorname{supp}\Omega` means the union of all cells touched by the two words. This is a local map supported in `X`, and the empty paired word gives the identity.

The compatible-family expansion follows from the exponential shuffle identity. If the support hypergraph of a paired word has connected components `X_1,\ldots,X_k`, then terms on different `X_j` act on disjoint tensor factors and commute. Moreover,

```math
\frac1{p!\,q!}
```

is exactly the coefficient obtained by summing over all shuffles of the amplitude subwords and conjugate subwords belonging to the different components. If component `X_j` carries `p_j` amplitude terms and `q_j` conjugate terms, with `p=\sum_jp_j` and `q=\sum_jq_j`, then the global coefficient times the number of independent shuffles is

```math
\frac1{p!\,q!}
\frac{p!}{\prod_j p_j!}
\frac{q!}{\prod_j q_j!}
=
\prod_j\frac1{p_j!\,q_j!},
```

which is exactly the coefficient in the product of the component activities.

Therefore the sum of all paired words whose connected components are `X_1,\ldots,X_k` factors as

```math
\prod_{j=1}^k\zeta_{X_j}^\Lambda(z),
```

and summing over all finite compatible families gives

```math
\Gamma_H^\Lambda(z)
=
\sum_{\mathcal F\ \mathrm{compatible}}
\prod_{X\in\mathcal F}\zeta_X^\Lambda(z).
```

The same construction with `h_Y+c_{R,Y}` gives the activities `\zeta_{R,X}` for `H_R`.

It remains to prove the activity bounds. Let `\omega=(Y_1,\ldots,Y_n)` be an ordered word of local supports whose overlap graph is connected and touches a fixed cell `x`. There is a constant `C_{\mathrm{cw}}`, depending only on bounded geometry, such that the number of such words is bounded by

```math
N_n(x)\le C_{\mathrm{cw}}^n n!.
```

because a connected word can be exposed by a spanning-tree order, and at the `k`th exposure there are at most `Ck` local supports touching the already exposed cluster. The Taylor coefficient `1/n!` in `e^{-izH}` cancels this factorial. Consequently

```math
\sup_x
\sum_{\substack{\omega\ \mathrm{connected}\\\omega\ni x\\|\omega|=n}}
e^{a|\operatorname{supp}\omega|+\mu\operatorname{diam}(\omega)}
\frac{\|h_{Y_n}\cdots h_{Y_1}\|_{1,\operatorname{supp}\omega}}{n!}
\le
\left(C_{\mathrm{cw}}J_1e^{as+\mu r}\right)^n.
```

For paired words, set `m=p+q`. The sum over splits `p+q=m` and over the two ordered channels contributes only another exponential factor, absorbed into `C_2^m`. Since each support in a paired word has size at most `s` and diameter at most `r`, the preceding estimate gives

```math
\sup_x
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{a|X|+\mu\operatorname{diam}(X)}
\|\zeta_X^\Lambda(z)\|_{1,X}
\le
\sum_{m\ge2}\left(C_2J_1e^{as+\mu r}|z|\right)^m.
```

The sum starts at `m=2`. Indeed, the order-`z` contribution for a single local Hermitian term is

```math
(-iz h_Y)\odot I_Y
+
I_Y\odot(iz\overline h_Y)
=
-iz\,\operatorname{diag}(h_Y)
+
iz\,\operatorname{diag}(\overline h_Y)
=0,
```

because the diagonal of a Hermitian matrix is real and the off-diagonal entries are killed by the entrywise product with `I_Y`.

For the localized deformation, expand every deformed local factor as an unmarked reference factor plus a marked difference factor `c_{R,Y}`. The paired-word expansion for

```math
\delta\zeta_X^\Lambda(z)=\zeta_{R,X}^\Lambda(z)-\zeta_X^\Lambda(z)
```

is therefore a connected paired-word sum with at least one marked local term. Expose the connected paired word from the first marked factor; all later factors are chosen from supports touching the already exposed cluster. The anchored weight of the first marked term is controlled by the assumed `C_R` bound, and subsequent supports are absorbed by `e^{as+\mu r}`. The same factorial-cancellation argument gives

```math
\sum_{\substack{X\ \mathrm{connected}}}
e^{a|X|+\mu\ell_R(X)}
\|\delta\zeta_X^\Lambda(z)\|_{1,X}
\le
C_R
\sum_{m\ge2}
\left(C_3J_{\mathrm{def}} e^{as+\mu r}|z|\right)^m,
```

again starting at order `m=2` by the same Hermitian diagonal cancellation.

The displayed geometric sums are exactly the activity bounds with `\alpha_0`
and `\alpha_R`. If `\rho_0` is chosen so that these bounds are below the
operator-valued KP threshold, the preceding Banach-valued polymer logarithm
applies uniformly in `\Lambda`. Uniformity is inherited as follows: the
lattice-animal constant `\mathfrak N_{a,\mu-\mu'}` depends only on bounded
degree and the decay loss, the activity smallness constants depend only on
`r,s,b,J_1,J_{\mathrm{def}}`, the local dimension bound, and `C_R`, and the
KP constants are functions only of those regulator-independent quantities.

The matrix-valued case is controlled by the scalar majorant in norm, not by
pretending overlapping activities commute. Disjoint activities commute because
they act on disjoint tensor factors. Incompatible overlapping activities are
handled by the Banach-valued cluster coefficients
`\mathcal U(X_1,\ldots,X_n;\zeta)` and bounded using local column-sum
submultiplicativity. The cluster logarithm gives

```math
\log\Gamma_H^\Lambda(z)
=
\sum_{\mathrm{connected\ incompatibility\ clusters}}
\mathcal U(\cdots;\zeta^\Lambda(z)),
```

with the displayed bulk bound after reducing the decay rate from `\mu` to
`\mu'`. The difference `\log\Gamma_{H_R}-\log\Gamma_H` is obtained by marking
at least one activity difference `\zeta_{R,X}-\zeta_X`; the anchored activity
bound forces the whole cluster to be connected back to `R` and yields the
displayed tree-norm estimate. The logarithm here is the KP/analytic branch from
the identity at `z=0`, so finite-volume invertibility is part of the
cluster-expansion conclusion rather than a separate global Neumann estimate.

Finally, `W_0^\Lambda(z)` and `D_R^\Lambda(z)` are holomorphic in `|z|\le\rho_0` and obey uniform `O(z^2)` bounds there. Cauchy's estimate on the circle `|z|=\rho_0` gives, for their Taylor coefficients, exponential-in-order bounds of the form required in Proposition 9, with `B=\rho_0^{-1}` after absorbing constants into `A_0` and `A_R`. Proposition 9 then gives finite-slab LC-log. `square`

### Positive and negative routes

There are now two rigorous ways to stress-test item 4.

**Positive route.** Use Proposition 10 as the finite-slab theorem for bounded finite-range common-collar systems, then check the hypotheses in each gauge or refinement benchmark.

**Negative route.** Produce a bounded-degree, bounded-local-dimension, finite-range Hamiltonian and a localized collar deformation for which some coefficient of `L_R=\log J_R` contains an exterior local component `K_X` with `\ell_R(X)` unbounded and coefficient not decaying exponentially. A primitive far-away term in `\Gamma_R-\Gamma_0` is not enough; the counterexample must survive the relative logarithm.

Thus the paper should not spend its main effort trying to globally bound `\Gamma_0^{-1}`. It should either prove tree-polymer LC-log or find the first coefficient where tree-polymer anchoring fails.

## 10. Consequences Of Anchored Locality

The following results are rigorous consequences of LC or LC-log. They are conditional in arbitrary interacting systems, and unconditional inside the Proposition 10 common-collar finite-range class after choosing the corresponding small-slab radius.

### Corollary: LC-log gives finite-slab inverse calculus

Assume Hypothesis LC-log in the anchored tree-polymer algebra:

```math
\|L_R^\Lambda(\Delta)\|_{\mu,R}^{\mathrm{tree}}
\le C\Delta^2.
```

Then

```math
J_R^\Lambda=e^{L_R^\Lambda},
\qquad
(J_R^\Lambda)^{-1}=e^{-L_R^\Lambda},
```

and

```math
\|J_R^\Lambda-I\|_{\mu,R}^{\mathrm{tree}}
\le e^{C\Delta^2}-1,
\qquad
\|(J_R^\Lambda)^{-1}-I\|_{\mu,R}^{\mathrm{tree}}
\le e^{C\Delta^2}-1.
```

This is stronger than a Neumann argument because invertibility is built into the exponential representation. The Neumann theorem below remains useful when one proves locality for `J_R-I` directly rather than through `L_R`.

### Theorem 2: inverse coefficient locality

Assume Hypothesis LC at the coefficient level, so

```math
K_R^\Lambda(\Delta):=J_R^\Lambda(\Delta)-I
=
\sum_{m\ge2}\Delta^mA_{R,m}^\Lambda
```

with `A_{R,m}^\Lambda` supported in `N_{v m}(R)`. Then the formal inverse

```math
\left(J_R^\Lambda(\Delta)\right)^{-1}
=
I+\sum_{m\ge2}\Delta^m\widetilde A_{R,m}^\Lambda
```

has coefficients supported in `N_{v m}(R)`.

Proof. Formally,

```math
\left(I+K_R\right)^{-1}
=
\sum_{\ell\ge0}(-K_R)^\ell.
```

The coefficient of order `Delta^m` is a finite sum of products

```math
A_{R,m_1}A_{R,m_2}\cdots A_{R,m_\ell},
\qquad
m_1+\cdots+m_\ell=m.
```

Each factor is supported within `N_{v m_j}(R)`. Because support growth under multiplication is at most additive along the interaction graph, the product is supported within `N_{v(m_1+\cdots+m_\ell)}(R)=N_{v m}(R)`. `square`

### Theorem 3: anchored finite-slab inverse control

Assume there is an admissible anchored quasilocal norm such that, for `|\Delta|<Delta_*`,

```math
\|J_R^\Lambda(\Delta)-I\|_{\mathcal A_{\mu,R}}
\le C\Delta^2
```

with constants independent of total volume. If `C\Delta^2<1`, then `J_R^\Lambda(\Delta)` is invertible in the same anchored algebra and

```math
\left\|\left(J_R^\Lambda(\Delta)\right)^{-1}-I\right\|_{\mathcal A_{\mu,R}}
\le
\frac{C\Delta^2}{1-C\Delta^2}.
```

Proof. Apply the Neumann series inside the anchored Banach algebra:

```math
(I+K_R)^{-1}-I
=
\sum_{\ell\ge1}(-K_R)^\ell.
```

Submultiplicativity gives the displayed geometric bound. `square`

### Theorem 4: exchange-defect corridor/window theorem

Let `R_*` and `S_*` be the fixed collar scaffolds for two localized
deformations. For a finite cell set `Z`, let `\tau(Z)` be the length of the
smallest connected cell subgraph containing `Z`, using the fixed scaffolds when
`R_*` or `S_*` has several components. Define the two-anchor excess length

```math
\ell_{R:S}(Z)
:=
\tau(R_*\cup S_*\cup Z)-\tau(R_*\cup S_*).
```

The corridor window of width `w` is

```math
\operatorname{Corr}_{R,S}(w)
:=
\{x\in\Lambda:\ell_{R:S}(\{x\})\le w\}.
```

On a one-dimensional lattice this is just the interval between the two collars,
thickened by `w`. In higher dimension it is the union of near-minimal connecting
trees, again thickened by `w`.

Define the two-anchor corridor norm

```math
\|Q\|_{\nu,R:S}^{\mathrm{corr}}
:=
\inf_{Q=\sum_ZQ_Z}
\sum_Z e^{\nu\ell_{R:S}(Z)}\|Q_Z\|_{1,Z},
```

where the infimum is over local decompositions. Also define the outside-window
tail seminorm

```math
\|Q\|_{>w}^{(1),R:S}
:=
\inf_{Q=\sum_ZQ_Z}
\sum_{\ell_{R:S}(Z)>w}\|Q_Z\|_{1,Z}.
```

Assume

```math
K_R:=J_R-I\in\mathcal A_{\mu,R}^{\mathrm{tree}},
\qquad
K_S:=J_S-I\in\mathcal A_{\mu,S}^{\mathrm{tree}},
```

and that the inverse maps have bounded unitized anchored norms

```math
M_R^{-}:=\|J_R^{-1}\|_{\mu,R}^{+}<\infty,
\qquad
M_S^{-}:=\|J_S^{-1}\|_{\mu,S}^{+}<\infty.
```

Let

```math
\kappa_R:=\|K_R\|_{\mu,R}^{\mathrm{tree}},
\qquad
\kappa_S:=\|K_S\|_{\mu,S}^{\mathrm{tree}},
\qquad
d_{R,S}:=\operatorname{dist}(R_*,S_*).
```

Then for every `0<\nu<\mu` there is a bounded-geometry constant
`C_{\mu,\nu}` independent of total volume such that

```math
\|E_{R,S}-I\|_{\nu,R:S}^{\mathrm{corr}}
\le
C_{\mu,\nu}
e^{-\nu d_{R,S}}
\kappa_R\kappa_S M_R^{-}M_S^{-},
```

where

```math
E_{R,S}
:=
J_RJ_SJ_R^{-1}J_S^{-1}.
```

Consequently, for every corridor width `w>=0`,

```math
\|E_{R,S}-I\|_{>w}^{(1),R:S}
\le
C_{\mu,\nu}
e^{-\nu(d_{R,S}+w)}
\kappa_R\kappa_S M_R^{-}M_S^{-}.
```

If Theorem 3 or LC-log gives `\kappa_R,\kappa_S=O(\Delta^2)` and bounded
inverse norms in a finite slab, then the raw exchange curvature satisfies

```math
\|E_{R,S}-I\|_{>w}^{(1),R:S}
\le
C
\Delta^4
e^{-\nu(d_{R,S}+w)}
```

after shrinking the slab window if necessary.

There is also a sharp finite-order onset statement. Suppose

```math
J_R-I=\sum_{m\ge2}\Delta^mK_{R,m},
\qquad
J_S-I=\sum_{m\ge2}\Delta^mK_{S,m},
```

and, through the order being considered, `K_{R,m}` is supported in
`N_{vm}(R_*)` and `K_{S,m}` is supported in `N_{vm}(S_*)`. Then

```math
[\Delta^m](E_{R,S}-I)=0
```

for all `m<4` and for all `m` with `vm<d_{R,S}`. Equivalently,

```math
E_{R,S}-I
=
O\!\left(\Delta^{n_*}\right),
\qquad
n_*=\max\left(4,\left\lceil d_{R,S}/v\right\rceil\right),
```

with the convention that the displayed order is only an onset lower bound:
the coefficient at `n_*` may still vanish for dynamical reasons.

Proof. Let `A=J_R=I+K_R` and `B=J_S=I+K_S`. The exact identity

```math
ABA^{-1}B^{-1}-I
=
(AB-BA)A^{-1}B^{-1}
=
[K_R,K_S]J_R^{-1}J_S^{-1}
```

reduces the support question to the commutator. Choose local decompositions

```math
K_R=\sum_XK_{R,X},
\qquad
K_S=\sum_YK_{S,Y}.
```

If `X\cap Y=\emptyset`, then the two local maps act on disjoint tensor factors
and commute. Hence

```math
[K_R,K_S]
=
\sum_{X\cap Y\ne\emptyset}[K_{R,X},K_{S,Y}].
```

For intersecting `X,Y`, bounded geometry gives

```math
\ell_{R:S}(X\cup Y)+d_{R,S}
\le
\ell_R(X)+\ell_S(Y)+c_*,
```

where `c_*` depends only on the fixed collar scaffolds. Therefore, using
`\nu<\mu`,

```math
\begin{aligned}
\|[K_R,K_S]\|_{\nu,R:S}^{\mathrm{corr}}
&\le
2e^{\nu c_*}e^{-\nu d_{R,S}}
\sum_Xe^{\nu\ell_R(X)}\|K_{R,X}\|_{1,X}
\sum_Ye^{\nu\ell_S(Y)}\|K_{S,Y}\|_{1,Y} \\
&\le
C_{\mu,\nu}e^{-\nu d_{R,S}}\kappa_R\kappa_S .
\end{aligned}
```

The corridor algebra is a bimodule over the `R`- and `S`-anchored algebras:
multiplication by `J_R^{-1}` and `J_S^{-1}` increases the corridor norm by at
most the unitized anchored norms, after the same harmless decay loss. This gives
the stated bound for `E_{R,S}-I`.

The outside-window estimate follows immediately from the definition of the
weighted norm:

```math
\|Q\|_{>w}^{(1),R:S}
\le
e^{-\nu w}\|Q\|_{\nu,R:S}^{\mathrm{corr}}.
```

For the coefficient onset, a coefficient of order `m` in the commutator core is
a sum of terms `[K_{R,p},K_{S,q}]` with `p,q>=2` and `p+q<=m`. Such a term
vanishes whenever

```math
N_{vp}(R_*)\cap N_{vq}(S_*)=\emptyset,
```

which is guaranteed by `v(p+q)<d_{R,S}`. Hence every commutator contribution of
total order `m` vanishes if `vm<d_{R,S}`; all orders below `4` vanish because
both `K_R` and `K_S` start at order `2`. Multiplication by the inverse factors
cannot create an exchange term when the commutator core at that order is zero.
`square`

This is the raw exchange-curvature control exported to Paper 4. It is a
support and tail theorem for algebraic comparison maps, not yet an operational
observable-locality theorem.

### Theorem 5: projective refinement transfer

Let `a'` refine `a`. Write

```math
A^a:=\Gamma_0^a,
\qquad
B_R^a:=\Gamma_R^a,
\qquad
J_R^a:=B_R^a(A^a)^{-1}.
```

Assume `A^a` and `A^{a'}` are invertible in the slab window under discussion.

Let

```math
P_0:V_{\Sigma_0,a'}\to V_{\Sigma_0,a},
\qquad
P_1:V_{\Sigma_1,a'}\to V_{\Sigma_1,a}
```

be the initial and final coarse-graining maps. Define the primitive projective
residuals

```math
R_0^{a,a'}:=P_1A^{a'}-A^aP_0,
\qquad
R_R^{a,a'}:=P_1B_R^{a'}-B_R^aP_0.
```

The raw Paper 2 identity is

```math
\delta_R^{a,a'}
:=
P_1J_R^{a'}-J_R^aP_1
=
(R_R^{a,a'}-J_R^aR_0^{a,a'})(A^{a'})^{-1}.
```

Consequently, a raw primitive residual estimate is useful only together with a
bound on the reference inverse `(A^{a'})^{-1}` in the same cross-regulator
topology.

In raw form, if

```math
\|R_0^{a,a'}\|\le\epsilon_0(a,a'),
\qquad
\|R_R^{a,a'}\|\le\epsilon_R(a,a'),
\qquad
\|(A^{a'})^{-1}\|\le N_0(a'),
```

and `\|J_R^a\|\le M_R`, then

```math
\|\delta_R^{a,a'}\|
\le
\left(\epsilon_R(a,a')+M_R\epsilon_0(a,a')\right)N_0(a').
```

Thus raw primitive errors must beat any growth of `N_0(a')`.

For the continuum-facing statement, absorb that bottleneck into the hypotheses
and define the reference-renormalized residuals

```math
\widehat R_0^{a,a'}:=R_0^{a,a'}(A^{a'})^{-1},
\qquad
\widehat R_R^{a,a'}:=R_R^{a,a'}(A^{a'})^{-1},
```

which are maps from fine final data to coarse final data. Then the comparison
defect is exactly

```math
\delta_R^{a,a'}
=
\widehat R_R^{a,a'}-J_R^a\widehat R_0^{a,a'}.
```

Let `\mathcal B_{\mu,R}^{a'\to a}` denote the cross-regulator norm in which
comparison naturality is claimed for maps
`V_{\Sigma_1,a'}\to V_{\Sigma_1,a}`. For localized claims this is the
`R`-anchored version; for cylinder or test-effect claims it may be the
corresponding bulk/cylinder seminorm, provided it is a module over the anchored
algebras below.

Assume the following.

1. The coarse-graining maps and cross-regulator operator norms are compatible
   with the anchored tree-polymer algebras: multiplication on the left by a
   coarse anchored operator and on the right by a fine anchored operator is
   bounded, with constants independent of the regulator pair.
2. For the collar `R`, the renormalized primitive residuals obey

```math
\|\widehat R_0^{a,a'}\|_{\mathcal B_{\mu,R}^{a'\to a}}
\le
\eta_0(a,a'),
\qquad
\|\widehat R_R^{a,a'}\|_{\mathcal B_{\mu,R}^{a'\to a}}
\le
\eta_R(a,a'),
```

where `\eta_0(a,a'),\eta_R(a,a')\to0` in the declared refinement limit.
3. The comparison maps have uniform anchored control, either from Theorem 3 or
   from LC-log:

```math
\|J_R^a\|_{\mathcal A_{\mu,R}^{a,+}}
\le M_R,
\qquad
\|(J_R^a)^{-1}\|_{\mathcal A_{\mu,R}^{a,+}}
\le M_R^{-},
```

and similarly at regulator `a'`, with constants independent of the refinement
pair.

Then

```math
\|\delta_R^{a,a'}\|_{\mathcal B_{\mu,R}^{a'\to a}}
\le
\eta_R(a,a')+M_R\eta_0(a,a').
```

In particular,

```math
P_1J_R^{a'}-J_R^aP_1\to0
```

in the anchored cross-regulator topology.

The inverse comparison maps satisfy the exact identity

```math
\delta_{R,\mathrm{inv}}^{a,a'}
:=
P_1(J_R^{a'})^{-1}-(J_R^a)^{-1}P_1
=
-(J_R^a)^{-1}\delta_R^{a,a'}(J_R^{a'})^{-1},
```

and hence

```math
\|P_1(J_R^{a'})^{-1}-(J_R^a)^{-1}P_1\|
\le
M_R^{-}M_{R,\mathrm{fine}}^{-}
\|\delta_R^{a,a'}\|.
```

More explicitly, with the multiplication constants restored, the right-hand
side is multiplied by the corresponding cross-norm constants.

For two collars `R,S`, define

```math
E_{R,S}^a
:=
J_R^aJ_S^a(J_R^a)^{-1}(J_S^a)^{-1}.
```

If the hypotheses above hold for `R` and `S`, then

```math
P_1E_{R,S}^{a'}-E_{R,S}^aP_1\to0
```

in the corresponding corridor/cross-regulator topology. Quantitatively, if all
four factors `J_R,J_S,J_R^{-1},J_S^{-1}` are bounded by `M` at both regulators,
then

```math
\|P_1E_{R,S}^{a'}-E_{R,S}^aP_1\|
\le
M^3
\left(
\|\delta_R\|+\|\delta_S\|
+\|\delta_{R,\mathrm{inv}}\|+\|\delta_{S,\mathrm{inv}}\|
\right),
```

up to the fixed cross-norm multiplication constants.

Proof. The first identity is Paper 2's exact calculation:

```math
P_1J_R^{a'}-J_R^aP_1
=
(R_R-J_R^aR_0)(A^{a'})^{-1},
```

and the renormalized form follows by distributing `(A^{a'})^{-1}` to the two
primitive residuals. The comparison-defect bound is the triangle inequality
and the left-module estimate for multiplication by `J_R^a`.

For inverses, start from

```math
\delta_R=P_1J_R^{a'}-J_R^aP_1
```

and multiply on the left by `(J_R^a)^{-1}` and on the right by
`(J_R^{a'})^{-1}` to get

```math
(J_R^a)^{-1}\delta_R(J_R^{a'})^{-1}
=
(J_R^a)^{-1}P_1-P_1(J_R^{a'})^{-1}.
```

This is the displayed inverse identity with signs reversed.

For exchange defects, set

```math
X_1=J_R,\quad X_2=J_S,\quad X_3=J_R^{-1},\quad X_4=J_S^{-1},
```

and write

```math
\delta_i=P_1X_i^{a'}-X_i^aP_1.
```

The telescoping expansion

```math
P_1X_1^{a'}X_2^{a'}X_3^{a'}X_4^{a'}
-X_1^aX_2^aX_3^aX_4^aP_1
```

```math
=
\delta_1X_2^{a'}X_3^{a'}X_4^{a'}
+X_1^a\delta_2X_3^{a'}X_4^{a'}
+X_1^aX_2^a\delta_3X_4^{a'}
+X_1^aX_2^aX_3^a\delta_4
```

gives the exchange bound by repeated cross-norm multiplication. Since each
`\delta_i` tends to zero under the hypotheses, the exchange defect is
asymptotically projectively compatible. `square`

The important lesson is that Theorem 3 or LC-log controls `J_R` and
`J_R^{-1}`; it does not by itself control the reference inverse
`(A^{a'})^{-1}` appearing in raw projective residuals. A projective continuum
claim must therefore prove either raw primitive residuals plus a reference
inverse bound, or the renormalized residual estimates
`\widehat R_0,\widehat R_R` directly.

## 11. Gauge And Sector Variants

Gauge systems require a sectorwise theorem, not a slogan that "locality is
gauge invariant." The correct object is a family of fibered comparison maps,
with the locality norm inherited from a primitive local matter-link
presentation or supplied explicitly on a center-resolved physical sector.

For a center or Gauss-sector label `z`, write

```math
V_{\Lambda,z}
```

for the corresponding coordinate sector block, and write

```math
\iota_z:V_{\Lambda,z}\hookrightarrow V_\Lambda,
\qquad
\rho_z:V_\Lambda\to V_{\Lambda,z}
```

for inclusion and restriction. If a block-preserving map `K` is defined on the
unreduced space, set

```math
K_z:=\rho_zK\iota_z.
```

The inherited sector norm is the quotient/image norm

```math
\|K_z\|_{\mu,R,z}^{\mathrm{tree}}
:=
\inf\{
\|K\|_{\mu,R}^{\mathrm{tree}}:
\rho_zK\iota_z=K_z,\ K\ \text{block preserving}
\}.
```

With this definition, restriction to a sector is contractive and algebraic
products restrict correctly:

```math
(KL)_z=K_zL_z.
```

Thus the sector algebra is a quotient Banach algebra of the block-preserving
unreduced algebra.

This is the safe way to talk about locality on constrained physical sectors:
the support bookkeeping is inherited from the unreduced local graph rather than
silently replaced by possibly nonlocal reduced variables.

### Theorem 6: sectorwise common-collar inverse theorem

Let `\Lambda` be a bounded-degree finite matter-link graph with uniformly
finite local configuration spaces, and let `Z_\Lambda^{\mathrm{adm}}` be a
finite family of admissible Gauss-sector, center, or boundary-flux labels. For
each `z\in Z_\Lambda^{\mathrm{adm}}`, let `V_{\Lambda,z}` be a coordinate block.
Assume:

1. **Sector preservation.** Each local term in the common-collar
   decomposition preserves every admissible block:

```math
h_YV_{\Lambda,z}\subseteq V_{\Lambda,z},
\qquad
(h_Y+c_{R,Y})V_{\Lambda,z}\subseteq V_{\Lambda,z}.
```

2. **Common-collar local presentation.** On the unreduced graph,

```math
H_\Lambda=\sum_{Y\in\mathcal E_\Lambda}h_Y,
\qquad
H_{R,\Lambda}=\sum_{Y\in\mathcal E_\Lambda}(h_Y+c_{R,Y})
```

satisfy the hypotheses of Proposition 10 with constants independent of total
volume.

3. **Uniform sector range.** Either the Proposition 10 constants are uniform
over `z\in Z_\Lambda^{\mathrm{adm}}`, or the theorem is read with the explicit
sector-dependent constants `C_z` and `\Delta_{*,z}`. For refinement claims, the
uniform version is required over the sector family being refined.

Define the sector primitive kernels

```math
\Gamma_{0,z}^\Lambda(\Delta)
:=
\rho_z\Gamma_0^\Lambda(\Delta)\iota_z,
\qquad
\Gamma_{R,z}^\Lambda(\Delta)
:=
\rho_z\Gamma_R^\Lambda(\Delta)\iota_z,
```

and, when `\Gamma_{0,z}^\Lambda` is invertible,

```math
J_{R,z}^\Lambda
:=
\Gamma_{R,z}^\Lambda(\Gamma_{0,z}^\Lambda)^{-1}.
```

Then for every `0<\mu'<\mu` there are constants
`\Delta_*^{\mathrm{sec}}>0` and `C_{\mathrm{sec}}<\infty`, independent of
total volume and uniform over the named sector family in the uniform case, such
that for `|\Delta|<\Delta_*^{\mathrm{sec}}`,

```math
L_{R,z}^\Lambda(\Delta):=\log J_{R,z}^\Lambda(\Delta)
\in
\mathcal A_{\mu',R,z}^{\mathrm{tree}},
```

and

```math
\|L_{R,z}^\Lambda(\Delta)\|_{\mu',R,z}^{\mathrm{tree}}
\le
C_{\mathrm{sec}}\Delta^2.
```

Consequently,

```math
J_{R,z}^\Lambda-I,\quad
(J_{R,z}^\Lambda)^{-1}-I
\in
\mathcal A_{\mu',R,z}^{\mathrm{tree}},
```

with

```math
\|J_{R,z}^\Lambda-I\|_{\mu',R,z}^{\mathrm{tree}}
\le
e^{C_{\mathrm{sec}}\Delta^2}-1,
\qquad
\|(J_{R,z}^\Lambda)^{-1}-I\|_{\mu',R,z}^{\mathrm{tree}}
\le
e^{C_{\mathrm{sec}}\Delta^2}-1.
```

For two collars `R,S`, the sector exchange defect

```math
E_{R,S,z}
:=
J_{R,z}J_{S,z}J_{R,z}^{-1}J_{S,z}^{-1}
```

obeys the same two-anchor corridor/window estimate as Theorem 4 in the
inherited sector norm.

Finally, suppose a refinement `a'\to a` carries a center map

```math
q_{a\leftarrow a'}:Z_{a'}^{\mathrm{adm}}\to Z_a^{\mathrm{adm}}
```

and sectorwise coarse-graining maps

```math
P_{a\leftarrow a',z'}:
V_{a',z'}\to V_{a,q_{a\leftarrow a'}(z')}
```

which are bounded between the inherited tree-polymer norms and satisfy the
fiberwise Paper 2 primitive error estimates for `\Gamma_0` and `\Gamma_R`.
If the constants above are uniform along the refinement family, then

```math
P_{a\leftarrow a',z'}J_{R,z'}^{a'}
-
J_{R,q_{a\leftarrow a'}(z')}^aP_{a\leftarrow a',z'}
\to0
```

in the corresponding sector anchored topology, and the same holds for
sectorwise exchange defects.

Proof. Sector preservation makes `H_\Lambda`, `H_{R,\Lambda}`, the unitary
matrices, and the Born-squared kernels block diagonal on the admissible block
sum:

```math
\Gamma_0^\Lambda=\bigoplus_z\Gamma_{0,z}^\Lambda,
\qquad
\Gamma_R^\Lambda=\bigoplus_z\Gamma_{R,z}^\Lambda.
```

For sufficiently small `|\Delta|`, every block is close to the identity and
therefore invertible. Block inversion and the principal logarithm commute with
restriction:

```math
(\Gamma_0^\Lambda)^{-1}_z=(\Gamma_{0,z}^\Lambda)^{-1},
\qquad
\rho_z\log K\,\iota_z=\log K_z
```

for each block-diagonal `K` in the logarithm neighborhood of the identity.
Apply Proposition 10 to the unreduced common-collar system, then use the
LC-log/BCH construction of Section 9. The bulk logarithm and the anchored
logarithmic defect restrict to each block, and the inherited sector norm is
contractive by definition. Hence the LC-log estimate restricts to

```math
\|L_{R,z}^\Lambda\|_{\mu',R,z}^{\mathrm{tree}}
\le
\|L_R^\Lambda\|_{\mu',R}^{\mathrm{tree}}
\le
C_{\mathrm{sec}}\Delta^2
```

in the uniform case. If only a fixed finite sector family is specified, take
the minimum of the finitely many small-slab radii and the maximum of the
finitely many constants. If the constants are not uniform in a growing family,
the theorem remains true sector by sector but gives no refinement-stable
statement.

The exponential estimates for `J_{R,z}` and `(J_{R,z})^{-1}` are exactly
Proposition 5 applied in the sector algebra. The exchange-defect statement is
Theorem 4 applied fiberwise. The refinement statement is Theorem 5 applied to
the sector map `P_{a\leftarrow a',z'}` and the center map
`q_{a\leftarrow a'}`. `square`

If a paper works directly with center-resolved physical sectors rather than an
explicit unreduced embedding, the same theorem holds after replacing the
inherited norm by a specified sector tree-polymer norm, provided the
sector-resolved local terms satisfy Proposition 10 with constants uniform over
the named sector family. This is an assumption, not an automatic consequence of
Gauss-law reduction.

Equivalently, the correct version of Hypothesis LC in a gauge sector is:

```math
J_{R,z}^\Lambda-I
\in
\mathcal A_{\mu,R,z}
```

with constants either uniform over the sector family being refined or with explicit sector dependence.

### Sector cautions

Three cautions are essential.

1. **Reduced variables may be nonlocal.** In one-dimensional gauge theory, solving Gauss law often produces string Hamiltonians. This does not mean the unreduced gauge theory is nonlocal; it means reduced matter variables are not the right primitive locality coordinates.
2. **Truncation is part of the theorem.** For truncated compact `U(1)`, every estimate must state its dependence on `K` unless a real `K`-uniform theorem is proved.
3. **Boundary centers are data.** Boundary-flux or representation centers cannot be erased by an unfibered projection without changing the locality statement.

Any application of Theorem 6 should therefore specify:

1. the primitive unreduced local configuration space, or a center-resolved physical sector obtained from it;
2. the sector family `Z_a` over which constants are claimed uniform;
3. the center or boundary-flux maps used under refinement;
4. whether the local dimension bound is fixed, as in finite `Z_2`, or cutoff-dependent, as in truncated compact `U(1)`;
5. the exact norm `\mathcal A_{\mu,R,z}` and whether it is inherited by restriction from the unreduced tree-polymer norm.

The safest positive theorem is finite-sector uniformity: fixed local link cutoff, fixed admissible center family, and constants uniform over the finite set of sectors used by the refinement problem. `K -> infinity` or compact-rotor uniformity is a separate theorem.

## 12. How The Existing Interacting Benchmarks Fit

### Common-collar benchmark audit

The audit criterion is stricter than "there is a finite benchmark." A
benchmark belongs to Proposition 10 only in variables where all of the
following are true:

1. the primitive configuration space is a bounded-degree local tensor product,
   or a center-resolved sector inherited from one;
2. the local dimension is uniformly finite over the refinement problem being
   claimed;
3. the Hamiltonian is a bounded finite-range sum on that primitive graph;
4. the unperturbed Hamiltonian and collar deformation are written on one common
   anchored support family, so the induced expansions for `\log J_R`, `J_R`,
   and `J_R^{-1}` live in the same topology;
5. sector, boundary-center, and cutoff dependences are either uniform over a
   named finite family or carried explicitly in the constants.

With that criterion, the benchmark status is:

| Benchmark presentation | Common-collar status | What Paper 3 may claim |
| --- | --- | --- |
| Unconstrained finite-dimensional local spin/qudit lattice | Pass, provided the collar deformation is supported on the same finite-range family as the Hamiltonian. | Proposition 10 gives finite-slab LC-log, inverse locality, and exchange-defect bounds. |
| Dynamical Abelian finite-link benchmark, unreduced or sector-resolved | Conditional pass at fixed finite link space and fixed finite sector family. Existing results support fixed sectorwise inverse control and mixed-support coefficient locality, not volume-stable control by themselves. | Cite as the closest finite precursor. Do not upgrade it to a refinement-uniform theorem without proving uniform constants. |
| Minimal `Z_2` gauge-matter benchmark, unreduced matter-link variables | Pass as the cleanest gauge candidate: finite local dimension, local matter-link graph, and finite sector family after center resolution. | Use for a worked finite-sector gauge theorem if the support family and sector constants are written explicitly. |
| Minimal `Z_2` benchmark after Gauss-law reduction to matter-only variables | Does not automatically pass. Gauss-law elimination can turn local link constraints into strings or global parity data in the reduced coordinates. | Use as evidence for interaction-sensitive exchange coefficients, not as a direct input to Proposition 10 unless a reduced-coordinate locality norm is separately proved. |
| Truncated compact `U(1)` benchmark, unreduced, fixed `K` | Conditional pass at each fixed `K` and fixed admissible sector family. Constants are allowed to depend on `K`. | A legitimate fixed-cutoff finite local-dimension test case. No `K -> infinity` or compact-rotor conclusion follows. |
| Truncated compact `U(1)` after physical-sector elimination | Usually conditional or outside the theorem, depending on whether the no-truncation sector and eliminated variables preserve a common finite-range collar. | Treat as a sector/cutoff example only after proving the inherited norm; otherwise cite as reduced-sector evidence. |
| Static background holonomy or external-gauge benchmark | Not a stress test for interacting gauge inverse control because the gauge field is not dynamical. | Use only as covariance or background-coupling precedent. |
| Reduced-strip/overlap companion papers | Outside Proposition 10 as finite-slab inverse-control evidence. | Use as coefficient ledgers, basis checks, and small-block diagnostics. |

The practical conclusion is simple. The theorem should be advertised as an
unreduced, common-collar local theorem. Gauge benchmarks enter cleanly only
when the primitive matter-link graph, the sector family, and the cutoff
dependence are part of the statement. Reduced physical coordinates are useful
for intuition and coefficient diagnostics, but they do not inherit finite-range
locality for free.

### Finite quantum-simulator exchange-defect diagnostic

Theorem 4 also suggests a near-term technology diagnostic. This is not a direct
test against relativistic QFT; it is a finite-regulator validation of the raw
ISP exchange-curvature object.

On a small controllable spin, qudit, or matter-link simulator, choose a bounded
finite-range Hamiltonian `H` and two localized collar deformations

```math
H_R=H-C_R,
\qquad
H_S=H-C_S.
```

For a small slab time `\Delta`, prepare each computational-basis input state
and estimate the endpoint transition matrices

```math
\Gamma_0=|e^{-i\Delta H}|^2,
\qquad
\Gamma_R=|e^{-i\Delta H_R}|^2,
\qquad
\Gamma_S=|e^{-i\Delta H_S}|^2.
```

For a sufficiently small finite system, this requires only endpoint probability
tomography in the chosen basis, not full phase-sensitive quantum process
tomography. After estimating `\Gamma_0^{-1}` in the finite slab, reconstruct

```math
J_R=\Gamma_R\Gamma_0^{-1},
\qquad
J_S=\Gamma_S\Gamma_0^{-1},
\qquad
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}.
```

The diagnostic checks the structural predictions of Theorem 4:

1. the exchange defect turns on no earlier than fourth order in `\Delta`;
2. separated collars have the onset bound `[\Delta^m](E_{R,S}-I)=0` whenever
   `vm<d(R_*,S_*)`;
3. the reconstructed outside-window tail is consistent with

```math
\|E_{R,S}-I\|_{>w}^{(1),R:S}
\lesssim
\Delta^4e^{-\nu(d_{R,S}+w)}.
```

This is experimentally modest compared with a continuum relativistic test:
all data are finite endpoint frequencies on a small device, and the theorem
only asks for the corridor/onset pattern after finite-matrix reconstruction.
Standard quantum mechanics predicts the same transition matrices once the
implemented Hamiltonian is known, so this diagnostic does not by itself show a
deviation from standard QFT. Its role is to test whether the ISP
comparison-map construction and raw exchange-defect bookkeeping are visible,
stable, and correctly scaled in a controlled finite system. An actual
operational prediction requires Paper 4's instrument layer.

### Dynamical Abelian finite-link benchmark

This is the closest existing precursor. It proves fixed finite sectorwise inverse control and mixed-support coefficient locality. It should be cited as the finite benchmark model for this paper, but not as a volume-stable theorem.

### Minimal `Z_2` gauge-matter benchmark

Use the unreduced matter-link system for locality. Use the reduced physical-sector Hamiltonian and prototype coefficients as evidence that genuinely interaction-sensitive exchange data exist. Do not claim nonintegrability, continuum interaction, or duality resistance.

### Truncated compact `U(1)` benchmark

Use fixed `K` blocks as finite local-dimension examples. The no-truncation condition belongs in the sector definition. Paper 3 must not convert fixed-`K` exactness into compact-rotor control.

### Reduced-strip/overlap companion

Use these papers as coefficient ledgers and strip-basis inputs. They do not control finite-slab inverses.

## 13. Minimal Successful Paper 3

A minimal publishable Paper 3 should prove:

1. Proposition 1, the global-norm obstruction;
2. Theorem 1, fixed finite inverse control with explicit limitations;
3. a precise anchored or cylinder-effect topology;
4. either finite-slab Hypothesis LC, preferably through convergent LC-log, as a proved linked-cluster theorem for a bounded finite-range class, or a counterexample showing it fails;
5. Theorems 2 through 5 as consequences of that linked-cluster theorem or as conditional results;
6. sectorwise gauge variants;
7. a precise statement of what Paper 4 may and may not use.

If finite-slab Hypothesis LC remains unproved outside the common-collar finite-range class, the paper is still useful as a theorem/no-go/conditional framework there, but it should not advertise broader interacting continuum covariance.

Current proof status of this checklist:

1. items 1 and 2 are proved at theorem-framework level in this draft;
2. item 3 is mostly closed at the abstract level: the draft now defines an anchored tree-polymer Banach algebra and proves its inverse/exponential/log/commutator calculus; the remaining item-3 burden is to prove the actual ISP objects satisfy the stated tree-polymer bounds;
3. item 4 is proved at fixed formal order by Proposition 8, reduced to coefficient majorants by Proposition 9, and upgraded to finite-slab LC-log by Proposition 10 for bounded finite-range Hamiltonians with uniformly finite local dimension and common-support anchored collar deformations. Proposition 10 now states the operator-valued KP logarithm, analytic branch, complex-majorant setting, decay-loss constants, and noncommutative activity control explicitly. Outside that class, item 4 remains a named hypothesis or a counterexample target;
4. item 5 is proved from LC or LC-log for inverse and exchange locality; Theorem 4 now gives the concrete corridor/window tail and separated-support onset bound. The projective refinement part, Theorem 5, additionally requires either raw primitive refinement errors strong enough to beat the reference inverse or the reference-renormalized residual estimates `\widehat R_0,\widehat R_R`;
5. item 6 is proved as Theorem 6 for invariant common-collar sector fibers, and the benchmark audit identifies which presentations satisfy its hypotheses; a worked gauge example still has to name the actual sector family, center maps, and uniformity range;
6. item 7 is explicitly boxed below: Paper 4 may use raw `J_R` and `E_{R,S}` as algebraic relative-dynamics maps with locality bounds, but not as observables, effects, or instruments without extra operational structure.

### Paper 4 export

**Paper 4 Export Box.** Paper 3 exports algebraic locality, not operational
measurement theory.

Paper 4 may treat

```math
J_R=\Gamma_R\Gamma_0^{-1},
\qquad
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}
```

as raw relative-dynamics maps in the pseudo-stochastic endpoint-vector space.
When LC/LC-log, Theorem 4, Theorem 5, and the relevant sector hypotheses hold,
Paper 4 may use their anchored support, inverse, exchange-corridor, and
projective-transfer bounds.

Paper 4 may not identify raw `J_R`, `J_R^{-1}`, or `E_{R,S}` with detector
effects, POVM elements, operational instruments, local observable algebras, or
probabilities. These maps can have pseudo-stochastic signs and are not
automatically positive. Operational instruments require additional structure:
a specified preparation/effect pairing, an instrument map or effect functional,
positivity/normalization checks, and a proof that the operational layer
inherits the raw locality bounds.

Paper 4 may use the following only after Paper 3 proves or assumes LC/LC-log in a named topology and, for refinement claims, verifies Theorem 5's reference-renormalized primitive residual estimates:

1. raw comparison maps form localized algebraic relative-dynamics maps in the anchored tree-polymer sense;
2. their inverses obey the same locality bounds;
3. exchange defects have two-anchor corridor/window bounds, exponential outside-window tails, and separated-support coefficient onset bounds;
4. reference-renormalized projective errors propagate through `J_R`, `J_R^{-1}`, and `E_{R,S}` in the same topology.

Paper 4 may not use any of the following as consequences of Paper 3:

1. positivity of `J_R` or `E_{R,S}`;
2. identification of raw comparison maps with operational observables;
3. Haag-Kastler local algebras, additivity, time-slice, spectrum, or type-III structure;
4. Lorentz covariance beyond the regulator/projective hypotheses actually proved;
5. compact-rotor or `K -> infinity` gauge control unless the sector theorem proves it.

Operational instruments and effects must be introduced as additional structures and checked against the raw comparison-map bounds; they are not automatically supplied by those bounds.

### Short Paper 3 Backlog

The following items should be revisited before treating Paper 3 as
publication-polished, but they do not block the Paper 4 handoff:

1. turn the operator-valued KP logarithm into a standalone appendix-level
   theorem with all constants and decay losses tracked line by line;
2. instantiate Theorem 6 in one worked finite gauge sector, preferably the
   unreduced finite `Z_2` matter-link benchmark, including the sector family,
   center maps, and uniformity range;
3. give one explicit small finite quantum-simulator diagnostic example with
   matrices or pseudocode for reconstructing `\Gamma_0`, `J_R`, and `E_{R,S}`;
4. decide whether the common-collar theorem should be stated only for fixed
   local dimension or also in a carefully parameterized cutoff-dependent form;
5. polish notation between `\mathcal A_{\mu,R}^{\mathrm{tree}}`,
   cross-regulator norms, and sector inherited norms so the final paper reads
   as one theorem package rather than a sequence of investigations.

## 14. Failure Modes

The program should stop or narrow if any of the following occur.

1. **Global inverse blowup only.** If no local topology controls the inverse, then interacting raw comparison maps are not continuum-local objects.
2. **Disconnected inverse terms survive.** If `Gamma_0^{-1}` leaves volume-wide disconnected pieces inside `J_R-I`, anchored locality fails.
3. **Gauge reduction hides locality.** If one works only in reduced matter variables, string interactions may produce false nonlocality or false locality claims.
4. **Cutoff dependence is uncontrolled.** Fixed-`K` compact `U(1)` exactness is not a compact-rotor theorem.
5. **Coarse-graining breaks the topology.** Paper 2 refinement estimates must live in the same local topology as inverse control, and their reference-renormalized residuals must vanish.
6. **Raw maps are mistaken for observables.** Raw `J_R` support is not an operational local-net theorem.

## 15. Relationship To Later V2 And V3 Papers

Paper 4 on operational observable reconstruction needs this paper to decide whether raw comparison maps have enough locality to seed operational instruments, or whether additional operational structure must be primitive.

Paper 5 on continuum gauge benchmarks needs sectorwise inverse control before asking for `K`-stability or Schwinger-model-like limits.

V3 interacting and non-Abelian programs should treat this paper as a prerequisite. Inside the bounded finite-range/common-collar class, V3 may cite Proposition 10. Outside that class, especially for non-Abelian sectors, reduced nonlocal variables, or cutoff-removal limits, V3 must carry LC-log explicitly as a named assumption rather than hiding it inside "local Hamiltonian" language.

## 16. Conclusion

The existing interacting benchmark stack proves exact finite interacting kernels and first interaction-sensitive exchange coefficients. That is real progress, but it does not yet prove interacting continuum locality. The obstruction is the inverse.

The correct V2 Paper 3 target is therefore a local inverse calculus: show that `Gamma_0^{-1}` does not delocalize localized defects after Born-squared projection, or prove sharply that it does. With an anchored linked-cluster theorem in hand, comparison-map inverse control, exchange-defect window bounds, and projective refinement compatibility follow by clean algebra. Without it, relativistic ISP remains exact and useful at fixed finite interacting benchmark scope, but not yet a continuum covariant interacting theory.
