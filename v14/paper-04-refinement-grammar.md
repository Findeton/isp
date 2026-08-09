# R6a — THE REFINEMENT GRAMMAR: WHAT THE RECORD'S OWN COUNTING FORCES, AND WHAT IT LEAVES FREE

**Status:** `GREEN-UNREVIEWED` (v14 R6a, delivered).
**Pin:** `v14/note-r6a-refinement-grammar-pin.md` (frozen v14 ledger #25, sha256-12 `a22582f67168`).
**Grammar sources (the unit's only authority, hash-verified at run time):** `v13/code/ha_successor_receipt.json` (`542b8735daf0`), `v13/paper-ha-successor.md` (`f286ba10d2d9`), `v13/code/ha_successor_exact.py` (`d44cb72f8ee9`).
**Verdict:** **`R6A-NO-MOTIVATED-SPLIT`**, with the per-class table below.
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

The two facts the rest of the paper leans on are the **type** of the counts and their **independence from the front**. The interval counts are a configuration variable that $H_a[N]$ does not move; only the front does. They are therefore not front differences, and this is not merely undeclared — it is impossible:

> **The no-potential theorem.** No record's counts are the coboundary of a site function. A coboundary sums to zero around every cycle of the periodic lattice; the counts are strictly positive, so every axis cycle sum is positive. Measured over the nine admissible records, the smallest axis cycle sum is 3.

This is the *mechanism* of everything that follows. If the counts were $n_\ell(x)=\varphi(x+\ell)-\varphi(x)$, the split of an interval at its interior site would be read off $\varphi$ and there would be no freedom to measure. There is no such $\varphi$, so the splitting datum a refinement needs is exactly the datum the record does not carry.

---

## 3. The move census

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

### 3.1 Why the hyperplane class is blocked, and not merely awkward

Inserting one hyperplane orthogonal to direction 0 subdivides the axis intervals that cross it. It does **not** subdivide the diagonal intervals that cross it, because the site that would do so lies at half-integer height and is not in $(\mathbb Z_{L+1}\times\mathbb Z_L)$. The move therefore cannot simultaneously subdivide every crossing interval and preserve the arena class.

What the refined arena leaves behind is a coarse diagonal whose refined displacement is $(2,1)$, and the coarse displacement has 2 minimal decompositions with 2 distinct interior sites, and over 16 declared completions the two candidate readings disagree at 12. The pinned sources declare a link *set*; they declare no incidence rule choosing between two candidate interior sites, and supplying one would be a grammar fact from outside them. The branch therefore stops with the fact named: **`DIAGONAL-INTERVAL-INCIDENCE`**. All three declared loci give the same reading.

The ambiguity is measured rather than assumed to matter: if one *did* declare path-additivity, the two readings would give different coarse counts at most completions, so no reading can be adopted silently.

### 3.2 Why the single-interval class is refused

The refusal is arithmetic and it is measured, not argued: the direction-0 cycle lengths become [4, 3, 3], 10 sites is not divisible by the longest cycle 4, and only 1 of the 3 declared link displacements has a target at the new site. A product-of-cyclic-groups site set carrying the declared displacements by translation forces every direction-0 cycle to have the same length; inserting one site into one link breaks that, and the new site has no target for the transverse links. The class is refused with its reason, not skipped.

### 3.3 The dimension reading

At $d=3$ the declared link set has three axis links and three positive diagonals and **no body diagonal**. Consequently one parity class of refined sites is the interior site of no coarse interval: at d = 3 the dyadic move leaves 27 of 216 refined sites on no coarse interval at all. The dyadic move is site-complete at $d=2$ and site-incomplete at $d=3$, and the gap is exactly the all-odd parity class.

---

## 4. The forced part, verified

For the one admissible class, over the declared record family and the declared split and completion rules, the unit builds 36 refinements, of which 28 are admissible, and checks both halves of the forced part at every cell.

- **Additivity.** By construction the two halves of every coarse interval sum to its count; the check is run anyway, because a construction that is never checked is a claim.
- **The metric-restriction test.** The coarse counts are read *back* from the refined arena by summing along the unique minimal decomposition, the readout is applied to the restricted counts, and the result is compared against the coarse record's own $q$ — an object built by a route the restriction does not touch.

Measured: additivity holds at 972 of 972 constraints and the coarse metric is recovered at 324 of 324 cells.

> **Record-IS-metric commutes with refinement.** Whatever else the move leaves free, it does not disturb the identification of the record with the metric candidate: refining and then restricting returns the coarse metric exactly, at every record, every declared split and every declared completion.

There is one obstruction inside the forced part itself, and it is a consequence of the count type. A count-1 interval cannot be split into two strictly positive parts, and the readout independently rejects a zero part (a vanishing diagonal entry makes $q$ non-positive-definite). Measured: 3 of the 9 admissible records carry a count-1 interval and admit no subdivision at all: G-ANISO, G-CURVED, G-FLAT.

The flat record is one of them. **The flattest arena in the declared family is the one that cannot be refined at all.**

---

## 5. The choice inventory

This is the unit's core. For the admissible class, every residual freedom is enumerated and classified by a rule applied uniformly: **(i)** forced by a *named* pinned declaration with fiber 1; **(ii)** fixed by a *measured* stabiliser (chart-equivariant fiber 1); **(iii)** genuinely free, with the fiber counted exactly. The class is recomputed from each item's own evidence, so a class-(iii) freedom relabelled class-(i) fails a gate.

| freedom | class | fiber | forced by |
|---|---|---|---|
| INSERTION-LOCUS | (i) | 1 | the move-class declaration: DYADIC subdivides every coarse interval |
| SUBDIVISION-INCIDENCE | (i) | 1 | the declared link set — unique minimal decomposition, 27 of 27 |
| INTERVAL-COUNT-SUM | (i) | 1 | the counting semantics — additivity |
| FRONT-AT-COARSE-IMAGES | (i) | 1 | the image of a coarse site *is* that site |
| **THE-SPLIT** | **(iii)** | 19 683 … 1 257 565 061 957 837 936 381 | — nothing in the pinned grammar — |
| **FREE-TRANSVERSE-LINKS** | **(iii)** | INFINITE | — nothing in the pinned grammar — |
| **NEW-FRONT-VALUES** | **(iii)** | INFINITE | — nothing in the pinned grammar — |
| **THE-LIFT-PAIR** | **(iii)** | 2 | — nothing in the pinned grammar — |

Measured: 4 freedoms forced by a named pinned declaration, 0 fixed by a measured stabiliser, 4 genuinely free. The motivation qualifier is computed from this table and from nothing else: **NOT-MOTIVATED**.

### 5.1 The split

Measured: the admissible split fiber runs from 19683 to 1257565061957837936381 over the six records that admit the move, and the chart-equivariant fiber is never 1 (its smallest value is 3). The equivariant fiber is the count of split assignments invariant under the record's *measured* stabiliser in the declared chart group — the strongest symmetry argument the pinned arena supports. It never singles out a split.

The obvious rejoinder is that one should "just take the uniform split". Two measurements answer it. First, the uniform split is **not always admissible**: of the 36 declared builds only 28 give an admissible refined record, and the balanced split is among the ones that fail (it makes nine refined sites non-positive-definite on `G-OFFDIAG2`). Second, the uniform split is **not always definable**: an interval of odd count has no balanced partition, and the declared family contains counts 3, 5, 9 and 13.

Nor is the freedom an accident of the nine declared records. Over the pinned count box: of the 361 admissible count vectors in the declared box, 261 are splittable at all and exactly 1 has a unique admissible split. That one is the count vector $(2,2,2)$, and it is not a member of the declared record family.

### 5.2 The free transverse links

Half the refined arena is invisible to the coarse record: 54 of the 108 refined links lie on no coarse interval. Their fiber is not merely large but infinite, and the infinite family is exhibited rather than asserted: at the interior site of an axis interval the transverse count $b$ is unconstrained and setting $c=a+b$ makes the readout diagonal with $\det q=ab>0$ for every $b\ge1$. A whole one-parameter family of admissible refinements restricts to the same coarse record.

### 5.3 The new front values

The front at a newly inserted site is not determined by the coarse record — by §2's no-potential theorem it cannot be. §6 shows that dynamics-compatibility *does* determine it, and determines it to a value the declared type does not admit.

---

## 6. The dynamics-compatibility census

Refine-then-advance versus advance-then-refine, for $H_a[N](n,m)=(n+N,\;m+w[N,n])$, over both drag architectures, every declared rule, every declared lapse, a declared front family and both declared lifts. The matter record cancels between the two orders, so the defect is a pure drag comparison,

$$D(z) \;=\; w^{\mathrm c}[N,n]\bigl(\mathrm{base}(z)\bigr) \;-\; w^{\mathrm r}\bigl[N^{\mathrm r},F(n)\bigr](z).$$

### 6.1 The lift is itself a choice, and the dynamics ties it without fixing it

The front sector commutes for exactly the **matched** lift pairs: (left, left) and (right, right) commute, the two mixed pairs do not. So compatibility rigidly ties the lapse lift to the front lift — and fixes neither. That is the class-(iii) `THE-LIFT-PAIR` entry, fiber 2 over the declared lift family.

A second, sharper measurement follows. Requiring the *drag* to agree at the coarse image sites forces the front lift to the count-weighted interpolation

$$F(\text{interior site of }[x,x+\ell]) \;=\; n(x) \;+\; \frac{n_1\bigl(n(x+\ell)-n(x)\bigr)}{n_1+n_2}.$$

The front is $\mathbb Z$-valued. Integrality of that value for *every* front tilt would require $(n_1+n_2)\mid n_1$ with $1\le n_1<n_1+n_2$, which is impossible. Measured: the dynamics-forced front lift is non-integral at 30 of 81 cells, and n divides n_1 at 0 of the 207 splits of the declared family.

> **The dynamics does not rescue the free front value; it forces an inadmissible one.**

### 6.2 The defect, characterised

Measured: the commutation defect is nonzero at 7112 of 11088 census cells and identically zero at 3976. The zero cells are the census's positive control — a comparator that could not return zero would not be measuring anything.

The defect is a structured object, not a scalar failure. Its site support, classified by which coarse interval each refined site subdivides:

| site class | nonzero | of |
|---|---|---|
| coarse image | 16 296 | 99 792 |
| interior of an $e_2$ interval | 20 706 | 99 792 |
| interior of an $e_1$ interval | 18 438 | 99 792 |
| interior of a diagonal interval | 16 079 | 99 792 |

At the coarse image sites the defect has an **exact closed form** under the left lift, verified cell by cell: the lifted front is constant on each cell, so the refined drag vanishes there and

$$D(\iota(x)) \;=\; w^{\mathrm c}[N,n](x)$$

— the defect at a coarse site is the *entire* coarse drag. It is measured at every one of those cells, not argued.

The defect is **split-dependent**: over a genuine split fiber it takes distinct values under both declared lifts, so the class-(iii) split freedom is not physically inert — a different split is a different obstruction. Restricted to the coarse image sites the dependence is lift-relative: under the left lift that part is split-independent (it is the whole coarse drag), under the right lift it is not. Both readings are reported because both are what was measured.

The defect is **rule-blind at the census level**: every architecture-A rule and two of the three architecture-B rules carry the same nonzero count, and `B-all` — the rule that sums over the diagonal link — carries slightly more. Inserting the metric does not help: `A-insert`, the pinned unit's positive control, has exactly the same defect count as `A-chart`.

---

## 7. The iteration probe

Does a refinement *family* exist? The class composes — a dyadic step applied to a dyadic refinement is again a dyadic step — but the family terminates, and the bound is a theorem about the count type rather than a property of the declared splits.

> **The ceiling.** After $k$ steps a coarse interval of count $n$ has been partitioned into $2^k$ strictly positive parts, so $n\ge 2^k$. No record admits more than $\lfloor\log_2(\min n_\ell)\rfloor$ consecutive steps.

Measured over the declared family: the ceiling is 2 consecutive steps and it is attained. It is attained on `G-ANISO2`, whose minimum count is 4; the remaining records stop at one step or at none. Two of the six splittable records stop earlier still, because the balanced split makes the refined record inadmissible.

And the choice inventory **grows** under iteration. Each step covers exactly half the refined links and leaves the other half free, so the free part grows by the volume factor at every level, while the fraction of the level-$k$ arena that the *original* record reaches falls: 54 of 108, then 108 of 432, then 216 of 1728.

> **The continuum question is unposable from inside the pinned grammar.** The substrate's own refinement runs out after a measured, small number of steps, and each step adds more freedom than it resolves.

---

## 8. The negative control: the audit can fail a move

The R1 copying move — append a disjoint block, the label-growth rule — is run through the *same* uniform audit. It preserves the arena class (a product lattice with all links defined), so it is not refused on shape. What the audit measures is that it subdivides nothing: it forces 0 additivity constraints where the dyadic move forces 27, and it loses 6 of the 27 coarse intervals entirely, so for those the restriction test cannot even be posed. Its counts on the appended block are set by a free label rule that no coarse interval constrains.

The audit therefore scores it strictly worse than the dyadic move, **and by a different failure mode**. Both fail; that they fail differently is what makes the audit an instrument rather than a verdict.

---

## 9. The verdict

```
R6A-NO-MOTIVATED-SPLIT<CLASSES=ADMISSIBLE:1(DYADIC)|BLOCKED:3|REFUSED:1|CONTROL:1|BLOCKED-AT=DIAGONAL-INTERVAL-INCIDENCE:3-OF-27-INTERVALS-2-CANDIDATES|REFUSED-AT=SINGLE-INTERVAL:CYCLES433-LINK-TARGETS-1-OF-3|FORCED=INCIDENCE-27-OF-27|ADDITIVITY-972-OF-972|RESTRICTION-324-OF-324|INVENTORY=FORCED:4|STABILIZER:0|FREE:4|OBSTRUCTION=THE-SPLIT+FREE-TRANSVERSE-LINKS+NEW-FRONT-VALUES+THE-LIFT-PAIR|SPLIT-FIBER=MIN-19683-MAX-1257565061957837936381-EQUIVARIANT-MIN-3-LATTICE-FORCED-1-OF-361|FREE-LINKS=54-OF-108-FIBER-INFINITE-WITNESSES-64|NEW-FRONTS=27-FIBER-INFINITE-DYNAMICS-FORCED-NON-INTEGRAL-30-OF-81|DEFECT=NONZERO-7112-OF-11088-CELLS-ZERO-3976-SUPPORT-IMAGE:16296-OF-99792|MID-(0, 1):20706-OF-99792|MID-(1, 0):18438-OF-99792|MID-(1, 1):16079-OF-99792|ITERATION=FAMILY-FINITE-CEILING-2-ATTAINED-2-INVENTORY-GROWS|CONTROL=R1-COPY-SUBDIVIDES-0-OF-27-UNREPRESENTED-6-UNMOTIVATED>
```

Read as a sentence: **the record grammar as pinned forces exactly the part its counting semantics forces — the incidence, the additivity, the metric restriction — and nothing else.** One move class survives the census; its forced part is perfect; its residual freedom is irreducible, infinite in two of its four components, and not removed by symmetry, by admissibility, or by dynamics-compatibility. A second class stops at a named grammar fact. A third breaks the arena. The control fails by a different route, which is how the audit shows it is measuring.

---

## 10. Non-claims

- No continuum limit, no scaling limit, no invariant trajectory. R6b is not entered.
- No claim that a motivated refinement is impossible in general — only that **none is derivable from the three pinned sources at the declared arena**. A grammar carrying, for example, a rule locating division events *within* an interval, or an incidence relation for non-parallel intervals, is not tested here and is not excluded.
- No claim about the constraint algebra, about $\Delta^B$, or about R3's question.
- The defect's site support is **completion-relative**: it is measured at the declared free-link completions, and a different completion moves it. This is reported as a declared-arena coordinate, never as an intrinsic quantity.
- The blocked branch is a statement about the pinned grammar's silence, not about the hyperplane move's impossibility.
- The $d=3$ reading is a coverage measurement at one shape; no general-$d$ claim is made.
- Nothing here is citable before a hostile round confers terminal.

---

## 11. Opens

1. **The incidence rule.** What minimal addition to the grammar would decide `DIAGONAL-INTERVAL-INCIDENCE`, and would it be a declaration or a derivation? The blocked branch names exactly what is missing.
2. **A record law that carries a potential.** The split freedom is precisely the failure of the counts to be a coboundary. A grammar in which they are (an event-position record rather than an event-count record) would force the split — and would be a different substrate, not a reinterpretation of this one.
3. **The forced-but-inadmissible lift.** The count-weighted interpolation is the unique dynamics-compatible front lift and is non-integral. A $\mathbb Q$-valued front is a declared change of type whose cost is unmeasured.
4. **R6b's prerequisite is not met.** A refinement family exists as a class but terminates at a measured depth of 2 on the declared record family. Any scaling programme on this substrate must first supply a record family with unbounded counts, and that supply is itself a declaration to be audited.

---

## 12. The instrument

`v14/code/r6a_refinement_exact.py` emits `r6a_refinement_output.txt` and `r6a_refinement_receipt.json`. Interpreter `/opt/homebrew/bin/python3.13`. Exact arithmetic throughout: `int` and `fractions.Fraction` only, with an AST scan of the source that admits no float literal, no float-adjacent import and no true-division operator; every quotient is routed through one exact helper.

Measured: 48 gates, all passed; 32 anchors; 34 mutants, no survivors. The anchors are of three kinds: file-byte hashes of the pin and the three grammar sources; (path, value) pairs read out of the pinned receipt, so that a path drift changing the arena dies by anchor and not only a byte change; and **verbatim text anchors**, which require each load-bearing grammar sentence this unit reimplements to appear word for word in its pinned source. The grammar is quoted, not paraphrased.

Run-mode identity is read by exactly one function, and an AST gate — validated by synthetic injections it must flag — measures that no other function, and in particular no gate predicate, names it. The verdict string is compared for complete equality against a reconstruction built from the receipt object by a function sharing no code and no input with the builder; five injection classes plus a head-pinning injection die on it, and every one of the twelve segments is shown to move when the receipt row it derives from is perturbed. All three pre-registered heads are demonstrated reachable.
