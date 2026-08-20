# Paper 13 hostile-panel adjudication

Date: 2026-08-19

Status: **ADJUDICATED REJECT AS WRITTEN / TYPED-GROUPOID FORWARD PIN ONLY**

## 1. Immutable record

This adjudication concerns the immutable Paper 13 candidate and bundle at
commit `317f3b58627a06539a470509b07259aebe15be7f`:

| object | SHA-256 |
|---|---|
| evaluator `v16/code/p13_gamma_exact.py` | `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e` |
| paper `v16/paper-13-one-relational-gamma.md` | `db2f9f9a84f423bd8d23429ce567bc2e9236ea8deb3076f113c6aa692bd32446` |
| receipt `v16/code/p13_gamma_receipt.json` | `83bd33028c81e9dd555a44e9e7721d5ace298d522e0c069409118bdbf51c6c48` |
| master runner `v16/paper13_code/run_all.py` | `b99a458f76c90be19e396b5f332db8219298e8d3f875cb97328f89aa83d595a4` |
| hostile protocol | `1914ef55118c8261f55d271a7431cf5bc7e5aa90689d39f4b927e6c39fe8bd58` |

The following mutually blind reports are preserved byte-for-byte:

| seat | commit | report | ordinary SHA-256 | verdict |
|---|---|---|---|---|
| A — operator/category | `56044158ad810cd6c3ef40aec131c4f616080b14` | `v16/review-paper13-operator-category.md` | `1b4d566143837c8614bf4aa44469fe87061ce45055fe9aa9ca348057020dc702` | `REJECT-AS-WRITTEN` |
| I — indivisibility/records | `87989e5ea19ed4c2e63cd501b4d860aadd4220b9` | `v16/review-paper13-indivisibility-records.md` | `8153eda3ff440712d30483dfa12b6c20e7109d91a2785b1577f3374ebe1fd636` | `ACCEPT-WITH-FIXES` |
| R — relational ontology | `9c576f92a7837641ae3e786c00c952d868140697` | `v16/review-paper13-relational-ontology.md` | `340a7b7c2e5a24526486244106eb3ec8ba5de485cc585769ad7ca9c878efb314` | `ACCEPT-WITH-FIXES` |

There is no majority rule.  The smallest independently reproducible object
governs the universal claim it tests.  Candidate, evaluator, fresh cases,
outputs, receipt, paper, bundle, protocol, and reports remain immutable.

## 2. Decisive reconstruction

The frozen `SourceGroupoidWitness` contains four sparse maps but no source or
target carrier.  Missing rows are interpreted as identities by `_rename`.
Its composition helper applies `first` and then `second`, but enumerates only
rows present in `first`:

```text
compose_rows(first, second)
  = ((source, second.get(middle, middle))
     for (source, middle) in first)
```

Let `e=()` be the advertised sparse identity and let
`w=((A,B),)` be one nontrivial role relabeling.  Then

```text
compose_rows(e,w) = ()
act(compose_rows(e,w), A) = A
act(w, A) = B.
```

Therefore `compose_witnesses(e,w)` is not extensionally equal to `w`.
Under the evaluator's order convention this is the ordinary law

```text
w o id_X = w,
```

and it fails.  The opposite direction happens to pass because enumerating
the rows of `w` retains them when the second map is empty.  The same defect is
available independently in the role, matter, port, and occurrence maps.

The receipt's identity row tests relabeling by `e`, not composition with `e`
as the first argument.  Its composition row uses two nontrivial witnesses
whose first map already enumerates the needed source labels.  The frozen
`groupoid.all_exact` field therefore omits the decisive law.

The adjudicator separately reconstructed the sparse action and the proposed
typed-total composition.  Once a witness carries finite source and target
label carriers, composition over every source label, identity completion,
target-surjectivity, and canonical removal of identity rows give both identity
laws, both inverse laws, and three-witness associativity on the minimal chain.
This shows that the defect is repairable in principle.  It does not make the
current bytes correct.

## 3. Accepted panel finding

Seat A's `KILL A1` is accepted.  The frozen implementation does not supply the
claimed source groupoid or its action, so it does not operationalize the
quotient of presentations used to promote a point-free physical referent.
The strict current rung is

```text
P13-REFERENT-PRESENTATION-ONLY
```

`P13-SPECIFICATION-INCONSISTENT` is not selected.  The corpus, source domain,
law family, grammar, paper spans, and artifact hashes agree.  This is a false
universal algebraic claim and an incomplete receipt measurement, not a
cross-file specification mismatch.

The paper grade is

```text
REJECT-AS-WRITTEN
```

This rejection is load-bearing but localized.  It is not evidence that the
candidate `Gamma_g`, its exact arithmetic, stochastic indivisibility, or the
physical strategy has failed.  It says that the present implementation has
not yet removed presentation dependence by a lawful groupoid quotient.

## 4. Reconciled Results A through G

The positive scope is the intersection of the three reports after applying
the decisive earlier rung.

