# Paper 13 Stage-C source audit — typed groupoid, operator/category seat

## 1. Disposition

| field | result |
|---|---|
| reviewer seat | operator/category source audit |
| frozen source | `v16/code/p13_gamma_exact_v2.py` |
| source SHA-256 | `b56383236a2aa0ff484aaa4c9082393beb4e4dd3ceb4d2724e4332bf68b6cba1` |
| disposition | **NO-GO** |
| earliest outcome rung | **`P13-REFERENT-PRESENTATION-ONLY`** |
| decisive finding | `A-SRC-1`: configuration transport accepts a target boundary that is not the witness image |
| integrity status | authenticated corpus; no integrity block |

Verdict in one sentence: the frozen finite-map algebra, category, totality wall,
and registered G1--G20 controls reconstruct, but the purported full groupoid
action is not typed at the configuration boundary because
`relabel_configuration` silently accepts an exact valid target boundary that
is not the image selected by the witness.

## 2. Identity, authorization, and blindness declaration

I performed the mutually blind operator/category Stage-C source audit.  I did
not read, list, request, infer, or communicate with any peer source-audit
report or auditor.  I did not import the evaluator or call its scientific
functions.  Candidate executions were subprocess-only black-box invocations
using `--selftest` or a registered development-mutant name.  Independent
reconstruction used separately written exact-arithmetic code in private
off-tree scratch.

I did not invoke `--generate-fresh` or `--run`, did not create or read any v2
fresh/output/receipt artifact, and did not stage or commit.  I edited no
repository path other than this report.  Candidate, pin, freeze note, planning
and status files, Git, and all other repository paths remained immutable.

The stop rule was obeyed.  Scientific work stopped immediately after the first
independently invented semantic counterexample was reproduced.  Operations
after that point were limited to hashing the already produced evidence,
checking the self-hash formatting convention in my own prior report, and
freezing this report.

## 3. Authentication and read ledger

Pre-science authentication at `2026-08-20T02:57:12Z` gave:

| object | authenticated value | use |
|---|---|---|
| HEAD | `2ee5fba54e7336e3aab80a401c976f8d2fbe670e` | required Stage-C source-audit HEAD |
| `v16/note-paper13-typed-groupoid-forward-repair-pin.md` | `08f7f64efca6210eee356852ad9e9b59487ea62a55aeaf85a483f6a70b85b004` | read completely before science; governing contract |
| `v16/code/p13_gamma_exact_v2.py` | `b56383236a2aa0ff484aaa4c9082393beb4e4dd3ceb4d2724e4332bf68b6cba1` | frozen source; inspected only after independent reconstruction |
| `v16/note-paper13-typed-groupoid-source-freeze.md` | `33ff983e6c9b8f4bab6aa98abfea18f0f27d609b572c7980e05e7e63e80e51f7` | read completely before science; frozen runner claims treated as claims to test |
| `v16/review-paper13-operator-category.md` | `1b4d566143837c8614bf4aa44469fe87061ce45055fe9aa9ca348057020dc702` | opened only after the kill, solely to reuse the already-authored normalized-self-hash convention |

The target report did not exist before this freeze.  Immediately before report
creation, HEAD and all three Stage-C anchors above were reauthenticated at the
same values.  No future v2 artifact was listed or opened.

## 4. Audit chronology and independent method

The independent reconstruction was completed and frozen before implementation
semantics were inspected:

| item | value |
|---|---|
| private script | `independent_groupoid.py` |
| script SHA-256 | `839df7ef2b8f3a0ec806ed2f918e81760d69b85b7765384769bdd8d7a3c0ea04` |
| RC / runtime | `0` / approximately `3.06 s` |
| stdout SHA-256 | `1342aafb6604b992ccc20a8655f923f9e74dd45d12f1e46a0740a5476d82bc5b` |
| canonical result SHA-256 | `be38f9bb35dfb8c1e9ca9a73865c5463d862a3c246d71c2d9508e34d5c1b0918` |
| candidate imported | `false` |

