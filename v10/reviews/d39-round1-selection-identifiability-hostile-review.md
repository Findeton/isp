# D39 round-one selection and identifiability hostile review

**Frozen target:** commit `a9af380`.
**Receipt:** `PASS 10/10`, complete-output SHA-256
`36f6984f4ca68c895d0b64573f87e749cb4fcf9bbfbf5ffac59cc92615a1b64c`.
**Lanes:** category/causal software; probability/selection; corpus/physics
scope.
**Verdict:** `4 BLOCKERS / 5 MAJOR / 3 MINOR / 1 NIT`.
**Promotion:** withheld.  Paper 28 remains held.

Fresh executions under hash seeds `0`, `1`, `7`, `19`, `101` and `999`
reproduce the committed stdout byte for byte.  The source, stdout-body,
internal-science and complete-output hashes reproduce as

```text
3f976eff94a28ee7cd8551b37ddad1fab81b358dcadad3e9e37dba3fac520e06
3586e702a55a9cada88e111b5886d2b974ef4fadba18d6f9561a48199d4e4c91
51cdf3a29872a097f8a492353728a207afd3fe40dcef2e8166ada90b761de1b5
36f6984f4ca68c895d0b64573f87e749cb4fcf9bbfbf5ffac59cc92615a1b64c
```

The rejection is not a reproducibility complaint.  Several gates do not
exercise the mathematical object named by their output, and H1 has exact
soundness failures omitted from the twenty-case battery.

## 1. Independent derivations that survive

### 1.1 The projected D38b commuting square

At the initial A--B star the relevant rates are

```text
root birth       1/4
root idle        1/2
root out         1/4
B birth          1/4
B incoming       1/4
total            3/2.
```

Root idle leaves these rates unchanged, so

```text
P(idle then B-birth) = (1/3)(1/6) = 1/18.
```

B-birth changes B's degree from one to two.  The incoming rate becomes `1/8`
and the new total is `11/8`, hence

```text
P(B-birth then idle) = (1/6)(4/11) = 2/33.
```

The two star updates commute but the path products differ.  This negative
result is correct and important: the projected relevant-event kernel does not
descend to that action quotient.

### 1.2 Finite packet and visibility arithmetic

Independent enumeration of positive integer quadruples in `{1,2,3,4}^4`
finds 32 solutions of `w_x w_(y|x)=w_y w_(x|y)` and 224 failures.  D26's
conditional factors are also correct: at `g=9/25`, one same-line BORN factor
is `4/5`, three give `64/125`, and dormant TOKEN gives one.

### 1.3 Pinned cancellation arithmetic

The D31B rational rotations multiply to the identity after the declared four-
plus-four sequence, while the intermediate squared response is `576/625`.
This is a valid inherited cancellation control.  It is not yet a D38b quantum
join.

## 2. BLOCKER B1 — R1 never constructs a D37 comparison functor

The executable hash-locks D37 but never imports or instantiates it.  `Phi`
maps a D38b `RegionView` into a new local `OrientedView` dataclass and maps a
star action into

```text
("D39_ORIENTED_ATOM", action_tag, target).
```

No D37 `OrientedCell`, incoming/base/parent-line row, lateral proposal,
generated row, `CausalEvent`, legal history or regional kernel appears.  The
identity, composition and update tests are D38b direct-versus-staged
restriction tests followed by the same deterministic projection.  Kernel
pushforward is an injective renaming of D38b path atoms.

Worse, the image contains `digest(view.witness)`, the hash of the complete
global admission witness.  Two equal regional boundaries with different
global completions therefore have different images.  That is the opposite of
the promised regional target and makes the displayed comparison depend on the
global data Paper 27 left open.

The triple-cover row does not repair this.  It is a standalone three-bit
anticorrelation example unrelated to either category.  Its printed `10/10`
is the sum of three pair normalizations, six singleton marginals and one empty-
triple-support predicate, not ten functorial cover checks.

