# JCV hostile review — gravity, covariance, and composition seat

Target commit: `35c2511657efbee6c1c1887f2d7626faa4d396ea`  
Seat: **G — GRAVITY / COVARIANCE / COMPOSITION**  
Grade: **ACCEPT-WITH-FIXES**

## Executive verdict

The frozen finite algebra survives. I independently reproduce all five target
artifact hashes, the total receipt seal, the gauge quotient, every nonempty
sector and dimension, both rational active witnesses, the homogeneity control,
and both classifier words. **There are zero numerical, algebraic, hash, seal,
orbit, witness, dimension, or classifier discrepancies.** The exact candidate
primary `JCV-STRATIFIED` and the active-locus word
`JCV-PAIRING-SELECTED-WEIGHTS-FREE` follow from the frozen table at the
registered finite scope.

The gravity interpretation requires repairs, but not rejection of that exact
primary. What the unit has selected is one flat holonomy class among calibrated
two-channel coordinate dictionaries, conditional on an active full-rank law.
It has not earned a comparison map from carrier physics, constructed a
refinement system, or formed a record-generated fixed point. In particular:

1. the declared comparison maps have an operational coordinate-dictionary
   referent, not an independently derived cross-carrier physical referent;
2. the active pairing result is already forced when each triangle has a
   full-rank law—the shared-law homogeneity declaration removes only two dark
   mixed-handoff sectors;
3. two adjacent triangle checks do not supply associativity, cylindrical
   consistency, or global extension; and
4. the law/record/comparison circularity is not instantiated by a self-map, so
   the words `fixed point` and `deepest circularity narrowed` outrun the
   certificate.

The paper's explicit walls against geometry, backreaction, covariance,
Lorentz, continuum, GR, constants, particles, and phenomenology otherwise
hold. I find no hidden quantum-gravity promotion.

## Independence, read set, and tools

I did not read, list, receive, or ask about either other JCV reviewer report. I
did not import `jcv_score.py` as an oracle. I first rebuilt the quotient and
solution sectors analytically and with a separate standard-library script;
only afterward did I inspect the frozen decision functions and repair delta.

Read set:

- `v16/note-jcv-hostile-protocol.md` — complete;
- `v16/note-jcv-pin.md` — complete;
- `v16/code/jcv_fixture.json` — complete;
- `v16/code/jcv_score.py` — complete, plus the historical scorer diff;
- `v16/code/jcv_output.txt` — complete;
- `v16/code/jcv_receipt.json` — parsed in full as JSON; all top-level sealed
  values were independently hashed, with detailed inspection of the gauge,
  solve, witness, instrument, classifier, consequence, scope, read-set, and
  manifest payloads;
- `v16/paper-02-joint-comparison-fixed-point.md` — complete;
- `v16/note-jcv-official-run-failure.md` — complete;
- `v16/note-jcv-scorer-repair.md` — complete;
- `v16/note-jcv-solver-freeze.md` — complete;
- `v16/note-jcv-solver-postcommit.md` — complete;
- `v16/note-jcv-postcommit-verification.md` — complete;
- JCV entries in `v16/LOG.md` at the immutable target;
- relevant typed-boundary/refinement/fixed-point passages of
  `v16/paper-01-joint-relational-history-law.md` and
  `v16/note-jrh-delta-adjudication.md`;
- relevant local-versus-extension passages of
  `v13/paper-coc-cocycle.md`;
- the record definition, Theorem 4.1, decision criterion, and legitimate-
  division scope passages of `v12/paper1-composition-defect.md`;
- the four primary external papers named by the candidate, through their
  arXiv primary texts.

Tools and runtime:

- `/opt/homebrew/bin/python3.13`, using only `fractions.Fraction`, `itertools`,
  `json`, and `hashlib` in the independent reconstruction;
- `sha256sum`, `git show`, `git diff`, `rg`, `sed`, and `wc`;
- primary-source inspection through arXiv's abstract/HTML texts;
- no floating point, numerical root finder, random sample, third-party CAS, or
  candidate scorer import in the independent calculation.

