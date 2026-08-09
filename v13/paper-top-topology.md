# TOP — topology on the ladder

**Status:** `GREEN-UNREVIEWED` — delivered at v13 TOP, not yet attacked.

## What Shape the Atlas Is, and Which Rung the Fano Plane Sits On

**Unit:** TOP (topology on the ladder), v13.
**Pin:** `v13/note-top-topology-pin.md`, sha `74a472b54b85`, commit `d9e3a66`.
**Immutable base:** commit `e82c647` (TB3 #299 terminal).
**Instrument:** `v13/code/top_topology_exact.py`.
**Artifacts:** `v13/code/top_topology_output.txt`,
`v13/code/top_topology_receipt.json`.
**Foundation:** TB3's terminal receipt, hash-pinned at SHA-256
`c9bc956fe75129bdf411e4d1c1ce082d5866e7e63f12712e56f6f231dcf5a9a7` and read as
data; the 36-chart atlas is rebuilt from TB3's §2 declaration and nothing is
imported from the TB3 instrument.
**Verdicts**, quoted exactly as the instrument emits them:

```
TOP-GLOBAL-STRUCTURE-<charts 36, 1-cells 5436, 2-cells 204384; components 1,
cycle rank 5401, chi 198984, F_2 ranks (b0,b1,b2) = (1,140,199123); the wing
quotient has chi 33114 and (b0,b1,b2) = (1,25,33138)>
```

```
TOP-MANIFOLD-READING-CONSISTENT<the declared estimator is CHART-INDEPENDENT at
all 36 charts of the reference instance -- one reading everywhere -- but the
reading it returns is not a single number: the local simplex dimension per
coordinate cell is (35,35,35,35,11,35,11,35,35,35), realising dimensions
(11,35), and every chart's link has b_1 = 16998, so a link is never a circle
and the uniformity is NOT manifoldhood; and the consistency is
INSTANCE-SPECIFIC, holding at 3 of the 5 declared instances and failing at
(a W-class preparation at a fully symmetric setting,a partially symmetric
setting)>
```

```
TOP-FANO-SELECTOR-NOT-FOUND<no candidate of the 13 declared passes all three
clauses; the best reach 2 of 3, the order-2 locus holds 384 completions of
which 48 reach GL(3,2), and GL(3,2) is reached at 252 completions spread over
defect orders (1,2,3,4) -- so the locus neither implies nor is implied by the
visit>
```

---

## Abstract

TB3 left an atlas with named groups: 36 charts over six seeds, a ladder
$1 < A_4 < \mathrm{GL}(3,2) < A_6 < A_7$, and a gauge-inclusive holonomy
$\mathrm{Hol} = K \rtimes S_3$. This unit reads its global shape.

**The overlap graph is complete.** Every one of the $\binom{36}{2} = 630$ chart
pairs is identified at some coordinate cell, so the *simplicial* nerve — the
faces being the chart sets with a common overlap — is the full 35-simplex and
is contractible: $\chi = 1$, every reduced homology zero. The atlas has no
simplicial-nerve topology at all.

**All of its topology is in the coordinates.** Resolving each identification by
the coordinate cell it is drawn at — the ten (checkpoint, rule) cells, TB3's
own link convention — gives a 2-dimensional cell complex $N$ with 36 0-cells,
**5,436** 1-cells and **204,384** 2-cells, whose invariants over $\mathbb F_2$
are $b_0 = 1$, $b_1 = \mathbf{140}$, $b_2 = 199{,}123$, $\chi = 198{,}984$,
each computed by two genuinely independent routes.

**That $b_1$ is entirely the read times.** Every cell of positive dimension
belongs to exactly one checkpoint, so $N$ is five sub-complexes glued along
their shared 0-skeleton. Each of the five is measured to have **vanishing
first $\mathbb F_2$-homology**, and
$b_1(N)$ is re-derived from the decomposition — an elimination-free route that
never touches the global boundary matrix — as
$b_0 + (T-1)\lvert V\rvert + \sum_t (b_1^t - b_0^t) = 1 + 144 + 0 - 5 = 140$.
The atlas's first homology is *nothing but* the comparison of read times. At a
**partially symmetric** setting that stops being true: checkpoints 2 and 3 each
acquire $b_1 = 1$, an intrinsic 1-cycle at a single read time, which the fully
symmetric base does not have.

**Coherence costs cycles.** Restricting the 2-cells to those whose three drawn
maps compose to the identity — the strict cocycle condition — keeps
**84,720** of the 204,384 and raises $b_1$ from 140 to **161**: exactly 21
cycles that the *incoherent* triangles were filling.

**The dimension reading is uniform and is not a manifold's.** The declared
estimator — per-coordinate-cell local simplex dimension, the star, and the
$\mathbb F_2$ homology of the vertex **link** — is chart-independent at all 36
charts of the reference instance. But it returns two dimensions, 11 and 35, and
every link has $b_1 = 16{,}998$; a 2-manifold's link is a circle, as the
declared 2-sphere and 2-torus controls exhibit and the pinched control refutes.
At two of the five declared instances the estimator **splits the charts 24/12**
and the reading is `INCONSISTENT`, with the witness chart and its profile
printed.

**The Fano rung is not selected by its locus.** Thirteen candidate selectors
were declared in the instrument's source before any defect subgroup was built,
and measured over the exhaustive **5,040**-completion family on three clauses.
**None passes all three.** Involutivity holds on all 384 completions of the
order-2 locus and nowhere off it — and fails to predict linearity at **320** of
them. Only **48** of the 384 reach $\mathrm{GL}(3,2)$, while
$\mathrm{GL}(3,2)$ is reached at **252** completions spread over defect orders
$\{1, 2, 3, 4\}$ and at none of order 5 or 6, exactly the orders
$\mathrm{GL}(3,2)$ has no element of. The exclusivity of the visit is a
property of the **lex-first selection rule**, not of the order-2 locus.

**The wing factor acts freely on charts and not above them.** The $S_3$ of
$\mathrm{Hol} = K \rtimes S_3$ acts on $N$ by chart pushforward — a
homomorphism, free on the 36 charts, carrying the drawn table to itself with
each drawn map conjugated. It is *not* free higher up: each transposition fixes
**180** 1-cells and each 3-cycle fixes **120** 2-cells. The orbit complex has
6, 996 and 34,104 cells by direct enumeration and by Burnside's lemma alike,
with $\chi = 33{,}114$ and $(b_0, b_1, b_2) = (1, 25, 33{,}138)$ — and
$\chi(N)/6 = 33{,}164$, the difference of exactly $-50$ being what the
fixed-cell census forces.

Everything is stated at the declared finite scope, over $\mathbb F_2$ only, and
nothing is claimed about nature.

---

## 1. The question, and what it is asked of

TB3 built a base and named its groups. What it did not ask is what the atlas
those groups act on *is*. The pin asks four things of it: the overlap graph and
its nerve as a cell complex, with components, cycle structure and
homology-like invariants over $\mathbb F_2$; a dimension reading, posed as a
measurement rather than assumed; the structural property that selects the
exclusive $\mathrm{GL}(3,2)$ visit; and whether the gauge-inclusive holonomy's
wing factor acts on the nerve.

Three of the four turn out to have answers that the obvious object cannot
carry, and saying which object *can* carry them is most of the work.

---

## 2. The foundation, the arena, and the declared objects

### 2.1 What is inherited and how

TB3's terminal receipt is hash-pinned and read as **data**. The base is then
rebuilt here from TB3's §2 declaration — the three-wing carrier of 64
configurations, the wing symmetry $P_\pi = \Sigma_\pi\otimes\Sigma_\pi$, the
three declared rotations, the preparation family, the lex-first-within-property
completion rule, and the two four-clause gluing rules — with **no import** from
the TB3 instrument. **196 anchors** are then gated exit-1 against the pinned
receipt's own bytes, among them:

| what is anchored | value |
|---|---|
| carrier / frames / checkpoints / admitted group | 64 / 6 / 5 / 6 |
| the rule-selected reference completion | `(0,3,2,1,4,5,6,7)` |
| charts and seeds, at all five instances | 36 (6 at the equivariant control) / 6 |
| ordered admitted pairs, per coordinate cell, at all five instances | 50 cells |
| the ordered triangle census, and per checkpoint | 1,226,304 and its five parts |
| the ordered triangle defect multiset over the wing group | 6 values |
| the completion family and its order distribution | 5,040; 48/384/1728/1152/1152/576 |
| the lex-first completion at each defect order | 6 permutations |
| $\lvert K\rvert$, its element-order spectrum, its support, its linear count, and its set equality with $\mathrm{GL}(3,2)$, at each of the five rule-selected rungs | 25 anchors |
| the committed two-wing and three-wing transport graphs | 24 anchors |

The rebuild reproduces every one of them.

### 2.2 The arena (RUNBOOK §15)

Inherited from TB3 verbatim: boundary the final division event (checkpoint 4);
family the 27 declared settings and 9 declared preparations, of which this unit
reads TB3's five declared A3 instances; law the exact Born law of the declared
leg sequence at the node's declared read time; state $p(0) = \delta_{j_0}$;
arena the declared relabelling scope and the subgroup surviving the $j_0$
filter. This unit adds one coordinate of its own, and it is the load-bearing
one: the **coordinate cell** of an identification, namely the pair
(checkpoint, rule), of which there are ten.

### 2.3 The three complexes, declared before they are built

- **$G$, the overlap graph.** A *simple* graph. Nodes: the charts. Edge
  $\{X,Y\}$: an identification link is drawn between them at **some** coordinate
  cell.
- **$N$, the coordinate-resolved nerve** — the **primary** object. 0-cells the
  charts; 1-cells the drawn identification links, **one per unordered pair per
  coordinate cell**, so two charts identified at $k$ cells carry $k$ parallel
  1-cells; 2-cells the **admissible triangles of TB3's own census** — three
  charts pairwise linked at a common checkpoint, one rule chosen per edge —
  deduplicated to their geometric edge-triples. The 1-cell convention is TB3's:
  its transport graph counts one identification link per (pair, checkpoint,
  rule).
- **$N_{\mathrm{coh}}$, the coherent sub-nerve.** Same 0- and 1-cells; a 2-cell
  only where the three drawn maps **compose to the identity** — the cocycle
  condition an atlas's transition maps must satisfy.
- **$N_{\mathrm{simp}}$, the simplicial nerve.** Faces: the chart sets that are
  pairwise linked at **one common** coordinate cell — a genuine nerve, a face
  being a set of charts with a common overlap.

Declared scope: 2-cells are same-checkpoint only, which is TB3's declared
census object. Cross-checkpoint triples lie outside this unit's complex and
nothing is claimed about them.

---

## 3. Q1 — the overlap graph and its nerve

### 3.1 The overlap graph is complete, and the simplicial nerve is therefore empty of content

At the reference instance eight of the ten coordinate cells admit **every**
ordered chart pair — 1,260 of 1,260 — so already at checkpoint 0 under the FULL
rule the overlap graph is $K_{36}$:

| | measured |
|---|---|
| nodes / edges | 36 / **630** |
| components (four routes) | **1** |
| cycle rank (two routes) | **595** |
| the graph is complete | **yes** |

Each coordinate cell's overlap graph is measured to be a **disjoint union of
complete graphs** — that is gated, not assumed — so the faces of
$N_{\mathrm{simp}}$ are exactly the subsets of those components. At the
reference instance the unique maximal face is the whole 36-chart set, so

$$N_{\mathrm{simp}} = \Delta^{35}, \qquad
\chi = \sum_{k=1}^{36} (-1)^{k+1}\binom{36}{k} = 1,$$

computed as an exact alternating binomial sum and predicted independently by
the cone argument. A full simplex is contractible. **The atlas has no
simplicial-nerve topology.** The same holds at all five instances; at the
equivariant control the maximal face is its whole 6-chart set.

That is a real answer to the pin's first question, and it is the reason the
rest of this section is about a different complex. An object whose every
overlap is total records nothing; what records something is *where* the overlaps
are.

### 3.2 The invariant table

| instance | charts | 1-cells | 2-cells | $b_0$ | cycle rank | $b_1$ | $b_2$ | $\chi$ |
|---|---|---|---|---|---|---|---|---|
| **the declared base, fully symmetric** | **36** | **5,436** | **204,384** | **1** | **5,401** | **140** | **199,123** | **198,984** |
| the equivariant-completion control | 6 | 75 | 100 | 1 | 70 | 20 | 50 | 31 |
| a partially symmetric setting | 36 | 3,276 | 57,216 | 1 | 3,241 | 140 | 54,115 | 53,976 |
| an asymmetric setting | 36 | 2,736 | 36,120 | 1 | 2,701 | **136** | 33,555 | 33,420 |
| a W-class preparation, fully symmetric | 36 | 3,276 | 57,216 | 1 | 3,241 | 140 | 54,115 | 53,976 |

Every quantity in that table is computed twice.

- **Components**, four ways: union-find over the drawn links; $\lvert V\rvert$
  minus the $\mathbb F_2$ rank of the boundary matrix; the same for its
  **transpose** under the opposite pivot rule; and a breadth-first spanning
  forest.
- **Cycle rank**, two ways: the spanning forest, which performs no elimination
  at all, and the boundary rank.
- **$\operatorname{rank}\partial_2$**, two ways: elimination on the
  edge-indexed boundary matrix with a highest-bit pivot (5,261 at the
  reference), and elimination on the **cotree-projected** matrix in
  fundamental-cycle coordinates with a lowest-bit pivot and the rows consumed
  in reverse (5,261).
- **$\chi$**, two ways: from the geometric 2-cell set built by the $a<b<c$
  enumeration, and from the **ordered** census taken by the independent triple
  loop divided by the exact traversal multiplicity.

The traversal multiplicity is itself a gate rather than a constant: the ordered
census is measured to be **exactly six times** the geometric 2-cell count at
every instance — three rotations by two orientations — and a probe that removes
**one** geometric 2-cell is measured to break that relation. The agreement of
$\chi$ computed from the Betti numbers with $\chi$ computed from the cell
counts is an **algebraic identity in the ranks** and is recorded as a
disclosure, never as a route.

### 3.3 The first homology is the read times, and the second route says so

Every 1-cell and every 2-cell carries a definite checkpoint, so the five
checkpoint sub-complexes meet exactly in their shared 0-skeleton. For a union
glued along a discrete set $H_2$ is additive and the Euler characteristics add
with the 0-skeleton counted once, whence

$$b_1(N) \;=\; b_0(N) \;+\; (T-1)\lvert V\rvert \;+\;
\sum_t \bigl(b_1(N_t) - b_0(N_t)\bigr).$$

Every input on the right is a per-checkpoint elimination or a union-find count;
the global boundary elimination enters nowhere. The decomposition's own
hypothesis is **measured, not assumed**: $\sum_t b_2(N_t) = b_2(N) = 199{,}123$
at the reference instance, and likewise for the coherent sub-nerve.

At the reference instance:

| checkpoint | 1-cells | 2-cells | $b_0$ | $b_1$ | $\chi$ |
|---|---|---|---|---|---|
| 0 | 1,260 | 57,120 | 1 | **0** | 55,896 |
| 1 | 1,260 | 57,120 | 1 | **0** | 55,896 |
| 2 | 828 | 16,512 | 1 | **0** | 15,720 |
| 3 | 828 | 16,512 | 1 | **0** | 15,720 |
| 4 | 1,260 | 57,120 | 1 | **0** | 55,896 |

so $b_1 = 1 + 144 + 0 - 5 = \mathbf{140}$, and the global elimination returns
140. **Each read time's own atlas has vanishing first $\mathbb F_2$-homology;
the whole first homology of the atlas is the gluing of the read times.**

The other instances make that a measurement and not a tautology of the
construction:

| instance | $\sum_t b_0$ | $\sum_t b_1$ | $b_1$ |
|---|---|---|---|
| the declared base, fully symmetric | 5 | **0** | 140 |
| a partially symmetric setting | 7 | **2** | 140 |
| an asymmetric setting | **9** | 0 | **136** |

At the **asymmetric** setting checkpoints 2 and 3 each split into **three**
components, and the extra $b_0$ costs the union four cycles: $1 + 144 + 0 - 9 =
136$. At the **partially symmetric** setting checkpoints 2 and 3 each split
into two components *and* each carries $b_1 = 1$ — the only place in the
declared family where a single read time has a cycle of its own — and the two
effects cancel to 140 exactly. The number is the same and the mechanism is not,
which is why the decomposition is reported and not only its total.

### 3.4 Coherence costs cycles

A 2-cell of $N$ is **coherent** when its three drawn maps compose to the
identity. At the reference instance **84,720 of 204,384** are, and the count is
taken twice: once while the cell is built, and once from the ordered defect
multiset — itself anchored against the committed receipt — at its identity
entry, $6 \times 84{,}720 = 508{,}320$.

| instance | coherent / all 2-cells | $b_1$ | $b_2$ | $\chi$ |
|---|---|---|---|---|
| the declared base, fully symmetric | 84,720 / 204,384 | **161** | 79,480 | 79,320 |
| the equivariant-completion control | **100 / 100** | 20 | 50 | 31 |
| a partially symmetric setting | 41,520 / 57,216 | 151 | 38,430 | 38,280 |
| an asymmetric setting | **36,120 / 36,120** | 136 | 33,555 | 33,420 |
| a W-class preparation, fully symmetric | 41,520 / 57,216 | 151 | 38,430 | 38,280 |

Two readings, both measured. First, coherence is **not** automatic and it is
**not** rare: at the reference instance only 41% of the admissible triangles
are coherent, while at the equivariant control and at the asymmetric
setting **every** 2-cell is coherent and the two complexes coincide exactly.
Second, deleting the incoherent 2-cells raises $b_1$ from 140 to **161**. The
1-skeleton is untouched, so the per-checkpoint decomposition carries the same
gluing term 144 and the same $\sum_t b_0 = 5$, and the increase is located
where it belongs: the coherent sub-complexes contribute
$161 - 1 - 144 + 5 = \mathbf{21}$ first-homology classes among the checkpoints,
against **0** for the full complex. **Twenty-one independent loops of the atlas
are filled only by triangles whose transition maps do not compose to the
identity.**

---

## 4. Q2 — the dimension reading

### 4.1 The estimator, declared as data

For a chart $X$:

- $\mathrm{dimprofile}(X)$ — over the ten coordinate cells, the local simplex
  dimension $\lvert\text{component of } X \text{ at } c\rvert - 1$, recorded as
  $-1$ where $X$ carries no link at $c$;
- $\mathrm{star}(X)$ — the number of 1-cells and of 2-cells at $X$;
- $\mathrm{link}(X)$ — $(V, E, b_0, b_1)$ over $\mathbb F_2$ of the **link**:
  the graph whose vertices are the charts adjacent to $X$ and whose edges are
  the 2-cells containing $X$.

The reading is `CONSISTENT` exactly when that triple is chart-independent. The
estimator's per-cell dimension is cross-checked inside its gate against a
component census run from the pair table alone — a comparator built
independently of the estimator it audits.

### 4.2 What it returns

| instance | charts | distinct values | reading |
|---|---|---|---|
| **the declared base, fully symmetric** | 36 | **1** | **CONSISTENT** |
| the equivariant-completion control | 6 | 1 | CONSISTENT |
| a partially symmetric setting | 36 | **2** | **INCONSISTENT-⟨`ABC\|ACB`⟩** |
| an asymmetric setting | 36 | 1 | CONSISTENT |
| a W-class preparation, fully symmetric | 36 | **2** | **INCONSISTENT-⟨`ABC\|BAC`⟩** |

At the reference instance the common profile is

$$\mathrm{dimprofile} = (35,35,35,35,11,35,11,35,35,35), \quad
\mathrm{star} = (302,\ 17{,}032), \quad
\mathrm{link} = (35,\ 17{,}032,\ 1,\ 16{,}998).$$

Three things must be said about that and the verdict says all three.

**It is uniform.** One reading at every chart: the pin's "one dimension
everywhere", in the chart direction, holds.

**It is not one number.** The local simplex dimension is 35 at eight coordinate
cells and 11 at two — the two cells where the FULL rule's overlap graph splits
into three complete blocks of twelve. Uniformity across charts is not
uniformity across coordinates, and the profile is printed rather than
summarised.

**It is not a manifold's.** Every link has $b_1 = 16{,}998$. A $d$-manifold's
vertex link has the $\mathbb F_2$ homology of $S^{d-1}$; the declared controls
show exactly that, and the atlas does not.

**And it is instance-specific.** At the partially symmetric setting and at the
W-class preparation the estimator splits the 36 charts **24 / 12**. The
dimension profile is identical across the split; what differs is the star and
the link:

| | majority (24 charts) | witness (12 charts) |
|---|---|---|
| chart | `ABC\|ABC` | **`ABC\|ACB`** (W-class: **`ABC\|BAC`**) |
| dimprofile | $(35,11,35,11,11,11,11,11,35,11)$ | the same |
| star | $(182,\ 4{,}828)$ | $(182,\ 4{,}648)$ |
| link | $(35,\ 4{,}828,\ 1,\ 4{,}794)$ | $(35,\ 4{,}648,\ 1,\ 4{,}614)$ |

Every chart carries the same number of 1-cells and the same per-cell
dimensions; a third of them sit in **180 fewer 2-cells**. Consistency at the
reference instance is therefore a measurement about that instance, not a
property of the construction.

### 4.3 The controls, which decide what the estimator can see

| complex | $V$ | $E$ | $F$ | $\chi$ | $b_0$ | $b_1$ | $b_2$ | every link a circle |
|---|---|---|---|---|---|---|---|---|
| the boundary of a tetrahedron (a 2-sphere) | 4 | 6 | 4 | **2** | 1 | 0 | 1 | **yes** |
| a 9-vertex torus | 9 | 27 | 18 | **0** | 1 | **2** | 1 | **yes** |
| two tetrahedra sharing one vertex | 7 | 12 | 8 | 3 | 1 | 0 | 2 | **no**, witness vertex 0 |

Every cell of that table is anchored exit-1 against the complex's declared
standard invariants. The first two are genuine 2-manifolds and the estimator
returns a circle link at every vertex; the third is a pinch and the estimator
names the pinch point. Positive and negative in one family, on the same code
path that reads the atlas.

---

## 5. Q3 — the Fano-rung selector

### 5.1 The candidate family, frozen before any fixture truth

Thirteen candidate selectors are declared in the instrument's source above
every measurement, and the count of defect subgroups built at the moment the
declaration is registered is gated at **zero**. Each is a predicate $C(q)$ on a
completion — a permutation of the eight system-triple labels fixing label 0.
$d_P(q) = \sigma_P^{-1} q^{-1}\sigma_P q$ is the label defect and
$K(q) = \langle d_P(q) : P \in S_3\rangle$; "reference value" means the value
the quantity takes at the rule-selected ord-2 target, computed in the same run.

The three clauses, also declared in advance: **(a)** the candidate holds on the
whole defect-order-2 locus; **(b)** it holds nowhere off it; **(c)** it
predicts the linearity of the resulting geometry — zero completions satisfying
it whose $K(q)$ has a non-linear element. A candidate is NAMED only if all
three pass.

Before the table, the objects it speaks about are anchored. Each of the five
rule-selected rungs is rebuilt here by the label route and its order, its
element-order spectrum, its support, its count of $\mathbb F_2$-linear elements
and its **set equality** with an independently brute-forced $\mathrm{GL}(3,2)$
are gated exit-1 against the committed receipt:

| rung | $\mathrm{ord}[P^*,u]$ | $\lvert K\rvert$ | linear elements | $K = \mathrm{GL}(3,2)$ |
|---|---|---|---|---|
| A1 target ord = 1 | 1 | 1 | 1 | no |
| **A1 target ord = 2** | 2 | **168** | **168** | **yes** |
| A1 target ord = 3 | 3 | 12 | 1 | no |
| A1 target ord = 6 | 6 | 2,520 | 168 | no |
| the reference completion (GHZ) | 3 | 360 | 24 | no |

### 5.2 The table

Exhaustive over all **5,040** completions; the locus has **384**.

| id | candidate | (a) on the locus | (b) off it | (c) non-linear $K$ | holds at | of those $=\mathrm{GL}(3,2)$ |
|---|---|---|---|---|---|---|
| C1 | involutivity | **384/384** | **0** | 320 | 384 | 48 |
| C2 | defect fixed-point count | **384/384** | **0** | 320 | 384 | 48 |
| C3 | completion support | 40/384 | 275 | 288 | 315 | 6 |
| C3b | completion cycle type | 24/384 | 81 | 84 | 105 | 6 |
| C4 | defect $\mathbb F_2$-linearity | 64/384 | 272 | **0** | 336 | 252 |
| C4b | declared-symmetry defect linearity | 192/384 | 816 | 672 | 1,008 | 252 |
| C5 | completion $\mathbb F_2$-linearity | 32/384 | 136 | **0** | 168 | 126 |
| C6 | defect order profile | 16/384 | 32 | 36 | 48 | 12 |
| C7 | involutive profile | 12/384 | 8 | **0** | 20 | **0** |
| C8 | transvection | 192/384 | **0** | 128 | 192 | 48 |
| C9 | $q$ normalises the wing group | **0**/384 | 12 | **0** | 12 | **0** |
| C10 | Fano collineation | 32/384 | 136 | **0** | 168 | 126 |
| C11 | abelian defect set | 20/384 | 130 | 126 | 150 | **0** |

**No candidate passes all three clauses; the best reach two of three.** The
family splits cleanly into two halves that fail in opposite directions. C1, C2
and C8 hold on the locus and nowhere off it — and do not predict linearity: 320
of the 384 order-2 completions have a $K$ with a non-linear element. C4, C5,
C7, C9 and C10 predict linearity perfectly — and are neither necessary nor
sufficient for the locus.

Two disclosures belong beside the table. **C1 and C2 are extensionally
identical** on this family: a defect at $P^*$ has exactly four fixed labels
precisely when it has order 2, measured 384-for-384 and 0-for-0. And **C4 is
equivalent to $K(q) \subseteq \mathrm{GL}(3,2)$ by algebra**, both at 336
completions — a group generated by $\mathbb F_2$-linear maps is
$\mathbb F_2$-linear, and the converse restricts to generators. Clause (c)'s
zero for C4 could not have come out otherwise and is entered as a disclosure,
not a result. Clause (c) is separately bounded, inside its gate, by a count
taken outside the candidate loop: no candidate's linear sub-count may exceed
the 336 completions in the whole family whose $K$ is linear.

### 5.3 What actually selects the visit

$\mathrm{GL}(3,2)$ is reached — as a **set**, not an order — at **252** of the
5,040 completions, distributed over the defect order at $P^*$ as

| $\mathrm{ord}[P^*,u]$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| completions with $K = \mathrm{GL}(3,2)$ | 4 | **48** | 72 | **128** | **0** | **0** |

Three things follow, all measured.

**The locus is not sufficient.** 48 of 384 is one in eight.

**The locus is not necessary.** 204 of the 252 lie off it, most of them at
defect order 4.

**The order does constrain, but only through the element spectrum.** The
element orders of $\mathrm{GL}(3,2)$ are measured to be $\{1,2,3,4,7\}$;
$d_{P^*}(q)$ lies in $K(q)$, so $\mathrm{ord}[P^*,u] \in \{5,6\}$ makes
$K \subseteq \mathrm{GL}(3,2)$ impossible. The measured zeros at orders 5 and 6
— 1,728 completions — are exactly that necessary condition biting, and nothing
finer.

What then makes the ladder's $\mathrm{GL}(3,2)$ visit *exclusive*? The four A1
targets are chosen by a **lex-first-within-target-order rule**, and against
that four-member comparison six of the thirteen candidates do separate the
ord-2 rung from all four of its neighbours:

| rung | candidates holding |
|---|---|
| A1 target ord = 1 | C4, C4b, C5, C7, C9, C10, C11 |
| **A1 target ord = 2** | **C1, C2, C3, C3b, C4, C4b, C5, C6, C8, C10** |
| A1 target ord = 3 | none |
| A1 target ord = 6 | none |
| the reference completion (GHZ) | none |

C1, C2, C3, C3b, C6 and C8 hold at the ord-2 rung and at none of the other
four. On four instances they look like selectors; on 5,040 they are not. This
is the same shape of honesty TB3's own §5.2 records about its centraliser
criterion: a four-target comparison cannot separate hypotheses that a full
census separates immediately.

TB3's reading — "the ord-2 target is the completion at which the geometry sees
the substrate's own linear group and no more" — is scoped in its own text to
its four rule-selected targets and is **not contradicted**. What this unit adds
is where the exclusivity comes from: the lex-first rule, applied at order 2,
happens to return the transvection $(s_A,s_B,s_C)\mapsto(s_A,s_B,s_C\oplus
s_A)$, which is $\mathbb F_2$-linear; linearity of the completion, not the
order of its defect, is what puts $K$ inside $\mathrm{GL}(3,2)$, and it is
neither implied by nor implies order 2.

---

## 6. Q4 — the wing quotient

### 6.1 The action, and its self-test

TB3 measures $\mathrm{Hol} = K \rtimes S_3$ with the $S_3$ factor the
relabelling group, present in the geometry because loops traverse
identification edges. That $S_3$ acts on the atlas by chart pushforward,
$\sigma' \cdot (\sigma, \text{seed}) = (\sigma'\sigma, \text{seed})$, and the
action is measured rather than declared (RUNBOOK §14: the invariance is
measured under the symmetry's **own** action, not under a wholesale
replacement):

