# Interacting Projective Kernel Dynamics And Comparison-Map Inverse Control

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

V3 Paper 3 investigation draft

Date: 2026-05-17

Status: First theorem-level projective inverse-control pass. V2 Paper 3 already
shows that global inverse norms are the wrong topology and proves LC-log
locality for the bounded finite-range/common-collar class. This V3 paper turns
that local inverse calculus into a projective refinement theorem: if primitive
interacting endpoint kernels have reference-renormalized refinement residuals
in the same anchored topology where LC-log controls `J_R` and `J_R^{-1}`, then
`J_R`, `J_R^{-1}`, and `E_{R,S}` inherit projective compatibility.

## 1. Purpose

V3 Paper 1 fixed the data discipline: `Gamma`-level claims, operational
instruments, and representation enrichments must be separated. V3 Paper 2
showed that primitive positive lapse kernels can generate the signed
hypersurface-deformation bracket by cone completion at the algebraic tangent
level.

V3 Paper 3 asks the first genuinely interacting question:

> Can local interacting finite dynamics preserve projective compatibility after
> Born-squared projection and algebraic inversion?

The hard object is not the primitive endpoint kernel alone. It is the relative
comparison map

```math
J_R^\Lambda(\Delta)
=
\Gamma_R^\Lambda(\Delta)\bigl(\Gamma_0^\Lambda(\Delta)\bigr)^{-1}
```

and the exchange defect

```math
E_{R,S}^\Lambda
=
J_R^\Lambda J_S^\Lambda
\bigl(J_R^\Lambda\bigr)^{-1}\bigl(J_S^\Lambda\bigr)^{-1}.
```

The inverse is the danger. V2 Paper 3 shows that ordinary global matrix norms
force useless volume-dependent smallness conditions. It also shows the positive
route: prove locality for the connected logarithmic defect

```math
L_R^\Lambda=\log J_R^\Lambda,
```

then `J_R`, `J_R^{-1}`, and `E_{R,S}` are controlled in an anchored local
Banach algebra.

This paper begins from that positive route and adds projective refinement.

## 2. V3 Paper 1 Import Contract

Baseline V3 Paper 3 is Gamma-level plus declared whole-process operations.

```text
Gamma-level imports:
- finite/projective configuration spaces;
- whole-process endpoint kernels Gamma_0 and Gamma_R;
- projective maps P_ab;
- algebraic comparison maps J_R=Gamma_R Gamma_0^{-1};
- exchange defects E_{R,S};
- anchored/cylinder-effect topologies in which residuals are measured.

Operational imports:
- none in the baseline inverse-control theorem.
- operational instruments enter only in later local-net papers.

Representation-enriched imports:
- none in the baseline theorem.
- a Hilbert Hamiltonian may be used to define the finite whole-process kernels,
  but the theorem's output is a statement about their Born-squared endpoint
  kernels and algebraic comparisons.

Forbidden:
- global Neumann control as a substitute for local inverse control;
- unrecorded Markov products of partial kernels;
- treating raw comparison maps as observables;
- hiding LC-log or reference inverse assumptions inside the phrase
  "local Hamiltonian."
```

## 3. V2 Paper 3 Import Ledger

V3 Paper 3 may import the following from V2 Paper 3.

1. **Global-norm no-go.** Global matrix-norm inverse control grows with volume
   even in product systems; it is not the continuum topology.
2. **Anchored topology.** Anchored tree-polymer or cylinder-effect norms are the
   correct local topologies for `J_R-I`, `J_R^{-1}-I`, and exchange defects.
3. **LC-log theorem in a bounded class.** For bounded finite-range Hamiltonians
   with uniformly finite local dimension and common-support anchored collar
   deformations, V2 Proposition 10 proves finite-slab LC-log locality by an
   operator-valued paired-word/KP expansion.
4. **Inverse calculus.** LC-log implies `J_R=e^{L_R}`,
   `J_R^{-1}=e^{-L_R}`, and anchored bounds for both maps.
5. **Exchange corridor theorem.** If `J_R`, `J_S` and their inverses are
   anchored quasilocal, then `E_{R,S}` obeys a two-anchor corridor/window
   estimate with exponential outside-window tails and separated-support onset.
6. **Projective transfer template.** V2 Paper 3 proves the algebraic error
   identity showing that primitive refinement errors must be measured after
   multiplication by the fine reference inverse.

V3 Paper 3 may not import:

1. volume-independent global inverse bounds;
2. compact-rotor or `K\to\infty` gauge cutoff control;
3. reduced-coordinate locality after Gauss-law elimination unless the reduced
   variables carry their own center-resolved anchored topology;
4. interacting stochastic curvature or QFT reconstruction.

## 4. Interacting Projective Setup

Let `a` label a regulator. For each `a`, let `\Lambda_a` be a finite bounded
degree lattice/cell complex with finite local configuration spaces. Let

```math
\Gamma_{0}^{a}(\Delta)
```

be the reference whole-process Born-squared endpoint kernel and let

```math
\Gamma_{R}^{a}(\Delta)
```

be the localized interacting deformation supported on a collar `R`.

For a refinement `b\succeq a`, let

```math
P_{ab}:\Delta(X_b)\to\Delta(X_a)
```

be the projective coarse-graining map.

Define primitive residuals

```math
R_0^{ab}
:=
P_{ab}\Gamma_0^b-\Gamma_0^aP_{ab},
```

```math
R_R^{ab}
:=
P_{ab}\Gamma_R^b-\Gamma_R^aP_{ab}.
```

The key residuals are not `R_0` and `R_R` themselves. They are the
reference-renormalized residuals

```math
\widehat R_0^{ab}
:=
R_0^{ab}(\Gamma_0^b)^{-1},
```

```math
\widehat R_R^{ab}
:=
R_R^{ab}(\Gamma_0^b)^{-1}.
```

This is exactly the lesson from V2 Paper 2 and V2 Paper 3: refinement errors
are amplified by the fine reference inverse, so the theorem must assume or
prove smallness of the renormalized residuals in the same local topology as
the comparison maps.

## 5. Anchored Cross-Regulator Norms

For each collar `R`, suppose there is an anchored Banach algebra

```math
\mathcal A_{\mu,R}^{a}
```

of pseudo-stochastic maps on regulator `a`, and a cross-regulator norm

```math
\|\cdot\|_{\mu,R}^{a\leftarrow b}
```

for maps from the fine regulator `b` to the coarse regulator `a`.

The cross-regulator norm must satisfy the module inequalities

```math
\|A^aD^{a\leftarrow b}\|_{\mu,R}^{a\leftarrow b}
\le
\|A^a\|_{\mu,R}^{a}\|D^{a\leftarrow b}\|_{\mu,R}^{a\leftarrow b},
```

```math
\|D^{a\leftarrow b}B^b\|_{\mu,R}^{a\leftarrow b}
\le
\|D^{a\leftarrow b}\|_{\mu,R}^{a\leftarrow b}\|B^b\|_{\mu,R}^{b}.
```

For exchange defects involving two anchors `R,S`, assume an analogous corridor
cross-regulator norm

```math
\|\cdot\|_{\mu,R:S}^{a\leftarrow b}
```

which is a bimodule over the `R`- and `S`-anchored algebras after the same
controlled decay loss.

This is an abstract version of the V2 anchored tree-polymer topology. A later
application must name the actual norm.

## 6. Hypothesis IC: Projective Interacting Inverse-Control Data

For a family of interacting regulators, **Hypothesis IC** consists of the
following data.

1. **LC-log or equivalent inverse locality.** There are constants
   `C_J, C_{J^{-1}}`, independent of total volume and stable under refinement,
   such that
   ```math
   \|J_R^a-I\|_{\mu,R}^a\le C_J\Delta^2,
   \qquad
   \|(J_R^a)^{-1}-I\|_{\mu,R}^a\le C_{J^{-1}}\Delta^2
   ```
   for all tested `R,a`.
2. **Unitized bounds.**
   ```math
   \|J_R^a\|_{\mu,R}^{a,\sharp}\le M_J,
   \qquad
   \|(J_R^a)^{-1}\|_{\mu,R}^{a,\sharp}\le M_{J^{-1}}.
   ```
3. **Reference-renormalized primitive residuals.** For every refinement
   `b\succeq a`,
   ```math
   \|\widehat R_0^{ab}\|_{\mu,R}^{a\leftarrow b}\le \varepsilon_0^{ab},
   \qquad
   \|\widehat R_R^{ab}\|_{\mu,R}^{a\leftarrow b}\le \varepsilon_R^{ab}.
   ```
4. **Vanishing refinement residuals.**
   ```math
   \varepsilon_0^{ab},\varepsilon_R^{ab}\to0
   ```
   along the projective continuum refinement path.

Inside the V2 bounded finite-range/common-collar class, item 1 follows from
LC-log for each fixed regulator family with uniform constants. Item 3 is the
new V3 projective burden: it is a primitive refinement estimate strong enough
to survive the reference inverse.

## 7. Theorem 7.1: Projective Transfer For Comparison Maps

Assume Hypothesis IC for a collar `R`. Then

```math
P_{ab}J_R^b-J_R^aP_{ab}
=
\widehat R_R^{ab}-J_R^a\widehat R_0^{ab}.
```

Consequently,

```math
\|P_{ab}J_R^b-J_R^aP_{ab}\|_{\mu,R}^{a\leftarrow b}
\le
\varepsilon_R^{ab}+M_J\varepsilon_0^{ab}.
```

In particular, if the reference-renormalized primitive residuals vanish, then
the comparison maps are projectively compatible in the anchored topology.

### Proof

By definition,

```math
J_R^b=\Gamma_R^b(\Gamma_0^b)^{-1},
\qquad
J_R^a=\Gamma_R^a(\Gamma_0^a)^{-1}.
```

Using the primitive residual identities,

```math
P_{ab}\Gamma_R^b
=
\Gamma_R^aP_{ab}+R_R^{ab},
```

```math
P_{ab}\Gamma_0^b
=
\Gamma_0^aP_{ab}+R_0^{ab}.
```

Multiply the first identity on the right by `(\Gamma_0^b)^{-1}`:

```math
P_{ab}J_R^b
=
\Gamma_R^aP_{ab}(\Gamma_0^b)^{-1}
+\widehat R_R^{ab}.
```

From the second identity,

```math
\Gamma_0^aP_{ab}(\Gamma_0^b)^{-1}
=
P_{ab}-\widehat R_0^{ab}.
```

Multiplying by `J_R^a=\Gamma_R^a(\Gamma_0^a)^{-1}` gives

```math
\Gamma_R^aP_{ab}(\Gamma_0^b)^{-1}
=
J_R^aP_{ab}-J_R^a\widehat R_0^{ab}.
```

Therefore

```math
P_{ab}J_R^b-J_R^aP_{ab}
=
\widehat R_R^{ab}-J_R^a\widehat R_0^{ab}.
```

The norm estimate follows from the cross-regulator module inequality and the
unitized bound on `J_R^a`. `square`

## 8. Theorem 8.1: Projective Transfer For Inverses

Assume Hypothesis IC and let

```math
D_R^{ab}:=P_{ab}J_R^b-J_R^aP_{ab}.
```

Then

```math
P_{ab}(J_R^b)^{-1}-(J_R^a)^{-1}P_{ab}
=
-(J_R^a)^{-1}D_R^{ab}(J_R^b)^{-1}.
```

Consequently,

```math
\|P_{ab}(J_R^b)^{-1}-(J_R^a)^{-1}P_{ab}\|_{\mu,R}^{a\leftarrow b}
\le
C_{\rm mod}M_{J^{-1}}^2
\bigl(\varepsilon_R^{ab}+M_J\varepsilon_0^{ab}\bigr),
```

where `C_{\rm mod}` is the fixed decay-loss/module constant of the
cross-regulator norm.

### Proof

Starting from

```math
D_R^{ab}=P_{ab}J_R^b-J_R^aP_{ab},
```

multiply on the left by `(J_R^a)^{-1}` and on the right by `(J_R^b)^{-1}`:

```math
(J_R^a)^{-1}D_R^{ab}(J_R^b)^{-1}
=
(J_R^a)^{-1}P_{ab}-P_{ab}(J_R^b)^{-1}.
```

Rearrange to obtain the identity. The bound follows from Theorem 7.1 and the
module inequalities. `square`

## 9. Theorem 9.1: Projective Transfer For Exchange Defects

Let

```math
E_{R,S}^a
=
J_R^aJ_S^a(J_R^a)^{-1}(J_S^a)^{-1}.
```

Assume Hypothesis IC for both `R` and `S`, and assume the corridor
cross-regulator norm is a bimodule over the corresponding anchored algebras.
Then

```math
\|P_{ab}E_{R,S}^b-E_{R,S}^aP_{ab}\|_{\mu,R:S}^{a\leftarrow b}
\le
C_E\Bigl(
\varepsilon_R^{ab}+\varepsilon_S^{ab}
+\varepsilon_0^{ab}
\Bigr),
```

