# Paper 01 blind review — Seat M: mathematics and composition

- Date: 2026-08-22
- Reviewer lens: mathematics, measures, composition, and quantifiers
- Bound construction commit: `93da0c2813f8c767a9ef96bb133013ba038a5bea`
- Review-protocol commit / reviewed HEAD at authentication: `5724c80df77735ff490ffa20eace8cec18b9523c`
- Verdict: **ACCEPT-WITH-SCOPE**
- First decisive semantic counterexample: **none**
- Ordinary SHA-256: reported externally after freeze
- Normalized self-hash convention: replace exactly the 64 lowercase hexadecimal
  characters on the line beginning `normalized_self_sha256:` by 64 ASCII
  zeroes, preserving every other byte, then apply SHA-256.
normalized_self_sha256: d48c131c272fbd4f64ab34b7cb257ea6e39dbdf0b9bf5fb60cf74ea758466a6d

## 1. Blindness and corpus authentication

I read the full frozen protocol, pin, candidate, construction audit, quantum
contract, and v17 charter. I did not inspect either forbidden sibling path:

```text
v17/review-paper01-quantum-foundations.md
v17/review-paper01-ontology-physics.md
```

Authentication reproduced the protocol table exactly:

| Artifact | Recomputed SHA-256 | Disposition |
|---|---|---|
| `v17/note-paper01-relational-quantum-process-pin.md` | `33a7dbb3cc615978024b683588ce66c9f19deb418d8f663e3ee4db937b509bbc` | authenticated |
| `v17/paper-01-positive-record-histories.md` | `c60bea9d9ade2f30f4f88366cac11599835e9d5cac1e4f4660292b15606ee9` | authenticated; immutable |
| `v17/note-paper01-construction-audit.md` | `83a7cc2e33f9447f377519c300182501d8431a7a32560c1dbfa94ae563262008` | authenticated; nonauthoritative |
| `v17/note-empirical-quantum-adequacy-contract.md` | `c5f628dc17a739ae73e2ceb97410625b58722ca51b8e8de0d37c6aa0df92d82f` | authenticated |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | authenticated |

The candidate remained byte-identical throughout this review. No
implementation exists or is relevant to this verdict.

## 2. Executive disposition

The central finite-dimensional construction is mathematically sound at its
printed scope. It is the deferred-measurement/Stinespring realization of a
complete, causally ordered finite experiment, followed by the Born measure's
pushforward to physical setting/outcome records. This gives an ordinary
positive probability measure without imposing a positive restart kernel at
every intermediate cut. Sequential composition is therefore program wiring
before one evaluation, and not multiplication of the endpoint
modulus-squared matrices. Tensor wiring, mixtures, recorded conditioning,
ignored slots, ancillas, discard, and adaptive control survive direct
reconstruction.

The result must be read with three exact restrictions already substantially
printed by the candidate:

1. the multi-slot target is the **definite laboratory-order comb/process-
   tensor domain**, not general process matrices without predefined causal
   order;
2. the standard-Borel extension requires countably additive instruments and
   **measurable** adaptive policies, with finite-dimensional quantum input and
   output systems but a possibly separable record carrier;
3. the claimed natural equivalence is an equivalence of the **operational
   quotient/on-image category**, not an equivalence of complete ontic
   categories and not a functor of positive transition kernels at arbitrary
   cuts.

Within those restrictions I found no admitted counterexample. The proof is a
representation theorem, not an explanatory reduction of quantum process
data, and its proposed ceiling says exactly that.

## 3. Reconstruction of the positive measure

### 3.1 Finite instrument lineage

For a finite instrument `I = {I_a}` choose Kraus operators
$K_{a\alpha}$ with

$$
\sum_{a,\alpha}K_{a\alpha}^{\dagger}K_{a\alpha}=I.
$$

Then

$$
V_I|\psi\rangle
=\sum_{a,\alpha}K_{a\alpha}|\psi\rangle
 \otimes |a\rangle_R\otimes|\alpha\rangle_E
