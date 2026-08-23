# Paper 03 hostile review — Seat A

## AQFT, category, and covariance

Date: 2026-08-22

Seat: A

Status: **FROZEN BLIND REPORT**

Verdict: **REVISE**

Earliest supported rung: **rung 4**

Strongest supported rung:

~~~text
P03-RELATIVISTIC-NOSIGNALLING-OPERATIONAL-SUBPACKAGE-CONSTRUCTED
~~~

## 1. Authentication, chronology, and blindness

I authenticated the following frozen corpus before scientific review.

| artifact | SHA-256 | LF lines | bytes |
|---|---|---:|---:|
| hostile-review protocol | c3b387e53b14efd9d705d911a3ea717cce9395103f073e9fddbc46c1b7f78f9e | 263 | 10472 |
| Paper 03 pin | 0486f7ce04bc70c5f14d7609e4baf9244dc02195248d45d66ccb3c8a46813696 | 694 | 30954 |
| pin audit | 2ee41bfa77e8c919b71dca4a66e780a1f1e71220a133b7d71c39a3153e59bf8f | 338 | 14336 |
| Paper 03 candidate | 6506c950ec26354e063960631aaabfb759216ddf0822f3be8057dad2250036af | 1068 | 46560 |
| construction audit | bdabe5b9aa4331b43dc4c1b2b8bfb0db6bed673268aa27fa8ce88e2e5e1a27ef | 302 | 12476 |
| Paper 01 terminal adjudication | 3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1 | 314 | 13844 |
| Paper 02 v2 terminal adjudication | 37e1ada87f17723c248896f77ce03012d809f088632abb50ed01d1b166bed135 | 381 | 19166 |
| Paper 02 v2 candidate | d92787631860e9dcc7379a5922a4213585571d61f98a2a1fb82aa1dc18ba2a77 | 1400 | 60916 |
| empirical contract | c5f628dc17a739ae73e2ceb97410625b58722ca51b8e8de0d37c6aa0df92d82f | 437 | 17521 |
| v17 charter | a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe | 476 | 21268 |

The review HEAD was
d30b3b4ce1c6c14a2bf9710c06d587e0575c7613, exactly the committed
protocol HEAD. The construction-audit commit was
ff2493443fe7bb3d0fda539e52bd46f2e4cb7d02; the protocol HEAD descends
from it. The protocol hash and all bound corpus hashes matched.

I read the entire bound corpus and the relevant primary AQFT sources. I did
not inspect, name, message, or infer either sibling report. I reviewed only
the AQFT/category/covariance lens assigned to Seat A. I did not edit the
candidate, pin, audits, code, ledgers, or prior papers.

## 2. Verdict and first decisive semantic counterexample

### 2.1 The printed physical-procedure object is not a category

Definition 5.1, candidate lines 392--402, types a boundary by

$$
(M,\mathcal A,\mathfrak S,\text{open probe ports},
 \text{classical records},\text{reader domain}).
$$

It contains no executed causal down-set, causal frontier, support profile, or
other field that distinguishes an earlier boundary from a later boundary on
the same spacetime. Definition 5.2, lines 404--421, nevertheless says both:

1. $\mathcal P_{\rm rel}$ is a category; and
2. composition exists only if boundary types match **and** causal wiring is
   allowed, while reversing timelike order may be inadmissible.

That conjunction violates the category axiom that every pair of morphisms
with matching codomain and domain has a composite.

Here is an exact admitted counterexample. Fix one legal boundary type $B$ on
one comparator spacetime, with no open probe port and no retained outcome.
Use a compact localized coupling in an earlier region $K_-$, then complete
its probe instrument and discard its outcome. This is an admitted morphism

$$
F_-:B\longrightarrow B.
$$

Do the same for a later timelike-related compact region $K_+$:

$$
F_+:B\longrightarrow B,
\qquad K_-\prec K_+.
$$

Both arrows have exactly the printed source and target type. If
$\mathcal P_{\rm rel}$ is a category, both $F_+\circ F_-$ and
$F_-\circ F_+$ must exist. Definition 5.2 licenses the first and declares
the reversed timelike wiring different or inadmissible. Therefore its
composition is an extra partial operation not determined by object typing.
The declared $\mathcal P_{\rm rel}$ is not a category.

This is not a complaint about Python, notation, or an absent citation. It
invalidates the categorical premise of Proposition 5.4 and Theorem 5.6.
Consequently the printed quotient category and its ordinary universal
property are not constructed. T10's factorization through $q_{\rm rel}$ is
also not established.

The physically honest repair has two possible forms:

