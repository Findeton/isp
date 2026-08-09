# R1 — The continuum rung

**Status:** GREEN-REPAIRED 2026-08-09 (v14 ledger #2 pin; delivered against
`v14/note-r1-continuum-pin.md`, sha256-12 `27c9f1144ffa`).

**Artifacts:** `v14/code/r1_continuum_exact.py`,
`v14/code/r1_continuum_output.txt`, `v14/code/r1_continuum_receipt.json`.

---

## Abstract

A refinement family of five arenas is declared before anything is computed,
its growth rule extracted as data from a hash-pinned predecessor receipt, and
five intensive invariants are registered before any of them is evaluated. The
family's own atlas is built at every member and the five invariants are read
off it exactly, in integer and rational arithmetic only.

Two of the five are exactly constant on the declared three-member window at
$37/27$ and $20/37$. **The finding of this unit is why**, and it is not a
convergence. The declared growth rule adds an *isomorphic copy* of a block.
Measured: the block count plus the basepoint equals $b_0$ of the nerve at
$5$ of $5$ members, no $1$-cell crosses a block anywhere, and at every window
member the bijection the declared cyclic orders name is measured to
intertwine the arena symmetry and to carry one block's cyclic order to
another's. The nerve and its coherent sub-nerve are therefore $m$ disjoint
copies of a single block's atlas together with an isolated basepoint, and
every ratio of two block-additive, point-vanishing counts is independent of
$m$ — a theorem, proved and verified here. **Both stabilised values already
hold at $m = 1$, the single-block member.** The affine law of every counting
quantity, fitted from the one- and two-block censuses alone, predicts every
later member exactly ($100$ of $100$ at $m = 3\ldots12$), and $26$ of the
$26$ data points contributed by the window's second and third members are
those predictions. Nothing converges; the window carries one block's census.

What discriminates the mechanism is *isomorphic* copying and not addition: a
mixed-block family with the same disjoint addition, the same symmetry-stable
blocks and the same $b_0 = \text{blocks} + 1$, differing only in that its
blocks are not isomorphic to one another, **moves** both densities.

Three further measurements decide what the unit may claim. The atlas is
**verdict-determining**: over the same arenas and the same five invariant
definitions, three transport-convention re-declarations leave both values
fixed, dropping the realised cell moves them to $5/3$ and $4/7$, a
non-block-local declaration stabilises *nothing* and flips the head to
`NO-CONTINUUM-LIMIT`, and a one-cell-per-block declaration leaves both
headline invariants *undefined*. Deleting the single structureless basepoint
makes $4$ of $5$ invariants constant, so the registered split is between
basepoint-blind and basepoint-sensitive rather than between substantive and
not. And the inherited locality gateway is **withdrawn**: $\varphi < 1$ is
forced by an isolated basepoint at every member, componentwise overlap
completeness is $1$ at $7$ of $7$ members and probes, and the successor
criterion that has teeth — the first component whose overlap graph is
incomplete — is measured **empty**.

The honest deliverable is therefore two-sided and complete: this family
cannot answer the continuum question, for a proved reason, and the unit
states what a family that could must do.

---

## 1. The question

> Does a declared refinement family over the v13 substrate admit a
> pre-registered **intensive** invariant that stabilizes under refinement?

Both answers are first-class. The instrument can emit
`R1-STABILIZES-...-AT-<...>` and `R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE`,
the head is derived from the measured count of stabilised invariants inside a
gate, and both heads are exhibited on real measurements — by the positive and
negative controls of §13, and by one of the alternative declared atlases of
§10, which returns the `NO-CONTINUUM-LIMIT` head over these same five arenas.

Nothing in the family, the invariants or the window is chosen after a number
is seen. The family is declared in the pin; the growth rule is extracted from
a pinned receipt; the five invariants are registered in the pin before any is
computed; the stabilisation window is the pin's $K = 3$. The instrument
counts every measured datum through a single counter and gates that counter
to be **zero** at the point where the declarations end.

## 2. The inheritance

The founding pin's inheritance is hashed at run time and compared against its
own record: eight entries — the seven inherited results, with I1 and I2
sharing one carrying receipt — plus the charter and both pins. All match.

| row | carrying artifact | sha256-12 |
|---|---|---|
| I1, I2 | `v13/code/rsq_reposed_square_receipt.json` | `85f3cf809544` |
| I3 | `v13/code/top_topology_receipt.json` | `65bb1fc5231f` |
| I4a | `v13/note-top-adjudication.md` | `e4934f2525b0` |
| I4b | `v13/note-rsq-adjudication.md` | `31b70406c6e8` |
| I5 | `v13/code/lcb_livecell_receipt.json` | `3e502f685ab3` |
| I6 | `v13/code/tb3_third_base_receipt.json` | `c9bc956fe751` |
| I7 | `v13/code/ha_successor_receipt.json` | `542b8735daf0` |

The table above is not merely typed here. The founding pin's markdown is
**parsed at run time** — seven rows, nine (artifact, hash) pairs, fifteen
hashes — and the parsed set is compared against the typed set in both
directions, so a typed hash absent from the pin and a pinned hash absent from
the code are equally caught. Nothing of the predecessor is imported as code.
Every number this unit reuses is read from those bytes and recomputed here.

**A companion-hash finding.** The founding pin also names companion artifacts
in parentheses. Six of the eight reproduce. The two that do not are the two
**papers**:

| companion | recorded in R0 | measured | cited here |
|---|---|---|---|
| `v13/paper-rsq-reposed-square.md` | `07bea42728a2` | `f80317a25037` | v14 LOG #4 erratum |
| `v13/paper-top-topology.md` | `4e4cd4f11bab` | `379194959fbc` | v14 LOG #4 erratum |

What the instrument measures is exactly those columns and the set on which
they differ, and the gate requires the erratum set to be exactly the set on
which the cited value differs from R0's own — so a silent substitution where
none was recorded, or a failure to apply one where it was, dies the same way.
The provenance, read separately from the repository's history, is that the
two recorded values are each the paper's hash at its **repair** commit and
that each paper was edited once more afterwards, at its terminal commit. The
two entries are stale by one commit, not invented.

