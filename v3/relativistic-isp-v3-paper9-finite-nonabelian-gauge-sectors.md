# Relativistic ISP V3 Paper 9: Finite Non-Abelian Gauge Sectors

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: theorem-level finite benchmark draft. This paper starts the
non-Abelian part of V3. It does not try to prove continuum Yang-Mills. Its job
is narrower and sharper: formulate a finite non-Abelian gauge-sector ISP model
with declared Gauss constraints, boundary centers, localized comparison maps,
and a first non-Abelian exchange coefficient.

The named benchmark is finite `S_3` gauge theory. Most definitions work for any
finite non-Abelian group `G`; `S_3` is used because it is the smallest concrete
non-Abelian group and it gives an explicit nonzero commutator witness.

The guiding rule is the same as Papers 1-8:

```text
Do not claim that gauge fields, Hilbert representations, or continuum
Yang-Mills have been reconstructed from bare Gamma. Declare the gauge-sector
data, prove the finite stochastic/gauge statements, and export only those.
```

Paper 8's finite-to-continuum audit is active here. In particular, an exact
invertible stochastic covariance on one fixed finite endpoint set would only be
a permutation action, so this paper does not claim exact nontrivial finite
Lorentz covariance. Any continuum covariance, continuum gauge field, or
continuum Yang-Mills claim must be supplied by a later projective/refinement
construction.

## 1. Main Question

Can non-Abelian gauge structure be formulated at the finite `Gamma`, `J`, and
`E` levels, with the necessary sector and enrichment data declared?

The answer of this paper is:

1. **Yes, finitely.** A finite non-Abelian gauge ISP benchmark exists for
   `S_3` gauge variables on links and group-valued matter variables on sites.
2. **Yes, sectorwise.** Gauge-compatible kernels decompose by Gauss/boundary
   sectors, and comparison maps preserve that decomposition.
3. **Yes, locally.** Localized gauge-compatible deformations have localized
   comparison maps inside fixed sectors.
4. **Yes, non-Abelianly.** The first mixed exchange coefficient contains an
   explicit representation commutator in charged transport channels.
5. **No, not yet continuum Yang-Mills.** Representation-cutoff and refinement
   limits are Paper 10.

## 2. The Conservative Target

Let

```math
G=S_3=\langle r,s\mid r^3=e,\ s^2=e,\ srs=r^{-1}\rangle.
```

Every element is uniquely of the form `r^i` or `sr^i`, with `i=0,1,2`.
The conjugacy classes are

```math
C_e=\{e\},
\qquad
C_3=\{r,r^2\},
\qquad
C_2=\{s,sr,sr^2\}.
```

The standard two-dimensional real representation `\rho_{\rm std}` may be
chosen so that

```math
\rho_{\rm std}(r)=
\begin{pmatrix}
-1/2&-\sqrt{3}/2\\
\sqrt{3}/2&-1/2
\end{pmatrix},
\qquad
\rho_{\rm std}(s)=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
```

Then

```math
[\rho_{\rm std}(r),\rho_{\rm std}(s)]
=
\begin{pmatrix}
0&\sqrt{3}\\
\sqrt{3}&0
\end{pmatrix}
\ne 0.
```

This explicit matrix is the finite non-Abelian witness used in Section 9.

Its character values are

```math
\chi_{\rm std}(e)=2,
\qquad
\chi_{\rm std}(r)=\chi_{\rm std}(r^2)=-1,
\qquad
\chi_{\rm std}(s)=\chi_{\rm std}(sr)=\chi_{\rm std}(sr^2)=0.
```

These values are used below as the concrete class functions in the finite
gauge action.

### Why Not Start With `SU(2)`?

`SU(2)` is the correct continuum-facing target, but a finite benchmark should
not hide analytic representation-cutoff assumptions. `S_3` already tests the
hard finite-gauge ontology:

1. gauge redundancy is not a configuration variable;
2. physical records are gauge-invariant or gauge-covariantly endpoint-labelled;
3. local regions carry boundary centers;
4. non-Abelian exchange appears only in oriented representation-carrying
   channels, not in scalar class-function probes alone.

Paper 10 may replace `S_3` by Peter-Weyl or quantum-link cutoffs.

## 2A. Finite Gauge-Sector Audit

### Definition 2A.1: Finite Gauge-Sector Source Ledger

A theorem in this paper is a **finite gauge-sector theorem** only if its inputs
are finite and explicitly declared:

1. a finite group `G`;
2. a finite oriented lattice or 2-complex `K`;
3. a finite raw configuration space `G^V\times G^E`;
4. a finite gauge action `G^V`;
5. the finite physical orbit space `\Omega_K^{phys}`;
6. declared sector labels and boundary-center labels;
7. finite gauge-invariant scalar records or declared charged instruments;
8. finite stochastic kernels and their sectorwise comparison maps.

Its allowed outputs are finite orbit-space laws, finite sector decompositions,
finite center-conditioned gluing statements, finite comparison maps, and finite
exchange coefficients. It does not output a continuum gauge field, continuum
measure, Hamiltonian, Euclidean OS measure, AQFT net, Wightman field, Wilson-loop
area law, mass gap, or confinement theorem.

### Lemma 2A.2: Gauge Redundancy Is Not A Gamma-Only Reconstruction

The finite gauge action, the orbit projection, charged representation labels,
and boundary-center labels used in this paper are declared finite gauge-sector
data. They are not reconstructed from bare `Gamma` alone.

### Proof

The same finite stochastic endpoint kernel may be presented with different
typed gauge actions, different charged instruments, or no charged instruments
at all. Bare `Gamma` records only stochastic endpoint transitions; it does not
select the group `G`, the sitewise gauge action, a representation label
`\rho`, or a boundary-center algebra. Those are exactly the enriched
finite-gauge inputs in Definition 2A.1. `square`

### Theorem 2A.3: No Continuum Yang-Mills Smuggling From Paper 9

Paper 9 may be used downstream only as a finite gauge-sector source in the
sense of Definition 2A.1. It cannot be used as a proof of any of the following:

