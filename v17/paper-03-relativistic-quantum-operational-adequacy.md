# Relativistic quantum-operational adequacy without a preferred laboratory frame

## A locally covariant system--probe extension of the procedures-first architecture

Date: 2026-08-22

Status: **GREEN-UNREVIEWED MATHEMATICAL CONSTRUCTION**

## Abstract

We ask whether the procedures-first stochastic architecture accepted in
Papers 01--02 survives the operational structure of relativistic quantum field
theory. The comparison is deliberately conditional. We take as input a
declared locally covariant algebraic quantum field theory on oriented,
time-oriented globally hyperbolic spacetimes, a compatible state class, and
localized system--probe couplings satisfying causal factorization. None of
these inputs is derived.

For every admitted finite localized-measurement program we construct a typed
physical-procedure category, a presentation groupoid, and the complete
relativistic operational quotient. The system--probe scattering morphism
induces positive instruments. Causal factorization makes causally disjoint
program serializations operationally equal, while retaining the order of
timelike couplings. Locality of the complete nonselective operation proves
no-signalling; selective conditioning can nevertheless steer a spacelike
conditional state. Commuting local algebras remain compatible with Bell
violation, so microcausality is not Bell factorization.

We also give a positive history representation of every admitted finite
program. Its latent states are complete algebraic predictive states or
conditional process objects and its transitions are the outcome-weighted
instrument updates. This representation is covariant on the registered
interface and compositional under causal wiring. It is also global,
contextual, generally memory-bearing, background-dependent, and
ontologically unselected. Type-III local algebras, the split property,
Reeh--Schlieder cyclicity, gauge sectors, identical particles, and ultraviolet
scope are treated without importing regional density matrices or lattice
factorizations.

The strongest supported rung is
`P03-LOCALLY-COVARIANT-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT`.
This establishes relativistic operational adequacy of the architecture on a
declared comparator. It does not construct a fundamental QFT, spacetime,
preferred-state law, local microontology, actual trajectory, internal clock,
or gravity.

## 1. Exact claim and nonclaim

### 1.1 Claim

Let an **admitted relativistic packet** supply:

1. a locally covariant algebraic theory on a declared spacetime;
2. a measurable compatible state class;
3. finitely many localized system--probe schemes;
4. complete finite-outcome instruments, or standard-Borel instruments with
   explicit measurable kernels;
5. finite typed control and record systems; and
6. causal factorization for every registered composite.

Then all registered predictions admit a positive contextual record-history
representation and a complete operational quotient with:

- covariant evaluation under admitted spacetime morphisms;
- schedule independence for causally disjoint couplings;
- physical order retention for timelike couplings;
- nonselective spacelike no-signalling;
- selective steering without signalling; and
- compatibility with Bell-violating local correlations.

### 1.2 Nonclaim

The theorem does not say that the comparator's spacetime, orientation, state,
algebra net, or dynamics is fundamental. It does not select one AQFT, one
state, one field content, one gauge group, one preferred frame, one ontology,
or one actual history. It gives no construction of interacting four-
dimensional QFT, the Standard Model, gravity, or background independence.

## 2. Comparator and variance conventions

### Definition 2.1 — spacetime category

`Loc` is a declared category whose objects are oriented, time-oriented,
globally hyperbolic Lorentzian spacetimes of one fixed dimension and whose
morphisms

$$
\psi:M\longrightarrow N
$$

are orientation- and time-orientation-preserving isometric embeddings with
causally convex images. A concrete packet may restrict this category further.

The metric, dimension, orientations, and global hyperbolicity are comparator
inputs. They are not outputs of this paper.

### Definition 2.2 — locally covariant algebra

Let `Alg` be a category of unital complex `*`-algebras with injective unital
`*`-morphisms, or a specified $C^*$/$W^*$ subcategory when positivity and
normality are used. A locally covariant theory is a covariant functor

$$
\mathcal A:\mathbf{Loc}\longrightarrow\mathbf{Alg}.
$$

For every morphism $\psi:M\to N$ write
$\alpha_\psi=\mathcal A(\psi)$.

The packet also supplies isotony on its region net, Einstein causality, and
the time-slice axiom. Dynamical locality is never inferred from those axioms;
if used, it is an additional named hypothesis.

### Definition 2.3 — state class and measurable structure

For each $M$, $\mathfrak S(M)$ is a declared class of positive normalized
linear functionals on $\mathcal A(M)$. In represented von Neumann examples it
is restricted as stated, normally to locally normal states. Its measurable
structure is part of the packet.

For $\psi:M\to N$, states restrict contravariantly:

$$
\psi^*:\mathfrak S(N)\longrightarrow\mathfrak S(M),
\qquad
\psi^*\nu=\nu\circ\alpha_\psi.
$$

No canonical extension $\mathfrak S(M)\to\mathfrak S(N)$ is presumed. Under a
spacetime isomorphism, inverse pullback supplies the corresponding transported
state. Any other extension map must be an exposed typed field.

A convenient measurable domain is a separable unital $C^*$-algebra with the
weak-$*$ Borel state space, or a von Neumann algebra with separable predual and
its normal-state Borel structure. Outside that domain, every evaluation,
update, conditioning, and reader map must be separately proved measurable.

### Proposition 2.4 — evaluation naturality

Let $A\in\mathcal A(M)$ and $\nu\in\mathfrak S(N)$. Then

$$
(\psi^*\nu)(A)=\nu(\alpha_\psi(A)).
$$

This identity is the variance-correct scalar naturality condition. Equal
coordinate expressions without the intertwining map do not establish it.

