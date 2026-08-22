# Empirical quantum-adequacy contract

Date: 2026-08-22

Status: **REFERENCE CONTRACT — standard quantum process theory defines the
target; no candidate is awarded adequacy**

## 1. Why this contract comes first

The first v17 question is not whether one stochastic matrix displays
interference-like nondivision. Quantum physics is a compositional experimental
theory. A proposed ontology must assign probabilities coherently across
preparations, transformations, instruments, adaptive choices, composite
systems, and multiple times.

This contract freezes the target before a replacement is designed. It blocks
the recurrent move of testing only those experiments already native to a toy
law.

## 2. Standard comparator

The registered comparator is finite-dimensional operational quantum theory.
For each finite-dimensional complex Hilbert space `H` it contains:

- density operators `rho`;
- completely positive trace-nonincreasing operations;
- instruments whose operation sum is trace preserving;
- unitary and isometric transformations;
- effects and POVMs;
- tensor composition;
- classical control and outcome conditioning;
- quantum combs/process tensors for multi-slot experiments.

For an experiment `e` and outcome string `o`, the comparator supplies

\[
p_{\rm Q}(o\mid e).
\]

The target is the complete family of these probabilities on the frozen
experiment class, not a preferred Kraus representation, wavefunction, basis,
or circuit decomposition.

Hilbert space is the reference representation at this stage. Whether it is
ontic is an output coordinate.

## 3. Candidate interface

A candidate relational stochastic theory supplies

\[
(\mathsf{Cfg},\mathsf{Exp},\omega,\boldsymbol\Gamma,
 \mathsf{Read}),
\]

with:

- a configuration/history referent independent of diagnostic readers;
- a contingent preparation/state `omega`;
- one compatible family `Gamma-bold` over complete histories;
- typed operational embeddings of every registered quantum experiment;
- outcome maps giving ordinary nonnegative probabilities.

For an embedding `J`, operational adequacy is

\[
p_{\rm S}(o\mid J(e),\omega_e)=p_{\rm Q}(o\mid e)
\]

for every registered `e,o`, with preparation dependence carried by `omega_e`
or a typed preparation arrow rather than retuning the universal law.

The equality must respect composition. Independent experiment-by-experiment
lookups do not count.

## 4. Scope tiers

| Tier | Required content | Paper 01 status |
|---|---|---|
| Q0 | finite-dimensional prepare–transform–measure probabilities | required |
| Q1 | sequential instruments, adaptive control, disturbance, ancillas | required |
| Q2 | composites, entanglement, Bell/no-signalling, contextuality | required |
| Q3 | arbitrary finite-slot process tensors/combs and operational memory | required |
| Q4 | continuous variables, unbounded systems, identical-particle QFT | deferred, explicitly unearned |
| Q5 | quantum fields on dynamical geometry and quantum gravity | closed |

Passing Q0 alone earns only a single-system representation. Paper 01's
strongest possible mathematical outcome requires Q0–Q3.

## 5. Registered benchmark families

### B1 — continuous phase and interference

For a qubit path basis, admit a continuous phase

\[
U_\phi=|0\rangle\!\langle0|+e^{i\phi}|1\rangle\!\langle1|,
\qquad \phi\in[0,2\pi).
\]

A balanced interferometer produces a sinusoidal fringe over the whole phase
circle. A candidate must reproduce the complete continuous family, including
composition `U_phi U_theta = U_(phi+theta)`, not only finitely sampled phases.

Discriminator: two candidate preparations with the same basis probabilities
and different relative phase must be operationally distinguishable after a
common recombiner. A model whose complete physical state is only the diagonal
probability vector fails unless an independently typed history variable
retains the missing information.

### B2 — arbitrary finite-dimensional transformations

For every registered finite dimension `d`, preparations and effects must
separate states, and admitted transformations must reproduce arbitrary
unitaries and general quantum instruments. The theorem target is uniform in
`d`, not a census of `d=2` examples.

