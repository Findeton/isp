# R6b′ — HOSTILE REVIEW, REVIEWER R1 (OPERATOR LENS)

**Object:** the frozen R6b′ delivery — paper `68c20d1fdae4`, code
`8e188dd3ab70`, output `42a39fcaf194`, receipt `50f63b3ba362`.
**Protocol:** `v14/note-r6bp-hostile-protocol.md` (`1cf5fc8b3272`, FROZEN).
**Pin:** `v14/note-r6bprime-transport-pin.md` (`17111fd19022`).
**Lens:** from-scratch reconstruction with different primitives — nothing
imported from the unit; every source re-parsed by my own routes; exact
`int`/`Fraction` arithmetic throughout.

**GRADE: ACCEPT-WITH-FIXES.**  The fixes are blocking, not cosmetic: one
delivered headline and one verdict head must be re-derived.

**Recomputations: 171.**  Two of them (R088, R163) were my own malformed
probes and were re-run correctly as R154/R155 and by direct inspection.
**Divergences against the delivery's printed numbers: ZERO.**  I found no
false number anywhere in the unit.  Every figure the paper prints is
correct *under the unit's own stated definitions*.  All four kills below
are definitional and compositional, not arithmetic.

---

## 0. Hash verification

All six artifacts verified byte-identical at entry and re-verified
unchanged after the run:

| artifact | sha256-12 | entry | exit |
|---|---|---|---|
| paper-09 | `68c20d1fdae4` | ✓ | ✓ |
| code | `8e188dd3ab70` | ✓ | ✓ |
| output | `42a39fcaf194` | ✓ | ✓ |
| receipt | `50f63b3ba362` | ✓ | ✓ |
| protocol | `1cf5fc8b3272` | ✓ | ✓ |
| pin | `17111fd19022` | ✓ | ✓ |

All twelve pinned source artifacts (S1–S6) hash-verified against the pin's
table: `7ac66f3fe74d`, `5f91f0190b4c`, `47f001fad828`, `a955b8484465`,
`5adb205a33d6`, `37a428321f46`, `e431a7c48f76`, `bad952ee5849`,
`038a424a8843`, `dee1cc968268`, `2670a2ea7644`, `dbf027b2fbc9` — **12 of
12 exact.**  CR-B anchor `5ebeec141303` exact.  R6a: consumed bytes
`022c3f488a93` recovered by `git show b0087a9`, terminal receipt on disk
`856f6e810ab5` — both confirmed at their stated provenance (see NOTE-1).

I wrote exactly one repo file: this one.  No git writes.  Repo hashes
unchanged after all work.

---

## 1. Findings, ranked

### MAJOR-1 — The renewal convention is an undeclared choice, and the one taken contradicts S1's own operative definition. (K1)

§3 derives the first-return law for **a visit to state 0**: because
q′(0→0) = 3/4, an idle at the root counts as a completed inter-renewal
leg of length 1, and f(1) = 3/4 carries most of the mass.

Three of the pinned rows name the *event*, not the state:

- **S1's own code.**  `d43b_state_chain_exact.py:368` defines the renewal
  set as `REN = [h for h in FAM if len(h) <= 4 and CLS[tuple(h)] == 0 and
  any(e[0] == 'r' for e in h)]`, and its gate MG6 reads *"ALL clean-slate
  renewal points at len <= 4 (class 0 **carrying an arb**…) — the 144-point
  census"*.  Class 0 is **necessary and not sufficient**; an arbitration
  event is required.
- **S4.**  *"every pair arbitration is a renewal to the root state
  [THEOREM at two-actor delivery-free scope]"* (verified verbatim in
  paper-30).
- **S2.**  Every censused leg terminates in the `'r'` tag — the same token
  d43b tests for.

The unit's reading is the odd one out, and paper-31's own pad-shift
identity (*"idle events never change any menu"*, verified present) is
exactly what makes the two readings differ: an idle at the root is a
self-loop at class 0.

Measured consequences, all exact and all recomputed by taboo iteration to
400 terms plus an independent closed form (R090–R097, R145–R147):

| quantity | delivered (state convention) | S1's own (arb convention) |
|---|---|---|
| return probability | `13/16` | `1/4` |
| defect | `3/16` | `3/4` |
| expected visits | `16/3` | `4/3` |
| f(4) | `3/512` | `9/1024` |
| support holes | `{2}` | `{1, 2}` |
| hole cost over the arena | `50` of `201` | `79` of `201` |