**Proof.** It is the definition of pullback. The content is typing: the two
sides compare one observable and one state through the functor rather than
pretend that a state pushes forward canonically. $\square$

### State-selection wall

The state class is covariant only in this pullback/closure sense. The
construction does not choose one state naturally on every spacetime. In the
scope of the Fewster--Verch no-natural-state theorem, such a choice would
contradict the comparator hypotheses. Hadamard or microlocal-spectrum
conditions, when used, specify an admissible class in named free-field models;
they do not select a unique vacuum or cosmology.

## 3. Localized system--probe schemes

### Definition 3.1 — one coupling scheme

On $M$, a scheme $s$ contains:

$$
s=(\mathcal A,\mathcal B,K,\Theta,\sigma,\mathsf E).
$$

Here $\mathcal B$ is a probe theory, $K\Subset M$ is the compact coupling
region, $\sigma$ is the initial probe state, and $\mathsf E$ is a finite POVM
or a typed standard-Borel probe instrument. The uncoupled system--probe
algebra uses one tensor product fixed by the packet. This tensor product joins
two theories; it is not a claim that the system's algebras of two touching
spacetime regions tensor-factor.

$\Theta$ is the scattering `*`-automorphism in the following fixed convention:
it maps an uncoupled outgoing observable to the corresponding uncoupled
incoming representative. A source using the inverse scattering convention
must translate all later formulae at this definition.

The coupled theory and comparison maps are required to agree with the
uncoupled theory outside the causal influence of $K$. Their time-slice
isomorphisms construct $\Theta$; an arbitrary global unitary does not qualify.

### Definition 3.2 — induced pre-instrument

Let

$$
\eta_\sigma=\operatorname{id}\otimes\sigma.
$$

For a probe effect $B$ and system observable $A$, define

$$
\mathcal J_{s,B}(A)
=\eta_\sigma\!\left(\Theta(A\otimes B)\right).
$$

The induced system effect is

$$
\varepsilon_s(B)=\mathcal J_{s,B}(1),
$$

and in state $\omega$ the outcome probability is

$$
p_s(B\mid\omega)=\omega(\varepsilon_s(B)).
$$

For $p_s(B\mid\omega)>0$, the posterior state is

$$
U_{s,B}(\omega)(A)
=\frac{\omega(\mathcal J_{s,B}(A))}
       {\omega(\mathcal J_{s,B}(1))}.
$$

At zero support we retain a typed zero functional and do not invent a
normalized state.

### Theorem 3.3 — positivity and normalization

For every admitted positive probe effect $B$, $\mathcal J_{s,B}$ is a positive
map; in the $C^*/W^*$ packet it is completely positive. If
$\{B_r\}_{r\in R}$ is a finite complete POVM, then

$$
\sum_{r\in R}\mathcal J_{s,B_r}=\mathcal J_{s,1},
\qquad
\sum_r p_s(r\mid\omega)=1.
$$

Every positive-support posterior is a normalized positive state.

**Proof.** $A\mapsto A\otimes B$ is completely positive for $B\ge0$;
$\Theta$ is a `*`-automorphism and $\eta_\sigma$ is completely positive. Their
composition is completely positive. Linearity and $\sum_rB_r=1$ give the
first equality. Unitality of $\Theta$ and normalization of $\sigma$ give
$\mathcal J_{s,1}(1)=1$, hence normalization. Dividing the positive
functional $\omega\circ\mathcal J_{s,B}$ by its positive mass gives a state.
$\square$

### Theorem 3.4 — localization

Under the localized-coupling hypotheses of the packet, $\varepsilon_s(B)$ is
localizable in every causally convex connected region containing the causal
hull of $K$. If $C$ is localized spacelike to $K$, the complete nonselective
operation acts trivially on it:

$$
\mathcal J_{s,1}(C)=C.
$$

**Proof.** The first statement is the induced-observable localization theorem
for the system--probe scattering construction. The second follows because
the scattering morphism agrees with the uncoupled identification outside the
causal influence of $K$, and $\eta_\sigma(C\otimes1)=C$. It is a property of
the localized coupling, not a consequence of $[C,D]=0$ alone. $\square$

## 4. Composite measurements and relativistic causality

### Definition 4.1 — support order

For compact coupling regions $K_i,K_j$, write $K_i\prec K_j$ when the packet
certifies the causal ordering required by its factorization theorem. Write
$K_i\perp K_j$ when they are causally disjoint. Timelike order is physical;
the order in which a program loop happens to enumerate a spacelike family is
not.

### Theorem 4.2 — causal factorization

Let $s_1,\ldots,s_n$ be an admitted finite family whose composite scattering
scheme satisfies causal factorization.

1. If $K_i\prec K_j$, the composite instrument equals the physically ordered
   composition with $i$ before $j$.
2. If $K_i\perp K_j$, both linear extensions are admissible and

   $$
   \mathcal J_{i,r}\circ\mathcal J_{j,t}
   =\mathcal J_{j,t}\circ\mathcal J_{i,r}
   $$

   on the full registered algebra, for every pair of outcomes.
3. Any two linear extensions of the same finite causal partial order yield
   the same joint instrument, outcome law, and final operational state.

**Proof.** Items 1--2 are the packet's scattering causal-factorization theorem
carried through the probe-state partial evaluation. Any two linear extensions
of a finite partial order are connected by adjacent exchanges of incomparable
elements. Item 2 validates each exchange, proving item 3. Equality on one
initial state would not suffice; the maps themselves intertwine. $\square$

### Corollary 4.3 — no hidden scheduling frame

