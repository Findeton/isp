# ISP v17 MG0 common-law reciprocal benchmark review

## Seat M — mathematics, probability, and typing

Date: 2026-08-24

Status: COMPLETE INDEPENDENT REPORT

Candidate construction, completion, simulation, comparison, numerical
evaluation, ontology selection, and gravity verdict: NOT PERFORMED

Recommended disposition: MG0P-D3 — ACCEPT-WITH-SCOPE

---

## 0. Scope, method, and evidence notation

I reviewed only the frozen bundle authorized by the governing protocol. I did
not construct a physics candidate, inspect another current review seat's
prompt or report, use external literature, or treat contextual MG0 material as
a source of missing clauses.

The following abbreviations identify exact frozen evidence:

- C: v17/research-incubator/active/mg0/v17_mg0_common_matter_geometry_contract.md
- B: v17/research-incubator/active/mg0/v17_mg0_selector_controls_and_benchmark.md
- P: v17/note-mg0-common-law-reciprocal-benchmark-pin.md
- R1: v17/note-r1-native-source-gap-independent-review-adjudication.md
- PR: v17/note-mg0-common-law-reciprocal-benchmark-review-protocol.md

Line references below are one-based line numbers in those authenticated
objects. The review uses direct reconstruction, countermodels, and quantifier
normalization. Cautionary language was not treated as proof.

---

## 1. Chain of custody and authentication

Repository HEAD was exactly
c54b54ffacb777e1cc98d3e12be320a8eb7c2183. That commit has parent
7c96afca5c616624135526f2ae1fea858546aafd and subject
"mg0: freeze reciprocal benchmark review protocol". The protocol path at that
commit is the path supplied in the authorization.

The protocol authenticated as follows:

| object | LF lines | bytes | ordinary SHA-256 | result |
|---|---:|---:|---|---|
| PR | 439 | 16950 | 11ee64b5da11dbad3833cb43097b8130a91f95c27d494ce6a58b197ce3e00217 | PASS |

Applying the printed protocol normalization rule independently produced
7f8aad7ac09ecdbb90f7c17897a2d66d78c938f3c78ea34ea89c215496ed0e0b,
exactly the authorized normalized self-SHA-256.

Every Section 2 object authenticated:

| object | authenticated commit | LF lines | bytes | ordinary SHA-256 | result |
|---|---|---:|---:|---|---|
| C | 0ed5f3c3388c46ca14642c3075a4b3f41a38eddd | 699 | 24600 | 3552e4d00806c1a17294b9e57a4a1d693e72bfb0fdff0356411f6af2fa12d475 | PASS |
| B | 0ed5f3c3388c46ca14642c3075a4b3f41a38eddd | 518 | 19557 | 7d527e68df9ab788433d3d953b607181d1624e46aea40b50b630e675c70d8482 | PASS |
| P | f844666a26104d6503f41aeb4375a7e20146de8d | 427 | 16227 | 2355b2f6809b1ddaed8ec4a2dc8792980bcb051f075383d11ba240b21a27ade8 | PASS |
| R1 | 1eebddef46a677c67c465deb352d022c01e15fca | 646 | 26718 | 53f38d9bdda430f41c857cb73d44f48c13be2f79f5432277fd217718a0f03668 | PASS |

For each historical commit, hashing the committed blob, rather than merely
the working-tree path, reproduced the same digest. P's normalized
self-SHA-256 independently reproduced as
e36bf6032d79cd03a1cf4be481f84f9eae4c60cac1da493529eefad21590faa2.
R1's normalized self-SHA-256 independently reproduced as
1a6b3fc32de563a1b8d82c7f1fa5d7e7fdac4f0acb67b6be2d3a3ceb7655b786.

All five files use LF, end in byte 0x0a, and contain no carriage returns or
trailing horizontal whitespace. The working tree had no tracked difference
to a frozen object. One unrelated untracked v16 path was present; it is
outside Section 2 and changes none of the authenticated bytes.

Finding M-01 — chain of custody

Severity: NONE / PASS.

Exact evidence: PR:25-51 and PR:84-128 define the custody duties and
digests; the reproduced values above match all of them. No procedural
mismatch bars substantive review.

---

## 2. Reconstructed comparison carrier

Fix one bounded experiment e. Let the future public packet be Pi_e and let the
common physical record interface be

$$
\mathcal I_e=(B_e,C_e,R_e,\tau_e,U_e),
$$

where B_e and C_e are the frozen preparation/control grammar, R_e is the
complete registered record algebra, tau_e is the frozen comparison tolerance,
and U_e is the uncertainty rule. Pi_e also contains the physical apparatus,
calibrations, nuisance model, held-out settings, and the comparison-map
specification. This reconstruction is forced by C:132-157, B:55-111,
B:442-459, and P:145-189.

