# Paper 13 typed-groupoid source-audit adjudication

Date: 2026-08-20

Status: **SOURCE NO-GO / `P13-REFERENT-PRESENTATION-ONLY` / FRESH BARRED**

## 1. Authority and adjudication rule

This note jointly adjudicates the two mutually blind Stage-C source audits
required by `v16/note-paper13-typed-groupoid-forward-repair-pin.md`, SHA-256
`08f7f64efca6210eee356852ad9e9b59487ea62a55aeaf85a483f6a70b85b004`.
The frozen source under audit is
`v16/code/p13_gamma_exact_v2.py`, SHA-256
`b56383236a2aa0ff484aaa4c9082393beb4e4dd3ceb4d2724e4332bf68b6cba1`,
committed at `2ee5fba54e7336e3aab80a401c976f8d2fbe670e`.

The frozen reports are:

| seat | report | commit | ordinary SHA-256 | normalized SHA-256 |
|---|---|---|---|---|
| operator/category | `v16/review-paper13-typed-groupoid-source-operator.md` | `891c514ccae7eaac66c34b4090210b53f58705fe` | `884337d385d0997d7fddcf748297544869c9effc537c46017a6db018c7f4da5a` | `64444496857f22868215e85c920f369b855b43dc2bc1a1e9a15cc92d8e4cf0b2` |
| records/integrity | `v16/review-paper13-typed-groupoid-source-records.md` | `d5f01cef66c1e28c5eb70a46b359468e77bd9eb5` | `c90a16072084896da248a53551a54dc44eb0f7c668c401395b2c1d1b49c0cf07` | `3baf9c6fb42c0595be22d7610ec54aeed360b765b563139c20676f83ddad6a82` |

The reports contain 365 and 414 LF-terminated lines respectively.  Each seat
authenticated the same source, pin, and freeze note before science, completed
an independent no-import reconstruction before implementation inspection,
used only development modes, preserved mutual blindness, and wrote only its
assigned report.  The authorized commit of the first frozen report advanced
shared HEAD during the second audit without changing any candidate byte; the
second seat reauthenticated the pinned corpus and did not inspect the sibling
commit.

There is no majority rule.  One reproducible counterexample defeats a
universal groupoid-action claim.  Both reports independently return `NO-GO`
at `P13-REFERENT-PRESENTATION-ONLY`, through distinct objects.

## 2. Independent adjudicator reconstruction

The adjudicator read both reports completely, authenticated their ordinary
hashes and the source hash, inspected the exact frozen functions, and built a
separate no-import static/semantic checker at
`/private/tmp/p13_typed_groupoid_source_adjudicator.py`, SHA-256
`412bdd6cb567c8e49661ee5a3bb2341d3ce1d3a254a15a27b49b48044dc50119`.
It imports no evaluator function and mutates no repository byte.

Its canonical result has normalized payload SHA-256
`dc97ca94d27b07869fb54a9994c4601cda45c5bbae8f959f2dd0406b9fb3d325`
and returns:

```text
both_reproduced             true
earliest_rung               P13-REFERENT-PRESENTATION-ONLY
fresh_generation_authorized false
```

For the operator object it confirms that frozen lines 5121--5145 call
`validate_configuration`, `configuration_from_assignments`, and
`relabel_context`, but never call `relabel_boundary` and contain no equality
between the supplied target boundary and the witness image.  An identity
witness whose image is an `ACTIVE` boundary therefore accepts assignments in
an exact same-catalogue `CARRIED` boundary when the contexts agree.

For the certificate object it extracts the literal predicate:

```text
certificate_row is None or
  (all_original_final and all_transformed_final and count_preserved)
```

The expression and the promotion function mention neither original nor
transformed classifier-hash lists, and the native row serializes no paired
certificate bytes.  Replacing every transformed hash by
`NOT-A-TRANSPORTED-CERTIFICATE` changes the evidence hash while leaving the
literal certificate predicate and promotion true.

## 3. Accepted KILL A — nonimage configuration target

The operator report's decisive object is accepted in full.

`relabel_configuration` has the public signature

```text
(source_boundary, target_boundary, configuration, witness)
```

but does not require

```text
target_boundary == relabel_boundary(source_boundary, witness).
```

