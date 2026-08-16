# SEC-2 (paper-40) — K1 OPERATOR review

**Seat:** K1 OPERATOR, three-seat hostile panel. **Method:** rebuild from
nothing, different primitives, no line of code, no input and no typed literal
shared with `sec2_exact.py`. Every number below is this seat's own, computed in
exact integer/rational arithmetic by six scripts written for this review.

**Objects verified open, sha256-12, against the mandate:**
`v14/paper-40-sec2.md` **aeeeb6757715**, `v14/code/sec2_exact.py`
**4cb4011cfa05**, `v14/code/sec2_output.txt` **57c98674b479**,
`v14/code/sec2_receipt.json` **b66fdfaacc33**, `v14/note-sec2-pin.md`
**bfe5c66be9ec**. Authorities also verified: `v14/note-sec-adjudication.md`
**7a82ffe7168a**; the pinned sources `paper-19-r3-weld.md` **50bb81e67942**,
`paper-27-smu.md` **6df0db523d32**, `paper-30-lor.md` **0a08203b7e99**; the four
#301 SEC objects read only by `git show 88e4a834f532:` and matching their
declared digests **cfe0825d67b2 / 6481a8706503 / e80d2f08a257 / fdf66d990dbf**.
No worktree SEC file was opened.

---

## GRADE: **AWF** (accept with fixes)

Three majors, nine minors, all with lifted repairs. **No delivered number
moves.** Every measured claim in all four verdict strings reproduced under an
independent rebuild, including the sharpest one, which I found to be *stronger*
than the paper states. The majors are one false prose numeral, one table whose
two columns are properties of the run's representative rather than of the class
they head, and one load-bearing convention that is never named although the
headline's first number depends on it.

**Between delivery and adjudication this review's findings are themselves a
candidate reading.**

---

## 1. What reproduced (the substance)

Built from scratch: two copies of AG(2,3) on Z₃² with the declared directions
(1,0), (0,1), (1,1); gluings as partial injections with |dom| ≤ 3; the union,
its seams, its charts, its detector, its automorphisms.

| delivered claim | this seat's independent value |
|---|---|
| 45,010 gluings, 16 types | 45,010 by enumeration **and** by Σ C(9,k)·9!/(9−k)!; 16 types, all 16 rows of §5's table (gluings / carriers / realised / doubled) identical |
| 132,273 shared sites | 132,273 (= Σ k over the family) |
| **49 seam types, (2,2,2) never** | **49**, all 49 populations identical to §3.2 (42606 / 7533 / 3483 / 486 / 162 / …); (2,2,2) absent on both sides; seven of eight vectors on each side |
| rank 6 on 10, kernel 4, at every seam type | rank 6, kernel 4 by explicit row reduction on Sym²(Q⁴) with no right-hand side; the ladder 0→4 cross links gives kernel 4, 3, 2, 1, 0 |
| completion lattice 31–275 admissible, 31–267 PD | identical at all 49 rows (31/31, 49/49, 103/103, 79/73, 155/141, 275/267); box widened by 2 returns the same set at all 49 |
| positivity non-selecting; adm ⟹ pos at 13 of 49 | min PD over the 49 = **31**; adm = PD at exactly **13** rows, exactly those with an all-simple side |
| convention-free price constant | the two-sided cross budget is a single value at **49 of 49** seam types (it is 2·Σ(nAᵢ+nBⱼ), free of the completion) |
| one-sided minimiser 8 → disjoint 8 | **8** and **8**, disjoint, at the all-simple seam (see m-1 for scope) |
| refinement empty by the ceiling law | union minimum count = **1** at every one of the 45,010 gluings → ceiling 0 |
| hypothetical refinement: 48/49 empty, direct sum at the 49th | nonempty at exactly **1** of 49, and there it is the direct sum and nothing else |
| max-determinant selects the direct sum 49/49 | unique argmax = the direct sum at **49 of 49** |
| SEC's witness outside the admissible lattice | Q(v) at (2,1,−1,−2) = **−2**; returns all six declared counts; **4** of its 18 cross counts are 0 → inadmissible; not PD |
| **the driven crossing cuts 31 → 8, all PD, direct sum excluded** | **confirmed, and stronger** — see S-1 |
| 455 groups, 9 orbits, sizes 108/108/72/54/36/36/36/4/1 | identical, with all four census columns (charts, crossings, within-sector new, doublings) identical |
| \|Aut(union)\| = 62,208 | 62,208 by backtracking search **and** by the closed form 2·(432²/6) |
| 288 seam-spanning, all dead at the delivered target | 288, none ALIVE |
| 216 lawful at the matched extension, 72 dead | 216 / 72, and the 72 are exactly the within-sector openers |
| 54 non-crossing controls ALIVE | 54, one orbit, all with 0 crossings and 0 within-sector new pairs |
| the 30-cell window grid | all 60 fates (baseline + driven) identical, cell for cell |
| QUOTIENT+POSITIVE ≡ EMBEDDING on liveness | agrees at 5 of 5 targets, by two procedures |
| inventories 62208 / 1728 / 1728 / 576, fibers 1·1·1, 1·1·1, 3·9·4, 1·3·2, free 0/0/3/2 | identical at all four arenas |
| blindness 36→1 arena, 630→5, 7140→15; sweeps 36/36 and 108/630 | identical; orbit sizes at two crossings 216/162/108/72/72; the driven pair's orbit is the 108, agreeing with the detector's 108 by different machinery |
| the five price laws, zero violations | 0 violations over all 45,010 composites × 5 currencies, each recomputed from the union object rather than from the law |
| seam-confinement of the surcharge | an unshared site's system is 3 equations on 3 unknowns, **rank 3, kernel 0** — determined, and its cells can never double (doubling needs both endpoints shared), so its form is the lone sector's exactly |
| the 22 inherited SEC values | all 22 match the committed #301 receipt key-for-key **and** are re-derived here from this seat's own construction |
| 12 union arenas, 4 mirror pairs | 12, 4, with the identical class partition |

