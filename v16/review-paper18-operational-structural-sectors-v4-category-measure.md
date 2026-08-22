# Paper 18 version-4 category, bundle, and measure review

Date: 2026-08-21

Seat: **M -- category, bundle, and measure**

Verdict: **REVISE**

First decisive issue: **Replacement Definition 12 together with the unrestricted
choice of the total sigma algebra \(\Xi\) does not reject a non-Borel
same-target split hidden by a strict coarse sub-sigma-algebra.**  The exact
product-Borel example in version 4 is rejected, but the coarse variant below
satisfies Definitions 10 and 10A, satisfies (V4.2)--(V4.5), and witnesses
positive branching at every input under (V4.3).  This falsifies the claim in
Section 4.1 that coarsening necessarily removes rather than hides the
branching failure, and it fails Seat-M mandatory control 11.

No earlier category or measure failure was found.  In particular, the
event/integral equivalence, target pushforward, normalization, and measurable
gauge calculations are valid on the declared measurable spaces.  The verdict
is nevertheless at least `REVISE` because a frozen mandatory control fails.

This is a mathematical review only.  It supplies no implementation,
code-based proof, parameter fit, downstream output, or in-place repair.

## 1. Authentication, composite, and review integrity

I authenticated and read every assigned artifact completely.  Counts below
are ordinary LF counts and byte counts; hashes are ordinary SHA-256.

