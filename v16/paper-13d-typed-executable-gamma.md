# A typed executable relational Gamma

## Abstract

A probability distribution over completed histories does not determine what
an intervention means, and a list of transformations does not define a
dynamical category. We construct one exact candidate law

$$
\mathbf\Gamma_D:
\mathsf{Experiment}_D\longrightarrow
\operatorname{Prob}(\mathsf{PhysicalHistory}_D)
$$

whose intervention slots, boundary species, process arrows, independent
tensor, fusion, readers, future operations, and eraser are all typed before
evaluation. The same recursive evaluator supplies every admitted law value.
The observational law is one value of this map, not the source from which the
other values are inferred.

The candidate contains an unqueried primitive transition with endpoint
kernel $C$ and a native queried interface with first-leg kernel $B$. No
positive stochastic continuation through that declared native carrier
reproduces the unqueried law. Queried processes instead have positive $B$
continuations and endpoint law $B^2$. A typed stable-future subcategory
preserves record sectors at arbitrary finite depth, while a distinct
executable eraser destroys future-boundary readability. Stable records and
complete probabilistic divisions remain independent.

The construction is covariant over arbitrary finite occurrence sets. Its
physical quotient is fixed before a reader is chosen, its independent tensor
is internal to the law's domain, and its physical fusion is a separate
simultaneous operation. It gives exact relational response in both directions
but derives no actual outcome, chronology, dimension, geometry, metric,
curvature, gravity, continuum physics, or quantum field theory.

## 1. Status and nonselection

The entire packet below is one declared mathematical candidate. Its rational
constants, seed law, syntax, types, and evaluator are fixed together. They
are not selected by a desired outcome, dimension, geometric fit, or later
test. Two candidates are different laws if they differ on any admitted
experiment, even if their observational distributions agree.

Operational type phases used to validate interventions are not physical
times. Execution paths are not assumed to form a causal order. Cardinality is
not volume. A record is not automatically a division. A possible history is
not an actual history.

## 2. Exact numerical primitive

Let $\mathbb B=\{0,1\}$ with addition $\oplus$ modulo two, and let
$[25]=\{0,1,\ldots,24\}$. Fix

$$
R=
\begin{pmatrix}
3/5&-4/5\\
4/5&3/5
\end{pmatrix},
$$

$$
B=|R|^2=
\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix},
\qquad
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

Define deterministic maps

$$
\beta(a,u)=
\begin{cases}
a,&u<9,\\
1-a,&u\ge 9,
\end{cases}
$$

and, writing $s=25u_1+u_2$,

$$
\kappa(a,u_1,u_2)=
\begin{cases}
a,&s<49,\\
1-a,&s\ge49.
\end{cases}
$$

Uniform $u,u_1,u_2\in[25]$ give $B$ and $C$ exactly. These maps are
primitive clauses of the candidate, not fitted transition tables.

## 3. Finite-set species and presentation groupoid

### 3.1 Occurrences and local port frames

An occurrence carrier is an arbitrary finite set $I$. Each occurrence has a
two-port frame $\{X,Y\}$. A presentation morphism

$$
g=(\sigma,\tau):I\longrightarrow J
$$

consists of a bijection $\sigma:I\to J$ and a function
$\tau:I\to C_2$ specifying whether the local $X/Y$ ports are exchanged. These
morphisms form the finite-set action groupoid $\mathcal G$ under the evident
semidirect composition.

The local swap exchanges

$$
(x,y),\ (x',y'),\ (z_X,z_Y),\ (u_X,u_Y),\
(\eta_X,\eta_Y),\ (X,Y),
$$

and fixes scalar relation, process, record, and context fields. The bijection
transports occurrence coordinates and unordered-pair endpoints. Every
constructor below is functorial for this action.

### 3.2 Relational packets and bonds

For $i\in I$, a relational packet is

$$
a_i=(x_i,y_i,\epsilon_i,x'_i,y'_i,e'_i,
z_{Xi},z_{Yi},u_{Xi},u_{Yi},d_i)\in\mathbb B^{11},
\qquad d_i=e'_i.
$$

Let $\binom I2$ be the finite set of unordered two-element subsets of $I$.
A bond field is a function $L:\binom I2\to\mathbb B$.

### 3.3 Atomic boundary species

The exact atomic boundary sets are

$$
B_0(I)=
\mathbb B^{\{q_0,h,c,e^0\}\times I},
$$

$$
B_1^0(I)=
\left\{(m,h,a)\right\}_{i\in I},
$$

$$
B_1^r(I)=
\left\{(m,r,h,a)\right\}_{i\in I}:r_i=m_i,
$$

$$
B_2^0(I)=
\left\{(q_2,h,t,a)_{i\in I},L:t_i=h_i\right\},
$$

$$
B_2^r(I)=
\left\{(q_2,h,t,a,r)_{i\in I},L:t_i=h_i\right\}.
$$

Unlike the defective predecessor, the equality $t=h$ is an invariant of a
single boundary object because both fields are carried by that object.

The stable post-endpoint boundary is

$$
B_3^r(I)=\left\{(q^+,h,t^+,a,r)_{i\in I},L\right\},
$$

with no equation between $t^+$ and $h$. The erased post-endpoint boundary is

$$
B_3^e(I)=\left\{(q^+,h,t^+,a)_{i\in I},L\right\}.
$$

Thus changing a later readout never mutates a field while pretending to
remain inside a type whose invariant it violates.

### 3.4 Tensor boundary objects

For a finite component set $A$ and a family of atomic boundary objects
$S_\alpha(I_\alpha)$, define the formal independent boundary

$$
\boxtimes_{\alpha\in A}S_\alpha(I_\alpha)
$$

