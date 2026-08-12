# PER-R (paper-29) — OPERATOR-LENS HOSTILE REVIEW (K1)

**Reviewer:** K1, the operator lens. **Object at commit `442b3fe`:**
`v14/paper-29-perr.md` (sha256-12 `7d1d6ca3c5bc`), `v14/code/perr_exact.py`
(`d2f8fdac143d`), `v14/code/perr_output.txt` (`6dad652f81fe`),
`v14/code/perr_receipt.json` (`ac424c8a7bdd`), pin `v14/note-perr-pin.md`
(`6339ba42f354`). **All five digests verified at the start of this review and
again at its end; all five unchanged.** The unit's own 14 pinned sources were
re-hashed independently: 14 of 14 match, 0 mismatches.

**Method.** Every census below was rebuilt from the arena definition alone, in
eleven programs of my own, sharing no code with the instrument. The delivered
code was read to fix the arena's conventions — sites `Z_3^2`, the three
declared links `(1,0), (0,1), (1,1)`, cell `(x, l)` hit exactly when `x` and
`x + l` share a conflict group, `q12 = (n_diag - n_e1 - n_e2)/2` — and was
never used as an oracle for any number. Where the unit computed a quantity by
one route I computed it by two or three; the R = 6 door was taken by three, the
DIA compulsion by four. All arithmetic is integer.

---

## VERDICT

```
AWF -- ACCEPT WITH FIXES
```

Roughly **500 individual quantities were recomputed** (every number the paper
publishes, plus the measured layer of the receipt), by routes independent of
the instrument. **Zero disagreements. Not one published number moved, and no
claimed theorem is false.** The three predictions, the parity law, the locking
theorem, the covering-class census, the R = 6 door, the DIA law, the floors,
the weld fibers, the slack row and the numeral sweep all reproduce exactly.

Against that: **1 MAJOR** — a disclosure the terminal parent judged mandatory
on the very same object is dropped here — and **6 MINOR**, all of them wording
or scope repairs that move no number. The fixes are cheap; none requires a
re-run of any census.

---

## 1. WHAT REPRODUCED (the prompt's decisive targets, one by one)

**(1) The parity law — the hardest target, and it is stronger than claimed.**
All 9 declared homogeneous records carry an even count sum (10, 26, 8, 4, 8,
10, 20, 12, 6) and all 9 have integral `q12`. I7's committed box, recomputed
from its own `axis_max = 6` / `diag_max = 12` by its own Sylvester criterion,
holds **361 admissible points, 181 even and 180 odd** — exact.

The `<=>` is **not merely exact on the committed box; it is an algebraic
identity**: `sum(n) even <=> n3 - n1 - n2 even <=> q12 in Z`, with 0 violations
over the box and 0 over an independent 64,000-point sweep of `[0,39]^3`. Both
directions hold everywhere, not just on the 361. The paper states the mechanism
correctly ("the sum is even exactly when q12 ... is an integer"); the gate
evidence reports it as measured "on 9 of 9", which understates it.

**(2) The three predictions — 3 of 3 PASS, confirmed independently.**

*(a)* I7's box holds exactly **6** admissible points at count-sum 5 —
`(1,1,3), (1,2,2), (1,3,1), (2,1,2), (2,2,1), (3,1,1)` — the R = 5 saturating
stratum reaches **all six** (at 680/1350/680/1350/1350/680 ordered quintuples,
recomputed by three routes), and **0** are declared. Confirmed by exhaustion.

*(b)* The in-arena mod-3 proof holds: a live R-tuple deposits 9R incidences on
27 cells, so a field constant on all 27 needs `27 | 9R`, i.e. `3 | R`; the rows
R = 2..9 were recomputed one at a time. The STRUCT-DEAD control reproduces
exactly: the schedule ROW·COL·DIA·ANT·ANT carries a field **identically 1**,
is link-constant, and carries **18 foreign pairs** — 9 from each ANT round,
which is the only partition of the 280 with zero declared incidence. Link-
constancy is reachable at R = 5 and not reachable live: confirmed.

*(c)* Declared-record yield **{3: 0, 4: 276, 5: 0, 6: 1350}**; motivated weld
possible exactly at 3 | R; and every richer-slack column reproduces — site
codes 105 -> 181, covering-class codes 7 -> 32, max cell 2 -> 4, 4det support
3 -> 8 values, stratum cover **9,936 -> 1,842,120**.

