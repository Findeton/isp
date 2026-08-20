# Joint curvature response and conditional GR recovery

## A covariant control model beyond the $1+1$ reconstruction

### Research-preparation status

Date: 2026-08-20

This is a nonbinding Paper 16 research draft. It is not an authoritative
construction, evaluator result, or promotion of the Paper 14 substrate. Paper
14 presently supplies only an abstract point-free stable-happening order and
interval measure. Paper 15 conditionally reconstructs a smooth $1+1$
spacetime inside a declared affine-copula/Poisson family. Neither result has
derived a $3+1$ carrier, a stress tensor, Newton's constant, Einstein
dynamics, or a continuum limit from the primitive relational law.

The purpose of this draft is narrower and useful: state the first exact
covariant matter--geometry target that a future point-free construction would
have to reproduce, solve it without numerical fitting, expose genuine
two-direction response, and preregister the controls that prevent a copied
Einstein equation from masquerading as emergence.

The scoped target is a spatially flat homogeneous $3+1$ geometry coupled to
a canonical massless scalar. The geometry, dimension, symmetry reduction,
continuum action, scalar interpretation, and coupling $G_N$ are declared.
The target therefore cannot earn physical GR for ISP. It can earn only a
conditional recovery theorem and a precise interface for the next
Gamma-derived construction.

## Abstract

The Paper 15 $1+1$ reconstruction cannot by itself support ordinary Einstein
backreaction: in two dimensions the Einstein tensor vanishes identically,

\[
G_{ab}=R_{ab}-\frac12 Rg_{ab}=0.
\]

This is a structural obstruction, not a shortage of numerical evidence. Any
nontrivial ordinary Einstein target must change dimension or change the
gravitational theory.

We therefore declare a minimal $3+1$ control family, derive its matter stress
from a scalar action and its geometric equation from the Einstein--Hilbert
action, and then reduce both to complete homogeneous division frontiers. The
exact expanding solution is

\[
V(\tau)=V_0+\sqrt{12\pi G_N}\,|P|\tau,
\qquad
\phi(\tau)=\phi_0+
\frac{\operatorname{sgn}P}{\sqrt{12\pi G_N}}
\log\frac{V(\tau)}{V_0},
\]

where $V=a^3$ is physical volume per fixed comoving cell and
$P=V\dot\phi$ is conserved scalar momentum. Matter changes the geometric
expansion rate, while geometry changes the scalar rate through
$\dot\phi=P/V$. Curvature is dynamical,

\[
R=-\frac{8\pi G_NP^2}{V^2},
\qquad
\dot R+6HR=0,
\]

and the same solution predicts redshift and a finite-frontier semigroup.

The result is an exact conditional Einstein--scalar closure, not a derivation
of GR. A future physical promotion must derive the carrier, order, volume,
proper time, scalar, stress map, coupling, joint update, and constraint
closure from the same point-free law, with actualization still external.

## 1. Ontology and term bindings

### 1.1 Stable happenings are not Markov checkpoints

A stable happening is a persistent physical fact. A division frontier is a
complete typed argument sufficient for every licensed future. The two notions
remain independent. Nothing in this draft licenses factorization through an
individual happening.

In the declared homogeneous target, a complete frontier is represented by

\[
Z_\tau=(\mathsf T_\tau,V_\tau,\phi_\tau,P_\tau),
\]

where $\mathsf T_\tau$ binds the frontier type and orientation. The triple
$(V,\phi,P)$ is sufficient only inside the declared homogeneous
Einstein--massless-scalar family. It is not asserted to be sufficient for the
underlying ISP law or for an arbitrary inhomogeneous spacetime.

### 1.2 Declared versus derived objects

The following objects are declared in this control model:

1. a differentiable $3+1$ Lorentzian manifold;
2. spatially flat homogeneous and isotropic symmetry;
3. the Einstein--Hilbert and canonical massless-scalar actions;
4. a positive Newton coupling $G_N$;
5. a fixed fiducial comoving cell used only to make $V=a^3$ finite;
6. a time orientation and the expanding branch;
7. the interpretation of $\phi$ as a continuum scalar field.

The following are derived inside that declared family:

