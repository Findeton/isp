# External hostile review — v13 RQ0-L0 computational certification

## Verdict: REJECT

The finite order-144 computation is mathematically correct, but the delivery cannot earn the registered L0 rung. The binding novelty condition fails: the held-out fixture is directly derived from the forbidden opened benchmark construction. Independent implementation attacks also refute the advertised fail-closed artifact validator and total untrusted-input resolver.

This is not a topology, causality, T1, or C1 objection.

## Ranked findings

### 1. CRITICAL — binding novelty/provenance gate fails

This is a procedural defect, not a group-theoretic counterexample.

The pin forbids a held-out object “derived from” either `S3^3` or `C2 x C3 x C4 x D4` ([pin:375-387](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification-pin.md:375)).

The fixture is plainly the opened order-192 template with its fourth factor changed:

- Opened fixture: `C2 x C3 x C4 x D4`, tensor-character construction, factor helpers, six selected generators, full rows, per-atom fields/records/gauges, and atom-set contexts ([old fixture:58-205](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_certification_fixtures_exact.py:58), [243-361](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_certification_fixtures_exact.py:243)).
- Held-out fixture: the same first three cyclic factors, tensor helpers, representation layout, selected-generator pattern, factor/scope helpers, row generator, per-atom records/gauges, and context machinery, with `D4` replaced by `S3` ([held-out fixture:52-240](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_fixture_exact.py:52), [262-390](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_fixture_exact.py:262)).
- Its natural permutation representation of `S3` also reproduces a component already present in the forbidden `S3^3` family ([S3 fixture:43-89](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_addressability_fixtures_exact.py:43)).

The scorer’s novelty predicate checks only:

```python
order == 144 and order not in (192, 216)
```

([scorer:313-319](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_score.py:313)). That proves nonisomorphism by order, but cannot prove non-derivation. The delivery substitutes “nonisomorphic” for the stronger registered condition at [delivery:94-97](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification.md:94).

### 2. HIGH — adversarial artifact adjudication can admit a false positive certificate

This is an implementation/certificate-validation counterexample.

`adjudicate_resolution_artifacts` checks that a positive atlas factorization occurs in `finest_certificates`, then rebuilds the atlas; it never reruns P1–P8 or even checks `certificate.passes` ([estimator:1810-1846](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:1810)). `build_full_regional_atlas` likewise checks membership only ([1117-1119](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:1117)).

On the unrelated public calibration, a fresh adversarial probe:

- replaced the finest certificate with an otherwise identical certificate having `independently_generated=False`;
- synchronized that object into `analysis` and `atlas`;
- passed it to `adjudicate_resolution_artifacts`.

Result:

```text
RQ0-LOCAL-ATLAS, exit 0, certificate_passes=False
```

The same hook admitted a positive after deleting all reported normal subobjects and all non-finest certificates. It also admitted forged scientific address/regional negatives without deriving their obstruction.

This refutes the “total, fail-closed validation of a returned or adversarially mutated result” docstring and the proof claim that artifact adjudication validates certificates ([soundness:324-340](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification-soundness.md:324)).

### 3. HIGH — serialized input and cap handling are not total or type-strict

Fresh probes used only the unrelated public calibration, not the held-out fixture or scorer.

The deserializer coerces arbitrary values with `bool`, `int`, and `str`; notably `bool("false")` becomes `True` ([legacy estimator:462-477](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_certification_estimator_exact.py:462)). Replacing every serialized selectability Boolean by the JSON string `"false"` still returned:

```text
RQ0-LOCAL-ATLAS, exit 0
```

Shape validation omits carrier checks for gauge laws, validation of readout projector partitions, and boundary compatibility among contexts, fields, and records ([633-672](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_certification_estimator_exact.py:633)). Each of these malformed public mutations still returned a positive atlas:

- dimension-1 gauge law on a dimension-30 carrier;
- readout resolution `[[999]]`;
- incompatible nonempty context boundary;
- incompatible record boundary.

Cap construction occurs before the resolver’s `try` block ([compcert estimator:1867-1869](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:1867)):

- `cap_seconds=None` raised an uncaught `TypeError`;
- `cap_seconds=NaN` disabled deadline comparison and returned a positive atlas.

Thus “every invocation” and “untrusted serialized input” are too broad.

### 4. HIGH — official gate design does not implement the registered neutral stopping rule

Several gates are declarative or truth-fed:

- H005 is the insufficient order-only novelty predicate.
- H035 is literally `add(..., True, ...)` ([scorer:422-424](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_score.py:422)).
- The anchor mutant merely constructs a procedural `Outcome`; it does not run a corrupted-anchor official pipeline ([479-484](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_score.py:479)).
- H001–H004 compare fixture fields with truth constants originating in the same fixture.

