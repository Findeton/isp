# REVIEW — SMU (paper-27), THE OPERATOR LENS (K1)

**Reviewer seat:** K1 OPERATOR, panel protocol v14 ledger #235.
**Object under review, hash-verified at the start of this review and again at
its end:** `v14/paper-27-smu.md` (`d14689919289`), `v14/code/smu_exact.py`
(`394cbfca621c`), `v14/code/smu_output.txt` (`0bf6cc0502e6`),
`v14/code/smu_receipt.json` (`808aca088ff6`), pin `v14/note-smu-pin.md`
(`a1fca5e7b238`), all at commit 6d8582e.
**Method:** every quantity below was rebuilt from the parents' *definitions*
with an independent implementation — own $\mathbb{Q}(\zeta_8)$ carrier
(4-tuples of `Fraction` over $(1,z,z^2,z^3)$, not the delivered integer
5-tuples), own coin enumeration, own lattice/link/plaquette derivation, own
group closures and orbit routine, own iterative Tarjan SCC, own closed-class
test, own exact left-kernel elimination over `Fraction`, own lumpability test.
The delivered instrument was **never** used as an oracle for any value; it was
read only for *declarations* (what was declared), and executed only in a
provisioned off-tree mirror for the two out-of-harness mutants.

## VERDICT: **ACCEPT-WITH-FIXES (AWF)**

Every physics number in this unit reproduced. Nothing I recomputed moved.
Three findings are MAJOR and none of them touches a measured quantity: all
three are claims *about* the measurements — a mislabelled head, a false
universal in the choice inventory, and one published number that is an artifact
of an internal enumeration order. Three MINOR findings follow, one of which
(the full-support edge) is a case where the unit **understates a theorem it in
fact proved**.

**Recomputations: 119**, numbered `[001]`–`[119]` in the scratch transcript,
every one of them a value computed by my own code from the parents'
definitions. In addition: **13 sha256 verifications** (the 5 objects under
review, plus all 8 parent objects at their cited commits bb26ca4 / 987cd73 /
2895a9a — every one matches the digest the paper prints), **5 verbatim-quote
checks** against the parents' and the pin's own bytes (all 5 present and
faithful), a **350-numeral sweep** of the paper, 1 baseline off-tree mirror run
and **2 out-of-harness mutant runs**.

---

## 1. WHAT REPRODUCED (the whole census, independently)

### 1.1 The arena and the parents' objects

| object | parent's / paper's value | my rebuild |
|---|---|---|
| coefficient alphabet | 25 | 25 |
| coin family; sectors | 640 = 64 + 64 + 512 | **identical** |
| unitarity, second route | all | all 640 |
| sites / links / plaquettes | 16 / 32 / 16 | **identical** |
| NON-FLAT / NON-COMMUTING / DEFECT-CARRYING | 632 / 576 / 384 | **identical**, and R5's per-sector split (diag 56 non-flat, 0 non-commuting) reproduces |
| $\Delta^B$ on the Hadamard | half-and-minus-half | **identical** |
| realisable constant twists | the even ones | $\{0,2,4,6\}$ by propagation on the $L=4$ torus |
| residual gauge group order | 4 / 8 | **identical** |
| gauge orbits | 208 / 120 | **identical**, and the size profiles $\{1{:}64,4{:}144\}$ and $\{1{:}8,2{:}28,4{:}24,8{:}60\}$ match paper-23 exactly |
| chart group orders | 32 / 128 | **identical** |
| products staying in the family | 278528 of 409600 | **identical** |
| family closed under inverse | 640 of 640 | **identical** |
| monomial subgroup | 128 | **identical** |

### 1.2 The chart action — the unit's first surprise, confirmed

Measured element by element on my own construction of the two chart groups:

- **32 of 32** anchored chart elements have a constant reversal flag and it is
  `False` everywhere, so **all 32 induce the identity** on the 640 carrier;
  the transition matrix of CHART-32 is literally $I$, giving 640 closed classes
  and a stationary simplex of dimension **639**. Confirmed.
- **64 of 128** extension elements carry a uniform configuration **off** the
  carrier (mixed reversal flag). The 64 that do not split exactly **32 that
  reverse no link / 32 that reverse every link**, precisely as §4.1 states.