Additional reproductions: |Aut(sector)| = 1296 by brute force over all 9!
permutations; the LOR ceiling-law quotation occurs verbatim exactly once in
`paper-30-lor.md`; the "eight verbatim anchors" of §11 are eight.

**Recomputation count: 558 delivered quantities re-derived from scratch** —
every data cell of every table, every numeral of the four verdict strings, and
the 22 inherited values. **555 reproduce exactly**; the 3 that do not are M-2
(they are table cells about the *declaration*, not about the physics, and they
move no fate). Beyond the delivered set this seat ran a further ~228,000 exact
measurements (the 455-group census without the orbit shortcut; 216 inventories;
42 window-target members × 12 fates; 18 cross directions × 3 predicates; six
extremal principles × 49 seam types; the 45,010 × 5 price evaluations; the
alternative seam convention).

---

## 2. MAJORS

### M-1 — §1 states a measured shortfall that is false ("six equations short")

> The seam's own form was six equations short of determined

The seam system is **6 equations on 10 unknowns, rank 6, kernel 4**. Reaching
determination therefore needs **four** more independent equations, and SEC's own
ladder — reproduced here exactly — says so: cross links 0, 1, 2, 3, 4 give
kernels 4, 3, 2, 1, 0. The paper itself says "four" everywhere else: §2's arena
row ("the completion of the seam's **four** undetermined entries"), §3.5 ("the
kernel falls from 4 to 3"), §5 ("four numbers each, twelve at a k = 3 seam"),
§8's inventory row. Six is the number of equations the record *supplies*, not
the shortfall.

**Why it survived the run.** §11's numeral coverage scans "spelled numerals
above twelve". *Six* is below the floor, so no gate ever met it. This is the
exact gap the finding sits in.

**LIFT (either):** "was **four** equations short of determined"; or, if the
intended sense was the supply, "carried six equations and stood four short of
determined". **And** lower the spelled-numeral floor to one, or bind §1's
numerals to the receipt as the tables are bound.

### M-2 — §4.2's window table publishes two columns that belong to the run's representative, not to the class they head

**(a) "declaration fiber" counts declaration *forms*, not distinct declared
targets.** Measured here, over the same (seam, direction-pair) declaration route
the instrument uses:

| target | declarations | **distinct targets** |
|---|---|---|
| ONE-AT-ONE-SEAM | 27 | **24** |
| ONE-AT-EVERY-SEAM | 9 | **8** |
| SEAM-MAP | 6 | 6 |

The three ONE-AT-ONE-SEAM collisions, explicitly: declarations (seam 0, dir 0,
dir 0) and (seam 1, dir 1, dir 1) both declare the link {A(1,0), B(1,0)};
(0,1,1) and (2,0,0) both declare {A(0,1), B(0,1)}; (1,0,0) and (2,1,1) both
declare {A(2,2), B(2,2)}. The ONE-AT-EVERY-SEAM collision is (0,0) with (1,1).

**The paper's own table carries the refutation.** Its FULL-CROSS row publishes
**24** declared links for "every forward cross direction at every shared site" —
which is precisely the number of *distinct* one-link declarations. If there were
27 of them, FULL-CROSS would carry 27.

Both fibers are **typed literals** in `sec2_exact.py`'s `WINDOW_TARGETS` (the
`27` and the `9` beside `cross_at(...)`), against the standing rule that counts
are computed and never typed. By the corpus's own fiber convention (paper-19
§5.4: a fiber is the number of *distinct objects a choice produces*), 27 and 9
are not fibers of anything.

