# EPR (paper-38) — K2 EFFECTUS review

*Three-seat hostile panel, K2 seat: licensure and meaning. Repo
`/Users/felixrobles/workspace/isp`, python3.13, scratch off-tree. Authority: the pin
(`v14/note-epr-pin.md`, b1e4cf9a8b9f), the 1935 original
(`v14/sources/epr-1935-physrev-47-777.pdf`, 66b5deb150c4, read in the original by this
seat), `HANDOFF-PROMPT.md` §4/§9 with the RUNBOOK engravings E-22/E-23/E-24 and the
#267/#295 checklists, and v5 paper-14 as the Bell wall's ground. Single repo write:
this file. Git read-only.*

**Object verified at open and at close — all five, unchanged:**

| file | sha256-12 | lines |
|---|---|---|
| `v14/paper-38-epr.md` | 550e3c8fff93 | 487 |
| `v14/code/epr_exact.py` | 9ed817d9649d | 3511 |
| `v14/code/epr_output.txt` | 1b30c6761281 | 188 |
| `v14/code/epr_receipt.json` | a51326de11a8 | 2789 |
| `v14/note-epr-pin.md` | b1e4cf9a8b9f | 137 |

---

## GRADE: ACCEPT-WITH-FIXES

**Zero false numbers.** 84 independent recomputations; one disagreement, resolved to the
object the paper itself names; no delivered number moves anywhere in this review. The
instrument reproduces **byte-identical** off-tree with no version control present
(mirror at `.../scratchpad/epr_k2/tree`; rerun output 1b30c6761281, receipt a51326de11a8
— both equal to the delivered digests). All 30 declared falsifiers die at their declared
gates, 0 off target, including the Bell plant on the paper leg.

**Not ACCEPT.** Eight majors. Two of them are sentences that are false or unlicensed as
written and must be re-ruled before adjudication (M3 the E6 upgrade, M4 a false
self-certification). Two are pin ownership under #299/#319 (M1, M2) — the ACT/FAC
disposition applies: *the delivered words stand because they are true; what is owned is
the architecture that made them the only utterable words.* Two are instrument assurance
weaker than the sentence it supports (M5 the wall, M6 the E5 zero). One is an unmeasured
modal-causal sentence (M7). One is a 1935 fidelity failure (M8).

**Not REJECT.** No false theorem. The head words are true at the objects they name. The
Bell wall holds on the merits: I swept the paper myself for local-realism and
Bell-evasion content and it is **clean** — no claim of restored locality, evaded Bell,
vindicated hidden variables, or refuted spooky action appears anywhere in the paper's own
voice, and the v5 paper-14 rendering is byte-exact.

**Every headline in this review is a candidate reading until adjudication.**

---

## Recomputation ledger

| leg | count | result |
|---|---|---|
| independent rebuild of arena, corpus, blocks, predicates, census, E4, readings, controls | 45 | 45/45 agree at the named objects (1 resolved, below) |
| off-tree byte reproduction (output, receipt) | 2 | both byte-identical |
| falsifier sweep, death-site verified | 30 | 30/30 on target |
| adversarial wall plants written by this seat | 7 | 1 caught, 6 passed (M5) |
| **total** | **84** | **zero false numbers** |

Rebuilt independently and confirmed: 27 cells in bijection with 27 co-division pairs, six
cells per actor; 72 of 72 ordered site pairs unlinked exactly on the undeclared class,
every degree 6; 490 / 19 / 0 on the 512-subset lattice; 72 I7-STRICT triples, 5,184
concatenations, 600 schedules, 5,856 histories; site-constant at 5,856 of 5,856; 36
distinct records; 6 LEG-1 survivors and 4 non-unique histories; all four census arms
(0/0/0, 18/54/54, 105,408/316,224/316,224, 421,656/1,265,112/1,265,112) with the shadow's
self-certified count 0 at every arm; 9 residue classes, 64-state sweep, best 4, primary 4,
0 separations; the five readings' cells 36/4/1/23/3 with largest fibres 1/12/36/4/13; 3
non-jointly-declarable pairs; the full E4 distribution {3:594, 4:8,514, 5:96,300} and
{3:2,382, 4:34,062, 5:385,212} and {4:18}; the control arena's 35,136 / 351,360 / 105,408
/ 105,408.

