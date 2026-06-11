# Metric Data Gate And Gamma-Level Obstruction

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

V2 Paper 10 obstruction draft

Date: 2026-05-16

Updated: 2026-05-17

Status: Final V2 Gamma-level obstruction pass. The Paper 9 import discipline is locked,
Theorem 10.1 proves the abstract metric-coefficient extraction lemma,
Proposition 10.3 reduces the first `2+1D` benchmark to a finite active
commutator-stencil, Proposition 10.4 shows that the leading site/cell
Born-squared Dirac coefficient fails the rotated-metric cross-term test,
Proposition 10.5 shows that the first higher-order frame-interference signal is
quadratic/signless, and Proposition 10.6 gives an all-order sign-ambiguity
no-go for full `Gamma`-level metric reconstruction under the present
Born-squared rule. This paper follows the Paper 9 Route-B completion gate. It
asks whether the stochastic exchange-curvature data developed in Papers 1-9 can
identify fixed-background spatial metric data. It does not attempt dynamical
gravity.

The scope decision is strict:

> Paper 10 is a metric-data gate, not a gravity paper. Its job is to determine
> whether the coefficient of stochastic hypersurface-deformation curvature can
> be read as inverse spatial metric data in more than one spatial dimension.

If the answer is yes, relativistic ISP has earned the next question: curved
backgrounds and, later, dynamical geometry. If the answer is no, the program may
still be a strong probability-first account of finite and operational quantum
dynamics, but it has not found spacetime geometry inside `Gamma`-level data.

## 1. Why Paper 10 Exists

Paper 1 proved the first safe free stochastic-curvature theorem in `1+1D`:

```math
\mathfrak C_a[N,M]\iota_a\phi
\longrightarrow
K_\parallel[N\partial_xM-M\partial_xN]\phi .
```

This is real evidence that exchange defects can reproduce the tangential part
of the hypersurface-deformation bracket. But in one spatial dimension the
metric question is almost invisible: the coefficient is one scalar, and many
normalizations can hide inside the lapse, the lattice spacing, or the tangential
generator convention.

The geometric hinge appears in more than one spatial dimension:

```math
[H[N],H[M]]
=
D[\beta],
\qquad
\beta^i=h^{ij}(N\partial_jM-M\partial_jN).
```

The coefficient `h^{ij}` is fixed background geometry in ordinary QFT on a
fixed spacetime. In general relativity it becomes a dynamical structure
function. Paper 10 is only about the first statement:

> Can stochastic exchange curvature recover fixed-background `h^{ij}` or its
> density-weighted version from finite-kernel data?

## 2. Ontological Discipline

The layers must remain separate.

1. **Raw exchange curvature.** `E_{R,S}` and its normalized coefficients are
   algebraic relative-dynamics data. They are not automatically detector
   observables.
2. **Tangential representation.** A map `K_i[v^i]` represents a tangential
   deformation on the tested continuum state/effect domain. Its faithfulness is
   an extra hypothesis to prove or declare.
3. **Metric coefficient.** A coefficient `C^{ij}(x)` extracted from
   `K_i[C^{ij}(N\partial_jM-M\partial_jN)]` is metric data only after symmetry,
   positivity, locality, and coordinate behavior are established.
4. **Dynamical geometry.** A metric coefficient is not gravity unless it can vary
   as a physical configuration variable and obey a dynamical closure law.

Barandes alignment also remains in force. Products of comparison maps are
algebraic curvature tests around declared finite deformation loops. They are not
Markov divisibility through unrecorded intermediate stochastic stages.

## 3. Export Ledger From Papers 1-9

Paper 10 may use the following.

| Source | Exported To Paper 10 | Not Exported |
| --- | --- | --- |
| Paper 1 | `1+1D` free stochastic-curvature theorem, smooth lapse sampling, tangential target operator. | Multi-dimensional metric coefficient, Fock QFT, curved background, gravity. |
| Paper 2 | Projective hypersurface-kernel language, regulator naturality, path compatibility without Markov divisibility. | Lorentz covariance theorem or metric reconstruction. |
| Paper 3 | Interacting comparison-map locality and exchange-corridor control under explicit inverse hypotheses. | General interacting QFT or metric data. |
| Paper 4 | Operational projection discipline: raw exchange maps are not automatically observables. | Raw-to-metric observability without an instrument. |
| Paper 5 | Gauge center discipline and fixed-cutoff gauge benchmark. | Non-Abelian geometry or continuum compact gauge QFT. |
| Paper 6 | No-go for Markovized shadows, finite operational reconstruction, QFT-promotion gates. | Continuum QFT reconstruction or spacetime metric. |
| Paper 7 | Free-QFT promotion investigation: sampling, covariance, spectrum, vacuum/Fock sector, local algebra, and continuum stability gates. | Metric data or dynamical spacetime. |
| Paper 8 | Standard free-QFT matching audit for the promoted massive `1+1D` Dirac/CAR candidate. | Multi-dimensional metric coefficient, stress-energy, or dynamical spacetime. |
| Paper 9 | Route-B sampled Lorentz-covariant free-QFT completion: finite boost approximants, spacetime local net, microcausality audit, and tested tangential-action compatibility. | Stress-energy, metric coefficient, interacting QFT, exact finite-lattice Lorentz covariance, all-mode Fock convergence, Gamma-only QFT, or dynamical geometry. |

Therefore Paper 10 must not assume:

1. a continuum metric is already known from `Gamma`;
2. local Lorentz covariance beyond what Paper 9 explicitly proves or imports as
   standard free-QFT continuum completion;
3. a faithful tangential generator;
4. symmetry or positivity of the extracted coefficient;
5. a stress-energy tensor;
6. dynamical geometry.

Each of these must be proved, made a hypothesis, or left outside scope.

### Paper 9 import discipline

Paper 10 may use Paper 9 in one narrow way:

```text
tested stochastic exchange curvature
-> tangential action on the enriched free local-QFT benchmark.
```

This makes the metric question meaningful because the tangential action now
lives inside a Lorentz-covariant free-QFT comparison class rather than only an
equal-time one-particle calculation.

Paper 10 may not use Paper 9 as if it had already supplied `h^{ij}`,
stress-energy, dynamical geometry, or a Hilbert-free reconstruction of QFT from
`Gamma`. In particular, the Paper 9 boost theorem is a sampled-sector theorem
for enriched one-particle/CAR data. It does not prove that raw endpoint kernels
alone determine boosts or metric coefficients.

Therefore every metric claim in Paper 10 must be labelled as one of two types.

1. **Gamma-level metric claim.** The coefficient `C^{ij}` is determined by the
   finite stochastic kernels, projective maps, comparison maps, and normalized
   exchange defects alone, up to declared gauge/normalization conventions.
2. **Enriched-representation metric claim.** The coefficient is visible only
   after adding a lift, field algebra, polarization, or other QFT-matching data.
   This can still be useful, but it is not geometry reconstructed from stochastic
   kernels alone.

The stronger Paper 10 goal is Gamma-level metric extraction. The fallback goal
is an honest enriched-representation obstruction/diagnostic theorem.

## 4. Core Definition: Metric-Candidate Curvature Coefficient

Let `Sigma` be a fixed spatial manifold of dimension `d>=2`. Let
`\{C_{a}\}` be a directed family of regulated hypersurface configuration spaces,
with exact finite stochastic kernels and localized comparison maps. For smooth
compactly supported lapse profiles `N,M`, suppose the normalized stochastic
exchange curvature has a continuum limit on a test domain `\mathcal D`:

```math
\mathfrak C_a[N,M]\iota_a\phi
\longrightarrow
\mathfrak C[N,M]\phi .
```

A **metric-candidate coefficient** is a local contravariant field
`C^{ij}(x)` such that

```math
\mathfrak C[N,M]
=
K_i\!\left[C^{ij}(N\partial_jM-M\partial_jN)\right]
```

for all compactly supported `N,M` in the tested class, where `K_i[v^i]` is the
continuum tangential deformation representation.

The coefficient is unique only if `K_i` is faithful on the tested vector-field
quotient:

```math
K_i[v^i]=0
\quad\Longrightarrow\quad
v^i\sim 0
```

for the declared tangential gauge equivalence.

### Local extraction principle

At a point `x`, the covector

```math
\omega_j(x):=N(x)\partial_jM(x)-M(x)\partial_jN(x)
```

