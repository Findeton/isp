# Paper 13 typed-groupoid source freeze v4

Date: 2026-08-20

Status: **FROZEN / REPAIR-GREEN-UNREVIEWED / NO FRESH CASE GENERATED**

## Authority and bounded result

This note freezes the Stage-B source authorized by
`v16/note-paper13-typed-groupoid-v4-source-delta-pin.md`, ordinary SHA-256
`ae1283784bdcb274ff16cc2f06288f27258e0ada0dd8efe2f84084339941acb0`
and normalized SHA-256
`24ab3fc9072b39c2e128158a20352c1ffe1375ee46c5c40fb9e0988c4c447263`.
The binding v3 source-audit adjudication is
`v16/note-paper13-typed-groupoid-v3-source-audit-adjudication.md`, SHA-256
`1dd09ef639d96c973a3991890e96695692d89249e4033c61579ff5bdbdd93326`.

The authenticated forward-repair corpus includes:

| object | path | SHA-256 |
|---|---|---|
| RUNBOOK | `RUNBOOK.md` | `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58` |
| rejected v3 source | `v16/code/p13_gamma_exact_v3.py` | `cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111` |
| v3 source freeze | `v16/note-paper13-typed-groupoid-source-freeze-v3.md` | `02e22f32ce44d46104377d77469cefc1e7c3ca82445f119ede2056c9b8d16028` |
| v3 operator audit | `v16/review-paper13-typed-groupoid-v3-source-operator.md` | `51e1a028c4e7d74fda2f1fe975d24a04e5925525916de1ba006ada80c2771a76` |
| v3 records audit | `v16/review-paper13-typed-groupoid-v3-source-records.md` | `1d0ceba5fca290399f8e24dfbf07b69c1b4758dfbc57c6e87cea9d5ac2cf9148` |

This is an implementability freeze, not a positive Paper-13 verdict. It does
not restore any rejected paper, pre-award the point-free referent, authorize a
nonce, or authorize an official Paper-14 construction.

## Frozen source identity

| property | value |
|---|---|
| path | `v16/code/p13_gamma_exact_v4.py` |
| SHA-256 | `272b64972e3eb620867cf6ad0decf8db1fcc03092adfd1d69d77aa10e2605910` |
| lines | `16564` |
| bytes | `656207` |
| schema | `p13-gamma-exact-v4` |
| AST parse | `PASS` |
| float AST nodes | `0` |
| forbidden calls | `0` |
| forbidden imports | `0` |
| Git-query literals | `0` |
| answer-table names | `0` |
| support-promotion AST SHA-256 | `1f40e18056b38afe19390885994627220fd8bbca485bad8fdcbde39e898cfc25` |
| groupoid backward-slice AST SHA-256 | `5e246ccc26ebf4338b0889344830b154680f98e1b5369da8c2fac9efc629ab8c` |
| static-audit record SHA-256 | `309ce463239d9a45bfba5238ab3d32608343e037397b9b86aa767116988acf46` |

The exact action signatures, target assertion, tensor root-source/root-target
equalities, literal certificate transport, raw decoder, per-key action
verification, and producer-to-promotion slice are all in the bound AST. The
static scan excludes caller targets, registries, expected-target oracles,
copied final booleans, count-only promotion, and detached validators.

Before expensive reconstruction, `--selftest` recomputes the same exact
static, support, and groupoid backward-slice gates. This is not a source-hash
whitelist: each gate is an AST/dataflow theorem. A changed source must first
demonstrate its forbidden semantics in an independent probe; the full
selftest then refuses the inexact backward slice before spending the
300-second mode budget.

## Typed action closure

The configuration action remains exactly:

```text
act_configuration(source_node, configuration, witness)
```

It derives its target internally. The assertion-only helper requires exact
equality with that target. Tensor action independently reconstructs both
factor root `SOURCE` nodes, both root targets, and the tensor root target. An
internal factor node is not interchangeable with a factor root even when its
boundary value happens to be semantically equal.

