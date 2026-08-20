# Paper 13 typed-groupoid v4 source audit — operator/category seat

Date: 2026-08-20

Disposition: **NO-GO**

Earliest surviving rung: `P13-REFERENT-PRESENTATION-ONLY`

## 1. Scope and authenticated corpus

This is the mutually blind Stage-C operator/category source audit of the
frozen Paper 13 v4 evaluator.  The audit stopped at the first reproducible
semantic counterexample, as required by the v4 pin.

The opening and closing authentications agreed exactly:

| object | authenticated identity |
|---|---|
| Git HEAD | `0d63ca9b493e8bd1ee55ee5a7f204a23898b892f` |
| v4 result-neutral delta pin | `ae1283784bdcb274ff16cc2f06288f27258e0ada0dd8efe2f84084339941acb0` |
| v4 source | `272b64972e3eb620867cf6ad0decf8db1fcc03092adfd1d69d77aa10e2605910` |
| v4 source freeze note | `5bf797eae6a80690a27bcad59c8e3b2206f008f1ce2039d4b6883d22a82d38c7` |

The pin's 687 lines and the freeze note's 292 lines were read completely
before source inspection.  The source was not imported.  No fresh-generation
or official-run mode was invoked.  No sibling report, artifact, or auditor
was inspected or contacted.  All counterexample work was performed on one
private off-tree source copy; the only repository write is this report.

## 2. Independent semantic reconstruction

Before inspecting implementation semantics, I reconstructed the pinned
operator/category contract as follows.

- Objects are complete `SourcePresentation` values.  A witness is a typed,
  total bijection on every role, matter, port, and occurrence carrier whose
  literal relabelling maps the complete source Arrow to the complete target
  Arrow.
- A `BoundaryNode` is distinguished by complete boundary semantic bytes, its
  Arrow-AST address, and endpoint role.  Configuration action derives the
  target at the same address and role; no caller-selected target is part of
  the action.
- Identity, inverse, composition, and associativity compare the independently
  evaluated paths on complete nodes and configurations.  Tensor action accepts
  only factor root `SOURCE` nodes, independently reconstructs source and target
  tensor roots, and compares the transported tensor configuration with the
  product of the two transported factor configurations.
- Tensor receipt lineage is the canonical address-keyed flattening of exactly
  the generator-leaf certificates in the declared factor paths: structural
  leaves contribute zero; generator leaves contribute every bound nonzero
  transition; nested factors contribute all such leaves without drop,
  duplication, or pseudo-certificate.
- Each lineage certificate remains an ordinary complete certificate-action
  input.  Its raw bytes must decode, its certificate and pairing key must be
  recomputed from that input, and its retained address must agree with the
  complete factor Arrow.  Counts or stored `exact`/uniqueness booleans cannot
  replace that reconstruction.

This reconstruction makes deletion of a nonempty factor lineage an exact
negative oracle independently of the implementation.

## 3. First exact counterexample

### Claim defeated

Sections 4.4, 5, and 6 of the pin require complete, no-drop tensor
factor-certificate lineage and ordinary per-key verification of every retained
entry.  The source promotion path does not enforce that requirement.

The relevant frozen-source locations are:

- `_tensor_factor_certificate_lineage`, lines 7840–7871, constructs a positive
  lineage;
- `_tensor_configuration_action_exact`, lines 7649–7689, checks only that each
  retained entry has references present in the store, an address tuple, and a
  pairing-key tuple, plus a stored uniqueness Boolean;
- `groupoid_promotion_predicate`, lines 9088–9242, repeats only reference
  membership/uniqueness checks and requires merely that the stored top-level
  cardinalities are nonnegative.

Neither verifier derives the expected generator leaves, compares the retained
tuple with them, binds `factor_certificate_count` to tuple length, recomputes a
retained pairing key, nor proves that `certificate_ref` is the certificate
inside `input_ref`.  In particular, both lineage loops are vacuously true for
an empty tuple.

### Smallest changed object

