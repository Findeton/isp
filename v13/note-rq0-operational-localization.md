# v13 RQ0-L0 — operational localization and overlap discovery

**Status:** GREEN-UNREVIEWED, 2026-07-30.
**Pin:** `note-rq0-operational-localization-pin.md`, commit
`f218dde7b73631f7fd6359582d7bf494990eb076`.
**Estimator freeze:** commit
`a5b71735fb80d7214e1cc4e5a389289572895d53`.

## 1. Result

At one exact finite operational scope, this unit earns

$$
\boxed{\texttt{RQ0-LOCAL-ATLAS}.}
$$

The construction starts from an amplitude-native process with frozen
preparations, opaque interventions, composition contexts, accessible probes,
and candidate record readouts.  After quotienting operationally
indistinguishable actions, the estimator recovers four independently
addressable noncommutative intervention algebras from a globally encoded
16-state presentation.  Their nonempty proper joins form a finite operational
localization category with:

$$
14\ \text{objects},
\qquad
50\ \text{identity/restriction arrows},
$$

$$
66\ \text{nonempty pair overlaps},
\qquad
134\ \text{nonempty triple overlaps}.
$$

Ten recovered regions carry stable records derived from the same amplitude
dynamics.  On one explicit triple, the same record projector family restricts
through all three regional paths to the common operational overlap.

The result is a finite existence and recovery theorem under a declared
operational-access postulate.  It is not a derivation of space from one bare
matrix.  The intervention algebra contains exact addressability and
commutation information; the new result is that its localized subobjects,
encoded presentations, overlaps, ambiguity, and W3 record restrictions can be
recovered without reading the construction's subsystem labels or expected
nerve.

No influence or causal relation is defined.  The word *local* means
operationally local at this rung, not spatial or spacelike.

## 2. Immutable provenance and executable separation

The strict pin was committed before estimator construction.  The generic
estimator was then committed separately before the main fixture and its hidden
truth existed:

| Object | Commit / SHA-256 |
|---|---|
| L0 strict pin | `f218dde7b73631f7fd6359582d7bf494990eb076` / `02ed47ad0a294741e613639b02066797a2057fcfcd816edd81203f353b1f9a59` |
| frozen estimator | `a5b71735fb80d7214e1cc4e5a389289572895d53` / `0b8d90bad735f6574ee367dd0bf7e98bcc1c6f2854f7a12070c82bae84e063b8` |
| fixture/truth module | SHA-256 `ada6dcbce2e9686b7ab45523cb8e8937a0c98cbae6504fd95092cf60aa7388f5` |
| scorer/receipt runner | SHA-256 `60a9819790b4c81ff76c04ef14b0bb2e0dedeb41a516ec884bd11eebdfb61988` |
| text receipt | SHA-256 `0297ac85c85743eb5ef0dc15ca4fdb07acf421b142019cc256da3f4d671e5068` |
| JSON receipt | SHA-256 `a073dd2da23d2236658b118ab3d0e19965ae12a1b5caafbac7e7ad1fc59144a5` |

The estimator imports only Python standard-library modules.  It does not
import the fixture, scorer, construction truth, or delivery note.  The fixture
and scorer import the frozen estimator in the permitted direction.  An AST
control detects an in-memory estimator contaminated by a truth import.

This Git order proves temporal source freeze and executable dependency
separation.  It does not prove independent blind authorship.  That stronger
test belongs to the hostile round, which must rebuild or mutate at least one
fixture without relying on this delivery's truth module.

## 3. Exact operational input

The primitive finite instrument is

$$
D=
\bigl[
(V_b),
\mathsf{Prep}_D,
\mathsf{Amp}_D,
\mathsf{Int}_D,
\mathsf{Ctx}_D,
\mathsf{Obs}_D,
\mathsf{Comp}_D
\bigr]/G_D.
$$

The main fixture declares:

- a 16-dimensional carrier;
- 48 exact preparations;
- 48 exact rank-one readout probes;
- one exact composition context;
- eight opaque intervention handles;
- six record candidates frozen before W3 evaluation;
- exact amplitudes in $\mathbb Q(\zeta_8)$;
- configuration relabelling and the finite $\mu_8$ boundary-phase subgroup as
  the implemented presentation gauge.

