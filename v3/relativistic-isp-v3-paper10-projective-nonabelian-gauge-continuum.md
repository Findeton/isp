# Relativistic ISP V3 Paper 10: Projective Non-Abelian Gauge Cutoffs

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: theorem-level projective-cutoff draft. This paper is the bridge from
the finite `S_3` gauge benchmark of V3 Paper 9 to continuum-facing non-Abelian
gauge data. It does not prove continuum Yang-Mills. It proves that a declared
`SU(2)` Peter-Weyl finite-battery cutoff can preserve Gauss sectors, boundary
centers, reference-kernel inverse control, comparison-map compatibility, and a
field-strength target for charged exchange coefficients under explicit
hypotheses. It also adds a finite-battery Yang-Mills target, a standard-facing
finite Wilson gauge-matter target, exact finite-battery perfect blocking, an
exact two-dimensional heat-kernel blocking theorem, a finite-battery
local-projection theorem for four-dimensional local RG tests, and a Gamma-only
gauge reconstruction no-go.

After the Paper 8 and Paper 9 audits, the boundary is sharper: Paper 10 defines
the right typed records for a projective gauge tower and proves exact
finite-battery pushforward identities when the coarse record law is defined as
the pushforward of the fine law. It does not, by itself, prove an unconditional
cofinal same-record continuum tower. That stronger object still requires the
named projective compatibility, local-action, tightness, uniqueness, and
continuum scaling gates below.

The central ontology is:

```text
finite S_3 Paper 9:
  finite endpoint space;

SU(2) Peter-Weyl Paper 10:
  compact endpoint space with finite declared observable/effect batteries.
```

That distinction matters. A Peter-Weyl cutoff is not a finite hidden state
space. It is a finite representation battery over a compact gauge endpoint
space. This is the Barandes-aligned route: do not replace the whole stochastic
process by an undeclared Markov sub-process, and do not treat representation
data as if bare Gamma had already reconstructed it.

## 1. Main Question

Can the finite non-Abelian benchmark of Paper 9 survive representation-cutoff
and lattice refinement strongly enough to support continuum-facing gauge data?

The answer of this paper is:

1. **Yes for Peter-Weyl finite batteries.** `SU(2)` gauge variables on links
   admit finite declared representation batteries indexed by a spin cutoff
   `J`.
2. **Yes for Gauss and boundary centers.** The gauge-invariant finite battery
   decomposes by boundary representation labels and intertwiners, and the
   cutoff projections preserve those labels below cutoff.
3. **Yes for reference-kernel inverse control.** A parent gauge-action
   heat-bath reference restricted to finite batteries has an explicit inverse
   bound.
4. **Conditionally yes for comparison maps.** Projective comparison-map
   compatibility follows from a stated primitive-kernel compatibility estimate.
5. **Yes for the smooth-background curvature target.** Charged plaquette
   transport has the usual non-Abelian field-strength limit by the
   Baker-Campbell-Hausdorff expansion.
6. **Partly for renormalization.** Exact heat-kernel blocking is proved in the
   safe two-dimensional plaquette setting. Exact finite-battery perfect
   blocking works in any dimension, but is generally nonlocal; replacing it by
   a local Wilson/heat-kernel ansatz remains a named residual gate.
7. **No for Gamma-only gauge reconstruction.** Scalar Gamma gauge data cannot
   reconstruct charged parallel transport or the full non-Abelian connection.
8. **No for full Yang-Mills.** Continuum measure construction, mass gap,
   BRST/OS/Wightman reconstruction, QCD, and full QFT are not proved here.

## 2. Import Contract From Paper 9

Paper 10 imports:

1. finite non-Abelian gauge-sector discipline;
2. boundary-center conditioning;
3. sectorwise comparison maps;
4. finite charged instruments;
5. scalar-probe no-faking;
6. nonzero charged-channel commutator onset;
7. the Wilson/no-Wilson gauge-coupling fork.

It does not import:

```text
continuum Yang-Mills;
SU(2) continuum gauge theory;
fermion continuum limits;
renormalization;
Gamma-only gauge-field reconstruction;
exact finite-regulator Lorentz covariance;
Wilson-loop area law;
mass gap;
confinement;
an unconditional same-record whole-process tower;
projective tightness or uniqueness;
the Paper-20 SEL2 tree-rate/source gate.
```

## 2A. Projective Continuum Audit

This audit answers a narrow question needed by Papers 11-20:

```text
Does Paper 10 construct the same-record pushforward tower itself,
or only a conditional tower once compatibility and tightness are supplied?
```

The answer is conditional. Paper 10 supplies the finite records, finite
pushforward maps, and exact one-step perfect-block identity. It does not prove
the cofinal continuum tower without extra gates.

### Definition 2A.1: Same-Record Projective Pushforward Tower

A same-record projective pushforward tower for a declared gauge observable
class consists of the following data.

1. A directed cutoff/refinement index set `\alpha=(K_\alpha,J_\alpha,V_\alpha)`,
   where `K_\alpha` is a finite lattice, `J_\alpha` is a Peter-Weyl cutoff,
   and `V_\alpha` is the finite volume.
2. A finite typed record battery `{\mathcal F}_\alpha` at each index, with
   stable record names: scalar loops, charged source/sink records,
   boundary-center labels, and any Wilson/no-Wilson branch data are declared
   before transport.
3. Gauge-covariant record maps
   ```math
   B_{\alpha,\beta}:G^{E_\alpha}\to G^{E_\beta},
   \qquad \alpha\succ\beta,
   ```
   and pullbacks `B_{\alpha,\beta}^*{\mathcal F}_\beta\subseteq
   {\mathcal F}_\alpha` up to the declared projection residuals.
4. Finite record laws `\omega_\alpha` on `{\mathcal F}_\alpha`.
5. A pushforward estimate
   ```math
   \sup_{\|F\|_{{\mathcal F}_\beta}\le1}
   \left|
   \omega_\alpha(F\circ B_{\alpha,\beta})
   -
   \omega_\beta(F)
   \right|
   \le \epsilon_{\alpha,\beta},
   ```
   with `\epsilon_{\alpha,\beta}\to0` along the chosen cofinal refinement
   path.
6. A cocycle estimate
   ```math
   B_{\alpha,\gamma}
   =
   B_{\beta,\gamma}\circ B_{\alpha,\beta}
   ```
   on the tested records, again up to a residual tending to zero.
7. Tightness or compactness for the induced continuum record distributions,
   plus uniqueness or a declared subsequential choice of limit.

The word "same-record" is doing real work. The record at coarse scale must be
the same operational record as the pushed-forward fine record, not merely a
similarly named observable in a different scheme. Charged frames, center
labels, endpoint/collar conventions, and branch labels must therefore be part
of the typed record, not silent background structure.

### Definition 2A.2: Paper-10 Projective Source Gates

The source gates for Definition 2A.1 are:

```text
P10-PC:       battery projectivity and cocycle residuals;
P10-KCOMP:    primitive kernel compatibility;
P10-INVCOMP: reference inverse compatibility;
P10-RGD:      higher-dimensional local RG compatibility, or
              an explicit perfect-block replacement;
P10-LOCRG:    vanishing local-action residual if a local Wilson/heat-kernel
              ansatz is used instead of the perfect block;
P10-YMLIM:    continuum scaling convergence and OS-type conditions;
P10-TIGHT:    tightness/compactness of the induced continuum record laws;
P10-UNIQ:     uniqueness of the limit, or a declared subsequential branch;
P10-SAMEREC:  no change of record convention under projection or blocking.
```

Only finite-dimensional parts of this list are proved unconditionally in this
paper. The continuum gates are named hypotheses or later-paper obligations.

### Lemma 2A.3: Perfect Blocking Is Exact But Not A Continuum Tower

The perfect block of Definition 10.4 gives an exact one-step same-record
pushforward identity on a fixed finite coarse battery. It does not by itself
prove a cofinal continuum same-record tower.

### Proof

For a fixed pair `\alpha\succ\beta`, Theorem 10.5 defines

```math
\omega_\beta^{\rm perf}(F)
=
\omega_\alpha(F\circ B_{\alpha,\beta}).
```

Therefore the one-step residual is zero by definition. This is a genuine
finite-record pushforward identity and is useful: no undeclared Markov process
or local action has been smuggled in.

However, the identity is attached to the chosen fine law, block map, and finite
coarse battery. It does not prove that a local ansatz represents the perfect
law, that different refinement paths give the same law, that the cocycle errors
vanish on cofinal batteries, that the resulting continuum record distributions
are tight, or that the continuum limit is unique. Those are exactly the gates
listed in Definition 2A.2. `square`

### Theorem 2A.4: Projective Continuum Audit Verdict

