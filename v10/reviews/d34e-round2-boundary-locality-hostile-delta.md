# D34e round 2 — independent boundary/locality hostile delta

**Frozen target:** commit `bd143fb`, compared with the round-1 findings in
`d34e-round1-boundary-locality-hostile-review.md`.

**Exact verdict:** **BOTH PRIOR MAJORS CLOSE; ONE FRESH OUTPUT/GAUGE MAJOR
PREVENTS A CLEAN DELTA. THE PHYSICAL B3 ALL-FUTURE CONSTRUCTION SURVIVES.**

**Count:** **0 BLOCKER / 1 MAJOR / 3 MINOR / 0 NIT.**

The replacement is a genuine repair, not a narration patch. It now has an
independent physical B3 updater, explicit B3-to-B2/L maps, separate nominal-
relabeling and construction-order covariance campaigns, ordered regional
composition, endpoint-port ownership, a capacity/minimality ledger and an
executable verdict machine. My independent multi-event and associativity
attacks found no hidden global update.

The remaining major is narrower but exact. The executable claims to test the
declared count-bearing C/L output and transport role-labeled output under the
root relabeling used by E6. It does neither. Adding the frozen A-own/A-wire
counts to the actual output alphabet changes the registered finite predictive
classes from the committed `(29,29,29)` to `(111,111,111)`, and the
role-labeled closed formula generates `A/1` after transporting the root
`A -> R`, while the actual renamed law generates `R/1`. The physical B3 state
contains enough information, so this does not refute its sufficiency; it does
make E4's “true predictive partitions” and E6's “transports role outputs”
claims false as receipt statements.

## 1. Reproduction

The repaired executable reproduced at fresh salts `17`, `65537` and `541`.
The declared salts produced byte-identical stdout with:

```text
stdout SHA-256
b168723596fde346b227e6e96f9a00d0304740a498f834809d42afbab346f9bc

source SHA-256
e3d3daee3297174183b970299df3289a03ce5491349aa1c43acc2a3a14d26533

internal summary SHA-256
88ce0efb91521151d098bc8f68a132cf6b4fc3278d9be032785817a2452714c3
```

All `13/13` program predicates evaluate true. `git diff --check` is clean.
The review findings concern whether those predicates implement the frozen
physical and query-level gates.

## 2. Prior finding disposition

### Round-1 M1 — construction-order covariance was replaced by actor relabeling: CLOSED

E6 now separates the two notions.

For nominal covariance it transports the complete state, event rows, Ulam
actors and freshly generated children. For construction covariance it applies
every registered pair of disjoint write-support rows in both orders and
compares both the complete state and B3 projection. The frozen campaign reports

```text
relabel rows    = 35,898,
disjoint swaps  = 120,276,
mismatches      = 0.
```

The analytic scope is also correct: disjoint touched/created actor and event-
record supports commute, whereas events sharing a wire are not declared
incomparable. Physical time marks are retained while only auxiliary commit
serialization is exchanged. No fixed-global-depth locality inference is made.

The fresh role-output problem below does not reopen this result for the
physical B3 carrier. The required disjoint-update construction gauge itself is
now present and passes.

**Disposition:** **CLOSED.**

### Round-1 M2 — reduced tuples closed, but physical B3 did not: CLOSED

The repair freezes one concrete record-carried object:

```text
root-owned carrier/ring/birth/wire row,
root-owned endpoint ports,
neighbor-owned eligible-degree and birth-ordinal rows,
shared incident edges,
elapsed time from the conditioning stop.
```

`b3_update` consumes only old B3, a relative-time increment and a typed event
view. It has separate rows for root birth, root idle, root outgoing, silent
neighbor birth and passive incoming interaction. An event outside the
projected boundary changes only elapsed time. The program then compares this
update with direct projection after every one of the `35,898` full-state rows
and prints explicit maps to B2 and the role-labeled state.

I independently composed the following six-event path:

```text
B birth                  [silent boundary update]
B -> A                   [passive incoming]
A birth
A idle
B/1 idle                 [irrelevant global event]
A -> B
```