`CertificateActionInput` retains the complete literal binding. Certificate
action remains exactly:

```text
act_certificate(witness, certificate_action_input)
```

It constructs the transported binding field-by-field and compares it with an
independent rebuild. The complete-action census decodes raw bytes and checks
each original key against its own derived target packet. Enumeration reorder
is a non-kill; crossing complete target packets is a kill.

The full mutation registry shares only immutable setup objects. Each mutation
still constructs independent copy-on-write changed objects and records the
same old/new canonical bytes. Standalone `--mutant` execution builds its own
context. No Gamma operator, endpoint probability, or physical response is
cached.

## Exhaustive positive census

The fixture-free selftest reconstructs and serializes:

- `34` abstract total bijections and `14050` composable triples;
- `13` native presentation rows;
- `66` boundary-node occurrences and `988` configuration-action rows;
- `12` generator families and `312` declared source columns;
- `468` nonzero certificate-bound transitions;
- `468` identity actions plus `12` nontrivial complete actions, all decoded
  from raw bytes and checked per key;
- `CREATE=156`, `MERGE=156`, and `UNCHANGED=156`;
- three tensor cases with factor-certificate cardinalities `24`, `12`, `24`;
- `72` ambient Boolean representatives, `42` contextual classes, and `72`
  exact replays;
- all coefficient-zero target coordinates.

The content-addressed evidence stores contain:

| store | objects | canonical bytes |
|---|---:|---:|
| complete certificate-action store | `504` | `46642013` |
| thirteen native configuration-action stores | `7968` | `6195774` |
| tensor-action store | `132` | `1658613` |

The store-count record SHA-256 is
`f3cbc7644c14e85e2da5dbb4f476191c187349b3567b4f242c54143edb88a0e7`.
The raw selftest evidence payload is `242830641` bytes and is the source-stage
upper-bound estimate used for later receipt planning; it is not an official
receipt.

The native action-count record SHA-256 is
`a9aefd3e43d695515f23ced05118cdb1b9a3694f646107a54260255184e3cf4a`.
All thirteen rows are exact, including duplicate-semantic-node provenance,
record, reciprocal, matching, and tensor rows.

## Development selftest freeze

Only `--selftest` and development-mutant paths ran. Neither
`--generate-fresh` nor official `--run` ran.

| property | value |
|---|---|
| status | `PASS` |
| checks | `50/50` |
| registered attacks killed | `153/153` |
| inherited attacks | `149` |
| v4 additions | `A17`, `A18`, `C22`, `C23` |
| mutation-registry SHA-256 | `443f70a2b61c00fc0c0ed5bb6ab4175ca0fa363a224d861917548e3fa2da1972` |
| normalized payload SHA-256 | `3041d9f26f33903ad3554dd18eda915f728c7a956dda49065408a00633d3cba7` |
| exact stdout SHA-256 | `95d7975c643a0bd95e60cc1420ef0b0bcb6f157ffbe1a3cd6c70a70b6dc62880` |
| exact stdout bytes | `242830641` |
| repair disposition | `REPAIR-GREEN-UNREVIEWED` |
| strict eligible cap | `P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED` |
| scientific fixture evaluated | `false` |
| fresh cases read | `false` |
| official artifacts read | `false` |
| publication writes | `0` |

An independent canonical deletion/re-hash of the normalized field reproduces
`3041d9f2...3cba7`. The selected-evidence record SHA-256 is
`91963677a925ddc72ea07c11c49dc63b854d5fd07e7d46c9e93b5868669a8c32`.

## Root, alien-CWD, and true one-file parity

The three peak-memory replays used exact source SHA-256
`272b64972e3eb620867cf6ad0decf8db1fcc03092adfd1d69d77aa10e2605910`.
The off-tree directory contained one source file and no `.git` directory.

