# Stable happenings and premetric order

## Durable local facts, complete stochastic frontiers, and the gates for an extensive event measure

### Research-draft status

Date: 2026-08-20

This is a scientific Paper 14 draft. It develops the mathematics of stable
happenings without treating every happening as a Markov checkpoint and without
assuming a background space, time coordinate, causal graph, metric, event
counter, or clock. It does not report an authoritative evaluation of a frozen
Paper 13 implementation. Its strongest claims are conditional structural
theorems with their hypotheses printed below.

The intended terminal object is premetric:

$$
\left[
(\mathsf B,\prec,\mu;\{\operatorname{DivStatus}(F)\}_F)
\right]_{\mathcal G}.
$$

In a presentation, $\mathsf E$ is the finite or countable set of stable record
fact occurrences and $\mathsf B=\mathsf E/\!\simeq$ identifies mutually
dependent components of one indivisible onset. The groupoid transports the
whole bundle incidence structure by isomorphisms. The physical object is its
isomorphism class, not a set of node orbits. Consequently an automorphism may
exchange two anonymous bundles without collapsing their multiplicity.
$\prec$ is the bundle dependency order, $\mu$ is an interval-finite atomic
measure when one has been earned, and each proposed frontier has its own
division status. Nothing in this tuple is yet a spacetime metric.

## Abstract

We separate four structures that are often conflated: durable records,
physical event identity, lawful stochastic restart boundaries, and metric
data. A stable happening is an actual occurrence that leaves a distinguishable
record preserved by every continuation in a declared future grammar. A
complete division frontier is instead an exhaustive, exactly-once cut whose
complete typed state is sufficient for every licensed future probability.
These predicates are logically independent.

We first prove a typed stable-record theorem. Orthogonal writer branches whose
record sectors are intertwined by every future generator remain perfectly
readable after every finite licensed continuation word. This removes
interference between the recorded alternatives and licenses ordinary
probability composition at the complete record boundary. It does not turn an
unrecorded cut, an isolated local record, or every happening into a restart
state.

We then define presentation-independent occurrence germs and derive a
dependency preorder from necessary history support and essential typed
provenance, not from serialization order. Distinct records can be created by
one symmetric indivisible transition and therefore be mutually dependent.
Quotienting mutual dependence produces indivisible happening bundles. Under
covariance and trace-invariance hypotheses, those bundles form a partial order
with no preferred global clock. Locally finite bundle intervals carry a
canonical unit counting measure. Unequal $\Gamma$-derived atomic weights
require an additional descent theorem: a chain-rule surprisal can be invariant
for a whole history while its allocation to incomparable happenings remains
linearization dependent.

The result is a rigorous premetric target. Stable happenings may supply the
atoms of a later geometry, while complete frontiers organize prediction.
Dimension, Lorentzian signature, manifoldlikeness, scale, proper time,
curvature, Einstein dynamics, thermodynamic entropy, energy flux, and
actualization remain unconstructed.

## 1. The physical distinction

A happening does not magically solve stochastic factorization. The useful
engineering analogy is exact:

- a happening is an immutable event-log entry;
- a division frontier is a complete restartable system snapshot;
- an event log may be durable without containing enough state to restart the
  whole system.

The physical claim of this paper is therefore not

> every stable happening is a Markov step,

but rather

> stable happenings provide durable local facts; some complete compatible
> frontiers containing those facts and every other law-relevant degree of
> freedom may qualify as lawful stochastic divisions. Between such frontiers
> the primitive whole-process law need not divide.

This retains the non-Markovian architecture. It also separates ISP's proposed
happening ontology from Barandes's technical use of configurations,
indivisible stochastic laws, and system-relative division events. Stable
happenings and their use as a possible geometric substrate are additions made
here, not definitions or theorems imported from Barandes.

## 2. Exact motivation from the two-state law

At $g=1/2$, let

$$
R=\frac15
\begin{pmatrix}
3&-4\\
4&3
\end{pmatrix},
\qquad
B=|R|^2=\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix}.
$$

For two unrecorded coherent steps,

$$
R^2=\frac1{25}
\begin{pmatrix}
-7&-24\\
24&-7
\end{pmatrix},
$$

so the direct endpoint law is

$$
C=|R^2|^2=\frac1{625}
\begin{pmatrix}
49&576\\
576&49
\end{pmatrix}.
$$

If the intermediate two-state configuration were an autonomous stochastic
restart point, there would be a stochastic matrix $K$ with $C=KB$. Since
$B$ is invertible, the only candidate is

$$
K=CB^{-1}
=\frac1{175}
\begin{pmatrix}
351&-176\\
-176&351
\end{pmatrix}.
$$

For clarity, the superficially similar matrix

$$
B^{-1}=\frac17
\begin{pmatrix}
-9&16\\
16&-9
\end{pmatrix}
$$

is the inverse of $B$ itself, not the failed continuation $CB^{-1}$.

Its negative entries exclude a positive source-independent restart kernel on
that declared carrier and cut. This is a nondivision result. It does not imply
that an actual intermediate configuration is unreal, incomplete, or awaiting
an ontological repair. A history-conditioned, phase-carrying, or enlarged
state can Markovize a representation; whether such extra variables are
physical is a separate question.

When the intermediate alternative writes a stable orthogonal record, the
licensed future may no longer recombine those sectors coherently. The recorded
two-step law is instead

$$
B^2=\frac1{625}
\begin{pmatrix}
337&288\\
288&337
\end{pmatrix},
$$

and the factorization $B^2=B B$ is stochastic. The record has changed the
division structure by blocking interference between the recorded
alternatives; it has not merely appended a descriptive label.

The distinction between

$$
|R^2|^2
\quad\text{and}\quad
|R|^2|R|^2
$$

is the exact reason to count durable occurrences rather than internal paths
through an amplitude calculation.

## 3. Typed stable-record theorem

Let $\mathcal H_0$ be an input representation space and let the writer branch
maps

$$
V_r:\mathcal H_0\longrightarrow\mathcal H_1
$$

satisfy

$$
\sum_r V_r^\dagger V_r=I,
\qquad
P_r^{(1)}V_s=\delta_{rs}V_s,
$$

where the $P_r^{(1)}$ are mutually orthogonal record-sector projectors on the
writer output. Let a licensed future word be typed as

$$
U=F_n\cdots F_1,
\qquad
F_j:\mathcal H_j\longrightarrow\mathcal H_{j+1}.
$$

For every carried record label $r$, assume there are transported projectors
$P_r^{(j)}$ such that

$$
P_r^{(j+1)}F_j=F_jP_r^{(j)}
$$

for every generator and every admitted source. Also require that admitted
continuations are normalized on every reached branch, so conditional reader
probabilities are defined.

### Theorem 1 — finite-word record persistence

For every finite licensed word $U$,

$$
P_r^{(n+1)}U=UP_r^{(1)}.
$$

If writer branch $s$ is selected, then

$$
P_r^{(n+1)}UV_s=\delta_{rs}UV_s.
$$

Consequently the record is perfectly readable after every finite licensed
future word, and distinct recorded alternatives remain orthogonal.

### Proof

The one-generator relation is the hypothesis. If
$P_r^{(j)}F_{j-1}\cdots F_1=F_{j-1}\cdots F_1P_r^{(1)}$, then

