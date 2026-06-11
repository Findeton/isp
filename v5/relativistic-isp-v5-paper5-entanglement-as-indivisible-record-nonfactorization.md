# Relativistic ISP V5 Paper 5: Entanglement As Indivisible Record Nonfactorization

Preprint, not peer reviewed, version 2026-05-29.

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper defines entanglement in ISP as
failure of a finite record process to factor into independent local ledgers.

## Abstract

Entanglement is usually represented as nonfactorization of a Hilbert-space
state.  ISP keeps the operational content but changes the ontology:
entanglement is indivisibility of the underlying finite stochastic process.
The records are local at readout, but the process that constrains their joint
statistics is not a product of independent local record ledgers.

The central claim is:

$$
entanglement = finite same-process nonfactorization
$$

Searchable paper tag:

`V5P5-ENTANGLEMENT-INDIVISIBLE-RECORD-NONFACTORIZATION`.

## 0. Purpose

Quantum computing uses entanglement as a resource, but entanglement is often
described in language that sounds like faster-than-light influence.  ISP gives
a cleaner reading: entangled systems are not locally independent systems plus
signals.  They are one indivisible process with multiple finite readout
interfaces.

## 1. Record Factorization

Let a two-register record interface be:

$$
R_AB
$$

It factors classically when:

$$
R_AB = R_A product R_B
$$

It is entangled in ISP when no finite same-actual presentation permits that
product decomposition while preserving all joint readout statistics.

## 2. Bell Pair Translation

A Bell pair is not two hidden classical bits.  It is a finite process whose
admissible joint records are constrained before either side is read.

The ISP statement is:

$$
local outputs are records; correlations belong to the indivisible process
$$

No superluminal information is required, because no local record is chosen by
a signal from the other side.

## 3. Computational Resource

Entanglement is useful because it lets a circuit operate on a joint record
constraint rather than on independently stored local alternatives.

The resource measure proposed here is:

$$
NFI(R_AB) = minimum failure of product record description
$$

where NFI means nonfactorization index.

## 4. Gate Ledger

| Gate | Meaning |
| --- | --- |
| EN1 | finite joint readout interfaces exist |
| EN2 | local marginals are compatible with relativistic no-signaling |
| EN3 | joint statistics cannot be represented by independent local ledgers |
| EN4 | the nonfactorization can be transported through gates without premature readout |

## 5. Cluster And GHZ Records

Cluster states become extended nonfactorizing record graphs.  GHZ states
become high-order same-process constraints whose local parts are individually
ambiguous but whose global parity record is structured.

The ISP distinction is:

$$
local ambiguity is not ignorance; it is unresolved finite actual structure
$$

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| ENF1 | all entangled statistics admit local product record ledgers |
| ENF2 | same-process nonfactorization allows faster-than-light messages |
| ENF3 | entanglement measures fail to track nonfactorization of record constraints |
| ENF4 | computation speedup appears with no nonfactorizing record resource |

## 7. Initial Verdict

Entanglement survives ISP as indivisible finite process structure.  The
quantum-computing value is that entanglement lets algorithms manipulate joint
record constraints before any one local stable record is forced.

## 8. Developed Nonfactorization Definition

Define a finite joint record interface:

$$
R_AB = (R_A, R_B, C_AB)
$$

where C_AB is the joint constraint ledger.  The record factors when C_AB can
be reconstructed from independent local ledgers and shared classical records.

It is ISP-entangled when:

$$
C_AB cannot be replaced by local finite ledgers without changing joint statistics
$$

This definition is operational.  It does not require superluminal influence.
It requires only that the observed joint statistics cannot be generated from
independent local actual records.

## 9. No-Signaling Clause

Any acceptable ISP entanglement definition must satisfy:

$$
local choice at A does not transmit a controllable record to B
$$

Entanglement constrains joint records; it does not allow local record control
at spacelike separation.

The ledger is:

| Layer | Status |
| --- | --- |
| local marginal records | locally stable and no-signaling |
| joint correlation record | only stable after comparison |
| process constraint | indivisible before readout |

## 10. Bell Gate

The Bell gate for ISP is:

| Gate | Meaning |
| --- | --- |
| BELL1 | local readout records exist at each wing |
| BELL2 | joint statistics violate product-ledger explanation |
| BELL3 | local marginals remain no-signaling |
| BELL4 | comparison record stabilizes only after both outcomes exist |

This separates entanglement from communication.  The process is nonfactorized;
the readout channels remain local.

## 11. Entanglement In Circuits

Entangling gates create nonfactorizing record constraints.  They are useful
when later transports can exploit those constraints before they are reduced to
classical records.

Three computational roles are:

| Role | Record meaning |
| --- | --- |
| parallel constraint | answer depends on a joint record relation |
| phase kickback | joint transport defect moves into a control record |
| error correction | logical record is distributed across many physical records |

## 12. Nonfactorization Index

A mature paper should define a finite nonfactorization index:

$$
NFI(R_AB) = minimum record deficit of all product-ledger simulations
$$

If NFI is zero, the record interface is product-like.  If NFI is positive,
there is irreducible same-process structure.  The index should be compared to
standard entanglement monotones in external calibration.

## 13. Computational Boundary

Entanglement alone does not guarantee speedup.  Highly entangled states can be
classically simulable when their record constraints have efficient tensor or
stabilizer descriptions.

The ISP condition for algorithmic usefulness is:

$$
nonfactorization + protected holonomy + answer-coupled readout
$$

## 14. Mature Verdict

Paper 5 makes entanglement precise in record terms: it is indivisible finite
process structure with local no-signaling readouts.  This gives quantum
computing a non-mystical but nonclassical resource: joint records that cannot
be decomposed into independent local actual ledgers.

## 15. Formal Closure

### Definition 15.1: Product-Ledger Simulation

A bipartite record interface admits a product-ledger simulation when there
exist local ledgers and shared classical data such that every joint readout
probability factors through them:

$$
\boxed{
P(a,b|x,y)
=
\sum_\lambda
p(\lambda)P_A(a|x,\lambda)P_B(b|y,\lambda).
}
$$

### Definition 15.2: Nonfactorization Index

The nonfactorization index is the minimum finite record deficit of all
product-ledger simulations:

$$
\boxed{
\mathrm{NFI}(A:B)
=
\inf_{\mathrm{product\ ledgers}}
D_{\mathrm{rec}}
(
P_{AB},
P_A\otimes_{\lambda}P_B
).
}
$$

### Lemma 15.3: No-Signaling Is Compatible With Positive Nonfactorization

Positive nonfactorization does not imply signaling:

$$
\boxed{
\mathrm{NFI}(A:B)>0
\quad\not\Rightarrow\quad
P(a|x,y)\hbox{ depends on }y.
}
$$

Proof.  Nonfactorization concerns the impossibility of a product explanation
of joint records.  Signaling concerns the dependence of a local marginal on a
remote setting.  Quantum correlations can violate product-ledger
factorization while preserving fixed local marginals.  In ISP language, the
joint process is indivisible before comparison, but local readout channels
remain local.

$$
\square
$$

### Lemma 15.4: Entangling Gates Create Nonfactorizing Constraints

An entangling gate is exactly a gate whose output record relation has positive
nonfactorization index for some input product packet:

$$
\boxed{
U\hbox{ entangling}
\Longleftrightarrow
\exists R_{in}:
\mathrm{NFI}(U R_{in} U^\dagger)>0.
}
$$

Proof.  If a gate maps every product packet to a product-ledger packet, it is
not entangling.  If it creates a state whose joint readout statistics cannot
be simulated by any product ledger, the nonfactorization index is positive.
This is precisely the operational content of entanglement.

$$
\square
$$

### Theorem 15.5: Paper 5 Closure

Entanglement is indivisible record nonfactorization:

$$
\boxed{
\hbox{entangled interface}
\Longleftrightarrow
\mathrm{NFI}>0
\hbox{ with no-signaling local marginals}.
}
$$

Proof.  Definition 15.1 states what it means for a joint record to factor.
Definition 15.2 measures failure of such a factorization.  Lemma 15.3 separates
nonfactorization from signaling.  Lemma 15.4 shows how circuit entanglers
create the resource.  Therefore the paper's entanglement translation is
closed.

$$
\square
$$
