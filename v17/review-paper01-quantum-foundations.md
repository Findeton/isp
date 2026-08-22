# Paper 01 hostile review — Seat Q

## Quantum information and foundations

Date: 2026-08-22

Status: **INDEPENDENT BLIND REPORT — UNSTAGED AND UNCOMMITTED ON HANDOFF**

Verdict: **ACCEPT-WITH-SCOPE**

## 0. Independence and authentication

This is the sole Seat Q report required by the frozen hostile-review protocol.
I did not inspect either forbidden sibling path:

- `v17/review-paper01-mathematics-composition.md`;
- `v17/review-paper01-ontology-physics.md`.

I did not communicate with either sibling seat, delegate any part of the
review, inspect an implementation, or edit the candidate corpus.

The worktree HEAD at authentication was
`5724c80df77735ff490ffa20eace8cec18b9523c`.  The protocol's bound
construction commit `93da0c2813f8c767a9ef96bb133013ba038a5bea` exists and
the five scientific artifacts are byte-identical between that commit and the
reviewed worktree.  The only pre-existing worktree item outside the reviewed
corpus was the unrelated untracked file
`v16/note-handoff-prompt-2026-08-22.md`.

| Artifact | Authenticated SHA-256 | Result |
|---|---|---|
| `v17/note-paper01-hostile-review-protocol.md` | `e059de0988d54d67ebc069cbb79f24c0dd7584d1861c5bf42a15e1b0e78ab2b0` | exact |
| `v17/note-paper01-relational-quantum-process-pin.md` | `33a7dbb3cc615978024b683588ce66c9f19deb418d8f663e3ee4db937b509bbc` | exact |
| `v17/paper-01-positive-record-histories.md` | `c60bea9d9d9ade2f30f4f88366cac11599835e9d5cac1e4f4660292b15606ee9` | exact |
| `v17/note-paper01-construction-audit.md` | `83a7cc2e33f9447f377519c300182501d8431a7a32560c1dbfa94ae563262008` | exact |
| `v17/note-empirical-quantum-adequacy-contract.md` | `c5f628dc17a739ae73e2ceb97410625b58722ca51b8e8de0d37c6aa0df92d82f` | exact |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | exact |

The reviewed candidate had 1,242 LF lines and 49,693 bytes.  No bound byte
changed during the review.

## 1. Executive finding

The finite-dimensional, finite-slot, causally ordered, finite-outcome core is
correct as a quantum operational representation.  Given the entire quantum
process and the entire instrument program, a common Stinespring/comb dilation
exists; the squared norm on the final dilation registers is positive and
normalized; summing inaccessible dilation labels returns exactly the joint
instrument probabilities.  This construction preserves disturbance,
entanglement, adaptive control, causal-break memory tests, record transport,
and coherent erasure because it retains the full quantum process rather than
only an immediate probability table.

That success is also its exact physical ceiling.  The construction is a
Hilbert/process wrapper with a positive record readout, not an independently
specified stochastic microdynamics.  The candidate says this repeatedly and
therefore does not commit the hidden-Hilbert null as an overclaim.  It changes
the proposed beables, but it does not explain the Born rule, select a
configuration algebra, supply Bell-local causation, or select an actual
microscopic history.

Two scope qualifications are binding:

1. the standard-Borel adaptive extension is valid only for measurably
   parameterized instrument kernels, and point conditioning is defined only
   almost everywhere (or on positive-probability record events); and
2. `GLOBAL-CONTEXTUAL-HISTORY` describes a whole-program operational joint
   law, not a constructed Bell ontology or spacetime causal mechanism.

Neither qualification defeats the finite-outcome theorem or its printed
ontology-debt ceiling.  There is no decisive semantic counterexample in the
Seat Q lens.

## 2. Primary-source scope audit

Only primary sources were used to check inherited theorem scope.

