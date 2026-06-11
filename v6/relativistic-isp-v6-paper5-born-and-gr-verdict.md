# Paper 5 (v6) - SHARD Born Rule and GR Verdict

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Finite Born representation theorem and current-data falsification of full GR
```

## 0. Verdict

This paper asks two hard questions about SHARD:

```text
1. Does SHARD derive a real Born rule?
2. Does SHARD derive general relativity?
```

The answers are different.

```text
Born rule:
  yes, as a finite SHARD representation theorem.

Full Hilbert-space quantum measurement theorem:
  not fully; this requires a representation theorem connecting all ordinary
  measurement contexts to retained SHARD holonomy amplitudes.

Operative finite gravity:
  yes; SHARD has finite source/response/transport gravity.

Full 3+1 continuum GR:
  Einstein form yes under the standard 3+1/HKT/Lovelock gates;
  full universal coupling no, not from the current SHARD data alone.
```

Thus Paper 5 proves and falsifies different things:

```text
Born:
  derived in the finite retained-holonomy composition packet.

GR:
  falsified as a derivation from current SHARD data alone.
  The normal-normal determinacy campaign closes on the negative side:
  current sealed finite record data can hide two different normal-normal
  responses.

Minimal normal completion:
  the smallest invariant record datum that blocks the split is the oriented
  normal-frame holonomy center of the normal rectangle.

Full-coupling obstruction:
  the remaining minimal continuum datum is the universal screen
  entropy-area density, equivalently the record area quantum.
```

This is a good outcome. The Born side closes in a clear finite category. The
gravity side does not collapse into vague failure; it identifies the exact
missing data:

```text
normal sector / lapse-cross-normalization-shift data;
full tensor stress-energy readout;
universal screen entropy-area density sigma_A;
continuum coupling/convergence theorem;
covariant 3+1 convergence theorem.
```

## 1. SHARD assumptions used here

Paper 4 defines SHARD:

```text
SHARD = Sealed Holonomy And Record Dynamics.
```

The primitive object is a sealed finite record diamond with a whole-history
law:

```math
P_G^{\rm hist}(\omega)
=
\mu_G(\omega)
\exp\!\left(\langle h_G,\chi_G(\omega)\rangle-\psi_G(h_G)\right),
```

where `chi_G` is the complete primitive oriented RN/KL closed-history ledger.
The commitment law is:

```math
S(I)=\exp(-I),
\qquad
\nabla\psi_G(h_G)=\exp(-h_G).
```

This fixes the closed-history coefficients in the finite SHARD category. It
also survives admissible refinement and admissible sealed-diamond cover
changes.

Paper 5 does not change those primitives. It asks whether two familiar
physical structures follow from them.

## 2. Born rule target

The finite Born target is:

```math
P(i)
=
{|a_i|^2\over \sum_j |a_j|^2},
```

where `a_i` is the retained holonomy amplitude for outcome `i`.

This is not the same as the single-diamond event law. A single sealed diamond
has no interference, no alternative-composition rule, and no visible memory.
Born probabilities live in the composition of retained holonomy across
diamonds.

The theorem therefore uses the following finite SHARD composition packet:

```text
B1. retained holonomy alternatives form a finite complex screen vector a;
B2. alternatives add linearly before a division event;
B3. admissible screen changes are norm-preserving screen transports;
B4. event weights are componentwise and phase-convention blind;
B5. exclusive record cells add probabilities after division;
B6. independent sealed screens compose by product amplitudes.
```

These are not arbitrary quantum postulates. They are the finite expression of
the SHARD distinction:

```text
before division:
  retained holonomies add as amplitudes;

after division:
  exclusive record facts add as probabilities.
