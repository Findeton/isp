# TOP — HOSTILE REVIEW R2 (STRUCTURAL / CATEGORICAL LENS)

**Reviewer:** R2, effectus/categorical lens — structural and conceptual.
**Object (frozen, SHA-256-12 verified by me before reading):**

| file | claimed | measured |
|---|---|---|
| `v13/paper-top-topology.md` | `ab09d091ed1d` | **`ab09d091ed1d`** |
| `v13/code/top_topology_exact.py` | `e2d0200e4a06` | **`e2d0200e4a06`** |
| `v13/code/top_topology_output.txt` | `bd213b18d1b1` | **`bd213b18d1b1`** |
| `v13/code/top_topology_receipt.json` | `0fb290cf4bfd` | **`0fb290cf4bfd`** |

All four match. I also verified the unit's foundation hash independently:
`v13/code/tb3_third_base_receipt.json` hashes to
`c9bc956fe75129bdf411e4d1c1ce082d5866e7e63f12712e56f6f231dcf5a9a7`, exactly the
value pinned in the paper's front matter.

**Read in order:** RUNBOOK §0–§15 including all addenda; the pin
(`note-top-topology-pin.md`); the frozen protocol (`note-top-hostile-protocol.md`,
K1–K5 binding); then the paper, the instrument, the output and the receipt.
Background read: TB3 §2, §3.1–§3.4, §5.1–§5.2 (the §3.4 sentence whose scope K4
tests) and the LCB/BRG/TB3 adjudication notes for the verdict-naming precedent.

**Method.** Everything below is recomputed on my own instrument, written from
the published prose before I opened `top_topology_exact.py`. Five scripts in the
session scratchpad; exact integer / `Fraction` arithmetic only; no float
anywhere; nothing imported from the unit. Where the published prose
under-determines the object I built **both** admissible reconstructions and used
the paper's own published census to decide between them (F-12).

**Recomputation count: 236 quantities independently recomputed**, plus five
hash verifications. Breakdown: 90 in the completion/selector census; 20 in the
self-recognition probe; 79 in the nerve rebuild (both variants); 3 in the
automorphism probe; 28 in the residual checks (simplicial nerve, three declared
control complexes, instance consistency, digon generation); 16 read back out of
TB3's committed receipt.

**Zero computed numbers of this unit were found wrong.** Every published
quantity I could rebuild rebuilt exactly. The findings below are about naming,
scope, forced gates, and two disclosures that are missing — not about
arithmetic.

---

## 0. The independent numbers table

Claimed (paper) versus mine (my instrument, built from the prose):

