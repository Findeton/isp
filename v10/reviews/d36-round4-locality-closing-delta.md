# D36 round 4 — locality closing delta

**Frozen target:** commit
`da9942d828a19ff12e2774768f5655a1270ef91c`.

**Round-three baseline:**
`reviews/d36-round3-locality-closing-delta.md` at `0B / 1M / 1m / 0n`.

**Lane:** participant-local attempt opening, local slot allocation and durable
registration, pre-service predictive-state preservation, orchestration scope,
and handler/transport event granularity.

**Verdict:** **DELTA CLOSED.  THE REBASE CARRIER NO LONGER INSTALLS
PARTICIPANT-OWNED PREDICTIVE STATE.  EACH PARTICIPANT DERIVES AND RECORDS THE
ATTEMPT WHEN IT SERVICES ITS OWN PREPARE, AND THE SERVICE DRIVER IS NOW
ACCURATELY SCOPED AS A HANDLER-PLUS-TRANSPORT MACRO.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

The round-three authorization oracle is gone.  `append_rebase_attempt` appends
the T-owned carrier, constructs the new T actor and delivers prepares, but it
does not extend any participant application slot, response slot or
authorization table.  The only participant field changed before addressed
service is the mailbox, which the note and receipt now explicitly identify as
transport state rather than a one-object handler transition.

## 1. Exact independent reproduction

I reran the reference, actor companion and external two-process replay checker
from the frozen tree.  They return `PASS 22/22`, `PASS 12/12` and `PASS 8/8`.
The external checker independently reruns both executables under hash seeds 17
and 104729 and reports byte identity with the committed receipts.

```text
reference source  2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683
reference stdout  868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17
reference science a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source      56552383fa42f446b1de925109489b0f180ee880b62a383ed0f97ba8727b5eff
actor stdout      e73216911555fbbfb38fbe67538e9119a2bcb5eddf6e0a697b8804e0df38fd1b
actor body        dc0c1f4993638e4819d2d64968ed3d6b4c68eefbb0a749d629af1779d6087c03
actor science     2ca6dbb3d998fe87f991c3df26ef036bd9e606f0dd024f0e0c0191b772d72f7e

replay source     a8d3f4554a86bffa9faa4d79ab2c7975aacdb957e585512ede2ba9a7e5c886d8
replay stdout     363eb0825999b082a0f34eb899eacf59ca645b6f386a61d67afeff42e83681cd
note              e39ff5b3f963ab6cd69e76e359bb313938e1e7ca29d1fb1a7d3d5d2eb7c0baa5
```

The revised exact rows reproduce:

```text
authentication/replay attacks                         14 / 14 rejected
opening predictive state preserved                      2 / 2
participant-local registration                          2 / 2
same-world stale attempts                               2 / 2 closed abort
same-world rebased attempts                             2 / 2 closed commit
combined ledgers valid                                  2 / 2
old close below new close                               2 / 2
combined continuation records                              50
```

Independent direct calls return:

```text
adversarial_gate  (14,14)
continuation_gate (2,2,2,2,2,2,2,2,2,50,
  754a90581f491029b6878524187b0229145ed9bb3ff24590947b3a2f853f11c0).
```

## 2. Changed-line audit

I inspected every line changed by `da9942d` in its six-file patch.

- `d36b_actor_record_refinement_exact.py` introduces one canonical
  `structural_attempt_id(carrier, body)` calculation, uses it in initial and
  continuing attempts, moves next-slot allocation and authorization storage
  into `handle_participant`, removes those writes from
  `append_rebase_attempt`, adds the non-carrier attempt attack and continuation
  snapshot gates, and replaces the one-mailbox wording with the transport-macro
  scope.
- The actor receipt records the expected 14/14, 2/2 and 2/2 gate changes,
  updates the deterministic hashes, and explicitly prints both recipient
  mailbox delivery and the honest-record-actor ceiling.
- The replay checker changes only the locked actor source hash; its committed
  output changes only the actor source/stdout hashes and reproduces exactly.
- The note and log freeze the round-three findings, describe the local repair,
  retain the opportunity and remote-ancestry ceilings, and state that
  `service_world` is not a literal one-object transition.

No unrelated reference semantics, graph count, terminal count, probability,
arbitration, clock, quantum or spacetime claim changes in this patch.

## 3. Round-three major M1 — participant-local opening: closed

### 3.1 Carrier opening preserves participant predictive state

For both BORN and TOKEN I independently ran the stale attempt to its actual
terminal world, snapshotted the ledger and participants, and called
`append_rebase_attempt`.  The exact census is:

```text
old transaction tuple retained                              1
every old ledger byte retained                              1
records added by opening                                    1
owner kind of every added record                            T

predictive fields equal across every participant:
  name/version/version_record/head_record                   1
  promise/promise_attempt                                   1
  applications/response_records                             1
  capabilities/authorizations/used                          1

authorization-count delta before service                 (0,0)
application-slot delta before service                    (0,0)
response-slot delta before service                       (0,0)
mailbox delta from routed prepares                       (1,1)
```

