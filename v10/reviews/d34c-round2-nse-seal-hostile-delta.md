# D34c bounded-record repair — NSE/seal hostile delta

**Target:** frozen repair commit `cf33fe2`, reviewed only against
`d34c-round2-nse-seal-hostile-review.md`.  **Verdict:** **DELTA-CLEAN —
0 BLOCKER / 0 MAJOR / 0 MINOR.**  Two non-blocking precision notes are carried
below.  The repaired terminal noun is accepted at finite typed-DAG width.

## Reproduction

Fresh executions under `PYTHONHASHSEED=424242` and `8675309` both passed
`14/14` and were byte-identical to the committed output.  All three files have
SHA-256
`8349459eb2ff077578f8a9d08a761b12b98997430d9e1fd2134af83a49270cd0`.
No fraction, matrix identity, branch count, record partition, incidence check,
incoming-reception result, merge result, or remote-factor result changed under
the salts.

## Disposition of the two MAJOR findings

### M1 — incoming events versus a false stopped marginal: CLOSED

The old `3/10`, `10/108` tree is now named and gated as a
**consecutive-A-initiated conditioned specimen with non-A events suppressed**.
No current line calls it the marginal obtained by coarse-graining the timed
D34b process.  C13 explicitly leaves the timed operator-valued measure and the
infinite incoming marginal open.

C10 separately constructs the missing physical mechanism: `i(B,A)` advances
B's private ring but not A's, updates both wire tips, changes A's carrier, adds
one fresh event record, and becomes A's next predecessor.  The two-tip merge
has predecessor set `{A#r1,B#r1}` and is invariant under the two serializations
of the incomparable tips.  This does not pretend to perform the unbounded
incoming marginal; it exactly supports the new finite typed-DAG theorem.  The
scope repair is complete.

### M2 — unbounded append-only actor mailbox: CLOSED

No actor mailbox remains.  Each event allocates one new immutable event-record
factor.  Its **local evidence alphabet has exactly six values**:

- birth;
- idle;
- interaction with one of four durable `(s,o)` results.

The internal path `p` is absent.  The receipt requires one factor per event,
checks the six-symbol content set, compares the durable-signature and record
partitions in both directions, and checks that every prefix factor persists
unchanged in the final product.  Future operations act on new carrier/record
factors and do not rewrite old evidence factors.

“Bounded” is now typed correctly.  It means bounded **local evidence rank per
record**, not bounded total web size.  Initiator, target and predecessor
relations live in the typed graph incidence, with at most two incoming wire
links for this event grammar.  Link endpoints are structural relations, not an
ever-growing bit string stored inside the six-state record.  Under that
record-versus-relation ontology there is no hidden infinite local capacity;
the universe may grow by adding more bounded records.  If a future version
chooses to encode endpoint names as record payload, this conclusion would have
to be reopened, but the present note explicitly does not make that choice.

## Disposition of the five MINOR findings

1. **All-state NSE link: CLOSED.**  C9 constructs the correctly typed
   `C_(x,r,p)`, coherently sums `p` to form `K_(x,r)`, and only then forms the
   orthogonally recorded event map `W_x`.  Exact `16x16` identities establish
   `W_x^dag W_x=I` for idle, the D24 birth, and interaction with either target.
   Degree-one and degree-two scheduler closures are identity on arbitrary
   inputs.  The receipt also verifies that individual durable-result operators
   are not isometries, so the round-2 typing correction is load-bearing rather
   than narration.

2. **Preparation independence: CLOSED.**  Scheduler weights depend on the
   fixed classical graph sector and local degree only.  No scheduler choice
   reads a quantum state or durable result.  The preparation-dependent Born
   distribution of `(s,o)` is internal to `W_x`, not an external lottery.
   Graph-sector superposition remains explicitly open.

3. **Remote actor factor: CLOSED.**  C11 uses the actual A--B diamond and the
   actual disconnected P-to-P/1 D24 birth, not the old `I/X/Z` surrogate.  The
   maps commute on all 64 carrier basis vectors, the eight class branches
   agree in both orders, the canonical actor/record state agrees, and the
   complete local diamond functional is unchanged.

