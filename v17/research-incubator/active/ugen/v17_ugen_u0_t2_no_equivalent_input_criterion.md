# ISP v17 — U-Gen U0-T2 no-equivalent-input criterion

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICAL CRITERION / NO CANDIDATE / NO RESULT
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official pin/review opened:** no

This document makes the no-equivalent-input clause of U0 testable without
assuming that configurations are discrete, continuous, spatial,
trajectory-like, or quantum-state-like.

Its central distinction is:

> A successful physical law must make outcomes predictable from physical
> inputs. That fact is not answer import. Answer import occurs when the target
> complete process is already recoverable from the supplied instance packet,
> calibration, reader, advice, or a known target-complete comparator before
> the candidate's proposed nomological rule does its new physical work.

The criterion is intentionally layered. No purely syntactic scanner can
distinguish every genuine law from every hidden answer. The exact verdict is
therefore relative to a frozen operational grammar, decoder language,
calibration split, tolerance, and proof-carrying provenance graph.

---

## 0. Scope and nonclaims

U0-T2 does:

1. define the operational object whose information must not be imported;
2. identify lossless recodings and target-complete comparator inputs;
3. detect tomographic, split-packet, advice, and precision laundering;
4. distinguish incomplete physical calibration from a complete answer;
5. state necessary conditions for native predictive credit; and
6. expose cases that remain undecidable or under-specified.

U0-T2 does not:

1. construct a native indivisible stochastic law;
2. select a configuration ontology;
3. prove that such a law exists or is impossible;
4. turn a supplied Barandes law into a source-complete law;
5. forbid ordinary masses, couplings, material properties, boundary records,
   or apparatus settings;
6. require a hidden selector for the realized random outcome;
7. award quantum, relativistic, spacetime, or gravity results; or
8. authorize U0-T3, a pin, review cycle, candidate, or paper.

---

## 1. Registered complete-process surface

### Definition T2.1 — experiment grammar

For one bounded evaluation, freeze an operational experiment grammar

$$
\mathfrak E=
(\mathsf{Sys},\mathsf{Prep},\mathsf{Ctrl},\mathsf{Read},
 \mathsf{Rec},\mathsf{Comp},\mathsf{Div}).
$$

The entries are typed physical procedures and composition permissions, not
fundamental spacetime assumptions. An arrow in the laboratory grammar records
which operation can be inserted into which experimental port. It does not by
itself assert an ontic global clock or trajectory.

For each experiment member $e$, let $\mathfrak A_e$ be the registered family
of complete admissible intervention programs, including adaptive choices,
retained records, physical erasures, null controls, product controls, and
declared composite operations. Let $(\mathcal R_e,\Sigma_e)$ be the measurable
space of complete records.

Neither set is required to be finite. A finite fixture is merely a bounded
control.

### Definition T2.2 — complete record process

A complete record process at member $e$ is a normalized probability kernel

$$
\mathbf P_e:
\mathfrak A_e\longrightarrow\mathcal P(\mathcal R_e),
\qquad
a\longmapsto P_e(\,\cdot\mid a).
\tag{1}
$$

Equation (1) does not assert Markov divisibility through intermediate
configurations. The full map may depend indivisibly on the complete
intervention program.

### Definition T2.3 — operational distance and quotient

For two complete record processes on the same registered grammar, define

$$
d_{\rm op}(\mathbf P,\mathbf Q)
=
\sup_{a\in\mathfrak A_e}
\left\|P(\,\cdot\mid a)-Q(\,\cdot\mid a)\right\|_{\rm TV}.
\tag{2}
$$

If the supremum is not measurable or experimentally accessible, the pin must
replace it by an explicitly registered tester family or essential supremum.
That restriction is part of scope.

Exact operational equivalence is

$$
\mathbf P\simeq_{\rm op}\mathbf Q
\quad\Longleftrightarrow\quad
d_{\rm op}(\mathbf P,\mathbf Q)=0.
\tag{3}
$$

At finite resolution $\epsilon_{\rm op}$, replace zero by the preregistered
tolerance. The target is the quotient

$$
Q_e=[\mathbf P_e]_{\rm op},
\tag{4}
$$

not a preferred wavefunction, basis, gauge, gate label, process-matrix
coordinate system, or latent realization.