```text
continuum 4D SU(N) Yang-Mills measure;
Euclidean OS reconstruction;
continuum Lorentz-covariant gauge QFT;
Wilson-loop area law;
mass gap;
confinement;
renormalization-group continuum limit;
exact nontrivial finite-regulator Lorentz covariance.
```

Any later theorem requiring one of these conclusions must prove it in the
later paper or carry it as an explicit source gate.

### Proof

All objects constructed in Sections 3-12 are finite: finite groups, finite
orbits, finite sectors, finite kernels, finite instruments, and finite
comparison maps. Paper 8's continuum reconstruction audit says that continuum
AQFT/Wightman/covariance conclusions require projective-limit, tightness,
uniqueness, spectrum, time-slice, and algebra-completion clauses not present
here. Paper 8's finite covariance no-go also prevents reading a nontrivial
Lorentz boost as an exact stochastic isomorphism of one fixed finite set.
Therefore Paper 9 exports only finite gauge-sector data. `square`

## 3. Finite Gauge Ontology

Let `K` be a finite oriented lattice/2-complex with vertices `V`, oriented
edges `E`, and plaquettes `P`. For each unoriented edge choose one reference
orientation. If `e:x\to y`, write `s(e)=x` and `t(e)=y`.

The raw configuration space is

```math
\Omega_K=G^V\times G^E.
```

An element is written

```math
\omega=(\psi,U),
```

where `\psi_v\in G` is a finite group-valued matter/Higgs variable at vertex
`v`, and `U_e\in G` is a link variable. If the opposite edge is used,
`U_{\bar e}=U_e^{-1}`.

The finite gauge group is

```math
{\mathcal G}_K=G^V.
```

It acts by

```math
(h\cdot\psi)_v=h_v\psi_v,
\qquad
(h\cdot U)_e=h_{t(e)}U_e h_{s(e)}^{-1}.
```

The physical endpoint space is not `\Omega_K` but the orbit space

```math
\Omega_K^{\rm phys}=\Omega_K/{\mathcal G}_K.
```

Equivalently, physical scalar records are gauge-invariant functions on
`\Omega_K`.

### Minimal Tiny Lattice

The explicit coefficient calculation later uses the square one-plaquette
lattice with vertices `0,1,2,3`, oriented boundary edges

```math
e_{01},e_{12},e_{23},e_{30},
```

and one plaquette

```math
p=e_{30}e_{23}e_{12}e_{01}.
```

The charged transport path used for the non-Abelian witness is the single edge
`\gamma=e_{01}`. This is the smallest example with a plaquette scalar channel,
a matter-link channel, and a charged transport channel on the same finite
gauge system.

### Lemma 3.1: Gauge-Fixed Physical Endpoint Model

For any connected finite `K`, the map

```math
\Phi:\Omega_K^{\rm phys}\to G^E,
\qquad
\Phi([\psi,U])_e=\psi_{t(e)}^{-1}U_e\psi_{s(e)}
```

is a bijection.

### Proof

The expression `\psi_{t(e)}^{-1}U_e\psi_{s(e)}` is gauge-invariant by Lemma
4.1 for paths of length one. Thus `\Phi` is well-defined on gauge orbits.

It is surjective because any tuple `(H_e)_{e\in E}\in G^E` is represented by
the raw configuration `\psi_v=e` for all vertices and `U_e=H_e`.

It is injective because for any raw configuration choose the gauge
transformation `h_v=\psi_v^{-1}`. Then `h\cdot\psi_v=e`, and the transformed
link variable is exactly `H_e=\psi_{t(e)}^{-1}U_e\psi_{s(e)}`. Hence every
orbit has a unique representative with all matter variables fixed to the group
identity. `square`

For the one-plaquette lattice, this gives the concrete finite endpoint set

```math
\Omega_{\square}^{\rm phys}\cong S_3^4,
\qquad
|\Omega_{\square}^{\rm phys}|=6^4=1296.
```

In gauge-fixed variables

```math
H_{ij}=\psi_j^{-1}U_{ij}\psi_i,
```

the plaquette class is read from

```math
H_p=H_{30}H_{23}H_{12}H_{01}.
```

The scalar matter-link record on `e_{01}` is `H_{01}` up to class function,
and the charged transport channel on `e_{01}` is the representation matrix
`\rho_{\rm std}(H_{01})` with declared endpoint vectors. Thus the tiny model is
fully finite and computationally checkable.

## 4. Gauge-Invariant Local Data

For an oriented path `\gamma=e_n\cdots e_1`, define the path transporter

```math
U_\gamma=U_{e_n}\cdots U_{e_1}.
```

If `\gamma:x\to y`, the group-valued matter-dressed transporter is

```math
T_\gamma(\omega)=\psi_y^{-1}U_\gamma\psi_x.
```

### Lemma 4.1: Matter-Dressed Transporters Are Gauge-Invariant

For every path `\gamma:x\to y`,

```math
T_\gamma(h\cdot\omega)=T_\gamma(\omega).
```

### Proof

The path transporter transforms as

```math
U_\gamma\mapsto h_y U_\gamma h_x^{-1}.
```

The endpoint matter variables transform as

```math
\psi_y\mapsto h_y\psi_y,\qquad \psi_x\mapsto h_x\psi_x.
```

Therefore

```math
(h_y\psi_y)^{-1}(h_yU_\gamma h_x^{-1})(h_x\psi_x)
=
\psi_y^{-1}U_\gamma\psi_x.
```

Thus `T_\gamma` is gauge-invariant. `square`

For a plaquette `p` with chosen basepoint, define its holonomy `U_p`. Under
gauge transformations it changes by conjugation at the basepoint. Therefore any
class function `c:G\to{\mathbb R}` gives a gauge-invariant plaquette observable
`c(U_p)`.

The basic finite gauge records are:

1. scalar plaquette records `c(U_p)`;
2. scalar matter-link records `c(\psi_{t(e)}^{-1}U_e\psi_{s(e)})`;
3. charged transport records `\ell^*\rho(T_\gamma)r`, where `\rho` is a
   declared finite-dimensional representation and `\ell,r` are declared
   endpoint source/sink vectors.

The third class is enriched operational data. It is not reconstructed from
bare `Gamma`; it is a declared charged probe.

