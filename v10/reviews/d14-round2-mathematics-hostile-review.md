# D14 hostile round-2 mathematics/category/decoherence review

**Date:** 2026-07-11  
**Reviewer:** independent mathematics/category/decoherence referee  
**Verdict:** **MAJOR REVISION — ONE GENERIC CATEGORY BLOCKER REMAINS**  
**Current protocol status:** `INCOMPLETE-INVESTIGATION`  
**Eventual honest ceiling after closure:** `BRIDGE-CONDITIONAL`

## Decision first

The repaired 39-check receipt closes nearly all round-one openings.  Protected
overwrite now raises in the constructor; the theorem correctly requires
branchwise isometric/CPTP future dynamics; live, absent, and dead collar cases
are distinguished; local sequential record isometries reproduce every
depth-one through depth-three class-operator cylinder; the record-extended
decoherence functional is explicit; the finite-memory packet is projective and
non-Markov; and a complete reset channel removes its memory dependence.

One structural blocker remains.  `Mor.__post_init__` associates old protected
ports with output protected ports by **occurrence order**.  This rule is not
closed under the symmetric-monoidal tensor and symmetry operations.  I
constructed two morphisms that are each admitted; their tensor is rejected.
A valid symmetry exchanging two protected wires is also rejected.  Therefore
the implemented protected morphisms do not form the claimed symmetric-
monoidal class, and the executed “closure” cell is not generic.

This is not a numerical defect and does not invalidate the unprotected free-
SMC evaluation theorem.  It blocks B0/B1/B5 and therefore blocks round-two
PASS.  A persistent source-to-target record-identity map fixes it cleanly.

The proposed `BRIDGE-CONDITIONAL` grade is the correct **ceiling** once this
category defect and hostile closure are repaired: regional matrices and record
instruments remain supplied rather than derived from a physical action.

## Frozen artifacts and reproduction

```text
abf7e4d2e4638e4a8f4e545e9a21fe77cb5dbfceb86eb7ef366a8b0d165b514d  code/d14_action_record_bridge_exact.py
70f552bf3f9d962029d1a48dff20159f170a8e10f971c15e9ef54bdb5865ab22  data/d14-action-record-bridge-exact.json
ba37f5909f4e8d556df4b654f9bd2496001deaf74f1247ff3171091509c6feb7  note-d14-finite-action-record-bridge-theorem.md
09f35a312f379e607654089d70f69ba01f88073671fd5d51371399f84925a610  relativistic-isp-v10-paper15-from-action-to-records-without-a-global-clock.md
ac11a65c738b0a822d4f1e9b908f6036a93ca3b3fb70605a73b17134608b64f4  reviews/d14-hostile-round1-opening-ledger.md
c1a07de0b1ccb6d6ff8c6f053d34e017669627163f189dd914d52a39b98d1a86  data/d14-round1-repair-receipt.md
```

Normal and optimized execution reproduced byte-identically:

```text
checks                         = 39/39
stdout SHA-256 normal/-O       = 99e51861cf472bdfea9dad570e7a6663d112b5704425db80609eaa65aceea20b
semantic SHA-256               = 6bead748846c5b33995212ac03576e30c2ed17e6689570a4e1c4119072637ea3
source SHA-256                 = abf7e4d2e4638e4a8f4e545e9a21fe77cb5dbfceb86eb7ef366a8b0d165b514d
D13 dependency SHA-256         = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
generated JSON SHA-256         = 70f552bf3f9d962029d1a48dff20159f170a8e10f971c15e9ef54bdb5865ab22
```

All 39 printed checks are true.  The remaining finding is outside the narrow
closure example selected by check 24.

## Round-one opening dispositions

```text
M1 branchwise probability preservation        CLOSED IN THEOREM HYPOTHESES
M2 overwrite enforcement                       CLOSED FOR FIXED POSITIONAL PORTS;
                                                GENERIC IDENTITY/CLOSURE STILL OPEN
M3 absent/dead collar controls                  CLOSED
M4 memory deletion control                      CLOSED
M5 bare versus record-extended D notation       CLOSED
M6 code/image versus syntactic free source      CLOSED BY EXPLICIT SCOPE
M7 local sequential record realization          SUBSTANTIALLY CLOSED;
                                                LIVE COLLARS REMAIN A SEPARATE CELL
M8 exact positivity predicate                   CLOSED
M9 premature positive protocol verdict          CLOSED; CURRENT STATUS INCOMPLETE

new C1 generic protected tensor/symmetry closure MAJOR BLOCKER
```

## 1. Generic protected-record enforcement

### What was repaired correctly

Every `Mor` now checks dimensions and inspects nonzero matrix entries.  If a
source has protected ports, it requires at least as many protected output ports
and verifies that the source label equals the corresponding output label.
The explicit record-flip matrix now raises `ValueError`; it is no longer merely
constructed and diagnosed afterward.

Sequential record appends work because each new protected port is appended
after all old protected ports.  Composition with the tested future system
unitary and tensoring that unitary with an unprotected identity also work.

### Remaining blocker C1 — occurrence-order matching is not monoidal

