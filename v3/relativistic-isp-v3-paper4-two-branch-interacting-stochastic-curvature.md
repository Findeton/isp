# Detail-Sector Options And Interacting Stochastic Curvature In Relativistic ISP

Author: Felix Robles Elvira

V3 Paper 4 draft

Date: 2026-05-18

Status: theorem-level first pass. This paper imports the projective-kernel,
detail-preserving, Wilson, staggered, and operational-interface contract from
V3 Paper 3. It advances the two main dynamical branches:

```text
detail-preserving + Wilson:
  single-species finite-energy branch, with Wilson detail modes decoupled;

detail-preserving + no Wilson:
  staggered/multi-taste branch, with detail modes interpreted as tastes.
```

The goal is not to prove full interacting continuum QFT. The goal is narrower:
show that the exchange-defect/stochastic-curvature mechanism survives a
controlled interaction in the Wilson and no-Wilson branches, while also
laying out the operational-projection and dynamical-taste-breaking options
needed for an exhaustive Barandes-aligned detail-sector analysis.

## 1. Import Contract From Paper 3

Paper 3 exports the following facts.

1. `J_R`, `J_R^{-1}`, and `E_{R,S}` are algebraic relative-dynamics maps.
2. Projective transfer for `J_R`, `J_R^{-1}`, and `E_{R,S}` holds under the
   declared readouts.
3. The naive all-mode dyadic marginal fails at fixed nonzero `Delta/a`.
4. The detail-preserving all-mode readout works:
   ```text
   2n     -> (n,0),
   2n + 1 -> (n,1).
   ```
5. The Wilson branch gives a single-species finite-energy route when the
   Wilson detail sector has an `O(1/a)` gap and the interaction is
   Wilson-admissible.
6. The no-Wilson branch is a staggered/multi-taste route.
7. Raw `J_R` and `E_{R,S}` become measurable only after compatible
   instruments/effects are declared.

This paper may not use:

```text
full interacting renormalized QFT;
full Lorentz covariance;
non-Abelian gauge stability;
operational observability of raw J_R or E_{R,S};
derivation of Fock/local-field representation data from bare Gamma alone.
```

## 2. Detail-Sector Ontology Principle

The detail label introduced by the all-mode readout is not disposable
notation. It is part of the declared finite state description. Therefore this
paper imposes the following Barandes-aligned rule.

```text
No detail degree of freedom may be erased silently.

It must be:
  retained as physical data;
  made dynamically inaccessible by a declared mechanism;
  projected by a declared operational instrument with its rejected sector
  accounted for;
  or shown redundant by an exact equivalence.
```

This rule is not aesthetic. It is the difference between a projective ISP
theorem and an undeclared change of ontology.

### The Four Detail-Sector Options

At fixed nonzero `Delta/a`, the detail-preserving regulator leads to four
honest options.

```text
Option A: Wilson mass removal
  Retain the detail label at finite cutoff, add a declared Wilson term, and
  prove that finite-energy tests cannot excite the detail/doubler sector.

Option B: no-Wilson multi-taste retention
  Retain the detail label as physical taste/species data. The continuum target
  is multi-taste unless further structure is declared.

Option C: operational taste projection
  Retain the detail label in the underlying process, but declare an
  instrument/effect that accepts only a chosen taste sector and records or
  conditions on the rejected sector.

Option D: dynamical taste-breaking or taste-splitting
  Retain the detail label and add a declared interaction that splits, mixes,
  or masses taste sectors. Hidden or visible sectors are then determined by
  that dynamics, not by silent erasure.
```

All four can be Barandes-aligned if the relevant operation is declared and its
effect is proved. The non-Barandes-aligned move is:

```text
identify detail states, drop the rejected information, and still call the
result all-mode single-species QFT.
```

Paper 3 already ruled out that move mathematically for the naive dyadic
marginal.

## 3. Common Interacting Curvature Setup

Let `b` be a branch label:

```text
b = W   Wilson single-species finite-energy branch,
b = st  staggered multi-taste branch.
b = pr  operational taste-projected branch,
b = tb  dynamical taste-breaking branch.
```

At lattice spacing `a`, let `F_a^b` be the declared finite-volume,
finite-particle branch space. For compactly supported lapse profiles `N,M`,
write `N_n=N(an)`, `M_n=M(an)`.

For a local region `R`, let

```math
J_{R,b}(g,\Delta)
```

be the exact branch comparison map for a coupling `g`, and assume its
relative-cumulant logarithm has the local even-onset expansion

```math
L_{R,b}(g,\Delta)
:=
\log J_{R,b}(g,\Delta)
=
\Delta^2 A_{R,b}(g)+O(\Delta^4)
```

on the tested branch domain. For singleton `R_n={n}`, define the coefficient
smooth-lapse deformation

```math
{\mathcal K}_{a,b}[N;g]
=
a\sum_n N_n A_{n,b}(g).
```

The coefficient-level interacting stochastic curvature is

```math
{\mathfrak C}_{a,b}[N,M;g]
=
[{\mathcal K}_{a,b}[N;g],{\mathcal K}_{a,b}[M;g]].
```

This is the correct coefficient object behind the first visible exchange
defect:

```math
E_{N,M,b}(g,\Delta)
=
I+\Delta^4{\mathfrak C}_{a,b}[N,M;g]+O(\Delta^6)
```

whenever the smooth-lapse product is built from the local coefficient package.

## 4. Interaction Hypothesis ICURV

For a branch `b`, the interacting coefficient package satisfies Hypothesis
ICURV if:

1. **Locality.** Each `A_{n,b}(g)` is supported in a fixed lattice
   neighborhood of `n`, uniformly for small `a` and bounded `g`.
2. **Perturbative interaction expansion.**
   ```math
   A_{n,b}(g)
   =
   A_{n,b}^{(0)}
   +gB_{n,b}
   +g^2D_{n,b}(g),
   ```
   with uniform tested-domain bounds after smooth-lapse smearing.
3. **Free curvature limit.**
   ```math
   [{\mathcal K}_{a,b}^{(0)}[N],
    {\mathcal K}_{a,b}^{(0)}[M]]
   \to
   K_{\parallel,b}[N\partial_xM-M\partial_xN].
   ```
   For `b=W`, this is the single-species Dirac target. For `b=st`, it is the
   corresponding two-taste target.
4. **Mixed interaction limits.** The following strong limits exist on the
   declared smooth finite test domain:
   ```math
   {\mathfrak C}_{b}^{(1)}[N,M]
   =
   \lim_{a\to0}
   \left(
   [{\mathcal K}_{a,b}^{(0)}[N],{\mathcal B}_{a,b}[M]]
   +
   [{\mathcal B}_{a,b}[N],{\mathcal K}_{a,b}^{(0)}[M]]
   \right),
   ```
   where
   ```math
   {\mathcal B}_{a,b}[N]=a\sum_nN_nB_{n,b}.
   ```
5. **Pure interaction limits.**
   ```math
   {\mathfrak C}_{b}^{(2)}[N,M]
   =
   \lim_{a\to0}
   [{\mathcal B}_{a,b}[N],{\mathcal B}_{a,b}[M]]
   ```
   exists, and the `D_{n,b}(g)` remainders are controlled at the order stated
   in the theorem.

This hypothesis is intentionally explicit. It prevents the paper from hiding
the hard interacting estimate inside the word "local".

## 5. Deriving ICURV From The Primitive Born-Squared Kernel

ICURV is not merely a formal assumption. At the first visible
`Delta^2` coefficient it can be derived from the primitive finite kernel

