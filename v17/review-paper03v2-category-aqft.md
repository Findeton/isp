# Paper 03 v2 hostile review — Seat A

## Category, AQFT, covariance, and semantic functors

Date: 2026-08-22

Seat: A

Status: **FROZEN MUTUALLY BLIND REPORT**

Verdict: **REVISE**

First supported positive rung: **rung 4**

Strongest supported rung: **rung 5**

~~~text
P03V2-RELATIVISTIC-NOSIGNALLING-PACKAGE-CONSTRUCTED
~~~

## 1. Corpus authentication and chronology

I authenticated every bound artifact before scientific judgment.

| artifact | SHA-256 | LF lines | bytes |
|---|---|---:|---:|
| Paper 03 v2 hostile-review protocol | 2b1d742b09df8e3215c8f51dd0d329222e8237400c4cd83c711a6e9e42461816 | 457 | 18918 |
| Paper 03 v2 repair pin | d9df65a0bfb39576663396f75476db9c3be9413ebbd281853162411e9376ce73 | 628 | 25109 |
| Paper 03 v2 pin audit | ccce3ca2600f9096b25686aea36db4b79a2a4b94ad66d95b8f5c1c1bbc852f91 | 274 | 10465 |
| Paper 03 v2 candidate | 93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181 | 958 | 36711 |
| Paper 03 v2 construction audit | 713d8aab7a7b4f9366536316432c939174e1cc9de9965a99ad4fbb8ee1ca8694 | 228 | 9551 |
| Paper 03 v1 adjudication | 165fa3690dda1613152bfa94c2188823a296063678a5ebdea8be5dcd34e796b7 | 339 | 16311 |
| Paper 02 v2 adjudication | 37e1ada87f17723c248896f77ce03012d809f088632abb50ed01d1b166bed135 | 381 | 19166 |
| Paper 01 adjudication | 3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1 | 314 | 13844 |
| v17 era charter | a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe | 476 | 21268 |

The review HEAD was exactly
c19bd79ed2bc1ff01533352bbb99037727cd8582. Its parent construction-audit
commit was 4568a3c6079c745df99c72b7ab0af073cb655800, and the former descends from
the latter. The frozen chronology is therefore:

~~~text
Paper 03 v1 terminal REVISE
  -> v2 causal-frontier repair pin
  -> result-neutral pin audit
  -> frozen v2 candidate
  -> construction audit
  -> frozen v2 hostile protocol
  -> this blind report
~~~

There was no integrity mismatch.

## 2. Blindness and write boundary

I read the complete frozen corpus and the relevant primary AQFT sources. I
did not open, name, infer, or discuss either sibling report. I did not edit
the candidate, pin, audits, authorities, code, or ledgers. This report is my
sole write and remains unstaged and uncommitted.

## 3. Verdict and first decisive semantic counterexample

### 3.1 The causal-frontier repair succeeds

The v1 counterexample is genuinely removed. If $v_-\prec v_+$, the early
primitive has type

$$
B_D\longrightarrow B_{D\cup\{v_-\}},
$$

and the later primitive has type

$$
B_{D\cup\{v_-\}}\longrightarrow B_{D\cup\{v_-,v_+\}}.
$$

There is no lower-set object $B_{D\cup\{v_+\}}$. These are not two
endomorphisms of one boundary, and no reverse word is composable. Once the
directed graph is fixed, the free path category has total composition on
every exactly matching pair, empty-path units, and associative concatenation.
No second causal predicate remains in composition.

### 3.2 First decisive failure: the Heisenberg target is not constructed

Candidate Definition 5.4, lines 321--337, declares

$$
\operatorname{Heis}_\Xi:
\mathcal P_\Xi^{\mathrm{op}}\longrightarrow\mathbf{CP}_\Xi
$$

and describes $\mathbf{CP}_\Xi$ as a category of unital/nonselective and
branch CP maps “with their typed classical outputs.” It supplies none of the
data needed for that declaration:

1. no object assignment $B_{\Xi,D}\mapsto\mathfrak A_D$;
2. no definition of a morphism that retains a classical result;
3. no identity or composition rule for hybrid quantum--classical arrows;
4. no relation between a complete instrument arrow and its nonunital branch
   CP maps; and
5. no finite-direct-sum or standard-Borel classical algebra on which later
   guards and readers act.

This omission becomes an exact counterexample on the smallest admitted
adaptive path. Let slot $v$ perform a two-outcome instrument
$\{\mathcal J_0,\mathcal J_1\}$ and retain $r\in\{0,1\}$. Let a later enabled
slot $w$ apply $\Phi_r$ according to that retained record. On the state side,
Definition 5.2 gives one well-typed kernel