The choice appears in **none** of the five choice inventories.  There is
no `I-RENEWAL` item.  It is genuinely free at the pinned rows — and it is
the single most consequential item in the unit.

**Repair (definite).**  Add `I-RENEWAL-CONVENTION` to the inventory,
classed FORCED-to-the-arb-reading if d43b's `REN` is accepted as S1's
operative definition (I would accept it), otherwise FREE.  Then re-derive
whichever head the adopted convention breaks — see MAJOR-2.

### MAJOR-2 — The two composed heads sit on different conventions; the composite kernel is not the law of any single process. (K1, K4)

The verdict writes `LAW=FIRST-RETURN-…` and
`COLLAPSE=DISTRIBUTION-UNIFORM-AT-COUNT-4` inside **one head**.  They
cannot both hold.

I enumerated the length-4 legs of q′ under each convention directly
(R098–R106):

- **State convention (§3's).**  Exactly **2** first-return paths, interior
  words `(1,1,3)` and `(1,3,3)`; fillers at interior positions 2 and 3
  only.  Induced delivery-free positional law = **(0, 1/2, 1/2)** —
  *not* uniform.  Two pattern classes against three admissible splits: the
  same cardinality mismatch the unit's own negative control uses to fail a
  candidate (§10).
- **Arb convention (S1's/S2's).**  Exactly **3** paths, interior words
  `(0,1,3)`, `(1,1,3)`, `(1,3,3)`; fillers at positions 1, 2, 3.  Induced
  law = **(1/3, 1/3, 1/3)**, which **reproduces S2's delivery-free census
  exactly**, from S1's chain alone (R103/R104/R140).

So §6's uniform law is the *arb* law, and §3's kernel is the *state*
kernel.  If §3's convention is taken as binding, the following delivered
numbers all move (R148–R153):

- maximisers at delivery-free scope: `3` → `2`;
- TV against S5's binomial: `2/21` → `2/7` (and the CR-B cross-unit
  reproduction is lost);
- the G-DIAG2 product law's support: `19683` → `2^9 = 512`, so
  *"raw and admissible-at-images sizes coincide"* fails;
- max-det ratified at probability `1/3` → `0`;
- `I-ORIENT` loses its stabilizer classification, because (0, 1/2, 1/2) is
  **not** reversal-invariant (R106) — the "first stabilizer-fixed items in
  this line" claim drops from `2` to `1`.

