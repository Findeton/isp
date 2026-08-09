# R2 — the manifold rung

**Status:** `GREEN-UNREVIEWED` — delivered 2026-08-09; v14 ledger entry
pending. Independent verification and the hostile panel have not run.

## Locality Can Be Declared Into Existence, and Nothing Follows From It

**Unit:** R2 (the manifold rung), v14.
**Pin:** `v14/note-r2-manifold-pin.md`, sha256-12 `76d42dfbc900` (v14 ledger
#11), verified at run time by gate `A-PIN-R2`.
**Instrument:** `v14/code/r2_manifold_exact.py`.
**Artifacts:** `v14/code/r2_manifold_output.txt`,
`v14/code/r2_manifold_receipt.json`.
**Inheritance, hash-verified at run time and by no other route:** R0 row I6
(`v13/code/tb3_third_base_receipt.json`, `c9bc956fe751`) supplies the block —
the eight system-triple labels, the ×7 embedding witness, the declared
completion transposition; R0 row I3 (`v13/code/top_topology_receipt.json`,
`65bb1fc5231f`, with the v14 LOG #4 erratum's companion
`v13/paper-top-topology.md` = `379194959fbc`) supplies the nerve, link and
dimension definitions, reimplemented here and imported from nowhere; the R1
joint adjudication (`v14/note-r1-adjudication.md`, `4115dcd83cfa`) supplies
the criterion, the recipe and the null. Five anchors, five gates.
**Exact arithmetic only:** integers and `Fraction`; an AST scan of the
instrument's own source is the first gate.

**The verdict, quoted exactly as the instrument emits it.** Every segment is
derived inside a gate from measured counts and the complete string is compared
for equality against a segment-by-segment rebuild:

```
R2-LOCALITY-AT<RULES=14-OF-109:R005,R008,R011,R030,R033,R036,R048,R051,R063,
R066,R088,R091,R106,R109|GRID=T4:G0=1;G1=2;G2=24;G3-ORBITS=7;G3-UNIONS=24|T7:
G0=1;G1=1;G2=18;G3-ORBITS=7;G3-UNIONS=24|TOTAL=109|MECHANISM=DECLARED-PARTIAL-
COSET-OVERLAP(CLASSES=G2+G3-UNIONS;MODES=SLIDING)|COMPONENTS=NONCOMPLETE-
COMPONENT-SIZES=4+7;RULES-WITH-NONTRIVIAL-B1=9|STANDARDS=LINK-CIRCLES=1-OF-80-
CHARTS;DIMREAD=INCONSISTENT;LOCAL-DIMENSIONS=1+2+3;DIMPROFILE=EXTENSIVE-
EXCLUDED|B2-PERSISTENCE=SURVIVES-AT-14-OF-14;COMPONENTS-DOUBLE-AT-14|NULL=G0-
CLIQUE-ONLY-AT-4-OF-4;ORBIT-PARTITION-CLASSES-CLIQUE-ONLY-AT-38-OF-38(R2-A-
VERIFIED-10-UNIT-ACTIONS-AND-40320-SWEPT-ACTIONS-0-COUNTEREXAMPLES)|REFUSES=5-
OF-109|BLOCK-CONSTANTS=DENSITIES-CONSTANT-B-TO-B2-AT-109-OF-109;UNDEFINED-B2-
DENSITY-AT-28>
```

(The line breaks are typographical; the emitted string is one line, and the
gate compares that line.)

**Declared scope.** At the single block **B** — TB3's native 8-label arena via
I6 — and at **B₂** — two isomorphic blocks plus an isolated basepoint — over
an exhaustively enumerated declared atlas grid of **109** rules at **two**
declared transports. Nothing outside that grid is measured, and the grid is
itself a named coordinate of the verdict.

---

## 1. What the rung asks, and what it inherits

The R1 adjudication left the manifold rung **not an arena but a criterion and
a recipe**. The criterion: *locality exists at a rule iff some connected
component of that rule's overlap graph is not complete.* Measured across R1's
whole family it returned nothing — componentwise overlap completeness was 1 at
every member and both probes. The recipe, theorem R2-A: with regular-orbit
drawing the overlap graph is always a union of cliques, so locality can only
be earned by declaring cells whose orbits overlap **partially**. The null: the
regular-orbit atlas, guaranteed clique-only.

R2 therefore starts at **atlas design**. Its question, falsifiable and
two-sided:

> Does any drawing rule in a declared finite grid of atlas declarations
> produce a component with a non-complete overlap graph — and where locality
> appears, what do the ported standards measure?

Both heads are first class and both are reachable by the derivation
(`G-VERDICT-BOTH-HEADS-REACHABLE`): `R2-NO-LOCALITY-IN-THE-DECLARED-GRID` is
as good a delivery as `R2-LOCALITY-AT`, and two flip mutants prove the
instrument can emit either.

The copy-forcing theorem says per-block structure carries all content, so R2
works at the block, not the tower. That reduction is **verified, not assumed**
(`G-COPY-REDUCTION`), on every rule of the grid.

---

## 2. The arenas, the transports and the grid — declared as data

Everything in this section is printed by the instrument, matched against its
computed value at every coordinate, and gated (`G-ARENA-DECL-MATCHED`,
`G-BLOCKSIZE-FROM-I6`, `G-GROUP-CAP`, `G-GRID-CELL-COMPLETE`).

### 2.1 The arenas

- **B** — the single block: the 8 system-triple labels $\{0,\dots,7\}$ of I6's
  declared carrier. The block size is *read* from I6
  (`base_declaration.carrier.system_triple_dimension`), never typed.
- **B₂** — two isomorphic copies of B (labels 0–7 and 8–15) plus an isolated
  basepoint (label 16), 17 labels. The rule is applied **block-locally**: a
  rule's cells are copied into each block and the basepoint lies in no cell.
  Transports never cross blocks.

The full-tower members are not rebuilt; the copy-forcing reduction that makes
them redundant is the object of `G-COPY-REDUCTION` rather than an assumption.

### 2.2 The transports

The transport is arena data with two declared values, each read from I6 by an
exact path:

| name | γ | order | source in I6 |
|---|---|---|---|
| **T7** | `(0,2,3,4,5,6,7,1)` — the 7-cycle on the seven non-zero labels | 7 | `tables.the_ladder.the_embedding.the_witness_system_part`, the ×7 = [A₇:A₆] embedding witness |
| **T4** | `(0,1,3,4,5,2,7,6)` = (2 3 4 5)(6 7) | 4 | `tables.ord_census.lex_first_Q_per_order['4']`, the lex-first completion permutation at defect order 4 |

Σ is the same at both: `(0,3,2,1,4,5,6,7)` = (1 3), I6's
`tables.arena.the_declared_completion_transposition`. The drawing group is
$\langle\gamma\rangle$ throughout; $\langle\gamma,\Sigma\rangle$ has order
5040 at T7 and 240 at T4 and is used only to generate cells.

Two transports rather than one because the transport is a *declaration*: a
census that holds at one and not the other would be a declaration artefact.
Both are printed; the census is reported at both; the verdict names both.

### 2.3 The drawing relation

Identical to R1's, so that the **only** variable across the grid is the
declared cell structure:

> $(a,b)$ is **drawn** iff exactly one transport element carries $a \to b$,
> and $a,b$ lie in a common declared cell.

### 2.4 The grid

Cells are orbit-type sets. For a subgroup $H$ the *cosets* are $H$'s orbits on
the labels, ordered canonically by minimum label; a **mode** says how cosets
are bunched into cells:

- `ALL` — every $c$-subset of cosets is a cell;
- `BLOCKWISE` — disjoint consecutive windows of $c$ cosets;
- `SLIDING` — every cyclic window of $c$ consecutive cosets.

The four declared classes:

| class | cells |
|---|---|
| **G0** (the null) | the $\langle\gamma\rangle$-orbits |
| **G1** | the $H$-orbits, for every proper $H<\langle\gamma\rangle$ of the complete cyclic subgroup lattice |
| **G2** | unions of $c\ge 2$ $H$-cosets, for every $(H,c)$ with $c\cdot|H| <$ block size, in every mode |
| **G3** | the same two constructions with cells taken from the **declared** subgroup lattice of $\langle\gamma,\Sigma\rangle$ (the cyclic subgroups of the declared words `e, g, s, gs, sg, ggs, gsgs`, plus the whole group) |

Enumerated exhaustively: **109 rules** (T7: 1 + 1 + 18 + 7 + 24; T4: 1 + 2 +
24 + 7 + 24). The enumeration is checked against an independently rebuilt
coordinate set constructed by divisor arithmetic that touches none of the
enumerator's own code (`G-GRID-CELL-COMPLETE`, `G-GRID-NO-DUPLICATES`); a
silently dropped $(H,c,\text{mode})$ triple is fatal, and the mutant
`grid-drop` proves it. There is **no cap**: `G-GRID-NOT-TRUNCATED` gates that
the enumerated size equals the declared size.

Every rule is measured at both arenas and every result is recorded. A rule
whose relation draws nothing is recorded **REFUSES**, never skipped
(`G-EVERY-RULE-RECORDED`, mutant `refuses-skip`); five rules refuse.

---

## 3. Three theorems, proved and verified in unit

### 3.1 Theorem R2-A, at this family's actions

> **Theorem R2-A.** Let a finite group $T$ act on a label set $L$ and admit
> $(a,b)$, $a\neq b$, iff exactly one $\pi\in T$ has $\pi(a)=b$. Then
> $\{\pi : \pi(a)=b\}$ is empty or a coset of $\mathrm{Stab}(a)$; so it is a
> singleton iff $\mathrm{Stab}(a)=1$ and $b\in \mathrm{orbit}(a)$. Hence
> $(a,b)$ is drawn **iff $b$ lies in $a$'s orbit and that orbit is regular**,
> $|\mathrm{orbit}(a)|=|T|$, and the drawn relation is the disjoint union of
> **complete** graphs on the regular orbits.

*Proof.* If $\pi(a)=\rho(a)=b$ then $\rho^{-1}\pi\in\mathrm{Stab}(a)$, so the
solution set is $\pi\,\mathrm{Stab}(a)$, of size $|T|/|\mathrm{orbit}(a)|$ by
orbit–stabiliser. Uniqueness is exactly $|\mathrm{orbit}(a)|=|T|$, a property
of the orbit, not of the pair; so within a regular orbit every ordered pair is
drawn and outside one none is. ∎

*Verification.* The instrument computes the drawn relation twice by genuinely
independent routes — orbit/stabiliser, and brute force over the group elements
— and gates their agreement at every rule and arena
(`G-DRAW-TWO-ROUTES`, 218 measurements). Beyond that, R2-A is checked at
**10** cyclic actions this unit uses and swept over **every** cyclic action on
the block's eight labels — one per permutation, **40,320 actions, 0
counterexamples** (`G-R2A-AT-THIS-UNITS-ACTIONS`, `G-R2A-EXHAUSTIVE`). The
mutant `orbit-corrupt`, which perturbs the regularity test, dies on the
two-route gate.

### 3.2 The partition corollary — why the null cannot fail

> **Corollary (R2-partition).** An atlas whose cells *partition* the labels
> can never produce a non-complete component.

*Proof.* Each cell lies inside one $T$-orbit or meets several; the drawn pairs
inside a cell are exactly the pairs of that cell lying in a common regular
orbit, so each cell contributes a clique on each of its regular-orbit slices.
Distinct cells of a partition share no label, so distinct cliques share no
vertex, and the components of the union are the cliques themselves. ∎

Measured: **G0 clique-only at 4 of 4** rules, and the whole orbit-partition
family — G0, G1 and G3-ORBITS together — **clique-only at 38 of 38**
(`G-R2A-NULL-CLIQUE-ONLY`, `G-ORBIT-CLASSES-CLIQUE-ONLY`). The mutant
`locality-inject` dies here.

### 3.3 The coherence corollary — a forced clause, entered as a disclosure

> **Corollary (R2-A-coherence).** For any 2-cell of $N$ the three drawn maps
> compose to the identity; $N_{\mathrm{coh}} = N$ identically.

*Proof.* $m_{ca}\circ m_{bc}\circ m_{ab}$ fixes $a$; a drawn pair forces
$\mathrm{Stab}(a)=1$ by R2-A; so the composite is the identity. ∎

This is true by algebra for every input, so per RUNBOOK §14 (#208) it is a
**disclosure**, not a claim of measurement. It is nevertheless verified at all
218 measurements (`G-COHERENCE-FORCED`) — and the scramble control (§7.3)
shows the coherence instrument is not vacuous: perturbing the drawn maps moves
the coherent 2-cell count at 81 of 81 rules of the declared tested set.

A consequence worth stating plainly: **the identification data this scale
carries is not in the cocycle condition.** Under the R1 drawing relation the
cocycle is free.

---

## 4. The locality census — the unit's core result

The criterion is applied at every rule at B. The full 109-row table is in
`r2_manifold_output.txt` §4 and in the receipt's `census_rows`; the shape of
it:

| class | rules at B | clique-only | REFUSES | **non-complete** |
|---|---|---|---|---|
| G0 | 2 | 2 | 0 | 0 |
| G1 | 3 | 1 | 2 | 0 |
| G2 | 42 | 37 | 0 | **5** |
| G3-ORBITS | 14 | 11 | 3 | 0 |
| G3-UNIONS | 48 | 39 | 0 | **9** |
| **total** | **109** | **90** | **5** | **14** |

**Fourteen of 109 rules produce a component that is not complete.** Every one
of them is a `SLIDING` rule; every `ALL` and every `BLOCKWISE` rule in the
grid returns clique-only, as does every orbit-partition rule. Locality appears
at both transports and in both union classes:

| rule | transport | H | c | component | drawn / possible pairs | completeness |
|---|---|---|---|---|---|---|
| R005 / R030 | T7 | trivial | 2 | 7 | 6 / 21 | 2/7 |
| R008 / R033 | T7 | trivial | 3 | 7 | 12 / 21 | 4/7 |
| R011 / R036 | T7 | trivial | 4 | 7 | 18 / 21 | 6/7 |
| R048 | T7 | ⟨Σ⟩ | 2 | 7 | 7 / 21 | 1/3 |
| R051 | T7 | ⟨Σ⟩ | 3 | 7 | 14 / 21 | 2/3 |
| R063 / R088 | T4 | trivial | 2 | 4 | 3 / 6 | 1/2 |
| R066 / R091 | T4 | trivial | 3 | 4 | 5 / 6 | 5/6 |
| R106 | T4 | ⟨Σ⟩ | 2 | 4 | 3 / 6 | 1/2 |
| R109 | T4 | ⟨Σ⟩ | 3 | 4 | 5 / 6 | 5/6 |

Two non-complete component sizes occur: **7** (T7's regular orbit) and **4**
(T4's). In every case the non-complete component is exactly the transport's
regular orbit, and the missing pairs are the pairs no cyclic window of length
$c$ can cover.

**The mechanism, named.** Locality is produced by *declared partial coset
overlap* and by nothing else. `SLIDING` is the only declared mode whose cells
overlap without nesting; `BLOCKWISE` partitions, and `ALL` puts every pair of
cosets into a common cell and so restores the whole clique. Where the sliding
window becomes long enough to cover every pair — measured at $c\ge 5$ for T7
and $c\ge 4$ for T4, in the trivial-subgroup sliding family — the locality disappears again and the rule returns
clique-only. Locality here is a window-width effect, exactly and only.

**The census is measured, not asserted.** Completeness is computed twice, from
the stored edge count and from an explicit pair scan
(`G-COMPLETENESS-TWO-ROUTES`); components twice, by union–find and by
$|V|-\operatorname{rank}\partial_1$ over $\mathbb F_2$
(`G-COMPONENTS-TWO-ROUTES`). Mutants `census-corrupt` and `complete-flip` die
on those gates.

---

## 5. What the ported standards say where locality exists

I3's estimator is reimplemented from its written definition and imports
nothing: for a chart $X$, $\mathrm{dimprofile}(X)$ over the rule's coordinate
cells (the local simplex dimension $|{\rm component\ of\ }X{\rm\ at\ }c|-1$,
recorded $-1$ where $X$ carries no link at $c$); $\mathrm{star}(X)$, the
1-cell and 2-cell counts at $X$; $\mathrm{link}(X) = (V,E,b_0,b_1)$ of the
graph whose vertices are $X$'s neighbours and whose edges are the 2-cells
containing $X$. The reading is `CONSISTENT` exactly when the triple is
chart-independent.

The estimator is calibrated against I3's declared controls, rebuilt here: the
boundary of a tetrahedron ($V,E,F = 4,6,4$; $b = 1,0,1$), a 9-vertex torus
($9,27,18$; $1,2,1$) and two tetrahedra sharing a vertex ($7,12,8$; $1,0,2$).
The first two return a circle link at every vertex and the third does not
(`G-STANDARDS-CONTROLS`, `G-STANDARDS-CONTROL-BETTI`). The global identities
$\sum_v \mathrm{star}_E = 2|E|$ and $\sum_v \mathrm{star}_F = 3|F|$ are gated,
and the per-cell dimension is cross-checked against a component census that
never routes through the estimator (`G-STANDARDS-IDENTITIES`).

At the 14 locality-bearing rules, over the charts of the non-complete
component:

- **Links are essentially never circles: 1 of 80 charts.** The single
  exception is chart 4 of R051 (T7, $H=\langle\Sigma\rangle$, $c=3$,
  `SLIDING`), whose link is $(5,5,1,1)$. At $c=2$ every link is edgeless
  except at R048, where two charts carry one link edge apiece, and $b_1=0$
  throughout; at $c=3$ the links have $b_1=0$ at five of the six rules and
  reach $b_1=2$ at R051; at $c=4$ they are connected with $b_1$ from 2 to 7.
  Nothing in the sequence approaches the controls' $(k,k,1,1)$.
- **The dimension reading is `INCONSISTENT` at every one of the 14 rules.**
  At twelve of them every chart of the component returns a distinct reading;
  the best case is 6 distinct readings over 7 charts, at R048 and R051. There
  is no chart-independent reading anywhere in the locality-bearing part of the
  grid.
- **The local dimensions realised are 1, 2 and 3** across the 14 rules, and
  they grow with the declared window width: $\{1\}$ at $c=2$ (except R048,
  $\{1,2\}$), $\{1,2\}$ at $c=3$ (except R051, $\{1,2,3\}$), $\{2,3\}$
  at $c=4$. The reading tracks the declaration, which is what an extensive
  estimator does.
- $\mathrm{dimprofile}$ is carried as **EXTENSIVE-EXCLUDED**: I3 measured the
  estimator extensive and R0 excludes it as an intensive candidate. It is
  printed, never used as an invariant.

These are **disclosures**. The unit measures the standards and reports what
they return; it makes no claim about the geometric type of anything it built,
and the verdict string contains no such word.

---

## 6. The two block constants under the new atlases, and $b_1$

### 6.1 The constants

Both denominator conventions are printed at every rule and both arenas
(receipt `block_constants`; output §8): the per-incidence
$|F(N_{\mathrm{coh}})|/|E(N)|$ and the per-drawn-pair
$|F(N_{\mathrm{coh}})|/|E(G)|$, and $b_2$ density
$b_2(N_{\mathrm{coh}})/|F(N_{\mathrm{coh}})|$. Representative rows:

| rule | atlas | $E(N)$ | pairs | $F$ | $F_{\rm coh}$ | per-incidence | per-pair | $b_2$ density |
|---|---|---|---|---|---|---|---|---|
| R001 | G0, T7 | 21 | 21 | 35 | 35 | 5/3 | 5/3 | 4/7 |
| R052 | G0, T4 | 6 | 6 | 4 | 4 | 2/3 | 2/3 | 1/4 |
| R008 | G2, T7, $c=3$, SLIDING | 18 | 12 | 5 | 5 | 5/18 | 5/12 | 0/1 |
| R011 | G2, T7, $c=4$, SLIDING | 36 | 18 | 20 | 20 | 5/9 | 10/9 | 1/5 |
| R009 | G2, T7, $c=4$, ALL | 315 | 21 | 175 | 175 | 5/9 | 25/3 | 1/5 |

Three facts, all measured:

1. **Every density is constant from B to B₂ at 109 of 109 rules**, and the
   additive counts double exactly (`G-COPY-REDUCTION`). The copy-forcing
   invariance R1 measured for one atlas is here verified for **every** atlas
   in the grid, including all 14 locality-bearing ones. Declared locality does
   not disturb it.
2. **The values are strongly atlas-dependent.** The per-incidence density runs
   from 0/1 to 25/18 across the grid; the two conventions agree exactly when
   each drawn pair sits in exactly one cell and diverge otherwise (R009: 5/9
   against 25/3). The constants are constants *of a declaration*, not of the
   substrate.
3. **The $b_2$ density is UNDEFINED at 28 rules** — those with no coherent
   2-cell at all, $F_{\rm coh}=0$. That path is live, reached by shipped
   inputs, and recorded with its reason (`G-UNDEFINED-PATH-LIVE`).

### 6.2 $b_1$ per component

I3's ordered measurement left degree one trivial. Here, at the 14
locality-bearing rules, the non-complete component's own cycle rank is
recorded, together with $b_1(N)$ and $b_1(N_{\rm coh})$:

| rule | component | edges | cycle rank | $b_1(N)$ |
|---|---|---|---|---|
| R005 / R030 | 7 | 6 | 0 | 0 |
| R008 / R033 | 7 | 12 | **6** | 7 |
| R011 / R036 | 7 | 18 | **12** | 14 |
| R048 | 7 | 7 | **1** | 1 |
| R051 | 7 | 14 | **8** | 8 |
| R063 / R088 / R106 | 4 | 3 | 0 | 0 |
| R066 / R091 / R109 | 4 | 5 | **2** | 3 |

Nine of the 14 carry a non-trivial degree-one component. This is measured and
disclosed; it is the first non-zero degree-one reading in the declared arenas
of this line, and it is produced by the same window overlap that produces the
locality — a cycle in the overlap graph is a cycle of the sliding window, not
an identification datum. $b_1(N_{\rm coh}) = b_1(N)$ everywhere, because
$N_{\rm coh}=N$ (§3.3).

---

## 7. B₂, and the controls

### 7.1 Persistence at B₂

Every locality-bearing rule is re-measured at B₂ (`G-B2-PERSISTENCE-MEASURED`).
**Locality survives at 14 of 14**, the non-complete component count **doubles
at 14 of 14** (one per block), and componentwise completeness is **unchanged
at 14 of 14** — 2/7 stays 2/7, 5/6 stays 5/6, and so on. The basepoint enters
as an isolated component and changes nothing. Block addition neither creates
nor destroys locality here; it copies it.

### 7.2 The positive control

A hand-declared toy, outside the grid, with known partial overlap: two cells
$\{1,2,3\}$ and $\{3,4,5\}$ sharing exactly the label 3. It returns a
component of size 5 with 6 of 10 pairs drawn — **non-complete**
(`G-POSITIVE-CONTROL`). The mutant `toy-broken` (which makes the two cells
identical) dies here. The criterion's instrument can see partial overlap when
partial overlap is present.

### 7.3 The scramble control

The tested set is fixed by declaration — every grid rule with $F(N)>0$, 81 of
them — never selected by the verdicts under audit. Scrambling the drawn maps
by a declared deterministic rule **moves the identification-sensitive measure
at 81 of 81** and **leaves the component census unchanged at 81 of 81**
(`G-SCRAMBLE-CONTROL`; mutant `scramble-inert`). Locality is a fact about the
cells; coherence is a fact about the maps.

### 7.4 The symmetry self-test and the parity witness

Relabelling the arena by γ, by Σ, by γΣ and by a declared wild involution —
conjugating the transport and transporting the cells together — leaves the
census invariant at every probe, evaluated **fresh** with the memo bypassed
(`G-SYMMETRY-SELFTEST`); the cache's own hit and miss counts are gated
non-zero (`G-CACHE-EXERCISED`: 1289 hits, 212 misses, 48 fresh self-test
evaluations). The Boolean connective at the 2-cell boundary carries its
witness: replacing pairwise-drawn by any-pair-drawn changes the 2-cell count
at 78 of 90 rules of the declared tested set, total measured delta 4000
(`G-BOUNDARY-PARITY`).

### 7.5 The alternative drawing-group reading, disclosed

The pin fixes the drawing relation across the grid so that only the cell
structure varies. Had $\langle\gamma,\Sigma\rangle$ been used as the *drawing*
group instead, **nothing would be drawn at either transport** — 0 pairs at
order 5040 and 0 at order 240 — because a drawn pair forces a trivial
stabiliser and neither group can have a regular orbit inside eight labels
(`G-ALT-DRAW-PROBE`). The Σ-mixed class is therefore a statement about cells,
and the paper says so rather than leaving the reading implicit.

---

## 8. The instrument

**42 gates, all passed; 5 anchors; 14 declared mutants, all dead.** Two plain
delivery runs are byte-identical in both artifacts. The falsification selftest
re-invokes the instrument once per mutant and requires exit 1, a death
certificate naming the expected gate, and the on-disk artifacts unchanged.

| mutant | what it breaks | dies on |
|---|---|---|
| `grid-drop` | drops one $(H,c,\text{mode})$ grid cell | `G-GRID-CELL-COMPLETE` |
| `census-corrupt` | drops one drawn edge from a rule's census | `G-DRAW-TWO-ROUTES` |
| `orbit-corrupt` | corrupts the regularity test of the orbit machinery | `G-DRAW-TWO-ROUTES` |
| `complete-flip` | flips per-component completeness and the rule's locality flag | `G-COMPLETENESS-TWO-ROUTES` |
| `locality-inject` | injects a spurious non-complete component at the null | `G-R2A-NULL-CLIQUE-ONLY` |
| `locality-erase` | collapses SLIDING onto BLOCKWISE, erasing all locality | `G-MODES-DISTINCT` |
| `refuses-skip` | skips refusing rules instead of recording them | `G-EVERY-RULE-RECORDED` |
| `verdict-pair-swap` | swaps two verdict segments' names against their values | `G-VERDICT-STRING-EQUALITY` |
| `table-corrupt` | corrupts a block-constants cell after measurement | `G-RENDER-FROM-GATED-OBJECT` |
| `census-row-corrupt` | corrupts a rendered census row after measurement | `G-RENDER-FROM-GATED-OBJECT` |
| `toy-broken` | breaks the positive control's partial overlap | `G-POSITIVE-CONTROL` |
| `scramble-inert` | makes the scramble control a no-op | `G-SCRAMBLE-CONTROL` |
| `anchor-hash` | corrupts the I6 anchor hash | `A-R0-I6` |
| `float-leak` | reports a float offence in the source scan | `G-FLOATGUARD` |

`locality-erase` and `locality-inject` are the two verdict-flip mutants:
the first drives the emitted head to
`R2-NO-LOCALITY-IN-THE-DECLARED-GRID`, the second changes the named rule list;
both die. No gate predicate reads mutant identity.

The verdict is derived inside a gate and the **complete** emitted string is
compared for equality against a segment-by-segment rebuild — containment,
prefix and substring checks are not verdict gates
(`G-VERDICT-STRING-EQUALITY`). Every one of the nine segments is shown to be
flippable: perturbing its measured input changes the emitted string
(`G-VERDICT-SEGMENTS-FLIPPABLE`). The receipt and this paper render from the
**gated object** — one object, one source of truth — and a gate checks every
rendered table cell against it (`G-RENDER-FROM-GATED-OBJECT`).

---

## 9. What this unit found

1. **Locality can be declared into existence.** 14 rules of a 109-rule
   exhaustively enumerated declared grid produce a component whose overlap
   graph is not complete. The criterion the R1 adjudication handed forward,
   measured empty across R1's whole family, is non-empty here.
2. **The mechanism is exactly the recipe, and only the recipe.** Every
   locality-bearing rule is a partial-coset-overlap rule; every
   orbit-partition rule (38 of 38) and every non-overlapping bunching returns
   clique-only. Theorem R2-A and its partition corollary say why, and the
   40,320-action sweep leaves no room for an exception at this scale.
3. **The standards say nothing manifold-shaped.** Links are circles at 1 of 80
   charts, the dimension reading is `INCONSISTENT` at 14 of 14 rules, and the
   local dimensions realised (1, 2, 3) track the declared window width. What
   the declaration buys is a non-complete overlap graph; it does not buy a
   chart-independent dimension, and it does not buy sphere-like links.
4. **Declared locality does not disturb the copying invariance.** Both block
   constants are constant from B to B₂ at 109 of 109 rules, locality-bearing
   ones included; the additive counts double exactly. The constants remain
   constants of a declaration — their values move across the grid by more than
   an order of magnitude.
5. **Degree one becomes non-trivial for the first time in these arenas** — at
   9 of the 14 rules, with cycle ranks up to 12 and $b_1(N)$ up to 14 — and
   the cause is measured: it is the sliding window's own cycle, not
   identification data. $N_{\rm coh}=N$ identically, so the cocycle condition
   carries nothing at this scale.
6. **Locality survives block addition by copying**, at 14 of 14, with
   componentwise completeness unchanged and the non-complete component count
   doubling.

## 10. What this unit does not claim

- **No continuum claim.** R1's question is untouched.
- **No geometric-type claim.** The standards are ported as disclosures and
  measured; one component of one block is not evidence about anything's shape,
  and the verdict does not name a shape.
- **No claim that the grid is the space of all atlases.** It is a declared,
  finite, exhaustively enumerated grid, printed in full and carried as a named
  verdict coordinate. A rule outside it is not measured, and the verdict is
  scoped to the grid by construction.
- **No claim that locality here is substrate content.** It is a declaration
  effect with a measured mechanism, and the paper's own §4 names the width at
  which it disappears. The honest reading is: *the criterion is satisfiable,
  the recipe works, and what it produces does not meet the standards.*
- **No claim about $\varphi$.** R1's gateway is forced by the basepoint
  (theorem R2-C, inherited by anchor); this unit does not use it.

## 11. What the next rung inherits

- A **satisfiable** criterion with a proved mechanism, and a measured boundary
  for it: partial coset overlap yields locality only while the window is
  narrower than the orbit, and only at the regular orbit.
- The finding that the two block constants are **atlas-dependent in value and
  copy-invariant in behaviour**, so any later intensive claim must name its
  atlas as a coordinate — the R1 atlas lesson, now measured across 109 atlases
  rather than five.
- The finding that at this drawing relation the **cocycle condition is free**
  ($N_{\rm coh}=N$), so identification content must be sought elsewhere than
  in coherence.
- The open question this unit deliberately did not answer: whether any
  declaration exists — necessarily outside this grid, and therefore outside
  the pin — under which the ported standards return a chart-independent
  reading. Everything measured here says width-based overlap will not do it.
