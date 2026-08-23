# Paper 03 v2 hostile review — quantum instruments, probability, and histories

Date: 2026-08-22

Seat: **Q — quantum instruments, probability, histories, and Bell**

Verdict: **REVISE**

First decisive semantic counterexample:

> Definition 5.4 does not construct the claimed Heisenberg target category.
> In particular, a retained binary instrument followed by an
> outcome-controlled operation has no printed single CP arrow carrying both
> the quantum output and the classical result. Choosing one branch is not the
> semantics of the complete primitive; summing the branches erases the
> record needed by the guard. A typed direct-sum/classical-quantum boundary
> algebra and its composition law would solve this, but neither is part of
> the frozen candidate.

This is a mathematical-semantic failure, not an implementation issue and not
a counterexample to the surviving quantum probabilities.

Earliest positive supported rung: rung 4,

    P03V2-CAUSAL-FRONTIER-PROCEDURE-QUOTIENT-CONSTRUCTED

Strongest supported rung: rung 6,

    P03V2-POSITIVE-RELATIVISTIC-PREDICTIVE-REPRESENTATION-CONSTRUCTED-WITH-COSTS

The rung-7 ceiling is not earned because the paper advertises two compatible
functorial semantics, while only the Markov-kernel functor is completely
typed.

I conducted this review without opening, naming, messaging, or inferring
either sibling report. I wrote only this assigned path. I did not edit,
stage, or commit the candidate, protocol, pins, audits, authorities, code, or
ledgers.

## 0. Corpus authentication and chronology

Review began at committed HEAD
c19bd79ed2bc1ff01533352bbb99037727cd8582. This HEAD descends from the
protocol-parent commit 4568a3c6079c745df99c72b7ab0af073cb655800. Every
bound byte reproduced before scientific work.

| Artifact | Recomputed SHA-256 | LF / bytes | Status |
|---|---|---:|---|
| v17/note-paper03v2-hostile-review-protocol.md | 2b1d742b09df8e3215c8f51dd0d329222e8237400c4cd83c711a6e9e42461816 | 457 / 18,918 | exact review authority |
| v17/note-paper03v2-causal-frontier-repair-pin.md | d9df65a0bfb39576663396f75476db9c3be9413ebbd281853162411e9376ce73 | 628 / 25,109 | exact |
| v17/note-paper03v2-pin-audit.md | ccce3ca2600f9096b25686aea36db4b79a2a4b94ad66d95b8f5c1c1bbc852f91 | 274 / 10,465 | exact; nonauthoritative |
| v17/paper-03v2-causal-frontier-relativistic-adequacy.md | 93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181 | 958 / 36,711 | exact frozen candidate |
| v17/note-paper03v2-construction-audit.md | 713d8aab7a7b4f9366536316432c939174e1cc9de9965a99ad4fbb8ee1ca8694 | 228 / 9,551 | exact; nonauthoritative |
| v17/note-paper03-hostile-review-adjudication.md | 165fa3690dda1613152bfa94c2188823a296063678a5ebdea8be5dcd34e796b7 | 339 / 16,311 | exact v1 repair authority |
| v17/note-paper02v2-hostile-review-adjudication.md | 37e1ada87f17723c248896f77ce03012d809f088632abb50ed01d1b166bed135 | 381 / 19,166 | exact upstream authority |
| v17/note-paper01-hostile-review-adjudication.md | 3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1 | 314 / 13,844 | exact upstream authority |
| v17/paper-00-reality-first-programme.md | a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe | 476 / 21,268 | exact programme authority |

The chronology is valid: terminal v1 revision, v2 repair pin, pin audit,
frozen construction, construction audit, protocol, then blind review. A
later report-only commit moved HEAD without changing any bound corpus byte,
as the protocol permits.

## 1. Exact decisive counterexample

### 1.1 What is printed

Definitions 5.1–5.3 give an actual covariant functor

$$
\operatorname{Ev}_\Xi:\mathcal P_\Xi\longrightarrow\mathbf{Kern}.
$$

Its object assignment is $B_{\Xi,D}\mapsto X_D$, its primitive-arrow
assignment is the normalized state/record kernel $K_{v,m,D}$, and its
composition and identity laws are those of Markov kernels.

Definition 5.4 instead says only that

$$
\operatorname{Heis}_\Xi:
\mathcal P_\Xi^{\mathrm{op}}\longrightarrow\mathbf{CP}_\Xi
$$

exists, and describes $\mathbf{CP}_\Xi$ as a category containing
unital/nonselective maps, branch CP maps, and typed classical outputs. It
does not define:

