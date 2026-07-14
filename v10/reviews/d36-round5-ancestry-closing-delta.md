# D36 round 5 — focused record-DAG closing delta

**Frozen target:** commit
`9dcdb5f6be7e8dd1b611797c2374a415321012ce`.

**Prior review:** `reviews/d36-round4-ancestry-closing-delta.md` at
`0B / 1M / 0m / 0n`.

**Lane:** sparse participant state, global-index-gap admission, complete
response routing, record-DAG closure, persistent ledgers, authentication and
the honest-record-generating-actor scope ceiling.

**Verdict:** **MAJOR REVISION. THE ROUND-FOUR PARTICIPANT-STATE DEFECT IS
CLOSED: ADMISSION IS NOW KEYED BY STRUCTURAL ATTEMPT AND A VALID ADDRESS-TWO
PREPARE IS ACCEPTED WITH ADDRESS ONE ABSENT. THE CLAIM DOES NOT YET HOLD FOR A
COMPLETE ACTOR HISTORY. TRANSACTION ACTORS STILL LIVE IN A DENSE GLOBAL TUPLE,
AND THE TRANSPORT ROUTES A RESPONSE BY POSITIONAL INDEX. THE SAME GAP PREPARE
THEREFORE EMITS A VALID GRANT AND THEN CRASHES WHEN THE WORLD TRIES TO DELIVER
IT TO TRANSACTION TWO WITHOUT TRANSACTION ONE AS PADDING.**

**Count:** **0 blockers / 1 major / 0 minors / 0 nits.**

The repair is genuine but one layer too narrow.  It establishes sparse local
admission for an isolated participant handler.  It does not establish a
sparse executable actor world, a closed history, or a valid terminal ledger
for that gap case.

## 1. Independent reproduction

I reran the frozen reference with `PYTHONHASHSEED=161803398`, the actor
companion with `PYTHONHASHSEED=314159265` and `271828182`, and the external
replay checker.  All exited zero.  The two actor outputs were byte-identical,
and the replay checker independently reproduced both frozen receipts under
seeds `17` and `104729` before returning `PASS 8/8`.

```text
reference source SHA-256
2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683

reference complete stdout / receipt SHA-256
868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17

reference science SHA-256
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor companion source SHA-256
f353ac2dcff2a7e1b80159cd5602b763669b0157439b09c5a92b50fb01c339b8

actor companion complete stdout / receipt SHA-256
1c72a2d132add307fc49514d52ed6d82e88b42b3ce114fd6d8e3c996c79c5fc4

actor companion stdout-body SHA-256
02375603f824efc74a6953b8d8e6d4a35c3a8f6cff964200e005e7c4752db9b7

actor companion science SHA-256
6621a32688a27b0f55e99eddf570c7a2956d718e5bd4a37f95d48b3529403227

replay checker source SHA-256
b76adbe744c278b3d91a2f3f2a4be0c278a2bad40982ea54f9a10a867719519f

replay checker complete stdout / receipt SHA-256
554369b4f93057f3d838f891c19f49ebb92f4eae35f2afc6703dc7efa62d9a33

note SHA-256
422fafcb42edcef4da58209d2cb7fc74223daa9f2d7be546438f056b74663aa4
```

The new receipt exactly reproduces:

```text
global-index-gap prepare accepted        1 / 1
local prepare delivery orders            2 / 2
typed responses                           4 / 4
no global slot padding                    2 / 2
actor gates                              PASS 13 / 13
```

The pre-existing reference gates reproduce `PASS 22/22`.  The actor receipt
also reproduces all `56` representative terminal ledgers, maximum parent
arity two, all `14/14` authentication/replay attacks rejected before durable
mutation, both persistent stale/rebase continuations, all four disjoint
service diamonds, and the declared ownership ceiling:

```text
remote_predecessor_ownership_proof=0
honest_record_generating_actor_scope=1
```

The finding below is therefore a new finite counterexample to the promoted
gap claim, not seed sensitivity or drift in an older receipt.

## 2. Round-four finding disposition

### M1 — global ordinal in participant admission: closed locally

`ParticipantActor` no longer carries dense promise, application or response
arrays indexed by the world transaction ordinal.  Its mutable coordination
state is sparse by structural attempt:

```text
promise_attempt
application_entries   (attempt ID -> status)
response_entries      (attempt ID -> exact response record)
authorizations        keyed first by attempt ID
```

The prepare handler derives the attempt from the exact carrier and body,
checks that it is absent from the sparse application and response domains,
and applies the prior capability, signature and replay checks.  It has no
lower-global-index admission predicate.

I repeated the round-four gap at the handler boundary.  Starting from the
closed transaction-zero BORN participant, an exact valid transaction-two
prepare is accepted while transaction one has never been presented.  The
participant adds only transaction two's structural attempt and emits one
typed `GRANT`; it creates no entry for transaction one.  Delivering exact
prepares one and two in either order gives one typed `GRANT` followed by one
typed `REJECT`, because the first attempt holds the exclusive promise.  Both
attempts receive responses and neither order requires a participant padding
slot.

That is the right local result.  The round-four major is closed as a theorem
about the participant handler and its physical participant state.

