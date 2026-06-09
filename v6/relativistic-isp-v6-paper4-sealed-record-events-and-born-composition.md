# Paper 4 (v6) - Sealed Record Events, Born Composition, and Record Gravity

## 0. Thesis

This paper states the v6 sealed-record ontology without relying on Paper 3's
campaign history.

Relative to the v1-v5 papers, this is deliberately a change of primitive, not
a simple summary. The earlier program starts from exact stochastic transition
or transport laws and reads exchange holonomy as their observable
noncommuting shadow. This paper tests the inverse presentation: the complete
closed exchange-holonomy ledger is treated as the finite intrinsic encoding of
the whole sealed record process. If that ledger fails to reconstruct the same
transport/readout data, the presentation fails. If it succeeds, it is a
compressed ontology for the same indivisible process content.

To avoid notation collision with earlier uses of `Gamma_D` for transition
kernels and `U_D` for unitary lifts, this paper uses:

```text
mu_D:
  the finite count/reference law;

P_D^{hist}:
  the whole sealed history law on finite record atoms.
```

The primitive object is not a causal-set atom, a detector click, or a Markov
transition. It is a sealed finite record diamond carrying an internal
exchange-defect holonomy. A primitive objective event is a complete,
count-symmetric idempotent readout of that holonomy.

The single-diamond law is:

```text
event = complete count-symmetric idempotent modular proposition;
eventless repair = remove the holonomy defect and return the count-dual base;
primitive law = KL holonomy content equals Fisher holonomy capacity.
```

In formulas:

```text
E^2 = E;
Var_mu(q_raw | E) = 0;
E <-> 1-E under mu;
q = 2E - 1;
Pi_0 P_eta = mu;
D(P_eta || mu) = Var_{P_eta}(q).
```

This fixes the primitive one-diamond constants:

```text
eta_*   = 1.090344354879492;
theta_* = 0.797003794162878;
W_*=J_* = 0.364784952089976.
```

This does not by itself derive Born or non-Markovian dynamics. Born and
observable non-Markovianity live in the composition rule for multiple sealed
diamonds. The finite two-diamond campaign below shows that if retained
exchange holonomy composes linearly and sealed screen transport preserves
total event weight, the Born exponent `2` is selected inside that composition
packet. The linear retained-holonomy rule and the invariant screen norm are
therefore load-bearing composition hypotheses, not consequences of a single
diamond.

There are two faces of the law. The single-diamond event law is a real
positive RN/readout law: it fixes a binary record proposition, its count-dual
reference, and its information-geometric scale. Phase, interference, and the
Born role live in the retained exchange-holonomy composition law between
diamonds. A purely real Gibbs tilt is only the positive readout face; it is
not the whole phase-sensitive ISP process.

Gravity is treated in the same spirit. It is not added as an external metric
or a post-event stress-energy source. In the finite v6 gravity campaigns,
shared eventless collars define the allowed-change operator, deletion/RN work
fixes the source amplitude in the scoped packet, and source conservation is
derived as a cellular coboundary of complete interface holonomy. This is a v6
finite-cellular extension of the v1-v5 boundary-flux/seam-cancellation
discipline, not a claim that v1-v5 already proved the general coboundary law
at arbitrary continuum scope.

## 1. Sealed finite record diamond

A sealed finite record diamond `D` consists of:

```text
Omega_D:
  a finite record atom set;

mu_D:
  the count/reference law on Omega_D;

lower and upper screens:
  internally ordered boundary record surfaces;

collar data:
  the record information preserved by eventless repair;

internal transports:
  record comparison maps between screen/collar readouts.
```

"Sealed" means no observer slicing, coordinate clock, or external detector
label is allowed to define the event. All event data must be recoverable from
the diamond's internal record algebra, screen/collar structure, count
reference, and transport relations.

## 2. Exchange-defect holonomy

Let `T_A` and `T_B` be two internally available record transports across the
diamond. Their exchange defect is:

```math
\Delta_{AB}=T_BT_A-T_AT_B.
```

The exchange defect is the source of modular contrast. The raw contrast
`q_raw` is an internally normalized scalar readout of `Delta_AB`. The
important point is:

```text
the physical tilt is not by arbitrary continuous q_raw.
```

The tilt is by the complete event readout extracted from `q_raw`.

## 3. Primitive event identity

A primitive event is a record proposition `E` satisfying:

```math
E^2=E.
```

In a finite commutative record algebra this means:

```math
E(a)\in\{0,1\}.
```

The event is complete for the holonomy contrast if:

```math
{\rm Var}_{\mu_D}(q_{\rm raw}|E)=0.
```

Thus `q_raw` has no residual interior value once the event/no-event readout is
known. Equivalently, `q_raw` is affine in `E`.

The event is count-symmetric if the sealed count/reference structure contains
an internal `mu_D`-preserving complement symmetry:

```math
E\leftrightarrow 1-E.
```

This implies:

```math
\mu_D(E=0)=\mu_D(E=1)=1/2.
```

Therefore the normalized primitive contrast is:

```math
q=2E-1,
\qquad
q^2=1,
\qquad
\mu_D(q=-1)=\mu_D(q=+1)=1/2.
```

This is the finite event identity:

```text
objective event = complete count-symmetric idempotent modular proposition.
```

## 4. Eventless repair

The eventless repair `Pi_0` is not pinching by the event label. It is the
collar-preserving repair that removes the exchange-defect holonomy.

For the primitive event law:

```math
\Pi_0P_\eta=\mu_D.
```

This is essential. If one instead uses event-label pinching `Pi_E`, then the
event law is already diagonal in `E` and:

```math
D(P_\eta\Vert \Pi_E P_\eta)=0,
```

so the balance degenerates. The nonzero work is:

```math
D(P_\eta\Vert \Pi_0P_\eta)=D(P_\eta\Vert\mu_D).
```

## 5. Single-diamond law

The primitive law is the exponential tilt of the count-dual eventless base by
the idempotent contrast:

```math
P_\eta(q)
=
{e^{\eta q}\over 2\cosh\eta},
\qquad
q\in\{-1,+1\}.
```

The log partition function is:

```math
\psi(\eta)=\log(2\cosh\eta)-\log2.
```

The Fisher screen response is not a black box. It is the log-partition
Hessian:

```math
J(\eta)
=
{d^2\psi\over d\eta^2}
=
{\rm Var}_{P_\eta}(q)
=
1-\tanh^2\eta.
```

The information-geometric saturation law is:

```math
D(P_\eta\Vert\mu_D)=J(\eta).
```

Equivalently:

```math
\eta\tanh\eta-\log\cosh\eta
=
1-\tanh^2\eta.
```

This is not an FDT identity. The identity:

```math
{d\over d\eta}E_\eta[q]= {\rm Var}_{P_\eta}(q)
```

is automatic for exponential families. The independent principle is:

```text
KL content accumulated by the primitive event equals the Fisher capacity of
the same holonomy contrast.
```

This balance has one nonzero solution:

```text
eta_*   = 1.090344354879492;
theta_* = tanh eta_* = 0.797003794162878;
W_*=J_* = 0.364784952089976.
```

## 6. Single-diamond diagnostic

The finite diagnostic is:

```text
code/v6_p4a_single_diamond_event_law.py
```

Its audit is:

| target | check | result | value | verdict |
|---|---|---|---:|---|
| idempotent event | E^2=E and q=2E-1 | q^2=1 | q in {-1,+1} | PASS |
| count-dual base | internal complement E <-> 1-E | mu=(-,+)=(1/2,1/2) | mu fixed | PASS |
| eventless repair | Pi_0 kills holonomy contrast | Pi_0 P_eta = mu | explicit assumption/definition | PASS-SCOPED |
| Fisher term | d^2 log Z / d eta^2 | Var_{P_eta}(q) | 0.364784952089976 | DEFINED |
| information-geometric saturation | D(P_eta\|\|mu)=Var(q) | unique crossing | eta=1.090344354879492 | PASS |
| fixed primitive constants | forced by q^2=1 and count-duality | theta, eta, W=J | 0.797003794162878, 1.090344354879492, 0.364784952089977 | PASS |
| pinch trap | Pi_E P_eta instead of Pi_0 P_eta | D(P\|\|Pi_E P)=0 | degenerate | FAILS |
| continuous-score tilt | tilt by raw q_D with 3 score levels | root moves | eta=1.149609196641639 | FAILS-UNIVERSALITY |
| unbalanced binary | drop complement count-duality | root moves | eta=1.166712545484554 | FAILS-UNIVERSALITY |

Thus the constants are canonical only because:

```text
E^2=E;
q=2E-1;
q^2=1;
mu(q=-1)=mu(q=+1)=1/2.
```

If any of these are weakened, the constants move or the balance degenerates.

## 7. Scope of the single-diamond law

The single diamond fixes a primitive event law. It does not yet define:

```text
Born probabilities for arbitrary preparations;
interference between alternatives;
Barandes-style indivisible stochastic dynamics;
observable non-Markovian signatures.
```

Those are composition questions. A single diamond has no memory because there
is no previous or next diamond for it to remember.

## 8. Two-diamond composition packet

The minimal composition packet introduces retained exchange holonomy.

Let two alternatives contribute complex holonomy amplitudes:

```math
c_0,
\qquad
c_1=e^{i\phi}c_0
```

to the next sealed screen. The composed screen amplitudes are:

```math
a_+
=
{c_0+c_1\over\sqrt2},
\qquad
a_-
=
{c_0-c_1\over\sqrt2}.
```

The Born role asks why event weights are:

```math
P(\pm)=|a_\pm|^2.
```

The finite conditional answer is:

```text
If retained holonomy amplitudes add linearly and sealed screen transports
preserve total event weight under Hadamard screen changes, then the p-norm
family selects p=2.
```

For a general `p`-weight:

```math
W_p(a)=\sum_i |a_i|^p,
```

Hadamard transport sends:

```math
(1,0)\mapsto(1/\sqrt2,1/\sqrt2).
```

Total weight is preserved only if:

```math
1
=
2(1/\sqrt2)^p,
```

hence:

```math
p=2.
```

Thus the exponent `2` is not supplied by the single-diamond balance. It is
selected by the composition packet:

```text
linear retained holonomy + screen-weight invariance.
```

The hard theorem is exactly the premise: derive linear retained-holonomy
composition and the invariant screen norm from the whole sealed process law.
Without those premises, this section is a finite selection theorem, not a
universal Born-rule derivation.

## 9. Two-diamond diagnostic

The finite diagnostic is:

```text
code/v6_p4b_two_diamond_born_composition.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| single diamond | one event law only | no phase composition; no Born role | not typed | FAIL-BORN-SCOPE |
| classical composition | discard retained holonomy | no interference | phase span=0.000 | FAIL-BORN |
| complex holonomy composition | amplitudes add before event readout | interference appears | P+(0,pi/3,pi/2,pi)=1.000,0.750,0.500,0.000 | PASS-INTERFERENCE |
| p-norm family | replace squared norm by p-norm | many phase-sensitive rules exist | p=1 at pi/3 0.634; p=4 at pi/3 0.900 | FAIL-UNIQUE-WITHOUT-INVARIANCE |
| screen transport invariance | Hadamard preserves total event weight | selects p=2 | p*=2.000000000000 | SELECTS-P2-GIVEN-INVARIANCE |
| p=2 check | p-norm rule equals squared amplitude | matches Born row | max gap=2.2e-16 | PASS |
| p != 2 attack | Hadamard total weight error | p=1.0: 0.414, p=2.0: 0.000, p=3.0: 0.293, p=4.0: 0.500 | only p=2 has zero error | REFUTES-OTHER-EXPONENTS |
| visible non-Markovianity | retain hidden holonomy then marginalize it | visible event process fails first-order Markov | gap=0.130069 | PASS-VISIBLE-NONMARKOV |
| Barandes-level warning | hidden-state model is still a Markov completion upstairs | not yet full indivisible-process theorem | composition target remains | HONEST-SCOPE |
| Born role verdict | linear holonomy + unitary screen invariance | quadratic weighting is selected inside composition packet | not from single diamond alone | CONDITIONAL-SELECTION |

The two-diamond calculation gives the familiar interference pattern:

```text
P_+(0)     = 1.000;
P_+(pi/3)  = 0.750;
P_+(pi/2)  = 0.500;
P_+(pi)    = 0.000.
```

Classical composition gives no phase dependence. The `p`-norm family gives
phase dependence but no invariant exponent until screen transport invariance
is imposed. That invariance selects:

```text
p=2.
```

## 10. Non-Markovianity in the composition campaign

The finite diagnostic also tests retained hidden holonomy. A hidden holonomy
state persists between events; visible event outcomes are emitted from it and
the hidden holonomy is then marginalized. The visible three-event law fails
the first-order Markov condition:

```text
max |P(X_3=1|X_2,X_1)-P(X_3=1|X_2)| = 0.130068881646990.
```

This is an observable non-Markovian signature at the visible event level.

It is not yet the full Barandes theorem. The toy model still has a Markov
completion upstairs in the retained holonomy. The Barandes-level target is
stronger:

```text
construct a whole composed sealed-diamond process whose event statistics have
the intended indivisible-process structure, not merely a hidden Markov model.
```

## 11. Gravity attachment without leaving the stochastic ontology

Gravity must be attached at the composition level. A single sealed diamond can
define an event, but it cannot define curvature, source propagation, or
non-Markovian record response. Those require neighboring diamonds and shared
collars.

The Barandes-aligned demand is:

```text
do not add a metric field after the stochastic law;
derive the gravitational response as a property of how sealed record laws
compose.
```

Thus the gravity object is not:

```text
event set + external stress-energy map + external metric equation.
```

It is:

```text
sealed diamond network
-> eventless collar transport
-> intrinsic allowed-change operator
-> deletion source from the same primitive event law
-> stochastic deformation of future record transport.
```

Let a finite composed packet contain sealed diamonds indexed by `i`. The shared
eventless collars define an ordinary stochastic base transport:

```math
K_0(i,j).
```

Equivalently, the collar adjacency/conductance defines a graph Laplacian:

```math
L = D-A.
```

This is the finite allowed-change operator. It is not a metric supplied from
outside. It is the invariant expression of eventless record transport across
the shared collars.

The source is the deletion response of the same primitive event law. The
single-diamond event balance fixed:

```math
W_*
=
D(P_{\eta_*}\Vert\mu)
=
J(\eta_*)
=
0.364784952089976\ldots .
```

For a sealed finite packet with primitive event support `E_i in {0,1}`, the
compact source is the centered deletion source:

```math
\rho_i
=
W_*(E_i-\bar E),
\qquad
\bar E={1\over N}\sum_i E_i.
```

The centering is not a free subtraction. In a sealed finite packet the constant
mode of `L` is gauge, so a source with nonzero total charge cannot be solved
without declaring a boundary flux. If the packet has an external screen flux,
that flux must be part of the sealed boundary data. In the closed finite
packet, the only intrinsic source is the mean-zero deletion response.

The finite record-gravity equation is:

```math
L\phi=\rho,
\qquad
\sum_i\phi_i=0.
```

The potential `phi` is not itself a new ontology. It is a representation of how
the event history deforms future eventless transport. The corresponding future
stochastic law is the ordinary probability tilt:

```math
K_\phi(i,j)
=
{K_0(i,j)\exp[-(\phi_j-\phi_i)/2]
 \over
 \sum_k K_0(i,k)\exp[-(\phi_k-\phi_i)/2]}.
```

Only potential differences enter. Therefore:

```text
phi -> phi + constant
```

changes no transition probability. This is the finite slice/gauge test.

The gravity slogan becomes precise:

```text
gravity = curvature/response of indivisible record transport.
```

In the finite linear packet:

```text
curvature = L phi;
source    = deletion response rho;
future stochastic law = K_phi.
```

No Hilbert state, wavefunction, detector frame, or external metric has been
introduced.

## 12. Gravity diagnostic

The finite diagnostic is:

```text
code/v6_p4c_barandes_aligned_gravity.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| eventless collar transport | shared sealed collars define symmetric K0 | ordinary stochastic base law | row_err=0.0e+00 | PASS |
| allowed-change operator | L = degree - collar adjacency | constant mode is gauge | max\|L1\|=0.0e+00 | PASS |
| fixed source amplitude | primitive deletion work W*=D(P_eta\|\|mu) | kappa fixed by one-diamond law | W*=0.364784952089977 | PASS-SCOPED |
| deletion source | rho_i=W*(E_i-mean E) | sealed source has zero total charge | sum rho=5.6e-17 | PASS |
| record-gravity equation | L phi = rho, sum phi=0 | curvature equals deletion source | residual=8.3e-17, span(phi)=0.182392 | PASS |
| stochastic future law | K_phi tilts K0 by potential differences | ordinary row-stochastic transition law | row_err=1.1e-16, KL=0.000390 | PASS |
| slice/gauge freedom | phi -> phi + constant | future law unchanged | kernel_gap=1.1e-16 | PASS |
| eventless vacuum | no event support | rho=0, phi=0, K_phi=K0 | kernel_gap=0.0e+00 | PASS |
| no-silent-seam attack | use uncentered source in sealed network | violates solvability constraint | sum source=1.094355 | FAILS |
| free-amplitude attack | same support, vary kappa | gravity work changes | work_span=0.001751 | FAILS-BRANCH-A |
| split-source attack | same event count, different source support | response field changes while source no longer equals event | same_count=True, phi_gap=0.341986 | FAILS-ONE-EVENT |
| external-collar attack | add one non-intrinsic chord to the collar graph | gravity response changes | work_gap=0.000061, span=0.182392->0.182392 | FAILS-INTRINSICITY |
| visible memory | same present diamond, different retained event history | next transition differs | kernel_gap=0.045567 | PASS-COMPOSITION |
| gravity attachment verdict | source, amplitude, L, and K_phi from sealed record data | finite Barandes-aligned gravity packet closes only in this scoped sense | not a continuum Einstein-equation theorem | HONEST-CLOSURE |

The numerical source and response in the test packet are:

```text
primitive_work = 0.364784952089977

rho =
  0.227990595056 -0.136794357034 -0.136794357034 0.227990595056
 -0.136794357034  0.227990595056 -0.136794357034 -0.136794357034

phi =
  0.034198589258 -0.079796708270 -0.056997648764 0.102595767775
  0.034198589258  0.102595767775 -0.056997648764 -0.079796708270

max |L phi - rho| = 8.326672684688674e-17
```

This is the finite gravity receipt. In a closed collar packet, the eventless
transport fixes `L`; the primitive event law fixes `W_*`; the event support
fixes `rho`; the gauge-fixed equation fixes `phi`; and `phi` fixes the next
ordinary stochastic transport `K_phi`.

## 13. What this gravity campaign proves and does not prove

It proves a finite branch-A-compatible attachment:

```text
same event support -> deletion source;
same primitive law -> source amplitude;
same eventless collar -> allowed-change operator;
same response field -> future stochastic law.
```

It also proves four useful failure facts.

First, source support alone is not enough. A split source with the same event
count produces a different response field while no longer being the same event.
That is branch B.

Second, an uncentered source cannot be silently inserted into a sealed compact
packet. It requires boundary flux data. That flux may be physical, but it must
belong to the sealed screen.

Third, a free gravitational coefficient is not harmless. Varying `kappa` while
holding event support fixed changes the gravitational work. Therefore the
coefficient must be the primitive deletion work `W_*`, or the theory has
introduced a phenomenological gravity parameter.

Fourth, the collar graph cannot be chosen for convenience. Adding one
non-intrinsic chord changes the response. The allowed-change operator must be
the eventless collar transport supplied by the sealed record packet.

The finite attachment by itself is not yet a continuum Einstein-equation
theorem. It leaves a precise refinement question:

```text
finite sealed collar transport L_n
-> refinement-stable causal screen geometry
-> continuum curvature tensor / Einstein tensor
-> stress-energy readout from deletion response.
```

The next campaign solves the first bridge in a scoped class: count-uniform
sealed collar refinements on a compact one-screen packet.

But the attachment is Barandes-aligned in the precise sense needed here:

```text
the primitive process remains an ordinary stochastic process on record
configurations;
the quantum-like phase data remain retained exchange holonomy;
observable non-Markovianity appears through composition/history;
gravity is a deformation of future stochastic transport, not a new primitive
field glued onto the process.
```

The full gravity theorem target is now:

```text
For every refinement-stable sealed-diamond network, eventless collar transport
converges to a covariant local differential operator L, primitive deletion
sources converge to a conserved stress-energy readout, and the finite
record-gravity equation L phi = rho converges to the appropriate gravitational
field equation.
```

If the full theorem holds, gravity is internal to the indivisible stochastic
record law. If it fails, Paper 4 still gives a coherent finite stochastic event
ontology, but gravity must be added in branch-B form beyond the solved finite
and scalar-refinement packets.

## 14. Refinement gravity theorem campaign

The Einstein pressure point is:

```text
Is L phi = rho an invariant continuum law, or only a finite graph trick?
```

There is an exact positive answer in the simplest sealed refinement class.
Take a compact one-screen packet with `n` count-dual collar atoms and no
distinguished origin. The intrinsic count spacing is:

```math
h_n={1\over n}.
```

Eventless collar transport connects each atom only to its two adjacent collar
atoms. The count-uniform allowed-change operator is:

```math
L_n
=
h_n^{-2}(D-A)
=
n^2(D-A).
```

The factor `h_n^{-2}` is not a tunable coupling. It is the unique scaling that
keeps the eventless one-step collar variance finite under count refinement.
Without it, the response field diverges under refinement.

For a centered deletion source:

```math
\rho_n(i)
=
W_*(E_n(i)-\bar E_n),
```

or a smooth coarse-grained event density with the same fixed amplitude `W_*`,
solve:

```math
L_n\phi_n=\rho_n,
\qquad
\sum_i\phi_n(i)=0.
```

In the smooth-source case, `L_n` is the standard second-order finite
difference approximation to `-\partial_x^2`. Therefore:

```math
\phi_n\to\phi,
\qquad
-\phi''=\rho,
\qquad
\int_0^1\phi\,dx=0.
```

The tilted future transport:

```math
K_{\phi_n}(i,i\pm1)
\propto
\exp[-(\phi_n(i\pm1)-\phi_n(i))/2]
```

has continuum drift:

```math
n\{K_{\phi_n}(i,i+1)-K_{\phi_n}(i,i-1)\}
\to
-{1\over2}\partial_x\phi.
```

Thus in this sealed collar class:

```text
eventless collar refinement -> continuum allowed-change operator;
primitive deletion work      -> fixed source amplitude;
event support/density        -> centered source;
record-gravity equation      -> continuum Poisson response;
future stochastic transport  -> drift from the same response field.
```

This solves the first continuum gate. It does not yet produce the full
Einstein tensor. It proves that the finite record-gravity law is not merely a
finite graph artifact when the sealed collar refinement is count-uniform and
local.

## 15. Refinement diagnostic

The finite diagnostic is:

```text
code/v6_p4d_refinement_gravity_limit.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| scaled collar limit | L_n=h^-2(degree-adjacency), h=1/n | smooth Poisson response converges | err32/64/128/256=4.171e-05/1.040e-05/2.598e-06/6.494e-07 | PASS |
| curvature/source identity | apply L_n to solved phi_n | L_n phi_n equals rho_n to numerical precision | res=1.4e-13/1.1e-12/8.7e-12/8.0e-11 | PASS |
| binary event-source refinement | E_n is interval support, rho_n=W*(E_n-mean E_n) | coarse/fine potentials stabilize | gap32-64/64-128/128-256=2.672e-04/1.336e-04/6.679e-05 | PASS |
| future transport limit | K_phi nearest-neighbor tilt | scaled drift converges to -1/2 grad phi | err32/64/128/256=1.467e-04/3.664e-05/9.156e-06/2.289e-06 | PASS |
| unscaled collar attack | use degree-adjacency without h^-2 | potential span grows with refinement | span32/64/128=1.898e+01/7.576e+01/3.028e+02 | FAILS |
| external chord attack | add nonlocal collar edge before solving | limit no longer matches local continuum operator | err64=8.699e-03 | FAILS-INTRINSICITY |
| alternating weight attack | alternate collar conductances not implied by count-uniform screen | converges to a different variable-coefficient geometry | err64=2.533e-03 | FAILS-UNIFORM-GEOMETRY |
| free source-amplitude attack | replace W* by 2W* | continuum response changes linearly | phi_gap64=1.017e-02 | FAILS-BRANCH-A |
| refinement theorem verdict | uniform sealed collars + W* deletion sources | finite record gravity has a stable local continuum limit | scoped theorem, not full Einstein tensor | FINITE-CLOSURE |

The important numbers are:

```text
primitive_work = 0.364784952089977

smooth source errors:
  4.171022146332373e-05
  1.039950558033229e-05
  2.598130446644295e-06
  6.494236021413469e-07

binary event-source refinement gaps:
  2.671764785815637e-04
  1.335882392907721e-04
  6.679411964562306e-05

future drift errors:
  1.467110154173418e-04
  3.663505226041142e-05
  9.156101906139524e-06
  2.289215645243786e-06
```

The failures are as important as the pass. If the `h^{-2}` scaling is removed,
the potential span grows:

```text
18.98466174605557,
75.75581431353692,
302.8407548620417.
```

If a nonlocal chord is added, or if alternating collar weights are supplied
without being forced by the sealed record law, the response converges to a
different operator. That is not a paradox. It says that different intrinsic
eventless collar laws define different geometries. The branch-A requirement is
not "all graphs give the same continuum." The requirement is:

```text
the sealed record process itself must supply the collar law and refinement
class.
```

Within the count-uniform local class, the scalar continuum gate is closed.

## 16. Causal-screen tensor campaign

The scalar ring collar proves that the record-gravity equation can have a
continuum limit. It does not yet show that sealed record transport determines
spacetime geometry. The next test is a two-dimensional causal screen with a
local conductance tensor.

Let the sealed screen be a count-uniform `n x n` collar packet with local
eventless collar edges in four undirected directions:

```text
x direction;
y direction;
diagonal direction (1,1);
anti-diagonal direction (1,-1).
```

With nonnegative collar conductances:

```math
w_x,\quad w_y,\quad w_d,\quad w_a,
```

the screen supplies the symmetric conductance tensor:

```math
G
=
w_x
\begin{pmatrix}1&0\\0&0\end{pmatrix}
+
w_y
\begin{pmatrix}0&0\\0&1\end{pmatrix}
+
w_d
\begin{pmatrix}1&1\\1&1\end{pmatrix}
+
w_a
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
```

This is the first real tensor-like geometry object in Paper 4. It is still a
screen conductance tensor, not the Einstein tensor. Its scaled collar operator
is:

```math
L_n=n^2B^TCB,
```

where `B` is the finite incidence/difference map and `C` is the diagonal
conductance form on collar edges. For smooth sources:

```math
L_n\phi_n\to-\nabla_a(G^{ab}\nabla_b\phi).
```

The same primitive deletion work supplies the source amplitude:

```math
\rho_n=W_*(E_n-\bar E_n)
```

or its smooth coarse-grained density. The same potential-difference tilt of
all local collar edges supplies future stochastic transport. In the continuum
limit, the drift is:

```math
v
=
-{G\nabla\phi\over 2\sum_e w_e}.
```

This is the correct record-gravity extension of the 1D result:

```text
sealed screen collar conductance
-> intrinsic conductance tensor G
-> Laplace-Beltrami-type scalar response
-> conserved centered deletion source
-> stochastic drift from the same response field.
```

The finite scalar Bianchi analogue is exact:

```math
\mathbf 1^T L_n = 0.
```

Therefore a closed screen cannot accept a source with nonzero total deletion
charge unless boundary flux is part of the sealed screen data. This is the
same no-silent-seam rule in tensor-screen form.

But this is not the full contracted Bianchi identity. A scalar potential
equation has one response component per screen atom. A two-dimensional
symmetric tensor equation has three components per atom, with differential
constraints. The diagnostic therefore rejects the overclaim:

```text
screen conductance tensor geometry closes the scalar Laplace-Beltrami gate;
it does not by itself derive the full Einstein tensor.
```

The full Einstein-style target now has a sharper form:

```text
sealed screen law
-> intrinsic record connection on screen bundles
-> curvature object with a discrete Bianchi identity
-> deletion/source tensor satisfying the same conservation identity
-> continuum Einstein equation, or a distinct record-gravity tensor equation.
```

## 17. Causal-screen tensor diagnostic

The finite diagnostic is:

```text
code/v6_p4e_screen_tensor_gravity_gate.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| screen conductance tensor | x/y/diagonal collar weights | defines SPD G with off-diagonal term | G=(1.40,0.25;0.25,1.00), wx=1.15, wy=0.75 | PASS |
| Laplace-Beltrami scalar gate | L_n=n^2 B^T C B on smooth modes | converges to -div(G grad) | err16/32/64/128=2.071e-04/5.146e-05/1.285e-05/3.210e-06 | PASS |
| curvature/source identity | apply L_n to exact discrete mode solution | recovers rho_n | res=3.9e-15/2.1e-14/8.9e-14/3.2e-13 | PASS |
| binary event-source refinement | localized event island, rho=W*(E-mean E) | coarse/fine response stabilizes | gap16-32/32-64=1.709e-04/1.298e-04 | PASS |
| CG receipt | solve singular mean-zero screen equation | iterations/residuals finite | iters=47/92/184, rms=8.0e-11/9.9e-11/8.9e-11 | PASS |
| future transport tensor drift | tilt all local collar edges by phi differences | drift tends to -G grad(phi)/(2 sum weights) | err16/32/64/128=2.548e-04/6.364e-05/1.591e-05/3.980e-06 | PASS |
| scalar Bianchi/no-silent-source | constant mode of L_n vanishes | closed screen needs zero total source | max\|L1\|=0.0e+00 | PASS |
| uncentered source attack | insert positive event charge without boundary flux | violates closed-screen conservation | sum source=1.823925 | FAILS |
| unscaled tensor attack | drop h^-2 scaling | potential span grows with refinement | span16/32/64=6.778e+00/2.685e+01/1.071e+02 | FAILS |
| nonlocal collar attack | add long chord not present in local sealed screen | local continuum tensor no longer predicts source | mismatch64=2.143e+02 | FAILS-INTRINSICITY |
| free source-amplitude attack | replace W* by 2W* | response changes linearly | phi_gap64=1.501e-02 | FAILS-BRANCH-A |
| Einstein/Bianchi overclaim | try to read full symmetric tensor equation from one scalar phi | component count does not match | missing_components=8193 | FAILS-FULL-GR |
| tensor-screen verdict | local count-uniform conductance tensor + W* sources | screen geometry gate closes; full Einstein gate remains tensorial | scalar/tensor boundary exposed | FINITE-CLOSURE |

