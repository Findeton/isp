# Paper 13 v3 typed-groupoid source audit — operator/category seat

## Freeze record

| field | value |
|---|---|
| audit stage | Stage C, mutually blind source audit |
| seat | operator/category |
| disposition | **NO-GO** |
| source-adjudication result | **REJECT** |
| earliest outcome rung | `P13-REFERENT-PRESENTATION-ONLY` (index 1) |
| decisive finding | `V3-OP-TENSOR-FACTOR-NODE-SUBSTITUTION` |
| ordinary SHA-256 | externally reported after freeze |
| normalized SHA-256 | `2a21ce90ec2d23fff93c98c7355a1b0baa3294324e7de310e61f707a06a2bf02` |

The normalized digest is the SHA-256 of the complete LF byte stream after
replacing only the 64 hexadecimal digits in the `normalized SHA-256` cell above
with 64 ASCII zeroes.  The ordinary digest is necessarily reported outside the
self-hashed file after the final bytes are frozen.

## 1. Authentication, custody, and blindness

Before scientific inspection I authenticated the following immutable inputs:

| object | authenticated value |
|---|---|
| repository HEAD | `8a272e98fb83e0a42cb4931173acc0d76b29afe2` |
| `v16/code/p13_gamma_exact_v3.py` | SHA-256 `cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111`; 14,941 LF lines; 595,989 bytes |
| `v16/note-paper13-typed-groupoid-source-freeze-v3.md` | SHA-256 `02e22f32ce44d46104377d77469cefc1e7c3ca82445f119ede2056c9b8d16028`; 380 LF lines; 18,271 bytes |
| `v16/note-paper13-typed-groupoid-source-delta-pin.md` | SHA-256 `44fe6f86eeb6990537b36760eda68da5ccdc31fd8d15dfe003b42e6d4324a154`; 784 LF lines; 39,364 bytes |

I read the complete freeze note and delta pin.  I did not read, list, request,
infer, or communicate with the sibling source-audit report or auditor.  I did
not inspect future artifacts.  The candidate, notes, ledger files, corpus, and
Git index were not modified.  The only repository path written by this seat is
this report.

The authenticated HEAD and all three immutable file hashes were rechecked
unchanged immediately before report creation.

## 2. Independent reconstruction before implementation inspection

I wrote a no-import reconstruction in private off-tree scratch before reading
candidate implementation semantics.  Its frozen facts were:

| field | value |
|---|---|
| private reconstruction | `/private/tmp/p13-v3-seat-a.nQBVdd/independent_v3_operator.py` |
| size | 481 LF lines; 19,176 bytes |
| SHA-256 | `f4a060587fd25619180bd27117bf6b45af6afc1e0ee83e77b4d597bb5dc98d66` |
| exit/runtime | RC 0; approximately 0.06 s |
| stdout SHA-256 | `61ad93d708d75f58386705bcce4fd08cb18b1e98943c4de9f0564bc2030e968f` |
| canonical result SHA-256 | `e238b9fdba9e2fa41f340c0c0dbdc874e3af294a556ca3ef77a9d25097641f91` |

The reconstruction included exact `SourcePresentation` and witness types,
total sparse-map completion, address-and-role-bound `BoundaryNode` values,
target-derived configuration action, identity/inverse/composition/
associativity/tensor laws, address-collision controls, operator/Gamma
covariance, and exact rational `R`, `B`, `C`, `B2`, and `K` values.  Its tensor
contract requires each factor node to be the literal root `SOURCE` node whose
boundary is a component of the reconstructed tensor root.

## 3. Black-box execution ledger

Only the permitted `--selftest` mode was used on the immutable candidate.  The
forbidden `--generate-fresh` and `--run` modes were never invoked.

