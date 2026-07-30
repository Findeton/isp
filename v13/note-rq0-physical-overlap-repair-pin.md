# v13 RQ0 — physical-overlap repair pin

**Status:** PIN, STRICT, 2026-07-30.
**Authority:** the external hostile review frozen at v13 #14 and accepted in
full at v13 #15 (`150f191f6d67dbaa2de99594e6b401d0a3f6e71f`).
**Reviewed commits remain immutable:**
`307c36f017d9d5587334d3b79421645ee5b54c61` and
`1537b1475705a5def1d1d063459fa7d4fb534982`.

## 1. Question and ceiling

The repair asks one question:

> Can three genuinely different, equal-dimensional, non-spectator quantum
> amplitude instruments be exhibited as typed subinstruments of one finite
> master instrument, so that their common stable record is an actual
> restriction/pullback through process morphisms rather than a diagonal
> coupling selected after matching marginal laws?

The repair may restore at most:

1. `RQ0-REGIONS-CONSTRUCTED`;
2. `RQ0-REGIONAL-SITE`;
3. `RQ0-FACT-DESCENT`.

It may not construct localized influence, a causal order or cone, spacetime,
volume, conformal geometry, fields, stress, gravity, or `RQ0-C1`.  Token
symmetries may be measured, but no `RQ0-GROUPOID-ARENA` is available without
geometric data.

## 2. Binding corrections

The repair inherits the quantum-region and continuation-relative record
definitions from the amendment pin, with six strict corrections.

### 2.1 Same dimension and anti-padding

The main positive atlas must contain three regions $D_1,D_2,D_3$ with the
same finite carrier dimension.  At least one pair, and preferably all three,
must be non-isomorphic under the declared gauge by an exact invariant of
accessible amplitude/composite dynamics—not dimension, filenames, or an
independent ancillary factor.

Every declared auxiliary subsystem must couple to the branch, record, or
another accessible subsystem in at least one admitted arrow.  In addition,
the executable must test the stronger family-level condition:

> There is no common configuration relabelling and nontrivial product split
> of the carrier for which every substantive arrow in the regional instrument
> is a Kronecker product across that same split.

For an eight-configuration fixture, all relabellings relevant to the declared
$2\times4$ split must be searched exactly, or an exact stronger invariant
must be proved.  The old factorized $4/8/16$ family is a mandatory negative
control and must be detected as padded.

### 2.2 Physical master and region morphisms

Before any fact comparison, define a finite master amplitude instrument
$\mathsf E$ and a category of instrument morphisms.

An instrument morphism $f:D\to E$ contains:

- typed boundary maps $f_j:V_j^D\to V_j^E$;
- a family-preserving map of accessible arrow labels;
- exact intertwining for every mapped arrow $U:V_s\to V_t$,
  $$
  f_tU_D=U_Ef_s;
  $$
- preparation compatibility;
- readout pullback/restriction, expressed either as equality of diagonal
  projectors or an exact value-map diagram;
- compatibility with the declared real gauge.

The positive construction must supply embeddings

$$
j_a:D_a\hookrightarrow\mathsf E,
\qquad a=1,2,3,
$$

or equally strong typed quotient/channel maps.  Matrix equality after a
constructor has copied regional matrices is not enough by itself: the maps,
their domains, arrow-label action, and commuting diagrams must be explicit
objects and independently checked.

### 2.3 Overlap is an amplitude subinstrument

Construct a common core $O$ and embeddings

$$
i_a:O\hookrightarrow D_a
$$

such that $O$ is the pairwise and triple pullback/intersection of the
$D_a\hookrightarrow\mathsf E$ subinstruments at the declared operational
scope.  “Intersection” here is intersection of accessible subinstrument
structure inside the typed master, not intersection of subsets of a global
event set.

$O$ must contain at least:

- the shared write arrow;
- one shared record-preserving continuation;
- the shared accessible record readout;
- the preparation scope needed for its W3 certificate.

The regional record proposition must literally be the pullback/restriction of
the master/core record projector under $j_a$ and $i_a$.  Equality of marginal
probabilities is printed only as a consequence; it is forbidden as the
co-reference criterion.

### 2.4 Admissible extensions are frozen first

The constructor for $\mathsf E$, the morphism type, the three embeddings and
the admissible-extension class must be hash-locked before the fact comparison
is evaluated.  The constructor may not consume regional marginal laws or a
requested fact map.

Two negative controls are mandatory:

1. **Diagonal/anti-diagonal ambiguity.**  Construct exact diagonal and
   anti-diagonal record-copy extensions with the same one-record marginals.
   A law-only predicate must accept both or return incompatible maps, while
   the structural morphism predicate accepts only the predeclared physical
   master/region bridge.
2. **Equal law, no bridge.**  Construct a region with the same stable binary
   record law but no admissible instrument morphism into the frozen master.
   Exhaust the declared finite morphism scope or use an exact invariant that
   proves absence.  The result must be `SAME-LAW-NOT-SAME-FACT`.