The important numbers are:

```text
G =
  1.400000000000  0.250000000000
  0.250000000000  1.000000000000

smooth tensor-screen errors:
  2.070946755852402e-04
  5.146120853475808e-05
  1.284587455933905e-05
  3.210255992269068e-06

future tensor-drift errors:
  2.547942283458136e-04
  6.363926923133242e-05
  1.590610372311993e-05
  3.979715600899159e-06

scalar Bianchi / no-silent-source:
  max |L1| = 0.0
  uncentered source sum = 1.823924760449883
```

This is the current sharp verdict:

```text
Screen geometry gate: closed in the count-uniform local conductance class.
Full Einstein gate: still open, and now known to require a record connection
or tensor curvature object, not merely scalar conductance.
```

## 18. Causal-diamond screen-stack campaign

The two-dimensional screen result is necessary, but a single screen is not
spacetime. The next object is a nested causal-diamond screen stack:

```text
screen at radius r_0;
screen at radius r_1;
screen at radius r_2;
...
```

Each screen has its own intrinsic count-uniform conductance tensor:

```math
G_{AB}(r,x,y).
```

The new question is whether neighboring screens determine an inter-screen
connection, expansion/shear, and loop holonomy. The finite campaign tests the
minimal/no-twist record connection:

```math
\Omega_\mu
=
{1\over2}G^{-1}\partial_\mu G,
\qquad
\mu\in\{r,x,y\}.
```

For the radial direction:

```math
\Omega_r
=
{1\over2}G^{-1}\partial_rG.
```

This is metric-compatible:

```math
\partial_rG
=
\Omega_r^TG+G\Omega_r.
```

It gives finite expansion and shear:

```math
\theta={\rm tr}\,\Omega_r,
\qquad
\sigma=\Omega_r-{\theta\over2}I.
```

Since the induced screen metric is `q=G^{-1}`, the area-density identity is:

```math
\partial_r\log\sqrt{\det q}
=
-\theta.
```

The screen-stack connection has a genuine loop-curvature readout. For example:

```math
F_{rx}
=
\partial_r\Omega_x-\partial_x\Omega_r+[\Omega_r,\Omega_x].
```

The corresponding connection Bianchi identity is:

```math
D_rF_{xy}+D_xF_{yr}+D_yF_{rx}=0.
```

This is the first place Paper 4 gets a curvature identity rather than only a
scalar conservation identity.

But there is a crucial theorem boundary. The conductance tensors `G` alone do
not select the connection. If `A` is skew-symmetric, then:

```math
H=G^{-1}A
```

satisfies:

```math
H^TG+GH=0.
```

Therefore:

```math
\Omega_r\mapsto\Omega_r+H
```

preserves metric compatibility while changing holonomy. Thus branch A needs
the sealed process to derive the **minimal/no-twist inter-screen transport**.
If that transport is chosen by the analyst, the construction has a hidden
branch-B connection coefficient.

The result is also not full `3+1` gravity. A nested 2D screen stack supplies:

```text
screen metric/conductance;
radial expansion and shear;
screen-time holonomy;
connection Bianchi identity.
```

It does not yet supply:

```text
two null normals;
lapse/shift or their covariant replacement;
the full Lorentzian metric;
the full stress-energy tensor;
the contracted Bianchi identity for an Einstein tensor.
```

Thus the screen stack is the right next object, not the final theory.

## 19. Screen-stack diagnostic

The finite diagnostic is:

```text
code/v6_p4f_screen_stack_connection_gate.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| screen stack object | nested count-uniform sealed screens with G(r,x,y) | positive conductance tensor at every screen atom | min det G=7.866e-01 | PASS |
| minimal inter-screen connection | Omega_r=1/2 G^-1 d_r G | metric-compatible radial transport | compat10/20/40=9.3e-16/1.3e-15/1.4e-15 | PASS |
| expansion/shear readout | theta=tr Omega_r, sigma=Omega_r-theta I/2 | nonzero expansion/shear derived from screen evolution | shear10/20/40=1.468e+00/1.534e+00/1.550e+00 | PASS |
| area/expansion identity | q=G^-1 gives d log sqrt(det q) = -theta | finite identity converges for minimal connection | err10/20/40=8.2e-02/2.2e-02/5.7e-03 | PASS |
| screen-time holonomy | F_rx=d_r Omega_x-d_x Omega_r+[Omega_r,Omega_x] | nonzero loop curvature from screen-stack transport | max10/20/40=3.768e-01/9.529e-01/1.197e+00 | PASS |
| holonomy refinement | restrict fine F_rx to coarse stack | coarse/fine curvature stabilizes | gap10-20/20-40=6.686e-01/2.347e-01 | PASS |
| connection Bianchi identity | D_r F_xy + D_x F_yr + D_y F_rx | finite residual decreases under refinement | res10/20/40=5.818e-01/1.834e-01/4.824e-02 | PASS |
| twist freedom attack | add G-skew H=G^-1 A to Omega_r | metric compatibility survives but holonomy changes | compat=8.0e-17, hol_gap=6.171e-03 | FAILS-G-ONLY |
| radial-clock attack | rescale inter-screen derivative externally | connection/curvature scale changes | curv_gap_proxy=2.993e-01 | FAILS-IF-RADIUS-SUPPLIED |
| 3+1 overclaim attack | screen stack lacks full normal/lapse/shift data | null normals/lapse/shift not present | not a Lorentzian metric theorem | FAILS-FULL-3+1 |
| screen-stack verdict | minimal/no-twist record connection from sealed stack | connection, expansion/shear, holonomy, and Bianchi gate close | requires intrinsic no-twist/radius law | FINITE-CLOSURE |

The important numbers are:

```text
primitive_work = 0.364784952089977
min_det_G = 7.866278610665529e-01

metric compatibility residuals:
  9.288792252416251e-16
  1.339188546924366e-15
  1.386668113311984e-15

curvature refinement gaps:
  6.685502439641622e-01
  2.347134446816480e-01

Bianchi residuals:
  5.817964558399312e-01
  1.834222857046809e-01
  4.823855102400611e-02

twist attack:
  metric compatibility residual = 8.002322828458972e-17
  holonomy gap = 6.171015786734835e-03
```

This is the new status:

```text
Screen-stack connection gate:
  closed for the minimal/no-twist record connection.

Conductance-only closure:
  refuted by twist freedom.

Full 3+1 gravity:
  still open; requires intrinsic null-normal/lapse-shift data or a covariant
  replacement derived from the sealed diamond process.
```

## 20. No-twist and null-screen transport campaign

The previous section exposed a precise freedom:

```math
\Omega=\Omega_0+H,
\qquad
\Omega_0={1\over2}G^{-1}\partial_rG,
\qquad
H^TG+GH=0.
```

Equivalently:

```math
G\Omega
=
{1\over2}\partial_rG+A,
\qquad
A^T=-A.
```

Metric compatibility fixes the symmetric part:

```math
S={1\over2}\partial_rG.
```

It does not fix the skew part `A`. The no-twist campaign asks whether an
invariant sealed-record principle fixes `A=0`.

The answer is positive for eventless inter-screen transport. Define the
eventless record-work norm:

```math
\mathcal W(\Omega)
=
\langle \|G\Omega\|_F^2\rangle_{\rm screen}.
```

Since the Frobenius inner product makes symmetric and skew matrices
orthogonal:

```math
\langle S,A\rangle_F=0,
```

one has:

```math
\mathcal W(\Omega)
=
\langle \|S\|_F^2\rangle
+
\langle \|A\|_F^2\rangle.
```

Therefore the least-work eventless connection is unique:

```math
A=0,
\qquad
\Omega=\Omega_0={1\over2}G^{-1}\partial_rG.
```

The same result can be stated without optimization:

```math
{\rm skew}(G\Omega)=0.
```

This is the no-silent-circulation condition. It says that eventless
inter-screen transport may stretch and shear records as the screen changes,
but it cannot carry an oriented silent circulation around the screen fiber.
If such circulation exists, it is a physical exchange-defect source, not
eventless transport.

Two weaker ideas fail.

First, area/expansion cannot select the connection. The twist is trace-free:

```math
{\rm tr}(G^{-1}A)=0.
```

So expansion and area density do not see it.

Second, reciprocal null-pair transport does not select the connection. One may
take:

```math
\Omega_-=-\Omega_+
```

with the same nonzero twist. The pair is reciprocal, but still contains
oriented circulation. Thus null reciprocity is necessary but not sufficient.

The branch-A rule is now:

```text
eventless inter-screen transport = least record-work / no-silent-circulation
transport;
nonzero twist = exchange-defect holonomy source, not a free connection.
```

This closes the no-twist gate for eventless transport. It does not close the
radial/null-normal gate. The sealed diamond process still has to derive the
radius normalization and the two null directions or their covariant record
replacement.

## 21. No-twist diagnostic

The finite diagnostic is:

```text
code/v6_p4g_no_twist_null_transport_gate.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| metric-compatible family | Omega=Omega0+G^-1 A, A skew | all scanned twists preserve dG=Omega^T G+G Omega | max compat=1.4e-15 | FAILS-G-ONLY |
| record-work split | G Omega = symmetric S + skew A | symmetric/skew cross term vanishes | max cross=4.2e-17 | PASS |
| least eventless transport | minimize mean \|\|G Omega\|\|_F^2 over twists | unique minimum at no twist | min_tau=0.0, work_penalty_tau=.2=0.080000 | PROVES-NO-TWIST |
| no silent circulation | require skew(G Omega)=0 on eventless radial transport | selects no-twist connection | circ=0.320/0.080/0.000/0.080/0.320 | PROVES-NO-TWIST |
| area/expansion attack | compare base and twisted trace/area law | twist is invisible to expansion | trace_gap=2.2e-16, area=2.221e-02->2.221e-02 | FAILS-AREA-ONLY |
| null-pair attack | Omega_-=-Omega_+ with same twist | reciprocity passes but circulation remains | pair_res=0.0e+00, circ=0.080000 | FAILS-NULL-PAIR-ONLY |
| holonomy consequence | compute F_rx before/after twist | twist changes screen-time holonomy | hol_gap=0.006171 | PASS-PHYSICAL |
| radius-scale attack | rescale inter-screen derivative externally | least-work connection rescales too | work_gap_proxy=0.416802 | FAILS-IF-RADIUS-SUPPLIED |
| twist-source option | allow twist only as explicit exchange-defect source | free twist becomes sourced holonomy, not eventless transport | W*circ_tau=.2=0.029183 | BRANCH-A-IF-SOURCED |
| no-twist theorem verdict | metric compatibility + least work/no circulation | minimal connection is derived in the eventless stack | null/radius still need sealed data | FINITE-CLOSURE |

The decisive numbers are:

```text
record work for tau=-0.4,-0.2,0,0.2,0.4:
  1.060981807427678
  0.820981807427666
  0.740981807427669
  0.820981807427666
  1.060981807427678

circulation for tau=-0.4,-0.2,0,0.2,0.4:
  0.320000000000016
  0.080000000000004
  0.000000000000000
  0.080000000000004
  0.320000000000016

area/expansion sees no twist:
  trace gap = 2.220446049250313e-16

reciprocal null-pair still sees twist:
  pair residual = 0.0
  circulation = 0.080000000000004
```

Thus the no-twist result is no longer just an assumption. It follows from an
invariant eventless-transport law:

```text
eventless inter-screen transport minimizes record work, equivalently carries
no oriented silent circulation.
```

If the sealed process makes that law intrinsic, the no-twist gate is branch A.
If least-work/no-circulation is imposed by hand as a connection gauge, it is
branch B.

## 22. Intrinsic double-null diamond campaign

The no-twist theorem fixes eventless inter-screen transport once an intrinsic
screen direction has been supplied. The next Einstein gate is sharper:

```text
does a sealed finite diamond supply its own double-null screen stack?
```

The branch-A object is not a coordinate pair `(u,v)`. It is a pair of
opposite causal record-front directions picked out by the sealed diamond
boundary and its eventless collar separators. If those directions are supplied
internally, every screen carries a positive conductance tensor

```math
G_{AB}(u,v,y),
\qquad A,B=1,2,
```

and the no-twist theorem gives two intrinsic eventless record connections:

```math
\Omega_+
=
{1\over2}G^{-1}\partial_+G,
\qquad
\Omega_-
=
{1\over2}G^{-1}\partial_-G.
```

These are metric-compatible by construction:

```math
\partial_\pm G
=
\Omega_\pm^TG+G\Omega_\pm.
```

With the sign convention used in the finite diagnostic, the null expansions
are:

```math
\theta_\pm
=
-{\rm tr}\,\Omega_\pm
=
-\partial_\pm\log \sqrt{\det G}.
```

The traceless parts are the screen shears:

```math
\sigma_\pm
=
\Omega_\pm
-
{1\over2}{\rm tr}(\Omega_\pm)I.
```

The same sealed stack then has a mixed null holonomy:

```math
F_{+-}
=
\partial_+\Omega_-
-
\partial_-\Omega_+
+
[\Omega_+,\Omega_-],
```

and a connection Bianchi identity:

```math
D_+F_{-A}+D_-F_{A+}+D_AF_{+-}=0.
```

Finally, the local focusing readouts are determined by the same data:

```math
\mathcal T_{\pm\pm}^{\rm focus}
=
-\partial_\pm\theta_\pm
-
{1\over2}\theta_\pm^2
-
\|\sigma_\pm\|^2.
```

This is not yet the full Einstein equation. It is the finite null-diamond
kinematic theorem:

```text
sealed count-null axes + no-twist eventless transport
-> Omega_±, theta_±, sigma_±, F_+-, focusing readouts.
```

Three attacks show exactly what remains.

First, a screen tensor `G` at each screen does not by itself fix affine
normalization. Rescaling the derivative along one null direction changes
`theta_+` and `T_{++}^{focus}` while leaving the screen snapshots unchanged.
Thus a sealed diamond must supply the count/affine scale of its null fronts,
not merely the screen metric.

Second, cross-normalization alone is not enough. A balanced rescaling

```math
\Omega_+\mapsto a\Omega_+,
\qquad
\Omega_-\mapsto a^{-1}\Omega_-
```

can preserve a mixed product while moving the individual focusing sources.
The null pair must be normalized as a physical record-front pair, not only as
a product.

Third, focusing is not automatically the deletion source. One can preserve
the double-null geometry receipts and alter the deletion-response source
unless the sealed event law identifies them. Therefore the remaining gravity
identity is:

```text
deletion response = focusing source
```

as an intrinsic one-event theorem, not as a source-matching convention.

## 23. Double-null diagnostic

The finite diagnostic is:

```text
code/v6_p4h_intrinsic_null_diamond_gate.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| double-null screen packet | positive `G(u,v,x,y)` on `S_{u,v}` | two count-null directions are available | radius_span=6.932e-02/7.613e-02/7.804e-02 | PASS-SCOPED |
| null-pair connections | `Omega_+=1/2 G^-1 d_u G`, `Omega_-=1/2 G^-1 d_v G` | both metric-compatible | compat6/10/14=4.6e-16/4.6e-16/7.0e-16 | PASS |
| area/expansion identities | `d_± log sqrt(det q)=-theta_±` | finite identities converge | u=4.65e-02/2.25e-02/1.19e-02, v=2.97e-02/1.66e-02/9.85e-03 | PASS |
| expansion/shear readout | `theta_±` and `sigma_±` from no-twist connections | nonzero null deformation data | theta+=4.875e-01, sigma+=7.744e-01 | PASS |
| mixed null holonomy | `F_uv=d_u Omega_v-d_v Omega_u+[Omega_u,Omega_v]` | screen stack has null-loop curvature | max6/10/14=1.538e-01/9.228e-02/1.089e-01 | PASS |
| connection Bianchi identity | `D_u F_vx + D_v F_xu + D_x F_uv` | finite residual decreases | res6/10/14=2.581e-01/2.202e-01/1.492e-01 | PASS |
| focusing readout | `-d_±theta_±-theta_±^2/2-|sigma_±|^2` | finite focusing scalars are computable | plus/max=2.185e+00/2.876e+00/3.034e+00 | PASS-READOUT |
| null rescaling attack | externally change the `u` derivative scale | expansion and focusing move while `G` snapshots do not | theta_gap=1.706e-01, focus_gap=2.495e+00 | FAILS-G-ONLY |
| balanced rescaling attack | `Omega_+ -> a Omega_+`, `Omega_- -> a^-1 Omega_-` | mixed normalization can be hidden while focusing moves | product_gap=0.0 but T++ changes | FAILS-CROSS-NORM-ONLY |
| source matching attack | alter deletion source while preserving geometry receipts | focusing source is not deletion source unless sealed law identifies them | source_gap=6.364e-02 | FAILS-SOURCE-FREE |
| double-null verdict | sealed count-null axes + no-twist transport | null kinematics close; affine/source gates remain | not full 3+1 yet | FINITE-CLOSURE-WITH-GATES |

The decisive finite facts are:

```text
metric-compatibility residuals:
  4.644396126208125e-16
  4.644396126208125e-16
  7.024409240299214e-16

area/expansion identity residuals:
  u: 4.651323353064507e-02 -> 1.186367666552202e-02
  v: 2.967148061378422e-02 -> 9.854282573978468e-03

connection Bianchi residual:
  2.580856916594180e-01
  2.202353353363560e-01
  1.492104505963817e-01

null-rescaling attack:
  theta gap = 1.706356551112643e-01
  focusing gap = 2.495274876266057e+00

source-matching attack:
  source gap = 6.363520408163348e-02
```

Thus the double-null campaign gives a real finite theorem, but a scoped one.
The sealed diamond can derive null kinematics from intrinsic count-null axes
and no-twist transport. It cannot derive full gravity from screen snapshots
alone. The remaining branch-A gate is:

```text
intrinsic null-front normalization + deletion-response/focusing identity.
```

If those are supplied externally, this part becomes branch B. If they are
forced by the same sealed event law, this is the route from record diamonds to
tensor gravity.

## 24. Sealed null-work balance campaign

The double-null campaign left two questions:

```text
who fixes the null-front scale?
why is focusing source the deletion response?
```

The strongest intrinsic candidate is closed null-work balance. Once the
sealed diamond supplies count-null fronts and no-twist transport, define:

```math
W_+
=
\left\langle \|G\Omega_+\|_F^2\right\rangle,
\qquad
W_-
=
\left\langle \|G\Omega_-\|_F^2\right\rangle.
```

Under constant null-front rescalings

```math
\Omega_+\mapsto a\Omega_+,
\qquad
\Omega_-\mapsto b\Omega_-,
```

the works become:

```math
W_+(a)=a^2W_+,
\qquad
W_-(b)=b^2W_-.
```

The first result is negative:

```text
closed work balance alone cannot fix affine normalization.
```

Indeed:

```math
a^2W_+=b^2W_-
```

is one equation in two positive unknowns. It leaves a one-parameter family of
balanced null units.

The missing invariant is front-dual reciprocity. The two null fronts are not
two unrelated clocks; they are opposite boundary fronts of the same sealed
diamond. If their count units are reciprocal,

```math
ab=1,
```

then closed work balance has the unique positive solution:

```math
a_*=\left({W_-\over W_+}\right)^{1/4},
\qquad
b_*=\left({W_+\over W_-}\right)^{1/4}.
```

The solution is isolated in log-affine scale. If `a=e^s` and `b=e^{-s}`,

```math
B(s)
=
\left(e^{2s}W_+ - e^{-2s}W_-\right)^2
```

has:

```math
B''(s_*)>0.
```

Thus affine normalization is not fixed by work alone, but it is fixed by:

```text
front-dual reciprocity + closed null-work balance.
```

That is a real Einstein-style reduction. It replaces an arbitrary null scale
with a closed-diamond invariant, provided the reciprocal-front fact is
intrinsic to the sealed diamond rather than imposed as a coordinate
normalization.

The second result is also negative. Even after the affine pair is fixed, the
focusing readout:

```math
\rho_{\rm focus}
=
{\rm center}\left(
{1\over2}\{a_*^2\mathcal T_{++}^{\rm focus}
       +b_*^2\mathcal T_{--}^{\rm focus}\}
\right)
```

is not automatically the deletion response. One can keep the same screen
geometry, same no-twist connections, same null-work balance, same conserved
mean-zero source norm, and still alter the source shape. Therefore:

```text
closed null-work balance does not by itself prove
deletion response = focusing source.
```

The branch-A theorem target is now exact:

```text
front-dual reciprocity must be intrinsic;
deletion response must be the balanced focusing source of the same sealed
event law.
```

If either is supplied externally, the construction remains branch B at that
point. If both are forced by the sealed record process, the null normalization
and source identity gates close.

## 25. Sealed null-work diagnostic

The finite diagnostic is:

```text
code/v6_p4i_sealed_null_work_balance.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| null work readout | `W_±=<\|\|G Omega_±\|\|_F^2>` | both front work densities are intrinsic once count-null axes exist | W+=0.188058, W-=0.155733 | PASS |
| work-only attack | solve `a^2 W_+ = b^2 W_-` with free `a,b` | closed work balance is a one-parameter family | pairs=(0.75,0.82),(1.00,1.10),(1.35,1.48) | FAILS-WORK-ONLY |
| front-dual reciprocity | add the sealed-pair condition `ab=1` | work balance has one positive solution | a*=0.953943, b*=1.048281 | PROVES-AFFINE-PAIR-IF-DUALITY |
| isolation margin | second variation in log affine scale | the balanced solution is locally isolated | B''=0.937180, residual=2.8e-17 | PASS |
| cross-normalization attack | use the work-only family without `ab=1` | all rows balance work but have different cross products | res_max=2.8e-17, ab_span=1.384604 | FAILS-WITHOUT-FRONT-DUALITY |
| balanced focusing source | `rho_focus = centered(a*^2 T++ + b*^2 T--)`, normalized by `W*` | one conserved source is fixed if focusing identity is declared | mean=6.7e-18, norm=0.133068 | PASS-SCOPED |
| constant-source gauge attack | add a constant to `rho_focus` then recenter | closed source conservation kills the silent constant | gap_after_recentering=1.1e-16 | PASS |
| source-free attack | alter source shape, recenter, and preserve source norm | same geometry and same work balance do not select deletion source | mean_gap=2.6e-18, norm_gap=0.0e+00, shape_gap=0.695185 | FAILS-SOURCE-FREE |
| identity theorem option | require deletion response to be `rho_focus` | deletion/focusing residual vanishes by the same sealed law | identity_residual=0.0e+00 | BRANCH-A-IF-PROVED |
| sealed null-work verdict | closed work balance + front-dual reciprocity + focusing identity | affine pair closes; source identity remains the hard theorem | not a full tensor conservation theorem yet | PARTIAL-CLOSURE-WITH-NO-GO |

The decisive numbers are:

```text
primitive_work = 0.364784952089977
W_+ = 1.880579107965533e-01
W_- = 1.557333094499118e-01

a_* = 9.539431118313593e-01
b_* = 1.048280539580837e+00
balanced work = 1.711341018516869e-01
balance residual = 2.775557561562891e-17
B'' = 9.371801861306731e-01

work-only balanced family:
  (a,b)=(0.75,0.824169067248)
  (a,b)=(1.00,1.098892089664)
  (a,b)=(1.35,1.483504321046)

source-free conserved alternative:
  same mean and same norm,
  shape gap = 6.951848827794218e-01.
```

Thus the campaign partly closes the null-front gate and proves a no-go for a
tempting overclaim:

```text
work balance alone does not derive null normalization;
work balance plus front-dual reciprocity does derive the affine pair;
affine closure does not derive deletion/focusing equality.
```

The next theorem cannot be another scale selector. It must be the source
identity theorem:

```text
the deletion response of an isolated sealed event is exactly the balanced
focusing source of its reciprocal null fronts.
```

## 26. Deletion/focusing source-identity campaign

The source identity theorem can now be attacked directly. The current
primitive deletion response has the form:

```math
\rho_E(i)
=
W_*(E_i-\bar E),
\qquad
E_i\in\{0,1\}.
```

Therefore it is a centered two-level source:

```math
\rho_E(i)
\in
\{W_*(1-\bar E),-W_*\bar E\}.
```

The balanced double-null focusing source, however, is the screen field:

```math
\rho_{\rm focus}
=
{\rm center}\left(
{1\over2}\{a_*^2\mathcal T_{++}^{\rm focus}
       +b_*^2\mathcal T_{--}^{\rm focus}\}
\right).
```

For exact identity under the current primitive event law, this focusing source
must itself become a two-level centered deletion source. That is a strong
dynamical condition, not a consequence of null work.

The finite campaign proves the negative statement:

```text
generic balanced double-null focusing is not the primitive binary deletion
response.
```

The proof is simple. Among all binary event supports with the fixed primitive
work `W_*`, choose the best two-level deletion source in least-square error.
If the residual is nonzero, exact identity is impossible for the current
primitive deletion law. In the finite double-null screen stack, the focusing
source has hundreds of distinct values and the best binary deletion source
still has a large residual.

This also defeats the weak projection route. Thresholding the focusing field
does pick an informative event support, but an informative support is not the
source identity. One can preserve:

```text
the same event support direction;
the same mean-zero conservation;
the same source norm;
the same projection onto the binary deletion source;
```

while changing the source shape. Thus support-only deletion data do not
determine the focusing source.

The exchange-holonomy rescue also fails for the current primitive law. If one
sets:

```math
q_{\rm focus}={\rho_{\rm focus}\over W_*},
```

then `q_focus` is not the idempotent primitive event contrast:

```math
q^2=1.
```

So making the full focusing field into the primitive holonomy contrast is not
a derivation inside the old primitive law. It is an enriched deletion-germ
proposal.

The campaign leaves exactly two branch-A routes:

```text
1. focus-binary dynamics:
   the isolated sealed event dynamics forces rho_focus to be exactly two-level;

2. enriched RN deletion field:
   the primitive deletion action is the full local Radon-Nikodym field, and
   the binary event support is only a threshold/readout of that field.
```

The first route keeps the old primitive binary deletion law but imposes a very
strong geometric restriction. The second route changes the primitive object:
the event is no longer only a binary support; it is a full deletion action
whose support is a readout. Without one of these two the deletion/focusing
identity is not derived.

## 27. Deletion/focusing diagnostic

The finite diagnostic is:

```text
code/v6_p4j_deletion_focusing_identity.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| balanced focusing source | `rho_focus` from reciprocal affine null fronts | conserved and `W*`-normalized, but many-valued | N=10000, levels=295, rms=0.364785 | PASS-READOUT |
| primitive deletion form | `rho_E=W*(E-mean E)`, `E in {0,1}` | current deletion response is necessarily two-level | best_k=4000, binary_levels=2 | DEFINED |
| exact identity attempt | best two-level deletion source fitted to `rho_focus` | generic focusing source is not a primitive deletion response | rms_res=0.242377, max_res=0.555921 | FAILS-GENERIC-IDENTITY |
| weak projection route | threshold `rho_focus` into the best event support | projection is informative but not identity | corr=0.814987 | COND-NOT-IDENTITY |
| same support receipt attack | reflect `rho_focus` off its binary support direction | same norm and same event projection, different source shape | norm_gap=2.8e-17, proj_gap=7.1e-15, shape_gap=0.918189 | FAILS-SUPPORT-ONLY |
| holonomy contrast attempt | take `q=rho_focus/W*` as primitive contrast | it is not the idempotent event contrast `q^2=1` | levels=295, max\|q^2-1\|=2.889098 | FAILS-PRIMITIVE-HOLONOMY |
| defect-locked positive toy | force focusing source to be the two-level deletion source | identity then holds, but only because the dynamics was locked | toy_rms_res=6.5e-08 | PASS-TOY-NOT-DERIVED |
| source identity verdict | primitive binary deletion + generic double-null focusing | does not force deletion response = focusing source | needs focus-binary dynamics or enriched RN deletion field | FINITE-NO-GO |

The decisive numbers are:

```text
primitive_work = 0.364784952089977
front_product = 1.0
rho_focus rms = 0.364784952089977
rho_focus rounded levels = 295

best binary deletion fit:
  selected events = 4000 out of 10000
  rms residual = 2.423772380740975e-01
  max residual = 5.559208657928597e-01
  correlation = 8.149873059574702e-01

same-support reflected source:
  norm gap = 2.775557561562891e-17
  projection gap = 7.105427357601002e-15
  shape gap = 9.181888191555867e-01

holonomy contrast attempt:
  q_focus levels = 295
  max |q_focus^2 - 1| = 2.889097981753846
