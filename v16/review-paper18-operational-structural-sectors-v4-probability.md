# Paper 18 version-4 probability and identifiability review

Date: 2026-08-21

Seat: **P -- probability, projectivity, and identifiability**

Verdict: **ACCEPT**

First decisive issue: **none**.

The ordered version-2 plus version-3 plus version-4 composite is
mathematically sound on this seat. Version 4 repairs the version-3
varying-input measurability defect without erasing same-target resolved
branching. This acceptance is only of the literal mathematical contract and
its conditional theorems. It constructs no physical channel kernel, no
selector, and no downstream physical coordinate.

## 1. Integrity, scope, and blindness

I authenticated and read every assigned artifact completely. Ordinary
SHA-256, newline count, and byte count were:

| artifact | ordinary SHA-256 | lines | bytes |
|---|---:|---:|---:|
| version-2 base | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | 1165 | 41256 |
| version-3 amendment | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` | 318 | 10598 |
| version-4 amendment | `33f1e9a05bdc16b7aa96831fe1e8bc4c3bd4ca5095d2f79cbbe0c6d32abe8137` | 357 | 13093 |
| version-4 construction note | `16299722b0cefee1e4bf26ddd2b644e50461def6261d355f971b2563875c609e` | 81 | 3342 |
| version-4 review protocol | `9f3078ded7f3c91fc52efa098160a05123e77fab9a60bfb5dbbc85567c6dddd8` | 160 | 7491 |
| version-3 adjudication | `f35e91d9dd5b68aefcd75a55612f64ba15e9f1d6a30f856eb12f43ff914ec45c` | 116 | 4683 |

For the required inherited regressions, I also authenticated and read the
complete version-2 adjudication at
`172f8fa73d3f3d06703c6128bb53ccf28f11936d8210a8e1a3603a9566f8468b`
(79 lines, 2944 bytes), and authenticated the bound Paper 13D law at
`3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9`
(1285 lines, 42928 bytes) before searching its relevant generator, history,
fusion, and deletion clauses.

I did not inspect, list, contact, summarize, or infer any sibling report or
reviewer. The frozen adjudications were read only because they are binding
inputs to the composite. I wrote only this designated report and performed
no implementation, parameter fitting, downstream evaluation, repair,
staging, or commit.

## 2. P1 -- reconstruction of both prior decisive counterexamples

### Version-2 same-target failure

Take sectors \(\{\mathbf 1,a\}\), with two inequivalent resolved channels

\[
 \kappa_0,\kappa_1:a\boxtimes a\longrightarrow a.
\]

Resolved counting measure gives

\[
 \mu_{a,a}=\delta_{\kappa_0}+\delta_{\kappa_1},\qquad
 \mathsf M_{a,a}=2\delta_a.
\]

The positive character equation forces \(d(a)=2\). Hence

\[
 \mathsf P^{\rm res}_{a,a}(\kappa_i)=\frac12,
 \qquad
 \mathsf P^{\rm tgt}_{a,a}(a)=1.
\]

Version 2's requirement of different targets missed this genuine resolved
branching. Version 4 accepts it: the finite discrete dependent sum with full
sigma algebra and counting kernel satisfies every event-measurability
condition.

### Version-3 nonmeasurable varying-input failure

Let \(X=\mathbb R_{\geq0}^2\), let every fiber contain two channels
\(\kappa^0_x,\kappa^1_x\), and let both target \(a+b\) at
\(x=(a,b)\). Give \(X\times\{0,1\}\) its product Borel sigma algebra.
For a non-Borel \(V\subset(0,\infty)\), put

\[
 \mu_{a,b}(\{\kappa^0_{a,b}\})=
 \begin{cases}
  1/3,&a\in V,\\
  2/3,&a\notin V,
 \end{cases}
\]

and give channel 1 the complementary mass. Every fiber is a finite
probability space and the target pushforward is the measurable associative
kernel \(\delta_{a+b}\). Nevertheless the total channel-0 event has a
nonmeasurable probability map. If that map were Borel on \(X\), its section
at any fixed positive \(b\) would make \(V\) Borel. Definition 10A therefore
rejects the family before Theorem 3. Coarsening the sigma algebra to hide the
channel-index event removes measurable resolved plurality; it does not
repair the law.

Thus version 4 accepts exactly the first counterexample and rejects exactly
the second.

## 3. P2--P3 -- the two probability kernels

Write \(x=(a,b)\) and

\[
 g(\kappa)=d(\tau\kappa).
\]

The function \(g\) is positive and total-\(\Xi\)-measurable. For a fiber
event \(F\in\Xi_x\), choose any total event \(E\in\Xi\) with
\(E_x=F\) and define

\[
 \mathsf P^{\rm res}_x(F)
 =\frac{1}{d(a)d(b)}\int_F g\,d\mu_x.
\]

This is independent of the chosen extension because only its fiber section
is integrated. For fixed \(x\), it is a positive countably additive measure.
For every total \(E\), (V4.1), applied to
\(\mathbf 1_Eg\), makes \(x\mapsto\mathsf P^{\rm res}_x(E_x)\)
measurable. Finally,

\[
 \mathsf P^{\rm res}_x(\mathcal C_x)
 =\frac{\int d(\tau\kappa)\,\mu_x(d\kappa)}{d(a)d(b)}
 =\frac{\int d(c)\,\mathsf M_x(dc)}{d(a)d(b)}=1.
\]

Consequently (V4.5) is a resolved probability kernel, not merely a
pointwise normalized family. The argument uses indicator approximation,
nonnegative simple functions, and monotone convergence only; it imports no
standard-Borel or disintegration hypothesis.

For every \(A\in\Sigma\), its target pushforward is exactly

\[
\begin{aligned}
 (\tau_*\mathsf P^{\rm res}_x)(A)
 &=\frac1{d(a)d(b)}
   \int_{\tau^{-1}A}d(\tau\kappa)\,\mu_x(d\kappa)\\
 &=\frac1{d(a)d(b)}\int_A d(c)\,\mathsf M_x(dc)
 =\mathsf P^{\rm tgt}_x(A).
\end{aligned}
\]

This proves (V4.6), including event measurability and normalization, with no
extra regular conditional law.

## 4. P4 -- finite Frobenius--Perron probabilities

For a finite resolved counting kernel, enumerate the channels targeting
\(c\) by \(\kappa_{c,\alpha}\),
\(1\leq\alpha\leq N_{ab}^{c}\). Formula (V4.5) gives each resolved slot

\[
 \mathsf P^{\rm res}(\kappa_{c,\alpha}\mid a,b)
 =\frac{d_c}{d_ad_b}.
\]

Summing the \(N_{ab}^{c}\) equal slot masses gives

\[
 \mathsf P^{\rm tgt}(c\mid a,b)
 =\frac{N_{ab}^{c}d_c}{d_ad_b}.
\]

For a several-target check, use the rank-two finite based algebra
\(a^2=\mathbf1+2a\). Its positive character is
\(d(a)=1+\sqrt2\). At input \((a,a)\), the unit-target slot has
probability \(d(a)^{-2}\), each of the two \(a\)-target slots has
probability \(d(a)^{-1}\), and the target probabilities are
\(d(a)^{-2}\) and \(2d(a)^{-1}\). Their sum is one because
\(d(a)^2=1+2d(a)\). The same-target control instead has two positive
resolved slots but only one positive target.

## 5. P5 -- required fiber controls

All requested fiber regimes behave consistently.

1. **One target.** The two-channel \(a^2=2a\) control is accepted, with
   resolved probabilities \(1/2,1/2\) and deterministic target.
2. **Several targets.** The \(a^2=\mathbf1+2a\) control above has positive
   mass on two targets and the correct three resolved-slot probabilities.
3. **Nonatomic fiber.** On finite sector space
   \(\{\mathbf1,a\}\), take \(\mathcal C_{a,a}=[0,1]\) with Borel
   sigma algebra, Lebesgue measure, and constant target \(a\); use singleton
   unit fibers. With \(a^2=a\) and \(d=1\), the two half-intervals have
   probability \(1/2\) while every channel point has probability zero.
4. **Varying finite fibers.** The first fresh model in Section 11 has one or
   two channels according to a measurable input predicate and is a genuine
   kernel.
5. **Hybrid measurable fibers.** The second fresh model in Section 11
   switches measurably between a two-atom fiber and a Lebesgue fiber.
6. **Non-standard fiber.** Let \(I\) be uncountable and put
   \(\mathcal C_{a,a}=\{0,1\}^{I}\) with its cylinder sigma algebra and
   Bernoulli product measure, all targeting \(a\). On the finite input base,
   the total event maps are automatically measurable. This is an admissible
   non-standard resolved kernel constructed directly; no regular
   disintegration is used or needed.

## 6. P6 -- five notions that remain distinct

The composite correctly separates:

| notion | necessary datum | what it does not imply |
|---|---|---|
| set-level plurality | at least two inequivalent elements of \(\mathcal C_x\) | measurable separation or odds |
| measurable plurality | disjoint nonempty events in \(\Xi_x\) extending to total events | positive measure |
| positive-measure resolved branching | two such events of positive \(\mu_x\)-mass | different targets or occurrence of composition |
| target branching | positive target law on disjoint target events | identification of resolved channels |
| occurrence propensity | a whole-law factor \(q(a,b,\xi)\) for whether composition happens | any change in the conditional channel law |

The coarse-sigma model in Section 11 separates set plurality from measurable
plurality. The Lebesgue control separates measurable positive-family
branching from positive point masses. The same-target ring separates
resolved branching from target branching. The two-\(q\) model separates
conditional output from occurrence propensity. At \(q=0\), a displayed
conditional kernel remains counterfactual structure not identified by the
whole measure.

## 7. P7 -- target kernels do not reconstruct resolved data

A target kernel specifies only \(x\mapsto\mathsf M_x(A)\). It contains no
set \(\mathcal C\), projection \(p\), sigma algebra \(\Xi\), target map
from a resolved bundle, or resolved kernel. The two-lift model in Section 11
gives inequivalent one-channel and two-channel resolved constructions with
the same deterministic target kernel. Therefore target pushforward is
many-to-one even on finite standard spaces. On a non-standard branch there
is additionally no general right to a regular conditional disintegration.
Version 4 assumes neither reconstruction.

## 8. P8 -- measurable gauge and normalized-representation no-go

For measurable positive \(h\), the density

\[
 \frac{h(a)h(b)}{h(\tau\kappa)}
\]

is total measurable. Formula (V4.1) therefore gives measurable event maps
for \(\boldsymbol\mu^h\); strict positivity preserves nonzero fibers, while
the stated finiteness hypothesis supplies finite measures. Pushforward gives
the inherited \(\mathsf M^h\). Substitution cancels all \(h\)-factors in
both (V4.5) and (V4.6).

This gauge is nontrivial, not merely formal. For the finite algebra
\(a^2=\mathbf1+a\), let \(d(a)=\varphi\) and \(h(a)=s>0\). At \((a,a)\),
the transformed resolved weights are \(s^2\) on the unit-target channel and
\(s\) on the \(a\)-target channel, while \(d^h(a)=s\varphi\). The resulting
probabilities remain \(\varphi^{-2}\) and \(\varphi^{-1}\) at both resolved
and target levels for every \(s\).

Conversely, writing an already selected resolved probability kernel as
\(\mu=\mathsf P^{\rm res},d=1\), or a selected target Markov convolution as
\(\mathsf M=\mathsf P^{\rm tgt},d=1\), is only a representation. It derives
neither bundle nor probabilities. Version 4 states this no-go correctly at
both levels.

## 9. P9 -- target words versus resolved paths

For target convolutions, every intermediate \(d\)-factor cancels. An
\(n\)-input bracketing has final measure

\[
 \frac{d(z)}{\prod_i d(a_i)}\,\mathsf M^{(n)}(dz).
\]

The inherited assumptions make \(\mathsf M^{(n)}\) finite and independent
of target bracketing, so the target probability law has the same property.
Nothing in this argument composes resolved objects or identifies resolved
paths. The composite correctly leaves a resolved composition category,
resolved path kernel, associators, and coherence as separate constructions.

## 10. P10 -- projectivity and deletion

Uniform deletion remains

\[
 K_{n+1,n}(x,y)=\frac{m(x,y)}{n+1},
\]

not the raw multiplicity \(m\). The primary condition is
\(P_nK_{n,m}=P_m\), with Chapman--Kolmogorov composition for the deletion
kernels. Orbit, inverse-automorphism, and labeled bases retain their distinct
normalizations.

The binary count laws

\[
 P_n^{(p)}(k)=\binom nkp^k(1-p)^{n-k}
\]

are projective for every \(p\in[0,1]\), as are mixtures over \(p\).
Projectivity therefore does not identify a boundary parameter. These
deletion equations compare sizes; they neither construct nor compose a
resolved structural channel.

## 11. P11--P12 -- Paper 13D audit and fresh semantic countermodels

### Paper 13D search

For each fixed finite component family and atomic sort, Paper 13D declares
one permutation-invariant simultaneous n-ary fusion generator. Its fresh
cross-component bond values are drawn only by that generator's evaluator and
are retained in the fusion history. Any invariant of those values is a
Gamma pushforward, not a second resolved simultaneous-fusion channel.

The search did find the explicitly declared parallel whole-process syntax:
\(U_J\) versus \(D\circ Q_J^0\) have the same endpoint boundary types but
different traces and kernels, and for three or more components a deliberately
staged fusion composite is distinct from the single simultaneous n-ary
fusion. These are not hidden second simultaneous-fusion generators. The
composite already preserves them as inequivalent whole-process or resolved
path alternatives and states that Paper 13D supplies no autonomous measure
over them. They establish possible set-level alternatives, not a
measure-supported branch or selector law.

### Six fresh semantic countermodels

These models are additional to the amendment's four frozen controls.

1. **Measurably varying finite cardinality.** Let
   \(\mathsf S=\mathbb N_0\) be discrete. Put \(n(a,b)=2\) when
   \(a,b>0\) and \(a+b\) is odd, and \(n(a,b)=1\) otherwise. Set
   \(\mathcal C_{a,b}=\{0,\ldots,n(a,b)-1\}\), give it uniform mass, and
   target every element at \(a+b\). The countable total dependent sum has
   its full sigma algebra, so this is a resolved probability kernel with
   \(\mathsf M_{a,b}=\delta_{a+b}\) and \(d=1\). It refutes any inference
   that a measurable bundle must have constant fiber cardinality.

2. **Hybrid atom/continuum bundle.** Let
   \(X=\mathbb R_{\geq0}^2\), \(A=\{(a,b):a+b\leq1\}\), and
   \[
    \mathcal C=(A\times\{0,1\})\cup(A^c\times[0,1])
   \]
   with the trace Borel sigma algebra. Use half-half atomic mass on \(A\)
   and Lebesgue mass on \(A^c\), with constant fiber target \(a+b\). For a
   total Borel event \(E\), its probability is the measurable splice of two
   Borel sections on \(A\) and the parameterized Lebesgue integral on
   \(A^c\). Thus it is a genuine hybrid kernel, again with deterministic
   addition as target.

3. **Set plurality hidden by a coarse sigma algebra.** On a singleton base,
   let \(\mathcal C_x=\{\kappa_0,\kappa_1\}\) but
   \(\Xi_x=\{\varnothing,\mathcal C_x\}\). A unit-mass kernel exists, yet
   no measurable event separates the two set elements. This refutes
   set-level plurality \(\Rightarrow\) measurable or positive-measure
   branching and confirms the amendment's refusal to use an undeclared
   distinction probabilistically.

4. **Two inequivalent lifts of one target kernel.** For deterministic
   addition on \(\mathbb N_0\), one resolved bundle may have one channel per
   input, while another has two same-target channels with measurable masses
   \(1/3\) and \(2/3\). Both push forward to
   \(\delta_{a+b}\), but their resolved event algebras and laws are not
   isomorphic. This refutes target-law identifiability of the resolved
   bundle and kernel.

5. **Gauge-family nonidentifiability.** The
   \(a^2=\mathbf1+a\) family with \(h(a)=s\) constructed in Section 8 gives
   a continuum of distinct positive measure/character representatives and
   one resolved and target probability law. This refutes identification of
   \(\mu\) and \(d\) from normalized probabilities at either level.

6. **Same conditional law, different occurrence laws.** Fix any resolved
   conditional kernel and form two whole laws with composition propensities
   \(q_1=1/3\) and \(q_2=2/3\). Conditional on composition their resolved
   and target laws coincide, while their no-composition masses differ. This
   refutes identification of occurrence propensity from either conditional
   law.

## 12. P13 -- inherited probability regressions

The regressions affected by the amendments all pass.

- On \(\mathbb N_0\) addition, \(d_r(n)=r^n\), and on
  \(\mathbb R_{\geq0}\) addition, \(d_\lambda(a)=e^{\lambda a}\); every
  character in either family induces the same deterministic target law.
- The positive-character transform normalizes only after a physical
  resolved kernel and its target convolution are supplied.
- Pairwise finiteness does not replace finite-word finiteness, and target
  associativity does not replace resolved path coherence.
- A physical topology, support, groupoid, orbit census, or normalized
  representation supplies no measure provenance.
- Uniform deletion, marked restriction, and channel composition retain
  different types.
- Projective families can retain continuous parameter and mixture freedom.
- A conditional channel law does not fix \(q\), and at \(q=0\) it is not
  identified by the whole law.
- Reader labels, presentation bases, automorphism conventions, child
  histories, and retained bond values do not create resolved multiplicity.
- No accepted control promotes a current physical measure, character,
  resolved law, target law, or whole selector.

## 13. P14 -- accepted-law result versus general controls

**General conditional result accepted.** Given a constructed total resolved
bundle, finite input-measurable resolved kernel, finite associative target
pushforward, and measurable positive character, (V4.5) is a resolved
probability kernel, (V4.6) is exactly its target pushforward, and finite-word
target laws are bracketing independent. The measurable gauge and both
normalized-representation no-go statements hold.

**Current Paper 13D result accepted separately.** Its fixed simultaneous
fusion family has one resolved generator class; fresh cross-bonds are
history values. Its other explicit whole-process and staged alternatives
carry no autonomous resolved structural kernel. Hence the structural/history
fork is proved, while measure-supported branching and every selector-law
coordinate remain unconstructed.

## 14. P15 -- full version-4 product vector

No coordinate is promoted or demoted:

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

The verdict authorizes mathematical adjudication only. It does not
authorize implementation, selector construction, parameter selection,
actualization, Paper 17 evaluation, or Paper 19.