## 5. Gauss Sectors And Boundary Centers

For a finite region `R\subset K`, let `K_R` be the induced subcomplex and let
`\partial R` denote its cut vertices/links. The local gauge group
`{\mathcal G}_R^{0}` consists of gauge transformations supported in the
interior of `R` and equal to the identity on `\partial R`.

### Definition 5.1: Boundary Center Label

The boundary center label of a configuration relative to `R` is the orbit

```math
\sigma_R(\omega)
=
\left[\omega|_{\partial R}\right]_{
{\mathcal G}_R^{0}\times{\mathcal G}_{K\setminus R}^{0}}.
```

Equivalently, `\sigma_R` is the maximal boundary information that both the
inside and outside gauge-invariant algebras can read without choosing a gauge.

### Interpretation

This is the finite stochastic analogue of the gauge-theory fact that local
physical algebras do not tensor-factor cleanly across a boundary. Boundary
electric/representation centers must be tracked; otherwise a local
factorization theorem is false.

### Lemma 5.2: Local Gauge-Invariant Records Preserve Boundary Centers

If a record or deformation is supported strictly inside `R` and is invariant
under `{\mathcal G}_R^{0}`, then it cannot distinguish or change boundary data
except through `\sigma_R`.

### Proof

Interior gauge transformations identify all representatives of the same
interior orbit while leaving the boundary label fixed. A strictly interior
gauge-invariant record is constant on those interior orbits. Since it has no
support on cut links or boundary vertices, it has no access to the complement
representatives. Its only possible shared label with the complement is the
center label `\sigma_R`. `square`

## 6. Finite Stochastic Kernels

Let the physical endpoint space decompose into finitely many declared global
gauge sectors:

```math
\Omega_K^{\rm phys}=\bigsqcup_{\alpha\in{\mathcal S}}\Omega_\alpha.
```

Here `\alpha` may encode total boundary charge, fixed external flux, or other
declared superselection data. The sector labels are part of the enriched
finite-gauge datum.

Choose real class functions `c_P,c_M:G\to{\mathbb R}`. For the `S_3`
benchmark one may take `c_P=c_M=\chi_{\rm std}`, the character of
`\rho_{\rm std}`. For couplings `\beta,\kappa\in{\mathbb R}`, define the
finite gauge action weight on raw configurations by

```math
W_{\beta,\kappa}(\omega)
=
\exp\left(
\beta\sum_{p\in P} c_P(U_p(\omega))
+
\kappa\sum_{e\in E}c_M(\psi_{t(e)}^{-1}U_e\psi_{s(e)})
\right).
```

### Lemma 6.1: Gauge-Action Weight Descends To The Physical Endpoint Space

The weight `W_{\beta,\kappa}` is constant on gauge orbits and therefore defines
a strictly positive weight on `\Omega_K^{\rm phys}`.

### Proof

Plaquette holonomies transform by conjugation, and `c_P` is a class function.
Matter-link terms are matter-dressed transporters of length one, hence
gauge-invariant by Lemma 4.1. The exponential is strictly positive and
therefore descends to the orbit space. `square`

For each sector define

```math
Z_\alpha(\beta,\kappa)
=
\sum_{\eta\in\Omega_\alpha} W_{\beta,\kappa}(\eta),
\qquad
\pi_\alpha(\eta)
=
\frac{W_{\beta,\kappa}(\eta)}{Z_\alpha(\beta,\kappa)}.
```

This is the finite gauge-action Gibbs endpoint law in sector `\alpha`.

Choose a parameter `0<\epsilon<1`. Define the full-rank reference kernel

```math
\Gamma_{0,\alpha}
=(1-\epsilon)I_\alpha+\epsilon\Pi_\alpha,
\qquad
(\Pi_\alpha)_{\eta\omega}=(\pi_\alpha)_\eta.
```

Then define

```math
\Gamma_0=\bigoplus_{\alpha\in{\mathcal S}}\Gamma_{0,\alpha}.
```

This is a finite column-stochastic kernel. It is invertible on every sector:
on the one-dimensional stationary direction its eigenvalue is `1`, and on the
zero-sum subspace its eigenvalue is `1-\epsilon`.

This lazy heat-bath kernel is a whole-endpoint reference kernel. It is not a
claim that the unobserved process is Markov-divisible in time.

### Lemma 6.2: Explicit Sectorwise Inverse

For each sector,

```math
\Gamma_{0,\alpha}^{-1}
=
(1-\epsilon)^{-1}(I_\alpha-\Pi_\alpha)+\Pi_\alpha.
```

### Proof

The projection `\Pi_\alpha` has range spanned by `\pi_\alpha` and satisfies
`\Pi_\alpha^2=\Pi_\alpha`. On this range,
`\Gamma_{0,\alpha}` acts as the identity. On the zero-sum subspace
`{\rm ker}\,\Pi_\alpha`, it acts as multiplication by `1-\epsilon`. Inverting
on the two invariant subspaces gives the displayed formula. `square`

### Theorem 6.3: Gauge-Action Reference Kernel

The kernel `\Gamma_0=\bigoplus_\alpha\Gamma_{0,\alpha}` is gauge-invariant,
sector preserving, full rank in every declared sector, column-stochastic, and
derived from the finite gauge action weight `W_{\beta,\kappa}`.

### Proof

Gauge invariance follows from Lemma 6.1. Sector preservation is built into the
direct sum over `\Omega_\alpha`. Column-stochasticity follows because each
column of `(1-\epsilon)I_\alpha+\epsilon\Pi_\alpha` sums to `1`. Full rank and
the inverse formula follow from Lemma 6.2. `square`

### Optional Transfer-Kernel Reference

The heat-bath endpoint kernel is the cleanest reference for inverse control.
One can also define a more dynamical two-endpoint reference without making the
unobserved process Markov-divisible.

In gauge-fixed physical variables, choose a class function `c_T:G\to{\mathbb R}`
and define

```math
S_{\rm tr}(\eta,\omega)
=
-\beta\sum_{p\in P}c_P(H_p(\eta))
-\kappa\sum_{e\in E}c_M(H_e(\eta))
-\tau\sum_{e\in E}c_T(H_e(\eta)H_e(\omega)^{-1}).
```

