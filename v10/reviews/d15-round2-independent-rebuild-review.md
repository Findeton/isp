# D15 hostile review, round 2: independent clean-room verification

**Referee:** independent reconstruction/reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **PASS AT THE FINITE REGULATED-DICTIONARY WITNESS SCOPE**  
**Formal D15 status:** **`INCOMPLETE-INVESTIGATION`**

The revised D15 executable is reproducible and its round-1 clean-room
openings are materially repaired.  Normal and optimized Python pass 26/26
with byte-identical stdout.  The source, generated packet, semantic object,
and D13/D14 dependency hashes agree exactly with the pre-review receipt.

D14 is now an actual semantic dependency.  D15 imports `Port`, `Obj`, `Mor`,
`compose`, and `preserves_record`; it composes fresh-environment injection,
the action-derived CNOT, environment-to-protected-record commit, and live
collar emission inside the D14 API.  The resulting typed morphism equals the
direct seal matrix exactly.  A D14-admitted future action composes and
preserves the protected record, while a fresh hostile record-flip constructor
raises.

The other repairs also survive independent attack.  The exact `Z2` multiplier
sums generate the full CNOT zero/support pattern.  The memory matrix is rebuilt
locally from two four-bit CNOT placements and maps basis indices `0 -> 0` and
`8 -> 13`.  The alternative phase action gives closed fixed-frame probability
`1/2` versus the base action's `1`.  When the downstream cell is transformed
as required for a pure boundary-frame change, the phase cancels and the
probability returns to `1`.  Thus the tested fixed-frame distinction is not a
frame-gauge artifact.

The primary notes and UV audit preserve the correct ceiling.  This is one
finite nongravitational S4 witness and a conditional S5 environment-
decoherence witness.  It is not an autonomous record law, generally covariant
gravity action, continuum limit, UV selector, `3+1` derivation, scale
calculation, or V9 holdout.  The UV audit lists incomplete survivors and
explicitly refuses `FUNDAMENTAL-NONSELECTION-PROVED` as a no-go theorem.

No remaining clean-room opening weakens the 26-check witness at that narrowed
scope.  The full D15 protocol remains incomplete for the reasons its notes
state.

## 1. Authoritative reproduction

### Commands

From `/Users/felixrobles/workspace/isp`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d15_regulated_action_dictionary_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d15_regulated_action_dictionary_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d15_regulated_action_dictionary_exact.py | shasum -a 256
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d15_regulated_action_dictionary_exact.py | shasum -a 256
shasum -a 256 v10/code/d15_regulated_action_dictionary_exact.py
shasum -a 256 v10/code/d13_finite_kernel_no_go_exact.py
shasum -a 256 v10/code/d14_action_record_bridge_exact.py
shasum -a 256 v10/data/d15-regulated-action-dictionary-exact.json
```

Both direct runs completed with the same 26 labels and ended in:

```text
PASS 026: pre-final exact check count is frozen
CHECKS PASSED: 26/26
SEMANTIC SHA256: f739c75352b8099b85836b4b7c471d131a173491217156e9d3da7d658ca1f1e3
SOURCE SHA256: 78af9ed95a1ab5e27aa5edea2104c8f834688a1a1b3a06c6ef271b35afdb045a
VERDICT: REGULATED-ACTION-DICTIONARY-WITNESS-PASSED
```

The complete stdout hashes are byte-identical:

```text
normal  89bef6673905ceac8506cd2a6e9624a3265a31e087f7a69ead0f3d8a59152384
-O      89bef6673905ceac8506cd2a6e9624a3265a31e087f7a69ead0f3d8a59152384
```

Current authoritative hashes are:

```text
78af9ed95a1ab5e27aa5edea2104c8f834688a1a1b3a06c6ef271b35afdb045a  D15 source
d4ea94c6b727aa9ec7e20cad1304ad019e4711ffc1512d0f90532d75e01b3777  generated packet
f739c75352b8099b85836b4b7c471d131a173491217156e9d3da7d658ca1f1e3  semantic object
1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45  D13 dependency
e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425  D14 dependency
```

I independently selected and compactly serialized the six semantic fields in
the packet and reproduced `f739c753...` exactly.  Every hash printed in
`d15-regulated-dictionary-pre-review-receipt.md` matches current bytes and
execution.

## 2. Optimization and packet provenance

No Python `assert`, `__debug__` branch, random source, wall clock, external
package, floating arithmetic, or optimization-sensitive path supplies a gate.
`check`, the exact count guard, and the semantic-hash guard use explicit
conditionals, so `-O` cannot erase them.

The program writes the JSON only after all checks and the semantic hash pass.
No check reads the packet.  Regeneration gives the frozen packet hash, so the
receipt is not self-authenticating.

D13 supplies the exact arithmetic runtime.  D14 now supplies imported classes
and operations that are executed, in addition to being hash-locked.  This
closes the former hash-only dependency problem.

## 3. Focused adversarial driver

I ran a separate probe program:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/d15_round2_adversarial_probes.py
```

