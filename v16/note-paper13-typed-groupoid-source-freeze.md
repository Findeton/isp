# Paper 13 typed-groupoid source freeze

Date: 2026-08-19

## Authority and bounded purpose

This note freezes the source-only forward repair authorized by
`v16/note-paper13-typed-groupoid-forward-repair-pin.md`, SHA-256
`08f7f64efca6210eee356852ad9e9b59487ea62a55aeaf85a483f6a70b85b004`.
The pin was committed at
`e8e48184b8833284ce4b0db195a05a9a645d0100` after the hostile-panel
adjudication at commit
`7368c13e4d38f63a92f69694d7d0ed195f221123`.

The repair question is deliberately narrow:

> Can every sparse presentation witness be made into a typed arrow
> `w:X->Y`, completed to a total finite bijection before identity, inverse,
> composition, transport, naturality, certificate, and Gamma claims are
> evaluated?

These bytes answer only the source-implementability question.  They do not
regenerate fresh cases, official artifacts, the paper, or its bundle; they do
not overturn the hostile verdict; and they do not pre-award any scientific
outcome.  Their disposition is `REPAIR-GREEN-UNREVIEWED` until two independent
post-freeze source audits and a separate adjudication accept them.

## Immutable authority and exposed history

| object | path / identity | SHA-256 |
|---|---|---|
| hostile adjudication | `v16/note-paper13-hostile-review-adjudication.md` | `9546729fce24ce8a4a08239c881814b9526232a33151324c1b2e98b9daa61e49` |
| decisive Seat A report | `v16/review-paper13-operator-category.md` | `1b4d566143837c8614bf4aa44469fe87061ce45055fe9aa9ca348057020dc702` |
| Seat I report | `v16/review-paper13-indivisibility-records.md` | `8153eda3ff440712d30483dfa12b6c20e7109d91a2785b1577f3374ebe1fd636` |
| Seat R report | `v16/review-paper13-relational-ontology.md` | `340a7b7c2e5a24526486244106eb3ec8ba5de485cc585769ad7ca9c878efb314` |
| forward-repair pin | `v16/note-paper13-typed-groupoid-forward-repair-pin.md` | `08f7f64efca6210eee356852ad9e9b59487ea62a55aeaf85a483f6a70b85b004` |
| old rejected evaluator | `v16/code/p13_gamma_exact.py` | `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e` |

The old evaluator and every old fresh case, output, receipt, paper, review,
and exact `e=()` / `w=(A->B)` counterexample are exposed historical inputs.
The old source was not edited, imported, or promoted.  The repair uses a new
versioned source and new versioned future artifact paths.

## Frozen source

| property | value |
|---|---|
| path | `v16/code/p13_gamma_exact_v2.py` |
| SHA-256 | `b56383236a2aa0ff484aaa4c9082393beb4e4dd3ceb4d2724e4332bf68b6cba1` |
| lines | `11790` |
| bytes | `464013` |
| AST parse | `PASS` |
| float AST nodes | `0` |
| forbidden imports | `0` |
| private Paper-13 exploratory imports | `0` |
| fixture imports | `0` |
| support-promotion AST SHA-256 | `1f40e18056b38afe19390885994627220fd8bbca485bad8fdcbde39e898cfc25` |
| groupoid-promotion AST SHA-256 | `b8c1d3b48021bf03f7df2b5684ad49783e6571764ecabaf3d887b9b1f19c2f25` |

The source is frozen at the hash above.  No source edit occurred after the
root, alien-CWD, true off-tree, G1, and G18 evidence below.

## Closed typed presentation language

`SourcePresentation` is immutable, frozen, and slotted.  It contains the full
Arrow and its complete typed role, matter, port, and occurrence carriers.  It
recomputes those carriers from the complete source and derived target
boundaries, every realized context, every port parent and child, every query,
the ordered filling AST, and coefficient-zero-inclusive target catalogues.
Hashes are provenance only; the literal typed presentation is the source and
target datum.