The column-normalized transfer kernel in sector `\alpha` is

```math
T_\alpha(\eta|\omega)
=
\frac{\exp(-S_{\rm tr}(\eta,\omega))}
{\sum_{\zeta\in\Omega_\alpha}\exp(-S_{\rm tr}(\zeta,\omega))}.
```

For `0<\epsilon<1/2`, define the lazy transfer reference

```math
\Gamma_{\rm tr,\alpha}
=
(1-\epsilon)I_\alpha+\epsilon T_\alpha.
```

### Theorem 6.4: Finite Transfer Reference Is Admissible

The lazy transfer reference `\Gamma_{\rm tr}=\bigoplus_\alpha
\Gamma_{\rm tr,\alpha}` is gauge-invariant, sector preserving,
column-stochastic, and invertible in every sector. Moreover,

```math
\|\Gamma_{\rm tr,\alpha}^{-1}\|_1\le (1-2\epsilon)^{-1}.
```

### Proof

The transfer action is written in terms of gauge-invariant dressed link and
plaquette variables, so it descends to `\Omega_K^{\rm phys}`. Positivity and
column normalization make `T_\alpha` column-stochastic with
`\|T_\alpha\|_1=1`. Since

```math
\Gamma_{\rm tr,\alpha}
=(1-\epsilon)
\left(I_\alpha+\frac{\epsilon}{1-\epsilon}T_\alpha\right),
```

and `\epsilon/(1-\epsilon)<1`, the inverse exists by the Neumann series

```math
\Gamma_{\rm tr,\alpha}^{-1}
=
(1-\epsilon)^{-1}
\left[
\sum_{n\ge0}
\left(-\frac{\epsilon}{1-\epsilon}T_\alpha\right)^n
\right]
```

Therefore

```math
\|\Gamma_{\rm tr,\alpha}^{-1}\|_1
\le
(1-\epsilon)^{-1}
\left[
\sum_{n\ge0}
\left(\frac{\epsilon}{1-\epsilon}\right)^n
\right]
=
(1-2\epsilon)^{-1}.
```

`square`

This optional reference kernel is still a whole-endpoint kernel. It is a
finite two-boundary kernel, not a composition law for unrecorded subprocesses.

### Definition 6.5: Gauge-Compatible Deformation

A regulated deformation `R` is gauge-compatible if its deformed kernel
`\Gamma_R` satisfies:

1. `\Gamma_R` is column-stochastic;
2. `\Gamma_R` commutes with the gauge action before passage to orbit space;
3. `\Gamma_R` preserves the declared global sector `\alpha`;
4. if localized in a region `R_0`, it changes no boundary-center label outside
   the collar of `R_0`;
5. in every sector, `\Gamma_R\Gamma_0^{-1}` is defined.

The comparison map is

```math
J_R=\Gamma_R\Gamma_0^{-1}.
```

For two deformations `R,S`, use the exchange convention

```math
E_{R,S}=J_S^{-1}J_R^{-1}J_SJ_R.
```

## 7. Exact Sectorwise Gauge Theorem

### Theorem 7.1: Sectorwise Non-Abelian Gauge Kernel Decomposition

Let `\Gamma_0` be the reference kernel above and let `\Gamma_R` be any
gauge-compatible deformation. Then:

1. `\Gamma_0` and `\Gamma_R` decompose as direct sums over declared gauge
   sectors:
   ```math
   \Gamma_0=\bigoplus_\alpha\Gamma_{0,\alpha},
   \qquad
   \Gamma_R=\bigoplus_\alpha\Gamma_{R,\alpha}.
   ```
2. The comparison map is sectorwise:
   ```math
   J_R=\bigoplus_\alpha J_{R,\alpha},
   \qquad
   J_{R,\alpha}=\Gamma_{R,\alpha}\Gamma_{0,\alpha}^{-1}.
   ```
3. The exchange defect is sectorwise:
   ```math
   E_{R,S}=\bigoplus_\alpha E_{R,S;\alpha}.
   ```
4. If `R` is localized in `R_0`, then `J_R` is invisible outside the collar of
   `R_0` except through the boundary center label `\sigma_{R_0}`.

### Proof

Gauge compatibility requires both `\Gamma_0` and `\Gamma_R` to preserve the
declared sector `\alpha`; hence the first direct-sum decomposition holds.
Because `\Gamma_{0,\alpha}` is invertible in each finite sector, multiplication
by `\Gamma_0^{-1}` preserves the same direct sum, proving the second statement.
The exchange defect is built from products and inverses of the sectorwise
comparison maps, so it is sectorwise as well. The localization statement is
Lemma 5.2 applied to the support collar of the deformation. `square`

### Corollary 7.2: No Hidden Gauge Factorization

The local finite gauge ISP net factors over separated regions only after
conditioning on the relevant boundary center labels. Without those labels, the
inside and outside algebras share a center and the tensor-factorization claim
is false.

### Proof

Theorem 7.1 shows that local comparison maps are local only modulo
`\sigma_R`. If two local algebras share a boundary-center variable, they cannot
be represented as independent tensor factors without either duplicating or
forgetting that variable. Conditioning on the center removes the shared
classical label. `square`

### Theorem 7.3: Explicit Center-Conditioned Gluing

Let `R` be a finite region and `R^c` its complement. Let `{\mathcal A}_R` and
`{\mathcal A}_{R^c}` be the finite scalar physical record algebras generated by
gauge-invariant endpoint records supported in the two regions, including their
shared boundary-center algebra

```math
{\mathcal Z}_{\partial R}
=
{\mathbb C}[\sigma_R].
```

Let `z` range over the atoms of `{\mathcal Z}_{\partial R}`. Define the finite
center fibers

```math
X_R(z)=\{\xi_R:\sigma_R(\xi_R)=z\},
\qquad
X_{R^c}(z)=\{\xi_{R^c}:\sigma_R(\xi_{R^c})=z\}.
```

The compatible regional endpoint set is the finite fiber product

```math
X_R\times_{\partial R}X_{R^c}
=
\bigsqcup_z X_R(z)\times X_{R^c}(z).
```