**(3) The SIG feed.**

*The floor table.* Each of the eight floors was computed by my own census, in
its own class: SINGULAR **4 / 5 / 6 / 6**, INDEFINITE **5 / 6 / 7 / 8**. Exact.

*The locking theorem.* Rebuilt at all three declared links **with no pruning at
all** (full union closure over the 70 locked partitions): 70 locked partitions
and 70 distinct masks per link, covering unreachable at every link, and the
required third members are **7 — which are precisely all seven other sites**.
The counting mechanism is not only sound, it is *exactly tight*: my controls
give best coverage 24 at R = 4, **25 at R = 5**, 26 at R = 6 and 27 at R = 7,
i.e. a locked R-tuple misses exactly `7 - R` cells and R = 7 is the first
budget at which the lock can cover. This is a free strengthening of S-3.

*The covered split.* R = 5: **90 = 84 + 3 + 3**, indefinite exactly
`(1,1,5), (1,5,1), (5,1,1)` at **4det = -5**; R = 4: **44 = 41 + 3 + 0** with
the three identity-breaking codes. Exact.

*The covering-class census and its exhaustiveness license — AUDITED, and the
reduction is SOUND.* The argument is valid (a tuple's site code is the sum of
its rounds' local types, union is monotone so mask dedup loses nothing, and the
prune "missing cells <= 9 x remaining rounds" is admissible). I did not take it
on the argument:

- **full brute force over all `280^3 = 21,952,000` ordered triples** returns
  exactly the reduction's answer (1 code, `(1,1,1)`);
- **raw enumeration with no reduction, no prune and no dedup** at R = 4 on five
  targets, both polarities — `(1,2,2)` and `(2,2,1)` True over 672,103 and
  672,121 tuples, `(1,1,3)`, `(1,3,1)`, `(2,2,2)` False over 4,250,000,
  4,250,000 and 1,600,000 — agrees with the reduction on all five;
- **all 28 R = 5 negatives with max entry <= 4 re-run with the prune switched
  off**: same answer on 28 of 28. The prune is doing no work on the verdict.
  The remaining 30 negatives all carry an entry of 5 and are killed by the
  locking theorem independently of any search.

Result: **32 covering-class codes, max cell 4, 4det support
{0, 3, 4, 7, 8, 11, 12, 15}**, non-posdef exactly the three singular codes; and
one rung down, **7 codes all inside {1,2}^3, max cell 2, support {3,4,7}** —
paper-21's committed row, by my route.

*The singular witness.* The receipt's exhibited quintuple was re-measured from
its own five groupings: five valid partitions, union = all 27 cells,
**41 incidences**, round profile (7,7,9,9,9) so **3 of 5 saturating**, nine
site codes, **exactly one non-posdef site**, code `(1,1,4)` at 4det 0 = I7's
declared `G-SINGULAR`, max cell 4. My own independent witness search returns a
quintuple with identical statistics.

**(4) COVER=POSDEF and block quantisation.** The covering class's maximum cell
count is 1 / 2 / 4 at R = 3 / 4 / 5, so block quantisation does break; and the
covering class stops being a positive-definite class at exactly R = 5. Both
confirmed. (The *naming* of the first is MINOR-6 below.)

**(5) The slack row.** 9R - 27 = 9(R - 3) recomputed at R = 2..6:
-9, 0, 9, **18**, 27, with the binding constraint THE BUDGET / THE PERFECT
MATCHING / THE COVER / THE COVER / THE COVER. The cover binds at 45 > 27.

**(6) The dictionary fibers and the R = 6 census.** Weld 2's detector was
rebuilt in site coordinates (the realised relation is the Cayley graph of the
three declared classes; its automorphism group is `S3 wr S3`, order **1296**,
which is the isomorphism count the unit publishes). Fibers: `1/1/1` at R = 3,
**`36/3/1`** at R = 4 G-FLAT, **`36/3/1`** at both R = 5 records, `1/1/1` at
R = 6 (2,2,2), `36/3/1` at R = 6 G-SINGULAR; and the fiber law — all three
fibers 1 exactly at the link-constant records — holds on every one of 14
records I tested. The R = 6 door was counted by **three independent routes**
(target-bounded level DP, meet-in-the-middle over two half-censuses, and
explicit enumeration): **(2,2,2) = 48,600** and **G-SINGULAR (1,1,4) = 1,350**,
all three routes agreeing, with (1,2,3) and (3,2,1) at 4,020 as controls.

