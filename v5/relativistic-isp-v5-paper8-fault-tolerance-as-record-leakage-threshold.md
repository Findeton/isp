# Relativistic ISP V5 Paper 8: Fault Tolerance As A Record-Leakage Threshold

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper reads the fault-tolerance
threshold theorem as a finite-record leakage threshold.

## Abstract

Fault-tolerant quantum computing says that arbitrarily long computations are
possible if physical noise is below a threshold and correction overhead is
scaled appropriately.  ISP rephrases this as a record statement: logical
computation survives if branch-distinguishing records leak slowly enough that
correction can absorb them into syndrome ledgers before they stabilize logical
alternatives.

The central claim is:

$$
fault tolerance = record leakage below logical distinguishability threshold
$$

Searchable paper tag:

`V5P8-FAULT-TOLERANCE-RECORD-LEAKAGE-THRESHOLD`.

## 0. Purpose

This paper gives an ISP reading of the threshold theorem without pretending to
replace standard proofs.  The value is conceptual and diagnostic: all noise
channels are classified by what kind of record they leak.

## 1. Record Leakage Functional

Define a logical record-leakage budget:

$$
L_logical(T) = distinguishability leaked about logical alternatives during T
$$

Fault tolerance requires:

$$
L_logical(T_circuit) << 1
$$

after correction is included.

## 2. Noise Channels

| Noise | ISP reading |
| --- | --- |
| dephasing | environment records relative branch phase |
| relaxation | environment records energy transition |
| leakage | state leaves the licensed record interface |
| crosstalk | neighboring controls record each other accidentally |
| measurement error | wrong syndrome record is stabilized |
| loss | record carrier disappears from the code ledger |

## 3. Threshold Statement

Let p be the physical error probability per location and d the code distance.
The standard threshold structure says that below threshold, increasing d
suppresses logical errors.

ISP reads this as:

$$
physical record leaks are converted into local syndrome records faster than
they become logical records
$$

## 4. Main Gate

| Gate | Meaning |
| --- | --- |
| FT1 | physical noise can be represented as finite record leakage |
| FT2 | correction maps local leakage into syndrome ledgers |
| FT3 | logical branch distinguishability decays with code distance below threshold |
| FT4 | above threshold, leakage percolates into logical records |

## 5. Practical Diagnostic

An ISP fault-tolerance analysis should ask:

1. what record did the environment acquire;
2. is that record local, syndrome-compatible, or logical;
3. can the code absorb it before it stabilizes a logical branch;
4. does the leakage scale down with code distance.

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| FTF1 | noise affects computation without any record-distinguishability channel |
| FTF2 | below-threshold correction still produces growing logical records |
| FTF3 | code distance does not reduce logical distinguishability |
| FTF4 | observed threshold cannot be mapped to any record-leakage boundary |

## 7. Initial Verdict

Fault tolerance survives ISP as the engineering discipline of keeping logical
records unstabilized while continuously stabilizing error records.

## 8. Developed Threshold Picture

Fault tolerance is a competition between two rates:

$$
rate of local record leakage
$$

and:

$$
rate of correction into harmless syndrome records
$$

Below threshold, leakage is localized and correctable.  Above threshold,
leakage forms connected histories that stabilize logical alternatives.

## 9. Logical Distinguishability Functional

Define:

$$
D_L(t) = distinguishability of logical alternatives available to uncontrolled records
$$

Fault tolerance requires:

$$
D_L(T_circuit) << 1
$$

after decoding and recovery.

This is stronger than saying the physical error rate is small.  It asks
whether the physical records combine into logical branch information.

## 10. Threshold Theorem Reading

The standard threshold theorem has the form:

$$
p < p_threshold => logical error can be suppressed by scaling overhead
$$

ISP reading:

$$
local record leakage below threshold does not percolate into stable logical records
$$

The code distance controls how much finite record leakage is needed before the
logical alternative becomes distinguishable.

## 11. Leakage Taxonomy

| Leakage type | Harmless if | Harmful if |
| --- | --- | --- |
| local Pauli-like fault | syndrome records it | chains to logical operator |
| photon/phonon emission | not logical-correlated | carries branch label |
| crosstalk | decoder models it | creates correlated logical leak |
| measurement fault | repeated checks correct it | flips syndrome history globally |
| leakage outside code space | detected and reset | persists as hidden logical tag |

## 12. Correlation Boundary

Fault tolerance assumes noise correlations are sufficiently local or
structured.  ISP states why: long-range correlated noise is dangerous because
it can create a logical record without first appearing as isolated local
syndrome records.

The failure condition is:

$$
uncontrolled environment stores a global logical label
$$

## 13. Mature Verdict

Paper 8 develops the threshold theorem as a record-percolation boundary.
Quantum computation survives when local record leaks are repeatedly absorbed
into syndrome histories before they form a stable logical output or wrong
logical branch.

## 14. Formal Closure

### Definition 14.1: Logical Leakage Functional

For a fault-tolerant computation, define:

$$
\boxed{
D_L(t)
=
\sup_{R_E}
D_{\mathrm{TV}}
(
P(R_E|L=0),
P(R_E|L=1)
).
}
$$

The supremum ranges over uncontrolled environmental records available before
intended logical readout.

### Lemma 14.2: Local Leakage Below Threshold Does Not Percolate

Assume a code family with distance increasing with scale and a local noise
model below threshold:

$$
\boxed{
p<p_{th}.
}
$$

Then the probability that uncontrolled records form a logical distinguishing
path decays with code distance:

$$
\boxed{
P_{\mathrm{logical\ leak}}
\le
C e^{-\alpha d}.
}
$$

Proof.  Below threshold, connected fault clusters have exponentially decaying
size distribution.  A logical leak requires a connected or decoder-equivalent
chain spanning a logical operator class.  The minimum such chain has weight
at least \(d\).  Standard threshold combinatorics then gives the exponential
bound.

$$
\square
$$

### Lemma 14.3: Syndrome Records Convert Local Faults Into Correctable Data

When syndrome extraction is reliable below threshold:

$$
\boxed{
I(S;E)>0,
\qquad
I(S;L)\approx0.
}
$$

Proof.  Repeated local checks are designed to reveal local fault classes.  The
threshold condition ensures that the decoder can map the syndrome history to
a recovery class without learning the logical branch.  Thus local leakage is
absorbed into correctable syndrome records rather than becoming logical
distinguishability.

$$
\square
$$

### Theorem 14.4: Record-Leakage Threshold

Fault tolerance is the phase in which logical leakage remains below final
readout distinguishability:

$$
\boxed{
p<p_{th}
\Longrightarrow
D_L(T_{\mathrm{circuit}})
\le
C e^{-\alpha d}.
}
$$

Proof.  Lemma 14.2 bounds the probability of a logical distinguishing path.
Lemma 14.3 explains why subthreshold local records are useful syndrome data
rather than harmful logical records.  Increasing code distance suppresses
logical leakage while preserving intended final readout.  This is exactly the
threshold theorem in record language.

$$
\square
$$

### Corollary 14.5: Paper 8 Closure

Paper 8 is closed:

$$
\boxed{
\hbox{fault tolerance}
=
\hbox{subthreshold local record leakage with no stable logical record}.
}
$$