**The one disagreement, resolved.** C14, "the two declared coin orders differ at 30 of the
36 committed records": comparing the two orders' *Born menus* I get **24**, not 30.
Comparing the two orders' *matrices* `G·D(x)` against `D(x)·G` entrywise in Z[w] — which
is the object the paper's own em-dash gloss names, and which `commutator_census`
(`epr_exact.py:1940-1951`) computes — I get **30**, and the six that commute are exactly
the six records whose three residues are equal. The delivered number is correct at the
object named. See minor m2 for the residual precision cost.

---

## MAJORS

### M1 — The selector is two-way at the committed corpus; two of the five pre-registered words were unreachable before the run, and the pin's feasibility lines argue abstract conditions rather than the corpus (#299/#319)

**Establishing measurements.**

*EPR-RECORD-ALSO-INCOMPLETE is unreachable analytically, not merely at this corpus.* At
`epr_exact.py:1733-1735` the spec builder sets

    (tuple(sorted({k % 3 for k in locf(A)})),      # da
     tuple(sorted({k % 3 for k in locf(B)})),      # db
     tuple(sorted(k % 3 for k in qs)))             # qs,  qs = locf(B)

so `set(qs) == set(db)` by construction. `ownr = FR[(db, r)]` (`:1759`) is the fibre of
records agreeing with `r` on every direction in `db`; therefore
`epr_counterpart_at(d, ownr)` (`:1254-1259`) returns True for every censused `d`. I
enumerated every spec of every localization × separation: **`set(qs) ⊆ set(db)` at 132 of
132 specs**. `without_counterpart_in_D_RECORD` is identically zero — measured 0 on all
four arms and on every control arm that does not mutate the description itself. The head
law's branch at `:1714` can never fire on unmutated data.

*EPR-BOTH-COMPLETE is unreachable at the committed corpus by a pigeonhole computable at
pin time.* The coin consumes `w^{n mod 3}` (`shadow_menu`, `:1194-1208`); the corpus
carries **36 distinct records over 9 residue classes**. I swept the entire declared
64-state family and computed, for each state, the number of certified record-directions
the shadow's own fibre fails to fix: **the minimum over all 64 states is greater than
zero**. No declared state can return BOTH-COMPLETE here.

*EPR-BLOCKED-AT-\<object\>* is stamped instrument-fault-only in the pin (`:113`) and does
not count as an arm.

So the live selector is exactly **two-way**, and its two-wayness is entirely the
premise-existence question — the localization axis, which is M2.

The pin's lines are the #319 failure mode verbatim. `note-epr-pin.md:100-101` reads
"EPR-BOTH-COMPLETE — reachable if the shadow map is injective on the certainty-elements
(decidable)" and `:102-104` "EPR-RECORD-ALSO-INCOMPLETE — reachable if a certainty-element
exists with no record counterpart (decidable ...)". Both argue an abstract condition. The
#319 clause requires the feasibility line to be argued **against the committed corpus**;
against this corpus the first is refuted by a residue-class pigeonhole and the second by
the predicate's own domain. The pin itself already knew the second — `:97-98` says
"D-RECORD **trivially** contains every record-defined value" — and that word never
reaches the paper.

**Disposition.** Per ACT #299 / FAC #319: the delivered words stand; the pin is owned by
the adjudicator; repair, not reversal. **No number moves.**

**Repair.** Add to §5, immediately after the sentence at paper line 234-235:

> Two of the three branches the head law can take are closed at this corpus before any
> measurement. `set(qs) ⊆ set(db)` at 132 of 132 declared specs, so a censused quantity is
> always one D-RECORD's own content at the block already fixes: the record-incomplete
> branch cannot fire on unmutated data, and the record's zero is a property of the
> counterpart predicate's domain rather than a finding. The both-complete branch is closed
> by the residue-class ceiling of section 4: 36 distinct records over 9 residue classes,
> and the minimum over all 64 declared states of the certified directions the shadow fails
> to fix is nonzero. What the census measures at this corpus is one column — the shadow's.

### M2 — The localization axis, which is the only thing the selector turns on, is not in the pin; the primary arm and the `<object>` slot are supplied by the instrument

