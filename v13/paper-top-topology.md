# TOP — topology on the ladder

**Status:** `GREEN-REPAIRED` — panel #307/#310/#311, adjudicated
ACCEPT-WITH-FIXES; repair R-TOP-1 … R-TOP-12 executed 2026-08-09, delivery
reruns byte-identical, awaiting adjudicator verification.

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
**Verdicts**, quoted exactly as the instrument emits them. Each head carries
its own restrictions, and every number in head and body alike is interpolated
from a measured count and gated byte-for-byte against a string rebuilt inside
its gate from the recorded tables:

```
TOP-GLOBAL-STRUCTURE-OF-THE-COORDINATE-RESOLVED-NERVE-DEGREE-1-IS-THE-COORDINATE-COUNT-4x35-UNMOVED-BY-THE-SCRAMBLE<charts
36, 1-cells 5436, 2-cells 204384; components 1, cycle rank 5401, chi 198984,
F_2 ranks (b0,b1,b2) = (1,140,199123); b_1 = (T-1)(|V|-1) = 4 x 35 = 140 and
the scrambled control returns b_1 = 140 as well, so degree one is the
coordinate count and only b_2 (199123 -> 81748) sees the identification data;
the wing quotient has chi 33114 and (b0,b1,b2) = (1,25,33138)>
```

```
TOP-MANIFOLD-READING-CONSISTENT-AT-3-OF-5-INSTANCES-DIMENSIONS-11-AND-35-LINKS-NEVER-CIRCLES-AND-SYMMETRY-FORCED-AT-THE-REFERENCE<the
declared estimator is CHART-INDEPENDENT at all 36 charts of the reference
instance -- one reading everywhere -- but the reading it returns is not a
single number: the local simplex dimension per coordinate cell is
(35,35,35,35,11,35,11,35,35,35), realising dimensions (11,35), and every
chart's link has b_1 = 16998, so a link is never a circle and the uniformity
is NOT manifoldhood; the drawn table of that instance is measured to have 1
chart-orbit(s) under its 36 measured automorphisms, so chart-independence
there is FORCED and is entered as a disclosure; and the consistency is
INSTANCE-SPECIFIC, holding at 3 of the 5 declared instances and failing at (a
W-class preparation at a fully symmetric setting,a partially symmetric
setting)>
```

```
TOP-FANO-SELECTOR-NOT-FOUND-THE-LOCUS-IS-P-STAR-RELATIVE-TRANSPOSITION-CLASS<no
candidate of the 13 declared passes all three clauses; the best reach 2 of 3,
the order-2 locus at the declared P* = ACB holds 384 completions of which 48
reach GL(3,2), and GL(3,2) is reached at 252 completions spread over defect
orders (1,2,3,4) -- so the locus neither implies nor is implied by the visit. 
The locus is an ARENA COORDINATE: the 3 transposition symmetries agree at
locus 384 / on-locus 48, the 2 3-cycles give locus 270 / on-locus 0, so both
counts are P*-relative and only the 252 completions reaching GL(3,2) as a set
are not>
```

And one further pre-registered outcome, declared in the instrument's source
with both of its branches before it was run and re-derived inside its gate
from the measured residual:

```
CROSS-CELL-COHERENT-DIGONS-FILL-EVERY-DEGREE-1-CLASS
```

---

## Abstract

TB3 left an atlas with named groups: 36 charts over six seeds, a ladder
$1 < A_4 < \mathrm{GL}(3,2) < A_6 < A_7$, and a gauge-inclusive holonomy
$\mathrm{Hol} = K \rtimes S_3$. This unit reads its global shape.

**The overlap graph is complete.** Every one of the $\binom{36}{2} = 630$ chart
pairs is identified at some coordinate cell, so the *simplicial* nerve — the
faces being the chart sets with a common overlap — has a single maximal face,
the whole 36-chart set: the full 35-simplex, a cone, contractible. The atlas
has no simplicial-nerve topology at all.

**What topology it has is in the coordinates.** Resolving each identification
by the coordinate cell it is drawn at — the ten (checkpoint, rule) cells,
TB3's own link convention — gives a 2-dimensional cell complex $N$ with 36
0-cells, **5,436** 1-cells and **204,384** 2-cells, whose invariants over
$\mathbb F_2$ are $b_0 = 1$, $b_1 = \mathbf{140}$, $b_2 = 199{,}123$,
$\chi = 198{,}984$.

**In degree one that is the coordinate grid, not the identifications.** Every
cell of positive dimension belongs to exactly one checkpoint, so $N$ is five
sub-complexes glued along their shared 0-skeleton, and the gluing formula
makes $b_1$ the pure coordinate count $(T-1)(\lvert V\rvert - 1) = 4 \times 35
= 140$ exactly when $\sum_t b_0^t - T = \sum_t b_1^t$. The measured content is
that per-checkpoint census, and nothing else: the **scrambled negative
control**, whose identification data is destroyed, returns $b_1 = 140$ too,
while $b_2$ moves from 199,123 to 81,748. The degree-two invariant measures
the atlas; the degree-one invariant measures the grid.

**A read time's own topology is partition nesting, exactly.** At each
checkpoint the two rules partition the charts into complete blocks; the
bipartite **block-incidence graph** joining blocks that share a chart has, at
all **25** (instance, checkpoint) pairs, the sub-nerve's own $b_0$ and $b_1$.
"Every checkpoint sub-nerve is simply connected" *is* "at every read time the
two block partitions are nested". Where they are not — checkpoints 2 and 3 of
the partially symmetric setting and of the W-class preparation — the incidence
graph carries the cycle the sub-nerve carries.

**And the surviving degree-one classes are not a cross-read-time
obstruction.** Two charts identified at $k$ coordinate cells carry $k$
parallel 1-cells and $\binom{k}{2}$ digons; a digon is *coherent* when its two
drawn maps agree. At the reference instance 540 of the 630 multiply-drawn
pairs disagree somewhere — and yet filling **only** the 11,268 coherent
cross-read-time digons already reduces $b_1$ from 140 to **0**, while the
2,286 same-checkpoint digons kill nothing at all. So no degree-one class is
carried by a disagreement between the maps drawn at different read times: the
cycles of $N$ are an artifact of the declared same-checkpoint 2-cell scope,
and the continuum rung inherits a trivial $H_1$ from this base.