where `C_E` depends only on the unitized anchored bounds for `J_R,J_S` and
their inverses, and on the fixed decay-loss constants, not on total volume.

### Proof

Use the telescoping identity for products:

```math
P B_1B_2B_3B_4-A_1A_2A_3A_4P
=
\sum_{k=1}^4
A_1\cdots A_{k-1}
\bigl(PB_k-A_kP\bigr)
B_{k+1}\cdots B_4,
```

with

```math
(B_1,B_2,B_3,B_4)
=
(J_R^b,J_S^b,(J_R^b)^{-1},(J_S^b)^{-1})
```

and the analogous coarse factors `A_k`. The four cross terms are controlled by
Theorems 7.1 and 8.1 for anchors `R` and `S`. The corridor norm absorbs
left/right multiplication by anchored unitized factors. Summing the four
bounds gives the stated estimate. `square`

## 10. Corollary 10.1: First V3 Interacting Projective Inverse-Control Theorem

Consider a projective regulator family of bounded finite-range interacting
systems with:

1. uniformly finite local configuration dimension;
2. uniformly bounded degree, range, and local interaction strength;
3. common-support anchored collar deformations;
4. LC-log constants supplied by the V2 paired-word/KP theorem uniformly along
   the regulator family;
5. reference-renormalized primitive residuals satisfying Hypothesis IC.

Then `J_R`, `J_R^{-1}`, and `E_{R,S}` are projectively compatible in the
anchored/corridor topologies. The estimates are volume-uniform and vanish along
the chosen refinement path whenever the renormalized primitive residuals
vanish.

This is the first clean V3 interacting inverse-control theorem.

It is not yet interacting stochastic curvature. It is the infrastructure
needed before an interacting stochastic-curvature theorem can be honest.

## 11. Benchmark A: Bounded Interacting Chain With Declared Projective Fibers

The first benchmark should not be the full continuum Dirac scaling. A naive
Dirac lattice Hamiltonian usually has hopping strength of order `1/a`, which
falls outside the bounded finite-range LC-log theorem unless the slab size is
scaled and the KP constants are reproved. The first honest interacting
benchmark is therefore a bounded qudit/Dirac-chain surrogate.

Let `\Lambda_a` be a bounded-degree one-dimensional cell complex. At each cell
take a finite configuration set `C_x`, for example a qudit surrogate for local
fermion occupation. Let

```math
X_a=\prod_{x\in\Lambda_a}C_x,
\qquad
\mathcal H_a=\ell^2(X_a).
```

Choose a bounded finite-range interacting Hamiltonian

```math
H_0^a
=
\sum_x h_x^{\rm loc}
+\sum_{\langle x,y\rangle}h_{xy}^{\rm hop}
+g\sum_{\langle x,y\rangle}q_xq_y,
```

with

```math
\|h_x^{\rm loc}\|,\|h_{xy}^{\rm hop}\|,|g|\|q_xq_y\|\le J_*,
```

uniformly in `a`. The symbol `h^{\rm hop}` is meant only as a bounded
finite-dimensional analogue of the Dirac hopping term. The CAR/Fock lift and
true relativistic dispersion are not part of this Gamma-level theorem.

For a collar `R`, let

```math
H_R^a=H_0^a-C_R^a,
```

where `C_R^a` is a finite-range common-collar term supported in the same local
interaction family as `H_0^a`. The primitive whole-process kernels are

```math
\Gamma_0^a(\Delta)=\left|e^{-i\Delta H_0^a}\right|^2,
\qquad
\Gamma_R^a(\Delta)=\left|e^{-i\Delta H_R^a}\right|^2.
```

This use of a Hamiltonian is representational: it declares one whole-process
endpoint kernel. It is not a Markov product through hidden intermediate times.

For a refinement `b\succeq a`, take a finite fiber configuration space

```math
Y_{ab}=\prod_{u\in F_{ab}}D_u
```

with uniformly bounded local dimension, degree, range, and local interaction
strength. The fine configuration space is

```math
X_b=X_a\times Y_{ab},
```

and the coarse-graining map is the marginal

```math
(P_{ab}p)(x)=\sum_{y\in Y_{ab}}p(x,y).
```

Equivalently, `P_{ab}` is the column-stochastic readout that forgets the
declared refinement fiber. This is a projective readout, not a time evolution
and not a hidden Markov step.

The fine Hamiltonians are the tensor-sum whole-process lifts

```math
H_0^b
=
H_0^a\otimes I_{Y_{ab}}+I_{X_a}\otimes K_0^{ab},
```

```math
H_R^b
=
H_R^a\otimes I_{Y_{ab}}+I_{X_a}\otimes K_R^{ab},
```

where `K_0^{ab}` and `K_R^{ab}` are bounded finite-range fiber Hamiltonians,
with `K_R^{ab}-K_0^{ab}` supported only over the fiber cells above the same
collar `R`. The coarse chain may be genuinely interacting through the
`gq_xq_y` term; the refinement fibers may also carry local dynamics. What is
special is only that the refinement is a declared tensor/projective fiber
extension, so the coarse readout is exact.

This benchmark is deliberately conservative. It proves that interacting
inverse control is compatible with projective refinement in at least one
nontrivial interacting class. It does not yet prove continuum spatial
refinement or QFT reconstruction.

## 12. Exact Primitive Endpoint Refinement

### Proposition 12.1: Exact Projective Naturality Of The Fiber Benchmark

In Benchmark A, define

```math
\Phi_0^{ab}(\Delta)=\left|e^{-i\Delta K_0^{ab}}\right|^2,
\qquad
\Phi_R^{ab}(\Delta)=\left|e^{-i\Delta K_R^{ab}}\right|^2.
```

Then

```math
\Gamma_0^b=\Gamma_0^a\otimes\Phi_0^{ab},
\qquad
\Gamma_R^b=\Gamma_R^a\otimes\Phi_R^{ab}.
```

Consequently,

```math
P_{ab}\Gamma_0^b=\Gamma_0^aP_{ab},
\qquad
P_{ab}\Gamma_R^b=\Gamma_R^aP_{ab}.
```

Thus the primitive residuals vanish exactly:

```math
R_0^{ab}=0,
\qquad
R_R^{ab}=0.
```

### Proof

The tensor-sum Hamiltonians commute across the coarse/fiber tensor factors, so

```math
e^{-i\Delta H_0^b}
=
e^{-i\Delta H_0^a}\otimes e^{-i\Delta K_0^{ab}},
```

and similarly for `R`. Entrywise squared modulus preserves tensor products,
giving the displayed factorization of `Gamma_0^b` and `Gamma_R^b`.

Every `\Phi_*^{ab}` is column-stochastic. Therefore, for any probability vector
`p(x,y)`,

```math
\sum_y
\sum_{x',y'}
\Gamma_*^a(x|x')\Phi_*^{ab}(y|y')p(x',y')
=
\sum_{x'}\Gamma_*^a(x|x')\sum_{y'}p(x',y').
```

This is exactly `P_{ab}\Gamma_*^b=\Gamma_*^aP_{ab}`. `square`

## 13. The Hard Estimate In The Benchmark

### Theorem 13.1: Reference-Renormalized Residuals Vanish Exactly

Assume `\Gamma_0^a` and `\Gamma_0^b` are invertible in the slab window under
discussion. In Benchmark A,

```math
\widehat R_0^{ab}
=
R_0^{ab}(\Gamma_0^b)^{-1}
=0,
```

and

```math
\widehat R_R^{ab}
=
R_R^{ab}(\Gamma_0^b)^{-1}
=0.
```

Therefore Hypothesis IC holds with

```math
\varepsilon_0^{ab}=\varepsilon_R^{ab}=0
```

for every refinement pair.

### Proof

This is immediate from Proposition 12.1. The point is not algebraic difficulty;
the point is conceptual cleanliness. The reference inverse can amplify raw
errors, but here the raw projective residuals are exactly zero before the
inverse is applied. Hence there is nothing for the fine reference inverse to
amplify. `square`

### Comment: Why This Is Barandes-Aligned

The factorization above is not a Markov factorization through intermediate
times. It is a tensor factorization of one declared endpoint operation on a
larger configuration space. The primitive stochastic object remains the
whole-process kernel `Gamma_*^b`. The map `P_{ab}` is a final/initial readout
between regulator descriptions, not a dynamical stage.

## 14. Uniform LC-Log Verification For Benchmark A

### Proposition 14.1: Uniform LC-Log Constants

There exists a slab radius `\rho_*>0`, depending only on the bounded-geometry
constants

```math
(J_*,r,b,d_{\rm loc},\mu,\mu')
```

and not on total volume or refinement depth, such that for
`|\Delta|\le\rho_*` Benchmark A satisfies the V2 finite-slab LC-log theorem.
In particular, for every collar `R`,

```math
\|J_R^a-I\|_{\mu',R}^{a}\le C_J\Delta^2,
\qquad
\|(J_R^a)^{-1}-I\|_{\mu',R}^{a}\le C_{J^{-1}}\Delta^2,
```

with constants independent of `a`, and similarly at regulator `b`.

### Proof

The Hamiltonians `H_0^a,H_R^a,H_0^b,H_R^b` are bounded finite-range sums on
bounded-degree complexes with uniformly finite local dimension. The collar
difference `C_R` is supported in the same local interaction family at every
regulator. The fiber terms add local supports but do not change the bounded
degree, range, or local dimension constants beyond the declared uniform
bounds.

Thus the hypotheses of V2 Paper 3 Proposition 10 apply uniformly. The
operator-valued paired-word/KP expansion gives a volume-uniform analytic
branch for the connected logarithmic defect

```math
L_R^a=\log J_R^a
```

and the anchored estimate

```math
\|L_R^a\|_{\mu',R}^{a}\le C_L\Delta^2.
```

The Banach-algebra exponential calculus gives

```math
J_R^a=e^{L_R^a},
\qquad
(J_R^a)^{-1}=e^{-L_R^a},
```

and hence the displayed bounds after shrinking `\rho_*` if necessary. `square`

## 15. Benchmark Projective Inverse-Control Theorem

### Theorem 15.1: Exact Interacting Projective Inverse Control In Benchmark A

For Benchmark A, in the slab window `|\Delta|\le\rho_*`,

```math
P_{ab}J_R^b=J_R^aP_{ab},
```

```math
P_{ab}(J_R^b)^{-1}=(J_R^a)^{-1}P_{ab},
```

and for every pair of collars `R,S`,

```math
P_{ab}E_{R,S}^b=E_{R,S}^aP_{ab}.
```

Moreover, the exchange defect has the V2 corridor/window tail estimate

```math
\|E_{R,S}^a-I\|_{>w}^{(1),R:S}
\le
C\Delta^4e^{-\nu(d_{R,S}+w)}
```

with constants independent of total volume and refinement depth.

### Proof

The first identity follows from Theorem 7.1 and Theorem 13.1:

```math
P_{ab}J_R^b-J_R^aP_{ab}
=
\widehat R_R^{ab}-J_R^a\widehat R_0^{ab}
=0.
```

The inverse identity follows from Theorem 8.1. The exchange identity follows
from the telescoping estimate in Theorem 9.1 with all comparison and inverse
defects equal to zero.

Finally, Proposition 14.1 supplies the LC-log anchored bounds for `J_R`,
`J_S`, and their inverses. V2 Paper 3's exchange-defect corridor/window theorem
then gives

```math
\|E_{R,S}^a-I\|_{>w}^{(1),R:S}
\le
C_{\mu,\nu}
e^{-\nu(d_{R,S}+w)}
\kappa_R\kappa_SM_R^-M_S^-.
```

Since LC-log gives `\kappa_R,\kappa_S=O(\Delta^2)` and bounded inverse
unitized norms in the slab, this is the stated `O(\Delta^4)` corridor tail.
`square`

## 16. Spatial Dirac-Chain Refinement Gate

Benchmark A proves that the abstract theorem is not empty. It is not yet the
continuum spatial Dirac-chain theorem. A true spatial refinement must replace
the exact fiber extension by block coarse-graining between different lattices.
That is where the hard estimate lives.

Let `b` be a spatial refinement of `a`, for example spacing `a/2` refining
spacing `a`. Let

```math
P_{ab}: \Delta(X_b)\to\Delta(X_a)
```

be a declared block readout. Let the bounded or scaled Dirac-chain surrogates
be

```math
H_0^a
=
H_{\rm D,lat}^a+g_a\sum_{\langle x,y\rangle}q_xq_y,
\qquad
H_R^a=H_0^a-C_R^a.
```

If `\|H_{\rm D,lat}^a\|_{\rm local}` grows like `1/a`, then the slab must be
scaled so that the KP smallness parameter remains bounded:

```math
|\Delta(a)|\,J(a)\le\rho_{\rm KP}.
```

This is not a cosmetic condition. Without it, V2 Proposition 10 does not
provide uniform LC-log constants.

### Named Readout: Dyadic Occupation-Block Marginal

For the first spatial theorem use the dyadic refinement `b=a/2`. In the
one-particle site-spin sector, define

```math
\pi_{ab}(2n,\sigma)=\pi_{ab}(2n+1,\sigma)=(n,\sigma),
```

