# D47 — the sphere rung (PIN)

**Status:** PIN, STRICT, 2026-07-25.  Committed BEFORE any receipt
code exists.  Parents: D46c (exact rational M^{2+1} certificates,
TERMINAL), D46d (the typicality retraction), D45b §1 (the SCOPING
DOCTRINE), the user's binding §1 observation.

## 1. Why this unit exists, and why the previous instrument was wrong

D45b §1 already forbids reading order dimension as a
spacetime-dimension estimator.  The user's observation — **"3+1
spacetime is not 4 clocks, it's infinite clocks"** — is the reason,
and it is binding on this line: the causal order of real Minkowski
space needs unboundedly many linear extensions, so a program that
climbs 2 -> 3 -> 4 by COUNTING clocks is climbing toward the wrong
number.  D46d is what that looks like from the inside: "width
spreads with depth" survived only through an idle-counting proxy
(0.981 -> 0.672 -> 0.414 as the proxy tightened) and its
discriminating scalings collapsed.

**So this unit stops counting and starts constructing.**  What
distinguishes 2+1 from 3+1 is not a number of clocks but the
SHAPE OF THE SKY: the set of directions leaving an event is a
CIRCLE in 2+1 and a 2-SPHERE in 3+1.  Those are separated by a
finite, exact, decidable invariant (§2), so the question becomes
computable on finite records with integer arithmetic.

## 2. The separator, and the ONE-SIDEDNESS DOCTRINE (binding)

In 2+1 the shadows other events cast on an event's sky are ARCS of
a circle; in 3+1 they are CAPS of a 2-sphere.  Two classical facts
separate those families, and **both are to be GATED BY EXPLICIT
CONSTRUCTION in this unit, never asserted from literature:**

- **arcs on a circle cannot shatter 4 points** (four points in
  cyclic order admit no connected arc containing the 1st and 3rd
  but not the 2nd and 4th); they CAN shatter 3;
- **caps on a 2-sphere CAN shatter 4 points** (four points in
  convex position; the hard case, two opposite edges of a
  tetrahedron, is separated by a plane parallel to both).

Two instruments follow, with DIFFERENT logical strengths:

- **INSTRUMENT 1 — CIRCULAR-ONES (two-sided on ARC-REALIZABILITY).**
  A 0/1 incidence matrix is an arc system iff its columns admit a
  cyclic order making every row's ones contiguous.  Decidable
  exactly.
- **INSTRUMENT 2 — SHATTER-4 (one-sided OBSTRUCTION).**  A
  shattered 4-set proves the system is NOT an arc system, by a
  route independent of Instrument 1's algorithm.

**THE ONE-SIDEDNESS DOCTRINE, binding on every statement this unit
produces:**

1. **Shatter-4 found => NOT arc-realizable => the sky is not a 2+1
   celestial sky UNDER THE COMMITTED SKY DEFINITION.**  This is an
   obstruction certificate and may be stated as such.
2. **Circular-ones HOLDS => the system is arc-realizable.  This is
   CONSISTENT WITH 2+1 AND IS NOT EVIDENCE OF IT**, still less
   proof: arcs are necessary, not sufficient, for a 2+1 sky, and a
   discrete sky need not be an arc system or a cap system at all.
   No statement of the form "the sky IS a circle" may be made.
3. Every conclusion is stated CONDITIONAL ON THE SKY DEFINITION.

## 3. The sky definitions — THREE, committed here (the D46e lesson)

"The direction set at an event" is a CONSTRUCTION CHOICE, not
something the grammar hands over.  D46e is the precedent: the
"grain not interaction" headline reversed once the channel reading
was varied.  **Therefore three definitions are committed before
any run, all three are reported, and a result holding under only
one is READING-RELATIVE and must be said that way.**

Given a poset C and a base event e:

- **SKY-A (cover sky).**  Directions = the minimal elements of the
  strict future of e (its covers).  Shadows = for each f strictly
  above e, S_f = {c : c <= f}.
- **SKY-B (antichain sky at depth d).**  Directions = a committed
  maximal antichain in the strict future of e; shadows as in A.
  d is committed per run and printed.
- **SKY-C (past sky, the dual).**  Directions = the maximal
  elements of the strict past of e; shadows = for each f strictly
  below e, S_f = {c : f <= c}.

## 4. Gates (SG-series), fixed here