```

## 3. Finite Born representation theorem

Let a finite retained-holonomy screen be:

```math
a=(a_1,\ldots,a_n)\in\mathbb C^n.
```

Suppose the event weight has the component form:

```math
W_p(a)=\sum_i |a_i|^p.
```

The admissible screen transports include equal-splitting isometries:

```math
(1,0,\ldots,0)
\mapsto
{1\over\sqrt n}(1,\ldots,1).
```

Screen-weight invariance requires:

```math
1
=
n\left({1\over\sqrt n}\right)^p.
```

Therefore:

```math
p=2.
```

This already kills the `p`-family. More generally, if the weight is
continuous, phase-blind, componentwise, and additive over exclusive records,
then equal splitting gives:

```math
w(r)=n\,w(r/\sqrt n).
```

By finite rational refinements and continuity:

```math
w(r)=C r^2.
```

Normalizing the weights gives:

```math
P(i)
=
{|a_i|^2\over \sum_j |a_j|^2}.
```

That is the finite SHARD Born rule.

## 4. Interference and division

The theorem also fixes the role of interference.

Before division, coherent alternatives add:

```math
a_{\rm coh}=a+b,
\qquad
W_{\rm coh}=|a+b|^2.
```

After division, record alternatives are exclusive:

```math
W_{\rm excl}=|a|^2+|b|^2.
```

These differ by:

```math
2\,{\rm Re}(a\bar b).
```

So interference is not an extra ingredient. It is the difference between:

```text
retained holonomy before division
```

and:

```text
exclusive record alternatives after division.
```

## 5. Born diagnostic

The diagnostic script is:

```text
code/v6_p5a_born_representation_campaign.py
```

It tests equal-splitting invariance, screen rotations, phase blindness,
exclusive coarse-graining, interference, `p`-family attacks, rational finite
frequency refinements, and independent composition.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| equal-split invariance | `(1,0,...)->n^{-1/2}(1,...,1)` | screen-weight preservation forces `p=2` for every tested split | p_values=[2.0, 2.0, 2.0, 2.0, 2.0], gap=0.0e+00 | SELECTS-P2 |
| unitary screen invariance | rotate two retained holonomy coordinates | `p=2` is invariant; `p=1` and `p=4` are not | gap2=0.0e+00, gap1=0.018181, gap4=0.039073 | PASS-BORN-ONLY |
| phase blindness of event weights | change local phases after amplitude formation | probabilities depend on modulus-squared weights, not phase convention | phase_gap=5.6e-17 | PASS |
| exclusive coarse-graining | coarse event after division is a disjoint union of record cells | Born probabilities add over exclusive records | coarse_gap=0.0e+00, block=0.716776 | PASS |
| interference gate | compare coherent alternatives with divided alternatives | before division amplitudes add; after division probabilities add | gap=0.465178 | PASS-SHARD-DISTINCTION |
| `p`-family falsifier | try `p=1.3` as an alternative Born exponent | it fails admissible screen invariance | p_gap=0.014474 | REFUTES-P-FAMILY |
| rational frequency representation | split equal primitive cells into `M` of `N` cells | Born weights reproduce `M/N` exactly for tested finite refinements | max_gap=1.1e-16 | PASS-FINITE-FREQUENCY |
| independent composition | product of independent screens | Born weights factor for independent retained holonomy packets | product_gap=1.1e-16 | PASS-COMPOSITION |
| Born verdict | linear retained holonomy + admissible screen isometries + exclusive additivity | finite SHARD representation uniquely gives normalized squared moduli | finite theorem | DERIVED-FINITE-BORN |

The decisive numbers are:

```text
split_gap = 0.000000000000000e+00
norm2_gap = 0.000000000000000e+00
norm1_gap = 1.818073746578142e-02
norm4_gap = 3.907301855063650e-02
phase_gap = 5.551115123125783e-17
coarse_gap = 0.000000000000000e+00
interference_gap = 4.651777931679608e-01
p_invariance_gap = 1.447433544987442e-02
rational_gap = 1.110223024625157e-16
product_gap = 1.110223024625157e-16
```

The finite verdict is:

```text
SHARD derives the Born rule in its finite retained-holonomy representation.
```

The honest boundary is:

```text
This is not yet a theorem that every standard Hilbert-space measurement
context has been reconstructed from SHARD.
```

That is the next Born theorem:

```text
represent arbitrary finite quantum measurement contexts as admissible SHARD
retained-holonomy screens, preserving coarse-graining and incompatible-context
composition.
```

## 6. GR target

The full GR target is not:

```text
can SHARD solve a finite Poisson equation?
```

That is already true in Paper 4. The full target is:

```math
G_{\mu\nu}
=
8\pi G\,T_{\mu\nu}
```

as a continuum 3+1 tensor equation, with:

```text
Lorentzian metric;
connection;
contracted Bianchi identity;
full tensor source;
universal coupling;
covariant continuum limit.
```

Paper 4 derives significant finite record-gravity structure:

```text
eventless collar operator L;
finite response equation L phi = rho;
screen conductance tensor;
minimal/no-twist screen connection;
double-null kinematic readouts;
cellular source conservation;
cofinal readout completeness.
```

The question is whether this already determines full GR. It does not.

## 7. GR falsification from current SHARD data

The falsification has four independent attacks.

### 7.1 Coupling attack

The finite scalar response equation:

```math
L\phi=\kappa\rho
```

is well-defined once `L`, `rho`, and `kappa` are fixed. But the equation itself
does not fix a universal continuum coupling. Changing `kappa` preserves the
finite conservation identity while changing the response scale.

In Paper 4's scoped finite packet, the local amplitude is tied to primitive
deletion work. That is a real finite receipt. It is still not the same as a
derivation of Newton's constant or a universal Einstein coupling in the
continuum tensor equation.

### 7.2 Normal-sector twin

A two-dimensional screen metric does not determine the full 3+1 Lorentzian
metric.

Consider product metrics with the same flat screen:

```math
q_{AB}=\delta_{AB},
```

but different normal conformal factor:

```math
ds^2=-2\Omega(u,v)^2\,du\,dv+dx^2+dy^2.
```

Take:

```math
\Omega_0=1,
\qquad
\Omega_1=\exp(\alpha uv).
```

The screen metric `q_AB` is identical in both cases. But the base curvature at
`u=v=0` is:

```math
R_{\rm base}=4\alpha/\Omega(0,0)^2.
```

For the product metric, the screen component of the Einstein tensor changes:

```math
G_{xx}=-{1\over2}R_{\rm base}.
```

Thus identical screen data can give different Einstein tensors unless the
normal/cross-normalization sector is intrinsic.

### 7.3 Component-count gate

A scalar response field has one component per record cell. A 3+1 symmetric
Einstein tensor has ten components per cell, with four contracted Bianchi
relations, leaving roughly six tensorial components per cell.

Therefore scalar record gravity cannot be identical to full GR by component
count. It can be a projection or a sector. Full GR requires tensor readouts.

### 7.4 Stress tensor projection attack

Holding a scalar source projection fixed does not determine pressure, flux,
or anisotropic stress. Two stress tensors can have the same scalar deletion
source readout and different tensor stress data. Therefore a full GR theorem
needs a full tensor record-source map, not only scalar deletion density.

## 8. GR diagnostic

The diagnostic script is:

```text
code/v6_p5b_gr_derivation_falsification_campaign.py
```

It tests finite record-gravity response and the four attacks above.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| finite record-gravity receipt | solve ring `L phi = rho` with zero total source | the operative finite SHARD response equation works | res=4.2e-15, span=4.000000 | PASS-FINITE-GRAVITY |
| coupling attack | change only `kappa` in `L phi = kappa rho` | finite conservation survives but response scale moves | span_half=2.000000, span_two=8.000000, gap=6.000000 | REFUTES-UNIVERSAL-COUPLING-FROM-POISSON |
| normal-sector twin | same flat screen metric `q_AB` but `Omega=1` versus `exp(alpha u v)` | Einstein tensor screen component changes while screen `q_AB` is identical | Gxx_flat=-0.000000, Gxx_curved=-0.740000, gap=0.740000 | REFUTES-SCREEN-ONLY-GR |
| cross-normalization attack | same `alpha` but rescale `Omega0` | normal normalization changes Einstein tensor component | Gxx_omega1=-0.740000, Gxx_omega1.7=-0.256055, gap=0.483945 | NEEDS-INTRINSIC-NORMALIZATION |
| component-count gate | compare scalar response components with symmetric 3+1 tensor components | scalar record gravity cannot be a full Einstein tensor equation | scalar=64, Gmunu=640, after_Bianchi~=384, missing=320 | REFUTES-SCALAR-TO-FULL-GR |
| stress tensor projection attack | hold scalar source projection fixed while changing pressure/flux data | same scalar rho does not determine full stress-energy tensor | rho_gap=0.0e+00, pressure_gap=0.812404 | NEEDS-TENSOR-RECORD-READOUT |
| GR verdict | current SHARD screen/source data versus full 3+1 Einstein equation | operative finite gravity is real; full GR is not derived from current data alone | normal sector + tensor stress + coupling theorem required | FULL-GR-FALSIFIED-FROM-CURRENT-DATA |

The decisive numbers are:

```text
finite_residual = 4.208727362491627e-15
finite_span = 3.999999999999995e+00
coupling_span_gap = 5.999999999999992e+00
normal_twin_gap = 7.400000000000000e-01
omega_scale_gap = 4.839446366782006e-01
component_missing_after_bianchi = 3.200000000000000e+02
pressure_gap = 8.124038404635960e-01
```

The finite verdict is:

```text
SHARD has operative finite record gravity.
SHARD does not currently derive full 3+1 GR.
Full GR is falsified as a theorem from the current SHARD screen/source data
alone.
```

## 9. What would be needed to derive GR

A future SHARD-to-GR theorem must derive, not supply:

```text
1. intrinsic normal/cross-normalization data;
2. intrinsic shift/lapse or an equivalent covariant record object;
3. a full tensor source readout T_mu_nu from complete closed holonomy;
4. a universal coupling map from RN/KL record units to Einstein units;
5. a continuum convergence theorem for the resulting Lorentzian metric and
   tensor equation;