1. the stress tensor and equation of state;
2. the Friedmann, Raychaudhuri, and Klein--Gordon equations;
3. conserved momentum $P$;
4. the exact finite-frontier update;
5. reciprocal matter--geometry response;
6. scalar curvature, Kretschmann curvature, and redshift;
7. several held-out consistency estimators of the same $G_N$.

No item in the second list is thereby Gamma-derived.

### 1.3 Actuality remains external

The equations provide possible joint histories. Selecting one history as
actual remains an actualization postulate. Stable records may document the
selected history, but persistence does not perform the selection.

## 2. Exact obstruction in $1+1$

For every two-dimensional pseudo-Riemannian metric,

\[
R_{ab}=\frac12 Rg_{ab}.
\]

Consequently,

\[
G_{ab}=0
\]

as a geometric identity. The ordinary field equation

\[
G_{ab}=8\pi G_NT_{ab}
\]

would force $T_{ab}=0$. The two-dimensional Einstein--Hilbert integral is
topological up to boundary terms and supplies no local metric equation.

Therefore Paper 15's conditional $1+1$ curvature is genuine metric
curvature inside its target family, but it is not an ordinary Einstein
backreaction degree of freedom. Three common evasions are forbidden:

- reading nonzero scalar curvature as a nonzero Einstein tensor;
- defining $T_{ab}=G_{ab}/(8\pi G_N)$ after the geometry is known;
- importing a dilaton or modified-gravity field without declaring a new
  theory and outcome ladder.

This establishes the exact result

`P16-1+1-EINSTEIN-TENSOR-IDENTICALLY-ZERO`.

It forces the ordinary-GR control to use dimension at least three. This draft
uses $3+1$, while recording that the dimension is supplied rather than
derived.

## 3. Four-gate ledger for the $3+1$ control

Every load-bearing object must pass four distinct gates.

| Object | Definition | Construction | Discriminator | Use |
|---|---|---|---|---|
| $3+1$ carrier | Lorentzian manifold with flat homogeneous slices | declared FLRW ansatz | $1+1$ Einstein-tensor zero control; wrong-dimension attack | permits nontrivial Einstein dynamics |
| spatial volume $V$ | volume of a fixed comoving cell | $V=a^3$ | cell-rescaling covariance; copied-counter attack | frontier geometry and expansion |
| scalar $\phi$ | canonical massless matter field | independent matter action | wrong-sign, potential, and hand-coded-stress attacks | supplies matter dynamics |
| momentum $P$ | $P=V\dot\phi$ | Noether/Klein--Gordon conservation | momentum drift and sign controls | complete homogeneous matter datum |
| $G_N$ | positive coupling in the action | declared once | fit-once/held-out estimators; scale mutation | couples independent sectors |
| proper duration | lapse-invariant $d\tau=N\,d\lambda$ | metric line element | lapse reparameterization | compares frontier intervals |

No column may be inferred merely because another column contains a matching
number.

## 4. Covariant joint action

Use signature ((-+++)) and the action

\[
S[g,\phi]
=
\int d^4x\sqrt{-g}
\left[
\frac{R}{16\pi G_N}
-\frac12 g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi
\right].
\]

The matter stress tensor is derived before imposing the geometric equation:

\[
T_{\mu\nu}
=
\partial_\mu\phi\partial_\nu\phi
-\frac12g_{\mu\nu}
g^{\alpha\beta}\partial_\alpha\phi\partial_\beta\phi.
\]

Metric variation gives

\[
G_{\mu\nu}=8\pi G_NT_{\mu\nu},
\]

and scalar variation gives

\[
\Box_g\phi=0.
\]

This ordering matters. Defining the right-hand side from the left-hand side
would make backreaction tautological.

## 5. Homogeneous reduction without a hidden clock

Keep the lapse explicit:

\[
ds^2=-N(\lambda)^2d\lambda^2
+a(\lambda)^2(dx^2+dy^2+dz^2).
\]

Proper duration is

\[
d\tau=N(\lambda)d\lambda.
\]

Dots below mean $d/d\tau$, not differentiation with respect to an
implementation index. Define

\[
V=a^3,
\qquad
H=\frac{\dot a}{a}=\frac{\dot V}{3V}.
\]

For homogeneous $\phi$,

\[
\rho=\frac12\dot\phi^2,
\qquad
p=\frac12\dot\phi^2.
\]

