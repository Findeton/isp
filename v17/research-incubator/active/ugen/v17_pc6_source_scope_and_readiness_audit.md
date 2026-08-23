# ISP v17 — PC6 source, scope, and readiness audit

**Status:** ACTIVE AUTHOR-SIDE SOURCE/SCOPE AUDIT / NOT A PIN / NOT REVIEWED

**Date:** 2026-08-23

**Scientific result awarded:** none
**Authority created:** none

Audited object:

- `v17_pc6_scalable_markov_and_indivisible_frontier.md`.

---

## 1. Root verdict

```text
MONTINA M-SHORT THEOREM:          RECONSTRUCTED / CLASS-RELATIVE
WEAK INVERTIBILITY PREMISE:       EXPOSED / NOT DERIVED GLOBALLY
ROUND-OFF-TO-BITS BRIDGE:         CONDITIONAL / NOT IMPORTED
NON-MARKOV QUBIT CONTROL:         PRESENT / NOT SCALABLE
CONTEXTUAL STABILIZER LOWER:      QUADRATIC FINITE-ONLINE SCOPE
CONTEXTUAL STABILIZER UPPER:      QUADRATIC POSITIVE CONTROL PRESENT
PROCESS-TENSOR COMPARATOR:        COMPLETE OPERATIONAL TARGET / NOT ONTOLOGY
QHMM SPECTRAL RESULT:             PROMISING / VISIBILITY REPAIR REQUIRED
FINITE-CONTEXT GLEASON RESULT:    STRUCTURAL CONDITIONAL / NOT COST THEOREM
INDIVISIBLE GENERATOR CONTEST:    TYPED AUTHOR-SIDE / NO CANDIDATE YET
SCALABLE POSITIVITY NO-GO:        ABSENT
ONTOLOGY OR EMPIRICAL RESULT:     ABSENT
OFFICIAL FREEZE READINESS:        NO
```

The scientifically important correction is that no single resource notion is
allowed to stand for all the others. Existing results constrain different
interfaces. Their conjunction motivates a hard constructive question; it does
not already prove the PC6 trilemma.

---

## 2. Exact source receipts

The author-side reconstruction used the following retrieved arXiv versions.
The PDF bytes were inspected outside the repository; these receipts identify
the exact sources and do not make them ISP dependencies or results.

