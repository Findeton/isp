# One executable point-free Gamma

## Abstract

A static probability law does not determine interventions. We therefore
construct one exact executable law

$$
\mathbf\Gamma:
\mathsf{Exp}\longrightarrow
\operatorname{Prob}(\mathsf{CompleteHist}),
$$

whose identity experiment is the observational whole-history law. The domain
is a typed category of finite experiment programs. Every admitted mechanism
replacement, context, target boundary, and reader is explicit; unlisted or
ill-typed operations are refused. One deterministic global evaluator and one
fixed finite seed law produce every experiment measure. Chain-rule
refactorization is never consulted.

The law has an unqueried $B_0\to B_2$ transition with endpoint kernel $C$ and
native $B_1$ query morphisms with first-leg kernel $B$. No positive stochastic
second leg completes the unqueried law through that declared interface,
although recording and nonrecording queries create positive $B$ continuations
and endpoint law $B^2$. The distinction is cut-relative and operational.

The construction also gives exact point-free marked interventions,
presentation-covariant varying-size atom-and-bond histories, grammar-stable
records, complete divisions, and reciprocal matter--relation response. It
does not derive chronology, actuality, dimension, topology, volume, duration,
metric, curvature, gravity, continuum physics, or QFT.

## 1. Primitive status

The full map $\mathbf\Gamma$, not only its identity value, is the proposed
primitive law. It is a fixed candidate, not uniquely derived. Its constants,
experiment generators, type system, evaluator, and seed distribution are
declared before any output or geometric test.

Two executable maps are different laws if any admitted experiment has a
different output measure, even when their identity experiments have the same
static distribution.

Operational mechanism order is part of the experiment interface. It is not a
spacetime order. Whether response among physical regions later closes to a
chronology remains an unproved question.

## 2. Fixed exact seed

Fix the declared primitive rational rotation

$$
R=
\begin{pmatrix}
3/5&-4/5\\
4/5&3/5
\end{pmatrix}.
$$

Define

$$
B=|R|^2=
\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix},
$$

$$
C=|R^2|^2=
\frac1{625}
\begin{pmatrix}
49&576\\
576&49
\end{pmatrix},
$$

and

$$
B^2=
\frac1{625}
\begin{pmatrix}
337&288\\
288&337
\end{pmatrix}.
$$

Let $[25]=\{0,1,\ldots,24\}$. Define deterministic transition maps

$$
\beta(a,u)=
\begin{cases}
a,&u<9,\\
1-a,&u\ge9,
\end{cases}
$$

and, with $s=25u_1+u_2$,

$$
\kappa(a,u_1,u_2)=
\begin{cases}
a,&s<49,\\
1-a,&s\ge49.
\end{cases}
$$

Uniform $u,u_1,u_2$ give kernels $B$ and $C$ exactly. These threshold maps
are fixed parts of the evaluator, not fitted tables.

## 3. Boundary and history types

For every finite cardinality $n$, the process boundary objects are

$$
0_n,
\qquad
1_n^0,
\qquad
1_n^r,
\qquad
2_n^0,
\qquad
2_n^r.
$$

Here $0$ is the source, $1$ the native candidate boundary, and $2$ the
endpoint. Superscript $0$ has no record register; superscript $r$ carries a
binary record sector.

The exact legal fields are as follows. A source-boundary value at $0_n$ is

$$
z_0=((q_{0i},h_i,c_i,e_i^0))_{i=1}^n.
$$

The relational packet of occurrence $i$ is

