# PER-R (paper-29) — EFFECTUS-LENS HOSTILE REVIEW (seat K2)

**Reviewer:** K2, the effectus lens (what the unit's results *license*).
**Date:** 2026-08-12, v14 ledger row for #281's panel.
**Object at 442b3fe** — hashes verified at open and at close, sha256-12:

| artifact | declared | measured |
|---|---|---|
| `v14/paper-29-perr.md` | 7d1d6ca3c5bc | **7d1d6ca3c5bc** |
| `v14/code/perr_exact.py` | d2f8fdac143d | **d2f8fdac143d** |
| `v14/code/perr_output.txt` | 6dad652f81fe | **6dad652f81fe** |
| `v14/code/perr_receipt.json` | ac424c8a7bdd | **ac424c8a7bdd** |
| `v14/note-perr-pin.md` (pin, frozen) | 6339ba42f354 | **6339ba42f354** |

**GRADE: AWF (accept with fixes).**

**210 distinct published quantities recomputed from a from-scratch
reconstruction of the arena built out of I7's own `links_d2` — no line of
`perr_exact.py` reused — and ZERO disagreed** (the count is conservative; the
per-section tally in §0 exceeds it). A further **75** recomputations were
taken *outside* the delivered surface (the R = 6 covering census, seven
unpublished DIA rows, the live-only floors and their witness, the full R = 6
homogeneous census); three of them are PROMOTIONS for the unit and one is a
routing finding against a sibling.

**No computed number in this unit is wrong.** Five of the six MAJORs below are
about what the numbers are *allowed to say*, not about the numbers; the sixth
is a surviving injection. Two (M1, M2) change the head; three make the paper
stronger once repaired; one (M6) is template-shaped and belongs in the disease
list.

---

## 0. What was actually run

An independent arena was rebuilt from I7's committed receipt
(`v13/code/ha_successor_receipt.json`): 9 sites = Z_3^2, the three declared
links (1,0), (0,1), (1,1), the 27 cells as the pairs {s, s+d}, a round as a
partition of the 9 sites into three triples, a site code as the indicator of
its three declared partners. That reconstruction reproduces, exactly and
independently:

- the arena: **280** partitions, spectrum **{0:1, 4:27, 6:54, 7:162, 9:36}**,
  **36** saturating, **2,520** translation pairs at 0 mismatches, the
  **7**-code alphabet realised identically at all 9 sites;
- the code space **54 / 105 / 181 / 287** at R = 3/4/5/6;
- the class split **44 = 41 + 3 + 0** at R = 4 (breaking codes (1,1,4),
  (1,4,1), (4,1,1)) and **90 = 84 + 3 + 3** at R = 5, indefinite at
  (1,1,5), (1,5,1), (5,1,1), every one at **4det = −5**;
- the covering-class census **1 / 7 / 32** codes, max cell **1 / 2 / 4**,
  4det support **{3} / {3,4,7} / {0,3,4,7,8,11,12,15}**, non-posdef at R = 5
  exactly the three singular codes and **no indefinite code** — i.e. the
  locking theorem's conclusion re-derived by direct search rather than by the
  counting argument;
- the locking mechanism at each of the three links: **70** locked partitions,
  **70** distinct masks, **7** required distinct third members against 5
  rounds, best coverage **25 of 27** — *min uncovered 2*, which is
  **numerically identical to SIG's independently measured R = 5
  non-attainment** (#272: branch-and-bound + union-closure DP, "min uncovered
  2"). Two units, two instruments, one number;
- the singular witness re-summed round by round from the receipt's own five
  groupings: incidences **[7,7,9,9,9] = 41**, covering **True**, max cell
  **4**, **3 of 5** rounds saturating, all nine site codes identical to the
  receipt's, exactly **1 of 9** sites non-posdef at (1,1,4), 4det **0**;
- the saturating stratum: **72** at R = 3, **9,936** at R = 4 with
  **276/276/276**, and at R = 5 **60,466,176** total, **619,092** distinct
  fields, **1,842,120** covering, homogeneous **680/1350/680/1350/1350/680**;
- the R = 6 door by meet-in-the-middle: **(2,2,2) 48,600**, **(1,1,4) 1,350**,
  **(1,2,3) 4,020**, **(3,2,1) 4,020**;
- the whole parity apparatus: box **432 → 361** admissible, **181** even /
  **180** odd, **9 of 9** declared records even-summed, all nine budgets and
  all nine classes of §3.5, the **6** admissible points at count sum 5;
- **all thirteen DIA rows** — every witness count, every multiset count, every
  compulsory class — and the law 13/13 with the count clause alone falsified
  at (2,2,2);
- d66's committed rows **(66, 12, 18)** and **(102, 18, 30)**, and all eight
  paper-21 back-validation anchors read from that unit's committed receipt.

The delivered code was also executed (`--no-write`, green, repo untouched) and
hostile-injected against the paper (§7 below).

---

## 1. THE LICENSED CLAIM

What this unit has earned, stated as it may be stated:

> **At R = 5 the covering class stops being the positive-definite class.** The
> singular boundary is reachable inside the covering class at a named,
> round-by-round witness carrying I7's own `G-SINGULAR` code at exactly one of
> nine sites; the indefinite region, which opens in the code space here for
> the first time, is not — and its unreachability is a **theorem with an
> integer witness**: a cell at count R locks two sites, the cells at those two
> sites demand seven distinct third members, and five rounds supply five.
> Independently: the direct search over the covering class returns max cell 4,
> so no covering quintuple carries a 5.

> **The identity that broke was never a law.** `cover = posdef` held at R = 3
> and R = 4 as an *arithmetic corollary* of the covering class's cell ceiling
> (1, then 2) — every breaking code needs a cell at 4 — and the ceiling is a
> budget-dependent quantity, measured 1, 2, 4 here and **5 at R = 6** (this
> review). What R = 5 discovers is not that a law failed but that a
> small-budget coincidence expired at the budget its own mechanism predicted.
> The licensed verb for the row is **BREAKS**, and the licensed *reading* is
> "the ceiling rose"; the identity row is that row's corollary, not a second
> break.

> **The parity observation is a fact about a closed declared list, and one
> forward-checkable consequence follows from it.** All nine of I7's declared
> homogeneous records have an even count sum — equivalently, integral q₁₂ — so
> by the ladder law **every odd budget of this ladder is declared-record-
> empty**, which is prediction (a) at R = 5 and at every odd rung above it. It
> is *not* a theorem about I7's construction and it constrains no future
> declaration; the unit says so itself (S-4, and the standing "may not be
> inherited" row).

> **The DIA ruling stands and is stronger than delivered.** A parallel class is
> compulsory exactly when the record counts its link more than once *and*
> counts some link exactly once; the count clause alone is falsified at the
> link-constant record. Verified 13/13 as delivered and **20/20** with the
> seven rows this review added — including **(1,1,1) at R = 3, the ladder's
> *other* link-constant record, where no class is compulsory either.** So
> "compulsion is carried by the scarce link and vanishes exactly where the
> weld turns motivated" is licensed **at both link-constant records of the
> ladder**, not at one.

> **The grammar drives R = 5 and R = 6.** 19 of 19 driven fields equal their
> groupings' field, anchored at d66's own committed R = 4 and R = 6 rows. This
> closes the **first** conjunct of paper-21's S-1 and only the first.

What is **not** licensed, and is claimed or implied:

1. that the "structurally live" floors 6 and 7 belong to the class the paper
   defines (M1);
2. that the rung carries **three** breaks (M2);
3. that 36/3/1 is a fiber *of the arena* (M3);
4. that the record floors at R = 6 and R = 8 are established by the
   1,721,036,800,000-quintuple census the head stamps them with (M4).

---

## 2. MAJOR FINDINGS

### MAJOR 1 — THE THIRD CLASS OF THE LADDER IS DEFINED AS ONE CLASS AND COMPUTED AS ANOTHER. The floors 6 and 7 are right; the printed definition gives 4 and 5.

**Decisive, and it lands on the SIG feed.** §3.6 defines the class:

> a STRUCTURALLY LIVE RECORD carries no foreign pair, so every one of its
> rounds saturates

The instrument computes that column as `covering_with_code(c, r, alpha,
live_only=True)` (code line 1956) — which requires the union to reach
`FULLMASK` **and** restricts the pool to saturating partitions. The class
computed is **live ∧ covering**; the class defined is **live**.

Measured, by the independent reconstruction:

| class as printed in §3.6 | SINGULAR floor | INDEFINITE floor |
|---|---|---|
| live only (the paper's words) | **4** | **5** |
| live ∧ covering (what the code computes) | **6** | **7** |

The delivered 6 and 7 are correct for live ∧ covering — reproduced here
independently. Under the paper's own words they are wrong by two rungs.

This is not a wording quibble, because §3.7 turns the class into an
operational instruction for the consumer:

> one run over structurally live records at R = 5 can see neither

**That sentence is false under the paper's own definition, and here is the
witness.** Five saturating partitions (no foreign pair anywhere, 45
incidences, every round at 9):

```
((0,0),(1,0),(1,1)) ((0,1),(0,2),(1,2)) ((2,0),(2,1),(2,2))
((0,0),(0,1),(1,1)) ((0,2),(1,0),(1,2)) ((2,0),(2,1),(2,2))
((0,0),(1,1),(2,2)) ((0,1),(0,2),(1,2)) ((1,0),(2,0),(2,1))
((0,0),(1,1),(2,2)) ((0,1),(0,2),(2,1)) ((1,0),(1,2),(2,0))
((0,0),(0,2),(2,2)) ((0,1),(1,1),(1,2)) ((1,0),(2,0),(2,1))
```

site code at the origin **(1,1,4)**, 4det **0** — I7's own `G-SINGULAR` code,
**SINGULAR, at R = 5, on a structurally live record**. (It covers 23 of 27
cells, which is exactly why the covering condition is the one doing the work.)

The irony is exact: this table exists *because* of the #270 advisory about
class substitution, and the class substitution recurs one level inside it.

**REPAIR (exact).** In §3.6 replace the third definition with:

> a STRUCTURALLY LIVE RECORD is a COVERING record that also carries no foreign
> pair, so every one of its rounds saturates

and add one sentence after "the nesting is checked rather than assumed":

> The four classes are CUMULATIVE — each adds its condition to the one before
> it — which is why the nesting is a check and not a coincidence. Dropped to
> live alone, without the covering condition, the floors are 4 and 5, at
> records that cover 23 of the 27 cells.

Add the live-only pair to §3.6 as a fifth measured row or as a deviation, and
re-stamp §3.7's last sentence as "one run over structurally live COVERING
records at R = 5 can see neither."

### MAJOR 2 — THE PERSISTENCE TALLY COUNTS ONE MECHANISM TWICE AND ONE THEOREM AS A DISCOVERY. "3 BREAKS" is not three breaks.

§11.1's tally — **3 BREAKS / 4 PERSISTS / 1 TRANSFORMS** — is arithmetically
right as a count of re-measured propositions and wrong as a count of
independent content. The three BREAKS rows are:

| row | status |
|---|---|
| block quantisation, cell ceiling 2 → 4 | the **mechanism**; genuinely new |
| cover = positive definite, True → False | a **corollary** of the row above plus arithmetic: every breaking code needs a cell at 4 |
| the declared-record yield, 276 → 0 | **forced by this unit's own parity law**: every declared record has an even count sum, R = 5 is odd |

The paper already knows the second — §11's "And with it the identity that
mechanism protected", and §5.2's "the covering class grows and stops being a
positive-definite class in the same step". It also already knows the third: it
*is* prediction (a), which the same head counts a second time as a passed
prediction. So the unit's two headline
tallies — "3 of 3 predictions pass" and "3 breaks" — share a row.

**REPAIR (exact).** Add a fourth column to §11.1, `independence`, with the
values `MECHANISM`, `COROLLARY OF ROW 6`, `FORCED BY §4.1's PARITY LAW`, and
replace the sentence "Read out. The three breaks are the content of the rung."
with:

> Read out. **One mechanism breaks** — the covering class's cell ceiling, 2 to
> 4 — and it carries the identity that depended on it; the third row is not a
> discovery but this unit's own parity law seen from the other side, since a
> declared record cannot occur at an odd budget at all.

The tally string in the head is then still 3/4/1 but the paper no longer
reads it as three findings.

### MAJOR 3 — THE PUBLISHED WELD FIBERS 3 AND 1 ARE BASE-MAP-RELATIVE, AND THE PARENT'S DISCLOSURE OF THAT WAS DROPPED.

The receipt measures, at every R = 4, R = 5 and R = 6 non-link-constant
arena, `fibers_base_map_invariant: false`, `label_fiber_spread: [3, 6]`,
`orient_fiber_spread: [1, 2]`. Paper-21 discloses this twice — in prose
(§4.5) and in its own inventory:

> | 11 | `I-DIRECTION-LABEL` | **measured** | **3** | §4.5, at the forced base map; spread [3, 6] across the 1296 — not base-map invariant |
> | 12 | `I-ORIENT` | **measured** | **1** | §4.5, at the forced base map; spread [1, 2] across the 1296 — not base-map invariant |

PER-R's rows 11 and 12 read `§6` and `§6`. The stamp is gone, while the
headline persistence row — "the weld fiber signature | 36/3/1 | 36/3/1 |
PERSISTS" — is a claim about precisely those base-map-relative numbers.

**REPAIR (exact), and it STRENGTHENS the row.** Restore the parent's two
"where it binds" cells verbatim (the measured spreads here are *identical* to
the parent's), and add to §6:

> The label and orient fibers are read at the forced base map and are not
> base-map invariant: across the 1296 they take 3 and 6, and 1 and 2. What
> persists from R = 4 to R = 5 is therefore not only the headline 36/3/1 but
> **the whole spread**, [3, 6] and [1, 2], unchanged — a stronger persistence
> statement than the one the table makes.

### MAJOR 4 — THE HEAD'S SCOPE STAMP COVERS TWO CLAIMS THE NAMED CENSUS CANNOT REACH.

Segment 1 ends:

```
RECORD FLOORS: G-SINGULAR R=6, G-INDEF R=8@EXHAUSTIVE-OVER-1,721,036,800,000-ORDERED-GROUPING-QUINTUPLES
```

1,721,036,800,000 = 280⁵ is the **R = 5** family. The two record floors are at
R = 6 and R = 8 and are established by the ladder law (§4.2 arithmetic) plus,
at R = 6, a sextuple census — not by any quintuple. The body attributes them
correctly ("by the ladder law of §4.2"); the head's stamp does not. Under
RUNBOOK §15 the stamp *is* the license.

**REPAIR (exact).** Split the stamp:

```
... COVER=POSDEF BREAKS AT R=5 AFTER HOLDING AT R=3 AND R=4@EXHAUSTIVE-OVER-1,721,036,800,000-ORDERED-GROUPING-QUINTUPLES -- RECORD FLOORS (BY THE LADDER LAW, THE R=6 ROW CENSUSED OVER 36^6): G-SINGULAR R=6, G-INDEF R=8
```

### MAJOR 5 — A DECLARED CHOICE THE PARENT ITEMISED IS MADE HERE AND ABSORBED INTO ANOTHER ROW.

`canon_transversals` is documented in this unit's own code as **"THE DECLARED
SEED MENU of a grouping"** (three options); `class_schedule` fixes option 0
for all six W5-LADDER schedules and both W6-DOOR schedules, and W5-SEEDFAN
varies it 3 × 3 on the first two rounds of one record only. Paper-21 carries
this as its own inventory row:

> | 8 | the seed menu: one canonical transversal, plus the declared fan | **declared** | 1 | §2.3; the exhaustive columns do not use it |

PER-R's inventory has no such row: the choice is absorbed into item 7 (the
window). This is the same fiber-absorption disease adjudicated at #274 (order
Z4), one unit later.

**REPAIR (exact).** Restore the row between items 7 and 8:

> | 8 | the seed menu: the first canonical transversal, plus the declared fan | **declared** | 1 | §6.2; the fan exercises 3 × 3 of it on (1,1,3)'s first two rounds; no exhaustive column uses it |

and renumber. (Note for the repair: the fan enumerates nine choices and
contributes eight schedules to the window because one of the nine *is* the
W5-LADDER member for (1,1,3) — worth one clause in §6.2, since the head
publishes 19.)

### MAJOR 6 — ONE INJECTION SURVIVES: A FALSE PROSE NUMBER PASSES EVERY PAPER GATE BECAUSE THE ALLOW-LIST IS THE RECEIPT AS A BAG.

`paper_coverage` backs a numeral if it is registered, **appears anywhere in
the receipt**, or is one of 26 declared exemptions. The middle route is a bag
lookup with no context. Injected into §3.2's prose:

> determinant support is {0, 3, 4, 7, 8, 11, 12, 15} **over 72 classes**, and …

`--verify-paper` returns **exit 0, "verify-paper: clean"** — every gate passes,
including G-PAPER-COVERAGE, G-PAPER-CLAIMS, G-PAPER-TABLES and
G-PAPER-POLARITY. The covering class has **32** codes; 72 is the R = 3
I7-STRICT count from a different census in the same receipt, and that is the
whole reason the sentence survives. (The control is exact: the same sentence
with **47** — a number the receipt does not yet carry when the scan runs —
**dies at G-PAPER-COVERAGE**. The gate works; its dictionary is too large.)

This is the #267 M6 family one level deeper: not sha digit-runs, but
**cross-census values reused in the wrong sentence**. It is template-shaped —
every unit with a receipt-wide allow-list has it — so the repair belongs in
the disease list as well as in this unit.

**REPAIR (exact, cheap).** Do not narrow the allow-list; **publish the
residue**. Add to `paper_coverage` a gated count: the numerals backed *only*
by the receipt-wide route and sitting *outside* every rendered claim and
rendered table row. Gate it against a declared ceiling. Today that residue
contains this injection; a paper whose residue is empty cannot carry a forged
number at all. As a second, independent line: scope each of the 26 exemptions
to a context regex (`#87`, `v14/`, `paper-2\d`) rather than exempting the
literal everywhere in the paper.

---

## 3. MINOR FINDINGS

**m1 — "R = 6 BUYS BOTH" buys them at two different records.** Prediction (c)
is measured correctly (declared yield 0/276/0/1350; motivated weld only at
R ≡ 0 mod 3), but at R = 6 the declared record is `G-SINGULAR` (1,1,4) and the
motivated weld is at the *undeclared* (2,2,2) — the paper's own §6 table says
so. Repair: "R = 6 buys both, at two different records".

**m2 — S-1 is a conjunction and half of it is closed.** §6.1 says "The
parent's registered question was whether the committed grammar drives a
concatenation". The parent's sentence is: "whether the committed grammar
*drives* a concatenation … **and** whether any admissible refinement **move**
consumes the law that becomes non-empty — a unit reporting a non-empty law
without a move that consumes it has reproduced this unit's crack rather than
opened the door." The unit's own S-2 registers the second conjunct honestly;
§6.1 should say "the first of the parent's two registered questions", and
§14 S-2 should name S-1 explicitly as half-open.

**m3 — "one rung below" is a step of two in this paper's own ladder.** §6:
"`G-SINGULAR` is reachable at R = 6, one rung below the declared record
paper-21 registered" — paper-21's declared rung is LOR-B at R = 8. The
sentence is right on the *declared* ladder, whose step is 2 **because of this
unit's parity law**, and wrong on the R-ladder the same paper indexes by 3, 4,
5, 6. Repair: "one rung below on the declared ladder, whose step is two by
§4.1's parity law".

**m4 — "every tuple with a given code lies in exactly one type multiset"
(§3.2) is false as written.** Codes do not determine multisets: (1,1,0) at
R = 5 is (1,1,0)+0+0+0+0 and (1,0,0)+(0,1,0)+0+0+0. The intended (and
implemented) statement is "every tuple lies in exactly one type multiset, and
the census quantifies over all multisets summing to the code". The
implementation is correct; the sentence is not.

**m5 — the receipt publishes two gate counts and the honest denominator is
neither the run's.** `totals.gates = 49`, `coverage.gates = 47`, transcript 50
rows. The two excluded from the coverage ledger are the ledger's own auditors
(G-COVERAGE-HONEST, G-SWEEP-EXECUTED), neither of which has a mutant or a
declared waiver. G-COVERAGE-HONEST's statement — "The denominator is this
run's own gate count" — should read "the gate count at the moment the ledger
is snapshotted: 47 of the run's 49; the two excluded are this ledger and the
sweep binding, which cannot be inside the object they audit". **Ledger note:**
#280's entry says "49 gates" and "825+119 numerals/words"; the run's own
numbers are 47 (coverage denominator) and **825 + 121**. The ledger row, not
the paper, carries the drift.

**m6 — two waiver forcings are stale in a way that undersells the unit.**
G-WALL-BHS and G-WALL-KR are waived as "a scan of the declared surface; the
interference mutant demonstrates the same scanner firing" — but this unit has
`M-PAPER-BHS` and `M-PAPER-KR`, dedicated **paper-leg** falsifiers, which is
exactly what #269's caveat of record demanded. Delete the waivers; the gates
have real mutants.

**m7 — "UNMOTIVATED everywhere else" (head segment 4) is measured on six
arenas.** The fiber law is measured per arena on 6 arenas, 12 agreements. The
head's "everywhere else" reads as a family statement. Repair: "and
UNMOTIVATED at every other arena of the declared dictionary".

**m8 — §7's vocabulary is undefined in the paper.** "compulsory", "witness"
and the `multisets` column are never defined; a reader cannot check the DIA
table without guessing (correctly, as it turns out: a class is compulsory when
its parallel class occurs as a round of *every* witness, a witness is an
ordered saturating tuple realising the record, and the multiset column counts
the distinct round-multisets). One sentence fixes it.

**m9 — paper-21's S-2 (the standard, or the list) is consumed at four more
rungs and not re-registered.** Every UNMOTIVATED row here is priced (2 free
items), which honours the parent's "may not be inherited" clause, but the
parent registered the *choice of standard* as an open corpus decision and this
unit adds four rungs of evidence to it without saying so.

---

## 4. THE ROWS I WAS ASKED TO DECIDE

**(1) The head's licensure — the eight verbs.** Audited row by row. The four
PERSISTS are sound (the cover binds with slack 18 = 9(R−3), verified; the
saturation schema re-proved and exact; the fiber law 12/12; the fiber
signature — with M3's stamp owed). The one TRANSFORMS is the best row in the
paper and survives an extension to 20/20. Of the three BREAKS, **one is a
mechanism, one is its corollary, one is a theorem of the unit's own making**
(M2). On the specific question: **COVER = POSDEF's break is the discovery that
the identity was a small-R coincidence** — and the unit has the evidence to
say exactly that, since it publishes the ceiling sequence 1, 2, 4 and paper-21
publishes the mechanism ("every breaking code needs a cell at 4"). The
licensed sentence is in §1 above. This review adds the datum that settles the
shape: **the ceiling at R = 6 is 5, not 8** — so the sequence is 1, 2, 4, 5,
and the identity was living on a ceiling that rises by construction.

**(2) The parity law's status — REGISTER ROW: CATALOGUE FACT, NOT CATALOGUE
LAW.** It is *not* a theorem about the declared records. Both directions of
the stated mechanism (even sum ⟺ q₁₂ ∈ ℤ) hold, but that biconditional is an
**identity** — n₁+n₂+n₃ even ⟺ n₃−n₁−n₂ even — true of every integer triple,
so verifying it "on 9 of 9" verifies nothing about I7. The content is the
empirical 9-for-9: I7's declared homogeneous family lies inside the
integer-off-diagonal sublattice while its own box splits 181/180. That is a
true, exhaustively checked statement about a **closed list**, and one real
forward consequence follows from it by the ladder law: **every odd budget of
this ladder is declared-record-empty** — checkable at every future rung, and
already the reason prediction (a) could not have failed. It **does not
constrain future record declarations**: nothing measured here forbids a unit
from declaring an odd-sum record tomorrow. The unit's S-4 routes the only
question that could upgrade it — is integrality of q₁₂ a constraint of I7's
construction or a choice of its author — to the declaring unit, correctly. Two
cheap extensions the register should carry: the two *site-dependent* declared
records (`G-CURVED`, `G-CURVOFF`) are untested for parity, and the d = 3
family (`G3-*`) is untouched.

**(3) The SIG-feed handoff.** Written out in §5 below as the row SIG's Z2 must
consume. **The floors agree with SIG's delivered four-class ladder on every
tier they share** (indefinite: covered-site 5, covering 6, structurally-live 7,
declared 8 — identical to the #274 adjudication's canonical form). Two
reconciliations are owed: (a) SIG's canonical form has **five** tiers and
PER-R publishes **four** — the "anywhere R = 1" tier (an *unrestricted* site
code, e.g. (0,0,1) at 4det = −1) is dropped here; (b) tier 3's definition must
travel in M1's repaired form or SIG will publish 7 for a class whose floor is
5. Cross-unit confirmation of record: **PER-R's locking theorem and SIG's
branch-and-bound both give min uncovered = 2** at R = 5, by wholly different
routes.

**(4) The DIA ruling — LICENSED, and it narrows to the scarcity law.**
"Compulsion is carried by the scarce link and vanishes exactly where the weld
turns motivated" is licensed, at 13/13 as delivered and **20/20** after this
review, and the "exactly" now has **two** instances rather than one: no class
is compulsory at (2,2,2) at R = 6 **and none at (1,1,1) at R = 3**, the only
two link-constant records the ladder reaches below R = 9. **Register row: the
diagonal motif CLOSES and the scarcity law opens.** The diagonal was never the
carrier — DIA, ROW and COL are interchangeable under the record's own counts,
which is why every permuted row behaves as its permutation; what carries the
compulsion is *a link counted once*. The undeclared direction's absence from
every witness is trivially forced (its parallel class deposits zero
incidences, so it is not saturating) and should be stamped as forced rather
than reported as a finding.

**(5) The G-SINGULAR-at-R=6 routing — and a finding against a sibling.**
`G-SINGULAR` is a **declared** record, reachable and now **driven** at R = 6,
at 1,350 ordered saturating sextuples, with an UNMOTIVATED weld at 36/3/1. Two
inheritances:

- **SIG inherits** a declared record at the singular boundary two rungs below
  its own declared indefinite floor, i.e. a polarity census over declared
  records has a non-empty singular stratum at R = 6 and an empty one at R = 5
  and R = 7.
- **LOR inherits a contradiction, and PER-R's own numbers are the datum.**
  LOR's committed §7 states: *"At budget R = 3m a structurally live schedule
  reaches the link-constant record (m, m, m) **and no other homogeneous
  record**."* At m = 2 (R = 6) the saturating stratum reaches **28 homogeneous
  records, ten of them covering** — (1,1,4) 1350, (1,2,3) 4020, (1,3,2) 4020,
  (1,4,1) 1350, (2,1,3) 4020, (2,2,2) 48600, (2,3,1) 4020, (3,1,2) 4020,
  (3,2,1) 4020, (4,1,1) 1350 (this review's recomputation; four of the ten are
  PER-R's own published DIA rows). LOR's **code-sealed** `budget_law` says
  only "a structurally live schedule reaches the link-constant record (m,m,m)
  at exactly R = 3m", which is true — the uniqueness clause exists **only in
  LOR's prose**. Route to the LOR repair/adjudicator: delete "and no other
  homogeneous record", or scope it to a class LOR names. PER-R is not at
  fault; PER-R is the instrument that decides it, and should say so in a
  successor row.
- **Mortality/admissibility datum:** the singular geometry is
  grammar-reachable, driven, and *declared* — so "admissible" and
  "positive definite" are not the same predicate on this ladder, and the
  corpus's admissibility discussions inherit a driven counterexample rather
  than an abstract one.

**(6) The S-1 closure.** Paper-21's S-1 is a **conjunction**; the unit closes
its first conjunct decisively (19/19 driven equalities, maxhits 1, zero
refusals, anchored twice including one budget wider than its own) and does not
touch the second (whether an admissible refinement *move* consumes the law
that becomes non-empty). **Register row: S-1 is HALF-CLOSED — the drive is
answered, the move is not**, and PER-R's own S-2 is the correct carrier for
the remainder. The paper's §6.1 wording should stop calling the drive "the
parent's registered question" (m2). The ledger's "paper-21's S-1 answered"
(#280) should be softened for the same reason.

**(7) The two-advisory compliance audit — REAL, not asserted, with one
recursion.**

| advisory | required | verified how | verdict |
|---|---|---|---|
| #267 M1 (walls never scan the paper) | walls scan the paper body | `body = paper_body(paper_text)` feeds the surface; BHS/KR/interference each re-append `body`; `paper_body` strips only §9 (38,833 → 36,683 chars) | **REAL** |
| #269 caveat (wall plants must die on the paper leg) | dedicated paper-leg mutants | `M-PAPER-BHS`, `M-PAPER-KR`, `M-PAPER-INTERFERENCE`, `M-WALL-L1`, `M-WALL-LORENTZ` all corrupt `body`/`ptext`, not the boolean | **REAL** (m6: the stale waivers undersell it) |
| #267 M2 (unrendered table rows) | all rows rendered | 54 rendered = all 54 data rows; 61 counts the 7 headers | **REAL** |
| #267 M3 (typed totals) | derived counts | sources 14, anchors 23, mutants 43 all gate-derived | **REAL**, with m5's two-denominator drift |
| #267 M6 (digest-token whitelists) | no sha digit-runs in the allow-list | `receipt_numbers` uses `(?<![0-9A-Za-z])\d[\d,]*(?![0-9A-Za-z])`, which rejects every digit run bounded by a hex letter; number-words scanned on the same terms (121 of them) | **REAL** |
| #270 (the class-explicit ladder) | floors stated class by class | the table exists, is gated (G-CLASS-LADDER), and its floors are correct **for the classes the code computes** | **FORM REAL, CONTENT DEFECTIVE — see M1** |

The last row is the finding: the unit received the class-substitution advisory,
built the instrument the advisory asked for, and **substituted a class inside
it**. That is worth engraving as a panel-protocol disease entry:
*a class-explicit table is only class-explicit if each column's printed
definition is the predicate its number was computed with.*

**(8) Walls, choice inventory, prose↔receipt sweep.** The four walls are
argued before any test, scan the paper, and carry paper-leg falsifiers; the
Lorentzian naming sentence derives its own form (q = [[1, 1/2], [1/2, 1]] is
the R = 5 first record (1,1,3)'s — verified) and is gated by a paper edit
rather than a boolean. The choice inventory is complete except M5's dropped
seed-menu row and M3's dropped invariance stamps. The 825 numerals / 121
number-words scan is honest: 26 exemptions all fire, each with a reason, and
the exemption table contains no measurement literal. Injection results in §7.

**(9) Successor register.** §6 below.

---

## 5. THE SIG-FEED ROW, AS SIG's Z2 MUST CONSUME IT

Verbatim, for the repair worker:

> **THE REACHABILITY LADDER IS FIVE TIERS DEEP AND THE TIERS ARE CUMULATIVE.**
> A determinant polarity is reachable at a different budget in each of five
> nested classes: an UNRESTRICTED site code; a COVERED site code (all three
> links present); a COVERING record (all 27 cells); a STRUCTURALLY LIVE
> COVERING record (covering, and no foreign pair, so every round saturates);
> and an I7-DECLARED record.
>
> | polarity | unrestricted | covered site code | covering record | live ∧ covering record | I7-declared |
> |---|---|---|---|---|---|
> | SINGULAR | 1 | 4 | 5 | 6 | 6 (`G-SINGULAR`) |
> | INDEFINITE | 1 | 5 | 6 | 7 | 8 (`G-INDEF`) |
>
> **At R = 5 the covered-site class IS attained for both polarities and the
> covering class is attained for SINGULAR only.** The indefinite region's
> absence at R = 5 is a property of the COVERING class and of nothing coarser,
> and it is a theorem: a cell at count 5 locks its two sites into one group in
> every round; the ten cells at those two sites demand seven distinct third
> members; five rounds supply at most five; so at least two cells stay
> uncovered. (SIG's own branch-and-bound and union-closure DP measure the same
> minimum: **2 uncovered**.)

Notes for the adjudicator on the reconciliation:

- PER-R's four columns are SIG's canonical five minus the "anywhere" tier; the
  four shared tiers agree exactly with the #274 adjudication's ladder.
- **The unrestricted tier is 1 for BOTH polarities** (this review's
  recomputation: (0,1,1) is singular and (0,0,1) is indefinite, both already
  in the one-round alphabet), so that tier discriminates nothing and is the
  one column of the five that carries no information. That is a defence of
  PER-R's four-column choice, and a caution for SIG's Z2: keep the tier if the
  ladder is to be stated in full, but record it as **trivially 1**, not as a
  measured floor. SIG's canonical form already has the indefinite value right.
- SIG's "2,210,000 multisets" and PER-R's "3 covered indefinite codes" are
  different objects at the same budget and do not need reconciling; the
  polarity verdicts do, and they agree.

---

## 6. THE SUCCESSOR REGISTER

**PER-R2 SITS AT R = 8, NOT R = 7 — AND THIS UNIT'S OWN PARITY LAW CHOOSES
THE BUDGET.** R = 7 is declared-record-empty *by theorem*, so the whole
declared-currency column of a rung census is a foregone conclusion there; R = 8
is the first budget carrying a declared **indefinite** record (`G-INDEF`
(1,1,6)) and also carries `G-DIAG2` (2,2,4), which is paper-21's original
LOR-B. The register row: **the ladder's interesting budgets are the even ones,
and the parity law is why.**

**THE LOCKING THEOREM'S GENERAL FORM IS DERIVABLE NOW, AND ITS BOUNDARY IS
R = 7.** The unit's S-3 leaves the general form open and reports the ceiling
sequence "1, 2, 4". Two things this review supplies:

- the counting obstruction is **budget-free in its numerator**: a cell at
  count R locks two sites whose ten remaining cells require **seven** distinct
  third members, and R rounds supply at most R — so **no covering R-tuple
  carries a cell count of R for any R ≤ 6**, and the obstruction *dissolves
  exactly at R = 7*, where seven rounds can supply seven thirds. Whether a
  covering 7-tuple with a locked cell actually exists is one search away and
  is the sharp form of S-3;
- the ceiling does **not** double: measured here, the covering class at R = 6
  has **72 codes and maximum cell count 5**, so the sequence is **1, 2, 4, 5**
  — and the indefinite codes (1,1,5), (1,5,1), (5,1,1) are in the R = 6
  covering class, independently confirming the covering floor of 6.

**THE PARITY LAW DOES NOT GET ITS OWN UNIT.** It is one measured row plus a
tautology; what would earn a unit is the question S-4 already routes — whether
I7's construction *forces* integral q₁₂ — and that is a question for the
declaring unit, on I7's own generator, not a rung census. Two cheap additions
belong to whoever asks it: the two site-dependent declared records, and the
d = 3 family.

**WHAT THE PERSISTENCE TALLY HANDS THE LIMIT PROGRAM.** Four rungs in, the
R-ladder's invariants split cleanly into *those that are theorems of the price
law* (the binding constraint, the saturation schema, the ladder law) and
*those that were artifacts of a small budget* (the cell ceiling and everything
that rode on it). The limit program's usable statement is the second half:
**a quantisation that holds at three consecutive rungs and is a corollary of a
budget-dependent ceiling is not an invariant of the arena**, and the R-ladder
now has an instrument that decides which of the two any candidate invariant
is — re-measure it at the rung where its mechanism's own parameter moves.

**ROUTED OUT OF THIS UNIT.** (i) The LOR uniqueness clause (§4 row 5) — a
one-line deletion in a sibling, with PER-R's R = 6 census as the datum.
(ii) The panel-protocol disease entry from §4 row 7. (iii) S-1's second
conjunct, unchanged.

---

## 7. THE INJECTION BATTERY

Injections were built against the committed paper and run through
`--verify-paper`, which rebuilds the whole derivation with the injected file as
the object under test — so the claim, table, coverage, polarity, fence **and
wall** gates all see it. **None of these is one of the unit's 43 declared
mutants**: each is my own sentence, at a location I chose.

| injection | result |
|---|---|
| covering-class code 32 → 33 in the §3.2 table | **DIED at G-PAPER-TABLES** |
| "over 47 classes" appended to §3.2's support sentence | **DIED at G-PAPER-COVERAGE** |
| **"over 72 classes" appended to the same sentence** | **SURVIVED — exit 0, clean (MAJOR 6)** |
| a sprinkling-grade Lorentz test named in §5's prose | **DIED at G-WALL-BHS** |
| a Myrheim–Meyer dimension estimate named in §5's prose | **DIED at G-WALL-KR** |
| an interference reading named in §5's prose | **DIED at G-INTERFERENCE-CLOSED** |
| the Lorentz naming verb flipped to "read as a signature" | **DIED at G-WALL-LORENTZ** |

The four wall rows are the decisive ones for the #267 M1 / #269 compliance
question: they are *foreign* plants in the paper's body, and every one dies on
the paper leg. The walls here really do scan the paper. The one survivor is
MAJOR 6, and it is a dictionary problem, not a wall problem.

---

## 8. VERDICT

**AWF.** The census is exact, the theorem is real, the witness is exhibited
round by round, the DIA law is the best measured object in the R-ladder, and
the grammar drives two rungs nobody had driven. **210 published values
recomputed independently, zero wrong** — including the locking theorem's
min-uncovered, which lands on SIG's independently measured 2. Six MAJORs, none
of which moves a computed number: one class defined as one thing and computed
as another in the very table built to prevent that (M1, and it is the SIG
feed); one tally that reads three findings where there is one mechanism, its
corollary and its own theorem (M2); one inherited disclosure dropped (M3); one
scope stamp over its census (M4); one inventory row absorbed (M5); and one
surviving injection whose cause is the allow-list's breadth, template-shaped
across the corpus (M6). Nine MINORs, one of which is a ledger drift in #280
rather than a defect in the unit. Three promotions the unit may take: the DIA
law at **20/20** with a second link-constant witness, the whole fiber *spread*
persisting rather than just its headline, and the ceiling sequence continued to
**1, 2, 4, 5** with the locking obstruction's boundary located at **R = 7**.
One finding is routed out of the unit entirely: **PER-R's R = 6 census
falsifies the uniqueness clause in LOR's committed §7**, and PER-R is the
instrument that decides it.
