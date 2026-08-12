# FAC (paper-35) — K1 OPERATOR-LENS REVIEW

**Seat:** OPERATOR — rebuild the mathematics from scratch, sharing no code with
`v14/code/fac_exact.py`; every number wrong until re-derived.
**Object digests, verified at open AND at close (all five unchanged):**

| object | sha256-12 |
|---|---|
| `v14/paper-35-fac.md` | `2e9cbae8a83e` |
| `v14/code/fac_exact.py` | `53e1e2683937` |
| `v14/code/fac_output.txt` | `43212e390250` |
| `v14/code/fac_receipt.json` | `240bad74217a` |
| `v14/note-fac-pin.md` (pin) | `11380265fcf3` |

Parents read at their delivery digests: `paper-33-aid.md` `ecdd3fbf1d06`,
`paper-31-occ.md` `0092caa4d9ad`, `paper-20-coupling.md` `4824d190af73`,
`v14/code/coupling_exact.py` `72e7b299f66e`. The in-flight siblings (PER-R,
POT, SPC object files; the SEC reviews) were **not** read — `git status` shows
them dirty and they stayed closed. Git was read-only throughout; this file is
my sole repo write.

---

## GRADE: **AWF** (accept with fixes)

**Every published number in this unit is correct.** I rebuilt the arena, the
carrier, the three corpora, the four legs, the two closed-form theorems, the
carrier window, both censuses, the groupoid ladder, the grain triangle, the
persistence rows and every control arm from the definitions, with my own cell
indexing (unordered co-division pairs sorted by site index, not the
instrument's site-major `(x, l)`), my own partition enumerator, my own
translation-invariance predicate, my own Z[ω] arithmetic and my own dynamic
programme. **≈230 published quantities recomputed** — all 170 numeric cells of
the paper's seven tables plus ~60 substantive prose numerals — with **zero
disagreements on any published number**, including the extreme carrier
stabilizer order, which is exactly 27!. Both claimed theorems are theorems and
I re-proved both independently. The criterion digest `0019d84588bb` reproduces
from the committed source (10 functions, 107 lines).

The unit is nevertheless not terminal-ready. Three MAJORs, all in what the
paper *says* about the objects it measured rather than in the numbers:

- **M1** — the criterion carries an **undeclared and non-inert free item**: at
  the actor grain LEG-4 is evaluated on the *directionwise* image of the actor
  partition, never disclosed; on the *pairwise* image — the other member of the
  family the paper itself declares in §2, and the one the unit's own gated
  carrier typing certifies — the headline count and the named inventory both
  move.
- **M2** — §5 uses "local identifications" for two different objects, and the
  section's closing inference is **false of the object every number in §5 is
  about**.
- **M3** — §4, titled "Which leg binds, and which does not", **omits LEG-4**;
  measured, LEG-4 is non-binding at the actor grain over the whole corpus and
  binding at the carrier grain, so the leg-binding fact is itself stratified by
  grain — the unit's own headline shape — and goes unreported.

None of the three touches a computed number and none overturns the head word:
`FAC-STRATIFIED` and `FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN` survive every
probe I ran, including M1's alternative member. The repairs are prose plus one
added measurement column, which is why this is AWF and not REJECT.

---

## 1. WHAT I REBUILT, AND WHAT IT RETURNED

Eight independent programs, no line shared with the instrument. Interpreter
`/opt/homebrew/bin/python3.13`, integers and integer pairs over Z[ω] with
ω² = −1 − ω throughout; no float is constructed anywhere in my rebuild either.

### 1.1 The arena and the carrier (§1) — reproduced

| quantity | paper | my rebuild |
|---|---|---|
| sites / declared link directions | 9 / 3 of 4 | 9 / 3 of 4 |
| cells; cell ↔ co-division pair | 27 / bijection | 27 / bijection |
| two-actor cells; cells per actor | 27 of 27; 6 | 27 of 27; 6 |
| groupings into three triples | 280 | 280 |
| per-round incidence spectrum | — | 1@0, 27@4, 54@6, 162@7, 36@9 |
| saturating groupings | 36 | 36 |
| I7-STRICT ordered triples (R = 3) | 72 | 72 |
| G-FLAT ordered quadruples | 276 | 276 |
| driven window | 600 | 600 (256 CLASS + 264 FLAT + 80 SEEDFAN) |
| \|Aut(arena)\| | 108 | 108 (= 9 × 12; 108 distinct site perms, 108 cell perms) |
| corpus | 5,856 = 72 + 5,184 + 600 | 5,856; 5,784 distinct; events 9 / 12 / 18 |

The incidence spectrum is not in this paper but is paper-21's own published
row, and my constructor returns it entry for entry — which is the check that my
arena is the parents' arena and not a lookalike. `|Aut| = 108` is
independently forced: `|GL(2,3)| = 48`, the stabilizer of the declared
3-set of parallel classes inside PGL(2,3) ≅ S₄ is S₃, so 6 × 2 × 9 = 108.

### 1.2 The two closed-form theorems (§2) — both re-proved

**LEG-1 at the actor grain = the subgroup-coset partitions.** My proof: LEG-1
says the translation x ↦ x + l descends to the blocks for every declared l,
i.e. the equivalence relation is invariant under translation by ⟨L⟩. On the
regular Z₃² -set an invariant equivalence relation is exactly a group
congruence, so its blocks are the cosets of H = {x : x ~ 0}. Z₃² has six
subgroups (trivial, the four parallel classes, the whole group), giving six
coset partitions. Measured against a full enumeration of all 21,147 partitions
of the nine actors: **survivors 6, coset partitions 6, SET-equal True** — not
merely equal in count; I compared the partitions themselves.

The paper's §8 saturation claim falls out of the same proof and I confirm it by
running the parameterised predicate: **1 declared direction → 42 survivors, 2 →
6, 3 → 6, 4 → 6.** The leg saturates exactly when the declared directions
generate the translation group, as §8 says.

**LEG-2 = refinement of the participation-signature partition.** My proof: if
every event is a union of blocks then any two members of a block lie in exactly
the same events, so each block sits inside a signature class; conversely if
each block sits inside a signature class then for every event E and block B
either B ⊆ E or B ∩ E = ∅, so E is a union of blocks. Hence the count is
∏ Bell(|block|) over the signature blocks. Verified on the paper's own 76-history
sub-window by **three routes that agree at every history** — direct enumeration
over the 21,147 partitions, the ∏Bell closed form, and an explicit
refinement test: **0 mismatches**, with counts **1 at each of the 72 strict
triples and 125 at each of the four non-unique histories**, exactly as §4
reports. (125 = Bell(3)³ = 5³, the signature partition there being the three
lines of the repeated class.)

### 1.3 The carrier window (§2) — reproduced, and its decomposition named

My build: the directionwise image of every actor partition (**21,147 distinct**),
the pairwise image of every actor partition (**21,147 distinct**), union
**42,293** — the two families meet in exactly one partition, the discrete one —
then the 12 declared strata (which collapse to **9 distinct** partitions, the
shift-orbit stratum being the AG-line stratum and two others coinciding with
images already present), adding **2** new: **42,295**. Bell(27) =
545,717,047,936,059,989,389, reproduced by my own triangle. The shift is a
permutation of order 3; **LEG-1 at the carrier grain admits 10** of the window,
with block-count profile 1, 3, 6, 6, 9, 9, 9, 9, 9, 27.

### 1.4 The census (§3) — reproduced exactly, including the corpus indices

| | paper | my rebuild |
|---|---|---|
| actor cardinalities | 1 and 2 | 1 at 5,852; 2 at 4 |
| the four non-unique | the constant-class quadruples | corpus indices **5256, 5341, 5426, 5511** |
| inventories | {parallel class, discrete} | {ROW, DISCRETE}, {COL, DISCRETE}, {DIA, DISCRETE}, {ANT, DISCRETE} |
| carrier cardinalities | 1, 2, 3, 9 | 5,810 @1; 15 @2; 30 @3; 1 @9 |
| carrier unique / non-unique | 5,810 / 46 | 5,810 / 46 |
| cross-grain | subset True, equal False, 42 / 0 | subset True, equal False, 42 carrier-only, 0 actor-only |
| coin-order disagreements | 0 | 0 |

The four indices are the four constant-class quadruples in the window's own
enumeration order (W4-CLASS is `product(ROW, COL, DIA, ANT, repeat=4)` offset by
72 + 5,184), so 5256 = ROW⁴, 5341 = COL⁴, 5426 = DIA⁴, 5511 = ANT⁴. They are
also exactly the four histories whose global stabilizer is non-trivial (order
216 at all four) — the set-identity with AID's chart set holds element by
element.

**On the 11,799.** My per-distinct-history tally is 11,655; the difference is
the 72 duplicate corpus rows (5,856 − 5,784), each contributing one actor and
one carrier admissible. Per corpus row the total is
5,852·1 + 4·2 = 5,860 at the actor grain and
5,810·1 + 15·2 + 30·3 + 1·9 = 5,939 at the carrier grain, **= 11,799**, at each
coin order. Confirmed. See MINOR-6 for what that identity means.

### 1.5 The groupoid (§5) — every one of the eighteen rows reproduced

I built the arrow groupoid myself (objects = events; arrows = bijections of
footprints preserving, for every ordered internal pair, both "is a declared
cell" and the declared direction itself) and counted coherent families myself
(a family assigns each event a permutation of its own footprint; where two times
are related the two permutations agree on the intersection), by a sliding-window
dynamic programme for the window relations and by a **third** route for the
complete relation — counting maps f on the actors with f|F_t ∈ Sym(F_t) — that
shares nothing with either of the instrument's two.

| corpus | relation | distinct | minimum | maximum | mine = paper |
|---|---|---|---|---|---|
| C1 | R-ADJACENT | 1 | 124,416 | 124,416 | ✓ |
| C1 | R-COMPLETE | 1 | 1 | 1 | ✓ |
| C1 | R-EMPTY / R-ROUND | 1 | 10,077,696 | 10,077,696 | ✓ |
| C1 | R-WINDOW-2 | 2 | 144 | 288 | ✓ |
| C1 | R-WINDOW-3 | 1 | 4 | 4 | ✓ |
| C2 | R-ADJACENT | 3 | 859,963,392 | 15,479,341,056 | ✓ |
| C2 | R-COMPLETE | 1 | 1 | 1 | ✓ |
| C2 | R-EMPTY / R-ROUND | 1 | 101,559,956,668,416 | 101,559,956,668,416 | ✓ |
| C2 | R-WINDOW-2 | 13 | 144 | 41,472 | ✓ |
| C2 | R-WINDOW-3 | 2 | 4 | 8 | ✓ |
| C3 | R-ADJACENT | 7 | 1,492,992 | 2,176,782,336 | ✓ |
| C3 | R-COMPLETE | 2 | 1 | 216 | ✓ |
| C3 | R-EMPTY / R-ROUND | 1 | 2,176,782,336 | 2,176,782,336 | ✓ |
| C3 | R-WINDOW-2 | 22 | 144 | 2,176,782,336 | ✓ |
| C3 | R-WINDOW-3 | 9 | 2 | 216 | ✓ |

C2's three adjacent values are {859,963,392 · 1, 2, 18}. The R-ROUND explanation
is verified rather than accepted: **0 of the 672 sub-window histories has a
round-local pair whose footprints meet**, so the round relation is the free
product by construction. R-COMPLETE equals the global stabilizer at **5,856 of
5,856** (my third route). Trivial stabilizers **5,852**; **ATOM-BREAKS 5,852 of
5,852**; identity forced at the adjacent relation at **0**. The arrow groupoid
over the 672: **isotropy orders {1, 3, 6}**, occurring in 330 / 659 / 175
histories respectively, and **connected components 1–5**, distributed
16 / 132 / 230 / 24 / 270 — which matches the receipt's `arrow_profiles`
aggregate cell for cell.

### 1.6 The grain triangle (§6) — all eight rows, by my own routes

| corpus | RAW S₉ | RAW S₂₇ | REALIZABLE site | REALIZABLE carrier | n |
|---|---|---|---|---|---|
| C1 | 1 | 10,077,696 | 1 | 1 | 72 |
| C3 | 1 | 512 | 1 | 1 | 48 |
| C3 | 1 | 13,824 | 1 | 1 | 216 |
| C3 | 1 | 10,077,696 | 1 | 1 | 140 |
| C3 | 1 | 16,930,529,280 | 1 | 1 | 150 |
| C3 | 1 | 1,382,912,720,437,248,000 | 1 | 6 | 42 |
| C3 | 216 | 1,382,912,720,437,248,000 | 6 | 6 | 3 |
| C3 | 216 | 10,888,869,450,418,352,160,768,000,000 | 18 | 108 | 1 |

Agreement of the two tests: **actor 668 of 672, carrier 0 of 672**; raw carrier
non-trivial at **672 of 672**. I brute-forced the actor raw stabilizer by
explicit filtration of S₉ at **24** histories: **0 mismatches**.

For the carrier orders I used a route the instrument does not use: the
stabilizer of a family of subsets of a 27-set is the Young subgroup on the
**atoms of the Boolean algebra the footprints generate**, and I checked that the
atom sizes equal the signature-block sizes and that the product of factorials
equals the published order, at six orders including both extremes: block sizes
[27] → **27! = 10,888,869,450,418,352,160,768,000,000** (the ANT⁴ history, whose
events deposit no declared cell, so every cell carries the empty signature), and
[3,3,3,18] → 1,382,912,720,437,248,000, [3,3,3,3,3,3,9] → 16,930,529,280,
[3]×9 → 10,077,696, the 2- and 1-block profiles → 13,824 and 512. All six ✓.

### 1.7 Persistence and the rungs (§7) — reproduced

Thresholds, searched upward with no cap, taken against each history's own
stabilizer order: **C1 4 at all 72; C2 4 at all 5,184; C3 3 at 4, 4 at 521, 5 at
75** — i.e. the value set {3, 4, 5} with exactly the published distribution.
Rungs: R = 3 → 72/72 actor-unique, 72 breaks, w* = 4; R = 4 → **596** of 600
actor-unique, **554** carrier-unique, 596 breaks, w* ∈ {3,4,5}; R = 6 →
5,184/5,184, 5,184 breaks, w* = 4. The break coincides with actor-grain
uniqueness at every rung ✓.

### 1.8 The control arms (§8) — every row a genuine evaluation

| declared arena | histories | actor | carrier | head word (my head law) |
|---|---|---|---|---|
| CTRL-C1-THE-STRICT-TRIPLES | 72 | 0 | 0 | FAC-FACTORIZATION-FORCED |
| CTRL-THE-NON-UNIQUE-HISTORIES | 4 | 4 | 4 | FAC-FACTORIZATION-DECLARED |
| CTRL-C3-THE-DRIVEN-WINDOW | 600 | 4 | 46 | FAC-STRATIFIED |
| CTRL-THE-WHOLE-CORPUS | 5,856 | 4 | 46 | FAC-STRATIFIED |

| synthetic | events | record rows | LEG-3 passers | wedge | stab | adjacent | atom word |
|---|---|---|---|---|---|---|---|
| X1 | 1 | 2 | 1,015 | 0 | 4,320 | 6 | HOLDS |
| X2 | 3 | 1 | 21,147 | 0 | 216 | 216 | HOLDS |
| X3 | 12 | 3 | 125 | 4 | 216 | 216 | HOLDS |
| X4 | 7 | 4 | 104 | 0 | 1 | 1 | HOLDS |
| X5 | 6 | 1 | 21,147 | 0 | 1 | 5,184 | BREAKS |

Link arenas: 1 direction → 42, 2 → 6, 4 → 6. Wedge fires 4 on the control.
Every cell ✓. The control arm does what §8 claims: three distinct head words on
three declared arenas and both substantive atom words on declared data, and X4
is a genuine `HOLDS` (trivial stabilizer *and* a rigid adjacent groupoid).

---

## 2. MAJOR FINDINGS

### MAJOR-1 — LEG-4 carries an undeclared induced-carrier fiber, and it is NOT inert

**The defect.** LEG-4 is stated in §2 as "the coupled step is exactly LUMPABLE
for **the induced carrier partition**". At the carrier grain that is the
partition itself. At the actor grain "the induced carrier partition" is a
choice, and the paper *knows* it is a choice: §2 declares the carrier window as
"the **directionwise** image of every actor partition, the **pairwise** image of
every actor partition (a cell IS a pair, so the pair-image is the identification
the carrier's own typing suggests)". The criterion silently uses the
directionwise image. The paper never says so — `directionwise` and `pairwise`
appear in the paper only in that one window sentence, and never in §2's LEG
definitions, §3, §4 or §9. Worse, the *unchosen* member is the one the unit's
own gate certifies: `G-CELL-IS-A-CO-DIVISION-PAIR` establishes exactly that a
cell IS a co-division pair, and §1 draws the consequence "so a partition of the
cells IS a partition of the co-division pairs".

**The establishing measurement.** I ran the whole actor census twice, changing
nothing but the induced image:

| induced image | cardinalities | unique | non-unique | inventory at the non-unique |
|---|---|---|---|---|
| DIRECTIONWISE (the instrument's, undisclosed) | 1 @5,852; 2 @4 | **5,852** | **4** | ROW, COL, DIA, ANT — each with DISCRETE |
| PAIRWISE (the paper's own other declared member) | 1 @5,854; 2 @2 | **5,854** | **2** | ROW, COL only |

The mechanism is exact and I isolated it history by history: at histories 5426
(DIA⁴) and 5511 (ANT⁴) the class partition passes LEG-2 and LEG-3 under both
images, passes LEG-4 under the directionwise image, and **fails LEG-4 at both
declared coin orders** under the pairwise image. Corpus-wide, of the rows
admissible under one image and not the other, **the killing leg is LEG-4 in 2 of
2 cases; LEG-3 never differs.**

**What moves.** The verdict *word* does not: `FAC-STRATIFIED` under both members
(2 ≠ 46 as sets), and all three head words remain emittable on the declared
control arenas. What moves is:

- the verdict field `ACTOR-GRAIN-UNIQUE-FACTORIZATION=5,852-OF-5,856` → 5,854 of 5,856;
- the §3 sentence "the instrument names what: the **ROW, COL, DIA and ANT**
  parallel-class partitions, one each" — false under the other member, where
  DIA and ANT are inadmissible;
- the §7 rung row "At R = 4 the actor grain is unique at 596 of 600" → 598 of 600;
- the §4 sub-window, which is defined as the 72 strict triples *plus every
  history the census found non-unique*: 76 → 74.

**Why this is a MAJOR and not a taste question.** The unit's own discipline
forbids exactly this. §15 licenses a claim of significance only for quantities
gated invariant across declared free axes, else the quantity is arena-relative.
The unit demonstrates that it knows how to discharge such an axis — it runs
*both* coin orders because paper-20 declared that a fiber, and it publishes the
measured inertness (0 disagreements). Here an equally consequential axis of the
*same leg* is resolved silently, and unlike the coin order it is **not** inert.

**Repair (exact, liftable).** Publish the fiber. Add to §2's LEG-4 bullet and to
the verdict:

> *The actor grain's LEG-4 is evaluated on the DIRECTIONWISE image of the actor
> partition, `(x, l) ~ (y, l)` whenever `x ~ y`. The PAIRWISE image — the other
> member of the declared family, and the one the carrier's own typing suggests —
> is the second member of this fiber and is run entire: on it the actor-grain
> factorization is unique at 5,854 of 5,856 committed histories, the inventory
> at the two non-unique ones is the ROW and COL class partitions with the
> discrete one, and the DIA and ANT class partitions fail LEG-4 at both declared
> coin orders. The fiber is therefore NOT inert, and every actor-grain count in
> this unit carries the image it was taken at.*

and stamp the head field
`ACTOR-GRAIN-UNIQUE-FACTORIZATION=5,852-OF-5,856-AT-THE-DIRECTIONWISE-IMAGE`.
If the worker can *derive* the directionwise image as forced (it is the
functorial image under the `(site, link)` typing, which LEG-1-at-the-carrier
also uses), then say that in one sentence and gate it — but the derivation must
be published, because the unit's own gated typing points the other way.

### MAJOR-2 — §5 names two different objects "local identifications", and its closing inference is false of the counted one

**The defect.** §5 opens: "objects are the events, an arrow is a
**structure-preserving bijection** between two event footprints, and a global
object is a FAMILY of **local identifications** — one per event — subject to a
DECLARED COHERENCE RELATION". A reader takes "local identification" to be that
arrow. It is not. Every number in §5's eighteen-row table is a count of families
drawn from the **full symmetric group of each footprint**, without any
structure-preservation requirement. The proof is in the table itself:
R-EMPTY returns 10,077,696 = 6⁹ for C1 and 2,176,782,336 = 6¹² for C3 — six
choices at every event, always.

§5 then closes: "The groupoid itself is measured, not merely used: on the 672
histories of the declared sub-window its isotropy orders are 1, 3 and 6 and its
connected components run from 1 to 5, **so the local identifications genuinely
differ from event to event**." The "so" is false of the objects the ladder
counts: those number **six at every event of every history in the corpus**,
uniformly, which is precisely why the empty relation returns 6^T.

**The establishing measurement.** For the first C1 history the isotropy orders
of the arrow groupoid are 3 at all nine events, so a family space built from the
arrows would have 3⁹ = **19,683** members against the published 10,077,696; the
same at C3's first history and at ROW⁴, 3¹² = 531,441 against 2,176,782,336.
The two objects are not merely differently described, they are different sizes
at every history. And the substitution is not available as a repair: with
families drawn from the isotropy groups, R-COMPLETE would no longer return the
global stabilizer, which is the identification the whole atom argument rests on
— the stabilizer's restriction to an event is an *arbitrary* permutation of that
event, not a direction-preserving one.

**What survives.** Everything numeric. The arrow groupoid's own measurements
(isotropy {1,3,6} in 330/659/175 histories, components 1–5 in
16/132/230/24/270) reproduce exactly; the ladder reproduces exactly. What fails
is the sentence that welds them.

**Repair (exact, liftable).** Replace the closing paragraph of §5 with:

> *Two objects sit in this section and neither stands for the other. The
> coherence ladder's local identifications are the FULL symmetric groups of the
> event footprints — six at every event of every history, which is why the empty
> relation returns 6^T exactly. The ARROW GROUPOID, whose arrows preserve the
> events' internal declared cell directions, is measured separately and is not
> what any ladder row counts: on the 672 histories of the declared sub-window
> its isotropy orders are 1, 3 and 6 and its connected components run from 1 to
> 5. Restricting the families to the arrows would be a different census, and it
> would not return the global stabilizer at the complete relation.*

and delete "so the local identifications genuinely differ from event to event".

### MAJOR-3 — §4 separates three legs of four; the fourth is non-binding at one grain and binding at the other, and neither fact is published

**The defect.** §4 is titled "Which leg binds, and which does not" and reports
LEG-1, LEG-2 and LEG-3. LEG-4 is absent from the section, from the receipt's
`binding_legs`, and from its `non_binding_legs`. §4 concludes "the binding here
is done by geometry and history", and §4's own declared rule — carried into the
gate statement — is "A leg that never fails on a corpus is declared non-binding
ON THAT CORPUS and is exercised on the control arm instead."

**The establishing measurement**, over all 5,856 histories and both grains,
counting rows where the earlier legs pass and the named leg kills:

| grain | rows where LEG-1,2,3 pass and LEG-4 kills | rows where LEG-1,2 pass and LEG-3 kills |
|---|---|---|
| ACTOR | **0** | **0** |
| CARRIER | **306** | **0** |

and the decisive form of the same fact — the census run with LEG-4 deleted:

| grain | cardinality profile WITH LEG-4 | WITHOUT LEG-4 |
|---|---|---|
| ACTOR | 1 @5,852; 2 @4 | **identical**: 1 @5,852; 2 @4 |
| CARRIER | 1 @5,810; 2 @15; 3 @30; 9 @1 | 1 @**5,478**; 2 @332; 3 @15; 4 @30; 10 @1 |

So: **the actor-grain headline 5,852 of 5,856 is produced by LEG-1 and LEG-2
alone.** Neither the record leg nor the dynamics leg removes a single partition
from the actor census at any committed history. By §4's own rule LEG-4 owed the
non-binding declaration at the actor grain and did not get it. At the carrier
grain LEG-4 *is* binding and does substantial work (306 rows; 5,810 → 5,478
unique when removed) — so the true statement about which legs bind is itself
**stratified by grain**, which is this unit's own headline shape and is exactly
the kind of thing it elsewhere insists on measuring rather than assuming.

The omission matters because of what the paper does publish in LEG-4's place:
"11,799 passes under each" and "0 disagreements". A reader takes those as
evidence the dynamics leg was exercised and found consistent. It was run, and
the counts are right — but see MINOR-6: 11,799 is by construction the admissible
total, so it cannot tell a reader whether LEG-4 ever failed, and at the grain
carrying the headline it never did.

**Repair (exact, liftable).** Extend §4's leg sweep to all four legs at both
grains, and add:

> *LEG-4 is reported at both grains because it does not behave the same way at
> the two. On the committed corpus it removes no partition that LEG-1 and LEG-2
> admit at the actor grain — the actor-grain cardinality profile is unchanged
> when it is deleted — so at the actor grain the dynamics leg is NON-BINDING on
> this corpus, as the record leg is, and the actor-grain census is carried by
> geometry and history alone. At the carrier grain it binds: it removes 306
> partition-history rows the other three legs admit, and deleting it moves the
> carrier census from 5,810 unique of 5,856 to 5,478. Which leg binds is
> therefore itself grain-dependent.*

and add `LEG-4-DYNAMICS` to the receipt's `non_binding_legs` **with its grain**,
and to `binding_legs` with its grain.

---

## 3. MINOR FINDINGS

**MINOR-1 — the implemented LEG-4 predicate is strictly finer than the stated
one.** §2 says "for any two cells of a block the sums of the column's entries
falling into each block agree, exactly, in Z[ω] — the standard quotient
criterion". The code compares, for each column, the map
(target block, ω-exponent) ↦ integer coefficient — i.e. *before* summing over
exponents. Because 1 + ω + ω² = 0, these are not the same predicate in general:
the keyed version distinguishes profiles the Z[ω] sums identify. I implemented
both and compared them on **every** LEG-4 evaluation of the corpus
(5,784 distinct histories × 16 partitions × 2 coin orders): **0 disagreements**.
At G·D they are provably equivalent — all three entries of a column share one
exponent, so ω^e·S = ω^{e′}·S′ with e ≠ e′ forces S = S′ = 0, which the keyed
version also reports as equal after its zero filter. *Repair:* state the
implemented predicate ("the per-exponent integer tallies of the column's entries
falling into each block") or sum before comparing; either way say that the two
were measured to coincide here.

**MINOR-2 — the corpus value of the record-versus-dynamics wedge is TYPED, not
computed.** `fac_exact.py` writes
`"record_dynamics_wedge_on_the_committed_corpus": 0` as a literal; only the
control value (4) is measured. §4's "That wedge is empty on the committed
corpus" therefore rests on a typed constant, against the era's *counts computed,
never typed* rule. I measured it: at the actor grain it **is 0** over all 5,856
histories, and it is forced — the record is site-constant everywhere, so
`leg3_actor` passes for all 21,147 partitions and the wedge cannot fire.
*Repair:* compute it in the same loop that computes the control value.

**MINOR-3 — the wedge sentence is not grain-qualified.** At the carrier grain
the same quantity (LEG-4 passes, LEG-3 fails) fires **44** times over the 5,784
distinct histories. It changes no verdict — carrier rows where LEG-1 and LEG-2
pass and LEG-3 fails number 0, so all 44 sit on rows the history leg already
removes — but in a unit whose head word is `FAC-STRATIFIED` an unqualified "that
wedge is empty on the committed corpus" reads across both grains and is false at
one of them. *Repair:* "empty at the actor grain on the committed corpus; at the
carrier grain it fires 44 times, on rows the history leg already removes, so it
moves no admissibility verdict."

**MINOR-4 — "measurement rather than definition" overstates the R-COMPLETE
row.** §5: "the complete coherence relation returns the global stabilizer at
5,856 of 5,856 histories — counted by a backtracking enumeration that shares no
code with the sliding-window dynamic programme, so the identification is a
measurement rather than a definition." It is a definition-level identity, and a
short one: a pairwise-coherent family determines a single map f on the actors
with f|F_t ∈ Sym(F_t) for every t, and conversely; since each round partitions
the nine actors the events cover, so f is a bijection permuting every event
setwise — i.e. a stabilizer element. The equality cannot fail on any history of
this corpus, so the 5,856-of-5,856 tests the two implementations, not the
corpus. (I re-derived |Γ_complete| by exactly that actor-map route — a third
independent route — and got 0 mismatches at 5,856, which is the same
non-information.) The neighbouring R-ROUND explanation has the same character:
"within a round the three division events are pairwise DISJOINT" is forced by
`G-CORPORA-SHAPE`, which requires each round to partition the nine actors. Both
readings are true; both are theorems of the construction. *Repair:* state the
gluing identity as the theorem it is and keep the two-route agreement as what it
actually is — a code check.

**MINOR-5 — three of the five `HOLDS` rows in §8's synthetic table are
vacuous.** X1, X2 and X3 have global stabilizers 4,320, 216 and 216. The atom
question — does a *trivial-stabilizer* history stay rigid at a weaker coherence
— is not posed at any of them, and `atom_law` returns `HOLDS` because `breaks`
is 0 for want of a candidate, not because rigidity was found. The paper does
name X4 as "the decisive one", which mostly discharges this; the table alone
does not. *Repair:* flag the column, e.g. `HOLDS (vacuous — stabilizer
nontrivial)` for X1–X3 and `HOLDS (decisive)` for X4.

**MINOR-6 — the published LEG-4 pass count carries no information about
LEG-4.** Because the criterion short-circuits (LEG-4 is evaluated only on rows
that already pass LEG-1, LEG-2 and LEG-3), "11,799 passes under each" is
identically the admissible total, 5,860 + 5,939. It is correct and I reproduce
it, but it cannot distinguish a leg that never fails from one that fails often,
which is why MAJOR-3's measurement was needed. *Repair:* publish the LEG-4
evaluation count alongside the pass count, and the failure count per grain.

**MINOR-7 — the carrier headline's window-sensitivity is measurable and
unmeasured.** The unit is scrupulous that 42,295 is a declared window, but it
never prices what the window does. I did, running the carrier census on each
declared sub-family:

| declared sub-window | size | LEG-1 survivors | carrier cardinalities |
|---|---|---|---|
| the 12 strata (9 distinct) | 9 | 8 | 1 @5,810; 2 @45; 7 @1 |
| directionwise images only | 21,147 | 6 | 1 @5,810; 2 @45; 6 @1 |
| pairwise images only | 21,147 | 4 | 1 @5,825; 2 @30; 4 @1 |
| the declared window | 42,295 | 10 | 1 @5,810; 2 @15; 3 @30; 9 @1 |

This is **good news for the paper** and is worth publishing: 5,810 is returned
by three of the four sub-windows, so the headline count is far more robust than
the window's declared status alone would license. The *cardinality profile*
[1,2,3,9] is window-specific and should be stamped as such.

---

## 4. WHAT I ATTACKED AND COULD NOT BREAK

Recorded because a hostile seat's failures are evidence too.

- **The four corpus indices.** 5256 / 5341 / 5426 / 5511 are ROW⁴ / COL⁴ / DIA⁴ /
  ANT⁴ in my independently-built window, and they are simultaneously the only
  non-trivial-stabilizer histories (order 216 each), the only actor-grain
  non-unique histories, and a subset of the carrier's 46. Four independent
  characterisations, one set.
- **The thesis field.** "THE-LAW-ADMITS-MORE-THAN-ONE-FACTORIZATION-ONLY-WHERE-
  THE-HISTORY-REPEATS-A-PARALLEL-CLASS" is a one-way conditional and survives
  MAJOR-1's alternative member (the two survivors there are still
  class-repeating). §3's stronger four-name sentence does not.
- **The extreme carrier order.** 10,888,869,450,418,352,160,768,000,000 is
  exactly 27!, reached at ANT⁴ where no event deposits a declared cell, so every
  cell shares the empty footprint signature. The paper's reading of that row —
  "a statement about the size of S₂₇ as much as about the law" — is if anything
  understated: at that history the carrier stabilizer is the whole of S₂₇.
- **Both closed forms.** Re-proved from scratch and confirmed as *theorems*, not
  fitted formulas; the LEG-1 set-equality is a set equality in my build too.
- **The coin-order fiber.** 0 disagreements at every one of my ~92,500 LEG-4
  evaluations, in both the keyed and the true-Z[ω] predicates.
- **The criterion's freeze.** `combined digest 0019d84588bb` reproduces from the
  committed source by an AST walk I wrote myself; 10 functions, 107 lines; the
  free-name extraction returns no census product.
- **The falsifier accounting.** "34 ... the remaining 9" appears to contradict
  the 39 gates in the transcript and receipt; it does not. Four gates
  (`G-ARTIFACT-INTEGRITY`, `G-GATE-ACCOUNTING`, `G-SEAL-TOTALITY`,
  `G-TRANSCRIPT-SEALED-WHOLE`) are raised on the write path after the receipt is
  assembled; 31 + 8 = 39 in the receipt, +4 = 43 = 34 + 9. Clean, and disclosed
  in the receipt's reachability ledger.
- **Instrument-side counts I could check from the artifacts:** 39 gates all
  passed with 0 waivers; 13 anchors; 6 windows; 5 walls carrying 3+3+2+4+3 = 15
  needles, all clean; 36 falsifiers; 39 seals; 18 referent universes with 5
  relations checked and 0 unbound; 5 polarity axes with 0 inverted forms; 10
  paper claims; 7 tables / 42 rows; 38 class-word rows with 0 mismatches; 6
  ratios all windowed and stamped COUNTING-ONLY; 403 numerals and 97 spelled,
  0 exemptions.
- **Walls.** I read the paper against the AID not-licensed list myself. §9's
  disclaimers hold; I found no sentence assigning identity to one kind of thing
  and chart to another, and no unscoped reality slogan. §7's "thread-hood ... is
  a declaration, and this corpus prices it at three to five events of coherence"
  is the sharpest sentence in the unit and it stays inside the measured rows.

**Out of my scope by the read discipline:** §7's "PER-R places its own successor
at R = 8". PER-R's object files are in flight and I did not open them; that
clause is unverified here by declaration, not by failure.

---

## 5. RECOMPUTATION COUNT AND METHOD

**≈230 published quantities recomputed from scratch**: all 170 numeric cells of
the seven tables (§2 4, §3 6, §5 72, §6 40, §8 12 + 30 + 6) plus ~60 substantive
prose numerals, across **eight independent programs** in the session scratchpad
(`arena.py`, `corpora.py`, `census.py`, `groupoid.py`, `run1`–`run8`). No line,
literal, or intermediate product was taken from `fac_exact.py`; my cell indexing,
partition enumerator, shift construction, coherence dynamic programme and
complete-relation counter are all different objects from the instrument's.
Beyond the paper's own numbers I took **12 probe measurements** that the unit
does not publish (the pairwise-image census; the leg-binding split per grain;
the LEG-4-deleted censuses; the keyed-vs-Z[ω] predicate comparison; the
carrier-grain wedge; the four sub-window carrier censuses; the isotropy-product
contrast; the round-local overlap check), and it is those that produced the
three MAJORs.

**Disagreements with the paper on any published number: zero.**

---

## 6. VERDICT

`FAC-STRATIFIED` and `FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN` are, on my
independent rebuild, the words this corpus returns, and every count behind them
is right. The unit's mathematics is sound and its two theorems are theorems.
What it has not yet done is tell the reader (i) that its actor-grain headline is
taken at one of two declared induced images and moves to 5,854 with a different
inventory at the other, (ii) that the object its groupoid ladder counts is not
the groupoid its §5 defines, and (iii) that the leg it spends the most machinery
on removes nothing at the grain that carries the headline. All three are
repairable without touching a number.

**GRADE: AWF.** Candidate reading until adjudication.