```math
\Gamma_H(\Delta)=\Gamma(e^{-i\Delta H}),
\qquad
(\Gamma(U))_{xy}=|U_{xy}|^2.
```

Let `X` be a finite configuration basis and let `H=H^\dagger`. Define the
Born transition coefficient `Q(H)` by

```math
Q(H)_{xy}=|H_{xy}|^2,\qquad x\ne y,
```

and

```math
Q(H)_{xx}=-\sum_{z\ne x}|H_{zx}|^2.
```

Then each column of `Q(H)` sums to zero.

### Lemma 5.1: Primitive `Delta^2` Kernel Coefficient

For fixed finite `X`,

```math
\Gamma_H(\Delta)=I+\Delta^2Q(H)+O(\Delta^3).
```

In the even-onset classes used by the earlier Dirac collar-excision papers,
the remainder improves to `O(\Delta^4)`, but the `Delta^2` coefficient is
always `Q(H)`.

### Proof

For `x\ne y`,

```math
(e^{-i\Delta H})_{xy}
=
-i\Delta H_{xy}+O(\Delta^2),
```

so

```math
|(e^{-i\Delta H})_{xy}|^2
=
\Delta^2|H_{xy}|^2+O(\Delta^3).
```

Column stochasticity of `\Gamma_H(\Delta)` determines the diagonal
coefficient:

```math
Q(H)_{xx}
=
-\sum_{z\ne x}Q(H)_{zx}.
```

This proves the claim. `square`

### Lemma 5.2: First Interaction Coefficient

Let

```math
H(g)=H^{(0)}+gV.
```

Then

```math
Q(H(g))
=
Q(H^{(0)})
+
g\,DQ_{H^{(0)}}(V)
+
g^2Q(V),
```

where, for `x\ne y`,

```math
(DQ_H(V))_{xy}
=
2{\rm Re}\left(\overline{H_{xy}}V_{xy}\right),
```

and the diagonal entries are again fixed by column-sum zero:

```math
(DQ_H(V))_{xx}
=
-\sum_{z\ne x}(DQ_H(V))_{zx}.
```

For a comparison map

```math
J_R(g,\Delta)
=
\Gamma_{H_R(g)}(\Delta)\Gamma_{H_0(g)}(\Delta)^{-1},
```

the `Delta^2` logarithmic coefficient is

```math
A_R(g)=Q(H_R(g))-Q(H_0(g)).
```

Therefore

```math
A_R(g)=A_R^{(0)}+gB_R+g^2D_R,
```

with

```math
B_R=
DQ_{H_R^{(0)}}(V_R)-DQ_{H_0^{(0)}}(V_0),
```

and

```math
D_R=Q(V_R)-Q(V_0).
```

This is ICURV items 1 and 2 whenever `H_R^{(0)}`, `H_0^{(0)}`, `V_R`, and
`V_0` have uniformly finite range and controlled local norms.

### Proof

For `x\ne y`,

```math
|H_{xy}+gV_{xy}|^2
=
|H_{xy}|^2
+
2g{\rm Re}(\overline{H_{xy}}V_{xy})
+
g^2|V_{xy}|^2.
```

The diagonal follows from column-sum zero. The comparison-map formula follows
from

```math
\Gamma_{H_R(g)}(\Delta)
\Gamma_{H_0(g)}(\Delta)^{-1}
=
\left(I+\Delta^2Q(H_R(g))+O(\Delta^3)\right)
\left(I-\Delta^2Q(H_0(g))+O(\Delta^3)\right),
```

and from the fact that `log(I+\Delta^2A+O(\Delta^3))` has the same
`Delta^2` coefficient `A`. `square`

### Corollary 5.3: Diagonal Interactions Are Invisible At Leading `Delta^2`

If `V` is diagonal in the declared configuration basis, then

```math
DQ_H(V)=0,
\qquad
Q(V)=0.
```

Hence

```math
A_R(g)=A_R^{(0)}
```

at the leading `Delta^2` coefficient level. A density-density interaction,
being diagonal in the occupation-number configuration basis, therefore has

```math
B_R=0,
\qquad
D_R=0
```

for this coefficient. It can affect stochastic curvature only through higher
small-slab coefficients, through a different declared interaction with
off-diagonal matrix elements, or through representation-level dynamics beyond
the leading `Delta^2` Born coefficient.

This is a constraint, not a problem: it says exactly what the primitive
Born-squared coefficient can and cannot see.

## 6. Diagonal Interactions Are Phase-Like Whole-Process Data

The preceding corollary is the first-principles point. A diagonal interaction
does not directly change a configuration. It changes the phase/action assigned
to a configuration while the process evolves. Therefore it should not appear
as an immediate transition intensity. It should appear only when a complete
process contains enough off-diagonal motion for that phase/action information
to interfere with another route.

This is exactly the Barandes-aligned reading:

```text
Do not smuggle phase-sensitive Hamiltonian data into Gamma at an order where
Gamma cannot see it.

Use the whole finite process, or the next coefficient where paths interfere.
```

The next theorem shows the precise delayed onset. It is deliberately stated as
a finite-cutoff coefficient theorem. Continuum limits, thermodynamic limits,
and QFT reconstruction are not hidden inside the notation; they are separate
branch hypotheses later in the paper.

### Theorem 6.1: `Delta^4` Delayed-Onset Coefficient For Diagonal `V`

Fix one finite cutoff configuration space `X_a`. Let `H` be the bounded
Hermitian matrix that generates the declared finite process on `X_a`, let
`V` be a bounded diagonal perturbation in the same declared configuration
basis, and set

```math
H(g)=H+gV,
```

with `V` diagonal in the declared configuration basis:

```math
V_{xy}=v_x\delta_{xy}.
```

For `x\ne y`, write

```math
U_{xy}(\Delta,g)
=
\left(e^{-i\Delta H(g)}\right)_{xy}.
```

Then the linear-in-`g` part of `|U_{xy}(\Delta,g)|^2` has no `Delta^2` or
`Delta^3` term. Its first possible contribution is at order `Delta^4`:

```math
\left.
\frac{d}{dg}|U_{xy}(\Delta,g)|^2
\right|_{g=0}
=
\Delta^4\,{\mathcal D}^{(4)}_{H,V}(x,y)
+
O(\Delta^5),
```

where the remainder is uniform for `|g|<=g_*` and `0<=Delta<=Delta_*` on this
finite cutoff, with a bound depending only on

```math
\|H\|,\qquad \|V\|,\qquad g_*,\qquad |X_a|.
```

Equivalently, in the off-diagonal entrywise norm,

```math
\left|
\left.
\frac{d}{dg}|U_{xy}(\Delta,g)|^2
\right|_{g=0}
-
\Delta^4{\mathcal D}^{(4)}_{H,V}(x,y)
\right|
\le
C_{a,H,V}\Delta^5.
```

The coefficient is

```math
{\mathcal D}^{(4)}_{H,V}(x,y)
=
\frac12
{\rm Re}
\left(
\overline{(H^2)_{xy}}\,(v_x+v_y)H_{xy}
\right)
-
\frac13
{\rm Re}
\left(
\overline{H_{xy}}\,
\left[
(v_x+v_y)(H^2)_{xy}
+
\sum_z H_{xz}v_zH_{zy}
\right]
\right).
```

Equivalently,

```math
{\mathcal D}^{(4)}_{H,V}(x,y)
=
\frac16(v_x+v_y)
{\rm Re}\left(\overline{(H^2)_{xy}}H_{xy}\right)
-
\frac13
{\rm Re}
\left(
\overline{H_{xy}}\sum_zH_{xz}v_zH_{zy}
\right).
```

