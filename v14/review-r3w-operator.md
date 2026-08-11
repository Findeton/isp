# OPERATOR-LENS HOSTILE REVIEW — paper-19, the R = 3 weld (K1 decisive + K2)

**Object** (commit `ddcd475`): paper `c669ab35e12a` / code `7a84aa27de8d` /
output `76ef29488b60` / receipt `03670731ba1c`; pin `20fba9b15f5e`.
**Protocol:** v14 ledger #163, rows K1 and K2.
**Interpreter:** `/opt/homebrew/bin/python3.13`. Exact arithmetic throughout
(`fractions.Fraction` and `int` only; no float anywhere in my rebuild).

## GRADE

```
ACCEPT-WITH-FIXES
```

**WELD3-FOUND STANDS.** I rebuilt it from nothing — my own slicer of the
committed d42b1 layer, my own picker, my own generalized conflict-grid
driver, my own detector, my own geometry census on two routes neither of
which is the unit's — and every headline number reproduced exactly. FOUND
survived every attack I could pose, including two the unit did not run. One
MAJOR finding: a sub-claim of §5.7 (**count-sufficiency**) is **false as
worded**, with 46,584 counterexamples inside the unit's own family and one of
them a row of its own census. The verdict strings are untouched by it.

**Recomputations: 190.** All agreed with the unit except the two numbers named
in MAJOR-1, which are the finding.

---

## 1. Integrity, and the byte-identity run

All six object hashes verify. All **13** declared source anchors verify at
their pinned sha-12 (`A-PIN`, `A-U4BADJ`, `A-U4BEFF`, `A-W2`, `A-HA`, `A-I7`,
`A-D42B1`, `A-D60`, `A-D66`, `A-D66OUT`, `A-D58`, `A-L1`, `A-CAT`).

The plain delivery run was taken **off-tree** in a scratch mirror
(`repo/v14/code/` with `v10`, `v11`, `v13` symlinked, no git present):

| artifact | my run | committed |
|---|---|---|
| `r3_weld_output.txt` | `76ef29488b60` | `76ef29488b60` |
| `r3_weld_receipt.json` | `03670731ba1c` | `03670731ba1c` |

**Byte-identical at my own hands.** `git status` clean before and after; my
only repo write is this file.

*Housekeeping note, not a finding against the unit:* while I worked, another
process was running `r3_weld_exact.py` with cwd `= v14/code/` — i.e. writing
the delivery artifacts inside the repo. It reproduced byte-identically so
nothing moved, but a panel member running the delivery path in-tree is one
non-reproducible run away from perturbing the object under review.

---

## 2. K1 — THE FOUND VERDICT, REBUILT FROM NOTHING

### 2.1 What I built differently

I imported **no code from the unit**. My rebuild:

- **the grammar**: my own text-slice of `d42b1_transport_exact.py` at
  `print("[d42b1` and `exec` of the head — `candidates_for` is the committed
  layer's own, nothing about admissibility re-typed;
- **the picker**: my own class, full-tuple specification only, recording the
  menu-hit count of *every* pick (so FORCED is the max over the whole record,
  not a single probe);
- **the driver**: my own generalization of d66's `conflict_grid` cycle,
  written from the committed source's text rather than from the unit's
  `drive`, and **anchored event-for-event against d66's own
  `conflict_grid(3,2)` AND `conflict_grid(3,3)`** — my event lists are
  identical to d66's in both cases;
- **the detector**: my own backtracking bijection search, `ISO` branch and
  `INTO` branch written separately;
- **the geometry census**: a **27-bit presence-mask** route, licensed by a
  sitewise theorem I proved rather than assumed (below), cross-checked
  against a packed 6-bit-per-site route;
- **the determinant spectrum**: a **separable-convolution** route that never
  enumerates an ordered triple at all — per-site histograms over the 280
  partitions, three-fold convolved, summed over the nine sites;
- **the stabilizers**: direct translation and the exact
  `Z[w] = Z[t]/(t^2+t+1)` Fourier annihilator, written independently.

### 2.2 Stage 1, driven (K1.1)

| quantity | my measurement | unit |
|---|---|---|
| uniform ROW\|COL\|DIA record | 48 events, 9 divisions | 48, 9 |
| every pick's menu-hit count | `{1}` — **maxhits 1**, no refusal | FORCED |
| cells at n = 1 | **27 of 27** | 27 |
| link incidences | **27** | 27 |
| q at every site | `[[1, -1/2], [-1/2, 1]]` | same |
| det at every site | **3/4**, one distinct value | 3/4 |
| positive-definite sites | **9 of 9** | 9 of 9 |
| realised co-division pairs | **27** distinct, 9 site objects | — |
| driven field vs combinatorial | equal | equal |

