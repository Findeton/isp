# D36 round 3 — probability/capacity/replay integrity delta

**Frozen target:** commit
`e80ca6af30ff1e6ca83b97e1521d8a335c054850`

**Comparison target:** commit
`63314a24cfd181793034763fcec9fdb701ddb6b2`

**Prior lane:**
`v10/reviews/d36-round2-probability-closing-delta.md`

**Scope:** reference G20 relabeling, K1/K2/K3 preservation, component-mark
factorization, DLR support counts, bounded-cell capacity, finite-bit retry,
source/receipt replay integrity, and probability/capacity/history-law side
effects of the actor attempt-authentication and persistent-continuation repair

**Verdict:** **PASS — THE ROUND-2 PROBABILITY CLOSURE SURVIVES THE ROUND-3
ACTOR REPAIR.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

The reference scientific object is unchanged.  The only reference-source
delta adds `static_scope_assertion=1` to G20's narration.  The actor repair
adds exact attempt/evidence binding and one persistent two-attempt exhibit; it
does not add a random service law, global arbitration selector, uniform
capacity theorem or complete-history measure.

## 1. Independent reproduction and hashes

I reran the frozen reference under `PYTHONHASHSEED=141421356`; it exited zero
with `PASS 22/22`.  I reran the actor companion independently under
`PYTHONHASHSEED=173205080`; it exited zero with `PASS 12/12`.  Finally, the
external checker launched both programs under seeds `17` and `104729`, matched
each pair byte-for-byte to its committed receipt and returned `PASS 8/8`.

The independently recomputed frozen hashes are:

```text
reference source
2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683

reference complete stdout / committed receipt
868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17

reference stdout body before hash/gate trailer
683ba498d99bac3d430606efc3697cb4e1aa7ac3d4b6103c17237e44b4ba5225

reference internal science
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source
748128631ff32268a9d0f5c8f74306189a9d371752569e06f87f2a0c2ca0214a

actor complete stdout / committed receipt
8ee46d53a1f392222b4e60e10ead369a831661f272120e090a2166985edfcf43

actor stdout body before hash/gate trailer
f147e3afd77c81971a86136ebaa8e6add87bb0ce5988f4e5c152d66750757b47

actor internal science
c9fb8f5e75fb635f6dade6c2e176959d96a2451465d2813d4afe72ceb757f19d

replay-checker source
3cbf013bbb1766fbc8e304be33ebcec3d3783f8f5fedc6fc6b7f3a62e7c8ef95

replay-checker complete stdout / committed receipt
c69b25e39df2f7ac478643ec2a9716c02ff924c02636fcce6211d0c4d1dee94e
```

`git diff --check 63314a2..e80ca6a` is clean.  Every active identifier printed
in section 21 of the note agrees with the frozen files.

## 2. Reference G20 delta — narration only

The complete reference source diff is one changed output field:

```text
coordinator_loss_can_block_promise=1
```

became

```text
static_scope_assertion=1; coordinator_loss_can_block_promise=1.
```

The gate expression remains

```text
crash_blocking == 1 and unilateral_expiry == 0.
```

The `science["failure_scope"]` value remains `[1,0]`.  Most decisively, the
internal science hash is unchanged from round 2:

```text
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314.
```

The source, stdout-body and complete-stdout hashes properly changed because
the literal receipt text changed.  The revised label closes a provenance
ambiguity: G20 is a static failure-scope witness, not an executed crash trace.
It has no route into the probability calculations.

## 3. K1/K2/K3 — bytewise and mathematical preservation

The committed receipt diff changes no line from closed ordered batches through
regional restriction.  Fresh execution reproduces all round-2 values.

### K1

On `P--Q--R`, Q precedes both endpoints in two of the six strict orders.  Thus

```text
K1({Q})   = 2/6 = 1/3;
K1({P,R}) = 4/6 = 2/3.
```

### K2

The maximal independent sets are `{Q}` and `{P,R}`, so

```text
K2({Q})   = 1/2;
K2({P,R}) = 1/2.
```

### K3

The independent sets are

```text
{}, {P}, {Q}, {R}, {P,R}.
```