**(7) The DIA law's iff — rebuilt, and it survives an extension the paper did
not run.** All 13 tabled rows reproduce cell for cell (witnesses
276/276/276/680/1350/680/1350/1350/680/48,600/1350/4020/4020; multisets 12
twelve times and 78 once; every compulsory set). The law holds on 13 of 13 and
the count clause alone is falsified at exactly `(2,2,2)`. I then ran a fourth,
structurally different route — **compulsion by deletion**: a class is
compulsory iff the census run with that class's own partition removed from the
pool is empty — over **every** homogeneous record at R = 4, 5, 6, 7 and 8:
**55 rows, and the full law holds on 55 of 55**, the count clause failing
exactly on the rows with `min(counts) >= 2`. In particular the paper tables
only 4 of the 10 records at R = 6; the other 6 also obey the law.

**(8) The driven anchors and the window.** d66's committed output carries
`GRID(g=3,R=4) n=66 arbs=12 deliveries=18` and `GRID(g=3,R=6) n=102 arbs=18
deliveries=30` at the pinned sha — the two anchor rows, read correctly. The
declared window rebuilds to **19** schedules with exactly the published tag
split `{W4-ANCHOR 1, W5-CTRL 1, W5-LADDER 6, W5-SEEDFAN 8, W6-CTRL 1,
W6-DOOR 2}` over budgets {4,5,6}, and I recomputed the combinatorial field of
all 19: the six W5-LADDER schedules carry exactly the six R = 5 records, the
two W6-DOOR schedules carry (2,2,2) and (1,1,4), and the three d66 control
points carry (2,2,0), (2,3,0), (3,3,0) — uncovered, hence the COUNT-DEAD
control. **Scope note:** I did not rebuild the transport grammar itself, so the
driven-vs-combinatorial equality on the 19 is verified on its combinatorial
side and on its two committed anchors, not re-derived event by event.

**(9) The paper sweep.** The numeral scan reproduces exactly: **825 numerals,
121 number-words, 38,833 characters** (the launch prompt's "119" is off by two;
the object and my count agree at 121). The two block quotes attributed to
paper-21 are verbatim in paper-21 under the unit's own normalisation, and the
PER-L corollary cited for the cancelled interference census is present in
`note-perl-adjudication.md` in as many words.

**Off-tree reproduction.** In a provisioned mirror the instrument's
`--no-write` run reproduces the committed transcript exactly: same gates, same
evidence strings, differing only in the three expected mode artifacts (the
delivery-only `G-SWEEP-EXECUTED` row, 52 vs 53 published keys, and one
`[REFUSAL]` diagnostic that the driven builder prints to stdout and which never
enters the artifact).

---

## 2. FINDINGS

### MAJOR-1 — the parent's base-map qualifier on the weld fibers is dropped

**What is true.** The fiber triple `36/3/1` is not three invariants. The site
fiber is read at every base map and is a property of the field; the label and
orient fibers are read **at the enumeration's first base map only** and are not
base-map invariant. I recomputed both spreads from scratch: across the 1296
base maps the label fiber takes the values **3 and 6** and the orient fiber
takes **1 and 2**. So `I-ORIENT` — published in this paper's choice inventory
as `measured, fiber 1` — is a **free item at some base maps**, and the price is
"at least 2 free items at every base map, exactly 2 at the declared one", not
"2 free items".

