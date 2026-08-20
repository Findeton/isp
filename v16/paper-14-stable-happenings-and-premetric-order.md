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
(\mathsf E/\!\simeq,\prec,\mu;\{\operatorname{DivStatus}(F)\}_F).
$$

Here $\mathsf E$ is a set of presentation-independent stable occurrence
classes, $\simeq$ identifies mutually dependent components of one indivisible
onset, $\prec$ is the induced dependency order on those bundles, $\mu$ is an
interval-finite atomic measure when one has been earned, and each proposed
frontier has its own division status. Nothing in this tuple is yet a spacetime
metric.

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

### 5.2 Presentation and refinement quotient

Two onset germs are physically equivalent when they are related by the
equivalence relation generated by:

1. the complete $\mathcal G$ action;
2. insertion or deletion of a neutral identity/refinement that exposes no new
   semantic record and changes no continuation law;
3. replacement of a printed label by another label with the same transported
   event, support, and provenance.

The quotient must remove label clones and bookkeeping splits while retaining
equal payloads produced at different supports or by different essential
provenance. It acts on the complete onset family, so a symmetry exchanging two
co-created components does not arbitrarily order them.

### 5.3 Possible, actual, and stable

An occurrence component class $e=[o,i]$ is possible from $x$ if its cylinder
event $E_e$ is measurable, has $\Gamma_x(E_e)>0$, and this value is
representative independent. The whole onset family is possible when its joint
event is measurable and positive.

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

is a partial order on happening bundles.

### Proof

Reflexivity, symmetry, and transitivity of $\simeq$ follow from the preorder
laws. If $e\simeq e'$ and $f\simeq f'$, transitivity shows that
$e\precsim f$ iff $e'\precsim f'$, so the quotient relation is well defined.
It is reflexive and transitive. If both bundle inequalities hold, their
representatives are mutually dependent and therefore belong to the same
bundle; hence antisymmetry holds. ∎

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

Once $\mathsf E/\!\simeq$ is a countable presentation-independent happening-
bundle set, define

$$
N(A)=|A|
$$

for finite $A\subseteq\mathsf E/\!\simeq$. If the dependency order is locally
finite, every interval has finite count. On all subsets, the corresponding
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

## 11. What Paper 14 can honestly earn

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
P14-INTRINSIC-GAMMA-ATOMIC-WEIGHT
P14-INTERVAL-FINITE-ATOMIC-MEASURE
```

### Geometric coordinate

```text
P14-NO-METRIC
P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE
```

The strongest Paper 14 ceiling is

```text
P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE
```

with frontier statuses and $\Gamma$-weight status printed alongside it. This
does not require every stable happening to be a division or every division to
contain a new stable happening.

## 12. Hostile controls

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

The positive controls are equally important: an enlarged history carrier may
be Markov even when the native cut is not; a complete frontier may exist with
no new stable record; unit counting may remain valid when intrinsic unequal
$\Gamma$ weights fail.

## 13. Why this is not yet spacetime

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
(\mathsf E/\!\simeq,\prec,\mu)
+\text{manifoldlike correspondence and calibration}
\longrightarrow
\text{candidate Lorentzian metric data}.
$$

## 14. Paper 15 entrance gates

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

Curvature, connection, Einstein dynamics, energy flux, thermodynamic entropy,
and QFT remain later questions. A finite causal graph with a counter does not
pass these gates.

## 15. Current result and next construction

This draft establishes the abstract finite-word persistence theorem, the
typed compatible-meet theorem, the mutual-dependency quotient from a preorder
to a bundle poset, the no-hidden-clock theorem for commuting diamonds, the
complete-frontier kernel theorem, the fixed-memory obstruction, and the
atomic-measure theorem. It also gives exact countermodels proving that stable
happenings, complete divisions, order, and unequal weights are independent
coordinates.

It does not yet instantiate those theorems on an accepted point-free
$\Gamma$. The next scientific construction is therefore not another verifier
repair. It is a finite, presentation-covariant happening model that must:

1. derive onset germs from record transport;
2. derive the dependency preorder from co-onset and typed provenance;
3. quotient symmetric mutual dependence into indivisible happening bundles;
4. realize an independent commuting diamond;
5. classify all four stable/division combinations;
6. prove direct interval finiteness in a varying-size family;
7. compare unit count, contextual history surprisal, and any candidate
   intrinsic unequal weight;
8. return the coordinate record in Section 11 without importing geometry.

That is the scientific Paper 14 target.

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
