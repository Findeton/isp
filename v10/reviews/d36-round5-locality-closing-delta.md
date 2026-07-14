# D36 round 5 — locality closing delta

**Frozen target:** commit
`9dcdb5f6be7e8dd1b611797c2374a415321012ce`.

**Round-four baseline:** the focused record-DAG review at
`0B / 1M / 0m / 0n`; the parallel locality review was already clean at
`0B / 0M / 0m / 0n`.

**Lane:** sparse participant-owned attempt state, disjoint-insertion and
renaming covariance, local prepare-order response totality, duplicate
structural identities, no-padding locality, reference projection separation,
and handler-plus-transport scope.

**Verdict:** **DELTA CLOSED.  STRUCTURAL ATTEMPT IDENTITY, NOT A GLOBAL
TRANSACTION-TUPLE POSITION, NOW CONTROLS PARTICIPANT ALLOCATION.  GAP ADDRESSES
AND BOTH LOCAL DELIVERY ORDERS RECEIVE TYPED RESPONSES WITHOUT PADDING, WHILE
GLOBAL ADDRESSES REMAIN ONLY ROUTING AND REFERENCE-ANALYSIS COORDINATES.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

The round-four counterexample no longer reproduces.  A participant can allocate
an exact address-two or address-42 attempt while lower global addresses are
absent from its local state.  Its application, response and authorization
domains grow by exactly the structural attempts it services.  Arrival order
may decide which contender obtains the exclusive grant, as explicitly scoped,
but it no longer decides whether the other valid prepare receives a typed
response.

## 1. Exact independent reproduction

I reran the reference, actor companion and external replay checker from the
frozen tree.  They return `PASS 22/22`, `PASS 13/13` and `PASS 8/8`.
The replay checker independently runs the reference and actor processes under
hash seeds 17 and 104729 and confirms byte identity with both committed
receipts.

```text
reference source  2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683
reference stdout  868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17
reference science a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source      f353ac2dcff2a7e1b80159cd5602b763669b0157439b09c5a92b50fb01c339b8
actor stdout      1c72a2d132add307fc49514d52ed6d82e88b42b3ce114fd6d8e3c996c79c5fc4
actor body        02375603f824efc74a6953b8d8e6d4a35c3a8f6cff964200e005e7c4752db9b7
actor science     6621a32688a27b0f55e99eddf570c7a2956d718e5bd4a37f95d48b3529403227

replay source     b76adbe744c278b3d91a2f3f2a4be0c278a2bad40982ea54f9a10a867719519f
replay stdout     554369b4f93057f3d838f891c19f49ebb92f4eae35f2afc6703dc7efa62d9a33
note              422fafcb42edcef4da58209d2cb7fc74223daa9f2d7be546438f056b74663aa4
```

The new exact row reproduces:

```text
global-index-gap prepare accepted                    1 / 1
two local prepare orders                             2 / 2
typed responses                                      4 / 4
no global slot padding                               2 / 2
order-family SHA-256
43e49aa3790326a5fd153f29500879f3287507d4ff299baadfde5fbe11a06e1f
```

The earlier gates also remain exact:

```text
authentication/replay attacks                       14 / 14 rejected
disjoint service diamonds                            4 / 4 commuting
opening predictive state preserved                   2 / 2
participant-local registration                       2 / 2
combined continuation ledgers valid                  2 / 2
old close below new close                            2 / 2
combined continuation records                           50
```

Independent direct calls return:

```text
adversarial_gate          (14,14)
sparse_slot_covariance_gate
  (1,2,4,2,43e49aa3790326a5fd153f29500879f3287507d4ff299baadfde5fbe11a06e1f)
```

All four fixed coordination projections, all 56 representative terminal
ledgers and all 297,980 representative edge deltas remain unchanged.

## 2. Changed-line audit

I inspected every changed line in the six-file `9dcdb5f` patch.

- `ParticipantActor` replaces dense global-indexed promise/application/
  response state with `promise_attempt`, sparse `application_entries`, sparse
  `response_entries`, and attempt-first authorization entries.
- `sparse_has`, `sparse_value` and `sparse_set` provide deterministic finite
  attempt-keyed lookup and update.  Insertion is sorted by structural attempt
  ID and never manufactures missing global positions.
- Prepare acceptance tests absence of the exact structural attempt from the
  two sparse domains.  The handler allocates and updates those domains by
  attempt ID; decision acceptance and application likewise read that exact
  attempt's entries.
- `project_reference` alone reconstructs dense applications and promise
  transaction indices for comparison with the frozen reference checker.  That
  reconstruction is downstream of physical handler execution and is not read
  by the allocation law.
- The new `sparse_slot_covariance_gate` exercises the round-four gap and both
  local orders.  Gate A12 and the receipt make its exact scope visible.
- The replay checker updates only the locked actor-source hash.  Its output,
  the actor receipt, note and log contain the corresponding deterministic
  hashes and sparse-state wording.

`git diff --check 9dcdb5f^ 9dcdb5f` is clean.  No probability, selector,
clock, failure, quantum or spacetime rule changes in this patch.

## 3. Round-four major M1 — global ordinal controls local allocation: closed

The rejected rule was:

```text
tx_index == len(local dense applications).
```

The replacement is:

```text
attempt absent from local application_entries
and
attempt absent from local response_entries.
```

Carrier/body derivation, stable capability, exact authentication and replay
checks still apply.  `tx_index` remains authenticated and recorded so a
response can be routed to its transaction actor, but no integer comparison or
array subscript involving it occurs in participant allocation.

I repeated the exact finite gap construction with a carrier at nominal address
42 after one closed attempt.  The participant had one prior sparse entry and
no entries for addresses 1 through 41.  The result was:

```text
carrier/body attempt formula valid                           1
prepare accepted                                             1
typed response                                           GRANT
application-domain delta                                    +1
new exact attempt present                                    1
padding entries created                                      0
```

Thus neither a missing lower transaction ordinal nor the size of a global
transaction tuple controls physical local admissibility.

## 4. Both local orders and full transport

The committed gate directly handles address-one and address-two prepares from
the same closed base in both orders.  The first serviced prepare obtains the
free promise and emits `GRANT`; the second is still accepted as a local event,
allocates its own sparse entry and emits the typed busy `REJECT`.  Reversing
the order reverses which structural attempt receives the grant, but preserves
the response census and two-attempt sparse domain.

I additionally embedded the counterexample in a full three-transaction actor
world:

```text
global 0  P(A,B)
global 1  Q(C,D)    disjoint insertion
global 2  R(A,B)
```

Participant A begins with exactly two sparse entries, for P and R; it has no Q
entry and the local domain length is two while the global transaction tuple
length is three.  Servicing A's prepares through `service_world` gives:

```text
A order              typed responses       A entries    response destinations
R(index 2), P(0)     GRANT, REJECT              2        T2, T0
P(index 0), R(2)     GRANT, REJECT              2        T0, T2
```

Each service changes A's handler state and then the addressed transaction's
recipient mailbox.  This verifies that the sparse result is not an artifact of
calling `handle_participant` without transport and that no placeholder
transaction or participant slot is needed.

The existing scope language remains honest:

```text
handler_reads_only_addressed_actor=1
service_world_is_handler_plus_transport_macro=1
outgoing_delivery_updates_recipient_mailboxes=1.
```

No literal one-object `service_world` claim has returned.

## 5. Disjoint insertion and renaming covariance

I checked two independent presentations beyond the committed gap gate.

First, moving the same P(A,B) component around a disjoint Q(C,D) component
changes P's nominal global address from zero to one.  In both presentations A
has one sparse entry, services the prepare, emits a participant-owned record
and routes the same typed `GRANT`.  Exact IDs relabel because transaction
addresses are committed structural coordinates; local admissibility and
response type do not change.

Second, renaming only the remote component from Q(C,D) to Q(X,Y), while
leaving the A/B component's structural coordinates fixed, leaves the complete
A and B actor objects byte-equal before service.  Both executions accept and
emit the same typed grant.  Hence an unrelated component neither pads nor
silently perturbs the local sparse law.

This is the covariance required by the round-four closure gate.  It does not
claim that construction addresses are absent from record identity; it proves
that their relabeling or disjoint insertion no longer selects whether a valid
local response exists.

## 6. Duplicate-identity sweep

Sparse maps require a unique structural key, so I tested replay and duplicate
variants explicitly.

```text
exact duplicate prepare after response rejects unchanged             1
same attempt with a distinct authenticated envelope ID exists         1
that same-attempt envelope variant rejects unchanged                  1
same carrier/body attempt moved to another tx address rejects         1
```

The exact replay is caught by the used-envelope set.  A distinct envelope
with the already registered attempt reaches the sparse response check and
rejects because that attempt already has an exact response record.  Moving the
same identity to another address fails the carrier-owner/address binding.

Within the declared collision-free digest abstraction, two distinct exact
carrier/body pairs cannot share an attempt ID.  `sparse_set` also checks for an
existing key before insertion, so all reachable constructors preserve a
single entry per attempt.  Manually corrupting an actor dataclass with duplicate
keys is not a protocol transition and does not create an in-scope duplicate
history.

## 7. Scope retained, not promoted

Sparse entries are finite because the attempt family is supplied and finite;
the patch does not claim a uniform bounded-state or infinite-history theorem.
Arrival order still selects which compatible contender receives an exclusive
grant before an arbitration law is supplied.  It does not suppress the other
contender's typed response.

The previously declared remote-predecessor ceiling also remains explicit:

```text
remote_predecessor_ownership_proof=0
honest_record_generating_actor_scope=1.
```

None of these honest scope ceilings is disguised as sparse-state locality.

## 8. Final disposition

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Final count:** **0B / 0M / 0m / 0n.**

At the declared finite, ideal-authentication and honest-record-actor scope,
the focused locality result is now:

```text
STRUCTURAL-ATTEMPT-KEYED ACTOR-LOCAL SERVICING WITH TYPED RESPONSE TOTALITY
UNDER GLOBAL-ADDRESS GAPS AND BOTH LOCAL PREPARE ORDERS, ON ONE APPEND-ONLY
LEDGER; SERVICE_WORLD REMAINS AN EXPLICIT HANDLER-PLUS-TRANSPORT MACRO.
```

This closure does not promote opportunity, arbitration, retry fairness,
failure recovery, unbounded completion, quantum realization or spacetime
claims.