**Coherence costs cycles.** Restricting the 2-cells to those whose three drawn
maps compose to the identity — the strict cocycle condition — keeps **84,720**
of the 204,384 and raises $b_1$ from 140 to **161**: exactly 21 cycles,
intrinsic to single read times, that the *incoherent* triangles were filling.

**The dimension reading is uniform, is not a manifold's, and where it is
uniform it is forced.** The declared estimator — per-coordinate-cell local
simplex dimension, the star, and the $\mathbb F_2$ homology of the vertex
**link** — is chart-independent at all 36 charts of the reference instance.
But it returns two dimensions, 11 and 35, and every link has $b_1 = 16{,}998$;
a 2-manifold's link is a circle, as the declared 2-sphere and 2-torus controls
exhibit and the pinched control refutes. And the reference instance's drawn
table is **chart-transitive** — 36 of 36 declared automorphism candidates pass,
one chart-orbit — so a chart-invariant *could not* have come out
chart-dependent there, and `CONSISTENT` at the reference is entered as a
disclosure. What is measured is the contrast: at two of the five declared
instances the table is not chart-transitive and the estimator **splits the
charts 24/12**.

**The Fano rung is not selected by its locus, and the locus is an arena
coordinate.** Thirteen candidate selectors were declared in the instrument's
source above every measurement, and measured over the exhaustive
**5,040**-completion family on three clauses. **None passes all three** — and
the thirteen names carry only **eleven** distinct predicates, C1 ≡ C2 and
C5 ≡ C10. Involutivity holds on all 384 completions of the order-2 locus and
nowhere off it, and fails to predict linearity at **320** of them. Only **48**
of the 384 reach $\mathrm{GL}(3,2)$, while $\mathrm{GL}(3,2)$ is reached at
**252** completions spread over defect orders $\{1, 2, 3, 4\}$ and at none of
order 5 or 6. Both those counts are relative to the declared wing symmetry
$P^*$: the three transpositions agree at 384/48, the two 3-cycles give 270/0.
The exclusivity of the visit is a property of the **lex-first selection rule**,
and no purely order-theoretic condition captures it — the finest one measured
still admits 432 false positives out of 768.

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
carry, and saying which object *can* carry them is most of the work. A fifth
question — declared in the instrument's source with both of its outcomes
before it was run, because the first question's degree-one answer means
nothing without it — is settled in §3.5: whether the degree-one classes of the
object that does carry that topology are an obstruction or a scope effect.

---

## 2. The foundation, the arena, and the declared objects

### 2.1 What is inherited and how

TB3's terminal receipt is hash-pinned and read as **data**. The base is then
rebuilt here from TB3's §2 declaration — the three-wing carrier of 64
configurations, the wing symmetry $P_\pi = \Sigma_\pi\otimes\Sigma_\pi$, the
three declared rotations, the preparation family, the lex-first-within-property
completion rule, and the two four-clause gluing rules — with **no import** from
the TB3 instrument. **196 anchors** are then gated exit-1, among them:

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
| the committed two-wing and three-wing transport graphs | 30 anchors (14 + 16) |
| the control complexes' standard invariants | 24 anchors |

The rebuild reproduces every one of them. Their provenance is printed in four
classes and never rounded up (§10): **168 external**, whose declared side is
read from the pinned receipt's bytes; **1 self-pin**, whose declared side is
the SHA-256 typed here and whose computed side is the hash of the foundation;
**3 declared-structural**, the transport controls' node counts, which TB3's
committed rows do not carry and which are therefore the declared size
$\lvert\text{frames}\rvert \times \lvert\text{checkpoints}\rvert$ — computed
from the declaration, incapable of failing, and named rather than counted as
evidence; and **24 declared-standard**, the control complexes' invariants.

### 2.2 The arena (RUNBOOK §15)

Inherited from TB3 verbatim: boundary the final division event (checkpoint 4);
family the 27 declared settings and 9 declared preparations, of which this unit
reads TB3's five declared A3 instances; law the exact Born law of the declared
leg sequence at the node's declared read time; state $p(0) = \delta_{j_0}$;
arena the declared relabelling scope and the subgroup surviving the $j_0$
filter. This unit adds **two** coordinates of its own, both load-bearing and
both declared as data.

The first is the **coordinate cell** of an identification, namely the pair
(checkpoint, rule), of which there are ten. It carries §3.

The second is the **declared wing symmetry $P^*$**, the first non-identity
element of the enumerated wing group — a transposition. The label defect
$d_P(q)$, the order-2 **locus** and the defect-order axis of §5's census are
all defined relative to it. $P^*$ is an arena coordinate and not a fact about
the base, so all five non-identity wing symmetries are swept and the dependence
is measured (§5.1).

### 2.3 The complexes and the auxiliary objects, declared before they are built

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
- **The digons and their coherence** (§3.5). Two charts drawn at two coordinate
  cells bound a digon on their two parallel 1-cells; the digon is **coherent**
  when the two drawn maps agree. The digons are not 2-cells of $N$ — they are
  the probe by which the declared scope is tested from outside.
- **The block-incidence graph $I_t$** (§3.3). Vertices the blocks of the two
  rules' partitions at checkpoint $t$; an edge for every block pair sharing a
  chart.
- **The automorphism candidates** (§4.2). The 36 left translations
  $(\sigma,\text{seed}) \mapsto (g\sigma, h\,\text{seed})$ of the chart set,
  each tested against the drawn relation at every coordinate cell.

Declared scope: 2-cells are same-checkpoint only, which is TB3's declared
census object. Cross-checkpoint triples lie outside this unit's complex and
nothing is claimed about them — but the *consequence* of that scope for degree
one is measured, in §3.5, rather than left as a scope declaration.

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
$N_{\mathrm{simp}}$ are exactly the subsets of those components. The measured
content is then that the **unique maximal face is the whole chart set**, at
every declared instance: 36 charts at four of them, the whole 6-chart set at
the equivariant control. That is what is gated, and a smaller maximal face
would break it. A complex with one maximal face is a simplex, hence a cone,
hence contractible: $N_{\mathrm{simp}} = \Delta^{35}$ and $\chi = 1$.

The alternating binomial sum $\sum_{k=1}^{n} (-1)^{k+1}\binom{n}{k}$ is
computed and printed beside it, but it is **not** a second route and is not
part of any predicate: it equals 1 for every $n \ge 1$, evaluated here at
$n = 1 \ldots 40$ with a one-element value set. It is a consistency print, and
is entered in the forced-clause disclosure of §5.2.

