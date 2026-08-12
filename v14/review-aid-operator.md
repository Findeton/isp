# AID (paper-33) — OPERATOR-LENS HOSTILE REVIEW (K1)

**Seat:** K1 OPERATOR, panel protocol ledger v14 #285.
**Object under test, at commit `9f14488`, sha256-12 verified at START and at
END of this review, unchanged, and identical in the worktree and in the
commit:** `v14/paper-33-aid.md` `507da54ae871` / `v14/code/aid_exact.py`
`edf3a540cd57` / `v14/code/aid_output.txt` `48fe931bfcdc` /
`v14/code/aid_receipt.json` `cd938d7ae9be`; pin `v14/note-aid-pin.md`
`294ffe6c9deb`.
**Parents read at their committed bytes, hashes verified against the object's
own pin declaration (13 of 13 digests recomputed from the bytes, 0
mismatches):** paper-19 `50bb81e67942` (receipt `dfea664f2408`), paper-21
`ef4a8c35a0c4` (code `1958a8cdfe28`, receipt `a4538c7019e6`), paper-20
`4824d190af73` (code `72e7b299f66e`, receipt `55273f6b6068`); the v10 layers
d42b1 `576275d55ecf`, d60 `684cdb76552b`, d66 `3d0516ab106e`.

**Method.** Every decisive target was rebuilt from nothing, in my own files,
with my own data layout (sites as integers `0..8`, partitions enumerated by a
different recursion, `int` arithmetic only). `aid_exact.py` was **never used
as an oracle for a number**; it was read to learn which objects the claims
quantify over and to locate the two invariance predicates. Specifically:

- **Route A was rebuilt differently from the delivered Route A.** The
  delivered route filters the *parent prefix's* group by the last event. Mine
  computes, for each of the 84 possible three-actor events, `Stab(E)` by an
  explicit filter of all 362,880 elements of S₉, and then intersects. The two
  share no code path.
- **The driven leg was re-driven from the v10 layers themselves**, not from
  the delivered driver: d42b1's module slice cut at its own banner, d60's and
  d66's definitions by my own AST extraction, and a drive loop written from
  d66's `conflict_grid` / `conflict_pair_group` source. It calls d66's own
  `conflict_pair_group` and d60's own `dl`; no admissibility rule is
  re-implemented anywhere in my rebuild.
- **The walk was re-implemented over Z[ω] from paper-20's committed
  `coin_apply` / `walk_step`** (order `GD`, orientation `PLUS`, `GROVER_Z`),
  read from `coupling_exact.py`, not from the delivered re-implementation.

Interpreter `/opt/homebrew/bin/python3.13`. Scratch off-tree. Read-only git.

---

## VERDICT

**GRADE: AWF (ACCEPT WITH FIXES).**

Every measured number in the object reproduces exactly. **Zero false
numbers.** Of the **136 independent recomputations** below, every published
numeral that bears on a measurement was re-derived from scratch and agreed —
including the full 23-entry cycle-type census (sum 121,152), the twelve-row
stabilizer/automorphism index table, the five-deep Born-menu vector and both
E-24 fraction pairs. My rebuild threw two mismatches during the run; **both
were my own bugs** (a memo keyed on `frozenset(H)`, which silently drops
repeated events in the constant-class histories, corrupting my `Aut` table and
my depth-one residue law). Once the key was corrected to the event multiset,
both agreed with the object at every row.

The verdict segments stand **unmoved in their numbers**. One **MAJOR** stands
against the *attribution* in segment 4 and against a false sentence in §3: the
stabilizer is provably blind to the event ORDER, so nothing in this unit is
"what the sequence remembers". Five MINORs follow. No repair moves a number.

**Recomputations: 136.**
Substrate 14; corpora and prefix census 12; stabilizer census 24 (incl. the
23-entry cycle-type census as one); crystallization 15; driven leg 10;
invariance census 38; E-24 measures 7; parent back-validation 9; paper
instrument 7; two out-of-harness mutants and the order-blindness probes 6.
Numeral sweep: 566 tokens / 89 distinct literals, all backed.

---

## 1. Target-by-target