The whole declared window **W3** rebuilt from its own definition — 4³ class
triples ∪ all 72 I7-STRICT triples, each at the first two canonical
transversals per round — gives **1040** (512 + 576 − 48 overlap), against a
family of 280³ · 27³ = **432,081,216,000**, ratio 1 : **415,462,707**. All
1040 re-driven with my builder:

- **FORCED 1040 of 1040**; BRANCHING 0; REFUSED 0;
- record-length trichotomy **32 / 192 / 816** at 36 / 42 / 48 events;
- **driven field = combinatorial field on all 1040, 0 mismatches** — the
  licence for every exhaustive column, re-earned at my hands;
- the 576 driven saturating records: **one** co-division relation, **one**
  link field, every one (48 events, 9 divisions, maxhits 1).

Both constructibility controls reproduce exactly: the no-supply control
refuses **`propose G10` at prefix 14**; the under-specified control reads
**7** menu candidates at prefix **3** for seed **G00**. The **31** strata
cells over **136** scanned grouping triples reproduce.

### 2.3 Both map censuses, and the census table (K1.2, K1.3)

My detector, on my driven records, over all nine arenas at both readings —
**all 18 rows match the paper's declared table, cell by cell**:

| arena | @EMBEDDING | @QUOTIENT |
|---|---|---|
| R3-SAT | **FOUND**, isos **1296**, fibers **1/1/1** | **FOUND**, maps **1296**, fibers **1/1/1** |
| R3-ROW\|COL\|ANT | **FOUND**, 1296, 1/1/1 | **FOUND**, 1296, 1/1/1 |
| R3-COMMITTED-GRID(3,3) | STRUCT-DEAD, 0 maps | COUNT-DEAD, 2592 maps, **9** zero cells |
| R3-SAT-FALSIFIER | STRUCT-DEAD, 0 maps | COUNT-DEAD, 1296 maps, **3** zero cells |
| R2-COMMITTED-GRID(3,2) | STRUCT-DEAD, 0 maps | COUNT-DEAD, 2592 maps, 9 zero cells |
| CRYSTAL/DOUBLE-GRID(3,2)@L2 | **FOUND**, **72**, 1/1/1 | **FOUND**, 72, 1/1/1 |
| CRYSTAL/DOUBLE-GRID(3,2)@I7 | STRUCT-DEAD, 0 maps | COUNT-DEAD, **9 of 9** zero (the diagonal) |
| CRYSTAL-INHOMOGENEOUS@L2 | UNMOTIVATED, site fiber **6**, label **2** | UNMOTIVATED, 6, 2 |
| D58-WALK@I7 (depth 30, seed 4242) | ARITY-DEAD, **2 against 9** | ARITY-DEAD |

Fate distribution **FOUND 6 / STRUCT-DEAD 4 / COUNT-DEAD 4 / UNMOTIVATED 2 /
ARITY-DEAD 2** ✓. **The reading-difference result reproduces**: every dead row
dies at `maps = 0` under EMBEDDING and at count positivity under QUOTIENT.

The zero-free-items accounting at the RSQ standard is confirmed with the
forcing exhibited: fibers are 1 because the field is identically 1, so the
whole 1296-element map orbit, all six direction relabellings and both
orientations collapse to one field. The standard is not vacuous — the
declared falsifier returns 6 and 2, which is weld 2's own committed value.

**Cross-unit anchors verified at their commits** (read-only `git show`):
weld 2 at `e80d7ef` commits *"FOUND — 72 site assignments … all 72 give one
and the same field"*, `I-SITE-ASSIGNMENT` fiber **6** at the falsifier, and
the declared I7-target probe at **1296** isos / 15552 configs; U4b at
`6d9f45d` commits *"wall permits 6, measured 3"* and *"747 of the 78400
pairs"* with `I7-STRICT-EMPTY`. My own re-measurement of all four matches.

### 2.4 THE ATTACKS

**(a) Does the W3 window smuggle the selection? NO — and I can prove it.**

I re-derived FOUND by a **window-free route**. For *any* I7-STRICT grouping
triple the arithmetic is forced: three rounds deposit at most 9 link
incidences each, all 27 cells need ≥ 1, so every round saturates and every
one of the 27 cells is covered exactly once — which means the realised
co-division relation is forced to be **exactly the 27 non-ANT site pairs with
count 1**. I checked this combinatorially at **all 72** triples (0
exceptions, no driving involved), and then *drove* a representative of **all
12 multisets**: every one returns **FOUND at both readings with 1296 maps**.
The window contains the whole stratum and the stratum is homogeneous by
theorem. **Attack fails; FOUND is stratum-wide, not window-relative.**

