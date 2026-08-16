# ARITY (paper-44) — K1 OPERATOR review

**Seat:** K1 (OPERATOR), three-seat hostile panel, v15 ledger #24.
**Object, verified at open AND at close, byte-identical both times:**

| file | sha256-12 |
|---|---|
| v15/paper-44-arity.md | `177560920b33` |
| v15/code/arity_exact.py | `d0044766fcd8` |
| v15/code/arity_output.txt | `95414a8d2824` |
| v15/code/arity_receipt.json | `c1354b632733` |
| v15/note-arity-pin.md | `89b35dad3219` |

The unit's own three declared parent sources re-hashed independently and agree
with the pinned digests 3 of 3: `v14/paper-39-ndep.md` `e2293b8c3858`,
`v14/code/ndep_receipt.json` `29216cea946f`, `v14/paper-40-sec2.md`
`4fe88602280c`.

**Method.** Everything below was rebuilt from scratch in a private scratch tree
(`k1_core.py` + four stages), from the definitions as the paper states them,
with **no code, no import and no data path shared with `arity_exact.py`**: sites
are integer bit-indices here rather than `(i, j)` pairs, the packing enumerator
is written from the declaration, the naming stabilizer is built as the setwise
stabilizer of the first event and filtered (never as a Young subgroup), and the
information floor is decided by a signature-vector feasibility argument rather
than by enumerating subsets of the event universe. The delivered receipt was
opened only to compare against, after each quantity was computed. Repository
writes: this file only. Git untouched. No PID killed but my own.

---

## GRADE: **ACCEPT WITH FIXES (AWF)**

Every measurement in this unit is right. I rebuilt 432 delivered receipt fields
and **431 agree exactly; the one difference is a container shape (`0` vs `[]`
for the mismatch list), not a value.** No physics number moved anywhere: not the
fidelity gate, not the substrate, not the corpora, not the naming legs (down to
868,480 and 3,981,934), not the crystallization pair, not the ladder, not the
forcing census's leg counters, not SEC-2's census, not the principle table, not
a single transport word or stamp. **THE LEAD reproduces object for object,
including the profile decomposition at a = 2.**

Two MAJORS, both of the same species and neither of them a lever: **a published
metric is named as something other than what it counts (§7, twice, and in the
verdict fence), and a spelled numeral in §11 is contradicted by the unit's own
sealed receipt.** Neither moves a measurement and neither moves a verdict word.
Both are fixable by rewording plus one gate.

Candidate until adjudication.

---

## 1. What reproduced, exactly

### 1.1 The fidelity gate, on my own constructor

| leg | anchored (NDEP receipt, at the declared JSON path) | K1 rebuild |
|---|---|---|
| groupings | 280 | **280** |
| saturating | 36 | **36** |
| strict triples at R = L | 72 | **72** |
| near-flat quadruples | 276 | **276** |
| driven window | 600 | **600** |

5 of 5, and the eight path anchors read out of `v14/code/ndep_receipt.json` at
the declared paths independently: `fidelity/groupings/parent` 280,
`fidelity/saturating/parent` 36, `fidelity/strict_tuples/parent` 72,
`fidelity/flat_tuples/parent` 276, `fidelity/window/parent` 600,
`fidelity/budget_n` 9, `fidelity/max_round_incidence` 9,
`fidelity/saturation_is_maximal` true. 8 of 8.

The 600 is worth its own line because it is the one anchored count whose
construction is intricate. My rebuild decomposes it as **256 class tuples + 264
near-flat tuples + 0 control + 80 seed-fan = 600**: 12 of the 276 near-flat
quadruples are already class tuples `(COL, ROW, DIA, DIA)` in some order and
deduplicate away, the alternating control is itself a class tuple and
contributes nothing new, and the collinear seed fan contributes 81 − 1. The
delivered receipt's window count is reproduced with the same internal
structure, not merely the same total.

I also confirmed the extension claim at the object level, not the count level:
the maximal-packing route at a = 3 returns **the identical 280 objects** the
partition route returns (list equality, not cardinality).

