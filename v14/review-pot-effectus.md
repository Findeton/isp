# K2 EFFECTUS-LENS — hostile review of POT (paper-36)

**Seat:** K2, verdicts / licensure / meaning. **Posture:** hostile.
**Status of this document:** CANDIDATE until adjudication.

**Object verified at open AND at close, by me, at the paths the pin names:**

| object | pinned sha256-12 | measured at open | measured at close |
|---|---|---|---|
| `v14/paper-36-pot.md` | `173a88d8755f` | `173a88d8755f` | `173a88d8755f` |
| `v14/code/pot_exact.py` | `8c11f16002d1` | `8c11f16002d1` | `8c11f16002d1` |
| `v14/code/pot_output.txt` | `50f295f31b67` | `50f295f31b67` | `50f295f31b67` |
| `v14/code/pot_receipt.json` | `5b5f731fb615` | `5b5f731fb615` | `5b5f731fb615` |
| `v14/note-pot-pin.md` | `df2f15efa7b0` | `df2f15efa7b0` | `df2f15efa7b0` |

(The brief located the three code artifacts at `v14/`; they live at `v14/code/`.
Digests are identical, so this is a path note and not a discrepancy.)

---

## GRADE

**ACCEPT-WITH-FIXES.**

No headline reverses. The head word `POT-SPLIT-BY-WEIGHT` is genuinely
multi-way and correctly emitted; the area-blindness universal — this unit's
biggest sentence — is **licensed**, and licensed on a ground stronger than the
one the brief supposed; the orientation row, the stamps, the gap's scoping and
the vocabulary of the delivered text are all clean under adversarial sweep.

Three majors stand. One is a **false claim, stated twice, one of them in the
Decided list** (M1). One is a **licence wall that fails 8 of 10 plants**,
including two that read as naked physical confinement claims (M2). One is a
**counting-basis mismatch on the unit's headline evidence number** (M3). All
three are repairable by sentence surgery plus one gate strengthening; none
touches a computed number in the receipt, and I found **no false number
anywhere in the receipt or the verdict string.**

**Recomputations: 10,151.** Breakdown at the end.

---

## MAJORS

### M1 — §7 and §14 assert a FALSE identification, and the true one is never stated

**The sentences.** §7: "there are 24 of the 136 extreme points where the ratio
is one, and they are **exactly the points at which a single mode is active**,
while the rest carry two modes or three." §14, in the Decided list: "the Creutz
leg at one **precisely on the single-mode corners**."

**The establishing measurement.** I cross-tabulated `active_modes` against
`creutz_is_unit` over all 136 sweep rows in the receipt, then recomputed χ
independently from the published mode coefficients (136 points × 4 rungs = 544
χ values in exact Q(√2), 0 mismatches against the receipt):

| active modes | χ = 1 | χ ≠ 1 |
|---|---|---|
| 1 | 24 | **8** |
| 2 | 0 | 64 |
| 3 | 0 | 40 |

`creutz_is_unit` is True at **24**. A single mode is active at **32**. The sets
are not equal; the paper's own §8 table publishes the 32 in the ACTIVE-MODES
row ("1 32, 2 64, 3 40"), so the paper contains both numbers and asserts they
are the same set. The 8 exceptions are the points with (A, B, C) = (0, 2, 0) —
the perimeter-proportional mode alone, where W(P) = 2P and
χ(P) = P(P−2)/(P−1)² ≠ 1 at every rung.

**The true characterization, which the paper never states.** I recomputed the
ladder W(P) = A + B·P + C·2⁻ᴾ at P = 2…6 for all 136 points (680 evaluations).
The χ = 1 set is **exactly** the set on which the ladder is **constant in the
perimeter** — set equality, 24 = 24, verified elementwise. All 24 are
constant-only (A ≠ 0, B = C = 0): 16 at A = 2, 8 at A = 1. Not one of them is a
halving-only point; there are none.

**Why this is a major and not a wording slip.** This is the seat's item 3. The
classifier's DECONFINES branch fires on `(not area_seen) and unit`, and a
constant ladder is the degenerate r = 1 member of the perimeter-geometric
family. So the 24 DECONFINES points are, without exception, points where **the
loop observable does not move with the perimeter at all**. The statement that
defuses any physical reading of the tally is precisely the statement the paper
omits — and in its place stands a false one that makes the 24 sound like a
structural corner of the coupling space rather than a flat ladder. The paper's
only two mechanism sentences for the 24 are both wrong, and both wrong in the
direction that flatters the word.