The diagonal entries are fixed by column-sum zero:

```math
{\mathcal D}^{(4)}_{H,V}(y,y)
=
-
\sum_{x\ne y}{\mathcal D}^{(4)}_{H,V}(x,y).
```

This diagonal completion is part of the stochastic-kernel coefficient, not an
extra Hamiltonian assertion. It says that the delayed coefficient preserves
normalization column by column.

### Proof

For `x\ne y`, expand the amplitude:

```math
U_{xy}
=
\Delta a_1+\Delta^2a_2+\Delta^3a_3+O(\Delta^4),
```

with

```math
a_1=-iH_{xy},
\qquad
a_2=-\frac12(H^2)_{xy},
\qquad
a_3=\frac{i}{6}(H^3)_{xy}.
```

The expansion is the ordinary finite-matrix exponential expansion. Since
`H(g)` is uniformly bounded for `|g|<=g_*`, the remainder and its first
`g`-derivative are bounded in operator norm by constants times `Delta^4`.
Multiplying by the leading `O(Delta)` off-diagonal amplitude gives a
`Delta^5` remainder for the derivative of the Born-squared entry.

Thus

```math
|U_{xy}|^2
=
\Delta^2|a_1|^2
+
2\Delta^3{\rm Re}(\overline{a_1}a_2)
+
\Delta^4\left(|a_2|^2+2{\rm Re}(\overline{a_1}a_3)\right)
+
O(\Delta^5).
```

Because `V` is diagonal, `dH_{xy}/dg=0` for `x\ne y`, so the `Delta^2`
variation vanishes. Also

```math
\left.\frac d{dg}(H(g)^2)_{xy}\right|_{g=0}
=
(v_x+v_y)H_{xy}.
```

The `Delta^3` variation is proportional to

```math
{\rm Re}\left(
i\overline{H_{xy}}(v_x+v_y)H_{xy}
\right)=0.
```

At order `Delta^4`,

```math
\left.\frac d{dg}(H(g)^3)_{xy}\right|_{g=0}
=
(v_x+v_y)(H^2)_{xy}
+
\sum_zH_{xz}v_zH_{zy}.
```

Differentiating

```math
\frac14 |(H^2)_{xy}|^2
-
\frac13{\rm Re}\left(\overline{H_{xy}}(H^3)_{xy}\right)
```

gives the displayed expression. Column-sum zero follows from stochastic
normalization of the full Born-squared kernel. `square`

### Corollary 6.2: Delayed Coefficient For Comparison Maps

Let

```math
J_R(g,\Delta)
=
\Gamma_{H_R(g)}(\Delta)\Gamma_{H_0(g)}(\Delta)^{-1},
```

where `H_R(g)=H_R+gV_R` and `H_0(g)=H_0+gV_0`, with `V_R,V_0` diagonal.
Since the `Delta^2` interaction coefficient vanishes, the first
linear-in-`g` diagonal interaction coefficient of `J_R` at delayed order is

```math
B_{R}^{(4),diag}
=
{\mathcal D}^{(4)}_{H_R,V_R}
-
{\mathcal D}^{(4)}_{H_0,V_0}
```

up to branch-independent terms already present in the free `Delta^4`
comparison coefficient. Thus density-density interactions enter the
stochastic comparison-map curvature through a delayed coefficient, not through
the leading transition-intensity coefficient.

### Proof

Multiply the two expansions

```math
\Gamma_{H_R(g)}(\Delta)
```

and

```math
\Gamma_{H_0(g)}(\Delta)^{-1}.
```

The linear-in-`g` `Delta^2` term is zero by Corollary 5.3, so no inverse
cross-term containing a `Delta^2` interaction coefficient appears. The first
linear diagonal-interaction term is therefore the difference of the two
`Delta^4` delayed coefficients. `square`

### Corollary 6.3: Density-Density Local Path Formula

For a density-density interaction in an occupation basis,

```math
V_x
=
\sum_j\eta_j\,\rho_j(x)\rho_{j+1}(x),
```

the delayed coefficient for an off-diagonal transition `y\to x` is

```math
{\mathcal D}^{(4)}_{H,V}(x,y)
=
\frac16(V_x+V_y)
{\rm Re}\left(\overline{(H^2)_{xy}}H_{xy}\right)
-
\frac13
{\rm Re}
\left(
\overline{H_{xy}}\sum_zH_{xz}V_zH_{zy}
\right).
```

The first term samples the interaction energy at the endpoints of the jump;
the second samples the interaction energy of intermediate configurations
`z` along two-step paths `y\to z\to x`. Hence density-density interactions
are visible exactly as whole-process path-interference data.

### Proof

Substitute the occupation-basis diagonal value `v_x=V_x` into Theorem 6.1.
Locality follows because finite-range `H` permits only finitely many
intermediate configurations `z` in the two-step sum. `square`

### Hypotheses ICURV-2 And ICURV-4

The branch analysis now separates two cases.

```text
ICURV-2:
  off-diagonal interactions contribute at the leading Delta^2 comparison
  coefficient through B_R = DQ_H(V).

ICURV-4:
  diagonal phase-like interactions have B_R=0 at Delta^2 and first contribute
  through the delayed Delta^4 coefficient B_R^{(4),diag}.
```

The theorem chain used in this paper is therefore:

```text
finite whole-process amplitude e^{-iDelta H}
-> Born-squared finite-process kernel Gamma
-> single-slab comparison map J_R
-> exchange defect of declared comparison maps
-> continuum limit only after branch-specific estimates.
```

No step composes unobserved partial kernels as if the underlying process were
Markov-divisible. The algebraic commutators below are commutators of declared
comparison maps/coefficient operators, not a hidden assumption that the
finite-slab stochastic kernel factors through unrecorded intermediate states.

Paper 4 must therefore not advertise diagonal density-density curvature as a
leading `Delta^2` effect. Its correct first-principles status is delayed
whole-process curvature.

### Physics Meaning

```text
ISP does not ignore diagonal density-density interactions.

It refuses to treat them as immediate transition intensities.

They are phase/action interactions. They become visible when a whole process
contains configuration-changing paths whose amplitudes can interfere.
```

In standard Hamiltonian language, a diagonal potential is obviously present in
`H`. In a Born-squared ISP kernel, its first primitive signature is subtler:
it is not `|V_{xy}|^2` because there is no off-diagonal transition `x<-y`.
Its signature is the delayed path expression in Theorem 6.1, where endpoint
and intermediate interaction energies alter the probability of a complete
transition. This is the Einstein/Barandes lesson of the calculation: ask what
the whole observable process can reveal, not what a formal generator seems to
contain before the process is specified.

## 7. Theorem 7.1: Branchwise Interacting Curvature Expansion

Assume Hypothesis ICURV for branch `b`. Then on the declared smooth finite
test domain,

```math
{\mathfrak C}_{a,b}[N,M;g]
\to
K_{\parallel,b}[N\partial_xM-M\partial_xN]
+
g{\mathfrak C}_{b}^{(1)}[N,M]
+
g^2{\mathfrak C}_{b}^{(2)}[N,M]
+
R_b(g;N,M),
```

where `R_b(g;N,M)=O(g^2\|D_b(g)\|)+O(g^3)` in the tested topology. If
`D_{n,b}(g)=O(1)` uniformly for bounded `g`, this is a valid small-coupling
interacting stochastic-curvature theorem through first order in `g`, and a
second-order theorem whenever the pure interaction limit is controlled.

### Proof

Insert

