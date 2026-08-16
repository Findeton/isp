# THEORY-CONTRACT (paper-43) — K1 OPERATOR-LENS REVIEW

**Seat:** K1, the operator lens — the mathematics itself, rebuilt from the
arena's and the parents' definitions with code sharing nothing with
`v15/code/contract_exact.py` (no import, no copied function, no shared literal,
no shared intermediate file).
**Stance:** hostile; every number assumed wrong until independently rebuilt.
**All rulings below are candidate until adjudication.**

**Objects, sha256-12, verified at open AND at close (all five match):**

| object | sha256-12 |
|---|---|
| `v15/paper-43-contract.md` | `a0caabea6566` |
| `v15/code/contract_exact.py` | `d7f4c15e7704` |
| `v15/code/contract_output.txt` | `2f1933c09b8f` |
| `v15/code/contract_receipt.json` | `9b3638b796ae` |
| `v15/note-contract-pin.md` (pin) | `438586c11db5` |

All sixteen pinned sources re-hashed independently against the instrument's
`SOURCES` table and the paper's §8 read-set table, all sixteen matching:
`v14/TEMPLATE.md` `809ebe3514ad`, `v14/code/era_template.py` `d04a3eb58fbc`,
paper-19 `50bb81e67942`, paper-20 `4824d190af73`, paper-21 `ef4a8c35a0c4`,
paper-31 `0092caa4d9ad`, paper-32 `f3f43d94cd75`, paper-33 `ecdd3fbf1d06`,
paper-35 `281289a615ad`, paper-38 `22beb6696223`, paper-39 `e2293b8c3858`,
paper-40 `4fe88602280c`, paper-41 `c5fbc9acbd76`, paper-42 `164aa0d755bc`,
`v15/PLAN.md` `6ba8621d4ec7`, pin `438586c11db5`.

**Recomputations: 215.** 114 receipt scalars/booleans re-derived from scratch
and compared leaf by leaf (**114 agree, 0 disagree**); 23 further quantities
computed that the unit does not carry; 13 anchor needles located verbatim in
their claimed parents at pinned digests; 21 sha256-12 digests; 4 head segments
byte-compared paper↔`contract_output.txt`; 40 distinct paper numerals swept.

---

## GRADE: **AWF** (accept with fixes)

**No computed number in this unit was found to be wrong.** I rebuilt AG(2,3),
the 27-cell carrier, the link graph, the 280 groupings, the round law, the
I7-STRICT and G-FLAT strata, the driven window, all three committed corpora, the
record, the coupled walk over Z[ω], the reconstructor, the cast search, the
nine arms and all four parameter fibers on primitives that share nothing with
the instrument, and **every one of the 114 receipt leaves reproduced exactly** —
the 20 census quantities, the residue theorem, the invariance census, the
quotients, the dependency cycles, the cast search, the nine arm certificates,
the coin/menu/seam/direction fibers. The four verdict segments in the paper are
byte-identical to the ones in `contract_output.txt`. The three citation rows
are located verbatim in their claimed parents at their pinned digests. The
numeral sweep is clean: every numeral in the paper is either a quantity I
recomputed or a section number/row tally I verified.

Two of the paper's own identifications turn out to be **stronger** than it
claims, and I record them as FOUNDs below.

The grade is AWF and not A because three findings are not about numbers but
about *what the correct numbers measure*, and two of them touch headline
sentences: the Q58 domain probe over-counts its own evidence fivefold at the
grain the reconstructor actually reads (M1); the quotient row silently changes
object between its "before" and "after" columns, attributing to the
automorphism groups a collapse that is 97.7% order-forgetting (M2); and the
`Born-menu values` row prints a quantity that is not the Born menu, backed by a
builder the module never calls (M3). None of these moves a receipt leaf. All
three have exact liftable repairs.

---

## THE PANEL BRIEF ITEM (review #5), SETTLED

> *verify the alleged SEAM census duplication + duplicated parent quotation
> against the 23-object claim*

**Ruling: the SEAM duplication does NOT exist. The duplicated parent quotation
DOES exist in substance, though not in letter.**

**(a) SEAM in the census table — no duplication.** I parsed the §1 table out of
the paper's bytes rather than trusting the instrument, and measured:

| measured on the paper's own table | value |
|---|---|
| rows parsed | 23 |
| distinct object names | 23 |
| repeated names | none |
| rows named SEAM | **1** |
| class tally | DECLARED 9 / GENERATED 10 / LAW-SELECTED 2 / RECONSTRUCTED 2 = 23 |
| backing tally | COMPUTED-HERE 20 / SEALED-CITATION 3 = 23 |

