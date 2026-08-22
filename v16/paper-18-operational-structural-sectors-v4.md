# Paper 18 version-4 measurable-channel-bundle amendment

## Status and composition rule

The version-4 mathematical candidate is the ordered composite of:

1. the complete version-2 base
   `v16/paper-18-operational-structural-sectors-v2.md`, ordinary SHA-256
   `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614`;
2. the binding version-3 amendment
   `v16/paper-18-operational-structural-sectors-v3.md`, ordinary SHA-256
   `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd`;
   and
3. this amendment.

This amendment has precedence over version 3 exactly where it names a
replacement. Version 3 has precedence over version 2 everywhere else stated
in version 3. Every unmentioned clause remains literal. These precedence
rules define one mathematical object, not optional commentary.

Version 4 binds the version-3 adjudication, ordinary SHA-256
`f35e91d9dd5b68aefcd75a55612f64ba15e9f1d6a30f856eb12f43ff914ec45c`.

The amendment is result-neutral. It adds no channel, measure, parameter,
selector, dimension, geometry, implementation, or physical outcome. It
repairs only the measurable typing of a varying family of resolved channel
spaces.

## 1. The total measurable resolved-channel bundle

### Replacement Definition 10 -- resolved-channel class bundle

Let

\[
 X=\mathsf S\times\mathsf S
\]

with its product sigma algebra. For each input pair \(x=(a,b)\), let

\[
 \mathcal C_x=|\mathsf{Ch}(a,b)|
\]

be the set of isomorphism classes of resolved unmarked physical channel
objects defined in version 3. Form the set-theoretic dependent sum

\[
 \mathcal C=\coprod_{x\in X}\mathcal C_x
\]

with projection \(p:\mathcal C\to X\).

A **resolved-channel measurable bundle** is a declared sigma algebra
\(\Xi\) on \(\mathcal C\) such that:

1. \(p:(\mathcal C,\Xi)\to X\) is measurable;
2. the fiber sigma algebra is
   \[
    \Xi_x=\{E\cap\mathcal C_x:E\in\Xi\};
   \]
3. every admitted resolved-channel observable is represented by a
   \(\Xi\)-measurable function, with reader names, labels, bases, and
   realized child histories still excluded as channel distinctions; and
4. the total target map
   \[
    \tau:(\mathcal C,\Xi)\longrightarrow(\mathsf S,\Sigma),
    \qquad \tau|_{\mathcal C_{(a,b)}}=\tau_{a,b},
   \]
   is measurable.

This is a measurable dependent sum, not an assumption that all fibers are
equal or that \(\mathsf S\) is discrete or standard Borel. Finite,
countable, continuous, hybrid, and declared non-standard measurable branches
remain admissible. If no such total measurable bundle is constructed, a
varying-input resolved probability law is unconstructed even when every
individual fiber is a measurable space.

Set-level inequivalence can establish a possible channel catalogue. A
purported physical distinction that is absent from \(\Xi\) cannot be used
as an event of the resolved probability law.

### Replacement Definition 10A -- finite resolved-channel kernel

An independently physical finite resolved-channel kernel on
\((\mathcal C,\Xi,p)\) is a family

\[
 \boldsymbol\mu=\{\mu_x:x\in X\}
\]

such that:

1. \(\mu_x\) is a finite nonzero positive measure on
   \((\mathcal C_x,\Xi_x)\);
2. for every total measurable resolved event \(E\in\Xi\),
   \[
    x\longmapsto\mu_x(E_x),
    \qquad E_x=E\cap\mathcal C_x,
   \]
   is measurable on \(X\); and
3. its provenance is exactly one of the version-2 Definition-14 branches and
   is fixed before conditional probabilities are evaluated.

The kernel is invariant because its fibers consist of channel isomorphism
classes. An equivalent object-level formulation may use invariant measures
on the total channel groupoid, but it must descend to exactly this class
kernel and may not replace it by representative weights.

The event condition, not merely fiberwise measurability, is the defining
input-measurability requirement. Equivalently, for every nonnegative
\(\Xi\)-measurable function \(f\),

\[
 x\longmapsto
 \int_{\mathcal C_x}f(\kappa)\,\mu_x(d\kappa)
\tag{V4.1}
\]

is measurable. The equivalence follows first for indicator functions, then
for nonnegative simple functions, and finally by monotone convergence.