can realize an arbitrary covector by choosing local jets, for example
`N(x)=1`, `M(x)=0`, `\partial_jN(x)=0`, and `\partial_jM(x)=\omega_j(x)`.
Thus, if the curvature limit is local and first-order in the lapse derivatives,
the map

```math
\omega_j\mapsto \beta^i=C^{ij}\omega_j
```

is pointwise extractable from exchange-curvature data.

This is the first-principles reason Paper 10 must go to `d>=2`: only then can we
test tensor structure, cross terms, symmetry, and positivity rather than merely
fit one scalar coefficient.

## 5. Metric Identification Criteria

A metric-candidate coefficient `C^{ij}` may be identified with inverse spatial
metric data only if the following gates pass.

### Gate M1: locality and first-derivative form

The curvature must depend on `N,M` through

```math
N\partial_jM-M\partial_jN
```

up to controlled lower-order gauge terms or boundary terms. Nonlocal dependence
on remote lapse values fails the metric interpretation.

### Gate M2: tensorial coordinate behavior

Under a spatial coordinate change `x -> y`, the coefficient must transform as a
contravariant tensor or tensor density:

```math
C'^{ab}(y)
=
|\det(\partial x/\partial y)|^w
{\partial y^a\over\partial x^i}
{\partial y^b\over\partial x^j}
C^{ij}(x).
```

The weight `w` depends on the lapse and tangential-generator convention. Paper 10
must state the convention. Without this, the object is only a regulator
coefficient, not geometry.

### Gate M3: symmetry

The symmetric part is the metric candidate:

```math
C^{(ij)}.
```

The antisymmetric part

```math
C^{[ij]}
```

has no ordinary inverse-metric interpretation. If it survives all regulator and
coordinate tests, Paper 10 has found either an obstruction or extra geometric
structure, not a spatial metric.

### Gate M4: positivity and nondegeneracy

For Riemannian spatial slices, the candidate must satisfy

```math
C^{ij}(x)\xi_i\xi_j>0
```

for nonzero covectors `\xi`, up to the declared density convention. If the
coefficient is degenerate or indefinite, it is not ordinary spatial metric data.

### Gate M5: regulator stability

For every admissible regulator family `r`, there may be a known scalar
normalization `Z_r(a)`, but after this normalization the same `C^{ij}` must be
obtained:

```math
C^{ij}_{r}(x)\longrightarrow C^{ij}(x).
```

If different local deformation rules give different tensor fields on the same
background, stochastic curvature has not reconstructed geometry.

### Gate M6: no hidden lift dependence

The coefficient must be determined by the declared finite stochastic kernels,
comparison maps, projective maps, and normalized exchange-curvature data. If it
requires a Hilbert lift, phase convention, or circuit decomposition not fixed by
the stochastic connection, the metric claim fails at `Gamma` level.

The same calculation may still define an enriched-representation coefficient.
In that case Paper 10 must say so explicitly:

```text
this coefficient is a metric diagnostic of the QFT-matching representation,
not a metric reconstructed from bare stochastic kernels.
```

This distinction is not cosmetic. It decides whether Paper 10 advances
probability-first geometry or merely checks that an already chosen QFT
representation contains the metric put into its principal symbol.

## 6. First Benchmark: Flat `2+1D` Free Field

The first concrete benchmark should be deliberately plain.

### Candidate model

Use a free relativistic lattice Dirac or scalar model on a two-dimensional
spatial lattice with spacing `a`, large finite support, and a fixed flat spatial
background. For the Dirac version, use a principal part of the form

```math
H_a
=
\sum_{j=1}^2
\alpha^j D_{j,a}
+m\beta
```

or an anisotropic/rotated variant with constant frame coefficients. The
primitive finite stochastic kernel is still the Born-squared endpoint kernel

```math
\Gamma_a(U)_{xy}=|U_{xy}|^2
```

for the declared whole slab or deformation, not a Markov product through
unrecorded gates.

### Expected flat result

For isotropic flat space, the target is

```math
C^{ij}=\delta^{ij}
```

up to a known scalar normalization convention. Thus

```math
\beta^i=\delta^{ij}(N\partial_jM-M\partial_jN).
```

For a constant anisotropic benchmark, the target should be

```math
C^{ij}=h^{ij}_{0},
```

where `h^{ij}_{0}` is the known constant inverse spatial metric used in the
principal symbol. Rotated constant metrics should produce cross terms
`C^{12}=C^{21}`. Those cross terms are the simplest nontrivial check that the
coefficient is tensorial rather than an axis-by-axis lattice artifact.

### Minimum deliverables

1. Define localized finite deformation maps for lapse profiles in two spatial
   directions.
2. Prove a support/onset filtration for the relevant exchange coefficients.
3. Build a face-centered or cell-centered smearing convention replacing the
   bond-centered `1+1D` convention.
4. Prove the discrete antisymmetry identity:
   ```math
   N_xM_{x+r}-M_xN_{x+r}
   =
   a\,r^j(N\partial_jM-M\partial_jN)(x+r/2)+O(a^2).
   ```
5. Compute the strip/face first moments and test whether they assemble into
   `C^{ij}`.
6. Prove convergence on smooth compactly supported sampled test fields.
7. Repeat for a rotated or anisotropic constant metric to test cross terms.

## 7. Theorem 10.1: Metric Coefficient Extraction Lemma

This section turns the first metric gate into a theorem. The theorem is
deliberately conditional: it does not prove that a finite ISP model has the
right curvature form. It proves that once the finite model supplies that form,
the metric-candidate coefficient is unique, pointwise extractable, and subject
to clean metric-identification tests.

Let

```math
\mathcal N=C_c^\infty(\Sigma)
```

be the tested lapse space, and let

```math
K:\mathfrak X_c(\Sigma)\longrightarrow {\rm End}(\mathcal D)
```

be the tested tangential-deformation representation on the continuum state or
effect domain `\mathcal D`. Let `\mathcal G_K=\ker K` denote the declared
tangential gauge kernel.

**Theorem 10.1: metric coefficient extraction.** Suppose `d\ge2` and the
continuum exchange-curvature limit

```math
\mathfrak C:\mathcal N\times\mathcal N\longrightarrow {\rm End}(\mathcal D)
```

satisfies the following assumptions.

1. **Tangential closure.** There is a bilinear alternating map
   `\beta:\mathcal N\times\mathcal N\to\mathfrak X_c(\Sigma)/\mathcal G_K`
   such that
   ```math
   \mathfrak C[N,M]=K[\beta[N,M]] .
   ```
2. **Local anchored first-jet form.** In every coordinate chart, the class
   `\beta[N,M](x)` is represented by a vector field whose value at `x` depends
   only on the first jets
   ```math
   (N(x),dN_x,M(x),dM_x),
   ```
   depends smoothly on `x`, is bilinear and alternating in `(N,M)`, and vanishes
   whenever
   ```math
   N(x)=M(x)=0.
   ```
   The last condition removes pure gradient-wedge terms
   `\partial_jN\,\partial_kM-\partial_jM\,\partial_kN`, which are not part of
   the hypersurface-deformation metric bracket.
3. **Local faithfulness.** If a compactly supported vector field in the tested
   class has `K[v]=0`, then `v\in\mathcal G_K`; and on sufficiently small
   coordinate neighborhoods the declared gauge does not identify a nonzero
   pointwise vector with zero.

Then in each coordinate chart there is a unique smooth local coefficient
`C^{ij}(x)`, modulo the declared gauge convention, such that

```math
\beta^i[N,M](x)
=
C^{ij}(x)\bigl(N\partial_jM-M\partial_jN\bigr)(x),
```

and therefore

```math
\mathfrak C[N,M]
=
K_i\!\left[C^{ij}(N\partial_jM-M\partial_jN)\right].
```

Moreover `C^{ij}` is pointwise extractable: for any `x\in\Sigma` and any
covector `\omega_j\in T_x^*\Sigma`, choose lapse jets with

```math
N(x)=1,\qquad M(x)=0,\qquad dN_x=0,\qquad dM_x=\omega.
```

Then

```math
\beta^i[N,M](x)=C^{ij}(x)\omega_j.
```

Thus the exchange-curvature response to localized lapse-jet tests determines
the linear map

```math
C_x:T_x^*\Sigma\longrightarrow T_x\Sigma.
```

### Proof

The argument is local, so work in a coordinate chart and fix a point `x`. Write
the first jets as

```math
a=N(x),\qquad \xi_j=\partial_jN(x),
\qquad
b=M(x),\qquad \eta_j=\partial_jM(x).
```