SEAM's second appearance in the paper is in the **§6 parameters table** (`the
seam | the completion at a shared site | COMPUTED-HERE | FREE`). That is a
different table with a different subject — §1 censuses *objects*, §6 censuses
*declarations* — and an object that is also a declaration legitimately appears
in both. The same is true of `the coin`, `the menu`, `L` and `the record`. The
23-object claim is not inflated by any SEAM row.

**(b) The duplicated parent quotation — real, at two hops.** The
CARRIER-CANDIDATE row is backed by two anchors, and they are two *different*
files at two *different* pinned digests, each carrying its needle exactly once
(I located all thirteen anchors under the era's whitespace/markdown
normalisation; 13 of 13 found, each with occurrence count 1):

- `REC-CARRIER` → `v14/paper-41-rec.md` `c5fbc9acbd76`: *"27 cells against 27
  pairs, two actors in each cell at all of them, six cells per actor at all
  nine"*
- `OCC-CARRIER` → `v14/paper-31-occ.md` `0092caa4d9ad`:
  *"CELLS-WITH-EXACTLY-TWO-ACTORS=27-OF-27; ACTORS-IN-EXACTLY-SIX-CELLS=9-OF-9"*

So it is not a duplicated *quotation*. But paper-41's sentence is **itself a
quotation of OCC** — its line 46 reads *"The parent's own carrier row says
`27 cells against 27 pairs…`"* — and the strings `27 cells against 27 pairs`
and `six cells per actor` occur in paper-41 only, while
`CELLS-WITH-EXACTLY-TWO-ACTORS` and `ACTORS-IN-EXACTLY-SIX-CELLS` occur in
paper-31 only. The two anchors therefore trace to **one measurement in one
parent**, presented in §1 as two viewpoints (*"and the same object seen from the
exclusion census reads"*). One of the three SEALED-CITATION rows is doubly
backed by a single fact.

**Repair (minor):** say so in §1 — *"the exclusion census measured it and the
reconstruction unit quotes that measurement back"* — or drop `REC-CARRIER` from
the census gate and keep it where it does independent work.

**(c) A weaker duplication the brief did not name, which is real.** Three census
rows are re-descriptions of rows already in the table, by the rows' own reading
columns:

| row | its own reading | the row it re-describes |
|---|---|---|
| SITE (9) | *"the same objects as the actors under the weld's dictionary"* | ACTOR (9) |
| CO-DIVISION-PAIR (27) | *"the cell is the unordered pair, by the carrier typing"* | CELL (27) |
| CARRIER-CANDIDATE (27) | OCC's carrier is the 27 cells | CELL (27) |

I confirmed the CELL↔CO-DIVISION-PAIR map is a bijection (27 cells, 27 distinct
unordered pairs, `cells == pairs` True) and that RECORD-BLOCK is *not* a fourth
copy (its members are 3-element sets of cells, verified `{3}`). Extensionally
the census names at most **20** distinct sets of objects, not 23. The paper is
not hiding this — each reading column says it — but the head prints
`OBJECTS=23`, and 23 is a row count, not an object count. See m1/m2.

---

## FOUNDS (things that got stronger under hostile rebuild)

**F1. "index 12 = the record's residue 12" is an orbit-stabilizer theorem, not a
numerical coincidence.** §3 asserts the round law's stabilizer is larger than
the arena's *"by exactly the index the record's residue has"*, and §4 calls the
residue *"an index the record offers and does not choose"*, with the head
carrying `DIRECTION-INDEX=12` and `SPLITTINGS=12` as two separate integers. I
tested whether the equality is structural. Measured: the orbit of the declared
splitting under Aut(link graph) has size **12** and equals the full set of 12
splittings (**the action is transitive**, 1 orbit); the stabilizer of the
declared splitting inside Aut(link graph) has order **108** and is *set-equal to
the arena automorphism group*; orbit–stabilizer gives 1296/108 = 12. So the two
12s are the same 12 by a theorem. **The paper under-claims here and can say so.**

**F2. The round law's stabilizer = Aut(link graph) is forced, and I verified it
by full enumeration rather than by pruned search.** §3 says the stabilizer *"was
computed by an exhaustive pruned search over the whole symmetric group"*. I
enumerated all **362,880** permutations of the nine actors with no pruning at
all and filtered twice, independently: permutations carrying the 27 admissible
groups to themselves → **1,296**; permutations carrying the 27 link edges to
themselves → **1,296**; and the two sets are **equal as sets**, not merely
equinumerous. Closed form cross-check: the link graph is K(3,3,3) (I verified
the three non-adjacency classes are exactly the three ANT lines, every degree
6), so Aut = S₃ ≀ S₃ = 6³·6 = 1,296. The identity is a theorem: the 27
admissible groups are exactly the transversals of the tripartition, so
preserving them is equivalent to preserving the non-adjacency relation.

---

## MAJOR FINDINGS

### M1 — Q58's nine arms are five inputs; the "5 recover" is one measurement recorded five times

**The measurement.** `r_reconstruct(bl)` reads its `blocks` argument and nothing
else — no schedule, no grammar, no history, no corpus label. I rebuilt all nine
arms' block sets independently and asked how many *distinct* sets the
reconstructor is ever handed:

| distinct block-set | size | arms handing it |
|---|---|---|
| the 27 triangles | 27 | **5**: THE-COMMITTED-GRAMMAR, THE-STRICT-COVER-DRIVER, THE-CONCATENATION-DRIVER, THE-DRIVEN-WINDOW, THE-PAIRWISE-LINKED-GROUPS |
| the unrestricted groups | 81 | 1 |
| the two-cell blocks | 54 | 1 |
| the emitted cells | 27 (singletons) | 1 |
| the site stars | 9 | 1 |

**Distinct inputs: 5.** Of the five *recovering* arms, distinct inputs: **1**.
Of the four *refusing* arms, distinct inputs: **4**. I confirmed the three
committed strata individually: `C1 blocks == the 27 triangles` True, `C2` True,
`C3` True, and the union over strata True. The five recovering rows of the
paper's §5 table are identical in every column (`3 | 27 | 27 x 3 | CERTIFIED |
yes`) because they are the same measurement.

**What this costs.** §5's sentence

> The class is not the committed schedule -- four mechanisms outside it recover
> the cast exactly, one of them with no grammar at all

is **not established by these arms**. Those four mechanisms write a record the
reconstructor cannot tell from the committed grammar's: the distinct-block-set
map erases exactly the thing that is supposed to vary. What was measured is that
*one record — the set of all 27 triangles — recovers the cast, and four other
block-sets refuse*. The criterion "triangularity with total cover" is therefore
tested at 5 points (1 positive, 4 negative), not 9 (5 positive, 4 negative);
`q58_split_is_triangularity` is true on both readings, but a criterion
separating 1 positive from 4 negatives is weaker evidence than one separating 5
from 4. The head's `ARMS=9; RECOVERING=5; REFUSING=4` and the LOG's *"9
in-corpus mechanisms through one reconstructor"* both read as nine independent
probes.

**Why no gate caught it.** `g_q58_arms` checks
`len({a["arm"] for a in arms}) == len(arms)` — distinct arm *names*. Nothing
measures distinct arm *inputs*.

**Exact repair.** (i) Add `q58_distinct_block_sets` and
`q58_distinct_recovering_inputs` to the receipt, measured as the cardinality of
`{frozenset(bl)}` over the arms and over the recovering arms; gate that the
former is reported. (ii) Add a `record` column to the §5 table naming the block
set, so the five identical rows are visibly one record. (iii) Reword §5 to:
*"Five in-corpus mechanisms — four schedules and one grammar-free rule — write
the same record, the 27 triangles, and the reconstructor recovers the cast from
it; four other block-sets refuse. The probe therefore has five distinct inputs,
one recovering and four refusing, and what the recovering mechanisms share is
that the reconstructor cannot tell them apart."* (iv) The head may keep
`ARMS=9` if it also carries `DISTINCT-INPUTS=5`. The Q58 verdict word
(IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS) survives; its evidential width does
not.

---

### M2 — the quotient row changes object between its columns; 97.7% of the "collapse" is the sort, not the group

**The measurement.** The census defines HISTORY as *"the distinct sequences of
events the committed drivers produce"*, and `quotient_histories = 5,784` counts
those sequences. But the orbit counts are taken after sorting the events:
`himg` returns `tuple(sorted(...))` over `F in H`, so the sequence is discarded
before any group acts. I measured the intermediate the unit does not report —
the image under the **identity** permutation:

| step | count |
|---|---|
| ordered histories (as the census defines HISTORY) | **5,784** |
| distinct event **multisets** (order forgotten, no group) | **136** |
| orbits of multisets under the arena's 108 | **25** |
| orbits of multisets under the link group's 1,296 | **17** |

So 5,784 → 136 is done by `sorted()`, and 136 → 25 / 17 is the group's actual
work. Under the **order-preserving** action — the one the census row's own
definition of HISTORY requires — I measured the honest orbit counts:

| object | before | modulo the arena | modulo the links |
|---|---|---|---|
| histories, order kept | 5,784 | **3,830** | **1,067** |

**What this costs.** §3's *"The histories collapse hard"*, the table row
`| histories | 5,784 | 25 | 17 |`, and the head's `HISTORIES-SURVIVING=17-OF-5784`
credit the automorphism groups with a 340-fold collapse of which the groups
supply 8-fold. The count-field row is unaffected — I verified `fimg` is a
genuine group action keyed by the image pair, and 36 → 12 / 12 reproduces
exactly under both groups, including the paper's real observation that the link
group's extra freedom merges no further count field.

**Why no gate caught it.** `g_quotient` checks only the monotone chain
`link <= arena <= before`, which is satisfied by a "before" of a different type.

**Exact repair.** Either (a) report the honest three-step chain
`5,784 → 136 → 25 / 17` with a new receipt leaf
`quotient_histories_event_multisets = 136` and a sentence in §3 saying the first
step forgets the order, or (b) use the order-preserving image and report
`5,784 → 3,830 / 1,067`. Under (a) the head becomes
`HISTORIES-SURVIVING=17-OF-136`; under (b) `17-OF-5784` becomes `1067-OF-5784`.
Route (a) is the smaller edit and keeps the striking numbers; route (b) is the
one that matches the census row's own definition of HISTORY. Whichever is taken,
`g_quotient` must gain a same-object predicate.

---

### M3 — "Born-menu values | 24" is not the Born menu, and the builder that would compute it is never called

**The measurement.** `b_born_menu` is defined at `contract_exact.py:449` and
appears at no other line in the module — a carried-not-used family, which the
era's TPL-2 items forbid. What the §2 table prints as `Born-menu values` is
`state_reading_a_menus = len({succ[n][1] for n in fields})`, the number of
distinct **post-coin amplitude vectors**. I computed the actual reading-A
emission weights (the Born weights `|z|²` of the post-coin amplitudes, i.e.
exactly what `b_born_menu` would return) over the 36 count fields:

| quantity | value |
|---|---|
| distinct Born-menu vectors over the 36 count fields | **4** |
| distinct post-coin amplitude vectors (what the paper prints) | 24 |
| the four Born-menu vectors, per site | site-uniform (9,9,9) ×12 fields; (3,3,21) ×8; (3,21,3) ×8; (21,3,3) ×8 |

The four values are forced: with ψ₀ uniform and C = G·diag(ω^n), a site whose
three residues are all equal or all distinct emits (9,9,9), and a site with
exactly two equal emits a permutation of (3,3,21).

**What this costs.** The §2 argument is stated as a contrast between the two
readings — *"the count field enters the quantum update only through its residue,
and enters the record menu whole"* — and the table's evidence for that is `24`
vs `36`. The conclusion **survives and in fact strengthens**: reading A's menu
sees 4 of the 36 fields, reading B's sees all 36, so the reading-relativity gap
is wider than reported. But the printed numeral is not the quantity its label
names, and `g_state_reading` cannot detect this because it only asserts
`state_reading_a_menus == record_residue_fields` (24 == 24), which follows from
the residue→successor injectivity I verified separately, not from the row being
a Born menu.

**Exact repair.** Call `b_born_menu` and add
`state_reading_a_born_values = 4`; either rename the existing row to
`post-coin state vectors` and add a `Born-menu values` row carrying 4, or
replace it. Extend `g_state_reading` to gate
`state_reading_a_born_values < state_reading_a_menus < state_reading_b_menus`.
§2 gains one sentence: *"the Born menu is coarser still — four values over the
thirty-six fields — so reading A's emission sees less than the residue does."*

---

## MINOR FINDINGS

**m1 — the census's `cardinality` column is not one type.** QUANTUM-STATE 27 is
a state-space dimension (one amplitude per cell), SEAM 4 is a kernel dimension
(the numbers a gluing must declare — I reproduced rank 6 on 10, kernel 4), TICK
1 is a scheduling convention. These are summed with genuine object counts (9
actors, 280 groupings, 5,784 histories) into `OBJECTS=23`. *Repair:* add a
`what the number counts` column, or rename the head field `CENSUS-ROWS=23`.

**m2 — `OBJECTS=23` is a row count, not an object count.** Extensionally the
table names ≤20 distinct sets (SITE=ACTOR, CO-DIVISION-PAIR=CELL,
CARRIER-CANDIDATE=CELL, each by its own reading column). *Repair:* keep the 23
rows and add one measured leaf `census_distinct_extents`, or say in §1 that
three rows are re-descriptions the weld and the carrier typing identify.

**m3 — the CARRIER-CANDIDATE row's two backings are one measurement at two
hops.** Settled in the panel-brief section above.

**m4 — the equal-residue half of the screening theorem is analytically forced.**
`b_coin_apply` indexes `B_WPOW[n[base+j] % B_Q]`, so equal residues give
byte-identical successors by construction. I probed this at 972 points (+3 on
each of the 27 cells of each of the 36 fields): **0 successors moved**.
`g_state_screens` asserts `equal-residue pairs 24 agreeing 24` as though it
could fail. The contentful half is the other one — **0 of 606** distinct-residue
collisions, which I reproduce, and which is equivalent to residue→successor
being injective on the 24 residue classes (verified: 24 classes, 24 distinct
successors, 0 classes with more than one successor). *Repair:* mark the
equal-residue half as forced-by-construction in §2, and let the gate carry the
0/606 as the measurement.

**m5 — the head's `CYCLE-LENGTH=3` is not §4's circle.** `dep_cycle_length` is
the minimum over all three cycles, which is the dynamical loop COUNT-FIELD →
QUANTUM-STATE → EMISSION → COUNT-FIELD (length 3). §4 narrates *"an actor makes
an event, an event makes a history, a history writes a record block, and the
record block hands the actor back"* — length **4**, carried separately as
`dep_actor_record_cycle_length`. I reproduced all three cycles: lengths 3, 4, 5;
two through both ACTOR and RECORD-BLOCK; shortest such 4. In a head segment
named `CONTRACT-CIRCULAR-CAST-…` the numeral 3 reads as the cast circle's
length. *Repair:* print `ACTOR-RECORD-CYCLE-LENGTH=4`.

**m6 — the verdict blocks mix measured and declared integers unmarked.**
`DEPENDENCY_EDGES` and `PARAMETER_ROWS` are author-written literal tables;
`DECLARATIONS=21; FREE=13; INVARIANT…=2; DERIVED=3;
RECONSTRUCTED-CONDITIONALLY=1; INITIAL=2` and `CYCLE-LENGTH` are counts of their
rows. They sit in the same fenced block as `LAW-STABILIZER=1296`,
`COIN-CLASSES=6` and `SEAM-KERNEL=4`, which are measured. I verified the tallies
are internally right (13+2+3+1+2 = 21; no FREE row carries YES). §6's *"The
verdict word follows from the count and not from a judgement"* is true of the
last step only — the judgement is in the table's authorship. *Repair:* one
sentence in §6, or a `DECLARED` marker on those head fields.

**m7 — `saturating` is an a=3 coincidence in the idiom.** The predicate is
`sum(round_vec) == NACT`: nine cells covered, nine actors. The general identity
is (n/a)·C(a,2) = n(a−1)/2, which equals n **only** at a = 3. Correct here — I
confirmed independently that the 36 saturating groupings are exactly the
partitions into link-triangles, and that the 27 admissible groups are the 3·3·3
transversals — but the idiom will mis-fire silently if the ARITY unit reuses it
at a = 2 or a = 4. *Repair:* state the predicate as "every group is a triangle",
or write the threshold as `len(parts)*C(arity,2)`. Worth routing to the ARITY
runner rather than repairing here.

**m8 — the cast search's exhaustiveness carries an ungated precondition.**
`r_cast_solutions` offers, for each token after the first, only pairs drawn from
the used labels plus **one** fresh label. That is complete only if every token
after the first shares a block with an already-assigned token, i.e. only if the
record's block hypergraph is connected — and the fallback `frontier = [t for t
in toks if t not in seen][:1]` reaches a disconnected token with the same
one-fresh-label menu. I measured the precondition (**1** connected component) and
re-ran my own search with two fresh labels permitted: **still exactly 1
solution, the same family, actor count 9**. So §4's *"searched exhaustively"*
stands at this corpus. *Repair:* gate `blocks_connected` as a stated hypothesis
of the search, so the claim does not silently travel to a record where it fails.

---

## THE CENSUS, RECOMPUTED — the 20 quantities and the 3 citations

Every value below was produced by my own constructors and compared to the
receipt leaf; all agree.

| quantity | K1 | unit |
|---|---|---|
| actors / sites | 9 | 9 |
| declared directions / parallel classes | 3 / 4 | 3 / 4 |
| cells (= co-division pairs, bijection verified) | 27 | 27 |
| division events (all 3-subsets) | 84 | 84 |
| realised events (27 triangles + 3 ANT lines) | 30 | 30 |
| groupings | **280** | 280 |
| admissible rounds (saturating) | **36** | 36 |
| I7-STRICT triples | **72** | 72 |
| G-FLAT quadruples | **276** | 276 |
| driven-window schedules | **600** | 600 |
| corpus slots = 72 + 5,184 + 600 | **5,856** | 5,856 |
| distinct histories | **5,784** | 5,784 |
| record blocks | **27** | 27 |
| unwritten event occurrences / partly-unwritten histories / silent histories | **768 / 175 / 1** | 768 / 175 / 1 |
| distinct bare records | **5,643** | 5,643 |
| collision classes / colliding / vanishing (5,784 − 141 = 5,643) | **39 / 180 / 141** | 39 / 180 / 141 |
| count fields | **36** | 36 |
| menu (coset partitions of the 6 translation subgroups) | 6 | 6 |
| namings = \|Aut(link graph)\| | 1,296 | 1,296 |
| direction splittings | 12 | 12 |
| coin classes / seam kernel | 6 / 4 | 6 / 4 |
| max blocks one history sees | 18 | 18 |
| CHART 16, TICK 1, CARRIER 27 (citations) | located verbatim | ✓ |

**State (residue theorem):** 36 count fields → 24 residue fields → 24 distinct
one-step successors; equal-residue pairs 24, agreeing 24; distinct-residue pairs
606, colliding 0; 24 + 606 = C(36,2) = 630. Record menu reads the counts whole:
36 values, falling to 24 if reduced to residues.

**Invariance:** \|S₉\| = 362,880 enumerated in full; law stabilizer 1,296 =
Aut(link graph) 1,296 (equal as sets); arena 108 = 9·12, a subgroup; index 12;
splittings 12 (one Aut-orbit, stabilizer = the arena group); direction sweep
4/4 across all 7 profile quantities — every one of the four declarations returns
`(27, 36, 72, 276, ((0,3),(2,54),(3,27)), 81, ((6,9),))`, and AID's own three
numerals (36 saturating, 72 strict, 276 flat) sit inside it; local-arity widths
10,077,696 / 124,416 / 144 / 4 / 1 / 1, global 1, collapse width 4, uniform over
all 72 C1 histories.

**Circularity:** 10 nodes, 12 edges, 3 simple cycles (lengths 3, 4, 5), 2
through both cast and record, shortest such 4; cast search with the actor count
free returns **exactly 1** family, actor count **9**, equal to the declared cast
as sets, and survives loosening the canonical labelling rule.

**Q58:** 9 arms, certificates CERTIFIED ×5, TOKEN-NOT-IN-EXACTLY-TWO ×2,
THRESHOLD-UNDETERMINED ×2; 5 recover, 4 refuse; the coupled walk's own emission
refuses at **both** grains; triangularity-with-total-cover decides 9/9 and block
size alone does not (the site-menu arm writes blocks of the declared arity and
still refuses) — subject to M1's grain caveat.

**Parameters:** 6 ring elements of norm 9 → 36 covariant unitary solutions → 6
classes up to a global phase → 1 is ±Grover; menu 6; seam 6 rows on 10 columns,
rank 6, kernel 4; direction choices 4.

---

## WHAT I DID NOT TEST

Batteries, mutants, falsifier move-proofs, the seal/transcript machinery, the
S-1 region disjointness proof, the wall patterns and their controls, and the
template's nine families are the K3 seat's object, not this one. Where I name a
gate above it is only to say why a finding survived the battery, not to grade
the battery. The `--render` diagnostic, the C1-only width sweep and the nine-arm
domain probe are disclosed residuals in §7 and I did not treat them as
undisclosed. I did not read the in-flight ARITY, AUTOGLUE or DISC materials.

**All rulings above are candidate until adjudication.**