Paper 10 gives the right finite/projective language for a same-record
pushforward tower, but it proves only a conditional projective continuum tower.
The unconditional exports are finite-battery records, Gauss/boundary-center
stability, finite inverse control, exact one-step perfect-block pushforward,
and exact two-dimensional heat-kernel blocking. The continuum same-record tower
is available only after `P10-PC`, `P10-KCOMP`, `P10-INVCOMP`,
`P10-RGD` or a perfect-block replacement, `P10-LOCRG` when a local ansatz is
used, `P10-YMLIM`, `P10-TIGHT`, `P10-UNIQ`, and `P10-SAMEREC` are supplied.

### Proof

Sections 3-4 build finite Peter-Weyl gauge batteries and Gauss-invariant
sectors. Sections 5-7 prove transport only under `PC` and `KCOMP` plus inverse
compatibility. Section 9 explicitly declares `YM-LIM` as an unproved continuum
gate. Section 10 proves exact perfect blocking on a finite battery, but
Corollary 10.6 identifies the local-action residual as the real
higher-dimensional gate. None of these results supplies tightness, uniqueness,
or an unconditional local continuum Yang-Mills law. Therefore the projective
continuum tower is a conditional construction, not an unconditional theorem.
`square`

### Corollary 2A.5: Consequence For Papers 11-20

Later papers may cite Paper 10 for:

```text
finite Peter-Weyl gauge batteries;
finite same-record bookkeeping;
Gauss-sector and boundary-center stability;
finite reference inverse control;
conditional comparison-map transfer;
exact finite perfect-block pushforward;
exact 2D heat-kernel blocking;
the named higher-dimensional local-action residual gate.
```

Later papers may not cite Paper 10 for:

```text
unconditional continuum Yang-Mills measure existence;
unconditional same-record whole-process tower;
continuum Lorentz/AQFT reconstruction;
Wilson-loop area law;
mass gap;
confinement;
the Paper-20 SEL2 tree-rate/source gate.
```

## 3. Regulator Choice

The primary route is the `SU(2)` Peter-Weyl finite-battery route.

Let

```math
G=SU(2).
```

For each half-integer cutoff

```math
J\in\{0,1/2,1,3/2,\ldots\},
```

let `{\widehat G}_{\le J}` be the set of irreducible `SU(2)`
representations with spin `j\le J`. Let `V_j` be the spin-`j` representation
space, with `d_j=2j+1`.

The Peter-Weyl matrix-coefficient space on one link is

```math
{\mathcal C}_J(G)
=
{\rm span}
\{
\sqrt{d_j}\,D^j_{mn}(U):j\le J,\ -j\le m,n\le j
\}
\subset L^2(G,dU).
```

For a finite lattice `K` with edge set `E`, the link battery is

```math
{\mathcal C}_J(G^E)=
\bigotimes_{e\in E}{\mathcal C}_J(G).
```

The endpoint space remains `G^E` or its gauge quotient. The cutoff object is
the finite declared battery `{\mathcal C}_J(G^E)`.

## 4. Gauge Action, Gauss Battery, And Boundary Centers

Gauge transformations `h\in G^V` act on links by

```math
(h\cdot U)_e=h_{t(e)}U_eh_{s(e)}^{-1}.
```

Let `{\mathcal P}_{\rm G}` be the Haar gauge-average projector:

```math
({\mathcal P}_{\rm G}F)(U)
=
\int_{G^V}F(h\cdot U)\,dh.
```

The finite Gauss-invariant battery is

```math
{\mathcal B}_{J}^{\rm phys}(K)
=
{\mathcal P}_{\rm G}{\mathcal C}_J(G^E).
```

This is a finite-dimensional declared effect/observable battery, not a full
continuum local algebra.

### Definition 4.1: Boundary Representation Center

For a region `R\subset K`, cut links crossing `\partial R` carry representation
labels `j_e\le J` and magnetic/intertwiner indices. The boundary center at
cutoff `J` is the finite commutative label algebra generated by:

1. cut-link irreducible labels `j_e`;
2. admissible boundary intertwiners coupling the incident representations;
3. any declared external charge sector.

Write this label as

```math
z_{\partial R,J}.
```

It is the Peter-Weyl analogue of Paper 9's finite boundary-center label
`\sigma_R`.

### Theorem 4.2: Gauss Battery And Boundary Centers Are Cutoff-Stable

If `J'\ge J`, then the orthogonal Peter-Weyl projection

```math
P_{J,J'}:{\mathcal C}_{J'}(G^E)\to{\mathcal C}_{J}(G^E)
```

commutes with gauge averaging:

```math
P_{J,J'}{\mathcal P}_{\rm G}
=
{\mathcal P}_{\rm G}P_{J,J'}.
```

Consequently,

```math
P_{J,J'}{\mathcal B}_{J'}^{\rm phys}(K)
\subset
{\mathcal B}_{J}^{\rm phys}(K),
```

and boundary-center labels with all cut irreps `j_e\le J` are preserved by
projection.

### Proof

Peter-Weyl projection is the direct sum projection onto irreducible
representation blocks `j\le J` on each link. Left and right regular `SU(2)`
actions preserve each irreducible block. Gauge transformations are products of
left and right regular actions on incident links. Therefore the block
projection commutes with every gauge transformation and hence with Haar
averaging. Boundary labels are made from the same representation blocks and
intertwiner multiplicity spaces, so labels below cutoff are unchanged by
discarding only blocks above `J`. `square`

## 5. Projective Maps

There are two projective directions.

### Representation-Cutoff Projection

For `J'\ge J`, use

```math
P_{J,J'}:{\mathcal B}_{J'}^{\rm phys}(K)\to
{\mathcal B}_{J}^{\rm phys}(K)
```

as in Theorem 4.2.

### Lattice Coarsening Map

For lattices `K_a` and `K_b` with `b=na`, assume each coarse edge `E` is a
path of fine edges `e_n\cdots e_1`. The group-level coarse holonomy map is

```math
U_E^{(b)}=U_{e_n}^{(a)}\cdots U_{e_1}^{(a)}.
```

Pullback along this map sends coarse cylindrical functions to fine cylindrical
functions:

```math
B_{a,b}^*:{\mathcal C}(G^{E_b})\to{\mathcal C}(G^{E_a}).
```

The projective coarse-graining map on finite batteries is its adjoint/restrict
map after Peter-Weyl projection:

```math
B_{b,a}^{(J)}
=
P_J(B_{a,b}^*)^*P_J.
```

This is not claimed to be exact continuum renormalization. It is the declared
finite-battery map for tested cylindrical observables.

### Hypothesis PC: Projective Compatibility Of Batteries

For every finite admissible battery `{\mathcal F}`, there are cutoffs
`J(a)` and lattices `K_a` such that the combined maps

```math
{\mathcal P}_{a\to b}
=
B_{b,a}^{(J(b))}P_{J(b),J(a)}
```

are uniformly bounded and satisfy projectivity on the battery:

```math
\|{\mathcal P}_{b\to c}{\mathcal P}_{a\to b}
-{\mathcal P}_{a\to c}\|_{\mathcal F}
\le
\delta_{\rm proj}(a,b,c),
```

with `\delta_{\rm proj}\to0` along the refinement net.

### Theorem 5.1: Gauss-Sector Projective Stability

Under Hypothesis PC, the combined projective maps preserve Gauss-invariant
finite batteries and preserve boundary-center labels below the retained
cutoff, up to the explicit residual `\delta_{\rm proj}`.

### Proof

Representation projection commutes with gauge averaging by Theorem 4.2.
Coarse holonomy maps are gauge covariant: if the fine path goes from `x` to
`y`, the product holonomy transforms as `h_yU_Eh_x^{-1}`. Hence pullback and
its finite-battery adjoint preserve the gauge-invariant subspace. Boundary
labels below cutoff are representation/intertwiner labels of the cut
holonomies and are preserved by projection unless explicitly discarded by
`P_{J,J'}`. The only remaining failure is the declared battery projectivity
residual. `square`

## 6. Reference Kernels And Inverse Control

Let `\mu_{\beta,J,a}` be a declared gauge-action state on
`{\mathcal B}_{J}^{\rm phys}(K_a)`. The conservative choice is not to truncate
the positivity of the parent gauge measure; instead restrict its expectations
to the finite Peter-Weyl battery:

```math
\mu_{\beta,J,a}(F)
=
\frac{\int F(U)\exp(-S_{\beta,a}(U))\,dU}
{\int \exp(-S_{\beta,a}(U))\,dU},
\qquad
F\in{\mathcal B}_{J}^{\rm phys}(K_a).
```

Define the finite-battery heat-bath reference operator

```math
\Gamma_{0,J,a}
=
(1-\epsilon)I+\epsilon\Pi_{\mu_{\beta,J,a}},
```

where

```math
\Pi_{\mu_{\beta,J,a}}F=\mu_{\beta,J,a}(F)\,1.
```

### Theorem 6.1: Uniform Reference Inverse Bound

For `0<\epsilon<1`, the reference operator is invertible on every finite
battery and

