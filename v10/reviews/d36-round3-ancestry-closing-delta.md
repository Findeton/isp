# D36 round 3 — ancestry and ontology closing delta

**Frozen target:** commit
`e80ca6af30ff1e6ca83b97e1521d8a335c054850`.

**Prior review:** `reviews/d36-round2-ancestry-closing-delta.md` at
`0B / 2M / 2m / 0n`.

**Lane:** exact-record authentication, carrier-derived attempt identity,
record payload and parent commitments, persistent BORN/TOKEN continuation,
prefix/wire/closure validation, capability provenance, and finite structural-
identity scope.

**Verdict:** **MAJOR REVISION. THE TWO ROUND-TWO MAJORS ARE REPAIRED AS
FORMAL GENERATED-TRACE PROPERTIES, BUT THE CONTINUATION IS ACTOR-LOCAL ONLY
AFTER A PRIVILEGED OPENER DIRECTLY INSTALLS THE NEW ATTEMPT INTO EVERY
PARTICIPANT'S PRIVATE STATE. THE CARRIER-DERIVED ATTEMPT LAW IS THEREFORE A
CONSTRUCTOR CONVENTION, NOT YET A RECORD-GENERATED LOCAL TRANSITION.**

**Count:** **0 blockers / 1 major / 1 minor / 0 nits.**

The repair is substantial.  Exact evidence bytes are now protected, same-base
carrier attempts are separated, and the BORN/TOKEN stale/rebase histories are
genuinely linear append-only DAGs.  The remaining major is not a receipt
failure.  It identifies an unrecorded regional state transition immediately
before the repaired local protocol begins.

## 1. Independent reproduction

I reran the reference under `PYTHONHASHSEED=161803398`, the actor companion
under `PYTHONHASHSEED=314159265` and `271828182`, and the independent replay
checker.  Every process exited zero.  The two actor runs were byte-identical;
the replay checker independently reproduced both executables under seeds `17`
and `104729` and returned `PASS 8/8`.

```text
reference source SHA-256
2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683

reference complete stdout / receipt SHA-256
868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17

reference science SHA-256
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor companion source SHA-256
748128631ff32268a9d0f5c8f74306189a9d371752569e06f87f2a0c2ca0214a

actor companion complete stdout / receipt SHA-256
8ee46d53a1f392222b4e60e10ead369a831661f272120e090a2166985edfcf43

actor companion stdout-body SHA-256
f147e3afd77c81971a86136ebaa8e6add87bb0ce5988f4e5c152d66750757b47

actor companion science SHA-256
c9fb8f5e75fb635f6dade6c2e176959d96a2451465d2813d4afe72ceb757f19d

replay checker source SHA-256
3cbf013bbb1766fbc8e304be33ebcec3d3783f8f5fedc6fc6b7f3a62e7c8ef95

replay checker complete stdout / receipt SHA-256
c69b25e39df2f7ac478643ec2a9716c02ff924c02636fcce6211d0c4d1dee94e

note SHA-256
754225ac748903bd2c7781803ac4b033301b8e92b3be092bc7aaa729964edcf5
```

The actor companion exactly reproduces:

```text
PASS 12/12;
13 / 13 registered attacks rejected;
56 representative terminal ledgers;
297,980 representative coordination-quotient edge deltas;
maximum parent arity 2;
old-base abort 2 / 2;
rebased commit 2 / 2;
same-world prefix preservation 2 / 2;
combined-ledger validation 2 / 2;
old close below new close 2 / 2;
stale-envelope rejection 2 / 2;
combined continuation records 50.
```

`git diff --check e80ca6a^ e80ca6a` is clean.  The committed reference,
companion and replay receipts have the hashes printed above.  No finding below
is numerical drift or nondeterminism.

## 2. Round-two finding dispositions

### M1 — quotient header was used as physical authentication: closed for tamper resistance

`Envelope.authenticated_fields()` now includes the structural attempt ID,
participant response-record binding where applicable, and the exact evidence
`record_id`.  That record ID commits owner, kind, complete payload and every
parent.  The reduced `public_fields()`/`evidence_header()` remains only the
finite coordination-graph label.

I repeated the round-two grant attack exactly: keep the old signature, retain
the same quotient header and payload, but replace the two-parent grant by a
new one-parent record.  The repaired predicates are:

```text
evidence_header_equal=1
record_id_changed=1
authentic=0
handler_accepted=0
actor_and_outputs_unchanged=1
```

The formerly omitted live-version substitution also enters the evidence
record digest and therefore invalidates an unchanged signature.  The old
claim that multiple exact DAG nodes share one physical signature is false at
the frozen target.  This part of round-two M1 is closed.

### M1 — same-base attempts shared identity: closed on generated openings

