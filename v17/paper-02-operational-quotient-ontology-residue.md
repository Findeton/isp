# The operational quotient and the ontology residue of quantum processes

## What complete quantum experiments determine, and what they leave open

Date: 2026-08-22

Status: **CONSTRUCTION — GREEN-UNREVIEWED; NO PHYSICAL RESULT AWARDED**

## Abstract

Suppose a stochastic representation reproduces not merely isolated Born
probabilities but the complete finite-dimensional, finite-slot,
definite-laboratory-order quantum-process interface: preparations,
instruments, adaptive controls, ancillas, sequential and tensor wiring,
discard, conditioning, and every compatible continuation. What part of that
representation is fixed by experiment?

We prove that complete continuation equivalence is a typed congruence. The
quotient of the reachable part of every adequate representation by this
congruence is naturally isomorphic to the operational quantum process
category on its image. This canonical quotient contains phase-complete
predictive states, transformations, instruments, records, and process memory.
It is substantially richer than a vector of probabilities in one preferred
basis.

We then prove a complementary no-selection theorem. Every adequate
representation can be enlarged by finite, countable, or standard-Borel
latent fibers, including preparation-correlated and dynamically evolving
variables, without changing any probability in the accepted experiment
class. Any invariant required to be natural under all admitted
representational refinements and reductions factors uniquely through the
operational quotient. This theorem does not say that all latent structure is
unreal. It says that the present experiment class cannot decide whether such
structure is coordinate gauge, empirical redundancy, or contingent but
unobserved reality.

The same analysis separates phase completeness from scalar ontology.
Complex Hilbert coordinates are not uniquely selected: exact realification
preserves every finite complex experiment when its global complex structure
and composition costs are carried. Natural real quantum theory with the
ordinary real tensor product is a different theory unless its source and
composition assumptions are correspondingly changed. Contextuality and Bell
theorems forbid a single positive, affine, universally noncontextual and
Bell-factorizable microontology under their stated premises; they do not
forbid positive contextual probability laws on actual records.

The strongest construction-level conclusion is therefore a canonical
phase-complete operational quotient with classified but unselected ontology
fibers. Registered records are invariant; one actual record may be
postulated. A preferred microscopic configuration space, a complete
microtrajectory, an actualization mechanism, time, space, and gravity are not
derived.

## 1. Question and scope

The question is:

> Across all typed ordinary-positive stochastic representations of the
> complete accepted quantum-process interface, what structure is invariant,
> and what microscopic structure remains empirically underdetermined?

There are three logically different tasks.

1. Identify the operational object fixed by every complete experiment.
2. Classify changes of representation above that object.
3. Determine whether any further physical principle selects one microscopic
   completion.

The first two tasks have exact answers in the declared domain. The third does
not acquire an answer merely because a representation is simple, finite,
Markovian, geometrically suggestive, or convenient to compute.

The domain is finite-dimensional quantum systems, a finite number of slots,
and definite laboratory control order. Explicit constructions use finite
outcomes. Countably additive instruments on standard-Borel outcome spaces
are included when all kernels and adaptive policies are measurable and
conditioning is understood almost everywhere. Indefinite-order process
matrices, continuous-variable field theory, spacetime, and gravity are not
part of the theorem.

The theorem is exact, not finite-precision. Laboratory slot order is an
external control type. It is not interpreted as emergent physical time.

## 2. The operational category and adequate representations

### 2.1 The separated operational category

Let $\mathcal Q$ be a small skeleton of the finite-dimensional,
finite-slot, definite-order quantum operational category. Objects are typed
laboratory boundaries. Arrows include preparations, completely positive
events, instruments, deterministic channels, adaptive classical control,
ancillary extension, discard, and finite process tensors with compatible
open wires.

Two arrows of the same type are equal in $\mathcal Q$ exactly when every
compatible ancillary extension, continuation, and complete reader assigns
them the same outcome distribution. Thus $\mathcal Q$ is already
operationally separated. In finite dimension a fixed, independently chosen
tomographically complete tester family witnesses this separation. The
definition, however, uses all compatible continuations and not a
candidate-dependent subset.

Sequential composition is denoted by $g\circ f$ and tensor composition by
$f\otimes g$. Convex mixing is physical classical randomization with its
setting record retained or forgotten as declared.

### 2.2 Adequate representation packet

An adequate representation is a packet

$$
R=(\mathcal S_R,J_R,K_R,\mathsf{Hist}_R,\Gamma_R,
\mathsf{Read}_R,\mathsf{Gauge}_R,\mathsf{Act}_R).
$$

It has the following properties.

1. $\mathcal S_R$ is a typed symmetric-monoidal operational structure with
   every experiment in $\mathcal Q$.
2. $J_R$ represents each operational object and arrow while preserving
   sequential and tensor wiring up to complete operational equivalence.
3. $K_R$ decodes the reachable operational image and satisfies
   $K_RJ_R\simeq\mathrm{id}_{\mathcal Q}$.
4. $\Gamma_R$ is one normalized stochastic rule for complete candidate
   histories conditional on the declared process, preparation, controls, and
   readers.
5. Every complete reader distribution equals its quantum comparator.
6. Physical mixtures are affine, and the packet respects ancillas, discard,
   ignored slots, adaptive control, and conditioning.
7. Every microscopic variable, memory, order, law parameter, and retained
   record is typed. No implementation cache or default value is exempt from
   the packet.
8. The declared gauge action acts on the complete packet and preserves every
   complete continuation profile.

For set-theoretic hygiene, the results below are schemas over small typed
representation categories inside a fixed universe. They make no claim that
the collection of every conceivable ontology is itself a small set.

### 2.3 Reachable boundaries and complete profiles

For a laboratory boundary type $A$, let $B_R(A)$ be the candidate boundary
objects reachable after admitted prefixes. For $x\in B_R(A)$ define its
complete continuation profile

$$
\Phi_R(x):(C,o)\longmapsto \Pr_R(o\mid C,x),
$$

where $C$ ranges over every compatible ancillary extension, adaptive
continuation, and complete reader and $o$ ranges over the reader's complete
outcomes.

Define

$$
x\sim_R y
\quad\Longleftrightarrow\quad
\Phi_R(x)=\Phi_R(y).
$$

The relation is typed: objects of distinct boundary type are never
identified merely because one scalar probability agrees.

The same definition applies to reachable arrows by allowing arbitrary
compatible prefixes and suffixes. Let

$$
\mathcal O_R(A)=B_R(A)/{\sim_R}
$$

and let $F_R(q)$ be the fiber of representatives over $q\in\mathcal O_R(A)$.

## 3. The canonical operational quotient

### 3.1 Congruence theorem

**Theorem 1 (complete continuation equivalence is a typed congruence).**
For every adequate representation $R$, the relation $\sim_R$ is an
equivalence relation and is preserved by every admitted sequential
composition, tensor composition, ancillary extension, convex mixture,
record map, and discard.

**Proof.** Equality of functions is reflexive, symmetric, and transitive, so
$\sim_R$ is an equivalence relation.

Let $x\sim_R y$ and let $f$ be a compatible represented continuation. Every
complete continuation $C$ after $f(x)$ defines the composite continuation
$C\circ f$ after $x$. Hence

$$
\Pr_R(o\mid C,f(x))
=\Pr_R(o\mid C\circ f,x)
=\Pr_R(o\mid C\circ f,y)
=\Pr_R(o\mid C,f(y)).
$$