A bilinear alternating vector-valued function of the two first jets has the
general form

```math
\beta^i_x(N,M)
=
B^{ij}(x)(a\eta_j-b\xi_j)
+A^{ijk}(x)(\xi_j\eta_k-\eta_j\xi_k).
```

There is no independent `ab-ba` term because the lapse-value space is
one-dimensional. The anchored condition says `\beta_x=0` whenever `a=b=0`,
for arbitrary gradients `\xi,\eta`; hence

```math
A^{ijk}(x)=0.
```

Therefore

```math
\beta^i_x(N,M)
=
B^{ij}(x)(N\partial_jM-M\partial_jN)(x).
```

Set `C^{ij}=B^{ij}`. Smooth dependence on `x` follows from the assumed smooth
local first-jet dependence.

For uniqueness, suppose `C^{ij}` and `\widetilde C^{ij}` give the same
curvature. Let

```math
D^{ij}=C^{ij}-\widetilde C^{ij}.
```

Then

```math
K_i[D^{ij}(N\partial_jM-M\partial_jN)]=0
```

for all compactly supported `N,M`. By local faithfulness, the corresponding
vector field is gauge-zero, and in a sufficiently small chart it is pointwise
zero. Using the jet choice

```math
N(x)=1,\quad M(x)=0,\quad dN_x=0,\quad dM_x=\omega
```

gives

```math
D^{ij}(x)\omega_j=0
```

for every covector `\omega`. Hence `D^{ij}(x)=0`. Since `x` was arbitrary,
`C=\widetilde C` on the tested chart, modulo the declared global gauge
equivalence.

The extraction formula follows from the same jet choice. Bump functions allow
these prescribed jets to be realized by compactly supported lapses without
changing the pointwise calculation.

### Coordinate behavior

The theorem itself extracts a coefficient in whatever tangential convention has
been chosen. To identify it as geometry, one must still verify Gate M2.

If lapses are scalars and `K[v]` takes an ordinary vector field, then

```math
\omega_j=N\partial_jM-M\partial_jN
```

is a covector and `\beta^i=C^{ij}\omega_j` is a vector. Coordinate covariance of
`\beta` forces

```math
C'^{ab}(y)
=
{\partial y^a\over\partial x^i}
{\partial y^b\over\partial x^j}
C^{ij}(x),
```

so `C^{ij}` is a contravariant rank-two tensor. If the lapse or tangential
generator convention uses densities, the same calculation gives the density
weight stated in Gate M2:

```math
C'^{ab}(y)
=
|\det(\partial x/\partial y)|^w
{\partial y^a\over\partial x^i}
{\partial y^b\over\partial x^j}
C^{ij}(x).
```

The weight `w` is not optional bookkeeping; it is part of the physical
normalization convention.

### Metric upgrade corollary

If, in addition,

```math
C^{ij}=C^{ji},
\qquad
C^{ij}\xi_i\xi_j>0
\quad(\xi\ne0),
```

and `C^{ij}` obeys the declared contravariant tensor or tensor-density
transformation law, then `C^{ij}` is inverse spatial metric data, or inverse
spatial metric density data, for the fixed-background benchmark.

If `C^{[ij]}` survives, the theorem has still extracted a real local
coefficient, but not an ordinary inverse metric. If positivity fails, the
coefficient is not Riemannian spatial metric data. If coordinate covariance
fails, the coefficient is a regulator artifact rather than geometry.

### Regulator-stability corollary

For a regulator family `r`, suppose the normalized finite exchange curvature
produces coefficients `C_r^{ij}(a,x)` and allowed scalar normalizations
`Z_r(a)`. If

```math
Z_r(a)C_r^{ij}(a,x)\longrightarrow C^{ij}(x)
```

locally uniformly, and the limit is independent of `r`, then the extracted
coefficient is regulator-stable. If two admissible regulator families produce
different limiting tensors after the allowed normalization, Paper 10 must mark
the metric claim as failed.

### What Theorem 10.1 does not prove

The theorem does not prove:

1. that a concrete ISP model has tangential closure;
2. that the exchange curvature is local;
3. that pure gradient-wedge terms are absent;
4. that `K_i[v^i]` is faithful;
5. that `C^{ij}` is symmetric or positive;
6. that `C^{ij}` is visible at `Gamma` level rather than only after an enriched
   lift.

Those are exactly the burdens of the flat `2+1D` benchmark. The theorem is
useful because it turns that benchmark into a finite list of tests rather than a
vague search for "geometry".

## 8. Benchmark Decision And Candidate Theorem 10.2: Flat `2+1D` Free Metric Test

The first concrete model should be the massive `2+1D` Dirac benchmark, not a
scalar benchmark. The reason is practical and ontological: Papers 7-9 already
use a Dirac/CAR enrichment ledger, and the Dirac operator is first order, so the
principal-symbol metric is exposed directly in the commutator of local normal
deformations. A scalar benchmark is useful later, but it would introduce a
second-order Hamiltonian formalism before the metric-extraction gate is stable.

### Model choice

Work on the lattice `a\mathbb Z^2`, or on a growing two-torus with the same
nonwrapping policy used in Paper 9. Use spinors in `\mathbb C^2` and choose

```math
\alpha^1=\sigma_x,\qquad
\alpha^2=\sigma_y,\qquad
\beta=\sigma_z.
```

Let `E_A^{\ j}` be a constant frame matrix, and define

```math
h_0^{ij}
=
\sum_{A=1}^2 E_A^{\ i}E_A^{\ j}.
```

The finite one-particle Hamiltonian is

```math
H_{a,h}
=
\alpha^A E_A^{\ j}D_{j,a}+m\beta,
\qquad
D_{j,a}={T_{+e_j}-T_{-e_j}\over 2ia}.
```

For a sampled lapse profile `N`, the formal continuum normal generator is

```math
H_{a,h}[N]
=
{1\over2}\bigl(N_aH_{a,h}+H_{a,h}N_a\bigr),
```

where `N_a` is multiplication by `N(an)`. It is tempting to define the smooth
finite kernel directly by

```math
U_a[N;\Delta]=\exp(-i\Delta H_{a,h}[N]),
```

and

```math
\Gamma_a[N;\Delta]_{xy}
=
\left|U_a[N;\Delta]_{xy}\right|^2.
```

Paper 10 does **not** use this direct smooth-lapse Born-squared kernel as the
first comparison-loop definition. The reason is structural: the leading
stochastic coefficient of `|e^{-i\Delta H[N]}|^2` is quadratic in the matrix
entries of `H[N]`, hence quadratic in the lapse. The hypersurface-deformation
bracket needs a bilinear alternating response in `N,M`. Therefore the first
benchmark uses elementary local comparison maps and then smears their
logarithms linearly in the lapse, following the safe Paper 1 finite-slab
strategy.

### Normalized curvature object

Paper 10 fixes the following convention for the first `2+1D` benchmark.

Let `\chi_x` denote the elementary cell lapse at lattice cell/site `x`, with the
chosen face/cell smearing convention to be fixed in the next step. Define the
elementary local normal unitary

```math
U_{a,h}[x;\Delta]
:=
\exp(-i\Delta H_{a,h}[\chi_x]),
```

and its endpoint kernel

```math
\Gamma_{a,h}[x;\Delta]_{yz}
:=
\left|U_{a,h}[x;\Delta]_{yz}\right|^2.
```

The zero-deformation reference is the identity kernel

```math
\Gamma_{a,h}^{0}(\Delta):=I.
```

The elementary comparison map is

```math
J_{a,h}[x;\Delta]
:=
\Gamma_{a,h}[x;\Delta]\bigl(\Gamma_{a,h}^{0}(\Delta)\bigr)^{-1}
=
\Gamma_{a,h}[x;\Delta].
```

For sufficiently small `|\Delta|`, take the principal logarithm of each
elementary comparison map and define the smooth-lapse comparison generator

```math
L_{a,h}[N;\Delta]
:=
a^2\sum_x N_x\log J_{a,h}[x;\Delta],
\qquad
N_x:=N(ax).
```

The smooth-lapse comparison map is then

```math
\mathbb J_{a,h}[N;\Delta]
:=
\exp L_{a,h}[N;\Delta].
```

This is the exact finite object for the first benchmark. It is algebraic and
linear in the lapse at the logarithmic comparison-generator level. It should not
be confused with a Markov product through unrecorded intermediate cells.
For sign-changing smooth lapses, `\mathbb J_{a,h}[N;\Delta]` is an algebraic
pseudo-stochastic comparison map rather than a primitive positive stochastic
kernel; this is acceptable for a curvature test, but it is not an operational
instrument without extra structure.

