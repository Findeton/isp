# v13 RQ0-L0 — operational localization and overlap-discovery pin

**Status:** PIN, STRICT, 2026-07-30.
**Authority:** the user's post-terminal review accepted at v13 #23 and Paper
0 v0.3, committed as
`10dc6b27c1d85ad124214c5df43186e5979c0c61`.
**Predecessor gate:** terminal `RQ0-FACT-DESCENT` at v13 #22, commit
`9d8828bc66c186d199ab1fdbe0b91bb987d46db2`.

## 1. Question and ceiling

This unit asks one question:

> Can proper local quantum subinstruments and their nontrivial overlap
> structure be reconstructed from finite operational amplitude laws without
> reading qubit names, circuit wires, planted tensor factors, construction
> labels, coordinates, causal graphs, metrics, or fields?

The target is a gauge-invariant localization object

$$
\operatorname{Loc}(D)
$$

whose objects are operationally individuated quantum subinstruments, whose
arrows are restriction or operational-isomorphism maps, and whose meets or
overlap spans produce a nontrivial finite nerve.  When operational symmetries
prevent a unique presentation, the target is a groupoid of admissible
localizations rather than a selected representative.

The strict ceiling is localization.  This unit must not define or claim:

- influence, signalling, screening, causal precedence, a causal cone, or a
  directed acyclic graph;
- spacelike separation, spatial distance, dimension, volume, topology of a
  manifold, a Lorentzian metric, or special relativity;
- a field propagator, microcausality, a stress object, backreaction, gravity,
  or any deformation algebra.

Operational co-addressability or commutation is not called spacelike
separation.  Instrument composition order is not called causal order.
`RQ0-C1` remains unpinned and may not begin in this unit.

## 2. Anchors and exact inherited scope

Before construction, reproduce or authenticate the following immutable
anchors and classify each reuse as theorem, lemma, fixture, control, or
benchmark:

1. **Paper 1 / W3:** `v12/paper1-composition-defect.md`, terminal commit
   `279a34b4f49209d2e6d2085bea28560122cc6b80`, SHA-256
   `81bdab5673fb67b63cd10c08fbb80870f8aa01088047718c5b4bf447e1669128`.
   Inherit the H-corr/H-avail record-seam decision procedure,
   continuation-relative availability, and the composition-compatible
   boundary-gauge lesson.  Records must be derived from the same process
   family, never attached afterward.
2. **Paper 2 / W6:** `v12/paper2-record-coreference.md`, terminal commit
   `a0dadd5122c88f69f37fcc6cc6b024051649790a`, SHA-256
   `d6af0e6513fc7088407dc5a26c513ecc4e9e45b5a5ae71ffa8a9571f274ad670`.
   Inherit that fact co-reference is distinct from token co-reference; law
   equality is insufficient; phase is forbidden as a fact-identity
   criterion; erasure does not erase historical occurrence; and exact
   symmetry may require groupoid-valued descent.
3. **Terminal RQ0-A:** `v13/note-rq0-physical-overlap-repair.md`, SHA-256
   `cadc7953004f7124160f325929d05fe651f18182a00df1ffd48652eab025546f`.
4. **Terminal executable:** `v13/code/rq0_physical_overlap_exact.py`,
   SHA-256
   `56781c9a10c65be076d86570abd87cbde0901ecc09df2aa04586b30ff31d08d6`.
5. **Terminal receipts:** text SHA-256
   `0b8f97ef8716a2d69c5ae5d8c80d5836523914effcc997fb755c09483751a460`
   and JSON SHA-256
   `fff8c4d633a8e3b1c43db0645305fb02deb763f15db139f7b5ce25bf0f8b375a`.
6. **Paper 0 v0.3:**
   `v13/relativistic-isp-v13-paper0-gravity.md`, SHA-256
   `501c0bb2db3f8448fdc4a07acd2188491f88b12a9d491d19add97bd3208bcbc1`.

The terminal RQ0-A atlas may be reused as a calibration fixture and source of
typed amplitude-instrument morphisms.  Its planted core and region labels may
not be supplied to the localization estimator.  If its intervention family
is too small to support localization, new exact fixtures must be constructed.
Absence of an L0 object from v10 or any earlier corpus is not a block.

Legacy v10 causal sets, diamonds, embeddings, dimension estimators, and
geometric data remain closed.  They are neither inputs nor scoring fixtures
for L0.  No old object is promoted merely because it exists.