**Repair (definite).**  Declare one convention in §2, gate it, and
recompute exactly one head.  Adopting the arb convention (my
recommendation, on d43b's authority) leaves §4/§6 **completely intact**
and requires re-deriving only `R6BP-KERNEL-DEFECTIVE`'s arithmetic; its
qualitative content (terminates almost surely, delivery-free) survives and
in fact strengthens.

### MAJOR-3 — THE SCOPE VERDICT: count-4-only is an artifact of the chosen route. It is neither a law nor a census cap. (K2 — decisive)

§6 labels the 65 count-≥5 intervals **"uncensused by S2"**, which implies a
deeper census would extend the collapse.  It would not.

Measured from S1's chain alone, exhaustively at n = 3…12 (R112–R120): a
delivery-free leg of length n has exactly **two advancing steps** (0→1 and
1→3) among its n−1 interior steps, hence exactly **n−3 fillers** and
**C(n−1, 2) equiprobable configurations**.  So:

| leg length | configurations | fillers | splits available | position map single-valued? |
|---|---|---|---|---|
| 3 | 1 | 0 | 2 | no (stratum empty) |
| **4** | **3** | **1** | **3** | **yes** |
| 5 | 6 | 2 | 4 | no |
| 6 | 10 | 3 | 5 | no |

The unit's "pattern class determines a distinguished interior position"
reading is single-valued **only at n = 4**, where n−3 = 1.  A census at
length 5 would return 6 classes against 4 splits.  The census is not the
blocker.

**What IS derivable at count 5 (and every count) from the pinned rows
alone** — this is the part the unit misses, and it cuts in its favour:

1. **The leg-length law, at every n.**  f(5) = `27/4096` (state
   convention) or g(5) = `27/2048` (arb convention), exact (R134/R135).
2. **The full configuration law, at every n.**  Uniform on the C(n−1,2)
   filler configurations, from S1 alone, delivery-free, no S2 (R120).
3. **The position marginal — uniform on n−1 positions at EVERY n ≥ 4**,
   verified exactly for n = 4…12 (R129).  The two advancing steps are
   uniformly placed among the n−1 interior steps, so every position is
   symmetric.  At n = 4 it **reproduces the delivered law exactly**
   (R130).  Adopting it would raise coverage from **37 of 201 to 102 of
   201** — 102 of the 122 non-trivial-fiber intervals (R136–R138).

**What actually blocks count 5** is a free item the unit never measures:
at n ≥ 5 a leg carries ≥ 2 fillers, so reducing the filler *set* to a
*position* is a choice, and the choices differ measurably.  At n = 5 the
marginal gives `(1/4, 1/4, 1/4, 1/4)` while first-filler gives
`(1/2, 1/3, 1/6, 0)` (R123/R124/R131).  At n = 4 the two coincide, because
there is nothing to choose (R133) — which is precisely why the delivered
result looks convention-free and is not.

**Repair (definite).**  (a) Replace the "uncensused by S2" label with the
measured statement (`n−3` fillers; the map is single-valued only at
n = 4).  (b) Add `I-FILLER-REDUCTION` to the inventory.  (c) Report the
marginal law and its 102/201 coverage as a measured segment — it
strengthens `KERNEL-DERIVED` and is honest either way.  (d) Correct §12:
the registered u1c/depth-15 lead extends the *chain position*, and would
not relieve the count-≥5 gap at all.  The paper does not claim it would,
but §6's table invites the inference.

### MAJOR-4 — THE SEAM RULING: `BLOCKED-AT-THE-SCOPE-SEAM` is not earned. The seam is an artifact of the route, not of the pin. (K3)

The seam exists only because the unit sources the **length** layer from S1
(delivery-free) and the **positional** layer from S2 (transport).  But S1
supplies the positional layer too, and at its own scope: S1 alone
reproduces S2's delivery-free count-4 census exactly (R140).  S2 is a
**cross-check** for the delivery-free positional layer, not its only
source.

K3's posed test — *do S1-scope objects exist at transport scope in the
pinned rows?* — answers **NO** (no transport-scope transfer is pinned; S1
declares the class structure not stable across the change; R142).  But
that is the wrong direction.  The right direction is: *do S2-scope objects
exist at S1's scope?*  **YES** — the entire delivery-free positional law
(R140/R141).

**A single-scope row set therefore already exists inside the pin:
S1 + S4 + I7, all delivery-free** (R143).  It supplies everything §3 and
§6 need.  What S2 uniquely adds is the transport-scope *position
dependence* (TV = `2/63`) — a statement **about** transport scope, not an
obstruction to the delivery-free construction (R144).

**Consequence for Γ-main's pin (the protocol asks).**  Γ-prep does not
need to dissolve this seam, because the seam was never load-bearing for
the delivery-free positional layer.  Γ-main should pin the **delivery-free
single-scope set** and treat the transport-scope arm as a separate,
declared question.  The `2/63` measurement is real and should be carried —
as a transport-scope finding, not as a blocker.

**Repair (definite).**  Re-derive the positional layer from S1 (one
enumeration; I ran it), keep S2 as the declared cross-check, and re-grade
the fourth head to something like
`R6BP-SEAM-AVOIDABLE-AT-DELIVERY-FREE-SCOPE<POSITIONAL-LAYER-DERIVABLE-FROM-S1-ALONE|S2-AGREES-AT-COUNT-4|TRANSPORT-POSITION-DEPENDENCE-TV=2/63-CARRIED>`.

### MODERATE-1 — "the declared readout is det-blind" is false as stated. (K4)

`I = q⁻¹ (det q)^w` at `w = 0` gives `I = q⁻¹ = adj(q)/det(q)`.  Measured
on the pinned count-4 interval (R156–R159): the balanced half reads
`I = [[1,0],[0,1]]`, the unbalanced half `I = [[4/3,2/3],[2/3,4/3]]` —
differing by exactly the `1/det` factor `4/3`.  The readout is **inversely
det-weighted**, not det-blind.

What is true: at `w = 0` the readout carries no *explicit* det weighting,
so nothing in the declaration asks for det to be extremised.

Not load-bearing — leg (a) of the extremal kill (4 functionals, 3
selections) is independent and stands, and I reproduced it in full (R077–
R087: max-det → middle, max-balance → middle, max-left-count → last,
max-|q₁₂| → ties on the two ends).  But the verdict head asserts
`READOUT-DET-BLIND-AT-W-0=TRUE` as a first-class segment.

**Repair.**  Change the segment to
`READOUT-CARRIES-NO-EXPLICIT-DET-WEIGHT-AT-W-0` and reword §8's second
paragraph.

### MODERATE-2 — the D12 kill is an extension of the standard, applied without saying so. (K4)

D12's bar, quoted correctly by the paper, is a test on **one** selector Q:
*premises + Q must have exactly one physical equivalence class of models*
(verified verbatim in d12 §1, R170).  Max-det **passes** that clause — it
selects uniquely, and the unit says so.  The unit's kill is that the
*choice of Q* is unforced, which is D12's second clause ("selects one
member of a preselected toy family", verified present, R171) generalised
from families of models to families of selectors.

I sustain `DIES-AT-THE-BAR` — the generalisation is sound, and the third
leg (0 of 6 rows declare a variational principle; the derived law ratifies
at 1/3) is independent.  But the paper presents non-uniqueness across
functionals as "D12's own structure" without flagging the extension.

**Repair.**  One sentence naming it as an extension of D12's second clause.

### MINOR-1 — §6 understates its own strength against CR-B.

CR-B refuted `THE-UNIFORM-LAW-ON-THE-ADMISSIBLE-FIBER` for **two**
reasons: support-dependence *and* non-factorisation at 4 of 6 records.
The paper cites only the first ("for want of a declared support").  But
CR-B itself measured `sites_not_factorising = 0` at G-DIAG2 (R073) — the
second leg is inapplicable exactly where the unit lands.  Say so; it is a
free strengthening.

### MINOR-2 — the `THE-LIFT-PAIR` table cell reads as self-contradictory.

"**unchanged**, and the freedom grows" — the *class* is unchanged (iii)
while the *fiber* goes 2 → 3.  Split the cell into class and fiber columns.

### MINOR-3 — the verbatim anchors are verbatim-modulo-markdown.

Four quoted contexts differ from source only by stripped emphasis: S1's
`did *not* need`, S4's `**rooted**`, S3's `**The bridges**`, S6's
backticked `` `Q` ``.  S1's transport caveat additionally drops a trailing
"(§7, successor 2)" without an ellipsis.  All substantively faithful — I
re-located every one under whitespace-and-emphasis normalisation and
confirmed it in the *pinned* row (including S2's *"Transport scope
(d42b1) only"*, which is genuinely at u1b §10, **not** borrowed from the
unpinned u1 note; I checked that specifically).  But an emphasis-only
drift in a source would not trip the anchor.  Flagged for the instrument
reviewer under K5(a).

### NOTE-1 — the R6a provenance handling is clean; I would adopt it as the standard.

I diffed the #26 committed bytes (`git show b0087a9`, hash `022c3f488a93`
confirmed) against the terminal receipt (`856f6e810ab5`).  Of 140 paths in
the consumed classes, **every** `/record_family/*` and `/split_fibers/*`
path is byte-identical across the two.  The only divergence is
`/extremal_selectors/*` — **absent from #26 entirely**, therefore
provably unreadable by this unit.  The unit's §8 extremal work is its own
construction, independently confirmed.  Committed-bytes-via-git-show with
disclosed drift and a path-value stability gate is a sound standard for
concurrent-unit reads.

