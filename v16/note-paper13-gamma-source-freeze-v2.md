# Paper 13 Stage-A Gamma source freeze v2

Date: 2026-08-19

## Authority and scope

This note freezes the forward repair required by
`note-paper13-stageA-support-split-forward-repair-pin.md`, SHA-256
`8ae54ada2a97f347a18b90adcab86dcb2e7c18c04c748cc5e0779b8251449a36`.
The original result-neutral construction pin remains anchored at SHA-256
`4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35`.

The authenticated audit chain is:

| path | SHA-256 |
|---|---|
| `v16/note-paper13-gamma-source-freeze.md` | `d717f97832efe05996ae5f94249629376ddbe916fc837e0d5d16984bd7a13ad5` |
| `v16/review-paper13-stageA-source-physics.md` | `20a054cd6542fd02f556b461408f48d75ead0c69ec06abd76c9eed3ce3c3d352` |
| `v16/review-paper13-stageA-source-records.md` | `7c5b14a04f938de05b64750f6c8ae454eb4bbe8d0824e9eaaa0016532ab52ed4` |
| `v16/note-paper13-stageA-source-audit-adjudication.md` | `bd089458ef1d4c4fe8f9dc13fc21134695aba552b95b20f023e4d2f9f34dfb74` |

Those paths and the repair pin are authentication-only inputs. The superseded
Stage-A source is represented only by the cross-checked
`historical-unobserved` provenance record; it is not claimed as a live disk
anchor or scientific input.

## Frozen source

| property | value |
|---|---|
| path | `v16/code/p13_gamma_exact.py` |
| SHA-256 | `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e` |
| lines | `9913` |
| bytes | `389487` |
| AST parse | `PASS` |
| float AST nodes | `0` |
| forbidden imports | `0` |
| private Paper-13 exploratory-path mentions | `0` |
| `apr_fixtures` imports | `0` |
| `load_frozen_fixture` mentions | `0` |
| support-promotion AST SHA-256 | `1f40e18056b38afe19390885994627220fd8bbca485bad8fdcbde39e898cfc25` |
| support predicate required certificate keys present | `true` |
| legacy role/cell keys absent from support predicate | `true` |

A pre-freeze replay exposed one equal-key ordering tie inside the deliberately
malformed `TRANSPORT-SPLIT-SEVER` evidence. The source was minimally repaired
to order split-proof cells by `(typed bit key, literal cell)`; every earlier
freeze/replay observation was discarded. All evidence below was regenerated
from the SHA-256 above.

## Exact split construction

`ContextSplitProof` is a pure immutable context-level proof used for the
72-ambient/42-contextual census. It is diagnostic and never promotive.
`BoundSplitCertificate` is a distinct immutable type with non-optional law,
source, Arrow, occurrence, port, input/output bit, sector, literal target,
operation, inverse, classifier-consumed, and embedded context-proof fields.
Only the latter enters support, variable-carrier, gate, lineage, claim, and
seal promotion. Passing a `ContextSplitProof`, supplied Boolean, wrong port,
wrong branch, or swapped target as a bound certificate is refused.

The frozen selftest reports:

- ambient nonzero representatives: `72`;
- contextual Boolean classes: `42`;
- ambient replays: `72`;
- generator families: `12`;
- declared source columns checked: `312`;
- nonzero transitions with bound certificates: `468`;
- representative bound transitions: `12`, split as `CREATE=4`, `MERGE=4`,
  `UNCHANGED=4`;
- public exact node types visited: `20/20`;
- context proof alone promotive: `false`;
- legacy role/cell inequality promotive: `false`.

Within each contextual class, the physical source key, Arrow identity, target,
operator, endpoint law, classifier lineage, and certificate are invariant.
In particular the C3 parents `B` and `A and B` have different ambient syntax
hashes but identical contextual physical data.

## Development selftest freeze

Only fixture-free `--selftest` and registered development-mutant paths ran.
Neither `--generate-fresh` nor official `--run` ran.

