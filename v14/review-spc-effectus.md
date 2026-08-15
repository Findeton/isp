# SPC (PAPER-37) — K2 EFFECTUS-LENS REVIEW

**Seat:** K2, effectus — verdicts, licensure, meaning.  **Posture:** hostile.
**Date:** 2026-08-15.  **Authority:** `HANDOFF-PROMPT.md` §4/§9; the frozen pin
`v14/note-spc-pin.md` (`7f0b1e9d5071`); the ACT adjudication
`v14/note-act-adjudication.md`; the AID adjudication
`v14/note-aid-adjudication.md`.  In-flight siblings were not read.

**Object, sha256-12 verified at open and re-verified at close:**

| object | sha256-12 | lines |
|---|---|---|
| `v14/paper-37-spc.md` | `1555d049d558` | 657 |
| `v14/code/spc_exact.py` | `6b399487f286` | 5316 |
| `v14/code/spc_output.txt` | `dc6410c72036` | 31 |
| `v14/code/spc_receipt.json` | `3958fe51495b` | 8581 |
| `v14/note-spc-pin.md` (the pin) | `7f0b1e9d5071` | 118 |

The unit's declared inheritance was verified independently: ACT
`d933221780ed`, AID `ecdd3fbf1d06`, OCC `0092caa4d9ad`, SMU `6df0db523d32` —
all four match the digests the paper prints at lines 16–24.

**Recomputations: 166.**  All arithmetic exact (integers and `Fraction`);
nothing imported from `spc_exact.py`; the nine-actor layer rebuilt from
partitions upward by a route the instrument does not use.

---

## 0. GRADE

# ACCEPT-WITH-FIXES

**Zero delivered computed numbers moved.**  I rebuilt the entire nine-actor
layer from scratch — the character table by permutation-character/Kostka
inversion (the instrument uses rim hooks), all thirty degrees, row
orthogonality at 900 of 900 pairs, all seven dominance counts, all thirty
Kostka numbers of the (3,3,3) branching table, all thirty Littlewood–Richardson
constituent counts, the actor row's hosting, its tensor square, its composite
rules and its statistics split — and every published number reproduced.  Every
column total in the paper reproduced from the paper's own tables: 220, 220,
246, 156, 90, 2154, 10/9, 192/14/9/31, 4-of-19, 9-of-19.  The
`hosted + homeless = irreps` identity holds at all nineteen rows; the four
statistics columns sum to each row's species count at all nineteen; the
closing rows are *exactly* the rows with no homeless species at 10 of 10.  The
head string is character-identical in paper, receipt and transcript.  The
census is real and the instrument is strong: the two-engine agreement, the
two-route orbit counts, the tableau third route, the four synthetic arenas
emitting four distinct heads, and the total falsifier registry are all genuine
and are better than what ACT delivered at the same station.

The defects are all mine to find: **referent binding, licensure, scope, and
one verdict-architecture failure that replays ACT's §2 ruling verbatim.**  None
of them is a false computed number.  Seven are MAJOR.

---

## 1. MAJOR-1 — THE HEAD'S FEASIBILITY IS ROW-LEVEL; ITS WORDS ARE ARENA-LEVEL. ALL FOUR WERE DETERMINED BEFORE THE RUN.

**This is ACT's §2 ruling replayed, and the paper contains both the claim and
its refutation.**

§1 (lines 93–98) says, in the paper's own voice:

> **Every pre-registered word could have come out otherwise here.** The pin's
> own engraving demands a feasibility line; here it is a measurement, because
> the arena carries rows on both sides of every question the head asks:
> 7 of the 8 outcome arms are live at this arena, each of them witnessed by a
> delivered row rather than by a control.

§9 (lines 557–560) says, in the same voice:

> **The carrier row list.** … Both arms of every outcome word are populated by
> delivered rows, so **adding a row cannot flip a word**, but it moves the
> numbers.

The second sentence is the first sentence's refutation, stated as a virtue.
An aggregate over nineteen rows with rows on both sides is not *live*; having
rows on both sides is precisely what **pins** it. The head's words aggregate
all nineteen rows (`head_law`, `spc_exact.py:3263–3266`:
`k = sum(r["hosted"] …)`, `n = sum(r["irreps"] …)`, `exits = [r for r in rows
if not r["selection_closes"]]`).  The witnesses in §1's table are *rows*.

**Establishing measurement.**  I rebuilt the nine-point permutation module of
the symmetric group on nine letters from the character table upward, with no
reference to the instrument, and confirmed that once `ACTOR-9-UNDER-S9` sits in
the declared row list **all four head words are determined before any code
runs**:

| head word | why it was pinned at declaration time | verified |
|---|---|---|
| `SPC-CARRIER-SELECTS-k-OF-n`, k<n | the module is trivial ⊕ standard: 2 hosted, 28 homeless | 2 of 30 |
| `SPC-SELECTION-OPEN` | standard ⊗ standard reaches four species, two of them unhosted | 4 constituents, mult 1 each, 2 unhosted |
| `SPC-STATISTICS-SPLITS` proper | the trivial species lies in the symmetric square and **not** in the antisymmetric one | split (1, 2, 1, 26) |
| `SPC-INVENTORY-…` | single-armed by construction — the pin says so, and §1's own table lists exactly one arm for it | 1 arm of 8 |

All four are classical facts about the symmetric group's natural permutation
module, computable at pin time from a textbook.  Nothing this arena could have
been is at issue: the row list *is* the arena, and the row list contains the
actor row.