$$
\omega\longmapsto
\sum_{r=0}^1 p_r(\omega)\,
\delta_{(U_r(\omega),r)}
$$

followed by the record-controlled kernel for $\Phi_r$.

No arrow printed in Definition 5.4 represents the same primitive. A branch
map $\mathcal J_r:\mathcal A\to\mathcal A$ is CP but generally nonunital and
does not carry the random classical value. The nonselective map
$\mathcal J_0+\mathcal J_1$ is unital but erases the value needed by the
guard. The required finite-outcome Heisenberg arrow would instead have a
hybrid type such as

$$
\widehat{\mathcal J}:
\mathcal A_{\rm later}\oplus\mathcal A_{\rm later}
\longrightarrow\mathcal A_{\rm earlier},
\qquad
\widehat{\mathcal J}(A_0,A_1)
=\mathcal J_0(A_0)+\mathcal J_1(A_1),
$$

with the guarded future represented by the corresponding map into the direct
sum. No such boundary algebra, map, or composition is defined. For
standard-Borel records the missing construction is more substantial: one
needs an explicit measurable hybrid target and an integration law, not a list
of point branches.

Therefore the claimed functor does not exist as printed, and Proposition 5.5
is untyped for a retained-outcome adaptive program. This is precisely a
protocol-listed semantic failure: a claimed semantic functor lacks a genuine
target category and functor law. It is not a prose or implementation defect.

The repair must define one actual hybrid classical--quantum category,
including objects for every boundary, complete instruments as its arrows,
discard and classical control, finite and standard-Borel outputs, and then
prove identity, composition, contravariance, and compatibility with
$\operatorname{Ev}_\Xi$. That is new mathematics and may not be inserted into
this frozen candidate.

### 3.3 Independent quantifier failure in schedule independence

Theorem 7.2 is correctly conditional: it exchanges two incomparable slots
only when their complete mechanism maps satisfy causal factorization.
Corollary 7.4, lines 459--465, then claims that **all** linear extensions of
one finite slot partial order have the same operation.

The proof requires every adjacent incomparable swap encountered between two
linear extensions to be certified. Definition 3.1 only says that a pair may
be called exchangeable after certification; it does not require every
incomparable pair in every admitted skeleton to be certified. Thus an admitted
skeleton may contain an incomparable pair for which no exchange generator is
present. The free category still has the two paths, while Theorem 7.2 supplies
no equality.

The supported statement is:

> All linear extensions connected entirely by certified incomparable
> exchanges have one kernel law; in particular this holds for a finite
> packet whose every incomparable adjacent pair satisfies the named
> factorization theorem.

Changing V2-T6 and the frame theorem from universal to this conditional
domain changes a printed quantifier and product coordinate. It is semantic.

## 4. Independent reconstruction by subject

### 4.1 Loc, Alg, and state variance

The candidate has the correct variance. Loc arrows preserve orientation,
time orientation, metric, and causal convexity. The algebra functor is
covariant, while states pull back:

$$
\psi^*\nu=\nu\circ\mathcal A(\psi),
\qquad
(\psi^*\nu)(A)=\nu(\mathcal A(\psi)A).
$$

No canonical state extension along a proper embedding is introduced.
Comparator dimension, geometry, and causal order remain declared data.

The target algebra category should be named more exactly when switching among
abstract star algebras, C-star algebras, and represented W-star algebras, but
the candidate keeps positivity and normality conditional on the relevant
packet. It does not infer dynamical locality or a natural state.

### 4.2 State closure

Definition 2.3 explicitly makes closure under every registered
positive-support posterior, nonselective update, and adaptive composite an
admission condition. It also requires normality in represented W-star
packets and a model-specific preservation proof for Hadamard or microlocal
classes.

This blocks an out-of-class posterior only by excluding that packet. It is a
conditional input theorem, not a derivation for arbitrary locally normal or
Hadamard classes. The product and theorem matrix must retain that distinction.

### 4.3 Boundary and primitive typing

Lower-set frontiers and enabled slots are coherent. Explicit skip and the
empty path have different targets. Guards depend only on predecessor records,
so no future value enables a past operation.

The construction is abstract rather than constructor-by-constructor:
Definition 4.1 says the target interface is “determined by the mechanism”
without printing the update map for preparation, measurement, discard,
record write/read, and control. The graph of **admitted** primitive arrows can
be defined to contain only interface-compatible edges, so this is not a
counterexample to the path category. It means V2-T2 is an admission schema,
and any concrete packet owes a complete primitive interface table.