6. contracted Bianchi / covariant conservation as a cofinal identity.
```

The current SHARD machinery is not wasted. It gives much of the finite
infrastructure:

```text
screen metric/conductance;
minimal connection;
null kinematics;
source conservation;
readout completeness;
cofinal admissible refinement.
```

But full GR needs the normal/tensor/coupling theorem. Without that theorem,
claiming `G_mu_nu = 8 pi G T_mu_nu` would overclaim.

## 10. Normal-normal determinacy-or-split campaign

The first GR-facing missing object is now no longer vague. In the older V4
language it is the normal-normal coordinate:

```math
\chi^{NN}_{a,ij}.
```

In the current sealed-diamond language it is the question:

```text
does the sealed finite record packet determine the normal-normal response,
or can the same sealed packet hide two different normal-normal responses?
```

Let the current GR-facing sealed shadow be:

```math
S_a(q)
=
\left(
X^{hyp}_a(q),
H^{NN,ij}_a(q),
Q^{screen}_a(q),
R^{source}_a(q)
\right),
```

where `X_a^hyp` is the recorded hypersurface/sealed-diamond packet,
`H_a^NN` is the normal-rectangle loop shadow, and the last two entries denote
the current screen/source/transport data used by the finite record-gravity
packet.

The Einstein closure target is:

```math
\chi^{NN}_{a,ij}
=
K_a(S_a)
```

with actual-law probability tending to one under refinement. The stronger
version replaces `S_a` by the smaller rectangle shadow `H_a^NN`.

The Feynman split target is:

```math
S_a(q_0)=S_a(q_1),
\qquad
\chi^{NN}_{a,ij}(q_0)\ne\chi^{NN}_{a,ij}(q_1),
```

with positive cofinal actual-law mass.

### 10.1 Cofinal split theorem

There is a cofinal finite record family satisfying the current sealed
screen/source/hyp/rectangle data constraints in which the Feynman split holds.

For regulator level `n`, define:

```math
\Omega_n
=
\{(b,k): b\in\{0,1\},\; k=1,\ldots,n\},
```

with actual law:

```math
P_n(b,k)
=
{1\over 2n}.
```

Let all current sealed shadows be identical:

```math
S_n(b,k)=s_0.
```

Let the normal-normal coordinate be:

```math
\chi^{NN}_n(b,k)
=
\begin{cases}
-1,& b=0,\\
+1,& b=1.
\end{cases}
```

Then:

```math
\operatorname{Var}_{P_n}\!\left(\chi^{NN}_n\mid S_n\right)=1
```

for every `n`. Thus `chi_NN` is not measurable with respect to the current
sealed data. The best deterministic map:

```math
K_n:S_n\to\{-1,+1\}
```

succeeds with probability:

```math
{1\over2},
```

not with probability tending to one.

The two-copy same-shadow split mass is:

```math
P_n^{\otimes2}
\left(
S_n(q_0)=S_n(q_1),
\quad
\chi^{NN}_n(q_0)\ne\chi^{NN}_n(q_1)
\right)
=
{1\over2}.
```

The family is cofinal: refinement only splits each branch into more copies,
and pushforward to the two-branch base law is exact. Therefore refinement does
not wash out the hidden normal-normal split.

This proves the Feynman side of the fork for the current sealed data.

### 10.2 What would block the split

There are only three ways to block the counterfamily:

```text
1. prove chi_NN = K(H_NN) from the normal rectangle shadow;
2. prove chi_NN = K(S) from the full sealed packet;
3. enrich the primitive sealed ledger by a record datum that separates the two
   normal-route branches.