| measured | value |
|---|---|
| a group homomorphism, on all 36 ordered pairs | **yes** |
| well defined on every chart and every cell | **yes** |
| free on the 36 charts | **yes** |
| the drawn table carried to itself | **yes** |
| each drawn map **conjugated** by the acting element | **yes** |
| the 2-cells permuted | **yes** |

### 6.2 It is free on charts and on nothing above them

| element | fixed 0-cells | fixed 1-cells | fixed 2-cells |
|---|---|---|---|
| identity | 36 | 5,436 | 204,384 |
| each transposition (`ACB`, `BAC`, `CBA`) | 0 | **180** | 0 |
| each 3-cycle (`BCA`, `CAB`) | 0 | 0 | **120** |

A transposition fixes a 1-cell by **swapping its endpoints**; a 3-cycle fixes a
2-cell by **rotating its three edges**. So no non-trivial subgroup acts freely
on all of $N$, and the quotient is reported as the **orbit chain complex** —
cells the orbits, boundary induced mod 2 — with that stated rather than assumed
away.

### 6.3 The quotient

Orbit counts by two genuinely independent routes — direct enumeration, which
builds each orbit as a set of images, and Burnside's lemma applied to the
fixed-cell census, which builds no orbit at all:

$$(\,\lvert V/G\rvert,\ \lvert E/G\rvert,\ \lvert F/G\rvert\,) = (6,\ 996,\
34{,}104) \quad \text{by both.}$$

