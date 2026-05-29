# Relativistic ISP V5 Paper 13: Finite Record Resource Bounds For Shor Factoring

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper studies physical
finite-record limits on quantum algorithms for factoring integers into
primes.  It does not claim that Shor's abstract algorithm is false.

## Abstract

Shor's algorithm places integer factoring in BQP in the standard circuit
model.  ISP should not deny that theorem.  The ISP question is physical: what
finite-record resources are needed to keep the period-finding computation
coherent until the hidden period becomes a stable output record?  This paper
defines a period-record leakage budget and explains how ordinary noise,
imperfect error correction, control leakage, and possible gravitational
record stabilization contribute to it.

The central claim is:

$$
Shor succeeds physically only while period-relevant records remain unstabilized
$$

Searchable paper tag:

`V5P13-FINITE-RECORD-RESOURCE-BOUNDS-SHOR-FACTORING`.

## 0. Purpose

The phrase factorising primes is usually shorthand, but technically primes do
not need factoring.  The real target is factoring composite integers into
prime factors, especially semiprimes.

This paper asks:

$$
what does ISP add to physical limits on Shor-like factoring?
$$

## 1. Boundary

Forbidden claim:

$$
Shor's algorithm is mathematically invalid
$$

Allowed claim:

$$
real factoring machines must satisfy a finite-record leakage inequality
$$

The paper is about physical realizability, not abstract complexity collapse.

## 2. Shor As Period-Record Extraction

The quantum part of Shor does not directly output the factors.  It extracts a
period record from modular exponentiation.

ISP translation:

1. prepare unresolved exponent records;
2. apply controlled modular transport;
3. encode periodicity as phase or holonomy;
4. Fourier-read the period-compatible record;
5. use classical arithmetic to recover factors.

## 3. Period Leakage Functional

Define:

$$
R_period(n,T) = distinguishability leaked about the hidden period during the coherent computation
$$

For an n-bit integer, a physical Shor run requires:

$$
R_period(n,T_circuit) << 1
$$

until the intended phase-estimation readout.

If the environment learns period-correlated information early, the
interference needed for period extraction is damaged.

## 4. Ordinary Quantum Information Already Gives

Standard quantum theory already supplies:

1. circuit resource estimates;
2. surface-code overhead estimates;
3. logical error budgets;
4. noise models;
5. threshold theorems.

ISP adds value only if it sharpens the invariant being budgeted:

$$
harmful leakage = leakage correlated with the period record
$$

## 5. Resource Inequality

Let D(n) be the logical circuit depth and p_period(n) be the corrected
period-record leakage per logical layer.

A first bound is:

$$
D(n) p_period(n) << 1
$$

With multiple channels:

$$
R_period = R_dephase + R_relax + R_control + R_crosstalk + R_measure + R_gravity
$$

The success condition is:

$$
R_period < R_margin
$$

where R_margin is the period-resolution margin of the algorithm.

## 6. Syndrome Versus Period Records

The essential ISP distinction is:

$$
syndrome records may stabilize; period records must not stabilize early
$$

This is the core reason error correction can coexist with coherent factoring.

## 7. Main Gate

| Gate | Meaning |
| --- | --- |
| SF1 | Shor's quantum part is period-record extraction |
| SF2 | harmful leakage is period-correlated distinguishability |
| SF3 | error correction records syndrome without recording the period |
| SF4 | factoring success requires integrated period leakage below margin |

## 8. Falsifier Gates

| Gate | Failure |
| --- | --- |
| SFF1 | period extraction succeeds despite large period-correlated leakage |
| SFF2 | all leakage is equally harmful, independent of period correlation |
| SFF3 | syndrome extraction necessarily records the hidden period |
| SFF4 | ISP predicts a factoring bound contradicted by a verified scalable machine |

## 9. Initial Verdict

This paper gets real value from ISP only if it defines and uses the
period-record leakage functional.  Without that, ordinary quantum information
already says the same thing in density-matrix language.  With that functional,
ISP gives a clean physical criterion: factoring is possible when error
correction and controls prevent premature stabilization of the hidden period
record.

## 10. Developed Shor Ledger

For an n-bit semiprime N, Shor's algorithm reduces factoring to order finding.
Choose a random a coprime to N and find the least r such that:

$$
a^r = 1 mod N
$$

The quantum part estimates r.  The factors are recovered classically when r
has suitable parity and nontrivial greatest-common-divisor conditions.

ISP translation:

| Stage | Record role |
| --- | --- |
| choose a | classical setup record |
| exponent register | unresolved exponent records |
| modular exponentiation | controlled finite arithmetic transport |
| phase/Fourier readout | period-compatible record stabilization |
| gcd post-processing | classical factor records |

## 11. Resource Scaling

The abstract quantum algorithm is polynomial.  Physical implementations still
need logical resources.

A conservative ledger is:

| Resource | Scaling role |
| --- | --- |
| logical qubits | store exponent and modular arithmetic records |
| logical depth | coherent time for modular exponentiation and readout |
| T gates or non-Clifford resources | arithmetic transport cost |
| syndrome cycles | same-actual preservation overhead |
| classical decoder | converts syndrome records to recovery operations |

The ISP condition is not that these resources are small.  It is that they
scale while period leakage remains below margin.

## 12. Period-Record Margin

Let M_period be the algorithmic resolution margin needed to infer r from the
measured phase record.  Let R_period be the integrated period-correlated
leakage.

The physical success condition is:

$$
R_period << M_period
$$

Ordinary local errors are harmful only insofar as they contribute to
R_period after decoding.  This is sharper than a generic decoherence budget.

## 13. Error Correction Clause

Error correction is compatible with Shor because syndrome records need not
record the hidden period.

The required clause is:

$$
I(syndrome history ; period record) approximately 0
$$

where I is ordinary mutual information in the external information-theoretic
description.  ISP reads this as same-actual preservation of the period record
while error records become actual.

## 14. What Would Be New

Standard quantum information already gives resource estimates.  ISP adds a
specific diagnostic:

$$
measure not just logical error, but period-correlated logical record leakage
$$

Two machines with similar logical error rates might differ if one leaks
information correlated with modular-exponentiation branches more strongly than
the other.

## 15. Physical Channels

| Channel | Period-leakage route |
| --- | --- |
| dephasing | phase record smeared before Fourier readout |
| relaxation | arithmetic branch leaves licensed record sector |
| crosstalk | control hardware records branch-dependent activity |
| measurement backaction | syndrome readout leaks logical arithmetic data |
| thermal bath | bath stores period-correlated histories |
| gravitational mismatch | only relevant for massive branch-distinct hardware |

## 16. No-Go Boundary

The paper cannot honestly prove:

$$
large-scale factoring is impossible
$$

unless it proves a lower bound showing R_period must exceed M_period for all
physical architectures.  That is far stronger than the present ISP claim.

The honest result is:

$$
any physical factoring machine must keep period-correlated record leakage below the period margin
$$

## 17. Mature Verdict

Paper 13 becomes valuable when it supplies the period-record leakage
functional.  It does not refute Shor.  It identifies the physical invariant a
real Shor machine must protect: the hidden period must remain an unresolved
same-actual record until the intended phase-estimation readout stabilizes it.