```

The first two would be genuine Einstein closure theorems. The third is not a
derivation from the old shadow; it is an enriched ontology. It may still be
SHARD-native if the added datum is a closed-holonomy record rather than a raw
answer label. It changes the premise from:

```text
current sealed data determine the normal sector
```

to:

```text
the complete normal-route holonomy is included among the primitive sealed data.
```

Section 11 identifies the minimal non-tautological version of item 3.

### 10.3 Normal-normal diagnostic

The diagnostic script is:

```text
code/v6_p5c_nn_determinacy_split_campaign.py
```

| target | test | result | value | verdict |
|---|---|---|---:|---|
| same sealed shadow | all atoms share `X_hyp`, `H_NN`, screen, and source data | sealed data have one value while `chi_NN` has two values | shadow_counts=[1, 1, 1, 1, 1, 1], chi_counts=[2, 2, 2, 2, 2, 2] | SAME-SEALED-DATA |
| positive actual split | compute `Var(chi_NN | sealed shadow)` | normal-normal response is not measurable with respect to current sealed data | vars=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0] | SPLIT-POSITIVE |
| determinacy refuter | best `K(sealed_shadow)->chi_NN` predictor | no intrinsic map can succeed with probability tending to one | success=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5] | REFUTES-DETERMINACY |
| two-copy witness | two independent actual records with same sealed shadow | different `chi_NN` occurs with stable positive same-law mass | mass=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5] | FEYNMAN-SPLIT |
| cofinal refinement | split each branch into level-many copies and push to base | actual law and sealed shadows are projectively compatible | push_gaps=['0.0e+00', '0.0e+00', '0.0e+00', '0.0e+00', '0.0e+00', '0.0e+00'] | COFINAL |
| completion check | include `chi_NN` in the sealed primitive ledger | determinacy becomes tautological, showing exactly what must be added | completed_var=0.0e+00, completed_success=1.0 | ENRICHMENT-NOT-DERIVATION |
| campaign verdict | current sealed data versus `chi_NN` | same sealed finite record data can hide two normal-normal responses cofinally | finish condition reached | NN-SPLIT-PROVED |

The decisive numbers are:

```text
max_pushforward_gap = 0.000000000000000e+00
min_conditional_variance = 1.000000000000000e+00
max_best_deterministic_success = 5.000000000000000e-01
min_two_copy_split_mass = 5.000000000000000e-01
completed_conditional_variance = 0.000000000000000e+00
completed_best_success = 1.000000000000000e+00
```

The campaign finish condition is therefore reached:

```text
same sealed finite record data can hide two different normal-normal responses.
```

That is not a conditional result. It is a finite counterfamily to intrinsic
normal-normal determinacy from the current sealed data.

## 11. Minimal invariant datum for `chi_NN`

The previous section proves that the current sealed shadow is too small. The
next question is not whether one can store the answer directly. One can always
add:

```math
\chi^{NN}_{a,ij}
```

as a primitive coordinate. That is determinacy by declaration. The Einstein
question is sharper:

```text
what is the minimal invariant record datum whose physical meaning already is
the normal-normal comparison?
```

The answer is:

```text
the oriented normal-frame holonomy center of the normal rectangle.
```

Notation:

```math
Z^{\perp}_{a,ij}
=
\left[
{\mathcal T}^{\perp}_{j}{\mathcal T}^{\perp}_{i}
\left({\mathcal T}^{\perp}_{i}{\mathcal T}^{\perp}_{j}\right)^{-1}
\right]_{\rm boost}.
```

Here `T_i^perp` and `T_j^perp` are the finite record transports along the two
tested normal directions, and the brackets mean:

```text
keep the closed normal-frame boost holonomy, modulo local normal-frame
relabeling.
```

In a Lorentzian codimension-two screen, the normal plane has a boost gauge.
Local boosts of the two null normals change the connection representative,
but not the closed oriented holonomy class. For the finite normal rectangle,
that holonomy is exactly the missing comparison datum: it says whether the two
normal routes return the same normal frame or differ by a signed boost.

Thus the non-tautological completion is:

```math
S^{+}_a(q)
=
\left(S_a(q),Z^{\perp}_{a,ij}(q)\right).
```

The finite theorem is:

```math
\chi^{NN}_{a,ij}
=
K_a\!\left(S^{+}_a\right)
```

on actual support, and `Z_a^perp` is the coarsest invariant refinement of the
current sealed shadow with that property.

### 11.1 Why this is minimal

Let `S_a` be the current sealed shadow and let `chi_NN` be the normal-normal
readout. In any finite actual law, a datum `D_a` determines `chi_NN` over
`S_a` if and only if `chi_NN` is constant on the positive-mass fibers of:

```math
(S_a,D_a).
```

Equivalently:

```math
\operatorname{Var}\!\left(\chi^{NN}_{a,ij}\mid S_a,D_a\right)=0.
```

The coarsest possible refinement is the two-cell quotient of each sealed
fiber by the value of the normal-normal route comparison. A datum with fewer
cells cannot distinguish the two branches in Section 10. A datum with more
cells is overcomplete.

The oriented normal-frame holonomy center realizes exactly that quotient. It
is not a raw `chi_NN` label because it is a closed-route record:

```text
perform the two normal transports in opposite orders, compare the returned
normal frames at the same screen, and keep the oriented boost holonomy.
```

Its relation to `chi_NN` is the finite normal-response readout map:

```math
\chi^{NN}_{a,ij}
=
{\rm read}_{ij}\!\left(Z^{\perp}_{a,ij}\right).
```

Scalar work, magnitude-only holonomy, and unoriented holonomy all forget the
sign of the normal-route comparison. They therefore leave the same split
alive.

### 11.2 Literature check

This datum is the gravitational version of the holonomy lesson already used
in the v1 gauge benchmark: gauge representatives are not physical, but a
closed holonomy around a finite loop is. In finite-region gravity, the same
logic appears at codimension-two corners. The outside literature points to the
same place:

- Hojman, Kuchar, and Teitelboim's geometrodynamics program makes the algebra
  of hypersurface deformations the invariant content behind spacetime
  embeddability.
- Donnelly and Freidel-style local subsystem work introduces boundary/edge
  data because finite gauge/gravity regions otherwise lose physical
  information at the boundary.
- Freidel, Geiller, and Pranzetti's corner-mode program identifies
  codimension-two corner variables and Lorentz/boost charges as real finite
  gravitational data, not disposable gauge decoration.

The present finite result is narrower than those continuum programs. It uses
only their shared lesson:

```text
the normal-sector comparison of a finite gravitational region lives at the
corner/normal-frame holonomy, not in scalar screen shadows.
```

### 11.3 Minimal normal-holonomy diagnostic

The diagnostic script is:

```text
code/v6_p5d_minimal_normal_holonomy_datum.py
```

It tests every candidate that could plausibly block the Section 10 split:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| current sealed shadow | screen/source/hyp/rectangle data only | `chi_NN` still hidden | var=1.0e+00, success=0.5, cells=1 | FAILS |
| scalar work shadow | one scalar normal-work value | `chi_NN` still hidden | var=1.0e+00, success=0.5, cells=1 | FAILS |
| magnitude-only holonomy | normal loop size without orientation | `chi_NN` still hidden | var=1.0e+00, success=0.5, cells=1 | FAILS |
| unoriented normal holonomy | boost pair with route orientation forgotten | `chi_NN` still hidden | var=1.0e+00, success=0.5, cells=1 | FAILS |
| oriented normal-frame holonomy | `SO(1,1)` boost-center of the normal rectangle | `chi_NN` determined | var=0.0e+00, success=1.0, cells=2 | PASS-MINIMAL |
| overcomplete ADM packet | normal holonomy plus irrelevant copy data | `chi_NN` determined | var=0.0e+00, success=1.0, cells=4 | PASS-NONMINIMAL |
| raw `chi_NN` answer | stores queried response directly | `chi_NN` determined | var=0.0e+00, success=1.0, cells=2 | PASS-TAUTOLOGICAL |
| finite minimality | coarsest refinement of one sealed cell that makes `chi_NN` measurable | two cells are necessary and sufficient | min_cells=[2, 2, 2, 2, 2, 2], oriented_cells=[2, 2, 2, 2, 2, 2] | MINIMAL |
| overcompletion audit | compare oriented center with ADM packet carrying extra copy data | ADM packet determines `chi_NN` only by refining the minimal center | oriented=2, overcomplete=4 | NOT-MINIMAL |
| non-tautology audit | compare oriented holonomy with raw `chi_NN` label | same finite partition, but holonomy is a closed-route record datum | common_refinement_cells=[2, 2, 2, 2, 2, 2] | PHYSICAL-REALIZATION |
| campaign verdict | all candidate invariant record data | the minimal invariant datum is oriented normal-frame holonomy center | finish condition reached | NN-HOLONOMY-CENTER-FOUND |

The decisive numbers are:

```text
sealed_variance = 1.000000000000000e+00
magnitude_variance = 1.000000000000000e+00
unoriented_variance = 1.000000000000000e+00
oriented_variance = 0.000000000000000e+00
oriented_success = 1.000000000000000e+00
minimal_cell_count = 2.000000000000000e+00
oriented_cell_count = 2.000000000000000e+00
overcomplete_cell_count = 4.000000000000000e+00
```

So the finish condition is reached:

```text
the minimal invariant record datum that makes chi_NN unavoidable is the
oriented normal-frame holonomy center Z_perp of the normal rectangle.
```

This also explains the status of the older ADM route. An ADM normal-response
packet can be sufficient, but only because it contains `Z_perp` plus extra
normal-response data. For `chi_NN` itself, that packet is not minimal.

## 12. Full 3+1 GR closure campaign after `Z_perp`

Section 11 closes the first normal-sector hole. It does not by itself prove
full 3+1 GR. The new finish condition is stricter:

```text
Either SHARD plus Z_perp determines the full continuum Einstein equation,
including universal source coupling, or the same finite sealed record data can
hide two different continuum couplings.
```

The campaign splits into two parts.

### 12.1 Einstein-form gate

The positive part is the familiar GR uniqueness route. Once the following are
available:

```text
1. a Lorentzian 3+1 metric readout;
2. the oriented normal-frame holonomy center Z_perp;
3. a conserved tensor source readout T_mu_nu;
4. hypersurface-deformation covariance / embeddability;
5. a local, symmetric, divergence-free, rank-two low-derivative sector;
```

then the untyped low-energy equation has the Lovelock/HKT form:

```math
G_{\mu\nu}
+\Lambda g_{\mu\nu}
=
\kappa T_{\mu\nu}.
```

That is a real positive theorem target, and it is aligned with the v4
low-energy Lovelock repair. `Z_perp` supplies the missing normal comparison
needed before this target is even well-typed.

### 12.2 Coupling gate

The negative part is the coupling. The RN/KL commitment law fixes the
dimensionless evidence clock:

```math
S(I)=\exp(-I).
```

It does not fix the conversion between finite record entropy and continuum
screen area. Let:

```math
\sigma_A
=
{dI\over dA}
```

be the universal screen entropy-area density in record nats per continuum
area. Causal-diamond and horizon-first-law derivations fix the Einstein
coupling only after this density is known. Schematically:

```math
\kappa
\propto
{1\over \sigma_A}.
```

Therefore the remaining minimal continuum invariant is:

```text
universal screen entropy-area density sigma_A
```

or equivalently:

```text
the record area quantum A_rec = sigma_A^{-1}.
```

This is not the old `chi_NN` problem. `chi_NN` was a missing normal holonomy
datum. The new obstruction is the continuum calibration that turns record
entropy into geometric area.

### 12.3 Why the obvious laws do not fix it

The campaign checked the candidate rescuers.

**HKT / hypersurface deformation algebra.** It fixes embeddability and the
normal-deformation structure. It does not set Newton's constant.

**Lovelock uniqueness.** It fixes the tensor form in four low-energy
dimensions:

```math
G+\Lambda g=\kappa T.
```

It leaves `kappa` and `Lambda` as constants or integration/boundary data.

**RN/KL commitment.** It fixes the dimensionless record evidence scale:

```math
-\log S(I)=I.
```

It does not know how many continuum area units correspond to one record nat.

**Jacobson / causal-diamond first law.** It is the best bridge. But its
coupling is proportional to the inverse entropy-area density. Thus it turns
`sigma_A` into `kappa`; it does not derive `sigma_A` from finite record data.

**Bekenstein-Hawking record counting.** The v5 black-hole paper already flags
the exact issue: reading black-hole entropy as record count is natural, but
deriving the area law and the coefficient is not done there.

Thus the full-coupling gate is not closed by creativity alone. The finite
counterfamily is stable:

```text
same SHARD closed-holonomy data
+ same Z_perp
+ same tensor source readout
+ different sigma_A
-> different continuum kappa.
```

### 12.4 Full-GR diagnostic

The diagnostic script is:

```text
code/v6_p5e_full_31_gr_closure_campaign.py
```

It tests the Einstein-form gate, the same-record/two-coupling attack, the
RN/KL commitment rescue, the causal-diamond first-law route, and the
cosmological-term gate.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| Einstein-form gate | assume Lorentzian metric + `Z_perp` + conserved tensor source + 4D Lovelock sector | equation form is `G + Lambda g = kappa T`, not a larger local tensor family | form_family_dim=2 | PASS-FORM |
| same sealed data | compare records before continuum area calibration | all finite SHARD entries agree, including `Z_perp` and tensor source | same_record_gap=0 | SAME-SHARD-DATA |
| area-density attack | vary record-area quantum while holding record evidence fixed | entropy-per-area density changes but finite record data do not | density=1.000/0.250 | DENSITY-FREE |
| coupling split | `kappa` is inverse to entropy-per-area density in causal-diamond first-law routes | same finite data give two Einstein couplings | kappa=1.000/4.000, gap=3.000 | REFUTES-UNIQUE-COUPLING |
| Einstein residual check | build curvature response with each `kappa` | both satisfy Einstein-form equations exactly, but with different response scales | res=0.0e+00/0.0e+00, curvature_gap=1.110 | BOTH-GR-FORM |
| RN/KL commitment law | `S(I)=exp(-I)` at the same record evidence | dimensionless division scale is fixed but cannot see area calibration | survival_gap=0.0e+00 | FIXES-EVIDENCE-NOT-G |
| Jacobson/causal-diamond route | supply entropy-area density, then compute `kappa` | first-law derivations fix coupling only after the density is given | supplied_density=1.000, supplied_kappa=1.000 | COND-POSITIVE |
| cosmological term gate | vary `Lambda` while preserving Lovelock/Bianchi form | Bianchi permits a metric term; local vacuum centering would be an extra selection | Lambda_gap=0.180, res=0.0e+00/0.0e+00 | LAMBDA-INTEGRATION-DATA |
| closure with missing datum | add universal screen entropy-area density / record area quantum | `kappa` is then determined by record data plus the supplied density | res=0.0e+00 | CLOSES-IF-SUPPLIED |
| full GR verdict | SHARD + `Z_perp` + current continuum gates | Einstein form is derivable under Lovelock/HKT assumptions; full coupling is not | same data hide different kappa | FULL-3PLUS1-GR-NOT-DERIVED |

The decisive numbers are:

```text
same_record_gap = 0.000000000000000e+00
density_small = 1.000000000000000e+00
density_large = 2.500000000000000e-01
kappa_small = 1.000000000000000e+00
kappa_large = 4.000000000000000e+00
coupling_gap = 3.000000000000000e+00
curvature_gap = 1.110000000000000e+00
einstein_residual_small = 0.000000000000000e+00
einstein_residual_large = 0.000000000000000e+00
survival_gap = 0.000000000000000e+00
lambda_gap = 1.800000000000000e-01
supplied_residual = 0.000000000000000e+00
```

The finish condition is therefore reached on the falsification side:

```text
same finite SHARD + Z_perp data can hide two different full-GR continuum
couplings unless sigma_A is also intrinsic.
```

The minimal remaining invariant is not another normal variable. It is:

```text
sigma_A = universal record entropy per continuum screen area.
```

If SHARD later derives `sigma_A` from its complete closed-holonomy ledger,
then the causal-diamond first-law route can turn the current finite theory
into a full 3+1 Einstein-coupling theorem. If `sigma_A` is calibrated from
outside, full GR coupling is branch B at that final scale.

## 13. `sigma_A` determinacy campaign

The remaining question is now isolated:

```text
Does the sealed finite record packet intrinsically determine the universal
screen entropy-area density sigma_A?
```

The finish condition is:

```text
Either sigma_A is intrinsically determined by sealed finite record data,
or the same sealed horizon/diamond data can hide two different entropy-area
densities.
```

The campaign includes every current positive structure:

```text
RN/KL commitment law;
primitive Diamond Work-Balance constant;
Born/screen norm;
oriented normal-frame holonomy Z_perp;
tensor source readout;
Unruh/modular temperature;
causal-diamond first-law form;
Bekenstein/holographic bound.
```

All of these fix real dimensionless record facts. None fixes the conversion
between record entropy and continuum area.

### 13.1 Why the candidates fail

**RN/KL commitment.** This fixes:

```math
S(I)=\exp(-I).
```

It says one nat of sealed evidence is one nat of sealed evidence. It does not
say how many square meters, Planck areas, or continuum screen-area units carry
one nat.

**Primitive Diamond Work-Balance.** This fixes the primitive binary defect law
and a dimensionless common work:

```text
theta_* = 0.797003794162878.
```

It fixes the event's internal record amplitude. It does not assign a continuum
area to the event.

**Unruh/modular temperature.** The local first-law form:

```math
\delta Q = T\,\delta S
```

turns record entropy into heat in modular units. But the Einstein coupling
requires the next identification:

```math
\delta S = \sigma_A\,\delta A.
```

That is exactly the missing density.

**Jacobson / causal-diamond route.** This is the best positive bridge. It
turns a universal entropy-area density into Einstein coupling. It does not
derive that density from the sealed record packet.

**Bekenstein/holographic bound.** A bound such as:

```math
S \leq \sigma_A A
```

permits a family of `sigma_A` values. Saturation can select a value on a
black-hole or horizon branch, but saturation and the coefficient are extra
horizon input unless SHARD derives them.

**Entanglement area laws.** They support the idea that local horizons and
screens carry area-proportional entropy, but the coefficient is cutoff/theory
data. That is the same obstruction in continuum language.

Thus the same conclusion appears from both sides:

```text
record evidence is fixed;
area calibration is not.
```

### 13.2 Finite split theorem

Let a sealed horizon record have:

```text
N atoms;
one nat of evidence per atom;
the same Z_perp;
the same tensor source;
the same modular temperature;
the same primitive DWB constant theta_*.
```

Let the continuum area per record atom be either:

```math
A_{\rm rec}=1
```

or:

```math
A_{\rm rec}=3.
```

All sealed record entries are identical. But:

```math
\sigma_A
=
{I\over A}
=
{N\over N A_{\rm rec}}
=
{1\over A_{\rm rec}},
```

so:

```math
\sigma_A=1
\quad\hbox{or}\quad
\sigma_A={1\over3}.
```

The Jacobson/causal-diamond coupling then changes:

```math
\kappa\propto {1\over\sigma_A}.
```

Therefore the same sealed horizon data hide two different continuum Einstein
couplings.

### 13.3 `sigma_A` diagnostic

The diagnostic script is:

```text
code/v6_p5f_sigma_area_density_campaign.py
```

It tests the current record/modular/horizon candidates against the
same-record/two-density split.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| same sealed horizon data | compare record atoms, RN evidence, `Z_perp`, tensor source, modular temperature, DWB theta | all finite SHARD entries agree before area calibration | same_record_gap=0 | SAME-SEALED-DATA |
| RN/KL commitment | `S(I)=exp(-I)` on each atom | evidence scale is fixed but independent of continuum area quantum | survival_gap=0.0e+00 | NO-SIGMA-SELECTION |
| primitive DWB constant | compare selected `theta_*` for the primitive binary defect | dimensionless event law is fixed while area density remains free | theta_gap=0.0e+00 | NO-SIGMA-SELECTION |
| Born/screen norm | compare retained-holonomy norm convention | Born normalization is unaffected by area calibration | norm_gap=0.0e+00 | NO-SIGMA-SELECTION |
| Unruh/modular temperature | `delta Q = T delta S` with same `T` and same record entropy | heat flux is fixed in record units but not in area units | heat_gap=0.0e+00, T=0.159155 | NO-SIGMA-SELECTION |
| area-calibration split | vary `A_rec` while keeping record entropy fixed | `sigma_A` changes with no change to sealed data | sigma=1.000/0.333 | SIGMA-SPLIT |
| coupling consequence | Jacobson/causal-diamond route `kappa` proportional to `1/sigma_A` | two `sigma_A` values give two couplings and two curvature responses | kappa=1.000/3.000, curvature=0.410/1.230 | COUPLING-SPLIT |
| Bekenstein/holographic bound | test `S <= bound_density * A` | a bound allows a family; only saturation would select an area density | slack=0.000/256.000 | BOUND-NOT-LAW |
| black-hole saturation | impose `S = sigma_A A` on a horizon | this fixes `sigma_A` only by adding saturation/coefficient input | sigma_if_area_a=1.000 | COND-SATURATION |
| closure if supplied | add record area quantum `A_rec` to the sealed ledger | `sigma_A` and `kappa` are then determined | A_rec=1.000, sigma=1.000, kappa=1.000 | CLOSES-IF-SUPPLIED |
| campaign verdict | all current record/modular/horizon candidates versus `sigma_A` | same sealed horizon data can hide two entropy-area densities | finish condition reached | SIGMA-SPLIT-PROVED |

The decisive numbers are:

```text
same_record_gap = 0.000000000000000e+00
sigma_a = 1.000000000000000e+00
sigma_b = 3.333333333333333e-01
sigma_gap = 6.666666666666667e-01
kappa_a = 1.000000000000000e+00
kappa_b = 3.000000000000000e+00
kappa_gap = 2.000000000000000e+00
curvature_gap = 8.200000000000001e-01
survival_gap = 0.000000000000000e+00
heat_gap = 0.000000000000000e+00
dwb_gap = 0.000000000000000e+00
born_gap = 0.000000000000000e+00
```

So the finish condition is reached:

```text
same sealed horizon/diamond data can hide two different entropy-area densities.
```

### 13.4 Minimal closure datum

The minimal datum that would close this final coupling gate is:

```text
A_rec = the universal continuum screen area carried by one primitive sealed
record nat.
```

Equivalently:

```math
\sigma_A=A_{\rm rec}^{-1}.
```

If `A_rec` is supplied externally, the Einstein coupling is calibrated, not
derived. If SHARD derives `A_rec` from the complete closed-holonomy ledger,
the full GR coupling route closes.

The campaign therefore does not leave a vague open gate. It proves the
negative side for current data and names the exact missing invariant.

## 14. Record-area operational campaign

The previous section proves that `sigma_A` is not fixed by the current sealed
record packet. One possible objection remains:

```text
Maybe continuum area was the wrong target. Maybe sealed record operations
define area operationally, and the apparent missing A_rec disappears.
```

This section runs that campaign directly.

### 14.1 Finish condition

The finish condition is:

```text
Either sealed screen operations determine an absolute record-area quantum
A_rec, or they determine only an additive area valuation up to one global
multiplier.
```

The second outcome is still a positive theorem. It means record-area is real
inside the theory. But it does not derive the continuum Einstein coupling,
because the coupling depends on the absolute entropy per continuum area.

### 14.2 Operational screen axioms

A sealed screen `S` has an intrinsic finite record capacity:

```math
C(S)\geq 0.
```

The allowed operational tests are:

```text
finite additivity:
  C(S\sqcup T)=C(S)+C(T);