1. enrich each boundary object by a causal frontier/executed down-set so that
   the forbidden reverse pair is not composable by type; then reprove
   identities, associativity, constructor closure, presentation action, and
   quotient congruence; or
2. state that the referent is a partial category, causal operad, event
   structure, or suitable double category and rebuild the quotient in that
   structure.

Either changes a central definition and theorem. It is a semantic revision.

### 2.2 What survives the counterexample

The defect does not refute the fixed-packet localized system--probe
subconstruction. The following remain independently valid under the printed
packet hypotheses:

- the Loc/Alg variance convention;
- the induced positive/CP pre-instrument;
- finite-outcome normalization and zero-support discipline;
- causal factorization assumed for a named finite scheme;
- adjacent-swap schedule independence for a causally disjoint family;
- nonselective no-signalling from operation localization;
- selective steering with an explicit record/communication cost;
- Bell compatibility as an existential comparator control;
- the refusal of regional density matrices and tensor factors in generic
  type-III settings;
- the conditional split and Reeh--Schlieder controls; and
- the no-state-selection, no-background-independence, and no-actuality
  firewalls.

This supports rung 4, not rung 5 or higher.

## 3. Independent AQFT reconstruction

### 3.1 Variance and state transport

The candidate correctly defines Loc objects as oriented, time-oriented,
globally hyperbolic Lorentzian spacetimes and Loc arrows as orientation- and
time-orientation-preserving isometric embeddings with causally convex image.
The algebra functor is covariant,

$$
\mathcal A:\mathbf{Loc}\to\mathbf{Alg},
$$

whereas states pull back contravariantly:

$$
\psi^*\nu=\nu\circ\mathcal A(\psi).
$$

Thus

$$
(\psi^*\nu)(A)=\nu(\mathcal A(\psi)A)
$$

is well typed. The refusal of a canonical state extension along a proper
embedding is correct. The time-slice axiom is not confused with dynamical
locality, and local covariance is not promoted to background independence.

There is, however, a second semantic incompleteness below the first kill.
The candidate never defines the class of “admitted packet morphisms” used by
its covariance product. Proposition 2.4 transports one observable-state
evaluation, and Proposition 5.4 treats comparator isomorphisms, but the
candidate supplies no general intertwining data for the probe theories,
coupled theory, coupling region, scattering map, probe state, effects,
control/record tree, reader domain, predictive object, and measurable history
map along a proper Loc embedding. Theorem 6.5's phrase “covariantly transported
packets” is consequently not a defined construction. Full packet covariance
is unproved even though the elementary evaluation identity is correct.

### 3.2 State-class closure

Definition 2.3 explicitly requires closure under state pullback. It does not
explicitly require closure under every registered positive-support posterior
or nonselective channel. This matters for composability.

Take a pullback-stable but narrow admitted class containing a state $\omega_0$,
and choose an admitted instrument for which
$U_{s,B}(\omega_0)\notin\mathfrak S(M)$. Theorem 3.3 proves that the result is
a state on the algebra; it does not prove membership in the declared state
class. The next branch kernel is then outside its typed domain.

The packet contract must require, and each model must verify,

$$
\omega\in\mathfrak S(M),\ p_s(B\mid\omega)>0
\Longrightarrow U_{s,B}(\omega)\in\mathfrak S(M),
$$

together with closure under the nonselective maps actually used. Normal
locally normal classes can often satisfy this under normal localized CP maps;
a narrower Hadamard or other microlocal class needs its own preservation
proof.

### 3.3 Scattering convention and localized instruments

The convention at lines 179--182 is internally consistent with the
Fewster--Verch convention: the scattering automorphism maps outgoing
uncoupled observables to incoming representatives. With
$\eta_\sigma=\operatorname{id}\otimes\sigma$,

$$
\mathcal J_{s,B}(A)
=\eta_\sigma\!\left(\Theta(A\otimes B)\right)
$$

is CP for positive $B$ on the packet's fixed system--probe tensor product:
$A\mapsto A\otimes B$, $\Theta$, and $\eta_\sigma$ are CP. A complete POVM
sums to $\mathcal J_{s,1}$, and unitality gives total probability one.
The construction correctly keeps a zero functional at zero support.

The Heisenberg order in Theorem 6.3 is also consistent: if physical operation
1 precedes operation 2, state updates compose as
$\mathcal I_2\circ\mathcal I_1$, while the dual observable maps occur as
$\mathcal J_1\circ\mathcal J_2$ inside the initial state.