The notation $B_{\Xi,D}$ suppresses the possibility of different interface
schemas at the same lower set. Either the packet fixes one schema per $D$ and
excludes mechanisms with a different interface, or the object label must
include the schema. The candidate's sentence about exact matching supports
the first reading.

### 4.4 Markov-kernel semantics

$\mathbf{Kern}$ is a genuine category: objects are standard-Borel spaces and
arrows are normalized Markov kernels. Candidate lines 288--319 assign
$X_D$ to each boundary and a normalized kernel to each primitive. Empty paths
map to Dirac identity kernels; chronological path concatenation maps to
kernel integration. This functor is constructed, conditional on the packet's
measurability and state-class closure.

Finite outcome instruments can store the outcome in the target record field.
For nonatomic outcomes, the packet must supply a countably additive
instrument/kernel and regular conditionals only almost everywhere. The
candidate correctly refuses a posterior on an arbitrary null singleton.

### 4.5 Localized AQFT instruments

For a positive probe effect $B$,

$$
\mathcal J_{s,B}(A)
=(\operatorname{id}\otimes\sigma)\Theta(A\otimes B)
$$

is CP under the fixed tensor convention. The positive insertion, scattering
star automorphism, and probe-state slice are CP. Finite POVM completeness and
unitality give

$$
\sum_r\mathcal J_{s,B_r}=\mathcal J_{s,1},
\qquad
\mathcal J_{s,1}(1)=1.
$$

Normality remains an admission condition in W-star packets. The
outgoing-to-incoming scattering convention is consistent with the cited
Fewster--Verch source.

The localization claim now names both the localized coupled/uncoupled
comparison and the Haag property or exact substitute. Its honest source scope
is localization in suitable connected open causally convex neighbourhoods of
the causal hull and identity of the nonselective operation on registered
causally disjoint observables. It is not a theorem for arbitrary CP maps.

### 4.6 Causal factorization and no-signalling

The factorization family exposes compact supports, independent product-probe
source, correlated-source alternatives, and map-level scattering identities.
For a certified pair, equality is of complete maps and not merely one state's
scalars. The least category congruence generated by such same-endpoint
exchanges is compatible with composition.

Nonselective no-signalling is independently correct:

$$
\sum_a p(a,b\mid\omega)
=\omega(\mathcal J_{A,1}(D_b))
=\omega(D_b).
$$

It uses a complete localized operation, not a commutator slogan. Selective
steering is a conditional subensemble and consumes a retained record for
comparison. Bell factorization, measurement independence, parameter
independence, outcome independence, microcausality, and operation-level
no-signalling remain distinct.

### 4.7 Presentation and operational quotients

Bijective renaming, complete coordinate transport, reassociation, and
certified incomparable exchange preserve lower-set incidence and occurrence
multiplicity. Supports, mechanisms, source correlations, states, effects,
records, and readers are not erased. The path-level presentation action can
therefore be read as a functor and its least congruence gives a category
quotient.

Complete operational equivalence over every registered one-hole context is a
congruence if the context family really is closed under every named
constructor. Theorem 9.3 assumes that closure in its proof. At the
$\operatorname{Ev}_\Xi$ probability level, the within-packet reachable
quotient and ordinary universal property survive. The asserted simultaneous
intertwining/descent of $\operatorname{Heis}_\Xi$ does not.

Ancillary probes or common refinements that change the skeleton require an
explicit registered extension; the theorem cannot silently compare unrelated
packets.

### 4.8 Packet covariance

Definition 10.1 lists every field that a packet isomorphism must transport:
geometry, system/probe/coupled theories, scattering, states/effects, slot
data, correlations, readers, and predictive/history maps. This blocks
coordinate-only transport and proper-embedding state pushforward.

Theorem 10.2 is a conditional induction once explicit component
intertwiners are supplied. It establishes the kernel-law part. Its Heisenberg
part remains unconstructed because the target category and object assignment
are absent. Local covariance compares jointly transported data; it does not
make one contingent state or apparatus invariant.

### 4.9 Type-III, split, and relative Cauchy evolution

The candidate correctly uses algebraic positive functionals and normal CP
maps rather than universal regional density matrices, traces, finite Kraus
lists, or tensor factors. A split control retains the separated collar and
verified type-I intermediate factor. It is not extended to touching regions
or arbitrary gauge systems.

Reeh--Schlieder density is not treated as deterministic bounded-cost remote
preparation. Gauge observables, charged fields, sectors, Wilson/flux
operators, centers/edges, particles, and Fock regimes remain separate types.

Relative Cauchy evolution is correctly classified as response to perturbing a
declared background, not as a probability law for geometry, metric dynamics,
Einstein equations, or gravity.

