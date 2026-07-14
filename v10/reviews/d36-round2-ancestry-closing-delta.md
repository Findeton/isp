# D36 round 2 — ancestry and ontology closing delta

**Frozen target:** commit
`63314a24cfd181793034763fcec9fdb701ddb6b2`.

**Prior review:** `reviews/d36-round1-ancestry-hostile.md` at
`5f6cd7fccb6e34991bccd10fa1aa7992ebd0a393`.

**Lane:** exact record authentication and ancestry, logical versus attempt
identity, three-party bounded closure, independent BORN/TOKEN openings,
coordination quotient versus ontology, stale/rebase continuation, append-only
owned wires, D24 scope, and finite structural identity.

**Verdict:** **MAJOR REVISION. THE SINGLE-ATTEMPT ACTOR/RECORD REFINEMENT AND
THE BORN/TOKEN COORDINATION QUOTIENT ARE NOW SUBSTANTIALLY EARNED, BUT THE
SIGNED ENVELOPE DOES NOT AUTHENTICATE THE EXACT CARRIED RECORD AND THE CLAIMED
TWO-EPOCH CONTINUATION IS TWO DISCONNECTED RUNS.**

**Count:** **0 blockers / 2 majors / 2 minors / 0 nits.**

The round-one ontology, append-only-history, remote-tip and arity findings are
repaired at the declared single-attempt coordination scope.  Two fresh exact
counterexamples prevent closure.  They do not overturn the finite P4 control
semantics, but they do defeat the stronger authenticated-record and
continuation claims in the candidate verdict.

## 1. Independent reproduction

Fresh companion runs under

```text
PYTHONHASHSEED=314159265
PYTHONHASHSEED=271828182
```

both exited zero and were byte-identical to the committed receipt.  A fresh
reference run under `PYTHONHASHSEED=161803398` was likewise byte-identical.
The independent replay/integrity executable also reproduced `PASS 8/8`.

```text
reference source SHA-256
dad183c2e303b0315fa7f452ab1c197569d6983332696421d70f04ba5b3d0743

reference complete stdout / receipt SHA-256
3478d1447ee54a33599d9d1e3b00b63cfa323ed7df1a44e3915b13da62545093

reference science SHA-256
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor companion source SHA-256
5813304446d267dc3d08f520f4db991bf6bdb94ae45b1f96a5e0cc2a094996ba

actor companion complete stdout / receipt SHA-256
8e2e9b9ad6de8ad7ebef4554c2eef32f20b1ffead33a7af6f89f6251e0d8b41d

actor companion stdout-body SHA-256
aff1bda30fdd4d7841a8bb248c8623c9ca2926c135bb3bf235b32cf6c58771d6

actor companion science SHA-256
ab275cc69ef529bceba96c7cb484232a5c4b661e9cd1a902c695067bd04193a4

replay checker source SHA-256
878f0a1daa08db30974bf06e7075a9952faa18d569d74286eea2ed51011f2ec6

replay checker receipt SHA-256
b89689d1570e2bb50a101dabb50c6390c1a6d2f08bef8bcd2844b5c505882313
```

The companion reproduces `PASS 12/12`, all four reference projections, `56`
terminal ledgers, maximum ledger size `39`, maximum parent arity two, four
disjoint-service diamonds, eight registered authentication/replay rejections,
and the printed BORN/TOKEN ontology inequality.  `git diff --check
63314a2^ 63314a2` is clean.  The findings below are therefore interpretation
and adversarial-coverage failures, not nondeterministic receipt failures.

## 2. Round-one dispositions

### M1 — decorated born/token identity: closed at the newly stated quotient

BORN and TOKEN now begin from different pre-proposal types and use independent
opening relations: BORN emits `T0_BIRTH`; TOKEN starts with `DORMANT_SLOT` and
emits `SLOT_ACTIVATION`.  Both independently generate the actor graph for the
pair, triangle, disjoint and partial-overlap fixtures.  The edgewise projections
match the reference exactly in all four cases.

The candidate also makes the essential limitation explicit:

```text
coordination_projection_equal_all_fixtures=1
full_support_record_algebra_equal=0
```

Thus it earns finite-horizon **coordination-quotient equivalence**, not record-
ontology equivalence.  Fresh support and dormant activation remain physically
distinguishable when support records are observable.  That is an honest and
useful result; the old bisimulation overclaim is closed.

### M2 — mutable summary instead of immutable history: closed for one supplied attempt

The companion now appends immutable typed `Record` objects on participant and
transaction wires.  Every accepted graph edge emits a checked record delta.
For one representative path to each of the `56` terminal coordination states,
the replay verifies parent existence before append, prefix immutability, linear
owned wires and complete transaction ancestry below `Close(T)`.  Grant,
rejection, apply and release records persist.  This connects the P4 actor
transitions to actual record histories and closes the round-one major at that
declared scope.