### 1.2 The substrate and the packing extension at a = 2 | 4 | 5

| a | blocks | idle | groupings | max weight | weights | sat@budget | sat@max | cover R_min |
|---|---|---|---|---|---|---|---|---|
| 2 | 4 | 1 | **945** | **4** | 1,2,3,4 | **0** | **324** | 7 |
| 3 | 3 | 0 | **280** | **9** | 0,4,6,7,9 | **36** | **36** | 3 |
| 4 | 2 | 1 | **315** | **10** | 6,7,9,10 | **81** | **162** | 3 |
| 5 | 1 | 4 | **126** | **8** | 6,7,8 | **0** | **81** | 4 |

Every cell agrees with the delivered row, including the weight spectra the
paper does not print. Saturation-is-maximality is true at a = 3 alone.

Corpora, all four rows exact: strict R = L 0 | 72 | 162 | 0; driven window
0 | 600 | 0 | 0; near-flat tuples 0 | 276 | 0 | 0; least-crystallizing rounds
2 | 2 | 3 | 4; multi corpora 11,664 (CX-ORBIT-REDUCED, 36 orbit
representatives × 324) | 72 | 162 | 0 (NOT-REACHED, **4,782,969** = 9 × 81³
against the declared cap 100,000); orbit sizes [9] at both orbit-reduced rows.

### 1.3 Law 1 — naming

| leg | delivered | K1 rebuild |
|---|---|---|
| prefixes vs the whole symmetric group | 400 | **400** |
| positives on the group leg | 868,480 | **868,480** |
| prefixes vs the declared window | 19,778 | **19,778** |
| window size | 204 | **204** |
| positives / negatives on the window leg | 52,778 / 3,981,934 | **52,778 / 3,981,934** |
| mismatches | 0 | **0** |

Route A was built here **without any reference to the signature partition** —
the setwise stabilizer of the first event, enumerated exactly, then filtered by
the remaining events — and compared as a set against a Young subgroup built
from the signature blocks. 400 set equalities on the group leg and 19,778 on
the window leg, **0 mismatches**, and the group-leg positive sum equals the
product-of-factorials sum independently (868,480 both ways). The window leg's
arithmetic closes: 19,778 × 204 = 4,034,712 = 52,778 + 3,981,934. Distinct
prefix event sets by arity (unpublished): 17,608 | 1,287 | 757 | 126.

### 1.4 Law 2 — crystallization, and the NDEP floor bonus

| a | schedule (events) | rounds | attained floor | universe | counting bound | sharpened | offset |
|---|---|---|---|---|---|---|---|
| 2 | **6** | 2 | **6** | 36 | 4 | **6** | **0** |
| 3 | **5** | 2 | **4** | 84 | 4 | **4** | **1** |
| 4 | **5** | 3 | **4** | 126 | 4 | **4** | **1** |
| 5 | **4** | 4 | **4** | 126 | 4 | **4** | **0** |

Schedule 6|5|5|4, floor 6|4|4|4, offset 0|1|1|0 — all exact.

**The floor bonus is confirmed and it is the sharpest thing in the paper.** The
attained floor was re-derived here by a route the unit does not use: a floor of
k is attainable at arity a exactly when nine distinct k-bit signature vectors
exist with every coordinate covered exactly a times. That decides all four rows
without touching the event universe, and it certifies the a = 2 row as *exact*
rather than merely searched: k = 4 and k = 5 are infeasible (the nine lightest
distinct signatures cost 12 and 11 against budgets 8 and 10), k = 6 has a
witness. So:

- **sharpened floor, with the EVENT SIZE in the place NDEP's own quotation
  names, reproduces the attained value at 4 of 4 arities;**
- **the counting bound published beside it reproduces it at 3 of 4** — it fails
  at a = 2 by exactly two (4 against 6);
- and the same formula read with the FIELD ORDER instead of the event size —
  which is precisely what MUT-FLOOR does — returns 4|4|4|4 and fails at a = 2.
  The falsifier bites on a real distinction, verified here by hand.