The primary key of every inheritance row — the carrying **receipt** —
verifies, all six other companions verify, and no number of this unit is read
from a paper, so the run proceeds and the delta is carried as disclosure
`X-COMPANION-HASH` rather than smoothed away.

## 3. The declared family

### 3.1 What an arena is here

An arena is a finite label set $L$ with a distinguished label $0$, a declared
chart symmetry $\Sigma \in \mathrm{Sym}(L)$, and the declared block partition
of $L \setminus \{0\}$ — the orbits of the arena's own completion subgroup.
Nothing outside $(L, 0, \Sigma, \text{blocks})$ enters any construction. Every
coordinate of that declaration is printed at every member and the comparison
across members is made on the printed table, never on a name.

### 3.2 The growth rule, extracted as data

The predecessor's receipt carries its growth family verbatim:

> `L_m = {0} + (F_2^3 minus 0) x {1..m}: m copies of TB3's seven moved
> labels, with S_3 acting on the F_2^3 factor alone and fixing label 0.
> m = 1 is TB3's native arena.`

The rule's parameters are parsed out of that string rather than typed: base
$2$, exponent $3$, hence block width $2^3 - 1 = 7$ and
$\lvert L_m\rvert = 7m + 1$. The member-selection rule is the smallest $m$
whose blocks can carry an elementary abelian subgroup of the record rank at a
prime, $m^*(p) = \min\{m : 7m \ge 6p\}$.

Both are required to reproduce the receipt's whole scale-threshold table
before any new member is built:

| $p$ | $m$ | labels | elementary threshold | divisibility threshold |
|---|---|---|---|---|
| 5 | 5 | 36 | 31 | 26 |
| **7** | **6** | **43** | **43** | **43** |
| 11 | 10 | 71 | 67 | 67 |
| 13 | 12 | 85 | 79 | 79 |
| 17 | 15 | 106 | 103 | 103 |
| 19 | 17 | 120 | 115 | 115 |
| 23 | 20 | 141 | 139 | 139 |

Every one of those 28 cells is an anchor. The block width is separately
cross-anchored against the third base's own moved-label count: $8 - 1 = 7$,
and $L_1$ has $8$ labels, which is that base's native arena.

**The rule's own text is what makes the blocks isomorphic**, and it says so
without any computation: *$m$ copies of the same seven moved labels*. That
sentence is the hypothesis §8 turns into a theorem.

### 3.3 The five members

No label count is typed. $A_1$'s nine come from inverting the factorial of
the pinned completion-family size ($40\,320 = 8!$, so $n - 1 = 8$); $A_2$'s
sixteen come from the pinned arena rule $\mathrm{rank}\cdot p + 1$ with the
rank read off the record-space size $125 = 5^3$ and the prime solved for;
$A_3$'s forty-three come from the extracted rule at the member the rule
itself selects; $A_4$ and $A_5$ are the family's next two members.

| member | labels | blocks | block sizes | $\mathrm{ord}(\Sigma)$ | $\Sigma$ cycle lengths | provenance |
|---|---|---|---|---|---|---|
| $A_1$ | 9 | 1 | 8 | 2 | 1, 2 | I5's nine-label completion arena |
| $A_2$ | 16 | 3 | 5, 5, 5 | 2 | 1, 2 | I5's sixteen-label successor arena |
| $A_3$ | 43 | 6 | 7 each | 3 | 1, 3 | I2's grown arena $L_6$ |
| $A_4$ | 50 | 7 | 7 each | 3 | 1, 3 | $L_7$, the rule's next member |
| $A_5$ | 57 | 8 | 7 each | 3 | 1, 3 | $L_8$ |

The family is a gluing of three constructions, as the pin declares it: $A_1$
and $A_2$ come from one predecessor, $A_3$ from another, and $A_4$, $A_5$
from $A_3$'s own rule. Only the last three are members of that rule's family,
and §6 and §11 both carry that restriction as measured data rather than as a
caveat.

Before $A_4$ is built, the extracted rule is required to regenerate $A_3$ from
scratch — label set, block partition and symmetry, coordinate by coordinate —
with the memo **bypassed**, the bypass count measured to have risen, and the
self-test's cache-hit count measured zero against a non-zero lookup count.

## 4. The atlas

The atlas over an arena is declared before it is built.

- **Charts** are the labels of $L$.
- **Coordinate cells** are pairs $(k, \text{rule})$ with $k$ a block index and
  the rule one of two. The FULL transport at cell $k$ is $\gamma_k$, the
  increasing-index cycle on block $B_k$. The REAL transport is
  $\Sigma_k\gamma_k$, where $\Sigma_k$ is the arena symmetry restricted to the
  $\langle\Sigma\rangle$-saturation of $B_k$ and extended by the identity —
  the block transport as the chart symmetry realises it on that patch.
- **Drawn.** An ordered pair $(a,b)$, $a \ne b$, is drawn at a cell iff
  **exactly one** element $\pi$ of that cell's cyclic transport group
  satisfies $\pi(a) = b$; the drawn map is that $\pi$.
- $N$, the coordinate-resolved nerve: $0$-cells the charts; $1$-cells one per
  unordered drawn pair **per coordinate cell**; $2$-cells the unordered chart
  triples pairwise drawn at a **common block index**, one rule chosen per
  edge.
- $N_{\mathrm{coh}}$: the $2$-cells of $N$ whose three drawn maps compose to
  the identity — the cocycle condition transition maps must satisfy.
- $G$, the overlap graph: simple, an edge wherever an identification is drawn
  at some cell.

The measured census:

| member | cells | transport orders | drawn ordered pairs per cell | overlap edges | $1$-cells | $2$-cells | coherent |
|---|---|---|---|---|---|---|---|
| $A_1$ | 2 | 8, 4 | 56, 24 | 28 | 40 | 160 | 96 |
| $A_2$ | 6 | 5, 10 (each block) | 20, 0 | 30 | 30 | 30 | 30 |
| $A_3$ | 12 | 7, 3 | 42, 12 | 126 | 162 | 438 | 222 |
| $A_4$ | 14 | 7, 3 | 42, 12 | 147 | 189 | 511 | 259 |
| $A_5$ | 16 | 7, 3 | 42, 12 | 168 | 216 | 584 | 296 |