**(b) "declared links" at SEAM-MAP is a property of one of its six members.**
SEAM-MAP declares a bijection of the two charts' three link directions at every
seam. Measured over all six bijections: the identity gives **6** links; the other
five give **9**. The published row says 6.

**What does not move.** I put every member of every non-trivial target family
through all twelve fate cells — 27 + 9 + 6 = 42 declarations × 12 fates = 504
measurements. **Every family is fate-homogeneous**: ONE-AT-ONE-SEAM returns the
published row at all 27, ONE-AT-EVERY-SEAM at all 9, and SEAM-MAP at all 6
including the five 9-link members. So M-2 is a table-and-scope repair, not a
verdict move.

**LIFT:** compute both columns. Publish the fiber as distinct targets (1, 24, 8,
6, 1), keeping the declaration count beside it if the declaration route is what
is meant; and at SEAM-MAP either name the identity bijection as the member run
(and say the other five carry 9 links) or publish "6 or 9" with the measured
homogeneity of fates. One sentence covers both.

### M-3 — the convention that produces "49 seam types" is never named, and the alternative reading gives 37

§3.1 defines a seam's type as "the pair of count vectors its two charts carry on
their three declared links". A site has, in each chart, *six* neighbours along
those three directions. Two readings are available and they do not agree:

| reading | seam types |
|---|---|
| **FORWARD** — the count at (site, direction) is the count of the cell {x, x+d}, I7's own 27-cell structure | **49** |
| BOTH SIGNS — the direction reads 2 if either {x, x+d} or {x, x−d} is doubled | **37** |

The delivered census is the FORWARD one: I reproduced all 49 populations exactly
under it, and 37 types under the other. Both censuses cover the same 132,273
sites; only the type function differs. The forward reading *is* derivable from
the paper's own arena row ("the 54 (chart, site, link) cells") and is the right
one — but the number it produces is the first number of the first verdict
string, and no sentence of the paper tells a reader which reading produced it.
This is §15's "match every coordinate" applied to the headline's own coordinate.

**LIFT:** one clause in §3.1 — "…on its three declared links, a link being the
cell (site, direction) that I7's lattice carries, so the count at x in direction
d is the count on {x, x+d}" — and, if cheap, a gated row recording that the
both-signs reading returns 37, since the verdict quotes 49.

---

## 3. MINORS

**m-1 — §3.3's "eight completions" is unscoped.** The one-sided minimiser is 8
at the all-simple seam; over the 49 types the argmin size ranges **4 to 80**
(4 at ((1,1,1),(1,1,2)), 80 at ((2,2,1),(2,2,1)) — measured at all 49). The
sentence sits in a paragraph whose previous claim is explicitly "at every seam
type", so the scope reads across. The *disjointness* under sign reversal **is**
general: forward and reverse minimising sets are disjoint at 49 of 49. The
receipt's `plus_argmin`/`minus_argmin` are aligned-seam values without a scope
key. **LIFT:** "at the all-simple seam the minimum is attained at eight
completions rather than one, and at every seam type reversing the sign
convention moves the minimising set to a disjoint one."

**m-2 — "THE ONE PRINCIPLE THAT DOES SELECT" is a uniqueness claim over an
unquantified space.** Four criteria were measured; the verdict generalises to
all principles. I attacked it with five more on the same lattices: minimum
determinant (never a unique argopt), maximin cross count and minimax cross count
(unique at only **16 of 49**), maximum two-sided budget (never unique) — **the
claim survives all four**. The only other 49/49 selector I could construct,
"minimise Σ|cross entry|", is question-begging (it is the distance to the direct
sum). Report as *survived*, and scope the wording. **LIFT:** "of the criteria
measured here, the one that does select…".