## Artifact and seal audit

All five protocol hashes match exactly:

| artifact | frozen SHA-256 | independent result |
|---|---|---|
| fixture | `ad887c213d14781838c6e70227b8f2c162f1392a08060de7c6e57829a8db012b` | MATCH |
| scorer | `66b87bdf68f7210d959e13bfacae4c5957413e6d8f234647bfe3ad4a19619a03` | MATCH |
| paper | `b54858c394fe22626ef1e233781737b7199cc56bf816f52e8aae063a99deaefc` | MATCH |
| transcript | `b1d950c804c8b568514f1a0206853496b2f578650a3d98187e64c1c8a9b70d6d` | MATCH |
| receipt | `a1b0baeee418d3f2c82e1ec6d07993cb51f69f3f51d63a9996dae9fb177fe3d1` | MATCH |

The receipt has 17 keys excluding `seal_manifest`; its manifest declares 17,
contains exactly those 17 keys, and every SHA-256 of the canonical JSON value
matches. There are no missing, extra, or edited sealed keys. The paper and
transcript byte hashes also match the values sealed inside the receipt.

The frozen source-anchor hashes for the solver, public receipt, pin, and
solver-postcommit note also match. The pre-repair scorer is independently
`768c4bbc6b0e39436a6d6b7dcf026149f95c2e8bb931d080052262638827f692`;
the repaired scorer is the protocol hash above.

## Independent exact reconstruction

### 1. Gauge quotient and holonomies

For either eigenchannel, the comparison graph has `V=4`, `E=5`, is connected,
and therefore has cycle rank `E-V+1=2`. There are `2^5` raw edge signs. Vertex
rephasing has an image of size `2^(4-1)=8`, since the common vertex sign is the
kernel. Thus each channel has `2^2=4` gauge classes. The two channels are
independent, giving:

- raw assignments: `2^10 = 1024`;
- orbit size: `8^2 = 64`;
- quotient sectors: `1024/64 = 16`.

The two triangle products in each channel generate the cycle quotient, so the
four registered `q` values are a complete invariant for this declared graph
and gauge—not merely a count-compatible label.

Writing a triangle's direct-edge sign as `e`, the raw defect obeys

`ac-e = e(ace-1) = e(q-1)`.

The analogous identity holds for all four channel/triangle defects. This gives
`4*1024=4096` exact raw-to-quotient checks. The matrix formula

`P_ij = E_j diag(s_plus,s_minus) E_i^T`

is orthogonal and intertwines the registered observable. Path composition
multiplies the two channel signs and equals the direct map exactly when both
triangle holonomies are `+1`. This independently explains the reported 40
local checks (`5 edges * 4 sign pairs * 2 identities`) and 2048 path checks
(`1024 assignments * 2 triangles`).

### 2. Shared-law solution

Order the holonomy key as
`(q012_plus,q012_minus,q123_plus,q123_minus)`.

- If either plus holonomy is `-1`, cut equality forces `x=u=0`.
- If either minus holonomy is `-1`, it forces `y=v=0`.
- Completeness forbids both columns from vanishing.

Therefore the shared model has exactly seven nonempty keys:

`(-1,1,-1,1)`, `(-1,1,1,1)`, `(1,-1,1,-1)`,
`(1,-1,1,1)`, `(1,1,-1,1)`, `(1,1,1,-1)`, and
`(1,1,1,1)`.

The first six have one whole column zero and reduce to a circle, so each has
algebraic dimension 1, determinant zero, and `xy=0`. The all-plus sector obeys
two independent equations in four weight variables and has algebraic dimension
2. Its nonzero locus `(xv-yu)xy != 0` is inhabited by the displayed rational
witnesses, so the algebraic statement also has a real certificate.

The other nine holonomy sectors are empty and carry the receipt's empty
dimension `-1`. Thus every shared-sector dimension is reproduced.

