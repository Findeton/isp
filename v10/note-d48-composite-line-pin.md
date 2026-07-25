# D48 — what is a composite in record terms? (PIN)

**Status:** PIN, STRICT, 2026-07-25.  Committed BEFORE the receipt
exists.  Parent: `note-d41c-step3-bridge-declarations.md` §1A —
this question is recorded there as **the sole unblocking condition
for the entire d41c laboratory program**, promoted to a named
successor at LOG #405 after the author's scale/layer objection.

## 1. The question, and why it is INTERNAL

d41c is blocked because both bridge declarations identify a
laboratory system with ONE record line, across ~20 orders of
magnitude and at least three unbuilt layers.  §1A found the
defensible reading to be the EFFECTIVE one — that the record
structure coarse-grains at laboratory scale into something that
behaves as a single line — and found the corpus has no
coarse-graining theorem to support it.

The narrowest internal form of that question, and the only part
answerable without the missing layers:

> **Is the grammar CLOSED under actor coarse-graining?**  If the
> actors of an admissible record are merged into groups, is the
> image an admissible record of the coarsened system?

If YES, a composite genuinely is one line and the identification
is at least internally coherent.  If NO, the actor decomposition
is not a free choice: an aggregate is irreducibly many lines, and
any bridge that treats a many-constituent object as one line is
measuring the LINE COUNT — which is exactly the failure mode
named as d41c's top risk.

## 2. Pre-registered expectation

**NOT CLOSED.**  Two actors may propose on the same base version;
their merged image would be one actor proposing twice on a base
its own line has already left, which the grammar should reject.
Recorded before the receipt so the expectation cannot be fitted
afterwards.

## 3. Gates (CG-series)

- **CG0 ANCHOR.**  The layer exec'd path-anchored from the
  committed `d42b3_placement_exact.py`; admissibility decided
  ONLY by membership in that layer's own `candidates_for` output,
  never by a re-implemented predicate.
- **CG1 EQUIVARIANCE CONTROL (the instrument check).**  Under a
  BIJECTIVE actor renaming the image must be admissible for
  **100%** of histories — the grammar must not care what actors
  are called.  Anything less is instrument breakage, not a
  finding: exit 1.
- **CG2 IDENTITY CONTROL.**  The identity map must give 100%.
  Exit 1 otherwise.
- **CG3 THE MERGE TEST.**  Non-injective maps over several
  partitions (2->1, 4->2, 3->1, 4->1) and several groupings, each
  reported separately.  The admissible fraction is reported per
  map; no map's number is merged with another's.
- **CG4 THE FAILURE IS EXHIBITED, NOT COUNTED.**  The first
  non-admissible image of each map is printed in full with the
  index at which admissibility breaks, so the mechanism is on the
  record rather than inferred from a percentage.
- **CG5 DEPTH DEPENDENCE.**  The admissible fraction is reported
  per history length.  A fraction that falls with depth means
  failure is generic; one that is constant means it is a
  boundary effect.  Stated either way.
- **CG6 THE DUAL — REFINEMENT.**  The converse question: can one
  actor be SPLIT into two with the image still admissible?  If
  neither merging nor splitting is closed, "how many lines an
  object is" is not a matter of description at all.
- **CG7 ANTI-VACUITY.**  The tested stratum must be non-empty and
  its size printed; an AST scan of every `check()` predicate,
  labelled with the LOG #403 MA-2 scoping (it enforces
  "references >= 1 run-bound name" and nothing more).

## 4. What this unit may and may NOT conclude

**May:** whether the grammar admits an actor-coarse-graining
functor, as an exact internal fact about the committed layer.

**MAY NOT:** anything about ions, molecules, constituents, or
mass.  The step from "actors" to "physical constituents" is
ITSELF a bridge, of exactly the kind §1A blocked.  A negative
result here does NOT become "a molecule is many record lines"; it
becomes "IF constituents are actors, THEN the composite is
irreducibly many lines" — and the antecedent stays unsigned.

## 5. Falsifier

CG1 or CG2 below 100% => instrument breakage, exit 1.  CG3
returning 100% for every map => closure holds, the pre-registered
expectation is FALSIFIED, and d41c's §1A blocker weakens
substantially — a result to report loudly, not to bury.

## 6. Deliverable

An exact statement of whether actors are aggregable, plus the
disposition for d41c §1A: does the blocker stand, weaken, or lift.
