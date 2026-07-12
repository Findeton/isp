# D15 focused round-3 mathematics/action review

**Date:** 2026-07-11  
**Reviewer:** independent mathematics/action referee  
**Verdict:** **PASS AT THE DECLARED FINITE CONDITIONAL SCOPE**  
**Formal D15 status:** remains `INCOMPLETE-INVESTIGATION` for the broader
empirical, EFT4/gravity and UV-selection protocol

## Decision

All focused mathematical minors from round 2 are closed on the final 28-check
candidate.

The D14 action dictionary is now confined to one explicit owner, `cell-A`.
System and environment are therefore carriers of one local component rather
than an unlicensed cross-component join.  The paper states this ontology and
does not claim to exercise a join.  The actual D14 constructor directly
rejects a record flip.  The four-bit memory circuit embeds entries of the
two-bit CNOT kernel produced by the `Z2` multiplier action, rather than
reimplementing an independent truth table.  Its visible conditionals are
exactly one and zero.  The Bell label, finite regulator, trivial gauge quotient,
fixed boundary basis, single-owner scope and dimensionless action phases are
all stated correctly.

No replacement blocker was found.  This PASS applies to one finite,
nongravitational, action/measure/support-plus-supplied-record dictionary.  It
does not upgrade the toy to an EFT4 regulator, autonomous record selector,
cross-component birth law, physical unit bridge or fundamental action.

## Frozen artifacts and reproduction

```text
9f539129d5712d28b86d89637248a0fe3b60678fcc29fcddf2e5e675aa8fb4b9  code/d15_regulated_action_dictionary_exact.py
b9bc2fc3a2c8dc9342d985df55f2298db182e8cf0a0e97fc22fd8de5fa2d3b41  data/d15-regulated-action-dictionary-exact.json
0d39eb2f023ce33fb27a0455424a8fba2e93dec590b3de6cc71fae84a27bd66b  note-d15-maximal-low-energy-action.md
99be0212ca2e0afb7dd837dfdcc5b8ab3c189d6e9356e306070e876bfdf6f070  note-d15-eft-action-parameter-ledger.md
f29d06acf04d066a297be22bec693a7082994cc4b87d1f058210918c494f717c  data/d15-regulated-dictionary-pre-review-receipt.md
26984f708277ba0a630a2444b3132412e824c29f86bdf56a0fc65906c34cf44f  reviews/d15-round2-mathematics-action-review.md
```

Independent execution produced:

```text
checks                         = 28/28
normal stdout SHA-256          = 06c5ab5d6455942e14835814914a57f0cc6dad4a4f30997bc504d04153446408
optimized stdout SHA-256       = 06c5ab5d6455942e14835814914a57f0cc6dad4a4f30997bc504d04153446408
semantic SHA-256               = 12f73918e7876a2f423d1d4596163e787f52ac50332f2d59bb941c0381f499fe
source SHA-256                 = 9f539129d5712d28b86d89637248a0fe3b60678fcc29fcddf2e5e675aa8fb4b9
packet SHA-256                 = b9bc2fc3a2c8dc9342d985df55f2298db182e8cf0a0e97fc22fd8de5fa2d3b41
D13 arithmetic dependency      = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
D14 bridge dependency          = e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
```

Normal and optimized stdout are byte-identical, the packet matches the
receipt, and no Python `assert` supplies a gate.

## 1. Owner confinement and join scope

The D14 objects are now:

```text
system       owner=cell-A
environment  owner=cell-A
record       owner=cell-A, sealed, record_id=R
collar       owner=cell-A.
```

The environment injection, CNOT interaction, environment-to-record commit and
collar emission all consequently operate inside one declared component.
D14 primitive admission sees no mixed ownerless/owned source and no
multi-owner source requiring entitlement.

The exact receipt additionally verifies that every external source and target
port of the composed seal has owner `cell-A`.  Intermediate objects are built
from the same four port values, so owner confinement is preserved throughout
the composition.

This is the correct resolution of the round-two fork: D15 chose the
same-component laboratory interpretation.  It therefore need not invent a
join entitlement.  The paper explicitly says no cross-component join is
exercised, so this cell does not claim to solve the origin of joins.

## 2. Direct record-protection control

After the action/environment/commit/collar chain, the seal target is

