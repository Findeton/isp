# Relativistic ISP V5 Paper 4: Phase As Stochastic Holonomy, The Computational Resource

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper interprets quantum phase in
algorithms as stochastic transport holonomy.  It gives an ISP reason why phase
estimation, Fourier sampling, and interference are computational resources.

## Abstract

Quantum algorithms use phase.  ISP says phase is not primitive complex
decoration.  Phase is the effective shadow of stochastic transport curvature,
or holonomy, across incompatible finite record transports.  This paper
translates the computational advantage of phase into the ability to engineer,
compare, and read transport defects.

The central claim is:

$$
quantum speedup comes from engineered finite transport curvature
$$

Searchable paper tag:

`V5P4-PHASE-STOCHASTIC-HOLONOMY-COMPUTATIONAL-RESOURCE`.

## 0. Purpose

This paper asks what a quantum phase is doing inside a computation if ISP is
right.

The answer is:

$$
phase = observable bookkeeping of path-order mismatch
$$

Algorithms such as phase estimation, Shor, amplitude estimation, and quantum
walk algorithms exploit that mismatch in a controlled way.

## 1. ISP Translation

| Standard term | ISP term |
| --- | --- |
| phase | transport holonomy |
| relative phase | branch-comparison defect |
| interference | recombination of incompatible transports |
| Fourier transform | change of record basis that exposes periodic holonomy |
| phase estimation | stable readout of a transport eigen-defect |

## 2. Holonomy Ledger

Consider two controlled transports:

$$
A then B
$$

and:

$$
B then A
$$

The ISP computational resource is the finite mismatch:

$$
H(A,B) = compare(A after B, B after A)
$$

If:

$$
H(A,B) = 0
$$

the transport behaves classically at that interface.  If:

$$
H(A,B) not equal 0
$$

then recombination can amplify some output records and suppress others.

## 3. Phase Estimation As Holonomy Readout

The phase-estimation routine becomes:

1. prepare a control record;
2. couple it to repeated controlled transports;
3. accumulate a stable comparison defect;
4. expose the defect using a Fourier readout;
5. stabilize a finite phase record.

The output is not a mystical number attached to a vector.  It is a finite
record of a transport defect.

## 4. The Main Gate

The holonomy computation gate is:

$$
HC1 = controlled noncommuting transports + recombination + stable defect readout
$$

Pass condition:

$$
defect records predict output interference peaks
$$

Fail condition:

$$
interference peaks appear with no corresponding transport defect
$$

## 5. Why This Is Not Just Rewording

Standard quantum mechanics says phase matters.  ISP says why phase is a
record-geometric resource: it is a measurable residue of finite transport
noncommutativity.

The proposed invariant is:

$$
algorithmic phase resource = controlled holonomy available before readout
$$

This gives a way to compare algorithms by the amount and structure of
transport curvature they require.

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| HC1F1 | phase cannot be represented as a finite transport defect |
| HC1F2 | algorithmic phase survives even when all comparison defects vanish |
| HC1F3 | holonomy magnitude does not track interference visibility |
| HC1F4 | Fourier sampling gives no stable record of transport periodicity |

## 7. Initial Verdict

Quantum phase is the computational form of stochastic holonomy.  ISP adds
value by making phase a finite geometric resource rather than a primitive
complex label.

## 8. Developed Holonomy Resource

The operational resource is not phase as a real number by itself.  It is phase
as a record-comparison invariant.  A computation uses phase when two or more
licensed transports reach a common record interface and their comparison
changes output stabilization weights.

Define the computational holonomy resource:

$$
H_alg = record-visible transport mismatch available before readout
$$

The resource is zero when all relevant transports commute at the record
interface.  It is useful when it can be coupled to an answer predicate.

## 9. Fourier Sampling In ISP

Fourier sampling is the standard way to expose hidden periodic holonomy.

The ISP sequence is:

1. prepare a uniform unresolved record family;
2. apply a controlled transport with hidden periodicity;
3. accumulate branch-dependent holonomy;
4. apply the Fourier readout interface;
5. stabilize a record concentrated on period-compatible outputs.

The Fourier transform is therefore a record-basis change that makes transport
periodicity recordable.

## 10. Phase Estimation Theorem Target

Let U be an effective transport and let an unresolved branch be compatible
with a transport eigen-defect theta.

The theorem statement is:

$$
controlled powers of U + Fourier readout => finite phase record for theta
$$

The ISP content is:

| Step | Record reading |
| --- | --- |
| controlled powers | amplify a transport defect into control records |
| inverse Fourier readout | convert periodic defect into binary record |
| measurement | stabilize an approximate phase record |
| repetition | refine the finite phase record |

The output record is not the phase itself.  It is a finite approximation to a
holonomy class.

## 11. Resource Inequality

Let delta_theta be the required phase resolution and let L_phase be the
phase-destroying record leakage during the algorithm.

The computation requires:

$$
L_phase << delta_theta
$$

in the units of the chosen readout margin.  If environmental records erase the
relative holonomy before the Fourier readout, phase estimation fails.

## 12. Relation To Shor

In Shor's algorithm, the hidden order r appears as periodic structure in
modular exponentiation.  The phase register does not need to record all
classical residues.  It needs to record enough holonomy to infer r.

ISP reading:

$$
period finding = holonomy-to-record conversion
$$

This becomes the basis for Paper 13, where premature leakage about the period
is treated as the damaging record channel.

## 13. Classical Boundary

If holonomy can be represented by a compact classical invariant, no quantum
advantage follows.  The computational power appears only when the finite
transport defect is compactly accessible to the device but not to a classical
record-by-record simulation.

The boundary is:

$$
efficient physical holonomy access versus inefficient classical record expansion
$$

## 14. Mature Verdict

Paper 4 identifies the first nonclassical resource of ISP quantum computing:
algorithmic phase is record-visible holonomy.  It is useful when a circuit can
protect the holonomy until readout and then convert it into a stable answer
record.