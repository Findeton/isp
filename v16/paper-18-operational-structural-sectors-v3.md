# Paper 18 version-3 resolved-channel amendment

## Status and composition rule

The version-3 mathematical candidate is the ordered composite of:

1. the complete version-2 base
   `v16/paper-18-operational-structural-sectors-v2.md`, ordinary SHA-256
   `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614`;
   and
2. this amendment.

This amendment replaces the named version-2 definitions, theorem statements,
outcome coordinates, and scope sentences below. Every unmentioned version-2
clause remains literal. The precedence rule makes version 3 one unique
mathematical object rather than an optional commentary.

Version 3 binds the version-2 adjudication, ordinary SHA-256
`172f8fa73d3f3d06703c6128bb53ccf28f11936d8210a8e1a3603a9566f8468b`.

The amendment is result-neutral. It supplies no physical channel measure,
selector, parameter, sector type, dimension, geometry, or implementation.

## 1. Literal category and completion scopes

### 1.1 Replacement scope for version-2 Definition 8

The groupoid-valued inverse limit in version-2 Definition 8 means the
standard pseudo-limit, or descent groupoid, of the contravariant groupoid
functor. Its objects are compatible families together with specified
restriction isomorphisms satisfying the usual cocycle equation; its arrows
are compatible families of component arrows. It is not a strict set-level
equalizer.

### 1.2 Replacement heading and scope for version-2 Definition 11

The heading “history fibration” is replaced by:

> **Indexed history fibers.**

For every resolved channel object \(\kappa\), Paper 13D supplies an
equivariant indexed history fiber \(\mathsf H(\kappa)\) and normalized child
law. No Grothendieck cartesian-lifting property is claimed unless separately
constructed.

### 1.3 Completion-axis interpretation

Cardinality in version-2 Definition 9 means cardinality of point-free
isomorphism classes. The measurable-type entries are hierarchical
descriptors: finite and countable discrete spaces are also standard Borel.
The axes are independent evidence fields, not mutually exclusive labels.

## 2. Resolved channels and target pushforward

### Replacement Definition 10 -- measurable resolved channel groupoid

For each compatible input pair \((a,b)\),
\(\mathsf{Ch}(a,b)\) is the groupoid of resolved unmarked physical channel
objects. Its invariant isomorphism-class space carries the smallest declared
sigma algebra needed by physical channel observables. The target map

\[
 \tau_{a,b}:\mathsf{Ch}(a,b)\longrightarrow\mathsf S
\]

is measurable and groupoid invariant.

Two channel objects may be inequivalent even when their targets coincide.
They can differ by retained physical generator incidence, trace structure,
topological channel data if independently physical, or another exact
selector-level object. Reader names, labels, bases, and realized child
history values do not create distinct resolved channels.

### Definition 10A -- resolved channel measure

An independently physical resolved channel measure is a finite nonzero
invariant measure

\[
 \mu_{a,b}(d\kappa)
\]

on the resolved channel class space. Its provenance must be one of the
version-2 Definition-14 branches and must be fixed before conditional channel
probabilities are evaluated.

Its target convolution is the pushforward

\[
 \mathsf M_{a,b}
 =(\tau_{a,b})_*\mu_{a,b},
 \qquad
 \mathsf M_{a,b}(A)
 =\mu_{a,b}(\tau_{a,b}^{-1}A).
\tag{V3.1}
\]

When only a primitive target-level kernel \(\mathsf M\) is supplied and no
resolved \(\mu\) exists, target-sector probabilities may be discussed but
resolved-channel probabilities remain unconstructed.

### Replacement Definition 12 -- channel plurality and positive branching

There is **resolved structural plurality** at \((a,b)\) when
\(\mathsf{Ch}(a,b)\) contains at least two inequivalent independently
physical channel objects not reducible to child histories or their
coarse-grainings. Their targets may coincide or differ.

There is **nontrivial measure-supported structural branching** when an
independently physical \(\mu_{a,b}\) admits two disjoint invariant measurable
channel families \(A_0,A_1\) with

\[
 \mu_{a,b}(A_0)>0,
 \qquad
 \mu_{a,b}(A_1)>0.
\]

For a finite resolved census this reduces to at least two inequivalent
positive-weight channel objects. Distinct targets give target-sector
branching; a common target gives resolved-channel branching with a
deterministic target pushforward.

Support without a physical measure proves only plurality, not occurrence
odds. A measure on child histories proves neither plurality nor a resolved
channel law.

## 3. Resolved and target probability laws

### Replacement scope for version-2 Definition 13

The finite-word closure and associativity requirements apply to the target
pushforwards \(\mathsf M\). If resolved paths themselves are retained as
physical objects, their composition category, resolved measures,
associators, and pentagon coherence are additional required structures.

### Replacement Theorem 3 -- resolved and target positive-character laws

Suppose an independently physical resolved channel measure \(\mu_{a,b}\)
has target pushforward \(\mathsf M_{a,b}\), and a measurable positive
character satisfies

\[
 d(a)d(b)=\int_{\mathsf S}d(c)\,\mathsf M_{a,b}(dc).
\tag{V3.2}
\]

Then the resolved conditional law is

