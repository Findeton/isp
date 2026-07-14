# D36 round 4 — focused record-DAG closing delta

**Frozen target:** commit
`da9942d828a19ff12e2774768f5655a1270ef91c`.

**Prior review:** `reviews/d36-round3-ancestry-closing-delta.md` at
`0B / 1M / 1m / 0n`.

**Lane:** participant-local attempt derivation and registration, pre-service
state preservation, response-record provenance, persistent continuation DAGs,
and the honest-record-generating-actor ceiling.

**Verdict:** **MAJOR REVISION. THE ROUND-THREE MAJOR AND MINOR ARE CLOSED AT
THE AUDITED TWO-EPOCH HORIZON, BUT THE NEW “LOCAL” SLOT RULE IS INDEXED BY THE
GLOBAL TRANSACTION ORDINAL. INSERTING OR DELIVERING AN UNRELATED EARLIER
TRANSACTION CAN TURN THE SAME LOCALLY VALID PREPARE FROM ACCEPTED TO REJECTED.**

**Count:** **0 blockers / 1 major / 0 minors / 0 nits.**

The target performs the requested repair faithfully for transaction index
one.  It removes the regional authorization write, derives the attempt inside
the addressed participant, records the local registration through that
participant's response, and retains the valid continuous ledger.  The fresh
counterexample is a finite locality/covariance failure in the rule used to
decide which new slot may be allocated.

## 1. Independent reproduction

I reran the reference under `PYTHONHASHSEED=161803398`, the actor companion
under `PYTHONHASHSEED=314159265` and `271828182`, and the external replay
checker.  All exited zero.  The actor runs were byte-identical, and the replay
checker independently reproduced the reference and actor receipts under seeds
`17` and `104729` before returning `PASS 8/8`.

```text
reference source SHA-256
2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683

reference complete stdout / receipt SHA-256
868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17

reference science SHA-256
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor companion source SHA-256
56552383fa42f446b1de925109489b0f180ee880b62a383ed0f97ba8727b5eff

actor companion complete stdout / receipt SHA-256
e73216911555fbbfb38fbe67538e9119a2bcb5eddf6e0a697b8804e0df38fd1b

actor companion stdout-body SHA-256
dc0c1f4993638e4819d2d64968ed3d6b4c68eefbb0a749d629af1779d6087c03

actor companion science SHA-256
2ca6dbb3d998fe87f991c3df26ef036bd9e606f0dd024f0e0c0191b772d72f7e

replay checker source SHA-256
a8d3f4554a86bffa9faa4d79ab2c7975aacdb957e585512ede2ba9a7e5c886d8

replay checker complete stdout / receipt SHA-256
363eb0825999b082a0f34eb899eacf59ca645b6f386a61d67afeff42e83681cd

note SHA-256
e39ff5b3f963ab6cd69e76e359bb313938e1e7ca29d1fb1a7d3d5d2eb7c0baa5
```

The companion exactly reproduces:

```text
PASS 12/12;
14 / 14 registered attacks rejected;
opening predictive state preserved 2 / 2;
participant-local registration 2 / 2;
same-world prefix preserved 2 / 2;
combined ledger valid 2 / 2;
old close below new close 2 / 2;
stale envelope rejected 2 / 2;
combined continuation records 50;
remote predecessor ownership proof 0;
honest record-generating actor scope 1.
```

All four original coordination projections, all `56` representative terminal
ledgers, the `297,980` representative edge deltas and parent arity two also
reproduce.  `git diff --check da9942d^ da9942d` is clean.  The finding below is
therefore not receipt drift.

## 2. Round-three finding dispositions

### M1 — direct regional authorization installation: closed at the audited continuation

`append_rebase_attempt()` no longer extends any participant's application
slots, response slots or authorization table.  It appends the T-owned carrier
and routes one prepare to each named participant.  I snapshotted all
participant fields other than transport mailbox state immediately before and
after this opening.  Both carrier modes give:

