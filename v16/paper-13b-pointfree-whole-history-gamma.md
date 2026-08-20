# One point-free whole-history law

## Abstract

We construct one exact probability law on isomorphism classes of complete
finite typed relational histories. The law is fixed before evaluation. Its
only nontrivial numerical seed is the least primitive rational rotation; no
parameter, dimension, geometry, metric, or desired large-scale behavior is
selected afterward. Complete histories are finite relational structures whose
atoms are joined by an exchangeable endpoint-generated bond field. Internal
port relabelings and permutations of atoms are presentation changes, and
physical probabilities are orbit pushforwards, never representative masses.

Thus varying size produces relational ensembles rather than a dormant fixed
carrier or a bag of disconnected labels. The same law contains four logically
independent record/division cases, an
exact native cut with no positive stochastic restart, a grammar-stable record
theorem, complete marked-intervention semantics, and reciprocal
matter--relation response. Conditional laws at every cardinality are
exchangeable and projectively consistent under uniform deletion. The result
is a finite, point-free, varying-size indivisible relational law. It does not
derive actuality, chronology, dimension, topology, volume, duration, metric,
curvature, gravity, or continuum physics.

## 1. Scope and status

This paper defines a candidate primitive law. It does not derive that law from
a deeper principle. The candidate is fixed by the mathematical declaration
below before any dimensional or geometric test is permitted.

The physical objects are complete history and complete experiment orbits.
Labels, enumeration order, representative choice, and the auxiliary order in
which independent components are written are presentation data.

The construction is classical as a probability law. A rational orthogonal
matrix is used only to define exact transition probabilities and the native
nondivision control. It is a representation, not an additional ontic field.

## 2. The fixed numerical seed

Every nontrivial rational rotation is parameterized by a primitive
Pythagorean triple. The primitive triple with least hypotenuse greater than
one is uniquely $(3,4,5)$ up to signs and interchange. Fix the orientation
convention

$$
R=
\begin{pmatrix}
3/5 & -4/5\\
4/5 & 3/5
\end{pmatrix}.
$$

Only squared entries enter the physical one-step law:

$$
B=|R|^2=
\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix}.
$$

The unrecorded coherent two-step law is

$$
C=|R^2|^2=
\frac1{625}
\begin{pmatrix}
49&576\\
576&49
\end{pmatrix},
$$

while the recorded two-step law is

$$
B^2=
\frac1{625}
\begin{pmatrix}
337&288\\
288&337
\end{pmatrix}.
$$

Both matrices are bistochastic. No later result selects among rotations.
The least-triple convention is part of the frozen definition.

All unresolved binary priors below are fair. The three declared process modes
have equal prior mass. The finite-size stopping law is the fair geometric law.
These are explicit primitive choices, not derived necessities.

## 3. The typed local history atom

Write $\mathbb B=\{0,1\}$ with addition $\oplus$ modulo two. One local atom
has three mutually distinguishable process modes

$$
w\in\{U,R,D\},
$$

standing for unrecorded, recorded, and division-without-new-record.

It also has:

- a process input $q_0\in\mathbb B$;
- a carried context bit $h\in\mathbb B$;
- two exchangeable matter ports $X,Y$;
- an unordered relational port $E$ joining $X$ and $Y$;
- a common-source bit $c\in\mathbb B$; and
- two independent source-noise bits $\eta_X,\eta_Y$.

The source law is

$$
P(q_0)=P(h)=P(c)=P(e)=\frac12,
$$

$$
P(\eta_J=0)=\frac{16}{25},
\qquad
P(\eta_J=1)=\frac9{25},
\qquad J\in\{X,Y\},
$$

with all displayed primitive variables independent, and

$$
x=c\oplus\eta_X,
\qquad
y=c\oplus\eta_Y.
$$

The relational output is the fixed bijective Boolean transformation

$$
x'=x\oplus e,
\qquad
y'=y\oplus e,
$$

$$
e'=e\oplus x\oplus y,
$$

$$
z_X=x\oplus e'=e\oplus y,
\qquad
z_Y=y\oplus e'=e\oplus x,
$$

$$
u_X=x\oplus c,
\qquad
u_Y=y\oplus c.
$$