**m-3 — the Fischer attribution does not cover the whole measured set.**
Fischer's inequality is a statement about positive semidefinite matrices; the
admissible lattice contains completions that are not PD (6 of 79 at
((1,1,2),(1,1,2)), 14 of 155, 8 of 275, at 36 of the 49 types). Measured here:
**no** non-PD admissible completion has positive determinant at any seam type,
so the maximum is still the direct sum — but by measurement, not by Fischer.
**LIFT:** "…Fischer's inequality doing the work on the positive-definite points,
and the census covering the rest."

**m-4 — the orbit shortcut is not gated.** The lawful/dead columns and every
inventory are computed at **one representative per orbit**; the run's invariance
check (`orb_checked`) compares only the **first two** members of each orbit, and
only their (crossings, within, doublings) counts — never the fate, never the
inventory. The conjugation argument is sound, and I confirmed it by brute force:
censusing all **455** groups one by one with no orbit shortcut returns 216
lawful, 0 motivated, 54 controls, 72 dead, and inventories exactly
(1 cross link, 1728 maps, 3, 9, 4, free 3) ×108 and (2, 576, 1, 3, 2, free 2)
×108. The numbers are right; the gate is short of them. **LIFT:** extend the
invariance check to the fate and the free-item count, at every member.

**m-5 — "MOTIVATED AT 0 OF 216" mixes units.** The numerator is a count of
lawful *orbit rows* (`len(motivated)`), the denominator a count of *groups*
(`sum(orbit_size)`). Zero is zero, so nothing moves; but a single motivated orbit
would have rendered "1 OF 216" against a true 108. This is #87 (gates bind
objects, not cardinalities) at the rendering layer. **LIFT:** sum `orbit_size`
over the motivated rows.