```math
\Gamma_{0,J,a}^{-1}
=
(1-\epsilon)^{-1}(I-\Pi_{\mu_{\beta,J,a}})
+\Pi_{\mu_{\beta,J,a}}.
```

In any norm for which `\Pi_{\mu}` is a contraction and the decomposition into
constants plus zero-mean functions is bounded by `C_{\rm dec}`,

```math
\|\Gamma_{0,J,a}^{-1}\|
\le
C_{\rm dec}\max\{(1-\epsilon)^{-1},1\}.
```

### Proof

The expectation projection satisfies `\Pi_\mu^2=\Pi_\mu`. On constants,
`\Gamma_0` acts as identity. On the zero-mean subspace, it acts as
`1-\epsilon`. Inverting on these two invariant subspaces gives the formula and
the bound. `square`

### Hypothesis KCOMP: Kernel Compatibility

For every localized gauge-compatible deformation `R`, assume the primitive
deformed kernels satisfy

```math
\|
{\mathcal P}_{a\to b}\Gamma_{R,J(a),a}
-
\Gamma_{R,J(b),b}{\mathcal P}_{a\to b}
\|_{\mathcal F}
\le
\delta_R(a,b),
```

and the same estimate for `R=0`, with `\delta_R(a,b)\to0` on the finite
admissible battery.

Assume also the reference inverses are projectively compatible:

```math
\|
{\mathcal P}_{a\to b}\Gamma_{0,J(a),a}^{-1}
-
\Gamma_{0,J(b),b}^{-1}{\mathcal P}_{a\to b}
\|_{\mathcal F}
\le
\delta_0^{\rm inv}(a,b),
```

with `\delta_0^{\rm inv}(a,b)\to0`.

This is the main nontrivial analytic hypothesis of Paper 10. It must not be
hidden.

## 7. Comparison-Map Compatibility

Define

```math
J_{R,J,a}
=
\Gamma_{R,J,a}\Gamma_{0,J,a}^{-1}.
```

### Theorem 7.1: Projective Comparison-Map Transfer

Assume Hypothesis KCOMP and the uniform inverse bound of Theorem 6.1. Then on
every finite admissible battery,

```math
\|
{\mathcal P}_{a\to b}J_{R,J(a),a}
-
J_{R,J(b),b}{\mathcal P}_{a\to b}
\|
\le
C_{\rm inv}\delta_R(a,b)+C_R\delta_0^{\rm inv}(a,b),
```

where `C_{\rm inv}` is the uniform reference-inverse bound and `C_R` depends
on the bounded deformed kernel on the tested battery.

### Proof

Insert `J_R=\Gamma_R\Gamma_0^{-1}` and add/subtract
`\Gamma_{R,b}{\mathcal P}_{a\to b}\Gamma_{0,a}^{-1}`. The first term is
bounded by the primitive deformation compatibility error times the inverse
bound. The second term is bounded by the deformed-kernel norm times the
declared inverse-compatibility residual. All operators are finite-dimensional
on the declared battery, so the displayed bound follows. `square`

### Corollary 7.2: Exchange-Defect Compatibility

If `J_R`, `J_S`, and their inverses are uniformly bounded on the tested
battery, then

```math
{\mathcal P}_{a\to b}E_{R,S;J(a),a}
-
E_{R,S;J(b),b}{\mathcal P}_{a\to b}
\to0.
```

### Proof

The exchange defect is a finite product
`J_S^{-1}J_R^{-1}J_SJ_R`. Apply Theorem 7.1 to each factor and use the
uniform product bound. `square`

## 8. Smooth Curvature Target

This section identifies the continuum-facing target of the non-Abelian
charged-channel coefficient. It is a smooth-background theorem, not a
Yang-Mills measure construction.

Let `A_\mu(x)` be a smooth `\mathfrak{su}(2)` connection in a coordinate patch.
For a small edge of length `a`, define the link holonomy

```math
U_\mu(x,a)
=
\mathcal P\exp\left(\int_0^a A_\mu(x+t\hat\mu)\,dt\right).
```

The plaquette holonomy is

```math
U_{\mu\nu}(x,a)
=
U_\nu(x+a\hat\mu,a)U_\mu(x,a)
U_\nu(x,a)^{-1}U_\mu(x+a\hat\nu,a)^{-1}.
```

### Theorem 8.1: Non-Abelian Field-Strength Target

For a smooth connection,

```math
U_{\mu\nu}(x,a)
=
\exp\left(a^2F_{\mu\nu}(x)+O(a^3)\right),
```

where

```math
F_{\mu\nu}
=
\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu].
```

Consequently, for every fixed finite-dimensional representation `\rho`,

```math
\frac{\rho(U_{\mu\nu}(x,a))-I}{a^2}
\to
d\rho(F_{\mu\nu}(x)).
```

### Proof

Expand the four edge transports by the ordered exponential expansion and use
the Baker-Campbell-Hausdorff formula. The first-order terms cancel around the
plaquette. The second-order derivative terms give
`\partial_\mu A_\nu-\partial_\nu A_\mu`, and the noncommuting second-order
terms give `[A_\mu,A_\nu]`. Applying the finite-dimensional representation and
dividing by `a^2` gives the stated limit. `square`

### Theorem 8.2: Charged Exchange-Coefficient Limit

Assume:

1. the charged transport deformations are supported on a plaquette-scale
   collar;
2. the smooth-background embedding above controls the tested finite battery;
3. the comparison-map compatibility of Theorem 7.1 holds;
4. the residuals obey
   ```math
   a^{-2}(\delta_R(a,b)+\delta_S(a,b)+\delta_{\rm proj}(a,b,c))\to0.
   ```

Then the normalized charged exchange coefficient has the continuum-facing
target

```math
a^{-2}C_{R,S;J(a),a}
\to
d\rho(F_{\mu\nu})
```

on the declared charged plaquette channel, up to the source/sink contractions
of the instrument.

### Proof

Paper 9 identifies the first non-Abelian coefficient as the charged
representation ordering defect. Theorem 8.1 identifies the corresponding
small-plaquette ordered product with `a^2F_{\mu\nu}+O(a^3)`. Theorem 7.1 and
the residual assumption allow this coefficient to be transferred along the
projective system after division by `a^2`. `square`

### Scalar Probe Boundary

By Paper 9's scalar-probe no-faking theorem, class-function probes can detect
conjugacy-class data such as Wilson-loop traces, but they cannot by themselves
recover the full oriented matrix-valued `F_{\mu\nu}`. The charged channel is
not optional if the target is the non-Abelian covariant curvature, rather than
only trace data.

## 9. Continuum Yang-Mills Target Conditions

This section pushes toward continuum Yang-Mills without claiming it. The target
is a finite-battery Euclidean gauge theory interface: Wilson-loop expectations,
reflection-positive finite lattices, and a projective family of gauge-invariant
Schwinger functions.

### Definition 9.1: Finite-Battery Yang-Mills Target

A projective `SU(2)` gauge ISP family has a finite-battery Yang-Mills target if
for every finite list of piecewise smooth loops `C_1,\ldots,C_n` and every
representation list `\rho_1,\ldots,\rho_n`, there are lattice loops
`C_{i,a}` and Peter-Weyl cutoffs `J(a)` such that the Wilson-loop tests

```math
W_{\rho_i}(C_{i,a})
=
{\rm tr}_{\rho_i}\left(\prod_{e\in C_{i,a}}\rho_i(U_e)\right)
```

have a limit

```math
\lim_{a\to0}
\mu_{\beta(a),J(a),a}
\left(
\prod_{i=1}^n W_{\rho_i}(C_{i,a})
\right)
=
S(C_1,\rho_1;\ldots;C_n,\rho_n),
```

and the limiting functional satisfies:

1. Euclidean covariance on the tested loop class;
2. reflection positivity on the tested loop class;
3. gauge invariance;
4. Osterwalder-Schrader continuity on the tested class;
5. a nontrivial continuum scaling window.

This is still weaker than constructing continuum Yang-Mills. It is the
finite-battery target that Paper 10 can honestly aim at.

### Heat-Kernel Plaquette Action

Let `K_t(g)` be the `SU(2)` heat kernel:

```math
K_t(g)
=
\sum_{j\in\widehat{SU(2)}}d_j e^{-t j(j+1)}\chi_j(g),
\qquad
t>0.
```

On a finite Euclidean lattice define

```math
d\mu_{t,a}(U)
=
\frac{1}{Z_{t,a}}
\prod_p K_t(U_p)\prod_e dU_e.
```

This is the heat-kernel lattice gauge measure. Its Peter-Weyl cutoff
restriction is obtained by testing only against `{\mathcal B}_{J}^{\rm phys}`.

### Theorem 9.2: Finite Heat-Kernel Gauge Measure Is Admissible

For every finite lattice and every `t>0`, the heat-kernel gauge measure is:

1. gauge-invariant;
2. strictly positive on the compact endpoint space;
3. reflection-positive for reflections through lattice hyperplanes compatible
   with the plaquette decomposition;