**The atlas has no simplicial-nerve topology.** That is a real answer to the
pin's first question, and it is the reason the rest of this section is about a
different complex. An object whose every overlap is total records nothing; what
records something is *where* the overlaps are.

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
  in reverse (5,261). These are two pivot disciplines on the same rank, and are
  described as that.
- **$\chi$**, two ways: from the geometric 2-cell set built by the $a<b<c$
  enumeration, and from the **ordered** census taken by the independent triple
  loop divided by the exact traversal multiplicity. These consume different
  data and are genuinely independent.

The traversal multiplicity is itself a gate rather than a constant: the ordered
census is measured to be **exactly six times** the geometric 2-cell count at
every instance — three rotations by two orientations — and a probe that removes
**one** geometric 2-cell is measured to break that relation. The agreement of
$\chi$ computed from the Betti numbers with $\chi$ computed from the cell
counts is an **algebraic identity in the ranks** and is recorded as a
disclosure, never as a route. So is $\partial_1\partial_2 = 0$: it holds for
every input here, because a 2-cell's three 1-cells are the three sides of a
triangle and their six endpoint bits cancel in pairs, and the guard that
evaluates it is a *sample* whose cap and denominator are both printed. The
argument, not the sample, is what carries it.

The drawn admission relation is measured **symmetric** at all ten coordinate
cells of all five instances, so the 1-cell census — which reads the ordered
entry with $a < b$ — does not depend on the chart indexing.

### 3.3 The first homology is the read times, what that measures, and what it does not

Every 1-cell and every 2-cell carries a definite checkpoint, so the five
checkpoint sub-complexes meet exactly in their shared 0-skeleton. For a union
glued along a discrete set $H_2$ is additive and the Euler characteristics add
with the 0-skeleton counted once, whence

$$b_1(N) \;=\; b_0(N) \;+\; (T-1)\lvert V\rvert \;+\;
\sum_t \bigl(b_1(N_t) - b_0(N_t)\bigr).$$

Every input on the right is a per-checkpoint elimination or a union-find count;
the global boundary elimination enters nowhere. The decomposition's own
hypothesis is **measured, not assumed**: $\sum_t b_2(N_t) = b_2(N) = 199{,}123$
at the reference instance, and likewise for the coherent sub-nerve — and a
mutant that drops one 2-cell from each sub-complex alone breaks it.

At the reference instance:

| checkpoint | 1-cells | 2-cells | $b_0$ | $b_1$ | $\chi$ |
|---|---|---|---|---|---|
| 0 | 1,260 | 57,120 | 1 | **0** | 55,896 |
| 1 | 1,260 | 57,120 | 1 | **0** | 55,896 |
| 2 | 828 | 16,512 | 1 | **0** | 15,720 |
| 3 | 828 | 16,512 | 1 | **0** | 15,720 |
| 4 | 1,260 | 57,120 | 1 | **0** | 55,896 |

so $b_1 = 1 + 144 + 0 - 5 = \mathbf{140}$, and the global elimination returns
140.

**What that number is.** Rearranging the same formula,
$b_1(N) - (T-1)(\lvert V\rvert-1) = \sum_t b_1^t - \bigl(\sum_t b_0^t -
T\bigr)$, so $b_1$ equals the pure **coordinate count** — read times minus one,
times charts minus one — exactly when the per-checkpoint excess matches the
per-checkpoint first homology. That equivalence is an identity, not a
measurement. The measured content of the degree-one claim is the
per-checkpoint census in the last two columns below, and nothing else:

| instance | $T$ | $\lvert V\rvert$ | $(T-1)(\lvert V\rvert-1)$ | $b_1$ | $\sum_t b_0$ | $\sum_t b_1$ |
|---|---|---|---|---|---|---|
| **the declared base, fully symmetric** | 5 | 36 | 140 | 140 | 5 | 0 |
| the equivariant-completion control | 5 | 6 | 20 | 20 | 5 | 0 |
| a partially symmetric setting | 5 | 36 | 140 | 140 | 7 | 2 |
| an asymmetric setting | 5 | 36 | 140 | **136** | 9 | 0 |
| a W-class preparation, fully symmetric | 5 | 36 | 140 | 140 | 7 | 2 |
| **the scrambled negative control** | 5 | 36 | 140 | **140** | 5 | 0 |

The last row is the point. A deterministic scramble that destroys the
identification data (§7.2) returns the same $b_1$, by the same mechanism, and
its own per-checkpoint census is computed rather than asserted. **The
degree-one invariant is insensitive to the identification data.** The
invariants that are not are $b_2$ — 199,123 → 81,748 under the same scramble —
and the coherent sub-nerve of §3.4.

**What a read time's own topology is.** At checkpoint $t$ the FULL rule and the
REALIZED rule each partition the charts into the components of their drawn
relation. The bipartite **block-incidence graph** $I_t$ joins two blocks that
share a chart, and its $b_0$ and cycle rank are measured equal to the
sub-nerve's $b_0$ and $b_1$ at **all 25** (instance, checkpoint) pairs — by
union-find and Euler alone, touching neither the sub-complex nor its
elimination:

| instance | $t$ | blocks (FULL, REALIZED) | $I_t$: $V$ | $E$ | $(b_0, \mathrm{cyc})$ | sub-nerve $(b_0,b_1)$ |
|---|---|---|---|---|---|---|
| the declared base, fully symmetric | 0, 1, 4 | (1, 1) | 2 | 1 | (1, 0) | (1, 0) |
| the declared base, fully symmetric | 2, 3 | (3, 1) | 4 | 3 | (1, 0) | (1, 0) |
| the equivariant-completion control | 0–4 | (6, 1) | 7 | 6 | (1, 0) | (1, 0) |
| a partially symmetric setting | 0, 1, 4 | (1, 3) | 4 | 3 | (1, 0) | (1, 0) |
| a partially symmetric setting | 2, 3 | (3, 3) | 6 | 5 | **(2, 1)** | **(2, 1)** |
| an asymmetric setting | 0, 1, 4 | (1, 6) | 7 | 6 | (1, 0) | (1, 0) |
| an asymmetric setting | 2, 3 | (3, 6) | 9 | 6 | **(3, 0)** | **(3, 0)** |
| a W-class preparation, fully symmetric | 0, 1, 4 | (1, 3) | 4 | 3 | (1, 0) | (1, 0) |
| a W-class preparation, fully symmetric | 2, 3 | (3, 3) | 6 | 5 | **(2, 1)** | **(2, 1)** |