Thus $f(x)\sim_R f(y)$. Prefix congruence for arrows follows by the same
argument after absorbing the prefix into the preparation.

For a compatible ancillary object $z$, every continuation after
$x\otimes z$ is already among the ancillary continuations quantified in
$\Phi_R(x)$. Therefore $x\otimes z\sim_R y\otimes z$. Applying the argument
twice gives congruence when both tensor factors vary within their classes.

Affine mixing follows from equality of the component probabilities and
linearity of physical randomization. A record map or discard is itself an
admitted continuation. Adaptive wiring causes no new case: fixing every
earlier recorded branch turns the remaining policy into a compatible
continuation, and summing over the branches preserves equality. QED.

The ancillary quantifier is essential. Without it, two maps can agree on all
unentangled probes and disagree when applied to one side of an entangled
state. A single terminal reader is equally insufficient.

### 3.2 Quotient theorem

**Theorem 2 (reachable operational-quotient theorem).** For every adequate
$R$, the quotient of its $\mathcal Q$-reachable subcategory by $\sim_R$ is
naturally isomorphic, as a convex symmetric-monoidal typed operational
category, to the corresponding reachable part of $\mathcal Q$.

**Proof.** Define

$$
\overline K_R([x]_R)=K_R(x).
$$

If $x\sim_R y$, all separating quantum testers give equal probabilities.
Because $\mathcal Q$ is operationally separated, $K_R(x)=K_R(y)$, so
$\overline K_R$ is well defined. Conversely, if $K_R(x)=K_R(y)$, adequacy
gives equal probabilities for every represented continuation and reader;
hence $x\sim_R y$. Thus $\overline K_R$ is faithful.

Every object or arrow $q$ in the declared reachable image has representative
$J_R(q)$, so the functor is full and essentially surjective on that image.
The induced inverse is

$$
\overline J_R(q)=[J_R(q)]_R.
$$

Adequacy gives

$$
\overline K_R\overline J_R=\mathrm{id},
\qquad
\overline J_R\overline K_R=\mathrm{id}
$$

on the quotient. Theorem 1 makes composition, tensoring, mixing, records,
and discard well defined, and $J_R,K_R$ preserve each of them by adequacy.
The resulting identities are natural in the typed boundary. QED.

This is an on-image theorem. It neither asserts that $J_RK_R$ is identity on
extra native states of $\mathcal S_R$ nor identifies such states
ontologically.

### 3.3 Representation spans

For two adequate representations $R$ and $R'$, their operational quotients
fit into a canonical span

$$
R\longrightarrow\mathcal Q\longleftarrow R'.
$$

This does not imply that a direct microscopic isomorphism $R\to R'$ exists.
An inverse on operational classes is not an inverse on history spaces. The
span says exactly that the two packets have the same tested image.

### 3.4 Predictive states and process memory

At a cut, a quotient state is the complete future probability functional,
not merely a one-time density or a last observed configuration. For a
memoryful process, two pasts that yield the same current reduced system state
can induce different future combs. They remain distinct in $\mathcal O_R$
whenever a continuation exposes that difference.

Thus the quotient does not Markovize an indivisible process. It identifies
only histories that agree for every licensed future.

## 4. Fiber freedom

### 4.1 A uniform latent-fiber construction

Fix an adequate $R$ and a standard-Borel space $Z$. At the successive
laboratory boundaries of a finite program $P$, choose normalized measurable
kernels

$$
\nu_P(dz_0\mid h_0),
\qquad
L_{P,k}(dz_k\mid z_{k-1},h_{\leq k}),
$$

where each kernel may depend on the declared preparation and the realized
prefix but not on an unperformed future setting. Define

$$
\Gamma_R^Z(dh,dz_0\cdots dz_n\mid P)
=\Gamma_R(dh\mid P)\nu_P(dz_0\mid h_0)
\prod_{k=1}^{n}L_{P,k}(dz_k\mid z_{k-1},h_{\leq k}).
$$

All readers inherited from $R$ ignore $Z$. Normalization of the kernels and
iterated integration give

$$
\int_{Z^{n+1}}\Gamma_R^Z(dh,dz_0\cdots dz_n\mid P)
=\Gamma_R(dh\mid P).
$$

Sequential composition uses the same prefix kernels and passes the terminal
$z_k$ into the next typed segment. Tensor composition uses the declared
product kernel for independently prepared fibers unless a correlated fiber is
itself declared. The kernel assignment is affine under physical mixtures and
monoidal under independently controlled tensor products. Standard-Borel
measurability gives the iterated measure; for the finite controls no extension
theorem is needed.

**Theorem 3 (fiber inflation).** Every adequate representation has adequate
finite, countable, and standard-Borel fiber inflations with exactly the same
registered operational quotient.

**Proof.** The construction above is normalized and uses one fixed rule per
typed program. Marginalization returns every original history law, hence all
reader probabilities, mixtures, compositions, and conditionings. The
projection that forgets $Z$ intertwines the operational packets. QED.

### 4.2 Four exact inflations

**Static hidden bit.** Take $Z=\{0,1\}$, choose a fixed Bernoulli law, and set
$z_k=z_0$. The two values change the asserted microscopic history but no
continuation profile.

**Preparation-correlated idle variable.** Under a declared preparation
interface that forgets the implementation label, let $z_0$ record which of two
operationally equivalent preparation procedures was used and carry it
unchanged. Physical randomization produces the corresponding affine mixture
of $z_0$ laws. This is a preparation-contextual completion. Deleting it is not
an invertible coordinate transformation even though it preserves that
interface. If the implementation label is itself a registered record, the
preparations are not operationally equivalent and this control does not
apply.

**Different latent dynamics.** On the same bit fiber compare

$$
L^{\mathrm{hold}}(z_k\mid z_{k-1},h_{\leq k})
=\delta_{z_k,z_{k-1}}
$$

with

$$
L^{\mathrm{flip}}(z_k\mid z_{k-1},h_{\leq k})
=\delta_{z_k,z_{k-1}\oplus b(h_k)},
$$

where $b(h_k)$ is a fixed recorded prefix bit. Their microscopic temporal
correlations differ. Their complete registered pushforwards are identical.

**Mutually singular continuum laws.** Take $Z=[0,1]$. One adequate
inflation uses Lebesgue measure and another uses the Cantor probability
measure, with $z$ carried unchanged. The measures are mutually singular, yet
every inherited operational prediction agrees exactly.

These controls do not assign a distribution to a variable absent from the
packet. Each inflation explicitly introduces its variable and law before it
is used.

### 4.3 Reduction and future readability

The projection

$$
\pi_Z:(h,z_0,\ldots,z_n)\longmapsto h
$$

is a probability-preserving reduction. It is generally many-to-one and is
therefore not a coordinate isomorphism.

If a later experiment adds a calibrated reader $D_Z$ with different outcome
statistics for different $z$, then $D_Z$ enlarges the operational domain.
The former fiber splits into new operational classes. The variable has become
physical relative to the enlarged interface. There is no contradiction: an
equivalence relation is always indexed by its experiment class.

## 5. The no-selection theorem and the gauge taxonomy

### 5.1 Representation morphisms

Let $\mathbf{Rep}(\mathcal Q)$ be the category whose objects are adequate
representations and whose arrows preserve the typed operational decoder,
history pushforwards, records, sequential and tensor wiring, while declaring
whether microscopic data are relabelled, refined, or forgotten. For the
present theorem it is enough to use the wide subcategory generated by:

- complete-packet isomorphisms;
- the explicit fiber inflations of Section 4; and
- their probability-preserving projections.

Let $R_{\mathrm{op}}$ be the record-only adequate representation obtained by
retaining the operational class and the actual setting/outcome records while
forgetting unobserved microscopic coordinates. Theorem 2 and the physical
record map give a morphism

$$
\pi_R:R\longrightarrow R_{\mathrm{op}}.
$$

The map is an ontological forgetting map, not an asserted identity of worlds.

### 5.2 Universal factorization

Let $X$ be any fixed target set, measurable space, ordered set, or category.
A representation-natural invariant is a family of maps

$$
I_R:B_R(A)\longrightarrow X
$$

that is natural under every admitted representation morphism. In particular,

$$
I_{R'}(T x)=I_R(x)
$$

for every admitted $T:R\to R'$. Requiring robustness under both fiber
inflation and reduction is a substantive invariance criterion; it is not
silently inferred from empirical adequacy.

**Theorem 4 (operational no-selection and factorization).** Every
representation-natural invariant robust under the admitted fiber refinements
and reductions is constant on each operational fiber and factors uniquely
through the operational quotient:

$$
I_R=\overline I\circ\pi_R.
$$

Conversely, every invariant $\overline I$ of the operational quotient pulls
back to such a family.

**Proof.** Naturality with respect to $\pi_R$ gives

$$
I_R(x)=I_{R_{\mathrm{op}}}(\pi_Rx).
$$

If $x\sim_Ry$, then $\pi_Rx=\pi_Ry$, so $I_R(x)=I_R(y)$. Define
$\overline I([x])=I_R(x)$. This is well defined and unique because $\pi_R$
is surjective on the reachable quotient. Conversely, if $\overline I$ is
defined on the quotient, then $I_R=\overline I\pi_R$ is unchanged by any
morphism commuting with the quotient maps. QED.

The theorem is intentionally conditional. A proposed physical quantity that
changes under a fiber reduction is not disproved; it simply is not selected
by the operational interface plus the stated representation-invariance
criterion. To promote it, one must supply an independent principle or an
experiment that refuses the reduction.

### 5.3 What the theorem does not say

It does not prove that:

- all microscopic completions are physically equivalent;
- every hidden variable is gauge;
- nature realizes the quotient and nothing else;
- the shortest completion is most likely;
- a uniform measure exists on the class of completions; or
- empirical underdetermination is evidence for a particular interpretation.

There is no coordinate-free uniform distribution on an arbitrary fiber
without a base measure. Maximum entropy is equally relative to the chosen
variables and constraints. Kolmogorov complexity changes with the description
language. None is a physical selector until independently justified.

### 5.4 Five-way classification

| Case | Mathematical relation | Physical conclusion available now |
|---|---|---|
| coordinate gauge | invertible automorphism of the complete packet, preserving all declared beables and laws | one physical description in different coordinates |
| dilation presentation gauge | unitary or isometric change of an inaccessible dilation presentation within a fixed minimality class | one represented channel; no new observed fact |
| empirical redundancy | noninvertible forgetting map preserving the frozen interface | distinction is presently unidentifiable |
| contingent hidden structure | extra asserted variable and law with no present reader | possible ontology, not selected or refuted |
| physical difference | some fixed extended preparation, intervention, or reader changes a prediction | distinct theories in that enlarged domain |

The second row has restricted exact theorems. If

$$
\mathcal E(\rho)=\sum_\alpha K_\alpha\rho K_\alpha^\dagger
$$

and

$$
K'_\beta=\sum_\alpha u_{\beta\alpha}K_\alpha
$$

for an isometry $u$, then the channel is unchanged. If the Kraus label is not
a physical record, this is presentation freedom. If the label is read, the
fine-grained instruments differ and may not be identified.

Minimal Stinespring dilations of one completely positive map are unique up to
an environment unitary at finite dimension. A padded dilation contains an
additional idle environment and is connected to the minimum by an isometry,
not by a unique ontological identification. Minimality inside this class does
not prove that the environment is nature's microscopic state space.

## 6. The phase-complete operational residue

### 6.1 Predictive-state theorem

For a finite-dimensional boundary, define a predictive state by its affine
functional on every compatible future effect. For ordinary quantum states,

$$
\omega_\rho(E)=\operatorname{tr}(\rho E).
$$

**Theorem 5 (phase-complete predictive state).** If

$$
\operatorname{tr}(\rho E)=\operatorname{tr}(\sigma E)
$$

for every effect $0\leq E\leq I$, then $\rho=\sigma$. At a process cut, the
analogous complete tester functional determines the operational process
class. Consequently a diagonal probability vector in one fixed configuration
basis is not a sufficient predictive state for the full continuation domain.

**Proof.** Effects linearly span the Hermitian operators in finite dimension.
Taking the difference $D=\rho-\sigma$, the hypothesis gives
$\operatorname{tr}(DE)=0$ on a spanning set and hence on every Hermitian
operator. Choosing $E$ from the positive and negative spectral parts of $D$
gives $D=0$. The process statement applies the same separating argument to a
tomographically complete family of positive process testers. QED.

An exact two-state control makes the phase content visible. Let

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
$$

Their diagonals in the $Z$ basis are both $(1/2,1/2)$. After a Hadamard,
$|+\rangle$ yields $0$ with certainty and $|-\rangle$ yields $1$ with
certainty. The common continuation separates them.

The phase family

$$
U_\phi=|0\rangle\langle0|+e^{i\phi}|1\rangle\langle1|
$$

satisfies

$$
U_\phi U_\theta=U_{\phi+\theta}.
$$

Any adequate representation must reproduce this full circle and its action
under common continuations. It need not represent the circle by fundamental
complex numbers, but it cannot discard the corresponding composition data.

### 6.2 Exact realification

Write a complex matrix $M=A+iB$, with real $A,B$, and define

$$
\mathfrak R(M)=
\begin{pmatrix}
A&-B\\
B&A
\end{pmatrix}.
$$

Then

$$
\mathfrak R(MN)=\mathfrak R(M)\mathfrak R(N),
\qquad
\mathfrak R(M^\dagger)=\mathfrak R(M)^T.
$$

For a complex density operator and effect set

$$
\rho_{\mathbb R}=\frac12\mathfrak R(\rho),
\qquad
E_{\mathbb R}=\mathfrak R(E).
$$

They are real positive operators with the correct normalization on the
encoded sector, and

$$
\operatorname{tr}_{\mathbb R}(\rho_{\mathbb R}E_{\mathbb R})
=\operatorname{tr}_{\mathbb C}(\rho E).
$$

The real space carries the distinguished operator

$$
J=
\begin{pmatrix}
0&-I\\
I&0
\end{pmatrix},
\qquad
J^2=-I.
$$

The real matrices representing complex-linear maps commute with $J$.
Realification therefore removes complex coordinates while retaining an
equivalent complex structure.

### 6.3 Composition is where the cost lives

For separate complex systems $A$ and $B$,

$$
\dim_{\mathbb R}\mathfrak R(\mathcal H_A\otimes_{\mathbb C}\mathcal H_B)
=2d_Ad_B,
$$

whereas the ordinary tensor product of separately realified carriers has
dimension $4d_Ad_B$. In general

$$
\mathfrak R(M_A\otimes_{\mathbb C}M_B)
\neq
\mathfrak R(M_A)\otimes_{\mathbb R}\mathfrak R(M_B).
$$

An equivalent real simulation must therefore constrain or correlate the
extra phase carriers, use a global complex structure, or modify the
composition rule. Natural real quantum theory with the unrestricted ordinary
real tensor product is not just a coordinate change of complex quantum
theory.

This resolves an apparent conflict between two network claims. A test that
assumes independently prepared sources are represented by real product states
can distinguish natural real quantum theory. A simulation that requires only
operational independence may use real states that are locally uncorrelated
yet not product states in the unrestricted real tensor product. Under that
different premise, finite complex networks and sequential protocols admit a
real representation. The two claims compare different source-independence
contracts.

**Corollary 5.1.** The accepted operational interface forces a
phase-complete predictive structure, but does not select complex scalars as
fundamental ontology. Exact real representations exist with explicit global
structure and composition costs. Conversely, real coordinates do not make
phase-complete structure eliminable.

### 6.4 Reconstruction assumptions are inputs

Complex quantum theory can be selected inside broader probabilistic
frameworks by adding assumptions such as homogeneous self-dual state cones,
Jordan structure, local tomography, a compatible composite rule, and the
existence of a qubit. Those are powerful conditional reconstruction
theorems. They are not consequences of operational adequacy alone.

Quaternionic and other Jordan models are likewise comparators only after
their composite systems and tester domains are fixed. No scalar field is
promoted here by historical familiarity.

## 7. Positivity and generalized contextuality

### 7.1 Three levels of positivity

The following claims are distinct.

1. Every actually registered outcome has a nonnegative probability.
2. One chosen quasiprobability frame represents all states and effects
   nonnegatively.
3. One fixed ontic sample space represents preparations, transformations,
   and measurements by nonnegative affine objects that depend only on their
   complete operational equivalence classes.

The accepted record-history representation satisfies the first claim. Frame
and generalized-contextuality theorems obstruct combinations of the second
and third. They do not turn an actual probability negative.

### 7.2 Preparation-contextuality witness

Consider the two-bit parity-oblivious multiplexing task. Alice receives
$x=(x_1,x_2)\in\{0,1\}^2$ uniformly and prepares

$$
\rho_x=\frac12\left[
I+\frac{(-1)^{x_1}X+(-1)^{x_2}Z}{\sqrt2}
\right].
$$

Bob receives $y\in\{1,2\}$ uniformly, measures $X$ for $y=1$ and $Z$ for
$y=2$, and guesses $x_y$. The quantum success probability is

$$
p_{\mathrm Q}=\frac12\left(1+\frac1{\sqrt2}\right)>\frac34.
$$

The even- and odd-parity mixtures are operationally identical:

$$
\frac12(\rho_{00}+\rho_{11})
=\frac12(\rho_{01}+\rho_{10})
=\frac I2.
$$

In a preparation-noncontextual affine ontological model, the corresponding
ontic mixtures must also be equal. Conditional on any ontic state $\lambda$,
write the posterior probabilities as
$a,b,c,d$ for $00,01,10,11$. Parity obliviousness implies

$$
a+d=b+c=\frac12.
$$

The best mean probability of guessing either requested bit is

$$
s_\lambda=\frac12\left[
\max(a+b,c+d)+\max(a+c,b+d)
\right]\leq\frac34.
$$

To see the bound, set $d=1/2-a$ and $c=1/2-b$. The two maxima become
$1/2+|a+b-1/2|$ and $1/2+|a-b|$. For
$0\leq a,b\leq1/2$,

$$
|a+b-1/2|+|a-b|\leq\frac12.
$$

Averaging over $\lambda$ preserves the bound. The quantum value therefore
witnesses preparation contextuality under affine mixing and the stated
operational equivalence.

### 7.3 Transformation-contextuality witness

Let $T_\theta$ be qubit rotation by angle $\theta$ about the Bloch $y$ axis,
and let $T$ project the Bloch vector onto that axis. Quantum theory has five
convex decompositions of the same channel:

$$
T=\frac12(T_0+T_\pi)
=\frac12(T_{\pi/3}+T_{4\pi/3})
=\frac12(T_{2\pi/3}+T_{5\pi/3}),
$$

and

$$
T=\frac13(T_0+T_{2\pi/3}+T_{4\pi/3})
=\frac13(T_{\pi/3}+T_\pi+T_{5\pi/3}).
$$

Assume affine transformation noncontextuality, so one transition kernel
$\Gamma$ represents $T$ and one kernel $\Gamma_k$ represents each rotation
$T_{k\pi/3}$. Apply them to an ontic distribution representing a pure state
in the $xz$ plane, and call the resulting densities $\mu$ and $\mu_k$.
Opposite rotations produce orthogonal quantum states, so perfect
distinguishability requires

$$
\mu_k(\lambda)\mu_{k+3}(\lambda)=0
$$

almost everywhere. Affinity transfers all five channel decompositions to
the densities.

At any $\lambda$ with $\mu(\lambda)>0$, set
$r_k=\mu_k(\lambda)/\mu(\lambda)$. The three half-mixtures imply

$$
r_0+r_3=r_1+r_4=r_2+r_5=2.
$$

Disjointness forces each opposing pair to be $(2,0)$ or $(0,2)$. But the
three-way decompositions require

$$
r_0+r_2+r_4=3,
\qquad
r_1+r_3+r_5=3.
$$

Each left side must be an even integer, contradiction. Thus a nonnegative
affine transformation kernel cannot be both adequate and transformation
noncontextual for this operational fragment.

### 7.4 Immediate effects do not define transformations

A single-outcome identity channel and a single-outcome $Z$ conjugation both
have immediate effect $I$: their outcome occurs with probability one for
every input. They are not operationally equivalent transformations. On input
$|+\rangle$, a later $X$ measurement distinguishes them with certainty.

This control explains why transformation equivalence must quantify over
complete continuations. Apparatus labels are not allowed to create a
difference when complete profiles agree, but channel disturbance is not
discarded merely because an immediate POVM effect agrees.

### 7.5 Peres--Mermin control

Consider the commuting rows and columns of

$$
\begin{pmatrix}
X\otimes I&I\otimes X&X\otimes X\\
I\otimes Y&Y\otimes I&Y\otimes Y\\
X\otimes Y&Y\otimes X&Z\otimes Z
\end{pmatrix}.
$$

Each row product is $+I$. The first two column products are $+I$ and the
last is $-I$. A context-independent deterministic assignment of values
$v(A)\in\{+1,-1\}$ respecting products of commuting observables would give
$+1$ when all row equations are multiplied and $-1$ when all column
equations are multiplied. Both products contain every assigned value twice,
so this is impossible.

The conclusion uses sharp outcome determinism, measurement
noncontextuality, and the commuting functional-product rule. It does not
show that a contextual positive history law is impossible.

## 8. Bell locality and the full premise theorem

### 8.1 Exact CHSH control

Let two independently chosen settings be $x,y\in\{0,1\}$ and outcomes be
$a,b\in\{+1,-1\}$. A measurement-independent Bell-factorizable completion
has

$$
p(a,b\mid x,y)=\int_\Lambda
\mu(d\lambda),p_A(a\mid x,\lambda)p_B(b\mid y,\lambda),
$$

with $\mu$ independent of $x,y$. Define conditional means

$$
A_x(\lambda)=\sum_a a,p_A(a\mid x,\lambda),
\qquad
B_y(\lambda)=\sum_b b,p_B(b\mid y,\lambda),
$$

so $|A_x|,|B_y|\leq1$. Pointwise,

$$
\left|A_0(B_0+B_1)+A_1(B_0-B_1)\right|\leq2.
$$

Integration gives the CHSH inequality

$$
|S|\leq2,
$$

where

$$
S=\langle A_0B_0\rangle+\langle A_0B_1\rangle
+\langle A_1B_0\rangle-\langle A_1B_1\rangle.
$$

For a singlet and coplanar measurement axes separated by the standard
$45$-degree choices, quantum theory gives

$$
|S|=2\sqrt2.
$$

The contradiction is with the conjunction of measurement independence and
Bell factorization. No-signalling alone does not imply either premise.

### 8.2 Premise theorem

**Theorem 6 (noncontextual and Bell-local completion cost).** The complete
finite quantum operational category admits no one ontological model on a
fixed measurable space $\Lambda$ satisfying all of the following at once:

1. nonnegative affine preparation distributions;
2. nonnegative normalized measurement responses;
3. nonnegative affine transformation kernels;
4. preparation noncontextuality;
5. measurement noncontextuality together with the sharp-product premises in
   the Peres--Mermin fragment;
6. transformation noncontextuality;
7. compatible tensor composition for independently controlled preparations;
8. measurement independence in the Bell fragment; and
9. Bell factorization.

**Proof.** Section 7.2 contradicts items 1 and 4 with affine mixture
preservation. Section 7.3 independently contradicts items 3 and 6 with
perfect distinguishability. Section 7.5 contradicts item 5. Section 8.1
contradicts items 8 and 9. Any one contradiction defeats the conjunction.
QED.

The theorem is a premise classifier, not a proof that ordinary probability
fails. A positive whole-program record model can retain preparation and
transformation context in its microscopic history, and its bipartite history
need not factorize through separate local ontic responses. That is where its
cost resides.

### 8.3 Negativity is representation-relative

In an affine frame representation, one seeks functions
$\mu_\rho(\lambda)$ and $\xi_E(\lambda)$ such that

$$
\operatorname{tr}(\rho E)
=\int_\Lambda\mu_\rho(\lambda)\xi_E(\lambda),d\lambda
$$

while states, effects, transformations, and convex mixtures all share one
noncontextual representation. Full quantum theory forces negativity or a
deformation of this classical calculus under the frame hypotheses. The
record-history construction avoids the conclusion by being contextual at the
procedure and whole-program level. Its actual record probabilities remain in
$[0,1]$.

## 9. Resource minima and their domains

### 9.1 Hilbert and dilation resources

For a finite-dimensional completely positive map $\mathcal E$, the Choi rank
equals the minimum number of Kraus operators and the minimum environment
dimension of a Stinespring dilation, after the input and output Hilbert spaces
and dilation class are fixed. Minimal dilations are unique up to an
environment isometry, unitary when both are minimal.

These are exact restricted-class invariants. Fiber inflation makes the
microscopic state space arbitrarily larger without changing the channel. The
Choi rank therefore does not become a universal ontic dimension.

### 9.2 Statistical sufficiency

A statistical experiment is a parameter-indexed family of states. Relative
to completely positive postprocessings and a common parameter set, finite or
normal von Neumann-algebraic experiments admit precise sufficiency and
minimal-sufficiency relations. Under the hypotheses of the relevant
theorems, a minimal sufficient experiment is unique up to the stated normal
isomorphism or randomization equivalence.

This supplies a canonical predictive compression for a frozen decision
problem. It does not select which latent variables exist outside the
experiment. Changing the parameter family or allowed future tasks can change
the minimum.

### 9.3 Process memory

For a finite quantum comb $W$ and a fixed typed cut $D$, define

$$
m_D(W)=\min\{\dim M:\ M\text{ is a Hilbert memory crossing }D
\text{ in an exact causal realization of }W\}.
$$

A finite realization exists, and the nonempty set of admissible positive
integer dimensions has a least member. Thus $m_D(W)$ is well defined and
achieved in this class. Choi ranks and operator-factorization ranks provide
exact bounds in specified subclasses; no universal closed formula is claimed
here. The affine dimension of the complete predictive state space is likewise
an invariant of the decoded operational object. For a $d$-level quantum state
it is $d^2-1$, while process-boundary dimensions depend on the fixed tester
profile.

These are minima among representations obeying the same cut, tensor,
future-task, and Hilbert-channel rules.

A non-Markovian stochastic history can encode the same predictions in its
whole past rather than in a finite present-state carrier. Conversely, an
arbitrarily padded Markov state can carry redundant memory. Process-memory
dimension is therefore not representation-universal without a declared
Markov and state-sufficiency contract.

The analogous minimum classical latent memory is meaningful after fixing
Markov order, contextuality allowances, exact precision, and the input family.
Changing any of those resources changes the optimization problem.

### 9.4 Markovian ontological dimension

For an $N$-dimensional Hilbert system, a known lower bound of $2N-2$
continuous variables applies to a broad class of Markovian ontological
models with the stated regularity and dynamical assumptions. The bound is
important precisely because its assumptions are strong. It does not apply to
the non-Markovian fiber constructions of Section 4 or to an ontology whose
state is the complete history.

### 9.5 Real-coordinate overhead

Single-system realification doubles the carrier dimension. Separately
realifying many systems with the ordinary real tensor product introduces
additional sectors unless a shared complex structure or correlated source
rule is imposed. This is a representation and composition cost. It is not a
proof that complex numbers are substances.

### 9.6 Resource-classification theorem

**Theorem 7 (restricted minima versus universal ontology).** Decoded Choi
rank, minimal Stinespring dimension, minimal sufficient experiments, and
fixed-cut comb-memory minima are genuine operational invariants when their
channel, task, cut, and representation class are held fixed. They factor
through the quotient in exactly that restricted sense. Their values do not
equal the size of every adequate microscopic realization. Markovian ontic
dimension and realification overhead are additionally conditional on their
Markov and composition classes. Consequently none selects a universal
microscopic ontology from the accepted interface.

**Proof.** The restricted minima are functions of the decoded quantum
channel, experiment, or comb, so equal operational classes have equal values.
But given any realization attaining one such minimum, Theorem 3 appends a
nontrivial idle fiber while preserving the decoded object and increasing the
realized microscopic state space or memory. Projection removes that fiber.
Thus the operational minimum survives, while the assertion that every
adequate ontology literally has that minimum size does not. The Markovian and
real-composition quantities are not even defined until their extra class
assumptions are fixed. QED.

Computational complexity and description length are also representation
relative. They may guide engineering, but do not become laws of nature
without an independently fixed coding and physical principle.

## 10. Records, divisions, and actuality

### 10.1 Operational records descend

A physical record is a typed outcome variable with a calibrated future
reader that distinguishes its values. If $r\neq r'$, there is a continuation
$C$ and outcome $o$ such that

$$
\Pr(o\mid C,r)\neq\Pr(o\mid C,r').
$$

Therefore $r$ and $r'$ lie in different operational classes. Representation
morphisms preserve the record probabilities, so the record event descends to
the canonical quotient.

Removing one diagnostic reader does not by itself erase the record from
nature. It changes the chosen experiment domain. A record claim is tied to a
physical reader family fixed independently of the quotient calculation.

### 10.2 Division boundaries are predictive, not microscopic by default

A boundary is an operational division for a declared future task family only
when its complete quotient state is sufficient for every future in that
family. In probabilistic notation, if $Z_D$ is the complete boundary
argument, then

$$
Z_D(H_1)=Z_D(H_2)
\Longrightarrow
\Pr(F\mid H_1)=\Pr(F\mid H_2)
$$

for every licensed future $F$. A local record may be stable without being a
complete division boundary. Hidden fiber variables cannot be smuggled into
$Z_D$ after a failure is found.

### 10.3 Actual record versus microtrajectory

The claim that one registered record history actually occurs can be added as
an actuality postulate. Let $h_{\mathrm{rec}}$ be that history. An adequate
representation can have many microscopic histories in the fiber

$$
\pi_H^{-1}(h_{\mathrm{rec}}).
$$

Neither normalization nor decoherence chooses one member of this fiber.
Therefore

$$
\mathrm{actual\ record}
\nRightarrow
\mathrm{selected\ complete\ microtrajectory}.
$$

**Theorem 8 (record invariance and microscopic actuality gap).** Registered
record distinctions and their operational probabilities are invariant under
adequate representation morphisms. One actual record history may be
postulated at quotient level. No unique microscopic completion or
actualization mechanism is determined by the accepted interface.

**Proof.** Record invariance follows from preservation of complete reader
probabilities. The fiber constructions in Section 4 attach distinct
microscopic histories to every record without changing those probabilities.
Theorem 4 then prevents any representation-natural selector from depending
on the added fiber. QED.

### 10.4 Syntax is not time or space

Reordering independent instructions in a program serialization does not
create a physical chronology. A slot order is part of the laboratory type and
is consumed by the process theorem; it is not derived. Likewise a tensor
factor is an independently controlled system type, not a spatial region.
No discrete latent fiber is introduced here as a candidate spacetime atom.

## 11. The Barandes correspondence boundary

An indivisible stochastic model in the relevant sense asserts more than a
positive operational record law. It specifies a fixed configuration space as
kinematics, contingent standalone probabilities, and indivisible transition
laws at declared division events. A system ultimately follows one trajectory,
while the minimalist law may admit many compatible non-Markovian realizers.

The present analysis agrees with four important points.

1. Hilbert-space variables need not be fundamental beables.
2. Ordinary probability can underlie quantum operational statistics.
3. Indivisible dynamics need not factor through every intermediate cut.
4. A first-order indivisible law can leave its non-Markovian realizer
   underdetermined.

But operational representation is not ontological reconstruction.

**Theorem 9 (Barandes boundary).** The positive record-history
representation supplies an operational representation of indivisible
quantum behavior. The canonical quotient fixes neither a preferred complete
configuration space nor one complete configuration trajectory. Therefore a
Barandes-style configuration ontology is represented as an admissible
completion but remains unselected by the present experiment class.

The conclusion is neither `reconstructed` nor `refuted`. To reconstruct the
ontology one would need an independently fixed configuration referent, its
complete stochastic law, and a discriminator or principle that rejects the
other adequate fibers. To refute it one would need a no-go for every such
completion, not merely for a Markovian, noncontextual, or finite-dimensional
subclass.

Preparation-independence theorems and Markovian dimension bounds do not close
this gap. The former add a factorization premise on independently prepared
ontic states; the latter add Markovian evolution and regularity. Their
conclusions remain valuable but conditional.

## 12. Discriminator ledger

No exact operational equivalence can be broken by reanalyzing the same
probabilities. The following ledger prices the surviving differences.

| Competing packets | Shared domain | Differing physical claim | Required discriminator or principle | Present result |
|---|---|---|---|---|
| record model and hidden-bit inflation | complete finite quantum experiments | an idle binary fact exists | a calibrated intervention or reader coupled to the bit | none in domain; underdetermined |
| Lebesgue and Cantor fiber models | same | mutually singular continuous microstate law | a fiber-sensitive preparation or readout fixed before comparison | none in domain; underdetermined |
| hold and flip latent dynamics | same | different microscopic temporal correlations | expose $Z$ at two or more boundaries without changing the law afterward | none in domain; underdetermined |
| minimal and padded Stinespring packets | same decoded channel | additional environment is physical | independent environment access or a law forbidding padding | restricted minimum only |
| complex and realified packets | finite protocols with the same operational independence | scalar/carrier ontology differs | fix composition, source independence, and local access identically, then test | no scalar selection in present domain |
| two non-Markovian realizers | same indivisible operational law | different unrecorded trajectory probabilities | a reader of unrecorded cuts or a separately justified realization law | none in domain; underdetermined |
| quotient-only and configuration-space ontology | same registered records | complete configurations exist at every boundary | a configuration-sensitive intervention or independently derived configuration principle | represented, not selected |
| distinct actualization laws | same normalized probabilities | different event becomes actual | an exact probability or structural prediction beyond normalization | no mechanism supplied |

If any proposed discriminator is admitted later, its preparation, coupling,
reader, calibration, and predicted difference are new physical inputs. They
must be fixed before the competing models are compared.

## 13. Registered controls

| ID | Exact control | Result |
|---|---|---|
| C1 | positive record-history representation | Theorem 2 returns its complete decoded quantum process, not its dilation coordinates |
| C2 | static hidden bit | Theorem 3 doubles the microscopic fiber with zero change in any continuation profile |
| C3 | hidden continuum | Lebesgue and Cantor fiber laws are mutually singular and operationally identical |
| C4 | latent dynamics mutation | hold and prefix-controlled flip kernels have different correlations and the same pushforward |
| C5 | Kraus rotation | isometric Kraus mixing changes fine labels but not the unrecorded CP map |
| C6 | minimal versus padded Stinespring | the restricted minimum is exact; padding is not thereby a false ontology |
| C7 | equal density, different preparations | parity-even and parity-odd mixtures both give $I/2$ while preparation noncontextuality yields the $3/4$ bound |
| C8 | equal immediate effect, different channel | identity and $Z$ conjugation both have effect $I$ but a later $X$ reader distinguishes them |
| C9 | Peres--Mermin | five positive and one negative commuting-product constraints forbid one context-independent sharp value table |
| C10 | CHSH | measurement independence plus Bell factorization gives $2$, quantum theory gives $2\sqrt2$ |
| C11 | full phase circle | $U_\phi U_\theta=U_{\phi+\theta}$ and the Hadamard continuation reject a diagonal-only state |
| C12 | complex versus real | exact realification preserves probabilities while exposing the shared-$J$ and tensor costs |
| C13 | process memory | complete future combs, not current reduced states, define the predictive quotient |
| C14 | reader removal | changing the reader family changes the domain; a diagnostic reader does not retroactively define ontology |
| C15 | program-order permutation | serialization of independent instructions is not a physical time observable |
| C16 | actual record, absent microtrajectory | the actual record class has arbitrarily many adequate microscopic completions |
| C17 | fiber made readable | an independently calibrated $Z$ reader splits the old fiber in the enlarged domain |
| C18 | simplicity selector | coordinate-dependent description length supplies no invariant probability or physical law |

## 14. Hostile-attack disposition

### 14.1 Quotient and category attacks

1. **One terminal reader.** Rejected. The definition quantifies over every
   typed ancillary continuation and complete reader.
2. **No ancillary continuations.** Rejected. Ancillas are explicit in
   $\Phi_R$ and are used in the tensor congruence proof.
3. **Post-selected tomography.** Rejected. Separation is fixed by the
   operational category before a candidate representation is chosen.
4. **Injectivity called equivalence.** Rejected. Theorem 2 proves
   well-definedness, faithfulness, fullness, and essential surjectivity on the
   declared reachable image.
5. **Tensor or adaptive wiring omitted.** Rejected by Theorem 1's ancillary
   and branchwise arguments.
6. **Different types merged by equal scalars.** Rejected. Equivalence is
   defined separately at each boundary and arrow type.
7. **Diagnostic-reader dependence.** Rejected. The reader family is the
   independently fixed physical experiment domain, not a reader chosen to
   produce a desired quotient.
8. **On-image inverse called global.** Accepted as a scope warning. The
   natural isomorphism is only on the $\mathcal Q$-reachable quotient; extra
   native objects need not have inverses.

### 14.2 Fiber and gauge attacks

9. **Every idle variable called gauge.** Rejected by the five-way taxonomy;
   noninvertible deletion is not coordinate gauge.
10. **Every idle variable called physical.** Rejected as selection without a
    discriminator. Contingent physicality remains an open option.
11. **Uniform fiber measure.** Rejected unless a base measure is independently
    given.
12. **Maximum entropy after coordinates.** Rejected because the variables and
    constraints already select the answer class.
13. **Preparation-correlated data deleted as gauge.** Rejected. The projection
    is many-to-one and only operationally sufficient in the frozen domain.
14. **Future setting hidden in the latent state.** Rejected. Fiber kernels
    depend only on the declared preparation and realized prefix.
15. **Default law for an absent variable.** Rejected. Every inflation
    explicitly introduces $Z$ and its normalized law.
16. **Growing hidden memory called one fixed rule.** Rejected. $Z$ and its
    typed update family are fixed uniformly before the finite program; no
    experiment-specific lookup table is introduced.

### 14.3 Phase and scalar attacks

17. **Diagonal probabilities retained alone.** Killed by the $|+\rangle$,
    $|-\rangle$, Hadamard control.
18. **Global complex carrier hidden in real coordinates.** Rejected. The
    operator $J$, doubled carrier, encoded sector, and composition rule are
    printed.
19. **Different source assumptions compared.** Rejected. Product-state and
    operational source independence are separated explicitly.
20. **Local tomography silently assumed empirical.** Rejected. It is an
    additional composition postulate unless separately bound by experiment.
21. **Complex coordinates called fundamental.** Rejected by exact
    realification.
22. **Phase structure called eliminable.** Rejected because realification
    retains $J$ or an equivalent global constraint.
23. **Wigner uniqueness used outside its hypotheses.** Not used. No scalar
    conclusion is inferred from transition-probability symmetries alone.
24. **Reconstruction postulates counted as results.** Rejected. Jordan,
    homogeneity, self-duality, local tomography, and qubit assumptions remain
    inputs to the conditional comparator theorem.

### 14.4 Context, locality, and resource attacks

25. **Positive records imply noncontextuality.** Rejected by Sections 7--8.
26. **No-signalling implies Bell locality.** Rejected by the CHSH premise
    ledger.
27. **Context hidden as evaluator metadata.** Rejected. Procedures and
    microscopic context are fields of the adequate packet; operationally
    equivalent procedures are identified only in the quotient.
28. **Minimal dilation equals ontic dimension.** Rejected. It is a minimum in
    the fixed Stinespring class.
29. **Markov lower bound applied to non-Markov realizers.** Rejected. The
    Markov hypothesis is retained at every use.
30. **Computational complexity selects ontology.** Rejected without a
    physical coding and selection law.
31. **Finite precision merges exact states.** Rejected. Equivalence is exact.
32. **One process-memory realization is unique.** Rejected. Only restricted
    minimality, up to its declared equivalence, is claimed.

### 14.5 Actuality and downstream-smuggling attacks

33. **Actual record becomes a microtrajectory.** Rejected by Theorem 8.
34. **Normalization becomes actualization.** Rejected. Normalization assigns
    weights and selects no outcome.
35. **Decoherence becomes outcome selection.** Rejected. Decoherence can make
    records stable without choosing the actual branch.
36. **Program slot becomes time.** Rejected. Definite laboratory order is an
    input type.
37. **Tensor factor becomes spatial region.** Rejected. It is only an
    independently controlled system type.
38. **Hidden order inserted for a successor.** Rejected; no microscopic order
    is added.
39. **Discrete fiber inserted as spacetime.** Rejected; the finite bit is a
    nonidentifiability control only.
40. **Empirical equivalence becomes evidence for this ontology.** Rejected.
    Equivalence proves adequacy, not truth.
41. **Underdetermination proves all ontologies equally good.** Rejected.
    Other physical principles may discriminate; none has been supplied here.
42. **New postulate after the no-go.** Rejected. Every proposed extension is
    left in the discriminator ledger and not used to alter the result.

## 15. Quantifier and resource ledger

| Result | Domain | Exact quantifier | Kind | Enlarged-domain sensitivity |
|---|---|---|---|---|
| Theorems 1--2 | finite-dimensional, finite-slot, definite-order reachable category; standard-Borel measurable extension | every adequate representation in the fixed schema | mathematical and operational | new readers refine the quotient |
| Theorem 3 | every adequate representation and any fixed finite, countable, or standard-Borel fiber | existence of infinitely many refinements for each $R$ | mathematical | fiber-sensitive readers defeat equivalence |
| Theorem 4 | invariants natural under the explicitly admitted refinement/reduction category | every such invariant | mathematical no-selection | a new principle may refuse a reduction |
| Theorem 5 | finite states and complete finite-process testers | every compatible effect/tester | operational | a smaller tester family gives a coarser quotient |
| Theorem 6 | the explicit POM, rotation, Peres--Mermin, and CHSH fragments | no one model satisfying the listed conjunction | foundations no-go with premises | dropping a premise opens model classes |
| Theorem 7 | fixed channel/task/cut/Markov/tensor classes as stated | minima within each class, not all ontologies | mathematical resource classification | different task or class changes the minimum |
| Theorem 8 | registered record events and all adequate completions | every representation morphism; existence of multiple fibers | operational plus actuality scope | micro-readers can split completions |
| Theorem 9 | admitted indivisible stochastic completions | representation and nonselection, not universal refutation | ontological boundary | a configuration discriminator could select |

All equivalences are exact. Systems, slots, and explicit outcomes are finite.
The standard-Borel extension assumes countable additivity, measurable kernels,
and measurable adaptive policies. Tensor composition and source independence
are operational assumptions only where stated. No spacetime locality is
used.

## 16. Result product

The construction-level product is:

```text
contract       P02-ADEQUATE-REPRESENTATION-CLASS-CONSTRUCTED
quotient       P02-OPERATIONAL-QUOTIENT-CANONICAL
naturality     P02-QUOTIENT-NATURALITY-CONSTRUCTED
fibers         P02-ONTOLOGY-FIBERS-CLASSIFIED
selection      P02-OPERATIONAL-NOSELECTION-THEOREM
phase          P02-PHASE-COMPLETE-PREDICTIVE-STATE-FORCED
scalar         P02-COMPLEX-SCALAR-ONTOLOGY-REPRESENTATION-NONUNIQUE
positivity     P02-POSITIVE-RECORD-LAWS-SURVIVE
context        P02-NONCONTEXTUAL-MICROONTOLOGY-NOGO-WITH-AFFINITY-PERFECT-DISTINGUISHABILITY-SHARP-PRODUCT-PREMISES
bell           P02-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
memory         P02-RESOURCE-INVARIANTS-CLASSIFIED
gauge          P02-GAUGE-REDUNDANCY-PHYSICAL-DIFFERENCE-CLASSIFIED
record         P02-OPERATIONAL-RECORD-INVARIANT
actuality      P02-RECORD-ACTUALITY-POSTULATED + MICROACTUALITY-UNCONSTRUCTED
barandes       P02-BARANDES-ONTOLOGY-UNSELECTED
discriminator  P02-EXTRA-ONTOLOGY-DISCRIMINATOR-NONE-IN-DOMAIN
ontology       P02-ONTOLOGY-UNDERDETERMINED
overall        P02-CANONICAL-QUOTIENT-WITH-UNSELECTED-ONTOLOGY-FIBERS
```

This product is provisional until independent review. The ceiling is rung 6
of the declared ladder. No representation-invariant microontology and no
empirical discriminator are constructed.

## 17. What has been learned

### 17.1 Positive result

Complete quantum experiments do determine a canonical object: the typed
phase-complete operational category of predictive states, processes,
instruments, records, and their composition. This is not merely a list of
terminal probabilities. It knows how every preparation behaves under every
allowed future and how processes compose.

### 17.2 Negative result

That canonical object does not determine what else exists microscopically.
Finite bits, continuous variables, preparation memories, and distinct latent
dynamics can all sit above the same operational point. Calling those
differences gauge is an extra ontological judgment unless the map is an
invertible redescription or a separately justified reduction.

### 17.3 Physical interpretation

The result avoids two opposite errors.

- It does not reify a convenient Hilbert, Kraus, dilation, real, or stochastic
  representation as nature.
- It does not infer that reality contains only operational equivalence
  classes.

Nature may have a definite microscopic ontology. If so, the present
experiments do not select it. A serious successor must identify a physical
question on which adequate completions differ, or derive a non-operational
principle with independent necessity. It cannot obtain a decision by
counting variables after choosing coordinates.

## 18. Primary sources and exact bridges

The quotient and no-selection theorems above are proved here. The following
sources provide comparator results whose assumptions have been retained.

1. R. W. Spekkens, “Contextuality for preparations, transformations, and
   unsharp measurements,” *Physical Review A* 71, 052108 (2005).
   [arXiv:quant-ph/0406166](https://arxiv.org/abs/quant-ph/0406166).
   Section 7.3 reconstructs its six-rotation transformation witness.
2. R. W. Spekkens, D. H. Buzacott, A. J. Keehn, B. Toner, and G. J. Pryde,
   “Preparation contextuality powers parity-oblivious multiplexing,”
   *Physical Review Letters* 102, 010401 (2009).
   [arXiv:0805.1463](https://arxiv.org/abs/0805.1463). Section 7.2 derives the
   two-bit inequality explicitly.
3. C. Ferrie and J. Emerson, “Frame representations of quantum mechanics and
   the necessity of negativity in quasi-probability representations,”
   *Journal of Physics A* 41, 352001 (2008).
   [arXiv:0711.2658](https://arxiv.org/abs/0711.2658). Its frame hypotheses
   are the restricted setting of Section 8.3.
4. Y. Kuramochi, “Minimal sufficient statistical experiments on von Neumann
   algebras,” *Journal of Mathematical Physics* 58, 062203 (2017).
   [arXiv:1701.03394](https://arxiv.org/abs/1701.03394). Section 9.2 retains
   the common parameter set, normal-state, and normal-isomorphism scope.
5. F. Buscemi, “Comparison of quantum statistical models: equivalent
   conditions for sufficiency,” *Communications in Mathematical Physics*
   310, 625–647 (2012).
   [arXiv:1004.3794](https://arxiv.org/abs/1004.3794). The decision-theoretic
   comparison is used only at finite-dimensional CP-postprocessing scope.
6. H. Barnum and A. Wilce, “Local tomography and the Jordan structure of
   quantum theory,” *Foundations of Physics* 44, 192–212 (2014).
   [arXiv:1202.4513](https://arxiv.org/abs/1202.4513). Section 6.4 lists the
   homogeneous self-dual, Jordan, composite, local-tomography, and qubit
   assumptions instead of importing them as results.
7. M. McKague, “On the power of quantum computation over real Hilbert
   spaces,” *International Journal of Quantum Information* 11, 1350001
   (2013). [arXiv:1109.0795](https://arxiv.org/abs/1109.0795). Section 6
   reconstructs the realification mechanism and exposes its global carrier.
8. Z.-D. Li et al., “Testing real quantum theory in an optical quantum
   network,” *Physical Review Letters* 128, 040402 (2022).
   [arXiv:2111.15128](https://arxiv.org/abs/2111.15128). Its natural-real
   source-composition premise is kept distinct.
9. T. Hoffreumon and M. P. Woods, “Quantum theory based on real numbers
   cannot be experimentally falsified,” unrefereed preprint (2026).
   [arXiv:2603.19208](https://arxiv.org/abs/2603.19208). Its operational
   source-independence theorem is treated as an adversarial comparator, not
   settled authority.
10. M. F. Pusey, J. Barrett, and T. Rudolph, “On the reality of the quantum
    state,” *Nature Physics* 8, 475–478 (2012).
    [arXiv:1111.3328](https://arxiv.org/abs/1111.3328). Preparation
    independence remains an explicit extra premise in Section 11.
11. A. Montina, “Exponential complexity and ontological theories of quantum
    mechanics,” *Physical Review A* 77, 022104 (2008).
    [arXiv:0711.4770](https://arxiv.org/abs/0711.4770). Section 9.4 applies
    its $2N-2$ bound only to the stated Markovian ontological class.
12. S. Gogioso and C. M. Scandolo, “Categorical probabilistic theories,” in
    *Proceedings of QPL 2017*, EPTCS 266, 367–385 (2018).
    [arXiv:1701.08075](https://arxiv.org/abs/1701.08075). It is a comparator
    for typed probabilistic composition, not an ontology selector.
13. J. A. Barandes, “Quantum systems as indivisible stochastic processes,”
    preprint (2025).
    [arXiv:2507.21192](https://arxiv.org/html/2507.21192v1). Section 11
    separates its asserted configuration ontology, minimalist transition law,
    and non-Markovian-realizer freedom.
14. W. F. Stinespring, “Positive functions on C*-algebras,” *Proceedings of
    the American Mathematical Society* 6, 211–216 (1955). The restricted
    dilation theorem is used in Sections 5.4 and 9.1.
15. A. Peres, “Incompatible results of quantum measurements,” *Physics
    Letters A* 151, 107–108 (1990).
16. N. D. Mermin, “Simple unified form for the major no-hidden-variables
    theorems,” *Physical Review Letters* 65, 3373–3376 (1990). References 15
    and 16 support the square reconstructed in Section 7.5.
17. J. S. Bell, “On the Einstein Podolsky Rosen paradox,” *Physics Physique
    Fizika* 1, 195–200 (1964). Section 8.1 derives the exact CHSH premise
    bound rather than citing locality by name.
18. G. Chiribella, G. M. D'Ariano, and P. Perinotti, “Theoretical framework
    for quantum networks,” *Physical Review A* 80, 022339 (2009). The
    finite-comb realization and fixed-cut memory setting underlie Section 9.3.

## 19. Construction boundary

This manuscript constructs mathematics only. It does not select a preferred
representation, perform a new experiment, derive an actualization law, or
open any time, spacetime, field, or gravity claim. Its product remains
construction-level until independent mathematical, quantum-foundations, and
ontology reviews are frozen and jointly adjudicated.
