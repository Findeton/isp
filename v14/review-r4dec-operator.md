# PAPER-21 (R4DEC) — K1 OPERATOR HOSTILE REVIEW

**Seat:** K1 OPERATOR, panel per v14 ledger #203.
**Object at `f45b3a1`:** `v14/paper-21-r4dec.md` `f54dad8d51b8` ·
`v14/code/r4dec_exact.py` `e387674bfcdd` · `v14/code/r4dec_output.txt`
`27ed73ded234` · `v14/code/r4dec_receipt.json` `e1f148dd6a0e`.
**Pin:** `v14/note-r4dec-pin.md` `f50630ced3be` (commit `d55571d`).
All five sha256-12s verified at open and again at close; unchanged.

**Method.** Every decisive object was rebuilt from nothing with independent
machinery — my own partition enumerator, my own cell↔edge map, my own packed
and vector censuses, my own isomorphism enumeration by brute force over all
9! bijections, and a **prune-free meet-in-the-middle** covering census that
shares no bound, no branch and no ordering with the delivered
branch-and-bound. The only things read out of `r4dec_exact.py` were four
*definitions* (`count_field`, `graph_isomorphisms`, `quotient_bijections`, the
fiber accounting), never a result. Parents were read at their own pinned
bytes: I7 (`v13/code/ha_successor_receipt.json` `542b8735daf0`), paper-19 and
its receipt, papers 04/06/09 and their receipts, d66's committed output.

---

## GRADE: **AWF** (accept with fixes)

**Recomputations: 131. Disagreements with the delivered numbers: 0.**
**MAJOR: 0. MINOR: 6** — all textual scope/attribution/disclosure repairs;
**no number moves and no verdict moves.**

Every headline in all four verdict segments reproduces exactly. The
saturation theorem — the load-bearing licence for stage 4's exhaustiveness —
is not merely sound, it is **stronger than the paper states**. The covering
census reproduces at 100,080 by a route with no pruning at all. The
delivery run reproduces **byte-identically off-tree with no version control
present**. Two mutants of my own design, outside the declared 50-mutant
registry, both die at named gates with the artifacts untouched.

---

## 1. STAGE 1 — THE 276 (three routes, plus the saturation theorem)

| object | paper | K1 route | agree |
|---|---|---|---|
| round family, enumerated | 280 | 280 | ✓ |
| round family, closed form 9!/(3!³·3!) | 280 | 280 | ✓ |
| incidence spectrum over the 280 | 1@0, 27@4, 54@6, 162@7, 36@9 | identical | ✓ |
| saturating partitions | 36 | 36 | ✓ |
| ordered grouping quadruples 280⁴ | 6,146,560,000 | 6,146,560,000 | ✓ |
| saturating quadruples 36⁴ | 1,679,616 | 1,679,616 | ✓ |
| schedules/round; R=4 family | 7,560; 3,266,533,992,960,000 | identical | ✓ |
| **G-FLAT quadruples, packed route** | **276** | **276** | ✓ |
| **G-FLAT quadruples, vector route** | **276** | **276** (meet-in-the-middle, own packing) | ✓ |
| the two routes agree *as sets* | — | **identical 276-element sets** | ✓ |
| grouping multisets / orbit sizes | 12; (12,1),(24,11) | 12; (12,1),(24,11) | ✓ |
| collinear multisets / non-collinear | 1 / 11 | 1 (= COL,ROW,DIA,DIA) / 11 | ✓ |
| the 11 contain non-AG(2,3) groups | yes | 11 of 11 | ✓ |
| induced field / det / posdef | 27 of 27; det 1 at 9/9; posdef 9/9 | identical, and **all 276** induce it | ✓ |