| Source | Bound version | PDF SHA-256 | Scope used |
|---|---|---|---|
| A. Montina, *State space dimensionality in short memory hidden variable theories* | [arXiv:1008.4415v2](https://arxiv.org/abs/1008.4415) | `6da900d3d55ffc8dda873c3387083a1d7e52b557698c1b781d365b7801f6b44c` | regular Markov $M\ge2N-2$ theorem, equality rigidity, non-Markov qubit control |
| A. Montina, *Epistemic view of quantum states and communication complexity of quantum channels* | [arXiv:1206.2961v1](https://arxiv.org/abs/1206.2961) | `f9fb5a474421444426180905ff1041be8e7af9b9bba9c9b7af6af3a6183b9f55` | mutual-information/communication bridge and qubit control |
| A. Karanjai, J. J. Wallman, S. D. Bartlett, *Contextuality bounds the efficiency of classical simulation of quantum processes* | [arXiv:1802.07744v1](https://arxiv.org/abs/1802.07744) | `f955de276b289dcb9abbe2eb3858116fa54a12fd5d0b574a5ebb9e471e9bc8a9` | finite online stabilizer memory lower bound |
| C. Hindlycke, J.-Å. Larsson, *Efficient Contextual Ontological Model of n-Qubit Stabilizer Quantum Mechanics* | [arXiv:2202.05081v2](https://arxiv.org/abs/2202.05081) | `1e97d568b23911e307b7b1be797957f010800c471f21789b4bdf034a6994cf28` | explicit quadratic contextual upper control |
| F. A. Pollock et al., *Non-Markovian quantum processes: complete framework and efficient characterisation* | [arXiv:1512.00589v3](https://arxiv.org/abs/1512.00589) | `67b2e293fae23007e96b9d57356a079ac3057283eb8c814aa8b48da6dd8bb848` | complete process-tensor interface and MPO control |
| F. A. Pollock et al., *Operational Markov condition for quantum processes* | [arXiv:1801.09811v1](https://arxiv.org/abs/1801.09811) | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` | causal-break Markov criterion and CP-divisibility control |
| M. Zonnios, A. Boyd, F. C. Binder, *Memory-minimal quantum generation of stochastic processes* | [arXiv:2412.12812v1](https://arxiv.org/abs/2412.12812) | `e59c943b2c72035c7d477ca7e33deca7b57adb7dc606fa1d1e474b8076af0843` | candidate process-visible spectral memory discriminator |
| A. Montina, S. Wolf, *Generalized Gleason theorem and finite amount of information for the context* | [arXiv:2206.11830v2](https://arxiv.org/abs/2206.11830) | `b2eb075245ac3596a5c1e9d6f2eae5fa67170557d74eeecea31fbd131cc29e0e` | finite-context conditional response structure |

---

## 3. M-SHORT premise audit

### 3.1 What is proved by the source

The theorem printed in arXiv:1008.4415v2 assumes a differentiable continuous
ontic manifold, positive Markov kernels, Montina's local support regularity
Property 1, and invertibility of all relevant nonzero processes. It concludes

$$
M\ge2N-2.
$$

The source allows preparation and measurement context. The obstruction is not
a noncontextuality theorem.

### 3.2 Compactness is not a substitute for Property 3

The source proves that, in a compact ontic space, processes along an infinite
series become arbitrarily close to invertible after transient behavior. The
main theorem nevertheless invokes Property 3 for all processes. PC6 therefore
prints weak invertibility as an antecedent rather than reporting it as a
general consequence of compactness.

### 3.3 The topology is load bearing

Property 1 invokes the local Euclidean structure of the ontic manifold and a
smoothly movable nonzero-support branch. The proof is not a result for an
arbitrary standard-Borel carrier or for a singular/fractal/nonmanifold history
space.

### 3.4 All-unitary scope is load bearing

The Lie-subgroup dimension argument requires access, through physical building
blocks and concatenation, to the generator directions used to cover $SU(N)$.
A restricted operational subtheory such as stabilizer mechanics is not in the
same antecedent.

### 3.5 Equality rigidity is not ontic selection

At minimal dimension the source identifies a Hilbert-axis variable evolving
by the Schrödinger equation, up to a discrete index. This says that members of
the minimal regular Markov class carry an equivalent geometric object. It
does not show that nature belongs to that class or that the Hilbert axis is an
empirically unique microscopic referent.

---

## 4. Resource-bridge audit

### 4.1 Continuous dimension

$M$ is a manifold dimension. A single real can have infinite Shannon
information, while many coordinates can be operationally insensitive. No bit
claim follows from $M$ alone.

### 4.2 Round-off information

The source's Section IV.E discretizes bounded coordinates and introduces
response sensitivities $g_i$. The claimed scaling requires a fixed error model
and the additional expectation that the geometric mean sensitivity does not
decay exponentially. PC6 records this as a conditional physical-resource
bridge, not part of M-SHORT.

### 4.3 Mutual information and communication

arXiv:1206.2961v1 establishes a bridge for a preparation/channel/readout
simulation: finite mutual information in a completely $\psi$-epistemic model
yields an amortized classical communication protocol, with an explicit
one-shot overhead. That bridge does not turn ontic dimension into
communication and does not cover an arbitrary adaptive multi-time process.

### 4.4 Online memory

The Karanjai--Wallman--Bartlett memory coordinate is the logarithm of the
cardinality of a finite simulator's internal state under their update and
single-shot-distinguishability axioms. It is not the description length of a
whole-program probability functional.

### 4.5 Quantum process representation

A process tensor's Choi state and MPO bond dimension quantify a quantum
representation. The most general bond dimension grows with the number of
steps, while many finite-environment processes can be compact. Neither number
is an ontic or laboratory cost without another bridge.

---

## 5. Hostile-control audit

### 5.1 Non-Markov shrinking

Montina's explicit one-dimensional qubit model escapes the Markov theorem.
Consequently PC6 cannot use M-SHORT against an indivisible whole-law or a model
whose future is not screened by the present ontic variable.

### 5.2 Efficient contextuality

The quadratic stabilizer construction prevents the claim that contextuality
alone forces exponential classical resources. It must be included in every
future scalable battery.

The model is not a universal quantum simulator: it is scoped to the stabilizer
subtheory, is $\psi$-ontic, and has nonlocal GHZ behavior. Those limitations do
not weaken its role as a hostile positive control.

### 5.3 Whole-program context

The finite online lower bound assumes that the current simulator state is not
a representation chosen with knowledge of the future measurement circuit. An
all-at-once or future-contextual law exits that theorem and must be charged in
$R_{\rm ctx}$ or $R_{\rm unif}$ rather than called a counterexample inside the
class.

### 5.4 QHMM visibility defect

The proof in arXiv:2412.12812v1 notes that an eigenvalue appearing in only one
presentation can have coefficient $\alpha_\lambda=0$. Such a mode is invisible
to the generated output process. A theorem phrased using every distinct
nonzero transfer eigenvalue therefore needs a process-visible-set correction
or an additional nonvanishing premise. The diagonalizability premise must also
be printed.

PC6 uses this source only as a candidate route, not as a certified lower bound.

### 5.5 Finite-context Gleason scope

arXiv:2206.11830v2 assumes finite relevant context information and local
regularity sufficient for its generalized Gleason theorem. It derives a
conditional linear form for measurements with at least three outcomes. The
authors explicitly state that they have not proved the existence of the
general finite-context ontological model. The result cannot be promoted into a
quantitative $R_{\rm ctx}$ theorem or a process generator.

---

## 6. Process-tensor scope audit

The process tensor is the correct complete operational comparator because it
supports arbitrary sequences of controls, including correlated/adaptive
operations, and has a representation theorem through open-system unitary
dynamics. Its containment property encodes the supplied ordering of
laboratory interventions.

Two ceilings follow:

1. reconstructing a target process tensor from tomography is not explaining
   its microscopic origin; and
2. the process tensor's slot order is not an emergent chronology.

The operational causal-break criterion supplies a fair boundary between a
future-sufficient cut and detectable memory. It also shows why CP divisibility
is not a sufficient Markov test.

---

## 7. Barandes/ISP scope audit

The existing v17 Barandes source audit finds one complete configuration space
and one contingent indivisible stochastic process per model, with external
real time, carrier-relative division, and supplied composite parent laws. It
does not find a general source theorem generating every interacting parent
law from subsystem laws and typed interaction data. It also does not prove
that such a generator is impossible.

PC6 therefore asks for uniform generation across a scalable experiment family.
It does not deny that a complete fixed parent law can represent the target.
The test is whether the proposed nomology explains the family without taking
the complete family as contingent input.

---

## 8. Assessment of the external direction review

The review of repository commit `421e7ca` was scientifically sound on the
following points:

1. Q-Cut is the best next official result-neutral unit;
2. Q-Cut constrains a positive future-sufficient cut, not all positive
   histories;
3. E-Comp belongs as a compact nonselection lemma/control;
4. U-Gen must be split into source completion, resource displacement, and a
   constructive contest;
5. the clock branch should wait for a native candidate law;
6. locality/Tsirelson and gravity must remain downstream; and
7. semantic lineage is necessary for imported author-side work.

The review is nine commits behind this packet. Since `421e7ca`, v17 has:

1. added the machine-readable semantic index and canonical `active/` layer;
2. repaired and source-bound Q-Cut;
3. separated E-Comp as a compact candidate lemma;
4. split U-Gen into its physical gates;
5. constructed PC2--PC3 source-completion classifiers;
6. supplied PC4's enlarged positive endpoint control; and
7. reached PC5's non-Clifford complete-process resource displacement.

PC6 implements the surviving scalable criticism. It does not retroactively
validate the preceding author-side candidates.

---

## 9. Readiness decision

PC6 is **not ready for an official pin** because:

1. it is a frontier synthesis rather than one theorem with a fixed admitted
   class;
2. the M-SHORT theorem is an external class theorem whose premises have not
   received independent v17 review;
3. the QHMM spectral route has a live visibility caveat;
4. no concrete indivisible generator has yet entered the contest;
5. the scalable target grammar and held-out family remain to be frozen; and
6. no physical-resource bridge or empirical deviation has been established.

Q-Cut remains the next recommended official unit if separately authorized.
The next author-side U-Gen construction should be the bounded U-Gen C1 pin
draft described in PC6, not another finite endpoint census.

No review, freeze, numbered paper, or automatic successor is opened by this
audit.
