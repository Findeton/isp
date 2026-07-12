# D14 hostile review, round 2: independent clean-room verification

**Referee:** independent reconstruction/reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **PASS AT THE NARROWED EXECUTABLE-CORE SCOPE**  
**Formal D14 protocol status:** **`INCOMPLETE-INVESTIGATION` pending full hostile closure**

The repaired D14 core is reproducible and the repairs are substantive.  The
authoritative executable passes 42/42 checks under normal and optimized Python
with byte-identical stdout.  Its source, reviewed local dependency, generated
packet, semantic payload, and stdout hashes all match the repair receipt.

Independent adversarial probes now confirm:

- actual constructor rejection of sealed-record overwrite;
- live continuation, ill-typed missing-collar refusal, and zero dead-collar
  continuation amplitude;
- rejection of unentitled joins through both `Signature.declare` and direct
  primitive `Mor` construction;
- rejection also when the only two owned inputs are protected sealed records;
- persistent protected-record correspondence through composition, tensor,
  fresh-record insertion, and symmetry;
- rejection of record-owner reassignment;
- sequential local production of the depth-1–3 protected history strings;
- equality of those local cylinder weights with the class-operator weights;
- projectivity of both the measurement history and the integrated memory
  packet;
- exact visible non-Markov support `000/101` with weights `1/2,1/2`;
- completeness of the hidden-memory reset and its change of both relevant
  post-reset conditionals to zero.

The claim manifest is also repaired.  The packet proves only
`FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED`.  The theorem and
paper explicitly begin with supplied kernels, boundary state, instruments,
protected algebra, signature, and units.  They call contraction order an
evaluation-schedule gauge for a supplied DAG, leave diagram generation and
weights open, withhold all V9 holdouts, and state that the action-level result
can be at most `BRIDGE-CONDITIONAL`.  No positive full-protocol verdict is
printed before B12.

I found no remaining clean-room or reproducibility opening that weakens this
narrowed finite core.  This PASS does not itself finish B12; the mathematics
and ontology/locality streams must independently close at the same scope.

## 1. Authoritative reproduction

### Commands

From `/Users/felixrobles/workspace/isp`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d14_action_record_bridge_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d14_action_record_bridge_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d14_action_record_bridge_exact.py | shasum -a 256
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d14_action_record_bridge_exact.py | shasum -a 256
shasum -a 256 v10/code/d14_action_record_bridge_exact.py
shasum -a 256 v10/code/d13_finite_kernel_no_go_exact.py
shasum -a 256 v10/data/d14-action-record-bridge-exact.json
```

Both direct executions completed successfully with the same 42 labeled
checks, ending in:

```text
PASS 042: pre-final exact check count is frozen
CHECKS PASSED: 42/42
SEMANTIC SHA256: a8b22100a104b04069734bd563a8a3f1411e7772dafa1d0062baf019859658c7
SOURCE SHA256: e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
DEPENDENCY SHA256: 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
EXECUTABLE VERDICT: FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED
```

The complete stdout hashes are byte-identical:

```text
normal  a7c840c55373bb4fc84530c8cd47f48d4ebbaed545581fb784096ef4b01ce830
-O      a7c840c55373bb4fc84530c8cd47f48d4ebbaed545581fb784096ef4b01ce830
```

Current authoritative file hashes are:

```text
e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425  D14 source
1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45  D13 exact dependency
37f411d53d0b93313bac1066be71fc7450a92a5b90225c4ad14f17a177397663  generated D14 packet
```

I independently selected the seven semantic fields from the generated packet,
serialized them with sorted compact JSON, and obtained:

```text
a8b22100a104b04069734bd563a8a3f1411e7772dafa1d0062baf019859658c7
```

Every executable hash in `d14-round1-repair-receipt.md` therefore matches the
current bytes and independent execution.

## 2. Optimization, dependencies, and packet provenance

The D14 gate path contains no Python `assert`, no `__debug__` branch, and no
optimization-sensitive result.  `check` uses an explicit conditional and
raises `AssertionError`; the check-count and semantic-hash gates are ordinary
conditionals.  The normal/`-O` identity is therefore both explained and
observed.

The only non-stdlib import is the declared sibling
`d13_finite_kernel_no_go_exact.py`, whose exact reviewed hash is checked.  It
uses only the standard library.  No external package, network resource,
random seed, wall clock, locale, or floating-point precision enters.

The executable writes its JSON only after all exact gates and the semantic
hash pass.  No proof check reads that packet.  The regenerated packet is
byte-identical to the frozen file, so the receipt is not self-authenticated by
its own output.

The round-1 review-provenance hashes also match current immutable bytes:

```text
7cdec33e8a3be93d48e53c9328c060ac6bd77109af41052f08932e3288663dce  mathematics
dc5626c0d2d7c963b53e5cc21e1ed985b871511908cf44e28e10d6063419bb65  ontology/locality
6961525d51f028d64f01f1db1c07c70d97f1249895ad05d3eb9b1158e14c0fd3  clean-room rebuild
```

## 3. Independent adversarial packet

I ran a separate scratch driver against the public repaired API:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/d14_round2_adversarial_probes.py
```