A **third, fully independent** confirmation of the 276 falls out of my
stage-4 census, which never mentions G-FLAT: the homogeneous covering row for
(1,1,2) is exactly 276. The paper claims this ("arrived at a second time from
a census that never mentions G-FLAT") and it holds.

### THE SATURATION THEOREM — attacked hardest, and it survives with margin

The theorem as delivered: *no round deposits more than 9 link incidences; four
rounds carry at most 36; G-FLAT needs exactly 36; equality forces every round
to saturate; so the 36⁴ census is exhaustive over all 6,146,560,000.*

I attacked it at four points and it holds at all four:

1. **Is 9 really the ceiling, and is it structural?** A round is three triples;
   each triple contributes exactly 3 unordered pairs, so 9 pairs per round.
   Distinct pairs are distinct edges, and I verified **cell ↔ edge is a
   bijection** on the 27 declared cells (and that the 36 edges of K₉ split
   27 declared + 9 foreign). My builder carries an assertion that no round
   deposits twice on one cell; it never fired over all 280 partitions. So a
   round's field is 0/1 and its weight is ≤ 9, attained 36 times.
2. **Is the equality argument tight?** Total = Σ per-round weights. G-FLAT's
   27-vector sums to 9·1 + 9·1 + 9·2 = 36. Hence all four rounds saturate.
3. **The margin is bigger than the paper says.** The next spectrum value below
   9 is **7**, not 8. So a quadruple containing any non-saturating round totals
   at most 3·9 + 7 = **34 < 36** — a gap of 2, not 1. The theorem is robust to
   an off-by-one anywhere in the ceiling. *(Registered as a strengthening the
   paper may claim; it does not need it.)*
4. **Empirical corroboration outside the stratum.** 3,000,000 quadruples drawn
   at random from the full 280⁴ family and *filtered to contain at least one
   non-saturating round*: **0 G-FLAT hits.**

**Verdict on the theorem: SOUND. It carries stage 4's exhaustiveness licence,
and the licence is not close to its margin.**

### The driven column, and what I could and could not rebuild

FORCED 600/600 needs the committed d42b1 transport layer and is not
independently rebuildable inside this seat's scope. What I did establish:

- **Off-tree, git-less byte reproduction.** A mirror provisioned by
  `git archive f45b3a1` (no `.git` present) ran the delivery to completion and
  produced `r4dec_output.txt` = `27ed73ded234…` and `r4dec_receipt.json` =
  `e1f148dd6a0e…`, **sha256-identical to the committed artifacts**.
- **The window arithmetic is mine, and it closes.** 4⁴ = 256 class quadruples;
  the class∩G-FLAT overlap is exactly **12** (only the collinear multiset has
  all four rounds a parallel class), so W4-FLAT contributes **264** new; the
  seed fan 3⁴ = 81 contributes **80** new; **256+264+80 = 600**, spanning
  **256+264 = 520** grouping quadruples, and the driven G-FLAT set is
  **276+81−1 = 356**. All four numbers as published.
- **The anchor is genuinely bound to d66's bytes.** `v10/data/d66_arbitration_crystal_exact.out`
  (sha `e252529d2586`, as declared) line 60 reads `GRID(g=3,R=4) n= 66 arb 0.1818`;
  0.1818 × 66 = 12 arbitrations, and 66 − 12 − 36 = 18 deliveries. The
  published row (66, 12, 18) is read, not typed.
- **The length spectrum is structurally consistent.** 12 arbitrations + 36
  proposals = 48 forced events, so lengths must be 48 + deliveries. The
  published spectrum {48,54,60,61,62,63,64,65,66} gives deliveries
  {0,6,12,13,…,18}, maximum 18 — exactly d66's own committed delivery count.
  The spectrum sums to 600.

---

## 2. STAGE 2 — THE WELD

Rebuilt with my own brute-force isomorphism enumeration over all 362,880
bijections and my own count-field.

| object | paper | K1 | agree |
|---|---|---|---|
| isomorphisms @EMBEDDING | 1296 | 1296 | ✓ |
| quotient maps @QUOTIENT | 1296 | 1296 | ✓ |
| = \|Aut\| of the target | 1296 | (3!)³·3! = 1296 (K₃,₃,₃) | ✓ |
| directed comparator | 0 | 0 | ✓ |
| count cells / min / max | 27 / 1 / 2 | 27 / 1 / 2 | ✓ |
| induced record at the base map | (1,1,2) | (1,1,2) | ✓ |
| I-SITE-ASSIGNMENT | 36 | 36 | ✓ |
| I-DIRECTION-LABEL | 3 | 3 | ✓ |
| I-ORIENT | 1 | 1 | ✓ |
| label / orient spread over the 1296 | [3,6] / [1,2] | [3,6] / [1,2] | ✓ |
| free items at **every** base map | ≥ 2 | min = 2 | ✓ |
| assignment fiber: fields / homogeneous / inhomog. | 36 / 3 / 33 | 36 / {(1,1,2),(1,2,1),(2,1,1)} / 33 | ✓ |
| every field in the fiber admissible | yes | 36 of 36 | ✓ |
| R3-SAT control | FOUND, fibers 1/1/1, invariant | isos 1296, quots 1296, 1/1/1, spreads [1]/[1], free items 0 | ✓ |
| R4-ONE-ANT control | 27 incidences, field ≡ 1, 9 foreign, STRUCT-DEAD both | identical; isos 0 and quots 0 | ✓ |
| R4-COMMITTED-GRID(3,4) | STRUCT-DEAD / COUNT-DEAD | field (2,2,0), 18 of 27 cells | ✓ |
| R4-FLAT-FALSIFIER | STRUCT-DEAD / COUNT-DEAD | 24 edges → isos 0; quots 1296 with 3 zero cells | ✓ |
| ARITY probe | ARITY-DEAD both | 8 objects vs 9 sites | ✓ |

### The two theorems

**(a) Zero free items ⟺ link-constant record.** Rebuilt from scratch and
verified *over I7's whole declared count box*, not just at the target:

- The realised relation's edge orbit under its 1296 automorphisms is **27 of
  27** — edge-transitive, as claimed.
- Sweeping all 432 box points (1 ≤ n_e1,n_e2 ≤ 6, 1 ≤ n_diag ≤ 12): the
  records with `I-SITE-ASSIGNMENT` fiber 1 are **exactly** the six
  (n,n,n), n = 1…6, and `I-DIRECTION-LABEL` fiber 1 selects **the identical
  set**. Both directions of the iff hold.
- I7 declares **0 of 9** link-constant homogeneous records (I read its
  `records_d2` block directly: (1,4,5), (4,9,13), (2,2,4), (1,1,2), (1,1,6),
  (2,2,6), (3,5,12), (3,5,4), (1,1,4) — none constant), while its own box
  holds **6** admissible link-constant points. Fiber at (1,1,1) = 1; fiber at
  G-FLAT = 36. All as published.

**(b) Link-constancy arithmetically impossible at R = 4.** 36/27 = 4/3, not an
integer; 27/27 = 1, forced. Correct — **subject to a premise the paper's own
blockquote drops** (MINOR-1 below).

**The 1296 = 1296 structure equality.** Confirmed: the realised co-division
relation *is* the complete tripartite graph on the ANT parallel classes, which
is precisely I7's Cayley incidence for its three declared links, so the
embedding and quotient map sets coincide and both equal Aut.

---

## 3. STAGE 3 — THE SPLIT

| object | paper | K1 | agree |
|---|---|---|---|
| split fiber > 0, (1,1,1) | 0 of 27 | 0 of 27 | ✓ |
| split fiber > 0, (1,1,2) | 9 of 27, fiber 1 each; 0 at 18 | (0,18),(1,9) | ✓ |
| the 9 are the diagonal intervals | yes | exactly the (1,1)-link cells | ✓ |
| raw product over 27 | 0 | 0 | ✓ |
| paper-06 at count 1 / count 2 | fiber 0, no orbit / fiber 1, 1 orbit, dim 0 = n−2, transitive | rebuilt from R6a's identity n−1 and CR-B's dim n−2 | ✓ |
| paper-04 ceilings on (a,a,2a) | [0,1,1,2,2,2] | ⌊log₂ min n⌋ = [0,1,1,2,2,2] | ✓ |
| first refinable member | (2,2,4) = G-DIAG2, 72 incidences, R = 8 | identical; 9·(2+2+4) = 72 = 8·9 | ✓ |
| concatenation witnesses | ≥ 76,176 | 276² = 76,176 | ✓ |
| paper-09 hole covers all 27 | yes | max count 2 ∈ {1,2} | ✓ |
| paper-09's 201 / 79 / 60 / 102 | as cited | all four present in `r6bp_transport_receipt.json` | ✓ |

**The four parent blockquotes are verbatim and correctly attributed.**
`v14/paper-04-refinement-grammar.md` L152 carries "3 of the 9 admissible
records carry a count-1 interval and admit no subdivision at all: G-ANISO,
G-CURVED, G-FLAT"; L131 carries the SINGLE-INTERVAL refusal sentence; L154
carries the floor-not-flatness sentence and the ceilings.
`v14/paper-06-stochastic-split.md` L80–81 carries CR-B's own version;
`v14/paper-09-renewal-transport.md` L144/L159 carry g(1)=g(2)=0 and the
support-hole sentence.

**Priority check on "first welded record with a positive split fiber."** Weld 2
reached (2,2,2) — which *does* have split fiber 1 at all 27 intervals and raw
fiber 1 — but paper-13 L725–727 states that witness sits "on a declared probe
rather than on a grammar record … the probe is not a weld and no verdict"
rests on it. The priority claim therefore stands.

---

## 4. STAGE 4 — THE PRICE ROW

Rebuilt **twice**, by two routes of my own. Route A is a **census with no
pruning at all**: all 78,400 ordered round pairs keyed by (OR, AND) → 39,340
distinct keys; per-cell bitsets over the keys; every compatible key pair
enumerated. Nothing can be missed by a bad bound because there is no bound.
Route B re-implements the *shape* of the delivered branch-and-bound in my own
code (the coverer index over all 2⁹ sub-masks, both budget prunes) and returns
the identical 100,080 with the identical (1,1,2) row of 276 — so the delivered
algorithm's pruning is not merely sound in principle, it is sound in the exact
form it is written.

| object | paper | K1 (prune-free) | agree |
|---|---|---|---|
| COVER-27 over all 6,146,560,000 | 100,080 | **100,080** | ✓ |
| POSDEF-9 | 100,080 | 100,080 | ✓ |
| I7-STRICT | 100,080 | 100,080 | ✓ |
| posdef-site distribution | single cell (9, 100080) | (9, 100080) | ✓ |
| det spectrum over 900,720 cells | 3/4@437,184; 1@386,640; 7/4@76,896 | identical (exact `Fraction`) | ✓ |
| homogeneous / inhomogeneous | 20,988 / 79,092 | 20,988 / 79,092 | ✓ |
| the four homogeneous records | (1,1,1) 20,160; (1,1,2) 276; (1,2,1) 276; (2,1,1) 276 | identical | ✓ |
| breaking codes inside the covering class | 0 occurrences | 0 | ✓ |
| reachable site codes R=3 / R=4 | 54 / 105 | 54 / 105 | ✓ |
| covered-but-not-posdef codes | (1,1,4),(1,4,1),(4,1,1), all det 0 | identical; and these are the **only** three in all of {1..4}³ | ✓ |
| G-SINGULAR among them | yes | (1,1,4) = I7's `G-SINGULAR` | ✓ |
| R=3 back-validation | 72 triples, 12 multisets | 72, 12 — **and re-run exhaustively over all 21,952,000** triples, not only the saturating cube | ✓ |
| R=2 back-validation | ceiling 3 at 252; 747 non-degenerate; I7-STRICT 0; wall 6 | identical; full distribution (0:49,996)(1:24,660)(2:3,492)(3:252) | ✓ |

I also re-derived paper-19's committed rows from its own receipt: `/geometry/
r4_register_probe/reaching_the_target_chart_orbit` = 276, `/geometry/
i7_strict_ordered_triples` = 72, `/geometry/r2_back_anchor` = wall/ceiling
[6,3], `nondegenerate_at_9` 747, `i7_strict` 0, `ordered_pairs` 78,400.

**Note on the algebra, in the paper's favour.** POSDEF-9 ⊆ COVER-27 is *free*:
q = [[n₁,(n₃−n₁−n₂)/2],[·,n₂]] positive definite forces n₁,n₂ ≥ 1, and n₃ = 0
gives det = −((n₁−n₂)/2)² ≤ 0, so n₃ ≥ 1 too. The measured half of the
coincidence is COVER ⟹ POSDEF, and that is exactly the half §6.2 explains by
the empty cell. The paper's framing is correct.

---

## 5. INSTRUMENT PROBES (this seat's share)

- **Off-tree / git-less byte reproduction: PASS.** Both artifacts sha-identical
  from a `git archive` mirror with no `.git`.
- **21 verbatim anchors, re-checked with my own markdown-prefix normaliser
  against the declared pinned source of each: 21 of 21 found in their own
  anchor.** V06 additionally appears in A-R3WEFF, V10/V11 additionally in
  A-P19 — no anchor is mis-homed.
- **Head/verdict block identity:** the paper's 8 fenced blocks are 4 distinct
  strings each appearing twice, **byte-identical** between the head and §9.
- **Numeral sweep:** 80 distinct numerals in the paper; **78 covered** by my own
  recomputations or by the delivered receipt. The two residuals are `82` (the
  `#82` RUNBOOK engraving) and `112` — an artifact of my own comma-stripping on
  the tuple "(1,1,2)". **No uncovered numeral.**
- **Two mutants outside the declared 50-mutant registry:**

  | mutant (mine) | edit | outcome |
  |---|---|---|
  | **O-1** | `price_census` depth-2 prune weakened by one cell (`> 2*maxinc` → `> 2*maxinc - 1`), making the branch-and-bound *unsound* — it silently loses the 216 covering quadruples that leave exactly 18 cells uncovered after two rounds | **KILLED at `G-HOMOGENEOUS-R4`**, exit 1, **ARTIFACTS-UNCHANGED**; the gate printed `homogeneous covering quadruples 20838 of 99864 … [[1,1,2], 274]` |
  | **O-2** | one saturating partition dropped from **both** census routes, so route 1 and route 2 agree on a wrong number | **KILLED at `G-276`**, exit 1, **ARTIFACTS-UNCHANGED**; the gate printed `route 1 264, route 2 264, paper-19's committed row 276, multisets 11` |

  O-2 is the sharper of the two: I predicted 264 and 11 multisets from my own
  census before running it (the dropped partition is the ROW parallel class,
  which occurs in exactly the 12 orderings of the collinear multiset), and the
  run matched both. It shows **where the binding actually lives**: not in
  route-1-vs-route-2 (a common-mode error passes both), but in paper-19's
  independently committed register row carried inside the same gate. That is
  the right design and it works.

### 5.1 O-1 — the census's cross-binding

O-1 is the interesting probe because deviation 3 claims "the pruning is the
budget theorem and nothing else … so no covering quadruple can be missed."
I made the pruning unsound and checked whether anything catches it. The
binding that must fire is in `G-HOMOGENEOUS-R4`, whose pass condition is
`homo_hist[FLAT] == n276` — the price census's own G-FLAT row is compared
against the stage-1 number. By my own arithmetic O-1 loses exactly **2** of the
276 (the two orderings of the collinear multiset with DIA in both of the first
two positions — the only quadruples in the 276 with a repeated round, since
distinct saturating partitions have distinct masks), so the census would report
274 against 276 and the gate must fail.

I fixed the prediction *before* the run, by emulating the O-1 prune inside my
own machinery: COVER-27 would read **99,864** (= 100,080 − 216) and the
(1,1,2) row **274**.

**Result: the live run died at `G-HOMOGENEOUS-R4`, exit 1,
ARTIFACTS-UNCHANGED, printing `homogeneous covering quadruples 20838 of 99864
over 4 records [[[1, 1, 1], 20016], [[1, 1, 2], 274], [[1, 2, 1], 274],
[[2, 1, 1], 274]]` — both predicted numbers, exactly.**

Two things follow, and the second is MINOR-6:

- `back_validation` does **not** share `price_census`'s prune (it enumerates
  directly), so the R = 3 / R = 2 rows would not have caught this. The
  cross-binding at the G-FLAT row is the load-bearing one, and it fired.
