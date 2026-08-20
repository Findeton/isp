# Paper 13 v3 typed-groupoid source-audit adjudication

Date: 2026-08-20

Status: **SOURCE NO-GO / `P13-REFERENT-PRESENTATION-ONLY` / FRESH BARRED**

## 1. Authority and adjudication rule

This note jointly adjudicates the two mutually blind source audits required by
the result-neutral v3 source-delta pin at
`v16/note-paper13-typed-groupoid-source-delta-pin.md`, ordinary SHA-256
`44fe6f86eeb6990537b36760eda68da5ccdc31fd8d15dfe003b42e6d4324a154`
and normalized SHA-256
`354b28c183622d61dcf643df4e1c654130f50e8c2ab5be9b34bbe4da357ab76a`.
The source under audit is
`v16/code/p13_gamma_exact_v3.py`, SHA-256
`cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111`,
committed at `8a272e98fb83e0a42cb4931173acc0d76b29afe2`.  Its freeze note is
`v16/note-paper13-typed-groupoid-source-freeze-v3.md`, ordinary SHA-256
`02e22f32ce44d46104377d77469cefc1e7c3ca82445f119ede2056c9b8d16028`.

The frozen reports are:

| seat | report | commit | ordinary SHA-256 | normalized SHA-256 |
|---|---|---|---|---|
| operator/category | `v16/review-paper13-typed-groupoid-v3-source-operator.md` | `ec3100ef38ff782bb146edba70061d1f2236c27f` | `51e1a028c4e7d74fda2f1fe975d24a04e5925525916de1ba006ada80c2771a76` | `2a21ce90ec2d23fff93c98c7355a1b0baa3294324e7de310e61f707a06a2bf02` |
| records/integrity | `v16/review-paper13-typed-groupoid-v3-source-records.md` | `98f3340728043c9f2fea7d3c20f851aba228e239` | `1d0ceba5fca290399f8e24dfbf07b69c1b4758dfbc57c6e87cea9d5ac2cf9148` | `e58661b3e691e4acb0dd6502123471cb62690512b3d232175501c1634e0eaaa4` |

The reports contain 276 and 399 LF-terminated lines respectively.  Each seat
authenticated the same source, pin, and freeze note before science, completed
an independent no-import reconstruction, used development modes only, and
wrote only its assigned report.  The authorized report commits advanced the
shared HEAD without changing any pinned candidate byte.

There is no majority rule.  A single exact counterexample defeats a universal
source-groupoid claim.  Here both seats independently return `NO-GO` at
`P13-REFERENT-PRESENTATION-ONLY`, through different failures in the purported
complete action.

## 2. Independent adjudicator reconstruction

The adjudicator read both reports completely, reauthenticated all five frozen
objects above, and inspected the exact source functions on the claimed
backward slices.  A separate standard-library-only, no-import checker at
`/private/tmp/p13_v3_source_adjudicator.py`, SHA-256
`7311b972695ec11a940accdd353d87ce43b8e25aee8fdc592a9b26d8bcb2d622`,
imports no candidate function and changes no repository byte.  Its canonical
payload SHA-256 is
`572432205a74ca0e1b1bad4c4c7d9ab1c2239c3de4ac2ea13399b6eef08ea138`
and returns:

```text
both_reproduced                         true
tensor_factor_root_binding_absent      true
packet_swap_current_clause_true        true
packet_swap_actual_identity_false      true
producer_absent_from_static_slice      true
earliest_rung                          P13-REFERENT-PRESENTATION-ONLY
fresh_authorized                       false
```

The checker confirms that `tensor_action_row` admits any boundary node found
somewhere in each factor presentation, rather than requiring the exact root
`SOURCE` node used to build the tensor source.  It also reconstructs the
complete-census consumer on two distinct identity inputs and shows that a
whole target-packet swap preserves every current clause while making both
identity actions false.