refinement stability:
  splitting one screen cell into capacity-preserving subcells does not change C;

shared-boundary gluing:
  C(S\cup_R T)=C(S)+C(T)-C(R);

monotonicity:
  adding record capacity cannot lower area;

empty screen normalization:
  A_{\rm op}(\varnothing)=0.
```

These are exactly the finite record analogue of an additive valuation. They are
not coordinate assumptions and do not require a prior metric.

### 14.3 Positive theorem: operational area ratios are derived

Let `A_op` be a monotone, refinement-stable screen valuation depending only on
sealed screen capacity and obeying finite additivity. On the rational finite
refinement lattice:

```math
A_{\rm op}(S)=A_{\rm rec}\,C(S)
```

for one positive constant `A_rec`.

The proof is elementary. Additivity and empty normalization remove offsets.
Refinement stability makes equal-capacity refinements indistinguishable.
Monotonicity rules out pathological sign-changing solutions. Therefore the
valuation is fixed by its value on one primitive record-capacity unit. Every
screen ratio is then intrinsic:

```math
{A_{\rm op}(S)\over A_{\rm op}(T)}
=
{C(S)\over C(T)}.
```

So the campaign has a genuine positive result:

```text
sealed screen operations derive record-area ratios and gluing laws.
```

### 14.4 Negative theorem: the absolute unit is not derived

The same proof shows the obstruction. The value on one primitive capacity unit
is exactly:

```math
A_{\rm rec}.
```

If `A_rec` is replaced by `3 A_rec`, then every finite operational screen test
still passes:

```text
additivity passes;
refinement stability passes;
shared-boundary gluing passes;
area ratios are unchanged;
record heat is unchanged;
Born normalization is unchanged;
closed holonomy is unchanged.
```

But the entropy-area density changes:

```math
\sigma_A={C(S)\over A_{\rm op}(S)}={1\over A_{\rm rec}},
```

and the Jacobson/causal-diamond coupling changes with it:

```math
\kappa\propto {1\over\sigma_A}\propto A_{\rm rec}.
```

Thus operational record-area closes the intrinsic area-measure problem, but not
the absolute continuum-coupling problem.

### 14.5 Record-area diagnostic

The diagnostic script is:

```text
code/v6_p5g_record_area_operational_campaign.py
```

It tests finite additivity, refinement stability, shared-boundary gluing,
nonlinear alternatives, offsets, area ratios, entropy-area density, modular
heat per area, and coupling.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| record capacity | `C(S union T)=C(S)+C(T)` and refinement preserves `C` | sealed screen operations define intrinsic capacity | C_base=4.000, C_refined=4.000 | CAPACITY-DERIVED |
| linear record-area | `A_op(S)=A_rec C(S)` | passes additivity, refinement, and shared-boundary gluing | add=0.0e+00, ref=0.0e+00, glue=0.0e+00 | PASS |
| scale twin | `A'_op(S)=3 A_rec C(S)` | also passes all record-area operational tests | add=0.0e+00, ref=0.0e+00, glue=0.0e+00 | SAME-TESTS |
| offset valuation | `A(S)=A_rec C(S)+b` | constant offsets violate finite additivity | add_gap=0.750 | REJECT |
| nonlinear valuation | `A(S)=A_rec C(S)^2` | nonlinear capacity rules violate additivity while preserving refinement | add_gap=16.000, ref_gap=0.0e+00 | REJECT |
| area ratios | compare `S/T` before and after rescaling `A_rec` | all operational ratios are fixed by record capacity | C_ratio=2.000, A_ratios=2.000/2.000 | RATIO-DERIVED |
| entropy-area density | `sigma_A=C/A_op` | density changes under the invisible global multiplier | sigma=1.000/0.333 | SIGMA-FREE |
| modular heat per area | same record heat, different continuum area unit | record thermodynamics is fixed but area density is not | q_A=0.159155/0.053052 | DENSITY-FREE |
| Einstein coupling | `kappa` proportional to `1/sigma_A` | two accepted record-area valuations give two couplings | kappa=1.000/3.000 | COUPLING-SPLIT |
| campaign verdict | all operational screen tests versus `A_rec` | record-area is unique up to one global unit, not absolutely fixed | finish condition reached | A_REC-SPLIT-PROVED |