It reported:

```text
overwrite REJECTED protected record overwrite
missing collar REJECTED ill-typed boundary gluing
dead collar zero True
unowned signature join REJECTED multi-component generator lacks a connected join entitlement
entitled join admitted True
raw Mor unowned join REJECTED multi-component generator lacks a connected join entitlement
sequential records equal direct cylinders True
sequential projectivity True
integrated memory projectivity True
integrated support {(0,0,0): 1/2, (1,0,1): 1/2}
reset complete True
reset conditionals 0 0
fresh-record tensor old-record identity ADMITTED ((1,2),)
sealed-wire symmetry roundtrip True ((0,0),(1,1))
record owner reassignment REJECTED protected record identity/type mismatch
two-owner sealed-record primitive join REJECTED multi-component generator lacks a connected join entitlement
sealed-record join entitlement bypass False
closure regression False
ROUND2 PROBES COMPLETE
```

These probes are not aliases for the printed check labels.  They construct
fresh maps, including the exact edge cases that defeated the earlier versions.

## 4. Protected-record category repair

The original ordinal `zip(source_sealed,target_sealed)` rule has been replaced
by explicit source-to-target protected correspondences.  Port identity now
includes kind, dimension, sealed status, owner, and optional record identity.
A `Mor` carries its protected correspondence; composition composes it, tensor
takes the disjoint union with offsets, and symmetry explicitly transports each
wire to its permuted target position.

This closes the previously missed case:

```text
f : q -> q tensor fresh-record
g : old-record -> old-record
f tensor g
```

The tensor is admitted with the old source record mapped to the old target
record rather than mistakenly to the new left-factor record.  Protected
symmetry followed by its inverse returns the exact identity matrix and identity
correspondence.  A target that changes an old record's owner is rejected.

The constructor still tests every nonzero matrix entry against the declared
correspondence, so a basis-label flip raises rather than merely receiving a
false diagnostic.  This establishes the executed identity/composition/tensor/
symmetry closure needed at the finite image scope.

## 5. Primitive join admission

Primitive admission now counts owners on **all** source ports, including
sealed read-only records.  Consequently all of the following are exact:

- two live owners without entitlement: rejected through `Signature`;
- the same direct raw primitive `Mor`: rejected;
- exact entitlement `("A","B")`: admitted;
- mixed owned/ownerless source input: rejected;
- two owned sealed records preserved while emitting a joint live output:
  rejected without entitlement.

This repairs the executable bypass.  It does not derive where a physical join
entitlement comes from; the theorem and paper retain that as a primitive/open
law.  Thus the result is conditional admission, not a solution to first
component joining.

## 6. Collar, records, and sequential histories

The declared continuation consumes the system, protected record, and collar.
It composes after the live seal.  Removing the collar changes the object and
makes composition ill-typed; the dead collar basis vector is sent to the zero
amplitude.  This proves the frozen declared-gate control, not that every
conceivable future physics must use that collar.

Sequential local seal isometries now accumulate one fresh protected bit after
each supplied unitary.  For every history through depth 3, independent branch
norms from that network equal the direct class-operator cylinder exactly.
The record-extended off-diagonals vanish, all depth distributions normalize,
all depth-1/2 parent cylinders equal the sum of their children, and the frozen
conditional is exactly `1/2`.

Paper 15 correctly distinguishes the possibly nondiagonal bare functional
`D_0` from the diagonal record-extended functional `D_R`.  The positivity
predicate now requires zero imaginary and quadratic components and a
nonnegative rational coefficient, closing the weak-check opening.

## 7. Integrated memory and deletion

One typed packet now performs the memory storage, seals X, seals Y, reveals M
into Z, and seals Z.  Its only nonzero visible histories are:

```text
P(000)=1/2,
P(101)=1/2.
```

The same packet's depth-1–3 cylinder tables are projective.  Therefore the
non-Markov conditionals and projectivity no longer come from unrelated
examples.

