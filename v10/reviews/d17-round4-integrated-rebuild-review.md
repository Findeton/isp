# D17 hostile review, round 4: integrated clean-room rebuild

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-12  
**Integrated-packet verdict:** **MAJOR REVISION**  
**Finite fixed-action kernel-nonselection theorem:** **PASS**

The 38-check packet is exactly reproducible, and most round-three repairs are
real.  Normal and optimized Python have identical output and reproduce every
receipt hash.  Former owner, collar, memory, carrier, relabeling, past-join,
isometry, reset-completeness and reset-map attacks now behave as intended.
The causal carriers are the actual successive D14 network targets, and direct
unique-child induction remains projective through depth 100.

One load-bearing grammar defect remains.  `canonical_typed_key` canonicalizes
the parent and child as two independent typed objects; it does not canonicalize
the **extension embedding**.  Consequently the declared edge that extends a
two-chain by a new maximal point also admits an undeclared extension by a new
minimal point, because both have the same abstract parent and child posets.
The key also omits D16 past/future boundary ports, so a child with a newly
forged typed boundary is accepted as the declared boundary-free child.

These counterexamples do not alter the displayed three kernels or the narrow
nonselection theorem.  They prevent acceptance of the stronger claim that the
supplied `Ext(C)` is now a complete typed, gauge-covariant admission law.

## 1. Frozen reproduction