| # | decisive target | verdict |
|---|---|---|
| 1 | **the Young-subgroup theorem (the spine)** | **PROVED + REPRODUCED**; both route-agreement claims hold at my own Route A |
| 2 | the stabilizer census, order histogram, 23 cycle types | **REPRODUCED**, every row |
| 3 | **the crystallization constant 5** and C3's stratification | **REPRODUCED**, and **stronger than published** (see M-2) |
| 4 | **the invariance split** (weld-blindness theorem; record; walk) | **REPRODUCED**, every row; theorem verified at all 12 parses |
| 5 | relation-forgets-sequence: the 24; \|Aut\|=362,880 vs trivial; 1,296-vs-1 | **NUMBERS REPRODUCED**; attribution **MAJOR-1** |
| 6 | two mutants outside the harness; the numeral sweep | **both land**; sweep clean |
| 7 | the driven leg (17 schedules, maxhits, the refusal) | **REPRODUCED** by my own driver over the v10 layers |

---

## 2. The Young-subgroup theorem — the spine

### 2.1 The proof, checked as a proof

The paper's §4 argument is **sound and complete**. I re-derived it
independently and then checked the paper's own wording clause by clause:

- σ fixes every event setwise ⟹ σ fixes every complement setwise ⟹ σ fixes
  every atom of the generated Boolean algebra setwise (an atom is a finite
  intersection of events and complements). ✔
- Conversely every event is a union of atoms, so fixing every atom setwise
  fixes every event setwise. ✔
- The nonempty atoms are exactly the participation-signature blocks (including
  the all-zero block). ✔
- {σ : σ fixes each block setwise} is by definition the Young subgroup, order
  = ∏ |bᵢ|!, trivial iff every actor has its own signature. ✔

**No gap.** The shorter route (x and σ(x) share a signature ⟺ σ(E)=E for all
E) gives the same group; I used it as the independent check.

### 2.2 The two agreement claims, at my own Route A

| claim | published | K1 |
|---|---|---|
| distinct prefixes over the four corpora | 41,347 | **41,347** |
| order mismatches, Route A vs Route B | 0 | **0 / 41,347** |
| element-set comparisons (nontrivial) | 703 | **703** |
| element-set mismatches | 0 | **0** |

My Route A is the per-event S₉ filter intersected; the object's is a recursive
filter of the parent prefix. They agree at every one of the 41,347, and the
subgroups agree **as sets of permutations** at all 703 nontrivial objects.

### 2.3 A corollary the unit does not draw, and which MAJOR-1 turns on

Because the condition is σ(Eᵢ) = Eᵢ *for each i separately*, **Stab(H) is a
function of the event SET alone**. Measured: 840 random reshuffles of the
events of 140 histories (120 C3 + 20 C1) changed the stabilizer at **0**.

---

## 3. The stabilizer census

| quantity | published | K1 |
|---|---|---|
| nontrivial distinct prefixes | 703 | **703** |
| stabilizer elements over them | 121,152 | **121,152** |
| order histogram | {2:60, 4:108, 8:270, 24:66, 216:181, 4320:18} | **identical** |
| orbit shapes | 1+1+1+1+1+1+1+2:60 … 3+6:18 | **identical, all six** |
| distinct cycle types | 23 | **23**, and all 23 counts identical, summing to 121,152 |
| FORCED / CHART | 5,852 / 4 | **5,852 / 4** |
| the 4 chart histories | order 216, shape 3+3+3 | **identical** |
| C1 / C2 / C3 per corpus | 72/72, 5,184/5,184, 596 + 4 | **identical** |
| the 4 arrangements | ANT⁴, COL⁴, DIA⁴, ROW⁴ | **identical**, and the "iff" holds: these are exactly the constant-class quadruples in the 600 |
| forced ⟺ crystallized | all 5,856 | **holds at all 5,856** |

---

## 4. The crystallization constant

| quantity | published | K1 |
|---|---|---|
| C1 | exactly 5, all 72 | **5, all 72** |
| C1FAN | exactly 5, all 1,944 | **5, all 1,944** |
| C2 | exactly 5, all 5,184 | **5, all 5,184** |
| C3 | 5:404 \| 7:36 \| 8:144 \| 11:12 \| never:4 | **identical** |
| prefix profile | (4320, 216, 216, 8, 1, 1) | **unique on C1, on C2 and on C1FAN**; the full 9-length profile is (4320,216,216,8,1,1,1,1,1) |
| events 4,5 are transversals of round 1 | True | **True** (C1 and C1FAN) |
| prefix law, disagreements | 0 of 5,184 | **0** |
| stabilizer never grows | 0 in 2,000 prefixes | **0 over all 41,347** |
| nontrivial prefixes with corpus multiplicity | 24,032 | **24,032** |