## 5. V2-T1--V2-T20 matrix

| target | mandatory quantifier | Seat A disposition | exact reason |
|---|---|---|---|
| V2-T1 | FOR-EVERY-ADMITTED-PACKET | CONSTRUCTED | finite poset, lower sets, and enabled frontier are exact declared types |
| V2-T2 | FOR-EVERY-ADMITTED-PACKET | CONSTRUCTED-AS-ADMISSION-SCHEMA | each edge extends one enabled slot; concrete interface table remains packet debt |
| V2-T3 | FOR-EVERY-ADMITTED-PACKET | CONSTRUCTED | free path category has total matched composition, units, associativity |
| V2-T4 | FOR-EVERY-ADMITTED-PACKET | CONSTRUCTED | v1 reverse timelike word is absent by object type |
| V2-T5 | CONDITIONAL-ON-NAMED-HYPOTHESES | CONSTRUCTED-CONDITIONALLY | only full map/source-certified exchanges |
| V2-T6 | FOR-EVERY-ADMITTED-PACKET | FAIL-AS-QUANTIFIED | adjacent-swap proof needs every used incomparable pair certified |
| V2-T7 | FOR-EVERY-ADMITTED-PACKET | PARTIAL | syntactic action preserves multiplicity; Heis intertwining is unconstructed |
| V2-T8 | FOR-EVERY-ADMITTED-PACKET | CONSTRUCTED-SCOPED | only explicitly constructor-closed within-packet context family |
| V2-T9 | FOR-EVERY-ADMITTED-PACKET | CONSTRUCTED-SCOPED | ordinary reachable quotient survives at kernel/prediction level |
| V2-T10 | CONDITIONAL-ON-NAMED-HYPOTHESES | DECLARED-ADMISSION-CONDITION | each concrete model owes preservation proof |
| V2-T11 | FOR-EVERY-ADMITTED-PACKET | CONSTRUCTED-AS-SUPPLIED | finite normalization; continuous countable additivity and measurability supplied |
| V2-T12 | FOR-EVERY-ADMITTED-PACKET | PARTIAL | full packet list and pullback refusal pass; Heis transport is undefined |
| V2-T13 | CONDITIONAL-ON-NAMED-HYPOTHESES | CONSTRUCTED-CONDITIONALLY | localized comparison, Haag/substitute, normality as applicable |
| V2-T14 | FOR-EVERY-ADMITTED-PACKET plus one control | CONSTRUCTED | nonselective operation theorem and record-cost steering |
| V2-T15 | EXISTS-ONE-NAMED-COMPARATOR plus FINITE-CALIBRATION-CONTROL | CONSTRUCTED-SCOPED | QFT existence and split-qubit arithmetic remain separate |
| V2-T16 | FOR-EVERY-ADMITTED-PACKET | PARTIAL | positive kernel normalization/prefix pass; adaptive AQFT-Heis compatibility untyped |
| V2-T17 | REFUSAL/NONIMPLICATION | CONSTRUCTED | lower set alone is not future sufficiency |
| V2-T18 | FOR-EVERY-ADMITTED-PACKET | PARTIAL | physical rest-frame distinction passes; schedule statement needs certification scope |
| V2-T19 | REFUSAL/NONIMPLICATION or named conditional | CONSTRUCTED | type and model-collage firewalls pass |
| V2-T20 | UNCONSTRUCTED | UNCONSTRUCTED-AS-REQUIRED | no ontology, actuality, spacetime, or gravity |

## 6. Quantifier ledger