So "every checkpoint sub-nerve has vanishing first homology" says exactly: **at
every read time the two block partitions are nested, their incidence graph a
forest.** At the reference because one rule always draws a single block; at the
asymmetric setting because the 6-block partition refines the 3-block one — and
it fails at the partially symmetric setting and the W-class preparation, where
neither partition refines the other, which is precisely the measured
$b_1 = 1$ at checkpoints 2 and 3. That is the exact statement of the read-time
claim, and it is the language the successor inherits.

### 3.4 Coherence costs cycles

A 2-cell of $N$ is **coherent** when its three drawn maps compose to the
identity. At the reference instance **84,720 of 204,384** are.

The count has **one route**, and the instrument says so rather than claiming
two. It is flagged while the cell is built. The ordered defect multiset's entry
at the identity, $6 \times 84{,}720 = 508{,}320$, is not an independent second
census of it: the three traversal defects of a 2-cell are conjugate,
$d_2 = p_1 d_1 p_1^{-1}$ and $d_3 = (p_2p_1) d_1 (p_2p_1)^{-1}$, measured at
every 2-cell of every instance, so the pattern $(d_1, d_2, d_3)$ is never mixed
— 84,720 cells all-identity and 119,664 none-identity at the reference — and
the identity entry is *identically* six times the coherent count. What the
second computation buys is not independence but an **external anchor**: the
multiset is gated exit-1 against TB3's committed receipt, so the coherent count
is pinned to bytes outside the instrument.

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
identity** — and they live *inside* single read times, which is what makes
$N_{\mathrm{coh}}$, not $N$, the object the successor should work in.

### 3.5 Do the drawn maps agree across coordinate cells?

The degree-one classes of $N$ compare read times because no 2-cell of $N$ is
permitted to carry edges from two checkpoints. That is a declared scope. The
question it leaves open is whether those classes are an **obstruction** —
whether the identification *drawn* between two charts at one read time differs
from the one drawn at another — or bookkeeping. It is decided by one
comparison, declared with both outcomes before it was run.

Two charts drawn at $k \ge 2$ coordinate cells carry $k$ parallel 1-cells and
$\binom{k}{2}$ digons; the digon census is gated complete against those
multiplicities. A digon is **coherent** when its two drawn maps agree, and a
pair **agrees** when all of its drawn maps do — computed twice, once from the
set of drawn maps and once from the digon flags, and gated equal at every pair.

| instance | pairs at $\ge 2$ cells | maps agree | disagree | digons | same-ck | cross-ck | coherent cross-ck | $b_1$ after filling them |
|---|---|---|---|---|---|---|---|---|
| **the declared base, fully symmetric** | 630 | 90 | **540** | 20,898 | 2,286 | 18,612 | 11,268 | **0** |
| the equivariant-completion control | 15 | 15 | 0 | 150 | 0 | 150 | 150 | **0** |
| a partially symmetric setting | 630 | 522 | 108 | 9,378 | 846 | 8,532 | 6,948 | **0** |
| an asymmetric setting | 630 | 630 | 0 | 6,318 | 450 | 5,868 | 5,868 | **0** |
| a W-class preparation, fully symmetric | 630 | 522 | 108 | 9,378 | 846 | 8,532 | 6,948 | **0** |

Three measured facts, and one conclusion.

**The same-checkpoint digons kill nothing.** All 2,286 of them add rank zero:
no degree-one class of $N$ compares two rules at one read time. Those cycles
are already filled from inside, by the triangles of the same checkpoint.

**The drawn maps do disagree.** At the reference instance 540 of the 630
multiply-drawn pairs carry at least two different drawn maps across their
cells. Disagreement is the rule here, not the exception.

**And the coherent digons alone fill everything.** Filling only the 11,268
cross-read-time digons *whose two drawn maps agree* already reduces $b_1$ from
140 to **0**. The disagreement, though abundant, is nowhere load-bearing: every
one of the 140 classes is killed by identifications that agree across read
times.

> `CROSS-CELL-COHERENT-DIGONS-FILL-EVERY-DEGREE-1-CLASS`

So the degree-one classes of $N$ are **not** a measured cross-read-time
obstruction; they are an artifact of the declared same-checkpoint 2-cell scope,
exactly as the coordinate-count identity of §3.3 suggested and as this section
confirms independently, at the level of the maps themselves. What the continuum
rung inherits from this base in degree one is therefore *nothing*: a trivial
$H_1$, joining the contractible simplicial nerve. The identification data is
carried by $b_2$, by the 21 intra-read-time classes of $N_{\mathrm{coh}}$, and
by the coherent 2-cell count — not by $b_1$.

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

The reading is `CONSISTENT` exactly when that triple is chart-independent.
**All three components are cross-checked**, each against a comparator that does
not route through the estimator: the per-cell dimension against a component
census run from the pair table alone; the star and the link against a second
pass that never touches the estimator's own construction and reads the link's
homology by **union-find and Euler** rather than by an $\mathbb F_2$ rank, with
the global identities $\sum_v \mathrm{star}_E(v) = 2\lvert E\rvert$ and
$\sum_v \mathrm{star}_F(v) = 3\lvert F\rvert$ gated beside it. Injecting the
star-and-link bug class into the atlas path alone — leaving the control path
untouched — is measured to die here.

### 4.2 What it returns, and whether returning it was a measurement

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

**And where it is uniform, uniformity is forced.** The estimator is a
chart-invariant of the drawn table, so if the drawn table has an automorphism
group transitive on charts then a chart-invariant *cannot* be chart-dependent
and `CONSISTENT` could not have come out otherwise. The declared automorphism
candidates — the 36 left translations
$(\sigma,\text{seed}) \mapsto (g\sigma, h\,\text{seed})$ — are each tested
against the drawn relation at every coordinate cell:

| instance | measured automorphisms of 36 candidates | chart-orbits | distinct estimator values | the reading |
|---|---|---|---|---|
| **the declared base, fully symmetric** | 36 | **1** | 1 | CONSISTENT — **forced, a disclosure** |
| the equivariant-completion control | 6 | **1** | 1 | CONSISTENT — **forced, a disclosure** |
| a partially symmetric setting | 12 | **3** | 2 | INCONSISTENT — **measured** |
| an asymmetric setting | 36 | **1** | 1 | CONSISTENT — **forced, a disclosure** |
| a W-class preparation, fully symmetric | 12 | **3** | 2 | INCONSISTENT — **measured** |