### 2.5 `Reg` and `FactIface` are distinct

Define:

- $\mathbf{Reg}$: objects are amplitude instruments; arrows are the typed
  instrument morphisms above;
- $\mathsf{FactIface}$: objects are the derived stable-record algebras and
  arrows are algebra/value restrictions induced by `Reg` morphisms;
- $\mathrm{Rec}:\mathbf{Reg}^{op}\to\mathsf{FactIface}$: the derived record
  assignment at the declared preservation scope.

The old nine-arrow binary-value groupoid is retained only as a negative/type
control.  It may not earn `RQ0-REGIONAL-SITE`.  The positive regional site
requires identities, composition, the master embeddings, pair/triple overlap
spans, a declared cover, and commuting diagrams at the amplitude-instrument
level.  Fact descent is evaluated only after that site exists.

### 2.6 Refinement, gauge, and access scope

The old $D_1\to D_2\to D_3$ result is named **Born-shadow product
coarse-graining**, not amplitude refinement.

Any positive `Ref` object in this repair must be an instrument-family
inclusion/channel with explicit boundary and arrow maps satisfying the same
intertwining equations as other `Reg` morphisms.  Refinement of intervention
families at fixed carrier dimension is permitted, but it must not be called a
spacetime-resolution limit.

The implemented exact gauge is engraved as

$$
G_D^{\mathbb R}
=\text{configuration relabellings}\times\{\pm1\}
\text{-boundary gauge}.
$$

No claim about the full complex $U(1)$ gauge is permitted.  Declaring all
basis configurations preparable and exposing the complete configuration
readout is an **operational-access postulate** unless preparation and
measurement instruments are themselves constructed.

## 3. Required positive construction

The preferred exact first rung uses equal eight-dimensional boundary spaces
with three operational subsystems: branch, record, and auxiliary.  This is a
permitted schema, not a planted answer.

The construction must provide:

1. one common write arrow that establishes a W3 record and couples all
   declared subsystems;
2. one common preserving continuation carried by the overlap core;
3. three region-specific preserving dynamics, each W3-compatible and each
   involving the auxiliary subsystem;
4. three region-specific coherent erasers with failed H-avail, nonzero
   cross-sector cut coherence, and nonzero $\Delta^B$;
5. one no-write control failing H-corr;
6. three exact accessible composite invariants proving same-dimensional
   non-isomorphism;
7. one master instrument whose declared arrow family contains the common core
   and all three regional subfamilies;
8. explicit core-to-region and region-to-master morphisms;
9. an exact pair/triple overlap and cover in `Reg`;
10. the induced `Rec` diagram and fact triple law.

The master is a finite local witness object, not a global universe or global
event set.  Region individuality resides in the accessible subinstrument
family and composition law, not in preferred matrix labels.

## 4. Gates and controls

### G1 — Typed-object gate

Every boundary, arrow, family label, readout, preparation, gauge action,
morphism, overlap and cover is typed.  Arrow dimensions alone are not a
substitute for source/target and label maps.

### G2 — Quantum-seam gate

For each new region, derive occurrence and continuation-relative availability
from its own matrices.  Preserve must have zero record residual; erase must
restore cross-sector coherence and a nonzero defect; no-write must fail.

### G3 — Anti-padding and diversity gate

All regions have equal dimension; every auxiliary participates; the main
families pass the exact no-product test; the old family fails it; and an
accessible exact invariant separates at least one same-dimensional pair.

### G4 — Morphism gate

Every positive region/master and overlap/region map satisfies all typed
intertwining, preparation and readout-pullback equations.  Deleting or
altering one mapped arrow must make this gate fail.

### G5 — Physical-overlap gate

The common record belongs to the constructed overlap subinstrument and its
regional images.  The pair and triple pullback/overlap laws hold.  Marginal
equality is not consulted.

### G6 — No-circularity gate

The master/morphism digest is frozen before comparison.  Diagonal versus
anti-diagonal and equal-law/no-bridge controls defeat the law-only criterion
while the structural criterion gives the intended positive and negative
answers.

### G7 — Category/type gate

`Reg`, `FactIface`, and `Rec` are separate executable objects.  Regional
identities/composition, cover and overlap diagrams pass.  The value-only
groupoid cannot satisfy the `Reg` schema.

### G8 — Instrument-refinement gate

The positive refinement/inclusion carries boundary maps, arrow maps and exact
intertwining.  The old Born-shadow result is printed under its corrected name
and cannot satisfy this gate.

### G9 — Gauge/access gate

The executable says `REAL-SIGN-GAUGE`; full $U(1)$ claims and geometry/field
inputs trigger schema failures.  Preparation/tomography access is printed as
`POSTULATE`, not `DERIVED`.

### G10 — Falsification and determinism gate

One deliberate anchor mutant exits 1 with exactly one visible failure.  Two
complete text runs and two JSON runs are byte-identical.  Exact arithmetic is
used throughout; no floats, tolerances, randomness or numerical geometry.