The comparison loop is the algebraic group commutator

```math
E_{a,h}[N,M;\Delta]
=
\mathbb J_{a,h}[N;\Delta]\,
\mathbb J_{a,h}[M;\Delta]\,
\mathbb J_{a,h}[N;\Delta]^{-1}\,
\mathbb J_{a,h}[M;\Delta]^{-1}.
```

The orientation is fixed by this order. If

```math
L_{a,h}[N;\Delta]
=
\Delta^2\mathcal B_{a,h}[N]+O(\Delta^3),
```

then

```math
E_{a,h}[N,M;\Delta]
=
I+\Delta^4[\mathcal B_{a,h}[N],\mathcal B_{a,h}[M]]+O(\Delta^5).
```

Thus the sign convention is the one in which the leading coefficient is
`[\mathcal B[N],\mathcal B[M]]` and the target vector field is
`h_0^{ij}(N\partial_jM-M\partial_jN)`. If the finite coefficient calculation
produces the opposite sign, the error is in the orientation convention and must
be corrected globally; Paper 10 may not absorb a sign into the definition of
`h_0^{ij}`.

For every fixed finite lattice, the elementary `J_{a,h}[x;\Delta]` and the
smeared `\mathbb J_{a,h}[N;\Delta]` are invertible for sufficiently small
`|\Delta|` because they are analytic and equal `I` at `\Delta=0`. Their inverses
are algebraic and pseudo-stochastic; they are not operational stochastic
instruments.

Define the finite-slab normalized curvature by

```math
\mathfrak C_{a,h}^{\rm slab}[N,M;\Delta]
:=
R_a\Delta^{-4}\bigl(E_{a,h}[N,M;\Delta]-I\bigr),
```

where `R_a` is the spatial strip/face normalization to be fixed by the first
moment calculation. The exact value of `R_a` is not a convention-free input; it
is part of the finite benchmark and must be chosen once so that the isotropic
flat metric gives `C^{ij}=\delta^{ij}`.

The coefficient-level curvature associated with the same loop is

```math
\mathfrak C_{a,h}^{\rm coef}[N,M]
:=
R_a[\mathcal B_{a,h}[N],\mathcal B_{a,h}[M]],
\qquad
\mathcal B_{a,h}[N]:=[\Delta^2]L_{a,h}[N;\Delta].
```

This is the object used for the support/onset and first-moment calculation. A
finite-slab theorem must then prove a coupled small-slab estimate of the form

```math
\left\|
\mathfrak C_{a,h}^{\rm slab}[N,M;\Delta(a)]\iota_a\phi
-
\mathfrak C_{a,h}^{\rm coef}[N,M]\iota_a\phi
\right\|
\longrightarrow0
```

under an explicit condition on `\Delta(a)`. Until that estimate is proved,
Paper 10's metric claim is coefficient-level.

This log-smeared comparison-loop convention is not the only possible
regularization. A truly primitive smooth-lapse kernel based directly on
`|e^{-i\Delta H[N]}|^2` would be physically attractive, but it has a different
lapse-onset structure and requires a separate theorem before it can be used as a
metric-coefficient extractor. Another admissible cross-check is to replace
elementary cell maps by face maps and define

```math
\mathbb J_{a,h}^{\rm face}[N;\Delta]
=
\exp\!\left(\sum_f w_fN_f\log J_{a,h}[f;\Delta]\right).
```

Those alternatives are later regulator-stability tests, not the definition of
the first benchmark.

The target continuum form is

```math
\mathfrak C_{a,h}^{\rm coef}[N,M]\iota_a\phi
\longrightarrow
K_i[h_0^{ij}(N\partial_jM-M\partial_jN)]\phi
```

with the finite-slab version obtained by replacing `\mathfrak C^{\rm coef}` by
`\mathfrak C^{\rm slab}` after the remainder theorem is proved. The convergence
is required for all compactly supported smooth lapses `N,M` and sampled test
fields `\phi`, possibly modulo explicitly identified lower-order gauge terms.
Any surviving non-gauge lower-order term fails the clean metric interpretation.

### Explicit cross-term benchmark

The isotropic test is

```math
h_0^{ij}=\delta^{ij}.
```

That test is necessary but too easy. The decisive flat benchmark is a rotated
anisotropic constant metric. Choose, for example,

```math
h_0
=
R_{\pi/4}
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix}
R_{\pi/4}^{T}
=
\begin{pmatrix}
5/2&-3/2\\
-3/2&5/2
\end{pmatrix}.
```

Then the target tangential vector field is

```math
\begin{aligned}
\beta^1
&=
{5\over2}(N\partial_1M-M\partial_1N)
-{3\over2}(N\partial_2M-M\partial_2N),\\
\beta^2
&=
-{3\over2}(N\partial_1M-M\partial_1N)
+{5\over2}(N\partial_2M-M\partial_2N).
\end{aligned}
```

This is the first serious tensoriality test. An axis-by-axis lattice artifact
can reproduce the isotropic case and even a diagonal anisotropic case. It should
not reproduce the rotated cross terms unless the exchange-curvature coefficient
is actually seeing the principal-symbol metric.

### Candidate Theorem 10.2

For the constant-frame `2+1D` Dirac benchmark above, prove that there exists an
allowed spatial normalization `R_a` such that

```math
\mathfrak C_{a,h}^{\rm coef}[N,M]\iota_a\phi
\longrightarrow
K_i[h_0^{ij}(N\partial_jM-M\partial_jN)]\phi
```

locally uniformly for smooth compactly supported lapses and sampled test
fields, first for `h_0=I` and then for the rotated anisotropic matrix above.
Equivalently, using

```math
\mathfrak C_{a,h}^{\rm coef}[N,M]
=
R_a[\mathcal B_{a,h}[N],\mathcal B_{a,h}[M]],
```

the first-moment tensor of the commutator coefficient must converge to
`h_0^{ij}`.

The finite-slab strengthening is the same statement with
`\mathfrak C_{a,h}^{\rm coef}` replaced by
`\mathfrak C_{a,h}^{\rm slab}[N,M;\Delta(a)]`, under an explicit small-slab
condition. Paper 10 should not claim that strengthening until the finite-slab
remainder is bounded.

Passing only `h_0=I` is not enough. Paper 10 needs the rotated matrix, because
the cross terms are what distinguish metric extraction from coordinate-axis
curve fitting.

### Immediate proof obligations

The benchmark now has five concrete obligations.

1. Prove the two-dimensional support/onset filtration for exchange
   coefficients. Done at coefficient level in Proposition 10.3.
2. Replace the `1+1D` bond-centered smearing by a face-centered or
   cell-centered smearing convention. Done at audit level in Proposition 10.4:
   use the axis-face channel basis.
3. Compute the first moment tensor of the exchange coefficient and show that it
   equals `h_0^{ij}` after the allowed normalization. The tensor package to
   compute is defined in Proposition 10.3; Proposition 10.4 shows the leading
   site/cell coefficient cannot produce off-diagonal entries.
4. Prove that lower-order Clifford/spin terms are either absent, vanish in the
   limit, or lie in the declared tangential gauge kernel. Proposition 10.4
   identifies the main residual as lost frame-interference data, not gauge.
5. Prove the finite-slab remainder estimate if Paper 10 wants the stronger
   `\mathfrak C^{\rm slab}` theorem rather than only the coefficient theorem.

### Proposition 10.3: coefficient onset and finite active displacement formula

This proposition completes the support/onset setup for the first benchmark. It
does not yet compute the metric tensor. It proves that the coefficient-level
problem reduces to a finite list of translated commutator channels with a
standard lapse-antisymmetry factor.

Let

```math
H_x:=H_{a,h}[\chi_x],
\qquad
J_x(\Delta):=J_{a,h}[x;\Delta],
```

and write matrix indices as site-spin labels `u=(n,s)`. For the site-centered
cell convention, the elementary active stencil is

```math
S:=\{0,\pm e_1,\pm e_2\},
\qquad
S_x:=x+S.
```

For a later face-centered convention, `S` is replaced by the corresponding
finite face stencil; the proof below uses only that `S` is finite and
translation-covariant.

**Proposition 10.3: onset/support filtration.** For the constant-frame
`2+1D` Dirac benchmark:

1. the elementary logarithmic comparison map has the expansion
   ```math
   \log J_x(\Delta)
   =
   \Delta^2A_x^{(1)}+O(\Delta^3);
   ```
2. `A_x^{(1)}` is supported on the active stencil `S_x`;
3. `A_x^{(1)}` is mass-independent at this order;
4. `[A_x^{(1)},A_y^{(1)}]=0` whenever `S_x\cap S_y=\varnothing`;
5. the coefficient-level curvature has the finite displacement form
   ```math
   \mathfrak C_{a,h}^{\rm coef}[N,M]
   =
   {R_a a^4\over2}
   \sum_x\sum_{r\in\mathcal R}
   \bigl(N_xM_{x+r}-M_xN_{x+r}\bigr)
   [A_x^{(1)},A_{x+r}^{(1)}],
   ```
   where
   ```math
   \mathcal R:=(S-S)\setminus\{0\};
   ```
6. for fixed `r\in\mathcal R`,
   ```math
   N_xM_{x+r}-M_xN_{x+r}
   =
   a\,r^j(N\partial_jM-M\partial_jN)(ax)
   +O(a^2|r|^2\|N,M\|_{C^2})
   ```
   uniformly on compact support away from the periodic seam.

Consequently the metric-coefficient calculation is reduced to a finite
first-moment problem over `r\in\mathcal R`.

#### Proof

For a Hermitian finite Hamiltonian `H_x`,

```math
U_x(\Delta)=e^{-i\Delta H_x}
=
I-i\Delta H_x-\frac{\Delta^2}{2}H_x^2+O(\Delta^3).
```

The Born-squared endpoint kernel has no linear term:

```math
J_x(\Delta)=|U_x(\Delta)|^2
=
I+\Delta^2A_x^{(1)}+O(\Delta^3),
```

where, for `u\ne v`,

```math
(A_x^{(1)})_{uv}=|(H_x)_{uv}|^2,
```

and the diagonal is fixed by zero column sum:

```math
(A_x^{(1)})_{vv}
=
-\sum_{u\ne v}|(H_x)_{uv}|^2.
```

Since `\log(I+\Delta^2A+O(\Delta^3))=\Delta^2A+O(\Delta^3)`, the same
coefficient appears in `\log J_x(\Delta)`.

The symmetric local normal Hamiltonian satisfies

```math
(H_x)_{uv}
=
{1\over2}\bigl(\chi_x(u)+\chi_x(v)\bigr)(H_{a,h})_{uv}.
```

Because `H_{a,h}` has only the mass term and nearest-neighbor central-difference
terms, `(H_x)_{uv}` can be off-diagonal only on coordinate edges incident on
`x`. Thus the off-diagonal stochastic transitions generated by
`A_x^{(1)}` lie inside the cross-shaped stencil `S_x`. The mass term is
diagonal in site space, hence it does not contribute to `|(H_x)_{uv}|^2` for
`u\ne v`; it also cancels from the leading diagonal probability balance. The
coefficient `A_x^{(1)}` is therefore mass-independent, exactly as in the
`1+1D` leading coefficient.

If `S_x\cap S_y=\varnothing`, the two matrices act on disjoint site-spin blocks.
Their products agree in either order, so

```math
[A_x^{(1)},A_y^{(1)}]=0.
```

Translation covariance gives

```math
A_x^{(1)}=\tau_xA_0^{(1)}\tau_x^{-1},
```

up to the periodic seam residual excluded by the nonwrapping convention.

Now

```math
\mathcal B_{a,h}[N]
=
[\Delta^2]L_{a,h}[N;\Delta]
=
a^2\sum_xN_xA_x^{(1)}.
```

Therefore

```math
[\mathcal B_{a,h}[N],\mathcal B_{a,h}[M]]
=
a^4\sum_{x,y}N_xM_y[A_x^{(1)},A_y^{(1)}].
```

Only `y=x+r` with `r\in S-S` can contribute. The `r=0` term vanishes because a
matrix commutes with itself. Since the active displacement set is symmetric and

```math
[\mathcal B[M],\mathcal B[N]]
=
-[\mathcal B[N],\mathcal B[M]],
```

the finite sum can be antisymmetrized:

```math
[\mathcal B[N],\mathcal B[M]]
=
{a^4\over2}
\sum_x\sum_{r\in\mathcal R}
(N_xM_{x+r}-M_xN_{x+r})
[A_x^{(1)},A_{x+r}^{(1)}].
```

Multiplication by the spatial normalization `R_a` gives the stated curvature
formula.

Finally, Taylor expansion gives

```math
M_{x+r}
=
M_x+a r^j\partial_jM(ax)+O(a^2|r|^2\|M\|_{C^2}),
```

and the analogous expression for `N_{x+r}`. Subtracting yields

```math
N_xM_{x+r}-M_xN_{x+r}
=
a\,r^j(N\partial_jM-M\partial_jN)(ax)
+O(a^2|r|^2\|N,M\|_{C^2}).
```

This proves the reduction.

#### Active displacement set

For the site-centered convention,

```math
\mathcal R
=
\{\pm e_1,\pm e_2,\pm2e_1,\pm2e_2,
\pm(e_1+e_2),\pm(e_1-e_2)\}.
```

Some of these channels may vanish after the spin/Clifford calculation, but no
other displacement can contribute to the leading coefficient.

#### First-moment tensor package

The next calculation must decompose the finite channel

```math
C_r:=[A_0^{(1)},A_r^{(1)}]
```

into tangential strip/face channels and non-metric residuals. Write this
schematically as

```math
C_r
=
\sum_{i=1}^2 s_r^i(a,h)\,\mathsf T_i
+\mathsf G_r
+\mathsf R_r,
```

where:

1. `\mathsf T_i` is the normalized local channel converging to the tangential
   generator `K_i`;
2. `\mathsf G_r` lies in the declared tangential gauge kernel, if any;
3. `\mathsf R_r` must vanish after the continuum normalization or else is a
   non-metric obstruction.

The first-moment matrix to be computed is

```math
T_a^{ij}
:=
{R_a a^5\over2}
\sum_{r\in\mathcal R}r^j s_r^i(a,h).
```

The flat metric benchmark passes at coefficient level precisely if one can
choose a regulator-stable `R_a` such that

```math
T_a^{ij}\longrightarrow h_0^{ij}
```

and the summed gauge/residual channels vanish or are explicitly accounted for.
For the rotated anisotropic test, this means producing nonzero off-diagonal
limits

```math
T^{12}=T^{21}=-{3\over2}.
```

This is the concrete object the next section must evaluate.

### Proposition 10.4: leading first-moment audit and rotated-metric obstruction

This proposition performs the first-moment audit for the leading site/cell
Born-squared Dirac coefficient. The result is important and negative: the
leading `Gamma`-level coefficient sees the coordinate-edge intensities
`h_0^{11}` and `h_0^{22}`, but it does not see the off-diagonal metric entry
`h_0^{12}`. Therefore the rotated anisotropic benchmark fails for this first
regularization.

#### Face-centered channel basis

Use the axis-face channel basis `\mathsf T_i(f)` as the two-dimensional
replacement for the `1+1D` bond-centered channel. For an oriented face
`f=(x+e_i/2,i)`, `\mathsf T_i(f)` denotes the local antisymmetric transfer
channel across that face, normalized so that smooth face sums converge to the
tangential generator `K_i[v^i]`. A coefficient channel is metric-relevant only
through its projection onto the span of these two axis-face channels:

```math
C_r
\mapsto
\sum_{i=1}^2s_r^i(a,h)\mathsf T_i+\mathsf G_r+\mathsf R_r.
```

Here `\mathsf G_r` is declared tangential gauge, and `\mathsf R_r` is residual.
This is the minimal channel basis needed to test whether a vector field
`\beta^i=C^{ij}\omega_j` is present. It is also the basis in which off-diagonal
metric entries must appear as cross moments: `T^{12}` and `T^{21}`.

#### Explicit elementary coefficient

Define the coordinate Dirac edge matrices

```math
\gamma^j:=\alpha^AE_A^{\ j}
=
E_1^{\ j}\sigma_x+E_2^{\ j}\sigma_y.
```

In the chosen Pauli representation,

```math
\gamma^j
=
\begin{pmatrix}
0&E_1^{\ j}-iE_2^{\ j}\\
E_1^{\ j}+iE_2^{\ j}&0
\end{pmatrix}.
```