The scorer is also positive-biased. Its metamorphic checks require `is_positive(result)` ([375-383](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_score.py:375)); therefore a stable, valid scientific negative cannot pass the official suite, contrary to the pin’s instruction to freeze whichever registered positive or scientific negative occurs.

When the main result is negative, unreachable controls are counted as passing or silently omitted ([348-350](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_score.py:348), [398-400](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_score.py:398)), contrary to the pin’s “not reached, never counted as passing” requirement.

The actual receipt does contain exactly 35 entries, but H005 and H035 do not earn their advertised conclusions.

### 5. HIGH — the twisted-triple gate is not a full fieldwise triple audit

All three generated pair maps pass the implementation’s validator. That limited fact survives.

The stronger claim does not:

- Record dynamics are matched by literal `_record_nonprojector_key` equality, not transported through the carrier action ([1402-1406](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:1402), [1613-1637](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:1613)).
- The triple comparison never composes operation, row, preparation, context, probe, readout, record, or gauge maps.
- It compares only carrier actions and two hard-coded singleton atoms ([1691-1702](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:1691)).
- The pair validator does not require every source row exactly once; a duplicated row pair can replace another while preserving its length and membership tests.

Therefore H034 establishes a small carrier/projector twist, not the claimed full-instrument “only loop equation fails” theorem.

### 6. MEDIUM — declared completeness theorem omits a necessary qualification

The search excludes the ambient subgroup and emits only tuples of at least two factors ([estimator:532-537](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:532), [619-623](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_estimator_exact.py:619)). Yet the proof claims every finest tuple satisfying P1–P8 ([soundness:368-380](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification-soundness.md:368)).

For a fully selectable indecomposable group, the singleton tuple `(G)` can satisfy the coded P1–P8—pair predicates are vacuous and its represented algebra is the ambient algebra—but the search returns no tuple. The theorem must be restricted to decompositions having at least two proper factors.

The divisibility pruning itself is sound for that corrected search class.

### 7. MEDIUM — claim inflation in the delivery note

Required replacements:

- “fresh W3 record candidates” ([delivery:99-107](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification.md:99), [180-182](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification.md:180)) should say four instances of the same pre-existing two-level Fourier witness helper. Their supports and ambient projectors differ; their write/preserve/erase dynamics do not.
- “independently supplied laws” and “observed signatures” should say separately serialized but co-generated fixture fields: every row law is looked up from `laws[result_index]`, and every signature is immediately computed from it ([fixture:281-295](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_fixture_exact.py:281)).
- “physical stable-fact descent” ([delivery:190-191](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification.md:190)) should be narrowed to a synthetic exact operational model.
- The 64 regional/fact paths include identities; only 12 are strict two-step restrictions.
- “all mandatory controls” and the corrupted-anchor claim ([195-235](/Users/felixrobles/workspace/isp/v13/note-rq0-operational-localization-computational-certification.md:195)) overstate the gate coverage.

The no-topology/no-causality ceiling is correctly stated.

## Chronology and immutability

These checks pass:

- The commit chain is linear in the registered order:
  `605761b → d881a3e → 59011af → b9e574a → 1b3ffb7`.
- The pin is byte-identical from `605761b` through HEAD.
- Estimator and proof are byte-identical from `d881a3e` through HEAD.
- Current SHA-256 values match the receipt:
  `a9f8…30f8b` and `5839…cd2d`.
- All five registered future paths are absent from the `d881a3e` tree.
- The exact `C2 x C3 x C4 x S3` family/string is absent at `d881a3e`.
- Fixture and scorer are byte-identical from `b9e574a` through HEAD.
- Receipt/output/delivery are added only at `1b3ffb7`.
- The previous invalid-cycle estimator/fixture targets remain unchanged.
- Git contains one committed official receipt and no receipt rewrite. Actual process invocation count is not observable; `official_runs: 1` is a hard-coded receipt field ([scorer:550-557](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_heldout_score.py:550)).

Static inspection finds no estimator branch on 192, 144, 216, fixture hashes, `theta` handles, intended factors, contexts, records, or atlas truth.

## Independent exact reconstruction

Fresh code at `/tmp/rq0_independent_rebuild.py` imported no delivery modules. It implemented the group, monomial laws, exact arithmetic in  
\(\mathbb Q[x]/(x^8-x^4+1)\), sparse Gaussian elimination, normal-subgroup closure, complement enumeration, certificate enumeration, and the context/fact poset.