Its exact relevant output was:

```text
D14 classes d14_action_record_bridge_exact d14_action_record_bridge_exact
typed seal equals direct True
typed target True
record sealed/id True R
D14 overwrite rejected protected record overwrite
future protected correspondence ((1,1),) True True
Z2 multiplier support ((1,0,0,0),(0,1,0,0),(0,0,0,1),(0,0,1,0))
local memory indices ([0],[13])
closed probabilities base/fixed/gauge-cancelled 1 1/2 1
D15 ROUND2 PROBES COMPLETE
```

These probes construct new hostile maps and separately enumerate support; they
do not merely parse the executable's PASS labels.

## 4. Actual D14 integration

The typed action dictionary now uses:

```text
q                    = D14 system object;
environment          = fresh unsealed two-level object;
record               = sealed D14 object with record_id R;
collar               = D14 live output object;
fresh injection      = q -> q tensor environment;
CNOT interaction     = q tensor environment -> q tensor environment;
commit               = environment label -> fresh protected record;
live emission        = q tensor record -> q tensor record tensor collar.
```

All four maps are D14 `Mor` instances and are composed with D14 `compose`.
The resulting `8 x 2` amplitude is byte-for-byte the independently written
direct seal.  Its target is exactly `q tensor record tensor collar`.

The later system action is admitted on that target with protected
correspondence `((1,1),)`.  It composes after the seal and preserves the record
label.  A matrix that flips the middle record bit is rejected by D14's
constructor.  Therefore the dependency cannot be replaced by a mere matching
hash without losing executed behavior.

This is a genuine finite nongauge S4 bridge instance.  It does not supply an
EFT4/gravity regulator, gauge fixing, edge modes, or an autonomous record
environment; the notes do not claim that it does.

## 5. Direct seal equality and protected future

The direct seal has the only nonzero transitions:

```text
|0> -> |0>_S |0>_R |1>_C,
|1> -> |1>_S |1>_R |1>_C.
```

The D14 composition produces exactly the same transitions by:

```text
|s> -> |s>|0>_E
     -> CNOT |s>|0>_E = |s>|s>_E
     -> |s>|s>_R
     -> |s>|s>_R|1>_C.
```

Thus the seal is no longer a logically independent hardcoding: the equality
between the action composition and direct optimized matrix is an exact gate.
The Born record distribution `(1/2,1/2)`, live collar, pointer decoherence,
recorded interference `1/2`, and future marginal persistence follow on that
same matrix.

## 6. Exact `Z2` multiplier support

The CNOT kernel is now generated by two finite Fourier delta sums:

```text
(1/2) sum_lambda (-1)^[lambda (b_c xor a_c)],
(1/2) sum_lambda (-1)^[lambda (b_t xor a_t xor a_c)].
```

Each is one when its binary constraint vanishes and zero otherwise.
Independent enumeration gives:

```text
[[1,0,0,0],
 [0,1,0,0],
 [0,0,0,1],
 [0,0,1,0]],
```

exactly the CNOT permutation.  The support zeros are therefore derived from
the printed multiplier sum rather than inserted as an unexplained delta
matrix.  The `1/sqrt(2)` Hadamard vertex measure remains explicitly supplied,
as the notes correctly state.

## 7. Memory rebuilt locally

D15 no longer imports D13's memory circuit.  It constructs a four-bit CNOT
placement and composes:

```text
CNOT X -> M,
CNOT M -> Z.
```

The resulting permutation is unitary and maps input basis index `0` to `0`
and input index `8` (`1000`) to `13` (`1101`).  The audited mixture therefore
has exact mass `1/2` at output indices 0 and 13.

The placement helper encodes the same binary CNOT rule whose two-bit support
is independently frozen in check 6.  As an optional hardening, a generic
tensor/permutation embedding could take the two-bit `cnot` matrix as an
argument, but no current numerical or semantic mismatch remains.

## 8. Fixed-frame distinction and gauge control

Let

```text
K       = H,
K_alt   = P H,
P       = diag(1,i).
```

With preparation `|0>`, downstream `H`, and final `|0>` effect all held fixed,
the closed probabilities are:

```text
|<0| H H |0>|^2     = 1,
|<0| H P H |0>|^2   = 1/2.
```