`SourceGroupoidWitness` is an immutable typed arrow

```text
w : X -> Y
```

with exact `source`, exact `target`, and sparse maps in four disjoint
namespaces.  Validation completes each sparse map on every source label.  An
omitted row means `x->x` only when the same typed label occurs in the target.
The completion must be total, injective, surjective, type-preserving, and
namespace-preserving.  Transporting the complete literal source Arrow must
produce the complete literal target Arrow exactly.

Explicit identity rows canonicalize away.  Therefore an empty map remains a
lawful compact encoding of `id_X:X->X`, but an empty untyped tuple is not a
physical witness.

## Identity, inverse, and composition

The repaired implementation defines:

```text
id_X          : X -> X
w^-1          : Y -> X
compose(w, v) : X -> Z, only when w.target == v.source
```

Composition uses the first-then-second convention and evaluates every source
label in every namespace:

```text
(v o w)(x) = v(w(x)).
```

It does not iterate only the explicit rows of either sparse operand.  The
total result is checked as a typed bijection `X->Z`, checked to transport the
complete presentation, and only then sparsified.

The source establishes extensionally and by canonical typed equality:

```text
w o id_X       = w
id_Y o w       = w
w^-1 o w       = id_X
w o w^-1       = id_Y
u o (v o w)    = (u o v) o w.
```

## Transported physical structure

The same completed witness transports and revalidates:

- contextual Boolean formulas and truth-vector identities;
- contexts and split/merge fibers;
- ports, declarations, source and target boundaries;
- configurations and complete state catalogues;
- occurrences and complete Arrow/filling ASTs;
- source-presentation and provenance keys;
- `BoundSplitCertificate` objects and classifier-consumed hashes;
- primitive linear maps and complete class operators;
- Gamma endpoint laws;
- record projectors and sectors;
- division, reciprocal, matching-family, and tensor rows.

Operator and endpoint covariance are recomputed from the transported source,
not copied from the untransported row.  The promotion gate calls
`groupoid_promotion_predicate` over the explicit native law rows; it never
consumes a supplied or cached `groupoid["all_exact"]` Boolean.

## Exhaustive and native positive census

The abstract one-namespace census exhausts carrier sizes `0,1,2,3,4`.  It
contains all `34` bijections and all `14050` composable permutation triples.
Both identities, both inverses, roundtrip canonical equality, application
order, and associativity are exact for every row.

The native census contains `13` complete-presentation rows:

1. the exact minimal role relabeling `A->B` from the hostile counterexample;
2. a matter-only relabeling;
3. a port-only relabeling;
4. an occurrence-only relabeling;
5. one witness moving all four namespaces;
6. one contextual Boolean alias;
7. CREATE, MERGE, and UNCHANGED certificate rows;
8. a record writer/continuation row;
9. a reciprocal writer/probe row;
10. one size-twelve global matching row;
11. one two-factor tensor row.

Every native row checks both identities, both inverses, composition,
three-map associativity, source/target typing, source-configuration action,
formula/context/port/boundary/occurrence/Arrow action, complete-target action,
projector-sector action, split-certificate transport, nomological roots,
direct class-operator covariance, and endpoint-law covariance.

The size-twelve row uses the complete 24-role global context but a fixed
two-query subset.  That retains the required genuinely global presentation
transport while keeping a complete development selftest below the 300-second
cap.  It does not replace the future post-freeze global-law confirmation.

## Development selftest freeze

Only fixture-free `--selftest` and registered development-mutant paths ran.
Neither `--generate-fresh` nor official `--run` ran.