Bijectivity of the $(x,y,e)\mapsto(x',y',e')$ core is explicit:

$$
e=e'\oplus x'\oplus y',
\qquad
x=x'\oplus e,
\qquad
y=y'\oplus e.
$$

The pair $(z_X,z_Y)$ is a later matter readout downstream of the relational
field $e'$. The pair $(u_X,u_Y)$ is a context-sensitive readout used to retain
the sign of response rather than only its maximum magnitude.

### 3.1 Process-mode kernel

The mode is sampled with $P(w)=1/3$.

For $w=U$, no intermediate state or record is a random variable of the
physical history. The final process bit is sampled directly by

$$
P(q_2=b\mid q_0=a,w=U)=C_{ba}.
$$

For $w=R$, sample

$$
P(m=j\mid q_0=a,w=R)=B_{ja},
$$

write the record $r=m$, and then sample

$$
P(q_2=b\mid m=j,w=R)=B_{bj}.
$$

For $w=D$, use the same two stochastic steps through $m$ but write no new
record. In every mode the late carried-context readout is $t=h$.

The local labeled law $\widetilde\mu$ is the product of the declared source
law, the mode weight, the appropriate process-mode kernel, and the
deterministic relational outputs. It is a completely determined rational
probability distribution on a finite set $\mathcal A$ of labeled atoms.

## 4. Point-free local and whole histories

### 4.1 Local presentation action

Let $\tau$ exchange the matter ports $X$ and $Y$. It acts simultaneously on

$$
(x,y),\ (\eta_X,\eta_Y),\ (x',y'),\ (z_X,z_Y),\ (u_X,u_Y)
$$

and fixes the unordered relation fields $e,e'$, the process fields, mode,
context, and record fields. The equations and source weights are invariant
under $\tau$.

The local presentation group is $G_1=\{1,\tau\}$. A physical local atom is an
orbit $o=[a]_{G_1}$, with mass

$$
\mu(o)=\sum_{a'\in o}\widetilde\mu(a').
$$

Fixed points are counted once and two-element orbits twice. A chosen
representative's mass is never used as the orbit mass.

### 4.2 Generated inter-atom relations

Each atom carries the internal-swap-invariant relational color

$$
d(a)=e'(a)\in\mathbb B.
$$

For every unordered pair of distinct atoms, independently conditional on the
endpoint atoms, generate one bond $\ell_{ij}\in\mathbb B$ with

$$
P(\ell_{ij}=1\mid d_i,d_j)=
\begin{cases}
16/25,&d_i\ne d_j,\\
9/25,&d_i=d_j.
\end{cases}
$$

This uses the two entries already fixed by $B$ and introduces no new numerical
parameter. The bond is an unordered relational field. It is generated with
its endpoints and is not a pre-existing lattice edge.

### 4.3 Whole histories

For fixed cardinality $n$, a labeled complete history is an ordered
$n$-tuple in $\mathcal A^n$ together with all generated unordered bond bits.
Its law is

$$
\widetilde\Gamma_n(a_1,\ldots,a_n;\ell)
=\prod_{i=1}^n\widetilde\mu(a_i)
\prod_{1\le i<j\le n}
p_{ij}^{\ell_{ij}}(1-p_{ij})^{1-\ell_{ij}},
$$

where $p_{ij}$ is the endpoint rule above.

The presentation group is the wreath product

$$
\mathcal G_n=G_1^n\rtimes S_n,
$$

which independently exchanges the two matter ports inside every atom,
permutes the atoms, and transports every bond with its unordered endpoints.
A physical history is a complete orbit of the atom-decorated bond structure.
Its conditional mass is the pushforward

$$
\Gamma_n([H])=\sum_{H'\in[H]}\widetilde\Gamma_n(H').
$$

The sum, rather than one representative, automatically includes atom
permutations, internal fixed points, graph automorphisms, and physical
occurrence multiplicity.

Finally choose the physical cardinality by

$$
P(N=n)=2^{-(n+1)},
\qquad n=0,1,2,\ldots.
$$

The one whole-history law is

$$
\Gamma_*([H])=2^{-(|H|+1)}\Gamma_{|H|}([H]).
$$

No infinite pre-existing carrier is activated. The physical carrier of a
history is exactly its finite occurrences and their generated bonds.

### Theorem 1 — normalization and exact descent

$\Gamma_*$ is a normalized probability law on the countable set of physical
finite-history orbits. It is independent of all representative choices,
enumeration orders, and port names.

#### Proof

The atom law sums to one. Conditional on any endpoint atoms, each bond law
sums to one, so the labeled $n$-history law sums to one. The physical orbits
partition the labeled history set, and summing all labeled masses in each
orbit preserves normalization. The geometric series gives
$\sum_{n\ge0}2^{-(n+1)}=1$. Internal exchange and atom permutation preserve
endpoint colors and transport bonds, so every labeled term is carried to a
term of equal mass. The orbit sum retains every labeled realization and
occurrence multiplicity, including at nontrivial automorphisms. ∎

## 5. Varying-size consistency

The conditional family $(\Gamma_n)_{n\ge0}$ is the quotient of one
exchangeable endpoint rule, not a collection of fitted tables.

### Theorem 2 — uniform-deletion projectivity

Choose a physical $n$-history according to $\Gamma_n$, lift it by choosing a
uniform labeled representative, delete a uniformly chosen atom, and quotient
again. The resulting $(n-1)$-history has law $\Gamma_{n-1}$.

#### Proof

Before quotienting, the atoms are iid with law $\widetilde\mu$. Conditional on
them, every surviving pair bond has exactly the same endpoint law after one
atom and its incident bonds are deleted. Exchangeability makes the deleted
index irrelevant, and pushforward commutes with the equivariant deletion
map. ∎

Adding atoms $a$ and $b$ in either auxiliary order generates the same set of
endpoint-conditioned bond factors, including the bond $\ell_{ab}$; finite
factor multiplication commutes. Thus incomparable extensions have the same
law. Every realized history is finite and hence locally finite. No linear
extension or write index is present in the physical sigma algebra.

The count $N$ is physical multiplicity, not time, duration, volume, or a
global clock.

## 6. Complete marked experiments

A labeled experiment packet is

$$
\mathsf e=(H,Z,A,a,R,E),
$$

where $H$ is a complete labeled history, $Z$ the full typed regional argument
including relevant endpoint and bond fields, $A$ a marked intervention slot
in a marked atom, $a$ its forced value, $R$ a
complete reader, and $E$ the complete exterior context. The presentation
group transports all six entries together.

A physical experiment is the action-groupoid orbit $[\mathsf e]$. At a local
atom fixed by $X\leftrightarrow Y$, the packet with `do(X=1)` transports to
the packet with `do(Y=1)`. Neither naked command is a function on the naive
history orbit. The marked orbit, or the full unmarked intervention orbit, is.

### 6.1 Same-law intervention

An intervention replaces exactly one declared structural assignment while
retaining every other factor of $\widetilde\mu$. For example,
`do(X=a)` replaces $x=c\oplus\eta_X$ by $x=a$; `do(E=a)` replaces the source
relation value; and `do(E'=a)` replaces only the mediator assignment before
the downstream $z$ readout. This is truncated evaluation of the same frozen
factor law, not observational conditioning and not a new kernel selected for
the experiment.

A complete reader returns the full finite outcome partition on its declared
future fields. Restricted readers are permitted only as diagnostics and may
not establish separation.

### Theorem 3 — experiment covariance

If $g$ is a presentation isomorphism, then

$$
P_{\Gamma_*}(R=r\mid\operatorname{do}(A=a),E)
=P_{\Gamma_*}(gR=gr\mid\operatorname{do}(gA=ga),gE).
$$

#### Proof

Every primitive source weight is invariant, the relational assignments are
$X\leftrightarrow Y$ equivariant, and the process subsystem is fixed by that
action. Endpoint colors are invariant under the internal exchange, while atom
permutations carry every bond to the bond with transported endpoints.
Replacing one transported assignment and reading the transported partition
therefore bijects terms of equal mass. ∎

## 7. Exact response tensors

For complete exterior context $E$, two values $a,a'$ at a marked slot $A$,
complete reader $R$, and result $r$, define

$$
\Delta^{\Gamma_*}_{A\to R}[E;a,a'](r)
=P(R=r\mid\operatorname{do}(A=a),E)
-P(R=r\mid\operatorname{do}(A=a'),E).
$$

The complete tensor sums to zero over $r$ and descends by Theorem 3.

### 7.1 Matter to relation

With $y,e$ fixed, changing $x$ flips

$$
e'=e\oplus x\oplus y.
$$

The complete binary reader of $e'$ therefore has total-variation response
one.

The response also reaches the generated relational ensemble. Toggling $x$
toggles $d=e'$ and changes every incident bond probability, at fixed other
endpoint color, by signed magnitude

$$
\frac{16}{25}-\frac9{25}=\frac7{25}.
$$

### 7.2 Relation to matter

With $x,y$ fixed, changing $e$ flips both $x'=x\oplus e$ and
$y'=y\oplus e$. The complete pair reader has total-variation response one.
Thus the same fixed law has response in both matter--relation directions.

### 7.3 Exact mediation

The total response $X\to Z_Y$ is one because

$$
z_Y=y\oplus e'=e\oplus x.
$$

If the mediator $e'$ is separately held fixed, $z_Y=y\oplus e'$ is
independent of $x$. The direct residual is zero. This distinguishes total
from direct response without inserting an intermediate division claim.

### 7.4 Common cause is not intervention

The source mechanism gives

$$
P(y=1\mid x=1)=
\left(\frac{16}{25}\right)^2+
\left(\frac9{25}\right)^2
=\frac{337}{625}.
$$

But intervening on $x$ leaves the marginal of $y$ fair:

$$
P(y=1\mid\operatorname{do}(x=1))=\frac12.
$$

The exact observational excess is $49/1250$, while the intervention response
$X\to Y$ is zero.

### 7.5 Reader cancellation

Changing $e$ flips both $x'$ and $y'$. The restricted parity reader sees

$$
x'\oplus y'=x\oplus y
$$

and reports zero response, while the complete pair reader reports response
one. A restricted-reader zero is therefore not separation.

### 7.6 Context reversal and one-way control

For $u_X=x\oplus c$, the signed effect of `do(X=1)` versus `do(X=0)` on the
outcome $u_X=1$ is $+1$ at $c=0$ and $-1$ at $c=1$. A scalar maximum would
erase this reversal; the tensor retains it.

The process source $q_0$ is a typed spectator for relational readouts, so its
intervention response to $e'$ is zero. This is an exact one-way negative
control inside the same law.

### Theorem 4 — reciprocal relational response

The point-free marked-experiment law has nonzero matter-to-local-relation,
matter-to-inter-atom-bond, and relation-to-matter response tensors, an exactly
mediated route, a common-cause observational false positive, a
restricted-reader false zero, a context-sign reversal, and a typed spectator
zero.

No part of this theorem names chronology, geometry, metric response,
backreaction, energy, or gravity. ∎

## 8. Stable records and licensed futures

In recorded mode, the record register has basis sectors $r=0,1$ and diagonal
projectors $P_0,P_1$. A continuation state contains

$$
(r;q_2,t,x',y',e',z_X,z_Y,u_X,u_Y).
$$

The licensed future grammar is generated by:

1. $F_Q$, which toggles $q_2$ and fixes $r$;
2. $F_T$, which toggles $t$ and fixes $r$;
3. $F_{XY}$, which exchanges every $X/Y$-typed field and fixes $r$; and
4. $F_R$, the reversible record-label swap, with transported output sectors
   $P_r^{\rm out}=P_{1-r}^{\rm in}$.

Each generator is a typed bijection. For every generator,

$$
P_r^{\rm out}F=FP_r^{\rm in}.
$$

### Theorem 5 — grammar-stable record

For every finite licensed word $W=F_k\cdots F_1$,

$$
P_r^{\rm out}W=WP_r^{\rm in}.
$$

Consequently a complete reader, transported with the known word, recovers the
written record exactly.

#### Proof

Compose the generator intertwining equalities. ∎

The reversible swap $F_R$ is not an eraser. The noninjective map sending both
record values to zero is a true eraser: it merges the two sectors, has no
inverse transported reader, and is not licensed.

## 9. Division and nondivision

### 9.1 Recorded complete frontier

In mode $R$, the frontier

$$
Z_R=(m,r,h;\text{all relational source and incident-bond fields})
$$

is complete. Conditional on it, the late process law is $B_{q_2m}$, the
carried readout is $t=h$, and the relational future is determined by its full
source and endpoint fields. The joint law factors through $Z_R$ with
nonnegative normalized kernels. Direct and cut evaluations agree term by
term.

### 9.2 Stable but incomplete frontier

The restricted frontier containing $r$ but omitting $h$ retains a perfectly
stable record. It is not future-sufficient: histories with equal $r$ and
opposite $h$ have distinct deterministic future readouts $t=h$.

### 9.3 Complete division without a new record

In mode $D$, the frontier

$$
Z_D=(m,h;\text{all relational source and incident-bond fields})
$$

is future-sufficient and supports the same positive $B$ continuation, but no
record register is written. A lawful division need not be a new stable
happening.

### 9.4 Native indivisible cut

In mode $U$, the physical whole transition is $C$. Suppose a two-state
restart through the proposed $B$ intermediate carrier existed. It would
require a stochastic matrix $K$ satisfying

$$
C=KB.
$$

Since $B$ is invertible, the unique candidate is

$$
K=CB^{-1}=
\frac1{175}
\begin{pmatrix}
351&-176\\
-176&351
\end{pmatrix}.
$$

Its negative entries rule out a positive restart kernel. The whole law $C$
remains normalized. No phase, history identifier, cache, clock, or enlarged
state is added to repair this declared carrier.

An explicitly enlarged history carrying the intermediate branch and record
has the positive $B^2$ law. This is a separate explanatory control, not a
factorization of the native unrecorded cut.

### Theorem 6 — independence square

The one fixed law realizes all four cases:

| stable record | complete division | witness |
|---|---|---|
| yes | yes | mode $R$ at $Z_R$ |
| yes | no | mode $R$ at the restricted $r$ frontier |
| no | yes | mode $D$ at $Z_D$ |
| no | no | mode $U$ at the proposed $B$ cut |

Thus stable happening-record and lawful probabilistic division are distinct
coordinates. ∎

## 10. One law, not a model menu

Modes $U,R,D$ are values of a typed source field inside one normalized joint
law. They are no more separate laws than different matter preparations are.
The conditional kernels are fixed before the mode is sampled or intervened
upon. No result chooses their probabilities.

The only rational transition seed is fixed by the least primitive
Pythagorean triple. Fair binary priors, equal mode weights, and the geometric
cardinality prior are declared parts of the primitive candidate. Their
physical uniqueness is not claimed.

This candidate is therefore selected by stipulation and simplicity, not
derived from observations. Later failure to generate chronology or a stable
dimension would reject those later coordinates; it may not trigger retuning
of this law.

## 11. Actuality and ontology

$\Gamma_*$ supplies possible complete physical histories and their exact
probabilities. It does not select one history as actual. Actualization is
unconstructed.

The ontic proposal tested here is limited to one complete-history probability
law on finite relational occurrences. The rational rotation, labeled
representatives, construction indices, and factorization notation are
representations. Stable records are possible durable facts conditional on a
realized branch; no realized branch is selected by this paper.

## 12. Provisional result vector

Subject to independent mathematical hostile review, the construction supports
the following provisional coordinates:

```text
referent    P13B-POINT-FREE-HISTORY-REFERENT-CONSTRUCTED
law         P13B-ONE-WHOLE-HISTORY-GAMMA-CONSTRUCTED
experiment  P13B-POINT-FREE-EXPERIMENT-ACTION-CONSTRUCTED
record      P13B-GRAMMAR-STABLE-RECORD-CONSTRUCTED
division    P13B-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
nondivision P13B-NATIVE-INDIVISIBLE-CUT-CONSTRUCTED
size        P13B-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13B-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13B-ACTUALIZATION-UNCONSTRUCTED
```

These coordinates are `GREEN-UNREVIEWED`, not citable or terminal.

## 13. Permanent nonclaims

This construction does not establish:

- an actual history or actual happening;
- chronology, causal order, or a signal cone;
- spatial adjacency between distinct atoms;
- dimension, signature, topology, or manifoldlikeness;
- volume, duration, proper time, or physical scale;
- a metric, connection, curvature, stress tensor, energy, or entropy;
- gravity, Einstein dynamics, GR, QFT, particles, or phenomenology; or
- uniqueness or derivation of the primitive law.

Those questions require later result-neutral investigations. The present law
may fail them.
