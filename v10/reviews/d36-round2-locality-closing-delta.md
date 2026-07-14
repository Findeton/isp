# D36 round 2 — locality closing delta

**Frozen target:** commit
`63314a24cfd181793034763fcec9fdb701ddb6b2`.

**Round-one baseline:**
`reviews/d36-round1-locality-hostile.md` at `0B / 1M / 2m / 1n`.

**Lane:** actor ownership, authenticated causal evidence, append-only record
histories, continuation, construction-order gauge, failure/visibility scope and
receipt provenance.

**Verdict:** **DELTA NOT CLOSED.  THE OWNED-MAILBOX REFINEMENT REMOVES THE
ROUND-ONE CROSS-OWNER READS, BUT ITS SIGNATURE DOES NOT AUTHENTICATE THE EXACT
CAUSAL RECORD OR ATTEMPT, AND ITS TWO-EPOCH EXHIBIT IS NOT ONE CONTINUING
APPEND-ONLY ACTOR WORLD.**

**Count:** **1 blocker / 1 major / 1 minor / 1 nit.**

This is not a rejection of the finite fail-fast reference semantics.  The
reference result still passes, and the companion is a substantial architectural
repair: normal handlers now receive only one owned actor and one addressed
envelope.  The closing failure is sharper.  The object advertised as the
signed predecessor is mutable outside the signature, and the only
continuation gate reinitializes the actors whose persistence it is meant to
test.

## 1. Exact independent reproduction

I reran all three frozen executables under `PYTHONHASHSEED=2718281`.  The
reference printed `PASS 22/22`, the actor companion printed `PASS 12/12`, and
the external replay checker printed `PASS 8/8`.  The committed artifact hashes
are:

```text
reference source  dad183c2e303b0315fa7f452ab1c197569d6983332696421d70f04ba5b3d0743
reference stdout  3478d1447ee54a33599d9d1e3b00b63cfa323ed7df1a44e3915b13da62545093
reference science a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source      5813304446d267dc3d08f520f4db991bf6bdb94ae45b1f96a5e0cc2a094996ba
actor stdout      8e2e9b9ad6de8ad7ebef4554c2eef32f20b1ffead33a7af6f89f6251e0d8b41d
actor science     ab275cc69ef529bceba96c7cb484232a5c4b661e9cd1a902c695067bd04193a4

replay source     878f0a1daa08db30974bf06e7075a9952faa18d569d74286eea2ed51011f2ec6
replay stdout     b89689d1570e2bb50a101dabb50c6390c1a6d2f08bef8bcd2844b5c505882313
note              8fee0c339f9a279f0659c71c45bc3adb5743925f9ea1e0a22d00eb941eaf1d0b
```

The companion reproduces the registered finite counts exactly:

```text
pair       1,113 states /   2,984 edges /  8 terminals per carrier mode
triangle  34,637 states / 140,028 edges / 17 terminals per carrier mode
disjoint     289 states /     816 edges /  1 terminal  per carrier mode
partial    1,517 states /   5,162 edges /  2 terminals per carrier mode

terminal ledgers                         56
combined representative edge checks     297,980
registered attacks                       8 / 8 rejected
disjoint two-service diamonds            4 / 4 commuting.
```

Those numbers are reproducible.  The findings below concern what they
establish, not receipt drift.

## 2. Round-one finding disposition

### M1 — actor-local/authenticated record refinement: partially repaired, not closed

The shared-state implementation criticism is repaired.  `ParticipantActor`
and `TransactionActor` own separate mailboxes and state, and the normal
participant/transaction handlers receive no live remote actor.  The global
driver selects an addressed mailbox and transports outgoing envelopes; it
does not inspect remote state on behalf of a handler.  This earns logical
actor ownership at the finite simulator level.

The authentication and causal-evidence half is not repaired.  B1 below is a
direct successful mutation attack against the advertised signed predecessor
record.

### m1 — fixed one-batch/version-zero scope: wording closed; continuation claim not closed

T1 is now explicitly pinned to a supplied fixed batch and the base checker no
longer claims an online theorem.  That part closes.  The companion adds a
stale/rebase row, but M1 below shows that it is two independent runs joined as
sets, not a continuation of one actor world.

### m2 — safety/failure/visibility noun: wording closed

The repaired verdict says `FAILURE-FREE CLOSED ATTEMPTS`, and the note defines
the longer safety predicate.  It explicitly excludes linearizable multiwire
visibility, crash recovery, starvation freedom and an unbounded online
theorem.  Partial application remains visible.  This closes the dangerous
headline ambiguity.

The requested executable post-grant and post-first-application loss witnesses
were not added; the base G20 still returns a literal finite scope pair.  I
retain only n1 below because the final noun is now accurate and the negative
result itself was already exact in round one.