## 5. Four-gate worksheets

### Master instrument $\mathsf E$

- **REFERENT:** a finite operational amplitude family containing the common
  core and the three declared regional arrow subfamilies.
- **NECESSITY:** a common coupling without region maps failed to certify
  regional co-reference.
- **NO-SMUGGLING:** it contains no fact map, target marginal law, causal
  order, coordinate, metric or field; its constructor and digest are frozen
  before comparison.
- **DISCRIMINATOR:** anti-diagonal and rogue equal-law objects share marginals
  but fail the structural embeddings.

### Instrument morphism

- **REFERENT:** boundary maps plus an arrow-label map satisfying exact
  intertwining, preparation and readout diagrams.
- **NECESSITY:** value projections did not connect the old extension to the
  regional processes.
- **NO-SMUGGLING:** fact identity is not a morphism input.
- **DISCRIMINATOR:** a mutated arrow or a same-law rogue region has no valid
  morphism.

### Overlap $O$

- **REFERENT:** the common amplitude subinstrument/pullback of the three
  regional embeddings inside the master.
- **NECESSITY:** a value-level groupoid is not a physical regional overlap.
- **NO-SMUGGLING:** $O$ is computed from mapped operational arrows, not
  declared from equal probabilities.
- **DISCRIMINATOR:** the positive triple has a nonempty common core; the
  equal-law/no-bridge fixture does not.

### `Reg`, `FactIface`, and `Rec`

- **REFERENT:** respectively amplitude instruments/morphisms,
  stable-record algebras/restrictions, and the induced record assignment.
- **NECESSITY:** commit #12 compressed these three types.
- **NO-SMUGGLING:** fact arrows are induced only after regional morphisms
  pass.
- **DISCRIMINATOR:** the old value-only groupoid passes `FactIface` laws but
  fails the `Reg` morphism schema.

## 6. Pre-registered outcomes

- `RQ0-REPAIR-BLOCKED-AT-DIVERSITY`: no same-dimensional non-padding pair;
- `RQ0-REPAIR-BLOCKED-AT-MORPHISM`: regions exist but no typed master bridge;
- `RQ0-REPAIR-BLOCKED-AT-OVERLAP`: bridges exist but no common stable-record
  pullback/triple;
- `RQ0-REGIONS-CONSTRUCTED`: the quantum regions and internal seams survive;
- `RQ0-REGIONAL-SITE`: `Reg`, its physical overlaps, cover and instrument
  refinement exist at the declared finite scope;
- `RQ0-FACT-DESCENT`: the derived record functor descends the common fact on
  that physical site and both no-circularity controls pass.

A later negative never erases earlier earned rungs.  The highest positive
claim requires every preceding positive gate.

## 7. Exact implementation discipline

The repair may create only:

```text
v13/note-rq0-physical-overlap-repair.md
v13/code/rq0_physical_overlap_exact.py
v13/code/rq0_physical_overlap_output.txt
v13/code/rq0_physical_overlap_receipt.json
```

The adjudicator may append `v13/LOG.md` and update RUNBOOK's live pointer.  No
reviewed #12 file, prior pin, v10–v12 file or v13 Paper 0 file may be edited.

The executable must:

- lock this pin, the two prior pins, Paper 1, Paper 2, the hostile review and
  adjudication commit;
- construct every new amplitude and morphism from scratch;
- print every postulate, search scope, cap, use class and legacy import;
- use exact arithmetic, exhaustive finite searches where claimed, no random
  seed, float or tolerance;
- state which old objects are negative controls only;
- regenerate both receipts exactly;
- make one deliberate anchor mutant exit 1 visibly.

## 8. Required report answers

1. What makes the three equal-dimensional regions physically different?
2. What exact test rules out spectator padding?
3. What is the master amplitude instrument?
4. What are the typed region/master and overlap/region morphisms?
5. Which diagrams commute, and at which preparation/continuation scope?
6. How is the regional record the actual restriction of the master/core
   record?
7. Why can neither matching marginals nor a post-selected coupling certify
   the fact?
8. How do the anti-diagonal and equal-law/no-bridge controls behave?
9. What is `Reg`, what is `FactIface`, and how does `Rec` act?
10. Is refinement an amplitude-instrument morphism or only a shadow map?
11. What exact real gauge is implemented?
12. Which access assumptions are postulates?
13. What is the highest honestly restored rung and the first remaining
    obstruction?

If all gates pass, the terminal sentence for this repair delivery is:

> Three equal-dimensional, non-padding finite quantum regional instruments
> occur as typed subinstruments of one predeclared finite master instrument.
> Their common W3-stable record is the actual pullback of a shared overlap
> record through exact amplitude-instrument morphisms, not a consequence of
> matching laws.  `Reg`, `FactIface`, and `Rec` are distinct and the physical
> triple descends.  No causal, spacetime, field or gravity claim is made.

The unit then halts before `RQ0-C1`.
