# RQ0-L0 architecture-reset and verifier-hardening pin

**Date:** 2026-07-31  
**Status:** PIN  
**Authority:** explicit user authorization from immutable HEAD `e247d34`  
**Scope:** public engineering, theorem correction and design only  
**Scientific L0 outcome:** forbidden in this cycle

## 0. Binding instruction

This is one bounded, forward-only RQ0-L0 architecture-reset and
verifier-hardening cycle.  It is not a held-out scoring cycle.  It may not
create, name, infer or score a new hidden fixture or hidden truth, and it may
not confer a positive or negative scientific L0 rung.

The cycle has exactly five events:

1. freeze this pin in its own commit;
2. construct a public-only proposer, trusted verifier, adversarial suite and
   overlap-first design at new paths;
3. commit one reviewable public architecture snapshot, without calling the
   estimator frozen;
4. dispatch and freeze one fresh external repo-read-only hostile review;
5. adjudicate that review and halt.

No post-review repair, estimator freeze or held-out authorization is implicit.
After adjudication the programme must request a new explicit user instruction
before any held-out cycle.

---

## 1. Immutable antecedents and reclassification

Every commit, file, receipt, report and disposition through v13 ledger #54 is
immutable.  In particular, no file from commits `4366531..e247d34` may be
edited or rescored.

The following are opened public regression objects only:

- order-192 `C2 x C3 x C4 x D4`;
- order-144 `C2 x C3 x C4 x S3`;
- all earlier `S3^3` and direct-product calibration objects.

They may test performance, arithmetic, regressions and adversarial behavior.
They can never earn a scientific rung in this or any later nominally held-out
cycle.

The terminal finite quantum fact-descent result at v13 ledger #22 remains
untouched.  This cycle concerns the still-unearned localization successor.

---

## 2. Corrected direct-factor lemma

Normal-direct-factor recovery is reclassified as a narrow finite theorem and
calibration lemma, not the ontology or definition of a region.

At the implemented exact finite scope the completeness claim must read:

> Subject to the declared type and cap bounds, the search enumerates every
> decomposition into **two through eight proper normal direct factors** that
> satisfies the implemented P1--P8 predicates.

It does not cover:

- the singleton ambient tuple;
- nonnormal factors;
- non-product overlap systems;
- operator-algebraic subsystems unrelated to a group direct product;
- general quantum locality;
- emergent space.

Every public note, proof and output created in this cycle must use the
corrected scope.

---

## 3. New raw boundary and exact schema

Create a new public architecture at new paths.  It may adapt opened objects
into a new raw schema, but the trusted verifier must consume serialized raw
data rather than estimator-internal dataclasses.

### 3.1 Exact schema discipline

Every mapping has a frozen set of required keys.  Missing and unknown keys are
errors.  Every scalar is checked by exact runtime type before conversion:

- booleans are exactly booleans, never strings or integers;
- integers are exactly integers, never booleans, strings or floats;
- handles and boundary labels are nonempty strings;
- sequences are arrays, not strings or generic iterables;
- optional values are explicit `null` or the declared exact type;
- duplicate handles, duplicate rows, duplicate map sources or targets and
  duplicate projector atoms are errors.

No `bool(...)`, `int(...)` or `str(...)` coercion is permitted at the trusted
boundary.

The dataset schema must type and validate at least:

- schema version and dataset handle;
- carrier dimension;
- declared boundary types and their compatible compositions;
- exact monomial amplitude laws;
- operation classes and independent-selectability declarations;
- the complete ordered composition table;
- row `tau`, status, result, independently serialized law and observed
  signature;
- preparations;
- operational contexts;
- probes;
- readouts and projector resolutions;
- record candidates and their complete record dynamics;
- gauge actions;
- access postulates.

Exact monomial laws must have the carrier dimension, a bijective permutation,
integer phase exponents in the declared exact cyclotomic modulus and a
recomputed signature.  Projector resolutions must be nonempty disjoint
partitions of the correct carrier.  Every referenced handle must exist and
every boundary assignment must satisfy the declared compatibility table.

The complete row table contains every ordered operation pair exactly once.
Implemented and collapsed rows carry an exact law and observed signature;
unavailable rows carry neither.  No unavailable row is replaced by a
synthetic product.

### 3.2 Strict cap type

The public total entry point accepts `cap_milliseconds` as an exact positive
integer, excluding booleans.  `None`, strings, floats, infinities and NaNs are
invalid.  Cap validation occurs inside the same outer fail-closed boundary as
parsing and all later stages.

---

## 4. Independent trusted verifier

Construct a trusted verifier in a module independent of the public proposer.
The verifier receives only:

1. the raw serialized dataset;
2. a raw claimed outcome;
3. raw claimed factor certificates and, when applicable, raw regional and
   factual maps.

It may share a tiny exact-arithmetic primitive module, but it may not import
the proposer, trust proposer dataclasses, or accept any of these as evidence:

- `certificate.passes`;
- membership in a supplied result list;
- an attached atlas;
- supplied obstruction prose;
- fixture novelty flags;
- declared expected factors or expected regional truth.

