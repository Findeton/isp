# APR Paper 12 — v3 black-box verification failure

**Date:** 2026-08-19

**Status:** V3 ARTIFACTS AUTHENTIC AND REPRODUCIBLE BUT NOT CERTIFIABLE

**Disposition:** REPAIR REQUIRED; CANDIDATE AND PANEL REMAIN PROHIBITED

## 1. Frozen v3 evidence

The scorer source was committed before its first v3 fixture evaluation at
v16 #171 (`1361ed8`). The committed source and resulting artifacts are:

| object | SHA-256 |
|---|---|
| `v16/code/apr_score.py` | `3284484d91f83440f9472ba9e9605b90065bfa0c30094b9225806ee01724fef8` |
| `v16/apr_output_v3.txt` | `d8efb23720fb38188b3ecd4ed38b2e15a16b20e18a525f8627676edae7f6b122` |
| `v16/apr_receipt_v3.json` | `925681dfa1adc688bf36920d064483ccadcf7940fd6ff6bf177d55d96733c70c` |
| canonical receipt payload | `07090a2c420bae91f003cecae030ca2832dd365324cade7decfe6d696963d67c` |

Repository-root, alien-working-directory, and true off-tree/no-`.git` runs
produce byte-identical transcript and receipt. The payload self-hash
recomputes exactly, an independently assembled transcript is byte-identical,
and a second attempt at the official destinations refuses without changing
either file. Strict CLI, transactional publication, frozen-input hashes, and
all 56 transformation descriptors pass.

The required disclosure is present in both artifacts:

```text
blinding_status: RESULT-KNOWN-BEFORE-V3-IMPLEMENTATION
exposure_debt: PERMANENT-PREFREEZE-M01-AND-ALL-MUTANTS-EXPOSURE
v3_source_frozen_before_v3_run: true
```

V3 froze before its own run, but it is not pre-truth or mutually blind.

## 2. Robust scientific result

Independent reconstruction again returns:

```text
APR-BLOCKED-AT-BOUNDARY-GLUING
```

This primary does not depend on any failed positive-path test:

- raw prefix syntax is atomless, but no physical quotient is constructed;
- the restriction response is normalized on the full valuation cone;
- the active process domain is B0--B3, with only the assigned empty-tree
  identity `qw_000 -> hf_015` at B0 and no identities at B1--B3;
- no total adaptive-frontier constructor, filling-to-process assignment,
  tensor factory, or nontrivial vertical/horizontal naturality square exists;
- the valid prefix-free frontier `{0,10,110,111}` is absent;
- `og_000` and `og_001` have the same four uniform `AB` and `BC` marginals
  `1/4`, but `P(A=C)=1/2` versus `1`; no frozen law selects one extension.

The artifact correctly reports `process=STATIC-RESPONSE-ONLY`, measured
`ontology_role=STATIC-RESPONSE`, separate
`ontology_candidate=POSTULATED-CANDIDATE-RELATIONAL-WEB`, contact and
causality `PRICED`, one-law provenance `UNCONSTRUCTED`, and the exact
syntax-only qualifier. It makes no geometry, gravity, continuum, GR/QFT,
particle, Hamiltonian, or actualization claim.

## 3. Independent verification ledger

The independent black-box verifier is:

```text
/private/tmp/apr_v3_independent_blackbox.py
SHA-256 f3ca964721b51bd9071a80a5a817d624e0d092f35ef1b70b7af6f0f71ce02685
```

Its full result ledger is:

```text
/private/tmp/apr_v3_independent_result.json
SHA-256 63de0b3a4fcda9973225b364ea1f30b81b8d4594e13707027b5c94ed99e47fac
```

The verifier imports no scorer functions and uses the scorer only as a
subprocess/source-under-audit. It independently reruns the frozen v2 verifier
against the v2 bytes (`197 PASS / 7 historical FAIL`), confirms that all seven
scoped v3 repairs are green, and checks the v3 descriptors and integrity. Its
v3 ledger is:

```text
307 PASS / 4 FAIL
```

## 4. Four binding failures

### 4.1 Classical process promotion is not semantic

The positive synthetic package declares B0/B1 frontiers `{epsilon}` and
`{0,1}`, while its nonidentity assigned map uses unrelated carriers
`{s0,s1}` and `{t0,t1}`. Only one nonidentity map exists, so no genuine
sequential composite or alternate cut can be reconstructed. Composition,
cut, tensor, interchange, and naturality accept caller-supplied equal JSON
objects; positivity, affinity, and mass preservation accept booleans.

An exact changed-source control replaces every equation by the same opaque
copy object. All 27 synthetic self-tests still pass. Therefore
`HORIZONTAL-CLASSICAL` can be manufactured without one typed process.

### 4.2 Quantum completeness is not unit-normalized

The quantum validator requires positive branches to sum to a supplied
`total`, but never requires that total to be the identity or the conserved
typed unit. Branches `I,I` with total `2I` still earn
`HORIZONTAL-QUANTUM`. Recovery and coherent-cut rows are also accepted as
opaque equal objects rather than being derived from the same histories and
division law.

### 4.3 Contact and causal influence are supplied, not generated

The positive contact fixture uses identity-shaped schedule/reader data while
supplying distinct normalized before/after distributions. Intervention
alternatives are never applied through the schedule to the reader. The
validator checks inequality and shared root strings, so an arbitrary response
can earn generated contact. Provenance records a declaration; it does not
derive dynamics.

### 4.4 Ontology record/rewrite promotion is supplied, not generated

The alleged writer is identity-shaped on the record bit and is promoted by a
disconnected `record-write` label. Region rewriting accepts a changed region
token plus separately supplied response distributions under a common root,
without composing a same-law rewrite into a later probe. The baseline
`STATIC-RESPONSE` diagnosis is correct, but the required generic positive
role ladder is not certified.

The independent physics audit also confirms that the generic classifier can
consume shallow/bare positive evidence for higher rungs. A result-neutral
scorer must instead consume typed measurement objects produced by the same
law; a provenance path or `present:true` cannot fill a missing construction.

## 5. Ordered repair

The next scorer must, synthetically and without adding APR physics:

1. type exact stochastic maps against declared boundary frontiers and
   recompute identity, a genuine composable nonidentity pair, alternate cuts,
   positivity, mass preservation, tensor/interchange, and naturality;
2. derive quantum history/division operators from that same typed law and
   require `sum_j L_j^dagger L_j = I` exactly, with an operational same-law
   interference witness and stable division;
3. derive influence distributions by inserting each intervention into a
   typed schedule and applying a typed later reader;
4. replace bare capability booleans by typed measurement objects at every
   classifier rung and require shared semantic roots;
5. derive record-writing and region-rewrite responses by composition in the
   same process before promoting the ontology role.

Deleting the positive branches is not a lawful repair under the frozen
positive-path addendum. The next event must be a new, separately frozen,
scorer-only semantic-repair pin followed by source freeze before any v4
fixture evaluation. V3 artifacts remain immutable and cannot support the
candidate or three-seat paper panel.

## 6. Ontology ceiling

APR presently owns one predeclared commutative prefix algebra, exact finite
static restriction responses, and raw syntactic atomlessness. The proposed
actual partial web of durable relational facts remains a postulate. No
horizontal regional process, physical atomless regional referent, generated
contact or causal order, dynamic locality, geometry, matter--geometry
backreaction, continuum, metric, curvature, GR/QFT, Hamiltonian, particles,
or actualization has been constructed.