**(b) Does the site assignment consume anything undeclared? NO.**

The detector's inputs are the actor label set, the realised pair set, and
I7's declared (X, links, L). I confirmed **naming-blindness** by relabelling
the nine actors under a random permutation: identical fate, identical map
count. The one place a name could leak is `sorted(S, key=str)`, which fixes
`maps[0]` — the base map at which the label and orient fibers are read. I
therefore measured those two fibers at **every** base map (1296 for R3-SAT,
72 for the falsifier): constant `[1]`/`[1]` and `[2]`/`[1]`. The reported
numbers are right and are in fact base-map-independent; see MINOR-1 for the
gap between that fact and what the code measures.

**(c) COUNT-SUFFICIENCY: REFUTED AS WORDED.** See MAJOR-1.

**(d) FOUND-killing readings the unit did not run.** I posed three.

1. **The round-structured reading** — require each round's nine pairs to land
   on one *full* declared direction class, i.e. keep the record's own round
   labels instead of forgetting them. Measured: **1 of the 12 multisets
   survives**. This narrows FOUND from the 72-triple stratum to the single
   ROW|COL|DIA multiset. It is *not* a kill, because I7 declares sites and
   links and no round structure, so the reading has no target-side referent —
   but it is the sharpest thing the detector throws away, and it is worth a
   named sentence: the record carries a decomposition of its 27 pairs into 9
   division-event triangles that the weld does not read.
2. **The directed reading** — 0 surviving maps at R3-SAT. This would kill
   FOUND, but it returns 0 at every co-division arena in the census, so by
   HA §14 requirement 3 it cannot be the admit test. The unit discloses this
   and carries the directed comparator. No finding.
3. **The site-carrier-fixed reading** — the strictest one available: force
   the map to be the constructor's own actor → Z_3² parse (inventory item 3,
   which the paper itself calls *forced*). Measured: **R3-SAT survives**
   (min = max = 1 under the identity), while **R3-ROW|COL|ANT dies with 9
   zero cells**. This is a *positive* result for the unit that the unit did
   not claim: **FOUND at the primary arena does not depend on the site
   assignment being free at all.** Only the ROW|COL|ANT row does, exactly as
   §4.4 and deviation 6 price.

---

## 3. K2 — THE GEOMETRY CENSUS

Exhaustive over all **21,952,000** ordered grouping triples, by two routes.
Every cell of the distribution reproduces:

| posdef sites | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | **8** | **9** |
|---|---|---|---|---|---|---|---|---|---|---|
| triples | 4,341,196 | 8,655,660 | 6,350,724 | 2,177,064 | 384,318 | 38,286 | 4,410 | 270 | **0** | **72** |

- **THE EMPTY CELL AT 8 CONFIRMED** — the ceiling is attained or missed by at
  least two.
- **I7-STRICT = POSDEF-9 = field ≡ 1 at exactly 72**, in **12** multisets, by
  two routes (packed census over 21.95M; direct search over the 36 saturating
  partitions). Exactly **1** multiset is the three parallel classes, **11**
  use non-line conflict groups. **1,417,176** schedules.
- **Det spectrum**: 9 values on **197,568,000** cells, exact match on all
  nine counts, obtained by a convolution route that never touches a triple.
  **328** homogeneous triples. **715,755** non-degenerate at 9 of 9.
- **Coordinate-free 288 = 4 × 72** — 36 admissible partitions and 72 triples
  for *each* of the four missing classes, 216 extra over the committed
  naming. **The worker's self-correction is right**: R3-ROW|COL|ANT deposits
  literally zero I7 incidences in fixed coordinates yet realises a relation
  isomorphic to the target, so its FOUND is carried by the free site
  assignment and by nothing else (I confirmed both halves in (d3) above).
- **R = 2 back-anchor**, all 78,400 ordered pairs: ceiling **3**, wall
  18//3 = **6**, I7-STRICT **0**, max incidences **18**, non-degenerate at 9
  of 9 = **747**. Matches U4b's committed row at `6d9f45d`.
- **Crystallinity**, all 84³ = **592,704** ordered seed-set triples:
  stabilizer distribution **588,780 / 561 / 561 / 561 / 561 / 1,680** exact;
  **3,924** crystalline; the full group reachable at **1,680** = 9!/(3!)³;
  **13,051** distinct fields with two independent stabilizer routes agreeing
  at all of them; **0** affine-law violations; **3,816** beyond-coset and
  **1,656** of the 1,680; **no CU-SPLIT triple is crystalline**.