The smallest counterexample uses an exact identity witness on the coherent
control's source boundary.  The source port mode is `ACTIVE`; the supplied
target is an otherwise exact valid boundary with the same catalogue and port
name but mode `CARRIED`.  The identity witness image is the original `ACTIVE`
boundary.  The source configuration's assignments fit both catalogues and
its context is unchanged, so the frozen function returns a configuration on
the wrong target instead of refusing.

The private black-box instrumentation changed only one registered-mutant
harness branch and reported:

```text
source_boundary_is_literal_arrow_source true
wrong_target_is_exact_valid_boundary    true
supplied_target_is_witness_image        false
malformed_target_accepted               true
refusal                                 NO-REFUSAL
```

The instrumented source SHA-256 is
`6e0789288e6c472756e4a82dd8847b31634d4b8da7aab15d33f8863523aa5897`;
stdout SHA-256 is
`2c6beae4c82f83b351b42d0d6d919eee7867b18dcd1e4eff7779923ac796fd08`;
normalized payload SHA-256 is
`cc641b86440a39a7ab8236a45b7c0b4a4b2a9ddcca36d25b3174ac9d51def3a8`;
and independently recomputed evidence SHA-256 is
`2dbc1e4dc52e265d0eeba731440021c759fd637c2feb291cb85296cfbc35f4c9`.

This is not a malformed-object nuisance.  Both boundaries are exact native
objects with equal catalogue cardinality.  Port mode is physical boundary
typing.  An identity action that silently changes `ACTIVE` to `CARRIED` is not
an action of the pinned source groupoid.

The passing native covariance rows do not answer the object because every
positive caller supplies the already-derived target.  G15 severs a query; it
does not test a different exact target boundary admitted by the same
assignments.  The universal complete-object action is therefore false.

## 4. Accepted KILL B — native certificate transport not evidenced

The records report's decisive object is accepted in full.

For native CREATE, MERGE, and UNCHANGED rows, the frozen source independently
collects original and transformed certificates, then serializes only:

- operation and counts;
- original and transformed classifier-hash lists;
- `all_original_final` and `all_transformed_final`;
- `count_preserved`.

It serializes no paired original certificate, literal witness-transported
certificate, or independently rebuilt transformed certificate bytes.  It
does not prove which transformed certificate is the image of which original.
Its `certificate_transport_exact` Boolean consumes only finality and equal
counts.  `groupoid_promotion_predicate` consumes that Boolean, not the hash
lists or any transported bytes.

The independent malformed-evidence probe changes four transformed hashes to
four copies of `NOT-A-TRANSPORTED-CERTIFICATE`.  The measurement, referent
claim, and seal hashes all move, yet:

```text
transport evidence valid      false
certificate_transport_exact   true
native row all_exact           true
groupoid promotion before      true
groupoid promotion after       true
```

This violates the forward pin's explicit rule that a transported hash without
transported bytes is non-evidence.  A seal can authenticate that bytes changed
without proving the claimed functorial action.  The independent probe SHA-256
is `26f9b31abf19a02cdd302c4b353652ede8b25c0c714a2a0530f18388f70eadf5`,
with normalized payload SHA-256
`9a3e0d4c6ba03f9df995bfa14b1b7fecf792e2cc910e3c0848eada377ad3cac3`.

The detailed `split_certificate_covariance` control proves one representative
certificate and G16 kills one stale-cache object.  Neither supplies the
pairwise native CREATE/MERGE/UNCHANGED action claimed by all three census
rows.  Passing them cannot repair the missing promotion dependency.

## 5. Preserved source facts

The source audits and adjudicator preserve the following as regression facts
at their already narrowed scopes:

- immutable typed `SourcePresentation` and total sparse maps;
- both witness identities, both inverses, first-then-second composition, and
  associativity on the registered lawful surface;
- 34 abstract bijections and 14,050 composable triples;
- exact category, tensor, totality, and positive operator/Gamma covariance
  rows when the target is the actual witness image;
- 72 ambient Boolean representatives and 42 contextual classes;
- 12 generator families, 312 source columns, and 468 bound nonzero
  transitions split 156/156/156;