Orbit sizes: 816 free 1-cell orbits of size 6 and **180 of size 3**; 34,044
free 2-cell orbits of size 6 and **60 of size 2**.

| the quotient complex | value |
|---|---|
| $V$ / $E$ / $F$ | 6 / 996 / 34,104 |
| $b_0$ / $b_1$ / $b_2$ | **1 / 25 / 33,138** |
| $\chi$ | **33,114** |
| $\chi(N)/\lvert S_3\rvert$ | 33,164 |
| the correction | $\mathbf{-50}$ |

The correction is not a residue: a free action of order 6 would give
$5436/6 = 906$ edge orbits and $204384/6 = 34064$ face orbits, and the measured
excesses are $996 - 906 = 90$ and $34104 - 34064 = 40$, whence
$-90 + 40 = -50$ exactly. The fixed-cell census accounts for the whole of it.

The wing quotient's first homology, **25**, is larger than one sixth of
anything: quotienting by the relabelling group does not divide the atlas's
cycles, it folds 180 edges onto themselves and creates new ones.

---

## 7. The controls

### 7.1 The positive control: the same machinery at two wings

The instrument is written generic in the wing count. Run at **two** wings — a
16-configuration carrier neither committed unit used — it must reproduce the
committed two-wing transport structure, and every cell below is anchored
exit-1 against the hash-pinned receipt:

| $\mathrm{ord}(D)$ | $Q$ | nodes | links | identification links | cycle rank | $b_1$ over $\mathbb F_2$ |
|---|---|---|---|---|---|---|
| 1 | `(0,1,2,3)` | **8** | **11** | **5** | **4** | 4 |
| 3 | `(0,1,3,2)` | **8** | **13** | **7** | **6** | **6** |

The last column is the point of the control: the $\mathbb F_2$ homology
machinery that produces $b_1 = 140$ at three wings returns $b_1 = 6$ here, and
6 is a **committed** number. The homology route is anchored to the corpus and
not only to itself.

The two-wing **atlas** is then run through the same nerve machinery: 4 charts,
44 1-cells, 104 2-cells of which 56 are coherent, $b_0 = 1$, $b_1 = 9$,
$b_2 = 72$, $\chi = 64$.

The three-wing transport graphs are anchored the same way, the reference and
all three of TB3's committed negative controls:

| | links | identification links | cycle rank |
|---|---|---|---|
| the reference transport graph | **150** | **126** | **121** |
| the equivariant completion | 99 | 75 | 70 |
| a different declared transposition | 111 | 87 | 82 |
| an asymmetric setting | 75 | 51 | 46 |

### 7.2 The negative control: the scrambled atlas

Declared before it is built: at each coordinate cell the drawn link set is
replaced by a deterministic pseudo-random set of $\lfloor 3m/4\rfloor$ distinct
chart pairs, the generator an exact integer linear congruential recurrence
seeded by the SHA-256 of the declared data alone — no float, no system entropy,
the same stream on every run.