| property | value |
|---|---|
| status | `PASS` |
| checks | `42/42` |
| registered attacks killed | `92/92` |
| mutation-registry SHA-256 | `7f60ecd06c85c4b4a3eb18ceb7b86470201904cfcd27c7f9c14392c58ea54aeb` |
| normalized payload SHA-256 | `0894a736dd27ac2be619c0c4e9f24e79ac897b1d8675e2176096df40e7d307fa` |
| exact stdout SHA-256 | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1` |
| exact stdout bytes | `27380971` |
| repair disposition | `REPAIR-GREEN-UNREVIEWED` |
| `scientific_fixture_evaluated` | `false` |
| fresh cases read | `false` |
| official artifacts read | `false` |
| publication writes | `0` |

The 42 checks, in output order, are:

```text
AST-AND-STATIC-SOURCE-CLEAN
FRACTION-ONLY-SCIENTIFIC-COORDINATES
ESSENTIAL-SUPPORT-BOOLEAN-QUOTIENT
CONTEXT-SPLIT-CENSUS-72-AMBIENT-42-CONTEXTUAL
CONTEXTUAL-BOOLEAN-ALIAS-PHYSICAL-IDENTITY
PUBLIC-PRIMITIVE-LANGUAGE-CLOSED
FOUR-PRIMITIVE-LEGS-ON-FULL-TYPED-CHAIN
ZERO-AMPLITUDE-TARGETS-RETAINED
COHERENT-R-B-C-EXACT
CATEGORY-IDENTITY-COMPOSE-TENSOR-SYMMETRY
TOTAL-NORMALIZED-PRIMITIVE-DOMAIN
COMPLETE-SOURCE-KEY-SUFFICIENCY
NEUTRAL-PRESENTATION-INVARIANCE
SOURCE-GROUPOID-COVARIANCE
BOUND-SPLIT-GROUPOID-IDENTITY-INVERSE-COMPOSITION
ONE-PRIMITIVE-ROOT-LINEAGE
ACTIVE-SUPPORT-CHANGE-AND-INVERSE-MERGE
BOUND-SPLIT-CREATE-MERGE-UNCHANGED-EXHAUSTIVE
RECIPROCAL-SAME-LAW-READER
WRITER-ALL-INPUT-NORMALIZATION
ACTIVE-TO-CARRIED-GENERATOR-INTERTWINING
ALL-WORD-CONTINUATION-RECOVERY
ALTERNATE-RECORD-CUT-EXACT
REACTIVATED-CARRIED-PORT-ERASES-RECORD
NATIVE-NONDIVISION-NEGATIVE-FACTOR
RATIONAL-INTERVAL-CERTIFICATE
HISTORY-CONDITIONED-POSITIVE-CONTROL
BLIND-RESOURCE-PARITY-AND-INDUCTION
SAME-ROOT-MATCHING-RESPONSE-SEPARATION
EXACT-SCOPE-COORDINATES-AND-WALLS
ORDERED-MEASUREMENT-PROGRAMME
RESULT-NEUTRAL-SCIENTIFIC-REGRESSION-WALL
OUTCOME-LADDER-CAP-AND-INDEPENDENT-COMPARATOR
MUTANT-REGISTRY-UNIQUE-AND-COMPLETE
ALL-REGISTERED-MUTATIONS-KILLED
S1-THROUGH-S11-SPLIT-ATTACKS-KILLED
SYNTHETIC-ANCHOR-CORRUPTION-IS-INTEGRITY-ONLY
STRICT-CLI-FORMS-AND-REFUSALS
READ-LEDGER-ORDER-AND-ANCHOR-BINDING
SEAL-MANIFEST-TOTALITY-RECOMPUTED
STAGE-WHITELIST-EXACT
FIXTURE-AND-OFFICIAL-ARTIFACT-SEPARATION
```

The newly registered split attacks are exactly `TAUTOLOGICAL-CHILD`,
`COEXTENSIVE-CHILD-OBJECT`, `FORGET-ONLY`, `CELL-COUNT-PADDING`,
`ROLE-COUNT-ONLY`, `TRANSPORT-SPLIT-SEVER`, `SUPPLIED-SPLIT-BOOLEAN`,
`CERTIFICATE-PORT-SWAP`, `OLD-CHILD-REUSE`, `AMBIENT-TARGET-PADDING`, and
`CONTEXTUAL-BOOLEAN-ALIAS`.

## Repository, alien-CWD, and source-only replay

After the final canonical-order repair, three fresh executions used identical
source bytes:

| execution | runtime | stdout SHA-256 | payload SHA-256 | result |
|---|---:|---|---|---|
| repository root | `29.52 s` | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1` | `0894a736dd27ac2be619c0c4e9f24e79ac897b1d8675e2176096df40e7d307fa` | `42/42`, `92/92` |
| alien CWD, absolute repository source | `30.93 s` | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1` | `0894a736dd27ac2be619c0c4e9f24e79ac897b1d8675e2176096df40e7d307fa` | `42/42`, `92/92` |
| true source-only off-tree tree, no `.git` | `30.02 s` | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1` | `0894a736dd27ac2be619c0c4e9f24e79ac897b1d8675e2176096df40e7d307fa` | `42/42`, `92/92` |

