# D10 hostile mathematics review — round 2 closure

**Date:** 2026-07-11  
**Reviewer role:** independent hostile mathematics closure audit  
**Verdict:** **MINOR REVISION**

All substantive round-1 mathematical openings are repaired at the narrowed
scope. One explicit group-theory sentence is still false: Paper 11 says the
quotient `PSL(2,C)` double-covers the proper orthochronous Lorentz group.
`SL(2,C)` is the double cover; after quotienting by `{+I,-I}`, `PSL(2,C)` is
isomorphic to that Lorentz group. This is a one-line repair and does not affect
the boost calculation or the `KINEMATICS-ONLY` verdict.

## 1. Frozen repair package and reproduction

Every repaired artifact hash in
`v10/data/d10-round1-repair-receipt.md` matches the reviewed files. The
reproducibility audit completed successfully and independently reran every D10
script under ordinary and optimized Python. It reproduced:

```text
checks                                      109 / 99 / 43
normal_optimized                            BYTE_IDENTICAL
frozen_stdout_hashes                        PASS
d10_bloch_lorentz_exact.py                  a05b84aa0a94a4a3086c190045fc56e96eb0fde6a00c179073a23944bbebcd5f
d10_finite_clock_convergence.py             f2e8c45e1a224e4f84ebfdd5a11e9973266879723443508d9f04539fdaa3be27
d10_relational_scir_packet.py               b5827de1d703ab492563fb1b981a41da477a1627943215ffe4ce660d0feb65eb
reproducibility audit                       f8c409191f05ee830a6422428517860e1961311b98c6f3b6be1dc5c505e6b596
```

The scripts now contain fixed `EXPECTED_CHECKS` gates, and the reproduction
script contains fixed complete-stdout hashes. Check deletion or optimized-mode
drift therefore fails rather than silently producing a new self-referential
receipt.

## 2. Independent decisive recomputations

### 2.1 Rank-two comparison witnesses

Using the repaired coordinates independently gives:

```text
field   q    ab-|z|^2    t^2-s^2-|z|^2    positive witness
R       1       23              23             yes
C       2       30              30             yes
H       4       33              33             yes
O       8      -61             -61              no
```

For a rank-two element `[[a,z],[z*,b]]`, the off-diagonal coordinate contributes
only its Euclidean norm. Thus `q=1,2,4,8` gives event dimensions `3,4,6,10` and
Lorentz signatures `1+2,1+3,1+5,1+9`. The octonionic claim remains correctly
limited to the rank-two ordered spin-factor shadow; no associative octonionic
matrix calculus is inferred.

The executable's positivity equality is algebraically redundant once
`det=ab-|z|^2` is established, but it is now honestly presented as a finite
coordinate witness rather than a machine proof of all universal quantifiers.
The written spin-factor classification supplies the universal statement.

### 2.2 Finite covering geometry

The previously independent hull-facet reconstruction continues to agree with
all published finite support minima, including:

```text
tetrahedron       0.33333333333333337
octahedron        0.5773502691896258
icosahedron       0.7946544722917661
dual union        0.8421281485007003
nested K=14       0.8068982213550735
nested K=26       0.8634489800144580
```

For every production set, the repaired gates verify three-dimensional span and
a strictly positive equal-weight zero barycenter. Full span plus that positive
convex representation places the origin in the hull interior. The centered
inradius is consequently attained at a supporting facet, and an affinely
independent triple from that facet supplies a normal included by the algorithm.
Extra triple normals are genuine sphere points and cannot lower the result
below the global minimum. The completeness gap is closed for the tested sets.

### 2.3 Finite versus infinite convergence

Paper 11 now separates the finite support calculations from the infinite
statement. Lemma 3.1 is correct: a nested family with dense union in compact
`S^2` eventually contains a finite epsilon-net for every epsilon, so its
covering radius tends to zero and its support tends to one. Applying it to the
positive H/T-word family is explicitly conditional on imported Clifford+T
density. The inverse identities `H^-1=H` and `T^-1=T^7` ensure positive words
generate the same group orbit. The finite receipts are no longer claimed to
prove that imported density theorem or an infinite limit.

The depth-12 Fibonacci value remains labeled a sampled diagnostic. The repaired
investigation ledger also records the hostile hull value
`m approximately 0.912486956834076`
separately from the sample `0.914143429015`; it no longer converts the latter
into a certified global error.

### 2.4 Instruments and schedules

The old dictionary-order tautology is gone. The repaired packet now:

1. constructs complete pointer Kraus operators `P0,P1`;
2. obtains exact Born weights `1/2,1/2` on `H|0>`;
3. verifies normalization and repeated-outcome durability;
4. composes `H tensor I` and `I tensor T` in both schedules on an explicit
   two-qubit state and obtains identical normalized outputs;
5. independently verifies the two disjoint operators commute;
6. uses overlapping `H` and `T` operations as a noncommuting order-sensitive
   control.

This is an actual test with a capable control. Its conclusion is correctly
restricted to the chosen imported complex tensor packet, not promoted to a
general SCIR construction-order theorem.

The bounded-forest intervention likewise computes a finite continuation law,
not global reachability disguised as an update. Changing the local Bernoulli
source from `1/3` to `2/3` changes exactly nodes `{1,3,4}` and leaves the other
branch and disconnected component unchanged. Joining sectors and a spacetime
influence cone remain explicitly untested.

## 3. Round-1 mathematics closure table

| round-1 opening | round-2 disposition |
|---|---|
| R/C/H/O determinant gate absent | **CLOSED at representative-witness scope.** Exact coordinate determinant and positive/negative cone witnesses now run for all four rank-two shadows; universal scope remains in the written classification. |
| finite examples graded as infinite convergence | **CLOSED.** Finite outer approximation is PASS; generated convergence is conditional on a dense nested union and imported Clifford+T density. |
| triple-normal minimum lacked completeness hypotheses | **CLOSED.** Span and origin-interiority are gated, and the supporting-facet completeness proof is stated. |
| H/T sampled coverage treated as certified | **CLOSED.** Sample and hostile hull minimum are separately labeled; no sampled value is called the true minimum. |
| external sphere sampler reported absent | **CLOSED.** Generation reports no sphere oracle while the 50,000/120,000-point Fibonacci diagnostics are explicitly present. |
| construction-order check was dictionary equality | **CLOSED at chosen-packet scope.** Both disjoint schedules are executed and an overlapping noncommuting control is present. |
| broad locality/influence inference | **CLOSED by narrowing.** Only the bounded copied-mark forest intervention is passed; joining and spacetime influence remain open. |
| `SEAL` was only a string | **CLOSED at chosen-packet scope.** A complete repeatable projective instrument and its outcome law are executed. |
| no fixed counts or stdout hashes | **CLOSED.** `109/99/43`, optimized equality, and complete stdout digests are enforced. |
| four independent vertex gauges overstated | **CLOSED.** Four distinct vertex-local matrices are now used and the prose says vertex-local rather than independent. |
| final receipt referenced before existence | **CLOSED.** Paper 11 references the pre-review receipt and says a final receipt follows review closure. |
| proper-Lorentz wording | **NOT FULLY CLOSED.** “Proper orthochronous” is now correct, but the paper assigns the double cover to `PSL(2,C)` rather than `SL(2,C)`. |

## 4. Remaining opening

### Opening R2-M1 — quotienting removes the double cover

**Severity: MINOR**

Paper 11, section 7, states:

> The quotient `PSL(2,C)` double-covers the proper orthochronous Lorentz group.

The correct alternatives are:

```text
SL(2,C) --2:1--> SO^+(1,3), with kernel {+I,-I};
PSL(2,C) = SL(2,C)/{+I,-I} isomorphic to SO^+(1,3).
```

The tested diagonal boost, determinant invariance, trace change, and distinction
between SU(2) rotation gauge and nonunitary boosts are unaffected. The opening
requires only replacement of that sentence and the corresponding disposition
claim; no executable change is necessary.

## 5. New-opening search

I found no further mathematical opening in the repaired scope:

- the complex rank-two proof remains valid;
- the comparison-algebra dimensions and determinant forms are correct;
- the finite hull minima reproduce independently;
- the hull completeness hypotheses are sufficient;
- the compactness lemma is valid and properly conditional;
- H/T inverse accessibility is correct;
- sampler use is accurately partitioned between generation and diagnostics;
- the seal and schedule tests perform the operations they claim;
- frozen counts and hashes are effective;
- receipt references are internally consistent;
- all physical selection, capacity, link-birth, boost-gauge, joining, and
  order/influence conclusions remain explicitly open.

## 6. Verdict

**MINOR REVISION.** The repaired D10 package closes every substantive round-1
mathematics opening at its narrowed finite/conditional scope. It is not eligible
for a clean mathematics PASS until the `PSL(2,C)` double-cover sentence is
corrected. After that one-line repair, no additional mathematics review round
should be necessary unless the frozen artifacts change materially.
