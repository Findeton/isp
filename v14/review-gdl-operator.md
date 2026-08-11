# K1 — OPERATOR-LENS HOSTILE REVIEW of paper-25 (GDL)

**Seat:** K1 OPERATOR, ledger v14 #222.  **Object at commit `4c85ca4`**, hashes
verified at the start and re-verified at the end of this review, byte-identical
both times: paper `e98003841378`, code `81595d600575`, output `39128fafc7bf`,
receipt `b87016e96285`; pin `fe9533371046`.  Parent read at `1196ad6`: paper-20
`4824d190af73`, code `72e7b299f66e`, receipt `55273f6b6068`.

**Method.** Everything below was rebuilt from nothing at
`/private/tmp/.../scratchpad/gdl-op/` with the reviewer's own machinery.  No
module of `gdl_exact.py` is imported, no subprocess of it is run, and no
intermediate of it is read.  The ring representation is deliberately different:
elements of Z[ω] are carried as coefficient triples in the group ring
Z[x]/(x³−1) (basis 1, x, x² with x = ω) and reduced to a canonical Z[ω] pair
`(c₀−c₂, c₁−c₂)` only where an equality or a norm is needed.  ρ is summed over
unordered site-pairs and doubled rather than over ordered pairs.  ε(x) is
computed as Σ_l p(x)·k₁(l|x) through the kernel rather than assigned.  The
failure census is taken twice, the second time by a sort-based pass sharing no
dictionary with the first.  Arithmetic is exact throughout;
`/opt/homebrew/bin/python3.13`.

---

## GRADE: **ACCEPT-WITH-FIXES (AWF)**

**348 independent recomputations of delivered published values and table cells,
zero mismatches.  No false number was found anywhere in the unit.**  The
numeral sweep over the paper's 106 distinct numerals leaves nothing unaccounted
except three structural references (`#205`, `#91`, `2026`).  The verdict
`GDL-PARTIAL` with `GRAVITATIONAL-CELLS=0` is confirmed by independent
measurement, and the frozen exclusion is correctly applied.

Three MAJOR findings, all of them about **what the paper says about its own
numbers** rather than about the numbers.  None moves the verdict.  All three
have one-clause repairs.

---

## 1. THE RECOMPUTATION LEDGER

| block | recomputations | mismatches |
|---|---|---|
| A. the 14-value parent anchor (equality) | 14 | 0 |
| A. the 14-value anchor (verbatim location in `55273f6b6068`) | 14 | 0 |
| A. machine counters: det values, 296,784, 1,479,176 + its 3-way split | 6 | 0 |
| B. object counts and the two collapses | 5 | 0 |
| B. the 45-cell grid, COUPLED arm | 45 | 0 |
| B. the 45-cell grid, FROZEN arm | 45 | 0 |
| B. the second, independent failure census (all 90 cells) | 90 | 0 |
| B. RES-SITE pool, identities (coupled + frozen), ℓ₁ price, co-occupancy ladders | 30 | 0 |
| C. the blindness census: 5×3 table, totals, field admissibility, 6 coins' unitarity + S₃-covariance | 37 | 0 |
| D. fiber rows, separation ladder per-step, §8 value lists, dominations + exact witnesses, n-growth profile | 62 | 0 |
| **total** | **348** | **0** |

Additional work not counted as recomputation: a symbolic verification of the
cancellation algebra over **4,374** coefficient identities; **1,971,720**
per-site-pair mechanism checks (new); **305** explicit 9×9 Tr(ρ²) matrix
squarings (new); **4** mutants outside the harness; a 106-numeral sweep.

## 2. WHAT REPRODUCES (the decisive list)

**The arena and the anchor.**  All 14 parent values come back out of an
independent implementation at equality, and all 14 are located verbatim in the
committed parent receipt bytes: branches per level `[3,27,486,10527,284078]`,
`[3,27,486,9234,212382]`, `[3,27,486,11664,314928]`; IPRs
`35971074413334039128803/239299329230617529590083` and `2306155/14348907`;
exits `927415552/847288609443`, `37440224/5811307335`, `0`; the link-class
marginal, both site distributions, the max-cell ladder `[2,2,3,3,4]`, and
`11044` / `9751`.  Determinants reached: `0, 1, 2, 3, 3/4, 7/4`.  Site-branch
steps `296,784` and law checks `1,479,176` both reproduce, the latter
decomposing exactly as `296,784 + 295,598 + 886,794` (see MAJOR-3).

