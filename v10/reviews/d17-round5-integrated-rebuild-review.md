# D17 hostile review, round 5: integrated clean-room rebuild

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-12  
**Verdict:** **PASS AT THE SUPPLIED-FILTRATION FINITE SCOPE**  
**Broader interacting-law status:** **OPEN**

The 40-check integrated packet reproduces exactly.  Both round-four exploits
now reject for structural reasons: the edge key jointly canonicalizes the
parent embedding with the new element distinguished, and it includes D16 past
and future boundary-port metadata.  Consistent relabelings of one declared
embedding still admit.

I found no adjacent material bypass.  An exhaustive small-edge census covered
19 labeled one-element extensions of every two-point strict order, producing
11 joint canonical edge classes with zero collisions between inequivalent
embeddings.  Separate attacks on boundary polarity, element, kind and owner;
element ownership; collar memory/owner; and carrier type all behaved as
declared.

The finite result therefore passes: one supplied, owner-checked filtration and
record network admit three inequivalent projective kernels under the same
action.  The result remains nonselection, not the sought action-derived click
law.  Alternate construction filtrations, the physical origin of the grammar,
kernel and commit, and continuum/geometry questions remain explicitly open.

## 1. Frozen reproduction

The following commands were repeated:

```bash
python3 v10/code/d17_integrated_causal_history_exact.py
python3 -O v10/code/d17_integrated_causal_history_exact.py
python3 v10/code/d17_integrated_causal_history_exact.py | shasum -a 256
python3 -O v10/code/d17_integrated_causal_history_exact.py | shasum -a 256
shasum -a 256 v10/code/d17_integrated_causal_history_exact.py
shasum -a 256 v10/data/d17-integrated-causal-history-exact.json
```

Both modes end with:

```text
CHECKS PASSED: 40/40
SEMANTIC SHA256: bf465b07380b96350afb929ba661fe4309b002cfcb5142b9a495876b22a92987
SOURCE SHA256: 5fffa4d676da38a64e61cdd3b01c031d6fa74d2e1119f72c35369ad7be40be57
VERDICT: INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION
```

Normal and `-O` stdout hashes are identical:

```text
b8593b3aa3f012243455904f407a2822b3e866b4ddf9a8554b6a0dc752df8398
```

The remaining receipt hashes match:

```text
packet     a9c08c3b5702dce8726f2b2b355b98398f227085ced61eedda98207d3018fa00
D14        e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16        861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
first D17  305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
```

No `assert` or `__debug__` gate occurs.  Explicit checks, count guard and
semantic-hash guard survive optimization; the packet is written afterward.

## 2. Round-four embedding exploit replay

The declared left edge extends the two-chain by a new maximal point:

```text
parent: 0 < 1
child:  0 < 1 < 2.
```

The hostile child uses the same marks, owners, collar and abstract child
isomorphism type, but inserts the new point below the parent:

```text
child: 2 < 0 < 1.
```

Round four admitted this because parent and child were canonicalized
independently.  Round five gives:

```text
is induced one-element extension                True
honest and hostile joint edge keys equal        False
grammar.admit(hostile embedding)                 ValueError: undeclared
```

`canonical_typed_edge_key` now permutes only the old `n` elements and fixes
the new element at index `n`.  The same permutation is applied jointly to the
parent and its embedded copy in the child.  This preserves the injection and
distinguishes new-minimal from new-maximal extension orbits.

A consistently relabeled honest edge still admits, confirming that the repair
retains element-label covariance inside the supplied filtration.

## 3. Round-four D16 boundary exploit replay

The joint presentation key now includes separately:

```text
flattened strict relation,
past BoundaryPort(element,kind,owner),
future BoundaryPort(element,kind,owner),
element-owner tuple.
```

I replayed the original forged future boundary and adjacent variants:

| Child modification | Result |
|---|---|
| Add foreign future boundary on maximal element | rejected |
| Add foreign past boundary on minimal element | rejected |
| Change boundary kind to `screen` | rejected |
| Change boundary owner | rejected |
| Change old element ownership | rejected |
| Replace D14 carrier with unrelated type/dimension | rejected |

Past/future polarity is represented by separate tuple positions, so swapping
polarity cannot collide.  `CausalOrder.permute` transports boundary elements,
and consistent relabeling continues to admit.

## 4. Exhaustive adjacent embedding census

To test more than the two frozen examples, I enumerated every transitively
closed three-element strict order whose first two elements form a valid
two-element parent.  This includes all labeled antichain and chain parent
presentations and every valid relationship of the distinguished new element
to them.

The census found:

```text
labeled embedded edges             19
joint canonical edge classes       11
non-equivalent same-key collisions  0
```