The reduced equations are

\[
3H^2=4\pi G_N\dot\phi^2,
\tag{F}
\]

\[
\dot H=-4\pi G_N\dot\phi^2,
\tag{R}
\]

and

\[
\ddot\phi+3H\dot\phi=0.
\tag{KG}
\]

Equation (KG) gives the conserved charge

\[
P=V\dot\phi,
\qquad
\dot P=0.
\]

The coordinate label (lambda) has disappeared from all observables. A lapse
change alters the serialization of a curve but not its physical duration,
frontier map, or predictions.

## 6. Exact solution and complete-frontier map

Let

\[
\kappa=\sqrt{12\pi G_N}.
\]

For $V_0>0$, $P\ne0$, and the expanding branch, equation (F) gives

\[
\dot V=\kappa|P|.
\]

Hence

\[
V(\tau)=V_0+\kappa|P|\tau
\]

and

\[
\phi(\tau)=
\phi_0+
\frac{\operatorname{sgn}P}{\kappa}
\log\left(\frac{V_0+\kappa|P|\tau}{V_0}\right).
\]

The $P=0$ limit is static Minkowski space with constant $\phi$. It must be
handled directly, not by asking for $\operatorname{sgn}(0)$.

For a proper-duration increment $s\ge0$, define the finite update

\[
\mathcal F_s(V,\phi,P)
=
\left(
V+\kappa|P|s,
\phi+\frac{\operatorname{sgn}P}{\kappa}
\log\frac{V+\kappa|P|s}{V},
P
\right)
\]

for $P\ne0$, with $\mathcal F_s(V,\phi,0)=(V,\phi,0)$. Direct substitution
gives

\[
\mathcal F_s\circ\mathcal F_t=\mathcal F_{s+t},
\qquad
\mathcal F_0=\mathrm{id}.
\]

This is not a claim that every microscopic cut is Markovian. It is a semigroup
only on the declared complete homogeneous frontiers. At an incomplete cut the
primitive whole law must be retained and no kernel is invented.

For disjoint homogeneous cells with no shared constraint or interaction, the
tensor updates commute. Once a shared constraint or interaction is present,
the joint complete frontier must be updated as one object; serializing its
pieces cannot define a preferred time order.

## 7. Joint matter--geometry closure

The coupled solution has two independent response directions.

### 7.1 Matter changes geometry

At fixed $G_N$, changing the conserved matter magnitude changes expansion:

\[
\frac{\partial\dot V}{\partial|P|}
=\sqrt{12\pi G_N}.
\]

The ablation $P=0$ has $\dot V=0$ and vanishing curvature. A mutation of
(|P|) therefore moves a geometric future while holding the law fixed.

### 7.2 Geometry changes matter

At fixed $P$, the scalar response is

\[
\dot\phi=\frac{P}{V}.
\]

Expansion suppresses the local scalar rate, equivalently producing the
Hubble-friction term in (KG). Changing the geometric frontier $V$ while
holding $P$ fixed changes a later matter reading.

### 7.3 Sign control

The mutation $P\mapsto-P$ leaves $V$, $H$, and every curvature scalar
unchanged while reversing the scalar trajectory. A candidate that changes
geometry under this sign flip has copied an orientation label into the stress
sector. A candidate that fails to reverse $\phi$ has erased matter data.

Together these statements establish, inside the declared control family,

`P16-DECLARED-3+1-EINSTEIN-SCALAR-JOINT-CLOSURE`.

The word `DECLARED` is load-bearing.

## 8. Dynamical curvature and observable response

For a flat FLRW metric,

\[
R=6(\dot H+2H^2).
\]

Using the exact solution,

\[
R
=-\frac{8\pi G_NP^2}{V^2}.
\]

Thus curvature changes along the joint history and obeys

\[
\dot R+6HR=0,
\qquad
RV^2=-8\pi G_NP^2.
\]

The Kretschmann invariant is

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=
\frac{20}{27}
\frac{\kappa^4P^4}{V^4}.
\]

This distinguishes nonzero curvature from a coordinate artifact. The
expanding solution has a past singular boundary at $V=0$; this draft does
not resolve it.

For a freely propagating null probe between complete frontiers,