| statement | quantifier | scope |
|---|---|---|
| lower-set/frontier syntax | FOR-EVERY-ADMITTED-PACKET | every finite declared slot packet |
| free path category laws | FOR-EVERY-ADMITTED-PACKET | graph fixed before composition |
| primitive interface correctness | CONDITIONAL-ON-NAMED-HYPOTHESES | packet admits only exact source/target interfaces |
| Markov evaluation functor | FOR-EVERY-ADMITTED-PACKET | standard-Borel, normalized, measurable primitive kernels |
| Heisenberg semantic functor | UNCONSTRUCTED | no hybrid classical--quantum target category |
| state-class closure | CONDITIONAL-ON-NAMED-HYPOTHESES | declared and model-specific |
| finite instrument CP/normalization | FOR-EVERY-ADMITTED-PACKET | within stated C-star/W-star packet |
| standard-Borel instrument | CONDITIONAL-ON-NAMED-HYPOTHESES | supplied countable additivity, topology, and measurability |
| localized observable/operation | CONDITIONAL-ON-NAMED-HYPOTHESES | localized comparison plus Haag property/substitute |
| one certified incomparable exchange | CONDITIONAL-ON-NAMED-HYPOTHESES | complete maps and source lineage |
| every linear extension agrees | CONDITIONAL-ON-NAMED-HYPOTHESES | only fully exchange-certified skeletons |
| no-signalling | FOR-EVERY-ADMITTED-PACKET | registered complete localized operation and remote reader |
| steering | FINITE-CALIBRATION-CONTROL | named split/type-I control |
| Bell compatibility | EXISTS-ONE-NAMED-COMPARATOR | no universal exact probe |
| reachable operational quotient | FOR-EVERY-ADMITTED-PACKET | explicitly closed within-packet context family; kernel semantics |
| packet covariance | CONDITIONAL-ON-NAMED-HYPOTHESES | full packet isomorphisms; no proper-embedding state push |
| positive kernel history | FOR-EVERY-ADMITTED-PACKET | normalized state/record kernels; global/contextual cost |
| full adaptive AQFT semantic agreement | UNCONSTRUCTED | depends on missing Heis category |
| type-III/split/gauge/particle walls | REFUSAL/NONIMPLICATION | positive examples stay model-specific |
| KMS/material rest frame | EXISTS-ONE-NAMED-COMPARATOR | contingent state, not covariance failure |
| actuality and local ontology | UNCONSTRUCTED | no selector or local beable law |

## 7. C1--C28 two-way controls

| ID | positive direction | hostile direction | Seat A result |
|---|---|---|---|
| C1 | lower-set frontier | non-down-closed set refused | PASS |
| C2 | one enabled-slot extension | predecessor-skipping edge refused | PASS-AS-ADMISSION |
| C3 | same-interface alternatives are parallel | physical mechanism not erased as a name | PASS |
| C4 | empty path is identity | explicit skip consumes slot | PASS |
| C5 | incomparable paths share frontier | rank/loop index absent | PASS |
| C6 | certified factorizing maps exchange | correlated or uncertified pair does not | PASS-CONDITIONAL |
| C7 | timelike order in types | reverse word absent without partial composition | PASS |
| C8 | occurrence-bearing slots | isomorphic occurrences remain two | PASS |
| C9 | guard reads predecessor record | future-record guard refused | PASS |
| C10 | complete closed context family | omitted constructor invalidates congruence | PASS-SCOPED / closure is a theorem premise |
| C11 | full packet transport | scalar/coordinate equality insufficient | PARTIAL: Ev passes, Heis absent |
| C12 | proper-embedding state pullback | canonical forward state extension refused | PASS |
| C13 | normal class-preserving update | nonnormal/out-of-class packet refused | PASS-AS-ADMISSION |
| C14 | nonatomic measure kernel | null singleton posterior refused | PASS |
| C15 | product-probe source exposed | correlated source is different mechanism | PASS |
| C16 | localized complete operation fixes reader | commutator alone insufficient | PASS |
| C17 | steering consumes record | selected conditional is not marginal | PASS |
| C18 | Bell premise ledger | microcausality is not factorization | PASS |
| C19 | KMS/apparatus rest frame allowed | covariance is not fixed-state invariance | PASS |
| C20 | no certified serialization dependence | idle microscopic foliation not excluded | PASS-WITH-CERTIFICATION-SCOPE |
| C21 | type-III functional formulation | density/trace/Kraus/tensor not generic | PASS |
| C22 | split control has collar | touching-region factorization refused | PASS |
| C23 | positive global kernel history | local microontology refused | PASS-WITH-HEIS-COST |
| C24 | retained record typed in Ev | record not actuality/division | PARTIAL: Heis record object absent |
| C25 | comparator geometry declared | no emergent spacetime | PASS |
| C26 | relative Cauchy response | no metric dynamics/gravity | PASS |
| C27 | slots are laboratory protocol | no discrete-universe reading | PASS |
| C28 | procedure context retained | trace/run token not ontic | PASS |

## 8. Hostile attacks 1--40