and let

```math
(P_{ab}p)(n,\sigma)
=
\sum_{\epsilon=0}^{1}p(2n+\epsilon,\sigma).
```

For finite occupation sectors, use the product block readout obtained by
applying the same local marginal to each dyadic block, with an explicit
overflow or failure record whenever the chosen coarse alphabet cannot represent
the fine block occupation. All estimates below are stated on the successful
block-compatible sector, or equivalently in the record-conditioned
cross-regulator seminorm. This is a declared readout/instrument, not a
dynamical stage.

This readout is intentionally simple. It does not attempt to reconstruct
high-frequency fine modes. Its job is to test whether whole-process endpoint
kernels are compatible after a physically declared coarse spatial readout.

### Hypothesis SR: Spatial Refinement Residual Control

For a spatial Dirac-chain refinement family, require activity-level matching
rather than raw matrix matching. In the operator-valued KP expansion of the
projected fine endpoint kernel and the coarse endpoint kernel, suppose the
difference activities satisfy

```math
\mathfrak a_{\mu}^{ab}(\delta\zeta_0)\le \eta_0^{ab},
\qquad
\mathfrak a_{\mu,R}^{ab}(\delta\zeta_R)\le \eta_R^{ab},
```

with

```math
\eta_0^{ab},\eta_R^{ab}\to0
```

along the spatial refinement path, and with the same KP smallness radius as
the reference activities. The marked activity `\delta\zeta_R` must be anchored
at the collar plus block-boundary mismatch region. This is the mathematical
form of "coarse and fine whole-process endpoint laws agree locally after
renormalization."

### Theorem 16.1: Thin-Slab SR For Dyadic Blocks With `1/a` Hopping

Consider the dyadic block readout above for a one-dimensional Dirac-chain
surrogate whose local Hamiltonian has the form

```math
H_0^a
=
\frac1aK^a+V^a,
\qquad
H_R^a=H_0^a-C_R^a.
```

Assume:

1. `K^a,V^a,C_R^a` are finite-range sums with uniformly bounded local
   coefficients and bounded degree;
2. `V^a` contains the bounded density-density or qudit interaction terms, with
   coupling `g_a` uniformly bounded or at most satisfying
   `|\Delta(a)|\,|g_a|\to0`;
3. the same assumptions hold at spacing `b=a/2`;
4. the slab is thin relative to the hopping scale:
   ```math
   \theta(a):=\frac{|\Delta(a)|}{a}\to0,
   ```
   and, for KP analyticity,
   ```math
   \theta(a)\le\theta_{\rm KP}
   ```
   for a sufficiently small regulator-independent constant.

Then the dyadic block readout satisfies Hypothesis SR with

```math
\eta_0^{ab}
\le
C_{\rm SR}\bigl(\theta(a)^2+|\Delta(a)|^2|g_a|^2\bigr),
```

and

```math
\eta_R^{ab}
\le
C_{\rm SR,R}\bigl(\theta(a)^2+|\Delta(a)|^2|g_a|^2\bigr),
```

after the usual decay loss `\mu\to\mu'`. The constants depend on bounded
geometry, local dimension, interaction range, and the collar scaffold, but not
on total volume. Hence

```math
\eta_0^{ab},\eta_R^{ab}\to0
```

whenever `\Delta(a)/a\to0` and `|\Delta(a)|\,|g_a|\to0`.

### Proof

Write the endpoint unitary as

```math
U_a(\Delta)=e^{-i\Delta H_0^a}.
```

The local norm of the hopping part is `O(a^{-1})`, so the Duhamel word
parameter for a local hopping factor is

```math
\theta(a)=|\Delta(a)|/a.
```

The bounded interaction parameter is

```math
\upsilon(a)=|\Delta(a)|\,|g_a|.
```

In a Born-squared endpoint kernel, a configuration-changing transition requires
at least one off-diagonal amplitude in `U_a` and its conjugate. Therefore the
first nontrivial stochastic activity has size bounded by

```math
C\bigl(\theta(a)^2+\upsilon(a)^2\bigr)
```

in the local column-sum activity norm. Mixed hopping-interaction words are
bounded by the same expression after increasing `C`, because
`\theta,\upsilon` are inside a fixed small polydisc. Pure diagonal interaction
phases do not create a configuration-changing stochastic activity by
themselves; they only enter through mixed words.

The dyadic readout `P_{ab}` is local, column-stochastic, and norm-contractive
in the local column-sum activity norms. Thus the activity mismatch between the
projected fine endpoint kernel and the coarse endpoint kernel is bounded by
the sum of their non-identity local activities:

```math
\mathfrak a_\mu^{ab}(\delta\zeta_0)
\le
C_{\rm SR}\bigl(\theta(a)^2+\upsilon(a)^2\bigr).
```

For the collar-deformed kernel the same argument applies, except that marked
activities must contain either a collar factor or a block-boundary mismatch
linked to the collar scaffold. The common-collar finite-range assumption gives
the anchored version

```math
\mathfrak a_{\mu,R}^{ab}(\delta\zeta_R)
\le
C_{\rm SR,R}\bigl(\theta(a)^2+\upsilon(a)^2\bigr).
```

The dyadic block map does not introduce long-range support: the image of a
connected fine activity is contained in the corresponding connected coarse
block neighborhood, with diameter changed only by a fixed factor. The
bounded-degree lattice-animal constants therefore remain uniform after
coarse-graining.

Finally, `\theta(a)\le\theta_{\rm KP}` puts both the coarse and fine
operator-valued polymer gases inside the KP smallness radius. Hence the two
displayed activity mismatch bounds are exactly Hypothesis SR, with
`\upsilon(a)=|\Delta(a)||g_a|`. `square`

### Proposition 16.2: Fixed `\Delta/a` Is Not An All-Mode SR Theorem

The thin-slab condition in Theorem 16.1 is not just a proof artifact. For the
dyadic block marginal, an all-mode operator-norm SR theorem at fixed nonzero

```math
\liminf_{a\to0}|\Delta(a)|/a>0
```

is not available from the present data.

Already in the free one-particle chain, start from a fine site at a block edge.
In time `\Delta`, the fine central-difference hopping sends probability of
order `(\Delta/a)^2` across one of the two fine bonds adjacent to that site.
After dyadic marginalization, one of those hops remains inside the same coarse
cell while the other exits to a neighboring coarse cell. The coarse lattice
kernel distributes its order-`(\Delta/a)^2` probability according to the coarse
two-neighbor stencil. The two column laws differ by a local amount of order
`(\Delta/a)^2` unless extra low-pass/smooth-sector structure is declared.
Thus a fixed nonzero `\Delta/a` leaves a nonvanishing all-mode block mismatch.

The Barandes-compatible repair is not to pretend that the fine process is
Markov-divisible or that high-frequency modes disappear. One must either:

1. work in the thin-slab regime of Theorem 16.1;
2. add a declared low-momentum/smooth-sector readout and prove sector
   invariance; or
3. change the regulator by a Wilson/staggered/doubler-controlled construction
   and prove the corresponding block-spin RG estimate.

### Low-Momentum Readout Route

The first fixed-ratio repair is the low-momentum route. It is not Gamma-only.
It uses the enriched representation data already isolated in V3 Paper 1 and
the sampled-sector discipline from V2 Papers 7-9.

Choose a physical momentum cutoff `\Lambda(a)` such that

```math
\Lambda(a)\to\infty,
\qquad
a\Lambda(a)\to0,
\qquad
a^2\Lambda(a)^3\to0.
```

Let `\Pi_a^{\rm low}` be the lattice Fourier projection onto
`|p|\le\Lambda(a)`. The projection is not a stochastic map on configurations.
Therefore define it as a declared instrument:

```text
accept low sector -> coherent projection Pi_a^low followed by configuration readout,
reject high sector -> an explicit reject record.
```

At the kernel level this means that every low-sector theorem is stated in the
accepted branch, with the reject probability retained as a record. No
unrecorded projection is being silently inserted into the dynamics.

For a dyadic refinement `b=a/2`, let

```math
B_{ab}^{\rm low}:\Pi_b^{\rm low}\mathcal H_b\to \Pi_a^{\rm low}\mathcal H_a
```

be the Fourier block map that identifies the shared physical low-momentum
Fourier modes and then samples them on the coarse lattice. Let

```math
P_{ab}^{\rm low}:=\Gamma(B_{ab}^{\rm low})
```

denote the accepted-branch sub-stochastic readout; adding the explicit reject
record makes the full instrument column-stochastic. This is a readout between
declared low-sector records, not a dynamical Markov step.

### Theorem 16.3: Low-Sector Stability At Fixed `\Delta/a`

Let

```math
\Delta(a)=\lambda a+o(a),
\qquad
0<|\lambda|\le\lambda_{\rm KP},
```

where `\lambda_{\rm KP}` is small enough to keep the hopping activities inside
the KP radius. Assume:

1. the free lattice Dirac part is the central-difference generator on the
   principal Brillouin branch;
2. the collar deformation is sampled from a fixed smooth compactly supported
   lapse/collar profile, not a sharp deleted-bond characteristic function;
3. the interaction part is bounded finite range with coupling `g_a` satisfying
   `a|g_a|\to0`;
4. sampled smooth test states have super-polynomial high-momentum tails as in
   V2 Paper 7.

Let `Q_a^{\rm high}=I-\Pi_a^{\rm low}`. Then, uniformly for sampled smooth
states in a bounded Sobolev class,

```math
\|Q_a^{\rm high}e^{-i\Delta(a)H_R^a}\Pi_a^{\rm low}\|
_{\rm sm}
\le
C_\lambda\bigl(a^2\Lambda(a)^3+\tau_N(a)+a|g_a|\bigr),
```

where `\tau_N(a)=O_N(a^N)` is the sampled high-momentum tail. The same estimate
holds for `H_0^a`.

Consequently the reject probability of the declared low-sector instrument
vanishes on the tested smooth sector.

### Proof

For the translation-invariant free Dirac part, Fourier modes are invariant.
The only low-sector error is the symbol mismatch

```math
\frac{\sin(ap)}{a}-p=O(a^2|p|^3)
```

on `|p|\le\Lambda(a)`, giving the standard
`a^2\Lambda(a)^3` sampled-sector bound from V2 Papers 7-9.

A smooth collar profile acts in Fourier variables by convolution with a
rapidly decaying Fourier transform. Since `a\Lambda(a)\to0`, the distance from
the accepted low sector to the Brillouin edge diverges in physical momentum
units. The leakage from a sampled smooth low-sector state into
`Q_a^{\rm high}` is therefore bounded by the same symbol error plus the
super-polynomial tail `\tau_N(a)`.

The bounded interaction contributes by Duhamel:

```math
Q_a^{\rm high}e^{-i\Delta(H_{\rm free}+g_aV)}
\Pi_a^{\rm low}
=
-i\int_0^\Delta
Q_a^{\rm high}e^{-i(\Delta-s)H_R^a}g_aV
e^{-isH_{\rm free}}\Pi_a^{\rm low}\,ds
+\text{free/collar leakage},
```

so its contribution is at most `C|\Delta(a)|\,|g_a|=C|\lambda|a|g_a|+o(a|g_a|)`.
Combining the bounds proves the estimate. `square`

### Theorem 16.4: Fixed-Ratio Low-Sector SR

Under the assumptions of Theorem 16.3, the accepted low-sector readout
`P_{ab}^{\rm low}` satisfies Hypothesis SR in the smooth-sector
cross-regulator seminorm, with

```math
\eta_{0,\rm low}^{ab}
\le
C_\lambda\bigl(
a^2\Lambda(a)^3+\tau_N(a)+a|g_a|+|\Delta(a)/a-\lambda|
\bigr),
```

and

```math
\eta_{R,\rm low}^{ab}
\le
C_{\lambda,R}\bigl(
a^2\Lambda(a)^3+\tau_N(a)+a|g_a|+|\Delta(a)/a-\lambda|
\bigr).
```

In particular, if

```math
a^2\Lambda(a)^3\to0,
\qquad
a|g_a|\to0,
\qquad
\Delta(a)/a\to\lambda,
```

then

```math
\eta_{0,\rm low}^{ab},\eta_{R,\rm low}^{ab}\to0.
```

Thus Hypothesis SR is proved for the fixed-ratio low-momentum readout.

### Proof

On the accepted low sector, both the coarse and fine lattice generators
converge to the same continuum smooth Dirac generator on the tested Sobolev
class. More precisely,

```math
\|H_a\Pi_a^{\rm low}\iota_af-\iota_aH_Df\|
\le
C(a^2\Lambda(a)^3+\tau_N(a))+O(|g_a|),
```

and the interaction contribution is used only after integration over the slab,
where it becomes `O(a|g_a|)`. The same estimate holds at spacing
`b=a/2`, and the Fourier block map `B_{ab}^{\rm low}` identifies the shared
physical low modes up to the sampling residual already included in `\tau_N(a)`.

Duhamel's formula over the common physical slab gives, for accepted smooth
states,