4. character-positive, with coefficients `d_j e^{-t j(j+1)}>0`;
5. compatible with every finite Peter-Weyl battery by restriction of
   expectations.

### Proof

Gauge invariance follows because each plaquette holonomy transforms by
conjugation and `K_t` is central. Strict positivity follows from positivity of
the heat kernel for `t>0` on compact connected Lie groups. Character positivity
is displayed in the Peter-Weyl expansion. Reflection positivity for the
heat-kernel lattice action follows from cutting the lattice along the
reflection plane and using the heat-kernel convolution/semigroup identity
together with positive character coefficients; reflected half-lattice
observables pair through a positive sum of representation-channel squares.
Finite Peter-Weyl compatibility is restriction of a positive expectation
functional to a finite-dimensional subspace. `square`

### Hypothesis YM-LIM: Continuum Yang-Mills Scaling Window

There exists a coupling/cutoff scaling

```math
t=t(a),
\qquad
J=J(a),
```

and finite-volume/thermodynamic-volume prescription such that the
finite-battery Wilson-loop functionals of Definition 9.1 converge and satisfy
the listed OS-type conditions.

This is not proved here. It is the honest continuum Yang-Mills gate.

### Theorem 9.3: Conditional Finite-Battery Yang-Mills Interface

If Hypothesis YM-LIM holds, then the projective Peter-Weyl ISP family defines a
finite-battery Euclidean Yang-Mills interface on the declared Wilson-loop test
class.

### Proof

The finite measures are gauge-invariant, character-positive, and
reflection-positive by Theorem 9.2. Hypothesis YM-LIM supplies convergence,
continuity, covariance, and a scaling window. Therefore the limiting functional
is a finite-battery Euclidean Yang-Mills interface on the declared test class.
`square`

### Definition 9.4: Standard-Facing Wilson Gauge-Matter Target

The conservative standard-QFT-facing target of Paper 10 is the finite-volume
`SU(2)` heat-kernel gauge field coupled to a declared Wilson matter battery.
On a hypercubic Euclidean lattice let the matter field be

```math
\psi_x\in{\mathbb C}^{d_{\rm spin}}\otimes V_\rho,
```

where `V_\rho` is a finite-dimensional charged `SU(2)` representation. Fix
Euclidean gamma matrices `\gamma_\mu`, Wilson parameter `r>0`, lattice spacing
`a`, and bare mass `m`. The finite Wilson-Dirac block is the matrix

```math
(D_W[U]\psi)_x
=
\left(m+\frac{dr}{a}\right)\psi_x
-\frac{1}{2a}\sum_{\mu=1}^d
\left[
(r-\gamma_\mu)\rho(U_{x,\mu})\psi_{x+a\hat\mu}
+(r+\gamma_\mu)\rho(U_{x-a\hat\mu,\mu})^{-1}\psi_{x-a\hat\mu}
\right].
```

A standard-facing finite test battery consists of finitely many records of the
following types:

1. Wilson-loop traces of the gauge field;
2. gauge-invariant fermion bilinears with source/sink transport;
3. finite source contractions built from `D_W[U]^{-1}` on the invertible
   subdomain or with a declared infrared regulator;
4. optional determinant records, such as `\det(D_W[U]+M)` or an even-flavor
   positive prescription, when the sign/phase convention is explicitly part of
   the instrument.

The target is finite and typed. It is not a Gamma-only reconstruction of
fermions, spin, gauge frames, or the continuum QCD measure.

### Lemma 9.5: Finite Wilson Gauge-Matter Records Are Gauge-Compatible

On every finite lattice, the records in Definition 9.4 are gauge-compatible
finite-battery records.

### Proof

Under a gauge transformation,

```math
\psi_x\mapsto (I_{\rm spin}\otimes\rho(h_x))\psi_x,
\qquad
U_{x,\mu}\mapsto h_xU_{x,\mu}h_{x+a\hat\mu}^{-1},
```

the edge transport term in `D_W[U]` intertwines the sitewise gauge action.
Thus `D_W[U]` transforms by conjugation on the finite matter vector space.
Gauge-loop traces are conjugation invariant. Source/sink contractions are
invariant once the sources are declared as charged instruments transforming in
the dual representation. Determinants and traces of finite conjugated matrices
are invariant. Therefore the listed records are admissible finite operational
records. `square`

## 10. One-Step Gauge Renormalization

This section replaces part of the vague projectivity burden with a concrete
blocking theorem in the safest setting. It is exact for heat-kernel plaquette
variables in two-dimensional plaquette blocking and becomes a named hypothesis
in higher dimensions.

### Theorem 10.1: Exact Heat-Kernel Plaquette Blocking In Two Dimensions

Consider two adjacent plaquettes in a two-dimensional lattice whose holonomies
multiply to a coarse plaquette holonomy

```math
U_P=U_{p_2}U_{p_1}.
```

If the fine plaquette weights are heat kernels `K_{t_1}(U_{p_1})` and
`K_{t_2}(U_{p_2})`, then integrating over the shared internal edge gives the
coarse heat-kernel weight

```math
K_{t_1+t_2}(U_P).
```

More generally, blocking `N` fine plaquettes in a simply connected
two-dimensional block gives `K_{Nt}(U_P)` for equal fine time `t`.

### Proof

After gauge fixing all internal tree edges of the two-plaquette block, the only
internal integration left is group convolution. The heat kernel satisfies the
semigroup identity

```math
\int_G K_{t_2}(gh^{-1})K_{t_1}(h)\,dh
=
K_{t_1+t_2}(g).
```

Applying this identity to the shared edge variable yields the coarse
plaquette heat kernel. Iterating gives the `N`-plaquette formula. `square`

### Corollary 10.2: One-Step Renormalization Residual In The 2D Heat-Kernel Block

For the two-dimensional heat-kernel block above, the projective kernel
compatibility residual for scalar Wilson-loop batteries is exactly zero when
the coarse heat-kernel time is chosen as

```math
t_b=N\,t_a.
```

### Proof

The blocked measure is exactly the coarse heat-kernel measure by Theorem 10.1.
Therefore coarse Wilson-loop expectations agree with blocked fine expectations
on the scalar loop battery. The residual is zero. `square`

### Hypothesis RG-D: Higher-Dimensional Gauge Blocking Residual

In dimensions `d\ge3`, plaquettes are coupled by Bianchi constraints and
blocking is not an exact heat-kernel convolution. Assume a gauge-covariant
block map and running coupling `t_b=R_b(t_a)` such that for every finite
admissible gauge battery

```math
\|
{\mathcal R}_{a\to b}^*\mu_{t_a,J(a),a}
-
\mu_{t_b,J(b),b}
\|_{\mathcal F}
\le
\delta_{\rm RG}(a,b),
```

with `\delta_{\rm RG}(a,b)\to0` in the desired scaling window.

### Theorem 10.3: RG-D Implies Projective Kernel Compatibility

If Hypothesis RG-D holds and the deformation kernels are local
Radon-Nikodym/finite-instrument tilts with uniformly bounded logarithmic
activities on the tested battery, then Hypothesis KCOMP holds with residual

```math
\delta_R(a,b)
\le
C_R\delta_{\rm RG}(a,b)+\delta_{\rm loc}(a,b),
```

where `\delta_{\rm loc}` is the localization error of transporting the
deformation through the block map.

### Proof

The undeformed kernel compatibility follows directly from RG-D. A localized
tilt multiplies the finite expectation functional by a bounded local activity.
Transporting it through the block map changes it by the RG residual times the
activity bound plus the error made by replacing the fine local activity by its
coarse localized representative. This is exactly the displayed estimate.
`square`

### Definition 10.4: Finite-Battery Perfect Block

Fix a fine lattice `K_a`, a coarse lattice `K_b`, a gauge-covariant block map
`B_{a,b}:G^{E_a}\to G^{E_b}`, and a finite coarse test battery
`{\mathcal F}_b`. The perfect blocked state on `{\mathcal F}_b` is

```math
\mu^{\rm perf}_{b}(F)
=
\mu_{a}(F\circ B_{a,b}),
\qquad
F\in{\mathcal F}_b.
```

This is not assumed to come from a local Wilson or heat-kernel action. It is
the exact whole-process coarse description seen by the declared finite
battery.

### Theorem 10.5: Exact One-Step Projectivity For Perfect Blocks

For every finite lattice, every compact gauge group, every gauge-covariant
block map, and every finite coarse battery `{\mathcal F}_b`, the perfect block
has zero one-step residual:

```math
\sup_{\|F\|_{\mathcal F_b}\le1}
\left|
\mu_a(F\circ B_{a,b})-\mu^{\rm perf}_b(F)
\right|
=0.
```

If localized finite-instrument tilts are blocked by the same pushforward rule,
the corresponding primitive kernel compatibility residual is also zero on the
declared battery.

### Proof