- **THE FRAGILITY CONTRAST, both directions:** all **5,832** single
  grouping transpositions (72 × 81) taken — **0** leave the triple
  I7-STRICT; **8,424** crystalline schedules on the stratum, all **151,632**
  single-arbitration re-seatings (8,424 × 18) break the period; the geometry
  is invariant under all **19,683** seed choices by construction (the
  combinatorial field does not take seeds as an argument) and by the
  driven-equals-combinatorial equality on 1040 records. The **144** driven
  re-seatings of the first 8 crystals are all FORCED.

### A strengthening the unit did not claim

I proved, over all 64 site codes reachable in this family, that

> **posdef at a site ⟺ min(n_(1,0), n_(0,1), n_(1,1)) ≥ 1**

whenever the three counts are ≤ 3 — which they always are, since three rounds
deposit at most 1 per cell. So "I7-STRICT = POSDEF-9" is not only a
top-of-the-ladder coincidence forced by the 27-incidence budget; the two
predicates coincide **at every site of every one of the 21,952,000 triples**,
and therefore the whole posdef distribution equals the whole strict
distribution. §4.2's theorem is a corollary of a sitewise identity. Worth a
line; it costs nothing and it makes the rigidity result stronger.

---

## 4. FINDINGS

### MAJOR-1 — "deposits 18" is false, and the count-sufficiency claim is false as worded

**Where.** paper §5.7 line 513, §8 line 620; code line 2973 (the `18` is a
**typed literal inside the `G-COUNT-IMPLIES-WELD` evidence string**, so no
gate can catch it).

**What the unit says.**

> all 72 I7-STRICT triples carry exactly 27 incidences, and every arena in
> the census that deposits fewer dies — the committed R = 3 grid deposits 18
> and is COUNT-DEAD.
> … At this candidate family and this target, **27 incidences force the field
> to be identically 1**, the co-division relation to be the target's own
> Cayley incidence, and every fiber to be 1

**What I measure.** Under the unit's *own* operative metric — the `w`
returned by `pack_links`, the same quantity that produces
`max_incidences_per_round: 9`, `max_incidences: 27`, and the R = 2 anchor's
`max incidences 18` (`inc2 = max(inc2, W[a] + W[b])`, code line 2450) —
d66's own R = 3 point (ROW, COL, ROW) deposits:

```
link incidences (the W-metric)      27      <-- not 18
distinct cells covered              18
field                               2 on the nine (0,1) cells
                                    1 on the nine (1,0) cells
                                    0 on the nine (1,1) cells
```

Consequences, both measured:

1. The necessity sentence mis-describes its own exhibit. The committed R = 3
   grid does **not** "deposit fewer" than 27. It deposits exactly 27 and dies
   anyway — which is a *better* illustration of the point than the one
   written, but it is not the point written.
2. **The sufficiency claim is refuted inside the unit's own family.** Of the
   **46,656** ordered grouping triples all three of whose rounds saturate
   (36³, every one depositing the full 27 incidences), **46,584 are not
   field-identically-1**; only **72** are. One of the 46,584 is the committed
   R = 3 grid, which is a row of this unit's own census and is COUNT-DEAD.
   So "27 incidences force the field to be identically 1" is false, with
   46,584 counterexamples.

**What is true**, and is exactly what §4.2's rigidity argument already
proves: *27 incidences spread over all 27 cells* — equivalently, every one of
the 27 cells covered — forces the field to be identically 1. The paper's own
§4.2 wording ("every round saturating, **every cell covered exactly once**")
is the correct statement; §5.7 dropped the second clause.

**Exact repair.**

- §5.7 line 513: `the committed R = 3 grid deposits 18 and is COUNT-DEAD` →
  `the committed R = 3 grid spends its 27 incidences on only 18 of the 27
  cells — two on every row cell, none on any diagonal cell — and is
  COUNT-DEAD`.
- §5.7 line 518: `27 incidences force the field to be identically 1` →
  `27 incidences spread over all 27 cells force the field to be identically
  1`, plus one measured sentence: `the count alone does not — 46,584 of the
  46,656 triples that deposit all 27 incidences are not field-identically-1`.
- §8 line 620: `deposits 18 incidences and is COUNT-DEAD` → `spends its 27
  incidences on 18 of the 27 cells and is COUNT-DEAD`.
- code line 2973: replace the typed `18` with the computed covered-cell
  count, and extend `G-COUNT-IMPLIES-WELD`'s predicate to bind the corrected
  statement (assert the committed grid's incidence count is 27, its
  covered-cell count is 18, and that full coverage — not the raw count — is
  what forces the field).

