# K1 — OPERATOR-LENS HOSTILE REVIEW of paper-32 (SEC)

**Seat:** K1 OPERATOR (protocol: HANDOFF-PROMPT.md §4/§9; pin
`v14/note-sec-pin.md`, ledger #258).
**Object, hashes verified at open AND at close, unchanged:**
`v14/paper-32-sec.md` `cfe0825d67b2` · `v14/code/sec_exact.py` `6481a8706503` ·
`v14/code/sec_output.txt` `e80d2f08a257` · `v14/code/sec_receipt.json`
`fdf66d990dbf` · pin `v14/note-sec-pin.md` `c46a9927f2a8`.
**All 15 runtime sources re-hashed independently and matching:** pin
`c46a9927f2a8`, paper-19 `50bb81e67942`, r3_weld_receipt `dfea664f2408`,
paper-21 `ef4a8c35a0c4`, r4dec_receipt `a4538c7019e6`, paper-01
`c4c8880874bf`, paper-02 `1a80a5bf1a1b`, paper-ha `f286ba10d2d9`,
ha_successor_receipt `542b8735daf0`, d42b1 `576275d55ecf`, d60 `684cdb76552b`,
d66 `3d0516ab106e`, d66 output `e252529d2586`, L-1 note `93ea24591c3c`,
reproduction catalog `0cebe543e814`.

**Method.** Everything below was rebuilt from the declared semantics in a
scratch tree. `sec_exact.py` was read to learn what the declarations MEAN and
was then never used as an oracle: no function, no constant and no data
structure of it appears in my code. I built AG(2,3), the parallel classes, the
sector relation, the gluing family, the type canonicalisation, the amalgam
target, the count field, the three fibers, the seam algebra over Q, the
compatibility census and the alignment criterion from scratch; automorphism
orders were computed by two routes of my own (plain leaf-counting backtracking
enumeration, and an amalgam formula Σ_π N_A(π)N_B(π) + Σ_π M_A(π)M_B(π) over
the 1,296 elements of Aut(K₃,₃,₃) built and independently brute-force
verified against all 9! permutations). The DRIVEN layer is the committed
object of study, so d42b1's `candidates_for` is loaded as data; the builder,
the schedule, the record reader and the co-division reader are mine.
Interpreter `/opt/homebrew/bin/python3.13`; `fractions.Fraction` and Python
ints only, no float anywhere. Repo reads were read-only; git untouched; the
single repo write is this file.

---

## VERDICT

**GRADE: AWF — ACCEPT WITH FIXES.**

Four verdict segments, and their measured content survives. I rebuilt the
45,010-gluing census, the 16 types with every population, the whole
automorphism column by two of my own routes, the driven 32-record window row
for row through the committed grammar, the seam system, the compatibility
census, the alignment selection over every one of the 45,010 gluings, the
three cross-sector arms, the five dead arms and the k=0 sterility control —
and **every delivered numeral I could recompute reproduced exactly. Zero false
numbers.** The refusal mechanism §3.2 describes in prose is exactly what the
layer does, down to the menu offering nothing but idle.

The fixes are to **scope and to one head field**, not to a measurement.
Three things say more than the run supports:

1. The RSQ inventory is published as **one** free item where the instrument's
   own receipt records **two** at five of the six doubled types.
2. Four of the sixteen published inventory rows and the TRIANGLE seam row are
   properties of **the chosen representative**, not of the type; the published
   fiber pair is wrong on **25,434 of the 45,010 gluings**, and §5.2's "every
   published row is a row of a type" is false for them.
3. §4.3's "the induced field becomes identically 1" is contradicted by the
   unit's own `EXT-INCIDENCE` rows, which publish `field_values [1, 2]`.

None of these moves the headline: the union welds at 10 of 16 types
(4,186 of 45,010 gluings), alignment and not k is what selects, the seam's
kernel is 4, the cross-sector event kills the dictionary, and the k=0 arm is
sterile — all reproduced.

**Recomputations: 842** (independent rebuilds compared against a delivered
value), across the 16-type census ×2 automorphism routes, 32 driven window
records, 45,010 gluings walked twice, 7 shared-site seam systems, 96
dictionary rows, 3 cross-sector arms, 5 dead arms, 15 source digests and 81
distinct paper numerals.

---

## WHAT REPRODUCED (the decisive targets)

**(1) THE GLUING CENSUS — exact, all 16 rows.** Enumerating gluings as
(k-subset of A) × (injection into B) gives **45,010**, and the closed form
C(9,k)·9!/(9−k)! gives 45,010 by k = 1 / 81 / 2,592 / 42,336. My own type
canonicalisation (min over row and column permutations of the bipartite
part-incidence matrix) returns **exactly 16** types with populations
1, 81, 486, 486, 1,458, 162, 486, 11,664, 8,748, 972, 486, 8,748, 972, 4,374,
5,832, 54 — the paper's §3.1 column, cell for cell. Union carriers 18−k give
**15…18**; realised pairs E = 54 − doubled, giving 54/53/52/51 exactly as
published; the type-map fiber runs **1 to 11,664**.

**(2) THE AUTOMORPHISM COLUMN — all 16, two of my own routes.** Leaf-counting
enumeration (15 types, k ≥ 1) and the amalgam formula (all 16) agree with each
other and with every delivered value: 3359232, 41472, 3456, 3456, 2304, 20736,
3456, 288, 192, 1728, 3456, 192, 1728, 768, 576, 62208. The weighted order
|Aut_w| equals |Aut| at **all 16**, so the site-assignment fiber is **1 at
16 of 16** by a route (weight-stabiliser index computed on an explicitly
enumerated group) that shares nothing with either delivered route.

**(3) THE SWAP FACTOR AT k = 0, ISOLATED.** My amalgam route splits
|Aut| = 3,359,232 into a non-swap coset of **1,679,616 = 1296²** and a
sector-swap coset of **1,679,616**. The factor 2 is the sector swap and
nothing else — the paper's claim, now measured as a decomposition rather than
inferred from a product. |Aut(K₃,₃,₃)| = 1296 by a structured construction and
by brute force over all 362,880 permutations.

**(4) THE DRIVEN WINDOW — 32 rows, row for row.** My own builder over d42b1's
committed menu reproduces every fate, every event count and every division
count: FORCED/REFUSED exactly where published; events 96/98/100/102 and 49 at
each refusal; divisions 18 (9 at refusals); **6 REFUSED under `first`, 0 under
`shared`**; and **driven = combinatorial at 26 of 26**. The single-sector
control reproduces 48 events, 9 divisions, 27 of 27 cells at n = 1,
det = 3/4 at all nine sites, positive definite 9 of 9.

**(5) THE REFUSAL MECHANISM — corroborated to the event.** All six refusals
are the **same event**: `propose ('B', (1, 0))` at prefix 49, i.e. the sector-B
seed's own proposal, after its supply delivery has pulled sector A's past into
its causal past. I queried the layer's menu at that prefix: it offers
**exactly one candidate, of type `n` (idle)**. §3.2's sentence "the layer's own
menu offers nothing but idle" is literally true.

**(6) THE SEAM — every shared site, not just the first.** The six rows
quad(a₁), quad(a₂), quad(a₁+a₂), quad(b₁), quad(b₂), quad(b₁+b₂) have **rank 6
on the 10 entries of Sym²(Q⁴), kernel 4** — and, since the rows do not depend
on the counts, this holds at every shared site of every gluing (see MINOR-6).
I solved the system at **all three** shared sites of ALIGNED(k=3), **all
three** of TRIANGLE(k=3) and the one of k=1: rank 6 / kernel 4 at 7 of 7.
Direct-sum minors **1, 3/4, 3/4, 9/16** (aligned and k=1) and **1, 1, 1, 1**
(triangle), positive definite at all seven. The indefinite completion
reproduces all six counts and gives **Q(2,1,−1,−2) = −2** aligned and **−1**
triangle. Cross-link algebra: kernel **4 → 3 → 2 → 1 → 0**, and it survives a
different nesting order and a third-direction endpoint (each such row touches
exactly one cross entry).

**(7) THE ALIGNMENT SELECTION — exhaustive, and the criterion is exact.**
Walking all 45,010 gluings and computing weldability from **each gluing's own
realised relation** (no doubled pair) gives **1 / 81 / 1,134 / 2,970 = 4,186**;
computing it from the criterion (every shared pair shares a tripartite class
on at least one side) gives the same four numbers, with **0 disagreements at
45,010 of 45,010**. At k = 3 the closed reading "all three in one class on the
A side or one on the B side" counts **2,970 of 42,336** — the same set. k with
a welding type **[0,1,2,3]**; k with a non-welding type **[2,3]**.

**(8) THE COMPATIBILITY CENSUS AND THE LEAK.** Shared cells 0/6/12/18 and cells
where the union differs 0,0,0,0,**2**,0,0,**2**,**4**,0,0,**4**,0,**6**,**4**,0
— exactly the published column, and exactly **2 cells per doubled pair** at
every type (this is forced: a doubled pair is one cell in each chart). The leak
is real and I exhibited it: at the triangle representative the six cells
(chart A/B, sites (0,0)/(0,1)/(0,2), link (0,1)) each read **union n = 2 where
the owning sector reads n = 1**.

**(9) CROSS-SECTOR DIVISION EVENTS, END TO END.** Re-driving the aligned k=3
union (102 events, 18 divisions, relation identical to the combinatorial one)
and then attempting each of the three specifications through the layer's own
menu: SHARED-SEEDED **ADMITTED**, 1 new pair, 1 foreign, |E| 54 → 55;
A-SEEDED **REFUSED** at its proposal; B-SEEDED-PURE **ADMITTED**, 2 new,
2 foreign, |E| 54 → 56. Both admitted records realise a pair between an A-only
and a B-only actor, which the amalgam does not carry, so no bijection can
carry the realised relation onto a 54-edge incidence: **STRUCT-DEAD at both**.

**(10) THE STERILITY CONTROL AND THE DEAD ARMS.** k = 0: 18 carriers, 54
pairs, **0** beyond the two sectors' own, **0** doubled, **0** seam cells,
**0** shared actors, field values [1], |Aut| = 3,359,232 = 1296²×2. Dead arms:
15 site objects against 9 (ARITY-DEAD), 15 against 18 (ARITY-DEAD), triangle
union |E| = 51 against a 54-edge target (STRUCT-DEAD), falsifier realised ⊆
target with **48 of 54 cells at zero** (STRUCT-DEAD / COUNT-DEAD).

**(11) EXTENDED CARRIERS.** `EXT-PAIR` arity matches the SIMPLE subdivision at
16 of 16 and the incidence identity holds at 16 of 16; `EXT-INCIDENCE` arity
matches the CHARTED subdivision at 16 of 16 (70/70, 69/69 at the doubled
types) — and would be ARITY-DEAD under SIMPLE at every doubled type, which is
exactly the price §4.3 states.

**(12) ANCHORS AND ABSTENTION.** All eight verbatim needles located in their
pinned parents by my own normaliser (paper-19 line 477 and `ISOS=1296`;
paper-21 line 383; paper-01 line 812; HA line 192; catalog row 1.6; the three
pin needles across the pin's own line wraps). **No SEC sentence depends on LOR
content**: the extended-carrier lesson is quoted from SEC's own frozen pin,
verbatim, and the pin is one of the 15 hashed sources. The eight fenced blocks
in the paper are the four receipt verdict segments, each exactly twice, with no
stray.

---

## MAJORS

### MAJOR-1 — The RSQ inventory is published as one free item where the run measures two.

**Establishing measurement.** My detector, rebuilt, returns
(`I-SITE-ASSIGNMENT`, `I-DIRECTION-LABEL`, `I-ORIENT`) = **(1, 9, 4)** at five
of the six doubled types and **(1, 9, 1)** at
`(3,(0,0,1),(1,1,1),(2,2,1))`. The instrument agrees with me: its own receipt
carries `"free_items": ["I-DIRECTION-LABEL", "I-ORIENT"]` on those five types.
The mechanism is the mirror of §4.2's: a doubled cell (x, d) is read at cell
(x, d) unflipped and at (x+d, d) flipped, so each chart's flip moves the field
unless the doubled-cell set is invariant under (x,d) ↦ (x+d,d) — which happens
only when the doubled cells fill a whole line.

**What the paper says.** §4.1's table row: `free item: I-DIRECTION-LABEL`,
`fiber: 9`. §4.2: "the free item is always `I-DIRECTION-LABEL`, at fiber 9".
Verdict head: `THE-FREE-ITEM-IS-ALWAYS-I-DIRECTION-LABEL`. The §4.1 "fiber"
column means *all three fibers* on the FOUND row ("1, 1, 1") and *one fiber* on
the UNMOTIVATED row ("9") — the same column, two meanings. Only §11 item 14
discloses `I-ORIENT` "1 or 4", and it cross-references **§4.2, which never
mentions `I-ORIENT`**. The parent's own convention is against this: paper-19's
head publishes `FIBERS=1/1/1(SITE/LABEL/ORIENT,...)`, all three.

**Licensed sentences.**
- §4.1 row: `| doubled types (6 of 16) | UNMOTIVATED | I-DIRECTION-LABEL, and I-ORIENT at five of the six | 1, 9, 4 — 1, 9, 1 at the triangle type |`
- §4.2 opening: "At a doubled type `I-SITE-ASSIGNMENT` is never free. The free
  items are `I-DIRECTION-LABEL`, at fiber 9 at every doubled representative,
  and `I-ORIENT`, at fiber 4 at five of the six: a chart's orientation flip
  reads the doubled pair at the other endpoint's cell, so the field moves
  unless the doubled cells fill a whole line, which is what the triangle
  representative's collinear shared triple does."
- Head: replace `THE-FREE-ITEM-IS-ALWAYS-I-DIRECTION-LABEL` with
  `I-SITE-ASSIGNMENT-NEVER-FREE;THE-FREE-ITEMS-ARE-I-DIRECTION-LABEL-AT-EVERY-DOUBLED-TYPE-AND-I-ORIENT-AT-FIVE-OF-SIX`.
- §11 item 14: point at the repaired §4.2.

### MAJOR-2 — Four published inventory rows and the TRIANGLE seam row are properties of the representative, not of the type. §5.2 and Deviation 2 overstate.

**Establishing measurement.** I walked **all 45,010 gluings** and recomputed
the two chart-borne fibers on each (cheap route validated against the long
36-relabelling / 4-flip field enumeration on six hand-picked gluings, all
agreeing). Spread inside a type:

| type | published | measured over the type's gluings |
|---|---|---|
| `(3,(0,0,1),(0,1,1),(1,2,1))` | (9, 4) | (9,4) at **810**, (18,4) at 4,698, (36,4) at 3,240 of 8,748 |
| `(3,(0,0,1),(1,0,1),(2,1,1))` | (9, 4) | (9,4) at **810**, (18,4) at 4,698, (36,4) at 3,240 of 8,748 |
| `(3,(0,0,1),(1,1,2))` | (9, 4) | (9,4) at **162**, (18,4) at 1,620, (36,4) at 4,050 of 5,832 |
| `(3,(0,0,1),(1,1,1),(2,2,1))` | (9, 1) | (9,1) at **486**, (9,2) at 1,944, (9,4) at 1,944 of 4,374 |

The published (label, orient) pair is correct at **19,576 of 45,010** gluings
and wrong at **25,434**. The seam moves too: the TRIANGLE row
nA = nB = [1,2,1] with minors [1,1,1,1] at every shared site is the *collinear*
representative; the corner-triple gluing `((0,0),(0,0)),((0,1),(0,1)),((1,1),(1,1))`
— same type — gives per-site profiles (1,2,2)/(2,1,1)/(1,1,1) with minors
**[1, 7/4, 7/4, 49/16]**, **[2, 1, 2, 1]**, **[1, 3/4, 3/4, 9/16]**. So §6.1's
closing remark, "the triangle seam's direct-sum minors are all 1 … it moves its
determinant", is representative-bound; the determinant it moves to is not a
type invariant. Six of the sixteen types carry more than one per-site seam
profile (18, 18, 79, 79, 45, 53 distinct profiles respectively).

Drivability is not type-fixed either. Probing non-representative gluings:
`(3,(0,0,1),(1,1,1),(2,2,1))` is FORCED at 98 events under `first` at the
representative, **REFUSED** at one alternative and FORCED at 102 at another;
`(3,(0,0,1),(0,1,1),(1,2,1))` is FORCED at the representative and **REFUSED at
both** alternatives I drew. Even under `shared`, event counts inside one type
run 98 / 99 / 100. (Driven = combinatorial held at every one of the 16 extra
records I drove.)

**Why the mechanism, so the fix is principled.** Two gluings of one type are
related by an element of Aut(K₃,₃,₃)², which is *not* the affine group: it
carries a collinear transversal to a non-collinear one. So the **abstract**
weighted arena is a type invariant — I checked 50 gluings per type and
(carriers, pairs, doubled, |Aut|, |Aut_w|, site fiber) is constant at
**15 of 15** types with k ≥ 1, zero exceptions — while everything read against
the target's *chart* (label fiber, orient fiber, per-site nA/nB, minors,
schedule) is finer than the type.

**What is untouched.** Fate (FOUND vs UNMOTIVATED) is a function of the
doubled count, which is a type invariant; so **10 of 16**, **4,186 of 45,010**,
the alignment criterion, the whole §3.1 census, the site fiber and the k=0 arm
all stand.

**Licensed sentences.**
- §5.2, replacing "Nothing in this paper is read off a single gluing: every
  published row is a row of a type, and every type is given a driven witness at
  both seed rules.":
  "The ABSTRACT union arena is a function of the type: carriers, realised
  pairs, doubled pairs, |Aut|, |Aut_w| and the site-assignment fiber are
  constant on every type's fiber, and so is the FOUND/UNMOTIVATED fate. The
  chart-borne rows are not. The `I-DIRECTION-LABEL` and `I-ORIENT` fibers, the
  seam's per-site (n_A, n_B) profile with its direct-sum minors, and
  drivability under the canonical seed rule are functions of the GLUING; every
  such row below is read at that type's declared representative and is stamped
  `AT-THE-REPRESENTATIVE`."
- Deviation 2, replacing "the census measures that the union arena is a
  function of the type": "the census measures that the ABSTRACT union arena —
  carriers, pairs, doubled pairs and automorphism order — is a function of the
  type; the chart-borne quantities of §4.2 and §6.1 are not."
- §6.1 TRIANGLE row and §4.1: stamp `AT-THE-REPRESENTATIVE`.
- New Deviation 7: "**The per-type fiber and seam rows are representative
  rows.** Price: the published (`I-DIRECTION-LABEL`, `I-ORIENT`) pair is
  correct at 19,576 of the 45,010 gluings; the triangle seam's [1,2,1] /
  [1,1,1,1] row holds at 486 of that type's 4,374. Mitigation: the fate, the
  site fiber and every census column are type invariants and are unaffected,
  and the arena verdict already stamps the driven window."

### MAJOR-3 — §4.3's "the induced field becomes identically 1" is contradicted by the unit's own EXT-INCIDENCE rows.

**Establishing measurement.** The receipt's `EXT-INCIDENCE` rows publish
`count_min 1`, `count_max 2`, `field_values [1, 2]` at all six doubled types —
because the instrument computes the field on the target's own cells
(chart, x, l), which reads the count on the ACTOR PAIR and is unchanged by any
carrier extension (`sec_exact.py:1366-1378`). No field on the subdivided
carrier's own objects is ever computed anywhere in the run. So the sentence is
both unbacked and, on the row a reader would check, contradicted.

**Licensed sentence,** replacing "the induced field becomes identically 1":
"each new site object carries exactly one division by construction, so the
doubled pair is no longer a single object reading 2 — a statement about the
carrier's own objects. The count this run publishes on that row is still the
count on the ACTOR PAIR, and it still reads 1 and 2; the repair is structural,
which is what the row's `STRUCTURE-AND-COUNT-ONLY` scope already says."

---

## MINORS

**MINOR-1 — §7, "at k = 3 the aligned type carries 2970 of the 42336
gluings".** 2,970 is spread over **five** types (486 + 972 + 486 + 972 + 54);
no single k = 3 type carries more than 972. The verdict head has it right
(it attributes 2,970 to the criterion). *Licensed:* "at k = 3 the criterion is
met by 2970 of the 42336 gluings, spread over five types".

**MINOR-2 — §2.4 under-claims its own arrangement fiber.** I enumerated all
**280** partitions of the nine sites into triples, the **36** that are
I7-STRICT saturating, and all **72** admissible arrangement triples: every one
of the 72 realises **exactly the same 27 pairs at count 1**. The fiber is 1 by
exhaustion, not by one witness — and paper-19's own head already carries it
(`STRATUM-WIDE-BY-THEOREM: ALL-72-CARRY-ONE-ARENA`). One sentence buys a
theorem the unit is currently paying for with a single driven example.

**MINOR-3 — `STRUCT-ALIVE-16-OF-16` is forced, and could say so.** Under SIMPLE
individuation the amalgam's incidence set is *identically* the union's realised
pair set at all 16 types — necessarily, since each sector's realised relation
IS the I7 link incidence (measured at G-SECTOR) and the union and the amalgam
are formed by the same identification. The structural test cannot fail at any
gluing of this family. It is not vacuous as a detector (the falsifier and the
triangle-against-aligned arm both die at structure), but the 16-of-16 is a
corollary of the single-sector identity, not new information at the union.
§2.2's "a measurement rather than a construction" is defensible for the target;
the *result* should be stamped as inherited.

**MINOR-4 — a typed constant stands in for a measurement in the compatibility
census.** `sec_exact.py:2227` sets `own = 1` rather than reading the sector's
own field. The value is right (G-SECTOR measures 27 of 27 cells at n = 1) and I
reproduced every row, but the census compares against a literal.

**MINOR-5 — the 12 undetermined seam entries are `4 * 3` typed, not measured.**
`sec_exact.py:2517`. The instrument solves only `gl[0]`'s seam
(`sec_exact.py:2260`). I solved all three shared sites of the aligned
representative independently: kernel 4 at each, so **12 is right** — but it is
currently an arithmetic assertion, and one loop makes it a measurement.

**MINOR-6 — the rank-6 / kernel-4 result is a theorem, presented as three
witnesses.** The six rows are the quadratic rows of a₁, a₂, a₁+a₂, b₁, b₂,
b₁+b₂ and do not depend on the counts, so rank 6 and kernel 4 hold at every
shared site of every gluing of every type. The head's universal "AT EVERY
SHARED SITE" is therefore **safe** — but it is currently earned at three seams.
Saying it is RHS-independent costs a clause and buys the quantifier outright.

**MINOR-7 — §4.4's falsifier is a stump, not a near-complete record.**
Withholding the first arbitration causes the drive to refuse at event 13; the
record carries **2 divisions and 6 realised pairs**, not 17 divisions and 53
pairs. Both declared fates are correct on that object and I reproduced them,
but "one arbitration withheld from a driven union" invites a reader to picture
a nearly complete union. *Licensed:* "one arbitration withheld — after which
the layer refuses the remainder, leaving a 13-event stump with two divisions."

**MINOR-8 — instrument docstring drift.** `sec_exact.py:37` says "16 pinned
sources" and `:99` says "Exactly 16 files are read at run time as SOURCES";
`SOURCES` carries **15**, the output says 15 and the paper says 15. The paper
is right and the docstring is stale.

**MINOR-9 — the LOR citation digest is now unresolvable.** §1 cites paper-30
at `f3e9e9df2c70` (ledger #252); the file on disk now hashes `0a08203b7e99`.
The abstention itself is sound and I verified it independently: no SEC sentence
carries LOR content, the extended-carrier lesson is quoted verbatim from SEC's
own frozen pin, and paper-30 is absent from the 15-source read set. The
citation should be re-stamped at LOR's terminal digest, or explicitly marked
"the delivered version at ledger #252".

**MINOR-10 — `detect`'s docstring inverts its own inclusion.**
`sec_exact.py:1325-1326` says EMBEDDING is a bijection "under which the
realised relation CONTAINS the target's incidence"; §2.3 says "carrying the
realised relation ONTO the target's incidence". The implementation is an
isomorphism test, so both are satisfied — a comment defect only.

**MINOR-11 — §3.2's closing iff is a window statement.** "A union is drivable
exactly when the shared actors carry the base into the second sector rather
than receive one" is measured on 32 records. It survives them exactly (all six
refusals are the same event at prefix 49), but off-window I find refusals at
prefixes 53 and 54 on other gluings of types whose representatives are FORCED,
so the "one event" reading is a property of the table — which the paper does
say — while the iff is not measured beyond it.

---

## NOT IN MY LANE

The seal manifest, the 30-mutant sweep, the CLI contract, the gate-coverage and
DECLARED-LATER accounting, the wall scans, the numeral registry's provenance
rule and the byte-reproduction discipline are K3's; I exercised none of them
beyond reading the receipt for the three rows I cite. Whether `SEC-K-SELECTED`
is properly declined, whether the CHARTED individuation is a licit declaration
at this budget, and the relation of the seam's four free entries to the R-line
are K2's.

## RESIDUAL RISK IF THE FIXES ARE TAKEN

None to any verdict word. MAJOR-1 changes a head field and one table cell and
adds a fiber the receipt already carries. MAJOR-2 adds a scope stamp, a
deviation row and two replacement sentences; **no census number moves**, because
the abstract arena is a type invariant and I verified it at 50 gluings per type.
MAJOR-3 removes one clause. After the repairs, the unit's four decided claims —
the alignment criterion, the seam's four undetermined entries, the cross-sector
kill, and the k = 0 sterility contrast — all stand on measurements I rebuilt
from nothing and reproduced exactly.

**Objects re-hashed at close and unchanged:** `cfe0825d67b2` /
`6481a8706503` / `e80d2f08a257` / `fdf66d990dbf`; pin `c46a9927f2a8`.