- exact `R`, `B`, `C`, `B2`,
  `K=[[351,-176],[-176,351]]/175`, and the `527/175` interval bound;
- the exact native statement that no positive source-independent restart
  exists on the declared carrier, without implying an unreal or incomplete
  configuration;
- positive history-conditioned and enlarged-carrier Markovization controls;
- all-input writer normalization, the six-letter finite continuation grammar,
  alternate-cut equality, record preservation, and active inverse erasure;
- reciprocal joint `{00:9/25,01:0,10:144/625,11:256/625}`;
- the exposed development matching rows at their incidence-blind-class scope;
- strict CLI, deterministic root/alien/off-tree selftest replay, artifact
  absence, and G1/G18 changed-source kills.

These preserved facts do not promote the failed point-free referent.  The
size-twelve native row remains only the disclosed fixed two-query source
control, not a fresh global-law confirmation.

## 6. Adjudicated outcome

The source-audit disposition is:

```text
NO-GO
```

The strict earliest outcome remains:

```text
P13-REFERENT-PRESENTATION-ONLY
```

This is a source-action and evidence-lineage failure, not an integrity block
and not a refutation of the preserved presentation-indexed mathematics.  It
does prevent these bytes from restoring the point-free quotient, generating a
fresh case, producing official v2 artifacts, or regenerating the paper.

No nonce may be supplied.  No `--generate-fresh` or official `--run` may be
invoked.  Every future v2 publication path remains barred.  The rejected
paper remains rejected and noncitable.

## 7. Bounded forward-repair boundary

The two defects are local enough to admit one further result-neutral source
delta, but not an editorial correction and not an in-place edit of the v2
source.  A separate pin must freeze the following before any new source byte.

### 7.1 Configuration-action closure

1. Prefer an API that derives the target boundary internally from
   `(source_boundary,witness)` and exposes no caller-selected target.
2. If a target argument remains, require exact semantic equality with
   `relabel_boundary(source_boundary,witness)` before constructing any
   assignment.
3. Require the source boundary to be a literal typed subobject of the witness
   source presentation and validate all matter and port names against the
   witness source carriers.
4. Validate the returned configuration on the exact derived target and prove
   identity, inverse, composition, and tensor action on source and target
   catalogues.
5. Freeze changed objects for identity `ACTIVE->CARRIED`, same-cardinality
   alien boundary, wrong branch target, alien matter/port, and a chained
   nonimage target.  All must refuse before an action result exists.

### 7.2 Certificate-action closure

1. For every native CREATE, MERGE, and UNCHANGED certificate, serialize a
   keyed triple of complete bytes: original, literal witness transport, and
   independent rebuild from the transformed law/Arrow/transition.
2. Pair by immutable branch identity and complete binding, never by count or
   incidental enumeration order.
3. Require exact equality of transported and rebuilt bytes, context proof,
   law, Arrow, occurrence, port, source/target configuration, operation,
   branch bit, sector, classifier-consumed hash, and inverse data.
4. Prove identity, inverse, two-map composition, and three-map associativity
   on every pair, with exact residuals.
5. Make the promotion predicate consume every pairwise fact directly; a
   copied aggregate Boolean, finality, equal counts, or hash lists alone are
   non-evidence.
6. Freeze changed objects for malformed transported bytes, permutation-only
   pairing, final-and-count-only acceptance, missing operation class, stale
   transported/rebuilt certificate, and dropped classifier lineage.

### 7.3 Version and review discipline

The next source uses a new versioned path and identity.  The v2 source and
both reports remain immutable.  All 112 existing attacks remain live, the two
adjudicated objects become mandatory real changed-source controls, and the
entire scientific regression wall must remain exact.  A new source freeze is
followed by two new mutually blind audits and adjudication before any fresh
nonce or artifact exists.

## 8. Next authorized event

The sole next authorized event is a result-neutral delta pin for the two
closures in Section 7.  It may name new v3 source and artifact paths, audit
whitelists, attacks, receipts, and chronology.  It may not edit source,
generate a nonce, run publication modes, regenerate the paper, or begin
Paper 14, metric, curvature, gravity, continuum, GR/QFT, or later work.

This note intentionally does not contain its own ordinary SHA-256.  That hash
is computed only after these bytes freeze.