The reference instance's drawn table is chart-transitive — every
chart-invariant is chart-independent there by symmetry — so `CONSISTENT` at the
reference is a property of that instance's automorphism group and is entered as
a **disclosure**, not as a result. What is measured is the contrast: at the
partially symmetric setting and at the W-class preparation the table is **not**
chart-transitive, and the estimator splits the 36 charts **24 / 12**. (It is
coarser than the symmetry: three chart-orbits, two estimator values.) The
dimension profile is identical across the split; what differs is the star and
the link:

| | majority (24 charts) | witness (12 charts) |
|---|---|---|
| chart | `ABC\|ABC` | **`ABC\|ACB`** (W-class: **`ABC\|BAC`**) |
| dimprofile | $(35,11,35,11,11,11,11,11,35,11)$ | the same |
| star | $(182,\ 4{,}828)$ | $(182,\ 4{,}648)$ |
| link | $(35,\ 4{,}828,\ 1,\ 4{,}794)$ | $(35,\ 4{,}648,\ 1,\ 4{,}614)$ |

Every chart carries the same number of 1-cells and the same per-cell
dimensions; a third of them sit in **180 fewer 2-cells**. That contrast, and
not the reference instance's uniformity, is this section's measurement.

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
path that reads the atlas — and the atlas path and the control path carry
**separate** falsifiers, so a bug injected in one cannot die on the other.

---

## 5. Q3 — the Fano-rung selector

### 5.1 The candidate family, declared above every measurement — and the arena coordinate it is measured in

Thirteen candidate selectors are declared in the instrument's source above
every measurement, and the count of defect subgroups built at the moment the
declaration is registered is gated at **zero**. That records the ordering
*within one execution*; it is not offered as proof that the declarations were
fixed before any fixture truth was seen, which no in-run measurement can
establish — the process fact is the commit. Six candidates are labelled
`pin-derived`, meaning that they restate the pin's own order-2-locus language;
the pin contains no candidate list and none is claimed to.

Each candidate is a predicate $C(q)$ on a completion — a permutation of the
eight system-triple labels fixing label 0. $d_P(q) = \sigma_P^{-1}
q^{-1}\sigma_P q$ is the label defect and $K(q) = \langle d_P(q) : P \in S_3
\rangle$; "reference value" means the value the quantity takes at the
rule-selected ord-2 target, computed in the same run.

The three clauses, also declared in advance: **(a)** the candidate holds on the
whole defect-order-2 locus; **(b)** it holds nowhere off it; **(c)** it
predicts the linearity of the resulting geometry — zero completions satisfying
it whose $K(q)$ has a non-linear element. A candidate is NAMED only if all
three pass.

**The locus is $P^*$-relative.** The defect, the locus and the defect-order
axis are all defined against the declared wing symmetry $P^*$ (§2.2). All five
non-identity symmetries are swept:

| $P^*$ | type | locus | on the locus $K = \mathrm{GL}(3,2)$ | defect-order distribution |
|---|---|---|---|---|
| `ACB` (declared), `BAC`, `CBA` | transposition | **384** | **48** | 48/384/1728/1152/1152/576 |
| `BCA`, `CAB` | 3-cycle | **270** | **0** | 18/270/1080/1296/648/432, and **1,296 at order 7** |

The three transpositions agree exactly; the two 3-cycles agree with each other
and differ from them, and realise an order-7 defect that no transposition
does. So the 384 and the 48 that the verdict reports are coordinates, not
invariants, and the verdict's head says so. What is **not** $P^*$-relative is
$K(q)$ itself, and therefore the 252 completions at which it equals
$\mathrm{GL}(3,2)$ as a set.

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

Exhaustive over all **5,040** completions; the locus has **384**. Both tables
of this section are **emitted by the instrument** from the table it recorded,
markdown row by markdown row, and copied here verbatim: no cell is retyped. A
bold cell is a clause the candidate passed.

| id | candidate | (a) on the locus | (b) off it | (c) non-linear $K$ | holds at | of those $=\mathrm{GL}(3,2)$ | clauses |
|---|---|---|---|---|---|---|---|
| C1 | involutivity | **384/384** | **0** | 320 | 384 | 48 | 2 |
| C2 | defect fixed-point count | **384/384** | **0** | 320 | 384 | 48 | 2 |
| C3 | completion support | 40/384 | 275 | 288 | 315 | 6 | 0 |
| C3b | completion cycle type | 24/384 | 81 | 84 | 105 | 6 | 0 |
| C4 | defect $\mathbb F_2$-linearity | 64/384 | 272 | **0** | 336 | 252 | 1 |
| C4b | declared-symmetry defect linearity | 192/384 | 816 | 672 | 1,008 | 252 | 0 |
| C5 | completion $\mathbb F_2$-linearity | 32/384 | 136 | **0** | 168 | 126 | 1 |
| C6 | defect order profile | 16/384 | 32 | 36 | 48 | 12 | 0 |
| C7 | involutive profile | 12/384 | 8 | 6 | 20 | 0 | 0 |
| C8 | transvection | 192/384 | **0** | 128 | 192 | 48 | 1 |
| C9 | $q$ normalises the wing group | 0/384 | 12 | **0** | 12 | 0 | 1 |
| C10 | Fano collineation | 32/384 | 136 | **0** | 168 | 126 | 1 |
| C11 | abelian defect set | 20/384 | 130 | 126 | 150 | 0 | 0 |

**No candidate passes all three clauses; the best reach two of three.** That
tier is C1 and C2 — and they are the same predicate (below), so it is one
predicate, once. C8 is often grouped with them and does not belong there: it
holds nowhere off the locus but on only **192 of the 384** on it, so it fails
clause (a) as well as clause (c), reaching one of three. C7 passes **none** of
the three: 6 of the 20 completions satisfying it have a $K$ with a non-linear
element.

**Clause (c) is a containment, and its passers are forced.** This is the
section's main disclosure. For every one of the thirteen, clause (c)'s count is
measured to equal $\lvert C \setminus C4\rvert$ — so "clause (c) passes" is
literally $C \subseteq C4$, a set containment inside the declared family and
not a measurement about the geometry:

| id | holds at | clause (c) | $\lvert C\setminus C4\rvert$ | $C \subseteq C4$ |
|---|---|---|---|---|
| C1 | 384 | 320 | 320 | no |
| C2 | 384 | 320 | 320 | no |
| C3 | 315 | 288 | 288 | no |
| C3b | 105 | 84 | 84 | no |
| C4 | 336 | 0 | 0 | **yes** |
| C4b | 1,008 | 672 | 672 | no |
| C5 | 168 | 0 | 0 | **yes** |
| C6 | 48 | 36 | 36 | no |
| C7 | 20 | 6 | 6 | no |
| C8 | 192 | 128 | 128 | no |
| C9 | 12 | 0 | 0 | **yes** |
| C10 | 168 | 0 | 0 | **yes** |
| C11 | 150 | 126 | 126 | no |

And every passer's zero is forced by algebra, each forcing measured here as a
set containment rather than asserted. **C4** because a group generated by
$\mathbb F_2$-linear maps is $\mathbb F_2$-linear — the predicate is measured
*equal as a set* to $\{q : K(q) \subseteq \mathrm{GL}(3,2)\}$, 336 for 336.
**C5** and **C10** because all six $\sigma_P$ are measured $\mathbb F_2$-linear,
so $d_P = \sigma_P^{-1}q^{-1}\sigma_P q$ is linear whenever $q$ is. **C9**
because $q$ normalising the wing group puts every $d_P$ inside it, and the wing
group is linear. Clause (c) therefore separates nothing that clauses (a) and
(b) had not already separated — which *strengthens* the negative verdict, since
the clause turns out to be incapable of naming a selector on its own. Clause
(c) is separately bounded, inside its gate, by a count taken outside the
candidate loop: no candidate's linear sub-count may exceed the 336 completions
in the whole family whose $K$ is linear.

**Two extensional collapses, both measured, both disclosed.** **C1 ≡ C2**: a
defect at $P^*$ has exactly four fixed labels precisely when it has order 2,
measured 384-for-384 and 0-for-0. **C5 ≡ C10**: over the prime field a
permutation of $\mathbb F_2^3$ fixing 0 maps every line of $\mathrm{PG}(2,2)$
onto a line exactly when it is $\mathbb F_2$-linear, so the collineation group
of the Fano plane *is* $\mathrm{GL}(3,2)$ — measured identical as sets, and
identical in all five columns above. The thirteen declared names are
**eleven distinct predicates**, and the search's denominator is that eleven.

### 5.3 What actually selects the visit

$\mathrm{GL}(3,2)$ is reached — as a **set**, not an order — at **252** of the
5,040 completions, distributed over the defect order at $P^*$ as

| $\mathrm{ord}[P^*,u]$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| completions with $K = \mathrm{GL}(3,2)$ | 4 | **48** | 72 | **128** | **0** | **0** |

Four things follow, all measured.

**The locus is not sufficient.** 48 of 384 is one in eight.

**The locus is not necessary.** 204 of the 252 lie off it, most of them at
defect order 4.

**The order constrains through the element spectrum, and the two exclusions
cost different amounts.** The element orders of $\mathrm{GL}(3,2)$ are measured
to be $\{1,2,3,4,7\}$; $d_{P^*}(q)$ lies in $K(q)$, so
$\mathrm{ord}[P^*,u] \in \{5,6\}$ makes $K \subseteq \mathrm{GL}(3,2)$
impossible, and the measured zeros at orders 5 and 6 — 1,728 completions — are
that necessary condition biting. Order 5 is Lagrange-immediate: $5 \nmid 168$.
Order 6 is **not** — $6 \mid 168$ — and needs the actual element-order spectrum
of $\mathrm{GL}(3,2) \cong \mathrm{PSL}(2,7)$, which has no element of order 6.

**But no order-theoretic condition captures the visit, at any refinement.**
The $P^*$ condition is not the finest available, and the ladder is measured:

| purely order-theoretic condition | completions passing | false positives vs $K\subseteq\mathrm{GL}(3,2)$ |
|---|---|---|
| $\mathrm{ord}[P^*,u]$ lies in $\mathrm{GL}(3,2)$'s spectrum | 3,312 | 2,976 |
| the whole $S_3$ defect-order profile lies in the spectrum | 1,176 | 840 |
| every element order of $K$ itself lies in the spectrum | 768 | 432 |

Each level is measured to contain all 336 completions with
$K \subseteq \mathrm{GL}(3,2)$ and all 252 with equality, and each is strictly
smaller than the last — the condition tightens by a factor of more than four
while staying purely order-theoretic. And the finest of them still admits
**432** false positives out of 768. Linearity does irreducible work, and
linearity is not read off orders.

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
four. On five instances they look like selectors; on 5,040 they are not. This
is the same shape of honesty TB3's own §5.2 records about its centraliser
criterion: a five-row comparison cannot separate hypotheses that a full census
separates immediately.

TB3's reading — "the ord-2 target is the completion at which the geometry sees
the substrate's own linear group and no more" — is scoped in its own text to
its rule-selected targets and is **not contradicted**: over those five rows the
definite description is unique. What this unit adds is where the exclusivity
comes from: the lex-first rule, applied at order 2, happens to return the
transvection $(s_A,s_B,s_C)\mapsto(s_A,s_B,s_C\oplus s_A)$, which is
$\mathbb F_2$-linear. Linearity of the completion, not the order of its defect,
is what puts $K$ **inside** $\mathrm{GL}(3,2)$ — and containment is all it
buys: of the 168 linear completions, 126 reach $\mathrm{GL}(3,2)$ and 42 do
not, and on the locus "q linear" and "$K = \mathrm{GL}(3,2)$" are different
sets (32 linear, of which 24 reach it; a further 24 non-linear completions also
reach it, making the 48). What supplies *equality* at this particular $q$ is
not measured here.

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

Burnside divides by a group order with a floor, so the census that feeds it is
pinned two further ways: the fixed-cell sums are measured **exactly** divisible
by 6 in all three dimensions — the residues are printed and are zero — and the
orbit-size histograms are gated against the cell counts. Orbit sizes: 816 free
1-cell orbits of size 6 and **180 of size 3**, recovering
$816\cdot6 + 180\cdot3 = 5{,}436$; 34,044 free 2-cell orbits of size 6 and
**60 of size 2**, recovering $34{,}044\cdot6 + 60\cdot2 = 204{,}384$.

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