$$

is an isometry. A causally ordered finite comb has a sequential finite-memory
realization; dilating every memory channel and every instrument yields one
global isometry $U_{W,e}$. If the unmeasured final quantum output is not itself
part of `h`, its basis index is included in the collective fine label
$\lambda$. Thus

$$
q(h,\lambda\mid s)
=|\langle h,\lambda|U_{W,e}|s,0\rangle|^2\ge 0,
$$

and completeness gives

$$
\sum_{h,\lambda}q(h,\lambda\mid s)=1.
$$

For a contingent mixture $\omega$ the physical record measure is

$$
p_S(h\mid W,e,\omega)
=\sum_s\omega(s)\sum_\lambda q(h,\lambda\mid s).
$$

Contracting the unobserved dilation indices gives exactly the CP-instrument
composition, hence

$$
p_S(h\mid W,e,\omega)=p_Q(h\mid W,e,\rho_\omega).
$$

This is a derivation through a common dilation lineage, not a stored terminal
row. It does retain the complete quantum process/preparation data as input,
which is why it earns representation rather than ontological elimination.

### 3.2 Complete probability lineage

One explicit lineage is:

```text
rho and causally ordered process W
-> adaptive CP-instrument program e
-> memory-channel realization of W
-> outcome-recording Stinespring isometries for every instrument
-> one wired global isometry U_(W,e)
-> q(h,lambda|s) = |<h,lambda|U_(W,e)|s,0>|^2
-> sum over all inaccessible output/environment labels lambda
-> physical record measure p_S(h)
-> measurable reader r_* p_S
-> tr[I_(a_n)...I_(a_1)(rho)] = p_Q(h).
```

The probability remains normalized when the reader is removed or replaced by
a classical coarse-graining. A physical measurement continuation changes the
program, as it should; a diagnostic relabel does not.

### 3.3 Composition lineage

For compatible programs `f`, `g`, choose dilations $V_f,V_g$. The composite
dilation is their typed wiring, with both inaccessible environments retained:

$$
V_{g\circ f}=(V_g\otimes I_{E_f})V_f.
$$

Associativity follows from associativity of operator composition and tensor
reassociation. Replacing either dilation by an equivalent Stinespring
presentation changes the composite only by an inaccessible environment
isometry after common padding. Consequently, every later registered
continuation has the same CP map and the same record probabilities. This
establishes

$$
J(g\circ f)\simeq_{\rm op}J(g)\circ J(f)
$$

on the operational quotient. It does **not** establish factorization through
a positive kernel on a record-incomplete intermediate carrier.

### 3.4 First-order realizer lineage

With $X_0=0$ and uniform licensed marginals for $X_1$ and $X_2$, the two
measures

$$
R_+(00)=R_+(11)=\tfrac12,
\qquad
R_-(01)=R_-(10)=\tfrac12
$$

have identical licensed one-target marginals and opposite values of
$\Pr(X_1=X_2)$. This proves nonidentifiability whenever the intermediate cut
is not among the conditioning data. It does not say that a complete process
tensor, containing all interventions, is underdetermined operationally.

## 4. Source theorem versus candidate bridge

The candidate uses three distinct facts, and its bridge does not follow from
any citation alone:

1. The quantum-comb realization theorem supplies a sequence of memory
   channels for a positive causally normalized comb. The primary source
   describes universality of memory channels for admissible quantum networks:
   [Chiribella, D'Ariano, and Perinotti](https://arxiv.org/abs/0904.4483).
2. Continuous-outcome instruments on finite-dimensional quantum systems have
   dilation realizations. The primary source explicitly treats continuous
   outcome spaces:
   [Chiribella, D'Ariano, and Perinotti](https://arxiv.org/abs/0810.3211).
3. General process matrices can admit correlations without a predefined
   causal order and therefore are not all definite-order combs:
   [Oreshkov, Costa, and Brukner](https://arxiv.org/abs/1105.4464).

The candidate's own bridge is to wire those dilations for the complete
experiment, define a single positive fine measure, push it to records, and
prove operational naturality. That bridge reconstructs for definite-order
combs. The cited theorems do not turn it into a microscopic ontology or extend
it to causally indefinite process matrices.

## 5. Mandatory Seat-M fresh attacks

| Attack | Reconstruction | Disposition |
|---|---|---|
| M1 same immediate effect, different continuation | For input outcome `a=1`, the Lüders map leaves $|1\rangle$ while the reset map leaves $|0\rangle$; a later `Z` reader gives probabilities 1 and 0. Their immediate effects are both $P_a$. The dilation programs remain distinct. | **KILLED** |
| M2 $H\circ H$ versus $|H|^2$ kernels | $H^2=I$, while $B=|H|^2=\frac12\mathbf 1\mathbf 1^T$ obeys $B^2=B\ne I$. Whole-program evaluation returns `I`; no intermediate kernel product is claimed. | **KILLED** |
| M3 adaptive branch changes next instrument type | Record the first outcome `a` and use a controlled isometry $\sum_a |a\rangle\!\langle a|_R\otimes V_a$. Different finite branch carriers embed in a tagged direct sum with blank padding. The next instrument and disturbance may therefore depend on `a` without an evaluator-only branch. | **KILLED**, with the standard measurable-policy qualification in the Borel case |
| M4 discarded entangled ancilla | For $|\Phi^+\rangle_{AB}$, summing a complete basis of the discarded `B` output gives $\operatorname{tr}_B|\Phi^+\rangle\!\langle\Phi^+|=I_A/2$. The same sum is part of $\lambda$ in the dilation measure, so no remote fine label affects the local law. | **KILLED** |
| M5 atom plus continuous standard-Borel outcome | Let $X=\{\star\}\sqcup S^1$ and use a replacement instrument with atomic weight $p$ at `star` and density $(1-p)d\theta/(2\pi)$ on $S^1$. Its Choi measure has both parts, while $\mu=\operatorname{tr}J$ dominates both. The direct-integral carrier is $\mathbb C_{\star}\oplus L^2(S^1,d\theta)$ (with finite Kraus multiplicity). | **KILLED** for countably additive instruments and measurable adaptive policies |
| M6 unequal fine-grained dilation fibers | The identity channel may use $|\psi\rangle|0\rangle$ or $|\psi\rangle(|0\rangle+|1\rangle)/\sqrt2$. Fine environment masses differ, but their full sums agree. Stinespring uniqueness after common padding gives the general invariant. A single fine label is not physical. | **KILLED** |
| M7 nonminimal process memory | Attach and transport an inaccessible blank qudit to any memory realization. Its dimension increases while every complete continuation profile is unchanged. The theorem claims only existence of finite memory for each fixed process and does not claim minimality; the excess is representational/ontologically idle unless exposed. | **KILLED** |
| M8 causally indefinite process matrix | A causally nonseparable process-matrix fixture is not a definite-order comb and does not admit Lemma 1's fixed slot-order memory-channel induction. The candidate excludes it explicitly in Sections 1 and 17. | **EXCLUDED, NOT COVERED** |

The M8 result is a scope boundary, not positive evidence that indefinite order
has been represented.

## 6. Candidate-claim table

| Candidate claim | Seat-M determination |
|---|---|
| 1. finite definite-order comb realization | **PASS** for all finite dimensions and every fixed finite slot count |
| 2. positive normalized record pushforward | **PASS**; unobserved final-output indices must be included in collective $\lambda$ |
| 3. sequential and tensor naturality | **PASS AT OPERATIONAL-QUOTIENT SCOPE**; not kernel functoriality |
| 4. instruments, mixtures, adaptivity, conditioning, ancilla, discard, ignored slots | **PASS**; adaptive Borel policies must be measurable |
| 5. standard-Borel outcomes | **PASS WITH SCOPE**: countably additive CP instruments on finite-dimensional quantum ports; separable record carrier |
| 6. CHSH and Peres--Mermin controls | algebraically **PASS**; foundational premise audit belongs primarily to Seat Q/O |
| 7. inequivalent memory/division coordinates | **PASS**; one wording about “controlled permutations” should be read as finite enlarged-carrier CPTP/isometric dynamics, possibly with an extra dump ancilla |
| 8. record transport/uncompute/leak triad | **PASS** by direct unitary calculation |
| 9. first-order laws do not select a microscopic realizer | **PASS** under its explicit conditioning-domain hypothesis |
| 10. `KJ` operational identity; `JK` not ontic identity | **PASS ON THE IMAGE/OPERATIONAL QUOTIENT** |
| 11. phase-complete continuation data remain necessary | **PASS** by the common-Hadamard separator |
| 12. ceiling with ontology debt | **PASS** in this lens; no stronger ontological conclusion follows |

## 7. Registered controls C1--C12

| Control | Seat-M disposition |
|---|---|
| C1 phase completeness | **PASS**. The general-unitary theorem contains the complete $U_\phi$ family and composition $U_\phi U_\theta=U_{\phi+\theta}$; $|+\rangle,|-\rangle$ give the held-out common-continuation separator. |
| C2 general dimension | **PASS** for every finite dimension, by finite Kraus/Stinespring and comb induction rather than enumeration. |
| C3 instrument disturbance | **PASS**, M1. |
| C4 CHSH | **PASS algebraically**: the four printed correlations yield $2\sqrt2$ and uniform local marginals. No Bell-local completion is claimed. |
| C5 Peres--Mermin | **PASS algebraically**: five context products are `+I`, the final column is `-I`; no global value assignment is introduced. |
| C6 product/entangled separation | **PASS**, including the discarded-entangled-ancilla check M4. |
| C7 process memory | **PASS** with matched system interface: causal break distinguishes the retained-memory example; closed unitary channels supply the Markov control. |
| C8 nondivision translation | **PASS**. Two-Hadamard interference nondivision and the memory-bit process separate the named notions. |
| C9 record triad | **PASS**. Sector swap transports; global inverse restores; a surviving `E` copy prevents local restoration. |
| C10 convex randomization | **PASS** when the selecting coin is a physical control/record and the comparison coarse-grains it consistently. |
| C11 gauge packet | **PASS AT OPERATIONAL SCOPE**. Fine dilation presentations are invariant only after full environment pushforward; a physical control mutation is not gauge. |
| C12 v16 regression | **PASS AS NONCONTRADICTION ONLY**. No object-level embedding or v16-derived generality is earned. |

## 8. Hostile attacks 1--42

| No. | Attack | Seat-M disposition |
|---:|---|---|
| 1 | discard phase | killed by common-continuation separator and retained process state |
| 2 | copy target terminal rows | killed by the Kraus/global-dilation probability lineage |
| 3 | hidden Hilbert cache advertised eliminated | representation cost is printed; no elimination claimed |
| 4 | Kraus index as event | killed by full $\lambda$ pushforward |
| 5 | preferred basis without discriminator | no basis is promoted; cost remains open |
| 6 | qubit census as all finite `d` | killed by uniform finite-dimensional theorem |
| 7 | postselected tomography family | no such selection; finite process tomography is separating |
| 8 | same terminal table, different continuation | killed by operational equivalence under all continuations and M1 |
| 9 | tensor only on probabilities | killed by tensor wiring of ports, states, dilations, records, and environments |
| 10 | entanglement as local preagreement | killed; entangled state remains one global source datum |
| 11 | unused ancilla changes prediction | killed by unit-norm factor, including entangled-discard distinction |
| 12 | discard differs from marginalization | killed by complete output/environment sum |
| 13 | mixture nonaffinity | killed by explicit controlled coin and linearity |
| 14 | omitted postselection probability | killed; conditioning is only on a recorded event with its mass |
| 15 | source depends on Bell settings | not introduced in the registered CHSH program |
| 16 | no-signalling called locality | not claimed |
| 17 | remote setting hidden in lookup | settings are physical program records; global ontic interpretation remains open |
| 18 | omitted context key | context is a typed physical program component |
| 19 | context-independent Peres--Mermin values | no such table is constructed |
| 20 | untyped retrocausal label | no retrocausal/all-at-once law is claimed |
| 21 | every slot made Markov | killed by whole-program evaluation and H/H control |
| 22 | history cache grows invisibly | memory/environment resources are declared; no uniform constant bound claimed |
| 23 | ignored-slot inconsistency | killed by deterministic-channel insertion and outcome summation |
| 24 | memory from correlation alone | killed by causal-break definition |
| 25 | CP indivisibility equals stochastic nondivision | explicitly separated by counterexamples |
| 26 | program order called time | laboratory order is an external comparator input only |
| 27 | sector swap called erasure | killed by transported-projector equation |
| 28 | remote environment ignored after uncompute | killed by the explicit `E`-leak calculation |
| 29 | stable record called actualization | not claimed |
| 30 | no trajectory but complete ontology claimed | microscopic incompleteness is printed |
| 31 | reader defines quotient | diagnostic reader is downstream coarse-graining; physical measurement remains an experiment arrow |
| 32 | representative mass | killed by summing every dilation fiber |
| 33 | absent latent made uniform | not done; Theorem 3 reports underdetermination |
| 34 | idle hidden order called chronology | no chronology claim |
| 35 | state absorbed into law | process/preparation are typed arguments of a fixed evaluation rule |
| 36 | root/cosmological selector smuggled | absent and unclaimed |
| 37 | finite theorem called QFT | expressly excluded |
| 38 | laboratory order called spacetime | expressly excluded |
| 39 | process equivalence called ontic uniqueness | `JK` nonidentity and ontology debt are explicit |
| 40 | representation called empirical ISP evidence | expressly refused |
| 41 | candidate result generalized to all relational ontology | expressly refused |
| 42 | Paper 13D constants imported | no imported matrix, binary carrier, or size law found |

## 9. Exact scope and resources

| Axis | Reconstructed scope |
|---|---|
| dimension | every finite input/output/system dimension |
| slots | every fixed finite number |
| causal class | causally ordered combs/process tensors in supplied laboratory order |
| excluded causal class | causally indefinite/nonseparable process matrices |
| outcomes | finite; standard-Borel for countably additive CP instruments with measurable adaptive control |
| instrument class | arbitrary CP trace-nonincreasing events whose sum/integral is TP |
| quantum ancillas | arbitrary finite dimension |
| record ancilla | finite for finite outcomes; separable/direct-integral for standard-Borel outcomes |
| memory | some finite realization for each finite comb; no minimality or uniform bound claimed |
| construction kind | uniform theorem schema, explicit up to Stinespring/comb choices; not a finite lookup |
| contextual dependence | physical experiment context permitted and recorded |
| nomological datum | the global evaluation/pushforward rule |
| contingent/controlled data | process state, preparation, instruments, settings, laboratory order |
| stochastic division | only future-sufficient recorded boundaries; not every slot |
| naturality | sequential/tensor wiring before one whole-program evaluation, modulo complete operational equivalence |

### Scope notes that must survive adjudication

1. Pin Section 4.3, read in isolation, is broad enough to resemble the
   process-matrix axioms. The contract, Stage E, and the candidate consistently
   identify Q3 with process tensors/combs. The accepted target label therefore
   must print the definite-order restriction rather than the unqualified phrase
   “all finite quantum processes.”
2. “Measurable spectral factorization” is legitimate in finite matrix
   dimension (one may take the measurable positive square root and its fixed
   columns), but adaptive induction additionally presupposes a measurable
   family of branch instruments. Nonmeasurable policies are not physical
   standard-Borel instruments and are not covered.
3. The word “equivalence” is operational. The full stochastic packet contains
   presentation and possible ontological surplus for which `JK` is not an
   identity. Nothing here proves equivalence of complete beables.

These are scope controls, not repairs to the finite positive theorem.

## 10. Full 17-coordinate product

```text
target        P01-QUANTUM-PROCESS-TARGET-BOUND
              + SCOPE: FINITE-DIMENSIONAL DEFINITE-LABORATORY-ORDER COMBS
referent      P01-STOCHASTIC-RECORD-HISTORY-REFERENT-CONSTRUCTED
              + P01-MICROSCOPIC-HISTORY-REFERENT-INCOMPLETE
state-law     P01-STATE-LAW-SEPARATION-CONSTRUCTED-AT-OPERATIONAL-SCOPE
single        P01-ALL-FINITE-SINGLE-SYSTEM-CORRESPONDENCE
instrument    P01-COMPLETE-INSTRUMENT-TRANSLATION
              + SCOPE: MEASURABLE STANDARD-BOREL POLICIES
sequential    P01-SEQUENTIAL-NATURALITY-SCOPED-TO-WHOLE-PROGRAM-EVALUATION
tensor        P01-TENSOR-NATURALITY
bell          P01-BELL-NOSIGNALING-REPRODUCED-WITH-GLOBAL-CONTEXTUAL-HISTORY
              + P01-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
context       P01-CONTEXTUALITY-PHYSICALLY-TYPED
multitime     P01-FINITE-CAUSALLY-ORDERED-MULTITIME-PROCESS-EQUIVALENCE
memory        P01-MEMORY-INDIVISIBILITY-RELATION-CLASSIFIED
record        P01-DECOHERENCE-RECORD-ERASURE-TRIAD
equivalence   P01-NATURAL-OPERATIONAL-EQUIVALENCE
              + SCOPE: IMAGE/OPERATIONAL-QUOTIENT, NOT ONTIC EQUIVALENCE
hilbert       P01-HILBERT-SECONDARY-AS-BEABLE
              + P01-PHASE-COMPLETE-CONTINUATION-STRUCTURE-REQUIRED
ontology      P01-CONFIGURATION-ONTOLOGY-UNDERDETERMINED
              + P01-MICROSCOPIC-ONTOLOGY-INCOMPLETE
actuality     P01-ONE-ACTUAL-RECORD-HISTORY-POSTULATED
              + P01-MICROSCOPIC-ACTUALITY-UNCONSTRUCTED
preferred     P01-PREFERRED-STRUCTURE-COST-PRESENT
              (configuration algebra and supplied laboratory order)
overall ceiling
              P01-COMPOSITIONAL-OPERATIONAL-EQUIVALENCE-WITH-ONTOLOGY-DEBT
```

## 11. Bounded wording issues, not semantic counterexamples

1. In Section 3.2 the collective fine label $\lambda$ must be read as also
   indexing any unrecorded final quantum output in $\mathcal H_{\rm out}$;
   otherwise the displayed bra is incomplete. The proof elsewhere performs
   exactly that full sum.
2. In Section 9.3, overwriting `S` by `M` is not literally a reversible
   permutation on `S+M` for arbitrary `S`; a dump ancilla or a general CPTP
   memory channel is needed. The enlarged-carrier Markov conclusion remains
   valid and does not rely on permutation language.
3. A continuous record PVM on $L^2(X,\mu)$ is a projection-valued measure on
   measurable sets; non-atomic points are not normalizable orthogonal ket
   vectors. Section 6's direct-integral measure formulation is the governing
   one, so no point-ket ontology should be inferred.

None changes a definition, theorem domain, product coordinate, or ceiling.

## 12. Verdict and implementation wall

**ACCEPT-WITH-SCOPE.** The positive finite-dimensional, finite-slot,
causally ordered record-history representation and its operational
compositionality reconstruct. No mathematical counterexample defeats the
proposed representation-level ceiling. The restrictions in Sections 2 and 9
must remain attached to every headline.

A code implementation could not change this verdict. It could test a frozen
finite conformance suite or contain a defect, but it could neither extend the
theorem to indefinite causal order nor convert operational records into a
selected microscopic ontology.

This report is intentionally left unstaged and uncommitted on handoff.