\[
1+z=\frac{a_2}{a_1}
=\left(\frac{V_2}{V_1}\right)^{1/3}.
\]

Matter therefore changes a geometric redshift prediction through its effect
on $V$, and the resulting geometry changes later matter/probe response. The
conditional outcome is

`P16-DECLARED-FLRW-DYNAMICAL-CURVATURE-AND-REDSHIFT-RESPONSE`.

No local gravitational radiation, tidal anisotropy, black hole, or generic
inhomogeneous propagation is represented by this homogeneous sector.

## 9. Fit once, test elsewhere

The coupling may be estimated once from expansion and matter momentum:

\[
G_F=\frac{\dot V^2}{12\pi P^2}.
\]

That fitted value is then held fixed. The following must agree without
refitting:

\[
G_R=-\frac{RV^2}{8\pi P^2},
\]

\[
\dot H=-4\pi G_F\frac{P^2}{V^2},
\]

\[
\ddot\phi+3H\dot\phi=0,
\]

\[
\dot P=0,
\]

the finite semigroup law, and the redshift law. At least one test must use a
held-out frontier interval and one must use a changed $P$ magnitude.

These equations are not statistically independent: diffeomorphism invariance
and the contracted Bianchi identity make part of the reduced system
algebraically dependent. A future receipt must disclose the dependency graph
and must not count algebraic consequences as independent confirmations.

The honest conditional result is

`P16-CONDITIONAL-GR-HOMOGENEOUS-MASSLESS-SCALAR-SECTOR-RECOVERED`.

It means that one independently declared covariant action and one coupling
generate mutually consistent matter, geometry, curvature, and probe
predictions. It does not mean that ISP has selected that action or recovered
generic GR.

## 10. Gates required for physical promotion

Before any `Gamma-derived GR` wording is permitted, one construction must
derive all of the following from the accepted point-free law:

1. a varying-size family whose stable-happening bundles are physical objects;
2. intrinsic chronological order rather than serialized dependency;
3. complete spatial frontiers or an equivalent covariant regional carrier;
4. a $3+1$ dimension and Lorentzian signature;
5. an extensive regional measure that descends under relabeling and harmless
   refinement;
6. a proper-duration calibration independent of an implementation clock;
7. a matter field or excitation and an independently defined momentum/flux;
8. an independently derived stress map, not $G/(8\pi G_N)$;
9. a geometry update that responds when matter input changes;
10. a later matter response that changes when geometry changes;
11. a single constant $G_N$ that survives held-out regions, inputs, and
    scales;
12. Hamiltonian/diffeomorphism constraint closure or an equivalent covariant
    no-hidden-clock theorem;
13. a continuum/scaling regime in which discrete errors are controlled;
14. complete-frontier future sufficiency and positive normalized kernels;
15. independence of incomparable local update serialization.

Failure of a gate lowers only its coordinate. A stable happening may survive
while a frontier, metric, stress map, or Einstein closure fails.

## 11. Hostile controls

The future pin should contain at least these changed objects.

| ID | Changed object | Required disposition |
|---|---|---|
| G1 | Treat the $1+1$ scalar curvature as a nonzero Einstein tensor | Refuse at dimension gate |
| G2 | Define $T_{\mu\nu}=G_{\mu\nu}/(8\pi G_N)$ after constructing geometry | Refuse as circular stress |
| G3 | Change $P$ but replay cached $V(\tau)$ | Joint-response gate false |
| G4 | Change $V$ but replay cached $\phi(\tau)$ | Reverse-response gate false |
| G5 | Send $P\mapsto-P$ and move curvature | Sign-control failure |
| G6 | Send $P\mapsto-P$ without reversing $\phi$ | Matter-lineage failure |
| G7 | Insert a potential $U(\phi)$ while retaining massless equations | Refuse changed theory |
| G8 | Flip the scalar kinetic sign | Refuse ghost/wrong stress |
| G9 | Fit a different $G_N$ on every frontier or observable | Held-out closure false |
| G10 | Use coordinate increment $d\lambda$ as duration under a lapse change | No-hidden-clock failure |
| G11 | Factor through an incomplete local happening | Division-frontier failure |
| G12 | Serialize incomparable regional updates and retain an order effect | Covariance failure |
| G13 | Rescale the fiducial comoving cell and change dimensionless observables | Cell-gauge failure |
| G14 | Copy the final Einstein residual boolean instead of recomputing tensors | Dependency/receipt failure |
| G15 | Omit the $P=0$ sector or evaluate $\operatorname{sgn}(0)$ | Totality failure |
| G16 | Fit Friedmann and count Bianchi-dependent Raychaudhuri as independent evidence | Evidence-scope failure |
| G17 | Keep identical $(V,P)$ but alter $R$ or redshift | Curvature/probe inconsistency |
| G18 | Claim generic GR from the homogeneous scalar sector | Ontology/scope refusal |