The attempt label is constructed from exact carrier ID, body, members and
bases.  I independently compared epoch-zero and epoch-one attempts with
identical bodies and bases:

```text
mode    body equal   carrier equal   attempt equal   old decision accepted
BORN        1             0               0                   0
TOKEN       1             0               0                   0
```

The old decision remains correctly signed for its old attempt, but the new
participant rejects it without changing actor state or emitting a record.
Attempt separation and mismatched-earlier-message rejection are therefore
earned for worlds constructed by the frozen opener.

### M2 — two separately initialized histories: closed as a record-DAG defect

`append_rebase_attempt()` now consumes the actual terminal `ActorWorld` and
the same ledger.  It gives the new attempt a distinct transaction owner.  The
BORN carrier descends from the old close; the TOKEN carrier descends from both
its pre-existing dormant slot and the old close.  Subsequent participant
records extend the old participant heads.

My independent reconstruction returned:

```text
mode    old/final records   max arity   prefix exact   old close below new
BORN       13 / 24              2            1                 1
TOKEN      15 / 26              2            1                 1

old participant heads below new close
BORN   (1,1)
TOKEN  (1,1)

validate_terminal_ledger
BORN   (24,2)
TOKEN  (26,2)
```

Both complete ledgers pass parent-before-use, owned-wire and transaction-
closure validation.  Old record bytes remain identical.  The old prepare is
rejected by the final participant without actor or record output.  Thus the
round-two branching-wire and missing-ancestry counterexample is closed.

### m1 — capability and attempt provenance: finite scope is honest, local generation remains open

The note explicitly says ideal authentication, stable capabilities and fixed
attempt bodies are supplied.  It does not promote capability issuance,
participant discovery or opportunity to derived physics.  That appropriately
narrows the round-two provenance criticism.

The new persistent opener nevertheless reveals that supplied attempt data are
installed through an unrecorded multi-actor state change.  This is the new
major in section 3, not a revival of the old remote-tip contradiction.

### m2 — structural identity and cryptographic scope: closed by disclosure

The note now preserves the finite-fixture ceiling: finite structural slots and
cryptographic collision resistance are assumptions, not an equivariant root-
free freshness theorem.  The reference collision/rename battery is not
narrated as mathematical SHA-256 injectivity or an unbounded allocator.  No
new finding is needed on that declared scope.

The older BORN/TOKEN, arity-three and D24 dispositions also remain closed:
the carrier modes agree only on the coordination quotient, their support
ontologies remain explicitly unequal, the actual three-party closure has
arity two, and D24 compatibility means one-parent graph shape rather than an
executed `B_g`/NSE gate.

## 3. MAJOR M1 — the persistent rebase requires a direct regional write into every participant

The repaired ledger is continuous, but the actor transition that opens it is
not local or record-generated.  `append_rebase_attempt()` iterates over all
participants and directly replaces four fields before any actor services an
envelope:

```text
applications       append a new transaction slot;
response_records   append a new response slot;
authorizations     install (tx, attempt, body, base, capability);
mailbox            insert the prepare.
```

For both BORN and TOKEN, exact inspection gives:

```text
participant 0 changed fields
(applications, response_records, authorizations, mailbox)

participant 1 changed fields
(applications, response_records, authorizations, mailbox)

participant heads unchanged                         2 / 2
old/new authorization counts                         1 / 2
participant-owned authorization records appended     0
new ledger record at opening                          T carrier only
```

Mailbox delivery may reasonably be assigned to the network transport.  The
authorization and protocol-slot writes are different: they are private actor
state that changes acceptance behavior, yet no participant click handles
them and no participant record carries them.  The ledger's exact prefix
survives only because these decisive state changes are outside the ledger.

This write is essential, not redundant bookkeeping.  I retained the new
application/response slots and exact signed carrier, but restored only the old
authorization tuple.  The already carried stable route capability was still
present.  Both modes returned:

```text
stable_capability_present=1
without_direct_new_authorization_accepts_prepare=0
output_records=0
```

Therefore the current local record law cannot open the new attempt from the
stable capability and carrier.  A regional constructor first tells every
participant the complete attempt identity it will later be asked to validate.

The same side table also carries the alleged carrier derivation.  Neither
`participant_accepts_prepare()` nor `validate_terminal_ledger()` recomputes

```text
attempt_id = digest(carrier.record_id, body, members, bases).
```

I replaced the attempt with the literal `NOT-CARRIER-DERIVED`, installed the
matching authorization, and issued exactly signed prepares over the unchanged
valid carrier.  The normal handlers closed both histories and the full ledger
validator passed:

```text
mode    attempt matches carrier formula   closed   ledger valid   versions
BORN                 0                       1        (13,2)         (1,1)
TOKEN                0                       1        (14,2)         (1,1)

close payload attempt, both modes = NOT-CARRIER-DERIVED
```

