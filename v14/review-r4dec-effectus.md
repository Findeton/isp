# EFFECTUS-LENS HOSTILE REVIEW — paper-21 (the R = 4 arena)

**Seat:** K2 EFFECTUS. **Protocol:** v14 ledger #203, row K2.
**Object at `f45b3a1`:** `v14/paper-21-r4dec.md` `f54dad8d51b8` ·
`v14/code/r4dec_exact.py` `e387674bfcdd` ·
`v14/code/r4dec_output.txt` `27ed73ded234` ·
`v14/code/r4dec_receipt.json` `e1f148dd6a0e`; pin
`v14/note-r4dec-pin.md` `f50630ced3be` (at `d55571d`).
**Hashes verified at open and at close: 5 of 5 identical, both times.**

**GRADE: ACCEPT-WITH-FIXES.**

**Recomputations: 87** (77 independent computations from the declared
conventions with no import of the unit's code, plus 10 arithmetic
cross-checks). **False computed numbers found: 0.** Every number this
seat re-derived — the census, the fibers, the price row, the code
space, the back-validation, the window arithmetic — reproduces
exactly. **False or unscoped prose claims found: 2 MAJOR, 5 MINOR**,
all with exact liftable repairs, none moving a verdict.

The two MAJORs are both *scope elisions in quotable sentences*, and
both are elisions the paper's own body already contains the correction
for. One of them (M-2) changes the successor programme: **the
law-over-records door opens at R = 6, not at R = 8, and it opens there
with zero free items.** That is this seat's principal finding.

---

## 0. What was verified, and how

This seat re-implemented the arena from the *declared* conventions
only — sites $\mathbb{Z}_3^2$; the four direction classes; I7's three
declared links; the cell $(x,\ell)$ carrying 1 exactly when $x$ and
$x+\ell$ share a conflict group — and never imported, executed or
read-for-copying the unit's builder. Scratch at
`.../scratchpad/r4d-ef/`. Repo access read-only; one repo write (this
file).

The independent implementation reproduced, exactly:

| object | paper | this seat |
|---|---|---|
| partitions of the nine sites (enumeration / closed form) | 280 / 280 | **280 / 280** |
| incidence spectrum over the 280 | 1@0, 27@4, 54@6, 162@7, 36@9 | **identical** |
| max link incidences per round | 9 | **9** |
| saturating partitions | 36 | **36** |
| $36^4$ / $280^4$ / $280^3$ / $280^2$ | 1,679,616 / 6,146,560,000 / 21,952,000 / 78,400 | **identical** |
| schedules per round / the R = 4 family | 7,560 / 3,266,533,992,960,000 | **identical** |
| G-FLAT-inducing quadruples | 276 | **276** |
| grouping multisets / orbit sizes | 12; 12×1, 24×11 | **identical** |
| collinear multisets | 1 (ROW+COL+DIA×2) | **1, same directions** |
| $\lvert\mathrm{Aut}\rvert$ of the realised relation | 1296 | **1296** |
| I-SITE-ASSIGNMENT / I-DIRECTION-LABEL fibers at G-FLAT | 36 / 3 | **36 / 3** |
| the 36 count fields, homogeneous among them | 36, 3 | **36, 3** |
| fibers at the driven R = 3 record | 1 / 1 | **1 / 1** |
| covering quadruples (exhaustive over 6,146,560,000) | 100,080 | **100,080** |
| posdef-site distribution inside it | 9 at all 100,080 | **{9: 100,080}** |
| determinant spectrum over 900,720 cells | 3/4@437,184; 1@386,640; 7/4@76,896 | **identical** |
| homogeneous / inhomogeneous | 20,988 / 79,092 | **20,988 / 79,092** |
| homogeneous records | (1,1,1)@20,160; (1,1,2)@276; (1,2,1)@276; (2,1,1)@276 | **identical** |
| reachable site codes at R = 3 / R = 4 | 54 / 105 | **54 / 105** |
| identity-breaking codes at R = 4 | 3: (1,1,4), (1,4,1), (4,1,1), all det 0 | **identical** |
| their occurrences inside the covering class | 0 | **0, 0, 0** |
| back-validation R = 3 / R = 2 | 72 in 12 multisets / ceiling 3 at 252, 747 non-degenerate | **identical** |
| the two controls | ROW/COL/DIA/ANT: field ≡ 1, 27 incidences, **9 foreign pairs**; collinear: (1,1,2) at every site, 36 incidences, 0 foreign | **identical** |
| the resolvable table | 35 multisets, 4 admissible, 1 in a declared chart orbit | **identical** |
| window arithmetic | 256+264+80 = 600; 520 groupings; 276+80 = 356 driven | **identical** |
| record-length spectrum | sums to 600 | **600** |

**Zero discrepancies.** The unit's numbers are, on this seat's
evidence, correct without exception.

Two facts this seat measured that the paper does **not** report, both
load-bearing below:

- **the covering class's maximum cell count is 2** — never 3, never 4
  (20,160 quadruples max out at 1, the other 79,920 at 2), so the
  whole covering class occupies **7 site codes**, all inside
  $\{1,2\}^3$. This is the *mechanism* for S-4's "empty cell with
  teeth", which the paper registers as unexplained;
- **over the covered code box $[1,4]^3$ the determinant is
  non-negative at all 64 codes**, zero at exactly the 3 named ones.
  Negative determinant first becomes code-reachable at **R = 5**, at
  (1,1,5) and its two relabellings.

---

## 1. Row 1 — the stratified head's two verbs

**Question posed:** are `FOUND-AT-THE-FORCED-CARRIER` and
`UNMOTIVATED-AT-THE-FREE-ASSIGNMENT` both earned, given that the
intended in-arena FOUND control (R4-ONE-ANT) died STRUCT-DEAD and the
FOUND value was exhibited on the driven **R = 3** record instead —
does that substitution preserve the two-way license?

**Verdict: BOTH VERBS EARNED. The substitution preserves the license,
and it preserves it for a stronger reason than the paper gives.**

*The FOUND verb.* `FOUND-AT-THE-FORCED-CARRIER` is an in-arena
positive measurement with in-arena negative controls in abundance: at
the forced carrier the structural test passes at 1296 = 1296 at both
readings and the induced field is I7's G-FLAT row at 27 of 27 cells,
while d66's own committed R = 4 point returns COUNT-DEAD, the
field-identically-1 quadruple returns STRUCT-DEAD, the declared
falsifier returns STRUCT-DEAD/COUNT-DEAD and the arity probe returns
ARITY-DEAD. Four of the detector's five values are exhibited *inside*
the declared R = 4 arena. The verb is not at risk.

*The UNMOTIVATED verb.* This is where the substitution bites, and the
question is exact: the value UNMOTIVATED is meaningful only if its
opposite (zero free items) could have been returned. It could not have
been — **not anywhere in the R = 4 arena, by this paper's own two
theorems**:

- zero free items ⟺ the count field is link-constant (§4.5, carried by
  edge-transitivity of $K_{3,3,3}$ — verified here: fiber 1 at
  (1,1,1), (2,2,2), (3,3,3); fiber 36 at (1,1,2), (2,2,4), (1,1,4);
  fiber 72 at (1,2,3));
- a link-constant field at R = 4 costs 27 incidences, while a
  STRUCT-alive arena deposits 36 — so **the two conditions are
  simultaneously unsatisfiable at R = 4**.

This seat confirms the second leg with teeth: the 20,160 covering
quadruples inducing (1,1,1) *do* exist at R = 4, they *are*
link-constant, and every one of them carries exactly $36-27 = 9$
foreign pairs — hence every one is STRUCT-DEAD, exactly like the
R4-ONE-ANT control. The paper's intended control did not die of bad
luck. **It died of a theorem, and so would every possible in-arena
substitute.**

Therefore:

1. The two-way license is preserved, but it is preserved on **RUNBOOK
   §15 terms, not on HA §14's literal terms.** §15 makes the arena's
   coordinates data; choice-inventory item 1 declares the base object
   as `CONFLICT-GRID(3, R)` with *R a coordinate*, and item 6 declares
   `R = 4 rather than R = 3` **VERDICT-DETERMINING with the
   counterfactual measured in-unit**. The FOUND control at R = 3 is
   therefore a control taken at the declared counterfactual of a
   declared arena coordinate — which is precisely what §15 asks for,
   and is a *stronger* discipline than an in-arena control of
   convenience.