- **SG0 THE SEPARATOR, CONSTRUCTED.**  Build an explicit arc
  system on a circle and verify it shatters 3 and CANNOT shatter
  4; build an explicit exact-rational cap system on S^2
  (Pythagorean-quadruple points, Fraction dot-products against
  Fraction thresholds) and verify it DOES shatter 4 and FAILS
  circular-ones.  **No claim in §2 is taken from literature.**
- **SG1 INSTRUMENT VALIDATION (D47a, BEFORE ANY TRANSPORT DATA).**
  Both instruments must exhibit a true positive AND a true
  negative on the SG0 systems, and must agree with each other
  wherever both apply.  A blind or trigger-happy instrument is
  breakage: exit 1.
- **SG2 CAPACITY, GATED FIRST — NOT DISCOVERED AFTERWARD.**  A
  sky with fewer than 4 directions, or with too few distinct
  shadows, CANNOT shatter 4 for reasons that have nothing to do
  with geometry.  For every sky examined the receipt prints
  |directions|, |distinct shadows|, and whether the shatter-4
  question is DECIDABLE there at all.  **"No shattering" over an
  undecidable stratum is reported as UNDECIDABLE, never as a
  negative result.**
- **SG3 THE 2+1 CONSISTENCY CHECK.**  D46c's committed `W3_CERT`
  — 18 exact rational M^{2+1} points, already gated by that
  receipt's own verifier at 0/306 — has its skies computed under
  all three definitions.  Under the doctrine this is a CONSISTENCY
  CHECK, not a control: if a genuine 2+1 record shattered 4, the
  sky definition (not Minkowski) would be at fault, and the unit
  would halt and re-pin.
- **SG4 THE TRANSPORT SKIES (D47b).**  All three definitions over
  the committed fixtures, capacity gated first, every sky's
  verdict reported.
- **SG5 THE CONSTRUCTION-MATCHED NULL (the D46f lesson).**  Before
  any circular-ones failure is read as structure, it is compared
  against a null built to share the construction's forced
  features (down-closure, the same size profile).  A failure the
  null also produces is a CONSTRUCTION TAUTOLOGY and is reported
  as one.
- **SG6 POSITIVE CERTIFICATES (D47c) — only if SG4 finds non-arc
  skies.**  Exhibit exact rational cap centres and thresholds on
  S^2 realizing the observed shadow system, verified by Fraction
  dot-products — the structural analogue of D46c's 2+1 work.
- **SG7 NO SILENT CAPS.**  Circular-ones is decided by exhaustive
  cyclic-order search below a committed size; above it the sky is
  reported UNDECIDED-BY-CAP with its size.  The cap and the count
  of skies hitting it are PRINTED.  Silent truncation reads as
  coverage and is forbidden.
- **SG8 ANTI-VACUITY.**  AST scan of every `check()` predicate.
  **Label scope (LOG #403 MA-2): it enforces "references >= 1
  run-bound name" and NOTHING MORE.**
- **SG9 WITNESS BRANCH LIVE (LOG #354 F1, binding).**  A shattered
  4-set is a WITNESS and an exit-0 outcome, wired live and
  EXERCISED through the same reporter by an SG0 cap system.

## 5. PRE-REGISTERED EXPECTATION

**Most likely outcome: CAPACITY INSUFFICIENT.**  At four to six
actors the skies are probably too small to shatter anything, and
the honest deliverable is then the validated instrument plus a
certified statement of the width that would be required.  This is
recorded now, before the run, because pre-registering the boring
outcome is the cheapest defence against later talking oneself into
an exciting one.

Secondary: arc-realizable skies at every reachable width WITH
capacity demonstrably sufficient — a conditional cap at 2+1 under
the committed definitions, which is a real negative and would
redirect the line.

## 6. Falsifier / halt conditions

- SG0 or SG1 misbehaving => instrument breakage, exit 1.
- SG3 producing a shattered 4-set on genuine M^{2+1} points =>
  **HALT AND RE-PIN**: the sky definition is wrong, not Minkowski.
- SG5 showing the null reproduces a failure => that failure is a
  construction tautology and is reported as one, not as structure.

## 7. Deliverable

D47a (instrument + separator, standalone), D47b (transport skies),
D47c (positive certificates, conditional).  A hostile round after
D47b regardless of outcome.  Nothing from this unit may be cited
by any paper before that round: GREEN-UNREVIEWED, per the
quarantine that kept papers 30/31/32 intact through the D46 sweep.