The decisive numbers are:

```text
lin_add_gap = 0.000000000000000e+00
lin_ref_gap = 0.000000000000000e+00
lin_seam_gap = 0.000000000000000e+00
lin2_add_gap = 0.000000000000000e+00
lin2_ref_gap = 0.000000000000000e+00
lin2_seam_gap = 0.000000000000000e+00
off_add_gap = 7.500000000000000e-01
pow_add_gap = 1.600000000000000e+01
pow_ref_gap = 0.000000000000000e+00
cap_ratio = 2.000000000000000e+00
area_ratio_a1 = 2.000000000000000e+00
area_ratio_a2 = 2.000000000000000e+00
sigma_a1 = 1.000000000000000e+00
sigma_a2 = 3.333333333333333e-01
sigma_gap = 6.666666666666667e-01
kappa_a1 = 1.000000000000000e+00
kappa_a2 = 3.000000000000000e+00
kappa_gap = 2.000000000000000e+00
heat_per_area_gap = 1.061032953945969e-01
```

So the operational campaign closes as:

```text
Record-area measure:
  derived up to one universal multiplier.

Absolute record-area quantum:
  not derived from sealed screen operations.

Einstein coupling:
  still requires A_rec or sigma_A.
```

This is the most precise current status. The theory does not lack an
operational notion of area. It lacks the invariant that fixes the physical
unit of that area against continuum gravitational coupling.

