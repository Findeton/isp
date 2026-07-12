# D12 hostile review, round 4: final independent rebuild

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **PASS FOR THE FROZEN EXECUTABLE AND PAPER AT THE STATED SCOPE; ADMINISTRATIVE RECEIPT MANIFEST REPAIR REQUIRED**

The two substantive round-3 openings are closed.  The frozen executable now
derives each positive support from the stored history law, reconstructs exact
support-relative Radon--Nikodym contrast ratios against the conditioned
reference, and rejects both malicious RN mutations that survived round 3.
It also validates a newly supplied upper frame before constructing a link,
screen, record, or born collar; the former nonunitary upper-frame witness now
raises the intended `ValueError` before firing.

All 145 checks reproduce under normal and optimized Python with byte-identical
stdout.  Paper 13 matches the frozen hash and accurately states the repaired
mechanisms and their unitary-frame scope.  The mathematical and constructor
closure therefore passes.

One non-scientific archive defect remains: the old round-1 repair receipt has
partly updated metadata but still lists the preceding source, stdout, and
Paper hashes, while the round-3 repair note points to a
`data/d12-final-receipt.md` file that does not exist.  This does not change the
independently reproduced result, but it should be corrected before calling
the D12 receipt archive self-consistent.

## 1. Frozen artifacts and reproduction

The supplied frozen hashes reproduce exactly:

```text
54c2c6e1f193658924e3ac35e52ca897f95a07dbd4412bf86b4b0f0e0fb2b74b  v10/code/d12_multidiamond_history_exact.py
05ecdc0a99859ea3d2b8cc99e39edfc9d8e84ed8d1c02ab55ba715a16711a21c  v10/relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

I ran the executable with bytecode writes disabled under both modes:

```text
python3 d12_multidiamond_history_exact.py
python3 -O d12_multidiamond_history_exact.py
```

Both complete outputs have SHA-256:

```text
466cbfc9dbdfb4432428779b1f4054921a98f3869c3aa665ba723e7e0a623521
```

Both report:

```text
checks=145
support_relative_rn_reconstruction_and_mutation_refusal=PASS
lower_and_upper_unitary_frame_domain_refusal=PASS
finite_phase_two_sign_threshold_collar=PASS
equivalent_local_exponential_threshold_representation=PASS
receipt_sha256=d48f9a161dd3e7f850726225d9ea3faad8433fe35ede0c3957cbbb0963e691c6
```

The fixed check-count and semantic-receipt gates remain active under `-O`;
they do not depend on Python `assert` statements.

## 2. Exact RN reconstruction

The packet now stores exact support-relative RN **ratios**, not unverified
logarithm strings or a tuple whose length merely resembles a coordinate
dimension.  For a packet, the repair performs four exact operations:

1. derive support as the indices with nonzero stored history mass;
2. require exact equality with `positive_history_support`;
3. condition the stored law and positive reference on that support;
4. divide each resulting RN value by a fixed baseline RN value and compare
   the exact ratios with the packet field.

These ratios determine the conditioned law relative to the conditioned
reference up to the normalization that has already been fixed.  Their
logarithms are the corresponding nonconstant log-RN coordinates.  No
floating-point logarithm or extended-real sentinel is needed.

For quarter-iSWAP:

```text
ambient law                 (0, 1/2, 1/2, 0)
derived positive support    (1, 2)
conditioned reference       (1/2, 1/2)
conditioned law             (1/2, 1/2)
RN contrast ratio           (1)
log-RN contrast coordinate  (0)
```

For half-iSWAP the derived support is the singleton `(2)`, so the quotient
coordinate tuple is empty.  Thus the repaired representation is exact in the
two frozen models and explicitly does not pretend that the ambient Born-zero
atoms belong to a strictly positive finite log-RN chart.

## 3. Repeated malicious RN mutations

I repeated the two round-3 attacks by mutating the source only in memory,
leaving the frozen file untouched.

### False coordinate

```text
quarter support/ratio  (1,2),(1) -> (1,2),(7)
```

Result:

```text
REJECTED
AssertionError: exact support-relative RN contrast ratios reconstruct both stored history laws
passes completed before rejection: 5
```

### False support

```text
quarter support/ratio  (1,2),(1) -> (0,3),(1)
```

Result:

```text
REJECTED
AssertionError: exact support-relative RN contrast ratios reconstruct both stored history laws
passes completed before rejection: 5
```

Both attacks now stop at the first reconstruction gate.  They cannot reach
the 145-check summary or preserve the semantic receipt.  The executable also
contains separate built-in negative controls for the false ratio and false
support, which appear as passes 7 and 8 in both normal and optimized output.

This directly closes the mutation-sensitivity failure from round 3.

## 4. Lower- and upper-frame domain refusal

The input-collar predicate still validates the stored lower frame, transported
screen, identity order unit, state normalization, types, owners, opportunity,
eventless status, and staleness.  The new repair addresses the other endpoint:

```python
if upper_frame.basis^dagger upper_frame.basis != I4:
    raise ValueError(...)