These accessible operations are a provisional postulate.  Their handles carry
no branch, memory, qubit, wire, component, region, or coordinate name.  The
fixture module contains such construction truth only for later scoring.

The input does not contain a causal order, a graph edge, a metric, a field
propagator, or a desired region partition.

## 4. Operational quotient

For two same-typed admitted interventions, define

$$
I\sim_{\mathrm{op}}J
$$

when every frozen preparation, composition context, and probe gives the same
exact Born statistic.  Exact $\mu_8$ global phases are normalized.  The
reachable-support projector is constructed first, and permanently
inaccessible direct-sum structure is removed from every action.

The quotient is fail-closed.  If two interventions have equal operational
signatures but retain inequivalent accessible actions after the declared
phase gauge, the estimator returns `AccessUnderdetermined`; it does not select
a representative.

In the main fixture:

$$
\dim V_D=16,
\qquad
\dim V_D^{\mathrm{acc}}=16,
$$

and all eight opaque handles remain distinct operational classes.  Their
generated star-algebra has exact vector-space dimension

$$
\dim\mathfrak I_D=256.
$$

## 5. Localized subinstrument criterion

For each subset of opaque intervention classes, the estimator constructs the
generated unital star-algebra on accessible support.  A partition is an
independently addressable factorization only when:

1. every block algebra is non-scalar;
2. different block algebras commute elementwise;
3. every pair has scalar intersection;
4. the product of block dimensions equals the ambient algebra dimension;
5. their joint generated algebra is the ambient operational algebra.

The search exhausts all

$$
B_8=4140
$$

set partitions.  It retains every valid finest factorization.  No displayed
tensor factor is consulted.

The main search finds 14 valid nontrivial coarsenings and one finest
factorization.  Its four atom algebras have dimensions

$$
(4,4,4,4).
$$

Held-out scoring matches the four recovered opaque blocks bijectively to the
four hidden construction atoms.  None of the encoded atom algebras equals any
of the four displayed unencoded slot algebras.  Thus visible bit position is
not the localization rule.

This is not an exhaustive search of every abstract subalgebra of
$M_{16}(\mathbb Q(\zeta_8))$.  It is exhaustive only for star-algebras generated
by subsets of the eight frozen operational classes.

## 6. The localization category and overlap nerve

For the recovered atoms, every nonempty proper join is a localized
subinstrument.  A restriction arrow

$$
L_A\longrightarrow L_B
$$

exists when $B\subseteq A$ in the recovered atom lattice.  This orientation
means that a larger operational region restricts to a smaller one.  The
executable constructs all 14 identities and all proper restrictions, for 50
arrows total, and checks composition closure.

Pair and triple overlaps are exact algebra meets.  The estimator computes the
meet from recovered atoms and independently checks its dimension against the
intersection of the corresponding generated algebras.  Every nonempty pair
meet has both typed regional restriction arrows.

The atlas is non-star.  It has ten record-bearing regions, their intersection
over all ten is empty, and their pairwise meets realize ten distinct nonempty
operational subregions.  No one common core is silently used as every
intersection.

These are intersections of operational subtheories, not subsets of a global
event set.  `Loc(D)` is a finite localization category/lattice with an exact
presentation groupoid.  No Grothendieck topology or spacetime topology is
claimed.

## 7. Stable records on recovered local objects

The six candidate record witnesses correspond, in hidden scoring truth, to
the six unordered pairs of four atoms.  Their handles are opaque to the
estimator.  Each witness contains, on the same amplitude process:

- a write arrow;
- a record-preserving continuation;
- a coherent erasing continuation;
- a no-write control;
- input-alternative, cut-record, and final-availability projector families.

Every witness returns the exact row

$$
\begin{aligned}
\mathrm{H\text{-}corr}(U_{\mathrm{write}})&=1,\\
\mathrm{H\text{-}avail}(V_{\mathrm{preserve}})&=1,\\
\mathrm{H\text{-}avail}(V_{\mathrm{erase}})&=0,\\
N_{\mathrm{cross}}(V_{\mathrm{erase}})&=2,\\
\mathrm{H\text{-}corr}(U_{\mathrm{no\text{-}write}})&=0.
\end{aligned}
$$