```math
\|B_{ab}^{\rm low}e^{-i\Delta(a)H_0^b}
-e^{-i\Delta(a)H_0^a}B_{ab}^{\rm low}\|
_{\rm sm}
\le
C_\lambda\bigl(
a^2\Lambda(a)^3+\tau_N(a)+a|g_a|+|\Delta(a)/a-\lambda|
\bigr).
```

The same proof with one marked smooth collar factor gives the anchored
estimate for `H_R`. The smooth-collar assumption is essential here: a sharp
deleted-bond collar has high-momentum Fourier content and is covered only by
the obstruction in Proposition 16.2 unless an additional regulator is supplied.

Finally, the map `U\mapsto |U|^2` is locally Lipschitz from unitary matrix
elements to tested probability laws:

```math
\bigl||u|^2-|v|^2\bigr|
\le
2|u-v|
```

for unit-norm columns. Therefore the accepted-branch Born-squared endpoint
kernels obey the same vanishing bound in the smooth-sector cross-regulator
seminorm. These are precisely the two Hypothesis SR estimates. `square`

### Theorem 16.5: Marked-KP Criterion For Renormalized Spatial Residuals

Assume the spatial refinement family satisfies the KP smallness hypotheses and
Hypothesis SR. Then, after the standard decay loss `\mu\to\mu'`,

```math
\|\widehat R_0^{ab}\|_{\mu'}^{a\leftarrow b}
\le
C_{\rm KP}\eta_0^{ab},
```

and

```math
\|\widehat R_R^{ab}\|_{\mu',R}^{a\leftarrow b}
\le
C_{\rm KP}\eta_R^{ab}
+C_{\rm KP}'\eta_0^{ab}.
```

Consequently the spatial Dirac-chain family satisfies Hypothesis IC whenever
the activity mismatch parameters vanish.

### Proof

The projected fine kernel and the coarse kernel are written as two
Banach-valued polymer gases in the same cross-regulator algebra. Their
difference is represented by marked activities `\delta\zeta`. The
reference-renormalized residual is the relative defect: a marked endpoint
polymer gas multiplied by the inverse of the unmarked fine reference gas.

The operator-valued KP logarithm from V2 Paper 3 applies because all activities
remain inside the common smallness radius. Multiplication by the inverse of the
unmarked gas cancels disconnected unmarked reference clusters. The logarithm
of the relative object is therefore a sum of connected incompatibility
clusters containing at least one marked activity. The marked-cluster estimate
gives

```math
C_{\rm KP}\mathfrak a_{\mu}(\delta\zeta_0)
```

for the reference residual and

```math
C_{\rm KP}\mathfrak a_{\mu,R}(\delta\zeta_R)
+C_{\rm KP}'\mathfrak a_{\mu}(\delta\zeta_0)
```

for the deformed residual. The second term appears because the collar-relative
comparison also inherits any reference mismatch. These are exactly the two
displayed bounds. `square`

This theorem is the realistic route to spatial refinement. It does not assume
a global bound on `(\Gamma_0^b)^{-1}`. It proves the renormalized estimate by
the same Barandes-compatible whole-process cluster logic used for LC-log:
compare whole endpoint laws and keep only connected marked differences.

## 17. Exchange-Corridor Consequences For Spatial Refinement

The purpose of Theorems 7.1, 8.1, and 9.1 is exactly to turn SR-type endpoint
residual estimates into comparison-map, inverse-map, and exchange-defect
projective control. We now spell this out for both spatial routes.

### Theorem 17.1: Spatial Transfer Through `J`, `J^{-1}`, And `E`

Assume Hypothesis SR and the KP hypotheses of Theorem 16.5. Let

```math
\chi_R^{ab}:=\eta_R^{ab}+\eta_0^{ab}.
```

Then Theorems 7.1 and 16.5 imply

```math
\|P_{ab}J_R^b-J_R^aP_{ab}\|_{\mu',R}^{a\leftarrow b}
\le
C_R\chi_R^{ab}.
```

If the LC-log unitized inverse bounds hold uniformly, then Theorem 8.1 gives

```math
\|P_{ab}(J_R^b)^{-1}-(J_R^a)^{-1}P_{ab}\|_{\mu',R}^{a\leftarrow b}
\le
C_{{\rm inv},R}\chi_R^{ab}.
```

For two collars `R,S`, Theorem 9.1 gives

```math
\|P_{ab}E_{R,S}^b-E_{R,S}^aP_{ab}\|_{\mu',R:S}^{a\leftarrow b}
\le
C_{E,R:S}(\eta_R^{ab}+\eta_S^{ab}+\eta_0^{ab}).
```

The constants depend on the LC-log unitized bounds, the module constants, the
decay loss `\mu\to\mu'`, and the collar scaffolds, but not on total volume.

### Proof

Theorem 16.5 gives reference-renormalized residual bounds:

```math
\|\widehat R_0^{ab}\|\le C_{\rm KP}\eta_0^{ab},
\qquad
\|\widehat R_R^{ab}\|\le C_{\rm KP}\eta_R^{ab}
+C_{\rm KP}'\eta_0^{ab}.
```

Substitute these into Theorem 7.1:

```math
P_{ab}J_R^b-J_R^aP_{ab}
=
\widehat R_R^{ab}-J_R^a\widehat R_0^{ab}.
```

The module bound for multiplication by `J_R^a` gives the comparison estimate.
The inverse estimate is Theorem 8.1 applied to that comparison defect. The
exchange estimate is Theorem 9.1 applied to the four factors
`J_R,J_S,J_R^{-1},J_S^{-1}`. No new stochastic or Markov composition is used;
these are algebraic identities for declared whole-process endpoint kernels and
declared projective readouts. `square`

### Corollary 17.2: Thin-Slab Dyadic Transfer

For the named dyadic readout of Theorem 16.1, set

```math
\zeta_{\rm thin}^{ab}
:=
\theta(a)^2+|\Delta(a)|^2|g_a|^2,
\qquad
\theta(a)=|\Delta(a)|/a.
```

Then

```math
\|P_{ab}J_R^b-J_R^aP_{ab}\|_{\mu',R}^{a\leftarrow b}
\le
C_{\rm thin,R}\zeta_{\rm thin}^{ab},
```

```math
\|P_{ab}(J_R^b)^{-1}-(J_R^a)^{-1}P_{ab}\|_{\mu',R}^{a\leftarrow b}
\le
C_{\rm thin,inv,R}\zeta_{\rm thin}^{ab},
```

and

```math
\|P_{ab}E_{R,S}^b-E_{R,S}^aP_{ab}\|_{\mu',R:S}^{a\leftarrow b}
\le
C_{\rm thin,E,R:S}\zeta_{\rm thin}^{ab}.
```

If in addition the LC-log corridor constants are uniform along the spatial
refinement path, then the exchange defect retains the outside-window tail

```math
\|E_{R,S}^a-I\|_{>w}^{(1),R:S}
\le
C\bigl(\zeta_{\rm thin}^{ab}\bigr)^2e^{-\nu(d_{R,S}+w)}.
```

Thus the dyadic block theorem proves projective transfer in the thin-slab
regime `\Delta(a)/a\to0`.

### Corollary 17.3: Fixed-Ratio Low-Momentum Transfer

For the declared low-momentum accepted branch of Theorem 16.4, set

```math
\zeta_{\rm low}^{ab}(\lambda)
:=
a^2\Lambda(a)^3+\tau_N(a)+a|g_a|+|\Delta(a)/a-\lambda|.
```

Then, in the accepted smooth-sector cross-regulator seminorm,

```math
\|P_{ab}^{\rm low}J_R^b-J_R^aP_{ab}^{\rm low}\|_{\rm sm,R}
\le
C_{\lambda,R}\zeta_{\rm low}^{ab}(\lambda),
```

```math
\|P_{ab}^{\rm low}(J_R^b)^{-1}-(J_R^a)^{-1}P_{ab}^{\rm low}\|_{\rm sm,R}
\le
C_{\lambda,{\rm inv},R}\zeta_{\rm low}^{ab}(\lambda),
```

and

```math
\|P_{ab}^{\rm low}E_{R,S}^b-E_{R,S}^aP_{ab}^{\rm low}\|_{\rm sm,R:S}
\le
C_{\lambda,E,R:S}\zeta_{\rm low}^{ab}(\lambda).
```

Consequently, for smooth collars and the declared accepted low-sector
instrument,

```math
P_{ab}^{\rm low}J_R^b-J_R^aP_{ab}^{\rm low}\to0,
\qquad
P_{ab}^{\rm low}(J_R^b)^{-1}-(J_R^a)^{-1}P_{ab}^{\rm low}\to0,
```

and

```math
P_{ab}^{\rm low}E_{R,S}^b-E_{R,S}^aP_{ab}^{\rm low}\to0
```

whenever

```math
a^2\Lambda(a)^3\to0,
\qquad
a|g_a|\to0,
\qquad
\Delta(a)/a\to\lambda.
```

This is the completed push-through of Theorems 7.1, 8.1, and 9.1 for the
low-momentum fixed-ratio route. It is still not an all-mode theorem: the
projection/readout is a declared instrument with an explicit reject record, and
the result lives on the accepted smooth branch.

## 18. Closing The All-Mode Regulator Gap: Detail-Preserving Blocks

The failure in Proposition 16.2 is not a failure of all possible all-mode
regulators. It is a failure of the naive dyadic marginal, because that marginal
throws away the intra-block detail mode. A Barandes-compatible all-mode repair
must keep that detail as an actual declared record.

### Detail-Preserving Staggered Block Readout

For the dyadic refinement `b=a/2`, define the all-mode block map on the
one-particle site-spin basis by

```math
\pi_{ab}^{\rm st}(2n,\sigma)=(n,0,\sigma),
\qquad
\pi_{ab}^{\rm st}(2n+1,\sigma)=(n,1,\sigma).
```

The coarse configuration space is therefore not the naive one-site-per-block
space. It is the staggered/detail space

```math
X_a^{\rm st}
=
\Lambda_a\times\{0,1\}\times\{\uparrow,\downarrow\}.
```

Let

```math
P_{ab}^{\rm st}: \Delta(X_b)\to \Delta(X_a^{\rm st})
```

be the deterministic relabeling induced by `\pi_{ab}^{\rm st}`. This map is
column-stochastic and all-mode: no high-frequency state is rejected or
marginalized. The extra label `0,1` is the UV/detail record that the naive
marginal discarded.

For finite occupation sectors, apply the same relabeling to every occupied
cell, with the usual fermionic/CAR ordering or a declared qudit occupation
ordering as representation data. At Gamma level this is just a bijective
configuration relabeling.

### Theorem 18.1: Exact All-Mode SR For The Staggered Block Regulator

Let `b=a/2`. Suppose the coarse staggered Hamiltonians are defined by exact
transport of the fine whole-process generators:

```math
H_{0}^{a,{\rm st}}
=
U_{ab}^{\rm st}H_0^b(U_{ab}^{\rm st})^{-1},
\qquad
H_{R}^{a,{\rm st}}
=
U_{ab}^{\rm st}H_R^b(U_{ab}^{\rm st})^{-1},
```

where `U_{ab}^{\rm st}` is the Hilbert-space permutation implementing
`\pi_{ab}^{\rm st}`. Then, for every slab `\Delta` for which the reference
kernels are invertible,

```math
P_{ab}^{\rm st}\Gamma_0^b
=
\Gamma_0^{a,{\rm st}}P_{ab}^{\rm st},
\qquad
P_{ab}^{\rm st}\Gamma_R^b
=
\Gamma_R^{a,{\rm st}}P_{ab}^{\rm st}.
```

Thus

```math
R_{0,{\rm st}}^{ab}=0,
\qquad
R_{R,{\rm st}}^{ab}=0,
```

and the reference-renormalized residuals also vanish:

```math
\widehat R_{0,{\rm st}}^{ab}=0,
\qquad
\widehat R_{R,{\rm st}}^{ab}=0.
```

Consequently Hypothesis SR holds exactly, all modes included, for the
detail-preserving staggered block regulator.

### Proof

The map `U_{ab}^{\rm st}` is a basis permutation. Therefore

```math
e^{-i\Delta H_{*}^{a,{\rm st}}}
=
U_{ab}^{\rm st}e^{-i\Delta H_*^b}(U_{ab}^{\rm st})^{-1}.
```

Taking entrywise squared modulus gives

```math
\Gamma_*^{a,{\rm st}}
=
P_{ab}^{\rm st}\Gamma_*^b(P_{ab}^{\rm st})^{-1}
```

as a matrix identity, because `P_{ab}^{\rm st}` is the same permutation at the
stochastic level. Rearranging gives exact projective naturality for both
`*=0` and `*=R`. The residual and renormalized residual identities follow
immediately. `square`

### Theorem 18.2: All-Mode Fixed-Ratio Transfer For Staggered Blocks

Assume in addition that the transported staggered Hamiltonian is local on the
coarse staggered complex with uniformly bounded degree, finite range, and
local dimension, and that the fixed ratio