```text
system tensor protected-record tensor collar.
```

The future system action has protected correspondence

```text
((1,1),)
```

and composes normally.  The new direct hostile control then attempts

```math
I_S\otimes X_R\otimes I_C.
```

D14 `Mor` construction raises because a nonzero entry changes the mapped
record label.  The receipt freezes that rejection.  Thus persistence is no
longer supported only by one friendly system-only future; the obvious
adversarial overwrite is executed and refused in D15 itself.

The record is still born through a supplied explicit commit.  This is not a
defect at the declared scope: the primary calls the commit and pointer
interpretation supplied and grades S5 conditional.

## 3. Memory circuit now depends on the action-derived CNOT

`cnot_four(two_bit_kernel, control, target)` reads each entry of the supplied
four-by-four kernel, inserts that input/output pair on the selected two factors
and leaves spectator factors fixed.  D15 calls it with the `cnot` matrix
obtained from the exact multiplier sum:

```text
U_mem = embed(CNOT, M,Z) embed(CNOT, X,M).
```

The memory circuit can therefore no longer drift independently from the
action-derived two-bit kernel.

For the equal mixture of `0000` and `1000`, exact evolution gives support

```text
0000 with mass 1/2;
1101 with mass 1/2.
```

Tracing the hidden memory bit and conditioning on the visible bits yields

```text
P(Z=1 | Y=0,X=1)=1,
P(Z=1 | Y=0,X=0)=0.
```

I reconstructed these conditionals by explicitly summing over memory and the
two final-bit values in normal and optimized Python; both agree exactly.

The built-in variables use state-specific ratios `rho[13,13]/rho[13,13]` and
`rho[1,1]/(rho[0,0]+rho[1,1])` rather than a generic marginalization helper.
For this exact state the preceding unitary construction and frozen half-masses
put all trace mass on indices 0 and 13, so the ratios certify the stated
values.  A future generic conditional helper would improve readability but is
not needed for truth of this finite cell.

## 4. Label and regulator closure

The source now says “Bell state has exact perfect same-basis correlation.”
This accurately describes the subtest: it is a Bell-state preparation and
computational-basis correlation, not a D14 record or CHSH self-test.

The paper also prints the entire finite-scope ledger:

```text
regulator              = finite binary boundary/history sum;
gauge group/quotient    = trivial;
boundary basis          = fixed;
vertex normalization    = fixed supplied measure;
component ownership     = one owner, cell-A;
cross-component join    = not exercised;
action phases           = dimensionless.
```

This closes the ambiguity that `Z2` might denote an unaccounted gauge theory.
It also prevents the qubit witness from being mistaken for a metre/second/`G`
bridge or a discretization of gravity.

## 5. Fixed-frame and EFT scope retained

The fixed-frame experiment continues to distinguish the base and
phase-modified local kernels at probabilities `1` and `1/2` under one shared
boundary dictionary.  It is not promoted to frame-independent UV
inequivalence.

The EFT normal-form and parameter ledger remain appropriately separate from
this finite witness.  `xi_H H^dagger H R`, operator equivalences, the
curvature/matter tower and coefficient classes remain present.  A concrete
scheme/scale/truncation fit, generally covariant regulated D14 cell,
autonomous record selection and complete UV survivor test remain open under
the formal `INCOMPLETE-INVESTIGATION` status.

## Focused closure ledger

```text
F1 explicit owner confinement                    CLOSED
F2 same-component/no-join scope                  CLOSED IN PROSE AND CODE
F3 direct D15 record-flip rejection              CLOSED
F4 four-bit memory built from two-bit kernel     CLOSED
F5 exact visible conditionals 1 and 0            CLOSED AT FINITE STATE SCOPE
F6 Bell correlation label                        CLOSED
F7 finite regulator and trivial gauge ledger     CLOSED
F8 dimensionless/no-unit-bridge scope            CLOSED
```

## Final verdict

**PASS AT THE DECLARED FINITE CONDITIONAL SCOPE.**  The round-two minors are
repaired, all 28 exact checks reproduce, and no mathematical blocker remains
in the finite action-to-D14 witness.  Preserve the broader formal
`INCOMPLETE-INVESTIGATION` status: this closure does not select an autonomous
record law, generally covariant EFT4 regulator, cross-component join law,
physical scales or a unique UV action.