The first identity is the definition of the pushforward state restricted to
the finite battery. For a localized tilt, first multiply the fine whole-process
state by the declared activity and then push it forward. The coarse tilted
state is again defined as that pushforward on the battery, so the fine and
coarse expectation functionals agree identically. No Markov divisibility or
local-action assumption has been inserted. `square`

### Corollary 10.6: Local-Action Residual Is The Real Higher-Dimensional Gate

Let `\mu^{\rm loc}_{b,\theta}` be a chosen local coarse ansatz, for example a
heat-kernel, Wilson plaquette, or improved gauge action with parameters
`\theta`. For a finite battery `{\mathcal F}_b`, define

```math
\delta_{\rm locRG}^{\mathcal F}(a,b)
=
\inf_\theta
\sup_{\|F\|_{\mathcal F_b}\le1}
\left|
\mu_b^{\rm perf}(F)-\mu^{\rm loc}_{b,\theta}(F)
\right|.
```

Then one-step higher-dimensional RG compatibility with a local standard-QFT
ansatz is equivalent, on that finite battery, to
`\delta_{\rm locRG}^{\mathcal F}(a,b)\to0` along the chosen scaling path.

### Proof

The perfect block gives exact projectivity by Theorem 10.5. Replacing the
perfect block by a local ansatz changes finite-battery predictions by exactly
the displayed operator-norm difference. Minimizing over the ansatz parameters
gives the best local residual. Vanishing of that residual is therefore
precisely the finite-battery condition needed to replace exact whole-process
blocking by a local Wilson/heat-kernel RG step. `square`

### Definition 10.7: Concrete Four-Dimensional Local-RG Battery

For a finite four-dimensional hypercubic coarse lattice `K_b`, define the
standard local-RG battery `{\mathcal F}_{4D,b}` to be the finite real span of
the following declared records:

1. scalar gauge loops:
   ```math
   {\rm Re}\,{\rm tr}_{1/2}(U_P),\qquad
   {\rm Re}\,{\rm tr}_{1/2}(U_R),\qquad
   {\rm Re}\,{\rm tr}_{1/2}(U_C),
   ```
   for a declared finite list of plaquettes `P`, rectangles `R`, and
   chair/parallelogram loops `C`;
2. charged plaquette curvature records:
   ```math
   \Phi_{P,\rho,u,v}
   =
   b^{-2}\langle u,(\rho(U_P)-I)v\rangle,
   ```
   where `u,v` are declared source/sink frame vectors;
3. Wilson matter records from Definition 9.4, including finitely many
   gauge-invariant bilinears and source contractions built from the finite
   Wilson-Dirac block;
4. finite products of the listed records up to a declared degree `q`.

Choose a basis

```math
F_1,\ldots,F_m
```

for this battery. For any state or normalized functional `\nu`, write its
battery moment vector as

```math
M_{\mathcal F}(\nu)
=
(\nu(F_1),\ldots,\nu(F_m))\in{\mathbb C}^m.
```

This is the concrete battery on which Paper 10 measures the local-action
residual. It is finite, operationally typed, and intentionally weaker than a
claim about the full continuum local algebra.

### Definition 10.8: Local Coarse Ansatz Family

Let `A_1,\ldots,A_p` be bounded gauge-invariant local action terms on `K_b`.
The conservative choice includes:

1. plaquette heat-kernel or character terms;
2. rectangle terms;
3. chair/parallelogram terms;
4. local clover-curvature terms paired with charged instruments;
5. Wilson-matter counterterms and gauge-invariant source terms when the
   Wilson branch is being tested.

For real parameters `\theta=(\theta_1,\ldots,\theta_p)` define

```math
d\mu^{\rm loc}_{b,\theta}
=
\frac{\exp(\sum_{\alpha=1}^p\theta_\alpha A_\alpha)}
{Z(\theta)}
d\nu_b,
```

where `\nu_b` is the chosen finite positive reference measure. Complex
determinant phases or signs are not hidden in this formula; if present they
are declared as reweighting instruments as in Section 12.

The local moment map is

```math
M(\theta)
=
M_{\mathcal F}(\mu^{\rm loc}_{b,\theta})\in{\mathbb C}^m.
```

### Definition 10.9: Response Matrix And Missing Local Directions

Fix a base parameter `\theta_0`. The response matrix of the local ansatz on
the finite battery is

```math
C_{i\alpha}
=
\left.\frac{\partial M_i}{\partial\theta_\alpha}\right|_{\theta_0}
=
{\rm Cov}_{\theta_0}(F_i,A_\alpha),
```

with the obvious complex-bilinear interpretation when charged records are
included.

Let

```math
m^*
=
M_{\mathcal F}(\mu_b^{\rm perf}),
\qquad
y=m^*-M(\theta_0).
```

Choose a projection `\Pi_C` onto `{\rm Ran}\,C`. The finite-battery missing
local-direction error is

```math
\epsilon_\perp
=
\|(I-\Pi_C)y\|.
```

If `C` has a bounded right inverse `Q` on `{\rm Ran}\,C`, write

```math
\kappa=\|Q\|.
```

This rank condition is the finite-battery version of saying that the chosen
local terms can move all tested local records to first order. If the condition
fails, the failure is informative: the battery is seeing a nonlocal, omitted,
or branch-specific direction.

### Lemma 10.9A: Response-Rank Criterion

Work on the realification of the finite battery, so complex charged records
are represented by their real and imaginary parts. Let

```math
\widetilde F_i=F_i-\mu_{\theta_0}(F_i),
\qquad
\widetilde A_\alpha=A_\alpha-\mu_{\theta_0}(A_\alpha).
```

The response matrix has full tested rank on the battery if and only if the
only vector `\lambda=(\lambda_i)` satisfying

```math
\mu_{\theta_0}
\left[
\left(\sum_i\lambda_i\widetilde F_i\right)
\widetilde A_\alpha
\right]
=0
\qquad
\text{for every }\alpha
```

is a null tested direction, meaning

```math
\sum_i\lambda_i\widetilde F_i=0
```

in the covariance seminorm of the reference state on the declared battery.

In particular, if the local ansatz contains symmetry-allowed local operators
`A_\alpha` whose centered span contains the centered tested records
`\widetilde F_i` modulo covariance-null relations, and the covariance form is
nondegenerate on the quotient, then the response matrix has full tested rank.

### Proof

The response matrix is the finite covariance pairing between the tested record
space and the local-operator space. A vector `\lambda` is in the left kernel of
`C` exactly when the tested combination
`\sum_i\lambda_i\widetilde F_i` has zero covariance with every ansatz
direction. Thus `C` has full rank on the quotient precisely when its left
kernel consists only of covariance-null tested combinations. If the centered
ansatz span contains the centered test space and the covariance form is
nondegenerate after quotienting null relations, no nonzero tested combination
can be orthogonal to every ansatz direction. `square`

### Theorem 10.10: Finite-Battery Local Projection Estimate

Assume the local moment map is twice differentiable on the ball
`B(\theta_0,\rho)` and has second-order remainder bound

```math
\|M(\theta_0+\delta)-M(\theta_0)-C\delta\|
\le
L\|\delta\|^2
```

for all `\|\delta\|\le\rho`. Assume `C` has right inverse `Q` on
`{\rm Ran}\,C` and that

```math
\kappa\|\Pi_C y\|\le\rho.
```

Then the parameter shift

```math
\delta\theta=Q\Pi_C y
```

satisfies

```math
\|M(\theta_0+\delta\theta)-m^*\|
\le
\epsilon_\perp
+L\kappa^2\|\Pi_C y\|^2.
```

In particular, if the perfect-block displacement lies in `{\rm Ran}\,C` to
first order, the local ansatz matches the finite battery up to quadratic
error.

### Proof

By construction, `C\delta\theta=\Pi_Cy`. Therefore

```math
M(\theta_0+\delta\theta)-m^*
=
M(\theta_0)+C\delta\theta-m^*
+\left[M(\theta_0+\delta\theta)-M(\theta_0)-C\delta\theta\right].
```

The first two terms equal `-\,(I-\Pi_C)y`, whose norm is
`\epsilon_\perp`. The remainder is bounded by
`L\|\delta\theta\|^2\le L\kappa^2\|\Pi_Cy\|^2`. `square`

### Corollary 10.11: Explicit Local-Action Residual Bound

On the concrete battery `{\mathcal F}_{4D,b}`, suppose the battery norm is
equivalent to the chosen moment-vector norm with constant `C_{\mathcal F}`.
Then the local-action residual satisfies

```math
\delta_{\rm locRG}^{\mathcal F}(a,b)
\le
C_{\mathcal F}
\left(
\epsilon_\perp
+L\kappa^2\|\Pi_Cy\|^2
\right)
+\epsilon_{\rm tail}.
```

Here `\epsilon_{\rm tail}` is the explicitly declared error from records not
included in the finite basis or from replacing a larger local ansatz by the
chosen finite list of terms.

### Proof

