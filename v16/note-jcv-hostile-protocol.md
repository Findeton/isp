# JCV independent hostile-review protocol

Status: **FROZEN BEFORE ANY JCV REVIEWER IS COMMISSIONED**.

Immutable review target commit:
`35c2511657efbee6c1c1887f2d7626faa4d396ea`.

Candidate hashes:

- fixture `ad887c213d14781838c6e70227b8f2c162f1392a08060de7c6e57829a8db012b`;
- scorer `66b87bdf68f7210d959e13bfacae4c5957413e6d8f234647bfe3ad4a19619a03`;
- paper `b54858c394fe22626ef1e233781737b7199cc56bf816f52e8aae063a99deaefc`;
- transcript `b1d950c804c8b568514f1a0206853496b2f578650a3d98187e64c1c8a9b70d6d`;
- receipt `a1b0baeee418d3f2c82e1ec6d07993cb51f69f3f51d63a9996dae9fb177fe3d1`.

The candidate primary is `JCV-STRATIFIED`; its active-locus word is
`JCV-PAIRING-SELECTED-WEIGHTS-FREE`.  These are claims under review, not panel
premises.

## Independence wall

Three reviewers work from the target files and this protocol only.  They may
read the PIN, solver freezes, failed-run/repair record, candidate, receipt,
code, and cited corpus anchors.  They must not read, list, summarize, or receive
any other JCV reviewer report before their own report is frozen.  They may not
edit candidate files, shared status files, or one another's report paths.

Reports are delivered verbatim to distinct paths:

- algebraic geometry / quantifier seat:
  `v16/review-jcv-algebra.md`;
- operator / instrument / ontology seat:
  `v16/review-jcv-operator.md`;
- gravity / covariance / composition seat:
  `v16/review-jcv-gravity.md`.

Every report must state its read set, tool/runtime, independent constructions,
exact discrepancies, grade, and SHA-256.  Allowed grades are `ACCEPT`,
`ACCEPT-WITH-FIXES`, and `REJECT`.

## Common required rebuild

Each seat must independently, without importing `jcv_score.py` as an oracle:

1. check all five artifact hashes and the total receipt seal;
2. reconstruct the four holonomy invariants from raw chart-sign gauge and
   verify the orbit quotient;
3. solve or analytically derive the nonempty shared-law and
   independent-triangle-control sectors;
4. reproduce the active/dark split and every reported algebraic dimension;
5. verify the two rational active witnesses, all-input completeness, and the
   moving calibrated probability;
6. test whether the global and active classifier words follow from the frozen
   decision table rather than from prose;
7. audit the first-run failure and scorer-only repair for result leakage or a
   moved physical rule;
8. list every sentence whose scope is stronger than its certificate.

Zero numerical discrepancies must be reported explicitly, not implied.

## Seat A — algebraic geometry and quantifiers

Rebuild the ideals independently.  Audit the Buchberger bases, saturation
nonemptiness, leading-ideal dimension, sign-to-holonomy reduction, real versus
algebraic-closure quantifiers, radical/nonreduced risks, component structure,
and gauge quotient.  Decide whether two rational points plus a nonconstant
remainder suffice for the stated physical-weight freedom.  Challenge the
words `fixed point`, `selected`, `stratified`, `dark`, and `dimension two`.

Mandatory countermodel hunt: vary only an assumption that the paper calls
declared—real slice, nondegenerate binary calibration, isometry, or shared
law—and determine which conclusion changes.  Do not silently enlarge the
registered primary scope; label every such result as a conditional extension.

## Seat O — operator, instrument, and ontology

Rebuild the Kraus identities for all inputs, not just the two displayed
witnesses.  Audit complete positivity, trace preservation, outcome typing,
the meaning of coherent columns versus durable rows, probability calibration,
and whether the active observable movement is operational or basis artifact.
Check that the dark strata really are rank-deficient and dynamically silent.

Then audit the ontology and consequence ledger: comparison map as
representation, weight as nomological data, actualization as postulate, fixed-
boundary versus growing-factorization no-signalling, EPR/steering,
Hamiltonian/Lindbladian reconstruction, particles/species, and all-arity
composition.  A valid boundary instrument must not be promoted into any of
those absent structures.

## Seat G — gravity, covariance, and composition

Determine whether the comparison maps have any earned cross-carrier physical
referent or merely provide a calibrated coordinate dictionary.  Audit the two-
triangle overlap as a local coherence test, the shared-law homogeneity
declaration, the independent-triangle control, and the claim that the deepest
circularity was narrowed.  Test whether a third overlap/associativity or full
refinement system could overturn the local conclusion.

Check the paper's analogies against primary sources on cylindrical
consistency, quantum causal histories, quantum measure/decoherence
functionals, and associator/pentagon coherence.  Decide whether any geometry,
backreaction, covariance, Lorentz, continuum, GR, affine/cosmological
constant, or phenomenology language escaped its wall.

## Pre-registered kill and repair rules

Any of the following requires `REJECT` or an explicit primary demotion:

- a false nonempty-sector key, dimension, witness, probability, orbit, or
  control count;
- an untyped sum between different boundary spaces;
- calling algebraic-closure nonemptiness a real solution without a real
  certificate where the claim needs one;
- treating the declared comparison doctrine, shared-law homogeneity, or
  actualization as derived;
- treating a silent/dark mismatch as active pairing selection;
- treating fixed-boundary CPTP as a growing-factorization no-signalling
  theorem;
- promoting the fixture into geometry, backreaction, an all-n field,
  particles, constants, a Hamiltonian, continuum recovery, or QFT/GR
  deviation;
- evidence that the serializer repair changed physical truth or saw a result
  before its refreeze.

Minor prose, citation, formatting, or additional-gate defects may earn
`ACCEPT-WITH-FIXES` only if the exact primary and its scope survive.  Reviewers
must give the smallest falsifying or repairing construction, not just a wish
list.

## Panel rule

Each report is committed verbatim as it arrives, before another report is
shared with that reviewer.  Joint reading begins only after all three hashes
are frozen.  The adjudicator must resolve every material finding, recompute any
disputed value, update `STATUS.md`, and issue an ordered repair or terminal
refusal.  No candidate repair is authorized by this protocol alone.
