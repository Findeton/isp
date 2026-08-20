# Paper 13C mathematical review — category, groupoid, and referent

Date: 2026-08-20

Status: **INDEPENDENT BLIND SEMANTIC REVIEW / REJECT**

## 1. Verdict

```text
REJECT
```

The finite threshold evaluator contains a coherent and normalized labeled
subconstruction.  The native queried boundaries, the cut-relative negative
restart result, the record/division controls, and the unmarked varying-size
family survive this review.  The frozen packet nevertheless does not define
the claimed complete experiment category or a reader-independent point-free
physical-history law.

The first decisive counterexample is categorical.  Both
`set(E'_i,0)` and `set(X_i,1)` are individually admitted mechanism
generators.  The paper also calls their programs a category and says that
concatenation followed by normal-form reduction is its composition.  Their
concatenation in the order

$$
\operatorname{set}(E'_i,0)\ ;\ \operatorname{set}(X_i,1)
$$

is simultaneously required to compose, because the two generators are
already morphisms, and required to be refused, because a source-stage write
follows a mediator-stage write.  If distinct-slot commutation silently
reorders it, the explicitly forbidden stage-reversed word becomes admitted.
If stage objects are intended to make the pair noncomposable, the required
source and target objects of the mechanism generators are absent.  These are
different categories.  Resolving the choice changes an admitted composition
or the generator typing and is therefore a semantic-law change, not a proof
or prose repair.

Two further independent defects are also decisive:

1. A diagnostic reader is included in the experiment stabilizer used to
   quotient physical histories.  An invariant reader and an asymmetric
   reader therefore induce different physical-history cells even though the
   labeled history law is unchanged.  This fails mandatory attack H8.
2. The asserted independent tensor $e\boxtimes f$ is not an object of the
   stated domain $\coprod_n\mathsf{Exp}_n$: its tagged pair has no cross-pair
   field, whereas every fused size-$(n+m)$ endpoint has one.  No boundary
   types, group action, unit, associator, or evaluator are defined for the
   tagged-pair object.  Hence the mandatory $\otimes$ component of the packet
   is not constructed.

No implementation issue enters this verdict.

## 2. Corpus authentication and blindness

I authenticated the frozen bytes before review.

| artifact | commit | SHA-256 | size |
|---|---|---|---:|
| physics pin | `9acac0c` | `6f6acdfdc3065e7376eabb118adcf9c9b09cc89770f3616d31927366e7ab4c4f` | 464 LF lines / 15,629 bytes |
| mathematical paper | `562f623` | `51c16c5bf85bb7dd0db44e3477233a6f331a0efe01f306600379165fcf932bed` | 946 LF lines / 31,376 bytes |
| construction note | `562f623` | `c93e0ca95ba3bf75601a7dd1d258167f545fb60c733cdff6ad1d7e1b5ffc2a7f` | 104 LF lines / 3,858 bytes |
| review protocol | `6bae696` | `392a6d3497e3ea2b6e7116d462da35cbec8c8445f210e7943785d01e114eea64` | 285 LF lines / 11,396 bytes |

I read all four artifacts completely.  I did not inspect or contact a sibling
Paper 13C report or any Paper 13B review.  I used no repository evaluator,
fixture, Rust source, or generated result.

## 3. Independent common reconstruction

### 3.1 Exact transition arithmetic

Squaring the frozen rotation gives

$$
R^2=\frac1{25}
\begin{pmatrix}-7&-24\\24&-7\end{pmatrix}.
$$

Therefore

$$
B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix},
\qquad
C=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix}.
$$

The threshold $u<9$ has 9 same-state and 16 flipped-state values.  The
threshold $25u_1+u_2<49$ has 49 same-state and 576 flipped-state values, so
these matrices follow from the evaluator rather than being inserted answers.
Direct multiplication gives

$$
B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix},
$$

and

$$
B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix},
\qquad
CB^{-1}=\frac1{175}
\begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
$$

The restart candidate is unique because $\det B=-7/25\ne0$ and is not a
stochastic kernel because it has negative entries.

### 3.2 Boundary values and process paths

The frozen boundary fields reconstruct as follows.