Theorem 3.4's attribution is too compressed. The induced-observable
localization result requires the exact localized coupled/uncoupled comparison
hypotheses and, in the standard theorem, a Haag-property hypothesis or an
explicit substitute for the system theory. Those premises should be printed,
not hidden inside “localized-coupling hypotheses.” This is bounded if the
packet already contains them; otherwise it is a missing hypothesis.

### 3.4 Causal factorization and no-signalling

For a finite family whose composite scattering scheme is assumed to satisfy
causal factorization, map-level commutation for causally disjoint couplings
supports the adjacent-incomparable-swap proof. Equality on one state would not
suffice, and the candidate correctly demands equality on the full registered
domain.

The no-signalling proof is the right operation theorem:

$$
\sum_a\mathcal J_{A,B_a}=\mathcal J_{A,1},
\qquad
\mathcal J_{A,1}(D_b)=D_b
$$

for a remote reader $D_b$. It does not infer no-signalling from a commutator
alone. The selective conditional can differ without enabling control because
the outcome is not selected and comparison requires the retained classical
record.

The exact source of the independent product-probe construction used in the
multi-probe factorization should be printed. This is a source/scope repair,
not a refutation of the conditional fixed-family theorem.

### 3.5 Presentation action and operational quotient

The physical-versus-presentation table is conceptually sound: chart changes,
bound-name changes, reassociation, disjoint exchange after map-level proof,
and complete transport along comparator isomorphisms may be presentation;
coupling regions, causal relations, interactions, states, effects, records,
and accessible sectors may not.

But Proposition 5.4 only proves descent for individual finite programs under
the named isomorphisms and disjoint swaps. It does not define a functorial
action on the full packet family. More decisively, because
$\mathcal P_{\rm rel}$ is not a category, the ordinary categorical quotient
and universal property in Theorem 5.6 do not follow.

The definition of operational equivalence has the right complete-tester
intent. Its substitution proof is the usual congruence argument only after
the context family has been proved closed under every well-typed constructor.
The untyped causal admissibility gate prevents that proof as written.

### 3.6 Type III, split property, and covariance scope

The type-III firewall is correct: a local normal state need not be represented
by a density matrix internal to the regional algebra; normal CP maps do not
generically have a finite Kraus family; and commuting or touching regional
algebras need not be tensor factors.

The split statement is correctly conditional on a separated collar
$O_1\Subset O_2$ and a type-I intermediate factor

$$
\mathcal R(O_1)\subset\mathcal N\subset\mathcal R(O_2).
$$

It is not evidence for a lattice. The candidate correctly refuses to apply
this to touching regions or arbitrary gauge systems.

The no-natural-state firewall is substantively correct, but its theorem scope
must retain all hypotheses: dynamical locality, extended locality, and a
faithful Reeh--Schlieder-type representation in the relevant no-go result.
Relative Cauchy evolution measures response to background perturbations; it
does not make the metric a quantum dynamical variable.

## 4. Complete theorem-target matrix

| target | quantifier | Seat A result | reason |
|---|---|---|---|
| T1 comparator typing | FOR-EVERY-ADMITTED-PACKET | PASS-WITH-SCOPE | Loc/Alg and represented objects are separated; packet update closure is missing |
| T2 local covariance | CONDITIONAL-ON-NAMED-HYPOTHESES | PARTIAL | evaluation naturality passes; full packet morphisms are undefined |
| T2b state-class covariance | CONDITIONAL-ON-NAMED-HYPOTHESES | FAIL | pullback closure is printed, posterior/instrument closure is not |
| T3 localized measurement | CONDITIONAL-ON-NAMED-HYPOTHESES | PASS-WITH-SCOPE | CP and normalization pass; localization must expose Haag/local-comparison premise |
| T4 causal factorization | CONDITIONAL-ON-NAMED-HYPOTHESES | PASS | valid for the admitted factorizing finite family |
| T5 nonselective no-signalling | CONDITIONAL-ON-NAMED-HYPOTHESES | PASS | complete local operation fixes remote readers |
| T6 steering/signalling | EXISTS-ONE-NAMED-COMPARATOR | PASS | conditional difference and record cost are separated |
| T7 schedule independence | CONDITIONAL-ON-NAMED-HYPOTHESES | PASS | adjacent swaps of incomparable map-level operations |
| T8 Bell compatibility | EXISTS-ONE-NAMED-COMPARATOR | PASS-WITH-SCOPE | compatibility control, not universal exact-probe realization |
| T9 positive history | CONDITIONAL-ON-NAMED-HYPOTHESES | PARTIAL | fixed finite program works; state closure and packet covariance remain open |
| T10 context/idle fibers | CONDITIONAL-ON-NAMED-HYPOTHESES | FAIL-AS-PRINTED | factorization through a quotient category lacks a category |
| T11 type-III refusal | REFUSAL/NONIMPLICATION | PASS | no generic trace, density, finite Kraus, or tensor factor |
| T12 split independence | CONDITIONAL-ON-NAMED-HYPOTHESES | PASS | separated collar and split hypothesis retained |
| T13 Reeh--Schlieder control | CONDITIONAL-ON-NAMED-HYPOTHESES | PASS | density is not deterministic controllable preparation |
| T14 gauge firewall | REFUSAL/NONIMPLICATION | PASS | observable/field/sector/edge types remain separate |
| T15 identical-particle firewall | REFUSAL/NONIMPLICATION | PASS | no labeled particles, generic Fock space, or particle number |
| T16 continuum/UV | REFUSAL/NONIMPLICATION | PASS | abstract-net conditional; cutoff controls not ontology |
| T17 preferred-frame test | CONDITIONAL-ON-NAMED-HYPOTHESES | PASS-AT-FIXED-PACKET-SCOPE | no serialization frame; full packet covariance unproved |
| T18 ontology/actuality | REFUSAL/NONIMPLICATION | PASS | predictive histories are not selected microontology |