**This is not a discovery of mine.** The unit's own receipt already carries it:
`weld.rows[*].label_fiber_spread = [3, 6]`,
`orient_fiber_spread = [1, 2]`, `fibers_base_map_invariant = false` on all
eight UNMOTIVATED rows. And the terminal parent, paper-21, treated the
disclosure as mandatory in three places at once — its verdict head
(`LABEL+ORIENT-NOT-BASE-MAP-INVARIANT(SPREADS [3, 6] AND [1, 2];
>=2-FREE-ITEMS-AT-EVERY-BASE-MAP...)`), its §4.5 prose, and its choice
inventory rows 11 and 12 ("at the forced base map; spread [3, 6] across the
1296 — not base-map invariant").

**What paper-29 does.** The strings "base map" and "spread" do not occur in it
at all. It publishes `36/3/1` in the head, in the §6 fiber table (five rows),
in §6's "the price is 2 free items", in §10 inventory rows 11 and 12 as
**measured / 3** and **measured / 1** with no qualifier, and in §11.1 as
"the weld fiber signature | 36/3/1 | 36/3/1 | **PERSISTS**". A reader of the
persistence table takes that row as an invariant persisting across a rung. Two
of its three numbers are base-map artifacts.

**Why MAJOR.** No number is wrong and the verdict (UNMOTIVATED at both rungs,
the signature unchanged) is unaffected — the two rungs have *identical*
spreads, so the comparison is if anything better supported by the disclosure
than without it. But this is a successor silently dropping a qualifier its own
terminal parent declared necessary on the identical object, in a paper whose
§14 carries a standing "what may not be inherited" row. That is exactly the
inheritance failure the row exists to prevent.

**Exact repair** (no re-run; the receipt already holds every value):

1. §6, after the fiber table, add the parent's own sentence: *"The site fiber
   is read at every base map; the label and orient fibers are read at the
   enumeration's first, and are not base-map invariant — across the 1296 they
   take the values 3 and 6, and 1 and 2, so the price is at least 2 free items
   at every base map and exactly 2 at the declared one. The two rungs carry the
   same spreads."*
2. §10, rows 11 and 12: append, verbatim after paper-21's own rows,
   *", at the declared base map; spread [3, 6] (resp. [1, 2]) across the 1296 —
   not base-map invariant"*.
3. §11.1, the weld-fiber row: read it as *"36/3/1 at the declared base map,
   spreads [3,6] and [1,2] at both rungs"* — the persistence claim then rests
   on the spreads, which are genuinely equal.
4. §14, "What may not be inherited": add *the fiber triple 36/3/1 without its
   base map*.
5. Optional but cheap: bind `fibers_base_map_invariant` and the two spreads in
   `G-WELD-ROWS`, so the qualifier cannot be dropped again silently.

### MINOR-1 — §3.6's STRUCTURALLY LIVE class is defined without the condition its floors are computed under

§3.6 defines the third class as *"a STRUCTURALLY LIVE RECORD carries no foreign
pair, so every one of its rounds saturates"* — liveness alone. The instrument
computes that column as **live AND covering**
(`covering_with_code(..., live_only=True)`), and `G-CLASS-LADDER` checks the
nesting `site <= covering <= live <= declared`, which only makes sense
cumulatively.

The difference is not cosmetic. I measured the class as the prose literally
defines it — the R-fold sumset of the live alphabet, which is
`{(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1)}`, six letters, with
`(1,1,0)` absent because `{x, x+e1, x+e2}` always carries a foreign pair — and
the floors become **4 (SINGULAR) and 5 (INDEFINITE)**, not 6 and 7. Under the
literal reading §3.7's "In the STRUCTURALLY LIVE class both floors are one rung
higher again, R = 6 and R = 7" is false.

**Repair:** one clause — *"a STRUCTURALLY LIVE RECORD covers all 27 cells and
carries no foreign pair, so every one of its rounds saturates"*.

### MINOR-2 — §5.1 attaches a whole-stratum count to the covering subset

> "1,842,120 of the 60,466,176 ordered saturating quintuples cover all 27
> cells, over 619,092 distinct induced fields."

619,092 is the number of distinct fields induced by the **whole** stratum
(receipt key `stratum.5.distinct_fields`, sitting beside `total`). The
**covering** quintuples induce **6,336** distinct fields — I counted them. The
sentence's plain reading is wrong by two orders of magnitude.

**Repair:** *"…cover all 27 cells. The stratum as a whole induces 619,092
distinct fields."* (Or publish 6,336, which is the number the sentence's
grammar promises.)

### MINOR-3 — the declared-record floor at R = 8 is asserted from arithmetic, not censused

`reachability_ladder[*]["I7-DECLARED-RECORD"]` is `min(sum(v))` over the
polarity's declared records — pure arithmetic. That settles the *lower* half of
a floor (nothing can arrive earlier, by the ladder law), not the upper half.
For SINGULAR the upper half is measured elsewhere (G-SINGULAR at 1,350 ordered
saturating sextuples). For INDEFINITE it is not, yet §3.6 and §3.7 say
G-INDEF *"arrives as a whole record at R = 8"* and the table prints 8.