- **`G-PRICE-ROW` itself passed while reporting the corrupted total 99,864.**
  Its predicate compares COVER against POSDEF-9 and checks the posdef
  distribution — both of which stay internally consistent under an unsound
  prune. The run still died, correctly, one gate later. But the total
  100,080 has exactly **one** binding in this instrument and it is
  `G-HOMOGENEOUS-R4`'s `homo_hist[FLAT] == n276`.

---

## 6. FINDINGS

**MAJOR: none.**

### MINOR-1 — §4.3's blockquoted theorem drops its own premise, and the unit's own control is the counterexample

The bolded, quotable sentence reads:

> **A link-constant field is arithmetically impossible at R = 4, while at
> R = 3 the 27 incidences over 27 cells force one.**

As written this is false, and the unit itself measures the witness: the
**R4-ONE-ANT** quadruple ROW/COL/DIA/ANT deposits 27 incidences on I7's links
and induces the field **identically 1** — a link-constant field, at R = 4. It
dies at *structure* (its 9 foreign pairs), not at arithmetic. The preceding
sentence supplies the missing premise ("a **clean** R = 4 arena therefore
spreads 36 incidences over 27 cells") and the gate `G-CONSTANCY-IMPOSSIBLE`
carries the full chain, so nothing measured is wrong — but this is a
blockquote, and blockquotes are what successors inherit verbatim (this unit
inherits four of them). §9's read-out repeats it in the same compressed form.

**Exact repair.** §4.3, replace the blockquote with:

> **In a structurally admissible R = 4 arena — one whose realised pairs all lie
> inside the target's incidence, hence one whose four rounds all saturate — a
> link-constant field is arithmetically impossible, while at R = 3 the 27
> incidences over 27 cells force one.**

and append to it: *The premise is not vacuous and this unit measures why: the
one R = 4 quadruple in this census that does carry a link-constant field,
ROW/COL/DIA/ANT, buys it with nine foreign pairs and dies at structure.*
§9, amend "at R = 4 a link-constant field is arithmetically impossible anyway"
to "at R = 4 a *structurally admissible* arena's 36 incidences cannot spread
constantly over 27 cells".

### MINOR-2 — the headline fiber triple is read at one base map, and the coordinate is not named

`I-DIRECTION-LABEL 3` and `I-ORIENT 1` are computed at `maps[0]` — the first
bijection the enumeration returns — not at a canonical one. The paper
discloses the *spreads* [3,6] and [1,2] in the same breath, in both §4.5 and
the head, so nothing is hidden; but RUNBOOK §15 asks that every coordinate be
matched, and "at the enumeration's first base map" is the missing coordinate
for two of the three headline fibers. (`I-SITE-ASSIGNMENT` = 36 is base-map
independent and needs no such clause.)

**Exact repair.** §4.5, after "the three read **I-SITE-ASSIGNMENT 36,
I-DIRECTION-LABEL 3, I-ORIENT 1**", insert: *— the first read at every base map
and the other two at the enumeration's first, which is why the spreads below
are the invariant statement*.

### MINOR-3 — "the forced carrier" is two fixings, and the second is measured, not forced

§4.6 defines the strictest reading as "the site carrier fixed to the
constructor's own actor → Z_3^2 parse", then adds "with the direction labels
taken in I7's own declared order". The head compresses both into
`FOUND-AT-THE-FORCED-CARRIER`, while the choice inventory classes
`I-DIRECTION-LABEL` as **measured, fiber 3** (item 11).

I measured the datum that settles it and it is not in the paper: **the identity
parse is one of the 1296 isomorphisms, and at that parse the label fiber is
still 3.** So fixing the site carrier alone leaves the induced record ranging
over {(1,1,2), (1,2,1), (2,1,1)}, and it is the *second* fixing that selects
the declared one. The trade is fully disclosed elsewhere in §4.6 ("3 are
homogeneous and exactly one is a declared record"), so no claim is
overstated — but the head's phrase names one fixing where two are used.

**Exact repair.** §4.6, after the strictest-reading sentence, add: *Measured: the
identity parse is itself one of the 1296 isomorphisms, and at that parse the
label item still produces 3 distinct fields — so this reading fixes two
inventory items, the site carrier and I7's declared link order, and it is the
second that selects (1,1,2) from {(1,1,2), (1,2,1), (2,1,1)}.*

### MINOR-4 — "no typed target" reads stronger than it is, and it points at the wrong binding

§3.2: "Two routes that share no code, no packing and no typed target." Route 1
*does* type its target (`pack4(tuple([1, 1, 2] * 9))`); route 2 derives it from
I7's committed row. The sentence is literally true — they share no typed
target — but a reader takes it as "neither types one", and it invites the
inference that route independence is what binds the 276. My mutant O-2 shows
it is not: a common-mode edit passes both routes and is caught only by
paper-19's committed register row.

**Exact repair.** §3.2, replace with: *Two routes that share no code and no
packing: route 1 types the target field and compares packed integers, route 2
derives the target from I7's own committed row and compares 27-vectors entry by
entry, so no typed target is shared. What binds the number against an error
common to both is paper-19's committed register row, carried in the same gate.*

### MINOR-5 — §6.4's attribution of the R = 2 row is looser than the receipt supports

"…positive-definiteness ceiling of 3 with 747 pairs non-degenerate … the R = 2
ceiling is attained at **252** of the 78,400 ordered pairs against a wall of
18 // 3 = 6 … and it is U4b's committed row read from paper-19's receipt rather
than re-typed here." Paper-19's `/geometry/r2_back_anchor` carries
`committed_wall_and_ceiling [6,3]`, `posdef_ceiling 3`, `nondegenerate_at_9
747`, `i7_strict 0`, `ordered_pairs 78400` — but **not** the 252. The 252 is
this unit's own computation (I recomputed it independently: 252, with the full
distribution 0:49,996 / 1:24,660 / 2:3,492 / 3:252).

**Exact repair.** §6.4: "…the wall 6, the ceiling 3, the 747 and the empty
I7-STRICT are U4b's committed row read from paper-19's receipt rather than
re-typed here; the 252 at which the ceiling is attained is this unit's own
number."

### MINOR-6 — §11 should name where the 100,080's single binding lives

Found by mutant O-1 (§5.1). §11 lists the gates that "bind objects rather than
aggregates" — "the unit-grade, equality, forcedness, census-row, split-fiber
and sitewise gates" — and `G-PRICE-ROW` is correctly *not* among them. But the
consequence is not stated, and it is sharp: under an unsound prune
`G-PRICE-ROW` passes on a wrong total (it checks COVER against POSDEF-9 and
the posdef distribution, both of which stay internally consistent), and the
only thing that kills the run is `G-HOMOGENEOUS-R4`'s comparison of the
census's own G-FLAT row against `n276`. That is a good design — it is the only
independent handle available, since 100,080 is a new number with no committed
predecessor — but a successor weakening or re-scoping `G-HOMOGENEOUS-R4` would
silently unbind the price row.

**Exact repair.** §11, after "Gates bind objects rather than aggregates …",
add: *The stage-4 total is the one published number with no committed
predecessor to check it against; what binds it is the census's own G-FLAT row,
compared inside `G-HOMOGENEOUS-R4` against the independently computed 276, so
that an error in the search's pruning cannot survive to the artifacts.*
Register the same sentence in the successor's "what may not be inherited".

---

## 7. THINGS I TRIED TO BREAK AND COULD NOT

Registered so the panel does not re-spend them:

1. **A G-FLAT quadruple outside the saturating stratum.** Impossible with margin
   2 (34 < 36), and 3,000,000 random non-saturating quadruples confirm.
2. **A covering quadruple missed by the branch-and-bound.** My prune-free
   meet-in-the-middle returns the identical 100,080 and the identical field
   multiset.
3. **A fourth homogeneous record in the covering class**, or a fifth. Exactly
   four, and the (1,1,2) row is exactly 276.
4. **A code in {1..4}³ that is covered but not positive definite, beyond the
   three.** There are exactly three in the whole code space, not merely among
   the reachable 105.
5. **An earlier welded record with a positive split fiber** (weld 2's (2,2,2)).
   Paper-13 declares that witness a probe and explicitly "not a weld".
6. **A mis-homed verbatim anchor.** 21 of 21 found in their own declared source.
7. **An uncovered numeral.** None.
8. **A non-reproducing delivery.** Byte-identical off-tree with no VCS.

## 8. SUCCESSOR NOTE (not a finding)

One structural fact my census turned up that the paper does not report and
S-5 could use, measured: **the DIA parallel class occurs in every one of the
276 G-FLAT quadruples and in all 12 multisets** (276 of 276, 12 of 12). The
full diagonal line-partition is compulsory; the other three rounds are what
vary, and only the collinear multiset repeats a round (12 of the 276 have a
repeat, and they are exactly its 12 orderings — distinct saturating partitions
have distinct masks, 36 of 36). That is a sharper statement than "one of the
twelve is collinear", it explains why the diagonal is the link the budget
populates twice, and it is one line to gate.

---

## 9. ON THE DRIVEN COLUMN, RECORDED IN THE PAPER'S FAVOUR

My whole rebuild assumes the mechanism the paper states — *a division event's
footprint IS its conflict group* — and nothing else about the transport layer.
On that single assumption my machinery reproduced **every driven number in the
unit**: the (1,1,2) field at 27 of 27 cells, det 1 and posdef at 9 of 9, the
1296/1296 structure equality, the 36/3/1 fibers and their spreads, the arena
identity, the falsifier's 24 edges and 3 zero cells, d66's own (2,2,0) at 18
of 27, and the 9 foreign pairs of the ANT control. That is independent
corroboration of what `G-DRIVEN-EQUALS-COMBINATORIAL` measures at 600 records:
the combinatorial model and the driven record are the same object here. The
FORCED 600/600 column itself I could not rebuild in this seat — it needs the
committed d42b1 layer — but it is byte-reproduced off-tree, its window
arithmetic is mine, its anchor is bound to d66's committed bytes, and its
length spectrum is consistent with the 48 forced events the grammar requires.

---

*K1 OPERATOR. 131 recomputations, 0 disagreements, 0 MAJOR. Grade AWF: six
textual repairs, none of which moves a number or a verdict. Two out-of-registry
mutants, both killed at named gates with artifacts unchanged, both at numbers
predicted in advance. Object hashes re-verified unchanged at close:
`f54dad8d51b8` / `e387674bfcdd` / `27ed73ded234` / `e1f148dd6a0e`; pin
`f50630ced3be`.*