with six unequal rational elapsed increments. Updating B3 without rereading
the full state matched direct projection after every event. The final values
were

```text
root row = (carrier 0, own rings 3, births 1, wire events 4),
elapsed  = 2131/2520.
```

This simultaneously exercises silent, passive, own-ring, wire-count,
irrelevant-event and additive-time behavior. E4 supplies the next-boundary
survival `exp(-q Delta t)`; exponential memorylessness licenses omission of a
renewal-age coordinate. The inherited nonexplosive strong-Markov theorem then
applies at fixed time and the two monotone count-hitting stops.

The carrier is genuinely distributed. A neighbor birth changes that
neighbor's owned degree/birth row; it does not require writing A or consulting
disconnected history. The reference Python execution remains centralized, but
the ideal update rule and carrier ownership are record-local in the stated
graph-star sense.

**Disposition:** **CLOSED.**

### Round-1 m1 — composition and port/edge ownership: CLOSED IN SUBSTANCE, fresh m1 below

Edges are now one shared object and endpoint ports are separately owned.
Composition is tested in both orders over `159,734` registered disjoint region
pairs and agrees with direct projection. I additionally tested a three-region
specimen:

```text
(M_A union M_B) union M_(A/1)
    = M_A union (M_B union M_(A/1)).
```

It passed exactly. The valid-message set-union theorem is sound. The remaining
minor concerns fail-closed validation of malformed source messages, not
composition of carriers generated by `region_message`.

### Round-1 m2 — incomplete capacity/identity ledger: PARTIALLY CLOSED

The repair now declares radius, actor/reference count, endpoint ports, shared
edges, degree bits, root counters, nominal handles, relative continuous time,
renewal-age scope and bounded-alternative/minimality scope. It correctly says
this B3 is unbounded and a different bounded carrier remains open.

One bit-cost omission remains in fresh m2.

### Round-1 m3 — unbounded B3 was overread as excluding all bounded carriers: CLOSED

E8 now says exactly:

> this B3 has unbounded port/identifier/integer width, while a different
> bounded physical carrier and minimality remain open.

The Poisson argument proves unbounded support for B3's incident count; it is
not used as a universal no-bounded-encoding theorem.

### Round-1 m4 — role-label/fresh-name schema: NOT CLOSED; promoted to fresh M1

The physical nominal carrier is repaired, but its role-labeled output formula
is not transported by the executable. This is the fresh major below.

### Round-1 n1 — stale pre-receipt status: CLOSED

The header now distinguishes the historical pin, rejected provisional receipt,
frozen replacement protocol and replacement receipt awaiting delta review.

## 3. Fresh MAJOR

### M1 — the declared count-bearing and role-labeled output kernels are not the kernels E4/E6 test

There are two exact manifestations of one typing problem: the carrier state is
now correctly rich, but the output maps used to claim predictive equivalence
and gauge covariance omit part of the frozen query.

#### 3.1 E4 omits A-own/A-wire counts from the durable output

Branch C was frozen to retain at every A-wire event:

```text
event kind/direction,
A carrier after the event,
A-own-ring count,
A-wire-event count,
time coordinate.
```

The repair adds the two counts to `boundary_scoped` and updates them correctly.
But `global_projected_rows` still emits only labels such as

```text
A-idle:c0
incoming-to-A:c1
```

and `carrier_predictive_signature` treats that label—not the count fields in
the successor carrier—as the durable output. At horizon zero it deliberately
forgets the raw successor state. Consequently histories that differ only in
their current absolute counts remain identified at every tested horizon.

The committed result is:

```text
registered states/classes = 111 / (29,29,29).
```

I repeated the same exact coinductive construction while adding the successor
A-own/A-wire values to each non-silent output label. For the actually frozen
query the result is:

```text
absolute-count output classes = (111,111,111).
```

Thus E4's “TRUE FINITE PREDICTIVE PARTITIONS” noun and its printed class counts
do not apply to Q_C as written. Either:

1. include the two counts in every durable C/L output mark; or
2. explicitly change the query to count **increments from the conditioning
   stop** and register count-translation gauge, as was done for elapsed time.