### Persistent ancestry, authentication and scope gates: remain sound

The sparse participant tables do not regress the two-epoch construction.  In
both BORN and TOKEN modes the stale attempt aborts, the rebased attempt
commits, the final participant version is two, the old immutable prefix is
preserved, the combined ledger validates, and the old close is below the new
close.  Both modes retain participant-local registration and reject the stale
envelope.  Their combined record count remains `50`.

Carrier/body attempt derivation, exact response evidence, side-label
rejection and the prior replay/authentication attacks remain green.  The
remote-predecessor limitation remains explicitly outside the theorem rather
than being silently promoted.  I found no basis to reopen any prior
persistent-ledger, authentication, ownership-scope or clock-scope finding.

## 3. MAJOR M1 — the actor world still requires a dense global transaction registry

The sparse repair stops at the participant boundary.  The executable world
still declares

```text
transactions: Tuple[TransactionActor, ...]
```

and transport to a transaction actor still performs

```text
actor = transactions[envelope.target_index]
```

`services()` likewise gives transaction actors their address by enumerating
this tuple.  These are operational actor-world structures, not fields created
inside `project_reference()`.  Consequently, nominal transaction address two
cannot exist in the actor world unless tuple positions zero and one also
exist.  Appending a transaction-two actor as the second tuple element does
not help: its physical tuple position is one while all exact envelopes still
target address two.

### 3.1 Exact finite transport counterexample

I started from the exact quiescent single/BORN actor world used by the new
gate.  It has one closed transaction actor:

```text
len(world.transactions)                         1
transaction address 1 present                   0
transaction address 2 present                   0
```

I then constructed the same exact valid transaction-two `FOLLOWUP_BIRTH`
carrier, carrier/body structural attempt, stable capability, signature and
prepare used by the positive gap gate.  There are two different results at
the two advertised layers:

```text
direct participant handler accepts              1
typed response                                  GRANT
new participant record count                    1

full service_world result                       IndexError
exception                                       list index out of range
```

The participant transition itself succeeds.  `service_world()` then tries to
deliver its outgoing grant to target kind `T`, target index `2`.
`append_to_target()` indexes a one-element transaction tuple and crashes.
No transaction actor receives the typed response, no transaction-owned record
can follow it, the attempt cannot close, and no terminal ledger exists to
validate.

This is also a disjoint-insertion counterexample.  Without an unrelated actor
at transaction address one, the valid local interaction cannot be completed.
Adding such an actor as padding changes the world from transport failure to a
routable history even though no evidence from it reaches the participant.
Thus disjoint global registry occupancy still affects whether an otherwise
identical local history exists.

### 3.2 Why A12 does not gate the claimed closure

`sparse_slot_covariance_gate()` calls `handle_participant()` directly.  It
does not:

1. register a transaction-two actor while address one is absent;
2. route either emitted response through `append_to_target()`;
3. service the receiving transaction actor;
4. drive the two attempts to commit or abort;
5. validate their actor wires, record ancestry or terminal ledgers.

Its `typed_responses=4/4` are exact handler return values, not four responses
successfully delivered to sparsely addressed transaction actors.  Its
`no_global_slot_padding=2/2` establishes no padding only in the participant's
new sparse tables.  It does not inspect the dense transaction registry needed
by the complete world.  A12 therefore carries a valid participant-level
result but cannot support the stronger note statement that the integer
address survives only as a nominal routing/analysis coordinate or that dense
global arrays remain solely in the reference projection.

## 4. Required repair and closing gate

Replace the positional transaction tuple as a physical routing dependency.
A transaction actor needs a sparse structural address—preferably the exact
carrier or structural-attempt identity, or another stable actor-local
capability-bound key.  The reference adapter may separately enumerate those
actors into dense coordinates for comparison with the frozen checker.

The next exact gate must run through the complete actor world, not call the
participant handler alone:

1. create/register transaction two with transaction one genuinely absent;
2. service the valid prepare at the participant;
3. route its typed response to transaction two through ordinary transport;
4. service all resulting transaction and participant messages to quiescence;
5. validate exact ownership wires, parent-before-use, immutable ancestry and
   the terminal ledger;
6. repeat for both local prepare orders; and
7. insert an entirely disjoint transaction and prove the restricted local
   history is isomorphic, including routed response and closure records.

No placeholder transaction actor, empty tuple slot or preinstalled regional
entry may satisfy this gate.  The absence must exist in the executable world,
not only in participant state.

## 5. Strongest earned statement

At frozen commit `9dcdb5f`, D36 has a structurally keyed, sparse participant
admission law.  A participant can accept a valid later-address prepare and
issue a typed response without knowing or padding earlier global transaction
ordinals; the existing finite closed-attempt ledgers, authentication tests and
declared honest-actor scope remain intact.

D36 does **not** yet have a structurally sparse complete actor history for
that case.  Transaction routing still consults a dense global registry, so
the construction-order gauge has moved out of participant state but has not
been removed from the physical actor architecture.  Record-DAG closure for a
gapped structural attempt remains unproved.  Paper promotion should remain
withheld pending the end-to-end sparse-routing gate above.