```math
{\mathcal K}_{a,b}[N;g]
=
{\mathcal K}_{a,b}^{(0)}[N]
+
g{\mathcal B}_{a,b}[N]
+
g^2{\mathcal D}_{a,b}[N;g]
```

into the commutator. Bilinearity gives

```math
[K_0+gB+g^2D,K_0'+gB'+g^2D']
=
[K_0,K_0']
+
g([K_0,B']+[B,K_0'])
+
g^2([B,B']+[K_0,D']+[D,K_0'])
+
O(g^3).
```

The free, mixed, and pure interaction terms converge by ICURV. The terms
containing `D` are exactly the stated remainder. `square`

## 8. Option A: Wilson Branch - Density Interaction And Curvature

The Wilson branch uses the detail-preserving regulator plus a Wilson mass
term. Let `P_a` be the finite-particle physical projector and `Q_a=1-P_a` the
detail-containing block. Let the Wilson gap be `G_a>=c/a`.

### Wilson Density-Density Benchmark

On the finite-particle cutoff define the bounded local density

```math
\rho_n=\sum_\sigma c_{n,\sigma}^{\dagger}c_{n,\sigma},
```

and take a compactly supported profile `eta` with

```math
V_a^{dd}
=
g\,a\sum_n \eta(an):\rho_n\rho_{n+1}:.
```

On every fixed finite-particle sector, `\rho_n` is bounded, the interaction
range is finite, and

```math
\|V_a^{dd}\|_{\le N,E,O}=O_{N,E,O,g}(1).
```

Because the Wilson gap is `O(1/a)`,

```math
\|Q_aV_a^{dd}Q_a\|=O(1)\ll G_a,
\qquad
a\|Q_aV_a^{dd}P_a\|\to0.
```

Thus this density-density benchmark is Wilson-admissible in the sense of Paper
3.

### Theorem 8.1: Wilson ICURV And Mixed Curvature

For the Wilson density-density benchmark above, the primitive leading
coefficient derivation gives

```math
B_{R,W}^{dd}=0,
\qquad
D_{R,W}^{dd}=0
```

at the `Delta^2` Born-squared coefficient level. Therefore

```math
{\mathfrak C}_{W}^{(1)}[N,M]=0,
\qquad
{\mathfrak C}_{W}^{(2)}[N,M]=0
```

for the coefficient curvature built from `A_{R,W}(g)`.

Consequently,

```math
{\mathfrak C}_{a,W}^{dd}[N,M;g]
=
{\mathfrak C}_{a,W}^{(0)}[N,M]
```

at this leading coefficient scope. Nontrivial density-density interaction
curvature must be sought at the next small-slab coefficient, or through a
declared off-diagonal interaction such as hopping modulation, current
coupling, pair hopping, or taste-mixing.

### Proof

The density-density interaction is diagonal in the occupation-number
configuration basis. Corollary 5.3 gives `B=D=0` for every local comparison
coefficient. The mixed curvature is linear in `B`, and the pure leading
interaction curvature is built from `B` and `D`; hence both vanish at this
scope. `square`

### Theorem 8.2: Wilson Delayed Density-Density Curvature

For the Wilson density-density benchmark, define the delayed local coefficient

```math
B_{R,W}^{(4),dd}
=
{\mathcal D}^{(4)}_{H_{R,W}^{(0)},V_{R,W}^{dd}}
-
{\mathcal D}^{(4)}_{H_{0,W}^{(0)},V_{0,W}^{dd}}.
```

For smooth lapse `N`, set

```math
{\mathcal B}_{a,W}^{(4),dd}[N]
=
a\sum_nN_nB_{n,W}^{(4),dd}.
```

Then the first linear density-density contribution to the Wilson exchange
defect is delayed from the free `Delta^4` exchange coefficient to the mixed
`Delta^6` coefficient:

```math
{\mathfrak C}_{a,W}^{(dd,del)}[N,M]
=
[{\mathcal K}_{a,W}^{(0)}[N],{\mathcal B}_{a,W}^{(4),dd}[M]]
+
[{\mathcal B}_{a,W}^{(4),dd}[N],{\mathcal K}_{a,W}^{(0)}[M]].
```

If this expression has a strong continuum limit on Wilson smooth tests, then
the density-density interaction contributes to stochastic curvature through
that delayed limit, while Wilson detail-sector corrections remain suppressed
by the Wilson gap on finite-energy tests.

### Proof

The comparison map has the schematic form

```math
J_R^{dd}(g,\Delta)
=
I+\Delta^2A_R^{(0)}
+
g\Delta^4B_{R,W}^{(4),dd}
+
O(\Delta^4_{\rm free})+O(g\Delta^5)+O(g^2).
```

In a group commutator, the free term `[Delta^2A_N,Delta^2A_M]` appears at
`Delta^4`. The first linear diagonal-interaction term is the mixed commutator
between `Delta^2A^{(0)}` and `gDelta^4B^{(4),dd}`, hence appears at
`gDelta^6` with the displayed coefficient. The Wilson gap suppresses detail
blocks by the same Feshbach argument used for the Wilson branch in Paper 3 and
Theorem 8.3 below. `square`

### Theorem 8.3: Wilson Off-Diagonal Interacting Curvature Theorem

Let `V_W^{off}` be a Wilson-admissible finite-range interaction with
off-diagonal matrix elements in the declared configuration basis. Let

```math
H_{a,W,\rm eff}^{\rm phys}(z)
=
P_aH_{a,W}P_a
-
P_aH_{a,W}Q_a
\left(Q_a(H_{a,W}-z)Q_a\right)^{-1}
Q_aH_{a,W}P_a
```

be the Wilson Feshbach effective physical dynamics on the tested physical
resolvent set. Let `A_{n,W}^{\rm eff}(g)` be the `Delta^2` comparison
coefficient obtained from the physical comparison map generated by
`H_{a,W,\rm eff}^{\rm phys}(z)`, and assume this coefficient has a tested
continuum limit after Wilson smearing. Define

```math
B_{n,W}^{off}
=
DQ_{H_{n,W}^{(0)}}(V_{n,W}^{off})
-
DQ_{H_{0,W}^{(0)}}(V_{0,W}^{off}).
```

If the smeared mixed expression

```math
[{\mathcal K}_{a,W}^{(0)}[N],{\mathcal B}_{a,W}^{off}[M]]
+
[{\mathcal B}_{a,W}^{off}[N],{\mathcal K}_{a,W}^{(0)}[M]]
```

has a strong continuum limit on Wilson smooth tests, then

```math
P_a{\mathfrak C}_{a,W}[N,M;g]P_a
\to
K_{\parallel,W}[\beta]
+
g{\mathfrak C}_{W}^{(1)}[N,M]
+
g^2{\mathfrak C}_{W}^{(2)}[N,M],
```

with

```math
\beta=N\partial_xM-M\partial_xN.
```

The detail-sector correction obeys

```math
\left\|
P_a{\mathfrak C}_{a,W}[N,M;g]P_a
-
[P_a{\mathcal K}_{a,W}[N;g]P_a,
 P_a{\mathcal K}_{a,W}[M;g]P_a]
\right\|
\le
C\,\kappa_N(a)\kappa_M(a),
```

where

```math
\kappa_N(a)=\|Q_a{\mathcal K}_{a,W}[N;g]P_a\|,
\qquad
\kappa_M(a)=\|Q_a{\mathcal K}_{a,W}[M;g]P_a\|.
```

For Wilson-admissible interactions, `\kappa_N(a),\kappa_M(a)\to0` on the
tested finite-energy domain. Hence Wilson detail modes do not contribute to
the visible interacting stochastic curvature.