Fresh controls must additionally alter the equation of state, introduce
inhomogeneous modes, perturb the lapse, vary the scale window, and test a
second matter model. They are future evidence obligations, not present
results.

## 12. Outcome coordinates

The outcome is product-valued rather than one heroic ladder:

- `CARRIER`: unconstructed / declared / Gamma-derived;
- `ORDER`: dependency / chronological candidate / covariant chronology;
- `MEASURE`: count / calibrated volume candidate / physical volume;
- `DURATION`: rank / calibrated local duration / physical proper time;
- `MATTER`: label / covariant field candidate / independently derived stress;
- `RESPONSE`: one-way / reciprocal / joint law closure;
- `CURVATURE`: fitted / dynamically predicted / held-out reconstructed;
- `GR`: none / conditional sector / generic covariant recovery;
- `ACTUALITY`: postulated / otherwise independently earned.

The earliest-stop labels for this draft are:

```text
P16-1+1-EINSTEIN-TENSOR-IDENTICALLY-ZERO
P16-3+1-CARRIER-UNCONSTRUCTED
P16-INDEPENDENT-STRESS-MAP-UNCONSTRUCTED
P16-JOINT-MATTER-GEOMETRY-RESPONSE-UNPROVEN
P16-DYNAMICAL-CURVATURE-UNPROVEN
P16-HELD-OUT-EINSTEIN-CLOSURE-UNPROVEN
P16-DECLARED-3+1-EINSTEIN-SCALAR-JOINT-CLOSURE
P16-DECLARED-FLRW-DYNAMICAL-CURVATURE-AND-REDSHIFT-RESPONSE
P16-CONDITIONAL-GR-HOMOGENEOUS-MASSLESS-SCALAR-SECTOR-RECOVERED
P16-GAMMA-DERIVED-GENERIC-GR-UNPROVEN
```

The conditional sector labels are compatible with the physical programme
remaining at an earlier coordinate.

## 13. Current boundary

The draft has achieved an exact conditional target:

- the $1+1$ ordinary-Einstein route is ruled out structurally;
- a $3+1$ covariant matter action and geometric action are declared
  independently;
- their homogeneous reduction has an exact finite-frontier semigroup;
- matter changes expansion and curvature;
- geometry changes the later scalar and null-probe response;
- one fixed $G_N$ controls Friedmann, Raychaudhuri, curvature, conservation,
  and redshift predictions.

The physical status is nevertheless

`P16-CONDITIONAL-GR-BRIDGE-NOT-YET-PHYSICAL`.

The missing step is not another Python verifier repair. It is a physics
construction: derive the regional carrier, chronological order, volume,
duration, matter stress, and reciprocal geometry update from the same
point-free Gamma law, then demonstrate their continuum and constraint
closure. Until that exists, the continuum action is a target and calibration
language, not an emergent result.

## References

1. A. Einstein, “The Foundation of the General Theory of Relativity,”
   *Annalen der Physik* 49 (1916).
2. R. M. Wald, *General Relativity*, University of Chicago Press (1984),
   especially Chapters 3, 4, and 5.
3. S. W. Hawking and G. F. R. Ellis, *The Large Scale Structure of
   Space-Time*, Cambridge University Press (1973).
4. D. Baumann, [“TASI Lectures on Inflation”
   (2009)](https://arxiv.org/abs/0907.5424), for the covariant scalar action,
   stress tensor, and homogeneous Friedmann system.
5. S. Carlip, “Quantum Gravity in 2+1 Dimensions,” Cambridge University
   Press (1998), for dimensional sensitivity of Einstein dynamics; the
   two-dimensional identity used here follows directly from the Riemann
   tensor algebra.
