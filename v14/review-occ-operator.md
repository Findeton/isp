# K1 — OPERATOR-LENS HOSTILE REVIEW of paper-31 (OCC)

**Seat:** K1 OPERATOR (protocol: v14 ledger #256; HANDOFF-PROMPT.md §9).
**Object at 7ab2f21, hashes verified at open AND at close, unchanged:**
`v14/paper-31-occ.md` 1b140f7973d4 · `v14/code/occ_exact.py` e96c1e14a0b6 ·
`occ_output.txt` 63d98f4ee6f0 · `occ_receipt.json` 46e757ef9c47 · pin
`v14/note-occ-pin.md` 145db72ce547.  All 12 pinned sources re-hashed
independently and matching (paper-22 fb05cc2a376a, its receipt afa46ffaf651,
paper-19 50bb81e67942, paper-20 4824d190af73, coupling_exact 72e7b299f66e,
d42b1 576275d55ecf, d60 684cdb76552b, d66 3d0516ab106e,
r3_weld_receipt dfea664f2408, coupling_receipt 55273f6b6068,
r4c_multi_exact f202cf185804).

**Method.** Everything below was rebuilt from the definitions in a scratch
tree; the delivered instrument was never used as an oracle for any number.
The ring Z[ω] was implemented twice (integer-pair rule from ω²=−1−ω, and a
2×2 integer matrix representation) and cross-checked at 6,561 products with 0
mismatches.  The leak was measured by a **third** route of my own (explicit
sparse ordered tensor U⊗U, read entry by entry) beside the delivered two.
Interpreter `/opt/homebrew/bin/python3.13`; exact integer/Fraction arithmetic
throughout; no float.  Repo reads were read-only; the single repo write is
this file.

---

## VERDICT

**GRADE: AWF — ACCEPT WITH FIXES.**

The head `OCC-CEILING-OPEN` survives, and so does the unit's central
discovery: **the carrier is a pair of actors**.  I rebuilt the 27-cell
pair-carrier, the pool, the three theories, both leak censuses, both
theorems, the controls and the asymmetry rows from nothing, and **every
delivered numeral I could recompute reproduced exactly — zero false numbers.**
The instrument also reproduces BYTE-IDENTICAL off-tree in a provisioned
mirror (both artifacts, 63d98f4ee6f0 / 46e757ef9c47).

The fixes are not to the verdict.  They are to **three published statements
that say more than the measurement supports** and to **two gates that cannot
fail**.  One paper sentence is, read as written, FALSE at one of the six coin
classes; one published head-field NAME asserts a set equality that is false
by a factor of five; and the P3 blindness leg's inference is contradicted by
the instrument's own completions.

**Recomputations: 341** (independent rebuilds compared against a delivered
value), across 48 leak rows ×2 routes, 6 coins, 4 declarations, 7 census
layers, 8 verbatim anchors, 212 paper numerals, 3 control arenas, 2
off-harness mutants.

---

## WHAT REPRODUCED (the decisive targets)

**(1) The 27-cell PAIR-carrier identification — REPRODUCED, and the verbatim
coupling anchor is real.**  `v14/code/coupling_exact.py:761-766` carries the
anchor in the parent's own words ("the arena's 27 cells, indexed site-major.
Cell (x, l) IS the unordered co-division pair {x, x+l}"); I located all 8
verbatim anchors with my own normaliser and confirmed all 8 perturbations
fail to locate.  Rebuilt incidence: 27 cells ↔ 27 distinct unordered
co-division pairs (bijection per object); **every cell exactly 2 actors,
27/27**; **every actor exactly 6 cells, 9/9**; valence sets {2} and {6};
excitation→actor is NOT a function; ACTOR→SITE injective and surjective on 9.
Independent corroboration the unit does not take: of the 36 unordered actor
pairs, exactly the 9 in the undeclared fourth parallel class (1,2) are not
realised as cells — 27 + 9 = 36.

**(2) The P2 census — REPRODUCED exactly, including the positive control.**
My own scanner: A-COUPREC 418, A-W3REC 343, A-COUPSRC 2040, A-D42B1 433,
A-D60 372, A-D66 1339 = **4,945 names over the 6 committed layers, 0
occupancy-shaped**; the same scan on paper-22's receipt fires at **19**
(`occupancy`, `antisymmetric_hardcore_leak_cells`,
`one_excitation_configurations`, …).  Robustness: a deliberately WIDER name
reading (all arg kinds, lambdas, keywords, aliases, all string constants)
gives 5,416 names and still **0** occupancy-shaped in the deep arm, so the
zero is not an artefact of the declared reading.  AST leg: 102 FunctionDefs,
declared DIM = NCELL = 27 = the rebuild, 0 parameters matching the occupancy
vocabulary; and — a check the unit does not make — the parent contains no
product/pair state construction at all (8 single-excitation length-DIM
vectors, no `combinations`/`product` over cells).

**(3) The three theories — REPRODUCED.**  378/351, 351/351, 216/216, 378/351
from my own per-declaration predicate (actor load counted by summing the
excitation over BOTH of a cell's actors, not by a ceiling special case);
3 distinct two-excitation theories; the collapse D-ACTOR-2 ≡ D-CARRIER-2.
The one-excitation comparison count **53,460 = 6 coins × 6 declaration pairs
× (27 + 729 + 729)**, agreeing 53,460/53,460 when the restriction is built
*from the declaration* (my construction, not theirs).  The mathematical claim
is TRUE.  The delivered *gate* for it is not (see MAJOR-2).

**(4) The blindness pair and the completion fiber — numbers REPRODUCED.**
Site fields agree 9/9, cell occupations agree 25/27; completion totals
(2, 1, 1) so **2 of 3 preserve the parent identity**; pairwise field
differences (3, 9, 9); the doubly occupied carrier's menu is nonempty
(weight 228) and — measured PER COMPLETION, which the delivered loop does not
do — **0 of 3 refuse a division**.  The numbers stand; the inference drawn
from the blindness leg does not (MAJOR-3).

**(5) The P4 leak censuses at both grains — REPRODUCED at every row.**
Carrier grain: symmetric **81** cells at exactly the 5 non-monomial classes,
0 at the monomial one; antisymmetric **0**.  Actor grain: both shapes leak at
**6 of 6**; **864** leak cells at each non-monomial class and **81** at the
monomial one; admissible 216, forbidden 135 (antisym) / 162 (sym).  Paper-22's
theorem transports per coin in both directions (leaks ⟺ non-monomial, 6/6).
Parent split recomputed from paper-22's own receipt rows: 64 generators,
**48 leaking / 16 closed**, antisymmetric leaking **0**, and its
`ceiling_is_anchored` is False.

**(6) THE TWO THEOREMS — both REPRODUCED as mathematics.**
*Leak-set coincidence:* at the actor grain the two shapes' source sets,
target sets and counts coincide at **6/6** coins, with **0** cancellation
cells.  I confirmed the mechanism independently: two target cells' row
supports are the cell triples of two base sites, so a source pair feeding
both products must lie inside one triple and therefore shares an actor —
which the actor-grain declaration has already excluded.  Direct check: 0
targets whose row supports overlap in a pair of cells not sharing an actor.
*Grain unification:* the carrier-grain leak's source set is a **set equality
at 5/5 leaking coins** — but with the **same-SITE** set (27), not the
same-actor set (135).  See MAJOR-1.

**(7) The control arms — C1 and C2 rebuilt end to end.**  Control generator
(2/n)J − I at n = 9: 0 unitarity defects, every entry nonzero.
C1-SUBSET: sym adm 36 / forb 9 / leak **324** (open), anti adm 36 / forb 0 /
closed → exactly one shape closes → head law returns **OCC-CEILING-FORCED**.
C2-MULTISET: sym adm 45 / forb 0 / closed, anti closed → nothing selected →
**OCC-CEILING-OPEN**.  C3-ONE-CARRIER: both sector dimensions 0 → not posable
→ **OCC-BLOCKED-AT**.  With the two declared-exclusion arenas returning
**OCC-CEILING-PARTIAL**, the head law returns **4 distinct pre-registered
words over the 6 arenas**.  The two-way control is genuine.

**(8) The asymmetry rows — REPRODUCED.**  Permission selects at **0 of 12**;
exclusion at **5 of 12**; carrier grain 5 of 6, **actor grain 0 of 6**, and at
all 6 actor-grain rows the reason is that no shape closes.  The only shape
ever selected is ANTISYMMETRIC.

**(9) The 48 leak rows — a THIRD route agrees.**  I built the ordered
729×729 tensor U⊗U explicitly as a sparse object and read the sector element
off it; **48 of 48** rows agree with my route-1 census and with the delivered
pair.  Cancellation census recomputed: **405** both-products-nonzero cells in
the whole run, all of them at carrier-grain SYMMETRIC (81 at each of the 5
non-monomial coins), and **0** at the actor grain — which is exactly the
theorem.

**(10) Off-harness mutants and the numeral sweep.**  Both mutants below.
My own reimplementation of the paper sweep finds exactly **212 numerals
(144 prose / 58 fenced across 3 blocks / 10 inline across 39 spans) and 0
unlicensed** — and, a stronger result than the gate claims: every one of the
212 is licensed by a MEASURED INTEGER or a structural numeral.  The licensed
set is 109 values including digits typed inside receipt prose but only 71
from integer values; **0 of the paper's numerals depend on the prose-only
38**, so the known softness in `licensed_numerals` is not exercised here.
Head/paper agreement: the 3 fenced blocks equal the 3 derived segments as a
MULTISET and each occurs exactly once.

---

## FINDINGS

### MAJOR-1 — the grain-unification set equality is with the SAME-SITE set (27), not the same-actor set (135); the published field name and two paper sentences assert the false one

**Measured (mine).**  Configurations whose two cells **share an actor**: 135.
Configurations whose two cells sit at the **same base site**: 27.  The second
is a proper subset of the first.  The carrier-grain leak source set equals the
**27** at 5 of 5 leaking coins and equals the **135** at **0 of 5**.

The instrument knows this — `build_census` computes both sets and gates
`r_carrier["source_set"] == same_site_cfgs` (occ_exact.py:1479-1481) — but
publishes the result under the key
`carrier_grain_sources_are_the_same_actor_configurations`, and the head field
is `CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-ACTOR-CONFIGURATIONS=5-OF-5`.
The paper states it twice as a definite description:

- §6: "The configurations that leak are exactly the 27 whose two excitations
  sit on cells sharing an actor, by set equality at 5 of 5 leaking coin
  classes."
- §9: the same sentence, verbatim, as a decided result.

Read as written, "the 27 whose two excitations sit on cells sharing an actor"
denotes a set with **135** members.  It is also internally inconsistent with
the paper's own "every one of the **135** forbidden configurations is
reached", since the actor-grain forbidden set IS the share-an-actor set.
The gate text repeats the error ("that set IS the set of configurations whose
two excitations sit at one actor"; failure message "not the same-actor set").

**This does not damage the physics.**  The true statement — which the paper's
own mechanism paragraph gets right — is the containment: every carrier-grain
leak source is a configuration the actor-grain declaration forbids (27 ⊂ 135),
and the set equality is with the 27 same-base-site configurations.

**Exact repair.**
1. Rename the receipt key to
   `carrier_grain_sources_are_the_same_site_configurations` and the head field
   to `CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-SITE-CONFIGURATIONS=5-OF-5`.
2. §6 and §9: "…are exactly the **27 whose two excitations sit on two of the
   three cells based at one actor** — a set equality at 5 of 5 leaking coin
   classes — and every one of them is among the 135 configurations the
   actor-grain declaration forbids."
3. Add the containment as its own gated row (`27 ⊂ 135`, element for element)
   so the two numbers can never again be confused, and fix the G-P4-SET-EQUALITY
   gate statement and failure message.

### MAJOR-2 — the 53,460-comparison agreement gate cannot fail: the compared object is built without ever consulting the declaration

`one_excitation_object(W)` (occ_exact.py:690-700) takes only the walk
operator.  In `p2_fiber` the loop is

```
for did in DECLARATION_IDS:
    objs[did] = one_excitation_object(W)
```

so all four "restrictions" are the same object by construction and the
53,460 comparisons are a comparison of a thing with itself.

**Mutant K1-M1 (outside the harness).**  I imported the delivered module in
the mirror and replaced D-ACTOR-1's ceiling by **0**, whose true
one-excitation restriction is the EMPTY configuration set while the other
three have 27 cells.  Result: `comparisons=53460, disagreements=0,
restrictions_agree_as_objects=True` — **unchanged**.  The gate is blind to
the declaration it claims to be quantifying over.

The claim itself is TRUE — I built the restriction *from* each declaration
and got 53,460/53,460 agreement — so nothing published is false.  But the
number is a headline in the verdict block
(`P2-ONE-EXCITATION-RESTRICTIONS-AGREE=53460-OF-53460`) and one of P2's three
derivation legs, and it is carried by a gate that no perturbation of a
declaration can move.  Under #34-with-reachability and the era's
"gates bind objects" rule this is the wrong kind of support for a load-bearing
number.

**A second, smaller defect in the same neighbourhood:**
`admissible_configs` implements the ACTOR grain as the hard-coded special
case `if grain == "ACTOR" and ceiling == 1`, so a declaration is not a
parameter of the constructor.  At ceiling 0 the delivered constructor admits
351 symmetric configurations (it should admit 0) — visible in the mutant
output above.  The four declared declarations are unaffected: my
load-based predicate reproduces 378/351/216/378 exactly.

**Exact repair.**
1. `one_excitation_object(W, grain, ceiling)`: build the configuration set as
   `[c for c in range(NCELL) if the declaration admits one excitation on c]`,
   and restrict the matrix and Born shadow to it.  The published numbers do
   not change; the gate becomes falsifiable.
2. Register a mutant that moves one declaration's ceiling to 0 and require it
   to die at G-P2-INVISIBLE-FROM-BELOW.
3. Rewrite `admissible_configs` to evaluate the declaration's predicate
   (max occupancy at the declared grain ≤ ceiling) instead of branching on
   `ceiling == 1`.

### MAJOR-3 — the P3 blindness leg measures the pre-step occupation field, which is not what the committed emission rule reads; its conclusion is contradicted by the unit's own completions

The paper (§5): "the committed emission rule reads a site field, and the two
states agree on it at 9 of 9 sites … The rule cannot tell a doubly occupied
carrier from two singly occupied ones sitting at one actor, so **nothing it
computes can depend on which it is**."

The committed rule is `emission_weights(reading, Jn, n, den)`
(coupling_exact.py:1419-1440) with `Jn = [absq(post[m])]`, the **post-step**
Born vector, and `k = qrow/M` from `law_transport_at`:

- **reading A (the Born menu)** — `qrow = [Jn[b+i]/den]` — is a **per-cell**
  read; in fact `wts[b+i] == Jn[b+i]/den` identically.  The parent's coupled
  ensemble runs exactly this (`emission_weights("A", Jn, nn, den)`,
  coupling_exact.py:1860).
- **reading B (the record menu)** — `qrow = [n[b+i]]` — is record-side, and
  the state enters only through the site sum.

The reading is a **DECLARED FIBER OF 2** in the parent (`F10-EMISSION-READING`,
"the Born menu against the record menu; both run"), and OCC declares neither.

**Measured (mine), three ways:**
1. On the blindness pair's own per-cell fields at site 0, reading A gives
   k(P) = (1/2, 1/2, 0) and k(Q) = (1, 0, 0) — **separated**; reading B gives
   (1/3,1/3,1/3) for both — blind.  The claim is the reading-B claim.
2. Even under reading B the rule reads the **post-step** field: the two
   states' normalised post-step **site** fields agree at only **6 of 9**
   sites (and their post-step cell fields at 24 of 27).  The pre-step 9/9
   agreement the gate measures is not the rule's input under either reading.
3. **The unit's own three completions separate the pair**: E1 and E2 differ at
   3 of 27 cells and E3 at 9 of 27 between P and Q.  The instrument that
   asserts "nothing it computes can depend on which it is" computes three
   things that do.

**Consequence, bounded.**  P3's word survives on its other two legs — the
grammar has no occupancy vocabulary, and 0 of 3 completions refuse a division
to a doubly occupied carrier (I verified the latter per completion, which the
delivered loop does not: `refusals = sum(1 for cid, field, _why in
completions if sum(qocc) == 0)` ignores its loop variable, so the "3" is a
fiber size and not a per-object measurement).  The head is unaffected: on the
verdict arena `head_law` returns OPEN on P2 before P3 is consulted.  What
fails is the *reason* given for P3, and one sentence of the paper.

**Exact repair.**
1. §5: replace "the committed emission rule reads a site field" with the
   measured, reading-scoped statement: "under the record-menu reading the
   state enters the committed emission rule only through the site sum of the
   Born weights; under the Born-menu reading — the one the coupled ensemble
   runs — it enters per cell."  Delete "so nothing it computes can depend on
   which it is."
2. Replace the inference by what actually carries P3: the grammar has **no
   occupancy coordinate to condition on** (P2's census), and none of the three
   completions refuses the division.  That is enough for
   SILENT-AND-VACUOUSLY-SATISFIED and it is measured.
3. Add the emission reading to the choice inventory as a **declared fiber of
   2 inherited from the parent**, and gate the blindness statement per reading
   (it holds for B, fails for A) — §15, match every coordinate.
4. Make the refusal census per completion (evaluate each completion's field
   on the doubly occupied state), so the published 0-of-3 is a per-object read.

### MAJOR-4 — "every one of the 216 admissible configurations leaks" is false at the monomial coin class; the head publishes a MAX as a universal

`R["leaks"]["actor_grain_sources_leaking"]` and `..._targets_reached` are
`max(...)` over the pool (occ_exact.py:2721-2724).  The head renders them as
`ACTOR-GRAIN-SOURCES-LEAKING=216-OF-216` and
`ACTOR-GRAIN-TARGETS-REACHED=135-OF-135`.

**Measured (mine), per coin — and the delivered receipt's own per-coin rows
agree with me:**

| coin | monomial | leaking sources | targets reached |
|---|---|---|---|
| K-2-1w, K-2+0w, K-1-1w, K-1+1w, K+0+1w | no | 216 of 216 | 135 of 135 |
| **K+0+0w** | **yes** | **81 of 216** | **81 of 135** |

So the paper's §6 "Measured: at the actor's grain both shapes leak at 6 of 6
coin classes, **every one of the 216 admissible configurations leaks, and
every one of the 135 forbidden configurations is reached**" is false at 1 of
the 6 classes — and §6 says so itself two sentences later ("even the
deterministic shift carries 81 admissible configurations into forbidden
ones").  §9's decided-bullet repeats the universal with **no** caveat.

No gate binds these per-coin counts; only `closed == (leak_cells == 0)` is
bound per row (G-P4-GRAIN-CENSUS).  This is the #87 violation the era names:
an aggregate standing where a per-object predicate belongs.

**Exact repair.**
1. Publish per-coin: `actor_grain_sources_leaking_min/max` (81/216) and
   `..._coins_at_full_leak = 5 of 6`, and change the head fields to
   `ACTOR-GRAIN-COINS-WHERE-EVERY-ADMISSIBLE-SOURCE-LEAKS=5-OF-6` and
   `ACTOR-GRAIN-COINS-WHERE-EVERY-FORBIDDEN-TARGET-IS-REACHED=5-OF-6`.
2. §6 and §9: "at the 5 non-monomial classes every one of the 216 admissible
   configurations leaks and every one of the 135 forbidden configurations is
   reached; at the monomial class 81 of 216 leak and 81 of 135 are reached —
   the failure is total at every class, and complete at five of them."
3. Add a gate binding, per coin, `leaking_sources == admissible` ⟺ non-monomial,
   with the monomial row carrying its own 81/216 predicate.

### MINOR-1 — two P1 fields are typed constants, and "9 of 27" is a cross-type comparison
`p1_carrier` returns `"actor_leg_covers_the_carrier": False` and
`"actor_leg_image_in_the_carrier": 9` as literals (occ_exact.py:742-743);
the head publishes `ACTOR-LEG-COVERS-OF-THE-CARRIER=9-OF-27`.  The era rule is
"counts computed, never typed."  There is also no map from sites into cells,
so "covers 9 of the 27" is a cardinality comparison of two different kinds of
object dressed as a covering.  *Repair:* compute both cardinalities
(`len(set(actor_site.values()))` and `NCELL`) and rename to
`ACTOR-LEG-IMAGE-CARDINALITY-AGAINST-THE-CARRIER=9-VS-27`, with one sentence
saying the two sets are of different type.

### MINOR-2 — the G-P2-STATE-SPACE gate asserts a third measurement it does not take
Its statement and the paper's §4 both say "no constructor in it is indexed by
anything but a cell", but `p2_state_space` measures only `dims`, the function
count and the occupancy-token parameter list; `two_excitation_constructor_present`
is literally `bool(excitation_params)`.  The claim is TRUE (I checked: the
parent builds 8 single-excitation length-DIM vectors and no product/pair
object anywhere), but it is asserted, not measured.  *Repair:* census every
sequence constructor in the parent's AST whose declared length is DIM/NCELL
and require the set of state-carrying constructors to be exactly those — or
delete the clause from both the gate and §4.

### MINOR-3 — the carrier-grain antisymmetric 0 is vacuous, and one per-coin predicate is vacuously True
At D-CARRIER-1 the antisymmetric universe has **no** forbidden configuration
(forbidden set size 0 at every coin), so `CARRIER-GRAIN-ANTISYMMETRIC-LEAK-CELLS=0`
is a leak out of an empty set.  The paper discloses this ("the wedge has no
doubly occupied configuration to leak into at all"), which is why this is
MINOR — but the head field sits beside the 81 and invites the dynamical
reading.  Likewise `carrier_grain_sources_share_an_actor` is `all(...)` over
an empty source set at the monomial coin and publishes True.  *Repair:* stamp
both rows `VACUOUS-AT-THIS-DECLARATION` / `N/A` in the receipt and add
"(vacuously — the wedge has no such configuration)" to the head field's
rendering.

### MINOR-4 — P3's verdict word is a typed constant
`p3_closure` returns `"verdict": "SILENT-AND-VACUOUSLY-SATISFIED"` as a
literal, while P1's, P2's and P4's words are all derived from their legs.  The
paper's §10 says "no load-bearing verdict is a typed constant beside a stamp"
and then names only the turning premise.  P3's word is consumed by `head_law`
(it is a conjunct of the FORCED branch), so it is load-bearing on the control
arenas even though the verdict arena short-circuits before it.  *Repair:*
derive it from the three legs (blindness-per-reading, completions, refusals)
and gate the published word against the derivation, as P2 already does.

### MINOR-5 — `licensed_numerals` licenses digits typed in receipt prose
The licensed set walks every string in the receipt, so a numeral typed into a
gate statement licenses a paper numeral.  Measured: 109 licensed values with
prose, 71 from integers alone.  **In this delivery it costs nothing** — all
212 paper numerals are licensed by measured integers or structural numerals,
0 by the prose-only 38.  *Repair (cheap, and it locks the property in):*
license from integer-valued receipt paths only, and re-run.

---

## NOT IN MY LANE
The walls, the seal manifest, the 50 declared mutants, the CLI contract, the
falsifier-honesty registry and the description stamps are K3's; I exercised
only the two off-harness mutants above and the byte-reproduction.  The head's
licensure as a two-coordinate declaration, the MISTYPED-NOT-FALSE ruling and
the LOR convergence are K2's.

## RESIDUAL RISK IF THE FIXES ARE TAKEN
None to the verdict word.  MAJOR-1 and MAJOR-4 change **names and
quantifiers, not numbers**.  MAJOR-2 changes a gate, not a value.  MAJOR-3
removes one sentence and re-grounds P3 on the two legs that already carry it.
After the repairs the unit's four decided claims — the pair carrier, the
absent occupancy coordinate, the two-grain ceiling, and the coincidence
theorem — all stand on measurements I reproduced independently.

**Objects re-hashed at close and unchanged:** 1b140f7973d4 / e96c1e14a0b6 /
63d98f4ee6f0 / 46e757ef9c47; pin 145db72ce547.