**The collapses.**  Coupled `11,044 → 10,954` (all 90 duplicates at level 5:
distinct per level `1, 3, 27, 486, 10437` against raw `1, 3, 27, 486, 10527`).
Frozen `9,751 → 5`, one per level.  The frozen collapse is not merely measured,
it is **structurally forced** and the paper's reading of it is exactly right:
on the frozen arm ψ_{t+1} = shift(C(ψ_t, WELDED)) is deterministic and n never
moves, so a level carries exactly one (ψ, n).

**The 45-cell grid, both arms.**  COUPLED `2 EXACT / 28 PARTIAL / 15 VACUOUS`.
FROZEN `1 EXACT / 38 PARTIAL / 6 VACUOUS`.  Every RES-BRANCH number in §5's
table reproduces: `3740` of `4080`, `4074`, `4041`; `104` of `120`, `116`,
`117`; `24` of `31`, `25`, `31`; `2` of `4`, `2`, `3`; EXACT at `130`
non-singleton classes, `128`, `129`.  RES-SITE pool `55,140` with the same
single exact cell (`63` non-singleton).  RES-STEP `15` of `15` VACUOUS.  The
coarsening census `7498, 10599, 10905, 10923` for D1 and `8166`, `8100` at the
cell grain reproduce exactly, and the monotonicity the paper argues from is
real.  **My independent second failure census agrees with the first on all 90
cells** (failing classes, objects in them, and distinct D-values in them).

**The identities.**  `ID-RATE-IS-BORN` 98,586 coupled / 45 frozen checks;
`ID-RATE-TOTAL`, `ID-D1-IS-SQUARED-RATE`, `ID-PURITY-SPLIT` at 10,954 coupled
and 5 frozen; 0 violations everywhere, at 10,959 objects of both arms.  I
verified `D1 + D2 = Tr(ρ²)` is **real algebra and not bookkeeping** by forming
ρ as an explicit 9×9 matrix and squaring it, on 305 objects, 0 mismatches.

**The ℓ₁ pricing.**  `388,024` entries, `109,706` perfect squares, `278,318`
irrational, `547` distinct values.

**The separation ladder and the fiber.**  I rebuilt **five** of the seven fiber
members — GROVER, −GROVER, `w/3`, `(-2-w)/3` (two hidden coins) and the record
menu — each to full horizon on both arms, and recomputed the signature with my
own grid and my own digest.  Object counts `10954, 10954, 11935, 9043, 11941`
match the published table; every member returns ladder `{D1: 4, D2: 4, D3: 3}`;
**every member returns `da4248b1a55b`.**  All six coins verified exactly unitary
(MM* = 9I entry by entry) and exactly S₃-covariant against all six permutation
matrices.

**The dominations and their exact witnesses.**  D1 COUPLED-DOMINATES on [4,5]
with `3822155/14348907` vs `40411/177147` and `51476944417/282429536481` vs
`81857/531441`.  D2 NO-DOMINATION: rises at 4 (`2176942528/10460353203` vs
`33920/177147`) and **falls** at 5 (`5743648327744/22876792454961` vs
`184192/531441`).  D3 NO-DOMINATION on [3,4,5], rising at 3 and 4 and falling
at 5.  §8's value lists reproduce: D1 `1, 11/27, 619/2187`; D2 `0, 0, 128/729`;
D3 at step 3 takes `266/729, 289/729, 296/729` against the control's `266/729`.

**The co-occupancy threshold.**  Coupled `(1,0) (3,0) (27,0) (486,486)
(10437,10437)`; frozen one object per level with the first co-occupancy at
step 4.  **Threshold 4 on both arms**, confirmed.

## 3. THE BLINDNESS MECHANISM — verified as algebra, then strengthened

**The algebra.**  With M = 3C the coin numerator (MM* = 9I) and
post(x,l) = Σ_j M[l][j] ω^{n_j(x)} ψ(x,j), I verified **symbolically** — ψ
carried as formal monomials ψ(x,j)·conj(ψ(y,k)), counts ranging over all 729
residue pairs, coefficient by coefficient in Z[ω] — that

> ρ_xy = 9 · Σ_j ω^{n_j(x) − n_j(y)} ψ(x,j) conj(ψ(y,j))

holds with **0 coefficient mismatches for every one of the six fiber coins**
(4,374 identities).  The factor 9 is the numerator normalisation; in the
paper's normalised C it is 1, and the paper's displayed formula is correct.
The diagonal corollary follows in the same computation: at x = y every phase
difference vanishes and ρ_xx = 9 Σ_j |ψ(x,j)|², independent of n.