## 5. Quantifier ledger

| positive statement | mandatory quantifier | exact scope |
|---|---|---|
| Loc/Alg variance identity | FOR-EVERY-ADMITTED-PACKET | every typed Loc arrow and pulled-back registered state |
| state pullback closure | FOR-EVERY-ADMITTED-PACKET | declared packet premise, not a selected natural state |
| posterior state membership | UNCONSTRUCTED | algebraic statehood is proved; membership in the declared class is not |
| full packet covariance | UNCONSTRUCTED | no admitted packet-morphism category/intertwiners are defined |
| induced CP instrument | CONDITIONAL-ON-NAMED-HYPOTHESES | fixed tensor product, scattering automorphism, positive probe effect |
| localization | CONDITIONAL-ON-NAMED-HYPOTHESES | local comparison plus Haag property or exact substitute |
| causal factorization | CONDITIONAL-ON-NAMED-HYPOTHESES | admitted finite schemes satisfying factorization |
| disjoint schedule independence | FOR-EVERY-ADMITTED-PACKET | every registered factorizing disjoint family |
| no-signalling | FOR-EVERY-ADMITTED-PACKET | complete nonselective localized instruments and remote readers |
| steering control | FINITE-CALIBRATION-CONTROL | named split/type-I two-qubit control |
| Bell compatibility | EXISTS-ONE-NAMED-COMPARATOR | named Bell-capable AQFT comparator; not every model/state |
| physical procedure category | UNCONSTRUCTED | printed causal admissibility is partial beyond object typing |
| operational quotient category | UNCONSTRUCTED | depends on the failed procedure category |
| fixed-program positive history | CONDITIONAL-ON-NAMED-HYPOTHESES | finite registered programs with measurable, state-closed updates |
| contextual preparation witness | FINITE-CALIBRATION-CONTROL | named split finite-subalgebra construction |
| idle-fiber nonselection | FOR-EVERY-ADMITTED-PACKET | only explicitly admitted idle extensions/projections |
| type-III/tensor claims | REFUSAL/NONIMPLICATION | model-specific positive theorems only |
| split property | CONDITIONAL-ON-NAMED-HYPOTHESES | collar, nuclearity/split assumptions |
| Reeh--Schlieder | CONDITIONAL-ON-NAMED-HYPOTHESES | representation-specific density theorem |
| no operational preferred frame | CONDITIONAL-ON-NAMED-HYPOTHESES | fixed registered packet and schedule interface only |
| state/ontology/actuality selection | UNCONSTRUCTED | no universal state, ontology, or branch-selection law |

## 6. R1--R32 controls in both directions