All six record marginals are exactly $(1/2,1/2)$.  A record attaches to a
localized object only when its projectors and all write/preserve/erase/control
arrows belong to that object's operational algebra.  Consequently:

- single-atom objects carry no pair record;
- each two-atom object carries its one pair record;
- each three-atom object carries its three pair records.

This yields ten record-bearing proper regions.

## 8. Explicit fact-descent triple

Consider the three recovered regions with hidden scoring labels

$$
\{0,1\},
\qquad
\{0,1,2\},
\qquad
\{0,1,3\}.
$$

Their common operational meet is the two-atom algebra $\{0,1\}$, of dimension
16.  The same frozen witness `w0` occurs in all three source record algebras
and in the meet.  The executable constructs three typed record restrictions,
each the identity pullback of that one projector family, and checks the three
paths to the meet.

Thus the shared fact is not inferred from equal probability laws.  The
separate equal-law control gives a four-dimensional and an eight-dimensional
W3 witness the same exact fair marginal but rejects a declared fixed-carrier
bridge at the exact boundary-dimension mismatch `4 -> 8`.

Token identity is not added.  If later token symmetries remain, they belong in
the returned groupoid rather than in a chosen global label set.

## 9. Mandatory controls

| Control | Exact result |
|---|---|
| two circuit presentations | distinct circuit words give the same encoding matrix |
| configuration and $\mu_8$ gauge | full data are exact conjugates; all four atom algebras descend by conjugation |
| inaccessible spectator | raw dimension 8, accessible dimension 4; localization signature unchanged from the 4-dimensional base |
| active independent extension | recovered as a separate dimension-4 noncommutative atom |
| encoded subsystem | four hidden atoms recovered; none equals a visible slot algebra |
| globally irreducible process | generated algebra dimension 16; no proper localization |
| ambiguity | exact identity and atom-swap arrows retained in the localization groupoid |
| non-star atlas | 14 objects, empty universal atom core, distinct pair overlaps, genuine fact triple |
| complex phase | an uncompensated cyclotomic phase changes 576 access-table cells but leaves its atom algebra unchanged |
| W3 records | all six write/preserve/erase/no-write rows pass |
| equal-law false overlap | equal fair laws; no typed fixed-carrier bridge across `4 -> 8` |
| truth-import mutant | static audit fires |

The physical phase control is deliberately separate from fact co-reference.
Gauge-equivalent phase presentations localize identically.  An uncompensated
relative phase changes the operational law but neither defines nor identifies
a shared fact.

## 10. Outcome derivation

The receipt classifies 56 falsifiable rows into anchors, quotient,
localization, overlap, records, controls, and caps.  Definitions, outcomes,
and nonclaims add no scientific checks.

`RQ0-LOCALIZATION-GROUPOID` requires valid anchors, an exact operational
quotient, a nontrivial recovered localization with overlaps, the ambiguity
groupoid control, and the W3 records.  `RQ0-LOCAL-ATLAS` additionally requires
every scientific group to pass, including held-out atom matching, non-star
overlaps, explicit restriction categories, record descent, spectator,
encoding, phase, irreducibility, and equal-law controls.

The exact positive receipt returns:

$$
\begin{aligned}
\texttt{RQ0-L0-BLOCKED-AT-ADDRESS}&=\mathrm{false},\\
\texttt{RQ0-LOCALIZATION-GROUPOID}&=\mathrm{true},\\
\texttt{RQ0-LOCAL-ATLAS}&=\mathrm{true}.
\end{aligned}
$$

An observed-estimator-anchor mutant must mark the receipt invalid, suppress
all positive rungs, print no highest outcome, and exit 1.

The complete exact suite remains below the pinned 240-second cap.  Raw wall
time is not included in stored receipts, so byte determinism is not defeated
by an irrelevant clock value.

## 11. What has and has not been learned

The construction establishes the following exact finite implication:

> Given a sufficiently separating operational access contract whose
> intervention algebra admits nontrivial independently addressable factors,
> the frozen estimator can recover those factors and their overlap category
> through an encoded amplitude presentation, attach W3 records from the same
> dynamics, preserve exact ambiguity as a groupoid, and reject law-only fact
> matching.