### NOTE-2 — a same-name, opposite-sense selector across two units.

R6a's terminal receipt carries `min_abs_q12`; this unit uses
`max-|q12|`.  Not a drift (the R6a block did not exist in the consumed
bytes), but the two units now carry same-named selectors in opposite
senses.  Add a cross-reference so a later reader does not conflate them.

### NOTE-3 — what survives every kill above.

- `R6BP-TRANSPORT-UNMOTIVATED` is **robust**.  I recounted all five choice
  inventories item by item from the source item lists and reproduced
  `C1: 3/1/3`, `C2: 1/0/5`, `C3: 2/0/1`, `C4: 1/0/3`, `C5: 0/1/1` exactly
  (R167), and even reclassing C1's `I-ORIENT` to free leaves 0 motivated
  (R169).  The C1 type-error claim is correct: a leg carries exactly one
  division event (the `'r'` tag), so C1 equates a division-event count
  with a grammar-event count.  The bridges reading does land on the 29
  count-1 intervals, all with fiber 0.
- The **arena census reproduces exactly** from I7's declarations with no
  reference to the unit: admissibility rebuilt from the readout rejects
  exactly G-INDEF (det = −3) and G-SINGULAR (det = 0), one in each failure
  mode; 7 × 9 × 3 + 2 × 2 × 3 = **201**; the class breakdown is
  **29 / 50 / 20 / 37 / 65**; 122 non-trivial; **647** = Σ(n−1) over the
  201; **67** = the (record, site) pairs (R054–R067).