**Licensed replacement, §7:**

> The Creutz leg does not: there are 24 of the 136 extreme points where the
> ratio is one, and they are exactly the points at which the constant mode
> alone is active — the ladder is flat there, so the ratio is one because the
> observable does not move with the perimeter at all. A single mode is active
> at 32 extreme points and not at 24: at the remaining 8 the active mode is the
> perimeter-proportional one, and there the ratio is not one.

**Licensed replacement, §14 bullet:**

> and the Creutz leg at one precisely on the 24 flat corners, where the
> constant mode alone is active

**Licensed addition, §8, to sit with the price table (this discharges item 3):**

> DECONFINES is the classifier's word for a ladder whose Creutz ratio is one at
> every rung, and at this arena all 24 such points are points where the loop
> observable is constant in the perimeter: the word records a flat ladder, the
> degenerate member of the perimeter-geometric family, and it is not a finding
> that anything deconfines.

**Item 3 ruled.** Without that addition, no sentence in the paper states what
the 24 are, the word DECONFINES appears only inside two table cells (§8 price
table, §12 control-arm table), and the nearest prose is M1's false sentence.
With it, the tally is machine-only and cannot be read physically. The word
itself never appears in POT's prose outside tables — that part is clean.

---

### M2 — the licence wall does not have the teeth the pin ordered: 8 of 10 plants survive

**What the pin ordered.** "every confinement word in prose must sit in a
sentence carrying **its measured discriminator value**; unmeasured confinement
talk dies at a wall gate."

**What is implemented** (`pot_exact.py` §18, `G-THE-CONFINEMENT-LICENCE-WALL`):
a sentence containing one of 11 `CONFINEMENT_WORDS` passes if **any** token of
a `licence` set occurs in it **as a lowercased substring**. The licence set is
the receipt's whole numeral registry (every token of length ≥ 2) plus the head
word plus eight fixed strings — among them `"CONFINES"` and `"DECONFINES"`.

**The establishing measurement.** I mirrored the repo subset to a scratch tree,
confirmed the mirror reproduces the delivery run byte-for-byte in its verdict
and all 49 gates, then planted one sentence each immediately before §14 and ran
the full delivery gate:

| plant | sentence | result |
|---|---|---|
| P1 | "This arena is confining." | **DIED** at the wall |
| P2 | "This arena confines." | **PASSED** |
| P3 | "The area law is present at 136 of the extreme points." | **PASSED** |
| P4 | "The string tension of this arena is positive." | **DIED** at the wall |
| P5 | "The arena deconfines at 24 of the extreme points." | **PASSED** |
| P6 | "A quark and an antiquark on this lattice are never separated." | **PASSED**, undetected |
| P7 | "The Wilson loop falls off with the enclosed area on this arena." | **PASSED**, undetected |
| P8 | "A flux tube forms between the sources and does not break." | **PASSED**, undetected |
| P9 | "The potential grows linearly with the separation here." | **PASSED**, undetected |
| P10 | "The observable exhibits a non-zero tension per unit area." | **PASSED**, undetected |

Three distinct failure modes, all measured:

1. **Self-licensing.** `CONFINES` and `DECONFINES` are simultaneously in the
   policed list and in the licence set, so any sentence using either word
   licenses itself. P2 — a bare, false, unmeasured confinement claim — passes
   for this reason alone.
2. **Any numeral will do.** The test is presence of *a* measured token, not of
   *the sentence's own* discriminator value, and matching is by substring over
   a large numeral registry. P3 and P5 are false claims that pass because they
   carry a number the run happened to measure. P5 is the exact sentence item 3
   exists to prevent, and the wall admits it.
3. **Synonyms are outside the list entirely.** P6–P10 were never even counted
   as confinement sentences (the gate reported 10 carrying a licensed word, the
   unplanted baseline figure). The 11-word list catches "area law" and "string
   tension" but not "enclosed area", "flux tube", "grows linearly with the
   separation", "tension per unit area", or "quark".