## 3. Primitive operational instrument

The input object is a finite operational amplitude instrument

$$
D=
\bigl[
(V_b)_{b\in B},
\mathsf{Prep}_D,
\mathsf{Amp}_D,
\mathsf{Int}_D,
\mathsf{Ctx}_D,
\mathsf{Obs}_D,
\mathsf{Comp}_D
\bigr]/G_D.
$$

Its components have the following exact types.

- $V_b$ are finite boundary modules over the declared exact scalar ring.
- $\mathsf{Prep}_D$ is the frozen family of admitted preparations.
- $\mathsf{Amp}_D$ is the typed family of composable amplitude arrows.
- $\mathsf{Int}_D$ is the finite family of admissible, independently
  selectable intervention generators.  Generator names are opaque process
  handles, not subsystem or location labels.
- $\mathsf{Ctx}_D$ is the frozen family of pre- and post-composition contexts
  that can expose operational phase information.
- $\mathsf{Obs}_D$ is the frozen family of accessible readouts, including
  each candidate record readout before W3 is tested.
- $\mathsf{Comp}_D$ gives the flat typed table of implemented composites of
  opaque intervention handles.  It contains no subsystem partition or
  candidate-locality flag.  Joint implementability is inferred from the
  existence and exact law of these composites rather than supplied as a
  pairwise locality label.
- $G_D$ is the declared presentation gauge.  The executable first rung uses
  configuration relabellings and exact boundary phases in the finite subgroup
  $\mu_8\subset U(1)$; it does not claim the full continuous $U(1)$ gauge.

The operational access contract—preparations, intervention handles, contexts,
and readouts—is a new provisional postulate.  It is not a spatial
factorization.  Full tomography may not be silently assumed: every accessible
preparation, interference context, and readout used by the estimator must be
listed and classified as constructed or postulated.

## 4. Operational quotient

For admitted interventions $I,J$ of the same boundary type, define

$$
I\sim_{\mathrm{op}}J
$$

if and only if every frozen admissible preparation, composable pre-context,
post-context, and accessible readout yields the same exact process
probability for $I$ and $J$.  The comparison is made after quotienting by
$G_D$.  It must include interferometric contexts capable of detecting
physical relative phases; entrywise equality of raw matrices is not the
definition.

Let

$$
\mathfrak I_D
=
\operatorname{Alg}^{*}
\bigl(\mathsf{Int}_D/\!\sim_{\mathrm{op}}\bigr)
$$

denote the finite intervention algebra represented on the accessible process
support.  Any null ideal that no admitted preparation/context/readout can
distinguish is quotiented out before localization.  Permanently inaccessible
ancillary structure therefore cannot create a region.

For the exact first rung, candidate subalgebras are those generated by subsets
of the frozen opaque intervention classes, normalized by exact algebra
equality.  This is a declared finite search scope; the result does not claim
to enumerate every abstract subalgebra of an arbitrary matrix algebra.

## 5. Candidate localized quantum subinstrument

A candidate local object $L_A$ is not a displayed tensor factor.  It is the
gauge class of

$$
L_A=
\bigl[
\mathfrak I_A,
\mathsf{Prep}_A,
\mathsf{Ctx}_A,
\mathsf{Obs}_A,
\operatorname{Rec}_A,
\mathsf{Law}_A
\bigr]/G_A,
$$

where:

1. $\mathfrak I_A\subseteq\mathfrak I_D$ is a proper non-scalar unital
   star-subalgebra generated by admitted operational classes;
2. the restricted preparations, contexts, observations, and composition laws
   are closed and well typed;
3. $\operatorname{Rec}_A$ is derived after the candidate is frozen by applying
   the W3 H-corr/H-avail tests to frozen readouts whose projectors belong to
   the candidate's accessible algebra;
4. there exists at least one nontrivial independently addressable complement
   $\mathfrak I_{A^c}$ at the declared operational scope;
5. the candidate is invariant, up to an explicitly returned isomorphism or
   automorphism, under presentation changes and $G_D$;
6. it is minimal or irreducible under a criterion frozen before the main
   fixture truth is opened.

For this finite rung, an independently addressable complement must satisfy
all of the following exact tests on accessible support:

- elementwise commutation of the two intervention algebras;
- independently selectable generators and exact joint implementation in
  $\mathsf{Comp}_D$;
- scalar intersection after common central record structure has been
  separated and typed;