$$
\begin{aligned}
P_r^{(j+1)}F_j\cdots F_1
&=F_jP_r^{(j)}F_{j-1}\cdots F_1\\
&=F_j\cdots F_1P_r^{(1)}.
\end{aligned}
$$

Induction proves the first identity. Multiplying on the right by $V_s$ and
using the writer equation proves the second. Each $UV_s\psi$ lies in the
range of $P_s^{(n+1)}$, and those ranges are mutually orthogonal. Therefore

$$
\langle UV_r\psi,UV_s\psi\rangle=0
\qquad(r\ne s).
$$

After normalization, the reader law is

$$
\Pr(\text{reader returns }r\mid s,U)=\delta_{rs}.
$$

∎

### Corollary 1 — grammar-relative division

At a complete record boundary, direct endpoint evaluation agrees with cutting
at the record and summing the mutually exclusive alternatives. Interference
cross terms vanish because the future images occupy orthogonal record
sectors.

This is an all-word theorem for the declared grammar, not a finite-depth
test. It is also deliberately grammar relative. If an old record port is
reactivated and an inverse erases the record, the enlarged grammar fails the
hypothesis rather than contradicting the theorem.

### What Theorem 1 does not prove

It does not prove that a branch is actual, that every future operation in
nature belongs to the grammar, that one local record contains the full state
needed for restart, or that a record label is presentation-independent. Those
are separate actuality, completeness, and quotient questions.

Persistence of one record also does not prove redundant environmental
accessibility or observer-independent objectivity in the stronger quantum-
Darwinist sense. Those claims require a subsystem decomposition, multiple
independent record fragments, and a redundancy theorem not assumed here.

## 4. Abstract physical input

Paper 14 uses the abstract interface

$$
\mathfrak I=(\mathcal C,\mathcal G,\Gamma,\operatorname{Div},\mathcal B,\rho).
$$

For each source $x$, the contract supplies a complete-history space
$\Omega_x$ and a declared Boolean or sigma algebra $\mathcal A_x$ of
classical history events. The record algebra $\mathcal B_x$ is a typed Boolean
subalgebra of $\mathcal A_x$. An internal amplitude decomposition is not
automatically an event in $\mathcal A_x$; record decoherence or another exact
compatibility theorem is required before alternatives can be combined by
ordinary event algebra.

- $\mathcal C$ is a category of complete finite typed relational boundaries
  and licensed continuation fragments.
- $\mathcal G$ is a presentation groupoid acting functorially on those
  boundaries, continuations, records, and probability events.
- $\Gamma_x$ is a countably additive normalized probability law on
  $\mathcal A_x$ for each source $x$. No Markov property is assumed.
- $\operatorname{Div}$ supplies candidate frontiers; it does not certify
  them.
- $\mathcal B_x$ is a Boolean algebra of record events at boundary $x$.
- for $u:x\to y$, $\rho_u$ transports the persistent record subalgebra of
  $\mathcal B_x$ injectively into $\mathcal B_y$.

The transport is functorial:

$$
\rho_{\operatorname{id}_x}=\operatorname{id}_{\mathcal B_x},
\qquad
\rho_{v\circ u}=\rho_v\circ\rho_u.
$$

Continuation transport $\rho$ and presentation transport by $\mathcal G$ are
different operations. Their naturality is a theorem obligation, not an
identification.

An actual history $\omega_*$ is not contained in $\mathfrak I$. It must be
adjoined as an actualization fact or supplied by a later rule. Positive
probability alone does not select it.

## 5. From a record onset to a physical happening

### 5.1 Raw onset germ

A raw onset germ is a finite typed transition fragment in which a nonempty
finite family of semantic record keys changes from absent to present. Its data
are

$$
o=\left(x\xrightarrow{u}y,
\{(E_i,S_i,\pi_i)\}_{i\in J}\right),
$$

where $E_i\in\mathcal B_y$ is a newly active record event, $S_i$ is its
minimal typed relational support, and $\pi_i$ is the raw
producer/provenance data reconstructed from the typed fragment. The onset is
minimal when no proper non-neutral factorization already exposes the same
family.

The index set $J$ need not have one element. One indivisible transition can
create several distinguishable persistent facts. Its component germs remain
distinct record facts, but the order construction below may identify them as
one indivisible happening bundle.

The occurrence identity does not contain a predeclared predecessor ideal.
That would insert the desired order before deriving it.

### 5.2 Presentation and refinement descent

Presentation arrows and neutral refinements relate complete onset-incidence
structures by typed isomorphisms. At the level of a marked germ, the relation
is generated by:

1. the complete $\mathcal G$ action;
2. insertion or deletion of a neutral identity/refinement that exposes no new
   semantic record and changes no continuation law;
3. replacement of a printed label by another label with the same transported
   event, support, and provenance.

Descent must remove label clones and bookkeeping splits while retaining equal
payloads produced at different supports or by different essential provenance.
Most importantly, the physical history is the isomorphism class of the whole
finite incidence structure. It is not the orbit set of its nodes. If an
automorphism exchanges two distinct incomparable occurrences, their pointed
presentations can have the same type, but the unpointed history still contains
two nodes. Cardinality, incidence, and multiplicity are preserved by every
presentation bijection.

This distinction is the point-free analogue of an unlabeled graph: two
automorphic vertices need no individual names, yet the graph still has two
vertices. Counting groupoid node orbits would be a physical error.

### 5.3 Possible, actual, and stable

An occurrence component $e=(o,i)$ is possible from $x$ if its cylinder event
$E_e$ is measurable, has $\Gamma_x(E_e)>0$, and this value transports
covariantly. A marked isomorphism class classifies its occurrence type; an
actual history retains every incidence occurrence and its multiplicity. The
whole onset family is possible when its joint event is measurable and
positive.

It is actual relative to an adjoined history $\omega_*$ if

$$
\omega_*\in E_e.
$$

It is a stable possible type if every licensed continuation transports its
record key injectively to an active record key. A stable record fact is an
actual occurrence component whose type is stable. A stable happening bundle,
defined in Section 7, is an indivisible mutual-dependency class of those
facts.

Thus the hierarchy is

$$
\text{amplitude path}
\;
\not\Rightarrow
\;
\text{possible happening}
\;
\not\Rightarrow
\;
\text{actual happening},
$$

and

$$
\text{actual happening}
\;
\not\Rightarrow
\;
\text{stable record fact}
\;
\not\Rightarrow
\;
\text{complete division frontier}.
$$

## 6. Compatible histories on varying boundaries

Records that first appear on different boundaries cannot simply be
multiplied. Let $e_1,\ldots,e_n$ be stable possible occurrences. They are a
compatible finite family when there is a common admissible future boundary
$z$ to which every record event transports, the transported events belong to
the same Boolean algebra $\mathcal B_z$, and their meet

$$
E_H^{(z)}=\bigwedge_{i=1}^n\rho_{u_i}(E_{e_i})
$$

has positive support.

Different common future boundaries and different transport paths must give
the same event after further common transport. This is a cocone/path-
independence condition. In an operator representation, products of record
projectors are permitted only after this common-boundary typing and
commutation have been established.

### Theorem 2 — persistent compatible meet

Suppose the record transports are injective Boolean homomorphisms, functorial,
and path independent on common cocones. Then the meet of a compatible finite
family is presentation independent and remains active under every licensed
future continuation.

### Proof