| ID | positive direction | hostile/refusal direction | result |
|---|---|---|---|
| R1 | evaluation commutes with algebra push/state pull | scalar coincidence without intertwiners is insufficient | PARTIAL: packet-level intertwiners missing |
| R2 | disjoint couplings commute as full maps | one-state or loop equality rejected | PASS |
| R3 | timelike order retained | reversal differs or is inadmissible | PASS physically; exposes category failure |
| R4 | complete local instrument summed | selective branch is not no-signalling | PASS |
| R5 | selective steering exhibited | no record-free controlled signal | PASS |
| R6 | named CHSH value $2\sqrt2$ | commutation does not imply Bell factorization | PASS-SCOPED |
| R7 | compact localized coupling | no global hypersurface collapse | PASS |
| R8 | factorized finite causal family | impossible noncausal update refused | PASS |
| R9 | algebraic/normal states | no generic regional density/tracial formula | PASS |
| R10 | normal CP operations where represented | no generic finite Kraus family | PASS |
| R11 | separated split inclusion | no touching/arbitrary tensor factorization | PASS |
| R12 | cyclic-density theorem retained | no deterministic remote preparation | PASS |
| R13 | fields/sectors are typed | labeled-particle ontology refused | PASS |
| R14 | observable/field/gauge data separated | naive Gauss tensor factor refused | PASS |
| R15 | retained result changes boundary | forgotten result is distinct | PASS |
| R16 | zero support has zero mass | no normalized zero-support posterior | PASS |
| R17 | performed prefix fixed | later unperformed choice cannot alter prefix | PASS |
| R18 | independent probes require product source | correlated source is another preparation | PASS |
| R19 | Bell control uses entanglement | no-signalling assumes no separability | PASS |
| R20 | Loc comparator transports observables/states | metric remains declared | PARTIAL: full packet transport undefined |
| R21 | time-slice supports scattering | no internal clock/orientation derived | PASS |
| R22 | theorem is abstract-net conditional | no interacting 3+1 existence | PASS |
| R23 | named free-field probe example possible | not Standard Model or gravity | PASS |
| R24 | cutoff may be a calibration | no continuum/discreteness promotion | PASS |
| R25 | fixed-program global positive law | no relativistically local microontology | PASS-WITH-STATE-CLOSURE-SCOPE |
| R26 | admitted idle frame fiber definable | existence or equiprobability not inferred | PASS |
| R27 | physical preparation pair | coordinate tags forbidden | PASS |
| R28 | record is persistent program field | not division or actualization | PASS |
| R29 | complete registered testers define equivalence | new readers may refine it | FAIL-AS-CATEGORICAL-QUOTIENT |
| R30 | product and closure printed | no Paper 04/gravity promotion | PASS refusal; promoted rung fails |
| R31 | state pullback class is covariant | no preferred state family | PARTIAL: instrument closure missing |
| R32 | Hadamard is model-specific admissibility | no universal vacuum/cosmological selector | PASS |

## 7. Hostile attacks 1--76

The following dispositions are independent checks, not adoption of the
candidate's table.