Two structural remarks, both in the object's favour but neither drawn by it:

- **The transversality is forced, not accidental.** If two saturating rounds
  have disjoint cell sets, a group of round 2 sharing two actors with a group
  of round 1 would repeat a declared pair, so the cell sets would collide.
  I7-STRICTness therefore *forces* every round-2 group to be a transversal of
  round 1, which is what forces 216 → 8 → 1. The paper measures this
  ("The mechanism is measured and not assumed"); it is in fact a theorem.
- **The prefix-law leg is a tautology, not a test.** `C2[i][:9] == C1[i//72]`
  holds at all 5,184 (I checked), and C1 crystallizes at 5 ≤ 9, so
  `crystallization(C2[i]) = 5` is forced. §5's "it is a test of the law, and
  it passes" over-reads a check that cannot fail. The paper's own preceding
  sentence already gives the reason, so this is presentation only — folded
  into MINOR-4.

---

## 5. The invariance split

| row | published | K1 |
|---|---|---|
| co-division preserved | 0 violations / 121,152 elements / 703 objects | **0 / 121,152 / 703** |
| weld-dictionary readings | 121,152 comparisons, 0 differences | **121,152 / 0** at the identity parse; **1,453,824 / 0** at all 12 parses (see MINOR-3) |
| record orbit-constant | 111 of 703; naming-dependent 592 | **111 / 592** |
| Born menu by depth | 134, 58, 58, 58, 58 | **134, 58, 58, 58, 58** |
| cross-tab | 569 / 23 / 53 / 58 | **569 / 23 / 53 / 58** |
| shift-commuting | 813 | **813** |
| translations in the stabilizers | 813 | **813** |
| shift-vs-translation disagreements | 0 | **0** |
| record-preserving elements | 51,769 | **51,769** |
| walk symmetries | 813 | **813** |
| depth-one residue law | 18 triples, 0 collisions | **18 / 0** |
| \|Aut\| index table | 12 rows, 703 objects | **all 12 rows identical**; every index integral; Stab ≤ Aut verified explicitly on 80 objects |
| C1 and diagonal-C2 | \|Aut\| = 1,296, stabilizer trivial | **1,296 at all 72 and all 72**, stabilizer trivial at all |
| C3 \|Aut\| spectrum | 36:536, 72:36, 1296:4, 362880:24 | **identical** |
| complete-relation histories | 24, all trivial stabilizer | **24**, all trivial |
| iff all four classes | True | **True**, and the 24 are exactly the 4! orderings of ROW/COL/DIA/ANT |
| explicit \|Aut\| at one such object | 362,880 | **362,880** by explicit enumeration of S₉ |

Three theorem checks I ran rather than accepted:

- **Shift-commuting ⟹ translation.** σ(x)+ℓ = σ(x+ℓ) for ℓ ∈ {(1,0),(0,1)},
  which generate Z₃², forces σ(x) = σ(0) + x. ✔ (and measured, 0 disagreements
  over 121,152).
- **Translation ∈ Stab ⟹ record-preserving.** nℓ(σx) = r[σx][σ(x+ℓ)] =
  r[x][x+ℓ]. So "translation AND record-preserving" collapses to
  "translation", which is why both counts are 813. The object's two numbers
  are consistent, not redundant-by-accident.
- **The depth-one law is a theorem, not a measurement.** With the all-ones
  start the post-coin amplitude at (x,i) is Σⱼ (3G)ᵢⱼ ω^{nⱼ(x)}, a function of
  the residue triple alone. 0 collisions is forced.

---

## 6. The driven leg — re-driven, not re-read

I drove the 17-schedule W-DRIVE set myself over the committed v10 layers.
Every row of §3's table reproduces:

| window | rounds | events | divisions | maxhits | footprints = groups |
|---|---|---|---|---|---|
| W-C1 ×9 | 3 | 48 | 9 | 1 | **True** |
| W-C3 ×4 (the constant classes) | 4 | 48 | 12 | 1 | **True** |
| W-C3 (d66's own R=4 point) | 4 | 66 | 12 | 1 | **True** |
| W-C3 (collinear) | 4 | 60 | 12 | 1 | **True** |
| W-C2 ×2 | 6 | 102 | 18 | 1 | **True** |

- **0 mismatches**, maxhits ∈ {1} at all 17, refusals none.
- The no-supply control refuses at **`('propose G10', 14)`** — exactly the
  published pair.
- **Stronger than the object claims:** driven at d66's *own* diagonal seed my
  schedule-route builder and d66's committed `conflict_grid(3,4)` emit
  **identical event lists** (66 events / 12 arbitrations / 18 deliveries),
  matching d66's committed row. The object only compares counts here.
- The structural leg is confirmed by my own AST read of d42b1: the arbitration
  branch is `props = {t[0] for t in op[2]}` … `return frozenset(props |
  {vname(base, op[3], op[1])})`, so the footprint cut to the nine actor
  objects **is** the conflict group.
- All 9 back-validation rows verified against the parents' own receipt bytes:
  280, 36, 72 (paper-19 *and* paper-21), 276, 600, 9, 12, 5,184.

---

## 7. Two mutants outside the harness

**M1 — the order axis.** The unit's seed fan realises only the 3 *canonical*
transversals per round. I opened the whole axis:

| menu | orderings of the three groups realised per round |
|---|---|
| the 3 canonical transversals | 1 at 66 rounds, 2 at 96, 3 at 54 |
| all 27 transversals | 1 at 6, 2 at 36, 3 at 30, 4 at 6, 5 at 96, 6 at 42 |

Crystallization over the **full realisable seed axis** (4,512 histories):
**5 at every one**. Over the **full order axis** — all 6 orderings per round,
15,552 histories: **5 at every one**, and the prefix profile
(4320,216,216,8,1,1) is the *unique* profile there too. **The constant is
order-independent**, which is stronger than the published statement and makes
the fan corroborative rather than load-bearing. M1 therefore does not kill the
headline; it kills the licence sentence (MINOR-2).

**M2 — the link declaration.** I rebuilt the entire substrate with ANT in
place of DIA as the third declared link (target (1,1,2) on the new triple).
Result: incidence spectrum {0:1, 4:27, 6:54, 7:162, 9:36}, **36** saturating,
**72** I7-STRICT triples, **276** G-FLAT quadruples, C1 crystallization
**5** at all 72, the same prefix profile, **153** nontrivial C1-prefixes and
**15** record-blind among them — *identical to the delivered declaration in
every entry*. So which three of the four parallel classes are declared is a
gauge choice, as PGL(2,3) ≅ S₄ on the four directions predicts. Nothing in the
census is an artifact of the declaration. (I also re-ran the flat-target
census: (1,1,2), (1,2,1) and (2,1,1) each return 276; the other nine constant
rows return 4 or 6. The target is one of three equivalent choices.)

**The numeral sweep.** 566 numeral tokens over 89 distinct literals in the
paper (my tokenizer greedily keeps comma lists, hence 566 against the object's
544 — I checked the difference is tokenization, not coverage). Every literal
is backed by a value I recomputed, including `596` (600 − 4) and the
`134,58,58,58,58` list. 71 spelled numerals, all backed. 10 fenced blocks with
144 numerals; 7 inline spans with 4; 24,506 characters; 89 table lines = 10
headers + 10 separators + **69** data rows, matching the object's own table
ledger. The head appears in the paper as **exactly 2 copies of each of the 5
segments**, byte-identical to the transcript (E-22 multiset check
independently reproduced).

---

## FINDINGS

### MAJOR-1 — the unit attributes to the SEQUENCE what only the EVENT SET carries; §3 states it as a proposition, and it is false

**Where.** §3: *"here the SEQUENCE is the object, and **the sequence is what a
stabilizer acts on**."* §6.4 heading: *"The relation forgets what the sequence
remembers"*; §6.4: *"**The ordered history**, by contrast, forces the
labelling completely."* Verdict segment 4: *"DEGENERACY=THE RELATION FORGETS
WHAT THE SEQUENCE REMEMBERS … WHILE THE STABILIZER OF **THE ORDERED HISTORY**
IS TRIVIAL."*

**The defect.** Stab(H) = ⋂ᵢ Stab(Eᵢ) is a function of the event **set**; the
order is not a variable it reads. §3's sentence is therefore a false
proposition, and segment 4's contrast is drawn at the wrong structural level.

**Measured.** (i) 840 reshuffles of the events of 140 histories: **0**
stabilizer changes. (ii) At all **24** complete-relation histories the events
are 12 *distinct* triples and the stabilizer **of the unordered event set** is
trivial — the sequencing contributes nothing to the forcing. The 362,880-vs-1
gap is real and exactly as published; it is a gap between the co-division
relation and the *events*, not between the relation and the *ordering*.

**Why it matters here rather than as a nit.** This unit spends a gate
(G-EVENT-SHAPE) and a whole corpus (the 1,944-history seed fan) establishing
that "the history is a SEQUENCE and not a set". That work is legitimate — but
it pays for the **crystallization time**, not for the stabilizer. Measured: on
a 50-history C3 sample, the crystallization time **moves** under within-round
reordering at **9** of them (7↔8), so the sequence is a real variable there.
Segment 4 borrows that licence for a quantity that cannot use it.

**Exact repair (no number moves).**
1. §3: replace *"and the sequence is what a stabilizer acts on"* with *"and
   the sequence is what the crystallization time reads — the stabilizer itself
   reads only the event set, so the ordered comparison is the stronger licence
   of the two quantities."*
2. §6.4 heading: *"The relation forgets what the events remember"*.
3. §6.4 body: *"The ordered history"* → *"The events themselves"*.
4. Segment 4: *"THE RELATION FORGETS WHAT THE SEQUENCE REMEMBERS"* →
   *"THE RELATION FORGETS WHAT THE EVENTS REMEMBER"*, and *"THE STABILIZER OF
   THE ORDERED HISTORY IS TRIVIAL"* → *"THE STABILIZER OF THE EVENT SET IS
   TRIVIAL"*.
5. §1, one clause after the definition: *"(the order is not a variable the
   stabilizer reads: fixing each event setwise is a per-event condition; the
   order enters this unit only through the crystallization time)"*.