**What this does NOT impeach.** I swept the delivered paper myself and
reproduced the gate's count exactly — 10 sentences carry a listed word, and I
read all 10. **None of them exploits any of the three holes**, and none claims
the arena confines. The strongest is §14's negative "this arena cannot exhibit
an area law", which is the safe direction. A wider synonym sweep of the
delivered text (34 patterns) is clean: all 11 occurrences of "tension" are
inside the word "extension", the single "qcd" is `NOT-QCD` in the verdict, and
no quark, flux tube, linear potential or screening language occurs. **The paper
is clean; the wall is weak.** Those are separate findings and I record them
separately.

**The claim that must be repaired** is §1's framing "the licence has teeth."
§1's operative clause — "required … to carry a value this run measured" — is an
accurate description of the implementation and is not a false statement. But
"teeth" asserted beside a wall that passes 8 of 10 plants is an over-sell of
the unit's own instrument, and the pin's wall is strictly stronger than what
was built.

**Licensed replacement, §1:**

> **The vocabulary wall, and how it is enforced.** The confinement vocabulary is
> licensed for this unit only, and the licence is enforced by a gate on the
> delivered text: every sentence of this paper that uses one of 11 declared
> words must also carry a token this run measured, and an unmeasured sentence
> stops the delivery run. The wall's reach is a floor and is published as one:
> it kills a bare unmeasured claim, and it does not reach a sentence that
> carries a measured numeral for an unrelated reason, a sentence built from the
> classifier's own words, or a synonym outside the declared 11 — so this
> paper's vocabulary is clean by reading and not only by gate.

If the adjudicator prefers the gate strengthened rather than the claim scoped,
the two minimal repairs are: drop `CONFINES`/`DECONFINES` from the licence set,
and require the sentence to carry a token from the leg it names rather than any
registry token. I make no ruling on which route; either discharges M2.

---

### M3 — the headline evidence number 5760 is counted on a different basis from the 44800 it is read against

**The sentences.** §5: "5760 shape-by-coin comparisons at equal perimeter and 0
disagreements". §14, Decided list: "measured at 5760 comparisons". §11:
"44800 comparison-by-coin checks at L = 8 with 0 disagreements, over a set of
comparisons that is far richer there than here."

**The establishing measurement.** `measure_the_closed_form` compares every
shape against the *representative* of its perimeter class, so
`equal_perimeter_comparisons` = 9 shapes × 640 coins = 5760, of which the 5
representatives contribute 5 × 640 = **3200 self-comparisons** — a shape
compared with itself. `measure_the_boundary_lattice` instead counts
area-discriminating comparisons × coins: 44800 / 640 = **70**, matching its own
`area_discriminating_comparisons` field.

I rebuilt the ladder from R5's primitives through the instrument's own
`holonomy_trace` / `sym_qs` and recounted on the honest unordered-pair basis:

| basis | at L = 4 | at L = 8 |
|---|---|---|
| shape × coin (what §5/§14 report) | 5760 (3200 of them self-comparisons) | not reported |
| unordered equal-perimeter pair × coin | 3200, 0 disagreements | not reported |
| **area-discriminating comparison × coin** (what §11 reports) | **1280**, 0 disagreements | **44800**, 0 disagreements |

So the reader who sets §14's 5760 beside §11's 44800 reads a 7.8× enrichment;
on a common basis it is 1280 → 44800, a 35× enrichment, and the L = 4 leg is
4.5× thinner than its headline number suggests.

**This is also the item-9 finding.** §4 discloses the thinness honestly and
well — "the ladder carries 2 area-discriminating comparisons and 4 Creutz
rungs. That is thin, and it is published as thin." But §14, **where the finding
is claimed**, carries neither the 2 nor L = 8's 70; it carries only the inflated
5760. The duty is to disclose the thinness where the finding is claimed, and
§14 does not.

**Licensed replacement, §14 bullet 3:**

> **The area leg of the discriminator is therefore family-invariant**, and the
> partition it induces on the inventory of 135 couplings is trivial. This is the
> finite, exact sense in which this arena cannot exhibit an area law: not that
> the effect is small, but that the observable cannot see the area at all. At
> this lattice the ladder carries 2 area-discriminating comparisons, which is
> 1280 comparison-by-coin checks with 0 disagreements, and that leg is thin
> here; the boundary lattice carries 70 of them, which is the 44800 checks of
> section 11.

