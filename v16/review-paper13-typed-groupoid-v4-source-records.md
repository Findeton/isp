# Paper 13 v4 typed-groupoid source audit — records and integrity seat

## 1. Disposition

**Stage-C disposition: `NO-GO`.**

**Earliest affected outcome rung: `P13-SPECIFICATION-INCONSISTENT`.**

The first exact blocker is a non-reconstructible six-mutant evidence record.
Section 8 of the result-neutral v4 pin requires the record for every real
post-freeze source mutation to include the **exact patch**, together with the
old/new source hashes, probe/capture hashes, exit, stdout/stderr hashes,
runtime, and zero-write evidence.  The frozen source note instead supplies
only a one-way patch SHA-256 for each mutation, one probe-script SHA-256, per-
mutation probe SHA-256 values, aggregate prose, and runtime/RSS numbers.  It
contains neither the patch bytes nor the probe/capture program bytes and
identifies no authenticated artifact containing them.  The candidate source
contains neither record.

Consequently an independent reviewer cannot reconstruct any of the six
mutant sources, verify that its patch hashes to the recorded digest, verify
that applying it to the pinned source yields the recorded mutant-source
digest, or replay the claimed forbidden behavior and seven-object dependency
movement.  A SHA-256 digest is an authenticator for supplied bytes; it is not
a substitute for missing bytes.  This is a pre-science records and
specification failure, so the pin's stopping rule bars fresh generation and
ends this audit before long black-box selftests.

## 2. Authentication, isolation, and stopping rule

Before scientific work I authenticated dispatch HEAD as
`0d63ca9b493e8bd1ee55ee5a7f204a23898b892f` and authenticated the three
pinned objects.  I read the complete `687`-line pin and the complete
`292`-line freeze note.  Before implementation inspection I completed the
independent reconstruction in Section 3.  I then read the complete
`16564`-line source and inspected its raw-store, decoder, promotion,
lineage/claim/seal, mutation, CLI, and publication paths.

During the audit the shared HEAD advanced to
`c2db1d18bb1f2cdd04c047672bf2f45dd6fa7efd`.  The coordinator identified
this as the authorized separate commit of the other blind seat's sole report.
I did not inspect or list that path.  Reauthentication showed that all three
pinned candidate objects remained byte-identical:

| object | LF lines | bytes | ordinary SHA-256 |
|---|---:|---:|---|
| `v16/note-paper13-typed-groupoid-v4-source-delta-pin.md` | `687` | `28743` | `ae1283784bdcb274ff16cc2f06288f27258e0ada0dd8efe2f84084339941acb0` |
| `v16/code/p13_gamma_exact_v4.py` | `16564` | `656207` | `272b64972e3eb620867cf6ad0decf8db1fcc03092adfd1d69d77aa10e2605910` |
| `v16/note-paper13-typed-groupoid-source-freeze-v4.md` | `292` | `14206` | `5bf797eae6a80690a27bcad59c8e3b2206f008f1ce2039d4b6883d22a82d38c7` |

The pin's normalized SHA-256 is
`24ab3fc9072b39c2e128158a20352c1ffe1375ee46c5c40fb9e0988c4c447263`.

Mutual blindness was maintained.  I did not inspect, list, infer, or contact
the other seat, its private work, or any sibling report.  I imported no
candidate evaluator, fixture, scorer, receipt, or scientific function.  I
never invoked `--generate-fresh` or `--run`, created no nonce or future v4
artifact, and made no publication write.  Candidate, pin, freeze note,
ledgers, status files, Git state, and every non-report repository path were
left unchanged by this seat.  All independent work was off-tree under
`/private/tmp`.

The exact evidence-record blocker was found while checking the six mandatory
real changed-source obligations.  Per the instruction to stop at the first
exact counterexample, no repository-root, alien-CWD, or true-one-file
candidate selftest was launched after that point.  Subsequent work was
limited to localizing and hashing the blocker and freezing this report.

## 3. Independent pre-inspection reconstruction

The standard-library-only, no-import reconstruction is
`/private/tmp/p13_v4_records_reconstruct.py`, ordinary SHA-256
`840a62f2b91013a20eaa630f5b71108e86ba47c802de219bf698a4b69e2686d1`,
with `472` lines and `15725` bytes.  It was completed before source
implementation inspection and imports no repository module.  Its canonical
result SHA-256 is
`1d96157d31759ced29b2357028a1b7c0875be139ba9b402cfe20b18dd385f4f6`.

It independently reconstructed:

- `12` generator families and `312` source columns;
- `468` bound nonzero transitions, partitioned as `156` CREATE, `156` MERGE,
  and `156` UNCHANGED;
- `468` identity actions plus `12` nonidentity family actions, hence `480`
  complete action rows;
- strict canonical content-address storage, decode/re-encode, pairing-key
  recomputation, literal transport, and independent rebuild;
