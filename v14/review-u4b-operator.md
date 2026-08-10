# U4b (paper-17, the schedule census) — OPERATOR-LENS HOSTILE REVIEW

**Grade: AWF (accept with fixes).**

**Object, hashes verified at read time and again at write time:** paper
`v14/paper-17-schedule-census.md` `2bcba873d78e`, code
`v14/code/u4b_schedule_exact.py` `2c9b999dea31`, output
`v14/code/u4b_schedule_output.txt` `8715c46a7b7f`, receipt
`v14/code/u4b_schedule_receipt.json` `c4a4e8223b64`, all at commit `8c2dd98`;
pin `v14/note-u4b-pin.md` `d2cff9a274a8`, which reproduces its digest at the
commit the paper names (`42417f6`). All **10** declared runtime sources
hash-match their declarations, d42b1 `576275d55ecf` and d66 `3d0516ab106e`
among them. The three commits the paper cites as read-or-not-read
(`42417f6`, `06b89fe`, `58195da`) all exist and carry what the paper says they
carry.

**Recomputations: 200**, all exact (Python integers and
`fractions.Fraction`; no float anywhere in my chain either), all from a
rebuild that imports nothing from `u4b_schedule_exact.py` — plus **904
grammar records driven independently** through d42b1's own `candidates_for`
and **1 plain run** in scratch. The 200 break down as **153** gated
comparisons in three rebuild scripts, **16** auxiliary measured quantities,
**16** digest verifications (5 object + 10 source + the pin at `42417f6`),
**2** byte-identity checks, **9** verbatim-quote checks against source and
paper, **3** commit verifications and **1** whole-paper numeral audit.
**Two of the 153 gated comparisons failed and both were my own wrong
expectations, not paper claims** (the minimum per-partition link-incidence
count, which is 0 and not 6; and the affine split of the 540 window crystals,
which is 216 beyond-coset / 324 CU-JOINT). **Zero false numbers found. Every
delivered number in the paper, the output and the receipt reproduces
exactly**, and no finding below moves a computed value or changes a verdict
string.

**Byte-identity.** The plain run, executed only in
`…/scratchpad/u4b-op/repo/` on a git-less 12-file copy of the pinned tree,
exits 0 and writes `u4b_schedule_output.txt` `8715c46a7b7f` and
`u4b_schedule_receipt.json` `c4a4e8223b64` — **byte-identical to the committed
artifacts**. The repository working tree is untouched by me except this file.

**Disclosure.** Concurrent workers are active on other units (`giter_exact.py`,
`r5_gauge_exact.py`, `paper-16`); every byte I judged came from `git show` at
`8c2dd98`. HEAD was `a43748b` throughout. I have not read
`review-u4b-effectus.md` or `review-u4b-instrument.md`. My only repository
write is this file. Candidate-readings rule in force.

---

## 1. What I rebuilt, and how it differs from the instrument

Nothing in my chain shares code with the unit. Concretely:

- **The family** by two routes of my own — a recursive partition enumerator
  (280) and a factorial closed form `9!/(3!³·3!)·3³` (7560/round) — and the
  square taken independently.
- **The stabilizer** by three routes of my own: direct translation; the
  annihilator of the support of the Z₃² Fourier transform implemented in
  `Z[ω]=Z[t]/(t²+t+1)` as integer pairs `(a,b) ↦ a+bω` with `ω²=−1−ω`; and a
  subgroup-lattice walk taking the largest `H` on whose cosets the field is
  constant. **0 disagreements at all 7056 seed-set pairs.**
- **The grammar, loaded by a different route.** The unit cuts d42b1 as a
  *text slice* at the layer's banner print. I loaded it by **AST**, executing
  top-level `Import`/`FunctionDef`/`ClassDef`/`Assign` nodes one at a time and
  dropping the 53 nodes that are not those (or that need them) — so no
  module-level statement of theirs runs, by a mechanism independent of where
  the banner sits. Gated, not asserted: no `exit`/`quit`/`_exit` survives the
  strip. 157 nodes kept, 29 defs.