The algebra generated by the two regional physical record algebras is the
center-fibered sum

```math
{\mathcal A}_R\vee{\mathcal A}_{R^c}
\cong
\bigoplus_z
{\mathcal A}_R(z)\otimes{\mathcal A}_{R^c}(z),
```

where `{\mathcal A}_R(z)` and `{\mathcal A}_{R^c}(z)` are the conditioned
finite algebras at fixed boundary-center label `z`.

An explicit isomorphism is:

```math
\Theta(F)
=
\left(
F|_{X_R(z)\times X_{R^c}(z)}
\right)_z,
```

for every finite function `F` on the compatible endpoint set.

In particular, the unconditioned algebra is a plain tensor product
`{\mathcal A}_R\otimes{\mathcal A}_{R^c}` only when the boundary center is
trivial or has been fixed.

### Proof

A physical configuration on `K` restricts to a pair of regional physical
configurations whose boundary labels agree. Conversely, a compatible pair of
regional physical configurations with the same center label glues to a global
physical configuration up to the interior gauge actions already quotiented in
the regional algebras. Thus the finite physical endpoint set is the disjoint
union over center labels `z` of compatible products. Functions on a finite
disjoint union are direct sums of function algebras, and functions on each
finite product are tensor products:

```math
{\rm Fun}(X_R(z)\times X_{R^c}(z))
\cong
{\rm Fun}(X_R(z))\otimes{\rm Fun}(X_{R^c}(z)).
```

The restriction map `\Theta` is therefore a finite-dimensional algebra
isomorphism. If more than one center atom is present, forgetting `z` identifies
a shared classical variable and cannot be an ordinary tensor factorization.
`square`

### Charged-Channel Gluing

Declared charged instruments obey the same center rule, but with representation
blocks rather than only scalar functions. A charged line crossing the boundary
must carry a declared boundary representation/intertwiner label. Therefore
charged gluing is also center-conditioned:

```text
fix the boundary center and representation label first;
then compose charged regional blocks.
```

Without that declared label the charged channel is not an observable local
tensor factor. It is an enriched operational probe.

## 8. Local Deformations And Comparison Maps

The finite benchmark uses three elementary deformations.

### 8.1 Plaquette Scalar Deformation

For a plaquette `p` and class function `c:G\to{\mathbb R}`, define a small
tilt

```math
\Gamma_{p,\lambda}(\eta|\omega)
=
\frac{
\exp(\lambda c(U_p(\eta)))\Gamma_0(\eta|\omega)
}{
\sum_{\eta'}\exp(\lambda c(U_p(\eta')))\Gamma_0(\eta'|\omega)
}.
```

This is gauge-compatible and localized at `p`.

### 8.2 Matter-Link Scalar Deformation

For an edge `e:x\to y` and class function `c`, define the hopping record

```math
H_e(\omega)=\psi_y^{-1}U_e\psi_x.
```

The tilt by `c(H_e)` is gauge-compatible and localized at `e`.

### 8.3 Charged Transport Deformation

Fix a representation `\rho:G\to GL(V_\rho)`, endpoint vectors
`\ell\in V_\rho^*`, `r\in V_\rho`, and a path `\gamma:x\to y`. The charged
record is

```math
W_{\gamma,\rho,\ell,r}(\omega)
=
\ell\bigl(\rho(T_\gamma(\omega))r\bigr).
```

A charged transport deformation is an instrument-labelled source/sink probe
whose first variation acts on the charged transport channel by insertion of a
declared representation matrix along the path. This is an operational
enrichment, not a Gamma-only scalar observable.

### Definition 8.1: Elementary Charged Insertion

Let a path split as `\gamma=\gamma_2 e\gamma_1`, where `e` is the segment at
which an instrument inserts `a\in G`. On the charged transport channel define
the elementary insertion operator `Q_{\gamma,e,a}^{\rho}` by

```math
Q_{\gamma,e,a}^{\rho}:
\ell\rho(T_{\gamma_2})\rho(T_e)\rho(T_{\gamma_1})r
\mapsto
\ell\rho(T_{\gamma_2})\rho(a)\rho(T_e)\rho(T_{\gamma_1})r.
```

This is a finite-rank operational insertion on the declared charged channel.
If two insertions `a,b` occur at the same oriented segment, then

```math
[Q_{\gamma,e,b}^{\rho},Q_{\gamma,e,a}^{\rho}]
```

acts on the inserted factor by

```math
\rho(b)\rho(a)-\rho(a)\rho(b).
```

If the insertions occur on disjoint segments, the corresponding finite-rank
operators commute.

### Definition 8.2: Finite Charged Instrument

Fix a path segment `e` in `\gamma`, an insertion label `a\in G`, a
representation `\rho`, and a small record probability `0<q<1`. The charged
instrument is the pair

```math
{\mathcal I}_{\gamma,e,a}^{\rho}
=
({\mathsf K}_{\gamma,e,a},{\mathsf Q}_{\gamma,e,a}^{\rho}).
```

The stochastic record kernel acts on the extended endpoint space

```math
\widetilde\Omega=\Omega_K^{\rm phys}\times\{\varnothing,a\}
```

by

```math
{\mathsf K}_{\gamma,e,a}((\eta,a)|(\omega,\varnothing))
=
q\,\Gamma_0(\eta|\omega),
```

```math
{\mathsf K}_{\gamma,e,a}((\eta,\varnothing)|(\omega,\varnothing))
=
(1-q)\,\Gamma_0(\eta|\omega),
```

with the obvious identity action on already recorded labels. The charged
readout map is

```math
{\mathsf Q}_{\gamma,e,a}^{\rho}=Q_{\gamma,e,a}^{\rho}.
```

Thus the instrument has a positive stochastic record part and a typed charged
readout part. The matrix-valued insertion is not a probability kernel.

### Lemma 8.3: Charged Instruments Are Finite Gauge-Compatible Instruments

The instrument `{\mathcal I}_{\gamma,e,a}^{\rho}` is a finite
gauge-compatible instrument. Its stochastic record kernel is column-stochastic,
preserves gauge sectors, and is localized at the declared segment/path label.
Its charged readout is an enriched operational channel.