### n1 — status/gate provenance: substantially closed

The note status now says repairs executed and hostile delta required.  G21 is
nonvacuous, and the separate two-process checker verifies both executables
under two hash seeds against committed receipts.  Only the static G20
classification remains as a presentation nit.

## 3. BLOCKER B1 — the signature does not bind the causal record or the attempt

The note says each envelope carries a **signed predecessor record**.  In the
executable, the signature protects only `evidence_header(record)`.  That
header contains owner, kind and a reduced payload.  It omits
`record.record_id` and every parent.  For grant, reject, apply and release it
also removes the fourth payload field.  `Envelope.evidence` itself is marked
`compare=False, hash=False`.

Consequently a sender's unchanged signature authenticates multiple distinct
record DAG nodes.  This is not merely quotient presentation: the receiver
uses the unprotected evidence record ID as a parent of its next durable
record.

The attempt binding is also absent:

- `body_digest` contains logical transaction, members and bases, but not the
  carrier record or carrier epoch;
- `capability_id` contains transaction index, participant index and name, but
  not an attempt;
- participant authorizations contain transaction, body, base and capability,
  but not an attempt; and
- `participant_accepts_decision` validates the decision kind and body but does
  not require it to descend from the carrier or from this participant's grant.

### 3.1 Exact same-base cross-attempt replay

I independently opened two legitimate `single/BORN` attempts at participant
versions `(1,1)` and bases `(1,1)`, differing only in carrier epoch.  I
serviced both prepares and grants to the point where each transaction had
issued commit decisions.  The exact result was:

```text
body_equal                                      1
carrier_equal                                   0
capabilities_equal                              1
commit_envelope_ids_equal                       1
commit_evidence_ids_equal                       0
epoch0_commit_accepted_by_epoch1_participant     1
epoch0_commit_mutated_epoch1_participant         1
```

The old decision envelope is not recognized as old because the alleged
attempt identity is outside every protected acceptance field.

### 3.2 Exact evidence-splice attack

I then took a legitimate epoch-one commit envelope and replaced only its
evidence with a newly self-consistent `DECISION_COMMIT` record whose sole
parent was the nonexistent string `NONEXISTENT`.  I retained the original
signature.  The frozen checker returned:

```text
splice_evidence_id_changed              1
splice_signature_unchanged              1
splice_authentic                        1
splice_valid_record                     1
splice_decision_accepted                1
application_names_spliced_parent        1
```

`valid_record` proves only that the replacement record hashes itself; it does
not prove that its parent exists in the receiver's causal history.  The
participant therefore mutates its version/promise state and constructs an
application naming the attacker's substituted decision.  A later ledger
append would detect the missing parent, but the actor has already mutated.
That directly contradicts `reject_before_durable_mutation` for an alteration
of a purportedly authenticated field.

The registered `8/8` battery flips a signature or changes a protected base,
but never substitutes the evidence record or replays a valid same-body/base
decision across attempt carriers.  It therefore does not cover this attack
class.

### Required closure gate for B1

1. Give every attempt an explicit structural ID derived from the exact
   carrier record, body and bases.
2. Bind that attempt ID into capabilities/authorizations and every envelope
   and record in the attempt.
3. Sign the exact evidence `record_id` and its relevant parent commitment, not
   only a reduced coordination header.
4. Have each participant retain its active attempt and grant record and accept
   a decision only when the decision certificate binds that attempt/grant.
5. Reject evidence substitution before any actor field changes or output
   record is created.
6. Add exact attacks for parent/record-ID substitution, old decision replay,
   old grant splice and a same-base retry in one persistent actor world.

The reduced header may remain as the **coordination quotient key**.  It cannot
also be the cryptographic statement that authenticates full causal evidence.

## 4. MAJOR M1 — the two-epoch gate is not an append-only continuation

`continuation_gate` calls `run_policy` twice.  Each call invokes
`open_actor_world`, recreates participant seeds, mailboxes, `used` sets,
capabilities and transaction actors from scratch.  The gate then unions the
two completed ledger dictionaries and appends `REBASE_LINK`.  No actor from
the old run becomes the actor supplied to the new run.

I reconstructed exactly that combined object for BORN and TOKEN and applied
the companion's own `validate_owned_wires` and ancestry functions.  Both modes
failed:

```text
mode   old final versions   new run initial   new final   owned-wire check
BORN       (1,1)                (1,1)           (2,2)     FAIL
TOKEN      (1,1)                (1,1)           (2,2)     FAIL

participant-0 seed children, each mode                         2
participant-1 seed children, each mode                         2
T-owner roots, each mode                                       2
REBASE_LINK same-owner parents, each mode                       2
records required but absent below new close        12 BORN / 13 TOKEN
```

