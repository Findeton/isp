# R6a — HOSTILE REVIEW, OPERATOR LENS

**Reviewer:** R1 (operator).  **Object:** the frozen R6a delivery — paper
`af5b7f26e427`, code `ea914c6b55aa`, output `a04b97d2b7bc`, receipt
`022c3f488a93` (commit b0087a9).  **Protocol:**
`v14/note-r6a-hostile-protocol.md` (`02d249f22f6f`), K1–K5 binding.  **Pin:**
`v14/note-r6a-refinement-grammar-pin.md` (`a22582f67168`).  **Grammar sources
traced to origin:** `v13/code/ha_successor_receipt.json` (`542b8735daf0`),
`v13/paper-ha-successor.md` (`f286ba10d2d9`), `v13/code/ha_successor_exact.py`
(`d44cb72f8ee9`); founding pin `v14/note-r0-founding-pin.md` (`e9d2bedff244`)
+ the LOG #4 erratum.  **All nine hashes verified before and after this run —
unchanged.**  R3's files (`v14/paper-03-*`, `v14/code/r3_*`) were never opened.

**Method (operator lens).**  A from-scratch instrument
(`scratchpad/r6aop/op1…op7.py`): sites are **integer mixed-radix codes**, not
tuples; counts a **flat list** indexed `site·|L| + link`; the readout built by
the **closed form** `q_ii = n_i`, `q_ij = (n_ij − n_i − n_j)/2` with
determinants by **cofactor expansion** — no Gaussian elimination anywhere,
where the unit solves a linear system; interval decomposition by **BFS over
integer vectors by length**, where the unit recurses with orthant pruning;
orbits by **union–find**, ranks by my own elimination.  Nothing imported from
the unit; the unit's code was never executed.  The arena, the record family,
the lapse family, the drag-rule family and the dynamics were rebuilt from the
pinned declarations read by JSON path and from the HA paper's own tables.

**Recomputations: 177** (op1 51 · op2 30 · op3 22 · op4 33 · op5 19 · op6 12 ·
op7 10).  These cover **all 15 rendered prose claims, all 12 verdict segments,
every table entry of the paper**, and six measurements the unit does not have
(the fiber closed form, the coboundary rank arithmetic, the per-rule
image-agreement solution, the mode-consistent comparator, the zero-sector
characterisation, the reflection-extended stabiliser).

**Headline standing.** *Every delivered number is correct.*  27/27, 21·3·3·0,
0/6, 972/972, 324/324, 36/28, 19683 … 1257565061957837936381, equivariant min
3, 361/261/1 with (2,2,2), 54/108 with 64 witnesses, 7112/11088 with 3976,
the four-class support table, 49896/49896, 30/81, 0/207, ceiling 2 attained,
54/108→108/432→216/1728, 27/216, and all nine per-record cycle sums reproduce
**exactly** on an independent instrument.  The verdict string rebuilds
**byte-for-byte** from my own censuses.  One prose enumeration is
under-inclusive (F6); nothing else numerical moves.

What fails is not arithmetic.  It is (F1) a **false counterfactual in the
paper's central mechanism paragraph** — a granted potential does *not* fix the
split — and (F2) an **unqualified overclaim carrying a verdict segment**: the
"dynamics-forced" front lift is rule-relative, and under two of the eleven
declared drag rules the forced value is integral and is itself a declared
lift.

**Grade: ACCEPT-WITH-FIXES.**

---

## 1. K1 — THE COBOUNDARY THEOREM

### 1.1 The statement and its proof: CORRECT, and universal over the grammar

The proof is sound at pinned scope and needs nothing from the declared family:
a coboundary sums to zero around every cycle; an axis cycle of a strictly
positive record sums to at least `L`.  Measured min axis cycle sums, all nine
admissible records: `G-ANISO 3, G-ANISO2 12, G-CURVED 6, G-CURVOFF 9,
G-DIAG2 6, G-FLAT 3, G-OFFDIAG 6, G-OFFDIAG2 9, G-OFFNEG 9` — reproduced
exactly, smallest 3.