| property | value |
|---|---|
| status | `PASS` |
| checks | `46/46` |
| registered attacks killed | `112/112` |
| mutation-registry SHA-256 | `3397140b241465181b73434a6798f971492801aff2a38b1488a4109544ddbee6` |
| normalized payload SHA-256 | `2b7372afe4dd63b72ad8da0c58293e6f6b88128ebd7da495bfc44e950a31afbf` |
| exact stdout SHA-256 | `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938` |
| exact stdout bytes | `113764060` |
| repair disposition | `REPAIR-GREEN-UNREVIEWED` |
| scientific fixture evaluated | `false` |
| fresh cases read | `false` |
| official artifacts read | `false` |
| publication writes | `0` |

The four added top-level checks are:

```text
TYPED-GROUPOID-PROMOTION-CONSUMES-NATIVE-LAW-ROWS
SOURCE-GROUPOID-TOTAL-BIJECTION-LAWS
SOURCE-GROUPOID-ABSTRACT-AND-NATIVE-CENSUS
G1-THROUGH-G20-TYPED-GROUPOID-ATTACKS-KILLED
```

The source also separates previously colliding reflection and old-port
changed objects; `DISTINCT-REFLECTION-AND-OLD-PORT-CHANGED-OBJECTS` is exact.

## Mandatory G1--G20 attacks

All prior `92` attacks remain registered and killed.  The following `20`
typed-groupoid attacks are additionally registered and killed:

```text
EMPTY-LEFT-IDENTITY
EMPTY-RIGHT-IDENTITY
INVERSE-LEFT
INVERSE-RIGHT
THREE-SPARSE-ASSOCIATIVITY
MIDDLE-PRESENTATION-MISMATCH
SOURCE-LABEL-OMITTED
EXTRA-TARGET-LABEL
MAP-COLLISION
ROLE-TYPE-SWAP
NAMESPACE-CROSSING
TARGET-PRESENTATION-FORGERY
IDENTITY-ROW-ENCODING
ORDER-REVERSAL
TRANSPORT-SEVER
CERTIFICATE-TRANSPORT-CACHE
COMPOSITE-OPERATOR-CACHE
COPIED-GROUPOID-BOOLEAN
TENSOR-SHARED-LABEL-CONFLICT
FRESH-GLOBAL-RELABEL-SEVER
```

No row passes because its identifier is recognized.  Each registered row
contains distinct old/new object hashes, a changed object or explicit typed
refusal, the independently consumed predicate, and its dependency evidence.

## Root, alien-CWD, and true source-only replay

Three executions used identical source bytes:

| execution | runtime | stdout SHA-256 | payload SHA-256 | result |
|---|---:|---|---|---|
| repository root | `53.877 s` | `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938` | `2b7372afe4dd63b72ad8da0c58293e6f6b88128ebd7da495bfc44e950a31afbf` | `46/46`, `112/112` |
| alien CWD, absolute repository source | `62.846 s` | `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938` | `2b7372afe4dd63b72ad8da0c58293e6f6b88128ebd7da495bfc44e950a31afbf` | `46/46`, `112/112` |
| true source-only off-tree tree, no `.git` | `63.046 s` | `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938` | `2b7372afe4dd63b72ad8da0c58293e6f6b88128ebd7da495bfc44e950a31afbf` | `46/46`, `112/112` |

The three stdout objects are byte-identical.  The source-only tree contained
no `.git`, `__pycache__`, or `.pyc`.  No v2 bytecode cache remains in the
repository.

## Post-freeze G1 real source mutation

The G1 source-only mutation replaces total-source composition with the old
explicit-left-row-only loop that caused the hostile counterexample.

| property | value |
|---|---|
| mutant path | `/private/tmp/p13_gamma_exact_v2_g1.py` |
| mutant SHA-256 | `d4875c5c2f8cd62f4c0d3b2b8c437fc50e6fa6462137ece91386898d7808860a` |
| selftest exit | `2` |
| runtime | `1.375 s` |
| stdout SHA-256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| stderr SHA-256 | `b1a124423772a85c1f6157eaa9be07ae0a3f25140af03e86e35b6fae23dfa2cc` |
| refusal | `groupoid role map omits a nonidentity source` |