\[
 \boxed{
 \mathsf P^{\rm res}_{a,b}(d\kappa)
 =\frac{d(\tau_{a,b}(\kappa))}{d(a)d(b)}
  \mu_{a,b}(d\kappa)
 }
\tag{V3.3}
\]

and its target pushforward is

\[
 \boxed{
 \mathsf P^{\rm tgt}_{a,b}(dc)
 =\frac{d(c)}{d(a)d(b)}\mathsf M_{a,b}(dc)
 }.
\tag{V3.4}
\]

Both laws are normalized. Equation (V3.4) is exactly the version-2 target
law.

#### Proof

Integrating (V3.3) and using (V3.1) gives the right side of (V3.2) divided by
\(d(a)d(b)\), hence one. Pushing (V3.3) through \(\tau\) gives (V3.4).
Measurability follows from measurability of \(\tau\), \(d\), and the resolved
kernel. \(\square\)

Version-2 finite-word bracketing independence remains a theorem for final
target laws. Resolved path independence requires the separately retained
path-coherence data just stated.

### Replacement finite Frobenius--Perron corollary

For a finite physical resolved census with counting measure, each object
\(\kappa=(c,\alpha)\),
\(1\leq\alpha\leq N_{ab}^{c}\), has

\[
 \mathsf P^{\rm res}(c,\alpha\mid a,b)
 =\frac{d_c}{d_ad_b}.
\]

The target pushforward has

\[
 \mathsf P^{\rm tgt}(c\mid a,b)
 =\frac{N_{ab}^{c}d_c}{d_ad_b}.
\]

Thus \(N_{ab}^{c}>1\) can give nontrivial resolved-channel branching even
when only one target sector has positive probability.

### Replacement Theorem 5 scope -- resolved gauge

The version-2 \(h\)-gauge acts on resolved channel measure by

\[
 \mu^h_{a,b}(d\kappa)
 =\frac{h(a)h(b)}{h(\tau\kappa)}\mu_{a,b}(d\kappa),
 \qquad
 d^h(c)=h(c)d(c),
\]

subject to the same finite-word finiteness requirement. It pushes forward to
the version-2 \(\mathsf M^h\) and leaves both
\(\mathsf P^{\rm res}\) and \(\mathsf P^{\rm tgt}\) invariant.

### Replacement Theorem 6 scope -- representation no-go

The normalized-representation no-go applies separately at two levels.

1. Every associative target Markov convolution has
   \(\mathsf M=\mathsf P^{\rm tgt},d=1\).
2. Every already normalized resolved channel kernel whose target pushforward
   is an associative Markov convolution has
   \(\mu=\mathsf P^{\rm res},d=1\), with that target pushforward.

Neither representation derives its measure when introduced after the
probabilities are chosen.

## 4. Accepted Paper 13D specialization

For a fixed Paper 13D simultaneous-fusion component family, the unmarked
resolved channel groupoid has one generator isomorphism class and one target
class. Fresh cross-component bond values and every invariant coarse output of
them lie in its indexed history fiber. Retaining those values gives Gamma
pushforwards, not additional resolved channel objects.

Therefore the version-2 branching-fork result survives the stronger
channel-level definition. Paper 13D contains inequivalent primitive, staged,
and fused whole process complexes, but no accepted autonomous measure over
those alternatives. They witness whole-selector residue, not constructed
measure-supported branching.

## 5. Required same-target control

Let the sector set be \(\{\mathbf1,a\}\), and let
\(\mathsf{Ch}(a,a)\) contain two inequivalent resolved objects
\(\kappa_0,\kappa_1\), both targeting \(a\). With resolved counting measure,

\[
 \mu_{a,a}=\delta_{\kappa_0}+\delta_{\kappa_1},
 \qquad
 \mathsf M_{a,a}=2\delta_a.
\]

Together with the ordinary unit channels, finite-word target convolutions are
finite and associative. The character \(d(a)=2\) gives

\[
 \mathsf P^{\rm res}(\kappa_i\mid a,a)=\frac12,
 \qquad
 \mathsf P^{\rm tgt}(a\mid a,a)=1.
\]

Any definition requiring different targets fails this control. Any
definition collapsing \(\kappa_0,\kappa_1\) without an accepted channel
isomorphism also fails.

## 6. Replacement outcome coordinates

Version-2 Section 13’s single conditional-channel-law coordinate is replaced
by two independent coordinates.

### Resolved channel law

    P18-RESOLVED-CHANNEL-LAW-UNCONSTRUCTED
    P18-RESOLVED-CHANNEL-LAW-FAMILY-CONSTRUCTED
    P18-UNIQUE-RESOLVED-CHANNEL-LAW-DERIVED

### Target-sector pushforward law

    P18-TARGET-SECTOR-LAW-UNCONSTRUCTED
    P18-TARGET-SECTOR-LAW-FAMILY-CONSTRUCTED
    P18-UNIQUE-TARGET-SECTOR-LAW-DERIVED

The old umbrella label `P18-CHANNEL-LAW-UNCONSTRUCTED` is retired in version
3 because it did not specify which law was meant.

All other version-2 coordinates remain literal.

## 7. Version-3 present product vector

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

## 8. Review boundary

Version 3 requires fresh mutually blind review of the complete composite
object. No implementation or downstream Paper 17 evaluation is authorized
even if the mathematical amendment is accepted.