The script independently defined typed finite carriers, sparse completion,
canonical sparsification, source/target presentations, first-then-second
composition, inverse, identity, exact `Fraction` matrices, configuration
actions, tensor products, certificate lineage, and the Gamma covariance
square.  Its frozen result was `all_exact=true` and included:

- 34 total bijections at carrier sizes 0--4 and 14,050 composable permutation
  triples;
- shared-label sparse identity completion;
- both identities, both inverses, associativity, tensor action, full object
  action, operator naturality, endpoint-law naturality, certificate lineage,
  source sufficiency, and anti-wrapper checks;
- independent versions of G1--G20;
- 72 ambient Boolean representatives and 42 contextual classes;
- exact `R`, `B`, `C`, `B^2`, `K`, the `527/175` bound, category isometry,
  reciprocal joint, and the `12 / 312 / 468 / 156+156+156` census.

That independent model established what the contract requires; it did not
establish that every public implementation entry point enforces the same
typing.  The decisive discrepancy appeared only during the subsequent frozen
source trace.

## 5. Frozen black-box replay ledger

| run | location | RC | wall time | exact evidence |
|---|---|---:|---:|---|
| `python3 v16/code/p13_gamma_exact_v2.py --selftest` | repository root | 0 | `58.78 s` | stdout 113,764,060 bytes, SHA `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938`; stderr SHA `06f41b4b0a65f7a453258dd648b3d6f1351edff6b6eb89090a7cf49416bc2a4e` |
| same frozen source and mode | true source-only private tree with no `.git` | 0 | `65.00 s` | identical stdout SHA `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938`; stderr/time SHA `d17c6400162610406a78b5524c7d074f5694a86dbabb79c1bad3a11267327751` |
| all G1--G20 registered mutant modes | repository root, one subprocess per name | all 0 | `15.41 s` aggregate | harness SHA `5c90b27cc2b6eb08ef6f5ce002872fa63c82be638f1fd86206fa63cf62320898`; ledger SHA `b10647b0ca7b7a5f6fa0a40f26bc1c9b8a572e2594608dca93825a9e6027dd9d`; result SHA `b143c4ecbad5a896ab947d1904bfc5048f1dbf248da19a1376121265e89a8db1` |

Both selftests independently decoded as `PASS`, `46/46` checks, `112/112`
mutants, `fresh_cases_read=false`, `official_artifacts_read=false`, and
`publication_writes=0`.  Their normalized payload SHA-256 was
`2b7372afe4dd63b72ad8da0c58293e6f6b88128ebd7da495bfc44e950a31afbf`.
The off-tree source copy retained the exact frozen source SHA.  The G1--G20
runner independently recomputed every payload hash, evidence hash, and
old/new changed-object hash; all twenty old/new objects differed.

## 6. Completed implementation audit before the stop