Starting from the clean `measure_tensor_configuration_action` result, change
only the first case by copy-on-write:

```python
changed = dict(clean)
cases = list(clean["cases"])
case0 = dict(cases[0])
case0["factor_certificate_lineage"] = ()
cases[0] = case0
changed["cases"] = tuple(cases)
```

Everything else remains byte-for-byte unchanged, including the authenticated
content store, `factor_certificate_count = 24`, `factor_keys_unique = true`,
`all_exact = true`, and the top-level cardinality tuple `(24, 12, 24)`.
Twenty-four required generator-bound entries have therefore been dropped,
while the frozen verifier still returns true.  The promotion predicate adds no
stronger condition: all its other conjuncts are unchanged and its lineage
membership loop is vacuous.

### Exact black-box reproduction

I copied the authenticated source off-tree and changed only the existing named
development-mutant branch `TENSOR-TARGET-FACTOR-NODE-SEVER` so that its changed
object performs the tuple deletion above and reports the retained tuple
length.  No evaluator import or repository file mutation was used.

| property | value |
|---|---|
| off-tree mutant SHA-256 | `6e1c2e55c03990012b8ab80b334659e72a660fa7623bc33a2267c06f4c4c248b` |
| command | `python3 p13_gamma_exact_v4_lineage_mutant.py --mutant TENSOR-TARGET-FACTOR-NODE-SEVER` |
| CWD | private one-file/no-`.git` directory |
| exit | `0` |
| wall time | `0.739814 s` |
| clean tensor verifier | `true` |
| deletion-mutant tensor verifier | `true` |
| old retained count | `24` |
| new retained count | `0` |
| stored count left unchanged | `24` |
| mutation result | `pass=false`, `status=SURVIVED` |
| mutation evidence SHA-256 | `52e183bde2d79bbc61fc2c4680ada5c972340ad7cacdab7ad90c522dd9dc716f` |
| normalized mutant payload SHA-256 | `193f5785da95e2534acf83f5b8d7eca1ee258e6b7e3433aef7c5048823e1fbe6` |
| publication writes | `0` |

The runner completed normally; this is a semantic survivor, not a crash,
timeout, malformed object, or copied-label argument.

## 4. Required repair

The smallest adequate repair is to make tensor lineage a recomputed theorem,
not a stored summary:

1. Retain complete/content-addressed bytes sufficient for an independent
   decoder to reconstruct both factor presentations and their Arrow trees.
2. Derive the exact ordered generator-address set from those decoded trees.
3. Rebuild every nonzero `CertificateActionInput` for each generator address.
4. Require exact equality of the retained address-keyed lineage with that
   rebuilt sequence, including `factor_certificate_count == len(lineage)` and
   equality with the top-level flattened lineage/cardinality records.
5. For every entry, decode `input_ref`, require `certificate_ref` to equal the
   decoded input's complete certificate bytes, and recompute the pairing key.
6. Invoke this verifier from both `_tensor_configuration_action_exact` and the
   promotion backward slice.  Add an executable changed-object attack that
   drops one or all lineage entries while preserving the store and diagnostic
   fields; it must demote promotion.

Checking only the expected numeric cardinalities `24/12/24` is insufficient:
a same-count swap or duplicated/foreign certificate must also refuse.

## 5. Outcome and stopping boundary

Disposition is **NO-GO**.  The universal tensor/action closure fails at
`P13-REFERENT-PRESENTATION-ONLY`.  Per the first-counterexample stopping rule,
I did not continue to the remaining attacks, source mutants, three full
selftest parity runs, or later scientific claims.  Fresh generation and
publication remain barred.

Normalized-self-hash convention: replace only the 64 hexadecimal characters
on the final `normalized_sha256:` line by 64 ASCII zeroes, preserve all other
bytes and the final LF, then apply ordinary SHA-256.

normalized_sha256: 6c7c4c55ba53051a574b5a6a13e7d882a9dc0af93b3c17cd537c32cb8fe66edd
