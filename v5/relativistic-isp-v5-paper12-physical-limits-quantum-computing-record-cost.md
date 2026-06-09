# Relativistic ISP V5 Paper 12: Physical Limits Of Quantum Computing From Record Cost

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper collects physical limits on
quantum computation as finite-record stabilization costs.

## Abstract

Quantum computers are physical systems.  Their limits are not only algorithmic
but thermodynamic, environmental, control-theoretic, and possibly
gravitational in extreme regimes.  ISP unifies these limits as record costs:
the machine must prevent premature logical records while allowing control,
syndrome, and final output records.

The central claim is:

$$
quantum computing is limited by the cost of preventing premature records
$$

Searchable paper tag:

`V5P12-PHYSICAL-LIMITS-QUANTUM-COMPUTING-RECORD-COST`.

## 0. Purpose

This paper gives a unified record-cost ledger for the physical limits of
large quantum computers.

## 1. Total Record Cost

Define:

$$
R_total = R_env + R_control + R_heat + R_measure + R_syndrome + R_gravity
$$

Not all terms are harmful.  The dangerous part is:

$$
R_logical = record cost correlated with unresolved logical alternatives
$$

The survival condition is:

$$
R_logical << 1
$$

during the coherent part of the computation.

## 2. Ordinary Limits

| Limit | ISP reading |
| --- | --- |
| thermal noise | heat bath records energy and phase information |
| control noise | imperfect controls leak branch-dependent records |
| crosstalk | neighboring qubits record each other's state |
| readout error | wrong output or syndrome record stabilizes |
| leakage error | state exits licensed record interface |
| reset cost | erasing records costs thermodynamic resources |

## 3. Gravitational Limit

V5 Paper 2 adds a possible intrinsic term for massive spatial superpositions:

$$
R_gravity = E_G T / hbar
$$

For ordinary superconducting or ion-trap qubits this term is expected to be
tiny.  It becomes relevant only for architectures involving large mass
displacement, mesoscopic resonators, or gravitationally distinct branch
records.

## 4. Main Gate

| Gate | Meaning |
| --- | --- |
| PL1 | every physical limit is mapped to a record channel |
| PL2 | harmful channels distinguish logical alternatives |
| PL3 | harmless channels record only control, gauge, or syndrome data |
| PL4 | the total harmful record cost bounds circuit depth |

## 5. Scaling Bound

Let D be logical depth and p_L be logical record-leakage per layer.  A minimal
success condition is:

$$
D p_L << 1
$$

More generally:

$$
integrated logical record leakage during computation << answer margin
$$

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| PLF1 | a physical limit affects computation without record leakage or cost |
| PLF2 | record leakage does not bound loss of algorithmic success |
| PLF3 | gravitational term dominates ordinary qubits contrary to scale estimates |
| PLF4 | harmless syndrome records are indistinguishable from harmful logical records |

## 7. Initial Verdict

The physical limit of quantum computing is not merely noise.  It is the cost
of keeping the right records unstabilized while all the engineering around
them becomes increasingly actual.

## 8. Developed Record-Cost Ledger

A large quantum computer has many record channels.  Some are required for
control and correction.  Some are harmful because they distinguish logical
branches.

Define the harmful part:

$$
R_harm = R_total projected onto logical branch distinguishability
$$

The computation is viable only if:

$$
R_harm < R_failure_margin
$$

for the entire algorithm, including preparation, gates, correction, and final
readout.

## 9. Thermodynamic Cost

Quantum computers must cool, reset, measure, and classically decode.  These
operations create and erase records.  ISP does not identify thermodynamic cost
with logical decoherence, but it insists they share a record ledger.

The separation is:

| Cost | Record role |
| --- | --- |
| Landauer erasure | deletes classical/support records |
| measurement heat | amplifies output or syndrome records |
| cooling | removes uncontrolled bath records |
| control electronics | writes intended classical control records |
| logical decoherence | writes forbidden branch records |

The dangerous term is not heat by itself.  It is heat correlated with logical
alternatives.