A Boolean homomorphism preserves finite meets. Hence for $v:z\to z'$,

$$
\rho_v(E_H^{(z)})
=\bigwedge_i\rho_v\rho_{u_i}(E_{e_i})
=\bigwedge_i\rho_{v\circ u_i}(E_{e_i}).
$$

Functoriality and path independence make the right-hand side independent of
the chosen representative, path, and common cocone. Injectivity prevents a
persistent semantic distinction from being collapsed. ∎

Positive support is a separate hypothesis. Individually possible records can
have an impossible joint meet.

## 7. From dependency preorder to happening bundles

### 7.1 Generating dependency without a sequence index

Generate a relation $e\mathrel{\triangleleft}f$ in either of two ways.

**Co-onset dependence.** If $e$ and $f$ are distinct components of the same
minimal nonfactorizable onset germ, include both
$e\triangleleft f$ and $f\triangleleft e$. This records indivisible joint
creation without choosing an orientation.

**Essential producer dependence.** Include $e\triangleleft f$ when all of the
following hold:

1. every representative onset of $f$ consumes a typed provenance token whose
   unique semantic producer is $e$;
2. neutralizing or deleting that token changes the eligibility, relational
   output, record event, or calibrated $\Gamma$ response of $f$;
3. the relation is invariant under presentation transport, neutral
   refinement, and exchange of independent continuation fragments; and
4. occurrence of $f$ entails occurrence of $e$ up to the declared null-set
   convention.

Persistence or earlier appearance in one serialized execution is not
dependency. A record may already be present when an independent occurrence
is created. Accidental perfect correlation is also insufficient unless the
typed co-onset or producer condition is met.

Let $\precsim$ be the reflexive transitive closure of $\triangleleft$:

$$
e\precsim f
\quad\Longleftrightarrow\quad
e=f\ \text{or}\ e\mathrel{\triangleleft^+}f.
$$

This is generally a preorder, not a partial order on individual record
components.

### Symmetric co-creation countermodel

Let the complete record carrier consist of Boolean registers $(a,b)$ and let
the only nonidentity transition be

$$
(0,0)\longrightarrow(1,1),
$$

followed by persistent identity evolution. Suppose the law and all accessible
data are invariant under exchanging $a$ and $b$. The two stable component
facts $h_a,h_b$ are jointly created and mutually dependent:

$$
h_a\precsim h_b,
\qquad
h_b\precsim h_a.
$$

Orienting one before the other violates the exact swap symmetry. Declaring
them independent loses the supplied indivisibility of the onset. The correct
order atom is their mutual-dependence class.

Define

$$
e\simeq f
\quad\Longleftrightarrow\quad
e\precsim f\ \text{and}\ f\precsim e.
$$

An element $[e]_\simeq$ is an **indivisible stable-happening bundle**.

### Theorem 3 — dependency quotient poset

If $\precsim$ is a presentation-invariant preorder on stable record facts,
then $\simeq$ is an equivalence relation and

$$
[e]_\simeq\preceq_B[f]_\simeq
\quad\Longleftrightarrow\quad
e\precsim f
$$

is a partial order on happening bundles in every presentation. Every arrow of
$\mathcal G$ induces a bijective poset isomorphism between the corresponding
bundle posets. The presentation-independent physical history is the
isomorphism class of the complete bundle poset with its incidence
multiplicities, not the orbit set of its individual bundle nodes.

### Proof

Reflexivity, symmetry, and transitivity of $\simeq$ follow from the preorder
laws. If $e\simeq e'$ and $f\simeq f'$, transitivity shows that
$e\precsim f$ iff $e'\precsim f'$, so the quotient relation is well defined.
It is reflexive and transitive. If both bundle inequalities hold, their
representatives are mutually dependent and therefore belong to the same
bundle; hence antisymmetry holds.

Presentation covariance of $\precsim$ carries mutual-dependence classes to
mutual-dependence classes and preserves and reflects the quotient order. Since
the presentation action is invertible, the induced map is a bijective poset
isomorphism. An isomorphism preserves the number of nodes even when an
automorphism exchanges them. ∎

This is a dependency order on indivisible onset bundles. Calling it causal
order requires a later theorem relating it to operational influence and
excluding common-cause correlation. An order on the individual components
requires the additional separation theorem that distinct stable facts are
never mutually dependent; the countermodel shows that statement is false in
general.

### Theorem 4 — no hidden global clock

Suppose two incomparable happening bundles $e$ and $f$ form a commuting diamond:
both linearizations $ef$ and $fe$ have the same composite typed data, history
event, $\Gamma$ law, later record algebra, and dependency output. Then no
total ordering of $e$ and $f$ is invariantly derivable from $\mathfrak I$.

### Proof

The trace swap exchanging $ef$ and $fe$ is an automorphism of all supplied
physical data. A derived invariant must be fixed by this automorphism. Either
strict total-order assignment $e<f$ or $f<e$ is exchanged with the other and
is therefore not fixed. The only invariant relation is incomparability. ∎

An implementation loop index, sequence number, file order, or chosen linear
extension is thus extra structure, not emergent time.

## 8. Complete division frontiers

A candidate frontier is not a happening. It is a typed cut of complete
histories. For a finite or countable state set $S_F$, supply prefix sets
$L_F(s)$ and let

$$
C_F(s)=\bigcup_{\alpha\in L_F(s)}[\alpha].
$$

For every reachable state $s$, also supply a typed future-event algebra
$\mathcal A_s^+$ and gluing maps

$$
j_\alpha:\mathcal A_s^+\longrightarrow\mathcal A_x,
\qquad \alpha\in L_F(s),
$$

which identify a future event after $s$ with its source-history event after
the particular past prefix. A complete division frontier must pass all of the
following.

1. **Disjointness:** $C_F(s)\cap C_F(t)=\varnothing$ for $s\ne t$.
2. **Exhaustiveness:** the cells cover every admitted complete history,
   including a declared termination state if needed.
3. **Exactly-once crossing:** no history hits two frontier cells or the same
   frontier twice.
4. **Complete interface:** $s$ contains every declared law-relevant boundary,
   relational, matter, and carried-record degree of freedom.
5. **Record faithfulness and persistence:** no required stable fact is omitted
   or silently merged, and every claimed record survives the future grammar.
6. **Future sufficiency:** for all positive pasts
   $\alpha,\alpha'\in L_F(s)$ in the same state and every licensed future
   event $B\in\mathcal A_s^+$,

   $$
   \Gamma_x(j_\alpha(B)\mid[\alpha])
   =\Gamma_x(j_{\alpha'}(B)\mid[\alpha']).
   $$

7. **Positive normalization:** the resulting conditional law is a nonnegative
   normalized kernel on every admitted input.
8. **All-input cut equality:** direct and cut calculations agree for every
   source and future event, including zero-probability target coordinates.
9. **Grammar and presentation closure:** continuation, gluing, records, and
   all gates transport covariantly.
10. **No smuggling:** no hidden history identifier, phase cache, global clock,
    cached count, whole-history hash, or dormant fixed memory is added after
    seeing a failure.

Any native context is an explicit typed field declared before the test. There
is no optional post-hoc history payload.

### Theorem 5 — complete-frontier kernel

For reachable $s\in S_F$, future sufficiency defines

$$
K_F(B\mid s)=\Gamma_x(j_\alpha(B)\mid[\alpha]),
\qquad \alpha\in L_F(s),
$$

