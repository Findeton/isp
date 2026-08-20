# One relational transition law on changing point-free configurations

## A finite exact model with record-bearing divisions and indivisible cuts

### Abstract

<!-- CLAIM:ABSTRACT:START -->
We construct one exact stochastic law on complete typed relational
configurations and derive its support changes, probability screens, record
writer, delayed reader, and relational response from that same law.  The
primitive configurations are finite Boolean zero patterns modulo typed
relabeling; their Venn cells and raw names are presentation data, not points.
The law acts on complete fillings through rational class amplitudes and assigns
ordinary endpoint probabilities by a stated squaring postulate.

The model contains both kinds of cut that an indivisible stochastic theory
needs.  A carried-record boundary is a lawful probabilistic division: its
alternatives remain readable under every word in a declared continuation
grammar, and direct and cut factorizations agree.  At a different, unrecorded
cut, the complete endpoint law admits no positive source-independent restart
kernel on the declared configuration carrier.  A definite configuration may
still be actual there; only autonomous Markov restarting is excluded.

The same primitive also makes a matter bit change a raw Boolean relation and
makes that relation alter a later matter response.  A resource-matched family
then excludes every stochastic transducer that receives only a specified
incidence-blind interface.  These are finite, class-relative results.  The
coupling, event grammar, division doctrine, squaring clause, and actualization
rule are not selected, and no valuation, metric, curvature, continuum theory,
or gravitational dynamics is obtained.
<!-- CLAIM:ABSTRACT:END -->

## Why the whole law comes first

<!-- CLAIM:MOTIVATION:START -->
Indivisibility is easily weakened into a slogan.  One can independently build
regional laws, a quantum instrument, a record writer, and a relational rewrite
and then place them in a common container.  Even if every module is correct,
the container need not be one law.  The basic engineering requirement is
therefore also the scientific one: begin with one executable law on complete
configurations and obtain every claimed shadow by restriction or composition.

Barandes describes quantum systems as ordinary-probability stochastic
processes whose laws need not divide at arbitrary intermediate times, with
Hilbert-space objects taking a secondary representational role.  The present
construction adopts that architectural distinction but does not claim to
derive Barandes's framework or to inherit its physical adequacy.  In
particular, the configuration catalogue here can change, whereas the cited
formulation starts from a given configuration space.

The distinction to be tested is narrower than “Markovian versus mysterious.”
At a lawful division, probabilities can be restarted from the declared source
argument.  At a nondivision cut, a configuration can have an ordinary target
probability and can even be definite in one history, while no autonomous
positive kernel exists that forgets the earlier lawful boundary.  This is the
specific form of stochastic indivisibility investigated below.
<!-- CLAIM:MOTIVATION:END -->

## Point-free contextual configurations

<!-- CLAIM:KINEMATICS:START -->
A finite presentation context is a pair

$$
X=(\mathcal R,\mathcal C_X),
$$

where $\mathcal R$ is a finite set of typed Boolean roles and
$\mathcal C_X$ is the set of nonzero Venn cells realized by those roles.  A
cell $s\in\mathcal C_X$ is represented by the subset of roles true on that
cell.  The cells are bookkeeping for a finite Boolean subalgebra; they are not
physical points or indivisible atoms.  Standard Boolean-algebra background is
given by Sikorski.

Two formulas represent the same contextual Boolean element when they have the
same truth vector on $\mathcal C_X$.  Variables that do not change this vector
are inessential.  Thus, on a context where $B$ implies $A$,

$$
B=A\mathbin{\wedge}B
$$

as contextual elements even though the raw formulas differ.  A typed role
bijection transports cells, formulas, ports, configurations, complete
fillings, and the operators derived from them.  These bijections form the
source groupoid.  Equality of raw names or serialized hashes is not physical
equality.

A port consists of a fresh relation role $N$ and two nonzero complementary
parent elements $P_0,P_1$.  Its sector is one of

$$
\{\varnothing,0,1\}.
$$

If the sector is $\varnothing$, the child is absent.  In sector $b$, the child
is present over parent $P_b$.  For a nonzero contextual parent $P$, define the
support extension by

$$
\mathcal C_{\operatorname{Split}_{P,N}(X)}
=
\mathcal C_X
\mathbin{\cup}
\{s\mathbin{\cup}\{N\}:s\in\mathcal C_X,\ P(s)=1\}.
$$

The original satisfying cell is retained and its child-labelled partner is
added.  Forgetting $N$ is the inverse merge on the resulting context.

### Result A — exact contextual support extension