Theorem 10.10 gives a parameter value whose moment-vector mismatch is bounded
by the displayed finite-dimensional error. The norm-equivalence constant
converts this moment mismatch to the battery norm used in
`\delta_{\rm locRG}^{\mathcal F}`. Any omitted records or omitted local action
directions contribute only through the declared tail error. `square`

### Theorem 10.12: Local Residual Propagates To ISP Comparison Maps

Assume the finite-battery local-action residual obeys

```math
\delta_{\rm locRG}^{\mathcal F}(a,b)\le\varepsilon_{\rm RG}(a,b),
```

and that localized deformation activities have transport error
`\varepsilon_{\rm act}(a,b)`. Then on the same battery,

```math
\delta_R(a,b)
\le
C_R\varepsilon_{\rm RG}(a,b)+\varepsilon_{\rm act}(a,b),
```

so Theorem 7.1 gives

```math
\|
{\mathcal P}_{a\to b}J_{R,J(a),a}
-
J_{R,J(b),b}{\mathcal P}_{a\to b}
\|
\le
C_{\rm inv}C_R\varepsilon_{\rm RG}
+C_{\rm inv}\varepsilon_{\rm act}
+C_R'\delta_0^{\rm inv}.
```

If `J_R`, `J_S`, and their inverses are uniformly bounded, the same residual
propagates to the exchange defect `E_{R,S}` by the product estimate of
Corollary 7.2.

### Proof

The local ansatz differs from the exact perfect block by
`\varepsilon_{\rm RG}` on the declared battery. Transporting a localized
activity through the block map adds the activity error
`\varepsilon_{\rm act}`. This is precisely the hypothesis needed in Theorem
10.3. Applying Theorem 7.1 gives the displayed comparison-map estimate, and
Corollary 7.2 propagates it to products and commutators. `square`

### Diagnostic Examples 10.13: First Missing-Direction Tests

The response-rank test gives a concrete way to locate the obstruction.

**Scalar Wilson-loop battery.** If `{\mathcal F}_{4D,b}` contains only the
declared scalar loop records and the ansatz contains the same plaquette,
rectangle, and chair/parallelogram loop terms, then Lemma 10.9A reduces rank
to the covariance matrix of those loop records. If that covariance matrix is
nondegenerate after quotienting exact loop identities and lattice symmetries,
then `\epsilon_\perp=0` to first order. If it is degenerate, the degeneracy is
not a physical obstruction; the battery has redundant records and should be
quotiented.

**Scalar loops plus charged curvature.** If the battery includes charged
plaquette curvature records but the ansatz contains only scalar class
functions, the charged framed directions are generally outside the scalar
response span. Then `\epsilon_\perp` is the charged-channel signal that scalar
Wilson data cannot fake. Adding clover-curvature/source-sink local terms is
the minimal local completion if those records are part of the standard-facing
target.

**Wilson matter source contractions.** If the battery includes Wilson-Dirac
source contractions but the ansatz contains only pure gauge loops, the matter
directions are missing unless they are already determined by the gauge-loop
statistics on the finite battery. The response test therefore forces explicit
Wilson-matter counterterms, source terms, or determinant/reweighting records.

**No-Wilson taste/detail records.** If the no-Wilson battery includes
taste/detail resolving records and the ansatz omits taste/detail local
operators, the missing direction is physical branch data. Projecting it away
is allowed only as a declared taste-blind instrument with recorded rejection
or coarse-graining outcomes.

These are not separate assumptions. They are finite-dimensional consequences
of Lemma 10.9A applied to different declared batteries.

### Rule 10.14: Local Ansatz Completion Rule

When the residual decomposition gives `\epsilon_\perp\ne0`, exactly one of the
following actions must be taken:

1. **Add a symmetry-allowed local operator.** If the missing tested direction
   is generated by a gauge-invariant, local, branch-compatible operator, add
   the minimal such operator to the ansatz and recompute the response matrix.
2. **Record branch-specific data.** If the missing direction is a no-Wilson
   taste/detail record or a charged instrument label, keep it as typed
   operational data rather than absorbing it into scalar Gamma.
3. **Declare a nonlocal perfect-block obstruction.** If no local
   symmetry-allowed operator spans the direction on the tested battery, mark
   the residual as a genuine nonlocal local-action obstruction for that
   battery.
4. **Quotient a redundant battery direction.** If the missing direction is a
   covariance-null identity, lattice symmetry duplicate, or exact loop
   relation, remove it from the independent battery basis.

No fifth option is allowed. In particular, Paper 10 may not silently set
`\epsilon_\perp` to zero by Markovizing the blocked process or by treating
charged/taste records as if they were scalar Gamma records.

### Algorithm 10.15: Iterative Finite-Battery Local RG Closure

For a fixed refinement step `a\to b`, branch choice, and finite battery:

1. compute or estimate the perfect-block moment vector
   `m^*=M_{\mathcal F}(\mu_b^{\rm perf})`;
2. choose a local ansatz `A_1,\ldots,A_p` and base parameter `\theta_0`;
3. compute the response matrix
   `C_{i\alpha}={\rm Cov}_{\theta_0}(F_i,A_\alpha)`;
4. solve the least-squares/right-inverse problem
   `\delta\theta=Q\Pi_C(m^*-M(\theta_0))`;
5. evaluate the residual decomposition
   `\epsilon_\perp+L\kappa^2\|\Pi_Cy\|^2+\epsilon_{\rm tail}`;
6. apply Rule 10.14 to enlarge the ansatz, quotient redundancies, record
   branch-specific data, or declare a nonlocal obstruction;
7. iterate until the declared pass tolerance is met or until Rule 10.14 yields
   a stable obstruction.

If the iteration reaches residuals

```math
\varepsilon_{\rm RG}(a,b)\to0
```

along the scaling path for the chosen finite batteries, then Theorem 10.12
promotes the result to projective comparison-map and exchange-defect control.
If it does not, the output is still useful: it identifies the first concrete
operator, branch record, or nonlocal residue preventing standard local-QFT
closure.

### Theorem 10.16: Scalar Tiny-Battery Closure

Let the finite battery consist of independent scalar Wilson-loop records

```math
F_i=L_i-\mu_{\theta_0}(L_i),
\qquad
i=1,\ldots,m,
```

where the `L_i` are the declared plaquette, rectangle, and chair/parallelogram
loop records after quotienting exact lattice symmetries and loop identities.
Choose the local ansatz operators to include the same centered records:

```math
A_i=F_i.
```

Let

```math
G_{ij}=\mu_{\theta_0}(F_iF_j)
```

be the scalar-loop covariance matrix. If `G` is invertible on the quotient
and the displacement `y=m^*-M(\theta_0)` is inside the perturbative ball of
Theorem 10.10, then the scalar tiny battery has

```math
\epsilon_\perp=0
```

and

```math
\delta_{\rm locRG}^{\mathcal F}(a,b)
\le
C_{\mathcal F}L\|G^{-1}\|^2\|y\|^2+\epsilon_{\rm tail}.
```

### Proof

With `A_i=F_i`, the response matrix is exactly the covariance matrix `G`.
Invertibility on the quotient means `{\rm Ran}\,C` is the whole independent
tested scalar-loop space, so the perpendicular component vanishes. The
displayed estimate is Corollary 10.11 with `Q=G^{-1}`. `square`

This is the first positive closure test. It says that a scalar loop battery
does not require mystery data: once redundant loop directions are quotiented,
matched local loop terms close the battery to first order.

### Theorem 10.17: Charged Curvature Closure And Scalar Failure

Let the battery add traceless charged plaquette records

```math
\Phi_{P,\rho,u,v}^{\rm tr}
=
b^{-2}
\left\langle u,
\left(\rho(U_P)-\frac{\chi_\rho(U_P)}{d_\rho}I\right)v
\right\rangle,
```

with declared charged source/sink frames. Suppose the reference state averages
over gauge frames and the local ansatz contains only scalar class-function
loop terms. Then the traceless charged record lies outside the scalar response
span, so its contribution appears in `\epsilon_\perp`.

If the ansatz is enlarged by matching charged clover/source-sink local terms
`A_\Phi` for the declared charged records and the enlarged covariance matrix
is nondegenerate on the scalar-plus-charged quotient, then the scalar-plus-
charged battery closes to first order and obeys the local projection estimate
of Corollary 10.11.

### Proof

Scalar class-function loop terms are central in the charged representation
channel. The traceless charged record is the noncentral part of the same
plaquette transport. Under frame averaging, central and traceless noncentral
isotypic components are covariance-orthogonal. Thus a scalar-only ansatz has a
nonzero perpendicular component whenever the perfect block moves the charged
record. Adding the matching charged clover/source-sink operators puts those
directions into the ansatz span. Lemma 10.9A and Corollary 10.11 then give the
closure statement. `square`

This is the first non-Abelian lesson. Scalar Wilson data may close as a scalar
gauge battery, but it cannot by itself close charged curvature data. The
charged instrument is not decorative; it is the operational carrier of framed
non-Abelian curvature.