- faithful composition: distinct pairs of operational classes do not collapse
  to one class unless the declared quotient requires it;
- closure of the generated joint algebra and a declared exact
  dimension/product check appropriate to the finite algebra type.

These clauses define operational independence, not spatial separation.
Failure of the complement test is allowed and is essential to the globally
irreducible control.

Historical and continuation-relative record objects retain their prior types:

$$
\operatorname{Occ}_A(r),
\qquad
\operatorname{Avail}_A(r;V),
\qquad
\mathcal R_A^{\mathrm{hist}},
\qquad
\mathcal R_A(V).
$$

No $\mathcal R_A$ is primitive data.  A readout is frozen before H-corr or
H-avail is evaluated.  Phase may discriminate physical intervention laws but
may not enter fact co-reference.

## 6. Localization category, overlaps, and nerve

$\operatorname{Loc}(D)$ is built from every surviving candidate rather than
from a preferred decomposition.

- **Objects:** gauge/isomorphism classes of localized subinstruments $L_A$.
- **Arrows:** exact operational restrictions, inclusions, and operational
  isomorphisms preserving the typed intervention law and derived records.
- **Automorphisms:** operational symmetries that exchange indistinguishable
  local presentations.
- **Meet/overlap:** the greatest common closed operational subinstrument when
  it exists, computed from the shared intervention, context, readout, and
  record structure.  If no unique representative exists, retain the full
  overlap groupoid or span.
- **Join/refinement:** the closed operational subinstrument generated by the
  inputs, with exact restriction diagrams.
- **Nerve:** the incidence data of nontrivial pairwise and higher overlaps.

The overlap is an intersection of operational subtheories inside a typed
instrument, not a literal intersection of subsets of a global event set.  The
positive atlas must contain at least four recovered proper regions, at least
three differently shaped nonempty pairwise overlaps, and a genuine nonempty
triple overlap.  It must not be a star in which the same identical core is the
only overlap of every region.

For shared stable facts, the restriction diagrams in `Reg`, `FactIface`, and
the contravariant record assignment must commute exactly on every recovered
pair and on at least one triple.  Token symmetries are retained as
automorphisms; no representative is chosen by filename, basis order, or
lexicographic accident.

## 7. Estimator freeze and held-out truth discipline

The construction is split across committed stages.

### 7.1 Estimator-freeze commit

The generic localization estimator is committed before the main fixture's
construction labels are exposed to its executable path.  It may receive only
the typed black-box operational tables and gauge data declared in Sections 3
and 4.  It must contain:

- the exact operational quotient;
- candidate generation and algebra normalization;
- complement, irreducibility, ambiguity, meet, join, and nerve routines;
- a canonical, label-free result schema;
- public calibration controls that contain no main-fixture truth;
- explicit source hash, search cap, and failure behavior.

After this commit, the estimator file is byte-frozen.  The later fixture and
scoring modules may import the estimator; the estimator may not import them.
An AST/module-dependency audit must verify that direction.

### 7.2 Fixture and scoring commit

Only after the estimator is frozen may the main non-star fixture be scored
against its hidden construction labels.  Truth labels live in a separate
module and are supplied only to the scorer.  The estimator receives opaque
operation IDs and exact observable tables, never the truth partition,
displayed subsystem names, construction circuit, or expected overlap nerve.

This separation proves a frozen executable dependency, not independent blind
authorship.  That limited provenance claim must be stated verbatim in the
receipt.  An external hostile round must test the frozen estimator on at least
one independently rebuilt or mutated fixture before terminal status.

If the estimator changes after the main truth has been opened, the old score
is invalid.  A new estimator-freeze commit and a genuinely new unseen fixture
family are required; rescoring the old fixture cannot restore the headline.

## 8. Stages

### Stage 0 — referent and adapter census

Reproduce the anchors.  Inventory the exact RQ0-A process, intervention,
record, and morphism types.  State what can be reused without alteration and
what new L0 fixtures require.  This is an adapter census, not a search for a
pre-existing localization ontology.

`RQ0-L0-BLOCKED-AT-ADDRESS` is permitted at this stage only after an explicit
candidate class and exact operational-access obstruction are constructed.  A
grep result or absence from v10 is not a theorem.

### Stage 1 — exact operational quotient

Construct $\sim_{\mathrm{op}}$, the accessible null ideal, and
$\mathfrak I_D$.  Prove equivalence, gauge invariance, and compatibility with
composition on every fixture.  Freeze candidate record readouts before W3
tests.