**Scope: finite typed Boolean zero patterns.**  If $N$ is fresh and $P$ is
nonzero, the displayed construction is a proper Boolean support extension.
Every source cell has exactly one target representative when $P(s)=0$ and
exactly two when $P(s)=1$.  The target has no extra roles or cells, forgetting
$N$ returns $X$, and $N$ differs from every old Boolean element.

### Proof

The target cells are given exhaustively by the displayed union.  Projection
along $N$ therefore maps each target cell to one source cell.  Its fiber is
$\{s\}$ when $P(s)=0$ and

$$
\{s,s\mathbin{\cup}\{N\}\}
$$

when $P(s)=1$.  These fibers are disjoint and cover the target.  On a
satisfying fiber every formula in the old roles is constant, while $N$ takes
both truth values.  Hence $N$ cannot equal $P$ or any old Boolean element.
Forgetting $N$ collapses each two-cell fiber and recovers $X$.  ∎

The finite exact census used below contains six source contexts.  It has
seventy-two nonzero ambient formula presentations but forty-two contextual
Boolean classes.  Every ambient representative produces the same extension,
operator, endpoint law, and physical source key as the other representatives
in its contextual class.
<!-- CLAIM:KINEMATICS:END -->

## One whole-filling transition law

<!-- CLAIM:LAW:START -->
Fix a rational coupling

$$
\frac13\leq g\leq\frac12.
$$

For a Boolean query $Q$, let $\chi_X(Q)$ be one when $Q$ is nonzero on $X$
and zero otherwise.  Define the rational Cayley rotation

$$
R_x=
\frac{1}{1+x^2}
\begin{pmatrix}
1-x^2 & -2x\\
2x & 1-x^2
\end{pmatrix}.
$$

The configuration also carries matter bits and one sector for each declared
port.  For output bit $c'$, the structural map $\rho_{c'}$ exchanges
$\varnothing$ with sector $c'$ and fixes the other occupied sector.  On the
context it performs the corresponding exact split or inverse merge.

For one typed occurrence $a=(Q,p)$, the sole primitive matrix-element rule is