NDEP's own receipt confirms the two claims the paper makes about the parent:
schedule 3|5|7 and floor 2|4|6 at n = 4|9|16 with **offset one at all three
actor counts** (`v14/code/ndep_receipt.json`, law2_crystallization), and the
parent's n = 9 pair is 5 and 4 — both reproduced here at a = 3 by this unit's
own constructor.

### 1.5 Law 3 — the menu

Lattice **21,147** = Bell(9) by the Bell triangle; leg-1 survivors **6**; coset
partitions of the translation subgroups **6**; and the two sets are equal as
sets, not merely equinumerous. Subgroup orders 1, 3, 3, 3, 3, 9. The row is
correctly stamped a disclosure: leg 1 reads the partition and the arena only,
so no arity can move it, and the paper says so.

### 1.6 Law 4 — the ladder

All eight arity × reading rows exact — saturating counts, round mass, predicted
modulus, achievable set, derived-vs-searched split:

| a | reading | sat | mass | modulus | achievable | derived / searched |
|---|---|---|---|---|---|---|
| 2 | LITERAL | 0 | — | — | — | 0 / 0 |
| 2 | MAXIMAL | 324 | 4 | 27 | none | 9 / 0 |
| 3 | LITERAL | 36 | 9 | **3** | **3, 6, 9** | 6 / 3 |
| 3 | MAXIMAL | 36 | 9 | **3** | **3, 6, 9** | 6 / 3 |
| 4 | LITERAL | 81 | 9 | **3** | **3, 6, 9** | 6 / 3 |
| 4 | MAXIMAL | 162 | 10 | 27 | none | 9 / 0 |
| 5 | LITERAL | 0 | — | — | — | 0 / 0 |
| 5 | MAXIMAL | 81 | 8 | 27 | none | 9 / 0 |

The nL/gcd mechanism holds exactly: modulus = 27 / gcd(27, mass) at every row
(4 → 27, 9 → 3, 10 → 27, 8 → 27), and **the modulus reads 3 at a = 3 AND at
a = 4 under the budget reading**, which is the decisive row because there
a ≠ L. Three of the eight rows carry a rung and all three carry exactly the
multiples of L. See MAJOR-1 for how this is *named*.

### 1.7 Law 5 — division forcing

| a | single rounds | discrete alone | non-unique | rounds that are parallel classes |
|---|---|---|---|---|
| 2 | **945** | **945** | **0** | **0** |
| 3 | **280** | **276** | **4** | **4** |
| 4 | **315** | **315** | **0** | **0** |
| 5 | **126** | **126** | **0** | **0** |

Exact, and so are the multi and driven-window arms (72/72/0; 162/162/0;
600 → 596 unique + 4 non-unique with joiner block size 3) and **every leg
counter**, which is the part of this census most likely to drift under an
independent implementation of paper-20's operator:

| a | l2 | l3 | l4 | l4 reached |
|---|---|---|---|---|
| 2 | **12,609** | **12,636** | **12,609** | **12,609** |
| 3 | **960** | **4,356** | **960** | **960** |
| 4 | **477** | **1,287** | **477** | **477** |
| 5 | **126** | **126** | **126** | **126** |

I re-implemented the record vector, the induced cell partition and the coupled
walk's one-step columns at both coin orders from the paper's description; the
discrete partition is admissible at every one of the 14,164 histories (checked,
not assumed), and the thesis holds per object at every arity.

### 1.8 Law 6 — SEC-2, and THE LEAD

The union rebuilt independently from the arrangement: **15 carriers** (6 + 6
sector-only plus 3 seam), **54 realised pairs**, **0 doubled pairs**.

| a | groups | seam-spanning | opens no pair inside | and doubles nothing | max cut | forced inside |
|---|---|---|---|---|---|---|
| 2 | **105** | **36** | **36** | **36** | 1 | **0** |
| 3 | **455** | **288** | **216** | **0** | 2 | **1** |
| 4 | **1365** | **1113** | **405** | **0** | 4 | **2** |
| 5 | **3003** | **2751** | **243** | **0** | 6 | **4** |