## 10. Control Precision

Control errors matter because they can create distinguishable histories of the
logical transport.

Let epsilon_k be control error at layer k.  A coarse bound is:

$$
R_control <= sum over k of c_k epsilon_k^2
$$

where c_k measures how much that control error is correlated with logical
branch data.  ISP suggests prioritizing calibration by logical-record
correlation, not only by raw physical error size.

## 11. Gravity Term

For most ordinary qubits:

$$
R_gravity approximately 0
$$

at present scales.  The term matters only if the computation uses large
spatially separated mass distributions or mesoscopic mechanical cats.

When relevant:

$$
R_gravity = E_G T / hbar
$$

where E_G is the gravitational mismatch energy from V5 Paper 2.

## 12. Architecture Comparison

| Architecture | Likely dominant record cost |
| --- | --- |
| superconducting qubits | control noise, dielectric loss, readout crosstalk |
| trapped ions | motional heating, laser phase noise, photon scattering |
| neutral atoms | loss, laser noise, imperfect blockade, imaging errors |
| photonics | loss and detector records |
| spin qubits | charge noise, nuclear bath records, control crosstalk |
| mechanical cats | ordinary decoherence plus possible gravitational mismatch |

The ISP value is a common language for comparing these platforms.

## 13. Mature Verdict

Paper 12 develops a physical resource bound: a quantum computer is limited by
the integrated branch-distinguishing record cost.  Standard engineering noise
models remain valid, but ISP says what they are all measuring at the deepest
level: premature logical record formation.

## 14. Formal Closure

### Definition 14.1: Total Branch-Distinguishing Record Cost

For a computation of duration \(T\), define:

$$
\boxed{
R_{tot}(T)
=
\int_0^T
\sum_\alpha
\Gamma_\alpha(t)\,dt.
}
$$

The channels \(\alpha\) include dephasing, relaxation, leakage, crosstalk,
measurement backaction, thermal records, control records, and any
gravitational mismatch channel.

### Lemma 14.2: Record Costs Add For Independent Channels

If branch survival factors multiply, then costs add:

$$
\boxed{
S_{tot}
=
\prod_\alpha S_\alpha
\quad
\Longrightarrow
\quad
R_{tot}
=
\sum_\alpha R_\alpha.
}
$$

Proof.  Each independent channel contributes an exponential survival factor.
The negative logarithm of the product is the sum of the negative logarithms.
Thus the integrated record costs add.

$$
\square
$$

### Lemma 14.3: Computation Requires Cost Below Margin

Let \(M_{FT}\) be the distinguishability margin supplied by error correction,
fault tolerance, and final readout.  Successful coherent computation requires:

$$
\boxed{
R_{tot}<M_{FT}.
}
$$

Proof.  If the integrated uncontrolled record cost exceeds the margin, some
uncontrolled channel can stabilize enough logical branch information to
destroy same-actual preservation before intended readout.  If the cost remains
below the margin, the branch information is either unrecorded or absorbed into
correctable syndrome records.

$$
\square
$$

### Lemma 14.4: Gravitational Term Is A Special Case Of Record Cost

For mass-distribution alternatives:

$$
\boxed{
R_G
=
{E_G T\over \hbar}.
}
$$

Proof.  Paper 2 proves the gravitational survival rate.  Multiplying the rate
by the computation time gives the integrated record cost.  For ordinary
microscopic qubits this term is negligible; for mesoscopic mass-separated
hardware it becomes part of the same budget.

$$
\square
$$

### Theorem 14.5: Paper 12 Closure

The physical limit statement is:

$$
\boxed{
R_{tot}<M_{FT}
\quad
\hbox{is necessary for scalable coherent computation.}
}
$$

Proof.  Lemma 14.2 gives the additive cost ledger.  Lemma 14.3 gives the
success condition.  Lemma 14.4 embeds the gravitational channel.  Therefore
Paper 12 is closed as a physical record-cost bound.

$$
\square
$$