For the registered program family, no scalar probability, complete joint law,
or final operational class depends on a linear serialization of causally
disjoint couplings. A foliation or loop index used to calculate the common map
is operationally idle on this interface.

This does not prove that all possible microscopic completions lack preferred
structure.

### Theorem 4.4 — nonselective spacelike no-signalling

Let scheme $A$ be localized in $O_A$, let $D_b$ be the effect of a complete
reader localized in causally disjoint $O_B$, and let
$\{B_a\}_a$ be a complete local probe POVM at $A$. Then

$$
\sum_a p(a,b\mid\omega)
=\omega(D_b).
$$

More generally, every complete reader confined to $O_B$ has the same marginal
whether the nonselective $A$-instrument is performed or omitted.

**Proof.** By Theorem 3.3, summing branches gives
$\mathcal J_{A,1}$. By Theorem 3.4,
$\mathcal J_{A,1}(D_b)=D_b$. Evaluation in $\omega$ proves the identity. The
same calculation applies after arbitrary compatible prefixes and remote
reader continuations. $\square$

### Proposition 4.5 — steering is not signalling

There are admitted entangled-state controls for which

$$
p(b\mid a,\omega)\ne p(b\mid\omega)
$$

for some positive-support result $a$, while Theorem 4.4 holds after summing
over $a$. The result $a$ is not controlled; comparing conditional ensembles
requires its retained classical record.

**Exact control.** In a declared split matrix-subalgebra control, prepare the
singlet state and measure $\sigma_z$ in both spacelike regions. Alice's
outcomes are equiprobable. Conditional on Alice's $+1$, Bob obtains $-1$ with
probability one; without Alice's record Bob's two outcomes remain
equiprobable. This control uses a separately named split/type-I
interpolation. It is not a tensor factorization theorem for arbitrary
touching QFT regions.

### Proposition 4.6 — Bell compatibility

In a named QFT comparator satisfying the Summers--Werner hypotheses, there are
commuting spacelike local observables and states violating CHSH. This is the
QFT existence control. Separately, the split-qubit finite-subalgebra
calibration checks the probability and premise bookkeeping with the exact
choice

$$
A_0=\sigma_z,\quad A_1=\sigma_x,
$$

$$
B_0=-\frac{\sigma_z+\sigma_x}{\sqrt2},\qquad
B_1=-\frac{\sigma_z-\sigma_x}{\sqrt2},
$$

in the singlet state. Then

$$
S=E_{00}+E_{01}+E_{10}-E_{11}=2\sqrt2>2.
$$

The local marginals remain independent of the remote setting. The calibration
does not replace the Summers--Werner QFT theorem, and the theorem does not by
itself construct a particular probe coupling for each ideal observable.
Together they establish the registered compatibility claim at their separate
scopes. Hence:

```text
Einstein causality                         yes
operational remote-setting independence   yes
parameter independence for hidden lambda  not assigned: no Bell-local lambda model is posited
outcome independence for hidden lambda    not assigned / incompatible with Bell factorization under the full premises
Bell factorization                         no
measurement independence                   declared in this control
```

The Bell example is existential. It is not claimed for every state, region,
or AQFT.

## 5. Relativistic procedures and presentation gauge

### Definition 5.1 — boundary types

A boundary type records:

$$
(M,\mathcal A,\mathfrak S,\text{open probe ports},
 \text{classical records},\text{reader domain}).
$$

Records and ports have exact types. Forgetting a result changes the boundary;
it is not a presentation rename.

### Definition 5.2 — physical procedure category

$\mathcal P_{\rm rel}$ is the small constructor-closed category generated by
the admitted packet's:

1. state preparations;
2. localized probe couplings and outcome instruments;
3. causally allowed sequential composition;
4. causally disjoint parallel families;
5. trusted randomization;
6. finite classical record write/read and causal adaptation;
7. coarse-graining and discard; and
8. admitted covariant transports.

Composition exists only when source and target boundary types match and the
causal wiring is allowed. The symmetric exchange for parallel factors is
licensed only for causally disjoint families. Reversing a timelike order is a
different procedure or is inadmissible.

### Definition 5.3 — presentation groupoid

$\mathcal G_{\rm pres}$ is generated by:

- coordinate-chart changes with all geometric data transported;
- renaming bound probe and record variables;
- reassociation and exchange of causally disjoint serialization syntax; and
- natural transport along comparator isomorphisms.

It does not change a coupling region, causal relation, interaction, state,
effect, calibration, retained record, accessible sector, or any variable that
changes a registered probability.

### Proposition 5.4 — presentation descent

Evaluation, induced instruments, causal composition, records, and readers are
constant on $\mathcal G_{\rm pres}$ orbits.

**Proof.** Bound-name and syntax changes leave the typed composite unchanged.
For comparator isomorphisms, algebra/probe naturality and state pullback give
Proposition 2.4 at every node; induction over the finite program gives the
same joint law. Causally disjoint serialization is removed only after Theorem
4.2 proves equality of the complete operations. $\square$

### Definition 5.5 — complete operational equivalence

For same-typed procedures $p,p'$, write $p\sim_{\rm op}p'$ iff every
compatible covariant prefix, localized ancillary probe, causally allowed
adaptive continuation, record operation, and complete reader has the same
joint law in every registered state/context.

Define

$$
q_{\rm rel}:\mathcal P_{\rm rel}\longrightarrow
\mathcal Q_{\rm rel}=\mathcal P_{\rm rel}/\!\sim_{\rm op}.
$$

### Theorem 5.6 — congruence and universal property