Every number of THE LEAD reproduces, and so does the **profile decomposition**,
which the paper does not print but the receipt seals: at a = 3,
(2 cross, 0 new, 1 doubling) × 108, (1, 0, 2) × 108, (2, 1, 0) × 72 — which is
SEC-2's own 288 / 216 / 72 recovered by a route sharing no code with it — and
at a = 2 the single profile **(1 cross, 0 new, 0 doubling) × 36**. The
trichotomy identity (every pair of a group is a cross pair, a new within-sector
pair or a doubling; cross pairs never exceed the maximum cut) holds at **all
4,928 groups with 0 violations**.

`C(a,2) − ⌊a²/4⌋ = 0 | 1 | 2 | 4` re-derived and matched to the measured
forced-inside column at every arity. **At a = 2 the bound is zero, and the
measurement is not merely consistent with that — all 36 seam-spanning groups
sit in the free class.** The theorem holds at 3, 4, 5 and is empty at 2.

All four SEC-2 verbatim anchors are verbatim in `v14/paper-40-sec2.md` at the
declared character lengths, once each (90, 35, 123, 76 chars); the four NDEP
anchors likewise (85, 43, 96, 68). **8 of 8 anchors located, and each says what
the consuming gate says it says** — I read SEC-2 §4.3 in place: its second
table row *is* the crossing-alone control, priced at 0 free items and stamped
"no three-actor group can produce it". The paper's use of it is faithful, and
it correctly refuses to recompute the free items.

### 1.9 Principles, and the two-level aggregate

The principle census reproduces at all 9 candidate event sizes, row by row:
admits sets `round_completeness` {1,3,9}, `subgroup_order_available` {1,3,9},
`cover_at_R_equals_L` {3,4,6}, `saturation_at_the_budget` {3,4,6},
`saturation_is_maximality` {3}; **3 of 5 select the parent arity among the
nontrivial sizes.** The mechanism claim checks out: the translation group's
realised subgroup orders are 1, 3, 9 and at a prime field order the actor count
has no other divisors.

The aggregate, recomputed through my own decision procedure: **statements 4
LAW-IN-A / 2 BREAKS** (crystallization fails at 2 and 5; sec2-counting fails at
2), **numerals 0 LAW-IN-A / 2 NEEDS-3 / 5 BREAKS**, every stamp identical
(DISCRIMINATED at both NEEDS-3 rows, FAILS-BOTH at all five BREAKS rows),
**both declared alternative a-only rules move nothing (0 of 7 under `a` itself,
0 of 7 under blocks-per-round)**, and the six synthetic controls come out
forced 6 of 6 with four distinct stamps. The n = 16 successor's arithmetic in
§13 is correct: C₂⁴ has subgroup orders 1, 2, 4, 8, 16 (every divisor), while
F₄-linear subspace cosets have sizes 1, 4, 16 only — the registration's whole
point survives checking.

---

## 2. MAJOR findings

### MAJOR-1 — the ladder's headline metric is named as something it does not count; under its own words the value is 2, not 0

