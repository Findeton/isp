# APR Paper 12 — v4 artifact preservation and semantic verification failure

**Date:** 2026-08-19

**Status:** V4 ARTIFACTS REPRODUCIBLE; POSITIVE-PATH CERTIFICATION FAILED

**Disposition:** PRESERVE THE NEGATIVE BASELINE; NO CANDIDATE OR PANEL

## 1. Frozen source and artifacts

The committed v4 scorer is:

```text
commit: 6fe95fb8ef94029f4e4738da7d658bc13c5423c4
v16/code/apr_score.py
SHA-256: a7167e21e0a3e6b582acd8ebc8b7464476964cc09131a9721721a4dc99009e80
```

The one transactional official run produced:

```text
v16/apr_output_v4.txt
SHA-256: 68374ea18576466ccc40553f8b221360fdfce3fc43d5b555a6eeb0d2827a2f56

v16/apr_receipt_v4.json
SHA-256: ab9ea941fceebf5b57c7955d483730f3a5f0b317bb5a21da9cc0820331919a61

canonical receipt payload SHA-256:
04a1e370c601f9d7e3d5310f9bf20296d7be5c5428010f0f7af6c073d0b438d8
```

The payload digest independently recomputes after removing its self field,
and the output is the exact registered projection of the receipt. All 14
immutable file hashes agree. Repository-root, alien-CWD, and true off-tree/
no-`.git` official replays are byte-identical. The existing-path run refuses
without changing either artifact. The fixture-free self-test remains 27/27
with semantic witness SHA-256
`2dd13cc3f2a8e0850ce09b764e147cf37130bdc32d1c93d336f3da932a25cc90`.

## 2. Scientific baseline that survives

Independent reconstruction continues to give:

```text
strict_primary: APR-BLOCKED-AT-BOUNDARY-GLUING
process: STATIC-RESPONSE-ONLY
ontology_role: STATIC-RESPONSE
atomlessness: SYNTAX-ONLY
locality: FAIL as an unconstructed promotion, not observed nonlocality
contact: PRICED
causality: PRICED
one_law_provenance: UNCONSTRUCTED
law_selection: UNSELECTED
```

The decisive simultaneous-gluing ambiguity is exact. Both registered global
extensions give every `AB` and `BC` cell probability `1/4`; one gives
`P(A=C)=1/2`, the other gives `P(A=C)=1`. No frozen rule selects between
them. This is a regional joint-extension diagnostic only, not a microscopic
transition law.

The artifact therefore remains a valid, carefully scoped negative baseline.
The failures below concern the scorer's mandatory generic positive paths and
prevent certification of its result-neutral promotion logic. They do not move
the APR primary.

## 3. Independent verification result

One independent black-box verifier returns:

```text
319 PASS / 4 FAIL
three independent blocker roots
verifier SHA-256:
04ca6c1bfa78d52ff30d772fa8369567191450ad6a3accb1cd3a7231308a79be
result SHA-256:
67252d4f3047603999b7480ded0cf47477134e91c1063b37b3830d73d4fe82df
```

The corresponding private read-only audit files are
`/private/tmp/apr_v4_independent_blackbox.py` and
`/private/tmp/apr_v4_independent_blackbox_result.json`.

Its weld reproducer/result hashes are:

```text
0476941586246fbfdaf0bc2a7a8f5f18c4d86d96e5774118c812cbe9694890fe
837a0e2d62e747605d040d700087abc741f00c4d8cff97c697f1fee493a94cd0
```

Those files are `/private/tmp/apr_v4_weld_reproducer.py` and
`/private/tmp/apr_v4_weld_reproducer_result.json`.

Its conjugation source-mutant reproducer/result hashes are:

```text
bf2649f7beedf8ae55e1f241ec627d11c4535e09578f506ca32ed9b95e64283a
9727e8c95ad4411275de9c8aef452a6b0da2ec16f9cf71be87e7c2e7a0994e3e
```

Those files are `/private/tmp/apr_v4_s2_reproducer.py` and
`/private/tmp/apr_v4_s2_reproducer_result.json`.

A second independent scientific/ontology audit reaches the same two weld
blocks. Its private exact counterexample script hashes to
`24048356118452ef528dc7d1ea54a446241e0d11fadf796747d8232d31b9ce6b`;
its output hashes to
`df53fe2efa746214e653ac52255414bf11c0d0746dbbb5e9ffa72ba5214fd06c`.
Root reproduced that output exactly from the frozen scorer bytes.

## 4. Blocker A — the shared-transition weld is decorative