### Stage 2 — freeze the generic estimator

Implement the candidate enumeration, algebra closure, complement tests,
groupoid handling, and overlap-nerve construction.  Commit its exact source
hash before the main fixture scorer is run.

### Stage 3 — construct and open exact fixtures

Build the controls in Section 9 over exact cyclotomic amplitudes.  The main
fixture must provide a hidden non-star localization truth, but only its
black-box operational tables reach the estimator.

### Stage 4 — derive local records and overlap descent

Run W3 on frozen local readouts.  Construct pairwise and triple restriction
diagrams.  Distinguish fact descent from token automorphisms and retain every
exact symmetry.

### Stage 5 — score, falsify, and receipt

Score recovered localization only after the estimator hash is frozen.  Run
every positive and negative control, two-run determinism, stored-receipt
regeneration, an AST/no-smuggling audit, and an observed-anchor mutant that
must close all positive outcomes and exit nonzero.

## 9. Mandatory controls

### C1. Presentation change

Two distinct circuit or generator presentations of the same operational
process must yield isomorphic localization output, including the overlap
nerve.

### C2. Configuration relabelling and boundary gauge

Arbitrary tested configuration permutations and exact $\mu_8$ boundary
rephasings must change only the declared presentation.  A compensated phase
change is gauge; an operationally visible uncompensated relative phase is
physical.

### C3. Inaccessible spectator

A permanently inaccessible ancillary completion must lie in the operational
null quotient and must not create a local object, record, overlap, or volume-
like count.

### C4. Active independent spectator

An independently controlled and observed ancillary process must be recovered
as a separate operational component rather than discarded or merged into a
different local object.

### C5. Encoded subsystem

A logical subsystem conjugated across the displayed basis by an exact
non-product cyclotomic transformation must be recovered up to operational
isomorphism.  Visible qubit or bit position must fail as a localization rule.

### C6. Globally irreducible process

An accessible intervention family with trivial admissible complement must
return no false proper localization.

### C7. Ambiguous factorization

An exactly symmetric process admitting several operationally indistinguishable
factorizations must return the full localization groupoid or underdetermined
family.  No basis order, lexical name, minimal index, or arbitrary
representative may break the symmetry.

### C8. Non-star atlas

The main held-out fixture must recover at least four proper regions, distinct
pairwise overlaps, and a genuine triple overlap.  A common-core star or a
truth-supplied incidence list fails.

### C9. Exact complex phase

At least one fixture must use amplitudes in $\mathbb Q(\zeta_8)$ with a
physical interference phase.  Gauge-equivalent phase presentations must
localize identically; an operationally distinct relative phase must remain
distinct without being used as a fact-identity criterion.

### C10. Derived W3 records

Every positive localized object counted toward the main atlas must contain a
nonempty record algebra derived from its own exact write/preserve dynamics.
A no-write control must fail H-corr, and an erasing continuation must destroy
availability without erasing historical occurrence.

### C11. Equal-law false overlap

Two stable record readouts with matching marginal laws but no common
operational subinstrument or typed restriction bridge must not be merged.

### C12. Estimator no-smuggling mutant

A deliberately contaminated estimator that reads a hidden component label or
expected overlap edge must be detected by the static/dependency audit.  Its
receipt is invalid even if its numerical score is perfect.

## 10. Four-gate worksheets for new objects

### 10.1 Operational quotient $\mathfrak I_D$

- **Referent:** exact equality of every frozen accessible process statistic
  across all admitted preparations, contexts, and readouts.
- **Necessity:** raw matrix entries retain gauge and permanently inaccessible
  completions that cannot individuate a physical region.
- **No-smuggling:** no subsystem, location, circuit-wire, or truth label
  appears in the equivalence relation.
- **Discriminator:** an interferometrically visible relative phase separates
  classes; a gauge phase or inaccessible completion does not.

### 10.2 Localized subinstrument $L_A$

- **Referent:** a closed proper intervention subalgebra, its restricted
  operational law, a derived W3 record algebra, and at least one exact
  independently addressable complement.
- **Necessity:** the terminal atlas supplies typed regions but does not explain
  which proper parts of a black-box process deserve local status.
- **No-smuggling:** the definition contains no displayed tensor factor,
  qubit, wire, coordinate, graph vertex, causal direction, or known fixture
  partition.
