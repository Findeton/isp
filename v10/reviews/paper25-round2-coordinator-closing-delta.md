# Paper 25 round 2 — coordinator closing delta

**Reviewed manuscript:** `6424361` (`Repair Paper 25 hostile findings`).

**Reviewed D36 strengthening:** `4282521` (`Strengthen D36 disjoint absence
control`).

**Date:** 2026-07-14.

**Independence disclosure:** this is a focused coordinator delta against the
coordinator's own round-one hostile report.  It is not an independent paper
review.

**Verdict:** **DELTA CLOSED AT THE COORDINATOR-REVIEW LEVEL. PAPER 25 IS A
COORDINATOR-CLOSED CANDIDATE; INDEPENDENT PAPER-LEVEL REVIEW REMAINS OPEN.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

## 1. Artifact and receipt reproduction

The repaired manuscript SHA-256 is:

```text
f59446ba232b3def9ac43d598d9dcd7419260cd4aad8e223a2bdf9ed816c2928
```

The terminal code receipts reproduce under Python hash seeds `17` and
`104729`:

```text
reference model                 PASS 22/22
actor-record refinement         PASS 14/14
external deterministic replay  PASS 8/8
```

Current identifiers:

```text
reference source  2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683
reference stdout  868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17

actor source      57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b
actor stdout      eaf2e535b475b9f3fafe080175a5399e2748c0a554ed768f470869cfdf291b48
actor science     7bee23d9ebf22b2a0112ec0677f3b584990ef9a09a4e4ef34b77e75e7bca53d0

replay source     af3d773e11095bd125126a01028ffc83c7c91129fc6c921faa52dd173287ce98
replay stdout     9324aec40ad8f184058d75ea2870ed9628823971ee7ca0e591e28b5af0b06110
```

The paper's identifiers match these committed files exactly.

## 2. Major M1 — participant identity scope

**Disposition: closed.**

The abstract now says “participant per-attempt entries plus transaction
routing,” not “participant plus transaction state.”  Section 3.3 distinguishes
three facts:

```text
participant per-attempt entries       structural-attempt keyed;
transaction actor lookup/routing      structural-attempt keyed;
participant actor roles               fixed supplied interface, index/capability addressed.
```

It explicitly refuses participant discovery and covariance under inserting or
renumbering participant actors.  The decision table carries three separate
rows, and the conclusion narrows the construction-order claim to participant
per-attempt tables plus the transaction registry.  No root-free participant
namespace or discovery theorem remains implied.

## 3. Major M2 — pure absent-Q comparator

**Disposition: closed.**

Commit `4282521` removes Q's application entry, response entry, capability,
authorization and mailbox state from C/D in the absent branch, as well as Q's
transaction actor and carrier.  The present branch therefore begins with four
participant seeds and only local `P(A,B)` protocol state.  The comparison
branch installs and closes `Q(C,D)` normally.

The strengthening leaves every scientific value unchanged:

```text
gapped tx2 closed                         1 / 1
no tx1 actor or record                    1 / 1
complete local-order histories            2 / 2
typed full-run responses                  8 / 8
disjoint insertion exact local ledger     1 / 1
restricted local records                     13
gapped combined records                      24
maximum parent arity                          2
family hash  bebdcaa83877276fef663a2eb9f060edd25f5c15774647590e5ce11584b0fb89
```

Section 9.4 now states exactly which Q-specific fields are absent.  The
abstract's insertion statement is therefore supported by a committed pure
control.

## 4. Minor and nit dispositions

### m1 — transaction-commit positioning

**Closed.**  Section 2.3 cites Gray and Lamport's primary transaction-commit
paper and says precisely what is and is not inherited.  P4 is placed in the
failure-free coordinator/participant commit background; D36's contribution is
the record ontology, carrier comparison, actor refinement and ordinal audit.
Paxos consensus, replicated coordinators and crash recovery remain excluded.

### m2 — K3 progress language

**Closed.**  The abstract now calls K1 and K2 the two progressing arbitration
kernels and K3 a broader regional statistical family that need not progress.
The path separation and nonselection theorem are unchanged.

### m3 — authorization cache

**Closed.**  Section 3.1 lists authorization tuples with the other derived
actor caches and identifies the durable witness as the authenticated
carrier/prepare plus typed response.  It explicitly says there is no separate
`AUTHORIZATION` record type.

### n1 — registry representation

**Closed.**  Section 3.3 now says “tuple representation of a finite sparse
keyed registry,” states that lookup is by structural attempt and disclaims a
constant-time data-structure assertion.

## 5. Scope audit

The repaired paper consistently retains:

```text
supplied finite attempts and participant roles;
ideal authentication and honest record generation;
reliable delivery, failure-free operation and fair complete servicing;
representative quotient-edge lifts, not all exact histories;
coordination-quotient BORN/TOKEN equality, not record-algebra equality;
no probability on service orders;
no selected opportunity, batch boundary, arbitration or retry law;
no crash, Byzantine, uniform-memory or infinite-completion theorem;
no quantum join, root-free history law or spacetime consequence.
```

The Gray--Lamport addition does not alter those assumptions.  The paper calls
the protocol familiar background and makes its claimed contribution
ontological and model-auditing.

## 6. Final disposition

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

The accepted coordinator-level noun is:

```text
CLOCK-FREE ACTOR-LOCAL APPEND-ONLY COORDINATION /
SUPPLIED FINITE FAILURE-FREE ATTEMPTS / NONSELECTING.
```

This delta closes every frozen round-one coordinator finding.  Because both
review rounds were authored by the coordinator, it does not establish the
stronger repository convention of independent multi-lane paper acceptance.
Paper 25 should remain a coordinator-closed candidate until such review is
performed.
