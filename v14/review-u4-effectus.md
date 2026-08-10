# U4 (paper-14) — EFFECTUS-LENS HOSTILE REVIEW

**Reviewer:** effectus (meaning, scope, motivation; K4 decisive).
**Object:** paper `7e6db49f0e6e`, code `c1ae8ec7fdbe`, output
`d1bfbbca40c9`, receipt `ae7a4ce48538` (commit 06b89fe). Pin
`06b62ecb60a9`. Protocol `c4f2b33aa315`. Founding spec
`37a428321f46`. Adjudication `7213d26ea4d4`. Scout `88375db9cec2`.
**All ten object/authority hashes verified byte-exact**, plus six v10
constructor shas (`684cdb76552b`, `3d0516ab106e`, `e80edf851d93`,
`89e170f40579`, `576275d55ecf`, `f0b578c13409`) — all exact.

**GRADE: AWF (ACCEPT WITH FIXES).**

**Recomputations: 390. False numbers found: 0.** Every table in the
paper reproduces from the receipt and, where independently derivable,
from my own routes. The four walls are clean. The four MAJORs are
scope-and-attribution defects in prose; **no number moves and neither
verdict string moves.**

---

## 1. THE WALLS AUDIT (decisive) — NO BREACH

The decisive cell passes at all four walls. Each is gated in SEC 8 of
the output with evidence, and each gate's claim survives my check.

| wall | requirement | verdict |
|---|---|---|
| **L-1** | order-level covariance only; ARGUED before tested, or not tested; retracted wording BANNED | **CLEAN** |
| **BHS** | no sprinkling-grade LI test anywhere | **CLEAN** |
| **KR** | height control on any dimension reading; BLOCKED rather than proceed | **CLEAN** (but see MAJOR-3) |
| **DIAGONAL** | `q₁₂ ≡ 0` inherited; NAMED AND NOT READ | **CLEAN** |