Thus the only off-diagonal site transitions in `H_x` are spin-flips across
coordinate edges incident on `x`. For an edge in coordinate direction `j`,

```math
\left|(H_x)_{(n\pm e_j,\bar s),(n,s)}\right|^2
=
{1\over16a^2}
\left((E_1^{\ j})^2+(E_2^{\ j})^2\right)
=
{h_0^{jj}\over16a^2},
```

whenever the edge is incident on `x`, with the diagonal fixed by zero column
sum. Here `\bar s` denotes the opposite spin. Therefore the leading elementary
coefficient has the form

```math
A_x^{(1)}
=
\kappa_1\mathsf L_{x,1}
+\kappa_2\mathsf L_{x,2},
\qquad
\kappa_j={h_0^{jj}\over16a^2},
```

where `\mathsf L_{x,j}` is the universal spin-flip star generator on the two
coordinate edges in direction `j` incident on `x`.

The off-diagonal frame entry

```math
h_0^{12}
=
E_1^{\ 1}E_1^{\ 2}+E_2^{\ 1}E_2^{\ 2}
=
\operatorname{Re}(z_1\overline z_2)
```

with `z_j=E_1^{\ j}+iE_2^{\ j}`, is absent. The Born-squared leading coefficient
keeps `|z_1|^2` and `|z_2|^2`, but loses the relative phase between `z_1` and
`z_2`.

#### Commutator channels

For every active displacement `r`,

```math
C_r=[A_0^{(1)},A_r^{(1)}]
```

is a polynomial in `\kappa_1,\kappa_2` with universal axis-stencil
coefficients:

```math
C_r
=
\kappa_1^2[\mathsf L_{0,1},\mathsf L_{r,1}]
+\kappa_1\kappa_2[\mathsf L_{0,1},\mathsf L_{r,2}]
+\kappa_2\kappa_1[\mathsf L_{0,2},\mathsf L_{r,1}]
+\kappa_2^2[\mathsf L_{0,2},\mathsf L_{r,2}].
```

The channel coefficients `s_r^i(a,h)` in the face basis are therefore functions
only of `\kappa_1,\kappa_2`; they cannot depend on `h_0^{12}`.

#### First-moment consequence

The first-moment matrix from Proposition 10.3 has the form

```math
T_a^{ij}
=
F^{ij}_a(\kappa_1,\kappa_2),
```

with no dependence on `h_0^{12}`. More strongly, the axis-face channel basis and
the site-centered stencil are invariant under the independent coordinate
reflections `x^1\mapsto-x^1` and `x^2\mapsto-x^2`. The off-diagonal entries
`T^{12}` and `T^{21}` change sign under one of these reflections, while the
leading Born-squared coefficient does not. Hence

```math
T_a^{12}=T_a^{21}=0
```

for this leading site/cell convention.

The diagonal entries may still be calibrated in the isotropic case. If the
diagonal channel constant is nonzero, choose `R_a` so that for `h_0=I`,

```math
T_a^{ij}\longrightarrow\delta^{ij}.
```

That would pass the isotropic benchmark. It would not prove tensorial metric
recovery.

#### Rotated benchmark failure

For the rotated anisotropic metric selected above,

```math
h_0
=
\begin{pmatrix}
5/2&-3/2\\
-3/2&5/2
\end{pmatrix},
```

the leading coefficient sees only

```math
\kappa_1=\kappa_2={5\over32a^2}.
```

It therefore produces an axis-symmetric first-moment matrix with zero
off-diagonal entries:

```math
T_a^{12}=T_a^{21}=0,
```

whereas the target requires

```math
h_0^{12}=h_0^{21}=-{3\over2}.
```

No scalar normalization `R_a` can turn zero off-diagonal entries into
`-3/2`. The leading site/cell Born-squared Dirac coefficient therefore fails
Gate M2 for rotated metrics.

#### Residual-channel audit

This failure is not a harmless gauge term. The missing quantity is the relative
frame phase/interference information

```math
\operatorname{Re}(z_1\overline z_2),
```

which is exactly the off-diagonal metric coefficient. It has already been
erased by the leading `Gamma`-level Born-squared map before the commutator is
formed. Thus the obstruction is:

```text
leading Gamma-level edge intensities do not determine the full inverse metric
tensor for rotated constant frames.
```

The first benchmark can still be useful as a diagonal-metric or isotropic
sanity check, but it cannot be the theorem proving fixed-background metric
reconstruction.

#### Consequences

Paper 10 now has a clean fork.

1. **Gamma-level diagonal benchmark.** Continue with the present leading
   Born-squared coefficient, but downgrade the theorem to diagonal/axis-aligned
   metric data only.
2. **Higher-order Gamma-level search.** Look for `h^{12}` in higher
   exchange-coefficient orders where two-direction path interference can enter.
   This requires a new support/onset theorem and may or may not survive
   regulator normalization.
3. **Enriched-representation metric diagnostic.** Use the Dirac lift before
   Born-squaring; then the principal symbol contains `h^{ij}`. This is not
   Gamma-level metric reconstruction.
4. **Different primitive stochastic rule.** Design a local stochastic
   comparison map whose elementary coefficient retains oriented frame
   interference. That would be a new ISP postulate, not a consequence of the
   current Born-squared endpoint rule.

The honest conclusion is negative for the first attempted `2+1D` Gamma-level
metric benchmark.

### Proposition 10.5: higher-order Gamma-level search for frame interference

Option 2 asks whether the missing off-diagonal metric entry can reappear in
higher `Gamma`-level coefficients. For the strict site-star elementary map of
Proposition 10.3, the situation is even worse than the leading audit suggests:
two-step paths between different arms of the star are unique, so their
Born-squared probabilities still contain only products such as `h^{11}h^{22}`.

The first plausible place for genuine two-direction interference is therefore a
slightly richer face/cell elementary support that contains both path orderings
around a plaquette corner. The following audit is the optimistic version of
option 2: even when such two-path interference is allowed, the first recovered
quantity is signless.

The answer is mixed but still negative for metric reconstruction:

```text
h^{12} reappears as a probability invariant, but only through signless
quadratic combinations such as (h^{12})^2.
```

That can diagnose non-orthogonality of the frame axes, but it cannot supply the
signed tensor component required in

```math
\beta^i=h^{ij}(N\partial_jM-M\partial_jN).
```

#### Two-step diagonal amplitudes in a face/cell support

Let

```math
z_j:=E_1^{\ j}+iE_2^{\ j},
\qquad
\gamma^j=
\begin{pmatrix}
0&\overline z_j\\
z_j&0
\end{pmatrix}.
```

Then

```math
h^{jj}=|z_j|^2,
\qquad
h^{12}=\operatorname{Re}(z_1\overline z_2).
```

The two-step amplitudes of a face/cell local Dirac stencil containing both path
orderings around a coordinate corner contain the Clifford products

```math
\gamma^1\gamma^2+\gamma^2\gamma^1=2h^{12}I
```

and

```math
\gamma^1\gamma^2-\gamma^2\gamma^1
=
2i\,d_E\,\sigma_z,
\qquad
d_E:=E_1^{\ 1}E_2^{\ 2}-E_2^{\ 1}E_1^{\ 2}.
```

Thus diagonal two-step transitions can distinguish the two invariants

```math
(h^{12})^2,
\qquad
d_E^2=h^{11}h^{22}-(h^{12})^2.
```

For example, a diagonal displacement of type `e_1+e_2`, if both ordered paths
are included in the elementary support, receives a two-path amplitude
proportional to the anticommutator and hence a probability proportional to

```math
(h^{12})^2.
```

A diagonal displacement of type `e_1-e_2`, again in a support containing the
two ordered paths, receives the commutator channel and hence a probability
proportional to

```math
d_E^2.
```

So higher `Gamma` coefficients in a richer face/cell support can detect that the
frame is rotated/nonorthogonal in magnitude. This is already more information
than the leading edge-intensity coefficient, but it is still not signed tensor
data.

#### Why this still fails the metric bracket

The hypersurface-deformation bracket needs the signed coefficient `h^{12}`.
Under the coordinate reflection `x^2\mapsto -x^2`, a contravariant tensor obeys

```math
h^{12}\mapsto -h^{12}.
```

But the two-step Born-squared invariants above obey

```math
(h^{12})^2\mapsto (h^{12})^2,
\qquad
d_E^2\mapsto d_E^2.
```

They cannot decide between the two rotated metrics