| obligation | frozen-source trace and pre-kill result |
|---|---|
| complete `SourcePresentation` | Lines 4318--4452 walk literal Arrow source, target, structural objects, children, all catalogues, roles/types, matter, ports, formulas, and occurrence IDs; `__post_init__` recomputes and exactly equates all four canonical carriers.  No discrepancy found. |
| total sparse completion | Lines 4469--4516 reject malformed/duplicate/alien rows, complete only lawful identical target labels, enforce injection/surjection and role type preservation, then remove only identity rows.  No discrepancy found. |
| typed witness | Lines 4519--4570 retain literal source/target presentations and seal, canonicalize all four components, and require literal transported Arrow equality.  No discrepancy found. |
| full raw action | Lines 4589--4687 structurally relabel formulas, contexts, ports, boundaries, occurrences, identities, generators, compositions, tensors, symmetry, associators, and unitors.  Formula table order is correctly repaired by `Formula` canonicalization.  No discrepancy found in these branches. |
| identities/inverses/composition | Lines 4690--4814 derive targets, retain typed identity objects, invert completed maps, require literal middle-presentation equality, compose every source label first-then-second, and reconstruct a fully validated witness.  No discrepancy found. |
| abstract census | Lines 4860--4976 emit 34 bijections, shared sparse identities, and 14,050 triples.  Independent reconstruction agreed. |
| public object action | Formula, context, split proof, port, boundary, occurrence, and Arrow guards at lines 5021--5118 were consistent.  Configuration action at lines 5121--5145 failed the independent attack in Section 8. |
| operator/Gamma naturality | Lines 5148--5226 compare every source-by-target coordinate after transported bases, including implicit zero coefficients, and compare endpoint squares.  Internal lawful-target calls showed exact residual zero.  The universal transported-object action is nevertheless false because of `A-SRC-1`. |
| native census | Thirteen rows cover the minimal role map, each namespace, all four namespaces, contextual alias, CREATE/MERGE/UNCHANGED, record continuation, reciprocal probe, size-12 matching, and two-factor tensor.  All registered row predicates were exact before the kill. |
| certificate action | Lines 5652--5769 rebuild transported certificates and check proof/scalar transport plus identity, inverse roundtrip, and composition.  No pre-kill discrepancy found. |
| promotion consumer | Lines 5889--5934 consume native row fields rather than a copied top-level Boolean.  Registered G18 was killed. |
| source sufficiency | The full presentation key contains law identity, literal semantic endpoints, complete Arrow key, and source configuration.  Independent same-key/different-filling probes agreed before the kill. |
| anti-wrapper | Exact-type law reconstruction, recomputed operator/derivation equality, primitive-root counts, and shadow recomputation were present and independently reconstructed before the stop. |
| category and totality | Category identities, composition, associativity, tensor interchange, symmetry, associator inverse, unitors, and seven zero isometry residuals were exact.  Totality preserved 12 generators, 312 source columns, 468 bound transitions, and all rational-domain certificates. |

The table records only work completed before the first counterexample.  It is
not an attempt to promote later claims past the failed earlier rung.

## 7. G1--G20 registered attack audit

All registered attacks returned changed objects and the advertised baseline
disposition.  Full evidence hashes from the independent subprocess ledger are:

| ID | registered name | observed predicate | evidence SHA-256 |
|---:|---|---|---|
| G1 | `EMPTY-LEFT-IDENTITY` | exact `A->B` left identity and action | `b6a9e467e703c914d7013cdd727120d5cfbfe28d4c9e22243ff30ae02e14c411` |
| G2 | `EMPTY-RIGHT-IDENTITY` | right identity exact | `92b4e4bdab9f8621496552bdb2caa4d9e67a2e1058a3713e77f9bd6196fa2b43` |
| G3 | `INVERSE-LEFT` | first then inverse equals source identity | `1beae91789bc32f36d5261e7939f8b1cb92761e34afb713e6ce65ee248e65fbe` |
| G4 | `INVERSE-RIGHT` | inverse then first equals target identity | `3ca4e7fe80a6bbe045ab28cb1e6732ef8ec4d75b8123f423f9f494363e563f97` |
| G5 | `THREE-SPARSE-ASSOCIATIVITY` | parenthesizations and actions exact | `69dc3b05dd28a60b4b591ca929bc5d61f7a31be277e2bb7e94fd636619683e25` |
| G6 | `MIDDLE-PRESENTATION-MISMATCH` | equal-size alien middle refused | `eb0b0dd27b459b356eaa4168ae5dd7381143dcf92d667e2818d92cdff8f16ed9` |
| G7 | `SOURCE-LABEL-OMITTED` | nonidentity omission refused | `f3d078e4cd6c51326b0bb3d282ced65adea57f09444b7e0961c6605f4a67f6a5` |
| G8 | `EXTRA-TARGET-LABEL` | incomplete forged presentation refused | `38fee9037ef43af8267e4fc458ba2295139d3a4c42b14b586aa96ee6e1758748` |
| G9 | `MAP-COLLISION` | noninjective component refused | `98601f0717ebd47b7c3ac720f3df033f43e6ec2642f6c190d86634f4e54374a3` |
| G10 | `ROLE-TYPE-SWAP` | incompatible role type refused | `f0e51b2084278c0bf18929a035843b2d9117527fc06262bb1e5ce9b97c621e21` |
| G11 | `NAMESPACE-CROSSING` | role used as matter source refused | `e4866212fed53a39fb8d3335d0d6197960e2dc8b8b6cdc6025d98134bc38a517` |
| G12 | `TARGET-PRESENTATION-FORGERY` | altered query/filling refused | `056360230e36b1d3ec3480e1f10559939bb3135bf2058069bc388a5966f7e549` |
| G13 | `IDENTITY-ROW-ENCODING` | explicit/omitted identity canonical equality | `32ebecd00a103d3391491f7844b102b69a860e682ed6d902075c6cbc1919ec54` |
| G14 | `ORDER-REVERSAL` | reverse order changes transported formula | `dca364e5a90d404204cc64727c712d8e26ba471428d8f3b846885560619391c7` |
| G15 | `TRANSPORT-SEVER` | untransported query refused | `d3f9cd3dd26ec6eb7f0287847a8f03ae1e84db9b1f841975de3b119fb292b765` |
| G16 | `CERTIFICATE-TRANSPORT-CACHE` | cached certificate invalid; rebuilt final | `0cd783aaa81987ae3e69b608fe4ba8ff03d289a73c6eebb6542b5f2900ab7f26` |
| G17 | `COMPOSITE-OPERATOR-CACHE` | source key/operator changed; exact uncached covariance | `626bdab75508d4a7efbbc7f202b23afb0b9a8b1b3482958cb8869fe734203031` |
| G18 | `COPIED-GROUPOID-BOOLEAN` | native conjunction defeats copied final flag | `70f3b31f976ce15e79847114653dfb183018a629fbc17d931fc3b750045e8280` |
| G19 | `TENSOR-SHARED-LABEL-CONFLICT` | conflicting shared role type refused | `18f8668e7cb8576facf5e15130c0a76eca2e1ae6a7de33a9c8a6ff9e12c2a851` |
| G20 | `FRESH-GLOBAL-RELABEL-SEVER` | unmoved query/schedule refused | `e935ce8a8961231f9112024c2f38536cf58738457ce219c3a766f145eacee846` |

These twenty attacks do not cover the independently invented target-boundary
composability attack below.  In particular, G15 severs an occurrence query
while rebuilding an Arrow; it does not supply the configuration action with a
different exact target boundary whose catalogue happens to admit the same
assignment.

## 8. Decisive finding `A-SRC-1`

### 8.1 Contract violated

The pin requires one completed witness to exactly transport source and target
boundaries, configurations, and complete state catalogues.  For an identity
witness, the transported boundary must be the identical typed boundary.  An
input tuple whose supplied target is not `relabel_boundary(source,witness)` is
not composable and must be refused before an action result is returned.

### 8.2 Frozen implementation defect

The relevant frozen function is:

```python
def relabel_configuration(source_boundary, target_boundary, configuration, witness):
    _require_exact(witness, SourceGroupoidWitness, "configuration groupoid witness")
    validate_configuration(source_boundary, configuration)
    relabelled = configuration_from_assignments(
        target_boundary,
        {_rename(witness.matter_map, name): value for name, value in configuration.matter},
        {_rename(witness.port_map, name): value for name, value in configuration.sectors},
    )
    expected_context = relabel_context(configuration.context, witness)
    if context_semantic_key(relabelled.context) != context_semantic_key(expected_context):
        raise Refusal("configuration context failed groupoid transport")
    return relabelled
```

There is no check that:

```text
target_boundary == relabel_boundary(source_boundary, witness)
```

in exact boundary semantics.  There is also no direct requirement that the
configuration's matter and port names lie in the witness source carriers.
Because port mode is part of the typed boundary but not the generated
configuration context/catalogue, an `ACTIVE -> CARRIED` target substitution
passes the sole context comparison.

