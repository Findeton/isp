# Paper 13 typed-groupoid v4 source-audit adjudication

Date: 2026-08-20

Disposition: **NO-GO**

Strict earliest rung: `P13-SPECIFICATION-INCONSISTENT`

## 1. Authority and authenticated corpus

This adjudication binds the frozen Paper 13 v4 source and its two mutually
blind source audits.  It does not run a fresh case or publication mode and
does not restore a scientific rung.

| object | commit / ordinary SHA-256 |
|---|---|
| v4 source-freeze commit | `0d63ca9b493e8bd1ee55ee5a7f204a23898b892f` |
| v4 source | `272b64972e3eb620867cf6ad0decf8db1fcc03092adfd1d69d77aa10e2605910` |
| v4 source-freeze note | `5bf797eae6a80690a27bcad59c8e3b2206f008f1ce2039d4b6883d22a82d38c7` |
| v4 result-neutral source-delta pin | `ae1283784bdcb274ff16cc2f06288f27258e0ada0dd8efe2f84084339941acb0` |
| operator/category report commit | `c2db1d18bb1f2cdd04c047672bf2f45dd6fa7efd` |
| operator/category report | `59c5fa4206df7f7e2c9df9f820fb1256a6e3a6d73af2fac238a64c6ed336a5c4` |
| records/integrity report commit | `a14d36fdbf5951e85dde0b5346b763e00f9d59cb` |
| records/integrity report | `8f6faca179c0d13331d69d683db837bc2f050d573ff139ce96ba41ca31b837cc` |

The two seats remained mutually blind.  Each stopped at its first exact
blocker and wrote only its assigned report.  The authorized first report
commit advanced shared HEAD during the second audit without changing any
pinned candidate byte; the records seat reauthenticated those bytes and did
not inspect the sibling path.

## 2. Joint independent reproduction

The coordinator's independent adjudicator is
`/private/tmp/p13_v4_source_adjudicator.py`, ordinary SHA-256
`3dac0f1319517e27e6db7ac71aaf44b4b954cc0c136a8d36db196e242fb97b69`.
Its canonical one-line result is
`/private/tmp/p13_v4_source_adjudicator_result.json`, ordinary SHA-256
`30b4f719687d82d0744458c1cba5d854da306a0ff59d88845934e2c2c04edd07`.
It authenticates all five bound objects, imports only the frozen source under
audit with bytecode disabled, reconstructs the complete groupoid measurement,
and then applies the adjudicated tensor-lineage deletion.  It separately
checks the committed mutation-evidence surface.

The exact reproduced coordinates are:

```text
clean retained tensor lineage             24
deleted retained tensor lineage            0
stored factor_certificate_count           24
clean tensor exact                       true
deleted tensor exact                     true
clean promotion                          true
deleted promotion                        true

all six patch hashes printed             true
probe-script hash printed                true
exact patch bytes field present         false
bound mutation artifact path present    false
```

The adjudicator exits `0` with `all_exact=true`: both blind findings reproduce
on the exact frozen corpus.

## 3. Accepted finding A — factor lineage is not complete evidence

The operator/category report's changed object is accepted in full.  Tensor
case `GENERATOR-BY-GENERATOR` normally retains 24 address-keyed ordinary
generator-certificate entries.  Deleting the entire tuple while leaving the
content store, stored count `24`, uniqueness flag, law row, tensor transports,
and every other byte unchanged still satisfies
`_tensor_configuration_action_exact` and `groupoid_promotion_predicate`.

The failure is structural:

- the verifier checks only the entries that happen to remain;
- its loop is vacuously true for an empty tuple;
- it does not reconstruct the factor Arrow trees and their expected generator
  leaf addresses;
- it does not require the stored count to equal the retained tuple length;
- it does not decode each complete input, bind its certificate field to
  `certificate_ref`, or recompute its pairing key; and
- promotion repeats the same membership-only check rather than consuming a
  no-drop manifest.

The off-tree named-mutant reproduction exits normally with `status=SURVIVED`;
this is not a crash, timeout, malformed-object argument, or copied boolean.
It defeats the universal tensor/action evidence and therefore independently
caps the source at `P13-REFERENT-PRESENTATION-ONLY`.

## 4. Accepted finding I — source-mutant preimages are absent

The records/integrity report's evidentiary finding is also accepted in full.
Section 8 of the v4 pin requires every real source-mutation record to include
the exact patch plus source, probe/capture, process, and dependency-movement
evidence.  The frozen note prints six patch hashes, six mutant-source hashes,
one probe-program hash, six probe-result hashes, and prose descriptions.  The
authenticated Stage-B corpus contains none of their preimage bytes and names
no bound artifact path containing them.

A digest authenticates supplied bytes; it cannot replace missing bytes.  An
independent reviewer therefore cannot:

1. hash the alleged patch bytes;
2. apply them by a declared exact rule to the frozen source;
3. derive the alleged mutant-source hash;
4. run the alleged probe/capture program; or
5. reproduce the claimed movement of measurement, gate, outcome, action
   lineage, shadow DAG, claim-input DAG, and seal.

This contradicts the pin's literal source-freeze evidence contract before the
scientific gate.  The ordered strict earliest disposition is therefore
`P13-SPECIFICATION-INCONSISTENT`, earlier than the operator seat's independently
valid quotient cap.

## 5. Preserved scientific scope

Neither finding is a counterexample to the one-Gamma scientific arithmetic.
The following remain exact presentation-indexed regression facts but do not
promote through the failed point-free source gate:

- the 72 ambient / 42 contextual support-split theorem;
- the exact `R`, `B`, `C`, `B^2`, `K`, and `527/175` coordinates;
- failure of a positive source-independent native restart kernel at the
  declared intermediate cut;
- the positive history/enlarged-carrier Markovization control;
- grammar-relative stable-record division and all-input alternate-cut
  equality;
- reciprocal relation-mediated response; and
- the resource-matched, incidence-blind-class-relative matching calculation.

The native negative-`K` result says only that the cut is not an admissible
stochastic division on the declared carrier.  It does not imply that an actual
configuration is unreal or incomplete, and it does not prohibit a declared
history/phase/carrier enlargement.  Likewise, stable record persistence does
not turn each local happening into a complete Markov checkpoint.

Born squaring, the event/filling grammar, actualization, coupling selection,
and division doctrine remain postulated or priced.  No time, topology, metric,
curvature, continuum, gravity, GR/QFT, or absolute relational irreducibility is
earned.

## 6. Binding forward-repair boundary

The v4 bytes remain frozen and rejected.  No edit in place is authorized.  A
new result-neutral source-delta pin may be proposed at exactly:

```text
v16/note-paper13-typed-groupoid-v5-source-delta-pin.md
```

That pin must close both findings without changing the scientific outcome
ladder or pre-awarding the repair.

### 6.1 Exact tensor-lineage reconstruction

The next source contract must retain complete/content-addressed bytes for the
law, both factor source presentations, both typed witnesses, and every object
needed to reconstruct the factor Arrow trees.  An independent decoder must:

1. decode and re-encode those complete bytes;
2. derive the exact structural generator-leaf addresses in both factors;
3. rebuild every nonzero `CertificateActionInput` at each address;
4. construct the canonical address/pairing-key ordered expected lineage;
5. require byte equality with the retained lineage;
6. require `factor_certificate_count == len(lineage)` and equality with the
   top-level flattened lineage/cardinality records;
7. decode each `input_ref`, bind `certificate_ref` to that input's actual
   certificate, and recompute the pairing key; and
8. feed the independently rebuilt manifest bytes—not a stored final boolean—
   through tensor verification, promotion, measurement, lineage, claim, and
   seal.

The hostile set must include deletion of one/all entries, duplication,
same-count address/key swaps, foreign input/certificate attachment, wrong
pairing key, and expected-manifest producer bypass.  Pure enumeration reorder
remains a required non-kill after canonicalization.

### 6.2 Replayable real source mutations

The next pin must authorize exact versioned evidence paths in the source-
freeze whitelist.  The frozen corpus must contain, not merely hash:

```text
base source SHA-256
canonical ordered patch/replacement bytes
patch encoding and exact one-application rule
derived mutant-source SHA-256
probe/capture program bytes and SHA-256
probe/capture output bytes and SHA-256
exit, stdout, stderr, runtime, RSS, and zero-write evidence
recomputed measurement/gate/outcome/lineage/shadow/claim/seal objects
```

A small canonical JSON mutation-spec artifact plus a standard-library replay
program is acceptable if the new pin freezes their exact paths and schemas.
The replay must independently derive every mutant source from the accepted
base source and refuse zero/multiple old-byte matches.  It must not import an
expected result table or use a digest without its preimage.

All 153 v4 attacks remain live.  The lineage-deletion survivor and its
same-count/attachment variants are added changed objects, and the real-source
suite must include a direct bypass of the new expected-lineage producer.  The
root, alien-CWD, and true one-file/no-`.git` 300-second cap remains binding;
evidence may be streamed or content-address reused but not trimmed.

## 7. Chronology and next event

Fresh generation, official run mode, receipt, paper/bundle regeneration, and
hostile publication review remain barred.  No v5 source or mutation artifact
byte may precede a committed, independently audited v5 delta pin that names
its exact stage whitelists.

Nonbinding private Paper 14 definition/literature preparation has no
evidentiary standing and binds no Paper 13 byte.  Authoritative Paper 14,
Paper 15, metric reconstruction, curvature, gravity, continuum, and GR/QFT
remain closed.

The sole next authorized event is construction, blind implementability audit,
and commit of the result-neutral v5 source-delta pin above.