Distance notation is reused on quotient classes through representatives;
(2) is constant on exact operational-equivalence classes.

The grammar must be fixed before the quotient. Endpoint-only equivalence may
collapse processes that an adaptive, coherent, or erased-record continuation
distinguishes.

---

## 2. Typed inputs and the point at which a law acts

### Definition T2.4 — candidate-independent base packet

Before a native candidate acts, the instance embedding has the typed form

$$
B_e=\iota_0(e)=
(s_e,b_e,c_e,r_e,k_e,d_e,m_e),
\tag{5}
$$

where:

1. $s_e$ is the physical system/source specification;
2. $b_e$ is contingent preparation or boundary information;
3. $c_e$ is independently calibrated control information;
4. $r_e$ is reader and stable-record calibration;
5. $k_e$ is independently established composition information;
6. $d_e$ is the division/nondivision interface; and
7. $m_e$ is the precision, provenance, and resource metadata.

These fields may be abstract. Equation (5) assumes neither particles nor
fields, neither a lattice nor a manifold, and neither external time nor
continuous paths.

### Definition T2.5 — nomological cut

A proposed nomology is a single frozen rule

$$
\mathcal S_{\mathcal N}:B_e\longmapsto
\Gamma^{\mathcal N}_e
\longmapsto
\widehat{\mathbf P}^{\mathcal N}_e.
\tag{6}
$$

The **nomological cut** is the boundary immediately before
$\mathcal S_{\mathcal N}$ performs the physical construction claimed as new.
The no-equivalent-input test first asks what can be recovered from $B_e$
without applying that new rule.

This is essential. Mere functional dependence

$$
Q_e=f(\mathcal N,B_e)
\tag{7}
$$

cannot distinguish physics from compilation; every predictive theory has
that form. Credit depends on what was supplied before (6), how $\mathcal N$
was fixed, and whether one invariant rule predicts members that were not used
to construct or select it.

The claimant cannot move the cut downstream by renaming a registered Born,
unitary, action, holonomy, tomography, or response-table compiler as the new
law. The comparator grammar freezes independently. A genuinely new nomology
must expose which physical principle it adds beyond every registered
comparator.

### Definition T2.6 — provenance graph

Every coordinate of $(\mathcal N,B_e)$ must be a node in a directed acyclic
provenance graph. Each leaf declares one of:

1. independently observed physical calibration;
2. contingent run data;
3. universal constant or structural postulate fixed across the family;
4. public mathematical convention;
5. data learned from the registered calibration split;
6. opaque external object; or
7. held-out target information.

Every transformation declares its algorithm, precision, dependencies, and
resource cost. “Independent” is procedural and epistemic here; it does not
mean statistical independence of physical variables.

Any path from a held-out target node into an input node is target leakage.
An opaque leaf without an adequate certificate receives no presumption of
cleanliness.

---

## 3. Frozen decoder classes

No verdict is meaningful until the admissible recovery operations are frozen.
Let $\mathcal D$ be a bounded, explicit family of target-independent decoders.

### 3.1 Neutral decoders $\mathcal D_0$

Neutral operations may include:

1. relabeling and coordinate changes;
2. changes of units;
3. public lossless compression and decompression;
4. gauge changes that preserve all registered record laws;
5. concatenation of packet fields;
6. marginalization or addition/removal of independent noise;
7. registered sufficient-statistic maps; and
8. public arithmetic or measure-theoretic transformations that introduce no
   target-specific physics.

A neutral decoder may be lossy. If it maps the packet to the target, the
packet was at least as informative as the target. Two-way neutral simulation
defines a Blackwell-style presentation equivalence.

### 3.2 Quantum-comparator decoders $\mathcal D_Q$

These are standard, fully printed rules that turn a supplied quantum
predictive object into registered record probabilities. They may consume,
when jointly sufficient:

1. a wavefunction or density operator;
2. a Hamiltonian, unitary, channel, or instrument;
3. a process matrix, process tensor, comb, or Choi representation;
4. a decoherence functional or amplitude table;
5. a quantum current or target-derived trajectory rate;
6. an action, phase, connection, or holonomy packet; and
7. supplied preparation, control, and reader operators.