At activity one each has probability `1/5`.  At activity two the weights are
`1,2,2,2,4`, the partition function is `11`, and the probabilities remain

```text
1/11, 2/11, 2/11, 2/11, 4/11.
```

K1 and K2 still disagree on `{P,R}`, and K3 still changes with supplied
activity.  The receipt continues to print `selector=UNSELECTED` and
`lambda_unselected=1`.  No actor change selects among these families.

## 4. Marked factorization, DLR, capacity and retry — unchanged

### Component-local marked factorization

For the two disconnected conflicts, the physical K1 mark space remains

```text
Sym({P,Q}) x Sym({R,S}),
```

with four product atoms of probability `1/4`.  The 24 global presentation
orders restrict to those four atoms with six interleavings per atom, hence
`6/24=1/4`.  The receipt remains:

```text
physical_component_order_atoms=4;
global_presentation_orders=24;
gauge_shuffles_per_component_atom=6.
```

The four accepted sets remain the full product support.  The shared-coin
negative control remains supported only on `{P,R}` and `{Q,S}`.  No
continuation record is used as a priority mark or common random variable.

### DLR

Per activity, the path has ten positive-mass single-site boundary
conditionals and two inadmissible zero-mass outside assignments.  At the two
registered activities the exact census remains

```text
DLR_positive_mass_conditionals=20;
DLR_zero_mass_boundaries_skipped=4.
```

No actor or authentication field appears in the hard-core kernel.

### Reference capacity

G19 still requires and prints

```text
(max transaction arity,
 max participants,
 max proposals,
 max incident contenders,
 max priority bits) = (3,4,4,2,2).
```

The reference closure still has maximum parent arity two.  The actor repair
does not alter any reference fixture or auxiliary factorization region.

### Finite-bit events

The unique-greatest rows remain

```text
1/2, 3/4, 3/8, 21/32,
```

while the complete-order/all-distinct rows remain

```text
1/2, 3/4, 0, 3/8.
```

The receipt still conditions almost-sure resolution on continued iid retry
opportunities and denies a bounded worst case.  The repaired two-epoch actor
continuation is supplied deterministically; it is not evidence that the
history law supplies those retry opportunities.

## 5. Actor repair — no hidden probability law

The companion imports no random-number mechanism and constructs no measure on
mailbox service orders.  Its structural attempt ID is a deterministic digest
of the carrier, body, member set and requested bases.  Exact record signing is
an ideal deterministic authentication assumption at this finite scope, not a
new stochastic arbitration mark.

`run_to_quiescence()` chooses one canonical enabled actor mailbox in order to
construct a witness ledger.  That serializer choice receives no probability,
rate, duration or physical clock interpretation.  The four main actor graphs
still enumerate every enabled mailbox service at the coordination-quotient
level.  Their terminal multiplicities remain state counts, not service-order
probabilities.

The repair therefore does not couple actor scheduling to K1, K2 or K3.  It
also does not turn successful execution of the rebased attempt into a lineage-
success probability.  It is one supplied finite path per BORN/TOKEN mode.

## 6. Actor repair — capacity audit and the unbounded ceiling

The persistent continuation is two sequential two-participant attempts.  In
each mode, the stale attempt closes before the rebase carrier is appended.
The active receipt proves:

```text
maximum parent arity in the four main actor fixtures  2;
largest main-fixture terminal ledger                 39 records;
continuation ledger                                  24 records in BORN;
continuation ledger                                  26 records in TOKEN;
combined receipt count                               50 across the two modes.
```

`combined_records=50` is not one record's payload and not one universe-wide
batch.  It is the sum of separate 24-record BORN and 26-record TOKEN witness
ledgers; TOKEN carries the two pre-existing dormant-slot records.
Every new continuation record has bounded payload at the registered two-
participant scope and at most two parents.  The new carrier descends from the
old close; it does not copy the full old ledger into one field.

Some live simulator tuples grow by one entry per additional attempt:

```text
transactions, authorizations, applications, response-record slots and used
envelope IDs.
```

