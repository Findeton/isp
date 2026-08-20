# Paper 13 typed-groupoid forward repair pin

Status: **RESULT-NEUTRAL FORWARD REPAIR PIN / NO SOURCE EDIT YET**

Date: 2026-08-19

## 1. Authority and question

This pin implements only the forward authorization in the Paper 13 hostile-
panel adjudication at commit
`7368c13e4d38f63a92f69694d7d0ed195f221123`.

The bounded question is:

> Can the presentation-indexed one-Gamma candidate be equipped with an exact
> typed source groupoid whose sparse witnesses compose as total finite
> bijections and whose action transports every physical argument, operator,
> certificate, and endpoint law functorially?

The pin is result-neutral.  It neither declares the repair successful nor
pre-awards the former eligible cap.  A local identity test is insufficient;
the whole regenerated evidence chain must pass.

## 2. Immutable base and exposure

The rejected corpus remains immutable and historical:

| object | identity / SHA-256 | permitted use |
|---|---|---|
| hostile adjudication | `v16/note-paper13-hostile-review-adjudication.md`, `9546729fce24ce8a4a08239c881814b9526232a33151324c1b2e98b9daa61e49` | binding repair authority and scope |
| adjudication normalized hash | `bea277684ef0cacbebcce0464bf2bfc77a1629bf7dbd0e156e2e63263d755ec4` | self-hash authentication |
| original construction pin | `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35` | unchanged law, source-language, arithmetic, and ontology walls |
| support-split repair pin | `8ae54ada2a97f347a18b90adcab86dcb2e7c18c04c748cc5e0779b8251449a36` | unchanged split/certificate contract |
| rejected evaluator | `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e` | historical source and regression reference only; never imported at runtime |
| rejected fresh cases | `2ac664c94a6b29c5b73fd8047e97a2e086ac45defc9c3431bc1ded66f011dd29` | exposed historical evidence only |
| rejected output | `7f544c79f60d91c84e5805541313ec9d7ac068cdf0ee4f6184947cf44f43886f` | exposed regression values only |
| rejected receipt | `83bd33028c81e9dd555a44e9e7721d5ace298d522e0c069409118bdbf51c6c48` | historical lineage; its groupoid pass is known incomplete |
| rejected paper | `db2f9f9a84f423bd8d23429ce567bc2e9236ea8deb3076f113c6aa692bd32446` | historical candidate; never silently edited |
| hostile protocol | `1914ef55118c8261f55d271a7431cf5bc7e5aa90689d39f4b927e6c39fe8bd58` | prior review schema and attack provenance |
| Seat A report | `1b4d566143837c8614bf4aa44469fe87061ce45055fe9aa9ca348057020dc702` | decisive counterexample provenance |
| Seat I report | `8153eda3ff440712d30483dfa12b6c20e7109d91a2785b1577f3374ebe1fd636` | preserved nondivision/division scope and bounded repairs |
| Seat R report | `340a7b7c2e5a24526486244106eb3ec8ba5de485cc585769ad7ca9c878efb314` | preserved relational scope and runner repair |
| RUNBOOK | `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58` | process and integrity contract |

All old finite examples, outputs, fresh cases, report attacks, and the exact
`e=()` / `w=(A->B)` survivor are exposed before this pin.  They are
regression and falsification controls, not fresh confirmation.  The repaired
cycle uses new versioned paths; no rejected artifact is overwritten, deleted,
or relabeled as repaired evidence.

## 3. Typed presentation objects

The source-groupoid objects are complete finite presentations, not raw label
sets and not hashes.  The evaluator must expose one immutable exact
`SourcePresentation` or equivalently closed type containing:

```text
typed Boolean-role carrier
matter-label carrier
port-label carrier
occurrence-label carrier for the complete filling
source boundary presentation
derived target boundary presentation
complete filling/Arrow presentation
```

Each carrier is finite, duplicate-free, and canonically ordered only for
serialization.  Boolean roles include their declared types.  The structural
data include all realized source and target contexts, port parents/children,
matter assignments, occurrence queries and order, and every coefficient-zero
typed target.  A presentation hash is provenance; the literal typed object is
the domain/codomain datum.

Two presentation objects may be groupoid-related only through a validated
type-preserving relabeling.  Equality of a raw hash, equal carrier
cardinality, or coincident endpoint probabilities is never a witness.

## 4. Typed sparse witnesses

Every witness is an immutable arrow

```text
w : X -> Y
```

with exact `source=X`, `target=Y`, a seal, and four sparse component maps:

```text
role_map
matter_map
port_map
occurrence_map
```

