# D36 round 3 — locality closing delta

**Frozen target:** commit
`e80ca6af30ff1e6ca83b97e1521d8a335c054850`.

**Round-two baseline:**
`reviews/d36-round2-locality-closing-delta.md` at `1B / 1M / 1m / 1n`.

**Lane:** exact evidence and attempt authentication, historical-message
rejection, persistent actor/ledger continuation, participant-local opening,
owned-wire and closure ancestry, quotient wording and G20 provenance.

**Verdict:** **THE ROUND-TWO AUTHENTICATION BLOCKER AND RECORD-LEDGER
CONTINUATION FAILURE ARE CLOSED.  THE DELTA IS NOT FULLY CLOSED BECAUSE THE
REBASE OPENING DIRECTLY INSTALLS NEW AUTHORIZATIONS AND STATE SLOTS IN EVERY
PARTICIPANT WITHOUT A PARTICIPANT EVENT OR RECORD.**

**Count:** **0 blockers / 1 major / 1 minor / 0 nits.**

The repair is materially sound where it says it is cryptographic and
append-only.  Exact evidence identity is now outside the reduced graph key but
inside the authenticated statement, carrier-derived attempt IDs separate
same-body retries, and the two attempts now share one real ledger.  The one
remaining locality defect occurs one step earlier: the helper that opens the
second attempt rewrites participant-owned predictive state globally before
any mailbox handler runs.  A smaller event-granularity issue also remains:
`service_world` combines one local handler event with immediate delivery into
all recipient-owned mailboxes, so a simulator service step does not literally
change only one actor object.

## 1. Exact independent reproduction

I reran the reference, actor companion and external replay checker from the
frozen tree under `PYTHONHASHSEED=2718281`.  They return `PASS 22/22`,
`PASS 12/12` and `PASS 8/8`, respectively.  The committed hashes are:

```text
reference source  2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683
reference stdout  868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17
reference science a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source      748128631ff32268a9d0f5c8f74306189a9d371752569e06f87f2a0c2ca0214a
actor stdout      8ee46d53a1f392222b4e60e10ead369a831661f272120e090a2166985edfcf43
actor science     c9fb8f5e75fb635f6dade6c2e176959d96a2451465d2813d4afe72ceb757f19d

replay source     3cbf013bbb1766fbc8e304be33ebcec3d3783f8f5fedc6fc6b7f3a62e7c8ef95
replay stdout     c69b25e39df2f7ac478643ec2a9716c02ff924c02636fcce6211d0c4d1dee94e
note              754225ac748903bd2c7781803ac4b033301b8e92b3be092bc7aaa729964edcf5
```

The finite graph counts remain unchanged.  The revised exact gates report:

```text
authentication/replay attacks                         13 / 13 rejected
same-world stale attempts                               2 / 2 closed abort
same-world rebased attempts                             2 / 2 closed commit
old ledger prefixes preserved                           2 / 2
combined ledgers valid                                  2 / 2
old close below new close                               2 / 2
old envelope rejected after rebase                      2 / 2
combined continuation records                              50
```

Independent direct calls reproduce

```text
adversarial_gate  (13,13)
continuation_gate (2,2,2,2,2,2,2,50,
  098f4bd1ea3eb78371b50f23b6cc97bd4e49436a8e8fbc4ed48a3fa32d3ac5a3).
```

## 2. Round-two finding disposition

### B1 — exact record/attempt authentication: closed

`Envelope.public_fields()` remains the intentionally reduced coordination
label.  It is no longer the authenticated statement.  The separate
`authenticated_fields()` binds:

```text
sender and target;
transaction and participant indices;
body, base and stable capability;
carrier-derived attempt ID;
participant response-record ID;
exact evidence record ID; and
application code.
```

Because a record ID commits the complete owner/kind/parent/payload tuple,
changing a parent or an omitted quotient payload field changes the signed
statement.  `authentic` is deliberately no longer cached on the dataclass's
reduced comparison key, avoiding a false cache hit between quotient-equal
envelopes.

The attempt ID is derived from the exact carrier record, body, members and
bases.  It is carried by the authorization, promise, response, decision,
application and acknowledgement path.  Participants retain their exact
response record and require the decision envelope to bind it.

I repeated the round-two same-base and evidence-splice attacks and added
decision-commitment, response-ID and carrier splices.  The exact observations
were:

```text
same body across epoch-zero/epoch-one carriers                  1
same carrier                                                    0
same attempt ID                                                 0
same commit envelope ID                                         0
same commit signature                                           0
old commit accepted by new-attempt participant                  0
old-commit rejection left actor/output unchanged                1

nonexistent-parent decision has same public fields              1
nonexistent-parent decision remains authentic                   0
nonexistent-parent decision accepted                            0
rejection left actor/output unchanged                           1

changed response commitment has same public fields              1
changed response commitment remains authentic                   0
changed response commitment accepted                            0

changed response-record ID has same public fields               1
changed response-record ID remains authentic                    0
changed response-record ID accepted                             0

prepare carrier-parent splice remains authentic                 0
prepare carrier-parent splice accepted                          0
```

The signature is an ideal-authentication abstraction rather than a deployed
cryptosystem, as declared.  Within that abstraction, the previous blocker is
closed.

### M1 — one append-only continuation: ledger mechanics closed; actor-local opening remains open

The old two-fresh-world union has been removed.  The stale attempt is serviced
to quiescence, and `append_rebase_attempt` receives that terminal
`ActorWorld` and the same ledger.  The new carrier descends from the old close;
TOKEN uses a dormant slot that was already in the ledger.  The old transaction
object remains, participant heads/used sets/capabilities remain, and the new
participant records descend from the old participant heads.

My independent reconstruction confirms, for both BORN and TOKEN:

```text
old transaction retained                                      1
old ledger bytes preserved                                    1
owned wires valid immediately after carrier opening           1
combined terminal ledger valid                                1
old close below new close                                     1
old used sets are subsets of final used sets                  1
```

This closes the round-two branching-wire, multiple-root and missing-ancestry
counterexamples.  Section 3 isolates the different opening that remains.

### m1 — quotient representative wording: closed

The receipt now says

```text
every_representative_edge_emits_checked_record_delta=1
one_complete_append_only_ledger_per_terminal_quotient_state=1.
```

The note explicitly says that 56 ledgers and 297,980 checks are path lifts of
coordination-quotient states/edges rather than a census of all full causal
histories.  It also retains same-transaction order histories as potentially
physical and makes no new gauge claim.

The old separating probe still returns:

```text
reference projection equal                         1
ActorWorld equal under quotient comparison          1
full ledgers equal                                  0
decision record IDs equal                           0
commit envelope IDs equal                           1
```

That is now the disclosed scope, not a counterexample to the wording.

### n1 — G20 provenance: closed

The reference output now prints `static_scope_assertion=1` on G20.  It does
not present the literal crash/fairness pair as an executed loss trace.  The
round-two provenance nit is closed.

## 3. MAJOR M1 — rebase opening mutates participant-owned predictive state without local events

`append_rebase_attempt` is not merely a transaction birth plus message
delivery.  It loops over every participant and directly replaces three pieces
of participant-owned state:

```text
applications       append a new transaction slot;
response_records   append a new transaction slot;
authorizations     append (tx, attempt, body, base, capability).
```

It then inserts the prepare directly into each participant mailbox.  The only
record appended during this opening is the T-owned carrier.  No participant
handler runs and no participant-owned authorization/opening record is
created.

The authorization insertion is operational rather than inert bookkeeping.
I froze the old terminal participant, called the opening helper, and compared
the returned participant with an otherwise identical copy in which only the
new authorization tuple was removed.  For both BORN and TOKEN the opening
has the exact census:

```text
ledger records added by opening                               1
owner kind of every added record                              T
participant head preserved                                   1
participant used set preserved                               1
participant stable capabilities preserved                    1
authorization tuple delta                                    +1
application-slot delta                                       +1
response-record-slot delta                                   +1
mailbox delta                                                 +1
new prepare capability already present before opening         1
```

The controlled prediction test is decisive:

```text
same full record ledger                                       1
same head, capability, used set and mailbox                   1
all participant fields except authorization equal             1
signed prepare accepted with injected authorization            1
same signed prepare accepted without injected authorization    0
```

Thus two states with the same append-only record history, same carried stable
capability and same incoming signed carrier message predict different next
events solely because a global helper changed an unrecorded local tuple.  The
stable capability is not sufficient in the implemented law; the hidden
installation is essential.

This does not reopen the authentication blocker or invalidate the completed
single-attempt traces.  It does prevent promotion of the stronger statement
that the stale/rebase history is generated entirely by actor-local,
record-native transitions.  At present it is:

```text
one persistent record ledger plus a supplied nonlocal participant-
authorization installation, followed by actor-local mailbox execution.
```

The general birth opportunity law is already declared open, but that ceiling
does not make an undisclosed multi-participant state rewrite local.  It may be
retained as a regional opening oracle only if named as such in the earned
claim.

### Required closure gate for M1

Choose one explicit architecture and test it:

1. **Capability-derived opening:** the participant's already carried stable
   route capability plus authenticated carrier lineage suffices to validate a
   new attempt, so the global helper does not add an authorization tuple; or
2. **Recorded authorization:** each participant services a typed local
   authorization/opening envelope, appends its own bounded record and only
   then admits the prepare.

In either architecture, the pre-delivery opening operation must leave every
participant-owned predictive field unchanged.  Allocation of a new
application/response slot must likewise be derived or installed by that local
event rather than by simultaneous tuple extension.  Add an exact gate that:

- snapshots every participant before carrier birth;
- permits the environment to add only T-owned carrier/network data;
- proves no participant field changes before its addressed local service;
- proves the same prepare is not toggled solely by unrecorded side state; and
- reruns prefix, parent-before-use, owned-wire and old-close ancestry checks.

## 4. What is earned at round-three strength

## 4. MINOR m1 — `service_world` is a local-handler plus network-delivery macro

`handle_participant` and `handle_transaction` each receive and return only one
addressed actor.  That important round-one repair survives.  The full
`service_world` transition is coarser: after replacing the addressed actor, it
calls `append_to_target` for every outgoing envelope.  Because mailboxes are
fields of `ParticipantActor` and `TransactionActor`, those deliveries change
additional actor objects in the same returned `ActorWorld`.

I counted actor-object changes along a normal single-transaction commit:

```text
service                         changed P actors   changed T actors   total
P0 handles PREPARE                    (0)                (0)            2
P1 handles PREPARE                    (1)                (0)            2
T handles first response               ()                (0)            1
T handles final response/decision    (0,1)               (0)            3
P0 handles COMMIT                      (0)                (0)            2
```

The remote changes are mailbox insertions, not reads or durable
version/promise/application changes.  Therefore this is not a new safety
major.  It does mean that the literal invariant “one addressed actor changes
per service event” and the receipt phrase
`network_only_selects_addressed_mailbox=1` are too strong for the current
transition granularity: the driver also transports outgoing envelopes into
other owned mailboxes.

Close this minor either by separating handler execution from explicit
network/delivery transitions (with in-flight envelopes owned by the network),
or by naming `service_world` a transport macro and restricting the one-actor
claim to the handlers/durable actor fields.  No graph result should change
under the straightforward refinement.

## 5. What is earned at round-three strength

The following statements now survive this hostile lane:

- exact evidence records and carrier attempts are authenticated separately
  from the coordination quotient;
- same-body/same-base historical decisions do not cross attempts;
- the registered and extended evidence substitutions reject before actor
  mutation or output creation;
- after the rebase authorization is installed, both attempts execute on one
  persistent actor world and one append-only, linear, ancestry-complete
  ledger;
- each handler reads and mutates only its addressed actor, although the
  enclosing service macro also delivers outgoing envelopes into other
  mailboxes;
- the old ledger prefix, heads, used sets and stable capabilities persist;
- the receipt accurately labels representative quotient edges and terminal
  path lifts; and
- G20 accurately labels its static scope.

## 6. Final disposition

```text
B  blockers  0
M  majors    1   continuation opening globally installs unrecorded participant state
m  minors    1   service macro changes addressed actor plus recipient mailboxes
n  nits      0
```

**Final count:** **0B / 1M / 1m / 0n.**

The full candidate noun

```text
CLOCK-FREE ACTOR-LOCAL APPEND-ONLY COORDINATION REFINEMENT /
FAILURE-FREE CLOSED ATTEMPTS
```

is earned for each already supplied and participant-authorized attempt, but
not yet for the transition that opens the continuing attempt.  The strongest
closing statement is:

```text
CLOCK-FREE EXACT-AUTHENTICATED ACTOR-LOCAL EXECUTION OF SUPPLIED FINITE
ATTEMPTS ON ONE APPEND-ONLY LEDGER / CONTINUATION OPENING STILL REQUIRES AN
UNRECORDED REGIONAL AUTHORIZATION ORACLE.
```

No change to arbitration, probability, quantum or spacetime machinery is
needed to decide the remaining opening.  It is a finite causal-locality test.