```math
\begin{pmatrix}
5/2&-3/2\\
-3/2&5/2
\end{pmatrix}
\quad\hbox{and}\quad
\begin{pmatrix}
5/2&+3/2\\
+3/2&5/2
\end{pmatrix}.
```

Both give the same two-step probability invariants. Therefore no scalar
normalization of these higher-order probability coefficients can produce a
coordinate-covariant signed cross coefficient.

#### Interaction with the exchange loop

The coefficient-level exchange curvature is built from commutators of the
logarithmic comparison coefficients:

```math
[\mathcal B[N],\mathcal B[M]].
```

If the next logarithmic coefficient is written schematically as

```math
[\Delta^4]\log J_x(\Delta)=A_x^{(2)},
```

then higher exchange orders contain terms such as

```math
[A_x^{(1)},A_y^{(2)}]+[A_x^{(2)},A_y^{(1)}].
```

The two-step audit says that `A_x^{(2)}` may contain scalar information about
`(h^{12})^2` and `d_E^2`, but not the signed `h^{12}` needed for `T^{12}`.
Consequently these terms may improve a **shape diagnostic** of the frame, but
they do not by themselves repair the metric-coefficient theorem.

#### What a successful higher-order rescue would need

A genuine higher-order Gamma-level rescue must exhibit a regulator-stable
coefficient whose moment transforms linearly and with sign as `h^{12}`. In
practice that means proving all three statements:

1. a signed off-diagonal moment survives the exchange-loop antisymmetrization;
2. the sign changes correctly under `x^2\mapsto -x^2`;
3. the same normalization that recovers the diagonal components recovers the
   off-diagonal component.

The strict site-star sector does not even reach this stage at the first
non-leading order. The richer face/cell two-step probability sector reaches it,
but fails the first two requirements. It supplies only signless frame
invariants.

#### Current verdict on option 2

Option 2 is not dead in an all-order mathematical sense, but the first
plausible higher-order place where frame interference appears does not rescue
metric reconstruction. It supports the following sharper obstruction:

```text
bare Gamma-level probabilities may contain scalar invariants of the metric
shape, including |h^{12}|, but the signed tensor coefficient h^{12} is not
available at the first interference order.
```

Paper 10 should therefore not proceed to curved backgrounds on the basis of
this higher-order signal. The next rigorous choices are:

1. prove an all-order sign-ambiguity no-go for the present Born-squared rule;
2. restrict the Gamma-level theorem to diagonal/axis-aligned metrics;
3. move to an enriched-representation metric diagnostic where the Dirac
   principal symbol, not bare `Gamma`, carries `h^{ij}`;
4. change the primitive stochastic rule so oriented frame interference is not
   erased before the exchange curvature is formed.

### Proposition 10.6: all-order sign-ambiguity no-go for the Born-squared rule

This proposition proves the all-order obstruction for the present finite
Born-squared endpoint rule. It is stronger than the leading and first
higher-order audits: the obstruction is an exact finite-regulator ambiguity,
not a truncation artifact.

Let `E` be a constant frame and define the sign-flipped frame

```math
\widetilde E_A^{\ 1}=E_A^{\ 1},
\qquad
\widetilde E_A^{\ 2}=-E_A^{\ 2}.
```

Then

```math
\widetilde h^{11}=h^{11},
\qquad
\widetilde h^{22}=h^{22},
\qquad
\widetilde h^{12}=-h^{12}.
```

Thus a full metric reconstruction must distinguish `E` from `\widetilde E`
whenever `h^{12}\ne0`.

Work on the infinite lattice or on growing periodic tori with even length in
the `e_2` direction, so the following staggered phase is a well-defined
finite-regulator operator. Define

```math
(S_2\psi)_{n,s}=(-1)^{n_2}\psi_{n,s}.
```

Odd periodic rings/tori are excluded from this particular finite-regulator
symmetry statement; they may be treated by open boundaries or by passing through
the even-torus cofinal subsystem.

It obeys

```math
S_2D_{1,a}S_2^{-1}=D_{1,a},
\qquad
S_2D_{2,a}S_2^{-1}=-D_{2,a},
```

and commutes with site multiplication operators and with the mass matrix. Hence
for every elementary lapse cell `\chi_x`,

```math
H_{a,\widetilde h}[\chi_x]
=
S_2H_{a,h}[\chi_x]S_2^{-1}.
```

Therefore, for every finite slab parameter `\Delta`,

```math
U_{a,\widetilde h}[x;\Delta]
=
S_2U_{a,h}[x;\Delta]S_2^{-1}.
```

Taking entrywise absolute squares gives exact equality of the primitive
stochastic kernels:

```math
\Gamma_{a,\widetilde h}[x;\Delta]
=
\Gamma_{a,h}[x;\Delta].
```

Consequently all elementary comparison maps, their principal logarithms, the
log-smeared comparison maps, and every exchange loop built from them are
identical:

```math
J_{a,\widetilde h}[x;\Delta]=J_{a,h}[x;\Delta],
```

```math
\mathbb J_{a,\widetilde h}[N;\Delta]
=
\mathbb J_{a,h}[N;\Delta],
```

and

```math
E_{a,\widetilde h}[N,M;\Delta]
=
E_{a,h}[N,M;\Delta].
```

The same equality holds coefficient by coefficient in `\Delta`, at all orders,
and for all normalized exchange-curvature coefficients built only from these
`Gamma`-level objects.

**No-go conclusion.** No rule

```math
\Gamma\hbox{-data}\longmapsto C^{ij}
```

depending only on the present Born-squared finite kernels, projective maps,
comparison maps, logarithms, and exchange loops can reconstruct the signed
off-diagonal metric component `h^{12}` for both `E` and `\widetilde E`.

Indeed, the input `Gamma`-level data are identical, so any such rule must return
the same `C^{12}` for both frames. But the target metrics require opposite
values. Therefore full signed inverse-metric reconstruction fails at
`Gamma` level for this Born-squared rule.

#### Interpretation

The ambiguity is a phase/lift ambiguity. The two frames are distinguished at
the Hilbert-operator level by a staggered phase conjugation, but that phase is
invisible after taking endpoint probabilities. This is exactly the Barandes
discipline in action:

```text
Gamma-level data retain transition probabilities, not the oriented Clifford
phase data needed to reconstruct the full frame metric.
```

This is not a coordinate-reflection theorem. The lattice labels are unchanged;
the same endpoint probabilities are obtained on the same labelled finite
configuration space. The missing information is representational phase data,
not a relabelling convention.

#### Positive remnant

The no-go does not say that `Gamma` contains no geometric information. The
present Born-squared rule can still support limited positive claims:

```math
h^{11},\qquad h^{22}
```

are visible in leading coordinate-edge intensities, and richer face/cell
higher-order coefficients can contain signless invariants such as

```math
(h^{12})^2,
\qquad
\det h=h^{11}h^{22}-(h^{12})^2.
```

Thus bare `Gamma` may diagnose diagonal metric data, axis anisotropy, and the
magnitude of nonorthogonality. It cannot reconstruct the signed tensor
coefficient needed for the hypersurface-deformation bracket.

#### Enriched-representation alternative

If Paper 10 allows the enriched Dirac representation, the full metric is
immediately available from the Clifford principal symbol. Define

```math
\gamma^i:=\alpha^AE_A^{\ i}.
```

Then

```math
{1\over2}\{\gamma^i,\gamma^j\}=h^{ij}I.
```

This recovers the signed off-diagonal entry:

```math
h^{12}
=
{1\over4}{\rm tr}(\gamma^1\gamma^2+\gamma^2\gamma^1).
```

But this is **not** `Gamma`-level metric reconstruction. It is an
enriched-representation metric diagnostic: the Hilbert lift, Clifford matrices,
and oriented frame phase have been supplied as part of the representation.

#### Paper 10 identity after the no-go

Paper 10 therefore identifies itself as:

```text
a metric-data gate and Gamma-level obstruction paper.
```

The strongest honest theorem package is:

1. an abstract extraction theorem saying what would count as metric data;
2. a positive diagonal/signless-invariant remnant for Born-squared `Gamma`;
3. an all-order no-go for full signed metric reconstruction from the present
   `Gamma`-level rule;
4. an enriched-representation route that recovers the metric from the Dirac
   principal symbol, explicitly labelled as extra structure.

The paper should not advertise fixed-background metric reconstruction from
bare stochastic kernels.

## 9. Deferred Candidate: Fixed Curved Background Test

The fixed curved-background theorem is no longer in scope for the present
Gamma-level paper unless enriched metric data are explicitly supplied. The
target for a later enriched fixed-background paper would be