```text
version, version record, head record                 equal
promise and promise-attempt                          equal
applications and response-record slots               equal
capabilities and authorizations                       equal
used-envelope state                                   equal
only mailbox                                           +1 prepare
```

Thus a participant's predictive state no longer changes merely because the
regional constructor has created an attempt.

When the participant services its own prepare, it now checks

```text
attempt_id = SHA256("structural-attempt", exact carrier ID, body digest),
```

allocates the bounded application/response slot, stores the corresponding
attempt authorization, and emits its grant or rejection in the same local
event.  My direct BORN and TOKEN checks returned:

```text
predictive fields equal before own service             1 / 1
participant recomputed attempt formula                 1 / 1
prepare accepted                                       1 / 1
application slots before / after                       1 / 2
authorization installed locally                        1 / 1
authorization fields present in response record        1 / 1
participant head equals emitted response record        1 / 1
```

The response payload contains transaction, attempt, body, protected base,
live version and stable capability.  Its exact record ID commits those fields
and its old participant-head/carrier parents.  The local registration is
therefore represented in the immutable history rather than surviving only in
a side table.

### M1 — side-authorized non-carrier attempt: closed

I repeated the round-three counterexample in both modes.  I installed a
matching side authorization for `NOT-CARRIER-DERIVED`, signed a prepare over
the unchanged exact carrier and retained all other accepted fields.  The new
carrier equation dominates the side table:

```text
mode    formula holds   signature authentic   side authorization   accepted
BORN          0                  1                    1                 0
TOKEN         0                  1                    1                 0

actor/output unchanged, both modes = 1
```

The former fully closed arbitrary-label history can no longer be generated.
Carrier/body attempt derivation is now a participant acceptance invariant at
the audited opening.

### M1 — persistent ledger, wires and ancestry: remains closed

The local registration change does not break the repaired two-epoch history.
The BORN and TOKEN continuations still use the actual prior actor world and
one ledger, retain their exact old prefixes, extend participant heads, validate
all owned wires, and place the old close below the new close.  The combined
record total remains `24 + 26 = 50`, maximum parent arity remains two, and the
new attempt commits to participant version two in both modes.

### m1 — remote predecessor ownership: closed by an explicit theorem ceiling

The round-three wrong-wire exhibit remains possible: an ideally signed remote
record can carry an existing but incorrect owner-wire predecessor and pass the
receiver before the full ledger wire check fails.  The target now says this
directly in both note and receipt:

```text
remote_predecessor_ownership_proof=0
honest_record_generating_actor_scope=1
```

The note further states that Byzantine remote ancestry validation remains
open.  I reran the old malformed-sender exhibit and confirmed
`authentic=1`, `handler_accepted=1`, `validate_owned_wires=FAIL`; it is now
outside, rather than silently inside, the theorem.  That is exactly the scope
repair requested in round three.  No residual minor remains so long as this
honest-record-generating-actor hypothesis stays attached to every safety and
ancestry promotion.

## 3. MAJOR M1 — “next local slot” is actually the global transaction index

The new admission rule defines

```text
locally_allocatable =
    envelope.tx_index == len(actor.applications)
    and len(actor.response_records) == len(actor.applications).
```

But `tx_index` is not a participant-local incidence counter.  It is also the
index of the transaction actor in the global `world.transactions` tuple and
the address used throughout the reference projection.  Initial fixed batches
hide this by preallocating every global position—including `-1` positions for
transactions that do not involve the participant.  The new persistent opener
does not preallocate such positions, correctly avoiding the round-three
regional write.  It therefore exposes a gap whenever the next transaction
relevant to A is not the next transaction globally.

### 3.1 Exact finite counterexample

Start from the exact closed transaction-zero BORN participant used by the
continuation.  Its local application tuple has length one.  Construct two
valid lineage prepares using the already carried stable capability:

```text
prepare 1: exact T1 carrier, body 1, carrier-derived attempt 1;
prepare 2: exact T2 carrier, body 2, carrier-derived attempt 2.
```