Required composition laws include identity, sequential composition, convex
mixing by a physical classical randomizer, and reversible dilation. A
different stochastic law for each target unitary is permitted only if these
laws are images of one uniform construction and share the same ontology and
composition rule.

### B3 — mixtures and purification

Operationally identical mixtures must remain identical under every future
registered experiment. Distinct purifications of one reduced state must be
related in the standard way at the composite level. The candidate must state
whether mixedness is epistemic, ontic, or representation-dependent and expose
that choice to the complete experiment class.

Discriminator: an ensemble decomposition label that changes later local
predictions without an accessible physical record fails preparation
noncontextuality at the operational level.

### B4 — instruments and disturbance

An instrument is not merely an outcome distribution. It specifies the
post-outcome process available to later experiments. Candidates must reproduce
both:

\[
p(a\mid \mathcal I,\rho)
\quad\text{and}\quad
p(b\mid \mathcal J, a,\mathcal I,\rho)
\]

for arbitrary registered continuations. Two instruments with equal immediate
POVM statistics but different disturbance are required to remain distinct.

This is the primary defense against replacing a quantum process by a table of
terminal probabilities.

### B5 — tensor composition and entanglement

Independent systems require a compositional product compatible with local
instruments and classical control. Entangled preparations must not be recoded
as a list of pre-agreed local outcomes unless the recoding survives Bell and
contextuality gates.

Required controls:

- product preparations factor under product measurements;
- entangled preparations produce nonfactorizing joint laws;
- local marginal statistics are invariant under the remote measurement
  choice in the no-signalling regime;
- discarding a subsystem agrees with marginalization;
- adding an unused ancilla is an operational non-kill.

### B6 — Bell/CHSH

Use a two-party, two-setting, two-outcome experiment with freely chosen
settings in the declared operational model. The quantum target includes a
state and observables attaining

\[
S_{\rm CHSH}=2\sqrt2,
\]

while each party's marginal is independent of the other party's setting.

The candidate must identify which Bell premise it does not satisfy. Allowed
classifications include:

- nonlocal ontic dependence;
- contextual/global history law without superluminal operational signalling;
- measurement dependence, if openly postulated and independently tested;
- retrocausal or all-at-once boundary dependence, if typed and not a label for
  ordinary fine tuning;
- rejection of outcome independence or parameter independence with exact
  operational consequences.

It may not claim Einstein locality merely because the observable marginals do
not signal. It may not hide settings in the preparation while calling them
free.

### B7 — contextuality

Use the Peres–Mermin square as an exact algebraic control:

\[
\begin{array}{ccc}
X\otimes I&I\otimes X&X\otimes X\\
I\otimes Y&Y\otimes I&Y\otimes Y\\
X\otimes Y&Y\otimes X&Z\otimes Z
\end{array}
\]

The commuting row products and first two column products are `+I`, while the
last column product is `-I`. No context-independent assignment of pre-existing
`±1` values satisfies all six constraints.

A stochastic ontology may be contextual. If it is, the context must be a
physical part of the experiment/history interface, not an evaluator lookup
key omitted from the ontology. The result must distinguish contextuality from
signalling and from mere measurement disturbance.

### B8 — multi-time process completeness

For every registered finite slot set, a process tensor/quantum comb maps a
sequence of admissible CP operations to a joint outcome probability. The
candidate must provide a corresponding multi-time law satisfying:

- linearity/affinity in independently randomized instruments at the
  operational level;
- complete positivity under unused ancilla extension in the representation;
- normalization for every deterministic instrument sequence;
- consistency under ignored slots;
- compatibility with sequential and parallel composition;
- tomography by a separating instrument set.

A first-order transition kernel plus hidden cache is not automatically a
solution. If memory is physical, it belongs to the declared configuration or
history referent and its resource cost is reported.

### B9 — Markov, memory, and indivisibility

The following notions remain distinct:

1. failure of a stochastic restart kernel on a proposed carrier;
2. operational quantum non-Markovianity under causal-break instruments;
3. memory in an enlarged state;
4. failure of CP divisibility of a reduced channel;
5. interference at an unrecorded alternative;
6. grammar-relative stable records.