independently of the positive representative $\alpha$. The kernel is
nonnegative and normalized.

For nested complete frontiers $F_i,F_j$, define

$$
K_{ij}(t\mid s)=\Gamma(C_j(t)\mid C_i(s)).
$$

If $F_j$ is an exhaustive exactly-once refinement after $F_i$, then for a
later complete frontier $F_k$,

$$
K_{ik}(u\mid s)
=\sum_{t\in S_j}K_{jk}(u\mid t)K_{ij}(t\mid s).
$$

### Proof

Representative independence is precisely future sufficiency. Positivity and
normalization follow from the probability law. The cells $C_j(t)$ form a
disjoint exhaustive partition of histories after $C_i(s)$. The law of total
probability gives

$$
\Gamma(C_k(u)\mid C_i(s))
=\sum_t
\Gamma(C_k(u)\mid C_j(t),C_i(s))
\Gamma(C_j(t)\mid C_i(s)).
$$

Future sufficiency at $F_j$ removes the earlier conditioning from the first
factor and yields the displayed composition law. ∎

The theorem is required only at frontiers that pass the gates. At any other
cut the whole law remains primitive and no intermediate kernel is invented.

### Four exact independence controls

Let $U$ and $S$ be independent fair bits. A candidate frontier exposes
$s=S$, and a future bit $Z$ is produced. In the stable rows, a persistent
record of $S$ appears at the frontier. In the nonstable rows it does not.

| case | persistent record? | future rule | stable happening? | complete frontier? |
|---|---:|---|---:|---:|
| A | yes | $Z=S$ | yes | yes |
| B | yes | $Z=U$ | yes | no |
| C | no | $Z=S$ | no | yes |
| D | no | $Z=U$ | no | no |

In A and C, all pasts with the same $S$ give the same future law. In B and D,
the pasts $(U,S)=(0,s)$ and $(1,s)$ have the same exposed interface and
opposite deterministic futures. Record persistence changes only the stable-
happening coordinate. It does not determine future sufficiency.

## 9. Locally finite histories and genuine growth

The happening-bundle order is locally finite when

$$
[e,f]=\{h:e\preceq h\preceq f\}
$$

is finite for every comparable pair of bundles. This must be proved directly
for semantic mutual-dependence classes. It cannot be inferred from finite test
depth, stability, or the existence of complete frontiers.

### Theorem 6 — fixed-memory obstruction

If $n$ independently persistent binary happenings have occurred, their
records distinguish at least $2^n$ histories. No fixed carrier with $M$
states can represent all such histories once $2^n>M$.

### Proof

The $2^n$ distinct record strings must remain distinguishable under every
licensed future reader. A map into $M<2^n$ carrier states identifies two of
them by the pigeonhole principle, contradicting distinguishability. ∎

For example, eight states fail at $n=4$. Four dormant preallocated bits mimic
growth through depth four and fail at depth five. This is a capacity theorem,
not yet a construction of unbounded physical growth.

A direct local-finiteness theorem must rule out a Zeno interval

$$
a\prec e_1\prec e_2\prec\cdots\prec b.
$$

The fact that every finite prefix is finite does not make $[a,b]$ finite.

## 10. Event count and unequal weights

### 10.1 Unit counting measure

Let $(\mathsf B,\preceq_B)$ be any representative of a countable physical
bundle-poset isomorphism class. Define

$$
N(A)=|A|
$$

for finite $A\subseteq\mathsf B$. A presentation isomorphism carries $A$
bijectively to its image, so the count is presentation invariant. This does
not identify two distinct nodes merely because a symmetry exchanges them. If
the dependency order is locally finite, every interval has finite count. On
all subsets, the corresponding
atomic measure

$$
\mu_1(A)=\sum_{e\in A}1
$$

is countably additive, allowing $+\infty$ on unbounded sets.

This is an invariant bundle count after the quotient. Counting the distinct
record components inside a bundle instead defines a different measure and
must be declared explicitly. Neither count is automatically spacetime volume,
proper time, entropy, energy, or action.

### 10.2 Contextual $\Gamma$ weights

Raw probability is not an extensive event valuation. For independent bundle
events with probabilities $p,q$,

$$
\Gamma(e\otimes f)=pq,
$$

whereas extensivity asks for $V(e\otimes f)=V(e)+V(f)$. At
$p=q=1/2$, the joint probability is $1/4$, not the sum of two local values.
The logarithm converts products into sums, but that algebraic fact does not
make the resulting surprisal intrinsic to each bundle.

For a happening bundle $e$ after a certified complete predecessor frontier state
$(F,s)$, a contextual surprisal is

$$
w(F,s;e)=-\kappa\log \Gamma(E_e\mid F=s),
\qquad \kappa\ge0.
$$

It belongs to the typed triple $(F,s,e)$. It descends to an intrinsic atomic
weight $w(e)$ only if all admissible complete predecessor frontiers and all
neutral linearizations assign the same positive probability to the complete
bundle event $e$.

If this descent fails, the valid object is a contextual edge weight or the
whole-history functional

$$
S_\Gamma(H)=-\kappa\log\Gamma(E_H),
$$

not an intrinsic weight attached to the happening alone.

### Correlated-diamond obstruction

Let incomparable binary happenings $A,B$ have joint law

$$
\begin{array}{c|cccc}
(A,B)&(0,0)&(0,1)&(1,0)&(1,1)\\\hline
\Gamma&2/5&1/10&1/5&3/10.
\end{array}
$$

On the branch $(0,0)$, the linearization $AB$ gives

$$
\Pr(A=0)=\frac12,
\qquad
\Pr(B=0\mid A=0)=\frac45,
$$

whereas $BA$ gives

$$
\Pr(B=0)=\frac35,
\qquad
\Pr(A=0\mid B=0)=\frac23.
$$

The total surprisal agrees:

$$
\log2+\log\frac54
=\log\frac53+\log\frac32
=-\log\frac25.
$$

But the allocations to $A$ and $B$ differ. The chain rule protects the
history total, not intrinsic weights on incomparable atoms.

### Theorem 7 — atomic extensive valuation

Suppose an intrinsic nonnegative finite weight $w(e)$ has descended to every
happening-bundle class and is invariant under presentation, neutral
refinement, and incomparable trace swaps. Then

$$
\mu_w(A)=\sum_{e\in A}w(e)
$$

is a countably additive atomic measure. On a locally finite order, every
interval has finite measure.

### Proof

For pairwise disjoint subsets, each atom occurs in exactly one summand, so
rearrangement of the nonnegative series gives countable additivity. A finite
interval contains finitely many atoms of finite weight. ∎

Different happening bundles may have different weights. Those weights may
encode real nonuniform structure only if their provenance and descent are proved.
Inserting unequal values by hand merely adds a measure beside $\Gamma$.

### Theorem 8 — strong-diamond descent

Let $(V,\preceq)$ be a finite happening-bundle poset with finite nonempty
outcome fibers $X_v$, and let $\Gamma$ be a strictly positive normalized law
on $\prod_{v\in V}X_v$. For an order ideal $I$, an enabled bundle
$v\notin I$, and a partial assignment $x_I$, define

$$
q_I(v,a;x_I)
=
\frac{
\Gamma_{I\cup\{v\}}(x_I,a)
}{
\Gamma_I(x_I)
}.
$$