The point is decoupling, not forgetting. The full finite process still has the
detail block; the theorem only says that the declared finite-energy Wilson
tests cannot excite it in the continuum limit.

### Proof

The identity

```math
P[K_N,K_M]P-[PK_NP,PK_MP]
=
PK_NQK_MP-PK_MQK_NP
```

is exact. Taking norms gives the displayed bound. Wilson-admissibility and the
gap/Feshbach estimate from Paper 3 imply the off-block quantities
`\kappa_N(a),\kappa_M(a)` vanish on the tested domain. The remaining
physical-block commutator converges by Theorem 7.1 applied to the effective
physical Wilson coefficients. `square`

## 9. Option B: No-Wilson Multi-Taste Retention

The staggered branch uses the same detail-preserving all-mode readout but does
not add a Wilson term. The detail label is a physical taste label.

This is the most direct Barandes-aligned branch because no retained detail
record is removed by hand and no later projection is smuggled in as a
primitive equivalence relation. The price is also explicit: the target is not
a one-taste theory unless an additional declared instrument or dynamics makes
it so. The branch is therefore judged by a two-taste continuum test class, not
by comparing it secretly to the Wilson physical block.

Let the two-taste density be

```math
\rho(x)=\rho_0(x)+\rho_1(x).
```

For a parity-blind density-density lattice interaction

```math
V_a^{st,dd}
=
g\,a\sum_n\eta(an):\rho_n\rho_{n+1}:,
```

the folded smooth continuum target is the two-taste interaction

```math
V_{\rm cont}^{st}
=
g\int \eta(x):(\rho_0(x)+\rho_1(x))^2:\,dx
```

on the finite smooth test domain, up to taste-oscillatory terms that vanish
for parity-blind smooth couplings. If the microscopic coupling contains a
nonvanishing alternating component, the corresponding taste-mixing continuum
term must be retained as physical data.

### Theorem 9.1: Staggered ICURV And Mixed Curvature

For the parity-blind staggered density-density interaction above,

```math
B_{R,st}^{dd}=0,
\qquad
D_{R,st}^{dd}=0
```

at the leading `Delta^2` Born-squared coefficient level. Hence

```math
{\mathfrak C}_{st}^{(1)}[N,M]=0,
\qquad
{\mathfrak C}_{st}^{(2)}[N,M]=0
```

for the coefficient curvature built from `A_{R,st}(g)`, and

```math
{\mathfrak C}_{a,st}[N,M;g]
\to
K_{\parallel,st}[\beta].
```

Here

```math
K_{\parallel,st}[\beta]
=
K_{\parallel}^{(0)}[\beta]\oplus K_{\parallel}^{(1)}[\beta]
```

is the two-taste tangential stochastic curvature operator. For parity-blind
diagonal interactions, the first interaction contribution is not visible at
this leading coefficient scope. For couplings with off-diagonal or alternating
components, use Theorems 9.2 and 9.3 below.

There is no Wilson-suppressed error term, because there is no Wilson gap. The
extra branch is not a regulator artifact in this theorem; it is part of the
declared physical target.

### Proof

Paper 3 proves that the no-Wilson detail-preserving branch converges to a
two-taste CAR representation. Folding the Brillouin zone decomposes smooth
test functions into the two taste sectors. A parity-blind local density
interaction is diagonal in the occupation basis, so Corollary 5.3 gives
`B=D=0`. Apply the free part of Theorem 7.1. `square`

### Theorem 9.2: Staggered Delayed Density-Density Curvature

For the staggered density-density benchmark, define

```math
B_{R,st}^{(4),dd}
=
{\mathcal D}^{(4)}_{H_{R,st}^{(0)},V_{R,st}^{dd}}
-
{\mathcal D}^{(4)}_{H_{0,st}^{(0)},V_{0,st}^{dd}}.
```

Fold this coefficient into taste space. It decomposes as

```math
B_{R,st}^{(4),dd}
=
B_{R,{\rm preserve}}^{(4),dd}
+
B_{R,{\rm mix}}^{(4),dd}.
```

Parity-blind smooth density couplings contribute to the taste-preserving
delayed curvature channel. Alternating microscopic components can contribute
to the taste-mixing delayed channel if they survive the folded continuum
limit.

There is no Wilson gap available to suppress the second term. Therefore the
Barandes-aligned alternatives are only:

```text
retain it as physical multi-taste curvature;
prove oscillatory averaging kills it on the declared smooth tests;
or declare an operational instrument that conditions it away with a recorded
reject sector.
```

The first linear density-density contribution to staggered exchange curvature
is

```math
{\mathfrak C}_{a,st}^{(dd,del)}[N,M]
=
[{\mathcal K}_{a,st}^{(0)}[N],{\mathcal B}_{a,st}^{(4),dd}[M]]
+
[{\mathcal B}_{a,st}^{(4),dd}[N],{\mathcal K}_{a,st}^{(0)}[M]],
```

and it appears at exchange order `gDelta^6`, not at the leading free
`Delta^4` exchange order.

### Proof

The delayed coefficient is Corollary 6.2 applied to the staggered branch.
Folding the Brillouin zone decomposes the coefficient into taste-preserving
and taste-mixing blocks. The group-commutator order count is identical to
Theorem 8.2: `Delta^2` free data commuted with `gDelta^4` delayed diagonal
data gives `gDelta^6`. `square`

### Theorem 9.3: Staggered Off-Diagonal Or Alternating Interaction Curvature

Let `V_{st}^{off}` be a declared finite-range staggered interaction with
off-diagonal matrix elements or a surviving alternating folded component.
Define

```math
B_{n,st}^{off}
=
DQ_{H_{n,st}^{(0)}}(V_{n,st}^{off})
-
DQ_{H_{0,st}^{(0)}}(V_{0,st}^{off}).
```

Decompose the folded coefficient into taste-preserving and taste-mixing
pieces:

```math
B_{n,st}^{off}
=
B_{n,{\rm preserve}}
+
B_{n,{\rm mix}}.
```

If the corresponding mixed smeared commutators have strong limits on the
two-taste smooth test domain, then

```math
{\mathfrak C}_{a,st}[N,M;g]
\to
K_{\parallel,st}[\beta]
+
g{\mathfrak C}_{st,{\rm preserve}}^{(1)}[N,M]
+
g{\mathfrak C}_{st,{\rm mix}}^{(1)}[N,M]
+
O(g^2).
```

The taste-mixing term vanishes for taste-blind/parity-blind tests only when
oscillatory averaging or a declared instrument annihilates it. Otherwise it is
a physical multi-taste curvature channel.

### Proof

The first interaction coefficient is Lemma 5.2. Folding the Brillouin zone
splits its finite stencil into taste-preserving and taste-mixing matrix
blocks. Applying Theorem 7.1 gives the mixed curvature expansion. The final
statement is the usual oscillatory/taste-instrument alternative: if the
folded phase oscillates against smooth parity-blind tests it vanishes; if it
is retained by the declared coupling or measured by a taste-resolving
instrument, it survives. `square`

## 10. Option C: Operational Taste Projection

Operational projection is not the same as Wilson decoupling. Wilson changes
the dynamics by adding a gap. Projection changes the operational question by
declaring which sector an instrument accepts.

Let `\Pi_{\tau_0}` be the taste-sector projector in the staggered branch. A
taste-selecting instrument is a family of effects

```math
{\mathcal I}_{a}^{\tau_0}
:
{\mathbb R}^{X_a^{st}}\to{\mathbb R}^{X_a^{st}}
```

with two declared outcomes:

```text
accept tau_0,
reject not tau_0.
```

At the QFT representation level, the accepted branch acts as

```math
{\mathcal I}_{a}^{\tau_0}\sim \Pi_{\tau_0}(\cdot)\Pi_{\tau_0}.
```

The reject outcome is not erased; it is either recorded, conditioned on, or
included in the normalization of the accepted statistics.

### Theorem 10.1: Projected ICURV And Mixed Curvature

Assume the staggered branch satisfies the ICURV conclusion of Theorem 9.1,
9.2, or 9.3, and that the taste-selecting instrument is projectively
compatible:

```math
\|{\mathcal I}_{b}^{\tau_0}-{\mathcal I}_{a}^{\tau_0}P_{ab}\|
\le
\delta_{\tau}^{ab}.
```

Then the accepted curvature channel satisfies

```math
{\mathcal I}_{a}^{\tau_0}
{\mathfrak C}_{a,st}[N,M;g]
{\mathcal I}_{a}^{\tau_0}
\to
\Pi_{\tau_0}
\left(
K_{\parallel,st}[\beta]
+
g{\mathfrak C}_{st}^{(1)}[N,M]
+
g^2{\mathfrak C}_{st}^{(2)}[N,M]
\right)
\Pi_{\tau_0}
```

on accepted tests. The discarded taste sector contributes to the reject
statistics. Therefore this route can reproduce a single selected taste only
as a conditional operational prediction, not as an all-mode single-species
claim.

At the coefficient level, the accepted first interaction coefficient is

```math
B_{n,pr}^{\tau_0}
=
\Pi_{\tau_0}B_{n,st}\Pi_{\tau_0},
```

with the complementary rejected coefficient

```math
B_{n,rej}^{\tau_0}
=
(1-\Pi_{\tau_0})B_{n,st}(1-\Pi_{\tau_0})
```

and possible cross terms if the instrument records coherent taste transitions.
Thus projection does not create a new primitive `B`; it conditions the
staggered coefficient package.

### Proof

Apply the compatible instrument to the staggered curvature theorem. Projective
compatibility controls the finite-cutoff mismatch by `\delta_\tau^{ab}`. In
the continuum representation, the accepted effect converges to
`\Pi_{\tau_0}` on both sides of the local polynomial. The complement
`1-\Pi_{\tau_0}` is the reject effect, so no state information is silently
discarded. `square`

## 11. Option D: Dynamical Taste-Breaking Or Taste-Splitting

Taste-breaking keeps the detail label but changes its dynamics. A typical
declared taste-breaking perturbation has the continuum folded form

```math
V_{\rm tb}
=
\int dx\,
\Psi^\dagger(x)
\left(
\mu(x)\tau_z+\nu(x)\tau_x
\right)
\Psi(x),
```

where `\tau_i` act on taste space. The `\tau_z` term splits the two tastes;
the `\tau_x` term mixes them.

### Theorem 11.1: Taste-Breaking ICURV And Mixed Curvature Channels

Assume the taste-breaking branch satisfies ICURV with

```math
B_{n,tb}=B_{n,{\rm taste\ preserving}}+B_{n,{\rm break}}.
```

For a primitive taste-breaking Hamiltonian perturbation

```math
V_{tb}=V_{\rm preserve}+V_{\rm break},
```

the two terms are computed from the Born-squared derivative:

```math
B_{n,{\rm preserve}}
=
DQ_{H_{n,st}^{(0)}}(V_{n,{\rm preserve}})
-
DQ_{H_{0,st}^{(0)}}(V_{0,{\rm preserve}}),
```

and

```math
B_{n,{\rm break}}
=
DQ_{H_{n,st}^{(0)}}(V_{n,{\rm break}})
-
DQ_{H_{0,st}^{(0)}}(V_{0,{\rm break}}).
```

Then

```math
{\mathfrak C}_{a,tb}[N,M;g]
\to
K_{\parallel,st}[\beta]
+
g{\mathfrak C}_{\rm preserve}^{(1)}[N,M]
+
g{\mathfrak C}_{\rm break}^{(1)}[N,M]
+
O(g^2).
```

The breaking term vanishes from taste-blind observables only if the declared
instrument and tested states annihilate the corresponding taste-off-diagonal
matrix elements. Otherwise it is a physical curvature channel.

If the taste-breaking term gives one taste a mass gap `M_a\to\infty` and the
off-block coupling satisfies `M_a^{-1}\|V_{\rm mix}\|\to0`, then the heavy
taste decouples by the same Feshbach argument as the Wilson branch. This is a
dynamical-removal route, not silent erasure.

### Proof

The first statement is Theorem 7.1 with the first-order coefficient split into
taste-preserving and taste-breaking parts. Taste-blind observables trace over
or project taste only by declared instruments; if the instrument does not
annihilate the off-diagonal taste matrix elements, the breaking contribution
survives. The heavy-taste statement is the Schur/Feshbach estimate with
`M_a` replacing the Wilson gap `G_a`. `square`

## 12. Theorem 12.1: Detail-Sector Option Comparison

The four detail-sector options have the same common projective trunk but
different continuum and operational targets.

1. **Common trunk.** Every viable option uses the detail-preserving all-mode
   readout, so the projective transfer estimates for `J_R`, `J_R^{-1}`, and
   `E_{R,S}` are inherited from Paper 3.
2. **Wilson visible target.** Wilson detail modes decouple from finite-energy
   tests. The visible curvature is single-species:
   ```math
   K_{\parallel,W}[\beta]+{\rm interaction\ corrections}.
   ```
3. **Staggered visible target.** Without Wilson, the detail label remains as
   taste. The visible curvature is multi-taste:
   ```math
   K_{\parallel,st}[\beta]+{\rm taste\ interaction\ corrections}.
   ```
4. **Agreement condition.** The two branches agree on a tested observable
   family only if all of the following are declared and proved:
   ```text
   the staggered instruments are taste-blind or taste-projected;
   the states occupy the corresponding selected taste sector;
   the interaction is taste-preserving on that sector;
   the Wilson physical interaction and the selected staggered interaction
   have the same continuum matrix elements.
   ```
5. **Difference condition.** If a measured instrument resolves taste, or if
   the staggered interaction has taste-mixing curvature, then the staggered
   branch predicts extra exchange-curvature channels absent from the Wilson
   single-species branch.
6. **Projection target.** Operational projection can reproduce a selected
   single-taste channel only conditionally on an accepted outcome. The reject
   outcome remains part of the process.
7. **Taste-breaking target.** Dynamical taste-breaking can split, mix, or
   decouple tastes only through a declared interaction. Extra curvature
   channels are physical unless removed by a proved gap or a declared
   instrument.

### Proof

The common trunk is exactly the detail-preserving transfer theorem of Paper 3.
The Wilson target follows from the Wilson gap and Theorems 8.1, 8.2, and 8.3.
The staggered target follows from Theorems 9.1, 9.2, and 9.3. The projection
target follows from Theorem 10.1. The taste-breaking target follows from
Theorem 11.1.
The agreement
condition is necessary because
Wilson removes the detail branch from finite-energy tests while staggered
keeps it as physical taste data. If an instrument can distinguish taste, or if
the interaction couples tastes, no single-species Wilson observable can equal
the full staggered observable without an additional declared projection or
identification. `square`

## 13. Branch Comparison Table

```text
Route                          Target                  Barandes status
----------------------------------------------------------------------------
Naive detail-erasing marginal   none/all-mode fails      not aligned
Wilson mass removal             single-species tests     aligned if declared
No-Wilson retention             multi-taste QFT          most direct retention
Operational taste projection    conditional one-taste    aligned if reject recorded
Dynamical taste-breaking        split/mixed/heavy taste  aligned if dynamics proved
```

