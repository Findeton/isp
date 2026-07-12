# D12 hostile review, round 3: independent focused rebuild

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION / ONE FOCUSED RECEIPT BLOCKER**

The frozen 142-check replacement closes the screen/order-unit/frame and
finite-memory threshold openings.  Its classical all-level construction and
the main interaction-nonselection theorem also survive independent
reconstruction.  The positive-support Radon--Nikodym repair, however, is not
actually certified by the executable: its only gate checks tuple lengths.
In-memory hostile mutations show that a false coefficient and a false support
both pass all 142 checks and preserve both advertised receipts byte-for-byte.

This is a narrower finding than a rejection of D12's mathematical conclusion.
The two hard-coded support/coordinate pairs happen to be correct on manual
inspection, and the quarter-/half-iSWAP counterexample still proves
nonselection.  But round 2 explicitly required an exact reconstruction gate,
and the frozen round-3 receipt claims validity without one.  The advertised
complete-packet repair is therefore not yet executable evidence.

## 1. Frozen artifacts and exact reproduction

I reviewed these frozen artifacts:

```text
12ca4f04b65351158bdcb9eda3e455baa73340c077cbb604cf1c9582a555e0a6  v10/code/d12_multidiamond_history_exact.py
39b42a4af1ab48a2059c18096fb616094583cce4ea26cde2c2e1664a1a741f9f  v10/relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

Normal and optimized execution, both with bytecode writes disabled, produce
the same complete stdout hash:

```text
96df7ed44360c980f9bafbf5e86a792241d774a8995c2303bc3bbf47c8ed6e78
```

Both runs report:

```text
checks=142
depth=4
depth4_histories=16
finite_phase_two_sign_threshold_collar=PASS
equivalent_local_exponential_threshold_representation=PASS
receipt_sha256=47b5aecd660370264c2e5c377493b70a9e7371880168f2b3f9f04fed936af5ba
```

The frozen source, Paper 13, and the round-1 repair receipt agree on the check
count and all four source/stdout/semantic/paper hashes.  I found no numerical
or prose drift in the stated unitary-frame, primitive-process scope.

## 2. Screen, order-unit, and frame refusal

This repair is substantive.  `eligible` now requires:

```text
an unconsumed eventless collar;
the packet's incoming types;
the connected two-owner tuple;
the exact emitted opportunity;
a unitary endpoint frame;
the identity order unit;
the pointer screen transported into that frame;
a normalized state.
```

The new negative controls alter fields that the predicate actually reads:

- reversing the collar screen is rejected;
- replacing the order unit with a rank-one pointer projector is rejected;
- assigning a nonunitary diagonal frame is rejected.

Thus these are not decorative post-construction assertions.  The generated
collars at all tested depths carry the transported screen and identity unit,
and the frame sequence is independently unitary.  The paper correctly limits
the result to unitary frames; it does not promote this to an integrated
nonunitary Lorentz gauge.

One harmless asymmetry remains: the exhaustive screen covariance checks run
on the quarter-iSWAP framed tower, while the common two-model audit checks only
screen arity and the order unit for each packet.  Both packets use the same
constructor, so this does not affect the two-model counterexample.

## 3. Positive-support RN fields: values correct, gate absent

The revised objects are conceptually the right ones:

```text
quarter-iSWAP law       (0, 1/2, 1/2, 0)
positive support        (1, 2)
conditional reference  (1/2, 1/2)
conditional law         (1/2, 1/2)
quotient log-RN data    (0)