Paper 01 must give translation theorems or counterexamples between the
Barandes indivisibility condition and the process-tensor operational Markov
condition. Same numbers in one two-step example are not a general equivalence.

### B10 — decoherence, stable records, erasure, and uncomputation

Register one common unitary model with system `S`, record `R`, and environment
`E`.

- A record-writing isometry correlates alternatives with orthogonal record
  sectors.
- Restricted future operations preserving the record algebra suppress the
  corresponding interference operationally.
- A known unitary sector swap transports the record; it is not erasure.
- A reversible uncomputation can restore interference if all which-alternative
  information is coherently removed from every relevant degree of freedom.
- Tracing out or irreversibly merging the record gives a different physical
  experiment.

The candidate must reproduce the quantum predictions for all five cases and
state what is actual between interventions. Stable records do not select an
outcome by themselves.

### B11 — tomography and hidden differences

Adequacy is measured on a separating family. Two candidate laws are
operationally equivalent only if all registered process-tomography
probabilities agree. A hidden variable that never affects any allowed
experiment is ontologically underdetermined, not empirically discovered.

The protocol must include held-out instrument sequences not used in fitting
or constructing the candidate map.

### B12 — gauge and representation

Quantum descriptions have basis, Kraus, dilation, and phase redundancies.
The stochastic representation may have additional gauge freedom. Every gauge
claim must specify:

- the complete object transformed;
- the experiment class left invariant;
- the induced map on histories and beables;
- whether the transformation is empirical gauge, ontological isomorphism, or
  only a change of calculation.

Equal terminal probabilities under one reader do not establish gauge.

## 6. Natural equivalence target

The strongest Paper 01 mathematical target is not a cellwise equality table.
It is a pair of translations on the registered domain:

\[
\mathcal Q_{\rm fd}^{\rm proc}
\xrightarrow{\;J\;}
\mathcal S_{\rm rel}^{\rm indiv}
\xrightarrow{\;K\;}
\mathcal Q_{\rm fd}^{\rm proc},
\]

such that:

1. `KJ` is operationally naturally equivalent to the identity;
2. `J` respects typed sequential and tensor composition;
3. all process probabilities agree;
4. coarse-graining, conditioning, and discarded systems commute with the
   translations at their licensed boundaries;
5. `J` identifies the contingent state separately from the fixed law;
6. the stochastic history and actualization semantics are explicit;
7. any failure of `JK` to be ontologically the identity is classified as
   representational redundancy or genuine extra ontology.

An existence theorem without `J`'s compositional naturality earns only
representation, not a complete alternative formulation.

## 7. Ontology questions that probabilities alone do not answer

Even exact operational equivalence leaves open:

- whether configurations or histories are primary;
- whether the law is local in any emergent spacetime sense;
- whether wavefunctions are nomological, epistemic, gauge, or eliminable;
- whether a unique actual trajectory is primitive;
- whether measurement settings are free variables, boundary data, or part of
  one global history;
- whether the stochastic ontology is preparation contextual;
- whether continuous complex phase has an ontic counterpart;
- whether two empirically equivalent stochastic realizers are ontologically
  different.

Paper 01 must report these as a product vector rather than hide them behind a
single `PASS`.

## 8. Registered nulls and attacks

1. **Diagonal null:** retain only basis probabilities; must fail B1.
2. **Terminal-table null:** store final probabilities per experiment; must
   fail B4/B8 composition or resource bounds.
3. **Kraus-label ontology:** let nonunique Kraus indices be beables; must fail
   gauge/operational invariance unless independently fixed.
4. **Hidden-Hilbert wrapper:** call the wavefunction a stochastic cache while
   using it unchanged for every prediction; classify as representation, not
   ontological elimination.
5. **Bell-local lookup:** preassign local outcomes independent of remote
   settings; must fail B6.
6. **Superdeterministic smuggle:** correlate settings with the source without
   declaring measurement dependence; refuse.
7. **Context erasure:** identify operationally distinct contexts in B7; fail.
8. **Context lookup:** retain context only in source code, not in physical
   experiment/history; fail ontology completeness.