### 8.3 Exact counterexample

Using only native constructors already present in the registered mutant
harness:

1. Let `arrow = build_coherent_control("gmut_")["first_pair"]`.
2. Let `w = identity_witness(arrow)`.
3. Let `S = arrow.source`; its port `gmut_p` has mode `ACTIVE`.
4. Let `T = boundary_with_port_mode(S, "gmut_p", "CARRIED")`.
5. Let `q = S.catalogue[0]`, namely matter `gmut_c=0`, sector
   `gmut_p=empty`, with context role `gmut_L_record`.

All of `S`, `T`, `q`, and `w` are exact valid native objects.  The literal
witness image is `relabel_boundary(S,w)=S`, while `_same_boundary(T,S)=false`.
Thus `(S,T,q,w)` is an ill-typed action tuple and must be refused.

Observed result:

```text
source_boundary_is_literal_arrow_source = true
wrong_target_is_exact_valid_boundary    = true
wrong_target_port_mode                  = CARRIED
source_target_catalogue_cardinality_equal = true
supplied_target_is_witness_image        = false
refusal                                 = NO-REFUSAL
malformed_target_accepted               = true
```

The returned configuration was valid on `T` and retained
`gmut_c=0, gmut_p=empty`.  Returning a value is the failure: identity transport
has silently changed the typed boundary from `ACTIVE` to `CARRIED`.

### 8.4 Reproduction without evaluator import

I copied the authenticated source to private scratch and changed only the body
of the already registered `EMPTY-LEFT-IDENTITY` mutant branch so that it
constructed the tuple above and set `pass=caught_refusal`.  No function under
test, constructor, validator, action, operator, or promotion consumer was
changed.  The private copy was then run black-box as:

```text
python3 p13_gamma_exact_v2.py --mutant EMPTY-LEFT-IDENTITY
```

The deterministic unified harness diff has SHA-256
`bb67d19f7fdb3137da1d412cb0811948c50156a0b36ba0af93f3a0fbcc29562b`.
Its substantive replacement was:

```python
identity = identity_witness(arrow)
source_boundary = arrow.source
wrong_target = boundary_with_port_mode(
    source_boundary, source_boundary.ports[0].port.name, "CARRIED"
)
required_target = relabel_boundary(source_boundary, identity)
source_state = source_boundary.catalogue[0]
caught, error = _capture_refusal(
    lambda: relabel_configuration(
        source_boundary, wrong_target, source_state, identity
    )
)
accepted_configuration = (
    None if caught else relabel_configuration(
        source_boundary, wrong_target, source_state, identity
    )
)
passed = caught
```

| probe evidence | value |
|---|---|
| instrumented private source SHA-256 | `6e0789288e6c472756e4a82dd8847b31634d4b8da7aab15d33f8863523aa5897` |
| command RC / runtime | `0` / `0.22 s` |
| payload status / mutation status | `FAIL` / `SURVIVED` |
| normalized payload SHA-256 | `cc641b86440a39a7ab8236a45b7c0b4a4b2a9ddcca36d25b3174ac9d51def3a8` |
| independently recomputed evidence SHA-256 | `2dbc1e4dc52e265d0eeba731440021c759fd637c2feb291cb85296cfbc35f4c9` |
| stdout SHA-256 | `2c6beae4c82f83b351b42d0d6d919eee7867b18dcd1e4eff7779923ac796fd08` |
| stderr/time SHA-256 | `e4243fa30871f5db82c401285fcb4ead90cdfb7382eaa70c063a5f57c11b94c0` |
| old/new changed-object SHA-256 | `a56d687f47b4706a949f34c68f285ed4ddaf0eb054d49526a4050b946b210a70` / `46b126d51bfc7c726435164d4d50a19cebdce2da40d9257a9a07b956ccc2697d` |
| fresh/official reads; publication writes | `false`; `false`; `0` |
| emitted affected claim | `PRESENTATION-COVARIANCE` |
| emitted outcome drop | `P13-REFERENT-PRESENTATION-ONLY` |

