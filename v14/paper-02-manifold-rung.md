# R2 — the manifold rung

**Status:** `TERMINAL` — panel #17/#18/#19 (3× ACCEPT-WITH-FIXES),
adjudicated #20; repair R-R2-1…R-R2-12 delivered #21 and
adjudicator-verified (plain-run byte-identical; selftest 54/54 mutants
dead); v14 ledger #22, 2026-08-09.  Pin:
`v14/note-r2-manifold-pin.md`, sha256-12 `76d42dfbc900`.

## Locality Is Declarable, and the Declaration Is the Whole of It

**Unit:** R2 (the manifold rung), v14.
**Pin:** `v14/note-r2-manifold-pin.md`, sha256-12 `76d42dfbc900` (v14 ledger
#11), verified at run time by gate `A-PIN-R2`.
**Instrument:** `v14/code/r2_manifold_exact.py`.
**Artifacts:** `v14/code/r2_manifold_output.txt`,
`v14/code/r2_manifold_receipt.json`.
**Inheritance, hash-verified at run time and by no other route:** R0 row I6
(`v13/code/tb3_third_base_receipt.json`, `c9bc956fe751`) supplies the block —
the eight system-triple labels, the ×7 embedding witness, the declared
completion transposition, and the non-zero labels of $\mathbb F_2^3$ on which
its own Fano geometry is declared; R0 row I3
(`v13/code/top_topology_receipt.json`, `65bb1fc5231f`, with the v14 LOG #4
erratum's companion `v13/paper-top-topology.md` = `379194959fbc`) supplies the
nerve, link and dimension definitions, reimplemented here and imported from
nowhere; the R1 joint adjudication (`v14/note-r1-adjudication.md`,
`4115dcd83cfa`) supplies the criterion, the recipe and the null.
**Anchors are (path, value) pairs, not only file bytes:** five file-bytes
anchors and six path-value anchors, each naming the exact JSON path it reads
and the exact value it expects, so a one-key drift dies at the anchor rather
than delivering a different study.
**Exact arithmetic only:** integers and `Fraction`; an AST scan of the
instrument's own source is the first gate.

**The verdict, quoted exactly as the instrument emits it.** Every segment is
derived inside a gate from measured counts, and the complete string is compared
for equality against an *independent reconstruction* built from the receipt
object alone:

```
R2-LOCALITY-DECLARABLE-AT<RULES=14-OF-109:R005,R008,R011,R030,R033,R036,R048,
R051,R063,R066,R088,R091,R106,R109|GRID=T4:G0=1;G1=2;G2=24;G3-ORBITS=7;
G3-UNIONS=24|T7:G0=1;G1=1;G2=18;G3-ORBITS=7;G3-UNIONS=24|TOTAL=109|DRAWING=
R1-RELATION-AT-<GAMMA>-VERDICT-DETERMINING(ALT-<GAMMA,SIGMA>:0-PAIRS-AT-2-OF-2-
TRANSPORTS=>NO-LOCALITY-IN-THE-DECLARED-GRID)|MECHANISM=DECLARED-PARTIAL-COSET-
OVERLAP(CLASSES=G2+G3-UNIONS;MODES=SLIDING)|WIDTH-LAW=NONCOMPLETE-IFF-C<=D(D=
MAX-CYCLIC-COSET-DISTANCE-IN-THE-REGULAR-ORBIT);TWO-CAUSES=T4:CONTIGUOUS-ARC(D=
3,C-MAX=3);T7:MISSING-POINT(D=4,C-MAX=4);CENSUS-DERIVABLE-FROM-THE-DECLARATION-
AT-109-OF-109;CLOSED-FORMS-AGREE-AT-30-OF-30|MOTIVATION=NONE-INHERITED:
PARTITION-COVERS-NONCOMPLETE-AT-0-OF-8280(ALL-4140-PARTITIONS-X-2-TRANSPORTS);
I6-FANO-LINES-CLIQUE-ONLY-AT-2-OF-2(2-DESIGN:21-OF-21-PAIRS-COVERED);ORDER-
RELATIVE(COUNT=11..16-OVER-40320-NUMBERINGS;DECLARED=14-MODAL-34.29%;DISTINCT-
RULE-SETS=11)|COMPONENTS=NONCOMPLETE-COMPONENT-SIZES=4+7;RULES-WITH-NONTRIVIAL-
B1=9|STANDARDS=LINK-CIRCLES=1-OF-80-CHARTS;DIMREAD=INCONSISTENT-FORCED(CELL-
INDEXED-READING:CONSISTENT-EXCLUDES-NONCOMPLETE-BY-THEOREM;CONSISTENT-AT-22-OF-
109-RULES,INTERSECTION-WITH-LOCALITY=0);LOCAL-DIMENSIONS=1+2+3-FORCED(=MAX|
CELL-CAP-REGULAR-ORBIT|-1-AT-14-OF-14);DIMPROFILE=EXTENSIVE-EXCLUDED|LINK-
CONVENTION=CELL-MULTIPLICITY=1-OF-80;SIMPLE-GRAPH=8-OF-80;TRIANGULATED-CIRCLES=
0-OF-80|B2-PERSISTENCE=FORCED-BY-BLOCK-LOCALITY:SURVIVES-AT-14-OF-14;
COMPONENTS-DOUBLE-AT-14|NULL=G0-CLIQUE-ONLY-AT-2-OF-2-RULES(4-OF-4-
MEASUREMENTS);ORBIT-PARTITION-CLASSES-CLIQUE-ONLY-AT-19-OF-19-RULES(38-OF-38-
MEASUREMENTS;10-OF-THEM-REFUSE)(R2-A-VERIFIED-10-UNIT-ACTIONS-AND-40320-SWEPT-
ACTIONS-14170-DISTINCT-CYCLIC-GROUPS-0-COUNTEREXAMPLES)|REFUSES=5-OF-109|GRID-
BOUNDARY=(H,C)-ADMITTED-BY-GROUP-ORDER-NOT-COSET-COUNT:60-DECLARED-WORD-RULES-
EXCLUDED(72-WITH-THE-CYCLIC-LATTICE);1-OF-THEM-NONCOMPLETE(T7-<GSGS>-C2-
SLIDING-16-OF-21)|BLOCK-CONSTANTS=DENSITIES-CONSTANT-B-TO-B2-AT-109-OF-109-
FORCED-BY-COPYING;VALUES-GRID-DEPENDENT=0/1..5/3;UNDEFINED-B2-DENSITY-AT-28>
```

(The line breaks are typographical; the emitted string is one line, and the
gate compares that line.)

**The head says `DECLARABLE`, and that word is the finding.** What this unit
establishes is an existence statement about *atlas space*: the R1 criterion is
satisfiable, by a construction with a closed-form width threshold. It is not a
statement about the substrate, and §4 measures why it cannot be one.

**Declared scope.** At the single block **B** — TB3's native 8-label arena via
I6 — and at **B₂** — two isomorphic blocks plus an isolated basepoint — over
an exhaustively enumerated declared atlas grid of 109 rules at 2 declared transports.
Nothing outside that grid is measured; the grid, the drawing relation and the
transports are named coordinates of the verdict.

**Every numeric sentence below is rendered by the instrument from the receipt
object** and gated to appear here verbatim (`G-PROSE-RENDERS-FROM-THE-RECEIPT`);
the rendered set is printed in output §13a. Numbers in the tables render from
the same object. Nothing here is typed by hand.

---

## 1. What the rung asks, and what it inherits

The R1 adjudication left the manifold rung **not an arena but a criterion and
a recipe**. The criterion: *locality exists at a rule iff some connected
component of that rule's overlap graph is not complete.* Measured across R1's
whole family it returned nothing. The recipe, theorem R2-A: with regular-orbit
drawing the overlap graph is always a union of cliques, so locality can only be
earned by declaring cells whose orbits overlap **partially**. The null: the
regular-orbit atlas, guaranteed clique-only.

R2 therefore starts at **atlas design**, and its question is two-sided:

> Does any drawing rule in a declared finite grid of atlas declarations
> produce a component with a non-complete overlap graph — and where locality
> appears, what do the ported standards measure?

Both heads are first class. `G-VERDICT-BOTH-HEADS-REACHABLE` runs the verdict
derivation on two *synthesised receipts* — one carrying no non-complete rule,
one carrying a non-complete rule — and requires the negative and positive heads
respectively; the mutant `head-constant` proves the check can fail.

The copy-forcing theorem says per-block structure carries all content, so R2
works at the block, not the tower. That reduction is verified, not assumed
(`G-COPY-REDUCTION`, mutant `copy-reduction-break`), at every rule of the grid.

**A word on what a positive answer can mean.** The recipe names the mechanism
that produces locality before any measurement is taken. A grid built to contain
that mechanism will contain it. The unit's real questions are therefore the
next two: *is the census a measurement or a corollary of the declaration* (§3),
and *does anything in the inheritance motivate the covers that carry it* (§4).
Both are answered here, and both answers are negative for the strong reading.

---

## 2. The arenas, the transports and the grid — declared as data

Everything in this section is printed by the instrument, matched against its
computed value at every coordinate, and gated (`G-ARENA-DECL-MATCHED`,
`G-BLOCKSIZE-FROM-I6`, `G-READ-VALUES-MATCH-THE-DECLARATION`,
`G-GRID-CELL-COMPLETE`, `G-GRID-CELL-SETS-COMPLETE`).

### 2.1 The arenas

- **B** — the single block: the 8 system-triple labels $\{0,\dots,7\}$ of I6's
  declared carrier. The block size is *read* from I6
  (`base_declaration.carrier.system_triple_dimension`), never typed.
- **B₂** — two isomorphic copies of B (labels 0–7 and 8–15) plus an isolated
  basepoint (label 16), 17 labels. The rule is applied **block-locally**: a
  rule's cells are copied into each block and the basepoint lies in no cell.
  Transports never cross blocks. This is a declaration, and §7.1 states what it
  buys and what it therefore cannot test.

### 2.2 The transports, and the values as well as the files

The transport is arena data with two declared values, each read from I6 by an
exact path that is itself anchored:

| name | γ | order | source in I6 |
|---|---|---|---|
| **T7** | `(0,2,3,4,5,6,7,1)` — the 7-cycle on the seven non-zero labels | 7 | `tables.the_ladder.the_embedding.the_witness_system_part`, the ×7 = [A₇:A₆] embedding witness |
| **T4** | `(0,1,3,4,5,2,7,6)` = (2 3 4 5)(6 7) | 4 | `tables.ord_census.lex_first_Q_per_order['4']`, the lex-first completion permutation at defect order 4 |

Σ is the same at both: `(0,3,2,1,4,5,6,7)` = (1 3), I6's
`tables.arena.the_declared_completion_transposition`. The drawing group is
$\langle\gamma\rangle$ throughout; $\langle\gamma,\Sigma\rangle$ has order
5040 at T7 and 240 at T4 and is used only to generate cells.

Every property this paper states about those values — the orders 7, 4 and 2,
the cycle types, the two Σ-mixed group orders — is *recomputed from the
anchored value* and gated (`G-READ-VALUES-MATCH-THE-DECLARATION`, mutant
`read-value-drift`). A file-bytes anchor alone would not do it: a drift of one
JSON key delivers a different transport, a different grid size and a different
verdict with every file hash green, and the mutant `path-drift` demonstrates
that this instrument now dies on it by anchor (`P-I6-GAMMA4`).

Two transports rather than one because the transport is a *declaration*
(RUNBOOK §15: the arena is data). The choice is load-bearing rather than
decorative, and §3.3 is the reason: the two transports reach their width
thresholds by *different mechanisms*, which a single-transport census would
have reported as one effect. The strict T7-only sub-census remains a sub-table
of the census: 51 rules, 8 locality-bearing, 2 REFUSES, one component size.

### 2.3 The drawing relation, and that it decides the verdict

Identical to R1's, so that the **only** variable across the grid is the
declared cell structure:

> $(a,b)$ is **drawn** iff exactly one transport element carries $a \to b$,
> and $a,b$ lie in a common declared cell.

This is a declaration, and it is *verdict-determining*. Had
$\langle\gamma,\Sigma\rangle$ been used as the drawing group instead, **nothing
would be drawn at either transport** — 0 pairs at order 5040 and 0 at order
240, because a drawn pair forces a trivial stabiliser and neither group can
have a regular orbit inside eight labels. The head would then be
`R2-NO-LOCALITY-IN-THE-DECLARED-GRID`. The measurement is
`G-ALT-DRAW-PROBE`; it is carried in the verdict's `DRAWING` segment, where the
reader meets it before the census.

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
24 + 7 + 24). The enumeration is checked at two depths. `G-GRID-CELL-COMPLETE`
compares the coordinate set against one rebuilt by divisor arithmetic that
touches none of the enumerator's code (mutant `grid-drop`).
`G-GRID-CELL-SETS-COMPLETE` goes one level down and compares, for every rule,
the *cells themselves* against a set rebuilt from the coset-index map — because
a coordinate gate does not see a dropped window, and the mutant `window-drop`
shows what a dropped window would otherwise do to four verdict clauses.

Every rule is measured at both arenas and every result is recorded. A rule
whose relation draws nothing is recorded **REFUSES**, never skipped
(`G-EVERY-RULE-RECORDED`); 5 rules refuse.

§6.3 measures what this grid's *boundary* costs, and it is not nothing.

---

## 3. The width law: the census is a corollary of the declaration

### 3.1 Theorem R2-A, at this family's actions

> **Theorem R2-A.** Let a finite group $T$ act on a label set $L$ and admit
> $(a,b)$, $a\neq b$, iff exactly one $\pi\in T$ has $\pi(a)=b$. Then
> $\{\pi : \pi(a)=b\}$ is empty or a coset of $\mathrm{Stab}(a)$; so it is a
> singleton iff $\mathrm{Stab}(a)=1$ and $b\in \mathrm{orbit}(a)$. Hence
> $(a,b)$ is drawn **iff $b$ lies in $a$'s orbit and that orbit is regular**,
> and the drawn relation is the disjoint union of **complete** graphs on the
> regular orbits.

*Proof.* If $\pi(a)=\rho(a)=b$ then $\rho^{-1}\pi\in\mathrm{Stab}(a)$, so the
solution set is $\pi\,\mathrm{Stab}(a)$, of size $|T|/|\mathrm{orbit}(a)|$ by
orbit–stabiliser. Uniqueness is exactly $|\mathrm{orbit}(a)|=|T|$, a property
of the orbit, not of the pair. ∎

*Verification.* The drawn relation is computed twice by genuinely independent
routes — orbit/stabiliser, and brute force over the group elements — and their
agreement is gated at every rule and arena (`G-DRAW-TWO-ROUTES`, 218
measurements). Beyond that, R2-A is swept over 40320 cyclic actions on the block's eight labels, 14170 distinct cyclic groups, 0 counterexamples.
The sweep's exhaustiveness is gated against a *derived* factorial rather than
against zero, so a silent truncation is fatal (`G-R2A-EXHAUSTIVE`, mutant
`sweep-truncate`); and the distinct-group count is printed beside the
permutation count, because $\langle p\rangle$ is generated by $\varphi(\mathrm{ord}\,p)$
elements and the two denominators are not the same number.

### 3.2 The partition corollary — why the null cannot fail

> **Corollary (R2-partition).** An atlas whose cells *partition* the labels
> can never produce a non-complete component.

*Proof.* The drawn pairs inside a cell are exactly the pairs of that cell lying
in a common regular orbit, so each cell contributes a clique on each of its
regular-orbit slices. Distinct cells of a partition share no label, so distinct
cliques share no vertex, and the components of the union are the cliques
themselves. ∎

Measured, with the units named: G0 clique-only at 2 of 2 rules (4 of 4 rule-arena measurements) and the whole orbit-partition family at 19 of 19 rules (38 of 38 measurements, of which 10 refuse).
The last clause matters: REFUSES is a distinct status, and it is counted
separately rather than folded into "clique-only".

### 3.3 Theorem R2-W, the width law

The census is not an experimental result. It is a corollary of the grid
declaration, and this is the corollary.

> **Theorem R2-W.** Let $R$ be a regular orbit, let the declared subgroup's
> orbits ("cosets") be $c_0,\dots,c_{k-1}$ in minimum-label order, write
> $\iota(x)$ for the coset index of $x$, $S=\iota(R)\subseteq\mathbb Z_k$,
> $w_i=|c_i\cap R|$, and $d_k$ for cyclic distance. Under `SLIDING` of width
> $c$:
>
> 1. **Structure.** On $R$, $x\sim y \iff d_k(\iota x,\iota y)\le c-1$: the
>    drawn graph is the lexicographic blow-up of the circulant
>    $C_k(1,\dots,c-1)[S]$ by cliques $K_{w_i}$.
> 2. **Edges.** $|E| = \sum_{i\in S}\binom{w_i}{2} + \sum_{i<j\in S,\,d_k\le c-1} w_iw_j$.
> 3. **Locality.** A component is incomplete iff it contains a pair at cyclic
>    distance $\ge c$; when the circulant on $S$ is connected this is exactly
>    $c \le \operatorname{diam}_k(S)$.
> 4. **The other modes are theorems too.** `ALL` puts every two coset indices
>    in a common $c$-subset, so the drawn graph on $R$ is complete;
>    `BLOCKWISE` and the orbit classes partition the cosets, hence the labels,
>    so the partition corollary applies.

*Verification.* The instrument evaluates the law from the declaration alone —
the coset partition, the regular orbits, the mode and the width — building no
atlas and enumerating no cell, and the law predicts the locality status and the drawn edge count of every rule at 109 of 109
(`G-WIDTH-LAW-PREDICTS-THE-CENSUS`, mutant `width-law-corrupt`). A third route,
arithmetic in $(k,m,c)$ alone, specialises the law to the declared families:
the closed forms reproduce the measured edge counts and cycle ranks at 30 of 30 rows.

| family | validity | $|E|$ | $b_1$ | realised |
|---|---|---|---|---|
| $S=\mathbb Z_k\setminus\{\rm pt\}$, $w\equiv 1$ | $c-1<k/2$ | $(c-1)(k-2)$ | $(c-2)(k-2)$ | at $k=8$: $b_1 = 0, 6, 12$ |
| $S$ a contiguous arc of length $m$, $w\equiv 1$ | $c\le m$ | $(c-1)m-\binom{c}{2}$ | $|E|-m+1$ | at $m=4$: $b_1 = 0, 2$ |
| $S$ a contiguous arc, saturated | $c>m$ | $\binom{m}{2}$ | $|E|-m+1$ | complete |
| general blow-up | always | as (2) above | $|E|-\sum w_i+1$ | T7's Σ-cosets: $b_1 = 1, 8$ |

**The two thresholds have different causes, and this is why both transports
had to be run.** Measured: at T7 the support is missing point with diameter 4, at T4 it is contiguous arc with diameter 3.
At T7 the regular orbit misses exactly one coset, so
$\operatorname{diam} = \lfloor k/2\rfloor$ and locality vanishes at $c\ge 5$;
at T4 the regular orbit is a *contiguous arc* of length 4, so
$\operatorname{diam} = m-1$ and locality vanishes at $c\ge 4$. One reported
effect; two mechanisms. A T7-only census would have named the first as the
mechanism's content.

**Consequence, stated plainly.** *Which rules are local* is computed from the
declaration, and so are their component sizes, their completeness fractions and
their cycle ranks. Per RUNBOOK §14 (#208) those clauses are carried as
**forced**. What remains measured is the grid, the drawing relation, and the
values of $E_N$, $F$, $F_{\rm coh}$ and the two densities. The locality is not
killed by this — it is real at exactly those declared coordinates — but its
epistemic label moves from *discovered by census* to *computed from the
declaration*.

### 3.4 The coherence corollary — a forced clause, entered as a disclosure

> **Corollary (R2-A-coherence).** For any 2-cell of $N$ the three drawn maps
> compose to the identity; $N_{\mathrm{coh}} = N$ identically.

*Proof.* $m_{ca}\circ m_{bc}\circ m_{ab}$ fixes $a$; a drawn pair forces
$\mathrm{Stab}(a)=1$ by R2-A; so the composite is the identity. ∎

True by algebra for every input, so per #208 a **disclosure**. It is verified at
all 218 measurements (`G-COHERENCE-FORCED`) and the scramble control shows the
instrument is not vacuous. The consequence worth stating: under the R1 drawing
relation the cocycle is free, so the identification data this scale carries is
not in the cocycle condition — and the qualifier "coherent" does no
extensional work at this relation.

---

## 4. The motivation census: nothing in the inheritance supplies the cover

The recipe named the mechanism, and the grid contains it. The question that
decides what the census *means* is whether any locality-bearing cover is
expressible from the substrate's own inherited structure without a new choice.
It is measured here, three ways, all exhaustive.

### 4.1 Every group is disqualified at once

A cell structure produces locality iff the co-cell graph, restricted to the
transport's regular orbit, has a component that is not a clique. Orbits
partition; a partition's co-cell graph is a disjoint union of cliques. So the
question reduces to a sweep over partitions, and the sweep is finite: all 4140 set partitions of the eight labels at both transports -- 8280 measurements, 0 non-complete.

Since the orbit family of *any* subgroup of $S_8$ is one of those partitions,
this settles Σ, $\langle\gamma,\Sigma\rangle$, the seven declared words, the
ladder $1<A_4<\mathrm{GL}(3,2)<A_6<A_7$ and every subgroup of every one of
them — at once. **No inherited group can motivate a locality-bearing cover.**
This is not a limitation of the grid; it is a theorem about groups, and the
sweep's denominator is derived from the Bell number so a truncation is fatal
(`G-MOTIVATION-PARTITION-SWEEP`, mutant `partition-sweep-truncate`).

### 4.2 The one motivated cover the corpus owns is a locality-destroyer

What is needed instead is a *proximity datum*: a cover that is neither a
partition nor pair-complete. The inheritance supplies exactly one candidate,
and it supplies it by name. I6's receipt declares its type as
$\mathrm{GL}(3,2)$ acting $\mathbb F_2$-linearly on the seven Fano points, and
records `the_non_zero_labels_of_F2_cubed` = $\{1,\dots,7\}$. The seven Fano
lines are derived from that anchored declaration by the linear rule
$a \oplus b \oplus c = 0$ — not chosen here — and measured:

| cover | T7 | T4 |
|---|---|---|
| the seven Fano lines | clique-only | clique-only |
| the seven line complements | clique-only | clique-only |

the seven Fano lines cover 21 of 21 pairs and are clique-only at 2 of 2 transports.
And it fails *for a reason*: a 2-design covers every pair, so its overlap graph
is complete. **The corpus's own geometry is exactly the wrong shape to produce
this unit's locality** (`G-MOTIVATION-FANO-COVER`, mutant `fano-shrink`).

### 4.3 Where the cover actually comes from: the numbering, read twice

`SLIDING` means "every cyclic window of $c$ consecutive cosets", and cosets are
ordered by minimum label. The rule reads the label order twice — once to name
the cosets, once to say "consecutive" — and a cyclic order is precisely the
datum §4.1 says the inheritance does not supply. The transports do not rescue
it: T7's γ *is* the increasing cycle on the non-zero labels, and T4 is the
*lexicographically* first completion at its order, selected by the same label
order.

So the rule list is a coordinate of the numbering, and the size of that
dependence is measured, not argued: over all 40320 numberings of the carrier the count runs from 11 to 16, realising 11 distinct rule sets, and the declared numbering's 14 is the modal value at 34.29%.

| locality count | numberings | share |
|---|---|---|
| 11 | 4,032 | 10.00% |
| 12 | 2,880 | 7.14% |
| 13 | 10,368 | 25.71% |
| **14 — the declared numbering** | **13,824** | **34.29%** |
| 15 | 1,728 | 4.29% |
| 16 | 7,488 | 18.57% |

16 rules are local at some numbering; two of them (R069, R094) are local at
most orderings of their own cosets and non-local at the declared one. Two
things follow, and they point in opposite directions. The declared numbering
returns the **modal** count, and the mechanism — `SLIDING` against
`ALL`/`BLOCKWISE` — is completely order-independent: this is a real robustness
result, and no coordinate was selected for its answer. But
`RULES=14-OF-109:<list>`, the verdict's head segment, names a
numbering-relative set (`G-MOTIVATION-ORDER-RELATIVITY`, mutant
`order-sweep-truncate`).

The delivered symmetry self-test cannot see this: it conjugates the transport
*and* transports the cells together, which is covariance, not
order-invariance. Both are now carried, and the compliance sweep says which is
which.

### 4.4 What the verdict may therefore claim

> **LOCALITY-DECLARABLE**, not LOCALITY-FOUND.

Precisely: the R1 criterion is satisfiable; the mechanism that satisfies it is
declared partial coset overlap along a cyclic order that no inherited object
supplies; the inheritance's own partial-overlap cover fails the criterion
because it is a 2-design; and the rule list is a coordinate of the carrier's
numbering. That is an existence statement about atlas space, and it is what the
head now says.

---

## 5. The locality census

The criterion is applied at every rule at B. The full 109-row table is in
`r2_manifold_output.txt` §4 and in the receipt's `census_rows`:

| class | rules at B | clique-only | REFUSES | **non-complete** |
|---|---|---|---|---|
| G0 | 2 | 2 | 0 | 0 |
| G1 | 3 | 1 | 2 | 0 |
| G2 | 42 | 37 | 0 | **5** |
| G3-ORBITS | 14 | 11 | 3 | 0 |
| G3-UNIONS | 48 | 39 | 0 | **9** |
| **total** | **109** | **90** | **5** | **14** |

14 of 109 rules produce a component that is not complete. Every one of
them is a `SLIDING` rule; every `ALL` and every `BLOCKWISE` rule returns
clique-only, as does every orbit-partition rule.

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

Two non-complete component sizes occur, 7 (T7's regular orbit) and 4 (T4's).
In every case the non-complete component is exactly the transport's regular
orbit, and the missing pairs are the pairs no cyclic window of length $c$ can
cover — which is theorem R2-W, not an observation.

**The census is measured against itself as well as predicted.** Completeness is
computed twice, from the stored edge count and from an explicit pair scan
(`G-COMPLETENESS-TWO-ROUTES`); components twice, by union–find and by
$|V|-\operatorname{rank}\partial_1$ over $\mathbb F_2$
(`G-COMPONENTS-TWO-ROUTES`); the 2-cells twice, by cell enumeration and by an
independent triangle recount over the drawn-pair table
(`G-TWOCELLS-TWO-ROUTES`). The locality flag, the REFUSES flag, per-component
completeness and each cycle rank are re-derived inside a gate from
`per_component` and `edges` rather than trusted as stored bits
(`G-FLAGS-DERIVED-NOT-TRUSTED`) — because each was a single bit that the
census, the tables and the verdict all read from the same place. The mutants
`flag-flip`, `refuses-reclassify`, `b1-zero` and `twocell-drop` are the four
falsifiers, and `G-RECEIPT-INTERNALLY-CONSISTENT` additionally forbids the
receipt to contradict itself — no rule may be labelled clique-only while a
non-complete component is listed for it.

---

## 6. What the ported standards say, and where the grid ends

### 6.1 The standards, and the dimension reading over the whole grid

I3's estimator is reimplemented from its written definition and imports
nothing: for a chart $X$, $\mathrm{dimprofile}(X)$ over the rule's coordinate
cells; $\mathrm{star}(X)$; $\mathrm{link}(X)=(V,E,b_0,b_1)$. The reading is
`CONSISTENT` exactly when the triple is chart-independent. The estimator is
calibrated against I3's declared controls, rebuilt here: the boundary of a
tetrahedron ($4,6,4$; $b=1,0,1$), a 9-vertex torus ($9,27,18$; $1,2,1$) and two
tetrahedra sharing a vertex ($7,12,8$; $1,0,2$); the first two return a circle
link at every vertex and the third does not.

The delivered instrument evaluated the reading only at the 14 locality rules —
a filtered population on which the answer is forced. Run over all 109:
CONSISTENT is attained at 22 of 109 rules and its intersection with the locality census is empty.
That is the informative result, and it is a theorem:

> **Theorem R2-D.** Under the cell-indexed reading a component whose overlap
> graph is non-complete can never return `CONSISTENT`.
>
> *Proof.* Suppose $C$ is non-complete and every chart of $C$ shares one
> dimprofile. $C$ has a drawn edge, so some entry $i$ is $\ge 1$ at some chart,
> hence at every chart of $C$; an entry $\ge 1$ requires the chart to lie in
> cell $i$, so $C\subseteq$ cell $i$; a component lies in a single regular
> orbit, so every pair of $C$ is drawn inside cell $i$ and $C$ is a clique —
> complete. Contradiction. ∎

So `DIMREAD=INCONSISTENT` at 14 of 14 is not a finding about the arenas; it is
a restatement of the fact that those 14 are the locality-bearing ones, and the
verdict carries it labelled `FORCED`. The measurement that *is* live —
CONSISTENT is attainable at all, on shipped input — is the positive control the
delivered instrument did not have.

At the 14 locality-bearing rules, over the charts of the non-complete
component:

- **The link conventions disagree, and the headline moves with them.** links are circles at 1 of 80 charts under the cell-multiplicity convention and at 8 of 80 under the simple-graph convention.
  The delivered reading counts link *edges* as 2-cells with cell multiplicity
  while counting link *vertices* as distinct neighbours; both are now printed
  (`G-LINK-CONVENTION-WITNESSED`). And under the manifold test rather than the
  Betti coincidence, 0 of 80 links is a triangulated circle: the single
  cell-multiplicity "circle" is R051 chart 4, whose link has degree sequence
  $(1,2,2,2,3)$ — a triangle with a two-edge tail, homotopy-equivalent to $S^1$
  and not a manifold link.
- At $c=2$ every link is edgeless except at R048, where 3 charts carry one link edge apiece
  (two of the three share the profile $(2,1,1,0)$); $b_1=0$ throughout. At
  $c=3$ the links have $b_1=0$ at five of six rules and reach $b_1=2$ at R051;
  at $c=4$ they are connected with $b_1$ from 2 to 7.
- **The local dimensions realised are 1, 2 and 3**, and this is an identity,
  not a reading: the top local dimension equals
  $\max|{\rm cell}\cap{\rm regular\ orbit}|-1$ at 14 of 14
  (`G-LOCAL-DIMENSIONS-ARE-AN-IDENTITY`). The verdict carries it labelled
  `FORCED`.
- $\mathrm{dimprofile}$ is carried as **EXTENSIVE-EXCLUDED**: I3 measured the
  estimator extensive and R0 excludes it as an intensive candidate.

### 6.2 $b_1$ per component

I3's ordered measurement left degree one trivial. Here the non-complete
component's own cycle rank is recorded, with $b_1(N)$ and $b_1(N_{\rm coh})$:

| rule | component | edges | cycle rank | $b_1(N)$ |
|---|---|---|---|---|
| R005 / R030 | 7 | 6 | 0 | 0 |
| R008 / R033 | 7 | 12 | **6** | 7 |
| R011 / R036 | 7 | 18 | **12** | 14 |
| R048 | 7 | 7 | **1** | 1 |
| R051 | 7 | 14 | **8** | 8 |
| R063 / R088 / R106 | 4 | 3 | 0 | 0 |
| R066 / R091 / R109 | 4 | 5 | **2** | 3 |

9 of the 14 carry a non-trivial degree-one component. It is the first
non-zero degree-one reading in the declared arenas of this line, and its cause
is measured: it is the sliding window's own cycle — the closed forms of §3.3
give these numbers from $(k,m,c)$ — not an identification datum.
$b_1(N_{\rm coh}) = b_1(N)$ everywhere, because $N_{\rm coh}=N$.

### 6.3 The grid's boundary, and the one casualty

The declared admissibility test is $c\cdot|H| <$ block size: an arithmetic on
the **group order**. The construction uses $H$'s **orbits**. Where $|H|$
exceeds its orbit count the two disagree, and rules whose cells are perfectly
well formed are excluded. Measured: 60 rules constructible from the same declared words are excluded, and 1 of them bears locality
(72 including the cyclic lattice's own exclusions). The casualty:

> T7, $H=\langle gsgs\rangle$ (order 5; orbits $\{0\}$, $\{1,4,5,6,7\}$,
> $\{2\}$, $\{3\}$), $c=2$, `SLIDING`: cells $\{0,1,4,5,6,7\}$,
> $\{1,2,4,5,6,7\}$, $\{2,3\}$, $\{0,3\}$; component 7, **16 of 21 pairs**,
> non-complete.

completeness 16/21, a value no censused rule attains — so this is a genuinely new
census row, not a duplicate of one already counted. "14 of 109" is therefore
true at the declared arithmetic boundary and at no other, and the boundary is
now a named verdict coordinate (`G-GRID-BOUNDARY-CENSUSED`).

### 6.4 The two block constants

Both denominator conventions are printed at every rule and both arenas. Three
facts:

1. **Every density is constant from B to B₂ at 109 of 109 rules**, and the
   additive counts double exactly. This is **forced** by the block-local
   declaration plus copy-forcing: cells are copied into each block, the
   basepoint lies in no cell, and transports never cross blocks, so B₂ is a
   disjoint sum by construction. The verdict says `FORCED-BY-COPYING`.
2. **The values are grid-dependent, and that half is measured.** the per-incidence density runs from 0/1 to 5/3 across the grid;
   within the ALL-mode union classes it reaches 25/18. The span is computed in-gate
   (`G-CONSTANTS-SPAN-COMPUTED`) precisely so that no version of this sentence
   can be typed. The two conventions agree exactly when each drawn pair sits in
   one cell and diverge otherwise (R009: 5/9 against 25/3).
3. **The $b_2$ density is UNDEFINED at 28 rules** — those with $F_{\rm coh}=0$.
   The path is live, reached by shipped inputs, and recorded with its reason.

---

## 7. B₂, the controls, and the successor control

### 7.1 Persistence at B₂ — and what the declaration forbids

Every locality-bearing rule is re-measured at B₂. Locality survives at 14 of
14, the non-complete component count doubles at 14 of 14, and componentwise
completeness is unchanged at 14 of 14. All three are **forced** by the
block-local declaration, and the verdict says so.

The pin asked for this to be checked "against a case where blocks could
interact". Inside the delivered declaration they cannot: block-locality is
exactly the statement that they do not. The honest report is therefore that the
B₂ result is a property of *block-locality*, not of block addition, and that
the control the pin was reaching for does not exist in this construction. The
gate is rebuilt so that it can at least fail: the set it measures is derived
afresh from `per_component` rather than being the list it was built by
iterating (`G-B2-PERSISTENCE-MEASURED`, mutant `b2-persistence-drop`).

### 7.2 The positive control, the scramble, the parity witness

A hand-declared toy outside the grid with known partial overlap — two cells
$\{1,2,3\}$ and $\{3,4,5\}$ sharing exactly the label 3 — returns a component
of size 5 with 6 of 10 pairs drawn, non-complete (`G-POSITIVE-CONTROL`, mutant
`toy-broken`). Scrambling the drawn maps over a tested set fixed by declaration
(every grid rule with $F(N)>0$, 81 of them) moves the identification-sensitive
measure at 81 of 81 and leaves the component census unchanged at 81 of 81:
locality is a fact about the cells, coherence a fact about the maps. The
Boolean connective at the 2-cell boundary carries its witness — replacing
pairwise-drawn by any-pair-drawn changes the 2-cell count at 78 of 90 rules,
total measured delta 4000 (mutant `parity-inert`). The symmetry self-test
evaluates fresh with the memo bypassed, and the cache's own hit and miss counts
are gated non-zero (1289 hits, 212 misses, 48 fresh evaluations).

### 7.3 The successor control: the grid's boundary, made visible

Both declared transports have **fixed points** — T7 fixes 0; T4 fixes 0 and 1
and carries the 2-orbit $\{6,7\}$ — so the regular orbit is never the whole
label set and the coset-position circulant, restricted to it, is not
vertex-transitive. *That*, and not width-based overlap, is the obstruction to a
chart-independent dimension at this scale. The claim is testable, so it is
tested: the same sliding class is run at a fixed-point-free transport (the
8-cycle), outside the declared grid and claiming nothing about the substrate.

| $c$ | edges | 2-cells | non-complete | cell-indexed reading | chart-intrinsic reading | link (cell mult.) | link (simple) |
|---|---|---|---|---|---|---|---|
| 2 | 8 | 0 | yes | INCONSISTENT | **CONSISTENT** | (2,0,2,0) | (2,0,2,0) |
| 3 | 16 | 8 | yes | INCONSISTENT | **CONSISTENT** | (4,3,1,0) | (4,3,1,0) |
| 4 | 24 | 32 | yes | INCONSISTENT | **CONSISTENT** | (6,12,1,7) | (6,9,1,4) |

at width 2 the drawn graph is an 8-cycle: a triangulated 1-manifold, every link two points, and the chart-intrinsic reading is CONSISTENT.
$(2,0,2,0)$ is $S^0$ — the correct link for dimension one. The width-$4$ row is
also where the link convention shows its teeth: the same object reads
$(6,12,1,7)$ and $(6,9,1,4)$ under the two conventions, which is why both are
printed everywhere in this paper.

Two things follow. First, a consistent, manifold-correct reading *is* reachable
in this grid class; the obstruction is the transports' fixed points and it is
removable. Second, the sufficient conditions are now stated as measured
requirements for any successor: a transport acting **regularly on the whole
arena** with the cover permuted transitively, and a **chart-intrinsic** reading
— compared as a multiset of local dimensions, never as a vector indexed by the
external cell list. Under that repaired reading the 14 grid rules still read
INCONSISTENT (2 to 5 distinct profiles), so the repair is not a whitewash: it
separates *forced by indexing* from *really inhomogeneous*
(`G-SUCCESSOR-CONTROL`, mutant `successor-control-broken`).

---

## 8. The instrument

69 gates, all passed; 11 anchors; 54 declared mutants, all dead. Two plain
delivery runs are byte-identical in both artifacts. The falsification selftest
re-invokes the instrument once per mutant and requires exit 1, a death
certificate naming the expected gate, and the on-disk artifacts unchanged. No
gate predicate reads mutant identity: every injection lives in a measured
function or in the rendered object.

**The verdict gate.** The emitted string is compared for equality against
`reconstruct_verdict_from_receipt()`, which shares no code and no input with
the builder: it reads the receipt's own stored tables — `census_rows`, `grid`,
`standards`, `width_law`, `motivation_census`, `null_census`, `grid_boundary`,
`block_constants_summary` — and re-derives all fourteen segments. A comparator
that cannot disagree with the object under test verifies nothing, so five
injection classes are declared and all five die on it: a name↔value swap
(`verdict-pair-swap`), a typed segment (`verdict-typed-segment`), appended text
(`verdict-append-text`), a typed gateway-style claim
(`verdict-typed-motivation`), and a fully typed fourteen-segment verdict naming
a rule that does not exist (`verdict-fully-typed`).

**Flippability is tested at the measurement, not at the string.** For each
segment the instrument perturbs *the receipt row the segment is derived from*
and requires the independent reconstruction to move. A segment that is a
constant in both paths therefore fails, and `verdict-inert-segment` is that
falsifier.

**Anchors bind values, not only bytes.** Six path-value rows name their JSON
path and their expected value; `path-drift` — a single key changed from
`['4']` to `['6']`, which on the delivered instrument produced a 115-rule
grid, an order-2 transport and an entirely different verdict at exit 0 with
every anchor green — now dies by name on `P-I6-GAMMA4`. Every anchor row
carries its own corruption mutant.

**The render check is total.** Every rendered field of every rendered object is
rebuilt from the live measurement and compared, rather than a chosen subset of
ten (`render-escape` is the falsifier, corrupting seven cells that the previous
check did not reach). The receipt is also checked against *itself*
(`G-RECEIPT-INTERNALLY-CONSISTENT`, mutant `internal-contradiction`).

**The falsifier census is in the receipt, with an honest denominator.**
25 of 69 gates carry no declared falsifier, and 14 of those are waived with their forcing stated;
the rest are named, not waived. The waiver rows say what forces each gate —
analytically forced clauses (R2-A at this unit's actions, the partition
corollary, the coherence corollary, the alt-drawing probe), declared scope
statements, and the instrument's own bookkeeping.

**The prose surface is gated too.** Every load-bearing numeric sentence in this
paper is rendered by the instrument from the receipt object and must appear
here verbatim; `prose-claim-drift` demonstrates that the gate fires when a
rendered claim stops matching its measurement. This is the surface on which all
four of the programme's false paper numbers to date lived.

---

## 9. What this unit found

1. **Locality is declarable.** 14 of 109 rules produce a component that is not complete,
   every one a partial-coset-overlap rule. The criterion R1 handed forward,
   measured empty across R1's whole family, is non-empty here.
2. **And the census is a corollary of the declaration, not a discovery.** The
   width law predicts every rule's status and edge count from the declaration
   at 109 of 109, with closed forms for $|E|$ and $b_1$; the two transports'
   thresholds have different causes. The census clauses are carried forced.
3. **Nothing in the inheritance motivates the cover.** No inherited group can
   (all 4140 set partitions of the eight labels at both transports -- 8280 measurements, 0 non-complete), and the one
   motivated partial-overlap cover the corpus owns — I6's own seven Fano lines
   — is a locality-*destroyer*, because a 2-design covers every pair. The
   mechanism's essential ingredient is the integer labelling, and the rule
   list moves with it: 11 distinct rule sets over the numberings, with the
   declared one modal.
4. **The drawing relation decides the verdict.** At
   $\langle\gamma,\Sigma\rangle$ nothing is drawable and the head flips. It is
   now a named verdict coordinate.
5. **Dimension and locality are disjoint in this grid, and why.** CONSISTENT is attained at 22 of 109 rules and its intersection with the locality census is empty;
   theorem R2-D says the exclusion is analytic under a cell-indexed reading.
6. **And the escape is constructive.** At a fixed-point-free transport the same
   sliding class yields a triangulated 1-manifold with a consistent
   chart-intrinsic reading. The obstruction is the transports' fixed points.
7. **The standards return nothing manifold-shaped where locality lives.**
   0 of 80 links is a triangulated circle, under either convention's
   Betti reading the count is convention-relative, and the local dimensions are
   an identity in the declared width.
8. **Degree one becomes non-trivial for the first time in these arenas**, at
   9 of the 14, with the closed forms giving the cycle ranks from $(k,m,c)$.
9. **Declared locality does not disturb the copying invariance** — forced by
   block-locality — while the constants' *values* move across the grid.

## 10. What this unit does not claim

- **No continuum claim.** R1's question is untouched.
- **No claim about the substrate's own locality.** The unit claims
  existence-in-atlas-space and the walls around it: that the criterion is
  satisfiable by a declaration, at a computable width, with no inherited
  motivation, and with a numbering-relative rule list. Whether the substrate
  carries a locality of its own is a different question, on a different arena,
  and it is handed forward in §11 rather than answered here.
- **No geometric-type claim.** The standards are ported as disclosures; the one
  place this paper says "1-manifold" is the fixed-point-free control, where it
  is a measured graph-theoretic property declared outside the grid.
- **No claim that the grid is the space of all atlases.** It is declared,
  finite, exhaustively enumerated, and its boundary is measured: 60 rules constructible from the same declared words are excluded, and 1 of them bears locality.
- **No claim about $\varphi$.** R1's gateway is forced by the basepoint and
  this unit does not use it.

## 11. What the next rung inherits

- **The arena, and it is not a component of this grid.** The 14 components
  cannot carry hypersurface-deformation questions: their dimension reading is
  forced inconsistent, five of them carry no 2-cell at all and the largest
  carries 20, there is no direction structure, and the locality is
  numbering-relative. The corpus already owns a better arena. *(The I7 figures
  in this bullet are the R2 adjudication's recorded measurements on I7's own
  declared lattice, taken outside this instrument; they are carried here as the
  successor's input and are not gated by this unit's receipt. Everything else
  in this paper is.)* I7's record layer *declares*, as data, a site lattice
  with a declared link set
  (`links_d2`, `links_d3`), a `chart_group` acting on sites, link counts, lapse
  profiles and every tensor index, and a `lapse_family`. Measured against this
  unit's own criterion and standards, that lattice **satisfies the locality
  criterion** (64/120 at $d=2,L=4$; 324/351 at $d=3,L=3$; 768/2016 at
  $d=3,L=4$), is translation-covariant, and returns a **consistent**
  chart-intrinsic dimension with a **single link profile at every site** —
  $(8,12,1,5)$ at $d=2$ and $(24,96,1,73)$ at $d=3$. It fails only at
  $d=2, L=3$, where nine sites are too few and every difference is a link
  combination. **$L\ge 4$ is therefore a measured requirement** for the
  successor, with the $L=3$ degeneracy as its own control.
- **The successor requirements, as measured conditions**: an inherited
  proximity datum rather than a label order; a declared group transitive on the
  cells; relabelling-invariance of the rule list, swept and printed; a cover
  that is not a design; a chart-intrinsic reading; and a manifold link rather
  than a Betti coincidence. A consistent dimension is necessary and far from
  sufficient — even at I7's lattice the link is $(8,12,1,5)$, not a sphere.
- **This grid as the null control**: a declared, numbering-relative locality on
  which the ported standards demonstrably return nothing — the negative
  baseline a deformation claim needs.
- **The finding that the cocycle condition is free** at this drawing relation
  ($N_{\rm coh}=N$), so identification content must be sought elsewhere.