| | 1-cells | 2-cells | $b_0$ | $b_1$ | $b_2$ | $\chi$ | distinct estimator values |
|---|---|---|---|---|---|---|---|
| the reference | 5,436 | 204,384 | 1 | **140** | 199,123 | 198,984 | **1** |
| the scrambled atlas | 4,072 | 85,645 | 1 | **140** | 81,748 | 81,609 | **36** |

Four of the seven invariants move and the dimension reading **breaks
completely** — all 36 charts return different estimator values, so the reading
is `INCONSISTENT` with a named witness. Two do not move, and that is printed
rather than worked around: $b_0$ and $b_1$ are exactly the invariants the
gluing formula pins to the checkpoint count and the chart count, and a scramble
that preserves per-checkpoint connectivity and simple-connectivity cannot move
them. The control's teeth are in the other five columns, and the
`scramble-off` mutant — which leaves the atlas alone — dies on this gate,
which is what shows the two clauses are measurements rather than restatements.

---

## 8. The verdict

`TOP-GLOBAL-STRUCTURE-⟨computed⟩`, with the table of §3.2, §4.2 and §6.3;
`TOP-MANIFOLD-READING-CONSISTENT` with its computed qualifier; and
`TOP-FANO-SELECTOR-NOT-FOUND` with the family's failure computed clause by
clause. Each verdict string is derived **inside** a gate from the measured
counts, re-derived there independently of the emitter, and a verdict-flip
mutant proves the derivation can fail.