No item on this list is automatically complete by itself. The verdict is
operational: it is quantum-complete only when the supplied joint packet plus
a frozen comparator reconstructs $Q_e$ at the registered scope.

### 3.3 Tomography decoders $\mathcal D_{\rm tom}$

These contain preregistered reconstruction maps from informationally complete
calibration data to the operational quotient. They include state, detector,
gate-set, channel, and process-tensor tomography at their exact stated scope.
Gauge freedom does not remove answer content when every registered circuit
probability is fixed.

### 3.4 Advice decoders $\mathcal D_{\rm adv}$

These expose target-specific predictive information stored as:

1. a response table or program-indexed table;
2. code, a seed, or neural-network weights;
3. an infinite- or high-precision real;
4. an encryption key plus accessible payload;
5. an external database or oracle;
6. hidden memory or implementation context;
7. a reader whose labels or response map carry the answer; or
8. information split among state, control, reader, and composition fields.

Only transparent decoders or proof-carrying opaque objects can receive an
exact classification. Arbitrary program semantics are treated in Section 8.

### Definition T2.7 — recovery closure

For $X\subseteq\{0,Q,\mathrm{tom},\mathrm{adv}\}$, write

$$
\operatorname{Cl}_X(B_e)
=
\{[D(B_e)]_{\rm op}:D
\text{ is a composable word in the registered decoder classes }X\}.
\tag{8}
$$

The decoder, its auxiliary public data, and its precision are charged. It may
not query the held-out target or invoke the candidate's proposed new
nomological rule.

---

## 4. Direct information-equivalence verdicts

For target quotient $Q_e$ and tolerance $\epsilon_{\rm op}$:

### Definition T2.8 — direct import

The packet is **direct-equivalent** when

$$
\inf_{Q\in\operatorname{Cl}_0(B_e)}
d_{\rm op}(Q,Q_e)
\le\epsilon_{\rm op}.
\tag{9}
$$

This includes response tables and their lossless recodings.

### Definition T2.9 — quantum-complete import

The packet is **quantum-complete** when (9) first holds after admitting
$\mathcal D_Q$. A supplied action or holonomy is classified here only when,
with the rest of the packet, the frozen compiler reconstructs the complete
target process. G1 is the mandatory bounded control.

### Definition T2.10 — tomographic import

The packet is **tomographically complete** when (9) first holds after
admitting $\mathcal D_{\rm tom}$. Calling complete data “calibration” does not
change this verdict.

### Definition T2.11 — advice-equivalent import

The packet is **advice-equivalent** when (9) first holds through a registered
advice decoder. This classification applies to the joint packet: splitting
the payload across fields does not clean it.

These classes locate the first demonstrated recovery route. They need not be
ontologically exclusive.

---

## 5. Calibration fibers: does genuine predictive freedom remain?

Decoder recovery catches a known representation of the answer. A second test
asks whether the calibration constraints already determine the answer even
when no convenient decoder has been named.

### Definition T2.12 — admissible comparison class

Before target opening, freeze a comparison class $\mathfrak P_e$ of normalized
complete record processes on the same operational grammar. It should impose
only the advertised type, calibration, symmetry, causality, normalization,
composition, and resource constraints. It must not be secretly defined as
the candidate's image.

### Definition T2.13 — calibration fiber

Let $C_e$ denote all calibration observations available before the hold-out.
For their declared uncertainty $\eta$, define

$$
\mathcal F_\eta(B_e)=
\left\{
\mathbf Q\in\mathfrak P_e:
\mathbf Q\text{ agrees with }C_e
\text{ and every typed input constraint within }\eta
\right\}.
\tag{10}
$$

Define its held-out operational diameter

$$
\Delta_\eta(B_e)=
\sup_{\mathbf P,\mathbf Q\in\mathcal F_\eta(B_e)}
d_{\rm hold}(\mathbf P,\mathbf Q),
\tag{11}
$$

where $d_{\rm hold}$ is (2) restricted to the preregistered held-out
intervention family.

### Definition T2.14 — calibration-complete and native-testable

For a preregistered discrimination margin $\delta$:

1. $B_e$ is **calibration-complete** when
   $\Delta_\eta(B_e)\le\delta$.
