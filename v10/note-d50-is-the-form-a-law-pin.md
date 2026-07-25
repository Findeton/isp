# D50 — is the stationary FORM a law, or a choice? (PIN)

**Status:** PIN, STRICT, 2026-07-25.  Committed BEFORE any receipt
code exists.  Parent: D49 TERMINAL (LOG #418/#419, round 1 frozen at
`reviews/d49-round1-hostile-review.md`, delta at #420).  This unit
exists because of that round's **BLOCKER B2**, and it is the residue
B2 created.

## 1. What B2 established, and the question it leaves

D49 settled the dichotomy in favour of horn (II): a **root-free
completion EXISTS**, exactly what paper 30 §5.7 declared
`[OPEN, declared]`, and `Zhat(h) = lambda^(-|h|) f(class(sigma(h)))`
is one.  That result is untouched by this pin.

What B2 refuted was the *account of uniqueness*.  D49 sold it as a
consequence of an invariance demand — "among completions that do not
distinguish record points the law identifies, there is exactly one".
Measured at depth-4 truncation `[MEASURED, tangent-space counts at
b*, hence LOWER BOUNDS on freedom]`:

| demand | boundary directions still FREE |
|---|---|
| renewal-pair agreement | **308 of 313** |
| bisimulation-invariance of the completed class-to-class transfer at every interior cut | **119 of 313** |
| paper 30 §5.7's FORM (`Z` = state function × `lambda^(-depth)`) | **0** (one ray) |

So uniqueness comes from a **postulated SHAPE for `Z`**, not from any
invariance principle stated on the record.  Hence the standing
restriction: *"the record law is forward-complete" is true of the law
PLUS that form and may not be quoted without it.*

> **THE QUESTION.  Is there a demand stated on the RECORD — on what is
> observable in the generated structure — that FORCES the stationary
> form?  If yes, the form is a LAW and the restriction lifts.  If no,
> the form is a CHOICE and must be carried at every citation, forever.**

## 2. The candidate that makes this sharp

The invariance B2 measured (I2 below) constrains the transfer *cut by
cut*.  It says nothing about whether the same class-to-class step has
the same probability at different **depths** — and that is a
record-level statement, not a statement about `Z`.

**Pre-registered family of demands, all stated on the record:**

- **I1 — renewal agreement.**  Record points the law identifies price
  identically.  (D49's E2; 308/313 free.)
- **I2 — bisimulation invariance.**  The completed class-to-class
  transfer is a function of the classes at every interior cut.
  (B2's measurement; 119/313 free.)
- **I3 — DEPTH-STATIONARITY.**  The completed class-to-class transfer
  is the same *at every depth*: the probability of stepping from class
  `s` to class `s'` does not depend on when it happens.  **This is the
  primary target.**
- **I4 — I2 + I3 together.**

## 3. Pre-registered expectation, with its argument, recorded BEFORE running

**EXPECTED: I3 FORCES THE FORM.**  Sketch, to be either confirmed and
made rigorous, or refuted:

Write `r(h, e) = Z(h+e)/Z(h)`.  I2 makes `r` a function of
`(class(h), class(h+e))`; call it `r(s, s')`.  Consistency of `Z`
along every path then makes `r` a discrete gradient on the class
graph *up to a constant factor per step*: `r(s, s') = g(s')/(c·g(s))`.
That is exactly `Z(h) = c^(-|h|) g(class(h))` — **the form** — with `c`
fixed by normalization, hence `c = lambda = 2` by D49's C1/C2.

If that argument is sound, the form is a **consequence of a
record-level demand** and B2's restriction lifts.

**Recording the expectation before the measurement is the point.**  D49
was corrected precisely for selling a conclusion its evidence did not
carry, and this pin must not repeat it.

## 4. THE ONE-SIDEDNESS DOCTRINE (binding on every statement)

Tangent-space dimension counts at `b*` are **local**.  Therefore:

1. **A count > 1 (modulo overall scaling) is RIGOROUS in the negative
   direction**: it exhibits nearby non-proportional completions
   satisfying the demand, so the demand does **not** force the form.
   This may be stated as a refutation.
2. **A count of 1 is LOCAL EVIDENCE ONLY.**  It does not prove global
   uniqueness, and **no statement of the form "the demand forces the
   form" may be made from a tangent count alone** — it requires the
   §3 argument discharged as a proof.
3. Every conclusion carries its truncation depth.

## 5. Gates (SF-series)

- **SF0 ANCHOR.**  The d42a layer exec'd path-anchored from the
  committed `d42b3_placement_exact.py`; `sigma` and the class map from
  the committed d44a/D49 sources; D49's `Zhat` reproduced.  Reproduce
  B2's two numbers (308, 119 at depth-4) as a port check — a
  disagreement is anchor breakage, exit 1.
- **SF1 THE DEPTH SWEEP.**  For truncation depths `D = 2..5` (as far
  as exhaustively feasible; the reached depth is PRINTED, never
  silently capped), compute for each demand I1–I4 the tangent-space
  dimension of admissible boundary perturbations at `b*`, **and** the
  dimension of the induced space of distinct COMPLETIONS (the image,
  which is the quantity that matters — B1's lesson is that boundary
  dimensions and completion dimensions are different objects).
- **SF2 THE TREND IS THE RESULT.**  Report, per demand, whether the
  completion-space dimension **shrinks toward 1 with depth** or
  persists.  Both outcomes are deliverables.
- **SF3 I3 DECIDED.**  Whether depth-stationarity alone leaves exactly
  one ray of completions, at every depth reached.
- **SF4 THE PROOF, OR ITS ABSENCE.**  If SF3 returns one ray, §3's
  argument is to be discharged as a written proof with its steps gated
  where mechanical; if it cannot be discharged, the result is reported
  as `[MEASURED, local]` and the restriction **stays**.
- **SF5 CAPACITY / ANTI-VACUITY.**  At each depth the constraint count,
  the rank, and the *effective* (non-vacuous) constraint count are
  printed.  A demand that is vacuous at shallow depth must not read as
  a constraint.
- **SF6 NEGATIVE CONTROL.**  A demand known NOT to force the form (I1,
  which B2 measured at 308/313 free) must come back free at every
  depth.  If I1 tightens to a ray, the instrument is broken: exit 1.
- **SF7** AST anti-vacuity scan, labelled to exactly what it enforces
  (LOG #403 MA-2); witness branches live AND exercised (LOG #354 F1);
  determinism gated across `PYTHONHASHSEED` 0/7/61/999 (D49's own A4
  defect makes this non-optional).

## 6. Falsifier

- **I3 leaves > 1 ray at any reached depth** ⟹ the form is a genuine
  CHOICE; B2's restriction is permanent and must be carried at every
  citation of D49 forever.  A real result, reported at exit 0.
- **SF0 or SF6 failing** ⟹ instrument or anchor breakage, exit 1.

## 7. Scope

d42a, delivery-free, two actors — the same scope as D49 and no wider.
Whatever this unit decides, **transport scope remains open**, and that
is where the dichotomy is still genuinely undecided for a theory that
has delivery and merge in it.

## 8. Why this matters more than it looks

If I3 forces the form, then D49's settlement stops being conditional
on a modelling choice and becomes a statement about the law: *the
record law is forward-complete, full stop, at d42a scope.*  If I3 does
not, then the honest headline of the whole line is weaker than
currently written, and the brief's Part XII must say so.

Either way this is the cheapest remaining question with the largest
effect on what may be claimed.