- **My own record builder**, not d60's `B`: menu from `candidates_for`, hits by
  exact tuple equality, refusal recorded and never patched.
- **The determinant** from HA 3.2's readout re-derived by hand from the paper's
  own statement of it, on the co-division adjacency built from scratch.
- **Two things the unit did not do**, both reported below: 250 random
  **family-wide** (out-of-window) schedules driven; and the fragility argument
  pushed from the window to the **whole family** by exhaustion over a superset
  of the admissible edits.

## 2. K1.1 — the family count, both routes: **CONFIRMED**

| quantity | route A (enumeration) | route B (closed form) |
|---|---|---|
| partitions of 9 sites into 3 triples | 280 | `9!/(3!³·3!)` = 280 |
| seeds per partition | 27 | 3³ = 27 |
| schedules per round | 7560 | 7560 |
| **the family** | **57 153 600** | **57 153 600** |

`(280×27)² = 57 153 600` by both. The 84 three-element subsets each transverse
**exactly 90** of the 280 partitions — I measured the weight set and it is the
singleton `{90}`, so the multiplicity 8100 and the identity
`7056 × 8100 = 57 153 600` are earned, not assumed. §2.2 and §4.2 are exact.

## 3. K1.2 — the window's licence: **CONFIRMED, but the licensing fact is misidentified** (F4)

I rebuilt the driven-vs-combinatorial equality with my own driver on a
**stratified sample of 208 window schedules** (all 16 class pairs × every
non-empty (crystalline × affine-class) bucket × up to 4 members each), on
**my own 20 stratum witnesses**, on the committed schedule, and on
ROW|ROW/DIAG. Every one: `maxhits = 1`, no refusal, exactly 6 division events,
driven initiator field **equal** to `1_{S₀}+1_{S₁}`, driven footprint field
**≡ 2**. Zero mismatches. The 24/30 event dichotomy reproduces exactly on the
window sample (64/144 at my sampling), and my own strata witnesses outside the
window show the intermediate lengths 26, 28, 29 that the window's parallel
classes cannot produce.

**The honest disclosure question.** The window is named in §2.4, in the
constructibility verdict string, and in Deviation 1. That is honest disclosure
for the *constructibility* column. It is **not** honest for the *fragility*
column — see F2.