1. the observable object assigned to a boundary with retained records;
2. whether a complete instrument is one arrow or a family of arrows;
3. the domain/codomain of an outcome-controlled continuation;
4. the composition law joining a quantum instrument to classical control;
5. identities on mixed quantum/classical boundary objects; or
6. the functor law for those arrows.

### 1.2 Minimal retained-record experiment

Take a qubit, a retained projective $Z$ instrument

$$
\mathcal J_0(A)=P_0AP_0,\qquad
\mathcal J_1(A)=P_1AP_1,
$$

and a later slot whose guard applies $I$ when $r=0$ and $X$ when $r=1$.
The correct Heisenberg operation on a later observable $A$ is

$$
\mathcal J_0(A)+\mathcal J_1(XAX).
$$

Neither candidate interpretation gives this as a functor:

- mapping the measurement primitive to one branch $\mathcal J_r$ assigns
  multiple maps to one syntactic arrow and omits the probability-bearing
  alternative;
- mapping it to $\mathcal J_0+\mathcal J_1$ discards $r$, so the next guard
  cannot choose between $I$ and $X$.

The standard construction would assign the post-measurement boundary the
classical-quantum algebra

$$
\mathcal O_{\mathrm{post}}
=\mathcal O\oplus\mathcal O,
$$

package the instrument as

$$
\widehat{\mathcal J}(A_0,A_1)
=\mathcal J_0(A_0)+\mathcal J_1(A_1),
$$

and package the controlled continuation as

$$
\widehat T(A)=(A,XAX).
$$

Then $\widehat{\mathcal J}\circ\widehat T$ gives the required operation.
That is a coherent repair, but adding the boundary observable objects and
arrow/composition definition changes the frozen mathematical referent. The
protocol explicitly classifies a missing genuine semantic target/functor law
as semantic.

### 1.3 What survives the failure

The Markov-kernel route already carries the record in $X_D$, so the same
adaptive experiment has a normalized law. Branchwise CP composition also
computes its scalar probabilities. Therefore the failure does not refute:

- the free path category;
- the operational quotient defined from complete scalar contexts;
- finite instrument CP and normalization;
- operation-level no-signalling;
- steering/Bell compatibility;
- positive history normalization; or
- prefix coherence.

It blocks the advertised second functor, its claimed intertwining under
presentation/packet transport, and rung 7 as a complete two-semantics
adequacy package.

Quantifier: **FOR-EVERY-ADMITTED-PACKET** for the counterexample whenever a
retained binary result controls a later slot; otherwise the missing target
definition remains **UNCONSTRUCTED**.

## 2. Independent quantum-probability reconstruction

### 2.1 Finite localized instruments

Quantifier: **FOR-EVERY-ADMITTED-PACKET**.

For a positive probe effect $B$,

$$
A\longmapsto A\otimes B
=(1\otimes B^{1/2})(A\otimes1)(1\otimes B^{1/2})
$$

is CP. The scattering star-automorphism is CP, and the positive slice
$\operatorname{id}\otimes\sigma$ is CP under the packet’s tensor convention.
Their composite $\mathcal J_{s,B}$ is CP. If $\sum_rB_r=1$, linearity gives

$$
\sum_r\mathcal J_{s,B_r}=\mathcal J_{s,1},
\qquad
\mathcal J_{s,1}(1)=1.
$$

Thus every input state produces a normalized finite outcome law. In a
$W^*$ packet, normality follows only when the scattering automorphism, slice,
and every registered branch/nonselective operation are normal.

### 2.2 Support, posterior typing, and closure

Quantifier: **CONDITIONAL-ON-NAMED-HYPOTHESES**.

For $p_r=\omega(\mathcal J_r(1))>0$,

$$
\omega_r(A)=\frac{\omega(\mathcal J_r(A))}{p_r}
$$

is normalized and positive. If $p_r=0$, the branch has zero measure and no
posterior is defined. Algebraic statehood does not imply membership in a
narrow packet class. The candidate therefore correctly makes closure under
positive-support, nonselective, and adaptive updates an admission condition.
Hadamard/microlocal preservation remains model-specific.

### 2.3 Standard-Borel instruments

Quantifier: **CONDITIONAL-ON-NAMED-HYPOTHESES**.

A countably additive CP-valued set function alone is not enough for every
claimed posterior kernel on an arbitrary von Neumann algebra. The packet must
supply the normalized measurable state/record kernel—or an equivalent
posterior-state theorem such as the appropriate normal-extension/measurable
posterior property. The candidate’s Definitions 5.1–5.2 impose that stronger
kernel admission. Definition 6.3 must be read through it.