### Proof

For each initial endpoint `\omega`,

```math
\sum_{\eta}
{\mathsf K}_{\gamma,e,a}((\eta,a)|(\omega,\varnothing))
+
\sum_{\eta}
{\mathsf K}_{\gamma,e,a}((\eta,\varnothing)|(\omega,\varnothing))
=q+(1-q)=1,
```

because `\Gamma_0` is column-stochastic. Sector preservation and gauge
compatibility follow from `\Gamma_0`; the additional label `a` is an instrument
record, not a gauge configuration variable. The charged readout map is the
declared finite-rank map of Definition 8.1. `square`

### Lemma 8.4: The Three Deformations Are Gauge-Compatible

The plaquette scalar, matter-link scalar, and charged transport deformations
above are gauge-compatible whenever their endpoint source/sink labels are
declared as part of the instrument.

### Proof

Plaquette holonomies transform by conjugation, so class functions of them are
gauge-invariant. Matter-link records are the length-one case of Lemma 4.1.
Charged transport records are gauge-invariant after endpoint source/sink
contraction because `T_\gamma` is gauge-invariant. Scalar deformations are
column-normalized finite tilts. Charged deformations are the finite instruments
of Definition 8.2 and Lemma 8.3. Sector preservation and collar localization
are imposed in Definition 6.5 and are immediate for these local supports.
`square`

## 9. First Non-Abelian Mixed Exchange Coefficient

Let two small deformations have expansions in a fixed sector:

```math
\Gamma_R(\lambda)=\Gamma_0+\lambda D_R+O(\lambda^2),
\qquad
\Gamma_S(\mu)=\Gamma_0+\mu D_S+O(\mu^2),
```

with column sums zero for `D_R,D_S`. Then

```math
J_R(\lambda)=I+\lambda A_R+O(\lambda^2),
\qquad
J_S(\mu)=I+\mu A_S+O(\mu^2),
```

where

```math
A_R=D_R\Gamma_0^{-1},
\qquad
A_S=D_S\Gamma_0^{-1}.
```

For the convention `E_{R,S}=J_S^{-1}J_R^{-1}J_SJ_R`,

```math
E_{R,S}(\lambda,\mu)
=
I+\lambda\mu[A_S,A_R]+O(\lambda^2\mu+\lambda\mu^2).
```

Thus the first mixed exchange coefficient is

```math
C_{R,S}=[A_S,A_R].
```

### Theorem 9.1: Non-Abelian Coefficient Onset

For scalar class-function plaquette and matter-link deformations, the
non-Abelian representation-commutator component of `C_{R,S}` is zero. Such
probes can see sector weights and boundary centers, but not the oriented
matrix-ordering obstruction by themselves.

For charged transport deformations in representation `\rho`, if two probes
share an oriented link segment and insert group elements `a,b\in G` in opposite
orders, the charged-channel projection of the first mixed coefficient contains

```math
\rho(b)\rho(a)-\rho(a)\rho(b).
```

Consequently, for `G=S_3`, `a=r`, `b=s`, and
`\rho=\rho_{\rm std}`,

```math
\rho_{\rm std}(s)\rho_{\rm std}(r)
-
\rho_{\rm std}(r)\rho_{\rm std}(s)
=
-
\begin{pmatrix}
0&\sqrt{3}\\
\sqrt{3}&0
\end{pmatrix}
\ne 0.
```

Therefore the finite benchmark has a genuinely non-Abelian exchange-curvature
channel.

### Proof

The expansion of `E_{R,S}` gives the general coefficient
`C_{R,S}=[A_S,A_R]`. Scalar class-function deformations act through central
gauge-invariant functions. Their scalar multiplication part has no oriented
representation order, so its projection onto the charged representation
commutator channel is zero.

A charged transport probe, however, carries a declared representation channel.
By Definition 8.1, when two such probes share an oriented segment, the two
orders of insertion place the matrices along the same representation line in
opposite order. The coefficient projected to that charged line is therefore the
difference between the two ordered products, namely

```math
\rho(b)\rho(a)-\rho(a)\rho(b).
```

For `S_3` in the standard representation, the displayed matrix computation is
nonzero. `square`

### Theorem 9.2: Scalar Class-Function Probes Cannot Fake Non-Abelian Curvature

Let `{\mathcal C}(G)` be the algebra of class functions on a finite group
`G`. Any finite benchmark that uses only scalar records built from class
functions of plaquette holonomies and matter-dressed transporters is blind to
the oriented matrix-ordering commutator

```math
\rho(b)\rho(a)-\rho(a)\rho(b).
```

More precisely, for all `a,b\in G` and all `c\in{\mathcal C}(G)`,

```math
c(ab)=c(ba).
```

Therefore scalar class-function probes may detect non-Abelian conjugacy-class
statistics, but they cannot detect the charged-channel commutator onset of
Theorem 9.1.

### Proof

The products `ab` and `ba` are conjugate because

```math
ab=a(ba)a^{-1}.
```

Every class function is constant on conjugacy classes, hence `c(ab)=c(ba)`.
Also, scalar endpoint records act as multiplication operators on finite
functions of endpoints, and such multiplication operators commute. Thus the
scalar class-function algebra has no ordered representation line on which a
matrix commutator could act. Nonzero ordered commutators require a declared
charged representation channel. `square`

### Example 9.3: One-Plaquette `S_3` Coefficient

Use the square one-plaquette lattice of Section 3 and the charged path
`\gamma=e_{01}`. Work in the standard representation. Let the charged channel
be tested by

```math
\ell=e_1^*,
\qquad
r=e_2,
```

and choose two elementary insertions on the same oriented link:

```math
A_R=Q_{\gamma,e_{01},r}^{\rho_{\rm std}},
\qquad
A_S=Q_{\gamma,e_{01},s}^{\rho_{\rm std}}.
```

The first mixed coefficient in the charged channel is

```math
C_{R,S}=[A_S,A_R].
```

Its measured scalar matrix element is

