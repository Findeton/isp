# Paper 26 focused typed-carrier closing delta

**Frozen target:** `e3161f5ebf6b1e0cf1a6dcd688e370fc63d6b6c2`
**Review type:** independent three-lane focused delta against
`reviews/paper26-round1-independent-review.md`.
**Disposition:** promotion withheld.

```text
BLOCKER  1
MAJOR    3
MINOR    4
NIT      0
```

The probability core survives.  Fresh executions under seeds `271828`,
`32452843` and randomized hashing are byte-identical to the frozen receipt.
The K3/K2 theorems, the countable classical configuration-measure theorem and
all headline fractions and censuses reproduce.  S0 now validates real typed
parents and event DAGs, and S2 evaluates exact `Fraction` ratios.  The original
round-one causal-carrier blocker is closed.  Promotion is nevertheless not
earned because four typed bridges remain incomplete.

## 1. Blocker — K1 typed restriction is not parent closed

Restricting one typed `P-Q-R` K1 history to `{P,Q}` retains selection clicks
whose full-component `PRIORITY_CLICK` parent has been deleted.  The restricted
history therefore has missing causal parents and fails `validate_typed_history()`.
The registered D34 square sees only complete disconnected priority components
and does not exercise this case.

Required disposition: either construct a typed boundary event carrying the
component priority plus exterior outcomes and gate proper-region transport, or
exclude K1 from the typed region-indexed `F_D/Gamma_D` claim while retaining
its finite marked probability specification and complete-carrier witnesses.

## 2. Majors

### M1 — the D26 common line is a payload grouping, not causal ancestry

The first repair supplied three distinct root `OPPORTUNITY_PARENT` events and
overrode their `parent_line` strings.  `line_shadow()` grouped those strings,
but the roots were not a shared or sequential parent wire.  The single-Q
`431/465` value survives; the claimed represented-line basis for `64/125` and
`2744/3375` does not.

Required repair: bind every history to the carrier's declared line and build a
separate common-line fixture whose birth carriers are causally comparable.

### M2 — D36-shaped metadata are not a D36 adapter

D37 copied D36b's field order and signature formula into its own `CausalEvent`.
It did not construct a D36b `Record` or `Envelope`, and direct D36 participant
acceptance fails because D37's evidence kind and immutable-record schema are
different.  Calling these records “exact D36 PREPARE” is therefore too strong.

Required repair: construct admitted D36b `T0_BIRTH`/`SLOT_ACTIVATION` evidence,
sign an actual D36b envelope and gate `participant_accepts_prepare()`, or narrow
the output to D36-shaped signed metadata.

### M3 — finite digest identities cannot carry the countable pushforward

The countable typed-history proof used SHA-256 values as event identities and
content-derived actor indices.  A finite `2^256` identity space cannot be
injective on a genuinely countably infinite family of distinct finite
contents.  The finite receipt remains valid, but the countable typed
pushforward is not established.

Required repair: use injective mathematical identifiers, such as tagged
canonical tuples and arbitrary-precision injective actor encodings.  Retain
SHA-256 only as a serialization checksum.

## 3. Minors

1. S2's 30 traversals contain repeated edges and omit nine distinct feasible
   additions.  The paper's “30 traversed additions” is accurate, but claims
   that all 30 distinct ratios are gated are not.  Enumerate the distinct
   addition edges.
2. S7 prints 27 parent-line histories without requiring the exact count.
3. The 70-extension check validates canonical serialization of an already
   built DAG; it is not an independent actor-operation replay theorem.
4. “Parent/port carrier” exceeds the implemented object, which carries typed
   parents and wires but no port-dependency structure.

## 4. Results retained

The following survive unchanged:

```text
K3                         508 / 7,098 / 138
K2                         188 / 165 / 1,224
K1 path-five conditional   5/11, 6/11 versus 1
joint Q modes              34/93, 25/93, 34/93
joint Q selection          6/31
D26 arithmetic             64/125, 2744/3375, 431/465
finite receipt             PASS 9/9
```

No files were edited by the review lanes.  This file records their aggregate
verdict; subsequent authorship repair must receive another focused delta and
does not close itself.