For entrant i, let X_i be its native prediction object. It need not have the
same mathematical type as X_j. The entrant supplies

$$
F_i:(\mathcal N_i,\sigma_i,\Pi_e)\longmapsto X_i,
$$

a licensed-record operation lambda_i, and a frozen physical comparison map
kappa_i. The common operational output is

$$
\mathcal O_i
=
\kappa_i\!\left(\lambda_i(X_i)\right)
\in
\prod_{(b,c)\in\mathcal C_e}\Delta(R_e).
\tag{M-1}
$$

Delta(R_e) here means ordinary positive distributions on the jointly
registered record algebra in one licensed laboratory context. It does not
mean that incompatible controls possess one global joint distribution, or
that unrecorded fine histories possess ordinary probabilities.

### 2.1 Ordinary-positive precursor

If entrant i has an ordinary measure P_i on a candidate carrier Omega_i and a
physical record map rho_i, its registered law is the pushforward

$$
p_i(r\mid b,c)
=
P_i\!\left(\rho_i^{-1}(r)\mid b,c\right).
\tag{M-2}
$$

No Hilbert or pair-history object is imposed.

### 2.2 Pair-history or non-Kolmogorov precursor

If entrant i has a decoherence or pair object D_i, only a licensed record
partition {F_r} may be assigned ordinary probabilities:

$$
p_i(r\mid b,c)=D_i(F_r,F_r\mid b,c),
\tag{M-3}
$$

with the entrant's printed consistency, additivity, positivity, and
normalization conditions. Events outside a licensed record algebra do not
acquire probabilities by taking a diagonal. D_i itself is not compared
componentwise with P_j. C:215-226 and C:240-245 require this separation;
B:98-111 and P:170-183 require all licensed record probabilities and an
explicit map to the registered profile.

### 2.3 Quantum prediction plus actualization

If entrant i supplies a quantum predictive object Q_i and actualization law
A_i, lambda_i must include the complete instrument/record probabilities and
all physical records generated by A_i. The actual referent may be empty for a
record-only theory. If a trajectory, flash, branch, signal, or other referent
is claimed to source gravity, its occurrence law and its relation to R_e must
also be frozen. This follows from C:159-195, C:228-238, and P:193-225.

Thus stochastic, non-Kolmogorov, and quantum-plus-actualization laws meet only
on their complete licensed record predictions. They are not forced into one
microscopic probability semantics.

### 2.4 Quotients, invariance, and empirical equivalence

C:115-157 defines the raw presentation space and the empirically silent
groupoid. C:369-379 requires every declared gauge/presentation arrow to leave
complete registered predictions invariant. Therefore an admissible comparison
map must satisfy

$$
\kappa_i\lambda_i(gX_i)=\kappa_i\lambda_i(X_i)
\quad
\text{for all declared }g\in\mathcal G_{i,e}.
\tag{M-4}
$$

If a transformation changes a physical reference, relational boundary
record, curvature, or holonomy, C:377-379 prevents it from being discarded as
gauge. A pure record relabelling is presentation, not a second law
(P:233-255).

At the registered scope, define empirical equivalence only after these maps:

$$
i\sim_e j
\quad\Longleftrightarrow\quad
\mathcal O_i\text{ and }\mathcal O_j
\text{ agree under the frozen tolerance and uncertainty rule.}
\tag{M-5}
$$

This quotient is not physical-law identity. Two physically distinct laws can
occupy the same empirical class; P:248-255 and B:414-418 explicitly call that
nonselection.

Finding M-02 — probability/type compatibility

Severity: MATERIAL BINDING INTERPRETATION, not a semantic defect.

Exact evidence: C:199-245 keeps three native forms live; B:98-111 allows a
typed precursor plus licensed record probabilities; P:170-183 uniquely adds
the explicit comparison map; P:287-290 rejects different record algebras with
no frozen physical map.

Binding consequence: native precursors, fine histories, amplitudes, and
decoherence entries are never subtracted or compared as though they were one
probability. C's schematic Delta_e at C:526-545 is well typed only after
projection to a common registered coordinate. Without lambda_i and kappa_i,
the entrant or common interface fails; a decoder may not repair it.

---

## 3. Role typing does not imply microscopic factorization

C:132-157 types boundary data, controls, operational matter/gravity
projections, records, optional actuality, and prediction. C:159-185 then
separates law, contingent state, control, record, and actual referent.
B:55-67 adds source, coherence degree, gravity-sensitive role, probe,
apparatus, and retained records while expressly denying that G is a classical
metric, quantum field, or fundamental subsystem factor.