```math
\Delta(a)/a\to\lambda,
\qquad
|\lambda|\le\lambda_{\rm KP}^{\rm st},
```

keeps the operator-valued KP activities inside the smallness radius. Then
LC-log, inverse control, and exchange-corridor control hold uniformly for the
staggered all-mode regulator, and

```math
P_{ab}^{\rm st}J_R^b
=
J_R^{a,{\rm st}}P_{ab}^{\rm st},
```

```math
P_{ab}^{\rm st}(J_R^b)^{-1}
=
(J_R^{a,{\rm st}})^{-1}P_{ab}^{\rm st},
```

and

```math
P_{ab}^{\rm st}E_{R,S}^b
=
E_{R,S}^{a,{\rm st}}P_{ab}^{\rm st}.
```

The exchange defect retains the corridor tail

```math
\|E_{R,S}^{a,{\rm st}}-I\|_{>w}^{(1),R:S}
\le
C_{\rm st}(\lambda)\,e^{-\nu(d_{R,S}+w)}
```

with `C_{\rm st}(\lambda)=O(\lambda^4)` for small `\lambda`, uniformly in
total volume.

### Proof

The exact projective naturality and zero renormalized residuals are Theorem
18.1. The comparison-map, inverse-map, and exchange-defect identities are then
Theorems 7.1, 8.1, and 9.1 with zero right-hand side.

The only analytic input is LC-log at fixed ratio. The transported staggered
Hamiltonian has local coefficient scale `O(1/a)`, but the Duhamel activity is
controlled by the dimensionless product `|\Delta(a)|/a`, which tends to
`|\lambda|`. For `|\lambda|` smaller than the KP radius, the paired-word
operator-valued polymer expansion has uniform constants. The corridor estimate
then follows from the V2 exchange-window theorem. `square`

### What This Closes, And What It Does Not

This closes the all-mode projective regulator gap in the following precise
sense:

```text
naive all-mode marginal at fixed Delta/a: fails;
detail-preserving all-mode staggered block readout: exact SR and exact transfer.
```

The price is physical and important. The coarse regulator is not the naive
low-energy Dirac regulator. It carries an explicit parity/detail UV label. This
is the correct all-mode ontology: high-frequency/doubler data are not erased;
they are recorded. To recover standard low-energy QFT, a later theorem must
still show that the detail sector decouples, becomes massive by a Wilson term,
is removed by a declared low-sector instrument, or is interpreted as the
intended staggered species content.

## 19. Wilson/Staggered Continuum Decoupling Of The Detail Sector

The detail-preserving all-mode theorem solves the projective regulator problem.
It does not by itself say what low-energy continuum QFT is obtained. The
retained detail sector has two honest interpretations:

1. **Wilson interpretation:** add a local Wilson mass term so the detail/doubler
   sector becomes infinitely massive and decouples from finite-energy tests.
2. **Staggered interpretation:** keep the detail sector as a physical
   taste/species label, so the continuum target is a multi-taste Dirac theory
   unless a further taste projection or taste-breaking term is declared.

Both interpretations are Barandes-compatible because neither erases a degree
of freedom without a declared operation.

### Wilson Detail Gap

On the one-particle translation-invariant benchmark, use the Wilson lattice
Dirac symbol

```math
h_a^{W}(p)
=
\alpha\frac{\sin(ap)}{a}
+\beta\left(m+\frac r a(1-\cos(ap))\right),
\qquad
0<r<\infty.
```

Let `\Pi_a^{\rm phys}` be the physical low-momentum projector
`|p|\le\Lambda(a)` and let `\Pi_a^{\rm dbl}` be the doubler/detail projector
onto `|p-\pi/a|\le\Lambda(a)`, with

```math
\Lambda(a)\to\infty,
\qquad
a\Lambda(a)\to0.
```

### Theorem 19.1: Wilson Detail Sector Becomes Infinitely Massive

For the Wilson symbol above:

1. on the physical branch,
   ```math
   \sup_{|p|\le\Lambda(a)}
   \left\|
   h_a^W(p)-(\alpha p+m\beta)
   \right\|
   \le
   C\left(a\Lambda(a)^2+a^2\Lambda(a)^3\right);
   ```
2. on the doubler branch, for sufficiently small `a`,
   ```math
   \inf_{|p-\pi/a|\le\Lambda(a)}
   \operatorname{spec}|h_a^W(p)|
   \ge
   \frac r a-C(1+\Lambda(a)).
   ```

Consequently, for every fixed energy window `[-E,E]`, the spectral projection
of `h_a^W` onto that window has no doubler component for all sufficiently small
`a`, and the physical branch converges to the single massive Dirac generator.

### Proof

For `|p|\le\Lambda(a)`,

```math
\frac{\sin(ap)}{a}-p=O(a^2|p|^3),
\qquad
\frac1a(1-\cos(ap))=O(a|p|^2).
```

This gives the physical-branch estimate. On the doubler branch write
`p=\pi/a+k`, `|k|\le\Lambda(a)`. Then

```math
\sin(ap)=\sin(\pi+ak)=-\sin(ak),
```

and

```math
1-\cos(ap)=1-\cos(\pi+ak)=1+\cos(ak)=2+O(a^2k^2).
```

Thus the Wilson mass term is

```math
m+\frac{2r}{a}+O(ak^2),
```

while the kinetic term is `O(|k|)`. Since `a\Lambda(a)\to0`, the mass term
dominates and the displayed lower bound follows. The finite-energy spectral
projection statement is immediate. `square`

### Corollary 19.2: Wilson Decoupling For Tested ISP/QFT Data

Assume the projective all-mode staggered/detail regulator of Theorem 18.2 is
equipped with the Wilson term above and that tested states/effects have
uniformly bounded physical energy. Then the retained UV/detail sector is
harmless for low-energy continuum reconstruction:

```math
\Pi_a^{\rm dbl}\Pi_{[-E,E]}(h_a^W)=0
```

for small `a`, and all accepted finite-energy matrix elements of the
whole-process kernels converge to the single-species massive Dirac matrix
elements on the physical branch.

If bounded finite-range interactions are present on the tested finite-energy
sector and satisfy

```math
a\|V_a\|_{\rm tested}\to0,
```

then the physical/detail mixing induced by the interaction is suppressed by
the Wilson gap:

```math
\|\Pi_a^{\rm dbl}(H_a^W+V_a-z)^{-1}\Pi_a^{\rm phys}\|
\le
C_E\,a\|V_a\|_{\rm tested}
```

for `z` in compact subsets of the physical resolvent set. Hence the detail
sector decouples in the tested low-energy reconstruction limit.

### Proof

The first statement is Theorem 19.1 applied to the finite energy window. For
the interacting estimate, decompose the Hilbert space into physical and doubler
blocks. The doubler block has distance at least `c/a` from any fixed physical
energy window. The Schur/Feshbach resolvent identity bounds the off-diagonal
resolvent by the inverse gap times the interaction norm, giving
`O(a\|V_a\|_{\rm tested})`. `square`

### Staggered Detail As Taste/Species

Without a Wilson term, the detail label is not automatically a pathology. It is
a physical taste/species label unless the target theory says otherwise.

### Theorem 19.3: Staggered Detail Sector Converges To A Multi-Taste Dirac Target

For the detail-preserving staggered block regulator without Wilson mass, fold
the Brillouin zone into physical momentum `k` and detail/taste label
`\tau\in\{0,1\}`. On low folded momenta `|k|\le\Lambda(a)`, the transported
all-mode symbol has the form

```math
h_a^{\rm st}(k)
=
\begin{pmatrix}
\alpha k+m\beta & 0\\
0 & -\alpha k+m\beta
\end{pmatrix}
+O(a^2|k|^3),
```

up to a fixed taste-basis unitary. Therefore, after a taste rotation if
desired, the continuum target is a direct sum of Dirac tastes:

```math
H_{\rm cont}^{\rm st}
\simeq
H_D\oplus H_D
```

with the declared taste multiplicity. Thus the retained detail sector is
correctly interpreted as staggered species content, not as missing stochastic
data.

### Proof

The dyadic detail label folds the fine Brillouin zone into two branches: the
physical branch near `p=0` and the branch near `p=\pi/a`. The central
difference symbol on these branches is respectively

```math
\alpha\frac{\sin(ak)}{a}+m\beta
=
\alpha k+m\beta+O(a^2|k|^3),
```

and

```math
\alpha\frac{\sin(\pi+ak)}{a}+m\beta
=
-\alpha k+m\beta+O(a^2|k|^3).
```

These are the two diagonal taste blocks after the fixed folding transform.
The sign of the kinetic term in the second block is a taste/chirality
convention and may be absorbed into a fixed taste-spin rotation when the
representation data allow it. `square`

### Corollary 19.4: Detail-Sector Alternatives Are Exhaustive At This Level

At the present one-particle/projective-kernel level, the retained UV/detail
sector has the following rigorous alternatives:

```text
Wilson term present:
  detail/doubler branch has mass O(1/a) and decouples from finite-energy tests.

No Wilson term, staggered interpretation declared:
  detail branch is an additional Dirac taste/species in the continuum target.

No Wilson term and no taste/species interpretation:
  the single-species QFT claim is not justified.
```

This closes the Wilson/staggered continuum interpretation gap for Paper 3's
regulator theorem. It still does not reconstruct full QFT from bare `Gamma`;
it identifies which enriched representation target the projective kernels may
feed into.

## 20. Advancing The Detail-Preserving And Wilson Branches

The preceding section identifies the continuum meaning of the retained detail
sector. We now separate the common projective trunk from the two physical
branches.

```text
common trunk:
  retain the UV/detail label as declared data;
  prove all-mode projective transfer for J, J^{-1}, and E.

Wilson branch:
  add a Wilson mass term;
  prove that unwanted detail/doubler excitations leave finite-energy physics.

staggered branch:
  do not add a Wilson term;
  interpret the retained detail label as a physical taste/species index.
```

This is the Barandes-compatible way to push both routes. No degree of freedom
is silently discarded. It is either retained, made massive by a declared
regulator term, filtered by a declared instrument, or interpreted as physical
species content.

### Theorem 20.1: The Common Trunk Is Forced By All-Mode Refinement

Let `P_\pi` be a deterministic coarse readout induced by a map
`\pi:X_b\to X_a`. Suppose there exists a fine generator or whole-process
kernel `K_b` and a coarse object `K_a` such that exact all-mode projective
naturality holds,

```math
P_\pi K_b=K_aP_\pi.
```

If two fine states `x,y\in X_b` lie in the same coarse fiber,
`\pi(x)=\pi(y)`, then the induced outgoing coarse fluxes must agree:

```math
\sum_{\pi(z)=u}(K_b)_{z x}
=
\sum_{\pi(z)=u}(K_b)_{z y}
\qquad
\hbox{for every coarse state }u.
```

Consequently, any all-mode fixed-ratio readout that identifies two fine states
whose local Dirac/Wilson/staggered dynamics have different coarse outgoing
flux cannot satisfy exact projective naturality. For the dyadic Dirac block at
fixed nonzero `\Delta/a`, the ordinary marginal
`2n,2n+1\mapsto n` violates this condition. A Barandes-compatible all-mode
readout must therefore do at least one of the following:

1. retain the intra-block detail label;
2. declare a low-sector accepted branch with an explicit reject record;
3. restrict to a thin-slab regime where the offending mismatch vanishes;
4. introduce an additional declared stochastic instrument that records the
   coarse-graining loss.

In particular, the detail-preserving block readout of Section 18 is not a
cosmetic refinement. It is the common all-mode trunk on which both the Wilson
and staggered branches can be built.

### Proof

The equality `P_\pi K_b=K_aP_\pi` is an equality of columns. If
`\pi(x)=\pi(y)`, then `P_\pi e_x=P_\pi e_y`. Hence

```math
P_\pi K_b e_x
=
K_aP_\pi e_x
=
K_aP_\pi e_y
=
P_\pi K_b e_y.
```

The `u` component of this equality is precisely the displayed equality of
coarse outgoing fluxes. For the fixed-ratio dyadic Dirac block, Proposition
16.2 exhibits an `O((\Delta/a)^2)` mismatch between the two parity/detail
classes. Thus the ordinary marginal cannot be exact all-mode projective data.
The listed alternatives are exactly the ways to avoid erasing the mismatched
fine information. `square`

### Theorem 20.2: Wilson Finite-Particle Detail Decoupling

Work first in finite spatial volume, so all operators below are finite
matrices. Let `h_a^W` be the one-particle Wilson lattice Dirac generator of
Theorem 19.1. Let `\Pi_a^{\rm phys}` be the physical low-energy branch and
`\Pi_a^{\rm dbl}` the Wilson detail/doubler branch, with
`\Pi_a^{\rm phys}\Pi_a^{\rm dbl}=0`. Assume that, on the branch decomposition,

```math
\Pi_a^{\rm dbl}|h_a^W|\Pi_a^{\rm dbl}
\ge
G_a\Pi_a^{\rm dbl},
\qquad
G_a\ge c/a,
```

