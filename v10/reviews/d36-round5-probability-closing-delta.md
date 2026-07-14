# D36 round 5 — probability/capacity/replay closing delta

**Frozen target:** commit
`9dcdb5f6be7e8dd1b611797c2374a415321012ce`

**Comparison target:** commit
`da9942d828a19ff12e2774768f5655a1270ef91c`

**Prior lane:**
`v10/reviews/d36-round4-probability-closing-delta.md`

**Scope:** sparse structural-attempt maps, global-index covariance gate,
bounded-cell capacity, arbitration/probability preservation, scheduler and
full-history scope, and deterministic replay integrity

**Verdict:** **PASS — THE SPARSE-MAP REPAIR CLOSES THE GLOBAL-ORDINAL DEFECT
WITHOUT CHANGING THE PROBABILITY RESULT OR ASSERTING A UNIFORM BOUND.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

The reference source and receipt are byte-identical to rounds 3 and 4.  The
actor delta replaces dense participant arrays with finite sparse entries keyed
by structural attempt ID and adds one exact covariance gate.  The maps are
finite only because the audited boundary is finite; no uniform universe-wide
state bound, random selector, physical global scheduler or complete-history
measure is claimed.

## 1. Independent reproduction and integrity

I reran the frozen reference under `PYTHONHASHSEED=264575131`; it exited zero
with `PASS 22/22`.  I reran the actor companion under
`PYTHONHASHSEED=282842712`; it exited zero with `PASS 13/13`.  The external
checker then ran both programs under seeds `17` and `104729`, compared all
four outputs byte-for-byte with the committed receipts and returned
`PASS 8/8`.

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
f353ac2dcff2a7e1b80159cd5602b763669b0157439b09c5a92b50fb01c339b8

actor complete stdout / committed receipt
1c72a2d132add307fc49514d52ed6d82e88b42b3ce114fd6d8e3c996c79c5fc4

actor stdout body
02375603f824efc74a6953b8d8e6d4a35c3a8f6cff964200e005e7c4752db9b7

actor internal science
6621a32688a27b0f55e99eddf570c7a2956d718e5bd4a37f95d48b3529403227

replay-checker source
b76adbe744c278b3d91a2f3f2a4be0c278a2bad40982ea54f9a10a867719519f

replay-checker complete stdout / committed receipt
554369b4f93057f3d838f891c19f49ebb92f4eae35f2afc6703dc7efa62d9a33
```

`git diff --check da9942d..9dcdb5f` is clean.  The active identifiers in
section 25 of the note agree with the frozen files.

## 2. Delta census

The frozen patch does not modify either reference file:

```text
v10/code/d36_birth_coordination_exact.py
v10/data/d36_birth_coordination_exact.out.
```

The actor change is the registered round-4 repair:

1. `ParticipantActor` replaces globally indexed application and response
   arrays with finite tuples keyed by structural attempt ID;
2. the exclusive promise is keyed by attempt ID rather than transaction
   ordinal;
3. authorizations are keyed first by attempt ID;
4. prepare admission tests absence of that attempt from the two sparse domains
   rather than `tx_index == len(global array)`;
5. application and response lookup/update use the structural key;
6. the frozen reference projection reconstructs dense analysis arrays from
   the transaction actors' attempt IDs only for comparison; and
7. A12 tests an index gap and both local delivery orders without padding.

The integer transaction index remains an envelope/actor routing coordinate.
It no longer decides whether a participant can allocate local physical state.
No probability or rate field is added.

## 3. K1/K2/K3 — unchanged

Fresh reference execution reproduces:

```text
K1({Q})   = 1/3;
K1({P,R}) = 2/3;

K2({Q})   = 1/2;
K2({P,R}) = 1/2.
```

K1 still counts two Q-first orders and four endpoint-first orders among the
six strict path orders.  K2 remains uniform over the two maximal independent
sets.

K3 remains supported on

```text
{}, {P}, {Q}, {R}, {P,R}.
```

At activity one every probability remains `1/5`.  At activity two the weights
remain `1,2,2,2,4`, partition function `11`, and probabilities

```text
1/11, 2/11, 2/11, 2/11, 4/11.
```

The reference continues to state `selector=UNSELECTED` and
`lambda_unselected=1`.  Sparse actor keys do not select a kernel or activity.

## 4. Factorization, DLR, restriction and retry — unchanged

The physical K1 mark on the two disconnected conflict components remains a
four-atom product.  Its global presentation quotient remains exact:

```text
physical component-order atoms  4;
global presentation orders     24;
gauge shuffles per atom          6.
```

Each marked atom therefore has probability `6/24=1/4`.  The shared-coin
negative control remains nonfactorizing.

The hard-core support census remains:

```text
positive-mass DLR conditionals  20;
zero-mass boundaries skipped     4.
```

The raw K1 path-to-edge restriction remains `2/3,1/3` versus the direct
edge's `1/2,1/2`, and the explicit K3 boundary mixture remains exact.

Finite-bit unique-greatest probabilities remain

```text
1/2, 3/4, 3/8, 21/32,
```

while complete-order/all-distinct probabilities remain

```text
1/2, 3/4, 0, 3/8.
```

Almost-sure resolution is still conditioned on continued iid retry
opportunities; no bounded worst case or retry-opportunity law is inferred
from the sparse map.

## 5. Capacity audit — finite is not uniformly bounded

The reference capacity tuple remains exactly

```text
(max transaction arity,
 max participants,
 max proposals,
 max incident contenders,
 max priority bits) = (3,4,4,2,2),