$$
\langle X',c',e'\lvert T_g(a)\rvert X,c,e\rangle
=
R_{g\chi_X(Q)}[c',c]
\,\mathbf 1\!\left[(X',e')=\rho_{c'}(X,e)\right].
$$

All unselected matter bits and ports are transported identically.  A complete
filling $U=a_n\circ\cdots\circ a_1$ is a typed composite, and its class
operator is

$$
K_g(U)=T_g(a_n)\cdots T_g(a_1).
$$

Tensor products and typed structural permutations are included in the same
composition language.  This use of a symmetric monoidal process grammar is
standard; Selinger gives a general account of such compositional languages.

The stochastic law is the whole-filling assignment

$$
\Gamma_g(y\mid x;U)
=
\left\lvert\langle y\lvert K_g(U)\rvert x\rangle\right\rvert^2.
$$

Endpoint squaring is a postulated clause of this candidate law.  It is not
derived here.  Amplitude coordinates and internal path labels are
representational; the relative phase and composition class of the complete
filling are nomological because changing them changes $\Gamma_g$.  Sorkin's
histories-based quantum measure theory supplies broader context for
amplitude-squared assignments, but the particular finite rule above is our
construction.

### Result B — normalization and one-root composition

**Scope: every admitted finite filling of the declared typed grammar.**  Each
primitive $T_g(a)$ is an isometry, and identity, composition, tensor,
associator, symmetry, and unitor operations preserve that property.  Hence

$$
\sum_y\Gamma_g(y\mid x;U)=1
$$

for every complete admitted source argument $(g,U,x)$.

### Proof

For rational $x$, the two column norms of $R_x$ equal

$$
\frac{(1-x^2)^2+4x^2}{(1+x^2)^2}=1,
$$

and their inner product vanishes.  For each fixed output bit,
$\rho_{c'}$ is a bijection on the three port sectors and on the associated
typed contexts.  Distinct source columns therefore retain exactly the Cayley
inner products.  Composition and tensor products of isometries are
isometries, while the structural arrows are typed permutations.  Squaring one
source column of $K_g(U)$ then gives unit total probability.  ∎

The complete source argument includes the law identity, source and derived
target boundaries, full filling, and source configuration.  It has no optional
hidden-history or native-context slot.  This is lawful-source sufficiency; it
does not say that an arbitrary intermediate configuration is a Markov restart
state.
<!-- CLAIM:LAW:END -->

## Support change is derived, not declared

<!-- CLAIM:SUPPORT:START -->
The support split is an operand of the primitive structural map, rather than a
separately supplied rewrite.  Each nonzero primitive coefficient carries an
exhaustive fiber certificate bound to its actual law, occurrence, port,
source, output bit, parent element, child, target, and operation kind.  The
three operation kinds are create, merge, and unchanged.

### Result C — finite totality and split covariance

**Scope: the registered finite generator family and all contextual Boolean
representatives in the census.**  The exact finite controls have the following
sizes.

| object | exact count |
|---|---:|
| source contexts | 6 |
| nonzero ambient formula representatives | 72 |
| contextual Boolean classes | 42 |
| generator families | 12 |
| declared source columns | 312 |
| nonzero primitive transitions | 468 |
| create certificates | 156 |
| merge certificates | 156 |
| unchanged certificates | 156 |

Every one of the four hundred sixty-eight nonzero transitions is bound to its
own recomputed certificate.  Typed relabeling transports the certificate and
the operator together.  Replacing the split by a coextensive child, retaining
only the child-labelled cell, padding the target, attaching a certificate from
another parent, or reverting to a role-and-cell-count test fails the native
support predicate.

The census is a finite verification surface, not the reason the general split
lemma is true.  The proof of Result A supplies the all-context argument for an
admitted parent and fresh child.
<!-- CLAIM:SUPPORT:END -->

## A native nondivision cut

<!-- CLAIM:NONDIVISION:START -->
At $g=1/2$, one create-and-erase pair restricted to the matter bit has
amplitude matrix

$$
R=
\begin{pmatrix}
3/5 & -4/5\\
4/5 & 3/5
\end{pmatrix}.
$$

The one-pair probability screen is

$$
B=\lvert R\rvert^2
=
\frac1{25}
\begin{pmatrix}
9 & 16\\
16 & 9
\end{pmatrix},
$$

where the square is entrywise.  Two uninterrupted coherent pairs give

$$
C=\lvert R^2\rvert^2
=
\frac1{625}
\begin{pmatrix}
49 & 576\\
576 & 49
\end{pmatrix}.
$$

### Result D — no positive autonomous restart

**Scope: the declared two-state configuration carrier at the unrecorded cut.**
There is no positive source-independent stochastic matrix $K$ satisfying

$$
C=KB.
$$

### Proof

The determinant of $B$ is nonzero, so the algebraic solution is unique:

$$
K=CB^{-1}
=
\frac1{175}
\begin{pmatrix}
351 & -176\\
-176 & 351
\end{pmatrix}.
$$

Its off-diagonal entries are negative.  It is therefore not a transition
probability matrix.  ∎

The result holds throughout the frozen rational coupling interval.  Let

$$
t(g)=\frac{1-6g^2+g^4}{(1+g^2)^2}.
$$

On $1/3\leq g\leq1/2$, $t$ decreases from $7/25$ to $-7/25$.  It cannot
vanish at rational $g$: otherwise $u=g^2$ would be a rational root of

$$
u^2-6u+1=0,
$$

but the rational-root candidates are not roots.  The nontrivial eigenvalue of
the unique factor is $2t-1/t$, and therefore

$$
\left\lvert2t-\frac1t\right\rvert
=
\frac1{\lvert t\rvert}-2\lvert t\rvert
\geq
\frac{527}{175}>1.
$$

A stochastic two-state kernel cannot have such an eigenvalue.  Thus the
failure is not an isolated numerical accident.

The correct interpretation is limited but substantive:

> The cut is not a lawful stochastic division on the declared configuration
> space: the complete endpoint law admits no positive source-independent
> factorization through it. A definite configuration may still be actual
> there; what is forbidden is an autonomous Markov restart conditioned only
> on that configuration.

Indeed, the positive history-conditioned joint

$$
P(a,b\mid q)=B_{aq}C_{bq}
$$

has marginal $C_{bq}$ and permits a definite intermediate $a$.  Its future
conditional still depends on the earlier source $q$.  Enlarging the carrier
by a phase, amplitude vector, or complete history can also Markovize the
calculation.  Neither observation proves that the added variable is an ontic
property.  The theorem is configuration-relative and excludes only the
native autonomous restart.
<!-- CLAIM:NONDIVISION:END -->

## A lawful record-bearing division

<!-- CLAIM:DIVISION:START -->
The same primitive behaves differently when the first branch is sealed in a
carried child sector and later occurrences use a fresh active port.  The
recorded two-step matter probabilities are then the ordinary product

$$
B^2=
\frac1{625}
\begin{pmatrix}
337 & 288\\
288 & 337
\end{pmatrix},
$$

rather than the coherent screen $C$.

Let $P_r$ be the projector onto carried record value $r$.  The declared future
grammar has two matter roles and three exact query types, giving six generator
letters.  Every licensed letter $F$ satisfies the typed intertwining equation

$$
P_r^{\mathrm{out}}F=FP_r^{\mathrm{in}}.
$$

### Result E — grammar-relative stochastic division

**Scope: every finite word generated by the declared continuation grammar.**
The carried branch is readable after every licensed word, and direct endpoint
probabilities equal probabilities obtained by cutting at the carried-record
boundary and summing over its alternatives.

### Proof

The writer's branch maps have orthogonal target sectors and their Gram
operators sum to the identity for every admitted input.  The intertwining
equation holds for each generator.  It holds for the identity, and if it holds
for $F$ and $G$, then

$$
P_r(GF)=(P_rG)F=(GP_r)F=G(P_rF)=GFP_r.
$$

Induction therefore covers every finite licensed word.  Orthogonality removes
cross terms between carried alternatives, so the direct and cut probability
calculations agree.  ∎

Permanence is explicitly grammar-relative.  If the old carried port is
retyped as active, the same primitive admits an exact inverse toggle that
erases it.  The construction therefore earns one nontrivial division under a
declared future grammar, not an unconditional theorem that records can never
be erased.
<!-- CLAIM:DIVISION:END -->

## Matter changes relation and relation changes matter

<!-- CLAIM:RECIPROCAL:START -->
The writer correlates a source matter output with the presence and incidence
of a child relation.  A later occurrence acts on a distinct probe bit but
queries the literal output context of the writer.  For a blank input at
$g=1/2$, the joint distribution of source output $s'$ and probe output $p'$ is

$$
P(s',p')=
\begin{pmatrix}
9/25 & 0\\
144/625 & 256/625
\end{pmatrix}.
$$

The rows are $s'=0,1$ and the columns are $p'=0,1$.  The entries sum to one.
Conditioned on the written branch $s'=1$, the later probe-one probability is
$16/25$.  In the same typed boundary with the child incidence changed from
overlap to outside, that probability is zero.

### Result F — same-law reciprocal relational response

**Scope: the finite writer-reader fixture and its same-boundary incidence
counterfactual.**  A matter output changes the raw relation used by a later
matter response, and both arrows are restrictions of the same primitive law.

The counterfactual is a calibrated source-sensitivity comparison, not a new
eraser dynamics or a claim of autonomous experimental control.  The result
earns raw relation-mediated response, or proto-backreaction in this restricted
sense.  A Boolean contact is not yet distance, metric, curvature, or gravity.
<!-- CLAIM:RECIPROCAL:END -->

## A resource-matched relational family

<!-- CLAIM:FAMILY:START -->
For size $m$, introduce roles $L_i,N_j$ and a permutation $\pi$.  The global
context contains one zero cell, one private cell for every role, and one shared
cell $L_i=N_{\pi(i)}=1$ for each $i$.  Consequently every member has

$$
3m+1\ \text{cells},\qquad 4m\ \text{incidences},\qquad 2m\ \text{roles},
$$

with support two for every role and degree one in the $L$--$N$ contact graph.
The calibrated query at slot $i$ is $L_i\wedge N_i$, so it is nonzero exactly
when $i$ is a fixed point of $\pi$.

Distinct queried slots receive distinct matter bits and ports in one complete
filling.  The law is evaluated once on the global object.  Because the
occurrences act on disjoint bits and ports and their queries omit every newly
created child, the primitive maps commute and the endpoint law factorizes as
a theorem:

$$
\Gamma_g(z'\mid0;U_S)
=
\prod_{i\in S}
\left\lvert R_{g\mathbf1[\pi(i)=i]}[z'_i,0]\right\rvert^2.
$$

The product is not supplied to the evaluator; it is checked against the direct
global class operator.

### Result G — incidence-blind class exclusion

**Scope: stochastic transducers with common initialization that receive only
the declared incidence-blind interface, including transducers with unbounded
memory.**  There are resource-matched members with identical blind prefixes
and prior record laws but unequal relational responses.  No transducer in the
declared blind class reproduces both.

### Proof

The blind interface retains the size, role and port types, filling order,
resource counts, cell-arity histogram, support and degree multisets, query
schedule, and prior lawful record outcomes.  It removes only cross-interface
co-reference and the permutation itself.  Paired members therefore deliver
the same input token and prior-output law at each step before the challenge.
From a common initial memory distribution, induction gives the same memory
distribution and hence the same predicted response at the challenge.  The
one-law responses differ, a contradiction.  ∎

An exact size-twelve member uses query slots $1,8,9,10$.  In the common member
all four are fixed points, and their marginals are

$$
\left(\frac{16}{25},\frac{16}{25},\frac{16}{25},\frac{16}{25}\right).
$$

For the challenge permutation

$$
(5,11,7,3,2,1,6,4,9,0,10,8),
$$

only the final queried slot is fixed, giving

$$
\left(0,0,0,\frac{16}{25}\right).
$$

Both direct global evaluations have a target catalogue of one thousand two
hundred ninety-six states; the peak context has thirty-seven cells.  The
blind resources and prior record law are identical.

This is not an absolute irreducibility theorem.  A comparator given the
incidence relation, a member-specific initial state, or a lookup oracle lies
outside the declared class.  The family assay tests relational load; it is
factorized and is not itself the indivisibility witness of Result D.
<!-- CLAIM:FAMILY:END -->

## Representation, ontology, and open physics

<!-- CLAIM:ONTOLOGY:START -->
The construction keeps the following distinctions explicit.

| object | status in this model |
|---|---|
| typed Boolean zero-pattern orbit | candidate complete relational configuration |
| raw role names, Venn cells, and formula syntax | presentation |
| complete filling and its boundary order | priced process kinematics |
| rational class-amplitude assignment | representation of the law |
| whole-filling phase and composition class | nomological because it changes endpoint probabilities |
| endpoint squaring | postulated law clause |
| carried child sector | derived record under the declared grammar |
| raw Boolean contact | relation, not geometry or causality |
| coupling $g$ | unselected law parameter |
| one actual configuration | ontological candidate with actualization postulated |

Law-sufficiency belongs to the complete typed source argument at an admissible
source or division boundary.  It does not belong to a bare configuration at
every arbitrary cut.  Conversely, failure of a native Markov factorization
does not by itself prove that the configuration is ontologically incomplete.
The amplitude representation can retain boundary information without thereby
becoming a physical wavefunction or hidden phase register.

The model supplies neither a selector for $g$ nor an autonomous selector for
fillings, events, or lawful divisions.  It assumes a finite Boolean catalogue,
a process grammar, the Cayley family, endpoint squaring, and an actualization
postulate.  These assumptions are displayed rather than relabelled as
emergent.

Nothing here establishes an extensive valuation, operational length, metric,
dimension, topology, causal order, Lorentzian structure, curvature,
continuum limit, stress response, gravitational equation, quantum field
theory, particles, species, Hamiltonian, vacuum, or phenomenology.  Those
would require separate constructions and separate discriminators.
<!-- CLAIM:ONTOLOGY:END -->

## Conclusion

<!-- CLAIM:CONCLUSION:START -->
The finite model clears a specific architectural threshold.  It starts from
one law on complete changing relational configurations and derives, rather
than juxtaposes, support change, an indivisible screen, a lawful record
division, a delayed relational reader, and a resource-matched family assay.
The same law contains a cut through which ordinary probabilities compose and
a cut through which no positive autonomous restart exists.

The strongest justified conclusion is therefore one exact, finite,
class-relative relational transition-law candidate with event grammar priced.
That conclusion is deliberately short of law selection or geometry.  The next
scientific question is not how to decorate the raw contacts with metric
language.  It is whether an operational order and an extensive valuation can
be derived from the law without inserting the metric structure they are meant
to explain.
<!-- CLAIM:CONCLUSION:END -->

## References

<!-- CLAIM:REFERENCES:START -->
- Jacob A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,”
  arXiv:2507.21192, 2025, <https://doi.org/10.48550/arXiv.2507.21192>.
- Rafael D. Sorkin, “Quantum Mechanics as Quantum Measure Theory,” *Modern
  Physics Letters A* **9** (1994), 3119–3128,
  <https://doi.org/10.1142/S021773239400294X>.
- Roman Sikorski, *Boolean Algebras*, third edition, Ergebnisse der Mathematik
  und ihrer Grenzgebiete **25**, Springer, 1969,
  <https://books.google.com/books?id=ICMxwgEACAAJ>.
- Peter Selinger, “A Survey of Graphical Languages for Monoidal Categories,”
  in Bob Coecke, ed., *New Structures for Physics*, Lecture Notes in Physics
  **813**, Springer, 2011, 289–355,
  <https://doi.org/10.1007/978-3-642-12821-9_4>.
<!-- CLAIM:REFERENCES:END -->