| execution | wall time | peak RSS bytes | stdout SHA-256 | result |
|---|---:|---:|---|---|
| repository root | `199.187052 s` | `856850432` | `95d7975c...62880` | `50/50`, `153/153` |
| alien CWD | `267.359979 s` | `913489920` | `95d7975c...62880` | `50/50`, `153/153` |
| true one-file, no `.git` | `258.438360 s` | `1107476480` | `95d7975c...62880` | `50/50`, `153/153` |

The outputs are byte-identical. Every replay remained below `300 s`, emitted
progress at intervals no greater than 60 seconds, and left its working
directory unchanged. The external rusage wrapper never imported the
candidate; its SHA-256 is
`1d7a27fa424ea3698ffd5f4c43519e89617df71290bc4ef20e75a859055f50bd`.
The exact rusage summary SHA-256 is
`e8e1d7d101a5a9d5125f8e4d381292f59048e0b8b11ba2f1addd5e98edb8716c`.

## Real post-freeze source mutations

Six one-file/no-`.git` mutations start from the frozen source. Each independent
probe demonstrates the forbidden behavior and recomputes movement of:

```text
measurement -> groupoid gate -> outcome/rung -> action lineage
            -> shadow DAG -> claim-input DAG -> seal
```

For every mutation all seven objects move, the clean gate is `true`, the
mutant gate is `false`, and the independent outcome moves from index `12` to
index `1`, `P13-REFERENT-PRESENTATION-ONLY`. The probe script SHA-256 is
`0f8112348377560a3d1eb5a72f2e26b7f47b0f32eb487ed5ed320796f5571433`.