4. **Instrument completeness/all-m scope: CLOSED.**  The operator identities
   carry arbitrary input states for the instantiated degree-one/two sectors.
   For general positive `m`, the only additional scheduler algebra is the exact
   identity `m*(1/(4m))=1/4`; the finite-down-set theorem is explicitly
   conditional on the supplied local operation family.  No empirical finite-m
   sweep is narrated as a universal proof.

5. **Receiver and durability wording: CLOSED.**  C3 remains an exact
   class-branch embedding equivalent to inserting an orthogonal receiver at
   the `p` cut; it is not narrated as a literally evolved fifth-qubit code
   path.  C5 separately retains its honest scope: local R-algebra quarantine
   from support exclusion, with a changing relational R--S observable, not
   sealed holonomy.  Fresh event factors likewise persist by support exclusion;
   no general physical sealing law is claimed.

## Universe-ledger audit

The physical event identity is initiator-local (`actor#ring`); event type,
target and predecessors are assembled from the touched wire tips.  No live-web
census, global commit number, or universe-wide conditional enters an event
weight or operation.  `canonical_graph` and sorted dictionaries are verifier
representations that erase auxiliary serialization.  Orthogonality between
different typed graphs is the product/network-sector orthogonality of their
event factors and incidence, not a dynamically consulted universe-history
register.

The distinction is important: the total typed graph is global as a
mathematical object, just as the classical D34b history is, but no actor must
read that object to advance.  The finite construction therefore does not
reintroduce the global scheduler rejected earlier.

## Finite-down-set induction

At the declared width the induction now follows:

1. class vectors plus fresh orthogonal event-record factors give a Gram
   functional, hence strong positivity;
2. for one scheduler option, coherent internal paths are summed before the
   durable result is recorded, giving the isometry `W_x`;
3. preparation-independent normalized scheduler weights give
   `sum_x q_x W_x^dag W_x=I`;
4. summing exhaustive extensions therefore returns the earlier down-set
   functional;
5. repeating the identity proves every finite extension by induction;
6. record-disjoint incomparable operations commute, while shared-wire order
   and the two-tip merge remain physical.

The theorem is conditional on a finite typed DAG and the declared operation
family.  It does not construct an infinite Hilbert/direct-integral limit, the
timed D34b quantum measure, or the infinite incoming-event marginal.  Those
exclusions are explicit and binding.

## Non-blocking precision notes

- The executable variable `all_m_identity` evaluates the reduced constant
  identity `1/4+1/4+1/2=1`; the universal `m` step is the one-line algebra
  `m/(4m)=1/4`, carried by the theorem.  This is proof rather than a symbolic
  software gate and should continue to be described that way.
- The bounded-capacity statement relies on treating graph incidence as
  primitive bounded-degree relation rather than serializing endpoint labels
  into local evidence.  Section 17 makes this distinction correctly; it must
  remain explicit in any synthesis paper.

## Stamped terminal wording

> **D34c FINITE TYPED-DAG ACTOR/QUANTUM SEWING PASS WITH BOUNDED EVENT
> RECORDS.**  For the chosen preparation-independent scheduler weights and
> local operation family, finite typed record DAGs carry a strongly positive,
> down-set-consistent quantum history functional.  Each event contributes one
> bounded six-state durable evidence factor; graph incidence has bounded local
> degree and is not stored as an unbounded actor mailbox.  The correctly typed
> event instruments are NSE-compatible on arbitrary quantum inputs within a
> fixed classical graph sector.  Incoming reception, physical two-tip merge,
> incomparable-event gauge and an actual disconnected remote factor are
> exhibited exactly.  The timed operator-valued D34b measure, infinite
> incoming marginal, graph-sector superposition, derived NSE/weights/operations,
> sealing, joining and geometry remain open.

**Delta stamp:** DELTA-CLEAN at this wording.