**Required repair.**  Import the locked D37 carrier.  Define explicit source
objects, target objects and morphisms; map D38b typed parent/frontier data into
actual D37-compatible incoming/lateral rows; remove global witness identity
from the regional image; push finite kernels onto target histories; and gate
identity, composition, restriction and update on both sides.  If this cannot
be done, rename the result a D38b-oriented projection and withdraw the D37
comparison theorem.

## 3. BLOCKER B2 — H1 is unsound and is not a typed causal protocol

Two omitted attacks accept exactly.

First, replace the authentic A--B edge credential's source record by
`FOREIGN_SOURCE`, keep the endpoints and issue the model's ideal edge
signature over that foreign source.  `verify_h0` checks only that the signature
matches its own fields.  `commit_h1` never compares `edge.source` with
`ledger.edge_sources`.  The interaction accepts and mutates the ledger.

```text
foreign_edge_source_accepted = True
state_mutated                = True
```

Second, `release_h1` does not verify the certificate, signatures, attempt/body
binding or complete grant census.  A forged one-grant fragment naming one
public `(wire,head,attempt)` triple removes that lock from a legitimate two-
wire attempt.  A conflicting attempt can then collect on the released wire.

```text
forged_partial_release          = True
locks_before / locks_after      = 2 / 1
conflicting_collect_afterwards  = True
```

The protocol is also procedural rather than causal.  There are no durable
`HEAD_PREPARE`, `HEAD_GRANT`, decision, apply/release or acknowledgement
records, no parent relation proving decision-after-grants, and no typed record
validator.  A tuple in `LocalLedger.locks` is the authority.

These are direct failures of R4 soundness and of the pin's D36-style typed
causal carrier.  The reported `20/20` battery is incomplete.

**Required repair.**  Bind edge credentials to the ledger's authenticated
edge source; authenticate all-or-none release; add the missing attacks; and
realize prepare/grant/decision/apply-or-release/ack as typed causal records
whose parents enforce the protocol order.  Failed protocol transactions must
remain byte-identical.

## 4. BLOCKER B3 — R5 does not classify the pinned admissible family

R5 enumerates one unconstrained four-number cube and checks one multiplicative
equation.  The rank is assigned as the literal integer one and the positive
dimension as `4-1`.  No regional object, nested region, locality row,
covariance row, restriction row, normalization gauge, action coboundary or
record-closure condition enters the calculation.

The correct D38b negative square is embedded next to this toy census, but it
does not turn the census into a classification of

```text
A_D39 = record-closed + Level-A natural + action-compatible
        + finite all-transport kernels.
```

**Required repair.**  Build the exact finite constraint matrix on the actual
comparison cells, derive its rank rather than printing it, enumerate or
parameterize its positive solutions and gauges, and report whether chosen
D38b belongs.  A narrow theorem classifying only the one-square increment
variety is acceptable if named honestly; the current selection-family claim
is not.

## 5. BLOCKER B4 — R7 never computes the O-U causal-DAG law

`typed_order_law` is simply the outer product of a normalized two-entry actor
vector and a normalized three-entry mode vector.  It has no state, target role,
causal parent, record history, incomparable serialization or gauge pushforward.
Projective injectivity of this rank-one product table is elementary, but it is
not the declared O-U law of typed untimed causal DAGs.

The O-L negative is tautological.  Two arbitrary dictionaries called
`ou_silent_a/b` are unequal, while

```python
retained_star == dict(retained_star)
```

is always true.  No two parameterized generators are pushed through the D34e
star projection.

The Paper 21 shared-wire masses are correct constants, but they are hardcoded
and do not establish the D39 family theorem.

**Required repair.**  Enumerate finite typed causal histories, quotient their
linear extensions, sum the embedded path weights into O-U atoms, and compute
the exact collision set.  Separately push two explicit rate packets through
the O-L projection.  Until then, withdraw “gauge-pushed O-U identifiability.”

## 6. MAJOR M1 — certificate equivalence is not exhaustive at registered scope

The pin requires every registered finite D38b history and proposed
birth/idle/interaction.  R4 checks one sequential birth, one idle and one
interaction, plus attacks based almost entirely at the initial seed.  It does
not enumerate the registered reachable history cells, both interaction
directions, child interactions, later birth ordinals or proposals after
independent advances.  Even after the two soundness bugs are fixed, the printed
finite-cell sufficiency needs an explicit finite registry and exhaustive
oracle comparison.