The independent semantic probe is
`/private/tmp/p13_g1_probe.py`, SHA-256
`3df64d5319a950ec87f0a9919ae40e88d5db2f886709c6e22a899cd85ef18c0e`.
Its stdout SHA-256 is
`163484e3b10f6dde7900671f9acc9725cb241290187b688242d7de69ed8382a4` and
its normalized payload SHA-256 is
`12dfca5d3e4e3957c00d55eeaeee342e22ee14f904677ee5e098c32add445e34`.

For `id_X` followed by `w:A->B`, the correct total composition is `[A->B]`;
the old loop produces `[A->A]`, with residual `1`.  The probe recomputes:

| object | frozen source | G1 mutant |
|---|---|---|
| measurement | `58ebdd24b46c5f5167167118293cc97f89d5e2fc05efb30c1bed46d187f38427` | `1f4af345d60c25c06f60df1b77990419c1017e289d0084dc5c415e6e6cd45350` |
| lineage | `b64671821197ad3e2c37a67a8b588fd84ce6b70578752a1e82cc7ec6cd2b5536` | `83a6383443c3eef9099d1f41d23f40e14b106246d7e99474ef0e10c99103f215` |
| claim | `73b5d0a0a51eed9bbaeea9f723dfbcfe8f12271019185ab7f3858e597d40cea0` | `fe4918aa98bac8206b930c273def48987717e53f2a1a877e2ce1fe43800c60b9` |
| seal | `c20aa99153a2b45043f8526cc695f7da26ac79dc9b636ff7e3de21d718a8f8b9` | `cf03ed80dd28f8419b1bb699367aa42324c5163ba48f8bc6ad22f779abb6f47a` |

The groupoid gate falls `true -> false`, the independent outcome index moves
`12 -> 1`, and the earliest rendered rung is
`P13-REFERENT-PRESENTATION-ONLY`.  Thus the exact hostile counterexample is a
semantic kill, not merely a crash.

## Post-freeze G18 real source mutation

The G18 source-only mutation replaces the native-law conjunction at the
promotion door with `return groupoid["all_exact"]`.

| property | value |
|---|---|
| mutant path | `/private/tmp/p13_gamma_exact_v2_g18.py` |
| mutant SHA-256 | `fc3967b58ff07286c45822b33a0ed07bf8c322944f2a813555774696ea7200d8` |
| selftest exit | `1` |
| runtime | `53.2 s` |
| stdout SHA-256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| stderr SHA-256 | `97b043e7804e5932c18068293f014eb61d42fbc7adc14f14b611818ec0c4db1c` |
| failed integrity surface | `seal manifest coverage is incomplete` |

The independent semantic probe is
`/private/tmp/p13_g18_probe.py`, SHA-256
`3de6de5681562cbed63eb781ca1cb175888982faba495d9affe4d6e82f0db932`.
Its stdout SHA-256 is
`f6c3654ca142028ba2e9f1d876f24deecf386e656531fa4e11f4fb81dc5d84a6`
and its normalized payload SHA-256 is
`16c2d2131649903be6c3b843501c7a4e646e13a1c65a44dc83b3efc7c25e2be0`.

With a copied aggregate Boolean held `true` while native left identity is
false, the frozen predicate is `false`, the mutant predicate is `true`, the
registered attack fails, the groupoid-promotion AST check falls, the
specification gate falls `true -> false`, outcome index moves `12 -> 0`, and
the rendered rung is `P13-SPECIFICATION-INCONSISTENT`.