The component maps are completed over every label of the corresponding
source carrier.  An omitted row means `x->x` only if the same typed label is
present in the target carrier.  Completion must be a total bijection onto the
entire corresponding target carrier.  Validation therefore requires:

1. every source label has exactly one image;
2. every target label has exactly one preimage;
3. no source or target label is extra, missing, or duplicated;
4. Boolean role type is preserved;
5. namespaces cannot be crossed;
6. transporting the literal source presentation by the completed maps gives
   the literal target presentation exactly, including contexts, cells,
   boundaries, ports, formulas, filling order, and coefficient-zero targets.

Canonical serialization retains the complete source and target presentation
data and deletes only explicit identity rows from the sparse maps.  An empty
sparse map is lawful for `id_X:X->X`; an untyped empty tuple is not a physical
witness.  Distinct valid sparse encodings of the same typed total bijection
must canonicalize identically.

## 5. Identity, inverse, and composition

For each presentation `X`, the identity is

```text
id_X : X -> X
```

with empty canonical sparse maps and the complete typed carrier retained.

The inverse of `w:X->Y` is constructed from the completed bijection, has type
`w^-1:Y->X`, is revalidated as a total bijection, and is then canonically
sparsified.

For `w:X->Y` and `v:Y->Z`, composition is defined only when the complete
target presentation of `w` equals the complete source presentation of `v`.
It is computed for every label `x` of every source carrier:

```text
(v o w)(x) = v(w(x)).
```

The composite is checked as a total type-preserving bijection `X->Z`, checked
to transport the complete source presentation to the complete target, and
only then sparsified.  Iterating only the explicit rows of either operand is
forbidden.

The evaluator must establish extensionally and by canonical typed equality:

```text
w o id_X       = w
id_Y o w       = w
w^-1 o w       = id_X
w o w^-1       = id_Y
u o (v o w)    = (u o v) o w
```

for every registered composable triple.  No convention switch may make one
direction vacuous; the receipt prints the application order and both literal
sides of every law.

## 6. Groupoid action and naturality

The same completed witness acts on, and must exactly transport:

```text
contextual Boolean formulas and their truth-vector identities
contexts and split/merge fibers
ports and port declarations
source and target boundaries
configurations and complete state catalogues
occurrences and complete filling/Arrow ASTs
source-presentation keys and provenance keys
BoundSplitCertificate objects and classifier-consumed hashes
primitive linear maps and complete class operators
Gamma endpoint probability laws
record projectors, division cuts, reciprocal chains, and matching-family rows
```

For every such object `F`, the receipt checks the action law

```text
F(id_X) = id_{F(X)}
F(v o w) = F(v) o F(w)
```

in the appropriate exact category or value type.  For the Gamma evaluator it
also checks the naturality/covariance square after transporting source and
target bases.  The proof is repeated uncached for identity, inverse, a
nontrivial pair, and a three-witness chain.  A cached final Boolean, copied
operator, supplied endpoint table, or transported hash without transported
bytes is non-evidence.

Tensor compatibility is explicit.  Tensor witnesses require disjoint typed
namespaces or a validated common-label agreement, and satisfy identity,
composition, symmetry, associator, unitor, and interchange/naturality on
complete coefficient-zero-inclusive catalogues.

## 7. Finite positive census

The repaired source must derive, serialize, and independently reconstruct at
least the following finite surface.

### 7.1 Abstract total-bijection census

For one namespace, exhaust carrier sizes `n=0,1,2,3,4`.  For each `n`, use
typed source labels `s_0,...,s_{n-1}`, target labels
`t_0,...,t_{n-1}`, and every one of the `n!` bijections.  Include mixed
source/target carriers with at least one shared unchanged label so sparse
identity completion is exercised.  Record:

```text
source and target carriers
total map
canonical sparse map
inverse
left/right identity residuals
left/right inverse residuals
roundtrip canonical equality
```

For `n<=4`, exhaust every composable triple of permutations on a common
carrier and require exact associativity.  Repeat representative chains with
fresh target names and with disjoint explicit sparse supports.

### 7.2 Native complete-presentation census

Use at least:

1. the minimal `A->B` role relabeling that killed the old source;
2. one witness in each of the matter, port, and occurrence namespaces;
3. one witness moving all four namespaces together on the coherent control;
4. one contextual-alias case whose raw formula bytes differ but contextual
   Boolean identity agrees;
5. one CREATE, one MERGE, and one UNCHANGED bound split transition;
6. one complete record writer/continuation filling;
7. one reciprocal writer-to-probe filling;
8. one complete size-twelve global matching member;
9. one tensor product with nontrivial relabelings on both factors.