The Cartesian organization of registered record labels in B:103-111 is an
operational product alphabet. It does not imply

$$
\Omega_e=\Omega_e^S\times\Omega_e^G\times\Omega_e^P
$$

or a tensor factorization. C:149-157 expressly permits a unified entrant to
deny even the matter/gravity split while requiring physical intervention and
record maps. Readers and apparatus are included through C and the R_C
records; they are not silently absorbed into state or law.

The word "subsystems" in B:55 is therefore controlled by B:52-67 and
P:145-162 as a registered laboratory-role term. Promoting it to microscopic
factorization would contradict the frozen clauses.

---

## 4. Logical normal form of the admission gate

Let F be the finite set of proposed frozen entrants and A a certified
admission roster. For entrant i define Complete_e(i;Pi_e,I_e) to mean every
coordinate in P:193-229 and B:389-412 is reconstructible and total over the
whole frozen experiment. Define Distinct_e(i,j) before output unblinding,
modulo declared gauge, presentation, basis, notation, physical record
relabeling, decoder changes, and answer-table duplication.

The textually correct hard gate is

$$
\begin{aligned}
\exists\,\Pi_e,\mathcal I_e,A\subseteq F:\;&
\operatorname{FrozenBeforeEvaluation}(\Pi_e,\mathcal I_e,A)\\
&\land |A|\ge2\\
&\land\forall i\in A\;
  \operatorname{Complete}_e(i;\Pi_e,\mathcal I_e)\\
&\land\forall i\ne j\in A\;
  \operatorname{Distinct}_e(i,j)\\
&\land\forall i\in A\;
  \operatorname{TotalCleanOutput}_i(\Pi_e,\mathcal I_e).
\end{aligned}
\tag{M-6}
$$

The last predicate excludes target tables, solved geometry, future settings,
private calibration, and postselected histories. "One common packet" means
one byte-identical packet chosen for the roster, not a claim that only one
possible packet exists in mathematics.

Equation (P-3) at P:259-275 prints separate counts N_complete and N_distinct.
Read alone, that conjunction has a disconnected-count countermodel: laws
L1,L2 can be complete duplicates while an incomplete L3 supplies a second
distinct class. Both raw counts can be at least two although no
complete-distinct pair exists. The frozen prose blocks this model:

- C:603-632 requires at least two entrants satisfying all listed conditions;
- B:389-418 requires at least two genuinely distinct, fully specified laws
  and physical distinctness from every other entrant; and
- P:193-255 says at least two complete laws must also be physically distinct.

Accordingly, Equation (P-3) is a summary of the intersected predicates in
Equation (M-6), not an independent weaker definition.

Finding M-03 — gate quantifier coupling

Severity: MATERIAL BINDING INTERPRETATION.

Exact evidence: P:259-290, read with P:193-255; C:601-636; B:389-418.

Binding consequence: a future admission review must print the certified
roster and pairwise table. It may not certify disconnected counts. If any
proposed duplicate remains in a larger roster, either remove it before the
roster freezes or fail pairwise certification; at minimum, the two laws that
open the gate must themselves be complete and distinct.

### 4.1 Is completeness decidable enough?

Yes, at the frozen bounded scope and only as a conservative review predicate.
P:195-225 gives a finite reconstructibility checklist, and P:227-229
expressly permits narrow scope if it covers the entire registered benchmark
and prints outside-scope debt. Therefore an otherwise complete finite-mode
weak-field law is not rejected merely because general interacting QFT,
nonlinear GR, cosmology, or a theory of actuality remains open.

Completeness is not an algorithmic theorem about arbitrary source code. The
proponent bears the burden of frozen mathematical bytes, dependency ledger,
total predictions, and error/uncertainty maps. Missing proof or output means
"not certified", not decoder completion.

### 4.2 Is distinctness decidable enough?

Yes, conditionally and fail-closed for a finite frozen roster; no universal
decision algorithm is claimed. P:233-255 and B:408-412 define the excluded
equivalences and the special objective-unravelling burden. P:254-255 requires
certification before outputs are unblinded, and P:332-344 requires pairwise
testing and frozen equivalence tests.

A future reviewer must demand either a positive physical inequivalence witness
in nomology/referent/source coupling, or a proof within the entrants' declared
finite equivalence grammar that no admitted presentation map identifies them.
If that burden is unresolved, distinctness is not certified. Numerical
disagreement cannot retroactively prove it.

---

## 5. Same-parent reciprocity

For each entrant i, reciprocity has the quantifier order

$$
\forall i\in A\;\exists J_i\;
\left[
\operatorname{Reduce}_{M\to G}(J_i)=R_i^{M\to G}
\land
\operatorname{Reduce}_{G\to M}(J_i)=R_i^{G\to M}
\right],
\tag{M-7}
$$