Each full mutant selftest exits `1` before science, emits empty stdout SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`,
and emits common stderr SHA-256
`9bbc91359269b0baf5b7a1756d5789b274bfd691a71350da4daa58058a090e7f`:

```text
pre-science source-integrity backward slice is inexact
```

No mutant reads or writes an official artifact.

| mutation | mutant source SHA-256 | patch SHA-256 | probe SHA-256 | runtime | peak RSS |
|---|---|---|---|---:|---:|
| A-SOURCE-CORE | `ae8940992de146989cb09c7440220be146e682de4983cd8f613d57a3407658f2` | `96bb6e173c09131ec01c2e1e0912e8d3bab80b4e25350b0e0b3105c1ff45b6e3` | `609b51ca6988d3dab82f3eff7fff359631a1f48f6fb07c94216e077df1bd2469` | `1.807087 s` | `133906432` |
| A-SOURCE-ASSERT | `e0821f2970b4f1d15c9fb022b9ffad6a2f124fa68c12a60d667a3bc2e6ddc177` | `7f2f0ae030832bf9b68b326dac0149dae957cb57031e0004074a3d2ddccf8dbd` | `74703a68eed500cd255b62dd4ff99eee78fd5cd815e98d112f240e32ab6b2373` | `1.873645 s` | `132300800` |
| C-SOURCE-PROMOTION | `f3fd38e6f0e31ed6e93cf1f51a919beb016d258cebccbcb499aee7411ea1f48b` | `0e9d6424e03356bbade1514f97e31a2e36c388581af0ebd18c675e14bb1ec84c` | `b58230cbeda93504591478910b66b4638c58c488640eb052ccef65912793cc88` | `1.812220 s` | `130449408` |
| C-SOURCE-ACTION | `ea8e3df75421a62eaadaf6bbaf85844352cc1a5bd4c26f9aaf6a69752655d920` | `387649d2d016186a6240571c073e3f361caebf33705fcfdc02503038568bb0d2` | `0dd5ab68d799e0521a80fc81a54a440293db09748287e55ea1db05ead21e304f` | `1.849501 s` | `126058496` |
| A-SOURCE-TENSOR-ROOT | `111ff506cdf0e1857dec5ceb5884058bcd5c32eedf2612cc2024afbf3a4d58dc` | `7125c2f7e9b9b4416d478767d24ad22838e4b4640fcebd03adc995b6bfdd6647` | `7518301e3536877e425e94684a20d3357bef5ea691c5365a18f455f0c601e657` | `1.792206 s` | `132186112` |
| C-SOURCE-TARGET-PACKET | `ff0a52003c31cbd79f6ca37b72e385fc96de4bcbf79e9837325bb36d24cd74fa` | `37309ea3a9aa140f9a88942c2a18431a6cf20c7ebec34c6723dfb581e4e39ce6` | `b631cee8f5f9dd14a782e30dea1ab93b590bc7dc04c4139c5ed47931c2eef50d` | `1.825642 s` | `128303104` |

The semantic probes show, respectively:

1. direct acceptance of a caller-selected nonimage target;
2. deleted asserted-target equality with no refusal;
3. weak final/count promotion accepting a crossed target multiset;
4. replacement of literal action by the rebuild oracle;
5. acceptance of an internal factor node at address `(1,)` instead of root
   address `()`; the complete node hashes are distinct;
6. crossed literal/rebuild/key target packets, for which both per-key identity
   bindings and raw action verification fail.

## Preserved scientific regression wall

The v4 repair does not retune the law or any exposed coordinate:

```text
R  = [[3/5,-4/5],[4/5,3/5]]
B  = [[9/25,16/25],[16/25,9/25]]
C  = [[49/625,576/625],[576/625,49/625]]
B2 = [[337/625,288/625],[288/625,337/625]]
K  = [[351/175,-176/175],[-176/175,351/175]]
```

The universal native nondivision bound remains `527/175`. The reciprocal
joint remains `{00:9/25,01:0,10:144/625,11:256/625}`. Four writer inputs,
six continuation generators, 16 all-input cut comparisons, free-word record
preservation, active inverse erasure, the history-conditioned positive
control, global matching/resource parity, and the class-relative blind
exclusion remain exact.

The negative native factor means only that no positive, source-independent
stochastic kernel restarts the process at that cut on the declared
configuration space. A definite configuration may still be actual there;
history or phase enlargement may Markovize a representation. Stable record
divisions remain relative to the declared typed continuation grammar.

## Ontology and future-paper walls

The source continues to enforce:

```text
event_filling_selection = PRICED-KINEMATICS
division_doctrine       = TYPED-CANDIDATE-AND-GRAMMAR-RELATIVE
actualization           = POSTULATED
valuation               = UNCONSTRUCTED
metric                  = UNCONSTRUCTED
```

No passing development run selects `g`, a coupling, catalogue, filling,
division doctrine, or actual outcome. It does not prove absolute relational
irreducibility, time, topology, dimension, signature, continuum, metric,
curvature, QFT, gravity, or GR.

Nonbinding Paper-14 preparation, if kept outside the repository and outside
the v4 evaluator, is not Paper-14 scientific evidence. Authoritative happening
identity, event count or weight, causal order, division frontiers, metric
claims, evaluator construction, and publication remain closed until Paper 13
receives terminal acceptance.

## Artifact absence and next authorized event

All 17 future v4 source-audit, fresh, output, receipt, verification, paper,
bundle, hostile-protocol, hostile-report, and adjudication paths named by the
pin are absent. The exact absence record SHA-256 is
`8ec7fcf6f77528b6d34f9d91fdf635c0870ae88538a591d0c1f98d3a57fa32d1`.
No v4 `.pyc` remains.

No nonce exists, no fresh case was generated, no official/publication mode
ran, no official artifact was read, and no publication write occurred. The
Stage-B changed paths are exactly this source, this note, and the required
`v16/PLAN.md`, `v16/LOG.md`, and `STATUS.md` bookkeeping.

The sole next Paper-13 scientific event is the two mutually blind Stage-C
source audits, followed by a separately committed adjudication. Fresh
generation and publication remain barred until those gates accept.

This note intentionally does not contain its own ordinary SHA-256. That hash
is computed only after these bytes freeze and is then recorded in
`v16/LOG.md` and `STATUS.md`.