The pin declares blocks (FAC's decomposition), separation (SEC's SEAM-CONFINED ruling)
and two descriptions. It never mentions localization: the strings `localization`,
`LOC-PAIR`, `LOC-WALK` do not occur in `note-epr-pin.md`. The axis is introduced at
`epr_exact.py:1699`, the object slot is filled from a two-entry table at `:1702-1703`, and
the primary arm is chosen at `:1818-1819` by a literal filter on
`LOC-PAIR × SEP-LINK-DISJOINT`. Three of the four arms return the other word.

On the mandate's direct question: **`EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY`
does instantiate the pin's registered word-form** `EPR-CRITERION-INAPPLICABLE-AT-<object>`
(`:105`), and the outcome-vocabulary gate confirms it — the parsed families are exactly the
pin's five. The *form* is registered. What is not registered is the axis that selects
between the two emitted words and the object that names it.

The pin's own worked example for that word is also refuted by the corpus: `:107-109` offers
"e.g., no fully link-disjoint block pair exists at R=3". **105,408 link-disjoint block
pairs exist.** The word fired by an entirely different mechanism — link-disjoint pairs are
abundant but none carries a pair-localized quantity.

Per SPC #330 (recommended, not yet engraved): a compounded head must show feasibility at
the declared row list. Here the row list itself is post-hoc.

**Repair.** Two sentences. In §2, after the localization/separation axis declaration at
paper line 137-141:

> Both axes are this unit's own. The pin fixes the blocks, the separation and the two
> descriptions; it does not fix where a cell is read, and the head word turns on exactly
> that. The primary arm is declared here, not pre-registered, and it is declared before the
> census on the ground that a record entry's referent is the pair — section 1's
> measurement — not on the ground of what the arms returned.

And in §3, replacing the pin's refuted example, add:

> The pin anticipated this word arriving through a scarcity of separated pairs. It arrives
> through the opposite: separated pairs are abundant at 105,408, and none of them carries a
> pair-localized quantity.

### M3 — The completeness sentence upgrades at E6, from "complete for the censused certainty-elements" to "a complete theory exists"

Paper line 358 (table row) and lines 362-363:

> | E6 such a theory is possible | one exists on the measured arms | not applicable | yes |
>
> EPR close by saying *"we left open the question of whether or not such a description
> exists. We believe, however, that such a theory is possible."* On the measured arms this
> corpus has one — and it is not a local-realist one.

In the sentence quoted, EPR's "such a theory" is a theory furnishing a **complete
description of the physical reality**. "This corpus has one" therefore asserts completeness
simpliciter. The qualifier "on the measured arms" restricts the *arms*, not the *scope of
completeness* — and by M1 those are precisely the arms on which D-RECORD's completeness is
analytic. This is the only sentence in the unit that upgrades. Elsewhere the unit is
careful: §5's "no certified element lacks a record counterpart, on any arm" is exactly the
licensed form, and §11 correctly disclaims saying what is real.

A second, smaller instance is §7 line 316-317, "That is EPR's conclusion reached inside a
committed theory rather than argued for from outside it" — where by M1 the shadow's
incompleteness is forced by the residue ceiling and the record's completeness is analytic,
so "reached" carries more than was done.

**Repair — exact licensed sentences.** Replace the E6 table row's D-RECORD cell with:

> complete for the censused certainty-elements on the measured arms

and replace paper lines 362-363 with:

> On the arms where the census runs, D-RECORD carries every certainty-element the census
> certifies. That is completeness **for this census, at this arena, over these histories** —
> not the completeness EPR left open, which is a claim about physical reality and which this
> unit neither makes nor could make. It is also not a local-realist result.

Replace §7's line 316-317 with:

> That is the shape of EPR's conclusion, exhibited inside a committed theory: a coarse
> description that fails the completeness condition and a fine one that carries a conjugate
> pair at once. Section 5's disclosure applies — at this corpus both halves are close to
> forced, and section 9 says what the exhibit does not license.

### M4 — §11's "element of reality" self-certification is false, and that wall has no gate

Paper line 414-415:

> The phrase "element of reality" occurs in this unit only inside the formalised predicate
> and inside verbatim quotation of the 1935 paper.

Paper line 34, in the paper's own voice, in neither place, and *answering* the question:

> EPR ask a theory two questions. **Is there an element of reality here?** — yes, if the
> quantity can be predicted with certainty from data that does not disturb the system.

The pin's wall is absolute: `note-epr-pin.md:122-123`, "'element of reality' appears ONLY
inside the formalized predicate". Unlike the Bell wall, this one has **no gate**: the
strings occur in the instrument only as a source comment (`:54`) and a receipt label
(`:2124`). I planted *"There is an element of reality at every block."* into the paper and
reran — the run **passed**.

**Repair.** Rewrite paper line 34-36 so the paraphrase is put in EPR's mouth rather than
the unit's, and gate it. Replacement sentence:

> EPR ask a theory two questions. Their criterion says a quantity predictable with
> certainty from data that does not disturb the system has, on their account, a counterpart
> that a complete theory must carry; their condition of completeness says every such
> counterpart must be there. This unit turns both into total exact predicates on the
> committed arena and runs them.

Then extend the wall gate with a second needle set — the phrase outside quotation marks
and outside the predicate's own name — so the self-certification at §11 is machine-backed
rather than asserted.

### M5 — The Bell wall is enforced by a literal seven-string match; six semantic variants pass

`BANNED` (`:2110-2118`) is seven fixed strings and the check is
`hits = [s for s in BANNED if canon(s) in hay]` (`:2888`). I wrote six variants and
planted each into the paper, one at a time, rerunning the full instrument each time:

| planted sentence | result |
|---|---|
| "Einstein was right about locality." | **passed — not caught** |
| "Spooky action at a distance is refuted here." | **passed — not caught** |
| "The record restores locality." | **passed — not caught** |
| "A hidden-variable completion is vindicated by the record." | **passed — not caught** |
| "The corpus evades Bell's theorem." | **passed — not caught** |
| "There is an element of reality at every block." | **passed — not caught** |
| "local realism is restored" (exact control) | died at G-WALLS-SCAN-THE-PAPER |

**The paper itself is clean.** My own sweep of the delivered bytes finds zero occurrences
of "local realism", "hidden variable", "spooky"; the two occurrences of "locality" are
§4's "the locality that EPR's criterion needs is bought, here, by attributing to a block a
quantity that belongs to a pair straddling its boundary" and §9's own prohibition sentence;
the single "nonlocal" is inside the v5 paper-14 quotation; the single "Einstein" is the
byline. §9's rendering of v5 paper-14's (E1) and (E2) verdicts is **byte-exact** against
`v5/relativistic-isp-v5-paper14-...md:127-130`. The falsifier plant does die on the paper
leg, as the pin requires.

So this is an assurance defect, not a false sentence. The paper's §12 description of the
gate ("Seven banned sentences ... are scanned") is literally accurate; the standing wall is
nonetheless not enforced by it.

**Repair.** Either widen the needle set to token-level patterns (locality + restored/
recovered/regained; Bell + evade/escape/circumvent; hidden variable + vindicated/
established/exists; spooky + refuted/disproved; Einstein + right/vindicated), or amend §12
to state the gate's actual reach. The honest amendment, if the needles are not widened:

> The wall is additionally spot-checked by the instrument against seven exact sentences,
> and the falsifier for that gate plants one into this text; the scan is a literal match and
> is not a substitute for the reading.

### M6 — The E5 zero is analytic, and the test-declaration duty is discharged on one leg only

`record_at_B_under` (`:2033-2040`) is, outside the mutant branch, `tuple(row[d] for d in
qs)`. The parameter `rd` is bound *only* inside `if mut("MUT-E5-LEAK")`. `shadow_at_B_under`
(`:2043-2048`) is the same shape. So "B's own record moves at 0 of 105,408 probes" is a
property of the accessor's body, not a measurement of any modelled channel. MUT-E5-LEAK
proves the gate would catch an *injected* leak; it cannot probe a physical dependence,
because none is modelled. By contrast `assigned_description` (`:1865-1868`) genuinely
consults `rd` through `rfib[rd][row]`, so the 105,408 side is a real computation. The
contrast the paper draws is between a computation and a no-op.