### Theorem 10.18: Wilson Matter Tiny-Battery Closure

Let the battery include finitely many Wilson matter records

```math
S_\ell(U)
=
\langle \eta_\ell,(D_W[U]+M)^{-1}\xi_\ell\rangle
```

on a declared invertible or infrared-regularized finite Wilson-Dirac domain,
together with the scalar gauge-loop records of Theorem 10.16. A pure-gauge
local ansatz closes this battery only if the centered matter records lie in
the covariance span of the centered gauge-loop records.

If the local ansatz is enlarged by Wilson-matter source/counterterm operators
whose centered span contains the centered `S_\ell` modulo covariance-null
relations, and the enlarged covariance form is nondegenerate on the quotient,
then the Wilson matter battery closes to first order with the bound of
Corollary 10.11.

### Proof

Apply Lemma 10.9A. With only pure-gauge operators, the response span is the
covariance span generated by pure-gauge loop records. Any independent Wilson
matter source contraction is perpendicular to that restricted span and
contributes to `\epsilon_\perp`. Once the matching Wilson-matter operators are
declared and the covariance form is nondegenerate on the enlarged quotient,
the response matrix has full tested rank, and Theorem 10.10 plus Corollary
10.11 gives the residual estimate. `square`

This is the finite-battery version of the usual renormalization lesson:
matter records require matter counterterms or matter instruments. They are
not reconstructed from scalar gauge loops alone.

### Table 10.19: First Branch Outcomes

| Battery | Minimal local ansatz | Closure status | Interpretation |
| --- | --- | --- | --- |
| Scalar plaquette/rectangle/chair loops | Matching scalar loop terms | Closes to first order if the scalar covariance matrix is nondegenerate after quotienting identities | Positive finite scalar gauge benchmark |
| Scalar loops plus charged curvature | Scalar loop terms only | Fails in the traceless charged channel | Scalar Gamma cannot fake framed non-Abelian curvature |
| Scalar loops plus charged curvature | Scalar loops plus charged clover/source-sink terms | Closes to first order under enlarged covariance rank | Enriched charged instruments are required and sufficient on the finite battery |
| Wilson matter source contractions | Pure gauge loop terms only | Fails unless matter records are covariance-dependent on gauge loops | Wilson matter is not reconstructed from scalar gauge data alone |
| Wilson matter source contractions | Gauge loops plus Wilson-matter counterterms/source operators | Closes to first order under enlarged covariance rank | Conservative standard-QFT-facing branch |
| No-Wilson taste/detail records | Wilson-blind local ansatz | Fails in taste/detail directions unless records are projected or taste-blinded | Retained-record branch data, not disposable error |
| No-Wilson taste/detail records | Taste/detail local terms plus recorded projection rules | Conditional closure or measurable branch difference | Possible multi-taste benchmark or discovery channel |

The table is finite-battery information, not a continuum theorem. Its value is
that it identifies the exact point where standard local QFT matching either
closes, requires enriched instruments, or exposes a retained-record
obstruction.

### Branch Split For The Local RG Gate

The Wilson branch and no-Wilson branch now have different local-RG obligations.

For the Wilson branch, include the Wilson-Dirac records of Definition 9.4 and
the Wilson counterterms in Definition 10.8. The branch succeeds on a finite
test battery when the response matrix has full tested rank and the residual
bound of Corollary 10.11 tends to zero along the scaling path. This would be a
standard-QFT-facing Wilson benchmark, not a Gamma-only derivation.

For the no-Wilson detail-preserving branch, extend
`{\mathcal F}_{4D,b}` by taste/detail resolving records and extend the local
ansatz by taste/detail local terms. If those terms are omitted, their signal
appears as `\epsilon_\perp`; it is not an error to sweep away, but a measured
branch difference. The no-Wilson route therefore either reproduces the Wilson
branch after declared projection/taste-blinding, or exposes additional
retained-record physics in the perpendicular response channel.

## 11. Gamma-Only Gauge Reconstruction No-Go

This section is a no-go theorem, not a pessimistic aside. It is the gauge
analogue of the earlier QFT reconstruction discipline.

### Definition 11.1: Scalar Gamma Gauge Data

Scalar Gamma gauge data consist of projective endpoint kernels and
probabilities for gauge-invariant scalar records generated by:

1. class functions of plaquette holonomies;
2. Wilson-loop traces;
3. products and limits of such scalar records.

They do not include charged source/sink frames, matrix-valued holonomy
elements, boundary intertwiners as operational readouts, or a declared
representation-channel instrument.

### Theorem 11.2: No Gamma-Only Reconstruction Of Non-Abelian Gauge Connection

Scalar Gamma gauge data do not reconstruct the full non-Abelian gauge
connection, oriented holonomy matrices, or charged parallel transport.

More precisely, no reconstruction rule whose input is only scalar Gamma gauge
data can uniquely output all charged transport matrices

```math
\rho(U_\gamma)
```

for all paths `\gamma` and representations `\rho`.

### Proof

Scalar class functions are invariant under conjugation. Wilson-loop traces
therefore determine conjugacy-class data, not a framed group element. For
`SU(2)`, `g` and `hgh^{-1}` have identical scalar class-function data for
every `h`, but their matrices in a fixed charged frame differ unless the frame
is transformed as well. Also `\chi_j(g)=\chi_j(g^{-1})` for `SU(2)`, so scalar
traces do not determine oriented transport direction in a charged channel.

A charged parallel transport matrix is meaningful only after declaring source
and sink frames or an equivalent representation-channel instrument. Those data
are excluded by Definition 11.1. Hence scalar Gamma data can at most reconstruct
gauge-invariant conjugacy-class statistics, not the full connection or charged
transport. `square`

### Corollary 11.3: Enriched Operational Gauge Reconstruction Is The Right Target

The strongest reconstruction target compatible with Paper 10 is:

```text
scalar Gamma gauge data
+ declared charged instruments
+ boundary/intertwiner labels
+ representation batteries
-> finite/projective operational gauge reconstruction.
```

The target is not:

```text
bare scalar Gamma -> full non-Abelian gauge field.
```

### Proof

The no-go theorem removes the Gamma-only target. Paper 9 and the present paper
show that once charged instruments, representation labels, and boundary
centers are declared, finite/projective operational gauge data can be
controlled. `square`

## 12. Wilson And No-Wilson Branches

Paper 10 keeps both branches typed.

### Wilson-Gauge Branch

The Wilson-gauge branch imports Wilson-compatible fermion/matter data and
gauge-covariant Wilson terms. Paper 10 proves only that the finite gauge
Peter-Weyl projective layer can carry such declared Wilson-gauge batteries.
It does not prove the Wilson fermion continuum limit.

### No-Wilson Detail-Preserving Branch

The no-Wilson branch keeps detail/taste labels as real records. Paper 10 proves
only that these labels can be carried together with Gauss sectors and boundary
centers through the projective gauge layer. It does not prove a full
multi-taste continuum QFT.

### Dynamical Matter Boundary

Finite dynamical Wilson matter can be included only as a declared finite
operational prescription. On a finite lattice, if a gauge-invariant weight

```math
w_{\rm f}(U)
```

is specified, for example an even-flavor positive determinant prescription or
a determinant with an explicitly recorded phase/sign reweighting, then

```math
\omega_{\rm gauge+f}(dU)
=
\frac{w_{\rm f}(U)}{\int w_{\rm f}(U)d\mu_{\rm gauge}(U)}
d\mu_{\rm gauge}(U)
```

defines a finite-battery normalized functional whenever the denominator is
nonzero and the chosen prescription is integrable. It is a positive state only
when the declared weight is nonnegative. A complex determinant phase or sign
must therefore be represented as an explicitly recorded reweighting
instrument. This is finite operational bookkeeping, not a continuum QCD
theorem.

The missing continuum theorem would have to prove, for a stated scaling path:

1. gauge-field continuum convergence;
2. fermion determinant or reweighting control;
3. reflection positivity or the appropriate OS replacement;
4. anomaly and chiral-symmetry bookkeeping;
5. compatibility with the Wilson or no-Wilson branch target.

### Theorem 12.1: Branch-Typed Gauge Projectivity

Under Hypotheses PC and KCOMP, both the Wilson-gauge and no-Wilson
detail-preserving finite batteries can be transported by the same
gauge-sector projective maps, provided their extra branch labels are included
as declared boundary/detail data.

### Proof

The gauge part of both branches is built from the same gauge-covariant link
transport and the same Gauss-invariant Peter-Weyl battery. The additional
Wilson regulator data or detail/taste labels are declared finite labels on the
matter/instrument battery. The projective maps act on gauge representation
labels and carry the extra finite labels as typed data. Therefore projectivity
reduces to Hypotheses PC and KCOMP plus the branch-specific finite-battery
boundedness assumptions. `square`

## 13. Paper-10 Pass Theorem