```

Therefore the source identity theorem is not a consequence of the current
primitive binary deletion law plus generic double-null focusing. The result is
not that branch A is impossible. It is that the branch-A theorem has changed
shape:

```text
prove focus-binary dynamics,
or promote deletion from binary support to a full local RN action.
```

The second route is more natural for the sealed-diamond ontology. It says the
real invariant is the deletion action field, while the binary event is only
the stable support/readout of that field. But that is an ontology change, not
a theorem already proved by the current primitive event law.

## 28. Enriched RN deletion-field campaign

The natural continuation is to promote the deletion action itself:

```math
A_D(i)
=
\log {dP_D\over dP_{\setminus D}}(i).
```

In the enriched route, the primitive is no longer the binary support `E`. The
primitive is the full local Radon-Nikodym action field:

```text
primitive = A_D;
source    = center(A_D);
event     = stable positive/readout support of A_D.
```

For the finite double-null packet, the strongest branch-A proposal is:

```math
A_D
=
\rho_{\rm focus}
=
{\rm center}\left(
{1\over2}\{a_*^2\mathcal T_{++}^{\rm focus}
       +b_*^2\mathcal T_{--}^{\rm focus}\}
\right).
```

Then the source identity closes:

```text
deletion response = focusing source
```

because both are readouts of the same local action field. The binary event is
not discarded. It becomes:

```math
E_D=\{A_D\ge 0\}
```

or, more carefully, the stable positive component/readout of `A_D`.

This solves the two-level obstruction from §26, but it creates two new theorem
targets.

First, support is not source. The binary support recovered from `A_D` does not
reconstruct `A_D`. Replacing the RN action by `W_*(E_D-\bar E_D)` gives a
different gravity response. Therefore the enriched theory must keep the full
action field as primitive or derive it intrinsically.

Second, the old primitive constants do not automatically survive. The
single-diamond law in §5 used an idempotent contrast:

```math
q^2=1.
```

The RN focusing contrast:

```math
q_{\rm RN}={A_D\over W_*}
```

is many-valued. Rerunning the same information-geometric balance with
`q_RN` moves the constants. This is not a small detail; it means enriched RN
deletion is a real ontology change, not a harmless reinterpretation.

The enriched route is therefore:

```text
sealed double-null geometry
-> balanced focusing field
-> local RN deletion action A_D
-> source = center(A_D)
-> event = stable positive support/readout of A_D.
```

Its new branch-A gate is:

```text
derive A_D intrinsically and derive the event constants from the A_D process.
```

If `A_D` is chosen after the focusing geometry is known, this is branch B. If
the sealed process itself generates `A_D`, the source identity obstruction is
removed.

## 29. Enriched RN diagnostic

The finite diagnostic is:

```text
code/v6_p4k_enriched_rn_deletion_field.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| enriched RN primitive | `A_D := rho_focus` from balanced double-null readout | source/focusing identity is exact for the action field | mean=-8.3e-18, rms=0.364785 | PASS-BY-PRIMITIVE |
| event support readout | `E_D={A_D>=0}` | binary support is recovered as a threshold readout | density=0.580, components=1, max=752 | PASS-READOUT |
| threshold stability | count cells near `A_D=0` | finite margin exists but near-zero cells expose refinement gate | min\|A\|=3.145e-04, near=240/1296 | COND-STABILITY |
| binary-source comparison | compare source `A_D` to `W*(E_D-mean E_D)` | binary support is not the gravitational source | rms_gap=0.247811, max_gap=0.491780 | PASS-ENRICHED |
| best binary no-go persists | fit any two-level deletion source to `A_D` | best binary law still cannot reproduce the RN action | best_rms=0.244313, best_k=864 | PASS-NO-GO |
| gravity transport receipt | solve `L phi=A_D` on a sealed ring readout | mean-zero RN source has a finite record-gravity response | res=2.1e-09, KL=0.416766 | PASS |
| binary-gravity attack | replace `A_D` by its support source | same event support gives a different response field | phi_gap=2272.066758 | FAILS-SUPPORT-SOURCE |
| primitive constant drift | rerun information balance with `q=A_D/W*` | old idempotent constants do not survive automatically | eta_RN=1.240094, W_RN=0.583518, drift=0.218733 | REOPENS-CONSTANTS |
| holonomy idempotence attack | test `q_RN^2=1` | many-valued RN contrast is not the old primitive event contrast | levels=38, max\|q^2-1\|=2.305373 | FAILS-OLD-HOLONOMY |
| support-only RN attack | preserve support and rms while changing `A_D` shape | support readout alone cannot reconstruct the RN action | flips=0, norm_gap=5.6e-17, shape_gap=0.152203 | FAILS-SUPPORT-ONLY |
| enriched RN verdict | primitive `A_D` plus threshold readout | source identity closes, but constants/action dynamics become theorem targets | not closed unless `A_D` is intrinsically derived | PARTIAL-CLOSURE |

The decisive numbers are:

```text
primitive_work = 0.364784952089977
A_D rms = 0.364784952089977
positive support = 752 / 1296
positive components = 1
near-zero cells = 240 / 1296

binary support source gap:
  rms gap = 2.478112755855089e-01
  max gap = 4.917803910020492e-01

gravity response:
  L phi = A_D residual = 2.118750841439976e-09
  transport KL = 4.167658133642611e-01
  binary-source phi gap = 2.272066758252090e+03

RN information balance:
  eta_RN = 1.240093785338001
  W_RN = 0.5835180823645488
  old W* drift = 0.2187331302745723

support-only alternative:
  support flips = 0
  norm gap = 5.6e-17
  action shape gap = 1.522027461615951e-01.
```

Thus enriched RN deletion is not a cosmetic fix. It does exactly what it is
supposed to do:

```text
it makes deletion response and focusing source the same local action field.
```

But it also proves that Paper 4 has reached a new fork:

```text
old binary primitive:
  keeps the old constants but fails generic source/focusing identity;

enriched RN primitive:
  closes source/focusing identity but reopens primitive constants and demands
  an intrinsic derivation of A_D.
```

Einstein's pressure point is therefore no longer "which source do we choose?"
It is:

```text
what invariant sealed-diamond law generates A_D?
```

## 30. A_D generation-law campaign

The next campaign attacks that pressure point directly. Assume the sealed
diamond supplies a candidate local drive `H`, read as a boundary/holonomy work
imbalance. The question is whether an invariant rule can generate the full
local action field:

```math
A_D
\neq
W_*(E_D-\bar E_D)
```

rather than merely generating its binary support.

Three routes were tested.

**Variational smoothing.** A natural least-work attempt is:

```math
A_\mu
=
{\rm normalize}\{(I+\mu L)^{-1}H\}.
```

This is covariant inside a fixed collar operator, but it leaves a smoothing
coefficient `mu`. In the finite packet, varying `mu` moves the generated
action and even changes the event support. Therefore variational smoothing
does not generate `A_D` unless `mu` is itself derived from the sealed diamond.

**Maximum entropy.** Another attempt is to ask for the least biased action
compatible with event support, zero mean, and fixed RMS work. This collapses
the action to a two-level readout. It reconstructs a binary event source, not
the many-valued RN action. Worse, a same-histogram permutation preserves
entropy data while changing the spatial gravity response. Therefore entropy
or histogram data do not determine `A_D`.

**Self-consistent record-geometry fixed point.** The only finite route that
selects a full many-valued action is a feedback equation:

```math
L\Phi(A)=A,
```

```math
T(A)
=
{\rm normalize}\{H+\alpha\Phi(A)-\beta A^3\},
```

```math
A_D=T(A_D).
```

This equation has the right shape. It is relational, because the action
sources its own record-gravity response `Phi(A)`. It is nonlinear, because
the sealed event must be stable against indefinite amplification. It is
action-level, not support-level, because the whole shape of `A` is tested by
the fixed-point equation.

In the finite packet, fixed `H`, `alpha`, and `beta` give one attracting
nonzero fixed action from all tested starts. The fixed point remains
many-valued, has a stable threshold readout, rejects the support-only source,
and rejects same-support deformations. It also produces new RN balance
constants from the generated action.

But the coefficient attack is decisive. Changing `alpha` while keeping the
same drive and the same formal law moves the fixed point and can change the
event support. Thus the campaign has not derived `A_D` unconditionally. It has
found the sharpest current candidate:

```text
A_D is the isolated fixed point of an intrinsic sealed feedback map T_D.
```

The branch-A theorem target is therefore:

```text
derive H_D, alpha_D, and beta_D from the sealed diamond,
or replace them by a coefficient-free invariant feedback equation;
prove T_D has a cofinally isolated nonzero fixed point A_D;
prove the selected A_D gives the same source, event, gravity, and constants
under refinement.
```

The negative side is equally important:

```text
variational smoothing does not select A_D;
maximum entropy does not select A_D;
support data do not select A_D;
same-histogram data do not select A_D.
```

So Einstein's question has become precise enough to falsify:

```text
if the sealed diamond cannot intrinsically supply the feedback map T_D, then
enriched RN deletion is branch B with a better physical primitive.
```

If it can, `A_D` is no longer chosen. It is the diamond's self-consistent
record action.

## 31. A_D generation diagnostic

The finite diagnostic is:

```text
code/v6_p4l_ad_generation_laws.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| sealed drive | H from boundary/holonomy work imbalance | a nonzero many-valued candidate source is available | levels=96, rms=0.364785 | INPUT-SCOPED |
| variational route | A_mu=(I+mu L)^-1 H, normalized | least-work smoothing needs a coefficient | mu_span=0.044707, support_flips=1 | FAILS-FREE-MU |
| max-entropy route | least biased source from support, mean and rms | collapses spatial action to a two-level readout | gap_to_H=0.421512, levels=2 | FAILS-SPATIAL-ACTION |
| entropy permutation attack | same histogram/entropy, different placement | spatial gravity response changes | phi_gap=116.923365 | FAILS-HISTOGRAM-ONLY |
| fixed-point route | A=T(A)=normalize(H+alpha Phi(A)-beta A^3) | with fixed coefficients, all starts converge to one action | res=2.22e-16, attractor_gap=2.22e-16 | PASS-FINITE |
| fixed action readout | event support from A_*>=0 | fixed point remains many-valued and support-readable | levels=96, drive_gap=0.056228 | PASS |
| coefficient attack | change alpha while preserving the same drive and law form | the generated action moves | alpha_gap=0.059637, support_flips=1 | FAILS-IF-COEFFICIENT-FREE |
| support-only fixed-point attack | replace A_* by its support source | support source is not a fixed point | source_gap=0.402013, map_res=0.432860 | FAILS-SUPPORT-ONLY |
| same-support action attack | preserve support and rms but change A shape | altered action fails the fixed-point equation | flips=0, shape_gap=0.154244, map_res=0.146672 | PASS-SELECTS-SHAPE |
| RN constants | rerun information balance with q=A_*/W* | new constants are derived from the generated action | eta=1.209066, W=0.504137 | PASS-NEW-CONSTANTS |
| A_D generation verdict | variational/max-ent/fixed-point comparison | only the fixed-point route selects a full action in this finite packet | still conditional on intrinsic H, alpha, beta | BEST-CANDIDATE-CONDITIONAL |

The decisive numbers are:

```text
primitive_work = 0.364784952089977

variational route:
  mu span = 4.470700520720963e-02
  support flips = 1

maximum-entropy route:
  gap to H = 4.215119760893574e-01
  entropy permutation phi gap = 1.169233648197644e+02

fixed-point route:
  fixed residual = 2.220446049250313e-16
  attractor gap = 2.220446049250313e-16
  fixed-drive gap = 5.622794881177250e-02

coefficient attack:
  alpha gap = 5.963738311297286e-02
  alpha support flips = 1

support and same-support attacks:
  support source gap = 4.020131082202093e-01
  support source map residual = 4.328604432479395e-01
  same-support shape gap = 1.542437643257740e-01
  same-support map residual = 1.466716318327285e-01

new RN balance:
  eta = 1.209066012640940
  W = 0.504136897069791
```

Thus the finite conclusion is:

```text
A_D is not generated by the obvious variational or max-entropy laws.
The strongest finite candidate is a self-consistent sealed feedback fixed
point.
That candidate is branch-A only if the sealed diamond intrinsically fixes the
drive and feedback coefficients.
```

## 32. T_D classification campaign

The previous section leaves a narrower question than before:

```text
do the current sealed-diamond invariants determine the feedback map T_D?
```

They do not. The obstruction is structural, not numerical.

Let `V_D` be the finite mean-zero record field space of a sealed ring packet
with fixed count-uniform collar operator `L`, fixed primitive work `W_*`, and
fixed sealed drive `H`. Let:

```math
N(X)
=
W_*{X-\bar X\over \operatorname{rms}(X-\bar X)}
```

be the centered work normalization, and let:

```math
L\Phi(A)=A,
\qquad
L\Phi_2(A)=\Phi(A)
```

with mean-zero gauge. Then the whole coefficient family:

```math
T_{\alpha,\beta,\delta}(A)
=
N\{H+\alpha\Phi(A)-\beta A^3+\delta\Phi_2(A)\}
```

is built from the same sealed data:

```text
H, L, W_*, ring order, source conservation, and normalization.
```

It is also equivariant under relabelings that preserve the ring order. It
does not use coordinates, an external screen, a detector convention, or a
chosen event support.

**Finite coefficient-family lemma.** For any nonzero centered drive `H` and
any centered equivariant response term `R(A)` with finite Lipschitz bound, the
maps:

```math
T_c(A)=N\{H+cR(A)\}
```

form a one-parameter family of sealed feedback laws. For sufficiently small
`|c|`, `T_c` is a contraction on a neighborhood of `N(H)`, hence has a unique
isolated attracting fixed point `A_c`. If the tangent projection of `R(N(H))`
is nonzero, then:

```math
{dA_c\over dc}\bigg|_{c=0}\ne0,
```

so the fixed action changes with `c`. All structural receipts remain true:

```text
mean-zero source;
fixed RMS work;
ring covariance;
isolated fixed point;
stable threshold readout;
same sealed drive and collar.
```

Therefore the current invariants cannot select a unique `T_D`. They select an
admissible class.

The finite diagnostic strengthens the no-go in three ways.

First, it exhibits several explicit laws in the same family with exact
attracting fixed points and different actions.

Second, it finds a pair with the same binary event support but different
`A_D`. Thus binary support cannot classify `T_D` even after the fixed-point
route is imposed.

Third, it tests the obvious selectors:

```text
minimum residual;
maximum stability / isolation;
least deformation from H;
RN information balance.
```

None selects a nondegenerate unique law. Minimum residual is useless because
every candidate is an exact fixed point. Stability gives a range. Least
deformation selects the drive-only map, whose feedback derivative is zero.
RN balance computes new constants after an action is generated; it does not
select the generating law.

The resolved Einstein verdict is:

```text
current sealed-diamond invariants do not determine T_D.
```

This is not a failure of the fixed-point idea. It is a classification result.
The branch-A route now needs one of two things:

```text
1. an additional invariant that kills the coefficient family;
2. an explicit underlying record dynamics whose Euler/fixed-point equation is
   T_D, with no free coefficients.
```

Without one of these, enriched RN deletion is a branch-B dynamics chosen from
a covariant admissible family.

## 33. T_D classification diagnostic

The finite diagnostic is:

```text
code/v6_p4m_td_classification_no_go.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| classification data | same H, L, W*, normalization and mean-zero source condition | finite sealed packet is fixed before coefficient scan | n=48, W*=0.364785 | DEFINED |
| coefficient-family lemma | T_{a,b,d}=N[H+a Phi(A)-b A^3+d Phi2(A)] | many covariant source-conserving maps are available | families=5 | NO-UNIQUENESS-CLASS |
| isolated fixed points | iterate each T from three starts | all scanned laws have one attracting fixed action | res=2.2e-16, attractor=2.2e-16 | PASS-FAMILY |
| covariance receipt | rotate and reflect the sealed drive before solving | the law is intrinsic to ring order, not coordinate labels | rot=1.0e-15, ref=3.9e-16 | PASS |
| different actions | compare fixed points across admissible coefficient choices | same sealed data generate inequivalent A_D fields | family_gap=0.087903 | REFUTES-UNIQUENESS |
| same-support pair | vary alpha while preserving event support | binary readout can be identical while A_D differs | a=0.10,b=0.06,d=0.00 vs a=0.20,b=0.06,d=0.00, gap=0.026611, flips=0 | REFUTES-SUPPORT-CLASSIFICATION |
| fixed-point residual selector | choose law with smallest residual | all exact fixed points have residual near zero | max_res=2.2e-16 | FAILS |
| stability selector | use finite linearized gain/isolation | stability is a range, not a unique invariant | max_gain=0.117808 | FAILS-RANGE |
| least-deformation selector | minimize \|\|A-H\|\| over the family | selects the degenerate drive-only map, not feedback dynamics | drive_gain=0.0e+00, best=0.000000, responseful=0.029355 | FAILS-RELATIONALITY |
| RN balance selector | rerun eta,W from each generated A_D | each action has its own balance constants | eta_span=0.025338, W_span=0.050433 | FAILS-TO-SELECT |
| T_D classification verdict | current sealed invariants plus fixed-point isolation | do not determine a unique feedback law | needs one more invariant, or explicit dynamics | FINITE-NO-GO |

The decisive numbers are:

```text
primitive_work = 0.364784952089977

family no-go:
  family gap = 8.790276921676356e-02
  max fixed-point residual = 2.220446049250313e-16
  max attractor gap = 2.220446049250313e-16

covariance:
  rotation gap = 1.047772979489991e-15
  reflection gap = 3.885780586188048e-16

same-support counterexample:
  left law  = a=0.10,b=0.06,d=0.00
  right law = a=0.20,b=0.06,d=0.00
  action gap = 2.661114146642622e-02
  support flips = 0

selector failures:
  linearized gain range includes 0.0 to 0.1178077860304783
  eta span = 2.533771493825299e-02
  W span = 5.043298713125810e-02
  drive-only feedback gain = 0.0
  best responseful deviation from H = 2.935466875892789e-02
```

Thus the finite classification campaign has a clean endpoint:

```text
T_D is not uniquely fixed by the current sealed-diamond axioms.
The missing object is not A_D anymore; it is the unique record field equation
or the invariant that selects one member of the feedback family.
```

## 34. Sealed exchange-cocycle law

The classification no-go rules out the feedback-map route as the fundamental
law. It does not rule out `A_D`. It says `A_D` should not be generated by an
adjustable self-consistency equation.

The non-shadow law is already latent in the original sealed ISP ontology. A
sealed diamond contains internal record transports. If two internally
available transports can be composed in opposite orders, the diamond supplies
two physical path laws:

```math
P_{AB},
\qquad
P_{BA}.
```

The exchange-defect action is the Radon-Nikodym cocycle:

```math
A_D
=
\log {dP_{AB}\over dP_{BA}}.
```

This is not a support readout and not a feedback ansatz. It is the log action
of the two sealed process orderings themselves. Once `P_AB` and `P_BA` are
fixed by the ISP transport law, `A_D` has no coefficients:

```text
no alpha;
no beta;
no smoothing scale;
no entropy convention;
no fitted gravity source.
```

It also has the exact identities a real action should have:

```math
{\mathbb E}_{BA}e^{A_D}=1,
\qquad
{\mathbb E}_{AB}e^{-A_D}=1,
```

```math
A_{BA}=-A_{AB},
```

and for independent sealed composition:

```math
A_{D_1\times D_2}
=
A_{D_1}+A_{D_2}.
```

If the two transports commute, then:

```math
P_{AB}=P_{BA},
\qquad
A_D=0.
```

Thus eventless exchange is zero-action exchange, while event-producing
exchange is nonzero RN holonomy.

This law changes the status of the previous no-go. The `T_D` family is a
family of surrogate field equations for an action that should instead be read
directly from the exchange cocycle. The coefficient-family no-go remains
important because it prevents replacing the cocycle by a fitted feedback map.

The law also names the remaining boundary correctly. A scalar commutator norm,
event support, or same-histogram data do not determine `A_D`. The full ordered
process laws do. Therefore the branch-A condition is:

```text
the ISP ontology must supply the sealed record transports P_AB and P_BA;
A_D is then their RN exchange cocycle.
```

If `P_AB` and `P_BA` are chosen by the analyst, this is branch B. If they are
the original ISP process data, then `A_D` is not a new primitive. It is the
log cocycle shadow of the process itself.

The resulting hierarchy is:

```text
primitive ISP process:
  sealed record transports and their ordered path laws;

exchange-defect law:
  A_D = log dP_AB/dP_BA;

event readout:
  E_D = stable positive/idempotent component of A_D when a primitive binary
        defect is present;

gravity source:
  centered/projection readout of the same A_D in the record-gravity channel.
```

This is the first law in the campaign that does not underdetermine `A_D` once
the physical process is fixed, and does not overdetermine it by forcing a
binary support when the defect is many-valued.

## 35. Exchange-cocycle diagnostic

The finite diagnostic is:

```text
code/v6_p4n_exchange_cocycle_law.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| exchange-cocycle law | A_D=log dP_AB/dP_BA from two sealed transport orderings | A_D is generated without feedback coefficients | atoms=324, rms=0.654920 | PASS-GENERATES-A |
| RN identities | E_BA exp(A)=1 and E_AB exp(-A)=1 | integral fluctuation identities are exact | fwd=1.000000000000, rev=1.000000000000 | PASS |
| antisymmetry | reverse ordering has action -A_D | orientation reversal is fixed | gap=2.2e-16 | PASS |
| eventless exchange | set the two transports equal | commuting/eventless loop has zero action | rms=0.0e+00 | PASS |
| sealed relabeling | rotate the internal record labels before composing | A_D rotates with the diamond | gap=6.7e-16 | PASS |
| composition cocycle | independent sealed product of two exchange defects | log-RN actions add exactly | gap=4.4e-16 | PASS |
| support-only attack | replace A_D by its threshold support source | binary event readout loses the action shape | gap=0.739415 | FAILS-SUPPORT-ONLY |
| same-support deformation | alter normalized action while preserving support | RN law rejects arbitrary same-support shape changes | gap=0.036006, flips=0 | PASS-SELECTS-SHAPE |
| scalar commutator attack | match commutator norm with a different transport | scalar defect size does not determine A_D | eps=0.638, norm_gap=1.37e-04, action_gap=1.354604 | FAILS-SCALAR-SUMMARY |
| transport-family boundary | change the actual sealed transport law | A_D changes because the physical process changed | support_flips=48 | BOUNDARY-NOT-SHADOW |
| law verdict | fixed record transports plus sealed RN exchange | unique A_D is derived; the remaining primitive is the ISP transport law | no T_D coefficients | BEST-NONSHADOW-LAW |

The decisive numbers are:

```text
primitive_work = 0.364784952089977

raw exchange action:
  rms = 6.549198304956111e-01
  KL(P_AB || P_BA) = 6.045269588530489e-02
  KL(P_BA || P_AB) = 5.895313583503099e-02

RN identities:
  E_BA exp(A) = 1.000000000000000
  E_AB exp(-A) = 1.000000000000000
  reverse action gap = 2.220446049250313e-16

eventless and covariance:
  eventless rms = 0.000000000000000e+00
  covariance gap = 6.661338147750939e-16

composition:
  product cocycle gap = 4.440892098500626e-16

support and scalar-summary attacks:
  support-source gap = 7.394149770440063e-01
  same-support action gap = 3.600575332648881e-02
  same-support flips = 0
  scalar commutator norm gap = 1.369730962265184e-04
  scalar-summary action gap = 1.354604454603432
```

Thus the finite verdict is:

```text
The real A_D law is the sealed RN exchange cocycle.
It resolves the T_D coefficient problem at the action level.
It does not derive the underlying transport process; that process is the ISP
law itself.
```

## 36. Sealed transport-law campaign

The exchange-cocycle law moves the last freedom upstream. It says:

```text
given P_AB and P_BA, A_D is fixed.
```

The next question is whether the sealed structural axioms determine
`P_AB` and `P_BA`. The finite answer is no.

To make the no-go hard to dismiss, the diagnostic uses a strict local class.
Each transport is generated by a nearest-neighbor reversible collar generator
on a sealed ring. The resulting finite-time heat kernels satisfy:

```text
row stochasticity;
column stochasticity;
uniform count/reference stationarity;
detailed balance with the count law;
nearest-neighbor locality of the generator;
mutual absolute continuity for RN comparison.
```

Even inside this class there is a conductance-profile family. Different
profiles give different ordered exchange actions:

```math
A_D(K_A,K_B)
=
\log {d(K_AK_B)\over d(K_BK_A)}.
```

All the structural receipts remain true, but `A_D` changes. Therefore:

```text
sealed count law + locality + detailed balance + stochasticity do not
determine the ordered transports.
```

The obvious selectors fail for good reasons.

Maximum entropy from support/locality selects the uniform local heat kernel.
That is unique, but it commutes with itself and gives:

```text
A_D=0.
```

Least exchange action also selects the eventless solution:

```text
K_A=K_B,
\qquad
A_D=0.
```

Detailed balance was already imposed and still leaves a family. Screen/Born
compatibility supplies count or norm preservation; it does not choose the
kernel. Scalar work summaries do not classify the transport either: one can
nearly match the KL work while changing the normalized action shape.

Thus the non-shadow endpoint is:

```text
A_D is derived from the ordered ISP transports;
the ordered ISP transports are not derived from the current sealed structural
axioms.
```

This is the correct place for the primitive law. A branch-A theory must take
as primitive, or derive from a still deeper principle, the whole indivisible
sealed record process:

```text
whole ISP process law
-> ordered sealed transports P_AB, P_BA
-> RN exchange cocycle A_D
-> event/source/gravity readouts.
```

If the whole process law is chosen from a family, the construction is branch
B. If the process law is fixed by the original ISP principle of indivisible
stochastic histories, then the gravity extension is no longer adding
transport coefficients; it is reading the exchange action of the same process.

## 37. Transport-law diagnostic

The finite diagnostic is:

```text
code/v6_p4o_sealed_transport_law_campaign.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| sealed transport class | nearest-neighbor reversible count-preserving generators | all constraints are satisfied before the scan | row=1.6e-15, col=1.7e-15, db=2.8e-17, gen_nonlocal=0.0e+00 | DEFINED |
| reference exchange | compose two admissible transports in opposite orders | noncommuting local transports give a nonzero RN action | comm=0.003337, W=0.003459 | PASS-NONZERO |
| transport-family no-go | scan admissible local detailed-balance transports | same sealed axioms leave inequivalent exchange actions | shape_gap=4.884997, W_span=0.008520 | REFUTES-UNIQUENESS |
| same-work attack | match KL work with another admissible transport | scalar work does not determine ordered transport | phase=5.38,amp=0.34,eps=0.113, W_gap=1.13e-04, shape_gap=5.240579 | FAILS-WORK-SUMMARY |
| support attack | replace exchange action by binary support source | event support loses transport-law information | gap=2.693686 | FAILS-SUPPORT |
| maximum entropy selector | choose uniform local kernel from support/locality alone | unique but commuting/eventless, so it kills the defect | rms(A)=0.0e+00, W=0.0e+00 | FAILS-TRIVIAL |
| least action selector | minimize exchange action over admissible pairs | selects K_A=K_B and zero exchange | rms(A)=0.0e+00, W=0.0e+00 | FAILS-TRIVIAL |
| detailed-balance selector | require reversibility with count law | already imposed and still leaves a family | comm_span=0.003648 | FAILS-FAMILY |
| Born/screen compatibility | doubly stochastic count-preserving screens | preserves total count weight but does not select a kernel | candidates=44 | FAILS-TRANSPORT-SELECTION |
| transport-law verdict | sealed axioms below the full ISP process | do not derive P_AB and P_BA | whole process law remains primitive | FINITE-NO-GO |

The decisive numbers are:

```text
reference transport:
  K_A = phase=0.10,amp=0.42,eps=0.125
  K_B = phase=1.20,amp=0.38,eps=0.120

structural constraints:
  max row error = 1.554312234475219e-15
  max column error = 1.665334536937735e-15
  max detailed-balance error = 2.775557561562891e-17
  max generator nonlocality = 0.000000000000000e+00

reference exchange:
  KL(P_AB || P_BA) = 3.459036230569232e-03
  KL(P_BA || P_AB) = 3.459036230569222e-03
  commutator norm = 3.337156730861956e-03

family no-go:
  normalized action shape gap = 4.884997296596182
  work span = 8.520015603305368e-03
  commutator span = 3.648198596450415e-03

same-work counterexample:
  alternative = phase=5.38,amp=0.34,eps=0.113
  work gap = 1.125886373370727e-04
  normalized action shape gap = 5.240578954463678
  support flips = 222

selector failures:
  support-source gap = 2.693686408199134
  maximum-entropy action rms = 0.0
  least-action rms = 0.0
```

Thus the finite campaign fully resolves the current transport question:

```text
The sealed structural axioms do not derive the ordered transport laws.
The whole indivisible ISP process law must be the primitive input, or must be
derived by a deeper theorem not yet present in Paper 4.
```

## 38. Sealed whole-history determination campaign

The transport-law no-go leaves one possible escape: perhaps the whole sealed
diamond, not merely its endpoint transports, intrinsically determines the
indivisible history law. That is the Einstein test in its cleanest finite
form.

Let:

```math
P_D^{\rm hist}
```

be the whole sealed record-history law on the history atoms of a diamond. The
ordered transports are then pushforwards:

```math
P_{AB}=(r_{AB})_*P_D^{\rm hist},
\qquad
P_{BA}=(r_{BA})_*P_D^{\rm hist},
```

and the exchange action is the RN cocycle:

```math
A_D=\log {dP_{AB}\over dP_{BA}}.
```

The theorem one would need is:

```text
Sealed whole-history determination theorem:
the intrinsic relational facts of a sealed diamond determine P_D^{hist}
uniquely up to Leibniz relabeling.
```

The finite campaign refutes this theorem for the current sealed shadows. It
uses two independent Leibniz-twin attacks.

First, pairwise shadows do not determine a whole history. For three binary
history faces, define:

```math
P^{\rm hist}_\theta(a,b,c)
=
{1\over 8}\{1+\theta\,(-1)^{a+b+c}\}.
```

For opposite values of `theta`, all one-face and two-face marginals are
identical. The whole history is not identical, because the triple parity
moment changes sign. Thus any sealed ontology that sees only local faces,
pairwise transports, endpoint screens, or pairwise conditional information has
Leibniz twins.

Second, even fixed ordered transports and fixed `A_D` do not determine the
retained history. Let `e` be an endpoint exchange atom with fixed forward and
reverse laws:

```math
p_e=P_{AB}(e),
\qquad
q_e=P_{BA}(e).
```

Lift the endpoint atom by an internal history sign `h`:

```math
P^{\rm hist}_\theta(e,h)
=
p_e\,{1+h\theta m_e\over 2},
\qquad
P^{{\rm hist,rev}}_\theta(e,h)
=
q_e\,{1+h\theta m_e\over 2},
```

where `m_e` is a fixed centered mode with `|theta m_e|<1`. The endpoint
pushforwards are independent of `theta`, and the full history RN action is:

```math
\log{P^{\rm hist}_\theta(e,h)\over P^{{\rm hist,rev}}_\theta(e,h)}
=
\log{p_e\over q_e}
=
A_D(e).
```

Thus `P_AB`, `P_BA`, and `A_D` are all exactly fixed while the whole law
`Gamma_theta` changes. This is not a decorative hidden variable: if the next
diamond's reference law depends on the retained internal sign, the same
endpoint/action diamond composes into a different future. That is precisely
the non-Markovian missing object.

The obvious selectors fail. Maximum entropy at fixed endpoint law selects the
memoryless lift `theta=0`. Least hidden memory does the same. Maximum retained
memory runs to the positivity boundary and leaves an orientation/sign family.
Refinement does not remove the ambiguity: split every history atom into equal
count twins and coarse-grain back, and the same `theta` family survives.

There is also a positive theorem, but it is not dynamical closure:

```text
If the sealed process supplies the probabilities of all history atoms, then
P_D^{hist} is determined.
```

This is a full-law theorem, not a selection theorem. It says the correct
primitive has been named:

```text
the whole indivisible sealed ISP history law.
```

It does not derive that law from lower shadows. Therefore the current
Einstein verdict is:

```text
transport/action/readout shadows do not determine the process;
the process determines transport/action/readout shadows.
```

## 39. Whole-history diagnostic

The finite diagnostic is:

```text
code/v6_p4p_whole_history_determination.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| pairwise Leibniz twins | three-bit parity family with same one/two marginals | pairwise sealed shadows do not determine whole history | pair_gap=0.0e+00, TV=0.620000, triple_gap=1.240000 | REFUTES-PAIRWISE-DETERMINATION |
| fixed ordered transports | lift same P_AB and P_BA by opposite hidden-history bias | endpoint transports stay identical while P_D^{hist} changes | P_gap=0.0e+00, Q_gap=0.0e+00, TV=0.512361 | REFUTES-ENDPOINT-DETERMINATION |
| fixed RN action | use same hidden conditional under forward and reverse laws | A_D remains exactly the endpoint exchange cocycle | gap_plus=2.2e-16, gap_minus=2.2e-16, rms(A)=0.463953 | REFUTES-ACTION-DETERMINATION |
| composition memory | let next diamond depend on retained hidden-history sign | same P_AB/P_BA/A_D can compose into different futures | memory_span=0.851845, next_gap=0.306664 | PROVES-NONMARKOVIAN-GATE |
| maximum entropy selector | maximize hidden conditional entropy at fixed endpoints | selects the memoryless lift, not the retained-history law | theta*=0.00, memory=0.0e+00, S=3.296479 | FAILS-TRIVIALIZES-MEMORY |
| least hidden-memory selector | minimize retained memory at fixed endpoints | again selects theta=0 and kills history dependence | theta*=0.00, endpoint_work=0.111110 | FAILS-TRIVIALIZES-MEMORY |
| max memory selector | maximize retained memory subject only to positivity | runs to boundary and leaves orientation/sign freedom | theta=(-0.95,0.95), span=1.190078 | FAILS-BOUNDARY-FAMILY |
| refinement persistence | split every history atom into two count twins and coarse-grain back | whole-history ambiguity survives finite refinement | coarse_gap=0.0e+00, refined_TV=0.512361 | REFUTES-REFINEMENT-ESCAPE |
| full atom theorem | include all sealed history atom probabilities as the process law | theta and P_D^{hist} are then recovered, but the law was supplied | theta_rec=(0.680000,-0.680000) | THM-CONDITIONAL-FULL-LAW |
| whole-history verdict | current sealed shadows versus P_D^{hist} | only the full indivisible process law determines future composition | transport/action shadows insufficient | FINITE-NO-GO |

The decisive numbers are:

```text
pairwise-shadow twins:
  pair shadow gap = 0.000000000000000e+00
  total variation = 6.200000000000001e-01
  triple moment left/right = 6.200000000000001e-01 / -6.200000000000001e-01

fixed endpoint/action twins:
  P endpoint gap = 0.000000000000000e+00
  Q endpoint gap = 0.000000000000000e+00
  full history total variation = 5.123607231500579e-01
  A_D lift gap plus/minus = 2.220446049250313e-16 / 2.220446049250313e-16
  endpoint work = 1.111102724637482e-01

non-Markovian composition:
  memory plus/minus = 4.259227365841414e-01 / -4.259227365841414e-01
  memory span = 8.518454731682827e-01
  future probability plus/minus = 6.533321851702909e-01 / 3.466678148297091e-01
  future gap = 3.066643703405818e-01

selector failures:
  max-entropy theta = 0.000000000000000e+00
  max-entropy memory = 0.000000000000000e+00
  max-memory theta = -9.500000000000000e-01 / 9.500000000000000e-01

refinement and full-law theorem:
  refinement coarse gap = 0.000000000000000e+00
  refinement total variation = 5.123607231500579e-01
  recovered theta plus/minus = 6.799999999999999e-01 / -6.799999999999999e-01
```

Thus the whole-history campaign gives the sharpest current boundary:

```text
Current sealed invariants:
  determine many readouts, but not P_D^{hist}.

Full atom/cylinder process law:
  determines P_D^{hist}, hence ordered transports, A_D, memory, and future
  composition.

Branch-A closure:
  requires the whole indivisible sealed ISP process law itself, or a deeper
  theorem deriving it.
```

## 40. Complete closed-holonomy whole-history law

The previous no-go does not mean "no law." It says the law cannot be a
downstream shadow. The local corpus and the Barandes-aligned ISP lesson point
to the same object:

```text
the complete closed-exchange holonomy ledger of the sealed diamond.
```

Paper 1-v1/v2 already treated primitive slab kernels, localized comparison
maps, and exchange defects as the finite objects, not a metric behind them.
Paper 3-v3 kept returning to the full-law branch. Paper 5-v5 made the same
warning in dynamical language: semigroup factorization is the divisible
special case, not the ISP primitive. The finite law therefore has to be a
whole-history law, and its invariant content must be closed exchange
holonomy.

Let `At(D)` be the finite Leibniz history atoms of a sealed diamond and let:

```math
\mu_D(\omega)={1\over |At(D)|}
```

be the count reference. Let `C_D` be the complete set of sealed
closed-history contrasts, i.e. the nonconstant cylinder contrasts generated by
closed exchange/intervention experiments inside the sealed diamond. In a
binary finite presentation these are the Walsh/Mobius contrasts:

```math
\chi_C(\omega)\in\{-1,+1\}.
```

The law is:

```math
P_D^{\rm hist}(\omega)
=
{1\over Z_D}\,
\mu_D(\omega)
\exp\!\left(
\sum_{C\in{\cal C}_D} h_C(D)\,\chi_C(\omega)
\right).
```

Equivalently:

```math
\log {dP_D^{\rm hist}\over d\mu_D}
=
\hbox{closed-holonomy cochain of }D
\quad \hbox{mod constants}.
```

The name for the principle is:

```text
Complete Closed-Holonomy Whole-History Law.
```

It has two clauses.

**Completeness.** Every possible sealed record distinction that can affect
future gluing or future composition is represented by a closed-history
contrast in `C_D`.

**No silent history.** Every future-relevant contrast absent from `C_D` has
zero coefficient and cannot affect future composition.

This is the exact strengthening that the whole-history no-go demanded. A
hidden parity or retained sign is not allowed to sit outside the ontology and
then change the next diamond. If it changes the next diamond, it is a closed
history contrast and belongs to the holonomy ledger. If it is not in the
ledger, it is physically silent and must have zero coefficient.

The finite uniqueness theorem is elementary but decisive. For any strictly
positive law `P_D^{hist}`, the nonconstant coefficients:

```math
h_C(D)
=
{\mathbb E}_{\mu_D}
\left[
\log {dP_D^{\rm hist}\over d\mu_D}\,\chi_C
\right]
```

recover `P_D^{hist}` by the exponential formula above. This is not the hard
dynamical theorem by itself. Given a complete separating contrast ledger, it
is finite RN/Mobius identifiability. The hard physical claim is that the
sealed diamond intrinsically supplies the complete ledger of all
future-relevant closed-history contrasts.

The relation to maximum caliber is precise: if only some constraints are
known, maximum caliber selects the least-structured law compatible with those
constraints. That is inference. The present branch-A law is stronger:

```text
the physical closed-holonomy ledger is complete, so the law is not inferred
from incomplete statistics; it is reconstructed from the full intrinsic
cochain.
```

This also explains why the earlier selectors failed. Pairwise transport,
scalar work, endpoint RN action, and support are incomplete ledgers. They
throw away high-order closed-history coefficients. The complete ledger has
exactly the right number of finite degrees of freedom:

```math
|{\cal C}_D|=|At(D)|-1,
```

matching the dimension of the positive probability simplex modulo
normalization. Thus it neither underdetermines nor overdetermines a positive
finite history law.

The resulting hierarchy is now:

```text
sealed possible-change algebra
-> complete closed-holonomy cochain h_D
-> whole history law P_D^{hist}
-> ordered transports P_AB, P_BA
-> exchange action A_D = log dP_AB/dP_BA
-> event/source/gravity/Born readouts.
```

This is the finite law of possible whole histories. The cofinal/continuum
version is not a new selector; it is the same law with projective
compatibility:

```text
refining a diamond pushes the complete holonomy cochain and `P_D^{hist}` law to the
coarser diamond.
```

In standard probability language, a compatible projective family of such
finite cylinder laws determines the process. In ISP language, that projective
family is the indivisible stochastic process; it is not required to factor
through intermediate Markov kernels.

## 41. Closed-holonomy history-law diagnostic

The finite diagnostic is:

```text
code/v6_p4q_closed_holonomy_history_law.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| complete closed-holonomy ledger | Walsh/Mobius expansion of log(dP_hist/dmu) | full nonconstant ledger reconstructs P_D^{hist} exactly | gap=0.0e+00, coeffs=7 | FINITE-IDENTIFIABILITY |
| pairwise ledger attack | drop the triple closed-history coefficient | same one/two shadows lose the whole-history law | TV=0.310000, triple=0.725005 | REFUTES-PAIRWISE-LAW |
| Leibniz twin separation | compare theta and -theta parity diamonds | pair coefficients agree but complete holonomy distinguishes them | pair_gap=0.0e+00, full_gap=1.450010 | PASS-SEPARATES-TWINS |
| non-divisible history | triple closed-holonomy coefficient | finite law has nonzero conditional memory without Markov factorization | CMI=0.206924 | PASS-NONMARKOV |
| endpoint/action shadow attack | compare laws with same endpoint coefficient ledger | hidden closed-holonomy coefficients carry future-relevant memory | end_coeff_gap=0.0e+00, hidden_gap=0.699935, future_gap=0.011243 | PASS-CLOSES-HIDDEN-MEMORY |
| hidden-history reconstruction | include endpoint-hidden closed holonomies | retained history law is reconstructed exactly | gap=2.8e-17, memory_gap=0.036267 | PROVES-HIDDEN-LAW |
| sealed gluing | independent product of two sealed histories | log-RN coefficients add and mixed coefficients vanish | coeff_gap=5.6e-17, mixed=4.4e-17, recon=6.9e-18 | PASS-GLUING |
| Leibniz relabeling | permute record atoms and transform coefficients | reconstructed law covaries exactly | gap=0.0e+00 | PASS-COVARIANCE |
| neutral refinement | split every atom by an independent count twin | coarse law is exact and new silent coefficients vanish | coarse=0.0e+00, twin_coeff=0.0e+00 | PASS-PROJECTIVE-NEUTRAL |
| no-silent-history law | future-relevant contrasts must appear in the closed-holonomy ledger | otherwise the previous P_D^{hist} twins survive | complete ledger or family | LAW-FOUND-FINITE |

The decisive numbers are:

```text
complete reconstruction:
  gap = 0.000000000000000e+00
  simplex dimension = 7
  nonconstant coefficients = 7

pairwise failure:
  pairwise truncation total variation = 3.100000000000000e-01
  triple coefficient = 7.250050877529992e-01
  pair coefficient gap for theta/sign twins = 0.000000000000000e+00
  complete coefficient gap for theta/sign twins = 1.450010175505998e+00

non-Markovian memory:
  conditional mutual information = 2.069242158981531e-01

endpoint/action shadow attack:
  endpoint marginal gap = 0.000000000000000e+00
  endpoint coefficient gap = 0.000000000000000e+00
  hidden closed-holonomy coefficient gap = 6.999349148152647e-01
  hidden memory gap = 3.626713035640329e-02
  future gap = 1.124281041048502e-02
  hidden reconstruction gap = 2.775557561562891e-17

gluing/covariance/refinement:
  product coefficient gap = 5.551115123125783e-17
  product mixed coefficient max = 4.358492733391728e-17
  product reconstruction gap = 6.938893903907228e-18
  relabel reconstruction gap = 0.000000000000000e+00
  refinement coarse gap = 0.000000000000000e+00
  refinement twin coefficient max = 0.000000000000000e+00
```

Thus the law closes exactly the no-go surface opened in §38:

```text
If a hidden history can affect future composition, it appears as a
closed-holonomy coefficient.

If it does not appear in the complete closed-holonomy ledger, it cannot affect
future composition.

Given the complete ledger, `P_D^{hist}` is unique.
```

That is the law of possible whole histories in finite sealed form.

## 42. Closed-holonomy field-equation campaign

The complete closed-holonomy law gives the finite state variable. The next
question is whether invariant principles determine the values of the cochain:

```math
h_D=\{h_C(D)\}_{C\in{\cal C}_D}.
```

Here the target has to be corrected. A field equation should not choose one
universal `h_D` for every possible diamond. That would make the theory either
vacuum-like or one-state. A physical field equation should instead specify:

```text
which h_D histories are allowed;
how they glue;
how they refine;
how boundary/source data propagate;
which coefficients are physical state data rather than model parameters.
```

The finite campaign tests the obvious invariant equations.

**Bianchi/closure.** Closed holonomy has no boundary. On a finite closed
cycle, this is exact for every period:

```math
d h=0.
```

But every period value satisfies the same closure equation. Closure is
consistency, not dynamics.

**Gluing.** Independent sealed composition adds closed holonomy:

```math
h_{D_1\sqcup D_2}=h_{D_1}\oplus h_{D_2},
```

and periods add. This is exact and essential, but it does not select the
periods.

**Neutral refinement.** Splitting an atom or edge into count twins preserves
the coarse cochain and introduces no silent coefficient. Again, this is
projective consistency, not amplitude selection.

**Positivity.** The exponential RN form:

```math
P_D^{\rm hist}=Z_D^{-1}\mu_D e^{\langle h_D,\chi\rangle}
```

is positive on an open family of `h_D`. Positivity does not isolate one
cochain.

**Maximum entropy / least action without source.** With no boundary period or
source, both selectors choose:

```math
h_D=0.
```

That is the eventless/vacuum solution. It is a valid solution, but not the
nontrivial process law.

The useful field-equation form is Hodge/Poisson-like. Given physical
boundary periods or source cochains, the least-work equation selects a unique
representative:

```math
h_D
=
\arg\min \|h\|_{G_D}^2
\quad
\hbox{subject to fixed closed periods and source constraints}.
```

Equivalently, in a linear finite packet:

```math
L_D\phi_D=\rho_D,
\qquad
h_D=\nabla_D\phi_D
\quad
\hbox{or its cochain analogue}.
```

For fixed `rho_D` or fixed periods this is a proper field equation. But the
periods and sources are not selected by Bianchi, gluing, refinement,
positivity, or no-silent-history. They are the physical state data carried by
the sealed whole-history process and by neighboring/glued diamonds.

This is not a defeat. It is the normal shape of a field theory. Einstein's
equation does not choose the one metric of the universe without matter and
boundary data. Here the analogous statement is:

```text
closed-holonomy dynamics is not a selector of one universal h_D;
it is a projective boundary/source problem for the complete h_D state.
```

The branch-A distinction is therefore:

```text
allowed:
  h_D values are physical state/boundary data of the sealed process;

not allowed:
  new numerical couplings, smoothing scales, or transport coefficients are
  chosen by the analyst after the readouts are known.
```

Thus the campaign closes the overstrong target and leaves the correct one:

```text
derive the projective source/boundary evolution law for h_D across glued
diamonds.
```

The finite work already fixes the form of the local equation. What remains is
not "which variable is gravity?" but "what source/boundary cochain does the
whole ISP process carry from one sealed diamond to the next?"

## 43. Closed-holonomy field-equation diagnostic

The finite diagnostic is:

```text
code/v6_p4r_closed_holonomy_field_equation.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| Bianchi/closure | closed one-cycle holonomy has no boundary | closure is exact for a continuum of periods | res=(0.0e+00,0.0e+00), period_span=0.750000 | FAILS-UNIQUENESS |
| sealed gluing | compose independent closed cycles | periods add exactly but amplitudes remain state data | glue_err=1.4e-17, shape_gap=0.062500 | PASS-CONSISTENCY-NOT-SELECTION |
| neutral refinement | split each cycle edge into two equal count edges | period and coarse cochain are preserved | period_gap=0.0e+00, coarse_gap=0.0e+00 | PASS-PROJECTIVE-NOT-SELECTION |
| positivity | build finite Gibbs laws from two holonomy periods | positivity holds on an open family | min_p=0.099750, KL_span=0.310920 | FAILS-UNIQUENESS |
| maximum entropy | maximize entropy with no boundary/source constraint | selects the eventless vacuum cochain | h*=0.0, S=0.693147 | FAILS-TRIVIAL |
| least action | minimize \|\|h\|\|^2 with no boundary/source constraint | selects h=0 and kills nontrivial holonomy | h*=0.0, memory=0.0e+00 | FAILS-TRIVIAL |
| Hodge/least-work equation | minimize \|\|h\|\|^2 at fixed closed period | unique for each period, but the period is free state/boundary data | res=(0.0e+00,0.0e+00), family_gap=0.062500 | COND-FIELD-EQUATION |
| Poisson/source equation | solve L phi=rho with mean-zero gauge | unique response for each source, but source amplitude remains state data | res=(3.3e-16,2.3e-15), response_gap=1.222838 | COND-SOURCE-EQUATION |
| no-silent-history | let future composition depend on the closed period | the period must be in h_D, but its value is not selected by silence | future_gap=0.163643 | PASS-COMPLETENESS-NOT-DYNAMICS |
| field-equation verdict | structural principles versus h_D dynamics | they define the finite state space and boundary/source equations, not one universal h_D | state variable fixed; dynamics requires boundary/source law | FINITE-NO-GO-TO-UNIQUE-STATE |

The decisive numbers are:

```text
Bianchi/closure family:
  period small/large = 3.500000000000000e-01 / 1.100000000000000e+00
  closure residuals = 0.000000000000000e+00 / 0.000000000000000e+00
  period span = 7.500000000000001e-01

gluing/refinement:
  gluing error = 1.387778780781446e-17
  refinement period gap = 0.000000000000000e+00
  refinement coarse gap = 0.000000000000000e+00

positivity and vacuum selectors:
  minimum probability in tested family = 9.975048911968513e-02
  KL span = 3.109202125357384e-01
  max-entropy coefficient = 0.000000000000000e+00
  least-action coefficient = 0.000000000000000e+00

conditional field equations:
  Hodge residuals = 0.000000000000000e+00 / 0.000000000000000e+00
  Hodge family gap = 6.250000000000001e-02
  Poisson residuals = 3.330669073875470e-16 / 2.331468351712829e-15
  source response gap = 1.222837641564715e+00

composition:
  future probabilities = 5.866175789173301e-01 / 7.502601055951177e-01
  future gap = 1.636425266777876e-01
```

So the finite field-equation verdict is:

```text
The complete h_D cochain is the right state variable.
Bianchi, gluing, refinement, positivity, and no-silent-history are exact
consistency laws.
Hodge/Poisson equations give unique responses once source/boundary cochains
are fixed.
No tested invariant selects one nonzero h_D without physical source/boundary
data.
```

## 44. Sealed source-gluing campaign

The field-equation campaign left source/boundary cochains as physical state
data. The next branch-A question is whether those data are local knobs, or
whether they are induced by neighboring sealed diamonds.

The finite source-gluing law is:

```math
\rho_D
=
\delta^\dagger h_{\partial D}.
```

In words:

```text
the local source of a diamond is the boundary coboundary / divergence of the
global closed-holonomy cochain on the interfaces through which it is glued to
neighboring diamonds.
```

For a chain of sealed diamonds with oriented interface cochains:

```math
h_0,h_1,\ldots,h_N,
```

the local source in diamond `i` is:

```math
\rho_i=h_{i+1}-h_i.
```

This has the exact gluing property:

```math
\sum_{i=a}^{b-1}\rho_i
=
h_b-h_a.
```

So sources on artificial internal seams cancel. A source appears only as a
boundary mismatch of the global `h` cochain.

This resolves the worry from §42 in the correct direction. The local source
is not an external coefficient attached to a diamond after the fact. It is the
failure of closed-holonomy continuation across the diamond's sealed boundary.
Given the complete global interface cochain, every local source is fixed.

There are two important caveats.

First, external boundary totals alone do not determine local sources. Holding
`h_0` and `h_N` fixed while changing internal interfaces gives the same total
source but different local source distribution. Therefore a boundary summary
is not enough:

```text
external boundary mismatch is a shadow;
complete interface h is the state data.
```

Second, a zero-sum local source adjustment that preserves the total external
mismatch is still not the same physical process. It changes the internal
closed-holonomy cochain. Thus local source choices are not free knobs; they
are either induced by a different global `h`, or they violate gluing.

Once the induced `rho` is known, the Hodge/Poisson response is unique:

```math
L_D\phi_D=\rho_D.
```

Thus the branch-A source chain is:

```text
global complete closed-holonomy cochain
-> interface mismatch / coboundary
-> local source rho_D
-> unique Hodge/Poisson response
-> gravity readout.
```

This makes the source internal, but not boundary-summary reducible. The
physical free data are global closed-holonomy cochains of the whole sealed
process, not independent local source amplitudes.

## 45. Source-gluing diagnostic

The finite diagnostic is:

```text
code/v6_p4s_source_gluing_law.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| source as coboundary | rho_i=h_{i+1}-h_i from global interface cochain | complete glued h fixes every local source | rho_norm=1.207891 | PASS-INTERNAL-SOURCE |
| internal cancellation | shared interface contributes with opposite signs | no source is created by an artificial cut | cancel=0.0e+00 | PASS-SEAM-CANCELS |
| composite conservation | sum local sources over any glued block | composite source equals external boundary mismatch | err=5.6e-17, total=0.760000, ext=0.760000 | PASS-BOUNDARY-ONLY |
| same-boundary twin | hold external h fixed and change internal interfaces | external boundary summaries do not determine local sources | ext_gap=0.0e+00, local_gap=1.390000, total_gap=2.2e-16 | REFUTES-BOUNDARY-ONLY |
| complete h uniqueness | recover h from left boundary plus induced rho | same complete cochain gives same source assignment | gap=1.1e-16 | PROVES-UNIQUE-GIVEN-H |
| free local source attack | alter local rho after h is fixed | either right boundary or the global cochain changes | right_gap=0.050000, h_gap=0.200000 | FAILS-AS-EXTERNAL-KNOB |
| zero-sum local source attack | preserve external mismatch but alter internal rho | still changes the internal closed-holonomy cochain | ext_gap=0.0e+00, h_gap=0.180000 | FAILS-SAME-PROCESS |
| Poisson response | solve response equation using induced rho | response is unique once source is glued from h | res=0.0e+00, twin_response_gap=0.480000 | PASS-CONDITIONAL-RESPONSE |
| source-gluing verdict | source data from complete global h versus local knobs | sources are internal boundary mismatches, not independent parameters | complete h required | FINITE-CLOSURE-WITH-GLOBAL-H |

The decisive numbers are:

```text
global interface cochain:
  h = 0.150000, 0.720000, -0.080000, 0.460000, 0.910000
  rho = 0.570000, -0.800000, 0.540000, 0.450000

source conservation:
  internal cancel max = 0.000000000000000e+00
  composite error = 5.551115123125783e-17
  total source = 7.600000000000000e-01
  external mismatch = 7.600000000000000e-01

same-boundary twin:
  external gap = 0.000000000000000e+00
  local source gap = 1.390000000000000e+00
  total source gap = 2.220446049250313e-16

complete h / source attacks:
  recovery gap = 1.110223024625157e-16
  free right-boundary gap = 5.000000000000016e-02
  free h gap = 2.000000000000001e-01
  zero-sum adjusted external gap = 0.000000000000000e+00
  zero-sum adjusted h gap = 1.800000000000000e-01

response:
  Poisson residual = 0.000000000000000e+00
  twin response gap = 4.800000000000000e-01
```

The finite source-gluing verdict is:

```text
rho_D is internal once the complete global interface h cochain is known.
Artificial seams cancel.
Composite sources are boundary mismatches.
External boundary summaries do not determine local sources.
Local source knobs either change the global h process or violate gluing.
```

## 46. Cellular source-conservation campaign

The source-gluing law in §44 is a chain model. The tensor question requires a
cellular version. Replace a chain of sealed diamonds by a finite sealed cell
complex. Each oriented interface carries a vector-valued closed-holonomy
cochain:

```math
h_e^\nu,
```

where the component index `nu` labels the source/readout channel. For each
cell/diamond `D`, define:

```math
\rho_D^\nu
=
\sum_{e\subset \partial D}
\epsilon(D,e)\,h_e^\nu.
```

This is the finite cellular form of:

```math
\rho^\nu=\nabla_\mu T^{\mu\nu}.
```

It is not imposed as a separate conservation axiom. It follows from oriented
gluing. Every internal interface appears twice with opposite signs, so no
tensor source can be created by an artificial cellular cut. For every glued
subcomplex `K`:

```math
\sum_{D\subset K}\rho_D^\nu
=
\sum_{e\subset\partial K}\epsilon(K,e)h_e^\nu.
```

Thus the source of a composite is its external boundary flux, component by
component. In a closed complex the total source vanishes exactly.

Scalar sources are now readouts, not separate laws. For any fixed scalar
projection vector `w_nu`:

```math
\rho_D^{(w)}
=
w_\nu\rho_D^\nu.
```

The scalar conservation law follows immediately from the vector/tensor
source law. This is the finite answer to the question "does source gluing
give only a scalar conservation law?" It gives the componentwise cellular
conservation law; scalar receipts are projections.

The same caveat remains in the right place. Holding all external boundary
interfaces fixed while changing internal interfaces gives the same total
boundary source but different local source distribution. Therefore the
complete interface cochain is still required. Boundary summaries are shadows.

The cellular refinement test also passes. Splitting each diamond into count
subdiamonds preserves the coarse source and introduces no silent source.
Thus source conservation is invariant under finite neutral refinement.

The finite theorem target is:

```text
For every sealed finite cell complex with complete interface holonomy cochain
h, the induced source rho=delta^dagger h is componentwise conserved under
gluing; arbitrary local source choices are invalid unless they are induced by
a different global h.
```

This is the branch-A source-conservation statement. It does not say the
continuum tensor equation is already proved; it says the finite conservation
identity has the correct cellular origin.

## 47. Cellular source-conservation diagnostic

The finite diagnostic is:

```text
code/v6_p4t_cellular_source_conservation.py
```

Its audit is:

| target | test | result | value | verdict |
|---|---|---|---:|---|
| cellular tensor source | rho_D^nu = discrete divergence of vector interface h^{mu nu} | all source components are induced by one global interface cochain | norm=0.925745 | PASS-INTERNAL-TENSOR-SOURCE |
| internal seam cancellation | each shared interface enters adjacent cells with opposite signs | no tensor source is created by a cellular cut | cancel=0.0e+00 | PASS-SEAM-CANCELS |
| cellular divergence theorem | sum sources over every rectangular glued subcomplex | local source sum equals external boundary flux | block_err=2.2e-16, total_gap=2.2e-16 | PASS-CONSERVATION |
| same-boundary cellular twin | fix every external boundary interface and change internal h | boundary data alone do not determine local tensor sources | boundary_gap=0.0e+00, local_gap=1.154883, total_gap=0.0e+00 | REFUTES-BOUNDARY-ONLY |
| scalar projection | project vector source with an arbitrary readout weight | scalar source is a projection of the same conserved tensor source | proj_gap=0.0e+00, block_gap=1.1e-16 | PASS-SCALAR-AS-PROJECTION |
| neutral cellular refinement | split each diamond into four count subdiamonds | coarse sources and conservation are preserved | source_gap=5.6e-17, refined_block_err=4.4e-16 | PASS-REFINEMENT |
| free local tensor-source attack | add local source knobs after h is fixed | global boundary conservation is generically violated | boundary_gap=0.130000 | FAILS-AS-KNOB |
| zero-total tensor-source attack | adjust local sources with total boundary preserved | still changes local source field and is not the same h-process | total_gap=0.0e+00, local_gap=0.088333 | FAILS-SAME-PROCESS |
| cellular source verdict | complete interface h versus tensor source conservation | full source conservation is a cellular gluing identity, not an added axiom | complete h required | FINITE-CELLULAR-CLOSURE |

The decisive numbers are:

```text
cellular complex:
  width = 3
  height = 2
  source norm = 9.257453891259203e-01

conservation:
  seam cancel = 0.000000000000000e+00
  block conservation error = 2.220446049250313e-16
  total source = -1.061646052123611e+00, -1.276181199504001e+00
  boundary total = -1.061646052123611e+00, -1.276181199504001e+00
  total gap = 2.220446049250313e-16

same-boundary twin:
  external boundary gap = 0.000000000000000e+00
  local source gap = 1.154883244933415e+00
  total source gap = 0.000000000000000e+00

scalar and refinement:
  scalar projection gap = 0.000000000000000e+00
  scalar block gap = 1.110223024625157e-16
  refinement source gap = 5.551115123125783e-17
  refined block error = 4.440892098500626e-16

source-knob attacks:
  free knob boundary gap = 1.299999999999999e-01
  zero-total knob gap = 0.000000000000000e+00
  zero-total local gap = 8.833333333333336e-02
```

The finite cellular verdict is:

```text
full source conservation is a cellular gluing identity of the complete
interface h cochain;
scalar sources are projections of the same tensor/vector source;
boundary summaries and local source knobs do not define the physical process.
```

## 48. Cofinal continuum reconstruction campaign

The finite cellular law is not yet a continuum theory. It proves that source
conservation is exact on each sealed cell complex, but a continuum limit needs
more than one successful finite complex. It needs a cofinal family:

```math
(\mathcal C_n,h_n,\Gamma_n,L_n,\rho_n)_{n\in I}
```

with refinement maps between sealed cell complexes. Here `h_n` is the complete
interface holonomy cochain, `Gamma_n` is the whole-history law, `L_n` is the
allowed-change operator, and:

```math
\rho_n=\delta h_n
```

is the cellular source. The cofinal theorem target is:

```text
complete h_n cochains converge projectively;
rho_n = delta h_n converges as a source density;
L_n converges as the allowed-change operator;
Gamma_n is projective as a whole-history law;
no zero-coarse refinement may carry finite hidden source.
```

This is the refinement version of the same lesson that appeared in the finite
source-gluing attacks. Boundary summaries are not enough. A coarse cell
complex can have the same external boundary flux while hiding different
internal sources. Likewise, a coarse refinement shadow can be zero while a
fine-grid oscillatory holonomy carries local source density. Therefore the
continuum object is not a single coarse `h_D`; it is the complete cofinal
record:

```math
\{h_n,\Gamma_n,L_n\}_{n\in I}
```

modulo projective equivalence and bounded-energy/no-silent-refinement
tightness.

The positive controlled theorem is straightforward but important. Suppose
`h_n` is obtained by integrating a smooth vector/tensor record flux over cell
interfaces, `L_n` is the consistent conductance/Laplace operator on the same
cell complex, and `Gamma_n` is refined by splitting records without erasing
the retained whole-history variable. Then:

```text
coarsen(h_{2n}) = h_n + quadrature error;
coarsen(delta h_{2n}) = delta h_n + quadrature error;
delta h_n / cell volume -> div h;
L_n -> L_continuum on smooth tests;
pushforward(Gamma_{2n}) = Gamma_n;
non-Markovianity is not forced to disappear.
```

The proof is just finite calculus. Interface fluxes add under gluing, cellular
divergence commutes with coarsening up to the quadrature error of the chosen
interface rule, and the standard centered graph Laplacian has second-order
convergence on smooth tests. The whole-history law is different: it is not
made Markovian by refinement. If a parity-like retained history variable is
split into a neutral subrecord and then marginalized, the coarse whole-history
law is exactly recovered.

The negative theorem is equally important.

**Theorem: coarse shadows do not determine the continuum source.** There are
fine interface cochains `eta_{2n}` such that:

```math
\pi_{2n\to n}\eta_{2n}=0,
\qquad
\delta\eta_{2n}\ne 0.
```

Thus two cofinal candidates can have the same coarse shadow and different fine
source densities. The construction is an alternating interface holonomy whose
pair-sums vanish on every coarse interface, while adjacent fine cells see
different inflow and outflow. Hence:

```text
same coarse h does not imply same continuum source.
```

This does not refute the sealed-record program. It refutes a weaker idea: that
finite coarse records alone define the continuum. Branch A needs a cofinal
law with a tightness condition. In physical language:

```text
no finite hidden source may appear only because the observer refined the cell
complex.
```

Equivalently, admissible zero-coarse refinements must have vanishing source
in the continuum norm, or must be part of the complete retained `h_n` process
rather than an unrecorded oscillation.

So the continuum gate is:

```text
projective complete h + projective Gamma + convergent L + no-silent-refinement
tightness.
```

If these are derived from the whole sealed ISP process law, continuum geometry
is a branch-A reconstruction. If tightness or projectivity is supplied as an
external smoothing convention, the continuum step is branch B.

## 49. Cofinal continuum diagnostic

The diagnostic script is:

```text
code/v6_p4u_cofinal_continuum_reconstruction.py
```

It tests a controlled smooth flux family, an operator-convergence check, a
projective non-Markovian whole-history law, and a zero-coarse high-frequency
refinement attack.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| projective flux compatibility | coarsen integrated fine interface h to coarse grid | smooth flux family is cofinally compatible up to quadrature error | flux_gap=7.492e-05 | PASS-CONTROLLED |
| projective source compatibility | coarsen fine cellular divergences | source integrals coarsen to coarse source integrals | rho_gap=4.874e-05 | PASS-CONTROLLED |
| source-density convergence | compare cellular divergence density to continuum div F | smooth h gives convergent source density | err16/32/64=2.459e-02/6.157e-03/1.540e-03 | PASS-CONTINUUM |
| operator convergence | finite Laplacian on smooth scalar test field | L_n converges to continuum Laplace operator | err16/32/64=7.078e-02/1.665e-02/4.033e-03 | PASS-CONTINUUM |
| convergence rates | error ratios under dyadic refinement | rates are stable and near second-order for smooth tests | div=3.99/4.00, lap=4.25/4.13 | PASS-RATE |
| non-Markovian projective history | neutral refinement of parity whole-history law | coarse whole-history law is preserved; Markov factorization is not forced | TV=0.0e+00 | PASS-INDIVISIBLE |
| refinement-twin attack | add zero-coarse high-frequency interface holonomy | same coarse h can hide nonzero fine source density | coarse_gap=0.0e+00, density_max=4.096e+00 | REFUTES-COARSE-ONLY |
| energy/tightness gate | scale zero-coarse oscillation with refinement | bounded-energy/no-silent-refinement condition suppresses hidden fine source | density_max=1.953e-03, energy=9.604e-10 | COND-COFINAL-GATE |
| cofinal verdict | controlled projective h versus arbitrary refinements | continuum reconstruction works with projective tightness; fails from coarse shadows alone | bounded complete h required | FINITE-COFINAL-THEOREM-TARGET |

The decisive numbers are:

```text
projective_flux_gap = 7.492147420126716e-05
projective_source_gap = 4.874105173882648e-05

source-density convergence:
  div_error_16 = 2.459315955239664e-02
  div_error_32 = 6.157185672963430e-03
  div_error_64 = 1.539852883468156e-03
  ratios = 3.994220876006172, 3.998554497684102

operator convergence:
  lap_error_16 = 7.078430539497059e-02
  lap_error_32 = 1.664826466952986e-02
  lap_error_64 = 4.033414843590012e-03
  ratios = 4.251752768234283, 4.127585511316207

whole-history refinement:
  parity_refinement_tv = 0.000000000000000e+00

zero-coarse attack:
  osc_coarse_gap = 0.000000000000000e+00
  osc_density_max = 4.096000000000000e+00
  osc_energy = 4.223999999999999e-03

tightness gate:
  bounded_density_max = 1.953125000000000e-03
  bounded_energy = 9.604264050722122e-10
```

The finite verdict is:

```text
controlled projective complete-h families reconstruct continuum source and
operator data;
whole-history non-Markovianity can survive refinement exactly;
coarse shadows alone fail because zero-coarse fine holonomy can hide source;
therefore the continuum theorem needs projective tightness/no-silent-refinement
as part of the actual sealed process law.
```

## 50. Intrinsic admissible-refinement campaign

The preceding section left one word underived: **admissible**. A coarse shadow
alone is not enough, because zero-coarse fine holonomy can hide source. But
admissibility cannot be an external smoothness convention either. It has to be
read from the sealed record data.

Let a finite refinement be a sealed quotient:

```math
\pi:\Omega_f\to\Omega_c
```

from fine history atoms to coarse history atoms. The first intrinsic
requirement is count-reference naturality:

```math
\pi_*\mu_f=\mu_c.
```

Thus a neutral refinement is not an arbitrary subdivision; it is a
count-preserving split of record alternatives. Unequal fiber counts are not
silent unless the coarse count reference changes accordingly, in which case
the coarse diamond has changed.

Let:

```math
P_f=P_f^{\rm hist},
\qquad
P_c=\pi_*P_f,
```

and define the RN actions:

```math
A_f=\log {dP_f\over d\mu_f},
\qquad
A_c=\log {dP_c\over d\mu_c}.
```

The vertical refinement action is:

```math
V_\pi=A_f-\pi^*A_c.
```

This object is intrinsic. It uses only the fine law, the coarse pushforward,
and the count references. It is exactly the part of the fine history law that
the coarse diamond cannot see.

The KL chain rule gives the first admissibility theorem:

```math
D(P_f\Vert\mu_f)-D(P_c\Vert\mu_c)
=
\mathbb E_{P_c}
\left[
D\!\left(P_f(\cdot\mid c)\Vert\mu_f(\cdot\mid c)\right)
\right]
\ge 0.
```

Equality holds exactly when the fine conditional law is count-uniform inside
each coarse fiber. Equivalently, `V_pi` is fiberwise constant and no hidden
RN work remains. This is the probability side of no-silent-refinement:

```text
a refinement is silently eventless only when it adds no conditional RN work.
```

But the cofinal source attack shows that RN/L2 amplitude is not enough. An
oscillatory fine interface cochain can have vanishing coarse shadow and small
amplitude while its cellular divergence remains finite. Therefore the
admissibility test must include every future-relevant readout map supplied by
the sealed ontology.

For the cellular source readout, write:

```math
h_f=\pi^*h_c+v_\pi,
\qquad
\pi_*v_\pi=0.
```

By naturality of the cellular coboundary:

```math
\delta h_f-\pi^*\delta h_c=\delta v_\pi.
```

So a zero-coarse vertical holonomy is silently admissible only if its source
readout also vanishes:

```math
\|\delta v_\pi\|_{\rm source}\to 0
```

cofinally. If `delta v_pi` is nonzero at finite scale, then the refinement has
discovered a physical fine source. It is admissible only as a retained
fine-level closed-holonomy contrast, not as a silent split of the old coarse
diamond.

The general finite law is:

```text
Intrinsic admissible refinement =
  count-preserving sealed quotient
  + projective whole-history pushforward
  + vertical RN chain defect either retained or zero
  + vertical source/response defects either retained or cofinally zero.
```

Equivalently:

```text
silent refinement = equality in all intrinsic future-relevant readouts.
physical refinement = any nonzero vertical defect is entered into the complete
closed-holonomy ledger.
inadmissible refinement = a nonzero vertical defect affects source/future
composition while absent from the ledger.
```

This is the intrinsic form of the no-silent-refinement principle. It is not a
smoothness axiom. It is the same no-silent-history law applied to refinement
fibers: anything that can affect source, response, or future composition is a
record distinction and belongs to the process.

The amplitude-only trap is decisive. If a zero-coarse oscillatory holonomy has
amplitude `O(n^{-2})`, its flux energy can tend to zero while:

```math
\|\delta v_n\|_{\rm source}
```

stays finite. Thus admissibility cannot be based only on KL content, L2
holonomy size, or coarse projection. It must be based on the full intrinsic
readout complex:

```text
RN work;
cellular source work;
allowed-change response work;
future composition work.
```

For the current finite packet, the source readout already catches the
zero-coarse attack. A cofinally silent vertical oscillation must scale fast
enough that both the holonomy and the induced source vanish in the intrinsic
norms.

Thus the continuum condition becomes sharper:

```text
projective complete h + projective P^{hist} + convergent L
+ intrinsic admissible refinement.
```

If the whole sealed ISP process supplies this admissible refinement relation,
then hidden fine sources cannot be smuggled into the continuum. If the analyst
chooses which vertical defects to ignore, the continuum limit is branch B.

## 51. Intrinsic admissible-refinement diagnostic

The diagnostic script is:

```text
code/v6_p4v_intrinsic_admissible_refinement.py
```

It tests the KL/RN chain rule, no-silent hidden fiber work, zero-coarse source
holonomy, the amplitude-only trap, and the source-work gate.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| count-reference preservation | push forward the fine count law to the coarse count law | equal fibers preserve the intrinsic reference; unequal fibers do not | unequal_gap=1.500e-01 | PASS-GATE |
| neutral refinement | split each atom into two count-dual atoms | coarse law, KL content, and fiber action are exactly unchanged | push=0.0e+00, dKL=0.0e+00, fiber=0.0e+00 | PASS-SILENT |
| KL chain rule | add a hidden fiber contrast with identical coarse pushforward | hidden RN work is the conditional KL defect | push=2.8e-17, dKL=0.179191 | PASS-DETECTS-HIDDEN-WORK |
| no-silent-history | let the hidden fiber sign affect the next diamond | same coarse law is not the same physical process | fiber_range=1.324925, future_gap=0.429200 | REFUTES-SILENT-HIDDEN-FIBER |
| zero-coarse source attack | alternating fine interface holonomy with zero coarse flux | coarse shadow vanishes while source density remains nonzero | coarse_gap=0.0e+00, density=4.096e+00, energy=4.224e-03 | REFUTES-COARSE-ONLY |
| amplitude-only trap | scale zero-coarse amplitude as n^-2 | flux energy vanishes but source density stays finite | energy16/32/64=4.15e-03/1.01e-03/2.48e-04; density=2.00e+00/2.00e+00/2.00e+00 | REFUTES-KL-OR-L2-ONLY |
| intrinsic source-work gate | scale zero-coarse amplitude as n^-4 | source readout defect vanishes cofinally | energy16/32/64=6.33e-08/9.60e-10/1.48e-11; density=7.81e-03/1.95e-03/4.88e-04 | PASS-SILENT-COFINALLY |
| admissible refinement verdict | RN chain rule plus cellular source/readout defect | silent refinement is equality in all intrinsic future-relevant readouts | hidden defects retained or vanish | FINITE-INTRINSIC-LAW |

The decisive numbers are:

```text
neutral refinement:
  neutral_push_gap = 0.000000000000000e+00
  neutral_kl_gap = 0.000000000000000e+00
  neutral_fiber_action_range = 0.000000000000000e+00

hidden fiber contrast:
  hidden_push_gap = 2.775557561562891e-17
  hidden_kl_gap = 1.791905099427198e-01
  hidden_fiber_action_range = 1.324925414743598e+00
  hidden_future_gap = 4.292000000000000e-01

count reference:
  unequal_count_reference_gap = 1.500000000000000e-01

zero-coarse source:
  osc_coarse_gap = 0.000000000000000e+00
  osc_density_max = 4.096000000000000e+00
  osc_energy = 4.223999999999999e-03

amplitude-only trap:
  trap_energy_16_32_64 = 4.15e-03/1.01e-03/2.48e-04
  trap_density_16_32_64 = 2.00e+00/2.00e+00/2.00e+00

source-work gate:
  admissible_energy_16_32_64 = 6.33e-08/9.60e-10/1.48e-11
  admissible_density_16_32_64 = 7.81e-03/1.95e-03/4.88e-04
```

The finite verdict is:

```text
admissible silent refinement is not a coarse-shadow condition;
it is equality, or cofinal vanishing, in the full intrinsic readout complex.
Hidden fiber RN work, hidden source divergence, and hidden future composition
are all physical vertical defects unless retained in the complete ledger.
```

## 52. Readout-completeness campaign

The admissible-refinement law uses the phrase "all intrinsic
future-relevant readouts." That phrase must not remain decorative. The next
finite question is:

```text
does the proposed readout complex separate vertical refinement defects?
```

The finite answer has two independent parts.

First, for probability/history fibers, scalar work is not enough. Two fine
history laws can have:

```text
same coarse pushforward;
same conditional KL work;
different hidden orientation;
different future composition.
```

Thus a scalar value such as `D(P_f||mu_f)-D(P_c||mu_c)` detects that some
hidden work exists, but it does not classify the hidden record distinction.
The complete history readout is the vertical RN action:

```math
V_\pi
=
\log {dP_f\over d\mu_f}
-
\pi^*
\log {dP_c\over d\mu_c}.
```

Given `P_c`, `mu_f`, `mu_c`, and `V_pi`, the fine law is reconstructed:

```math
P_f(\omega)
=
\mu_f(\omega)
\exp\!\left[
\pi^*\log {dP_c\over d\mu_c}(\omega)+V_\pi(\omega)
\right].
```

So the probability side is complete only when the full vertical RN field is
kept, not merely its scalar KL norm.

Second, for cellular interface holonomy, source alone is not enough. On a
finite graph/cell complex, let `h` be an edge/interface cochain. The source
readout is the divergence:

```math
B h,
```

where `B` is the incidence/coboundary matrix. A plaquette circulation has:

```math
B h=0
```

but has nonzero closed-cycle period. Therefore source readout misses
circulation/curvature.

Conversely, closed-cycle periods alone are not enough. A cut/gradient defect
has zero plaquette period but nonzero source. Thus the finite cellular
readout must include both:

```text
source/divergence readouts;
closed-cycle/period readouts.
```

For a connected rectangular cell complex with `V` vertices, `E` edges, and
`F` faces:

```math
E=(V-1)+F.
```

The reduced incidence rows have rank `V-1`, the independent face-period rows
have rank `F`, and together they have rank `E`. Hence:

```math
\ker
\begin{pmatrix}
B_{\rm red}\\
C
\end{pmatrix}
=0.
```

This is the finite cellular readout-completeness theorem. A vertical edge
cochain with zero source and zero closed-cycle periods is zero. Therefore no
interface holonomy defect can be source-silent and period-silent while still
changing future cellular transport.

Scalar work fails again. One can match the total edge `L^2` work of a
circulation defect and a source defect while their readout/future effects
differ. Thus the complete readout is not a scalar energy. It is the vector of
intrinsic components:

```text
vertical RN action;
source/divergence;
closed-cycle periods;
and, downstream, any response/future-composition functional generated by
these complete fields.
```

The general finite criterion is:

```text
readout-complete = the combined readout map has zero kernel on vertical
defects modulo declared gauge/silent identities.
```

If a proposed future-composition functional is not in the dual span of the
complete readout map, it is not a consequence of the current ontology. It is a
new physical readout and must be added to the ledger. This is not a weakness;
it is the Leibniz discipline in operational form.

Thus the admissible-refinement theorem becomes exact at finite level:

```text
silent vertical defect
  = zero vertical RN action
  + zero source/divergence
  + zero closed-cycle period
  + zero value under every declared future-composition readout
  = no physical defect.
```

Partial lists fail. The complete finite readout list separates the tested
history and cellular vertical defects.

## 53. Readout-completeness diagnostic

The diagnostic script is:

```text
code/v6_p4w_readout_completeness.py
```

It tests scalar-work twins, full vertical RN reconstruction, source-only and
period-only cellular attacks, scalar cellular work, and the rank theorem for
source plus face-period readouts.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| history scalar-work attack | same coarse law and same conditional KL with different hidden orientation | scalar RN work does not determine future composition | dKL_gap=0.0e+00, future_gap=0.561600 | REFUTES-SCALAR-HISTORY |
| vertical RN action | reconstruct fine law from coarse law plus full fiber action | full vertical action separates hidden history twins | action_gap=2.305359, recon=1.4e-17 | PASS-HISTORY-COMPLETE |
| source-only attack | plaquette circulation has zero divergence | source readout misses closed-cycle holonomy | source=0.0e+00, period=4.242641 | REFUTES-SOURCE-ONLY |
| period-only attack | cut/gradient defect has zero plaquette period | cycle readout alone misses source | period=0.0e+00, source=2.449490 | REFUTES-PERIOD-ONLY |
| scalar work attack | match edge L2 work for different defects | same scalar work gives different readout/future effect | energy_gap=2.2e-16, readout_gap=4.000000 | REFUTES-SCALAR-CELLULAR |
| cellular rank theorem | divergence/source plus independent face periods | readout map has full rank on edge cochains | E=17, rankB=11, rankC=6, rankFull=17 | PASS-SEPARATES-EDGES |
| cellular reconstruction | solve defect from complete cellular readout | kernel is zero and defect is reconstructed | kernel=0, gap=3.3e-16 | PASS-COMPLETE |
| readout-completeness verdict | vertical RN action plus cellular source/cycle readouts | partial summaries have twins; complete finite readout separates them | history + cellular | FINITE-COMPLETENESS |

The decisive numbers are:

```text
history scalar-work twins:
  history_conditional_kl_a = 1.420672524729726e-01
  history_conditional_kl_b = 1.420672524729726e-01
  history_scalar_kl_gap = 0.000000000000000e+00
  history_future_gap = 5.616000000000000e-01
  history_vertical_action_gap = 2.305359019876771e+00
  history_reconstruction_gap = 1.387778780781446e-17

cellular complex:
  edge_count = 17
  vertex_count = 12
  face_count = 6
  rank_source = 11
  rank_period = 6
  rank_full = 17

partial readout failures:
  cycle_source_norm = 0.000000000000000e+00
  cycle_period_norm = 4.242640687119285e+00
  gradient_period_norm = 0.000000000000000e+00
  gradient_source_norm = 2.449489742783178e+00
  scalar_energy_gap = 2.220446049250313e-16
  scalar_readout_gap = 4.000000000000000e+00

complete reconstruction:
  cellular_reconstruction_gap = 3.330669073875470e-16
  cellular_kernel_dim = 0
```

The finite verdict is:

```text
the readout complex is complete only as a vector complex, not as a scalar
work value;
history fibers require the full vertical RN action;
cellular holonomy requires both source/divergence and closed-cycle periods;
the combined finite cellular readout has zero kernel.
```

## 54. Cofinal readout-completeness campaign

The previous diagnostic proved readout completeness on one rectangular cell
complex. The next Einstein question is whether this was an artifact of that
grid. The finite answer is a general graph/cell-complex theorem.

Let `G=(V,E)` be a connected finite sealed interface graph. Let:

```math
B:C_1(G)\to C_0(G)
```

be the oriented incidence/source map, and let `B_red` be `B` with one
redundant constant row removed. Then:

```math
{\rm rank}(B_{\rm red})=|V|-1.
```

The cycle space has dimension:

```math
\beta_1(G)=|E|-|V|+1.
```

Choose any independent cycle-period basis:

```math
C:C_1(G)\to\mathbb R^{\beta_1(G)}.
```

Here "cycle-period basis" means a basis of the closed interface loops, not
only the local plaquette faces. Then the complete cellular readout map is:

```math
R_G
=
\begin{pmatrix}
B_{\rm red}\\
C
\end{pmatrix}.
```

**Finite readout-completeness theorem.** For every connected finite sealed
interface graph:

```math
{\rm rank}(R_G)=|E|,
\qquad
\ker R_G=0.
```

Proof. The source-free subspace is:

```math
\ker B.
```

It has dimension `beta_1(G)`. If `h` is killed by `B_red`, then `h` is a
cycle. If the complete cycle-period basis also kills `h`, then `h` is
orthogonal to every cycle basis vector, hence to the whole cycle space. Since
`h` itself is in the cycle space, `h=0`. Therefore the stacked readout has
zero kernel. Counting gives full rank:

```math
(|V|-1)+(|E|-|V|+1)=|E|.
```

This theorem also identifies the topological trap. On a simply connected
rectangular cell complex, local face periods form a complete cycle basis:

```math
\beta_1=(n_x-1)(n_y-1).
```

But on a complex with a hole, local face periods are not complete. A global
homology circulation can have:

```math
B h=0,
\qquad
C_{\rm local}h=0,
\qquad
h\ne0.
```

Thus a sealed diamond with nontrivial topology must include homology cycle
periods as record readouts. Otherwise a global loop holonomy becomes a ghost
refinement.

The cofinal form is now precise. A refinement family is readout-complete if
each finite level uses:

```text
vertical RN action for history fibers;
source/divergence readouts for boundary/cut defects;
a complete independent cycle-period basis, including homology cycles;
the future-composition readouts generated by those complete fields.
```

Then:

```text
zero readout at every finite level
=> zero vertical defect at every finite level
=> zero projective/cylinder defect in the limit.
```

This is not a smoothness assumption. It is a finite separating theorem plus
projective consistency. The only way to defeat it is to produce a future
composition functional not represented in the dual span of the readout map.
If that happens, the readout list was incomplete and the new functional must
be added as a physical readout.

The refined no-silent rule is therefore:

```text
no silent vertical defect =
  no hidden RN action
  + no source/divergence
  + no local or homology cycle period
  + no future-composition functional outside the readout span.
```

This is the cofinal version of the finite Leibniz discipline. If two
refinement families differ but all finite readouts agree at every level, then
they are the same physical sealed process. If they differ in a finite readout,
the difference is physical and must be retained.

## 55. Cofinal readout-completeness diagnostic

The diagnostic script is:

```text
code/v6_p4x_cofinal_readout_completeness.py
```

It tests rectangular grids of increasing size, a general connected graph with
a fundamental cycle basis, a hole/homology attack, partial source/period
attacks, and a zero-coarse vertical defect.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| rectangular cofinal ranks | test simply connected grids of increasing size | source plus face periods have zero kernel at every tested scale | 3x3:E=12,F=4,rank=12,ker=0; 4x3:E=17,F=6,rank=17,ker=0; 5x4:E=31,F=12,rank=31,ker=0; 6x5:E=49,F=20,rank=49,ker=0 | PASS-COFINAL-FINITE |
| general graph rank theorem | source plus fundamental cycle basis on connected graph | rank(B_red)+rank(cycles)=E and full kernel is zero | E=12, rankB=7, cycles=5, rankFull=12, ker=0 | PASS-GRAPH |
| homology-hole attack | cycle graph with no local face period | source and local faces miss global circulation | local_ker=1, source=0.0e+00, local_period=0.0e+00, homology=8.0 | REFUTES-LOCAL-FACES-ONLY |
| homology completion | add the independent global cycle period | hole circulation is separated and kernel vanishes | rankLocal=7, rankFull=8, ker=0 | PASS-TOPOLOGY-COMPLETE |
| source/period twin attacks | test circulation and cut defects on rectangle | source-only and period-only lists both have twins | circ_source=0.0e+00, circ_period=4.243; cut_period=0.0e+00, cut_source=2.449 | REFUTES-PARTIAL-LISTS |
| zero-coarse vertical defect | pairwise fine defect with exact zero coarse shadow | coarse projection misses a nonzero fine vertical vector | coarse=0.0e+00, fine_norm=0.784362 | REFUTES-COARSE-SHADOW |
| cofinal readout verdict | all finite levels use source plus complete cycle basis | zero readout at every finite level implies zero vertical defect | rect_pass=True, graph_ker=0, ring_ker=0 | FINITE-COFINAL-COMPLETENESS |

The decisive numbers are:

```text
rectangular grids:
  rect_3x3: vertices=9, edges=12, faces=4,
             rank_source=8, rank_period=4, rank_full=12, kernel=0
  rect_4x3: vertices=12, edges=17, faces=6,
             rank_source=11, rank_period=6, rank_full=17, kernel=0
  rect_5x4: vertices=20, edges=31, faces=12,
             rank_source=19, rank_period=12, rank_full=31, kernel=0
  rect_6x5: vertices=30, edges=49, faces=20,
             rank_source=29, rank_period=20, rank_full=49, kernel=0

general graph:
  graph_edges = 12
  graph_rank_source = 7
  graph_rank_cycles = 5
  graph_rank_full = 12
  graph_kernel = 0

homology attack:
  ring_local_kernel = 1
  ring_full_kernel = 0
  ring_source_norm = 0.000000000000000e+00
  ring_local_period_norm = 0.000000000000000e+00
  ring_homology_norm = 8.000000000000000e+00

partial readout attacks:
  circulation_source_norm = 0.000000000000000e+00
  circulation_period_norm = 4.242640687119285e+00
  cut_source_norm = 2.449489742783178e+00
  cut_period_norm = 0.000000000000000e+00

coarse-shadow attack:
  zero_coarse_gap = 0.000000000000000e+00
  zero_fine_norm = 7.843622467070546e-01
```

The finite verdict is:

```text
cofinal readout completeness is a graph/cell-complex rank theorem;
local face periods are enough only in simply connected complexes;
holes require homology cycle periods;
with a complete cycle basis, source plus periods have zero kernel at every
tested finite level.
```

## 56. Closed-holonomy dynamics campaign

Readout completeness tells us what data separate `h`. Dynamics asks a
different question:

```text
what determines h?
```

The finite answer is sharp. On a connected sealed interface graph, the
complete readout map:

```math
R_G
=
\begin{pmatrix}
B_{\rm red}\\
C
\end{pmatrix}
```

has zero kernel. Therefore the finite closed-holonomy response equation:

```math
R_G h_G
=
\begin{pmatrix}
\rho_G\\
\kappa_G
\end{pmatrix}
```

has a unique solution for every supplied source/period datum
`(rho_G,kappa_G)`.

This is the proper finite Hodge law:

```text
source/divergence data + complete cycle periods determine interface holonomy.
```

It also explains why the weaker candidates fail.

**Vacuum consistency.** If:

```math
\rho_G=0,
\qquad
\kappa_G=0,
```

then:

```math
h_G=0.
```

So maximum entropy, least work, and consistency all agree on the eventless
vacuum. That is good, but it is not a law for nonzero physical holonomy.

**Source-only dynamics fails.** If only `rho_G` is fixed, a closed cycle can be
added to `h_G` without changing the source:

```math
B_{\rm red}(h_G+c)=B_{\rm red}h_G,
\qquad
C(h_G+c)\ne Ch_G.
```

