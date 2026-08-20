# Paper 13 typed-groupoid source freeze v3

Date: 2026-08-20

Status: **FROZEN / REPAIR-GREEN-UNREVIEWED / NO FRESH CASE GENERATED**

## Authority and bounded result

This note freezes the Stage-B source authorized by
`v16/note-paper13-typed-groupoid-source-delta-pin.md`, ordinary SHA-256
`44fe6f86eeb6990537b36760eda68da5ccdc31fd8d15dfe003b42e6d4324a154`
and normalized SHA-256
`354b28c183622d61dcf643df4e1c654130f50e8c2ab5be9b34bbe4da357ab76a`.
The binding defect adjudication is
`v16/note-paper13-typed-groupoid-source-audit-adjudication.md`, SHA-256
`92466ffa960ce0c3590b4d64707a9dc72fa61a6c76a623e492854c1d7ac3cb50`.

The authenticated forward-repair corpus includes:

| object | path | SHA-256 |
|---|---|---|
| RUNBOOK | `RUNBOOK.md` | `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58` |
| rejected v2 source | `v16/code/p13_gamma_exact_v2.py` | `b56383236a2aa0ff484aaa4c9082393beb4e4dd3ceb4d2724e4332bf68b6cba1` |
| v2 source freeze | `v16/note-paper13-typed-groupoid-source-freeze.md` | `33ff983e6c9b8f4bab6aa98abfea18f0f27d609b572c7980e05e7e63e80e51f7` |
| operator source audit | `v16/review-paper13-typed-groupoid-source-operator.md` | `884337d385d0997d7fddcf748297544869c9effc537c46017a6db018c7f4da5a` |
| records source audit | `v16/review-paper13-typed-groupoid-source-records.md` | `c90a16072084896da248a53551a54dc44eb0f7c668c401395b2c1d1b49c0cf07` |

This is an implementability freeze, not a positive Paper-13 verdict.  It does
not restore the rejected paper, pre-award the point-free referent, authorize a
nonce, or license Paper 14.

## Frozen source identity

| property | value |
|---|---|
| path | `v16/code/p13_gamma_exact_v3.py` |
| SHA-256 | `cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111` |
| lines | `14941` |
| bytes | `595989` |
| schema | `p13-gamma-exact-v3` |
| AST parse | `PASS` |
| float AST nodes | `0` |
| forbidden calls | `0` |
| forbidden imports | `0` |
| Git-query literals | `0` |
| answer-table names | `0` |
| public exact types visited | `27/27` |
| support-promotion AST SHA-256 | `1f40e18056b38afe19390885994627220fd8bbca485bad8fdcbde39e898cfc25` |
| groupoid-promotion backward-slice AST SHA-256 | `f35274555434590299221184229be0e0577b7e585da151eb34b3d42449da7fcd` |

Every behavior-bearing public node remains exact, frozen, and slotted.  The
v3 source imports no v1/v2 evaluator, fixture, private design, output,
receipt, or paper.  The static promotion scan requires the exact public action
signatures, exact assertion equality, literal certificate-input action, full
raw-byte validators, and the absence of caller-target, registry, cache,
preimage, copied-final, count-only, and hash-list-only channels.

## Typed action closure

The configuration action is exactly

```text
act_configuration(source_node, configuration, witness)
```

and derives its target node internally.  A separate assertion-only gate

```text
assert_configuration_target(source_node, asserted_target_node, witness)
```

requires the asserted node to equal the derived witness image before any
action result can be used.  Identity, inverse, composition, associativity, and
tensor rows retain their constituent typed transports and compare complete
target nodes and configurations.

`CertificateActionInput` binds one inherited hash-bearing split certificate
to the literal law, enclosing presentation, generator AST address, source and
target boundary nodes, Arrow, occurrence, port, contextual parent,
configurations, proof objects, classifier, and coefficient.  Its factory
recomputes every inherited identity.  Certificate action is exactly

```text
act_certificate(witness, certificate_action_input)
```