I censused it: `(1,1,6)` **is** realizable at R = 8, at **3,752** ordered
saturating octuples (exhaustive for that target by the unit's own saturation
schema). The number is right. I also checked the rest of the family at its own
budget: G-FLAT 276, G-SINGULAR 1,350, G-DIAG2 1,452,780, G-ANISO 278,460,
G-OFFDIAG 19,744,200 — all realizable.

**Repair:** add the count (the unit's own `stratum_target_count((1,1,6), 8)`
returns it in under a second), or reword the column as "cannot arrive before".

### MINOR-4 — the SIG-FEED head's scope tag lands on the record-floor clause

The head ends `... RECORD FLOORS: G-SINGULAR R=6, G-INDEF
R=8@EXHAUSTIVE-OVER-1,721,036,800,000-ORDERED-GROUPING-QUINTUPLES`. The
`280^5` exhaustiveness is the scope of the **covering-class census at R = 5**;
the record floors are claims at R = 6 and R = 8 and are not statements about
any quintuple census.

**Repair:** move the `@` tag onto the covering-class clause, and give the
record-floor clause its own scope (the ladder law plus, after MINOR-3, the
R = 6 and R = 8 counts).

### MINOR-5 — §7's undeclared-direction sentence is forced, not measured

*"The undeclared direction appears in no witness of any row."* Witnesses are
ordered **saturating** tuples, and ANT is the unique partition of the 280 with
zero declared incidence, so it is not in the stratum at all: `freq[ANT] = 0`
cannot fail. The same clause sits inside `G-DIA-LAW`'s conjunction as a
conjunct that cannot be false.

**Repair:** state the reason — *"ANT is the one partition that deposits no
declared incidence, so no live tuple can contain it"* — or drop the sentence.

### MINOR-6 — "cover = posdef" names an equality; what the instrument measures is a one-way inclusion

`cover_equals_posdef` is computed as *"no covering-class **code** is
non-posdef"*. At the level of codes the two classes are never equal: the
positive-definite covered codes number **17 / 41 / 84** at R = 3/4/5 against
covering-class codes **1 / 7 / 32**. So the §3.2 table header "cover = posdef",
§5.2's "the cover-equals-positive-definite identity", §11.1's row
"cover = positive definite" and the head's "COVER=POSDEF" all read, at the
level the surrounding table works at, as an equality that is false at every
rung including the two where the paper says it holds.

The sentence **is** true under the reading §3.4 names (the COVERING-RECORD
class): a record positive definite at every site necessarily covers, because
`q11 = n1 > 0` and `det > 0` force `n2 > 0` and, since
`4det = 4n1n2 - (n1+n2)^2 = -(n1-n2)^2 <= 0` when `n3 = 0`, also `n3 > 0` — I
verified there is no posdef code with a zero count over `[0,24]^3`. So
{posdef records} is contained in {covering records} always, and the equality of
record classes holds at R = 3 and R = 4 and breaks at R = 5. That is a real
result, and the paper never states the half-line that makes it one.

**Repair:** in the §3.2 table rename the column *"every covering-class code
positive definite"*; in §3.4 replace "coincide" with the record-level statement
plus its bridge — *"a positive-definite record necessarily covers, by I7's own
Sylvester criterion, so the two record classes coincide at R = 3 and R = 4 and
part company at R = 5"*; keep the head as is once the column is renamed.

---

## 3. STRENGTHENINGS FOUND (offered, not required)

1. **The locking bound is exactly tight.** A locked R-tuple covers at most
   `27 - (7 - R)` cells: 24, 25, 26 at R = 4, 5, 6, and 27 at R = 7. So the
   "seven third members against R rounds" mechanism is not merely sufficient —
   it is the exact obstruction, and R = 7 is where it dissolves. S-3's open
   question ("whether it gives the exact ceiling at every budget") is answered
   for the lock itself.
2. **The DIA law holds on 55 rows, not 13** — every homogeneous record at
   R = 4..8, by a fourth route (compulsion by deletion). The count clause fails
   exactly on the `min(counts) >= 2` rows, of which `(2,2,2)` is the smallest.