## 7. MAJOR M2 — the all-transport gate omits root-law covariance

The path-three automorphism exchanges endpoints 0 and 2.  The non-covariant
root vector

```text
(p0,p1,p2) = (1/6,1/3,1/2)
```

passes `mtp_holds`, although `p0 != p2`.  The executable compares the transport
matrix rank with the number of vertex orbits minus one but never restricts its
probability columns to automorphism-invariant root laws.  Rank agreement alone
therefore does not prove the displayed uniform-root classification.

**Required repair.**  Work directly with rooted-isomorphism-orbit masses, or
gate covariance and reduce the transport matrix to one variable per root
orbit before computing rank and its positive normalized kernel.

## 8. MAJOR M3 — R9 does not use the pinned preparation/query alphabet

The active states and `{Z,X}` queries are printed but never passed into a
response calculation.  `exact_nonzero_distances=12` counts the abstract
numbers `2^-r`, and both finite cutoffs are the same scalar inequality.  The
“hypothetical exact-zero cut” is the tautology `Fraction()==0`.

The summable versus nonsummable shell distinction is correct as an abstract
tail lesson.  It is not yet an operational-width theorem at the D28/D31B
alphabet.

**Required repair.**  Calculate exact response vectors for every declared
preparation/query pair under the registered attenuation maps, derive their
distances and omitted-tail bounds, and keep the absence of a D38b quantum join
explicit.

## 9. MAJOR M4 — the printed D36 vocabulary is not exact

R2's vacuity conclusion is correct: chosen D34b emits no `PROPOSAL` record and
therefore no contended base-version cell.  But the claimed future vocabulary is
a local eight-string set containing generic `DECISION`; D36b uses typed
`DECISION_COMMIT`/`DECISION_ABORT` records and distinct transaction carriers.
The count is returned by `len(PROPOSAL_KINDS)` rather than by inspection of the
locked D36b ontology.

**Required repair.**  Derive the adapter vocabulary from D36b constants and
record constructors, distinguish the generated proposal carrier from the
subsequent protocol, and keep the valid empty-conflict theorem.

## 10. MAJOR M5 — the receipt aggregates inherited controls as new gates

The D26 factors, Paper 21 masses and D31B cancellation are arithmetically
correct, but D39 retypes the numbers rather than calling the locked
constructors or comparing parsed locked output.  R8/R9 should label these rows
hash-locked inherited regressions.  New D39 evidence begins only where a new
bridge or parameterized pushforward is actually computed.

## 11. Minors

1. The R7 heading says “UNTYPED/TYPED,” while only the synthetic typed table
   is enumerated.  No untyped collision census exists.
2. `complete_witness_metadata_retained=1` is presented as positive evidence,
   although the retained global witness digest is precisely what blocks a
   regional comparison.
3. R2 reports `future_D36_vocabulary_rows=8` by adding and subtracting an
   unrelated `nonproposal_rows>0` flag.  The printed number is stable but its
   derivation is not semantic.

## 12. Nit

The first-receipt note calls the eighteen doubly rooted orbits “the complete
basis.”  Some yield zero balance rows.  “Complete orbit census, with the
nonzero balance rows forming the tested basis” is the exact wording.

## 13. Retained result and repair order

The following core survives:

- D34b's generated conflict image is empty at the chosen scope;
- H0 static signed heads fail by authentic staleness;
- the projected D38b commuting square has products `1/18` and `2/33`;
- the finite mass-transport idea, common-scale null direction, D26 conditional
  factors, summable/nonsummable tail distinction and D31B cancellation are
  valid ingredients once their scopes are repaired.

Repair in dependency order:

```text
typed D37 comparison
  -> typed causal H1 and exhaustive oracle equivalence
  -> actual action/transport classification
  -> actual O-U/O-L pushforwards
  -> pinned-alphabet operational calculation
  -> Paper 28.
```

No Paper 28 claim should be drafted from commit `a9af380`.