$\sim_{\rm op}$ is a typed congruence under every constructor of Definition
5.2. Therefore $\mathcal Q_{\rm rel}$ is a well-defined quotient category on
the reachable registered interface. Any prediction functor out of
$\mathcal P_{\rm rel}$ that is constant on complete operational classes
factors uniquely through $q_{\rm rel}$.

**Proof.** Suppose $p\sim_{\rm op}p'$. Substituting either into any registered
constructor and then any complete tester produces another complete compatible
tester of $p$ or $p'$. Its scalar laws agree by definition. This proves
closure under composition, parallel composition, randomization, records,
adaptation, covariant transport, coarse-graining, and discard. The ordinary
quotient universal property then applies on the separated reachable image.
$\square$

New physical readers may refine the quotient. No inverse from an operational
class to a microscopic procedure is claimed.

## 6. Positive predictive histories

### Definition 6.1 — complete predictive object

At a causal cut of one admitted finite program, let $\Lambda$ be the complete
algebraic predictive object required to evaluate every registered remaining
continuation. In a memoryless control it is a normalized algebraic state. In
an adaptive or memory-bearing control it includes the conditional process
object and every physical record/port needed by the remaining comb.

$\Lambda$ is never reduced to a density matrix unless the packet supplies a
type-I representation. It contains no procedure-name tag.

### Definition 6.2 — branch kernel

For a finite instrument $\{\mathcal J_{i,r}\}_{r\in R_i}$ define

$$
p_i(r\mid\lambda)=\lambda(\mathcal J_{i,r}(1))
$$

and, at positive support,

$$
U_i(\lambda,r)
=\frac{\lambda\circ\mathcal J_{i,r}}
       {p_i(r\mid\lambda)}.
$$

The substochastic kernel is