The one sentence the unit will defend:

> The atlas's overlaps are total, so its nerve carries no topology; all of its
> topology lives in the coordinate at which an overlap is drawn, and at the
> declared base the whole of that topology in degree one is the comparison of
> read times. Its local reading is uniform across charts and is not a
> manifold's. And the ladder's Fano rung is picked out by the selection rule
> that chose it, not by the order-2 locus it sits in.

---

## 9. Scope and non-claims

- Everything is at **TB3's declared finite three-wing base**, rebuilt from its
  §2 declaration, and at the **five declared A3 instances**. Nothing is claimed
  about other bases, other wing counts, or nature.
- All homology is over $\mathbb F_2$. No integral homology, no torsion, no
  homotopy type is computed or claimed. "Contractible" for
  $N_{\mathrm{simp}}$ is a **cone** statement about a full simplex, which is a
  genuine homotopy statement; every other homology-like claim is an
  $\mathbb F_2$ rank.
- The 2-cells of $N$ are **same-checkpoint** triangles, TB3's declared census
  object. Cross-checkpoint triples are outside this complex.
- The quotient is the **orbit chain complex**. Because the action is not free
  on 1- and 2-cells, its homology is not certified equal to the singular
  homology of a quotient space, and the fixed-cell census that obstructs the
  identification is printed.
