# Paper 13 typed-groupoid v4 source delta pin

Status: **RESULT-NEUTRAL V4 SOURCE DELTA PIN / NO V4 SOURCE BYTE YET**

Date: 2026-08-20

## 1. Authority and bounded question

This pin implements only the forward authorization in
`v16/note-paper13-typed-groupoid-v3-source-audit-adjudication.md`, SHA-256
`1dd09ef639d96c973a3991890e96695692d89249e4033c61579ff5bdbdd93326`,
committed at `2c55425b27dc8f836a7742dd9097956482191da4`.

The bounded question is:

> Can the preserved presentation-indexed Paper 13 construction be closed
> under exact tensor-factor root provenance and complete per-key certificate
> action, with the promotion gate recomputing both actions from complete raw
> bytes and binding the full producer-to-consumer source slice?

This is result-neutral.  It does not declare the closures successful, restore
the rejected paper, pre-award a point-free referent, authorize a nonce, or
alter a scientific coordinate.  A new v4 source must pass two fresh mutually
blind source audits and adjudication before publication chronology can resume.

## 2. Immutable corpus and exposure

| object | path / identity | SHA-256 | use |
|---|---|---|---|
| RUNBOOK | `RUNBOOK.md` | `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58` | process contract |
| original construction pin | `v16/note-paper13-one-gamma-construction-pin.md` | `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35` | frozen law, ladder, and walls |
| typed-groupoid repair pin | `v16/note-paper13-typed-groupoid-forward-repair-pin.md` | `08f7f64efca6210eee356852ad9e9b59487ea62a55aeaf85a483f6a70b85b004` | complete typed sparse witnesses |
| split-support repair pin | `v16/note-paper13-stageA-support-split-forward-repair-pin.md` | `8ae54ada2a97f347a18b90adcab86dcb2e7c18c04c748cc5e0779b8251449a36` | contextual classes and split certificates |
| v3 delta pin | `v16/note-paper13-typed-groupoid-source-delta-pin.md` | `44fe6f86eeb6990537b36760eda68da5ccdc31fd8d15dfe003b42e6d4324a154` | inherited complete action language |
| rejected v3 source | `v16/code/p13_gamma_exact_v3.py` | `cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111` | regression and changed-source reference only |
| v3 freeze note | `v16/note-paper13-typed-groupoid-source-freeze-v3.md` | `02e22f32ce44d46104377d77469cefc1e7c3ca82445f119ede2056c9b8d16028` | authenticated development evidence |
| operator v3 audit | `v16/review-paper13-typed-groupoid-v3-source-operator.md` | `51e1a028c4e7d74fda2f1fe975d24a04e5925525916de1ba006ada80c2771a76` | internal tensor-factor-node survivor |
| records v3 audit | `v16/review-paper13-typed-groupoid-v3-source-records.md` | `1d0ceba5fca290399f8e24dfbf07b69c1b4758dfbc57c6e87cea9d5ac2cf9148` | complete identity packet-swap survivor |
| v3 adjudication | `v16/note-paper13-typed-groupoid-v3-source-audit-adjudication.md` | `1dd09ef639d96c973a3991890e96695692d89249e4033c61579ff5bdbdd93326` | binding outcome and repair boundary |

The exact internal-node and whole-target-packet survivors are exposed before
this pin.  Every prior source, mutation, artifact, paper, bundle, audit, and
number is exposed historical evidence.  Nothing old may be overwritten,
edited, deleted, or relabeled as v4 confirmation.

## 3. Frozen v4 language and scientific non-change

The v4 source is one self-contained exact standard-library evaluator at:

```text
v16/code/p13_gamma_exact_v4.py
```

It contains the complete frozen scientific construction.  It may be derived
mechanically during private work, but the committed source stands alone and
imports no prior evaluator, fixture, result, receipt, expected table, or paper.

All inherited exact classes and semantics remain unchanged unless this pin
explicitly strengthens a proof consumer:

```text
Formula / Context / Port / Boundary / Configuration / Arrow
SourcePresentation / SourceGroupoidWitness / BoundaryNode
ConfigurationTransport / ConfigurationActionLawRow
BoundSplitCertificate / CertificateActionInput
CertificateTransportTriple / CertificateActionLawRow
GammaLaw / exact LinearMap
```

No physical carrier, transition amplitude, Born clause, event grammar,
division doctrine, actualization rule, coupling, or value of `g` changes.
Python proof objects and AST addresses are verifier provenance, not ontology.
The physical candidate remains the typed Boolean source-groupoid orbit only if
the complete action passes.

The complete source key remains exactly the law identity and `g`, complete
source boundary, derived target boundary, full filling Arrow AST, and complete
source configuration.  There is no optional native/history-context payload.
Law-sufficiency belongs to that complete typed source argument at an
admissible division, never to a bare configuration at an arbitrary cut.

## 4. Tensor factor-root action closure

### 4.1 Exact public signature

The v4 tensor law constructor retains one exact public signature:

```text
tensor_action_row(
    tensor_source_node,
    tensor_configuration,
    left_node,
    left_configuration,
    left_witness,
    right_node,
    right_configuration,
    right_witness,
) -> ConfigurationActionLawRow
```

There is no alternate tensor law entry point, optional node, variadic
argument, default, global/cache-selected factor, or caller-supplied target.
An AST gate freezes this exact signature and the derivation paths below.

### 4.2 Root nodes are derived, not searched

The constructor derives:

```text
left_source_root  = boundary_node_at(left_witness.source,  (), "SOURCE")
right_source_root = boundary_node_at(right_witness.source, (), "SOURCE")
left_target_root  = boundary_node_at(left_witness.target,  (), "SOURCE")
right_target_root = boundary_node_at(right_witness.target, (), "SOURCE")
```

It requires exact node equality:

```text
left_node  == left_source_root
right_node == right_source_root
```

Membership in `BoundaryNodes(X)`, semantic boundary equality, catalogue
equality, configuration equality, or equal hashes after address erasure is
insufficient.  The required root nodes retain complete boundary bytes, AST
address `()`, and endpoint role `SOURCE`.

The source tensor presentation is built only from the two complete factor
source presentations.  Its root source node is independently reconstructed
and must equal `tensor_source_node`.  The source tensor configuration is built
from the two factor configurations on the exact root source boundaries and
must equal `tensor_configuration`.

The tensor witness is built from the two complete factor witnesses.  Each
factor transport must end at its derived root target node:

```text
left_transport.target_node  == left_target_root
right_transport.target_node == right_target_root
```

The tensor transport must end at the independently reconstructed root
`SOURCE` node of the tensor witness target.  Its target configuration is
compared with the tensor product formed from the two transported factor
configurations on those exact root target nodes.

Any mismatch refuses before a `ConfigurationActionLawRow` exists.  No later
`exact` Boolean can convert a wrong-provenance row into evidence.

### 4.3 Complete tensor law row

The immutable `TENSOR` row retains complete bytes or content-addressed raw
bytes for:

- left and right source/target presentations;
- left and right source/target root nodes;
- tensor source/target presentations and root nodes;
- both factor witnesses and the derived tensor witness;
- both factor source and transported configurations;
- tensor source, transported, and independently rebuilt target
  configurations;
- the three constituent `ConfigurationTransport` objects;
- exact source-product, target-product, node-provenance, and naturality
  residuals.

A no-import verifier reconstructs all nodes from presentation bytes and all
configurations from the typed boundaries.  It does not trust stored node
hashes, membership flags, or `exact`.

### 4.4 Tensor laws and coverage

Positive coverage includes identity/nonidentity factor witnesses, both factor
orders, unit factors, nested tensor factors, equal-semantic boundaries at
different addresses, and every tensor row already present in the 13 native
presentations.  Where compositions are typed, the verifier checks tensor
naturality against the independently composed factor actions.