| attack | independent disposition |
|---:|---|
| 1 | BLOCKED: the v1 $F_-,F_+$ pair now has three distinct frontier types |
| 2 | BLOCKED: deleting $D$ recreates the v1 type failure and is not the candidate |
| 3 | BLOCKED: a non-down-closed completed set is not an object |
| 4 | BLOCKED: a successor cannot be enabled before its predecessor |
| 5 | BLOCKED: path concatenation has no second admissibility predicate |
| 6 | BLOCKED: skip and empty path have different codomains |
| 7 | BLOCKED: no topological-sort index is stored |
| 8 | BLOCKED: allowed renaming is bijective and multiplicity preserving |
| 9 | BLOCKED: hidden source correlation removes the exchange certificate |
| 10 | BLOCKED: retained-record flow is a dependency and is not exchanged |
| 11 | BLOCKED: guard inputs must already be present at the source frontier |
| 12 | BLOCKED ONLY AS PREMISE: omitting any constructor defeats Theorem 9.3 |
| 13 | BLOCKED: physical support is preserved by presentation |
| 14 | BLOCKED: coordinate-only movement is not a packet isomorphism |
| 15 | BLOCKED: proper Loc arrows have no canonical forward state map |
| 16 | BLOCKED: scattering intertwining is required; Heis target still missing |
| 17 | BLOCKED BY ADMISSION: W-star maps used must be normal |
| 18 | BLOCKED BY ADMISSION: positive-support updates must preserve $\mathfrak S$ |
| 19 | BLOCKED: zero finite branch remains zero |
| 20 | BLOCKED: no arbitrary nonatomic point posterior |
| 21 | BLOCKED: source correlation is exposed packet data |
| 22 | BLOCKED: no-signalling uses localized nonselective operation |
| 23 | BLOCKED: selected conditional is explicitly not a marginal |
| 24 | BLOCKED: postselection comparison consumes retained classical record |
| 25 | BLOCKED: QFT Bell existence is separated from exact probe realization |
| 26 | BLOCKED: free, split, Bell, and gauge controls remain distinct |
| 27 | BLOCKED: no intrinsic type-III regional density matrix is inferred |
| 28 | BLOCKED: touching local algebras are not tensor factors |
| 29 | BLOCKED: Reeh--Schlieder density retains norm/success/record costs |
| 30 | BLOCKED: no universal natural or Hadamard state is selected |
| 31 | BLOCKED: contingent KMS/material rest frame is explicitly allowed |
| 32 | BLOCKED: schedule equality does not exclude idle hidden structure |
| 33 | BLOCKED: slot is repeatedly typed as laboratory opportunity |
| 34 | BLOCKED: slot count is not duration, volume, or entropy |
| 35 | BLOCKED: global predictive object is not a local Bell variable |
| 36 | BLOCKED: lower-set frontier requires separate future-sufficiency test |
| 37 | BLOCKED: conditioning/decoherence/record do not actualize |
| 38 | BLOCKED: no v16 geometric, selector, or fusion object enters |
| 39 | BLOCKED: abstract net result constructs no interacting 3+1 theory |
| 40 | BLOCKED: Paper 04, internal time, and gravity remain closed |

## 9. Mandatory fresh attacks A1--A8

### A1 — same-boundary timelike endomorphisms

Attempt to type the old $F_-,F_+:B\to B$ pair. The early and late mechanisms
now advance different lower sets, and the later-first lower set does not
exist. **Disposition: blocked by source/target type.**

### A2 — lower-closed frontier with an inconsistent primitive interface

Choose a mechanism that writes a record not present in
$\mathsf R_{D\cup\{v\}}$, or consumes a port absent from $\mathsf P_D$.
It cannot be an admitted edge of $G_\Xi$. **Disposition: blocked at packet
admission, but a concrete packet owes the full interface-update table.**

### A3 — skip followed by an adaptive guard

Let a controlled slot write either an ordinary result or a typed skipped
value, and let a later guard read that record. The explicit skip reaches
$D\cup\{v\}$ and supplies the target record schema; the empty path remains at
$D$ and cannot type the later guard. **Disposition: skip is correctly
distinguished from identity, conditional on the printed exact interface.**

### A4 — incompatible classical-output semantics

Use the retained two-outcome instrument and later $r$-controlled channel in
Section 3.2. The Markov arrow is typed; the printed Heisenberg target offers
only branch/nonselective CP maps and no direct-sum or measurable classical
object. **Disposition: decisive semantic counterexample.**

### A5 — posterior leaves the state class on positive measure

Choose a normal instrument whose posterior exits a narrow declared class on
a positive-measure outcome set. Definition 2.3 excludes the packet.
**Disposition: blocked only by a named admission condition; no generic
Hadamard preservation theorem is claimed.**

### A6 — three incomparable scalar-commuting steps

Choose three complete operations that give the same scalar on one preparation
but do not commute as maps. They receive no exchange certificates. Pairwise
full map equalities, together with typed record permutations, would give
coherent adjacent swaps and the least congruence would enforce the braid
relations. **Disposition: scalar attack blocked; universal Corollary 7.4
still needs all swaps certified.**

### A7 — coordinate-only packet isomorphism

Transport coordinates but leave the scattering map, apparatus state, source,
or instrument fixed. It violates Definition 10.1 and cannot invoke Theorem
10.2. **Disposition: blocked.**