The helper source contains no read or write of `applications`,
`response_records` or `authorizations`.  It reuses the stable route
capabilities already carried by the participants and transports one prepare to
each addressed mailbox.  Thus the prior hidden regional authorization
installation is absent, not merely made inert.

### 3.2 The addressed handler derives, allocates and records locally

For a new slot, `participant_accepts_prepare` now requires:

```text
tx_index = len(local applications)
len(local response_records) = len(local applications)
capability is already in the addressed participant
attempt_id = SHA256("structural-attempt", exact carrier ID, body digest)
exact carrier and envelope authentication validate
envelope has not already been used.
```

Only after those checks does `handle_participant` extend its own application
and response tuples and store

```text
(tx_index, attempt_id, body_digest, base_version, capability).
```

The same local handler event emits one P-owned grant or rejection record whose
payload contains that transaction, attempt, body, base and capability.  My
direct before/after probe returns, in each carrier mode:

```text
local attempt equation                                      1
prepare accepted by addressed actor                         1
application-slot delta                                     +1
response-record-slot delta                                 +1
authorization delta                                        +1
emitted records                                              1
emitted record owner                                         P
emitted record names exact attempt                           1
other participant predictive state unchanged                1
```

This is the required no-silent-history repair.  The attempt-specific state is
both installed by the participant and represented immediately in its durable
response record.

### 3.3 The orchestrator no longer supplies acceptance authority

The previous decisive counterexample was that deleting only the helper-injected
authorization toggled the same prepare from accepted to rejected.  There is no
such tuple to delete now.  A participant's new-attempt acceptance is
determined by its pre-existing stable capability, its next local slot, and the
signed exact carrier/body equation.

The added negative gate goes further: it injects a matching authorization for
an arbitrary non-carrier-derived attempt and supplies a correspondingly signed
prepare.  The participant still rejects before actor mutation or record
creation because the carrier equation is unconditional.  This closes the
round-three observation that attempt derivation was only a constructor
convention.

## 4. Round-three minor m1 — service-event granularity: closed by scope

The implementation intentionally retains the same macro transition:
`service_world` removes one envelope, invokes exactly one addressed handler,
replaces that actor, and then delivers the handler's outgoing envelopes into
recipient-owned mailboxes.  Such a macro can change the addressed actor plus
one or more recipient actor objects, so it is not literally a one-object
event.

The overclaim has been removed.  The receipt now prints:

```text
handler_reads_only_addressed_actor=1
service_world_is_handler_plus_transport_macro=1
outgoing_delivery_updates_recipient_mailboxes=1.
```

The note likewise says the macro is not claimed to change only one actor
object.  The narrower locality statement is exact: `handle_participant` and
`handle_transaction` each receive and return only their addressed actor; the
additional object changes are declared mailbox transport, not remote reads or
silent durable participant updates.  This is the explicit scoping alternative
allowed by the round-three closure gate, so no delivery split is required.

## 5. Fresh finite counterexample sweep

I tested the new admission boundary beyond the registered receipt cases.

```text
duplicate locally registered prepare rejects unchanged                  1
future transaction index with a gap rejects unchanged                   1
side-authorized non-carrier attempt rejects unchanged                    1

two distinct carrier-derived prepares for the same free next slot:
  each is individually admissible before local service                1/1
  first serviced prepare allocates/registers exactly one slot            1
  competing prepare then rejects without mutation or output              1
```

Thus local allocation does not admit two attempt identities into one slot,
even when competing valid-looking prepares are placed at the admission
boundary.  Existing wrong-capability, replay, cross-attempt decision and exact
evidence-splice cases also continue to reject within the 14/14 battery.

The receiver still does not prove the full remote predecessor wire from the
carried record alone.  That was a separate round-three ancestry ceiling, and
this patch states it directly as
`remote_predecessor_ownership_proof=0` under an
`honest_record_generating_actor_scope=1`.  A Byzantine remote-record theorem
would need additional carried ancestry evidence.  Because the candidate no
longer claims that theorem, this is not a locality-delta finding.

Likewise, supplied fixture construction and birth opportunity remain outside
the online theorem.  The present result is for supplied finite attempts; it
does not derive participant discovery, arbitrary retry opening, or an
unbounded slot law.

## 6. Final disposition

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Final count:** **0B / 0M / 0m / 0n.**

At the declared finite and honest-actor scope, the locality lane now earns:

```text
CLOCK-FREE EXACT-AUTHENTICATED ACTOR-LOCAL HANDLER EXECUTION OF SUPPLIED
FINITE ATTEMPTS ON ONE APPEND-ONLY LEDGER, WITH SERVICE_WORLD EXPLICITLY A
HANDLER-PLUS-TRANSPORT MACRO.
```

This closing result does not promote the open opportunity, arbitration,
failure-recovery, infinite-completion, quantum or spacetime questions.
