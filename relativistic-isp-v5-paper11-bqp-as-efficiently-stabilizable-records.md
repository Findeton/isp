# Relativistic ISP V5 Paper 11: BQP As Efficiently Stabilizable Records

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper proposes an ISP reading of
the complexity class BQP.

## Abstract

BQP is usually defined as the class of decision problems solvable by a
polynomial-size quantum circuit with bounded error.  ISP keeps that definition
as the external computational standard, but gives it an ontology: BQP is the
class of answer records efficiently stabilizable by finite coherent transport.

The central claim is:

$$
BQP = efficiently stabilizable answer records under quantum finite transport
$$

Searchable paper tag:

`V5P11-BQP-EFFICIENTLY-STABILIZABLE-RECORDS`.

## 0. Purpose

This paper links ISP to computational complexity without claiming
hypercomputation or faster-than-light information.

The boundary is important:

$$
ISP does not make NP-complete problems automatically easy
$$

## 1. Standard Definition Retained

Externally, BQP remains:

$$
polynomial quantum circuit + bounded error + classical output bit
$$

ISP does not alter that definition.  It interprets the physical meaning of
the circuit and output.

## 2. ISP Definition

A language L is ISP-BQP when membership records can be stabilized with high
probability by a polynomial family of finite coherent transports.

The condition is:

$$
Pr(stabilize correct answer record) >= 2/3
$$

with polynomial record resources.

## 3. Resource Ledger

| Resource | ISP reading |
| --- | --- |
| qubits | finite coherent record interfaces |
| gates | controlled transports |
| depth | time before output stabilization |
| measurements | stable output records and syndrome records |
| error bound | allowed wrong-record stabilization probability |

## 4. Why BQP Is Not Magic

BQP is not the class of problems solved by trying every answer in another
world.  It is the class where finite transport curvature, nonfactorization,
and interference can efficiently amplify the right output records.

## 5. Main Gate

| Gate | Meaning |
| --- | --- |
| BQP1 | a uniform finite transport family exists |
| BQP2 | record resources scale polynomially |
| BQP3 | correct answer records stabilize with bounded error |
| BQP4 | no superluminal or noncomputable record channel is used |

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| BQPF1 | ISP requires resources outside the standard circuit model |
| BQPF2 | bounded-error output cannot be read as stable record probability |
| BQPF3 | the ontology implies hypercomputation |
| BQPF4 | efficient stabilizability diverges from BQP with no physical reason |

## 7. Initial Verdict

BQP survives ISP as the class of efficiently stabilizable answer records.  The
main value is conceptual discipline: quantum advantage is finite coherent
transport advantage, not infinite parallel computation.

## 8. Developed Complexity Translation

The standard class BQP is a promise about uniform polynomial quantum circuits.
The ISP version is a promise about finite record families:

$$
input record size n -> polynomial coherent transport ledger -> bounded-error answer record
$$

The output is still classical.  The nonclassical part is the protected
transport before the output stabilizes.

## 9. ISP-BQP Definition

Define ISP-BQP as the class of decision problems for which there exists a
uniform family of finite record transports A_n such that:

| Condition | Meaning |
| --- | --- |
| uniformity | the transport ledger is classically describable in polynomial time |
| polynomial size | number of record interfaces and gates is polynomial in n |
| bounded error | correct output record stabilizes with probability at least 2/3 |
| no hidden oracle | no unlicensed noncomputable record channel is used |

Then ISP-BQP is intended to match ordinary BQP under the circuit-descent gate.

## 10. Relationship To Other Classes

The conservative ISP stance is:

| Relationship | Status |
| --- | --- |
| P subset BQP | retained |
| BPP subset BQP | retained |
| factoring in BQP | retained |
| NP-complete in BQP | not claimed |
| hypercomputation | forbidden |

ISP does not make computation stronger by adding metaphysics.  It explains
which physical record resources the standard class already assumes.

## 11. Efficient Stabilization

The phrase efficiently stabilizable means that the answer record can be made
actual without expanding an exponential classical record ledger.

The condition is:

$$
physical coherent transport cost is polynomial while equivalent classical record expansion may be exponential
$$

This is the ISP way to describe quantum advantage.

## 12. Oracle And Relativistic Boundaries

ISP disallows two shortcuts:

| Shortcut | Why forbidden |
| --- | --- |
| superluminal answer records | violates finite relativistic record locality |
| noncomputable hidden record access | not a licensed finite transport ledger |

Thus ISP-BQP is not a route to arbitrary mathematical omniscience.  It is a
physical class of efficiently realizable record transports.

## 13. Mature Verdict

Paper 11 develops the complexity claim: BQP is the class of answer records
that finite coherent transport can stabilize efficiently with bounded error.
This preserves the standard theory while making its physical ontology
explicit.