where J_i is generated by the same immutable law and predeclared parameter
set across Stages B, C, and D. There is no requirement that rival entrants
share one microscopic parent, and no requirement for one Kolmogorov joint
distribution over mutually exclusive interventions. The parent has the
entrant's native type and yields the two licensed operational response
families.

C:284-325 requires nonzero registered responses in both directions and one
admissible joint parent. B:231-260 checks that both matrices descend from one
normalized parent. B:273-281 explicitly forbids fitting p(G|M), fitting
p(M|G), and multiplying them with an arbitrary normalization. Stages B and C
may be controlled one-way restrictions, but Stage D must preexist and reduce
to them (B:123-144; C:334-338).

An exact splice counterexample is immediate. Let binary M,G obey
p(G=M|M)=1 in the first fitted channel and p(M not equal to G|G)=1 in the
second. Each channel is separately normalized, but no normalized joint
parent can have support both on G=M and on M not equal to G. The frozen
same-parent test rejects the pair rather than mistaking normalized channels
for reciprocity.

The do notation is indexed by a declared low-energy laboratory control. It
does not create a fundamental chronology: C:327-332, B:50-53, and
P:159-162 say so explicitly. A timeless entrant must reconstruct a relational
instrument with physical clocks and records, not infer time from evaluation
order.

Finding M-04 — reciprocity typing

Severity: NONE / PASS, with the native-parent reading in Equation (M-7)
binding.

Exact evidence: C:284-338; B:115-144, B:231-295; P:195-214 and P:259-290.
The explicit splice above is rejected. Controlled one-way limits remain
permitted as approximations but do not pass as the fundamental reciprocal
entrant.

---

## 6. Common public packet, completeness, and non-generative decoders

The public packet required by P:185-189 and B:404-407 contains, before any
prediction is evaluated:

1. localized, mixed, phase-coherent, held-out-phase, retained-mark, and
   erased-mark source preparations;
2. null, calibrated fixed-background, gravity-sensitive,
   mediator-entanglement, retained/erased, and held-out probe settings;
3. apparatus, traps, supports, clocks, shields, lasers, references, readers,
   and complete retained record definitions;
4. intervention grammar and both reciprocal directions;
5. electromagnetic, Casimir, thermal, vibrational, seismic, cross-talk,
   measurement-backaction, and other registered nuisance controls;
6. independent calibration data and parameter provenance;
7. failures and failed-feasibility reporting;
8. tolerances and uncertainty propagation; and
9. the common physical record interface and comparison-map specification.

Exact evidence is B:55-111, B:117-144, B:266-295, B:351-361,
B:389-418, B:442-459, and P:145-229.

Each entrant may have a different internal algebra, but its kappa_i must be a
frozen, invariant physical map to the same R_e. A decoder is allowed to
rename, quotient, or physically coarse-grain a prediction the entrant already
generated. It may not supply probabilities, missing records, a solved metric,
or a target process. C:553-575, C:627-631, P:216-225, and P:277-290 make this
data-flow boundary explicit.

A hidden-target attack places the desired Stage-D response table in a field
called "calibration", then lets every entrant copy it. It fails even though
the packet is public: target processes and probability tables are forbidden
at P:277-285; target-imported inputs receive no explanatory credit at
C:553-575; and the future admission review must authenticate every law and
verify no target or private answer input at P:332-344. Independence of
calibration, not mere public visibility, is load-bearing.

---

## 7. Massive-apparatus and R1 scope

R1 is used faithfully as a conditional fixed-background quantum
source-to-record recovery target and import ledger. C:63-82, B:30-46, and
P:108-141 all forbid counting it as an entrant, gravity source, actuality
law, or ontology, and forbid weakening it. R1 itself says that its optical
descent consumes background spacetime/time, constitutive response, quantum
composition, and instrument rules (R1:325-351), that its reader is only
effective and bounded (R1:353-418), and that no-refit apparatus transfer,
spacetime, gravity, or reciprocal parent is earned (R1:598-617).

Consequently R1 cannot, by logical relabelling, certify the mechanics of a
massive source, traps, supports, actuation, source-coherence witness, and
probe apparatus. The frozen MG0 schema nevertheless already types that
candidate-neutral work through complete C and R_C roles, Stage-A
nongravitational closure, full-apparatus conservation, the public nuisance
packet, and uncertainty/failure duties.

Seat-M conclusion for Q9: before entrant admission, a candidate-neutral
mechanical source-to-record closure must be completed and frozen in substance.
It may be packaged as the mechanical portion of the common public packet or
as a separately reviewed baseline, but it cannot be supplied differently by
entrants. This is a pre-entrant control already typed by the frozen clauses;
it does not require a semantic edit to C, B, or P. Whether a separately named
artifact is physically sufficient is reserved to the physical seat, but R1
alone cannot discharge the typed burden.