- **Discriminator:** independent spectators split, inaccessible spectators
  vanish, encoded systems survive conjugation, and irreducible systems do not
  split.

### 10.3 Operational independence/complement

- **Referent:** commuting, independently selectable exact intervention
  algebras with faithful joint implementation and the declared algebraic
  product test on accessible support.
- **Necessity:** commutation alone can arise from a center, a dormant action,
  or an accidental restricted state and does not establish addressability.
- **No-smuggling:** no spatial, causal, or tensor-coordinate meaning is
  assigned to the complement.
- **Discriminator:** the active-spectator control passes; the inaccessible and
  irreducible controls fail for different measured reasons.

### 10.4 $\operatorname{Loc}(D)$ and its overlap nerve

- **Referent:** the exact category/groupoid of all surviving operational local
  objects and their computed restriction, meet, join, and automorphism maps.
- **Necessity:** choosing one factorization would erase physically exact
  ambiguity and would not support regional descent.
- **No-smuggling:** the expected fixture partition and overlap nerve are
  absent from the estimator path and opened only by the scorer.
- **Discriminator:** presentation changes preserve the object; a non-star
  fixture yields a non-star recovered nerve; an ambiguous fixture returns
  multiple isomorphic objects rather than one selected labeling.

## 11. Pre-registered outcomes

The receipt may report only the following scientific outcomes:

### `RQ0-L0-BLOCKED-AT-ADDRESS`

An explicit finite candidate class and operational quotient have been
constructed, but no nontrivial candidate satisfies the addressability,
record, and no-smuggling gates at the declared scope, or the frozen access
contract is proved insufficient to discriminate them.  “Not present in the
old corpus” cannot earn this result.

### `RQ0-LOCALIZATION-GROUPOID`

At least one nontrivial localized subinstrument and its overlaps are recovered
exactly, but one or more decompositions remain physically underdetermined up
to nontrivial automorphism.  All alternatives and arrows are retained; no
representative is selected.  Failure of a later atlas uniqueness condition
does not erase this rung.

### `RQ0-LOCAL-ATLAS`

At the declared finite search scope, localization is recovered uniquely up to
the returned gauge/groupoid equivalence; at least four proper regions form a
non-star nerve with distinct pairwise overlaps and a genuine triple overlap;
their derived stable-record restrictions descend; and every mandatory control
passes.

`RQ0-L0-INVALID` is a receipt status, not a scientific outcome.  It is
mandatory for an anchor failure, cap overrun, floating/nondeterministic
substantive path, truth-import violation, post-freeze estimator mutation,
unclassified failed check, or positive rung not derived from named
prerequisite groups.  An invalid receipt prints no positive outcome and exits
nonzero.

## 12. Kill conditions

Any of the following closes every positive L0 rung:

1. the estimator reads construction labels, expected component partitions,
   expected overlap edges, circuit wires, qubit names, tensor-factor names,
   coordinates, causal data, metric data, or fields;
2. a visible-basis factor passes while the exact encoded presentation fails;
3. an inaccessible spectator becomes a local object, or an active accessible
   spectator is erased by the quotient;
4. the globally irreducible fixture is falsely split;
5. an ambiguous exact factorization is resolved by an arbitrary
   representative;
6. presentation or gauge changes alter localization beyond the declared
   isomorphism/groupoid;
7. the non-star nerve is copied from hidden truth rather than computed;
8. a record algebra is declared, searched after seeing H-corr/H-avail, or
   certified by phase agreement;
9. complex phase is discarded, rounded, or evaluated through floating-point
   arithmetic on a substantive path;
10. the estimator is edited after fixture truth is opened without a fresh
    freeze and new unseen fixture;
11. any commutation or process direction is called spacelike or causal;
12. any C1, C2, geometric, field, or gravity object is constructed.

These are invalidating conditions, not evidence for
`RQ0-L0-BLOCKED-AT-ADDRESS` unless the declared no-go requirements for that
scientific outcome are separately met.

## 13. Exact implementation, caps, and receipts

Substantive arithmetic must be exact over $\mathbb Q(\zeta_8)$.  A concrete
representation by rational coefficient tuples with the exact cyclotomic
relation is preferred.  Floats, numerical tolerances, random sampling, and
numerical eigensolvers are forbidden on the scientific path.

The first-rung caps are:

- at most 32 accessible carrier configurations per fixture;
- at most eight inequivalent primitive intervention classes supplied to one
  exhaustive candidate search;