The two reset Kraus operators satisfy exact completeness.  Resetting M before
the final copy changes the `x=1` visible continuation and yields

```text
P_reset(z=1|y=0,x=0)=0,
P_reset(z=1|y=0,x=1)=0.
```

The paper limits this to one finite compatibility example and does not infer
bounded memory for every full-history law.

## 8. Claim and status manifest

The theorem-note title and Paper 15 title now say regional amplitudes and
instruments to recorded histories.  Both primary documents are marked
“repaired after hostile round 2; awaiting focused closure.”  The repair
receipt says `INCOMPLETE-INVESTIGATION, pending focused closure`.

The current hierarchy is consistent:

```text
executable core = FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED
action-level ceiling after hostile closure = BRIDGE-CONDITIONAL
current formal protocol status = INCOMPLETE-INVESTIGATION
```

The manuscripts explicitly leave primitive:

```text
signature and diagram-generation law;
regional kernels and any action-to-kernel map;
boundary state;
record instrument and protected algebra;
join-entitlement origin;
units and gravitational scale.
```

They restrict order gauge to contraction/evaluation of a supplied DAG, do not
claim a locally generated universe history, and license no cone, dimension, or
other V9 holdout.  The legacy filesystem names still contain `action-record`
or `from-action-to-records`; the current titles, statuses, semantic verdict,
and receipt remove the scientific ambiguity.  A final manifest may note that
the filenames are retained for provenance.

## 9. Round-1 opening disposition

| Opening | Round-2 clean-room result |
|---|---|
| overwrite only diagnosed | repaired: constructor raises |
| arbitrary block map called permanent | repaired in theorem by branchwise completeness/TP hypothesis |
| missing/dead collar absent | repaired for declared continuation |
| unowned live join | repaired in Signature and direct primitive admission |
| unowned sealed-record join | repaired and exact regression added |
| global history record appended afterward | repaired by sequential local isometries |
| projectivity/memory split | repaired in one integrated packet |
| deletion control absent | repaired with complete reset channel |
| weak positivity/conditional tests | repaired exactly |
| construction order overread | narrowed to supplied-DAG evaluation schedule |
| action-to-record overclaim | narrowed to regional amplitudes/instruments core |
| bare/record decoherence conflated | repaired as `D_0` versus `D_R` |
| arbitrary full-history memory overread | narrowed to finite compatibility |
| no-signalling overread | narrowed to one unitary Bell marginal/interchange cell |
| Lorentz overread | narrowed to one positive-cone pairing cell |
| premature B12 verdict | repaired: core verdict only; protocol still incomplete |
| protected tensor/symmetry closure | repaired by explicit persistent correspondence |
| record owner reassignment | rejected |

## 10. B0–B12 focused disposition

| Gate | Independent result |
|---|---|
| B0 typed/admitted source | pass at supplied finite scope |
| B1 category/coherence | pass: abstract free-SMC proof plus exact protected image cells |
| B2 order gauge | pass as evaluation schedule for one supplied DAG |
| B3 coherent gluing | pass |
| B4 frame/pairing | pass at stated finite cells |
| B5 records/birth | pass conditional on supplied instrument/algebra/grammar |
| B6 recorded decoherence | pass with sequential local records |
| B7 projectivity | pass at depths 1–3 plus completeness induction |
| B8 visible memory | pass for one finite integrated packet and reset control |
| B9 locality/no-signalling | pass at one finite unitary witness scope |
| B10 primitive/action scope | pass after narrowing |
| B11 downstream handoff | explicit; geometry holdouts withheld |
| B12 hostile closure | this stream passes; full multi-stream closure still pending |

## 11. Final verdict

```text
42/42 NORMAL AND -O                      = REPRODUCED
SOURCE/DEPENDENCY/PACKET/SEMANTIC/STDOUT = EXACT
OVERWRITE/COLLAR/JOIN CONTROLS           = PASS
PROTECTED TENSOR/SYMMETRY/OWNER GATES    = PASS
SEQUENTIAL RECORDS/DECOHERENCE           = PASS
PROJECTIVITY/INTEGRATED MEMORY/RESET      = PASS
CORE CLAIM MANIFEST                       = NARROWED AND CONSISTENT
INDEPENDENT ROUND-2 VERDICT               = PASS AT EXECUTABLE-CORE SCOPE
FORMAL D14 PROTOCOL                       = INCOMPLETE PENDING ALL B12 STREAMS
```

No clean-room opening remains that weakens the finite regional-amplitude and
supplied-instrument to recorded-history core at its declared scope.

`git diff --check` passed before this review was written.  No primary D14 file
was edited by this referee.