Finding M-05 — massive-apparatus closure

Severity: MATERIAL BINDING PRE-ENTRANT CONTROL.

Exact evidence: B:55-64, B:117-144, B:266-271, B:351-361,
B:442-459; P:145-229; R1:325-418, R1:471-481, and R1:598-617.

Consequence: no entrant can be admitted while common source preparation,
apparatus mechanics, nuisance descent, records, failures, or uncertainty
remain candidate-private or incomplete. R1 remains the sole quantum baseline;
the mechanical closure is not a rival quantum ontology or MG0 entrant.

---

## 8. Bounded decision tree and stopping rules

The valid order is:

1. Authenticate C, B, P, R1, the roster, Pi_e, and I_e.
2. Apply Equation (M-6). If it fails, report no admissible roster and run no
   comparison.
3. For every admitted entrant, test native parent typing and both reciprocal
   reductions.
4. Test gauge, conservation, causality, composition, and complete-apparatus
   closure.
5. Test the scoped R1 and classical-gravity limits.
6. Only then compare the mapped complete registered profiles under frozen
   tolerances and uncertainty.
7. Preserve exact agreement or nonidentifiability as nonselection; preserve a
   null witness, confounding, exclusion, and failed feasibility without
   ontological promotion.
8. Stop. Any change to source functional, noise, gravity carrier, time type,
   actual referent, parent architecture, or claimed limits is a new semantic
   candidate requiring new authority.

B's compact tree at B:463-485 is not safe as a standalone algorithm. Its
first "no joint object" branch says CONTRACT-INCOHERENT even when only one
proposed candidate is incomplete, while P:351-369 reserves contract
incoherence for a common-interface conflation and separately lists no
admissible roster and one-way failure. Its final "empirical difference"
branch is written per candidate, while nonselection is a relation among at
least two admitted distinct laws.

A second exact countermodel shows why the roster level matters. Let two
complete distinct laws yield the same nonzero deviation from an external
baseline. The per-candidate tree sends both to an empirical-wedge branch, but
their mutual comparison is nonselecting. Conversely, candidate-level zero
against a baseline says nothing by itself about whether another admitted law
differs. P:351-369 and B:414-418 resolve this: wedge status and pairwise
selection status are separate registered claims, and agreement never implies
law identity.

Finding M-06 — decision-tree quantifier level

Severity: MATERIAL BINDING INTERPRETATION.

Exact evidence: the shorthand at B:463-485 versus the hard gate at
P:259-290, later review order at P:332-344, outcome distinctions at
P:351-369, and nonselection rule at B:414-418.

Binding consequence: the pin's gate and outcome list govern the shorthand
tree. "Contract incoherent", "entrant incomplete/one-way", "no admissible
roster", "empirical wedge relative to a baseline", and "nonselection among
entrants" must not be collapsed. This interpretation uses existing frozen
clauses and needs no edit.

B:489-503 supplies the semantic-candidate stop rule. P:404-415 and
PR:379-439 bar automatic repair or successors. B:442-459 requires null,
nonidentifying, and failed-feasibility results to be published before stopping.

---

## 9. Quantifier and scope ledger

Every universal or existential quantifier that otherwise risks overreach is
fixed as follows.