RC 0 is the documented mutant-mode serialization behavior; the scientific
result is the payload's `FAIL`, mutation `SURVIVED`, and exact `NO-REFUSAL`
evidence.  I independently recomputed both the normalized payload hash and the
evidence hash from emitted bytes.

### 8.5 Why the passing selftest does not answer the counterexample

Every frozen covariance caller supplies the target obtained from
`relabel_arrow`, so the malformed composability edge is never exercised.  The
native catalogue checks that lawful calls have residual zero; it does not
establish that noncomposable target-boundary inputs are refused.  Exact
cardinality and exact configuration validity are insufficient because two
different port modes have the same state catalogue.  Consequently the frozen
`all_exact=true` rows are positive-path evidence, not a total typed-action
proof.

## 9. Preserved category/totality values before the kill

The following independently reconstructed values matched the frozen source.
They are preserved regression facts, not grounds to pass the failed referent
rung.

| surface | exact value |
|---|---|
| `R` | `[[3,-4],[4,3]]/5` |
| `B` | `[[9,16],[16,9]]/25` |
| `C` | `[[49,576],[576,49]]/625` |
| `B^2` | `[[337,288],[288,337]]/625` |
| `K` | `[[351,-176],[-176,351]]/175` |
| universal native bound | `527/175` |
| contextual Boolean census | `72` ambient / `42` contextual classes |
| totality census | `12` generator families / `312` source columns / `468` bound transitions |
| operation split | `156 CREATE / 156 MERGE / 156 UNCHANGED` |
| reciprocal joint `(00,01,10,11)` | `(9/25, 0, 144/625, 256/625)` |
| category | identity, both composition identities, composition associativity, tensor interchange, symmetry naturality/involution, associator inverse, unitors, and all seven isometry residuals exactly zero |
| rational totality | all generator isometries, rho involutions, Cayley norm identity, denominator `1+x^2 >= 1`, normalized domain endpoints, and bound nonzero transitions exact |

The root selftest advertised 13 native groupoid rows, 34 abstract bijections,
and 14,050 triples; all registered residuals were zero.  Those values are also
preserved, subject to the missing negative-domain guard exposed by `A-SRC-1`.

## 10. Finding, repair boundary, and outcome

**KILL `A-SRC-1` — nonimage configuration target accepted.**  The public
configuration action is not a total typed action of the source groupoid.  Even
the identity witness can return a configuration on a different typed boundary.
This defeats the universal full transported-object action and therefore the
referent/groupoid promotion.

**Required repair boundary.**  At minimum, configuration transport must derive
or exactly validate its target boundary from the witness before assignment
transport, and must validate matter/port carrier membership.  The repaired
negative case must cover exact valid same-cardinality boundaries with distinct
port modes, not merely malformed objects.  Because this changes scientific
source behavior, it requires a new source identity and a renewed source audit;
it is not an editorial fix.  I made no such source change.

**Earliest rung.**  The pin states that failure of a groupoid law/action caps
the outcome at `P13-REFERENT-PRESENTATION-ONLY`.  The lower specification rung
does not apply: HEAD and all frozen anchors authenticated, both selftests were
deterministic, and the defect is semantic rather than corpus-integrity failure.
Later category, totality, source-sufficiency, anti-wrapper, record, reciprocal,
nondivision, division, family, or ontology predicates cannot override this
earlier failure.

**Final disposition: NO-GO.**

## 11. Normalized self-hash

The ordinary SHA-256 is intentionally not embedded.  It is computed and
reported externally after this file freezes.

Normalization is UTF-8 with LF line endings and this one value replaced by 64
ASCII zeroes before SHA-256.

normalized_sha256: 64444496857f22868215e85c920f369b855b43dc2bc1a1e9a15cc92d8e4cf0b2
