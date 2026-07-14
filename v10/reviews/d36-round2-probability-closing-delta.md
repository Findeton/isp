# D36 round 2 — probability/capacity/replay closing delta

**Frozen target:** commit
`63314a24cfd181793034763fcec9fdb701ddb6b2`

**Round-one base:**
`v10/reviews/d36-round1-probability-hostile.md`

**Lane:** component-local K1 marks, disjoint marked-law factorization,
four-proposal capacity census, finite-bit retry scope, hard-core boundary
support, G2/G21 nonvacuity, external replay integrity and preservation of the
K1/K2/K3 numerical cells

**Verdict:** **PASS — CLOSE THE ROUND-ONE PROBABILITY/CAPACITY LANE.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

The two round-one majors, two minors and one nit are all repaired at their
registered scope.  I found no new mathematical or probability-scope error.
The repaired result remains a finite supplied-boundary family, not a selected
arbitration law, retry-opportunity theorem or infinite history measure.

## 1. Reproduction and frozen integrity

I reran the reference executable independently at hash seed `314159`.  It
exited zero, printed `PASS 22/22`, and reproduced the committed receipt.  I
then ran the separate replay checker, which executed both the reference and
actor-record companion under seeds `17` and `104729`, compared every stdout
byte with the two committed receipts and printed `PASS 8/8`.

The frozen hashes independently recompute as:

```text
reference source
dad183c2e303b0315fa7f452ab1c197569d6983332696421d70f04ba5b3d0743

reference complete stdout / committed receipt
3478d1447ee54a33599d9d1e3b00b63cfa323ed7df1a44e3915b13da62545093

reference internal science
a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor-record source
5813304446d267dc3d08f520f4db991bf6bdb94ae45b1f96a5e0cc2a094996ba

actor-record complete stdout / committed receipt
8e2e9b9ad6de8ad7ebef4554c2eef32f20b1ffead33a7af6f89f6251e0d8b41d

actor-record internal science
ab275cc69ef529bceba96c7cb484232a5c4b661e9cd1a902c695067bd04193a4

replay-checker source
878f0a1daa08db30974bf06e7075a9952faa18d569d74286eea2ed51011f2ec6

replay-checker committed receipt
b89689d1570e2bb50a101dabb50c6390c1a6d2f08bef8bcd2844b5c505882313
```

`git diff --check 5f6cd7f..63314a2` is clean.  The note's source, stdout,
science and replay-source identifiers agree with the files at the frozen
commit.

## 2. Round-one M1 — physical K1 factorization: closed

The ontology is now unambiguous.  A K1 physical mark is not one global order
on every proposal in a disconnected region.  It is one independently sampled
strict order on each connected component of the conflict graph.  Cross-
component comparisons do not exist in that physical mark.

For the registered union

```text
C1 = {P,Q}, with P--Q;
C2 = {R,S}, with R--S,
```

the full mark space is literally the Cartesian product

```text
Sym(C1) x Sym(C2).
```

Each factor has two orders.  There are therefore four physical marked atoms:

```text
(PQ,RS), (PQ,SR), (QP,RS), (QP,SR),
```

each with probability

```text
(1/2)(1/2) = 1/4.
```

This is full marked-law factorization by construction, before applying the
greedy accepted-set map.  It is not merely equality of local marginals.
Relabeling gives a bijection of the component permutation sets, so the uniform
marked law is alpha-covariant as well.

The old global presentation has `4! = 24` strict orders.  Restricting a global
order to the two components forgets only the interleaving between two
two-element sequences.  Every product atom consequently has exactly

```text
binomial(4,2) = 6
```

preimages.  Thus its quotient probability is `6/24 = 1/4`.  My independent
enumeration returned exactly

```text
quotient atoms       4
fiber multiplicities 6,6,6,6
```

matching the receipt's `24 -> 4` account.  Greedy acceptance maps the four
physical atoms to the four accepted sets

```text
{P,R}, {P,S}, {Q,R}, {Q,S}
```

with probability `1/4` each.  The executable also checks that this
component-mark pushforward equals the earlier global-presentation K1
pushforward.  The shared-coin negative control remains supported only on
`{P,R}` and `{Q,S}` with probability `1/2` each and therefore correctly fails
product factorization.

The repair chooses the first ontology allowed by round one: independently
sampled component marks.  Calling the six interleavings construction gauge is
therefore harmless bookkeeping, not the deletion of a physical mark after the
fact.

## 3. Round-one M2 — capacity census: closed

The pin now says at most four proposals in one audited region, and the census
includes the auxiliary four-proposal disjoint-factorization fixture.  The
exact audited maxima are:

```text
transaction arity                    3
participants in one fixture          4
proposals in one audited region       4
incident contenders per participant  2
priority bits per printed chunk       2
```

The named fixture proposal counts are `2,3,2,2,3`; the auxiliary union has
four.  The ad hoc right factor and alpha-renamed path have no larger field.
The former false `max_proposals=3` statement is gone from the active pin,
gate and receipt.  G19 requires the complete tuple `(3,4,4,2,2)` and passes.

This remains a finite campaign capacity statement.  It is not a uniform
universe-wide incidence bound, and the note still says that scalable growth
would require such a bound or a bounded-arity merge construction.

## 4. Round-one m1 — finite-bit events: closed

The receipt now prints two different events under different names.

For a fixed finite single-winner contest, the unique-greatest probability is

```text
U(k,M) = k/M^k * sum_(s=0)^(M-1) s^(k-1).
```

Independent reconstruction gives:

```text
(k,M)  unique greatest  expected attempts conditional on continued iid retry
(2,2)       1/2                            2
(2,4)       3/4                            4/3
(3,2)       3/8                            8/3
(3,4)      21/32                          32/21
```