- The selector census uses TB3's **label route** for the defect, which equals
  the transport defect's system image exactly where the preparation factor
  commutes with the declared symmetry; TB3 measures that at 6 of its 9 members
  and the reference preparation is one of them. The census is a statement about
  completions and their defect subgroups, not about transport at every
  preparation.
- `CONSISTENT` in the manifold verdict means **uniform across charts**. It does
  not mean one dimension across coordinate cells (it is not: 11 and 35 both
  occur) and it does not mean manifoldhood (it is not: no link is a circle).
- The unit decides nothing about the cocycle criterion, the dihedral law, the
  ladder's group names, or any TB3 verdict; TB3's terminal numbers are inputs
  here and every one of them is reproduced.

---

## 10. The receipt

| | |
|---|---|
| anchors | **196**, all passing — **172 external** (TB3's hash-pinned receipt) and **24 declared-standard** (the control complexes' invariants) |
| gates | **30** — 29 must-pass, 1 disclosure |
| must-pass failures | **0** |
| mutants | **29**, every one exits 1 and names a falsified gate or anchor |
| must-pass gates never falsified by any mutant | **EMPTY** |
| falsified by a **computation** mutant | 26 of 28 |
| falsified only by a **waiver** | 2, named: `TOP-EXACTNESS`, `TOP-NO-MUTANT-EXEMPTION` |
| the gate excluded from its own denominator | `TOP-FALSIFICATION` |
| determinism | two full delivery runs, **byte-identical** |
| exactness | AST sweep: **no float literal**; integers, `Fraction`s and integer XOR only |
| mutant-identity exemptions | AST sweep: **none** |