**The census.**  My foreign-field census reproduces the delivered table cell
for cell — `STALE 0 / 10,911 / 10,953`, `ALL-TWO 0 / 10,922 / 10,929`,
`INADMISSIBLE-ONE-CELL 0 / 10,922 / 10,929`, `LADDERED 0 / 10,922 / 10,954`,
`ZERO-AT-ONE-CELL 0 / 10,916 / 10,935` — totalling **D1 0, D2 54,593, D3
54,700** over 164,310 checks, with D2 moving at **not one** of the 155
object-field pairs whose object carries no co-occupying site-pair.  D2's 177
non-moves are 155 no-co-occupancy plus 22 others, so **co-occupancy is
necessary and not sufficient**, exactly as the paper scopes it.

**NEW — the mechanism at the grain its own algebra predicts.**  The delivered
census measures movement per OBJECT (an object counts as blind only when none
of its 36 site-pairs co-occupies).  The algebra predicts something finer: for
**every** site-pair meeting in at most one occupied link, |ρ_xy|² is
record-independent whatever the rest of the object does.  Measured over
10,954 objects × 5 fields × 36 site-pairs = **1,971,720 pair-checks**:

| class | checks | |ρ_xy|² moved |
|---|---|---|
| pairs meeting in ≤ 1 occupied link | **452,745** | **0** |
| pairs meeting in ≥ 2 occupied links | 1,518,975 | 840,889 (678,086 static) |

The mechanism holds at the finest grain, at 36× the delivered evidence.  This
is offered as a strengthening, not a correction.

**NEW — the growth functional is record-blind too.**  I ran the same foreign
fields against `G5-RATE-SITE`: **ε moves 0 times over all 5 fields and all
10,954 objects.**  Under both readings ε(x) = p(x) is the post-coin site mass,
so §7's diagonal theorem applies to G5 verbatim.  **The single EXACT cell of
the entire 45-cell table therefore relates a record-blind decoherence
functional to a record-blind growth functional.**  That is the sharpest
available statement of why it survives the frozen arm, and §6 currently reaches
it only obliquely ("a statement about the emission law's normaliser").  See
MINOR-4.

## 4. FINDINGS

### MAJOR-1 — §7's closing generalisation is contradicted by §7's own table