| environment | RC | runtime | stdout bytes | stdout SHA-256 | stderr SHA-256 |
|---|---:|---:|---:|---|---|
| repository root | 0 | 226.78 s | 234,018,261 | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` | `7c2f0d56bf433e5e3b26afb6429e12fff389a607e5c30905e1e55cd258a469a7` |
| alien current directory | 0 | 274.73 s | 234,018,261 | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` | `72cfe472b61a82a6f29ce07739993ba45914f73dcf20519ce422f1d87906a074` |
| true one-file directory, no `.git` | 0 | 273.48 s | 234,018,261 | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` | `eeee5631d5700b58a134315041de943199801f14e2102fbfe82418d108c87ff5` |

All three executions stayed below the 300 s cap and produced byte-identical
stdout.  The one-file directory contained only the candidate copy, whose hash
matched the authenticated source, and contained no `.git` entry.

Independent parsing found schema `p13-gamma-exact-v3`, status `PASS`, 49 checks,
and 149/149 registered/executed/killed development mutations.  The registered
mutation-name tuple hashed to
`bf00b700b51305b38afbe2bc2c514c7307eb3b2d77959d63a74a7848ec11bf8c`.
The payload declared no fresh/artifact reads and zero publication writes.  Its
normalized payload digest recomputed exactly as
`43aa7476d76315329bb7bd464131c8f3ac35e797c1fef249decc63b4c29d7955`.

These passing runs do not cure the independently found semantic counterexample
below: the registered tensor mutation severs a stored reference after using
proper root factor nodes; it does not test substitution of a different node
from inside the same factor presentation.

## 4. Source audit completed before the stop boundary

The static audit reached and checked the following surfaces before the first
counterexample:

- `SourcePresentation` builds complete carrier tuples from the root and every
  child Arrow boundary, and validates the sealed Arrow exactly.
- sparse role/matter/port/occurrence maps are completed over their entire
  carriers and checked for totality, injectivity, surjectivity, and type;
- `SourceGroupoidWitness` requires its target to equal the complete relabeling
  of the source Arrow;
- identity, inverse, and composable witness constructors retain the typed
  source and target presentations;
- `BoundaryNode` binds literal boundary semantic bytes, an AST address, and an
  endpoint role;
- `act_configuration` has the exact public three-argument surface, verifies
  membership in the witness source presentation, derives the target at the same
  address and role, and admits no caller-supplied target;
- identity, inverse, composition, and associativity action rows retain their
  presentations, witnesses, transports, nodes, configurations, and equality;
- tensor action source typing was inspected through the decisive failing gate.

Per the assignment, scientific inspection stopped at the first reproducible
semantic counterexample.  Later source surfaces are therefore not offered as
independently accepted by this report.  The black-box suite did exercise its
declared A1--A16, `A-SOURCE-CORE`, and `A-SOURCE-ASSERT` controls, but that fact
cannot override the missing tensor factor-node invariant.

## 5. Decisive counterexample

### 5.1 Required contract

For a tensor action row built from factor witnesses `L : P_L -> P'_L` and
`R : P_R -> P'_R`, the supplied factor source nodes must reconstruct the
components of the tensor source node.  In this API that means exactly

```text
left_node  == boundary_node_at(L.source, (), "SOURCE")
right_node == boundary_node_at(R.source, (), "SOURCE")
```

before factor configurations may be combined into the root tensor
configuration.  Mere membership somewhere in each presentation is weaker and
does not type a tensor component.

### 5.2 Fault in the frozen source

In `tensor_action_row`, frozen lines 5535--5542 reconstruct and check the tensor
root node, but check factor nodes only by membership:

```python
expected_tensor_source = boundary_node_at(tensor_presentation, (), "SOURCE")
if tensor_source_node != expected_tensor_source:
    raise Refusal(...)
if left_node not in boundary_nodes(left_witness.source) or right_node not in boundary_nodes(
    right_witness.source
):
    raise Refusal(...)
```

Lines 5543--5547 then build the root tensor configuration from whatever factor
configurations were supplied.  They do not establish that those configurations
belong to the factor boundaries used by `tensor_arrow`.  Lines 5555--5560 act
on the arbitrary member nodes, while lines 5561--5569 act on the tensor root
and compare only configuration values.  No node equation reconstructs the
tensor target from the two factor target nodes.

### 5.3 Smallest exact witness

The counterexample uses only public frozen constructors and an identity action:

1. Build `control = build_record_control("v3_tensor_wrong_")` and take
   `left_arrow = control["recorded_chain"]`.  This composition has root source
   node `()` with the record port mode `ACTIVE`, while child `(1,)` is the second
   generator's source and has that port mode `CARRIED`.
2. Let `left_witness = identity_witness(left_arrow)`.
3. Supply `left_node = boundary_node_at(left_witness.source, (1,), "SOURCE")`
   instead of the required root node
   `boundary_node_at(left_witness.source, (), "SOURCE")`.
4. Use a one-generator right factor with its correct root source node and its
   identity witness.
5. Choose catalogue index 0 for each factor and build the declared root tensor
   configuration with `_tensor_configuration_from_factors`.
6. Call `tensor_action_row` with the wrong internal left node.

The two left boundaries are semantically different:

| coordinate | required root | supplied internal node |
|---|---|---|
| AST address | `()` | `(1,)` |
| endpoint role | `SOURCE` | `SOURCE` |
| boundary-semantic-bytes SHA-256 | `dde29c8f6c024f000608c5793ac057ee5a212ec668304af0de8fc30ecc9079cf` | `8c2ae144f6d502914b909dd1efec9caca96c6c4f75dc23ce1db7d48624c68acd` |
| record-port presentation mode | `ACTIVE` | `CARRIED` |