The two denominators are reported because they differ. A waiver registers a
value in a gate's own evidence list after that gate's sweep has run; it proves
the gate's predicate is load-bearing for the exit code and nothing more, and
the two gates carried by a waiver alone are named rather than averaged away.

---

## Appendix: deviations

1. **Three complexes, not one.** The pin says "the nerve as a cell complex".
   The genuine simplicial nerve at this atlas is a full simplex and carries no
   invariants, so the unit declares three objects — the simple overlap graph,
   the simplicial nerve, and the coordinate-resolved nerve — and makes the
   third primary. The first two are computed and reported, not discarded.
2. **2-cells are same-checkpoint.** TB3's census object. Cross-checkpoint
   triangles would be a different complex and are outside scope.
3. **$\chi$ from Betti numbers is not a second route.** It is an algebraic
   identity in the ranks and is recorded as a disclosure. The second route to
   $\chi$ is a second **enumeration**.
4. **The $b_1$ second route uses a decomposition theorem.** $H_2$ additivity
   over the checkpoint pieces is what licenses it; the instrument **measures**
   that additivity rather than assuming it, at every instance and for the
   coherent sub-nerve as well.
5. **The quotient is a chain-level object** (§9); the non-freeness is measured
   and printed.
6. **The manifold verdict is read at the reference instance.** It is measured
   to fail at two of the five declared instances, and those instances and their
   witnesses are reported in the same table.
7. **Clause (c) is analytically forced for C4.** A group generated by linear
   maps is linear; the zero is a disclosure, not a measurement, and is labelled
   so. C1 and C2 are measured **extensionally identical** on this family.
8. **The scrambled control moves 4 of 7 invariants.** $b_0$ and $b_1$ do not
   move; the reason is stated (§7.2) rather than the control being re-tuned
   until they did.
9. **Two gates are falsified only by waivers** (`TOP-EXACTNESS`,
   `TOP-NO-MUTANT-EXEMPTION`), both of the AST-sweep kind, whose mutation
   cannot be injected in a computation without editing the source the sweep
   reads. Declared, named, not averaged.
10. **The manifold controls are DECLARED-STANDARD anchors.** Their declared
    side is typed in this source rather than read from committed bytes; they
    buy calibration, not independence, and the provenance table labels them so.
11. **Lean: NONE**, per the pin.
