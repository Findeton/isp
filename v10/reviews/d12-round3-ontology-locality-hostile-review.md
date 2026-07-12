# D12 hostile ontology/locality review — focused round 3

**Date:** 2026-07-11  
**Verdict:** **NOT YET PASS — ONE RESIDUAL FRAME-BOUNDARY BLOCKER**

## Reproduction

The authoritative frozen artifacts match the supplied hashes:

```text
12ca4f04b65351158bdcb9eda3e455baa73340c077cbb604cf1c9582a555e0a6  code/d12_multidiamond_history_exact.py
39b42a4af1ab48a2059c18096fb616094583cce4ea26cde2c2e1664a1a741f9f  Paper 13
```

Normal and optimized executions are byte-identical:

```text
checks=142
stdout_sha256=96df7ed44360c980f9bafbf5e86a792241d774a8995c2303bc3bbf47c8ed6e78
semantic_receipt=47b5aecd660370264c2e5c377493b70a9e7371880168f2b3f9f04fed936af5ba
```

The three round-2 blockers were independently reprobed rather than accepted
from receipt labels.

## Focused residual adjudication

### 1. Boundary-data eligibility — lower boundary repaired, upper frame still open

**Status:** **PARTIAL / BLOCKING**

`eligible()` now correctly requires:

- a unitary stored lower frame;
- order unit `I4` at the stated unitary scope;
- exact equality between the stored screen and the frame-transported pointer;
- the prior type, ownership, opportunity, staleness, eventless, and state gates.

Independent mutations now reproduce the intended refusals:

```text
corrupted screen eligible     False
corrupted order unit eligible False
nonunitary lower frame        False
```

However, the transition takes a second frame at the other endpoint:

```text
fire(history, diamond_index, upper_frame, packet)
```

Neither `fire()` nor `generate()` verifies that this newly supplied
`upper_frame` is unitary. The frozen `NONUNITARY` diagonal frame rejected when
placed on the input collar is accepted when passed as the upper frame:

```text
fire(root, 0, NONUNITARY, PACKET_Q)
  -> two positive children
  -> conditional masses (1/2, 1/2)
```

This is not merely an unused malformed object. The unvalidated frame is used
to construct the link, pointer, durable record, and born collar. That born
collar becomes ineligible only at the *next* commit. The current commit has
already admitted a transformation outside the paper's explicitly claimed
unitary-frame domain.

**Required repair:** validate `upper_frame` before computing the link or
construct frames through a type whose constructor enforces unitarity. Add a
negative control showing that `fire`/`generate` reject a nonunitary frame at
every endpoint, not only a corrupted existing collar. Then rerun the framed
history and receipt gates.

### 2. Positive-support log-RN coordinates

**Status:** **CLOSED at the exact packet scope**

The extended-real strings and false shared-support claim are gone. The
packets now distinguish:

```text
shared ambient atoms and grammar;
packet-specific positive_history_support;
finite log_rn_coordinates_on_support.
```

For quarter-iSWAP, the positive support is `(1,2)`. Conditioning both its law
and the ambient uniform reference on that support gives `(1/2,1/2)`, so the
single nonconstant log-RN coordinate is exactly zero. For half-iSWAP, the
positive support is the singleton `(2,)`, so no nonconstant coordinate
exists. The stored values `(0,)` and `()` are therefore valid and finite.

Paper 13 no longer says the induced positive supports agree. The shared object
is the ambient typed grammar/reference; the process measure selects a
different positive subset. This is the correct `Ext_G` versus
`Ext_(G,mu)` distinction.

**Nonblocking hardening:** the executable checks support/coordinate
dimensions rather than reconstructing the conditional reference law from the
stored coordinates. Because both current cases are trivial, independent
reconstruction closes them. A future nonuniform packet should add an explicit
support-ledger basis and reconstruction gate.

### 3. Finite classical collar and all-level threshold equivalence

**Status:** **CLOSED**