The constructor defines

```python
source_sealed = sealed source positions
target_sealed = sealed target positions
for source_pos, target_pos in zip(source_sealed, target_sealed): ...
```

Thus the first old sealed port is assumed to map to the first target sealed
port, the second old port to the second target sealed port, and so on.  That
assumption fails when a morphism creates a fresh record before another tensor
factor's existing record.

I executed the following clean counterexample against the frozen source:

1. `f` has source `q tensor A_record` and appends `fresh_record`.  It is
   admitted.
2. `g=id[B_record]`.  It is admitted.
3. The source of `f tensor g` has old sealed order `(A,B)`.
4. Its target has sealed order `(A,fresh,B)`.
5. Positional zip incorrectly pairs old `B` with `fresh`, so the constructor
   raises `protected record identity/type mismatch`.

Exact output:

```text
f admitted
g admitted
tensor rejected: ValueError protected record identity/type mismatch
```

Therefore two admitted protected morphisms are not closed under tensor.

The symmetry problem is even more direct.  For distinct protected port types
`A_record` and `B_record`, the valid free-SMC symmetry

$$
\sigma_{A,B}:A\otimes B\longrightarrow B\otimes A
$$

is rejected by the same occurrence-order comparison:

```text
sealed swap rejected: ValueError protected record identity/type mismatch
```

If the record types are identical, the type comparison no longer catches the
error, but positional label comparison rejects generic unequal record values.
Thus the implementation cannot generally permute protected wires at all.

This contradicts generic symmetric-monoidal closure.  Check 24 exercises only

```text
future o identity
future tensor unprotected identity
```

where no new protected port changes occurrence order.  It cannot certify the
general claim.

### Exact repair requirement

Protected identity must be explicit data, not inferred from position.  Add to
each morphism an injective correspondence

```text
old protected port ID -> target protected port ID/position
```

and use it when validating nonzero entries.  Then:

- identity carries the identity correspondence;
- append preserves every old ID and creates one new ID;
- composition composes the correspondences;
- tensor takes their disjoint union with index offsets;
- symmetry transports IDs by the declared wire permutation;
- type/owner compatibility is checked along that map.

Prove and test identity, composition, tensor, and symmetry closure.  At minimum
add the two counterexamples above as must-pass gates.  The existing `owner`
field is not used in the protected correspondence and does not repair this
problem.

Until then the protected executable is a valid append-ordered sublanguage, not
the protected symmetric-monoidal category claimed by B0/B1.

## 2. Branchwise isometry/CPTP scope

**The round-one mathematical error is repaired in prose.**

The theorem now requires, at Kraus level,

$$
M_k=\sum_r |r\rangle\langle r|_R\otimes M_{r,k},
\qquad
\sum_k M_{r,k}^\dagger M_{r,k}=I
\quad\text{for every }r.
$$

This condition preserves the unconditional old-record marginal.  The paper
correctly distinguishes postselected inference about an old label from
physical overwrite and explicitly says arbitrary block-diagonal linear maps
do not suffice.

The pure-matrix `Mor` constructor enforces only label preservation, not
isometry or Kraus completeness.  That is acceptable only because the theorem
treats branchwise isometry/CPTP completeness as a supplied licensed-algebra
hypothesis and the exact future morphism is unitary.  Do not describe every
constructor-admitted `Mor` as unconditional physical future dynamics.  A
future implementation should separate:

```text
label-preserving amplitude morphisms
from
licensed unconditional isometries/CPTP instruments.
```

This conditionality is one reason `BRIDGE-CONDITIONAL`, rather than the frozen
positive bridge verdict, is the correct action-level ceiling.

## 3. Sequential local records and decoherence equality

**Closed mathematically.**

`local_record_history_network` now alternates:

```text
system evolution U tensor identity_on_old_records
local copying of the current system pointer into one fresh protected record.
```

For depths one through three, the receipt evaluates this network from the
initial `|+>` state, projects by each protected record string, and compares the
resulting norm with

$$
p(\alpha)=\operatorname{Tr}
(C_\alpha\rho C_\alpha^\dagger).
$$

The dictionaries agree exactly.  Distinct protected strings are orthogonal, so
the explicitly computed record-extended functional is

$$
D_R(\alpha,\beta)
=\delta_{\alpha\beta}p(\alpha).
$$

The repaired theorem separately defines the bare system functional `D_0`,
which need not be diagonal.  That resolves the round-one notation problem.

The exact positivity predicate now requires zero imaginary and quadratic
components and nonnegative rational part.  The selected cylinder conditional
is frozen at `1/2`, not merely tested to lie in `[0,1]`.

### Residual integration note

The sequential history generators append protected record bits but do not emit
or consume a live-collar port at each step.  Collar birth/eligibility is proved
in a separate four-level seal cell.  This satisfies the literal frozen B5
requirement that at least one generator emit a live collar, but it does not yet
show that the depth-three history network's continuation is mediated by those
collars.

Keep the theorem wording at “sequential local record isometries” rather than
claiming that the integrated history packet itself implements the complete
collar opportunity grammar.  A stronger integrated claim would require adding
a live collar to each history step and consuming it in the next generator.