This closes the round-1 matrix-inequality weakness.  It also survives the
frame-gauge challenge in the correct way.  If `P` were only a new coordinate
frame on the glued boundary, the adjacent downstream kernel would transform
to `H P^dagger`; then:

```text
(H P^dagger)(P H)=H H,
```

and the probability is again 1.  D15 deliberately keeps the downstream frame
and external experiment fixed, so the observed `1/2` represents a physical
relative phase insertion rather than a pure frame change.

This proves only that the finite dictionary architecture does not select one
local action.  It is not S10 fundamental UV nonselection, and the UV audit
does not promote it to that theorem.

## 9. Receipt, notes, and UV audit

The pre-review receipt is internally consistent:

```text
executable verdict = REGULATED-ACTION-DICTIONARY-WITNESS-PASSED
formal D15 verdict = INCOMPLETE-INVESTIGATION
checks             = 26/26
```

The working theorem integrates the 26-check result and says it closes only a
finite nongravitational S4 instance and conditional environment-decoherence
S5 instance.  It leaves environment state, system/environment split, record
interpretation, continuum, covariance, gravity, dimension, and scales open.

The EFT parameter ledger correctly distinguishes operator-form constraints
from fitted/free coefficients and treats `G` as measured rather than derived
from records.

The UV audit includes all five frozen classes (`EFT4`, `BDQ`, `ASQ`, `SFQ`,
`PRIM`), lists their missing packet fields, treats survival as weaker than
selection, and says its IR coexistence argument is not a theorem that two
complete UV packets share all observations.  It leaves V9 closed.  Its phrase
“fundamental action not uniquely selected by current evidence” is an epistemic
status report, explicitly not the protocol verdict
`FUNDAMENTAL-NONSELECTION-PROVED`.

## 10. Round-1 clean-room opening disposition

| Opening | Round-2 result |
|---|---|
| D14 was hash-only | repaired: D14 types and composition imported/executed |
| direct seal disconnected from CNOT | repaired: exact D14 composition equals direct matrix |
| future record protection outside D14 | repaired: admitted future and overwrite adversary |
| CNOT zeros inserted | repaired: exact `Z2` multiplier sums generate support |
| memory imported from D13 | repaired: local four-bit CNOT construction |
| phase alternative could be frame gauge | repaired: fixed-frame closed probability plus gauge-cancellation control |
| no full receipt | repaired: complete pre-review receipt with both verdict levels |
| finite toy overread as gravity | never promoted; explicit nongravitational ceiling preserved |

## 11. Focused S0–S11 disposition

| Gate | Current clean-room result |
|---|---|
| S0 effective/fundamental scope | pass on explicit finite/EFT/UV separation |
| S1 gravity normal form | ledger/theorem argument retained; not proved by toy |
| S2 matter normal form | conditional on observed fields; not derived by toy |
| S3 coupling/scale ledger | explicit and scoped |
| S4 action-to-D14 dictionary | pass for one finite nongauge witness only |
| S5 autonomous records | conditional; exact supplied-environment decoherence, autonomy open |
| S6 locality/join/no clock | D14 finite composition used; general diagram/join law remains open |
| S7 dimension/cones | assumptions distinguished; no V9 emergence claim |
| S8 empirical selection | EFT evidence ledger, not a new holdout |
| S9 untouched prediction | correctly closed |
| S10 UV audit | incomplete survivors catalogued; no formal nonselection theorem |
| S11 hostile closure | this clean-room stream passes at narrowed scope; full closure pending |

## 12. Final determination

```text
26/26 NORMAL AND -O                      = REPRODUCED
SOURCE/PACKET/SEMANTIC/DEPENDENCIES      = EXACT
ACTUAL D14 IMPORT AND USE                = VERIFIED
ACTION CNOT -> D14 SEAL EQUALITY         = VERIFIED
D14 PROTECTED FUTURE/OVERWRITE CONTROL   = VERIFIED
Z2 MULTIPLIER SUPPORT                    = VERIFIED
LOCAL MEMORY REBUILD                     = VERIFIED
FIXED-FRAME 1 VERSUS 1/2                 = VERIFIED
FRAME-GAUGE CANCELLATION CONTROL         = VERIFIED
FINITE REGULATED DICTIONARY WITNESS      = PASS
GENERALLY COVARIANT/UV/FUNDAMENTAL D15   = STILL INCOMPLETE
ROUND-2 CLEAN-ROOM VERDICT               = PASS AT NARROWED SCOPE
```

No clean-room or reproducibility opening remains against the finite regulated
dictionary witness and its explicit ceiling.

`git diff --check` passed before this review was written.  No primary D15 file
was edited by this referee.