Every signature, carrier digest, capability and attempt formula is valid.  I
then ask the same participant to service prepare 2 before prepare 1.  The exact
result is:

```text
initial local slots                                  1
prepare-2 carrier/body formula                       1
prepare-2 signature authentic                        1
stable capability already present                    1
prepare 2 accepted before prepare 1                  0
actor and outputs unchanged                          1

prepare 1 accepted                                   1
local slots after prepare 1                          2
same prepare 2 accepted after prepare 1               1
prepare-2 response records emitted                    1
```

Nothing about prepare 2 changes.  Its acceptance flips solely because a lower
global transaction ordinal has now been serviced.

This has two equivalent physical readings.

1. **Disjoint insertion:** in history H, A's next local attempt has global
   index one and is admitted.  In H plus an unrelated transaction Q in another
   component, Q consumes global index one and A's otherwise equivalent next
   attempt has index two.  A rejects it despite having no causal information
   about Q.
2. **Out-of-order delivery:** two legitimate new attempts involving A exist,
   but the index-two prepare reaches A before index one.  The higher prepare is
   rejected without a typed grant/rejection response.  If the transport macro
   dequeues it once, its transaction can remain open even under failure-free
   fair service.

The counterexample uses only three finite attempts, below D36's audited
four-proposal ceiling.  It is not an objection about unbounded growth, crash
recovery or the still-open opportunity probabilities.  It shows that the
proposed local opening is not invariant under insertion of causally disjoint
history.  A global construction ordinal has become an operative acceptance
field.

This also creates a forced dilemma.  A participant can accept the skipped
index only if either:

- the missing global slots/authorization were preinstalled, reviving the
  round-three regional mutation; or
- every lower global transaction is first delivered to that participant,
  introducing a nonlocal global census/order.

Neither is an actor-local record rule.

**Required repair:** key local predictive state by structural attempt identity
or by an actual participant-local slot carried in that participant's causal
capability/wire, not by position in the global transaction tuple.  A sparse
finite map is sufficient at the present bounded scope; no unbounded record is
required.  Then execute two exact gates:

1. insert a disjoint transaction before A's next attempt and prove A's local
   acceptance/response is unchanged up to the declared structural relabeling;
2. deliver two valid new prepares in both orders and prove each receives a
   typed local response, with no preinstalled authorization and no global-slot
   padding.

The reference projection may retain global array indices as an analysis
coordinate.  They cannot select which physical local record transition is
allowed.

## 4. What is now earned

The frozen target earns a strong but two-epoch-specific result:

- exact carrier/body attempt labels are participant-recomputed;
- participant predictive state remains unchanged until its own prepare event;
- slot allocation, authorization and response-record creation occur in that
  one addressed event;
- the response record carries the complete local registration fields;
- matching side-table data cannot override a wrong attempt formula;
- BORN and TOKEN retain continuous valid record DAGs with old-close ancestry;
- exact evidence substitution and cross-attempt replay remain excluded; and
- remote-wire provenance is honestly limited to correct record-generating
  actors rather than promoted to Byzantine validation.

The strongest defensible headline is therefore:

> **Clock-free actor-local servicing and append-only record refinement for the
> audited fixed batches plus one causally ordered next-global-index attempt,
> under honest record-generating actors.**

It does not yet establish a component-local opening law for arbitrary supplied
finite attempt incidence or delivery order.

## 5. Final disposition

**Fresh mathematical counterexample:** **1 class — disjoint insertion / valid
prepare-order dependence.**

```text
B  blockers  0
M  majors    1   global transaction ordinal controls local slot admissibility
m  minors    0
n  nits      0
```

**Final count:** **0B / 1M / 0m / 0n.**

**Decision:** **MAJOR REVISION.**  Close the round-three regional-
authorization major and the remote-predecessor scope minor.  Retain the local
attempt equation, response-carried registration and persistent ledger gates.
Replace the globally contiguous slot condition with a participant-local sparse
attempt/slot law before promoting the actor-local continuation beyond the one
audited next-index epoch.
