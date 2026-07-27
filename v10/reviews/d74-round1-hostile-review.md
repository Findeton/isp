# D74 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-27.
**Unit under review:** D74 "the transport holonomy" —
`note-d74-transport-holonomy-pin.md` (STRICT, frozen and committed before any
code was written; four arms TH-A/B/C/D, three pre-registered outcomes
TH-I/II/III, Lean NONE), `note-d74-transport-holonomy-result.md`
(GREEN-UNREVIEWED), `code/d74_transport_holonomy_exact.py` +
`data/d74_transport_holonomy_exact.out` (41 PASS / 0 FAIL, exit 0, 282 s,
3 passes labelled no-independent-information), LOG #494.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`ref_recompute.py`, `ref_attack.py`, `ref_attack2.py`,
`ref_attack3.py`, `ref_attack4.py`, `ref_attack5.py`, under the session
scratchpad): my own family enumerator, my own exchange-square census, my own
`mu` map, my own six-rung abstraction ladder, my own menu quotient and
partition-refinement congruence, my own prime-valuation group computation, my
own linear-extension / order-dual machinery, my own orientation census. The
only object I share with the unit is the committed substrate
`v10/code/d42b1_transport_exact.py` (`candidates_for` / `admissible` /
`event_poset` / `View` / `canon` / `regs_of`), which no unit may
re-implement. Nothing was read out of the unit's `.out` except to diff a
re-run against it.
Calibration: `reviews/d72-round1-hostile-review.md` **and its DELTA**,
`note-d72-weld-result.md` (all of it, licensed claims and residues),
`reviews/d70-round1-hostile-review.md`, `reviews/d73-round1-hostile-review.md`,
`note-d71b-holonomy-phase-identity.md` (**all of it**, including its own
`[SILENT]` gradings and §6 limits), `note-d65-descent-conditions-result.md`
(§3.1 the repair cone, residues 2 and 3, the explicitly-not-licensed list),
`v10/code/d42b1_transport_exact.py`.

**VERDICT: REVISE. 5 MAJOR / 6 MODERATE / 6 MINOR.**

**The arithmetic is clean and the two hardest structural results survive my
attacks.** Every anchor and every headline number I recomputed reproduced
exactly from my own instrument: the `AB4` census `{both-blocked 142, closed
1546, AB-only 28, BA-only 12}` with ratios `{1: 1458, 1/2: 70, 2/3: 2, 3/2: 6,
2: 10}`, kinds and half-open kinds; `ABC3` `1554 / {1/2: 12}`; 3,969 histories
/ 2,477 record classes and 3,424 / 2,128; the whole six-rung ladder column for
column; 113 menu classes; the coarsest congruence at 185 classes after 5
refinement rounds; the 44 + 44 dichotomy; the group `⟨2,3⟩`; the
sign-definiteness break `{<1: 868, >1: 8}` at `d ≤ 5` and `{<1: 7116, >1: 344}`
at `d ≤ 6`; CTL-ORDER's transposition. I re-ran the receipt at
`PYTHONHASHSEED=7`: exit 0, 41 PASS / 0 FAIL, output identical to the
committed `.out` apart from timings and the echoed seed.

**And I tried hard to break the two theorems and could not.** The dichotomy
survives every weakening of "descent" I could construct — labelled-edge
single-valuedness, D65's own normalised-menu repair, support-only
identification, and projective (proportional-menu) descent all identify **0 of
the 44**. The group survives the one scope the unit did not run: at a **new
actor pool** `(A,B,C,D)`, depth ≤ 4, 1,728 defective squares and new menu
masses `{4, 9/2}`, the value set is still exactly `{1/2, 2/3, 3/2, 2}` with
prime content `{2,3}`.

**What I broke is the evidential architecture around the negative.** Three of
the unit's load-bearing gates — including the one the odd-sector verdict rests
on — are algebraic identities of their own definitions, counted as independent
evidence in a unit whose §3(b) convicts its parent of exactly that; the
pre-registered outcome predicate cannot return TH-III; and the reversal-**even**
channel that §0 declares empty is not empty — the receipt's own D5 arm
computed the raw material for a non-trivial substrate-supplied even invariant
and never looked at the complement of the 88 squares it evaluated.

---

## MAJOR 1 — Three load-bearing gates are identities of their own definitions, counted as independent evidence. The unit's §3(b) lesson is not applied to the unit.

**Where.** `C0.1` (`.out:128`, receipt:1000-ish block; note §1 TH-C and
licensed claim 2); `D1` (receipt:1685-1708, `.out:284`; note §1 TH-D row D1,
§0, licensed claim 8); `D4.1` (receipt:1752-1783, `.out:292`; note §1 D4.1,
licensed claim 9). Summary block `.out:330` — "41 PASS ... of which 3 carry NO
INDEPENDENT INFORMATION ... 38 independent passes".

**Defect.**