**The boundary's Boolean connective is gated by its own delta.** A boundary row
is assembled by XOR, so a 1-cell whose two endpoints coincide contributes zero.
On the nerve that is inert — every 1-cell joins two distinct charts — and the
convention bites exactly here: the quotient's 1-skeleton is measured to carry
**240** loop 1-cells, so the convention is exercised by construction. Both
connectives are evaluated on the same quotient:

| assembly | rank $\partial_1$ | $b_0$ | $b_1$ |
|---|---|---|---|
| **XOR** (the mod-2 boundary, as delivered) | 5 | 1 | **25** |
| OR (an incidence bit pattern) | 6 | 0 | **24** |

The measured delta is 1, and the delivered assembly is the XOR one. An OR
regression is caught twice over: here, and by the quotient's **four** component
routes — union-find, the boundary rank, the *transposed* rank, and a spanning
forest — the transpose route being the one only a complex with loops can
exercise, and the one without which a quotient could publish a component count
of zero for a non-empty complex.

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
| 3 | `(0,1,3,2)` | **8** | **13** | **7** | **6** | 6 |

What that anchors is the **1-dimensional** route and only it: nodes, links,
identification links and cycle rank are each anchored exit-1 against committed
bytes. The last column is *not* a second anchor. The control graph carries no
2-cells, so $\operatorname{rank}\partial_2 = 0$ and $b_1$ equals the cycle rank
identically; the identity is printed rather than counted, on deviation 3's own
standard. **No committed number anchors $\operatorname{rank}\partial_2$
anywhere in this unit.** The 2-dimensional half of the homology machinery — the
elimination that produces 5,261, 199,123 and therefore 140 — is calibrated by
the declared-standard control complexes of §4.3 alone, which buy calibration
and not independence.

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
is `INCONSISTENT` with a named witness. The `scramble-off` mutant, which leaves
the atlas alone, dies on this gate, which is what shows those two clauses are
measurements and not restatements.

Two invariants do not move, and *why* is measured rather than narrated. The
scrambled atlas's own per-checkpoint census is taken: five read times, each
with $b_0^t = 1$ and $b_1^t = 0$ (1-cells and 2-cells 944/23,972; 944/24,174;
620/6,718; 620/6,703; 944/24,078). So $\sum_t b_0 = 5$ and $\sum_t b_1 = 0$,
and the gluing formula pins $b_1 = 1 + 144 + 0 - 5 = 140$ at the scrambled
atlas by exactly the mechanism that pins it at the reference. This is not a
weakness of the control; it is the control's most informative output, and §3.3
reads it as such: $b_0$ and $b_1$ are the invariants the gluing formula ties to
the checkpoint count and the chart count, and they cannot see the
identification data. The control's teeth are in the other five columns.

---

## 8. The verdict

Three verdicts, each with its restrictions in its own head and every number in
head and body alike interpolated from a measured count:
`TOP-GLOBAL-STRUCTURE-OF-THE-COORDINATE-RESOLVED-NERVE-DEGREE-1-IS-THE-COORDINATE-COUNT-4x35-UNMOVED-BY-THE-SCRAMBLE`,
with the tables of §3.2, §3.3 and §6.3;
`TOP-MANIFOLD-READING-CONSISTENT-AT-3-OF-5-INSTANCES-DIMENSIONS-11-AND-35-LINKS-NEVER-CIRCLES-AND-SYMMETRY-FORCED-AT-THE-REFERENCE`,
with the tables of §4.2; and
`TOP-FANO-SELECTOR-NOT-FOUND-THE-LOCUS-IS-P-STAR-RELATIVE-TRANSPOSITION-CLASS`,
with the family's failure computed clause by clause. Each string is **rebuilt
inside a gate from the recorded tables and compared byte-for-byte** with the
emitted one — not by a prefix — and three typed-qualifier mutants, one per
verdict, move a single computed qualifier of the emitter while every recorded
table keeps its measured value, and die. A fourth pre-registered outcome,
`CROSS-CELL-COHERENT-DIGONS-FILL-EVERY-DEGREE-1-CLASS`, is re-derived inside
its gate from the measured residual; its other branch is representable and a
mutant emits it.

The one sentence the unit will defend:

> The atlas's overlaps are total, so its nerve carries no topology; what
> topology it has lives in the coordinate at which an overlap is drawn, and at
> the declared base its first homology is not an obstruction at all — of the
> full complex $N$ that degree-one rank is the coordinate count
> $(T-1)(\lvert V\rvert - 1)$, unmoved by a scramble that destroys the
> identification data, and the digons whose drawn maps *agree* across read
> times already fill every one of its classes. What does see the
> identifications is degree two, and the coherent sub-nerve, where twenty-one
> classes live inside single read times. Its local reading is uniform across
> charts wherever the drawn table is chart-transitive, which is where the
> uniformity is forced, and is never a manifold's. And the ladder's Fano rung
> is picked out by the selection rule that chose it, not by the order-2 locus
> it sits in — a locus which is itself a coordinate of the declared wing
> symmetry.

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
- $N$ is **not a nerve** and its homology is not licensed by the nerve lemma.
  It is a presentation of the identification data indexed by (pair, checkpoint,
  rule); the nerve lemma applies to $N_{\mathrm{simp}}$, which is contractible
  and says nothing. The parallel-1-cell convention is TB3's and is
  load-bearing: collapsing the parallel 1-cells to one edge per pair gives the
  simple graph $K_{36}$, for which $b_1 = 0$.
- **$b_1 = 140$ is a coordinate count.** It is $(T-1)(\lvert V\rvert - 1)$
  whenever each read time is connected and simply connected; the scrambled
  control returns it too. It is not evidence of structure in the
  identification data, and §3.5 measures that no degree-one class survives the
  coherent cross-read-time digons.
- The 2-cells of $N$ are **same-checkpoint** triangles, TB3's declared census
  object. Cross-checkpoint triples are outside this complex. The digons of §3.5
  are a probe of that scope, not cells of $N$.
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
- The **order-2 locus and the on-locus count are $P^*$-relative** (§5.1). The
  252 completions reaching $\mathrm{GL}(3,2)$ as a set are not.
- `CONSISTENT` in the manifold verdict means **uniform across charts**. It does
  not mean one dimension across coordinate cells (it is not: 11 and 35 both
  occur), it does not mean manifoldhood (it is not: no link is a circle), and
  at the three instances whose drawn table is chart-transitive it is **forced**
  and is entered as a disclosure rather than a result.