with no registry, hash-preimage, cache, caller target, or expected-output
parameter.  It transports the literal binding, independently rebuilds the
target binding, and compares a total keyed bijection.  Equal-semantic nodes or
generators at distinct AST addresses remain distinct provenance rows without
becoming distinct physical values.

## Exhaustive positive census

The fixture-free selftest directly serializes, rather than merely counts:

- `34` abstract total bijections and `14050` composable triples;
- `13` native presentation rows;
- `66` native boundary-node occurrences and `988` complete configuration
  action rows;
- identity, inverse, composition, and associativity rows for every admitted
  configuration action, plus an exact tensor action row;
- `12` generator families, `312` source columns, and `468` nonzero
  certificate-bound transitions;
- `468` identity certificate triples and one nontrivial complete transport per
  generator family;
- operation totals `CREATE=156`, `MERGE=156`, and `UNCHANGED=156`;
- all coefficient-zero target coordinates;
- `72` ambient Boolean representatives, `42` contextual classes, and `72`
  exact replays.

Per native presentation, the complete configuration-action counts are:

| native row | boundary nodes | configuration rows |
|---|---:|---:|
| minimal role A-to-B | 2 | 4 |
| matter namespace | 6 | 36 |
| port namespace | 6 | 36 |
| occurrence namespace | 6 | 36 |
| all four namespaces | 14 | 84 |
| contextual Boolean alias | 2 | 12 |
| bound split CREATE | 2 | 12 |
| bound split MERGE | 2 | 12 |
| bound split UNCHANGED | 2 | 12 |
| record writer/continuation | 6 | 216 |
| reciprocal writer/probe | 6 | 216 |
| size-12 global matching | 6 | 216 |
| tensor, two nontrivial factors | 6 | 96 |

The complete input/object stores are content-addressed.  Raw bytes are emitted
once and every node, configuration, input, literal transport, independent
rebuild, law row, and pairing row refers back to those bytes by a validated
identity.  Enumeration reorder is a non-kill; changing the object attached to
a derived key is a kill.

## Development selftest freeze

Only `--selftest` and development-mutant paths ran.  Neither
`--generate-fresh` nor official `--run` ran.

| property | value |
|---|---|
| status | `PASS` |
| checks | `49/49` |
| registered attacks killed | `149/149` |
| inherited attacks | `112` |
| v3 attacks | `37` (`A1-A16`, `C1-C21`) |
| mutation-registry SHA-256 | `bf00b70045431960356b8a1a0032a1aea2a598ddca750f98d6c1f15867ac5d12` |
| normalized payload SHA-256 | `43aa7476d76315329bb7bd464131c8f3ac35e797c1fef249decc63b4c29d7955` |
| exact stdout SHA-256 | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` |
| exact stdout bytes | `234018261` |
| repair disposition | `REPAIR-GREEN-UNREVIEWED` |
| strict eligible cap | `P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED` |
| scientific fixture evaluated | `false` |
| fresh cases read | `false` |
| official artifacts read | `false` |
| publication writes | `0` |

The new load-bearing checks cover complete configuration action at every
boundary node, complete certificate action over all 468 bound transitions,
tensor configuration action, raw-byte groupoid promotion, source mutation
backward slices, and all 37 v3 attacks.  All inherited support, Gamma,
division, nondivision, reciprocal, matching, result-neutrality, CLI, read,
seal, and artifact-separation checks remain live.

## Root, alien-CWD, and true off-tree parity

All three runs used the exact frozen source bytes.  The off-tree directory
contained only the source and no `.git` directory.

| execution | runtime | stdout SHA-256 | normalized payload | result |
|---|---:|---|---|---|
| repository root | `234.02 s` | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` | `43aa7476d76315329bb7bd464131c8f3ac35e797c1fef249decc63b4c29d7955` | `49/49`, `149/149` |
| alien CWD, absolute repository source | `281.65 s` | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` | `43aa7476d76315329bb7bd464131c8f3ac35e797c1fef249decc63b4c29d7955` | `49/49`, `149/149` |
| true source-only off-tree, no `.git` | `280.61 s` | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` | `43aa7476d76315329bb7bd464131c8f3ac35e797c1fef249decc63b4c29d7955` | `49/49`, `149/149` |