The outcome law

$$
\mu_\omega(\Delta)=
\omega(\mathcal J_s(\Delta)(1))
$$

is countably additive and normalized when
$\mathcal J_s(\Omega)(1)=1$. A regular conditional posterior is determined
only almost everywhere. A nonatomic singleton of zero measure has no
canonical normalized posterior.

Okamura and Ozawa’s primary analysis of CP instruments confirms that a
strongly measurable posterior family is a substantive property, not an
automatic consequence for every CP instrument:
https://arxiv.org/abs/1501.00239.

### 2.4 Sequential law and retained records

Quantifier: **FOR-EVERY-ADMITTED-PACKET** for the Markov semantics and
branchwise probability law; **UNCONSTRUCTED** for the advertised Heisenberg
functor with classical output.

For chronological operations $1$ then $2$, state kernels compose as
$K_2\circ K_1$, while scalar branch probabilities use
$\omega(\mathcal J_1\circ\mathcal J_2(1))$. This order is correct.
Zero-support terms vanish before conditioning. An adaptive continuation is
well defined in $\operatorname{Ev}_\Xi$ because retained record values are
coordinates of $X_D$.

The primary Fewster–Verch source independently supports the CP
pre-instrument, causally ordered composition, and equality of the two orders
for causally disjoint coupling regions under causal factorization:
https://arxiv.org/abs/1810.06512.

### 2.5 Nonselective no-signalling and selective steering

Quantifier for no-signalling: **FOR-EVERY-ADMITTED-PACKET** within the named
localized remote-reader domain.

Completeness and operation locality give

$$
\sum_a p(a,b\mid\omega)
=\omega(\mathcal J_{A,1}(D_b))
=\omega(D_b).
$$

This is an identity for the nonselective operation on the remote observable,
not a consequence of one-state commutation and not a statement about a
selected branch.

Quantifier for steering: **FINITE-CALIBRATION-CONTROL**.

For positive support, $p(b\mid a)$ may differ from $p(b)$, while summing over
$a$ restores the marginal. Comparing selected ensembles requires the
retained classical result. The split singlet is a separated type-I
calibration, not a generic tensor decomposition of touching QFT regions.

### 2.6 Bell scope and sources

Quantifier: **EXISTS-ONE-NAMED-COMPARATOR** plus
**FINITE-CALIBRATION-CONTROL**.

The split-qubit arithmetic gives $S=2\sqrt2$ with unbiased marginals for one
fixed singlet source used across settings. Excluding Bell-local
factorization additionally requires measurement independence: the source
measure may not vary with $x,y$. A correlated source or setting-dependent
preparation is a different packet and defeats that inference.

The Summers–Werner result supplies existential commuting QFT
observable/state Bell violations under its hypotheses:
https://doi.org/10.1007/BF01207366. It does not supply an exact localized
probe coupling for every ideal observable. The candidate keeps existence,
finite calibration, and exact-probe realization separate.

### 2.7 Positive histories and prefix coherence

Quantifier: **FOR-EVERY-ADMITTED-PACKET** with supplied normalized measurable
kernels.

For finite outcomes,