No disintegration is inferred from a target kernel. In particular, on a
non-standard measurable branch, the existence of a regular conditional law
inside target fibers is not assumed; \(\boldsymbol\mu\) itself must be
supplied or constructed.

## 2. Target pushforward and measurable branching

### Replacement of version-3 equation (V3.1)

The target pushforward of a finite resolved-channel kernel is

\[
 \mathsf M_x(A)
 =\mu_x\bigl((\tau^{-1}A)_x\bigr),
 \qquad A\in\Sigma.
\tag{V4.2}
\]

For each \(A\), \(\tau^{-1}A\in\Xi\), so Definition 10A makes
\(x\mapsto\mathsf M_x(A)\) measurable. Thus \(\mathsf M\) is a finite
nonzero positive kernel. Unit, finite-word finiteness, and bracketing
independence are additional requirements inherited from version-2
Definition 13; pushforward alone does not prove them.

When only a primitive target kernel \(\mathsf M\) is supplied, neither a
total resolved bundle nor a resolved kernel is inferred. Many distinct
resolved kernels can have the same target pushforward, and a disintegration
need not exist on the declared measurable branch.

### Replacement Definition 12 -- measurable resolved branching

Resolved structural plurality at an input \(x\) means that
\(\mathcal C_x\) contains at least two inequivalent independently physical
channel classes not reducible to child histories or their coarse-grainings.
Their targets may coincide.

There is **nontrivial measure-supported resolved branching** at \(x\) exactly
when an independently physical finite resolved-channel kernel admits two
disjoint events \(E_0,E_1\in\Xi\) such that

\[
 \mu_x((E_0)_x)>0,
 \qquad
 \mu_x((E_1)_x)>0.
\tag{V4.3}
\]

Equivalently, the two positive fiber events belong to \(\Xi_x\), which by
definition means that they extend to total measurable resolved events. The
events need not have different target images. A common target gives resolved
branching with a deterministic target pushforward.

Set-level plurality without a physical kernel proves no odds. A fiber split
whose input dependence is nonmeasurable is not a resolved conditional law.
If its two channel classes are not separated by \(\Xi\), it is not even a
measurable branching event at this level.

## 3. Measurable positive-character laws

### Replacement Theorem 3 -- resolved-kernel and target-kernel laws

Suppose:

1. \((\mathcal C,\Xi,p,\tau)\) is a resolved-channel measurable bundle;
2. \(\boldsymbol\mu\) is an independently physical finite
   resolved-channel kernel;
3. its target pushforward \(\mathsf M\) from (V4.2) is a finite positive
   measurable convolution in the sense of version-2 Definition 13; and
4. a measurable \(d:\mathsf S\to\mathbb R_{>0}\), with
   \(d(\mathbf1)=1\), satisfies
   \[
    d(a)d(b)=\int_{\mathsf S}d(c)\,\mathsf M_{a,b}(dc)
   \tag{V4.4}
   \]
   for every input pair.

Then

\[
 \boxed{
 \mathsf P^{\rm res}_{a,b}(E_{a,b})
 =\frac{1}{d(a)d(b)}
  \int_{E_{a,b}}d(\tau\kappa)\,\mu_{a,b}(d\kappa)
 }
\tag{V4.5}
\]

defines a measurable probability kernel on the resolved-channel bundle, and
its target pushforward is

\[
 \boxed{
 \mathsf P^{\rm tgt}_{a,b}(A)
 =\frac{1}{d(a)d(b)}
  \int_A d(c)\,\mathsf M_{a,b}(dc)
 }.
\tag{V4.6}
\]

#### Proof

The total function \(\kappa\mapsto d(\tau\kappa)\) is nonnegative and
\(\Xi\)-measurable. For every \(E\in\Xi\), (V4.1) makes the numerator in
(V4.5) measurable in \((a,b)\); its denominator is positive and measurable.
Equation (V4.4) makes total mass one. Hence
\(\mathsf P^{\rm res}\) is a measurable probability kernel.

For every \(A\in\Sigma\), apply (V4.5) to the total event
\(\tau^{-1}A\). Equation (V4.2) gives (V4.6). Taking
\(A=\mathsf S\) proves target normalization. \(\square\)

Finite-word bracketing independence remains a theorem for the target law by
the inherited target-convolution hypotheses. A physical resolved path law
still requires a separately constructed composition category, resolved path
kernel, associators, and coherence; a one-step resolved kernel does not
supply them.