For every row, test identity on both sides, inverse on both sides,
composition, three-map associativity, source/target typing, complete operator
transport, endpoint-law transport, and source/certificate lineage.  All
coefficient-zero targets remain present.

## 8. Mandatory changed objects

All 92 prior registered attacks remain live and independently reconstructible.
The repair adds at least these typed-groupoid attacks; no row passes because
its name is recognized.

| ID | changed object | required disposition |
|---|---|---|
| G1 `EMPTY-LEFT-IDENTITY` | exact adjudicated `id_X` followed by nontrivial `w:X->Y` | equality with `w`, not the empty witness |
| G2 `EMPTY-RIGHT-IDENTITY` | nontrivial `w:X->Y` followed by `id_Y` | equality with `w` |
| G3 `INVERSE-LEFT` | `w^-1 o w` | exact `id_X` |
| G4 `INVERSE-RIGHT` | `w o w^-1` | exact `id_Y` |
| G5 `THREE-SPARSE-ASSOCIATIVITY` | three nontrivial maps with disjoint explicit supports | both parenthesizations identical |
| G6 `MIDDLE-PRESENTATION-MISMATCH` | carriers have equal size but `target(w) != source(v)` | refuse before composition |
| G7 `SOURCE-LABEL-OMITTED` | omitted row whose source label has no identical target label | refuse as nontotal |
| G8 `EXTRA-TARGET-LABEL` | target has no preimage | refuse as nonsurjective |
| G9 `MAP-COLLISION` | two source labels share one target | refuse as noninjective |
| G10 `ROLE-TYPE-SWAP` | equal names but incompatible Boolean-role types | refuse |
| G11 `NAMESPACE-CROSSING` | role mapped to matter/port/occurrence identity | refuse |
| G12 `TARGET-PRESENTATION-FORGERY` | carriers map bijectively but transported cells/ports/filling differ | refuse |
| G13 `IDENTITY-ROW-ENCODING` | explicit `x->x` row versus omitted row | same canonical witness and action |
| G14 `ORDER-REVERSAL` | compose in the opposite application order | changed native transported object and failed law |
| G15 `TRANSPORT-SEVER` | leave one context cell, port parent, occurrence query, or zero target untransported | typed refusal or nonzero residual |
| G16 `CERTIFICATE-TRANSPORT-CACHE` | reuse pre-transport split certificate | changed lineage and failed binding |
| G17 `COMPOSITE-OPERATOR-CACHE` | reuse sequential/composite operator under a moved witness | changed source key and failed naturality |
| G18 `COPIED-GROUPOID-BOOLEAN` | force `all_exact=true` while one native law row is false | specification gate false; earliest rung cannot exceed presentation-only |
| G19 `TENSOR-SHARED-LABEL-CONFLICT` | tensor factors disagree on a common typed label | refuse before operator construction |
| G20 `FRESH-GLOBAL-RELABEL-SEVER` | fresh matching member relabels its context but not challenge query/schedule | blind/groupoid dependency fails |

After final source freeze, G1 and G18 must also run as real source-only
off-tree changed-source attacks.  G1 replaces total composition by the old
first-row-only helper.  G18 bypasses the native conjunction at the promotion
door.  Each records old/new source hashes, exact patch, exit code, recomputed
law residuals, gate/outcome effect, lineage/claim/seal movement, stdout/stderr
hashes, and the earliest rendered rung.  A crash without semantic residuals
is insufficient evidence by itself.

## 9. Preserved scientific regression wall

The repair is not permission to retune the candidate law.  The following are
frozen regression obligations and must be independently reconstructed from
the new source:

- the contact-only rational Cayley family on `1/3 <= g <= 1/2`;
- exact `R`, `B`, `C`, `B^2`, and
  `K=[[351,-176],[-176,351]]/175` at `g=1/2`;
- the universal rational native nondivision bound `527/175`;
- the positive history-conditioned and enlarged-carrier Markovization
  controls and the exact nondivision wording;
- 72 ambient Boolean representatives / 42 contextual classes;
- 12 generator families, 312 source columns, and 468 bound nonzero
  transitions split 156 / 156 / 156 across CREATE / MERGE / UNCHANGED;
- all-input writer completeness, alternate-cut equality, finite continuation-
  grammar record preservation, and active-port inverse erasure;
- reciprocal joint `{00:9/25,01:0,10:144/625,11:256/625}` and same-boundary
  incidence comparison;
- one-call global matching construction, resource parity, blind-prefix/prior-
  record equality, and class-relative exclusion;
- every anti-wrapper, source-sufficiency, support, actualization, and ontology
  wall from the original pins and adjudication.