For incomparable $v,w$ enabled over the same ideal, the weak diamond

$$
q_I(v,a)q_{I\cup\{v\}}(w,b)
=
q_I(w,b)q_{I\cup\{w\}}(v,a)
$$

is automatic: both sides are the same joint conditional. It protects the
two-step product but not the individual factors. Intrinsic occurrence weights
descend exactly when every such square also satisfies the two strong
equalities

$$
q_I(v,a)=q_{I\cup\{w\}}(v,a),
\qquad
q_I(w,b)=q_{I\cup\{v\}}(w,b).
$$

Equivalently, each local conditional depends only on the outcome at $v$ and
the complete assignment on its strict predecessor set, and

$$
\Gamma(x)
=
\prod_{v\in V}
q_v\!\left(x_v\mid x_{\downarrow v}\right).
$$

When these equivalent conditions and presentation covariance hold,

$$
w_\Gamma(v,x_v,x_{\downarrow v})
=
-\kappa\log q_v(x_v\mid x_{\downarrow v})
$$

is an intrinsic nonnegative occurrence weight. It is independent of every
linear extension and sums to $-\kappa\log\Gamma(x)$.

### Proof

Adjacent linear extensions of a finite poset differ by swaps of incomparable
enabled elements, and every two linear extensions are connected by such
swaps. The strong equalities therefore preserve each individual factor along
every path through the ideal lattice. Conversely, path-independent factors
give the strong equalities on each elementary square. This is exactly the
conditional-independence statement that previously exposed incomparable data
do not move the local conditional once all strict predecessors are supplied.
Multiplication along a linear extension gives the factorization. Reverse
topological marginalization recovers the same local conditionals from a
factorized positive law. Taking $-\kappa\log$ turns the product into the stated
sum. ∎

The correlated diamond above passes only the weak equality and therefore
remains a whole-history valuation. Strong-diamond descent is the additional
test that prevents a serialization-dependent allocation from being called a
physical event weight.

### Nontrivial positive control — screened common-cause fork

Strong descent does not require marginally independent incomparable events.
Let

$$
\bar R\prec\bar A,
\qquad
\bar R\prec\bar B,
\qquad
\bar A\parallel\bar B,
$$

with binary outcomes and

$$
\Pr(R=0)=\frac23,
\qquad
\Pr(R=1)=\frac13.
$$

Choose

$$
\begin{array}{c|cc}
&A=0&A=1\\\hline
R=0&3/4&1/4\\
R=1&1/4&3/4
\end{array},
\qquad
\begin{array}{c|cc}
&B=0&B=1\\\hline
R=0&4/5&1/5\\
R=1&3/5&2/5
\end{array},
$$

and set

$$
\Gamma(r,a,b)
=
\Pr(r)\Pr(a\mid r)\Pr(b\mid r).
$$

$A$ and $B$ are marginally correlated:

$$
\Pr(A=1,B=1)
-\Pr(A=1)\Pr(B=1)
=\frac1{45}>0.
$$

Nevertheless, the typed predecessor $R$ screens the correlation, so every
strong diamond passes. The exact unequal weights include

$$
w(R=1)=\kappa\log3,
\quad
w(A=1\mid R=1)=\kappa\log\frac43,
\quad
w(B=0\mid R=1)=\kappa\log\frac53.
$$

On the history $(R,A,B)=(1,1,0)$ their sum is
$\kappa\log(20/3)=-\kappa\log(3/20)$ in either $RAB$ or $RBA$
linearization. Thus a derived typed common cause can support intrinsic unequal
weights without orienting the incomparable children.

## 11. Exact finite point-free constructions

The following models instantiate the abstract mathematics without importing a
background graph, clock, coordinate, or metric. They are exact finite
witnesses, not an evaluation of an accepted Paper 13 object and not evidence
of unbounded growth or a continuum limit.

### 11.1 Minimal co-creation, diamond, and downstream-dependency frame

Let the primitive persistent facts be

$$
\{a,b,c,d\}
$$

and let the admissible record states be

$$
S_0=\varnothing,
\quad
S_U=\{a,b\},
\quad
S_C=\{c\},
\quad
S_{UC}=\{a,b,c\},
\quad
S_{UCD}=\{a,b,c,d\}.
$$

The three physical onsets are

$$
\begin{aligned}
U&:S_0\mapsto S_U,\qquad S_C\mapsto S_{UC},\\
C&:S_0\mapsto S_C,\qquad S_U\mapsto S_{UC},\\
D&:S_{UC}\mapsto S_{UCD}.
\end{aligned}
$$

$U$ co-creates the two exchange-symmetric persistent facts $a,b$. The first
diamond commutes exactly:

$$
C(U(S_0))=U(C(S_0))=S_{UC}.
$$

The legal words are

$$
\epsilon, U, C, UC, CU, UCD, CUD,
$$

and the trace quotient $UC\sim CU$ gives five physical history shapes

$$
[\epsilon], [U], [C], [UC], [UCD].
$$

The dependency preorder puts $a\simeq b$ by symmetric co-onset, while $c$ is
independent of them and $d$ essentially consumes both upstream records. The
bundle poset is therefore

$$
\bar U=\{a,b\},
\qquad
\bar C=\{c\},
\qquad
\bar D=\{d\},
$$

with

$$
\bar U\prec\bar D,
\qquad
\bar C\prec\bar D,
\qquad
\bar U\parallel\bar C.
$$

All intervals contain at most two bundles. Relabeling $a\leftrightarrow b$
is an automorphism of the complete history, but it does not turn the two raw
record facts into one raw fact; it preserves their multiplicity and places
them in one indivisible onset bundle.

Within persistent-set frames required to contain all three features, this
census is cardinality minimal: co-creation needs two facts, the independent
diamond needs a third onset and fact, a distinct downstream dependence needs
a third onset and fourth fact, the diamond needs four states, and its strict
downstream successor needs a fifth.

### 11.2 One-law reciprocal-response extension

To add an exact matter–relation–matter response while retaining the diamond,
use stable record components

$$
r_A, r_B, n, m, r_Y
$$

and four happening bundles

$$
\bar A=\{r_A\},
\quad
\bar B=\{r_B\},
\quad
\bar G=\{n,m\},
\quad
\bar Y=\{r_Y\}.
$$

$A$ and $B$ independently write binary matter records $a,b$. After both are
present, $G$ co-creates two exchange-symmetric relational record components
with a common binary value $g$. Finally $Y$ writes a later binary matter
response $y$. The six record-shape states are

$$
\varnothing,
\{r_A\},
\{r_B\},
\{r_A,r_B\},
\{r_A,r_B,n,m\},
\{r_A,r_B,n,m,r_Y\}.
$$

The $A$ and $B$ onsets commute. $G$ is enabled only after both, and $Y$ only
after $G$. Hence the bundle order is

$$
\bar A\parallel\bar B,
\qquad
\bar A,\bar B\prec\bar G\prec\bar Y.
$$

Every interval contains at most three bundles. The presentation groupoid may
rename every record, exchange $A$ with $B$, and exchange $n$ with $m$. It acts
on the complete incidence-and-value structure. In particular, the $A/B$
automorphism leaves two incomparable bundle nodes in the unlabeled poset.

Let

$$
B_{z\mid x}
=
\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix}_{z,x},
$$

put $p=a\oplus b$, and define the one complete positive history law

