# D17 hostile round-1 quantum-measure mathematics review

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**  
**Formal status:** `INCOMPLETE-INVESTIGATION`

## Decision

The narrow nonselection counterexample is valid: with one fixed two-order
domain and fixed action phases, two supplied preparations produce recorded
probabilities `(1/2,1/2)` and `(1,0)`. Therefore the action alone does not
select the boundary state or recorded law.

All 19 checks reproduce. The D14 seal is genuinely typed, isometric, emits a
live collar, gives orthogonal records and admits a protected future. The
finite probability arithmetic is exact.

The advertised quantum-history scope is substantially wider than the
executable. The depth towers are hand-written mark tables, not causal-order
extensions; no induction proves all-depth projectivity; no local hidden memory
or deletion control realizes the non-Markov law; and orbit-measure variation
is not propagated through amplitudes, records and projective towers. Thus H5,
H6, H7 and H8 remain open.

## Reproduction

```text
source    d71af38afa1a434b992cef2fa37c949a5ee2642b7c133c04ca16dee3e233805d
packet    08cffa34cf2b5b128ded2725299ce5a3dd46abad97164aa5435f3e89abcae0b0
semantic  7fa71590dc6fc08eec118d20974a06276a675cd7bd89b421444375d6da0c9da2
stdout    b3a70d06ef5726a491919d2188f58776a90f3c0c12c05f177d13f92e073b4c03
checks    19/19 normal and optimized
```

Dependencies match frozen D14 `e0db2c...` and D16 `861279...`.

## Blocker ledger

```text
Q1 MAJOR boundary state and action phase are multiplied before being named;
         H0 factors are not represented separately.
Q2 MAJOR supplied mark towers are not causal-order extension histories.
Q3 MAJOR projectivity is checked only at depths 1-3 with no induction.
Q4 MAJOR non-Markov tables have no local memory realization/deletion control.
Q5 MODERATE orbit conventions are compared as numbers but not integrated into
            complete amplitude/record/tower packets.
Q6 MODERATE “complete history laws” overclaims finite supplied cylinders.
Q7 MINOR full Hermitian/positive/normalized decoherence matrix is inferred
         from orthogonal branches rather than frozen explicitly.
```

## 1. Fixed action, domain and H0 factorization

The orders and `IntervalAction(0,(1,0,0,0))` are fixed, and its phases are
correctly `(-1,+1)`. But `equal_boundary_state` is actually the final amplitude

```text
(phase_0/sqrt(2), phase_1/sqrt(2)),
```

not the boundary state before action multiplication. The delta object likewise
contains `phase_0`. This does not invalidate state nonselection, but it fails
the frozen H0 demand to expose `Psi`, orbit square-root weight and `exp(iS)` as
separate factors.

Repair by constructing `Psi_equal`, `Psi_delta`, `mu_uniform` and `mu_inverse`
separately, then computing `A_i=Psi_i*sqrt(mu_i)*phase_i`. Freeze that the same
orders, action, record map and extension grammar are used in every packet.

## 2. Interference, D14 records and Born once

Opposite unrecorded amplitudes cancel exactly. The D14 map copies the two-valued
alternative into a sealed record and appends collar label one. Its columns are
orthonormal, branch inner product is zero, and norm-squared record weights are
half-half. A later identity morphism preserves the record.

This is a correct Born-once finite record cell. However the “causal-order” bit
is merely a two-state carrier whose basis is externally identified with chain
and diamond. No order boundary, extension or matter interaction enters D14.
Freeze the full two-by-two decoherence functional, Hermiticity, positivity and
normalization directly, and retain the conditional-record-instrument ceiling.

## 3. Orbit measure variation

The automorphism counts `1` and `2` and normalized conventions `(1/2,1/2)` and
`(2/3,1/3)` are exact. This proves orbit convention freedom numerically.

It does not yet prove that two orbit packets pass H0-H6: neither convention is
inserted as a square-root amplitude factor, sealed, decohered or extended into
a tower. Build both end-to-end packets before claiming orbit-measure
nonselection at the same strength as boundary-state nonselection.

## 4. Projective towers and non-Markov scope

`projective_tower` writes three tables by hand. Child sums equal parents, and
the inconsistent control fails. The conditional values one and zero are
arithmetically correct.

These strings are marks `(x,y,z)`, not causal orders `C`, and no truncation map
removes a causal element or validates an allowed typed extension. The same
fixed action is never evaluated on tower nodes. There is also no induction
beyond depth three.

Moreover the table reads the earlier `x` directly when assigning `z`; no
locally transported hidden carrier is built, and no memory deletion changes
the process. Thus it demonstrates compatibility of a supplied finite
non-Markov distribution, not H6's integrated local-memory law.

Replace “complete history laws” by “depth-1-to-3 supplied mark-cylinder
families.” To strengthen it, construct typed causal extensions, their
truncations and action amplitudes, derive records sequentially, prove the
completeness induction, and add a local memory/reset control.

## Gate disposition

```text
H0 PARTIAL; factors are conflated in amplitude variables.
H1 PARTIAL; exact conventions shown, not end-to-end packets.
H2 PASS for one supplied two-alternative D14 seal.
H3 PASS at that finite cell.
H4 PASS for recorded two-branch partition; freeze full D explicitly.
H5 FAIL beyond supplied depths 1-3; no causal truncations or induction.
H6 FAIL as a local-memory claim; numerical conditionals pass.
H7 PASS for boundary-state nonselection; PARTIAL for orbit packets.
H8 OPEN; no causal extension grammar.
H9 PASS in prose; no sampler/proper-time claim.
H10 OPEN; V9 correctly withheld.
H11 OPEN; major repairs remain.
```

## Final verdict

**MAJOR REVISION.** The fixed-action boundary-state nonselection theorem is a
sound finite subresult, and the D14 record cell is exact. The receipt does not
yet construct complete causal history laws: it supplies finite mark tables
without causal extensions, all-depth projectivity or local memory. Narrow the
theorem accordingly or implement H0/H5-H8 end to end.