§7 concludes: "**a decoherence functional built from the state at a single
time, in a basis the coin acts on site-locally, is blind to the record it is
supposed to be a function of**" and "the two ψ-internal *values* are blind
too."  `D2-OFFDIAG-SITE-MASS` is exactly such a functional — built from the
state at one time, in the site basis, with the coin acting site-locally — and
it is **not** blind: it moves at 54,593 of 54,770 object-and-field pairs, per
the table four paragraphs above.  §8 then opens by conceding the point ("The
ψ-internal functionals are not blind forever").  The universal as written is
false, and it is the sentence the paper itself flags as its deepest and most
falsifiable claim.

**Repair (exact, liftable).**  Replace the bolded universal with the scoped
statement the unit actually measured:

> **the DIAGONAL of a decoherence functional built from the state at a single
> time, in a basis the coin preserves each site's mass in, is blind to the
> record it is supposed to be a function of; its OFF-DIAGONAL is blind exactly
> on the site-pairs whose occupied-link sets meet in at most one link.**

and replace "the two ψ-internal *values* are blind too" with "the ψ-internal
value built from the diagonal is blind outright at 0 of 54,770; the one built
from the off-diagonal is blind exactly off the co-occupancy support, and moves
at 54,593 of 54,770."

### MAJOR-2 — a 3× inflated denominator on the headline blindness claim

§7: "**the inverse participation does not move once in 164,310 checks over 5
declared foreign count fields**."  164,310 is the total over **three**
functionals (3 × 5 × 10,954).  D1's own denominator is **54,770**.  The verdict
block states this correctly ("MEASURED ... AT 164,310 CHECKS: D1 MOVES 0
TIMES"); §7's prose does not.  Under the era's honest-denominator discipline
(#34) a blindness claim must carry the denominator of the thing that could have
moved.

**Repair.**  "…does not move once in the **54,770** object-and-field pairs at
which it is checked, of 164,310 checks over the three functionals and 5
declared foreign count fields."

### MAJOR-3 — the 1,479,176 law-native checks are unfalsifiable as coded, and the parent's own stamp was dropped

Verdict block and §2: "law-native at `1,479,176` kernel checks with `0`
violations."  I reproduced the number and its composition exactly:

| class | checks | predicate as coded | can it fail? |
|---|---|---|---|
| `law_native` | 296,784 | `G1 != M` where both are `sum(qrow)` | no |
| `kernel` | 295,598 | `sum(q/M) != 1` | no |
| `kernel_entry` | 886,794 | `q != (q/M)·M` | no |
| **total** | **1,479,176** | | **none** |

paper-20 published the analogous composite and explicitly warned its reader:
"the `column` class is Σ_l q/M = 1, an identity in the definition of the kernel
that cannot fail for any coin, menu or record … a reader should not take all
948,297 checks as rows that could have failed."  paper-25 carries the composite
into its **verdict block** with no such stamp, and the receipt's
`machine.law_checks` carries no `kind` field either.  This is a disclosure
regression from the parent, on a headline number.

Note the companion number is fine and I verified it is contentful: the
`296,784` site-branch-step unitarity row is site-mass preservation, and MUT-1b
below breaks it.

**Repair.**  Stamp the class as the parent did — in §2, "law-native at
`1,479,176` kernel checks with `0` violations, **every one of them an identity
in the definition of the kernel and none of them a row that could have
failed**" — and add `"kind": "DEFINITIONAL"` to `machine.law_checks`.  The
contentful sibling (`296,784`) should keep its unqualified reading.

### MINOR-1 — "45 cells per arm … 2 exact, 28 partial, 15 vacuous" is the coupled arm's tally only

The frozen arm's 45 cells tally **1 EXACT / 38 PARTIAL / 6 VACUOUS**, and the
receipt publishes that grid honestly (`relation.grid_frozen`).  §5's sentence
reads as a per-arm tally and the verdict block repeats the construction.  Same
for "The `RES-STEP` column is `15` of `15` VACUOUS" — on the frozen arm
RES-STEP is 12 PARTIAL / 3 VACUOUS.

**Repair.**  "45 cells per arm … **on the delivered arm**: 2 exact, 28 partial,
15 vacuous; on the control, 1, 38 and 6."

### MINOR-2 — `ID-RATE-IS-BORN`'s 98,586 checks cannot fail as instrumented

§4: "Two rows are measured about the rate itself, and both are properties of
the law-native normaliser rather than of this unit's arithmetic."  In
`emission_weights` the code sets `eps[s] = px` by assignment, so the
`eps(x) == p(x)` row compares a value with itself.  The *mathematical* content
is real — I recomputed ε as Σ_l p(x)·k₁(l|x) **through the kernel** and it
holds at all 98,586 site-checks with 0 violations — but the delivered
instrument does not test it, which is the opposite of what §4 says about it.
The DEFINITIONAL-THROUGH-THE-LAW stamp in the receipt is correct and mitigates.

**Repair (strengthening).**  Compute `eps[s] = sum(px * k[i] for i in range(3))`
instead of `eps[s] = px`.  The row then genuinely tests Σ_l k₁ = 1 at the site
grain and the §4 sentence becomes true as written.  Verified: the value is
unchanged and 0 violations, so nothing published moves.

### MINOR-3 — the cancellation premise is stronger than the diagonal leg needs

§7 and `mechanism.statement`: "the coin is unitary and **the same at every
site**, so it CANCELS out of the site-basis density matrix."  Site-uniformity
is required for the **off-diagonal** formula only.  Measured, by two mutants
that isolate the legs (§5 below): with a per-site-**different** unitary coin the
diagonal stays record-blind (D1 moves 0), while the off-diagonal cancellation
fails at **729 of 729** count-pairs symbolically.  §13 item 2 already states the
correct attribution ("the coin preserving each site's mass"); §7 and the
receipt statement do not.

**Repair.**  "Because the coin is unitary and site-block-diagonal it cancels out
of the **diagonal** of the site-basis density matrix; because it is in addition
**the same at every site**, the off-diagonal reduces to ρ_xy = Σ_l ω^{Δn_l} ψψ*."
This makes the theorem stronger, not weaker.

### MINOR-4 — the frozen exclusion has a sharper ground than the one given

§6 excludes the exact cells because they hold on a stage whose record never
grows.  The sharper and fully measured reason (§3 above): **G5 is itself
record-blind** — 0 moves over 5 foreign fields and 10,954 objects — so the cell
is a relation between two ψ-functionals and could not have distinguished the
arms whatever the record did.  Worth one sentence; it converts the exclusion
from an empirical observation into a consequence of §7's own theorem.

### MINOR-5 — the ℓ₁ price silently drops the rational entries

"278,318 of 388,024 off-diagonal moduli are irrational."  388,024 counts only
the **nonzero** |ρ_xy|²; the full off-diagonal population over unordered
site-pairs is 10,954 × 36 = **394,344**, the missing 6,320 being zeros, which
are rational.  The honest fraction is 278,318/394,344 (70.6%) rather than
278,318/388,024 (71.7%).  The qualitative claim is unaffected.

### MINOR-6 — the verbatim-location leg is near-vacuous on two anchor rows

All 14 rows locate, but the locator tokenises and accepts any occurrence in the
receipt bytes.  For "frozen admissibility-exit probability" (`0`) and "maximum
cell count on the ladder" (`[2,2,3,3,4]`) every token is a single digit and the
test is satisfied by essentially any JSON.  The other 12 rows carry
discriminating tokens (up to 23 digits) and are strong.

**Repair.**  Require at least one token of length ≥ 4 per row, or locate the
row's rendered list form rather than its tokens.

## 5. MUTANTS OUTSIDE THE HARNESS

All four run in my rebuild, never in the delivered file.

| mutant | construction | result |
|---|---|---|
| **MUT-1a** | delivered coin composed with a cyclic permutation of the 9 sites (unitary, not site-block-diagonal) | D1 moves **0** — a permutation preserves the mass multiset, so this mutant does **not** reach the gate.  Disclosed as a failed mutant. |
| **MUT-1b** | Grover applied **across** the site index inside each site-triple, per link channel (exactly unitary, genuinely moves mass between sites) | site mass no longer preserved at 2,400 of 2,400; **D1 moves 2,259 of 2,400.**  The delivered `D1 = 0 of 54,770` is therefore **contentful**, and §13 item 2's diagnosis is confirmed exactly. |
| **MUT-2** | a per-site-**different** unitary S₃-covariant coin (block-diagonal, not uniform) | **D1 moves 0** (diagonal leg survives site-variation); symbolically the off-diagonal cancellation fails at **729 of 729** count-pairs, against **0 of 729** with a uniform coin.  Isolates the two legs — the ground for MINOR-3. |
| **MUT-3** | drop the (t, ψ, n) deduplication | 11,044 objects instead of 10,954; the G1×D1 failing-object count is unchanged at 7,498 (all 90 duplicates fall in non-failing classes).  The dedup is load-bearing for the frozen headline `9,751 → 5`, not for the grid numbers. |

## 6. NUMERAL SWEEP

106 distinct numerals in the paper.  Every one is reproduced by this review's
own value set except `205` (ledger reference), `91` (engraving reference) and
`2026` (a year).  All 12 sha256-12 tokens in the paper resolve to the objects
they name.  Every small numeral was additionally adjudicated in context.  **No
false number.**

## 7. WHAT I COULD NOT FAULT

- The exclusion gate is **reachable**: had any G1–G4 cell been EXACT on the
  coupled arm it would have failed on the frozen control (where G1–G4 form one
  class carrying five D-values) and survived as gravitational.  The negative is
  measured, not designed.
- The RES-BRANCH exact cell's frozen counterpart is VACUOUS, so its exclusion
  rests on the identity rather than on the cell's own frozen word.  The receipt
  discloses this in `exclusion.excluded[0]` (`frozen_verdict: VACUOUS`,
  `identity_holds_frozen: true`) and §6 says so in prose.  Correct and honest.
- `D2` is exactly the squared Hilbert–Schmidt distance from the site-dephased
  state, as claimed.  `D3` is exactly ℓ₁ (half the ℓ₁ of the kernel difference,
  i.e. total variation), as claimed.
- The G-COIN-FIBER gate binds the cell digest **and** the separation ladder
  **and** the identities, so §9's "entire relation signature" is honest even
  though the digest column alone covers only the 15 cells.
- ±Grover are a genuine global-phase pair (−GN vs GN) and every published row
  is measured identical between them rather than assumed.
- No SI quantity, no rate in a physical unit, no experimental value, and no
  continuum or cosmological reading appears anywhere in the paper text.

## 8. VERDICT

The GDL unit's arithmetic is sound and its headline is earned.  `GDL-PARTIAL`,
`GRAVITATIONAL-CELLS=0`, the frozen exclusion, the co-occupancy threshold at
step 4 on both arms, the separation ladder D3@3 / D1@4 / D2@4 forced across the
whole executed fiber, and the record-blindness of the inherited observable are
all confirmed by an independent rebuild.  The three MAJOR findings are
descriptive: a false generalisation in the deepest paragraph, one inflated
denominator, and one dropped disclosure the parent had made.  Fix those three
clauses and the unit is terminal-grade.

**A/AWF/R → AWF.**  348 recomputations, 0 mismatches, 3 MAJOR, 6 MINOR.

Object hashes re-verified at close of review, unchanged: `e98003841378` /
`81595d600575` / `39128fafc7bf` / `b87016e96285`; pin `fe9533371046`; parent
`4824d190af73` / `72e7b299f66e` / `55273f6b6068`.