## 4. Projectivity and the integrated memory packet

**Closed at finite witness scope.**

The one-qubit sequential record network reproduces the class-operator cylinders
at depths one through three.  Adjacent child sums equal each parent, and the
standard completeness identity proves the finite-depth induction for every
complete future instrument.

The separate integrated memory packet now performs all three visible record
copies as actual protected morphisms:

```text
CNOT X->M; seal X;
seal Y;
CNOT M->Z; seal Z.
```

Its depth-one, depth-two, and depth-three tables are projective.  The only
terminal histories with nonzero mass are `000` and `101`, each with mass
`1/2`, so the visible conditionals are non-Markov exactly as claimed.

The reset channel has two Kraus operators mapping old memory `0` or `1` to
memory `0`.  Their completeness sum is `I_16`, so the reset is CPTP.  Applying
it before the final memory-to-Z copy changes the process and gives both
relevant `Z=1` conditionals zero.  The mandatory memory-deletion control is
therefore closed.

## 5. Collar controls

**Closed as the declared finite control.**

The live-gate morphism is diagonal on the collar and has support only at collar
label `1`.

- It composes after the seal that emits a collar port.
- A seal omitting the collar has the wrong target object and cannot compose.
- A dead collar basis input is mapped to the zero vector.

These are the required positive, absent, and dead controls.  The zero map is a
licensed opportunity filter rather than unconditional evolution; the prose
correctly treats it as continuation capability.

## 6. Count/hash semantics

**Reproducible and adequate.**

The executable freezes the 39-check count, semantic hash, and exact D13
dependency hash.  Its generated packet records source and dependency hashes.
Normal and optimized stdout and JSON are byte-identical.  The semantic verdict
has been narrowed to

```text
FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED
```

rather than prematurely printing the frozen protocol verdict.

The external repair receipt matches all reproduced hashes.  No Python
`assert` supplies a gate.

## 7. `BRIDGE-CONDITIONAL` ceiling

**Correct as the eventual action-level ceiling; not yet the current closed
protocol verdict.**

The repairs make three distinctions that were absent in round one:

1. evaluation schedule is gauge only for a supplied DAG;
2. diagram generation, support, and weights remain an open law;
3. the action-to-kernel and environment/action-to-record-instrument
   dictionaries remain supplied.

Therefore `FINITE-ACTION-TO-RECORD-BRIDGE-PROVED` would still be too strong as
an action-selection statement.  `BRIDGE-CONDITIONAL` precisely records that
the algebra works after those structural inputs are supplied.

During this round, however, the frozen status must remain
`INCOMPLETE-INVESTIGATION`: protected symmetric-monoidal closure is false in
the current constructor and B12 has not closed.

## B-gate disposition

```text
B0  OPEN/FAIL GENERICALLY  overwrite enforcement works, but record identity
                           mapping is not tensor/symmetry closed
B1  PASS for unprotected free SMC; protected symmetric image remains open
B2  PASS at supplied-DAG evaluation scope
B3  PASS
B4  PASS at stated finite frame/pairing scope
B5  PARTIAL  exact seal/collar/repeat cells and CPTP hypothesis pass;
             generic protected monoidal closure remains open
B6  PASS
B7  PASS finitely plus correct completeness induction
B8  PASS including integrated projective packet and deletion control
B9  PASS at the deliberately finite cell scope
B10 PASS with primitive inputs explicit
B11 PASS with downstream dictionary explicit
B12 NOT CLOSED while C1 remains
```

## Remaining blocker ledger

```text
C1  MAJOR  protected source-to-target identity is inferred by occurrence order;
           admitted morphisms are not tensor closed and sealed symmetries fail.

N1  MINOR  pure Mor admission checks labels but not isometry/CPTP completeness;
           retain the explicit supplied-algebra hypothesis.

N2  MINOR  sequential history/memory record copies do not carry live collars;
           collar grammar is established in a separate witness only.
```

## Exact required next repair

1. Add persistent protected port identities and an explicit source-to-target
   correspondence to every protected morphism.
2. Define correspondence composition, tensor disjoint union, append, and
   symmetry transport.
3. Re-run overwrite rejection against that mapping.
4. Add must-pass tests for:
   - tensor of a record-appending morphism with a morphism carrying an existing
     record on the right;
   - symmetry exchanging two protected wires;
   - composition and inverse symmetry returning the original correspondence.
5. Keep CPTP/isometry completeness as an additional physical-admission layer,
   not a consequence of label preservation.

## Final verdict

**MAJOR REVISION, narrowly.**  All round-one numerical, decoherence,
projectivity, memory, and frozen-countercontrol openings are repaired.  One
generic category defect prevents PASS: protected morphisms are not actually a
symmetric-monoidal class under the current occurrence-order constructor.
Repair that correspondence and rerun hostile closure.  If it passes, the
mathematics supports `BRIDGE-CONDITIONAL` as the honest final ceiling; until
then the frozen protocol remains `INCOMPLETE-INVESTIGATION`.