### 4.1 Certificate verification

For every claimed factor tuple the verifier reconstructs the quotient
composition object from raw rows and recomputes:

- P1 independently selectable generation;
- P2 mixed implementation in both required orders;
- P3 exact operational commutation;
- P4 injective and surjective multiplication onto the claimed product;
- P5 closure and inverse stability;
- P6 typed central/scalar intersections;
- P7 represented-algebra product equality;
- P8 stability under every declared restriction.

It also checks that every factor is proper and normal and that the tuple has
between two and eight factors.  Supplied booleans are ignored or forbidden;
the verifier emits its own predicate table.

For a claimed addressability negative, the verifier must itself exhaust the
declared finite search and find no passing tuple.  A prose obstruction is not
evidence.  A cap failure is procedural invalid, never a scientific negative.

### 4.2 Full `RegAddr` verification

Each raw regional arrow must be bijective or correctly injective/restrictive
at its declared type and explicitly map:

- operation classes;
- every complete composition row;
- row `tau`, status, source result, target result, exact law and signature;
- selectability and composite-only declarations;
- preparations;
- contexts and their complete field sets;
- probes;
- readouts;
- record candidates;
- record write/preserve/erase/no-write dynamics;
- projector resolutions;
- gauge actions.

The verifier recomputes source/target compatibility, law intertwining,
projector pullback, Boolean maps, identities and all direct-versus-composite
diagrams from the raw maps.  Every source field and row must occur exactly
once where a bijection is claimed.  Duplicating one map entry while omitting
another must fail.

### 4.3 Field-complete twisted triple

The public twisted control must contain three independently built full raw
amplitude instruments and three pairwise full-instrument isomorphisms.  The
verifier must first accept every pair map fieldwise.  It must then compose and
compare, not merely inspect, every mapped family listed in section 4.2.

The positive coherent triple has equality in every field.  The twisted triple
has valid pair maps but fails only the two-step-versus-direct loop equation.
A control with an invalid pair or a partial carrier/projector comparison does
not count.

---

## 5. One total fail-closed execution boundary

The public entry point places all of these inside one outer `try` boundary:

1. raw request/schema parsing;
2. cap validation and deadline construction;
3. proposal/estimation;
4. trusted verification;
5. neutral outcome resolution;
6. response serialization.

Every invocation must return exactly one structured engineering response.
Unexpected exceptions, serialization failures, timeouts, cap exhaustion,
missing or multiple outcomes and verifier disagreement return procedural
`ARCHRESET-INVALID` with exit code 1.  Nothing may escape the boundary.

The public engineering statuses are:

- `ARCHRESET-PUBLIC-PASS`, exit 0, only when the requested public claim is
  independently verified;
- `ARCHRESET-PUBLIC-SCIENTIFIC-NEGATIVE`, exit 0, only when the verifier
  independently proves the registered finite negative at its calibration
  scope;
- `ARCHRESET-INVALID`, exit 1, for every procedural defect.

These are engineering/calibration statuses, not RQ0 scientific outcomes.

---

## 6. Neutral public testing

The test harness must not require a positive main result.  Each case declares
which registered public outcome class is being exercised, then independently
checks that class.

Controls have three states:

- `PASS`;
- `FAIL`;
- `NOT-REACHED`.

An unreachable control is always `NOT-REACHED`; it is never counted in the
pass numerator.  Positive and finite scientific-negative public cases must
both be represented.  Procedural invalid cases must exit 1.

No gate may be a literal true declaration, a restatement of constructor
truth, or a comparison with a fixture-supplied expected outcome.

---

## 7. Mandatory adversarial public suite

Native end-to-end cases must include the exact hostile counterexamples:

- forged certificate with at least one failed P predicate;
- string `"false"` in an independently selectable Boolean field;
- gauge law with the wrong carrier dimension;
- invalid, overlapping, incomplete and out-of-range projector resolutions;
- incompatible context and record boundaries;
- duplicated regional row map with another row missing;
- `None` cap;
- `NaN` cap.

Also mutate every field of every raw schema object systematically.  For each
field exercise, as applicable:

- missing key;
- unknown extra key;
- wrong scalar/container type;
- empty required value;
- duplicate handle/source/target;
- dangling reference;
- out-of-range integer;
- dimension mismatch;
- incompatible boundary;
- corrupted exact law;
- corrupted observed signature.

Every mutation reruns the complete public entry point.  No positive response
may survive.  The audit must report mutation counts by schema path and failure
phase.

Opened order-192 and order-144 objects remain regression inputs only.  Static
inspection must reject proposer or verifier branches on their hashes, handles,
orders, factors, contexts, records or serialized fingerprints.

---

## 8. Overlap-first scientific-target reformulation

Write a design-only note.  It must not claim that the design has been
scientifically constructed.

The new target does not define every region as a product of globally recovered
factors.  For an amplitude instrument `D`, reconstruct two categories
independently:

### 8.1 Operational reconstruction

