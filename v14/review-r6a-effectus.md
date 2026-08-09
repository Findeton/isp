# R6a — HOSTILE REVIEW, REVIEWER R2 (EFFECTUS / STRUCTURAL LENS)

**Object:** the frozen R6a delivery — paper `af5b7f26e427`, code
`ea914c6b55aa`, output `a04b97d2b7bc`, receipt `022c3f488a93`.  **Pin:**
`a22582f67168`.  **Protocol:** `02d249f22f6f`.  **Grammar sources
(read-only):** `542b8735daf0` / `f286ba10d2d9` / `d44cb72f8ee9`.
**All four delivery hashes verified before and after this run** (§10).

**Interpreter:** `/opt/homebrew/bin/python3.13`.  **Method:** the arena,
the record family, the readout, the move census, the refinement, the
chart group, the drag-rule family and the whole dynamics census were
**reimplemented from the pinned declarations**; nothing was imported
from the unit; exact `int`/`Fraction` arithmetic throughout.  Scratch
only; one repo file written (this one).

**Weight:** **181 delivered scalars independently recomputed, zero
disagreements**, plus 15 new measurements of my own, over ≈4.0M exact
drag/defect evaluations and ≈57M count-vector split enumerations.

**GRADE: ACCEPT-WITH-FIXES.**  Every delivered number is right.  Two
MAJOR meaning defects: one boxed headline sentence is **false as a
universal** and the same census contains its counterexample unreported
(§K3); and the paper's declared *mechanism* does not do the work the
paper assigns it (§K1).  Neither touches the verdict's direction — the
four freedoms **are** genuinely free, and I hunted hard (§K2).

---

## 1. Findings, ranked

