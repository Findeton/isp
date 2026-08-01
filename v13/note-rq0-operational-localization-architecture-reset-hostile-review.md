# External hostile review — RQ0-L0 public architecture reset

**Target:** `e55cb68`  
**Governing pin:** `c0fab11`  
**Verdict:** **REJECT**

The opened finite mathematics is mostly sound. The `Q8` model, its W3 seams, its indecomposability, and its intended inclusion diagram all independently reproduce.

The rejection is architectural: the trusted verifier can certify a positive overlap-first result without requiring any overlap maps or intersections. Several other registered guarantees are also incomplete.

## Findings

### F1 — FATAL: a positive atlas passes with no arrows or intersections

In [`rq0_l0_archreset_verifier_exact.py:2148`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:2148), arrows are parsed from the claim, but no minimum arrow set is required. The loops checking composition, pair intersections and triple intersections are vacuous when those arrays are empty. The verifier then returns `category="positive"` at line 2278.

Starting from the valid public `Q8` overlap claim, retain the five object datasets and correct `op_scopes`/`rec_scopes`, but replace:

```text
arrows = []
pair_intersections = []
triple_intersections = []
```

The verifier reaches its positive return with:

```text
objects = 5
arrows = 0
pair_intersections = 0
triple_intersections = 0
```

It also never requires identity arrows. A weaker mutant can retain the seven proper inclusions but delete all five identities and still form the required public squares.

This directly violates the pin’s requirement that positive acceptance preserve executable arrows, pair pullbacks and triple pullbacks.

Replacement sentence:

> The current verifier authenticates reconstructed scope lists and any regional maps supplied by the claimant, but it does not require a regional category, identity arrows, or any pair or triple overlap. Therefore the overlap-first architecture gate is fail-open.

### F2 — FATAL: overlap is still inferred from shared handles

The proposer constructs intersections by literal set intersection at [`rq0_l0_archreset_exact.py:311`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_exact.py:311) and [`rq0_l0_archreset_exact.py:333`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_exact.py:333).

The verifier repeats this at:

- [`rq0_l0_archreset_verifier_exact.py:2136`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:2136), requiring regional objects to use the ambient operation handles literally;
- [`rq0_l0_archreset_verifier_exact.py:2197`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:2197), defining a pair intersection by `left_scope & right_scope`;
- [`rq0_l0_archreset_verifier_exact.py:2256`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:2256), doing the same for triples.

Consequently, independently renamed regional operation classes are rejected even if full `RegAddr` isomorphisms exhibit the same physical subinstrument. The public rename control renames the ambient dataset before reconstructing every region, so it does not test independent regional presentations.

The pair universal-property test is only relative to the claimant-supplied arrows. The triple check has no universal-property test at all; it checks only cone commutation.

This conflicts directly with pin lines 333–340, which prohibit equal handles or planted set intersections from establishing overlap.

Replacement sentence:

> The public `Q8` fixture realizes the intended inclusion poset, but the generic implementation still identifies intersections through globally shared operation handles. It has not yet reconstructed overlap solely from executable instrument morphisms.

### F3 — MAJOR: the descended projector algebra need not be the W3 record algebra

A record contains both:

- dense `cut_record_projectors` inside its W3 witness;
- a separate `ambient_projector_resolution`.

Both are validated individually, but they are never compared.

Relevant paths are:

- record parsing at [`rq0_l0_archreset_verifier_exact.py:636`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:636);
- W3 evaluation at [`rq0_l0_archreset_verifier_exact.py:950`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:950);
- record-scope recovery at [`rq0_l0_archreset_verifier_exact.py:1936`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:1936).

A concrete valid-schema mutant replaces each binary ambient resolution `[[0],[1]]` with the valid one-atom resolution `[[0,1]]`. The W3 binary seam still passes because it uses the unchanged dense cut projectors. Record scopes are unchanged because they use `access_operations`. Identity regional maps transport the new one-atom resolutions consistently. The positive overlap claim therefore survives while its purported fact algebra is trivial and no longer represents the W3-recorded binary fact.

The malformed-projector controls do not detect this because the replacement is a valid partition.

Replacement sentence:

> Projector pullbacks are checked only for the separately supplied ambient resolution. The verifier does not yet prove that this Boolean algebra is the algebra certified by the W3 witness.