## 15. Final status

The final Paper 5 status is:

```text
Born rule:
  derived as a finite SHARD retained-holonomy representation theorem.

Full quantum measurement reconstruction:
  open representation theorem.

Operative finite gravity:
  derived.

Full 3+1 GR:
  Einstein form follows under HKT/Lovelock-style continuum gates, but the
  universal coupling is not derived from current SHARD data alone.

Record-area:
  operational screen area ratios and gluing laws are derived as additive
  record-capacity valuations, but the absolute record-area quantum A_rec is
  not derived.

Normal-normal determinacy:
  refuted from current sealed data alone; a cofinal same-shadow/two-response
  split exists.

Minimal normal completion:
  the oriented normal-frame holonomy center Z_perp is the coarsest invariant
  record datum that makes chi_NN unavoidable.

Next GR route:
  include Z_perp as part of the complete closed-holonomy ledger, derive the
  full tensor source and continuum convergence, and either derive A_rec /
  sigma_A intrinsically or admit that Newton coupling is externally calibrated.
```

The two sides are therefore asymmetric.

Born works because the retained-holonomy screen already has the right
invariance object: finite norm-preserving composition. The exponent is forced.

Full GR does not yet fully work because the current record-gravity packet
supplies finite geometry, closed holonomy, source projections, and operational
record-area ratios, but not the universal entropy-area density that fixes the
continuum Einstein coupling. Section 11 identifies the minimal missing normal
datum. Sections 12 and 13 identify and then falsify intrinsic determinacy of
the remaining coupling density. Section 14 proves that operational screen
area is real but scale-free.