For each equal-key pair, I independently required an old-element permutation
that maps both parent and child while fixing the distinguished new child
element.  Every collision was exactly such a presentation relabeling; no
inequivalent insertion embedding shared a key.

This is not a universal proof for arbitrary poset size, but it directly tests
the first size where minimal, maximal and incomparable insertions differ and
supports the source's joint-canonical construction.

## 5. Grammar, owner and join controls

The previous adversarial cases continue to behave correctly:

```text
valid but undeclared edge                  rejects
foreign requested owner                    rejects
foreign new-element owner                  rejects
foreign child collar owner                 rejects
wrong carried-memory bit                   rejects
wrong owner arity                          rejects
changed old-element ownership              rejects
wrong D14 carrier signature                rejects
past-directed A/B join without entitlement rejects
same join with exact A,B entitlement        admits
```

The complete declaration identity now contains parent and child marked
presentations, element owners, D16 boundaries, collar owner, memory and the
ordered D14 carrier-port signature.  I found no remaining typed field that can
be changed while retaining the frozen edge key.

The public `declared=False` path remains a diagnostic mechanism used for the
join test; production `ext()` always invokes declared admission.  I do not
count the explicit test bypass as a grammar defect at this stated scope.

## 6. Projectivity and action scope

The equal, positive-envelope and inverse-orbit kernels remain exact:

```text
(1/2,1/2)
(9/25,16/25)
(2/3,1/3).
```

I independently iterated their deterministic unique-child continuation to
depth 100.  Every level normalized to one and every parent equaled its child
mass.  The visible depth-three conditionals remain exactly one and zero.

The fixed `N_0` action evaluates on every frozen causal node and has opposite
phases on the size-four chain and diamond leaves.  None of those action values
enters the supplied branch weights.  That is the theorem's point: the same
action and grammar are compatible with multiple kernels.

Joint canonicalization remains factorial in the number of old elements, so it
is a finite exact reference implementation rather than a scalable universe
algorithm.  The all-depth projective statement rests on the simple
unique-child induction, not on feasible factorial enumeration at arbitrary
depth.

## 7. Carrier, record and reset audit

The root memory object is the actual source of the D14 network.  Exact carrier
equalities hold at every recorded depth:

```text
node depth 1 carrier = net1.target
node depth 2 carrier = net2.target
node depth 3 carrier = net3.target
```

Later nodes preserve the complete depth-three carrier with sealed `X,Y,Z`
records and live collars.  Independent operator checks reproduce full network
isometry and reset-channel completeness.

For all three amplitude packets, the normalized record tables equal the
causal-tower tables through depth three.  Under reset, the causal path remains
the diamond path `(1,0,1)` while its visible record becomes `(1,0,0)`.  I
independently pushed the equal causal measure through that record map and
reproduced `record_table_after_reset` exactly.

Source check 31 still uses a tautological order self-equality instead of this
full pushforward comparison.  The intended statement is nevertheless true;
freezing the pushforward would strengthen the receipt without changing the
verdict.

## 8. Claim scope and remaining openings

The strongest accepted statement is:

> On one supplied finite filtration, an owner-checked, typed, label-covariant
> causal extension grammar and one local D14 record architecture are
> compatible with at least three inequivalent positive projective kernels
> under the same relabeling-invariant interval action.

Therefore the action alone does not select the kernel.  This does not establish:

- covariance or equivalence among different insertion filtrations of the same
  completed causal order;
- an action-derived `Ext(C)`, kernel, pointer basis or record commit;
- a physical law for how new records arise;
- a scalable sequential sampler or proper time;
- a BDG/continuum limit, geometry, metres, seconds, `G`, or a V9 holdout.

The round-four ledger now states the key distinction correctly: element-label
covariance inside one supplied filtration is proved; quotient/sewing across
alternate filtrations remains open.

## 9. Minor hardening notes

```text
H1 MINOR  canonical_typed_key is now unused legacy code; remove it to avoid
          confusing independent object canonicalization with the accepted
          joint edge key.
H2 MINOR  Freeze reset-table = pushforward(path measure, reset_record_map)
          rather than the current tautological unchanged-order conjunct.
H3 MINOR  Update the theorem status line, which still says it awaits round-3
          closure although the body contains the round-5 filtration scope.
```

None affects the exact packet or finite nonselection theorem.

## 10. Decision

**PASS AT THE SUPPLIED-FILTRATION FINITE SCOPE.**  The embedding and boundary
key bypasses are closed, the adjacent small-edge census finds no false
canonical collisions, and the probability, carrier, memory, reset and receipt
checks all reproduce independently.

The full investigation must continue toward selection or derivation of the
grammar and kernel.  This review closes the integrated finite compatibility
subresult only; it does not claim the final dynamic interacting click law.