Both censuses are taken twice. The $1$-cells from the ordered pair tables
agree with the count from the unordered edge list; the $2$-cells from the
construction loop agree with a multiplicity-product census taken from a
per-block pair-multiplicity dictionary that shares no edge index, no triple
key and no intermediate with it. The coherent count is recounted by a
comparator that ranges over **every** $2$-cell of $N$ — not over the list the
construction already filtered — rebuilding each cell's three drawn maps from
the edge table alone and re-composing them, so a coherent cell wrongly
*excluded* moves the recount and not the flag.

### 4.1 What the atlas can draw, and why

The drawn counts above are not a coincidence; they are a corollary.

> **Theorem A (the admission rule).** Let a cyclic group of order $N$ act on
> a finite set and admit an ordered pair $(a,b)$, $a \ne b$, iff **exactly
> one** group element carries $a$ to $b$. Then $(a,b)$ is admitted iff
> $b$ lies in the orbit of $a$ **and** that orbit is **regular**, i.e. has
> size $N$.
>
> *Proof.* The exponents $k$ with $\tau^k a = b$ are empty when $b$ is
> outside the orbit, and otherwise form a coset of the stabiliser of $a$,
> whose size is $N / \lvert\mathrm{orbit}(a)\rvert$. That coset is a
> singleton exactly when the orbit length is $N$. $\square$
>
> **Corollary.** The admitted relation at a cell is the disjoint union of
> **complete** graphs on the regular orbits, non-regular orbits drawing
> nothing; so an overlap graph assembled from such cells is always a union
> of cliques.

The statement is true by algebra for every input, so it is disclosed rather
than gated, and checked exhaustively all the same over every cyclic action
generated by a permutation of $n = 2\ldots6$ points — $872$ permutations,
zero counterexamples. What is *gated* is the claim that can fail: that this
unit's own atlas is an instance. At every coordinate cell of every member and
probe, the cell's drawn table is compared for set equality against the
ordered pairs lying inside its regular orbits, and the disagreeing-cell count
is measured zero. A widened admission rule makes a cell draw outside its
regular orbits and the gate dies.

Two consequences are immediate and are used later. **The realised rule draws
nothing at $A_2$** — there the realised transport has order $10$ on a
seven-label symmetry saturation, no orbit is regular, and the admission rule
refuses every candidate; at that member alone coherence is analytically
forced and $N$ coincides with $N_{\mathrm{coh}}$. And **every overlap graph
this schema builds is a union of cliques**, which is what §12 turns into the
successor's problem.

### 4.2 The machinery is calibrated against the pinned topology base

The homology identities this instrument uses —
$\chi = V - E + F$, $\operatorname{rank}\partial_2 = F - b_2$,
cycle rank $= E - V + b_0$, $b_1 = \text{cycle rank} - \operatorname{rank}\partial_2$
— are evaluated here on the pinned receipt's own published cell counts, for
both its nerve and its coherent sub-nerve, and each result is anchored
exit-1 against that receipt's independently recorded value:

| complex | $\chi$ | $\operatorname{rank}\partial_2$ | cycle rank | $b_1$ |
|---|---|---|---|---|
| $N$ | 198 984 | 5 261 | 5 401 | 140 |
| $N_{\mathrm{coh}}$ | 79 320 | 5 240 | 5 401 | 161 |

together with the coordinate count $(T-1)(V-1) = 4\cdot 35 = 140$. This is
the machinery's external calibration; the atlas's own census is protected
separately, by the unfiltered recount of §4 and by Theorem A's confrontation
with the cells.

## 5. The registered invariants

Five, fixed in the pin before any was computed.

1. **$\varphi$, the overlap-completeness fraction** — drawn chart pairs over
   all chart pairs.
2. **$N_{\mathrm{coh}}$ density** — coherent $2$-cells per drawn chart pair.
   The pin's phrase admits two readings of the denominator and **both are
   computed and printed** (§11).
3. **The normalised spectral profile of $I - E$** — over the arena's readouts
   $E = \rho_L(\pi)$, $\pi \in \langle\Sigma\rangle\setminus\{1\}$, the map
   $d \mapsto \mathrm{mult}(\Phi_d)/\dim$.
4. **The per-volume dimension profile** — the link-dimension distribution
   normalised by chart count.
5. **$b_2$ density** — $b_2$ of $N_{\mathrm{coh}}$ over $\mathbb F_2$, per
   $2$-cell; again both readings of the denominator are printed.

Two quantities are **excluded** by the pin and are not candidates: the raw
local-dimension estimator, provably extensive; and $b_1$. The $b_1$ exclusion
is a **declaration, not a measured triviality**, and this unit says so with
its own measurement: on $N$, $b_1$ is zero at every member — the trivial
first homology the topology base reports, reproduced here — but on
$N_{\mathrm{coh}}$ it is $2, 0, 24, 28, 32$, non-zero exactly where the
identification data is imposed, and its density
$b_1(N_{\mathrm{coh}})/\lvert F(N_{\mathrm{coh}})\rvert$ is constant at
$\mathbf{4/37}$ on the window and at both index probes. A sixth intensive
quantity of this substrate stabilises and was excluded by declaration; the
registered score of $2$ of $5$ is a registry fact, and counting the excluded
candidate it is $3$ of $6$. Both are carried in the verdict.

Each invariant is computed by two routes or against an independent
comparator: $\varphi$ from the edge list and from an accumulation that never
forms one; the coherent count once flagged during construction and once
re-composed from the unfiltered $2$-cell list; the link-vertex count from the
edge list and from a second pass over the per-cell tables; $b_2$ against a
comparator formed without passing through the complex selector. Components
and cycle rank are computed by two genuinely independent routes at every
complex of every member, and $\operatorname{rank}\partial_2$ under two pivot
disciplines whose pivot **sets** are measured to differ on a declared probe.