### Replacement Theorem 5 scope -- measurable gauge action

For measurable \(h:\mathsf S\to\mathbb R_{>0}\), \(h(\mathbf1)=1\), define

\[
 \mu^h_{a,b}(d\kappa)
 =\frac{h(a)h(b)}{h(\tau\kappa)}\mu_{a,b}(d\kappa),
 \qquad d^h(c)=h(c)d(c).
\tag{V4.7}
\]

If every transformed one-step measure and finite-word target convolution is
finite, then (V4.1) makes \(\boldsymbol\mu^h\) a resolved-channel kernel.
Its target pushforward is the inherited \(\mathsf M^h\), and both resolved
and target probability kernels are unchanged. The gauge does not turn a
nonmeasurable pointwise family into a kernel.

### Replacement Theorem 6 scope -- normalized representations

“Already normalized resolved channel kernel” now means a measurable
probability kernel on one declared total resolved-channel bundle. Taking
\(\mu=\mathsf P^{\rm res}\) and \(d=1\) is a representation only after that
kernel has been chosen. It does not derive the bundle, sigma algebra,
resolved distinctions, or probabilities. The target-level no-go remains
literal.

## 4. Exact rejection and positive controls

### 4.1 Nonmeasurable same-target split -- required rejection

Let \(\mathsf S=\mathbb R_{\geq0}\) with its Borel sigma algebra and let

\[
 \mathcal C_{(a,b)}=\{\kappa^0_{a,b},\kappa^1_{a,b}\},
 \qquad
 \tau(\kappa^i_{a,b})=a+b
\]

for positive \(a,b\). Give the total bundle the product Borel structure, so
the event \(E_0\) selecting channel 0 is measurable. For a non-Borel
\(V\subset(0,\infty)\), let the channel-0 weight be \(1/3\) on \(V\) and
\(2/3\) off \(V\), with the complementary channel-1 weight.

Every fiber measure is finite and positive, and the target pushforward is
the measurable associative kernel \(\delta_{a+b}\). But

\[
 (a,b)\longmapsto\mu_{a,b}((E_0)_{a,b})
\]

is nonmeasurable. Definition 10A therefore refuses this family before
Theorem 3. Coarsening \(\Xi\) so that \(E_0\) is not measurable removes the
purported resolved branching event rather than hiding its failure.

### 4.2 Same-target finite based-ring control -- required acceptance

For the version-3 two-channel control on
\(\mathsf S=\{\mathbf1,a\}\), use the finite discrete total bundle and its
full sigma algebra. Resolved counting measure is an input-measurable kernel,
the target pushforward has \(a^2=2a\), and \(d(a)=2\). The two resolved slots
have probability \(1/2\) each while the target law is deterministic at
\(a\). Every finite word is finite and target-bracketing independent.

### 4.3 Continuous same-target control -- required acceptance

Let one resolved fiber be \([0,1]\) with its Borel sigma algebra and
Lebesgue measure, with every channel targeting \(a\). On a finite discrete
input sector space this extends to a measurable total bundle and kernel. The
two half-intervals are disjoint positive-measure resolved events, every
singleton has zero probability, and the target law is deterministic. Thus
positive-family branching does not require atomic channels.

### 4.4 Non-standard measurable control -- no automatic rejection

The bundle definition does not assume regular conditional probabilities,
countable generation, or a standard-Borel base. A declared non-standard
measurable branch is admissible exactly when the total sigma algebra, kernel
event maps, target map, and required integrals are constructed directly.
Failure of a disintegration theorem blocks an attempted derivation from a
target kernel; it does not by itself forbid a primitive or otherwise
constructed resolved kernel.

## 5. Accepted Paper 13D specialization

Version 3's Paper 13D specialization remains literal. In addition, Paper 13D
does not supply a measurable total channel bundle and finite resolved kernel
over primitive, staged, fused, and disconnected whole complexes. Its
normalized history laws on fixed typed processes cannot fill that missing
structural kernel. Therefore no version-4 measure or law hypothesis is
pre-awarded.

## 6. Version-4 present product vector

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

## 7. Review boundary

Version 4 requires fresh mutually blind review of the complete composite.
No implementation, parameter choice, selector construction, or downstream
Paper 17 evaluation is authorized even if the mathematical composite is
accepted.