### F4 — MAJOR: the “481 systematic mutations” do not implement the pinned mutation matrix

The systematic generator at [`rq0_l0_archreset_public_audit.py:220`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_public_audit.py:220) performs:

- missing-key mutations;
- wrong-type mutations;
- one unknown-key mutation per normalized mapping object;
- wrong types for representative array leaves.

It does not systematically perform, for every applicable schema field:

- empty required values;
- duplicates;
- dangling references;
- out-of-range values;
- dimension mismatches;
- incompatible boundaries;
- corrupted laws;
- corrupted signatures.

Those appear only in a small named subset. The suite also lacks semantic coverage of `UNAVAILABLE` and `COLLAPSED` rows and skips contextual mutation of embedded datasets and maps.

The stored count of 481 is correct for the implemented normalization algorithm, but it is not the full field-by-field adversarial matrix required by pin lines 281–294.

The neutrality control at [`rq0_l0_archreset_public_audit.py:379`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_public_audit.py:379) is also declarative: it feeds the literal sequence `(True, False, True)` and literally records `not_reached_counted_as_pass=False`. It is not connected to actual pipeline prerequisites. This violates the pin’s prohibition on literal-true gates.

Replacement sentence:

> The audit rejects 481 normalized shape/type mutations and all eighteen named attacks. It does not yet cover every registered semantic mutation class, and its `NOT-REACHED` accounting is a synthetic demonstration rather than an end-to-end control.

### F5 — MAJOR: the total boundary can emit an unstructured success

At [`rq0_l0_archreset_exact.py:477`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_exact.py:477), the injected serializer’s output is accepted whenever its exact type is `str`. The returned text is not parsed or checked against the response object.

For example:

```python
serializer=lambda *_args, **_kwargs: "not-json"
```

produces exit code 0 and the text `not-json\n` after successful verification. Multiple JSON documents or a contradictory serialized status likewise pass.

Thus “every invocation returns exactly one structured engineering response” is false. The audit tests only a serializer that raises an exception.

There is also a small alarm-installation race: `alarm_state` is assigned after `setitimer`; a very short timer firing in that interval can leave the altered handler unrestored.

Replacement sentence:

> The default JSON serializer is fail-closed for the tested exception path, but arbitrary string-returning serializers are not authenticated. The total structured-response guarantee is therefore not yet secured.

### F6 — MAJOR: the direct-factor claim is narrower than stated

The algebraic search itself has a sound core:

- normal subgroups are generated by joins of element normal closures;
- candidate tuples are exhaustively enumerated from two through eight factors subject to caps;
- P1–P7 are recomputed exactly;
- a negative is accepted only after exhaustive search.

However:

1. The public proposer exposes only `finest_certificates` at [`rq0_l0_archreset_exact.py:139`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_exact.py:139), not every valid decomposition.
2. Positive verification checks only the supplied tuples at [`rq0_l0_archreset_verifier_exact.py:1321`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:1321); it does not establish that no valid tuple was omitted.
3. P8 at [`rq0_l0_archreset_verifier_exact.py:1223`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_verifier_exact.py:1223) checks algebraic closure and implemented rows for subtuples. It does not check stability of preparations, contexts, probes, readouts, records, projectors or gauges under declared restrictions.
4. The 100,000-test normal-subobject cap at line 1096 is not stated numerically in the theorem note or output.

An independent `C2^3` calculation found:

```text
valid two-factor decompositions:   28
valid three-factor decompositions: 28
```

A finest-only result exposes the 28 three-factor decompositions and omits the 28 valid two-factor decompositions.

Replacement sentence:

> The internal finite search explores candidate tuples of two through eight proper normal factors, while the public claim surface exposes only maximal-factor-count certificates. P8 currently means algebraic subtuple closure, not full-field regional restriction stability.

### F7 — MINOR: verifier independence is logical, but not supply-chain independent

The verifier imports no proposer or public-model module. It also does not use expected factors, expected atlas truth, novelty flags or obstruction prose.

However, the supposedly small shared kernel imports approximately thirty definitions from the 2,600-line legacy estimator at [`rq0_l0_archreset_kernel_exact.py:17`](/Users/felixrobles/workspace/isp/v13/code/rq0_l0_archreset_kernel_exact.py:17). That dependency contains much more than exact arithmetic.