For BORN the two T roots are two `T0_BIRTH` records.  For TOKEN they are two
`DORMANT_SLOT` records.  `REBASE_LINK` itself violates the validator's
one-same-owner-parent rule, and it is appended *after* the new close, so it
cannot repair the new close's ancestry.  The missing old branch includes the
old reject/release/abort/close records.

The receipt's `combined_records=52` is honest set-union arithmetic.  It is not
evidence of one linear owned history, because `continuation_gate` never calls
`validate_owned_wires(combined)` or validates the new close against the
combined transaction history.

### Required closure gate for M1

Add a continuation API whose input is the prior `ActorWorld` and ledger.  The
rebased participant events must descend from their actual prior heads; the new
transaction attempt must have one admitted same-owner predecessor; used
envelopes and capability state must persist; and the combined ledger must pass
parent-before-use, immutable-prefix, owned-wire and closure-ancestry checks.
Run stale rejection followed by rebase/commit in that one world.  A same-base
retry should be included because it also exercises B1's attempt binding.

Until then the online result is only:

```text
two separately initialized finite attempts can be related afterward by a
bounded record;
```

not:

```text
one append-only actor system continues across attempts.
```

## 5. MINOR m1 — the graph enumerates quotient representatives, not all record histories

The receipt is commendably explicit that `actor_graph` is a coordination
quotient and that it replays one complete ledger per terminal quotient state.
However, the labels `actor_states`, `actor_edges` and “every edge” are easy to
read as a census of the full actor-history process.

They are not.  `actor_graph` memoizes only `ref.FFState`.  Several causal
record fields are excluded from dataclass comparison.  I serviced the two
grant responses of one transaction in opposite orders and obtained:

```text
reference_projection_equal                 1
ActorWorld_equal_under_declared_compare     1
full_ledgers_equal                          0
decision_record_ids_equal                   0
commit_envelope_ids_equal                   1
both_ledgers_wire_valid                     1
```

This order is internal to one transaction actor, so it is not among the four
proved disjoint two-service gauge diamonds.  The `56` replayed ledgers are one
path lift for each terminal coordination state, not all full record histories,
and the `297,980` checks are representative quotient-edge deltas.

That can be a legitimate verification strategy, but it needs one of two
precise ceilings: either rename the counts and state that the full history
family is unenumerated, or prove that the quotient is a congruence with a
valid path lift from every hidden history representative.  If same-actor
response order is declared construction gauge, prove that separately at the
full-ledger observable level; otherwise retain the distinct physical record
histories.

## 6. NIT n1 — G20 remains a scope assertion rather than an executed loss control

The failure wording is now correct, so this is no longer a safety-noun
finding.  For receipt provenance, however, `crash_blocking_gate` still returns
the literal pair `(1,0)`.  The promised post-grant blocking and
post-first-application partial-visibility controls are not generated by the
current executable.  Label G20 as a static/symbolic scope assertion or add
the two tiny transition witnesses.

## 7. What survives this delta

The following repairs pass this lane:

- the reference executable is correctly downgraded and still passes `22/22`;
- normal participant and transaction handlers no longer read another live
  actor's state;
- actor-owned addressed mailboxes replace the global bare-message table;
- honest generated traces project exactly to the finite reference semantics;
- each of the 56 representative terminal ledgers is immutable, parent-closed
  and linear within its one-attempt replay;
- the four specifically declared disjoint two-service swaps commute in both
  world and ledger;
- BORN and TOKEN agree on the audited coordination quotient while differing
  in full support records; and
- the final failure, visibility, arbitration, opportunity, quantum and
  unbounded-horizon qualifiers are now appropriately narrow.

## 8. Final disposition

```text
B  blockers  1   exact evidence and attempt identity are outside signature
M  majors    1   two-epoch gate reinitializes actors; combined wires fail
m  minors    1   representative coordination quotient is not full history census
n  nits      1   G20 loss/failure row remains a literal scope assertion
```

**Final count:** **1B / 1M / 1m / 1n.**

The repaired candidate verdict

```text
CLOCK-FREE ACTOR-LOCAL APPEND-ONLY COORDINATION REFINEMENT /
FAILURE-FREE CLOSED ATTEMPTS
```

is not yet earned as a whole.  The strongest exact closing statement is:

```text
CLOCK-FREE ACTOR-OWNED MAILBOX IMPLEMENTATION OF THE FINITE COORDINATION
QUOTIENT / HONEST GENERATED CLOSED ATTEMPTS; AUTHENTICATED CAUSAL EVIDENCE AND
PERSISTENT CONTINUATION NOT YET ESTABLISHED.
```

The path to closure is short and concrete: bind signatures to exact evidence
and structural attempt IDs, then rerun stale/rebase in one persistent world
whose combined ledger passes the existing validators.  No probability or
quantum machinery is needed to decide those two gates.
