# Procedures, operational equivalence, and the ontology residue of quantum processes

## A procedures-first repair of the canonical quotient and contextuality bridge

Date: 2026-08-22

Status: **CONSTRUCTION — GREEN-UNREVIEWED; NO PHYSICAL RESULT AWARDED**

## Abstract

Quantum contextuality compares distinct laboratory procedures that are
operationally equivalent. A mathematical account must therefore retain the
procedures before quotienting them by their observed predictions. Paper 02
v1 reversed this order. It began with an operationally separated category
and then asked a representation on that quotient to remember which equal
procedure occurred. No function can do that.

We construct the corrected two-level architecture. A small typed physical
procedure category $\mathcal P$ contains reproducible preparations,
transformations, instruments, measurements, ancillas, adaptive controls,
records, discard, and explicit trusted-randomization procedures. Harmless
names and serializations are removed before an arrow of $\mathcal P$ is
formed, but physically different implementations remain distinct. Complete
operational equivalence is a monoidal congruence, and its quotient

$$
q:\mathcal P\longrightarrow\mathcal Q
$$

recovers the accepted finite-dimensional, finite-slot,
definite-laboratory-order quantum operational category on its reachable
image.

An ontological assignment is defined on $\mathcal P$. Preparation,
transformation, measurement, or instrument noncontextuality is the additional
claim that the corresponding system-facing assignment factors through $q$.
This repairs the type error without asserting that two operationally
equivalent apparatuses are physically identical in every respect. General
whole-history representations need not expose an intermediate ontic state;
standard ontological-model contextuality is not applicable to them until such
an interface is declared.

We give an exact positive contextual existence model. Its ontic variables are
normalized operational predictive objects: density operators at ordinary
boundaries and conditional predictive combs at finite-memory process cuts.
Direct preparations use point measures, trusted mixtures use affine mixtures
of those measures, channels push predictive objects forward, and instruments
use Born-weighted substochastic update kernels. Distinct decompositions of
one density operator then have unequal ontic measures even though all
operational predictions agree. The construction uses no procedure-name tag,
but its price is explicit: it reifies the quantum predictive object and may
be global and memory-bearing. It establishes possibility, not explanation or
selection.

The surviving canonical quotient, phase-complete predictive residue, exact
realification, premise-indexed contextuality and Bell no-gos, positive record
histories, resource classifications, and idle-fiber nonselection results are
reconstructed at their adjudicated scopes. Contextuality is a global descent
obstruction, not an idle coordinate removable by a positive affine
state-level map. Nevertheless many inequivalent contextual realizations
remain possible. A preferred microscopic ontology, a complete Barandes
configuration law and trajectory, an actualization mechanism, time, space,
QFT, geometry, and gravity remain unconstructed.

## 1. Question, domain, and exclusions

The question is:

> Can the accepted quantum-process interface be represented with concrete
> physical procedures retained before operational quotienting, so that
> contextuality is a well-typed factorization obstruction while the
> operational quotient and ontology-under-determination results remain exact?

The domain is finite-dimensional quantum systems, finite outcomes, a finite
number of process slots, and definite laboratory control order. Measurable
standard-Borel extensions are admitted only when every decoder, kernel,
policy, conditioning operation, and continuation profile is measurable.

This paper does not construct:

- an unknown microscopic law beneath quantum theory;
- a complete Barandes configuration space and trajectory law;
- relativistic QFT or an indefinite-causal-order process theory;
- internal time, causal order, spatial regions, dimension, topology, metric,
  curvature, gravity, or cosmology;
- a selector over ontologies; or
- an outcome-selection mechanism.

Laboratory order is supplied by the experiment. It is not emergent time.
Tensor factors are controlled system types. They are not spatial regions.

## 2. Binding distinctions

The construction uses the following objects without identifying them.

| Object | Meaning here | Not identified with |
|---|---|---|
| physical procedure presentation | a drawing, naming, port ordering, or serialization of one laboratory protocol | physical protocol itself |
| physical procedure | a reproducible typed preparation, apparatus operation, measurement, randomizer, or wiring | code path or ontic state |
| operational class | everything fixed by every compatible registered experiment | complete apparatus reality |
| context | procedure features not fixed by the operational class | future choice or hidden answer |
| apparatus state | explicitly included degrees of a device | system ontic state |
| system ontic state | optional candidate complete system description at one boundary | quantum state by definition |
| complete history | candidate history conditional on a complete procedure | boundary-Markov trajectory |
| operational record | calibrated setting/outcome fact | complete microscopic history |
| actualization | occurrence of one event or history | normalization or decoherence |

A use of one row where another is required is a type error, not an
interpretive disagreement.

## 3. The physical procedure category

### 3.1 Boundary types

Let $\mathsf{B}$ be a small set of typed laboratory boundaries. A boundary
lists:

1. finite-dimensional quantum input and output system types;
2. finite classical setting and record registers;
3. open memory ports when a finite process has memory; and
4. the declared laboratory-order interface.

Different boundary types are never identified because a scalar probability
happens to agree.

### 3.2 Procedure declarations

A physical procedure declaration is a finite typed incidence structure whose
vertices are calibrated preparations, channels, instruments, measurement
devices, trusted randomizers, record-copy operations, classical controls, or
discard operations and whose edges are compatible physical ports. It is a
reproducible protocol type, not a particular run and not a software object.

Let $\mathsf{Pres}(p)$ be the groupoid generated by:

- renaming internal bound ports and branch variables;
- changing a harmless serialization order for independent vertices;
- redrawing the same typed incidence structure; and
- renaming an unlandmarked tensor-factor index while carrying its complete
  incidence, type, and calibration unchanged.

The groupoid may not change a physical setting, device calibration,
randomizer correlation, retained record, incidence relation, boundary type,
or the identity of a physically landmarked port. An actual exchange wiring is
a symmetry arrow in $\mathcal P$, not a presentation move.

Define $\mathcal P$ to have objects $\mathsf B$ and arrows the orbits of
physical procedure declarations under $\mathsf{Pres}$. This removes
presentation before any operational quotient is taken.

### 3.3 Composition

Sequential composition glues matching physical ports. Tensor composition is
disjoint union with declared independent control. Classical adaptation is a
finite family of compatible continuations indexed by an earlier retained
record. Discard terminates a declared port. Identity is an empty wire, not an
extra physical event.

Associativity and the unit equations follow from associativity of typed
incidence gluing after presentation quotienting. Symmetry is the physical
exchange of tensor factors together with every attached type and calibration.
The interchange law follows because disjoint gluing commutes.

### 3.4 Trusted randomization

A forgotten-record randomization is an explicit arrow

$$
\operatorname{Mix}_{r}\bigl((\alpha_i,p_i)_i\bigr),
\qquad
\alpha_i\geq0,
\qquad
\sum_i\alpha_i=1,
$$

where $r$ is an independently calibrated physical randomizer, initially
independent of the system, with no undeclared interaction or future-setting
correlation. Distinct randomizer implementations may remain distinct arrows
of $\mathcal P$.

If the outcome $i$ is retained, the output boundary contains it and the
arrow is an outcome-indexed instrument. If it is forgotten, operational
decoding and every applicable system-facing assignment satisfy

$$
q(\operatorname{Mix}_{r})=\sum_i\alpha_iq(p_i),
\qquad
\mathsf A_{\operatorname{Mix}_{r}}
=\sum_i\alpha_i\mathsf A_{p_i}.
$$