**Scope.** None of the three verdict strings is affected: they say
`GRAMMAR-ADMISSIBLE-NOT-COMMITTED(d66'S-OWN-R=3-POINT-IS-COUNT-DEAD)`, which
is true and stays true. Necessity is unaffected. **The FOUND verdict is
unaffected.**

### MINOR-1 — the label and orient fibers are read at one base map

`_detect` (lines 1221–1224) computes `fib_label` and `fib_orient` at
`maps[0]` only, where `maps[0]` is fixed by `sorted(S, key=str)` — an
actor-name-order artifact. I measured both at *every* base map: constant at
`1` for R3-SAT (1296 maps) and at `2`/`1` for the falsifier (72 maps). The
published numbers are correct; the code does not measure that they are. Fix:
take the two fibers over all maps, or add a gate asserting base-map
invariance. One loop; no verdict moves.

### MINOR-2 — the receipt's `arena.q` is typed, not computed

Line 2140: `"q": ["1", "-1/2", "-1/2", "1"]`. The measured content is present
and correct one key away (`distinct_site_forms = [["1","1","-1/2","3/4"]]`),
and `MUT-DET-UNIFORM` guards the determinant, but the `q=[[1,-1/2],[-1/2,1]]`
that appears in the WELD3 verdict string is rendered from a literal. Fix:
build it from `q_of(nvec)` so the string cannot survive a moved form.

### MINOR-3 — §3.5's independence sentence is one cell wider than the measurement

> Each saturation is destroyed by the edit that moves its own variable and is
> untouched by the edit that moves the other's.

Three of the four cells are measured (151,632 / 151,632; 5,832 / 5,832; the
19,683-fold seed invariance). The fourth — the crystal is untouched by a
grouping transposition — is not run. It holds in the only sense in which it
is well posed: a transposition leaves the seed *sets* fixed as sets, so the
initiator field cannot move (I checked 648 edits on the first 8 crystals, 0
moved). But a transposition can move a seed out of its own group, so the
edited schedule is not always well formed. Fix: either add the fourth column
with that caveat, or narrow the sentence to the three columns actually
measured.

### MINOR-4 — 1296 is |Aut(K_{3,3,3})|, and FOUND at the stratum is entailed

Not a defect — a framing note the paper is one sentence away from making
explicit, and the candidate-readings rule bites hardest here. The rigidity
theorem forces the saturating arena's relation to be *exactly* the target's
Cayley graph, which is the complete tripartite graph K_{3,3,3}; so the
detector cannot return anything but FOUND there, at either reading, and the
map count cannot be anything but

```
|Aut(K_{3,3,3})| = 3! * (3!)^3 = 1296
```

The paper states the mechanism (§5.4, §5.7) but the verdict string presents
`ISOS=1296|QUOTIENT-MAPS=1296|FIBERS=1/1/1` as measurements of the weld. They
are consequences of the geometry census. Recommend naming 1296 as the
automorphism group of the complete tripartite graph in §5.4. This
**strengthens** the result — it is what makes FOUND window-free and
stratum-wide — but it should not be read as three independent data.

---

## 5. PROSE AUDITED AGAINST THE RECEIPT

Every numeral in the paper appears in the receipt (my independent scan: the
only non-hits are regex artifacts from `AG(2,3)` and `(1,1,1)`). All three
verdict strings render verbatim from receipt content. The mandatory Lorentz
naming sentence is present; the retracted L-1 sentence is absent. I7's
declared box (**361** admissible points), its readout re-encoding determinant
(**2**), its **11**-record family (9 homogeneous + 2 site-dependent) and the
fact that the induced `(1,1,1)` is admissible, inside the box, and hits none
of the 11 — all recomputed independently and all correct.

The only prose that does not survive the receipt is the two `18`s of
MAJOR-1 — and they do not survive because the receipt never computed them.

---

## 6. VERDICT

`WELD3-FOUND` is **sound and independently reproduced**. It is not window
relative, not naming relative, not smuggled by the site assignment, and it
survives even the strictest carrier reading. The geometry census, the
crystallinity census, the fragility contrast, both map censuses, all 18
census rows, all five controls and the R = 2 back-anchor reproduce exactly at
my hands, on machinery that shares no code with the unit.

**ACCEPT-WITH-FIXES.** MAJOR-1 must be repaired before terminal: it is a
false sentence with 46,584 counterexamples in the unit's own family, and one
of the counterexamples is a row of the unit's own census. The three MINORs
are cheap and none of them moves a number.

*Recomputations: 190. False numbers found: 1 (the `18`, twice in prose and
once typed in a gate's evidence). Verdict-bearing numbers found false: 0.*