| attack | Seat A disposition |
|---:|---|
| 1 | BLOCKED: abstract algebra, represented normality, and measurable state domains are distinguished |
| 2 | BLOCKED: coordinates are presentation only |
| 3 | BLOCKED: active spacetime symmetries are not silently gauge |
| 4 | BLOCKED: orientation and time orientation remain comparator data |
| 5 | BLOCKED: non-causally-convex embeddings are outside Loc |
| 6 | BLOCKED: presentation action may not move a physical coupling region |
| 7 | BLOCKED: run tokens are excluded from procedure identity |
| 8 | BLOCKED for a fixed complete program by prefix marginalization |
| 9 | BLOCKED: reader family freezes with the packet |
| 10 | PARTIAL: scalar naturality is right, but full packet intertwiners are undefined |
| 11 | BLOCKED: no global inverse from reachable quotient is claimed |
| 12 | BLOCKED: retained and discarded records have distinct boundary types |
| 13 | BLOCKED: no global Lüders hypersurface appears |
| 14 | BLOCKED: localization requires system--probe or separately certified local CP construction |
| 15 | BLOCKED: no-signalling uses operation locality |
| 16 | BLOCKED: selective conditional and nonselective marginal are separated |
| 17 | BLOCKED: zero-support branch stays a zero functional |
| 18 | BLOCKED: discard applies the nonselective channel, not identity in its future |
| 19 | COUNTEREXAMPLE TO CATEGORY: timelike reversal is forbidden despite matching printed boundaries |
| 20 | BLOCKED within a factorizing disjoint family by map-level adjacent swaps |
| 21 | BLOCKED: equality is required as maps, not in one state |
| 22 | BLOCKED: reader localization is typed |
| 23 | BLOCKED: source/probe correlations must be explicit |
| 24 | BLOCKED: postselection comparison consumes a classical record channel |
| 25 | BLOCKED subject to the exact localization hypotheses |
| 26 | BLOCKED for a complete fixed program by shared-prefix marginal equality |
| 27 | BLOCKED: microcausality is not Bell factorization |
| 28 | BLOCKED: no-signalling is not all Bell conditional independence |
| 29 | BLOCKED: measurement independence is an explicit control premise |
| 30 | BLOCKED: global predictive object is not called a local ontic state |
| 31 | BLOCKED: commuting algebras are not inferred separable |
| 32 | BLOCKED: CHSH violation is compatible with nonselective no-signalling |
| 33 | BLOCKED on the registered disjoint family; calculation order is operationally idle |
| 34 | BLOCKED: idle preferred microstructure remains possible |
| 35 | BLOCKED: entropy needs separately typed factorization and UV prescription |
| 36 | BLOCKED: cyclic density is not controlled finite-probability remote preparation |
| 37 | BLOCKED: no universal regional density matrix |
| 38 | BLOCKED: no universal finite Kraus representation |
| 39 | BLOCKED: touching local algebras are not tensor-factorized |
| 40 | BLOCKED: split claims retain collar and split/nuclearity hypotheses |
| 41 | BLOCKED: type-I interpolation is not a lattice |
| 42 | BLOCKED: observable and charged field algebras are separated |
| 43 | BLOCKED: Gauss-law, center, and edge data are not discarded |
| 44 | BLOCKED: Wilson/flux localization must be model supplied |
| 45 | BLOCKED: identical-particle labels are not physical |
| 46 | BLOCKED: Fock space and particle number are regime inputs |
| 47 | BLOCKED: spin/statistics needs sector and spectrum hypotheses |
| 48 | BLOCKED: superselection does not actualize a branch |
| 49 | BLOCKED: no procedure-name ontic tag in the predictive object |
| 50 | BLOCKED: global predictor is not explanatory microphysics |
| 51 | BLOCKED: restart is licensed only at future-sufficient boundaries |
| 52 | BLOCKED: future-postselected state is not substituted for a physical prefix |
| 53 | BLOCKED in the fixed model by affine mixture construction |
| 54 | BLOCKED: independent probes require declared product source |
| 55 | BLOCKED: nonlinear barycenter erasure is not an admitted representation map |
| 56 | BLOCKED: only exposed idle fibers are projected away |
| 57 | BLOCKED: entropy/dimension/coding length selects no ontology |
| 58 | BLOCKED: no uniform prior over completions is inferred |
| 59 | BLOCKED: recorded result selects no microscopic history |
| 60 | BLOCKED: conditioning/decoherence is not actualization |
| 61 | BLOCKED: abstract conditional theorem gives no interacting 3+1 construction |
| 62 | BLOCKED: free-field example is not universal field dynamics |
| 63 | BLOCKED: any cutoff is labeled as a control |
| 64 | BLOCKED: cutoff removal requires convergence/renormalization |
| 65 | BLOCKED: mode lattice is not spacetime ontology |
| 66 | BLOCKED: external Loc comparator is not emergent spacetime |
| 67 | BLOCKED: comparator time orientation is not internal time |
| 68 | BLOCKED: relative Cauchy evolution is not metric dynamics or gravity |
| 69 | BLOCKED: v16 dimension/metric/FLRW objects are not imported |
| 70 | BLOCKED: local covariance is distinguished from background independence |
| 71 | BLOCKED: downstream clocks remain closed by protocol |
| 72 | BLOCKED: operational adequacy is not a complete theory of reality |
| 73 | BLOCKED with exact no-natural-state theorem hypotheses retained |
| 74 | BLOCKED: Hadamard condition is not a unique vacuum selector |
| 75 | BLOCKED: dynamical locality is not inferred from covariance/time-slice |
| 76 | BLOCKED: $\omega$ is contingent declared input, not law-selected output |

## 8. Assigned fresh attacks A1--A8

### A1 — proper embedding without canonical state extension

Choose a proper Loc embedding $\psi:M\to N$ and a state in
$\mathfrak S(M)$. The candidate correctly supplies only the pullback
$\mathfrak S(N)\to\mathfrak S(M)$ and does not invent a canonical extension.
**Disposition: passed refusal.** It also confirms that the undeclared
packet-level forward transport in Theorem 6.5 cannot be assumed.

### A2 — inverse scattering conventions mixed

Recompute the induced observable and two-step Heisenberg composite using the
candidate's single outgoing-to-incoming $\Theta$ convention. No inverse is
silently inserted, and the branch order is consistent. **Disposition:
blocked.**

### A3 — one-state equality without instrument commutation

Take two CP maps that agree after evaluation in one invariant state but do not
commute as maps. Such an example cannot satisfy Theorem 4.2 item 2, which
requires equality on the full registered algebra for every outcome pair.
**Disposition: blocked by the printed map-level hypothesis.**

### A4 — non-causally-convex embedding

An isometric embedding whose image is not causally convex is not a Loc
morphism under Definition 2.1 and cannot be used as a local inclusion.
**Disposition: blocked by type.**

### A5 — state class not closed under registered posterior

