# Paper 17C relational sum-over-processes investigation note

## Status

This note records a physics-first investigation of whether known quantum
physics can motivate the autonomous occurrence law missing after Paper 17B.
It is not a frozen scientific pin and awards no new physical coordinate.

No implementation, evaluator, random case, dimension fit, metric object, or
geometry reconstruction was used.

## Bound inputs

- Paper 13D terminal law SHA-256:
  `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9`
- Paper 13D terminal adjudication SHA-256:
  `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9`
- Paper 17B SHA-256:
  `e426fd19d29fa0fa8621b4e6402e9b45fc3d4d820164dc6322b920dfa1e38ef9`
- Paper 17B construction note SHA-256:
  `55c08b40e74a9706feee69c5f0080b4247f675bfc5db04294c5edf74fa607307`

## Principal result

The accepted conditional law has an exact occurrence gauge. If a compatible
joint weight is multiplied by any positive point-free function of the
unmarked process complex, every conditional Paper 13D probability remains
unchanged. In a local action basis this includes arbitrary generator
activities

\[
 \prod_\gamma\lambda_\gamma^{N_\gamma(\chi)}.
\]

A quantum lift has an additional sector-phase freedom. Multiplying every
amplitude in process sector \(\chi\) by

\[
 r(\chi)e^{i\theta(\chi)}
\]

leaves normalized within-sector probabilities unchanged while altering
autonomous weights and possible cross-sector interference.

Therefore neither the new activities nor the cross-complex phases can be
reconstructed from \(\mathbf\Gamma_D\).

## Quantum-physics comparison

### Feynman sum over histories

Useful: it says coherent alternatives receive complex contributions and that
the physical amplitude is their sum.

Missing: a relational action, base measure, boundary state, and the evidence
that different Paper 13D process complexes are coherent alternatives.

### Decoherence functional and quantum measure

Useful: they describe a closed single-history theory without requiring an
external measurement at every step and make recorded decoherent partitions
ordinary probability spaces.

Missing: all off-diagonal process-complex matrix elements and a unique
selection principle.

### General-boundary formulation

Useful: it provides region/boundary amplitudes and gluing without a preferred
temporal slicing.

Missing: the amplitudes themselves.

### Process matrices

Useful: they sharply separate local laboratory operations from a global
process and do not require a predefined global causal order.

Missing: a principle selecting one global process or its cosmological
occurrence law.

### Group field theory and spin foams

Useful: a single field action can generate a covariant sum over combinatorial
complexes as its Feynman expansion.

Missing or forbidden here: imported Lorentz/group labels, simplicial
dimension, fixed geometric valence, and post-hoc selection of a phase.

### Stochastic-quantum correspondence and dilation

Useful: the accepted stochastic laws can have Hilbert-space/unitary
representations on enlarged carriers. In Barandes's treatment, environmental
decoherence is ordinary leakage of correlations into the environment, seen as
loss of off-diagonal coherences in the reduced Hilbert representation.

Missing: a unique environment, unitary, process marginal, or cross-complex
phase. Representation is not autonomous selection, and decoherence does not
select which autonomous process complex occurs.

## Ontological decision

Paper 13D already assigns ordinary probabilities to complete physical history
classes. The primary successor target is therefore a complete indivisible
stochastic \(\Gamma_\star\), not a primitive complex-amplitude ontology.
Complex potentials, unitary dilations, and decoherence functionals are first
treated as nonunique representations of that completed law.

The preferred order is:

1. construct a complete point-free indivisible occurrence family;
2. classify all stochastic-quantum representations without selecting one;
3. compare matched one-route controls with one complete both-route law;
4. interpret a nonzero residual as failure of mixture factorization;
5. test separately whether any observation distinguishes a fundamental
   amplitude ontology from a complete stochastic realization.

A nonzero interference residual does not by itself force fundamental complex
amplitudes. In a Barandes-style account, the both-route experiment can have
its own indivisible stochastic whole law rather than being a mixture of the
two one-route laws.

Paper 13D's record eraser does not by itself count as recoherence. Erasing a
readable record field does not prove that all which-process information in an
environment has been reversed.

## Best candidate architecture

The best architectural candidate is a dimension-neutral relational action on
the accepted boundary and process groupoids:

\[
 S_{\rm rel}[\varphi]
 =\tfrac12\langle\varphi,K\varphi\rangle
 +\sum_\gamma\lambda_\gamma V_\gamma[\varphi].
\]

The action is not automatically quantum. With positive weights such as

\[
 P(\chi)\propto e^{-S_{\rm rel}(\chi)},
\]

it organizes a stochastic law. With complex contributions such as

\[
 \mathcal A(\chi)\propto e^{iS_{\rm rel}(\chi)/\hbar},
\]

coherent addition and an amplitude-to-probability rule are additionally
required. A complex field by itself proves neither interference nor a quantum
ontology.

The propagator glues exact compatible boundaries. Each interaction vertex is
one whole accepted physical generator. Native nondivision generators remain
atomic. External experiments are insertions, not autonomous vertices.

The action may not encode dimension through a geometric group, simplex, fixed
valence, lattice, topology, or background time.

## What remains genuinely new

The following are not present in Paper 13D:

- the process-history base measure;
- generator activities \(\lambda_\gamma\);
- cross-generator and cross-complex phases;
- an autonomous boundary/cosmological state;
- a coherent dilation of erasure;
- a normalized or constructive infinite-complex law; and
- a rule selecting one actual history.

Known quantum theory normally treats analogous couplings and boundary states
as physical input. It does not derive them merely from conditional outcome
probabilities.

## Required first experiments

1. Antichain versus fusion-star occurrence ratio.
2. Exact spectator/tensor factorization control.
3. Staged versus simultaneous fusion distinction.
4. Matched one-route and both-route experiments with a calibrated mixture
   reference.
5. Stable-record insertion and exact decoherence check.
6. Erasure followed by a genuine recoherence fringe test.
7. Finite-size restriction/projective consistency.
8. A phase or coupling calibration using only nongeometric microscopic
   occurrence data.

## Scope of current outcome

```text
P17C-INPUT-P13D-GAMMA-BOUND
P17C-OCCURRENCE-GAUGE-THEOREM-CONSTRUCTED
P17C-AMPLITUDE-LIFT-EXISTS-NONUNIQUELY
P17C-MIXTURE-FACTORIZATION-INTERFERENCE-UNTESTED
P17C-DECOHERENCE-DERIVATION-FROM-FULL-GAMMA-UNTESTED
P17C-FUNDAMENTAL-QUANTAL-ONTOLOGY-NOT-REQUIRED
P17C-RELATIONAL-FIELD-ACTION-CONTRACT-CONSTRUCTED
P17C-GENERATOR-COUPLINGS-UNSELECTED
P17C-NORMALIZED-SUM-OVER-COMPLEXES-UNCONSTRUCTED
P17C-DIMENSION-NONE-OCCURRENCE-LAW-UNBOUND
P17C-METRIC-UNCONSTRUCTED
P17C-ACTUALIZATION-UNCONSTRUCTED
```

## Recommendation

Do not choose an amplitude merely because quantum mechanics uses amplitudes.
Freeze the relational process-history space and positive occurrence-gauge
basis first, then construct the complete indivisible \(\Gamma_\star\). Only
afterward classify its amplitude and decoherence representations. An
interference residual rejects mixture factorization but does not by itself
force a fundamental complex-amplitude ontology.

If a new coupling remains free, report it as a fundamental constant or an
unselected family. Do not tune it to yield dimension four, manifoldlikeness,
or a desired metric.
