# v14 R6a — THE REFINEMENT GRAMMAR (pin)

**Frozen:** 2026-08-09, v14 ledger #25.  **Charter authority:** the
user-ordered amendment (#24).  **Runs in parallel with R3** (disjoint
files; R3's verdict is not an input).  **Paper number:** `paper-04` —
deliverables `v14/paper-04-refinement-grammar.md`,
`v14/code/r6a_refinement_exact.py`, `_output.txt`, `_receipt.json`.
**Discipline:** RUNBOOK §13/§14/§15 with every addendum; all five
2026-08-09 engravings at birth, each compliance gate shipping its
injection-falsifier; exact arithmetic only.

## 1. Base and the grammar-source decision

Pinned sources (hash-verified + path-value anchored at run time):

- **I7** — `v13/code/ha_successor_receipt.json` (`542b8735daf0`), R0
  row: sites (ℤ_L)^d, links, the interval counts n_ℓ(x) (division
  events in the record interval), the front n(x), H_a[N] with the
  transported second step, record-IS-metric.
- **The HA paper and code as construction/legitimacy references** —
  `v13/paper-ha-successor.md` (`f286ba10d2d9`),
  `v13/code/ha_successor_exact.py` (`d44cb72f8ee9`): carry the
  GW1-§1.2 permitted list (event counts, record adjacency) and the
  exact definitions.  Read-only references; nothing imported.

**The scope ruling this pin makes:** the question is posed at I7's own
declared level.  If, at any point, deciding a move's legitimacy
requires a grammar fact NOT derivable from these pinned sources (e.g.
the deeper v10/v11 renewal grammar), the unit STOPS that branch and
returns `R6A-BLOCKED-AT-GRAMMAR-SOURCE-<the needed fact, named
precisely>` — a first-class verdict, not a failure.  Reaching outside
the pinned sources is forbidden.

## 2. The question (falsifiable, three-way)

**Does the record grammar, as pinned, admit a MOTIVATED
interval-subdivision move** — a refinement in which a new site exists
*because a division event resolved a record interval* — with the count
partition forced by the counting semantics and the residual freedom
measured, not smuggled?

The semantic anchor (from I7's own declaration): n_ℓ(x) *counts
division events in the interval*.  Therefore, if an interval is
subdivided at a new site y, **count additivity is forced**:
n(x,y) + n(y, x+ℓ) = n(x, x+ℓ) (events in the whole = events in the
parts) — this is semantics, not a choice.  What is NOT automatically
forced: which split (n₁, n₂) occurs; what the new site's transverse
links carry; whether the front value n(y) at the new site is
determined; whether the arena class (ℤ_L)^d is preserved.  Those are
exactly what the unit measures.

## 3. Registered measurements

1. **The move census (the design space as data).**  Enumerate the
   subdivision-move classes expressible from the pinned declarations:
   (a) axis-hyperplane insertion (subdivide every interval crossing a
   declared hyperplane — preserves (ℤ_{L+1} × ℤ_L^{d−1})-type
   structure); (b) global dyadic refinement (every axis interval
   subdivided — L → 2L); (c) single-interval insertion (one link only
   — expected to break the arena class; if so, REFUSED with the
   measured reason, never skipped).  For each class: is the refined
   object again an I7-class arena (sites/links/counts/front all
   defined)?  Gated, cell-complete.
2. **The forced part, verified:** count additivity holds by
   construction in every admissible move (gated); the coarse metric is
   recovered from the refined counts on coarse intervals (the
   restriction test: record-IS-metric commutes with refinement) —
   measured at every admissible move class, every record in a declared
   record family (reuse I7's declared record family, rebuilt from the
   pinned receipt).
3. **The choice inventory (the motivation audit — the unit's core).**
   For each admissible move class, enumerate the residual freedoms:
   the split (n₁, n₂) fiber; the new site's transverse-link counts;
   the new front value n(y); the insertion locus.  For each freedom:
   is it (i) forced by a pinned declaration (name it), (ii) fixed by a
   symmetry of the pinned structure (measure the stabilizer), or
   (iii) genuinely free (COUNT the fiber exactly)?  **The verdict's
   motivation qualifier is computed from this inventory** — the RSQ
   standard: a move whose every freedom is class-(i) or class-(ii) is
   MOTIVATED; any class-(iii) freedom is named in the verdict with its
   fiber size.
4. **The dynamics-compatibility census.**  For each admissible move
   class: refine-then-advance vs advance-then-refine — compute
   H_a[N]-refinement commutation exactly (both drag architectures A
   and B; the declared lapse family lifted/restricted in the declared
   way, with the lift itself audited for choices).  **A nonzero
   commutation defect is a measured object**: its site-support, its
   dependence on the split, its record dependence — characterized,
   not just reported (the v12 precedent binds).
5. **The iteration probe.**  For the best-motivated move class: apply
   it twice (two refinement steps); measure whether the composite is
   again a move of the class (the family closes) and whether the
   choice inventory grows, stays fixed, or collapses under iteration
   — the first data on whether a refinement FAMILY (R6b's
   prerequisite) exists.

## 4. Verdicts (first-class, all computed in-gate, comparator
independent, every segment flippable)

- `R6A-MOTIVATED-REFINEMENT-EXISTS-<move class; the forced list; the
  choice inventory (empty or stabilizer-fixed); the commutation
  defect status; the iteration result>` — R6b's gateway.
- `R6A-NO-MOTIVATED-SPLIT-<the obstruction: which freedom is
  irreducibly class-(iii), with its measured fiber>` — the continuum
  question then provably needs input beyond the pinned grammar.
- `R6A-BLOCKED-AT-GRAMMAR-SOURCE-<the named needed fact>` — per §1.
- Mixed outcomes compose (e.g. EXISTS at one move class, NO at
  another): the verdict carries the per-class table.

## 5. Controls and falsifiers (minimum set)

- **The R1 negative control:** a label-growth copying move (append a
  disjoint block) run through the same audit MUST come out
  unmotivated/foreign (its choice inventory names the free label
  rule) — the audit must be able to fail a move.
- **Additivity-violation mutant** dies on the forced-part gate;
  restriction-test mutant dies on the metric-commutation gate;
  choice-inventory corruption (a class-(iii) freedom relabelled
  class-(i)) dies on the inventory gate; commutation-defect
  suppression dies; move-census drop dies cell-complete; the five
  verdict injection classes with falsifiers at birth; path-drift per
  anchor row; never-falsified census in the receipt from delivery
  one.

## 6. Scope honesty

This unit decides whether the substrate's own dynamics defines its
refinement.  It takes no scaling limit (R6b's job, gated on this
unit's EXISTS), measures no invariant trajectories, and claims
nothing about R3's algebra.  All three verdicts are terminal-grade;
NO-MOTIVATED-SPLIT would be the strongest negative in the programme's
continuum line — the statement that the continuum question is
unposable from inside the pinned grammar.