while the physical branch converges to the target Dirac branch on the tested
momentum window as in Theorem 19.1.

Let

```math
{\mathcal F}_{a,\le N}
=
\bigoplus_{n=0}^N \wedge^n {\mathcal H}_a
```

be the finite-particle cutoff CAR space over the one-particle cutoff Hilbert
space. Let `N_a^{\rm dbl}=d\Gamma(\Pi_a^{\rm dbl})` count Wilson
detail/doubler excitations, and let the free finite-particle energy be

```math
H_{a,\le N}^{W,0}=d\Gamma(|h_a^W|).
```

Write

```math
{\mathbb P}_a^{\rm phys}={\bf 1}_{\{N_a^{\rm dbl}=0\}},
\qquad
{\mathbb P}_a^{\rm dbl}={\bf 1}-{\mathbb P}_a^{\rm phys}
```

for the finite-particle physical and detail-containing blocks.

For every fixed particle cutoff `N` and fixed energy window `[0,E]`, the
finite-energy spectral projection satisfies

```math
N_a^{\rm dbl}\,
\Pi_{[0,E]}(H_{a,\le N}^{W,0})=0
```

for all sufficiently small `a`.

Now add a self-adjoint finite-volume interaction `V_a` on
`{\mathcal F}_{a,\le N}`. Write

```math
P={\mathbb P}_a^{\rm phys},
\qquad
Q={\mathbb P}_a^{\rm dbl}.
```

For a compact set `K` in the physical resolvent region, assume the tested
interaction bounds

```math
\|QV_aQ\|_{\le N,E}\le G_a/4,
\qquad
a\|QV_aP\|_{\le N,E}\to0,
```

and assume the physical Schur complement

```math
S_P(z)
=
P(H_{a,\le N}^{W,0}+V_a-z)P
-
PV_aQ\,
\left(Q(H_{a,\le N}^{W,0}+V_a-z)Q\right)^{-1}
QV_aP
```

is invertible on `K` with `\sup_{z\in K}\|S_P(z)^{-1}\|\le M_K`. Then

```math
\sup_{z\in K}
\left\|
{\mathbb P}_a^{\rm dbl}
(H_{a,\le N}^{W,0}+V_a-z)^{-1}
{\mathbb P}_a^{\rm phys}
\right\|
\le
C_{E,N,K}\,a\|QV_aP\|_{\le N,E}.
```

In particular, the Wilson branch advances the detail-preserving all-mode
regulator toward single-species finite-energy QFT data: retained detail is
present in the regulator, but it is infinitely costly to excite and its
off-block influence vanishes under the displayed tested-sector scaling.

### Proof

Theorem 19.1 gives a one-particle detail gap at least `c/a` for small `a`.
Every finite-particle vector containing one detail excitation therefore has
`d\Gamma(|h_a^W|)` energy at least `G_a` before interactions. For fixed `E`
and fixed `N`, this lies outside `[0,E]` once `a` is small, proving the free
spectral-projection claim.

For the interacting estimate, use the block decomposition
`{\mathcal F}_{a,\le N}=P{\mathcal F}_{a,\le N}\oplus
Q{\mathcal F}_{a,\le N}`. Since `\|QV_aQ\|\le G_a/4`, the `Q` block remains
at distance at least `G_a/2` from the fixed physical resolvent set for small
`a`; hence

```math
\left\|
\left(Q(H_{a,\le N}^{W,0}+V_a-z)Q\right)^{-1}
\right\|
\le
C a.
```

The Feshbach formula gives

```math
Q(H_{a,\le N}^{W,0}+V_a-z)^{-1}P
=
-
\left(Q(H_{a,\le N}^{W,0}+V_a-z)Q\right)^{-1}
QV_aP\,S_P(z)^{-1}.
```

Taking norms yields the stated bound. `square`

### Theorem 20.3: Staggered Finite-Particle Multi-Taste Reconstruction

If no Wilson term is added, the detail-preserving regulator has a different
continuum target. Let `h_a^{\rm st}` be the folded staggered one-particle
symbol of Theorem 19.3. On folded low momenta, assume

```math
\|h_a^{\rm st}-(h_D\oplus h_D)\|
_{\Lambda(a)}
\le
\epsilon_a,
\qquad
\epsilon_a\to0.
```

Then for every fixed particle cutoff `N`, the finite-particle generators

```math
d\Gamma(h_a^{\rm st})
```

converge on the folded low-sector to

```math
d\Gamma(h_D\oplus h_D)
```

with error bounded by `N\epsilon_a` on the `N`-particle sector. The limiting
CAR algebra is therefore the CAR algebra over the two-taste one-particle
space,

```math
{\rm CAR}({\mathcal H}_D\oplus{\mathcal H}_D),
```

not the single-taste algebra `{\rm CAR}({\mathcal H}_D)`.

### Proof

Second quantization is functorial on finite exterior powers. If two
one-particle generators differ by at most `\epsilon_a` on the accepted folded
sector, then on `\wedge^n` their second quantizations differ by at most
`n\epsilon_a`. Taking `n\le N` gives `N\epsilon_a`. The CAR algebra follows
from the declared one-particle target. Because the detail/taste label is still
present, a single-taste claim would require an additional declared projection,
constraint, mass term, or taste-breaking mechanism. `square`

### Theorem 20.4: Branch Stability Under Declared Interactions

Let the detail-preserving all-mode regulator be fixed.

1. **Wilson branch.** If the Wilson gap is present and the tested interaction
   satisfies `a\|V_a\|_{\le N,E}\to0`, then finite-energy physical matrix
   elements are stable under integrating out the detail sector:
   ```math
   H_{\rm eff}^{\rm phys}(z)
   =
   H_{\rm phys}
   +V_{\rm phys}
   +O(a\|V_a\|_{\le N,E}^2).
   ```
   Thus detail modes do not re-enter finite-energy tests except through a
   vanishing Wilson-suppressed correction.
2. **Staggered branch.** If no Wilson gap is present, the interaction must be
   classified as either taste-preserving,
   ```math
   \|[V_a,\Pi_{\tau}]\|_{\le N,E}\to0,
   ```
   in which case the two-taste continuum theory remains block structured, or
   taste-mixing, in which case the continuum target is a multi-taste theory
   with taste-mixing interactions.

### Proof

The Wilson statement is the Feshbach effective Hamiltonian expansion with a
detail-block inverse of size `O(a)`. The correction term is quadratic in the
physical-detail coupling and proportional to the inverse gap. The staggered
statement has no gap to use. Therefore taste cannot be dismissed
dynamically; it is either asymptotically conserved by the interaction or it is
part of the continuum interaction data. `square`

### Theorem 20.5: All-Mode Continuum Branch Trichotomy

At fixed nonzero `\Delta/a`, an all-mode continuum reconstruction from the
Dirac-chain projective kernels has the following rigorous branch structure:

```text
naive dyadic marginal:
  fails as an all-mode single-species reconstruction.

detail-preserving + Wilson gap:
  viable single-species finite-energy branch, pending full Fock/vacuum and
  local-net reconstruction.

detail-preserving + staggered interpretation:
  viable multi-taste branch, pending full Fock/vacuum and local-net
  reconstruction for the declared taste space.

declared low-sector instrument:
  viable tested low-energy branch, with explicit reject records.
```

There is no fourth undeclared route in which the detail sector is simply
forgotten and the result is still claimed to be all-mode single-species QFT.

### Proof

The naive marginal is excluded by Proposition 16.2 and Theorem 20.1. The
detail-preserving branch has exact all-mode projective transfer by Theorems
18.1 and 18.2. The Wilson option is controlled by Theorems 19.1, 19.2, and
20.2. The staggered option is controlled by Theorems 19.3 and 20.3. The
low-sector option is controlled by Theorems 16.3, 16.4, 16.5, and Corollary
17.3, and it is not an all-mode claim because it carries a reject record.
These exhaust the declared alternatives available in this regulator analysis.
`square`

## 21. Fock, Local-CAR, And Operational Reconstruction Interface

The Wilson and staggered branches are now strong enough to state the QFT
interface cleanly. The claims in this section are conditional reconstruction
claims: they say exactly what must converge at the representation level for
the projective ISP kernels to feed finite-energy QFT data. They do not claim
that bare `Gamma` alone contains a Fock polarization, a vacuum, or local field
operators.

### Wilson Reconstruction Hypotheses

Let `\Lambda_a` be finite spatial volumes tending to the continuum volume, and
let

```math
I_a:C_c^\infty(\Sigma;{\mathbb C}^s)\to{\mathcal H}_a
```

be lattice smearing maps into the physical Wilson branch. Assume:

1. **CAR smearing convergence.**
   ```math
   \langle I_af,I_ag\rangle_{{\mathcal H}_a}
   \to
   \langle f,g\rangle_{{\mathcal H}_D}
   ```
   for all compactly supported smooth spinors `f,g`.
2. **Physical one-particle convergence.**
   ```math
   \|(h_a^W I_a-I_a h_D)f\|\to0
   ```
   for every test spinor `f`.
3. **Polarization convergence.** If
   `C_a^W=\chi_{(-\infty,0)}(h_a^W)` and
   `C_D=\chi_{(-\infty,0)}(h_D)`, then for every finite test family
   `{f_i}`,
   ```math
   \left|
   \langle I_af_i,C_a^W I_af_j\rangle
   -
   \langle f_i,C_D f_j\rangle
   \right|
   \le
   \epsilon_{\rm pol}(a;f_i,f_j),
   \qquad
   \epsilon_{\rm pol}\to0.
   ```
4. **Wilson detail gap.** The detail branch satisfies Theorem 20.2.
5. **Declared interaction convergence, if interactions are included.** The
   Wilson Feshbach effective physical interaction
   `H_{\rm eff}^{\rm phys}(z)` converges on tested local finite-energy
   matrix elements to a declared continuum interaction.

The first three hypotheses are representation data. They are not consequences
of the stochastic `Gamma` alone.

### Theorem 21.1: Wilson Vacuum And Finite-Local Fock Convergence

Under the Wilson reconstruction hypotheses, let `\omega_a^W` be the lattice
quasi-free vacuum state with covariance `C_a^W`, and let `\omega_D` be the
continuum Dirac quasi-free vacuum with covariance `C_D`. For every finite CAR
polynomial

```math
A(f_1,\ldots,f_m)
```

built from compactly supported test spinors, define its lattice approximation
by replacing each continuum field with the lattice field smeared by `I_af_i`.
Then

```math
\omega_a^W(A_a(I_af_1,\ldots,I_af_m))
\to
\omega_D(A(f_1,\ldots,f_m)).
```

More quantitatively, for each fixed polynomial `A`,

```math
\left|
\omega_a^W(A_a)-\omega_D(A)
\right|
\le
C_A\left(
\epsilon_{\rm CAR}(a)+\epsilon_{\rm pol}(a)+\epsilon_{\rm smear}(a)
\right),
```

where the three errors are respectively the finite test-family errors in the
CAR pairing, polarization matrix, and smearing approximation. Detail/doubler
fields do not contribute to fixed finite-energy Wilson tests, by Theorem
20.2.

### Proof

A quasi-free CAR state is determined on every finite polynomial by its
two-point covariance and the CAR pairing. Wick expansion writes every
`m`-point expectation as a finite sum of determinants or Pfaffians whose
entries are two-point matrix elements. The assumed convergence of the CAR
pairing and the polarization matrix therefore implies convergence of every
fixed polynomial expectation, with a polynomial-dependent Lipschitz constant
`C_A`. Wilson detail excitations are separated from fixed finite-energy tests
by Theorem 20.2, so no additional branch contributes. `square`

### Theorem 21.2: Wilson Local-CAR Net Convergence On A Cauchy Surface

For every bounded spatial region `O\subset\Sigma`, let `{\mathfrak A}_a^W(O)`
be the lattice CAR algebra generated by fields smeared with `I_af` for
`{\rm supp}(f)\subset O`, and let `{\mathfrak A}_D(O)` be the continuum Dirac
CAR algebra on the same Cauchy surface. Under the Wilson reconstruction
hypotheses:

1. isotony is exact at finite cutoff after choosing nested lattice
   approximants;
2. the local CAR relations converge on test fields:
   ```math
   \left\|
   \{\psi_a(I_af),\psi_a^\dagger(I_ag)\}
   -
   \langle f,g\rangle
   \right\|
   \to0;
   ```
3. vacuum matrix elements of local polynomials converge as in Theorem 21.1.

If, in addition, the lattice Wilson propagators converge to the continuum
Dirac propagator on compact spacetime test functions, then the time-evolved
local CAR net converges on those tests. In particular, spacelike
anti-commutators vanish in the continuum limit because the limiting Dirac
anti-commutator vanishes.

### Proof

The equal-time statements are direct consequences of the smearing-map
convergence and the functorial definition of the CAR algebra. The vacuum
matrix-element statement is Theorem 21.1. The spacetime statement follows by
replacing `I_af` with the propagated lattice test field and using the assumed
strong convergence of propagators. The vanishing of spacelike
anti-commutators is inherited from the continuum Dirac causal propagator.
`square`