Let $\mathfrak S(M)$ be pullback stable but narrow and choose an admitted
instrument with $U_{s,B}(\omega)\notin\mathfrak S(M)$. Definition 2.3 does
not block it. **Disposition: semantic incompleteness.** Instrument closure
must be an explicit packet axiom and model theorem.

### A6 — context family not closed under one constructor

Insert an operationally equivalent pair into a purported same-boundary
timelike composite. The context is accepted in the physical order and rejected
in the reverse order by an admissibility condition not represented in the
boundary type. The “substitute into every constructor” proof therefore lacks
a category of contexts on which closure can be stated. **Disposition:
counterexample; same root as the first decisive issue.**

### A7 — split inclusion without a collar

Remove $O_1\Subset O_2$. Proposition 8.2 no longer applies and the candidate
does not infer a type-I factor. **Disposition: blocked by its named
hypotheses.**

### A8 — relative Cauchy evolution promoted to metric dynamics

Relative Cauchy evolution compares response to compact perturbations of a
declared background. Candidate lines 761--772 explicitly refuse a metric
probability law, constraint algebra, Einstein dynamics, and backreaction.
**Disposition: blocked.**

### Additional Seat A attack — matched boundaries with forbidden composition

The pair $F_-,F_+:B\to B$ constructed in Section 2 is admitted individually
but cannot be composed in every category-required order. **Disposition:
decisive semantic counterexample.**

## 9. Full 31-coordinate product

| coordinate | Seat A status | exact boundary |
|---|---|---|
| input | BOUND | accepted upstream architecture plus declared AQFT packet |
| spacetime-comparator | DECLARED-STANDARD | fixed-dimensional oriented/time-oriented globally hyperbolic background |
| algebra-net | DECLARED-STANDARD | functor supplied; no interacting model derived |
| state-class | DECLARED-PULLBACK-TYPED / INSTRUMENT-CLOSURE-UNCONSTRUCTED | no preferred natural state |
| procedure | UNCONSTRUCTED-AS-CATEGORY | causal composition is partial beyond source/target typing |
| presentation | CONSTRUCTED-ON-INDIVIDUAL-PROCEDURES | full categorical action unproved |
| quotient | UNCONSTRUCTED-AS-QUOTIENT-CATEGORY | base category fails |
| covariance | EVALUATION-NATURALITY-CONSTRUCTED / FULL-PACKET-MORPHISMS-UNCONSTRUCTED | proper-embedding state pushforward refused |
| time-slice | INHERITED-COMPARATOR | scattering support; no internal time |
| instrument | CONSTRUCTED-CONDITIONALLY | localized system--probe CP pre-instruments |
| causal-factorization | CONSTRUCTED-CONDITIONALLY | only admitted factorizing finite schemes |
| spacelike-schedule | CONSTRUCTED | finite linear extensions agree by adjacent swaps |
| no-signalling | CONSTRUCTED | complete nonselective local operation |
| steering | CONSTRUCTED-CONTROL | selected conditional plus record cost |
| bell | CONSTRUCTED-EXISTENTIAL-CONTROL | compatibility, not universal realization |
| positive-model | FIXED-FINITE-PROGRAM-CONSTRUCTED-WITH-COSTS | state closure/full covariant family unconstructed |
| context | PHYSICAL-PROCEDURE-WITNESS-CONSTRUCTED / q-FACTORIZATION-UNCONSTRUCTED | categorical dependence |
| fibers | CONSTRUCTED-SCOPED | fixed admitted history models only |
| type-III | REFUSAL-CONSTRUCTED / MODEL-SPECIFIC | no generic density, trace, tensor |
| split | CONDITIONAL-CONTROL | separated collar and split/nuclearity hypotheses |
| gauge | TYPED-UNSELECTED | no group or sector spectrum derived |
| particles | TYPED-UNSELECTED | Fock/asymptotic interpretation conditional |
| continuum | ABSTRACT-NET-CONDITIONAL | no interacting 3+1 construction |
| UV | SCOPED | no hidden cutoff or uncontrolled removal |
| preferred-frame | NO-SERIALIZATION-FRAME-ON-CERTIFIED-FIXED-PACKETS | full covariant packet claim unproved; idle frames not excluded |
| record | CONSTRUCTED-OPERATIONALLY | typed retained classical outcome |
| actuality | UNCONSTRUCTED | no branch-selection rule |
| barandes | ADMISSIBLE-BUT-INCOMPLETE | no universal configuration/law/trajectory packet |
| ontology | GLOBAL-PREDICTIVE-CANDIDATE-UNSELECTED | not local explanatory microphysics |
| downstream | CLOSED | no clocks, emergence, matter--geometry, or gravity |
| overall ceiling | RUNG-4 | P03-RELATIVISTIC-NOSIGNALLING-OPERATIONAL-SUBPACKAGE-CONSTRUCTED |