`ClassicalCollar` no longer contains `sealed_prefix`. Its live data are:

```text
block_phase in {0,1,2};
block_memory with length <= 2;
parent record identifier.
```

The complete values remain in the immutable history/record sequence rather
than being copied into the live interface. `advance_classical_collar()` resets
memory after every complete triple. Direct reconstruction through depth nine
never exceeds two stored signs.

The finite-collar conditionals agree exactly with the arbitrary-depth
independent-`P_r` block formula in each of the three recurring phase cases.
The exponential-race winner probabilities equal those conditionals, and
their products reproduce the tested cylinder masses for both `r=1/2` and
`r=1/3`. The displayed block formula and its three-case recurrence supply the
all-level induction. Architecture E is now genuinely local and finite for
this particular block process. Paper 13 correctly refuses to generalize that
local computability to an arbitrary whole-history measure.

## Prior nonblocking issues

### D11 wording

**Residual wording only.** The abstract improved “accidentally replaced” to
“tested a different terminal-port ontology,” and the final verdict says
continuation is declared rather than derived. Section 2 still says D11's
physical interpretation “did not” survive and calls its port disposable.
D11's repaired architecture retains its durable record while terminating the
live carrier. The clean statement is that terminal architecture A cannot
adjudicate continuing architecture B, not that durable-record ontology itself
forces continuation.

### Construction-order scope

**Closed at the claimed finite commuting-instrument scope.** Paper 13 now
states the adjacent-incomparable-swap lemma. The exact `AB/BA` cell supplies
the generating swap, and the overlap control excludes physically ordered
operations. This proves weight/presentation independence for finite schedules
whose incomparable instruments commute. It is not a theorem for arbitrary
noncommuting or dynamically created spacelike supports, and the paper no
longer needs that stronger claim.

### Egri/Barandes wording

**Closed.** The selector table now labels the stochastic-quantum bridge
proposed and contested, distinguishes probability dynamics from probability
on trajectories, and makes D12's disintegration result independent of that
dispute.

### “Repeat-read” label

**Residual wording only.** The executable proves immutable stored-value
persistence, not a second physical nondemolition measurement. The underlying
record property is adequate at the declared classical-record scope, but the
receipt should preferably say `record_value_persistence` unless an actual
read instrument is added.

## Accepted narrowed result

Subject only to upper-frame validation, the following result is now supported:

```text
WORKING FINITE MULTI-COMMIT DIAMOND PACKET
+ IMMUTABLE RECORDS AND BORN OUTPUT COLLARS
+ FINITE LOCAL ELIGIBILITY AND BOUNDED CLASSICAL MEMORY
+ PROJECTIVE QUANTUM PREFIXES AND ALL-LEVEL P_r CYLINDERS
+ FINITE COMMUTING-SCHEDULE CONSTRUCTION GAUGE
+ INDEPENDENT UNITARY VERTEX-FRAME TRANSPORT
+ TWO COMPLETE PACKETS WITH DIFFERENT RECORD PROBABILITIES
= UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS
- NONUNITARY LORENTZ INTEGRATION
- UNIVERSE-SPECIFIC PROCESS SELECTION
- COSMOLOGICAL BRIDGE GRAMMAR, GRAVITY, SCALE, AND GEOMETRY
```

The upper-frame hole does not affect the already generated five-frame tower,
because those particular frames were separately verified unitary. It does
mean the public history constructor and its eligibility claim are not closed
under the stated domain.

## Verdict

**NOT YET PASS — ONE RESIDUAL FRAME-BOUNDARY BLOCKER.** The positive-support
ledger and finite-memory threshold repairs are genuine, and the prior
literature/construction scope issues are now honest. Reject a nonunitary newly
supplied upper frame before firing, add the exact negative gate, and
synchronize the two remaining wording labels. After that focused repair, D12
should be eligible for PASS at the narrowed finite-packet/unitary-frame
`UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS` scope.