| quantity | claimed | mine |
|---|---|---|
| 1-cells, per coordinate cell | 630×8, 198×2 | **630×8, 198×2** |
| 1-cells, total | 5,436 | **5,436** |
| 2-cells, per checkpoint | 57,120 / 57,120 / 16,512 / 16,512 / 57,120 | **identical** |
| 2-cells, total | 204,384 | **204,384** |
| per-checkpoint $b_0$ | 1,1,1,1,1 | **1,1,1,1,1** |
| per-checkpoint $b_1$ | 0,0,0,0,0 | **0,0,0,0,0** |
| per-checkpoint $\chi$ | 55,896 / 55,896 / 15,720 / 15,720 / 55,896 | **identical** |
| $b_0$ / cycle rank / rank $\partial_2$ | 1 / 5,401 / 5,261 | **1 / 5,401 / 5,261** |
| $b_1$ / $b_2$ / $\chi$ | 140 / 199,123 / 198,984 | **140 / 199,123 / 198,984** |
| gluing formula $1+144+0-5$ | 140 | **140** |
| dimprofile | (35,35,35,35,11,35,11,35,35,35) | **identical** |
| star / link | (302, 17,032) / (35, 17,032, 1, 16,998) | **identical** |
| distinct estimator values at the reference | 1 (CONSISTENT) | **1** |
| $\chi(N_{\mathrm{simp}}) = \sum(-1)^{k+1}\binom{36}{k}$ | 1 | **1** |
| fixed 1-cells, each transposition | 180 | **180** |
| fixed 2-cells, each 3-cycle | 120 | **120** |
| orbit counts, Burnside | (6, 996, 34,104) | **(6, 996, 34,104)** |
| orbit counts, direct enumeration | (6, 996, 34,104) | **(6, 996, 34,104)** |
| quotient $(b_0,b_1,b_2)$, $\chi$ | (1, 25, 33,138), 33,114 | **(1, 25, 33,138), 33,114** |
| coherent 2-cells, five instances | 84,720 / 100 / 41,520 / 36,120 / 41,520 | **identical** (read off TB3's pinned defect multiset: 508,320 / 600 / 249,120 / 216,720 / 249,120, each $=6\times$) |
| sphere / torus / pinch controls | 4,6,4,χ2,(1,0,1),yes / 9,27,18,χ0,(1,2,1),yes / 7,12,8,χ3,(1,0,2),no@0 | **every cell identical** |
| ord$[P^*,u]$ census | 48/384/1,728/1,152/1,152/576 | **identical** |
| completions with $K=\mathrm{GL}(3,2)$ | 252 | **252** |
| its spread over defect order | 4/48/72/128/0/0 | **4/48/72/128/0/0** |
| completions with $K\subseteq\mathrm{GL}(3,2)$ | 336 | **336** |
| $\lvert K\rvert$ at the five rungs | 1/168/12/2,520/360 | **identical** |
| linear elements at the five rungs | 1/168/1/168/24 | **identical** |
| lex-first $Q$ at ord 1,2,3,6 | 4 permutations | **identical** |
| $\mathrm{GL}(3,2)$ element orders / spectrum | {1,2,3,4,7} / {1:1,2:21,3:56,4:42,7:48} | **identical** |
| the 13-candidate table | 13 rows × 5 columns | **9 rows rebuilt, 45 of 45 cells identical** |
| 1-cells at the partially symmetric instance, implied by its published dimprofile | 3,276 | **3,276** |

Four candidate rows (C3, C3b, C6, C7) I did not rebuild: their predicates are
defined against a "reference value computed in the same run", and the paper does
not print that value, so the predicate is not reconstructible from the prose.
That is a reproducibility gap, not an error (noted in F-12).

---

## 1. Findings, most severe first

### F-1 — MAJOR (K3). The citable head of the manifold verdict carries none of its restrictions, against a settled house precedent.

**Evidence.** The emitted verdict is
`TOP-MANIFOLD-READING-CONSISTENT<…>`, with everything that qualifies it inside a
free-text angle-bracket body: not one number (11 and 35 both occur), not a
manifold (no link is a circle), and not general (3 of 5 instances). §8 then
writes it as "`TOP-MANIFOLD-READING-CONSISTENT` with its computed qualifier" —
the head is the citable object and the body is prose that will not survive one
citation hop.

The programme has already settled this, three times, in the direction opposite
to the delivery:

- **LCB (v13 #293, order L-1):** the adjudication ordered *"the naming honest:
  `EMPTY-AT-STRENGTHENED-STANDARD-UNIVERSAL-FOR-THIS-SQUARE`"* — the entire
  scope hyphenated **into the name**.
- **BRG (v13 #273):** the surviving verdict is `BRG-EMPTY-AT-CARRIER`, and order
  B-3 installed `FOUND-AT-DELIVERED-STANDARD-OUTSIDE-COMMITTED-SCOPE` — a
  qualifier longer than TOP's would need to be.
- **TB3 — this unit's own immutable base:** `TB3-A4-CONFIRMED-AT-FIXED-BORN-SHADOW`.

Against that, `CONSISTENT` alone is the one thing in the delivery that will
propagate, and it is the one thing that is not true without its body. RUNBOOK
§10 fixes the form as `UNIT-OUTCOME(-QUALIFIER)`; the pin's own INCONSISTENT
branch already carries a `⟨witness⟩` slot, so hyphenated qualification is
anticipated rather than invented, and per the LCB precedent it is the
**adjudicator** who installs it.

**Adjudication.** The name should carry the qualifier. `CONSISTENT` is honest
only about what the estimator did (it returned one value); it is silent about
what the estimator *is*, and the pin asked "is there a consistent local
dimension reading (the first manifold-shaped question)". A reader who is told
the manifold-shaped question came back CONSISTENT has been told the opposite of
the finding.

**Repair (verbatim).** Rename the head to

> `TOP-MANIFOLD-READING-CONSISTENT-AT-THE-REFERENCE-INSTANCE-NOT-A-MANIFOLD`

keeping the computed body exactly as it stands, and update `PREREGISTERED_MANIFOLD`
so the vocabulary check accepts the qualified head. In §8 replace

> `TOP-MANIFOLD-READING-CONSISTENT` with its computed qualifier;

with

> `TOP-MANIFOLD-READING-CONSISTENT-AT-THE-REFERENCE-INSTANCE-NOT-A-MANIFOLD`,
> whose computed body prints the two realised dimensions, the link's $b_1$, and
> the two instances at which the reading fails.

---

### F-2 — MAJOR (K3). `CONSISTENT` at the reference instance is forced by an automorphism of the drawn table; it is a disclosure, not a measurement, and §4.2 says the opposite.

**Evidence.** I reconstructed the reference drawn table from the paper's own
declaration (eight coordinate cells complete; the two FULL cells at checkpoints
2 and 3 split into three complete blocks of twelve) and then measured its
automorphism group. Result: of 21 candidate generators (uniform permutations of
the relabelling coordinate, and the six wing permutations acting on both
coordinates) **21 of 21 are automorphisms of the drawn table**, and the orbit of
a chart under them is **36 of 36 — the complex is vertex-transitive.**

The mechanism is visible and cheap to state: at the two FULL cells the block
label of a chart is a function of the **frame alone**, so the relabelling
coordinate is free — the complex does not see it. The 36 charts carry only
**six** types (first wing, last wing), six charts to a type, and every
type-preserving permutation is an automorphism.

Consequence: *every* chart-invariant of this complex is chart-independent. The
declared estimator $D(X)=(\mathrm{dimprofile},\mathrm{star},\mathrm{link})$ is a
chart-invariant. So `CONSISTENT` at the reference instance **could not have come
out otherwise** — RUNBOOK §4's "every gate must be a measurement that could have
come out otherwise", and the §14 addendum's "analytically-forced clauses are
disclosures, not must-pass gates".

§4.2 closes with the exact inverse claim:

> Consistency at the reference instance is therefore a measurement about that
> instance, not a property of the construction.

It *is* a property — of the reference instance's symmetry group, computable
without evaluating the estimator once. What genuinely *is* a measurement is that
the other two instances are **not** chart-transitive, which is why they split
24/12; that half of the sentence survives and is the interesting half.

**Note on robustness.** This finding does not depend on my reconstruction being
the instrument's: the same conclusion follows from any pair of $3\times12$
partitions whose intersection pattern has equal-sized non-empty cells, which
both admissible reconstructions have. It is also a finding the unit can settle
in ten lines against its own pair table.

**Repair.** (i) Measure the chart-orbit count of the automorphism group of the
drawn table at every instance and print it beside the estimator's distinct-value
count. (ii) Where the orbit count is 1, enter `CONSISTENT` as a **DISCLOSURE**,
with TB3's own precedent cited — TB3 §5.2 does exactly this for its
algebraically forced zero escape count ("That zero is algebraically forced, and
it is entered as a disclosure"). (iii) Replace §4.2's closing sentence with:

> The reference instance's drawn table is chart-transitive — every chart-invariant
> is chart-independent there by symmetry — so `CONSISTENT` at the reference is a
> property of that instance's automorphism group and is entered as a disclosure.
> What is measured is the contrast: at the partially symmetric setting and at the
> W-class preparation the table is **not** chart-transitive and the estimator
> splits the charts 24/12.

---

### F-3 — MAJOR (K2/K3). The temporal reading of $b_1$ is forced by deviation 2, and the one measurement that would decide whether it is physical was not taken.

**Evidence, three parts.**

**(a) The 140 classes are exactly the cross-read-time digons.** I added, as
2-cells, every "digon" joining two parallel 1-cells (the same chart pair drawn at
two coordinate cells) and measured the rank they add:

| digons added | how many | rank they add | classes they kill |
|---|---|---|---|
| same checkpoint, different **rule** | 2,286 | **0** | 0 of 140 |
| different **checkpoint** | 18,612 | **140** | **140 of 140** |

So no first-homology class compares two rules at one read time (they are already
filled inside the read time), and the cross-read-time digons kill the entire
$H_1$. The paper's "the only 1-dimensional holes are temporal" is exactly right
as a description — and it is exactly what deviation 2 guarantees, because no
2-cell of $N$ is permitted to carry edges from two checkpoints. The holes are
between read times **because nothing is allowed to fill between read times**.

**(b) The flagship number is arithmetic in two integers.** The unit's own
decomposition, closed, is

$$b_1(N) \;=\; (T-1)\bigl(\lvert V\rvert - 1\bigr) \;+\; \sum_t b_1(N_t)
\;=\; 4\times 35 + 0 \;=\; 140,$$

whenever each read time's sub-complex is connected. (It reproduces 136 at the
asymmetric setting too, with the extra components entering as
$1+144+0-9$.) So $b_1=140$ carries exactly two bits of measured information —
each read time is connected, and each read time is simply connected — and
everything else is 5 and 36. The paper's form $1+144+0-5$ is equivalent but
hides that.

**(c) The decisive measurement is missing.** A cross-read-time digon is a
genuine hole only if the identification *drawn* between $X$ and $Y$ at read time
$t$ **differs** from the one drawn at $t'$. The unit measures exactly this kind
of thing for triangles — 84,720 of 204,384 have three drawn maps composing to
the identity — but never for a pair across coordinate cells. If the drawn maps
always agree, the digons are coherent, the honest statement collapses to "the
atlas has no holes at all", and it joins the simplicial nerve's contractibility.
If they sometimes disagree, the 140 classes are a **measured** obstruction and
the temporal reading is earned at measured strength — which, given that 59% of
triangles are incoherent, is where I would bet. Either way the sentence the unit
says it will defend is currently resting on a scope declaration rather than on a
measurement, and the measurement is one comparison loop away.

**Repair.** (i) Run the cross-coordinate drawn-map comparison for every pair
drawn at $\ge 2$ cells; report the count of pairs whose drawn maps disagree and
the rank the **coherent** digons kill. (ii) State the closed form
$b_1 = (T-1)(\lvert V\rvert-1)+\sum_t b_1(N_t)$ in §3.3. (iii) Add to
deviation 2:

> The same-checkpoint scope is also what makes the first homology temporal: no
> 2-cell of $N$ carries edges from two checkpoints, so every cycle comparing two
> read times is unfillable by declaration. What is measured is that each read
> time is connected and simply connected; the temporal character of $H_1$ is a
> consequence of the declared scope, and whether those cycles are a genuine
> obstruction is decided by the cross-coordinate drawn-map comparison reported
> in §3.4.

---

### F-4 — MAJOR (K2). The sentence the unit says it will defend is false of the unit's own more physical complex, by 21 classes.

**Evidence.** §8's defended sentence says "at the declared base the whole of that
topology in degree one is the comparison of read times". In $N_{\mathrm{coh}}$ —
whose 2-cells are exactly those satisfying "the cocycle condition an atlas's
transition maps must satisfy" (§2.3, the unit's own words, i.e. the complex with
the better claim to being the atlas's geometry) — $b_1 = 161$, and by the unit's
own decomposition $161 - 1 - 144 + 5 = \mathbf{21}$ of those classes live
**inside single read times**. The arithmetic checks (I verified
$36-5436+84720 = 79{,}320 = 1-161+79{,}480$). So the sentence holds of $N$ and
fails of $N_{\mathrm{coh}}$.

§3.4 reports the 21 honestly; §8 then generalises past it. This is the §13-era
failure "descent measured at one setting, stated unscoped" in miniature.

**Repair.** Scope the pull-quote to $N$ and put the contrast in the same breath:

> …and at the declared base the whole of that topology in degree one is the
> comparison of read times — of the full complex $N$. Of the coherent
> sub-nerve it is not: deleting the triangles whose transition maps fail to
> compose to the identity adds 21 classes that live inside single read times.

---

### F-5 — MAJOR→MINOR (K1/K4). A second pair of candidates is analytically identical, and only the first collapse is disclosed.

**Evidence.** **C5 (completion $\mathbb F_2$-linearity) and C10 (Fano
collineation) are the same predicate**, not merely coextensive on this family: a
permutation of $\mathbb F_2^3$ fixing 0 maps every line $\{x,y,x\oplus y\}$ onto
a line **iff** it is $\mathbb F_2$-linear (bijectivity plus
$x\oplus y\notin\{x,y\}$ forces $q(x\oplus y)=q(x)\oplus q(y)$). I measured them
identical as sets over all 5,040 completions, and their published rows are
identical in all five columns (32/384, 136, 0, 168, 126) — a coincidence the
table displays and the text does not remark on. Deviation 7 discloses C1 ≡ C2
and stops.

Two consequences the paper should own. The declared family of **13** is **11**
distinct predicates. And the "best reach two of three" tier has exactly **one**
member up to identity: only C1 and C2 pass clauses (a) and (b), and they are the
same predicate. "The best reach 2 of 3", plural, reads as a family-wide near-miss
when it is one predicate, once.

This matters for K1's forking-paths question more than for the verdict:
`NOT-FOUND` is robust (I confirm no candidate passes all three), but the
**denominator** of the search is smaller than advertised, and a family whose
declared members silently coincide is weaker evidence of a genuine search.

**Repair.** Extend deviation 7 and §5.2's disclosure paragraph:

> **C5 and C10 are the same predicate by algebra**, not merely extensionally
> equal: a permutation of $\mathbb F_2^3$ fixing 0 preserves the lines of
> $\mathrm{PG}(2,2)$ exactly when it is $\mathbb F_2$-linear. With C1 ≡ C2 this
> makes the declared family of thirteen names **eleven distinct predicates**,
> and the two-of-three tier a single predicate rather than a pair.

---

### F-6 — MINOR (K4). §5.2's prose misstates C8's clause (a).

**Evidence.** "C1, C2 and C8 hold on the locus and nowhere off it". Measured (by
me, matching the paper's own table): C8 holds at **192 of the 384** locus
completions, and at 0 off it. C8 is *supported in* the locus; it does not *hold
on* it. Clause (a) is total-on-the-locus by declaration, and C8 fails it — which
is why C8 reaches one of three, not two.

**Repair.**

> C1 and C2 hold on all of the locus and nowhere off it — and do not predict
> linearity. C8 holds nowhere off the locus but on only half of it (192 of 384),
> so it fails clause (a) as well as clause (c).

---

### F-7 — MINOR (K4). "and nothing finer" is refuted by a strictly finer purely order-theoretic condition, measured.

**Evidence.** §5.3 says the measured zeros at defect orders 5 and 6 "are exactly
that necessary condition biting, and nothing finer". The element-order argument
is correct and I confirm it: $\mathrm{GL}(3,2)$'s element orders are
$\{1,2,3,4,7\}$; $d_{P^*}(q)\in K(q)$; the 1,728 completions at orders 5 and 6
contain 0 with $K\subseteq\mathrm{GL}(3,2)$. But "nothing finer" is false. I
measured a nested ladder of purely order-theoretic necessary conditions, each
containing all 336 linear-defect completions and all 252 targets:

| purely order-theoretic condition | completions passing | false positives vs $K\subseteq\mathrm{GL}(3,2)$ |
|---|---|---|
| $\mathrm{ord}[P^*,u]\in\{1,2,3,4,7\}$ (the unit's) | 3,312 | 2,976 |
| the **whole $S_3$ defect-order profile** $\subseteq\{1,2,3,4,7\}$ | 1,176 | 840 |
| **every element order of $K$ itself** $\subseteq\{1,2,3,4,7\}$ | 768 | 432 |

So the order-theoretic content is not exhausted by the $P^*$ condition — it
tightens by a factor of 4.3 while staying purely order-theoretic. And the last
row is the answer to K4's conceptual question: even the finest order condition
admits **432** false positives, so **no purely order-theoretic statement
characterises the visit**. Linearity does irreducible work.

**Repair.** Replace "and nothing finer" with the ladder and its conclusion:

> The measured zeros at orders 5 and 6 — 1,728 completions — are that necessary
> condition biting. It is not the finest order-theoretic condition available:
> requiring the whole $S_3$ order profile to lie in $\mathrm{GL}(3,2)$'s
> spectrum cuts 5,040 to 1,176, and requiring it of every element of $K$ cuts it
> to 768, both still containing all 336. But 432 of those 768 still have
> $K\not\subseteq\mathrm{GL}(3,2)$, so the visit is **not** an order-theoretic
> property at any refinement: what puts $K$ inside $\mathrm{GL}(3,2)$ is
> linearity, and linearity is not read off orders.

---

### F-8 — MINOR (K5, structural). No committed number anchors any $\mathrm{rank}\,\partial_2$ computation; §7.1 says one does.

**Evidence.** §7.1: "the $\mathbb F_2$ homology machinery that produces
$b_1 = 140$ at three wings returns $b_1 = 6$ here, and 6 is a **committed**
number. The homology route is anchored to the corpus and not only to itself."

In the instrument the two-wing control builds
`Complex(len(nodes), epairs, [], "two wings")` — an **empty 2-cell list** — and
`Complex.invariants` returns `"b1": cyc_rank - r2_high`. With no 2-cells
$r_2 = 0$, so $b_1 \equiv$ cycle rank **identically**, and the gate clause
`b1_ok = (rows["3"]["b1"] == two["cycle_rank"])` compares that identity against a
cycle rank which anchors `A-2W-RANK-3` and `A-2W-COMMITTED-RANK` already assert.
The clause cannot fail unless the cycle-rank anchor has already failed. The
paper's own table prints the identity in adjacent columns (cycle rank 4 / $b_1$ 4;
6 / 6), so it is visible — but the surrounding sentence claims it as an anchor.

This is deviation 3's own standard ("$\chi$ from Betti numbers is not a second
route. It is an algebraic identity in the ranks") applied inconsistently. And the
consequence is real and structural: **the 2-dimensional half of the homology
machinery — the elimination that produces 5,261, 199,123, and therefore 140 —
carries no external anchor anywhere in the unit.** Its only calibration is the
three declared-standard control complexes typed in this source, which
deviation 10 itself says "buy calibration, not independence". I verified all
three controls reproduce exactly, so the calibration is sound; the point is what
it is, and §7.1 currently claims more.

**Repair.**

> The two-wing control anchors the **1-dimensional** route: nodes, links,
> identification links and cycle rank are each anchored exit-1 against the
> committed receipt. Its $b_1$ column is not a second anchor — with no 2-cells,
> $b_1$ equals the cycle rank identically, and the identity is printed rather
> than counted (deviation 3's standard). No committed number anchors
> $\mathrm{rank}\,\partial_2$; the 2-dimensional machinery is calibrated by the
> declared-standard control complexes of §4.3 alone, which buy calibration and
> not independence.

---

### F-9 — MINOR (K5). Two of the advertised "genuinely independent routes" are related by algebraic identities — the §13 addendum's own test.

**Evidence.** The §13 addendum (v13 #234) rules that "a pair related by an
algebraic identity is one route".

- **Components, four routes.** Route 2 is $\lvert V\rvert - \mathrm{rank}\,\partial_1$;
  route 3 is the same for the **transpose** under the opposite pivot rule. But
  $\mathrm{rank}(A)=\mathrm{rank}(A^{\mathsf T})$ is an identity, so routes 2 and
  3 are one route with two pivot disciplines. (The gate text is careful — "four
  different computations reading different intermediates" — the paper's "four
  ways" is looser.)
- **$\mathrm{rank}\,\partial_2$, two routes.** Route 2 projects onto cotree
  coordinates. Since $\partial_1\partial_2=0$, every $\partial_2$ row is a cycle,
  and the cotree projection is **injective on the cycle space** — so it preserves
  rank by construction. Gate `TOP-HOMOLOGY` calls this "TWO GENUINELY INDEPENDENT
  ROUTES"; the abstract carries it up to "each computed by two genuinely
  independent routes", which then covers $b_2$.

Both are strong implementation checks and would catch a pivot bug. Neither is
logical independence. The third route to $b_1$ — the checkpoint decomposition,
which touches no global elimination — genuinely is independent, and the unit is
right to say so.

**Repair.** Downgrade the wording to "two independent pivot disciplines on the
same rank" for components-2/3 and for $\mathrm{rank}\,\partial_2$, and reserve
"genuinely independent" for the pairs that are: union-find vs elimination; the
$a<b<c$ enumeration vs the ordered triple loop; the decomposition route to $b_1$;
direct orbit enumeration vs Burnside.

---

### F-10 — MINOR (K1/K4). §5.1's title claims what the instrument's own gate says cannot be established.

**Evidence.** Gate `TOP-DECLARATION-ORDER` states, correctly and to the unit's
credit: "That records the ordering **WITHIN ONE EXECUTION**; it is not offered as
proof that the declarations were fixed before any fixture truth was seen, which
no in-run measurement can establish." TB3 — the immutable base — carries the same
disclaimer in its §2 prose.

But gate `TOP-SELECTOR-FREEZE`'s headline reads "THE CANDIDATE FAMILY IS FROZEN
BEFORE ANY FIXTURE TRUTH", and §5.1 is titled **"The candidate family, frozen
before any fixture truth"**. The paper carries the strong claim and not the
disclaimer. RUNBOOK §13.4's real protection is committing the source before the
truth is computed — a process fact, not an in-run one; this unit was delivered in
one commit, so the in-run gate is all there is.

**Repair.** Retitle §5.1 "The candidate family, declared above every
measurement", rename the gate headline to match, and carry TB3's sentence into
the paper's §5.1 body.

---

### F-11 — MINOR (K4). Six candidates carry a receipt provenance the pin does not support.

**Evidence.** `top_topology_receipt.json` tags C1, C2, C3, C3b, C4 and C4b with
`"origin": "pin"` (and the other seven `"worker"`). The pin, `74a472b54b85`,
which I read in full, contains **no candidate list** — only "the selector
declared as a candidate family before fixture truth, per the corridor
discipline". In a receipt whose gate `TOP-ANCHOR-PROVENANCE` boasts that "EVERY
ANCHOR DECLARES ITS PROVENANCE and the split is printed, never averaged", a
provenance tag pointing at a document that does not contain the item is the one
label that should not be loose. It does not reach the paper (§5.1 says only
"declared in the instrument's source"), which caps the severity.

**Repair.** Relabel the six as `"pin-derived"` (they restate the pin's own
order-2-locus language) or `"worker"`, and gate the tag against the pin text so
the label is measured rather than typed.

---

### F-12 — NOTE (K1). The published prose under-determines the complex; §6 is not independently reconstructible.

**Evidence.** The paper says the two FULL cells "split into three complete blocks
of twelve" but never says **which** twelve. I built both admissible
reconstructions — blocks determined by the frame, and blocks determined by the
relabelled wing $\sigma(\text{first})$ — and measured:

| | frame-determined | $\sigma$-determined | published |
|---|---|---|---|
| 1-cells, 2-cells, $b_0$, $b_1$, $b_2$, $\chi$, star, link, dimprofile | all identical | **all identical** | matched |
| fixed 1-cells per transposition | **180** | 156 | 180 |
| fixed 2-cells per 3-cycle | **120** | 96 | 120 |
| orbit counts | **(6, 996, 34,104)** | (6, 984, 34,096) | (6, 996, 34,104) |
| quotient $b_2$ | **33,138** | 33,142 | 33,138 |

So the global invariant table is robust to the ambiguity, and §6's entire
quotient section is **not** — only the published fixed-cell census resolves it.
Likewise: the four candidate rows whose predicate is "equals the reference value"
are not reconstructible (the reference values are not printed), and the 2-cell
counts at the two INCONSISTENT instances are not derivable from their published
dimprofiles (I get 54,336 against the published 57,216 for the natural transverse
model, i.e. the partition pair is neither aligned nor transverse and is not
recoverable from what is printed).

**Repair.** Publish one small table: the intersection pattern of the two FULL
partitions at each instance (a $3\times3$ matrix of block intersections), and the
four "reference values" the C3/C3b/C6/C7 predicates compare against. Two tables,
and §5 and §6 become independently checkable.

---

### F-13 — NOTE (K3, forward). The dimension estimator is **extensive**; it cannot stabilise under any refinement.

**Evidence.** $\mathrm{dimprofile}$ is (size of the overlap component) $-\,1$.
The two realised values are $\{11,35\} = \{12-1,\;36-1\}$ — the estimator
re-encodes the two block sizes and reports nothing else. It scales with the
atlas: the unit's own two-wing run has 4 charts, where the same estimator reads
**3** at a complete cell; at three wings it reads **35**. Going from 2 wings to 3
wings moved the "dimension" from 3 to 35.

A quantity that grows linearly with the chart count is not a dimension in any
sense that could converge, and the *second* obstruction is worse: the simple
overlap graph is $K_{36}$ — diameter 1, every pair of charts overlapping at 8 of
the 10 coordinate cells. **Dimension is a local concept and this atlas has no
locality.** The unit has, in effect, measured that fact ("the atlas has no
simplicial-nerve topology at all") without drawing its forward consequence.

I develop this into the honest requirements in §3 below. It is a NOTE against
the paper (which never claims otherwise, and whose §9 correctly disclaims "one
dimension across coordinate cells") and a MAJOR input to the successor pin.

---

### F-14 — NOTE (K1). Deviation 1 discloses the primacy choice honestly but stops short of its consequence.

Developed in §4 below. In one line: the primary object was chosen after the
simplicial nerve was measured empty, and the chosen object's headline invariant
is **forced non-zero** by the same scope decision, since
$b_1 \ge (T-1)(\lvert V\rvert-1)$ for any atlas with $\ge2$ read times whose
per-read-time overlap structure is connected. Deviation 1 handles the disclosure;
it does not handle the inference.

---

## 2. K3 adjudicated: the manifold verdict's naming

**The question.** Is `TOP-MANIFOLD-READING-CONSISTENT` honest when the reading is
non-manifold (no link is a circle) and instance-specific (3 of 5)?

**My adjudication: no, and the fix is the name, not the body.** Three reasons,
in increasing order of force.

1. **The body does not travel.** RUNBOOK §10 makes the verdict head the unit of
   citation; the LCB, BRG and TB3 precedents put scope into heads for exactly this
   reason, and LCB's was installed *by the adjudicator against a delivered
   unqualified name*. TOP is the same shape of case.

2. **`CONSISTENT` answers a question the pin did not ask.** The pin asked for
   "DIMENSION-like invariants — is there a consistent local dimension **reading**
   (the first manifold-shaped question, posed as a measurement)". The unit
   redefines consistency as *chart-uniformity of a triple* and reports
   CONSISTENT — while measuring that there is no local dimension (two values),
   no manifold (no link a circle), and no stability across the family (3 of 5).
   All three of the pin's substantive sub-questions came back negative and the
   head says CONSISTENT. §9's non-claim ("`CONSISTENT` in the manifold verdict
   means uniform across charts") is exactly the admission that the head is
   carrying a technical sense a reader will not supply.

3. **The positive content is symmetry-forced (F-2).** Once the reference table is
   chart-transitive, the only thing `CONSISTENT` reports at the reference is that
   a chart-invariant is chart-invariant. A verdict head whose positive branch is
   forced at the instance it is read at should not be the delivery's headline in
   unqualified form.

**What survives, and it is not nothing.** The instance contrast is real and is
the unit's genuine finding here: at two of five declared instances the estimator
splits the charts 24/12 with a named witness and a measured 180-fewer-2-cells
asymmetry, and the pinched control shows the estimator can name a non-manifold
point. That is a working instrument with a measured discriminating power. It
deserves a name that says so.

**Recommended head** (repeating F-1):
`TOP-MANIFOLD-READING-CONSISTENT-AT-THE-REFERENCE-INSTANCE-NOT-A-MANIFOLD`.

---

## 3. K3 forward: what $\{11,35\}$ and the temporal $b_1$ mean for the continuum rung

The pin's successor is "the continuum/type-III rung on whatever TOP earns". Here
is what I judge TOP has earned, and the honest requirements that follow.

### 3.1 What is earned

- **A negative that is worth more than the positives.** The atlas's overlaps are
  total: $G = K_{36}$, and the simplicial nerve is $\Delta^{35}$, contractible.
  I verify both. That is a genuine structural fact about the third base and it is
  the most useful thing in the unit.
- **A working, calibrated 2-complex instrument.** The three declared control
  complexes reproduce exactly on my own code, including the pinch witness; the
  quotient is computed two ways and agrees; the census routes are genuinely
  independent. The machinery is sound.
- **A measured instance contrast** (3 of 5 consistent, with witnesses) and a
  measured coherence contrast (41% at the reference; 100% at two instances).

### 3.2 What is not earned: "dimension"

The dimension reading is not a dimension. It is
$\lvert\text{overlap component}\rvert - 1$, i.e. a **size**, and the pair
$\{11,35\}$ is $\{12-1,\,36-1\}$ — a restatement of "eight cells identify
everything, two identify in three blocks of twelve". Three consequences:

1. **It is extensive.** It scales with the chart count (3 at two wings, 35 at
   three). No refinement can make it converge; a finer atlas makes it larger.
2. **There is no locality to be local about.** Every chart pair overlaps at 8 of
   10 coordinate cells. Dimension is a local invariant of a covering; a covering
   whose nerve is a full simplex has no local structure to measure. This, not the
   link's $b_1$, is the real obstruction.
3. **The link test was decided before it was run.** With parallel 1-cells and one
   2-cell per rule-assignment, each link has $E/V = 17{,}032/35 \approx 486$, so
   $b_1(\mathrm{link}) = E - V + 1 = 16{,}998$ is arithmetic, and "a link is
   never a circle" could not have failed. It is a correct and honest statement;
   it is not evidence, and the unit should say so beside deviation 3's standard.

### 3.3 The honest requirements a successor must meet

Written as the requirements I would want in the successor's pin:

1. **Exhibit a base whose overlap graph is not complete.** This is the
   precondition, and TOP has measured that the third base fails it. Until an
   atlas has sparse overlaps there is no local structure and therefore no
   dimension question; every dimension estimator will return either a
   size-of-the-atlas or nothing.
2. **Declare a refinement family, not a single object.** Dimension is a limit
   concept. TOP has two points (2 wings → 4 charts; 3 wings → 36) and the
   estimator diverges along them. A successor must declare the sequence
   (wing count, or read-time refinement, or chart subdivision) *in the pin*, and
   nominate the invariant that is to converge along it, *before* the fixture
   truth.
3. **Nominate an intensive invariant and prove it intensive.** Candidates worth
   pre-registering: a spectral dimension from a walk on the 1-skeleton; a growth
   exponent of balls (dead at $K_{36}$ — diameter 1 — which is itself the
   measurement); or an order-theoretic estimator on the read-time order
   (Myrheim–Meyer style), which is the only family that does not require locality
   in the chart direction and which is the natural bridge to the causal-set line
   already in the corpus. Whichever is chosen, the pin should require a measured
   demonstration that the quantity does **not** scale with the atlas size — the
   test TOP's estimator fails.
4. **Decide the temporal question before building on it** (F-3). Measure whether
   the drawn identification of a pair agrees across coordinate cells. If it does,
   the atlas has no holes and the continuum rung inherits a trivial $H_1$; if it
   does not, the 140 classes are a measured obstruction and the successor
   inherits a genuine cross-read-time holonomy — which is the only thing in this
   unit that could plausibly be called emergent time-like structure. This is one
   comparison loop and it changes what the successor is standing on.
5. **Work in $N_{\mathrm{coh}}$, not $N$.** The coherent sub-nerve is the object
   whose 2-cells satisfy the cocycle condition transition maps must satisfy. It
   is where the 21 intra-read-time classes live, and it is the only one of the
   three complexes with a claim to being the atlas's geometry rather than its
   bookkeeping.

### 3.4 Feature or artifact? My verdict

**Artifact of the declared scope, with an unmeasured residual that could be a
feature.** The temporality of $H_1$ follows from deviation 2 (F-3a) and the
magnitude follows from $(T-1)(\lvert V\rvert-1)$ (F-3b); neither is evidence of
time-like structure emerging. The residual — whether the identifications drawn at
different read times genuinely disagree — is not measured, and it is precisely
the thing that would make the finding a feature. Until it is measured, the
correct summary is: *the atlas has no topology anywhere it is allowed to have
none, and the one place it has some is the one place the complex forbids filling.*
That is a scope statement, and it should be labelled one.

---

## 4. K1 conceptual: is the coordinate-resolved complex's primacy principled?

**Verdict: principled in its warrant, post-hoc in its selection, and honestly
disclosed in the first respect only.**

**What makes it principled — and it is stronger than the paper shows.** §2.3
asserts "The 1-cell convention is TB3's: its transport graph counts one
identification link per (pair, checkpoint, rule)." That is **checkable, and I
checked it**: TB3's committed reference transport graph has 126 identification
links over 6 frames, and

$$8 \text{ complete cells} \times \binom{6}{2} \;+\; 2 \text{ split cells}
\times 3 \;=\; 120 + 6 \;=\; \mathbf{126},$$

exactly TB3's committed number, with the split cells being precisely the two FULL
cells at checkpoints 2 and 3. So the coordinate-resolution is not an invention of
this unit: it reproduces TB3's own committed link count on the nose. That is the
best possible answer to the forking-paths worry and the paper leaves it on the
table as an assertion. **Display the arithmetic** — it converts a claim of
inheritance into a check.

**What makes it post-hoc.** Deviation 1 says it plainly: the simplicial nerve
"carries no invariants, **so** the unit declares three objects … and makes the
third primary". The primary object was designated after the alternatives were
measured empty. That is the forking-paths structure in textbook form — choose the
estimator that returns a signal — and the mitigation (all three declared, all
three computed, all three reported) addresses transparency but not selection.

**What deviation 1 does not say, and should.** The chosen object's headline
invariant is **forced non-zero by the same scope decision**. For any atlas with
$T$ read times, $n$ charts, per-read-time overlap structure connected, and
2-cells confined to a single read time,

$$b_1 \;=\; (T-1)(n-1) + \sum_t b_1(N_t) \;\ge\; (T-1)(n-1),$$

so the primary complex was guaranteed to have $b_1 \ge 140$ before any
measurement was made. The measurement is the residual $\sum_t b_1(N_t) = 0$.
Deviation 1 handles the disclosure of the choice; it does not handle the
inference the choice licenses.

**Does deviation 1 handle it honestly?** On disclosure, yes — genuinely so, and
better than most units in the corpus: three objects declared in D2 before
construction, the simplicial nerve computed and reported rather than buried, the
reason for the primacy stated rather than smoothed. On inference, no. The
one-sentence repair is in F-3(iii) and F-14.

**Bottom line for K1:** the choice is defensible and I would not overturn it. But
"All of its topology is in the coordinates" (the abstract's boldface) reads as a
discovery, and what was discovered is that the *other* two objects are empty. The
third is non-empty by construction; what it measured is that each read time is
simply connected. Those are different sentences and the paper should write the
second.

---

## 5. K4: what survives of the self-recognition reading

**TB3's sentence, checked at its own scope.** TB3 §3.4 ends: "So the ord-2 target
is the completion at which the geometry sees the substrate's own linear group and
no more." I read the paragraph in full. The "So" discharges a comparison over the
five rows of TB3's own table (reference, ord 1, 2, 3, 6), and I verified by
independent rebuild that within those five rows the definite description is
**unique**: $K = \mathrm{GL}(3,2)$ as a set holds at ord 2 and at no other row
($\lvert K\rvert = 1, 168, 12, 2520, 360$; linear elements $1, 168, 1, 168, 24$).
**TOP's claim that TB3's sentence is not contradicted is correct**, and TOP is
right to add that read over all 5,040 completions the uniqueness fails (252
completions reach it). One wording slip: TOP says "scoped in its own text to its
**four** rule-selected targets" while the comparison — and TOP's own §5.3 table —
runs over **five** rungs (four A1 targets plus the reference). Trivial; fix the
count.

**Is there an honest sense in which the linear visit is special?** Yes — two,
both measured by me, and neither currently in the paper:

1. **Conditional on linearity, the geometry takes the whole group.** Among the
   336 completions whose six defects are all linear, $\lvert K\rvert$ distributes
   $1{:}2,\ 3{:}10,\ 4{:}12,\ 12{:}60,\ 168{:}252$ — so $K$ is the **entire**
   $\mathrm{GL}(3,2)$ at **252 of 336 = 75%**. TB3's "sees the substrate's own
   linear group **and no more**" survives cleanly as a conditional with a
   measured three-quarters: once every defect is linear, the geometry almost
   always generates all of the linear group and never exceeds it.
2. **Order 168 does not determine the group, and the coordinate-adapted copy is
   exactly half of it.** Over the 5,040 completions only **25 distinct** subgroups
   $K$ are realised. $\lvert K\rvert = 168$ occurs at **504** completions, split
   **252 that are $\mathrm{GL}(3,2)$ and 252 that are a different order-168
   subgroup**. So "the geometry reaches a group of order 168" is realised twice as
   often as "the geometry reaches the substrate's own linear group", and the
   distinction is measurable, not rhetorical. This is a direct vindication of
   TB3's methodological insistence that naming be earned by **set equality**
   rather than order — and it is the sharpest available defence of the
   self-recognition reading's *form*, even as TOP dissolves its *exclusivity*.

**Is the correct statement purely order-theoretic? No** (F-7). The finest purely
order-theoretic necessary condition I could construct — every element order of
$K$ lying in $\mathrm{GL}(3,2)$'s spectrum — still admits 432 false positives out
of 768. The order spectrum bounds the visit and never captures it. TOP's §5.3 has
the right instinct ("The order does constrain, but only through the element
spectrum") and overstates the closure with "and nothing finer".

**The freeze audit.** The 13-candidate declaration sits above every measurement
in the source; the in-run counter gates zero built subgroups; the `selfreeze-lax`
mutant dies there. That is as much as an in-run gate can do, and the instrument's
own `TOP-DECLARATION-ORDER` gate says so honestly. The paper does not (F-10), and
the receipt attributes six candidates to a pin that does not contain them (F-11).
Table integrity itself: sound arithmetically — I rebuilt 9 of the 13 rows and got
45 of 45 cells identical — but the *effective* family is 11 predicates, not 13
(F-5), and the two-of-three tier is one predicate.

**On the verdict `TOP-FANO-SELECTOR-NOT-FOUND`:** correct, robust, and I would
not disturb it. It is the strongest result in the unit — a pre-registered family,
an exhaustive census, an honest negative, and a mechanism (the lex-first rule
returning a transvection) identified for the phenomenon it dissolves.

---

## 6. K2 and K5 at the depth the protocol assigns me

**K2 — $b_1$ = the read times.** Both halves verified: every checkpoint
sub-nerve has $b_1 = 0$ (my own elimination, all five), and $1+144+0-5 = 140$ with
the global elimination agreeing. The decomposition's hypothesis ($H_2$ additive
over checkpoints) is genuinely measured, not assumed, and I confirm it is exact
because the 1- and 2-cells partition by checkpoint — a block-diagonal fact, so
the third route to $b_1$ is genuinely elimination-free and genuinely independent.
The coherent sub-nerve's $b_1 = 161$ coheres arithmetically (21 intra-checkpoint
classes; $36-5436+84720 = 79{,}320 = 1-161+79{,}480$) and **cuts against** the
deepest sentence rather than supporting it (F-4). The sentence is carried at
measured strength for $N$; it is not carried for the atlas, and it is scope-forced
rather than measured (F-3).

**K5 — instrument.** Anchors: I verified the TB3 receipt hash independently and
spot-verified the load-bearing external anchors — the ord census (6 values), the
lex-first completions (4), the five rungs' $\lvert K\rvert$ / linear counts /
set-equality (15), the ordered defect multiset (6 values, summing to 1,226,304),
and the coherence route through the identity entry $508{,}320 = 6\times84{,}720$
at all five instances. All correct. Route independence: the census routes are
genuinely independent (different loop order, no shared intermediate); the
cell-completeness gate (ordered census exactly $6\times$ geometric, with a
one-cell-drop probe) is a real completeness test and satisfies the #234 addendum.
Burnside-vs-enumeration is genuinely independent and I reproduce both. The
manifold standards are declared-standard and labelled so; I reproduce all three
exactly. Verdict-in-gate with computed qualifiers is properly implemented — the
qualifier is interpolated from measured values, never typed, and `verdict-flip`
falsifies. Two waiver-only gates are named rather than averaged, correctly.
The `TOP-EULER-POINCARE` disclosure is exemplary and is the standard §7.1 fails
to meet (F-8) and the rank-route wording fails to meet (F-9). One scope note:
$\partial_1\partial_2 = 0$ is checked on `self.tris[:2000]`; the key name says
"sampled", but the cap is not printed — print it.

---

## 7. What I could not check

- The chart-level admission machinery (the four-clause predicate at Born level) —
  I rebuilt the atlas's **combinatorics** from the published declaration and the
  published cell structure, not TB3's Born-level admission code. My reconstruction
  reproduces 20+ published invariants including the fixed-cell census, which is
  strong evidence it is the right object, but it is not a rebuild of the
  admission predicate.
- The coherent 2-cell count from first principles: I verified 84,720 through
  TB3's committed defect multiset (an anchor check), not by recomputing which
  triples of drawn maps compose to the identity.
- The two INCONSISTENT instances' internal structure (F-12): not reconstructible
  from what is published. I verified their published 1-cell counts against their
  published dimprofiles (3,276 ✓) and their coherence counts against TB3's
  receipt, but not their 2-cell counts.
- C3, C3b, C6, C7 (predicates defined against unprinted reference values).

---

## 8. Grade

Every number I could rebuild rebuilt exactly — 236 recomputations, zero
arithmetic errors, including all of §3.2, §3.3, §4.2, §4.3, §5.1, §5.2, §5.3,
§6.2 and §6.3. The verdicts' substance is sound: the overlap graph really is
complete, the simplicial nerve really is contractible, `NOT-FOUND` is robust and
well-earned, and the wing quotient is right by two genuinely independent routes.
The instrument is honest in places most units are not — the Euler–Poincaré
disclosure, the declaration-order disclaimer, the waiver naming, the
cell-completeness probe.

What blocks acceptance as delivered is naming and scope on the unit's two
headline sentences: a positive verdict head that carries none of its restrictions
against three settled precedents (F-1); a positive branch that is forced by the
reference instance's own symmetry and is asserted to be a measurement (F-2); a
deepest structural sentence whose temporal character follows from a declared
scope rather than from a measurement, with the deciding measurement one loop away
and not taken (F-3); and that sentence being false of the unit's own more
physical complex (F-4). None of these requires a number to move. All four have
verbatim repairs above.

### **ACCEPT-WITH-FIXES**

Binding on the repair pass: **F-1, F-2, F-3, F-4** (major — the naming, the
forced gate, the scope clause plus the missing measurement, the $N_{\mathrm{coh}}$
contrast); **F-5, F-6, F-7, F-8, F-9, F-10, F-11** (minor — the second
extensional collapse, C8's clause (a), the order ladder, the two-wing anchor
claim, the route wording, the freeze title, the provenance tags); **F-12, F-13,
F-14** as disclosures and as inputs to the successor pin.

No number may move. The two measurements I ask the repair to **add** —
the automorphism orbit count per instance (F-2) and the cross-coordinate
drawn-map comparison (F-3) — are both cheap, both in scope, and both capable of
coming out either way; the second decides what the continuum rung inherits.
