# Paper 18 version-5 observable-freeze amendment

## Status and composition rule

The version-5 mathematical candidate is the ordered composite of:

1. the complete version-2 base, ordinary SHA-256
   `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614`;
2. the binding version-3 amendment, ordinary SHA-256
   `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd`;
3. the binding version-4 amendment, ordinary SHA-256
   `33f1e9a05bdc16b7aa96831fe1e8bc4c3bd4ca5095d2f79cbbe0c6d32abe8137`;
   and
4. this amendment.

Later amendments have precedence only for clauses they explicitly replace.
Every other clause remains literal. The ordered composite is one
mathematical object.

Version 5 binds the version-4 adjudication, ordinary SHA-256
`5671861f1db4a8070bc604c87d0aa7f57f3a2d173d2094a3edd9865b6f19f11f`.

This amendment is result-neutral. It selects no sigma algebra, observable,
channel, measure, coupling, sector family, selector, dimension, or geometry.
It corrects the interpretation of coarse total sigma algebras and freezes
physical channel observables before any candidate measure is tested.

## 1. Pre-measure physical referent

### Definition 10B -- frozen resolved-channel observable contract

Before a candidate resolved-channel kernel is proposed, one must freeze the
**resolved-channel observable contract**

\[
 \mathfrak R=(\mathcal C,\Xi,p,\tau,\mathcal O).
\]

Here \((\mathcal C,\Xi,p,\tau)\) is the version-4 measurable bundle, and
\(\mathcal O\) is the declared family of physically meaningful
resolved-channel descriptors. Each descriptor

\[
 \ell:\mathcal C\longrightarrow L_\ell
\]

must be \(\Xi\)-measurable, invariant under accepted presentation changes,
and grounded in retained physical incidence, trace, topology if independently
physical, or another exact channel-level property. Reader names, arbitrary
labels, bases, representatives, and realized child histories remain
inadmissible descriptors.

The contract obeys four rules.

1. **Freeze before measure.** The total sigma algebra and every descriptor
   used to state or test a probability must be fixed before
   \(\boldsymbol\mu\), \(d\), or either normalized law is evaluated.
2. **No post-hoc coarsening.** A predeclared physical descriptor cannot be
   removed from \(\Xi\) because its event probabilities fail measurability.
3. **No post-hoc refinement.** An external cross-fiber label absent from
   \(\mathfrak R\) cannot be added after seeing \(\boldsymbol\mu\) and used
   to declare an otherwise valid kernel nonmeasurable.
4. **No forced trivialization.** The contract need not number, trivialize, or
   globally identify all channel classes across different inputs. A
   nontrivial measurable bundle and purely local channel identities are
   allowed.

Two choices of \(\Xi\) or \(\mathcal O\) are generally two different
physical referent proposals. They are equivalent only if an accepted
measurable bundle isomorphism transports every physical descriptor and every
experiment. Equality of their individual fiber sigma algebras is not enough.

The observable freeze does not construct a measure. It prevents the
observable algebra from being tuned to rescue or reject a proposed measure.

## 2. Three distinct branching predicates

### Replacement Definition 12 -- local, coherent, and target branching

Let \(x=(a,b)\).

1. **Set-level resolved plurality at \(x\).** The fiber \(\mathcal C_x\)
   contains at least two inequivalent independently physical channel classes
   not reducible to histories or coarse-grainings. This predicate requires no
   measure.

2. **Pointwise measure-supported resolved branching at \(x\).** For an
   independently physical resolved kernel, there are disjoint
   \(A_0,A_1\in\Xi_x\) with
   \[
    \mu_x(A_0)>0,
    \qquad
    \mu_x(A_1)>0.
   \tag{V5.1}
   \]
   Because \(\Xi_x\) is the trace algebra, both events extend to total
   measurable events. No common cross-input name for them is implied.

3. **Descriptor-coherent resolved branching on a declared input region
   \(B\subseteq X\).** A predeclared descriptor
   \(\ell\in\mathcal O\), disjoint measurable descriptor events
   \(D_0,D_1\subseteq L_\ell\), and a measurable \(B\) satisfy
   \[
    \mu_x(\ell^{-1}D_0\cap\mathcal C_x)>0,
    \qquad
    \mu_x(\ell^{-1}D_1\cap\mathcal C_x)>0
   \tag{V5.2}
   \]
   for every \(x\in B\). This stronger predicate tracks the same physical
   channel property across the declared inputs. The positivity sets are
   measurable by the kernel axiom.

4. **Target-sector branching at \(x\).** The target pushforward gives
   positive probability to two disjoint target events. This is independent
   of whether the resolved branching is pointwise or descriptor coherent.

