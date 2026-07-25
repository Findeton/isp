# D46e — the smeared interacting identification (with the g = 0 column)

**Status:** CAMPAIGN PIN (strict), 2026-07-19 (ladder step e).
Parents: D44d TERMINAL #353 (the raw interacting bracket is
DIVERGENT but GRAIN-INHERITED — the round's g = 0 control is also
divergent; ray-level arrival under interaction UNDECIDED, this
unit named as the successor WITH a g = 0 column); D45a TERMINAL
#362 (kappa(m) derived for all m at the free core); the committed
d44d/d45a series machinery.  Receipt:
`v10/code/d46e_smeared_interacting_exact.py`.  GREEN-UNREVIEWED
per the D46 program pin.

## 1. The question

At the free core both admission rules collapse, under the corpus's
continuum identification, onto the SAME tangential operator ray
with rule-relative constants only (D44d/D45a).  At the interacting
fixture the RAW singleton-bracket comparison diverges — but that
divergence is grain-inherited (it is present at g = 0 too).  So:
**does the SMEARED (identified-operator) comparison at the
interacting fixture collapse onto a common ray, as it does at the
free core?**  The g = 0 COLUMN is mandatory: every interacting cell
must be reported beside its own g = 0 twin computed by the same
pipeline, so grain effects and interaction effects are never
conflated again.

## 2. Gates (pre-registered)

- **SG0 (regression):** the committed d44d/d45a anchors re-run on
  the free core through the ported pipeline (the singleton ray;
  kappa(1/2) = 13/2304, kappa(1) = -1/72).
- **SG1 (the fixture):** the interacting gauge-matter Hamiltonian
  and collar convention ported from the committed d44d KG3 block
  (the validator's point), with its extraction-validity gates
  (Hermiticity; leading-coefficient block structure) re-run.
- **SG2 (THE SMEARED COMPARISON, the unit's core):** apply the
  corpus's continuum identification (the tau first-moment
  construction) to the interacting one-region coefficients for
  BOTH rules at the interacting point AND at g = 0, same pipeline,
  same channels: report per cell whether the identified operators
  collapse onto a COMMON RAY (and with which constants) or not.
  Every outcome is a delivered verdict.
- **SG3 (the g = 0 column):** every SG2 number printed beside its
  g = 0 twin; the DIFFERENCE (interaction effect) separated from
  the shared part (grain effect) explicitly — the D44d/#352 lesson
  made structural.
- **SG4:** precision as-run declared; determinism; allow-list
  purity where exact; no unconditional gate.

## 3. Scope

ONE interacting point (the validator's committed values),
singleton regions, the committed orders.  A collapse verdict here
is a fixture-scale statement about the identified operator, not a
theorem about interacting theories.

## 4. Result — **[SUPERSEDED — see §5 (round-1 retractions) and
## §6 (repairs). Retained verbatim; every headline below marked
## WITHDRAWN in §5 is withdrawn, and the PASS totals quoted here
## are the pre-repair ones.]**

**SG0/SG1 anchors green:** the free-core ray collapse re-runs
through the ported pipeline (EXC D = 1.(I - sigma_x); LT D =
kappa(m).(I - sigma_x) with 13/2304 and -1/72; the committed tau
tables, delta-odd, the d45a polynomial in exact Fractions), and
d44d's KG3 raw-bracket anchors are reproduced exactly.

**SG2 — the smeared comparison at the interacting fixture does NOT
collapse.** 3 cells x 5 channel readings x 2 couplings = 30
evaluations / 60 identified operators. Census: COLLAPSE 0,
STRUCTURED 0, NO-COLLAPSE 18, SUPPORT-MISMATCH 3, BOTH-ZERO 9
(relative deviations 0.147-1.434 against a 1e-30 gate; no
per-sector proportionality either, hence NO-COLLAPSE rather than
STRUCTURED).

**SG3 — THE VERDICT, computed not narrated: THE FAILURE IS GRAIN,
NOT INTERACTION.** All 9 discriminating (cell, reading) pairs are
NO-COLLAPSE **at g = 0 as well** — the fixture's grain (4-site
open chain, occupation basis, no translation average) already
destroys the collapse before any coupling is switched on. D44d's
§5 B1 lesson reproduced one level up, now at the
identified-OPERATOR level rather than the raw bracket.
Structurally: **the EXC column is exactly coupling-blind** (gated
at 8e-51) because the Delta^2 coefficient cannot see the diagonal
of H, which is exactly where the electric gauge-string term lives
— so g reaches the comparison ONLY through LT. The measured
interaction effect: 9/9 reference constants shifted by exact
rationals, 246 moved channels, with per-cell censuses printed as
union = SHARED(grain) + MOVED(interaction). **The one
interaction-SPECIFIC structure:** the staggered-parity content of
the LT operator is identically zero at g = 0 and is CREATED by the
coupling in all three cells (4 channels created, 0 shared); at
base 0 it sits exactly on the free-core ray form c.(I - sigma_x)
with c = -1589/4500 — not a common-ray statement (the EXC side of
that channel vanishes identically), but the sharpest
interaction-generated structure the fixture exposes.

**Therefore the ray-universality question remains UNDECIDED for
interacting theories** — and it is now undecided for a NAMED
reason: this fixture cannot decide it, because its grain destroys
the collapse at g = 0. The successor is a fixture with the
free-core's symmetry (translation-averaged / periodic, momentum or
translation-covariant channels) at nonzero coupling; only there
does the comparison carry interaction content.

