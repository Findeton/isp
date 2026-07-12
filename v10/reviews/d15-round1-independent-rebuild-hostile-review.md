# D15 hostile review, round 1: independent rebuild and reproducibility

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Exact finite toy witness:** **REPRODUCED AT ITS NONGRAVITATIONAL SCOPE**

The 22-check executable is exactly reproducible.  Normal and optimized Python
produce byte-identical stdout; source, generated packet, semantic object, and
both local source-dependency hashes agree with current bytes.  A separate
standard-library reconstruction confirms the Hadamard action/path sum, CNOT
seal, exact environment decoherence, Bell marginals and no-signalling cell,
record persistence, memory output indices `0` and `13`, and the existence of a
different unitary phase-composed kernel.

The executable nevertheless does not yet pass the frozen D15 protocol.  Its
D14 “dependency” is only a hash-read: D14 is never imported or used.  No D14
typed object, admitted `Mor`, ownership/join entitlement, protected
correspondence, or sequential history is constructed.  The seal is hardcoded
independently of the computed CNOT matrix, and the memory unitary is imported
from D13 rather than composed from D15's CNOT action.  Thus the exact cells do
not yet form the promised action-to-D14 dictionary.

The final nonselection check is also too weak.  `alternative = phase * H` is
merely unequal to `H`; it is exactly an output-unitary transformation of the
form D14 treats as boundary-frame covariance.  No fixed-frame closed
observable, gauge-invariant inequivalence, or pair of UV-compatible complete
packets is tested.  It cannot support S10 or `FUNDAMENTAL-NONSELECTION-PROVED`.

Most importantly, the exact witness is a finite `Z2`/qubit circuit with no
spacetime, diffeomorphism symmetry, metric, gravity, continuum limit, physical
unit bridge, or empirical fit.  Its source and JSON say this honestly.  It
cannot establish the protocol's generally covariant low-energy action packet.
The working theorem remains a literature-based provisional EFT normal-form
argument, not an executable generally covariant completion.

## 1. Exact reproduction

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

Both direct executions completed successfully with the same 22 labels and
ended in:

```text
PASS 022: pre-final exact check count is frozen
CHECKS PASSED: 22/22
SEMANTIC SHA256: f3b02e21a208a90d4c77215cae744bae249e903d11f87e197c23972635a104e6
SOURCE SHA256: 9d9fac31730d1c02ed7cc5694d28b50f8b9277b6da8bea1ce199a2f72b81f47c
VERDICT: REGULATED-ACTION-DICTIONARY-WITNESS-PASSED
```

The complete stdout hashes are byte-identical:

```text
normal  ba3a9a9f29a4722bb73f7e94f181ce1b9aefa38b605406e0bccca50173786591
-O      ba3a9a9f29a4722bb73f7e94f181ce1b9aefa38b605406e0bccca50173786591
```

Current file hashes are:

```text
9d9fac31730d1c02ed7cc5694d28b50f8b9277b6da8bea1ce199a2f72b81f47c  D15 source
1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45  D13 arithmetic source
e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425  D14 bridge source
b10bd2ce0772f658438aad91b714cf1804b0142800f96a8eedd76872b33d16f2  D15 generated packet
```

I independently selected the six semantic fields from the JSON and serialized
them using the source's sorted compact JSON convention.  The result was:

```text
f3b02e21a208a90d4c77215cae744bae249e903d11f87e197c23972635a104e6
```

Thus every requested current source/dependency/packet/semantic/stdout value is
verified, even though no separate D15 receipt presently freezes all of them.

## 2. Optimization, dependencies, and output provenance

The D15 source contains no Python `assert`, `__debug__` branch, random input,
floating arithmetic, or optimization-dependent gate.  `check` uses an
explicit conditional and raises; the count and semantic-hash guards are also
ordinary conditionals.  Normal/`-O` identity is real.

D13 is an actual runtime dependency: D15 imports its exact quadratic/complex
arithmetic and matrix operations.  D14 is not.  The source names a D14 path,
hashes its bytes, and compares the digest, but never imports a D14 symbol or
constructs a D14 object.  Check 2 therefore proves only that a neighboring
file has expected bytes; it supplies no semantic dependency or bridge
integration.

The program writes its JSON only after all checks and the semantic digest
pass, and no check reads the output packet.  The packet is not used to prove
itself.  The source digest in the packet is current but is not an internal
frozen source gate; the external audit above is what verifies it.