2. §4.7 quotes HA §14 requirement 3 ("*a predicate that cannot return
   its other value anywhere in the declared arena is not a
   measurement*") and then satisfies it at a different value of R.
   Read literally, the requirement is **not** met, and the honest
   statement is better than the literal one: the predicate *provably*
   cannot return its other value in this arena, and the instrument is
   shown live on the arena's declared counterfactual.
3. The residual risk the substitution leaves is narrow and worth
   naming: a fault that fires only at four rounds (e.g. in the
   four-round field summation) would not be caught by an R = 3 FOUND.
   It is covered elsewhere — the 600/600 driven-vs-combinatorial
   equality, the two independent census routes, and the fiber
   computation being the same code path at both budgets — so the risk
   is closed, but by other gates, not by this control.

**Repair (MINOR-2, §11).** Stamp the control row with its coordinate
and add the impossibility as a *result*: this converts an apparent
shortfall into the paper's third theorem.

---

## 2. Row 2 — the two theorems, their scope, and the corpus-facing row

**The two theorems.**

- **T1 (zero-free ⟺ link-constant).** Correct, and correctly stated.
  Verified independently: the realised relation is $K_{3,3,3}$
  (9 vertices, 27 edges, $\lvert\mathrm{Aut}\rvert = 1296$),
  edge-transitive; a count field with site-assignment fiber 1 is
  invariant under all 1296 automorphisms and therefore constant on all
  27 edges, and conversely. The fiber value 36 at G-FLAT is forced,
  not incidental: it is the number of decompositions of $K_{3,3,3}$
  into three disjoint transversal triangles ($3!\times 3! = 36$),
  $1296/36 = 36$ — and exactly 3 of those 36 are expressible as
  homogeneous I7 records, which is the paper's "3 homogeneous, exactly
  1 declared". Every step reproduces.
- **T2 (link-constancy impossible at R = 4).** Correct **only under
  the cleanliness scope** that §4.3's preceding sentence establishes
  ("a clean R = 4 arena therefore spreads 36 incidences over 27
  cells"). The blockquote that carries it drops the scope, and §9
  drops it again. See **M-1**.

**Scope-check of the licensed sentence "the R = 3 perfection was the
special case".** As written, this is *under*-stated and mildly
misleading: it suggests R = 3 was a one-off. It was not. The correct
statement is a **periodicity**, and it follows from the paper's own
two theorems plus one arithmetic step this seat verified:

> A homogeneous record $(n_1,n_2,n_3)$ is reachable by a STRUCT-alive
> (foreign-pair-free, hence fully saturating) schedule at exactly one
> budget: $R = n_1+n_2+n_3$. Zero free items requires
> $n_1=n_2=n_3=m$, hence $R = 3m$. **A weld at this carrier can be
> both structurally alive and motivated exactly at the budgets
> $R \equiv 0 \pmod 3$, and then its record is $(m,m,m)$ — which I7
> never declares.**

Verified: the budget law $R = \sum n_i$ holds on all nine declared
homogeneous records — G-FLAT (1,1,2) at R = 4 ✓ (the paper's own 36 =
4×9), G-DIAG2 (2,2,4) at R = 8 ✓ (the paper's own 72), G-SINGULAR
(1,1,4) at R = 6, G-INDEF (1,1,6) at R = 8, G-ANISO at 10, G-OFFDIAG
at 10, G-OFFNEG at 12, G-OFFDIAG2 at 20, G-ANISO2 at 26. And **no
declared record is link-constant (0 of 9), while the declared box holds
six link-constant admissible points (1,1,1)…(6,6,6)** — both
reproduced.

**Does this DEMOTE weld-3's achievement or EXPLAIN it? It EXPLAINS
it, and it promotes it.** The corpus-facing row:

> **The R = 3 weld's zero free items was not luck and not a
> one-budget accident: R = 3 is the first member of the arithmetic
> family $R = 3m$ at which a live weld is motivated at all, and the
> record it must land on there is $(m,m,m)$. Paper-19 did not get for
> free what paper-21 must pay for; it stood at the first rung of the
> only ladder on which the RSQ standard can ever be met at this
> carrier. What paper-21 adds is that the ladder and I7's declared
> list are **disjoint at every budget** — because no declared record
> is link-constant — so "a declared record" and "a free map" are not
> two things that happened to conflict at R = 4. They are two things
> that conflict everywhere, and R = 4 is simply the first budget at
> which the corpus could see it.**

That is strictly stronger than "the R = 3 perfection was the special
case", it is entailed by the paper's own theorems, and it is the
sentence STATUS and memory should carry.

**Constructive check of the periodicity (used again in §3 and §11).**
At R = 6 the link-constant record (2,2,2) is reachable by concatenating
any two of paper-19's own 72 I7-STRICT triples: field ≡ 2 at all 27
cells (verified), all six rounds saturating (hence 0 foreign pairs,
STRUCT-alive), $\ge 72^2 = 5{,}184$ ordered witnesses before
interleaving. (2,2,2) is admissible ($\det = 3$), link-constant (site
fiber 1, label fiber 1 — verified), and **undeclared** — the same
status weld-2's own FOUND witness had (#168). The trade is periodic
and it is constructive.

---

## 3. Row 3 — THE SPLIT'S MEANING: what the law-over-records door
actually opens

**What is licensed.** Exactly this, and no more:

> **On 9 of the R = 4 welded record's 27 intervals — the diagonal
> ones, the link this budget populates twice — the split fiber is 1
> rather than 0, and paper-06's per-interval invariant-split law is
> non-empty there and unique (fiber 1, one orbit, simplex dimension
> $0 = n-2$, pinned-transitive). This is the first welded record in
> the line with a positive split fiber anywhere.**

**What is NOT licensed, and the paper is at the edge of it.**

1. **"The first law over records."** *Overclaim, on two independent
   counts.*
   - The law is **per-interval**, not per-record. At the record level
     all three terminal laws remain empty: paper-04's raw product is 0
     (18 of the 27 intervals still carry count 1), CR-B's own lattice
     predicate still marks G-FLAT unsplittable, paper-09's kernel is
     empty at every one of the 27. "A law over records" is precisely
     what has *not* been reached, and the paper's own §1 is right to
     say *the door*, not the room.
   - **The one non-empty law is inert.** This is the sharper point,
     and the paper contains both halves without ever conjoining them.
     The only corpus move that could consume a per-interval law is
     R6a's `SINGLE-INTERVAL` class — and it is **REFUSED** on arena
     shape (verified in paper-04: direction-0 cycle lengths become
     [4,3,3], 10 sites not divisible by the longest cycle 4, and only
     1 of the 3 declared link displacements has a target at the new
     site). The only other move, DYADIC, needs the product, which is
     0. **So at R = 4 no admissible refinement move exists on this
     record at all, and the law that becomes non-empty has nothing to
     act on.** That belongs in §5.2 in one sentence (MINOR-1).
2. **Any dynamics of refinement.** None ran. The law is a
   measure-theoretic object on a 1-point fiber; its "uniqueness" is
   the uniqueness of a point mass on a singleton. The paper says this
   ("non-empty at its degenerate end") — successors must not drop it.

**The licensed phrase**, for STATUS, memory and every successor:

> **"The first welded record on which any refinement law is non-empty
> anywhere — non-empty on 9 of 27 intervals, unique because its fiber
> is a single point, and inert because both of the corpus's refinement
> moves are unavailable on it."**

### 3.1 — THE LOR UNIT: register rows

**The object.** *Not* paper-06's law on the R = 4 record — that object
is closed (measured, unique, inert). LOR's object is **the first
budget at which a welded record carries a refinement law the grammar
can act on**, and this seat's measurements put **two** candidate
objects on the board where the paper registers one:

| # | budget | record | struct-alive | free items | paper-04 DYADIC | paper-06 record-level | paper-09 kernel | declared? | witnesses |
|---|---|---|---|---|---|---|---|---|---|
| **LOR-A** | **R = 6** | **(2,2,2)** | yes (all 6 rounds saturate) | **0 — MOTIVATED** | **admissible, fiber 1 (the split is FORCED)** | **unique: the only pinned-transitive vector in the whole 361-point box** | empty ($g(2)=0$) | **no** | $\ge 72^2 = 5{,}184$ |
| **LOR-B** | R = 8 | (2,2,4) = G-DIAG2 | yes | **2 — UNMOTIVATED** (fibers 36/3, by T1 — verified) | admissible, ceiling 1 | splittable | **complete derived law** | **yes** | $\ge 276^2 = 76{,}176$ |

Both rows are this seat's recomputations, not the paper's. LOR-A is
two rounds cheaper, is built from paper-19's own 72 triples, and is the
**only** one of the two at which the weld is motivated. LOR-B is the
only one of the two at a declared record with a live renewal kernel.
**They are complementary, and running LOR-B without LOR-A would leave
the cheaper and more decisive rung unmeasured.**

**The gates LOR must carry.**

1. **The drive gate** (the real question at both rungs, and the one
   thing neither paper has done): does the committed grammar *drive* a
   concatenation, with the conflict-supply question re-asked 2 (resp.
   4) rounds wider? The paper's §3.4 record-length spectrum already
   shows supply is not uniform across the window; at 6 and 8 rounds
   this is where a REFUSED can appear. Outcomes first-class:
   `LOR-DRIVEN` / `LOR-REFUSED-AT-SUPPLY` / `LOR-BRANCHING`.
2. **The move gate, two-way.** A law is only reached if a *move*
   consumes it. Pre-register both: DYADIC (needs the product > 0 —
   satisfied at both rungs) and SINGLE-INTERVAL (REFUSED at this arena
   shape — must be re-tested, not assumed, at the refined site set).
   A unit that reports "the law is non-empty" without a move that
   consumes it has reproduced paper-21's crack, not opened the door.
3. **The motivation gate.** At LOR-A the weld must return **zero free
   items** (T1 predicts fibers 1/1/1). If it does not, T1 is false.
   At LOR-B it must return **36/3/1** (T1 predicts UNMOTIVATED at a
   declared record). Two pre-registered, falsifiable predictions.
4. **The commutation gate.** R6a's refinement-commutation defect
   (refine-then-advance vs advance-then-refine) is the object that
   would make the law a *dynamics* rather than a measure. It has never
   been evaluated on a welded record.

**The walls LOR must inherit.** All four of paper-21's, plus one
**new** one this seat raises: at (2,2,2) the induced form is
$q = [[2,-1],[-1,2]]$ — paper-19's hexagonal Gram matrix, doubled. The
hexagonal resonance returns at LOR-A and must be named before the rung
is driven, not after. And LOR-B sits at the budget where I7's own
**indefinite** record G-INDEF = (1,1,6) first becomes clean-reachable
($R = 8$, same as G-DIAG2): the signature wall must be pre-declared at
R = 8 in the pin, not in the paper.

---

## 4. Row 4 — G-SINGULAR's two senses, reconciled

**The apparent tension.** Paper-20: the coupled walk leaves I7's
admissible class at horizon 5 with exact probability
927415552/847288609443, and all 1,316 inadmissible leaves carry the
excess pattern (0,0,3) at exactly one site — codes (4,1,1)@379,
(1,4,1)@471, (1,1,4)@466, all at $\det = 0$. Paper-21: those same
three codes never occur at any site of any of the 100,080 covering
quadruples — 0 occurrences.

**They are consistent. The objects are different, in three ways —
and none of them is budget size.**

1. **Different carriers of the number.** Paper-20 classifies *leaves
   of a coupled walk's frontier* — histories over the R = 3 welded
   record, whose field is (1,1,1) plus the walk's own division events.
   Paper-21 classifies *ordered grouping quadruples* — static R = 4
   schedules — by the field they induce. A walk-record is not a
   grouping-induced record, and neither census quantifies over the
   other's objects.
2. **Different quantisation of deposition — this is the mechanism.**
   The walk emits **one** division event per coupled step and can
   therefore pile 3 events on a single cell while every other cell
   stays at 1 (a 30-incidence field with one cell at 4). A grouping
   round deposits **nine** pairs in one partition-structured block,
   and this seat's measurement shows what that costs: **across all
   100,080 covering quadruples the maximum cell count is 2** — the
   whole covering class lives in 7 site codes, all inside
   $\{1,2\}^3$. A count-4 cell with the remaining 26 cells still
   covered is not merely absent; it is outside what four *blocks* can
   build. **The two senses differ by block structure, not by budget.**
3. **Different direction of approach.** The walk approaches $\det = 0$
   from inside an already-covered record by adding; the static census
   asks what four rounds can build from nothing.

**And the positive half of the reconciliation, which neither paper
states.** G-SINGULAR is not unreachable by the static family — it is
reachable **two rounds up**: as a homogeneous record (1,1,4) its clean
budget is $R = \sum n_i = 6$. So:

> **THE LICENSED JOINT SENTENCE.** *The coupled dynamics reaches
> G-SINGULAR's site code three events above the R = 3 weld; the static
> R = 4 covering family reaches it nowhere, because no covering
> quadruple carries any cell above count 2; and the static family does
> reach G-SINGULAR as a whole record at R = 6, its clean budget.
> "G-SINGULAR is reached" and "G-SINGULAR is never reached" are
> statements about a site-local code under unquantised event
> deposition and about a field induced by whole grouping rounds
> respectively. Neither result bears on the other, and the corpus's
> singular boundary is reached by both arms — at different budgets, by
> different mechanisms.*

**This also closes S-4 from "measured, not explained" to "measured,
with a mechanism".** The paper registers the empty cell as unexplained.
The mechanism is: *the R = 4 covering class has maximum cell count 2*,
from which the absence of all three breaking codes (each of which
requires a cell at 4) follows immediately, and from which the whole
determinant spectrum follows as well — codes in $\{1,2\}^3$ have
determinant exactly $3/4$, $1$ or $7/4$, and this seat's per-code
counts add to the paper's published spectrum cell for cell:
$(1,1,1)$@437,184 → 3/4; $(1,1,2)+(1,2,1)+(2,1,1)$ = 129,168 + 128,736
+ 128,736 = 386,640 → 1; $(1,2,2)+(2,1,2)+(2,2,1)$ = 25,488 + 25,488 +
25,920 = 76,896 → 7/4. **The det spectrum is not three empirical
values; it is the image of $\{1,2\}^3$ minus the unaffordable
(2,2,2).** Recommended as an addition to S-4 (MINOR-5).

---

## 5. Row 5 — the SIG handoff: the row SIG's pin MUST carry

**The paper's handoff, as phrased in the ledger:** *no negative det in
the covering class ⟹ the indefinite form is DYNAMICS-ONLY.*

**This seat's verdict: the implication is NOT LICENSED, and shipping
it unqualified would make SIG report an artifact.** Three reasons,
each measured:

1. **The premise is forced by the code range, not by any
   dynamics/kinematics asymmetry.** Over the covered code box
   $[1,4]^3$ — all 64 codes — the determinant is **never negative**
   and is zero at exactly the 3 named codes. At R = 4 a covered site
   *cannot* carry an indefinite form, whatever schedule builds it.
   The covering-class measurement therefore carries no information
   about "dynamics vs kinematics"; it carries information about the
   number 4.
2. **The premise is scoped to covered sites.** Deviation 3 leaves the
   non-covering part of the family unprofiled, and at an uncovered
   site an indefinite form is trivially available (e.g. code (0,1,3),
   $\det = -1$). "No negative determinant at R = 4" is true of covered
   sites and false of the family.
3. **Indefiniteness is budget-gated, and the gates are computable.**
   A covered site can first carry $\det < 0$ at **R = 5**, at (1,1,5)
   and its two relabellings (verified: the R = 5 reachable code set is
   181, of which 6 are covered-but-not-posdef and 3 have $\det < 0$).
   I7's own declared indefinite record **G-INDEF = (1,1,6) has clean
   budget R = 8**. On the dynamical side, reaching $\det < 0$ from
   (1,1,1) needs **four** events on one cell, not three — so
   paper-20's horizon 5 cannot reach it either (its earliest third
   visit is step 5; a fourth is step ≥ 6).

**THE ROW SIG'S PIN MUST CARRY, in these words:**

> **At the arena and horizon currently pinned, the indefinite region
> is unreached by BOTH arms, and for reasons that are theorems rather
> than measurements: statically, no covered site at R = 4 can have
> negative determinant (0 of 64 codes in $[1,4]^3$); dynamically,
> paper-20's walk reaches $\det = 0$ at three events and $\det < 0$
> needs four, beyond its horizon. SIG MUST therefore establish
> REACHABILITY BEFORE POLARITY: it must declare a budget or horizon at
> which $\det < 0$ is reachable at all — the floors are R = 5 for a
> covered site statically, R = 8 for I7's own declared G-INDEF, and
> horizon ≥ 6 dynamically — and gate that reachability as a
> pre-condition. A SIG that runs at R = 4 / horizon 5 and reports
> SIGNATURE-AVOIDED will have measured an empty region, not an
> avoidance.** Under #34 (every falsifier must REACH its gate), the
> `SIGNATURE-SELECTED` arm is currently unreachable, and a two-way
> verdict is not yet posable.

That is the single most consequential handoff row in this review, and
it is a *precondition*, not an objection: it makes SIG runnable.

---

## 6. Row 6 — the PER-R inheritance: what the R = 5 census must carry
verbatim

**Carried verbatim — the METHOD, never the numbers.**

1. **The saturation theorem as a schema, not as "36".** The load-bearing
   fact is per-*round* and budget-independent: **no round deposits more
   than 9 link incidences** (spectrum 1@0, 27@4, 54@6, 162@7, 36@9;
   cross-check: the missing quarter of all $280\times 9$ pairs is
   exactly the one undeclared direction). From it, at *every* R:
   a homogeneous target with $\sum n_i = R$ forces every round to
   saturate, so a census over $36^R$ is exhaustive over $280^R$. What
   must **not** be inherited: the numbers 36⁴, 1,679,616 and 276, all
   of which are target- and budget-specific.
2. **The budget law $R = n_1+n_2+n_3$** for a homogeneous record under
   a STRUCT-alive schedule. This is the price law's real content and
   it is what makes PER-R's questions answerable in advance.
3. **The licensing pattern**: a declared window named *inside* the
   verdict string, licensed by the driven-vs-combinatorial equality
   measured on every driven record (600/600 here), with every other
   column exhaustive over an object the window does not cap.
4. **The dictionary** [ACTOR→SITE | CO-DIVISION-ACTOR-PAIR→LINK |
   DIVISION-COUNT→$n_\ell(x)$], which is budget-independent and has now
   been carried at two budgets with the same 1296/1296 structure.

**Pre-registered predictions PER-R must test (this seat's, falsifiable,
derived from the two theorems).**

- **P1.** At R = 5, **no declared I7 record is clean-reachable** — no
  declared record has $\sum n_i = 5$ (verified against all nine). The
  clean-reachable homogeneous records at R = 5 are exactly the six with
  $\sum n_i = 5$: (1,1,3), (1,3,1), (3,1,1), (1,2,2), (2,1,2), (2,2,1),
  all admissible, none declared.
- **P2.** At R = 5, zero free items is **impossible** ($3 \nmid 5$), so
  the R = 5 weld verdict must again be UNMOTIVATED with the site fiber
  at 36.
- **P3.** Consequently **R = 5 is strictly weaker than R = 4**: it
  keeps the priced map and loses the declared record. If PER-R measures
  a declared record or zero free items at R = 5, one of the two
  theorems is false.
- **P4.** The identity-breaking codes fill or stay empty: at R = 5 the
  slack is 18 (against 9), and (1,1,4) costs 3 of it. Whether the
  covering class's maximum cell count rises above 2 is the whole
  question, and it is the same census SIG needs.

**The price-sequence question — "what binds after the cover?" —
must NOT be inherited as an open question.** See row 7.

---

## 7. Row 7 — the price sequence: a law, or three data points?

**Neither, as stated. It is a trichotomy with one free parameter, and
it TERMINATES at R = 4.**

The three rows are the three cases of a single comparison, $9R$ against
27:

| | condition | what binds | why |
|---|---|---|---|
| R = 2 | $9R < 27$ | the budget | covering is infeasible at any schedule |
| R = 3 | $9R = 27$ | the perfect matching | covering forces exact disjointness |
| R ≥ 4 | $9R > 27$ | the cover | covering with slack $9(R-3)$ |

So it is a **law** in the sense that the three rows are not
independent measurements — they are the three branches of one
inequality, and this seat verified the boundary values (R = 2: ceiling
3 at 252 pairs against the wall $18//3 = 6$, I7-STRICT empty; R = 3:
72 triples in 12 multisets, field identically 1 at all of them; R = 4:
100,080 with slack 9). But the "sequence" framing — the pin's
`budget-binds → matching-binds → ?` — invites a fourth new binding
condition at R = 5, and **there is none**: for every $R \ge 4$ the
cover binds, with slack $9(R-3)$.

**The licensed reading, and the successor correction:**

> **The price law has exactly three rows and R = 4 is the last one.
> What changes above R = 4 is not WHAT binds but WHAT THE SLACK BUYS —
> and the slack is the whole content of the R-ladder: it is what grows
> the reachable code space (23 → 54 → 105 → 181 at R = 2, 3, 4, 5),
> what will eventually lift the covering class's maximum cell count
> above 2, and what will eventually admit a covered site with
> $\det \le 0$. PER-R's stage 4 must be re-posed as THE SLACK CENSUS,
> not as "what binds at R = 5".**

The paper is not wrong here — §6.1's table is exact and its "slack 9"
is stated — but the head's `SEQUENCE=…->R=4 THE COVER BINDS` reads as
an open ladder, and the successor register does not close it.
Recommended as MINOR-6.

---

## 8. Row 8 — the R = 8 concatenation-reachability row: scope

**The row is sound and its scope is honestly drawn.** Checks:

- $276^2 = 76{,}176$ ✓, and the count is *exact* as a count of ordered
  8-round grouping octuples obtained by concatenation (an octuple
  determines its two halves), hence a strict lower bound on all
  G-DIAG2-inducing octuples ✓ — "at least … before any interleaving is
  counted" is the right phrasing.
- Concatenating two (1,1,2)-inducing quadruples gives (2,2,4) = G-DIAG2
  ✓, at $8\times 9 = 72$ incidences = the paper's budget 72 ✓, with all
  eight rounds saturating, hence **STRUCT-alive** — worth stating,
  since it means the structural leg of the weld would pass at R = 8.
- Deviation 7 correctly prices it: "nothing at eight rounds is driven
  and no constructibility is claimed there" ✓.

**Two scope rows the successor register should add, both derived from
the paper's own T1 and verified here:**

1. **R = 8 cannot repair the weld's motivation.** G-DIAG2 = (2,2,4) is
   not link-constant, so by T1 its fibers are **36/3** — this seat
   computed them directly. The R = 8 rung would return
   `UNMOTIVATED-AT-THE-FREE-ASSIGNMENT` exactly as R = 4 does. S-1
   currently promises the *law*; it must not be read as promising the
   *map*.
2. **R = 8 is also G-INDEF's budget.** (1,1,6) has $\sum n_i = 8$, so
   the first budget at which the corpus's declared indefinite record is
   clean-reachable is the same R = 8. Any unit that drives an octuple
   will be one census away from the signature question, and the wall
   must be declared at pin time (see §3.1).

---

## 9. Row 9 — choice inventory and the prose↔receipt sweep

**The inventory (14 items) is honest and complete.** Items 1–5 forced,
6–9 declared (6 stamped VERDICT-DETERMINING with its counterfactual
measured in-unit at §6.4 — verified: the R = 3 and R = 2 columns are
that counterfactual), 10–12 measured, 13–14 free. The two free items
are instrument-side, deterministic, and neither touches a verdict — the
paper's justification (item 13's fates are independently supplied by
d66's own committed point; item 14's value was taken by paper-19 from a
committed walk this unit cites rather than re-runs) is correct.

**One §15 defect (MINOR-3).** Rows 11 and 12 print `I-DIRECTION-LABEL`
= **3** and `I-ORIENT` = **1** as bare values, while §4.5 measures both
as **not base-map invariant** (spreads [3,6] and [1,2] across the 1296
base maps). The head carries the relativity stamp; the inventory table
— the object a successor lifts — does not. `I-SITE-ASSIGNMENT` = 36 is
genuinely invariant (it is a property of the field, as §4.5 says, and
this seat's computation confirms it) and needs no stamp.

**The sweep — independent, clean.** This seat scanned the paper with
its own thousands-separator-aware numeral regex and matched every value
against the set of integers reachable anywhere in the receipt
(recursively, including inside strings):

- **1,094 numerals found** (a superset of the instrument's 1,068 — my
  scanner also catches sha fragments and section numbers), of which
  **exactly one has no receipt backing: `82`**, the RUNBOOK engraving
  reference in "#82 CLI contract". Not a measurement. **Every other
  numeral in the paper is backed.** The instrument's smaller
  denominator is therefore not concealing a claim.
- **8 fenced blocks; the four verdict blocks each appear exactly
  twice** (head and §9) — E-22's multiset condition satisfied by
  construction. 302 fenced numerals by my count (296 by the
  instrument's), **0 unbacked**.
- **E-24 (fractions): CLEAN.** No `%` anywhere. The only slash-forms
  are `3/4` and `7/4` (determinant *values*, published with counts, not
  as proportions), `1/2` (a matrix entry quoted from paper-19), and
  `36/3`, `1/1` (fiber triples, not fractions). Every ratio in the
  paper is published in the counting form "N of M". The single
  occurrence of "probability" is paper-09's own kernel assigning
  probability zero — its measure, cited, not this unit's. **No
  measure-relative quantity is published without its measure.**
- **Polarity / walled vocabulary: CLEAN.** Every occurrence of
  *signature*, *Lorentz*, *causal*, *continuum*, *cosmological*,
  *dimension*, *metric*, *hexagonal*, *triangular* in the paper sits
  inside a wall statement or its negation. The word *quantum* does not
  appear at all — correct for a kinematic unit.

---

## 10. Row 10 — the walls

**All four hold, and the two paper-reading walls are real
measurements.** Assessed one by one:

- **L-1.** Argued before any test and declined on the right ground (no
  bridge from $\mathbb{Z}_3^2$ translations to any covariance group;
  the unit constructs none). The retracted sentence is absent and its
  gate normalises whitespace, ASCII and markdown prefixes on both
  sides. ✓
- **BHS.** The abstention is measured — the gate scans the run's whole
  measurement layer and its falsifier writes a sprinkling-grade reading
  into that layer and dies there. This is the correct construction for
  an abstention: it cannot be satisfied by silence. ✓
- **Kleitman–Rothschild.** No dimension reading is taken (no chart
  width, no Myrheim–Meyer, no max-shatter), so the height control is
  not owed; again scanned rather than declared. ✓
- **The diagonal.** Read as a direction on a nine-site lattice and
  nothing else. ✓
- **The Lorentzian resonance, NAMED.** This is the strongest resonance
  the line has produced — at R = 4 the induced form is literally the
  identity matrix — and the naming sentence is present, gated, and
  falsified by deleting it from the object under test. ✓ The wall
  holds *and* the pressure on it is correctly described as increasing.
- **The hexagonal resonance.** Named before it is heard, as paper-19's
  S-7 asked. ✓

**One wall row this seat adds for the successors** (not a defect of
this unit): **the resonances return, and they return worse.** At LOR-A
(R = 6, (2,2,2)) the induced form is $[[2,-1],[-1,2]]$ — paper-19's
hexagonal Gram matrix doubled, so the hexagonal resonance returns at
double amplitude. At LOR-B / SIG (R = 8) the clean-reachable declared
record G-INDEF = (1,1,6) carries $\det = -3$ — an actually indefinite
form, at which the *Lorentzian* resonance stops being a resonance and
becomes the object under test. **Both walls must be declared in the
pins, before those rungs are driven.**

---

## 11. Findings

### MAJOR-1 — §4.3's quotable theorem sentence drops its scope, and the
paper's own §6.3 contradicts it as written

**Where.** §4.3 blockquote, and again in §9's readout.

> *"A link-constant field is arithmetically impossible at R = 4, while
> at R = 3 the 27 incidences over 27 cells force one."*
> §9: *"…at R = 4 a link-constant field is arithmetically impossible
> anyway, because 36 incidences do not spread constantly over 27
> cells."*

**Why it is false as written.** §6.3 of this same paper reports
**20,160 covering quadruples at R = 4 whose induced record is
(1,1,1)** — a link-constant field, at R = 4. This seat reproduced them.
The theorem is true only for **STRUCT-alive** (foreign-pair-free, hence
fully saturating, hence 36-incidence) arenas, which is the scope the
*preceding* sentence establishes and the blockquote drops. Blockquotes
are exactly what this corpus quotes forward — this paper itself lifts
six of them from its parents — so an unscoped blockquote is a defect
with a propagation path.

**Exact repair** (both sites; no number moves):

> *"A link-constant field is arithmetically impossible at R = 4 **in
> any structurally live arena**: a foreign-pair-free quadruple deposits
> 36 incidences over 27 cells and 36 is not a multiple of 27. (The
> R = 4 quadruples that do induce a link-constant field — the 20,160 of
> §6.3 at (1,1,1) — deposit only 27, and therefore carry 9 foreign
> pairs and die STRUCT-DEAD, exactly like the control of this section.)
> At R = 3 the 27 incidences over 27 cells force one."*

**Recommended strengthening** (free, and it upgrades the finding into a
result): add the general form, which follows from the same two
theorems —

> *"More generally: a homogeneous record $(n_1,n_2,n_3)$ is reachable
> by a structurally live schedule only at $R = n_1+n_2+n_3$, and zero
> free items requires $n_1=n_2=n_3$; so a live weld is motivated
> exactly at the budgets $R \equiv 0 \pmod 3$, where its record is
> $(m,m,m)$ — and I7 declares no link-constant record at any budget."*

### MAJOR-2 — S-1's closing sentence asserts a global first that its
own scope does not support: the door opens at R = 6, not R = 8

**Where.** §12, S-1, final sentence.

> *"The first budget at which the weld can reach a law over records,
> rather than a record, is therefore R = 8."*

**Why it is unsupported.** The three clauses *preceding* that sentence
are correct and conjunctive — R = 8 is indeed the first budget at which
R6a's dyadic move, CR-B's record-level splittability **and** R6b′'s
complete derived law all hold at once. The closing sentence drops the
conjunction and the scope (the reasoning runs inside G-FLAT's own scale
family $(a,a,2a)$), and asserts a global first. **At R = 6 the record
(2,2,2) satisfies the first two clauses, and satisfies them better:**

- reachable, constructively, by concatenating any two of paper-19's own
  72 I7-STRICT triples: $\ge 5{,}184$ ordered witnesses, field ≡ 2 at
  all 27 cells, all six rounds saturating, 0 foreign pairs
  (**verified here**);
- **zero free items** — link-constant, so site fiber 1 and label fiber
  1 by this paper's own T1 (**verified here**), i.e. the weld would be
  MOTIVATED, which R = 8 provably cannot be;
- paper-04's DYADIC move admissible with raw fiber $1^{27} = 1 > 0$,
  and R6a's own committed head calls (2,2,2) the **unique** count
  vector in the 361-point box with a unique split;
- paper-06's law unique **at the record level** — (2,2,2) is the *only*
  pinned-transitive vector in CR-B's entire census;
- admissible ($\det = 3$), and **undeclared** — the same status as
  weld-2's own FOUND witness (#168).

Only R6b′'s kernel fails there (all counts 2, inside the $g(2)=0$
hole). So the honest statement is a **trade that persists**, not a
single first.

**Exact repair** (replace the final sentence of S-1):

> *"Within G-FLAT's own scale family the first refinable member is
> (2,2,4) = G-DIAG2 at R = 8, and R = 8 is the first budget at which
> all three terminal laws are simultaneously non-empty. It is not the
> first budget at which the weld reaches any of them: at R = 6 the
> link-constant record (2,2,2) — reachable by concatenating any two of
> paper-19's 72 I7-STRICT triples, at least 5,184 ordered witnesses —
> carries paper-04's dyadic move at raw fiber 1, is CR-B's unique
> pinned-transitive vector, and is by §4.5's theorem a ZERO-FREE-ITEMS
> weld, at the price of being undeclared and of leaving paper-09's
> kernel empty. **The R = 6 and R = 8 rungs are complementary and the
> successor should measure the cheaper one first.**"*

And add the R = 6 rung to the successor register as its own row.

### MINOR-1 — §5.2 never conjoins its own two emptiness results, so
"non-empty" reads as "usable"

The section establishes (a) paper-06's per-interval law is non-empty at
9 intervals and (b) R6a's `SINGLE-INTERVAL` class — the only move that
could consume a per-interval law — is REFUSED on arena shape, while
DYADIC needs a product that is 0. It never says that together these
mean **no admissible refinement move exists on this record at all**.
*Repair:* one sentence at the end of §5.2 —

> *"The two emptinesses meet: the one law that becomes non-empty is
> per-interval, and the only per-interval move the grammar has is
> refused at this arena shape, so at R = 4 the law is non-empty and
> inert — there is no admissible move for it to act on."*

### MINOR-2 — §4.7's two-way compliance is claimed against a quoted
requirement it does not literally meet

FOUND is exhibited at R = 3, not in the declared R = 4 arena. The
license holds under §15 (R is a declared arena coordinate; inventory
item 6 declares the counterfactual and §6.4 measures it), and the
missing value is provably unreachable in-arena. *Repair:* stamp the row
and state the impossibility as the result it is —

> *"FOUND is exhibited at the declared counterfactual of inventory
> item 6 (R = 3) rather than at R = 4, and it could not have been
> exhibited at R = 4: by §4.5's theorem zero free items requires a
> link-constant field, and by §4.3 a structurally live R = 4 arena
> cannot carry one. The detector's other four values are all exhibited
> inside the R = 4 arena; the fifth is excluded by theorem, not by
> absence."*

### MINOR-3 — the choice inventory prints base-map-relative fibers
without the §15 stamp

Rows 11 and 12 (`I-DIRECTION-LABEL` 3, `I-ORIENT` 1) are values at the
forced base map; §4.5 measures their spreads as [3,6] and [1,2]. Row
10 (36) is genuinely invariant. *Repair:* append to rows 11 and 12
"(at the forced base map; spreads [3,6] / [1,2] across the 1296 — not
base-map invariant, §4.5)".

### MINOR-4 — the head verb `R4-SPLITTABLE-YES` collides with a
terminal paper's committed verb on the same object

CR-B's committed sentence, quoted *inside* this paper, is that G-FLAT
"admit[s] no subdivision at all"; §5.2 says "at the record level CR-B
still marks G-FLAT unsplittable". The head's bracket does disclose the
distinction (`RAW PRODUCT 0`), so this is disclosure-complete — but the
bare verb is what STATUS rows and memory carry. *Repair:* extend the
bracket to `[SPLIT FIBER 1 AT 9 OF 27 INTERVALS, 0 AT 18; RAW PRODUCT
0; RECORD-LEVEL: NO; …]`.

### MINOR-5 — S-4 is registered as unexplained; the mechanism is one
measurement away

*Repair:* add to S-4 —

> *"The absence has a measured mechanism: across all 100,080 covering
> quadruples the maximum cell count is 2 — 20,160 max out at 1 and
> 79,920 at 2 — so the covering class occupies exactly seven site
> codes, all inside $\{1,2\}^3$, and every identity-breaking code
> requires a cell at 4. The determinant spectrum is the image of that
> box: $\{1,2\}^3$ minus the unaffordable (2,2,2) gives exactly
> $\{3/4, 1, 7/4\}$. What remains open is why four rounds cannot lift a
> cell above 2 while still covering, and whether that survives at
> R = 5, where the slack is 18."*

### MINOR-6 — the price "sequence" is framed as open when it closes at
R = 4

*Repair:* one sentence in §6.1 —

> *"The sequence closes here: for every $R \ge 4$ the cover binds, with
> slack $9(R-3)$. What varies above R = 4 is not what binds but what
> the slack admits."*

---

## 12. THE LICENSED CLAIM

Stripped to what this seat will defend, at the scope it will defend it:

1. **The 276 are unit-grade and exhaustive over the whole family.**
   The saturation theorem is correct and its consequence is correctly
   drawn: 276 of 1,679,616 saturating quadruples **is** 276 of
   6,146,560,000 ordered grouping quadruples. Driven, FORCED at 600 of
   600 window schedules, inducing I7's committed G-FLAT row at 27 of
   27 cells with $\det = 1$ and positive definiteness at 9 of 9 sites.
   The window is declared in the verdict string and every other column
   is exhaustive over an object it does not cap. **Fully licensed.**
2. **The weld at a declared record: FOUND at the forced carrier,
   UNMOTIVATED at the free assignment.** Both verbs earned; the
   structural test passes at 1296 = 1296 at both readings; the fibers
   36/3/1 are correct and the 36 is forced by
   $\lvert\mathrm{Aut}(K_{3,3,3})\rvert$ divided by the stabiliser of a
   transversal-triangle decomposition. **Fully licensed**, with the
   control row stamped (MINOR-2).
3. **The trade, in its general form.** *A weld at this carrier can be
   structurally live and motivated exactly at budgets $R \equiv 0
   \pmod 3$, where its record is $(m,m,m)$; a homogeneous record is
   clean-reachable exactly at $R = \sum n_i$; and I7 declares no
   link-constant record at any budget. The declared record and the free
   map are therefore incompatible at every budget, not at R = 4.*
   **Licensed** — it is the paper's own two theorems plus one
   arithmetic step, all verified here. This supersedes "the R = 3
   perfection was the special case".
4. **The split.** *The first welded record with a positive split fiber
   anywhere: 9 of 27 intervals at fiber 1, raw product still 0. Exactly
   one of the three terminal refinement laws is non-empty there, it is
   unique because its fiber is a single point, and it is inert because
   both of the corpus's refinement moves are unavailable at this arena.*
   **Licensed at that scope.** *NOT licensed:* "the first law over
   records", "a law over records exists at R = 4", or any refinement
   dynamics.
5. **The price row.** COVER-27 = POSDEF-9 = I7-STRICT = 100,080 of
   6,146,560,000, exhaustive; 20,988 homogeneous over four records;
   79,092 inhomogeneous; determinant spectrum $\{3/4, 1, 7/4\}$; the
   sitewise identity true at R = 3 and false on the R = 4 code space
   at exactly 3 codes, none of which occurs in the covering class.
   **Fully licensed**, and now with a mechanism (MINOR-5).
6. **What must not travel:** the window as a family statement;
   UNMOTIVATED as a defeat rather than a priced choice; the 36 as a
   count of maps rather than of distinct count fields; "R = 8 is the
   first budget at which the weld reaches a law over records"
   (MAJOR-2); "the indefinite form is dynamics-only" (§5); and any
   dynamics, signature, dimension, cosmological or continuum reading
   whatever.

---

## 13. THE SUCCESSOR REGISTER

### LOR — the law-over-records unit *(new; pins at paper-21 terminal)*

**Object.** The first budget at which a welded record carries a
refinement law the grammar can **act on** — two candidate rungs, both
constructive, neither driven:

- **LOR-A, R = 6, record (2,2,2)**, $\ge 5{,}184$ ordered witnesses by
  concatenating two of paper-19's 72 I7-STRICT triples. Predicted:
  weld MOTIVATED (fibers 1/1/1, by T1), DYADIC admissible at raw fiber
  1 with the split **forced**, CR-B unique at the record level,
  paper-09 empty, record **undeclared**.
- **LOR-B, R = 8, record (2,2,4) = G-DIAG2**, $\ge 76{,}176$ witnesses.
  Predicted: weld UNMOTIVATED (fibers 36/3, by T1 — verified), all
  three laws non-empty, record **declared**.

**Gates.** (i) the drive gate — does the committed grammar drive a
concatenation, with the conflict-supply question re-asked 2 / 4 rounds
wider (`LOR-DRIVEN` / `LOR-REFUSED-AT-SUPPLY` / `LOR-BRANCHING`);
(ii) the move gate, two-way — DYADIC *and* SINGLE-INTERVAL re-tested at
the refined site set, never assumed; a law without a move that consumes
it is paper-21's crack, not the door; (iii) the motivation gate — 1/1/1
at LOR-A and 36/3/1 at LOR-B are falsifiable predictions of T1;
(iv) the commutation gate — R6a's refine-then-advance vs
advance-then-refine defect, never yet evaluated on a welded record, is
what would make the law a *dynamics*.

**Walls.** All four of paper-21's, plus: the hexagonal resonance
returns at LOR-A doubled ($q = [[2,-1],[-1,2]]$), and LOR-B sits at
G-INDEF's budget — both must be declared in the pin, before driving.

**Order.** LOR-A first: two rounds cheaper, built from paper-19's own
objects, and the only rung of the two at which the weld can be
motivated.

### PER-R (paper-29) — the R-ladder census

**Carries verbatim:** the max-9-per-round spectrum and the saturation
theorem **as a schema** (never the numbers 36⁴ / 1,679,616 / 276); the
budget law $R = \sum n_i$; the dictionary; the window-licensing pattern
(driven = combinatorial on every driven record).

**Re-poses:** stage 4 as **the slack census**, not "what binds" — the
price law closes at R = 4 and the slack $9(R-3)$ is the ladder's whole
content.

**Pre-registered, falsifiable:** at R = 5 (i) no declared record is
clean-reachable (none has $\sum n_i = 5$); (ii) zero free items is
impossible ($3\nmid5$); (iii) therefore R = 5 is strictly weaker than
R = 4 — priced map, undeclared record; (iv) the open measurement is
whether the covering class's maximum cell count rises above 2 and
whether the 6 covered-not-posdef codes at R = 5 (3 of them with
$\det<0$) actually occur.

**Standing prediction to test at R = 6:** G-SINGULAR (1,1,4) is
clean-reachable there and is **inadmissible by I7's own criterion**
($\det = 0$) — the corpus's first declared record that its own
admissibility test rejects, met by the static family.

### SIG (paper-24) — the row its pin must carry

**REACHABILITY BEFORE POLARITY.** At the currently pinned arena and
horizon the indefinite region is unreached by **both** arms, by
theorem: statically, no covered site at R = 4 can have negative
determinant (0 of 64 codes in $[1,4]^3$); dynamically, paper-20's walk
reaches $\det = 0$ at three events while $\det<0$ needs four, beyond
horizon 5. **The floors:** R = 5 for a covered site statically
((1,1,5) and its relabellings); R = 8 for I7's own declared
G-INDEF = (1,1,6); horizon ≥ 6 dynamically. SIG must declare and
**gate** a reachable arena before reporting polarity — under #34 the
`SIGNATURE-SELECTED` arm is currently unreachable, so a two-way verdict
is not yet posable, and a run at R = 4 / horizon 5 would report
`SIGNATURE-AVOIDED` on an empty region.

**Also for SIG:** the "no negative det in the covering class ⟹
dynamics-only" implication must not be inherited. The premise is forced
by the code range at R = 4 and says nothing about dynamics versus
kinematics; and it holds only at *covered* sites (an uncovered site
carries $\det<0$ trivially, e.g. (0,1,3) at $-1$).

---

## 14. Recomputation ledger

**87 recomputations, 0 discrepancies.** Independent implementation from
the declared conventions; no import, execution or transcription of the
unit's code; exact integers and `Fraction`s only; scratch at
`.../scratchpad/r4d-ef/` (`recompute_a.py`, `recompute_b2.py`,
`recompute_c.py`, `sweep.py`).

| block | count | contents |
|---|---|---|
| A — the family and the 276 | 23 | partitions ×2 routes; incidence spectrum; max 9; 36 saturating; the foreign-quarter cross-check; $36^4$, $280^{2,3,4}$, 7,560, the family size; 276; 12 multisets; orbit sizes; collinear ×1 with its directions; $276^2$; $72^2$; det over $[1,4]^3$, $[1,5]^3$, $[1,6]^3$; $(n,n,n)$ dets |
| B — the price row | 29 | 38,809 level-2 masks; 100,080 covering (exhaustive over 6,146,560,000); posdef 9/9 at all; det spectrum ×3 values over 900,720 cells; 20,988 / 79,092; the four homogeneous records; the 3 breaking codes at 0 occurrences each; min det 3/4; the 7 per-round site triples and their site-independence; reachable codes at R = 2/3/4/5; breaking codes at R = 4 and R = 5; R = 3's 72 in 12 multisets with field ≡ 1; R = 2's ceiling 3 at 252, 747 non-degenerate, wall 6 |
| C — fibers and structure | 16 | the 7 covering-class codes; max cell count 2; $\lvert\mathrm{Aut}\rvert = 1296$; site/label fibers at (1,1,2), (1,1,1), (2,2,2), (3,3,3), (2,2,4), (1,1,4), (1,2,3); 36 fields with 3 homogeneous; the budget law on all 9 declared records; no declared record at $\sum = 5$; 6 link-constant box points; 0 link-constant declared records; (2,2,2) by concatenation; $\det(2,2,2) = 3$ |
| D — sweep | 5 | 1,094 numerals with 1 non-measurement unbacked; 302 fenced numerals 0 unbacked; 8 fenced blocks, 4 verdicts ×2; E-24 fraction inventory; walled-vocabulary polarity |
| E — controls and window | 4 | ROW/COL/DIA/ANT (field ≡ 1, 27 incidences, 9 foreign); the collinear arrangement ((1,1,2) at every site, 36 incidences, 0 foreign); the 35-multiset resolvable table (4 admissible, 1 declared orbit); the window arithmetic 600 / 520 / 356 and the length spectrum |
| cross-checks | 10 | 20,160 + 79,920 = 100,080; 437,184 + 386,640 + 76,896 = 900,720; 20,160 + 3×276 = 20,988; 20,988 + 79,092 = 100,080; 256 + 264 + 80 = 600; 256 + 264 = 520; 276 + 80 = 356; the record-length spectrum → 600; $9R$ vs 27 at R = 2,3,4; $1296/36 = 36$ |

**Object hashes re-verified at close:** `f54dad8d51b8` / `e387674bfcdd`
/ `27ed73ded234` / `e1f148dd6a0e`, pin `f50630ced3be` — all five
identical to the open.

**Between delivery and adjudication every headline here — the paper's
and this review's — is a candidate reading.**