Curvature consequences:

```text
Wilson:
  extra detail curvature channels are gap-suppressed from finite-energy tests.

No-Wilson multi-taste:
  extra taste curvature channels remain physical.

Operational projection:
  extra channels are absent only in the accepted conditional statistics.

Taste-breaking:
  extra channels become taste-splitting or taste-mixing curvature terms unless
  a heavy-taste gap proves decoupling.
```

Interaction visibility:

```text
Interaction type              First ISP curvature signature
---------------------------------------------------------------------------
off-diagonal finite-range      immediate Delta^2 coefficient DQ_H(V),
                               hence mixed exchange at gDelta^4;

diagonal density-density       no Delta^2 interaction coefficient,
                               delayed D^(4) path coefficient,
                               hence mixed exchange at gDelta^6;

Wilson detail channels         present in the finite process but invisible to
                               declared finite-energy tests only after the
                               Wilson gap/Feshbach estimate;

no-Wilson taste channels       physical channels unless oscillatory averaging
                               or a recorded instrument removes them.
```

## 14. Concrete Smooth-Core Estimates For The Two Hard Limits

The previous sections reduced the remaining analytic work to two estimates:

```text
1. an immediate off-diagonal mixed-curvature limit;
2. a delayed diagonal density-density gDelta^6 limit.
```

This section proves both on the declared smooth finite-particle cores imported
from Paper 3. The result is deliberately not an all-energy operator-norm
continuum QFT theorem. It is a tested-core theorem: enough to make Paper 4 a
positive interacting curvature result, but still honest about the later QFT
reconstruction burden.

### The Declared Smooth Core

Let `{\mathcal D}_W` be the Wilson finite-particle smooth core obtained by
CAR/Fock lifting the Wilson smearing maps `I_a^W` of Paper 3. Let
`{\mathcal D}_{st}` be the analogous two-taste staggered smooth core obtained
from `I_a^{st}`. On these cores Paper 3 gives, for every fixed `r` needed
below,

```math
H_{a,W}^r I_a^W\Psi
-
I_a^W H_W^r\Psi
\to0,
\qquad
H_{a,st}^r I_a^{st}\Psi
-
I_a^{st}H_{st}^r\Psi
\to0,
```

where `H_W` is the single-species Dirac/Fock target and `H_{st}` is the
two-taste Dirac/Fock target. In this section `r<=3`.

This is a smooth-core statement. It uses the declared smearing maps and is not
a claim that bare `Gamma` reconstructs the QFT domain by itself.

### Theorem 14.1: Concrete Off-Diagonal Mass-Channel Mixed Curvature Limit

Choose a Dirac internal basis in which the onsite mass matrix has an
off-diagonal part `\beta_{\rm off}` in the declared configuration basis. Let
`\mu\in C_c^\infty({\mathbb R})` be real and define the bounded one-particle
off-diagonal mass-channel perturbation

```math
(v_a^{\mu}u)_n=\mu(an)\beta_{\rm off}u_n,
\qquad
V_a^{\mu}=d\Gamma(v_a^{\mu}).
```

This is off-diagonal in the configuration basis but bounded on every fixed
finite-particle sector. Define the local stochastic-coefficient overlap matrix

```math
(\mathsf q_\beta)_{\sigma\tau}
=
2\,{\rm Re}
\left(
\overline{(m\beta_{\rm off})_{\sigma\tau}}
(\beta_{\rm off})_{\sigma\tau}
\right),
\qquad \sigma\ne\tau,
```

with diagonal entries completed by column-sum zero. Let `B_{n,b}^{\mu}` be the
first interaction
coefficient

```math
B_{n,b}^{\mu}
=
DQ_{H_{n,b}^{(0)}}(V_{n,b}^{\mu})
-
DQ_{H_{0,b}^{(0)}}(V_{0,b}^{\mu}),
\qquad
b\in\{W,st\}.
```

For smooth lapse `N`, set

```math
{\mathcal B}_{a,b}^{\mu}[N]
=
a\sum_nN(an)B_{n,b}^{\mu}.
```

Then, on the declared smooth core of branch `b`,

```math
{\mathcal B}_{a,b}^{\mu}[N]I_a^b\Psi
\to
I_a^b{\mathcal B}_{b,\rm cont}^{\mu}[N]\Psi,
```

where the continuum coefficient is the local coefficient-space multiplication
operator obtained from the overlap of the free onsite mass channel with
`\beta_{\rm off}`:

```math
{\mathcal B}_{b,\rm cont}^{\mu}[N]
=
\mathsf M_{N\mu\mathsf q_\beta}
```

in the Wilson branch, and the corresponding block-diagonal/taste-folded
operator in the staggered branch.

Moreover the mixed curvature has the strong smooth-core limit

```math
\begin{aligned}
&[{\mathcal K}_{a,b}^{(0)}[N],{\mathcal B}_{a,b}^{\mu}[M]]I_a^b\Psi
+
[{\mathcal B}_{a,b}^{\mu}[N],{\mathcal K}_{a,b}^{(0)}[M]]I_a^b\Psi
\\
&\qquad\to
I_a^b\left(
[K_b^{(0)}[N],{\mathcal B}_{b,\rm cont}^{\mu}[M]]
+
[{\mathcal B}_{b,\rm cont}^{\mu}[N],K_b^{(0)}[M]]
\right)\Psi .
\end{aligned}
```

Thus this off-diagonal interaction supplies a genuine immediate
`gDelta^4` interacting stochastic-curvature channel.

### Proof

The perturbation is bounded because it is a compactly supported multiplication
operator on the one-particle lattice space and its finite-particle lift has
norm bounded by the particle cutoff times `\|\mu\|_\infty\|\beta_{\rm off}\|`.
It has nonzero off-diagonal matrix elements in the declared configuration
basis, so Lemma 5.2 gives

```math
(DQ_H(V))_{xy}
=
2{\rm Re}(\overline{H_{xy}}V_{xy})
```

for `x\ne y`. Since `v_a^\mu` is onsite, the only free entries that contribute
to this benchmark are the onsite off-diagonal mass entries. Therefore
`B_{n,b}^{\mu}` is a uniformly bounded local multiplication stencil with
coefficient converging to the displayed continuum overlap.

The smooth-lapse sum is then a Riemann-sum approximation to multiplication by
`N\mu` on the declared smearing maps. Hence
`{\mathcal B}_{a,b}^{\mu}[N]` converges strongly on the smooth core. Paper 3
already gives strong graph convergence of
`{\mathcal K}_{a,b}^{(0)}[N]` to `K_b^{(0)}[N]` on the same core. Because
`{\mathcal B}_{a,b}^{\mu}[N]` is uniformly bounded and local, the two mixed
commutators converge by adding and subtracting the corresponding continuum
terms. `square`

### Theorem 14.2: Smooth-Core Delayed Density-Density Continuum Limit

Let `W_a^{dd}` be the coupling-free compactly supported normal-ordered
density-density interaction used in Theorems 8.2 and 9.2, so that the
Hamiltonian is perturbed as `H_a(g)=H_a^{(0)}+gW_a^{dd}`. Its continuum target
is

```math
W_{\rm cont}^{dd}
=
\int\eta(x):\rho(x)^2:\,dx
```

in the Wilson branch and the two-taste target

```math
W_{\rm cont}^{st,dd}
=
\int\eta(x):(\rho_0(x)+\rho_1(x))^2:\,dx
```