- The smallest carrier on which the extension acts, computed as my own
  fixed-point orbit closure from the 640 uniform configurations, is **1248
  states**, and the walk on it has **336 closed classes**. Confirmed.

### 1.3 The census — 18 instances, 12 derive, 6 reducible

All eighteen rows reproduce, class counts and closed-class counts identical,
each chain verified row-stochastic first:

```
CHART-32 640/640 · CHART-128 336/336 · GAUGE-CHART-32 208/208
GAUGE-CHART-128 120/120 · LAW-NATIVE-{012,021,102,120,201,210} 1/1
COMPOSITION-{LEFT,RIGHT} 1/1 · MONOMIAL-{LEFT,RIGHT} 5/5
METROPOLIS-AT-{COUNTING,OU-32,OU-128,NON-INVARIANT} 1/1
```

In every one of the eighteen, #classes = #closed classes — so §3's remark that
the sharp/inherited distinction does not bite on this census is **measured
true** on my rebuild too (zero transient classes anywhere).

### 1.4 The weld, as sets

The gauge walk's closed communicating classes, computed by my Tarjan from the
chain's own support, are **identical as partitions** to the residual-gauge
orbits I built independently from the group action — at both readings, 208 and
120, compared class by class as sets and never by cardinality. The paper's
sharpest structural claim survives an independent rebuild of *both* sides.

### 1.5 The stationary vectors

- Every one of the 12 deriving instances: $\pi P = \pi$ verified **exactly at
  full size** (n = 640) against its own transition law.
- **LAW-NATIVE-012** $=(15/2432,\ 5/1216,\ 13/19456)$ on
  (diagonal, antidiagonal, balanced) — exactly the published triple, and it is
  the $\Gamma$-iteration's own $(15/38,\,5/19,\,13/38)$ (verified against
  `giter_receipt.json` at `targets/law_value_leg1`, both legs) graded by sector
  size. It is invariant under both residual readings, and it is **NEW**
  (equal to none of counting, OU-32, OU-128).
- **COMPOSITION-LEFT/RIGHT**: I verified doubly-stochasticity directly by
  summing all 640 columns exactly (all = 1), which is the identity the
  inverse-closure 640/640 buys; the counting measure is the unique stationary
  vector.
- **10 distinct stationary vectors**, named nulls reached = {COUNTING,
  ORBIT-UNIFORM-CHART-32, ORBIT-UNIFORM-CHART-128}, **NEW = 7**. Confirmed.
- Reducible instances: I solved **every closed class** of GAUGE-32, GAUGE-128,
  MONOMIAL-LEFT and MONOMIAL-RIGHT by my own exact `Fraction` elimination —
  all per-class kernels one-dimensional and class-uniform; class sizes
  $\{1{:}64,4{:}144\}$, $\{1{:}8,2{:}28,4{:}24,8{:}60\}$, $\{128{:}5\}$.

### 1.5b Where the corpus's one canonical measure lands

Both monomial walks split the carrier into 5 classes of 128, and in each walk
**one class is exactly the 128 monomial coins as a set** — paper-23's Haar
carrier, compared element by element and not by cardinality — while the other
four lie **wholly inside the interfering sector**, all 512 balanced coins and
nothing else. §4.5 is confirmed on both sides.

### 1.6 The relativity table and the spreads

My independent §6 table is **character-identical** to the paper's:

| set | count | composition | law-native (012) | OU chart-32 | OU chart-128 |
|---|---|---|---|---|---|
| NON-FLAT | 632 | 79/80 | 289/304 | 25/26 | 23/24 |
| NON-COMMUTING | 576 | 9/10 | 23/38 | 9/13 | 7/10 |
| DEFECT-CARRYING | 384 | 3/5 | 39/152 | 6/13 | 7/15 |
| DIAGONAL | 64 | 1/10 | 15/38 | 4/13 | 3/10 |

- widest spread over the **11** gauge-covariant deriving instances =
  **153/380**, attained on **1 of 4** sets (DEFECT-CARRYING);