| artifact | ordinary SHA-256 | LF | bytes | result |
|---|---|---:|---:|---|
| complete version-2 base | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | 1165 | 41256 | exact |
| binding version-3 amendment | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` | 318 | 10598 | exact |
| binding version-4 amendment | `33f1e9a05bdc16b7aa96831fe1e8bc4c3bd4ca5095d2f79cbbe0c6d32abe8137` | 357 | 13093 | exact |
| version-4 construction note | `16299722b0cefee1e4bf26ddd2b644e50461def6261d355f971b2563875c609e` | 81 | 3342 | exact |
| frozen version-4 review protocol | `9f3078ded7f3c91fc52efa098160a05123e77fab9a60bfb5dbbc85567c6dddd8` | 160 | 7491 | exact |
| version-3 adjudication | `f35e91d9dd5b68aefcd75a55612f64ba15e9f1d6a30f856eb12f43ff914ec45c` | 116 | 4683 | exact |

I reconstructed the candidate as the ordered composite

\[
 \text{version 2 base}\;<\;\text{version 3 amendment}\;<\;
 \text{version 4 amendment},
\]

with the later text controlling only its named replacements.  Thus the
version-3 pseudo-limit, indexed-history, resolved-object, Paper-13D, and
outcome-coordinate clauses survive except where version 4 expressly replaces
them; all other version-2 clauses survive.

I remained mutually blind.  I did not inspect, list, contact, summarize, or
infer any version-4 sibling report or reviewer.  I wrote only this assigned
report and did not stage or commit it.

## 2. Decisive coarse-sigma countermodel

This countermodel is a strict coarse variant of version 4's Section 4.1
example, not the product-Borel example already printed in the candidate.

Let

\[
 \mathsf S=\mathbb R_{\geq 0},\qquad X=\mathsf S\times\mathsf S,
 \qquad \mathcal C=X\times\{0,1\},
\]

and write \(x=(a,b)\).  Both channel classes over \(x\) target \(a+b\):

\[
 p(x,i)=x,\qquad \tau(x,i)=a+b.
\]

The two points in each fiber are stipulated to be inequivalent physical
resolved objects.  The indices \(0,1\) are only notation for the two points;
all events admitted below are events of the declared total measurable bundle.

Choose a non-Borel set \(V\subset(0,\infty)\) and put

\[
 w(a,b)=
 \begin{cases}
  1/3,&a\in V,\\
  2/3,&a\notin V,
 \end{cases}
 \qquad
 \mu_x=w(x)\delta_{(x,0)}+(1-w(x))\delta_{(x,1)}.
\tag{M.1}
\]

For Borel \(B\subseteq X\), let \(D(B)=p^{-1}(B)\).  Declare

\[
 \Xi_{\mathrm c}
 =\{D(B)\mathbin\triangle N:
       B\in\mathcal B(X),\;N\subseteq\mathcal C\text{ countable}\}.
\tag{M.2}
\]

This is a sigma algebra: complements retain the displayed form, and a
countable union differs from the diagonal cylinder over the union of its base
sets by at most a countable set.  Every displayed set is product Borel, so
\(\Xi_{\mathrm c}\) is a sub-sigma-algebra of the product-Borel sigma
algebra.

The bundle requirements all hold.

1. For Borel \(B\subseteq X\), \(p^{-1}(B)=D(B)\in\Xi_{\mathrm c}\), so
   \(p\) is measurable.
2. Each singleton \(\{(x,i)\}\) belongs to \(\Xi_{\mathrm c}\).  Hence the
   trace sigma algebra on every two-point fiber is the full discrete sigma
   algebra.
3. The admitted point-local channel tests are total measurable events.  No
   reader name, basis, or history value is being turned into a channel.
4. For Borel \(A\subseteq\mathsf S\),
   \(\tau^{-1}(A)=D(\{(a,b):a+b\in A\})\), so \(\tau\) is measurable.

The family (M.1) is a Definition-10A kernel on this coarse bundle.  Indeed,
if \(E=D(B)\mathbin\triangle N\), then

\[
 x\longmapsto\mu_x(E_x)
\]

equals \(\mathbf 1_B(x)\) away from the countable Borel set \(p(N)\).
On \(p(N)\) it can take the values \(0,1,w(x),1-w(x)\), but an arbitrary
real function supported on a countable subset of a standard Borel space is
Borel measurable.  Thus every total-event map required by Definition 10A is
measurable even though \(w\) itself is not.  The primitive-positive-kernel
provenance branch can be fixed before normalization, so provenance does not
exclude the example.

Moreover, at every input \(x\), the two disjoint total events

\[
 E_{x,0}=\{(x,0)\},\qquad E_{x,1}=\{(x,1)\}
\]

have positive \(\mu_x\)-mass.  Replacement Definition 12 therefore declares
nontrivial measure-supported resolved branching at every \(x\).

The target pushforward is

\[
 \mathsf M_{a,b}=\delta_{a+b}.
\]

It has unit \(0\), finite words, and bracketing independence.  With \(d=1\),
(V4.4) holds and (V4.5) returns the already normalized kernel \(\mu\).  Thus
none of the target-composition or positive-character hypotheses blocks the
example.

Finally, the global index event

\[
 E_0=X\times\{0\}
\]

is product Borel but is not in \(\Xi_{\mathrm c}\).  For every Borel
\(B\subseteq X\), the symmetric difference \(E_0\mathbin\triangle D(B)\)
contains exactly one point over every \(x\), hence is uncountable; it cannot
be the countable \(N\) in (M.2).  On the product-Borel bundle, its event map
is the nonmeasurable function \(w\), so the exact printed control is rightly
rejected.  On the strict coarsening, however, every fiber remains fully
measurable, both positive fiber branches extend to total events, the family
passes the event-kernel test, and Theorem 3 applies.

Consequently the formal contract does exactly what Section 4.1 says a
coarsening cannot do: it hides the nonmeasurable global split while retaining
pointwise measurable branching.  Extension of each positive event at one
fixed input is too weak to enforce the frozen coarse-sigma rejection control.
This is a contract-level counterexample, independent of any implementation
or downstream physics.

## 3. Seat-M duties M1--M15

### M1. Complete profiles and sector groupoids -- pass

Definitions 1--5 remain well typed.  A profile arrow contains a total
invertible typed functor, measurable outcome isomorphisms, exact pushforward
equalities, and naturality.  Identities, specified inverses, and composition
therefore close.  Partial catalogues and probability-preserving maps that
change intervention or reader identity are excluded.  The first coordinate
\([s]_{\mathcal G}\) prevents behavioral degeneracy from erasing
nonisomorphic physical structure.  Presentation automorphisms create arrows,
not extra sector classes.

### M2. Marked restriction, pseudo-limit/descent, and deletion -- pass

Marked restriction is a contravariant functor only when literal typed
pullback exists; its identity and composition equations are exact.  The
version-3 replacement correctly interprets the inverse limit as a
groupoid-valued pseudo-limit: an object carries coherent restriction
isomorphisms satisfying the cocycle equation, and arrows are compatible
families.  It is not a strict equality of chosen representatives.

Uniform unmarked deletion remains a separately typed Markov kernel on
point-free class spaces.  It is neither an arrow in the marked-boundary
category nor a substitute for exact restriction.  A presentation-dependent
rule such as retaining the first occurrence still fails the automorphism
test.

### M3. Dependent sum, projection, fiber sigmas, and target -- typed, but not
enough for the required rejection

The dependent sum \(\mathcal C=\coprod_x\mathcal C_x\), declared sigma
algebra \(\Xi\), measurable projection \(p\), trace algebras
\(\Xi_x\), and total measurable target \(\tau\) form a coherent measurable
bundle in the literal sense stated.  Trace algebras are sigma algebras, and
the definition does not assume equal fibers, discreteness, countable
generation, or a standard-Borel structure.

The defect is not a typing failure of these objects.  It is that these axioms
allow the coarse bundle (M.2), which defeats a mandatory semantic rejection
while retaining full fiber sigmas and local branching.

### M4. Event-kernel/integration equivalence -- pass without standard Borel

For a family of finite positive measures on the trace fibers, the total-event
condition implies (V4.1) as follows.  It first handles indicators
\(f=\mathbf1_E\).  Finite nonnegative linear combinations give total simple
functions.  Every nonnegative \(\Xi\)-measurable function is the increasing
pointwise limit of such simple functions, and fiberwise monotone convergence
makes its integral the increasing limit of measurable base functions.  The
limit is measurable.  Conversely, applying (V4.1) to every indicator recovers
the event condition.  None of these steps uses countable generation,
standard-Borel structure, regular conditional probabilities, or
disintegration.

### M5. Target kernel (V4.2) -- pass

For \(A\in\Sigma\), total measurability of \(\tau\) gives
\(\tau^{-1}(A)\in\Xi\); Definition 10A then makes
\(x\mapsto\mathsf M_x(A)\) measurable.  Each pushforward is finite and
positive, and

\[
 \mathsf M_x(\mathsf S)=\mu_x(\mathcal C_x)>0,
\]

so it is nonzero.  Thus (V4.2) is a finite input-measurable target kernel on
arbitrary declared measurable branches.

### M6. Unit and composition closure -- pass as separate hypotheses

Pushforward alone proves neither the unit equations nor finite-word
bracketing independence.  Version 4 explicitly imports both as additional
Definition-13 hypotheses.  It also preserves the stronger separation between
target marginal associativity and a resolved path category with associators
and pentagon coherence.  No resolved path coherence is awarded by a one-step
kernel.

### M7. Extension of positive fiber events -- local lemma passes; varying-input
criterion fails the coarse control

By definition, every \(A\in\Xi_x\) has at least one total extension.  If
disjoint \(A_0,A_1\in\Xi_x\) initially extend to \(E_0,E_1\in\Xi\), then
\(E_0\setminus E_1\) and \(E_1\) are disjoint total extensions with the same
traces at \(x\).  Hence the fixed-input equivalence asserted after (V4.3) is
correct.

It is not sufficient for the advertised varying-input rejection.  The total
extensions may be supported over one measurable input point, as in Section 2,
so all local positive branches survive although no uniform event follows the
non-Borel split.  That is the decisive failure.

### M8. Resolved normalization, target pushforward, and gauge -- pass on the
stated hypotheses

For total \(E\in\Xi\), (V4.1) applied to
\(\mathbf1_E d\circ\tau\) makes the numerator of (V4.5) measurable.  The
denominator is positive and measurable, and (V4.4) makes total mass one.
Applying the result to \(\tau^{-1}(A)\) gives exactly (V4.6), not merely an
equal normalization constant.

For measurable positive \(h\), the density in (V4.7) is total measurable:
the input factors are measurable through \(p\) and the coordinate
projections, while the output factor is measurable through \(\tau\).  The
event/integration equivalence therefore makes \(\boldsymbol\mu^h\) a kernel
whenever the expressly assumed one-step and finite-word finiteness holds.
The \(h\)-factors cancel in both resolved and target normalized laws.  The
candidate correctly does not claim that the gauge repairs a non-kernel.

### M9. No silent regular conditional probability -- pass

The resolved bundle and kernel are primitive or independently constructed
objects.  A target kernel is used only as a pushforward and is never
disintegrated to create resolved fibers or conditional laws.  The
non-standard branch explicitly requires direct event maps and integrals.
The proofs use only ordinary kernel integration and monotone convergence.

### M10. Same-target controls -- pass

For the finite discrete control,

\[
 \mu_{a,a}=\delta_{\kappa_0}+\delta_{\kappa_1},\qquad
 \mathsf M_{a,a}=2\delta_a,
\]

with ordinary unit channels is finite and target-associative.  The character
equation gives \(d(a)=2\), each resolved class has probability \(1/2\), and
the target law is \(\delta_a\).  Multiplicity is supplied by two stipulated
inequivalent physical classes, not by a basis or desired probabilities.

For the continuous control, Lebesgue measure on a Borel \([0,1]\) fiber has
two disjoint positive half-intervals while all singletons have zero measure;
constant target gives a deterministic target pushforward.  Thus the
definition correctly detects positive-family branching without atomicity.

### M11. Exact and coarse non-Borel controls -- fail

On the full product-Borel bundle, the event selecting index 0 is measurable
and has the nonmeasurable event map \(w\); Definition 10A correctly rejects
that exact model.  Section 2 proves that a strict coarse sub-sigma-algebra can
retain full fiber sigmas, positive total-event witnesses at every input, and
a valid kernel while removing only the uniform event.  The claimed coarse
rejection therefore fails.

### M12. Automorphisms, orbits, groupoids, rooted spectators, and multiplicity
-- pass with no measure promotion

Version 4 places measures on isomorphism classes.  Isomorphic representatives
and presentation or spectator permutations therefore do not become extra
resolved slots.  An object-level invariant measure is admissible only if it
descends to the same class kernel.  Resolved counting and finite-groupoid
cardinality remain different provenance choices: the former weights physical
classes, while the latter uses inverse automorphism weights.  Neither orbit
size nor a wreath-product representative count may silently replace the
other.  Rooted local odds still require an independently constructed physical
kernel and any required projectivity; spectator automorphisms alone supply no
factorial propensity.

Two equal-target slots count as multiplicity only when they are inequivalent
physical channel objects.  Reader labels, bases, and child-history values do
not create slots.  The Paper-13D fixed simultaneous-fusion family therefore
retains one resolved generator class; fresh bond values remain in its indexed
history fiber.

### M13. Inherited category/measure regressions -- one failure, otherwise
conservative

The following amendment-sensitive regressions were rerun.

| regression | result |
|---|---|
| partial or non-total profile correspondence | rejected |
| profile map omitting an intervention/reader or changing its identity | rejected |
| behavioral equality erasing nonisomorphic structure | rejected |
| presentation relabeling creating new sectors/channels | rejected |
| nonfunctorial marked restriction | rejected |
| `first occurrence` under an \(S_2\) automorphism | rejected |
| uniform deletion used as marked restriction | rejected |
| strict equalizer substituted for groupoid descent | rejected by v3 scope |
| finite levels used to infer finite/discrete completion | rejected |
| non-standard cylinder completion omitted by type | rejected |
| topology or groupoid claimed to choose a measure | rejected |
| history values or coarse outputs counted as channels | rejected |
| staged trace erased solely because endpoints agree | rejected |
| desired probabilities inserted as multiplicities | rejected |
| orbit count exchanged with inverse-automorphism weight | rejected |
| pairwise finite pushforward promoted to finite-word closure | rejected |
| target associativity promoted to resolved path coherence | rejected |
| target kernel used to infer a resolved kernel/disintegration | rejected |
| normalized representation used as prior measure selection | rejected |
| exact product-Borel nonmeasurable split | rejected |
| nonmeasurable split hidden by coarse \(\Xi\) | **accepted by countermodel; failure** |

No amendment licenses chronology, dimension, topology, geometry, or
actualization as a measure selector.

### M14. Contract versus constructed physical measure -- pass

Definitions 10 and 10A specify what a measurable bundle and a physically
provenanced kernel would have to be.  They do not construct either object for
the current Paper-13D alternatives.  The candidate explicitly states that no
total Paper-13D channel bundle or finite resolved kernel over primitive,
staged, fused, and disconnected whole complexes has been supplied.  A
normalized child-history law cannot fill that gap.  The present physical
measure and both induced-law coordinates therefore remain unconstructed.

### M15. Fresh semantic countermodels -- completed

Section 4 records eight fresh models, including a genuinely varying-fiber
bundle.  They are mathematical semantic tests, not implementations.

## 4. Fresh semantic countermodels

### F1. Strict coarse-sigma non-Borel split -- candidate fails

Section 2 gives the full construction.  It is the decisive model: full
two-point trace algebras and point-local total events coexist with a coarse
total sigma algebra that makes the non-Borel pointwise weights invisible to
the event-kernel test.  V4.3 nevertheless declares branching everywhere.

### F2. Borel varying finite fibers -- candidate passes

Let \(\mathsf S=\mathbb R_{\geq0}\), \(X=\mathsf S^2\), and

\[
 \mathcal C_x=
 \begin{cases}
  \{0\},&a\in\mathbb Q,\\
  \{0,1\},&a\notin\mathbb Q.
 \end{cases}
\]

Realize the dependent sum as the Borel subset

\[
 (X\times\{0\})\cup
 (\{(a,b):a\notin\mathbb Q\}\times\{1\})
\]

of \(X\times\{0,1\}\), with its trace Borel sigma algebra.  Put mass one on
0 at rational \(a\), and mass \(1/2\) on each point at irrational \(a\).
All event maps are Borel.  With target \(a+b\), the target kernel is
\(\delta_{a+b}\), so unit, finite words, associativity, and \(d=1\) hold.
There is no resolved branching at rational inputs and there is positive
resolved branching at irrational inputs.  This confirms that the dependent
sum handles genuinely varying fiber cardinality when the variation is
measurable.

### F3. Same target, two inequivalent resolved kernels -- candidate passes

On \(\mathsf S=\{\mathbf1,a\}\), give the \((a,a)\)-fiber two inequivalent
classes with common target \(a\).  Compare resolved weights \((1,3)\) and
\((2,2)\); use ordinary unit fibers.  Both push forward to
\(\mathsf M_{a,a}=4\delta_a\).  This convolution is associative, and
\(d(a)=4\) satisfies the character equation.  The first resolved law is
\((1/4,3/4)\), the second is \((1/2,1/2)\), while both target laws are
\(\delta_a\).  Thus target pushforward neither identifies a resolved kernel
nor supplies a disintegration.

### F4. Finite unit kernel with nonassociative target -- candidate passes by
refusing closure

Let \(\mathsf S=\{\mathbf1,a,b\}\) and put one resolved channel over each
input, targeting the value of a deterministic binary operation with unit
\(\mathbf1\) and table

\[
 a\star a=b,\quad a\star b=a,\quad b\star a=\mathbf1,
 \quad b\star b=b.
\]

Every one-step pushforward is a finite measurable probability kernel and the
unit equations hold.  But

\[
 (a\star a)\star a=\mathbf1\ne a=a\star(a\star a).
\]

Hence pushforward plus unit does not give bracketing independence.  The
composite correctly leaves composition closure as an additional hypothesis
and keeps its present coordinate unproven.

### F5. Automorphism-weighted same-target classes -- candidate passes

On \(\mathsf S=\{\mathbf1,a\}\), let the \((a,a)\)-channel groupoid have two
isomorphism classes \(\alpha,\beta\), both targeting \(a\), with automorphism
groups of orders 2 and 4.  Finite-groupoid cardinality gives class weights
\(1/2\) and \(1/4\), not two representative counts.  Thus
\(\mathsf M_{a,a}=(3/4)\delta_a\), and \(d(a)=3/4\) is a positive character.
The resolved probabilities are \(2/3\) and \(1/3\), while the target law is
deterministic.  This checks descent to isomorphism classes, inverse-
automorphism weighting, same-target multiplicity, and the distinction from
ordinary resolved counting.

### F6. Hybrid atomic/nonatomic same-target fiber -- candidate passes

Let the \((a,a)\)-fiber be the measurable disjoint union
\([0,1]\sqcup\{\star\}\), with measure
\(\lambda+\delta_\star\), and let every point target \(a\).  With ordinary
unit fibers, the target convolution is \(2\delta_a\), so \(d(a)=2\).  The
resolved law assigns probability \(1/2\) to the atom and probability \(1/2\)
to the continuum, while the target law is deterministic.  This tests a
hybrid fiber and shows that target multiplicity does not reveal whether the
resolved mass is atomic or continuous.

### F7. Direct non-standard cylinder branch -- candidate passes without RCP

Take \(\mathsf S=\{\mathbf1,a\}\) and, over \((a,a)\), the fiber
\(\Omega=\{0,1\}^I\) for uncountable \(I\), equipped with its cylinder sigma
algebra and directly supplied fair product measure; use singleton unit fibers
and give all points target \(a\).  A cylinder fixing one coordinate and its
complement are disjoint positive events, but the sigma algebra is not
countably generated.  The total bundle and kernel are constructed directly
over the finite base; no regular conditional probability or disintegration
is used.  Version 4 correctly accepts the declared branch by its event maps
rather than by its type name.

### F8. Two set-level points with a trivial fiber event algebra -- candidate
passes by refusing measurable branching

Let \(\mathcal C=X\times\{0,1\}\) but declare only the total sigma algebra
\(\Xi=\{p^{-1}(B):B\in\mathcal B(X)\}\).  Every trace fiber then has the
trivial sigma algebra \(\{\varnothing,\mathcal C_x\}\).  A total-mass-one
fiber measure gives a valid event kernel and may have a deterministic target,
but neither point singleton is a resolved event.  Version 4 correctly reports
set-level plurality without measurable positive branching.  Contrasting F8
with F1 isolates the defect: merely coarsening to the base algebra removes
branching, but the axioms also allow a strict coarse algebra that retains all
point-local branches.

## 5. Surviving mathematical results and scope

The decisive failure does not invalidate the following conditional results:

1. complete profile isomorphisms and bounded sector arrows form groupoids;
2. marked restriction, stochastic deletion, and pseudo-limit descent remain
   separately typed;
3. on any declared bundle satisfying Definition 10A, event measurability is
   equivalent to integration measurability for nonnegative total functions;
4. (V4.2) is the finite measurable target pushforward;
5. under the separately assumed target convolution and character hypotheses,
   (V4.5) is a resolved probability kernel and (V4.6) is exactly its target
   pushforward;
6. the measurable gauge preserves both normalized laws when all stated
   finiteness hypotheses hold;
7. a primitive target kernel supplies neither a resolved bundle nor a
   resolved kernel or regular conditional law;
8. target bracketing does not supply resolved path coherence; and
9. the finite same-target and continuous same-target positive controls remain
   mathematically valid.

These are conditional contract statements.  They do not construct the
current physical sector census, completion, channel measure, character,
resolved law, target law, whole selector, or actuality.

## 6. Full version-4 product vector

The conservative vector printed by the candidate remains the only admissible
current vector; the failed review does not promote or demote a scientific
coordinate:

    P18-SECTOR-REFERENT-CONTRACT-CONSTRUCTED
    P18-BOUNDED-SECTOR-CENSUS-UNCONSTRUCTED
    P18-GLOBAL-SECTOR-COMPLETION-UNCONSTRUCTED
    P18-CURRENT-GAMMA-STRUCTURAL-BRANCHING-FORK-PROVED
    P18-NONTRIVIAL-STRUCTURAL-BRANCHING-UNCONSTRUCTED
    P18-PHYSICAL-CHANNEL-MEASURE-UNCONSTRUCTED
    P18-COMPOSITION-CLOSURE-UNPROVEN
    P18-POSITIVE-CHARACTER-UNTESTED-NO-PHYSICAL-CHANNEL-MEASURE
    P18-RESOLVED-CHANNEL-LAW-UNCONSTRUCTED
    P18-TARGET-SECTOR-LAW-UNCONSTRUCTED
    P18-WHOLE-SELECTOR-UNCONSTRUCTED
    P18-ACTUALIZATION-UNCONSTRUCTED
    P18-CHRONOLOGY-NOT-EVALUATED
    P18-DIMENSION-NOT-EVALUATED
    P18-SIGNATURE-NOT-EVALUATED
    P18-METRIC-NOT-EVALUATED
    P18-CURVATURE-NOT-EVALUATED
    P18-GRAVITY-NOT-EVALUATED

## 7. Disposition

**REVISE.**  The full product-Borel nonmeasurable split is rejected, but the
formal definitions accept its strict coarse-sigma variant while still
declaring positive resolved branching at every input.  This is the first and
decisive mathematical issue.  Under the frozen completion rule, this report
does not alter the candidate or supply a repair.  It authorizes no
implementation, selector construction, parameter choice, actualization,
Paper-17 evaluation, or Paper 19 work.