**On the spectral wall.** The inherited result guarantees that the readout
carries the eigenvalue $1$. Two clauses of this unit's spectral census are
analytically forced and are recorded as disclosures rather than gated: the
eigenvalue-$1$ presence clause is $\mu_1 \ge 1$ with $\mu_1$ the readout's
cycle count, which no permutation of a non-empty set can violate; and the
degree identity $\sum_d \varphi(d)\,\mathrm{mult}(\Phi_d) = n$ is a
permutation identity. Both are swept exhaustively over all permutations of
$n = 2\ldots6$ with zero violations. **And the chain is about a different
operator from the inherited wall.** I2's $E$ is the record–metric readout
over $\mathbb F_p$, its pinned rows indexed by dimension, direction, ordering
and prime; this unit's $E$ is the arena's chart-symmetry permutation matrix
over $\mathbb Q$, indexed by member and readout, and the two coordinate sets
are measured disjoint. What this unit confirms — $0 \in \mathrm{spec}(I-E)$
for a permutation readout — is implied by the permutation form alone and
re-confirms neither I2's criterion, nor its unit-circle clause, nor its
prime-indexed universality. It is a strictly weaker statement about a
different operator; the wall is cited, not re-derived. What the gate retains
is the clause that can fail: that the multiplicity taken as a cycle count and
the multiplicity taken as the exact rational kernel dimension of $I - E$ by
elimination over $\mathbb Q$ agree at every readout of every member — a
numerical implementation comparator, named as one.

Two of this unit's anchors are recorded the same way. The two
$\delta$-fixed-point anchors compare a pinned recorded count against a
recomputation of $\lvert\{q : \delta(q) = q\}\rvert$ with
$\delta(q) = \sigma(q)^{-1}q$; but $\delta(q) = q$ iff $q$ is the identity,
for every symmetry — measured exhaustively over $\mathrm{Sym}(4)$ and
$\mathrm{Sym}(5)$. They carry no information about the arenas and are
recorded as inheritance checks rather than arena calibration, staying exit-1
because a drifted pinned receipt would still be caught.

## 6. The maps, and functoriality