**L-1.** The banned sentence ("precisely the form U4 tests, and
precisely the form the corpus's strongest relativity result took") does
not occur in the paper. It occurs in the code exactly once, at
`u4_crystals_exact.py:1008–1009`, as the `BANNED` constant the gate
searches *for* — the correct construction, and `G-WALL-L1` reports
`banned_sentence_hits: []`. The fourth form is named as a fourth form,
its admissibility argument is stated as owed, the argument is given
(admissibility needs a group on the generated causal order plus a reason
to read it as a covariance group; the arena supplies neither, and the
corpus has no bridge from Z₃² translations to any boost), and the form
is then **not tested** (`fourth_form_tested: false`). L-1 §6's C2 is
satisfied — target named, form named with it. The pin's disjunction
("argued-before-tested **or** not tested at all") is met on its second
limb, which is the stronger limb.

The unit further invokes L-1 §5's scope guard verbatim ("does **not**
forbid a permutation action") to place the Z₃² stabilizer outside the
fourth form's jurisdiction. I verified the quote at
`v11/note-L1-lorentz-no-go-lemma.md:290` and the reasoning holds: a
translation action on a nine-element actor set is a permutation action,
and needs no covariance argument.

**BHS.** No sprinkling, boost, rapidity or frame appears in any
measurement. The five occurrences of those words in the paper are all
inside §8's refusal and §11's registration. `sprinkling_grade_LI_tests_run: 0`.

**KR.** The catalog's engraved sentence, quoted by the pin and the paper
— "a dimension reading without a height control is worthless" — is
**verbatim** at `note-v11p0a-reproduction-catalog.md:1.7(e)`. The unit
reads exactly one dimension-adjacent row (chart width), carries the
longest chain of all ten populations with it, and returns BLOCKED on
every population-averaged row rather than proceeding. That is the wall's
letter and more than its letter.

**DIAGONAL.** Named in §5, argued in §8, registered in §12 (S-U4-7).
The counterpoint is stated and explicitly refused. §7's candidate
reading (i) — axis counts as the crystal's own `q₁₁`/`q₂₂` — is left a
candidate and never assembled with the inherited `q₁₂` into a metric.
**Not read.** (I did assemble it, in §6 below; that is a reviewer's
finding handed to the successor, not a defect in the unit.)

---

## 2. THE VERDICT PAIR'S HONESTY

### 2.1 What is measured, verified independently

I recomputed all ten stabilizers by brute-force translation over Z₃²,
sharing nothing with the unit's two routes: **10/10 agree on the element
set, the order and the support.** The claim is TRUE as stated at every
cell, and the control returns its other value at both readings.

### 2.2 Candidate readings of "form a crystal"

- **(R1) The field's translation stabilizer is nontrivial.** ✔ MEASURED,
  10/10 cells, three independent routes.
- **(R2) The renewal sublattice has a period lattice ⟨(1,1)⟩ as a
  discovered structural fact.** ✔ true as arithmetic, ✘ **misleading as
  provenance** — see MAJOR-1. The direction is the constructors'.
- **(R3) A nontrivial period lattice was found at all ten cells.** ✘
  **FALSE, and the verdict string invites it.** At CG32/CG34 footprint
  the string reads `Z3^2` — which sounds maximal and is in fact the
  *degenerate* case: the field is constant (2,2,…,2 and 4,4,…,4), and a
  constant field is stabilised by everything. §5 discloses the
  constancy; §10's read-out does not. See MINOR-4.
- **(R4) The control demonstrates the instrument detects aperiodicity.**
  ✘ **FALSE.** See MINOR-1: with one division event the trivial
  stabilizer is forced by a theorem, not found by a measurement.
- **(R5) Emergent/dynamical periodicity of division events.** ✘ **NOT
  LICENSED.** MAJOR-1.

### 2.3 Candidate readings of the geometry segment

- **(G1) On the one row a population restriction cannot confound, the
  restricted maximum equals the full maximum at 4/4 arbitration crystals
  and differs at the control.** ✔ MEASURED, 40/40 numbers verified. The
  §6.2 lemma ("a maximum over a subset equals the maximum over the whole
  set exactly when the maximum is attained on the subset") is correct,
  and correctly scoped to the POP sub-reading, where `profile(C, pop)`
  holds the poset whole and moves only the population.
- **(G2) "The renewal-only record has the same geometry as the full
  record."** ✘ **NOT LICENSED**, and the verdict string's word
  `GEOMETRY-INVARIANT` invites it. Under POP the poset is *identical by
  construction*, so nothing could have varied except population
  statistics; under SUB — the only sub-reading where the question is
  meaningful — the geometry is drastically different (max|D| 9,9,6,6,3 →
  3,3,0,3,0; longest chain 14,18,6,14,21 → 5,7,2,4,1) and no claim is
  made; under BUILDER-RERUN the object does not exist.
- **(G3) The falsifier was tested and came back negative.** ✘ **FALSE.**
  MAJOR-2.
- **(G4) Beyond chart width, invariance at other rows.** ✘ correctly
  refused; `BLOCKED` is the unit's own reading of §6.3, and the five
  `MEASURED-THEN-DECLINED` waivers back it per crystal.

**No candidate reading in the paper's own prose is false.** The paper is
honest cell by cell. The over-readings live in (a) the two verdict
strings standing alone, and (b) one asymmetric guard in §6.6.

---

## 3. HEIGHT PURITY — WHAT IT MEANS, AND WHETHER "FORBIDS" IS THE HONEST STRENGTH

Verified: `mixed_layers = []` at all five records; deficit 18, 24, 6,
12, 1 — i.e. **the height-matched control is empty at every crystal, and
empty by the full amount**. There is no unmarked event at any marked
height, anywhere.

**What height purity means at citable scope.** Division events are
**global temporal sheets** of the record: they occupy whole layers of
the event poset and share them with nothing. Every event at a marked
height is itself marked. The licensed sentence:

> On these five records the division events are height-pure: they fill
> whole layers of the event poset and share those layers with no other
> event, at 5 of 5 records including the control.

**What it does NOT license.** It is not a statement that division events
are simultaneous in any physical sense, nor that the height function is
a time; height is the poset's own longest-chain grading and the corpus
has no clock reading attached to it here. It is also not (yet) a
grammar theorem — S-U4-3 correctly leaves "theorem or artefact of these
five schedules" open.

**Is "forbids rather than qualifies" the honest strength?** *For the
population-averaged rows, yes.* The KR warning's remedy is a control; if
the control is provably unconstructible, no amount of qualification
recovers the reading, and BLOCKED is stronger and more honest than a
caveated INVARIANT. The unit is to be credited: it took the harder
verdict when a softer one was available, and it imposed on itself a
**stricter** standard (a matched control *population*) than the wall
demanded (the longest-chain *discriminator*, which it has). That is the
right direction of error.

*But the strength is over-attributed*, which is MAJOR-3: the object the
catalog calls the height control exists here and is reported; the object
that is empty is a stronger one of the unit's own devising (choice
inventory row 10, correctly classed **free**). Two different objects
carry one name across §6.1, §8, the verdict string and five receipt
waivers.

---

## 4. THE RENEWAL-ONLY REFUSAL — "the sparse world cannot be built sparse"

Verified: all five refusals at the first delivery (`D00->D01` at prefix
12 ×2; `G00->G10` at prefix 12 ×2; `spread G00->G01` at prefix 2), and
the isolation control rebuilding all five **event for event** (72, 96,
30, 66, 46, `idle_free_identical: true`) when only the idle tag is
dropped. The tag isolation is clean: exactly one kinematic tag blocks
the rebuild and it is the delivery.

**The licensed sentence at citable scope:**

> Under the declared sub-grammar that drops the two tags the [POSIT]
> calls kinematics, none of the five committed crystals can be rebuilt;
> each halts at its first delivery. Dropping only the idle tag rebuilds
> all five event-for-event. On this arena the delivery is the sole
> blocking kinematic tag: the crystals' construction consumes
> deliveries, so the sparse record is not constructible in the committed
> grammar.

**Over-readings killed.**
- ✘ "Kinematics and law do not separate." The unit itself refuses this
  (§6.6) and is right to: non-constructibility is a scaffolding fact,
  not a failure of separation.
- ✘ "Kinematics and law *do* separate." Equally unlicensed — and this is
  the direction §6.6 leaves unguarded (MAJOR-2).
- ✘ "Renewal-only records are impossible in the ISP grammar." Scoped to
  *these five constructors' schedules* and to arm (b)'s declared
  sub-grammar shape (fiber 1, D74's `filt`). S-U4-6 correctly registers
  the general question as unasked.
- ✔ "The delivery is constitutive of these crystals" — licensed, and it
  is the unit's genuine contribution here.

---

## 5. THE CHOICE INVENTORY AT THE RSQ STANDARD

Eleven rows, fibers computed. My audit of the classifications:

| # | item | unit's class | my verdict |
|---|---|---|---|
| 1 | the five crystals | forced/1 | **sustained** (pin R1) |
| 2 | control identity | forced/1 | **sustained** |
| 3 | marking = arbitration tag | forced/1 | **sustained, and honestly annotated** — the "where it binds" column already says "three rows, one reaching this arena"; §3 discloses that the class-0 clause has no 9-actor referent and that S4's hypothesis is vacuous here (0 pair arbitrations of 61). The two silent rows are discharged by two *unshared* re-derivations: a tag-free shape predicate selecting the identical set index-for-index (18, 24, 6, 12, 1) and the renewal-to-root property at 61/61. That is stronger than the pin asked for. |
| 4 | site carrier actors → Z₃² | forced/1 | **sustained** — the constructors name actors `D{i}{j}`/`G{i}{j}`; `G-SITEMAP` gates the bijection per crystal; MUT-SITEMAP guards it. |
| 5 | site reading | declared/2 | **sustained; both arms genuinely run.** Divergence is measured, not assumed: agreement at 2 of 4, divergence at 2 of 4, and **one-directional** — the footprint reading enlarges (3→9 at both CONFLICT-GRIDs) and never shrinks. Verified at all eight arbitration cells; ⟨(1,1)⟩ lies inside all eight. |
| 6 | renewal-only operationalization | declared/3 | **sustained.** (a) and (b) both run; **(c) QUOTIENT properly registered-not-run** — `G-GEOM-ARMC-REGISTERED`, waiver class `REGISTER-ONLY`, "its absence is visible in the arm rows, which carry (a) and (b) only", and nothing in either verdict descends from it. This is the correct handling. |
| 7 | POP / SUB sub-reading | declared/2 | **sustained**, both run, §6.2–§6.4 per sub-reading, SUB reported-not-certified (§11 dev 4). |
| 8 | arm (b) sub-grammar shape | declared/1 | **sustained** (D74 shape, support-restricting only). |
| 9 | geometry row set | forced/1 | **sustained** (D66 rows over D58/D47a, reproduced at v10's numbers). |
| 10 | height control construction | **free** | **sustained and correctly flagged** — and this is precisely the row MAJOR-3 turns on: a free instrument-side object was given the wall's name. |
| 11 | stabilizer as periodicity measure | **free** | **sustained**; two-way gated; the pin names the stabilizer, not its algorithm. |

"Two free items, both instrument-side and both two-way-gated. No free
item enters the verdict's data" — **verified true**, with the caveat
that free item 10's *name* entered the verdict string.

**The footprint reading's rise to full Z₃²: what it means.** Not extra
structure — *less*. It means the count field is constant, i.e. every one
of the nine actors appears in the register footprint of the same number
of division events. On CONFLICT-GRID this is immediate from the group
system: each round partitions the grid into three groups and arbitrates
once per group, so every actor sits in exactly one arbitration footprint
per round, giving n ≡ R. The rise to Z₃² is the signature of a
**partition**, not of a richer lattice.

---

## 6. WHAT IT HANDS THE WELD LINE — the most consequential section

**The FOUND-side arena now exists.** Before U4 the crystal side of the
weld was an event record; U4 delivers, for the first time, an object of
**the same species as I7's**: a site set X = Z₃², a link-indexed count
field, and a measured symmetry group. The renewal-crystal weld census is
therefore posable like-for-like. I ran the comparison, and its answer is
already determined by U4's own numbers.

**I7's arena** (paper-13 SEC 2.1, read at committed HEAD `9cdb10472953`):
sites Z₃²; **links L = {(1,0), (0,1), (1,1)}**; geometry record
`n_ℓ(x) ∈ Z_{>0}` at each of the 9 × 3 = 27 cells; readout
`q₁₁ = n_{e₁}`, `q₂₂ = n_{e₂}`, `q₁₂ = (n_{e₁+e₂} − n_{e₁} − n_{e₂})/2`.

**U4's bridges, evaluated on I7's coordinates** (my computation, exact):

| crystal | n_(1,0) | n_(0,1) | n_(1,1) | q₁₁ | q₂₂ | q₁₂ | det | I7 cells > 0 |
|---|---|---|---|---|---|---|---|---|
| DOUBLE-GRID(3,2) | 2 | 2 | 0 | 2 | 2 | −2 | **0** | 18 of 27 |
| DOUBLE-GRID(3,3) | 3 | 3 | 0 | 3 | 3 | −3 | **0** | 18 of 27 |
| CONFLICT-GRID(3,2) | 1 | 1 | 0 | 1 | 1 | −1 | **0** | 18 of 27 |
| CONFLICT-GRID(3,4) | 2 | 2 | 0 | 2 | 2 | −2 | **0** | 18 of 27 |
| D60-GRID(3,12) | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0 of 27 |

Three facts fall out, none of them in the paper:

1. **U4's bridges independently reproduce weld 2's
   `INDUCED-DET=0-AT-EVERY-SITE-OF-EVERY-CRYSTAL`.** With the diagonal
   count zero and the two axis counts equal and homogeneous, the induced
   form is `c·[[1,−1],[−1,1]]`, whose determinant is identically zero.
   This is a cross-unit consistency check the corpus did not have.
2. **The kernel of that degenerate form is spanned by (1,1)** —
   `[[1,−1],[−1,1]]·(1,1)ᵀ = 0`. So the direction weld 2's induced metric
   is blind along is the same direction U4 measures as the
   division-event field's period.
3. **I7's third link *is* the diagonal.** The renewal sublattice supplies
   18 of I7's 27 cells strictly positive and translation-homogeneous, and
   fails **exactly the 9 diagonal cells** — by I7's own strict-positivity
   criterion. The FOUND-side arena is inadmissible at I7 for the same
   reason, at the same link, that killed the crystals in weld 2.

**What this forces the census to confront.** The diagonal counterpoint
the unit names and refuses to read is **not a coincidence to be
explained — it is jointly forced by one design choice**, and a successor
must not count the two (1,1)'s as independent evidence. Both trace to
the constructors: seeds on the diagonal (and its mod-3 shift), conflict
groups on rows and columns. The seed rule makes the count field
⟨(1,1)⟩-periodic; the row/column group system makes the link set the two
axes and leaves the diagonal empty. One choice, two appearances of
(1,1), zero independent confirmations. The paper's §8 is right that they
are different objects; it does not know they are the same cause.

### Successor register rows this review hands forward

- **S-EF-1 (the renewal-crystal weld census, division-event lattice ↔
  I7).** Posable now, and **predictably EMPTY**: 18 of 27 cells positive
  and homogeneous, 9 diagonal cells zero, induced det ≡ 0 at every site
  of every crystal, kernel ⟨(1,1)⟩. The census must be run to record the
  verdict, not to discover it. It must state up front that the FOUND-side
  and deformation-side (1,1)'s are one cause, not two witnesses.
- **S-EF-2 (the diagonal, priced).** A carrier populating a diagonal pair
  is the single unblocking move for both weld 2 and the renewal census.
  The scout's S1 supplies the target (Cayley(Z₃², {e₁,e₂,e₁+e₂,e₁−e₂}) ≅
  K₉, 8-regular, 362,880 isomorphisms; the mismatch is 4 grammar
  directions vs I7's declared 3) and the price (a declared channel
  sub-grammar, Route-B-adjacent). U4 adds the datum that the diagonal is
  the *period* direction of the count field, so populating it perturbs
  the symmetry as well as the link set.
- **S-EF-3 (what may NOT be inherited).** The delivery-crystal control's
  rows are scoped to a record with **one** division event. Its trivial
  stabilizer, its 0-of-27 I7 cells and its `VARIES` width row are all
  consequences of that single count. Nothing about delivery crystals in
  general, and nothing about aperiodicity, may be inherited from it.
- **S-EF-4 (more crystals / d = 3).** The two structural facts a new
  crystal must be checked for *first* are the two this unit found to be
  degenerate here: is its division set height-pure (if yes, the geometry
  segment is BLOCKED again by the same theorem), and is its seed set a
  union of cosets of a nontrivial subgroup (if yes, the crystal claim is
  constructor-inherited again). A d = 3 or non-coset-seeded constructor
  is the first arena where "form a crystal" would be a finding rather
  than a restatement.
- **S-EF-5 (the indivisibility probe).** MAJOR-4's row: the founding
  spec's own clause is unposable on a FORCED record. See below.
- **S-EF-6 (paper 8's form 2).** L-1 §5 records projective compatibility
  of different finite batteries as surviving **both** L-1 and the BHS
  block and "stays on the table for U4". Neither run nor registered.

---

## 7. FINDINGS

### MAJOR-1 — The periodicity is constructor-inherited, and the paper does not say so

**All eight arbitration-crystal fields are derivable in closed form from
the constructors' seed rule and loop counts, with no record built at
all.** I derived them and they match the receipt exactly, site for site:

- `double_grid` seeds are `ac[i][i]` and `ac[(j+2)%g][j]` — the diagonal
  and a mod-3 shift of it, i.e. the two ⟨(1,1)⟩-cosets `j−i ≡ 0, 1`. Each
  seed arbitrates once at mint plus once per round, so the initiator
  field is `(R+1)·1_seeds`: **[3,3,0,0,3,3,3,0,3]** at R = 2 and
  **[4,4,0,0,4,4,4,0,4]** at R = 3.
- Every actor lies in exactly two groups, so the footprint field is
  `2R + 1_seeds`: **[5,5,4,4,5,5,5,4,5]** and **[7,7,6,6,7,7,7,6,7]**.
- `conflict_grid` seeds are `ac[i][i]` in both parities — the single
  diagonal coset — giving **[2,0,0,0,2,0,0,0,2]** and
  **[4,0,0,0,4,0,0,0,4]**; and each round partitions the grid, giving the
  constant footprint fields **[2]×9** and **[4]×9**.

A seed set that is a union of cosets of a nontrivial subgroup *cannot*
fail to produce a nontrivial stabilizer. The ⟨(1,1)⟩ direction is written
into `ac[(j+2)%g][j]` and `ac[i][i]` in the committed constructors. The
measurement is correct and the verdict is true; what is missing is that
its **provenance is the constructor's own symmetry, not the dynamics.**

This is not fatal — the pin asked for the claim to be made corpus-grade,
and it is. But an undeflated "the division events of a conflict crystal
do form a crystal" will be inherited as an emergent fact, and it is not
one.

**Exact repair.** Add to §5, after the stabilizer table:

> **Where the periodicity comes from.** It is the constructors'. D66
> seeds `double_grid`'s row groups at `ac[i][i]` and its column groups at
> `ac[(j+2)%g][j]` — the diagonal and its mod-3 shift, i.e. two full
> ⟨(1,1)⟩-cosets — and seeds `conflict_grid` at `ac[i][i]` in both
> parities. Each seed arbitrates once per round (plus once at mint on the
> DOUBLE-GRIDs), and every actor lies in two groups on the DOUBLE-GRIDs
> and one per round on the CONFLICT-GRIDs. All eight arbitration fields
> above follow in closed form from those two facts, with no record built:
> `(R+1)·1_seeds` and `2R + 1_seeds` on the DOUBLE-GRIDs, `R·1_diag` and
> the constant `R` on the CONFLICT-GRIDs. A seed set that is a union of
> cosets of a nontrivial subgroup cannot fail to have that subgroup in
> its stabilizer. The claim is therefore TRUE and *inherited*: the
> division events of these crystals form a crystal because their
> constructors seed conflict on a coset and group by rows and columns.
> Whether any constructor whose seed set is not a coset union produces a
> periodic division field is the open question, and it is not asked here.

And **downgrade S-U4-5** from open to derived: the one-directionality of
the reading divergence follows from the footprint field being
`(group multiplicity) + 1_seeds` with the group system carrying at least
the seed set's symmetry — so the footprint stabilizer contains the
initiator's on these constructors. Restate S-U4-5 as: "one-directional
here by the group system's symmetry; whether it holds for a constructor
whose group system is *less* symmetric than its seed set is open."

### MAJOR-2 — §6.6 guards one direction of the falsifier and not the other

§6.6 says the third falsifier "**does not fire**", then correctly guards
against the anti-separability reading ("it is not evidence that
kinematics and law fail to separate"). It never guards the other
direction. A pre-registered falsifier that "does not fire" reads, in the
corpus's own idiom, as a test that ran and returned negative — i.e. as
support for separability. It did not run.

On this arena the falsifier is **not evaluable**: under POP the poset is
unchanged by construction so nothing *could* vary; under SUB the poset
really does change — and changes drastically (§6.4: max|D| 9,9,6,6,3 →
3,3,0,3,0; longest chain 14,18,6,14,21 → 5,7,2,4,1) — but the unit
correctly rules the two posets incomparable; under BUILDER-RERUN the
object does not exist. Three sub-readings, no evaluable test.

**Exact repair.** In §6.6, after "Nothing here shows sparse records
destroying a geometry", insert:

> Nor does anything here show them preserving one. On this arena the
> falsifier is **not evaluable**: under arm (a)-POP the poset is held
> whole by construction, so no geometry could vary; under arm (a)-SUB the
> geometry does change substantially, but the two posets are different
> objects and the comparison is refused (§6.4); under arm (b) the object
> does not exist. The falsifier does not fire because it cannot be
> evaluated here, not because it was tested and returned negative.

### MAJOR-3 — The KR refusal's stated ground names the wrong object

Two distinct objects carry the name "height control":

- **(i)** the catalog's — the **longest chain**, reported alongside the
  dimension reading so a KR order is unmasked (§1.7(c): "unmasked only by
  a height-based estimator (longest chain 3 vs a sprinkling's 46)"). The
  unit **has** this, for all ten populations, and `G-WALL-KR` prints it.
- **(ii)** the unit's own — a **height-matched control population**,
  drawn from unmarked events (choice inventory row 10, class **free**).
  This is empty everywhere.

§6.1, §8, the verdict string and five receipt waivers ("the KR control
the catalog requires is empty") attribute the emptiness of (ii) to the
requirement (i). The consequence is not cosmetic: it is the stated ground
for declining the max-shatter meter, one of the two catalog tests paper 0
§7 attaches to U4, and it propagates into **S-U4-2**, where it tells a
successor the wrong precondition. Two further points sharpen it: catalog
§1.8 grades max-shatter as "a 1+1-escape detector, **never** a dimension
estimator", so the KR clause about *dimension readings* is not obviously
its gate at all; and the sparse posets (n = 1…24, heights 1…7) are far
too small for any acceptance gauge to discriminate — which is the real
and sufficient reason.

**Exact repairs.**
1. §6.1, at the head: "The catalog's own requirement — that a dimension
   reading carry its height — is met: the longest chain of every
   population is reported below. What this section adds is a stricter
   object of this unit's own devising (choice inventory row 10), a
   height-*matched control population*; and that object is empty."
2. §8, KR paragraph, replace the max-shatter clause with: "the
   max-shatter meter is not run for two reasons, neither of them the KR
   discriminator, which this unit carries: the catalog grades it a
   1+1-escape detector and not a dimension estimator (§1.8), and at
   n ≤ 24 events and heights ≤ 7 no acceptance gauge on these sparse
   posets could discriminate."
3. **S-U4-2**, restate: "posable once a carrier's sparse posets are large
   enough for the meter to discriminate, and — for any *population*
   comparison against the full record — once its division events are not
   height-pure. The KR height statistic itself is available already."
4. The five `MEASURED-THEN-DECLINED` waivers: change "the KR control the
   catalog requires is empty" to "the height-matched control population
   this unit requires of itself is empty".

### MAJOR-4 — The founding spec's indivisibility clause is undischarged and unregistered, and the aggregate scope statement is missing

Paper 0 §7 attaches five things to U4. Measured against the delivered
unit:

| paper 0 §7 clause | status |
|---|---|
| geometry invariant under renewal-only rebuild | BLOCKED except one row; rebuild not constructible |
| *the division events of a crystal form a crystal* | **discharged** (constructor-inherited) |
| the bridges "are **probed for indivisible structure**" | **not performed** |
| statistical Lorentz invariance of the renewal sublattice | not run (BHS) |
| max-shatter dimension meter as acceptance gauge | not run |

§7 states the refusal ("none of the three objects is a transition kernel,
so no indivisibility reading is available here at all") but **§12
registers no row for it**, and the structural reason is stronger than §7
says. The records are FORCED: `maxhits == 1` is gated per crystal, and
`Builder.pick` takes `hits[0]` from a menu that never exceeds one match.
A record with no branching carries no transition kernel — so the founding
spec's own clause is not merely unrun but **unposable on this arena as
declared**. The scout's S3 independently supplies the supporting datum
("no crystal menu ever BRANCHED at 9 actors").

Second, paper 0 §8 bills Phase III as "the first honest test of 'our
emergence' against 'his relativity'". Nothing relativistic was tested.
The unit is honest cell by cell and never claims otherwise, but it never
makes the aggregate statement, and the aggregate is what a reader of the
verdict pair will take away.

**Exact repairs.**
1. Add **S-U4-8**: "The founding spec's own clause — the bridges 'probed
   for indivisible structure' — is not discharged, and is not merely
   unrun: all five records are FORCED (`maxhits = 1`, no branching), so
   the arena carries no transition kernel and no indivisibility reading
   is definable on it. The scout's S3 records the same fact from the menu
   side. A successor needs a branched carrier or a declared window before
   the clause is posable at all."
2. Add to §10, after the read-out: "Of the five things paper 0 §7
   attaches to U4, this unit discharges one — the crystal claim — blocks
   the geometry at every row a population restriction can confound, and
   refuses three: the indivisibility probe (§7, no transition kernel on a
   forced record), sprinkling-grade Lorentz invariance and the dimension
   meter (§8, both under the pin's own walls). **Phase III's relativity
   test has not been run here**, and nothing in this unit bears on
   relativity."

### MINOR-1 — The control's trivial stabilizer is forced arithmetic, not a measurement against aperiodicity

If `H ≤ Z₃²` is nontrivial then the support of an H-invariant field is a
union of H-cosets, so `|support| ≡ 0 mod |H|`. The control's support is
**1**. Its stabilizer therefore *cannot* be nontrivial, at either
reading. The control shows delivery crystals have too few division events
to carry any spatial structure — a real fact about sparsity — not that
they are aperiodic. The instrument's aperiodicity-detection power is
carried entirely by MUT-APERIODIC-DIVISION, which does its job.

**Repair.** §5, after "the stabilizer is trivial": "— necessarily so: an
H-invariant field's support is a union of H-cosets, so a support of size
1 forbids any nontrivial H. The control's other value is forced by its
single division event, and the instrument's power to detect *aperiodicity*
is demonstrated by the planted-aperiodic mutant rather than by the
control."

### MINOR-2 — "the scout's preliminary is corrected" mis-attributes the corrected sentence

§5 says "the scout's preliminary is corrected" and quotes "stabilizers
AGREE, supports differ (6/9 vs 9/9)". That sentence is from the scout's
**declared-data obligations** paragraph (§(b)), not its PRELIMINARY. The
scout's PRELIMINARY, four lines earlier, already records "CONFLICT-GRID(3,2)
30/6 → ⟨(1,1)⟩ (**footprint constant, order 9**)" — i.e. it already had
the CG32 divergence. The correction lands on the obligations sentence, on
CG34 (where the scout was silent), and on the two support figures (3/9 vs
9/9 on the CONFLICT-GRIDs, not 6/9 vs 9/9).

**Repair.** "The scout of record's declared-data obligations recorded
'supports differ 6/9 vs 9/9; stabilizers agree'; its own PRELIMINARY had
already flagged CONFLICT-GRID(3,2)'s footprint as constant at order 9.
Measured: …" and note that the correction reaches CG34 and both support
figures.

### MINOR-3 — Name the two height-control objects distinctly

Consequential enough to state separately from MAJOR-3's repairs: adopt
"the KR discriminator (the longest chain)" and "the height-matched
control population" as fixed distinct names, in §6.1, §6.2, §8, §12 and
the receipt's waiver text. The verdict string
`BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL` may stand — but §10 must gloss it
once as "the height-matched control population, not the KR discriminator,
which is carried".

### MINOR-4 — §10's read-out omits the constancy behind `Z3^2`

§5 discloses that the CONFLICT-GRID footprint fields are constant; §10's
read-out says only that the footprint reading "enlarges the stabilizer to
the whole group", which reads as *more* structure when it is *less*.

**Repair.** §10: "…enlarges the stabilizer to the whole group at both
CONFLICT-GRIDs — where the field is constant, every actor sitting in
exactly one arbitration footprint per round — and never shrinks it."

### MINOR-5 — Pin R2's plural obligation is met at one row and is not in §11

Pin R2 requires the unit to "gate [the marking] against the source rows"
— plural. Exactly one row reaches this arena. §3 discloses this fully and
supplies two unshared substitutes, but §11 "Deviations, priced" does not
list it.

**Repair.** Add §11 item 7: "Pin R2 asks the marking to be gated against
the source rows; of the three, only the arbitration tag has a referent at
nine actors (§3). The class-0 clause is a two-actor delivery-free notion,
and S4's pair hypothesis is vacuous here — 0 pair arbitrations of 61.
Price: the marking is corpus-anchored at one row. Mitigation: the two
silent rows are discharged by two independent re-derivations that share
no code with the tag — a tag-free shape predicate selecting the identical
set index-for-index, and the renewal-to-root property at 61 of 61."

### MINOR-6 — Receipt label defect: `support_cosets` on the control

The control's `support_cosets` is `[0]` while its support is a single
site, which is not a coset. The paper's prose is correct ("a single site
and no coset union"); the receipt field name is not.

**Repair.** Rename to `support_residues`, or add a gate asserting the
listed residues are *full* cosets (true at the four arbitration crystals:
6 sites = 2 full cosets, 3 sites = 1 full coset; false at the control).

### MINOR-7 — §6.4 "have no such cover" is loose

CONFLICT-GRID(3,2)'s sparse poset has longest chain 2, so it *has*
covers; what it has none of is a cover entering the ω average, since the
average requires `|D| ≥ 2` and its sparse charts are all empty
(`pairs: 0`, `max: 0`).

**Repair.** "…no cover whose chart has two or more directions, so no
value is averaged."

### MINOR-8 — Paper 8's form 2 is neither run nor registered

L-1 §5 records projective compatibility of different finite batteries as
surviving both L-1 and the BHS block and staying "on the table for U4".
The unit's §8 discusses only the fourth form and §12's S-U4-1 registers
only that. Not a breach — the wall is a permission — but the successor
register understates what remains available.

**Repair.** Extend S-U4-1: "Paper 8's admissible form 2 (projective
compatibility of different finite batteries) survives both L-1 and the
BHS block (L-1 §5) and is neither run nor argued here; it remains the one
admissible covariance form available to a successor on this carrier
without a fourth-form argument."

---

## 8. DEVIATIONS, RE-PRICED

1. **The #91-forced constructor substitution — priced correctly, and the
   unit was not merely entitled but obliged.** I verified that the pin's
   cited weld-2 sha `290149118b9d` **matches no committed version of
   paper-13**: the file is `535e288ff412` at commit 58195da (#92) and
   `9cdb10472953` at HEAD (#120). The pin pinned a live worktree state.
   Reading it would have violated #91; refusing it was mandatory. The
   substitute route is strictly older, strictly more anchored (42
   committed-number anchors, 42/42 reproduce), and I independently
   confirmed the closed-form event-count laws the unit uses for the two
   never-swept crystals: `24(R+1)` for DOUBLE-GRID (72, 96, 120 at
   R = 2, 3, 4) and `18R − 6` for CONFLICT-GRID (30, 66, 102, 174 at
   R = 2, 4, 6, 10), fitted to nothing and correct at every committed
   member. **This deviation is a finding about the pin, not the unit**,
   and should be recorded as such at adjudication.
2. **The shared outcome NAME in the head** — priced honestly; the head's
   *data* shares nothing, and the shared input is one pre-registered
   string with nowhere else to come from. Sustained.
3. **The reconstruction shares the arena** — sustained; the records are
   the object, not the instrument, and everything downstream is unshared.
4. **Arm (a)-SUB reported not certified** — sustained, and correct.
5. **The third value BLOCKED** — sustained; the VARIES path is
   demonstrably emittable (MUT-GEOM-VARIES), and the output shows the
   control emitting `VARIES-3->1` and `VARIES-3->2` on the width row in
   the plain run.
6. **Two catalog tests not run** — sustained as to the fact, **re-priced
   as to the ground** for max-shatter (MAJOR-3).
7. *(missing)* — the S4-vacuity / one-of-three-rows deviation, MINOR-5.

---

## 9. THE LICENSED CLAIM

After the repairs above, what U4 may be cited for, at citable scope:

> On the five committed crystals, the division-event count field on Z₃²
> has a nontrivial translation stabilizer at all four arbitration
> crystals under both declared site readings — ⟨(1,1)⟩ at six cells and
> the whole group at the two CONFLICT-GRID footprint cells, where the
> field is constant — and the trivial stabilizer at the delivery control
> under both, where a support of size one forbids anything else. The
> shared invariance direction is the diagonal ⟨(1,1)⟩, and it is
> **inherited from the constructors**, which seed conflict on
> ⟨(1,1)⟩-cosets and group by rows and columns; all eight arbitration
> fields follow in closed form from the seed rule and the loop counts.
>
> The division events of all five records are **height-pure**: they fill
> whole layers of the event poset and share them with nothing, so a
> height-matched control population drawn from unmarked events cannot be
> built at any crystal. Every population-averaged geometry row is
> therefore confounded and none is certified. The chart-width row
> survives, because a maximum over a subset equals the maximum over the
> whole set exactly when it is attained there: it is unmoved at 4 of 4
> arbitration crystals at both depths and moves at the control, and at
> depth 2 the widest charts are centred exclusively on division events
> (3/3, 6/6, 1/1, 3/3) against 0 of 8 at the control.
>
> The renewal-only *rebuild* is not constructible: under the declared
> sub-grammar every crystal halts at its first delivery, while dropping
> only the idle tag rebuilds all five event-for-event. The delivery is
> the sole blocking kinematic tag on this arena.
>
> **Not licensed:** that the periodicity is emergent or dynamical; that
> the control demonstrates aperiodicity-detection; that the renewal-only
> record preserves the geometry, or destroys it — paper 0 §10's third
> falsifier is not evaluable on this arena; that any relativity claim,
> of any grade, was tested; that the bridges were probed for indivisible
> structure — on a forced, unbranched record there is no transition
> kernel to probe.

---

## 10. RECOMPUTATION LEDGER (390)

| block | count |
|---|---|
| sha256 verifications (10 authority/object + 6 v10 sources + 2 paper-13 history) | 18 |
| stabilizers: element set, order, support × 10 cells, brute force | 30 |
| closed-form field derivation from the constructors (8 fields × 9 sites) | 8 |
| event-count laws `24(R+1)`, `18R−6` at 7 committed members | 7 |
| marking rows (marked, structural, renewal-to-root, pair-arbs, total, ckey profiles) | 26 |
| §6.1 height-purity table | 20 |
| §6.2 chart-width table (incl. attainer counts from the output) | 40 |
| §6.3 blocked-row table | 20 |
| §6.4 sparse-record rows | 23 |
| §7 bridge table (link vectors, legs, support cosets) | 30 |
| §6.5 arm-(b) refusals and the idle-free isolation control | 20 |
| I7 evaluation: q₁₁, q₂₂, q₁₂, det, admissible-cell counts | 25 |
| paper↔receipt numeric token sweep (712 occurrences, 72 distinct) | 72 |
| receipt counts block | 10 |
| head / geometry-verdict string identity across paper, output, receipt | 4 |
| verbatim quote checks (L-1 ×2, catalog §1.6, §1.7, paper 0 §7, I7 link set) | 6 |
| banned-sentence scans (paper, source) | 2 |
| scout cross-check (5 preliminary rows + 2 quoted sentences) | 7 |
| waiver backing audit | 22 |
| **total** | **390** |

**False numbers: 0.** Every table reproduces. The verdict pair stands as
computed; all four MAJORs and all eight MINORs are prose, attribution and
register repairs.