I do not ask for §5's 5760 to move — it is the correct count of what that gate
checks, and the gate checks a *stronger* property than area-blindness. I ask
that the number not be carried into §14 as the measure of the area finding.

---

## MINORS

**m1 — `DISCRIMINATOR-DEGENERATE` is one token for two predicates, and the
re-scope is not disclosed.** Ruling, exactly as asked: **it is a re-scope
needing disclosure, not the registered word.** The pin registered it for a
failure of the discriminator's own well-definedness ("too few rungs, zero
denominators"). `classify()` emits it from two disjoint branches: `not defined`
(the registered predicate — missing shapes, zero denominators, no rungs, no
comparisons) and a terminal `else` (well defined, but matching neither law
shape). Every delivered row takes the second branch: `creutz_defined` is True at
136 of 136 and at all 4 declared rows, with `creutz_zero_denominators` = 0.

Severity is MINOR, not MAJOR, for four measured reasons: the head law never
spends the word (`POT-SPLIT-BY-WEIGHT` is emitted); §6 states the second
predicate's mechanism at first use ("the area is not seen and the Creutz ratio
is not one, so neither shape of law is present"); the verdict string carries
`DISCRIMINATOR=WELL-DEFINED-AT-L-4` and `LEG-CREUTZ=DEFINED-AT-136-OF-136`
explicitly; and §8 states "it is undefined at 0 of them" immediately below the
table. But disclosure is still owed, because §8's table places
"DISCRIMINATOR-DEGENERATE 112" two rows above "LEG-CREUTZ-DEFINED … True 136",
and a reader of that table alone reads a contradiction.

**Licensed addition, §4 or §8:**

> `DISCRIMINATOR-DEGENERATE` names two different measurements in this paper and
> both are reported. The pin registered it for a failure of the discriminator's
> own well-definedness — too few rungs, or a vanishing denominator — which is
> the condition the SYN-ZERO-DENOMINATOR control arm exhibits and which this
> arena does not meet, the ratio being defined at 136 of 136 extreme points and
> at every declared row. The row-level tallies use the same word in its second
> and wider sense: a ladder that is well defined and matches neither shape of
> law, which is the condition at 112 of the 136.

**m2 — the universal's operative restriction is the carrier, and the sentence
says "arena".** §8: "No coupling this arena admits can make the loop observable
see the area, because the blindness is a property of the carrier and not of the
measure." The "because" clause names the carrier correctly, so the sentence
supplies its own scope and I do not rule it unlicensed; but at the unit's most
quotable sentence the subject should carry the premise. **Licensed form:**

> No coupling this arena admits can make the loop observable see the area at any
> configuration of this carrier, because the blindness is a property of the
> carrier — one coin on every link — and not of the measure.

**m3 — the receipt's `spectral_door.SPC_inherits` is stronger than the paper.**
The field reads
`THE-GAP-1/2-IS-THE-MASS-GAP-QUESTIONS-FINITE-FORM-AT-THIS-ARENA-AND-IT-IS-FAMILY-INVARIANT`.
The framing is the pin's own, so it is licensed; but it is the field SPC will
read, and it never meets the fact — published elsewhere in the same receipt and
in the verdict — that the halving mode is **absent at 72 of the 136 extreme
points**. The gap 1/2 is a property of the fitting basis {1, P, 2⁻ᴾ}; at those
72 points the 1/2 eigenvalue has zero amplitude and the realized ladder is
A + B·P. §9's "The gap is family-invariant; what a coupling moves is which modes
are switched on and how strongly" is honest and joins the two facts; the receipt
field does not. Recommend the successor's pin bind the two together so SPC
cannot inherit "mass gap" from a three-term ansatz.

**m4 — §14's odd-part sentence is garbled**: "non-zero at 3760 of 11520
shape-by-coin traces carry a non-zero odd part at 9 of the 18 shapes" — the
verb doubles. Numbers are correct (11520 − 7760 = 3760, cross-checked against
`loop_observable.shape_by_coin_traces_already_real`).

**m5 — a brief-level note, not a paper defect.** The brief cites 252 sentences;
the receipt's `paper_binding.sentences` measures **258**, with 10 carrying a
licensed word and 1 declaring the wall. My independent sweep reproduces the 10
exactly.