No D15 pre-review receipt currently records the full stdout/source/packet
manifest.  The code freezes check count, semantic digest, and dependency
digests, while the packet records current source/dependencies.  A repair
receipt should freeze the complete command/output manifest before round 2.

## 3. Independent exact reconstruction

I wrote an independent scratch implementation using only `dataclasses` and
`fractions.Fraction`.  It implements `Q(sqrt(2))`, matrix multiplication,
partial traces, the CNOT truth table, the seal embedding, system-only future
dynamics, and the two-CNOT memory permutation.  It does not import D13, D14,
or D15.

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/d15_cleanroom_rebuild.py
```

### H action and path sum

For

```text
K(b,a)=2^(-1/2)(-1)^(ab),
```

the independent matrix is exactly Hadamard.  It obtains:

```text
K K = I,
sum_k K(0,k)K(k,0) = 1,
sum_k K(1,k)K(k,0) = 0.
```

The regulated local phase and one-use normalization therefore reproduce the
constructive/destructive internal-boundary sum exactly.

### CNOT seal and environment decoherence

With fresh record bit `0`, CNOT `S -> R`, and appended collar bit `1`, only
seal rows `1` and `7` are nonzero.  For input `|+>` their amplitudes are both
`1/sqrt(2)`, so the record masses are exactly `(1/2,1/2)` and every dead-collar
component is zero.

Removing the collar leaves the system-record Bell state

```text
(|00>+|11>)/sqrt(2).
```

Tracing either carrier gives `I/2`.  Hence the exact Z-pointer decoherence
claim reconstructs.

### Bell correlation and no-signalling

`CNOT(H tensor I)|00>` gives the same Bell vector.  Its two local reduced
states are `I/2` and its same-basis correlation has probability one.  Applying
H on the first subsystem yields amplitudes `(1,1,1,-1)/2`; tracing the first
subsystem still gives `I/2` on the second.  The finite no-signalling cell is
correct.

The manuscript/executable phrase “Bell record” should remain a correlation
label: no protected record register is added in that particular Bell cell.

### Record persistence and interference

Applying H only to the system factor of the sealed `S,R,C` state leaves the
record masses exactly `(1/2,1/2)`.  The later system-zero probability is
`1/2`, whereas coherent `H H|0>` gives system-zero probability one.  This
confirms both the one-map persistence cell and the recorded/coherent
interference difference.

### Memory indices

For bits ordered `X,M,Y,Z`, the two reversible operations are

```text
M <- M xor X,
Z <- Z xor M.
```

They send `0000 -> 0000` and `1000 -> 1101`.  Row-major binary indices are
therefore exactly `0` and `13`, with mass `1/2` on each.  The printed index
claim is correct.

### Alternative phase kernel

`P=diag(1,i)` gives `P H != H` and remains unitary.  This establishes only
that a different unitary matrix can be written; it does not yet establish a
physically inequivalent action after D14 boundary-frame quotienting or an S10
UV survivor.

## 4. Major opening R1: the action dictionary never enters D14

**Severity:** major for S4 and S6.  
**Status:** open.

The frozen S4 gate requires one regulated action example whose boundary
kernel, gluing, state, and local record instrument enter the **repaired D14
bridge**.  The D15 program only checks D14's file hash.  It does not import or
use:

```text
Port / Obj / Signature / Mor;
protected record correspondence;
owner and join-entitlement admission;
live/dead collar continuation;
sequential protected history construction;
D14 projectivity or memory packet.
```

D15 instead implements parallel local matrix helpers.  Consequently a change
that preserved D14's source hash expectation but made the D15 matrices
incompatible with its API would not be detected semantically.

**Required repair:** import the reviewed D14 module and instantiate the toy as
an admitted typed signature.  Give the boundary/system/environment/collar
ports owners and persistent record identities; admit the H and CNOT
generators; build the seal and later history from those generators; execute
the protected/missing/dead-collar and entitlement rules; and compare D14's
cylinder table with the direct action path sum.  The D14 hash should remain a
provenance guard, not stand in for integration.

## 5. Major opening R2: the seal and memory are parallel hardcodings

**Severity:** major for the claimed construction chain.  
**Status:** open.

`seal_from_cnot_with_live()` directly writes the two nonzero rows.  It does not
take `cnot_action_kernel()` as an argument or contract the computed CNOT with
the supplied `|0>` environment and `|live>` collar.  The result is correct,
as the clean-room derivation confirms, but the executable would not notice if
the action-derived CNOT and hardcoded seal diverged.

Likewise, the memory cell calls D13's `memory_copy_unitary()` rather than
composing D15's `cnot_action_kernel()` on the declared four-bit factors.  Its
label “local CNOT action gives” is mathematically true but not linked in code.

**Required repair:** construct both objects from the actual `cnot` variable,
using explicit ancilla embeddings, tensor placement, and composition.  Assert
equality with any optimized closed form.  Then the semantic chain

```text
action weights -> CNOT kernel -> seal/memory -> records
```

will be load-bearing rather than duplicated.

## 6. Major opening R3: alternative matrix is not action nonselection

**Severity:** major if used for S10 or fundamental nonselection; moderate for
the narrow toy label.  
**Status:** open.

The final check establishes only:

```text
P H is unitary,
P H != H,
P = diag(1,i).
```

But D14 explicitly treats

```text
K -> G_out K G_in^dagger
```

as boundary-frame covariance.  `P H` has exactly this form with
`G_out=P`, `G_in=I`.  Matrix inequality is therefore not a certificate of
physical/action inequivalence.  The check also gives no explicit second
regulated action functional, no same-boundary closed observable, and no pair
of complete UV packets sharing all established low-energy evidence.

The executable verdict does not claim `FUNDAMENTAL-NONSELECTION-PROVED`, which
is correct.  The check label should be narrowed or strengthened.

**Required repair:** either call this a different representative before frame
quotient, or construct two fixed-frame action kernels with a gauge-invariant
closed probability difference.  For S10, exhibit two inequivalent complete or
UV-compatible packets agreeing on every frozen established constraint, not
merely two unitary matrices.

## 7. Scope opening R4: finite qubits are not generally covariant gravity

**Severity:** fatal to any complete D15/general-covariance verdict; not a flaw
in the finite witness.  
**Status:** explicitly open in source, JSON, and working theorem.

The exact arena contains:

```text
two-level boundary labels;
finite H/CNOT/phase matrices;
one supplied environment qubit and pointer basis;
one supplied live-collar bit;
no spacetime, metric, diffeomorphism group, gravitational field, or units.
```

It therefore cannot establish:

```text
Einstein-Hilbert normal-form uniqueness;
the Standard Model operator basis;
gauge fixing, ghosts, constraints, edge modes, or anomalies;
a generally covariant boundary/gluing measure;
3+1 dimension or Lorentzian signature;
G, Lambda, metres, seconds, or a continuum limit;
an influence/cone prediction or V9 holdout.
```

The source docstring and semantic ceiling correctly refuse those promotions.
That refusal must dominate every headline.  The literature-based EFT normal
form in `note-d15-maximal-low-energy-action.md` is a provisional synthesis,
not a result proved by the 22-check receipt.

## 8. Records remain conditional, not autonomous

The toy derives exact decoherence once the following are supplied:

```text
system/environment split;
environment initial state |0>;
CNOT coupling and its computational basis;
one live-collar convention;
later system-only future algebra.
```

That is a useful regulated dictionary cell.  It does not derive the split,
initial state, pointer basis, redundancy, stability tolerance, coarse-graining
scale, or why the environment coupling is nature's interaction.  S5 remains
`ACTION-BRIDGE-CONDITIONAL`, matching the working theorem's prose.

## 9. S0–S11 protocol audit

| Gate | Current evidence | Round-1 disposition |
|---|---|---|
| S0 scope | toy JSON says finite/nongravitational; EFT note states inputs/domain | partial/pass on honesty |
| S1 gravity normal form | literature argument only; no exact generally covariant construction | incomplete |
| S2 matter normal form | conditional prose given observed group/representations | incomplete as D15 derivation |
| S3 coupling/scale ledger | explicit and appropriately labels measured/free quantities | pass as ledger |
| S4 action-to-D14 dictionary | finite action cells exist, but D14 is unused and gauge/boundary structure absent | **fail/incomplete** |
| S5 autonomous records | exact toy decoherence after supplied split/state/basis; autonomy not derived | conditional/incomplete |
| S6 locality/join/no clock | disjoint commute only; no D14 ownership or entitlement packet | **incomplete** |
| S7 3+1/cones/influence | EFT assumes 3+1/metric cone and withholds emergence/V9 claims | honest but no prediction |
| S8 empirical selection | narrative source ledger; no frozen fit/model-selection calculation in this packet | incomplete |
| S9 untouched prediction | no candidate-ready prediction; holdout correctly closed | pass as refusal |
| S10 UV survivor audit | candidate list plus unequal frame-related matrix; no complete survivor pair | incomplete |
| S11 hostile closure | round 1 begins here; openings remain | incomplete |

Under the frozen verdict table, the only formal D15 disposition currently
licensed is:

```text
INCOMPLETE-INVESTIGATION.
```

The internal finite executable verdict may remain
`REGULATED-ACTION-DICTIONARY-WITNESS-PASSED` if “dictionary witness” is read as
the small nongravitational construction, not as S0–S11 completion.

## 10. Claim and artifact manifest

The protocol is correctly marked frozen before D15 outcome work.  The theorem
is correctly marked a derivation draft and calls its verdict provisional.  Its
new section 10 now integrates the first regulated toy result, records 22/22,
and explicitly limits it to a finite nongravitational S4/S5 instance.  It also
inherits the two executable overreads identified above: appending a collar is
said to make the map fit D14 although no D14 API object is constructed, and an
unequal phase-modified matrix is said to prove nonselection without first
quotienting boundary frames or exhibiting a closed invariant difference.

There is no D15 pre-review/final receipt file recording the full current
source, dependency, packet, semantic, and stdout hashes.  Nor is D15 yet
entered in V10 `PLAN.md` or `LOG.md`.  Before round 2, add a repair receipt and
update the working theorem to adjudicate what the toy closes and what it does
not.

The filename `note-d15-maximal-low-energy-action.md` is potentially stronger
than the current gate state, but its title/body consistently use “current
evidence,” “normal form,” and “provisional.”  The substantive risk is not the
filename; it is conflating the finite witness with the generally covariant EFT
argument.  Keep them explicitly separate.

## 11. Opening ledger and required next round

| ID | Severity | Opening | Required repair |
|---|---:|---|---|
| R1 | major | D14 hash is unused semantically | construct the action packet through actual D14 typed/admitted APIs |
| R2 | major | seal and memory are parallel hardcodings | derive both from the computed CNOT matrix |
| R3 | major for S10 | `P H != H` may be boundary-frame gauge | add fixed-frame invariant observable or withdraw nonselection reading |
| R4 | fatal to completion | finite toy has no general covariance/gravity | preserve nongrav ceiling; separate EFT proof packet required |
| R5 | major | autonomous record instrument not derived | keep bridge conditional or derive split/state/pointer/stability |
| R6 | major | S6 ownership/join grammar absent | use D14 owner/entitlement/collar admission explicitly |
| R7 | major | S10 complete UV survivor pair absent | construct/audit complete compatible rivals before fundamental nonselection |
| R8 | moderate | no frozen D15 receipt/PLAN/LOG handoff | add complete manifest and scope disposition |

## 12. Final determination

```text
22/22 NORMAL AND -O                      = REPRODUCED
SOURCE/PACKET/SEMANTIC/DEPENDENCY HASHES = VERIFIED
H ACTION AND INTERNAL PATH SUM           = INDEPENDENTLY REBUILT
CNOT SEAL/DECOHERENCE                     = INDEPENDENTLY REBUILT
BELL/NO-SIGNALLING                        = INDEPENDENTLY REBUILT
RECORD PERSISTENCE                        = INDEPENDENTLY REBUILT
MEMORY INDICES 0/13                      = INDEPENDENTLY REBUILT
FINITE NONGRAVITATIONAL TOY              = PASS
ACTION -> ACTUAL D14 PACKET               = NOT YET CONSTRUCTED
GENERALLY COVARIANT EFT/GRAVITY PACKET    = NOT PROVED BY RECEIPT
FUNDAMENTAL ACTION NONSELECTION           = NOT PROVED
ROUND-1 D15 VERDICT                       = MAJOR REVISION
FORMAL PROTOCOL STATUS                    = INCOMPLETE-INVESTIGATION
```

`git diff --check` passed before this review was written.  No primary D15 file
was edited by this referee.