### 3. Independent-triangle control

A triangle with both channel holonomies `+1` contributes dimension 2; one
surviving channel contributes dimension 1; no surviving channel is empty. The
product control is nonempty exactly when neither triangle has key `(-1,-1)`.
Hence there are nine sectors:

- four dimension-2 sectors (one live channel at each triangle);
- four dimension-3 sectors (one full triangle and one one-channel triangle);
- one dimension-4 sector (both triangles full).

The two control-only keys are exactly
`(-1,1,1,-1)` and `(1,-1,-1,1)`. Thus the shared declaration excludes two of
nine control sectors and leaves seven. Every reported control dimension and
count is reproduced.

### 4. Active witnesses and all-input completeness

For the two active witnesses:

| `(x,y,u,v)` | norm equation | orthogonality | `Delta` | `Delta*x*y` | `p_plus` |
|---|---:|---:|---:|---:|---:|
| `(12/25,-12/25,16/25,9/25)` | `1` | `0` | `12/25` | `-1728/15625` | `0` |
| `(16/25,-9/25,12/25,12/25)` | `1` | `0` | `12/25` | `-1728/15625` | `49/625` |

Both are real, exact, active, and give distinct calibrated responses. For all
inputs—not just these witnesses—

`K0^dagger K0 + K1^dagger K1`

equals

`(x^2+y^2+u^2+v^2) I + 2(xy+uv) Z = I`.

The six dark witnesses use the rational circle point `(3/5,4/5)` in their one
live column and satisfy the same identity. This reproduces all eight witness
rows and zero instrument failures.

### 5. Frozen classifier

The independently reconstructed summary is:

- nonempty `7`, active `1`, dark `6`;
- active maximum dimension `2`;
- calibrated observable moves: true.

The frozen decision table assigns a single active positive-dimensional class
with observable movement to
`JCV-PAIRING-SELECTED-WEIGHTS-FREE`; its separate compound rule assigns any
mixture of active and dark nonempty strata to `JCV-STRATIFIED`. Both words
therefore follow from the table rather than the paper's prose.

## Gravity/covariance/composition findings

### G1. The comparison map is a declared dictionary, not an earned carrier fact

The exact map is physically well typed as a real two-dimensional isometry
intertwining one calibrated binary observable. That earns a coordinate
dictionary. It does **not** earn the proposition that two actual carrier
rewrites encode the same unread fact. No carrier rewrite, continuation algebra,
record extractor, second held-out boundary observable, or independent transport
experiment appears in the fixture. The phrase `same declared unread boundary
fact` in the pin is doing the ontological work.

This is not a hidden arithmetic defect: it is exactly why the paper's
`CONDITIONAL-PARTIAL` qualifier is necessary. On the active locus, the only
surviving holonomy is flat, so no pairing alternative moves an observable. On
the dark loci, differing holonomies are silent by construction. The measured
movement `0 -> 49/625` is movement among **weights on the one flat class**, not
an experimental calibration of a cross-carrier comparison.

The smallest repair is terminological: call `P_ij` a *declared calibrated
inter-chart comparison* and call the result
`ACTIVE-CUT-COMPATIBLE-HOLONOMY-UNIQUE` in explanatory prose. Reserve
`cross-carrier physical comparison` for a successor in which actual rewrite
outputs generate the boundary algebras and a held-out continuation tests the
identification.

### G2. Active selection is homogeneity-independent

The paper accurately says homogeneity is declared and prices its effect as two
sectors. It does not, however, state the strongest exact control conclusion.
If each triangle has its own independent full-rank law, then each triangle
already forces both of its holonomies to `+1`; the only doubly active control
key is still `(1,1,1,1)`. Numeric reuse of the same `W` is not needed for the
active pairing result.

Shared `W` removes only the two rank-deficient mixed handoffs where one
triangle uses the plus channel and the other uses the minus channel. The honest
secondary statement is therefore:

`ACTIVE PAIRING SELECTION: HOMOGENEITY-INDEPENDENT; DARK STRATIFICATION:
HOMOGENEITY-DEPENDENT.`

There is a second covariance issue. Equality of the arrays called `W` at two
different charts is equality in a chosen trivialization. A physical
homogeneity law should transport local law data between interfaces, or derive
both arrays from one local relational rule. The control compares `W0=W1` with
unrelated `W0,W1`; it does not test a nontrivial transport law. No homogeneity,
translation symmetry, or covariance principle follows.

### G3. Two triangles are local coherence, not associativity or global closure

The current graph genuinely improves on a one-triangle fixture: it checks two
independent cycle generators sharing an edge. It is nevertheless only the
cycle quotient of that five-edge graph.

A smallest exact extension countermodel makes the limit visible. Set every
existing edge sign to `+1`, so all four current holonomies are `+1`, and use
either active rational witness above. Add a direct `03` comparison edge. The
existing paths `0-1-3` and `0-2-3` both have plus-channel sign `+1`. Give the
new direct edge signs `(-1,+1)`. The old JCV fixture still passes unchanged,
but each new triangle containing `03` has plus holonomy `-1`; the active
law has nonzero plus-column amplitudes and therefore fails the new cut
equality. Choosing `(+1,+1)` instead gives a coherent extension.

This proves neither a global obstruction nor global success. It proves that
the old solution does not determine the next overlap. Within the same freely
solved abelian sign doctrine a flat extension always exists, but an actual
carrier-generated edge could supply the incompatible sign. A nonabelian or
dimension-changing refinement system could impose still different conditions.

The inherited v13 COC result is the apt internal warning: closure at one
declared atlas did not control the extension-orbit atlas. JCV should therefore
retain `LOCAL-TWO-TRIANGLE` in every positive scope tag.

### G4. The record-generated circularity is untouched at its load-bearing edge

JCV solves simultaneous polynomial constraints in `(q,W)`. That is valuable,
but it is not a fixed point in the sense proposed by paper 01. There is no map
that:

1. uses the law to generate durable record partitions;
2. uses those records to decide which boundaries are identical or orthogonal;
3. uses that resulting comparison structure to type and coarse-grain the law;
4. reproduces the original law and comparisons under refinement.

The two outcome rows are declared durable. The history columns are declared
coherent. The comparison doctrine is declared before the law. Thus the
law-to-record-to-comparison-to-law loop is not run even once. Solving
`W*r=0` only narrows compatibility inside its externally supplied middle
arrow.

This distinction matters in light of the v12 record theorem: there, a record
structure is tested from support correlation and future availability before
the composition defect is evaluated. JCV does not derive its durable rows or
pairing from analogous process facts. It therefore cannot yet claim that its
own record structure reproduces the typing it presupposed.

The smallest prose repair is to replace `fixed point` with `joint compatibility
variety` in the title, abstract, and conclusion, and to replace `the deepest
circularity has been narrowed` with `one algebraic compatibility subproblem
inside the circularity has been solved conditionally`.

### G5. No gravity or covariance result escaped the wall

The four chart-sign gauges are basis rephasings, not diffeomorphisms. The
triangle products are graph holonomies, not spacetime curvature. The fixture
contains no relation rewrite, causal order, metric, matter flux, stress-energy,
branchwise geometric constraint, held-out propagation response, dimensional
scale, or continuum/refoliation algebra.

Accordingly, it establishes none of the following:

- gravitational backreaction or even matter-geometry co-presence;
- general covariance, Lorentz symmetry, or Lorentz violation;
- a continuum or GR limit;
- an affine/cosmological constant or any dimensionful scale;
- particles, species, a vacuum, scattering, or an all-arity interaction law;
- a Hamiltonian or generator;
- a QFT/GR deviation or phenomenological observable.

