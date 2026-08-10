# R6a — THE REFINEMENT GRAMMAR: WHAT THE RECORD'S OWN COUNTING FORCES, AND WHAT IT LEAVES FREE

**Status:** `GREEN-REPAIRED` (v14 R6a, 2026-08-09).
**Pin:** `v14/note-r6a-refinement-grammar-pin.md` (frozen v14 ledger #25, sha256-12 `a22582f67168`).
**Grammar sources (the unit's only authority, hash-verified at run time):** `v13/code/ha_successor_receipt.json` (`542b8735daf0`), `v13/paper-ha-successor.md` (`f286ba10d2d9`), `v13/code/ha_successor_exact.py` (`d44cb72f8ee9`).
**Verdict:** **`R6A-NO-MOTIVATED-SPLIT`**, with the per-class table and the three-wall mechanism below.
**Deliverables:** this paper; `v14/code/r6a_refinement_exact.py`, `v14/code/r6a_refinement_output.txt`, `v14/code/r6a_refinement_receipt.json`.

---

## Scope box

Everything below is at one declared finite arena: the sites $X=(\mathbb Z_L)^d$ with $L=3$ and $d=2$ (with the $d=3$ coverage measurement reported where it is taken), the declared link set, the declared record family, the declared lapse family, the declared drag-rule family, the density weight $w=0$. The grammar is **reimplemented** from the three pinned sources; nothing is imported from them, and every inherited number is recomputed and gated against its pinned value.

The unit takes **no scaling limit**, measures no invariant trajectory, and claims nothing about a constraint algebra. It decides one question: whether the substrate's own record law defines its own refinement.

---

## 1. The question, and the shape of the answer

A refinement move inserts a new site into a record interval. The pinned grammar says what an interval count *is*: $n_\ell(x)$ is **the number of division events in the record interval** between $x$ and $x+\ell$, and it lies in $\mathbb Z_{>0}$. From that semantics one thing follows immediately and is not a choice: if a new site $y$ subdivides the interval $[x,\,x+\ell]$, then

$$n(x,y) \;+\; n(y,\,x+\ell) \;=\; n(x,\,x+\ell),$$

because the events in the whole are the events in the parts. Everything else — which partition $(n_1,n_2)$ occurs, what the new site's transverse links carry, what the front value at the new site is, whether the arena class survives — is what this unit measures.

The answer has three parts, and they point in different directions.

> **The forced part holds exactly.** Additivity is verified at every constraint of every admissible move, and record-IS-metric **commutes with refinement**: the coarse metric rebuilt from the restricted refined counts equals the coarse metric computed directly. Measured: additivity holds at 972 of 972 constraints and the coarse metric is recovered at 324 of 324 cells.

> **The free part is irreducible.** Of the eight residual freedoms the admissible move carries, 4 freedoms forced by a named pinned declaration, 0 fixed by a measured stabiliser, 4 genuinely free. The split is not fixed by any pinned declaration, and it is not fixed by the declared chart group's measured stabiliser either.

> **And the grammar runs out before the census does.** Single-direction hyperplane insertion needs an incidence fact — *which* refined site subdivides a cut diagonal interval — that the pinned sources do not supply, and the ambiguity is measured to be real rather than harmless. That branch stops at `BLOCKED-AT-GRAMMAR-SOURCE`, which the pin makes a first-class outcome.

---

## 2. The arena, rebuilt

| coordinate | value |
|---|---|
| sites | $X=(\mathbb Z_L)^d$, $L=3$, $d=2$ primary ($\lvert X\rvert=9$); $d=3$ extension |
| links $\mathcal L$ | the $d$ axis links and the $\binom d2$ positive diagonals — at $d=2$: $(1,0)$, $(0,1)$, $(1,1)$ |
| geometry record | $n_\ell(x)\in\mathbb Z_{>0}$, the number of division events in the record interval between $x$ and $x+\ell$ |
| front | $n:X\to\mathbb Z$, the number of division events already committed at record site $x$ |
| readout | $q_{ij}(x)\,e_\ell^ie_\ell^j=n_\ell(x)$; at $d=2$, $q_{12}=(n_{e_1+e_2}-n_{e_1}-n_{e_2})/2$ |
| admissible | $q$ nonsingular and positive definite at every site |
| lapse family | the $\lvert X\rvert$ site deltas, the constant profile $1$, and the $d$ chart ramps |
| chart group | the $\lvert X\rvert$ translations and the $d!$ direction relabellings — 18 elements at $d=2$ |

The rebuild reproduces the pinned unit's own readings before anything new is measured: nine admissible records with the two declared negative controls rejected, one in each failure mode; the readout re-encoding determinant; record-IS-metric at 81 of 81 (record, site) pairs; the lapse-bracket rank full at every site; and 361 admissible count vectors in the pinned count box.

Two declared facts carry the rest of the paper: the **type** of the counts — a cardinality, and nothing else — and their **independence from the front**. The interval counts are a configuration variable that $H_a[N]$ does not move; only the front does.

---

## 3. The three walls

The freedoms this unit measures are stopped by three *different* obstructions. Naming them separately is not bookkeeping: they have different scopes, and only one of them is about information.

### 3.1 Wall 1 — the split: combinatorial multiplicity

An interval that carries only its total $n$ admits exactly $n-1$ places for one interior boundary. So the split fiber is a product of multiplicities, and this is an identity rather than an estimate:

$$\text{raw split fiber} \;=\; \prod_{(x,\ell)} \bigl(n_\ell(x)-1\bigr).$$

Measured: the raw split fiber equals the product of (n_l - 1) over the 27 (site, link) slots at 9 of the 9 admissible records, and a granted refinement-compatible potential leaves it unchanged while collapsing the free transverse links from infinite to 1.

The second clause is the counterfactual, granted in its strongest form. Suppose the grammar carried a potential — not on the coarse sites, where the interior site does not live, but a *refinement-compatible* $\varphi^{\mathrm r}$ on the refined lattice with $n^{\mathrm r}=\delta\varphi^{\mathrm r}$. The split at the interior site $y$ of $[x,x+\ell]$ is then $\varphi^{\mathrm r}(y)-\varphi^{\mathrm r}(2x)$, and strict positivity of both halves leaves exactly $n-1$ admissible values of $\varphi^{\mathrm r}(y)$. A potential does not remove one element of the split fiber. What it removes is a *different* entry of the inventory: with $\varphi^{\mathrm r}$ given, every refined link count is a difference of $\varphi^{\mathrm r}$, so `FREE-TRANSVERSE-LINKS` falls from INFINITE to 1.

The split's wall is therefore not a missing potential. It is that **the record carries interval totals and not event positions**, and one interior position in a total of $n$ has $n-1$ places to sit.

### 3.2 Wall 2 — the transverse links: the coboundary theorem, characterised

> **The no-potential theorem.** No record's counts are the coboundary of a site function **on the periodic lattice $X$**. A coboundary sums to zero around every cycle of $X$; the counts are strictly positive, so every axis cycle sum is at least $L$. Measured over the nine admissible records, the smallest axis cycle sum is 3.

The theorem is about the **grammar**, not the declared family: it holds for any strictly positive count field on any periodic lattice, at any $L$ and any $d$, so no admissible record inside this grammar can carry coboundary counts and none exists to construct. The nine cycle sums are a witness table, not the proof.

Its exact content is a characterisation, and the characterisation is measured rather than asserted. An edge assignment is a coboundary **iff** (a) every axis cycle sums to zero **and** (b) the triangle relations $n_{e_i+e_j}(x)=n_{e_i}(x)+n_{e_j}(x+e_i)=n_{e_j}(x)+n_{e_i}(x+e_j)$ hold. Necessity is immediate; sufficiency is rank arithmetic: the coboundary conditions cut out a solution space of dimension 8 in 27 edge variables, matching the rank of delta exactly. Condition (a) alone is what positivity forbids — which is why the theorem is grammar-wide.

There is a second route to the same conclusion, and it is the robust one because it uses neither positivity nor periodicity: $H_a[N]$ moves the front and not the counts, so if the counts were front differences they would move with the front and they do not.

What the theorem forecloses is the front/count relation and the completion, not the split: with a potential on the refined lattice every transverse link is determined, and the front cannot supply the splitting datum either.

### 3.3 Wall 3 — the $q_{12}=0$ sector: periodic holonomy alone

Condition (b) of the characterisation is exactly the vanishing of the off-diagonal metric component. That has a consequence the periodic statement hides: 5 of the 9 admissible records -- exactly those whose off-diagonal metric component vanishes identically -- carry counts that are coboundaries on the universal cover.

On that sector the obstruction is not information. It is **one integer of holonomy per axis cycle**. And the sector is constructive: lift a cover potential to the refined lattice by the same count-weighted interpolation the dynamics forces for the front, and read off the refined counts. Measured, at the one declared record where that interpolation is integral: the induced canonical refinement of G-DIAG2 is admissible at 36 of 36 refined sites, recovers the coarse record at 9 of 9 sites and determines the split. It agrees with the declared balanced split on every covered slot and differs from the declared minimal completion on the free ones, so it is a distinct member of the same split fiber rather than a rediscovery of a build already in the census.

> **Scope, binding.** The universal cover is **not a pinned object**. Nothing in the pinned sources declares it, so this measurement names no declaration, moves no freedom out of class (iii), and cannot flip the verdict. It is recorded because it says *where* the obstruction lives on that sector, and because it is the sharpest available statement of what a further declaration would buy.

---

## 4. The move census

Each move class declares a refined lattice shape and a site embedding $\iota$, and nothing else. Every coarse interval is then classified by a single computed criterion — the **uniqueness of the minimal decomposition of its refined displacement into declared link vectors**:

- **INHERITED** — the coarse interval *is* a refined link (one step);
- **SUBDIVIDED** — exactly one refined site lies on it (two steps, one interior site);
- **AMBIGUOUS** — two steps, more than one candidate interior site;
- **UNREPRESENTED** — no minimal one- or two-step realisation at all.

| class | verdict | INH | SUB | AMB | UNR | refined shape |
|---|---|---|---|---|---|---|
| `DYADIC` | **ADMISSIBLE** | 0 | 27 | 0 | 0 | $6\times6$ |
| `HYPERPLANE@0` | BLOCKED | 21 | 3 | 3 | 0 | $4\times3$ |
| `HYPERPLANE@1` | BLOCKED | 21 | 3 | 3 | 0 | $4\times3$ |
| `HYPERPLANE@2` | BLOCKED | 21 | 3 | 3 | 0 | $4\times3$ |
| `SINGLE-INTERVAL` | REFUSED | — | — | — | — | no product lattice |
| `R1-COPY` (control) | CONTROL | 21 | 0 | 0 | 6 | $6\times3$ |

Measured: 27 coarse intervals per class; the dyadic move subdivides 27 of 27, single-direction hyperplane insertion subdivides 3 and leaves 3 ambiguous, and the copying move subdivides 0 and leaves 6 unrepresented.

The census denominator is itself gated against a class list derived from $L$ alone, so a class dropped inside the constructor cannot shrink it.

### 4.1 Why the hyperplane class is blocked, and not merely awkward

Inserting one hyperplane orthogonal to direction 0 subdivides the axis intervals that cross it. It does **not** subdivide the diagonal intervals that cross it: the displacement $(2,1)$ admits two minimal decompositions with two distinct *integer* interior sites, both legitimate refined sites, and the pinned grammar declares a link *set* with no rule choosing between them.

Measured: the coarse displacement has 2 minimal decompositions with 2 distinct interior sites, at each of 3 of the 27 coarse intervals of the class.

The ambiguity is measured rather than assumed to matter, and it is measured at its own criterion. The two candidate readings of a cut interval's count are $n_1+f_0$ and $f_1+n_2$, so they agree exactly when $f_1-f_0=n_2-n_1$; the census runs every splittable record, every site, every split of the axis interval and both free counts over $1\ldots12$. Measured: over 14256 declared completions the two candidate readings disagree at 13158, and the agreement criterion f_1 - f_0 = n_2 - n_1 is verified at every one.

Supplying an incidence rule would be a grammar fact from outside the pinned sources. The branch therefore stops with the fact named: **`DIAGONAL-INTERVAL-INCIDENCE`**. All three declared loci give the same reading. The block is a first-class per-class outcome, not a way-station.

### 4.2 Why the single-interval class is refused

The refusal is arithmetic and it is measured on a built site set: $X$ together with the inserted interior site is constructed, the direction-0 cycle lengths are read off its successor relation, and every declared link displacement is tested for a target at the new site. Measured: the direction-0 cycle lengths become [4, 3, 3], 10 sites is not divisible by the longest cycle 4, and only 1 of the 3 declared link displacements has a target at the new site. A product-of-cyclic-groups site set carrying the declared displacements by translation forces every direction-0 cycle to have the same length; inserting one site into one link breaks that. The class is refused with its reason, not skipped.

### 4.3 The dimension reading

At $d=3$ the declared link set has three axis links and three positive diagonals and **no body diagonal**. Consequently one parity class of refined sites is the interior site of no coarse interval: at d = 3 the dyadic move leaves 27 of 216 refined sites on no coarse interval at all. The dyadic move is site-complete at $d=2$ and site-incomplete at $d=3$, and the gap is exactly the all-odd parity class.

---

## 5. The forced part, verified

For the one admissible class, over the declared record family and the declared split and completion rules, the unit builds 36 refinements, of which 28 are admissible, and checks both halves of the forced part at every cell. The build and constraint denominators are gated against their declared products, so a record dropped from the forced part dies.

- **Additivity.** By construction the two halves of every coarse interval sum to its count; the check is run anyway, because a construction that is never checked is a claim.
- **The metric-restriction test.** The coarse counts are read *back* from the refined arena by summing along the unique minimal decomposition, the readout is applied to the restricted counts, and the result is compared against the coarse record's own $q$.

Measured: additivity holds at 972 of 972 constraints and the coarse metric is recovered at 324 of 324 cells.

> **Record-IS-metric commutes with refinement.** Whatever else the move leaves free, it does not disturb the identification of the record with the metric candidate: refining and then restricting returns the coarse metric exactly, at every record, every declared split and every declared completion.

The restriction test is a **corollary of additivity**, and the unit records it as one: the restricted counts equal the coarse counts at every cell, so the $q$ comparisons are the same integers re-projected through a deterministic readout. The headline stands; it is not an independent comparator.

There is one obstruction inside the forced part itself, and it is a consequence of the count type. A count-1 interval cannot be split into two strictly positive parts, and the readout independently rejects a zero part (a vanishing diagonal entry makes $q$ non-positive-definite). Measured: 3 of the 9 admissible records carry a count-1 interval and admit no subdivision at all: G-ANISO, G-CURVED, G-FLAT.

The declared flat record is one of them — and that is a statement about **scale**, not about flatness. Measured: the flat family (a, a, 2a) is admissible at every scale in the declared count box, with refinement ceilings 0, 1, 1, 2, 2, 2. The declared flat record sits at the count floor, and it is the floor, not the flatness, that forbids refinement.

---

## 6. The choice inventory

This is the unit's core. For the admissible class, every residual freedom is enumerated and classified by a rule applied uniformly: **(i)** forced by a *named* pinned declaration with fiber 1; **(ii)** fixed by a *measured* stabiliser (chart-equivariant fiber 1); **(iii)** genuinely free, with the fiber counted exactly. The class is recomputed from each item's own evidence, so a class-(iii) freedom relabelled class-(i) fails a gate.

| freedom | class | fiber | forced by |
|---|---|---|---|
| INSERTION-LOCUS | (i) | 1 | the move-class declaration: DYADIC subdivides every coarse interval |
| SUBDIVISION-INCIDENCE | (i) | 1 | the declared link set — unique minimal decomposition, 27 of 27 |
| INTERVAL-COUNT-SUM | (i) | 1 | the counting semantics — additivity |
| FRONT-AT-COARSE-IMAGES | (i) | 1 | the image of a coarse site *is* that site |
| **THE-SPLIT** | **(iii)** | 19 683 … 1 257 565 061 957 837 936 381 | — no declared selector — |
| **FREE-TRANSVERSE-LINKS** | **(iii)** | INFINITE | — no declared selector — |
| **NEW-FRONT-VALUES** | **(iii)** | INFINITE | — no declared selector — |
| **THE-LIFT-PAIR** | **(iii)** | 2 | — no declared selector — |

Measured: 4 freedoms forced by a named pinned declaration, 0 fixed by a measured stabiliser, 4 genuinely free. The motivation qualifier is computed from this table and from nothing else: **NOT-MOTIVATED**.

The inventory ships the forcings it **rejected**, each with its measured kill: the declared chart group (equivariant fibers never 1), readout admissibility as a selector, an extremal selection, the cumulative front reading, the new site as an event, and a dynamical gauge that would identify refinements with equal commutation defect.

### 6.1 The split

Measured: the admissible split fiber runs from 19683 to 1257565061957837936381 over the 6 records that admit the move, and the chart-equivariant fiber is never 1 (its smallest value is 3). The equivariant fiber is the count of split assignments invariant under the record's *measured* stabiliser in the declared chart group — the strongest symmetry argument the pinned arena supports. It never singles out a split.

The obvious rejoinder is that one should "just take the uniform split". Two measurements answer it. First, the uniform split is **not always admissible**: of the 36 declared builds only 28 give an admissible refined record, and the balanced split is among the ones that fail (it makes nine refined sites non-positive-definite on `G-OFFDIAG2`). Second, the uniform split is **not always definable**: an interval of odd count has no balanced partition, and the declared family's splittable records carry the odd counts 3, 5, 7, 9 and 13.

Nor is the freedom an accident of the nine declared records. Over the pinned count box: of the 361 admissible count vectors in the declared box, 261 are splittable at all and exactly 1 has a unique admissible split. That vector is $(2,2,2)$, and the reason it is unique is arithmetic, not structural: a site fiber is a singleton exactly when every count at that site is 2. **The readout never selects a split** — over the splittable vectors of the pinned box, positive-definiteness eliminates candidate splits but narrows a fiber from more than one to exactly one at none of them. The only vectors with a forced split are those with nothing to choose.

There is a selector class that *does* single out a split, and it is not declared. A max-det selection at the refined image site is unique at every site of every splittable record and yields a globally admissible refinement; the most-balanced and min-$\lvert q_{12}\rvert$ selectors are not unique. The honest statement is therefore not "no selector" but **no declared selector**: nothing in the pinned sources names a functional to extremise.

### 6.2 The free transverse links

Half the refined arena is invisible to the coarse record: 54 of the 108 refined links lie on no coarse interval. Their fiber is not merely large but infinite, and the infinite family is exhibited rather than asserted: at the interior site of an axis interval the transverse count $b$ is unconstrained and setting $c=a+b$ makes the readout diagonal with $\det q=ab>0$ for every $b\ge1$. A whole one-parameter family of admissible refinements restricts to the same coarse record.

### 6.3 The new front values

The front at a newly inserted site is a separate configuration variable, and neither of the two bridges that would tie it to the counts survives: the cumulative reading is excluded by the coboundary theorem *and*, independently, by the declared independence of the record from the front; and the pinned front is a site-local advance counter, so nothing relates a new site's counter to its neighbours'. §7 shows what dynamics-compatibility does instead — and that what it does is a function of the drag rule.

---

## 7. The dynamics-compatibility census

Refine-then-advance versus advance-then-refine, for $H_a[N](n,m)=(n+N,\;m+w[N,n])$, over both drag architectures, every declared rule, every declared lapse, a declared front family and both declared lifts. The matter record cancels between the two orders, so the defect is a pure drag comparison,

$$D(z) \;=\; w^{\mathrm c}[N,n]\bigl(\mathrm{base}(z)\bigr) \;-\; w^{\mathrm r}\bigl[N^{\mathrm r},F(n)\bigr](z).$$

### 7.1 The lift is a choice, and what the dynamics forces depends on the rule

The front sector commutes for exactly the **matched** lift pairs: (left, left) and (right, right) commute, the two mixed pairs do not. So compatibility rigidly ties the lapse lift to the front lift — and fixes neither. That is the class-(iii) `THE-LIFT-PAIR` entry, fiber 2 over the declared lift family.

Requiring the *drag* to agree at the coarse image sites is a second, sharper condition. Writing $u_\ell$ for the interior-site front offset and $v_\ell$ for the coarse front tilt, the condition is $\Lambda^{\mathrm r}(\iota x)\,u=\Lambda^{\mathrm c}(x)\,v$ — so the forced lift is a **function of the drag rule**, and the unit solves it exactly, per rule, over every admissible build. Measured: of the 11 declared drag rules 2 force the declared right lift, which is integral at every cell, 2 force the count-weighted interpolation, 5 force a third value, 1 imposes no condition on the lift and 1 leaves it underdetermined.

The count-weighted interpolation

$$F(\text{interior site of }[x,x+\ell]) \;=\; n(x) \;+\; \frac{n_1\bigl(n(x+\ell)-n(x)\bigr)}{n_1+n_2}$$

is the value the count-scaled rules force, and it is not of the declared type: integrality for *every* front tilt would require $(n_1+n_2)\mid n_1$ with $1\le n_1<n_1+n_2$, which is impossible. Measured: the count-weighted interpolation is non-integral at 30 of the 81 (front, site, link) cells of G-ANISO2 at the balanced split, and n divides n_1 at 0 of the 207 splits of G-ANISO2 -- the record at which the forced lift is censused; over the 6 splittable records of the declared family the same sweep carries 650 splits.

> **The dynamics never removes the freedom. Under the count-scaled rules it forces a value the declared type does not admit; under the count-blind rules it re-selects one of the two lifts that are already the class-(iii) `THE-LIFT-PAIR`; under the frozen-front rule it imposes no condition on the lift at all; and under the rule that also weights the diagonal link it leaves the lift underdetermined.**

### 7.2 The defect, characterised

Measured: the commutation defect is nonzero at 7126 of 11088 census cells and identically zero at 3962.

The zero cells are not a working positive control, and the census says what they are instead. Measured: every identically-zero cell is a cell at which the coarse drag itself vanishes, 3962 of 3962; the converse fails at 14 cells, all of them under the declared frozen-front rule. The comparator has never returned zero on a nontrivial pair — it has only ever computed $0-0$. That is a result about the census, and it is stated as one.

The defect is a structured object, not a scalar failure. Its site support, classified by which coarse interval each refined site subdivides:

| site class | nonzero | of |
|---|---|---|
| coarse image | 16 296 | 99 792 |
| interior of an $e_2$ interval | 20 510 | 99 792 |
| interior of an $e_1$ interval | 18 578 | 99 792 |
| interior of a diagonal interval | 16 457 | 99 792 |

The support signature is rebuilt in a second pass over the per-cell rows, and the census is also denominated in the defect's own *values*: every site class carries a strictly positive absolute-value mass and a distinct nonzero-component count, so erasing a parity class of defect values is visible where a cell count is not.

At the coarse image sites the defect has an **exact closed form under the left lift**, verified cell by cell: the lifted front is constant on each cell, so the refined drag vanishes there and

$$D(\iota(x)) \;=\; w^{\mathrm c}[N,n](x).$$

That reading is a **coordinate of the lift**, not a property of the move. Under the *right* lift the image defect vanishes identically for the count-blind rules and does not for the others, and both readings come from the same census.

The defect is **split-dependent**: over a genuine split fiber it takes distinct values under both declared lifts, so the class-(iii) split freedom is not physically inert — a different split is a different obstruction.

The declared rule family's own denominator is measured rather than assumed. Measured: the 11 declared drag rules realise 9 distinct defect fields over the census. Architecture B supported on the axis links with weights $\lambda_{e_j}$ *is* architecture A at $\Lambda=\mathrm{diag}(\lambda_{e_j})$; the two architectures separate only through a diagonal link or a non-diagonal $\Lambda$.

---

## 8. The iteration probe

Does a refinement *family* exist? The class composes — a dyadic step applied to a dyadic refinement is again a dyadic step — but the family terminates, and the bound is a theorem about the count type rather than a property of the declared splits.

> **The ceiling.** After $k$ steps a coarse interval of count $n$ has been partitioned into $2^k$ strictly positive parts, so $n\ge 2^k$. No record admits more than $\lfloor\log_2(\min n_\ell)\rfloor$ consecutive steps.

The law is grammar-level; its *value* is a property of the declared counts. Measured over the declared family: the ceiling is 2 consecutive steps and it is attained. It is attained on `G-ANISO2`, whose minimum count is 4; the remaining records stop at one step or at none. Two of the six splittable records stop earlier still, because the balanced split makes the refined record inadmissible.

And the choice inventory **grows** under iteration. Each step covers exactly half the refined links and leaves the other half free, so the free part grows by the volume factor at every level, while the fraction of the level-$k$ arena that the *original* record reaches falls: 54 of 108, then 108 of 432, then 216 of 1728.

> **The continuum question is unposable from inside the pinned grammar.** The substrate's own refinement runs out after a measured, small number of steps, and each step adds more freedom than it resolves.

---

## 9. The negative control: the audit can fail a move

The R1 copying move — append a disjoint block, the label-growth rule — is run through the *same* uniform audit. It preserves the arena class (a product lattice with all links defined), so it is not refused on shape. What the audit measures is that it subdivides nothing: it forces 0 additivity constraints where the dyadic move forces 27, and it loses 6 of the 27 coarse intervals entirely, so for those the restriction test cannot even be posed. Its counts on the appended block are set by a free label rule that no coarse interval constrains.

The audit therefore scores it strictly worse than the dyadic move, **and by a different failure mode**. Both fail; that they fail differently is what makes the audit an instrument rather than a verdict.

---

## 10. The verdict

```
R6A-NO-MOTIVATED-SPLIT<MECHANISM=THE-RECORD-CARRIES-INTERVAL-TOTALS-NOT-EVENT-POSITIONS(SPLIT-FIBER=PROD(n_l-1)-OVER-27-SLOTS-EXACT-9-OF-9-RECORDS|UNIQUE-SPLIT-IFF-ALL-COUNTS-2-1-OF-361|ADMISSIBILITY-NARROWS-0-OF-261|POTENTIAL-COUNTERFACTUAL-LEAVES-THE-SPLIT-FIBER-UNCHANGED-AND-COLLAPSES-FREE-LINKS-INFINITE-TO-1|TRANSVERSE-WALL=COBOUNDARY-THEOREM-ON-THE-PERIODIC-LATTICE-RANK-19-OF-27|q12-ZERO-SECTOR-WALL=PERIODIC-HOLONOMY-5-OF-9-RECORDS-COBOUNDARY-ON-THE-COVER)|CLASSES=ADMISSIBLE:1(DYADIC)|BLOCKED:3|REFUSED:1|CONTROL:1|BLOCKED-AT=DIAGONAL-INTERVAL-INCIDENCE:3-OF-27-INTERVALS-2-CANDIDATES|REFUSED-AT=SINGLE-INTERVAL:CYCLES433-LINK-TARGETS-1-OF-3|FORCED=INCIDENCE-27-OF-27|ADDITIVITY-972-OF-972|RESTRICTION-324-OF-324|INVENTORY=FORCED:4|STABILIZER:0|FREE:4|OBSTRUCTION=THE-SPLIT+FREE-TRANSVERSE-LINKS+NEW-FRONT-VALUES+THE-LIFT-PAIR|SPLIT-FIBER=MIN-19683-MAX-1257565061957837936381-EQUIVARIANT-MIN-3-UNIQUE-SPLIT-IFF-ALL-COUNTS-2-1-OF-361-ADMISSIBILITY-NARROWS-0-OF-261|FREE-LINKS=54-OF-108-FIBER-INFINITE-WITNESSES-64|NEW-FRONTS=27-FIBER-INFINITE|DYNAMICS-FORCED-LIFT-RULE-RELATIVE(COUNT-WEIGHTED@2-RULES-NON-INTEGRAL-30-OF-81-AT-(G-ANISO2,FLOOR)|THE-DECLARED-RIGHT-LIFT@2-RULES-INTEGRAL|A-THIRD-VALUE@5-RULES|VACUOUS@1|UNDERDETERMINED@1)|DEFECT=NONZERO-7126-OF-11088-CELLS-ZERO-3962-SUPPORT-IMAGE:16296-OF-99792|MID-(0, 1):20510-OF-99792|MID-(1, 0):18578-OF-99792|MID-(1, 1):16457-OF-99792|ZERO-SECTOR=BOTH-DRAGS-VANISH-3962-OF-3962|ITERATION=CEILING-LAW-FLOOR-LOG2-MIN-N-GRAMMAR|VALUE-2-ATTAINED-2-AT-THE-DECLARED-FAMILY|INVENTORY-GROWS|CONTROL=R1-COPY-SUBDIVIDES-0-OF-27-UNREPRESENTED-6-UNMOTIVATED|DIMENSION-RELATIVITY=D2-SITE-COMPLETE-27-OF-27|D3-INCOMPLETE-27-OF-216-ALL-ODD-PARITY|LIFT-RELATIVITY=IMAGE-DEFECT-LEFT-WHOLE-COARSE-DRAG-49896-OF-49896|RIGHT-IDENTICALLY-ZERO-AT-2-OF-11-RULES|FAMILY-RELATIVITY=CEILING-VALUE-IS-A-PROPERTY-OF-THE-DECLARED-COUNTS|FLAT-SCALES-0,1,1,2,2,2|COMPLETION-RELATIVITY=DEFECT-SUPPORT-MOVES-AT-36-OF-2772-MATCHED-CELLS-UNDER-THE-OTHER-DECLARED-COMPLETION|RULE-RELATIVITY=11-DECLARED-RULES-9-DISTINCT-DEFECT-FIELDS|FORCED-LIFT-FORMS-A-THIRD-VALUE:5,THE-COUNT-WEIGHTED-INTERPOLATION:2,THE-DECLARED-RIGHT-LIFT:2,UNDERDETERMINED:1,VACUOUS:1>
```

Read as a sentence: **the record grammar as pinned forces exactly the part its counting semantics forces — the incidence, the additivity, the metric restriction — and nothing else.** One move class survives the census; its forced part is perfect; its residual freedom is irreducible, infinite in two of its four components, and not removed by symmetry, by admissibility, or by dynamics-compatibility. A second class stops at a named grammar fact. A third breaks the arena. The control fails by a different route, which is how the audit shows it is measuring.

The last five segments are the unit's **measured relativities**, carried by the verdict rather than by prose because each is a coordinate of the declared arena rather than a property of the substrate:

- **dimension** — the move is site-complete at $d=2$ and site-incomplete at $d=3$;
- **lift** — the image reading is the whole coarse drag under one lift and identically zero, for two of the eleven rules, under the other;
- **family** — the ceiling *law* is grammar-level, its *value* 2 belongs to the declared counts;
- **completion** — the defect's site support moves under the other declared free-link completion;
- **rule** — which front lift the dynamics forces, and how many distinct defect fields the declared rule family realises.

---

## 11. Non-claims

- No continuum limit, no scaling limit, no invariant trajectory. R6b is not entered.
- No claim that a motivated refinement is impossible in general — only that **none is derivable from the three pinned sources at the declared arena**. A grammar carrying, for example, a rule locating division events *within* an interval, or an incidence relation for non-parallel intervals, is not tested here and is not excluded.
- No claim about the constraint algebra, about $\Delta^B$, or about R3's question.
- The universal-cover measurement of §3.3 is a **disclosure about a non-pinned object**. It names no declaration, changes no class, and is not evidence that any freedom is fixed.
- The defect's site support is **completion-relative** and its image reading is **lift-relative**; both are reported as declared-arena coordinates, never as intrinsic quantities.
- The extremal selector of §6.1 is **not a forcing**: it is a measurement of what a declaration this grammar does not make would buy.
- The blocked branch is a statement about the pinned grammar's silence, not about the hyperplane move's impossibility.
- The $d=3$ reading is a coverage measurement at one shape; no general-$d$ claim is made.
- Nothing here is citable before a hostile round confers terminal.

---

## 12. The reopening leads

Three routes could reopen the question. Each is recorded at the strength this unit *measured*, together with what would motivate it. None is entered here: all three would require pinning a grammar row this unit does not pin, and **charter changes are the user's**.

**(i) R6b′ — the record-type discriminator.** The raw split fiber is exactly $\prod(n_\ell-1)$, which is the number of ways to place one interior position given only the totals. A record carrying event *positions* rather than event *counts* therefore kills the split freedom by construction, and a potential collapses the free transverse links from infinite to 1. It does **not** touch `NEW-FRONT-VALUES`, which is a separate declared variable — so the audit must be re-run on the new row, not assumed. *Motivated by:* pinning a deeper grammar row that declares event positions beside this cardinality row, and re-running this unit's audit verbatim on it.

**(ii) The extremal principle.** A max-det selection at the refined image site is unique at every site of every splittable record and yields a globally admissible refinement, while two rival extremal selectors are not unique. This has exactly the shape a forcing would have and is not one. *Motivated by:* a deeper row declaring a variational principle on the record, at which point a selector becomes a derivation rather than a declaration.

**(iii) The universal-cover route.** On the $q_{12}=0$ sector the counts are coboundaries on the cover, and the cover potential's interpolation induces a canonical, admissible, restriction-exact refinement with the split determined. On that sector the obstruction is periodic holonomy, not information. *Motivated by:* a deeper row that de-periodizes the arena or pins cover objects, so that a cover potential is a declared object rather than a construction outside the pinned sources.

---

## 13. The instrument

`v14/code/r6a_refinement_exact.py` emits `r6a_refinement_output.txt` and `r6a_refinement_receipt.json`. Interpreter `/opt/homebrew/bin/python3.13`. Exact arithmetic throughout: `int` and `fractions.Fraction` only, with an AST scan of the source that admits no float literal, no float-adjacent import and no true-division operator; every quotient is routed through one exact helper.

Measured: 71 gates, all passed; 32 anchors; 78 mutants, all dead at their declared gate.

The anchors are of three kinds: file-byte hashes of the pin and the three grammar sources; (path, value) pairs read out of the pinned receipt, so that a path drift changing the arena dies by anchor and not only a byte change; and **verbatim text anchors**, which require each load-bearing grammar sentence this unit reimplements to appear word for word in its pinned source. The text anchors are evaluated *before* the byte anchors, each row names the gate it licenses and that gate is checked registered, and each row anchors the hash of the 480-byte context window centred on its sentence — so a repeal or a negation inserted *around* a preserved sentence dies at the anchor.

The falsifier census is a census of **measured deaths**: every declared mutant is re-invoked by the delivery run itself, each must exit 1 on exactly the gate its row declares with both artifacts byte-unchanged, and the survivor count is computed rather than typed. A gate without a declared falsifier may carry exactly one kind of waiver — `FORCED`, with a machine-checked witness this run evaluates — and no waiver may name a mutant.

Run-mode identity is read by exactly one function, and an AST gate — validated by synthetic injections it must flag — measures that no other function, and in particular no gate predicate, names it. The verdict string is compared for complete equality against a reconstruction built from the receipt object by a function sharing no code and no input with the builder; injection classes for typed, appended, swapped, inert and wholesale-replaced segments die on it, every one of the eighteen segments is shown to move when the receipt row it derives from is perturbed, and all three pre-registered heads are demonstrated reachable. Finally, the serialised receipt is parsed back and its load-bearing cells are compared against the values their own gates measured, so a cell corrupted after its gate passed cannot ship.