| object | frozen source | G18 mutant |
|---|---|---|
| measurement | `c55d180ce0dc775661c2ba22a0a4f8e43340cc2abe846bed241c39f1de02587f` | `fac1c9080d16ae0854716e8c86a85f193408457976029bd35667b33f539d8a36` |
| claim | `1147bf313268f0d1f374f68dd74e7084114fd277e025fc1a55380589335600f6` | `1a0ba047d3c7530f5dfdfdbccdb27b1bd707ace30ef1d93158e433e2abf1a7c7` |
| seal | `077b12f452d87205ba7cb90b6fd7fcbdbce1abbc99e71e943d27d1e8415360cf` | `fddcd56de2b72071b03d7b90c9cbad2ec40e28cdf98fdc1423af0e4f659220df` |

The native dependency SHA-256 remains
`5d3350cd78d638c01e48ccaecc26cf0195b17e9f0c927055d04aafa051789fbd`,
as it should: G18 changes the promotion consumer rather than the native law
rows.  The probe nevertheless proves that the copied-Boolean bypass is
scientifically and procedurally fatal.

## Preserved scientific regression wall

The forward repair does not retune the physical candidate.  The following
recompute exactly:

- `72` ambient Boolean representatives, `42` contextual classes, and all
  `72` replays;
- `12` generator families, `312` source columns, `468` bound nonzero
  transitions, split `156/156/156` across CREATE/MERGE/UNCHANGED;
- representative support operations `CREATE=4`, `MERGE=4`,
  `UNCHANGED=4`;
- exact `R`, `B`, coherent `C`, recorded `B2`, native factor `K`, and the
  `527/175` rational-interval certificate;
- the positive history-conditioned control and the strict statement that the
  native cut is not a lawful stochastic division on the declared carrier;
- the all-input writer, grammar-relative division, alternate-cut equality,
  carried-record continuation, and active-reuse eraser;
- the reciprocal matter-to-relation-to-matter joint and opposite-incidence
  zero row;
- matching-family resource parity, one-root global response, and the
  incidence-blind transducer theorem;
- exact scope coordinates, outcome ladder, eligible cap, strict CLI,
  transactionality, read order, seals, and publication whitelists.

The physical interpretation remains unchanged.  A definite configuration
may be actual at the native nondivision cut; the negative factor excludes an
autonomous positive source-independent restart there, not ontological
completeness and not history/phase Markovization.  Division remains relative
to the frozen continuation grammar.  The relational result remains relative
to the frozen incidence-blind adversary class.  Event/filling selection,
catalogue selection, `g`, the Born clause, division doctrine, and
actualization remain priced or postulated.

No absolute relational irreducibility, autonomous dynamics selection,
metric, topology, causal order, curvature, continuum, QFT, gravity, GR,
species, particles, or Hamiltonian reconstruction is earned.

## Artifact absence and delivery boundary

The following future Stage-C and publication paths were absent at freeze:

```text
v16/code/p13_gamma_fresh_cases_v2.json
v16/code/p13_gamma_output_v2.txt
v16/code/p13_gamma_receipt_v2.json
v16/note-paper13-typed-groupoid-verification.md
v16/paper-13-one-relational-gamma-v2.md
v16/paper13_typed_groupoid_code/run_all.py
v16/paper13_typed_groupoid_code/manifest.json
v16/paper13_typed_groupoid_code/receipts_table.json
v16/paper13_typed_groupoid_code/RUN.txt
```

No fresh nonce or fresh case was generated.  Neither `--generate-fresh` nor
official `--run` was invoked.  No fixture was imported or evaluated.  No
official artifact was read.  Publication writes were zero.

The source-audit gate is next.  Fresh generation remains barred until two
mutually blind independent source audits authenticate these exact bytes,
reconstruct the total-bijection laws and G1/G18 effects without importing the
candidate, and a separate adjudication accepts the source.  A source-audit
failure keeps the rejected paper terminal and forbids regeneration.

The Stage-B implementation whitelist is exactly this frozen source, this
freeze note, and the three status/ledger boards required by the RUNBOOK.  This
note intentionally does not contain its own ordinary SHA-256; that value is
computed only after these note bytes stop changing.