*C0.1 — `r = μ(h·e_A·e_B)/μ(h·e_B·e_A)` on 3,100/3,100.* `mu_map`
(receipt:486-494) defines `μ(h·e) := μ(h)·q(e|h)`. Therefore
`μ(h·e_A·e_B) = μ(h)·q_A·q_{B2}` and `μ(h·e_B·e_A) = μ(h)·q_B·q_{A2}`, and
their ratio **is** the definition of `r`. The identity holds on every closed
square of every grammar with a product weight, at every depth, forever. "3,100
of 3,100, 0 exceptions" is not a measurement of this substrate. The unit half
knows this — but it tags the **wrong gate**: `C0.2` (the tree / `H¹ = 0`
observation, which at least says something about the shape of the sequence
layer) is labelled no-independent-information, while `C0.1`, the actual
tautology, is counted as evidence.

*D1 — "the reversal is exactly inversion, with gap zero, 1,546/1,546".*
receipt:1685-1695 recomputes the same four Fractions `q_A, q_B, q_{B2}, q_{A2}`
and compares `(q_B·q_{A2})/(q_A·q_{B2})` against `1/r`, where
`r := (q_A·q_{B2})/(q_B·q_{A2})`. It is the reciprocal of the same expression.
There is no assignment of weights, no substrate, and no grammar on which this
can return a non-zero exception count. **This is the gate on which "the
log-holonomy is purely odd and has no even part at all" and "the MIRROR of
v7's arrangement" rest** — the unit's single most quoted sentence (note §0,
§1 D1, licensed claim 8, LOG #494) is carried by a test that cannot fail.

*D4.1 — the i-twist and its "500 adversarially drawn positive rationals".* The
predicate actually evaluated (receipt:1758-1765) is
`(-1)*v.numerator*v.denominator == -(v.numerator*v.denominator)`, i.e.
`-x == -x`. It never forms `e^{i log r}`, never applies a reversal, and never
reads the substrate. The "adversarial control" verifies `-x = -x` five hundred
times. `_real_fail` (receipt:1752-1753) counts squares with `r ≠ 1/r`, which
for positive rationals is `r ≠ 1`, i.e. it re-counts the 88 by definition.

**Recomputation.** My own census: C0.1 holds 3,100/3,100 (as it must). D1: 0
exceptions of 1,546 (as it must). D4.1's predicate evaluated on
`1/2, 7/3, 1, 97/5, 123456/7`: `True` for every one.

**Consequence and repair.** The conclusion of D4.1 (*the i-twist is a change of
variables, not a discovery*) is **correct as mathematics** and I endorse it;
what is wrong is that the receipt presents a tautology as its demonstration and
LOG #494 cites "passes on 500 adversarial rationals" as the evidence. Repair:
(i) re-tag `C0.1`, `D1` and `D4.1` as identities/corollaries and restate the
independent-evidence count (38 → at most 35); (ii) state D1 as the one-line
lemma it is — *`r` is defined as a ratio, so swapping the two events inverts
it* — and delete "with gap zero, on exact Fractions, 1,546/1,546", which
implies a measurement; (iii) either delete the 500-rational control or replace
it with one that actually evaluates the twisted law on drawn inputs.

---

## MAJOR 2 — The pre-registered outcome predicate cannot return TH-III. The three-way pin is decided by a two-way test.

**Where.** receipt:1936 `ODD_FOUND = bool(_unimod - {Fr(1)}) or _dual_conj > 0`;
`_unimod` at receipt:1711-1712; `_dual_conj` at receipt:1804-1831; the outcome
cascade at receipt:1961-1976; `.out:315-325`. Pin §2 lists TH-III ("the odd
residue exists — the U(1) seed") as a live outcome; pin §4 says "the
odd-sector search's negative is as reportable as its positive".

**Defect.** Both disjuncts are structurally incapable of firing.
`_unimod = {v ∈ _allvals : v == 1 or v == −1}` where `_allvals` is drawn from
ratios of products of committed weights — all positive rationals. The unit
**itself proves** at `D2` that `−1` can never occur there ("every weight the
committed layer produces is a POSITIVE RATIONAL ... the only positive rational
of modulus 1 is 1"). So disjunct one is `∅` by a theorem the receipt states two
gates earlier. `_dual_conj` is incremented only inside `if _o1 and _o2:`, and
`_dual_pairs = 0` — the loop body never executes. So disjunct two ranges over
the empty set.

The outcome selector therefore reads: `TH-I` if the carrier has no non-unit
self-loop, else `TH-II`. TH-III is unreachable on any input this receipt can
produce, and no measurement in the unit could have changed the branch.

**Recomputation.** Trivial by inspection and confirmed by the receipt's own
`.out:320` (`an orientation-sensitive (conjugating) residue exists = False`)
being the only value that line can take.

**Repair.** A pre-registered outcome must be decidable in every direction by
the fixture. Either (a) redesign TH-D so that a positive is representable —
the natural move is to admit non-scalar-valued residues (see MAJOR 3), since
the unit has already proved a scalar `U(1)` part is impossible a priori — or
(b) retire TH-III from the pin's outcome set and state plainly that on a
positive-rational-valued connection the odd-sector question is answered by D2
alone, in one line, before any fixture is run. What must not stand is a
"0-for-4 at the grammar's native addresses" tally (LOG #494) in which this
address was scored by a predicate that had no positive branch.

---

## MAJOR 3 — The reversal-EVEN channel is not empty. The receipt's own D5 arm computed the raw material and drew the opposite conclusion for want of a control.

**Where.** Note §0 ("reversal is exactly inversion, so the log-holonomy is
purely odd and has **no even part at all** — the mirror image of v7's
amplitude, which puts the modulus in the even channel and the phase in the odd
one"); §1 D1 and D8 ("no orientation-sensitive residue exists on this carrier
... Everything invertible under reversal; nothing conjugating"); §1 D5.1 and
its stated reason; licensed claim 8.

**Defect.** Two separate things.

*(a) The stated reason for the 0/176 is factually false.* D5.1 says "the
reversed sequences are **overwhelmingly NOT admissible histories of this
grammar**, so `*` is not an operation on the defective squares at all". That is
not true of this grammar. Over the whole `AB4` family with `|h| ≥ 2`, **2,456
of 3,960** reversed sequences are admissible histories (62%; by length: 56/60
at `|h|=2`, 352/452 at 3, 2,048/3,448 at 4). Over the closed-square endpoints
specifically, **2,196 of 3,092** (71%) are reverse-admissible — including
1,798 of the 2,286 endpoints that contain a delivery. The grammar is not
reversal-blocking. The 0/176 is therefore **not** a generic support fact; it is
a sharp and highly non-generic property of the defect locus, and the unit
attributed it to the wrong cause because it evaluated its own predicate only on
the 88 defective squares and never on the complement.

*(b) That predicate is a non-trivial reversal-even invariant, and it separates
the curvature support exactly.* Define
`J(square) := [both endpoint sequences are reverse-admissible]` — precisely
what `admissible_history` (receipt:1791-1801) computes. `J` is symmetric in
`(e_A, e_B)`, hence reversal-**even**; in my census it is never mixed (the pair
`(rev_A, rev_B)` is never `(True, False)`). It is non-constant on the closed
census, and:

```
   AB4        J=True 1098  (all r = 1)   J=False 448  (360 unit + 88 defective)
   ABC3       J=True 1476  (all r = 1)   J=False  78  ( 66 unit + 12 defective)
   (A,B) d<=5 J=True 6026  (all r = 1)   J=False 5788 (4828 unit + 960 defective)
```

**`J = 1 ⟹ r = 1`, on 8,600 closed squares across three arms, zero
exceptions**; and `J = 0` on every defective square of every arm. It is not a
relabelling of the register invariant the unit already has (A2.1 / D72 T2.3b):
793 of the `J=True` squares at `AB4` are register-**overlapping**, and 168
register-disjoint squares have `J=False`.

**Recomputation.** `ref_attack2.py` (calibration), `ref_attack3.py`
(cross-tabulation and depth stratification: at depth 4, 912 of 1,252 unit
squares have `J=1` and 0 of 84 defective do), `ref_attack4.py` (ABC3 and
`d ≤ 5`, and the cross-tab against `regs_of` overlap).

**Consequence.** The "mirror of v7" reading is the unit's most striking
sentence and it does not survive. v7 puts the modulus in the **even** channel;
the unit concludes the transport object leaves the even channel empty. That
conclusion is drawn entirely from `log r`, where "no even part" is the
tautology of MAJOR 1. On the carrier itself there *is* non-trivial even-channel
structure, it is supplied by the substrate rather than the enumeration (which
is exactly what D6 was hunting and failed to find in the odd channel), and it
is a **flatness predicate**. D8's second clause — "every quantity this unit
could build on the holonomy-carrying loops inverts under reversal" — is
refuted: `J` neither inverts nor conjugates; it is invariant, and it is not
constant.

**Repair.** `J` is `[MEASURED]` on three windows and is **not** a theorem; I do
not ask for it to be licensed as one. What I ask is that §0, §1 D1 and D8, and
LOG #494 stop asserting that the even channel is empty on the strength of a
statement about `log r`; that D5.1's reason be replaced by the measured one;
and that the `J`-vs-`r` table be run (it costs seconds — the receipt already
has the function) and reported, in whichever direction it comes out at wider
depth. Whether `J = 1 ⟹ r = 1` survives `d ≤ 6` and three actors is the
natural first line of the successor.

---

## MAJOR 4 — "D71b's linear-extension carrier" is a mis-citation, and the D5 arm builds neither of the two carriers it names. (The negative itself survives, at greater strength than the unit established.)

**Where.** receipt:1787-1788 (section header "THE ORDER-DUAL ARM — D71b's
linear-extension carrier, at transport scope"); receipt:1791-1801 docstring
("the order-dual of a history is its reversal read as a sequence: D71b's rev on
linear extensions"); note §1 D5.1 ("D71b's carrier is real, and it is empty at
this scope"); LOG #494 ("the order-dual IS NOT DEFINED here (0/176 reversed
sequences admissible) — the v7 phase lives in a different CATEGORY").

**Defect.** Three distinct objects are being conflated.

1. **D71b's carrier is not linear extensions.** The phrase does not occur in
   `note-d71b-holonomy-phase-identity.md`, in `note-d71-phase-archaeology.md`,
   or in v7 paper 30. D71b's carrier is the committed **unlabeled record order**
   `R` (a permutation-order type; the hidden permutations are projected away by
   `ρ_N`), and its `*` is **poset reversal of a five-record order type**
   (`paper30:2506-2511`, quoted at D71b `:258-291`). Poset reversal is defined
   on every poset. It is never "not defined". "Linear extensions" is **D72's**
   common-carrier construction (`note-d72-weld-result.md:60`, licensed claim 2,
   scoped to 2-event histories "and on nothing larger").
2. **The receipt tests a third thing.** It reverses **one** enumeration-chosen
   sequence per endpoint and asks whether that bare sequence is admissible from
   the empty history. That is neither poset reversal on a record type nor a
   statement about linear extensions.
3. **The AST signature pass requires `linear_extensions` (receipt:336) and the
   receipt never calls it.** grep over the whole file: one hit, in `B1_REQ`.
   The one committed function that would have implemented the arm honestly is
   declared as a dependency and left unused.

**Recomputation — and the unit's conclusion survives.** I ran the honest
version. For each of the 176 endpoint sequences of the 88 defective squares I
built the event poset, enumerated **every** linear extension (304 in total, all
304 admissible in the forward direction), reversed each, and tested
admissibility: **0 of 304**. So the negative is real, and is in fact stronger
than the unit's single-sequence test established — it is a statement about the
opposite **poset** having no admissible realisation at all, not about one
enumeration order.

**Repair.** Fix the attribution (D71b's carrier is the record order; the
linear-extension carrier is D72's, at 2-event scope); replace the
single-sequence test with the all-linear-extensions test, which is cheap and
strictly stronger; and restate LOG #494's clause — the order-dual is *defined*
(it is poset reversal), what is measured is that the dual poset has **no
admissible realisation in this family**, 0/304. That is a better sentence than
the one currently in the LOG and it costs nothing.

---

## MAJOR 5 — The dichotomy is stated three times without the qualifier that makes it true, and a quotient graph that closes the "unclosable" half sits on the unit's own ladder.

**Where.** §0 ("a square whose two orders have different menus **cannot close in
any descent quotient whatsoever**" — correct; then "44 of a **descent
obstruction** that no quotient graph can carry" — not correct); §1 A3.2 and the
gate's own text at receipt:1541-1542 ("a DESCENT OBSTRUCTION **that no quotient
graph can carry**, and for which **the exchange square is the only
instrument**"); §3(d) (same, plus "**This is a new object in the corpus**");
residue 1 ("The corpus has no object for this"). Licensed claim 5 is correctly
scoped and is not at issue.

**Defect.** "No descent quotient" and "no quotient graph" are different
statements, and the second is false on the unit's own page. **MULT** — rung 3
of the C2 ladder, the multiset-of-events quotient — closes **88 of 88**
defective squares (`.out:164`, and my recomputation), which includes **all 44**
of the descent-obstruction half. MULT is a perfectly good quotient graph; what
it fails is *descent*, by 8 multi-valued labelled edges out of 3,391, which the
unit itself reports in the `multi-w` column. So the exchange square is not "the
only instrument", and residue 1's "the corpus has no object for this" is
answered three rows above it in the same table.

**Recomputation.** `ref_attack5.py`: MULT closes 88/88 defective squares,
including 44/44 of the menu-quotient's unseen set. Also checked: PORT closes
exactly the same 44 as MENU (set equality, not just count equality) — the
identity the note asserts at C2.4/A3.1 is true as sets, which is stronger than
what it claims.

**Repair.** Insert "descent" in all three places, or say instead what is
actually true and interesting: *the descent-obstruction half is closable only
by quotients on which the connection is not well defined*. Residue 1 should
then be re-posed as "is there a formalism for a defect that is visible only
after descent is abandoned" — a sharper question than the one now written.

---

## MODERATE 1 — The §3(a) status correction is mis-addressed to D72's licensed claim 7, which does not contain the numbers it corrects.

**Where.** §3(a) ("`{1/2: 70, …, 2: 10}` and `AB-only 28, BA-only 12`
(**licensed claim 7**) should be restated"); licensed claim 10 ("that the
AB-only/BA-only split or the unpaired spectrum are substrate facts");
`.out:337`.

**Defect.** D72's licensed claim 7 (`note-d72-weld-result.md:396-400`) reads in
full: "*88 of 1,546 closed exchange squares have `dP_AB/dP_BA ∈ {1/2, 2/3, 3/2,
2}` and 40 further squares are half-open; at `(A,B,C)` depth ≤ 3, 12 of 1,554
at 1/2. Every one carries a delivery event; none closes at record level.*" It
licenses the **value set** and the **totals**. The multiplicities
`{1/2: 70, …}` and the `28/12` split appear in D72's §1 table rows T6.1/T6.2
and in its DELTA, and in **no** licensed claim. D72's round-1 referee reported
the same numbers from its own instrument and never interpreted the 28/12
asymmetry either.

**Consequence.** The substance of the correction is right and worth routing.
Its addressee is wrong, and as written it implies D72 licensed something it did
not. Repair: route the correction against `note-d72-weld-result.md:150-151`
(the T6.1/T6.2 rows) and the DELTA, and note that D72's licensed claims already
survive CTL-ORDER untouched — which is a *credit* to the parent that the
current wording withholds.

---

## MODERATE 2 — CTL-ORDER is applied to the parent and not to the unit's own dichotomy headline.

**Where.** §1 A3.2 ("every one of the invisible half is an `(r,d)` pair at the
single value `1/2`"); §3(d) ("all of them `(r,d)` pairs at `1/2`"); the gate
predicate itself at receipt:1549-1551, which tests
`set(unseen spectrum) == {1/2}` and `set(unseen kinds) == {("r","d")}`.

**Defect.** These are precisely the quantities the unit's own CTL-ORDER
declares to be enumeration-orientation readings. I re-ran the identical
dichotomy under the reversed candidate order:

```
   forward   seen 44 / unseen 44   unseen spectrum {1/2: 44}  kinds {(r,d): 44}
   reversed  seen 44 / unseen 44   unseen spectrum {  2: 44}  kinds {(d,r): 44}
                                   seen spectrum transposed likewise
```

The 44 + 44 split is invariant (good, and licensed claim 5 says only that); the
kind-clean refinement is not. A gate whose predicate asserts an
orientation-dependent value set is exactly the defect §3(a) routes upstream.

**Repair.** State the invariant form — 44 + 44, and the unordered class
`{1/2 ≡ 2}: 44` — or carry the orientation convention explicitly, as §3(a)
demands of D72. Note that the deeper arms' unseen spectra (`{1/2: 348, 2/3: 8}`
at `d≤5`, `{1/2: 378, 2: 30}` at `(A,B,C) d≤4`) are genuinely two-valued and so
are partly orientation-robust; the AB4 row is the fragile one.

---

## MODERATE 3 — §3(e)'s "correction" to D65 is D65's own committed residue, and `⟨5/4⟩` is D72's construction, not D65's.

**Where.** §3(e) ("**D65's committed `{4/5, 5/4}` is a two-actor statement** and
should not be carried as the shape of the mass twist in general ... recorded
here and **routed to the principal**"); §6; B.2 and `.out:270` ("D65's `⟨5/4⟩`
has prime support `[2,5]` and rank 1").

**Defect.** D65 already says this, in its own voice, twice. Residue 2
(`note-d65-descent-conditions-result.md:613-617`): "*`M` takes two values here
because the quarter law's excess is binary at two actors. At three actors or
with delivery the mass spectrum changes and the coboundary statement must be
**re-derived, not carried**.*" And its explicitly-not-licensed list (`:600-601`)
forbids "*any of the above at three-actor scope, **at transport scope**, or
beyond the exhaustive depth-6 family*". D65's scope header (`:51-58`) is
"non-negotiable and load-bearing in every sentence below: TWO-ACTOR,
DELIVERY-FREE". Routing this to the principal as a correction implies the
parent overreached; it did not.

Separately: D65 never writes group notation and never asserts a holonomy group
— grep confirms `⟨5/4⟩` occurs nowhere in it. The infinite cyclic group
`⟨5/4⟩ ⊂ R+` is **D72's** object (T4.3, licensed claim 6). D74's B.2 and §0
attribute it to D65.

**Repair.** Downgrade §3(e) from a routed correction to a confirmation:
*D65's residue 2 predicted this and the three-actor menu masses `{3, 7/2, 19/4}`
and ratios `{6/7, 7/6}` confirm it at transport scope* — which is a genuine and
citable result, and better than what is currently written. Re-attribute
`⟨5/4⟩` to D72 claim 6.

---

## MODERATE 4 — "The coarsest descent quotient exists and is unique because descent is closed under joins" is a definitional remark sold as a construction; and A3.3's self-loop is a tautology of the exchange graph.

**Where.** receipt:1418-1429 (the CONSTRUCTION block) and `.out:210-222`; note
§0 ("descent is closed under joins, so a coarsest descent quotient exists and
is unique ... it is **not a search**"); licensed claim 4; §1 A3.3 and gate
A3.3 (receipt:1564-1574).

**Defect (a).** "Descent quotient" is defined as: `h ~ h'` implies
`q(·|h) = q(·|h')`. That is exactly "`~` refines `ker(menu)`". The set of
equivalences refining the kernel of a fixed function has a maximum — the kernel
— by definition. So existence, uniqueness and the identification with the menu
partition are one and the same triviality; the join-closure argument is
decoration on a statement that needs no argument, and "not a search" is true
because the definition names the answer. Note that the notion was *chosen* so
that a coarsest exists: the weaker and arguably more natural notion for a
labelled quotient graph — *`h ~ h'` need only agree on the weights of events
admissible at both* — is **not** join-closed and has no unique coarsest. The
unit does not say it made this choice.

**Defect (b).** In the exchange graph, the edge of a square runs between the
classes of its two endpoints (receipt:1471). So "the square closes in the
quotient" and "the square's edge is a self-loop" are the same statement. A3.3's
"the closing defective squares are LOOPS — self-loops at a single class" and
its gate (`non-unit self-loops == len(seen)` on every arm) are definitional. The
non-removability **verdict** is genuine — a non-unit self-loop is
gauge-invariant outright, and that is the right argument — but no structural
fact about self-loops was discovered.

**Recomputation.** I built the menu quotient (113 classes) and the
partition-refinement congruence (185 classes, fixed point after 5 rounds)
independently: 44 and 44 defective squares closed, same sets. The **measured**
content of claim 4 reproduces exactly and is not in question.

**Repair.** Demote the coarsest-quotient sentence to a definitional remark;
state the choice of descent notion and why (I checked the weaker notion — see
CLEAN below — and it changes nothing, which is worth saying); let the measured
44 / 44 / congruence agreement carry claim 4.

---

## MODERATE 5 — "Unmoved across 8 scopes" — the eight scopes are two nested chains plus two of their sub-grammars, and none goes beyond three actors. (I ran the missing scope; the claim survives.)

**Where.** Note §0 and TH-B table ("stable across eight scopes and two
asymmetric sub-grammars ... while the defect count runs from 88 to 14,736");
B.1 (`.out:269`); LOG #494.

**Defect.** `census_arm` (receipt:1282-1299) enumerates bases to depth `dep−2`,
so the `d ≤ 5` arm re-counts every `d ≤ 4` square and the `d ≤ 6` arm re-counts
every `d ≤ 5` square. I verified the containment directly: the 88 defective
squares of `AB4` are literally a subset of the 960 of `(A,B) d ≤ 5`. Likewise
`ABC3 ⊂ ABC4 ⊂ ABC5`. ASYM-1 and ASYM-2 are support-restrictions of `(A,B)
d ≤ 5` and `(A,B,C) d ≤ 4`. So the eight scopes are **two nested chains plus
two sub-grammars of them**, with actor pools of size 2 and 3 only, and the
"88 → 14,736" range partly counts the same squares repeatedly. Along a nested
chain the value set can only grow, so "it does not move" has content — but
"eight scopes" implies eight independent tests and the phrase should not stand.

**Recomputation — and the claim survives the scope the unit did not run.** I
added a **new actor pool**:

```
   (A,B,C,D) d<=3 : closed 6,624    non-unit    24   values {1/2}          primes {2}
   (A,B,C,D) d<=4 : closed 155,704  non-unit 1,728   values {1/2,2/3,3/2,2} primes {2,3}
                    menu-mass spectrum {4: 569, 9/2: 24}  (new masses)
```

New pool, new menu masses, an order of magnitude more defects than `AB4` — and
the value set is exactly the anchor window's, prime content `{2,3}`. **No new
prime enters at four actors.** This is the first genuinely independent scope in
the group claim and it confirms it.

**Repair.** Restate as "two nested depth chains at two pools, plus two
asymmetric sub-grammars, plus (if adopted) a four-actor pool", and cite the
four-actor arm — which is a stronger result than the one currently claimed.

---

## MODERATE 6 — "No corpus formalism handles the second kind" is too strong: D65's repair cone computes the same split.

**Where.** §3(d) ("**This is a new object in the corpus**"); licensed claim 10
("no formalism in the corpus currently handles it — residue 1"); residue 1
("The corpus has no object for this").

**Defect.** D65 §3.1 (`note-d65-descent-conditions-result.md:277-299`) solves
two linear systems over **Q** — "repairs the defect" and "descends to the
record" — and reports, at `D = 4`: "*repair rows NOT implied by
record-constancy = **152 of 403** (= exactly the rows whose two corners carry
**different records**)*". That is the same criterion as D74's dichotomy — a
square whose two corners land in different classes of the identification —
computed under a different functor and at a different scope, with the
transverse dimension counted (313 record-constant, 205 in the intersection) and
a positive witness (DC1-R(e)) that annihilates all 403 square identities while
still failing to descend. D70, by contrast, genuinely has nothing: it contains
zero occurrences of holonomy / cocycle / cohomology / coboundary / curvature /
descent, and its one quotient-shaped instrument (HZ5 lumpability) is
cap-bounded and lower-bounded and cannot classify an obstruction.

**Repair.** "No formalism at transport scope, and none that quantifies over
quotients" is defensible and I would pass it. "The corpus has no object for
this" is not — cite D65 §3.1, and note that its residue 3 (the record functor
is a *choice*; a coarser functor breaks the containment) is the standing
warning D74's dichotomy should be read against.

---

## MINOR

1. **§1 D6.1 overstates its own arm.** "under it **every** defective square of
   **both anchor arms** lands strictly **below 1**" — 4 of the 88 at `AB4` are
   unorientable (equal kind rank), so it is 84 of 84 orientable, as §3(f)
   correctly says. Align §1 with §3(f).
2. **§1 C2.1's "(obstruction 88 at every one)"** silently sums two columns its
   own table prints separately (R1 obstruction `0, 0, 44, 44`; self-loops
   `88, 88, 44, 44`). Say which quantity is 88.
3. **D3.1's gate predicate is the bare constant `True`** (receipt:1739) in a
   receipt whose banner promises "no bare-constant predicates"; the block also
   carries dead code (`_sq_events[...] += 0`, `_lab_ok = all(True for _ in ())`,
   neither used). It is correctly tagged no-independent-information, but this is
   D72's own MODERATE 5 repeating.
4. **`linear_extensions` is required by the AST signature pass and never
   called** (receipt:336). Either use it (MAJOR 4) or drop it from `B1_REQ`.
5. **The title and §0 lead with "the census splits exactly in half".** The
   even split is an `AB4` coincidence; §3(d) says so ("strongly
   window-dependent: 44/88, 0/12, 604/960, 132/540, 218/334, 60/228") but only
   after the headline has landed. Move the hedge up.
6. **LOG #494 cites the 500 adversarial rationals as the evidence** that the
   i-twist is content-free. The conclusion is right; the cited evidence is the
   tautology of MAJOR 1. Cite the argument (`exp(i·)` turns any odd real into a
   conjugating unimodular), not the control.

---

## Checked and CLEAN

Everything below I recomputed from my own code and it reproduces exactly.

* **Every anchor.** `AB4`: 3,969 histories, 2,477 record classes, census
  `{both-blocked 142, closed 1546, AB-only 28, BA-only 12}`, ratios
  `{1: 1458, 1/2: 70, 2/3: 2, 3/2: 6, 2: 10}`, kinds
  `{(r,d): 68, (d,r): 8, (d,n): 6, (d,d): 4, (n,d): 2}`, half-open kinds
  `{(r,d): 12, (d,r): 4, (p,d): 16, (d,p): 8}`, shallowest defect at total
  depth 3, delivery-bearing 88/88. `ABC3`: 3,424 / 2,128 / 1,554 / `{1/2: 12}`
  / `{(r,d): 12}` / no half-open. The exit-1 anchor discipline is correctly
  scoped and was not reached.
* **The full C2 ladder, column for column** (`AB4`): classes
  `3969, 2477, 578, 125, 65, 113`; `μ` descent `3969/3969, 2477/2477, 514/578,
  84/125, 24/65, 44/113`; menu descent `3969, 2477, 492/578, 103/125, 29/65,
  113/113`; multi-valued labelled edges `0, 0, 8, 4, 0, 0`; squares closing
  `0, 473, 1546, 1546, 1458, 1402`; defective closing `0, 0, 88, 88, 44, 44`.
  The threshold verdict — coboundary at `[SEQ, REC]`, not at
  `[MULT, STATE, PORT, MENU]` — is correct, and the reading of *why* the record
  functor sits at the threshold (§3(c): the instrument is blind because it is
  fine enough to be flat) is the best sentence in the unit.
* **The carrier.** Menu quotient 113 classes; coarsest weighted congruence 185
  classes, fixed point after 5 refinement rounds; both close the **same** 44 of
  88. PORT closes exactly the same 44 as MENU — set equality, not merely equal
  counts, which is stronger than C2.4 claims.
* **The dichotomy survives every weakening of "descent" I could build.** Of the
  44 descent-obstruction squares at `AB4`: **0** have menus that agree on every
  commonly-admissible event (all 44 genuinely disagree on a shared event's
  weight, so even the weak labelled-edge notion is obstructed); **0** are
  identified by the normalised menu `q/M` (D65's own repair, the
  measure-twisted quotient); **0** have equal support; **0** have proportional
  menus (projective descent). The theorem is robust and is stronger than the
  unit argued — it does not depend on the strong descent notion it chose.
* **The group.** `{1/2, 2/3, 3/2, 2}`, prime content `{2,3}`, rank 2, the full
  3-smooth group. The Hermite/exponent-lattice computation is the right way to
  do it and B.3's refusal to license the basis-cycle count carries D72's lesson
  correctly. It does not move at four actors (see MODERATE 5).
* **The sign-definiteness self-correction (f).** Reproduced exactly:
  `AB4 {<1: 84}` with 4 unorientable; `(A,B) d ≤ 5 {<1: 868, >1: 8}` with 84
  unorientable; `(A,B) d ≤ 6 {<1: 7116, >1: 344}` with 1,076 unorientable. The
  headline is correctly withdrawn to the windows where it holds, the failing
  arms are named, and the depth-vs-symmetry attribution is right. This is the
  unit's best piece of self-discipline and it should be said plainly.
* **CTL-ORDER.** Reproduced: totals invariant, spectrum transposed
  `1/2 ↔ 2` and `2/3 ↔ 3/2`, half-open split `(28,12) → (12,28)`, unordered
  `{r, 1/r}` classes `{1: 1458, 1/2: 80, 2/3: 8}` both ways. The control is
  genuinely new and it does bite; my only complaint is that it was not turned
  on the unit's own output (MODERATE 2).
* **CTL-TAMPER** can fail and does move the census (88 → 94), unlike D72's
  T2.NC. **CTL-FLAT** and the determinism probe are sound.
* **A2.1 / the register profile**: every defective square register-overlapping
  on an actor register, `{actor: 88}` / `{actor: 12}`, all closed squares
  `{actor: 1073, DISJOINT: 473}`.
* **C1 / the D65 orthogonality.** The intermediate mass ratio is identically 1
  on the raw-defective squares (`{1: 88}`, `{1: 12}`), the normalisation defect
  is supported disjointly, and the three-actor mass set `{3, 7/2, 19/4}` with
  ratios `{6/7, 7/6}` is right.
* **Determinism and exit protocol.** Re-run at `PYTHONHASHSEED=7`: exit 0,
  41 PASS / 0 FAIL, 302 s, output identical to `data/d74_transport_holonomy_exact.out`
  apart from timings and the echoed seed. Substantive negatives exit 0; exit 1
  reserved for anchors; `ANCHOR_FAIL = 0`.
* **Scope discipline.** §4 claim 10 is well drawn and I have no complaint about
  TH-II's licence in the note itself: it does not infer any grammar-wide
  phase-existence result from this scope's emptiness, it explicitly refuses the
  v7 identification, refuses the measure, refuses infinite volume, and refuses
  the forest-dependent basis count. The enrichment-fork framing in LOG #494 is
  honest as a fork. Its "0-for-4 at the grammar's native addresses" tally is the
  one place where the scope discipline slips, because this address was scored by
  a predicate with no positive branch (MAJOR 2).

---

**Summary for the principal.** The unit's two structural theorems — the
removability threshold at `μ`-descent, and the curvature / descent-obstruction
dichotomy — are correct, reproduce exactly, and survived every attack I could
mount, including four different weakenings of "descent" and a new actor pool.
The group claim is confirmed and strengthened. What needs revision is the
evidential architecture around the **negative**: the odd-sector verdict rests on
a gate that cannot fail, was decided by a predicate with no positive branch,
mis-cites the carrier it claims to have emptied, and declares empty an even
channel in which the receipt's own arm had already computed a non-trivial
substrate-supplied invariant. None of that makes the odd sector non-empty in the
scalar sense — D2 settles that in one line, a priori — but the unit is not
currently entitled to the sentence it leads with.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-27)

All findings applied; receipt rerun 48 PASS / 0 FAIL (41 independent
after the honest corollary count; 311 s), every referee number
reproduced from an independent rebuild — with ONE correction to the
review itself (MAJOR 5's "3,391 labelled edges" is the receipt's
up-rank column; MULT carries 1,288 labelled edges on 3,968 up-moves;
the 8 is right; nothing depends on it; noted in the note §7).
**THE J INVARIANT GATED (D9.1, the round's find, credited): J = 1
=> r = 1 on all 8,600 closed squares across three arms, zero
exceptions; J = 0 on all 1,060 defective squares — the reversal-EVEN
channel exactly characterises the curvature's geography.**  The
honest carrier gated (0/304 reversed linear extensions admissible;
AND the grammar is NOT reversal-blocking — 2,196/3,092 closed-square
endpoints reverse fine: the inadmissibility is specific to defective
structure).  The outcome predicate rebuilt three-way (OUT.1
exercises all branches); the dichotomy carries its "descent"
qualifier everywhere with MULT-closes-88/88 and the four-weakenings
0/44 both gated; the four-pool group table stands (the (A,B,C,D)
pool gated: 1,728 defects, masses {4, 9/2}, same four values, no
new prime; 27,186 non-unit squares over 10 honestly-described
scopes).  **Verdict after repairs: TH-II WITH A FIND — the
curvature genuine, irremovable, <2,3> at four pools; the scalar
phase empty on the honest carrier; the even channel NOT silent (J).**
TERMINAL for round 1.