Thus source-only dynamics silently erases global/cyclic holonomy.

**Period-only dynamics fails.** If only cycle periods are fixed, a cut or
gradient defect can be added without changing the periods:

```math
C(h_G+\nabla f)=Ch_G,
\qquad
B_{\rm red}(h_G+\nabla f)\ne B_{\rm red}h_G.
```

Thus period-only dynamics misses source.

**Scalar work fails.** Matching total edge work:

```math
\|h_1\|=\|h_2\|
```

does not imply the same source, periods, or future composition. Work is a
useful diagnostic, not a complete law.

**Least-work trap.** Solving only the source equation and silently setting all
cycle periods to zero gives a unique representative, but it is the wrong
claim: it selects a zero-period gauge by convention. If the physical diamond
has nonzero cycle periods, that solution erases real holonomy.

Therefore the finite dynamics result is:

```text
complete closed-holonomy response is unique for supplied complete physical
readout data;
the response equation does not by itself select the source/period data.
```

This is exactly the boundary between kinematics and dynamics. The finite
equation:

```math
R_Gh_G=(\rho_G,\kappa_G)
```

is a real field equation. It says how complete physical readout data determine
the sealed holonomy field. But the deeper branch-A theorem must still explain
why the whole sealed ISP process supplies a particular projective family:

```math
(\rho_G,\kappa_G)_G.
```

If those data are chosen externally, the response equation is branch B with a
clean intrinsic geometry. If they are generated by the indivisible process
law, the response equation becomes the gravity/holonomy sector of branch A.

## 57. Closed-holonomy dynamics diagnostic

The diagnostic script is:

```text
code/v6_p4y_closed_holonomy_dynamics.py
```

It tests vacuum consistency, source-only and period-only twins, scalar-work
twins, the least-work trap, unique complete response, and the remaining
source-law boundary.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| vacuum consistency | set all source and cycle-period data to zero | complete response equation selects h=0 | norm=0.0e+00 | PASS-VACUUM |
| source-only no-go | add a closed cycle to h | source is unchanged but periods/future holonomy change | source_gap=1.1e-16, period_gap=0.883346, h_gap=0.340000 | REFUTES-SOURCE-ONLY-DYNAMICS |
| period-only no-go | add a cut/gradient to h | periods are unchanged but source changes | period_gap=5.6e-17, source_gap=0.416413 | REFUTES-PERIOD-ONLY-DYNAMICS |
| least-work trap | solve source with all cycle periods silently set to zero | same source is recovered but physical periods are erased | source_gap=1.7e-16, lost_period=0.620086, h_gap=0.408515 | REFUTES-UNSUPPLIED-PERIODS |
| scalar-work no-go | match L2 work of cut and cycle defects | same scalar work gives different complete readout | work_gap=0.0e+00, readout_gap=4.415880 | REFUTES-SCALAR-DYNAMICS |
| complete response equation | solve [B_red; C]h=(rho,kappa) | source plus periods reconstruct h uniquely | rank=17/17, kernel=0, gap=1.2e-16 | PASS-UNIQUE-RESPONSE |
| source-law boundary | change one physical period datum | new data give a new unique solution; the response law does not select the data | readout_gap=0.310000, h_gap=0.200278 | OPEN-SOURCE-LAW |
| closed-holonomy dynamics verdict | selectors versus complete readout response | finite dynamics closes as response to physical source/period data, not as universal h selection | unique response / source law open | FINITE-DYNAMICS-BOUNDARY |

The decisive numbers are:

```text
readout map:
  edge_count = 17
  vertex_count = 12
  cycle_count = 6
  rank_readout = 17
  kernel_dim = 0

unique response:
  complete_reconstruction_gap = 1.249000902703301e-16

vacuum:
  vacuum_norm = 0.000000000000000e+00

source-only no-go:
  source_only_source_gap = 1.110223024625157e-16
  source_only_period_gap = 8.833459118601275e-01
  source_only_h_gap = 3.400000000000000e-01

period-only no-go:
  period_only_period_gap = 5.551115123125783e-17
  period_only_source_gap = 4.164132562731403e-01

least-work trap:
  least_work_source_gap = 1.665334536937735e-16
  least_work_lost_period_norm = 6.200860347411501e-01
  least_work_h_gap = 4.085154006326709e-01

scalar-work no-go:
  scalar_work_gap = 0.000000000000000e+00
  scalar_readout_gap = 4.415880433163924e+00

source-law boundary:
  changed_readout_gap = 3.099999999999999e-01
  changed_h_gap = 2.002780675656377e-01
```

The finite verdict is:

```text
the complete Hodge/readout equation uniquely determines h from complete
source and period data;
no invariant tested here selects those data from nothing;
the missing branch-A object is the whole-process law for the projective
source/period family.
```

## 58. Projective source/period origin campaign

The response equation left a clean question:

```text
are rho_G and kappa_G supplied externally, or are they readouts of the same
whole-history law P_G^{hist}?
```

The finite answer is positive once the complete closed-holonomy ledger has
been supplied. Let the whole-history law have count reference `mu_G` and
finite RN action:

```math
A_G=\log {dP_G^{\rm hist}\over d\mu_G}.
```

Expand `A_G` in the complete interface/closed-history basis and write the
edge/interface coefficients as:

```math
h_G\in C_1(G).
```

Then source and period are not new data. They are the exact and cyclic
derivatives/readouts of the same RN action:

```math
\rho_G=B_{\rm red}h_G,
\qquad
\kappa_G=C h_G.
```

Equivalently:

```math
\begin{pmatrix}
\rho_G\\
\kappa_G
\end{pmatrix}
=
R_Gh_G,
\qquad
R_G=
\begin{pmatrix}
B_{\rm red}\\
C
\end{pmatrix}.
```

This closes the finite source/period origin problem:

```text
P_G^{hist} -> A_G -> h_G -> (rho_G,kappa_G).
```

It also rejects external assignments. If the same `P_G^{hist}` is held fixed
but `rho_G` is altered by hand, the altered source is not the derivative of
the same RN action. It defines a different response problem, hence a different
history law or an external source convention.

The source-only twin attack remains a useful warning. Adding a closed cycle to
`h_G` leaves:

```math
B_{\rm red}h_G
```

fixed, but changes:

```math
C h_G
```

and can change future composition. Therefore `rho_G` alone is not the
originating readout. The pair `(rho_G,kappa_G)` is.

The projective test also passes in finite form. A neutral edge/history split
with zero vertical RN defect preserves the coarse coefficients:

```math
\pi_*h_f=h_c,
```

and therefore preserves:

```math
B_{\rm red}h_c,
\qquad
C h_c.
```

But a hidden fine split with opposite vertical defects can have the same
coarse `h_c`, `rho_c`, and `kappa_c` while carrying nonzero fine vertical RN
data. That is not a contradiction. It is exactly the admissible-refinement
law: the hidden fine defect is physical unless it vanishes in the complete
fine readout complex or is retained in the fine closed-holonomy ledger.

Thus the source/period chain is now:

```text
whole-history law P^{hist}
-> RN action A
-> interface holonomy coefficients h
-> exact/cycle readouts (rho,kappa)
-> unique response h = R^{-1}(rho,kappa).
```

The last arrow is redundant at finite level, because it reconstructs the same
`h`; that redundancy is good. It is the finite consistency check that the
source/period readouts and the response equation are the same object read in
opposite directions.

The remaining open object is therefore smaller:

```text
derive the projective whole-history law P_G^{hist};
then rho, kappa, A, h, and the response field follow as readouts.
```

If `P_G^{hist}` is chosen externally, the theory is branch B. If the
indivisible ISP process law supplies `P_G^{hist}` cofinally, source and period
are branch-A readouts, not extra inputs.

## 59. Projective source/period origin diagnostic

The diagnostic script is:

```text
code/v6_p4z_source_period_origin.py
```

It reconstructs `h` from a finite whole-history edge law, derives
`rho,kappa`, rejects external reassignment, tests source-only twins, and checks
neutral/projective versus hidden fine vertical refinements.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| RN coefficient origin | recover h from the finite whole-history edge law | half-log odds reconstruct the closed-holonomy coefficients | gap=1.1e-16 | PASS-H-FROM-P |
| source/period derivation | apply exact/cycle readouts to reconstructed h | rho and kappa are derivatives/readouts of the same RN action | rho_dim=11, kappa_dim=6, response_gap=1.4e-16 | PASS-DERIVES-READOUTS |
| same-P external-source attack | alter rho after P_hist is fixed | altered source is not the derivative of the same history law | residual=0.210, h_gap=0.278091 | REFUTES-EXTERNAL-RHO |
| source-only twin | add closed cycle to h | same rho has different kappa and future composition | source_gap=2.2e-16, kappa_gap=0.727461, future_gap=0.013434 | REFUTES-RHO-ONLY |
| same complete readout | solve response from identical rho and kappa | same complete readout gives same h and same future | h_gap=1.4e-16, future_gap=0.0e+00 | PASS-NO-TWIN |
| projective neutral lift | split every edge coefficient with zero vertical defect | coarse source and periods are exactly preserved | coarse=0.0e+00, vertical=0.0e+00, rho=2.2e-16, kappa=3.9e-16 | PASS-PROJECTIVE |
| hidden fine vertical attack | add opposite fine defects with the same coarse h | coarse rho/kappa agree but fine vertical RN data are nonzero | coarse=0.0e+00, vertical=0.172988, future=0.989129 | REFUTES-COARSE-ONLY |
| source/period origin verdict | P_hist -> h -> (rho,kappa) with projective tests | source and periods are intrinsic readouts once P_hist is supplied | process law still selects P_hist | FINITE-ORIGIN-CLOSED |

The decisive numbers are:

```text
dimensions:
  edge_count = 17
  rho_dim = 11
  kappa_dim = 6

origin:
  rn_reconstruction_gap = 1.110223024625157e-16
  response_gap = 1.387778780781446e-16

external-source attack:
  external_source_residual = 2.100000000000000e-01
  external_h_gap = 2.780913206281269e-01

source-only twin:
  source_twin_gap = 2.220446049250313e-16
  kappa_twin_gap = 7.274613391789284e-01
  future_source_twin_gap = 1.343382156467493e-02

same complete readout:
  same_h_gap = 1.387778780781446e-16
  same_future_gap = 0.000000000000000e+00

projective neutral lift:
  neutral_coarse_gap = 0.000000000000000e+00
  neutral_vertical_norm = 0.000000000000000e+00
  rho_projective_gap = 2.220446049250313e-16
  kappa_projective_gap = 3.885780586188048e-16

hidden fine vertical attack:
  hidden_coarse_gap = 0.000000000000000e+00
  hidden_vertical_norm = 1.729879019285777e-01
  hidden_future_gap = 9.891285444318414e-01
```

The finite verdict is:

```text
source and cycle periods are intrinsic readouts of the whole-history RN action;
external rho/kappa assignments are rejected;
coarse agreement does not erase hidden fine vertical RN data;
the only remaining selector is the whole-process law for P^{hist}.
```

## 60. Whole-history law selection campaign

The last open object is now exposed cleanly:

```text
P_G^{hist}.
```

This section attacks it directly. The question is not whether a complete
whole-history law determines its RN action, source, periods, response field,
and future composition. The previous sections prove that it does. The question
is whether the structural principles already stated select the law itself.

The answer is no at finite level. There is a one-parameter family of positive
sealed whole-history laws that satisfies the current structural packet:

```text
count reference;
exact RN action;
readout completeness;
neutral/projective refinement;
sealed product gluing;
positive non-divisibility;
retained future-relevant memory.
```

Let a sealed three-stage history have signs:

```math
\omega=(a,b,c)\in\{\pm 1\}^3,
```

and let the count reference be uniform:

```math
U(\omega)=1/8.
```

For any `theta in (-1,1)`, define:

```math
P_\theta(a,b,c)
=
{1\over 8}\{1+\theta abc\}.
```

This is the smallest clean model of a retained closed history holonomy. Every
one-variable and two-variable shadow is count-uniform, but the complete
three-history law changes with `theta`. The RN action relative to count is:

```math
A_\theta(a,b,c)
=
\log {dP_\theta\over dU}
=
\log(1+\theta abc).
```

Equivalently, up to an additive normalization, the separating closed-history
coefficient is:

```math
h_\theta
=
{1\over 2}
\log {1+\theta\over 1-\theta}.
```

Thus a complete RN/Mobius ledger reconstructs the law. But this is not a
selection theorem: it reconstructs whichever `theta` was already present.

This family defeats the obvious possible selectors:

- shadows fail, because all one- and two-time marginals agree for every
  `theta`;
- RN identities fail as selectors, because every `P_theta` satisfies them
  exactly;
- neutral refinement fails as a selector, because every `P_theta` has an exact
  count-preserving twin refinement;
- sealed gluing fails as a selector, because product gluing adds the
  closed-history coefficients for arbitrary `theta`;
- non-divisibility fails as a selector, because every nonzero `theta` gives
  positive conditional memory;
- scalar work and entropy fail as selectors, because entropy chooses
  `theta=0`, the divisible vacuum, while maximum memory runs to the boundary;
- even-orientation scalar selectors fail, because `theta` and `-theta` have
  the same entropy and conditional memory but opposite retained future
  orientation.

This is not a failure of the RN/holonomy ontology. It is the finite proof that
RN/holonomy readouts are readouts of the law, not the law itself.

**Finite no-go.** The current structural invariants do not determine
`P_G^{hist}`. They leave a positive one-parameter family of mutually
future-distinguishable indivisible history laws. Therefore the cofinal
whole-history law must be supplied by the actual indivisible process rule for
possible complete histories, or by a new invariant whose content is directly
about whole-history probability, not merely about consistency of its readouts.

In Einstein language: a family of invariant process laws is not yet a law of
nature. In Feynman language: two histories with the same shadows and the same
formal receipts still give different next experiments, so the missing object
is operationally real.

## 61. Whole-history law selection diagnostic

The diagnostic script is:

```text
code/v6_p4aa_whole_history_law_selection.py
```

It builds the finite parity family `P_theta`, checks all current structural
receipts, and then compares two different values of `theta`.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| same shadows, different laws | compare two parity whole-history laws | all one/two marginals agree but the full law differs | pair_gap=0.0e+00, TV=0.210000 | REFUTES-SHADOW-SELECTION |
| RN/readout completeness | recover each law from its complete parity RN coefficient | complete readout reconstructs but does not select the coefficient | hA=0.331647, hB=0.950479, recon=2.8e-17 | PASS-READOUT-NOT-SELECTION |
| RN identities | check integral fluctuation identities against count reference | both laws satisfy exact RN consistency | gap=0.0e+00 | PASS-CONSISTENCY-FAMILY |
| neutral refinement | split every history atom into count twins | both laws are projectively compatible under neutral refinement | gap=0.0e+00 | PASS-PROJECTIVE-FAMILY |
| sealed gluing | independent product of two sealed histories | closed-holonomy coefficients add exactly for arbitrary theta | gap=1.4e-17 | PASS-GLUING-FAMILY |
| non-divisibility family | require positive conditional memory | non-divisibility removes theta=0 but leaves a continuum | CMI_A=0.052112, CMI_B=0.306760, count>0.02=80 | REFUTES-NONDIV-UNIQUENESS |
| sign/orientation twin | compare theta and -theta | same entropy and CMI can have different future orientation | cmi_gap=6.9e-18, S_gap=0.0e+00, future_gap=0.640000 | REFUTES-SCALAR-SELECTORS |
| selector audit | max entropy and max memory over the family | max entropy selects divisible vacuum; max memory runs to boundary | theta_entropy=0.00, theta_maxCMI=0.99 | FAILS-AS-LAW |
| future-composition difference | use parity moment as retained future coupling | surviving laws predict different next composition | future_gap=0.420000 | PHYSICAL-FAMILY |
| whole-history selection verdict | gluing + projectivity + RN + readout completeness + nondivisibility | the structural packet leaves a positive one-parameter family | P_hist must be primitive/process law | FINITE-NO-GO |

The decisive numbers are:

```text
theta_a = 3.200000000000000e-01
theta_b = 7.400000000000000e-01
pairwise_shadow_gap = 0.000000000000000e+00
full_total_variation = 2.100000000000000e-01
h_a = 3.316471087051321e-01
h_b = 9.504793805965235e-01
reconstruction_gap_a = 2.775557561562891e-17
reconstruction_gap_b = 0.000000000000000e+00
rn_identity_gap = 0.000000000000000e+00
neutral_refinement_gap = 0.000000000000000e+00
product_gluing_gap = 1.387778780781446e-17
cmi_a = 5.211170267878970e-02
cmi_b = 3.067604742713415e-01
nondivisible_count_threshold_0p02 = 80
sign_cmi_gap = 6.938893903907228e-18
sign_entropy_gap = 0.000000000000000e+00
sign_future_gap = 6.400000000000001e-01
max_entropy_theta = 0.000000000000000e+00
max_cmi_theta_grid = 9.900000000000000e-01
future_gap = 4.199999999999999e-01
```

The finite verdict is:

```text
complete RN/readout data reconstruct P^{hist} once supplied;
the current structural packet does not select which P^{hist} is realized;
positive non-divisibility still leaves a continuum of laws;
therefore P_G^{hist} must be the cofinal indivisible ISP process law,
not a shadow derived from lower structural receipts.
```

## 62. V1-V5 closed-exchange action campaign

The older v1-v5 papers do give real guidance. They do not point toward another
local event score. They point toward:

```text
exact finite slabs;
localized finite deformations;
exchange defects;
projective endpoint/path kernels;
phase as stochastic holonomy;
non-Markovian whole-interval survival.
```

The strongest law form suggested by that stack is therefore a whole-history
closed-exchange action:

```text
P_h^{hist}(omega)
=
U_G(omega) exp(<h_G, chi_G(omega)> - psi_G(h_G)).
```

Here `chi_G` is the complete separating ledger of closed exchange-history
statistics, and `h_G` is the coefficient cochain. In this form the law is not
an endpoint kernel, not a Markov semigroup, and not a local rate. It is a
maximum-caliber/RN law over complete histories.

This is the correct schema. It exactly represents the parity no-go family:

```text
P_eta(a,b,c)
=
U(a,b,c) exp(eta abc - psi(eta)).
```

Equivalently, it is the same family as:

```text
P_theta(a,b,c)=1/8(1+theta abc),
theta=tanh(eta).
```

That is progress, but it is not closure. The schema identifies the coordinate
in which the law lives; it does not choose the value of `eta`, or in the
general case the complete coefficient field `h_G`.

The campaign tests the v1-v5 closures one by one.

- Maximum caliber with a fixed closed-holonomy mean reconstructs `eta`, but
  the mean is already complete whole-history information.
- Entropy maximization selects `eta=0`, the divisible vacuum.
- Memory maximization runs to a boundary.
- A regularized memory objective can have a clean interior optimum, but the
  optimum moves when the regularization coefficient moves.
- Born-square readout fixes the exponent of relative event weights, but not
  the common raw holonomy scale.
- Onset-renormalized universality can fix the normalized tangential bracket
  while leaving the raw whole-process coefficient free.

Thus v1-v5 point to the right form:

```text
closed exchange-holonomy whole-history law.
```

They do not by themselves select the coefficient field:

```text
h_G.
```

In branch-A language, the cofinal ISP process must supply `h_G` as part of the
whole-history law. If `h_G` is chosen by hand, this is branch B. If a future
theorem derives `h_G` from a stronger indivisible-process principle, then the
v1-v5 schema becomes the natural home of that theorem.

## 63. V1-V5 closed-exchange action diagnostic

The diagnostic script is:

```text
code/v6_p4ab_closed_exchange_action_campaign.py
```

It tests the v1-v5-inspired closed-exchange Gibbs/RN law against the parity
family and the obvious selectors.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| closed-exchange Gibbs form | represent parity whole-history laws as U exp(eta H) | the v1-v5 action shape exactly represents the complete law family | schema_gap=2.8e-17 | PASS-SCHEMA |
| coefficient selection | compare two eta values with same lower shadows | both are positive closed-holonomy laws but predict different future memory | pair_gap=0.0e+00, TV=0.210000, eta_span=0.618832 | FINITE-NO-GO |
| maximum caliber with fixed holonomy mean | recover eta from E[H] | works only after the complete whole-history moment is supplied | mean=0.320000, recon_gap=0.0e+00 | READOUT-NOT-SELECTION |
| entropy and memory selectors | maximize entropy or conditional memory over eta | entropy gives divisible vacuum; memory runs to the grid boundary | eta_entropy=0.00, eta_memory=3.00 | FAILS-AS-LAW |
| regularized memory selector | maximize CMI - alpha eta^2 | a nice interior optimum exists but moves with the free coefficient alpha | eta_a2=2.29, eta_a10=1.44 | BRANCH-B-COEFFICIENT |
| Born exponent compatibility | compare square readout under common holonomy rescaling | the square exponent fixes relative readout but not raw eta magnitude | born_gap=2.8e-17 | EXPONENT-NOT-SCALE |
| onset-renormalized universality | compare normalized holonomy orientation | the normalized bracket can agree while raw future memory differs | orient_gap=0.0e+00, future_gap=0.420000 | UNIVERSALITY-NOT-LAW |
| v1-v5 law verdict | finite slabs + exchange holonomy + projectivity + Born readout | these identify the correct law schema but not the cofinal coefficient field | P_hist=P_h, h still selected by whole ISP process | SCHEMA-CLOSED-LAW-OPEN |

The decisive numbers are:

```text
theta_a = 3.200000000000000e-01
theta_b = 7.400000000000000e-01
eta_a = 3.316471087051321e-01
eta_b = 9.504793805965235e-01
schema_gap = 2.775557561562891e-17
pairwise_shadow_gap = 0.000000000000000e+00
full_total_variation = 2.100000000000000e-01
eta_span = 6.188322718913913e-01
mean_holonomy_a = 3.200000000000000e-01
eta_from_mean_a = 3.316471087051321e-01
maxent_reconstruction_gap = 0.000000000000000e+00
entropy_selector_eta = 0.000000000000000e+00
memory_selector_eta = 3.000000000000000e+00
regularized_eta_alpha_0p02 = 2.290000000000000e+00
regularized_eta_alpha_0p10 = 1.440000000000000e+00
born_scale_gap = 2.775557561562891e-17
normalized_orientation_gap = 0.000000000000000e+00
future_memory_gap = 4.200000000000000e-01
```

The finite verdict is:

```text
v1-v5 identify the correct law schema:
  projective closed-exchange whole-history RN/Gibbs law.

They do not select the coefficient field:
  h_G.

Thus the remaining law is not another readout but the cofinal whole-process
selection of h_G, equivalently P_G^{hist}.
```

## 64. h_G field-equation campaign

The v1-v5 campaign closes the law schema:

```text
P_h^{hist}(omega)
=
U_G(omega) exp(<h_G,chi_G(omega)> - psi_G(h_G)).
```

The remaining question is the Einstein question:

```text
what invariant field equation selects h_G?
```

This campaign attacks the finite one-dimensional version first. In the parity
model, `h_G` is the scalar `eta`. A real field equation must explain why one
`eta` is realized rather than another. The campaign tests the strongest
available candidates.

1. **Source-free least action.** A homogeneous quadratic response equation
   selects `eta=0`, the divisible vacuum. It is too weak.
2. **Supplied source response.** A linear equation `eta=R^{-1}j` selects a
   value only after `j` is supplied. That is a response law, not an intrinsic
   process law.
3. **Self-source identity.** If the source is defined as the expectation of the
   holonomy under the same law, then `eta=atanh(E_eta[H])` is true for every
   `eta`. It is a readout identity.
4. **Sealed gluing.** Product histories add closed-exchange coefficients
   exactly, but for arbitrary coefficients. It is consistency, not dynamics.
5. **Non-divisibility threshold.** Choosing the smallest `eta` with positive
   memory above `epsilon` selects a value only when `epsilon` is supplied.
6. **Self-induced memory equation.** Equations such as
   `eta=lambda tanh(eta)` can select nonzero values, but the selected value
   moves with the supplied coupling `lambda`.
7. **Regularized memory action.** Objectives such as
   `CMI(eta)-alpha eta^2` can have clean interior optima, but the optimum moves
   with the supplied regularization coefficient.
8. **Quantized holonomy unit.** Restricting `eta` to multiples of a unit leaves
   many possibilities unless the unit and level are supplied.
9. **Onset-renormalized exchange bracket.** A normalized bracket can fix the
   direction/sign of `eta`, but not its magnitude.

The finite result is a no-go for the current candidate field-equation list:

```text
every tested equation is vacuum, tautological, coefficient-dependent,
threshold-dependent, source-dependent, or family-valued.
```

This does not refute branch A. It sharpens it. The missing equation cannot be
another invariant consistency law over the already known readouts. It must be
the actual indivisible process law selecting the complete coefficient field
`h_G` cofinally.

In other words:

```text
h_G is not selected by the response calculus.
h_G is the process field selected by the whole-history ISP law.
```

## 65. h_G field-equation diagnostic

The diagnostic script is:

```text
code/v6_p4ac_h_field_equation_campaign.py
```

It tests the field-equation candidates against the parity law.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| source-free least action | solve the homogeneous quadratic field equation | the only selected solution is the divisible vacuum | eta=0 | FAILS-NONDIV |
| supplied source response | eta = R^{-1} j | selects eta only after the source value is supplied externally | jA=0.320000, etaA=0.331647; jB=0.740000, etaB=0.950479 | BRANCH-B-SOURCE |
| self-source identity | j(eta)=E_eta[H], eta=atanh(j) | exact for every eta, so it is a readout identity, not a field equation | gapA=5.6e-17, gapB=0.0e+00 | TAUTOLOGY-FAMILY |
| sealed gluing | product whole histories add closed-exchange coefficients | gluing is exact for arbitrary eta values | gap=2.1e-17 | CONSISTENCY-NOT-SELECTION |
| non-divisibility threshold | select smallest eta with CMI >= epsilon | the selected eta moves with the unsupplied threshold epsilon | eta_0p02=0.2022, eta_0p10=0.4718 | BRANCH-B-THRESHOLD |
| self-induced memory equation | solve eta = lambda tanh(eta) | nonzero solutions exist only after a coupling lambda is supplied | eta_l1p5=1.2880, eta_l2p5=2.4640 | BRANCH-B-COUPLING |
| regularized memory action | maximize CMI(eta)-alpha eta^2 | interior optima exist but drift with the regularization coefficient | eta_a0p02=2.2924, eta_a0p10=1.4436 | BRANCH-B-COEFFICIENT |
| quantized holonomy unit | restrict eta to integer multiples of q0 | quantization leaves many possibilities unless q0 and level are supplied | count_q0p10=10, count_q0p25=4 | BRANCH-B-UNIT |
| normalized exchange bracket | fix only eta/abs(eta) as in onset-renormalized universality | same normalized bracket can have different future memory | pair_gap=0.0e+00, future_gap=0.420000 | DIRECTION-NOT-AMPLITUDE |
| h-field equation verdict | test all v1-v5-inspired invariant field-equation candidates | every candidate is vacuum, tautological, coefficient-dependent, or family-valued | h_G not selected | FINITE-NO-GO |

The decisive numbers are:

```text
eta_a = 3.316471087051321e-01
eta_b = 9.504793805965235e-01
pairwise_shadow_gap = 0.000000000000000e+00
future_memory_gap = 4.200000000000000e-01
source_a = 3.200000000000000e-01
source_b = 7.400000000000000e-01
self_identity_gap_a = 5.551115123125783e-17
self_identity_gap_b = 0.000000000000000e+00
product_gluing_gap = 2.081668171172169e-17
threshold_eta_0p02 = 2.022000000000000e-01
threshold_eta_0p10 = 4.718000000000000e-01
landau_eta_lambda_1p5 = 1.288000000000000e+00
landau_eta_lambda_2p5 = 2.464000000000000e+00
regularized_eta_alpha_0p02 = 2.292400000000000e+00
regularized_eta_alpha_0p10 = 1.443600000000000e+00
quantized_count_q0_0p10 = 1.000000000000000e+01
quantized_count_q0_0p25 = 4.000000000000000e+00
```

The finite verdict is:

```text
the current invariant response equations do not determine h_G;
source-free equations select vacuum;
self-source equations are tautologies;
nonzero equations require supplied thresholds, couplings, units, or sources;
therefore h_G is still selected only by the cofinal whole-history ISP law.
```

## 66. Overlap/sheaf composition campaign

The strongest remaining Einstein-style structural principle is not product
gluing. Product gluing only says that disjoint sealed histories compose. A
general local law must also pass nontrivial overlap:

```text
local sealed diamonds must be restrictions of one coherent whole-history law;
the result must not depend on the chosen diamond cover.
```

This is a sheaf condition for whole-history laws. It is necessary. The campaign
asks whether it also selects `h_G`.

The finite answer is no.

First take two overlapping three-history diamonds:

```text
D_1 = ABC,
D_2 = BCD,
D_1 cap D_2 = BC.
```

For arbitrary local coefficients `eta_1,eta_2`, the global law

```text
P(a,b,c,d)
proportional to exp(eta_1 abc + eta_2 bcd)
```

restricts exactly to the two local closed-history laws. The common overlap is
uniform in both restrictions. Thus path-overlap sheaf consistency admits
arbitrary local coefficients. If covariance is added by setting
`eta_1=eta_2`, a one-parameter family remains.

Next take a loop cover of four overlapping three-history diamonds:

```text
ABC, BCD, CDA, DAB.
```

A global Fourier/RN law of the form

```text
P(a,b,c,d)
=
1/16 [1 + theta(abc+bcd+cda+dab) + q abcd]
```

has the same local triple law on every face:

```text
P_D(local triple) = 1/8 [1 + theta(local triple product)].
```

Positivity constrains `theta`, but it does not select it. For a fixed nonzero
`theta`, the four-history coefficient `q` can still vary over an interval.
Therefore even a nontrivial loop sheaf has two failures:

- same overlap-compatible local diamond laws do not select the local
  coefficient `theta`;
- even after local laws are fixed, they do not determine the global
  four-history holonomy `q`.

Maximum entropy can select `q` after `theta` is supplied, but it does not select
`theta`. Maximizing entropy over both returns the divisible vacuum.

Thus overlap/sheaf composition is a necessary consistency principle, not the
cofinal law. It improves the ontology by saying which local data can be glued,
but it does not choose the glued process.

The missing law is therefore not:

```text
product gluing;
overlap gluing;
sheaf compatibility;
maximum-entropy extension of supplied local laws.
```

It is still:

```text
the whole-process rule selecting the projective global h_G field,
including local closed-history coefficients and hidden higher overlap
holonomies.
```

## 67. Overlap/sheaf composition diagnostic

The diagnostic script is:

```text
code/v6_p4ad_overlap_sheaf_campaign.py
```

It tests path overlaps, isomorphic local diamonds, loop covers, hidden global
holonomy, maximum-entropy extension, and global entropy.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| path-overlap sheaf gluing | two triples ABC and BCD share BC | a global whole-history law restricts to arbitrary local eta values | left=0.0e+00, right=2.8e-17, overlap=2.8e-17 | CONSISTENT-FAMILY |
| isomorphic local diamonds | force the same eta on each path diamond | same-eta covariance still leaves a one-parameter family | overlap_gap=0.0e+00, future_gap=0.420000 | COVARIANT-FAMILY |
| loop-cover existence | four overlapping triples around a 4-history loop | positivity restricts theta but leaves many nonzero choices | count=333, theta_range=[0.001,0.333] | CONSTRAINS-NOT-SELECTS |
| same local sheaf, different global laws | hold every triple restriction fixed and vary four-body q | local diamonds agree exactly while hidden global holonomy changes | local_gap=1.4e-17, q_gap=0.460000, minP=0.014375 | REFUTES-LOCAL-SHEAF-COMPLETENESS |
| maximum-entropy extension | choose q after local theta is supplied | max entropy can pick hidden q but not the local coefficient theta | theta=0.180, q_star=0.008880, q_gap=5.2e-17 | EXTENSION-NOT-LAW |
| global entropy over the sheaf family | maximize entropy over theta and q | global max entropy returns the divisible vacuum | theta=0.000, q=0.000 | FAILS-NONDIV |
| overlap/sheaf verdict | path covers + loop covers + positivity + extension | overlap consistency is necessary, but it does not select h_G | needs whole-process law | FINITE-NO-GO |

The decisive numbers are:

```text
eta_left = 3.316471087051321e-01
eta_right = 9.504793805965235e-01
path_left_gap = 0.000000000000000e+00
path_right_gap = 2.775557561562891e-17
path_overlap_gap = 2.775557561562891e-17
same_eta_future_gap = 4.200000000000000e-01
cycle_theta = 1.800000000000000e-01
cycle_q_lo = -2.800000000000000e-01
cycle_q_hi = 6.400000000000000e-01
cycle_q_low = -5.000000000000002e-02
cycle_q_high = 4.100000000000000e-01
cycle_local_gap_low = 1.387778780781446e-17
cycle_local_gap_high = 1.387778780781446e-17
hidden_q_gap = 4.600000000000001e-01
cycle_min_probability = 1.437500000000000e-02
admissible_theta_count = 3.330000000000000e+02
admissible_theta_first = 1.000000000000000e-03
admissible_theta_last = 3.330000000000000e-01
max_entropy_q_fixed_theta = 8.879999999999943e-03
max_entropy_global_theta = 0.000000000000000e+00
max_entropy_global_q = 0.000000000000000e+00
```

The finite verdict is:

```text
overlap/sheaf consistency is necessary but not complete;
path covers leave arbitrary coefficients;
loop covers constrain coefficients but still leave a continuum;
fixed local laws can hide distinct global four-history holonomy;
maximum entropy extends supplied local laws but does not choose them;
therefore the global projective h_G field remains selected only by the
whole-history ISP process law.
```

## 68. Further v1-v5 process-law audit

The fuller v1-v5 audit gives a sharper hint than the first pass. It does not
derive `h_G`, but it does identify the only older route that has the right
type.

The useful imports are:

1. **Whole-process discipline.** V1 and V2 insist that the primary stochastic
   objects are whole finite slabs, whole endpoint kernels, or declared division
   events. Products of partial kernels are physical only when a record/division
   event is supplied. This confirms that `P_G^{hist}` must be a whole-history
   law, not a Markovized composition of local shadows.
2. **Rule-selection no-go.** V1 proves that local finite-deformation
   admissibility does not select a unique microscopic rule. Only
   onset-renormalized bond-centered exchange content survives. This is the old
   version of the current `h_G` coefficient problem.
3. **Same-law pressure calculus.** V3 Papers 30-31 introduce the most relevant
   idea: missing actual values should be rewritten as derivatives of a finite
   same-law pressure
   ```text
   Psi_V(s)=log E_act exp(s V).
   ```
   Source parameters are probes, not new laws. Physical values are derivatives
   at `s=0` under the actual law. This is Barandes-aligned and directly
   suggests how to test `h_G`: closed-history coefficients should be same-law
   response values of the actual whole-history law, not externally assigned
   couplings.
4. **Actual-law value gaps.** V3 Papers 25-27 repeatedly prove that formal
   atoms, Mobius inversion, reflection positivity, finite worksheets, and
   closed scalar ledgers do not populate actual cofinal values. What is missing
   is cofinal same-law density/ratio/mixed-amplitude information. This is
   exactly the present gap for `P_G^{hist}`.
5. **Finite value generator.** V4 Paper 23 already states the correct source
   philosophy:
   ```text
   values are generated by a law over finite histories,
   not supplied as free table entries.
   ```
   Its generator has the form:
   ```text
   Z = sum_history multiplicity * exp(action).
   ```
   This is the finite ancestor of the current closed-exchange whole-history
   RN/Gibbs schema. But V4 also records that the intrinsic G2/G3 packets are
   physically open, while calibrated G1 closes only externally.
6. **Finite calibration bridge.** V4 Paper 24 proves rigidity of a finite
   calibration functor once the functor and anchor records are supplied. This
   is useful for comparing faces of the law, but it does not select the
   underlying whole-history action.
7. **Division-event renewal law.** V5's non-Markovian gravitational follow-up
   gives the one concrete mechanism that really looks like a process law:
   division events form a renewal/reset process, and the memory kernel is
   derived from the waiting-time law. A self-consistency condition can pin the
   record time to a stabilization time up to order-one ambiguity. This suggests
   that `h_G` might ultimately be fixed by a division-event/record-commitment
   law, not by static sheaf consistency.
8. **Protected hidden global records.** V5's QEC/topological/entanglement
   papers normalize the hidden-global-holonomy lesson: local records can be
   actual while global logical or holonomy records remain protected. This
   predicts the loop-cover `q` ambiguity rather than resolving it.

The strongest hint is therefore:

```text
P_G^{hist} should be a cofinal same-law finite pressure / finite value
generator over complete closed-exchange histories.
```

But the audit also prevents overclaiming. A same-law pressure is only a
re-expression unless the actual law is supplied:

```text
Psi_V(s)=log E_{P_G^{hist}} exp(sV)
```

does not derive `P_G^{hist}`. It differentiates it. Likewise, a finite value
generator:

```text
Z_G = sum exp(A_G)
```

does not close branch A until the action `A_G`, the multiplicity, the history
space, and the division/record commitment law are fixed intrinsically.

Thus the best next theorem target imported from v1-v5 is not another
geometric consistency condition. It is:

```text
Cofinal same-law pressure theorem:
the actual indivisible record process supplies a unique projective finite
pressure whose closed-exchange derivatives are h_G.
```

Equivalently, a positive theorem must prove one of the following:

```text
1. a renewal/division-event commitment law that fixes the waiting statistics
   and hence the closed-history coefficients;
2. a same-law Ward/Stein/source-neutrality/curvature theorem that fixes or
   bounds all closed-holonomy responses;
3. a cofinal actual density/ratio table for complete history cylinders;
4. a finite value-generator action whose coefficients are derived from
   same-record data before the query.
```

The parity and loop-cover diagnostics are now the first tests for any such
theorem. It must say why `eta` and hidden `q` take their values. If it merely
reconstructs them after they are supplied, it is not the law.

## 69. Same-law pressure and division-commitment campaign

The v1-v5 audit points to the most promising remaining route:

```text
same-law pressure + division-event commitment.
```

This route is different from the failed structural selectors. It does not try
to select `h_G` from shadows, gluing, entropy, or local response equations. It
tries to make `h_G` the output of a record-commitment process:

```text
complete history law
-> same-law pressure Psi
-> closed-holonomy derivatives h_G
```

or, dynamically:

```text
record distinguishability growth
-> division/commitment waiting law
-> retained closed-history memory
-> h_G.
```

In the parity model, the same-law pressure is:

```text
Psi_eta(s)=log E_eta exp(sH)
          =log cosh(eta+s)-log cosh(eta),
```

with:

```text
Psi_eta'(0)=tanh(eta).
```

This reconstructs `eta` once the law is supplied:

```text
eta=atanh(Psi_eta'(0)).
```

But this is still only a readout. The real test is whether a division-event
commitment law can select `eta`.

The finite campaign gives the route its best chance. Suppose a division event
commits a record when accumulated distinguishability reaches a fixed unit, and
suppose retained memory over a window is the probability that no division has
intervened. For a Poisson renewal law with effective commitment ratio `r`, the
minimal self-consistency equation is:

```text
eta = atanh(exp(-r eta)).
```

This does select a nonzero `eta` for fixed `r`. In the finite diagnostic,
`r=1` gives:

```text
eta = 0.609390,
theta = tanh(eta) = 0.543698,
tau = 1/eta = 1.640985,
information at tau = 1.
```

That is the first real positive sign in this direction. It says that a
record-commitment law can, in principle, turn the parity coefficient into a
self-consistent division scale rather than an externally supplied number.

But the same diagnostic immediately exposes the remaining gates.

- If the waiting time `tau` is supplied, `eta` is selected, but that is branch
  B unless `tau` is derived.
- Two renewal laws with the same mean division time, Poisson and deterministic,
  give different `eta`. Thus division density is not enough; the full waiting
  law matters.
- A likelihood-zero commitment threshold can be canonical while the
  information-growth scale remains free.
- The self-consistent equation selects a value only after the dimensionless
  ratio `r` is fixed.
- Changing the renewal shape changes the selected `eta`.

So the route is not closed, but it is the right kind of open. The missing
object has been reduced from a generic process law to a sharper theorem:

```text
derive the intrinsic division-event commitment law:
  waiting-law shape,
  dimensionless commitment scale,
  information-growth functional,
  and renewal/reset rule.
```

If that theorem is proved, the same-law pressure route can select `h_G` and
hence `P_G^{hist}`. If those quantities are supplied, the construction is
branch B with an ISP-compatible renewal law.

## 70. Same-law pressure and division-commitment diagnostic

The diagnostic script is:

```text
code/v6_p4ae_same_law_pressure_division_commitment.py
```

It tests pressure readout, supplied renewal laws, waiting-shape dependence,
likelihood-zero commitment, self-consistency, and commitment-scale dependence.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| same-law pressure identity | Psi_eta(s)=log E_eta exp(sH) | pressure derivatives reconstruct supplied eta but do not select it | meanA=0.320000, meanB=0.740000, recon=5.6e-17 | READOUT-NOT-SELECTION |
| pressure curvature | compare susceptibilities at two eta values | finite curvature exists for both laws but does not choose between them | curvA=0.897600, curvB=0.452400 | BOUND-NOT-LAW |
| supplied renewal waiting time | Poisson no-division survival over the same window | eta is selected only after tau is supplied | eta_tau1=0.811324, eta_tau2=1.100664 | BRANCH-B-TAU |
| same mean, different waiting law | Poisson versus deterministic divisions with same mean tau | the full waiting-law shape matters, not just division density | eta_poisson=0.811324, eta_det=0.693147, gap=0.118177 | BRANCH-B-PSI |
| likelihood-zero commitment | commit at canonical likelihood threshold with different growth rates | the threshold can be canonical while the information-growth scale remains free | eta_g1=0.385968, eta_g4=0.136171, gap=0.249798 | SCALE-STILL-FREE |
| self-consistent commitment | solve eta=atanh(exp(-r eta)) | a nonzero eta is selected for fixed dimensionless r | r1_eta=0.609390, theta=0.543698, info_tau=1.000000 | PASS-CONDITIONAL |
| commitment scale attack | change only the dimensionless commitment ratio r | the selected eta moves, so r must be intrinsic | eta_r1=0.609390, eta_r2=0.440700, gap=0.168690 | BRANCH-B-SCALE |
| commitment shape attack | Poisson versus deterministic self-commitment | the selected eta moves when the division waiting-law class changes | eta_poisson=0.609390, eta_det=0.521295, gap=0.088095 | BRANCH-B-SHAPE |
| division-law verdict | same-law pressure + renewal + likelihood + self-consistency | this is the right law-shape, but closure requires intrinsic r and waiting law | P_hist closed only if division law is derived | CONDITIONAL-ONLY |

The decisive numbers are:

```text
eta_a = 3.316471087051321e-01
eta_b = 9.504793805965235e-01
pressure_mean_a = 3.200000000000000e-01
pressure_mean_b = 7.400000000000000e-01
pressure_curvature_a = 8.976000000000001e-01
pressure_curvature_b = 4.524000000000000e-01
pressure_reconstruction_gap = 5.551115123125783e-17
window = 4.000000000000000e-01
tau_a = 1.000000000000000e+00
tau_b = 1.800000000000000e+00
eta_tau_a = 8.113240919944404e-01
eta_tau_b = 1.100663995054014e+00
eta_poisson_same_mean = 8.113240919944404e-01
eta_deterministic_same_mean = 6.931471805599453e-01
same_mean_waiting_shape_gap = 1.181769114344952e-01
eta_growth_1 = 3.859684164526524e-01
eta_growth_4 = 1.361707344559158e-01
growth_scale_gap = 2.497976819967365e-01
eta_fixed_point_r1 = 6.093900000000000e-01
eta_fixed_point_r2 = 4.407000000000000e-01
fixed_point_scale_gap = 1.686900000000000e-01
eta_fixed_point_det_r1 = 5.212950000000000e-01
eta_fixed_point_det_r2 = 3.374100000000000e-01
fixed_point_shape_gap = 8.809500000000003e-02
theta_fixed_point_r1 = 5.436975616587407e-01
tau_fixed_point_r1 = 1.640985247542625e+00
info_at_tau_r1 = 1.000000000000000e+00
```

The finite verdict is:

```text
same-law pressure is the correct readout technology;
division-event commitment is the first route that conditionally selects eta;
but the waiting-law shape and dimensionless commitment scale remain unsourced;
therefore this is the leading branch-A theorem target, not closure.
```

## 71. Intrinsic division-event commitment law

The preceding campaign left two apparent free choices:

```text
waiting-law shape;
dimensionless commitment scale r.
```

The Einstein move is to remove the external clock. A sealed record diamond has
no primitive waiting time until a record process supplies one. What it does
have intrinsically is additive RN/KL evidence. Let:

```text
I >= 0
```

be the accumulated sealed record evidence along an eventless collar. This is
not a generic monotone score. It is the RN/KL action measured in natural log
units, so it obeys the chain rule under sealed gluing:

```text
I(D1 glued D2) = I(D1) + I(D2).
```

Let `S(I)` be the probability that no division event has occurred after
evidence `I`. Eventless gluing demands:

```text
S(I+J)=S(I)S(J),     S(0)=1,     0<S(I)<=1.
```

With continuity, this forces:

```text
S(I)=exp(-lambda I).
```

That derives the exponential/Poisson shape in the intrinsic clock. The
remaining coefficient `lambda` is killed by exact RN self-accounting. The
eventless collar is supposed to contain no hidden action besides the evidence
it carries. Therefore:

```text
-log S(I) = I.
```

Thus:

```text
lambda = 1,
S(I)=exp(-I),
P(division by evidence I)=1-exp(-I).
```

Equivalently, in any external parameter `t`, the division process is an
inhomogeneous Poisson process with cumulative intensity:

```text
I(t).
```

This is not a supplied waiting-time model. The waiting law in `t` changes when
the physical evidence-growth functional changes. The intrinsic law is fixed in
RN/KL evidence time.

This also fixes the commitment scale. A linear rescaling `I -> cI` preserves
additivity, but it changes the RN action:

```text
-log S(I)=cI.
```

For `c != 1`, the eventless collar has a surplus or deficit action
`(c-1)I` that is not carried by any sealed record evidence. That is exactly a
silent seam. Nonlinear regraduations are worse: they violate the chain rule
itself. Therefore the dimensionless commitment ratio is not free:

```text
r=1.
```

Now apply the law to the closed-holonomy history family. Let:

```text
P_h(omega)=U(omega) exp(<h,chi(omega)> - psi(h)).
```

The complete closed-history ledger `chi` is the primitive oriented cochain
ledger. Its coefficient `h_j` is the RN action of one primitive oriented
closed-history mode. Division commitment says:

```text
retained same-law memory of mode j
=
probability of no division through evidence h_j.
```

In coordinates:

```text
partial_j psi(h) = exp(-h_j)
```

for each positive primitive oriented mode. This is the finite intrinsic
division-event commitment law.

For the one-mode parity family:

```text
P_eta(H)=U(H) exp(eta H - log cosh eta),
partial_eta psi = tanh eta.
```

The law becomes:

```text
tanh eta = exp(-eta).
```

The left side is the retained closed-holonomy memory; the right side is the
no-division survival through the same RN cochain action. The equation has one
positive solution because:

```text
d/deta [tanh eta - exp(-eta)]
= sech^2 eta + exp(-eta) > 0.
```

The selected coefficient is:

```text
eta_* = 0.6093778634360061,
theta_* = tanh(eta_*) = exp(-eta_*) = 0.5436890126920763.
```

For a complete finite ledger, the same law is the Euler equation of a strictly
convex commitment potential:

```text
Phi(h)=psi(h)+sum_j exp(-h_j),
partial_j Phi(h)=partial_j psi(h)-exp(-h_j).
```

Since `psi` is convex and `sum_j exp(-h_j)` has positive diagonal curvature,
`Phi` is strictly convex on the primitive ledger directions. Therefore any
critical point is isolated and unique. In the finite complete-ledger test with
primitive statistics:

```text
x, y, xy,
```

the solution is:

```text
h=(0.495053,0.495053,0.495053),
```

with positive curvature margin. Thus the law is not merely a scalar trick; it
works in a coupled complete-history ledger.

The dangerous normalization attack is the two-sided log-odds attack. In the
parity family:

```text
log P(+)/P(-)=2 eta.
```

If one incorrectly treats the full two-sided odds as one primitive commitment
unit, the equation becomes:

```text
tanh eta = exp(-2 eta),
```

and gives a different value:

```text
eta=0.4406867935097715.
```

That is rejected by the cochain normalization. The primitive ledger coefficient
is the oriented half-log action `eta`; the full odds compare two opposite
oriented traversals and therefore count two primitive units. Using it as a
single commitment unit double-counts the RN action and reintroduces a branch-B
scale.

So the intrinsic division-event commitment law is:

```text
Evidence clock:
  I = additive sealed RN/KL record evidence.

Eventless survival:
  S(I)=exp(-I).

Division probability:
  P_D(I)=1-exp(-I).

Closed-holonomy fixed point:
  grad psi_G(h_G)=exp(-h_G)
  on the complete primitive oriented closed-history ledger.

Whole-history law:
  P_G^{hist}(omega)
  =
  U_G(omega) exp(<h_G,chi_G(omega)> - psi_G(h_G)),
  with h_G the unique solution of the commitment fixed point.
```

This is the first place where the waiting shape and the scale are both fixed
from sealed record facts rather than supplied.

Two caveats remain, but they are no longer the old free-parameter caveats.

1. The primitive closed-history ledger must be complete and canonically
   oriented. Earlier readout-completeness sections give finite zero-kernel
   tests for such ledgers; the cofinal continuum theorem must preserve that
   completeness.
2. The evidence functional `I` must be the actual RN/KL evidence of the sealed
   record process. If a generic monotone score is used instead, the proof
   collapses. This is not optional terminology: the chain rule and
   self-accounting require the RN/KL clock.

Under those two already-named structural gates, the division-event commitment
law is no longer a shadow. It is the missing law:

```text
division is Poisson in intrinsic RN/KL evidence,
and closed-history memory equals no-division survival through its own
cochain action.
```

## 72. Intrinsic division-event commitment diagnostic

The diagnostic script is:

```text
code/v6_p4af_intrinsic_division_commitment_law.py
```

It tests sealed gluing, scale self-accounting, clock regraduations, scalar
selection, vector/coupled selection, convex isolation, and the full-odds
normalization attack.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| eventless gluing | S(I+J)=S(I)S(J) in additive RN/KL evidence | exponential survival glues exactly; non-exponential waiting shapes do not | exp=0.0e+00, linear=0.113, weibull=0.203 | DERIVES-EXPONENTIAL-SHAPE |
| scale self-accounting | -log S(I) must equal the sealed record evidence I | lambda=1 is the only exponential rate with no surplus/deficit RN action | lam.5=0.700, lam1=0.0e+00, lam2=1.400 | FIXES-r=1 |
| clock regraduation attack | replace I by f(I) | nonlinear clocks violate sealed additivity; linear rescalings violate self-accounting unless c=1 | nonlinear_gap=0.607, c2_mismatch=1.400 | REJECTS-HIDDEN-CLOCK |
| scalar commitment law | retained parity memory equals no-division survival through its own RN cochain action | tanh(eta)=exp(-eta) has one positive root | eta=0.609377863, theta=0.543689013, residual=2.2e-16 | SELECTS-h |
| scalar uniqueness | d/deta[tanh(eta)-exp(-eta)] is positive | the scalar root cannot bifurcate or form a branch family | min_derivative_sample=0.000048 | UNIQUE |
| scale-family refutation | solve tanh(eta)=exp(-lambda eta) | other lambda values select other eta, but those lambda values already fail RN self-accounting | eta_lam.5=0.807052, eta_lam2=0.440687 | REJECTS-BRANCH-B-SCALE |
| independent ledger | minimize psi(h)+sum exp(-h_j) for two primitive modes | the vector law decouples and selects the same intrinsic scalar root per mode | h=(0.609378,0.609378), residual=8.7e-13 | PASS |
| complete coupled ledger | solve grad psi(h)=exp(-h) for x,y,xy closed-history statistics | strict convex commitment potential selects a single coupled h vector | h=(0.495053,0.495053,0.495053), residual=8.6e-14 | PASS-COUPLED |
| convex isolation | finite second differences of psi+sum exp(-h_j) | positive curvature around the coupled solution gives an isolated selector | min_curv=1.238001, value=2.273988 | ISOLATED |
| full-odds normalization attack | use two-sided log odds 2 eta as one commitment unit | it moves the root and double-counts one primitive oriented cochain action | eta_2unit=0.440687, gap=0.168691, surplus=0.609378 | REJECTED-BY-COCHAIN-UNIT |
| division-law verdict | RN/KL clock + sealed gluing + exact self-accounting + same-law holonomy fixed point | the intrinsic division-event commitment law is S(I)=exp(-I) and grad psi(h)=exp(-h) | eta_star=0.609377863 | FINITE-CLOSURE |

The decisive numbers are:

```text
eta_star = 6.093778634360061e-01
theta_star = 5.436890126920763e-01
eta_lambda_half = 8.070518565778841e-01
eta_lambda_two = 4.406867935097715e-01
h_independent = (6.093778634364979e-01, 6.093778634364979e-01)
h_complete = (4.950532643315756e-01, 4.950532643315756e-01, 4.950532643315756e-01)
complete_residual = 8.614872834998366e-14
min_curv_complete = 1.238001345882367e+00
```

The finite verdict is:

```text
the old waiting-law shape freedom is killed by sealed gluing in RN/KL evidence;
the old r freedom is killed by exact RN self-accounting;
the closed-history coefficient is selected by retained memory =
no-division survival through its own cochain action;
therefore P_G^{hist} is fixed by the complete closed-holonomy Gibbs law plus
the intrinsic division-event commitment fixed point.
```

This does not erase the need for cofinal completeness of the primitive ledger.
It does remove the particular free renewal model that blocked the previous
section.

## 73. Cofinal primitive-ledger commitment theorem

The remaining word is **cofinal**. The commitment law must survive refinement
without turning a subdivision convention into new physics.

The mistake to avoid is simple. If one primitive RN/KL cochain action `H` is
split into `m` coordinate pieces and each piece is incorrectly treated as a
new independent commitment unit, the scalar equation becomes:

```text
tanh H = exp(-H/m).
```

The selected `H` then drifts with `m`. That is not a physical refinement. It
is duplicate bookkeeping. A serial subdivision of one eventless collar has
evidence pieces:

```text
I_1,...,I_m,
sum_k I_k = I.
```

The intrinsic survival law gives:

```text
prod_k exp(-I_k)=exp(-sum_k I_k)=exp(-I).
```

So the primitive commitment unit is the total projective RN/KL evidence of the
same oriented closed-history mode, not the number of coordinate intervals used
to describe it.

This fixes the cofinal ledger definition.

```text
Primitive oriented RN/KL ledger at level n
=
minimal projective quotient of all future-relevant closed-history RN/KL
contrasts.
```

More explicitly:

1. Start with all finite closed-history RN/KL contrasts at level `n`.
2. Quotient duplicate coordinates whose covariance/readout rank is redundant.
3. Keep one oriented representative for each positive primitive mode.
4. Split a refinement into a horizontal lift of old primitive modes plus
   vertical modes.
5. A vertical mode is silent only when all intrinsic future-relevant readouts
   vanish cofinally; otherwise it is a new primitive ledger entry.

Thus a refinement cannot multiply a commitment unit by subdividing it. It can
only:

```text
preserve the old total RN/KL evidence;
add a new independent vertical RN/KL mode;
or add a cofinally silent vertical mode.
```

This is exactly the finite readout-completeness theorem in projective form.
Duplicate coordinates have nontrivial kernel and are quotiented away. Genuine
vertical contrasts have nonzero readout and are retained.

Now define the finite commitment potential at level `n` on this primitive
quotient ledger:

```text
Phi_n(h)=psi_n(h)+sum_j exp(-h_j),
```

where:

```text
psi_n(h)=log E_{U_n} exp(<h,chi_n>).
```

Here `chi_n` is the complete primitive oriented closed-history ledger, not an
arbitrary coordinate refinement of it. The selected coefficient is:

```text
h_n = argmin Phi_n(h),
```

equivalently:

```text
grad psi_n(h_n)=exp(-h_n).
```

Finite uniqueness is immediate. `psi_n` is convex as a log-partition
function. The term:

```text
sum_j exp(-h_j)
```

has positive diagonal curvature on the primitive positive-mode coordinates and
is coercive toward `h_j -> -infinity`, while `psi_n` controls the positive
tail in every non-silent primitive direction. Therefore `Phi_n` is strictly
convex on the primitive quotient directions and has at most one critical
point. Under the finite ledger hypotheses used in the diagnostics, it has one.

The cofinal theorem is the standard convex convergence theorem applied to the
sealed process.

**Cofinal primitive-ledger commitment theorem.** Let:

```text
(G_n, U_n, chi_n, psi_n)
```

be a projective sequence of sealed finite record diamonds such that:

```text
1. the quotient maps are count-reference preserving;
2. the ledgers chi_n are complete primitive oriented RN/KL ledgers;
3. horizontal lifts preserve total RN/KL evidence by the chain rule;
4. every nonzero vertical future-relevant readout is retained, and silent
   vertical readouts vanish cofinally;
5. psi_n Gamma-converges on every finite cylinder of primitive modes to
   psi_infty;
6. the commitment potentials Phi_n=psi_n+sum exp(-h_j) have a uniform local
   convex isolation margin around their minimizers.
```

Then the selected finite coefficients:

```text
h_n = argmin Phi_n
```

are projectively stable under silent refinements and converge on every finite
cylinder to the unique cofinal minimizer:

```text
h_infty = argmin Phi_infty,
Phi_infty(h)=psi_infty(h)+sum_j exp(-h_j).
```

Equivalently:

```text
grad psi_infty(h_infty)=exp(-h_infty).
```

Proof sketch. Serial subdivision invariance follows exactly from:

```text
exp(-I_1)...exp(-I_m)=exp(-(I_1+...+I_m)).
```

Duplicate coordinates are killed by the primitive quotient because they add no
rank to the complete readout/covariance map. Non-silent vertical contrasts are
not quotiented away; they become new coordinates of `chi_n`. On every finite
cylinder, `Phi_n` Gamma-converges to `Phi_infty` because `psi_n`
Gamma-converges and the commitment term is continuous in the primitive RN/KL
coordinates. Uniform convex isolation prevents minimizer wandering. Hence
the projective minimizers converge.

This is the cofinal closure that the previous section needed. The continuum
object is not an arbitrary limit of coordinate ledgers. It is the limit of the
primitive projective RN/KL quotient ledgers.

The theorem also says exactly what would falsify the construction. A purported
refinement is not admissible if:

```text
it treats one serial subdivision as several primitive commitment units;
it drops a nonzero vertical future-relevant RN/KL contrast;
it lacks a complete cycle/history readout basis;
or its log-partitions fail projective convex convergence.
```

Those are not open parameters. They are violations of the sealed-process
definition.

## 74. Cofinal primitive-ledger commitment diagnostic

The diagnostic script is:

```text
code/v6_p4ag_cofinal_primitive_ledger_commitment.py
```