That architecture is not a uniform bounded-state theorem.  The candidate does
not claim otherwise.  The capacity pin says the retry/rebase history uses new
bounded records per attempt, and the final ceiling explicitly leaves
`unbounded completion` and the scalable law open.  At the executed two-epoch
scope, those tuples have finite registered lengths and no record hides an
unbounded list.

The fixed-length digests are also explicitly ideal/collision-resistant
identifiers in this finite campaign.  They are not claimed to be a proved
injective compression of arbitrary infinite evidence.

## 7. Actor repair — no physical global selector

The simulation engine can see the finite collection of nonempty mailboxes in
order to enumerate or serialize the test.  A serviced handler nevertheless
reads only the addressed actor and carried envelope.  The chosen service is a
machine construction order, not an accepted physical queue.

The only gauge theorem remains narrow: four pairs of genuinely incomparable
services on disjoint actors commute in both world and ledger.  The note
explicitly refuses to gauge alternative services at one actor, and the
continuation uses a canonical serializer only to exhibit one valid history.

Consequently the repair does not supply:

```text
the birth opportunity law;
participant discovery;
the closed eligibility boundary;
arbitration among overlapping proposals;
retry fairness; or
a root-free global commit order.
```

All remain open in the final active paragraph.  There is no hidden promotion
of Python's sorted mailbox choice into universe dynamics.

## 8. Actor repair — full-history claim remains properly limited

The round-2 overstatement is explicitly repaired in both receipt and note.
The `297,980` BORN+TOKEN edge checks are called **representative coordination-
quotient edges**.  The 56 terminal ledgers are one complete causal lift per
terminal quotient state.  They are not a census of every record-distinct path
or every full causal history.

The persistent continuation now earns a different, narrower statement.  For
each of two carrier modes it constructs one actual world and ledger in which:

```text
the stale attempt aborts;
the old immutable prefix is unchanged;
the new attempt commits;
the complete combined ledger validates;
the old close lies below the new close;
replay of the old envelope is rejected.
```

That is a valid two-attempt existence exhibit.  It is not an infinite-history
extension theorem, a Kolmogorov/projective completion, or a primitive history
measure.  Same-transaction service-order histories are expressly retained as
potentially different physical histories.  The note's historical section 19
records the superseded candidate, while sections 20--21 freeze and repair its
scope; the active verdict relies on the latter.

## 9. Replay integrity after the actor repair

The replay checker now pins the two new source hashes.  It runs each source in
fresh subprocesses at two hash seeds, rejects stderr, demands within-source
byte identity and compares the bytes with the committed receipt.  Fresh
execution returned:

```text
reference seeded executions  2;
actor seeded executions      2;
within-source equalities     2;
receipt equalities           2;
PASS                         8/8.
```

The actor source also pins the new reference source hash internally.  Thus the
actor receipt cannot silently import the old reference semantics, and the
external receipt confirms the exact frozen pair.

## 10. Final disposition

The round-3 delta has the following probability-lane disposition:

| Question | Disposition |
|---|---|
| G20 label changed reference science | no; narration only, science hash unchanged |
| K1/K2/K3 values moved | no; every exact value preserved |
| physical K1 factorization regressed | no; component product and 24-to-4 quotient preserved |
| DLR support accounting regressed | no; `20+4` preserved |
| reference capacity moved | no; `(3,4,4,2,2)` and parent arity two preserved |
| retry events reconflated | no; unique-greatest and complete-order rows remain separate |
| actor repair added a probability law | no; serializer is deterministic test construction |
| actor repair proved uniform bounded memory | no; finite two-epoch scope only, unbounded completion open |
| actor repair supplied global arbitration | no; opportunity, eligibility and arbitration remain open |
| actor repair claimed all full histories | no; representative lifts and one continuation exhibit only |
| replay integrity regressed | no; fresh `PASS 8/8` and all hashes match |

Final tally:

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Recommendation:** close the round-3 probability/capacity/replay delta.  The
actor authentication and continuation repairs do not disturb the exact
arbitration receipts or cross the candidate's explicitly finite,
nonselecting, non-global and non-history-complete boundary.