The pin ordered otherwise — `note-epr-pin.md:80-81`: "(Expected NO by seam-confinement —
**measured, not assumed**)". And the test-declaration duty (AID MAJOR-1, carried at
`note-fac-pin.md:65`) requires that where the contrast is the claim, **both** tests run on
**both** objects. Only the transported-reading leg runs; there is no fixed-attribution
counterpart. The paper's line 332 and 335-336 — "The test-declaration duty is discharged
rather than promised ... The zero is a measurement, not a blind spot" — overstate.

Note the mandate's phrase "only the assigned description moves" does not occur in the
paper; the rendering under review is paper line 329-330.

**Repair.** Replace paper lines 332-336 with:

> The test-declaration duty is discharged on the transported-reading leg and stated to be
> the only leg run. The probe is SIGHTED against injection: B's record and B's shadow are
> reached through a reading-parameterised path and a declared falsifier routes the reading's
> own index into both, dying at this gate. What the zero is *not* is a measurement of a
> modelled channel — a reading is a description of A, not an operation on the arena, and B's
> record is read straight off the committed history. The zero is therefore forced by the
> model and demonstrated to be uninjected, and it is reported as that rather than as a
> discovery.

### M7 — An unmeasured universal-modal causal sentence at the E5 arm

Paper line 338-339:

> This is SEC's ruling seen from the other side. No sector-private link moves, so **nothing
> done to a separated block can move this one's record.**

The measured variable at this arm is the declared **reading** — five values — not any
operation. The unit's only dynamical measurement, `disturbance_census` (`:1379-1406`), uses
`ib = loc_pair(B)`: **LOC-PAIR ownership only**, never LOC-WALK. And its confined events
exist only for blocks of three or more actors (measured: 24 confined events, 54 cell
probes, all from the 3×3 class partitions), because a division event has three actors and
cannot fit inside a smaller block. At the E5 arm **every block is a singleton** — all
105,408 pairs are singleton-against-singleton — so the dynamical reading is vacuous exactly
where §8 invokes it.

§3 is correctly scoped and should be credited: it binds the dynamical result to census row
2, which is the row whose blocks are lines. §8 does not carry that binding. This is the only
sentence in the paper that reads causation into the zero, and it is the only unlicensed
dynamic-vocabulary sentence in the paper's own voice.

**Repair.** Replace paper lines 338-341 with:

> This is SEC's ruling seen from the other side, and it is a kinematic statement: no
> sector-private link moves. It is not a measurement of what any operation on a separated
> block would do — the variable moved here is the declared reading, and the unit's dynamical
> probe of section 3 runs at the pair localization and at block sizes this arm does not
> contain. What EPR would not permit — a reality depending on the distant choice — does not
> occur among the readings declared; what does occur is a description depending on them,
> which is section 6.

### M8 — EPR's own sufficient-not-necessary caveat is nowhere in the unit, and §9 puts a premise in their mouth

Read in the original, p.777 col.2 running to p.778 col.1, immediately after the criterion
the pin anchors as E2:

> "It seems to us that this criterion, while far from exhausting all possible ways of
> recognizing a physical reality, at least provides us with one such way, **whenever the
> conditions set down in it occur**. Regarded **not as a necessary, but merely as a
> sufficient, condition of reality**, this criterion is in agreement with classical as well
> as quantum-mechanical ideas of reality."

The words *sufficient*, *necessary*, *exhausting* and *whenever the conditions* occur
nowhere in `paper-38-epr.md` and nowhere in `note-epr-pin.md`. The pin's six anchors omit
the caveat entirely; the paper inherits the omission.

This matters directly to the head. EPR's criterion is explicitly only sufficient, and
explicitly applies *whenever its conditions occur*. Its non-instantiation at the pair
localization is therefore, **on EPR's own terms, a no-op**: it licenses nothing about
whether elements of reality are there, and it is not a finding against them. The paper
nonetheless closes §9 at lines 375-377 with:

> **EPR's premise — that a criterion of reality can be applied to a system in isolation — is
> where this arena resists them first**, before any question about completeness is reached.

EPR premised no such thing. The caveat is the explicit disclaimer of it. This is the one
place in the unit where words are put in EPR's mouth.