### MINOR-1 — §2 pairs two counts taken over different corpus bases

*"the census runs over 101,160 prefix objects, 41,347 of them distinct."*
Measured: **101,160** is the prefix-object total over C1+C2+C3 only, and the
distinct count over *those three* is **39,747**. **41,347** is the distinct
count over **four** corpora, whose prefix-object total is **118,656**; 1,600 of
the 41,347 (and **220** of the 703 nontrivial objects) are contributed by
C1FAN alone. The sentence's "of them" is therefore not true of either pairing.

The same base split reaches §7 undisclosed: the distinct-prefix measure runs
over four corpora and the corpus-multiplicity measure over three. The
**receipt** says so ("distinct prefixes over the four declared corpora, and
prefixes counted with corpus multiplicity over the three primary ones"); the
paper does not.

**Repair.** §2: *"the census runs over 118,656 prefix objects across the four
corpora, 41,347 of them distinct (101,160 objects and 39,747 distinct over the
three primary corpora)."* §7, one clause in the table caption: *"the
distinct-prefix measure is taken over the four declared corpora, the
multiplicity measure over the three primary ones."*

### MINOR-2 — W-C1FAN's licence over-claims what the canonical seed menu exhausts

W-C1FAN: *"at ALL 27 canonical transversal triples, so the seed axis — the
only coordinate that moves the WITHIN-ROUND event order — is exhausted rather
than fixed"*; §2: *"It exists so that the order axis is exhausted rather than
fixed."* The seed axis of a round is **27** transversals (paper-19 enumerates
all 19,683 seed triples at R=3); the canonical menu is **3** of them.
Measured (M1): the canonical menu realises 1–3 group-orderings per round where
the full transversal set realises up to 6; the fan's 432 distinct sequences
against 4,512 on the full seed axis and 15,552 on the full order axis.

**Repair.** Replace *"the seed axis … is exhausted"* with *"the canonical seed
menu is exhausted"*, and §2's *"the order axis is exhausted"* with *"the
canonical seed menu is exhausted"*. **Strengthening available at no cost:**
add to §5 *"and the constant is order-independent: measured over all 15,552
histories obtained by reordering the three groups of every round arbitrarily,
the crystallization time is 5 and the prefix profile is (4320, 216, 216, 8, 1,
1) at every one."* That converts the licence from a claim into a surplus.