- **G-DIAG2's complete coverage is genuinely unique** — I searched the
  whole family and it is the only record with every splittable interval at
  count 4 and every other at fiber 1 (R068); 3⁹ = 19683; raw =
  admissible-at-images there and *not* at G-OFFDIAG, so the coincidence
  discriminates (R069–R072).
- **8 of 9 raw split fibers rebuilt** from count data alone, agreeing with
  R6a; G-CURVOFF is correctly the one not determined by the printed sites
  (R074/R075).
- **CR-B's 2 → 0 and the 2/21 cross-unit reproduction both confirmed**
  (R048–R051) — CR-B's own anchored `tv_uniform_vs_binomial["4"] = "2/21"`,
  computed on a different route.
- The **two-route independence claim is real**: I parsed paper-31's fenced
  prose block and d43b's `T_REF` dict by two different regex routes and
  they agree on all 36 entries (R001–R003).  I *solved* for the harmonic
  vector rather than reading it, recovering `(4,4,3,7,3,3)/3` (R005), and
  verified the h-transform is invariant under `f → cf`, so the harmonic
  scale is **not** an undeclared choice (R010).
- The **400-term tail bound holds**: exact residual `1.181e−49 < 1e−40`
  (R026/R027).  The closed form matches the taboo iteration termwise at all
  400 terms (R024).
- **Paper ↔ output verdict block: 7 of 7 segments byte-identical** (R161).
- **Named exclusions honoured**: u1c appears only as a registered lead with
  its status printed; d70 and THE-THEORY-SO-FAR appear only inside the
  exclusion list the gate needs (R162, and by inspection of
  `r6bp_transport_exact.py:279–281`).

---

## 2. K1–K5 adjudications

**K1 — THE DERIVED KERNEL: FAILS ON PURITY.**  The arithmetic is
impeccable and independently reproduced (two routes, 400-term tail,
scale-invariance of the h-transform, closed classes, hitting
probabilities, 13/16, 3/16, 16/3, 21/13, the hole at 2 — all exact).  But
the kernel imports one undeclared choice, and it is the decisive one: the
**first-return definition**.  The unit reads "renewal = visit to state 0";
S1's own code, S4's theorem and S2's leg delimiter all read "renewal =
arbitration".  State ordering is clean (pinned by both S1 artifacts, and
the renewal state's identity is declared, not chosen).  The completed-chain
convention is clean (pinned formula, and provably scale-invariant).  The
first-return definition is not.  **MAJOR-1, MAJOR-2.**

**K2 — THE SCOPE QUESTION: ARTIFACT, of the route — not a law, and not
S2's censused lengths.**  Count-4-only holds because the unit reads
positions off S2's *pattern classes*, and a leg of length n carries n−3
fillers, so the class→position map is single-valued only at n = 4.  A
deeper S2 census does not extend it.  **Derivable at count 5 from the
pinned rows alone:** the leg-length law at every n (g(5) = 27/2048); the
uniform law on the C(n−1,2) filler configurations at every n; and the
position marginal, **exactly uniform on n−1 positions at every n ≥ 4**,
which coincides with the delivered law at n = 4 and would carry coverage to
102 of 201.  **What blocks:** not the census — the reduction of a filler
*set* to a *position* at n ≥ 5, which is an unmeasured free choice whose
alternatives differ (marginal `(1/4,1/4,1/4,1/4)` vs first-filler
`(1/2,1/3,1/6,0)`).  **MAJOR-3.**