$$
\Gamma(a,b,g,y)
=
\frac14 B_{g\mid p}B_{y\mid g},
\qquad
a,b,g,y\in\{0,1\}.
$$

Normalization is exact because the two root records are independent fair
bits and both columns of $B$ sum to one. All sixteen histories are positive.
The law is invariant under exchanging $A$ and $B$, since $a\oplus b$ is, and
under either serialization of their commuting onsets.

The factorization satisfies Theorem 8. With $\kappa>0$, its intrinsic
$\Gamma$-derived occurrence weights are

$$
\begin{aligned}
w_A(a)&=w_B(b)=\kappa\log2,\\
w_G(g\mid a,b)&=-\kappa\log B_{g\mid a\oplus b},\\
w_Y(y\mid g)&=-\kappa\log B_{y\mid g}.
\end{aligned}
$$

Thus $w_G$ and $w_Y$ take the unequal values

$$
\kappa\log\frac{25}{9}
\quad\text{or}\quad
\kappa\log\frac{25}{16}.
$$

Every complete history has unit bundle count four, while

$$
\Gamma(a,b,g,y)
\in
\left\{
\frac{81}{2500},
\frac{144}{2500},
\frac{256}{2500}
\right\}.
$$

Therefore unit count and intrinsic $\Gamma$ valuation are demonstrably
different coordinates. The occurrence identity used by the unequal weight
contains its derived predecessor values; merging, for example, all printed
$G=1$ rows while discarding their physical parity provenance would destroy
descent rather than simplify it.

### 11.3 Exact pre-geometric reciprocal response

Holding the law fixed, the matter parity changes the relational-bundle law:

$$
\Pr(g=1\mid p=0)=\frac{16}{25},
\qquad
\Pr(g=1\mid p=1)=\frac9{25}.
$$

The relational outcome in turn changes the later matter response:

$$
\Pr(y=1\mid g=0)=\frac{16}{25},
\qquad
\Pr(y=1\mid g=1)=\frac9{25}.
$$

After eliminating the recorded intermediate value,

$$
\Pr(y=1\mid p=0)=\frac{288}{625},
\qquad
\Pr(y=1\mid p=1)=\frac{337}{625}.
$$

The two exact source-sensitivity residuals are $7/25$ at each local leg, and
the integrated matter-to-matter residual through the relational record is
$49/625$. This is a closed reciprocal matter–relation–matter response under
one law. It is not geometry: $g$ is a stable relational fact, not a metric,
connection, or curvature variable.

The full $(a,b)$ frontier is a complete division for the declared $G,Y$
future grammar, and the full $(a,b,g)$ frontier is a complete division for the
$Y$ continuation. By contrast, the projected frontier exposing only the
stable $A=a$ record is not complete. At fixed $a$, the two positive hidden
values of $b$ give the different $g=1$ probabilities $9/25$ and $16/25$, so
future sufficiency fails. Stable record and complete frontier are separated
inside the same exact law.

The recorded $g$ alternatives factorize lawfully at the certified frontier.
The unrecorded coherent cut in Section 2 still has the negative restart
candidate and remains nondivisible. The construction therefore adds local
durable facts without converting every intermediate cut into a Markov step.

### 11.4 Uniform fresh-port graft family

The finite cell extends by one recursive rule. Fix a finite branching bound
$q\ge1$. A source boundary carries finitely many open typed successor ports,
each owned by either the declared seed or a previously written $Y$ bundle. A
graft consumes one open port exactly once and creates fresh bundles

$$
A_\pi, B_\pi, G_\pi, Y_\pi
$$

with local order

$$
\operatorname{owner}(\pi)
\prec A_\pi,B_\pi
\prec G_\pi
\prec Y_\pi,
\qquad
A_\pi\parallel B_\pi.
$$

$G_\pi$ again contains two individually readable but exchange-symmetric raw
record sectors. $Y_\pi$ exposes $q$ fresh successor ports. No old record or
port is reused, and every later operation preserves every earlier record.

A finite graft shape is a finite prefix-closed rooted set $T$ of port
addresses. Addresses and sibling order are presentation data. The groupoid
contains all typed renamings and sibling permutations and acts on the whole
decorated graft tree. The physical shape is the unlabeled rooted incidence
structure, which retains every sibling's multiplicity.

Let $s_\pi$ be the seed bit carried by the owner of port $\pi$. On every cell
use the same local law

$$
\gamma_{s_\pi}(a_\pi,b_\pi,g_\pi,y_\pi)
=
B_{a_\pi\mid s_\pi}
B_{b_\pi\mid s_\pi}
B_{g_\pi\mid a_\pi\oplus b_\pi}
B_{y_\pi\mid g_\pi}.
$$

For a declared finite shape $T$, define

$$
\Gamma_T(\omega\mid s_0)
=
\prod_{\pi\in T}
\gamma_{s_\pi}
(a_\pi,b_\pi,g_\pi,y_\pi),
$$

where a child port's seed is its parent's $y$ value. Every factor is positive
and normalized, so reverse leaf elimination proves that $\Gamma_T$ is
normalized for every finite $T$. Conditional on their complete ancestors,
different open-port cells and each local $A_\pi/B_\pi$ pair are independent.
Every strong diamond therefore passes, and the local weights

$$
-\kappa\log B_{a_\pi\mid s_\pi},
\quad
-\kappa\log B_{b_\pi\mid s_\pi},
\quad
-\kappa\log B_{g_\pi\mid a_\pi\oplus b_\pi},
\quad
-\kappa\log B_{y_\pi\mid g_\pi}
$$

descend to complete typed occurrence provenance. Grafts on distinct open ports
commute, so their construction order is not a physical clock.

### Theorem 9 — uniform local finiteness and genuine carrier growth

Every finite graft shape with $n$ cells has $4n$ happening bundles, $5n$ raw
stable record components, and $16^n$ positive outcome histories. The direct
limit over any prefix-closed locally finite graft tree is locally finite as a
bundle order.

### Proof

Each cell adds four bundles and five raw record components, and its four
binary values give sixteen positive assignments. Fresh-sector persistence
keeps distinct cell assignments distinguishable, so the counts multiply.

For local finiteness, assign the seed rank zero and derive every later rank
from dependency depth; the rule does not read this rank. Every dependency edge
strictly increases rank, and every node has finite out-degree bounded in terms
of $q$. For comparable fixed bundles $x\prec y$, every element of $[x,y]$ is
reachable from $x$ by at most
$\operatorname{rank}(y)-\operatorname{rank}(x)$ edges. Finite branching gives
only finitely many such nodes. Hence every closed interval is finite. ∎

This is genuine varying-carrier growth. The $16^n$ stable histories cannot be
stored faithfully in one fixed finite carrier for unbounded $n$. The derived
rank is a proof coordinate on the order, not a total execution index; sibling
cells remain incomparable and may be grafted in either serialization.

A complete finite frontier consists of the full current typed graft shape,
all carried records, and the owner seed on every open port. The future product
law depends only on that data. A single local happening or a projection that
omits one open-port seed is not thereby a division. Which open ports are
actually grafted remains part of the declared event grammar/actualization; the
law above is uniform over every admitted finite shape but does not select a
shape.

The branching bound $q$ is a declared local capacity parameter. It is not a
spatial dimension, coordination number of an already existing lattice, or
metric datum. Paper 15 must infer or reject geometric interpretations from
the resulting unlabeled orders rather than reading $q$ as dimension.

