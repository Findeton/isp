# D36 round 4 — probability/capacity/replay closing delta

**Frozen target:** commit
`da9942d828a19ff12e2774768f5655a1270ef91c`

**Comparison target:** commit
`e80ca6af30ff1e6ca83b97e1521d8a335c054850`

**Prior lane:**
`v10/reviews/d36-round3-probability-closing-delta.md`

**Scope:** participant-local attempt opening, actor receipt wording, reference
probability/capacity preservation, deterministic replay and hidden-law scope

**Verdict:** **PASS — THE PARTICIPANT-LOCAL OPENING REPAIR DOES NOT CHANGE
THE D36 PROBABILITY OR CAPACITY RESULT.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

The reference source and receipt are byte-identical to round 3.  The actor
delta is confined to locally recomputable attempt identities, registration
during addressed prepare handling, a new negative attack/gate, and narrower
transport/remote-ancestry wording.  It introduces no random law, arbitration
selector, rate, uniform capacity theorem or unbounded completion claim.

## 1. Independent reproduction and integrity

I reran the frozen reference under `PYTHONHASHSEED=223606797`; it exited zero
and printed `PASS 22/22`.  I reran the actor companion under
`PYTHONHASHSEED=244948974`; it exited zero and printed `PASS 12/12`.  The
external checker then launched both programs under seeds `17` and `104729`,
compared each output with its committed receipt and printed `PASS 8/8`.

The independently recomputed hashes are:

```text
reference source
2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683

reference complete stdout / committed receipt
868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17

reference stdout body
683ba498d99bac3d430606efc3697cb4e1aa7ac3d4b6103c17237e44b4ba5225

reference internal science
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source
56552383fa42f446b1de925109489b0f180ee880b62a383ed0f97ba8727b5eff

actor complete stdout / committed receipt
e73216911555fbbfb38fbe67538e9119a2bcb5eddf6e0a697b8804e0df38fd1b

actor stdout body
dc0c1f4993638e4819d2d64968ed3d6b4c68eefbb0a749d629af1779d6087c03

actor internal science
2ca6dbb3d998fe87f991c3df26ef036bd9e606f0dd024f0e0c0191b772d72f7e

replay-checker source
a8d3f4554a86bffa9faa4d79ab2c7975aacdb957e585512ede2ba9a7e5c886d8

replay-checker complete stdout / committed receipt
363eb0825999b082a0f34eb899eacf59ca645b6f386a61d67afeff42e83681cd
```

`git diff --check e80ca6a..da9942d` is clean.  The active hashes printed in
section 23 of the note agree with the frozen files.

## 2. Delta census — reference untouched, actor opening repaired

Neither

```text
v10/code/d36_birth_coordination_exact.py
v10/data/d36_birth_coordination_exact.out
```

changes between the comparison and frozen commits.  Thus the complete
reference transition system, exact probability code, gate values, science
object and receipt remain the same bytes.

The actor-source changes are limited to the round-3 opening findings:

1. the structural attempt ID is locally recomputable as

   ```text
   SHA256("structural-attempt", exact carrier record ID, body digest);
   ```

   the body already commits members and requested bases;
2. the rebase opener appends the T-owned carrier and routes prepares but no
   longer extends participant-owned application, response or authorization
   tuples;
3. each addressed participant allocates its next finite slot and registers
   the attempt while servicing its own prepare;
4. a non-carrier-derived attempt with a matching injected side authorization
   is now an exact negative control, raising the attack battery from `13/13`
   to `14/14`;
5. the continuation gate adds `2/2` predictive-state-preservation and `2/2`
   local-registration checks; and
6. the receipt now calls `service_world` a handler-plus-transport macro and
   limits remote ancestry to honest record-generating actors.

These changes alter actor record IDs, science and receipt hashes, as they
should.  They do not alter projected state/edge/terminal counts, main-fixture
ledger sizes, continuation record count or reference semantics.

## 3. K1/K2/K3 and marked factorization — unchanged

Fresh reference execution gives the same path laws:

```text
K1: {Q}:1/3, {P,R}:2/3;
K2: {Q}:1/2, {P,R}:1/2.
```

The K1 arithmetic remains `2/6` orders with Q before both endpoints and `4/6`
orders selecting both endpoints.  K2 remains uniform on the two maximal
independent sets.

K3 remains supported on

```text
{}, {P}, {Q}, {R}, {P,R}.
```

At activity one every probability is `1/5`.  At activity two the weights
remain `1,2,2,2,4`, partition function `11`, and probabilities

```text
1/11, 2/11, 2/11, 2/11, 4/11.
```

The physical K1 mark on two disconnected conflicts remains the four-atom
product of their two local strict orders.  The 24 global presentation orders
still quotient six-to-one:

```text
physical_component_order_atoms=4;
global_presentation_orders=24;
gauge_shuffles_per_component_atom=6.
```

The shared-coin negative control remains nonfactorizing.  Nothing in the
participant registration path supplies a priority, component mark, activity
or random coin.  The reference still prints `selector=UNSELECTED` and
`lambda_unselected=1`.

## 4. DLR, restriction and retry arithmetic — unchanged

The hard-core support accounting remains exact:

```text
positive-mass DLR conditionals  20;
zero-mass boundaries skipped     4.
```

The raw K1 restriction remains `{P}:2/3, {Q}:1/3` versus the direct edge's
`1/2,1/2`.  The explicit K3 R-boundary mixture remains exact.

The finite-bit unique-greatest rows remain

```text
1/2, 3/4, 3/8, 21/32,
```

and the all-distinct complete-order rows remain

```text
1/2, 3/4, 0, 3/8.
```

The almost-sure clause remains conditional on the history law supplying
continued iid retry opportunities, and the receipt still states
`bounded_worst_case=0`.  Local admission of one supplied rebase prepare does
not provide that opportunity law.

## 5. Capacity preservation

The reference capacity gate remains

```text
(max transaction arity,
 max participants,
 max proposals,
 max incident contenders,
 max priority bits) = (3,4,4,2,2),
```

with maximum closure parent arity two.

The four actor graph rows retain the same exact maxima:

```text
pair       26 records;
triangle   39 records;
disjoint   28 records;
partial    32 records;
parent arity at most 2 throughout.
```

The persistent continuation still totals 50 records across its finite BORN
and TOKEN witnesses; the opening repair adds no record to that total.  It
moves allocation of the new finite application/response/authorization slots
from a regional helper into the participant's local prepare event.

Iterating the construction indefinitely would still grow participant state,
transaction count and the append-only ledger.  No uniform bounded-state law
is claimed.  The active verdict continues to leave `unbounded completion`
open, and no record contains a copied unbounded history list.

## 6. No hidden probability law or selector

The actor companion imports no random module, samples no mark and constructs
no probability distribution on mailbox services.  Attempt IDs and signatures
are deterministic digests under the declared ideal-authentication
abstraction.

The simulator still either exhaustively enumerates enabled services for the
main quotient graphs or chooses a canonical serializer to build one
continuation witness.  That construction order has no assigned probability,
rate, duration or clock meaning.  The new participant-local validation tests
whether an addressed prepare is causally admissible; it does not choose among
competing valid proposals.

The receipt's new wording is more conservative, not less:

```text
handler_reads_only_addressed_actor=1;
service_world_is_handler_plus_transport_macro=1;
outgoing_delivery_updates_recipient_mailboxes=1;
remote_predecessor_ownership_proof=0;
honest_record_generating_actor_scope=1.
```

Therefore neither the network transport macro nor participant registration is
promoted into a global scheduler or universe-wide selector.  Opportunity,
arbitration selection, crash recovery, unbounded completion and quantum join
remain explicitly open in the final receipt line.

## 7. Full-history and replay scope

The repair retains the representative-history ceiling.  The 297,980 edge
record checks are representative coordination-quotient edge lifts, and the 56
terminal ledgers are one complete append-only path lift per terminal quotient
state.  They are not all full record histories.

The two continuation paths still prove only finite existence in BORN and TOKEN
mode.  Their old prefixes survive, their old closes lie below their new closes
and their combined ledgers validate.  Participant-local registration improves
those two histories without creating an infinite extension theorem or path
measure.

The updated external replay checker pins the unchanged reference source and
new actor source.  Its fresh `PASS 8/8` comprises four seeded executions, two
within-source equality checks and two committed-receipt equality checks.

## 8. Final disposition

| Integrity question | Disposition |
|---|---|
| reference source or science changed | no; byte-identical to round 3 |
| K1/K2/K3 moved | no |
| marked factorization moved | no; four atoms and `24 -> 4` preserved |
| DLR/restriction moved | no; `20+4` and boundary cells preserved |
| retry events reconflated | no |
| capacity bound moved | no; `(3,4,4,2,2)` and parent arity two preserved |
| actor opening adds randomness | no; carrier/body check is deterministic |
| actor opening selects arbitration | no; supplied attempt admission only |
| actor opening claims uniform bounded memory | no; finite witness only |
| actor opening claims a full history law | no; representative finite lifts only |
| replay integrity regressed | no; fresh `PASS 8/8` |

Final tally:

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Recommendation:** close the D36 round-4 probability/capacity/replay delta.
The participant-local opening repair touches only the actor witness and scope
wording; it preserves every frozen probability and bounded-cell result without
introducing a hidden dynamical law.