- widest over all **12** = **1701/3800**, also on DEFECT-CARRYING;
- the parent's widest over its own invariant measures = **27/130**, attained on
  **2 of 4** sets (NON-COMMUTING, DIAGONAL) — reproducing paper-23's own
  arg-max multiplicity as well as its number.

### 1.7 The Wilson rows

- The four-corner block trace is **plaquette-independent at 16 × 640** checked
  exhaustively; it lies in $\mathbb{Q}(\sqrt2)$ at all 640; it takes exactly
  **11** distinct values; it is **constant on every gauge orbit** at both
  readings.
- The full 16-site trace equals the block trace **+ 12** at all 640 coins —
  which is the "normalisation fibre is 2" claim, and it puts the receipt's
  `full_trace_value` 133/10 against `block_trace_value` 13/10 exactly.
- All **twelve** expectations reproduce exactly:
  13/10 (COMPOSITION-LEFT, COMPOSITION-RIGHT, METROPOLIS-AT-COUNTING),
  19/13, 29/20, 225/152, 111/76, 205/152, 207/152, 107/76, 219/152, 263/200.
- **The [0,4] range**: the observable's orbit values run from 0 to 4 over the
  208 orbits; **both endpoint orbits are singletons**, so the point masses on
  them are invariant measures and are extreme points of the simplex — I built
  both endpoint measures explicitly, verified each is gauge-invariant, and
  recovered $E[W] = 0$ and $E[W] = 4$. The claim that covariance pins the
  expectation nowhere is **exactly right**.

### 1.8 The sharp condition

- The three-state witness: **2 communicating classes, 1 closed, kernel
  dimension 1 (simplex dimension 0)**, $\pi = (0,\tfrac12,\tfrac12)$, verified
  by my own elimination and by $\pi P = \pi$. Not irreducible; derives.
- The delivered exhaustive family (7 support patterns cubed = **343** chains,
  rows uniform on their support): **0 mismatches** between kernel dimension and
  closed-class count, on my elimination.
- **Beyond the delivered window** (the unit did not run these): the same 343
  supports with **non-uniform** rows — 0 mismatches; and the **whole 4-state
  layer**, $15^4 =$ **50,625** chains — **0 mismatches**.

### 1.9 The surjection theorem — the hardest target

- The three real instances: each **covariant** under the residual gauge group
  (checked generator-free, by comparing the whole permuted row set for all 4
  group elements), **irreducible**, **0 detailed-balance failures** over all
  $640^2$ ordered pairs, and stationary measure **equal to the target**.
- The control: 0 detailed-balance failures, **not** gauge-covariant, target
  **not** orbit-constant, lands on its own target. So covariance and not
  dynamics is what confines the answer. Confirmed.
- The declared exhaustive arm rebuilt from scratch (4 states, orbits
  [[0,1],[2],[3]], denominator 12): **55 targets, 0 failures**.
- **My own probes far beyond it**: 1229 invariant targets over 5 carriers
  (n = 3,4,5,6) × 5 denominators × several orbit structures — 0 failures; and
  1206 *arbitrary* full-support targets at n = 3,4,5 — 0 failures.
- **And the probe the unit needed and did not run**: five arbitrary
  full-support **invariant targets on the real 640-state carrier**, built from
  weight rules of my own over the 208 orbits ($k+1$, $1+(k\bmod 7)$,
  $2^{k\bmod 5}$, $1/(k+1)$, $1+(k^2\bmod 11)$). Every one: row-stochastic,
  **1 communicating class**, **1 closed class**, **gauge-covariant**, and
  $\pi$ = the target exactly. The surjection onto paper-23's simplex is
  therefore verified **at the arena**, not only at a 4-state toy. §7's
  headline stands on stronger ground than the unit gave it.

### 1.10 The elimination-cap-208 lumping licence — **exact**

