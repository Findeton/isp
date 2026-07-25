# D46e + D46f — round 1, hostile review (one round, two units)

**Reviewer:** independent referee (fresh session; no build context).
**Date:** 2026-07-24.  **Objects under review (both GREEN-UNREVIEWED,
first round; the LAST round of the three-round D46 sweep):**

- **UNIT 1 — D46e (LOG #389):** `v10/note-d46e-smeared-interacting.md`,
  `v10/code/d46e_smeared_interacting_exact.py`,
  `v10/data/d46e_smeared_interacting_exact.out`.
- **UNIT 2 — D46f (LOG #388):** `v10/note-d46f-reception-dynamics.md`,
  `v10/code/d46f_reception_dynamics_exact.py`,
  `v10/data/d46f_reception_dynamics_exact.out`.

Nothing in this review edits a committed file.  The two sibling rounds
(`d46ac-round1-hostile-review.md`, `d46bd-round1-hostile-review.md`)
were read first; their five standing failure patterns —
(i) prose/verdict strings asserting more than the gates deliver and
surviving a retraction, (ii) a NEGATIVE that is an artifact of a
restricted or mismatched comparison, (iii) controls and scanners that
cannot fire or advertise more coverage than they enforce, (iv) a proxy
measuring something other than the headline, (v) "the theory's own
law" claims over a disclaimed layer — **all recur here: (i)+(ii)+(iii)
in D46e, (i)+(iii)+(iv) in D46f.**

For D46e the referee built an **independent exact-rational
(`fractions.Fraction`) reimplementation of the whole interacting
pipeline** — no mpmath, no floats — from the note's and receipt's
stated definitions, and re-derived every SG2/SG3 number from it.  For
D46f the referee read the committed `d42b2` `View` class and reasoned
about the receipt's gate dependency graph, then confirmed each
conclusion by probe.

---

## COMBINED VERDICT

| unit | verdict | BLOCKER | MAJOR | minor | nit |
|---|---|---|---|---|---|
| **D46e** — the smeared interacting identification | **REVISE — the arithmetic is exactly right and independently reproduced, but the unit's single headline REVERSES: under sector-resolved coarsenings of the receipt's own channel family the g = 0 twin COLLAPSES and the interacting cell does not** | 3 | 4 | 6 | 2 |
| **D46f** — reception dynamics | **REVISE — the extraction (RD1-a) is real and reproduces, but the two headline findings (the abelian monoid, the click identity) are construction tautologies: RD1-b and RD3-b are strict logical consequences of RD1-a and cannot fire** | 2 | 5 | 5 | 2 |

**One line each.**

- **D46e.** Every gate reproduces byte-identically and every number the
  referee could recompute in exact rational arithmetic is **exactly
  right** — the 30 verdict classes, the PAR entries including
  `-1589/4500`, the identical-EXC-column fact (which the referee can
  strengthen from "8e-51" to *exact*).  But **SG3's headline reverses.**
  The receipt's channel family contains a sector reading (SEC) and a
  parity reading (PAR) and never forms their product.  The referee did:
  under `(N(u), X(u) mod 2)` — and under four further natural
  coarsenings — **the g = 0 twin is an exact COLLAPSE (one rational
  constant, residual exactly 0) in all three cells while the
  interacting cell is NO-COLLAPSE.**  Run through the receipt's *own*
  code (referee mutant e1) it prints
  `INTERACTION-SPECIFIC (COLLAPSE -> NO-COLLAPSE)` three times — and the
  `[SG3 VERDICT]` line still says "the failure to collapse is GRAIN,
  not interaction", because that verdict is a **hard-coded string
  literal**, not the computed object the note calls it.  Separately,
  **nothing in the receipt ties the interacting identification to the
  corpus first moment**: deleting the `delta` weight (mutant e5) gives
  19 PASS / 0 FAIL, exit 0, verdict strings unchanged.
- **D46f.** The receipt is clean, fast, byte-reproducible, and RD1-a —
  an independent re-implementation of the committed `View` semantics,
  gated on 23,069 instances — is a genuine and valuable gate.  But the
  two things the note and LOG #388 lead with are not findings.  The
  committed `View` is *constructed from a down-closed index SET*
  (`View.__init__(acts, pred, idxs)`), so order-independence is
  definitional; and the extracted `ACT(s,e,a)` is a **join with a
  record-determined increment**, so it commutes with everything.
  Formally: **once RD1-a passes, RD1-b and RD3-b cannot fail** — both
  are theorems about a faithful function, not measurements.  "sigma is
  an ABELIAN MONOID under reception ... strictly stronger than the
  pin's disjointness gate" is a restatement of the `View` constructor.
  Likewise RD1-d's "delivered finding" that `ko/kc/ka` are the exact
  identity is read off the constructor's own filter: `View` only ever
  looks at `p/r/d/m` records; click and noop records are *not in the
  state space at all*.

---

# UNIT 1 — D46e (LOG #389), the smeared interacting identification

## 1.1 What the referee confirms (independent recomputation)

The referee rebuilt the fixture, the collar, the series exponentials,
`Gamma = |U|^2`, the Neumann inverse, the `J` coefficients and the tau
first moment **in exact `Fraction`-valued complex arithmetic** (file
`scratchpad/ref_d46e.py`, reproduced in the appendix).  This is a
genuinely independent path: the receipt is mpmath-binary at dps 50 with
a 1e-30 threshold; the referee's arithmetic has no threshold at all.

| claim | source | referee finding |
|---|---|---|
| receipt reproduces | rerun | **exit 0, 19 PASS / 0 FAIL, byte-identical** to `v10/data/d46e_smeared_interacting_exact.out`; 24.8 s wall (LOG #389 says 25 s — matches) |
| kappa(1/2) = 13/2304, kappa(1) = -1/72 from `(9m^4-15m^2+4)/144` | SG0-B | confirmed by hand: `(9/16-15/4+4)/144 = (13/16)/144 = 13/2304`; `(9-15+4)/144 = -1/72` |
| SG2 census COLLAPSE 0 / STRUCTURED 0 / NO-COLLAPSE 18 / SUPPORT-MISMATCH 3 / BOTH-ZERO 9 | SG2 CENSUS | **all 30 verdict classes reproduced exactly**, with an exact zero/nonzero proportionality test rather than a 1e-30 threshold |
| support sizes (24/52, 12/14, 40/50, 14/14, 4, 0 …) | SG2 table | reproduced channel-for-channel in every cell, reading and coupling |
| PAR entries at b = 0: `-1589/4500, 1589/4500, 1589/4500, -1589/4500` | SG3 VERDICT / note §4 | **exactly confirmed**, both cells (r <= 3 and r <= 2), and the ray form `c*(I - sigma_x)` with `c = -1589/4500` is correct |
| PAR entries at b = 1: `511/1125, -1561/2250, -1561/2250, 14/15` | SG3 VERDICT | **exactly confirmed**, and correctly *not* on the ray |
| the LT PAR content is identically zero at g = 0 | SG3 VERDICT | **exactly confirmed** (all four entries exactly 0, all three cells) |
| the EXC PAR side vanishes identically | SG3-C / SG3 VERDICT | **exactly confirmed** (all four entries exactly 0 at both couplings, all three cells) |
| "the EXC column is EXACTLY coupling-blind (gated 8e-51)" | SG3-C, note §4, LOG #389 | **confirmed and STRENGTHENED**: in exact rational arithmetic the Delta^2 EXC region coefficient at `g = 1/2` and at `g = 0` are *entrywise identical rationals* for all four regions `n0 = 0,1,2,3`, and the LT coefficients differ for all four.  The receipt's numeric bound understates its own result |
| the canonical-reference-channel rule is load-bearing | declared banner | **confirmed**: mutant e4 (bare argmax) makes `SG4-A` fail at 0.107 — the naive convention really is precision-broken.  The declaration is honest and the rule is needed |
| the zero-sum lemma (SG2-B) and the SEC BOTH-ZERO consequence | SG2-B | confirmed structurally: row/column sums of the `Gamma` order-p>0 coefficients vanish, hence so do the commutator's, hence the sector-summed first moment vanishes because the coefficients are N-block-diagonal (SG1-C).  The referee reproduces SEC BOTH-ZERO in all six (cell, coupling) pairs |
| note §4's cited scalars: 246 moved channels; 75/75 exact; max denominator 4,320,000; 398 leaves / 0 impure; dps-80 agreement 1.88e-49; deviations 0.147–1.434 | note §4 vs `.out` | all six check out verbatim against the printed run (`0.146674` rounds to `0.147`) |

**Nothing in this unit is arithmetically wrong.**  What is wrong is the
inference drawn from the arithmetic, and the fact that the inference is
typed rather than computed.

## 1.2 Findings

### BLOCKER E-A1 — SG3's headline REVERSES: the g = 0 twin COLLAPSES under sector-resolved coarsenings, and the interacting cell does not

**Where.** `note-d46e-smeared-interacting.md` §4, "**SG3 — THE VERDICT,
computed not narrated: THE FAILURE IS GRAIN, NOT INTERACTION.** All 9
discriminating (cell, reading) pairs are NO-COLLAPSE **at g = 0 as
well**"; receipt `sg3_verdict` (lines 1039-1054) and the `[VERDICT]`
block (lines 1205-1243); LOG #389's title line ("**THE INTERACTING
FAILURE IS GRAIN, NOT INTERACTION**") and its "**SG3 THE VERDICT ...
all 9 discriminating cells are NO-COLLAPSE AT g = 0 TOO**".

**The defect.**  The receipt pre-registers five channel readings and
declares (D2) that the family "is this receipt's construction".  It
runs FULL, ROW, COL, **PAR** (a parity reading) and **SEC** (a
particle-number-sector reading) — and never forms the obvious product
of its own two coarse readings.  The referee did.

Define `NPR(i, j) = (N(u_i), X(u_i) mod 2)` — the receipt's SEC label
refined by the receipt's PAR label on the row index.  It is a
coarsening of ROW, which is a coarsening of FULL; it is inside the
declared construction, not outside it.  In **exact rational
arithmetic**:

| cell | reading | g = 1/2 | g = 0 |
|---|---|---|---|
| b=0, r<=3 | `NPR` | NO-COLLAPSE (4 EXC / 6 LT ch) | **COLLAPSE**, `c = 204703/480000`, residual **exactly 0** |
| b=0, r<=2 | `NPR` | NO-COLLAPSE (4/6) | **COLLAPSE**, `c = 204703/480000` |
| b=1, r<=2 | `NPR` | NO-COLLAPSE (4/6) | **COLLAPSE**, `c = 265103/480000` |

The g = 0 channel values, exactly (cell b = 0, r <= 3):

```
g=0  EXC: (N=1,p=0)= 6           (N=1,p=1)= -6
          (N=3,p=0)= -6          (N=3,p=1)= 6
g=0  LT : (N=1,p=0)= 204703/80000   (N=1,p=1)= -204703/80000
          (N=3,p=0)= -204703/80000  (N=3,p=1)= 204703/80000
```

— a clean single-constant ray, `D^LT = (204703/480000) * D^EXC`.  At
`g = 1/2` the LT side acquires a **sector-N=2 channel with no EXC
partner** and the N=1/N=3 magnitudes split, and the collapse is
destroyed.  Under this reading **the interaction is exactly what kills
the ray**, which is the opposite attribution to the one the unit
delivers.

This is not one lucky reading.  The referee scanned eighteen
coarsenings of FULL built from the fixture's own labels.  Five of them
show the same inversion, in **every** cell:

| referee reading | definition | g = 1/2 | g = 0 | cells |
|---|---|---|---|---|
| `N|Prow` | `(N(u), X(u) mod 2)` | NO-COLLAPSE | **COLLAPSE** | 3/3 |
| `N|Pcol` | `(N(v), X(v) mod 2)` | NO-COLLAPSE | **COLLAPSE** | 3/3 |
| `occ0row` | `(N(u), u_0)` | NO-COLLAPSE | **COLLAPSE** | 3/3 |
| `occ1row` | `(N(u), u_1)` | NO-COLLAPSE | **COLLAPSE** | 3/3 |
| `occ2row` | `(N(u), u_2)` | NO-COLLAPSE | **COLLAPSE** | 3/3 |
| `occ3row` | `(N(u), u_3)` | NO-COLLAPSE | **COLLAPSE** | 1/3 (2 cells SUPPORT-MISMATCH both sides) |

That is **16 (cell, reading) pairs in which the g = 0 twin collapses
onto a common ray with an exact rational constant and the interacting
cell does not** — against the 9 pairs on which the unit's verdict
rests.

**Run through the receipt's own code.**  Referee mutant e1 adds the one
reading `NPR` to `READINGS` and changes nothing else.  The receipt's
own twin-labelling machinery prints, verbatim:

```
b=0 r<=3 NPR : g=1/2 NO-COLLAPSE  c = 414469/4320000 | g=0 COLLAPSE  c = 204703/480000 | ... | INTERACTION-SPECIFIC (COLLAPSE -> NO-COLLAPSE)
b=0 r<=2 NPR : g=1/2 NO-COLLAPSE  c = 1050769/4320000 | g=0 COLLAPSE  c = 204703/480000 | ... | INTERACTION-SPECIFIC (COLLAPSE -> NO-COLLAPSE)
b=1 r<=2 NPR : g=1/2 NO-COLLAPSE  c = 366859/2880000 | g=0 COLLAPSE  c = 265103/480000 | ... | INTERACTION-SPECIFIC (COLLAPSE -> NO-COLLAPSE)
[SG2 CENSUS] ... COLLAPSE 3; STRUCTURED 0; NO-COLLAPSE 21; ...
[SG2 VERDICT] MIXED: 3 COLLAPSE / 0 STRUCTURED cells — see the table above.
```

with `reldev = 4.17817e-51` and `7.25903e-51` at g = 0 (the receipt's
own gate is 1e-30), matching the referee's exact zeros.  **The receipt's
own classifier calls these pairs INTERACTION-SPECIFIC.**

**Why the receipt could not see it.**  Its own SG2 declaration states
the rule correctly — "*a collapse [at FULL] implies a collapse in every
coarsening; a NON-collapse here does NOT imply one*" — and then the
SG3 verdict reasons in exactly the forbidden direction: from
NO-COLLAPSE at FULL/ROW/COL at g = 0 to "the grain destroys the
collapse before any coupling is switched on".  The receipt states the
one-way implication and then uses it backwards.

**Prescribed fix.**  Retract "THE FAILURE IS GRAIN, NOT INTERACTION"
from note §4, from `sg3_verdict`, from the final `[VERDICT]` block and
from LOG #389 (title line and body) with a forward-correcting entry.
Re-run the sweep with the family closed under products of its own
labels (at minimum SEC x PAR, and the `(N, u_k)` site-occupation
readings), and deliver the honest finding: **the verdict class is
reading-relative, and the two attributions co-exist — the failure is
grain in the finest readings and interaction in the sector-resolved
coarsenings.**  That is a stronger and more interesting result than the
one claimed, and it is what the receipt's own numbers say.

### BLOCKER E-A2 — the SG3 verdict is a hard-coded string literal; note §4's "computed not narrated" is false

**Where.** Receipt lines 1039-1054 (`sg3_verdict = ( "the D44d §5 B1
lesson holds ... " )` — a plain literal with every number typed in);
`note-d46e-smeared-interacting.md` §4, "**SG3 — THE VERDICT, computed
not narrated**".

**The defect.**  `sg2_verdict` (lines 899-911) *is* data-gated: it
switches to `"MIXED: {n_collapse} COLLAPSE ..."` when the census moves.
`sg3_verdict` has no such guard.  Its "In all 9 discriminating (cell,
reading) pairs", its "9/9 constants shifted", its "**The one genuinely
INTERACTION-SPECIFIC structure in the whole sweep is the PAR
channel**", its `-1589/4500` and its `511/1125, -1561/2250, ...` are all
typed characters.  The computed census variables (`n_grain`,
`n_ispec`, `disc_same`, `par_int`, lines 1003-1009) are printed on the
line above and **not used** in the verdict.

**Demonstrated.**  In mutant e1 the receipt prints, three lines apart:

```
[SG3 CENSUS] 12/15 ... 6/15 are INTERACTION-SPECIFIC ...
[SG3 VERDICT] ... The one genuinely INTERACTION-SPECIFIC structure in the whole sweep is the PAR channel ...
```

In mutant e2 (the g = 0 twin silently *not* set to zero coupling) the
census reads `0/15 are INTERACTION-SPECIFIC` and the verdict still
announces the PAR interaction-specific structure.  In mutant e6 (the LT
operator replaced by the EXC one, so *everything* collapses) SG2
correctly reports `18 COLLAPSE` and `MIXED`, and the SG3 verdict still
says "the failure to collapse is GRAIN".  This is the sibling rounds'
pattern (i) with the pattern (ii) aggravation built in: a retraction of
SG2's finding leaves SG3's prose standing.

**Prescribed fix.**  Rebuild `sg3_verdict` from `TWIN`, `n_grain`,
`n_ispec`, `disc_same`, `par_int` and the recognized PAR rationals, the
way `sg2_verdict` is built, with an explicit `MIXED`/`INVERTED` branch;
and strike "computed not narrated" from note §4 until it is true.

### BLOCKER E-A3 — no gate anchors the interacting identification to the corpus FIRST MOMENT; deleting the moment weight passes 19/19

**Where.** `D_identified` (receipt lines 686-699); the banner's
"*THE IDENTIFICATION AT THE INTERACTING FIXTURE (declared BEFORE any
verdict) ... the corpus construction is the tau FIRST MOMENT*"; SG0's
claim to be "the free-core regression **through the ported pipeline**"
(note §2, §4).

**The defect.**  SG0 exercises `tau_D_pairs` (lines 220-241) — the
free-core function.  Every interacting number comes from
`D_identified` (lines 686-699) — a **second, independent
implementation** of the same formula.  No gate compares them, and no
gate checks that `D_identified` weights `tau` by `delta` at all.  SG2-C
(coarsening consistency) and SG2-B (zero-sum) are both invariant under
dropping the weight.

**Demonstrated (mutant e5).**  Replace `D[c_] += d_ * v` by
`D[c_] += v` — i.e. compute the zeroth moment instead of the first,
which is a different physical object and not the corpus construction at
all:

```
[SUMMARY] 19 PASS / 0 FAIL          (exit 0)
[SG2 CENSUS] COLLAPSE 0; STRUCTURED 0; NO-COLLAPSE 6; SUPPORT-MISMATCH 5; BOTH-ZERO 19.
[SG2 VERDICT] NO COMMON RAY at the interacting fixture under ANY reading of the channel family ...
[SG3 VERDICT] ... the failure to collapse is GRAIN, not interaction ...
```

Every gate passes; both headline verdicts print unchanged.  The
regression anchor advertises coverage of the pipeline that it does not
enforce — the sibling rounds' pattern (iii), on the unit's load-bearing
code path.

**Prescribed fix.**  Add a gate that runs `D_identified` on the
free-core data and requires it to equal `tau_D_pairs` entry-for-entry
(they are the same formula on a common input), or refactor so that one
function serves both phases.  Until then, no printed interacting number
is anchored to the committed corpus identification.

### MAJOR E-M1 — the `-1589/4500` ray-form claim is ungated

**Where.** `rayform` (lines 745-752); `par_form` (line 803-810) is
populated and printed and **never referenced by a `check()`**; the claim
is nevertheless promoted to note §4 ("at base 0 it sits exactly on the
free-core ray form c.(I - sigma_x) with c = -1589/4500"), to
`sg3_verdict` and to LOG #389.

**Demonstrated (mutant e3).**  Replace `rayform`'s body by
`return True, d00`.  Result: **19 PASS / 0 FAIL, exit 0**, and the
delivered record now asserts that the identically-zero EXC PAR object
is "on the free-core ray: YES, c = 0" — a false physics statement in a
green receipt, undetected.

**The referee independently confirms the value is correct** (exact
rational rebuild).  The finding is that a true number is riding on an
ungated print, in a corpus whose whole discipline is that delivered
claims are gated.

**Prescribed fix.**  Gate `par_form`: assert the ray form holds at b = 0
in both cells with the recognized constant `-1589/4500`, fails at b = 1
with the four recognized entries, and is undefined (zero object) at
g = 0 — and route the note/LOG sentence to that gate's detail string.

### MAJOR E-M2 — "9/9 reference constants shifted by exact rationals" is not a measurement of the interaction

**Where.** note §4 ("The measured interaction effect: 9/9 reference
constants shifted by exact rationals, 246 moved channels"); `sg3_verdict`
("what the interaction changes there is only the reference constant
(9/9 constants shifted)"); LOG #389 ("Measured interaction effect: 9/9
constants shifted by exact rationals").

**The defect, two parts.**

1. *It is one channel's number, not a global one.*  `ref_key` selects
   the reference from `D^EXC`, and SG3-C establishes `D^EXC` is
   **identical** at both couplings — so the same channel `k*` is chosen
   in both columns and
   `delta c = [D^LT_{g}(k*) - D^LT_{0}(k*)] / D^EXC(k*)`.
   "9/9 constants shifted" therefore says exactly: *the LT operator
   moved at one arbitrarily-selected channel in 9 of 9 cells*.  Given
   that the same table already reports 246 moved LT channels, a zero
   here would have been the surprise; the statistic cannot carry the
   weight "the measured interaction effect".
2. *It is convention-dependent.*  The reference-channel rule is
   declared, but the resulting numbers are artefacts of it.  The
   referee's independent rebuild used a different, equally canonical
   rule (first nonzero channel in `str` order) and reproduces **4 of the
   9** printed constants (`867463/1440000`, `-92993/160000`,
   `216121/480000`, `-680437/1440000`) and changes the other **5**
   (e.g. b=0 r<=3 FULL: receipt `1856189/4320000`, referee
   `618263/1440000`).  All 30 **verdict classes** agree — the receipt is
   right that the class is reference-free — but `delta c` is not an
   invariant of anything.

**Prescribed fix.**  Either report a reference-free interaction
measure (e.g. the exact rational `D^LT_g - c_0 * D^EXC` residual norm,
or the per-channel shift vector, both of which the receipt already has)
or demote "9/9 constants shifted" to a declared convention-relative
diagnostic and strike "the measured interaction effect" from note §4
and LOG #389.

### MAJOR E-M3 — "this fixture cannot decide it" is an over-general excuse, and the prescribed successor rests on it

**Where.** note §4 ("**Therefore the ray-universality question remains
UNDECIDED for interacting theories** — and it is now undecided for a
NAMED reason: this fixture cannot decide it, because its grain destroys
the collapse at g = 0.  The successor is a fixture with the free-core's
symmetry ... only there does the comparison carry interaction
content"); LOG #389 ("ray-universality under interaction remains
UNDECIDED, now for a NAMED reason — this fixture cannot decide it").

**The defect.**  The named reason is E-A1's false premise.  The fixture
*does* carry interaction content: under six sector-resolved
coarsenings, in 16 (cell, reading) pairs, the g = 0 twin collapses onto
an exact common ray and the coupling destroys it.  The successor
prescription ("a fixture whose grain ADMITS the free-core collapse at
g = 0") is thereby answered *inside this fixture* for those readings —
so the honest successor is not a new fixture but the **channel-reading
question**: which coarsening is the right continuum analogue of the
free-core spinor channel, and is the collapse-at-g=0 a genuine ray or
an artifact of two-channels-per-sector plus the sum rule.  (The referee
notes the latter is a real caveat: within a sector with exactly two
channels the zero-sum lemma forces proportionality, so the substantive
content of the `NPR` collapse is the *equality of the two sector
constants* — nontrivial, but a weaker object than the free-core ray.
That caveat belongs in the delivered record, and it does not rescue the
GRAIN attribution.)

**Prescribed fix.**  Replace the "cannot decide" clause with the
computed statement of E-A1, name the two-channels-per-sector degeneracy
explicitly, and re-derive the successor from the surviving open
question.

### MAJOR E-M4 — SG4-E's determinism gate asserts three properties and tests one weak proxy; SG4-D's self-scan advertises coverage it does not enforce (the standing CARRIED findings, recurring)

**Where.** SG4-E (lines 1181-1187): label = "no RNG is loaded, **no wall
clock is read**, and **no output ordering depends on hash
randomization** ... rerun byte-identical under any PYTHONHASHSEED";
predicate = `'random' not in sys.modules`; detail = the hard-coded
string "modules touched by this receipt: mpmath, fractions, sys, os".
SG4-D (lines 1170-1179): four literal needles
`check(True`, `check(1,`, `check(not False`, `check(bool(True)`.

**Demonstrated (mutant e8).**  Add `import time; _WALL = time.time()` and
a gate `check("...", len(str(_WALL)) >= 0, "always true")`.  Result:
**20 PASS / 0 FAIL, exit 0**; SG4-D reports "occurrences across 4
needles = 0"; SG4-E reports "'random' loaded: False; modules touched by
this receipt: mpmath, fractions, sys, os" — a **false** detail line,
since `time` is now imported and read.  A genuinely vacuous gate written
in any non-literal form survives, exactly as the d46bd round found.

Note the contrast with the sibling unit: **D46f's RD4-e is a real
internal determinism gate** (reversed-traversal SHA-256 identity over
every delivered aggregate).  D46e has no internal determinism arm at
all; note §4's "3 runs byte-identical" is a runner claim, not a receipt
claim.

**Prescribed fix.**  (a) Make SG4-E's predicate test what its label
says, or shorten the label to "no RNG module is loaded" — and compute
the module list from `sys.modules` instead of typing it.  (b) Give the
receipt a D46f-style reversed-iteration digest gate.  (c) Replace the
literal needles by an AST walk over `check()` call sites that flags any
predicate with no free variable bound in the run (the standing
CARRIED finding, now three rounds old).

### minor E-m1 — hard-coded counts make the sweep un-extensible and the census non-self-describing

`SG2-A` requires `n_eval == 30` (line 829); `SG3-B` requires
`len(TWIN) == 15` (line 1000); the `[SG3 CENSUS]` f-string types the
denominator `/15` twice (lines 1010-1012) while computing the
numerators; SG2-B's detail types "over all 32 coefficients" and
"all {len(CELLS)*2}" inconsistently.  In mutant e1 this produced the
absurd line "`12/15 ... 6/15 are INTERACTION-SPECIFIC`" over 18 pairs.
Fix: derive every denominator from the live containers.

### minor E-m2 — SG3-A's "the g = 0 column is a real control" is carried by `tot_moved > 0`

Lines 957-964.  The gate's label promises that the twin "is a real
control and not a copy of the interacting one"; the predicate is
`part_ok and tot_moved > 0`.  Mutant e2 shows it does fire in the
degenerate copy case — so it is not vacuous — but it is satisfied by
*any* nonzero LT motion whatever, which SG3-C guarantees a priori for a
coupling that enters through LT.  Fix: state the gate as what it is (a
non-degeneracy check) and stop billing it as the control that
establishes the twin's validity.

### minor E-m3 — the g = 0 twin's comparability is verified only on the Hamiltonian, not on the derived structures

SG1-B gates that the two Hamiltonians differ only on the diagonal.  The
referee checked the rest and **acquits the twin**: same basis, same 16
dimensions, same particle-number sectors, same collar decomposition,
same extraction-validity behaviour, and the EXC leading coefficients
exactly equal.  But the receipt never gates the sector structure or the
support pattern of the twin — a twin that silently changed the block
structure would be caught only incidentally.  Fix: add the sector/
support comparison to SG1-B's detail (the numbers are already computed).

### minor E-m4 — "under ANY reading of the channel family" is the load-bearing scope clause and it does not survive into the note's §1 or the LOG

`[SG2 VERDICT]` is correctly scoped ("of the channel family").  Note §4
compresses to "the smeared comparison at the interacting fixture does
NOT collapse", and the note's §1 question ("does the SMEARED comparison
collapse onto a common ray?") is answered without the qualifier.  Given
E-A1 this scope clause is the difference between a true and a false
statement.  Fix: carry it everywhere.

### minor E-m5 — the displacement analogue is declared but unanchored

`DIP` (line 300) is the receipt's declared fixture analogue of the
free-core lattice displacement, justified in-banner by "a hop across
one bond shifts X by exactly 1, so this reduces to the free-core
lattice displacement on the one-particle sector".  That reduction is
stated, never gated.  Mutant e7 (replace `DIP` by particle number) is
caught only incidentally, by `SG3-A`'s moved-channel count.  Fix: gate
the one-particle-sector reduction directly against `tau_D_pairs`.

### minor E-m6 — SG1-D's re-anchor tolerances are asymmetric and undeclared in the note

`|C^exc|` at 1e-30, `|C^LT|` at 1e-8, per-sector kappa at 1e-20, rel dev
at 1e-5 (lines 634-640).  The 1e-8 and 1e-5 slots exist because the
committed d44d strings were printed at 8 and 6 significant digits; that
is legitimate and the receipt says so in the gate label, but note §2/§4
describe SG1 as "re-run exactly".  Fix: one clause in note §4.

### nit E-n1 — "3 cells x 5 channel readings x 2 couplings = 30 evaluations / 60 identified operators" appears in note §4 without the D2 deviation flag that makes the family the receipt's own construction; the deviation is declared only in §4's last paragraph.

### nit E-n2 — LOG #389 says "the ladder's last step closes" and "THE D46 LADDER IS COMPLETE"; with E-A1 outstanding, step e is not closed.  A forward-correcting entry should say so explicitly rather than leaving the completion claim standing.

## 1.3 Mutation table — D46e

| id | mutation | expected if the gates cover the claim | observed | verdict |
|---|---|---|---|---|
| **e1** | add one reading `NPR = (N(u), X(u) mod 2)` to `READINGS` | the SG3 verdict adapts | 3 cells print `INTERACTION-SPECIFIC (COLLAPSE -> NO-COLLAPSE)`; SG2 flips to `MIXED: 3 COLLAPSE`; **`[SG3 VERDICT]` unchanged, still "GRAIN, not interaction"**; only failure is the literal `len(TWIN) == 15` | **BLOCKER E-A1 + E-A2** |
| **e2** | the g = 0 twin silently given `G_INT` (not a twin at all) | SG3-A fires | `SG3-A` **FAILS** (moved = 0), exit 1 — control works; but `[SG3 VERDICT]` still narrates the PAR interaction-specific structure against a `0/15` census | control OK; **E-A2** |
| **e3** | `rayform` returns `True` unconditionally | some gate fires | **19 PASS / 0 FAIL, exit 0**; the record now claims the zero EXC object is on the free-core ray with `c = 0` | **MAJOR E-M1** |
| **e4** | `ref_key` -> bare `argmax` | the declared canonicalization is load-bearing | `SG4-A` **FAILS** at 0.107 | declaration **vindicated** |
| **e5** | `D_identified` drops the `delta` weight (zeroth moment) | the identification anchor fires | **19 PASS / 0 FAIL, exit 0**, both verdicts printed unchanged | **BLOCKER E-A3** |
| **e6** | `D^LT := D^EXC` (a total-collapse world) | SG2 + SG3 both adapt | SG2 correctly `MIXED: 18 COLLAPSE`; `SG3-A` and `SG4-A` fail (exit 1); `[SG3 VERDICT]` still "GRAIN, not interaction" | partial; **E-A2** |
| **e7** | `DIP` displacement replaced by particle number | a displacement anchor fires | caught only incidentally by `SG3-A` (moved = 0) | **minor E-m5** |
| **e8** | `import time` + a vacuous gate written as `len(str(x)) >= 0` | SG4-D and SG4-E fire | **20 PASS / 0 FAIL**; SG4-D "0 occurrences"; SG4-E prints the now-false module list | **MAJOR E-M4** |

## 1.4 Independent-recomputation inventory — D46e

Built from scratch in exact `Fraction` complex arithmetic
(`scratchpad/ref_d46e.py`, `scratchpad/scan_d46e.py`); no mpmath, no
float, no threshold.

- fixture `H(g)` for `g in {1/2, 0}`; region collars for `n0 = 0..3`;
  `exp` series to order 4; `Gamma = |U|^2`; Neumann inverse; `J`
  coefficients at `Delta^2` (EXC) and `Delta^4` (LT).
- **30/30 SG2 verdict classes reproduced.**
- **All 12 PAR entry-rows reproduced exactly**, including `-1589/4500`,
  `511/1125`, `-1561/2250`, `14/15`, and the identically-zero rows.
- **EXC coupling-blindness established exactly** (entrywise rational
  equality, all four regions), strengthening the receipt's 8.02e-51.
- **LT coupling-dependence established exactly** (all four regions).
- 4 of 9 reference constants reproduced under an independent reference
  convention; 5 changed (E-M2).
- SEC BOTH-ZERO reproduced in all 6 (cell, coupling) pairs, with the
  structural reason (block-diagonality + vanishing row/col sums).
- 18-reading coarsening scan: 6 readings x 3 cells classified at both
  couplings; **16 (cell, reading) pairs with COLLAPSE at g = 0 and
  NO-COLLAPSE at g = 1/2** (E-A1).
- `kappa(1/2) = 13/2304`, `kappa(1) = -1/72` re-derived by hand from the
  d45a polynomial.

---

# UNIT 2 — D46f (LOG #388), reception dynamics

## 2.1 What the referee confirms (independent recomputation)

| claim | source | referee finding |
|---|---|---|
| receipt reproduces | rerun | **exit 0, 29 PASS / 0 FAIL, byte-identical** to `v10/data/d46f_reception_dynamics_exact.out`; 9.5 s wall (LOG #388 says ~10 s — matches) |
| 23,069 instances / 228 pre-states / 869 repeated keys / 7,163 pairs / 63 overlapping / 635 of 1107 / 171 lossy fibers / 72 v.arb / 41,326 leaves | note §4, LOG #388 vs `.out` | every cited scalar checks out verbatim |
| **RD1-a is a genuine and valuable gate** | RD1-a | **confirmed.** `ACT` is a real independent re-implementation of the committed `View` semantics and it is gated on every enumerated instance.  Referee mutants f1 and f3 both break it as they should.  This is the unit's real contribution |
| the RD1-b control genuinely fires and genuinely can fail to fire | RD1-b CONTROL | **confirmed.** Referee mutant f5 (control state made index-free, so it cannot fire) is **caught** — the receipt exits 1.  A properly wired control |
| the lossy control (171) and the alien control | RD2-d, RD1-e | confirmed |
| RD2-b's mechanism: `deliver_options_in_view` filters the SENDER's holdings only | RD2-b | **confirmed by code reading** (`d42b2` lines 218-220: `for v in view.holdings(a)` where `a` is the sender) |
| **re-delivery really is admissible in the committed layer** | RD4-b | **confirmed independently**: `admissible([pA0, rA1, d(A,B,v1)], d(A,B,v1), ('A','B','C'))` returns `(True, Fraction(1,16))`, and B **already holds** `v1` in that view.  The RD2-b finding is a property of the committed admission rule, not an artefact of the receipt-built fixture.  **Attack (d) is acquitted** |
| PROBE-DD is load-bearing and declared | RD4-b | **confirmed**: referee mutant f4 (PROBE-DD removed) makes RD2-b **FAIL** — the finding really does ride on the probe, exactly as declared |
| "`prop_options_in_view` is a function of holdings, superseded and live alone" | RD3-f parenthetical | **confirmed by code reading** (`d42b2` lines 200-208) — all three are in sigma |
| RD4-e's reversed-traversal determinism digest | RD4-e | confirmed as a real internal gate (and notably stronger than D46e's, which has none) |

## 2.2 Findings

### BLOCKER F-A1 — "sigma is an ABELIAN MONOID under reception" is a construction tautology: RD3-b cannot fail once RD1-a passes

**Where.** `note-d46f-reception-dynamics.md` §4 ("**RD3 — RECEPTION IS
COMMUTATIVE ... All 7,163 co-receivable pairs commute — including the 63
with overlapping footprints: the reception state is an ABELIAN MONOID
under reception, strictly stronger than the pin's disjointness gate**");
receipt RD3-b (lines 865-881) and the `[VERDICT]` block; LOG #388
("**ALL 7,163 co-receivable pairs COMMUTE — including the 63 with
overlapping footprints: the reception state is an ABELIAN MONOID under
reception**, strictly stronger than the pin asked").

**Defect 1 — the committed state is a function of a SET.**  The
committed `View` (`v10/code/d42b2_click_refinement_exact.py`,
lines 74-96) is constructed as `View(acts, pred, idxs)`: every field
(`props`, `arbs`, `dels`, `mrgs`, `resolved`, `superseded`, `created`,
`live`, and `holdings(a)`) is built by iterating the **index set**
`self.idxs` with dict comprehensions and `|=` unions.  There is no
reception order anywhere in the layer.  "Receiving `e1` then `e2`" and
"receiving `e2` then `e1`" both denote `View(h, pred, S | {j1, j2})` —
the *same object*.  Order-independence is definitional, not
discovered.

**Defect 2 — the extracted action is a join homomorphism.**  Reading
`ACT` (lines 356-384): every branch returns `s` with a *fixed*
increment determined by `(e, a)` alone — a multiset `+1`, or set unions
`R | set(ck)`, `S | {b}`, `C | {v}`, `H | {v}`.  Nothing in the
increment reads `s`.  So `ACT(s, e, a) = s ⊔ inc(e, a)`, and any two
such operators commute for **all** records, co-receivable or not.
Referee probe P3 confirms it mechanically: `ACT(s ⊔ t, e, a) =
ACT(s, e, a) ⊔ ACT(t, e, a)` on **255,840 tests, 0 violations**.

**Defect 3 — the entailment.**  Suppose RD1-a passes.  Take a
co-receivable pair `(j1, j2)` at down-set `S`.  Then `S | {j2}` is
itself a down-set in `DS`, and `j1` is in its `ext`; so both single
steps of *either* order are enumerated instances, and faithfulness
gives `s21 = state_of(View(h, pred, S | {j1, j2}), a) = s12`.
**RD3-b's counter is therefore identically zero for every faithful
`ACT`.**  The referee verified the missing half directly: probe P2
shows the reversed composite `s21` also equals the layer's set-indexed
state on all 7,163 pairs (the receipt only gates `s12`, at RD3-a).

**Defect 4 — the pair universe is not the constraint it is billed as.**
Probe P1 applied `ACT` in both orders to **every** record pair in every
history against every enumerated pre-state — 170,820 tests, including
the 163,657 pairs that are **not** co-receivable (causally ordered, or
never simultaneously available).  Non-commuting: **0**.  So the
"co-receivable" restriction excludes nothing that would fail — but by
the same token the 7,163 figure measures the enumeration, not the
claim.  *(Attack (a) is answered in the unit's favour on the narrow
question — the pairing rule hides no failures — and against it on the
broad one: there is nothing for the pairing rule to hide.)*

**Mutation evidence.**  f1 replaces `ACT`'s delivery branch by the
identity — a demonstrably **wrong** action map.  RD1-a and RD3-a fail;
**RD3-b still reports `non-commuting = 0`.**  f3 installs the
non-abelian `created`-by-replacement variant as the delivered action:
RD3-b fires, but so do RD1-a and RD3-a.  **No mutation separates RD3-b
from RD1-a**, as the entailment predicts.

**Prescribed fix.**  Retract "the reception state is an ABELIAN MONOID
under reception, strictly stronger than the pin's disjointness gate"
from note §4, the receipt's RD3-b label and `[VERDICT]`, and LOG #388,
with a forward-correcting entry.  Replace with the two-line theorem —
*the committed layer's reception state is a function of a down-closed
index set, and the extracted action is a join with a record-determined
increment; therefore reception commutes, universally and a priori* —
and restate RD3-b honestly as a **regression test on `ACT`**, which is
what it is and what f1/f3 show it to be worth.

### BLOCKER F-A2 — RD1-b's "ZERO conflicts" is entailed by RD1-a and carries no independent information; the note and LOG lead with it

**Where.** note §4 ("**RD1 — the action map EXISTS and is a genuine
function.** Over 23,069 reception instances and 228 distinct pre-states,
the committed layer's state update is a function of (record, receiver,
pre-state): 869 repeated keys, ZERO conflicts — no hidden dependence on
history, index, poset, or unseen events"); receipt RD1-b (lines
670-680); LOG #388 ("**THE ACTION MAP EXISTS AND IS A GENUINE FUNCTION
of (record, receiver, pre-state)** — 23,069 reception instances, 228
pre-states, 869 repeated keys, ZERO conflicts").

**The defect.**  RD1-a establishes `post = ACT(pre, e, a)` on **every**
instance, with `ACT` a deterministic function of exactly those three
arguments.  A quantity equal to a function of `(pre, e, a)` on every
instance is a function of `(pre, e, a)`.  `RES['wd_bad'] == 0` is
therefore forced by `RES['faith_bad'] == 0`, and the two counters are
accumulated in the same loop (lines 562-579).

**Demonstrated (mutant f1).**  With a wrong-but-still-functional `ACT`,
RD1-a fails and **RD1-b passes at 0 conflicts** — the gate is blind to
an action map that is demonstrably not the layer's.  RD1-b's number is
a property of `ACT` being a function, not of the layer.

The RD1-b *control* is a different matter and is sound (f5 confirms the
receipt catches a control that cannot fire).  But the control convicts
the index-valued storage form; it does not make RD1-b's zero
informative.

**Prescribed fix.**  Lead with RD1-a — "an independent re-implementation
of the committed `View` semantics reproduces it exactly on 23,069
instances" is a real, checkable, valuable claim.  Demote RD1-b to a
stated corollary of RD1-a ("hence the update is a function of
(record, receiver, pre-state)") and strike "869 repeated keys, ZERO
conflicts" from the headline positions in note §4 and LOG #388.

### MAJOR F-M1 — RD1-d ("the click layer is view-transparent") is read off the `View` constructor's filter, not discovered

**Where.** note §4 ("**DELIVERED FINDING RD1-d: the click records
ko/kc/ka are the EXACT IDENTITY on reception state** — view-transparent
... **Unreachable from D44e's copy-form template**; this is what the
dynamics arm was for"); receipt RD1-d (lines 701-714, "the copy-form
template could not have said this"); LOG #388 (same, in bold).

**The defect.**  `state_of` is built entirely from `View`, and the
committed `View.__init__` reads records **only** through
`acts[i][0] == 'p' / 'r' / 'd' / 'm'`.  Referee probe P5 (a literal
scan of the constructor body):

```
View body mentions 'p' : True     View body mentions 'ko': False
View body mentions 'r' : True     View body mentions 'kc': False
View body mentions 'd' : True     View body mentions 'ka': False
View body mentions 'm' : True     View body mentions 'n' : False
```

Every record kind outside `{p, r, d, m}` is **necessarily** the identity
on sigma, because it is not in the state space at all.  The 216 + 216 +
216 + 7,734 instance census cannot fail and adds nothing to the
one-line constructor reading.  (The claim is *true*; the objection is to
its billing.)

Two knock-ons.  (a) RD4-a's declared residual "(i) click-chain reception
at |C| >= 3 is UNREACHED — the view-transparency finding RD1-d is
therefore stated at |C| = 2" presents the finding as empirical and
scope-limited when the structural reason covers all `|C|` at once.
(b) "what the dynamics arm was for" over-claims the arm's yield.

**Prescribed fix.**  Restate RD1-d as a code-reading theorem with its
one-line proof (the `View` constructor never inspects a click or noop
record), drop "unreachable from D44e's copy-form template" and "the
copy-form template could not have said this", and drop the `|C| = 2`
scope caveat as unnecessary for this particular claim.

### MAJOR F-M2 — RD2-a's INJECTIVE verdicts for `r` and `m` are pool artefacts, and the receipt probes only `d`

**Where.** note §4 ("**RD2 — injectivity, with two honest failures.**
p, r, n, m, and all three click types are injective"); receipt RD2-a
(lines 763-774); LOG #388 ("injective for p/r/n/m/ko/kc/ka").

**The defect.**  The action's holdings leg is an **idempotent set
union** for `r`, `d` and `m` alike — RD1-f says so in terms ("the SAME
map the r / d / m actions apply on their holdings leg") and RD2-c
convicts that map ("THE VERSION-RECORD ACTION IS IDEMPOTENT SET
INSERTION, hence NOT INJECTIVE").  So `r` is non-injective **as a map**
for exactly the reason `d` is.  Referee probe P4 exhibits it:

```
r record : ('r','A', {('B',v0,1), ('A',v0,0)}, {('A',v0,0)})
pre-state A holdings = { v0 }
pre-state B holdings = { v0 , ('v',v0,(0),('A'),'A') }      (distinct: True)
ACT(A, r, 'A') == ACT(B, r, 'A')  ->  True                  (collision)
```

RD2-a's zero for `r` and `m` is therefore a statement about **which
pre-states the enumeration happened to reach**, not about the action.
The receipt knows how to make that distinction — RD2-c argues
reachability explicitly for `v0` ("the genesis is held in EVERY
reachable state") and declares scope for `v.mrg` — and it built
PROBE-DD specifically to reach the `d` degeneracy.  No analogous probe
or reachability argument is offered for `r` or `m`, yet they are
reported as flat positives beside `d`'s flat negative.

**Prescribed fix.**  Either supply the reachability argument for `r`/`m`
(is a pre-state holding the to-be-created version, with `created` not
yet containing it, layer-reachable?) or restate RD2-a as
"no collision **among the enumerated fibers**" and add the map-level
statement: `r`, `d`, `m` and the version records all act by idempotent
union on holdings and are non-injective as maps.

### MAJOR F-M3 — the RD3 headline juxtaposes two different notions of "order"

**Where.** note §4 ("**RD3 — RECEPTION IS COMMUTATIVE; THE OBSTRUCTION
LIVES IN THE MENUS.** ... The order-dependence D44f found therefore does
NOT live in the state"); receipt RD3-e ("the SAME THREE RECORDS
{pA0, ('d','A','B',V0), pB1}, **two reception orders**"); LOG #388
("so D44f's order-dependence does NOT live in the state").

**The defect.**  RD3-b's "order" is *intra-history concurrency*: two
records minimal at one down-set of **one** history, with **one** poset.
RD3-e's "order" is *inter-history generation order*: `ORD1 =
[pA0, dAB0, pB1]` and `ORD2 = [pA0, pB1, dAB0]` are two **different
histories with different posets** (in ORD1 the delivery register-links
A to B so `pB1` sits above `dAB0`; in ORD2 `pA0` and `pB1` are
concurrent).  They are not two reception orders of one history and the
receipt's own explanation says so.

Consequently the "therefore" does not hold: RD3-b establishes nothing
about generation order, and RD3-e is a single hand-built two-history
example.  The conclusion "D44f's order-dependence does NOT live in the
state" is supported *only* by that one example, not by the 7,163-pair
sweep it is printed next to.

**Prescribed fix.**  Split the claim.  State RD3-b's scope as
intra-history concurrency (and see F-A1 for what it is worth there).
State RD3-e as a two-history exhibit and drop "two reception orders"
in favour of "two generated histories over the same record multiset".
Strike the "therefore".

### MAJOR F-M4 — the co-receivable universe is dominated by pairs with an identity factor, and RD3-c's control fires on the only pairs where it could

**Where.** RD3-b's detail ("pairs = 7163 (disjoint footprints 7100,
OVERLAPPING footprints 63)"); RD3-c ("fails the SAME gate on a positive
fraction of the SAME pairs ... 63 of 7163"); note §4 and LOG #388's
"all 7,163 ... including the 63 with overlapping footprints".

**Referee census of the same 7,163 pairs:**

| stratum | count |
|---|---|
| both footprints EMPTY (click/click, click/noop, noop/noop) | **970** |
| exactly one footprint empty | **3,172** |
| both records write structure, footprints disjoint | 2,958 |
| overlapping footprints | 63 — **all of them `(r, r)`** |

So **4,142 of 7,163 (58%)** of the "co-receivable pairs" contain a
record whose action is the identity; commutation there is content-free
even setting F-A1 aside.  And RD3-c's control differs from `ACT` only in
the `created` field, which two records can both write only if they
overlap — so `63 of 7163` is the **maximum** that control could ever
report, not evidence of breadth.

**Prescribed fix.**  Print the footprint stratification; restate RD3-c's
number as "63 of 63 possible".

### MAJOR F-M5 — RD3-f's gated asymmetry rests on one example, while its real justification is an ungated code reading

**Where.** RD3-f (lines 978-998); note §4 and LOG #388's "**GATED
ASYMMETRY: the PROPOSE menu is STATE-determined; the ARBITRATE/MERGE
menus are CAUSALLY determined**".

**The defect.**  The predicate compares `prop_options_in_view` on
**one** pair of views (`VW1`, `VW2`) and `arb_components_in_view` on the
same one pair.  A single instance of equality is not a determination
claim, and a single instance of inequality is not a non-determination
claim.  The parenthetical justification — "a function of holdings,
superseded and live alone — all four in sigma" — is the real argument,
and the referee **confirms it is correct** (`d42b2` lines 200-208: the
function reads `view.holdings(a)`, `view.superseded` and `view.live`
only, and RD1-a gates `live` as derived from sigma).  But that code
reading is nowhere gated, and the merge half rests on the same
one-example basis.

**Prescribed fix.**  Gate the state-determination over all 228
enumerated pre-states (compare `prop_options_in_view` across every pair
of views with equal sigma — the sweep already has the state objects),
or label the asymmetry a code-reading theorem and stop calling it
"gated".

### minor F-m1 — hard-coded instance counts

`RD1-a` requires `RES['inst'] == 23069` (line 665); `RD4-c` requires
`RES['inst'] == 23069 and RES['pairs'] == 7163` (lines 1052-1053).  In
mutant f4 (PROBE-DD removed) these fire for a reason unrelated to what
they claim to test, obscuring the one real failure (RD2-b).  Fix: derive
the counts, gate the *properties*.

### minor F-m2 — RD2-c's 72 collisions are a synthetic cross-product, not reception instances

Lines 799-810 build the version-record fibers as
`ACT_V(pre_state, v, 'A')` over **all** 228 enumerated pre-states x
**all** 23 realized version records — 5,172 fibers, most of which are
not layer-reachable receptions (and all evaluated at a fixed receiver
`'A'`).  The detail string discloses the construction; note §4 ("version
records act by idempotent set insertion, colliding on 72 v.arb fibers")
and LOG #388 do not.  Fix: carry the disclosure.

### minor F-m3 — RD3-d says "recorded, never counted as a pass" and is counted as a pass

Line 892's label reads "THE SECOND CONTROL IS SILENT, AND ITS SILENCE IS
THE STRUCTURAL FACT (**recorded, never counted as a pass**)".  It is a
`check(...)` call; it increments `PASS`; it is one of the 29.  Fix: say
"printed as a declaration and counted in the gate total", or move it out
of `check()`.

### minor F-m4 — RD4-f asserts "no vacuous gate anywhere in this receipt" against a single literal needle, next to a gate the receipt itself calls vacuous

`_pat = "check(Tr" + "ue"` — **one** needle (D46e uses four; both are
the standing CARRIED finding).  The label claims "no vacuous gate
anywhere in this receipt ... every check carries a computed predicate",
while RD3-d is declared by the receipt to be "structurally vacuous"
(note §4) three gates earlier and passes the scan.  The scanner
advertises coverage it does not enforce and contradicts its own
receipt.  Fix: as prescribed in E-M4(c) — an AST walk over `check()`
call sites — and reconcile the RD4-f label with RD3-d.

### minor F-m5 — RD4-e's digest silently excludes `sobj`

`digest(R)` drops the `'sobj'` key (line 1110).  The label claims the
digest covers "every delivered aggregate ... the full post-state fiber
map, the pre-state set".  The pre-state *keys* are covered (`states`);
the pre-state *objects* are not.  Harmless here (the objects are
determined by the keys) but undeclared.  Fix: one clause.

### nit F-n1 — "co-receivable" is never defined in the note

The universe (both records minimal at a common down-set of one history,
for one actor) is only reconstructible from the receipt's `sweep`.
Given F-A1 and F-M4 the definition is load-bearing.

### nit F-n2 — LOG #388's title "RECEPTION COMMUTES, MENUS DO NOT" survives F-A1 and F-M3 unchanged and should be re-titled in the forward-correcting entry.

## 2.3 Mutation table — D46f

| id | mutation | expected if the gates cover the claim | observed | verdict |
|---|---|---|---|---|
| **f1** | `ACT`'s delivery branch replaced by the identity (wrong, still a join) | RD1-b and/or RD3-b detect a wrong action map | RD1-a **FAIL**, RD3-a **FAIL**; **RD1-b passes (0 conflicts), RD3-b passes (0 non-commuting)** | **BLOCKER F-A1 + F-A2** |
| **f3** | the delivered action = the non-abelian `created`-by-replacement variant | RD3-b fires independently of RD1-a | RD3-b fires — **and so do RD1-a and RD3-a**; no separation exists | **F-A1** (entailment confirmed) |
| **f4** | PROBE-DD removed from the corpus | RD2-b's finding disappears | RD2-b **FAILS** (colliding d fibers = 0) — the probe really is load-bearing and declared | probe discipline **vindicated** |
| **f5** | RD1-b's control state made index-free (control cannot fire) | the receipt catches a dead control | **RD1-b CONTROL FAILS**, exit 1 | control wiring **vindicated** |
| **P1** (probe, not mutation) | apply `ACT` in both orders to **all** 170,820 record pairs, co-receivable or not | commutation is a property of the co-receivable universe | **0 non-commuting everywhere** | **F-A1** |
| **P2** | check the *reversed* composite against the layer (the receipt gates only `s12`) | — | 7,163 pairs, **0 mismatches** | **F-A1** |
| **P3** | test `ACT(s ⊔ t) == ACT(s) ⊔ ACT(t)` | — | 255,840 tests, **0 violations** — `ACT` is a join homomorphism | **F-A1** |
| **P4** | two abstract pre-states differing only by the version an `r` inserts | `r` is injective | **collision** — `r` is non-injective as a map | **MAJOR F-M2** |
| **P5** | scan the committed `View` constructor for click/noop kinds | RD1-d is empirical | `View` never mentions `ko`/`kc`/`ka`/`n` | **MAJOR F-M1** |
| **P6** | `admissible()` on a genuine re-delivery | RD2-b may be a probe artefact | `(True, 1/16)`, and B already holds `v1` | RD2-b **acquitted** |

## 2.4 Independent-recomputation inventory — D46f

- receipt rerun: byte-identical, 29/29, 9.5 s.
- committed `View` constructor read line by line (`d42b2` 74-111) —
  establishes the set-indexed state (F-A1) and the click/noop filter
  (F-M1).
- `prop_options_in_view` and `deliver_options_in_view` read line by
  line (`d42b2` 200-220) — confirms RD3-f's parenthetical and RD2-b's
  mechanism.
- `ACT` join-homomorphism probe: 255,840 tests, 0 violations.
- all-pairs commutation probe: 170,820 tests, 0 non-commuting
  (163,657 of them outside the receipt's universe).
- reversed-composite-vs-layer probe: 7,163 pairs, 0 mismatches.
- `r`-injectivity counterexample constructed and exhibited.
- footprint stratification of the 7,163 pairs (970 / 3,172 / 2,958 /
  63, the last exclusively `(r, r)`).
- `admissible()` re-delivery check re-executed independently.
- five receipt mutations (f1, f3, f4, f5 plus the RD1-b control
  variant) run to completion against the committed layers.

---

# REPRODUCTION APPENDIX

All referee artefacts live in the session scratchpad
`/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad`
and nothing under `v10/` other than this file was written.

**D46e.**

```
python3 v10/code/d46e_smeared_interacting_exact.py   # 19/19, byte-identical, 24.8 s
python3 scratchpad/ref_d46e.py all                   # exact-Fraction rebuild (1.8 s)
python3 scratchpad/scan_d46e.py                      # 18-reading coarsening scan
python3 scratchpad/m_e1.py ... m_e8.py               # the eight mutants
```

`ref_d46e.py` implements, in `fractions.Fraction`-valued complex
arithmetic with no threshold anywhere: `build_H(site_w, bond_w, g)`;
`exp_series` (`U_k = (-i)^k H^k / k!`); `gamma_series`
(`|U|^2` entrywise); `neumann_inv`; the region collar
(`site_w[n0] = 0`, `bond_w = 0` on bonds incident to `n0`);
`A(n0, EXC) = [J]_{Delta^2}`, `A(n0, LT) = [J]_{Delta^4}`;
`D(ch) = sum_delta delta * sum_r r * [A(b), A(b+r)]`; and an exact
proportionality test.  `scan_d46e.py` sweeps eighteen channel maps.

The reversal (E-A1) is reproduced by either path: the exact rebuild
(`COLLAPSE` with residual identically zero at g = 0), or the receipt's
own code with one line changed (`m_e1.py`, `READINGS` extended by
`'NPR'`).

**D46f.**

```
python3 v10/code/d46f_reception_dynamics_exact.py    # 29/29, byte-identical, 9.5 s
python3 scratchpad/probe_d46f.py                     # P1-P6
python3 scratchpad/probe2_d46f.py                    # footprint census
python3 scratchpad/m_f1.py m_f3.py m_f4.py m_f5.py   # the four mutants
```

The mutants are `__file__`-anchored like the original; run them from a
directory containing `d42b3_placement_exact.py` and
`d42b2_click_refinement_exact.py` (symlinks suffice).  `probe_d46f.py`
execs the receipt's head up to `RES = sweep()` with stdout suppressed
and then works directly with `ACT`, `state_of`, `View` and
`downsets`.

---

# WHAT THE ROUND ASKS FOR

**D46e — three retractions and one re-run.**

1. Retract "THE FAILURE IS GRAIN, NOT INTERACTION" (note §4, `sg3_verdict`,
   the `[VERDICT]` block, LOG #389 title and body) and re-run the sweep
   with the channel family closed under products of its own labels.
   Deliver the reading-relative statement.
2. Make `sg3_verdict` computed, the way `sg2_verdict` already is, and
   strike "computed not narrated" until it is true.
3. Add a gate tying `D_identified` to `tau_D_pairs` on common input, so
   that the interacting numbers are anchored to the corpus first moment.

**D46f — two retractions, no re-run needed.**

1. Retract "ABELIAN MONOID ... strictly stronger than the pin's
   disjointness gate" and replace it with the two-line theorem; restate
   RD3-b as a regression test on `ACT`.
2. Move RD1-a to the headline and demote RD1-b to its corollary;
   restate RD1-d as a code-reading theorem.

**Both.**  The scanner-coverage finding is now three rounds old and
recurs in both receipts (four literal needles in D46e, one in D46f,
neither able to see a vacuous gate written in any other form, and D46f's
scan contradicting a gate its own note calls vacuous).  It should be
promoted from a per-round minor to a corpus-level obligation.