$$
a_i=(x_i,y_i,\epsilon_i,x'_i,y'_i,e'_i,z_{Xi},z_{Yi},u_{Xi},u_{Yi},d_i),
\qquad d_i=e'_i.
$$

A value at $1_n^0$ is $((m_i,h_i,a_i))_i$; a value at $1_n^r$ is
$((m_i,r_i,h_i,a_i))_i$ with $r_i=m_i$. A value at $2_n^0$ is

$$
((q_{2i},t_i,a_i))_i,
\qquad (\ell_{ij})_{i<j},
$$

and a value at $2_n^r$ additionally contains $(r_i)_i$. In either endpoint
type $t_i=h_i$. No other field is legal on these boundaries.

A complete history contains its source-boundary value, every boundary value
actually traversed by its typed process path, and its target value. It does
not contain a private random seed. In particular, an unqueried $U$ history
contains no fictitious $B_1$ value.

Experiment marks, mechanism programs, and program names are *not* physical
history fields. They index which law value is being evaluated and which
reader is used. Putting them into the history would make two interventions
artificially distinguishable from their metadata alone. A complete physical
history therefore includes exactly:

- the cardinality and the boundary types actually traversed;
- every occurrence and every legal field on those boundaries;
- every generated bond with both endpoints;
- every record field present on a traversed boundary; and
- no enumeration order beyond a presentation.

For the unmarked observational law, the physical sigma algebra is the full
power set of the countable union of finite history orbits. For a marked
experiment it is instead the full power set of the diagonal
experiment--history orbit fiber defined in Section 9.

## 4. Exact seed spaces

For fixed $n$, a labeled seed contains for each occurrence $i$:

$$
q_{0i},h_i,c_i,e_i^0\in\mathbb B,
$$

$$
\eta_{Xi},\eta_{Yi}\in\mathbb B,
\qquad
u_{1i},u_{2i}\in[25],
$$

and for each unordered pair $i<j$ one bond seed $v_{ij}\in[25]$.

The primitive seed law is a product law:

$$
P(q_0)=P(h)=P(c)=P(e)=\frac12,
$$

$$
P(\eta_J=0)=\frac{16}{25},
\qquad
P(\eta_J=1)=\frac9{25},
$$

with $u_1,u_2,v$ uniform on $[25]$. The global cardinality law is

$$
P(N=n)=2^{-(n+1)}.
$$

All factors are fixed and positive. A context is a nonempty cylinder condition
on the public source-boundary variables $q_0,h,c,e^0$. Mechanism programs are
separate law inputs, not random variables on which one conditions. Transition,
matter-noise, and bond coins remain private. Every admitted context therefore
has a uniquely normalized conditional seed law. An inconsistent cylinder is
refused rather than assigned a zero-denominator conditional law.

## 5. The process-path category

For each $n$, let $\mathsf P_n$ be the finite category generated by

$$
U:0_n\to2_n^0,
$$

$$
Q^0:0_n\to1_n^0,
\qquad
D:1_n^0\to2_n^0,
$$

$$
Q^r:0_n\to1_n^r,
\qquad
R_c:1_n^r\to2_n^r,
$$

and identities at every object. The only nonidentity composites are

$$
D\circ Q^0:0_n\to2_n^0,
$$

$$
R_c\circ Q^r:0_n\to2_n^r.
$$

$U$ bypasses the candidate boundary. It is not identified with either
composite. Source and target equality determine composition; every mismatched
word is refused. This is an ordinary small category, so identity and
associativity follow from path concatenation.

## 6. Mechanism programs

For each occurrence $i$, the admitted source-stage mechanism slots are

$$
X_i,
\qquad Y_i,
\qquad E_i,
$$

and the admitted mediator-stage slot is $E'_i$. Each has alternative set
$\mathbb B$. No mode variable exists and no generic mechanism retyping is
admitted.

A mechanism program is a word in generators

$$
\operatorname{set}(S,a),
\qquad S\in\{X_i,Y_i,E_i,E'_i}, a\in\mathbb B,
$$

subject to the stage rule: source-stage generators precede mediator-stage
generators. Generators on distinct slots commute. Repeated writes to one slot
are reduced to the last value. A word violating the stage rule or naming an
unlisted slot is not a morphism.

Normal form is therefore a pair of finite partial maps

$$
J=(J_0,J_1),
$$

where $J_0$ acts on $X,Y,E$ and $J_1$ acts on $E'$. Concatenation followed by
last-write normalization is associative; the empty pair is identity.

This mechanism category is not extracted from a joint distribution. It is
primitive typed law data.

## 7. Complete experiments and readers

### 7.1 Execution programs

Let $\mathsf{Exec}_n$ be the category whose objects are the five boundary
types in Section 3 and whose morphisms are legal process paths decorated by
mechanism writes at their named stages. Composition concatenates compatible
paths and then applies the mechanism normal form of Section 6. A downstream
write overrides an earlier write to the same slot. Distinct-slot writes
commute. Boundary mismatch, a write at an unavailable stage, and an unlisted
slot are refused. Path concatenation and last-write normalization prove
identity and associativity.

This $\mathsf{Exec}_n$ is the experiment-program category. We write
$\mathsf{Exp}_n$ for its set of closed, source-argument-and-reader-decorated
evaluation packets in Section 7.2, and $\mathsf{Exp}=\coprod_n\mathsf{Exp}_n$
plus the grand observational identity. Thus $\mathbf\Gamma$ is evaluated on
closed packets, while the composition symbol refers to their underlying
$\mathsf{Exec}$ morphisms. This prevents the common but ill-typed operation
of “composing” two already normalized conditional probability measures.

Conditioning is not this composition. A nontrivial context is attached only
after an execution word has been composed, at the source of the resulting
closed execution. Underlying execution morphisms compose; two already closed
source-conditioned probability laws do not. Conditioning on an intermediate
reader cell is instead the separately named derived operation
$\operatorname{Cond}$, and exists only for a positive-probability cell.

### 7.2 Closed experiments

For a path $p:S\to T$, let $\Omega_n(p)$ be the finite set of all
type-correct complete physical histories traversing $p$, whether or not a
particular experiment assigns them positive mass. Let $\mathsf{Val}_n(T)$ be
the finite set of legal target-boundary values. A target reader is a set
partition $\Pi$ of $\mathsf{Val}_n(T)$. Its value on a history is the cell
containing that history's target projection. Every partition is admitted;
the discrete partition is the complete reader and coarser partitions are
diagnostic readers. Thus reader completeness is a constructor, not a short
list of examples.

A fixed-$n$ closed experiment is the exact tuple

$$
e=(\mathcal H_Z,Z,p,J,K,M,\Pi),
$$

where:

- $\mathcal H_Z$ is the presented source frame with its $n$ occurrences and
  typed ports;
- $Z$ is one of the five named source-boundary types;
- $p:Z\to T$ is a morphism in $\mathsf P_n$;
- $J$ is a legal mechanism normal form, equivalently a finite composite of
  marked pairs $(A,a)$ with $a$ in the binary alternative set of slot $A$;
  it must be empty unless $Z=0_n$ because the relational mechanism stage has
  already occurred at later boundaries;
- $K$ is the complete source argument: a consistent cylinder context on
  $z_0$ when $Z=0_n$, and one exact legal boundary value when $Z\ne0_n$;
- $M$ is the finite set of marked occurrences and ports transported with the
  experiment; it must contain every slot in $\operatorname{dom}J$ and may
  contain additional reader probes; and
- $\Pi$ is a reader in the complete catalogue for $T$.

For one primitive replacement this is exactly the pinned packet
$(H,Z,A,a,R,E)$: $H=\mathcal H_Z$, $Z$ is the complete typed source argument,
$(A,a)$ is the
one-write program, $R=\Pi$, and the exterior data $E$ are $(p,K,M)$ together
with every unmodified slot governed by the global evaluator. General $J$ is
the unique composite normal form of such generators.

A composed execution program may carry an ordered list of nondisturbing reader
maps at traversed targets; it does not condition on their values. Program
composition concatenates the execution morphisms, transports and unites the
marks, retains that reader list, and uses the final target reader when the
program is closed with one initial source argument. This makes program
composition, observation, and postselection distinct exact operations.

The all-size family is the disjoint union of these finite categories. The
distinguished no-manipulation experiment

$$
\mathbb 1_{\rm obs,n}
=(\mathcal H_0,0_n,U,\varnothing,\top,\varnothing,\Pi_{\rm disc})
$$

is called the identity experiment because its mechanism program is the
identity and its context is tautological; it is not the identity path of
$\mathsf P_n$. The grand observational identity mixes these experiments
with the fixed geometric cardinality law.

Independent tensoring and physical fusion are not conflated. The external
tensor $e\boxtimes f$ is a pair of separately tagged trials with product seed
law, product reader, and no cross-pair field. By contrast, a single
size-$(n+m)$ experiment is a fused trial governed by the same all-size
evaluator and includes fresh cross-bond seeds. It is generally not
$e\boxtimes f$. Exchange of independent tensor factors is symmetric, while
fusion order independence is the separate theorem in Section 11.

## 8. One global evaluator

For $Z=0_n$, draw the public source variables and private seed $\xi$ from the
fixed law conditioned on $K$. For $Z\ne0_n$, $K$ supplies the exact source
boundary value and $\xi$ contains only the fresh private coins required after
that boundary. This is one typed evaluator by cases on $Z$, not a fitted
per-experiment kernel.

### 8.1 Relational stage

This stage is evaluated exactly once, and only when the source is $0_n$.

First set

$$
x_i=
\begin{cases}
J_0(X_i),&X_i\in\operatorname{dom}J_0,\\
c_i\oplus\eta_{Xi},&\text{otherwise},
\end{cases}
$$

and analogously for $y_i$. Set the effective relation value

$$
\epsilon_i=
\begin{cases}
J_0(E_i),&E_i\in\operatorname{dom}J_0,\\
e_i^0,&\text{otherwise}.
\end{cases}
$$

Compute

$$
x'_i=x_i\oplus\epsilon_i,
\qquad
y'_i=y_i\oplus\epsilon_i,
$$

$$
\widehat e'_i=\epsilon_i\oplus x_i\oplus y_i.
$$

Then set

$$
e'_i=
\begin{cases}
J_1(E'_i),&E'_i\in\operatorname{dom}J_1,\\
\widehat e'_i,&\text{otherwise}.
\end{cases}
$$

The downstream fields are

$$
z_{Xi}=x_i\oplus e'_i,
\qquad
z_{Yi}=y_i\oplus e'_i,
$$

$$
u_{Xi}=x_i\oplus c_i,
\qquad
u_{Yi}=y_i\oplus c_i.
$$

This is the complete mechanism action. Refactorizing its identity-output
measure does not alter these rules.

### 8.2 Process paths

For $p=U$, set

$$
q_{2i}=\kappa(q_{0i},u_{1i},u_{2i})
$$

and create no $m_i$ or $r_i$ field.

For $p=Q^0$, set

$$
m_i=\beta(q_{0i},u_{1i})
$$

and terminate at $1_n^0$.

For $p=Q^r$, use the same $m_i$ and write $r_i=m_i$, terminating at
$1_n^r$.

For $p=D\circ Q^0$, additionally set

$$
q_{2i}=\beta(m_i,u_{2i})
$$

and create no record.

For $p=R_c\circ Q^r$, use the same endpoint rule and carry $r_i=m_i$.
In every endpoint path set $t_i=h_i$.

For the standalone arrow $D:1_n^0\to2_n^0$, take the supplied exact
$1_n^0$ value, draw fresh independent $u_{2i}$ and $v_{ij}$, and apply the
same endpoint and bond rules. For $R_c:1_n^r\to2_n^r$, do the same and carry
the supplied $r_i$. An identity arrow copies its complete supplied boundary
value and draws no coin. These clauses evaluate every generator and identity
of $\mathsf P_n$. They also make the directly evaluated composites equal to
categorical composition of the corresponding kernels.

### 8.3 Generated bonds

If and only if the target has type $2_n^0$ or $2_n^r$, let the endpoint color
be $d_i=e'_i$. For $i<j$, define

$$
\ell_{ij}=1
\quad\Longleftrightarrow\quad
v_{ij}<
\begin{cases}
16,&d_i\ne d_j,\\
9,&d_i=d_j.
\end{cases}
$$

The bond is generated with its unordered endpoints. It is not a dormant
lattice edge. A target of type $0_n$, $1_n^0$, or $1_n^r$ has no bond field
and draws no $v_{ij}$.

The evaluator returns the complete labeled physical history specified in
Section 3. The experiment and reader remain external typed arguments; their
names are not inserted into the history. Denote the result
$\mathcal E_n(e,\xi)$.

## 9. Definition of executable Gamma

For every admitted experiment $e$, define

$$
\widetilde{\mathbf\Gamma}(e)
=(\mathcal E_n(e,\cdot))_*P_Z(d\xi\mid K),
$$

where $P_{0_n}$ is the conditioned seed law of Section 4, $P_{1_n^0}$ and
$P_{1_n^r}$ are the fresh product laws of the remaining $u_2$ and bond seeds,
and $P_{2_n^0},P_{2_n^r}$ are point masses for identity executions. Thus a
standalone continuation is a kernel evaluated at a supplied complete
boundary value, not a posterior factorization of the observational law.

The presentation group is

$$
\mathcal G_n=(C_2)^n\rtimes S_n,
$$

where each $C_2$ exchanges $X_i,Y_i$ and all their transported fields, while
$S_n$ permutes occurrences and bond endpoints. It transports the complete
source frame, boundary values, path endpoints, $J,K,M$, and $\Pi$.

The quotient is diagonal in experiment and outcome. For a presented
experiment $e$, let

$$
\mathcal G_e=\{g\in\mathcal G_n:g\cdot e=e\}
$$

be its stabilizer. A physical outcome over the physical experiment $[e]$ is
the diagonal orbit of the pair $(e,H)$; in the representative-$e$ fiber it is
equivalently the stabilizer orbit $[H]_e=\mathcal G_e\cdot H$. Define

$$
\mathbf\Gamma([e])([H]_e)
=\sum_{H'\in[H]_e}
\widetilde{\mathbf\Gamma}(e)(H').
$$

If $e$ is replaced by $g\cdot e$, this cell is transported to
$[g\cdot H]_{g\cdot e}$. This joint quotient retains the physical location
of a marked intervention relative to its outcome. Quotienting the history
alone by the full group would incorrectly erase that relation. For the
unmarked observational identity, $\mathcal G_e=\mathcal G_n$ and the formula
reduces to ordinary history-orbit pushforward.

All smaller observational objects are shadows of this law. For a marked set
$A$ of occurrences, $\operatorname{Res}_A$ retains their boundary fields and
internal bonds and deletes every other occurrence and incident bond; the
regional law is $(\operatorname{Res}_A)_*\mathbf\Gamma(e)$. For a reader
partition $\Pi$, its law is the pushforward under the target-cell map. For a
positive reader cell $C$, the postselected law is the ordinary normalized
restriction $\operatorname{Cond}(\mathbf\Gamma(e),C)$. None of these shadows
is an independently supplied regional kernel or intervention rule.

The grand identity law is

$$
\mathbf\Gamma(\mathbb 1_{\rm obs})
=\sum_{n\ge0}2^{-(n+1)}
\mathbf\Gamma(\mathbb 1_{\rm obs,n}).
$$

### Theorem 1 — totality and normalization

Every admitted experiment has one evaluator normal form and a normalized
physical output law. Every unlisted or ill-typed experiment is refused before
evaluation.

#### Proof

Process paths and mechanism words have unique normal forms. Context cylinder
conditioning is unique because all primitive source masses are positive. The
finite seed law is normalized, and a deterministic pushforward preserves
normalization. Stabilizer orbits partition the labeled outcome fiber.
Equivariance makes the mass constant on each stabilizer orbit, so its physical
mass is the representative mass times the exact orbit cardinality; fixed
points and other automorphisms are therefore counted rather than discarded.
The grand law is normalized by the geometric series. ∎

### Theorem 2 — law identity is interventional

$\mathbf\Gamma$ is not determined by its identity value. A map with the same
identity measure but a different mechanism evaluator is a different law.

#### Proof

Equality of executable laws means equality as functions on every experiment
object. Equality at one object, including identity, is insufficient. The
mechanism rules in §8 are part of the definition, so a chain-rule
refactorization of the identity measure is never consulted. ∎

## 10. Presentation covariance

### Theorem 3 — experiment and output descent

For every $g\in\mathcal G_n$,

$$
\widetilde{\mathbf\Gamma}(g\cdot e)
=g_*\widetilde{\mathbf\Gamma}(e).
$$

#### Proof

The seed product measure is exchangeable. The internal swap exchanges the
$X/Y$ source bits, noise bits, mechanism slots, downstream fields, marks, and
reader cells, while fixing the unordered relation color. Atom permutation
transports every pair seed and bond endpoint. The deterministic evaluator is
equivariant at each stage. Hence the labeled output measures correspond term
by term. The diagonal orbit construction of Section 9 then gives a
representative-independent physical probability kernel over experiment
orbits. ∎

At a symmetric occurrence, `set(X,1)` and `set(Y,1)` are distinct marked
presentations in one experiment orbit when the mark and reader transport. A
naked slot name is not a physical experiment.

## 11. Varying-size theorem

The conditional identity law at size $n$ uses iid occurrence seeds and
endpoint-conditioned pair seeds. Deleting a uniformly selected occurrence
and all its incident pair seeds leaves precisely the size-$(n-1)$ seed law.

### Theorem 4 — projectivity and order independence

Uniform deletion also deletes the corresponding source-frame occurrence,
marks if any, traversed boundary fields, and incident bonds. On the unmarked
observational family it commutes with physical quotient and sends the identity
size-$n$ law to the identity size-$(n-1)$ law. Adding two occurrences in
either auxiliary order gives the same joint evaluator law.

#### Proof

All surviving occurrence factors and pair factors are unchanged after
deletion. Exchangeability makes the deleted presentation index irrelevant.
For addition, both auxiliary orders produce the same occurrence seeds and the
same unordered set of pair seeds, including the cross-pair seed. Finite factor
multiplication commutes. ∎

Every realized history is finite. Cardinality is physical multiplicity, not
time, volume, or a global clock.

## 12. Native boundary and cut-relative nondivision

For one occurrence with fixed $q_0=a$, the native query experiments satisfy

$$
P(m=j\mid Q^0,q_0=a)=P(m=j\mid Q^r,q_0=a)=B_{ja}.
$$

The unqueried native path satisfies

$$
P(q_2=b\mid U,q_0=a)=C_{ba}.
$$

These two kernels are unchanged after conditioning on any common exterior
source context in $h,c,e^0$ because their private transition coins are
independent of that context. Thus the comparison preserves the complete
declared exterior rather than averaging away a distinguishing field.

Thus $B_1$ is an actual object of the experiment category and $B$ is the
shadow of native query morphisms. It need not be a realized boundary in $U$.
The candidate carrier is exactly the $1_n^0$ or $1_n^r$ value listed in
Section 3. It does not carry $q_0$, a seed, or a past-history identifier. A
continuation may be indexed by a fixed common exterior context, but it may not
read the stochastic input $q_0$ except through $m$. Enlarging the carrier to
$(m,q_0)$ would make a positive restart trivial, but it would be a different
declared cut and is an explicit nonkill rather than a repair of this one.

Suppose the unqueried endpoint law factored stochastically through that native
query interface. Then $C=KB$. Since $B$ is invertible,

$$
K=CB^{-1}=
\frac1{175}
\begin{pmatrix}
351&-176\\
-176&351
\end{pmatrix}.
$$

No positive normalized $K$ exists.

For $n\ge1$, conditioning on the complete common relational exterior leaves
the process coordinates independent, so the unique candidate is

$$
K_n=(CB^{-1})^{\otimes n}.
$$

It has a negative entry: choose one negative one-occurrence factor and
positive diagonal factors on all other occurrences. The $n=0$ empty process
is a unit nonkill.

### Theorem 5 — native $B_1$ cut nondivision

For every nonempty size, the unqueried $U$ experiment is not stochastically
divisible through its declared native $B_1$ query interface.

This is cut-relative. $C=CI=IC$ uses other carriers and is an explicit
nonkill. Querying $B_1$ changes the experiment and may change the endpoint
law.

## 13. Query, record, and division

A frontier $F$ of a closed experiment is a **complete division** precisely
when there is a positive normalized continuation kernel $K_F$ on the complete
typed frontier values such that (i) any two positive-probability past
histories with the same $F$ value give the same law for every licensed future
reader, and (ii) the directly evaluated whole law equals the cut sum through
$K_F$ on every admitted source value and exterior context. A restricted
frontier fails as soon as either clause fails. No hidden history identifier
may be appended after the test.

A record field is **stable** precisely when it has at least two
positive-probability sectors and every word in the exact future grammar of
Section 14 has transported sector projectors satisfying
$P_r^{\rm out}F=FP_r^{\rm in}$. Stability neither asserts nor presupposes
future sufficiency of the rest of the frontier.

The nonrecording queried path $D\circ Q^0$ has joint kernel

$$
P(m,q_2\mid q_0)=B_{mq_0}B_{q_2m}
$$

and endpoint $B^2$. Its $1_n^0$ boundary is a complete positive division with
no record. More strongly, for every complete source value and target history,
the direct evaluator sum through $1_n^0$ equals composition of the $Q^0$ and
$D$ kernels: the relational packet is copied, while $u_2$ and every endpoint
pair seed are fresh and independent. Thus the division claim is not inferred
from the displayed two-state marginal alone.

The recording path $R_c\circ Q^r$ has the same branch law, writes $r=m$, and
carries $r$ to $2_n^r$. Its complete $1_n^r$ boundary is exactly
$((m_i,r_i,h_i,a_i))_i$. Conditional on that value, all remaining $u_2$ and
pair seeds are independent with their frozen laws, so it is future-sufficient
and supports the positive $B$ continuation and the declared bond generator.

The restricted record-only frontier retains only $(r_i)_i$ and omits $h$ and
the relational packet. Equal $r$ with opposite $h$
gives opposite deterministic $t=h$, so it is stable but not a complete
division.

The unqueried $U$ path has no record and fails division through native $B_1$.

### Theorem 6 — record/division independence square

| stable record | complete division | experiment/frontier |
|---|---|---|
| yes | yes | $R_c\circ Q^r$, complete $1^r$ frontier |
| yes | no | $R_c\circ Q^r$, record-only frontier |
| no | yes | $D\circ Q^0$, complete $1^0$ frontier |
| no | no | unqueried $U$ through candidate $B_1$ |

The four cells are values of one executable law on different typed
experiments, not a posterior model menu. ∎

## 14. Stable future grammar

For recorded targets, let $P_0,P_1$ be the record-sector projectors. The
licensed future grammar is generated by the following exact bijections, each
applied to any declared subset of occurrences:

- $F_q$ toggles $q_2$ and leaves every $r$ unchanged;
- $F_t$ toggles $t$ and leaves every $r$ unchanged;
- $F_{XY}$ exchanges all $X/Y$-typed entries of the relational packet and
  transports the reader, leaving $e',r$ and bonds unchanged; and
- $F_r$ toggles $r$ while transporting the sector names and output reader by
  $P_r^{\rm out}=F_rP_r^{\rm in}F_r^{-1}$.

Composition of these finite bijections and identities is the entire licensed
grammar; there is no additional generator hidden behind the word “lawful.”

Every generator satisfies

$$
P_r^{\rm out}F=FP_r^{\rm in}.
$$

Therefore every finite licensed word preserves exact recoverability by
induction. The reversible record-label swap is a nonkill. A many-to-one reset
$E_r:(r_i)_i\mapsto(0)_i$ is the admitted eraser control, not a licensed
stable future, and fails recoverability whenever both input sectors occur.

## 15. Exact interventional response

Because mechanism programs are primitive inputs to $\mathbf\Gamma$, the
following are law-defined interventions, not factorization choices.

For every path $p$, consistent source context $K$, legal base program $J$ not
writing slot $S$, transported mark set $M$ containing $S$, alternative pair
$a,b\in\mathbb B$, target reader $\Pi$, and reader cell $A\in\Pi$, define the
complete signed response coordinate

$$
\Delta^{p,J,K,M,\Pi}_{S;a,b}(A)
=\widetilde{\mathbf\Gamma}(e[J;S\leftarrow a])
  (\operatorname{target}\in A)
-\widetilde{\mathbf\Gamma}(e[J;S\leftarrow b])
  (\operatorname{target}\in A).
$$

Here both probabilities are computed by the same seed law and global
evaluator in one common presented frame; only the named mechanism value
differs. The tensor is the family of these coordinates over *all* legal
indices, not a selected scalar. The presentation group transports the entire
contrast $(e_a,e_b,A)$, and Theorem 3 makes $\Delta$ constant on its diagonal
orbit. That orbit, rather than a naked slot name or a separately quotiented
outcome, is the physical response coordinate. The discrete reader is always
retained alongside diagnostic coarse readers.

### 15.1 Matter to relation and bonds

At fixed $Y,E$, `set(X,1)` versus `set(X,0)` flips $e'$. The complete $E'$
reader has total-variation response one. The endpoint color also flips, so
every incident bond probability changes by signed magnitude

$$
\frac{16}{25}-\frac9{25}=\frac7{25}.
$$

### 15.2 Relation to matter

At fixed $X,Y$, changing $E$ flips both $x'$ and $y'$. The complete pair
reader has total-variation response one.

### 15.3 Mediation

Without an $E'$ override,

$$
z_Y=y\oplus e'=\epsilon\oplus x,
$$

so $X\to Z_Y$ has total response one. Holding $E'$ fixed with the admitted
mediator-stage generator makes $z_Y=y\oplus e'$ independent of $X$; the direct
residual is zero.

### 15.4 Common cause

In the identity experiment,

$$
P(y=1\mid x=1)=\frac{337}{625}.
$$

Under `set(X,1)`, $Y$ retains its source mechanism and remains marginally
fair:

$$
P(y=1\mid\operatorname{set}(X,1))=\frac12.
$$

The executable law, not observational conditioning, defines the second row.

### 15.5 Reader cancellation

Changing $E$ flips the complete pair $(x',y')$ but leaves the parity
$x'\oplus y'=x\oplus y$ unchanged. The parity partition is a diagnostic
reader with a false zero; the discrete partition detects response.

### 15.6 Context reversal and spectator

For $u_X=x\oplus c$, the signed `set(X,1)` minus `set(X,0)` effect on
$u_X=1$ is $+1$ at $c=0$ and $-1$ at $c=1$. The complete tensor retains
context. The process source $q_0$ is a spectator for relational outputs and
has exact response zero.

### 15.7 Symmetric joint onset control

The evaluator creates $(x',y',e')$ in one relational stage and transports the
triple covariantly under $X\leftrightarrow Y$. This is a joint mechanism
control. It is not by itself a derived co-onset bundle or chronology edge.

### Theorem 7 — reciprocal relational response

The accepted experiment generators give nonzero matter-to-relation and
relation-to-matter signed tensors, with exact common-cause, mediation,
cancellation, reversal, symmetry, and spectator controls. The result is
presentation-covariant by Theorem 3.

It is relational response, not geometry, metric response, backreaction,
energy, or gravity. ∎

## 16. Actuality and permanent walls

$\mathbf\Gamma(e)$ supplies possible complete histories for every experiment.
It selects no actual history. Actualization is unconstructed.

The law contains no derived chronology, causal order, signal cone, dimension,
signature, topology, volume, duration, scale, metric, connection, curvature,
stress tensor, energy, entropy, gravity, GR, continuum limit, QFT, particle,
or phenomenology.

The generated graph ensemble may later fail every manifoldlike test. Such a
failure does not authorize retuning this law.

## 17. Provisional product vector

Subject to independent mathematical hostile review:

```text
referent    P13C-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED
law         P13C-ONE-INTERVENTIONALLY-COMPLETE-GAMMA-CONSTRUCTED
experiment  P13C-TYPED-EXPERIMENT-CATEGORY-CONSTRUCTED
nondivision P13C-NATIVE-B1-CUT-NONDIVISIBLE
record      P13C-GRAMMAR-STABLE-RECORD-CONSTRUCTED
division    P13C-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13C-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13C-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13C-ACTUALIZATION-UNCONSTRUCTED
```

These are `GREEN-UNREVIEWED`, not terminal and not citable.