For all 12 deriving instances I tested strong lumpability directly (for every
block, every member's aggregated row must agree): **all 12 lumpable** on their
declared blocks (the 208 gauge orbits; the control's 4 declared blocks); $\pi$
**block-constant** in all 12; the quotient's kernel is one-dimensional in all
12; and the lift (quotient mass spread uniformly inside each block) equals the
full-size $\pi$ **exactly** in all 12. Separately, every closed class the
reducible instances solve directly is at or below the cap (max 128). **The cap
route is exact and the licence is earned.**

---

## 2. FINDINGS

### MAJOR-1 — the head string labels the headline spread with the wrong population

`verdict_head` is

```
SMU-DYNAMICS-RELATIVE-SPREAD-153/380-OVER-12-DERIVING-INSTANCES
```

but 153/380 is the widest spread over the **11 gauge-covariant** deriving
instances. The receipt says so itself — `widest_spread = 153/380` sits beside
`gauge_covariant_deriving_instances = 11`, while
`widest_spread_over_every_deriving_instance = 1701/3800` and
`deriving_instances = 12`. The same verdict string later states both correctly:
`WIDEST-SPREAD-OVER-THE-11-GAUGE-COVARIANT-DERIVING-INSTANCES=153/380 |
OVER-ALL-12-DERIVING-INSTANCES-...=1701/3800`. So the head contradicts its own
body: it asserts that the spread over 12 deriving instances is 153/380 when
this unit measured that number to be 1701/3800.

This is not a rendering slip that a gate could have caught. `head_law` composes
`widest` (the 11-instance figure) with `len(der)` (= 12), and
`second_head_law` — the "independent reconstruction ... written from the same
pre-registered outcomes with a different branch structure" — composes
`str(widest)` with `str(n_der)`. Both carry the identical wrong template, so
the string-equality-against-an-independent-head gate is structurally incapable
of firing on it. §12 shows the authors knew the distinction ("The head carries
the like-for-like one") and the label was simply not moved with it.

**Exact repair.** In `head_law` and `second_head_law`, emit the population the
number was measured over. Minimal form:

```python
# head_law
return ("SMU-DYNAMICS-RELATIVE-SPREAD-%s-OVER-THE-%d-GAUGE-COVARIANT-"
        "DERIVING-INSTANCES" % (widest, n_cov))
# second_head_law
return ("SMU-DYNAMICS-RELATIVE-SPREAD-" + str(widest)
        + "-OVER-THE-" + str(n_cov) + "-GAUGE-COVARIANT-DERIVING-INSTANCES")
```

with `n_cov` taken from the same measured field the spread came from
(`relativity.gauge_covariant_deriving_instances`), never from `len(der)`, and
the paper's fenced verdict block updated to match. **Verified liftable:** I
planted exactly this repair in an off-tree mirror (MUT-K1-A) — see §3.

### MAJOR-2 — "no member of a declared fibre is left unrun" is false at two of the six axes

§10 states, without qualification:

> every declared dynamics axis is DECLARED-AND-SWEPT, with the number of
> instances built equal to the fibre at every one of them, so no member of a
> declared fibre is left unrun

and §1 states "every declared axis is swept to the bottom". The receipt's own
choice inventory refutes both at two rows:

| choice | fibre | instances_built | status |
|---|---|---|---|
| WHICH-INVARIANT-TARGET | `THE-INVARIANT-SIMPLEX-ITSELF` | 3 | DECLARED-AND-SWEPT |
| WHICH-TARGET-THE-CONTROL | `THE-WHOLE-SIMPLEX` | 1 | DECLARED-AND-SWEPT |

The number of instances built is not equal to the fibre at those rows — the
fibre is a 207-dimensional simplex and three points of it were built — and the
why-string "every declared instance of this axis is RUN and its outcome
published" is doing the work of a claim it does not support. §11 then says the
opposite in as many words: "The fibre is now measured to be the whole invariant
simplex."

The substance is fine: the unrun members are covered by the surjection theorem,
which is exhaustive at the declared small carrier (55/55) and which I verified
at 2435 further targets including five on the real 640-carrier. What is wrong
is the universal quantifier and the status stamp.

**Exact repair.** (i) Give the two Metropolis rows their own status —
`DECLARED-AND-THEOREM-COVERED` — with `instances_built: 3` and a
`covered_by: "G-PRICE-IS-CONSERVED"` field, and reserve `DECLARED-AND-SWEPT`
for axes with a finite fibre exhausted by construction. (ii) In §10 replace the
universal with: *"every declared dynamics axis with a finite fibre is
DECLARED-AND-SWEPT, with the number of instances built equal to the fibre; the
two Metropolis axes have the invariant simplex itself as their fibre, three
points of it are built, and the rest is covered by the surjection theorem of
§7, verified exhaustively at a declared small carrier."* (iii) In §1 replace
"because every declared axis is swept to the bottom" with "because every
finite declared axis is swept to the bottom and the two infinite ones are
covered by a theorem".

### MAJOR-3 — one published number is an artifact of the instrument's internal coin enumeration, undisclosed

The declared non-covariant control's target is built on **contiguous blocks of
the coin index**: four blocks `range(0,160) … range(480,640)` carrying masses
1/10, 2/10, 3/10, 4/10. Those blocks are not an arena object; they are an
artifact of the order in which the instrument happens to enumerate the coin
family (rows first, then orthogonal second rows). R5's own declaration of the
family — "the enumeration is exhaustive over the alphabet's fourth power" —
admits at least one other literal reading, the plain product order, which
returns the *same 640 coins as a set* in a different order.

I rebuilt the control under that alternative enumeration and re-measured its two
published numbers:

| published | delivered (rows-first order) | alternative admissible order |
|---|---|---|
| $E[W]$ under the control | **263/200** | **127/100** |
| widest spread over all 12 deriving instances | **1701/3800** | **234/475** |
| widest spread over the 11 covariant instances | 153/380 | 153/380 (unchanged) |

The second of these is carried in the **verdict string**. Nothing in the paper,
the pin or the receipt's published keys discloses that the control target is
index-block-defined, so a reader cannot tell that these two numbers are
enumeration-relative. (The like-for-like headline 153/380 is computed over the
11 gauge-covariant instances only and is **unaffected** — I confirmed it is
identical under both enumerations.)

This does not touch a physics claim: the control exists to show that a
non-invariant target lands outside the simplex, and that verdict
(`ORBIT-CONSTANT=FALSE`, not gauge-covariant) is order-independent. The
like-for-like headline 153/380 excludes the control and is computed from
measures that are functions of sector and orbit membership alone, so it is
enumeration-free by construction. What is wrong is publishing two
order-dependent rationals without the stamp.

**Exact repair.** Either (a) define the control on an arena object rather than
an index range — e.g. mass $\propto$ (1, 2, 3) on the three **sectors**, which
is orbit-refining but not orbit-constant, and is enumeration-free — and
republish 263/200 and 1701/3800 at that target; or, if the declared control is
kept, (b) stamp both numbers, in the Wilson row and in the RELATIVITY segment,
as `CONTROL-TARGET-IS-INDEX-BLOCK-DECLARED-ENUMERATION-RELATIVE`, and add the
control's definition to the receipt as a published (currently `_ctrl_target` is
private, underscore-prefixed and therefore unsealed and unpublished). Option
(a) is the stronger repair and costs one function.

### MINOR-1 — §7 applies the criterion §3 corrected, and thereby understates its own theorem

§3 corrects the inherited law: what decides is the **closed-class count**, not
irreducibility. §7 then bounds the surjection with the superseded form:

> a target with a zero is the stationary measure of a chain irreducible on its
> support and therefore reducible on the carrier, so the reach is onto the
> simplex's interior and onto its boundary only through the reducible arm this
> census already reports

Measured, on my rebuild: a Metropolis chain at a target with zeros has the zero
states **transient** and exactly **one closed class**, so by this unit's own
sharp criterion it **derives**, with the boundary target as its unique
stationary measure.

- small carriers (n = 3,4,5, every zero pattern): **38 boundary targets, 38
  reached exactly, 38 with exactly one closed class, 0 irreducible**;
- the real 640-carrier, with 1, 5 and 100 whole orbits set to mass zero:
  **2 communicating classes, 1 closed class, $\pi$ = the target exactly**, in
  all three.

So the covariant-dynamics fibre surjects onto the **closed** invariant simplex,
every point of it derived — not onto the interior only. Calling the boundary
chains "the reducible arm this census already reports" also conflates two
different things: the census's reducible instances have **many** closed classes
and fix **no** measure, whereas these have one closed class and fix their
target uniquely. The price claim (207 / 119 numbers) is unchanged and if
anything strengthened.

**Exact repair.** Replace the quoted sentence with: *"A target with a zero is
still reached exactly: the Metropolis chain at it has its zeros as transient
states and exactly one closed class, so by the sharp criterion of §3 it derives
and the target is its unique stationary measure. The reach is therefore onto
the closed simplex, boundary included; what the boundary costs is
irreducibility, not derivation."* Add a gate over a declared boundary target
(one line: reuse `metropolis` with a zeroed orbit and assert closed classes = 1
and $\pi$ = target), so the strengthened statement is measured rather than
argued.

### MINOR-2 — the numeral-coverage gate's forgiven list is wider than §10 describes

§10: "The structural literals the coverage gate is permitted to forgive —
section numbers and the engraving references — are published in the receipt".
The published list is
$\{0,1,\dots,27\}\cup\{34,46,62,82,87,91,119,125\}\cup\{a.b\}$. Sections run
1–12; the engraving references used are eight. The integers 0 and 13–27 are
**neither**, and they blanket most of this paper's load-bearing small counts —
6 families, 18 instances, 12 deriving, 6 reducible, 5 monomial classes, 11
distinct observable values, 16 plaquettes, 25 alphabet elements, 2 fibre, 4
corners. A prose numeral moved among any of those would not be caught by this
gate. (The gate's `allowed` set is additionally harvested from *every* numeral
appearing anywhere in any receipt string, the 3490-character verdict included,
which widens it further.) The numbers themselves are all correct — I checked
every one of the paper's 350 numerals against my own rebuild and found no
discrepancy — so this is a gate-strength and disclosure defect, not an error.

**Exact repair.** Narrow `STRUCTURAL` to `{str(k) for k in range(1, 13)}` (the
sections this paper actually has) plus the section-decimal set plus the eight
engraving references, and let the harvested `allowed` set carry the rest; if
any numeral then goes unmatched, that is the gate doing its job. Failing that,
change §10's description to name the band honestly: "section numbers, the
engraving references, **and every integer below 28**".

### MINOR-3 — the dimension-theorem sweep is narrower than "exhaustively on a declared family of small chains" suggests

The delivered sweep is 343 three-state chains whose rows are **uniform on their
support** — one row shape, one carrier size. §3 and §5 lean on it ("verified
exhaustively on small chains") to license every reducible verdict. Widening it
is nearly free: I ran the same 343 supports with **non-uniform** rows (0
mismatches) and the entire **4-state layer**, $15^4 = 50{,}625$ chains
(0 mismatches), in under 4 seconds of `Fraction` arithmetic.

**Exact repair.** Add the 4-state layer to `verify_the_dimension_theorem`
(one extra loop nest, `rowset` generated from `itertools.combinations` rather
than typed) and publish `carrier_states: [3, 4]`,
`chains_enumerated: 50968`. The claim then matches the sweep.

### MINOR-4 — "declaring a dynamics widened rather than narrowed the range" is monotone by construction

§6 presents the comparison 153/380 against the parent's 27/130 as a surprise:
"supplying it did not narrow the answer, it widened the reachable range... the
opposite of what a reader might expect". But the eleven gauge-covariant
deriving instances carry **nine distinct measures**, and paper-23's three
compared measures — counting, orbit-uniform chart-32, orbit-uniform chart-128 —
are **all three among them** (reached by the composition walks and
METROPOLIS-AT-COUNTING, and by the two orbit-uniform Metropolis instances). A
maximum minus a minimum over a superset can only be $\ge$ the same quantity
over the subset, so the *direction* of the comparison is forced by set
inclusion and not measured. Only the *size* is contingent, and it is real:
on DEFECT-CARRYING the parent's own three measures spread 9/65, and the
law-native family pushes the minimum from 6/13 down to 15/76, taking it to
153/380. That is the actual finding and it is a good one.

**Exact repair.** In §6 replace the surprise framing with the inclusion and the
increment: *"The nine distinct measures the covariant deriving instances carry
include all three the parent compared, so this spread is at least the parent's
by inclusion; what is measured is how much further it goes. On
DEFECT-CARRYING the parent's three spread 9/65 and the law-native family takes
the minimum from 6/13 to 15/76, widening it to 153/380."* Publish
`parent_measures_contained_in_this_census: 3 of 3` in the relativity block so
the inclusion is a measurement rather than a reader's inference.

---

## 3. THE TWO OUT-OF-HARNESS MUTANTS

Both were planted in a provisioned off-tree mirror of the instrument and its
nine pinned sources (baseline mirror run: exit 0, verdict byte-identical to the
delivered artifact — so the "correct off-tree, no version control" claim of #91
is confirmed independently).

**MUT-K1-A — the MAJOR-1 repair, applied to both head laws.** Changed
`head_law` and `second_head_law` to emit
`-OVER-%d-GAUGE-COVARIANT-DERIVING-INSTANCES` with the covariant count.
Result: **exit 1, REFUSED at `G-PAPER-VERDICT-EQUALITY`** — "1 fenced blocks;
0 equal to this run's verdict" — and at **no measurement gate whatever**. The
independent-reconstruction gate did *not* fire, because both head laws were
changed identically, which is exactly the shape of the live defect. This is the
diagnostic that matters: it establishes
that nothing *measured* contradicts the repair, and that the wrong label is
held in place only by the paper's own fenced block — so MAJOR-1 is fixed by a
coordinated edit of the two head laws and the paper's verdict block, and by
nothing else.

**MUT-K1-B — an undeclared change to a declared construction.** Changed the
law-native resampling to draw **non-uniformly inside the sector**
(weights $1+(q \bmod 3)$) while leaving the sector law untouched — i.e. a
silent violation of §4.3's "then uniformly inside it" that preserves every
sector mass. Result: **died at exit 1** at
`G-INSTANCE-LAW-NATIVE-012`, reporting `covariance failures 1920 over 4
generators` and `0 verified at full size`. (Both mutants were run through the
`--no-write` twin, so "writes nothing" is not what these two runs test; they
test *which gate* catches the change, which is the question I put to them.)
This is a **credit
to the unit**: the declared construction is bound by a measurement gate — the
per-instance covariance and full-size $\pi P = \pi$ checks — and not merely by
prose, and the per-instance gates of #87 catch a change that leaves every
aggregate count intact.

---

## 4. WHAT I COULD NOT FAULT

- The **weld** (§4.2) is the strongest thing here and it survives a rebuild of
  both sides from definitions: the dynamics layer's decomposition and the
  static layer's orbit census really are one object reached twice.
- The **[0,4] range** (§8) is exactly right and its consequence — "an
  expectation on this arena is not a number the arena has" — is the honest
  reading of a measurement I reproduced endpoint by endpoint, singleton orbits
  included.
- The **conserved-price** sentence (§7) is sound on the measurements, and my
  five arbitrary invariant targets on the real carrier make it stronger than
  the unit's own three declared points did.
- The **lumping licence** is exact, not merely disclosed: lumpable, block-
  constant, one-dimensional quotient kernel, and lift = full-size $\pi$ at all
  twelve.
- **Zero false numerical results.** I swept all 350 numerals of the paper.
  Every one that denotes a measured quantity matched my independent value; the
  remainder are sha256-12 and commit-hash fragments (all 13 digests verified
  above), section and engraving references, and the six LAW-NATIVE permutation
  labels — which are themselves the six members of a fibre I built and ran.

## 5. FOR THE ADJUDICATOR

MAJOR-1 and MAJOR-3 both touch the **verdict string**, so both require a
re-render of the fenced block; MAJOR-2 touches §1, §10 and the receipt's
`fibre.rows`. None of the three requires re-deriving a single measurement.
MINOR-1's repair changes a sentence and adds one gate. My recommendation is
AWF with those seven repairs lifted verbatim, and with the boundary-target probe
and the 640-carrier surjection probe adopted into the instrument, since both
close gaps the unit's own argument depends on and neither costs more than a
few seconds of exact arithmetic.

**Hashes re-verified at the end of this review:** paper `d146899192890b1f`,
code `394cbfca621c78ce`, output `0bf6cc0502e6485b`, receipt `808aca088ff63328`,
pin `a1fca5e7b238513b` — unchanged from the start.