## 3. Accepted KILL A — tensor factor provenance is not root-bound

The operator/category report's decisive object is accepted in full.

The frozen `tensor_action_row` correctly reconstructs the tensor source
presentation and requires the supplied tensor source node to equal its root
`SOURCE` node.  But for its factor inputs it checks only:

```text
left_node  in BoundaryNodes(left_witness.source)
right_node in BoundaryNodes(right_witness.source)
```

It never requires:

```text
left_node  == boundary_node_at(left_witness.source,  (), "SOURCE")
right_node == boundary_node_at(right_witness.source, (), "SOURCE")
```

Nor does it explicitly bind the transported factor targets to the root target
components from which the tensor target is reconstructed.

The exact counterexample supplies, as the left factor node, an internal node
at AST address `(1,)` rather than the required root `SOURCE` node at `()`.
The two boundary semantic hashes are distinct:

```text
required factor root  dde29c8f6c024f000608c5793ac057ee5a212ec668304af0de8fc30ecc9079cf
supplied internal     8c2ae144f6d502914b909dd1efec9caca96c6c4f75dc23ce1db7d48624c68acd
```

The chosen configurations happen to compare equal, so product reconstruction
passes.  The function returns a `TENSOR` law row with `exact=true` instead of
refusing the wrong provenance.  The independently hashed evidence is
`da3b494fa3bbbb408c046b163a7bc95c5b31abb4f0af5cb87a87d4f866445a52`.

This is not a harmless duplicate presentation.  `BoundaryNode` was introduced
precisely to retain AST address and endpoint provenance when semantic
boundaries coincide.  A tensor action that accepts an internal factor node in
place of the declared factor root does not establish functorial action on the
typed tensor source.

## 4. Accepted KILL B — identity target packets are not attached to input keys

The records/integrity report's decisive object is accepted in full.

The complete certificate-action census has correct literal inputs, complete
content-addressed bytes, independently rebuilt targets, and derived pairing
keys on its clean path.  The failure is in what the promotion consumer proves
about their attachment.

For two distinct global identity rows, with inputs

```text
344071d781ad56d73f2568269959a7eea4c94aaed8f324e19c8643af83a1b60b
d7e62bac853cc9e5e08b31e198cfeeb159aa6b8d51e620ae9f2c4b4a566f76e3
```

the counterexample swaps as one packet:

```text
literal_transport_ref
independent_rebuild_ref
transported_pairing_key
```

The source input reference, original pairing key, object store, target
multiset, cardinalities, and operation counts stay fixed.  Both target objects
remain valid complete bytes; literal transport still equals independent
rebuild within each changed row.  The complete-census predicate and
`groupoid_promotion_predicate` remain true.  Yet each identity target is now
the other row's input, and the transported pairing keys are crossed.  Thus
both identity actions are false.

The clean and changed complete-action hashes are:

```text
clean      2dc822de1dfcc90ac33105e09a8e1f758660999faa12a6d6f81d56df5c60bcc9
malformed  fb0f81baa8e1a2e091dcf19de024c13c10bc258fe39427a94cf1facaee705f3b
```

The crossed pairing keys are:

```text
296a64a9ac0110e206d950a5aaaf70403c8b3e2fa3040ae47ef4d87469f673b9
f38d5d5feeb238744ba70b8d570b4625d3ed713513f4cb352a9c260864404ebf
```

The implementation gap is exact:

1. `_certificate_triple_reference_exact` proves content membership and
   target self-equality, but not the original-to-target action or recomputed
   pairing-key attachment.
2. `_complete_certificate_action_census_exact` requires the triple's
   `original_ref` to equal `input_ref`, but does not require its identity
   target refs to equal that input or its transported key to equal the row's
   original key.
3. `groupoid_promotion_predicate` repeats the incomplete checks.
4. The registered C4 attack swaps only the independent-rebuild reference.  It
   catches a literal/rebuild mismatch but not a self-consistent wrong packet.