That is the honest verdict.

## References

- S. A. Hojman, K. Kuchar, and C. Teitelboim, "Geometrodynamics regained,"
  Annals of Physics 96, 88-135 (1976),
  <https://doi.org/10.1016/0003-4916(76)90112-3>.
- D. Lovelock, "The Einstein tensor and its generalizations," Journal of
  Mathematical Physics 12, 498 (1971), <https://doi.org/10.1063/1.1665613>.
- T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State,"
  Physical Review Letters 75, 1260 (1995), <https://arxiv.org/abs/gr-qc/9504004>.
- T. Faulkner, M. Guica, T. Hartman, R. C. Myers, and M. Van Raamsdonk,
  "Gravitation from Entanglement in Holographic CFTs,"
  <https://arxiv.org/abs/1312.7856>.
- J. D. Bekenstein, "Black holes and entropy," Physical Review D 7, 2333
  (1973), <https://doi.org/10.1103/PhysRevD.7.2333>.
- S. W. Hawking, "Particle Creation by Black Holes," Communications in
  Mathematical Physics 43, 199-220 (1975),
  <https://doi.org/10.1007/BF02345020>.
- L. Bombelli, R. K. Koul, J. Lee, and R. D. Sorkin, "Quantum source of
  entropy for black holes," Physical Review D 34, 373 (1986),
  <https://doi.org/10.1103/PhysRevD.34.373>.
- M. Srednicki, "Entropy and area," Physical Review Letters 71, 666 (1993),
  <https://arxiv.org/abs/hep-th/9303048>.
- W. Donnelly and L. Freidel, "Local subsystems in gauge theory and gravity,"
  JHEP 09 (2016) 102, <https://arxiv.org/abs/1601.04744>.
- L. Freidel, M. Geiller, and D. Pranzetti, "Edge modes of gravity I: Corner
  potentials and charges," JHEP 11 (2020) 026,
  <https://arxiv.org/abs/2006.12527>.
- L. Freidel, M. Geiller, and D. Pranzetti, "Edge modes of gravity II: Corner
  metric and Lorentz charges," <https://arxiv.org/abs/2007.03563>.
- W. Donnelly, L. Freidel, S. F. Moosavian, and A. J. Speranza,
  "Gravitational Edge Modes, Coadjoint Orbits, and Hydrodynamics,"
  <https://arxiv.org/abs/2012.10367>.