---

## WHAT I CLEAR, WITH THE MEASUREMENT THAT CLEARS IT

**Item 1 — the head is genuinely multi-way. CLEARED.** All five pre-registered
words are emitted through the **real** `classify()` and the **real**
`head_law()`, with no delivered field overwritten: a table geometric in the area
→ `CONFINES` → `POT-CONFINES-AT`; geometric in the perimeter → `DECONFINES` →
`POT-DECONFINES-AT`; a vanishing rung → `DISCRIMINATOR-DEGENERATE` →
`POT-DISCRIMINATOR-DEGENERATE-AT` (and note this arm exercises the *registered*
predicate, which is what makes m1 a disclosure rather than a substitution); a
shape the family does not cover → `BLOCKED-AT-THE-LADDER` → `POT-BLOCKED-AT`;
two rows that disagree → `POT-SPLIT-BY-WEIGHT`. The gate additionally requires
5 distinct head words against 5 pre-registered. This is the ACT Z1 pattern
correctly executed. A second head law over the receipt's *tallies* rather than
its rows agrees on the delivered string (3063 characters).

**Item 6 — the area-blindness universal. LICENSED, and on a stronger ground
than the brief supposed. This is the ruling the brief called the unit's biggest
sentence.**

The brief asks whether 136 extreme points + 9 slices license a universal over a
135-parameter polytope, and whether "area seen" is linear. Ruling in three
parts:

1. **"Area seen" is not linear** — it is a boolean predicate on an expectation,
   and the expectation itself is a *ratio* of linear functionals, hence affine-
   projective and not linear. So the naive "linear functional on a polytope"
   licence does not apply to it as written.
2. **A repaired polytope argument would nevertheless work**, and I record it:
   E_μ[W_x] − E_μ[W_y] = Σ_c μ(c)(W_x(c) − W_y(c)) / Σ_c μ(c). The **numerator
   is linear in μ**; vanishing at every vertex of the reachable set forces it to
   vanish on the hull. So even the weak route closes.
3. **But the paper does not rest on either route, and says so.** §5 establishes
   the identity **per configuration**: at every coin and every equal-perimeter
   shape pair the observable takes the same value. From that, equality of
   expectations follows for **every** measure on the carrier — not merely every
   allowed weight system — with no polytope argument and no census. §5 states
   exactly this: "Because the statement is per-configuration, it holds under
   every measure on this carrier without a second census." The 136 + 9 are
   confirmations, not the ground, and §8's "because" clause names the right
   ground.

**My independent witness.** I rebuilt the ladder traces from R5's primitives and
tested the universal at measures the sweep never visits: **1500 random
full-support positive-rational measures over the 640 coins** (3000
area-discriminating expectation comparisons) and **all 640 Dirac measures**
(1280 comparisons) — **0 mismatches**, plus 3200 per-configuration pair × coin
checks with 0 disagreements. The universal stands. Its scope is measures on
**this carrier**; see m2 for the wording.

**Item 5 — the perimeter-only claim's scope. CLEARED.** The uniform-carrier
premise is disclosed at the headline, not only in §13: the §1 title reads "The
Loop Observable **on This Carrier** Is a Function of the Perimeter Alone at
Every Configuration"; §2 defines it ("the 640 uniform configurations, one coin
repeated on every link"); the verdict's SCOPE segment carries
`CARRIER=THE-640-UNIFORM-CONFIGURATIONS;FULL-CONFIGURATION-SPACE=640^32-NOT-A-CARRIER-HERE`;
§5 states the mechanism's dependence on it explicitly. The first successor is
registered in §14 with the premise named as exactly what a non-uniform carrier
removes. I found **no sentence generalizing beyond the uniform carrier.**

**Item 7 — the gap. CLEARED, no upgrade found.** "Spectrum {1,1,1/2}, gap 1/2"
is attached throughout to the *ladder's closed form* read as a transfer object,
never to the true transfer matrix. §9 names the door at 167772160000 states per
slice and does not run it; §14's Not-decided list says "no statement about its
spectrum is made here." No mass-gap vocabulary appears in the paper; the verdict
says only `SPC-INHERITS-THE-GAP`, and the pin licensed that handoff. The one
place a stronger reading could enter is the receipt field, recorded at m3.