### A8 — collapse of isomorphic occurrences or support

Map two distinct isomorphic slots to one, or move a physical support while
calling it presentation. The action is not bijective or fails the preservation
list in Definition 9.1. **Disposition: blocked.**

### Further fresh A9 — uncertified incomparable pair

Take an admitted lower-set skeleton with an incomparable pair for which no
factorization certificate is supplied. The two free paths exist and no
exchange generator relates them. **Disposition: exact quantifier
counterexample to universal V2-T6/Corollary 7.4.**

### Further fresh A10 — nonatomic retained result

For a standard-Borel retained outcome, a CP-valued measure supplies event
maps but not by itself an algebra object carrying a pointwise record into a
later guard. **Disposition: reinforces the missing Heis target; a.e.
conditioning alone does not construct the hybrid arrow category.**

## 10. Complete 31-coordinate product

| coordinate | Seat A status | exact boundary |
|---|---|---|
| input | BOUND | terminal Papers 01/02 v2, v1 salvage, declared AQFT packet |
| slot-skeleton | DECLARED-LABORATORY-PROTOCOL | finite partial order, not ontology |
| frontier | CONSTRUCTED-TYPE | lower set; no automatic division |
| boundary | CONSTRUCTED-AS-ADMISSION-SCHEMA | exact concrete interface table remains packet debt |
| procedure | CONSTRUCTED | free path category; total matched composition |
| presentation | CONSTRUCTED-SYNTACTICALLY / HEIS-DESCENT-UNCONSTRUCTED | multiplicity and support preserved |
| quotient | CONSTRUCTED-SCOPED-AT-PREDICTION-KERNEL-LEVEL | reachable within-packet contexts |
| covariance | Ev-PACKET-ISOMORPHISM-CONDITIONAL / Heis-UNCONSTRUCTED | proper embeddings give pullback only |
| state-class | DECLARED-AND-CLOSED-WHEN-ADMITTED | model-specific preservation proof |
| instrument | BRANCH-CP-AND-Ev-KERNEL-CONSTRUCTED / HYBRID-Heis-ARROW-UNCONSTRUCTED | normality conditional |
| causal-factorization | CONSTRUCTED-CONDITIONALLY | full maps and product-source premise |
| spacelike-schedule | CONSTRUCTED-ONLY-FOR-FULLY-CERTIFIED-SWAPS | universal wording unsupported |
| no-signalling | CONSTRUCTED | complete localized nonselective operation |
| steering | CONSTRUCTED-CONTROL | selected conditional plus record cost |
| bell | CONSTRUCTED-EXISTENTIAL-COMPATIBILITY | no universal exact probe |
| positive-model | KERNEL-HISTORY-CONSTRUCTED-WITH-COSTS / FULL-ADAPTIVE-AQFT-COMPATIBILITY-UNCONSTRUCTED | global/contextual/memory-bearing |
| context | CONSTRUCTED-SCOPED | same-slot physical procedures at Ev level |
| fibers | CONSTRUCTED-SCOPED | admitted affine idle projections |
| type-III | REFUSAL-CONSTRUCTED / MODEL-SPECIFIC | no generic density, trace, Kraus, tensor |
| split | CONDITIONAL-CONTROL | separated collar and split/nuclearity |
| gauge | TYPED-UNSELECTED | no group or sector spectrum derived |
| particles | TYPED-UNSELECTED | no labeled/Fock ontology |
| continuum | ABSTRACT-NET-CONDITIONAL | no interacting-model construction |
| UV | SCOPED | no hidden cutoff/removal |
| preferred-frame | NO-UNDECLARED-SCHEDULING-FRAME-ON-CERTIFIED-FAMILIES | physical rest frames allowed; idle structure not excluded |
| record | CONSTRUCTED-IN-Ev / Heis-RECORD-OBJECT-UNCONSTRUCTED | persistent classical output |
| division | FUTURE-SUFFICIENCY-REQUIRED | frontier alone insufficient |
| actuality | UNCONSTRUCTED | no branch selector |
| barandes | ADMISSIBLE-BUT-INCOMPLETE | no universal configuration/law/state/trajectory |
| ontology | GLOBAL-PREDICTIVE-CANDIDATE-UNSELECTED | not local explanatory microphysics |
| downstream | CLOSED | no internal time, spacetime emergence, or gravity |

## 11. Outcome ladder