These are affine laws for the decoded operation and the assignment. They are
not equations identifying the underlying procedure arrows.

### 3.5 Presentation and closure theorem

**Theorem 1 (physical-procedure presentation invariance and closure).**
The operations above define a small typed symmetric-monoidal category
$\mathcal P$ with trusted-randomization constructors. Its arrows are invariant
under $\mathsf{Pres}$, and no listed presentation move changes a retained
record, physical incidence, setting, calibration, or randomizer contract.

**Proof.** Every generator of $\mathsf{Pres}$ is a typed incidence
isomorphism. Gluing and disjoint union send isomorphic diagrams to isomorphic
diagrams, so sequential and tensor composition descend to orbits.
Associativity, units, symmetry, and interchange are the corresponding
finite-incidence identities. Adaptive control and discard are typed gluing
operations and therefore descend as well. A trusted-randomization constructor
is transported by carrying its probability vector, branch procedures, record
status, and calibration together. The forbidden changes are not groupoid
arrows, so they remain physical data. QED.

This is a category of declared physical procedures. It does not claim that
apparatus descriptions are microscopic ontology.

## 4. Complete operational equivalence and the quotient

### 4.1 Independently fixed semantics

Let

$$
\mathsf{Sem}:\mathcal P\longrightarrow\mathsf{QProc}_{\rm fd}
$$

assign to every calibrated procedure its standard finite-dimensional quantum
operational object. The target contains states, completely positive events,
instruments, deterministic channels, classical records, finite combs,
ancillas, discard, and compatible wiring. It is the accepted Paper 01
comparator, not a candidate ontology.

For same-typed $p,p'$, write $p\sim_{\rm op}p'$ iff every one-hole physical
context $C[-]$ built from compatible prefixes, ancillary extensions,
adaptive continuations, and complete readers obeys