```math
\ell C_{R,S} r
=
e_1^*
\left(
\rho_{\rm std}(s)\rho_{\rm std}(r)
-
\rho_{\rm std}(r)\rho_{\rm std}(s)
\right)
e_2
=
-\sqrt{3}.
```

Thus the smallest explicit benchmark has:

1. a plaquette scalar channel `c_P(U_p)`;
2. a matter-link scalar channel `c_M(T_{e_{01}})`;
3. a charged transport channel on `e_{01}`;
4. a nonzero non-Abelian mixed coefficient in that charged channel.

The sign depends on the exchange convention and insertion order. The invariant
fact for the benchmark is nonzero onset, here with magnitude `\sqrt{3}`.

### Corollary 9.4: Separated-Support Onset Bound

In the strictly local finite benchmark, if the collars of `R` and `S` are
disjoint and share no boundary-center label, then

```math
C_{R,S}=0.
```

If a later leaky/reference-kernel version is used with exponential leakage
scale `m>0`, the expected replacement bound is

```math
\|C_{R,S}\|\le C_0\|A_R\|\|A_S\|\exp(-m\,d(R,S)).
```

The first statement is proved here; the second is a Paper-10 refinement target.

### Proof

With disjoint collars and no shared boundary center, the two first-variation
operators act on independent finite factors after conditioning on centers, so
they commute. Hence `[A_S,A_R]=0`. The exponential bound requires additional
analytic assumptions on leakage and is not claimed in this finite exact paper.
`square`

## 10. Paper-9 Pass Theorem

### Theorem 10.1: Finite Non-Abelian Gauge ISP Benchmark

The `S_3` construction above gives an exact finite non-Abelian ISP gauge
benchmark with:

1. a finite physical endpoint space;
2. declared Gauss/gauge sectors;
3. boundary center labels for regions;
4. gauge-action-derived full-rank sectorwise reference kernels;
5. an optional admissible finite transfer-kernel reference;
6. gauge-compatible localized deformations;
7. finite charged instruments with positive stochastic record kernels;
8. sectorwise comparison maps;
9. sectorwise exchange defects;
10. center-conditioned gluing of local physical record algebras;
11. a theorem showing scalar class-function probes cannot fake charged
   non-Abelian curvature;
12. a nonzero first non-Abelian mixed exchange coefficient in charged transport
   channels.

### Proof

Items 1-3 are Sections 3-5 and Definition 5.1. Item 4 is Theorem 6.3. Item 5
is Theorem 6.4. Items 6-9 are Lemmas 8.3-8.4 and Theorem 7.1. Item 10 is
Theorem 7.3. Item 11 is Theorem 9.2. Item 12 is Theorem 9.1 and Example 9.3.
`square`

## 11. What Is Gamma-Level And What Is Enriched?

Gamma-level:

1. finite endpoint orbit spaces;
2. sectorwise stochastic kernels;
3. sectorwise comparison maps;
4. exchange defects after deformations are declared.

Enriched/declared:

1. the choice of finite gauge group `S_3`;
2. the gauge action and sector labels;
3. local instruments and charged source/sink probes;
4. representation labels such as `\rho_{\rm std}`;
5. boundary-center bookkeeping for local regions.

Not claimed:

```text
Gamma-only gauge-field reconstruction;
continuum Yang-Mills;
Peter-Weyl refinement;
full non-Abelian QFT;
exact finite-regulator Lorentz covariance.
```

This is exactly the Barandes-aligned separation: the stochastic endpoint layer
is real, but the representational and operational gauge probes must be typed.

## 12. Wilson And No-Wilson Gauge Coupling Fork

Paper 9 is gauge-sector finite and regulator-neutral. It is not itself the
Wilson fermion route, and it is not itself the no-Wilson detail-preserving
fermion route. It is the finite gauge layer that both routes may couple to.

### Wilson-Gauge Continuation

The Wilson-facing continuation declares:

1. Wilson fermion variables or Wilson-compatible matter fields;
2. gauge-covariant Wilson hopping terms;
3. a Wilson term that removes unwanted lattice tastes in the chosen continuum
   target;
4. charged instruments compatible with the Wilson single-species test class;
5. projective/refinement maps that preserve Gauss sectors and the Wilson
   admissible finite-energy sector.

This is the conservative standard-QFT-facing route. Its target is
single-species gauge-coupled QFT matching on controlled finite batteries.

### Finite Wilson-Gauge Block

Let `V_\rho` be a declared charged representation space. A finite Wilson-gauge
matter vector is a function

```math
\varphi:V\to{\mathbb C}^{d_{\rm spin}}\otimes V_\rho.
```

For an edge `e:x\to y`, define gauge-covariant transport by

```math
({\mathcal U}_e\varphi)_y
=
(I_{\rm spin}\otimes\rho(U_e))\varphi_x.
```

A finite Wilson hopping/Wilson-term block is any finite matrix built from
linear combinations of edge transports, their adjoints, a mass term, and
gauge-covariant edge differences

```math
L_e\varphi
=
\varphi_{t(e)}
-
(I_{\rm spin}\otimes\rho(U_e))\varphi_{s(e)}.
```

Wilson-laplacian terms are finite sums of `L_e^*L_e`, with the orientation
adjusted to the chosen edge convention.

### Lemma 12.1: Wilson-Gauge Block Is Gauge-Covariant

Under the gauge action

```math
\varphi_v\mapsto (I_{\rm spin}\otimes\rho(h_v))\varphi_v,
\qquad
U_e\mapsto h_{t(e)}U_eh_{s(e)}^{-1},
```

each finite Wilson-gauge block transforms by conjugation on the finite matter
space. Therefore its declared traces, determinants on finite cutoffs, and
instrument matrix elements with covariantly transformed sources are
gauge-compatible records.

### Proof

For `e:x\to y`,

```math
\rho(h_yU_eh_x^{-1})\rho(h_x)\varphi_x
=
\rho(h_y)\rho(U_e)\varphi_x.
```

Thus edge transport intertwines the sitewise gauge action. Finite sums,
adjoints, mass terms, and Wilson-laplacian terms inherit covariance. Gauge
invariant finite records are obtained by traces/determinants or by transforming
the external sources covariantly. `square`