- The dimension estimator is **extensive**: $\mathrm{dimprofile}$ is an overlap
  component's size minus one, so $\{11,35\} = \{12-1,\ 36-1\}$, and the same
  estimator reads 3 at the two-wing atlas's complete cells and 35 at three
  wings. It cannot converge under refinement, and the simple overlap graph
  being $K_{36}$ means there is no locality for a local invariant to measure.
  Both are inputs to the successor, not claims of this unit.
- The unit decides nothing about the cocycle criterion, the dihedral law, the
  ladder's group names, or any TB3 verdict; TB3's terminal numbers are inputs
  here and every one of them is reproduced.

---

## 10. The receipt

| | |
|---|---|
| anchors | **196**, all passing — **168 external** (TB3's hash-pinned receipt), **1 self-pin**, **3 declared-structural**, **24 declared-standard** |
| gates | **41** — 38 must-pass, 3 disclosures |
| must-pass failures | **0** |
| mutants | **44**, every one exits 1 and names a falsified gate or anchor; none crashed before reporting |
| must-pass gates never falsified by any mutant | **EMPTY** |
| falsified by a **computation** mutant | 34 of 37 |
| falsified only by a **waiver** | 3, named: `TOP-EXACTNESS`, `TOP-NO-MUTANT-EXEMPTION`, `TOP-ANCHOR-PROVENANCE` |
| the gate excluded from its own denominator | `TOP-FALSIFICATION` |
| determinism | two full delivery runs, **byte-identical** |
| exactness | AST sweep: **no float literal**; integers, `Fraction`s and integer XOR only |
| mutant-identity exemptions | AST sweep: **none** |

The two denominators are reported because they differ. A waiver registers a
value in a gate's own evidence list after that gate's sweep has run; it proves
the gate's predicate is load-bearing for the exit code and nothing more, and
the three gates carried by a waiver alone are named rather than averaged away.
`TOP-ANCHOR-PROVENANCE` is one of them by construction: it is a *vocabulary*
check — every anchor names a declared provenance class — and its only falsifier
registers a bad label after the sweep, so it is classified as a waiver and not
as a computation mutant.

---

## Appendix: deviations

1. **Three complexes, not one.** The pin says "the nerve as a cell complex".
   The genuine simplicial nerve at this atlas is a full simplex and carries no
   invariants, so the unit declares three objects — the simple overlap graph,
   the simplicial nerve, and the coordinate-resolved nerve — and makes the
   third primary. The first two are computed and reported, not discarded. The
   primacy was designated *after* the alternatives were measured empty, which
   is the forking-paths shape; the mitigation is that all three are declared,
   computed and reported, and that the chosen object's headline invariant is
   disclosed as forced non-zero by the same scope decision (deviation 2).
2. **2-cells are same-checkpoint.** TB3's census object. Cross-checkpoint
   triangles would be a different complex and are outside scope. That scope is
   also what makes the first homology temporal: no 2-cell of $N$ carries edges
   from two checkpoints, so every cycle comparing two read times is unfillable
   *by declaration*, and $b_1 \ge (T-1)(\lvert V\rvert - 1)$ before any
   measurement is taken. What is measured is the residual $\sum_t b_1(N_t)$,
   and — §3.5 — that filling only the coherent cross-read-time digons kills
   every class the scope creates.
3. **$\chi$ from Betti numbers is not a second route.** It is an algebraic
   identity in the ranks and is recorded as a disclosure. The second route to
   $\chi$ is a second **enumeration**. The same standard is applied to the
   simplicial nerve's alternating binomial sum (= 1 for every $n$; the measured
   clause is the maximal face size), to $\partial_1\partial_2 = 0$ (true here
   for every input; the sample cap is printed), to the two-wing control's $b_1$
   (= the cycle rank identically, with no 2-cells), and to the conjugacy of a
   2-cell's three traversal defects (which is why the coherent count has one
   route, §3.4).
4. **The $b_1$ second route uses a decomposition theorem.** $H_2$ additivity
   over the checkpoint pieces is what licenses it; the instrument **measures**
   that additivity rather than assuming it, at every instance and for the
   coherent sub-nerve as well, and a declared mutant that drops one 2-cell from
   each sub-complex alone makes it false. A third route — the block-incidence
   graph of §3.3 — reproduces the per-checkpoint $b_0$ and $b_1$ with no
   elimination anywhere.
5. **The quotient is a chain-level object** (§9); the non-freeness is measured
   and printed, and the mod-2 boundary convention carries a parity gate whose
   death certificate is the measured OR-vs-XOR delta (§6.3).
6. **The manifold verdict is read at the reference instance.** It is measured
   to fail at two of the five declared instances, and those instances and their
   witnesses are reported in the same table. Where the drawn table is
   chart-transitive the positive branch is forced and is entered as a
   disclosure (§4.2).
7. **Clause (c) has no measured content.** Its count is $\lvert C\setminus
   C4\rvert$ for every candidate, so it passes exactly when $C \subseteq C4$,
   and all four passers are analytically forced — C4, C5, C10 and C9, each
   forcing measured as a set containment (§5.2). The declared thirteen names
   carry eleven distinct predicates: C1 ≡ C2 and C5 ≡ C10, both measured
   extensionally identical and both disclosed.
8. **The scrambled control moves 4 of 7 invariants.** $b_0$ and $b_1$ do not
   move; the reason is **measured** — the scrambled atlas's own per-checkpoint
   census (§7.2) — rather than the control being re-tuned until they did.
9. **Three gates are falsified only by waivers** (`TOP-EXACTNESS`,
   `TOP-NO-MUTANT-EXEMPTION`, `TOP-ANCHOR-PROVENANCE`). The first two are of
   the AST-sweep kind, whose mutation cannot be injected in a computation
   without editing the source the sweep reads; the third is a vocabulary check
   whose only mutation registers a label after its sweep. Declared, named, not
   averaged.
10. **The manifold controls are DECLARED-STANDARD anchors** and the transport
    controls' node counts are DECLARED-STRUCTURAL. Their declared sides come
    from this source or from the declared base rather than from committed
    bytes; they buy calibration, not independence, and the provenance table
    prints them in their own classes rather than inside the external count.
11. **$P^*$ is an arena coordinate**, declared as data in §2.2 and swept in
    §5.1. The verdict's locus counts are scoped to the transposition class.
12. **Lean: NONE**, per the pin.