**Universality answered (protocol's first K1 question).**  I characterise the
coboundaries exactly, by rank arithmetic on my own instrument:

> **R6a-OP-1 (characterisation).**  On `X = (Z_L)^d` with the declared link
> set, an edge assignment `n` is a coboundary `δφ` **iff** (a) every axis
> cycle sums to 0 **and** (b) the triangle relations hold:
> `n_{e_i+e_j}(x) = n_{e_i}(x) + n_{e_j}(x+e_i) = n_{e_j}(x) + n_{e_i}(x+e_j)`.

Measured at the pinned arena: `|V| = 9`, `|E| = 27`; `rank δ = 8 = |V| − 1`;
cycle rank `|E| − |V| + 1 = 19`; the (a)+(b) system has rank exactly **19**, so
its solution space has dimension `27 − 19 = 8 = rank δ` — the conditions are
not merely necessary, they cut out the coboundaries precisely (integrality
follows by path-summing).  Condition (a) alone forbids positivity, for **any**
`L ≥ 1`, **any** `d`, **any** record — so the theorem is about the GRAMMAR,
not the declared family.  **No admissible record within I7's grammar can carry
coboundary counts; none exists to construct.**  Over the pinned count box the
count of coboundary-admissible vectors is 0 of 361.

**A sharpening the unit should own.**  Measured: condition (b) holds on
exactly the records whose off-diagonal metric component vanishes — `G-ANISO,
G-ANISO2, G-CURVED, G-DIAG2, G-FLAT` (all `q₁₂ ≡ 0`), and fails on exactly
`G-CURVOFF, G-OFFDIAG, G-OFFDIAG2, G-OFFNEG` (`q₁₂ ∈ {1, 2, −2}`).  So *the
cocycle half of "coboundary" IS the vanishing of `q₁₂`*, and for five of the
nine admissible records the **only** obstruction is the periodic
identification: `G-FLAT`'s counts are exactly `δφ` with `φ(x) = x₁ + x₂` on
the universal cover `Z²` (verified at all 27 (site, link) slots).  The freedom
does not come from the record being "far from" a coboundary; it comes from one
integer of holonomy per axis cycle.  One sentence in §2 would carry this.

### 1.2 Is it the MECHANISM? — NO.  Measured, and this is F1

§2 says: *"If the counts were `n_ℓ(x) = φ(x+ℓ) − φ(x)`, the split of an
interval at its interior site would be read off `φ` and there would be no
freedom to measure."*  **This is false**, and the falsity is measurable.

`φ` is a function on the **coarse** sites.  The interior site `y` is not a
coarse site, so `φ(y)` does not exist.  Grant the counterfactual its strongest
form — a **refinement-compatible** potential `φ^r` on the refined lattice with
`n^r = δφ^r` — and the split at each coarse interval is
`n₁ = φ^r(mid) − φ^r(2x)`: **one free integer per interior site, exactly
`n_ℓ − 1` values**.  Measured on `G-ANISO2`: the split fiber under a granted
potential is `13 631 146 639 813 244 878 848`, **identical to the measured raw
fiber with no potential**.  A potential does not shrink the split fiber by a
single element.

What a potential *does* collapse is a different entry of the inventory:
with `φ^r` given, **all 108 refined link counts are determined** (measured),
so `FREE-TRANSVERSE-LINKS` falls from INFINITE to **1**.  And the front
freedom is genuinely foreclosed by the theorem, because the natural
front-native rule (§2.2 below) has the coboundary relation as its own
consistency condition.

> **Adjudication.**  The coboundary theorem is the mechanism of the
> **FREE-TRANSVERSE-LINKS** and **NEW-FRONT-VALUES** freedoms.  With respect
> to **THE-SPLIT** — the headline freedom, the one in the verdict head — it is
> **parallel**: the fiber count is `Π_x #{(a,b,c) admissible}` and is logically
> independent of whether the counts are a coboundary.  §2's "This is the
> mechanism of everything that follows" and §11 open 2's "A grammar in which
> they are [a coboundary] … would force the split" are both wrong.

**Exact repair.**  Replace §2's counterfactual with:

> A potential on the *refined* lattice would determine every transverse link
> and so remove the completion freedom entirely; it would still leave the
> split one free integer per interior site — `φ^r(mid)` is a datum of the
> refinement, not of the record.  What the theorem forecloses is the
> front/count relation: the counts cannot be front differences, so the front
> cannot supply the splitting datum either.

and in §11 open 2 replace "would force the split" with "would force the
transverse links and the front lift; the split would still be declared".

### 1.3 A closed form the unit does not carry

The split fiber has an exact closed form, verified against the unit's triple
loop on all nine records:

> `fiber(record) = Π_x T(n_{e1}(x), n_{e2}(x), n_{diag}(x))`,
> `T(A,B,C) = Σ_{a<A} Σ_{b<B} #{ c ∈ [1, C−1] : (√a−√b)² < c < (√a+√b)² }`.

Both endpoints verified from the closed form alone: `T(2,2,4) = 3`, `3⁹ =
19 683`; `T(4,9,13) = 221`, `221⁹ = 1 257 565 061 957 837 936 381`.  The span
is therefore `3⁹ … 221⁹` and its shape is `T⁹` — a homogeneity statement worth
one line in §5.1.

---

## 2. K2 — THE CLASSIFICATION HUNT (every candidate, with its measured result)

The hunt was run at the exhaustiveness the protocol demands.  **Nine
candidate fixing structures tested; two reduce a fiber to 1; neither is
derivable from the pinned sources; the verdict does not flip.**

| # | candidate structure | measured result | fixes the freedom? |
|---|---|---|---|
| 1 | declared chart group (18 elts), raw equivariance | fibers `G-ANISO2 288, G-CURVOFF 29 393 280, G-DIAG2 3, G-OFFDIAG 5, G-OFFDIAG2 88, G-OFFNEG 24`; min **3** | no (reproduces the unit) |
| 2 | chart equivariance **∧ admissibility** (strengthening the unit's test) | `221, 2 394 000, 3, 3, 54, 23`; min **3** | no — the unit's class-(ii) verdict is robust to the strengthening |
| 3 | **lattice reflection** `x ↦ −x` (interval reversal), group order 36 | fiber **1** on `G-DIAG2`, **1** on `G-OFFDIAG`; **0** on `G-ANISO2`, `G-OFFDIAG2`, `G-OFFNEG`; unchanged on `G-CURVOFF` (no reflection in its stabiliser) | **fixes 2, forbids 3** — see below |
| 4 | extremal: **max det q** at the refined image site | unique at **9 of 9 sites of all 6 splittable records**, and the resulting refinement is **globally admissible** in all 6 | **fiber 1** — but no extremal principle is declared |
| 5 | extremal: most-balanced (min `Σ|2n₁−n|`) | unique at 0/9 sites on `G-ANISO2`, `G-OFFDIAG2`, `G-OFFNEG`; 4/9 on `G-CURVOFF` | no |
| 6 | extremal: min `|q₁₂|` at the image | unique at 0/9 on three records, 1/9 on `G-CURVOFF` | no |
| 7 | a **declared front lift** used in reverse to fix the split | left lift ⇒ `n₁ = 0`; right lift ⇒ `n₁ = n`; both outside `1 ≤ n₁ < n` | no — both forced splits are inadmissible |
| 8 | **the dynamics** (a split annihilating the defect) | under the left lift `D(ι(x)) = w^c[N,n](x)`, which contains no split variable; and the coarse drag vanishes identically at only 3976 of 11088 cells | no — impossible in closed form |
| 9 | `FREE-TRANSVERSE-LINKS`: **d-dimensional consistency** | free fraction **grows** with d: 54 of 108 (50%) at d = 2, **972 of 1296 (75%)** at d = 3 | no — d-consistency loosens, it does not restrict |

**Candidate 3 (the reflection) is the consequential one.**  `x ↦ −x` is a
symmetry of the pinned *interval* structure — it maps `[x, x+ℓ]` to
`[−x−ℓ, −x]` with the same link label — and it is **not** in `[P-I7-CHART]`
(translations and direction relabellings only).  Because it reverses the
interval, an equivariant split must satisfy `(n₁,n₂) ↦ (n₂,n₁)`, i.e. `n₁ =
n₂` on reflection-linked orbits.  Measured consequence: on the even-count
records the split becomes **forced to balanced (fiber 1)**; on the odd-count
records **no equivariant split exists at all (fiber 0)** — the move would be
*refused*, not motivated.  So a reflection declaration does not convert
class (iii) into class (ii): it splits the family into forced and forbidden.
Using it is forbidden by pin §1 (outside the pinned sources), so the unit is
right to exclude it — but this is the sharpest available statement of what a
further declaration buys, and it belongs in §11.

**Candidate 4 (max-det) is the one the inventory should have tested.**  Pin §3
and protocol K2 both name extremal/variational selections; the delivered
inventory has no such row.  Measured, a max-det selector is *unique at every
site of every splittable record* and yields an admissible refinement — so the
paper's "— nothing in the pinned grammar —" is exactly right as written
("nothing *in the pinned grammar*") but reads stronger than it is.  The honest
form is: *no pinned declaration selects a split; a variational selector would,
and none is declared* (F3).

**`NEW-FRONT-VALUES`, the front's own semantics** (the protocol's "committed
events at a site that already existed unlabelled?").  The natural candidate is
`F(mid) = n(x) + n₁` — integral, front-native, and *not* derivable: the front
and the interval counts are independent configuration variables (the pinned
`T-FROZEN-GEOMETRY` sentence says `H_a[N]` moves only the front), and the
candidate's own consistency principle, `n(x+ℓ) − n(x) = n_ℓ(x)`, **is** the
coboundary relation §2's theorem kills.  Measured against the image-agreement
condition it fails under every count-scaled rule (`0 of 378` cells) and holds
only accidentally under the count-blind rules (`9 of 378`).  Measured against
the declared fronts directly: `692 of 729` (front, record, interval) cells
violate the front-as-potential relation.  So this candidate is genuinely dead,
and the theorem is what kills it — which is where §2's mechanism claim *is*
earned.

---

## 3. K3 — WHAT FORCES THE COUNT-WEIGHTED INTERPOLATION (F2)

The protocol asks for a derivation or the lift class.  Here is the derivation,
and it does not support the paper's sentence.

At a coarse image `z₀ = ι(x) = 2x` both lifts agree, `N^r(z₀) = N(x)`,
`F(z₀) = n(x)`.  Write `u_j = F(mid_j) − n(x)` and `v_j = n(x+e_j) − n(x)`.
Requiring `w^r(z₀) = w^c(x)` gives, for architecture A,
`Λ^r(z₀) u = Λ^c(x) v`, i.e. **`u = Λ^r(z₀)^{-1} Λ^c(x) v`** — the forced lift
is a **function of the drag rule**.  Solved exactly on all 14 censused builds
× 3 fronts × 9 image sites (378 cells per rule):

| rule | what the image-agreement condition forces | Z-valued? |
|---|---|---|
| `A-axis`, `B-axis` | `u_j = (n₁/n) v_j` — **the count-weighted interpolation** | no |
| `B-all` | **underdetermined**: 3 unknowns, 2 equations (a one-parameter family containing the count-weighted solution) | n/a |
| `A-chart`, `B-chart` | `u = v` — **the declared RIGHT lift** | **yes, 378 of 378** |
| `A-insert`, `A-insert-x`, `A-insert-2x`, `A-notransport`, `A-linkframe`, `A-linkhalf` | `u = q^r (q^c)^{-1} v` (or the link-frame analogue) — a **third** value, neither count-weighted nor the right lift | no |

(On a diagonal record such as `G-ANISO2` alone, `A-insert` coincides with
`A-axis` because `q = diag(n₁,n₂)` there; over all 14 builds it separates.
That coincidence is why a single-record probe would report the paper's
statement as true.)

> **Adjudication.**  §6.1's "Requiring the drag to agree at the coarse image
> sites forces the front lift to the count-weighted interpolation" is
> **rule-relative and unqualified in the paper**.  The display line **"The
> dynamics does not rescue the free front value; it forces an inadmissible
> one"** is false for `A-chart` and `B-chart`, where the forced value is
> integral, admissible, and is one of the two declared lifts.  §11 open 3's
> "The count-weighted interpolation is the unique dynamics-compatible front
> lift" is false as stated.

**The conclusion survives; the sentence does not.**  Under every declared rule
`NEW-FRONT-VALUES` stays class (iii): where the forced value is integral it is
one of the two declared lifts (fiber 2, already class (iii) as
`THE-LIFT-PAIR`), and where it is not integral it leaves the declared type.
The honest statement is stronger than the delivered one because it is
rule-complete:

> **Exact repair (§6.1, and the verdict segment).**  "Requiring the drag to
> agree at the coarse image sites forces a front lift, and *which* lift is a
> function of the drag rule: the count-scaled rules (`A-axis`, `B-axis`, and
> `B-all` up to one free direction) force the count-weighted interpolation,
> non-integral at 30 of 81 cells; the count-blind rules (`A-chart`,
> `B-chart`) force the declared right lift, which is Z-valued; the
> metric-inserted and link-frame rules force a third value, also non-integral.
> The dynamics therefore never *removes* the freedom: it either re-selects a
> lift already inside the class-(iii) pair or leaves the declared type."

The verdict segment `NEW-FRONTS=…DYNAMICS-FORCED-NON-INTEGRAL-30-OF-81`
should carry the rule scope, e.g. `…NON-INTEGRAL-30-OF-81-AT-COUNT-SCALED-
RULES-6-OF-11-RULES-NON-INTEGRAL-2-OF-11-FORCE-THE-RIGHT-LIFT`.

**The rest of K3 verifies.**  The defect census (7112/11088, zero 3976, the
four-class support table, 49896/49896 closed form, split dependence
`{left: 2, right: 2}` and the image-restricted `{left: 1, right: 2}`), the
lift grid (matched pairs commute, mixed do not), and `0 of 207` all reproduce
exactly.  Two qualifications, measured:

- **The zero cells are not a working positive control (F4).**  The
  identically-zero sector is *exactly* the sector where the coarse drag
  vanishes identically: 3976 of 3976, with the refined drag vanishing too in
  every one, and **0 of 11088 cells where a nonvanishing coarse drag meets a
  zero defect**.  The comparator has never returned zero on a nontrivial pair;
  it has only ever computed `0 − 0`.
- **"Rule-blind at the census level" hides a sharp dichotomy (F5).**  The
  cell-level counts are flat (644 for ten rules, 672 for `B-all`) only because
  a cell is scored nonzero if *any* of its 36 sites is.  Site-resolved:
  under the **right** lift the IMAGE support is **0 of 4536** for `A-chart`
  and `B-chart` and **812 of 4536** for every other rule; under the **left**
  lift the MID-(1,1) support is **0 of 4536** for those two and 718–840 for
  the rest.  That dichotomy is exactly the K3 result above.
- `n | n₁` at `0 of 207` is a **vacuous** test as coded (`n₁ % n` for
  `1 ≤ n₁ < n` can never be 0); it is a valid exhaustive restatement of the
  theorem, not an independent measurement.  Verified vacuous for all
  `n ≤ 29`.
- **Sensitivity, no defect:** the comparator reads the coarse drag at
  `base(z)` in *both* lift modes while lifting the refined side by mode.  I
  recomputed the whole census with a **mode-consistent** comparator (coarse
  drag at `base(z)+ℓ` for mid sites under the right lift): **7112 of 11088,
  unchanged**.  Reported as a null.

---

## 4. K4 — THE MOVE CENSUS AND THE HEAD

**Everything in the census reproduces**, on a decomposition algorithm that
shares nothing with the unit's: 27 coarse intervals per class; `DYADIC`
27 SUBDIVIDED / 0 AMBIGUOUS; each `HYPERPLANE@λ` 21/3/3/0 with all three loci
identical; `R1-COPY` 21/0/0/6; `SINGLE-INTERVAL` refused.

**The hyperplane block is real and correctly named.**  The three ambiguous
intervals are the three coarse diagonals starting on the cut column
(`(0,0), (0,1), (0,2)` with link `(1,1)`); each has refined displacement
`(2,1)`, minimal length 2, and **two** distinct candidate interior sites
(offsets `(1,0)` and `(1,1)`), both legitimate refined sites.  I searched the
pinned sources for an incidence or path rule: the declarations carry a link
*set* (`P-I7-LINKS2`), record adjacency, and nothing that orders or selects a
path.  **Concur: `BLOCKED-AT-GRAMMAR-SOURCE-DIAGONAL-INTERVAL-INCIDENCE`.**
One caveat worth a clause: the ambiguity exists *relative to the unit's own
requirement that a coarse interval be realised as a minimal refined path* —
which is the requirement the metric-restriction test needs, so it is not
gratuitous, but it is the unit's, not the grammar's.

**The "16 declared completions … disagree at 12" is thin (F7).**  Reproduced
exactly (16, 12), and then dissected: the sweep runs `n₁` over the splits of
`G-DIAG2`'s axis count (which is 2, so `n₁ = n₂ = 1`) and `f₀, f₁` over
`{1,…,4}`; the disagreement condition `f₀ + n₂ ≠ n₁ + f₁` therefore collapses
to `f₀ ≠ f₁`, and 12 of 16 is that tautology.  The *structure* is right (the
two readings are `n₁ + c_a` and `c_b + n₂`), the number is uninformative, and
"declared completions" is loose — the unit's declared completion rules are
`minimal`/`iterable-64`, not this box.  My stronger version — all six
splittable records, every split, both free counts over `1…12` — gives
**13 158 of 14 256 disagreeing (92.3%)**, with the exact agreement criterion
`f₁ − f₀ = n₂ − n₁` verified on every tuple.  That is the measurement the
claim wants.

**The single-interval refusal is sound.**  The translation-forced cycle
argument checks out: if a displacement acts on a site set by translation, the
set decomposes into equal-length orbits, and a product of cyclic groups forces
every direction-0 cycle to have length `L₀`.  Measured: 10 sites, cycle
lengths `[4,3,3]`, not constant, and `10 % 4 ≠ 0`.  Note the third reported
fact — "only 1 of the 3 declared link displacements has a target at the new
site" — is **declared in the probe, not computed** (`targets` is a literal);
it is true by the construction of the move, but it is not a measurement (F9).

**The count-1 floor and its scope.**  3 of 9 admissible records are
unrefinable — `G-ANISO`, `G-CURVED`, `G-FLAT` — reproduced; the flat record is
among them.  Scope is stated correctly in the paper (a count-1 interval admits
no positive partition; the readout independently rejects a zero part —
verified: a zero part gives a vanishing diagonal entry and a non-positive
`q`).

**The d = 3 gap** (27 of 216, the all-odd parity class) and **the iteration
ceiling** (`⌊log₂ min n⌋`, max 2, attained on `G-ANISO2`; `G-CURVOFF` and
`G-OFFDIAG2` halting early at the inadmissible balanced split) reproduce
exactly, as does the growth series 54/108 → 108/432 → 216/1728 and the
"exactly half the refined links" statement at d = 2.

**The R1-copy control: both fingerprints verified.**  `DYADIC` forces 27
additivity constraints and represents 27 of 27 coarse intervals; `R1-COPY`
forces 0 and leaves 6 unrepresented (the three direction-0 wraps and the three
diagonal wraps, minimal length 4).  The failure modes are genuinely different,
not merely both failures.

**Head composition — adjudication.**  The delivered head
`R6A-NO-MOTIVATED-SPLIT` with `BLOCKED-AT=…` as segment 2 is **the right
carrier**, and I recommend keeping it.  Pin §4's "mixed outcomes compose … the
verdict carries the per-class table" is satisfied by the per-class table plus
the `CLASSES` and `BLOCKED-AT` segments.  One structural remark for the
adjudicator: the head-selection function can *never* emit a composed head —
`BLOCKED` is reachable only when no class is admissible — so "compose" is
realised in the segments alone.  That is defensible (a head must be one
string), but §9 should say in one sentence that the hyperplane branch's
`BLOCKED-AT-GRAMMAR-SOURCE` is a **first-class per-class outcome**, not a
subordinate note on the way to `NO-MOTIVATED-SPLIT`.

---

## 5. K5 — VERDICT REBUILD FROM MY OWN CENSUSES

Every segment was assembled from my own measured numbers and compared to the
delivered string:

```
R6A-NO-MOTIVATED-SPLIT<CLASSES=ADMISSIBLE:1(DYADIC)|BLOCKED:3|REFUSED:1|CONTROL:1|
BLOCKED-AT=DIAGONAL-INTERVAL-INCIDENCE:3-OF-27-INTERVALS-2-CANDIDATES|
REFUSED-AT=SINGLE-INTERVAL:CYCLES433-LINK-TARGETS-1-OF-3|
FORCED=INCIDENCE-27-OF-27|ADDITIVITY-972-OF-972|RESTRICTION-324-OF-324|
INVENTORY=FORCED:4|STABILIZER:0|FREE:4| … |CONTROL=R1-COPY-SUBDIVIDES-0-OF-27-UNREPRESENTED-6-UNMOTIVATED>
```

**Result: byte-identical.**  All twelve segments, including the 21-digit
maximum fiber and the four-class support signature.  No divergence.

Two K5-adjacent checks from the operator side: the arena reproduction claims
of §2 are genuine measurements, not anchor reads — I independently recomputed
the readout determinant (2), record-IS-metric (81 of 81), and the
**lapse-bracket rank, full (2) at every one of the 9 sites**, matching the
pinned value at the origin.  And the two declared negative controls fail in
genuinely different modes: `G-SINGULAR` `det q = 0`, `G-INDEF` `det q = −3`.

---

## 6. FINDINGS

**F1 — MAJOR (K1).  The mechanism paragraph contains a false counterfactual.**
§2: "If the counts were `n_ℓ(x)=φ(x+ℓ)−φ(x)`, the split … would be read off
`φ` and there would be no freedom to measure."  `φ` lives on coarse sites; the
interior site is not one.  Granting a refinement-compatible `φ^r`, the split
is still one free integer per interior site — measured fiber
`13 631 146 639 813 244 878 848` on `G-ANISO2`, **identical to the raw fiber
with no potential** — while the transverse-link fiber collapses INFINITE → 1
(all 108 refined counts determined).  The theorem is the mechanism of the
transverse-link and front freedoms and is **parallel** to the split fiber.
§11 open 2 ("would force the split") inherits the error.
*Repair:* the replacement text in §1.2 above; demote "the mechanism of
everything that follows" to "the mechanism of the front and transverse-link
freedoms"; keep the theorem, which is correct and grammar-universal.

**F2 — MAJOR (K3).  "The dynamics forces an inadmissible value" is
rule-relative and false for two declared rules.**  Solved exactly, 378 cells
per rule over all 14 builds: `A-chart` and `B-chart` force `u = v`, the
declared **right lift**, Z-valued at 378 of 378; `A-axis`/`B-axis` force the
count-weighted interpolation; `B-all` is underdetermined; the six remaining
rules force a third, non-integral value.  A verdict segment
(`NEW-FRONTS=…DYNAMICS-FORCED-NON-INTEGRAL-30-OF-81`) and §11 open 3 carry
the unqualified form.  *Repair:* the rule-scoped sentence and segment in §3
above.  The class-(iii) conclusion for `NEW-FRONT-VALUES` **survives**.

**F3 — MODERATE (K2).  The inventory never tests extremal selections, and one
is unique.**  Max-det at the refined image site is unique at 9 of 9 sites of
all 6 splittable records and yields a globally admissible refinement; the
"most balanced" and "min |q₁₂|" selectors are not unique (0 of 9 sites on
three records).  Pin §3 and protocol K2 both name variational selections.
*Repair:* add an inventory row `EXTREMAL-SELECTORS: tested, max-det unique
9/9 on 6/6 records, NOT DERIVABLE — no extremal principle is declared`, and
soften §5's reading of "genuinely free" to "no declared selector".

**F4 — MODERATE (K3).  The 3976 zero cells are a degenerate sector, not a
working positive control.**  Measured: the zero sector is *exactly* the
sector where the coarse drag vanishes identically (3976 of 3976, refined drag
vanishing too), and there are **0 of 11088** cells with a nonvanishing coarse
drag and a zero defect.  The comparator has never returned zero on a
nontrivial pair.  *Repair:* state the characterisation ("the defect vanishes
exactly where both drags do") — which is itself a result — instead of
"positive control".

**F5 — MODERATE (K3).  The aggregated support table hides a rule dichotomy.**
Site-resolved, the support is strongly rule-dependent: IMAGE support under the
right lift is 0/4536 for the count-blind rules and 812/4536 for all others;
MID-(1,1) under the left lift is 0/4536 vs 718–840.  "Rule-blind at the census
level" is literally true and materially misleading.  *Repair:* print the
per-(rule, lift, class) row, or say the blindness is an artefact of the
cell-level any-site indicator.

**F6 — MODERATE (K5/forced part).  The restriction test is a corollary of
additivity, not an independent comparator.**  Measured: the restricted counts
equal the coarse counts at **972 of 972** cells, so the 324 `q` comparisons
are the same integers re-projected through a deterministic readout.  §4's "the
comparator is … an object built by a route the restriction does not touch"
claims an independence that does not exist.  *Repair:* "restrict ∘ refine = id
on counts (972 of 972); the readout therefore commutes (324 of 324)" — keep
the headline, drop the independence framing.

**F7 — MINOR (K4).  The blocked-branch sweep is a tautology at one record.**
(16, 12) reproduced; it reduces to `f₀ ≠ f₁` because `G-DIAG2`'s axis count is
2.  *Repair:* replace with the criterion `f₁ − f₀ = n₂ − n₁` plus the wider
census (13 158 of 14 256 = 92.3% disagreeing over all splittable records and
both free counts 1…12), or relabel as "a two-parameter completion sweep at
`G-DIAG2`".

**F8 — MINOR (prose, unrendered).  §5.1's odd-count list is
under-inclusive.**  Measured odd counts carried by the splittable declared
records: `{3, 5, 7, 9, 13}`.  The paper lists "3, 5, 9 and 13"; the 7 lives on
`G-CURVOFF` (e.g. `n_diag(0,1) = 7`).  This sentence is **not** among the 15
rendered claims — the programme's known failure locus.  *Repair:* "3, 5, 7, 9
and 13", and add the sentence to the rendered set.

**F9 — MINOR (K4).  `A-notransport` is a duplicate row, and one refusal fact
is declared rather than computed.**  (a) The unit's `drag_at` has no
frozen-front branch, so `A-notransport` is *identically* `A-insert` — measured
identical defect counts (644 = 644) and identical forced-lift behaviour.  The
census has 10 distinct rules, not 11.  (b) `single_interval_arena_probe`
hard-codes "1 of 3 link displacements has a target"; the surrounding
arithmetic is genuine.  *Repair:* implement the frozen front or mark the row
`DEGENERATE-IN-THIS-UNIT`; compute the link-target count from the site set.

**N1 — NOTE.  The comparator asymmetry is inert.**  Mode-consistent
comparator: 7112 of 11088, unchanged.  Recorded so the question is closed.

**N2 — NOTE.  §3.1's "half-integer height" is a continuum gloss**; what is
measured is that the displacement `(2,1)` admits two minimal decompositions
with two distinct *integer* interior sites.

**N3 — NOTE.  K1 sharpening worth adopting** (§1.1): the cocycle half of the
coboundary conditions is exactly `q₁₂ ≡ 0`, and five of the nine admissible
records — including `G-FLAT`, with `φ(x) = x₁+x₂` — are coboundaries on the
universal cover.  The obstruction is purely the periodic holonomy.

**N4 — NOTE.  What the unit gets right and should be credited for.**  The
forced part is genuinely forced and genuinely verified; the incidence
criterion (uniqueness of the minimal decomposition) is a real instrument that
separates three move classes and the control by *different* fingerprints; the
`BLOCKED-AT-GRAMMAR-SOURCE` branch is correctly identified and correctly
named; the count-1 floor and the `⌊log₂ min n⌋` ceiling are theorems, not
observations; and the negative control fails by a measurably different route.
The verdict head is the right one on my own censuses.

---

## 7. GRADE

**ACCEPT-WITH-FIXES.**

The head does not flip.  On a from-scratch instrument sharing no primitive
with the unit's, **every delivered number reproduces** and the verdict string
rebuilds byte-for-byte; the K2 hunt, run to the exhaustiveness the protocol
demands, found no fixing structure derivable from the pinned sources — the two
structures that *do* reduce a fiber to 1 (a lattice reflection, a max-det
selector) are both undeclared, and the reflection would forbid the move on
half the family rather than motivate it.  `R6A-NO-MOTIVATED-SPLIT` stands.

What must change is the reasoning layer: one **false counterfactual** in the
mechanism paragraph (F1) and one **unqualified overclaim carrying a verdict
segment** (F2), plus an untested selector class (F3), a control that has never
fired nontrivially (F4), an aggregated table that hides the dichotomy carrying
F2 (F5), a corollary presented as an independent comparator (F6), a
tautological sweep (F7), an under-inclusive unrendered prose list (F8), and a
duplicate rule row (F9).

Re-verified after this run, unchanged: paper `af5b7f26e427`, code
`ea914c6b55aa`, output `a04b97d2b7bc`, receipt `022c3f488a93`; pin
`a22582f67168`; protocol `02d249f22f6f`; grammar sources `542b8735daf0`,
`f286ba10d2d9`, `d44cb72f8ee9`; founding pin `e9d2bedff244`.

**Single repo file written: `v14/review-r6a-operator.md`.  Nothing else in the
repository was created, modified, or executed.**