$$
\Pr(o\mid C[p])=\Pr(o\mid C[p'])
$$

for every complete outcome $o$. The context family is fixed before any
ontological representation is considered.

A context connects only to declared open ports and records. It may not open a
sealed apparatus and read an internal implementation label that is absent
from the boundary. If such access is calibrated and added, it defines a new
procedure type or reader and may refine the quotient.

### 4.2 Congruence theorem

**Theorem 2 (complete operational equivalence is a typed congruence).**
$\sim_{\rm op}$ is preserved by sequential pre- and postcomposition,
tensoring with compatible procedures and entangled ancillas, trusted
randomization, adaptive control, coarse-graining, retained records, and
discard.

**Proof.** Reflexivity, symmetry, and transitivity follow from equality of all
context probabilities. Suppose $p\sim_{\rm op}p'$. Every complete context
after postcomposition by $f$ defines a context $C[f\circ-]$ for $p$ and
$p'$. Every context before precomposition is absorbed similarly. A context
for $p\otimes a$ is already an ancillary context for $p$, including entangled
inputs; applying the argument twice handles two varying factors. Trusted
randomization preserves equality by the affine probability law. An adaptive
context is a finite sum over earlier retained outcomes, on each of which the
remaining branch is a compatible context. Coarse-graining and discard are
postcompositions, while a retained record changes the boundary type and is
compared only with an equally typed record. QED.

The ancillary quantifier is indispensable: complete positivity rather than
mere positivity is detected by allowing entangled extensions. Immediate
effects alone are also insufficient: the identity channel and $Z$ conjugation
both occur with probability one, but a later $X$ measurement on $|+\rangle$
separates them.

### 4.3 Quotient and universal property

Define

$$
\mathcal Q:=\mathcal P/{\sim_{\rm op}},
\qquad
q(p)=[p].
$$

Theorem 2 makes composition and tensoring well defined.

**Theorem 3 (operational quotient and universal property).**
The quotient functor $q:\mathcal P\to\mathcal Q$ is typed, symmetric
monoidal, and compatible with trusted randomization, adaptation, records, and
discard. On the accepted reachable image, the functor

$$
[p]\longmapsto\mathsf{Sem}(p)
$$

is an operational isomorphism onto the separated Paper 01 category.
Moreover, every typed functor $F:\mathcal P\to\mathcal C$ that preserves the
registered operations and is constant on $\sim_{\rm op}$ factors uniquely as
$F=\bar Fq$.

**Proof.** If $p\sim_{\rm op}p'$, every separating quantum tester agrees, so
$\mathsf{Sem}(p)=\mathsf{Sem}(p')$. Conversely, equality of the standard
operational objects gives equality in every compatible quantum context, hence
$p\sim_{\rm op}p'$. The map is therefore well defined and faithful. Every
accepted reachable quantum procedure has a declared laboratory
representative, giving fullness and essential surjectivity on the image.
The universal property is the usual congruence quotient: define
$\bar F([p])=F(p)$; constancy makes it well defined, and surjectivity of $q$
gives uniqueness. QED.

This is not a microscopic equivalence. Two arrows in one $q$ class may use
different devices or mixture procedures, and $q$ has no global inverse on
extra native states of a representation.

## 5. Corrected adequate representation packets

### 5.1 Whole-history packet

An adequate procedure-level representation is

$$
R=(\mathcal S_R,J_R^{\mathcal P},K_R,
\mathsf{Hist}_R,\Gamma_R,\mathsf{Read}_R,
\mathsf{Gauge}_R,\mathsf{Act}_R).
$$

It obeys:

1. $J_R^{\mathcal P}:\mathcal P\to\mathcal S_R$ is typed and preserves the
   registered procedure composition;
2. $K_RJ_R^{\mathcal P}=q$ on the reachable operational image;
3. $\Gamma_R(dh\mid p)$ is a normalized law on complete candidate histories
   for the complete procedure $p$;
4. every registered reader pushforward equals its quantum comparator;
5. the marginal law of a shared physical prefix is independent of which
   normalized, unperformed suffix is later chosen;
6. trusted mixtures are affine and independent tensor sources obey the
   declared source contract;
7. apparatus, record, memory, latent, law, and actuality fields are typed; and
8. gauge acts on the whole packet and preserves histories and readers.

The history spaces may depend on the procedure, but any comparison must state
the exact measurable transport between them. A whole-history packet need not
have a sufficient ontic state at every intermediate boundary.

### 5.2 Standard system-ontological subclass

A packet belongs to the standard subclass only if it also supplies measurable
spaces $\Lambda_A$ and:

- preparation measures $\mu_p(d\lambda)$;
- transformation kernels $\tau_t(d\lambda'\mid\lambda)$;
- outcome-indexed instrument kernels $T_{t,k}$;
- measurement responses $\xi_m(k\mid\lambda)$; and
- typed sequential, tensor, mixture, and conditioning rules.

For an ordinary preparation--transformation--measurement experiment,

$$
\Pr(k\mid p,t,m)=
\int_{\Lambda_B}\int_{\Lambda_A}
\xi_m(k\mid\lambda')
\tau_t(d\lambda'\mid\lambda)
\mu_p(d\lambda).
$$

Longer programs use iterated kernels and retained outcomes. Instrument
kernels are substochastic branchwise and normalized after summing outcomes.

### 5.3 Applicability theorem

**Theorem 4 (corrected adequate packets and contextuality applicability).**
The equation $K_RJ_R^{\mathcal P}=q$ permits a procedure-level
representation to distinguish $p$ from $p'$ even when $q(p)=q(p')$, while
forcing all decoded predictions to agree. Standard ontological
contextuality is defined only for packets carrying the interface of Section
5.2. A packet lacking that interface is neither contextual nor
noncontextual under that predicate.

**Proof.** The two arrows have distinct arguments in $\mathcal P$, so their
images under $J_R^{\mathcal P}$ may differ. Applying $K_R$ gives the same
$q$ class. The preparation, transformation, and measurement factorization
predicates require measures or kernels on common typed $\Lambda_A$ spaces;
without those objects the equations are not propositions. QED.

Noncontextuality never requires the full apparatus world to factor through
$q$. It constrains only the explicitly declared system-facing assignment.

## 6. Contextuality as failure of descent

### 6.1 Sort-specific definitions

A preparation model is noncontextual iff there exists $\bar\mu$ such that

$$
\mu_p=\bar\mu_{q(p)}.
$$

Transformation and measurement noncontextuality require

$$
\tau_t=\bar\tau_{q(t)},
\qquad
\xi_m=\bar\xi_{q(m)}.
$$

Instrument noncontextuality uses the entire outcome-indexed substochastic
kernel, not merely its immediate POVM effects. Universal noncontextuality is
the conjunction over every registered sort. Contextuality is exact failure
of one of these factorization equations for operationally equivalent
procedures.

Appending a procedure name to $\lambda$ produces a context-dependent data
structure but explains no probability. It is excluded as a positive
construction unless the declared measures, kernels, and responses actually
use the non-diagnostic ontic values to reproduce the experiment.

### 6.2 A positive predictive-object model

For an ordinary boundary $A$, set

$$
\Lambda_A=\mathsf{Pred}(A),
$$

the compact convex set of normalized positive affine functionals on every
compatible future test. In finite-dimensional quantum theory this is the
density-operator state space. At a finite-memory cut it is the corresponding
normalized conditional predictive comb, with all memory ports required by
the accepted interface.

A direct preparation of $\rho$ has

$$
\mu_{P_\rho}=\delta_\rho.
$$

A trusted forgotten mixture obeys

$$
\mu_{\operatorname{Mix}_{r}((\alpha_i,p_i)_i)}
=\sum_i\alpha_i\mu_{p_i}.
$$

A deterministic channel $\mathcal E$ uses

$$
\tau_{\mathcal E}(d\lambda'\mid\lambda)
=\delta_{\mathcal E(\lambda)}(d\lambda').
$$

A trusted random mixture of channel procedures uses the mixture of these
pushes. For a quantum instrument $\{\mathcal I_k\}_k$, define

$$
T_{k}(d\lambda'\mid\lambda)
=p_k(\lambda)
\delta_{u_k(\lambda)}(d\lambda'),
$$

where

$$
p_k(\lambda)=\operatorname{tr}[\mathcal I_k(\lambda)],
\qquad
u_k(\lambda)=
\frac{\mathcal I_k(\lambda)}{p_k(\lambda)}
$$

when $p_k(\lambda)>0$. When $p_k(\lambda)=0$, $T_k$ is the zero measure and
no normalized branch state is introduced. A terminal POVM
$m=\{E_k\}_k$ has

$$
\xi_m(k\mid\lambda)=\operatorname{tr}(E_k\lambda).
$$

For predictive combs, $p_k$ and $u_k$ are the corresponding link-product
probability and normalized conditional comb. Composite predictive objects
carry the declared tensor type. Independently prepared sources use product
preparation measures; entangled preparations are direct composite states.

### 6.3 Positivity and lineage theorem

**Theorem 5 (positive contextual predictive-object representation).**
The assignments of Section 6.2 are nonnegative, normalized, affine under
trusted randomization, closed under sequential instruments, compatible with
the declared tensor/source contract, and reproduce every finite registered
quantum-process probability. They form a standard positive ontological model
that is preparation contextual and, when a channel has inequivalent physical
decompositions, transformation contextual.

**Proof.** Point measures and convex mixtures of probability measures are
positive and normalized. The instrument kernels are positive and have total
mass $p_k(\lambda)$. Since $\sum_k\mathcal I_k$ is trace preserving,

$$
\sum_k\int T_k(d\lambda'\mid\lambda)=1.
$$

For a sequence of instruments, iterated integration multiplies the
conditional branch probabilities and composes the normalized postevent
states. The normalization factors telescope, leaving the standard unnormalized
composition

$$
\operatorname{tr}
\left[\mathcal I^{(n)}_{k_n}\circ\cdots\circ
\mathcal I^{(1)}_{k_1}(\rho)\right].
$$

Adaptive control is a branchwise choice of the next kernel. Tensor-product
sources and local operations give the usual composite Born expression;
conditional-comb contraction gives the finite-memory process expression.
Trusted randomization is affine by construction.

Now compare

$$
M_Z=\operatorname{Mix}\left(\tfrac12P_{|0\rangle},
                            \tfrac12P_{|1\rangle}\right),
\qquad
M_X=\operatorname{Mix}\left(\tfrac12P_{|+\rangle},
                            \tfrac12P_{|-\rangle}\right).
$$

Both decode to $I/2$, but

$$
\mu_{M_Z}=\tfrac12\delta_{|0\rangle\langle0|}
          +\tfrac12\delta_{|1\rangle\langle1|},
$$

and

$$
\mu_{M_X}=\tfrac12\delta_{|+\rangle\langle+|}
          +\tfrac12\delta_{|-\rangle\langle-|}
$$

are unequal measures with disjoint supports. Hence preparation factorization
through $q$ fails without any procedure-name coordinate. A direct channel
realizing an averaged CP map gives a deterministic push of $\lambda$, while
a trusted physical mixture of its component channels gives a mixture of
pushes; when those measures differ, transformation factorization fails. QED.

The model is global and may carry the complete predictive comb. It reifies
the standard quantum predictive object. It proves that positive contextual
models exist; it does not explain or select that ontology.

### 6.4 Exact noncontextuality witnesses

For parity-oblivious multiplexing, Alice prepares

$$
\rho_x=\frac12\left[
I+\frac{(-1)^{x_1}X+(-1)^{x_2}Z}{\sqrt2}
\right],
$$

and Bob measures $X$ or $Z$. Quantum theory gives

$$
p_Q=\frac12\left(1+\frac1{\sqrt2}\right)>\frac34.
$$

The even and odd mixtures both equal $I/2$. In a preparation-noncontextual
affine model, conditional posterior weights $a,b,c,d$ obey
$a+d=b+c=1/2$. The best average guess satisfies

$$
s_\lambda=\frac12[
\max(a+b,c+d)+\max(a+c,b+d)]\leq\frac34,
$$

because

$$
|a+b-1/2|+|a-b|\leq1/2
$$

for $0\leq a,b\leq1/2$. Averaging yields the contradiction.

For transformation contextuality, let $T_{k\pi/3}$ be rotations around the
Bloch $y$ axis and let $T$ project the Bloch vector onto that axis. The five
physical decompositions

$$
T=\tfrac12(T_0+T_\pi)
=\tfrac12(T_{\pi/3}+T_{4\pi/3})
=\tfrac12(T_{2\pi/3}+T_{5\pi/3})
$$

and

$$
T=\tfrac13(T_0+T_{2\pi/3}+T_{4\pi/3})
=\tfrac13(T_{\pi/3}+T_\pi+T_{5\pi/3})
$$

are distinct arrows of $\mathcal P$ with one channel image in $\mathcal Q$.
For an input pure state in the $xz$ plane, opposite rotations have disjoint
ontic supports under perfect distinguishability. Writing
$r_k=\mu_k(\lambda)/\mu(\lambda)$ where $\mu(\lambda)>0$, the half-mixtures
force each opposing pair to be $(2,0)$ or $(0,2)$, while the third-mixtures
require

$$
r_0+r_2+r_4=r_1+r_3+r_5=3.
$$

The left sides are even integers, contradiction.

The Peres--Mermin square

$$
\begin{pmatrix}
X\otimes I&I\otimes X&X\otimes X\\
I\otimes Y&Y\otimes I&Y\otimes Y\\
X\otimes Y&Y\otimes X&Z\otimes Z
\end{pmatrix}
$$

has three positive row products, two positive column products, and one
negative column product. Multiplying one context-independent deterministic
value assignment counts every observable twice but demands both $+1$ and
$-1$. The conclusion requires the preparation-noncontextuality and
perfect-prediction bridge to sharp outcome determinism, common maximally
mixed preparation coverage, measurement noncontextuality, and the commuting
functional-product rule.

### 6.5 Premise-indexed no-go theorem

**Theorem 6 (structural contextuality with printed premises).**
No one standard ontological model for the complete registered fragments can
satisfy simultaneously:

1. positive affine preparation measures;
2. positive normalized measurement responses;
3. positive affine transformation and instrument kernels;
4. preparation noncontextuality;
5. transformation noncontextuality;
6. measurement noncontextuality plus the sharp Peres--Mermin bridge;
7. the declared independent-source tensor contract;
8. measurement independence in the Bell fragment; and
9. Bell factorization.

**Proof.** Parity-oblivious multiplexing contradicts items 1 and 4.
The six-rotation construction contradicts items 3 and 5. The Peres--Mermin
product contradicts item 6 with its printed bridge. For CHSH, measurement
independence and Bell factorization give conditional means
$|A_x(\lambda)|,|B_y(\lambda)|\leq1$ and pointwise

$$
|A_0(B_0+B_1)+A_1(B_0-B_1)|\leq2.
$$

Integration gives $|S|\leq2$, while the singlet with the standard coplanar
settings gives $2\sqrt2$. Any one contradiction defeats the conjunction.
QED.

This is a no-go for a premise package, not for ordinary positive probability.
Theorem 5 is an explicit positive contextual counterexample to that
overreading.

## 7. Fiber freedom and no-selection

### 7.1 Uniform idle-fiber inflation

Fix an adequate packet $R$ and a standard-Borel space $Z$. For each finite
procedure tree choose normalized measurable kernels

$$
\nu_p(dz_0\mid h_0),
\qquad
L_{p,k}(dz_k\mid z_{k-1},h_{\leq k}),
$$

depending only on the declared preparation/procedure prefix and realized
history prefix, never on an unperformed future choice. The family is indexed
by physical prefixes: whenever two complete procedures share a prefix, they
use literally the same kernels on that prefix. Define

$$
\Gamma_R^Z(dh,dz_0\cdots dz_n\mid p)
=\Gamma_R(dh\mid p)\nu_p(dz_0\mid h_0)
\prod_{k=1}^{n}L_{p,k}(dz_k\mid z_{k-1},h_{\leq k}).
$$

Inherited readers ignore $Z$. Trusted mixtures mix the full measures.
Independently controlled tensor factors use the declared product kernel unless
a correlated source is separately entered.

**Theorem 7 (idle-fiber inflation and reduction).**
For finite, countable, and standard-Borel $Z$, the construction above is an
adequate procedure-level packet with the same operational quotient as $R$.
Projection

$$
\pi_Z:(h,z_0,\ldots,z_n)\longmapsto h
$$

is a positive probability-preserving representation morphism. If an
independently fixed future reader couples to $Z$, the projection ceases to
preserve that enlarged experiment and the quotient may split.

**Proof.** Iterated normalization of $\nu$ and $L$ returns
$\Gamma_R(dh\mid p)$. Prefix coherence, mixture affinity, and tensor scope
hold by the kernel hypotheses. Every inherited reader therefore has the same
law, and marginalization intertwines all registered operations. A
$Z$-sensitive reader violates the intertwining equation, so it is a genuine
enlargement rather than a contradiction. QED.

Exact controls include a static bit, a prefix-controlled hold/flip bit,
Lebesgue versus Cantor measures on $[0,1]$, and preparation-correlated fibers
indexed by distinct procedures in one $q$ class.

### 7.2 Restricted representation category

Let $\mathbf{Rep}_{\rm adm}(\mathcal P\to\mathcal Q)$ contain adequate
packets and only those morphisms that preserve decoders, history
pushforwards, trusted mixtures, tensor/source declarations, records, and the
full positive assignment class. It includes complete-packet isomorphisms,
the explicit idle inflations, and their probability-preserving projections.
It does not include every imaginable forgetting map.

A representation-natural pointwise invariant $I$ satisfies

$$
I_{R'}(Tx)=I_R(x)
$$

for every admitted $T:R\to R'$.

**Theorem 8 (scoped idle-fiber no-selection).**
For every admitted idle inflation $R^Z$ and projection
$\pi_Z:R^Z\to R$, a representation-natural invariant obeys

$$
I_{R^Z}(h,z_0,\ldots,z_n)=I_R(h).
$$

It is therefore constant on the added $Z$ fiber and factors uniquely through
the base representation $R$. It factors further through an operational
quotient only when a separately admitted chain of positive affine
representation morphisms reaches that quotient. Conversely, every invariant
of the base representation pulls back to a fiber-insensitive invariant on
the inflation/projection diagram.

**Proof.** Naturality with respect to $\pi_Z$ gives the displayed equality.
Equal projected histories therefore have equal values, and surjectivity of
$\pi_Z$ gives the unique factor on $R$. Repeating the argument along an
actually admitted chain gives further factorization; no unlisted reduction is
created by the proof. The converse is composition with $\pi_Z$. QED.

This is conditional on the chosen morphism class. It neither declares every
idle variable unreal, collapses contextual dependence through $q$, nor
assigns equal prior probability to all completions.

### 7.3 Why contextuality is not an idle coordinate

Suppose one tried to map Theorem 5's contextual preparation family to the
direct operational-state assignment $\mu_p=\delta_{q(p)}$ using one positive
affine Markov kernel $D(d\sigma\mid\lambda)$. Direct preparations require

$$
D_*\delta_\rho=\delta_\rho
$$

for every $\rho$. Affinity then forces

$$
D_*\left(\sum_i\alpha_i\delta_{\rho_i}\right)
=\sum_i\alpha_i\delta_{\rho_i},
$$

not $\delta_{\sum_i\alpha_i\rho_i}$ when the decomposition is nontrivial.
Thus the desired erasure is nonlinear at the level of measures and is not an
admitted positive affine representation morphism.

**Theorem 9 (contextuality/idle-fiber separation and particular-model
nonselection).** A theory-level failure of noncontextual descent can coexist
with Theorem 8. Contextual dependence cannot be erased by the forbidden map
above inside the same positive affine class. Nevertheless the
predictive-object model and its binary idle-fiber inflation are nonisomorphic
adequate contextual packets **over the predictive-object projection** with
identical registered predictions: an isomorphism commuting with that
projection would have to biject each singleton base fiber with a two-element
fiber. Hence structural contextuality does not select a particular contextual
ontology.

The added idle fiber is a mathematical nonuniqueness witness, not evidence
that the fiber exists.

## 8. Phase-complete predictive residue and scalar nonselection

### 8.1 Predictive-state separation

For an ordinary boundary define

$$
\omega_\rho(E)=\operatorname{tr}(\rho E).
$$

If $\operatorname{tr}[(\rho-\sigma)E]=0$ for every effect
$0\leq E\leq I$, effects span the Hermitian operators, so $\rho=\sigma$.
The same separating-tester argument applies to finite process combs.

The states

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}
$$

have equal $Z$ diagonals but are perfectly separated after a Hadamard. The
phase family

$$
U_\phi=|0\rangle\langle0|+e^{i\phi}|1\rangle\langle1|,
\qquad
U_\phi U_\theta=U_{\phi+\theta},
$$

shows that the complete composition data contain a full circle, not one
preferred probability vector.

### 8.2 Exact realification

For $M=A+iB$, define

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

With

$$
\rho_{\mathbb R}=\tfrac12\mathfrak R(\rho),
\qquad
E_{\mathbb R}=\mathfrak R(E),
$$

one has

$$
\operatorname{tr}_{\mathbb R}(\rho_{\mathbb R}E_{\mathbb R})
=\operatorname{tr}_{\mathbb C}(\rho E).
$$

The real carrier retains

$$
J=\begin{pmatrix}0&-I\\I&0\end{pmatrix},
\qquad J^2=-I,
$$

and represented complex-linear maps commute with $J$. For separate systems,
$\mathfrak R(\mathcal H_A\otimes_{\mathbb C}\mathcal H_B)$ has real
dimension $2d_Ad_B$, whereas separately realified carriers have ordinary
real tensor dimension $4d_Ad_B$. Exact simulation therefore carries a shared
complex structure, a constraint on the extra carrier, or a modified
composition rule.

**Theorem 10 (phase completeness without scalar selection).**
Complete continuations force phase-complete predictive structure, but the
registered finite operational domain does not select complex numbers as
fundamental ontology. Exact realification preserves the encoded experiments
only with its global $J$, tensor, and source-independence costs exposed.

Natural real quantum theory with an unrestricted ordinary real tensor
product is a different comparator. Claims that distinguish it and claims
that realify a complete complex network use different source/composition
contracts; neither may borrow the other's premises.

## 9. Positivity, Bell locality, and representation costs

### 9.1 Three positivity claims

The following statements are different:

1. every registered actual outcome has a probability in $[0,1]$;
2. one affine quasiprobability frame represents all states and effects
   nonnegatively; and
3. one fixed ontological interface represents every procedure by positive
   affine objects that factor through $q$.

Paper 01 and Theorem 5 satisfy the first. Theorem 5 also supplies positive
objects for the third interface while deliberately failing factorization.
Frame-negativity and contextuality theorems obstruct stronger conjunctions;
they do not make an actual record probability negative.

### 9.2 Bell premise ledger

For settings $x,y\in\{0,1\}$ and outcomes $a,b\in\{+1,-1\}$, a
measurement-independent Bell-factorizable model has

$$
p(a,b\mid x,y)=\int_\Lambda\mu(d\lambda)
p_A(a\mid x,\lambda)p_B(b\mid y,\lambda),
$$

where $\mu$ does not depend on $x,y$. With

$$
A_x(\lambda)=\sum_a a\,p_A(a\mid x,\lambda),
\qquad
B_y(\lambda)=\sum_b b\,p_B(b\mid y,\lambda),
$$

one has

$$
|A_0(B_0+B_1)+A_1(B_0-B_1)|\leq2
$$

pointwise, hence $|S|\leq2$. The singlet and the standard coplanar settings
give $2\sqrt2$. This excludes the conjunction of measurement independence
and Bell factorization. It does not exclude no-signalling quantum statistics,
global histories, or contextual positive models.

### 9.3 Frame negativity

An affine frame model seeks

$$
\operatorname{tr}(\rho E)
=\int_\Lambda\mu_\rho(\lambda)\xi_E(\lambda)\,d\lambda
$$

with one common noncontextual representation of states, effects,
transformations, and mixtures. Quantum theory forces negativity or a
deformation of the classical calculus under the frame assumptions. Theorem
5 evades the conclusion by preparation and transformation context dependence,
not by assigning negative probabilities to records.

## 10. Restricted resource invariants

For a finite-dimensional CP map, Choi rank is the minimum number of Kraus
operators and the minimum Stinespring environment dimension after the input,
output, and dilation class are fixed. Minimal dilations are unique up to the
declared environment isometry.

For a parameter-indexed statistical experiment, minimal sufficiency is
defined relative to the fixed parameter family and allowed CP
postprocessings. Under the corresponding finite or normal
von-Neumann-algebraic hypotheses, the minimal sufficient experiment is unique
up to the printed randomization or normal-isomorphism relation.

For a finite comb $W$ and typed cut $D$, define

$$
m_D(W)=\min\{\dim M:
M\text{ is Hilbert memory crossing }D
\text{ in an exact causal realization of }W\}.
$$

A finite realization exists, so the nonempty set of positive integer
dimensions has a minimum. It is a fixed-cut, fixed-task, Hilbert-realization
quantity. A non-Markovian whole history can encode the same predictions
without a sufficient current carrier, while a padded Markov carrier can be
arbitrarily larger.

Known lower bounds on continuous ontic dimension retain their Markov,
regularity, and dynamical assumptions. Single-system realification doubles
the carrier and multi-system simulation has the global-$J$/tensor cost of
Section 8. Neither is a universal size of reality.

**Theorem 11 (restricted resource classification).**
Decoded Choi rank, minimal Stinespring size, minimal sufficient experiments,
and fixed-cut comb-memory minima factor through $q$ in their fixed resource
classes. They do not equal the size of every adequate microscopic
realization. Markovian ontic dimension and real-coordinate overhead are
defined only after their additional model-class assumptions are fixed.

**Proof.** Each restricted minimum is a function of the decoded channel,
experiment, or comb, so equal $q$ classes have equal values. Theorem 7
adjoins a nontrivial idle fiber to any minimizer without changing the decoded
object and projection removes it. Thus the operational minimum remains exact
while universal microscopic minimality fails. QED.

Description length and computational convenience are representation
dependent. They select no ontology without an independently fixed physical
coding and selection law.

## 11. Records, predictive divisions, and actuality

### 11.1 Records descend to the quotient

A record has typed values and an independently calibrated future reader. If
$r\neq r'$, some registered continuation $C$ and outcome $o$ obey

$$
\Pr(o\mid C,r)\neq\Pr(o\mid C,r').
$$

The two values therefore lie in different operational classes. Every
adequate representation morphism preserves the corresponding reader laws.

### 11.2 A record is not automatically a division

A boundary argument $Z_D$ is sufficient for a declared future family only if

$$
Z_D(H_1)=Z_D(H_2)
\Longrightarrow
\Pr(F\mid H_1)=\Pr(F\mid H_2)
$$

for every licensed future $F$. A stable local record may fail this complete
future-sufficiency test. No hidden phase, history identifier, or cache may be
added after failure.

### 11.3 Actual record versus microhistory

One may postulate that one quotient-level record history
$h_{\rm rec}$ occurs. An adequate completion can contain many microscopic
histories in

$$
\pi_H^{-1}(h_{\rm rec}).
$$

Normalization, conditioning, and decoherence assign or stabilize
probabilities; none selects one element of this fiber.

**Theorem 12 (record invariance and actuality gap).**
Registered record distinctions and probabilities descend through $q$ and are
preserved by every adequate representation morphism. One actual record may be
postulated. No unique microscopic trajectory or actualization law follows.

**Proof.** Reader separation proves descent. Theorem 7 attaches multiple
microscopic histories to the same record without moving its law, and Theorem
8 prevents a representation-natural pointwise selector from reading an
admitted idle fiber. QED.

Reordering a serialization of independent procedures is not time. Renaming a
tensor factor is not space. No fiber in this paper is a spacetime atom.

## 12. The Barandes boundary

A complete Barandes-style ontology would require at least:

1. one fixed configuration space or fully typed family of configuration
   spaces;
2. contingent standalone probabilities;
3. a complete indivisible transition-law family across the admitted
   experiments and divisions; and
4. one actual configuration trajectory as referent.

This paper constructs none of those four as a complete packet. It is
compatible with the possibility that such a packet underlies the positive
record laws, but compatibility is not construction.

**Theorem 13 (Barandes admissibility without reconstruction).**
The accepted positive record histories and Theorem 5 show that ordinary
positive stochastic representation remains possible at the declared
operational scope. The quotient and no-selection theorems fix neither a
preferred configuration referent nor one complete trajectory law. The exact
classification is

```text
P02V2-BARANDES-ONTOLOGY-ADMISSIBLE-BUT-UNCONSTRUCTED-AND-UNSELECTED.
```

This neither refutes nor reconstructs Barandes's proposal. A no-go against a
Markovian, noncontextual, or finite-dimensional subclass is not a no-go
against every indivisible completion.

## 13. Discriminator ledger

| Competing representations | Shared registered predictions | Differing claim | Required independent discriminator or principle | Present disposition |
|---|---|---|---|---|
| direct predictive-object model / idle-bit inflation | all finite registered quantum procedures | an additional binary fact exists | predeclared bit-sensitive intervention or reader | none; underdetermined |
| Lebesgue / Cantor fiber | same | continuous microstate law | fiber-sensitive preparation/readout | none; underdetermined |
| hold / prefix-flip fiber dynamics | same | temporal microcorrelations | two-boundary fiber access under one frozen law | none; underdetermined |
| direct mixed-state preparation / physical decomposition mixture | same density operator | ontic measure differs | a system-ontic discriminator beyond standard quantum predictions | contextuality proved; realization unselected |
| direct channel / randomized decomposition | same CP map | ontic transition kernel differs | a kernel-sensitive intervention beyond the channel class | contextuality possible; realization unselected |
| minimal / padded dilation | same channel | extra environment is physical | independent environment access or physical no-padding law | restricted minimum only |
| complex / exact realification | encoded finite experiments | scalar/carrier ontology | matched composition, source, and access contract | no scalar selection |
| two whole-history realizers | same record law | unrecorded paths differ | reader of unrecorded cuts or derived realizer law | none; underdetermined |
| quotient-only / configuration ontology | same records | complete configurations exist | configuration-sensitive physics or independent principle | admissible, unselected |
| competing actualization laws | same normalized law | which event occurs | new probability/structure beyond normalization | mechanism absent |

An extension in the fourth column is new physics. It must be frozen before
the competing models are evaluated.

## 14. Registered controls C1--C24

| ID | Positive direction | Negative/refusal direction |
|---|---|---|
| C1 | even and odd POM mixtures are distinct $\mathcal P$ arrows | both map to $I/2$ under $q$; they are not distinct operational states |
| C2 | five physical channel decompositions remain distinct procedures | one CP channel class does not retain the decomposition |
| C3 | a measurement fine-graining is a physical procedure | forgetting its suboutcome can yield one POVM class; retaining it changes type |
| C4 | retained randomizer result is a typed record instrument | forgotten result is an affine operational mixture, not the same output type |
| C5 | identity and $Z$ conjugation have equal immediate certainty | a later $X$ reader separates their channel classes |
| C6 | ancillary and adaptive contexts preserve the quotient relation | a relation tested only by terminal effects is refused as incomplete |
| C7 | redrawings and bound-port renamings are presentation gauge | changed calibration, incidence, or record is not gauge |
| C8 | reproducible physical device protocols form procedures | a source branch name or evaluator flag is refused |
| C9 | an appended procedure tag is context dependent | it is not accepted as a predictive explanation or positive control |
| C10 | Theorem 5 reproduces full lineage with predictive ontic objects | its global quantum-state/comb cost blocks ontology selection |
| C11 | POM quantum success exceeds $3/4$ | the no-go is refused without affine mixing and the even/odd equivalence |
| C12 | the six-rotation parity contradiction is exact | it is refused without perfect distinguishability and affine kernels |
| C13 | Peres--Mermin blocks one sharp context-independent value table | it is refused without the preparation/perfect-prediction bridge and product rule |
| C14 | Bell factorization plus measurement independence gives $2$ | no-signalling alone is not called Bell locality |
| C15 | a whole-history packet may be positive and adequate | without $\Lambda_A$ it is `NOT-APPLICABLE`, not noncontextual |
| C16 | a static hidden bit gives an exact idle inflation | it is not called physical or gauge merely because unread |
| C17 | hold and prefix-flip fibers have different microcorrelations | their inherited operational pushforwards remain equal |
| C18 | admitted idle projection preserves positive affine wiring | context erasure is refused when it is nonlinear on measures |
| C19 | a calibrated latent reader splits old equivalence classes | no reader is added after observing which split is desired |
| C20 | exact realification preserves encoded probabilities | global $J$, tensor, and source costs are not hidden |
| C21 | minimal dilation is exact in its class | padded realization is not thereby declared false ontology |
| C22 | one operational record can be actual | multiple compatible microhistories block microscopic selection |
| C23 | a complete Barandes packet remains logically admissible | a placeholder or positive record law is not called a construction |
| C24 | serialization/tensor renaming leaves physics unchanged | procedure order and factor labels are not promoted to time or space |

Every positive direction is paired with a scope refusal; no control is passed
by a name match.

## 15. Hostile-attack disposition 1--56

### 15.1 Procedure and quotient attacks

1. **Collapse $\mathcal P$ into $\mathcal Q$.** Refused by Sections 3--4;
   $M_Z\neq M_X$ in $\mathcal P$ while $q(M_Z)=q(M_X)$.
2. **Code path as procedure.** Refused by the physical incidence referent and
   presentation groupoid.
3. **Unperformed future setting in procedure data.** Refused by procedure
   typing and shared-prefix coherence.
4. **Forget retained randomizer status.** Refused because retained and
   forgotten records have different boundaries.
5. **Merge types by scalar equality.** Refused; equivalence is hom-set typed.
6. **Equate instruments by immediate POVM effect.** Refused by the identity
   versus $Z$ continuation control.
7. **Omit entangled ancillas.** Refused by the complete context family.
8. **Choose testers after construction.** Refused; $\mathsf{Sem}$ and the
   tester closure precede every ontology.
9. **Fail adaptive congruence.** Refused by Theorem 2's branchwise proof.
10. **Call $q$ presentation gauge.** Refused; it is many-to-one operational
    forgetting, not an invertible redescription.
11. **Call $q$ microscopic equivalence.** Refused by apparatus and fiber
    countermodels.
12. **Invert $q$ on extra native objects.** Refused; Theorem 3 is on-image.

### 15.2 Ontological-interface and contextuality attacks

13. **Factor the complete apparatus world.** Refused; only the declared
    system-facing assignment is tested.
14. **Infer $\Lambda_A$ from any history law.** Refused by Theorem 4.
15. **No interface marked noncontextual.** Refused; the coordinate is
    `NOT-APPLICABLE-UNTIL-INTERFACE`.
16. **Procedure tag called explanation.** Refused; Theorem 5 uses unequal
    measures on predictive objects after all names are deleted.
17. **Drop mixture affinity.** Refused by the trusted-randomization equation.
18. **Compare measures on untyped spaces.** Refused; factorization is within
    one boundary type and declared measurable identification.
19. **Hide preparation context in transformations.** Counted as
    transformation contextuality, so universal factorization still fails.
20. **Factor immediate effects only.** Refused; instruments use complete
    substochastic kernels and continuations.
21. **Measurement noncontextuality alone implies determinism.** Refused; the
    sharp bridge is printed.
22. **Omit perfect prediction/common-mixture coverage.** Refused by the
    Peres--Mermin premise ledger.
23. **Positivity equals noncontextuality.** Killed by Theorem 5.
24. **No-signalling equals Bell locality.** Refused by Section 9.2.
25. **Bell state depends on settings.** That violates measurement
    independence and does not answer the registered Bell-local question.
26. **Global predictive state called relativistically local.** Refused; the
    control is openly global and Paper 03 remains closed.

### 15.3 Fiber and no-selection attacks

27. **Every idle distinction is coordinate gauge.** Refused; projection is
    generally noninvertible.
28. **Erase context without checking structure.** The attempted map fails
    positive affinity as shown in Section 7.3.
29. **Apply pointwise factorization to every invariant.** Refused; Theorem 8
    quantifies only over natural invariants and admitted morphisms.
30. **Treat contextuality as one coordinate over $q$.** Refused; it is a
    family-level descent obstruction over $\mathcal P$.
31. **Continuous fiber without base measure.** Refused; every inflation binds
    its normalized Borel law.
32. **Future-dependent latent dynamics.** Refused by prefix-local kernels.
33. **Inconsistent tensor kernel.** Refused by the declared source contract.
34. **Delete a readable coordinate.** A fiber-sensitive reader removes the
    projection from the admitted morphism class.
35. **Select by entropy, code, dimension, elegance.** Refused without an
    independent physical principle.
36. **All completions equally plausible.** Not inferred; no measure on
    completions is supplied.

### 15.4 Quantum residue and resource attacks

37. **Keep only diagonal probabilities.** Killed by the Hadamard phase
    control.
38. **Hide complex structure in real coordinates.** Refused; $J$ and the
    doubled carrier are explicit.
39. **Mismatch source assumptions.** Refused; real/complex comparisons retain
    one declared source contract.
40. **Promote local tomography from premise to fact.** Refused; it remains a
    conditional reconstruction input.
41. **Quasiprobability negativity is actual negative probability.** Refused
    by the three-level positivity table.
42. **Minimal dilation is universal ontic size.** Killed by fiber inflation.
43. **Markov bound on non-Markov history.** Refused by Theorem 11's domain.
44. **Terminal lookup as process memory.** Refused; the predictive comb must
    compose under every continuation.
45. **Record actuality is microactuality.** Killed by Theorem 12.
46. **Normalization/conditioning/decoherence actualizes.** Refused; none
    chooses one outcome.

### 15.5 Ontology and downstream attacks

47. **Positive record law is complete Barandes ontology.** Refused by
    Theorem 13's four missing objects.
48. **One subclass no-go refutes Barandes.** Refused; model-class premises
    remain explicit.
49. **Contextuality selects a configuration algebra.** Killed by Theorem 9.
50. **Phase completeness selects complex substance.** Killed by Theorem 10.
51. **Procedure order is time.** Refused; it is an experiment input.
52. **Tensor factor is space.** Refused; it is a system type.
53. **Discrete ontic states are spacetime atoms.** Refused; no spatial or
    geometric discriminator exists.
54. **Insert dimension, topology, metric, gravity.** Outside the pin and not
    used.
55. **Use v16 Paper 13D as v17's law.** Refused; it remains a reference model.
56. **Open Paper 03 before terminal adjudication.** Refused; this construction
    is green-unreviewed.

## 16. Mandatory theorem-package census

| Pin item | Construction location | Disposition |
|---:|---|---|
| 1 | Theorem 1 | physical-procedure presentation invariance constructed |
| 2 | Theorem 1 | procedure-category closure constructed |
| 3 | Theorem 2 | complete equivalence congruence constructed |
| 4 | Theorem 3 | quotient universal property constructed on reachable image |
| 5 | Theorem 4 | corrected adequate-packet typing constructed |
| 6 | Section 6.1 and Theorem 6 | sort-specific factorization constructed |
| 7 | Theorem 4 | interface applicability/refusal constructed |
| 8 | Theorem 5 | positive contextual model constructed |
| 9 | Theorem 6 | premise-indexed no-gos reconstructed |
| 10 | Theorem 7 | idle-fiber inflation/reduction constructed |
| 11 | Theorem 8 | invariant factorization constructed at admitted scope |
| 12 | Theorem 9 | contextuality/fiber separation constructed |
| 13 | Theorem 9 | particular contextual ontology unselected |
| 14 | Theorem 10 | phase-complete residue reconstructed |
| 15 | Theorem 10 | scalar ontology nonuniqueness reconstructed with costs |
| 16 | Theorem 11 | resource classification reconstructed at fixed classes |
| 17 | Theorem 12 | record/microactuality separation reconstructed |
| 18 | Theorem 13 | Barandes boundary demoted as required |
| 19 | Section 13 | complete discriminator ledger constructed |
| 20 | Section 18 | full product and outcome rung printed |

## 17. Quantifier and resource ledger

| Result | Procedure/representation domain | Exact quantifier | Kind | Sensitivity |
|---|---|---|---|---|
| Theorem 1 | finite physical incidence procedures modulo presentation groupoid | every registered generator and composition | mathematical referent | a changed calibration is a new procedure |
| Theorems 2--3 | finite-dimensional, finite-slot, definite-order complete context closure | every same-typed procedure pair | operational mathematics | new readers refine $q$ |
| Theorem 4 | adequate whole-history packets and optional standard interfaces | every packet satisfying the printed fields | typing theorem | adding $\Lambda_A$ opens contextuality predicates |
| Theorem 5 | finite quantum states and conditional finite combs | every registered preparation, channel, instrument, reader | positive existence construction | global predictive ontology cost remains |
| Theorem 6 | POM, six-rotation, Peres--Mermin, CHSH fragments | no one model satisfying all nine premises | foundations no-go | dropping a premise opens models |
| Theorem 7 | any adequate packet and bound finite/countable/Borel fiber | existence of infinitely many refinements | mathematical | fiber reader splits equivalence |
| Theorem 8 | invariants natural under explicit admitted idle projections | every such invariant is fiber-blind; further descent only along an admitted chain | conditional no-selection | a new principle may refuse reduction |
| Theorem 9 | positive contextual model class | at least two nonisomorphic realizations; no selector | structural/nonselection | new experiment may discriminate |
| Theorem 10 | finite states and complete finite-process testers | every compatible effect/tester | operational/representation | source/composition contract matters |
| Theorem 11 | fixed channel/task/cut/Markov/tensor classes | minima within each class | resource mathematics | model-class change moves minimum |
| Theorem 12 | registered records and adequate completions | every record-preserving morphism | operational plus actuality scope | micro-reader enlarges domain |
| Theorem 13 | admitted possible Barandes completions | compatibility, not universal existence | ontology boundary | complete law/referent still needed |

All equalities are exact. Finite outcomes are used in the explicit controls.
Standard-Borel extensions require countable additivity and measurable policies.
No relativistic locality, internal time, geometry, or gravitational dynamics
enters any row.

## 18. Construction product and outcome rung

The green-unreviewed construction-level product is:

```text
procedure       P02V2-PHYSICAL-PROCEDURE-CATEGORY-CONSTRUCTED
presentation    P02V2-PROCEDURE-PRESENTATION-GROUPOID-CONSTRUCTED
quotient        P02V2-OPERATIONAL-QUOTIENT-FUNCTOR-CONSTRUCTED-SCOPED
adequacy        P02V2-PROCEDURE-LEVEL-ADEQUATE-PACKETS-CONSTRUCTED
standard-ontic  P02V2-STANDARD-ONTOLOGICAL-SUBCLASS-TYPED
context         P02V2-CONTEXTUALITY-FACTORIZATION-TYPED
positive-model  P02V2-POSITIVE-CONTEXTUAL-MODEL-CONSTRUCTED
no-go           P02V2-NONCONTEXTUAL-COMPLETION-NOGO-WITH-PRINTED-PREMISES
fibers          P02V2-IDLE-ONTOLOGY-FIBERS-CLASSIFIED
selection       P02V2-IDLE-FIBER-NOSELECTION-THEOREM
particular      P02V2-PARTICULAR-CONTEXTUAL-ONTOLOGY-UNSELECTED
phase           P02-PHASE-COMPLETE-PREDICTIVE-STATE-FORCED
scalar          P02-COMPLEX-SCALAR-ONTOLOGY-REPRESENTATION-NONUNIQUE
positivity      P02-POSITIVE-RECORD-LAWS-SURVIVE
bell            P02-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
memory          P02-RESOURCE-INVARIANTS-CLASSIFIED-SCOPED
record          P02-OPERATIONAL-RECORD-INVARIANT
actuality       P02-RECORD-ACTUALITY-POSTULATED
                + P02-MICROACTUALITY-UNCONSTRUCTED
barandes        P02V2-BARANDES-ONTOLOGY-ADMISSIBLE-BUT-UNCONSTRUCTED-AND-UNSELECTED
discriminator   P02V2-EXTRA-ONTOLOGY-DISCRIMINATOR-NONE-IN-DOMAIN
ontology        P02V2-ONTOLOGY-UNDERDETERMINED
downstream      P02V2-NO-CLOCK-QFT-SPACETIME-GRAVITY-PROMOTION

overall ceiling
                P02V2-CANONICAL-QUOTIENT-WITH-TYPED-STRUCTURAL-CONTEXTUALITY-AND-IDLE-FIBER-NONSELECTION
```

This is rung 7 of the frozen ladder. It is a construction claim only and may
be lowered by independent review. No representation-invariant microontology
or empirical discriminator is constructed.

## 19. What the construction says about reality

The positive result is that complete laboratory practice fixes a canonical,
phase-complete structure of preparations, processes, instruments, records,
and composition. Contextuality is not a defect of notation: quantum theory
does not admit one positive affine system-facing description that ignores how
every operational equivalence class is physically implemented while also
satisfying all the printed premises.

The negative result is equally important. Contextuality does not tell us
which contextual ontology is real. The predictive-object model is positive
but largely redescribes quantum theory. Idle variables and alternative
realizers can be added without moving the registered facts. Complex numbers,
minimal dilations, and efficient encodings remain representations or
class-relative resources rather than selected substances.

The construction therefore avoids two opposite mistakes:

1. it does not treat operational equivalence as proof that only the quotient
   exists; and
2. it does not treat one adequate contextual realization as nature's hidden
   machinery.

A later theory must earn additional ontology through a new physical
principle or an experiment on which adequate completions differ. It cannot
derive spacetime by renaming laboratory order or by counting latent states.

## 20. Primary-source bridges

The new procedure/descent architecture follows the operational ordering of
R. W. Spekkens, “Contextuality for preparations, transformations, and
unsharp measurements,” *Physical Review A* 71, 052108 (2005),
[arXiv:quant-ph/0406166](https://arxiv.org/abs/quant-ph/0406166): procedures
are primary, operational equivalence is equality of all relevant statistics,
ontological assignments are procedure indexed, and noncontextuality requires
dependence only on the equivalence class. The parity-oblivious and
transformation witnesses are reconstructed rather than imported by name.

The remaining primary comparators and their retained scopes are:

1. Spekkens et al., preparation contextuality and parity-oblivious
   multiplexing, [arXiv:0805.1463](https://arxiv.org/abs/0805.1463);
2. Ferrie and Emerson, frame negativity,
   [arXiv:0711.2658](https://arxiv.org/abs/0711.2658);
3. Pusey--Barrett--Rudolph, with preparation independence explicit,
   [arXiv:1111.3328](https://arxiv.org/abs/1111.3328);
4. McKague, exact realification,
   [arXiv:1109.0795](https://arxiv.org/abs/1109.0795);
5. Li et al., natural real-network comparison,
   [arXiv:2111.15128](https://arxiv.org/abs/2111.15128);
6. Hoffreumon and Woods, unrefereed adversarial source-contract comparator,
   [arXiv:2603.19208](https://arxiv.org/abs/2603.19208);
7. Kuramochi and Buscemi, statistical sufficiency,
   [arXiv:1701.03394](https://arxiv.org/abs/1701.03394) and
   [arXiv:1004.3794](https://arxiv.org/abs/1004.3794);
8. Montina, Markovian ontological dimension,
   [arXiv:0711.4770](https://arxiv.org/abs/0711.4770);
9. Chiribella--D'Ariano--Perinotti, finite quantum networks,
   [arXiv:0904.4483](https://arxiv.org/abs/0904.4483); and
10. J. A. Barandes, indivisible stochastic processes,
    [arXiv:2507.21192](https://arxiv.org/html/2507.21192v1).

No source selects a v17 ontology or supplies spacetime.

## 21. Construction boundary

This is a mathematics-only author construction under the frozen pin. It has
not undergone the required three mutually blind reviews. It performs no new
experiment, implementation, numerical fit, actualization, clock, QFT,
spacetime, or gravity construction.

The next legitimate event is an author construction audit, followed—only if
that audit passes—by a frozen hostile-review protocol. Paper 03 remains
closed.