5. `groupoid_promotion_source_scan` binds the consumer helpers but omits the
   producer `measure_complete_certificate_action_census` from its static
   backward slice.

This is not a pure enumeration reorder.  Row order and the target multiset do
not change; which complete target is attached to each derived source key does.
A content seal that records the malformed attachment cannot substitute for a
proof of identity action.

## 5. Preserved source facts

The two kills are quotient/action failures.  They do not alter the following
presentation-indexed regression facts or their already narrow meanings:

- exact finite Boolean census: 72 ambient representatives and 42 contextual
  classes;
- the split-fiber theorem and 468 bound nonzero transitions, divided as
  156 CREATE, 156 MERGE, and 156 UNCHANGED;
- the exact one-root sparse Gamma evaluator on its admitted typed arguments;
- `R`, `B`, `C`, `B2`,
  `K=[[351,-176],[-176,351]]/175`, and the `527/175` interval bound;
- the native result that no positive source-independent stochastic restart
  exists at the declared cut;
- the positive history-conditioned/enlarged-carrier Markovization controls;
- writer normalization, finite grammar closure, projector intertwining,
  all-input alternate-cut equality, and active inverse erasure;
- reciprocal joint `{00:9/25,01:0,10:144/625,11:256/625}`;
- the exposed matching-family response and its exclusion only of the frozen
  incidence-blind transducer class;
- strict CLI behavior, deterministic root/alien/one-file replay, and absence
  of fresh or publication artifacts.

The native nondivision theorem remains evidence of stochastic indivisibility,
not a claim that a definite intermediate configuration is unreal or
ontologically incomplete.  A history, phase, or enlarged carrier can
Markovize the representation without defeating the native no-restart result.

The record theorem also retains its limited meaning: a sealed record is stable
under every finite word of the declared continuation grammar, and the
record-bearing complete boundary is a lawful division on that grammar.  A
stable local record is not thereby a complete Markov checkpoint at every cut.

None of these preserved values can promote the claimed point-free quotient
while the complete tensor and certificate actions admit the counterexamples
above.

## 6. Adjudicated outcome and chronology

The v3 source-audit disposition is:

```text
NO-GO
```

The strict earliest outcome is:

```text
P13-REFERENT-PRESENTATION-ONLY
```

This is not a corpus-integrity block and not a refutation of the preserved
presentation-indexed calculations.  It does prevent these bytes from earning
the source groupoid, generating a fresh case, producing official v3 artifacts,
or supporting a regenerated Paper 13.

No nonce may be supplied.  Neither `--generate-fresh` nor official `--run` may
be invoked.  All future v3 publication paths remain absent and barred.  Paper
14 and Paper 15 remain closed because happening identity cannot be called
point-free while Paper 13's complete presentation action is false.

## 7. Bounded v4 forward-repair contract

The failures are local enough for one more result-neutral forward repair, but
they are scientific evidence-path defects, not editorial corrections.  The
v3 source, freeze note, and both reports remain immutable.  Before any v4
source byte, a separate delta pin must freeze both closures below.

### 7.1 Tensor factor-node closure

1. Reconstruct each factor's exact root `SOURCE` node from its complete source
   presentation and require the supplied factor node to equal it.
2. Reconstruct each factor's exact root target node from the witness target and
   require the returned factor transport to end there.
3. Reconstruct the tensor source and target only from those root factor nodes;
   refuse an internal node even if its boundary or configuration happens to be
   extensionally equal.
4. Retain full factor source/target nodes, AST addresses, endpoint roles,
   configurations, witnesses, and tensor source/target nodes in the law row and
   receipt.
5. Independently rebuild the tensor row and require identity, inverse,
   composition, associativity where typed, and tensor naturality without an
   address-erasing projection.

Mandatory attacks include:

```text
A17 TENSOR-INTERNAL-FACTOR-NODE
A18 TENSOR-TARGET-FACTOR-NODE-SEVER
```