## 10. Outcome ladder

| rung | outcome | Seat A disposition |
|---:|---|---|
| 1 | P03-RELATIVISTIC-COMPARATOR-TYPE-FAILURE | surpassed |
| 2 | P03-LOCALIZED-EXPERIMENT-REFERENT-UNCONSTRUCTED | surpassed for fixed schemes |
| 3 | P03-CAUSAL-FACTORIZATION-UNPROVEN | surpassed conditionally |
| 4 | P03-RELATIVISTIC-NOSIGNALLING-OPERATIONAL-SUBPACKAGE-CONSTRUCTED | supported |
| 5 | P03-LOCALLY-COVARIANT-QFT-OPERATIONAL-QUOTIENT-CONSTRUCTED | not supported |
| 6 | P03-POSITIVE-RELATIVISTIC-PREDICTIVE-REPRESENTATION-CONSTRUCTED-WITH-COSTS | partial fixed-program salvage only |
| 7 | P03-LOCALLY-COVARIANT-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT | not supported |
| 8 | P03-RELATIVISTIC-LOCAL-MICROONTOLOGY-CONSTRUCTED-WITH-COSTS | not supported |
| 9 | P03-EMPIRICALLY-DISCRIMINATED-RELATIVISTIC-ONTOLOGY | not supported |

The earliest supported rung in the sense of the first nonfailure positive
outcome is rung 4. It is also the strongest supported rung.

## 11. Bounded fixes versus semantic repairs

### Bounded fixes

1. Candidate line 551 prints \!left( rather than \!\left(.
2. Theorem 3.4 should name the Haag-property or exact substitute used by its
   induced-observable localization theorem.
3. Theorem 4.2 should cite the exact independent product-probe causal
   factorization source.
4. The no-natural-state statement should print its dynamical-locality,
   extended-locality, faithfulness, and Reeh--Schlieder hypotheses.
5. Every isomorphism-gauge sentence should say explicitly that the entire
   packet, not merely the background and algebra, is transported.

### Semantic repairs

1. Replace the false category with a correctly typed causal category or an
   explicitly partial categorical structure, then reconstruct associativity,
   contexts, presentation action, quotient congruence, and universal property.
2. Define the category/class of admitted packet morphisms and all
   intertwiners needed for full covariant packet and history transport.
3. Add and prove closure of every admitted state class under every registered
   positive-support posterior and nonselective update.

These repairs alter theorem content or declared types. They cannot be made in
this report and should not be classified as code defects.

## 12. Primary-source checks

I checked the following primary sources against the candidate rather than
using secondary summaries:

- Brunetti, Fredenhagen, and Verch, locally covariant QFT:
  https://arxiv.org/abs/math-ph/0112041
- Fewster and Verch, quantum fields and local measurements:
  https://arxiv.org/abs/1810.06512
- Fewster, the split property for locally covariant QFT:
  https://arxiv.org/abs/1601.06936
- Fewster and Verch, dynamical locality and the no-natural-state result:
  https://arxiv.org/abs/1106.4785

These checks confirm the candidate's Loc variance, scattering convention,
state-instrument composition order, operation-local no-signalling, separated
split collar, and refusal to turn relative Cauchy evolution into gravity.
They also motivate the missing explicit localization and no-natural-state
hypotheses identified above.

## 13. Final verdict

**REVISE.**

The first decisive semantic counterexample is the same-boundary timelike pair
$F_-,F_+:B\to B$: ordinary category axioms require both composites, while
the candidate's causal wiring rejects the reversed one. Therefore
$\mathcal P_{\rm rel}$, $\mathcal Q_{\rm rel}$, and their universal property
are not constructed as printed.

This does not erase the physically meaningful result. The fixed-packet AQFT
subconstruction genuinely supports localized CP instruments, factorization
under named hypotheses, disjoint schedule independence, nonselective
no-signalling, and the steering/Bell distinctions. The honest ceiling is
rung 4.

## 14. Final integrity metadata

Candidate reauthenticated after review:

~~~text
6506c950ec26354e063960631aaabfb759216ddf0822f3be8057dad2250036af
~~~

Report LF line count: 0662

Report byte count: 036079

normalized_self_sha256: b841d81b9c312f76a2dd3ecdf9dcd0b6188552a2fd9a9516f01cc82c52148128

The normalized self-hash is computed after replacing the 64 hexadecimal
characters on the normalized_self_sha256 line by 64 zeroes and leaving every
other byte unchanged.