half-iSWAP law          (0, 0, 1, 0)
positive support        (2)
conditional reference  (1)
conditional law         (1)
quotient log-RN data    ()
```

So the stored finite values avoid the former extended-real `-infinity`
mistake.  They also correctly demonstrate that positive support is additional
data not selected by finite log-RN coordinates.

The executable gate is nevertheless only:

```python
support_Q != support_H
len(coords_Q) == len(support_Q) - 1
len(coords_H) == len(support_H) - 1
```

It never derives either support from `one_diamond_history_law`, defines an
induced support contrast basis, computes density ratios relative to the
conditioned reference, or reconstructs the conditioned law from the stored
coordinates.  The label
`finite log-RN coordinates are valid on each positive support` therefore says
more than its Boolean condition establishes.

### Hostile mutation result

I executed two source mutations entirely in memory, leaving the frozen file
untouched:

```text
(1, 2), (0)  ->  (1, 2), (7)    false RN coordinate
(1, 2), (0)  ->  (0, 3), (0)    false positive support
```

Both mutations survived all 142 checks.  Both printed exactly:

```text
stdout_sha256 = 96df7ed44360c980f9bafbf5e86a792241d774a8995c2303bc3bbf47c8ed6e78
semantic      = 47b5aecd660370264c2e5c377493b70a9e7371880168f2b3f9f04fed936af5ba
```

This is a decisive mutation test: the advertised receipts cannot distinguish
the valid packet from packets containing mathematically false support/RN
data.  Because the round-2 hostile review expressly required an exact
reconstruction gate, the repair is incomplete rather than merely
under-tested.

### Required focused repair

The next source should, for each packet:

1. derive `positive_history_support` exactly from the positive entries of the
   stored history law;
2. condition both the law and the positive reference on that support;
3. define the support contrast convention and verify every stored finite
   coordinate;
4. reconstruct the conditioned law, up to normalization, from those
   coordinates and the conditioned reference;
5. add hostile wrong-support and wrong-coordinate refusal probes; and
6. make those data affect the semantic receipt through the passed gates.

For the present two packets this needs no numerical logarithm: every
conditioned density ratio is exactly one, so the sole nonconstant coordinate
is exactly zero and the singleton quotient has dimension zero.

## 4. Finite phase/two-sign collar

This repair closes the unbounded-live-memory objection.  A live
`ClassicalCollar` stores only:

```text
block phase in {0,1,2};
zero, one, or two signs from the current block;
one parent-record identifier.
```

After the third sign the phase and memory reset.  The complete past remains in
the immutable record tuple, not in the live interface.

For

```math
P_r(x,y,z)=(1+rxyz)/8,
```

the first two signs of each block are fair, and the third has conditional law

```math
P_r(z\mid x,y)=(1+rxyz)/2.
```

The executable constructs the collar from every prefix through depth nine for
`r=1/2` and `r=1/3`, bounds memory by two, and compares its conditional with
the independent block-index formula.  It separately verifies normalization,
every adjacent bonding map, and exact disintegration.  The displayed
arbitrary-`n` product in Paper 13 supplies the general continuation proof.

Invalid hand-constructed phase/memory pairs are not rejected, but generated
collars preserve the invariant by construction.  No general untrusted-collar
parser is claimed, so this is not a blocker.

## 5. Threshold equivalence at and across block boundaries

The threshold repair is also sound.  Independent exponential clocks with
rates `lambda_e` select `e` with probability

```math
lambda_e / \sum_f lambda_f.
```

Taking the already supplied conditional probabilities as rates therefore
represents, rather than selects, the primitive history process.  Since the two
rates sum to one, the race winner law equals the finite-collar conditional
exactly.

The focused tests include the completed-block prefix `(1,1,-1)`.  Product
equality is then checked for every cylinder through depth nine, for both
values of `r`.  The all-level product check calls the independent
block-conditional function, while the preceding exhaustive gate equates that
function with the finite collar at every tested prefix.  Together with the
arbitrary-depth block formula, this closes the former first-block-only bug.

## 6. Effect on the paper's theorem

The RN receipt defect does **not** refute the central underdetermination
result.  Independently:

```math
U_\theta|01\rangle
=\cos\theta|01\rangle+i\sin\theta|10\rangle,
```

so the selected later pointer probability is `cos^2(theta)`: `1/2` for the
quarter-iSWAP packet and `0` for the half-iSWAP packet.  The two interactions
pass the same declared finite/unitary packet grammar while disagreeing on a
durable prediction.  Therefore the shared principles do not select one
interaction or whole-history measure.

Paper 13 properly keeps connectivity as primitive two-owner collar typing,
keeps evidence and commitment as supplied packet data, refuses a global
commit order, and leaves nonunitary frame integration, physical scale,
gravity, bridge grammar, and V9 geometry open.  Its arbitrary-depth classical
formula, adjacent-incomparable-swap argument, and stale-constructor invariant
match the implementation's narrowed scope.

The overclaim is localized: the exact receipt cannot currently certify that
the packet's support-specific RN fields are the fields of its stored law.

## 7. Opening ledger

| Focused opening | Round-3 finding | Status |
|---|---|---|
| corrupted collar screen | predicate consumes exact transported screen; hostile probe rejects mutation | closed |
| corrupted order unit | predicate requires identity unit; hostile probe rejects mutation | closed at unitary scope |
| nonunitary frame | predicate verifies unitarity and rejects diagonal counterexample | closed at stated unitary scope |
| positive-support RN object | hard-coded values are manually correct | mathematically repaired |
| positive-support RN executable gate | wrong support/coordinate preserve all checks and both receipts | **open blocker** |
| full-prefix live threshold memory | replaced by phase plus at most two signs | closed |
| threshold only valid in first block | boundary prefix and all cylinders through depth nine tested; formula proves all levels | closed |
| receipt/prose drift | frozen hashes, check count, semantic receipt, and scope agree | closed |

## 8. Final determination

The frozen source is an exact and persuasive witness for:

```text
continuing sealed-record construction;
unitary-frame local boundary eligibility;
projective quantum and classical history towers;
construction-order gauge for commuting disjoint events;
bounded-memory non-Markov conditionals;
threshold representation of a supplied process;
interaction/process nonselection.
```

It is not yet an exact witness that its stored positive-support RN fields
correspond to its stored law.  Because that was an explicit major round-2
repair condition and false data retain the frozen receipts, round 3 cannot
receive an unqualified PASS.

**Round-3 independent-rebuild verdict: MAJOR REVISION, limited to one exact
support/RN reconstruction and mutation-sensitivity repair.**