- rejection of both rows after a complete identity target-packet swap while
  preserving a pure enumeration reorder as a non-kill; and
- address-keyed factor-lineage multiplicities with a dropped entry rejected.

The reconstruction returned `all_rows_verified=true`,
`packet_swap_rejections=2`, `factor_lineage_drop_rejected=true`, and
`enumeration_reorder_nonkill=true`.  These positive controls show that the
pinned receipt model is implementable in principle.  They do not repair the
missing committed mutation evidence.

## 4. Decisive counterexample: hash-only real-mutant records

The binding requirement is literal.  Pin lines `382--402` require six
source-only true-one-file/no-`.git` mutations, an independent semantic probe
for each, movement through measurement, gate, outcome, action lineage,
shadow DAG, claim-input DAG, and seal, and a mutation record that includes
the **exact patch**.

Freeze-note lines `179--223` provide the following digest table:

| mutation | mutant-source SHA-256 | patch SHA-256 | probe SHA-256 |
|---|---|---|---|
| `A-SOURCE-CORE` | `ae8940992de146989cb09c7440220be146e682de4983cd8f613d57a3407658f2` | `96bb6e173c09131ec01c2e1e0912e8d3bab80b4e25350b0e0b3105c1ff45b6e3` | `609b51ca6988d3dab82f3eff7fff359631a1f48f6fb07c94216e077df1bd2469` |
| `A-SOURCE-ASSERT` | `e0821f2970b4f1d15c9fb022b9ffad6a2f124fa68c12a60d667a3bc2e6ddc177` | `7f2f0ae030832bf9b68b326dac0149dae957cb57031e0004074a3d2ddccf8dbd` | `74703a68eed500cd255b62dd4ff99eee78fd5cd815e98d112f240e32ab6b2373` |
| `C-SOURCE-PROMOTION` | `f3fd38e6f0e31ed6e93cf1f51a919beb016d258cebccbcb499aee7411ea1f48b` | `0e9d6424e03356bbade1514f97e31a2e36c388581af0ebd18c675e14bb1ec84c` | `b58230cbeda93504591478910b66b4638c58c488640eb052ccef65912793cc88` |
| `C-SOURCE-ACTION` | `ea8e3df75421a62eaadaf6bbaf85844352cc1a5bd4c26f9aaf6a69752655d920` | `387649d2d016186a6240571c073e3f361caebf33705fcfdc02503038568bb0d2` | `0dd5ab68d799e0521a80fc81a54a440293db09748287e55ea1db05ead21e304f` |
| `A-SOURCE-TENSOR-ROOT` | `111ff506cdf0e1857dec5ceb5884058bcd5c32eedf2612cc2024afbf3a4d58dc` | `7125c2f7e9b9b4416d478767d24ad22838e4b4640fcebd03adc995b6bfdd6647` | `7518301e3536877e425e94684a20d3357bef5ea691c5365a18f455f0c601e657` |
| `C-SOURCE-TARGET-PACKET` | `ff0a52003c31cbd79f6ca37b72e385fc96de4bcbf79e9837325bb36d24cd74fa` | `37309ea3a9aa140f9a88942c2a18431a6cf20c7ebec34c6723dfb581e4e39ce6` | `b631cee8f5f9dd14a782e30dea1ab93b590bc7dc04c4139c5ed47931c2eef50d` |

It also provides one overall probe-script SHA-256,
`0f8112348377560a3d1eb5a72f2e26b7f47b0f32eb487ed5ed320796f5571433`,
and prose descriptions of the six intended semantic changes.  It does not
provide any of the following bytes:

1. a unified patch, replacement tuple, old/new source slice, or deterministic
   edit program for any mutation;
2. the probe script whose digest is quoted;
3. the per-mutation probe/capture payload whose digest is quoted; or
4. a bound path and authenticated read record from which any of those bytes
   can be obtained.

The exact read-only localization command was:

```text
rg -n "patch|probe script|source mutation|mutant source" \
  v16/code/p13_gamma_exact_v4.py \
  v16/note-paper13-typed-groupoid-source-freeze-v4.md \
  v16/note-paper13-typed-groupoid-v4-source-delta-pin.md
```

It returns only the pin's exact-patch requirement, the freeze section and
hash-table headings, and an unrelated source dispatcher name.  A second
search for all six mutation identifiers and the recorded probe-script/patch
digests returns occurrences only in the pin descriptions and freeze hash
table; the candidate source has none.

This is a direct completeness failure, not a demand to trust an unavailable
private log.  The candidate's own content-addressed store rule at source
lines `6687--6719` accepts an object only when both `sha256` and
`canonical_bytes` are present and match.  The six external mutation records
fall below that same evidentiary standard: they retain the identifiers but
omit every authenticated preimage.

For example, the `A-SOURCE-CORE` record does not permit the following required
reconstruction:

```text
patch_bytes = <absent>
sha256(patch_bytes)
  ?= 96bb6e173c09131ec01c2e1e0912e8d3bab80b4e25350b0e0b3105c1ff45b6e3
apply_exactly(source_sha256=272b6497..., patch_bytes)
sha256(mutant_source)
  ?= ae8940992de146989cb09c7440220be146e682de4983cd8f613d57a3407658f2
```

The same obstruction holds independently for all six rows.  Since the bytes
needed to define the changed objects are absent, the recorded mutant-source,
probe, stderr, runtime, RSS, zero-write, and seven-object-movement claims
cannot be independently tied to those exact mutations.  The freeze's
positive statements are therefore attestations, not replayable certificate-
action evidence.

## 5. Effect on source adjudication and scientific scope

The failure occurs before the scientific gate.  It does not establish a
counterexample to the candidate Gamma arithmetic, category laws, record
division, reciprocal response, matching control, or native nondivision
calculation.  Those later claims remain unadjudicated by this seat after the
stopping point.

In particular, nothing in this finding conflates native stochastic
nondivision with ontological state incompleteness.  Native nondivision is the
failure of a positive source-independent restart factor at the declared cut;
it is not evidence that an actual configuration is unreal or incomplete.
Likewise, positive history/enlarged-carrier Markovization is a mandatory scope
control and is not an automatic kill of the native result.  The source's
walls leaving actualization postulated and valuation, metric, curvature,
continuum, and GR unconstructed are not enlarged by this audit.

The correct disposition is nevertheless `NO-GO`: Stage C is an audit of the
source **and its frozen evidence**.  A universal claim that all six exact real
source mutants were demonstrated is unsupported when none of the six changed
objects can be reconstructed from the authenticated record.

## 6. Findings ledger

1. **`KILL-1 — REAL-SOURCE-MUTATION-PATCH-BYTES-ABSENT`.**  All six mandatory
   real source-mutant records retain only patch/probe digests and prose, not
   the exact patches or probe/capture bytes required by the pin.  Earliest
   rung: `P13-SPECIFICATION-INCONSISTENT`.
2. **`KILL-1A — MUTANT-SOURCE-DIGESTS-NONREPRODUCIBLE`.**  Without the exact
   patch preimages, no independent audit can derive any recorded mutant source
   from the pinned source or prove that the named semantic mutation is the
   object whose hash appears in the freeze table.
3. **`KILL-1B — SEVEN-OBJECT-MOVEMENT-NONREPLAYABLE`.**  Without the exact
   probe/capture program and payload bytes, the claimed measurement, gate,
   outcome, lineage, shadow, claim-input, and seal movement is not an
   independently checkable certificate.
4. **`NON-KILL-1 — PINNED-CANDIDATE-BYTES-STABLE`.**  The authorized HEAD
   advance did not change the authenticated source, pin, or freeze-note bytes.
5. **`NON-KILL-2 — ABSTRACT-RECEIPT-MODEL-IMPLEMENTABLE`.**  The independent
   no-import reconstruction closes `480` action rows and rejects the complete
   identity-packet swap per key.
6. **`NOT-REACHED-1 — LONG BLACK-BOX PARITY`.**  Root, alien-CWD, and true
   one-file candidate runs were intentionally not launched after `KILL-1`.
7. **`NOT-REACHED-2 — SCIENTIFIC REGRESSION`.**  Exact R/B/C/B2/K,
   `527/175`, record/division/reciprocal/matching, and later receipt/seal
   claims were not used to override the earlier records blocker.

## 7. Literal repair and final gate

Because the authenticated snapshot is frozen, the repair requires a new
result-neutral source-freeze snapshot rather than an edit in place.  At
minimum, the authorized frozen record must bind, for each of the six rows:

```text
base_source_sha256
exact_patch_bytes
patch_encoding_and_application_rule
patch_sha256
derived_mutant_source_sha256
exact_probe_program_bytes
probe_program_sha256
exact_probe/capture_output_bytes
probe/capture_sha256
exit/stdout/stderr/runtime/RSS/zero-write evidence
recomputed measurement/gate/outcome/lineage/shadow/claim-input/seal objects
```

If stage whitelists permit no separate evidence artifact, these bytes must be
embedded canonically in the new freeze note.  If a separate artifact is
preferred, a new result-neutral pin must authorize and byte-bind its exact
path before source freeze.  Merely adding another digest or prose edit does
not repair the missing-preimage problem.

After that evidence is frozen, both blind source audits must restart on the
new immutable bytes.  Until then, the records/integrity disposition remains
**`NO-GO`**, fresh generation and official modes remain barred, and the
earliest defensible outcome is **`P13-SPECIFICATION-INCONSISTENT`**.

The ordinary SHA-256 is intentionally not embedded in these self-referential
bytes; it is reported externally after freeze.

normalized_sha256: 5a4254658e5d6347308d2d0a73b15563fb24347e72db3e3239d8c3393c5b6c6b