**K3 — THE SEAM: NOT NON-INNOCUOUS; AVOIDABLE.**  A single-scope row set
could have been pinned, and in fact already is inside the pin: S1 + S4 +
I7, all delivery-free, supply both layers.  S1 alone reproduces S2's
delivery-free positional census.  The seam is a property of the unit's
sourcing decision, not of the pinned corpus.  Γ-prep need not dissolve it;
Γ-main should pin the delivery-free single-scope set and carry the
transport arm (TV = 2/63) as a separate declared question.
`BLOCKED-AT-THE-SCOPE-SEAM` should be re-graded.  **MAJOR-4.**

**K4 — THE COMPOSED HEADS: two of four are not mutually consistent.**  The
heads are individually well-formed and every scope qualifier is present and
correct, but `KERNEL-DERIVED` and `KERNEL-DEFECTIVE` rest on incompatible
renewal conventions (MAJOR-2).  The re-classifications: THE-SPLIT →
(ii)-in-distribution is sustained *at the arb convention only*;
NEW-FRONT-VALUES → fiber 1 forced-relative-to-the-split is sustained and
correctly qualified (the front is forced only once the split is fixed —
the paper says so); the lift third-rule claim is sustained but the table
cell wording is contradictory (MINOR-2); FREE-TRANSVERSE-LINKS unchanged is
sustained, and its reason ("no index at all for a link that lies on no
interval") is structurally correct.  The extremal bar: 4 functionals → 3
distinct selections **fully reproduced** by my own construction; the
det-blind leg is overstated (MODERATE-1); non-uniqueness across functionals
is a defensible **extension** of the D12 standard rather than the standard
itself (MODERATE-2), and DIES-AT-THE-BAR stands.

**K5 — AT MY DEPTH: the four verdict heads rebuild byte-for-byte from my
own censuses, with ZERO numerical divergence.**  Every segment of all seven
verdict lines was independently recomputed: IDENT/LAW/COLLAPSE/COVERAGE=37-
OF-201/CRB-SIMPLEX-2-TO-0/SCOPE; CANDIDATES=5/MOTIVATED=0/FREE-ITEMS
3+5+1+3+1/TV=2/63/TV-DF=0/BRIDGES-29-OF-201; RETURN=13/16/DEFECT=3/16/
CLOSED-CLASS={2,4,5}/VISITS=16/3/HOLE-COSTS-50-OF-201; LEG1=3/7/LEG2=1/3;
FUNCTIONALS=4/DISTINCT=3/RATIFIES-AT-1/3; COVER 0-of-6 twice; CONTROLS.
Paper block == emitted block, 7 of 7.  **The divergence is not in any
number — it is in the convention under which two heads are simultaneously
assertable.**  I record that explicitly so the adjudicator does not read
this review as a false-number finding: the corpus's zero-false-numbers
record is not broken by this unit.

---

## 3. Blocking fix list

1. Declare the renewal convention in §2 and gate it.  Adopt the
   arbitration reading on d43b's authority.
2. Re-derive `R6BP-KERNEL-DEFECTIVE`: return `1/4`, defect `3/4`, visits
   `4/3`, holes `{1,2}`, cost `79 of 201`.  §4/§6 need no change under this
   adoption.
3. Add `I-RENEWAL-CONVENTION` and `I-FILLER-REDUCTION` to the choice
   inventory.  (`0 of 5 motivated` is unaffected — verified.)
4. Replace §6's "uncensused by S2" label with the measured `n−3` filler
   statement; add the marginal law and its 102/201 coverage as a segment.
5. Re-grade the fourth head from `BLOCKED-AT-THE-SCOPE-SEAM` to a
   seam-avoidable head, carrying `2/63` as a transport-scope finding.
6. `READOUT-DET-BLIND-AT-W-0` → `READOUT-CARRIES-NO-EXPLICIT-DET-WEIGHT-AT-W-0`.
7. Name the D12 extension in §8; add the CR-B factorisation strengthening
   in §6; split the `THE-LIFT-PAIR` cell.

---

*R1 (operator lens), frozen as delivered.  171 recomputations, 0 divergences
against printed numbers, 4 MAJOR / 2 MODERATE / 3 MINOR / 3 NOTE.
Disagreements are the adjudicator's.*