The three stdout objects are byte-identical.

## Post-freeze real source mutations

Both mutations started from the frozen source SHA-256
`3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e`,
used independent source-only off-tree trees with no `.git`, and did not alter
the repository source.

### S1 `TAUTOLOGICAL-CHILD`

The exact source patch replaced retention-plus-child with replacement:

```diff
     for cell in context.cells:
-        cells.append(cell)
         if formula_evaluate(parent, cell):
             cells.append(tuple(sorted(cell + (child.name,))))
+        else:
+            cells.append(cell)
```

- mutant source SHA-256:
  `edb8e4900ab77f61c264348080d18140d918489d2653e173059bc2e88babb2c7`;
- selftest exit: `1`, runtime `18.43 s`;
- stdout: empty, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- program-error-line SHA-256:
  `afe0fe4e57549ae4cb72aca8443638c5d0ddb4c12b88f378323512e3eb4f6439`;
- combined stderr plus timing SHA-256:
  `2c01a2e1ed6fd420f0c8f9e32245cbf8ffab0776d83bd92738c9f7444190aab3`;
- failure: `claim falsifier does not change its object`, so no stale claim
  Boolean could be promoted.

The serialized certificate probe, SHA-256
`a4a835343ff1208e93615168f9b2ea85e259c37fa73515d1102893914633286f`,
recomputed both `CREATE` branches. Each has bound-certificate and embedded
context-proof `final=false`, count residual `-1`, expected satisfying-fiber
bits `{0,1}`, observed bits `{1}`, `P and child=true`,
`P and not child=false`, exact forgetting `true`, and target exhaustiveness
`true`. The support and variable-carrier gates both fall to `false`; the
independent outcome index moves from `12` to `0`, rendering
`P13-SPECIFICATION-INCONSISTENT`, which is no higher than the required
`P13-SUPPORT-CHANGE-UNPROVEN` ceiling.

The dependency probe, SHA-256
`3867e424a9196ded7270d1fdf04e0a65db82dd771ade43b5a95c851fb17a22d9`,
records these exact movements:

| object | frozen | S1 mutant |
|---|---|---|
| support measurement | `cad779bb03daa221ea9b20d5811898a4f390b8015247e965f856a8845760a13d` | `341e6f302f476c93aba6621bf44e27279a6c9b9ab5a25015784c67d93d472d4a` |
| operator lineage | `233cbea8b576694f19c4012e64be47ba35275671d41ba2c74563bd5defc5d9ba` | `b3394c3188de74152d8762132790e25e80698d242b02981531841b31485dde32` |
| shadow lineages | `e645bd2c368463b37aa18861f04efbe002c89893cec84eef55d080e2da46ba70` | `54f26dd8c7959660bd362b0846a4b361ed194cbf5eb57cb83e3b378877779e77` |
| support-claim input DAG | `c3a11e65edeefd5b987ed5c06ebba5d178b008946182dd629372db9bf8b97b56` | `9db696f58c74d34526a79ba08e85d2c4f8dfc102400c54e3d89065f7a3103075` |
| receipt dependency slice | `d0edc72ee67268c544624a2b5a21af11d0597e7815e0dc8f90a6747f6d89bd0a` | `42dec414b0dc6747ec9c55281f1a584190a8e510790ea85226f51b21082426ee` |

### S5 `ROLE-COUNT-ONLY`

The exact source patch replaced the certificate predicate with the legacy
pair inequality:

```diff
-    return (
-        support["all_inverse_merge"]
-        and support["all_support_changed"]
-        and support["all_create_certificates_exact"]
-        and support["all_merge_certificates_exact"]
-        and support["all_unchanged_certificates_exact"]
-        and support["all_bound_certificates_exact"]
-        and not support["context_proof_alone_is_promotive"]
-        and not support["legacy_role_cell_inequality_is_promotive"]
-        and split_groupoid["all_exact"]
+    return all(
+        (branch["source_role_count"], branch["source_cell_count"])
+        != (branch["target_role_count"], branch["target_cell_count"])
+        for branch in support["branches"]
     )
```