| rung | outcome | Seat A disposition |
|---:|---|---|
| 1 | P03V2-CAUSAL-FRONTIER-TYPE-FAILURE | surpassed |
| 2 | P03V2-ORDINARY-PROCEDURE-CATEGORY-UNCONSTRUCTED | surpassed |
| 3 | P03V2-OPERATIONAL-QUOTIENT-UNCONSTRUCTED | surpassed at scoped kernel-prediction level |
| 4 | P03V2-CAUSAL-FRONTIER-PROCEDURE-QUOTIENT-CONSTRUCTED | supported |
| 5 | P03V2-RELATIVISTIC-NOSIGNALLING-PACKAGE-CONSTRUCTED | supported ceiling |
| 6 | P03V2-POSITIVE-RELATIVISTIC-PREDICTIVE-REPRESENTATION-CONSTRUCTED-WITH-COSTS | fixed kernel histories survive, but advertised adaptive AQFT semantic compatibility is incomplete |
| 7 | P03V2-LOCALLY-COVARIANT-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT | not supported |
| 8 | P03V2-RELATIVISTIC-LOCAL-MICROONTOLOGY-CONSTRUCTED-WITH-COSTS | not supported |
| 9 | P03V2-EMPIRICALLY-DISCRIMINATED-RELATIVISTIC-ONTOLOGY | not supported |

The first supported positive rung is 4. The strongest supported rung is 5.

## 12. Bounded fixes and semantic repairs

### Bounded fixes

1. Specify the exact Alg convention or cite the inherited fixed convention
   when moving between C-star and represented W-star packets.
2. State localization as localization in appropriate connected open causally
   convex neighbourhoods of the causal hull.
3. State the topology in which a standard-Borel CP instrument measure is
   countably additive.
4. Clarify that $B_{\Xi,D}$ is unique only after its port, record, and
   predictive schemas are fixed.
5. Replace “all linear extensions” wherever the intended domain already was
   explicitly fully exchange-certified. If that intent was not already an
   admission condition, this is semantic rather than bounded.

### Semantic repairs

1. Construct the hybrid classical--quantum target category for
   $\operatorname{Heis}_\Xi$, with an object assignment for every boundary,
   complete finite and standard-Borel instrument arrows, guards, records,
   discard, identities, composition, and functor laws.
2. Reprove Proposition 5.5, exchange descent, packet intertwining, and
   positive-history AQFT agreement using that actual category.
3. Restrict V2-T6 and the schedule/frame product to fully certified slot
   families, or strengthen packet admission so every incomparable pair used
   in a linear-extension swap is certified.
4. If multiple interfaces at one frontier are intended, include the interface
   schema in the object index and reconstruct primitive/context typing.

No code implementation can settle these semantic questions.

## 13. Primary-source audit

I checked the candidate against these primary sources:

- Brunetti, Fredenhagen, and Verch, locally covariant QFT:
  https://arxiv.org/abs/math-ph/0112041
- Fewster and Verch, localized system--probe measurements and instruments:
  https://arxiv.org/abs/1810.06512
- Fewster, split property in locally covariant QFT:
  https://arxiv.org/abs/1601.06936
- Fewster and Verch, dynamical locality and natural-state no-go:
  https://arxiv.org/abs/1106.4785
- Sewell, thermal equilibrium and inertial rest frames:
  https://arxiv.org/abs/0808.0803

The sources support the candidate's algebra/state variance, scattering
convention, localized instrument formula, causal-order composition, separated
split scope, and refusal of a natural preferred state or metric dynamics.
They do not supply the missing hybrid semantic category.

## 14. Final verdict

**REVISE.**

The causal-frontier construction is a real repair: it produces an ordinary
path category and blocks the exact v1 timelike reversal by type. The localized
AQFT CP maps, certified causal factorization, nonselective no-signalling,
steering/Bell separation, packet rest-frame distinction, and ontology
firewalls substantially survive.

But Definition 5.4 does not construct the target category needed for its
contravariant semantic functor. A retained outcome followed by an adaptive
guard is typed by $\operatorname{Ev}_\Xi$ and not by the printed
$\operatorname{Heis}_\Xi$. Corollary 7.4 also exceeds the certification
premise of Theorem 7.2. The honest frozen ceiling is rung 5.

## 15. Final integrity metadata

Candidate reauthenticated after review:

~~~text
93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181
~~~

Report LF line count: 0686

Report byte count: 035611

Ordinary report SHA-256: recorded externally at freeze because embedding an
ordinary hash changes the bytes it hashes.

normalized_self_sha256: 72dfa6ff7f260a1e5e946c3c5659e8dfce7cc1ba4b0831d745d706256080e160

The normalized self-hash is computed after replacing the 64 hexadecimal
characters on the normalized_self_sha256 line by 64 zeroes and leaving every
other byte unchanged.