- at most the exact 4,140 set partitions of eight generators before algebra
  equality removes duplicates;
- at most 240 seconds total wall time for the complete positive and control
  suite, with progress output at intervals shorter than eight minutes.

A cap hit is explicit `RQ0-L0-INVALID`; it may not trigger sampling, a greedy
fallback, or a silently reduced fixture.

The final receipt must state:

- every new postulate and every inherited theorem;
- every constructed object and exact type;
- the complete operational access contract;
- every legacy reuse and its classification;
- every scalar ring and implemented gauge subgroup;
- estimator-freeze commit and source hash;
- fixture/scorer commit and source hashes;
- proof that the estimator does not import fixture truth;
- every search space, cap, candidate count, quotient count, and automorphism;
- exact W3 occurrence/availability results;
- exact pair/triple overlap and record-restriction diagrams;
- check class, prerequisite group, and pass/fail reason for every row;
- deterministic text and JSON receipt hashes;
- the limited provenance statement from Section 7.2;
- all nonclaims and the highest pre-registered outcome.

Outcome booleans must be computed from named prerequisite groups, never typed
as constants.  A one-observed-anchor mutant must fail exactly or with a fully
accounted failure set, suppress every positive rung, mark the receipt invalid,
and exit 1.  Two fresh text runs and two fresh JSON runs must be byte-identical
and regenerate the stored receipts before delivery.

## 14. File and commit discipline

This pin commit may modify only:

- `v13/note-rq0-operational-localization-pin.md`;
- append-only `v13/LOG.md`;
- the live pointer in `RUNBOOK.md`.

The later estimator-freeze commit may create or modify only:

- `v13/code/rq0_l0_localization_estimator_exact.py`;
- append-only `v13/LOG.md`;
- the live pointer in `RUNBOOK.md`.

The later fixture/delivery commits may create or modify only:

- `v13/note-rq0-operational-localization.md`;
- the byte-frozen estimator file only for hash verification, never editing;
- `v13/code/rq0_l0_fixtures_exact.py`;
- `v13/code/rq0_l0_operational_localization.py`;
- `v13/code/rq0_l0_output.txt`;
- `v13/code/rq0_l0_receipt.json`;
- append-only `v13/LOG.md`;
- the live pointer in `RUNBOOK.md`.

Every commit stages explicit paths only.  The terminal RQ0-A note, executable,
receipts, Paper 0, and all v10-v12 files are read-only.  No file outside the
whitelist may be changed.  Each pin/freeze/delivery/review/adjudication event
is a separate ledger and Git commit.

## 15. Required report

The construction report must answer:

1. What is operationally quotiented, and what survives as physical process
   structure?
2. What precisely makes a subinstrument independently addressable without
   assuming space?
3. How are inaccessible and active spectators distinguished?
4. How is an encoded subsystem recovered without reading its displayed
   factorization?
5. When is localization unique, and when is it groupoid-valued?
6. What are the recovered regions, restriction maps, pair overlaps, and
   genuine triple overlap?
7. Why is the overlap nerve non-star and not copied from held-out truth?
8. How are local W3 records derived from the same amplitudes?
9. Do stable facts descend on the recovered overlaps?
10. Which physical phases survive the operational quotient, and which phases
    are gauge?
11. What is the first real unresolved obstruction?
12. Which claims are definitions, postulates, exact theorems, measurements,
    conjectures, or nonclaims?

## 16. Successor discipline

On delivery, halt at the highest pre-registered L0 outcome.  A separate
external hostile round must independently attack the frozen estimator,
encoded-system control, ambiguity handling, non-star nerve, W3 descent, and
receipt circularity.  Only a later adjudicator ledger may confer terminal
status.

`RQ0-C1` may be considered only after L0 is terminal.  Its future question is
whether two operations differing only on one recovered localized
subinstrument change accessible stable-record laws on another under a frozen
screening rule.  That question is recorded only as successor scope; no
influence relation is defined here.

The binding order remains:

$$
\text{RQ0-A fact descent}
\to
\text{RQ0-L0 localization}
\to
\text{RQ0-C1 influence}
\to
\text{RQ0-C2 causal cones}
\to
\text{RQ0-G Lorentzian kinematics}
\to
\text{RQ1 matter}
\to
\text{GR1 gravity}.
$$

**Freeze this pin before writing the localization estimator.**
