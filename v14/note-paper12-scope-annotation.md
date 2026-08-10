# PAPER-12 (Γ-MAIN) — SCOPE ANNOTATION, NOT AN ERRATUM

**Status:** registered by the Γ-iteration joint adjudication
(`v14/note-giter-adjudication.md`, §2, commit ddfd7ee) and written here
as a standing note. **Paper-12 is terminal and is not edited.** Its
claim was true of its own object; what follows records which object
that was, and where a different object gives a different answer.

---

## 1. The two objects

Γ-main's §5.4 concludes:

> at every depth-cut triple with a non-degenerate first cut, **no
> interpolant of eq. 22's form** exists.

*Eq. 22's form* is the **square, padded** object: the three cuts of a
triple are embedded in one enlarged configuration space, the first
transfer is completed to a square matrix under a declared padding
convention, and the candidate interpolant is then the unique algebraic
solution of a determined system.

Paper-16's `b3_problem` asks a different question, in its own words:

> does a COLUMN-STOCHASTIC non-negative Ḡ exist with
> Γ(dd←d) = Ḡ · Γ(md←d)?

**Rectangular, unpadded, no enlarged configuration space.** This is a
feasibility question over a polytope, not the solution of a determined
system.

The two are not the same question, and neither answer transfers to the
other. Γ-main's statement is true of the padded object at 4 of 4
triples. Paper-16's statement is true of the rectangular object at 3 of
4.

## 2. The cell where they diverge: MENU-113, (1, 2, 4)

At the contrast carrier MENU-113, at the depth-cut triple (1, 2, 4),
**both hold at once**:

| object | verdict at MENU-113 (1, 2, 4) |
|---|---|
| eq. 22's unique padded candidate | carries **104 negative entries** — no interpolant of that form exists |
| the rectangular column-stochastic feasibility problem | **FEASIBLE**, with a verified primal point in 413 variables and 258 equations |

The comparison cell is (1, 2, 3): 121 variables against 94 equations,
and there the rectangular problem is **infeasible** with a verified
Farkas vector. The other two triples, (1, 3, 4) and (2, 3, 4), are
infeasible and Farkas-certified as well.

The mechanism is visible and is the point of the annotation. **The
padding converts an underdetermined feasibility question into a
determined algebraic one.** Completing the first transfer to a square
invertible matrix makes the candidate unique; a unique candidate that
fails positivity refutes existence *of that candidate*. But the
unpadded feasible set can be non-empty at the same cell, and at
(1, 2, 4) it is.

## 3. The corpus-wide scope note

Registered by the adjudication and carried prominently in paper-16:

> **EQ-22 NEGATIVITY DOES NOT IMPLY NON-EXISTENCE OF A STOCHASTIC
> INTERPOLANT.**

This is a **standing caution for every eq-22-based refutation in the
corpus.** It is demonstrated at 1 of 4 cells in one unit; nothing here
says how often it bites elsewhere, and that is precisely what is not
known. Any refutation resting on eq-22 negativity is scoped to the
padded object unless the rectangular column-stochastic question has
also been asked.

## 4. What this note does and does not do

- It **does not** retro-edit paper-12 or any other terminal paper.
  Their claims were form-scoped and remain true at their own scope.
- It **does not** weaken Γ-main's §5.4 as stated. The refutation of
  eq.-22-form interpolants survives entirely.
- It **does** annotate the reading of that row: the 4-of-4 is a
  statement about eq. 22's padded form, and the rectangular
  column-stochastic question — answered in paper-16 — separates 3-of-4,
  diverging at MENU-113 (1, 2, 4).
- It **does** put the separation question on the successor register:
  re-run the corpus's eq-22-based refutations against the rectangular
  feasibility question, and measure how often the two diverge. Paper-16
  has shown that they *can*; nothing tells us the rate.

## 5. Provenance

The measurements above are paper-16's, at `v14/code/giter_exact.py`,
gated at `G-B3-ROW-DECOMPOSED` and `G-B3-COUPLED`: 772 row problems
over 8 (carrier, triple) cells with 0 infeasible and 772 certificates
verified; both coupled verdict directions certificated — a feasible
verdict returns a primal point re-substituted into the constraints, an
infeasible verdict returns a Farkas vector re-checked against
y·A ≤ 0 and y·b > 0. The eq.-22 census is gated at `G-EQ22-STAMPED`,
bound per cell rather than per field. All eight coupled verdicts were
independently re-solved and re-proved from their certificates by the
operator seat under an independent simplex implementation.