2. $B_e$ is **native-testable** when
   $\Delta_\eta(B_e)>\delta$ and the actual target remains in the fiber.

Calibration completeness means the held-out process was already fixed to the
claimed resolution. Native-testability means only that a real selection
problem remains. It does not supply a law or confer native credit.

The comparison class and tolerance must be stress-tested. An artificially
tiny $\mathfrak P_e$ can manufacture a singleton fiber; an artificially huge
class can make any calibration look uninformative.

---

## 6. Necessary conditions for native predictive credit

### Definition T2.15 — admissible pre-nomological input

A packet is admissible at T2 only if:

1. none of Definitions T2.8--T2.11 applies at target tolerance;
2. its calibration fiber is native-testable;
3. every nonopaque leaf has a clean provenance graph;
4. opaque leaves have sufficient certificates or receive an undecided veto;
5. its precision, memory, context, communication, and external resources are
   charged;
6. its configuration type was not selected after target inspection; and
7. the packet contains no unavailable future setting or future record.

This is a necessary input verdict, not a success result.

### Definition T2.16 — candidate-level native evidence

A candidate may earn native predictive evidence on a preregistered family
$\mathfrak E_{\rm eval}$ only when:

1. each evaluated input packet passes Definition T2.15;
2. one $\mathcal N$ and one source-completion algorithm freeze before target
   opening;
3. the provenance of $\mathcal N$ does not descend from held-out answers;
4. law choice, hyperparameters, configuration form, and decoder do not change
   after target opening;
5. the same rule predicts calibration and held-out complete processes;
6. the targets include members not used to design or choose the law;
7. failures are recorded rather than removed from domain; and
8. the law, instance data, decoder, precision, and all hidden resources are
   compared with the registered controls.

A universal-looking table over the entire frozen benchmark still fails item
3. A genuinely simple or independently motivated law can be long and still
pass; short description alone is not the criterion.

---

## 7. Exact propositions

### Proposition T2.P1 — representation invariance

Suppose packets $B$ and $B'$ simulate one another through target-independent
neutral decoders. Then direct target recoverability is the same for $B$ and
$B'$, up to the registered decoder approximation errors.