| result | adjudicated status | exact surviving scope |
|---|---|---|
| A — contextual support extension | `SUPPORTED` | The literal finite Boolean split theorem, 72 ambient representatives, 42 contextual classes, and exact fiber certificates survive.  This does not by itself construct the quotient of complete presentations. |
| B — normalization and one-root composition | `SUPPORTED-PRESENTATION-INDEXED` | The complete typed process category and one whole-filling evaluator normalize on admitted presentation-level arguments.  No delegated screen, writer, reader, rewrite, or answer table was found. |
| C — totality and split covariance | `NARROWED` | The 312 declared columns, 468 nonzero transitions, and 156 CREATE / 156 MERGE / 156 UNCHANGED certificates survive.  Individual relabeling covariance survives; functorial groupoid composition and quotient promotion do not. |
| D — native nondivision | `SUPPORTED-CARRIER-RELATIVE` | The direct endpoint law has no positive source-independent restart kernel on the declared two-state carrier.  Definite intermediate configurations, positive history-conditioned joints, and enlarged-carrier or amplitude Markovizations remain explicit non-kills. |
| E — stochastic division | `SUPPORTED-GRAMMAR-RELATIVE` | Writer completeness, alternate-cut equality, and record preservation hold for every finite word in the frozen continuation grammar.  No universal permanence or autonomous division selector follows. |
| F — reciprocal response | `SUPPORTED-PRESENTATION-INDEXED` | One finite same-root matter-to-relation-to-matter response and its same-boundary incidence comparison survive.  It is raw relational sensitivity, not geometry, causality, curvature, or gravity. |
| G — blind-class exclusion | `SUPPORTED-PRESENTATION-INDEXED-AND-CLASS-RELATIVE` | The direct global size-twelve laws and induction exclude the predeclared incidence-blind transducer class under common initialization and equal resources, schedule, prefix token, and prior record law.  Unqueried-incidence drift prevents complete relation reconstruction, and no point-free quotient follows from the current source. |

The native nondivision result is not a state-description embarrassment.  Its
precise content remains:

> The cut is not a lawful stochastic division on the declared configuration
> space: the complete endpoint law admits no positive source-independent
> factorization through it.  A definite configuration may still be actual
> there; what is forbidden is an autonomous Markov restart conditioned only
> on that configuration.

## 5. Orthogonal coordinates

| coordinate | adjudicated disposition |
|---|---|
| specification consistency | `SUPPORTED` |
| presentation covariance | `SUPPORTED-CASE-BY-CASE` for individual complete relabelings |
| source groupoid / point-free quotient | `FAILED-IN-CURRENT-BYTES` |
| physical referent | `PRESENTATION-ONLY`; quotient candidate unconstructed |
| complete `Gamma_g` | `SUPPORTED-PRESENTATION-INDEXED` on the declared exact grammar |
| lawful-source sufficiency | `SUPPORTED-PRESENTATION-INDEXED` for complete typed lawful source arguments, never arbitrary cuts |
| shadow derivation | `SUPPORTED`; every registered scientific shadow reaches one primitive root |
| support change | `SUPPORTED` as an exact finite Boolean extension; quotient-functorial promotion withheld |
| reciprocal response | `SUPPORTED-FINITE-PRESENTATION-INDEXED` |
| division recovery | `SUPPORTED-GRAMMAR-RELATIVE` |
| native nondivision | `SUPPORTED-CONFIGURATION/CARRIER-RELATIVE` |
| blind-class eliminability | `SUPPORTED-FROZEN-INTERFACE-CLASS/PRESENTATION-INDEXED` |
| coupling `g` | `UNSELECTED` |
| law | `UNSELECTED`; candidate family postulated |
| catalogue | `UNSELECTED` |
| event/filling selection | `PRICED-KINEMATICS` |
| division doctrine | `TYPED-CANDIDATE-AND-GRAMMAR-RELATIVE` |
| actualization | `POSTULATED-NOT-DERIVED` |
| valuation | `UNCONSTRUCTED` |
| metric | `UNCONSTRUCTED` |
| curvature | `UNCONSTRUCTED` |
| continuum / gravity / GR / QFT | `UNCONSTRUCTED` |

## 6. Representation and ontology ledger

The finite typed presentations, exact Boolean incidence tables, process
fillings, and presentation-indexed endpoint laws are constructed.  The
implemented equivalence relation that would license a presentation-free
physical orbit is not.

Raw role names, Venn-cell encodings, formula syntax, hashes, matrix
coordinates, and internal path labels remain presentation or representation.
The whole-filling phase and composition class are nomological because changing
them changes endpoint probabilities; that does not make amplitude coordinates
ontic.  Endpoint squaring remains a postulated law clause.  Actualization is
not derived.

Nothing in the panel or this adjudication supplies valuation, distance,
dimension, topology, locality, causal order, Lorentz structure, curvature,
continuum, stress response, gravity, Einstein dynamics, QFT, particles,
Hamiltonian reconstruction, phenomenology, or empirical adequacy.  Boolean
contact is not metric contact, and filling order is not emergent time.