**m-6 — an inherited standard is weakened silently.** The direction-label and
orient fibers are read at `ms[0]`, one base map. Paper-19 measured their base-map
independence ("re-read at every one of the 1,296 base maps and both are
constant") and said so. Measured here over **all** maps: LABEL 9 and ORIENT 4 at
every one of the 1,728 maps of the shared-seeded arena, LABEL 3 and ORIENT 2 at
every one of the 576 of the B-seeded one. True, but unmeasured in the delivered
run. **LIFT:** sweep it (it is cheap) or name the reading as read-at-one-map.

**m-7 — the blindness census and the target axis run on different placement
spaces.** The blindness census sweeps **36** placements (every A-only × B-only
pair); the window's targets can declare only the **24** forward cross directions
at the seams. The 12 that no target can declare are the backward ones — excluded
by exactly the sign convention §3.3 elsewhere prices as convention-dependent.
The conclusion is unharmed (all 36 lie in one Aut-orbit, so any two placements
are conjugate), but §4.4's 36 and §4.2's 27/24 are never reconciled, and §8's
inventory row publishes 36 for "the placement of a declared cross link" while
§4.2 publishes 27 for what a reader takes to be the same choice. **LIFT:** one
sentence in §4.4 naming the two spaces and the convention that separates them.

**m-8 — §4.5's mechanism sentence misdescribes what was measured.**

> no cross-link declaration repairs a lattice that has lost a link of its own

Nothing is lost. The 72 dead groups **open** a pair inside one sector — two
actors of a single tripartite class, a pair the lattice does not carry — so the
record gains an edge the extended target still lacks. **LIFT:** "…repairs a
record that has gained a link of its own that the lattice does not carry."

**m-9 — output rendering.** `sec2_output.txt` line 39 reads "the driven crossing
cuts the aligned lattice 31 -> 8 and EXCLUDES the direct sum (False)": the
trailing `(False)` is `direct_sum_after_crossing` printed raw and reads as a
negation of the sentence it terminates. Output only; the paper is clean.
**LIFT:** render "direct sum in the cut lattice: no".

---

## 4. Strengthenings this seat found by attacking

**S-1 — the sharpest claim is sharper than delivered.** §3.5 places the cut at
the crossing the grammar drives, "the shared site's third A-neighbour to its
third B-neighbour" — which I confirm is exactly the link `cross_at(0,(2,2))`,
and exactly the SHARED-SEEDED group's foreign pair. But the cut is not a
property of *that* direction. Measured at **every one of the 18 cross directions
of the chart** (9 direction pairs × 2 signs): each forces one cross count to 1,
each cuts the all-simple lattice **31 → 8**, **all 8 are positive definite** at
every one, and **the direct sum is excluded at every one** (it has u ≡ 0, and
every such constraint requires |u| = 1 somewhere). The result is
placement-independent — the same fact §4.4's blindness census reaches on the
other route, and the paper can say so.

**S-2 — §3.3 and §3.5 are the same eight completions, unremarked.** The
forward-budget minimising set at the all-simple seam is exactly
{u : u₃₃ = +1} — which is exactly the 8-completion lattice the driven crossing
cuts to; the reversed convention gives {u₃₃ = −1}. The "criterion whose argument
moves with a convention" and "the lattice the measured crossing leaves" are one
set. Worth a sentence: it explains why the one-sided price is convention-bound
(the convention is a choice of which cross direction counts as realised).

**S-3 — the driven-events reconstruction binds.** Deviation 3 says the grammar
is not re-driven and the two admitted specifications are reconstructed as arena
objects. Rebuilt independently from SEC's declared groups: SHARED-SEEDED
{A(1,1), B(1,1), S(0,0)} deposits 1 crossing and 2 doublings, B-SEEDED-PURE
{A(1,1), B(1,1), B(1,0)} deposits 2 crossings and 1 doubling — reproducing SEC's
`new_pairs` 1 and 2 and `foreign_pairs` 1 and 2 exactly, and landing both in
ALIVE orbits (both among the 216). The binding the deviation claims is real.

---

## 5. Licensed replacements

Nothing in the four verdict strings needs replacing on the measurements: all
four survive an independent rebuild. Two wording repairs are licensed inside
them, neither changing a number:

1. Verdict 1: `THE ONE PRINCIPLE THAT DOES SELECT, MAXIMUM DETERMINANT` →
   `THE ONE OF THE CRITERIA MEASURED THAT DOES SELECT, MAXIMUM DETERMINANT`
   (m-2), and the head's `49 SEAM TYPES` should be reachable from a stated
   convention (M-3), which is a paper-body repair, not a head repair.
2. Nothing in verdicts 2, 3, 4. The M-2 repair lands in §4.2's table and §8's
   inventory row; the M-1 repair in §1.

---

## 6. Method, and what this seat did not do

Six scripts, all in scratch, none importing or reading `sec2_exact.py`:
`k1_arena.py` (family, types, price laws), `k1_seam.py` (both seam conventions),
`k1_lattice.py` (completion lattices and the four criteria), `k1_cut.py` (the
crossing cut and the SEC witness), `k1_union.py` (Aut, group census, window,
blindness, inventories), `k1_rank.py`/`k1_arenas.py`/`k1_allgroups.py`/
`k1_probe.py`/`k1_sweep.py` (row reduction, arena collapse, the un-shortcut
census, the principle probe, the numeral sweep). Different primitives
throughout: my detector's QUOTIENT+POSITIVE branch, automorphism search, orbit
machinery, canonical types and Gram handling were written independently and
agree with the delivered fates cell for cell.

Not this seat's business, and deliberately not done: the seal/coverage/CLI
audit (K3's), the meaning-and-scope inventory (K2's). One observation for K3
only: an off-tree, git-less byte-reproduction run of `sec2_exact.py` was
launched from a clean scratch copy of the tree and was still executing its
mutant sweep at the close of this review; it is reported as **in flight, not
concluded**, and no byte-identity claim is made here either way. The repo tree
also carried other units' uncommitted edits and at least one concurrent
`sec2_exact.py` process during this review; nothing was written to the tree from
this seat except this file.

---

## 7. Verdict of this seat

**AWF.** The physics reproduces. `SEAM-DECLARATION-IRREDUCIBLE` holds against an
independent lattice census at all 49 seam types and against five extremal
principles beyond the four the paper measured.
`GLUING-EVENT-LAWFUL-AT-THE-MATCHED-CROSS-LINK-EXTENSION` holds group by group
over all 455 conflict groups without the orbit shortcut the run uses.
`COMPOSITE-PRICE-SPLITS` holds with zero violations over all 45,010 composites in
five currencies recomputed from the union object. `BLIND-AT-ONE-CROSSING-AND-
SIGHTED-AT-TWO` holds by both routes, with the two independent counts (orbit 108,
detector 108) agreeing. The single sharpest claim in the unit — the driven
crossing cutting 31 → 8 and excluding the completion SEC declared — is not only
true but true at every cross direction of the chart.

The three majors are a false spelled numeral in §1, a table whose declaration
columns describe one member of each class rather than the class, and an unnamed
convention on which the headline's own "49" depends. None of them moves a fate,
a lattice count, a price or a verdict.