Nevertheless, the catalogue configurations compare equal because a
`Configuration` records context, matter assignment, and sector assignment but
not the boundary port presentation mode.  The tensor configuration therefore
validates against the root tensor boundary even though its purported left
factor node is not that boundary's left component.

### 5.4 Independent private-copy replay

To obey the no-import rule, I copied the authenticated candidate to private
off-tree scratch and changed only the body of the registered named-development
mutant `CONFIGURATION-TENSOR-SEVER` into the witness above.  The repository
candidate was neither imported nor edited.

| replay field | value |
|---|---|
| probe file | `/private/tmp/p13-v3-seat-a.nQBVdd/tensor_probe.py` |
| probe SHA-256 | `f4e421c0be6c5bbd182d8f9ce5c25022af1fb42600f237e64e5cecc3c7044bd1` |
| probe size | 14,980 LF lines; 597,175 bytes |
| command | `python3 tensor_probe.py --mutant CONFIGURATION-TENSOR-SEVER` |
| process result | RC 0; 0.80 s |
| top-level result | `status = FAIL` |
| mutation result | `status = SURVIVED`, `pass = false`, `changed = true` |
| refusal | `NO-REFUSAL` |
| returned row | `tensor_row_returned = true`, `tensor_row_exact = true` |
| factor boundary mismatch | `true` |
| left configurations equal | `true` |
| evidence SHA-256 | `da3b494fa3bbbb408c046b163a7bc95c5b31abb4f0af5cb87a87d4f866445a52` |
| replay normalized payload SHA-256 | `418c424f758511d8455dadb01b9a2316984d180ac81772a79c1e40b032cdd05d` |
| replay-declared outcome drop | `P13-REFERENT-PRESENTATION-ONLY` |

This is a total, deterministic, sub-second counterexample.  It does not depend
on Git, an artifact, a registry, a caller-supplied target, floating point,
pointwise ontology, or a metric.

## 6. Why this is decisive

The returned `exact = true` row purports to certify tensor naturality for three
actions, but its left factor action is based at a boundary occurrence that is
not a component of the tensor source object.  Thus the row is not well typed as
the claimed tensor action law.  An action law that accepts a same-presentation
internal node substitution is a presentation-only certificate, not a complete
typed tensor witness.  The earliest applicable rung is consequently
`P13-REFERENT-PRESENTATION-ONLY`, not a later operator or numerical rung.

This finding is not a hidden point or metric promotion.  It is an exact equality
failure between finite, serialized source objects: two `BoundaryNode` values
have distinct addresses and distinct literal boundary bytes.

## 7. Literal minimum repair and required regression

Before combining factor configurations, add the exact root-source gate:

```python
expected_left_source = boundary_node_at(left_witness.source, (), "SOURCE")
expected_right_source = boundary_node_at(right_witness.source, (), "SOURCE")
if left_node != expected_left_source or right_node != expected_right_source:
    raise Refusal("tensor factor node is not its factor root source")
```

The tensor law row should also explicitly retain and compare the derived factor
target root nodes against the two components of the reconstructed tensor target
root.  Add a named development mutation using the exact `recorded_chain` witness
above and require refusal before any `ConfigurationActionLawRow` is returned.
The existing post-hoc transport-reference sever does not cover this input-typing
attack.

## 8. Claim and scope disposition

| surface | disposition |
|---|---|
| complete typed witness category | no contrary example found before stop |
| total sparse completion | no contrary example found before stop |
| target-derived one-edge action | no contrary example found before stop |
| identity/inverse/composition/associativity | no contrary example found before stop |
| tensor action/naturality | **rejected by exact counterexample** |
| full operator/Gamma naturality | not independently promotable after tensor failure |
| source sufficiency / anti-wrapper | not independently promotable after tensor failure |
| v3 source adjudication | **NO-GO** |

The result-neutral scientific values and the passing black-box output are not
altered by this audit.  This report makes no claim beyond source adjudication.
In particular it preserves the Barandes nondivision scope and every permanent
ontology wall: no stochastic-process ontology, trajectory ontology, hidden
sample space, point-set carrier, metric, or topological structure is introduced
or inferred.

## 9. Final declaration

The first reproducible semantic counterexample is the accepted internal-factor
node substitution in `tensor_action_row`.  Under the frozen stop rule, it is
decisive.  Disposition: **NO-GO**, earliest rung
`P13-REFERENT-PRESENTATION-ONLY`.