Merely storing the counts inside B3 proves that B3 can predict them; it does
not make a partition that erased them the declared query partition.

#### 3.2 E6 does not transport role outputs and the closed formula is root-name dependent

E6's PASS label says nominal relabeling “transports role outputs,” but its
relabel loop compares full states and B3 carriers only. It never compares
`global_labeled_rows` or `labeled_formula_rows`.

The omission exposes an exact mismatch under the root transport used by E6.
For the seed state and mapping

```text
A -> R,
B -> X,
```

the actual renamed generator emits the birth mark and successor

```text
A-birth:R/1:c0,  neighbor R/1,
```

whereas `labeled_formula_rows` is hard-coded to emit

```text
A-birth:A/1:c0,  neighbor A/1.
```

The two marked row counters are unequal. The physical B3 updater is correctly
parameterized by `root` and the underlying law is nominally covariant; what is
missing is a single declared chart/transport rule for the **output kernel**.

Repair by either:

- requiring all gauge maps to fix the literal distinguished name `A` and
  testing only root-fixing maps; or
- parameterizing `labeled_formula_rows(root, boundary)` and checking the
  conjugacy equation

  ```text
  T_g Rows_A = Rows_(gA) T_g
  ```

  for marks, successor states and fresh children.

Add the count marks from §3.1 to that same regression. Until this is done, the
physical C/L carrier theorem remains supported, but the committed E4/E6 output
gates and the unqualified role-labeled verdict are not exact.

## 4. Fresh MINOR findings

### m1 — the composition validator accepts missing ports and phantom owners

For valid `region_message` inputs the composition theorem passes. But the
replacement protocol also says typed union validates exactly-once port
ownership and rejects corruption. Only duplicate shared-edge metadata is
corrupted in E7.

Two independent attacks were accepted without exception:

```text
1. remove A's endpoint port from M_A, then compose M_A with M_B;
2. add a phantom Z-owned port and A--Z edge to M_A while Z is neither owned
   by nor referenced from the region, then compose with M_B.
```

`compose_messages` checks the internal consistency of each port tuple but does
not check that the owner belongs to `region/owned`, that every incident edge
has the required owned endpoint port, or that every external peer has a
boundary reference.

Add a message validator before union and corrupt independently:

- absent endpoint port;
- phantom owner or reference;
- edge with no owned port;
- duplicated port owner;
- inconsistent reference, edge and peer fields.

This is minor because every directly constructed message is valid and the
arbitrary-region union identity survives. It prevents the validator from being
advertised as a complete physical ownership gate.

### m2 — the capacity ledger does not count every field in the frozen B3 schema

The schema stores for every neighbor both

```text
(eligible degree, locally owned birth ordinal),
```

but the bit ledger counts only `sum ceil(log2(degree+1))`. It does not count
the neighbor birth ordinals, root carrier bit, or the concrete shared-edge and
endpoint-handle encodings. The nominal-identifier row says the encoding is
unbounded, which is honest, but the promised complete per-carrier comparison
still lacks a total formula. The stdout also prints only `capacity fields=10`
rather than the ledger values.

Either remove/prove redundancy of neighbor birth ordinals or count them; then
print the complete ledger. The continuous-time entry is now correct: one
relative real coordinate with ideal precision uncalibrated, and no renewal-age
field only because the chosen clocks are exponential.

The omission cannot reverse the unbounded-width conclusion.

### m3 — `bounded=False` conflates proved unboundedness with unknown capacity in the verdict machine

Paper 21's growing-carrier row requires a proof that the constructed carrier's
physical width is unbounded. `decide_branch` instead selects that row whenever

```text
core gates pass and bounded == False.
```

But `False` is also the default used before any capacity theorem is supplied.
The unit specimen for row 3 therefore tests the implementation's conflation,
not the frozen scientific criterion.

Use separate flags such as

```text
bounded_proved,
unbounded_proved,
capacity_unknown,
```

and require `unbounded_proved` for `ALL-FUTURE GROWING-CARRIER PASS`. The actual
C/L B3 branch can set it from E8's Poisson/ledger proof, so its substantive
verdict is unchanged. This is a decision-protocol repair, not a counterexample
to B3.