It does not establish that generic quantum laws possess such a factorization,
that the operational access contract is uniquely selected by nature, or that
commuting addressable factors are spatial.  In particular, the addressability
postulate is load-bearing: removing preparations, probes, or independently
selectable interventions can make the quotient underdetermined.

The first unresolved object is therefore not a metric.  It is an operational
influence relation between these recovered local subinstruments, with a
screening rule that separates signalling from correlation and entanglement.
That belongs to a separately pinned `RQ0-C1` only after this L0 delivery has
survived its hostile round and terminal adjudication.

## 12. Claim register

### Definitions

- operational equivalence and reachable-support quotient;
- generator-subset intervention star-algebra;
- independently addressable factorization at the frozen finite scope;
- localized subinstrument, restriction category, meet, join, and nerve;
- basis-invariant finite W3 witness representation.

### New provisional postulates

- the finite operational access contract;
- the finite $\mu_8$ presentation-gauge scope;
- restriction to subalgebras generated by subsets of at most eight opaque
  intervention classes;
- supplied exact presentation actions as gauge/symmetry data.

### Inherited theorems

- Paper 1's W3 H-corr/H-avail record-seam result and boundary-gauge scope;
- Paper 2's fact/law/token distinction, erasure distinction, and groupoid
  allowance;
- terminal RQ0-A's typed amplitude instruments, process morphisms, and record
  pullbacks.

### Exact constructed measurements

- all dimensions, partition counts, factorization counts, category arrows,
  overlap counts, W3 rows, phase differences, groupoid arrows, and control
  outcomes in Sections 4–10.

### Conjectures and open extensions

- stability under larger or incomplete access families;
- intrinsic selection of the operational access contract;
- localization beyond the generator-subset search class;
- recovery under arbitrary exact or continuous-unitary presentations;
- whether later operational influence produces a stable causal order and
  Lorentzian cone.

## 13. Required-question answers

1. **What is quotiented?** Every inaccessible completion and every
   intervention difference invisible to all frozen preparation/context/probe
   experiments, modulo the declared finite boundary phase gauge.
2. **What makes a subinstrument addressable?** A proper non-scalar closed
   intervention algebra with a faithful commuting complement, scalar
   intersection, joint implementation, and exact product dimension.
3. **How are spectators distinguished?** Inaccessible structure vanishes in
   the reachable-support quotient; an actively prepared, controlled, and
   observed extension survives as its own noncommutative atom.
4. **How is encoding defeated?** All operations and access probes are globally
   conjugated; the estimator uses algebra relations, and none of the recovered
   atoms equals a visible slot algebra.
5. **When is localization groupoid-valued?** Exact presentation actions that
   exchange indistinguishable atoms are returned as arrows; no representative
   is selected.
6. **What are the regions and overlaps?** The 14 nonempty proper joins of four
   recovered atoms, with 50 restrictions, 66 nonempty pair meets, and 134
   nonempty triple meets.
7. **Why is the nerve non-star?** The ten record-bearing regions have empty
   total atom intersection and ten distinct nonempty pairwise meets.
8. **How are records derived?** Frozen write/preserve/erase/no-write projector
   witnesses are tested by exact H-corr, H-avail, and cross-coherence on the
   same amplitudes.
9. **Do facts descend?** Yes, on the stated `w0` triple by three explicit
   identity projector pullbacks.
10. **What happens to phase?** Exact gauge phase is quotiented; physical phase
    changes the law and is retained, but never enters fact identity.
11. **What is unresolved?** Influence and screening between recovered local
    operational algebras.
12. **What is the epistemic status?** Definitions, postulates, inherited
    theorems, exact finite measurements, and conjectures are separated in
    Section 12.

## 14. Nonclaims and halt

This unit does not construct or claim:

- influence, signalling, screening, causal precedence, or a causal cone;
- spacelike separation, dimension, volume, manifold topology, Lorentzian
  geometry, Lorentz transformations, or special relativity;
- fields, propagators, microcausality, stress, backreaction, gravity, or a
  deformation algebra;
- full $U(1)$ gauge, arbitrary-unitary subalgebra enumeration, black-box
  discovery from unrestricted unknown instruments, or independent blind
  authorship.

The result remains **GREEN-UNREVIEWED**.  It must halt after delivery and face
an external hostile round before any terminal status or `RQ0-C1` pin is
considered.