The following executions were repeated:

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
CHECKS PASSED: 38/38
SEMANTIC SHA256: addbfd1a0324b9ca26906361e42be731dbe0531660628a7db3ebe33cd614e7b2
SOURCE SHA256: 1e934d2630aaae6ece9670b10132ab4f1c3f87d92c17c148ac699fd2209c0640
VERDICT: INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION
```

Normal and `-O` stdout hashes are identical:

```text
1c520ddbfe0822a62c7e86ae7e80dc3305952bfb3a3aca66a5f28783242f18f4
```

The packet and dependency hashes match the receipt:

```text
packet     397f35deafa549731b43c01886ecade5f8981651d13aca222b3a6430dcd84624
D14        e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16        861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
first D17  305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
```

There is no Python `assert` or `__debug__` gate.  The explicit checks, final
count guard and semantic digest survive optimization, and the packet is
written only after they pass.

## 2. Round-three counterexamples replayed

I repeated the old attacks rather than relying only on the new source checks.
Their disposition is:

| Attack | Round-four result |
|---|---|
| Consistently relabeled `chain2 -> chain3` | admitted |
| Foreign new-element owner | rejected |
| Foreign child collar owner | rejected |
| Wrong carried-memory value | rejected |
| Unrelated carrier type/dimension | rejected |
| Owner tuple with wrong arity | rejected |
| Changed old-element ownership | rejected |
| Past-directed two-owner join, no entitlement | rejected |
| Same past join, exact `A,B` entitlement | admitted |
| Empty/non-unit-start/nonbinary/projectively inconsistent tower | rejected cleanly |

The new owner checks preserve the old owner tuple, require the new element to
belong to the requested live-collar owner, validate the child collar owner and
memory, and compute the exact next carrier type.  The join guard now counts
both `old<new` and `new<old` comparabilities, closing the orientation bypass.

## 3. All-depth causal and projective reconstruction

The frozen depth-six tree still consists of one root and two nodes at every
positive depth.  Every child restricts to its parent; the right path contains
the relabeled `V3 -> diamond4` edge; and later nodes add one maximal element.
The fixed `N_0` action evaluates on all nodes and has phases `(-1,+1)` on the
size-four leaves.

I independently iterated the deterministic continuation formula for all three
kernels through depth 100:

```text
equal              (1/2,1/2)
positive envelope  (9/25,16/25)
inverse orbit      (2/3,1/3)
```

Every level normalizes and every parent equals its unique child's mass.  The
source's canonical grammar was also executed through depth seven, producing
15 valid nodes and a projective tower.  Canonicalization exhausts `n!`
permutations, so depth seven already takes roughly twelve seconds and direct
large-depth execution is impractical.  That is a performance ceiling, not a
failure of the simple mathematical induction.

## 4. Carrier and record composition is repaired

The root's dimension-two memory carrier is passed directly into
`local_record_network`.  Exact object equalities now hold:

```text
depth-one node carrier   = net1.target  (dimension 8)
depth-two node carrier   = net2.target  (dimension 32)
depth-three node carrier = net3.target  (dimension 128)
```

Every later causal node preserves the complete depth-three carrier, including
sealed `X,Y,Z` record IDs and the emitted live collars.  A wrong carrier no
longer passes merely by sharing a dimension.

Independent matrix checks reproduce:

```text
V_record^dagger V_record = I_2
sum_r K_r^dagger K_r      = I_32.
```

For equal, positive-envelope and inverse-orbit amplitudes, every normalized
record entry through depth three equals the corresponding causal tower entry.
The exact distributions remain:

```text
000/101 = 1/2,1/2
000/101 = 9/25,16/25
000/101 = 2/3,1/3.
```

Thus the former parallel-carrier defect is repaired at the declared finite
record depth.

## 5. Reset map separation is correct

The reset still changes the visible record distribution to:

```text
000 -> 1/2
100 -> 1/2.
```

Round four now represents causal paths and visible records by separate maps:
the underlying right causal path remains `(1,0,1)` and still denotes the same
diamond order, while its reset-dependent record becomes `(1,0,0)`.  I pushed
the equal causal measure through this reset record map independently; the
result equals `record_table_after_reset` entry for entry.

The source's second equality in check 29 compares the diamond order to itself
and is tautological, but the complete independent pushforward establishes the
intended statement.  This is a receipt-hardening opportunity, not a remaining
mathematical defect.

## 6. New bypass: independent canonicalization forgets the embedding

A causal extension is not determined solely by the isomorphism types of its
parent and child.  It also includes the inclusion map—or equivalently, the
distinguished new child element and its relations to the old elements.

The declared left edge is:

```text
parent: 0 < 1
child:  0 < 1 < 2, with new element 2 maximal.
```

I supplied a different induced extension with the exact same marks, owners,
collar and abstract order types:

```text
parent: 0 < 1
child:  2 < 0 < 1, with new element 2 minimal.
```

Both children canonically become the unique abstract three-chain.  Therefore
the independently computed parent key, child key and collar keys equal the
declared edge, even though the extension embedding is different.  The hostile
result is:

```text
is_one_element_extension       True
same canonical child type      True
grammar.admit(...)              True   # should reject as undeclared
```

This is not merely a labeling change: a three-chain has no automorphism taking
its maximal element to its minimal element.  The two insertions are distinct
orbits of embeddings.  The current key fixes presentation covariance by
quotienting away precisely the information that `Ext(C)` must retain.

**Required repair:** canonicalize the entire extension jointly, with the new
element or parent injection distinguished.  For example, minimize one marked
child structure containing relation, owners, boundary data and an old/new
flag, under permutations that transport that complete structure.  Do not
canonicalize parent and child independently.

## 7. New bypass: D16 boundary ports are absent from the typed key

`CausalOrder` contains typed and owned `past_boundary` and `future_boundary`
ports.  `canonical_typed_key` calls `order.permute`, but its returned candidate
contains only:

```text
flattened relation matrix,
element_owners.
```

It discards the relabeled boundary tuples.  I took the honest declared
`chain3` child and added a valid future boundary port on its maximal element:

```text
BoundaryPort(element=2, kind="screen", owner="foreign-boundary").
```

The relation, external owner tuple, marks and collar were unchanged.  The
hostile result is:

```text
same canonical_typed_key as boundary-free child  True
grammar.admit(...)                               True
```

Thus the key is typed with respect to the separate `element_owners` tuple and
D14 collar, but not with respect to the D16 causal boundary type it claims to
canonicalize.  This also contradicts any claim that all boundary ports are
transported into the key.

**Required repair:** include canonicalized past/future polarity, element,
kind and owner for every D16 boundary port, or enforce and validate that all
`CausalOrder` boundary lists must be empty because the external `Collar` is
the only permitted boundary representation.

## 8. Adjacent validator and coupling audit

The current frozen nodes themselves are well formed and the three displayed
laws do not exploit either canonical-key collision.  The action remains
evaluated rather than used to generate the kernels, exactly as the stated
nonselection ceiling requires.

The remaining material weakness is confined to grammar identity:

```text
probability validator        repaired
owner/collar/carrier checks  repaired on frozen and hostile variants
past/future join touching    repaired
record/reset composition     repaired at depths one through three
extension embedding key      incomplete
D16 boundary key             incomplete
```

The source still accepts a public `declared=False` mode for diagnostic join
tests; production `ext()` always uses declarations, so I do not count that
test hook as an additional bypass.  Likewise, factorial canonicalization is a
scalability issue rather than a counterexample to the finite theorem.

## 9. Finding ledger

```text
R4-1 MAJOR  Parent and child are canonicalized independently, erasing the
            extension embedding. A declared maximal insertion authorizes an
            undeclared minimal insertion between the same abstract posets.
R4-2 MAJOR  canonical_typed_key omits D16 past/future BoundaryPort data; a
            forged typed boundary is admitted as the boundary-free child.
R4-3 MINOR  Reset/path separation is mathematically correct, but source check
            29 does not itself compare the reset table with the map pushforward.
R4-4 MINOR  Exhaustive n! canonicalization limits executable depth even though
            the deterministic projective induction remains exact.
```

## 10. Decision

**PASS** the exact fixed-action kernel-nonselection theorem, the three finite
probability packets, record-carrier composition, local memory/reset witness,
and deterministic projective induction.

**MAJOR REVISION** remains necessary for the integrated `Ext(C)` claim.  A
typed causal extension is a morphism/embedding, not just a pair of typed
objects.  Freeze a joint canonical edge key and either include or explicitly
forbid D16 boundary ports, then replay both hostile counterexamples before
closure.

No geometry, scale, `G`, proper-time or final interacting-universe-law claim is
licensed by this conditional result.
