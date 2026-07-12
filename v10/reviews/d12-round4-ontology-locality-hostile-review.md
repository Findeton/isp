# D12 hostile ontology/locality review — final focused round 4

**Date:** 2026-07-11  
**Verdict:** **PASS AT NARROWED FINITE-PACKET / UNITARY-FRAME SCOPE**

## Reproduction

The frozen artifacts match the authoritative hashes:

```text
54c2c6e1f193658924e3ac35e52ca897f95a07dbd4412bf86b4b0f0e0fb2b74b  code/d12_multidiamond_history_exact.py
05ecdc0a99859ea3d2b8cc99e39edfc9d8e84ed8d1c02ab55ba715a16711a21c  Paper 13
```

Normal and optimized execution are byte-identical:

```text
checks=145
stdout_sha256=466cbfc9dbdfb4432428779b1f4054921a98f3869c3aa665ba723e7e0a623521
semantic_receipt=d48f9a161dd3e7f850726225d9ea3faad8433fe35ede0c3957cbbb0963e691c6
```

## Final blocker probes

### Endpoint-frame domain

**CLOSED.** `fire()` now verifies `A^dagger A=I` for the newly supplied upper
frame before constructing a link, pointer, record, or output collar. Direct
execution with the frozen diagonal `NONUNITARY` frame raises `ValueError`:

```text
nonunitary upper frame rejected True
```

The previous lower-boundary controls also remain closed:

```text
corrupted screen eligible     False
corrupted order unit eligible False
nonunitary lower frame        False
```

Both endpoints of every admitted link therefore lie inside the explicitly
claimed unitary-frame domain. This does not establish nonunitary Lorentz-frame
integration, which Paper 13 continues to leave open.

### Positive-support RN data

**CLOSED.** The packet stores exact support-relative RN contrast ratios, not
atomwise `-infinity` strings. The executable reconstructs positive support
from the stored law, conditions the law and reference on that support,
computes exact RN values, and compares their ratios with the packet field.

Independent probes give:

```text
quarter packet reconstructs True
half packet reconstructs    True
mutated ratio accepted      False
mutated support accepted    False
```

Quarter-iSWAP correctly has positive support `(1,2)` and ratio `(1)`;
half-iSWAP has singleton support `(2)` and no nonconstant ratio. Paper 13 no
longer claims their positive supports agree. The shared object is the ambient
grammar/reference; the process measure determines `Ext_(G,mu)`.

### Finite local threshold memory

**CLOSED.** `ClassicalCollar` contains only block phase, at most two signs,
and parent-record identity. The complete past remains in immutable records.
Direct hostile reconstruction through deeper prefixes gives maximum live
memory length two.

The three phase cases reproduce the arbitrary-depth independent-`P_r` block
conditionals. Exponential-race products reproduce the cylinder laws for both
registered values of `r`. This is a genuine finite local realization for the
specific block process, without implying that an arbitrary non-Markov measure
has a bounded local evaluator.

## Prior nonblocking issues

- **D11 wording:** closed sufficiently. Paper 13 now says what failed was
  extrapolation from terminal architecture A to a continuing architecture;
  it does not derive successor birth from record persistence.
- **Construction order:** closed at the claimed finite commuting-instrument
  scope by the exact `AB/BA` generating swap plus the adjacent-incomparable-
  swap lemma. Overlapping operations retain physical order.
- **Egri/Barandes:** closed. The bridge is labeled proposed and contested;
  probability dynamics, path measures, and implementations are distinguished.
- **Repeat-read:** the receipt still uses this phrase for immutable
  stored-value persistence rather than a second physical measurement. This is
  a harmless label at the declared classical-record scope, not a physics
  durability theorem.

## Accepted result and boundary

The completed D12 result is:

```text
WORKING FINITE MULTI-COMMIT DIAMOND PACKET
+ IMMUTABLE RECORDS AND DECLARED OUTPUT-COLLAR BIRTH
+ FINITE LOCAL ELIGIBILITY AND BOUNDED CLASSICAL MEMORY
+ PROJECTIVE QUANTUM PREFIXES AND ALL-LEVEL P_r CYLINDERS
+ FINITE COMMUTING-SCHEDULE CONSTRUCTION GAUGE
+ INDEPENDENT UNITARY VERTEX-FRAME TRANSPORT
+ TWO PACKETS PASSING THE SAME TESTED ARCHITECTURE
+ DIFFERENT DURABLE-RECORD PROBABILITIES
= UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS
```

This PASS does **not** supply or select:

```text
the universe's actual process measure or interaction coupling;
general cosmological bridge/branch grammar;
nonunitary Lorentz-frame integration;
quantum gravity or Einstein dynamics;
the evidence-to-metre/second scale bridge;
round-cone, dimension, or V9 geometry predictions.
```

The core theorem is underdetermination relative to the tested packet
principles: a supplied compatible whole-history measure determines its
cylinder conditionals, but sealed-record architecture, evidence survival,
symmetry, covariance, and projectivity do not select that measure or its
interaction.

## Verdict

**PASS AT NARROWED FINITE-PACKET / UNITARY-FRAME SCOPE.** All three ontology
blockers and the final upper-frame constructor hole are genuinely repaired.
The exact executable reproduces, hostile mutations are refused, and Paper 13
keeps the unresolved physical selection and geometry questions outside the
theorem. D12 is closed as an underdetermination result, not as the final law
of our universe.