```math
\mathfrak C_a[N,M]\iota_a\phi
\longrightarrow
K_i[h^{ij}(x)(N\partial_jM-M\partial_jN)]\phi .
```

This requires a known background `h^{ij}(x)` in the regulated model or a
declared enriched principal-symbol datum from which `h^{ij}(x)` is recovered.
Passing this theorem would show that stochastic exchange curvature can be
compatible with fixed background geometry. It would still not show dynamical
geometry, stress-energy, or Einstein equations.

## 10. Failure Modes

Paper 10 is built to fail cleanly.

1. **Regulator artifact:** different deformation rules give different
   `C^{ij}` after allowed normalization.
2. **Axis artifact:** isotropic axes work, but rotated metrics or cross terms do
   not.
3. **Signed-cross-term obstruction:** the stochastic rule sees only
   diagonal/signless invariants, such as `h^{11}`, `h^{22}`, or `(h^{12})^2`,
   but not the signed `h^{12}` required by the hypersurface-deformation
   bracket.
4. **Nonsymmetric coefficient:** `C^{[ij]}` survives.
5. **Nonpositive coefficient:** the extracted quadratic form is not spatial
   Riemannian metric data.
6. **Nonlocal lapse dependence:** curvature depends on remote lapse values.
7. **Lift dependence:** `C^{ij}` can be recovered only from Hilbert/circuit data
   absent from the stochastic connection.
8. **Tangential nonfaithfulness:** the extracted vector field is not unique
   because `K_i` has a large kernel on the tested domain.
9. **Operational confusion:** a raw coefficient is advertised as an observable
   without the Paper 4/Paper 6 operational projection layer.

Any of these failures is scientifically useful. It says exactly where
probability-first stochastic geometry stops.

## 11. Relation To Gravity

The positive part of Paper 10 justifies this weaker statement:

> Relativistic ISP can test whether fixed-background spatial metric data are
> visible in stochastic exchange curvature.

At the present stage, Paper 10 does **not** justify the stronger statement that
bare `Gamma` reconstructs the full metric. Proposition 10.6 gives an all-order
sign-ambiguity obstruction for the current Born-squared rule.

It would not justify:

1. the metric is dynamical;
2. Einstein equations hold;
3. stress-energy has been reconstructed;
4. quantum gravity has been formulated;
5. Lorentz covariance is automatic;
6. full signed metric reconstruction from bare `Gamma` data.

The next gates after Paper 10 would be:

```text
Gamma-level obstruction or enriched fixed metric data
-> fixed curved background test
-> stress-energy/response theorem
-> dynamical geometry variables
-> Einstein/semiclassical/weak-field limits
```

## 12. Final Theorem Ledger And V3 Export

Paper 10 closes as a gate theorem, not as a positive full-metric
reconstruction theorem.

| Result | Status | Export |
| --- | --- | --- |
| Theorem 10.1, metric coefficient extraction | Positive conditional theorem | Defines what would count as inverse spatial metric data if a local first-derivative curvature coefficient is present. |
| Candidate flat `2+1D` Dirac test | Audited benchmark | Supplies the concrete Born-squared `Gamma` rule tested in the paper. |
| Proposition 10.3, onset/support filtration | Positive finite-stencil theorem | Reduces the coefficient search to finite active displacement channels. |
| Proposition 10.4, leading first-moment audit | Negative for rotated metrics | Leading `Gamma` data see coordinate-edge intensities, not the signed off-diagonal metric entry. |
| Proposition 10.5, higher-order frame-interference search | Negative for signed metric recovery | Higher-order interference can produce signless invariants such as `(h^{12})^2`, not signed `h^{12}`. |
| Proposition 10.6, all-order sign-ambiguity no-go | Negative theorem | The present Born-squared `Gamma` rule cannot reconstruct the full signed inverse spatial metric. |

The V3 export is therefore:

1. `Gamma` remains the stochastic ISP base layer, but it is not sufficient for
   full signed metric reconstruction under the present Born-squared rule.
2. Bare `Gamma` may still export useful geometric remnants: diagonal
   coefficients, anisotropy, determinant-like data, and signless
   nonorthogonality magnitudes.
3. Full signed metric recovery requires an enriched datum, for example a
   Clifford/principal-symbol lift satisfying
   `\frac12\{\gamma^i,\gamma^j\}=h^{ij}I`.
4. Enriched metric recovery is not gravity. It supplies fixed-background
   coefficient data only.
5. Any V3 QFT reconstruction theorem must declare whether metric, orientation,
   phase, CAR/Clifford, and local-instrument data are inputs or outputs.

This is enough to finish Paper 10 for the V2 sequence. It gives V3 a sharp
instruction: start with a minimal enriched ISP data paper before attempting
full relativistic QFT reconstruction.

## 13. Completion Checklist

1. Lock the Paper 9 import discipline and classify every proposed metric claim
   as Gamma-level or enriched-representation. Done in Sections 3 and 5.
2. Prove the abstract Metric Coefficient Extraction Lemma. Done in Section 7.
3. Choose the first `2+1D` free benchmark: Dirac or scalar. Done in Section 8:
   use the constant-frame massive Dirac benchmark first.
4. Define the finite deformation rule and the normalized curvature object.
   Done in Section 8: use the log-smeared elementary normal-comparison loop
   `E=\mathbb J_N\mathbb J_M\mathbb J_N^{-1}\mathbb J_M^{-1}` with
   coefficient-level curvature first and finite-slab curvature only after a
   remainder estimate.
5. Compute the leading support/onset coefficients in the two coordinate
   directions. Done at the support-filtration level in Proposition 10.3.
6. Build the face-centered smearing convention. Done at the channel-audit level
   in Proposition 10.4.
7. Test isotropic flat `C^{ij}=\delta^{ij}`. Proposition 10.4 shows this can be
   calibrated if the diagonal channel constant is nonzero, but this is not a
   tensorial metric test.
8. Test anisotropic/rotated constant `C^{ij}` to expose cross terms. Done in
   Proposition 10.4: the leading site/cell Gamma-level benchmark fails because
   `T^{12}=T^{21}=0`.
9. Audit whether the coefficient is visible at `Gamma` level or only through a
   Hilbert lift. Done: Proposition 10.4 shows that the full rotated metric is
   not visible at leading Gamma level for the present Born-squared rule.
   Proposition 10.5 investigates the first higher-order Gamma-level
   frame-interference sector and finds only signless invariants such as
   `(h^{12})^2`, not the signed tensor component.
   Proposition 10.6 proves the all-order sign-ambiguity no-go for the present
   Born-squared rule.
10. Decide whether the fixed curved-background theorem is in scope for Paper 10 or
   deferred to a later curved-background paper. Deferred unless the paper
   switches explicitly to enriched-representation metric data.

## 14. Current Verdict

Paper 10 is not a positive full-metric reconstruction paper. It is a
metric-data gate and Gamma-level obstruction paper. It has a formal extraction
theorem, a concrete first benchmark, positive diagonal/signless remnants, and an
all-order no-go for full signed metric reconstruction from the present
Born-squared `Gamma` rule.

The strongest honest first claim is:

> If normalized multi-dimensional stochastic exchange curvature has a local
> first-derivative tangential form, then its coefficient can be tested as inverse
> spatial metric data by symmetry, positivity, coordinate behavior, and regulator
> stability.

The first real model burden is now specific: a constant-frame massive `2+1D`
Dirac benchmark with a rotated anisotropic metric

```math
h_0=
\begin{pmatrix}
5/2&-3/2\\
-3/2&5/2
\end{pmatrix}.
```

Proposition 10.4 shows that the leading site/cell Born-squared Dirac
coefficient cannot pass this cross-term test: it sees only coordinate-edge
intensities `h^{11}` and `h^{22}`, not `h^{12}`. Proposition 10.5 then checks
the first higher-order frame-interference signal and finds signless invariants
such as `(h^{12})^2`, still not the signed tensor component required by the
hypersurface-deformation bracket. Proposition 10.6 turns this into an all-order
sign-ambiguity no-go for the current Born-squared rule.

The final Paper 10 conclusion is:

```text
Paper 10 finalizes as a Gamma-level obstruction paper with a positive
diagonal/signless remnant and a declared enriched-representation route for full
signed metric data. Fixed curved backgrounds, stress-energy, and dynamical
geometry are deferred and may not be advertised as Gamma-level consequences.
```