The outputs are byte-identical.  All runs remained below the pinned
`300 s` cap and emitted progress at no more than 60-second intervals.  The
largest observed changed-source maximum resident set was `878362624` bytes;
the largest observed completed runtime was `281.65 s`.

## Real post-freeze source mutations

Four exact source-only mutations started from SHA-256
`cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111`.
Each ran outside the repository with no `.git`, returned child exit `1`,
emitted zero stdout bytes with SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`,
and made `0` publication writes.  The common captured stderr SHA-256 is
`f62025095466d5d6d55e0ff1789b6af94b3680cc99135ae6647dbfa0605b68a6`;
it contains the four progress records and an integrity stop before a
publishable payload.

### A-SOURCE-CORE — caller-selected target backdoor

The patch adds a fourth optional target argument to `act_configuration` and
returns it directly.  Exact patch SHA-256:
`688a9799aebeded8f9e4588c75ed24ccf673143a9d2f66decf039f743c07e82f`.

| property | value |
|---|---|
| mutant source SHA-256 | `efc4b2f48c30225e5d8a5344c7765e1c147a147915a460fba5b66bdac5aba6e8` |
| semantic probe SHA-256 | `27cf0fbbadfe1852e2d1577777c19ce989ad584637c81308e44401a90b8d8de8` |
| semantic payload SHA-256 | `6b8298a657b5e4d1a8202d24cbc5f352afdfd63b8a24883930a97c325f78b6d6` |
| full-run capture SHA-256 | `99567e720b852377f722d7fdd30880695e2882b69351650fc72dea712690f2f2` |
| runtime / peak RSS | `273.285174 s` / `878362624` |
| dependency probe SHA-256 | `94cb4e88aaa4a892c09e5506613f6a0f50596cdf0a2ad9f0078a0d126cb34a86` |

The direct call returns the asserted `CARRIED` target although the identity
witness image is `ACTIVE`.  Canonical source and derived target bytes are both
`650` bytes, SHA-256
`839d5b7b877e7f053bf85cab972405a64d943bc72ddd42c955863906c05cd921`;
the forged asserted target is `652` bytes, SHA-256
`285fb16d5db4fdb38e6acc83af4ca563ea0b43a03e440302eda6a007bdfcc115`.
The source/asserted pair is `1305` bytes, SHA-256
`64c8b5315313a9ddd63ed6c365f1bbd6b3ae65fb79f45053e407d5c389497acb`.
The exact-signature and core-dataflow coordinates fall.

### A-SOURCE-ASSERT — deleted target equality

The patch removes only the nonimage comparison and refusal from
`assert_configuration_target`.  Exact patch SHA-256:
`f772dce926d65b8c70346f6e6bf535ff323c30da3cf8ebed4bb32ebc8f8f0d45`.

| property | value |
|---|---|
| mutant source SHA-256 | `5b35c510b286a9ca4c67e99f3a06c1b8545f50692f2ad012b00553d746fb5c21` |
| semantic probe SHA-256 | `2a473bc04b7a13d738d18de6d61c65dcc46637dd51c2face76c901c9a27ad8e3` |
| semantic payload SHA-256 | `a58f05b3d0282b137a6aefb47e9946f67edd9152f8991cc4957bef58e343bd58` |
| full-run capture SHA-256 | `2552eeef2ff5602118d82391beb5232f1b73d7e5c8920a18cd38e5c523b88d03` |
| runtime / peak RSS | `273.166352 s` / `866435072` |
| dependency probe SHA-256 | `d8fe53f13ef899e185b775aff091cd85b5fe4ba8134a66acdab97f90be9c27ed` |

The same nonimage target bytes are accepted, while the helper returns the
derived target.  The exact signature remains true but
`assertion_target_equality_exact` becomes false.  This proves the assertion
comparison itself, rather than only the public-core arity, is in the
promotion backward slice.

### C-SOURCE-PROMOTION — copied final/count summary

The patch inserts the rejected predicate based on abstract/native `all_exact`,
identity count `468`, copied native certificate finality, and tensor
`all_exact`.  Exact patch SHA-256:
`85086e9871578fa9beebf7fc969dc844010c0506017075403975d90acbc07584`.

| property | value |
|---|---|
| mutant source SHA-256 | `baf0360c51099db0774760de4b72ccefde329ce469b8f05a02309ca895817bfb` |
| semantic probe SHA-256 | `2ff239a7ae5576c821e614dd9f6975e06e4bc6ddd6e4afe2f2fdfc482e65c85b` |
| semantic payload SHA-256 | `806db88e29697271c9e81fbc08d07772a3ea71454c889757907521f3e31a7efc` |
| full-run capture SHA-256 | `0a197194343bfcafdebb0514de10d9c1bde9008e84e6195bb4562d62863b50d7` |
| runtime / peak RSS | `271.932171 s` / `866385920` |
| dependency probe SHA-256 | `057763a55a1498b8a0cd6a40e90aee04e3bdae8cd6fcb5cf07d38ebd2485de2c` |

The copied predicate accepts a malformed `269`-byte promotion input with no
complete certificate table, SHA-256
`a91accc6ced59a68aaeb08ef09784543fbf45813f3b2b8652b253c0977c3b9d9`.
The static scan detects the copied summary and refuses promotion.

### C-SOURCE-ACTION — hash/registry backdoor

The patch adds an optional registry and lets `act_certificate` return a value
from a hash key.  Exact patch SHA-256:
`6e592035b562502c9277de905a43dd983adf9748e2db60211161c0479db49635`.

| property | value |
|---|---|
| mutant source SHA-256 | `f7fa69c1d803c5369e07313ad51d0cd3b6ff5bf4eca3678727a1895b84a307e1` |
| semantic probe SHA-256 | `b58d54438363c417a3643aef481888779ba98ca48b006614e092ea6381cf03b2` |
| semantic payload SHA-256 | `34630de0aedbf2e6c3bb60200cf7f2e46be46cf85370f87b69eec8b20c019aef` |
| full-run capture SHA-256 | `be742f385a7e11571f3940b49fc8e0678f7ed80490b75e54bdef83a95181e5d9` |
| runtime / peak RSS | `273.064753 s` / `849887232` |
| dependency probe SHA-256 | `d03736286036b95d9c2e922f6268a91539024f238ea51e9f00495cd185fbfa36` |

The backdoor accepts a `66`-byte hash-key object, SHA-256
`4ad002a9e4fe576dc0a673d7cb591f2c1b2215d926c5c7990157c1782e9ef286`,
instead of the complete `22139`-byte input, SHA-256
`f037244f2893463b530bedf6e33eca21ab4d93589083c556d2ee0438238a4141`.
It returns `29048` bytes, SHA-256
`8e3cd5f2c64afc573532f01f78d157277a355a26739d40826e00ae1d0ee048b1`.
The complete input/returned pair is `51190` bytes, SHA-256
`c8f9484ce3d7d6054ab8c336ad10b9e12cfd7071f709c5ecaa6d6b013ced30d9`.
The exact action signature and no-registry dataflow coordinates fall.

## Downstream dependency movement

The dependency probe is SHA-256
`045d455620469935db1e10cc9afade36cf0ab7d04c975ac2db9b34642f1dec83`.
For every source mutant, all required downstream objects move:

| object | frozen | A core | A assert | C promotion | C action |
|---|---|---|---|---|---|
| promotion AST | `f3527455...7fcd` | `184f1565...2abd` | `6b3d63e8...63fe` | `256b1cb1...8bed` | `e22c031f...eb7` |
| measurement slice | `cc3a7f47...afc7` | `e76effde...b39b` | `9b722bb5...80d6` | `651ced5b...e1f1` | `be8ffe89...aa32` |
| operator lineage | `d6f4aa7d...3d9e` | `fbf8ecf1...8be1` | `92c9b262...570c` | `4466a7d0...70d7` | `03e388c8...ce3b` |
| shadow action DAG | `fcb229f0...88a5` | `2867b747...c331` | `b710ad54...7e6` | `8cf6b922...cf4d` | `a0d65850...719` |
| specification claim | `18fb8a48...b086` | `1de666c9...ae0` | `0a2b6067...0f04` | `0d2d692c...19e5` | `beb606e5...ffc` |
| seal | `70f5c603...6a29` | `71884532...a3c6` | `692bccf1...d1b` | `9dc3e583...47ad` | `fc940a1c...b987` |

In every column the specification gate moves `true -> false`, the independent
outcome index moves `12 -> 0`, and the rendered primary moves from the frozen
eligible cap to `P13-SPECIFICATION-INCONSISTENT`.  Each dependency result has
`all_required_movements=true`; the four result-file SHA-256 values are,
respectively,
`94cb4e88aaa4a892c09e5506613f6a0f50596cdf0a2ad9f0078a0d126cb34a86`,
`d8fe53f13ef899e185b775aff091cd85b5fe4ba8134a66acdab97f90be9c27ed`,
`057763a55a1498b8a0cd6a40e90aee04e3bdae8cd6fcb5cf07d38ebd2485de2c`,
and `d03736286036b95d9c2e922f6268a91539024f238ea51e9f00495cd185fbfa36`.

## Preserved scientific regression wall

The v3 delta does not retune the law or any exposed coordinate.  The exact
fixture-free reconstruction retains:

```text
R  = [[3/5,-4/5],[4/5,3/5]]
B  = [[9/25,16/25],[16/25,9/25]]
C  = [[49/625,576/625],[576/625,49/625]]
B2 = [[337/625,288/625],[288/625,337/625]]
K  = [[351/175,-176/175],[-176/175,351/175]]
```

The universal native nondivision bound remains `527/175`; the reciprocal
joint remains `{00:9/25,01:0,10:144/625,11:256/625}`.  The all-input writer,
six-letter continuation grammar, free-word record preservation, 16 alternate
cut comparisons, active inverse erasure, positive history-conditioned
control, global matching/resource parity, prior-record/blind-prefix equality,
and class-relative exclusion all remain exact.

The negative native factor says only that the cut admits no positive
source-independent stochastic restart on the declared configuration carrier.
A definite configuration may be actual there, and an enlarged history/phase
representation may Markovize the calculation.  Stable record divisions remain
relative to the declared typed continuation grammar.

## Ontology and outcome walls

The source continues to print and enforce:

```text
event_filling_selection = PRICED-KINEMATICS
division_doctrine       = TYPED-CANDIDATE-AND-GRAMMAR-RELATIVE
actualization           = POSTULATED
valuation               = UNCONSTRUCTED
metric                  = UNCONSTRUCTED
```

The construction is a candidate finite relational Gamma on covariant typed
presentations.  Passing development checks does not select `g`, a coupling,
catalogue, filling, division doctrine, or actual outcome.  It does not prove
absolute relational irreducibility, time, topology, dimension, signature,
continuum, metric, curvature, QFT, gravity, or GR.

## Artifact absence and next authorized event

The following paths are absent:

```text
v16/code/p13_gamma_fresh_cases_v3.json
v16/code/p13_gamma_output_v3.txt
v16/code/p13_gamma_receipt_v3.json
v16/note-paper13-typed-groupoid-verification-v3.md
v16/paper-13-one-relational-gamma-v3.md
v16/paper13_typed_groupoid_v3_code/
```

No v3 `.pyc` remains.  No nonce exists, no fresh case was generated, no
official/publication mode ran, no artifact was read, and no publication write
occurred.  The Stage-B changed paths are exactly this source, this note, and
the separately required `PLAN.md`, `LOG.md`, and `STATUS.md` bookkeeping.

The sole next scientific event is the two mutually blind Stage-C source
audits, followed by a separately committed adjudication.  Fresh generation,
Paper 13 publication, Paper 14 stable-happening work, and Paper 15 spacetime
work remain barred until the required earlier gates accept.

This note intentionally does not contain its own ordinary SHA-256.  That hash
is computed only after these bytes freeze and is then recorded in `LOG.md` and
`STATUS.md`.
