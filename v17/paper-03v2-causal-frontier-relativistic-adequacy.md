# Causal-frontier typed relativistic quantum-operational adequacy

Date: 2026-08-22

Status: **GREEN-UNREVIEWED MATHEMATICS**

## Abstract

We construct a category of finite relativistic laboratory procedures whose
causal admissibility is encoded in its boundary objects rather than imposed as
a partial composition rule. A laboratory packet supplies a finite partial
order of operation slots. Boundary frontiers are lower sets. Primitive arrows
fill exactly one enabled slot, and arbitrary procedures are paths in the
resulting graph. Therefore every pair of genuinely matching arrows composes,
identities and associativity are exact, and a forbidden timelike reversal is
absent by type. Certified incomparable operations become exchangeable only
after their full localized instruments satisfy causal factorization.

The syntax carries two compatible semantics. A covariant Markov-kernel
functor propagates predictive states, records, and probabilities. A
contravariant Heisenberg functor composes algebraic instruments. Under declared
locally covariant AQFT, localized system--probe, normality, measurability, and
state-closure hypotheses, the construction gives normalized positive
histories, prefix coherence, spacelike schedule independence, nonselective
no-signalling, selective steering with record cost, and Bell compatibility.
Complete operational equivalence is a congruence and produces a scoped
reachable quotient.

The result removes only undeclared coordinate and scheduling dependence. A
contingent state or apparatus may select a detectable rest frame. The slot
partial order is declared laboratory protocol, not fundamental happenings,
spacetime points, a global clock, or emergent geometry. The positive history
is global predictive bookkeeping, not a selected local microontology. AQFT,
spacetime, state, actuality, and gravity remain inputs or unconstructed.

Provisional ceiling:

```text
P03V2-LOCALLY-COVARIANT-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

No result is terminal before independent review.

## 1. Scope and input

### 1.1 Scientific aim

The question is not whether one can draw a relativistic circuit. It is whether
the surviving positive quantum-process representation can be made exactly
compositional on relativistic laboratory protocols without inserting a
collapse surface or a hidden total time order.

We assume a declared comparator packet

$$
\Xi=(M,\mathcal A,\mathfrak S,\mathsf L,
     \mathsf{Probe},\mathsf{Reader},\mathsf{Kernel}).
$$

Here $M$ is an oriented, time-oriented, globally hyperbolic Lorentzian
spacetime; $\mathcal A$ is a locally covariant algebra theory on the registered
region net; $\mathfrak S(M)$ is the measurable admitted predictive-state
class; $\mathsf L$ is one finite laboratory slot structure; and the remaining
fields provide localized probes, readers, and finite or standard-Borel
instruments.

Every source correlation, calibration, apparatus state, guard, record
alphabet, and reader used below is packet data. Nothing selects the packet as
the law of nature.

### 1.2 Main nonclaims

This paper does not derive:

- the Lorentzian background, dimension, orientation, or causal order;
- the algebra net or an interacting four-dimensional QFT;
- a preferred or cosmological quantum state;
- a collapse hypersurface;
- a local hidden-variable model or Bell-local causation;
- a microscopic configuration ontology;
- one actual history;
- internal time, spacetime emergence, metric dynamics, or gravity; or
- a discrete web of fundamental entities.

The finite slot system is an operational type system for a registered
experiment.

## 2. Locally covariant state and observable typing

### Definition 2.1 — comparator variance

Let `Loc` have oriented, time-oriented, globally hyperbolic spacetimes as
objects and orientation/time-orientation-preserving isometric embeddings with
causally convex image as arrows. Let

$$
\mathcal A:\mathbf{Loc}\longrightarrow\mathbf{Alg}
$$

be covariant. For $\psi:M\to N$, write
$\alpha_\psi=\mathcal A(\psi)$.

States restrict contravariantly:

$$
\psi^*\nu=\nu\circ\alpha_\psi.
$$

No canonical extension $\mathfrak S(M)\to\mathfrak S(N)$ is assumed for a
proper embedding.

### Proposition 2.2 — evaluation naturality

For $A\in\mathcal A(M)$ and $\nu\in\mathfrak S(N)$,

$$
(\psi^*\nu)(A)=\nu(\alpha_\psi(A)).
$$

**Proof.** This is the definition of state pullback. Its content is variance:
the equality compares one observable and one state through the algebra
intertwiner, not through coordinate names. $\square$

### Definition 2.3 — admitted state closure

The measurable state class is part of the packet. Besides pullback closure,
it must satisfy, for every registered finite positive-support branch,

$$
\omega\in\mathfrak S(M)
\Longrightarrow
\frac{\omega\circ\mathcal J_{s,B}}
     {\omega(\mathcal J_{s,B}(1))}
\in\mathfrak S(M),
$$

and it must be closed under every registered nonselective update and adaptive
composite. In represented $W^*$ packets the relevant maps are normal. A
Hadamard or microlocal class is admitted only after a model-specific
preservation proof.

This is an admission theorem, not a natural-state selector.

## 3. Finite causal slot structures

### Definition 3.1 — slots

The laboratory slot structure is

$$
\mathsf L=(V,\prec,\operatorname{supp},
           \operatorname{port},\operatorname{guard}),
$$

where $V$ is finite, $\prec$ is a strict partial order, supports are compact
subsets of $M$, ports are typed, and guards depend only on retained records
from predecessor slots.

Admission requires:

1. port and record dependencies follow $\prec$;
2. if one support lies entirely to the causal past of another, the slots are
   ordered in that direction;
3. incomparable slots have no hidden port, record, or source dependence; and
4. a pair is called exchangeable only after its complete operation maps obey
   the named causal-factorization theorem.

Overlapping or causally mixed supports require a separately typed joint
mechanism. No total ranking is physical data.

### Definition 3.2 — frontiers

A completed frontier is a lower set $D\subseteq V$:

$$
v\in D,\ u\prec v\Longrightarrow u\in D.
$$

A slot $v\notin D$ is enabled when every predecessor lies in $D$ and its
guard is typed by records already present at $D$.

### Definition 3.3 — boundary objects

The boundary object at $D$ is

$$
B_{\Xi,D}=(\Xi,D,\mathsf P_D,\mathsf R_D,\mathsf X_D),
$$

where $\mathsf P_D$ is the open quantum/probe-port schema,
$\mathsf R_D$ the retained classical-record schema, and $\mathsf X_D$ the
standard-Borel predictive-state/reader type.

A boundary value contains an actual predictive object and record values.
Values are not object types.

### Proposition 3.4 — no serialization clock

Completing incomparable slots $v$ and $w$ in either order lands on the same
frontier $D\cup\{v,w\}$. The frontier does not retain a topological-sort index.

**Proof.** Set union is independent of insertion order. Lower-set closure is
preserved because both slots are enabled. $\square$

This proposition removes arbitrary laboratory serialization only. It does not
derive physical time.

## 4. The physical procedure category

### Definition 4.1 — primitive mechanism arrows

For every enabled $v\notin D$ and admitted mechanism $m$ at that slot, define

$$
g_{v,m,D}:B_{\Xi,D}\longrightarrow B_{\Xi,D\cup\{v\}}.
$$

The exact target port, record, and predictive types are determined by the
mechanism interface. Different mechanisms may be parallel arrows only when
these interfaces agree.

The generator set contains preparation, localized coupling/instrument,
trusted randomization, controlled operation, record write/read,
coarse-graining, discard, and explicit skip. A false guard selects the typed
skip branch of one complete controlled operation.

The explicit skip has type

$$
\operatorname{skip}_{v,D}:B_{\Xi,D}\to B_{\Xi,D\cup\{v\}}.
$$

It is not an identity: it consumes a laboratory opportunity and changes the
compatible-future interface.

### Definition 4.2 — path category

Let $G_\Xi$ be the directed multigraph of admitted boundary objects and
primitive arrows. Define

$$
\mathcal P_\Xi=\operatorname{Path}(G_\Xi).
$$

Objects are the vertices. Morphisms are finite directed paths. Identity is the
empty path and composition is concatenation.

### Theorem 4.3 — ordinary category theorem

$\mathcal P_\Xi$ is a small category. Every pair with exactly matching
codomain/domain composes, and composition is associative.

**Proof.** The path category of a small directed multigraph is a category.
Concatenation is defined for every matching pair. Empty paths are two-sided
identities. Concatenation of finite paths is associative. No physical
admissibility predicate is consulted after the graph is formed. $\square$

### Corollary 4.4 — the v1 timelike counterexample is blocked by type

Let $v_-\prec v_+$. The early operation has source/target

$$
B_D\longrightarrow B_{D\cup\{v_-\}},
$$

and the later operation has source/target

$$
B_{D\cup\{v_-\}}
\longrightarrow B_{D\cup\{v_-,v_+\}}.
$$

They are not endomorphisms of one boundary. The set
$D\cup\{v_+\}$ is not a lower set, so no later-first primitive arrow exists.

**Proof.** Immediate from Definitions 3.2 and 4.1. $\square$

### Proposition 4.5 — same-slot procedure alternatives survive

Two admitted mechanisms $m,m'$ with the same slot and exact interface define
parallel arrows. Procedure identity can therefore be finer than operational
equivalence without asking a quotient arrow to remember erased data.

This preserves the procedures-first contextuality architecture.

## 5. Algebraic and probabilistic semantics

### Definition 5.1 — boundary value spaces

For each boundary object let $X_D$ be its standard-Borel space of admitted
predictive objects and retained record values.

Let `Kern` be the category of standard-Borel spaces and Markov kernels. A
finite instrument is represented by its complete outcome kernel; a continuous
instrument uses the packet's countably additive kernel.

### Definition 5.2 — state/record evaluation functor

Each primitive mechanism supplies a normalized kernel

$$
K_{v,m,D}:X_D\longrightarrow\operatorname{Prob}(X_{D\cup\{v\}}).
$$

Define

$$
\operatorname{Ev}_\Xi:\mathcal P_\Xi\longrightarrow\mathbf{Kern}
$$

by sending a path to the chronological composite of its primitive kernels.

### Proposition 5.3 — functoriality

$\operatorname{Ev}_\Xi$ maps empty paths to identity kernels and path
concatenation to kernel composition.

**Proof.** This is the recursive definition of path evaluation. Identity and
associativity are the identity and associativity laws in `Kern`. $\square$

### Definition 5.4 — Heisenberg semantics

Each localized mechanism also supplies its complete algebraic instrument map.
Physical chronological composition reverses on observables. Hence there is a
contravariant semantics

$$
\operatorname{Heis}_\Xi:
\mathcal P_\Xi^{\mathrm{op}}\longrightarrow\mathbf{CP}_\Xi,
$$

where $\mathbf{CP}_\Xi$ is the packet's category of admitted unital/nonselective
and branch CP maps with their typed classical outputs.

For physical operations $1$ then $2$, state/record kernels compose as
$K_2\circ K_1$, while an initial state evaluates the Heisenberg composite
$\mathcal J_1\circ\mathcal J_2$.

### Proposition 5.5 — semantic compatibility

For every finite path and complete reader, the probability obtained by
`Ev` equals evaluation of the corresponding composed Heisenberg instrument in
the input predictive state.

**Proof.** For one generator this is the definition of its state-update
kernel. Induction uses the conditional-state identity and the tower property.
Zero-support branches contribute zero and are never normalized. $\square$

## 6. Localized system--probe instruments

### Definition 6.1 — one scheme

A localized scheme contains

$$
s=(\mathcal A,\mathcal B,K,\Theta,\sigma,\mathsf E),
$$

with compact coupling region $K$, probe algebra/theory $\mathcal B$, initial
probe state $\sigma$, scattering automorphism $\Theta$, and a finite POVM or
typed standard-Borel probe instrument.

For a positive probe effect $B$, define

$$
\mathcal J_{s,B}(A)
=(\operatorname{id}\otimes\sigma)\Theta(A\otimes B).
$$

The tensor product and the outgoing-to-incoming scattering convention are
fixed by the packet.

### Theorem 6.2 — CP and normalization

$\mathcal J_{s,B}$ is CP. For a complete finite POVM $\{B_r\}$,

$$
\sum_r\mathcal J_{s,B_r}=\mathcal J_{s,1},
\qquad
\mathcal J_{s,1}(1)=1.
$$

In a $W^*$ packet the conclusion is normal CP when the scattering map and
slice are normal.

**Proof.** The insertion

$$
A\longmapsto
(1\otimes B^{1/2})(A\otimes1)(1\otimes B^{1/2})
$$

is CP. Composition with a star automorphism and a positive slice is CP.
Linearity, POVM completeness, and unitality prove normalization. $\square$

### Definition 6.3 — standard-Borel instrument

For a nonatomic outcome space $(\Omega,\Sigma)$, the packet supplies a
countably additive CP instrument measure

$$
\Delta\longmapsto\mathcal J_s(\Delta),
$$

and

$$
\mu_\omega(\Delta)
=\omega\!\left(\mathcal J_s(\Delta)(1)\right).
$$

Regular conditional posteriors are used only almost everywhere. No point
posterior is assigned to an arbitrary null singleton.

### Theorem 6.4 — localization scope

Under the Fewster--Verch localized-coupling comparison hypotheses and the
packet's named Haag property or exact substitute, the induced observable is
localized in the causal hull of $K$, and the nonselective operation acts
identically on registered observables spacelike to that hull.

The hypotheses are part of packet admission; this is not a theorem for an
arbitrary CP map.

## 7. Causal factorization and scheduling

### Definition 7.1 — factorizing family

A finite multi-probe family is admitted for the factorization theorem only if:

1. every coupling region and support relation is typed;
2. independent probes use the declared product preparation source;
3. any source correlation is exposed as a different joint mechanism; and
4. the composite scattering maps satisfy the named causal-factorization
   identities on the full registered domain.

### Theorem 7.2 — incomparable exchange

For two enabled incomparable slots $v,w$ whose complete mechanism maps
causally factorize,

$$
\operatorname{Ev}(g_wg_v)
=\operatorname{Ev}(g_vg_w),
$$

with the corresponding exchange of classical records. The Heisenberg
instrument maps also agree in the two orders.

**Proof.** This is the causal-factorization identity for causally disjoint
localized couplings, including the declared product source and complete
outcome maps. $\square$

### Definition 7.3 — exchange congruence

Let $\sim_{\rm ex}$ be the least category congruence generated by every
certified incomparable exchange. It is not a composition predicate.

### Corollary 7.4 — finite schedule independence

All linear extensions of one finite slot partial order give the same complete
kernel and Heisenberg operation after record exchange.

**Proof.** Any two linear extensions are joined by adjacent swaps of
incomparable elements. Apply Theorem 7.2 at each swap. $\square$

Timelike order, record dependence, and source correlation are not exchanged.

## 8. No-signalling, steering, and Bell scope

### Theorem 8.1 — nonselective no-signalling

Let $\{B_a\}$ be a complete localized instrument in one slot and $D_b$ a
registered spacelike reader effect. Then

$$
\sum_a p(a,b\mid\omega)
=\omega\!\left(\mathcal J_{A,1}(D_b)\right)
=\omega(D_b).
$$

**Proof.** Sum every local outcome, then use the localized nonselective
operation theorem. Microcausal commutation alone is not used. $\square$

### Proposition 8.2 — selective steering

For a positive-support retained result $a$, the conditional

$$
p(b\mid a,\omega)
=\frac{p(a,b\mid\omega)}{p(a\mid\omega)}
$$

may differ from $p(b\mid\omega)$. This does not signal: the branch is random,
and comparing the conditional subensemble requires the retained classical
record.

The exact singlet calculation is a finite split/type-I calibration, not a
generic regional tensor-factor theorem.

### Proposition 8.3 — Bell premise ledger

A Bell-local completion requires one setting-independent source measure and

$$
p(a,b\mid x,y,\lambda)
=p_A(a\mid x,\lambda)p_B(b\mid y,\lambda).
$$

The split-qubit calibration gives $S=2\sqrt2$ with unbiased local marginals.
The Summers--Werner theorem supplies an existential QFT observable/state
control under its own hypotheses. Neither constructs an exact localized probe
for every ideal Bell observable.

Thus Einstein causality, operation-level no-signalling, Bell factorization,
parameter independence, outcome independence, and measurement independence
remain distinct predicates.

## 9. Presentation and complete operational quotient

### Definition 9.1 — presentation groupoid

The presentation groupoid acts by:

- coordinate changes with the entire physical packet transported;
- bijective renaming of slots, ports, probes, and records;
- reassociation of constructor syntax; and
- certified incomparable schedule exchange.

It preserves occurrence multiplicity, lower-set incidence, supports, physical
causal order, mechanisms, source correlations, states, effects, records, and
readers. It acts functorially on $\mathcal P_\Xi$ and intertwines both semantic
functors.

Let $\sim_{\rm pres}$ be the least category congruence generated by this
functorial presentation action together with the certified exchange congruence
$\sim_{\rm ex}$. Define the physical-procedure presentation quotient

$$
\mathcal P_{\rm rel}^{(2)}
=\mathcal P_\Xi/\!\sim_{\rm pres}.
$$

The quotient may be taken over a disjoint union of explicitly isomorphic
packet presentations when the full packet isomorphisms of Definition 10.1 are
supplied. No quotient across unrelated packets is implied.

### Definition 9.2 — complete operational equivalence

For parallel procedures $p,p'$ in $\mathcal P_{\rm rel}^{(2)}$ for the same
admitted packet/skeleton, write
$p\sim_{\rm op}p'$ when every compatible prefix, localized ancillary probe,
adaptive continuation, record operation, and complete reader gives the same
joint law in every registered state/context.

### Theorem 9.3 — congruence

$\sim_{\rm op}$ is a category congruence.

**Proof.** Precomposition and postcomposition with any path produce another
registered one-hole context. Controlled operations, trusted randomization,
coarse-graining, record handling, and ancillary probes are included in the
frozen context family. Equality under every complete tester is therefore
preserved by each constructor and by composition. $\square$

### Theorem 9.4 — reachable quotient

The quotient

$$
q_{\rm rel}^{(2)}:\mathcal P_{\rm rel}^{(2)}
\longrightarrow\mathcal Q_{\rm rel}^{(2)}
$$

is a well-defined category on the registered reachable interface. Every
prediction functor constant on operational classes factors uniquely through
$q_{\rm rel}^{(2)}$.

**Proof.** Quotient a category by the congruence of Theorem 9.3. The universal
property is the standard quotient universal property. $\square$

The result is within one packet/skeleton or a separately typed packet
isomorphism. New readers, packets, or common refinements may refine the
quotient. No microscopic inverse is inferred.

## 10. Full packet covariance

### Definition 10.1 — packet isomorphism

A packet isomorphism transports and intertwines:

1. the comparator and region supports;
2. system, probe, and coupled theories;
3. the scattering maps;
4. probe states and effects;
5. slot posets, lower sets, ports, guards, and records;
6. every source correlation;
7. reader families; and
8. predictive/history measurable maps.

### Theorem 10.2 — transported law

Full packet isomorphisms induce isomorphic path categories and intertwine
`Ev` and `Heis`. Therefore every transported complete program has the same
transported joint law.

**Proof.** The packet isomorphism maps objects, enabled-slot generators, and
interfaces bijectively. The stipulated intertwiners give equality on each
primitive semantic map. Induction over paths proves the result. $\square$

A proper `Loc` embedding without these fields supplies only algebra transport
and state pullback, not a transported preparation or program.

## 11. Positive record histories

### Definition 11.1 — primitive history kernel

For a finite branch outcome $r$ at predictive object $\lambda$, define

$$
K_i(r,d\lambda'\mid\lambda)
=p_i(r\mid\lambda)
 \delta_{U_i(\lambda,r)}(d\lambda').
$$

The history record also contains the completed lower-set frontier and retained
classical values. Zero support gives zero mass and no posterior.

For standard-Borel outcomes, use the supplied measure kernel rather than a
point density.

### Theorem 11.2 — normalization and AQFT agreement

For every admitted finite path, iterating the complete primitive kernels gives
a normalized positive measure $\Gamma_p$ on complete records and predictive
histories. Every complete registered reader has the same law under
$\Gamma_p$ as under the composed AQFT instrument.

**Proof.** Proposition 5.5 identifies every cylinder mass. Complete instrument
normalization removes the last outcome; induction gives total mass one.
Reader values are measurable pushforwards. $\square$

### Theorem 11.3 — prefix coherence

Marginalizing every complete suffix returns the literal performed-prefix law.

**Proof.** Repeatedly sum/integrate the normalized suffix kernels. $\square$

### Proposition 11.4 — frontier is not automatically division

A lower-set frontier is a protocol boundary. It is a stochastic division only
if equal retained predictive objects and records imply equal future profiles
for every licensed continuation. Otherwise no restart kernel at that frontier
is licensed.

This preserves indivisibility at insufficient cuts.

### Cost theorem 11.5

The positive latent object is the complete predictive state or conditional
process object. It may encode global entanglement and all memory needed for
future sufficiency. It is contextual, background dependent, experiment
indexed, and not selected by the representation theorem.

Therefore $\Gamma_p$ is a positive operational representation, not a local
microontology or an actuality law.

## 12. Contextuality and idle fibers

### Proposition 12.1 — same-slot preparation contextuality control

In a declared split/type-I calibration, use one preparation slot with two
distinct mechanisms:

$$
\tfrac12\delta_{|0\rangle\langle0|}
+\tfrac12\delta_{|1\rangle\langle1|}
\ne
\tfrac12\delta_{|+\rangle\langle+|}
+\tfrac12\delta_{|-\rangle\langle-|}.
$$

Fix the same complementary state. The complete global barycenters agree while
the predictive-state measures have different supports. The two procedures
have the same source/target frontier type and operational image but different
system-facing positive representations.

Thus a system-facing assignment need not factor through the operational
quotient. No procedure-name tag is used.

### Proposition 12.2 — idle-fiber nonselection

For any normalized standard probability space $(Z,\zeta)$, the inflation

$$
\widetilde\Gamma_p=\Gamma_p\otimes\zeta
$$

with projection $\pi(\lambda,z)=\lambda$ preserves every registered
prediction. No invariant natural under this admitted projection selects the
idle coordinate or its prior.

This does not prove that such a coordinate exists or that every hidden
structure is idle.

## 13. Frame theorem

### Theorem 13.1 — covariance without a scheduling frame

Within the registered domain:

1. jointly transported packet data obey Theorem 10.2; and
2. certified incomparable serializations obey Corollary 7.4.

Hence no undeclared coordinate chart, loop order, or scheduling foliation
changes the registered law.

### Proposition 13.2 — physical rest-frame control

Let $\beta_v$ be a boost automorphism and choose an admitted state $\omega$
that is not boost invariant. Then for some local observable $A$,

$$
\omega(A)\ne\omega(\beta_v(A)).
$$

In particular, an inertial KMS state can select a thermal rest frame. This is
physical state data, not a covariance failure.

Theorems 10.2 and 13.1 compare jointly transported data and remain true.

### Corollary 13.3 — exact frame scope

The construction earns no undeclared scheduling-frame dependence. It does not
earn invariance of every state/apparatus and does not exclude an empirically
idle preferred microscopic structure.

## 14. Type III, split, Reeh--Schlieder, gauge, particles, and continuum

### Proposition 14.1 — algebraic-state sufficiency

The instrument and history formulas use positive functionals, effects, and
positive/normal CP maps. They do not require an intrinsic regional density
matrix, trace, finite Kraus list, or tensor factor. Any use of those objects
requires a model-specific representation theorem.

### Proposition 14.2 — split conditional

For a separated inclusion with a collar and a verified type-I intermediate
factor, the declared calibration may use matrix subalgebras and tensor-product
independence. This does not extend to touching regions or arbitrary gauge
systems and does not define a lattice cell.

### Proposition 14.3 — Reeh--Schlieder cost

Dense local action on a cyclic vector does not provide deterministic
bounded-cost remote preparation. Norm growth, success probability,
postselection, and record cost remain exposed. The complete operation obeys
Theorem 8.1.

### Type firewalls

Observable algebras, charged fields, gauge actions, sectors, Wilson/flux
operators, regional centers/edges, and records are distinct types. No gauge
group, charge spectrum, statistics, particle number, Fock representation, or
actualized sector is selected.

The abstract-net result constructs no interacting 3+1 model. A free-field,
finite-mode, or lattice control is not universal dynamics or spacetime
ontology. Cutoff removal requires a separate convergence and renormalization
theorem. Relative Cauchy evolution is response to a declared background
perturbation, not metric dynamics or gravity.

## 15. Theorem-target disposition

| Target | Construction disposition | Exact boundary |
|---|---|---|
| V2-T1 | constructed | finite slot poset and lower sets |
| V2-T2 | constructed | one enabled-slot extension per primitive arrow |
| V2-T3 | constructed | free path category theorem |
| V2-T4 | constructed | timelike v1 counterexample killed by type |
| V2-T5 | constructed conditionally | full map causal factorization only |
| V2-T6 | constructed | adjacent incomparable exchanges |
| V2-T7 | constructed | functorial multiplicity-preserving presentation action |
| V2-T8 | constructed | complete context-family congruence |
| V2-T9 | constructed scoped | reachable packet quotient |
| V2-T10 | constructed as admission condition | model-specific closure proof required |
| V2-T11 | constructed | finite normalization; supplied measure kernels for continuous outcomes |
| V2-T12 | constructed | full packet isomorphisms; proper-embedding pushforward refused |
| V2-T13 | constructed conditionally | exact localization hypotheses |
| V2-T14 | constructed | nonselective theorem plus steering control |
| V2-T15 | constructed as compatibility | QFT existence and qubit calibration separated |
| V2-T16 | constructed | positive normalization and prefix coherence |
| V2-T17 | refusal constructed | lower-set frontier not automatically division |
| V2-T18 | constructed | no scheduling frame; physical state frame allowed |
| V2-T19 | refusal/conditional controls constructed | no model collage |
| V2-T20 | unconstructed as required | ontology/actuality/spacetime/gravity |

## 16. Two-way controls

| ID | Positive direction | Hostile direction | Result |
|---|---|---|---|
| C1 | lower-set frontier | non-down-closed set refused | pass |
| C2 | enabled-slot extension | predecessor omission refused | pass |
| C3 | same-slot parallel mechanisms | procedure identity retained | pass |
| C4 | empty path identity | explicit skip distinct | pass |
| C5 | same incomparable frontier | rank/loop token absent | pass |
| C6 | certified exchange | correlated/linked pair not exchanged | pass |
| C7 | timelike types | reverse word absent by source/target | pass |
| C8 | multiplicity-bearing slots | isomorphic occurrences retained | pass |
| C9 | past-record guard | future guard refused | pass |
| C10 | context family closed | missing constructor kills theorem | pass |
| C11 | full packet transport | equal scalar shortcut refused | pass |
| C12 | state pullback | canonical proper-embedding pushforward refused | pass |
| C13 | normal class-preserving update | nonnormal/out-of-class packet refused | pass |
| C14 | measure kernel | null-point posterior refused | pass |
| C15 | product source exposed | correlated source distinct | pass |
| C16 | localized complete operation | commutator shortcut refused | pass |
| C17 | steering plus record | conditional not marginal | pass |
| C18 | Bell ledger | microcausality not factorization | pass |
| C19 | physical KMS/apparatus frame | fixed-state invariance not inferred | pass |
| C20 | no scheduling frame | hidden idle structure not excluded | pass |
| C21 | algebraic type-III formulation | generic density/trace/Kraus/tensor refused | pass |
| C22 | split with collar | touching factorization refused | pass |
| C23 | positive global history | local microontology refused | pass |
| C24 | typed record | division/actuality not inferred | pass |
| C25 | declared comparator | emergent spacetime refused | pass |
| C26 | background response | gravity refused | pass |
| C27 | laboratory slots | discrete-universe reading refused | pass |
| C28 | procedure context retained | run/procedure tag excluded | pass |

## 17. Hostile-attack disposition

1. The v1 same-boundary timelike pair fails Corollary 4.4.
2. Deleting $D$ destroys boundary typing and T1--T4.
3. A non-down-closed frontier is not an object.
4. A later slot before its predecessor is not enabled.
5. A second composition predicate is forbidden by Definition 4.2.
6. Skip and identity have different targets.
7. No topological-sort index appears in objects or kernels.
8. Slot bijections preserve two distinct occurrences.
9. Source-correlated slots fail Definition 7.1.
10. Record-linked slots are comparable and not exchanged.
11. A future record cannot type a guard.
12. Omitting a constructor invalidates Theorem 9.3 rather than passing it.
13. Physical support is not presentation gauge.
14. Coordinate transport without state/apparatus transport is not packet
    isomorphism.
15. Proper embeddings provide no canonical state pushforward.
16. Scattering maps must intertwine under packet transport.
17. A nonnormal $W^*$ update is outside the admitted packet.
18. Leaving $\mathfrak S(M)$ violates Definition 2.3.
19. A zero-support finite branch remains zero.
20. A nonatomic singleton receives no canonical posterior.
21. Probe/source correlations are exposed packet fields.
22. No-signalling uses operation locality, not commutation alone.
23. A selected conditional is not a remote marginal.
24. Postselection comparison consumes the retained record.
25. QFT Bell observables are not automatically exact probe realizations.
26. Free-field, split, Bell, and gauge controls remain separate models.
27. Type-III local states need no intrinsic density matrix.
28. Touching regions are not tensor factors by default.
29. Reeh--Schlieder density is not deterministic control.
30. No universal natural or Hadamard state is selected.
31. Proposition 13.2 blocks the false no-rest-frame inference.
32. Schedule equality does not exclude idle microscopic structure.
33. Slots are laboratory protocol positions, not happenings.
34. Slot counts are not volume, duration, or entropy.
35. The positive predictor is not a local Bell variable.
36. Frontier alone is not complete division.
37. Conditioning, decoherence, and record formation do not actualize.
38. No v16 order, metric, FLRW, selector, or fusion result is imported.
39. Abstract AQFT mathematics constructs no interacting 3+1 model.
40. Paper 04 and gravity remain closed.

## 18. Product

| Coordinate | Provisional status | Exact boundary |
|---|---|---|
| input | `BOUND` | terminal Papers 01/02 v2, v1 salvage, declared AQFT packet |
| slot-skeleton | `DECLARED-LABORATORY-PROTOCOL` | finite partial order, not ontology |
| frontier | `CONSTRUCTED-TYPE` | lower set, not automatic division |
| boundary | `CONSTRUCTED` | ports, records, predictive/reader types |
| procedure | `CONSTRUCTED` | free path category |
| presentation | `CONSTRUCTED` | functorial, multiplicity preserving |
| quotient | `CONSTRUCTED-SCOPED` | complete reachable within-packet interface |
| covariance | `CONSTRUCTED-CONDITIONALLY` | full packet isomorphism; proper-embedding pullback only |
| state-class | `DECLARED-AND-CLOSED-WHEN-ADMITTED` | model-specific preservation |
| instrument | `CONSTRUCTED` | CP; normal in admitted $W^*$ packets |
| causal-factorization | `CONSTRUCTED-CONDITIONALLY` | named maps and product-source premise |
| spacelike-schedule | `CONSTRUCTED` | finite linear extensions agree |
| no-signalling | `CONSTRUCTED` | complete nonselective localized operation |
| steering | `CONSTRUCTED-CONTROL` | selected conditional plus record cost |
| bell | `CONSTRUCTED-EXISTENTIAL-COMPATIBILITY` | no universal exact probe |
| positive-model | `CONSTRUCTED-WITH-COSTS` | global/contextual/memory-bearing/unselected |
| context | `CONSTRUCTED` | same-slot procedure witness |
| fibers | `CONSTRUCTED-SCOPED` | admitted positive affine projections |
| type-III | `REFUSAL-CONSTRUCTED / MODEL-SPECIFIC` | no universal density/trace/tensor |
| split | `CONDITIONAL-CONTROL` | separated collar and split/nuclearity |
| gauge | `TYPED-UNSELECTED` | no group/sector derivation |
| particles | `TYPED-UNSELECTED` | no labeled/Fock ontology |
| continuum | `ABSTRACT-NET-CONDITIONAL` | no interacting-model construction |
| UV | `SCOPED` | no hidden cutoff/removal |
| preferred-frame | `NO-UNDECLARED-SCHEDULING-FRAME` | physical rest frames allowed; idle microstructure not excluded |
| record | `CONSTRUCTED-OPERATIONALLY` | persistent classical output |
| division | `FUTURE-SUFFICIENCY-REQUIRED` | frontier alone insufficient |
| actuality | `UNCONSTRUCTED` | no branch selector |
| Barandes | `ADMISSIBLE-BUT-INCOMPLETE` | no universal configuration/law/state/trajectory packet |
| ontology | `GLOBAL-PREDICTIVE-CANDIDATE-UNSELECTED` | not local explanatory microphysics |
| downstream | `CLOSED` | no internal time, spacetime emergence, or gravity |

## 19. Outcome

The provisional strongest supported rung is:

```text
P03V2-LOCALLY-COVARIANT-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