Any changed exposed scientific value, law family, carrier, grammar, division
doctrine, outcome vocabulary, or scope coordinate is a new result and blocks
this bounded repair.  Presentation/source hashes and groupoid receipt rows are
expected to change.

## 10. Outcome ladder and scope coordinates

The full original ladder remains ordered by earliest failure:

```text
P13-SPECIFICATION-INCONSISTENT
P13-REFERENT-PRESENTATION-ONLY
P13-GAMMA-UNCONSTRUCTED
P13-LAWFUL-SOURCE-SUFFICIENCY-UNPROVEN
P13-WRAPPER-OR-LOOKUP
P13-SHADOW-WELD-FAILS
P13-FIXED-CARRIER-ONLY
P13-SUPPORT-CHANGE-UNPROVEN
P13-RECIPROCAL-CHAIN-UNINSTANTIATED
P13-DIVISION-RECOVERY-UNPROVEN
P13-NATIVE-NONDIVISION-UNRESOLVED
P13-BLIND-CLASS-UNRESOLVED
P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED
P13-RELATIONAL-GAMMA-LAW-UNSELECTED
P13-LAW-SELECTED
```

If any typed-groupoid object, law, action, naturality row, or required attack
fails, the strict outcome is no higher than
`P13-REFERENT-PRESENTATION-ONLY`.  Passing the groupoid repair only restores
eligibility to test later rungs; it does not pre-award them.  The last two
rungs remain capped because no selector is introduced.

Every output and paper prints:

```text
event_filling_selection = PRICED-KINEMATICS
division_doctrine       = TYPED-CANDIDATE-AND-GRAMMAR-RELATIVE
actualization           = POSTULATED
valuation               = UNCONSTRUCTED
metric                  = UNCONSTRUCTED
curvature               = UNCONSTRUCTED
continuum               = UNCONSTRUCTED
GR                      = UNCONSTRUCTED
```

Native nondivision remains carrier/configuration-relative and does not imply
an unreal or ontologically incomplete intermediate configuration.  Blind
exclusion remains relative to the frozen incidence-erased transducer class
and calibrated query subset.

## 11. Receipt and lineage contract

The regenerated receipt includes machine-reconstructible bytes for:

- pin, RUNBOOK, adjudication, old-corpus provenance, new source, fresh cases,
  output, and normalized receipt identities;
- each complete `SourcePresentation` and typed witness used by a promoted
  claim;
- source/target carriers and presentations, sparse and completed maps,
  inverse, both identity composites, both inverse composites, and both
  associativity parenthesizations;
- composability/type checks and literal transported-presentation equality;
- the action on every object listed in Section 6, with uncached old/new bytes,
  residuals, and dependency hashes;
- the abstract census and native complete-presentation census;
- all old and new mutation objects, their semantic predicates, changed
  source/object hashes, affected claims, and rendered outcomes;
- every preserved scientific measurement and orthogonal scope wall;
- read-at-open ledger, exact publication whitelist, exposure/freshness ledger,
  and promotion-time seal manifest.

The groupoid claim is a conjunction over native law rows.  No consumer reads
only `groupoid.all_exact`; it consumes the typed witnesses, completed maps,
law residuals, transported-object hashes, and source/target identities in its
backward slice.  Claim and mutation tables use exact two-way keyed equality.
Counts are computed from emitted objects.  Falsifiers are verified to change
their assigned objects.  A separately implemented no-import verifier rebuilds
the total maps and groupoid laws without evaluator functions.

Correct the prior receipt wording by either serializing the literal
`-16*g*(1-g^2)/(1+g^2)^3` derivative or naming the existing half-scaled
expression `derivative_sign_witness`.  Use distinct changed objects for the
two reflection controls and the two old-port controls.

## 12. New source, fresh chronology, and paths

The repaired evaluator is a new complete source at

```text
v16/code/p13_gamma_exact_v2.py
```

It may be mechanically derived from the rejected source during construction,
but it is self-contained, imports no rejected evaluator or output, and gets a
new source identity.  The rejected source path never changes.

After the new source commits and passes independent source audit, one mutually
blind reviewer supplies one 32-byte nonce.  The generator uses the distinct
domain separator

```text
SHAKE256("P13-TYPED-GROUPOID-FRESH-v2" || new_source_sha256 || nonce)
```

with a frozen deterministic rejection/increment rule and no reroll.  The new
absent publication paths are:

```text
v16/code/p13_gamma_fresh_cases_v2.json
v16/code/p13_gamma_output_v2.txt
v16/code/p13_gamma_receipt_v2.json
```