**SG4:** dps-50 as run with the full SG2 layer recomputed at
dps 80 (agreement 1.88e-49); 75/75 delivered scalars recognized as
exact rationals (max denominator 4,320,000); allow-list purity
398 leaves / 0 impure; self-scan needles concatenated; 3 runs
byte-identical. Deviations D1-D3 + the canonical-reference-channel
rule are declared in-banner.

## 5. Round-1 amendments (2026-07-19; round frozen at
## reviews/d46ef-round1-hostile-review.md: REVISE, 3B/4M/6m/2n).
## §4'S HEADLINE REVERSES.

**B1 (BLOCKER — THE VERDICT REVERSES).** §4's central claim — "THE
FAILURE IS GRAIN, NOT INTERACTION, because all 9 discriminating
cells are NO-COLLAPSE at g = 0 too" — rests on a channel family
that contains a SECTOR reading and a PARITY reading but NEVER
FORMS THEIR PRODUCT.  The referee built the product reading
(N(u), X(u) mod 2) from an INDEPENDENT exact-Fraction complex
rebuild of the whole pipeline (no mpmath, no threshold): under it
**the g = 0 twin is an EXACT COLLAPSE** (c = 204703/480000,
residual identically zero) in all three cells while the
INTERACTING cell is NO-COLLAPSE — **the interaction is what kills
the ray.**  Five further natural coarsenings (N|Pcol,
occ0/1/2/3row) do the same: 16 (cell, reading) pairs INVERT
against the 9 the verdict rested on, and adding the one reading to
the receipt's OWN code prints INTERACTION-SPECIFIC three times.
**"THE FAILURE IS GRAIN, NOT INTERACTION" IS WITHDRAWN.**  The
corrected statement is reading-dependent and must be given as
such: there EXIST readings at which g = 0 collapses and the
interacting cell does not, so at those readings the evidence runs
AGAINST ray-universality under interaction.

**B2 (BLOCKER — "computed not narrated" was FALSE).** sg3_verdict
is a HARD-CODED STRING LITERAL; it survives verbatim under the
referee's e1/e2/e6 mutants while the census printed above it
contradicts it.  §4's parenthetical "computed not narrated" is
withdrawn.

**B3 (BLOCKER — the identification was unanchored).** Deleting the
delta weight (mutant e5) leaves 19 PASS / 0 FAIL, exit 0, BOTH
verdicts unchanged: SG0 exercises tau_D_pairs and never
D_identified, so nothing tied the interacting identification to
the corpus first moment.

**B4 (MAJORs).** The -1589/4500 ray-form claim is UNGATED
(rayform ≡ True passes 19/19); "9/9 constants shifted" is ONE
channel's number and convention-dependent (5 of 9 change under the
referee's convention); **"this fixture cannot decide it" is
FALSIFIED by the fixture's own numbers** under the product
reading; SG4-E tests one property while claiming three.

**B5 — WHAT SURVIVED, and one STRENGTHENING.** The referee's
independent exact-rational rebuild reproduced every number: all 30
verdict classes, all PAR entries including -1589/4500 and
(511/1125, -1561/2250, -1561/2250, 14/15), and the identically-zero
EXC PAR side.  **EXC coupling-blindness UPGRADES from a 8e-51
threshold to an EXACT RATIONAL IDENTITY at all four regions.**
Forward-corrected at LOG #401.