### Theorem 21.3: Staggered Multi-Taste Fock And Local-CAR Reconstruction

On the staggered branch, replace the Wilson physical one-particle space by

```math
{\mathcal H}_{\rm st}
=
{\mathcal H}_D\oplus{\mathcal H}_D
```

and replace the smearing map by

```math
I_a^{\rm st}:
C_c^\infty(\Sigma;{\mathbb C}^s\otimes{\mathbb C}^2)
\to
{\mathcal H}_a^{\rm st}.
```

Assume CAR smearing convergence, one-particle convergence, and polarization
convergence to the two-taste Dirac target. Then the staggered lattice
quasi-free vacuum and local CAR algebras converge, on every finite local
polynomial, to

```math
{\rm CAR}({\mathcal H}_D\oplus{\mathcal H}_D).
```

If interactions are included, there are exactly two declared continuum
possibilities at this level:

```text
taste-preserving interactions:
  the limiting local net remains block/taste structured;

taste-mixing interactions:
  the limiting local net is a multi-taste net with taste-mixing couplings.
```

It is not a single-species net unless an additional Wilson term, taste
projection, constraint, or taste-removal mechanism is declared and proved.

### Proof

The proof is the same as Theorems 21.1 and 21.2 after replacing the
one-particle target by the two-taste target. The additional taste label is part
of the one-particle test-function space, so the resulting CAR functor produces
the two-taste algebra. With no Wilson gap, no estimate removes this label.
Taste-preserving interactions commute asymptotically with the taste
projectors; taste-mixing interactions do not, and therefore belong to the
declared continuum interaction data. `square`

### Theorem 21.4: Projective ISP Kernels Feed Declared QFT Instruments

Let `A` be a local CAR polynomial in either the Wilson single-species branch or
the staggered multi-taste branch. A measurement of `A` in ISP is not obtained
from the raw algebraic maps `J_R` or `E_{R,S}` alone. It requires a declared
instrument/effect functional

```math
\ell_{A,a}:{\mathbb R}^{X_a}\to{\mathbb R}
```

whose continuum limit is the QFT expectation functional for `A`. Assume
uniform boundedness and projective compatibility,

```math
\|\ell_{A,a}\|\le L_A,
\qquad
\|\ell_{A,b}-\ell_{A,a}P_{ab}\|\le\delta_A^{ab}.
```

If the comparison maps satisfy

```math
\|P_{ab}J_R^b-J_R^aP_{ab}\|\le\chi_R^{ab},
```

then the declared measurable comparison obeys

```math
\left|
\ell_{A,b}J_R^b
-
\ell_{A,a}J_R^aP_{ab}
\right|
\le
\delta_A^{ab}\|J_R^b\|
L_{\rm state}
+
L_A\chi_R^{ab}L_{\rm state},
```

on the tested state set of size `L_{\rm state}`. The same statement holds for
`J_R^{-1}` and `E_{R,S}` with their corresponding transfer errors.

Thus Paper 3 exports controlled algebraic relative-dynamics maps to QFT only
after a branch and an operational instrument have been declared.

### Proof

Add and subtract `\ell_{A,a}P_{ab}J_R^b` and use the two displayed bounds:

```math
\ell_{A,b}J_R^b-\ell_{A,a}J_R^aP_{ab}
=
(\ell_{A,b}-\ell_{A,a}P_{ab})J_R^b
+
\ell_{A,a}(P_{ab}J_R^b-J_R^aP_{ab}).
```

Taking norms on the tested state set gives the estimate. The inverse and
exchange-defect versions use the same one-line argument with the transfer
bounds from Theorems 8.1, 9.1, and 17.1. `square`

### Theorem 21.5: Branch Reconstruction Contract

After Sections 20 and 21, the strongest rigorous reconstruction contract is:

```text
common detail-preserving trunk:
  all-mode projective compatibility is exact when UV/detail data are retained.

Wilson branch:
  finite-energy single-species QFT data are obtained if the Wilson
  polarization, smearing maps, propagators, and tested interactions converge.

staggered branch:
  multi-taste QFT data are obtained if the staggered polarization, smearing
  maps, propagators, and tested interactions converge.

ISP operational bridge:
  raw J_R, J_R^{-1}, and E_{R,S} become measurable predictions only after
  declaring compatible instruments/effects.
```

The remaining full-QFT burden is therefore not the old all-mode regulator
problem. It is the representation-theoretic burden: prove the relevant
polarization, vacuum, local-net, interaction, and Lorentz-covariance
convergences for the chosen branch.

### Proof

The common trunk is Theorems 18.1, 18.2, and 20.1. The Wilson branch is
Theorems 19.1, 19.2, 20.2, 20.4, 21.1, and 21.2. The staggered branch is
Theorems 19.3, 20.3, 20.4, and 21.3. The operational bridge is Theorem 21.4.
The final sentence lists precisely the assumptions not derived from bare
`Gamma`. `square`

## 22. Concrete Wilson/Staggered Representation Package

Section 21 stated the QFT interface conditionally. This section supplies the
standard free Wilson and staggered representation package for the one-spatial
dimensional Dirac-chain benchmark. It is still representation data, not data
contained in bare `Gamma`, but it is now a concrete package rather than an
unnamed hypothesis.

Throughout this section take the continuum one-particle space to be

```math
{\mathcal H}_D=L^2({\mathbb R};{\mathbb C}^s),
\qquad
h_D(k)=\alpha k+m\beta,
```

with `m>0`, `\alpha^2=\beta^2=1`, and `\alpha\beta+\beta\alpha=0`. Let

```math
{\mathcal H}_a=\ell^2(a{\mathbb Z};{\mathbb C}^s),
\qquad
\langle u,v\rangle_a=a\sum_{n\in{\mathbb Z}}u_n^\dagger v_n,
```

with Brillouin zone `B_a=(-\pi/a,\pi/a]`. Choose a smooth cutoff
`\chi\in C_c^\infty((-1,1))` with `\chi=1` on `[-1/2,1/2]`, and choose
`\Lambda(a)` such that

```math
\Lambda(a)\to\infty,
\qquad
a\Lambda(a)\to0.
```

Let `\chi_a(k)=\chi(k/\Lambda(a))`. For a Schwartz test spinor `f`, define
the Wilson smearing map by Fourier sampling on the physical branch:

```math
\widehat{I_a^W f}(k)=\chi_a(k)\widehat f(k),
\qquad
k\in B_a.
```

Equivalently, `I_a^W` is band-limited sampling into the physical branch. The
band cutoff is not a hidden measurement; it is the declared test-function
embedding used to compare lattice and continuum fields.

### Theorem 22.1: Concrete Wilson Smearing And One-Particle Convergence

Let

```math
h_a^W(k)
=
\alpha\frac{\sin(ak)}{a}
+
\beta\left(m+\frac r a(1-\cos(ak))\right),
\qquad
r>0.
```

For every Schwartz spinor `f`,

```math
\|I_a^W f\|_a\to\|f\|_{L^2},
```

and

```math
\|(h_a^W I_a^W-I_a^W h_D)f\|_a
\le
C_f\left(a\Lambda(a)^2+a^2\Lambda(a)^3\right)
+
\varepsilon_f(\Lambda(a)),
```

where `\varepsilon_f(\Lambda)\to0` faster than any power of `\Lambda^{-1}`.

### Proof

The norm convergence is the Plancherel/Riemann-sum convergence for
band-limited samples, plus the Schwartz tail discarded by `\chi_a`. On the
support of `\chi_a`,

```math
\frac{\sin(ak)}a-k=O(a^2|k|^3),
\qquad
\frac1a(1-\cos(ak))=O(a|k|^2).
```

Thus

```math
\|h_a^W(k)-h_D(k)\|
\le
C(a|k|^2+a^2|k|^3)
```

for `|k|\le\Lambda(a)`. Multiplying by `\widehat f(k)` and integrating over
the cutoff region gives the displayed bound. The complement contributes the
Schwartz tail `\varepsilon_f(\Lambda(a))`. `square`

### Theorem 22.2: Wilson Polarization Convergence

Let

```math
C_D(k)=\chi_{(-\infty,0)}(h_D(k))
```

and

```math
C_a^W(k)=\chi_{(-\infty,0)}(h_a^W(k)).
```

Then for every pair of Schwartz test spinors `f,g`,

```math
\left|
\langle I_a^W f,C_a^W I_a^W g\rangle_a
-
\langle f,C_D g\rangle
\right|
\le
C_{f,g,m}\left(a\Lambda(a)^2+a^2\Lambda(a)^3\right)
+
\varepsilon_{f,g}(\Lambda(a)),
```

and the right side tends to zero. Hence the Wilson quasi-free vacuum
covariance converges on all finite test families.

### Proof

Because `m>0`, both continuum and physical Wilson symbols have a uniform
spectral gap around zero on the tested branch. The negative-energy projector
is the smooth matrix function

```math
P_-(H)=\frac12\left(1-\frac{H}{(H^2)^{1/2}}\right)
```

on this gapped set. Functional calculus for finite matrices gives a Lipschitz
bound

```math
\|C_a^W(k)-C_D(k)\|
\le
C_m\|h_a^W(k)-h_D(k)\|
```

for `|k|\le\Lambda(a)`. Theorem 22.1 supplies the symbol difference bound.
Integrating against `\widehat f` and `\widehat g`, and adding the discarded
Schwartz tails, gives the estimate. `square`

### Theorem 22.3: Wilson Propagator Convergence And Free Microcausality Limit

For every Schwartz spinor `f` and every fixed `T<\infty`,

```math
\sup_{|t|\le T}
\left\|
e^{-it h_a^W}I_a^W f-I_a^W e^{-it h_D}f
\right\|_a
\le
C_{T,f}\left(a\Lambda(a)^2+a^2\Lambda(a)^3\right)
+
\varepsilon_{T,f}(\Lambda(a)).
```

Consequently, for compactly supported spacetime test functions `F,G`, the
lattice Wilson CAR anti-commutator distribution converges to the continuum
Dirac anti-commutator distribution. If `{\rm supp}(F)` and `{\rm supp}(G)`
are spacelike separated, the limiting anti-commutator is zero.

### Proof

On the cutoff branch, Duhamel's formula gives

```math
e^{-it h_a^W}-e^{-it h_D}
=
-i\int_0^t
e^{-i(t-s)h_a^W}
(h_a^W-h_D)
e^{-is h_D}\,ds.
```

The integrand norm is bounded by the symbol estimate from Theorem 22.1. This
gives the uniform-in-`|t|\le T` estimate after adding the high-momentum
Schwartz tail. The spacetime CAR anti-commutator is the distribution kernel of
the propagated one-particle pairing; convergence on compact spacetime tests
therefore follows from the propagator estimate. The continuum Dirac
anti-commutator vanishes at spacelike separation, so the lattice
anti-commutator tends to zero on such tests. `square`

### Wilson-Admissible Interactions

A finite-cutoff interaction family `V_a` is called Wilson-admissible on a
tested finite-particle/finite-energy/local class if:

1. `V_a=V_a^\dagger` on the finite-volume finite-particle cutoff;
2. it has uniformly finite spatial range in lattice units after smearing over
   the declared local test region, or else an exponentially decaying kernel
   with uniform summable tail;
3. the detail-block bound and off-block mixing bound hold:
   ```math
   \|QV_aQ\|_{\le N,E,O}\le G_a/4,
   \qquad
   a\|QV_aP\|_{\le N,E,O}\to0;
   ```
4. the physical Feshbach effective interaction
   ```math
   V_{a,\rm eff}^{\rm phys}(z)
   =
   PV_aP
   -
   PV_aQ
   \left(Q(H_{a,\le N}^{W,0}+V_a-z)Q\right)^{-1}
   QV_aP
   ```
   converges on the declared local matrix elements to a continuum interaction
   `V_{\rm cont}`.

### Theorem 22.4: Wilson Interaction Stability For The Declared Class

For Wilson-admissible interactions,

```math
\|V_{a,\rm eff}^{\rm phys}(z)-PV_aP\|_{\le N,E,O}
\le
C a\|PV_aQ\|_{\le N,E,O}\|QV_aP\|_{\le N,E,O}.
```

In particular, if the physical block `PV_aP` converges to `V_{\rm cont}` on
the tested local matrix elements and the off-block mixing is uniformly
bounded, then the Wilson detail sector does not change the continuum
interaction. If the off-block mixing grows, the precise condition needed is
the displayed `a\|PV_aQ\|\|QV_aP\|\to0`.

### Proof

The Wilson gap and the `QV_aQ` bound imply

```math
\left\|
\left(Q(H_{a,\le N}^{W,0}+V_a-z)Q\right)^{-1}
\right\|
\le
Ca
```

on the tested physical resolvent set. Insert this into the Feshbach correction
term. The result is the displayed estimate. `square`

### Theorem 22.5: Concrete Staggered Two-Taste Representation Package

Define the two-branch staggered smearing map for
`F=(f_0,f_1)\in{\mathcal S}({\mathbb R};{\mathbb C}^s\otimes{\mathbb C}^2)`
by