```

This occurs at the start of `fire`, after lower-collar eligibility but before
the link, upper pointer, projected outcome, durable record, or successor
collar is constructed.

I independently called `fire` on the valid root history with the diagonal
nonunitary frame used in the prior hostile witness.  The result is:

```text
REJECTED
ValueError: upper frame lies outside the stated unitary-frame domain
```

The direct built-in negative control is pass 17 under both execution modes.
The rejection is therefore at the intended boundary and is not an accidental
later failure of normalization or successor eligibility.

This closes the round-3 constructor hole at the paper's explicitly unitary
scope.  It does not establish nonunitary `SL(2,C)` history transport, and
Paper 13 continues to list that integration as open.

## 5. Regression check on the earlier repairs

The final changes do not disturb the already closed D12 results:

- quarter- and half-iSWAP remain exact unitaries with different durable
  predictions under the shared finite packet grammar;
- records and output collars remain immutable and continuing;
- the quantum cylinder tower remains normalized and projective through depth
  four with its stated continuation induction;
- independent unitary endpoint frames transport states, screens, effects,
  links, and record frame names;
- disjoint `AB/BA` presentations push to one canonical law while overlapping
  same-collar order remains observable;
- the all-level `P_r` block family remains normalized, projective, and
  non-first-order-Markov;
- its live collar stores only phase and at most two current-block signs; and
- exponential threshold races reproduce the supplied finite-collar
  conditionals and every tested cylinder through depth nine for both `r`
  values.

The central theorem remains independently immediate from

```math
U_\theta|01\rangle
=\cos\theta|01\rangle+i\sin\theta|10\rangle,
```

which yields the differing durable probability `1/2` versus `0` at the two
chosen angles.  The shared framework therefore does not uniquely select the
interaction or history process.

## 6. Paper 13 audit

The frozen Paper 13 hash is exact.  Its updated claims agree with the final
source:

- it says the replacement has 145 gates;
- it lists support-relative RN reconstruction and mutation refusal;
- it lists lower- and upper-unitary-frame refusal;
- it explains that ambient Born zeros require restriction to positive
  support;
- it describes exact RN ratios rather than treating `-infinity` strings as
  finite coordinates;
- it prints the correct semantic receipt `d48f9a...`; and
- it limits the constructor theorem to finite packets and unitary frames.

The paper still distinguishes supplied process data from derived universal
form, refuses a preferred global commit order, and leaves connectivity
grammar, empirical process selection, nonunitary Lorentz integration,
gravity, physical units, and V9 geometry open.  I found no scientific prose
drift or renewed claim to the universe's final law.

## 7. Administrative receipt-manifest finding

The research result is reproducible, but the receipt archive is not yet
self-consistent.

`v10/data/d12-round1-repair-receipt.md` now says `checks=145` and records the
new semantic receipt, but the same block still lists:

```text
old stdout  96df7ed44360c980f9bafbf5e86a792241d774a8995c2303bc3bbf47c8ed6e78
old source  12ca4f04b65351158bdcb9eda3e455baa73340c077cbb604cf1c9582a555e0a6
old Paper   39b42a4af1ab48a2059c18096fb616094583cce4ea26cde2c2e1664a1a741f9f
```

Those are the preceding 142-check freeze, not the final 145-check freeze.
Furthermore, `v10/note-d12-round3-opening-repairs.md` says the final hashes are
recorded in `v10/data/d12-final-receipt.md`, but that file is absent.

This is an administrative traceability defect, not a mathematical or runtime
failure: the final values were independently reproduced above.  Closure
requires either creating the referenced final receipt with the frozen hashes
or updating the old manifest so it is unambiguously historical rather than a
mixed final record.

## 8. Final determination

| Focused gate | Independent result | Status |
|---|---|---|
| source hash | exact `54c2c6e1...` | pass |
| Paper hash | exact `05ecdc0a...` | pass |
| normal/-O complete stdout | byte-identical `466cbfc9...` | pass |
| check count / semantic receipt | `145` / `d48f9a16...` | pass |
| malicious RN ratio mutation | rejected at reconstruction gate | pass |
| malicious RN support mutation | rejected at reconstruction gate | pass |
| nonunitary supplied upper frame | rejected before firing | pass |
| Paper scientific scope | matches execution and preserves limitations | pass |
| final receipt manifest | stale mixed manifest; referenced final file absent | **administrative repair** |

The frozen 145-check executable and Paper 13 now support D12's scoped result:
sealed-record architecture fixes a conditional universal form but does not
select the primitive interaction or whole-history process.  No substantive
round-3 blocker survives.

**Round-4 independent-rebuild verdict: PASS for the executable, mathematics,
constructor, and Paper at the stated finite-packet/unitary-frame scope.
Correct the final receipt manifest before archival closure.**
