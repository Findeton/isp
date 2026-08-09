# R1 — The continuum rung

**Status:** GREEN-UNREVIEWED (v14 ledger #2 pin; delivered against
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

Two of the five are exactly constant on the declared three-member window and
three are not. The verdict, derived inside a gate from the measured table, is

> `R1-STABILIZES-AT-<NCOH_DENSITY=37/27;B2_DENSITY=20/37|DIVERGENT=PHI:STRICTLY-DECREASING;SPECTRAL_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING;DIMENSION_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING|WINDOW=K=3-OF-5-MEMBERS-NO-CAP|FUNCTORIALITY=FAMILY-NON-FUNCTORIAL-AT-2-OF-4-STEPS|R2-GATEWAY=A1>`

The mechanism behind the constancy is measured, not inferred: at every grown
member $b_0$ of the nerve equals the block count plus one, so the declared
growth rule refines by **disjoint addition** — it copies a block rather than
dividing one — and exactly the per-cell densities survive that operation
while every label-normalised quantity is diluted by the single basepoint. A
growth rule that widens a block instead of copying it is run through the same
instrument and moves both densities, so the constancy is a property of the
declared rule and not of the definitions.

Two further measured facts stand on their own. The family is **not
functorial**: no admissible arena morphism exists at two of its four steps,
and both obstructions are named from measured orbit and block data. And the
overlap-completeness fraction is strictly below 1 at **every** member, so
locality exists at this substrate and the manifold rung inherits its arena.

---

## 1. The question

> Does a declared refinement family over the v13 substrate admit a
> pre-registered **intensive** invariant that stabilizes under refinement?

Both answers are first-class. The instrument can emit
`R1-STABILIZES-AT-<...>` and `R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE-<...>`,
the head is derived from the measured count of stabilised invariants inside a
gate, and both heads are exhibited on real measurements by the positive and
negative controls of §10.

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

Nothing of the predecessor is imported as code. Every number this unit reuses
is read from those bytes and recomputed here, and 60 anchors carry the
comparison exit-1.

**A companion-hash finding.** The founding pin also names companion artifacts
in parentheses. Six of the eight reproduce. The two that do not are the two
**papers**:

| companion | recorded | measured |
|---|---|---|
| `v13/paper-rsq-reposed-square.md` | `07bea42728a2` | `f80317a25037` |
| `v13/paper-top-topology.md` | `4e4cd4f11bab` | `379194959fbc` |

What the instrument measures is exactly the two columns above and the set on
which they differ. The provenance, read separately from the repository's
history, is that the two recorded values are each the paper's hash at its
**repair** commit — `c45e80f` and `efc1bed` — and that each paper was edited
once more afterwards, at its terminal commit `cb18c24` and `cd98f05`. The two
companion entries are therefore **stale by one commit**, not invented: they
pin the pre-terminal version of each paper.

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
  satisfies $\pi(a) = b$; the drawn map is that $\pi$. Uniqueness is the
  admission rule, so a cell whose transport identifies a pair ambiguously
  draws nothing there.
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
key and no intermediate with it.

**The realised rule draws nothing at $A_2$** — measured, not assumed: there
the realised transport has order $10$ on a seven-label symmetry saturation, so
no ordered pair has a unique power carrying one label to the other. At that
member alone every $2$-cell therefore draws its three maps from one cyclic
group acting regularly on its block, coherence is analytically forced, and
$N$ coincides with $N_{\mathrm{coh}}$. At the other four members two distinct
transport groups meet at a common block and coherence is contingent: 96 of
160 at $A_1$, and 222 of 438, 259 of 511, 296 of 584 at the grown members.
This is a disclosure, not a gate.

### 4.1 The machinery is calibrated against the pinned topology base

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

together with the coordinate count $(T-1)(V-1) = 4\cdot 35 = 140$. Nothing of
that atlas is rebuilt here; this is the machinery's external calibration.

## 5. The registered invariants

Five, fixed in the pin before any was computed.

1. **$\varphi$, the overlap-completeness fraction** — drawn chart pairs over
   all chart pairs. Also the manifold rung's gateway: any member with
   $\varphi < 1$ unlocks it.
2. **$N_{\mathrm{coh}}$ density** — coherent $2$-cells per drawn chart pair,
   $\lvert F(N_{\mathrm{coh}})\rvert / \lvert E(N)\rvert$.
3. **The normalised spectral profile of $I - E$** — over the arena's readouts
   $E = \rho_L(\pi)$, $\pi \in \langle\Sigma\rangle\setminus\{1\}$, the map
   $d \mapsto \mathrm{mult}(\Phi_d)/\dim$.
4. **The per-volume dimension profile** — the link-dimension distribution
   normalised by chart count: the number of charts whose link has exactly
   $v$ vertices, divided by the chart count, as a function of $v$.
5. **$b_2$ density** — $b_2$ of $N_{\mathrm{coh}}$ over $\mathbb F_2$, per
   $2$-cell of $N_{\mathrm{coh}}$.

Two quantities are **excluded** by the pin and are not candidates: the raw
local-dimension estimator, provably extensive; and $b_1$, which carries no
identification content. $b_1$ is printed once as a disclosure: on $N$ it is
**zero at every member** — the trivial first homology the topology base
reports, reproduced at this substrate — while on $N_{\mathrm{coh}}$ it is
$2, 0, 24, 28, 32$: coherence costs cycles here exactly as it does there.

Each invariant is computed by two routes or against an independent
comparator: $\varphi$ from the edge list and from an accumulation that never
forms one; the coherent count once flagged during construction and once
re-composed from the edge table alone; the eigenvalue-$1$ multiplicity once
as the readout's cycle count and once as the exact rational kernel dimension
of $I - E$ by elimination over $\mathbb Q$; the link-vertex count from the
edge list and from a second pass over the per-cell tables; $b_2$ against a
comparator formed from $N_{\mathrm{coh}}$'s own $b_2$ and $2$-cell count
without passing through the complex selector. Components and cycle rank are
computed by two genuinely independent routes at every complex of every
member, and $\operatorname{rank}\partial_2$ under two pivot disciplines whose
pivot **sets** are measured to differ on a declared probe.

**The spectral wall rides along.** The inherited result guarantees that the
readout carries the eigenvalue $1$, so $0 \in \mathrm{spec}(I-E)$. That is
confirmed as an anchor at every readout of every member and never
re-censused; the anchor predicate is calibrated the other way inside the same
gate, returning false at multiplicity zero.

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
criterion is measured to admit some steps and refuse others, so it is not a
constant function. The computed qualifier is
`FAMILY-NON-FUNCTORIAL-AT-2-OF-4-STEPS`.

This is a real structural statement about the corpus's own measured line: the
nine- and sixteen-label arenas and the grown arena are not steps of one
refinement. The stabilisation window falls on the three members that **are**
connected by constructed morphisms.

## 7. The trajectory

All five invariants at all five members, exact:

| invariant | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
|---|---|---|---|---|---|
| $\varphi$ | $7/9$ | $1/4$ | $6/43$ | $3/25$ | $2/19$ |
| $N_{\mathrm{coh}}$ density | $12/5$ | $1$ | $\mathbf{37/27}$ | $\mathbf{37/27}$ | $\mathbf{37/27}$ |
| spectral profile | $\{1\!:\!\tfrac23,\,2\!:\!\tfrac13\}$ | $\{1\!:\!\tfrac58,\,2\!:\!\tfrac38\}$ | $\{1\!:\!\tfrac{19}{43},\,3\!:\!\tfrac{12}{43}\}$ | $\{1\!:\!\tfrac{11}{25},\,3\!:\!\tfrac{7}{25}\}$ | $\{1\!:\!\tfrac{25}{57},\,3\!:\!\tfrac{16}{57}\}$ |
| dimension profile | $\{0\!:\!\tfrac19,\,7\!:\!\tfrac89\}$ | $\{0\!:\!\tfrac1{16},\,4\!:\!\tfrac{15}{16}\}$ | $\{0\!:\!\tfrac1{43},\,6\!:\!\tfrac{42}{43}\}$ | $\{0\!:\!\tfrac1{50},\,6\!:\!\tfrac{49}{50}\}$ | $\{0\!:\!\tfrac1{57},\,6\!:\!\tfrac{56}{57}\}$ |
| $b_2$ density | $65/96$ | $2/5$ | $\mathbf{20/37}$ | $\mathbf{20/37}$ | $\mathbf{20/37}$ |

Twenty-five cells written against a forced product of twenty-five. The
supporting Betti data:

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

## 8. The verdict

Derived inside a gate from the table above: the head is `STABILIZES` exactly
when the measured set of constant invariants is non-empty and
`NO-CONTINUUM-LIMIT` exactly when it is empty; the stabilised values, each
divergent invariant's measured failure mode, the window with the family
length and cap state, the functoriality qualifier and the gateway are each
read out of the measurement, and each is required to appear verbatim in the
emitted string.

```
R1-STABILIZES-AT-<
  NCOH_DENSITY=37/27;B2_DENSITY=20/37
 |DIVERGENT=PHI:STRICTLY-DECREASING
          ;SPECTRAL_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING
          ;DIMENSION_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING
 |WINDOW=K=3-OF-5-MEMBERS-NO-CAP
 |FUNCTORIALITY=FAMILY-NON-FUNCTORIAL-AT-2-OF-4-STEPS
 |R2-GATEWAY=A1>
```

Two of five stabilise, and they are exactly the two the pin identifies as
carrying the identification data. Three do not, and each failure mode is
computed rather than described: $\varphi$ is strictly decreasing; the
spectral and dimension profiles keep a constant support while their weights
move.

The family is built to its declared target of five with **no cap**; the cap
state is derived from the comparison of built length against target, so a
truncation would appear in the window qualifier rather than silently.

## 9. Why the two stabilise, measured

The constancy is located, not merely observed.

At every member $b_0$ of the nerve equals the block count plus one, the
basepoint: $2, 4, 7, 8, 9$ against blocks $1, 3, 6, 7, 8$. The complex is a
disjoint sum of one copy per block together with an isolated basepoint. And
across the three grown members the per-block counts are measured **equal**:
27 one-cells and 37 coherent two-cells per block at $A_3$, $A_4$ and $A_5$
alike.

So the declared growth rule refines by **disjoint addition** — it adds a
block rather than dividing one. Under that operation a ratio of two per-cell
counts is invariant and a ratio normalised by label count is not, because the
single basepoint's share $1/n$ moves. That is exactly the split the table
shows: the two densities are per-cell and stabilise; $\varphi$, the dimension
profile and the spectral profile are per-label and drift.

The reading is that this substrate's own growth rule is not a refinement in
the geometric sense. It produces a direct sum, not a subdivision. What
stabilises under it stabilises for that reason, and the honest scope of the
stabilisation claim is the additive rule the corpus declares.

Three further measurements keep that reading from being a story.

- The same two values reproduce at the members the rule's **prime-indexed**
  selection picks instead — $L_{10}$ at 71 labels and $L_{12}$ at 85 labels
  both return $37/27$ and $20/37$ — so the stabilisation is not an artefact
  of which index the family walks. Their $\varphi$ continues to fall,
  $6/71$ and $6/85$.
- A growth rule that widens a block instead of copying it **moves** both
  densities (§10).
- Destroying the identification data while preserving the drawn relation
  moves exactly those two and fixes the other three (§10).

## 10. Controls

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
`R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE`. Both heads are therefore reachable
by the same derivation, on real measurements.

**Scramble.** At $A_3$ the drawn relation is preserved and the drawn maps are
deterministically permuted inside each coordinate cell by an exact integer
shift seeded from the declared control block alone. 240 drawn maps change.
The measured moved set is the coherence density and the $b_2$ density; the
measured fixed set is $\varphi$, the dimension profile and the spectral
profile — exactly the pin's declared split. The
scramble is maximally destructive at this substrate: the coherent $2$-cell
count falls to zero, so the density moves to $0$ and the $b_2$ density
becomes **undefined**, its denominator having vanished. That is recorded as
measured rather than rounded into a number.

**Discrimination.** The widening family — one block that grows rather than
being copied, with the block reversal as its symmetry — run through the same
instrument at sizes $5, 6, 7$:

| invariant | $W_5$ | $W_6$ | $W_7$ |
|---|---|---|---|
| $N_{\mathrm{coh}}$ density | $5/6$ | $20/17$ | $35/24$ |
| $b_2$ density | $2/5$ | $1/2$ | $4/7$ |

Both densities move. The constancy of §7 is therefore a property of the
declared family's additive rule, not of the definitions.

## 11. The manifold rung's arena

$\varphi < 1$ at **every** member — $7/9,\ 1/4,\ 6/43,\ 3/25,\ 2/19$. The
overlap graph is never complete at this substrate, so the simplicial nerve is
never a cone and locality exists. The first such member is computed and handed
forward:

> **The manifold rung's gateway arena is $A_1$, the nine-label arena, at
> $\varphi = 7/9$.**

The gateway is derived from the trajectory table, not named; the criterion is
measured non-vacuous, since $\varphi$'s declared range admits $1$ and the
measured values are strictly below it.

## 12. Scope and non-claims

- Everything here is measured at the five declared arenas, their declared
  atlas, and the declared window $K = 3$. Nothing is claimed about arenas
  outside that list or about a limit of the family in any topology.
- **No continuum is claimed.** Two intensive invariants are exactly constant
  on three consecutive members of one declared family, and the measured
  reason is that family's additive rule. That is a statement about the rule.
- The stabilisation is measured only across steps joined by constructed
  morphisms; the two steps with no admissible morphism are reported as such
  and the whole family is carried with the non-functoriality qualifier.
- $b_1$ and the raw dimension estimator are excluded candidates and are not
  used in any verdict.
- Coherence is analytically forced at $A_2$ and contingent at the other four
  members; the forcing is disclosed with its measured cause.
- The atlas construction is this unit's own declaration. It is arena-
  determined and self-tested under relabelling, but a different declared
  atlas over the same arenas is a different measurement.

**Opens.** Whether any refinement rule over this substrate divides a block
rather than copying one, and what the five invariants do under it. Whether an
arena morphism criterion weaker than equivariant block embedding makes the
nine- and sixteen-label arenas steps of one family. Whether the two constant
densities are invariants of the arena or of the atlas declaration.

## 13. The receipt

`v14/code/r1_continuum_receipt.json`, written by the plain delivery run,
which is byte-identical across runs.

| | |
|---|---|
| anchors | 60, all exit-1, 0 failures |
| gates | 33, all must-pass, 0 failures |
| disclosures | 4 |
| mutants | 47 declared, 47 died, 0 survivors |
| gate falsification | 32 of 32 must-pass gates falsified by some mutant; none never-falsified (the falsification gate itself is excluded from its own denominator) |
| measured data evaluated | 177, gated zero at the declaration freeze |
| arithmetic | exact `int` and `fractions.Fraction`; the file's own syntax tree is walked and measured to contain no float literal, no arithmetic division and no floating-point call |
| exemptions | no gate predicate references mutant identity; every occurrence sits inside a declared mutable instrument |

The falsification self-test corrupts one pinned external anchor and confirms
the run exits 1 naming that anchor; it writes no artifacts. The delivered
artifacts are the plain run's.