3. **The parity `<=>` is an identity, not a census.** It needs no box.
4. **The covering-class negatives do not need the prune** (28 of 28 unchanged
   with it off), which is worth one sentence in §12's deviation 1.

---

## 4. TWO MUTANTS OUTSIDE THE DECLARED HARNESS

Both are corruptions no member of the 43-mutant registry makes, applied to the
source in an off-tree mirror and run through `--no-write`.

**MUT-K1-1 — break the local-type reduction's completeness.** `type_multisets`
was changed to forbid a repeated letter (`rec(..., j)` -> `rec(..., j + 1)`),
which makes the covering-class census incomplete rather than wrong-by-a-value.
**KILLED** — the run died at `G-SINGULAR-WITNESS`.

*But note where it did not die.* The corrupted run still returned the R = 4
back-validation **intact**: 7 codes, max cell 2, 4det support [3,4,7], all
three matching paper-21's committed row — while the R = 5 census collapsed from
32 codes to 13, max cell 4 to 3, and lost all three non-posdef codes. §13's
"An error in this unit's machinery would have to reproduce all of them to
survive" is true only because a *different* gate caught it: the eight-column
back-validation is blind to this class of error, because the R = 4 covering
codes happen to be reachable with four distinct letters. Worth one clause in
§13, and a candidate for a declared mutant.

**MUT-K1-2 — widen I7's committed count box by one diagonal row**
(`diag_max + 1`), moving the box from 361 admissible points to 380 and the
parity split from 181/180 to 191/189. **KILLED** — the run died at
`G-PAPER-CLAIMS` ("claims 20, matched 19, missing ['parity']").

*Where it did not die:* `G-PARITY` itself **passed** on the corrupted box —
it binds "9 of 9 even" and the `q12` mechanism, not the split. The 361/181/180
triple is held only by the paper-claim rendering. That is the architecture
working as designed (the paper gate is the binding), but it is worth knowing
that the parity split has no census-side gate of its own.

(My first attempt at this mutant — adding the `n_e1 = 0` row — was a no-op, and
correctly so: `q11 > 0` makes those points inadmissible. My error, not the
unit's.)

---

## 5. RECOMPUTATION LEDGER

| block | quantities re-derived | route |
|---|---|---|
| digests | 19 | 14 pinned sources + 5 objects, re-hashed |
| the arena §2 | 12 | own partition generator + closed form |
| code space + class split | 24 | own sumset, R = 2..6 |
| parity, box, prediction (a) | 25 | own Sylvester recomputation + a 64,000-point identity sweep |
| the saturating stratum | 67 | convolution, cross-checked by meet-in-the-middle at R = 3, 4 |
| covering-class census + audits | 50 | own reduction + 21,952,000-triple brute force + raw enumeration + prune-off on all 28 negatives |
| the locking theorem | 21 | full union closure, no pruning, 3 links + 3 budget controls |
| the four-class floors | 11 | own census per class, plus the live-alone reading |
| the singular witness | 26 | re-measured from the receipt's own groupings + own search |
| R = 6 door and R = 5 targets | 21 | three independent routes each |
| the DIA row | ~100 | enumeration, plus a 55-row deletion-route extension |
| the weld | 40 | detector rebuilt in site coordinates |
| predictions (b), (c), slack, yields | 48 | own arithmetic and controls |
| the declared window | 26 | rebuilt, all 19 fields |
| the paper sweep | 3 | own regex scan |
| parent anchors, d66, quotes | 20 | read from pinned bytes |
| declared-record realizability | 6 | own census at each record's own budget |

**Total ~500 quantities. Disagreements: 0.**

---

## 6. WHAT I DID NOT REBUILD

The transport grammar itself. The 19 driven schedules' *driven* side, the
`maxhits` forcedness reading and the refusal control rest on the instrument's
own drive; I verified their combinatorial side, the window's composition, and
both committed anchor rows `(66, 12, 18)` and `(102, 18, 30)` against d66's
pinned output. Two of the nine declared records (G-OFFDIAG2 at R = 20 and
G-ANISO2 at R = 26) are beyond my census, as they are beyond the unit's; and
`G-OFFNEG` at R = 12 I did not run.

**Digests re-verified at the close of this review: paper `7d1d6ca3c5bc`, code
`d2f8fdac143d`, output `6dad652f81fe`, receipt `ac424c8a7bdd`, pin
`6339ba42f354` — all unchanged.**