| Source theorem | What it supports | What it does not supply |
|---|---|---|
| [Chiribella, D'Ariano and Perinotti, quantum networks](https://arxiv.org/abs/0904.4483) | deterministic causal combs admit realization by sequential memory channels; link composition and testers are operationally complete | a stochastic ontology or removal of causal laboratory order |
| [Chiribella, D'Ariano and Perinotti, continuous-outcome instruments](https://arxiv.org/abs/0810.3211) | continuous-outcome instruments on finite-dimensional systems admit dilation schemes | arbitrary nonmeasurable adaptive control or pointwise conditioning on null outcomes |
| [Pollock et al., operational Markov condition](https://arxiv.org/abs/1801.09811) | causal breaks give the relevant multi-time Markov discriminator; CP-divisible reduced dynamics can still carry process memory | equivalence with Barandes division or a microscopic stochastic restart law |
| [Barandes, indivisible stochastic processes](https://arxiv.org/abs/2507.21192) | minimalist first-order laws generically admit multiple non-Markovian realizers | selection of one realizer, complete instruments, Bell locality, or gravity |

The candidate's bridges beyond those sources were rebuilt below rather than
awarded by citation.

## 3. Complete probability lineages

### 3.1 General instrument lineage

For a finite instrument with Kraus operators `K_(a,alpha)`, define

$$
V_{\mathcal I}|\psi\rangle
=\sum_{a,\alpha}K_{a\alpha}|\psi\rangle
\otimes|a\rangle_R\otimes|\alpha\rangle_E.
$$

The instrument normalization identity makes `V_I` an isometry.  Wiring these
isometries into a causal-comb memory dilation gives one global isometry
`U_P`.  For a purified source `|Psi>` the fine law is

$$
q(h,\lambda)=
|\langle h,\lambda|U_{\mathcal P}|\Psi,0\rangle|^2\geq0.
$$

Unitarity gives `sum_(h,lambda) q = 1`.  The physical reader forgets the
unobserved label:

$$
p_S(h)=\sum_\lambda q(h,\lambda).
$$

Expanding the wired isometries contracts precisely the Kraus indices, so

$$
p_S(h)=\operatorname{tr}
\mathcal I^{x_n}_{a_n}\circ\cdots\circ
\mathcal I^{x_1}_{a_1}(\rho)
=p_Q(h).
$$

This is a derivation through a common dilation, not storage of one terminal
probability row.  It is nevertheless the Born rule applied to retained
quantum data; it is not a derivation of that rule from a smaller stochastic
law.

### 3.2 Held-out nonprojective disturbance lineage

Let `0 < eta < 1` and

$$
E_\pm=\frac{I\pm\eta Z}{2}.
$$

Define two instruments

$$
\mathcal A_\pm(\rho)=\sqrt{E_\pm}\rho\sqrt{E_\pm},
\qquad
\mathcal B_\pm(\rho)=
X\sqrt{E_\pm}\rho\sqrt{E_\pm}X.
$$

Both have the same nonprojective POVM because the effect of each branch is
`E_±`.  On input `|0><0|`, conditional on `+`, instrument `A` outputs `|0>`
while `B` outputs `|1>`.  A later `Z` reader separates them perfectly.  Their
record pushforwards agree at the immediate reader and differ after the common
continuation because their CP maps, and hence their wired dilations, differ.
The construction passes the stronger nonprojective version of C3.

### 3.3 Whole-program composition lineage

For compatible programs `f` and `g`, first wire their quantum ports and
memory carriers, then compile the wired object to `U_(g o f)`.  Any additional
continuation `k` is wired before the single evaluation.  Associativity of
physical wiring gives the same target process functional for

$$
k\circ(g\circ f)
\quad\text{and}\quad
(k\circ g)\circ f,
$$

and the record pushforwards agree for every complete reader.  This establishes
operational naturality on the image of `J`.  It does **not** establish
positive-kernel factorization at the intermediate cut.  Indeed, with

$$
B=|H|^2=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix},
$$

one has `B^2 = B` while `|H^2|^2 = I`.  Any account of sequential naturality
as multiplication of record kernels would fail; the candidate does not make
that move.

### 3.4 CHSH lineage

Give the setting registers independent distributions `q_A(x)` and `q_B(y)`,
prepare `|Phi+>`, and use controlled local measurement dilations for the four
observables printed in the candidate.  The positive fine law pushes forward
to

$$
p(x,y,a,b)=q_A(x)q_B(y)
\frac{1+abE_{xy}}{4},
$$

with

$$
E_{00}=E_{01}=E_{10}=\frac1{\sqrt2},
\qquad E_{11}=-\frac1{\sqrt2}.
$$

Thus `S = 2 sqrt(2)`, and summing over either local outcome gives the remote
setting-independent marginal `1/2`.  If one instead introduces a pre-setting
variable `lambda`, independent of `x,y`, and requires factorization

$$
p(a,b|x,y,\lambda)=p(a|x,\lambda)p(b|y,\lambda),
$$

the standard pointwise CHSH bound is at most `2`, so that completion fails.
The candidate correctly earns no-signalling but not Bell-local ontology.

### 3.5 First-order realizer lineage

The two measures

$$
R_+(00)=R_+(11)=\frac12,
\qquad
R_-(01)=R_-(10)=\frac12
$$

have identical one-time marginals at both targets and opposite values of the
higher-order statistic `Pr(X_1 = X_2)`.  Therefore licensed first-order
marginals do not determine a microscopic Kolmogorov tower.  Nothing in the
record pushforward selects one of these extensions.  The candidate's
ontology-debt theorem is correct at this stated level.

## 4. Mandatory Seat Q fresh attacks

| Attack | Reconstruction | Disposition |
|---|---|---|
| equal diagonal, held-out continuation | `|psi_phi>=(|0>+e^(i phi)|1>)/sqrt(2)` has constant diagonal; after `H`, `p(0)=(1+cos phi)/2`; `U_phi U_theta=U_(phi+theta)` | **PASS**; continuous phase and common-continuation data survive |
| nonprojective equal-POVM instruments | the `A_±/B_±` construction in Section 3.2 has identical effects and perfectly distinct conditional outputs | **PASS** |
| pre-setting Bell-local completion | measurement independence plus factorization implies `|S| <= 2`, contradicting `2 sqrt(2)` | **PASS**, at the cost of no Bell-local completion |
| context relabel changing apparatus | a simultaneous rename of apparatus, observables, records, and reader is presentation; changing the observable behind a fixed apparatus port changes the program and its continuation profile | **PASS**, though the paper should reserve “contextual history” for this operational sense |
| CP-divisible but causal-break non-Markov | a retained uniform memory bit overwrites `S` before and after a causal break; unperturbed reduced maps are the same depolarizing channel and are CP-divisible, while the final output retains the pre-break result | **PASS** |
| process-Markov but configuration-kernel-indivisible | the closed `H,H` process has no environmental memory and is causal-break Markov; since `B` has identical columns, every stochastic `KB` has identical columns and cannot equal `I` | **PASS** |
| incomplete uncomputation with remote copy | after `S -> R`, `R -> E`, and local inverse `S -> R`, the state is `(|000>+|101>)/sqrt(2)`; tracing `E` leaves no fringe | **PASS** |
| Kraus rotation | `K'_(a,beta)=sum_alpha u^(a)_(beta,alpha)K_(a,alpha)` changes fine labels but not `I_a`; summing the dilation fiber leaves every record probability fixed | **PASS**; rotations across physical outcome sectors are not gauge unless the complete record/reader packet is transformed |

## 5. Quantum claim audit

| Candidate claim | Seat Q finding |
|---|---|
| finite causal process realization | **PASS** for finite-dimensional causally ordered combs/process tensors |
| positive normalized record pushforward | **PASS**; ordinary probability on records, not a microscopic path law |
| sequential and tensor naturality | **PASS-WITH-SCOPE** at the operational whole-program quotient; not a functor of intermediate positive kernels |
| instruments, mixtures, control, conditioning, ancilla, discard | **PASS** for finite outcomes; conditioning keeps its success probability |
| standard-Borel extension | **PASS-WITH-SCOPE** for measurable instrument/control kernels and almost-everywhere disintegration; no pointwise posterior is fixed on null outcomes |
| CHSH and Peres--Mermin | **PASS** as contextual operational quantum predictions; no local/noncontextual completion |
| distinct memory/division notions | **PASS** with the carrier and intervention interface printed |
| record transport/uncompute/leakage triad | **PASS** in the declared common finite model |
| first-order realizer nonselection | **PASS**; exact two-measure counterexample |
| `KJ` operational identity and `JK` ontological nonidentity | **PASS-WITH-SCOPE** on the image of `J`; this is representation, not ontic equivalence |
| phase-complete structure remains necessary | **PASS**; diagonal-only state is refuted, though complex numbers themselves are not uniquely forced by that example |
| compositional equivalence with ontology debt | **PASS** and is the maximum justified ceiling |

## 6. Registered controls C1--C12

| Control | Verdict | Reason |
|---|---|---|
| C1 phase completeness | **PASS** | arbitrary unitaries cover the whole `U_phi` family; the held-out `H` reader yields the exact sinusoid and phase addition is preserved |
| C2 general dimension | **PASS** | finite-dimensional Kraus/Stinespring and causal-comb realization are uniform in every finite dimension |
| C3 disturbance | **PASS** | both the printed projective example and the fresh unsharp POVM example separate effect from channel |
| C4 CHSH | **PASS** | exact correlations, `2 sqrt(2)`, and no-signalling marginals reconstructed |
| C5 Peres--Mermin | **PASS** | three row products and first two columns are `+I`; final column is `-I`; no context-independent table is asserted |
| C6 product/entangled | **PASS** | product dilations factor; entangled sources remain global; discard and blank ancilla are correct pushforwards |
| C7 process memory | **PASS** | causal-break Markov and retained-memory examples both represented |
| C8 nondivision translation | **PASS** | `H,H` separates interference nondivision from operational process memory; CP divisibility has its own counterexample |
| C9 record triad | **PASS** | transported sector, complete inverse, and remote leak give distinct exact predictions |
| C10 convex randomization | **PASS** | a physical independent coin gives the affine sum of complete instrument laws |
| C11 gauge packet | **PASS-WITH-SCOPE** | Kraus/dilation and full-packet basis covariance are correct; the manuscript does not prove a classification theorem for every automorphism of the operational category |
| C12 v16 regression | **NONCONTRADICTION ONLY** | no v16 object is embedded; the limited claim made by the paper is accurate |

## 7. Hostile attacks 1--42

| No. | Disposition |
|---:|---|
| 1 | **PASS** — diagonal-only state is separated by a common continuation. |
| 2 | **PASS-WITH-COST** — no terminal row is stored, but the uniform evaluator is exactly the retained quantum/Born construction. |
| 3 | **PASS-WITH-COST** — the hidden-Hilbert-wrapper null applies descriptively; the paper openly calls the result representational and earns no elimination. |
| 4 | **PASS** — Kraus labels are summed and not beables. |
| 5 | **PASS** — no preferred configuration PVM is claimed; the missing discriminator is printed. |
| 6 | **PASS** — all finite dimensions follow from the general realization. |
| 7 | **PASS** — tomography is a fixed separating operational class, not post-selected data. |
| 8 | **PASS-WITH-SCOPE** — equality is under all wired continuations, not one reader; the stochastic image has no independent composition beyond the retained program class. |
| 9 | **PASS** — tensor wiring acts on ports, source/process data, dilations, and records. |
| 10 | **PASS** — entanglement is a global source state, not pre-agreed local values. |
| 11 | **PASS** — unused product ancillas contribute a normalized factor. |
| 12 | **PASS** — discard is complete marginalization/partial trace. |
| 13 | **PASS** — physical coin control gives affinity. |
| 14 | **PASS** — postselection is conditional probability with the success record and weight retained. |
| 15 | **PASS** — the CHSH source is held fixed independently of later setting coins. |
| 16 | **PASS** — operational no-signalling is not promoted to ontic locality. |
| 17 | **PASS-WITH-SCOPE** — the whole-program law is global, but no hidden lookup is promoted to an ontic causal mechanism. |
| 18 | **PASS** — measurement context is a typed physical control/apparatus component. |
| 19 | **PASS** — the Peres--Mermin contradiction blocks the forbidden table. |
| 20 | **PASS** — no retrocausal label is used. |
| 21 | **PASS** — unrecorded slots are not declared complete stochastic divisions. |
| 22 | **PASS-WITH-COST** — memory may scale with each finite target and is declared; no uniform constant bound is claimed. |
| 23 | **PASS** — ignored slots insert the deterministic operation and coarse-grain its record. |
| 24 | **PASS** — memory is diagnosed by a causal break, not correlation alone. |
| 25 | **PASS** — CP divisibility, process memory, and stochastic division remain separate. |
| 26 | **PASS** — program order is explicitly external laboratory order. |
| 27 | **PASS** — known sector swap is transport, not erasure. |
| 28 | **PASS** — the remote environment copy blocks the claimed uncompute. |
| 29 | **PASS** — records do not select actuality. |
| 30 | **PASS** — microscopic trajectory incompleteness is explicit. |
| 31 | **PASS** — readers coarse-grain a pre-existing record measure. |
| 32 | **PASS** — the whole dilation fiber is summed. |
| 33 | **PASS** — absent microscopic variables receive no uniform distribution. |
| 34 | **PASS** — no empirically idle order is called chronology. |
| 35 | **PASS** — process/preparation data are arguments distinct from the universal evaluation rule. |
| 36 | **PASS** — no root or cosmological selector appears. |
| 37 | **PASS** — QFT and continuous-variable systems are excluded. |
| 38 | **PASS** — laboratory order is not spacetime order. |
| 39 | **PASS** — `JK` ontological nonidentity is central to the result. |
| 40 | **PASS** — exact equivalence is not empirical evidence for ISP. |
| 41 | **PASS** — no no-go for Barandes or all relational ontologies is claimed. |
| 42 | **PASS** — no Paper 13D constants or binary carriers enter the construction. |

## 8. Exact scope and quantifiers

| Axis | Seat Q accepted scope |
|---|---|
| dimensions | all finite system and finite ancillary dimensions |
| slots | every fixed finite number in a supplied causal laboratory order |
| process class | deterministic causally ordered process tensors/quantum combs and their CP instruments; not indefinite-causal-order process matrices |
| outcomes | finite outcomes exactly; standard-Borel outcomes for countably additive CP instruments with measurable adaptive kernels |
| conditioning | positive-probability record events, or regular conditional states defined almost everywhere in the standard-Borel case |
| instruments | arbitrary CP trace-nonincreasing instruments, not POVMs alone |
| memory | finite for each finite comb; not necessarily minimal and with no uniform process-independent bound |
| contextuality | experiment-context dependence is physical and allowed; no common counterfactual value table |
| Bell status | exact operational no-signalling; no Bell-local ontic completion or relativistic causal account |
| construction type | uniform existence/compilation from the full target quantum process; not a finite answer catalogue |
| state/law | process and preparation are contingent/controlled inputs to a fixed Born-dilation rule |
| order | external laboratory control order only |

The direct-integral argument can be made exact as follows.  If `J(B)` is the
finite matrix-valued Choi measure and `mu(B)=tr J(B)`, then
`J(B)=int_B j(x)dmu(x)` with positive measurable `j(x)`.  A measurable square
root gives finitely many measurable Kraus fields `K_alpha(x)` and

$$
(V\psi)(x)=\sum_\alpha K_\alpha(x)\psi\otimes e_\alpha,
$$

where `V` is an isometry because the integrated instrument is trace
preserving.  Multiplication by indicator functions of Borel sets supplies the
record PVM.  This validates the existence claim.  It does not select a unique
posterior on a null singleton, and finite adaptive composition additionally
requires the family chosen from past records to be measurable.  These are the
scope qualifications in the verdict, not counterexamples to the construction.

## 9. Full 17-coordinate product

```text
target        P01-QUANTUM-PROCESS-TARGET-BOUND
               (finite-dimensional, finite-slot, causally ordered)
referent      P01-STOCHASTIC-RECORD-HISTORY-REFERENT-CONSTRUCTED
               + P01-MICROSCOPIC-HISTORY-REFERENT-INCOMPLETE
state-law     P01-STATE-LAW-SEPARATION-CONSTRUCTED-AT-OPERATIONAL-SCOPE
single        P01-ALL-FINITE-SINGLE-SYSTEM-CORRESPONDENCE
instrument    P01-COMPLETE-INSTRUMENT-TRANSLATION
               (finite; measurable standard-Borel extension)
sequential    P01-SEQUENTIAL-NATURALITY-SCOPED-TO-WHOLE-PROGRAM-EVALUATION
tensor        P01-TENSOR-NATURALITY
bell          P01-BELL-NOSIGNALING-REPRODUCED-WITH-WHOLE-PROGRAM-CONTEXT
               + P01-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
context       P01-CONTEXTUALITY-PHYSICALLY-TYPED
multitime     P01-FINITE-CAUSALLY-ORDERED-MULTITIME-PROCESS-EQUIVALENCE
memory        P01-MEMORY-INDIVISIBILITY-RELATION-CLASSIFIED
record        P01-DECOHERENCE-RECORD-ERASURE-TRIAD
equivalence   P01-NATURAL-OPERATIONAL-EQUIVALENCE-ON-THE-RECORD-QUOTIENT
               + P01-REPRESENTATION-ONLY
hilbert       P01-HILBERT-SECONDARY-AS-ASSERTED-BEABLE
               + P01-PHASE-COMPLETE-QUANTUM-STRUCTURE-IRREDUCIBLE-IN-CONSTRUCTION
ontology      P01-CONFIGURATION-ONTOLOGY-UNDERDETERMINED
actuality     P01-ONE-ACTUAL-RECORD-HISTORY-POSTULATED
               + P01-MICROSCOPIC-ACTUALITY-UNCONSTRUCTED
preferred     P01-PREFERRED-STRUCTURE-COST-PRESENT
               (configuration algebra unselected; laboratory order supplied)

overall ceiling
              P01-COMPOSITIONAL-OPERATIONAL-EQUIVALENCE-WITH-ONTOLOGY-DEBT
```

## 10. Verdict and repair classification

**Verdict: `ACCEPT-WITH-SCOPE`.**

First decisive semantic counterexample: **none**.

The finite-outcome Q0--Q3 representation survives every Seat Q control.  The
standard-Borel claim survives with the measurable-kernel and almost-everywhere
conditioning qualifications printed in Sections 1 and 8 of this report.  The
Bell label must be read as a contextual whole-program operational law, not a
constructed ontic causal story.  These are bounded scope/wording constraints;
they do not require new physics or a different construction.

The paper's main scientific lesson is narrower but cleaner than an ontology:
ordinary positive probabilities on actual laboratory records are compatible
with all finite causally ordered quantum-process statistics, provided the
phase-complete quantum process remains available to evaluate the indivisible
whole.  This neither removes quantum structure nor selects what exists behind
the records.

A code implementation could not change this verdict.  The positive result,
the scope qualifications, and the ontology debt are mathematical and
conceptual; software can only conform to or fail to conform to them.

## 11. Freeze statement

This report is left unstaged and uncommitted on handoff.  Its ordinary
post-freeze SHA-256, LF line count, and byte count are necessarily returned
outside the bytes whose hash they describe.  No normalized self-hash
convention is used.