| frozen phrase | binding quantifier and narrowed domain |
|---|---|
| "for a bounded registered experiment e" | One frozen finite experiment family and its declared control grammar, not all conceivable experiments. |
| "every candidate/entrant" | Every member of the finite proposed or admitted frozen roster, not every logically possible theory. |
| "at least two complete and distinct" | There exist i not equal to j such that both are complete and Distinct_e(i,j); for an admitted multi-law roster, pairwise distinctness is required. Separate counts cannot witness the gate. |
| "one common public packet/interface" | There exists one chosen byte-identical Pi_e and I_e consumed by all admitted entrants; this is not global mathematical uniqueness. |
| "complete output" | For every frozen (b,c) and every licensed registered outcome, a normalized prediction and uncertainty entry exists, including null and held-out settings; no claim outside e follows. |
| "every declared gauge arrow" | For every arrow in the entrant's complete declared presentation/gauge groupoid at e, mapped predictions are invariant; transformations changing physical records are outside that groupoid. |
| "same parent" | For every admitted entrant there exists its own one immutable native parent yielding both directions. It is not one parent shared by rivals and not one joint distribution over incompatible interventions. |
| "both responses nonzero" | There exist registered intervention pairs and outcomes witnessing each directional difference after nuisance control; nonzero is not required for every setting or outcome. |
| "all apparatus/nuisance channels" | Every channel capable of changing a registered output at the frozen tolerance and claimed scope must be represented or bounded; it is not a claim to model the universe. |
| "objective unravelling may count" | There must exist a frozen physical referent, occurrence law, source functional, and reciprocal coupling; a merely mathematical sample path does not count. Actuality is not required of record-only laws. |
| "physical distinctness from every other entrant" | Pairwise over the admitted finite roster, modulo the frozen equivalence grammar and before output unblinding. Global equivalence of arbitrary programs is not claimed decidable. |
| "two mandatory limits" | For each entrant there exist controlled L_Q and L_G regimes covering the registered scope, with errors and held-out tests; no solution of all QFT, nonlinear GR, or cosmology is required. |
| "every input in the ledger" | Every byte-level information dependency actually consumed by law, calibration, decoder, or simulation is classified; hidden tables and future settings are prohibited. |
| "agreement" | Equality or nonidentifiability of every mapped registered coordinate under the frozen tolerance at e; it creates empirical equivalence only at e, never law identity. |
| "every classical/nonclassical class fails or survives" | Only every admitted member of the frozen comparison class, as C:667-671 expressly says; no universal classical- or quantum-gravity theorem follows. |
| "possible null/negative outcomes" | Null, infeasible, confounded, excluded, unresolved, and nonidentifying outcomes remain terminal at the tested scope unless separately authorized work changes the question. |

This ledger is not an amendment. Each narrowing is forced by C:113-245,
C:284-338, C:526-636, B:98-144, B:365-459, and P:145-290.

---

## 10. Mandatory hostile attacks

### A-M1 — incompatible semantics presented as one probability

Attack: compare P_i(h) from an ordinary-positive fine-history law directly
with D_j(h,h) from a pair-history law on a nondecoherent event.

Result: REJECTED BY THE FROZEN GATE.

Evidence: C:203-245; B:98-111; P:170-183 and P:287-290. Only licensed record
probabilities after invariant maps share a type. If no such map exists, the
interface or entrant fails.

### A-M2 — S times G times P promoted to microscopic factorization

Attack: infer microscopic Cartesian or tensor factors from the registered
diamond and joint record notation.

Result: REJECTED.

Evidence: C:149-157, B:55-67, and P:145-162 explicitly deny this inference.
The product is an operational record organization.

### A-M3 — two conditionals spliced into a fake parent

Attack: splice the two contradictory binary channels constructed in Section
5, or any independently fitted p(G|M) and p(M|G), with an arbitrary
normalizer.

Result: REJECTED.

Evidence: C:248-280 and C:321-325; B:140-144, B:247-260, and B:273-281.
The same native Stage-D parent and parameters must reduce to both directions.

### A-M4 — two copies admitted by gauge, basis, or notation

Attack: let entrant j be T applied to entrant i for an invertible
presentation map T, then change only labels and decoder.

Result: REJECTED.

Evidence: C:369-379; C:614-619; B:408-412; P:233-255. Distinctness is tested
modulo these transformations before outputs are seen.

### A-M5 — "objective" unravelling without a physical referent

Attack: sample one of many mathematical trajectories of the same master
equation, call the sampled path objective, but add no occurrence law, record,
source functional, or reciprocal coupling.

Result: REJECTED.

Evidence: C:187-195 and C:614-619; B:408-412; P:233-250. Only a frozen
physical referent and reciprocal source law can create a distinct objective
unravelling.

### A-M6 — different internal record algebras with no invariant map

Attack: entrants output probabilities on unrelated algebras and compare
indices by an answer-dependent decoder.

Result: REJECTED.

Evidence: C:121-157 and C:369-379; P:170-189 and P:287-290. The map must be
physical, frozen, invariant, and non-generative. No map means no common
experiment.

### A-M7 — narrow complete law rejected for open general QFT

Attack: reject a total finite-mode weak-field entrant solely because its
general interacting-QFT, nonlinear-GR, or cosmology extension is open.

Result: REJECTED.

Evidence: P:227-229 explicitly permits narrow scope covering the full
benchmark and requires outside-scope debt. C:469-501 asks for controlled
limits appropriate to claimed scope. Completeness is not universality.

### A-M8 — decoder completes an incomplete law

Attack: entrant supplies one expectation or conditional channel; its decoder
uses calibration or target bytes to manufacture the remaining joint profile.

Result: REJECTED.

Evidence: C:603-631; B:389-418; P:193-225 and P:277-290. Generation must be
inside frozen entrant bytes from clean public inputs. A decoder only maps an
already complete prediction.

### A-M9 — agreement treated as law identity