The evaluator makes direct global Gamma calls.  Analytic factorization may
check but never supply fresh responses.  Any source edit after nonce
generation voids the cycle.  Old fresh cases are exposed anchors only.

## 13. CLI, determinism, and runner repair

The new source preserves strict modes:

```text
--selftest
--generate-fresh --nonce HEX --source-sha SHA256 --fresh-out ABSENT_PATH
--run --fresh FRESH_JSON --output ABSENT_PATH --receipt ABSENT_PATH
--mutant NAME
```

Unknown, absent, duplicate, incompatible, or relative publication arguments
refuse before science.  Writes are transactional to absent paths; failures
leave no partial files.  Scientific evaluation uses exact standard-library
arithmetic with no floats, tolerances, network, Git queries, time dependence,
unrecorded randomness, fixture import, or expected answer table.

Every complete mode has a 300-second cap and emits a progress record at least
once per sixty seconds.  The regenerated outer bundle runner must relay
authenticated child progress or emit its own periodic record rather than
buffering silently.  Root, alien-CWD, and true source-only off-tree/no-`.git`
runs are byte-identical apart from excluded timing diagnostics.

## 14. Staged whitelists

No path outside the active stage may change.  Every stage updates `v16/PLAN.md`,
`v16/LOG.md`, and `STATUS.md` in its own ledger commit.

### Stage A — this pin

```text
v16/note-paper13-typed-groupoid-forward-repair-pin.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

No source or result-known artifact changes in Stage A.

### Stage B — repaired source freeze

```text
v16/code/p13_gamma_exact_v2.py
v16/note-paper13-typed-groupoid-source-freeze.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

Only development selftests and source/object mutants may run.  No v2 fresh,
output, receipt, verification, paper, or bundle path may exist.

### Stage C — independent source audits

Each report freezes in its own commit and changes only its report path:

```text
v16/review-paper13-typed-groupoid-source-operator.md
v16/review-paper13-typed-groupoid-source-records.md
```

After both freeze, source-audit adjudication changes only:

```text
v16/note-paper13-typed-groupoid-source-audit-adjudication.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

Fresh generation remains barred until that adjudication accepts the source.

### Stage D — fresh generation, official run, and verification

```text
v16/code/p13_gamma_fresh_cases_v2.json
v16/code/p13_gamma_output_v2.txt
v16/code/p13_gamma_receipt_v2.json
v16/note-paper13-typed-groupoid-verification.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

Fresh generation occurs once.  Independent verification imports no evaluator
function and precedes paper drafting.

### Stage E — regenerated paper and bundle

```text
v16/paper-13-one-relational-gamma-v2.md
v16/paper13_typed_groupoid_code/run_all.py
v16/paper13_typed_groupoid_code/manifest.json
v16/paper13_typed_groupoid_code/receipts_table.json
v16/paper13_typed_groupoid_code/RUN.txt
v16/PLAN.md
v16/LOG.md
STATUS.md
```

The paper replaces `finite writer-reader fixture` by `finite writer-reader
construction`, states the typed groupoid theorem with both identity laws, and
retains every nondivision, grammar, class-relative, and ontology limitation.
The bundle contains no second scientific implementation and authenticates the
exact v2 source and artifacts.

### Stage F — hostile review and adjudication

A result-neutral protocol freezes first at
`v16/note-paper13-typed-groupoid-hostile-review-protocol.md`.  At least three
fresh mutually blind seats then freeze separate reports covering:

1. typed finite-map algebra, process category, totality, and anti-wrapper;
2. receipt lineage, source/fresh chronology, native nondivision, division,
   and all changed objects;
3. point-free quotient, reciprocal/family scope, representation, and ontology.

The protocol, each report, and final adjudication use separate explicit
whitelists and commits.  Reviewers do not import evaluator functions, inspect
sibling reports, or treat receipt conclusions as evidence.  One counterexample
defeats its universal claim.  Terminal status is conferred only by the final
adjudication.

## 15. Permanent walls and next event

This repair can at most recover one finite point-free relational Gamma
candidate with class-relative relational load and event grammar priced.  It
does not select the coupling, law, catalogue, event filling, division
doctrine, or actual outcome.  It does not turn contact into distance,
topology, causality, metric, curvature, gravity, continuum, GR, QFT, particles,
or phenomenology.

The sole next authorized event after this pin commits is Stage B construction
of `v16/code/p13_gamma_exact_v2.py` and its source-freeze note.  No fresh mode,
official run, paper edit, bundle edit, hostile dispatch, metric investigation,
or later unit may begin first.

normalized_sha256: 25710e084dc5539ab9d615e9baa833c46b93f27f681fee34df5cee6d31c2b7b1