No fixture truth or current proposer dependency was found through this path, so this is not evidence of circular acceptance. It does mean proposer and verifier share a large legacy implementation surface, and the “tiny exact-arithmetic primitive module” claim is inaccurate.

Replacement sentence:

> The verifier is independent of the new proposer and public fixtures, but its arithmetic dependency is a wrapper around a large legacy estimator module rather than a standalone minimal trusted kernel.

### F8 — MINOR: triple composition is implemented broadly, but public coverage is narrower

Individual `RegAddr` maps enforce source coverage, injectivity, isomorphism surjectivity, row metadata, laws, contexts, records, projectors and gauges. `compose_regaddr` composes every listed map family, and `verify_full_triple` compares them.

The public twisted control actually differs in:

```text
carrier_action
operation_map
row_map
context_map
record_map
```

It does not independently exercise loop differences in preparation, probe, readout or gauge maps. The source logic includes those families, so no direct defect was found, but the advertised adversarial coverage is incomplete.

## Independent rebuild

I used a fresh scratch implementation at:

```text
/tmp/rq0-archreset-hostile.mBg2Ho/independent_rebuild.py
```

It imports no ISP module. It independently implements the finite groups, monomial laws and the two-level exact W3 calculation.

Exact output:

```text
Q8 order: 8
normal subgroup orders: [1, 2, 4, 4, 4, 8]
proper normal subgroup orders: [2, 4, 4, 4]
normal direct-product pairs: 0
C4 pair-intersection orders: [2, 2, 2]
Q8 monomial representation multiplicative: true
distinct Q8 monomial laws: 8

W3 occurrence: true
preserving availability: true
erasing availability: false
erasing cross coherence: 2
no-write occurrence: false

Q8 atlas objects: 5
Q8 inclusion arrows: 12
composable paths: 22
pair pullbacks: 3
triple intersection equals central C2: true

C2 x C3 factor orders: (2, 3)
intersection order: 1
multiplication faithful and onto: true
```

The sparse monomial encoding is mathematically the same flattened vector with zero coordinates omitted. Exact Gaussian elimination therefore has the same rank as the dense encoding. The public dimensions—4 for the `C2 x C3` representation and 4 for the irreducible `Q8` matrix span—are consistent.

## Secured-status table

| Item | Assessment |
|---|---|
| Exact scalar/container typing | Secured for implemented parser paths |
| Named hostile malformed-input cases | Secured |
| Full registered schema-adversary matrix | Not secured |
| Total structured fail-closed boundary | Not secured |
| Independence from new proposer/model truth | Secured |
| Minimal trusted-kernel independence | Not secured |
| Algebraic P1–P7 tuple soundness | Secured |
| Negative search over 2–8 factors, subject to cap | Secured |
| Enumeration of every positive decomposition at public boundary | Not secured |
| Full-field P8 restriction stability | Not secured |
| Individual full `RegAddr` validation | Substantially secured |
| Category identities/mandatory regional maps | Not secured |
| Coherent/twisted full-map loop logic | Secured at public scope |
| Exact public `Q8` indecomposability | Secured |
| Intended public `Q8` inclusion diagram | Secured as a designed fixture |
| Generic physical overlap verification | Not secured |
| Handle-independent overlap | Not secured |
| W3-derived FactIface projector algebra | Not secured |
| Independent `OpSub`/`RecSub` categorical equivalence | Not secured |
| Positive/finite-negative status symmetry | Secured |
| End-to-end `NOT-REACHED` accounting | Not secured |
| Scientific L0 outcome | Correctly remains null |
| Performance qualification | Not earned; order 192 timed out |

## Scope conclusion

The public `Q8` construction remains useful calibration evidence: an indecomposable finite quantum process can contain the intended overlapping record-bearing subinstruments.

What failed is the verifier’s ability to distinguish that full construction from a claim containing only matching scope lists and object datasets. Therefore this snapshot cannot be treated as a sound pre-freeze overlap-first architecture.

No scientific L0 result, L0 no-go, topology, influence, causal, geometric, spacetime, field or gravity conclusion follows.
