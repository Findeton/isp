# PAPER-23 (R5M, THE CONFIGURATION MEASURE) — EFFECTUS REVIEW (K2)

**Seat:** EFFECTUS — meaning, scope, motivation; the licensed claim; the
choice inventory at the RSQ standard; the successor register; walls
compliance. **Protocol:** v14 ledger #183, row K2. **Objects at
`33da839`,** hash-verified at the start of this review and again at its
end, by `git show 33da839:<path> | shasum -a 256`, both against the
worktree and against the commit:

| object | pinned | measured (start) | measured (end) |
|---|---|---|---|
| `v14/paper-23-measure.md` | `9249dda1c0a3` | `9249dda1c0a3` | `9249dda1c0a3` |
| `v14/code/r5m_measure_exact.py` | `f7de59960fe6` | `f7de59960fe6` | `f7de59960fe6` |
| `v14/code/r5m_measure_output.txt` | `8ee12d000bad` | `8ee12d000bad` | `8ee12d000bad` |
| `v14/code/r5m_measure_receipt.json` | `1e794bd7f5fb` | `1e794bd7f5fb` | `1e794bd7f5fb` |
| `v14/note-r5m-pin.md` | `e5e09f65f83b` | `e5e09f65f83b` | `e5e09f65f83b` |

**GRADE: AWF** — accept with fixes. **55 recomputations: 46
re-derivations of delivered numbers, every one agreeing to the digit,
and 9 measurements this unit did not take.** The rebuild is
independent: my own $\mathbb{Q}(\zeta_8)$ representation (4-tuples of
`Fraction` over $(1,z,z^2,z^3)$, not the instrument's integer
5-tuples), my own indexing, my own Burnside, nothing imported from
`r5m_measure_exact.py` and nothing read back from its receipt.
**No delivered number moves. The verdict word
`MEASURE-DECLARATION-REQUIRED` survives every attack I could mount,
and two of my eight majors STRENGTHEN it.** The three false
delimitation stories I went looking for — an outcome-shaped candidate
list, a privileged chart reading, a Born claim that overstates the
substrate — came back one-for-three: the census is honest in
substance, both readings are genuinely carried, and the Born sentence
names the wrong object.

---

## 1. WHAT I REBUILT, AND WHAT AGREED

Every one of these is mine, from the parents' definitions, before I
looked at the delivered value:

alphabet 25 · admissible rows 80 · coins 640 · sectors 64/64/512 ·
unitarity by a second route 0 failures · chart order 32 · extension
order 128 · link orbits 1 at **both** readings · elements reversing at
least one link 0 and 96 · elements carrying an odd-parity cycle 0 and
12 · swap-fixed coins 32 · fixed-locus checks 655360 with 0 failures
($=640\times32\times32$) · realisable constant twists $\{0,2,4,6\}$ ·
residual groups of order 4 and 8 · orbits **208** ($64\times1 +
144\times4$) and **120** ($8\times1 + 28\times2 + 24\times4 +
60\times8$; members $8+56+96+480=640$) · parent census 632 / 576 / 384
· orbit-closure of all four sets at both readings, 8 of 8 · the whole
null table (79/80, 25/26, 23/24 · 9/10, 9/13, 7/10 · 3/5, 6/13, 7/15 ·
1/10, 4/13, 3/10) · spreads 7/240, 27/130, 9/65, 27/130 ·
cross-invariance 2624 checks 0 failures · Haar closure 278528 of
409600 · monomial coins 128 with 0 closure and 0 inverse failures ·
adjoinable interfering coins 0 of 512 (I ran the **full** closure, not
the delivered 3-round bounded version, and it agrees) · defect ∩
monomial = 0 of 384 · finite order 384 of 640 · Born doubly stochastic
640 of 640, 3 images, fibres 64/64/512 · **both 85- and 86-digit
Burnside integers, digit for digit** · sector multisets $\binom{34}{2}
= 561$ · the point-mass bound $640-113 = 527$ · anchors $10+26+12=48$ ·
the waiver ledger $27+23+6=56$ · and the paper's fenced verdict block
is character-identical to the receipt's `verdict.string` (2921
characters), so no stale head is quoted.

I also built the unit's own falsifier for its positive result: a
configuration differing from uniform on **one** link fails 62 of the
1024 fixed-locus checks. The 655360-of-655360 is not a check that
cannot fail.

---

## 2. THE LICENSED CLAIM

**Licensed exactly as delivered:**

- **No measure on the 640 configurations of R5's swept slice derives
  from any of the eight sources censused.** Each is priced in free
  items; none is zero.