The rest of the 1935 fidelity is sound and should be credited. E1, E2, E3, E4 and E6 are
quoted accurately and used in context. E5 is correctly understood: in the original it sits
inside EPR's *refusal of an objection* — the restrictive alternative criterion under which
P and Q are not simultaneously real — and both the pin ("the objection refused") and the
paper's §8 lead-in render it that way. §7's use of E3 is faithful to the disjunction and to
EPR's route through it.

**Repair.** Add the caveat to the pin's anchor list as E2b, and add to §3, after the
sentence at paper line 176-178:

> EPR guard this case themselves. Immediately after stating the criterion they call it
> *"far from exhausting all possible ways of recognizing a physical reality"*, applying
> *"whenever the conditions set down in it occur"*, and *"not a necessary, but merely a
> sufficient, condition of reality"*. So the criterion's non-instantiation here is not a
> verdict against anything: it decides nothing about what is or is not at the pair
> localization, and it is not a defeat of EPR's argument. It is a measurement of what this
> arena will let their test be applied to.

And replace paper lines 375-377 with:

> The criterion is applicable here only in the localization the quantum state uses, and
> there the quantity attributed to a block has as its referent a co-division pair straddling
> that block's boundary. That is a fact about this arena's smallness, reported under EPR's
> own sufficiency caveat: the criterion is silent where its conditions do not occur, and so
> is this unit.

---

## MINORS

**m1 — a typed count in the control arm the paper calls scope-fixing.** `:2288` publishes
`"without_counterpart_in_D_RECORD": 0` as a bare literal, where every other arm calls
`reg()` on a computed value, and the head law reads that field at `:1714`. §10 line 401
calls this row "the one that fixes the head's scope". I computed the field: **0** — the
typed value is correct and no number moves. "Counts computed, never typed"
(HANDOFF §4) is nonetheless breached. Repair: compute it, as the sibling arms do.

**m2 — "the two declared coin orders" denotes two different objects.** §7's 30-of-36 is the
matrix pair `G·D(x)` vs `D(x)·G`; §4 uses the identical phrase for the two *readings*,
whose Born menus differ at **24** of 36 — a number the unit never publishes. The em-dash
gloss names the matrix object, so this is a precision cost, not a false number. Repair:
"the two declared coin orders' **operators** differ at 30 of the 36 committed records".

**m3 — the E4 fibre of five is wider than the phenomenon quoted.** The E4 count runs over a
five-reading menu of which only 3 unordered pairs are non-jointly-declarable (measured;
I reproduce 3, and they are BORN-GD/RECORD-MENU, BORN-GD/CURVATURE, RECORD-MENU/CURVATURE).
READ-RECORD is the theory's own state and refines every reading, so including it in a count
anchored to EPR's *two wave functions of non-commuting operators* inflates the fibre
relative to the phenomenon. The menu is named at §6, so the referent is disclosed. Repair:
add "of the five, three unordered pairs are non-jointly-declarable; the fibre of five
counts declared coarsenings, not conjugate alternatives."

**m4 — the verdict block's second word carries no best-state stamp.** §4 establishes the
audit is at the shadow's best case (sweep max 4, primary 4 — both reproduced), but the
`SECOND-WORD=` field carries only SCOPE, COUNTING-ONLY and NO-LOCAL-REALISM-CLAIM. Repair:
append `AT-THE-SHADOW-S-BEST-DECLARED-STATE`.

**m5 — certification is total and the paper does not say so.** The site-constancy ground
*is* disclosed where the certainty rests on it — §5 lines 240-245 and §11 lines 428-430,
and this discharges that half of the mandate. What is not stated is the consequence:
certified ≡ quantities on all four arms (0/0, 54/54, 316,224/316,224, 1,265,112/1,265,112)
because `set(qs) ⊆ set(da)` at 132 of 132 specs. The reader must infer it from two equal
table columns. Folded into M1's repair.

**m6 — v5 paper-14 is rendered byte-exact but stripped of its own qualifiers.** The source
carries "in the technical sense", Prop 14.2's antecedent "Under SO∧MI∧PI", the unistochastic
scoping of the Tsirelson leg, and an explicit refusal of any one-word answer. §9 renders the
flat (E1)/(E2) sentences only. Direction is conservative — a wall stated without its
qualifiers is a stronger wall — so this is a fidelity note, not a defect in the prohibition.

