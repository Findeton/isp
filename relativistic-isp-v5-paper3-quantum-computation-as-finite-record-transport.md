# Relativistic ISP V5 Paper 3: Quantum Computation As Finite Record Transport

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper translates the circuit model
of quantum computation into finite-record ISP language.  It is not a claim
that standard quantum circuits are wrong.  It is a record-ontology reading of
why the circuit model works.

## Abstract

This paper proposes the first ISP definition of a quantum computer: a device
that preserves unresolved finite record alternatives, transports them through
controlled nonclassical comparison maps, and then stabilizes an output record.
The ordinary circuit model is retained as the effective representation.  The
primitive ISP reading is finite record transport.

The central translation is:

$$
quantum circuit = controlled finite transport of unresolved record branches
$$

Searchable paper tag:

`V5P3-QUANTUM-COMPUTATION-FINITE-RECORD-TRANSPORT`.

## 0. Purpose

The goal is to make quantum computing a direct consequence domain of the ISP
finite-record ontology.

The working slogan is:

$$
quantum computing is record engineering
$$

A quantum computer does three things:

1. prepares a finite input record;
2. keeps multiple output-compatible alternatives unresolved;
3. drives those alternatives through controlled transports until measurement
   stabilizes one output record.

## 1. Dictionary

| Standard quantum computing | ISP reading |
| --- | --- |
| qubit | two-level finite record interface |
| register | finite record product interface |
| gate | controlled finite transport |
| circuit | composed transport ledger |
| unitary | reversible effective transport before stabilization |
| measurement | stable output-record selection |
| decoherence | unwanted record leakage |
| algorithm | record-transport design whose final stable records are biased toward answers |

## 2. Circuit Records

Let an input record be:

$$
R_in
$$

Let a finite gate ledger be:

$$
G = (g_1, g_2, ..., g_D)
$$

The circuit transport is:

$$
T_G = T_gD ... T_g2 T_g1
$$

The ISP content is not that the symbols in the circuit are primitive.  The
content is that the physical device realizes a finite family of record
interfaces whose effective transport is represented by the circuit.

## 3. The Main Gate

The first quantum-computation gate is:

$$
QC1 = finite input records + reversible unresolved transport + final output record
$$

The pass condition is:

$$
same_actual(R_path_i, R_path_j) holds until final readout
$$

The fail condition is:

$$
environment records path information before the intended readout
$$

## 4. What This Adds

Standard quantum mechanics already has the circuit model.  ISP does not
replace it.  ISP identifies what the circuit model means ontologically: the
machine is delaying actuality at selected interfaces, not evaluating many
classical worlds in parallel.

This matters because it separates two records:

$$
allowed record = control and syndrome information
$$

$$
forbidden premature record = logical branch information
$$

## 5. Draft Theorem Target

If finite record alternatives remain same-actual throughout the transport
ledger, and if the effective comparison maps reproduce the circuit gate set,
then the observed output distribution agrees with the ordinary circuit model.

In short:

$$
same_actual preservation + gate descent => quantum circuit statistics
$$

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| QC1F1 | no finite record interface can represent a qubit |
| QC1F2 | reversible transport cannot approximate the gate set |
| QC1F3 | same-actual preservation cannot be separated from output readout |
| QC1F4 | environmental records are required for the circuit to work |
| QC1F5 | output statistics differ from standard quantum circuit predictions |

## 7. Initial Verdict

Quantum computation survives ISP as finite record transport.  The value of the
translation is not a new algorithm yet.  The value is a clean ontology: a
quantum circuit is a controlled delay of stable records, followed by a
deliberate record stabilization.

## 8. Developed Finite-Record Circuit Model

A circuit is represented by a finite layered record object:

$$
Q = (R_0, U_1, R_1, U_2, ..., U_D, R_D, M)
$$

where:

| Symbol | Meaning |
| --- | --- |
| R_0 | prepared input record interface |
| U_k | effective reversible transport at layer k |
| R_k | unresolved intermediate record interface |
| M | final stabilization/readout map |
| D | coherent depth |

At no intermediate layer is R_k required to be an actual classical record.
It is a licensed record interface: the device has enough finite structure to
define possible readouts, but the readout has not yet stabilized.

The ISP condition for coherent operation is:

$$
for all k < D, branch labels in R_k are not actual environmental records
$$

The output condition is:

$$
M(R_D) is an actual finite classical record
$$

This separates the quantum circuit from a classical probabilistic circuit.  A
classical circuit stabilizes intermediate records after each step.  A quantum
circuit protects the intermediate record interfaces from becoming actual.

## 9. Qubit Interface

A qubit is not defined as a tiny classical bit.  In ISP it is a finite
two-outcome interface whose alternatives can remain same-actual under selected
transports.

The minimal qubit gate is:

| Clause | Content |
| --- | --- |
| QB1 | two stable readout records exist |
| QB2 | coherent transports can mix those readout alternatives |
| QB3 | relative transport phase can be preserved |
| QB4 | final readout stabilizes one of the two records |

The licensed qubit interface fails if the environment stores which-alternative
information during the coherent interval.

## 10. Gate Descent

An effective gate is a finite control operation whose action descends to the
ordinary unitary gate at the Hilbert-space interface.

The descent claim is:

$$
finite controlled transport -> effective unitary action on the record interface
$$

For a universal gate set, the paper needs only a finite family of transports
whose effective actions approximate:

| Gate family | ISP role |
| --- | --- |
| single-qubit rotations | local record-interface mixing |
| controlled entangling gate | nonfactorizing joint-record transport |
| measurement | stable finite output record |
| reset | preparation of a new licensed record interface |

The corpus claim is conservative: if the effective descent reproduces the
standard gate set, standard circuit predictions follow.  ISP is explaining
the ontology of the gate, not changing its matrix action.

## 11. Circuit Statistics Theorem

The developed theorem statement is:

$$
QC-STAT = PASS under gate descent and same-actual preservation
$$

Assumptions:

| Assumption | Meaning |
| --- | --- |
| A1 | each physical gate has an effective unitary descent |
| A2 | branch alternatives remain same-actual until readout |
| A3 | environmental leakage is below distinguishability threshold |
| A4 | the final measurement stabilizes the intended output interface |

Then the output record distribution is:

$$
P(o) = standard circuit probability for output o
$$

Proof sketch:

1. A1 gives the ordinary circuit transport on the effective interface.
2. A2 prevents premature replacement by a classical stochastic mixture.
3. A3 licenses interference among branch alternatives.
4. A4 turns the final interface into a stable finite output record.
5. Therefore the observed frequencies are the ordinary quantum circuit
   frequencies.

## 12. Classical Simulation Boundary

ISP does not say every finite record transport is classically hard.  Classical
simulation becomes easy when the transport ledger admits an efficient product
or low-curvature representation.

Easy cases include:

| Case | Record reason |
| --- | --- |
| stabilizer circuits | record constraints remain efficiently trackable |
| low-entanglement circuits | joint record nonfactorization stays bounded |
| noisy circuits | premature records classicalize the process |
| shallow circuits | transport ledger has limited depth and curvature |

The hard cases are those where same-actual alternatives remain coherent while
the transport ledger develops nonclassical holonomy and nonfactorization.

## 13. Mature Verdict

Paper 3 establishes the root translation for the quantum-computing arc:

$$
quantum computation = finite coherent record transport + final record stabilization
$$

This is the platform for Papers 4-13.  Phase, entanglement, measurement, error
correction, fault tolerance, topology, algorithms, BQP, physical limits, and
factoring bounds are all refinements of this one statement.