The classifier's component evaluators carry a `transition_reference_id`, but
do not use the referenced transition in their load-bearing computations. A
separate dependency layer checks only the nominal reference and a one-input
calibration equation.

Two independent attacks demonstrate the defect:

1. Replace the selected `X` transition by reset-to-one
   `R_1=[[0,0],[1,1]]`. It still maps `delta_0` to `delta_1`. The dependency
   graph remains valid, `L_X` remains selected, the joint primary remains
   reachable, and every substantive component-measurement hash is unchanged,
   although `X delta_1=delta_0` while `R_1 delta_1=delta_1`.
2. Replace `X` by the non-involutive stochastic map
   `[[0,1/2],[1,1/2]]`, which also maps `delta_0` to `delta_1`. A changed
   scorer still passes all 27 groups and preserves the joint positive word;
   all seven component measurements remain byte-identical.

Thus one-point calibration plus IDs/roots does not make a transition the law
actually consumed by compiler, overlap, process, comparison, locality,
causal, or contact measurements. Complete candidate-law bundles and resolved
typed occurrence traces remain unbuilt.

## 5. Blocker B — the ontology ladder is not one composable law

The positive ontology control contains three separately valid pieces:

```text
conditioning: A -> A
writer: record-source -> record-source_x_flag
rewrite: G2 -> G3
```

There is no typed arrow identifying the conditioning output with the writer
input or the writer output with the rewrite input. Nevertheless the evaluator
promotes the package to `REGION-REWRITING`.

Replacing the rewrite source/target and regional IDs by wholly alien carrier
objects, while retaining the matrices and common root, leaves both record and
rewrite subchecks valid and leaves the ontology role at
`REGION-REWRITING`. The original writer/rewrite carrier-ID intersection is
already empty. Same root, matching dimensions, and dataclass containment are
not a same-law compositional weld.

There is a related integrity defect: duplicating a continuation identifier
produces the nonempty issue
`ontology-continuation:duplicate:record-I`, yet record/rewrite remain valid and
the positive ontology role survives. Nonempty typing/index issues must be
fatal to the affected promotion.

## 6. Blocker C — complex conjugation is not load-bearing

The v4 quantum implementation writes the correct conjugated coefficient
formula, but its registered witness is insensitive to the distinction. With
`K_0=I/2`, `K_1=X/2`, `rho_+=(I+X)/2`, and `z=(1,i)`, the correct and
unconjugated constructions give the same tested scalar. Replacing
`coefficient.conjugate()` by the unconjugated coefficient in a changed source
still passes all 27 groups.

This violates the v4 hard requirement that conjugate transpose and coefficient
orientation be tested by a phase-bearing exact witness. A future scorer must
use a Gaussian-rational history family whose two orientations produce
different exact values, while retaining unit all-input division completeness
and the independent `P^dagger P` versus `P^T P` control.

## 7. Law-type wording correction

The Barandes distinction remains correct: ordinary transition probabilities
are lawful, but arbitrary inserted positive stochastic divisions need not
exist. One phrase must be narrowed. The law acts between complete
configurations and is conditioned at admissible division events/times;
`division configuration` must not be treated as a special configuration
species. This correction adds no APR evidence and does not identify division
events with stable ISP records.

## 8. Disposition and next authorized event

V4 is noncertifiable as a result-neutral scorer. Its artifacts are preserved
because their negative scientific content is exact and reproducible. They may
be cited only as the scoped negative baseline, never as evidence that the
synthetic joint-law or ontology-positive paths are valid.

The only authorized next event is an outcome-neutral scorer-only weld-repair
pin that binds:

- complete candidate-law bundles with transitions actually consumed by every
  claimed component;
- one typed conditioning-to-writer-to-rewrite-to-probe carrier chain;
- fatal handling of duplicate/missing/unresolved identifiers;
- exact reset-one, alien-carrier, duplicate-ID, and phase-bearing
  conjugation mutants;
- the corrected Barandes conditioning-event wording.

No fixture, physical law, primary vocabulary, precedence, scientific result,
ontology, or candidate paper may change. Candidate drafting and the three-seat
panel remain prohibited until a separately frozen successor scorer passes
independent post-freeze verification.

## 9. Ontology ceiling

APR still owns only a predeclared commutative prefix algebra, exact finite
restriction responses, raw syntactic atomlessness, and separate finite
controls. It has not constructed a horizontal regional process, physical
atomless referent, same-law contact/causal structure, dynamic locality,
indivisible relational stochastic law, geometry, backreaction, continuum,
metric, curvature, GR/QFT, particles, Hamiltonian, or actualisation. The one
actual relational web remains a candidate ontology, not a measured result.