- mutant source SHA-256:
  `a2edbbb51bcd80c5e4189dffcd0c04d7863ea6b9deeb9ec9b1abab224fa123f3`;
- selftest exit: `1`, runtime `28.29 s`;
- stdout: empty, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- program-error-line SHA-256:
  `79042f714800e9e8391701f3b477bec9e3740c4edbe3b3acb6ffc4faf1d7a7e6`;
- combined stderr plus timing SHA-256:
  `6e0ce23bcde9c8cd32668f554baea248ff97fb47f5ee78e31521c008dc09430d`;
- failed checks: `RESULT-NEUTRAL-SCIENTIFIC-REGRESSION-WALL` and
  `OUTCOME-LADDER-CAP-AND-INDEPENDENT-COMPARATOR`.

The source-mutation probe, SHA-256
`09628ea3f489dfd3aa5cd59a7ca5c988e0ea7d8c2fb3f6b7d8c6dfba2f43ac6d`,
records support-promotion AST SHA-256 changing from
`1f40e18056b38afe19390885994627220fd8bbca485bad8fdcbde39e898cfc25`
to `ef7fc3603fcd65de8c435ca9c929739f829c786c0231387ea91f9014e0f78372`,
required certificate keys becoming absent, legacy role/cell keys becoming
present, the specification gate falling `true -> false`, outcome index moving
`12 -> 0`, and the selftest seal manifest changing
`b760739656b1e8735120861399e66579f82824145cfd6cd95d1a030f0ec3fa5c`
to `d6f1122f6e0d1d5beb20eb24999b6f4987d349c7bdf0efd07afa8533ba5a03b8`.
The predicate-only source mutation does not alter the still-native certificate,
so its operator-lineage and support-claim hashes correctly remain unchanged;
the source/gate/seal path nevertheless invalidates promotion.

Separately, the registered `ROLE-COUNT-ONLY` certificate-object attack is
`KILLED` and proves every downstream certificate consumer moves rather than
copying a final Boolean:

| object | native | dropped/replaced certificate |
|---|---|---|
| measurement | `3e509c3f9248ed7d68e887340351a49a588c8d239f6fa680ac9bba9dfc54630d` | `03443964ab8a2ea305095b61238ea462bbeccd3f60794579feac7c4c242819a1` |
| lineage | `fc4e7f3f85d000232631b8b3c87f15356cd0a1f511e7474e63c5bee99a7766d1` | `8b8583e281d995d653224953f5714c3a4455809fb77bdc55376e4836c6dedad4` |
| claim row | `236248e6af65164cb78bde12b99acdf7701fb9efd09f1aca7efdc2e85654711b` | `256fbe0a0a8ef9f065a5cf1f8adaf672f515625f41667e81f51e742c804efcdc` |
| seal | `eabcd1139cc65b1187a4d5f4d5a83d8f1a16d094e0817ece6cea07f08b030c2a` | `bc8625e181a875a6f6f334f6e20fbbf4e0d59d752a3717dfeedceba2a9dbb292` |

Its exact rendered drop is `P13-SUPPORT-CHANGE-UNPROVEN`.

## Result-neutral regression wall

The rational domain, single contact-Cayley primitive, Born clause, exact
`R/B/C/B2/K`, `527/175` certificate, reciprocal joint, native nondivision and
history controls, continuation grammar, writer/cut/eraser controls, matching
resources, blind projection, source groupoid, strict CLI, transactionality,
receipt schema, outcome ladder, eligible cap, and scope walls all recompute
exactly. The pre-existing strict primary remains
`P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED`; the forward repair
adds no scientific award. `REPAIR-GREEN-UNREVIEWED` means only that these bytes
are eligible for independent post-freeze audit.

## Artifact absence and delivery boundary

The following paths were absent after every development execution and at this
freeze:

```text
v16/code/p13_gamma_fresh_cases.json
v16/code/p13_gamma_output.txt
v16/code/p13_gamma_receipt.json
v16/note-paper13-gamma-verification.md
v16/paper-13-one-relational-gamma.md
v16/paper13_code/run_all.py
v16/paper13_code/manifest.json
v16/paper13_code/receipts_table.json
v16/paper13_code/RUN.txt
```

The Stage-A task whitelist is exactly this frozen source and this v2 note.
Those are the only changed paths. This note intentionally does not contain its
own ordinary SHA-256; that hash is computed only after these note bytes freeze.
