# D36 round 1 — record ontology, ancestry and birth hostile review

**Frozen target:** commit
`5f6cd7fccb6e34991bccd10fa1aa7992ebd0a393`.

**Lane:** immutable-record ontology, actor wires, causal transaction identity,
upper-seal ancestry, bounded capacity, D24 one-parent birth compatibility,
born/token matched control, finite versus unbounded scope, and
opportunity/quantum/birth-law ceilings.

**Verdict:** **MAJOR REVISION. THE FINITE FAIL-FAST COORDINATION GRAPH
REPRODUCES, BUT THE RECEIPT DOES NOT YET EXECUTE THE RECORD HISTORY OR THE
BIRTH/TOKEN COMPARISON THAT SUPPORT THE RECORD-NATIVE HEADLINE.**

**Count:** **0 blockers / 4 majors / 2 minors / 0 nits.**

The probability-free P0--P4 countermodels and the finite fail-fast state graph
remain useful. The four majors concern the additional interpretation of that
graph as an append-only SHARD record law. In particular, G18 constructs two
decorated copies of one pre-existing graph and then deletes the decorations;
the exact equality is tautological. Separately, the executable's mutable
summary states are never connected to its hand-written upper-seal DAG, the
proposal identity contains remote exact tips absent from the proposal's causal
past, and the stated parent-arity ceiling fails on the admitted arity-three
fixture.

## 1. Reproduction

Fresh executions under

```text
PYTHONHASHSEED=314159265
PYTHONHASHSEED=271828182
```

both exited zero and were byte-identical to the committed receipt. Exact
identifiers are:

```text
source SHA-256
f1b2c5010812e08f560876a570fc06693d59633de03421b0fed5ff5e5c3daed0

stdout body SHA-256
c5258f02d8f9763708e9355a304295e6c94a7c85aac39dde22c1d3f0b826c1c7

complete stdout / committed receipt SHA-256
0bf500873acdc71bb68c5b7d9012b89310941c879f59b013105db1f0e00fccea

internal science SHA-256
872a38acd65f7ebcb122a50f6713da53ae119764c7449387b1b55efe27acf04b

verdict
PASS 22/22.
```

The receipt exactly reproduces the advertised finite counts, including:

```text
held-lock control                  45 states / 69 edges / 1 deadlock;
fail-fast pair                  1,113 states / 2,984 edges / 8 terminals;
fail-fast triangle             34,637 states / 140,028 edges / 17 terminals;
fail-fast disjoint                289 states / 816 edges / 1 terminal;
fail-fast partial overlap       1,517 states / 5,162 edges / 2 terminals;
typed fail-fast terminals                              28 / 28;
born/token projected nodes                         1,113 / 1,113;
born/token projected edges                         2,984 / 2,984;
upper-seal nodes / ancestors / printed max arity       11 / 10 / 3.
```

`git diff --check 5f6cd7f^ 5f6cd7f` is clean. The findings below are not
reproduction failures; they identify what the passing gates actually prove.

## 2. What survives hostile review

The note makes several important distinctions correctly:

- a long-lived actor/wire is not one mutable sealed record;
- `T0`, grants, rejection, rebase, decision and closure should be successive
  immutable records rather than status mutations;
- an unselected kernel alternative is not a realized failed proposal;
- a malformed envelope may reject before a physical transition;
- structural identity, not printable spelling, must carry freshness;
- a finite payload cannot contain an arbitrary participant set, queue or retry
  history;
- exclusive promises are reservations even when no mutex object is named;
- fail-fast abort removes the held-resource circular-wait mechanism but does
  not establish retry success or starvation freedom;
- a closure record on T's wire is not automatically the successor on every
  participant wire;
- D24 supplies a conditional one-parent `B_g`, not opportunity probability,
  `g`, participant choice, priority, join or arbitration;
- the multi-parent commit and quantum join remain outside D24;
- P4 assumes reliable authenticated messages, a failure-free coordinator and
  fair delivery; and
- every capacity and eliminability conclusion is intended to be finite-scope,
  not a theorem about an unbounded universe.

The executable also supports the abstract finite-state claims that do not
require an append-only record interpretation: the registered held-lock
deadlock exists; reusable grants admit a double-commit witness; independent
adoption admits a split; exclusive waiting has two split-vote assignments;
and every enumerated P4 summary state reaches a typed terminal without a
disabled nonterminal state. Nothing below refutes those control results.