Attack: two pre-certified physically distinct laws yield identical mapped
profiles, so the review retroactively declares one law.

Result: REJECTED.

Evidence: C:633-636; B:414-418; P:248-255 and P:351-369. The outcome is
empirical nonselection at e.

### A-M10 — target table hidden in the public packet

Attack: publish the target response under the name "calibration" and let every
entrant copy it.

Result: REJECTED.

Evidence: C:553-575 and C:627-631; B:290-295 and B:404-407; P:277-285 and
P:332-344. Public is necessary but not sufficient; calibration must be
independent of the held-out target.

All ten mandatory attacks were executed. The disconnected-count and
per-candidate decision-tree attacks in Sections 4 and 8 were additional
structural attacks. They defeat isolated shorthand but not the full frozen
bundle because the later pin and the surrounding prose supply the stronger
quantifiers.

---

## 11. Answers to shared questions Q1-Q12

### Q1 — neutrality

YES, at the registered operational level. C:86-109 forbids metric,
continuum, dimension, topology input, foliation, classical or quantized
gravity, tensor-product matter/gravity factorization, and a universal Born,
history, or actuality rule. C:113-157 makes history notation an interface,
not ontology. B:50-67 and P:145-162 keep G operational. Ordinary positivity is
required only for actual licensed record frequencies within a context, not
for microscopic fine histories.

### Q2 — common interface

YES, subject to Finding M-02. Equations (M-1)--(M-3) show how
ordinary-positive, non-Kolmogorov/pair-history, and
quantum-plus-actualization precursors map to the same complete record profile.
No native precursor is forced to masquerade as another. Absence of a licensed
invariant map is gate failure, not an invitation to coerce types.

### Q3 — role typing

YES. C:132-195 separates boundary, controls, matter/gravity projections,
records, optional actuality, law, and state. B:55-67 and B:266-271 separately
register source, probe, apparatus, readers, supports, work, momentum exchange,
and records. These are operational roles and do not imply microscopic
factorization.

### Q4 — same-parent reciprocity

YES. C:284-338 and B:115-144, B:231-295 reject independently fitted
directions and require one native parent and parameter set. They permit
controlled one-way restrictions without admitting those restrictions as the
fundamental reciprocal law. The laboratory do schedule is expressly not a
derivation of fundamental chronology.

### Q5 — complete experiment

YES AS A FROZEN SCHEMA; NO ACTUAL PACKET EXISTS YET. P:145-189 and
P:193-229 require one physical preparation, apparatus, intervention, nuisance,
record, held-out, tolerance, uncertainty, and comparison-map packet.
P:287-290 fails different experiments or record algebras with no map. Finding
M-05 is binding: the massive apparatus must be closed candidate-neutrally
before admission.

### Q6 — entrant completeness

YES, conservatively at declared scope. P:195-229 and B:389-418 exclude
architectures, compilers, separate solved metrics, partial channels, hidden
tables, and incomplete master equations. P:227-229 protects a total bounded
law from rejection merely because broader QFT, GR, cosmology, or actuality is
open. Missing evidence fails certification.

### Q7 — genuine distinctness

YES, conditionally at a finite frozen roster. P:233-255 excludes gauge, basis,
notation, presentation, record relabelling, parameter changes, mathematical
unravellings, duplicated tables, and decoder-only changes. An objective
unravelling counts only with physical referent, occurrence law, source, and
reciprocal coupling. Distinctness is not globally algorithmic; the frozen
positive-witness/proof burden and fail-closed rule make it governable.

### Q8 — fixed-background control

YES WITH SCOPE. R1 is bound faithfully as the conditional quantum
source-to-record recovery target and cannot be weakened, counted as entrant,
or promoted to ontology. It supplies neither gravity nor the massive
mechanical apparatus closure. That latter burden is separate and typed by the
public-packet/full-apparatus clauses.

### Q9 — massive-apparatus completeness

THE SCHEMA IS ADEQUATE, BUT COMPLETION IS A MANDATORY PRE-ENTRANT CONTROL.
B:55-111, B:117-144, B:266-271, B:351-361, B:442-459 and P:145-229 require
source preparations, traps, supports, coherence/which-path witnesses,
retained/erased records, probe readout, electromagnetic, Casimir, thermal,
seismic, vibrational, cross-talk and backaction controls, failures, and
uncertainty propagation. No actual values or certified mechanical
source-to-record descent exist yet. Candidate-neutral completion is mandatory
and already typed, so no semantic contract revision is needed.

### Q10 — discriminator validity

