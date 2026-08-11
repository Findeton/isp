# PER-L (paper-28) — EFFECTUS REVIEW (K2)

**Seat:** EFFECTUS-LENS (the head's licensure, the readings, the scope, the
register).  **Protocol:** v14 ledger #218, row K2 (launched at #220).
**Object at 9fcc081, hashes verified at open and at close:**
`v14/paper-28-perl.md` `bd0298e2a482` · `v14/code/perl_exact.py`
`976d5b9e4ac8` · `v14/code/perl_output.txt` `e4ff37a7a13e` ·
`v14/code/perl_receipt.json` `54ec5a9e9b72` · pin `v14/note-perl-pin.md`
`973b160d52ed`.  All five identical at HEAD (37523c6) and at 9fcc081; no
sibling working state read.
**Binding context read:** the paper-20 adjudication at 159200e
(§SUCCESSOR REGISTER), paper-20 itself (§S-6), `review-coup-effectus.md`
§6 (S-EF-1, the register's source), R4 at 583cae7 (§2, §3, §11, §12),
R4b at 6d32993 (§4, §6, §9), R5 at 987cd73 (§7), R2's criterion as ported,
`v14/PLAN.md` (the structural-prediction ledger, entry (g)),
`v14/note-paper12-scope-annotation.md` (the #142 precedent).

---

## GRADE: ACCEPT WITH FIXES (AWF)

**~300 independent recomputations; ZERO delivered numbers moved.**  I rebuilt
the arithmetic from scratch — my own Q(ζ₂₄) over `fractions.Fraction`, reduced
mod Φ₂₄ = x⁸ − x⁴ + 1, my own alphabets, my own autocorrelation scan, sharing
no line with `perl_exact.py` — and every number in the paper that my route can
reach came back exact.  The eighteen-arena table (90 cells), the control table
(18 cells), the locality table (45 cells), the band table and its six
witnesses, the map total 1,952,424, the axis-and-lag total 2,940, the pool
identities 58/42/106, the cell counts 928/1512/6784: all exact.

**Every finding below is a reading, an attribution or a scope stamp.  Not one
is a computed number.**  The programme's constant holds for the seventeenth
time: the failures live one level up from the numbers.

The five fixes that make this terminal are M1–M5.  M1 is the one the unit
itself pointed the panel at, and the attack it invited does not land where it
expected — the band's *absence* half above width 1 is honestly declared open;
what fails is the band's **evenness** clause, and I have the witness.

---

## 1. THE RECOMPUTATION LEDGER

| what | rebuilt | result |
|---|---|---|
| Q(ζ₂₄), the three alphabets, unit-modulus counts (8/6/6) | own field, own build | exact |
| the 18-arena table: Sidon, DDS-free, multiplicities, unitary, non-monomial | 90 cells | 90/90 exact |
| the control table at L = 3, three probe alphabets | 18 cells | 18/18 exact |
| the 54 and its witness support | own scan | `{(1,0),(1,1),(1,2)}`, a coset of an order-3 subgroup — identical to `review-coup-effectus.md` S-EF-1 |
| the control multiplicities | own count | `[3,3,1,1,1,1,1,1]` = S-EF-1's `[1,1,1,1,1,1,3,3]` |
| 78 = 54 + 4·6 and paper-20's 72 = 54 + 3·6 | own arithmetic | the two unitary totals differ only by the monomials on the extra offset |
| maps scanned, 1,952,424 | 3·(15625 + 4·15625 + 390625) + (15625+343+6859+390625+2401+130321) | exact |
| axis-and-lag objects, 2,940 | 9·16 + 19·36 + 33·64 | exact |
| the locality table, 9 rows × (neighbours, offsets, complete, locality, b₁) | own graph, b₁ = E − V + 1 | 45/45 exact |
| interior radii, diameters, VMAX, eigenphase lattices | own | 1,2,3 / 2,3,4 / 2,3,4 / 8,24,8 exact |
| the speed-3/2 witness | analytic, from the definition | order-2 axis, Δs = ±6 in Z/24, v = −Δs/4 = ∓3/2 — exact, and it is not a tie |
| pool totals 58/42/106 | Σ per-axis gauge classes − (axes − 1) = 66−8, 60−18, 138−32 | exact, all three |
| the 3-term stencil's DDS-freeness by order | orders 2…12 | fails exactly at 2, 3, 4 — exact |
| the width-1 DDS census, sizes 2…14 | exhaustive over all subsets of the 9-offset ball | DDS-free at every L ≥ 5 — exact |
| the band identity, r = 1,2,3 | {L : locality ∧ involution pair} vs even L in [2r+2,4r] | equal at all three widths |
| the six band witnesses | whole-torus criterion, all L² lags | 0 violations each |
| coset-in-ball search, 3 widths × 13 sizes | own | 39 cells; **one disagreement with the band — see M1** |
| the L = 9 / r = 3 counterexample | 81-lag whole-torus check + 3 alphabet scans | unitary, non-monomial, radius exactly 3 |

**Nothing moved.**  The instrument's arithmetic is, as far as this seat can
reach, without fault.

---

## 2. MAJOR FINDINGS

### M1 — THE HEAD'S SCALE SEGMENT SAYS "ARE"; THE UNIT MEASURED A SUFFICIENT CONSTRUCTION.  MEASURED COUNTEREXAMPLE: L = 9 AT WIDTH 3.

The head asserts

> `ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-EVEN-L-IN-[2r+2,4r]`

and the §7 table heads its column **"admitted sizes"**.  But `admitted` in the
instrument is `locality_at_width(L,r)["locality"] and band_witness(L,r) is not
None`, and `band_witness` returns **one construction**: a pair of ball offsets
differing by an involution, carrying 1/√2 and i/√2.  What the run proves is
therefore the combinatorial identity

> {L : locality at width r} ∩ {L : the radius-r ball contains an involution
> pair} = {even L : 2r+2 ≤ L ≤ 4r},

which I verified at all three widths and which is genuinely true and pretty.
It is *not* the statement that those are the sizes carrying a local
non-monomial unitary — which is what "admitted" means in the parent whose
headline this row reframes.

The two differ, inside the swept range, at one cell.  **At L = 9, width 3:**
locality holds (2r+1 = 7 < 9); the radius-3 ball contains the full coset
`{(8,0),(8,3),(8,6)}` of the order-3 subgroup ⟨(0,3)⟩, which is
difference-doubled with multiplicities [3,3]; and the coefficient map
c = (1/3, −2/3, −2/3) on it is **unitary by the parent's own whole-torus
criterion — 0 violations over all 81 lags** — non-monomial, of max-norm
support radius exactly 3.  Over the THIRDS-19 probe alphabet that same coset
carries **54 non-monomial unitaries**: the unit's own control number, at a
rung of the *L*-ladder, three widths up.

So the odd-L exclusion in the band is **alphabet-relative, not structural** —
0 over the parents' 25 and over UNIT-7, 54 over THIRDS-19.  It is R4's order-3
gap recurring one window up, and this unit is the one that taught the corpus
to read that gap correctly (§3.3).  It did not apply its own lesson to its own
band.

This also puts the §9 sentence "Nothing about odd rungs" in tension with the
band, whose sweep runs over sizes 2…14 and whose law *asserts* evenness.  The
band is the unit's only odd-L claim.

**Exact repairs.**

1. Head, SCALE segment:
   `ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-EVEN-L-IN-[2r+2,4r]` →
   `INVOLUTION-PAIR-SIZES-AT-WIDTH-r-ARE-EXACTLY-THE-EVEN-L-IN-[2r+2,4r]`,
   and append
   `ODD-L-EXCLUSION-ALPHABET-RELATIVE(L-9-AT-r-3-CARRIES-A-COSET-WITNESS-OVER-Q;0-OVER-THE-PARENTS-25;54-OVER-THIRDS-19)`.
2. §7 table column "admitted sizes" → **"sizes with an involution-pair
   witness"**; add a fourth row to the table or a sentence after it recording
   L = 9 at r = 3.
3. §7 "**The honest half**" paragraph: the honest half is larger than stated.
   The *absence* direction is forced not only at width 1 but at every
   (L, r) with L ≤ 2r+1 (locality fails by a theorem); what is open above
   width 1 is only the DDS census over balls of 25 and 49 offsets.  Say that,
   and add: "and the presence direction is *narrower* than the ball — a
   second mechanism, the full coset, admits sizes the involution pair does
   not, at least one of them odd."
4. §9's "**The one reading that most wants a second look**" should record that
   the attack it invited (a size outside the band at width 2) is not where the
   row breaks; the row breaks at the evenness clause at width 3.
5. Persistence-table row "the window widths at which this size is admitted"
   → "…at which this size carries an involution-pair witness".  Its cells
   `[1] / [2] / [2,3]` are unchanged and — worth saying — every *exclusion* in
   that row is forced (locality failures at L=4,r≥2 and L=6,r=3; the width-1
   DDS census at L=6,8,r=1).  That row is the strongest one in the table and
   the paper does not say so.

### M2 — THE PARENT ALREADY PROVED A FIELD-FREE BALL COLLAPSE.  IT IS NEITHER CITED NOR DISTINGUISHED, AND IT IS THE DDS THEOREM'S FOURTH INSTANCE.

R4 (583cae7) §3 carries, in its own words:

> **Theorem (Moore-ball collapse).** *Let L ≥ 5 and let U be a unitary
> generator on (Z_L)² whose coefficient map is supported inside the radius-one
> Chebyshev ball {−1,0,1}². Then U is monomial. Over any field closed under
> conjugation.*

and its **Consequence**: "No local stencil whatever — three-term, five-point,
nine-point, or any subset of the radius-one ball — admits a non-monomial
unitary at any L ≥ 5, over any field."

PER-L's width-1 census is exactly that statement, re-proved by counting; my
own exhaustive subset census over the nine-offset ball at L = 2…14 returns
DDS-free at every L ≥ 5, confirming both.  Two consequences the paper misses:

- **The DDS theorem subsumes four prior results, not three.**  The Moore-ball
  collapse is the fourth and the most substantial: R4's proof runs through the
  aperiodic cross-correlation and an integral-domain argument; the DDS
  criterion gets it in two lines from a subset census.  That is a real
  strengthening and the paper gives itself no credit for it.
- **§7's "reproducing the parent's anchored admissible-scale set from a
  completely different argument" under-describes what happened.**  It is a
  second proof of the parent's *own* field-free ball theorem, not an
  independent route to a scan result.  The novelty at width 1 is the proof,
  not the fact.

There is a third, sharper point.  R4's §12 false-claim register already
recorded a relativity of exactly this shape:

> **the unique scale is a theorem about the declared link set of the record
> stage, not a law of the substrate**

— connective-relativity, registered by the parent itself.  PER-L's §7 presents
window-relativity as a discovery about a parent that thought its size was
absolute.  The parent did not think that.  What PER-L adds is a *second axis*
of the same relativity, and that is how it should read.

**Exact repairs.**  §3.1, after the DDS theorem: one sentence citing R4's
Moore-ball collapse and its Consequence, and naming it the fourth instance.
§7 first paragraph: replace "from a completely different argument" with "by a
second proof of the parent's own radius-one ball theorem".  §7 "The reading is
nevertheless sharp": open it by quoting R4 §12's connective-relativity row and
positioning the width as the second coordinate.  §9 "Decided": "…subsumes the
parent's order-collapse theorem, **its radius-one ball collapse**, and the
control's coset mechanism as three instances of one criterion" (see m2 for the
order-3 row, which is not an instance).

### M3 — "THE FIFTH BREAK IS UNRELATED" IS FALSE.  IT IS CARRIED BY EXACTLY THE FAMILIES THE DDS CRITERION STILL PERMITS.

§8 reads: "four of them are one failure seen from four sides … and the fifth,
the integer velocities, is unrelated and lives in the momentum layer."

From the receipt: at L = 6 the pool carries `non_monomial: 6`, all six on
order-2 axes (`by_axis_order: {"2": {non_monomial: 6}, "3": 0, "6": 0}`), and
`velocity_census` gives `non_integer_families: 6`.  Those are the same six,
and it is forced rather than coincidental: under this unit's own velocity
definition a monomial shift by offset o has velocity −o, an integer at every
rung (the parent's own forced normalisation, R4b §4).  So *every*
non-integer-velocity family is non-monomial; at L = 6 there are exactly six
non-monomial families; therefore the two sets coincide exactly.

And those six are precisely the DDS-permitted residue: an order-2 axis has
{0,a,−a} = {0,a} with the single difference a doubled by the involution, so
the criterion permits interference there and nowhere else at L = 6.  The fifth
break is not independent of the first four — it is what is left standing after
them, and it is standing on the same criterion.

**Exact repair.**  §8, second remark: "…and the fifth, the integer velocities,
is carried by exactly the six families the criterion still permits at L = 6 —
the order-2 axes, whose stencil is difference-doubled by the involution alone.
A monomial generator has integer velocity at every rung by the definition's own
normalisation, so the break can only ever live on the non-monomial residue, and
at L = 6 that residue is the whole of it."  Head, BREAKS segment:
`INTEGER-VELOCITIES-FAIL-AT-L-6(SPEED-3/2-ON-AN-ORDER-2-AXIS)` →
`…(SPEED-3/2-ON-AN-ORDER-2-AXIS;THE-6-NON-INTEGER-FAMILIES-ARE-THE-6-DDS-PERMITTED-NON-MONOMIAL-FAMILIES)`.

This is a strengthening, not a retreat: it makes the five breaks *one*
mechanism with a residue, which is a better result than four-plus-one.

### M4 — THERE IS NO SUCCESSOR REGISTER, AND THE "SUCCESSOR PREDICTION" AS LOGGED IS A THEOREM, NOT A PREDICTION.

The paper has §11 "Deviations, and the register of scope" and §12 "The
verdict" and nothing else.  R4 §11, R4b §11 and R5 all carry a successor
register; this unit — the unit built to *test* a predecessor's successor
register — carries none.  The word "successor" appears three times in the
paper and every time it refers to a parent's.

The ledger (#214) records "successor entry: the DDS-free criterion".  As
stated that is `DDS-free ⟹ monomial-only`, which is **Theorem §3.1**: it has a
proof, it is field-free, and it cannot be falsified by a measurement.  Putting
a theorem in a prediction ledger is a category error and would corrupt the
ledger's score.

The falsifiable successor is the **converse**, and this unit measured it
without reporting it.  `dds_law` records
`arenas_dds_carrying: 5` and `arenas_dds_carrying_with_a_non_monomial: 5` —
on the declared list, DDS-carrying ⟺ interference present, 5 for 5.  The paper
reports only the sufficiency half ("Every DDS-free arena is monomial-only").
And the converse is **false in general**: my L = 9 / r = 3 coset is
DDS-carrying with 0 non-monomial unitaries over the parents' 25 and over
UNIT-7, and 54 over THIRDS-19.  The gap between the criterion's permission and
the arena's realisation is exactly the alphabet — which is this unit's own §3.4
finding, restated one level up.

**Exact repair.**  Add §11.5, THE SUCCESSOR REGISTER, with the four rows in §6
below.  Correct the ledger entry: the theorem is a THEOREM (registered as a
result, not a bet); the prediction is the converse, `DDS-carrying ⟹
interference present`, registered NECESSARY-NOT-SUFFICIENT with its
falsification condition already met once, alphabet-relatively.

### M5 — TWO OF THE FINGERPRINT'S THREE RUNGS ARE THE GAUGE PARENT'S OWN PUBLISHED TABLE, AND SO IS THE FORCING ARGUMENT.

R5 (987cd73) §7 already publishes the six-stencil profile at **L = 4 and
L = 8**, identical, on the same 64 antidiagonal coins; its head carries
`REFINEMENT=LOCAL-STABLE-BY-NON-WRAPPING…`; and its prose reads:

> "for a patch that does not wrap the generators at L = 4 and at L = 8 are
> literally the same maps on the same relative coordinates, and the two groups
> are equal by relabelling.  **Local stability could not have come out
> otherwise at any size at least as large as the widest declared stencil.**"

PER-L §5 reads:

> "the generators at the three rungs are the same maps on the same relative
> coordinates.  **Local stability could not have come out otherwise at any
> size at least as wide as the widest declared patch**, and the unit says so
> instead of reporting a coincidence."

The argument is the parent's, and the parent said it first at its own doubling
step.  Twelve of the eighteen rung-and-stencil rows are R5's.  The unit's new
content at this stage is the **L = 6 rung** and the demonstration that R5's
non-wrapping argument covers a rung *between* its two.

The unit gets the neighbouring attribution exactly right — "the two outer
values are the gauge parent's own anchored numbers, and the middle one is new"
for the global support 16/36/64, which I confirmed against R5 §7's `A16 at
L = 4 and A64 at L = 8` — which makes the omission at the *profile* rows the
more visible.

**Exact repair.**  §5, after the profile table: "Twelve of these eighteen rows
are the gauge parent's own (its §7 refinement table, at the same 64
antidiagonal coins); the six at L = 6 are new, and what they add is that the
parent's non-wrapping argument covers a rung between its two."  Attribute the
forcing sentence to R5 §7.  The head's FINGERPRINT segment may stand as
written — it states a true fact, not a novelty claim.

---

## 3. MINOR FINDINGS

- **m1 — the register's third leg is untested here, and the head does not say
  so.**  What was registered at 159200e is: "The monomial theorem is a SIDON
  property of the offset set — **transports verbatim to R = 4**, dies at any
  declared fourth direction (54 non-monomial unitaries appear)."  R = 4 is
  paper-20's *own* ladder (R = 3 is its 27-cell, 9-site arena; the site
  lattice is Z_R²).  This unit tested the mechanism and the control on the
  **L**-ladder and never entered the R-ladder.  The paper's opening paragraph
  paraphrases the register as "transports verbatim wherever the offsets are
  Sidon", silently dropping the named target.  *Repair:* one clause in §1 —
  "the register's third leg, transport to the R = 4 arena, is not tested here;
  §6 of the successor register closes it by theorem" — and see §6 row 2, which
  closes it.
- **m2 — the order-3 gap is not subsumed; it is explained-as-not-forbidden.**
  §9's "subsumes … its alphabet-relative gap at order 3 … as three instances
  of one criterion" is the wrong verb: the criterion derives nothing at order
  3, it *declines* to forbid, which is why the emptiness must be
  alphabet-relative.  §3.3 words it correctly.  *Repair:* §9 → "subsumes the
  parent's order-collapse theorem, its radius-one ball collapse and the
  control's coset mechanism as three instances of one criterion, and accounts
  for the order-3 gap by showing the criterion is silent there."
- **m3 — "an unexplained gap at 3" over-reads the parent.**  R4 declared the
  order-3 emptiness alphabet-relative in the scope note of its own order
  census and again in §3 ("The order-three alphabet-relativity is therefore
  true of the table row and irrelevant to the verdict").  What was missing was
  the *mechanism*, not the status.  *Repair:* "an unexplained gap at 3" →
  "a gap the parent declared alphabet-relative without a mechanism".
- **m4 — E-24 is applied to two of four counts over the same denominator.**
  `declared_fractions` stamps "3 of 18" and "13 of 18" COUNTING-ONLY.  The
  head's `SUFFICIENCY-HOLDS-AT-18-OF-18-ARENAS` and
  `NECESSITY-FAILS-AT-10-ARENAS` are counts over the identical declared list
  and carry no stamp.  *Repair:* add both, same reason string.
- **m5 — the locality-width = interior-radius join is FORCED, not a measured
  cross-instrument coincidence.**  Completeness is "the ball covers the
  torus", so the locality-admitting widths are {1,…,diam−1}; the interior
  radii are the radius classes strictly between 0 and diam, i.e. {1,…,diam−1}.
  The two sets are *the same set*, for any connective and any L, odd or even —
  not merely the same cardinality at three rungs.  The paper's own sentence
  ("both count the radii strictly between the point and the diameter") gives
  the mechanism and then calls the result "new" (§1) and gates it as a
  measurement.  *Repair:* stamp the row FORCED-BY-THE-TWO-DEFINITIONS, state
  the identity of the *sets* (stronger than the counts), and note it holds at
  odd L too — which makes it the one result here that says anything about odd
  rungs, honestly.  Head: `EQUAL-TO-THE-LOCALITY-ADMITTING-WIDTH-COUNT-AT-
  EVERY-RUNG` → `…-BY-THEOREM(BOTH-ARE-{1..diam-1})`.
- **m6 — the persistence table does not distinguish PERSISTS-BY-THEOREM from
  PERSISTS-AS-MEASURED.**  At least seven of the eleven are forced: LINK is
  Sidon at every L ≥ 3 (one line); monomial-only on LINK follows from the DDS
  theorem over any field; the AXIS stencil is non-Sidon at every order ≥ 3;
  VMAX = diameter is the momentum parent's theorem at every even size; the
  coin family carries no L (the receipt's own `law` says so); the profile and
  the alternating character are forced by non-wrapping (R5's argument).  A
  reader of `TABLE=24-ROWS(11-PERSIST;…)` takes eleven survivals; the licensed
  reading is four contingent survivals and seven theorems restated at three
  rungs.  *Repair:* add a `forced` field per row and a one-line note under the
  table; the head may keep its counts if the note is there.
- **m7 — one BREAKS verb is unearned as the row is named.**  "the local AXIS
  stencil is DDS-free | False | True | True | BREAKS-AT-L=6" describes a
  property the parent rung *lacked* and the new rungs *have*.  Nothing breaks;
  a criterion turns on, which the paper says in prose two paragraphs later.
  *Minimal repair that preserves the head's 11/5/8:* negate the row —
  "the local AXIS stencil carries a difference-doubled subset | True | False |
  False | BREAKS-AT-L=6".  Verified: the L = 4 axis carries one (the
  involution pair {a,−a}), the L = 6 and L = 8 axes carry none.  The other
  four BREAKS are earned as named.
- **m8 — the Z/8 sentence is licensed but the 8 is unnamed.**  "The parent's
  Z/8 was not a fact about the stage; it was the coincidence lcm(8, 4) = 8" is
  correct, and the law Z/lcm(8, L) reproduces 8, 24, 8.  But the 8 is the
  declared global-phase gauge group's order (the receipt's `law` field says
  so; the paper does not), i.e. the alphabet's phase-group order.  The
  sentence's whole force is "not a fact about the stage"; its true completion
  is "it is a fact about the declared alphabet joined to the rung".  *Repair:*
  name it — `Z/lcm(|gauge|, L)` with |gauge| = 8 disclosed as the alphabet's.
- **m9 — the interior-radius row was measured by the parent, not first
  measured here.**  R4b §6 tabulates interior radii at L ∈ {4,6,8,10,12} as
  1,2,3,4,5 and its own headline prose says "one here, 3 at L = 8".  PER-L's
  "the momentum parent's own successor claim of three at L = 8, anchored at
  its receipt and now measured" reads as a first measurement.  *Repair:*
  "…anchored at its receipt and here re-derived from a pool this unit built
  itself" — which is the real and sufficient virtue.
- **m10 — the global-stencil class rests on a mis-stated classical theorem.**
  §5: "every plaquette holonomy is a three-cycle and the family is transitive
  on the whole site set, so the classical theorem gives the full alternating
  group".  Transitivity is not enough — Jordan's theorem needs **primitivity**
  (an imprimitive group can contain a 3-cycle inside a block).  The head
  claims only the *support*, so nothing published is wrong; the prose is.
  *Repair:* cite primitivity, or restate as "the support is measured; the
  class is the gauge parent's, argued there and not re-argued here".
- **m11 — the two zeros in the CONTROL segment are theorems and are reported
  as scans.**  The L = 6 and L = 8 LINK-PLUS-4TH sets are DDS-free (I verified
  both), so "0 non-monomial" holds over *any* field, not merely over the
  parents' 25.  That is strictly stronger than the head says and it is the
  right way to answer "does the death transport".  *Repair:* head, CONTROL
  segment: `0-AT-L-6-AND-L-8` → `0-AT-L-6-AND-L-8-BY-THEOREM-OVER-ANY-FIELD`.
- **m12 — RUNBOOK §15 wants all three velocity coordinates matched.**  R4b's
  choice inventory closes with: "a successor that inherits SCOPE inherits the
  stencil, the lift and the residual with it, and any cross-unit comparison
  must match all three."  §11 declares the stencil and the lift and says the
  residual "is not re-measured here".  The break survives both un-re-measured
  coordinates and the paper should say so: the residual varies the *sign*
  only (R4b measured 768 of 1856 cells differing in sign alone), and the
  witness sits at Δs = ±6 in Z/24, not at the tie Δs = 12, so the lift cannot
  reach it.  *Repair:* one clause in §4 or §11.
- **m13 — the control rung's size is never named in the paper.**  §3.4 says
  "the control rung" eight times; the receipt says `control_rung: 3`.  A
  reader cannot tell whether the control is the parent rung or paper-20's.
  *Repair:* "at paper-20's own rung, L = 3".
- **m14 — two free parameters are priced in the receipt but absent from §11.**
  `the window widths` (GENUINELY-FREE, fibre UNBOUNDED, instances 3) carries
  no `why`, and the band sweep range `L ∈ 2…14` is not inventoried at all.
  Given that the contested row is the band, both belong in the deviations
  list.  *Repair:* add both; give the widths a `why`.
- **m15 — §7's witness sentence is loosely stated.**  "the single surviving
  lag reads twice the real part of their product" — it is twice the real part
  of c_v · conj(c_w).  The value is 0 either way, so nothing moves.

---

## 4. THE LICENSED CLAIM

Everything below is what I will sign after M1–M5 and the minors are applied.

**On the prediction.**  Licensed: *the registered Sidon prediction's mechanism
half is confirmed and its control half is refuted as stated.*  Sufficiency
holds at 18 of 18 declared arenas and holds by a theorem stronger than the
prediction gave (DDS-free suffices, and Sidon ⟹ DDS-free strictly).  The
control clause "dies at any declared fourth direction" is false *as
compressed*: the death is a joint property of the offset set and the alphabet,
and whether a given fourth direction introduces a difference-doubled subset is
a property of the rung.  Not licensed: any statement about the register's
third leg (transport to the R = 4 arena) as tested — it was not run here,
though §6 closes it by theorem.

**On the theorem.**  Licensed in full, including "over any field closed under
conjugation": the proof uses only that a product of two nonzero elements is
nonzero and that the single-term lag must vanish.  It subsumes R4's
order-collapse bound, R4's radius-one Moore-ball collapse and paper-20's coset
mechanism; it *accounts for* R4's order-3 gap without subsuming it.  Its
converse is not licensed and is measured false alphabet-relatively (M4).

**On the band.**  Licensed: *R4's unique admissible size is the width-1
section of a family of window-width sections; at width 1 the section is {4}
and both halves are forced, the absence half by a counting proof of the
parent's own field-free ball theorem; at widths 2 and 3 the involution-pair
construction admits {6,8} and {8,10,12} constructively.*  Not licensed: that
those are *the* admitted sizes at widths 2 and 3 (the complement is open
above width 1, and the evenness clause is defeated at L = 9, r = 3 over a
wider alphabet).  Not licensed: that L = 4 is "less special" — at R4's own
window it remains the unique size and R4's absence half is a theorem there.
The correct headline is **a second relativity, not a reversal**: R4 registered
that its unique scale is connective-relative; this unit adds that it is
window-relative, and the two are the same kind of fact.

**On the join.**  Licensed as a theorem about the two definitions, not as a
measured cross-instrument coincidence (m5).

**On the fingerprint.**  Licensed: *the profile is inert along the ladder and
the inertness is forced by non-wrapping* — with the parent credited for two of
the three rungs and for the argument (M5).  Licensed: the global support is
the volume, with 16 and 64 the parent's and 36 new.

**On the breaks.**  Licensed: *five invariants break, all at L = 6, and they
are one mechanism with a residue* — four faces of the DDS criterion turning
on, plus the integer velocities, which are carried by exactly the six families
that criterion still permits (M3).

**On what is not decided.**  §9's list is correct and complete except that the
band's evenness clause *is* an odd-L claim and must move out of "Nothing about
odd rungs" into the licensed/limited column.

---

## 5. ROW 3 IN FULL — DOES R4 NEED A SCOPE-ANNOTATION NOTE?

**Yes, and the #142 precedent fits it exactly.**  The reasoning:

- **R4's body self-scopes.**  Its §2 declares "Two Boolean connectives … each
  with its own radius-one ball" and sweeps locality with `neighbours = 8` at
  every L ≥ 4; its §3 theorem names "the radius-one Chebyshev ball" in the
  statement.  Both halves of `L=4-UNIQUE` are radius-one statements and R4
  says so where it proves them.
- **R4's head does not.**  `SCALE=L=4-UNIQUE(LOCALITY-IFF-L>=4;NON-MONOMIAL-
  LOCAL-AXIS-ONLY-IF-L<=4;PRESENT-AT-L-IN-{2,4})` and the SCOPE segment
  `D=2;L=4;FIELD;ALPHABET=25;GENERATORS=64;STENCIL=3-TERM-AXIS;SECTOR;
  SWEPT-RANGE=L-IN-2..9` carry the **connective** but not the **window
  radius** — the one coordinate this unit moved.  `LOCALITY-IFF-L>=4` is false
  at width 2 (this unit's own table: L = 4, r = 2, locality no) and the head
  gives a reader no way to know it was a radius-one sentence.
- **R4 §12 registered the neighbouring relativity and not this one.**  It
  registered connective-relativity as the programme's fifth false claim,
  strengthened to "the unique scale is a theorem about the declared link set
  of the record stage".  Window-relativity is the second axis and was not
  registered.
- **R4 §11 and R4b §9 both carry a trichotomy that is now a quadrichotomy.**
  R4: "any dispersion measurement must either widen the modulus set, leave the
  local class, or leave the admitted size."  R4b: "must leave the local class,
  widen the alphabet, or leave the admitted size."  There is a fourth branch:
  **widen the window** — at width 2 the sizes 6 and 8 carry a non-monomial
  generator that is local under the ported criterion at that width.  Whether
  that counts as "leaving the local class" depends on whether "local" means
  radius-one; R4 means radius-one, so the branch is a *re-partition* of the
  trichotomy, not a refutation of it.

**Register row, written for the adjudicator to lift verbatim:**

> **PAPER-10 (R4) — SCOPE ANNOTATION, NOT AN ERRATUM.**  R4's
> `SCALE=L=4-UNIQUE` is a theorem at R4's declared window radius, which is one:
> the locality half sweeps the radius-one max-norm ball (§2, "each with its own
> radius-one ball"), and the interference half is proven for the whole
> radius-one ball, field-free (§3, Moore-ball collapse).  Both are true of that
> object.  R4's head string carries the forced connective but not the radius.
> PER-L measures the same two requirements at window widths 2 and 3 and finds
> they meet again — at {6,8} and at {8,10,12} respectively, by an
> involution-pair construction verified against R4's own whole-torus criterion.
> Nothing of R4 is withdrawn: at radius one the admitted set is {4} and PER-L
> re-proves the absence half by a second, counting proof of R4's own ball
> theorem.  What is annotated is the reading: **`L = 4 is unique` is a
> statement about the parent's window, as `MAX-NORM` is a statement about the
> parent's link set — the same species of relativity R4 §12 already
> registered, on a second coordinate.**  The R4 §11 and R4b §9 trichotomies
> ("widen the modulus set / leave the local class / leave the admitted size")
> gain a named fourth branch, *widen the window*, which sits inside "leave the
> local class" only because "local" there means radius-one.  Paper-10 and
> paper-15 are terminal and are not edited.

Write it as `v14/note-r4-scope-annotation.md`, structured on
`note-paper12-scope-annotation.md`: §1 the two objects, §2 the cell where they
diverge (L = 6 at width 2), §3 the corpus-wide caution — *any claim in this
corpus of the form "locality requires L ≥ n" or "the collapse bound is L ≤ n"
is window-scoped unless the window is declared beside it* — §4 what the note
does and does not do, §5 provenance (PER-L's gates `G-LOCALITY-WINDOWS`,
`G-BAND-LAW`, and this seat's independent rebuild).

---

## 6. ROW 4 — DOES PAPER-20 NEED A NOTE?  AND ROW 10 — THE SUCCESSOR REGISTER

**Paper-20 needs nothing, and the adjudication note must NOT be edited.**
Paper-20 §S-6 says: "The monomial-only theorem of §3.1 is a property of the
offset set and transports as long as that set stays as it is; a fourth
declared direction would end it."  That is true of paper-20's own object.
`review-coup-effectus.md` S-EF-1 is likewise careful: it names the specific
fourth direction {e₁,e₂,e₁+e₂,e₁+2e₂}, the specific 19-value probe, the
multiplicities [1,1,1,1,1,1,3,3], the witness c = (1/3,0,−2/3,−2/3) on the
line {(1,0),(1,1),(1,2)}, and the mechanism "interference returns exactly when
the offset set contains a coset of a subgroup".  I reproduced every one of
those and they are all correct.

**The over-claim entered at the compression step**: the adjudication's
SUCCESSOR REGISTER dropped the alphabet, dropped the specific offsets, and
universalised the quantifier to "dies at **any** declared fourth direction".
That is precisely the half PER-L refutes, and PER-L's "false as stated" is the
right verb.  The adjudication note is the *record of what was registered* —
editing it would destroy the datum that the failure entered at compression, not
at measurement.  PER-L's in-paper correction (§3.4) suffices for the content;
what is missing is the ledger entry and this unit's own register.

**THE SUCCESSOR REGISTER — four rows, for §11.5:**

1. **PREDICTION LEDGER, entry (g), split into three.**  A half-right
   prediction is recorded as its parts, never as a fraction:
   - **(g1) mechanism — CONFIRMED AND STRENGTHENED.**  "The monomial theorem
     is a Sidon property of the offset set", sufficiency direction: holds at
     18 of 18 declared arenas and is now a theorem with a weaker hypothesis
     (DDS-free ⊋ Sidon).  Tested at rungs the predictor never ran.
   - **(g2) transport to R = 4 — CLOSED BY THEOREM, NOT BY MEASUREMENT.**  The
     link set {(1,0),(0,1),(1,1)} is Sidon at every L ≥ 3, hence DDS-free,
     hence monomial-only **over any field** — including paper-20's own
     (1/3)Z[ω].  The register's named target needs no scan and no R-ladder
     run.  *(This seat verified the L = 4 row directly: 24 unitary, 0
     non-monomial.)*
   - **(g3) control — REFUTED AS STATED.**  "dies at any declared fourth
     direction (54)": the 54 is reproduced exactly with the same witness
     support, and is alphabet-relative (0 over the parents' 25, 0 over
     UNIT-7); the death does not transport up the L-ladder, and there by
     theorem (m11).  The universal quantifier was introduced at the
     compression from S-EF-1 to the register, and the ledger should say so —
     it is a governance datum, not a physics one.
   - **Score:** one confirmed, one closed-by-theorem, one refuted-as-stated.
     Not "half right".
2. **THE NEW PREDICTION, with its falsification conditions.**
   `DDS-CARRYING ⟹ INTERFERENCE PRESENT` — **NECESSARY-NOT-SUFFICIENT**.
   Status: holds 5 of 5 on this unit's declared list (receipt `dds_law`),
   and **already falsified once, alphabet-relatively**: the order-3 coset in
   the radius-3 ball at L = 9 is DDS-carrying and carries 0 non-monomial
   unitaries over the parents' 25 and over UNIT-7, and 54 over THIRDS-19.
   *Falsification condition, stated forward:* a DDS-carrying offset set whose
   non-monomial unitaries are empty over every alphabet closed under the
   declared field's conjugation would refute it structurally; a
   difference-doubled set is a *permission*, and what converts a permission
   into a realisation is the alphabet.  The theorem `DDS-free ⟹ monomial-only`
   is registered as a **result**, not a bet.
3. **PER-R (paper-29) inherits, in order of value:**
   (i) g2 above — the R-ladder's coin register is forced at every R ≥ 3 by
   theorem, so PER-R must not spend a scan on it and must instead ask what its
   *own* offset set is (S-EF-1's "posed, not solved: paper-21 must state its
   offset set before it inherits F3" is still open, and the DDS criterion is
   the thing to run against it the moment it is stated);
   (ii) the alphabet-relativity discipline — every count of non-monomial
   unitaries in this corpus is a joint property of the offset set and the
   alphabet, and the R-ladder's alphabet is (1/3)Z[ω], not the parents' 25;
   (iii) the coset mechanism as the R-ladder's live danger: paper-20's arena
   is over F₃, so cosets of order-3 subgroups are cheap there and the
   criterion will bite;
   (iv) NOT inherited: the L-ladder's window band, VMAX = L/2, the eigenphase
   law Z/lcm(8,L) and the interior-radius count — all four are statements
   about (Z_L)² with this alphabet and none has been asked of the R-ladder.
4. **GGS's first datum, and the odd-rung gap.**
   GGS receives: *the (order, support) profile is inert along L and the
   inertness is forced by non-wrapping* (R5's argument, extended by one rung
   here) — so the group is selected by the local stencil and not by the
   lattice, and any group-selection law GGS proposes must be a law about
   stencils.  The global class is the parent's and rests on a theorem this
   unit mis-states (m10); GGS should re-derive it with primitivity.
   The odd-rung gap: correctly declared open for the ladder, but **the band
   makes an odd-L claim and it is the one that fails** (M1), and the
   width/interior-radius identity (m5) holds at odd L by theorem.  The odd-L
   blade, when it runs, starts at L = 9 with width 3 — this seat's
   counterexample is its first datum.

---

## 7. WHAT I ATTACKED AND COULD NOT BREAK

Recorded so the adjudication knows the negative space.

- **The DDS theorem.**  The proof is correct as written and the field-freeness
  is real: only "a product of two nonzero elements is nonzero" and "an
  involution takes nonzero to nonzero" are used, so it holds over any integral
  domain with an involution, in any characteristic.  I could not construct a
  unitary map whose support carries a simple internal difference.
- **The eighteen-arena table and the control table.**  Rebuilt cell for cell
  on an independent field implementation.  Nothing moved.
- **The 54.**  Reproduced with the same support, and the two unitary totals
  (78 here, 72 in paper-20's K2 probe) are reconciled exactly by the
  monomials on the extra offset: 78 = 54 + 4·6, 72 = 54 + 3·6.  This is a
  stronger reproduction than the paper claims for itself.
- **The band identity under the unit's own predicate.**  Equal at all three
  widths; every witness unitary at all L² lags.  The attack the paper invited
  — a size outside the band at width 2 carrying a local non-monomial unitary —
  I could not produce: at width 2 the only coset in the ball is at L = 6,
  already in the band, and no involution pair exists above L = 8.
- **VMAX and the walls.**  VMAX = L/2 = diameter at all three rungs; the
  antipodal monomial attains it; the momentum parent's even-L theorem is not
  disturbed.  The speed-3/2 witness does **not** collide with any R4b terminal
  sentence: R4b's §9 "Not decided" explicitly excludes "a larger lattice" from
  its integer-velocity claim, and its derivation ran through the Q(ζ₈) parity
  grading, which does not survive the field change.  The break is licensed and
  the wall holds.
- **The four walls.**  No continuum, no scaling, no thermodynamic reading, no
  transport number inherited.  §1 and §9 both say so and the head's SCOPE
  segment carries it.  I found no smuggled limit anywhere in the text.
- **The pool arithmetic.**  58/42/106 reproduce from Σ(per-axis gauge classes)
  − (axes − 1) at all three rungs, and the by-order buckets reconcile with the
  shared identity assigned to the top bucket.  The non-monotonicity is exactly
  what the paper says it is.
- **The paper's own honesty rows.**  The DECLARED-WINDOW at |S| ≤ 12, the
  "presence band above width 1", the COUNTING-ONLY stamps that are present,
  the "no group-selection law is claimed here", the refusal to inherit a
  transport number, the naming of the L = 4 five-point disclosure's absence
  from scope — all correct, and several of them are the reason M1 is a fix and
  not a kill.

---

## 8. WHAT WOULD CHANGE MY GRADE

To **A**: M1–M5 applied as written, the successor register added, the R4 scope
annotation drafted as a standing note.  Nothing here requires a re-run of the
instrument except the head string, the two table labels, one persistence row's
name and the receipt's `declared_fractions` — and the band table if the
adjudication wants the L = 9 row rendered rather than remarked.

To **R**: only if the adjudication decides that a head asserting "ARE" over a
set the unit defined by one construction is a false claim rather than an
under-scoped one.  I do not so decide: the paper discloses the one-sidedness
two paragraphs below the table and again in the head's own last clause, which
is the behaviour of a unit trying to be caught rather than one hiding.

---

*Object hashes re-verified at close, unchanged: `bd0298e2a482` /
`976d5b9e4ac8` / `e4ff37a7a13e` / `54ec5a9e9b72`; pin `973b160d52ed`.
Recomputation scratch at `.../scratchpad/perl-ef/`; the independent field and
scan implementation is `recompute.py` there and shares no line with the
instrument.  This seat wrote one file in the repository and read no sibling's
uncommitted state.*