$$
K_i(r,d\lambda'\mid\lambda)
=p_i(r\mid\lambda)\,
 \delta_{U_i(\lambda,r)}(d\lambda').
$$

At zero support its mass is zero and the target is a typed zero functional.
For a standard-Borel outcome space the same formula denotes the supplied
measurable instrument kernel; existence of a regular conditional is not
assumed outside the declared standard-Borel domain.

### Theorem 6.3 — finite-program positive representation

Let $p$ be any admitted finite localized-measurement program with initial
predictive object $\lambda_0$. Iterating the branch kernels and deterministic
record/control transitions defines a normalized positive measure

$$
\Gamma_p(dH)
$$

on complete histories

$$
H=(\lambda_0,r_1,\lambda_1,\ldots,r_n,\lambda_n,
   \text{records}).
$$

For every complete registered reader $R$,

$$
\Pr_{\Gamma_p}[R=x]
=\Pr_{\rm AQFT}[R=x].
$$

**Proof.** Theorem 3.3 normalizes each complete instrument. For a history
$h=(r_1,\ldots,r_n)$ its mass is the iterated unnormalized instrument

$$
\Gamma_p(h)
=\lambda_0\!left(
 \mathcal J_{1,r_1}\circ\cdots\circ
 \mathcal J_{n,r_n}(1)
 \right),
$$

with the order fixed by the program's Heisenberg convention. Induction shows
that the product of conditional masses from Definition 6.2 equals this
number. Summing the last outcome uses completeness, then iterating backwards
gives total mass one. The records and reader are deterministic measurable
maps of the branch data, so pushforward yields the AQFT joint law. $\square$

### Theorem 6.4 — prefix coherence and indivisibility

Marginalizing every future outcome of a complete program returns the law of
its performed prefix. This does not imply that an arbitrary geometric cut is
a Markov division.

**Proof.** Repeated instrument normalization removes the suffix. A boundary
is restartable only if its retained $\lambda$ and records are complete
predictive data for every compatible future. If two pasts share the proposed
boundary data but have different future profiles, the cut is not a division
and no intermediate kernel is licensed. $\square$

### Theorem 6.5 — causal and covariant coherence

The measures $\Gamma_p$ descend through presentation gauge. Causally disjoint
serializations push forward to one history law after the corresponding record
exchange. Covariantly transported packets have identical transported history
laws under the state-pullback comparison of Proposition 2.4.

**Proof.** Apply Theorems 4.2 and 5.4 to every finite cylinder probability.
Cylinder equality determines the finite history law. $\square$

### Cost theorem 6.6

The construction of $\Gamma_p$ is a positive representation theorem, not an
ontological selection theorem.

1. $\lambda$ is the complete predictive object already used by the quantum
   comparator.
2. It may be global and encode spacelike entanglement.
3. It may retain the entire relevant process memory.
4. Its branch kernel depends on the physical instrument procedure.
5. The family is indexed by declared experiment packets rather than supplied
   by one universal cosmological law.
6. No rule selects one actual $H$.

Consequently it is not a Bell-local hidden-variable model, local field
beable, complete Barandes ontology, or explanation of why quantum theory is
true.

## 7. Contextuality, fibers, and preferred structure

### Definition 7.1 — relativistic structural contextuality

Let $\mathsf A$ be any system-facing representation assignment defined on
$\mathcal P_{\rm rel}$. It is noncontextual exactly when there exists
$\overline{\mathsf A}$ with

$$
\mathsf A=\overline{\mathsf A}\circ q_{\rm rel}.
$$

Failure of this equation is contextuality. Spacetime coordinates, source-code
labels, or run tokens are not allowed in $\mathsf A$ unless they denote a
physical procedure field.

### Proposition 7.2 — positive preparation contextuality survives

Inside a declared split matrix-subalgebra control, fix one state on every
complementary physical degree of freedom. The same complete global state has
two trusted preparation procedures whose local matrix component satisfies

$$
\tfrac12(|0\rangle\!\langle0|+|1\rangle\!\langle1|)
=\tfrac12(|+\rangle\!\langle+|+|-\rangle\!\langle-|)
=I/2.
$$

The predictive-state representation assigns distinct measures supported on
the two different local pure-state pairs tensored, through the declared split
control, with the same complementary state. Their barycenter is the same
complete global state, so the preparations have the same complete
system-facing quantum profile, but the assignment does not descend through
$q_{\rm rel}$. No procedure tag was appended; the difference lies in the
predictive states occurring in the trusted mixtures.

This is a positive contextual existence control. It does not establish that
these predictive states are nature's microscopic ontology.

### Definition 7.3 — idle-fiber inflation

For any standard probability space $(Z,\zeta)$ ignored by every registered
transition and reader, inflate a history model by

$$
\widetilde\Lambda=\Lambda\times Z,
\qquad
\widetilde\Gamma_p=\Gamma_p\otimes\zeta,
$$

and project $\pi(\lambda,z)=\lambda$. This is a positive affine reduction that
preserves every prediction, mixture, source product, and causal composition.

### Theorem 7.4 — idle-fiber nonselection

No invariant required to be natural under the admitted projection $\pi$ can
select the $Z$ coordinate or its cardinality as physical ontology. In
particular, an empirically idle foliation label may be appended, but
operational covariance supplies no evidence that it exists and no prior over
its values.

This theorem does not prove that every hidden preferred structure is idle. A
structure that changes a registered probability fails T17 and is observable.

### Corollary 7.5 — preferred-frame result

The construction earns only:

> No preferred frame is operationally visible in the registered comparator
> domain.

It does not earn:

> No microscopic completion of nature contains preferred structure.

## 8. Type III, split inclusions, and localization traps

### Proposition 8.1 — algebraic-state sufficiency

Every construction above uses positive functionals, effects, and positive/CP
maps. It therefore remains meaningful when a local von Neumann algebra is
type III and has no trace-class density operator intrinsic to the region.

A candidate proof that writes
$\rho_O$, $\operatorname{tr}(\rho_O A)$, a finite Kraus list, or
$\mathcal H=\mathcal H_O\otimes\mathcal H_{O'}$ must separately justify that
representation. No such object is inferred from the AQFT axioms.

### Proposition 8.2 — split-property conditional

Suppose an inclusion of separated local von Neumann algebras is split, so
there exists a type-I factor $\mathcal N$ with

$$
\mathcal A(O_1)''\subset\mathcal N\subset\mathcal A(O_2)''
$$

for $\overline O_1\subset O_2$ with the required collar. Then the registered
control may use the associated tensor-product independence and matrix
subalgebras. The conclusion is conditional on split/nuclearity hypotheses and
separation.

It does not extend to touching regions, arbitrary gauge theories, or the
continuum as a global tensor product. A type-I interpolation is not a lattice
cell.

### Proposition 8.3 — Reeh--Schlieder no-signal control

In a named Reeh--Schlieder state, the local algebra acting on the cyclic vector
has dense orbit. Approximating a remote target vector may nevertheless require
operators of growing norm and postselection of small or vanishing success.
The normalized selective target is therefore not a deterministic local
channel. The complete nonselective operation still obeys Theorem 4.4.

Density of a mathematical orbit is not controllable superluminal
preparation.

## 9. Gauge, sectors, particles, continuum, and UV

### 9.1 Gauge and superselection types

The construction distinguishes:

```text
observable net
charged field net
global or local gauge action
superselection sector
Wilson/flux operator
regional center or edge data
probe record.
```

No arrow between these types is inserted without a named model theorem.
Gauss constraints may obstruct regional tensor products. DHR-type sector and
spin/statistics conclusions retain localization, conjugacy, topology,
symmetry, and spectrum hypotheses. Operational covariance alone selects no
gauge group, charge spectrum, or sector statistics.

### 9.2 Identical particles

Relativistic fields and observable/sector structure replace labeled-particle
tensor factors. Particle number, Fock representation, and asymptotic particle
interpretation are representation- and regime-dependent. No physical label is
attached to identical particles in $\mathcal P_{\rm rel}$.

### 9.3 Continuum scope

The main theorem is abstract-net mathematics plus a named free-field
system--probe example inherited from the localized-measurement literature. It
does not construct an interacting 3+1 model. A finite-mode or lattice example
is only a control and cannot establish physical discreteness. Removing a
cutoff requires its own convergence and renormalization theorem.

Entanglement entropy and a regional density matrix are not universal AQFT
objects. Bell correlations, algebraic states, and local instruments do not
require either.

## 10. Locally covariant but not background independent

The functorial comparator expresses the same theory on different declared
backgrounds and relative Cauchy evolution describes its response to compact
metric perturbations. This is a strong covariance property. It is not a
quantum law for the metric.

No probability distribution over metrics is present. No Einstein equation,
constraint algebra, diffeomorphism-gauge quotient of dynamical geometries, or
matter--geometry backreaction law is constructed. Consequently neither
relative Cauchy evolution nor stress-energy response promotes the background
to a physical quantum variable.

## 11. Exact theorem package

### Theorem 11.1 — relativistic operational adequacy

For the admitted packet family, Theorems 2.4, 3.3--3.4, 4.2--4.6, 5.4--5.6,
6.3--6.6, 7.2--7.5, and Propositions 8.1--8.3 jointly establish:

1. exact comparator typing;
2. variance-correct local covariance;
3. state-class covariance without state selection;
4. localized positive instruments;
5. causal factorization;
6. nonselective no-signalling;
7. steering/signalling separation;
8. spacelike schedule independence;
9. Bell compatibility;
10. a positive predictive-history representation;
11. a physical procedure category and complete operational quotient;
12. contextuality and idle-fiber nonselection;
13. type-III/tensor refusal;
14. conditional split independence;
15. Reeh--Schlieder no-signal control;
16. gauge/sector/particle/UV typing;
17. no operationally visible preferred frame at registered scope; and
18. an explicit ontology/actuality debt.

The theorem is conditional on the comparator packet. It does not derive the
packet.

### Quantifier ledger

| theorem family | quantifier | scope |
|---|---|---|
| T1--T7 | every admitted packet/program | printed measurability, locality, causal-factorization hypotheses |
| T8 | existence | one named Bell-capable comparator; not every state/region/theory |
| T9--T10 | every admitted finite program | global contextual predictive representation; reachable interface |
| T11 | universal refusal plus named examples | no generic regional density/tensor assumption |
| T12--T13 | conditional | split/nuclearity and Reeh--Schlieder hypotheses respectively |
| T14--T16 | typed ledger / model-specific positive uses | no cross-model conjunction |
| T17 | every registered transport/schedule | operational domain only |
| T18 | universal nonimplication | entire Paper 03 result |

## 12. Required controls R1--R32

| ID | Positive disposition | Refusal disposition |
|---|---|---|
| R1 | Proposition 2.4 transports one packet naturally | equal coordinate scalars without intertwiners fail |
| R2 | Theorem 4.2 commutes two disjoint couplings as maps | one-state/program-loop equality fails |
| R3 | Theorem 4.2 retains timelike order | reversal is different or inadmissible |
| R4 | Theorem 4.4 sums a complete instrument | a selective branch is not no-signalling |
| R5 | Proposition 4.5 gives exact steering | no record-free controlled signal follows |
| R6 | Proposition 4.6 gives CHSH $2\sqrt2$ | Bell factorization is not inferred from commutation |
| R7 | Section 3 uses compact localized coupling | global hypersurface collapse is absent |
| R8 | Theorem 4.2 covers a factorized finite causal family | noncausal impossible-measurement updates are inadmissible |
| R9 | Section 2.3 uses algebraic normal states | regional density/tracial formula is refused generically |
| R10 | Section 3 uses normal CP maps where represented | finite Kraus form requires extra hypotheses |
| R11 | Proposition 8.2 uses separated split inclusions | touching/arbitrary tensor factorization refused |
| R12 | Proposition 8.3 retains cyclic density | deterministic remote preparation refused |
| R13 | Section 9 uses field/sector typing | labeled-particle ontology refused |
| R14 | Section 9 distinguishes observable/gauge data | naive Gauss-constrained tensor product refused |
| R15 | retained outcome is a boundary field | forgotten outcome is a distinct boundary |
| R16 | zero support carries zero mass | no normalized posterior is created |
| R17 | Theorem 6.4 fixes prefix marginal | later unperformed choice cannot alter it |
| R18 | independent probes use a declared product source | correlated probes are a different preparation |
| R19 | Proposition 4.6 uses entanglement | Theorem 4.4 needs no separability |
| R20 | Proposition 2.4 covers curved-background transport | metric remains declared |
| R21 | time-slice supports scattering dynamics | no internal clock/time orientation derived |
| R22 | main theorem is abstract-net conditional | no interacting 3+1 existence follows |
| R23 | named free-scalar probe example is admitted | it is neither Standard Model nor gravity |
| R24 | cutoff controls may approximate examples | continuum/discreteness claims refused |
| R25 | Theorem 6.3 constructs a global positive model | relativistically local microontology refused |
| R26 | Definition 7.3 constructs an idle frame fiber | existence/equiprobability not inferred |
| R27 | Proposition 7.2 is a physical procedure pair | coordinate tags are forbidden |
| R28 | records are persistent program fields | persistence is not division/actualization |
| R29 | Theorem 5.6 gives registered quotient | new readers may refine it |
| R30 | Theorem 11.1 prints the full product | no Paper 04/gravity promotion |
| R31 | state pullback/class closure is covariant | no preferred state on all spacetimes |
| R32 | Hadamard control is model-specific | no universal vacuum/cosmological selector |

## 13. Hostile attacks 1--76

Every registered attack is dispositioned against the construction rather than
merely restated.

| attack | disposition |
|---:|---|
| 1 | Definitions 2.2--2.3 separate abstract, represented, and measurable objects; ill-typed packets are inadmissible |
| 2 | coordinates occur only in presentations and never as beables |
| 3 | active spacetime symmetries transport physical inputs and are not automatically gauge |
| 4 | orientation/time orientation remain declared support-order data |
| 5 | `Loc` morphisms require causally convex image |
| 6 | the coupling region is physical and cannot move under presentation gauge |
| 7 | run tokens are excluded from Definition 5.2 |
| 8 | Theorem 6.4 makes every performed prefix suffix-independent |
| 9 | the complete reader family freezes with the packet, before ontology comparison |
| 10 | Proposition 2.4 requires natural intertwiners, not equal final numbers |
| 11 | Theorem 5.6 claims no inverse outside the reachable quotient |
| 12 | retained and forgotten records are different boundary types |
| 13 | Section 3 contains no global Lüders hypersurface |
| 14 | only system--probe or separately certified local CP maps qualify |
| 15 | Theorem 4.4 uses operation locality, not commutation alone |
| 16 | Proposition 4.5 explicitly separates selected and nonselected laws |
| 17 | zero-support branches remain zero functionals |
| 18 | forgotten outcomes apply the full nonselective channel, not identity in the causal future |
| 19 | Theorem 4.2 preserves timelike order |
| 20 | disjoint serialization dependence violates Theorem 4.2 and kills T7 |
| 21 | equality is required on the full admitted algebra/state domain |
| 22 | a reader's localization is part of its type |
| 23 | probe correlations are explicit source fields; omission changes the packet |
| 24 | postselection records are physical classical communication resources |
| 25 | Theorem 3.4 bounds the operation by the registered causal hull |
| 26 | Theorem 6.4 proves full shared-prefix equality, not only one final marginal |
| 27 | Proposition 4.6 separates microcausality from Bell factorization |
| 28 | no-signalling is not equated with all Bell conditional independences |
| 29 | measurement independence is explicit in the Bell control |
| 30 | Cost theorem 6.6 labels the predictive state global/nonlocal |
| 31 | commuting algebras are not inferred separable |
| 32 | CHSH violation coexists with Theorem 4.4 and is not a signal |
| 33 | calculation order is removed only after map-level factorization |
| 34 | Corollary 7.5 refuses microscopic preferred-frame absence |
| 35 | entropy requires a separately typed factorization and UV prescription |
| 36 | Proposition 8.3 blocks controllable Reeh--Schlieder signalling |
| 37 | Proposition 8.1 forbids universal regional density matrices |
| 38 | finite Kraus form is not required and needs separate hypotheses |
| 39 | touching local algebras are never tensor-factorized by default |
| 40 | Proposition 8.2 retains split/nuclearity/separation premises |
| 41 | type-I interpolation is explicitly not a lattice |
| 42 | Section 9 separates observable and charged field algebras |
| 43 | Gauss/center/edge data are typed rather than discarded |
| 44 | Wilson/flux localization must be supplied by the model |
| 45 | Section 9.2 excludes labeled identical particles |
| 46 | Fock space and particle number are representation/regime inputs |
| 47 | spin/statistics requires sector/spectrum/symmetry hypotheses |
| 48 | superselection does not choose one actual outcome |
| 49 | Definition 6.1 forbids procedure-name ontic tags |
| 50 | Cost theorem 6.6 refuses explanatory microphysics |
| 51 | Theorem 6.4 licenses division only at future-sufficient cuts |
| 52 | postselected future states cannot replace physical prefix states |
| 53 | trusted mixture affinity is built into the branch measure |
| 54 | independent probes use declared tensor-pushforward sources |
| 55 | nonlinear barycenter erasure is not an admitted representation morphism |
| 56 | only exposed idle reductions count; not every hidden variable is gauge |
| 57 | entropy, dimension, and coding length select no ontology here |
| 58 | Definition 7.3 permits a declared measure but infers no uniform prior |
| 59 | an observed record does not select a microscopic trajectory |
| 60 | conditioning/decoherence are not actualization in this construction |
| 61 | abstract-net conditional mathematics proves no interacting 3+1 model |
| 62 | a free scalar control is not universal dynamics |
| 63 | every cutoff is labeled as a control |
| 64 | cutoff removal requires a separate convergence/renormalization theorem |
| 65 | a mode lattice is not promoted to spacetime atoms |
| 66 | `Loc` remains a comparator, not ontology |
| 67 | comparator time orientation is not internal time |
| 68 | relative Cauchy evolution is not gravity |
| 69 | no v16 dimension, metric, or FLRW object enters the input hash table |
| 70 | Section 10 separates local covariance from background independence |
| 71 | Paper 04 remains closed before terminal adjudication |
| 72 | the title/result say operational adequacy, not a full theory of reality |
| 73 | the no-natural-state wall forbids a universal preferred state |
| 74 | Hadamard is an admissibility condition, not a unique vacuum |
| 75 | dynamical locality is never inferred from covariance plus time-slice |
| 76 | $\omega$ is printed as contingent declared state input, not hidden law output |

All attacks are blocked by definitions or theorem premises. This is an author
construction claim and remains subject to independent counterexamples.

## 14. Product coordinates

| coordinate | construction status | exact boundary |
|---|---|---|
| input | `BOUND` | Paper 01/Paper 02 v2 plus declared AQFT packets |
| spacetime-comparator | `DECLARED-STANDARD` | oriented/time-oriented globally hyperbolic Lorentzian background |
| algebra-net | `DECLARED-STANDARD` | locally covariant functor; no interacting-model derivation |
| state-class | `DECLARED-AND-TYPED` | contravariant pullback, packet closure, no preferred natural state |
| procedure | `CONSTRUCTED` | small constructor-closed relativistic laboratory procedures |
| presentation | `CONSTRUCTED` | harmless chart/name/disjoint-serialization/isomorphism groupoid |
| quotient | `CONSTRUCTED-SCOPED` | complete registered reachable interface |
| covariance | `CONSTRUCTED-CONDITIONALLY` | naturality for admitted packet morphisms |
| time-slice | `INHERITED-COMPARATOR` | supports scattering; no internal time |
| instrument | `CONSTRUCTED` | induced system--probe CP pre-instruments |
| causal-factorization | `CONSTRUCTED-CONDITIONALLY` | packets satisfying scattering factorization |
| spacelike-schedule | `CONSTRUCTED` | all finite linear extensions agree |
| no-signalling | `CONSTRUCTED` | nonselective localized operations and complete remote readers |
| steering | `CONSTRUCTED-CONTROL` | selective conditional difference plus classical-record cost |
| bell | `CONSTRUCTED-EXISTENTIAL-CONTROL` | named comparator/split calibration; not every state/theory |
| positive-model | `CONSTRUCTED-WITH-COSTS` | global predictive algebraic-state histories |
| context | `CONSTRUCTED` | failure to descend through $q_{\rm rel}$ |
| fibers | `CONSTRUCTED-SCOPED` | admitted idle standard-Borel inflation/projection |
| type-III | `REFUSAL-CONSTRUCTED / POSITIVE-MODEL-SPECIFIC` | no universal density/trace/tensor claim |
| split | `CONDITIONAL-CONTROL` | nuclearity/separation/split hypotheses |
| gauge | `TYPED-UNSELECTED` | no gauge group/sector spectrum derived |
| particles | `TYPED-UNSELECTED` | fields/sectors replace labels; Fock/asymptotic data conditional |
| continuum | `ABSTRACT-NET-CONDITIONAL` | no universal interacting 3+1 construction |
| UV | `SCOPED` | no hidden cutoff or uncontrolled removal |
| preferred-frame | `NO-OPERATIONALLY-VISIBLE-FRAME-SCOPED` | idle microscopic structure not excluded |
| record | `CONSTRUCTED-OPERATIONALLY` | typed persistent classical outcomes |
| actuality | `UNCONSTRUCTED` | no branch-selection rule |
| barandes | `ADMISSIBLE-BUT-INCOMPLETE` | no fixed universal configuration/law/trajectory packet |
| ontology | `GLOBAL-PREDICTIVE-CANDIDATE-UNSELECTED` | not local/explanatory/fundamental |
| downstream | `CLOSED` | no clocks, spacetime emergence, matter--geometry, gravity |
| overall ceiling | `GREEN-UNREVIEWED RUNG 7` | operational adequacy with global ontology debt |

## 15. Outcome and strongest honest interpretation

The earliest and strongest supported construction rung is:

```text
P03-LOCALLY-COVARIANT-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

The result means:

> A procedures-first positive-history architecture can encode every admitted
> finite localized AQFT measurement program while respecting local covariance,
> causal factorization, spacelike schedule independence, nonselective
> no-signalling, selective steering, and Bell correlations.

It does **not** mean:

> The universe is a classical stochastic field on a Lorentzian manifold, or
> the global predictive state is the local microscopic reality.

The construction answers an adequacy gate. It leaves the central ontological
question open: what physical referent and law, if any, make the quantum
predictive structure and the spacetime comparator true together?

## 16. Barandes comparison

The construction agrees with a Barandes-style lesson in one important sense:
complete probabilities may be assigned to whole registered processes without
inserting a classical Markov checkpoint at every geometric cut. Conditional
states are lawful at complete predictive boundaries and are not thereby
fundamental collapses.

But the present family is not yet a Barandes ontology of the universe. Each
packet begins with a quantum algebra, state, spacetime, coupling scheme, and
experiment. The positive history law is derived from that predictive object.
A complete Barandes-style proposal would still need:

1. a fixed physical configuration referent;
2. one law for possible complete histories independent of which experiment we
   choose to describe;
3. a contingent initial/cosmological state distinct from the law;
4. a precise division-event rule; and
5. one actual trajectory or an independently motivated actuality principle.

Paper 03 supplies none of those by reinterpretation.

## 17. Primary-source ledger

The construction relies on the following theorem scopes:

1. Brunetti, Fredenhagen, and Verch,
   [locally covariant QFT and relative Cauchy evolution](https://arxiv.org/abs/math-ph/0112041).
2. Fewster and Verch,
   [localized system--probe measurements and causal factorization](https://arxiv.org/abs/1810.06512).
3. Fewster,
   [split property in flat and curved spacetimes](https://arxiv.org/abs/1601.06936),
   and Fewster,
   [locally covariant split-property deformation](https://arxiv.org/abs/1501.02682).
4. Kitajima,
   [local CP operations and funnel-property approximation](https://arxiv.org/abs/1704.01229).
5. Reeh and Schlieder,
   [cyclicity theorem](https://doi.org/10.1007/BF02787889).
6. Summers and Werner,
   [Bell violations in QFT](https://doi.org/10.1007/BF01207366).
7. Doplicher, Haag, and Roberts,
   [local observables and particle statistics](https://doi.org/10.1007/BF01877742).
8. Guido, Longo, Roberts, and Verch,
   [curved-spacetime sectors](https://arxiv.org/abs/math-ph/9906019).
9. Fewster and Verch,
   [dynamical locality and the no-natural-state result](https://arxiv.org/abs/1106.4785).
10. Sahlmann and Verch,
    [microlocal-spectrum/Hadamard scope](https://arxiv.org/abs/math-ph/0008029).

These sources establish comparator mathematics under hypotheses. They do not
select the comparator as fundamental reality.

## 18. Permanent nonimplications and next gate

Even after independent acceptance, Paper 03 cannot imply:

- fundamental Lorentzian spacetime;
- background independence;
- a local microscopic stochastic ontology;
- an interacting 3+1 QFT or the Standard Model;
- a preferred vacuum, cosmological state, or actual trajectory;
- absence of every hidden preferred frame;
- internal time, dimension, metric emergence, or curvature;
- matter--geometry reciprocity or Einstein dynamics; or
- empirical deviation from standard quantum theory.

The next action is a result-neutral construction audit followed by a frozen
three-lens hostile-review protocol. Paper 04 remains closed until terminal
Paper 03 adjudication.