YES AT CLASS-RELATIVE SCOPE. PG expressly rejects only the simplistic
expectation-sourced averaged classical field and not every semiclassical law
(B:169-188). CP lists multiple null explanations and does not prove classical
gravity (B:190-204). ME is conditional on the frozen channel independence and
locality class and does not select a unique ontology (B:206-214). DD binds
decoherence and diffusion only when the entrant's own consistency relations
do (B:216-227). None is a universal ontology theorem.

### Q11 — nonselection and outcome scope

YES, with Finding M-06 controlling the shorthand tree. C:633-636,
B:414-418, and P:248-255 make agreement nonselection rather than law identity.
B:442-459 and P:351-369 preserve no roster, null/nonidentifying, infeasible,
constraint/limit failure, confounding, exclusion, and conditional wedge
outcomes. No result is forced into ontology selection.

### Q12 — authority

YES. P:14-15, P:31-33, P:70-81, P:296-347, and P:404-415 bar candidate
construction/completion, comparison, ontology selection, and automatic
successors. PR:379-439 adds the full nonpropagation list and terminal root
adjudication. No spacetime, metric, dimension, classical/quantum gravity, or
unification result can arise in this review.

---

## 12. Findings and severity summary

| finding | severity | adjudication |
|---|---|---|
| M-01 custody | NONE / PASS | Protocol and every Section 2 object authenticate exactly. |
| M-02 probability/type compatibility | MATERIAL BINDING INTERPRETATION | Compare only invariant licensed record profiles; never native precursors as one probability. |
| M-03 gate quantifier coupling | MATERIAL BINDING INTERPRETATION | Require a complete-and-distinct pair and a pairwise certified roster; disconnected counts fail. |
| M-04 reciprocity typing | NONE / PASS | One native parent per entrant yields both directions; fitted channel splicing fails. |
| M-05 massive-apparatus closure | MATERIAL BINDING PRE-ENTRANT CONTROL | R1 does not close massive mechanics; candidate-neutral closure is mandatory and already typed. |
| M-06 decision-tree level | MATERIAL BINDING INTERPRETATION | Pin-level roster gate and outcome distinctions control the per-candidate shorthand. |

No reproduced counterexample defeats the full frozen bundle under these
bindings. M-02, M-03, and M-06 are not optional editorial preferences: using
the isolated shorthand contrary to the pin would be a semantic error. M-05 is
a real pre-admission burden, not a reason to alter the benchmark semantics.

---

## 13. Disposition

MG0P-D3 — ACCEPT-WITH-SCOPE.

The chain of custody passes, the common operational carrier is type-coherent,
the hard gate is nonvacuous, and all mandatory attacks are blocked by exact
frozen clauses. Acceptance is not unqualified because four material bindings
must survive root adjudication and any future admission review:

1. all comparison occurs after invariant, non-generative maps to licensed
   complete records;
2. the admission gate means at least one pair that is simultaneously complete
   and physically distinct, with the admitted roster tested pairwise;
3. the pin's roster-level outcome logic controls the compact candidate tree;
   and
4. candidate-neutral massive-apparatus mechanical closure must be complete
   before entrants are admitted.

These bindings require no semantic edit to the frozen objects. They are
already entailed by the governing pin and direct clauses. No candidate,
comparison, or physical verdict is authorized.

---

## 14. Maximum surviving claim

> The authenticated MG0 contract, reciprocal benchmark, and pin define a
> coherent, ontology-neutral and result-neutral bounded admission/comparison
> protocol on complete licensed source--gravity-sensitive--probe record
> profiles. The protocol can admit a future comparison only after one
> byte-common public packet and output interface support at least two laws
> that are each complete at the whole registered scope and physically
> distinct from one another under frozen equivalence tests. Native
> probability semantics remain separate; both response directions must
> descend from each entrant's one immutable parent; exact agreement is
> nonselection. R1 supplies only the scoped fixed-background quantum recovery
> target, while candidate-neutral massive-apparatus mechanical closure remains
> a binding pre-entrant control.

The maximum claim does not supply a law, candidate roster, apparatus,
prediction, data set, feasible experiment, actuality rule, chronology,
spacetime, metric, dimension, classical or quantum gravity verdict, ontology
selection, or unification.

The review stops here.

---

Report LF line count: 000860

Report byte count: 039243

Report ordinary SHA-256: reported externally after the final byte is fixed;
embedding an ordinary self-hash in the file it hashes would be circular.

Report normalized self-SHA-256:
0bbb0d634b196440b0445f3bfa5c54b542b41b757146982a3ddddc5fbc2182e5

Normalization rule: replace the six decimal digits on both report count lines
and the 64 hexadecimal characters on the normalized-self line with ASCII
zeroes, preserve every other byte, and compute SHA-256. The report uses LF,
ends in one LF, and contains no trailing horizontal whitespace.