`A17` uses the exact adjudicated internal-node object.  `A18` preserves the
factor output configuration but replaces the derived target root node with a
different valid node.  Both must refuse before a tensor law row exists and
must move the gate, outcome, lineage, claim, and seal in a real source-only
mutation.

### 7.2 Complete keyed certificate-action closure

For every identity row require at minimum:

```text
row.exact is true
identity_triple.original_ref
  == identity_triple.literal_transport_ref
  == identity_triple.independent_rebuild_ref
  == row.input_ref
identity_triple.original_pairing_key
  == identity_triple.transported_pairing_key
  == row.pairing_key
```

The generic consumer must decode the referenced complete objects and
recompute original and transported pairing keys from their raw bytes.  It
must validate the actual original-to-target witness action, not merely target
self-equality.  Nontrivial, inverse, composition, and associativity rows must
validate the corresponding per-key action and chain.

The static promotion slice must include the complete-action producer
`measure_complete_certificate_action_census`, all serializers, all key
derivations, all action consumers, and the promotion predicate.  No copied
aggregate Boolean or trusted coordinate may bypass those bytes.

Mandatory attacks include:

```text
C22 COMPLETE-IDENTITY-TARGET-PACKET-SWAP
C23 COMPLETE-ACTION-PRODUCER-BYPASS
```

`C22` is the exact adjudicated whole-packet swap: it preserves row order,
target multiset, store, counts, and literal/rebuild equality while crossing
the per-input action.  It must be killed by recomputation.  A pure
pre-pairing enumeration reorder remains a mandatory non-kill.  `C23` mutates
the producer attachment while leaving consumer signatures unchanged and must
fall through the static source gate and every promotion consumer.

### 7.3 Registry, versioning, and review

All 149 v3 attacks remain live.  A17--A18 and C22--C23 raise the minimum v4
registry to 153.  The two decisive counterexamples must also run as exact
post-freeze source-only mutations, not only synthetic record edits.

The next source uses a new path and identity, provisionally
`v16/code/p13_gamma_exact_v4.py`, with a new v4 source-freeze note.  It may not
import or call the v3 evaluator.  The v4 receipt schema must retain all
original and transported object bytes, addresses, keys, producer and consumer
lineages, mutation changed objects, and source seals needed for a no-import
rebuild.

After source freeze, two mutually blind audits and one adjudication are again
required.  Only their acceptance may authorize fresh generation and the
result-known Paper 13 reconstruction.

## 8. Paper 14 and Paper 15 boundary

The user's intended later programme is retained, not abandoned:

- Paper 14: presentation-independent stable happenings, complete division
  frontiers, local partial order, Gamma-derived positive weights/extensive
  valuation, and an operational local-duration candidate;
- Paper 15: only if those gates pass, dimension, Lorentzian signature,
  manifoldlikeness, scale, and metric reconstruction.

The order is mandatory.  A stable happening is a durable local fact, not an
automatic Markov checkpoint.  Factorization is licensed only at a complete
frontier whose full typed source is future-sufficient and whose direct and cut
laws agree through a positive normalized kernel.  Different weights may be
allowed only when they are Gamma-derived, presentation invariant, additive on
independent composition, and locally finite.  No causal graph, event counter,
clock, metric, or geometry may be added beside Gamma as an independent input.

## 9. Next authorized event

The sole next authorized event is the result-neutral v4 source-delta pin
specified in Section 7.  It may name the versioned source, attacks, receipts,
runtime cap, audit whitelists, and chronology.  It may not edit evaluator
source, generate a nonce, run publication modes, regenerate Paper 13, or begin
Paper 14, Paper 15, metric, curvature, gravity, continuum, GR/QFT, or
phenomenology.

This note intentionally does not contain its own ordinary SHA-256.  That hash
is computed only after these bytes freeze.