The `TENSOR` configuration-action row itself carries no split certificate:
its exact eight-argument API has no law or certificate input, and a structural
tensor Arrow is not a generator.  In the encompassing native receipt, a
separate factor-lineage tuple is derived from the complete factor Arrow trees.
It contains zero, one, or many ordinary generator-bound certificates:

- unit, identity, symmetry, associator, unitor, and other structural leaves
  contribute none;
- a generator leaf contributes exactly its ordinary bound certificate when
  its registered nonzero transition is in scope;
- a nested tensor/composite contributes the canonical address-keyed flattening
  of every such leaf certificate.

Every retained entry is verified by the ordinary generator certificate-action
rules in Section 5.  Completeness requires exactly the generator leaves in the
declared factor paths, with no drop, duplicate, or structural pseudo-
certificate.  The tuple is receipt lineage, not an input to or premise of the
tensor configuration law.

## 5. Complete per-key certificate-action closure

### 5.1 Canonical complete action row

Every certificate action is serialized as an immutable
`CompleteCertificateActionRow` containing:

```text
complete witness bytes and identity
complete original CertificateActionInput bytes and reference
complete literal transported CertificateActionInput bytes and reference
complete independently rebuilt target input bytes and reference
original pairing-key bytes
transported pairing-key bytes
operation kind and branch coordinates
all fieldwise comparison residuals
```

The name is proof-language only.  It is not a new law or physical object.
The row's `exact` field is diagnostic; promotion is computed from an
independent decoder/verifier and never consumes it as a trusted premise.

### 5.2 Raw-byte decoder and recomputation

The source has one pure verifier:

```text
verify_complete_certificate_action_row(row, complete_store)
    -> recomputed action evidence
```

It performs, in order:

1. authenticate each store entry by hashing its complete canonical bytes;
2. decode exact slotted `SourceGroupoidWitness` and
   `CertificateActionInput` objects from those bytes using the frozen public
   language, with no registry, cache, preimage search, fixture, or expected
   table;
3. rebuild and validate every embedded law, presentation, AST address,
   subpresentation, source/target node, Arrow, occurrence, port,
   configuration, split proof, inverse proof, classifier input, coefficient,
   and inherited certificate hash;
4. recompute the original pairing key from the decoded original input;
5. call the closed `act_certificate(witness, original_input)` and require its
   complete bytes to equal the decoded literal target;
6. independently relabel the complete binding and rebuild a target input from
   the transformed law/Arrow/transition; require its complete bytes to equal
   the literal target;
7. recompute the transported pairing key from the decoded target input;
8. compare every field and return explicit residuals.

No caller-provided identity, stored hash list, trusted equality coordinate,
count, final flag, or copied summary Boolean can replace these steps.

### 5.3 Identity rows

For every identity row, promotion requires the independent verifier to prove:

```text
row.original_ref
  == row.literal_transport_ref
  == row.independent_rebuild_ref
  == row.input_ref
row.original_pairing_key
  == row.transported_pairing_key
  == row.pairing_key
decoded original bytes == decoded literal target bytes == decoded rebuild bytes
recomputed identity action == decoded original input
```

The census contains 468 such identity actions.  A target that is valid and
present in the store but belongs to another input key is rejected.

### 5.4 Nonidentity and functor rows

For nonidentity witnesses, target refs and keys may differ from the source,
but they must equal the literal action and independent rebuild derived from
that exact source input and witness.  The same decoder verifies every
nontrivial family row and every identity, inverse, composition, and
associativity chain.  Chain rows retain their constituent complete action rows
and require exact agreement of the two independently evaluated paths.

Pairing is by the recomputed original key and the witness-derived transported
key.  Incidental enumeration order is presentation only.  A pure enumeration
reorder must reproduce byte-identical canonical keyed output and is a required
non-kill.