in the staggered branch. Define the finite-cutoff delayed coefficient

```math
B_{R,b}^{(4),dd}
=
{\mathcal D}^{(4)}_{H_{R,b}^{(0)},W_{R,b}^{dd}}
-
{\mathcal D}^{(4)}_{H_{0,b}^{(0)},W_{0,b}^{dd}},
\qquad b\in\{W,st\}.
```

For smooth lapse `N`, set

```math
{\mathcal B}_{a,b}^{(4),dd}[N]
=
a\sum_nN(an)B_{n,b}^{(4),dd}.
```

Then, on the declared smooth finite-particle core,

```math
{\mathcal B}_{a,b}^{(4),dd}[N]I_a^b\Psi
\to
I_a^b{\mathcal B}_{b,\rm cont}^{(4),dd}[N]\Psi,
```

where the continuum delayed coefficient is the strong smooth-core limit of
the finite-stencil expression in Theorem 6.1. Equivalently, it is obtained by
replacing the lattice stencils in the `D^{(4)}` path-interference formula by
the corresponding continuum differential/Fock operators on the declared
smooth core. This is not a pointwise continuum configuration-basis assertion.
Consequently,

```math
\begin{aligned}
&[{\mathcal K}_{a,b}^{(0)}[N],{\mathcal B}_{a,b}^{(4),dd}[M]]I_a^b\Psi
+
[{\mathcal B}_{a,b}^{(4),dd}[N],{\mathcal K}_{a,b}^{(0)}[M]]I_a^b\Psi
\\
&\qquad\to
I_a^b\left(
[K_b^{(0)}[N],{\mathcal B}_{b,\rm cont}^{(4),dd}[M]]
+
[{\mathcal B}_{b,\rm cont}^{(4),dd}[N],K_b^{(0)}[M]]
\right)\Psi .
\end{aligned}
```

Thus compactly supported diagonal density-density interactions have a
well-defined delayed `gDelta^6` stochastic-curvature channel on the declared
smooth core of both the Wilson and staggered branches.

### Proof

The finite-cutoff coefficient in Theorem 6.1 is a finite polynomial in the
local stencils of `H_a` up to third order and one insertion of the bounded
diagonal interaction `W_a^{dd}`. On the smooth cores imported from Paper 3,
the lattice generators and their powers up to order three converge strongly to
the corresponding continuum Dirac/Fock generators, and the compactly supported
normal-ordered density interaction converges strongly on every fixed
finite-particle sector. Therefore each term in the local formula

```math
\frac16(V_x+V_y){\rm Re}\left(\overline{(H^2)_{xy}}H_{xy}\right)
-
\frac13{\rm Re}
\left(
\overline{H_{xy}}\sum_zH_{xz}V_zH_{zy}
\right)
```

has a Riemann-sum/finite-stencil limit on the declared smooth core. Summing
against the compactly supported lapse `N` preserves the convergence.

The mixed `gDelta^6` exchange coefficient is the commutator of the free
`Delta^2` coefficient with this delayed `Delta^4` coefficient. Strong
graph convergence of the free coefficient package and strong convergence of
the delayed local coefficient give the displayed commutator limit by the same
add-and-subtract argument as Theorem 14.1.

In the Wilson branch, Paper 3's Feshbach estimate additionally suppresses
detail-sector corrections on finite-energy tests. In the staggered branch,
there is no such suppression; the limit is a two-taste delayed coefficient,
with taste-mixing terms retained unless the declared smooth tests or a
recorded instrument remove them. `square`

### Branch-Decision Data After The Two Estimates

```text
Criterion                         Wilson branch                No-Wilson staggered branch
------------------------------------------------------------------------------------------------
Barandes directness               declared decoupling          direct detail retention
Target                            single-species tests         multi-taste QFT
Off-diagonal interaction          proved on smooth core         proved on smooth core
Density-density interaction       delayed gDelta^6 proved      delayed gDelta^6 proved
Detail/taste burden               Feshbach gap estimates       taste channels are physical
Experimental/operational story    simpler target               richer but less single-species
Risk                              gap/admissibility scope       multi-taste interpretation
Best immediate use                compare to standard Dirac     ontology-faithful ISP route
```

The data favor a two-track strategy. Use Wilson when the next paper needs a
clean single-species benchmark against standard relativistic QFT. Use
no-Wilson staggered when the next paper is testing the most literal
Barandes-aligned ontology of retained records.

## 15. Status After The Expanded Paper-4 Pass

What is now proved or made theorem-level:

1. the primitive `Delta^2` Born-squared coefficient formula
   `Q(H)_{xy}=|H_{xy}|^2` and its first interaction derivative
   `DQ_H(V)`;
2. ICURV items 1 and 2 for any finite-range interaction through the explicit
   formula
   `B_R=DQ_{H_R^{(0)}}(V_R)-DQ_{H_0^{(0)}}(V_0)`;
3. diagonal density-density interactions have zero first interaction
   coefficient at the leading `Delta^2` scope;
4. diagonal density-density interactions have a derived delayed-onset
   `Delta^4` comparison coefficient and a local path formula involving
   endpoint and intermediate configuration interaction energies, with an
   explicit finite-cutoff `O(Delta^5)` remainder;
5. Wilson density-density is Wilson-admissible but its mixed curvature is
   zero at leading `Delta^2`; its first linear contribution is the delayed
   `gDelta^6` exchange-curvature channel;
6. Wilson off-diagonal interactions have an explicit first coefficient and a
   mixed curvature theorem when the smeared mixed commutator has a strong
   continuum limit;
7. staggered density-density likewise has zero first interaction coefficient
   at leading `Delta^2`, with delayed taste-preserving/taste-mixing channels
   at `gDelta^6`;
8. staggered off-diagonal or alternating interactions split into
   taste-preserving and taste-mixing mixed curvature channels;
9. Wilson interacting curvature reduces to the physical block, with
   detail-sector curvature suppressed by the Wilson gap;
10. staggered interacting curvature survives as a two-taste curvature theorem;
11. operational taste projection gives conditional selected-taste curvature,
   not all-mode single-species curvature;
12. dynamical taste-breaking gives additional curvature channels unless a
   proved heavy-taste gap decouples them;
13. Wilson and staggered branches agree only after declared taste-blind or
   taste-projected comparison data.
14. a concrete off-diagonal mass-channel interaction has a strong smooth-core
   mixed-curvature limit in both Wilson and staggered branches;
15. compactly supported density-density interactions have a strong smooth-core
   delayed `gDelta^6` curvature limit in both Wilson and staggered branches.

What remains open:

1. upgrading the smooth-core limits to larger domains or uniform tested
   operator estimates;
2. extending the off-diagonal benchmark from bounded mass-channel modulation
   to derivative/current interactions with `1/a` hopping scaling;
3. nonperturbative interacting continuum QFT;
4. Lorentz/foliation covariance of the interacting curvature;
5. gauge and non-Abelian stability;
6. operational construction of the instruments that would measure the
   branch-specific curvature terms.

The important conceptual result is already clear: pushing Wilson alone would
miss the no-Wilson branch. The detail-preserving regulator supports both. The
price is that Wilson and staggered do not have the same ontology: Wilson
decouples the retained detail sector behind a declared infinite mass gap,
while staggered keeps that detail sector as observable taste/species content.

The strongest Barandes-aligned path is therefore not "choose Wilson and erase
the rest." It is:

```text
work with the whole finite process;
state which detail-sector option is being tested;
derive the finite-cutoff coefficient;
then prove the branch-specific continuum estimate.
```