$$
K_i(r,d\lambda'\mid\lambda)
=p_i(r\mid\lambda)\,
\delta_{U_i(\lambda,r)}(d\lambda')
$$

is a positive substochastic branch kernel, and summing $r$ gives a normalized
kernel. Iterating complete kernels therefore gives a normalized history
measure. Repeatedly integrating the final complete kernel removes the suffix;
induction returns the literal prefix law.

The history must include retained records and any complete predictive/process
memory. Equal reduced quantum states with different retained records need not
have equal future profiles. Conversely, a lower-set frontier alone is not a
division. Only the full future-sufficient boundary licenses restart.

### 2.8 Contextuality and idle fibers

Quantifier for preparation contextuality:
**FINITE-CALIBRATION-CONTROL**.

With the same complementary state,

$$
\tfrac12\delta_{|0\rangle\langle0|}
+\tfrac12\delta_{|1\rangle\langle1|}
\ne
\tfrac12\delta_{|+\rangle\langle+|}
+\tfrac12\delta_{|-\rangle\langle-|},
$$

although both complete global barycenters agree. The witness is in the
predictive-state support, not in a procedure-name tag.

Quantifier for idle fibers: **FOR-EVERY-ADMITTED-PROJECTION** at the declared
scope. Tensoring with an ignored normalized standard probability space
preserves all registered laws. This proves nonselection only for that
admitted idle projection; it neither creates the fiber nor assigns a
preferred prior.

## 3. Common structural reconstruction

The following common duties were independently checked to locate the
surviving product.

1. **FOR-EVERY-ADMITTED-PACKET:** algebras transport covariantly and states
   pull back contravariantly; no proper-embedding state pushforward exists.
2. **FOR-EVERY-ADMITTED-PACKET:** lower sets and enabled slots type causal
   frontiers; the non-down-closed later-first boundary is absent.
3. **FOR-EVERY-ADMITTED-PACKET:** a primitive extends one enabled slot;
   explicit skip and empty-path identity have different targets.
4. **FOR-EVERY-ADMITTED-PACKET:** the free path category has literal units,
   associative concatenation, and total composition for matching objects.
5. **CONDITIONAL-ON-NAMED-HYPOTHESES:** incomparable exchange is added only
   after full map/kernel factorization with source lineage exposed.
6. **FOR-EVERY-ADMITTED-PACKET:** adjacent certified swaps give one
   probability law for finite linear extensions; no topological-sort index is
   retained.
7. **FOR-EVERY-ADMITTED-PACKET:** presentation renaming preserves
   multiplicity, supports, causal incidence, mechanisms, records, sources,
   states, and readers.
8. **FOR-EVERY-ADMITTED-PACKET:** complete operational equivalence is a
   congruence within the constructor-closed reachable packet interface.
9. **FOR-EVERY-ADMITTED-PACKET:** full packet isomorphism transports every
   field. Equality of coordinates or scalars is insufficient.
10. **REFUSAL/NONIMPLICATION:** type-III, split, Reeh–Schlieder, gauge,
    particles, continuum, UV, frame, division, actuality, and geometry walls
    remain correctly scoped.

The v1 same-boundary timelike defect is genuinely repaired. No second
composition predicate survives. The new semantic failure is downstream: the
contravariant target of the otherwise valid path category is incomplete.

## 4. V2-T1–V2-T20 target matrix

| Target | Required label | Independent disposition | Exact boundary / first failure |
|---|---|---|---|
| V2-T1 | FOR-EVERY-ADMITTED-PACKET | constructed | finite declared slot poset; frontier is a lower set |
| V2-T2 | FOR-EVERY-ADMITTED-PACKET | constructed | each primitive fills exactly one enabled slot |
| V2-T3 | FOR-EVERY-ADMITTED-PACKET | constructed | free path category; total matched composition, units, associativity |
| V2-T4 | FOR-EVERY-ADMITTED-PACKET | constructed | later-first timelike word absent by lower-set type |
| V2-T5 | CONDITIONAL-ON-NAMED-HYPOTHESES | constructed for complete Kern/branch maps | full map causal factorization and source premise; Heis categorical equality unconstructed |
| V2-T6 | FOR-EVERY-ADMITTED-PACKET | constructed operationally | adjacent certified swaps give equal complete kernels/scalars |
| V2-T7 | FOR-EVERY-ADMITTED-PACKET | constructed on syntax/Kern; incomplete on Heis | multiplicity preserved; claimed Heis intertwiner has no defined target objects |
| V2-T8 | FOR-EVERY-ADMITTED-PACKET | constructed scoped | complete registered one-hole contexts absorb constructors |
| V2-T9 | FOR-EVERY-ADMITTED-PACKET | constructed scoped | reachable within-packet quotient; new readers may refine |
| V2-T10 | CONDITIONAL-ON-NAMED-HYPOTHESES | admission condition, not derived selector | positive-support, nonselective, adaptive closure; model-specific narrow classes |
| V2-T11 | FOR-EVERY-ADMITTED-PACKET | constructed with kernel scope | finite POVM normalization; continuous result only for supplied normalized measurable kernels |
| V2-T12 | FOR-EVERY-ADMITTED-PACKET | constructed for syntax/Kern/scalars; incomplete on Heis | every packet field must intertwine; no proper-embedding pushforward |
| V2-T13 | CONDITIONAL-ON-NAMED-HYPOTHESES | constructed | Fewster–Verch comparison plus named Haag property/substitute |
| V2-T14 | FOR-EVERY-ADMITTED-PACKET + control | constructed | nonselective remote marginal; selected steering plus record |
| V2-T15 | EXISTS-ONE-NAMED-COMPARATOR + FINITE-CALIBRATION-CONTROL | constructed as compatibility | measurement independence explicit; universal exact probe unconstructed |
| V2-T16 | FOR-EVERY-ADMITTED-PACKET | constructed at Markov/branchwise scalar scope | normalized positive histories and prefixes; categorical Heis compatibility not established |
| V2-T17 | REFUSAL/NONIMPLICATION | constructed | lower-set frontier alone is not future sufficiency |
| V2-T18 | FOR-EVERY-ADMITTED-PACKET | constructed scoped | no undeclared scheduling frame; physical/KMS rest frame allowed |
| V2-T19 | REFUSAL/NONIMPLICATION or named conditional | constructed | no density/tensor/model collage |
| V2-T20 | UNCONSTRUCTED | correctly unconstructed | ontology, actuality, spacetime, gravity |

## 5. Quantifier ledger

| Positive or refusal statement | Label | Forbidden promotion |
|---|---|---|
| lower-set path category | FOR-EVERY-ADMITTED-PACKET | laboratory poset is fundamental chronology |
| Markov-kernel semantics | FOR-EVERY-ADMITTED-PACKET | every reduced frontier is a division |
| Heisenberg functor with classical outputs | UNCONSTRUCTED | vague typed-output phrase is a target category |
| finite branch CP/normalization | FOR-EVERY-ADMITTED-PACKET | arbitrary CP map is localized |
| W* normality and state closure | CONDITIONAL-ON-NAMED-HYPOTHESES | every algebraic update preserves the physical class |
| continuous-outcome posterior kernel | CONDITIONAL-ON-NAMED-HYPOTHESES | every CP instrument has point posteriors |
| causal factorization | CONDITIONAL-ON-NAMED-HYPOTHESES | spacelike-looking supports imply map equality |
| no-signalling | FOR-EVERY-ADMITTED-PACKET | Bell factorization or selected-branch invariance |
| steering | FINITE-CALIBRATION-CONTROL | record-free superluminal communication |
| QFT Bell existence | EXISTS-ONE-NAMED-COMPARATOR | universal exact-probe construction |
| split CHSH | FINITE-CALIBRATION-CONTROL | generic QFT tensor factorization |
| positive history | FOR-EVERY-ADMITTED-PACKET | selected local microontology |
| preparation contextuality | FINITE-CALIBRATION-CONTROL | procedure-name ontic tag |
| idle-fiber theorem | FOR-EVERY-ADMITTED-PROJECTION | fiber existence or uniform prior |
| type/continuum/frame/ontology walls | REFUSAL/NONIMPLICATION or UNCONSTRUCTED | model collage, actuality, spacetime, gravity |

## 6. Controls C1–C28 in both directions

| ID | Positive direction reconstructed | Hostile direction reconstructed | Result / coordinate |
|---|---|---|---|
| C1 | completed set is a lower set | non-down-closed set is not an object | pass / frontier |
| C2 | primitive extends one enabled slot | successor before predecessor has no generator | pass / boundary |
| C3 | alternative mechanisms share exact interface | physical mechanism is not erased as a coordinate rename | pass / procedure |
| C4 | empty path is identity | explicit skip consumes a slot and changes target | pass / procedure |
| C5 | incomparable paths reach one frontier | arbitrary rank/loop index is absent | pass / slot-skeleton |
| C6 | full factorizing maps exchange | correlated or linked sources are different mechanisms | pass / causal-factorization |
| C7 | timelike order lies in source/target types | reverse word is absent without partial composition | pass / procedure |
| C8 | distinct slot occurrences retain multiplicity | isomorphic occurrences are not collapsed | pass / presentation |
| C9 | guard reads an earlier retained record | future-result guard is ill typed | pass / record |
| C10 | frozen context family is constructor closed | omitted constructor invalidates congruence | pass scoped / quotient |
| C11 | packet isomorphism moves all fields | equal scalars or coordinates alone do not | pass / covariance |
| C12 | proper embedding gives state pullback | canonical forward state extension refused | pass / covariance |
| C13 | normal class-preserving update admitted | nonnormal/out-of-class update rejected | pass conditional / state-class |
| C14 | normalized measure kernel admitted | null singleton posterior refused | pass conditional / instrument |
| C15 | independent probes expose product source | correlated source not relabeled independent | pass / source lineage |
| C16 | complete localized operation fixes remote effect | commutator slogan alone insufficient | pass / no-signalling |
| C17 | selected steering uses retained result | selected conditional not called marginal | pass / steering |
| C18 | Bell premises are separate | microcausality not Bell factorization | pass / bell |
| C19 | contingent state/apparatus may define rest frame | covariance not fixed-state invariance | pass / preferred-frame |
| C20 | topological serialization is idle | hidden idle microstructure not excluded | pass / preferred-frame |
| C21 | algebraic functionals and CP maps suffice | generic density/trace/Kraus/tensor refused | pass / type-III |
| C22 | split calibration requires separated collar | touching-region factorization refused | pass / split |
| C23 | global predictive history is positive | local explanatory microontology refused | pass / positive-model |
| C24 | retained record is typed | record is neither actuality nor automatically division | pass / record/division |
| C25 | comparator geometry is declared | emergent spacetime not inferred | pass / input |
| C26 | relative Cauchy evolution is response | no metric law or gravity inferred | pass / downstream |
| C27 | slots are laboratory protocol positions | discrete-universe ontology refused | pass / slot-skeleton |
| C28 | physical procedure context survives | run token/procedure name not an ontic label | pass / context |

Control C9 also locates the decisive gap: its probability direction passes in
Kern, but its claimed complete Heisenberg-instrument direction requires the
missing classical-quantum object and composition law.

## 7. Hostile attacks 1–40

1. **Reproduce the v1 same-boundary pair:** blocked; the two timelike arrows
   have different frontier endpoints.
2. **Delete $D$:** destroys the boundary type and category repair.
3. **Use a non-down-closed frontier:** no such object is admitted.
4. **Insert later slot first:** no enabled primitive exists.
5. **Add a second composition predicate:** absent; matching paths always
   concatenate.
6. **Equate skip and identity:** their codomains differ.
7. **Physicalize a topological-sort index:** no such field occurs.
8. **Collapse isomorphic occurrences:** presentation action is bijective and
   multiplicity preserving.
9. **Exchange source-correlated slots:** full factorization/source premise
   fails.
10. **Exchange record-linked slots:** they are dependent and not exchange
    generators.
11. **Future result enables past slot:** guard typing refuses it.
12. **Omit a context constructor:** Theorem 9.3 then fails rather than passing.
13. **Gauge away physical support:** presentation groupoid forbids it.
14. **Move coordinates only:** not a packet isomorphism.
15. **Push a state forward through proper embedding:** no canonical map is
    supplied.
16. **Transport without scattering intertwiner:** fails packet isomorphism.
17. **Use a nonnormal W* update:** outside the admitted packet.
18. **Leave the state class after positive support:** violates Definition 2.3.
19. **Normalize zero support:** refused; zero mass has no posterior.
20. **Normalize a nonatomic singleton:** refused; conditioning is a.e.
21. **Hide probe/source correlation:** changes the source mechanism/packet.
22. **Infer no-signalling from commutation:** theorem instead uses the
    complete localized operation identity.
23. **Call selected conditional a marginal:** explicitly separated.
24. **Hide communication in postselection:** retained result is a physical
    classical resource.
25. **Treat QFT Bell observable as exact probe:** universal realization remains
    unconstructed.
26. **Collage Bell, split, free-field, and gauge controls:** quantifier ledger
    keeps models separate.
27. **Give every local state a density matrix:** algebraic functional
    formulation refuses it.
28. **Tensor-factor touching regions:** split use requires separation/collar.
29. **Turn Reeh–Schlieder density into control:** norm, success,
    postselection, and record costs remain.
30. **Infer a universal natural/Hadamard state:** state is contingent and
    narrow classes require preservation proof.
31. **Erase a KMS/material rest frame:** Proposition 13.2 blocks the
    inference.
32. **Exclude hidden preferred structure from schedule equality:** explicitly
    refused.
33. **Call slots microscopic happenings:** repeatedly refused.
34. **Count slots as volume or duration:** no such valuation exists.
35. **Call predictor a local Bell variable:** it is global, contextual, and
    instrument indexed.
36. **Call a stable record complete division:** future sufficiency is a
    separate test.
37. **Call conditioning/decoherence actuality:** no selector is supplied.
38. **Import v16 geometry/selector/fusion:** no such input is used.
39. **Infer interacting 3+1 QFT:** the net theorem is abstract conditional
    mathematics.
40. **Open Paper 04/gravity:** downstream remains closed.

All numbered attacks remain typed after the semantic-functor failure and are
therefore dispositioned rather than omitted.

## 8. Fresh Seat-Q attacks

| ID | Exact attack | Independent result |
|---|---|---|
| Q1 | Give a finite branch $r$ zero probability and nevertheless normalize $\omega\circ\mathcal J_r$. | Refused: the branch is zero measure and has no posterior. |
| Q2 | Request a posterior at a specified point of a nonatomic continuous outcome. | Refused: only the supplied measure kernel and a.e. regular conditional are admitted. |
| Q3 | Retain a binary result and let the next enabled slot apply $I$ or $X$ according to it. | **Decisive:** Kern carries the record, but the printed $\mathbf{CP}_\Xi$ has no classical-quantum object/arrow composition that represents the complete adaptive operation. |
| Q4 | Choose incomparable instruments that commute only on one input state. | Refused: exchange requires full complete-map/kernel equality on the admitted domain. |
| Q5 | Report $p(b\mid a)$ after selection as Bob’s nonselective marginal. | Refused: marginalization sums $a$; steering retains and communicates the record. |
| Q6 | Correlate the Bell source with future settings while retaining the standard CHSH inference. | The attack defeats Bell-local exclusion; the valid control must use one setting-independent source, and a correlated source is a different packet. |
| Q7 | Take a Summers–Werner local observable and declare its exact probe coupling already built. | Refused: QFT observable existence is separate from localized-probe realization. |
| Q8 | Use two histories with the same current reduced state but different retained records, then identify their future profiles. | Refuted by a record-controlled continuation; $X_D$ must retain the records and the frontier alone is not a division. |
| Q9 | Use a normal CP instrument on a von Neumann algebra that lacks a measurable posterior family. | A CP-valued measure alone is insufficient; the packet must supply the stronger measurable kernel/NEP-type property. Candidate passes only under that admission scope. |
| Q10 | Reverse the Heisenberg order while leaving the state recursion chronological. | Two noncommuting timelike instruments then give different probabilities; the candidate’s branchwise order $\mathcal J_1\circ\mathcal J_2$ is correct. |
| Q11 | Forget Alice’s result and replace her complete map by the identity on all future observables. | False in the causal future; identity is asserted only on registered spacelike remote observables. |
| Q12 | Use a source-correlated pair of probes inside the product-source factorization proof. | The proof fails; it is a separately typed joint mechanism and cannot be relabeled independent. |
| Q13 | Match only local barycenters while complementary global states differ, then claim preparation equivalence. | Insufficient. The contextuality control passes because it fixes the same complementary state and hence the complete global barycenter. |
| Q14 | Markovize two memoryful histories using only the same reduced current state. | Future profiles may differ; the complete conditional process object and records are required. |

## 9. Full 31-coordinate product

    input                 BOUND
                          + SCOPE: TERMINAL P01/P02V2, V1 REPAIR AUTHORITY,
                            DECLARED AQFT PACKETS
    slot-skeleton         DECLARED-LABORATORY-PROTOCOL
                          + SCOPE: NOT MICROSCOPIC TIME OR ONTOLOGY
    frontier              CONSTRUCTED-TYPE
                          + SCOPE: LOWER SET, NOT AUTOMATIC DIVISION
    boundary              CONSTRUCTED
                          + SCOPE: PORTS, RECORDS, PREDICTIVE/READER TYPES
    procedure             CONSTRUCTED
                          + FREE PATH CATEGORY; V1 DEFECT REPAIRED
    presentation          CONSTRUCTED-SCOPED
                          + HEISENBERG INTERTWINING UNCONSTRUCTED
    quotient              CONSTRUCTED-SCOPED
                          + REACHABLE WITHIN-PACKET COMPLETE CONTEXTS
    covariance            CONSTRUCTED-CONDITIONALLY
                          + FULL PACKET/KERN TRANSPORT; HEIS TARGET GAP
    state-class           DECLARED-CLOSURE-CONDITIONAL
                          + MODEL-SPECIFIC NORMAL/HADAMARD PRESERVATION
    instrument            BRANCH-CP-AND-KERNEL-CONSTRUCTED
                          + COMPLETE CLASSICAL-OUTPUT HEIS CATEGORY UNCONSTRUCTED
    causal-factorization  CONSTRUCTED-CONDITIONALLY
                          + FULL MAP/KERNEL EQUALITY AND SOURCE PREMISES
    spacelike-schedule    CONSTRUCTED-OPERATIONALLY
                          + COMPLETE KERNEL/SCALAR LAW
    no-signalling         CONSTRUCTED
                          + COMPLETE NONSELECTIVE LOCALIZED OPERATION
    steering              CONSTRUCTED-CONTROL
                          + SELECTED CONDITIONAL AND RECORD COST
    bell                  CONSTRUCTED-EXISTENTIAL-COMPATIBILITY
                          + FIXED SOURCE; UNIVERSAL EXACT PROBE UNCONSTRUCTED
    positive-model        CONSTRUCTED-WITH-COSTS
                          + GLOBAL, CONTEXTUAL, MEMORY-BEARING, UNSELECTED
    context               CONSTRUCTED
                          + SAME-SLOT PREDICTIVE-SUPPORT WITNESS
    fibers                CONSTRUCTED-SCOPED
                          + ADMITTED POSITIVE AFFINE IDLE PROJECTIONS
    type-III              REFUSAL-CONSTRUCTED / MODEL-SPECIFIC
    split                 CONDITIONAL-CONTROL
                          + SEPARATED COLLAR AND SPLIT/NUCLEARITY
    gauge                 TYPED-UNSELECTED
    particles             TYPED-UNSELECTED
    continuum             ABSTRACT-NET-CONDITIONAL
                          + NO INTERACTING 3+1 CONSTRUCTION
    UV                    SCOPED
                          + NO HIDDEN CUTOFF OR UNPROVED REMOVAL
    preferred-frame       NO-UNDECLARED-SCHEDULING-FRAME
                          + PHYSICAL REST FRAMES AND IDLE STRUCTURE ALLOWED
    record                CONSTRUCTED-OPERATIONALLY
                          + CLASSICAL OUTPUT COMPLETE IN KERN, NOT IN HEIS TARGET
    division              FUTURE-SUFFICIENCY-REQUIRED
                          + FRONTIER ALONE INSUFFICIENT
    actuality             UNCONSTRUCTED
    barandes              ADMISSIBLE-BUT-INCOMPLETE
    ontology              GLOBAL-PREDICTIVE-CANDIDATE-UNSELECTED
                          + NOT LOCAL EXPLANATORY MICROPHYSICS
    downstream            CLOSED
                          + NO PAPER 04, CLOCKS, SPACETIME, OR GRAVITY

The product has 31 coordinates in the protocol order.

## 10. Verdict, rung, and repair-weight ledger

### Verdict

**REVISE.**

The causal-frontier repair succeeds, and the quantum probability subpackage
is strong. The one semantic defect is exact and local: the claimed
contravariant Heisenberg semantics with retained classical outputs is not a
defined category/functor. Because the abstract and main theorem claim two
compatible semantics, this is not a citation qualifier.

The strongest surviving cumulative result is rung 6:

    P03V2-POSITIVE-RELATIVISTIC-PREDICTIVE-REPRESENTATION-CONSTRUCTED-WITH-COSTS

Rung 7 requires the missing typed Heisenberg construction. Rungs 8–9 remain
unavailable for the independent ontology/empirical reasons already printed.

### Bounded fixes and scope clarifications

1. State explicitly in Definition 6.3 that
   $\mathcal J_s(\Omega)(1)=1$; normalization is already imposed by the
   packet kernel but should appear beside the CP-valued measure.
2. Bind continuous-outcome posterior claims to a supplied strongly measurable
   posterior kernel/normal-extension property, not to CP countable additivity
   alone.
3. State explicitly that the split CHSH source is the same preparation for
   every setting pair and is independent of the setting randomizers.
4. Continue to label the Summers–Werner theorem as observable/state existence,
   not exact-probe realization.
5. Clarify that “persistent classical output” means retained output; the
   constructor family also includes discard/coarse-graining.

### Semantic repair required

Define the complete boundary observable target before claiming
$\operatorname{Heis}_\Xi$. At minimum the successor must provide:

1. an observable object $\mathcal O_D$ for each quantum/classical boundary;
2. a complete instrument as one normalized CP arrow, for finite records
   naturally $\bigoplus_r\mathcal O_{D'}\to\mathcal O_D$;
3. standard-Borel classical-output objects and normal instrument maps at the
   declared measurable scope;
4. controlled/read/discard/coarse-grain arrows;
5. identity and composition laws;
6. proof that primitive source/target interfaces match;
7. functoriality under path concatenation; and
8. compatibility with $\operatorname{Ev}_\Xi$, exchange, presentation, and
   packet transport.

This repair does not require retuning any probability or physical parameter,
but it changes a mathematical object and therefore needs a successor rather
than an edit to the frozen candidate.

Paper 04 remains closed pending joint adjudication and user authorization.

## 11. Final reauthentication and report state

At freeze, the candidate again reproduced SHA-256
93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181.
Every other corpus hash in Section 0 remained exact. This report is
LF-terminated, contains no trailing whitespace, is unstaged and uncommitted,
and contains no sibling-report information. Its ordinary SHA-256, LF count,
and byte count are reported externally after the final byte is fixed. No
circular self-hash is embedded.
