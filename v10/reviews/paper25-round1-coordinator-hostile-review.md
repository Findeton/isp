# Paper 25 round 1 — coordinator hostile synthesis review

**Frozen manuscript:** `64f0bf9`.

**Manuscript:**
`relativistic-isp-v10-paper25-record-birth-carries-coordination-but-does-not-select-it.md`.

**Lane:** theorem width, actor/transport locality, disjoint covariance,
probability and arbitration attribution, transaction-protocol literature,
birth/token ontology and quantum nonclaims.

**Independence disclosure:** this is a coordinator self-hostile review, not an
independent reviewer lane.  It freezes paper-level defects before repair but
does not replace an external or separately authored review if that stronger
workflow is required.

**Verdict:** **PAPER-LEVEL TERMINAL PROMOTION WITHHELD; TERMINAL D36 SURVIVES.**

**Count:** **0 blockers / 2 majors / 3 minors / 1 nit.**

## 1. Reproduction and invariant core

The D36 reference, actor and replay receipts reproduce at the frozen target:

```text
reference model                 PASS 22/22
actor-record refinement         PASS 14/14
external deterministic replay  PASS 8/8
```

The manuscript accurately reports the central finite results:

- held acquisition retains one circular-wait deadlock;
- reusable grants allow double commit;
- participant-local adoption allows a split application;
- exclusive waiting has two split-vote deadlocks;
- exclusive fail-fast attempts have the four exact state-graph censuses;
- BORN and TOKEN actor coordination quotients match while support records
  differ;
- all fourteen authentication attacks reject before durable mutation;
- persistent stale/rebase histories close in both modes;
- gapped tx2 and both local orders close with typed records; and
- K1, K2 and K3 remain unselected.

No finding below reopens those terminal D36 statements.  The findings concern
the manuscript's scope and one paper-triggered strengthening of the disjoint
control.

## 2. MAJOR M1 — participant identity is conflated with attempt-local state

The decision table asks:

```text
Are participant and transaction identities local? structural attempt keyed
```

That is too broad.  The repair established two narrower properties:

```text
participant per-attempt state     sparse and keyed by structural attempt;
transaction actor registry        looked up by structural attempt;
participant actor registry        supplied finite tuple, addressed by role index;
ideal actor authentication key    derived from supplied kind/index role.
```

`append_to_target()` still addresses participant actors through
`participants[envelope.target_index]`.  That is acceptable at D36's fixed
finite participant boundary, because participant roles and capabilities are
supplied and no participant-insertion covariance theorem is claimed.  It is
not a proof that participant actor identity, participant discovery or all
transport addressing is structural-attempt keyed.

The abstract's sentence that “participant plus transaction state must be
keyed by the carrier-derived structural attempt” is defensible only if
“participant state” explicitly means attempt-indexed application/response and
authorization entries.  Read as actor identity or participant registry, it is
false.

**Required repair:** replace the decision-table row with separate rows for
participant per-attempt state, transaction routing and supplied participant
roles.  Add an explicit scope paragraph near section 3.3 or 15.3:

> D36 does not prove covariance under inserting or renumbering participant
> actors.  Participant roles are a supplied finite interface addressed by
> fixed indices and capabilities.  The construction-order repair concerns
> global transaction ordinals, per-attempt participant entries and transaction
> actor routing.

The abstract and conclusion must not imply a root-free participant registry or
discovery law.

## 3. MAJOR M2 — the frozen disjoint comparator is not a pure absent-Q world

Section 9.4 says one run contains only local `P(A,B)` plus four participant
seeds and another inserts `Q(C,D)`.  At frozen D36 commit `c481f82`, the local
branch removes Q's transaction actor, carrier and prepare mailboxes, but C and
D retain Q-specific predictive metadata constructed by
`open_actor_world("disjoint", "BORN")`:

```text
application entry for Q;
response entry for Q;
Q route capability;
Q authorization tuple.
```

Because those fields are confined to disconnected C/D actors, the existing
13-record A/B/P restriction equality is still meaningful: activating and
closing the remote transaction changes no exact local record.  But the paper's
stronger “only P plus seeds, then insert Q” description is not what the frozen
gate executes.

The paper-level audit triggered a direct strengthening in the working tree:
the absent-Q branch now removes Q-specific application, response, capability,
authorization and mailbox state as well as Q's actor and carrier.  The focused
gate still returns exactly:

```text
(1, 1, 2, 8, 1, 13, 24, 2,
 bebdcaa83877276fef663a2eb9f060edd25f5c15774647590e5ce11584b0fb89)
```

This repair is not yet committed or replay-frozen at the manuscript target.

**Required repair:** commit the strengthened absence control, regenerate the
actor and replay receipts under two hash seeds, update every paper/note/review
identifier, and describe the comparison exactly.  Paper-level promotion must
use the strengthened committed gate, not this review's ad hoc working-tree
observation.

## 4. MINOR m1 — transaction-protocol novelty is disclaimed but not situated

Section 2.3 says exclusive reservations, commit/abort and acknowledgement
closure are familiar ingredients, but gives no external transaction-commit
reference.  This makes the ontological contribution easier to misread as a
distributed-systems novelty claim.

Gray and Lamport's *Consensus on Transaction Commit* explicitly describes
traditional Two-Phase Commit, its zero-fault relation to Paxos Commit and its
failure behavior.  Paper 25 need not claim identity with classical 2PC—the
fail-fast conflict response, immutable record ontology and finite actor
refinement are its own declared model—but it should compare roles and separate
the contribution:

```text
classical transaction-commit layer   background protocol family;
D36 contribution                     record ontology, actor-local refinement,
                                     birth/token quotient and global-ordinal audit;
not supplied by D36                   fault-tolerant consensus/commit recovery.
```

**Required repair:** add a short positioning paragraph and the primary Gray--
Lamport reference.  Do not import Paxos fault tolerance into D36.

## 5. MINOR m2 — the abstract groups K3 with progressing arbitration kernels

The abstract says “three exact stochastic candidates survive” immediately
after discussing a winner.  Sections 10.2--10.4 correctly distinguish K1 and
K2 as progressing arbitration kernels from K3 as a hard-core regional family
that may select the empty or a nonmaximal set.

**Required repair:** say that two progressing arbitration kernels and one
broader regional statistical family survive.  The nonselection conclusion is
unchanged.

## 6. MINOR m3 — derived authorization cache needs one sentence

Section 3.1 says every durable effect is an immutable record, while section
5.2 says a participant locally records an authorization entry.  The executable
stores that entry in actor predictive state but does not append a separate
`AUTHORIZATION` record.  It is reconstructible from the already authenticated
carrier/prepare and the participant's typed response event, so this need not
be a theorem defect.

**Required repair:** identify authorization, current tip, phase and sparse
application/response tables as derived actor caches whose durable witness is
the carrier plus the emitted response/application records.  Do not imply a
separate record type that does not exist.

## 7. NIT n1 — “set serialized in a tuple” should remain literal

The note and paper describe the transaction registry as a finite sparse set
serialized canonically.  The Python object is still a tuple.  The explanation
is mathematically clear, but one occurrence should say “tuple representation
of a finite keyed registry” so readers do not infer a hash-set data structure
or constant-time lookup claim.

## 8. Scope checks that pass

The following possible overclaims were specifically attacked and do not
produce findings:

1. The paper says terminal multiplicities are not service-order probabilities.
2. Attempt closure is conditioned on reliable delivery, failure-free operation
   and fair complete service; crash recovery is excluded.
3. The theorem uses causal extension rather than elapsed duration.
4. Same-participant alternative prepare orders are retained as different
   physical histories, not gauged away.
5. BORN/TOKEN equality is explicitly only a coordination quotient; full record
   algebra inequality is retained.
6. The D24 relation is graph-shape-only until a quantum instrument is supplied.
7. Raw restriction failure, explicit boundary repair and finite-cover
   obstruction are all stated.
8. Sparse finiteness is not promoted to a uniform bound or infinite-history
   theorem.
9. `service_world` is honestly labeled a handler-plus-transport macro.
10. Honest remote record generation remains an assumption; no Byzantine
    ancestry proof is claimed.

## 9. Disposition

```text
B  blockers  0
M  majors    2
m  minors    3
n  nits      1
```

Paper 25 has the right central thesis and terminal D36 remains valid.  The
paper cannot yet be called terminal because its actor-identity summary exceeds
the theorem and its pure disjoint-insertion prose exceeds the frozen gate.
After the strengthened control is committed and replayed, the manuscript needs
only scoped wording, literature positioning and the narrower K3/cache
descriptions.  A focused paper-level closing delta may then decide promotion.