The exact scope matters: the graph quotients away full evidence records and
the receipt replays one ledger per terminal quotient state, not every distinct
causal presentation of every quotient path.  The new envelope failure in M1
below shows why those two layers must remain separate.

### M3 — remote exact tips in `tau`: closed at the supplied-capability scope

`logical_tau` now contains the initiator seed, bounded transaction slot,
participant roles and stable capabilities, not every participant's exact
current record tip.  Requested base versions enter the fixed attempt body;
actual current participant records arrive in later grant/reject evidence.
The note also separates stable logical lineage from a version-bound attempt.
This removes the direct causal contradiction in the old `tau` construction.

It is not a derivation of capabilities or a root-free identity law.  The note
correctly lists ideal authentication, capabilities and fixed attempt bodies as
supplied physics.  The residual wording issue is recorded as m1 below.

### M4 — parent arity at transaction arity three: closed

The reference's arity-three success closure is now an explicit 25-record
bounded merge construction: all 24 earlier records lie below `Close(T)` and
the maximum parent arity is two.  The actor companion separately runs the
actual three-participant transaction in the partial-overlap fixture and again
prints maximum arity two.  The old cross-fixture capacity mismatch is closed.

### m1 — structural identity coverage: partially repaired

The reference now executes a finite nominal/structural identity battery rather
than setting the theorem gate to a literal truth value.  That is progress, but
the finite collision sample and one rename do not prove injectivity of digest
identifiers, alpha covariance of full actor ledgers, or root-free local slot
allocation.  This remains a minor scope limitation, detailed as m2 below.

### m2 — D24 compatibility: closed by exact narrowing

The candidate now says precisely that the transaction opening has D24's
one-parent **graph shape only**.  It claims no `B_g`/NSE operator gate and keeps
the quantum join, opportunity, `g` and participant selection open.  That is the
repair requested in round one.

## 3. New major findings

### M1 — the signature authenticates a quotient header, not the exact predecessor record

The envelope claims to carry a “signed predecessor record,” but its signed
public fields contain only `evidence_header(record)`.  That header omits the
record identity and every parent.  For `GRANT`, `REJECT`, `APPLY` and `RELEASE`
it also deletes payload field 3.  `Envelope.evidence` is explicitly excluded
from dataclass equality and hashing.

This is not merely a harmless quotient for graph comparison.  The same coarse
header is the input to `signed_envelope()` and `authentic()`, so it is the
physical authentication algebra accepted by the handlers.

An independent exact attack took a valid signed grant and replaced its carried
evidence by a newly constructed valid `GRANT` record with identical owner,
kind and payload but parents

```text
(transaction.carrier.record_id,)
```

instead of the original

```text
(participant.head_record, transaction.carrier.record_id).
```

No signature byte was changed.  The observed predicates were:

```text
setup_valid=1
evidence_header_equal=1
record_id_changed=1
signature_unchanged=1
authentic=1
transaction_accepts_response=1
handle_transaction_accepted=1
durable_actor_mutated=1
records_emitted=1
```

The altered record has severed the participant-wire predecessor that the grant
is supposed to authenticate.  Nevertheless the transaction actor accepts it,
appends a receipt referring to it and mutates its durable protocol state.  A
record with another same-header parent presentation is indistinguishable to
the signature; omitted payload field 3 has the same problem for the kinds on
which it is projected away.  `valid_record()` verifies self-consistent bytes,
not membership in the receiver's causal ledger.

Therefore the registered `8/8` hostile battery does not establish its printed
“reject before durable mutation” width, and the candidate does not yet execute
authenticated exact causal evidence.  It authenticates a coordination claim
that can be attached to inequivalent record ancestry.

**Required repair:**

1. sign the exact evidence record identity or a full canonical record digest
   that commits owner, kind, complete payload and parents;
2. use a separately named `coordination_header` only for state-graph quotient
   labels, never as the authenticated physical record;
3. before durable mutation, validate that carried evidence exists in or is
   validly appendable to the receiver's causal history and satisfies the
   expected owned-wire and cross-wire predecessor conditions; and
4. extend the hostile battery with same-header/different-record, parent
   deletion/substitution, omitted-field substitution, nonexistent predecessor
   and wrong-owner predecessor attacks, checking the complete actor world and
   ledger remain byte-identical on rejection.

Until then, the words **authenticated**, **signed predecessor record** and the
exact-record half of the final verdict are not earned.

### M2 — the stale/rebase “continuation” is two fresh worlds joined after the fact

`continuation_gate()` does not continue the old terminal history.  In each
mode it calls `run_policy()` once for the stale attempt and again for the
rebased attempt.  Both calls seed a new world at participant versions `(1,1)`.
The second run therefore does not begin from the first run's terminal actor
heads, mailboxes, used-envelope sets or ledger.

Only after both independent runs close does the gate union their ledgers and
append

```text
REBASE_LINK <- (old_close, new_carrier).
```

It never applies `validate_owned_wires()` or terminal closure validation to
that union.  Reconstructing the BORN union exactly gives:

```text
combined_records=25
same_owner_multi_parent_kinds=('REBASE_LINK',)
validate_owned_wires=FAIL
old_close_below_new_close=0
```

The participant seed records each fork: the old reject/release path and the
new grant/apply path are two children of the same participant root.  The
transaction owner also fails because `REBASE_LINK` has two same-owner parents,
`old_close` and `new_carrier`.  The new close does not contain the old failed
attempt in its ancestry.  TOKEN independently gives `combined_records=27`,
`validate_owned_wires=FAIL` and `old_close_below_new_close=0`.  In both modes
each participant root branches into `REJECT` and `GRANT`; the transaction wire
also branches because the new carrier parents both its normal
`RESPONSE_RECEIPT` and the post-hoc `REBASE_LINK`.

The printed rows

```text
old_base_abort=2/2
rebased_commit=2/2
combined_records=52
```

therefore prove two correct isolated attempts plus a set union, not a valid
two-epoch append-only continuation.

**Required repair:** begin the second attempt from the actual old terminal
`ActorWorld` and ledger.  Append its participant events from the old terminal
participant heads and carry the old closure or a bounded lineage successor
into the new transaction history.  Then, in both BORN and TOKEN modes, require:

- one linear wire for every participant and transaction owner;
- the old rejection/release/close records in the ancestry of the new lineage
  closure;
- unchanged old record bytes;
- a changed version-bound attempt identity with stable logical lineage;
- rejection of any stale old-attempt envelope after rebase; and
- full validation of the combined ledger, not just its record count.

If each attempt is a new transaction actor, give it a distinct owner identity
and use a separate bounded lineage actor/record.  Do not attach two same-owner
parents to a record while claiming the owner wire is linear.

## 4. Minor findings

### m1 — capability provenance and attempt identity remain narrower than the narration

The repair correctly removes remote exact tips from `logical_tau`, but stable
capabilities are globally constructed fixture data.  The initiator seed's
payload does not contain capability-issuing records in its ancestry.  This is
acceptable only under the note's final, honest statement that capabilities
and fixed attempt bodies are supplied.

Moreover, `body_digest` is computed from requested integer bases before any
grant arrives.  The later exact grant record is a parent of response/receipt
records, but its record identity is not itself a field of that precomputed
attempt digest.  After M1 is repaired, the prose should distinguish:

```text
requested version claim named by the pre-grant attempt body;
actual current record certified by the later authenticated grant;
post-grant decision/closure identity, if exact grant identities must bind it.
```

Do not say the exact current tips already constitute the version-bound attempt
identity unless a realized post-grant record actually derives that identity
from their authenticated record IDs.

### m2 — the structural-identity gate is a finite collision battery, not a general freshness law

The repaired reference checks a small typed ordinal/slot sample and a rename.
The companion does not alpha-rename complete BORN and TOKEN ledgers or test
cross-domain digest collisions.  `tx_index`, participant labels and the local
slot census remain supplied finite-fixture structure, while SHA-256 outputs are
treated operationally as unique record IDs.

This supports the audited finite exhibit, not mathematical injectivity,
equivariant root-free fresh support or a scalable local allocator.  Keep N1's
nominal obstruction as the prose theorem and label the executable result a
finite structural-identity/collision test.  A later unbounded claim needs a
typed constructor theorem independent of cryptographic collision assumptions.

## 5. What is now earned

Subject to the two majors, the repair materially advances D36:

- the finite reference control remains exact;
- the actor handlers are local in the declared logical sense: one addressed
  actor services one mailbox item without reading another actor's live state;
- accepted single-attempt transitions append typed immutable records;
- representative terminal ledgers have linear owned wires and complete close
  ancestry;
- the three-participant closure respects parent arity two;
- BORN and TOKEN independently realize the same coordination quotient on all
  four fixtures while their support-record ontologies remain unequal;
- the global serializer step is not promoted to physical time;
- D24 compatibility means graph shape only; and
- opportunity, arbitration, crashes, starvation, unbounded completion,
  quantum join and spacetime consequences remain honestly open.

The exact result is consequently narrower than the candidate verdict:

> **Supplied finite single-attempt actor-local append-only coordination
> refinement, modulo an envelope-header quotient, with BORN/TOKEN coordination
> equivalence but distinct support ontologies.**

It is not yet an authenticated exact-record refinement or a demonstrated
multi-epoch append-only history.

## 6. Final disposition

**Fresh counterexamples:** **2**.

**Final count:** **0B / 2M / 2m / 0n.**

**Decision:** **MAJOR REVISION.**  Retain the single-attempt record companion,
four-fixture coordination projection, bounded merge closure and explicit
ontology inequality.  Before closing the ancestry lane, authenticate exact
record identities rather than quotient headers and rebuild stale/rebase as one
causally continuous ledger whose owned wires and closure ancestry pass the
same validators as every other terminal history.