The paper refuses or leaves open every one of these, and I find no sentence
that promotes one as a result. The abstract's phrase `relational-carrier
histories` is rhetorically ahead of the fixture, but the immediate and repeated
disclaimers prevent it from becoming a substantive gravity claim.

## Primary-source analogy audit

These findings use the cited papers only to audit attribution. The comparisons
below are my inferences; JCV does not instantiate the cited frameworks.

- **Cylindrical consistency.** Dittrich's programme uses a partial ordering of
  coarse and fine discretizations, embedding maps from coarse boundary data to
  fine data, and invariance of predictions under refinement; it also emphasizes
  that dynamics should select/adjust the embeddings
  ([arXiv:1205.6127](https://arxiv.org/abs/1205.6127)). JCV has none of the
  partial order, coarse/fine state maps, refinement pushforward, or dynamics-
  selected embedding. The paper's word `analogous` is acceptable only as a
  motivation for a future test.

- **Quantum causal histories.** Hawkins, Markopoulou, and Sahlmann assign
  matrix algebras to events in a causal pre-spacetime and CP maps to causal
  relations, subject to extension, spacelike-commutativity, and composition
  axioms ([arXiv:hep-th/0302111](https://arxiv.org/abs/hep-th/0302111)). JCV
  has a fixed-boundary instrument and isometric comparison dictionaries, but
  no causal set or those three axioms. `Resemble` is safe only at the very broad
  algebra/channel level.

- **Quantum measure.** Dowker, Johnston, and Surya study a strongly positive
  decoherence functional/quantum measure on an event algebra, the associated
  histories Hilbert space and vector measure, and the nontrivial extension
  problem ([arXiv:1007.2725](https://arxiv.org/abs/1007.2725)). JCV constructs
  none of those objects. Its two coherent columns and record vocabulary are
  compatible with that motivation, but `use of complete histories and record
  cuts` is too strong for this fixture; it should read `motivated by`.

- **Pentagon coherence.** Levin and Wen's pentagon identity equates two
  different sequences of fusion/recoupling moves with sums over intermediate
  labels; it is a self-consistency condition on `F` data
  ([arXiv:cond-mat/0404617](https://arxiv.org/abs/cond-mat/0404617)). JCV's two
  path-versus-direct triangles have no associator, fusion spaces, competing
  parenthesizations, or pentagon. Calling them a `minimal coherence check` is
  fine; calling them associativity evidence would not be. The paper should say
  `graph-cocycle check reminiscent only at the diagrammatic level`.

## Serializer-repair chronology

The git chronology is real and the physical rule did not move:

1. fixture/scorer freeze: `ee8e414c2e354b5447af57efedbe234ae12af111`;
2. failed-run record: `b0c0d244de3b1344a2a9e72c234460ebd0f2a670`;
3. scorer repair refreeze: `c561acc03e0837f7e72508a1e5aad06a8c75d2ff`;
4. candidate as-is: `ab2102a0f452b5760674946cecf5e9b581986bde`.

The complete scorer delta is exactly one three-line serializer branch for
`set`/`frozenset`, recursively canonicalized and sorted. The fixture,
equations, witnesses, classifier, renderer, and promotion paths did not move.
This repair could not tune a physical answer, and I find no evidence that a
human saw a physical value before refreeze.

One procedural sentence needs correction. In the frozen code, `build()` runs
`run_core()`, classifies the physical solution, and renders the paper **before**
entering `mutation_survey()`, where the set-serialization exception occurred.
Thus the first process computed a classifier and paper in memory. It did not
print, serialize, promote, or expose them in the traceback. The failure note's
claim `No physical value or classifier word was printed or promoted` is exact;
the stronger status phrase `FAILED-BEFORE-VERDICT` is true only if `verdict`
means an exposed artifact, not an internal classification.

I do not treat this as result leakage because the traceback contains no result
and the sole repair is mechanically forced. The smallest repair is a chronology
disclosure: `failed after internal classification but before result exposure,
serialization, or promotion`. Future scorers should run infrastructure and
mutation-survey serialization gates before physical classification. Also,
`P-CHRONOLOGY` is currently a hard-coded `True`; git history supplies the
evidence, not that runtime gate.

## Sentences stronger than their certificate

The following are the complete material scope excesses I found:

1. **Title:** `A joint comparison/law fixed point...` — no fixed-point map is
   present. Repair to `A joint comparison/law compatibility variety...`.
2. **Abstract/ontology:** `alternative relational-carrier histories` — the
   fixture contains chart encodings standing in for hypothetical alternatives,
   not carrier rewrites. Add `represented here only by declared charts`.
3. **Exact solution:** `physical weight freedom` — correct inside the fixed
   calibrated interface because `p_plus` moves, but not a fundamental physical
   coupling. Add `within this fixture`.
4. **Selection paragraph:** `cut equality plus reuse of one nonfactorizing law
   selects...` — reuse is unnecessary on the doubly active locus. State that
   full rank at both triangles selects flat holonomy; reuse only removes two
   dark handoffs.
5. **Existing-approaches paragraph:** `use of complete histories and record
   cuts` — no complete-history event algebra is constructed. Replace `use` with
   `motivation by`.
6. **Final sentence:** `the deepest circularity has been narrowed` — the
   record-generated loop is not instantiated. Replace with the conditional
   compatibility wording in G4.

The subjective sentence `That is a real advance...` is not a theorem. It is a
reasonable methodological assessment if explicitly labelled as such.

## Smallest binding repairs

No equation, sector, witness, receipt, classifier, or primary word should
move. The minimal repair set is:

1. rename `fixed point` to `joint compatibility variety` and demote the
   circularity sentence;
2. bind comparison maps to `declared inter-chart dictionaries`, not earned
   carrier identifications;
3. record the stronger control result: active selection is homogeneity-
   independent; only two dark handoffs are homogeneity-dependent;
4. add the explicit `03`-edge extension countermodel and the scope tag
   `LOCAL-TWO-TRIANGLE`;
5. sharpen the four external analogies as described above;
6. correct the failed-run chronology to distinguish internal computation from
   exposed/promoted truth and disclose that `P-CHRONOLOGY` is not itself an
   evidentiary check.

The smallest next scientific construction is not another sign census. It is a
typed three-overlap refinement diagram built from actual relation rewrites,
with comparison maps generated from their durable boundary record/continuation
algebras; a transported rather than numerically copied local weight law; two
different multi-step compositions required to agree; and a held-out
continuation whose result changes if the proposed identification is wrong. The
record extractor, comparison structure, and coarse law must then be iterated
and shown to reproduce one another. Only that would deserve `record-generated
fixed point`; only after a genuine relation/transport response would a gravity
seat become positive.

## Discrepancy ledger and grade

- Artifact-hash discrepancies: **0**.
- Total-seal discrepancies: **0**.
- Gauge-orbit/holonomy discrepancies: **0**.
- Shared-sector key/count discrepancies: **0**.
- Independent-control key/count discrepancies: **0**.
- Algebraic-dimension discrepancies: **0**.
- Rational-witness/equation discrepancies: **0**.
- All-input completeness discrepancies: **0**.
- Calibrated-probability discrepancies: **0**.
- Frozen-classifier discrepancies: **0**.
- Material conceptual/scope repairs: **6**, listed above.
- Evidence of physical-rule movement in serializer repair: **0**.
- Evidence of human-visible pre-refreeze result leakage: **0**.
- Evidence that the first failed process internally computed the result before
  the serializer exception: **1 exact code-order finding**, requiring the
  chronology wording repair above.

**Final grade: ACCEPT-WITH-FIXES.** The exact finite primary survives. The
paper must not be terminalized under `fixed point`, cross-carrier physical
selection, homogeneity-derived active coherence, or any global/covariant
reading until the six binding repairs are adjudicated.

Report SHA-256 is intentionally reported externally at freeze/delivery rather
than embedded self-referentially in these bytes.