| # | sev | finding |
|---|---|---|
| **F1** | **MAJOR** | §6.1's "requiring the drag to agree at the coarse image sites forces the front lift to the count-weighted interpolation" is **rule-relative and false for 9 of the 11 declared rules**. Solved exactly: `A-axis`/`B-axis` → the count-weighted interpolation; **`A-chart`/`B-chart` → the coarse tilt, i.e. `F(mid)=n(x+ℓ)` — the declared RIGHT lift, ℤ-valued and admissible**; `A-linkframe`/`A-linkhalf` → `(1/4,−1/12)`; `A-insert`/`-x`/`-2x`/`A-notransport` → `(6/11,∓9/22)`; `B-all` → underdetermined (2 equations, 3 unknowns). The boxed claim "**the dynamics does not rescue the free front value; it forces an inadmissible one**" is false for the count-blind rules. Verdict segment `NEW-FRONTS` moves. |
| **F2** | **MAJOR** | The same census contains, uncomputed and unreported, the counterexample to F1's headline: **under the RIGHT lift, `A-chart` and `B-chart` give exact drag agreement at every coarse image site, 4,536 of 4,536** (every other rule: 3,724 of 4,536). The paper reports only the LEFT-lift closed form `D(ι(x)) = w^c` — the worst case — and calls it "the defect at a coarse site is the *entire* coarse drag". Both readings are in the delivered census; one was printed. |
| **F3** | **MAJOR** | §2's counterfactual — "if the counts were `n_ℓ(x)=φ(x+ℓ)−φ(x)` … there would be no freedom to measure" — is **false as arithmetic**. Measured: the raw split fiber equals `∏(n_ℓ(x)−1)` over the 27 slots **exactly, at all 9 records**; under the potential counterfactual `φ'(y)` ranges over exactly `n−1` values, in bijection with `(n₁,n₂)` via `n₁ = φ'(y)−φ(x)`. **The fiber is identical** (19,683 → 19,683 at G-DIAG2, and at every record). The no-potential theorem is therefore **not the mechanism of the split freedom**; it is the mechanism of a *different* freedom (see F4). |
| **F4** | MODERATE (repair, favourable) | What the no-potential theorem *does* buy, measured: under a potential the 54 free refined links become functions of the 27 new-site `φ'` values, so **`FREE-TRANSVERSE-LINKS` collapses from INFINITE to 1 given the split**; `NEW-FRONT-VALUES` is untouched (the front is a separate variable, `T-FRONT`). §2's "this is the *mechanism* of everything that follows" should be re-pointed at the *infinite* freedom, where it is true, not at the split, where it is false. |
| **F5** | MODERATE | **False denominator scope, inside the gated render.** "n divides n₁ at 0 of **the 207 splits of the declared family**" — 207 is **G-ANISO2's own** split total (`9×(3+8+12)`); the declared family's splittable records carry **650** (207/101/45/63/153/81). The number is right, its description is not. The §13 addendum (prose renders from the receipt) fixed numerals; it does not check the words around them. |
| **F6** | MODERATE | "the dynamics-forced front lift is non-integral at **30 of 81** cells" names **no arena coordinate**. It is one of 18 (record, split) cells — `(G-ANISO2, floor)` — and the value ranges **18…37** over the design space (low/floor/high × 6 records). §15 (match every coordinate) applies. |
| **F7** | MODERATE | §4's rhetorical close — "**The flattest arena in the declared family is the one that cannot be refined at all**" — attributes to *flatness* what belongs to *scale*. Flat records `(a,a,2a)`, i.e. `q = a·I`, live inside **I7's own declared count box** for `a = 1…6` with ceilings 0,1,1,2,2,2; I built `(4,4,8)` and it takes **2 consecutive dyadic steps**. G-FLAT is unrefinable because it sits **at the count floor**, not because it is flat. |
| **F8** | MODERATE | **The 12 verdict segments carry none of the five measured relativities.** Absent from the verdict string: the d=3 coverage gap (27 of 216); the lift-relativity of the image reading; the family-relativity of the ceiling *value*; the completion-relativity of the defect support (the paper's own §10 concedes it); the rule-relativity of the forced lift (F1). Four live in §10 prose — the surface the programme has twice found false numbers on. |
| **F9** | MODERATE | The `LATTICE-FORCED-1-OF-361` segment names a **structurally empty** fact. Uniqueness of the admissible split ⟺ **every count is exactly 2**; verified over **20,356** splittable count vectors up to (24,24,48): admissibility narrows a site fiber from >1 to 1 at **0** of them, and the unique-split locus is `{(2,2,2)}` at every box size tested (6,12 / 8,16 / 12,24 / 20,40 / 24,48). Nothing about the *lattice* forces anything; the locus is the arithmetic boundary `n−1 = 1`. That "(2,2,2) is outside the declared family" therefore carries no evidential weight. |
| **F10** | MINOR | The "positive control" is thinner than named: of the 3,976 identically-zero cells, **3,696 (93%) are the zero-tilt front `n-const`** (2,772 delta-lapse + 924 other) and 280 are `n-sym`; `n-ramp0` contributes **zero**. The comparator does return zero — but mostly because there is nothing to drag. |
| **F11** | MINOR | `G-BLOCK-IS-REAL`'s "over 16 declared completions the two candidate readings disagree at 12" reduces to `f₀ ≠ f₁` over `{1..4}²` — 12 of 16 is the tautology that two independently free values usually differ. The BLOCKED verdict is right for the *grammar-silence* reason; this sweep adds no information to it. |
| **F12** | MINOR (favourable, strengthened) | The split-dependence probe varied **1 of 27 intervals over 2 values under 1 rule** (`A-axis`, G-OFFDIAG2). I extended it: over the **full declared rule family** the map split ↦ defect field is **injective on every sub-fiber tested** — 24 of 24 random admissible splits of G-DIAG2 distinct, and **9 of 9 exhaustive** on the two-site diagonal sub-fiber. The claim is true and much stronger than the unit measured. New datum: **per rule, `A-chart` and `B-chart` are blind to the diagonal-split direction** (1 distinct field of 3); every count-reading rule separates it. |
| **F13** | MINOR (instrument-adjacent, my lane only) | `G-FORCED-LIFT-NON-INTEGRAL`'s second conjunct tests `n1 % n == 0` for `1 ≤ n1 < n` — **analytically false for every input**. Per §14 (#208) that is a disclosure, not a must-pass gate. (The `forcedlift-lax` mutant dies on the injected literal, not on the predicate.) |
| **F14** | NOTE | The choice inventory records "— NOTHING IN THE PINNED GRAMMAR —" without exhibiting the **candidate forcings it rejected**. Two obvious candidates for `NEW-FRONT-VALUES` (y is itself an event ⟹ `n(y) ≥ 1`; the cumulative reading `n(y) = n(x)+n₁`) are killed by the pinned sources — the second by the no-potential theorem *and* independently by `T-FROZEN-GEOMETRY` — but the inventory shows neither. The RSQ precedent (named precheck candidates) asks for the rejected list. |

**Credit.** Every delivered number reproduces: the census tallies (6 classes × 4 statuses), 972/972, 324/324, all 9 raw and 9 admissible fibers including the 22-digit maximum, all 6 equivariant fibers, 361/261/(2,2,2), 11,088 / 7,112 / 3,976, all four support pairs, 49,896/49,896, all 11 per-rule counts (644×10, `B-all` 672), the 8 inadmissible-build bad-site counts, all 9 ceilings and 9 achieved depths, all 15 inventory-growth numbers, the 4-cell lift grid, 54/54/108, 64 witnesses, d=3's 216/27/162/27 with parity `(1,1,1)`. **Zero disagreements.** The verbatim-text anchors are genuinely load-bearing: `T-COUNTS-POSITIVE`, `T-COUNTS-SEMANTIC`, `T-FRONT`, `T-FROZEN-GEOMETRY` each name a declaration the reasoning actually uses.

---

## 2. K2 — THE CLASSIFICATION DISCIPLINE (primary)

### 2.1 Verdict on the hinge

**The four freedoms are genuinely free. NO MISSED FORCING FOUND.**  I
hunted every source the protocol names and three it does not:

| candidate forcing | measured result |
|---|---|
| the declared chart group (18 elements) | measured stabilisers of orders 2–18; equivariant fibers 3, 5, 24, 88, 288, 29,393,280 — **never 1** |
| readout admissibility as a selector | **0 of 20,356** splittable count vectors up to (24,24,48) have their site fiber narrowed from >1 to 1 by positive-definiteness |
| lattice arithmetic | unique split ⟺ all counts = 2; locus `{(2,2,2)}` stable across five box sizes |
| an extremal/variational selection | none is declared in the pinned sources; the readout is a *re-encoding* (`det = ±2`), not a functional to extremise |
| the dynamics (image agreement) | forces the **front lift**, not the split — and rule-relatively (F1) |
| the dynamics (defect equivalence) | the split ↦ defect map is **injective** over the full rule family (F12) — so no dynamical identification collapses the fiber |
| the front's own semantics | separate configuration variable; both bridges to the counts excluded (§2.3) |

### 2.2 (a) Is the (i)/(ii)/(iii) trichotomy well-posed?

**SOUND at the pinned scope — with one undeclared empty class and one
real gap that the unit closed by luck rather than by design.**

- **"fixed in distribution"** — **not posable, and this must be
  disclosed rather than silently absent.**  The pinned R0 declarations
  (`L, d, links, records, lapse_family, chart_group, count_lattice,
  density_weight, rules, primes, registers, …`) contain **no measure,
  no probability, no ensemble**.  A fourth class would be empty *by
  declaration*.  An empty class named is a scope statement; an empty
  class omitted is an unexamined one.
- **"fixed asymptotically"** — **not posable, and this is a strength
  the unit does not claim.**  The unit's own ceiling theorem
  (`depth ≤ ⌊log₂ min n⌋`) says there is no limit for a freedom to be
  asymptotically irrelevant *in*.  The trichotomy's completeness here
  is **purchased by §7**, and §5 should say so.
- **"fixed up to gauge"** — **the real gap.**  The unit tested exactly
  one equivalence (the declared chart group).  The equivalence that
  could actually collapse the fiber is *dynamical*: identify two
  refinements iff they give the same commutation defect.  The unit
  probed this on **2 of 3,904,305,912,313,344** fiber members, in one
  coordinate direction, under one rule — evidence far too thin for the
  weight it carries.  I closed it: over the full declared rule family
  the map is **injective at 24-of-24 random and 9-of-9 exhaustive**
  (F12).  **The gauge escape is closed at measured scope — but by this
  review, not by the unit.**  Repair: the injectivity sweep enters the
  unit as the class-(iii) *defence*, with the per-rule blindness table
  beside it.

Two further modes I checked and dismissed: *fixed up to isomorphism of
the refined arena* (the automorphisms of `(ℤ₆)²` preserving ι reduce to
the coarse chart group — no new identification), and *fixed by the
readout* (the record **is** the metric, an invertible re-encoding, so
distinct counts are distinct geometries — no collapse).

### 2.3 (b) The front's semantics — does the pinned reading constrain n(y)?

**No — and for a sharper reason than §5.3 gives, which the unit owns
but does not deploy.**

The pinned grammar declares *two different counters of "division
events"*: the front `n(x)` = events **already committed at** site `x`,
and the interval count `n_ℓ(x)` = events **in the interval** between
`x` and `x+ℓ`.  The single semantic bridge that would force the new
site's front value — the cumulative reading `n_ℓ(x) = n(x+ℓ) − n(x)`,
under which `n(y) = n(x) + n₁` — is excluded **twice over**:

1. by the no-potential theorem (strict positivity + periodicity: every
   axis cycle sum ≥ L = 3 > 0, measured minimum 3); and
2. **independently**, by `T-FROZEN-GEOMETRY`: `H_a[N]` moves the front
   and not the counts, so if the counts were front differences they
   would move with `N(x+ℓ) − N(x)` and they do not.

§5.3 cites only (1).  Route (2) is arena-free and positivity-free and
therefore survives exactly the deformations that kill (1) — it should
be printed, because it is the *robust* half of the argument.

The pin's own framing ("a new site exists **because a division event
resolved a record interval**") invites one more candidate: that `y`
*is* an event, so its front carries a floor.  The pinned front is a
**site-local advance counter**, not a global event index; nothing
relates a new site's counter to its neighbours'.  Candidate dead — but
it, and the cumulative reading, belong in the inventory's rejected list
(F14).  **No forcing on n(y) was missed.**

### 2.4 (c) The split: what the 1-of-361 near-miss structurally means

**It is not a near-miss.  It is the arithmetic fixed point of `n−1 =
1`, and it carries no lattice, dynamical or symmetry content.**

Measured (mine): uniqueness of the admissible split at a site ⟺ every
count at that site is exactly 2; **admissibility narrows nothing** (0
of 20,356 splittable vectors up to (24,24,48)); the unique-split locus
is `{(2,2,2)}` at box sizes (6,12), (8,16), (12,24), (20,40), (24,48).
So the measurement's real content — and it *is* real, and it is a
negative worth keeping — is:

> **The readout never selects a split.**  Over 20,356 admissible
> splittable count vectors, positive-definiteness eliminates candidate
> splits but never eliminates all but one.  The only vectors with a
> forced split are those with nothing to choose.

That is the honest sentence, and it is *stronger* than the delivered
one.  The delivered framing ("`LATTICE-FORCED-1-OF-361`", "and it is
not a member of the declared record family") suggests a structure
narrowly missed; there is none to miss.

### 2.5 (d) The head

Adjudicated in §5 below.  **Yes** — the honest head needs the
mechanism, and the mechanism is **totals, not positions** (not "no
coboundary", which F3 shows is the wrong lever).

---

## 3. K1 — THE COBOUNDARY THEOREM: what it means, and what it does not do

**(i) The statement is TRUE and it is a theorem about the GRAMMAR, not
the family.**  Strict positivity (`T-COUNTS-POSITIVE`,
`n_ℓ(x) ∈ ℤ_{>0}`) plus periodicity (`X = (ℤ_L)^d`) give: every axis
cycle sum ≥ L = 3 > 0, while a coboundary sums to zero on every cycle.
**No admissible record inside I7's grammar can carry coboundary
counts** — construction impossible, no census needed.  The nine
measured cycle sums are a witness table; the *theorem* needs none of
them.  Both declarations are load-bearing: on a non-periodic site set
the theorem fails outright (`φ(x)=x₁+x₂` gives positive counts (1,1,2),
`q = I`, admissible).  Within I7 as pinned, periodicity is declared, so
the theorem stands universally.

**(ii) It is NOT the mechanism of the split freedom.**  F3, measured:
the raw fiber is `∏_{27 slots}(n_ℓ(x)−1)` exactly at all 9 records, and
the potential counterfactual returns the *same* number at every record.
A potential does not fix the split because `φ'(y)` at a **new** site is
not determined by `φ` at coarse sites — and the range of `φ'(y)` is
`n−1` values, in bijection with the splits.  §2's "there would be no
freedom to measure" is false, and §2's "This is the *mechanism* of
everything that follows" is therefore mis-assigned.

**(iii) What it IS the mechanism of.**  `FREE-TRANSVERSE-LINKS`.  Under
a potential grammar the whole refined record is a function of the 27
new-site `φ'` values, so the 54 free links become determined and the
infinite fiber collapses to 1 *given the split*.  That is the freedom
the theorem actually governs — and it is the *bigger* one.

**(iv) Ontological or artefact of positivity?**  Neither, precisely:
"the record does not carry positions" is a statement about the
**declared type**.  I7 declares "the interval **cardinality**
`n_ℓ(x) ∈ ℤ_{>0}`" — a cardinality and nothing else.  Positivity
supplies the *size* of the freedom (`n−1` per interval); the
cardinality-only declaration supplies its *existence*.  Strip positivity
(allow 0) and the readout rejects the record anyway; strip periodicity
and the coboundary theorem dies but the split fiber does not.  **The
irreducible carrier is the cardinality declaration.**

**(v) What a position-carrying grammar looks like, and is it reachable
by declaration within I7?**  It is a record that, for each `(x,ℓ)`,
carries the events' *locations* in the interval (an ordered marker set,
or renewal times) rather than their number.  **It is NOT reachable
within I7**: the pinned R0 row declares a cardinality, and §1 of the
pin forbids reaching outside.  A follow-up pin cannot reopen this by
re-reading I7 — it must pin a **different grammar row**.  The named
address is the v10/v11 renewal grammar, which is exactly what the pin's
`BLOCKED-AT-GRAMMAR-SOURCE` machinery exists to point at.  This shapes
R6b (§7).

---

## 4. K3 — "THE DYNAMICS VETOES REFINEMENT": strength, and the honest wording

**The reading is OVERSTATED and must be rewritten.**  The protocol asks
whether the count-weighted interpolation is *the unique lift compatible
with a pinned declaration* or *one natural choice among several*.
Measured answer: **neither — it is the solution for 2 of the 11
declared drag rules.**

Solving `Σ_j Λ^{r}_{ij}(F(mid_j) − n(x)) = Σ_j Λ_{ij}(n(x+e_j) − n(x))`
exactly at (G-OFFDIAG2, low split, site (0,0), front `n-ramp0`), where
the count-weighted value is `(1/3, 0)`:

| rule | forced tilt at the image | ℤ-valued? | = count-weighted? |
|---|---|---|---|
| `A-axis`, `B-axis` | `(1/3, 0)` | no | **yes** |
| **`A-chart`, `B-chart`** | **`(1, 0)` = the coarse tilt** | **yes** | no |
| `A-linkframe`, `A-linkhalf` | `(1/4, −1/12)` | no | no |
| `A-insert`, `-x`, `-2x`, `A-notransport` | `(6/11, ∓9/22)` | no | no |
| `B-all` | underdetermined (2 eqns, 3 unknowns) | — | — |

For the count-blind rules the forced value is `F(mid) = n(x+e)` — **one
of the two declared lifts** (the right lift), integral at every cell.
And the consequence is measurable directly in the delivered census:
**right-lift drag agreement at every coarse image site holds at 4,536
of 4,536 cells for `A-chart` and `B-chart`** (3,724 of 4,536 for every
other rule).  The paper prints only the left-lift closed form, which is
the maximal-defect corner of the same grid.

**Proposed wording for the verdict segment** (every clause computed):

```
NEW-FRONTS=27-FIBER-INFINITE|IMAGE-AGREEMENT-RULE-RELATIVE(
  COUNT-WEIGHTED@A-AXIS+B-AXIS:NON-INTEGRAL-18..37-OF-81-RANGE-OVER-18-
    RECORDxSPLIT-CELLS-30-AT-(G-ANISO2,FLOOR)|
  COARSE-TILT@A-CHART+B-CHART:INTEGRAL=THE-DECLARED-RIGHT-LIFT-
    IMAGE-DEFECT-0-OF-4536|
  THIRD-FORM@6-RULES:NON-INTEGRAL|UNDERDETERMINED@B-ALL)
```

**Proposed replacement for §6.1's boxed sentence:**

> Dynamics-compatibility at the coarse images does not fix the new
> front value; **what it fixes is rule-relative**.  Two of the eleven
> declared rules force the count-weighted interpolation, which is not
> ℤ-valued; two force the declared right lift, which is, and under
> which the image defect vanishes identically; six force a third value;
> one leaves it underdetermined.  In every case the front value at a
> new site is a **declaration**, not a consequence.

And the closed-form paragraph gains its missing half:

> Under the **left** lift the refined front is constant on each cell, so
> the refined drag vanishes at the image and `D(ι(x))` is the entire
> coarse drag (49,896 of 49,896).  Under the **right** lift with a
> count-blind rule the refined tilt *is* the coarse tilt and the image
> defect is identically zero (4,536 of 4,536).  The image reading is a
> **coordinate of the lift**, not a property of the move.

Note this **does not rescue motivation**: the right lift is itself the
class-(iii) `THE-LIFT-PAIR` freedom (fiber 2), and the diagonal mid is
unconstrained by image agreement under both architectures.  The verdict
direction is unchanged; the sentence that claimed a *veto* is not.

---

## 5. K4 — HEAD COMPOSITION, THE COUNT-1 FLOOR, THE CEILING

### 5.1 Should `BLOCKED-AT-GRAMMAR-SOURCE` enter the head?

**No — and for a measured reason the unit should print.**  Granted
*any* incidence declaration, the hyperplane branch **still fails the
motivation audit**, for the same reasons and with two of the four
freedoms verbatim.  Measured (mine), HYPERPLANE@0: 36 refined links, 27
determined by unambiguous coarse intervals, **9 free**; **3 new sites**
whose front values are unconstrained for exactly the `T-FRONT` +
`T-FROZEN-GEOMETRY` reason; the split fiber on its 3 subdivided axis
intervals is 0/1/1/1/8/8/27 by record.  So `BLOCKED` is **a wall
upstream of a road that ends in the same place** — not an alternative
outcome.  Putting it in the head would advertise a branch that might
have gone differently; it would not have.

**Repair:** keep `BLOCKED-AT` as a segment, and add a *conditional
motivation audit* on the blocked branch (assume an incidence rule; run
the same inventory) so the head choice is measured rather than
editorial.  The delivered per-class table is otherwise the right
carrier and the pin's §4 is satisfied.

### 5.2 The count-1 floor — a quantum of separation, and whose artefact?

**A grammar fact, not a family artefact — and its physical reading is
sound but must be stated at record scope, not family scope.**

- The type declaration `n_ℓ ∈ ℤ_{>0}` makes a count-1 interval
  **atomic**; the readout independently rejects a zero part (a zero
  diagonal entry breaks positive-definiteness).  Two independent
  blocks, both declared.
- It is not rare: **100 of the 361** admissible box vectors (27.7%)
  carry a count-1 interval and are unrefinable.
- **Would richer records push it?**  Yes, and *exactly* by the ceiling:
  depth `k` requires a declared min count `≥ 2^k`.  The floor is not a
  floor on the grammar; it is a floor on each record, **purchased with
  counts**.  This is the honest sense in which it is a quantum of
  separation: *the record's own count is its resolution budget.*
- **F7 correction (binding):** "the flattest arena … cannot be refined"
  is a scale statement wearing a curvature costume.  Flat records
  `(a,a,2a)` sit inside I7's own box for `a = 1…6` with ceilings
  0,1,1,2,2,2; `(4,4,8)` achieves **2** steps.  Rewrite: *the declared
  flat record sits at the count floor, and it is the floor, not the
  flatness, that forbids refinement.*

### 5.3 The iteration ceiling — IR/UV, and the unit's most transportable result

`depth ≤ ⌊log₂ min n_ℓ⌋` is a **theorem about the count type** and
holds for any split, not merely the declared ones.  Its meaning is a
genuine UV statement: **the substrate's refinement depth is bounded by
the logarithm of its own smallest interval count** — the record's
information content bounds its refinability, and refinement *spends*
that content.  Paired with the growth measurement (54 free of 108, 216
of 432, 864 of 1,728: each step adds free data by the volume factor
while the original record's reach falls), the honest reading is:

> Refinement on this substrate is not a limit process with a fine
> structure to converge to; it is a **budget being spent**.  The budget
> is a declaration, and it runs out at `⌊log₂ min n⌋`.

**Repair:** separate the theorem (grammar-level) from the value
(family-level) in the verdict — `ITERATION=CEILING-LAW-FLOOR-LOG2-MIN-N
(GRAMMAR)|VALUE-2-ATTAINED-AT-THE-DECLARED-FAMILY|INVENTORY-GROWS-
54/108→216/432→864/1728`.  As delivered, `CEILING-2` reads as a
property of the substrate; it is a property of the declared counts.

---

## 6. K5 (my slice) — does the 12-segment verdict carry every measured restriction?

**No.  Five measured relativities are absent from the verdict string;
four survive only in §10 prose.**

| measured restriction | in the verdict? | where it lives |
|---|---|---|
| d = 3 coverage gap: 27 of 216 refined sites on no coarse interval | **NO** | §3.3 + §10 prose |
| lift-relativity of the image reading (left: whole coarse drag; right: 0 at count-blind rules) | **NO** | §6.2 prose (half of it) |
| family-relativity of the ceiling **value** 2 | **NO** | §7 prose |
| completion-relativity of the defect support | **NO** | §10 non-claim |
| rule-relativity of the forced lift (F1) | **NO** | nowhere — unmeasured |

Repair: add a `DIMENSION=D2-SITE-COMPLETE-27-OF-27|D3-INCOMPLETE-27-OF-216-ALL-ODD-PARITY`
segment; qualify `DEFECT` with `SUPPORT-COMPLETION-RELATIVE` and
`IMAGE-READING-LIFT-RELATIVE`; qualify `ITERATION` per §5.3; rewrite
`NEW-FRONTS` per §4.  Each computed in-gate and flippable, as the
existing twelve are.

---

## 7. THE PROGRAMME QUESTION

### 7.1 What is EARNED, at current scope

1. **(R1)** In the one declared family of drawn atlases, the
   continuum-diagnostic invariants stabilise **because the family
   copies itself** — algebraically forced, `m`-independent.  The family
   cannot answer the question, for a proved reason, and the successor
   recipe (partial orbit overlap) is proved necessary.
2. **(R6a)** On I7's declared record row, a subdivision move exists;
   its *semantic* part is forced and verified exactly (incidence 27/27,
   additivity 972/972, restriction 324/324 — record-IS-metric commutes
   with refinement); and its residual data are **underdetermined by the
   record**: 4 of 8 freedoms class-(iii), two of them infinite, not
   removed by the declared symmetry (equivariant min 3), by
   admissibility (0 of 20,356 narrowings), or by dynamics-compatibility
   (which fixes the *lift*, rule-relatively, and separates the split
   rather than selecting it).
3. **(R6a)** The refinement family **terminates**: `⌊log₂ min n_ℓ⌋`,
   value 2 on the declared family, with the free part growing by the
   volume factor at each level.

### 7.2 What is EARNED vs NARRATIVE about "the continuum is at most effective"

**"The continuum is at most effective" is NARRATIVE.**  It is a claim
about the substrate; nothing measured is about the substrate.  Two
negatives at two pinned rows do not compose into a positive statement
about what the continuum *is*, and there exists no measured *contrast*
row where the limit is posable — so "at most effective" has no
comparator.  Adopting it would be the sixth instance of the pattern the
R1 adjudication §3(c) already engraved.

**The earned statement is strictly weaker, strictly about posability,
and worth stating exactly:**

> **`CONTINUUM-NOT-POSABLE-AT-THE-PINNED-GRAMMAR-ROWS (2 OF 2)`** — at
> both grammar rows the programme has pinned, the continuum question
> cannot be posed from inside.  At R1's row the diagnostic is forced by
> isomorphic copying and carries no limit information.  At I7's row the
> refinement move exists and its *forced* part is exact, but the data a
> refinement needs are not in the record (four irreducible freedoms,
> two infinite) and the iteration terminates at a depth the record
> itself sets.  Both walls are **declarational**: each names the exact
> datum a grammar would have to supply.

Note the two negatives are **not the same negative**, and the programme
should say so: R1's is *the family is degenerate*; R6a's is *the record
is extensive*.  Only the second is about the substrate's own grammar.

### 7.3 What could still reopen it

| route | standing | measured basis |
|---|---|---|
| **A richer record row — an event-POSITION / renewal record (v10/v11)** | **LIVE, and the strongest** | the split fiber is exactly `∏(n_ℓ−1)` = the number of ways to place one interior position given only the totals; a position-carrying record kills it by construction, and (F4) also collapses `FREE-TRANSVERSE-LINKS` from infinite to 1. It does **not** fix `NEW-FRONT-VALUES` (separate variable) — so the audit must be re-run, not assumed. |
| **Unbounded counts** | LIVE but shallow | by the ceiling theorem it is **necessary** for any scaling programme; it removes the termination wall and touches no freedom (the freedoms are per-interval and scale with the counts). A pure declaration, cheap to audit. |
| **R3's algebra as a selector** | LIVE, untested, the only route that could force a freedom *without* changing the record type | R6a claims nothing about it (§10). Obstacle: R3's pin gates `L ≥ 4`, R6a is at `L = 3` — a joint test needs a common arena. |
| Symmetry / admissibility / chart arguments | **CLOSED** | equivariant min 3; 0 of 20,356; stabiliser-fixed count 0 |
| Dynamical gauge (identify splits by defect) | **CLOSED at measured scope** | injective 24-of-24 and 9-of-9 over the full rule family (F12) |

### 7.4 R6b's charter entry — RECOMMENDATION

**RE-SCOPE, do not retire.**  R6b was gated on `EXISTS`; it did not
come.  But retiring it discards the one measured prerequisite the
programme now owns.

1. **State R6b-as-written UNRUNNABLE, with its measured reason** — a
   scaling limit of the dyadic family cannot be taken at the pinned
   grammar: ceiling `⌊log₂ min n⌋` = 2 attained, free part growing by
   the volume factor at every level.  This is the R6a-shaped analogue
   of v13's `GW1-NOT-RUNNABLE`, and it should be recorded in the same
   language.
2. **Replace with `R6b′ — THE RECORD-TYPE DISCRIMINATOR.**  Pin the
   v10/v11 renewal / event-position grammar row *beside* I7's
   cardinality row and re-run **this unit's audit verbatim** on it.
   Falsifiable question: does a record carrying event positions move
   `THE-SPLIT` and `FREE-TRANSVERSE-LINKS` to class (i)?  Three
   pre-registered outcomes, with R6a's own numbers as the predictions:
   split fiber `∏(n−1) → 1` given the position datum; free-link fiber
   `INFINITE → 1` given the split; `NEW-FRONT-VALUES` **unchanged**
   (the front is a separate variable — if it moves, the pinned
   semantics were misread and that is the finding).  This is the
   strongest instrument-reuse case in v14 and it converts a negative
   into a discriminator.
3. **Ship `R6a-b — the unbounded-count probe` as a cheap separable
   unit:** declare a record family with min count `2^k` and measure
   whether anything except the ceiling moves.  Pre-registered
   prediction: **nothing does**.  If it holds, the "just supply
   unbounded counts" escape is closed as vacuous; if it fails, the
   programme has found a scale-dependence it does not expect.
4. **Demote the continuum line's head** in the charter/STATUS from any
   "at most effective" wording to §7.2's earned sentence, with the
   two-walls-are-different-walls note.

---

## 8. THE PROPOSED HEAD

The delivered head is `R6A-NO-MOTIVATED-SPLIT`.  Two defects:

- **It names the mildest wall.**  Of the four class-(iii) freedoms, two
  are **infinite** and the split is the *smallest*.  A reader who
  removed the split freedom would still have no motivated refinement.
- **It carries no mechanism**, and the mechanism is measured.

**Recommended (era-consistent, matching `R2-LOCALITY-DECLARABLE-AT<…>`):**

```
R6A-NO-MOTIVATED-REFINEMENT-AT<
  PIN-NAME=NO-MOTIVATED-SPLIT|
  MECHANISM=THE-RECORD-CARRIES-INTERVAL-TOTALS-NOT-EVENT-POSITIONS
    (SPLIT-FIBER=PROD(n_l-1)-OVER-27-SLOTS-EXACT-9-OF-9-RECORDS|
     UNIQUE-SPLIT-IFF-ALL-COUNTS-2-1-OF-361|
     ADMISSIBILITY-NARROWS-0-OF-20356|
     POTENTIAL-COUNTERFACTUAL-LEAVES-THE-SPLIT-FIBER-UNCHANGED-AND-
       COLLAPSES-FREE-LINKS-INFINITE-TO-1)|
  … the twelve existing segments, repaired per §4/§5/§6 …>
```

Three points on this proposal:

1. **The mechanism clause is measured, not narrated.**  `∏(n_ℓ−1)` is
   an exact identity verified at all nine records; it *is* the count of
   ways to place one interior position given only the total.  That is
   the information-theoretic content, stated as arithmetic.
2. **"Totals not positions", not "no coboundary."**  F3 shows the
   coboundary lever does not move the split at all.  A head built on it
   would be built on the wrong theorem.
3. **Pin fidelity is preserved by the `PIN-NAME=` alias.**  The pin §4
   pre-registered `NO-MOTIVATED-SPLIT`; renaming at adjudication is
   era-standard (RSQ's promotion/demotion; R1's head rewrite), but the
   pre-registered string should remain auditable inside the verdict so
   the pre-registration can still be checked.

If the adjudicator prefers minimal disturbance, the acceptable minimum
is: keep `R6A-NO-MOTIVATED-SPLIT` as the head, and add the `MECHANISM`
segment above verbatim.  **What is not acceptable is a head carrying
neither the move nor the mechanism.**

---

## 9. BINDING REPAIRS (proposed to the adjudicator)

1. **§6.1 rewritten** per §4: the per-rule forced-lift table computed
   in-unit and gated; the boxed sentence replaced; `NEW-FRONTS`
   re-segmented.
2. **§6.2 gains its missing half**: the right-lift image measurement
   (4,536 of 4,536 at the count-blind rules) printed beside the
   left-lift closed form; the image reading labelled lift-relative in
   the verdict.
3. **§2 re-pointed** per F3/F4: the potential counterfactual computed
   in-unit (`∏(n−1)` unchanged; free links `∞ → 1`); the "no freedom to
   measure" sentence deleted; the theorem's target moved to
   `FREE-TRANSVERSE-LINKS`; the `T-FROZEN-GEOMETRY` route printed as
   the positivity-free second argument.
4. **F5 / F6 fixed**: "207 splits" scoped to G-ANISO2 (family total 650
   printed); "30 of 81" carries its (record, split) coordinate and the
   18…37 range.  **Engraving candidate:** *a rendered numeric sentence
   must render its denominator's scope, not only its numeral* — the
   §13 addendum's blind spot, found here.
5. **F7 fixed**: the flat-record scale table `(a,a,2a)`, `a = 1…6`,
   ceilings 0,1,1,2,2,2, printed; the "flattest arena" sentence
   rewritten to name the count floor.
6. **F9 fixed**: `LATTICE-FORCED` renamed and re-derived as
   `UNIQUE-SPLIT-IFF-ALL-COUNTS-2`, with the 0-of-20,356
   admissibility-narrowing measurement as the segment's content.
7. **F8 fixed**: `DIMENSION` segment added; `DEFECT`, `ITERATION`,
   `NEW-FRONTS` qualified per §6.
8. **F12 promoted**: the split ↦ defect injectivity sweep (full rule
   family, exhaustive on a declared sub-fiber) enters the unit as the
   class-(iii) defence, with the per-rule blindness table
   (`A-chart`/`B-chart` blind to the diagonal direction).
9. **§5 gains the trichotomy's own scope statement** per §2.2: the
   distribution class empty by declaration; the asymptotic class
   blocked by §7's ceiling; the gauge class tested against the
   dynamical equivalence, not only the chart group.
10. **F14**: the inventory ships a REJECTED-CANDIDATES list with each
    candidate's measured kill.
11. **§5.1 blocked-branch conditional audit** per §5.1, so the head
    choice is measured.
12. **F13**: `G-FORCED-LIFT-NON-INTEGRAL`'s divisibility conjunct
    demoted to a disclosure (#208).

---

## 10. Hash re-verification (after all work)

| artifact | expected | measured |
|---|---|---|
| `v14/paper-04-refinement-grammar.md` | `af5b7f26e427` | **`af5b7f26e427`** |
| `v14/code/r6a_refinement_exact.py` | `ea914c6b55aa` | **`ea914c6b55aa`** |
| `v14/code/r6a_refinement_output.txt` | `a04b97d2b7bc` | **`a04b97d2b7bc`** |
| `v14/code/r6a_refinement_receipt.json` | `022c3f488a93` | **`022c3f488a93`** |
| pin `v14/note-r6a-refinement-grammar-pin.md` | `a22582f67168` | **`a22582f67168`** |
| protocol `v14/note-r6a-hostile-protocol.md` | `02d249f22f6f` | **`02d249f22f6f`** |

Grammar sources unchanged: `542b8735daf0`, `f286ba10d2d9`,
`d44cb72f8ee9`.  **One repo file written by this reviewer:
`v14/review-r6a-effectus.md`.**  No git writes; no imports from the
unit; `v14/paper-03-*` and `v14/code/r3_*` untouched.

**Recomputation count: 181 delivered scalars (0 disagreements) + 15 new
measurements, over ≈4.0M exact drag/defect evaluations and ≈57M
count-vector split enumerations.**

**GRADE: ACCEPT-WITH-FIXES.**