`OpSub(D)` is built only from composition, access and intervention structure.
Its objects are proper operational subinstruments closed under their admitted
rows and carrying their own restricted preparations, contexts, probes,
readouts and gauges.  Its arrows are executable full-field restriction or
embedding maps.  Direct-product factors may appear, but are not privileged.

### 8.2 Record reconstruction

`RecSub(D)` is built independently from candidates that pass W3 occurrence
and continuation-relative availability.  Its objects are record-bearing
subinstruments recovered from record dynamics and projector support, not from
the output of `OpSub(D)`.  Its arrows are exact record-dynamics and projector/
Boolean pullbacks.

### 8.3 Agreement gate

A public candidate passes the overlap-first architecture gate only if an
explicit functor or equivalence matches `OpSub(D)` and `RecSub(D)` while
preserving executable arrows, pairwise pullbacks and triple pullbacks.  Equal
record laws, equal handles or a common global factor label are insufficient.

Actual pair and triple intersections must be constructed as amplitude-
instrument objects with executable maps.  They may not be inferred by clique
completion or set intersection of planted atom labels.

Ambiguity returns a groupoid of admissible regional categories.  No arbitrary
representative is selected.

---

## 9. Mandatory public indecomposable model

Add at least one opened public exact model whose ambient operational
composition has no nontrivial global normal direct-product decomposition but
does contain overlapping record-bearing subinstruments.

The preferred calibration is the quaternion group `Q8` with its exact
two-dimensional monomial amplitude representation:

- the ambient composition is directly verified indecomposable under the
  corrected normal-direct-factor lemma;
- the three proper cyclic order-four subinstruments are recovered from
  operational closure rather than supplied as global product coordinates;
- their pair and triple intersection is the central order-two subinstrument;
- every region and intersection is record-bearing under independently checked
  W3 candidates;
- all inclusion and pullback maps are executable and field-complete;
- the operational and record reconstructions agree;
- no global direct-product regional decomposition is claimed or available.

Another exact indecomposable model is permitted only if it satisfies every
listed property.  This is a public architecture/calibration model, never a
scientific L0 result.

Public direct-product models remain positive controls for the narrow lemma.
Include an operational model with no admissible overlap-first agreement as a
finite negative control.

---

## 10. Public artifacts and forbidden paths

Permitted new paths include:

- `note-rq0-operational-localization-architecture-reset-pin.md`;
- `note-rq0-operational-localization-overlap-first-design.md`;
- `note-rq0-operational-localization-architecture-reset.md`;
- `code/rq0_l0_archreset_exact.py`;
- `code/rq0_l0_archreset_verifier_exact.py`;
- `code/rq0_l0_archreset_public_models.py`;
- `code/rq0_l0_archreset_public_audit.py`;
- `code/rq0_l0_archreset_public_audit.json`;
- `code/rq0_l0_archreset_public_output.txt`.

The JSON and text outputs are public engineering audit artifacts, not
scientific or official held-out receipts.

Forbidden in this cycle:

- any new `heldout`, `hidden`, `official`, `score` or scientific-delivery
  path;
- any hidden factor, context, record or atlas truth;
- any estimator-freeze declaration;
- any RQ0 scientific outcome;
- any edit to antecedent estimator, proof, fixture, scorer, receipt, delivery,
  review or adjudication artifacts.

---

## 11. Public review snapshot and hostile round

After local public tests pass, commit a reviewable public architecture
snapshot.  Committing provides an immutable review referent but does not
freeze or validate the estimator for future held-out use.

Then dispatch one fresh external repo-read-only hostile reviewer.  The
reviewer must not import the proposer or verifier into its independent checks
and must attack at least:

- strict schema coverage and every coercion path;
- the total boundary, including cap and response serialization;
- trusted-verifier independence;
- P1--P8 recomputation and corrected completeness scope;
- neutral positive/negative/invalid outcomes and `NOT-REACHED` accounting;
- bijective full-field `RegAddr` maps;
- the coherent and twisted full-field triples;
- systematic schema mutations;
- the indecomposability and overlap maps of the public non-product model;
- independent recovery and agreement of `OpSub(D)` and `RecSub(D)`;
- circularity, constructor-truth and hard-coded-handle branches;
- every claim in the public design and architecture notes.

The report must return `ACCEPT`, `ACCEPT-WITH-FIXES` or `REJECT`, ranked
findings and independently reconstructed evidence.  Freeze it verbatim,
adjudicate it separately, and halt.  Do not repair findings during or after
the review in this authorized cycle.

---

## 12. Claim ceiling and stopping rule

The strongest possible conclusion is only:

> A public architecture candidate and independent verifier survived or failed
> a pre-freeze hostile review.

It is not:

- `RQ0-LOCAL-ATLAS`;
- `RQ0-LOCALIZATION-GROUPOID`;
- an L0 no-go;
- a manifold, topology or spatial claim;
- influence or causality;
- Lorentzian geometry or spacetime;
- a field or gravity result.

`RQ0-T1`, `RQ0-C1`, topology, influence, causality, geometry, spacetime,
fields and gravity remain prohibited throughout.

After the hostile report is frozen and adjudicated, stop and request explicit
user authorization for any future held-out cycle.