**What is genuinely to the unit's credit, and what it does not buy.**  SPC's
four synthetic arenas do what ACT's Z1 repair was ordered to do: they run
foreign arenas through the *real* census functions and emit four distinct
heads — `SPC-CARRIER-SELECTS-3-OF-3`, `SPC-SELECTION-CLOSED-9-RULES`,
`SPC-SELECTION-OPEN`, and `SPC-BLOCKED-AT-THE-GROUP-CLOSURE` (I verified all
four control heads by hand from their stated constructions: a cyclic group of
order three acting regularly; the same acting trivially on two points, giving
1 of 3 hosted and the split 1|0|0|2; a cyclic group of order six with orbits of
size two and three, giving 4 of 6 hosted and an exiting composite; and a
non-closed set of permutations).  That establishes **machinery-level**
feasibility, and it is a real advance over ACT.  It does not establish
**arena-level** feasibility, and §1 explicitly claims the arena level and
explicitly disclaims the control route ("witnessed by a delivered row rather
than by a control").

**Ruling.**  The delivered words are all TRUE.  What is broken is the
architecture that made them the only utterable words, and the sentence that
denies it.  Per ACT §2, this is a repair, not a reject: the words stand, the
feasibility claim is re-levelled.

**LICENSED REPLACEMENT for §1's second paragraph (verbatim basis for the repair):**

> **What could have come out otherwise, and at which level.**  Two of the four
> head words are two-valued as words and two are parameterised counts; the
> pin's engraving is met at two levels and they must not be conflated.  At the
> ROW level this arena carries rows on both sides of every question the head
> asks, and the table below names the witnessing row for each arm.  At the
> ARENA level it does not: the head's words aggregate all nineteen rows, and
> once `ACTOR-9-UNDER-S9` was in the declared row list all four were
> determined before the run — its permutation module is the trivial species
> plus the standard one, so some species is homeless; the standard species
> composed with itself reaches two species the row does not host, so the
> selection exits; and the trivial species lies in the symmetric square and not
> in the antisymmetric one, so the statistics split properly.  What
> demonstrates that the census machinery can emit the other words is the
> control set and not this arena: four synthetic arenas through the same
> functions emit four distinct heads, including `SPC-CARRIER-SELECTS-3-OF-3`,
> `SPC-SELECTION-CLOSED-9-RULES` and the refusal.  Section nine's "adding a row
> cannot flip a word" is the same fact recorded as robustness.

**Head repair.**  `CONTROLS=…;7-OF-8-OUTCOME-ARMS-ARE-LIVE-AT-THIS-ARENA-EACH-WITNESSED-BY-A-DELIVERED-ROW`
→
`CONTROLS=4-SYNTHETIC-ARENAS-THROUGH-THE-SAME-CENSUS-FUNCTIONS-EMITTING-4-DISTINCT-HEADS-WHICH-IS-WHERE-THE-OTHER-WORDS-ARE-WITNESSED;7-OF-8-ARMS-ARE-WITNESSED-BY-A-DELIVERED-ROW-AT-THE-ROW-LEVEL;AT-THE-ARENA-LEVEL-ALL-4-WORDS-ARE-FORCED-BY-THE-DECLARED-ACTOR-ROW`.

---

## 2. MAJOR-2 (CRITICAL) — THE 246 REFERENT IS NEVER NAMED, AND 156 EXCEEDS THE SPECIES UNIVERSE IT APPEARS TO COUNT.

**What 246 is.**  `spc_exact.py:3264` and `:3292`: `n = sum(r["irreps"] for r
in rows)` over the nineteen carrier rows.  It is the **row-sum of per-row irrep
counts over nineteen (group, carrier) pairs** — species *slots*, not species.
Six of the eleven groups appear on more than one carrier and are counted once
per carrier:

| group repeated across rows | rows | species each | slots contributed |
|---|---|---|---|
| CHART-128 | 3 | 20 | 60 |
| CHART-32 | 3 | 14 | 42 |
| TORUS-TRANSLATIONS-16 | 2 | 16 | 32 |
| EXT-108 | 2 | 11 | 22 |
| TRANS-9 | 2 | 9 | 18 |
| CHART-18 | 2 | 9 | 18 |

**Where 246 appears.**  Three times in 657 lines, all three unnamed: twice in
the head (the second word `SPC-CARRIER-SELECTS-156-OF-246`, and the CARRIER
segment `156-OF-246-SPECIES-HOSTED`), and once in the body, line 253:

> 19 carrier rows over 7 declared carriers, and 156 of 246 species are hosted.

The word "slot" appears nowhere in the paper.  Nothing binds 246 to its
universe at any of its three uses.

**Why this is not a wording quibble — the arithmetic refutes the natural reading.**

| quantity | value | recomputed |
|---|---|---|
| species over the 22 inventory groups (head word 1) | 220 | ✓ from the §2 table |
| species-slots over the 19 carrier rows (head word 2's denominator) | 246 | ✓ from the §4 table |
| **distinct** species over the 11 groups that have a carrier row | **133** | ✓ |
| species of inventory groups with no carrier row (the seven identity-lattice groups) | 87 | ✓ 133 + 87 = 220 |
| slots that are duplicates of a species already counted | 113 | ✓ 246 − 133 |
| distinct species hosted on at least one of their own rows | **at most 90** | ✓ bound from the per-group maxima |

So the head's second word reads **156 of 246 species hosted** while there are
only **133** distinct species in play and at most **90** of them are hosted
anywhere.  A reader who takes the word at face value is handed a hosted count
that exceeds the entire species universe by twenty-three.  The paper's own §4
knows the right reading — "**Homelessness is a property of the pair and not of
the group**" (line 286) — and the head does not carry it.

**And the two head totals sit three tokens apart, both labelled SPECIES:**

```
SPC-INVENTORY-22-GROUPS-220-CLASSES-220-SPECIES--SPC-CARRIER-SELECTS-156-OF-246
```

220 is a sum over 22 groups counted once each.  246 is a sum over 19 pairings
of 11 groups counted up to three times each.  Neither universe is named; both
carry the word SPECIES; and the second is larger than the first, which invites
exactly the inference that the carrier census ranges over a *wider* inventory
than the group census, when it ranges over a *narrower* one (11 groups of 22,
133 species of 220).

**This is the AID §5 / LOR lesson exactly** — "every numeral true, the RELATION
false, and nothing binds two numerals of one sentence to one referent" — and
the AID adjudication ordered sentence-level referent binding as a *gate*.  SPC
inherits that order and does not discharge it at its own headline.

**The fourth head word carries the same unnamed denominator.**  I verified
192 + 14 + 9 + 31 = 246, and that the statistics table's `species` column is
the *irreps* column and not the *hosted* column at all nineteen rows.  So word
4 partitions the same 246 slots, and says so nowhere.

**LICENSED REPLACEMENT for line 253:**

> The census runs at 19 (group, carrier) rows over 7 declared carriers and over
> 11 of the 22 inventory groups; six of those eleven are censused on more than
> one carrier, so the nineteen rows offer **246 species-slots** — the row-sum of
> each row's own irrep count, a slot per (species, carrier) pairing and not a
> count of distinct species — and **156 of those slots are filled**.  Behind the
> 246 slots stand 133 distinct species; the remaining 87 species of the
> inventory belong to the seven identity-lattice groups, which have no carrier
> row here at all.  Because a species can be hosted on one carrier and homeless
> on another, the hosted slot count is not a species count and must not be read
> as one: at most 90 distinct species are hosted anywhere in this table.

**Head repairs (both occurrences):**

- word 2: `SPC-CARRIER-SELECTS-156-OF-246` → `SPC-CARRIER-SELECTS-156-OF-246-SPECIES-SLOTS`
- CARRIER segment: `156-OF-246-SPECIES-HOSTED` →
  `156-OF-246-SPECIES-SLOTS-HOSTED-OVER-19-GROUP-CARRIER-ROWS-AT-11-DISTINCT-GROUPS-AND-133-DISTINCT-SPECIES;THE-OTHER-87-INVENTORY-SPECIES-HAVE-NO-CARRIER-ROW`
- STATISTICS segment: `192-SPECIES-IN-BOTH-SHAPES,…` →
  `192-OF-THE-SAME-246-SLOTS-IN-BOTH-SHAPES,14-SYMMETRIC-ONLY,9-ANTISYMMETRIC-ONLY,31-IN-NEITHER`

**Gate leg to add:** the sentence-level referent binding AID ordered — every
sentence carrying two numerals must name one universe for both, and each of
220 / 246 / 133 / 87 must be located in the paper beside the noun that names
its list.

---

## 3. MAJOR-3 — THE STATISTICS DERIVATION IS TRANSPORTED OFF ITS PARENT'S GRAIN, AND ITS ZERO IS THE PARENT'S *VACUOUS* ZERO.

The head asserts:

```
STATISTICS=THE-SELECTED-SHAPE-IS-ANTISYMMETRIC-DERIVED-FROM-0-LEAK-CELLS-AGAINST-81
```

and §8 (lines 487–489):

> Which shape that selects is **derived** here from those two counts and not
> typed: the shape that leaks at 0 cells against 81 is the antisymmetric one.

**Three things OCC published about that 0, none of which SPC carries.**  I read
OCC's terminal at its declared digest `0092caa4d9ad`:

1. **The zero is vacuous, and OCC says so in its own body** (paper-31, lines
   305–309): "the wedge has no doubly occupied configuration to leak into at
   all — its forbidden set is empty, **which is why its 0 is a vacuous zero and
   is published as one**."  Its head publishes the same fact as a field:
   `CARRIER-GRAIN-ANTISYMMETRIC-FORBIDDEN-CONFIGURATIONS=0` and
   `WEDGE-FORBIDDEN-SET-EMPTY-IFF-THE-CARRIER-GRAIN=3-OF-3`.
2. **The selection holds at one grain only.**  OCC's head word is literally
   `OCC-POOL-AND-GRAIN<THESIS=EXCLUSION-SELECTS-ONLY-AT-THE-CARRIER-S-OWN-GRAIN`,
   and its body (line 331): "**At the actor's grain, both shapes leak, and
   neither is a law** … No shape closes, so nothing is selected," with
   `ACTOR-GRAIN-SHAPE-LEAK-SETS-COINCIDE=6-OF-6`.
3. **OCC's verdict on the shape is that it is a declaration** (line 91):
   "fermionic-shape is not a theorem of the coupled theory here — it is a
   **declaration**, made at a grain the committed dictionary names and never
   measures."

The words "vacuous" and "declaration"-in-that-sense appear nowhere in SPC
(grep: `declaration` occurs three times, all about the carrier row list, the
group inventory and the unsealed-key declaration).

**And the transport is measurable in SPC's own table.**  The parent's selection
grain is the 27-cell carrier.  SPC's statistics table at those rows:

| row (the parent's own selection grain) | species | both | sym only | anti only | neither |
|---|---|---|---|---|---|
| CELL-27-UNDER-TRANS-9 | 9 | 9 | 0 | 0 | 0 |
| CELL-27-UNDER-CHART-18 | 9 | 9 | 0 | 0 | 0 |
| CELL-27-UNDER-EXT-108 | 11 | 11 | 0 | 0 | 0 |

**At the only three rows sitting at the grain where the parent's selection
holds, the split is empty.**  Every one of the four splitting rows lies at a
grain the parent's selection does not reach: `SITE-16-UNDER-CHART-128` and
`PLAQUETTE-16-UNDER-CHART-128` (lattice carriers, not the identity arena at
all), `SITE-9-UNDER-EXT-108`, and `ACTOR-9-UNDER-S9`.

Yet §8 closes (lines 522–526):

> the sharpest instance is the actor row: **the trivial species is not
> compatible with the selected shape at the actor row** … The pin's question is
> answered in that one line, and **its scope is exactly the pair grain the
> parent's census selected at.**

The actor row is the actor grain.  The parent measured, in its own head and
body, that *nothing is selected there*.  The final clause asserts the exact
opposite of the parent's published scope.

**The underlying mathematics is correct and I verified it independently.**  For
the natural nine-point module M = trivial ⊕ standard: Sym²M = 2·trivial ⊕
2·standard ⊕ S^(7,2) and Λ²M = standard ⊕ S^(7,1,1).  So the trivial species is
in the symmetric square and not in the antisymmetric one; the split is
(1, 2, 1, 26); of the two hosted species only the standard survives into Λ².
Every number in that sentence is right.  What is unlicensed is calling Λ² "the
selected shape" *at that grain*, and then claiming the parent's selection scope
for it.

**LICENSED REPLACEMENT for §8's opening and closing (verbatim basis):**

> The occupancy terminal selected a shape, and it selected it under three
> conditions this unit must carry.  It selected at **its own carrier grain** and
> published its thesis as "exclusion selects only at the carrier's own grain";
> at the actor's grain it measured that both shapes leak at 6 of 6 coin classes
> and that their leak sets coincide, so nothing is selected there; and it
> published the antisymmetric shape's zero as a **vacuous** zero, since the
> wedge has no doubly occupied configuration to leak into and its forbidden set
> is empty.  Its own verdict on the shape at this arena is that it is a
> declaration and not a theorem.  Which shape the comparison names is derived
> here and not typed — 0 against 81 names the antisymmetric one — and it is
> derived from a comparison the parent scoped to one grain and one of whose two
> counts the parent published as vacuous.
>
> … [after the table] … At the three CELL-27 rows — the only rows at the grain
> where the parent's selection holds — the two squares carry the same species
> and the split is empty, so the selection costs no label where it was selected.
> All four splitting rows lie at grains the selection does not reach: two
> lattice rows under the chart group of order 128, the nine sites under the
> arena group, and the actor row.  At the actor row the trivial species lies in
> the symmetric square and not in the antisymmetric one, so of the two species
> that carrier hosts only one survives into the antisymmetric square.  That is a
> statement about the antisymmetric square at the actor grain.  It is **not** an
> application of the parent's selection there, and the parent measured that its
> selection does not reach that grain.

**Head repair:** `THE-SELECTED-SHAPE-IS-ANTISYMMETRIC-DERIVED-FROM-0-LEAK-CELLS-AGAINST-81`
→ `THE-SHAPE-THE-PARENTS-CARRIER-GRAIN-COMPARISON-NAMES-IS-ANTISYMMETRIC-DERIVED-FROM-0-LEAK-CELLS-AGAINST-81-WHERE-THE-0-IS-THE-PARENTS-VACUOUS-ZERO-AND-THE-PARENTS-SCOPE-IS-THE-CARRIER-GRAIN-ONLY-WHERE-THIS-UNITS-3-CELL-27-ROWS-DO-NOT-SPLIT-AT-ALL`.

**Gate leg to add:** an anchor on OCC's vacuity sentence and on its
actor-grain sentence, each bound to the §8 gate, so that a §8 that drops the
scope cannot pass.

---

## 4. MAJOR-4 — "THE PRICE IS ONE SPECIES" IS FORCED BY INDEX TWO; THE MEASURED CONTENT IS ELSEWHERE.

§5 (lines 306–313):

> There is exactly one species on which the odd twist acts by minus one while
> every twist the torus itself realises acts trivially, and **the price is one
> species**: it carries multiplicity 72 at the anchored reading and 40 at the
> extension, which is the drop in the trivial multiplicity between the arena's
> own gauge group and the acting group, and which is the parent's own count of
> identified orbit pairs at both readings.

**Every clause of that sentence is a theorem of index two.**  The instrument
builds `RESIDUAL-GAUGE-4 = ⟨tw[ctw[1]]⟩` and `ACTING-LINK-8 = ⟨tw[1]⟩`
(`spc_exact.py:2722–2731`), i.e. the subgroup generated by the square inside the
group generated by the element — index two by construction; likewise
`RESIDUAL-GAUGE-8 = ⟨tw[ctw[1]], sw⟩ ≤ GAMMA-16 = ⟨tw[1], sw⟩`.  For any
index-two pair H ≤ G and **any** finite G-set X:

- G/H has exactly one non-trivial character ε, so "exactly one species on which
  the odd twist acts by minus one while the subgroup acts trivially" is *the
  definition of ε*, not a discovery;
- Ind_H^G 1 = 1 ⊕ ε, so by Frobenius the H-orbit count minus the G-orbit count
  equals the multiplicity of ε in C[X];
- every G-orbit is one or two H-orbits, so the number of *merged pairs* equals
  the same drop.

All three coincide for every index-two pair and every carrier.  **Establishing
measurement:** I ran this on 300 random G-sets (random permutations of even
order, H = ⟨g²⟩, sizes 4–16) through an orbit counter and an ε-multiplicity
counter sharing no code: the identity held at 300 of 300.  The paper's own
numbers obey it: 208 − 136 = 72 and 120 − 80 = 40, and its table publishes
exactly those multiplicities.

**What is genuinely measured, and is the real result:**

1. **Which** character ε is — that the species on which the odd twist acts by
   minus one is the one whose kernel is the arena's own gauge group. That is a
   fact about this arena's twist structure and could have been otherwise.
2. That the parent's pinned observable has a **non-zero component in that one
   isotypic block and in no other** — verified in-run at
   `spc_exact.py:2989`, `nonzero_components == theone`, with the receipt's gate
   detail preserving the identity: "the species is [0] … its non-zero isotypic
   components are [0]".
3. 288 of 640 non-vanishing points, and 136 of 136 orbit sums zero.

Item 2 is the load-bearing one and it is *not* forced.  The paper's headline
spends its emphasis on the forced half.  §7 shows the unit knows how to do this
honestly — "the reason is arithmetic rather than deep: a complete hosted set
has nowhere to exit to" (lines 461–462) — and §5 does not.

**On "DERIVED from orthogonality" (§9 bullet, line 540: "the pinning follows
from orthogonality").**  The derivation is **valid and complete**, by two
independent routes, and I checked both: (i) an admissible weight system is
orbit-constant (the parent's quoted characterisation), the observable sums to
zero on every one of the 136 orbits, hence ⟨w, O⟩ = 0 for every admissible w;
(ii) w lies in the trivial isotypic block, O lies wholly in the ε block,
distinct isotypic blocks are orthogonal, hence the same.  **But the paper never
writes the value it reproduces.**  Line 327 stops at "so the expectation is a
single value."  ACT's pinned datum is `[0, 0]` against `[-2, 2]`
(paper-34 line 687, and its head "PINS-TO-THE-SINGLE-VALUE-[0,0]-AGAINST-[-2,2]").
A derivation claim whose conclusion is not stated cannot be checked against the
thing it claims to derive.

**LICENSED REPLACEMENT for §5's second and third paragraphs:**

> **That the discount is ONE label is forced; which label it is, is measured.**
> The arena's own gauge group has index two in the acting group at both
> readings — four inside eight anchored, eight inside sixteen at the extension —
> and for an index-two pair acting on any finite set three quantities coincide
> by theorem: the drop in the orbit count, the number of merged orbit pairs, and
> the multiplicity of the unique character trivial on the subgroup.  So 72 and
> 40 were going to agree with the parent's identified-pair counts whatever this
> arena had been.  What could have come out otherwise, and did not, is the
> identity of that character: it is the one on which the odd twist acts by minus
> one while every twist the torus realises acts trivially, and it carries
> multiplicity 72 anchored and 40 at the extension.
>
> **And the parent's one pinned observable lives in that same block, which is
> not forced by anything.**  Rebuilt here from its own definition, it is
> non-zero at 288 of the 640 coins, and — measured at the anchored reading — its
> component in every other species vanishes identically: the observable lies in
> that one isotypic block and in no other.  The parent's pinning follows, and
> reproduces the parent's own value: an admissible weight system is constant on
> the orbits, the observable's sum over each of the 136 orbits of the acting
> group is zero, so its expectation is **zero** for every admissible weight
> system — the parent's `[0, 0]` against the observable's own range `[-2, 2]`.
> The same conclusion follows from orthogonality alone, since an invariant
> vector lies in the trivial block and distinct isotypic blocks pair to zero.

**Head repair:** the PRICE segment gains `THE-ONE-SPECIES-IS-INDEX-2-FORCED-WHAT-IS-MEASURED-IS-WHICH-ONE`
and `LIES-IN-1-ISOTYPIC-COMPONENT` becomes
`LIES-IN-1-ISOTYPIC-COMPONENT-AT-THE-ANCHORED-READING-REPRODUCING-THE-PARENTS-[0,0]-AGAINST-[-2,2]`.

---

## 5. MAJOR-5 — "CRYSTALLIZATION RESTORES THE INVENTORY" IS DIRECTIONALLY WRONG, PROCESS-VOICED, AND HEAD-BORNE ON AN EXHIBITED CHOICE.

§6 (lines 364–372):

> The parent's crystallization profile is realised here by an exhibited flag of
> partitions of the nine actors, each step refining the one before, so the
> stabilizers are genuinely nested and the sequence is a restriction chain
> rather than six unrelated subgroups.  Along it the inventory runs from 4 … to
> 30 … Read in the direction the schedule runs, **crystallization does not
> destroy the inventory, it restores it**: the labels a history can carry are
> fewest at its first event and complete at the fifth …

The head hard-codes one direction:
`ALONG-THE-CRYSTALLIZATION-CHAIN-4,12,12,26,30,30-SO-CRYSTALLIZATION-RESTORES-THE-INVENTORY-AT-PREFIX-5`.

**Three defects, each measured.**

**(a) "Restores" presupposes a loss that never occurs.**  I verified the chain
is non-decreasing at every step: 4, 12, 12, 26, 30, 30.  Nothing is ever lost
along it.  The count starts at its minimum and rises to the full thirty.  To
*restore* is to return something taken away; along this chain nothing is ever
taken away.  The licensed verbs are *reaches*, *attains*, *completes*.

**(b) The paper simultaneously asserts the opposite direction.**  Line 359:
"**The inventory collapses as the stabilizer grows.**"  Both sentences are true
of the same six numbers read in opposite orders; the body discloses that the
direction is a *reading* ("Read in the direction the schedule runs"), and the
head does not.  A verdict block that hard-codes one of two admissible readings
of the same table is the ACT §5 falsifier-wording defect in miniature.

**(c) The chain is a stabilizer nesting, not a process, and AID's own
adjudication forbids the upgrade.**  I verified the chain's shapes refine at
every step (dominance falls: (6,3) ⊵ (3,3,3) ⊵ (3,3,3) ⊵ (2,2,2,1,1,1) ⊵ 1⁹ ⊵ 1⁹),
that the orders divide, and that each row's count equals #{λ ⊢ 9 : λ ⊵ μ} for
that row's shape.  The monotonicity is then a **theorem**: an invariant vector
for a larger stabilizer is an invariant vector for every smaller one.  Nothing
happens *to* the inventory; the count at each prefix is a function of that
prefix's stabilizer alone.  AID §3's ruling is directly in point — the
stabilizer is a function of the event SET, and AID's own "the sequence is what
a stabilizer acts on" was refused as a false proposition.  "The labels a history
**can carry** are fewest at its first event" is process voice over a
set-inclusion lattice.

**(d) The head carries six numbers from a choice the choice inventory marks
non-verdict-determining.**  §10's table declares
`| THE-CRYSTALLIZATION-FLAG | EXHIBITED | UNBOUNDED | 1 | no |` — one exhibit
from an unbounded family, verdict-determining **no**.  Yet 4, 12, 12, 26, 30, 30
sit inside the delivered verdict string.  Either the profile is invariant across
the flag family (in which case AID's fifteen-thousand-history census should be
inherited and cited, and the flag stops being a free choice), or the six numbers
are exhibit-relative and the head must stamp them.  As delivered the paper
claims both.

**LICENSED REPLACEMENT for §6's paragraph (verbatim basis):**

> The chain runs 4, 12, 12, 26, 30, 30, and the count never falls along it.  It
> never falls **by theorem**: the exhibited flag refines at every step, so the
> stabilizers are nested, and an invariant vector for a larger stabilizer is an
> invariant vector for every smaller one.  The chain is a nesting of subgroups
> indexed by prefix length, not a process in time — nothing is destroyed at the
> first prefix and nothing is returned at the fifth, and the count at each
> prefix is a function of that prefix's stabilizer alone.  Read from the largest
> measured stabilizer down to the trivial one the count rises to the full thirty
> and attains it at prefix five; read the other way, which is the reading
> section six's first table takes, it falls.  Both readings are of the same six
> numbers.  The flag is one exhibit from an unbounded family and the six counts
> move with it; what does not move is the theorem that they cannot fall.

**Head repair:** `…-SO-CRYSTALLIZATION-RESTORES-THE-INVENTORY-AT-PREFIX-5` →
`…-NON-DECREASING-BY-NESTING-AND-ATTAINING-THE-FULL-30-AT-PREFIX-5-AT-1-EXHIBITED-FLAG-OF-AN-UNBOUNDED-FAMILY`.

---

## 6. MAJOR-6 — "HOSTED" IS NEVER DEFINED IN THE PAPER'S OWN VOICE, AND NO WALL LEG STOPS THE UPGRADE TO REALIZED.

**The licensed meaning is right in the code.**  `spc_exact.py:1848`:
`row["hosted"] = sum(1 for m in mult if m > 0)` — multiplicity greater than zero
in the permutation module.  Exactly the permutation-module reading the brief
requires.

**The paper never says so.**  The word is introduced at line 73 ("a carrier
either hosts one or it does not") and used 20 times, including in the title and
in the head, with no definition anywhere.  I grepped for any sentence putting a
host-word within 120 characters of a multiplicity-word: **zero matches**.  The
nearest thing is §4's "the multiplicity of the *trivial* species is the orbit
count," which defines one multiplicity and not the predicate.

**And the word the pin bans is used in the module sense without a
disambiguation.**  "realization" / "realizes" / "realized" appear in nine
sentences.  Four are quotes (the pin's "NO carrier realization", the pin's
"carrier-realized species", ACT's "not realisable on this torus", and the wall
statement); two are scope declarations; but three are the paper's own prose in
the module sense: line 283 "28 have no **realization** there at all"; line 364
"the parent's crystallization profile is **realised** here"; line 536 "which of
them a carrier **realizes** is fixed by the carrier."  The root that carries
the corpus's banned meaning is doing the corpus's *licensed* meaning three
times, with only context to separate them.

**No wall leg covers it.**  I read both legs (`spc_exact.py:4055–4108`,
`:4348–4380`).  `WALL-DYNAMIC`'s sixteen banned forms are
mass/masses/massive/spectrum/spectra/spectral/energy/energies/hamiltonian/
lifetime/decay/decays/unstable/stability/eigenvalue/eigenvalues — **no
realization word of any spelling**.  The positive leg fires only on a sentence
carrying a species-word *and* an outside-register word
(particle/matter/the world/physical reality/the universe/fundamental/elementary).
So a planted sentence such as

> This species is realized on the coin carrier.

carries no banned token and no outside-register token, and **passes both legs**.
The wall's own falsifier `MUT-WALL-PARAPHRASE` plants "This species is the
elementary carrier of the world's own label," which dies on *elementary* and
*world* — it exercises the outside-register leg and not the realization gap.
The pin names the missing word explicitly ("no **realized**-particle claims"),
and the ban list omits it.

**LICENSED ADDITION at the head of §4 (verbatim basis):**

> A species is **hosted** on a carrier when it appears with non-zero
> multiplicity in that carrier's permutation module, and **homeless** when its
> multiplicity there is zero.  Both words are statements about the
> decomposition of a finite-dimensional module and about nothing else.  Neither
> asserts nor implies that any state exists, that anything occupies a carrier,
> or that any species is realized in any sense beyond appearing in a
> decomposition.  Which species are realized is the successor's question and
> waits on the potential unit's gate; where this paper writes "carrier
> realization" it means multiplicity greater than zero and it means nothing
> else.

**Instrument repairs (liftable):**

1. `WALL-DYNAMIC` gains `realized, realised, realizable, realisable,
   realization, realisation, occupied, occupancy, populated, exists as a state`,
   with the module-sense sentences added to `DECLARING` **by exact text** and
   each required to be located (the standing "an exemption carried and never
   used is a hole" rule applies to the new ones too).
2. The positive leg gains a second clause: any sentence carrying a species word
   *and* a realization word must be one of the wall statements, the new
   definition sentence, or a located declaring sentence.
3. A new mutant `MUT-HOSTED-IS-REALIZED` planting exactly
   "This species is realized on the coin carrier." must die at
   `G-MUST-NOT-VOCABULARY`.  As delivered it would not.

---

## 7. MAJOR-7 — THE CAP SCOPE-CLOSER DOES NOT CLOSE WHAT §2 CLAIMS IT CLOSES.

§2 (lines 189–198):

> At every one of the six (grain, reading) rows the subgroup of coin maps a
> uniform configuration can be moved by is the same group … it is closed, and
> the partition it induces on the carrier is exactly the partition the whole
> acting group induces there.  **That is why the species census on this carrier
> is complete at all six rows** although four of the six acting groups have no
> table here …

**What the measurement establishes.**  If the action of an acting group G on
COIN-640 factors through an image of order 8 or 16, then the permutation module
of G is the inflation of the image's module, and its irreducible constituents
are exactly the inflations of the image's constituents.  So the **hosted set**
is determined, and the orbit/class partition is determined.  Both are real, and
the measurement is a good one.

**What it does not establish, and what the head's own word needs.**  The
**denominator** is |Irr(G)|.  The four capped groups have no character table
here — the §2 table publishes `classes 0, species 0` for all four — so how many
species each carries, and therefore how many of them the carrier leaves
**homeless**, is not measured at all.  Word 2 of the head counts precisely
hosted-against-total.  "The species census is complete" is true of the hosted
half and undetermined of the homeless half.

**A second slip in the same sentence: the row universes differ.**  The "six
rows" are rows of the acting-group table (three grains × two readings).  The
carrier census has nineteen rows, of which four are on COIN-640, and only two
of those four use an acting group at all — `ACTING-LINK-8` and `GAMMA-16`, the
link grain's two readings.  The plaquette and site acting groups (1024, 4096,
8192, 32768) are **not carrier rows**.  So "the species census … is complete at
all six rows" asserts completeness at four rows where no species census was run.

§9's own bullet is nearly right and nearly vacuous: "so no carrier row is
affected; their abstract inventories remain open" (lines 553–556) — true,
because none of the four is a carrier row.  **The head is correct** — its SCOPE
segment says only "4-ACTING-GROUPS-STAND-ABOVE-IT-WITH-THEIR-ORDERS-RE-DERIVED-AND-THE-CARRIER-SEEING-THEM-THROUGH-A-GROUP-OF-ORDER-8-OR-16", which claims nothing about their species.  It is §2's prose that overreaches past its own head.

**LICENSED REPLACEMENT for §2's closing sentence:**

> What that measurement closes is the carrier's **orbit structure** and its
> **hosted set**: a permutation module that factors through an image of order
> eight or sixteen has exactly that image's constituents, inflated, so the
> hosted species at a capped row would be the hosted species at the
> corresponding uncapped one.  What it does not close is the **denominator**.
> The four acting groups above the cap carry no table here, so how many species
> each of them has — and therefore how many the carrier would leave homeless —
> is not measured, and none of the four appears among the nineteen carrier
> rows; the two acting groups that do appear are the two at the link grain.
> The cap is priced as a construction choice and its price is exactly this: an
> unmeasured denominator at four rows the census does not run.

---

## 8. MINORS

**m1 — the sealed-object count is stale and its gate is a tautology.**  §10:
"25 objects are sealed before the paper gates."  The receipt's
`ledger_shape.objects_sealed_before_the_paper_gates` is 25, but the delivered
`seal_manifest` contains **28** entries whose sealing gate precedes the first
paper gate (`G-MUST-NOT-VOCABULARY`, index 39 of 46 in the sealed ledger; total
manifest 34).  The value is snapshotted at `spc_exact.py:5097`
(`len(SEAL.man)` at the moment `ledger_shape` is built, before at least
`ledger_shape` itself is sealed), and the gate at `:5105` checks
`ls[…] == len(SEAL.man)` **at that same instant** — a tautology that cannot
detect the mismatch between the field's name and the property it asserts.
Repair: recount at the boundary (entries whose gate index is below the first
paper gate) and gate the recount, or rename the field to
`objects_sealed_when_the_ledger_shape_was_taken`.  The 39 / 7 / 1 / 2 gate
arithmetic is correct and reproduces the receipt's 46 and 49 exactly; only the
seal count is off.  I leave the exact insertion-order forensics to K3.

**m2 — the transcript under-reports the gate total by one.**  `spc_output.txt`
prints `GATES 46 (+2 closing)` = 48; the receipt's `totals.gates` is 49, the
extra being the receipt-wall gate, which the *paper* does disclose ("1
receipt-wall gate").  The transcript is the one artifact a reader meets first.
One-line repair.

**m3 — the head's order list is a set of 18 sitting next to the numeral 18.**
`22-GROUPS-AT-ORDERS-1,2,4,8,9,16,18,24,32,108,128,216,1024,4096,4320,8192,32768,362880-OF-WHICH-18-CARRY-A-FULL-EXACT-TABLE`.
I verified: 22 groups, **18 distinct order values** (4 appears twice, 8 three
times, 16 twice), and the list is that distinct set.  A reader who counts the
listed orders gets 18 and finds "18" asserted immediately after with a
different meaning.  Repair: `AT-18-DISTINCT-ORDERS-…`.

**m4 — one census gate is vacuous at 4 of 22 rows.**  §2: "the class count and
the species count agree group by group, which is itself one of the census
gates."  At the four capped rows both are 0, so the agreement is vacuous there.
Scope the sentence to the eighteen tabled rows.

**m5 — §9's arena contrast is refuted at two rows by the paper's own table.**
"**Exclusion is free on the gauge arena and costly on the identity arena**"
(line 544).  The nineteen rows partition 4 (COIN-640) + 8 (lattice: LINK-32,
SITE-16, PLAQUETTE-16) + 7 (identity: CELL-27, SITE-9, ACTOR-9), a partition the
paper never names.  Of the four splitting rows, **two are lattice rows**
(`SITE-16-UNDER-CHART-128`, `PLAQUETTE-16-UNDER-CHART-128`) and two are identity
rows; and 5 of the 7 identity rows do not split.  Licensed: "Exclusion costs no
label at any of the four coin rows or at any row under a chart or translation
group of order at most thirty-two; the four rows where the two squares carry
different species are the two lattice rows under the chart group of order 128,
the nine sites under the arena group, and the actor row."

**m6 — a theorem presented as a measurement.**  §9: "The identity lattice acts
on the inventory monotonically."  I verified the seven shapes form a **chain**
in dominance, so the counts 30, 29, 28, 26, 22, 12, 4 are non-increasing by
theorem (a K-invariant vector is H-invariant for H ≤ K).  What is measured is
the seven values, not the monotonicity.  One-clause repair.

**m7 — §7's closure correlation is arithmetic and the paper half-says so.**
"The rows that close are exactly the rows with no homeless species" — verified
at 10 of 10 and 9 of 9.  The forward direction is a triviality (a complete
hosted set has nowhere to exit to) and the paper says so; the converse
(homeless ⟹ some composite exits) is *not* a triviality and is the measured
half.  Say which half is which.

**m8 — the isotypic measurement is anchored-reading only.**  `spc_exact.py:2940`
computes `nonzero_components` against `ct8` = `COIN-640-UNDER-ACTING-LINK-8`
alone; the head's `LIES-IN-1-ISOTYPIC-COMPONENT` carries no reading stamp.
Either measure it at the extension too or stamp the reading (covered by the
MAJOR-4 head repair).

**m9 — the receipt seals the cardinality, the gate seals the identity.**
`odd_twist_species.its_non_vanishing_isotypic_components` is `1`; the identity
of that component survives only inside the gate's `detail` string ("its non-zero
isotypic components are [0]").  Since §5's whole headline is that it is *that*
species, promote the identity to a sealed structured field so a receipt-only
reconstruction can check it.

**m10 — the successor note claims an implication for a census not run.**  §9:
"which at the label level **implies** an exchange parity no single sector has …
and nothing here is claimed for it."  The two halves of that bullet disagree.
The wording is the pin's, so the pin owns it; the paper should carry it as
registered-not-derived: "…which the pin registers as implying an exchange
parity no single sector has; that census is not run here and this unit measures
nothing about it."

**m11 — the identification ban list has reachable gaps.**  `WALL-IDENTIFICATION`
bans seventeen forms but not *spin*, *charge*, *colour/color*, *generation*,
*chirality*, *antiparticle*.  Each is an outside-register word that could carry
an identification without tripping either leg.  Cheap to add.

---

## 9. WHAT I COULD NOT BREAK, AND SAY SO

These were attacked and held.  They are the unit's real strength and the panel
should not let the majors above obscure them.

- **The Standard-Model wall is clean, and cleaner than it had to be.**  I swept
  the paper's own characters for fifteen SM forms with the wall rows and the
  head removed: **zero hits**.  In particular *fermion* and *boson* appear
  **nowhere** — not even as shape words — although the entire §8 is about
  antisymmetric statistics and although OCC itself uses "fermionic-shape" and
  "bosonic-shape" as declared shape words.  The unit had a standing invitation
  to import them and refused it.  The ANALOGY licence appears exactly once, in
  the wall statement, registered and unused, and the paper draws no comparison
  anywhere.  **The SM wall passes.**
- **No SI number, no limit claim.**  Verified by my own sweep; every integer in
  the paper is a count, an order, a degree or a multiplicity.
- **The dynamic ban list finds nothing outside the declaring sentences.**  The
  only hits for mass / spectrum / stability are inside line 549–550, which is a
  declared exemption and is located.  The gap is the *realization* family
  (MAJOR-6), not the delivered text.
- **Every published table sum reproduces**: 220 / 220 / 246 / 156 / 90 / 2154 /
  10 / 9 / 192 / 14 / 9 / 31 / 4-of-19 / 9-of-19, plus the per-row identities
  `hosted + homeless = irreps` (19 of 19) and `both + sym + anti + neither =
  species` (19 of 19).
- **The nine-actor layer is exactly right at every entry I can reach**: 30
  partitions, 30 hook-length degrees summing in squares to 362880, row
  orthogonality at 900 of 900 pairs from an independently built table, the
  seven dominance counts 30/29/28/26/22/12/4 by two routes (dominance and
  character inner product), all 30 Kostka numbers of the (3,3,3) branching
  column, the degree-weighted sum 1680 = 9!/216, and all 30
  Littlewood–Richardson constituent counts for S₃×S₃×S₃.
- **The actor row is right in every cell**: hosted 2 of 30, orbits 1, composite
  rules 7, exits to 2, statistics (1, 2, 1, 26), and the tensor table's
  `[0,1,2,3]` with multiplicities `[1,1,1,1]`.
- **The four control arenas are real and their heads are right.**  I re-derived
  all four by hand from their stated constructions; all four heads reproduce,
  and they are distinct.  This is the ACT Z1 pattern executed properly and it is
  the reason MAJOR-1 is a re-levelling and not a kill.
- **The head is not stale.**  Character-identical across paper, receipt
  `verdict`, and the transcript's last line; the paper carries it exactly once.
- **Cap disclosure is present at every use of the capped groups' numbers** — in
  §2's table (engine `ABOVE-THE-TABLE-CAP`, classes and species 0), in the
  surrounding prose, in §9, and in the head's SCOPE segment.  MAJOR-7 is about
  what the closer *proves*, not about disclosure.

---

## 10. THE LICENSED SENTENCES, COLLECTED

For the repair worker, in one place.  Each is a verbatim basis, not a
paraphrase target.

1. **§1's feasibility paragraph** → the two-level replacement in §1 of this
   review (MAJOR-1).
2. **Line 253, the 246 sentence** → the species-slot replacement in §2 of this
   review (MAJOR-2), with the head's word 2, CARRIER segment and STATISTICS
   segment repaired as specified there.
3. **§8's opening and closing** → the three-condition replacement in §3 of this
   review (MAJOR-3).
4. **§5's second and third paragraphs** → the index-two replacement in §4 of
   this review (MAJOR-4).
5. **§6's crystallization paragraph** → the nesting replacement in §5 of this
   review (MAJOR-5).
6. **A new first paragraph of §4** → the hosted/homeless definition in §6 of
   this review (MAJOR-6).
7. **§2's cap-closer sentence** → the orbit-structure/denominator replacement in
   §7 of this review (MAJOR-7).

**Not licensed, and must not appear in the repair:**

- any sentence calling 246 a count of species, or placing 220 and 246 in one
  sentence without naming both universes;
- any sentence claiming a head word was live *at this arena*;
- any sentence applying "the selected shape" at the actor grain without the
  parent's grain restriction and its vacuity disclosure beside it;
- "crystallization restores the inventory", in any voice;
- any sentence saying a species is *realized*, *occupied* or *populated* on a
  carrier;
- any sentence claiming the species census is complete at the capped rows;
- any strengthening of the SEC×SPC successor note beyond registered-not-measured.

---

## 11. STANDING

Three recorded ownership notes for the adjudicator.

- **The pin is clean on the point ACT's pin was not.**  It carries a feasibility
  line per outcome word, as ACT §2 engraved.  MAJOR-1 is not a pin-design
  failure: the pin's feasibility lines are about the *machinery*, and the
  unit's controls discharge them.  What the pin did not require, and what the
  #299 engraving should now be extended to require, is that a compounded head
  whose words are **aggregates over a declared row list** must show feasibility
  **at the declared list**, not merely at some row of it.  I recommend that
  extension be engraved.
- **The pin's fifth measurement invited MAJOR-3.**  The pin says "OCC's ceiling
  selected exclusion at the carrier/pair grain — which species are compatible
  with the selected statistics at that grain."  "At that grain" is in the pin;
  the unit's census runs at every grain, and the pin gave it no instruction to
  carry OCC's vacuity and its actor-grain refutation forward.  The
  grain-transport was reachable at pin time.
- **Candidate until adjudication.**  Every verdict in this review is a candidate
  reading, including the grade.

---

## 12. CLOSE

**Recomputations: 166.**  140 machine checks in a scratch script written
against the paper's own tables and the two parents' published bytes, plus 26
hand recomputations (the symmetric- and antisymmetric-square decompositions of
the nine-point module; the composite-rule counts at `RESIDUAL-GAUGE-8` and
`GAMMA-16`; the identification of `CHART-18` and its 6/3 hosted split; the four
control arenas; the seal-manifest and gate arithmetic; six cross-reads of OCC's
head fields; four cross-reads of ACT's observable table and head segments).

**Zero delivered computed numbers moved.**  Ten script results initially
disagreed; all ten were my own script's column-index, sort-order and regex
faults, each resolved by hand against the paper, and none was a paper defect.

**Findings:** 7 MAJOR, 11 MINOR.  **Grade: ACCEPT-WITH-FIXES.**

**The five hashes, re-verified at close:**

```
1555d049d558  v14/paper-37-spc.md
6b399487f286  v14/code/spc_exact.py
dc6410c72036  v14/code/spc_output.txt
3958fe51495b  v14/code/spc_receipt.json
7f0b1e9d5071  v14/note-spc-pin.md
```

All five unchanged from open.  The object was not touched by this seat; this
review file is this seat's sole repo write.