### MINOR-3 — "every weld-dictionary reading" is measured at one parse of twelve

§6.1 and segment 3 publish *"EVERY WELD-DICTIONARY READING (121,152 PARSE
COMPARISONS, 0 DIFFERENCES)"*. The sweep is over every stabilizer element at
**one** parse — identity link-label permutation, unflipped orientation. The
dictionary's fiber carries 3!·2 = 12 (labelperm, orientation) readings.

The claim is **true**: I swept all twelve — **1,453,824 comparisons, 0
differences** — and the theorem is uniform in (assign, labelperm, orient), so
nothing is at risk. But the published number is a count of elements, not of
readings, and the head reads otherwise.

**Repair.** Either (a) segment 3: *"EVERY WELD-DICTIONARY READING (121,152
PARSE COMPARISONS AT THE IDENTITY PARSE, 0 DIFFERENCES; THE THEOREM IS UNIFORM
IN THE LABEL PERMUTATION AND THE ORIENTATION)"*, or (b) raise the sweep to all
twelve and publish 1,453,824. (b) costs one loop and is what I ran.

### MINOR-4 — the 5,856 denominator is 5,184 parts theorem

Segment 1's *"IDENTITY FORCED ON 5,852 OF 5,856 COMMITTED HISTORIES"*: 5,184
of the 5,856 are C2, and every C2 verdict is *forced* by its first factor —
`C2[i][:9] == C1[i//72]` at all 5,184 (measured), C1 crystallizes at 5 ≤ 9, so
Stab and the time are determined. The independent census is **672** histories
(72 + 600), of which 668 forced and 4 chart. §5 discloses the mechanism and
segments 1–2 supply the ingredients, so this is a reading hazard rather than a
false count — but the top-line number carries an 8.7× inflation for a reader
who stops at segment 1. The same applies to §5's *"it is a test of the law,
and it passes"*, which describes a check that cannot fail.

**Repair.** Segment 1, one clause: *"(672 INDEPENDENT: C2's 5,184 ARE FORCED
BY C1's 72 UNDER THE PREFIX LAW)"*. §5: *"it is a consistency check of the
law, and the law's prediction is exact"*.

### MINOR-5 — two unit slips

- §6.3: *"so it is blind wherever the record is and at a few sites more"* —
  the census unit is **objects** (134 against 111), not sites. Replace *"at a
  few sites more"* with *"at 23 objects more"*.
- §2: *"Three corpora carry the census"* immediately precedes a §2.2 table
  listing **four**. Replace with *"Three committed corpora carry the census,
  and a fourth — the seed fan — is derived from the first."*

---

## WHAT I TRIED TO BREAK AND COULD NOT

- The Young theorem: no gap in the proof; element-set identity at all 703.
- The order histogram, orbit shapes, 23 cycle types: identical, including the
  full 121,152-element census.
- The constant 5: survives the full order axis (15,552 histories), not merely
  the declared fan.
- The invariance split: every count identical, including 51,769 and 813, and
  both derived-theorem legs (shift⟹translation, translation⟹record-preserving)
  check out.
- The 24 / 362,880 / 1,296 rows and the twelve-row index table: identical.
- The driven leg: my own driver over the v10 layers reproduces every row and
  d66's committed constructor byte-for-byte.
- The link declaration: a gauge choice (M2), so no count is an artifact of it.
- The numeral sweep: every literal in the paper backed by my own recomputation.
- The pin: 13 of 13 declared source digests recomputed from the bytes, 0
  mismatches; the 5 head segments appear exactly twice each, byte-identical to
  the transcript.

---

## CLOSING HASH VERIFICATION

Re-verified at the end of this review, unchanged from the start and equal to
the committed blobs at `9f14488`:

| file | sha256-12 |
|---|---|
| `v14/paper-33-aid.md` | `507da54ae871` |
| `v14/code/aid_exact.py` | `edf3a540cd57` |
| `v14/code/aid_output.txt` | `48fe931bfcdc` |
| `v14/code/aid_receipt.json` | `cd938d7ae9be` |
| `v14/note-aid-pin.md` | `294ffe6c9deb` |

No file in the repository was modified by this review other than this document.