### 11.5 What the construction earns

The finite witness and uniform graft family supply:

1. a whole-structure presentation quotient that preserves anonymous
   multiplicity;
2. an indivisible co-onset bundle rather than a false orientation of its
   components;
3. a genuine commuting diamond with no hidden global clock;
4. a uniform unbounded varying-size family with a direct local-finiteness
   theorem;
5. a unit measure and a distinct intrinsic unequal $\Gamma$ measure passing
   strong-diamond descent;
6. stable and incomplete frontiers in one law; and
7. exact pre-geometric reciprocal response; and
8. fresh-sector growth that cannot be simulated by one fixed finite memory.

It does not supply shape selection, actualization, chronological order,
dimension, volume calibration, duration, topology, signature, continuum
convergence, curvature, stress-energy, or gravitational dynamics.

## 12. What Paper 14 can honestly earn

Paper 14 reports independent coordinates rather than forcing them into one
misleading ladder.

### Record coordinate

```text
P14-RECORD-ONSET-GERMS
P14-POSSIBLE-RECORD-FACT-QUOTIENT
P14-STABLE-RECORD-FACT-TYPES
P14-INDIVISIBLE-STABLE-HAPPENING-BUNDLES
P14-ACTUAL-STABLE-HAPPENINGS-CONDITIONAL-ON-ACTUALIZATION
```

### Dependency coordinate

```text
P14-DEPENDENCY-UNCONSTRUCTED
P14-PRESENTATION-COVARIANT-DEPENDENCY-PREORDER
P14-INDIVISIBLE-HAPPENING-BUNDLE-POSET
P14-FINITE-BUNDLE-POSET-WITNESS
P14-LOCALLY-FINITE-BUNDLE-POSET
```

### Frontier coordinate, reported for each candidate $F$

```text
P14-FRONTIER-INCOMPLETE
P14-COMPLETE-INTERFACE
P14-COMPLETE-DIVISION-FRONTIER
```

### Valuation coordinate

```text
P14-NO-EVENT-MEASURE
P14-UNIT-COUNTING-MEASURE
P14-CONTEXTUAL-GAMMA-HISTORY-WEIGHT
P14-FINITE-INTRINSIC-GAMMA-WEIGHT-WITNESS
P14-INTRINSIC-GAMMA-ATOMIC-WEIGHT
P14-INTERVAL-FINITE-ATOMIC-MEASURE
```

### Geometric coordinate

```text
P14-NO-METRIC
P14-FINITE-PREMETRIC-WITNESS
P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE
```

The strongest Paper 14 ceiling is

```text
P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE
```

with frontier statuses and $\Gamma$-weight status printed alongside it. A
single finite construction reaches only the finite-witness rung. The uniform
fresh-port family in Section 11 reaches the displayed ceiling at the level of
the declared abstract model: it has unbounded size, direct local finiteness,
and interval-finite unit and intrinsic $\Gamma$ measures. An authoritative
physical result still requires a lawful-input binding and independent
scientific adjudication. Neither rung requires every stable happening to be a
division or every division to contain a new stable happening.

## 13. Hostile controls

The following controls are scientific, not software-style checks. Each
changes the mathematical object whose invariance or sufficiency is claimed.

| ID | countermodel | required conclusion |
|---|---|---|
| H1 | clone one record label without changing its event, support, or provenance | one occurrence class and unchanged measure |
| H2 | split one onset into two neutral arrows with no intermediate record growth | one occurrence, not two |
| H3 | serialize an independent diamond in the two opposite orders | same order, histories, and measure; no global clock |
| H4 | admit an eraser after the trace $0\to1\to0$ | possible onset but not a stable type |
| H5 | expose stable $X_1$ while hidden $X_0$ controls the future | stable record passes; complete frontier fails |
| H6 | corrupt a cached count while leaving the bundle set fixed | recomputed count is unchanged |
| H7 | claim unbounded growth with eight fixed states or four dormant bits | collision at the proved capacity bound |
| H8 | change one unequal weight while holding $\Gamma$ fixed | intrinsic-$\Gamma$ weight claim fails |
| H9 | keep one order but change its positive history law | order unchanged; valuation may change |
| H10 | compare a two-event chain with a two-event antichain | equal count, different order |
| H11 | let a history hit two cells of one candidate frontier | frontier fails exactly-once and cut normalization |
| H12 | omit positive histories from a candidate frontier | frontier fails exhaustiveness |
| H13 | use the correlated diamond above | history surprisal survives; intrinsic atom weights fail |
| H14 | place infinitely many occurrences between fixed $a,b$ | local-finiteness claim fails |
| H15 | use stable record events on different boundaries without common transport | multi-record product is undefined |
| H16 | declare $e$ a predecessor of $f$ while $E_f\not\subseteq E_e$ | dependency entailment fails |
| H17 | append a whole-history hash to a frontier after a failure | enlarged-history control only, not native completeness |
| H18 | attach coordinates or distances to break an incomparability | imported geometry is quarantined |
| H19 | symmetrically co-create two persistent facts by $(0,0)\to(1,1)$ | two record components, one mutual-dependence bundle; no arbitrary orientation |
| H20 | exchange two anonymous incomparable nodes by an automorphism and then count node orbits | whole-poset isomorphism preserves two nodes; orbit counting is rejected |
| H21 | use a correlated antichain whose weak diamond passes but strong factors move | whole-history surprisal only; intrinsic atom weights fail |
| H22 | condition a correlated fork on its typed common cause | strong diamonds and unequal intrinsic weights pass without orienting the children |

The positive controls are equally important: an enlarged history carrier may
be Markov even when the native cut is not; a complete frontier may exist with
no new stable record; unit counting may remain valid when intrinsic unequal
$\Gamma$ weights fail.

## 14. Why this is not yet spacetime

A locally finite partially ordered set with a count or weight is not, by
itself, a Lorentzian manifold. The causal-order reconstruction literature
starts from substantial comparison hypotheses. Hawking, King, and McCarthy
and Malament recover topological/conformal information within smooth causal
spacetimes under causality conditions. Causal-set order-and-number proposals
add local finiteness and a continuum approximation. Modern probabilistic
reconstruction results compare all finite random chronological order laws
under smoothness, causal regularity, finite-volume, and sampling hypotheses.

The literature supplies constraints, not a shortcut:

- Barandes's division events are allowed conditioning locations for an
  indivisible stochastic law, often approximate and environment relative.
  They are not defined as spacetime atoms, and “happening” is not a technical
  object of that framework.
- Bombelli, Lee, Meyer, and Sorkin propose local finiteness plus causal order
  as discrete spacetime kinematics; the proposal does not make an arbitrary
  finite poset manifoldlike.
- the Hawking–King–McCarthy and Malament theorems begin with smooth causal
  spacetimes and appropriate distinguishing/causality hypotheses. They do not
  construct a smooth spacetime from the bundle order obtained here.
- longest-chain proper-time results require a faithful random sprinkling,
  asymptotic control, and dimension-dependent calibration. Without those
  inputs, longest chain is only order depth.
- Braun's order-and-number theorem compares all finite labeled chronological
  order laws under smooth causal-continuum, finite-mass, and i.i.d. sampling
  hypotheses. Its weighted result is a measure/conformal reconstruction in
  that setting, not a theorem for arbitrary unequal discrete event weights.