- **The measured symmetry fixes a support, not a measure.** At the
  anchored chart reading the chart-fixed configurations are exactly
  the 640 uniform ones (655360/655360); under the declared extension
  32 survive, the coins commuting with the swap. Both readings are
  carried in the head, in §3, in §6 and in §9. I found no thumb on the
  scale: the two small slips I did find (the receipt's typed
  `minimal.reading`, §3's unqualified bolded sentence) point in
  **opposite** directions.
- **The fibre statement is the licensed form and is exactly right.**
  On a finite $G$-set the invariant probability measures are precisely
  the orbit-constant ones; they form a simplex whose vertices are the
  orbit-uniform measures and whose dimension is $(\#\text{orbits}-1)$.
  120 orbits $\Rightarrow$ 119 independent numbers; 208 $\Rightarrow$
  207. "A declaration picks a point; the simplex is the price" is
  precisely what the mathematics says, and the uniqueness
  $\Leftrightarrow$ transitivity gate is the right gate for it. This
  is the strongest sentence in the unit and it is fully earned.
- **Haar on the 128 monomial coins is the one canonical measure this
  arena hands over, and it carries 0 of the 384 defect-carrying
  coins** — one-directionally (see MAJOR-3 and §5 below for what that
  does *not* license).
- **The declaration is not innocuous.** True, and true by more than
  the unit claims (MAJOR-4).
- **Walls: CLEAN.** Every occurrence of *confinement*, *area law*,
  *string tension* and *potential* in the paper is inside a quoted
  must-not or an explicit denial (lines 70, 480–481, 524). No *QCD*,
  no *continuum*, no *field* claim. The withheld-segment discipline is
  enforced on the product, not promised in prose. The unit makes no
  cross-unit resonance claim at all — it never mentions paper-20 —
  which is the correct call (§5).

**NOT licensed as delivered:**

- **"The substrate derives a measure over the states."** It derives a
  *kernel*. See MAJOR-3. This is the unit's title claim.
- **"8 candidates, 0 derive" read as "no measure derives."** The
  licensed form is "of these eight, none" — until the closure
  principle of MAJOR-1 is stated, at which point the stronger reading
  becomes earned.
- **"Which chart group is declared … fibre 2."** There are at least
  three admissible chart declarations and the unit's one positive
  result turns on which is taken. See MAJOR-6.
- **"Widest disagreement 27/130 on DIAGONAL."** The maximum is a tie.
  See MAJOR-5.
- **"That is the whole of it"** (§6) — the unit's own inventory names
  three verdict-determining axes and §6 prices two. MINOR-5.

---

## 3. THE MAJORS

### MAJOR-1 — the census is delimited honestly but the closure principle that would make it a criterion is unstated, and it is available at zero cost

**Where:** the head's `CENSUS=8-CANDIDATES-0-DERIVE`; §1; §4; §12's
second deviation.

**The row I was asked to decide: principled delimitation or
outcome-shaped?** **Principled in substance, under-argued in form.**
The evidence for *principled*: the pin named three sources and the
unit ran eight, adding the five a reader reaches for next; §12 states
the reason in the correct direction ("a census that leaves them
unmeasured cannot claim that none survives"); and two of the five
extras were the ones that most threatened the verdict (the Born layer
is the only candidate that derives anything, the group structure the
only place a measure is handed over), which is the opposite of
outcome-shaping. The evidence against *outcome-shaped* is decisive:
had the list been drawn to reach the answer, (d) and (g) would not be
on it.

**But a no-derivation is only as strong as its list, and the unit
leaves the list a list.** It has, unused, a criterion that closes it:

> **A canonical (equivariant, zero-free-item) probability measure on a
> finite carrier exists exactly where some declared structure acts
> TRANSITIVELY on it.**

Every one of the eight rows is an instance, and I checked each:

| row | the transitive structure it would need | measured |
|---|---|---|
| (c) invariance | the symmetry group, transitive | **not** — 208 / 120 orbits |
| (d) group Haar | a group acting on itself | **yes on 128 coins** — and Haar exists there and only there |
| (e) $U(2)$ Haar | the carrier as a $U(2)$-orbit | **not** — a finite subset, measure zero |
| (a) pushforward | transitivity borrowed through a correspondence | **no correspondence** |
| (h) holonomy pull-back | transitivity borrowed through a section | **no single group, and a section is one more free item** |
| (b) counting | transitivity by fiat | that *is* the free choice |
| (f) Gibbs | an action, which exists to *break* transitivity | needs the action and the coupling |
| (g) Born | its kernel is transitive on the carrier | **not** — identity off the domino, reducible (my measurement, MAJOR-3) |

With that sentence the head's "8 candidates, 0 derive" stops being a
list and becomes a test a ninth candidate can be run through. Without
it, a reader is entitled to ask what the ninth would be — and the
protocol asked me for two of them:

**The max-entropy candidate.** The unit answers it (§6) in **ungated
prose**: no census row, no free-item price, no gate, no receipt key,
no numeral. It is the only reader-move in the paper handled that way,
and it is the move the paper itself says "a reader will reach for."
The argument as written also covers only half the object: "maximising
relative to counting-on-configurations returns
counting-on-configurations" is true of *unconstrained* relative
entropy; under a constraint $\langle f\rangle = c$ maximum entropy
returns $e^{-\lambda f}\!\cdot q$, i.e. it becomes candidate (f) with
the coupling supplied. So the conclusion survives — by two different
routes for the two sub-cases — and the argument states only one.

**The stationary-measure candidate.** Not in the census at all, and it
is the one candidate that *could* have returned the third
pre-registered outcome: no dynamics acts on these configurations
(R5 declares "no dynamics for the link variables," quoted in §4.6), so
a stationary measure has nothing to be stationary for. Under this
unit's own convention that is a price (declare a dynamics), not a
blockage — which is why §1's "`MEASURE-BLOCKED-AT` is **forced shut**"
survives; but that row's forcing is *census-relative* and the paper
states it as a property of the arena.

**Repair (exact).**
1. §4 opens with the transitivity criterion as displayed above, and
   §4's table gains a column "the transitive structure required."
2. The head gains one segment:
   `CENSUS-CLOSURE=A-CANONICAL-MEASURE-EXISTS-EXACTLY-WHERE-SOMETHING-ACTS-TRANSITIVELY;8-ROWS-ARE-INSTANCES;A-9TH-CANDIDATE-IS-DECIDED-BY-THE-SAME-TEST`.
3. Max-entropy enters as census row **(i)**, `free_items` ≥ 1, split
   into the two sub-cases (unconstrained → returns its reference, and
   the reference is the free item already priced at (b); constrained →
   is (f) renamed, and the constraint is a second free item), with a
   gate that the arena supplies no pinned expectation to constrain on.
4. The stationary measure enters as census row **(j)**,
   `free_items` ≥ 1, verdict
   `NO-DYNAMICS-ON-THE-CONFIGURATIONS-BY-THE-PARENTS-OWN-DECLARATION;A-COVARIANT-CHAIN-DERIVES-IFF-IT-IS-IRREDUCIBLE`,
   with §1's "forced shut" row restated as census-relative.
5. §12's second deviation says "the pin's three plus five" — the
   receipt's choice row says "the pin's plus two" (MINOR-1).

### MAJOR-2 — the fibre's consequence is under-reported by the width of the whole simplex

**Where:** §7; §9's last bullet; the head's
`WIDEST-DISAGREEMENT=27/130`.

**What (measured, mine).** 27/130 is the disagreement between the two
**named** nulls. Over the *whole* invariant simplex the admissible
mass of every one of the four sets is exactly $[0,1]$, at both
readings, because each set and its complement contain whole orbits —
NON-COMMUTING: 84 orbits inside, 36 outside; DEFECT-CARRYING: 56 / 64;
NON-FLAT: 115 / 5; DIAGONAL: 36 / 84. So **invariance constrains
R5's headline probability not at all**, and the extremes are not
pathological objects: the non-flat indicator is orbit-constant at both
readings (measured), so the Gibbs family $e^{-\beta S}q$ built from
**this unit's own measured functional** is invariant, and it sweeps
R5's headline from 9/10 at $\beta = 0$ to **0** as $\beta \to \infty$
(the 8 flat configurations carry 0 non-commuting pairs — measured).

The claim in §7 — "the choice moves … by more than a fifth" — is true
(27/130 > 1/5) and is the *floor*, not the price. This is the single
place where the unit sells itself short, and the repair costs one
paragraph.

**Repair (exact).** §7 gains: "The two nulls disagree by 27/130. That
is a floor. Because each set and its complement are unions of orbits —
84 orbits inside NON-COMMUTING and 36 outside, at the extension
reading — the invariant simplex admits mass 0 and mass 1 for every set
in the table: **invariance alone constrains the parent's headline
probability not at all**, and the endpoints are reached by measures a
physicist would write down (the Gibbs family in the arena's own
non-flat indicator, orbit-constant at both readings, runs the
non-commuting mass from 9/10 to 0)." Head:
`WIDEST-DISAGREEMENT-BETWEEN-THE-TWO-NAMED-NULLS=27/130;RANGE-OVER-THE-WHOLE-INVARIANT-SIMPLEX=[0,1]-FOR-ALL-FOUR-SETS-AT-BOTH-READINGS`.

### MAJOR-3 — the Born sentence names the wrong object, and it is the paper's title

**Where:** the title; §4.7; §9's fifth bullet; the head's
`(g)BORN=DERIVES-EXACTLY-AND-LANDS-ON-THE-STATES`; the gate
`G-BORN-LAYER-IS-A-MEASURE`.

**What (measured, mine).** $B(U)=\lvert U\rvert^{\circ 2}$ is a
$16\times16$ **doubly stochastic matrix** — a kernel — and it is the
**identity off the domino** at every one of the 640 configurations
(measured). The paper says "$B$ is a distribution over the carrier's
16 states." A $16\times16$ doubly stochastic matrix is not a
distribution over 16 states; each of its *rows* is. Once that is said,
the object is a conditional law, not a measure.

Press it for a **measure** and it does not fix one either. Its
stationary set is itself a simplex: I computed
$\dim(\ker(B^{\mathsf T}-I)) - 1$ exactly in each sector —
**15 in the diagonal sector, where $B$ is the identity matrix and
*every* state distribution is stationary, and 14 in the other two**
(balanced block $\left[\begin{smallmatrix}1/2&1/2\\1/2&1/2
\end{smallmatrix}\right]$, antidiagonal block the swap). Double
stochasticity does single out the uniform state measure as
*stationary* — but the uniform measure on the states is the counting
measure, which is the very object candidate (b) calls "the declared
null carrying no information."

So the unit's deepest sentence, as written, claims for the state space
exactly the thing it denies for the configuration space. The verdict
is untouched — the asymmetry is real and is arguably sharper after the
repair — but the asymmetry is **law vs nothing**, not **measure vs
nothing**.

**Repair (exact).** Title → "The Substrate Derives a *Law* on the
States, Not a Measure on the Configurations." §4.7 → "$B(U)$ is a
**kernel**: each of its rows is an exact probability distribution over
the carrier's 16 states, at every one of the 640 configurations, and
it is doubly stochastic, so the uniform state measure is stationary
everywhere. It is the identity off the domino, hence reducible: its
stationary measures form a simplex of dimension 15 in the diagonal
sector, where $B$ is the identity, and 14 in the other two. So the
substrate derives, exactly, a **transition law** on the states; it
derives a measure on neither space, and on the configurations it
derives nothing at all." §9's bullet and the head segment follow
(`(g)BORN=DERIVES-A-LAW-ON-THE-STATES-EXACTLY-NOT-A-MEASURE-3-KERNELS-FOR-640-CONFIGURATIONS-STATIONARY-SIMPLEX-DIM-15/14/14`).
Rename `G-BORN-LAYER-IS-A-MEASURE` → `G-BORN-LAYER-IS-A-KERNEL`.
**This is the deepest sentence in the unit and it should be the one
sentence the adjudication settles word by word.**

### MAJOR-4 — the widest-disagreement segment is an undeclared tie-break (#91)

**Where:** the head's `WIDEST-DISAGREEMENT=27/130-ON-DIAGONAL`;
`G-TWO-NULLS-DISAGREE`; code L1584–1590.

**What (measured, mine).** The maximum spread 27/130 is attained by
**two** sets: DIAGONAL ($4/13 - 1/10$) and NON-COMMUTING ($9/10 -
9/13$). `spreads` is built over `sorted(sets.items())` and `max`
returns the first maximal element, so the alphabetical accident
`DIAGONAL < NON-COMMUTING` decides which set the head names — and it
names the sector this unit added over the parent's own headline set.
Had the tie gone the other way the head would read
`ON-NON-COMMUTING`, which is also the set §7's prose is about. RUNBOOK
#91's tie-break rule is explicit: state `maxhits == 1` immunity or
price the tie-break, as a gate. Here `maxhits == 2` and neither is
done.

**Repair (exact).** Publish the arg-max **set** —
`WIDEST-DISAGREEMENT=27/130-ATTAINED-BY-2-SETS(DIAGONAL,NON-COMMUTING)`
— and add a gate that asserts the arg-max multiplicity explicitly, so
a future run in which the tie breaks is a change the head shows.

### MAJOR-5 — the chart-group fibre is not 2, and the unit's one positive result turns on which chart is declared

**Where:** §3 ("carried in the inventory with fibre 2"); the choice
inventory row `WHICH CHART GROUP IS DECLARED`, `fibre: 2`; §3's bolded
"So R5's declared window is the chart-fixed locus itself."

**What (measured, mine).** Fibre 2 asserts that the admissible chart
declarations are exhausted by R5's two. They are not — R5 declared
two; nothing makes them exhaustive. The translation group alone has 15
subgroups, and the most natural third declaration decides the unit's
headline: **under the translations-only chart (order 16, no direction
relabelling) the link set falls into 2 orbits and the chart-fixed
locus is the $640^2 = 409600$ two-coin configurations, of which R5's
swept 640 is a proper subset.** So the positive result is carried
specifically by the direction relabelling being inside the declared
chart, and under a third admissible reading R5's window goes back to
being a genuine restriction. §15 requires exactly this to be visible:
the result is not invariant across the declared free axis, so it is
arena-relative and must say so.

**Repair (exact).** Inventory row → `fibre: "UNBOUNDED (2 INHERITED
FROM THE PARENT, BOTH MEASURED)"`, instances 2. §3's bolded sentence →
"**So R5's declared window is the chart-fixed locus of the declared
chart** — and it is the direction relabelling that forces it: drop it,
and the fixed locus is the 409600 two-coin configurations, of which
R5's 640 is a proper subset." §9's second bullet gains the same
clause. No number moves; a claim's scope does.

### MAJOR-6 — the weld-2 silence is L-parity-relative, and the successor register's gating item inherits it unqualified

**Where:** §4.1's "This target is bipartite too"; §9's first
"Not decided" bullet; §11's first register item; §12's fourth
deviation; the head's
`WELD-2s-STRUCTURAL-BLADE-IS-SILENT-HERE-BECAUSE-THIS-LATTICE-IS-BIPARTITE`.

**What (measured, mine).** $(\mathbb{Z}_L)^2$ is bipartite **exactly
when $L$ is even** — I checked $L = 3,\dots,8$: bipartite at 4, 6, 8;
not at 3, 5, 7; degree 4 throughout. So the blade's silence is a
property of the declared **even** $L$, not of the target species. At
any odd $L$ the target carries odd cycles, weld 2's blade **fires**,
and the correspondence question is *closed by inheritance*, not open.
The OPEN ruling is **correct** and should stand — I looked for a
reason to call it inherited-closed and there is none at $L=4$ — but it
is open over the even-$L$ family only, which includes R5's own refined
$L = 8$ and every scaling step the R6 programme would take.

**Repair (exact).** Every one of the four sites gains the clause "…
because this lattice is bipartite, which at $(\mathbb{Z}_L)^2$ holds
exactly when $L$ is even (measured at $L = 3,\dots,8$); at any odd $L$
the inherited blade fires and the question is closed." The register
item becomes: "the correspondence census at this target, **for the
even-$L$ family**." This is the cheapest strengthening in the review
and it is the one the scaling programme will use.

### MAJOR-7 — "(f) GIBBS = NO-ACTION" is an overstatement this unit's own §7 refutes

**Where:** the head's `(f)GIBBS=NO-ACTION-NO-COUPLING`; §4.6.

**What.** The arena is not action-free; it is action-*ambiguous*. This
very unit measures four orbit-constant functions on the slice (§7's
table), and I verified the non-flat indicator is orbit-constant at
both readings — each is an admissible $S$, and each generates an
invariant Gibbs family inside the 119-simplex. The price
(`free_items` = 2) is right in number and the §4.6 sentence about an
action being *more* data than the measure it produces is exactly
right; only the reason-word is wrong, and it is wrong in the direction
that makes the arena look emptier than it is.

**Repair (exact).** Head → `(f)GIBBS=NO-DECLARED-ACTION-AND-NO-COUPLING;THE-ARENA-SUPPLIES-4-ORBIT-CONSTANT-FUNCTIONALS-ANY-OF-WHICH-WOULD-SERVE-SO-THE-CHOICE-IS-FREE-NOT-EMPTY`.
§4.6 gains one sentence naming the four and the fact that each Gibbs
family lands inside the priced simplex.

### MAJOR-8 — the head's price segment omits the word that makes it true

**Where:** `MEASURE-DECLARATION-REQUIRED-<ONE-POINT-OF-A-119-SIMPLEX-…>`.

**What.** The price is one point of the **invariant** simplex. A
declaration is not obliged to be invariant; declare a non-invariant
measure and the price is one point of the 639-simplex on the slice,
not 119 numbers. §6 states the conditional correctly ("after every
symmetry this arena measures has been imposed"), and the head states
it correctly two segments later
(`INVARIANT-MEASURES-ARE-EXACTLY-THE-ORBIT-CONSTANT-ONES`) — but the
head's **first** segment, the one that gets quoted, is bare, and the
number 119 is meaningless without it. A related misreading is invited
by `CHART-128:120-ORBITS`: the orbits are those of the **residual**
group on the slice (order 8: $\langle$ twist$^2$, $X\rangle$), because
the chart group acts *trivially* on the slice — that is the
fixed-locus result. §4.3 says so; the head does not.

**Repair (exact).** `ONE-POINT-OF-THE-INVARIANT-119-SIMPLEX-ON-120-RESIDUAL-GROUP-ORBITS-AT-THE-CHART-128-READING;207-SIMPLEX-ON-208-AT-THE-CHART-32-READING`,
and §4.3's table gains an "acting group" column (order 4:
$\langle$twist$^2\rangle$; order 8: $\langle$twist$^2$, $X\rangle$,
the swap arriving from the point group's total inversion, the one
extension element that reverses every link).

---

## 4. THE MINORS

1. **Receipt vs paper on the census's provenance.** `choice_inventory`
   row 10 reads `DECLARED (the pin's plus two)`; the pin names three
   and the unit runs eight, so it is the pin's plus **five**, as §12
   says. Typed literal at code L2288. *(Repair: "the pin's three plus
   five".)*
2. **The #34 ledger is published in three classes, not four.** §10
   says four; the receipt's `waiver_ledger` carries
   `NO-FALSIFIER-REACHES-IT` 27, `COVERED-BY-A-DECLARED-MUTANT` 23,
   `REGISTERED-FORCING` 6 — 56 total, honest denominator, but the
   fourth class `COVERED-BY-THE-ANCHOR-BREAKER` (L2912) is
   **unreachable**: its three gates are all targeted by declared
   mutants and the earlier branch catches them first. *(Repair: say
   three, delete the dead branch — or re-order so anchor coverage is
   attributed to the breaker. Either way §10 should carry the numbers:
   27 of 56 gates that no falsifier reaches is the honest denominator
   the era asks to be published, and the paper currently names the
   class without its count.)*
3. **`fibre.minimal` carries a typed reading name behind a dead
   conditional.** Code L1927–1928:
   `hi["orbits"] if hi["orbits"] < lo["orbits"] else lo["orbits"]`
   with `hi = max`, `lo = min` — the test can never be true — and
   `"reading": "CHART-128"` is typed rather than derived. The number
   120 is correct and computed; the label is not. *(Repair: derive
   both from `lo`.)*
4. **§3's bolded sentence is unqualified by reading** — subsumed by
   MAJOR-5's repair.
5. **§6 prices two items where the inventory names three
   verdict-determining axes.** "That is the whole of it" omits the
   chart reading, whose fibre changes the simplex from 119 to 207.
   Both numbers *are* printed inside item 2, so nothing is hidden.
   *(Repair: make the list three items — the chart reading, the
   carrier, then the point.)*
6. **The seal manifest is not total by exactly one key**, and the
   exemption is typed: 42 top-level receipt keys = 31 sealed + 10
   declared unsealed + `declared_unsealed` itself, which is excluded
   by `and k != "declared_unsealed"` at L2839 with no disclosure in
   the receipt or the paper, while the paper asserts totality twice
   (§ intro and §10). *(Repair: add `"declared_unsealed"` to its own
   list — a well-founded self-inclusion — and delete the typed
   exemption; the manifest then reads 42 = 31 + 11.)* **→ K3's seat
   owns this; I register it because my prose↔receipt sweep is the row
   that catches it.**

---

## 5. THE MONOMIAL–HAAR RESONANCE WITH PAPER-20: WHAT IS LICENSED NOW

Paper-23 makes **no** cross-unit claim — it never mentions paper-20.
That is the correct call and nothing in the paper needs changing. The
licensure question is entirely about what the **adjudication and the
ledger** may say, and the ledger's current gloss ("two units, same
monomial ⇔ no-quantum-character line") is **not** licensed. Three
reasons, in increasing order of importance:

1. **The biconditional is false at paper-23's own measurement.**
   Monomial $\Rightarrow$ defect-free holds at 128 of 128. The
   converse fails: 256 coins are defect-free and only 128 are
   monomial, so **128 interfering coins carry no defect** at the
   declared probe — which is R5's own
   `DEFECT-STRICTLY-CONTAINED-384-OF-512-ONE-WAY-ONLY`. Any resonance
   sentence must be an arrow, never an equivalence.
2. **The two units' monomials agree in species but not in modality.**
   Both mean permutation-times-phase, hence no cross terms — in
   paper-20 a coefficient map with one nonzero entry, in paper-23 a
   $2\times2$ diagonal-or-antidiagonal coin. But paper-20's is
   **forced**: the offset set admits nothing else, so that arena has
   no interfering sector at that stencil at all. Paper-23's is
   **selected**: 128 of 640, inside a family whose other 512 members
   interfere. "No interference because nothing else is admissible" and
   "no measure trouble exactly where nothing interferes" are different
   facts about different arenas.
3. **The instrument warning is binding.** Paper-20's effectus seat
   measured its 343-map scan **blind** — it returns 18 unitary / 0
   non-monomial on R4b's axis stencil too, where interference
   survives; the conclusion survived only via the repaired 19-value,
   6859-map instrument (link 18/0 against axis 72/54). Any resonance
   sentence must cite the **repaired** instrument or no paper-20
   number at all.

**The sentence I would license, and only in the adjudication and the
ledger:**

> In both arenas the interference-free locus is the monomial one, and
> in paper-23 it is exactly where the substrate hands over a measure
> for free: the 128 monomial coins are the family's unique subgroup,
> so Haar exists there and nowhere else, and they carry 0 of the 384
> defect-carrying coins. The arrow runs one way — monomial $\Rightarrow$
> no defect, with 128 interfering coins defect-free as well — and the
> two units' monomials are the same species under different modality
> (forced by the offset set in paper-20, a proper subset in
> paper-23). No paper-20 count is inherited; paper-20's delivered
> scan was measured blind by its own panel.

---

## 6. THE R5 ANNOTATION QUESTION — MY RULING AND THE REGISTER ROW

**Ruling: R5 needs NO erratum and NO annotation of its numbers, and it
does need a note — for the opposite reason to the paper-12
precedent.**

**Why no erratum.** R5's headline is a **count** over an exhaustively
swept declared window: "the commutator subgroup is non-trivial at
`576 of 640 uniform configurations`," carried in the verdict as
`COMMUTATOR-SUBGROUP=NONTRIVIAL-AT-576-OF-640-UNIFORM-COINS` with
`SWEPT-RANGE=UNIFORM-CONFIGURATIONS-EXHAUSTIVE-OVER-THE-COIN-ALPHABET`.
Counts are measure-free. I swept R5's text for the language that would
convert one into a probability — *most*, *typical*, *generic*,
*probability*, *fraction*, *majority*, *often*, *rare* — and **found
none**: every hit is "at most" or "most transferable." R5 never made
the reading paper-23's table moves. The paper-12 precedent applies
where a terminal claim's **object** was narrower than its natural
reading; here R5's object is exactly what it says it is. Paper-23's
9/10, 9/13, 7/10 are not corrections of R5 — they are what a
*successor* would get if it converted R5's count into a probability
without declaring a measure, which R5 explicitly did not do.

**Why a note is nevertheless owed, and what goes in it.** Paper-23
delivers a **strengthening** of a terminal paper's scope row, and the
corpus has no precedent for recording one. R5's §11 first deviation
discloses the uniform-configuration sweep as "the declared window,"
a restriction with a pinned precedent. Paper-23 measures that the
window is the **chart-fixed locus itself** (655360/655360) — a
derivation, not a declaration. That upgrade belongs on the record, in
a separate note, with the terminal paper untouched, exactly as the
paper-12 precedent handles the reverse case.

**THE REGISTER ROW — for `v14/note-r5-measure-scope-annotation.md`,
written by the orchestrator, R5 untouched:**

> **Row 1 (strengthening).** R5's declared uniform-configuration
> window is not an arbitrary restriction: at the anchored chart
> reading it is exactly the chart-fixed locus, measured configuration
> by configuration at 655360 of 655360 checks (paper-23 §3,
> `G-CHART-FIXED-LOCUS-IS-THE-SWEPT-SLICE`). R5's §11 first deviation
> may be read as a derivation at that reading. **Scope, both ways:**
> under R5's own declared order-128 extension the fixed locus is 32 of
> the 640 (odd-parity cycles force $U = XUX$), and under a chart
> without the direction relabelling it is the 409600 two-coin
> configurations, of which R5's 640 is a proper subset — so the
> upgrade is *chart-declaration-relative*, and the relabelling is what
> carries it.
>
> **Row 2 (standing caution, corpus-wide).** *No count in this corpus
> becomes a probability without a declared measure.* R5's 576 of 640,
> 632 of 640 and 384 of 640 are counts over an exhaustively swept
> window and are untouched. Any successor that reports one as a
> probability inherits paper-23's price: one point of the invariant
> simplex over the carrier's orbits (119 numbers at the extension
> reading, 207 at the anchored one), and **invariance alone constrains
> that probability not at all** — every one of R5's headline sets and
> its complement is a union of orbits, so the admissible mass of each
> ranges over the full $[0,1]$, with the endpoints reached by Gibbs
> measures in the arena's own orbit-constant functionals. The two
> named nulls differ by 27/130; that is the floor of the effect, not
> its size. This is a caution of exactly the shape of the eq-22 note's
> §3: it says which readings are scoped, and it retro-edits nothing.

---

## 7. THE CHOICE INVENTORY AT THE RSQ STANDARD

11 rows; the discipline "a genuinely free choice with fibre 1 is a
contradiction" is respected; the two-number form (fibre *and* declared
instances) is the right form and is better than most units in this
campaign. The three verdict-determining rows, audited hard:

- **`WHICH CHART GROUP IS DECLARED`** — flag correct, **fibre wrong**
  (MAJOR-5), both instances genuinely measured, and this is the axis
  that carries the unit's only positive result. Audited hardest and it
  is where I found the most.
- **`the carrier: uniform slice or full space`** — flag and fibre
  correct. Note the published price is slice-relative and the full
  space's simplex dimension is *not* computed (the joint-group orbit
  count is open); this is disclosed in §9, §11 and §12 and in the head
  (`FULL-SPACE-ORBIT-COUNT-UNDER-THE-JOINT-GROUP=NOT-COMPUTED-BY-COST`).
  Clean.
- **`the null: counting on configurations or on orbits`** — flag and
  fibre (UNBOUNDED) correct, and the UNBOUNDED is not decoration: the
  real axis is *which point of the simplex*, and MAJOR-2 measures what
  that costs. Clean, and under-exploited rather than over-claimed.

**The row I would add to the flagged three:** `the candidate sources
censused`. Its cardinality appears **in the verdict head**
(`8-CANDIDATES`), its fibre is UNBOUNDED, and nothing in the arena
fixes it — which is precisely the paper's own stated criterion ("each
moves a published number and none is fixed by anything this arena
measures"). Flag it, or discharge it by stating the closure principle
of MAJOR-1, which is the better route: a criterion retires the axis in
a way a flag cannot.

**`the sets weighed against the nulls`** (4 instances, "the parent's
own"): I checked the pedigree and it holds — R5 carries the diagonal
sector as "the arena's own abelian arm," §3's per-sector table, not
merely as arena data. But note MAJOR-4: it is the *fourth* set that
wins the head's tie-break against one of the parent's three headline
sets, so this row is closer to verdict-determining than its flag
suggests. Fixing MAJOR-4 dissolves the issue.

---

## 8. THE WELD-2-BLADE-SILENT RULING (OPEN vs INHERITED-CLOSED)

**Correctly left OPEN.** I tried to close it and could not. Weld 2's
kill was structural: a graded class graph is bipartite and cannot
carry its target's odd cycle. The blade needs an odd cycle *in the
target*; at $L = 4$ the target has none (bipartite, 4-regular —
verified). Nothing else in weld 2's kill transfers: the arity blade
does transfer and is sharper here (2 actor objects against 16 sites),
but arity alone was never the kill. The unit's disclosure — that it
measures no *pinned* correspondence and does **not** measure that none
can exist — is the honest form and is the correct call under this
corpus's own standards. Scope it by parity per MAJOR-6 and the ruling
becomes both correct and useful.

---

## 9. THE SUCCESSOR REGISTER

**S-1 — the stationary-measure candidate belongs to a NEW UNIT, and
neither paper-22 nor the R = 4 arena can take it.** I ruled this from
committed material only (I did not read any uncommitted sibling
state). The R4c pin (`v14/note-r4c-pin.md`, committed) scopes
paper-22 to the **two-excitation sector on R4's stage** — statistics,
the defect at two excitations, dispersion composition. That is a
dynamics on the **state** space of a *different* arena, not on R5's
link variables, and the pin binds "NO transport number is inherited."
The R = 4 follow-on (G-FLAT) is a declared **record**, again not a
dynamics on coins. The Γ-iteration layer is a law on **histories**.
Nothing committed supplies a dynamics on configurations, which is why
the candidate is not merely unmeasured but **unownable** at present.

**S-2 — what a derivation would REQUIRE that this arena lacks, named
exactly.** Not "a measure" and not "more symmetry": **transitivity**.
Per MAJOR-1's criterion, a stationary-measure route derives iff its
chain is **irreducible** on the carrier; a covariant chain's
stationary measures are invariant, so it can only ever pick a point of
the *same* 119-simplex, and it fixes that point uniquely exactly when
irreducibility supplies the transitivity the symmetry group does not
(208 / 120 orbits). This is the same property that makes candidate (d)
succeed on 128 coins (a group acts on itself transitively) and
candidate (g) fail on the states (the Born kernel is the identity off
the domino, hence reducible — measured). **The missing object is
therefore precisely a link-variable update rule, and the corpus's
update law (Γ / weld 1) has division counts as its carrier, not
coins** — which is the same gap candidate (a) measures. A unit that
declares one owes: (i) covariance under the declared chart and gauge,
(ii) irreducibility on the declared carrier as a *gate*, not an
assumption, (iii) the honest statement that a reducible chain returns
a simplex, not a measure.

**S-3 — the census closure principle is transferable and should be
engraved, not merely repaired here.** "A canonical measure exists
exactly where something acts transitively" retires the
census-completeness objection for every future derive-or-declare unit
in this programme, and it converts the delimitation question from a
list-audit into a one-line test. It is the most portable thing this
unit produced and it is currently unstated.

**S-4 — the even-$L$ scoping is a live input to the scaling
programme.** The correspondence question at this target is open for
even $L$ and closed by inheritance for odd $L$ (measured). R5's own
refinement is to $L = 8$, so the open case is the one the programme
will meet. A scaling unit that ever declares an odd $L$ inherits a
closed correspondence census for free.

**S-5 — the Born fibre, re-posed more sharply than §11 poses it.**
§11 asks whether a finer substrate-native functional separates
configurations. My measurement narrows it: the collapse is not
3-to-640, it is total — the kernel is the identity off the domino, so
*every* single-link Born functional is blind to all 14 other sites by
construction. A separating functional must be **multi-link**, and the
first place to look is the plaquette, where the parent already
measures 384 defect-carrying coins. Whether a plaquette-grain Born
functional separates within a sector is a cheap, decisive next
measurement.

**S-6 — the maximum-entropy row, if it is entered, should be entered
with its constraint side.** The unconstrained case is settled (it
returns its reference; the references disagree; that is candidate
(b)'s price). The constrained case is candidate (f)'s and needs the
arena to supply a pinned expectation. **It supplies none** — which is
worth stating as a measurement, because "the arena pins no expectation
to condition on" is exactly the sentence a confinement-shaped
follow-on will need before it writes $\langle W\rangle$.

---

## 10. VERDICT

**AWF.** Eight majors, six minors, **zero delivered numbers moved**,
**55 recomputations** (46 re-derivations agreeing to the digit, 9 new
measurements). None of the majors touches the verdict word; MAJOR-2
and MAJOR-6 strengthen the unit, MAJOR-1 and MAJOR-3 sharpen its two
deepest sentences, MAJOR-4, -5, -7 and -8 are scope and precision
repairs that move no measurement. The census's delimitation is
**principled, not outcome-shaped** — and it will read as principled to
a hostile reader only once the closure criterion the unit already
owns is written down. The fibre statement is exactly licensed. The
Born sentence is not, and it is the title. R5 needs no erratum, one
note, and the note records a strengthening rather than a correction —
the first of its kind in this campaign.

**Hashes re-verified at close, all five unchanged** (see §0 table).
This review wrote exactly one file in the repo:
`v14/review-r5m-effectus.md`. Scratch:
`…/scratchpad/r5m-ef/` (`rebuild.py`, `rebuild2.py`, `probe.py`,
`probe2.py`).