**Item 8 — the orientation row. CLEARED, in full.**
`DECLARATION-RELATIVE-AT-THE-ORIENTATION-READING` stamps **all 4** reading rows,
each also carrying `DECLARED-NEVER-DERIVED`;
`status = DECLARED-NEVER-DERIVED-NEITHER-STANDARD-IS-CLAIMED-TRUE`. The price is
measured, not argued: index of the oriented subgroup 2 at both readings; coupling
counts 135 / 135 / 79 / 79 across ANCHORED / ANCHORED-ORIENTED / EXTENSION /
EXTENSION-ORIENTED, i.e. the declaration costs no coupling. The odd-part
invisibility sentence carries **both universes** as required — "0 non-zero odd
observables at every declared row" *and* "96 of the 136 extreme points carry at
least one" — in adjacent clauses of the same paragraph.

**Item 9 — the L-scope duty. CLEARED except at §14 (see M3).** The merging law
8/gcd(L,8) is stated, tabulated at L ∈ {2,4,8,16}, and **run** at L = 8 rather
than projected; §11 reports both halves honestly, including the one finding that
dies (class merging: 72 here, 0 at L = 8) and the three that survive. L = 8's 70
area-discriminating comparisons are cited as the strength in §11. The failure is
only that §14 does not carry the L = 4 thinness or the L = 8 count where the
finding is claimed.

**Item 10 — stamps. CLEARED.** `CONDITIONAL-ON-THE-DECLARED-WEIGHTS` is present
on **all 4** declared rows individually and at the section level. The law-native
control's stamp `LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION`
is **verbatim** — I located it in both parents' bytes (`paper-34-act.md` lines
442/446, `paper-27-smu.md` lines 302/740) — and
`the_control_is_never_spent_as_derived` is True, with ACT's own prohibition
quoted from its pinned bytes at line 451. E-24 counting-only stamps are carried
on `family_sweep` ("COUNTING-ONLY-E-24-NO-MEASURE-OVER-THE-FAMILY-IS-DECLARED"),
`price_binding` and `loop_family`. Window honesty holds: the declared family is
named as a window in the verdict string, the extension reading's 16 escapes are
published rather than absorbed, and §13 registers all three scope points. Every
fraction I checked is referent-bound to a named row.

**Provenance of the licence itself.** Both parents' verdicts end
`NO-CONFINEMENT-CLAIM` and carry
`NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-0-LOOP-FAMILIES-GROWN`.
POT's verdict drops `NO-CONFINEMENT-CLAIM` — correctly, the gate being open for
this unit — while adding
`CONFINEMENT-VOCABULARY-IS-LICENSED-FOR-THIS-UNIT-ONLY-AND-ONLY-IN-MEASURED-SENTENCES`
and retaining `NO-CONTINUUM-CLAIM;NO-SI-NUMBERS;NOT-QCD`. The inversion of
paper-23's withholding machinery is correctly executed at the verdict level.

---

## RECOMPUTATION COUNT — 10,151

| what | count |
|---|---|
| object digests (5 at open, 5 at close) | 10 |
| full delivery runs, repo + scratch mirror, 49 gates each | 98 |
| plant runs through the complete delivery gate | 10 |
| receipt sweep rows cross-tabulated (active modes × χ) | 136 |
| χ recomputed independently in exact Q(√2) from mode coefficients | 544 |
| ladder values W(P) recomputed, P = 2…6, all sweep points | 680 |
| arena rebuilt from R5 primitives (alphabet 25, coins 640, loops 192, circuit rows 16) | 873 |
| equal-perimeter pair × coin checks, unordered basis (1280 area-discriminating) | 3200 |
| expectation comparisons at 1500 random interior measures | 3000 |
| expectation comparisons at all 640 Dirac measures | 1280 |
| paper sentences swept for the 11 licensed words | 216 |
| synonym patterns swept over the delivered text | 34 |
| receipt field cross-checks against paper and parents | 70 |

Zero false numbers found in the receipt, the verdict string, or any table. The
three majors are a false *identification* (M1), an instrument weaker than its
pin (M2), and a counting *basis* mismatch (M3) — no computed quantity moves.

---

## CLOSE

Five pinned digests re-verified at close, all unchanged (table at head).
This document is my sole repo write.

**Candidate until adjudication.**