- distinct Hauptvermutung formulations have different positive and negative
  results. A single finite weighted order is therefore not a uniqueness
  certificate.

Paper 14 has not supplied those hypotheses. In particular:

- $\prec$ is currently a record-dependency order, not yet proven to equal a
  spacetime chronological relation;
- $\mu$ is an event measure, not yet calibrated to a Lorentzian volume form;
- longest-chain length is order depth, not yet proper time;
- no dimension, topology, signature, light cone, scale, or continuum limit has
  been constructed;
- no stress tensor, energy current, spatial region, horizon, entropy law, or
  gravitational equation exists.

The honest bridge to Paper 15 is conditional:

$$
[(\mathsf B,\prec,\mu)]_{\mathcal G}
+\text{manifoldlike correspondence and calibration}
\longrightarrow
\text{candidate Lorentzian metric data}.
$$

## 15. Paper 15 entrance gates

Paper 15 may attempt spacetime reconstruction only after Paper 14 supplies a
presentation-independent locally finite bundle order and interval-finite
measure. It must then independently earn:

1. an operational theorem relating dependency to chronological influence;
2. dimension, rather than an assumed embedding dimension;
3. Lorentzian signature and a light-cone structure;
4. a faithful manifoldlike or other continuum correspondence;
5. calibration of $\mu$ to a volume element and control of unequal weights;
6. local-duration estimators with no preferred global slicing;
7. agreement of order, duration, and volume reconstructions;
8. topology and a uniqueness/gauge statement;
9. stable scaling and continuum convergence.

The first honest Paper 15 test is ensemble-conditional. Before reading any
finite order as geometry, it must declare a target spacetime class, candidate
dimension and region, sampling law and density, boundary convention, weight
type, and scale window. It should then compare several independent intrinsic
interval statistics rather than tune one estimator: relation fraction and
higher-chain counts, midpoint scaling, interval-abundance profiles, and
longest-chain height versus interval mass. Agreement must persist across
sample sizes, subregions, covariant selections, and controlled thinning.

Even a successful finite fit licenses only compatibility with that declared
manifoldlike ensemble. A Dushnik–Miller order dimension greater than two can
rule out an exact conformally flat $1+1$ order embedding, but order dimension
at most two does not prove a faithful sprinkling. At any fixed finite sample
size, inequivalent continuum geometries can also have observationally
indistinguishable finite order laws. Conformal rescaling accompanied by a
compensating sampling-density change leaves a further scale degeneracy.
Unequal $\Gamma$ surprisal weights may enter a volume estimator only after a
separate quadrature or intensity theorem; positivity and additivity alone do
not make them volume.

Curvature, connection, Einstein dynamics, energy flux, thermodynamic entropy,
and QFT remain later questions. A finite causal graph with a counter does not
pass these gates.

## 16. Current result and next construction

This draft establishes the abstract finite-word persistence theorem, the
typed compatible-meet theorem, the mutual-dependency quotient from a preorder
to a bundle poset, the no-hidden-clock theorem for commuting diamonds, the
complete-frontier kernel theorem, the fixed-memory obstruction, the
strong-diamond descent criterion, and the atomic-measure theorem. It gives
exact countermodels proving that stable happenings, complete divisions,
order, and unequal weights are independent coordinates.

Section 11 supplies a minimal finite construction, its reciprocal stochastic
extension, and one uniform fresh-port graft family. The finite cell realizes a
four-node bundle poset, complete and incomplete frontiers, unequal intrinsic
$\Gamma$ weights, and a closed matter–relation–matter response with residuals
$7/25$, $7/25$, and $49/625$. The uniform rule adds four fresh bundles per
cell, preserves all old records, is invariant under disjoint graft order, and
proves local finiteness for every prefix-closed finitely branching direct
limit. Its strong-diamond factorization provides interval-finite unit and
intrinsic $\Gamma$ measures.

The declared abstract family therefore reaches
`P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE` as a mathematical construction. It
does not constitute an authoritative physical Paper 14 result because it is
not bound to a terminal accepted point-free base-law object, its graft-shape
selection remains declared, and actualization remains postulated.

The remaining Paper 14 scientific obligations are therefore:

1. decide and expose whether the uniform graft grammar is a new law postulate
   or descends from an accepted point-free input;
2. bind onset germs, record transport, and complete-frontier state to that
   input without label or address dependence;
3. classify every declared cut family rather than only the positive controls;
4. test the full hostile table under whole-structure presentation transport;
5. independently reconstruct the strong-diamond and local-finiteness proofs;
6. report the independent coordinates in Section 12; and
7. keep shape selection, actualization, and geometry explicitly external.

Paper 15 preparation may study the conditional ensemble tests in Section 15,
but no finite fit may be promoted to a unique metric, curvature, or gravity
claim.

## References

1. J. A. Barandes, [“The Stochastic-Quantum Correspondence,” *Philosophy of
   Physics* 3(1):8 (2025)](https://doi.org/10.31389/pop.186).
2. J. A. Barandes, [“Quantum Systems as Indivisible Stochastic Processes”
   (2025)](https://arxiv.org/abs/2507.21192).
3. L. Bombelli, J. Lee, D. Meyer, and R. D. Sorkin, [“Space-time as a causal
   set,” *Physical Review Letters* 59, 521
   (1987)](https://doi.org/10.1103/PhysRevLett.59.521).
4. S. W. Hawking, A. R. King, and P. J. McCarthy, [“A new topology for curved
   space-time which incorporates the causal, differential, and conformal
   structures,” *Journal of Mathematical Physics* 17, 174
   (1976)](https://doi.org/10.1063/1.522874).
5. D. B. Malament, [“The class of continuous timelike curves determines the
   topology of spacetime,” *Journal of Mathematical Physics* 18, 1399
   (1977)](https://doi.org/10.1063/1.523436).
6. G. Brightwell and R. Gregory, [“Structure of random discrete spacetime,”
   *Physical Review Letters* 66, 260
   (1991)](https://doi.org/10.1103/PhysRevLett.66.260).
7. D. P. Rideout and R. D. Sorkin, [“A classical sequential growth dynamics
   for causal sets” (2000)](https://arxiv.org/abs/gr-qc/9904062).
8. M. Braun, [“Spacetime reconstruction by order and number”
   (2025)](https://arxiv.org/abs/2507.01907).
9. O. Müller, [“On the Hauptvermutung of causal set theory”
   (2025)](https://arxiv.org/abs/2503.01719).
10. H. Ollivier, D. Poulin, and W. H. Zurek, [“Environment as a witness:
    Selective proliferation of information and emergence of objectivity in a
    quantum universe,” *Physical Review A* 72, 042113
    (2005)](https://doi.org/10.1103/PhysRevA.72.042113).
11. D. D. Reid, [“Manifold dimension of a causal set: tests in conformally
    flat spacetimes” (2002)](https://arxiv.org/abs/gr-qc/0207103).
12. L. Glaser and S. Surya, [“Towards a definition of locality in a
    manifoldlike causal set” (2013)](https://arxiv.org/abs/1309.3403).
13. B. Dushnik and E. W. Miller, [“Partially ordered sets,” *American Journal
    of Mathematics* 63, 600–610
    (1941)](https://doi.org/10.2307/2371374).