| object | complete legal value |
|---|---|
| $0_n$ | $((q_{0i},h_i,c_i,e_i^0))_i$ |
| $1_n^0$ | $((m_i,h_i,a_i))_i$ |
| $1_n^r$ | $((m_i,r_i,h_i,a_i))_i$, $r_i=m_i$ |
| $2_n^0$ | $((q_{2i},t_i,a_i))_i,(\ell_{ij})_{i<j}$, $t_i=h_i$ |
| $2_n^r$ | the $2_n^0$ value plus $(r_i)_i$ |

Here

$$
a_i=(x_i,y_i,\epsilon_i,x'_i,y'_i,e'_i,z_{Xi},z_{Yi},u_{Xi},u_{Yi},d_i),
\qquad d_i=e'_i.
$$

The process category has the five identities, generators

$$
U:0\to2^0,\quad Q^0:0\to1^0,\quad D:1^0\to2^0,
\quad Q^r:0\to1^r,\quad R_c:1^r\to2^r,
$$

and only the two nonidentity composites $D\circ Q^0$ and
$R_c\circ Q^r$.  Mismatched path endpoints refuse.  This process-path
subcategory itself is a well-defined finite category.

A path history contains the source, exactly the traversed intermediate
boundaries, and its target.  Thus $U$ contains no $B_1$ value; $Q^0,Q^r$
terminate at their respective $B_1$ objects; and the two composites contain
their respective $B_1$ values.

### 3.3 Evaluations and direct-composite equality

For each occurrence,

$$
U:\ q_2=\kappa(q_0,u_1,u_2),
$$

$$
Q^0:\ m=\beta(q_0,u_1),
\qquad
Q^r:\ (m,r)=(\beta(q_0,u_1),m),
$$

$$
D:\ q_2=\beta(m,u_2),
\qquad
R_c:\ q_2=\beta(m,u_2),\ r\text{ carried}.
$$

An identity copies the supplied complete boundary and uses no new coin.  The
two directly evaluated composites use independent $u_1,u_2$ and hence have
joint kernel

$$
P(m,q_2\mid q_0)=B_{m q_0}B_{q_2m}.
$$

Standalone $D$ or $R_c$ supplies exactly the same fresh $u_2$ law.  Its fresh
pair coins generate exactly the same endpoint bonds as the direct composite,
while $a$ and $h$ are copied.  Therefore direct and cut evaluation agree on
complete target histories, not merely on the $B^2$ marginal.

### 3.4 Seed and context normalization

At fixed $n$, all $4n$ public source bits are fair; the $2n$ matter-noise bits
have positive masses $16/25,9/25$; the $2n$ transition coins and
$\binom n2$ pair coins are uniform on $[25]$.  Every public assignment has
positive mass.  A nonempty public cylinder $K$ therefore has $P(K)>0$, and
$P(\xi\mid K)=P(\xi)1_K/P(K)$ is uniquely normalized.  Later-boundary inputs
are exact point arguments with only the declared fresh coins.  Deterministic
pushforward preserves normalization.

This reconstructs normalized laws for each explicitly given closed tuple.
It does not cure the missing experiment-category and tensor objects identified
in Sections 1 and 5.

### 3.5 Presentation action and orbit multiplicity

The declared group has order

$$
|\mathcal G_n|=2^n n!.
$$

Internal swaps exchange all $X/Y$-typed fields and slots and fix
$\epsilon,e',d$; occurrence permutations transport all occurrence fields and
unordered bond endpoints.  The product seed law and every evaluator formula
are equivariant under that action.

For a fully specified experiment $e$, the frozen physical cell is
$\mathcal G_eH$.  Its exact size is

$$
|\mathcal G_eH|
=\frac{|\mathcal G_e|}{|\mathcal G_{e,H}|},
\qquad
\mathcal G_{e,H}=\{g:g e=e,\ gH=H\}.
$$

Orbit-sum mass, rather than one representative mass, is consequently required.
This part of the construction correctly counts fixed points and graph
automorphisms when the experiment object itself is unambiguous.

### 3.6 Fixed-size, grand-size, deletion, and extension

At fixed size, orbit cells partition the labeled fiber, so orbit pushforward
preserves total mass one.  Globally,

$$
\sum_{n=0}^{\infty}2^{-(n+1)}=1.
$$

On the unmarked observational family, uniform deletion is an equivariant
Markov kernel: choose one of the $n$ occurrences, delete all its traversed
fields and incident bonds, and then quotient.  Iid occurrence seeds and iid
unordered-pair seeds leave the size-$(n-1)$ law.  Equivariance makes deletion
before or after quotient agree, including histories with automorphisms.

Adding two occurrences in either auxiliary order creates the same unordered
set of old--new and new--new pair seeds.  Product multiplication commutes, so
the two labeled laws and their quotient pushforwards agree.  This establishes
the stated observational projectivity; it does not define the absent external
tensor object or a general marked-deletion functor.

### 3.7 Record/division square

The reconstructed four cells are:

| stable record | complete division | witness |
|---|---|---|
| yes | yes | complete $1^r$ frontier of $R_c\circ Q^r$ |
| yes | no | record-only $(r_i)_i$, because omitted $h$ fixes later $t=h$ |
| no | yes | complete $1^0$ frontier of $D\circ Q^0$ |
| no | no | declared $B_1$ cut of unqueried $U$ |

The future generators preserve record sectors up to transported labels; the
many-to-one reset does not.  A reversible sector swap is therefore not an
eraser.  Record stability and complete future sufficiency remain independent.

### 3.8 Signed response reconstruction

For a fully specified labeled experiment, the contrast

$$
\Delta_{S;a,b}(A)
=P_{J;S\leftarrow a}(A)-P_{J;S\leftarrow b}(A)
$$

is defined by the one evaluator rather than a chain-rule factorization.  The
displayed controls check algebraically:

- toggling $X$ at fixed $Y,E$ flips
  $e'=\epsilon\oplus x\oplus y$ and hence changes an incident bond by signed
  magnitude $7/25$;
- toggling $E$ at fixed $X,Y$ flips the complete pair $(x',y')$;
- without an $E'$ override, $z_Y=\epsilon\oplus x$, while fixed $E'$ removes
  the $X$ response;
- iid $\eta_X,\eta_Y$ give
  $P(Y=1\mid X=1)=(16^2+9^2)/625=337/625$, whereas `set(X,1)` leaves $Y$
  marginally fair;
- the parity reader misses the $E$ response which the discrete pair reader
  detects;
- the $u_X=1$ sign is $+1$ at $c=0$ and $-1$ at $c=1$; and
- $q_0$ is a spectator for the relational packet.

Thus a labeled reciprocal-response precursor survives.  The claimed physical
point-free response coordinate does not pass this seat because its physical
history quotient changes with the diagnostic reader, as shown next.

## 4. First decisive semantic counterexample in full

Let

$$
A=\operatorname{set}(E'_1,0),
\qquad B=\operatorname{set}(X_1,1).
$$

Each is explicitly an admitted generator.  The mechanism-program paragraph
makes programs into a category, gives the empty program as identity, and
makes concatenation plus last-write normalization associative.  Category
closure therefore requires the composite word $A;B$ whenever $A$ and $B$ are
endomorphisms of the same implicit program object.

But $A;B$ places the mediator-stage generator before the source-stage
generator, and the frozen rule says exactly such a word is not a morphism.
There are only three possible readings:

1. refuse $A;B$, in which case the claimed mechanism category is not closed;
2. commute it to $B;A$, in which case the required stage-reversed refusal is
   false; or
3. give $A,B$ different stage source/target objects, in which case those
   objects and types are missing from the frozen category.

The partial-map normal form $(J_0,J_1)$ cannot decide among these readings,
because it erases the word order that is supposed to determine refusal.  A
three-write version, such as $A;\operatorname{set}(X_1,0);
\operatorname{set}(X_1,1)$, makes the same problem survive both last-write
parenthesizations.  This refutes the exact composition and refusal claims in
H9 and H11.

## 5. Reader-dependent physical quotient

Take $n=1$, path $U$, tautological context, empty mechanism and mark sets.
Let $\sigma$ be the internal $X/Y$ swap.

- Let $\Pi_{\rm inv}$ be the discrete target partition.  As an unordered set
  of singleton cells it is invariant under $\sigma$, so
  $\sigma\in\mathcal G_{e_{\rm inv}}$.
- Let $\Pi_X$ be the two-cell partition according to target field $x$.  Its
  transport is the partition according to $y$, so generically
  $\mathcal G_{e_X}=\{1\}$.

Choose a positive-mass history $H$ with $x\ne y$.  Exchangeability gives
$p(H)=p(\sigma H)>0$.  With $\Pi_{\rm inv}$ the frozen physical-history cell
is

$$
\{H,\sigma H\}
$$

and has mass $2p(H)$.  With $\Pi_X$ the two singleton history cells have mass
$p(H)$ each.  Only the nondisturbing diagnostic reader changed; the evaluator
and labeled history law did not.

Therefore the claimed physical history law is not reader-independent.  The
reader is described as an external typed argument and H8 explicitly requires
only its diagnostic pushforward to change.  Including $\Pi$ in
$\mathcal G_e$ instead changes the physical sample-space quotient itself.
Removing it from the stabilizer or replacing the construction by a common
history object with transported observables would change the frozen quotient
and hence is not an admissible review fix.

## 6. Mandatory attacks H2--H17

| attack | result | reconstruction |
|---|---|---|
| H2 metadata in history | pass | adding the program name makes alternative programs disjoint even for a spectator outcome, producing spurious total-variation response one; the frozen history field list excludes it |
| H3 history-only quotient | pass locally | full-group history quotient erases the intervention's relative marked location; the diagonal marked-pair idea is the correct comparator, although its reader treatment fails H8 |
| H4 representative mass | pass | a nonfixed orbit of size $k$ has mass $kp$, not $p$; representative mass undernormalizes |
| H5 fixed point/automorphism | pass | exact stabilizer examples are reconstructed in §7.2 |
| H6 naked symmetric slot | pass locally | naked $X$ descends neither as a fixed slot nor as an invariant contrast; the transported experiment/reader-cell triple does |
| H7 incomplete packet transport | **undefined/fail** | transport of listed components is stated, but the allowed additional “reader probes” in $M$ have no exact port catalogue or action; because $M$ affects $\mathcal G_e$, this is semantic |
| H8 reader-selected physics | **fail** | §5 gives an explicit invariant-reader/asymmetric-reader counterexample |
| H9 unlisted/retyping/stage reversal | **fail** | `W` and generic mode refuse, but stage-reversed legal generators contradict categorical closure |
| H10 composition/conditioning | partial pass | execution concatenation and positive-cell conditioning are named as distinct operations, but the execution category inherits the program-composition defect |
| H11 last-write associativity | **fail** | partial maps associate only after silently forgetting the stage order used to refuse words |
| H12 tensor/fusion | **fail** | fusion is defined, but the tagged no-cross-bond tensor is outside every stated $\mathsf{Exp}_n$ and has no evaluator/category data |
| H13 graph order | pass | occurrence permutation and unordered-pair seed transport remove enumeration order; two extension orders agree |
| H14 dormant carrier | pass | a fixed carrier with active bits is a different sample space and does not establish the frozen disjoint-union projectivity |
| H15 per-size replacement | pass | changing any threshold or bond rule at one size changes the uniform evaluator and therefore the law |
| H16 deletion after quotient | pass at claimed scope | the uniform deletion Markov kernel is equivariant on the unmarked observational family; marked naturality is not constructed |
| H17 native boundary absence | pass | $1_n^0,1_n^r,Q^0,Q^r,D,R_c$ are genuine typed objects/arrows with standalone evaluations, not comparison matrices |

## 7. Additional independent countermodels

These countermodels are independent of the first category-closure defect.

### 7.1 Marked-slot stabilizer

For $n=1$, a tautological unmarked frame may have stabilizer $C_2$.  Marking
`set(X,1)` reduces the experiment stabilizer to the identity because the swap
transports it to `set(Y,1)`.  A history-only full-group quotient would merge
$H$ with $\sigma H$ and erase which relative port was manipulated.  The
diagonal experiment--history construction correctly retains this relation.

### 7.2 Nontrivial graph automorphism

For $n=2$, $|\mathcal G_2|=8$.  Choose two identical occurrence packets, each
internally $X/Y$-fixed, and one symmetric bond value.  The complete history is
fixed by both internal swaps and the occurrence transposition, so its
stabilizer has size 8 and its orbit has size 1.  A generic history with two
distinct packets and no internal $X/Y$ symmetry has trivial stabilizer and
orbit size 8.  Assigning both one representative mass either overcounts the
fixed point or undercounts the generic orbit.  The frozen orbit-sum formula,
when the experiment is fixed, passes this control.

### 7.3 Invariant reader versus oriented reader

The $\Pi_{\rm inv}/\Pi_X$ construction in §5 uses the same evaluator and
positive pair $H,\sigma H$ but changes only reader invariance.  It changes the
physical outcome partition, refuting H8 and showing that reader transport and
reader participation in the history stabilizer are not interchangeable.

### 7.4 Intermediate source-boundary enlargement

Enlarge $1^0$ from $(m,h,a)$ to $(m,q_0,h,a)$.  Then the positive normalized
continuation

$$
K(q_2\mid m,q_0,h,a)=C_{q_2q_0}
$$

restarts the endpoint law while ignoring $m$.  This does not refute the frozen
negative result: it is an enlarged carrier carrying the source input and is a
different boundary object.  The example confirms that the nondivision claim
is correctly cut-relative.

### 7.5 Tensor/fusion separation countermodel

Fuse two one-occurrence endpoint trials.  The fused $n=2$ object contains a
fresh Bernoulli bond $\ell_{12}$ with probability $16/25$ or $9/25$ depending
on endpoint colors.  The asserted external tensor has no $\ell_{12}$ field.
Their sample spaces are not isomorphic as the declared typed histories, so
the product law cannot be represented by the fused evaluator.  This validates
the intended distinction but also proves that a new tagged-pair object and
evaluator are required for $\boxtimes$.

### 7.6 Incomplete marked-port universe

Let two presentations agree on $p,J,K,\Pi$ and on all named mechanism marks,
but let one additional probe be a transported $X$ port and the other an
invariant relation port.  These choices give different experiment stabilizers.
The phrase that $M$ “may contain additional reader probes” does not specify
which of these is admitted or how it transports.  Since the resulting orbit
masses can differ, the omission cannot be treated as harmless annotation.

## 8. Native cut and permanent nonkills

For every fixed common exterior context, $q_0$ is independent of the
relational and transition private coins, so the declared $B/C$ comparison is
not produced by averaging away $h,c,e^0$.  For $n\ge1$ the unique candidate
is $(CB^{-1})^{\otimes n}$; choosing one negative off-diagonal factor and
positive diagonal factors for the other occurrences exhibits a negative
entry.

The following remain explicit nonkills:

- $C=CI=IC$ on different carriers;
- the $n=0$ empty process;
- the enlarged $(m,q_0)$ source boundary in §7.4; and
- the positive queried endpoint law $B^2=BB$, which belongs to a different
  experiment from unqueried $U$.

No absolute indivisibility claim is earned or made.

## 9. Product vector

```text
referent    P13C-EXECUTABLE-GAMMA-REFERENT-UNCONSTRUCTED
law         P13C-LAW-UNSELECTED
experiment  P13C-EXPERIMENT-CATEGORY-UNDEFINED
nondivision P13C-NATIVE-B1-CUT-NONDIVISIBLE
record      P13C-GRAMMAR-STABLE-RECORD-CONSTRUCTED
division    P13C-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13C-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13C-RECIPROCAL-RESPONSE-UNCONSTRUCTED
actuality   P13C-ACTUALIZATION-UNCONSTRUCTED
```

`P13C-LAW-UNSELECTED` is used here because the frozen packet does not select
one complete value on its mandatory experiment domain: cross-stage
composition, additional probe marks, and the external tensor have no unique
simultaneous semantics.  It is not an allegation of output-based parameter
tuning.  Each explicitly supplied closed labeled tuple is normalized.

The lower response coordinate reflects the reader-dependent physical quotient.
The exact labeled signed tensors reconstructed in §3.8 remain valid algebraic
precursors, but they do not yet descend to the claimed reader-independent
point-free physical-history law.

## 10. Permanent walls and Rust gate

The corpus correctly does not derive actualization, chronology, causal order,
dimension, signature, topology, volume, duration, scale, metric, curvature,
gravity, GR, continuum physics, or QFT.  No hidden global clock, geometry, or
actual history was found in the evaluator.

This is a mathematical-semantic rejection under the frozen protocol.  Fixing
it would require changing category objects/composition, the physical quotient,
or the experiment domain.  Accordingly this report does not authorize Rust.