### 5.5 Producer-to-promotion backward slice

The frozen static source gate binds the AST and direct dataflow of at least:

```text
measure_complete_certificate_action_census
all complete-row and byte-store serializers
certificate_pairing_key and transported-key derivation
build_certificate_action_input
act_certificate
independent target rebuild
verify_complete_certificate_action_row
complete census consumer
groupoid_promotion_predicate
claim, lineage, shadow, outcome, and seal consumers
```

The producer is load-bearing.  Changing an attachment in
`measure_complete_certificate_action_census` changes the static gate even if
all downstream function signatures remain unchanged.  The gate rejects an
alternate producer, wrapper, cache, copied table, or detached post-hoc
validator.

## 6. Exhaustive positive census and receipt closure

The v4 selftest reconstructs, rather than merely reads:

- 34 total typed bijections and 14,050 composable triples;
- 13 native presentations;
- 66 boundary-node occurrences and 988 complete configuration-action rows;
- 12 generator families, 312 source columns, and 468 bound nonzero
  transitions;
- 156 CREATE, 156 MERGE, and 156 UNCHANGED certificate actions;
- every original, literal-action, and independent-rebuild object;
- all identity, inverse, composition, associativity, and typed tensor rows;
- the 72 ambient / 42 contextual Boolean census;
- all zero-probability target coordinates.

The future receipt uses a deduplicated content-addressed raw-byte store.
Complete bytes appear at least once; references never substitute for absent
bytes.  A separate no-import verifier decodes and recomputes every promotive
row from the receipt.  It validates per-key action, not merely content-store
closure or a target multiset.

The source prints actual row counts, store counts, receipt bytes, peak memory,
and per-mode runtime.  Optimizing by single computation, streaming, or
content-address reuse is allowed; trimming the census, omitting raw bytes, or
replacing action checks with analytic tables is not.

## 7. Mandatory attacks

All 149 v3 attacks remain executable changed objects and retain their original
meaning.  Four additional attacks raise the minimum registry to 153.

### A17 — `TENSOR-INTERNAL-FACTOR-NODE`

Supply the exact adjudicated internal left factor node at AST address `(1,)`
instead of the factor root `SOURCE` at `()`, keeping an equal accepted
configuration.  Exact node hashes differ.  Construction must refuse before a
tensor row exists.  A membership-only predicate, address-erasing comparison,
or accepted `exact=true` row is a survivor.

### A18 — `TENSOR-TARGET-FACTOR-NODE-SEVER`

Keep both source roots and factor configurations exact, but make one factor
transport report a different valid target node while preserving its target
configuration.  Independent root-target reconstruction must refuse before
tensor naturality is evaluated.

### C22 — `COMPLETE-IDENTITY-TARGET-PACKET-SWAP`

Between two distinct identity inputs, swap the entire target packet:

```text
literal transport bytes/reference
independent rebuild bytes/reference
transported pairing key
```

Preserve row order, input refs, original keys, store, target multiset, counts,
operation classes, and within-row literal/rebuild equality.  The raw decoder
must reject both wrong identity actions and demote promotion.  A pure
enumeration reorder is a separate required non-kill.

### C23 — `COMPLETE-ACTION-PRODUCER-BYPASS`

Mutate only the producer so it attaches a valid complete target packet to the
wrong original key while leaving the validator and promotion function source
unchanged.  The static producer-to-promotion slice and decoded action check
must both fail.  A changed seal with an unchanged gate is a survivor.

Each attack records complete old/new object bytes and hashes, the exact
predicate, expected refusal, measurement, gate, outcome index, lineage,
claim-input DAG, seal, and publication-write count.  Labels, copied booleans,
or crashes without a semantic changed object are non-evidence.

## 8. Real post-freeze source mutations

After final v4 source freeze, six source-only true one-file/no-`.git`
mutations run under the same cap:

1. **A-SOURCE-CORE:** restore a caller-selected configuration target channel.
2. **A-SOURCE-ASSERT:** delete the exact target assertion equality.
3. **C-SOURCE-PROMOTION:** restore final-and-count-only certificate promotion.
4. **C-SOURCE-ACTION:** replace literal certificate action with a hash
   registry/cache or expected target.
5. **A-SOURCE-TENSOR-ROOT:** replace exact factor-root equality with the v3
   membership-only guard and feed the adjudicated internal node.
6. **C-SOURCE-TARGET-PACKET:** cross the complete target packet between two
   identity inputs inside the census producer while leaving consumer
   signatures unchanged.

Each mutant must first demonstrate the forbidden semantic behavior in an
independent probe and then make the frozen source selftest exit nonzero with no
official output.  It must move measurement, specification/groupoid gate,
strict outcome index, operator/action lineage, shadow DAG, claim-input DAG,
and seal.  The mutation record includes exact patch, old/new source hashes,
probe/capture hashes, exit, stdout/stderr hashes, runtime, and zero-write
evidence.

## 9. Preserved scientific regression wall

The delta cannot retune or replace any preserved coordinate.  Independently
reconstruct exactly:

- rational contact-Cayley law on `1/3 <= g <= 1/2`;
- `R`, `B`, coherent `C`, recorded `B2`, and
  `K=[[351,-176],[-176,351]]/175` at `g=1/2`;
- universal `527/175` native nondivision bound;
- positive history-conditioned and enlarged-carrier Markovization controls;
- exact native wording: no positive source-independent stochastic restart on
  the declared carrier, never ontological incompleteness;
- 72 ambient representatives and 42 contextual classes;
- all-input writer, six-letter continuation grammar, all-word record
  preservation, alternate-cut equality, and active inverse erasure;
- reciprocal joint `{00:9/25,01:0,10:144/625,11:256/625}`;
- one-root global matching, resource parity, prior-record/blind-prefix
  equality, and exclusion only of the declared incidence-blind transducer
  class;
- every source-sufficiency, anti-wrapper, actualization, exposure, and
  ontology wall.

The recorded two-step law remains `B2`; the unrecorded coherent law remains
`C`.  A stable record makes the declared complete record boundary a lawful
division on the frozen continuation grammar.  It does not turn each local
happening or arbitrary intermediate configuration into an autonomous Markov
restart point.

Passing this delta restores only eligibility to test the point-free referent.
It does not select a law, coupling, catalogue, event filling, division
doctrine, actual branch, event weight, causal order, or metric.

## 10. Outcome ladder and permanent walls

The inherited ordered Paper 13 ladder remains unchanged.  Either adjudicated
survivor, any incomplete action, or any static-source bypass caps the source at
`P13-REFERENT-PRESENTATION-ONLY`.  Passing v4 pre-awards no later rung.  The
last two law-selector rungs remain capped.

Every source output and eventual paper prints:

```text
event_filling_selection = PRICED-KINEMATICS
division_doctrine       = TYPED-CANDIDATE-AND-GRAMMAR-RELATIVE
actualization           = POSTULATED
happening_identity      = UNCONSTRUCTED-BEYOND-RECORD-CANDIDATE
causal_order            = UNCONSTRUCTED
event_weight            = UNCONSTRUCTED
valuation               = UNCONSTRUCTED
metric                  = UNCONSTRUCTED
curvature               = UNCONSTRUCTED
continuum               = UNCONSTRUCTED
GR                      = UNCONSTRUCTED
```

No event list, causal graph, global clock, unit event count, distance,
topology, metric, curvature, gravity, continuum, GR/QFT, particle, species,
Hamiltonian, or phenomenology claim enters this repair.

## 11. CLI, runtime, determinism, and integrity

The strict modes are versioned but unchanged in form:

```text
--selftest
--mutant NAME
--generate-fresh --nonce HEX --source-sha SHA256 --fresh-out ABSENT_PATH
--run --fresh FRESH_JSON --output ABSENT_PATH --receipt ABSENT_PATH
```

Only `--selftest` and development mutants may run before source-audit
adjudication.  No-argument, unknown, duplicate, incompatible, relative-path,
existing-destination, and malformed input cases refuse with no writes.
Publication is transactional and absent-path-only.

Scientific arithmetic is exact and standard-library-only.  There is no float,
tolerance, network, Git, CWD query, time-dependent science, unrecorded random,
fixture import, expected answer table, prior-source import, cache-dependent
answer, or duplicated response evaluator.  Source rooting uses `__file__`.

Every mode has a 300-second hard cap and emits a progress record at least once
per 60 seconds.  Repository-root, alien-CWD, and true one-file/no-`.git`
selftests must emit byte-identical stdout and leave no file, cache, `.pyc`, or
publication artifact.  The source freeze records actual wall time and peak
memory for all three runs.  Exceeding the cap is a source-freeze blocker, not a
reason to remove exact evidence.

## 12. Versioned paths and chronology

Future v4 paths are absent at pin freeze:

```text
v16/code/p13_gamma_exact_v4.py
v16/note-paper13-typed-groupoid-source-freeze-v4.md
v16/review-paper13-typed-groupoid-v4-source-operator.md
v16/review-paper13-typed-groupoid-v4-source-records.md
v16/note-paper13-typed-groupoid-v4-source-audit-adjudication.md
v16/code/p13_gamma_fresh_cases_v4.json
v16/code/p13_gamma_output_v4.txt
v16/code/p13_gamma_receipt_v4.json
v16/note-paper13-typed-groupoid-verification-v4.md
v16/paper-13-one-relational-gamma-v4.md
v16/paper13_typed_groupoid_v4_code/run_all.py
v16/paper13_typed_groupoid_v4_code/manifest.json
v16/paper13_typed_groupoid_v4_code/receipts_table.json
v16/paper13_typed_groupoid_v4_code/RUN.txt
v16/protocol-paper13-typed-groupoid-v4-hostile-review.md
v16/review-paper13-v4-operator-category.md
v16/review-paper13-v4-records-integrity.md
v16/review-paper13-v4-relational-ontology.md
v16/note-paper13-v4-hostile-review-adjudication.md
```

The v4 source is committed before any blind audit.  Two mutually blind audits
then write only their assigned report paths in separate commits.  A separate
adjudication is required.  Only acceptance may authorize one blind nonce,
whose future domain is:

```text
SHAKE256("P13-TYPED-GROUPOID-FRESH-v4" || v4_source_sha256 || nonce)
```

There is one generation, deterministic rejection/increment, no reroll, direct
global Gamma evaluation, and an independently implemented no-import verifier
before paper drafting.

## 13. Staged whitelists

Every non-audit stage updates `v16/PLAN.md`, `v16/LOG.md`, and `STATUS.md`.
No path outside the exact stage whitelist changes.

### Stage A — this pin

```text
v16/note-paper13-typed-groupoid-v4-source-delta-pin.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

### Stage B — v4 source freeze

```text
v16/code/p13_gamma_exact_v4.py
v16/note-paper13-typed-groupoid-source-freeze-v4.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

No v4 fresh, output, receipt, verification, paper, or bundle path exists.

### Stage C — two mutually blind source audits

```text
v16/review-paper13-typed-groupoid-v4-source-operator.md
v16/review-paper13-typed-groupoid-v4-source-records.md
```

Each seat changes only its own report path and freezes in a separate commit.
After both freeze, adjudication changes only:

```text
v16/note-paper13-typed-groupoid-v4-source-audit-adjudication.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

### Stage D — fresh, official artifacts, and verification

```text
v16/code/p13_gamma_fresh_cases_v4.json
v16/code/p13_gamma_output_v4.txt
v16/code/p13_gamma_receipt_v4.json
v16/note-paper13-typed-groupoid-verification-v4.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