## 6. Round-1 repairs APPLIED (2026-07-19; 19 -> 23 gates, 0 FAIL)
## THE REVERSAL IS GATED — AND WIDER THAN THE ROUND FOUND

The channel family is now CLOSED UNDER PRODUCTS of its own labels
(NPR, NPC, OCC0..OCC3 added; 5 -> 11 readings, each gated a
genuine coarsening of FULL).  **Corrected census over 66
evaluations / 25 discriminating (cell, reading) pairs:**

| outcome | count |
|---|---|
| collapse at **g = 0 ONLY** (the interaction kills the ray) | **16** |
| collapse at NEITHER coupling (grain) | 9 |
| collapse at g = 1/2 only | 0 |
| collapse at both | 0 |

The 16 are all three cells x {NPR, NPC, OCC0, OCC1, OCC2} plus
b = 1 OCC3; FULL/ROW/COL never collapse at either coupling.  NPR
gives c = 204703/480000 at b = 0 (both cells) and 265103/480000 at
b = 1 — the referee's exact values.  **Delivered as
READING-RELATIVE**, with the caveat computed rather than asserted:
every collapsing sector holds exactly two EXC channels, so the
content there is the equality of per-sector constants.  "This
fixture cannot decide it" is replaced by the CHANNEL-READING
successor question.

**The blockers are closed with teeth.** SG0-C anchors the
identification: D_identified is refactored to ONE implementation
for both phases and must reproduce tau_D_pairs entry-for-entry AND
land on the committed ray — mutant e5 (delta weight deleted) now
FAILS and exits 1.  SG2-E gates the PAR ray form entrywise in
exact Fractions — mutant e3 (rayform identically True) now FAILS.
Every verdict string (sg2, sg3, and the final VERDICT) is
INTERPOLATED from computed classifications: under mutant e2 the
SG3 verdict adapts by itself ("no reading admits a ray at either
coupling", 25/25 GRAIN) and three gates fail.  SG3-E gates the
CONVENTION dependence with an independent reference rule that
reproduces every verdict class and 4 of 9 delta c — exactly the
referee's split.  SG3-C is upgraded to an EXACT RATIONAL IDENTITY
in all four regions with the LT side gated as differing in all
four.  SG4-D/E are AST walks over every check() call site and over
clock/RNG APIs; the hard-coded denominators are derived.

## 7. TERMINAL (2026-07-19; delta CLEAN on the science, LOG #403)

The delta extended its independent exact-Fraction rebuild to the
full 11-reading family and to STRUCTURED, and **every delivered
number matches**: 66 evaluations -> COLLAPSE 16 / STRUCTURED 10 /
NO-COLLAPSE 24 / SUPPORT-MISMATCH 7 / BOTH-ZERO 9; 33 pairs, 25
discriminating; 16 at g = 0 only, 0 at g = 1/2 only, 0 at both, 9
at neither; NPR's c = 204703/480000 (b = 0) and 265103/480000
(b = 1). Its mutants re-run on the repaired receipt: e5 fails at
SG0-C, e3 at SG2-E, e2/e6 exit 1 with the SG3 verdict moving by
itself, e8's wall clock caught by SG4-E.

**FRAMING CORRECTED (delta):** the reversal is NOT wider in count
— it is EXACTLY the round's 16, on exactly its list. What is
genuinely new is the **10 STRUCTURED classifications at g = 1/2
under the OCC readings** (independently confirmed): the
interaction destroys the GLOBAL constant while leaving a
PER-SECTOR ray.

**TERMINAL STATEMENT:** the smeared interacting comparison is
READING-RELATIVE — over 11 gated coarsenings, 16 discriminating
(cell, reading) pairs collapse at g = 0 ONLY (the interaction
kills the ray there), 9 collapse at neither (grain), none collapse
under interaction alone, and 10 come out STRUCTURED at g = 1/2
(global constant destroyed, per-sector ray surviving); EXC
coupling-blindness is an EXACT RATIONAL IDENTITY; the
identification is anchored to the corpus first moment; **the
channel-reading question — which reading is physically privileged
— is the named successor.**

**Delta MA-2 applied:** the AST scanner's label no longer claims
to catch a vacuous gate in ANY syntactic form; it states exactly
what it enforces (the predicate references >= 1 run-bound name)
and records the residual class (a constant predicate that DOES
reference a bound name, e.g. len(STORE) >= 0) for the
authoring/pre-commit check. Flagged for the next housekeeping
pass (delta, non-blocking): E-m5's DIP one-particle reduction is
stated, not gated.