The unqualified phrase **nontrivial measure-supported structural branching**
in the present Paper 18 product vector means pointwise resolved branching at
at least one admitted complete input. Any theorem needing the same branch
type across inputs must explicitly require descriptor-coherent branching.

Set-level plurality still supplies no odds. Pointwise branching supplies no
global branch identity. Descriptor coherence supplies no measure unless a
kernel is independently physical. Resolved branching with a common target
still need not produce target-sector branching.

## 3. Correct coarse-sigma interpretation

### Replacement for version-4 Section 4.1

Consider the two same-target channels over
\(X=\mathbb R_{\geq0}^2\) with an external set-theoretic index
\(i\in\{0,1\}\), and let their displayed weights exchange according to a
non-Borel subset of the first input coordinate.

There are two different physical referent proposals.

#### 3.1 The channel index is predeclared physical

If the frozen contract includes a measurable descriptor

\[
 \ell(x,i)=i,
\]

then \(E_0=\ell^{-1}\{0\}\in\Xi\). Its probability is the non-Borel weight
function, so the family fails the version-4 event-kernel axiom. Coarsening
\(\Xi\) after discovering this failure violates the no-post-hoc-coarsening
rule.

#### 3.2 The channel index is not a physical cross-input descriptor

Let \(\Xi_c\) contain diagonal cylinders over measurable base sets and their
countable modifications. It induces the full discrete sigma algebra on each
two-point fiber and admits point-local events, but the uniform index event
\(X\times\{0\}\) is not measurable. If every admitted total-event
probability is measurable, the family is a valid kernel on this different
observable contract. It has pointwise resolved branching at every input but
no descriptor-coherent “channel 0 versus channel 1” branching across a
nontrivial input region.

The non-Borel displayed weight is then attached only to an external
cross-fiber numbering absent from the physical referent. It is not the
probability of a physical total event. Adding that numbering after the fact
violates the no-post-hoc-refinement rule.

Thus a coarse sigma algebra does not automatically hide a failed physical
law, and it does not automatically cure one. The decisive question is
whether the omitted cross-fiber distinction was independently frozen as a
physical observable before the measure.

## 4. Measurable-kernel theorems remain literal

Version 4's event/integration equivalence, target pushforward, Theorem 3,
gauge action, and normalized-representation no-go remain literal. They are
theorems relative to the frozen observable contract \(\mathfrak R\).

In particular:

- a kernel is tested against every event of the frozen \(\Xi\);
- the target pushforward cannot reconstruct omitted resolved distinctions;
- neither measurability nor descriptor coherence supplies physical weights;
- no regular conditional probability is inferred on a non-standard branch;
  and
- changing \(\Xi\) or \(\mathcal O\) changes the candidate referent rather
  than gauge-transforming a fixed probability law.

## 5. Required controls

### 5.1 Predeclared-index rejection

On the full product-Borel bundle, freeze the index descriptor before the
non-Borel split. The candidate must be refused because the probability of
\(\ell=0\) is nonmeasurable.

### 5.2 Legitimate coarse-bundle acceptance

On the countable-modification coarse bundle, do not declare a uniform index
descriptor. The event-kernel family is accepted as pointwise branching. It
must not be promoted to descriptor-coherent channel-index branching.

### 5.3 Post-hoc sigma tuning rejection

Starting from 5.1, deleting the index event after seeing the kernel is
forbidden. Starting from 5.2, adding the external index after seeing the
kernel is also forbidden. Either change requires a new referent proposal and
a fresh independent law evaluation.

### 5.4 Nontrivial bundle control

A two-sheet bundle with no predeclared, presentation-invariant physical sheet
descriptor may support pointwise branching, whether or not an auxiliary
mathematical numbering can be chosen. A theorem about a transported channel
species may use only independently physical, transition-compatible
measurable descriptors, not a convenient sheet numbering. Paper 18 must not
force a global physical trivialization merely to make probabilities easy to
write.

### 5.5 Prior positive controls

The finite same-target based ring, continuous same-target Lebesgue family,
varying finite Borel fibers, hybrid atomic/nonatomic fiber, and directly
constructed non-standard cylinder kernel remain required positive controls.

## 6. Accepted Paper 13D specialization

Paper 13D supplies neither a total structural-channel observable contract
over all whole-process alternatives nor an autonomous resolved-channel
kernel on such a contract. Therefore version 5 cannot decide whether its
future structural channels possess only local identities or
descriptor-coherent families. Its fixed simultaneous-fusion family still
has one resolved generator class, while fresh bonds remain indexed history
values.

No measure, selector, or branching coordinate is promoted.

## 7. Version-5 present product vector

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

Version 5 requires a fresh mutually blind review of the complete composite.
Acceptance authorizes only terminal mathematical adjudication. No
implementation, selector construction, parameter selection, Paper 17
evaluation, or spacetime claim is authorized.