### Stage E — paper and self-contained bundle

```text
v16/paper-13-one-relational-gamma-v4.md
v16/paper13_typed_groupoid_v4_code/run_all.py
v16/paper13_typed_groupoid_v4_code/manifest.json
v16/paper13_typed_groupoid_v4_code/receipts_table.json
v16/paper13_typed_groupoid_v4_code/RUN.txt
v16/PLAN.md
v16/LOG.md
STATUS.md
```

The bundle byte-binds and replays the frozen Stage-B/D science; it contains no
second implementation.

### Stage F — hostile review and adjudication

A result-neutral protocol freezes first in a commit containing exactly:

```text
v16/protocol-paper13-typed-groupoid-v4-hostile-review.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

At least three fresh mutually blind seats cover finite-map/action/category,
receipt/nondivision/division, and point-free/relational/ontology surfaces.
Each report freezes in its own commit and changes exactly one assigned path:

```text
v16/review-paper13-v4-operator-category.md
v16/review-paper13-v4-records-integrity.md
v16/review-paper13-v4-relational-ontology.md
```

After all reports freeze, adjudication changes exactly:

```text
v16/note-paper13-v4-hostile-review-adjudication.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

No report commit changes a ledger or sibling path.  Protocol, reports, and
adjudication never overwrite a v1--v3 object.  One exact counterexample
defeats a universal claim.

## 14. Pin audits and stopping rule

Before Stage A commits, two mutually blind read-only pin audits authenticate
the same immutable bytes.  They test implementability, exact API/type closure,
attack changed objects, arithmetic, runtime feasibility, outcome neutrality,
whitelists, and chronology.  A first exact contradiction stops that audit and
requires a new immutable pin snapshot; findings are never blended across
hashes.

After an accepted pin commits, Stage B may implement only this contract.  A
source selftest that prints a positive ceiling is development evidence, not a
scientific verdict.  A source audit's first exact survivor stops science and
bars fresh generation.

## 15. Paper 14 and Paper 15 boundary

Paper 14 begins only after terminal Paper 13 acceptance.  It must preserve the
distinction:

```text
stable happening = durable local actual fact, conditional on actualization
division boundary = complete future-sufficient restartable frontier
```

Not every stable happening is a Markov step.  Factorization is required only
at complete frontiers that pass record persistence, completeness, future
sufficiency, positivity, normalization, all-input cut equality, grammar
closure, no-history-smuggling, and no-global-clock gates.

Any happening weight must be Gamma-derived, nonnegative, presentation
invariant, additive under independent composition, monotone, and locally
finite.  Unit counting is a control, not a default ontology.  Paper 15 begins
only if Paper 14 earns point-free happening identity, local partial order, and
an extensive valuation; it must then test dimension, Lorentzian signature,
manifoldlikeness, scale, local duration, and metric reconstruction rather than
assume spacetime.

## 16. Freeze evidence and next event

The v4 source freeze must record source identity, line/byte counts, AST/static
hashes, exact signature/dataflow scans, full selftest/stdout/payload/registry
hashes, all census and store counts, receipt-size estimate, peak memory,
root/alien/one-file parity, all 153-or-more attacks, six real source mutations,
artifact absence, and every preserved scientific coordinate.  The freeze note
records the source hash; its own ordinary hash is recorded afterward in
PLAN/LOG/STATUS to avoid a self-hash instruction.

After this pin freezes and its two audits accept, the sole authorized next
event is Stage B construction and freeze of the v4 source and note.  No nonce,
publication mode, paper, Paper 14, Paper 15, metric, curvature, gravity,
continuum, GR/QFT, or later unit may begin first.

normalized_sha256: 24ab3fc9072b39c2e128158a20352c1ffe1375ee46c5c40fb9e0988c4c447263