This means:

- relativistic laboratory procedure composition is correctly typed;
- localized quantum instruments and positive histories are compatible with
  the declared relativistic comparator;
- arbitrary spacelike serialization is physically idle;
- no-signalling, steering, and Bell violation retain their distinct meanings;
- the operational quotient is well defined at the frozen interface; and
- the remaining candidate ontology is global, contextual, unselected, and
  empirically underdetermined.

It does not mean that the universe is a causal slot network, that AQFT is
fundamental, that a preferred state or actual history has been selected, or
that spacetime/gravity has been derived.

The candidate remains green-unreviewed. Independent review must reconstruct
the category, both semantic functors, all controls and attacks, and the full
product before any terminal result.

## References

- R. Brunetti, K. Fredenhagen, and R. Verch, “The generally covariant locality
  principle — a new paradigm for local quantum field theory,” 2003.
  https://arxiv.org/abs/math-ph/0112041
- C. J. Fewster and R. Verch, “Quantum fields and local measurements,” 2020.
  https://arxiv.org/abs/1810.06512
- C. J. Fewster and R. Verch, “Measurement in Quantum Field Theory,” 2023.
  https://arxiv.org/abs/2304.13356
- C. J. Fewster, “The split property for locally covariant quantum field
  theories in curved spacetime,” 2016.
  https://arxiv.org/abs/1601.06936
- C. J. Fewster and R. Verch, “Dynamical locality and covariance,” 2012.
  https://arxiv.org/abs/1106.4785
- S. J. Summers and R. Werner, “Maximal violation of Bell's inequalities is
  generic in quantum field theory,” 1987.
  https://doi.org/10.1007/BF01207366
- G. L. Sewell, “On the Question of Temperature Transformations under Lorentz
  and Galilei Boosts,” 2008.
  https://arxiv.org/abs/0808.0803