**The claim.** §7, bolded: *"The number of rows whose first rung is the event
size is 0."* Repeated in the verdict fence: `THE NUMBER OF ROWS WHOSE FIRST
RUNG IS THE EVENT SIZE IS 0`, in the gate statement of G-LAW4-LADDER, and in a
second form at the close of §7: *"Across the whole sweep mod-a never appears,
at either saturation reading and at every arity searched."*

**The measurement.** Under those words the value is **2**. At a = 3, both
readings carry the achievable set {3, 6, 9}; the first rung is 3; the event
size is 3. The receipt's own per-row field says so — `first_rung_is_the_event_
size: true` at exactly the two a = 3 rows and false at the other six — and my
rebuild agrees row for row. The modulus at a = 3 is 3, which is the event size,
so "mod-a never appears" is false there too. The paper's own §7 table prints
`| 3 | LITERAL | 36 | 9 | 3 | 3, 6, 9 |` two paragraphs above the bolded
sentence, so the text contradicts its own table.

**What is actually counted.** `arity_exact.py:2554` defines
`mod_a_appears = bool(ach) and min(ach) == a and a != A.L`, and the head numeral
is `sum(1 for r in ladrows if r["mod_a_appears"])`. The registry even names it
correctly in the count register — *"rows whose first rung is the arity"* — but
the excluded clause `a != L` is nowhere in the published sentence. The code
comment at 2549–2553 shows the exclusion is deliberate and the reasoning is
sound; only the label is wrong.

**Severity.** No measurement moves and no verdict word moves: the ladder
numeral is NEEDS-3 under either accounting, and the discrimination is carried
entirely by the a = 4 budget-reading row where a ≠ L and the modulus is still
3. The defect is that a bolded head numeral and a verdict-fence segment are
false as written and are contradicted by the unit's own sealed rows. This is
the AUTOGLUE-M2 species (a false scope word in a head string), and like it, it
is short of a reject lever.

**Fix.** Rename the metric everywhere it appears — "the number of rows at which
the first rung is the event size **and the event size differs from the link
count** is 0" — or publish both counters (2 and 0) side by side, which is
strictly better because the coincidence at the parent's arity is exactly what
this axis exists to break. Gate it: `first_rung_is_the_event_size` must be
rendered into the head beside `mod_a_appears`, so that a run in which the two
diverge cannot publish only one.

### MAJOR-2 — a spelled numeral in §11 is false and is contradicted by the unit's own sealed receipt

**The claim.** §11: *"Under the maximality reading it is feasible at three
arities and false at all but the parent's."*

**The measurement.** Feasibility for that row is `bool(sat)` at the MAXIMAL
reading, and the MAXIMAL-saturating set is non-empty at **all four** arities:
324 | 36 | 162 | 81. The unit's own sealed evidence says so —
`transport/ladder_statement_under_the_maximal_reading/evidence/feasible = 4`,
`carried = 4`, `holds_at = [3]`, `fails_at = [2, 4, 5]` — and my rebuild returns
the same word (BREAKS) with the same failing set. **The true count is four.**

There is no repairing reading. The only set of size three in the neighbourhood
is {2, 4, 5}, the arities where the two readings differ, and that set excludes
the parent's arity, which the second half of the same sentence requires to be
feasible.

**Why nothing caught it.** The number is spelled. G-PAPER-COVERAGE scans
`(?<![\w.])(\d[\d,]*)(?![\w.])` — digits only, 456 numerals — so a spelled
cardinal is invisible to it; G-PAPER-CLAIMS binds 6 prose claims and this is
not one of them; G-PAPER-REFERENTS binds 23 sentences and this is not one of
them. This is the AUTOGLUE-M1 disease (a false SPELLED fraction in prose bound
by no gate) recurring in the fourth unit of the wave, and CONTRACT-K3's "92
spelled numerals ungated" is the same hole seen from the instrument side.

**Severity.** MAJOR because it is a false published number contradicted by the
unit's own receipt. It moves nothing: the alternative-reading row is BREAKS
either way, and the row is a disclosed sensitivity leg rather than a headline.

**Fix.** Change "three" to "four", and extend the coverage scan to spelled
cardinals (the unit already has `quote_spelled`, which parses spelled numerals
out of the parents — the same routine applied to its own prose closes the
hole).

---

## 3. MINOR findings

**m1 — the schedule time's search domain is narrower than the sentence that
publishes it (value confirmed anyway).** §5 and the verdict fence say the
schedule time is *"the minimum over every history the arity admits"*, by
"breadth-first search over every history the arity admits". The run calls
`bfs_min_schedule(P, satM)`: the round pool is the MAXIMAL-saturating groupings
only — 324 of 945, 36 of 280, 162 of 315, 81 of 126. So the delivered number is
a minimum over a declared sub-family, not over every history. **I re-ran the
breadth-first search over EVERY grouping at every arity: 6 | 5 | 5 | 4 events
and 2 | 2 | 3 | 4 rounds — identical.** The claim is true; the instrument did
not establish it, and now it has been. Either narrow the sentence or adopt the
measurement (see §5 below, it is free).

**m2 — §3's reason for the empty covering class is measured under the other
reading.** The `strict R = L` column is computed at the LITERAL reading, and at
a = 2 and a = 5 there are no budget-saturating groupings at all — the receipt
itself carries `mass_LITERAL: null` at both rows. §3 explains the emptiness
instead by "a round of measured mass w ... the least R that can cover it is the
cell count over that mass", which is `cover_R_min` (7 and 4 against L = 3) and
is computed from the MAXIMAL mass. Both statements are true; the sentence
attributes the column's emptiness to an arithmetic about a mass that column
never had.

**m3 — "they part company at a = 4" understates its own table.** The budget and
maximality readings differ at a = 2 (0 vs 324), a = 4 (81 vs 162) and a = 5
(0 vs 81). §3's prose is exact about all three; the §2 sentence and the verdict
fence compress to a = 4, which is defensible only under the unstated gloss
"the arity at which both are non-empty and still differ".

**m4 — "nothing else in the repository is read" vs the unit's own read set.**
§2 says four files are read at run time and nothing else in the repository is
read. G-READ-SET reports `distinct_reads: 6`: the four pinned sources, the
paper under test, and the module's own source under a declared exemption. The
four *authenticated* files are four; the files read are six.

**m5 — a dead check inside the head comparator.** `arity_exact.py:3265–3268`
builds `pat = "%d %s" % (count, word)` and then executes `pass`. The head's own
word-count numerals ("0 LAW-IN-A, 2 NEEDS-3 AND 5 BREAKS") are therefore bound
to the recomputed counters by nothing; only the counters' equality with the
builder's is checked. Credit where due, and against the pattern in this wave:
the comparator **does** genuinely re-decide both word tallies from the evidence
rows by its own arithmetic without calling `transport_word` (3242–3264), so
§11's independence claim is substantially true — this is the one leg of it
that was left switched off.

**m6 — "a driven event" at a = 2 is not measured.** §9 closes on *"the arity at
which a driven event can realise the row it could only construct by hand"*.
What is measured is that a two-actor **group** of the 15 union carriers
realises the configuration; nothing in this unit drives rounds on the union at
any arity (the a-grammar is built on one 9-site sector, whose events are never
cross pairs). SEC-2's own census ranges over exactly these groups, so the
comparison is apt, but the word "driven" carries more than the census does.
§13 states the honest version ("Whether a two-actor crossing is a lawful
autonomous event requires the price the unit that owns the update rule
computes"), so this is a wording slip, not a claim the paper elsewhere makes.

**m7 — a typed actor count inside a declared transport rule.**
`t_a_alt_blocks` at 346–347 reads `(9 // a) + (parent_value - (9 // PARENT_
ARITY))` — the actor count typed twice as a literal instead of `A.n`. No number
moves (n = 9 is held fixed by declaration and the sensitivity leg returns 0
either way), but it is a typed count in exactly the class TPL-2 polices.

---

## 4. Numeral sweep

473 numerals in the paper, 52 distinct. Every one checked against my rebuild or
against its structural referent: the nine unmatched-by-measurement values are
all identifiers read in place (paper-20/33/35/39/40/44, `#46`, `E-24`,
`sha256-12`). **No numeral in the paper is unaccounted for, and no
digit-carried numeral is wrong.**