## 7. Other accepted repairs and narrowings

These findings do not change the strict rung but must be carried into any
forward cycle:

1. Replace the receipt's literal `derivative_sign_formula` by the actual
   derivative with coefficient `-16`, or rename the current sign-equivalent
   half-derivative as `derivative_sign_witness`.  The interval theorem and
   `527/175` bound are unchanged.
2. Give `PHASE-REFLECTION-MUTATION` and `SAME-BORN-REFLECTION` distinct
   changed objects, and likewise distinguish mere carried-port relabeling
   from an actual return-to-old-port attack.
3. Replace the paper and receipt phrase `finite writer-reader fixture` by
   `finite writer-reader construction`.  This is editorial vocabulary, not a
   scientific repair.
4. Make the master bundle runner relay authenticated evaluator progress or
   emit its own progress record at least every sixty seconds during long
   runs.  Direct evaluator progress already works.
5. Preserve the calibrated scope of Result G: unqueried incidence can drift
   without changing an assayed response, so the result is neither complete
   relation reconstruction nor absolute relational irreducibility.

## 8. Forward-only repair authorization

One separately frozen, result-neutral forward-repair pin is authorized.  No
candidate source, artifact, paper, or bundle byte may change before that pin
commits.  The pin must require at least the following.

### 8.1 Typed witnesses

Every witness is a typed arrow

```text
w : X -> Y
```

between complete finite presentations.  It carries immutable canonical
source and target presentation identities and the complete active label
carriers for every physical namespace: Boolean roles with types, matter
labels, port labels, and occurrence labels.  An empty sparse map is permitted
for `id_X:X->X`; an untyped empty tuple is not a physical witness.

Each sparse component is interpreted over every label of its declared source
carrier.  Missing rows act identically only when that same typed label exists
in the target carrier.  The completed map must preserve namespace and role
type and must be a total bijection onto the complete target carrier.  Extra,
missing, duplicate, colliding, cross-namespace, or mistyped labels refuse.
Canonical serialization retains source and target types while deleting only
explicit identity rows.

### 8.2 Composition and laws

For `w:X->Y` and `v:Y->Z`, `v o w` is defined only when the complete target
presentation of `w` equals the complete source presentation of `v`.
Composition evaluates `v(w(x))` for every active label of `X`, validates the
result as a total bijection `X->Z`, and then sparsifies identity rows.

The authoritative evaluator and an independent no-import verifier must test:

1. `w o id_X = w` and `id_Y o w = w` extensionally and canonically;
2. `w^{-1} o w = id_X` and `w o w^{-1} = id_Y`;
3. associativity for three composable nontrivial witnesses, including sparse
   maps with disjoint explicit supports;
4. refusal of mismatched middle presentations and every incomplete,
   noninjective, nonsurjective, or type-changing map;
5. identity, inverse, composition, and tensor compatibility for the action on
   formulas, contexts, ports, boundaries, configurations, complete fillings,
   source keys, split certificates, class operators, and endpoint laws;
6. naturality and covariance for both ordinary controls and the global
   matching family, with no cached transported shadow.

The exact `e=()` / `w=(A->B)` survivor is a mandatory changed object.  Separate
registered attacks must cover right identity, both inverse directions,
three-map associativity, middle-object mismatch, missing source labels, extra
target labels, collision, namespace/type crossing, stale composite caching,
and a copied final `groupoid.all_exact` Boolean.

### 8.3 Regeneration and review

The change is scientific evidence repair, not an editorial patch.  It
requires a new evaluator source hash and freeze note, new post-source nonce
and no-reroll fresh cases, new output and receipt, independent no-import
verification, and a regenerated candidate paper and self-contained bundle.
The old fresh cases and result-known artifacts remain historical and may not
be relabeled as evidence for the repaired source.

A separately frozen hostile protocol must independently review the complete
typed witness algebra, its transported scientific objects, receipt lineage,
the regenerated point-free claim, and all preserved native
nondivision/division/reciprocal/family scopes.  Passing the local identity test
alone does not restore the prior rung.  Only adjudication of the regenerated
corpus can do so.

## 9. Ordered successor debts and halt

The sole next authorized event is the typed-groupoid forward-repair pin.
After that, and only under the pin's explicit staged whitelists, the order is:

1. implement and source-freeze the typed witness/groupoid repair;
2. independently audit the frozen source and decisive changed objects;
3. generate one new nonce-bound fresh set and regenerate official artifacts;
4. independently verify the receipt and all transported dependencies;
5. regenerate the paper and bundle;
6. run and adjudicate the separately frozen hostile review.

The former eligible cap may be recovered if this chain passes; it is not
pre-awarded.  Paper 13 remains nonterminal and noncitable now.  No metric,
curvature, gravity, continuum, GR, QFT, or later paper investigation may begin
before terminal Paper 13 adjudication and a separately authorized successor
pin.

normalized_sha256: bea277684ef0cacbebcce0464bf2bfc77a1629bf7dbd0e156e2e63263d755ec4