9. **Markov checkpoint:** force factorization at every instrument slot; must
   fail a registered memory process.
10. **Infinite hidden cache:** reproduce a finite suite by unbounded history
    storage; report resource class and fail any stronger finite-sufficiency
    claim.
11. **Representative mass:** assign orbit representatives rather than full
    pushforward probability; fail normalization/covariance.
12. **Prepared-answer ancilla:** put the future reader choice or outcome in an
    allegedly unused ancilla; fail no-smuggling.
13. **Postselection:** discard unfavorable histories without including the
    success flag and probability; fail normalization.
14. **Absolute record:** claim permanence while a registered global
    uncomputation restores interference; fail B10.
15. **Sector-swap eraser:** call a known relabeling an erasure; fail B10.
16. **Mixture nonaffinity:** independently randomize two instruments and obtain
    a law different from the corresponding convex mixture; fail operational
    randomization.
17. **Unused hidden order:** add a latent chronology with no readout; classify
    as underdetermined, not derived.
18. **Finite-census overclaim:** pass qubits but claim all finite dimensions;
    refuse.
19. **Clock smuggle:** use program order as physical time without a clock
    record; refuse any temporal ontology claim.
20. **Geometry smuggle:** assign distances to configuration labels; outside
    Paper 01 and nonpromotive.

## 9. Result coordinates

Paper 01 reports independent coordinates:

```text
P01-QUANTUM-TARGET-BOUND / UNBOUND
P01-SINGLE-SYSTEM-REPRESENTATION-CONSTRUCTED / FAILED
P01-INSTRUMENT-COMPLETENESS-CONSTRUCTED / FAILED
P01-TENSOR-COMPOSITION-CONSTRUCTED / FAILED
P01-BELL-AND-NOSIGNALING-REPRODUCED / FAILED
P01-CONTEXTUALITY-TYPED / FAILED
P01-MULTITIME-PROCESS-EQUIVALENCE-CONSTRUCTED / FAILED
P01-DECOHERENCE-RECORD-ERASURE-TRIAD-CONSTRUCTED / FAILED
P01-NATURAL-OPERATIONAL-EQUIVALENCE-CONSTRUCTED / UNPROVEN
P01-CONFIGURATION-ONTOLOGY-COMPLETE / INCOMPLETE / UNDERDETERMINED
P01-PREFERRED-STRUCTURE-COST-NONE / PRESENT / UNTESTED
P01-HILBERT-ONTOLOGY-ELIMINATED / REPRESENTATION-ONLY / UNRESOLVED
P01-ACTUAL-HISTORY-SEMANTICS-CONSTRUCTED / POSTULATED / UNCONSTRUCTED
```

No total verdict may conceal a mixed product.

## 10. What Paper 01 cannot earn

Even the strongest Paper 01 result cannot earn:

- background independence;
- removal of external laboratory time;
- relativistic locality;
- QFT;
- a cosmological state;
- a unique law of nature;
- dimension, signature, topology, metric, curvature, or gravity;
- an explanation of coupling constants;
- empirical superiority to quantum theory;
- ontological uniqueness.

It can earn a sound foundation on which those questions become meaningful.

## 11. Source spine

- Barandes's indivisible stochastic formulation and stochastic–quantum
  correspondence: <https://arxiv.org/html/2507.21192v1> and
  <https://arxiv.org/abs/2309.03085>.
- Quantum combs/networks: <https://arxiv.org/abs/0904.4483>.
- Complete non-Markovian process framework and operational Markov condition:
  <https://arxiv.org/abs/1512.00589> and
  <https://arxiv.org/abs/1801.09811>.
- Bell's theorem: <https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195>.
- Decoherence/einselection: <https://arxiv.org/abs/quant-ph/0105127>.
- Operational reconstruction principles and purification as a discriminator:
  <https://arxiv.org/abs/1011.6451>.

These references define questions and standard comparators. Paper 01 must
reconstruct every theorem it uses at the declared mathematical scope.