**m7 — §9 and §11 sit in tension over what the separation is.** §9 line 363-365 places
D-RECORD's joint value assignment "at the outcome-dependence level the corpus already
owns"; §11 line 420-423 says the separation is kinematic and "is not a spacelike separation
and no claim about spacelike separation is made or implied". Bell's OI is defined over
spacelike wings. The pin licenses the §9 sentence verbatim (`:88-91`) and its direction is
conservative — it assigns more constraint, not less — but it asserts an identification the
unit does not measure. Repair: "lives at the level the corpus's standing verdict already
owns; the identification with Bell's outcome dependence is the pin's, not this unit's
measurement, and the separation here is kinematic."

---

## What the mandate asked, item by item

1. **The head.** Word-form registered: `EPR-CRITERION-INAPPLICABLE-AT-<object>` is the
   pin's, and the emitted string instantiates the slot; the vocabulary gate confirms the
   five families are parsed from the pin's bytes. Selectors **not** both multi-way: the
   second word's record-complete leg is analytic (M1) and its shadow-incomplete leg is
   forced by a pigeonhole computable at pin time (M1); the axis that selects between the two
   words is not in the pin (M2). #299/#319 feasibility: **not met** for two of the four real
   words.
2. **The completeness sentence.** The licensed form is present and correct in §5. One
   sentence upgrades to completeness simpliciter, at E6 (M3); one overreaches at §7 (M3).
3. **The shadow verdict.** Shadow-ceiling best-case disclosure: **present** and established
   in §4 before the census consumes it, with the self-certification triviality disclosed at
   §5. Site-constancy ground: **disclosed** at both §5 and §11 where the certainty rests on
   it. Two gaps: the verdict block lacks the best-state stamp (m4) and the totality of
   certification is left to inference (m5).
4. **E5.** The phrase "only the assigned description moves" is not in the paper; the
   rendering is line 329-330 and is accurate as to what moved. Test-declaration duty:
   **half discharged** (M6). Causation read into the zero: **yes, once**, at line 339 (M7).
5. **The Bell wall.** Swept by this seat: the paper is **clean** — no local-realism,
   Bell-evasion, hidden-variable or spooky-action claim in its own voice; the v5 paper-14
   rendering is byte-exact; the falsifier plant does die on the paper leg. The gate behind
   it is a literal seven-string match through which six semantic variants pass (M5). The
   OI/PI scoping sentence is correct as against paper-14 but carries a tension with §11 (m7).
6. **1935 fidelity.** E1–E6 quoted accurately and used in context, E5's "objection refused"
   framing correct. The sufficient-not-necessary caveat is absent from both pin and paper,
   and §9 attributes to EPR a premise their own caveat disclaims (M8).
7. **Stamps.** Scope stamps present in the verdict block and §11 (one arena, committed
   histories, kinematic separation as measured). FAC/SEC candidate-under-repair stamps
   present and correct at §11 lines 433-439, including the abstention from the drifted
   parent, which the read-set gate makes provable. E-24 COUNTING-ONLY present at §11. Every
   fraction referent-bound (7 fractions, 6 declared universes, gate passes). No dynamic
   vocabulary beyond license except line 339 (M7).

## What is sound and should not be re-litigated

The arena and corpus rebuild, the block layer against FAC's cited receipt, the predicate
freeze with the free-name leak check, the exact-rational probability-one cross-check at
1,080 probes, the two-route head derivation (`head_route_two`, `:2382-2431`, genuinely
shares no dispatcher and no cache), the seal totality and read-back, the off-tree
byte-identical reproduction, the falsifier reachability by AST, the numeral and
table-header coverage of the paper, and the three synthetic control arms that are real
evaluations of the real predicates rather than forged rows. The central *physical* finding
— that at this arena EPR's criterion is instantiable only in the localization the quantum
state uses, and that there the quantity attributed to a block has as its referent a
co-division pair straddling that block's boundary — is measured, correct, and survives
every fix above.

---

*Candidate until adjudication. Five hashes re-verified at close, unchanged: paper-38
550e3c8fff93 (487 lines), epr_exact.py 9ed817d9649d (3511), epr_output.txt 1b30c6761281
(188), epr_receipt.json a51326de11a8 (2789), pin b1e4cf9a8b9f (137).*
