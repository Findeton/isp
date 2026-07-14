# D37 round 2 — regional-specification closing delta

**Frozen repair target:** commit
`94de860d96c8d6e6565267be3b08f4ba66e19ef5`.

**Parent review:**
`reviews/d37-round1-regional-specification-hostile-review.md`.

**Lane:** only the `0B/1M/3m/0n` findings frozen in round 1.

**Independence disclosure:** this is the coordinator's focused D37 closing
delta.  It closes the D37 receipt-hostility stream, not the independent Paper
26 review.

**Verdict:** **CLOSED — `0B/0M/0m/0n`.**

## 1. Fresh reproduction

I ran the repaired executable under `PYTHONHASHSEED=67867967` and `86028121`.
Both runs exited zero, were byte-identical to each other and were
byte-identical to the committed output.  Both print `PASS 9/9`.

The frozen repair hashes are:

```text
source
8a8772f878d725ce1f22acc703cd23accd531ca0ebb8a08af2bc01eca92f7f4a

complete stdout / committed receipt
6d0f9ed7bb703e7b17f9836453115b2dd14e9ada74bc9f9fd493deb4798fc9b7

printed stdout body
91a0cb3a85aca73d4cc78266ef29f0a4bdac8cf7a44406a7e258a3d71bb7f5c7

internal science
cf9997407d8cb8b974f442ab341b7f4d3e6a1b3d3db3c43c6c4207189c0df0bf

note
9f266c76adbccd9057605a069f56dca38e067ddec69e47eba7e081e73163ee38

Paper 26 candidate
caa07cc443e206bf93408c7ab6599190f67b6381ae3b9261bfb4b25d94babbb2
```

`git diff --check 94de860^ 94de860` is clean.

All frozen numerical results are unchanged:

```text
K3                         508 / 7,098 / 138;
K2                         188 / 165 / 1,224;
K1 path                    {Q}:1/3, {P,R}:2/3;
K1 path-five witness       5/11, 6/11 versus 1;
joint Q modes              34/93, 25/93, 34/93;
joint Q selected           6/31;
D26 joint-Q factor         431/465;
finite-cover checks        99;
covariance/factorization   6/6 and 4/4.
```

## 2. M1 closure — complete marked K1 factorization

The repair adds `product_priority(left,right)`.  For every left and right
`PriorityAtom`, it concatenates the component-order marks, unions the selected
sets and multiplies the exact rational probabilities.  S8 now requires

```text
priority_law(two_pairs)
  == product_priority(priority_law(left_pair), priority_law(right_pair)).
```

This is complete atom-by-atom equality, not an atom-count proxy.  The selected
left marginal remains as a separate local anti-dilution gate.

A clean-room enumeration of the product gives exactly four marked atoms:

```text
P<Q | R<S    selected {P,R}    1/4;
P<Q | S<R    selected {P,S}    1/4;
Q<P | R<S    selected {Q,R}    1/4;
Q<P | S<R    selected {Q,S}    1/4.
```

Their mass is one, and the repaired production law is identical.  M1 closes.

## 3. m1 closure — exact forcing premises

Paper 26's Theorem 1 now assumes only:

1. exact positive support on every feasible configuration; and
2. fixed feasible-addition ratios
   `mu(x union {v})/mu(x)=lambda_v`.

Those are exactly the premises used by the deletion-path proof.  K3's
accepted one-hop Markov boundary is now stated separately as a locality
property of the constructed kernel.  The paper no longer calls the unused
Markov premise load-bearing.  m1 closes.

## 4. m2 closure — K2 radius two

The paper and post-receipt note now derive the width explicitly: a selected
blocker lies at distance one, while deciding whether a rejected distance-one
exterior vertex remains an unmet demand may inspect one of its selected
neighbors at distance two.  The countable continuity proof and the
anti-dilution paragraph use that exact width.

The receipt prints:

```text
K2:two-hop-blockers+domination-demands.
```

m2 closes.

## 5. m3 closure — witness is fail-closed

S4 now includes `bool(one_hop_witness)`.  Removing the retained path-five
witness would therefore fail the gate rather than merely print an empty row.
The exact witness remains unchanged.  m3 closes.

## 6. Final disposition

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

The D37 hostile stream is closed.  This authorizes describing the D37 receipt
as hostile-closed at its exact finite and stated analytical scope.  It does
not promote Paper 26 beyond candidate status.  The independent paper reviewer
must still reconstruct at least one K1 path-five count and one joint
`34/93`-family count rather than relying on either D37 review.