to be their Cartesian product with the component partition retained in the
source type. It has no cross-component bond field. The empty family is the
unit $\mathbbm1$. Component bijections, component permutations, and local
presentation maps give its exact groupoid action.

Private seeds, control words, reader names, loop indices, serialization order,
and history identifiers occur in none of these boundary sets.

## 4. The stage-typed control category

### 4.1 Override monoids

Let

$$
\mathcal A_0(I)=I\times\{X,Y,E\},
\qquad
\mathcal A_1(I)=I\times\{E'\}.
$$

For $k=0,1$, let $M_k(I)$ be the set of finite partial functions
$\mathcal A_k(I)\rightharpoonup\mathbb B$. If $p$ is executed before $q$,
their right-biased override is

$$
(p\triangleright q)(s)=
\begin{cases}
q(s),&s\in\operatorname{dom}q,\\
p(s),&s\in\operatorname{dom}p\setminus\operatorname{dom}q.
\end{cases}
$$

with the empty map as identity. Override is associative.

### 4.2 Exact hom-sets

Define $\mathsf{Ctrl}(I)$ with objects $\mathsf S,\mathsf M,\mathsf C$ and

$$
\operatorname{Hom}(\mathsf S,\mathsf S)=M_0,
\qquad
\operatorname{Hom}(\mathsf M,\mathsf M)=M_1,
\qquad
\operatorname{Hom}(\mathsf C,\mathsf C)=\{1\},
$$

$$
\operatorname{Hom}(\mathsf S,\mathsf M)=M_0\times M_1,
\qquad
\operatorname{Hom}(\mathsf S,\mathsf C)=M_0\times M_1,
\qquad
\operatorname{Hom}(\mathsf M,\mathsf C)=M_1,
$$

and every other hom-set empty. The two copies of $M_0\times M_1$ are typed
by their codomains even though their underlying sets agree.

Composition is override in the component on which the adjacent arrow acts.
Writing the type as a subscript when needed, the complete list apart from
identities at $\mathsf C$ is

$$
p_0;q_0=p_0\triangleright q_0,
\qquad p_1;q_1=p_1\triangleright q_1,
$$

$$
p_0;(q_0,q_1)_{\mathsf S\mathsf M}
=(p_0\triangleright q_0,q_1)_{\mathsf S\mathsf M},
$$

$$
p_0;(q_0,q_1)_{\mathsf S\mathsf C}
=(p_0\triangleright q_0,q_1)_{\mathsf S\mathsf C},
$$

$$
(p_0,p_1)_{\mathsf S\mathsf M};q_1
=(p_0,p_1\triangleright q_1)_{\mathsf S\mathsf M},
$$

$$
(p_0,p_1)_{\mathsf S\mathsf M};q_{\mathsf M\mathsf C}
=(p_0,p_1\triangleright q_{\mathsf M\mathsf C})_{\mathsf S\mathsf C},
$$

and

$$
p_1;q_{\mathsf M\mathsf C}=p_1\triangleright q_{\mathsf M\mathsf C}.
$$

Arrows already ending at $\mathsf C$ compose only with its identity. These
are all possible compositions. Associativity follows componentwise from
associativity of $\triangleright$.

The empty elements

$$
\alpha=(\varnothing,\varnothing)_{\mathsf S\mathsf M},
\qquad
\omega=\varnothing_{\mathsf M\mathsf C}
$$

are the unique write-free stage transitions. Hence a program word has the
typed form

$$
J_0;\alpha;J_1;\omega
$$

and normalizes to its source-to-$\mathsf C$ pair $(J_0,J_1)$.

A complete control program is the unique normal form

$$
J=(J_0,J_1)\in M_0(I)\times M_1(I).
$$

The generator $\operatorname{set}(E',a)$ is an endomorphism of $\mathsf M$,
whereas $\operatorname{set}(X,b)$ is an endomorphism of $\mathsf S$.
Consequently

$$
\operatorname{set}(E',a);\operatorname{set}(X,b)
$$

is not a morphism: the first target is $\mathsf M$ and the second source is
$\mathsf S$. This is a type mismatch, not an after-the-fact word filter.

The symbols $\mathsf S,\mathsf M,\mathsf C$ describe validation phases of an
intervention program. They are absent from physical histories and imply no
chronology.

## 5. Exact execution category

### 5.1 Atomic generators

For every finite $I$ and every complete program $J$, the atomic process
generators are

$$
U_J:B_0(I)\to B_2^0(I),
$$

$$
Q_J^0:B_0(I)\to B_1^0(I),
\qquad
D:B_1^0(I)\to B_2^0(I),
$$

$$
Q_J^r:B_0(I)\to B_1^r(I),
\qquad
R_c:B_1^r(I)\to B_2^r(I).
$$

The program is part of a source arrow, not a boundary field. The standalone
continuations $D$ and $R_c$ accept complete $B_1$ values and have no control
program input. In particular,

$$
U_J\ne D\circ Q_J^0,
\qquad
U_J\ne R_c\circ Q_J^r.
$$

### 5.2 Structural and post-endpoint generators

The category also contains:

- identities at every boundary object;
- tensors of any finite family of arrows;
- simultaneous fusion arrows $\Phi_s^{\{I_\alpha\}}$ of Section 10;
- the stable entry $\iota:B_2^r(I)\to B_3^r(I)$;
- every stable $B_3^r(I)$ endomorphism of Section 11; and
- the eraser $E_r:B_2^r(I)\to B_3^e(I)$.

Define $\mathsf{Exec}_D$ to be the free symmetric monoidal category on these
typed generators, quotiented only by the symmetric-monoidal axioms, the
finite-set covariance equations, and the explicitly stated n-ary permutation
invariance of a single fusion generator. Its hom-sets are therefore exactly
the equivalence classes of finite well-typed syntax trees. Composition is
concatenation at matching boundary objects. An unmatched source and target,
an unavailable control stage, an unlisted address, or a nonexistent boundary
sort is not a morphism.

Free categorical syntax makes identities and associativity exact. It also
keeps six operations distinct: categorical composition, probabilistic
conditioning, reader pushforward, independent tensor, physical fusion, and
factorization through a division.

### 5.3 Closed reader-free experiments

For an arrow $f:S\to T$, a reader-free presented experiment is

$$
\widehat e=(\mathcal H_S,f,K,M_{\rm int},M_{\rm land}),
$$

where $\mathcal H_S$ is its presented typed source frame, $K$ is either a
nonempty cylinder on $B_0(I)$, one exact value of a later atomic source
boundary, or the component-indexed tuple of such arguments for a tensor
source,
and $M_{\rm int}$ is exactly the intervention-address set supporting every
nonempty control entry in $f$. The optional $M_{\rm land}$ is a finite set of
nondisturbing physical probe landmarks chosen from the exact target probe
addresses. It orients an apparatus but does not choose a reader function. If
$S\ne B_0(I)$, source controls are unavailable and $M_{\rm int}$ is empty.

Closing an experiment with a reader is a separate operation performed only
after the physical outcome fiber has been constructed in Section 9.

## 6. Exact seed law and relational evaluator

### 6.1 Seeds

For fixed $I$, the source variables $q_{0i},h_i,c_i,e_i^0$ are independent
fair bits. The private occurrence seeds are

$$
\eta_{Xi},\eta_{Yi}\in\mathbb B,
\qquad
u_{1i},u_{2i}\in[25],
$$

with

$$
P(\eta_J=0)=\frac{16}{25},
\qquad
P(\eta_J=1)=\frac9{25},
$$

and uniform $u_1,u_2$. Each unordered pair has an independent uniform seed
$v_{ij}\in[25]$. All factors are independent. A source context is a nonempty
cylinder on the public $B_0$ variables; inconsistent cylinders are refused.

For a standalone continuation from $B_1$, only fresh $u_2$ and endpoint-pair
seeds are drawn. Deterministic future maps and identities draw no seed.
Fusion draws only the fresh cross-pair seeds named in Section 10.

### 6.2 Relational mechanism

Given a complete source value and $J=(J_0,J_1)$, evaluate once for each
$i\in I$:

$$
x_i=
\begin{cases}
J_0(i,X),&(i,X)\in\operatorname{dom}J_0,\\
c_i\oplus\eta_{Xi},&\text{otherwise},
\end{cases}
$$

with the analogous formula for $y_i$, and

$$
\epsilon_i=
\begin{cases}
J_0(i,E),&(i,E)\in\operatorname{dom}J_0,\\
e_i^0,&\text{otherwise}.
\end{cases}
$$

Then

$$
x'_i=x_i\oplus\epsilon_i,
\qquad
y'_i=y_i\oplus\epsilon_i,
$$

$$
\widehat e'_i=\epsilon_i\oplus x_i\oplus y_i,
$$

$$
e'_i=
\begin{cases}
J_1(i,E'),&(i,E')\in\operatorname{dom}J_1,\\
\widehat e'_i,&\text{otherwise},
\end{cases}
$$

and

$$
z_{Xi}=x_i\oplus e'_i,
\qquad z_{Yi}=y_i\oplus e'_i,
$$

$$
u_{Xi}=x_i\oplus c_i,
\qquad u_{Yi}=y_i\oplus c_i,
\qquad d_i=e'_i.
$$

This is the only mechanism evaluator. Observational refactorizations never
enter it.

### 6.3 Endpoint bonds

Whenever an atomic or fused target has an endpoint bond field, set for every
new unordered pair

$$
\ell_{ij}=1
\quad\Longleftrightarrow\quad
v_{ij}<
\begin{cases}
16,&d_i\ne d_j,\\
9,&d_i=d_j.
\end{cases}
$$

Existing internal bonds carried by a fusion source are not redrawn.

## 7. Histories and the one global evaluator

### 7.1 Trace types

For a typed arrow $f:S\to T$ and source value $z\in S$, define
$\mathsf{Hist}(f;z)$ recursively from the syntax of $f$:

- an identity history is the one-entry trace $(z)$;
- a generator history is the ordered pair of its physical source and target
  boundary values;
- a composite history glues the equal target/source boundary and retains the
  complete resulting trace;
- a tensor history is the finite component-indexed family of its factor
  histories; and
- a fusion history retains its tensor source value and fused target value.

The trace records the boundary sorts actually traversed, all their physical
fields, bonds, and records. It records no seed, control normal form, reader,
probability, presentation enumeration, cache, or execution-loop index. In
particular, a $U_J$ history contains no fictitious $B_1$ value.

### 7.2 Atomic process kernels

For $U_J$ at a complete source value, construct the relational packet by
Section 6 and set

$$
q_{2i}=\kappa(q_{0i},u_{1i},u_{2i}),
\qquad h_i^\mathrm{out}=h_i,
\qquad t_i=h_i,
$$

then generate all endpoint bonds.

For $Q_J^0$ set

$$
m_i=\beta(q_{0i},u_{1i})
$$

and return $(m,h,a)$. For $Q_J^r$ use the same equation and additionally set
$r_i=m_i$. For a standalone $D$ at a supplied value of $B_1^0$, draw fresh
$u_2$ and pair seeds, set

$$
q_{2i}=\beta(m_i,u_{2i}),
\qquad t_i=h_i,
$$

copy $a$, and generate the endpoint bonds. The standalone $R_c$ uses the
same continuation and carries $r$ unchanged.

The process kernel of a composite such as $D\circ Q_J^0$ is not a second
table. It is the convolution of the two independently defined generator
kernels. Hence its endpoint kernel is $B^2$. The primitive $U_J$ remains a
parallel arrow with endpoint kernel $C$.

### 7.3 Structural recursion

For every generator, the clauses of Sections 6, 7, 10, and 11 define a finite
normalized kernel on its exact target boundary. Extend uniquely to every
$f\in\mathsf{Exec}_D$ by

$$
\mathbf\Gamma_{1_S}(z)=\delta_{(z)},
$$

For a complete trace with unique shared boundary value $y$,

$$
\mathbf\Gamma_{g\circ f}(z)(H_f\star_y H_g)
=\mathbf\Gamma_f(z)(H_f)\mathbf\Gamma_g(y)(H_g).
$$

Marginalizing the retained intermediate trace gives the usual finite sum over
$y$. On tensors set

$$
\mathbf\Gamma_{\boxtimes_\alpha f_\alpha}
=\bigotimes_\alpha\mathbf\Gamma_{f_\alpha}.
$$

This is one evaluator on typed syntax. It immediately gives

$$
\mathbf\Gamma_{g\circ f}
=\mathbf\Gamma_g\star\mathbf\Gamma_f
$$

for every composable pair, including histories rather than merely a selected
marginal. No chain-rule refactorization defines a new experiment.

For a source cylinder $K$, average this kernel over the fixed conditional
source law. For a later-boundary source, $K$ is one exact value and no past is
reconstructed. We denote the resulting presented law by
$\widetilde{\mathbf\Gamma}(\widehat e)$.

### Theorem 1 — totality, normalization, and refusal

Every well-typed finite experiment has exactly one normalized presented law.
Every ill-typed word is refused before probability evaluation.

#### Proof

Atomic seed spaces are finite products of normalized factors. Deterministic
pushforward, finite kernel convolution, and finite tensor product preserve
normalization. The free typed syntax has a unique structural recursion modulo
the category and symmetric-monoidal equations; the generator kernels respect
those equations by construction. Empty hom-sets are never passed to the
evaluator. ∎

## 8. Exact addresses and marks

For an atomic source $B_0(I)$ define

$$
\mathsf{InterventionAddr}(B_0(I))
=\mathcal A_0(I)\sqcup\mathcal A_1(I).
$$

For every other atomic source boundary the intervention-address set is empty.
For a general execution diagram $f$, let $V_0(f)$ be its finite set of
generator vertices of type $U_J,Q_J^0,$ or $Q_J^r$. This is the vertex set of
the typed string diagram, not a serialization index. Define

$$
\mathsf{InterventionAddr}(f)
=\bigsqcup_{v\in V_0(f)}\{v\}\times
\mathsf{InterventionAddr}(B_0(I_v)).
$$

Tensoring disjointly unions these vertex sets, and categorical composition
glues diagrams without renumbering them. A program entry is legal only at its
matching vertex and boundary address, and $M_{\rm int}$ must equal the set of
addresses on which the diagram's programs are nonempty. An address cannot be
supplied as an arbitrary string, loop counter, or integer.

For every target sort define $\mathsf{ProbeAddr}$ as the tagged disjoint union
of:

- each legal occurrence-field coordinate $(i,F)$ carried by that sort;
- each relational subfield $(i,a,F)$ it carries;
- each unordered bond coordinate $\{i,j\}$ it carries; and
- for a tensor, the component-tagged probe addresses of all factors.

The groupoid action sends $(i,F)$ to $(\sigma(i),\tau_iF)$, transports all
relational subfields by the rules in Section 3, and sends
$\{i,j\}$ to $\{\sigma(i),\sigma(j)\}$. These constructors supply every
address used below; there is no “additional probe” clause.

$M_{\rm land}\subseteq\mathsf{ProbeAddr}(T)$ is part of the reader-free
experiment and is transported by the same action. It may orient a later
reader without letting the reader itself change the physical quotient.

## 9. Reader-independent physical quotient

### 9.1 Physical experiment and outcome cells

The presentation groupoid acts diagonally on the reader-free experiment and
its histories. For a presented $\widehat e$, let

$$
\mathcal G_{\widehat e}
=\{g:g\widehat e=\widehat e\}
$$

be its stabilizer. Crucially, no diagnostic reader occurs in this definition.
A physical history cell over $[\widehat e]$ is the stabilizer orbit

$$
[H]_{\widehat e}=\mathcal G_{\widehat e}H.
$$

Define its mass by pushforward,

$$
\mathbf\Gamma_D([\widehat e])([H]_{\widehat e})
=\sum_{H'\in[H]_{\widehat e}}
\widetilde{\mathbf\Gamma}(\widehat e)(H').
$$

The stabilizer orbits partition the full presented history fiber, so their
masses sum to one. If the representative changes to $g\widehat e$, the cell
and its mass transport to $[gH]_{g\widehat e}$. This is the diagonal
experiment--history quotient; quotienting histories alone would erase the
physical relation between a marked operation and its result.

Representative mass is not physical mass. For any nontrivial orbit it omits
the other labeled histories and generally fails normalization. Automorphism
fixed points are retained with their actual orbit multiplicity.

### 9.2 Readers as derived equivariant observables

A reader on $[\widehat e]$ is a family of maps

$$
R_{g\widehat e}:\Omega_{[g\widehat e]}\longrightarrow O_{gR}
$$

satisfying

$$
R_{g\widehat e}([gH])=gR_{\widehat e}([H]).
$$

Its output law is the pushforward $R_*\mathbf\Gamma_D([\widehat e])$. The
complete reader is the identity map on the already-formed physical outcome
fiber. If a probe address is fixed pointwise by the experiment stabilizer—for
example because it is a singleton landmark in $M_{\rm land}$—its field value
defines an oriented reader. For a non-fixed address $p$, the admissible reader
returns

$$
R_{[p]}([H])=
\left[(q,\operatorname{value}_H(q))_{q\in\mathcal G_{\widehat e}p}
\right]_{\mathcal G_{\widehat e}},
$$

the stabilizer orbit of the complete addressed profile, rather than selecting
one representative. Replacing $H$ by a stabilizer translate only reindexes
this same orbit. Boolean combinations and finite tuples of these exact
constructors give the complete finite diagnostic catalogue. A naked
presentation coordinate is not a reader.

Changing only $R$ changes neither $\mathcal G_{\widehat e}$ nor the physical
history cells nor their masses. It may change only the pushforward partition.
Thus a coarse reader can hide response but cannot alter the physical law.

### Theorem 2 — point-free executable descent

For every presentation morphism $g$,

$$
\widetilde{\mathbf\Gamma}(g\widehat e)
=g_*\widetilde{\mathbf\Gamma}(\widehat e),
$$

and the quotient kernel and every equivariant reader law are independent of
the representative.

#### Proof

The source and private seed laws are exchangeable. Local port swaps exchange
the corresponding noise, control, relational, address, and reader
coordinates. Occurrence bijections transport all occurrence and unordered
pair factors. Every atomic kernel is therefore equivariant. Structural
recursion preserves equivariance under composition and tensor. The orbit
pushforward then gives the claimed representative-independent kernel. ∎

## 10. Independent tensor and simultaneous physical fusion

### 10.1 Independent tensor

The tensor object and arrow constructors of Sections 3 and 5 are part of the
domain of $\mathbf\Gamma_D$. For reader-free experiments
$\widehat e_\alpha$, their independent tensor retains component tags in its
source type, has no cross-component pair field, and obeys exactly

$$
\mathbf\Gamma_D\!\left(\boxtimes_\alpha\widehat e_\alpha\right)
=\bigotimes_\alpha\mathbf\Gamma_D(\widehat e_\alpha).
$$

The tensor reader is the product reader and the empty tensor is the
deterministic unit. Component permutation is the symmetric braiding. Tensor
is not a claim about a larger interacting system.

### 10.2 Fusion

For a finite component family all having the same atomic boundary sort $s$,
let $I=\bigsqcup_\alpha I_\alpha$. The single n-ary generator

$$
\Phi_s^{\{I_\alpha\}}:
\boxtimes_\alpha B_s(I_\alpha)\longrightarrow B_s(I)
$$

forgets the component partition at its target and unions every occurrence
field. At a sort without bonds this is deterministic. At a sort with bonds it
carries all existing within-component bonds and draws one fresh seed for each
cross-component unordered pair, using Section 6.3. No within-component bond
is redrawn.

The generator is indexed by the finite *family*, not by an ordered list. A
permutation of components gives the same kernel after the symmetric braiding.
Its evaluator draws the entire set of cross-pair seeds simultaneously, so no
fold order or loop index is a physical input.

A deliberately staged sequence of two physical fusion arrows is a different
execution trace containing an extra traversed boundary. It is not silently
identified with one simultaneous fusion. Auxiliary order used to construct a
single n-ary seed product has no observable effect.

### Theorem 3 — tensor/fusion separation

Independent tensor and physical fusion are both total, covariant operations
in the law's domain and are not equal when at least two nonempty components
admit a cross pair.

#### Proof

The tensor target has a retained component partition and no cross bond. The
fusion target lacks that partition and has a fresh, positive cross-bond law.
Their boundary types and probability kernels therefore differ. Product
normalization follows factorwise; fusion normalization follows from the
independent cross-pair seeds. Component permutation only reindexes the same
unordered seed set. ∎

## 11. Typed stable futures and executable erasure

### 11.1 Stable entry and endomorphisms

The entry map

$$
\iota:B_2^r(I)\longrightarrow B_3^r(I)
$$

is

$$
(q_2,h,t,a,r,L)\longmapsto(q^+=q_2,h,t^+=t,a,r,L).
$$

For arbitrary subsets $A\subseteq I$, define exact $B_3^r(I)$
endomorphisms:

- $F_q^A$ toggles $q_i^+$ precisely for $i\in A$;
- $F_t^A$ toggles the later field $t_i^+$ precisely for $i\in A$;
- $F_{XY}^A$ exchanges every $X/Y$-typed entry of $a_i$ for $i\in A$ and
  leaves the scalar color $d_i=e'_i$, bonds, and records unchanged; and
- $F_r^A$ toggles $r_i$ precisely for $i\in A$ and transports the record
  labels by the same bitwise translation.

Every map is a bijection of the declared target set. In particular $F_t^A$
does not act on $B_2^r$ and cannot violate $t=h$; it changes the separately
typed later field $t^+$.

Let $W(I)$ be the submonoid of all bijections generated by these maps. Define
$\mathsf{Fut}_{\rm stable}(I)$ to have objects
$B_1^r(I),B_2^r(I),B_3^r(I)$, identities, the exact record-carrying kernel
$R_c:B_1^r(I)\to B_2^r(I)$, the entry $\iota$, endomorphism monoid $W(I)$ at
$B_3^r(I)$, and all typed composites among these arrows, namely
$w\circ\iota$, $\iota\circ R_c$, and $w\circ\iota\circ R_c$ where defined.
There are no other arrows. This is a closed category, and arbitrary finite
words are already included.

The global $\mathsf{Fut}_{\rm stable}$ is the smallest symmetric-monoidal
subcategory of $\mathsf{Exec}_D$ containing these per-$I$ arrows, the
braidings, and the record-carrying fusion generators at sorts
$B_1^r,B_2^r,B_3^r$. Tensor retains the component record tuple; fusion carries
it to the canonically identified word on $\bigsqcup I_\alpha$ and draws only
record-independent cross-pair seeds. No eraser generator is included.

### 11.2 Projector transport

For a record word $\rho\in\mathbb B^I$, let $P_\rho^S$ be the diagonal
projector onto boundary values with record $\rho$ in the free real vector
space on $S$. Each stable generator has a bijection
$\sigma_F:\mathbb B^I\to\mathbb B^I$: identity for
$R_c,\iota,F_q,F_t,F_{XY}$ and bitwise translation for $F_r$. Tensor uses the
product label bijection, and fusion uses the canonical disjoint-union label
bijection. Although
$R_c$ is stochastic on the other fields, it carries $r$ deterministically.
Fusion's fresh bond law is independent of $r$. For the linear map or Markov
kernel associated with each generator, directly,

$$
P_{\sigma_F(\rho)}^T F=F P_\rho^S.
$$

For composable stable arrows,

$$
\sigma_{G\circ F}=\sigma_G\circ\sigma_F.
$$

Induction therefore proves the same equation for every finite licensed word,
not merely for tested continuation depths.

### 11.3 Eraser

The executable eraser is the deterministic arrow

$$
E_r:B_2^r(I)\longrightarrow B_3^e(I),
$$

$$
E_r(q_2,h,t,a,r,L)=(q^+=q_2,h,t^+=t,a,L).
$$

It is a generator of $\mathsf{Exec}_D$ and has a complete target reader, but
it is not an arrow of $\mathsf{Fut}_{\rm stable}$. If two legal source values
differ only in $r$, their $B_3^e$ outputs are identical. Thus their record
sectors are indistinguishable to every future-boundary reader after erasure.
The complete past trace still contains the supplied $B_2^r$ value; erasing a
future record is not rewriting history.

For $I=\{i\}$, fix any admitted $h,a,q_2$. The two legal values with
$r_i=0$ and $r_i=1$ and all other fields equal both have positive probability
under $R_c\circ Q_J^r$, because every entry of both $B$ factors is positive.
They are mapped to the same erased target. The control therefore acts on
reachable sectors, not only on a zero-probability corner of the boundary set.

### Theorem 4 — grammar-relative stable record

Every record sector written at $B_1^r(I)$, and hence every carried sector at
$B_2^r(I)$, remains exactly recoverable after every finite word in
$\mathsf{Fut}_{\rm stable}(I)$. The executable arrow $E_r$
is an exact control showing that the result is relative to that declared
subcategory and is not absolute permanence.

#### Proof

The generator equations and label-composition equation above give stability
by induction. Both record sectors occur with positive probability because all
entries of $B$ are positive. The eraser identifies an explicit cross-sector
pair at its target and so cannot admit a bijective record-label transport. ∎

## 12. Native carrier and cut-relative nondivision

Fix one occurrence and one source value $q_0=a$. For either query arrow,

$$
P(m=j\mid q_0=a)=B_{ja}.
$$

For the primitive unqueried arrow,

$$
P(q_2=b\mid q_0=a,U_J)=C_{ba}.
$$

These equations remain true after conditioning on any common fixed exterior
source fields and relational packet values because the transition seeds are
independent of that exterior.

The declared native carrier is the complete $B_1^0$ or $B_1^r$ boundary
value of Section 3. It contains $m,h,a$ and, in the recorded case, $r=m$. It
contains no $q_0$, private seed, control phase, prior history identifier, or
cache. A continuation may use the complete declared boundary but may not
recover $q_0$ from an unlisted channel.

If the primitive unqueried endpoint kernel factored positively through this
interface, some stochastic matrix $K$ would satisfy

$$
C=KB.
$$

Since $B$ is invertible, the only candidate is

$$
K=CB^{-1}
=\frac1{175}
\begin{pmatrix}
351&-176\\
-176&351
\end{pmatrix}.
$$

It has negative entries. For every nonempty finite $I$, conditioning on the
complete common relational exterior gives the unique candidate

$$
K_I=(CB^{-1})^{\otimes I}.
$$

Choose one negative off-diagonal factor and positive diagonal factors on all
other occurrences; the resulting entry is negative. Thus no positive
normalized continuation exists at any nonempty size.

If the carrier is enlarged to $(m,q_0)$, the continuation can simply use the
retained $q_0$ and a positive restart is immediate. Identity factorizations
$C=CI=IC$ and the empty process are also nonkills. They are different cuts,
not repairs of the declared carrier.

### Theorem 5 — native $B_1$ nondivision

For every nonempty finite occurrence set, the primitive unqueried process is
not stochastically divisible through the declared native $B_1$ carrier. This
is a source-independent, cut-relative statement and not a claim that the
underlying configuration is incomplete. ∎

## 13. Complete divisions and their independence from records

### 13.1 Definition

A typed frontier $F$ in an execution is a **complete division** when both
conditions hold:

1. **future sufficiency:** any two positive-mass past traces with the same
   complete $F$ value give the same law for every composable licensed future
   and every derived reader; and
2. **cut equality:** for every complete source value and context, the direct
   trace law equals the exact sum of the prefix and continuation trace laws
   over all complete $F$ values.

The argument at $F$ includes every boundary field, relation packet, bond,
record, and declared native context carried by its type. No history label,
phase, clock, or cache may be added after the test. A stable record field by
itself is not presumed sufficient.

### 13.2 Queried divisions

For $D\circ Q_J^0$, the complete intermediate value is $(m,h,a)$. Its joint
one-occurrence process kernel is

$$
P(m,q_2\mid q_0)=B_{mq_0}B_{q_2m}.
$$

For $R_c\circ Q_J^r$, the complete value is $(m,r=m,h,a)$ and the same
positive continuation carries the record. Conditional on either complete
frontier, the remaining $u_2$ and every future pair seed are fresh and
independent. Every later composed law is then determined by structural
recursion from that boundary value.

Expanding the primitive seed product directly gives the same sum as the
categorical convolution on every complete source, relational packet,
intermediate value, endpoint value, and bond field. Thus cut equality is not
inferred from the displayed two-state marginal.

The restricted record-only frontier keeps $r$ but omits $h$ and $a$. Two
histories may share $r$ while having opposite $h$, hence opposite mandatory
$t=h$ at the endpoint. They have different future profiles and this frontier
is not complete, even though its record is stable.

### Theorem 6 — record/division product square

| stable record | complete division | exact case |
|---|---|---|
| yes | yes | complete $B_1^r$ in $R_c\circ Q_J^r$ |
| yes | no | record-only restriction of that frontier |
| no | yes | complete $B_1^0$ in $D\circ Q_J^0$ |
| no | no | primitive $U_J$ tested through native $B_1$ |

All four cells are consequences of one law on distinct typed experiments and
frontiers. A happening record and a restartable probabilistic snapshot are
therefore mathematically independent notions. ∎

## 14. All-size covariance and deletion

For each finite $I$, use the product seed law of Section 6. On isomorphism
classes of unmarked finite experiments, define the grand observational
cardinality law

$$
P(|I|=n)=2^{-(n+1)},\qquad n\ge0.
$$

At size $n$ the grand observational experiment is the empty-program primitive
$U_\varnothing$ with tautological source context, no marks, and the physical
history quotient of Section 9.

No canonical order on $I$ is used. For $i\in I$, deletion removes that
occurrence from every traversed boundary, removes its incident bonds, and
restricts every seed, program, and intervention address to $I\setminus\{i\}$.
For an unmarked experiment, choose the deleted occurrence uniformly.

### Theorem 7 — natural deletion and extension

Deleting a uniformly selected occurrence from the size-$n$ unmarked law gives
the size-$(n-1)$ law. Deletion commutes with presentation transport and with
the evaluator. Adding any finite set of fresh occurrences is independent of
the auxiliary order in which their iid occurrence and unordered-pair seeds
are exposed.

#### Proof

Restriction of an independent product removes precisely the factors incident
on the deleted occurrence. All retained factors have their original law.
Exchangeability removes the presentation choice. The evaluator is local on
occurrences except for symmetric unordered-pair bond factors, which restrict
exactly. For an extension, both auxiliary orders expose the same finite set
of occurrence seeds and unordered-pair seeds; finite product multiplication
commutes. ∎

The theorem is compatible with tensor because componentwise restriction
preserves product factors. It is compatible with a single n-ary fusion
because restriction of the union and its cross-pair seed set equals fusion of
the restricted family after empty components are removed. These are laws on
arbitrary finite sets, not a simulation in dormant fixed memory.

Each realized history is finite. Cardinality and extension order are not
chronology, volume, or a clock.

## 15. Point-free signed response

### 15.1 Contrast objects

Fix a path beginning at $B_0(I)$, a source context $K$, a base program $J$
not writing address $A$, a common mark skeleton containing $A$, and two
distinct alternatives $a,b\in\mathbb B$. Let $\widehat e_a$ and
$\widehat e_b$ be the two reader-free experiments differing only by
$J(A)=a$ versus $J(A)=b$.

The **contrast object** is the ordered aligned pair

$$
\chi=(\widehat e_a,\widehat e_b),
$$

with stabilizer

$$
\mathcal G_\chi
=\mathcal G_{\widehat e_a}\cap\mathcal G_{\widehat e_b}.
$$

This definition remains valid even when alternative values change accidental
symmetries of one experiment. Push each presented law onto the common
$\mathcal G_\chi$-orbits of the shared typed history space, obtaining
$\mu_a^\chi$ and $\mu_b^\chi$. For every complete comparison cell $C$, define

$$
\Delta_\chi(C)=\mu_a^\chi(C)-\mu_b^\chi(C).
$$

The base physical quotients of $\widehat e_a$ and $\widehat e_b$ remain
unchanged; $\chi$ is a separately typed comparison object and not a reader.
Equivalently, a complete comparison cell is the diagonal groupoid orbit of
$(\widehat e_a,\widehat e_b,H)$; the intersection stabilizer is only its
description in one chosen common presentation.
Its complete contrast reader is the identity on the common comparison fiber.
For every equivariant diagnostic reader $R$ and reader output $o$, define

$$
\Delta_{A;a,b}^{f,K,R}(o)
=R_*\mu_a^\chi(o)-R_*\mu_b^\chi(o).
$$

The complete response tensor is the family of these signed coordinates over
every legal address, alternative pair, context, execution, equivariant reader,
and reader output. The complete reader is retained alongside every coarse
reader. The physical response object is the diagonal groupoid orbit of the
whole contrast, not a naked slot name.

### 15.2 Exact controls

The following consequences use the single evaluator of Section 6.

1. **Matter to relation.** At fixed $Y,E$ and with no $E'$ override, setting
   $X$ from zero to one flips $e'=\epsilon\oplus x\oplus y$. The complete
   $E'$ reader has total-variation response one. Each incident bond
   probability changes by signed magnitude $16/25-9/25=7/25$, with sign fixed
   by the other endpoint color.
2. **Relation to matter.** At fixed $X,Y$, changing $E$ flips the complete
   pair $(x',y')$, giving total-variation response one.
3. **Mediation.** Without an $E'$ override,
   $z_Y=y\oplus e'=\epsilon\oplus x$, so $X$ has total response on $z_Y$.
   Holding $E'$ fixed at the mediator stage makes $z_Y=y\oplus e'$ independent
   of $X$, and the controlled residual is zero.
4. **Common cause.** Observationally,
   $P(y=1\mid x=1)=337/625$, whereas
   $P(y=1\mid\operatorname{set}(X,1))=1/2$. Conditioning and intervention are
   not identified.
5. **Reader cancellation.** Changing $E$ flips $(x',y')$ while preserving
   $x'\oplus y'$. The parity reader reports zero response; the complete reader
   reports the nonzero change.
6. **Context reversal.** For $u_X=x\oplus c$, the signed effect of
   $\operatorname{set}(X,1)$ versus $\operatorname{set}(X,0)$ on $u_X=1$ is
   $+1$ at $c=0$ and $-1$ at $c=1$.
7. **Spectator.** As a registered source-context contrast rather than an
   intervention address, changing $q_0$ has exact zero effect on every
   relational output because it does not enter the relational evaluator.
8. **Joint-stage control.** The triple $(x',y',e')$ is constructed in one
   relational mechanism evaluation and is $X/Y$ covariant. Symmetry or
   simultaneous syntax alone is not promoted to a co-onset or chronology.

### Theorem 8 — reciprocal relational response

The candidate has nonzero matter-to-relation and relation-to-matter signed
response coordinates and passes the common-cause, mediation, cancellation,
context-reversal, spectator, and symmetric-joint-stage controls. Every
coordinate descends under the presentation groupoid.

#### Proof

The displayed Boolean identities give the exact labeled contrasts. Theorem 2
transports the complete experiment, mark, reader, and output together, so the
signed family is constant on its diagonal orbit. Because the physical quotient
was formed before $R$, a coarse-reader zero cannot delete the complete-reader
coordinate. ∎

This is reciprocal relational response. It is not geometry response,
backreaction, energy transfer, gravity, or causal influence.

## 16. Static-law and metadata firewalls

The observational law is the value at the empty program. Replacing a
conditional factorization of that value while retaining all observational
masses does not modify any generator kernel or any $J$-indexed law value.
It therefore cannot move an interventional response inside this candidate.
Doing so would define a different function $\mathbf\Gamma_D$.

Program syntax and marks select which primitive law value is evaluated but
are absent from histories. A reader that reports the experiment name would
not be generated by $\mathsf{ProbeAddr}$ and is refused. Consequently neither
program metadata nor serialization order can create a physical response.

## 17. Mandatory gate closure

The construction satisfies the seventeen pre-freeze gates as follows.

1. Reverse-stage writes meet an empty hom-set in $\mathsf{Ctrl}$.
2. All control hom-sets compose by associative override; all execution
   hom-sets compose by typed free-category concatenation.
3. Readers are absent from the stabilizer defining the physical quotient.
4. Every field reader is generated by and transports an exact probe address.
5. Tensor and fusion are different typed generators with product and
   cross-pair semantics respectively.
6. Sections 7, 10, and 11 give a total target-valued clause for every
   generator.
7. $\mathsf{Fut}_{\rm stable}$ contains its entire generated monoid and the
   projector theorem holds for every finite word.
8. $E_r$ is an executable typed arrow and is not in the stable subcategory.
9. The enlarged $(m,q_0)$ restart is an explicit nonkill, not the native cut.
10. Metadata readers are outside $\mathsf{ProbeAddr}$ and metadata are absent
    from histories.
11. Stabilizer-orbit pushforward normalizes; representative mass generally
    does not.
12. Theorem 7 proves deletion commutes with transport and evaluation.
13. Finite-set presentations and auxiliary seed exposure orders are gauge;
    staged physical fusion remains a distinct trace rather than a hidden
    presentation of one event.
14. The parity cancellation is exposed by the complete reader.
15. The full executable function, not a static factorization, fixes response.
16. No parameter, dimension, geometry, or desired result selects the packet.
17. The law supplies possible histories only and contains no actuality rule.

## 18. Product vector and permanent walls

Subject to independent semantic review, the mathematical candidate supports
the provisional product

```text
referent    P13D-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED
law         P13D-ONE-TYPED-EXECUTABLE-GAMMA-CONSTRUCTED
experiment  P13D-TYPED-EXPERIMENT-CATEGORY-CONSTRUCTED
nondivision P13D-NATIVE-B1-CUT-NONDIVISIBLE
record      P13D-TYPED-STABLE-FUTURE-CATEGORY-CONSTRUCTED
eraser      P13D-EXECUTABLE-ERASER-CONTROL-CONSTRUCTED
division    P13D-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13D-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13D-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13D-ACTUALIZATION-UNCONSTRUCTED
```

These coordinates are `GREEN-UNREVIEWED`, not terminal and not citable.

$\mathbf\Gamma_D$ supplies normalized possibilities, not a realized branch.
Actualization is unconstructed. The candidate derives no operational
chronology, causal order, signal cone, dimension, signature, topology,
volume, duration, scale, clock, metric, connection, curvature, stress tensor,
energy, entropy, gravity, general relativity, continuum limit, quantum field
theory, particle content, or phenomenology. A later failure of any geometric
test may not retune this law.