## 3. Major findings

### M1 — G18 is a decorated identity, not an independently constructed born/token bisimulation

`born_token_bisimulation_gate()` first constructs one graph:

```text
core_nodes, core_edges = failfast_graph(pair).
```

It then defines

```text
BORN nodes  = {("BORN", constant_born_header, state) for state in core_nodes};
TOKEN nodes = {("TOKEN", constant_token_slots, state) for state in core_nodes},
```

and creates both edge sets by wrapping every same `core_edges` pair. The
projection is literally `node[2]`. Therefore

```text
project(BORN graph) = core graph = project(TOKEN graph)
```

by construction, independently of whether birth and slot activation have the
same protocol semantics.

There is no common pre-proposal state, no BORN transition that creates `T0`, no
TOKEN transition that activates a dormant slot, no support count, no causal
parentage of the carrier, no inactive-slot state, and no independently written
transition rule on either side. The constant headers are already present in
every graph node, including the initial fail-fast node. A malformed born
header, a different number of dormant slots or a born-only causal ancestor
would remain invisible after the same projection.

This is not repaired by the statement that only participant/commit observables
are retained. Under that intentionally coarse algebra the equality is a valid
**definition-level projection identity**, but it does not test whether the
record systems are bisimilar. In the full declared ontology, the presentations
are already distinguished: BORN has newly created transaction support and
TOKEN has pre-existing dormant support. The code chooses to erase exactly that
observable before comparison.

The scope is also only one pair fixture and one closed batch. It does not cover
the triangle, disjoint, arity-three partial-overlap fixture, a rebase, a retry,
or two successive batches. Thus the final receipt line

```text
finite-horizon coordination power is token-equivalent
```

is wider than the check even after accepting the coarse observable projection.

**Required repair:**

1. start BORN and TOKEN from independently represented states before proposal
   creation/activation;
2. give them separate state types and transition generators;
3. have BORN append a structurally identified `T0` and have TOKEN activate a
   named dormant slot;
4. state the complete observable algebra, including whether support count and
   transaction ancestry are visible;
5. exhibit a relation `R` and check both forward and backward transition
   matching, initial-state relation and terminal-observable equality;
6. run at least pair, triangle, disjoint and arity-three partial overlap, plus
   one two-batch or retry/rebase horizon; and
7. if support/ancestry are intentionally hidden, rename the result
   **participant-commit projection equality on the one-pair fixture**, not
   born/token finite-horizon bisimulation.

Until that repair, decision row 3 and the token-equivalence half of the terminal
verdict are not earned.

### M2 — the exact P4 graph is a mutable protocol summary, not an append-only record history

The note's ontology normalization is good, but the executed P4 state is:

```text
FFState = versions, promises, responses, phases,
          applications, acknowledgements, pending.
```

Transitions replace these tuples. For example a grant writes
`promises[participant]=tx`; apply/release later writes it back to `-1`.
Messages are removed from `pending`. `phase` changes from OPEN through a
decision to CLOSED. No record identity, parent set, payload, capability,
proposal `tau`, event DAG or immutable-history prefix is present in `FFState`.

A frozen Python dataclass makes a summary node hashable; it does not prove that
the physical record that previously held a grant remains in the history. The
terminal typing checker only inspects final response/application/ack integers.
It cannot establish any of the note's stronger statements:

```text
every realized grant/rejection/rebase persists;
Close(T) has every apply and acknowledgement in its causal past;
independent delivery orders yield the same canonical marked DAG;
old record bytes and parentage are immutable;
transaction identity is alpha-safe throughout the protocol.
```

`upper_seal_gate()` does not close this gap. It separately declares one static
eleven-node, two-participant success DAG in a local dictionary. No
`ff_deliver()` transition appends one of those nodes, and no enumerated terminal
is converted to that DAG. The pair receipt itself has eight terminal summary
states, including two no-commit terminals; the static DAG describes only one
successful shape. No abort/rejection/release/rebase history is constructed.

Consequently G7's partial-application states and G10's `28/28` terminal types
are valid protocol-summary facts, while T2's append-only causal-closure theorem
and the terminal phrase “born records are durable causal carriers” remain
prose-level constructions.

**Required repair:** add a record-bearing companion to P4. Every accepted
transition must append a typed immutable record with structural identity,
bounded payload and explicit parents; earlier records must remain byte-equal.
For every reachable terminal:

- build the complete proposal/grant-or-reject/decision/apply-or-release/ack/
  close DAG;
- prove each accepted record's parent references exist and lie in its causal
  past;
- prove every success closure contains all required records in its ancestry;
- prove abort terminals retain their grants, rejections and releases;
- check prefix persistence after every transition; and
- quotient only independent machine delivery order, with exact alpha/projective
  comparison of the resulting marked DAGs.

Alternatively, keep the current code but narrow every earned noun to
**finite mutable protocol-state model** and remove the durable-record and
causal-closure promotion.

### M3 — the structural transaction identity names remote exact tips absent from T0's causal past

Section 3 defines

```text
tau = (initiator lower tip, local slot, ordered capability roles,
       referenced participant base tips).
```

The executable's identity exemplar accordingly puts `A7`, `B3` and `C5` into
`tau`. But its causal closure fixture gives the proposal record only one parent:

```text
parents[T0] = (A0,).
```

`A0` and `B0` are independent roots in that exact dictionary. There is no
capability/evidence record carrying the identity of `B0` into `A0` or `T0`, and
there is no path `B0 -> T0`. `B0` first joins the displayed transaction at

```text
GB <- (B0,T0).
```

Thus the two ontology gates cannot simultaneously describe one physical
fixture. If T0 physically contains B's **exact current base-tip identity**, it
has remote current information without a licensed prior ancestry path. If T0
is genuinely one-parent and knows only an initiator-held stable capability,
then the exact B base version must be supplied later by `GB` and cannot be part
of T0's initial structural identity.

This matters operationally: in a peer system B may advance between proposal
creation and prepare. A stable actor/port capability may be known locally;
B's current immutable tip is new evidence. Treating those as the same field
silently assumes the snapshot protocol D36 is meant to construct.

There is also an unresolved rebase consequence. If exact participant bases are
part of `tau`, changing a base creates a different structural identity. The note
introduces `T1` as a rebase of `T0` but does not say whether the logical
transaction identity persists while an attempt identity changes.

**Required repair:** choose one coherent model and run all identity/ancestry
gates on it:

- either include immutable authenticated capability/snapshot records in A0's
  causal past that license every exact base reference in T0; or
- define T0/tau from the initiator lower tip, local output slot and stable
  participant capability roles only, and let grants bind the exact participant
  versions after T0 exists.

In the second design, separate a stable logical transaction identity from a
version-bound attempt/rebase identity. Then prove that every identity field in
a realized record is deterministic boundary incidence or has a licensed
carried ancestry path. Do not count a nominal pointer to a remote tip as causal
evidence.

### M4 — G19's maximum parent arity three is false for the admitted arity-three transaction

The static upper-seal DAG is only a two-participant success. It has

```text
DT     <- (T0, GA, GB)        arity 3;
CloseT <- (DT, AckA, AckB)    arity 3.
```

`capacity_gate()` separately observes that the `partial` fixture admits one
transaction with three participants and prints:

```text
max_tx_arity=3;
max_parent_arity=3.
```

But applying the exact same T2 grammar to participants A, B, C requires

```text
DT     <- (T0, GA, GB, GC)             arity 4;
CloseT <- (DT, AckA, AckB, AckC)       arity 4.
```

Therefore the two numbers cannot be combined into the advertised capacity pin.
G19 passes only because it measures transaction arity on all fixtures and
record-parent arity on a different two-party fixture. It never constructs the
record DAG for the admitted arity-three transaction.

The same gate does not count the payload fields of `tau`, retry/rebase records
or any typed loser record. The finite-bit section computes retry probabilities
but constructs no retry lineage whose per-record capacity can be measured.

**Required repair:** generate the immutable record schema and closure DAG for
every fixture, especially the arity-three `P={A,B,C}` transaction, and census
the actual maximum parent count and payload fields. Then either:

- raise the campaign parent-arity bound to at least four;
- use a bounded-arity grant/ack merge tree and include its extra immutable
  records in the ancestry and born/token comparison; or
- lower transaction arity to two.

Add explicit retry/rebase and rejection record schemas to the capacity census.
Keep the honest existing statement that no bound is proved uniformly over the
universe.

## 4. Minor findings

### m1 — G0/G1 do not test structural freshness or protocol identity at their narrated width

The nominal-freshness theorem in section 7 is mathematically sound, but the
executable implements its gate as