```math
\widehat{I_a^{\rm st}F}(k)
=
\chi_a(k)\widehat f_0(k)
+
\chi_a(k-\pi/a)\widehat f_1(k-\pi/a),
\qquad
k\in B_a,
```

with the second term understood by folding a neighborhood of `\pi/a` back to
physical momentum. Then

```math
\|I_a^{\rm st}F\|_a^2
\to
\|f_0\|^2+\|f_1\|^2.
```

For the central-difference staggered symbol without Wilson term, the folded
one-particle generator converges on test functions to

```math
h_{\rm st}(k)
=
(\alpha k+m\beta)\oplus(-\alpha k+m\beta),
```

with the same error scale

```math
C_F a^2\Lambda(a)^3+\varepsilon_F(\Lambda(a)).
```

Consequently, the staggered polarization and propagator converge on finite
test families to those of the two-taste target. If a fixed taste-spin unitary
identifies the second block with the chosen Dirac representation, the target
may be written as `h_D\oplus h_D`; otherwise the honest target is the displayed
opposite-kinetic-sign two-taste Dirac theory.

### Proof

The two cutoff branches are disjoint because `a\Lambda(a)\to0`, so the norm
splits into the sum of the two branch norms. On the physical branch,
`sin(ak)/a=k+O(a^2|k|^3)`. On the folded branch `k=\pi/a+q`,

```math
\frac{\sin(ak)}a
=
\frac{\sin(\pi+aq)}a
=
-q+O(a^2|q|^3).
```

This gives the displayed block generator. The polarization proof repeats
Theorem 22.2 on the two gapped blocks, and the propagator proof repeats
Theorem 22.3 blockwise. `square`

### Theorem 22.6: V3 Paper 4 Import Contract

V3 Paper 4 may import the following facts from Paper 3:

```text
Projective kernel control:
  J_R, J_R^{-1}, and E_{R,S} are controlled under the declared projective
  readouts of this paper.

All-mode regulator:
  naive dyadic all-mode marginalization fails at fixed Delta/a;
  detail-preserving all-mode refinement works.

Wilson branch:
  the Wilson detail sector has an O(1/a) gap;
  Wilson smearing, polarization, and propagator convergence are proved on
  smooth finite test families;
  Wilson-admissible interactions decouple from detail modes under the stated
  Feshbach bounds;
  the branch targets single-species finite-energy Dirac/CAR data.

Staggered branch:
  without Wilson, the retained detail sector is a two-taste target;
  staggered smearing, polarization, and propagator convergence are proved on
  smooth finite test families;
  single-species claims require an additional declared taste-removal
  mechanism.

Operational bridge:
  raw algebraic maps become measurable predictions only after compatible
  instruments/effects are declared.
```

Paper 4 may not import, without additional proof, any of the following:

```text
full interacting renormalized QFT;
Lorentz/Poincare covariance of the full interacting net;
non-Abelian gauge stability;
operational observability of raw J_R or E_{R,S};
derivation of Fock polarization or local fields from bare Gamma alone.
```

### Proof

Each positive import is exactly one of Theorems 7.1, 8.1, 9.1, 17.1, 18.1,
18.2, 19.1, 19.3, 20.2, 20.3, 21.4, 22.1, 22.2, 22.3, 22.4, or 22.5. Each
negative import is listed in the status boundary because it is not a theorem
of this paper. `square`

## 23. Updated Status And Export Discipline

What is now proved in this draft:

1. The abstract transfer theorem:
   ```text
   LC-log + reference-renormalized residuals
   -> projective compatibility of J, J^{-1}, and E.
   ```
2. A concrete bounded interacting projective benchmark, Benchmark A, where the
   primitive residuals and reference-renormalized residuals vanish exactly.
3. Uniform LC-log applicability for Benchmark A by V2 Proposition 10.
4. Exact projective compatibility of `J_R`, `J_R^{-1}`, and `E_{R,S}` in
   Benchmark A.
5. A marked-KP criterion reducing genuine spatial Dirac-chain refinement to
   activity-level mismatch bounds, without global inverse estimates.
6. A named dyadic block readout proving Hypothesis SR in the thin-slab regime
   for hopping scale `1/a`.
7. A declared low-momentum accepted-branch readout proving fixed-ratio SR for
   `\Delta(a)/a\to\lambda`, provided the collar is smooth, the low-sector
   cutoff satisfies `a^2\Lambda(a)^3\to0`, and `a|g_a|\to0`.
8. Explicit transfer through Theorems 7.1, 8.1, and 9.1: the dyadic thin-slab
   and low-momentum fixed-ratio residuals propagate to `J_R`, `J_R^{-1}`, and
   `E_{R,S}` with the same vanishing error scale.
9. A detail-preserving staggered all-mode block readout closing the fixed-ratio
   regulator gap at the projective-kernel level: all-mode SR and transfer are
   exact when the UV/detail label is retained.
10. Wilson/staggered continuum interpretation of that retained detail sector:
    Wilson terms make the detail/doubler branch infinitely massive and
    decouple it from finite-energy tests; without Wilson terms the detail label
    is a declared staggered taste/species.
11. A common-trunk theorem showing why undeclared all-mode marginalization
    fails whenever identified fine states have different outgoing coarse
    fluxes.
12. A finite-particle Wilson decoupling theorem: for fixed particle number and
    fixed energy window, detail excitations leave the tested sector, and
    interaction-induced mixing is `O(a\|V_a\|)`.
13. A finite-particle staggered reconstruction theorem: without Wilson, the
    retained detail label gives a multi-taste CAR target, not a hidden
    single-species target.
14. A branch trichotomy separating the failed naive marginal route, the Wilson
    single-species finite-energy route, the staggered multi-taste route, and
    the declared low-sector route.
15. A conditional Wilson Fock/vacuum interface: if smearing maps,
    polarizations, propagators, and tested interactions converge, finite local
    CAR polynomial expectations converge to the single-species Dirac target.
16. A conditional Wilson local-CAR net interface on a Cauchy surface, with
    spacetime locality inherited when the lattice propagators converge to the
    Dirac causal propagator on test functions.
17. A parallel staggered local-CAR interface: under the analogous representation
    hypotheses, the target is the multi-taste CAR net
    `CAR({\mathcal H}_D\oplus{\mathcal H}_D)`.
18. An operational bridge theorem: controlled algebraic maps `J_R`,
    `J_R^{-1}`, and `E_{R,S}` become measurable QFT predictions only after
    compatible instrument/effect functionals are declared.
19. A concrete Wilson representation package for the one-dimensional
    Dirac-chain benchmark: band-limited lattice smearing maps, physical
    one-particle convergence, and an explicit error scale
    `a\Lambda(a)^2+a^2\Lambda(a)^3+\varepsilon(\Lambda(a))`.
20. Wilson polarization convergence for the massive free Dirac branch, proving
    convergence of the quasi-free covariance on finite smooth test families.
21. Wilson propagator convergence on finite spacetime test windows, with the
    free microcausality limit inherited from the continuum Dirac
    anti-commutator.
22. A Wilson-admissible interaction class and Feshbach correction bound showing
    when the detail sector does not alter the tested continuum interaction.
23. A concrete staggered two-taste representation package with smearing,
    polarization, and propagator convergence to the declared two-taste target.
24. A V3 Paper 4 import contract separating what later papers may use from
    what still requires additional proof.

What is still not proved:

1. a fixed-ratio theorem for sharp deleted-bond collars without smoothing;
2. nonperturbative interacting continuum decoupling beyond tested
   finite-energy sectors satisfying `a\|V_a\|_{\rm tested}\to0`;
3. derivation of the Wilson/staggered representation package directly from
   bare `Gamma`, rather than declaring it as enriched representation data;
4. nonperturbative interacting vacuum convergence and renormalized local-net
   convergence beyond the stated free/tested-polynomial/Feshbach hypotheses;
5. full Lorentz/Poincare covariance of the reconstructed spacetime net;
6. gauge-sector or non-Abelian cutoff stability;
7. interacting stochastic curvature;
8. operational observability of raw `J_R` or `E_{R,S}` without declared
   instruments, which should not be expected.

The status boundary is now sharp:

1. **Naive all-mode dyadic marginal fails at fixed `\Delta/a`.** Proposition
   16.2 shows that the ordinary dyadic marginal leaves a nonvanishing local
   block mismatch of order `(\Delta/a)^2` when `\Delta/a` has a nonzero limit.
   Therefore it is not a valid all-mode fixed-ratio projective readout for the
   Dirac chain.
2. **Detail-preserving all-mode refinement works.** Theorems 18.1 and 18.2
   show that retaining the intra-block detail/parity label gives exact all-mode
   SR and exact transfer at fixed ratio. The all-mode data are not erased; they
   are carried as explicit UV/detail records.
3. **Wilson/staggered continuum meaning is controlled.** Theorem 19.1 and
   Corollary 19.2 show that a Wilson term makes the retained detail sector
   infinitely massive and harmless for finite-energy tests. Theorem 19.3 shows
   that without a Wilson term the detail sector is a declared staggered
   taste/species, so the continuum target is multi-taste unless further
   structure removes it.
4. **Both detail-preserving branches advance.** Theorems 20.2, 20.3, and
   20.4 lift the split to finite-particle reconstruction data: Wilson gives a
   finite-energy single-species branch, while staggered gives a declared
   multi-taste branch.
5. **The free Wilson representation package is now concrete.** Theorems 22.1,
   22.2, and 22.3 prove smearing, polarization, and propagator convergence for
   the massive Wilson branch on smooth finite test families. The interaction
   part remains controlled only for the Wilson-admissible Feshbach class of
   Theorem 22.4.
6. **The staggered representation package is concrete.** Theorem 22.5 proves
   the parallel smearing, polarization, and propagator convergence to the
   two-taste target. Without an additional declared taste-removal mechanism,
   this is not single-species QFT.
7. **Conditional QFT interfaces are now explicit.** Theorems 21.1 and 21.2
   give the Wilson single-species Fock/local-CAR interface once the concrete
   representation package is chosen and interactions satisfy the declared
   convergence assumptions. Theorem 21.3 gives the staggered multi-taste
   analogue.
8. **Declared operational instruments are required.** Theorem 21.4 shows how
   projective bounds for `J_R`, `J_R^{-1}`, and `E_{R,S}` transfer to
   measurable QFT predictions once compatible effect functionals are declared.
   Raw algebraic maps are still not observables by themselves.
9. **Declared low-sector fixed-ratio refinement works.** Theorems 16.3, 16.4,
   16.5, and Corollary 17.3 prove fixed-ratio refinement on the accepted
   low-momentum smooth branch, with explicit reject records and error scale
   `a^2\Lambda(a)^3+\tau_N(a)+a|g_a|+|\Delta(a)/a-\lambda|`.
10. **Full QFT still requires enriched representation data.** This paper proves
   Gamma-level/projective control of algebraic relative-dynamics maps under
   declared readouts and gives concrete free Wilson/staggered QFT interfaces.
   It does not derive those representation choices, Lorentz covariance,
   stress-energy, or full interacting continuum QFT from bare `Gamma`.

Paper 4 and later papers may use the following from this paper:

```text
raw J_R and E_{R,S} are algebraic relative-dynamics maps;
they are projectively controlled in Benchmark A;
they are projectively controlled for dyadic spatial blocks in the thin-slab
regime `\Delta(a)/a\to0`;
at fixed nonzero `\Delta/a`, they need a declared low-momentum or
doubler-controlled readout;
the detail-preserving staggered block readout gives all-mode fixed-ratio
control by retaining the UV/detail label;
with a Wilson term the retained detail sector is massive and decouples from
finite-energy tests;
on fixed finite-particle sectors the Wilson branch suppresses physical/detail
mixing by the Wilson gap;
with declared Wilson smearing maps, polarization, propagator convergence, and
tested interaction convergence, finite local CAR polynomial expectations
converge to the single-species Dirac target;
the Wilson smearing, polarization, and propagator convergence are proved here
for the massive free branch on smooth finite test families;
Wilson-admissible interactions are controlled by a Feshbach correction bound;
without a Wilson term the retained detail sector is staggered taste/species
content, not something erased by Gamma;
on fixed finite-particle sectors the staggered branch reconstructs the
multi-taste CAR target, not single-species CAR;
the staggered smearing, polarization, and propagator convergence are proved
here for the two-taste free branch on smooth finite test families;
measurable QFT predictions require compatible instrument/effect functionals
ell_A; raw algebraic maps are not observables by themselves;
Theorem 22.6 gives the formal V3 Paper 4 import contract;
the low-momentum accepted branch gives fixed-ratio control for smooth collars;
full QFT claims still require enriched representation data beyond bare Gamma;
they are not automatically observables, effects, or measurement records.
```

This keeps the paper aligned with Barandes' ontology. The primitive data are
whole-process stochastic kernels and declared projective readouts. Hilbert
Hamiltonians are used only to define whole-process kernels in a chosen
representation. No theorem above composes undeclared partial kernels as if an
indivisible process were Markovian.
