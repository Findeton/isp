# Relativistic ISP V5 Paper 10: Quantum Algorithms As Record-Amplification Machines

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper interprets quantum algorithms
as machines that amplify answer-compatible records and suppress wrong records
through controlled transport and interference.

## Abstract

Quantum algorithms are often described as using superposition and
interference.  ISP sharpens this: an algorithm is a finite record-amplification
machine.  It prepares unresolved alternatives, applies structured transports,
and arranges recombination so that output records compatible with the answer
have high stabilization weight.

The central claim is:

$$
quantum algorithm = controlled amplification of answer-compatible records
$$

Searchable paper tag:

`V5P10-QUANTUM-ALGORITHMS-RECORD-AMPLIFICATION-MACHINES`.

## 0. Purpose

This paper gives an ISP account of why different algorithms work without
claiming that ISP changes their standard correctness proofs.

## 1. Algorithm Template

Every quantum algorithm has five record stages:

1. input record;
2. unresolved branch preparation;
3. structured transport;
4. interference or amplitude reshaping;
5. stable output record.

The algorithm succeeds when answer records have increased stabilization
weight.

## 2. Grover Search

Grover becomes a record-weight rotation:

$$
wrong records suppressed, target-compatible record amplified
$$

The oracle marks the compatibility class.  The diffusion step reshapes the
branch weights.  Measurement stabilizes the amplified record.

## 3. Shor And Period Finding

Shor becomes period-record extraction:

$$
modular transport periodicity -> Fourier readout -> period record
$$

The final factorization is classical post-processing of a period record.

## 4. Quantum Walks

Quantum walks become controlled transport on a graph of possible records.  The
speedup comes from holonomy and interference across paths, not from trying all
classical paths as separate worlds.

## 5. Main Gate

| Gate | Meaning |
| --- | --- |
| RA1 | problem has answer-compatible output records |
| RA2 | finite transports can reshape branch stabilization weights |
| RA3 | wrong records are suppressed by recombination |
| RA4 | final measurement samples the amplified record class |

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| RAF1 | algorithmic success does not correlate with record-weight amplification |
| RAF2 | wrong records remain equally stable after the designed transport |
| RAF3 | output statistics cannot be tied to finite transport structure |
| RAF4 | speedup appears without nonclassical transport or nonfactorization |

## 7. Initial Verdict

Quantum algorithms are not magic parallelism.  They are structured finite
transport procedures that make some records easier to stabilize than others.

## 8. Developed Algorithm Ledger

An algorithm is a finite record-amplification ledger:

$$
A = (Prepare, Transport, Interfere, Amplify, Stabilize)
$$

The success condition is:

$$
weight(answer-compatible records) >> weight(wrong records)
$$

at the final readout interface.

## 9. Amplitude Amplification

Amplitude amplification is record-weight rotation in a two-dimensional
effective subspace:

| Direction | ISP meaning |
| --- | --- |
| good subspace | answer-compatible records |
| bad subspace | answer-incompatible records |
| oracle reflection | mark compatibility structure |
| diffusion reflection | rotate stabilization weight |

The algorithm does not inspect every record.  It reshapes the final
stabilization distribution.

## 10. Period-Finding Algorithms

Period finding follows the pattern:

$$
hidden structure -> controlled transport -> holonomy -> stable period record
$$

The algorithm is efficient when the hidden structure is compactly encoded in a
transport defect and the readout interface can expose that defect without
expanding all classical alternatives.

## 11. Hamiltonian Simulation

Quantum simulation algorithms become controlled record transports that emulate
another physical transport ledger.

The ISP content is:

$$
simulate dynamics = reproduce finite record transport statistics of target system
$$

This is especially natural for chemistry and QFT simulation because the
output is usually not a full state record, but a finite observable record.

## 12. Algorithmic Resource Table

| Algorithm family | ISP resource |
| --- | --- |
| Grover/amplitude amplification | record-weight rotation |
| Shor/period finding | holonomy-to-period readout |
| phase estimation | transport-defect measurement |
| quantum walks | path-interference on record graph |
| HHL-like linear systems | spectral record filtering |
| simulation | target transport emulation |

## 13. Mature Verdict

Paper 10 develops the algorithmic thesis: quantum algorithms work when they
engineer finite transports so answer-compatible records are the records most
likely to stabilize.  This is a precise alternative to the misleading image of
many worlds trying all answers independently.

## 14. Formal Closure

### Definition 14.1: Record-Amplification Algorithm

A record-amplification algorithm is a finite transport packet:

$$
\boxed{
{\mathcal A}
=
(
{\mathcal R}_{cand},
{\mathcal R}_{good},
K,
{\mathcal M}_{out}
)
}
$$

where \(K\) increases the stabilization weight of answer-compatible records
relative to answer-incompatible records.

### Lemma 14.2: Amplitude Amplification Is Weight Rotation

In the two-dimensional good-bad subspace:

$$
\boxed{
K^q
:
w_{good}
\longmapsto
\sin^2((2q+1)\theta).
}
$$

Proof.  The oracle reflection and diffusion reflection generate a rotation in
the span of the good and bad components.  The final measurement stabilizes the
good record with the displayed rotated weight.  Thus amplitude amplification
is record-weight rotation, not enumeration of all candidates.

$$
\square
$$

### Lemma 14.3: Period Finding Is Holonomy Compression

Period finding is efficient when the hidden period is encoded as a compact
transport defect:

$$
\boxed{
\hbox{hidden period}
\longrightarrow
\hbox{controlled transport holonomy}
\longrightarrow
\hbox{finite period record}.
}
$$

Proof.  Modular exponentiation creates a periodic transport structure.  The
Fourier interface converts that structure into a finite record concentrated
near rational multiples of the inverse period.  Classical postprocessing then
extracts the period from the stable record.

$$
\square
$$

### Lemma 14.4: Simulation Is Target Transport Emulation

A quantum simulation succeeds when finite observables of the simulated device
match finite observables of the target transport:

$$
\boxed{
P_{\mathrm{device}}(r)
=
P_{\mathrm{target}}(r)
}
$$

for every licensed output record \(r\).

Proof.  Simulation does not need to copy an entire hidden state.  It needs to
reproduce the finite record statistics requested by the experiment.  A device
that matches those finite statistics emulates the target transport at the
specified resolution.

$$
\square
$$

### Theorem 14.5: Paper 10 Closure

Quantum algorithms are record-amplification machines:

$$
\boxed{
\hbox{algorithmic advantage}
=
\hbox{efficient transport that amplifies answer-compatible records}.
}
$$

Proof.  Lemma 14.2 closes amplitude amplification.  Lemma 14.3 closes period
finding.  Lemma 14.4 closes simulation.  The table in Section 12 is therefore
not only a dictionary but a common theorem schema.

$$
\square
$$