### Theorem 13.1: Projective Non-Abelian Gauge Cutoff Control

Under Hypotheses PC and KCOMP, and under the finite-battery boundedness
assumptions stated above, the `SU(2)` Peter-Weyl cutoff architecture gives:

1. finite declared gauge-invariant batteries at each cutoff;
2. cutoff-stable Gauss sectors and boundary centers;
3. projective maps preserving gauge data up to explicit residuals;
4. heat-bath reference-kernel inverse control;
5. projective comparison-map transfer;
6. projective exchange-defect transfer;
7. a smooth-background non-Abelian field-strength target for charged exchange
   coefficients;
8. a finite-battery Yang-Mills target conditional on YM-LIM;
9. a standard-facing finite Wilson gauge-matter target;
10. exact two-dimensional heat-kernel blocking;
11. exact one-step projectivity for finite-battery perfect blocks;
12. a concrete four-dimensional finite local-RG battery and local ansatz
    family;
13. a response-rank criterion identifying when local operators span the
    tested directions;
14. a finite-battery local projection theorem with explicit perpendicular,
    quadratic, and tail errors;
15. propagation of the local residual into `J_R` and `E_{R,S}` estimates;
16. diagnostic missing-direction examples for scalar, charged, Wilson-matter,
    and no-Wilson taste/detail batteries;
17. a local ansatz completion rule and iterative finite-battery RG closure
    algorithm;
18. first tiny-battery closure theorems for scalar loops, charged curvature,
    and Wilson matter source contractions;
19. a branch outcome table separating closure, enrichment, and obstruction
    cases;
20. a Gamma-only no-go theorem for full non-Abelian gauge reconstruction;
21. Wilson/no-Wilson branch typing through the same gauge projective layer;
22. a finite dynamical-matter boundary that does not overclaim QCD;
23. a projective continuum audit separating exact finite same-record
    pushforward from the conditional cofinal continuum tower.

### Proof

Items 1-2 are Sections 3-4. Item 3 is Theorem 5.1. Item 4 is Theorem 6.1.
Items 5-6 are Theorem 7.1 and Corollary 7.2. Item 7 is Theorems 8.1-8.2. Item
8 is Theorem 9.3. Item 9 is Definition 9.4 and Lemma 9.5. Items 10-17 are
Section 10, especially Theorems 10.1, 10.5, 10.10, 10.12, Lemma 10.9A,
Corollary 10.11, Diagnostic Examples 10.13, Rule 10.14, and Algorithm 10.15.
Items 18-19 are Theorems 10.16-10.18 and Table 10.19. Item 20 is Theorem
11.2. Items 21-22 are Section 12 and Theorem 12.1. Item 23 is Section 2A.
`square`

## 14. Honest Boundary

This paper proves a projective finite-battery non-Abelian gauge cutoff
framework.

It does not prove:

```text
continuum Yang-Mills measure existence;
an unconditional same-record whole-process tower;
projective tightness and uniqueness;
renormalization-group fixed points;
mass gap;
Wilson-loop area law;
confinement;
OS/Wightman reconstruction;
BRST or gauge-fixed continuum quantization;
QCD;
Gamma-only gauge-field reconstruction.
```

The precise status is:

```text
finite S_3 benchmark: Paper 9;
SU(2) Peter-Weyl finite-battery projective gauge layer: Paper 10;
same-record projective tower: finite records and exact one-step perfect-block
  pushforward proved; cofinal continuum tower conditional on PC/KCOMP/RG-D or
  perfect-block replacement, tightness, uniqueness, and YM-LIM;
smooth-background field-strength target: Paper 10;
2D heat-kernel blocking: exact finite theorem;
higher-dimensional perfect finite-battery blocking: exact but generally nonlocal;
higher-dimensional local Wilson/heat-kernel renormalization: finite-battery
  projection estimate proved under response-rank and tail-control conditions;
local-RG closure: iterative finite-battery algorithm with completion/obstruction rule;
tiny-battery closure tests: scalar loops close under rank, charged curvature
  requires charged instruments, Wilson matter requires Wilson-matter
  operators, no-Wilson detail requires recorded taste/detail handling;
Gamma-only gauge reconstruction: no-go;
finite dynamical matter: declared normalized functional; positive only under
  an explicitly nonnegative prescription;
full non-Abelian continuum QFT: not yet.
```

### Final Theorem Ledger

| Layer | Paper 10 status | What is proved | What remains open |
| --- | --- | --- | --- |
| Finite gauge endpoint layer | Theorem-level | `SU(2)` Peter-Weyl finite batteries, Gauss projection, boundary centers, and cutoff stability | Full continuum local algebra |
| Projective gauge maps | Conditional theorem-level | Projective stability under PC/KCOMP with explicit residuals | Unconditional higher-dimensional refinement compatibility |
| Same-record tower | Conditional audit | Exact finite perfect-block pushforward and typed record discipline | Cofinal tightness, uniqueness, and continuum compatibility |
| Reference inverse control | Theorem-level | Uniform finite-battery inverse for the heat-bath reference kernel | Continuum inverse domains |
| Comparison maps and exchange defects | Conditional theorem-level | `J_R` and `E_{R,S}` transfer once primitive residuals and inverse residuals are controlled | Nonperturbative all-battery residual bounds |
| Smooth non-Abelian curvature | Theorem-level target | Charged plaquette transport has `a^2F_{\mu\nu}` smooth-background limit | Gauge-field measure-level curvature reconstruction |
| Scalar Yang-Mills battery | Conditional target | Heat-kernel finite-lattice measure is admissible; YM-LIM would give finite-battery Yang-Mills interface | Continuum Yang-Mills existence, OS/Wightman reconstruction, mass gap |
| Two-dimensional RG | Exact theorem | Heat-kernel plaquette blocking gives `K_t*K_s=K_{t+s}` and zero scalar residual | Extension of exact locality to `d>=3` |
| Perfect higher-dimensional blocking | Exact theorem | Whole-process pushforward gives zero finite-battery residual in any dimension | The perfect block is generally nonlocal |
| Local higher-dimensional RG | Finite-battery theorem plus gate | Response-rank/local-projection theorem, `delta_locRG` bound, completion rule, closure algorithm | Showing the residuals vanish along a continuum scaling path |
| Tiny-battery closure | Theorem-level finite tests | Scalar loops close under covariance rank; charged curvature needs charged instruments; Wilson matter needs matter operators | Large batteries, thermodynamic limits, continuum scaling |
| Wilson/no-Wilson split | Typed finite theorem | Both branches pass through the gauge layer when their extra labels are declared | Wilson continuum limit, no-Wilson multi-taste continuum interpretation |
| Dynamical matter | Finite operational boundary | Declared determinant/reweighting prescriptions define normalized functionals when integrable | Continuum QCD, positivity/sign control, anomaly/chiral bookkeeping |
| Gamma-only reconstruction | No-go theorem | Scalar Gamma gauge data cannot reconstruct framed charged holonomies or full connection | Enriched operational reconstruction only |

The honest one-line conclusion is:

```text
Paper 10 proves finite-battery non-Abelian cutoff/RG control, defines the
same-record projective tower data, and exposes the local-action/tightness
continuum gates; it does not prove continuum Yang-Mills, QCD, area law, mass
gap, or confinement.
```

## 15. Export To Paper 11

Paper 11 may use Paper 10 to say:

1. the V3 program has a finite non-Abelian gauge benchmark;
2. it has a projective Peter-Weyl finite-battery `SU(2)` gauge layer;
3. it has explicit Gauss/boundary-center preservation;
4. it has inverse-control and comparison-map transfer conditional on named
   residual estimates;
5. it has a smooth-background field-strength target for charged exchange
   coefficients;
6. it has an exact two-dimensional heat-kernel blocking theorem;
7. it has exact finite-battery perfect blocking in any dimension;
8. it has a concrete four-dimensional finite local-RG battery and local
   coarse ansatz;
9. it has a response-rank criterion and finite-battery local projection
   estimate for the local-action residual;
10. it has diagnostic examples and a local ansatz completion algorithm;
11. it has first tiny-battery closure theorems and a branch outcome table;
12. it propagates that residual into comparison-map and exchange-defect
    estimates;
13. it has a finite Wilson gauge-matter target and a finite dynamical-matter
    boundary;
14. it has a Gamma-only no-go theorem for full charged gauge reconstruction;
15. it has a projective continuum audit: same-record perfect-block
    pushforward is exact on a fixed finite battery, while a cofinal continuum
    tower remains conditional on compatibility, tightness, uniqueness, and
    scaling gates.

Paper 11 may not say:

```text
V3 has reconstructed full non-Abelian QFT;
V3 has constructed an unconditional same-record continuum gauge tower;
V3 has derived Yang-Mills from bare Gamma;
V3 has proved Yang-Mills existence, mass gap, area law, or confinement;
V3 has proved QCD;
V3 has erased the distinction between Wilson and no-Wilson branches.
```