This is not a hash collision.  It proves that “carrier-derived” is guaranteed
only by the privileged Python opener, not by the accepted record grammar,
participant rule or terminal proof.  Generated traces pass because the global
constructor pre-installs the answer.

The note's statement that fixed attempt bodies are supplied honestly exposes
some external data.  It does not disclose that supplying them is implemented
as a simultaneous mutation of every participant's private acceptance state.
Consequently the frozen result may be called:

> actor-local servicing **conditional on a supplied regional attempt-
> installation oracle**;

but not an actor-local append-only continuation without that qualifier.

**Required repair:** choose and execute one of two physical openings.

1. If a stable capability authorizes future attempts in its lineage, let each
   participant validate the exact carrier, its own role, body/base claim and
   carrier-derived attempt formula locally when the prepare arrives.  Allocate
   attempt bookkeeping lazily.  The opener may birth the carrier and send
   messages, but may not alter participant authorization or application state.
2. If every attempt needs fresh consent, deliver that consent as authenticated
   causal evidence to each participant.  Each participant must process it in
   its own event and append an immutable authorization/scope record before the
   prepare becomes admissible.

In either design, add gates that (a) start from the exact old terminal actors,
(b) open the new attempt without direct participant replacement, (c) reject a
non-carrier-derived attempt even if other message fields agree, and (d) retain
the current prefix, wire, closure and stale-message validations.

## 4. MINOR m1 — exact authenticity is not receiver-side DAG admissibility

The repaired signature proves which exact record an envelope carries.  It does
not prove that the record occupies a valid position on its claimed owner's
wire.  Receiver handlers have no ledger argument and generally validate only
the cross-wire parent relevant to their transaction.

I constructed an exactly valid `P0` grant with two existing parents, but used
the `P1` seed rather than the `P0` head as its first parent.  I then signed that
exact record with the ideal `P0` key.  The frozen predicates were:

```text
valid_record=1
all_parents_exist=1
authentic=1
transaction_accepts_response=1
handler_accepted=1
actor_mutated=1
output_records=1
validate_owned_wires=FAIL
```

The unchanged-signature network attacker from round two cannot create this
record; exact authentication correctly defeats that attacker.  This fresh
case instead requires a faulty or equivocating authenticated sender.  The
frozen generated-trace theorem uses correct actor handlers, so I do not grade
it as another major.  It does establish a necessary scope boundary:

```text
authenticated exact bytes != independently validated causal provenance.
```

State explicitly that safety and ancestry assume honest record-generating
actors, not merely failure-free delivery plus authentication.  If D36 intends
receiver-side protection against a malformed authenticated sender, the repair
must carry a locally checkable wire/ancestry proof or validate exact evidence
against an admitted causal record store before actor mutation.  The present
`13/13` battery does not include an exactly re-signed wrong-wire predecessor.

## 5. What is now earned

The round-three repair earns the following exact statement:

- exact evidence IDs, hence complete parents and payloads, are protected
  against post-signature substitution;
- generated carrier attempts have distinct structural labels even at equal
  bodies and bases;
- earlier-attempt decisions do not advance a later generated attempt;
- BORN and TOKEN each continue one prior actor value and one ledger rather
  than unioning independent histories;
- both continuation ledgers preserve old bytes, linear owned wires, bounded
  parent arity and full old-close ancestry;
- participant histories genuinely continue from the old terminal heads;
- the BORN/TOKEN equality remains a coordination quotient only, not an
  ontology identity;
- the graph and terminal counts remain explicitly representative quotient
  lifts rather than all record histories; and
- opportunity, participant discovery, capability issuance, arbitration,
  failures, unbounded completion and quantum realization remain open.

The strongest supported headline before M1 is repaired is:

> **Clock-free actor-local servicing of supplied finite attempts, with exact
> append-only record lifts and persistent two-attempt DAGs, conditional on an
> external regional attempt-installation oracle and honest record-generating
> actors.**

That is a real advance over the round-two target, but it is narrower than
`CLOCK-FREE ACTOR-LOCAL APPEND-ONLY COORDINATION REFINEMENT` without
qualification.

## 6. Final disposition

**Fresh exact counterexamples:** **2 classes**.

```text
B  blockers  0
M  majors    1   direct unrecorded multi-participant authorization opening
m  minors    1   exact authentication does not validate sender-wire placement
n  nits      0
```

**Final count:** **0B / 1M / 1m / 0n.**

**Decision:** **MAJOR REVISION.**  Close the round-two evidence-substitution
and disconnected-continuation findings.  Retain the repaired signatures,
attempt separation and continuous ledgers.  Before closing D36's actor-local
claim, replace the direct authorization-table installation with a local
record-generating opening rule, or explicitly demote the result to a protocol
that begins only after a supplied nonlocal regional oracle has installed each
attempt.