Spelled fractions and spelled cardinals were swept sentence by sentence (the
AUTOGLUE-M1 check). Three fraction-shaped claims exist:

- "the five substrate counts agree with the committed anchors **5 of 5**" — TRUE, re-derived on my own constructor;
- "The counting bound reproduces it at **three of four**" — TRUE (agrees at a = 3, 4, 5; fails at a = 2 by two);
- "Every pair of a group is **one of three things**" — TRUE, 0 violations over all 4,928 groups.

Of the remaining spelled cardinals, all check out (six controls, six open
questions, six laws, five principles, four parallel classes, eight anchors of
each kind, "one redundant event at three different actor counts" — verified in
NDEP's receipt at n = 4, 9, 16) **except the one in MAJOR-2**.

---

## 5. Bonus for the unit — three things it may lift

1. **The schedule-time claim is TRUE at full strength, and I have the
   measurement.** Breadth-first over *every* grouping at every arity returns
   6 | 5 | 5 | 4 events, identical to the saturating-pool search. The unit can
   promote §5's sentence from an over-claim to a measurement by running the
   unrestricted pool (945/280/315/126 rounds; it costs about a minute) or by
   citing this leg.

2. **The mechanism behind two of its own numbers.** The declared-link graph on
   the nine actors is exactly **K₃,₃,₃**, whose three parts are the lines of
   the *undeclared* parallel class ANT — 27 edges, degree 6. That single fact
   explains, without search: why saturating groupings at a = 3 are precisely the
   transversal packings (hence 3! × 3! = 36); why the union carries **54 pairs
   with zero doublings** (the seam is an ANT line, so it carries no declared
   link, and the two sectors' relations are disjoint); and why the weight
   spectra are what they are. The paper currently reports 15/54/0 as measured
   outputs; they are forced.

3. **The a = 2 floor is exact, not merely searched.** The floor at arity a is
   the least k admitting nine distinct k-bit signatures with every coordinate
   covered exactly a times. That gives 6 | 4 | 4 | 4 with a two-line
   infeasibility proof at k = 4 and k = 5 for a = 2 — which is the very row
   where the counting bound fails and the sharpened floor wins, i.e. the row
   the paper's best result rests on. Worth carrying as a certificate beside the
   exhaustive search.

---

## 6. Recomputation count (honest)

- **432 delivered receipt fields** rebuilt and compared field by field: **431 exact, 1 container-shape difference (`0` vs `[]`), 0 wrong values.**
- **20,178 stabilizer set-equalities** recomputed by a definition-route that never mentions the signature partition (400 against the whole symmetric group, 19,778 against the declared 204-element window).
- **84,984 admissibility decisions** in the forcing census (14,164 histories × 6 lattice survivors), including the discrete-partition check at every history.
- **4,928 union groups** classified pair by pair for the SEC-2 census, with the trichotomy identity verified at each.
- **4 unrestricted breadth-first schedule searches** over the full grouping sets (the m1 leg the unit did not run).
- **16 floor feasibility decisions** (4 arities × k = 3…6) by an independent route.
- **473 paper numerals** swept, 52 distinct, plus a sentence-by-sentence spelled-cardinal sweep.
- **24 distinct provenance items, 29 verification acts**: 5 object digests (each verified at open and again at close = 10 acts), 3 parent source digests, 8 verbatim anchors located at their declared lengths in the pinned bytes, 8 path anchors read at their declared JSON paths.

**No computed number in this unit is wrong.** The two MAJORS are a name and a
spelled word.

---

## 7. Summary for the adjudicator

ARITY's measurements are as solid as anything this seat has rebuilt. The
fidelity gate reproduces on a from-scratch constructor 5 of 5 and, at the
object level, returns the parent's identical 280 groupings. The a = 2 and a = 4
grammars, the corpora, the two naming legs down to 868,480 and 3,981,934, the
crystallization pair, all eight ladder rows with the nL/gcd mechanism, all
sixteen forcing leg counters, the whole SEC-2 census including the profile
decomposition, the nine-row principle census and every transport word and stamp
— all exact.

**THE LEAD stands.** 36 | 288 | 1113 | 2751 seam-spanning, 36 | 216 | 405 | 243
opening no pair inside a sector, 36 | 0 | 0 | 0 also doubling nothing, and
C(a,2) − ⌊a²/4⌋ = 0 | 1 | 2 | 4 with the a = 2 free class fully populated. The
unit's discipline around it is correct: it does not recompute SEC-2's free
items, it says so, and it routes the price question to the unit that owns the
update rule.

What must be fixed before seal: **(1)** the ladder metric renamed so the
published sentence counts what the code counts — under its own words the value
is 2, and the receipt's own rows say so; **(2)** "three arities" corrected to
four in §11, with the coverage scan extended to spelled cardinals so the next
one dies in the harness. Seven minors, none of which moves a number; one of
them (m1) I have already closed in the unit's favour.

Grade: **ACCEPT WITH FIXES**. Candidate until adjudication.