| Quantity | Independent result | Delivery |
|---|---:|---:|
| Quotient order | 144 | 144 |
| Complete rows | 20,736 | 20,736 |
| Carrier | 24 | 24 |
| Distinct framed laws/signatures | 144 / 144 | implicit |
| Associative / identity / inverses | yes / unique / all | yes |
| Center / derived subgroup | 24 / 3 | 24 / 3 |
| Element orders | \(1^1,2^{15},3^8,4^{16},6^{48},12^{56}\) | same |
| Normal subobjects | 70 | 70 |
| Order-product complement tests | 234 | 234 |
| Actual direct-complement pairs | 41 | not reported |
| Direct-pool members | 36 | 36 |
| Selectability-eligible pool | 14 | 14 |
| Rejected by P1 generation | 22 | implicit |
| Passing certificates | 14: 7 pairs, 6 triples, 1 quadruple | 14 |
| Finest certificates | 1 | 1 |
| Finest orders | `(2,3,4,6)` | same |
| Finest algebra dimensions | `(2,2,2,5)` | not reported |
| Ambient represented algebra dimension | 40 | implicit |
| Explicit finest algebra-product rank | 40 from 40 products | pass |
| Regions / arrows / fact maps | 10 / 31 / 31 | same |
| Regional/fact composable paths | 64 / 64 | same |
| Strict nonidentity two-step paths | 12 / 12 | not reported |
| Nonempty pair meets / triples | 6 / 3 | 6 / 3 |
| Universal core | empty | empty |
| Complete proper Boolean | false | false |

Additional surviving facts:

- The frame-conjugated representation is exactly multiplicative, not merely projectively multiplicative.
- Its 144 row-gauge signatures are distinct, so the quotient has no hidden alias collapse.
- Group order alone proves nonisomorphism with the order-192 and order-216 objects.
- The five nonidentity selectable generators generate all 144 elements. Including inverses, word lengths are distributed as `0:1, 1:8, 2:26, 3:44, 4:41, 5:20, 6:4`; selectability is substantive.
- The 14 passing certificates are precisely the nontrivial set-partition coarsenings of the four finest factors.
- Every actual regional operation projection, all 23,081 carried row entries, all 699 operation/selectability entries, and all per-field restriction maps are consistent.
- The 10 regions contain nonempty record interfaces. Binary coordinate projectors give 2, 4, or 8 nonempty fact atoms for singleton, pair, or triple regions, and all 31 Boolean pullbacks are exact.
- Each reused two-level witness independently evaluates to:
  occurrence `True`, preserving availability `(True)`, erasing availability `(False)`, erasing cross-coherence `(2)`, and no-write occurrence `False`.
- Record and witness handles are absent from structural record identity; handle renaming is genuinely invisible for this fixture.

## Public qualification

The measured performance and cache facts survive:

- addressability `12.24 s`;
- base completion `14.05 s`;
- base plus listed mutant pipeline `67.21 s`;
- dense/sparse differential audit `81.33 s`;
- one ambient build;
- one build per 14 canonical nonambient keys;
- exact dense/sparse agreement on all 15 requested public subobjects;
- opened benchmark remains scientifically sterile.

Qualification evidence is weaker than the prose:

- Q007 compares two base-case functional objects, not two independently regenerated complete 48-gate receipts ([public runner:440-448](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_public_qualification.py:440)).
- The nominal functional receipt contains timing-derived Q008/Q009/Q048 pass bits, and its “functional output” contains raw timing values ([public output:6-8](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_compcert_public_functional_output.txt:6)).
- Several static/ceiling gates are weak or declarative.
- Metamorphic gates compare a coarse structural summary rather than full fieldwise canonical artifacts.

## Claims that survive

- Frozen chronology and byte immutability.
- No estimator tailoring to either old or new fixture.
- Exact finite group law, representation faithfulness, quotient invariants, and nonisomorphism.
- The corrected finite P1–P8 soundness result for normal resolver outputs.
- The corrected completeness result for decompositions into 2–8 proper normal direct factors, subject to caps.
- All independently reconstructed counts in the table.
- Actual held-out record/projector/context maps and handle invariance.
- Sparse/dense mathematical equivalence and the measured cache behavior.
- No topology, spatial, causal, Lorentzian, spacetime, field, or gravity claim.

## Claims to withdraw or replace

Withdraw:

- genuinely new/non-derived held-out fixture;
- H005 as a valid novelty gate;
- “35/35 mandatory hostile controls” as substantive evidence;
- total resolver for every invocation/untrusted serialized input;
- adversarial artifact replay as fail-closed;
- full-field twisted-triple certification;
- unqualified “every P1–P8 tuple” completeness;
- fresh record dynamics;
- independently observed row laws/signatures;
- physical stable facts.

Replace the scientific summary with:

> A byte-frozen generic estimator correctly reconstructed a finite normal-direct-product atlas on a post-freeze, nonisomorphic but source-derived synthetic benchmark. This computation is useful as opened regression evidence but does not satisfy the registered held-out novelty or robustness gates.

## Terminal recommendation

Adjudicate this successor cycle as:

```text
procedural outcome = RQ0-L0-INVALID
scientific outcome = null
```

Do not use `ACCEPT-WITH-FIXES`: the stopping rule prohibits post-truth estimator repair, fixture replacement, and rescore. Preserve the correct order-144 computation as an opened benchmark only. Do not begin T1 or C1.