## 5. Hostile attack ledger

| Attack | Result |
|---|---:|
| Byte reproduction, salts 17/65537 | exact |
| Additional salt 541 | `13/13` |
| Physical B3 one-row updates | `35,898/35,898` |
| Six-event silent/passive/irrelevant/time path | exact |
| Disjoint full/B3 update swaps | `120,276/120,276` |
| Valid ordered region compositions | `159,734/159,734` |
| Three-region associativity probe | pass |
| Root-transported L formula | **fail** |
| Absolute-count predictive classes | **111,111,111, not 29,29,29** |
| Missing-port corruption | **accepted** |
| Phantom-owner corruption | **accepted** |

No attack found a dependency on disconnected history, a central histogram
stored in A, a reset of A's private clock on passive reception, or a hidden
bounded-degree assumption.

## 6. C/L all-future verdict at delta strength

The mathematical carrier construction now has the ingredients needed for an
all-future result:

1. the arbitrary-state generator partition depends only on B3;
2. the physical updater closes under root, passive, silent and irrelevant
   events and deterministic elapsed-time flow;
3. the inherited nonexplosive pure-jump theorem gives the all-future law and
   strong Markov property at fixed-time and local count stops;
4. disjoint incomparable construction updates commute;
5. valid typed regional carriers compose by ordered set union;
6. B3 has unbounded incident-port and identifier support;
7. no bounded alternative or minimality theorem is claimed.

Therefore the fresh major does **not** reveal a nonlocal or global hidden
update. It shows that the executable's finite output quotient and nominal
role-output gate are not the declared ones. The honest split is:

```text
Branch C physical B3 carrier:
    ALL-FUTURE GROWING-CARRIER theorem structurally earned;
    committed finite Q_C partition receipt needs count-mark repair.

Branch L physical B3 carrier:
    all-future growing carrier structurally supported;
    role-output covariance gate not yet receipt-clean.
```

No relativistic conclusion follows. “Local” still means actor-star read scope,
bounded touched/write support and a distributed record carrier. Its radius is
one but its degree, port count, identifier cost and ideal time precision are
not bounded. The reference executable remains a central evaluator; it is not
evidence for independent hardware threads, Lorentz covariance, a light cone or
proper time.

## 7. Openings before the closing delta

### O-A — repair the exact output alphabet once

Freeze whether time and counters are absolute or increments from the
conditioning stop. Put every retained output field into C/L marks, parameterize
the L formula by the distinguished root, and gate nominal conjugacy of marks,
successors and fresh names. Recompute the finite partitions; do not preserve
`29` as a target if absolute counts remain licensed.

### O-B — fail-closed physical message validation

Validate each regional message before composition and run the full corruption
battery above. Keep the valid-message arbitrary-region set-union lemma and
ordered/associative regressions.

### O-C — finish the capacity and decision ledgers

Print every stored B3 field's count/bit/continuous cost and make capacity a
three-way proved-bounded/proved-unbounded/unknown status in the decision
machine.

After O-A, the fresh major should close without changing the physical B3
generator. O-B–O-C are receipt-hardening minors. Both round-1 majors require no
further scientific repair.

## 8. Exact delta disposition

| Item | Disposition |
|---|---|
| Round-1 M1 construction-order covariance | **CLOSED** |
| Round-1 M2 physical B3 recursive closure | **CLOSED** |
| Round-1 m1 valid typed composition | **CLOSED IN SUBSTANCE** |
| Round-1 m2 capacity/identifier ledger | **PARTIAL — m2** |
| Round-1 m3 bounded-alternative scope | **CLOSED** |
| Round-1 m4 role/fresh-name output gauge | **OPEN — M1** |
| Round-1 n1 status header | **CLOSED** |
| Fresh malformed-message ownership attacks | **m1** |
| Fresh verdict capacity typing | **m3** |

**Terminal count for `bd143fb`: `0B / 1M / 3m / 0n`.**

The replacement is much closer to the intended theorem than the provisional
receipt. The remaining major is an exact output-schema/gauge mismatch, not a
failure of distributed locality or recursive physical closure.