For a complete one-chunk strict order, all marks must instead be distinct:

```text
P(complete order) = (M)_k / M^k.
```

That gives:

```text
(k,M)  all distinct
(2,2)      1/2
(2,4)      3/4
(3,2)        0
(3,4)      3/8
```

All eight rows are exact and match the receipt.  In particular, the old
ambiguity at `(3,2)` is removed: `3/8` resolves a single-winner contest but
cannot create a complete three-way order in one chunk.

The almost-sure sentence is also properly conditional.  For the one-bit pair,
five continued independent attempts leave unresolved mass

```text
(1 - 1/2)^5 = 1/32.
```

The note and receipt now require the history law actually to supply the iid
retry sequence and explicitly deny a bounded worst case.  They do not claim
that these rows realize K1 on every conflict graph.

## 5. Round-one m2 — DLR support accounting: closed

For one activity value, each of the three path vertices has four formal
outside assignments.  At endpoint P, the outside assignment `{Q,R}` has zero
mass because Q and R conflict.  Symmetrically, `{P,Q}` has zero mass when R is
the target.  All four outside assignments for middle vertex Q have positive
outside mass because `{P,R}` is feasible.  Therefore, per activity,

```text
positive-mass conditionals = 3 + 4 + 3 = 10;
zero-mass boundaries       = 1 + 0 + 1 = 2.
```

At the two registered activities this is exactly

```text
tested positive mass 20
skipped zero mass      4.
```

The code now counts both branches, G14 requires exactly `20` and `4`, and the
prose limits the displayed DLR equation to admissible positive-mass outside
configurations.  No undefined zero-mass conditional is being smuggled into
the theorem.

## 6. Round-one nit — K1 attribution: closed

K1 now invokes P6/T3's greedy rule.  It no longer points to T1, the fail-fast
closed-attempt theorem.

## 7. G2, G21 and external replay — nonvacuity disposition

### G2

The reference checker now retains the full `45`-node, `69`-edge held-lock
graph, constructs the inert-ticket-decorated node and edge sets, forgets the
ticket field and compares both projected sets with the original graph.  The
circular-wait terminal is present and the projection is exact.

This construction is definitionally decorated rather than an independently
generated alternative protocol.  That is sufficient for N2's explicitly
conditional claim: **if** ticket birth leaves held-resource transitions
unchanged, inert birth cannot remove the deadlock.  The note does not use G2
as evidence about the independently implemented P4 actor protocol, which is
tested separately.  The former literal `same_graph` print with no graph
construction has therefore been repaired without inflating its scope.

### G21

G21 is no longer assigned `True`.  Before inserting G21, the executable
requires the existing key sequence to be exactly `G0,...,G20` and every one
of those 21 values to be a true Boolean.  Omitting, renaming or failing a prior
gate makes G21 fail.  Source, stdout-body and science hashes are then computed
from the executed source/report/science object.

The executable cannot authenticate its own expected source hash without an
external pin.  That role is correctly separated into the replay checker.

### External replay

The replay checker pins both executable source hashes, launches each in a
fresh subprocess under two different hash seeds, rejects stderr, checks
same-source byte identity and compares the result with the corresponding
committed receipt.  Its `PASS 8/8` is therefore nonvacuous:

```text
4 successful seeded executions;
2 within-source byte-identity checks;
2 committed-receipt equality checks.
```

I observed the fresh checker reproduce both printed stdout hashes and its
committed four-line receipt exactly.

## 8. K1/K2/K3 and restriction controls — unchanged

No probability-law value moved during repair.

On the path `P--Q--R`, K1 accepts Q exactly when Q is first among the three,
which occurs in two of six orders.  Hence

```text
K1({Q})   = 1/3;
K1({P,R}) = 2/3.
```

The two maximal independent sets are `{Q}` and `{P,R}`, so

```text
K2({Q})   = 1/2;
K2({P,R}) = 1/2.
```

The five K3 independent sets are

```text
{}, {P}, {Q}, {R}, {P,R}.
```

Thus activity one gives `1/5` each, while activity two gives weights
`1,2,2,2,4`, partition function `11`, and probabilities

```text
1/11, 2/11, 2/11, 2/11, 4/11.
```

The raw K1 restriction remains `{P}:2/3, {Q}:1/3` versus the direct edge's
`1/2,1/2`.  The K3 boundary mixture remains exact.  These are still finite
nonselection and restriction examples; the note explicitly leaves the
physical selector and all-region specification open.

## 9. Final disposition

Round-one probability findings close as follows:

| Round-one item | Round-two disposition |
|---|---|
| M1 physical K1 mark discarded before factorization | closed by component-local product marks and exact 24-to-4 quotient |
| M2 four-proposal fixture absent from capacity pin | closed by max-four pin and auxiliary-fixture census |
| m1 unique-greatest conflated with complete order | closed by separate exact rows and retry conditioning |
| m2 zero-mass DLR boundaries hidden | closed by explicit `20+4` accounting |
| n1 K1 points to T1 | closed by P6/T3 attribution |
| G2 printed but did not construct isomorphism | closed at inert-ticket conditional scope |
| G21 assigned literal `True` | closed by prior-gate census plus external replay |

The closing ceiling is unchanged and scientifically important:

```text
K1, K2 and supplied-lambda K3 remain competing candidate families;
the closed eligibility boundary remains supplied;
continued retry opportunities remain supplied;
no starvation, infinite completion or quantum-history measure follows.
```

Final tally:

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Recommendation:** close the D36 probability/capacity hostile lane.  The
round-one contradictions are repaired without changing the finite arbitration
numbers or overstating selection and infinite-liveness scope.