```

and maximum closure parent arity remains two.

The four actor graph rows preserve their earlier maxima:

```text
pair       26 records;
triangle   39 records;
disjoint   28 records;
partial    32 records;
maximum parent arity 2.
```

The persistent BORN/TOKEN continuation still has combined receipt count 50.
The new sparse covariance cell starts after one closed attempt and presents
two follow-up prepares.  Thus it uses only three historical attempts, two
currently competing prepares and two participants; it does not exceed the
registered finite proposal/incident cell.

The sparse representation removes **padding by absent global ordinals**.  It
does not bound the number of actual incident attempts.  For a finite supplied
region, each map has one entry per locally registered attempt and is finite.
Under indefinitely many attempts its size, the actor transaction collection
and the append-only ledger could all grow without bound.

That distinction is explicit in the active note:

```text
physical sparse tables remain finite under D36's supplied finite boundary;
no uniform bounded-state or infinite-history theorem is added.
```

No immutable record carries the whole sparse map or full ledger as a payload;
each emitted response/application record remains bounded at the registered
arity and has at most two parents.  The executable therefore proves a finite
sparse-state construction, not a constant-memory universe law.

## 6. Sparse order gate — nondeterminism, not a hidden random selector

A12 constructs two valid carrier-derived prepares with nominal transaction
addresses one and two after one closed attempt.  Address two is accepted while
address one is absent, proving there is no global-index padding prerequisite.

It then services both prepares in both orders.  The exact results are:

```text
global-index-gap prepare accepted  1/1;
tested local orders                2/2;
typed responses                    4/4;
no global padding                  2/2.
```

In each order, the first delivered prepare receives a grant and the second a
typed rejection because the participant's exclusive promise is occupied.
Reversing delivery reverses which structural attempt gets the grant.  This is
an explicit two-branch nondeterministic transition relation, not a random
law:

- both branches are checked;
- neither branch receives a probability;
- no random module, coin, mark, rate or duration is introduced; and
- no branch is promoted as nature's selected history.

The result exposes rather than solves arbitration.  A later history law or
recorded mark must say which delivery branch occurs and with what probability,
if any.  The active verdict still lists `arbitration selection` as open.

## 7. No physical global scheduler

`services(world)` and the canonical continuation policy remain simulation
machinery.  The main actor graphs enumerate all enabled mailbox services; the
continuation policy constructs one witness.  The sparse gate calls the
addressed participant handler directly in both orders.

The only declared gauge result remains four commuting pairs of genuinely
incomparable disjoint services.  Same-participant alternatives are not gauged:
their order can change grant/reject identities, and both histories remain in
scope.  The receipt continues to declare `service_world` a handler-plus-
transport macro and `serializer_step_is_not_physical_time=1`.

Although the finite Python harness sees all mailboxes to enumerate the state
graph, no actor handler reads a global queue and no theorem promotes the
harness's sorting rule into a universe scheduler.  Birth opportunity,
eligibility, arbitration and retry fairness remain supplied or open.

## 8. No full-history promotion

The 297,980 actor edge checks remain representative coordination-quotient
lifts, and the 56 terminal ledgers remain one complete path lift per terminal
quotient state.  They are not every record-distinct causal path.

The sparse A12 cell is a local handler counterexample/repair gate.  Its
follow-up carriers are bounded test evidence; it is not presented as a
validated infinite ledger or projective history family.  The persistent
two-attempt BORN/TOKEN histories remain the finite full-ledger witnesses.

Nothing in the patch claims Kolmogorov consistency, an all-cover law, an
infinite extension, starvation freedom or a complete history measure.  The
final receipt still leaves unbounded completion open.

## 9. Replay integrity

The replay checker pins the unchanged reference source and the new actor
source.  Fresh execution confirms:

```text
reference seeded runs          2;
actor seeded runs              2;
within-source byte equalities  2;
committed-receipt equalities   2;
PASS                           8/8.
```

The actor also locks the exact unchanged reference source hash before import,
so its new sparse projection cannot silently compare against a different
reference executable.

## 10. Final disposition

| Integrity question | Disposition |
|---|---|
| reference probability source changed | no; byte-identical |
| K1/K2/K3 moved | no |
| factorization or DLR moved | no |
| retry arithmetic moved | no |
| reference capacity moved | no; `(3,4,4,2,2)` and parent arity two |
| sparse maps assert a uniform bound | no; one entry per finite local attempt |
| sparse order gate adds a random selector | no; both unweighted branches retained |
| global transaction ordinal remains physical admission data | no; routing/projection only |
| simulator becomes a physical global scheduler | no; enumeration/witness machinery only |
| representative lifts become all full histories | no |
| replay integrity regressed | no; fresh `PASS 8/8` |

Final tally:

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Recommendation:** close the D36 round-5 probability/capacity/replay delta.
The sparse structural-attempt repair removes global ordinal padding while
preserving the exact finite probability and capacity results and keeping the
unselected, nonuniform and non-history-complete ceilings explicit.