**Proof.** If $D(B)$ recovers the target and $G(B')=B$, then
$D\circ G$ recovers it from $B'$. The reverse direction is identical. The
approximate statement follows by the triangle inequality for total variation.
$\square$

This prevents labels, gauge, units, real-versus-complex coordinates, and
lossless compression from changing the classification.

### Proposition T2.P2 — data-processing monotonicity

If $B'=G(B)$ for a registered target-independent stochastic garbling $G$, any
target recoverable from $B'$ is recoverable from $B$.

**Proof.** Compose the recovery decoder for $B'$ with $G$. $\square$

Adding noise or discarding a field cannot cleanse answer information that was
present upstream.

### Proposition T2.P3 — split-packet closure

Let $B=(B_1,\ldots,B_n)$. If a registered decoder applied jointly to the
fields recovers $Q_e$, dividing the fields among state, control, reader,
composition, memory, or metadata leaves the joint packet answer-equivalent.

**Proof.** The typed packet constructor is itself a neutral concatenation
map, after which the original decoder applies. $\square$

### Proposition T2.P4 — calibration-completeness obstruction

If $\Delta_\eta(B_e)\le\delta$ and the actual target belongs to
$\mathcal F_\eta(B_e)$, no candidate can earn member-selection credit at
resolution $\delta$ from successful held-out prediction on that member.

**Proof.** Every process compatible with the supplied calibration, including
the actual target by hypothesis, already agrees across the held-out family to
the declared discrimination margin. Choosing any one therefore adds no
empirically resolvable selection at that scope. $\square$

### Proposition T2.P5 — ambiguity is necessary, not sufficient

If a candidate earns member-selection credit at resolution $\delta$, then its
pre-nomological calibration fiber must contain two processes separated by
more than $\delta$. The converse is false.

**Proof.** The forward statement is the contrapositive of T2.P4. For the
converse, a nontrivial fiber may remain while no proposed law selects any
member, or while the proposed law predicts the wrong one. $\square$

### Proposition T2.P6 — informationally complete reconstruction

If the supplied calibration values and a frozen target-independent
reconstruction map determine every probability in the registered
complete-process grammar to tolerance $\epsilon_{\rm op}$, then the packet is
tomographically complete at that tolerance.

**Proof.** The reconstruction map is an element of
$\mathcal D_{\rm tom}$ and therefore witnesses Definition T2.10. $\square$

This applies to an informationally complete process tensor, comb, gate set, or
equivalent operational tomography. It does not classify incomplete endpoint
calibration as complete-process import.

### Proposition T2.P7 — process-comparator completeness

If a supplied process tensor or comb is valid for the entire registered
intervention grammar and the registered contraction rule returns every record
law, the joint packet is quantum-complete.

**Proof.** The contraction rule is a registered $\mathcal D_Q$ decoder. Its
image is $Q_e$, so Definition T2.9 applies. $\square$

This proposition classifies information, not ontology. It does not say a
process tensor is physically fundamental.

### Proposition T2.P8 — arbitrary opaque detection is undecidable

For an unrestricted partial-program field, there is no total algorithm
deciding whether that field computes a fixed nontrivial computable target
process at the registered interface.

**Proof sketch.** Computing the target is a nontrivial extensional property
of the partial computable function represented by the program. Rice's theorem
rules out a total decision procedure for all such programs. $\square$

Therefore T2 can be exact only for its frozen transparent language and
proof-carrying extensions. “Undecided” is an honest outcome, not permission to
treat an opaque payload as clean.

---

## 8. The undecidability and induction boundary

No finite audit proves that an arbitrary mathematical object contains no
clever encoding of a target. T2 handles this boundary by requiring:

1. a registered input grammar rather than arbitrary code;
2. typed, finite provenance dependencies;
3. declared precision and external resources;
4. proof certificates for opaque semantic components;
5. held-out members beyond those used to construct $\mathcal N$;
6. prospective freeze before target opening; and
7. scope-limited conclusions.

Nor can finite held-out success deductively prove one universal law of nature.
It can discriminate candidates, refute printed scopes, and earn bounded
empirical support. Uniformity beyond the tested family remains an inductive
claim whose scope and resource scaling must be printed.

This is not a special weakness of positive stochastic ontology. It applies to
any attempt to distinguish a law from a disguised predictive database.

---

## 9. Resource and provenance ledgers

Every candidate packet must report:

| coordinate | required charge |
|---|---|
| nomology | description, fitted constants, provenance, domain |
| contingent state | information and precision per preparation |
| controls | calibration data, context, physical implementation |
| readers | response calibration and record capacity |
| composition | interaction-specific and system-size data |
| configuration | capacity, dimension, topology, adaptivity |
| online dynamics | memory, update cost, future dependence |
| shared resources | communication, common advice, correlations |
| opaque objects | code, weights, oracle, certificate |
| decoder | algorithm, auxiliary data, compute, precision |
| family scaling | dependence on system size and program depth |

The basic accounting coordinate is

$$
L(\mathcal N)+L(B_e)+L(\text{decoder})+
L(\text{precision})+L(\text{external resources}).
\tag{12}
$$

No single coding language is ontologically preferred, so (12) is comparative
within a frozen language and under lossless-recoding controls. It can expose
answer displacement; it cannot by itself identify the true law.

Universal constants fixed once across the whole family are charged once.
Target-specific values are charged per member. A constant is not admissible
merely because it is called universal; its provenance and empirical role must
be printed.

---

## 10. Decision procedure

For each candidate evaluation:

1. **Freeze grammar.** Register systems, preparations, controls, readers,
   compositions, divisions, complete records, and held-out programs.
2. **Freeze resolution.** Register $\epsilon_{\rm op}$, calibration uncertainty
   $\eta$, and discrimination margin $\delta$.
3. **Freeze comparison class.** State $\mathfrak P_e$ without using the
   candidate image or hidden targets.
4. **Inventory the packet.** Type every field of $\mathcal N$ and $B_e$.
5. **Build provenance.** Trace every leaf and transformation.
6. **Freeze decoders.** Register $\mathcal D_0,\mathcal D_Q,
   \mathcal D_{\rm tom},\mathcal D_{\rm adv}$ and auxiliary resources.
7. **Run closure tests.** Attempt Definitions T2.8--T2.11 in order.
8. **Compute or bound the fiber.** Establish $\Delta_\eta(B_e)$ by theorem,
   exhaustive finite calculation, or a declared bound.
9. **Audit opacity.** Require certificates or assign undecided.
10. **Freeze the candidate law.** Only an admissible packet may proceed.
11. **Open targets once.** Evaluate complete processes without retuning.
12. **Report both verdicts.** Print the input verdict and predictive verdict
    separately.

Failure to calculate the exact fiber is not permission to assert it is
nontrivial. A rigorous lower bound above $\delta$ is sufficient for
native-testability; a rigorous upper bound below $\delta$ is sufficient for
calibration completeness.

---

## 11. Outcome vocabulary

| outcome | exact meaning |
|---|---|
| T2-DIRECT-IMPORT | neutral recovery of target complete process |
| T2-QUANTUM-COMPILER | target recovered through supplied quantum-complete object |
| T2-TOMOGRAPHIC-IMPORT | calibration reconstructs the target operational quotient |
| T2-ADVICE-LAUNDERING | target recovered from code, memory, precision, oracle, or split packet |
| T2-CALIBRATION-COMPLETE | fiber diameter below the registered discrimination margin |
| T2-ADMISSIBLE-INPUT-ONLY | no import located and a nontrivial fiber is certified |
| T2-UNDER-SPECIFIED | no import located, but no candidate law supplies the missing prediction |
| T2-UNDECIDED | opacity, missing proof, or unbounded decoder semantics prevent classification |

T2-ADMISSIBLE-INPUT-ONLY is the only passing input verdict. It awards no
physical result and makes no prediction.

---

## 12. Mandatory hostile-control battery

The following controls prevent the criterion from becoming a blacklist of
notation or a license for hidden answer tables.

| id | packet | required T2 behavior |
|---|---|---|
| H01 | complete record-probability table | DIRECT-IMPORT |
| H02 | lossless relabeling or compression of H01 | DIRECT-IMPORT |
| H03 | H01 split across state, control, and reader | ADVICE-LAUNDERING or DIRECT-IMPORT |
| H04 | process tensor plus contraction rule | QUANTUM-COMPILER |
| H05 | quantum comb plus link product | QUANTUM-COMPILER |
| H06 | Choi data sufficient for all registered circuits | QUANTUM-COMPILER |
| H07 | target wavefunction, dynamics, controls, and readers jointly sufficient | QUANTUM-COMPILER |
| H08 | a wavefunction alone that is insufficient for the grammar | not automatically complete |
| H09 | target action/phase/holonomy plus G1 compiler | QUANTUM-COMPILER |
| H10 | informationally complete process tomography | TOMOGRAPHIC-IMPORT |
| H11 | endpoint-only tomography with distinct continuation fibers | may remain ADMISSIBLE or UNDER-SPECIFIED |
| H12 | gate-set estimate fixing all registered circuit probabilities modulo gauge | TOMOGRAPHIC-IMPORT |
| H13 | independently measured mass, field setting, duration, or material property | not automatically import |
| H14 | public symmetry group with multiple compatible process members | not automatically import |
| H15 | universal constant fixed across all held-outs | charge once; not automatically import |
| H16 | a target-specific fitted constant for each program | ADVICE-LAUNDERING |
| H17 | response-table neural network trained on hidden targets | ADVICE-LAUNDERING |
| H18 | infinite-precision real encoding the table | ADVICE-LAUNDERING |
| H19 | short key plus accessible external target database | ADVICE-LAUNDERING |
| H20 | arbitrary opaque executable with no certificate | UNDECIDED |
| H21 | per-program stochastic seed selecting the distribution | ADVICE-LAUNDERING if target-specific |
| H22 | random seed selecting one realized outcome after a law fixes probabilities | not process import |
| H23 | reader response map equal to the target instrument table | QUANTUM-COMPILER or DIRECT-IMPORT |
| H24 | physical reader calibration leaving multiple complete processes | may be admissible |
| H25 | future control settings embedded in the initial state | reject provenance/type |
| H26 | candidate law containing one branch per held-out program | ADVICE-LAUNDERING at law level |
| H27 | one fixed law predicting new members from noncomplete inputs | eligible for later native evidence |
| H28 | configuration form chosen after target inspection | reject provenance/model selection |
| H29 | a large real apparatus described at high cost | not import merely because large |
| H30 | same endpoint $\Gamma$ with two admissible distinguishable complete continuations | certify nontrivial fiber |
| H31 | lossy coarse graining of an imported answer | import remains upstream by T2.P2 |
| H32 | candidate passes one fixture but changes rule for another | no uniform native credit |

H08, H13--H15, H22, H24, H27, and H29 are necessary anti-overreach controls.
The gate must not reject legitimate physical inputs merely because they are
predictively useful or mathematically rich.

---

## 13. Classification of existing v17 controls

This section assigns no new scientific status.

1. **Paper 01 / supplied record compiler.** Quantum-complete or direct at its
   declared process scope; exact representation, zero native selection.
2. **Supplied endpoint $\Gamma$.** Direct for the supplied endpoint surface.
   It may remain under-specified for complete continuations; incompleteness
   does not become derivation.
3. **Pair-history kernel.** Quantum-complete when reconstructed from the
   target amplitudes or decoherence functional.
4. **G1.** Quantum-complete at members where supplied action/holonomy plus its
   compiler determine the complete record law. It remains a mandatory control.
5. **G2.** A quantum-representation and fixed-background source-origin
   control, not a native U0 input packet.
6. **Bell/Bohm trajectory comparator.** Quantum-complete where target state,
   Hamiltonian, current, and reader structure are supplied.
7. **N1/N1A.** Bounded Nelson prior-art and hostile controls. Their local
   supplied fields leave global quantum sectors underdetermined; they are
   neither U0 parent ontology nor an admissible automatic repair.
8. **Raw physical apparatus packet.** Potentially admissible only after its
   provenance and calibration fiber are audited. The label “physical” is not
   a certificate.
9. **Barandes representation of a supplied law.** Downstream representation
   of $\Gamma$, not source completion. Whether the supplied $\Gamma$ is
   endpoint-complete, process-complete, or under-specified must be stated.

---

## 14. Boundary handed to U0-T3

T2 makes the next fixture requirement precise. U0-T3, if separately pursued
author-side, must supply:

1. a configuration-neutral physical program grammar;
2. independently grounded preparation, control, and reader equivalence
   classes;
3. a calibration split with a rigorously nontrivial complete-process fiber;
4. complete adaptive, composite, retained, and erased record targets;
5. a frozen decoder language and provenance schema;
6. finite, continuous, contextual, and whole-program positive controls;
7. no bare gate label or imported action/holonomy as physical source; and
8. no candidate ontology or law selected by the fixture's mathematical type.

The target processes remain hidden. A fixture is not a theory.

---

## 15. Present verdict

$$
\begin{array}{ll}
\text{OPERATIONAL TARGET QUOTIENT} & \text{DEFINED}\\
\text{NEUTRAL / QUANTUM / TOMOGRAPHY / ADVICE CLOSURES}
& \text{DEFINED}\\
\text{CALIBRATION FIBER AND DIAMETER} & \text{DEFINED}\\
\text{PROVENANCE AND RESOURCE AUDIT} & \text{DEFINED}\\
\text{OPAQUE-PROGRAM LIMIT} & \text{PRINTED}\\
\text{CONFIGURATION FORM} & \text{UNSELECTED}\\
\text{NATIVE CANDIDATE} & \text{ABSENT}\\
\text{EXISTENCE OR NO-GO RESULT} & \text{NONE}\\
\text{OFFICIAL PIN / REVIEW / PAPER} & \text{NONE}
\end{array}
$$

---

## 16. Maximum legitimate claim

> Relative to a frozen complete-process grammar, decoder language,
> calibration split, comparison class, tolerance, provenance graph, and
> resource ledger, U0 can rigorously distinguish target-complete calibration
> or comparator input from a packet that leaves empirically distinguishable
> processes open. A nontrivial calibration fiber is necessary but not
> sufficient for native-law credit. Arbitrary opaque answer encodings cannot
> be ruled out by a universal algorithm, so exact admissibility must remain
> proof-carrying and scope-relative. This criterion constructs no stochastic
> law and neither proves nor refutes Barandes's guiding ontology.