An **admissible arena morphism** $\iota : A \to A'$ is an injection of label
sets with $\iota(0) = 0$, $\iota\Sigma_A = \Sigma_{A'}\iota$, and a
block-index injection $\sigma$ with $\iota(B_k) \subseteq B'_{\sigma(k)}$.
Equivariance forces every $\langle\Sigma_A\rangle$-orbit to map bijectively
onto a $\langle\Sigma_{A'}\rangle$-orbit of the **same** size, so the search
is a finite orbit-and-block matching, decided exhaustively, and a witness is
constructed whenever one exists.

| step | outcome | measured reason |
|---|---|---|
| $A_1 \to A_2$ | no morphism | block width decreases: the largest source block has 8 labels, the largest target block has 5 |
| $A_2 \to A_3$ | no morphism | orbit size unavailable: $\langle\Sigma_A\rangle$ has orbit sizes 1 and 2, and the target carries no orbit of size 2 |
| $A_3 \to A_4$ | admissible | constructed |
| $A_4 \to A_5$ | admissible | constructed |

Where morphisms exist their equivariance, injectivity, basepoint
preservation, identity and composition are each measured and hold. The
criterion admits some steps and refuses others, so it is not a constant
function. The computed qualifier is
`FAMILY-NON-FUNCTORIAL-AT-2-OF-4-STEPS`.

**Restricted to the homogeneous tail the reading changes, and the verdict
carries both.** $A_3, A_4, A_5$ are exactly the members the extracted
generator rule produces, they are exactly the members the $K = 3$ window
covers, and they are exactly the steps that carry constructed morphisms. On
that tail the family is `FAMILY-FUNCTORIAL`, the stabilised set and both
values are unchanged, and every divergence mode is unchanged. So the
non-functoriality is a statement about the *gluing*, not about the growth
rule, and the two steps that fail join arenas built by different
constructions.

## 7. The trajectory

All five invariants at all five members, exact:

| invariant | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
|---|---|---|---|---|---|
| $\varphi$ | $7/9$ | $1/4$ | $6/43$ | $3/25$ | $2/19$ |
| $N_{\mathrm{coh}}$ density | $12/5$ | $1$ | $\mathbf{37/27}$ | $\mathbf{37/27}$ | $\mathbf{37/27}$ |
| spectral profile | $\{1\!:\!\tfrac23,\,2\!:\!\tfrac13\}$ | $\{1\!:\!\tfrac58,\,2\!:\!\tfrac38\}$ | $\{1\!:\!\tfrac{19}{43},\,3\!:\!\tfrac{12}{43}\}$ | $\{1\!:\!\tfrac{11}{25},\,3\!:\!\tfrac{7}{25}\}$ | $\{1\!:\!\tfrac{25}{57},\,3\!:\!\tfrac{16}{57}\}$ |
| dimension profile | $\{0\!:\!\tfrac19,\,7\!:\!\tfrac89\}$ | $\{0\!:\!\tfrac1{16},\,4\!:\!\tfrac{15}{16}\}$ | $\{0\!:\!\tfrac1{43},\,6\!:\!\tfrac{42}{43}\}$ | $\{0\!:\!\tfrac1{50},\,6\!:\!\tfrac{49}{50}\}$ | $\{0\!:\!\tfrac1{57},\,6\!:\!\tfrac{56}{57}\}$ |
| $b_2$ density | $65/96$ | $2/5$ | $\mathbf{20/37}$ | $\mathbf{20/37}$ | $\mathbf{20/37}$ |

Twenty-five cells written against a forced product of twenty-five. This table
is the one the gates check and the one the receipt and this paper render
from: every emitted cell is compared for string equality against the
canonical form of the live measurement at that coordinate, so a corrupted
cell is caught by the same gate that catches a dropped one. The supporting
Betti data:

| member | $b_0(N)$ | $b_1(N)$ | $b_2(N)$ | $b_0(N_{\mathrm{coh}})$ | $b_1(N_{\mathrm{coh}})$ | $b_2(N_{\mathrm{coh}})$ |
|---|---|---|---|---|---|---|
| $A_1$ | 2 | 0 | 127 | 2 | 2 | 65 |
| $A_2$ | 4 | 0 | 12 | 4 | 0 | 12 |
| $A_3$ | 7 | 0 | 312 | 7 | 24 | 120 |
| $A_4$ | 8 | 0 | 364 | 8 | 28 | 140 |
| $A_5$ | 9 | 0 | 416 | 9 | 32 | 160 |

**Stabilisation** is exact constancy on the final $K = 3$ members, with $K$
declared in the pin. The window is load-bearing and calibrated both ways on a
crafted fixture declared in advance — the trajectory $1/2,\,1/3,\,2/5,\,2/5$
is **not** stabilised at $K = 3$ and **is** at $K = 1$ — so a window shrink
flips a verdict.

## 8. The copying theorem: what the constancy is

This is the unit's finding.

### 8.1 The hypothesis, and why it is not additivity

Disjoint addition alone does **not** make a ratio of two per-cell counts
invariant. The load-bearing hypothesis is disjoint addition **of an
isomorphic copy**, and the difference is measurable.

> **Hypothesis (isomorphic copying).** The labels are
> $\{0\} \sqcup B_1 \sqcup \cdots \sqcup B_m$ with $\Sigma$ fixing $0$ and
> stabilising each block, and for each $k$ there is a bijection
> $\beta_k : B_1 \to B_k$ intertwining $\Sigma$ and carrying $B_1$'s declared
> cyclic order to $B_k$'s.

Measured at every member: $b_0(N)$ equals the block count plus one at $5$ of
$5$; cross-block $1$-cells number $0$ everywhere; and the intertwiner
$\beta_k$ is measured to exist, to intertwine $\Sigma$ and to carry the
cyclic order at $4$ of the $5$ members — the exception being $A_2$, whose
blocks are measured *not* $\Sigma$-stable, so the hypothesis genuinely has
content and is not satisfied by declaration alone.

### 8.2 The theorem

> **Theorem B (copy-forcing).** Under the hypothesis, (i) $N$ and
> $N_{\mathrm{coh}}$ are the disjoint union of $m$ copies of the block-$1$
> atlas together with the isolated chart $0$; (ii) for any two quantities
> $X, Y$ additive over connected components and vanishing on an isolated
> vertex, $X(A_m)/Y(A_m) = X(A_1)/Y(A_1)$ for every $m$; (iii) every counting
> quantity of the atlas has the affine form $am + b$ with $b$ the basepoint's
> contribution, and a ratio of two of them is constant in $m$ **iff** the
> cross product of their $(a,b)$ vanishes.
>
> **Corollary B′ (the converse half).** A quantity $A(N_m)/n$ with $A$
> additive and $n = m\lvert V(X)\rvert + 1$ is constant **iff**
> $A(X) = A(p)\lvert V(X)\rvert$; generically it is not, and then its whole
> variation is the single basepoint's share.

Theorem B is verified in-unit the only way a forcing claim can be: the affine
law $am+b$ of every counting quantity is **fitted from the one-block and
two-block censuses alone**, and every later member is then a *prediction*.
The predictions hold for all ten counting quantities at $m = 3\ldots12$ —
**$100$ of $100$**.

| $m$ | labels | $\lvert E\rvert$ | overlap | $\lvert F\rvert$ | coherent | $b_2(N_{\mathrm{coh}})$ | $N_{\mathrm{coh}}$ density | $b_2$ density | $\varphi$ |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **8** | **27** | **21** | **73** | **37** | **20** | **37/27** | **20/37** | 3/4 |
| 2 | 15 | 54 | 42 | 146 | 74 | 40 | 37/27 | 20/37 | 2/5 |
| 6 | 43 | 162 | 126 | 438 | 222 | 120 | 37/27 | 20/37 | 6/43 |
| 7 | 50 | 189 | 147 | 511 | 259 | 140 | 37/27 | 20/37 | 3/25 |
| 8 | 57 | 216 | 168 | 584 | 296 | 160 | 37/27 | 20/37 | 2/19 |
| 10 | 71 | 270 | 210 | 730 | 370 | 200 | 37/27 | 20/37 | 6/71 |
| 12 | 85 | 324 | 252 | 876 | 444 | 240 | 37/27 | 20/37 | 6/85 |

The closed forms are exact at every $m$: $\lvert E\rvert = 27m$, overlap
$= 21m$, $\lvert F\rvert = 73m$, coherent $= 37m$,
$b_2(N_{\mathrm{coh}}) = 20m$, $b_1(N_{\mathrm{coh}}) = 4m$,
$b_0(N) = m + 1$, $\varphi = 6/(7m+1)$.

**The base case is the claim's whole content.** At $m = 1$, the single-block
member, $N_{\mathrm{coh}}$ density is already $37/27$ and $b_2$ density is
already $20/37$. Nothing converges; there is no window in which the values
settle, because they never differed. Of the $26$ data points the window's
second and third members contribute, **$26$ of $26$** are exactly the
one-block census times $m$. The independent content of the three-member
window is **one block's census**.

### 8.3 The discriminating control

The hypothesis is *isomorphic* copying, and a shipped negative control
separates it from mere addition. $MX_m$ is $\{0\}$ plus $m$ copies of the
seven-label block plus **one further block of three labels** carrying a
$3$-cycle of the symmetry. It satisfies every property the additive reading
names — pure disjoint addition, symmetry-stable blocks, no $1$-cell crossing
a block, $b_0 = \text{blocks} + 1$ at every member — and differs only in that
its blocks are not isomorphic to one another.

| member | labels | blocks | $b_0(N)$ | all blocks isomorphic | $N_{\mathrm{coh}}$ density | $b_2$ density |
|---|---|---|---|---|---|---|
| $MX_6$ | 46 | 7 | 8 | no | $115/84$ | $62/115$ |
| $MX_7$ | 53 | 8 | 9 | no | $89/65$ | $48/89$ |
| $MX_8$ | 60 | 9 | 10 | no | $152/111$ | $41/76$ |

Both densities **move**. The disjoint addition is present in full; the
constancy is not.

### 8.4 What is measured and what is forced

The split is stated in the verdict itself. **Measured:** the block
isomorphism, by an exhibited intertwiner, at $4$ of $5$ members; the
per-block census $E = 27$, $F_{\mathrm{coh}} = 37$, $b_2 = 20$; and the atlas
sweep of six declarations. **Forced:** the constancy. Once the hypothesis is
measured to hold, both stabilisations are theorems, not observations, and
they are named as such rather than asserted as independent measurements.

## 9. The verdict

Derived inside a gate from the tables above, and rebuilt inside that gate
segment by segment from the receipt-facing tables and compared for
**equality**, character for character — no clause of the verdict gate is a
containment test, so a value swapped between two names, a typed segment or
text appended to a segment are each caught.

```
R1-STABILIZES-BY-DISJOINT-COPYING-AT-<
  NCOH_DENSITY=37/27-PER-INCIDENCE=37/21-PER-DRAWN-PAIR
 ;B2_DENSITY=20/37-PER-N_COH-2-CELL=20/73-PER-N-2-CELL
 |MECHANISM=DISJOINT-BLOCK-ADDITION:B0=BLOCKS+1-AT-5-OF-5
           ;PER-BLOCK-CENSUS-CONSTANT(E=27;F_COH=37;B2=20)
           ;RATIO-OF-ADDITIVES-FORCED
 |MEASURED=BLOCK-ISOMORPHISM-BY-INTERTWINER-AT-4-OF-5
          ;PER-BLOCK-CENSUS;ATLAS-SWEEP-OF-6-DECLARATIONS
 |FORCED=THE-CONSTANCY
 |INDEPENDENT-CONTENT=ONE-BLOCK-CENSUS(TAIL-DATA-POINTS-FORCED=26-OF-26)
 |DIVERGENT=PHI:STRICTLY-DECREASING-AS-(BLOCKSIZE-1)/N
           ;SPECTRAL_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING
                             -BY-BASEPOINT-SHARE-ONLY
           ;DIMENSION_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING
                              -BY-BASEPOINT-SHARE-ONLY
 |BASEPOINT-DELETED-STABILISING-SET=4-OF-5
  ;SIXTH-STABILISER=B1_NCOH_DENSITY=4/37-PIN-EXCLUDED
  ;SCORE-RESTATED=3-OF-6
 |WINDOW=K=3-OF-5-MEMBERS-NO-CAP-ALL-3-ON-ONE-GENERATOR-RULE
 |FUNCTORIALITY=FAMILY-NON-FUNCTORIAL-AT-2-OF-4-STEPS
                -TAIL-RESTRICTED-FAMILY-FUNCTORIAL
 |ATLAS=THIS-UNITS-DECLARATION-VERDICT-DETERMINING
       (TRANSPORT-CONVENTION-INVARIANT-3-OF-3
       ;CELL-SET-VARIANT-VALUES-MOVE-TO-5/3-AND-4/7
       ;NON-BLOCK-LOCAL-VARIANT-STABILISES-0-OF-5
        -HEAD-FLIPS-TO-NO-CONTINUUM-LIMIT
       ;CELL-STRUCTURE-VARIANT-BOTH-DENSITIES-UNDEFINED-AT-A-MEMBER)
 |R2-GATEWAY=NONE-EARNED:PHI<1-FORCED-AT-7-OF-7
            ;COMPONENTWISE-OVERLAP-COMPLETENESS=1-AT-7-OF-7
            ;SUCCESSOR-CRITERION=FIRST-COMPONENT-WITH-AN-INCOMPLETE
                                 -OVERLAP-GRAPH-EMPTY
            ;SUCCESSOR-RECIPE=DECLARE-CELLS-WITH-PARTIALLY
                              -OVERLAPPING-REGULAR-ORBITS>
```

(The string is emitted on one line; it is broken here for the page. The
emitted form is the receipt's `verdict` field.)

Every segment is computed from the measured tables and every one can fail.
The head is `STABILIZES` exactly when the measured set of constant invariants
is non-empty and `NO-CONTINUUM-LIMIT` exactly when it is empty; among the
`STABILIZES` heads it names the mechanism exactly when the copying census is
measured to hold. $\varphi$'s divergence carries its measured closed law
$\varphi = (\text{block size} - 1)/(\text{label count})$, verified at $7$ of
$7$ members and probes, rather than the bare word "decreasing".

The family is built to its declared target of five with **no cap**; the cap
state is derived from built length against target, so a truncation would
appear in the window qualifier rather than silently.

## 10. The atlas is a named verdict coordinate

The atlas is this unit's own declaration, and its dependence is therefore
measured in-unit rather than disclosed in prose. Six alternative declared
atlases, each stated in the declaration block before it is built, each using
this unit's own drawn rule, $2$-cell rule and five invariant definitions
verbatim, are run over the window and read by the **same** derivation:

| atlas | declaration | stabilised | head | values |
|---|---|---|---|---|
| ALT-A | $\mathrm{REAL} := \gamma_k\Sigma_k$ (composition order swapped) | 2 | STABILIZES | $37/27$, $20/37$ |
| ALT-B | block cyclic order reversed | 2 | STABILIZES | $37/27$, $20/37$ |
| ALT-C | block cyclic order in steps of two | 2 | STABILIZES | $37/27$, $20/37$ |
| B1 | drop the REAL cell — cells are $(k,\text{FULL})$ only | 2 | STABILIZES | $\mathbf{5/3}$, $\mathbf{4/7}$ |
| ATLAS-C | **not block-local**: one further index carrying the increasing-index cycle on the *whole* moved-label set | **0** | **NO-CONTINUUM-LIMIT** | — |
| ALT-D | one cell per block, carrying the group *generated* by both transports | 2 | — | both densities **undefined** |

Four outcomes are measured, and all four matter.

- The two values survive **three** re-declarations of the transport
  convention. That is a genuine robustness result and it is claimed as one.
- Dropping the realised cell keeps both stabilisations — as Theorem B
  predicts — and **moves both values**, to $5/3$ and $4/7$.
- **ATLAS-C flips the head.** It uses *less* arena data than this unit's own
  atlas (no block partition), and over the same five arenas with the same
  five registered invariants it stabilises nothing: $b_0(N) = 2$ at every
  member so the copying hypothesis fails outright, $\varphi$ becomes
  strictly *increasing* ($41/43$, $24/25$, $55/57$), and both densities move
  ($11702/1023$, $2669/195$, $7004/439$; $5390/5851$, $17436/18683$,
  $26395/28016$). Fed to this unit's own derivation it returns
  `R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE`.
- **ALT-D makes the headline invariants ill-defined.** One cell per block
  carrying the generated group of order $21$ on a seven-label block has no
  regular orbit, so by Theorem A the atlas draws nothing: zero $1$-cells,
  zero coherent $2$-cells, and both registered densities undefined at all
  three tail members. This is the declared failure mode
  `UNDEFINED-AT-A-MEMBER` reached by a shipped input, not by a contrived one.

So the two constant densities are invariants of the **atlas declaration**,
not of the arena, and the verdict says so in a computed segment.

## 11. The basepoint, the denominators, and the non-copied hunt

**The basepoint audit.** Delete one structureless label — the arena's
declared basepoint, symmetry-fixed, of degree zero in every complex of every
member, lying in no coordinate cell's support — renormalise the profiles over
the surviving charts and take $\varphi$ over the surviving chart pairs:

| member | charts | $\varphi$ | spectral profile | dimension profile |
|---|---|---|---|---|
| $A_3$ | 42 | $6/41$ | $\{1\!:\!3/7,\,3\!:\!2/7\}$ | $\{6\!:\!1\}$ |
| $A_4$ | 49 | $1/8$ | $\{1\!:\!3/7,\,3\!:\!2/7\}$ | $\{6\!:\!1\}$ |
| $A_5$ | 56 | $6/55$ | $\{1\!:\!3/7,\,3\!:\!2/7\}$ | $\{6\!:\!1\}$ |

**Four of the five** registered invariants are then constant. The registered
$2$-of-$5$ split is therefore between **basepoint-blind and
basepoint-sensitive**, not between substantive and not, and only $\varphi$
still moves — for a different and stronger reason, its denominator being
quadratic in the block count.

**Both denominator conventions.** The pin registers the coherence density
"per drawn chart pair" and the second density "per $2$-cell" without naming
the complex. Both readings are computed and both are printed; the delivered
convention is disclosed as a convention:

| member | coherent | $\lvert E(N)\rvert$ | $\lvert E(G)\rvert$ | $\lvert F(N)\rvert$ | per incidence | per drawn pair | per $N_{\mathrm{coh}}$ 2-cell | per $N$ 2-cell |
|---|---|---|---|---|---|---|---|---|
| $A_1$ | 96 | 40 | 28 | 160 | $12/5$ | $24/7$ | $65/96$ | $13/32$ |
| $A_2$ | 30 | 30 | 30 | 30 | $1$ | $1$ | $2/5$ | $2/5$ |
| $A_3$ | 222 | 162 | 126 | 438 | $\mathbf{37/27}$ | $\mathbf{37/21}$ | $\mathbf{20/37}$ | $\mathbf{20/73}$ |
| $A_4$ | 259 | 189 | 147 | 511 | $37/27$ | $37/21$ | $20/37$ | $20/73$ |
| $A_5$ | 296 | 216 | 168 | 584 | $37/27$ | $37/21$ | $20/37$ | $20/73$ |

The pin-literal readings are $37/21$ and $20/73$; the delivered readings are
$37/27$ and $20/37$. All four stabilise, so the head is safe under every
reading — but the *value* is convention-relative, and the verdict carries
both.

**The non-copied hunt.** Twenty-four intensive quantities, each assigned to
one of three classes in the declaration block *before* any was evaluated,
measured at the five growth members $m = 6, 7, 8, 10, 12$:

| class | count | constant on the tail |
|---|---|---|
| copied (numerator and denominator both block-additive, vanishing on the isolated basepoint) | 10 | **10** |
| basepoint-involving (a chart count enters) | 8 | **0** |
| cross-block (the quantity reads structure between blocks) | 6 | 4 — and each with a vacuity reason declared in advance |

The four constant cross-block quantities are componentwise overlap
completeness ($=1$: every component is a complete graph), the cross-block
$1$-cell density ($\equiv 0$: no $1$-cell crosses a block), $b_0$ of
$N_{\mathrm{coh}}$ over $b_0$ of $N$ ($=1$: the two complexes share a
$1$-skeleton), and the number of component size types ($=2$: which *is* the
copying statement itself). The gate requires constancy to hold exactly where
a vacuity reason was declared and nowhere else.

**Nothing that is neither copied nor vacuous stabilises.** Among the copied
class the constants include two the registry does not name:
$b_2(N)/\lvert F(N)\rvert = 52/73$,
and $b_1(N_{\mathrm{coh}})/\lvert F(N_{\mathrm{coh}})\rvert = 4/37$.
So the registered set is not selective: it is a sample of a class the rule
forces whole.

## 12. What the manifold rung inherits

Not an arena. A criterion and a recipe.

The inherited gateway — "the first member with $\varphi < 1$" — **cannot
fail**, and is therefore not a selection:

> **Theorem C.** The basepoint is symmetry-fixed at every declared member and
> lies in no coordinate cell's support. So it is isolated in the overlap
> graph, at least $n-1$ of the $\binom n2$ chart pairs are undrawn, and
> $\varphi \le (n-2)/n < 1$ always.

Measured at $7$ of $7$ members and probes, with $b_0 = \text{blocks}+1$
confirming the basepoint's isolation at each. Worse for the inherited
reading, $A_1$ *uniquely attains* the forced maximum,
$\varphi = 7/9 = (9-2)/9$: it is the **least** local member the family
contains, its overlap graph being $K_8 \sqcup \{\mathrm{pt}\}$.

And no member supplies a non-trivial overlap pattern at all. Componentwise
overlap completeness is measured $1$ at $7$ of $7$ members and probes:

| member | components | component sizes | completeness | $\varphi$ | forced bound |
|---|---|---|---|---|---|
| $A_1$ | 2 | 1, 8 | 1 | $7/9$ | $7/9$ |
| $A_2$ | 4 | 1, 5 | 1 | $1/4$ | $7/8$ |
| $A_3$ | 7 | 1, 7 | 1 | $6/43$ | $41/43$ |
| $A_4$ | 8 | 1, 7 | 1 | $3/25$ | $24/25$ |
| $A_5$ | 9 | 1, 7 | 1 | $2/19$ | $55/57$ |
| $L_{10}$ | 11 | 1, 7 | 1 | $6/71$ | $69/71$ |
| $L_{12}$ | 13 | 1, 7 | 1 | $6/85$ | $83/85$ |

Every component is a complete graph, so **every $\varphi < 1$ in this unit is
achieved by disconnection**, never by a non-trivial overlap pattern. By
Theorem A that is not an accident of these arenas but a property of the atlas
schema: cells draw complete graphs on regular orbits, so overlap graphs
assembled from them are unions of cliques.

The gateway is therefore handed forward as `R2-GATEWAY=NONE-EARNED`, and what
replaces it is a criterion with teeth and a constructive recipe.

- **Criterion (for the successor's pin):** the first *component* whose
  overlap graph is **incomplete**. Measured across $A_1$–$A_5$ and both
  probes: **empty**. It can return nothing, and here it does.
- **Recipe (proved, Theorem A):** partial orbit overlap must be **declared**.
  With regular-orbit drawing, cliques are all there is; a union of two
  cliques that is not itself a clique is the only way this schema can produce
  an incomplete overlap graph. So the successor starts from **atlas design**,
  not from arena choice — and this copying family remains available to it as
  a null control, a family guaranteed to produce no locality.

The distinction the successor must not lose: what non-trivial structure this
unit *does* see lives in the **coordinate resolution** — edges per cell,
rules per edge — and not in the overlap pattern.

## 13. Controls

**Positive.** A family constant by construction returns the `STABILIZES` head
naming all five registered invariants. The control runs the same instrument
end to end — same atlas, same five measurements, same window.

**Negative.** The excluded raw estimators, read along the same three grown
members:

| raw estimator | $A_3$ | $A_4$ | $A_5$ |
|---|---|---|---|
| overlap edges | 126 | 147 | 168 |
| coherent $2$-cells | 222 | 259 | 296 |
| eigenvalue-$1$ multiplicity | 19 | 22 | 25 |
| charts | 43 | 50 | 57 |
| $b_2(N_{\mathrm{coh}})$ | 120 | 140 | 160 |

Every one moves; zero stabilise; the instrument returns
`R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE`.

**Scramble.** At $A_3$ the drawn relation is preserved and the drawn maps are
deterministically permuted inside each coordinate cell by an exact integer
shift seeded from the declared control block alone. The measured moved set is
$\{N_{\mathrm{coh}}\text{ density},\ b_2\text{ density}\}$;
the measured fixed set is
$\{\varphi,\ \text{dimension profile},\ \text{spectral profile}\}$
— exactly the pin's declared split. The destruction it does is
built from the measurement rather than typed beside it, and the coherent
$2$-cell count is required to have fallen, so a scramble that left the
identification data intact could not pass.

**Discrimination.** The widening family — one block that grows rather than
being copied, with the block reversal as its symmetry — at sizes $5, 6, 7$:

| invariant | $W_5$ | $W_6$ | $W_7$ |
|---|---|---|---|
| $N_{\mathrm{coh}}$ density | $5/6$ | $20/17$ | $35/24$ |
| $b_2$ density | $2/5$ | $1/2$ | $4/7$ |

Both densities move. **Mixed-block** (§8.3) moves them too, and is the
control that separates additive from additive-with-isomorphic-blocks.

**Index sweep.** The rule also carries a prime-indexed selection; the members
it picks at the next two declared primes, $L_{10}$ at 71 labels and $L_{12}$
at 85 labels, both return $37/27$ and $20/37$, so the values are not an
artefact of which index the family walks. Their $\varphi$ continues to fall,
$6/71$ and $6/85$.

## 14. Scope and non-claims

**The continuum question itself is untouched.** This unit does not show that
the v13 substrate has a continuum limit, and it does not show that it lacks
one. It shows that *this* declared family cannot answer the question, for a
reason that is proved rather than suspected — and it states what a family
that could answer it must do.

- The two constant values are not a limit and not a convergence. They are one
  block's census, restated at every member by an operation that provably
  cannot change it. A refinement family that answers the continuum question
  must **divide** a block, not copy one; the quantity that would test it —
  new structure per new chart — is the constant $27/7$ here, read straight
  off the printed closed forms $\lvert E\rvert = 27m$ and $n = 7m+1$, which
  is the signature of an extensive sequence rather than of refinement.
- The values are invariants of the **atlas declaration**, measured (§10). Any
  successor that reuses them must carry the atlas as a coordinate.
- Everything here is measured at the five declared arenas, their declared
  atlas, and the declared window $K = 3$. Nothing is claimed about arenas
  outside that list or about a limit of the family in any topology.
- The stabilisation window lies entirely on the homogeneous tail, and $A_1$
  is not a member of the growth rule's family. The verdict carries both the
  full-family and the tail-restricted readings.
- $b_1$ and the raw dimension estimator are excluded **by declaration** and
  are used in no verdict. The $b_1$ exclusion is not a measured triviality:
  its density on $N_{\mathrm{coh}}$ stabilises at $4/37$ (§5).
- The spectral chain is a strictly weaker statement about a **different
  operator** than the inherited wall (§5); the wall is cited, never
  re-derived, and does not ride along.
- Coherence is analytically forced at $A_2$ and contingent at the other four
  members; the forcing is disclosed with its measured cause.
- No locality is handed forward. `R2-GATEWAY = NONE-EARNED`.

**Opens.** Whether any refinement rule over this substrate divides a block
rather than copying one, and what the five invariants do under it. Whether an
arena morphism criterion weaker than equivariant block embedding makes the
nine- and sixteen-label arenas steps of one family. Whether an atlas whose
cells have *partially* overlapping regular orbits — the recipe of §12 —
exists over this substrate, and what its overlap topology is.

## 15. The receipt

`v14/code/r1_continuum_receipt.json`, written by the plain delivery run,
which is byte-identical across runs.

| | |
|---|---|
| anchors | 62, all exit-1, 0 failures |
| gates | 42, all must-pass, 0 failures |
| disclosures | 7 |
| mutants | 59 declared, 59 died, 0 survivors |
| gate falsification | 41 of 41 must-pass gates falsified by some mutant; none never-falsified (the falsification gate itself is excluded from its own denominator) |
| measured data evaluated | 381, gated zero at the declaration freeze |
| arithmetic | exact `int` and `fractions.Fraction`; the file's own syntax tree is walked and measured to contain no float literal, no arithmetic division and no floating-point call |
| exemptions | no gate predicate references mutant identity; every occurrence sits inside a declared mutable instrument |

The verdict gate rebuilds the complete emitted string segment by segment from
the receipt-facing tables and compares for **equality**; the trajectory table
the gates check is the same object the receipt serialises and this paper
renders from. The falsification self-test corrupts one pinned external anchor
and confirms the run exits 1 naming that anchor; it writes no artifacts. The
delivered artifacts are the plain run's.