It tests serial survival, the coordinate-split attack, duplicate-coordinate
quotienting, horizontal lift stability, retained vertical modes, minimizer
convergence, and vanishing coupled refinements.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| serial refinement | split total RN/KL evidence into many eventless collar pieces | survival products are partition-independent: prod exp(-I_k)=exp(-sum I_k) | max_gap=1.9e-16 | PASS-COFINAL-SURVIVAL |
| wrong per-cell commitment | treat m subdivisions of one primitive mode as m independent commitment units | selected coarse h drifts with m, so this is an inadmissible duplicate ledger | m1=0.609378; m2=0.807052; m4=1.028442; m8=1.268445; span=0.659067 | REFUTES-COORDINATE-SPLIT |
| primitive quotient | compare duplicate coordinate stats with independent stats | duplicate ledgers have covariance rank one and collapse to one primitive cochain | dup_rank=1, independent_rank=2 | DERIVES-MINIMAL-LEDGER |
| neutral horizontal lift | refine without adding a future-relevant vertical contrast | the old primitive coefficient is lifted unchanged | h_lift=0.609377863, theta=0.543689013 | PASS-PROJECTIVE |
| retained vertical mode | add an independent future-relevant vertical RN/KL contrast | the vertical contrast becomes a new primitive mode; omitting it leaves a future gap | h_vertical=0.609377863, hidden_future_gap=0.543689013 | RETAIN-OR-NOT-SILENT |
| Gamma convergence | perturb psi_n=psi+eps_n h^2 with eps_n->0 | strict-convex commitment minimizers converge to the cofinal root | gap_eps1/4=0.164101, gap_eps1/128=0.007505 | PASS-MINIMIZER-CONVERGENCE |
| vanishing coupled refinement | add a cofinally vanishing coupled vertical correction | horizontal drift vanishes with the coupling strength | gap_eps1/4=0.184420, gap_eps1/128=0.009274 | PASS-COUPLED-COFINAL |
| cofinal ledger verdict | projective quotient ledger + RN/KL chain rule + strict convex commitment | finite selected h is stable under neutral refinements and converges under controlled cofinal refinements | eta=0.609377863 | COFINAL-CLOSURE |

The decisive numbers are:

```text
eta = 6.093778634360061e-01
theta = 5.436890126920763e-01
partition_max_gap = 1.942890293094024e-16
wrong_split_span = 6.590667434207642e-01
duplicate_rank = 1
independent_rank = 2
hidden_future_gap = 5.436890126920763e-01
gamma_gap_eps_1_4 = 1.641012086607552e-01
gamma_gap_eps_1_128 = 7.505336892962289e-03
coupled_gap_eps_1_4 = 1.844202840169632e-01
coupled_gap_eps_1_128 = 9.273511628507869e-03
```

The finite verdict is:

```text
cofinal commitment is stable only on the primitive quotient ledger;
serial RN/KL subdivisions preserve total survival exactly;
coordinate duplicate ledgers are rejected by rank;
non-silent vertical modes are retained as new primitive modes;
and controlled convex projective refinements converge to the same cofinal
commitment law.
```

## 75. Cover-independence theorem for the commitment law

The next Einstein test is cover independence. The same sealed process should
not give different `h_G` merely because the diamond is decomposed into
different local patches.

The theorem is true, but only with the right meaning of "same cover." The
commitment law is not invariant under arbitrary linear changes of coordinates
in the readout span. It is invariant under changes of cover that preserve the
primitive oriented RN/KL quotient ledger.

This distinction matters. The commitment potential:

```text
Phi(h)=psi(h)+sum_j exp(-h_j)
```

is separable in primitive commitment units. A primitive unit is an indivisible
oriented RN/KL record contrast, not an arbitrary basis vector of the linear
span. Therefore the admissible cover category is:

```text
objects:
  sealed finite diamond covers with local primitive oriented RN/KL ledgers;

morphisms:
  relabel primitive units;
  identify duplicate overlap units once;
  split serial eventless collars while preserving total RN/KL evidence;
  retain every non-silent vertical mode;
  quotient only cofinally silent vertical modes.
```

Under these morphisms, the primitive quotient ledger is the same object. Then
the log-partition `psi`, the commitment potential `Phi`, and the selected
coefficient `h` are natural.

**Finite cover-independence theorem.** Let two finite sealed diamond covers
`C` and `C'` of the same process glue to the same primitive oriented RN/KL
quotient ledger `chi_G`. Let:

```text
psi_G(h)=log E_U exp(<h,chi_G>)
Phi_G(h)=psi_G(h)+sum_j exp(-h_j).
```

Then both covers select the same physical coefficient:

```text
h_G=argmin Phi_G,
grad psi_G(h_G)=exp(-h_G),
```

up to relabeling of primitive units.

Proof. Permuting local primitive units permutes coordinates of `h`, and
`Phi_G` is symmetric under that permutation. Duplicate overlap units do not
increase the rank of the primitive readout/covariance map; they are identified
before the commitment term is evaluated. Serial subdivisions preserve total
survival because:

```text
prod_k exp(-I_k)=exp(-sum_k I_k).
```

Thus they keep one primitive commitment unit with total action `I`, not many
independent units. Non-silent vertical modes are retained as new primitive
coordinates; silent vertical modes vanish cofinally and do not perturb the
minimizer by the cofinal primitive-ledger theorem. Therefore admissible covers
produce the same primitive quotient ledger and hence the same minimizer.

The theorem also gives the falsifier. If a cover replaces primitive record
contrasts by arbitrary mixtures such as:

```text
u=(x+y)/sqrt(2),
v=(x-y)/sqrt(2),
```

then it has the same linear span as `x,y`, but not the same primitive ledger.
The values of `u` are:

```text
-sqrt(2), 0, sqrt(2),
```

not the two-valued oriented record contrast `{-1,+1}`. Evaluating:

```text
sum_j exp(-h_j)
```

on `u,v` attaches commitment units to mixed coordinates rather than
indivisible record contrasts. The selected effective `x,y` law changes. Thus
full `GL`-basis invariance is false and should be false: it would erase the
distinction between primitive record alternatives and analyst-chosen linear
coordinates.

So the cover principle is:

```text
same physical process
=
same primitive oriented RN/KL quotient ledger,
not merely same readout span.
```

This is the precise sense in which the commitment-selected `P_G^{hist}` is
cover-independent.

## 76. Cover-independence diagnostic

The diagnostic script is:

```text
code/v6_p4ah_cover_independence_commitment.py
```

It tests primitive-unit relabeling, overlap duplication, serial gluing,
vertical refinements, cofinally silent vertical modes, and the mixed-basis
attack.

| target | test | result | value | verdict |
|---|---|---|---:|---|
| permutation cover | swap local primitive ledger order | selected h is natural under primitive-unit relabeling | gap=0.0e+00, residuals=(8.7e-13,8.7e-13) | PASS-COVER |
| overlap duplicate attack | two cover patches both include the same y primitive mode | raw duplicate coordinates double-count y and drift; quotient identifies y once | raw_eff=(0.609378,0.807052,0.609378), quotient=(0.609378,0.609378,0.609378), gap=0.197674 | REFUTES-NAIVE-OVERLAP |
| overlap primitive quotient | rank of duplicate cover ledger versus quotient ledger | same process has rank three; duplicate cover has four coordinates but only three primitive modes | raw_rank=3, quotient_rank=3, residual=3.1e-14 | PASS-QUOTIENT |
| serial cover gluing | split one eventless collar evidence into serial pieces | survival is independent of cover partition | survival_gap=5.6e-17 | PASS-SERIAL |
| serial coordinate-count attack | treat m serial pieces as m primitive commitment units | selected h drifts with cover subdivision, hence the cover is inadmissible | m1=0.609378; m2=0.807052; m4=1.028442; span=0.419064 | REFUTES-PER-CELL-LAW |
| vertical extension | add independent z contrast in a refined cover | z is a new primitive mode; dropping it changes future readout | h=(0.609378,0.609378,0.609378), future_gap=0.543689 | RETAIN-VERTICAL |
| cofinally silent vertical | scale vertical contrast by eps -> 0 | horizontal selected h converges to the old cover value | gap_eps1/4=4.9e-13, gap_eps1/64=4.9e-13 | PASS-SILENT-LIMIT |
| mixed-basis attack | replace primitive x,y by (x+y)/sqrt2 and (x-y)/sqrt2 | same span but different primitive units; component commitment moves the effective x,y law | mixed_xy=(0.932130,0.000000), base=(0.609378,0.609378), gap=0.609378 | REFUTES-GL-INVARIANCE |
| primitive-value check | compare value spectra of primitive and mixed stats | mixed stats are not +/-1 indivisible record contrasts | primitive_values=[-1.0, 1.0], mixed_values=[-1.414213562373095, 0.0, 1.414213562373095] | REJECTS-MIXED-PRIMITIVE |
| cover-independence verdict | admissible cover = same primitive quotient ledger plus retained/non-silent vertical modes | the selected h is cover-independent exactly for admissible covers | h_base=(0.609377863,0.609377863) | FINITE-COVER-THEOREM |

The decisive numbers are:

```text
h_base = (6.093778634364979e-01, 6.093778634364979e-01)
perm_gap = 0.000000000000000e+00
overlap_raw_gap = 1.976739931425593e-01
overlap_rank_raw = 3
overlap_rank_quotient = 3
serial_survival_gap = 5.551115123125783e-17
serial_wrong_span = 4.190641968888045e-01
hidden_vertical_gap = 5.436890126920865e-01
silent_gap_eps_1_4 = 4.917177776064818e-13
silent_gap_eps_1_64 = 4.917177776064818e-13
mixed_effective_xy = (9.321295742034660e-01, 0.000000000000000e+00)
mixed_gap = 6.093778634364979e-01
```

The finite verdict is:

```text
the commitment-selected law is cover-independent for admissible sealed
diamond covers;
admissible means same primitive oriented RN/KL quotient ledger, with overlap
duplicates identified, serial evidence summed, non-silent vertical modes
retained, and cofinally silent modes removed;
arbitrary mixed bases are not admissible primitive ledgers and change the
law.
```

## 77. Status

The finite results are:

```text
Single primitive event:
  closed by complete count-symmetric idempotent holonomy readout plus
  information-geometric saturation.

Born exponent:
  selected inside the two-diamond composition packet from retained linear
  holonomy and screen-weight invariance; the composition premises remain
  load-bearing.

Interference:
  appears only when holonomy is retained and alternatives add before event
  readout.

Observable non-Markovianity:
  appears when retained holonomy is marginalized, but the toy process is not
  yet the full Barandes indivisible-process theorem.

Finite gravity attachment:
  source, amplitude, allowed-change operator, and future stochastic transport
  are all tied to sealed record data in the finite linear packet.

Scalar gravity refinement:
  for count-uniform local sealed collars, L_n=n^2(D-A) converges to the
  continuum allowed-change operator, centered deletion sources converge, and
  K_phi has a stable drift limit.

Causal-screen tensor geometry:
  local count-uniform conductance collars define a symmetric screen tensor G,
  L_n=n^2 B^T C B converges to -div(G grad), and the scalar no-silent-source
  identity 1^T L_n=0 is exact.

Causal-diamond screen stack:
  nested screens with G(r,x,y) support a minimal/no-twist record connection,
  expansion/shear, screen-time holonomy, and a connection Bianchi identity;
  conductance-only closure is refuted by twist freedom.

No-twist transport:
  metric compatibility leaves a G-skew twist, but least eventless record work
  and no oriented silent circulation both select the minimal/no-twist
  connection uniquely; reciprocal null pairs and area/expansion alone do not.

Double-null kinematics:
  sealed count-null axes plus no-twist transport derive Omega_±, theta_±,
  sigma_±, mixed null holonomy, connection Bianchi readouts, and focusing
  scalars; G-only, cross-normalization-only, and source-free completions fail.

Sealed null-work balance:
  closed work balance alone leaves a null-scale family; with intrinsic
  front-dual reciprocity it selects a unique affine pair, but it still does
  not force deletion response to equal focusing source.

Deletion/focusing identity:
  the current primitive binary deletion source is necessarily two-level, while
  generic balanced focusing is many-valued. The best binary fit leaves a large
  residual, and support/norm/projection receipts still do not select the
  focusing source.

Enriched RN deletion:
  promoting the local RN action A_D to the primitive closes the
  deletion/focusing identity and recovers binary support as a readout, but the
  old idempotent constants drift and support-only data cannot reconstruct A_D.

A_D generation law:
  variational smoothing, max entropy, support-only data, and histogram data
  fail to generate the full RN action. A self-consistent feedback fixed point
  selects a many-valued action in the finite packet, but only if the sealed
  drive and feedback coefficients are intrinsic.

T_D classification:
  the feedback-map surrogate is not fundamental. A finite coefficient-family
  no-go gives covariant source-conserving isolated fixed points with different
  A_D, including a same-support pair.

Exchange-cocycle law:
  if the sealed ISP process supplies the ordered transport laws P_AB and P_BA,
  then A_D is uniquely generated as log dP_AB/dP_BA. This removes the feedback
  coefficients and gives exact RN, antisymmetry, eventless, covariance, and
  composition identities.

Transport-law campaign:
  sealed structural constraints below the whole ISP process do not determine
  the ordered transports. Local reversible count-preserving generators still
  form a family, maximum entropy and least action collapse to zero exchange,
  and scalar work summaries do not classify the transport.

Whole-history determination:
  pairwise shadows, fixed endpoint transports, and fixed RN action do not
  determine P_D^{hist}. A retained internal history can change future composition
  while all those shadows remain fixed. Full atom/cylinder probabilities
  determine P_D^{hist} only when the whole process law has been supplied.

Complete closed-holonomy law:
  the missing whole process law is the complete closed-exchange holonomy
  cochain. Once a complete separating ledger is supplied, finite RN/Mobius
  inversion reconstructs P_D^{hist} uniquely, separates Leibniz twins, keeps
  retained non-Markovian memory, composes additively under sealed gluing,
  covaries under relabeling, and survives neutral refinement without silent
  coefficients.

Closed-holonomy field equation:
  Bianchi, gluing, refinement, positivity, and no-silent-history are
  consistency laws, not a selector of one universal h_D. Max entropy and least
  action without source select the vacuum. Hodge/Poisson equations are proper
  field equations once closed periods or sources are physical state data.

Source gluing:
  local source rho_D is the boundary coboundary/divergence of the complete
  global closed-holonomy interface cochain in the finite v6 cell packet.
  Internal seams cancel exactly, glued composites see only external boundary
  mismatch, and arbitrary local source choices either change the global h
  process or violate gluing. This extends the v1-v5 seam/boundary discipline
  rather than claiming that arbitrary continuum source geometry was already
  proved there.

Cellular source conservation:
  in a finite sealed cell complex, vector/tensor source components are the
  cellular divergence of the complete interface h cochain. Internal seams
  cancel for arbitrary glued subcomplexes, scalar source laws are projections
  of the same object, and neutral refinement preserves the coarse source.

Cofinal continuum reconstruction:
  controlled projective complete-h families give convergent source densities,
  convergent allowed-change operators, and exact projective whole-history
  refinement. Coarse shadows alone fail, because zero-coarse fine holonomy can
  hide nonzero source density unless the sealed process supplies
  bounded-energy/no-silent-refinement tightness.

Intrinsic admissible refinement:
  a silent refinement is a count-preserving sealed quotient with equality, or
  cofinal vanishing, in every intrinsic future-relevant readout. The KL/RN
  chain rule detects hidden fiber work, while the cellular coboundary/source
  readout detects zero-coarse fine holonomy. Amplitude or coarse shadow alone
  is too weak.

Readout completeness:
  scalar work values do not classify hidden history or cellular defects.
  Full vertical RN action reconstructs fine history fibers, and
  source/divergence plus a complete independent cycle-period basis reconstruct
  finite interface holonomy. Local face periods are complete only in simply
  connected complexes; holes require homology periods.

Cofinal readout completeness:
  for every connected finite sealed interface graph, reduced incidence/source
  readouts plus a complete cycle-period basis have rank equal to the number of
  interface edges. Thus the finite readout map has zero kernel at every level,
  and projective zero-readout families have no vertical defect in the
  continuum cylinder limit.

Closed-holonomy dynamics:
  the finite response equation R_G h_G=(rho_G,kappa_G) uniquely determines
  interface holonomy from complete source and cycle-period data. Source-only,
  period-only, scalar-work, and least-work-with-unsupplied-periods all have
  twins or erase physical holonomy. The response law is closed; the source
  and period data still need the whole-process law.

Source/period origin:
  once P_G^{hist} is supplied, its RN action reconstructs h_G, and source and
  cycle periods are the exact/cyclic readouts rho_G=B_red h_G and
  kappa_G=C h_G. External rho/kappa assignments are rejected. Neutral
  refinements preserve the readouts, while hidden fine vertical RN data remain
  physical unless retained or cofinally silent.

Whole-history law selection:
  gluing, projectivity, exact RN identities, readout completeness,
  source/period origin, and positive non-divisibility still leave a
  one-parameter family of positive whole-history laws. Entropy selects the
  divisible vacuum, maximum memory runs to a boundary, and scalar selectors
  miss future orientation. Thus P_G^{hist} itself is the remaining
  indivisible process law.

V1-V5 law clue:
  exact finite slabs, exchange defects, projective path kernels, phase as
  stochastic holonomy, and non-Markovian survival all point to a
  closed-exchange whole-history RN/Gibbs law. This closes the schema, but not
  the coefficient field h_G. Maximum caliber, entropy, memory, regularized
  memory, Born-square readout, and onset-renormalized universality do not
  select h_G.

h_G field equation:
  source-free least action selects the divisible vacuum; supplied source
  response is branch B; self-source response is tautological; gluing is
  consistency; non-divisibility thresholds, self-induced memory, regularized
  memory, and quantized holonomy all require unsupplied constants; normalized
  exchange brackets fix direction but not amplitude. Thus no tested invariant
  field equation selects h_G.

Overlap/sheaf composition:
  nontrivial overlap consistency is necessary but not a selector. Path
  overlaps glue arbitrary coefficients exactly; covariance leaves a
  one-parameter same-eta family; loop covers constrain positivity but leave
  many nonzero local coefficients; fixed local triple laws can hide distinct
  global four-history holonomy. Maximum entropy extends supplied local laws
  but does not choose them.

Further v1-v5 audit:
  the older corpus points most strongly to same-law finite pressure and finite
  value-generator technology. This gives the right next target: a cofinal
  actual-law pressure whose derivatives are h_G, or a renewal/division-event
  commitment law that fixes the closed-history coefficients. The corpus does
  not yet supply that pressure, density table, action, or division law.

Same-law pressure / division commitment:
  same-law pressure reconstructs h_G once P_G^{hist} is supplied. A
  self-consistent division-commitment equation can select a nonzero coefficient
  in the parity model, but only after the waiting-law shape and dimensionless
  commitment scale are fixed. This is the strongest current branch-A route,
  not closure.

Intrinsic division-event commitment:
  using additive RN/KL evidence as the sealed eventless clock, eventless gluing
  forces exponential survival and exact RN self-accounting fixes the rate to
  one. The commitment law is S(I)=exp(-I). Closed-history memory must equal
  no-division survival through its own primitive cochain action, giving
  grad psi_G(h_G)=exp(-h_G) on the complete oriented ledger. In the parity
  test this selects eta=0.609377863..., and in the coupled complete-ledger
  test the strict convex potential psi+sum exp(-h_j) gives an isolated
  solution. This removes the previous waiting-shape/r-scale freedom at finite
  level; the next theorem supplies the cofinal primitive-ledger stability.

Cofinal primitive-ledger commitment:
  the primitive oriented RN/KL ledger is the projective quotient of
  future-relevant contrasts, not a coordinate subdivision list. Serial
  refinements preserve total survival exactly, duplicate ledgers are rejected
  by rank, non-silent vertical modes are retained, and controlled convex
  projective refinements Gamma-converge to the cofinal minimizer of
  psi+sum exp(-h_j). Thus the commitment selector is stable cofinally inside
  the sealed-process ontology.

Cover independence:
  the commitment-selected law is invariant under admissible diamond cover
  changes: primitive-unit relabeling, overlap duplicate quotienting, serial
  evidence gluing, retained vertical modes, and cofinally silent vertical
  modes. It is not invariant under arbitrary mixed bases of the same readout
  span, and that failure is the correct falsifier: mixed bases are analyst
  coordinates, not primitive oriented RN/KL record units.
```

The honest remaining target is therefore the full composition law:

```text
sealed diamond sequence
-> retained exchange holonomy
-> linear screen composition
-> quadratic event weights
-> history-dependent record transport
-> deletion-response gravity
-> refinement-stable continuum geometry
-> record connection / tensor curvature identity
-> intrinsic front-dual reciprocity
-> affine/cross-normalized null-front structure
-> focus-binary dynamics or enriched RN deletion action
-> deletion-response/focusing identity
-> reject feedback-map surrogates for A_D
-> sealed exchange-cocycle law A_D = log dP_AB/dP_BA from actual ISP transports
-> derive source/focusing/gravity readouts as projections of the same A_D
-> complete closed-holonomy whole-history law for P_D^{hist}
-> closed-holonomy boundary/source field equation for h_D
-> source gluing as boundary coboundary of neighboring h_D data
-> full tensor source conservation
-> cellular refinement of source conservation
-> cofinal continuum reconstruction / projective tightness
-> intrinsic admissible refinement / no-silent-refinement
-> finite readout-completeness / zero-kernel vertical defects
-> cofinal readout-completeness / homology-complete cycle basis
-> closed-holonomy response dynamics R_G h_G=(rho_G,kappa_G)
-> source/period origin as readouts of P_G^{hist}
-> whole-history law selection no-go for the current structural packet
-> v1-v5 closed-exchange whole-history law schema P_h
-> h_G field-equation no-go for current invariant response candidates
-> overlap/sheaf composition no-go for local-to-global selection
-> v1-v5 same-law pressure / finite value-generator hint
-> same-law pressure / division-commitment conditional selector
-> intrinsic division-event commitment law S(I)=exp(-I)
-> closed-history fixed point grad psi_G(h_G)=exp(-h_G)
-> finite selection of h_G and P_G^{hist}
-> cofinal primitive-ledger quotient and minimizer convergence
-> refinement-stable selection of h_G and P_G^{hist}
-> cover independence under admissible sealed diamond decompositions.
```

This paper establishes thirty-five anchors of that program:

```text
1. the primitive event law;
2. the finite Born exponent selection inside a specific composition packet,
   conditional on linear retained holonomy and invariant screen weight;
3. the finite Barandes-aligned gravity attachment inside a record-transport
   packet.
4. the scalar continuum/refinement limit for count-uniform local sealed
   collars.
5. the causal-screen conductance-tensor gate, together with a falsifier for
   overclaiming full Einstein/Bianchi closure from scalar conductance alone.
6. the causal-diamond screen-stack connection gate, together with a falsifier
   for deriving the connection from conductance tensors alone.
7. the no-twist transport theorem from least eventless record work / no silent
   circulation, together with falsifiers for area-only and null-pair-only
   selection.
8. the double-null kinematic/focusing-readout gate, together with falsifiers
   for G-only null rescaling, cross-normalization-only completion, and
   source-free focusing.
9. the sealed null-work balance gate, which proves that work-only affine
   closure fails, work plus front-dual reciprocity selects a unique affine
   pair, and source-free focusing/deletion matching still fails.
10. the deletion/focusing identity no-go for the current primitive binary
    source law, together with the two remaining branch-A routes: focus-binary
    dynamics or an enriched local RN deletion action.
11. the enriched RN deletion-field route, which closes source/focusing
    identity only by promoting A_D to the primitive, while reopening the
    intrinsic-action and primitive-constant theorems.
12. the A_D generation-law campaign, which rules out variational smoothing,
    max-entropy, support-only, and histogram-only generation in the finite
    packet, and identifies the isolated self-consistent feedback fixed point
    as the best current conditional branch-A candidate.
13. the T_D classification no-go, which proves that the current sealed
    invariants plus fixed-point isolation leave a coefficient family of
    covariant feedback laws, including inequivalent same-support actions.
14. the sealed exchange-cocycle law, which derives A_D without feedback
    coefficients from the ordered ISP transport laws and gives exact RN,
    antisymmetry, eventless, covariance, and product-cocycle receipts.
15. the sealed transport-law no-go, which shows that locality, count
    preservation, detailed balance, stochasticity, maximum entropy, least
    action, and scalar work summaries do not derive the ordered transports;
    the whole indivisible ISP process law is the remaining primitive.
16. the sealed whole-history determination no-go, which shows that pairwise
    shadows, fixed endpoint transports, and fixed RN action do not determine
    P_D^{hist}; retained history can change future composition while all those
    shadows remain fixed, and only the full atom/cylinder process law
    determines the whole history.
17. the complete closed-holonomy whole-history law, which identifies the
    finite ISP process state with the complete RN/Mobius cochain of closed
    exchange-history contrasts; once the complete ledger is supplied, this
    reconstructs P_D^{hist} uniquely, blocks silent future-relevant hidden
    histories, and gives exact gluing, relabeling, and neutral-refinement
    receipts.
18. the closed-holonomy field-equation campaign, which proves that invariant
    consistency laws do not select one universal h_D, while Hodge/Poisson
    least-work equations give unique responses for fixed physical
    source/boundary cochains.
19. the sealed source-gluing law, which derives local source cochains as
    boundary coboundaries of the complete global interface h cochain in the
    finite v6 packet, proves internal seam cancellation and composite boundary
    conservation, and refutes both boundary-summary-only and local-source-knob
    interpretations.
20. the cellular source-conservation law, which upgrades source gluing from a
    chain to a finite cell complex, proving componentwise vector/tensor source
    conservation, scalar projection inheritance, neutral-refinement
    invariance, and the failure of boundary-summary/local-knob alternatives.
21. the cofinal continuum reconstruction gate, which proves positive
    convergence for controlled projective complete-h families, preserves
    non-Markovian whole-history laws under neutral refinement, and refutes
    coarse-shadow-only continuum reconstruction by a zero-coarse hidden-source
    attack.
22. the intrinsic admissible-refinement law, which derives silent refinement
    as count-reference preservation plus equality/cofinal vanishing in all
    intrinsic future-relevant readouts, and proves that KL/L2/coarse-shadow
    conditions alone miss hidden source defects.
23. the finite readout-completeness theorem, which proves that scalar readout
    summaries have Leibniz twins, while full vertical RN action plus
    source/divergence and complete cycle-period readouts separate the tested
    history and cellular vertical defects.
24. the cofinal readout-completeness theorem, which upgrades the cellular
    result to connected finite interface graphs by the rank identity
    `rank(B_red)+beta_1=|E|`, and shows that local face periods must be
    supplemented by homology cycle periods on complexes with holes.
25. the closed-holonomy dynamics theorem, which proves that the complete
    finite response equation uniquely reconstructs h from supplied source and
    cycle-period data, while refuting source-only, period-only, scalar-work,
    and unsupplied-period least-work dynamics.
26. the projective source/period origin theorem, which derives rho and kappa
    from the RN coefficients of P_G^{hist}, rejects external source/period
    reassignment, and proves finite projective naturality for neutral lifts
    while detecting hidden fine vertical RN data.
27. the whole-history law selection no-go, which proves that exact RN
    identities, gluing, projectivity, readout completeness, source/period
    origin, and positive non-divisibility leave a one-parameter family of
    future-distinguishable sealed history laws; therefore, under that
    structural packet alone, P_G^{hist} remains an indivisible process law, not
    a lower shadow.
28. the v1-v5 closed-exchange action campaign, which identifies the strongest
    older-paper clue as the projective closed-holonomy whole-history RN/Gibbs
    schema, proves that this schema exactly represents the finite parity
    history family, and shows that the coefficient field h_G is still not
    selected by maximum caliber, entropy, memory, regularized memory,
    Born-square readout, or onset-renormalized universality.
29. the h_G field-equation campaign, which tests source-free least action,
    supplied source response, self-source identities, sealed gluing,
    non-divisibility thresholds, self-induced memory equations, regularized
    memory actions, quantized holonomy units, and normalized exchange brackets,
    and proves that each is vacuum, tautological, coefficient-dependent,
    source-dependent, threshold-dependent, unit-dependent, or direction-only.
30. the overlap/sheaf composition campaign, which proves that nontrivial
    overlap consistency is necessary but not a selector: path covers glue
    arbitrary coefficients, same-eta covariance leaves a one-parameter family,
    loop covers constrain positivity without selecting theta, and fixed local
    laws can hide distinct global four-history holonomy.
31. the further v1-v5 process-law audit, which identifies the strongest older
    clue as same-law finite pressure / finite value-generator technology:
    closed-history coefficients should be actual-law pressure derivatives or
    outputs of a renewal/division-event commitment law, while the existing
    corpus still does not supply the needed pressure, action, density table,
    or waiting-time law.
32. the same-law pressure and division-commitment campaign, which proves that
    pressure derivatives reconstruct closed-history coefficients only after
    the law is supplied, and that a self-consistent renewal commitment equation
    can select a nonzero coefficient only conditionally on an intrinsic
    waiting-law shape and dimensionless commitment scale.
33. the intrinsic division-event commitment law, which derives exponential
    eventless survival from sealed gluing in additive RN/KL evidence, fixes
    the scale by exact RN self-accounting, rejects hidden clock
    regraduations and full-odds double-counting, and selects finite
    closed-history coefficients by the strict-convex fixed point
    `grad psi_G(h_G)=exp(-h_G)`.
34. the cofinal primitive-ledger commitment theorem, which proves that the
    commitment selector is refinement-stable on the projective primitive
    RN/KL quotient ledger: serial subdivisions preserve total survival,
    duplicate coordinate ledgers are rejected by rank, non-silent vertical
    modes are retained, and controlled convex refinements converge to the
    cofinal minimizer.
35. the cover-independence theorem for the commitment law, which proves that
    admissible diamond covers select the same h_G after primitive quotienting,
    while overlap double-counting, per-cell serial commitment, dropped
    vertical modes, and arbitrary mixed bases are rejected as non-admissible
    descriptions of the same sealed process.
```