```text
nominal_contradictions = 1.
```

No permutation or purported fresh-name function is evaluated. The structural
side hashes one `tau` exemplar and checks one hand-written rename. It does not
test:

- uniqueness of two proposals from the same lower tip and local slot;
- rejection of a duplicate structural identity;
- typed collisions between transaction, participant, event and slot domains;
- alpha covariance of P4 histories; or
- independence from a supplied global allocator.

The separate `alpha_covariance_gate()` checks four outcome kernels under one
fixture rename; it does not rename any P4 protocol state or transaction record.

**Required repair:** retain N1 as a prose theorem with its two-line permutation
proof, but do not call the hard-coded `1` an executable proof. Add typed identity
construction to the actual record-bearing P4 companion, exercise ordinary
renames and adversarial cross-domain display collisions, and show that reusing
one lower-tip/slot identity rejects before mutation. State explicitly which
local slot/ordinal resource guarantees uniqueness.

### m2 — “D24 compatibility” currently means only a one-parent graph shape

The receipt's D24 evidence is:

```text
parents[T0] == (A0,);
proposal_birth_one_parent=1;
quantum_join_derived=0.
```

It does not construct `B_g`, verify `B_g^dag B_g=I`, check
`P(T-content=1)=g P(initiator=1)`, extend identity over participant spectators,
or place physically operative proposal/priority marks in durable orthogonal
output factors. No D24 source or receipt is hash-locked by the D36 executable.

The note is otherwise admirably clear that the campaign is classical, that
the quantum join remains open, and that neither `q_birth` nor `g` is selected.
The repair may therefore be narrow.

**Required repair:** either say “one-parent causal shape, consistent with but
not an executed test of D24's quantum map,” or add a hash-locked D24 companion
gate applying the exact one-parent `B_g` on the transaction factor and identity
on spectators. Keep structural opportunity, numerical q/g selection,
multi-parent application and the quantum join explicitly open.

## 5. Finite and quantum ceiling

Apart from the over-wide G18 line and the unexecuted D24-compatibility phrase,
the note handles its ceilings correctly:

- all state spaces and priority marks are finite and explicitly bounded;
- worst-case retry-record count remains unbounded;
- almost-sure retry resolution is not a deterministic finite bound;
- failure-free fair delivery is a hypothesis;
- coordinator loss can strand a promise;
- batch closure, eligibility and arbitration are supplied;
- K1/K2/K3 remain an unselected family;
- no completed regional/all-cover law follows from the finite cells;
- D24 does not select q or g;
- no quantum join/instrument is claimed; and
- no root-free infinite history law, spacetime or actual law of nature is
  promoted.

Those limitations must survive the record-bearing repair.

## 6. Finding disposition

| Claim | Disposition |
|---|---|
| Fresh nominal atom obstruction | theorem sound in prose; executable gate vacuous |
| Structural `tau` alpha example | one exemplar passes; freshness/ancestry not established |
| P0 lock deadlock | pass |
| P1 reusable-grant double commit | pass at declared toy scope |
| P2 split adoption | pass at declared toy scope |
| P3 exclusive-wait split vote | pass at declared toy scope |
| P4 finite fail-fast summary graph | pass |
| P4 append-only immutable record law | **not executed; major** |
| T2 upper-seal ancestry for all terminals | **not linked to P4; major** |
| Born/token pair projection equality | true by construction |
| Independent born/token bisimulation | **not performed; major** |
| Parent arity three at transaction arity three | **false; major** |
| One-parent ancestry shape | pass on static two-party DAG |
| D24 `B_g` quantum compatibility | inherited/open, not tested |
| q/g/opportunity selection | honestly open |
| Quantum join | honestly open |
| Unbounded-universe eliminability | honestly not claimed |

## 7. Final disposition

**Final count:** **0B / 4M / 2m / 0n.**

Retain the exact finite control results and the P4 abstract fail-fast protocol.
Withhold the record-native causal-carrier and token-equivalence promotions.
The next candidate must make P4 append typed immutable histories, integrate
structural identity and capability ancestry into those same histories, rebuild
every upper seal from the enumerated transitions, correct the arity-three
capacity census, and compare independently implemented born and token systems
from a common pre-proposal boundary. Only then can D36 decide whether record
birth is a causal coordination carrier or a representational activation at the
declared observable scope.