**F4 (MINOR, but this is the unit's weakest joint).** §4.2 offers the
driven-vs-combinatorial equality as the *first of two facts* that "make the
column exhaustive over the whole family". It cannot carry that weight, because
**given a non-refused record the equality is a theorem, not a measurement**:
the driver specifies every event by its full tuple, `hits` is filtered by exact
equality, so `maxhits ∈ {0,1}` always and an appended event *is* the specified
tuple; the six arbitrations therefore have initiator = the declared seed and
`regs_of ∩ actors` = the declared group, for **any** schedule in the family.
The only way the equality can fail is a refusal. So the real licence for
exhaustiveness is **constructibility**, which is what is window-scoped — and
the inductive step "all 57 153 600 are constructible" is verified at 11 684 of
them. *I pressed that step:* **250 random family-wide schedules, drawn
uniformly over all 78 400 partition pairs and all seeds, all FORCED, all with
fields equal to the combinatorial ones** (event counts 26–30). The step
survives, but it is an induction and the paper should say so.
**Repair:** in §4.2 replace "Two facts make the column exhaustive over the
whole family" with the true structure — *(i)* full-tuple specification makes
the field a function of the schedule at every non-refused record (a theorem,
one line), *(ii)* constructibility is measured on the window and on 20
out-of-window strata witnesses, and *(iii)* the exhaustive columns therefore
inherit the window's induction, not its measurement.

**F5 (MINOR).** For the same reason the `BRANCHING 0` cell of the
constructibility verdict is a **structural zero, not a measurement**: with
full-tuple specification at most one candidate can ever match — `candidates_for`
generates each event tuple once, and `maxhits ∈ {0,1}` at every pick of every
one of my 904 driven records — so no schedule in the family can
branch. §3 states the mechanism (in the paragraph on the
second control) but then says the controls make "the FORCED reading … a
measurement rather than a structural tautology". That is earned for
FORCED-vs-REFUSED — my no-supply control reproduces the refusal exactly, so
refusal is genuinely at risk — and not earned for BRANCHING, whose control
changes the *specification mode* rather than the schedule.
**Repair:** one sentence in §3: "BRANCHING cannot arise for a family schedule,
because every event is specified by its full tuple; the second control
establishes instrument sensitivity, not family-level reachability."

## 4. K1.3 — the stratified crystallinity: **CONFIRMED, and the mechanism is stronger than stated**

Exhaustive over the whole family via my own stabilizer machinery (7056 seed
pairs × 8100 multiplicity):

| class | seed pairs | schedules | crystalline | rate |
|---|---|---|---|---|
| CU-JOINT | 36 | 291 600 | 291 600 | 1 |
| CU-SPLIT | 108 | 874 800 | 0 | 0 |
| BEYOND-COSET | 6912 | 55 987 200 | 1 749 600 | 1/32 |

**The affine null's prediction verified exactly and elementwise**: for every
one of the 36 CU-JOINT pairs I confirmed `H ≤ Stab(n)` for the common `H` —
not merely that the stabilizer is nontrivial. Per-subgroup: 63 seed pairs each
(9 CU-JOINT + 54 beyond-coset), Stab = Z₃² never occurs, and 6 events over 9
sites is indeed the reason (3 ∤ 6/… — a period of order 3 forces every value's
level set to have size divisible by 3, and 6 = 3·2 cannot fill 9 sites
constantly).

**The exhaustiveness licence for this column is sound** and is *not* the
window: the initiator field is a function of the two seed sets alone, the
transversal weight is uniform at 90, and I recomputed both facts myself.

**THE PAIR-MECHANISM: confirmed at the four named witnesses and family-wide.**
At each of `[(0,0),(0,1),(1,0)]|[(0,2),(1,1),(1,2)]` → ⟨(0,1)⟩,
`…|[(1,1),(2,0),(2,1)]` → ⟨(1,0)⟩, `…|[(1,2),(2,1),(2,2)]` → ⟨(1,2)⟩ and
`[(0,0),(0,1),(1,1)]|[(0,2),(1,0),(1,2)]` → ⟨(0,1)⟩ the field's values on the
three `H`-cosets are `{0,1,1}` and neither seed is a line. Across the full
216-of-6912 census: **0 of 216** has a line seed, **0 of 216** fails the
`(1,1,0)` coset shape, and the subgroup split is exactly 54 + 54 + 54 + 54.
The count is also closed-form derivable and I derived it: 4 subgroups × 3
choices of the zero coset × 18 ordered splits of the remaining 6 sites that are
not the two cosets themselves = **216**.

**F6 (MINOR — the paper under-claims its own strongest measurement).** §6 says
"while neither seed set is an H-coset". Measured — and provable — is the
stronger "**neither seed set is a line at all**": an `H′`-coset with `H′≠H`
meets each `H`-coset once and so cannot sit inside the union of two of them.
The instrument's own evidence block records `S0_is_line: False,
S1_is_line: False`, so the paper is weaker than its receipt.
**Repair:** §6, "while neither seed set is a coset of any order-3 subgroup".

## 5. K1.4 — the determinant census: **CONFIRMED**

Rebuilt from HA 3.2's readout over all 78 400 partition pairs with exact
`Fraction`s:

- **747** pairs with det ≠ 0 at all nine sites; **544 563 = 747 × 729**
  schedules; **9** of them homogeneous.
- **ROW|ROW/DIAG**: `q = [[0,−1],[−1,2]]`, **det = −1 at 9 of 9 sites**, the
  same form at every site, homogeneous. Its record drives **FORCED** in my own
  driver, 24 events (round 1 repeats round 0's groups, so no conflict supply),
  6 division events, `maxhits = 1`, driven field = combinatorial field, and its
  diagonal seed set is a transversal of the ROW class. The 16-row class-pair
  table reproduces **row for row**, including every `−1/4` and every `1/2`, and
  I re-derived four of the rows by hand from the coset geometry before
  computing them.
- **Positive-definite sites: maximum 3 over all 78 400 pairs.**
- **I7-STRICT-EMPTY: 0** pairs make all 27 link counts strictly positive.
- Signature: **261** all-negative, **486** both signs, and I checked the third
  possibility the paper does not mention — **0** pairs are det > 0 at all nine
  sites — so "both signs" is exactly right. Cell census `{−1: 855, −1/4: 5238,
  1: 108, 3/4: 522}`, summing to 747 × 9 = 6723. And `det > 0 ⟺ positive
  definite` holds cell for cell with **0** exceptions in both directions, which
  is what licenses §5.3's "Where det > 0 the form is positive definite".
- The effectus anchor reproduces: committed ROW|COL gives
  `(n₁₀,n₀₁,n₁₁,q₁₁,q₂₂,|q₁₂|,det) = (1,1,0,1,1,1,0)`, and the kernel of
  `[[1,−1],[−1,1]]` is the diagonal as §5.1 says.

I also re-derived the two READ anchors with **my own driver rather than d66's
function object**: GRID(g=3,R=4) → (66, 12, 18) and GRID(g=3,R=6) →
(102, 18, 30), both exact.

## 6. K1.5 — the two claimed theorems

### THE BUDGET WALL — **it is a theorem.** One implicit step should be written down (F3).

The counting argument is sound and general at the committed cycle:

1. Each round's partition into three triples has exactly **9** within-group
   unordered pairs, so two rounds give at most **18**.
2. A within-group pair `{x,y}` contributes at most **one** link-incidence,
   because `L = {(1,0),(0,1),(1,1)}` contains exactly one of each `±` direction
   class, and pairs in the fourth direction `±(1,2)` contribute **nothing**.
   Hence total incidences ≤ 18, with multiplicity if a group repeats.
3. Positive definiteness at a site needs at least **3** incidences there.
4. Nine positive-definite sites therefore need ≥ **27** > 18. ∎

I verified every step against the census: the maximum total incidence over all
78 400 pairs is **exactly 18** (attained by 1296 pairs, so the bound is tight),
the minimum site-incidence at a positive-definite site is **exactly 3**, and
there are **0** positive-definite sites with fewer than 3 incidences. The same
budget gives I7-STRICT-EMPTY immediately and more directly: 27 strictly
positive counts need 27 incidences.

**F3 (MINOR — a gap in the written proof, not in the theorem).** Step 3 as
written derives "at least 3 incidences at that site" from
"`q₁₁ > 0`, `q₂₂ > 0` and `4q₁₁q₂₂ > (n₍₁,₁₎ − q₁₁ − q₂₂)²`". Those give
`n₍₁,₀₎ ≥ 1` and `n₍₀,₁₎ ≥ 1` but **not** `n₍₁,₁₎ ≥ 1`, which is the third
incidence. It is forced, but by a step the paper omits: if `n₍₁,₁₎ = 0` then
`q₁₂ = −(q₁₁+q₂₂)/2` and `det = −(q₁₁−q₂₂)²/4 ≤ 0`, so the site is not
positive definite.
**Repair:** insert that clause in §5.3 after the inequality. One sentence; the
theorem stands.

*Scope note, no repair needed:* the counting bound alone yields "at most 6
positive-definite sites" (18/3), not 3. The paper is careful — it presents the
**max-3** as the exhaustive census result and the counting fact only for
**never-9**. That division is exactly right and should survive editing.

### NEVER-RIEMANNIAN — **the theorem is true; the sentence that states it in the verdict is false as written** (F1)

The theorem "no schedule in the family is positive definite at every site" is
established by the budget wall above and confirmed exhaustively (max 3 of 9).
§5.3's own statement of it is correct and explicit, including the honest
qualifier "Where det > 0 the form is positive definite; that happens, but never
at more than 3 sites of one schedule".

**F1 (MAJOR — a false universal in the verdict section, contradicted by the
paper's own §5.3).** §10 says of the carrier:

> It is never positive definite anywhere in the family

Read literally this is **false**, and by a wide margin. I measured it:
**32 400 (pair, site) cells are positive definite, across 28 404 of the 78 400
partition pairs — 20 706 516 of the 57 153 600 schedules, 36.2 %, carry at
least one positive-definite site** (histogram over pairs: 49 996 with none,
24 660 with one, 3492 with two, 252 with three). Among the 747 non-degenerate
pairs alone there are 630 positive-definite cells (108 at det = 1, 522 at
det = 3/4). The intended reading — "never positive definite *everywhere*" — is
true and is what §5.3 says; the verdict paragraph drops the quantifier and
contradicts its own §5.3 two pages earlier. The verdict *string* token
`POSDEF-EMPTY` inherits the same compression; the gate text expands it
correctly ("AT EVERY SITE") but the paper's head does not.
**Repair, exact:** §10 → "It is **never positive definite at every site**,
anywhere in the family, for a reason that is a counting fact…". Optionally add
the true positive datum to §5.3, where it belongs and where the max-3 already
sits: positive-definite sites occur at 28 404 of the 78 400 pairs but never at
more than 3 of the 9.

## 7. K1.6 — fragility and constructibility

**Fragility: 12/12 at all 540, confirmed — and it is a family-wide theorem the
paper does not claim.** I reproduced the window census exactly: 540 crystalline
window schedules, 12 admissible single-arbitration re-seatings at every one
(6 arbitrations × 2 alternative seats), and at every one of the 6480 edits the
original period is destroyed. I also measured what the paper does not report:
**every edit leaves a *trivial* stabilizer**, not merely a different one — so
"break the stabilizer" and "destroy all periodicity" coincide here, and §7's
"The crystal is maximally fragile" is the right word.

Then I pushed it off the window. Over **all 252 crystalline seed pairs** and
**all 9072 single-element seed replacements** — a strict superset of the
admissible re-seatings for *any* partition, not just the window's — **0**
preserve the original period and **0** leave any nontrivial period. So the
fragility statement holds over the whole family as a combinatorial theorem,
with the paper's own one-line mechanism (`1_new − 1_old` is never constant on
the cosets of an order-3 subgroup) as its proof.

**F2 (MAJOR — a bolded scope claim that the paper's own §7 and §11.4
contradict).** §2.4 says, in bold:

> **Every other column below is exhaustive over the whole family.**

The pin declares **four** columns (R2.1 constructibility, R2.2 the stabilizer,
R2.3 the determinant, R2.4 fragility). Fragility is *not* exhaustive over the
family: §7 says "Measured on the 540 crystalline schedules of the window" and
Deviation 4 says "The fragility column is window-scoped". The sentence
immediately following the bold claim names only the stabilizer and the
determinant, which is the true reading — but the bolded sentence as written is
false, and it is the sentence a reader carries away from §2. §10's "every one
of those crystals dies to a single re-seating" inherits the over-reach: "those
crystals" are the 1 749 600 family-wide beyond-coset crystals, while the
measurement covered 540 window schedules (of which, I measured, 216 are
beyond-coset and 324 CU-JOINT).
**Repair, exact and cheap:** §2.4 → "**The stabilizer and determinant columns
below are exhaustive over the whole family**; constructibility and fragility
are window-scoped (§3, §7, §11.1, §11.4)." And in §10, either scope the
sentence to the window or — better, since it is true — add the family-wide
seed-replacement exhaustion, which costs the instrument 9072 stabilizer
evaluations it already has the machinery for.

**Constructibility: FORCED 11 664/11 664 confirmed by sample, and both
negative-fate controls reproduce exactly.**

- *No-supply control:* my own driver, deliveries suppressed, refuses at
  **`('propose G10', 13)` after 13 events** — the delivered pair, character for
  character.
- *Under-specified control:* replaying the committed record to prefix 3 and
  asking `candidates_for` for an arbitration by `G00` without the conflict and
  winner keys returns **7** candidates. I report only the count, for the same
  reason the paper does; §3's explanation of the `sorted(key=repr)` /
  per-process string-hashing non-reproducibility is correct and is the right
  call.
- The 24/30 dichotomy's *reason* is correct as stated: two distinct parallel
  classes share no group, so a round-1 group from a different class contains
  exactly one member of the seed's round-0 group and needs exactly 2
  deliveries; and 4 same-class pairs × 729 = 2916, 12 × 729 = 8748.

**All 20 census strata are non-empty and witnessed.** I built my own
representatives by my own enumeration (10 (stabilizer × affine) cells × det9
∈ {T,F}) and drove all 20: every one FORCED, `maxhits = 1`, 6 division events,
fields matching, lengths 24–29. I also independently recomputed the receipt's
`joint_det_stab` table — all **10** cells, e.g. `1|BEYOND-COSET: 516 798`,
`⟨(1,1)⟩|CU-JOINT: 558`, `⟨(1,2)⟩|CU-JOINT: 819` — summing to 544 563, with
the nontrivial-stabilizer part **19 791** and its beyond-coset part **17 118**.

**F7 (MINOR — a choice-inventory misclassification).** Item 10, "the group and
member processing order", is classed **forced**, fiber 1, on the ground that it
is "d66's own order at the committed schedule". d66's order pins the committed
*point*; extending it to the family as "ascending seed-site index, ascending
member index" is one of 6 × 6 extensions per round and is a *declared*
convention. I measured whether it matters: **360 order variants** (3 group
orders × 2 member orders × 60 random family-wide schedules) — **0** refusals,
**0** branchings, **0** changes to either field, **0** changes to the event
count. So the choice is inert and nothing downstream moves.
**Repair (either is fine):** reclassify item 10 as **declared**, fiber 36 per
round, with the invariance measured; or keep **forced** and cite the invariance
sweep as the forcing. As it stands the fiber-1 claim is asserted rather than
earned.

## 8. Prose audited against the receipt

I extracted every numeral in the paper — **71 distinct, 406 occurrences** — and
matched them against my own rebuild. Every census numeral is one I
independently reproduced. The residue is exactly the expected set: engraving
numbers (#24, #34, #62, #82, #87, #91, #119, #125, #126), the year, the three
commits, and the d66 anchor rows (66/12/18 and 102/18/30) which I re-derived
with my own driver. **No numeral in the paper is unsupported.**

All nine verbatim source quotations were checked against their sources after
apostrophe folding, blockquote-marker stripping and whitespace normalisation —
the adjudication's affine-mechanism clause, d66's g-PROPOSER sentence, the
pin's family clause, the pin's DET-NONZERO clause, HA 3.2's re-encoding
sentence, the catalog's BHS and Kleitman–Rothschild lines, L-1's fourth-form
clause, and the pin's diagonal licence. **All nine are present in both the
source and the paper, verbatim.**

**The walls hold.** No sprinkling, boost, rapidity or frame is *computed*
anywhere; the words occur in §8 only inside the paper's own negations, which is
what the wall requires. No dimension reading is taken. The only occurrence of
"cosmolog" is the bar itself. §8's L-1 argument is genuinely prior — it argues
admissibility, declines it, and locates the measured object (a permutation
action of Z₃² on the actor set) inside L-1's own scope guard. That is the right
argument and it is made before any test.

**Two prose readings I checked and cleared.** (i) §4.1's "the footprint reading
is a census artifact" is correct and correctly reasoned — each round's groups
partition the nine cells, so the field is identically 2 and its stabilizer is
identically Z₃², for the whole family and not merely the window; declining to
put it in the verdict string (Deviation 6) is the honest call. (ii) §5.2's
"the seeds move the initiators, not the footprints" is exactly true: the
footprint of an arbitration is its whole conflict group regardless of which
member seeds it, which is why the determinant column is counted on partition
pairs.

## 9. One observation handed to K3 (instrument), not adjudicated here

`G-SEAL-COMPLETE` prints "**every one of those 15 in-run seals still verifies**"
with evidence `{'seals': 15, 'declared_in_run': 16}`, while the run's terminal
line reports **19** sealed objects. `Seal.verify` iterates `self.rows` — the
seals actually *taken* — and filters by the `only` list, so a declared seal id
that was never taken is invisible to it and the gate passes anyway. Whether
the manifest is total is K3's row; the numbers and the mechanism are recorded
here because I met them while verifying the artifacts.

## 10. Findings, collected

| # | grade | where | what | repair |
|---|---|---|---|---|
| F1 | **MAJOR** | §10 | "never positive definite anywhere in the family" is false; 28 404 of 78 400 pairs (20 706 516 schedules) carry a positive-definite site, and §5.3 says so | insert "at every site"; optionally add the measured count to §5.3 |
| F2 | **MAJOR** | §2.4 | bolded "Every other column below is exhaustive over the whole family" is false for the fragility column, per §7 and §11.4; §10 inherits the over-reach | name the two exhaustive columns; scope §10 or add the family-wide seed-replacement exhaustion (which I ran: 9072 replacements, 0 survivors) |
| F3 | MINOR | §5.3 | the never-Riemannian proof omits the step forcing `n₍₁,₁₎ ≥ 1` | add "if `n₍₁,₁₎ = 0` then det = −(q₁₁−q₂₂)²/4 ≤ 0" |
| F4 | MINOR | §4.2, §2.4 | the driven=combinatorial equality is a theorem given a non-refused record, so it cannot be one of "two facts" licensing exhaustiveness; the licence is constructibility, which is the window-scoped thing | restate the licence as theorem + induction; my 250 out-of-window drives support the induction |
| F5 | MINOR | §3 | `BRANCHING 0` is a structural zero for family schedules, not a measurement; the control changes the specification mode, not the schedule | one sentence distinguishing instrument sensitivity from family reachability |
| F6 | MINOR | §6 | under-claim: measured is "neither seed is a line at all", not merely "not an H-coset" | strengthen the sentence to match the receipt |
| F7 | MINOR | §9 item 10 | processing order classed forced/fiber-1 on a committed-point precedent; it is a declared extension | reclassify, or cite the invariance (360 variants, nothing moves) |

**Nothing above moves a number.** The three verdict strings stand as delivered:
`U4B-CRYSTAL-GENERIC-[beyond-coset 1/32; 1749600 of 55987200;
⟨(0,1)⟩|⟨(1,0)⟩|⟨(1,1)⟩|⟨(1,2)⟩]`,
`DET-NONZERO-EXISTS-[ROW|ROW/DIAG: det=−1 at 9 of 9; 747 of 78400 pairs;
POSDEF-EMPTY; I7-STRICT-EMPTY]`, and
`CONSTRUCTIBILITY-[FORCED 11664 of 11664; BRANCHING 0; REFUSED 0]@WINDOW-11664-OF-57153600+20-STRATUM-WITNESSES`.

## 11. What I judge, in one paragraph

The census is right. Both claimed theorems **are theorems** — the budget wall
is airtight modulo one omitted line, and never-Riemannian follows from it — and
the pair-mechanism, which is the unit's real finding, is not only confirmed at
the named witnesses but **derivable in closed form** (4 × 3 × 18 = 216) and
**stronger than the paper says** (neither seed is a line at all, not merely not
an `H`-coset). The affine null does exactly what a null should: it predicts 36
of 36 and it fails to exhaust, and the failure is a property of the *pair* of
seed sets, which no single-seed affine reading can produce. The determinant
segment's witness survives every check I could put on it. What needs fixing is
scope language, twice, in the two places a reader is most likely to quote: a
verdict sentence that drops a quantifier and a bolded §2.4 sentence that
promises exhaustiveness for a column the paper itself scopes to the window.
Both repairs are one sentence each and neither costs a number. **AWF.**

---

*Rebuild artifacts (scratch only, not committed):
`op_comb.py` (108 gated comparisons), `op_drive.py` (25 gated, 232 driven
records), `op_stress.py` (20 gated, 252 driven records), `op_order.py` (420
driven records over 6 processing orders), `posdef.py` and `op_sign.py` (12
auxiliary quantities), and the byte-identical plain run under
`…/scratchpad/u4b-op/repo/`.*