### No-Wilson Detail-Preserving Gauge Continuation

The no-Wilson continuation declares:

1. detail/taste sectors as real recorded structure;
2. gauge-covariant staggered or detail-preserving hopping;
3. charged transport probes carrying taste/detail labels;
4. boundary centers and taste centers as distinct typed labels;
5. no silent projection to a single species.

This is the more Barandes-like route in ontology: it refuses to erase detail
records unless an instrument explicitly records the erasure, quotient, or
selection. Its target is a multi-taste gauge-coupled QFT, a selected-taste
recorded channel, or a genuine retained-record ISP extension.

### Finite No-Wilson Detail-Preserving Gauge Block

Let `T` be a finite detail/taste label set. A detail-preserving charged matter
field is

```math
\chi:V\times T\to V_\rho.
```

For each taste/detail label `t\in T`, define gauge-covariant hopping by

```math
({\mathcal D}_{e,t}\chi)_{t(e),t}
=
\rho(U_e)\chi_{s(e),t},
```

and keep the label `t` as an explicit record. No Wilson projection, taste
averaging, or hidden quotient is allowed unless represented by a declared
instrument outcome.

### Lemma 12.2: Detail-Preserving Gauge Block Is Gauge-Covariant And
Record-Preserving

The no-Wilson detail-preserving gauge block is gauge-covariant and preserves
the declared taste/detail label. Consequently it is compatible with the finite
non-Abelian gauge layer, but its target is a multi-taste, selected-taste, or
retained-record theory rather than hidden single-species QFT.

### Proof

Gauge covariance is the same edge-transport identity used in Lemma 12.1. The
operator acts diagonally on the declared label `t` unless an explicit
instrument changes that label. Therefore the label remains part of the
operational record. Erasing it would be an additional quotient or selection
instrument, not a consequence of the gauge kernel. `square`

### Theorem 12.3: Finite Gauge Layer Supports Both Branches

The finite `S_3` gauge-sector ISP benchmark can be coupled to either the finite
Wilson-gauge block of Lemma 12.1 or the finite no-Wilson detail-preserving
block of Lemma 12.2. In both cases Gauss sectors, boundary centers, and charged
transport instruments remain typed finite data. Neither coupling proves a
fermion continuum limit.

### Proof

Both blocks use the same finite gauge-covariant edge transport
`\rho(U_e)`. Therefore both preserve the gauge action and can be restricted to
the sectorwise endpoint architecture of Sections 5-7. The Wilson block adds a
declared Wilson regulator; the no-Wilson block keeps detail labels as records.
Those are different branch enrichments over the same finite gauge layer.
Continuum claims require projective/refinement theorems not present in this
finite benchmark. `square`

### Fork Rule

The finite non-Abelian gauge benchmark may be imported into both branches, but
neither branch may quote Paper 9 as proving its fermion continuum limit.

```text
Paper 9 proves finite non-Abelian gauge-sector ISP.
Wilson/non-Wilson fermion continuum claims require additional branch theorems.
```

## 13. Export To Paper 10

Paper 10 may import:

1. the finite `S_3` gauge-sector ontology;
2. the sectorwise comparison-map theorem;
3. boundary-center conditioning;
4. the charged-channel non-Abelian coefficient formula;
5. the exact separated-support onset result;
6. the Wilson/no-Wilson gauge-coupling fork rule;
7. the finite gauge-sector source ledger and no-smuggling theorem of Section
   2A.

Paper 10 must add:

1. representation-cutoff maps, for example finite groups to Peter-Weyl or
   `SU(2)` quantum-link cutoffs;
2. preservation of Gauss sectors under refinement;
3. preservation or controlled flow of boundary centers;
4. inverse-control bounds uniform in the cutoff;
5. a continuum-facing field-strength or covariant-derivative target.

### Theorem 13.1: Paper-10 Export Contract

Paper 10 may use exactly the following theorem-level objects from Paper 9:

1. the finite orbit-space model and the one-plaquette `S_3^4` endpoint
   representative;
2. the gauge-action-derived lazy heat-bath reference kernel and its explicit
   inverse;
3. the optional lazy transfer reference and inverse bound;
4. sectorwise comparison maps and exchange defects;
5. center-conditioned gluing;
6. finite charged instruments and their representation-channel insertions;
7. scalar-probe no-faking;
8. the explicit nonzero charged-channel coefficient in the one-plaquette
   model;
9. the finite Wilson/no-Wilson gauge-coupling fork;
10. the finite gauge-sector source ledger of Definition 2A.1 and the
    no-smuggling theorem 2A.3.

Paper 10 may not use Paper 9 as proof of:

```text
continuum Yang-Mills;
SU(2) or SU(3) continuum gauge theory;
fermion continuum limits;
renormalization;
Wilson-loop area law;
mass gap;
confinement;
Gamma-only gauge-field reconstruction;
exact finite-regulator Lorentz covariance.
```

### Proof

Items 1-10 are precisely the proved finite results of Sections 2A-12. Every
forbidden claim requires a representation-cutoff/refinement limit, continuum
limit, renormalization theorem, or enriched representation reconstruction not
proved in this finite benchmark. Therefore Paper 10 may import the finite
objects but must prove the continuum/projective upgrades itself. `square`

### Corollary 13.2: Consequence For Papers 11-20

Papers 11-20 may cite Paper 9 for finite gauge-sector bookkeeping: Gauss
sectors, boundary centers, finite charged instruments, finite comparison maps,
and the finite non-Abelian exchange witness. They may not cite Paper 9 as a
source for continuum `4D SU(N)` existence, continuum Wilson-loop laws,
confinement, a mass gap, or the Paper-20 `SEL2` tree-rate gate. Those are
later analytic/projective source problems.

## 14. Status

This paper proves a finite non-Abelian gauge ISP benchmark.

It does not prove continuum non-Abelian gauge theory.

The honest status is:

```text
finite non-Abelian ISP: yes;
sectorwise Gauss/boundary-center control: yes;
localized comparison maps: yes;
first non-Abelian exchange coefficient: yes, in charged channels;
continuum Yang-Mills: not yet;
area law / mass gap / confinement: not supplied by this paper.
```
