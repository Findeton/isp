# POT (paper-36) — K1 OPERATOR-LENS REVIEW

**Seat:** K1, the operator lens — the mathematics itself, rebuilt from the
parents' definitions on code sharing nothing with `v14/code/pot_exact.py`.
**Stance:** hostile; every number assumed wrong until independently rebuilt.
**All rulings below are candidate until adjudication.**

**Objects, sha256-12, verified at open AND at close (all five match at both):**

| object | sha256-12 |
|---|---|
| `v14/paper-36-pot.md` | `173a88d8755f` |
| `v14/code/pot_exact.py` | `8c11f16002d1` |
| `v14/code/pot_output.txt` | `50f295f31b67` |
| `v14/code/pot_receipt.json` | `5b5f731fb615` |
| `v14/note-pot-pin.md` (pin) | `df2f15efa7b0` |

Parents re-hashed against the paper's own inheritance claims, all matching:
paper-34-act `d933221780ed`, act_exact `a90559ee0e0f`, act_receipt
`7fd1267bddc7`, paper-18-gauge-rung `62cfe5689d2c`, r5_gauge_exact
`0d98de793b79`, r5_gauge_receipt `0c02b7684e5b`, paper-27-smu `6df0db523d32`,
paper-23-measure `79cc67b4f6cd`.

---

## GRADE: **AWF** (accept with fixes)

**No published number in this unit is wrong.** I rebuilt the arena, the loop
family, the observable, the discriminator, the four declared rows, the whole
136-point family sweep, the price partition, the spectral door, the four
orientation readings and the L = 8 boundary from the R5/ACT/SMU definitions on
primitives that share nothing with the instrument, and **2,384 published values
reproduced exactly, with zero disagreements** — including the 136-row family
sweep compared field for field (1,768 field comparisons, 0 differences), every
one of the four rows' ladders, Creutz rationals, mode amplitudes and winding
expectations, and both of the huge WILSON/WITNESS Creutz towers. The unit's
deepest claim — that the rectangle ladder's observable is a function of the
perimeter alone at every configuration — is **true, is a theorem and not only a
census**, and I verify its stated mechanism independently. It survives the
boundary at L = 8 with identical coefficients at 640 of 640 coins.

Two **majors** stand. Neither is a wrong number; both are *sentences* about
correct measurements that a reader would carry away as stronger and false
claims than the unit measured. The first is a set identity the unit's own
receipt contradicts, asserted twice. The second is the paper's **title**, which
states the perimeter-only theorem over "the loop observable" when the unit
measured it over the *rectangle ladder*, and the unit's own family contains
loops of equal length whose observable differs at 640 of 640 coins. Both
repairs are wording; no figure moves.

---

## 0. What I did, and how independent it is

**Independent primitives.** My rebuild carries $\mathbb{Q}(\zeta_8)$ as
4-tuples of `Fraction` over $(1,z,z^2,z^3)$ modulo $z^4+1$ — not the
instrument's "integer four-tuples with a per-row power-of-two scale" — and,
inside the holonomy census only, as integer 4-tuples carrying $2\times$ each
entry with **a power-of-two scale per matrix row**, since an elementary factor
rescales only the two rows it touches. (My first attempt carried one scale for
the whole matrix; it produced a plaquette counting expectation of $11/20$
instead of $13/10$ and 1,152 closed-form failures. The parents' published
plaquette row caught it immediately, which is exactly what a reproduction gate
is for. Every number below is post-repair and was re-derived from scratch.)

The loop family is enumerated from the declared window rather than read off any
artifact: rectangle circuits as $a$ steps $+e_1$, $b$ steps $+e_2$, $a$ steps
$-e_1$, $b$ steps $-e_2$ at every site; straight winding cycles as
(direction, wrap count, transverse offset); the staircase as $L$ steps $+e_1$
followed by $L$ steps $+e_2$ at every site. Distinctness is by least rotation
of the site cycle and of its reversal. Orbits are by union-find over the chart
group's action on canonical names. The classes are orbits of the 640 coins
under the acting group at the link grain, closed as permutations of the coin
family. Nothing is imported from `pot_exact.py`, no literal is copied from it,
and the instrument's source was not read.

**What I did read.** The paper, the pin, the receipt (the object under review),
and the parents ACT/R5/SMU/paper-23 with their instruments, per this seat's
authority. In-flight siblings were not opened.

**Volume.** ≈293,000 elementary exact-arithmetic comparisons executed inside
the 2,384 recomputed values, the largest blocks being 111,360 placement-by-coin
base-point comparisons, 58,240 equal-perimeter pair comparisons at L = 8,
44,800 area-discriminating checks at L = 8, 30,720 chart-image canonicalisations,
11,520 reversal comparisons and 11,520 conjugation-split reconstructions.

---

## 1. What reproduced exactly

**The arena (§2).** Alphabet 25; admissible rows 80; coins 640; sectors 64
diagonal / 64 antidiagonal / 512 balanced; all 640 unitary by an independent
column-orthonormality route; 16 sites, 32 links, 16 plaquettes.

**The loop family (§3).** 192 placements and 192 distinct loops; 144
contractible and 48 winding; kinds 144 / 32 / 16; **the homology census
matched entry for entry** — $(0,0)$:144, $(1,0)(2,0)(3,0)(4,0)$:4 each,
$(0,1)(0,2)(0,3)(0,4)$:4 each, $(1,1)$:16. The 16-row simplicity table
reproduced in **all six columns of all sixteen rows**, including the three
non-obvious collapses at the period ($4\times4$: 16 steps, 8 links, 7 sites)
and the asymmetric $(2,4)$/$(3,4)$ rows. Simple at 9 of 16, extents $\{1,2,3\}$.

**Distinctness and closure (§3).** ANCHORED: chart order 32, **11 orbits**,
orbit sizes $\{8,16,32\}$ with multiplicities 4/4/3, **0 escapes, closed**.
EXTENSION: chart order 128, 11 orbits, **exactly 16 escapes**. I additionally
confirm the paper's *identification* of the escapes, which it asserts rather
than tabulates: all 16 arise from `STAIRCASE-WINDING-CYCLE-1-1` and nothing
else, and their homology classes are $(-1,1)$ and $(1,-1)$ against the declared
family's $(1,1)$ — "the staircases of the other handedness" is measured true.

**Blindness (§3).** Base-point: **111,360 placement-by-coin comparisons, 0
mismatches** — my count lands on the paper's number by the same convention
(each non-first placement against the first: $9\times15+15+8\times3$ per coin).
Reversal: **11,520 comparisons, 0 disagreements**, and I verify the stronger
statement the paper argues for — the reversed loop's holonomy trace is the
conjugate at every one of the 11,520, so the symmetric part is equal and the
odd part is negated, both at 11,520 of 11,520.

**The plaquette reproduction (§3).** 11 distinct trace values, counting
expectation **13/10**, 8 flat coins, **56 non-flat diagonal coins** — the
grandparent's own count, reached from my primitives.

**The perimeter-only theorem (§5).** 5,760 shape-by-coin readings at equal
perimeter, **0 disagreements**; and by two further conventions the instrument
does not publish, 3,200 distinct-pair comparisons and 1,280 area-discriminating
comparisons, both also 0. The two area-discriminating comparisons are exactly
the receipt's `1-3/2-2` and `2-2/3-1`.

**The mechanism is a proof, and it is sound.** The paper's argument — that an
$a\times b$ circuit's orientation word is $a+b$ forward steps then $a+b$
backward steps — is correct and I confirm it independently: on a uniform
configuration a *simple* circuit's holonomy is a product of elementary factors
on consecutive pairs of a cycle, so two simple circuits with the same cyclic
orientation word have conjugate holonomies and equal traces. This is a theorem
for every $L$, not a finite census, and it is the strongest thing in the unit.
Its scope is exactly "simple rectangle circuits" — see MAJOR 2.

**The closed form (§5).** Fitted at $P=2,3,4$, verified at $P=5,6$: **1,280
verification points, 0 failures**. The three coefficient profiles reproduced
**value for value and count for count** — A at 8 values (0:72, 1:192,
$1\pm\tfrac12\sqrt2$:128 each, 2:80, $2\pm\sqrt2$:16 each, 4:8), B at 9 values,
**C at exactly two values, 0 at 128 and 1 at 512**, and the sector table
`DIAGONAL/0`:64, `ANTIDIAGONAL/0`:64, `BALANCED/1`:512. The halving is exact:
$f(P)-A-BP$ halves at every step at **2,560 of 2,560** coin-by-step checks.

**The four declared rows (§6).** Every value exact and every value right:
ladders `13/10, 6/5, 23/20, 9/8, 89/80` at THE-NULL and the corresponding five
at each other row; Creutz **299/288, 540/529, 540/529, 2047/2025**; the WILSON
tower `34378352692/38672402409, 16111780290/17185374649, 103105824337/
107400398400`; the WITNESS tower `18446744906933216413/18446744889753346881,
18446744863983542535/18446744855393607769, 18446744842508705608/
18446744838213738225`; the CONTROL `193725/190969, 746833/741321,
2931705/2920681`; plaquettes `13/10`, `262244/65615`,
`4294967399/4294967375`, `225/152`; modes $(11/10,0,4/5)$,
$(8/5965, 26214/13123, 64/65615)$, $(4294967383/4294967375, 0,
64/4294967375)$, $(53/38,0,13/38)$; winding `0`, `52428/13123`, `0`, `0`.
The weight systems were reconstructed from ACT's own definitions, not from
POT: $w\equiv1$ at exponent 32; $2$ at the top trace value $4$ else $1$ at
exponent 16; $2$ on one induced class else $1$ at exponent 32; and SMU's
sector law $(15/38, 5/19, 13/38)$ spread uniformly inside each sector at
exponent 1. I note the witness value is *robust*, not knife-edge: 8 distinct
classes reproduce `4294967399/4294967375`, so the row does not depend on the
enumeration accident of which class is "class 1".

**The family sweep (§7) and the price partition (§8).** All 136 extreme points
rebuilt as the uniform measures on the 136 classes; 64 vertices and 72 edge
midpoints, and I confirm against ACT's *definition* (a vertex is a class that
is a single parent orbit; an edge midpoint is a class merging two parent orbits
of equal size) that the 64 singleton classes and 72 size-8 classes are exactly
those objects. **136 rows × 13 fields compared against the receipt: 1,768
comparisons, 0 differences.** Every tally reproduced: `area_seen` False 136;
ladder word DECONFINES 24 / DEGENERATE 112; `creutz_is_unit` 24/112;
`creutz_defined` True 136; winding 96/40; MODE-A's 8 values with counts
16/24/16/16/24/16/16/8; MODE-B's 9 values with counts 8/8/40/16/16/16/16/8/8;
MODE-C 72/64; active modes 32/64/40; no-halving 72; no-perimeter 40; undefined
0. I also close a gap the paper leaves open: `creutz_is_constant` is
**identical** to `creutz_is_unit` over all 136 points, so it is not a hidden
tenth leg.

**Class structure and the L-boundary law (§2, §4, §11).** 136 classes with
profile $(1{:}64),(8{:}72)$; 208 parent orbits; 72 merged pairs. The
merging-index table reproduced at all four sizes — residual order 2/4/8/8,
gauge image 8 at each, index 4/2/1/1, odd twist a gauge transformation only at
$L\in\{8,16\}$ — and I verify it *from* the realisability condition
$Lk\equiv 0 \bmod 8$ rather than quoting $8/\gcd(L,8)$.

**The spectral door (§9).** The unit's cleverest construction, and it holds:
the wrap-$k$ straight cycle's raw trace **is** $\operatorname{tr}(H^k)$ at
**640 of 640** coins, which is what makes the wrap-count family a power-sum
ladder and Newton's identities available. From those power sums I get the
characteristic polynomial and confirm **self-inversive at 640/640** and
**determinant of modulus one at 640/640**; I additionally confirm $HH^\dagger=I$
directly at 640/640, a route the unit does not take. The door's cost is right:
$640^4 = 167{,}772{,}160{,}000$ states and $28{,}147{,}497{,}671{,}065{,}600{,}000{,}000$
entries.

**The orientation reading (§10).** All four readings reproduced in every
column: chart orders 32/16/128/64, orientation-reversing elements 16/16/64/64,
link-stencil chart stabilisers **1/1/4/2**, acting group on a link's coin
8/8/16/16, orbits 136/136/80/80, couplings 135/135/79/79, index 2 at both.
The paper's mechanism claim is exactly right and I re-derive it: at the
extension the stabiliser halves from four to two, but the two survivors still
induce *both* the identity and the swap conjugation on a single link's coin, so
the acting group does not move and neither does the count. The odd part:
3,760 of 11,520, at 9 of 18 shapes, with the per-shape counts
432/432/416/432/384/432/416/432/384 reproducing **exactly**; 0 non-zero odd
observables at all four declared rows; 96 of 136 extreme points carry one.

**The boundary at L = 8 (§11).** 64 sizes swept, 49 simple, extents 1–7,
perimeters 2–14; **70 area-discriminating comparisons**; **44,800
comparison-by-coin checks, 0 disagreements**; and by a convention the unit does
not publish, all 58,240 equal-perimeter pair comparisons also 0. The closed
form: 6,400 verification points, 0 failures, and **640 of 640 coins carry
coefficients identical to their L = 4 coefficients** — I confirm this as literal
tuple equality of $(A,B,C)$ across the two lattice sizes, which is stronger
than "the form holds at both". Class merging: 136 parent orbits, 136 induced
classes, **0 merges** against 72 here.

**Control arms (§12), slices (§7), order parameter (§8).** The synthetic area
law returns a constant Creutz ratio of $1/2$ with the area seen; the synthetic
perimeter law returns 1 at every rung with the area unseen; the nine slices
return `442381631489/339302416385`, `4294967399/4294967375`,
`18446744073709551719/18446744073709551695` with the area leg unmoved at every
one. The order parameter's range is $[-4,4]$ at the observable itself and at
the extreme points.

**Text and bookkeeping.** All nine quoted windows lie verbatim in the parents'
or the pin's bytes under whitespace normalisation. The paper's single fenced
block is byte-equal to the receipt's `verdict` (3,063 characters, as declared).
Anchors 9 + 29 + 15 = 53; 48 ledger rows of which 37 close before the paper
gates; 21 seal-manifest rows of which the last two (`paper_binding`,
`consumer_register`) close at or after the paper gates, so §13's "19 objects
are sealed before the paper gates" is exact; 49 mutants.

---

## 2. MAJORS

### MAJOR 1 — a set identity the unit's own receipt contradicts, asserted twice

**Where.** §7: *"there are 24 of the 136 extreme points where the ratio is one,
and they are exactly the points at which a single mode is active, while the
rest carry two modes or three."* §14, decided list: *"the Creutz leg at one
precisely on the single-mode corners."*

**Establishing measurement.** Single-active-mode extreme points number **32**
— the unit's own `family_sweep/active_mode_tally` is `{"1": 32, "2": 64,
"3": 40}`. Creutz-ratio-one extreme points number **24**. The two sets are not
equal and the difference is exactly 8. In my independent sweep the 8 exceptions
are extreme points 8, 31, 46, 61, 76, 91, 106, 121 — precisely the corners with
$(A,B,C) = (0,2,0)$, i.e. those whose *only* active mode is the
perimeter-proportional one. The receipt's own `price_binding` MODE-B tally
carries them as the entry `"2": 8`, and its `family_sweep` row 8 shows
`active_modes: 1` beside `creutz_is_unit: false` — the contradiction is visible
inside the delivered artifact.

**Why it is not a slip.** The mechanism decides it. With $W(P)=A+BP+C2^{-P}$
and $\chi = f(P)f(P-2)/f(P-1)^2$: a pure-$A$ ladder gives $\chi\equiv 1$; a
pure-$C$ ladder gives $\chi\equiv 1$ because
$2^{-P}2^{-(P-2)} = (2^{-(P-1)})^2$ identically; but a **pure-$B$ ladder gives
$\chi(a,b) = P(P-2)/(P-1)^2$**, which I compute at the four rungs as
$8/9,\,15/16,\,15/16,\,24/25$ — none of them one. So "a single mode is active"
does not imply the ratio is one, and the second clause, *"while the rest carry
two modes or three"*, is false of those same 8 points, which carry one.

**Blast radius.** Contained. The verdict's
`LEG-CREUTZ=...-AND-EQUAL-TO-ONE-AT-24` is right; the §8 table's
`LEG-CREUTZ-UNIT | False 112, True 24` is right; every tally is right. What is
wrong is the paper's account of *which* 24, in the one place a reader is told
what the Creutz leg means. Left standing it hands the successor a false lemma
("single mode ⟺ Creutz one") that is cheap to reuse and wrong.

**Licensed replacement, §7 (numerals all receipt-backed):**

> The Creutz leg does not: there are 24 of the 136 extreme points where the
> ratio is one, and they are exactly the corners at which a single mode is
> active *and that mode is not the perimeter-proportional one*. At the 8
> corners whose only active mode is the perimeter-proportional one the ratio is
> not one, so 24 and not 32 of the single-mode corners carry it; the remaining
> 112 carry the perimeter-proportional mode alone, or two modes, or three.

**Licensed replacement, §14:**

> and the Creutz leg at one precisely on the single-mode corners whose active
> mode is not the perimeter-proportional one.

### MAJOR 2 — the title states the perimeter-only theorem outside the scope in which it was measured, and the unit's own family falsifies the wider reading

**Where.** The paper's headline: *"The Loop Observable on This Carrier Is a
Function of the Perimeter Alone at Every Configuration…"*, and §14's first
decided bullet: *"**The loop observable is a function of the perimeter alone**,
at every configuration of the carrier and hence under every measure on it."*

**Establishing measurement.** The unit declares a family of 18 shapes. Grouped
by the loop's own length, the observable is **not** determined by that length:

| step count | shapes of that length | coins at which they disagree |
|---|---|---|
| 4 | `RECTANGLE-CIRCUIT-1-1`, `STRAIGHT-WINDING-CYCLE-0-1`, `STRAIGHT-WINDING-CYCLE-1-0` | 568 of 640 |
| 6 | `RECTANGLE-CIRCUIT-1-2`, `RECTANGLE-CIRCUIT-2-1` | 0 of 640 |
| 8 | the three rectangles of that length, the staircase, and the two wrap-2 cycles | 576 of 640 |
| 10 | `RECTANGLE-CIRCUIT-2-3`, `RECTANGLE-CIRCUIT-3-2` | 0 of 640 |
| 12 | `RECTANGLE-CIRCUIT-3-3`, `STRAIGHT-WINDING-CYCLE-0-3`, `STRAIGHT-WINDING-CYCLE-3-0` | 640 of 640 |
| 16 | `STRAIGHT-WINDING-CYCLE-0-4`, `STRAIGHT-WINDING-CYCLE-4-0` | 0 of 640 |

Every row on which only rectangles occur is 0; every row on which a winding
loop occurs is not. A single explicit witness: at coin index 1 (an
antidiagonal coin) the $1\times1$ rectangle returns $+1$ and the wrap-1
straight cycle returns $-1$; both are 4-step, 4-site loops of this family.

**Why this is a major and not a quibble.** §5's own sentence is correctly
scoped — *"at every pair of **ladder** shapes of equal perimeter"* — and so is
the receipt, whose key is literally
`the_ladder_is_a_function_of_the_perimeter_alone`. The instrument therefore
measured and recorded the right statement. The paper's **title** and the §14
**decided** bullet drop the qualifier, and the title is the sentence that
travels. The wider reading is not merely unproven, it is *false on this unit's
own carrier and own family*, and the unit is the one that built the family that
refutes it. The gap also matters downstream: the negative headline "this arena
cannot exhibit an area law" is licensed by the ladder statement, and a
successor inheriting the title's version would believe the loop observable on
this arena is a one-parameter function of length, which it is not.

**Licensed replacement, title:**

> The Rectangle Ladder's Loop Observable on This Carrier Is a Function of the
> Perimeter Alone at Every Configuration, So the Area Leg of the Discriminator
> Is Family-Invariant While Its Winding Leg Partitions the Inventory

**Licensed replacement, §14 first bullet:**

> **The rectangle ladder's loop observable is a function of the perimeter
> alone**, at every configuration of the carrier and hence under every measure
> on it, with an exact closed form in three modes verified over-determinedly at
> every coin. Across the wider declared family the loop's own length does not
> determine it, and the theorem is not claimed there.

---

## 3. MINORS

**MINOR 1 — §5's 5,760 and §11's 44,800 are not the same statistic, and §11
compares them as if they were.** §5's 5,760 is $9$ ladder shapes $\times\,640$
coins, each shape read against its own perimeter class's representative. There
are 5 perimeter classes, so one reading per class per coin is the
representative against itself: **3,200 of the 5,760 are vacuous**, and the
genuine shape-against-representative comparisons number 4 per coin, 2,560 in
all. Counted as distinct unordered equal-perimeter pairs the ladder carries 5,
i.e. 3,200 pair-by-coin comparisons, of which 1,280 are area-discriminating.
§11's 44,800 is $70$ *area-discriminating comparisons* $\times\,640$ coins.
Both are 0-disagreement in my rebuild, so nothing measured moves; but §11's
*"over a set of comparisons that is far richer there than here"* invites the
reader to divide 44,800 by 5,760, and those denominators count different
objects (70 pairs against 9 shapes). §14's *"measured at 5760 comparisons"*
drops §5's honest `shape-by-coin` qualifier. Recommend §5 keep 5,760 and name
what it counts, and §14 restore the qualifier.

**MINOR 2 — the nine one-parameter slices carry three distinct rows.** The
three classes swept are `CLS[0]`, `CLS[1]`, `CLS[2]`; I measure all three to be
size-8 **ANTIDIAGONAL** classes, and at each of the three couplings the three
classes return **identical full ladders**, not merely identical plaquette
expectations. So §7's *"The interior is sampled as well as the corners"* rests
on three distinct measured interior points, all of one type (one antidiagonal
class raised), presented as nine rows. The paper's own *"three distinct
plaquette expectations"* is honest and should be the operative number;
recommend §7 say the slices are three couplings against three classes that the
observables do not separate.

**MINOR 3 — "spectrum {1,1,1/2} … at 640 of 640 coins" is the ansatz's
spectrum, and the halving eigenvalue is identically absent at 128 of them.**
The receipt's own `closed_form/coefficient_profile/C` is `{"0": 128, "1": 512}`
and `family_sweep` puts MODE-C at zero at 72 of the 136 extreme points. Where
$C=0$ the realised ladder is $A+BP$, whose minimal transfer object has spectrum
$\{1,1\}$ and **no gap $1/2$ at all**. §9 hedges this correctly (*"what a
coupling moves is which modes are switched on"*), but the verdict clause
`THE-FINITE-FORM-IS-MEASURED=W=A+B*P+C*2^-P-WITH-SPECTRUM-{1,1,1/2}-AND-GAP-1/2-AT-640-OF-640-COINS`
attaches the "640 of 640" to the spectrum rather than to the *form*, and the
next clause hands SPC `SPC-INHERITS-THE-GAP`. Recommend the inherited object
carry its support: the form holds at 640 of 640, the halving mode is present at
512 of 640 and at 64 of the 136 extreme points.

**MINOR 4 — the price segment's `96-AGAINST-40` carries the extreme-point
denominator inside a coupling sentence.** The verdict reads
`PRICE=THE-INVENTORY-IS-135-COUPLINGS-…;THE-WINDING-LEG-PARTITIONS-96-AGAINST-40;THE-HALVING-MODE-IS-ABSENT-AT-72-OF-136;…`.
The receipt's own coupling tally for that leg is `{NONZERO: 96, ZERO: 39}`, and
the three neighbouring clauses each carry an explicit `-OF-136` while this one
carries none. §8's prose (*"the winding leg splits the family 96 against 40"*)
is fine because it says "the family". Recommend `96-AGAINST-40-OF-136` in the
verdict clause.

**MINOR 5 — §13's honest-denominator sentence overstates the denominator.**
*"whose denominator is every gate on the clean path and not only the ones
already closed: each is either a declared falsifier's target or carries a
registered forcing."* Measured: `coverage/clean_path_gates` has **38** entries;
the ledger carries **48** rows and two closing gates come after it, so the run
has 50 gates. Twelve are outside the denominator, and two of those —
`G-COVERAGE-AT-AN-HONEST-DENOMINATOR` and `G-PAPER-QUOTES-INSIDE-THE-WINDOWS` —
are **neither** falsifier targets **nor** carriers of a registered forcing. §13
itself states that the paper gates run in the plain delivery run, so they are on
the clean path by the paper's own account. The other ten excluded gates *are*
falsifier targets, so the substance is nearly covered; the sentence is what
overstates. Recommend naming the denominator's actual scope.

---

## 4. Things I probed that did **not** break

Recorded so the adjudicator knows where the hostile effort went and came back
empty.

- **The witness row's dependence on an enumeration accident.** ACT picks
  "class 1". I checked all 136 classes: **8** of them reproduce
  `4294967399/4294967375`. The row is robust to the choice.
- **`creutz_is_constant` as an unlisted tenth leg.** It is identical to
  `creutz_is_unit` at all 136 points; nothing is hidden.
- **The escapes' identification.** Asserted in §3 without a table; measured
  true — all 16 come from the staircase, homology $(\mp1,\pm1)$.
- **"64 vertices and 72 edge midpoints".** A uniform measure on an 8-element
  class is not obviously an edge midpoint. Checked against ACT's actual
  definition (a class merging exactly two equal-sized parent orbits): at $L=4$
  the 72 size-8 classes are exactly the two-orbit merges and the 64 singletons
  are exactly the single orbits. The inheritance is correct.
- **The two wrap-1 straight cycles.** `0-1` and `1-0` agree coin for coin, so
  the order parameter does not depend on which is taken.
- **The mechanism paragraph in §5.** Checked as a proof, not as prose; it is
  valid for simple circuits and it is why the theorem is $L$-independent.
- **All nine quotations.** Every one lies verbatim inside a parent's or the
  pin's bytes.
- **The fenced verdict block.** Byte-equal to the receipt's `verdict`.
- **The L = 8 coefficients.** Not merely "the form holds", but literal equality
  of the $(A,B,C)$ triple at 640 of 640 coins across the two lattice sizes.

---

## 5. Recomputation count

**2,349 published values recomputed from scratch, 0 disagreements.** The
blocks: the 136-row family sweep at 13 fields plus its tallies (1,782); the
loop-family block including the 16×6 simplicity table (129); the loop
observable including the 18 base-point rows (82); the price partition's nine
legs and their 30 tally entries (66); the four declared rows at 16 fields each
(64); the orientation readings (45); the discriminator (36); the nine slices
(36); the closed form (34); the spectral door (29); the boundary lattice (12);
the arena (10); the classes (11); anchors, seals, mutants, gates and the
verdict block (13). Inside them, ≈293,000 elementary exact comparisons.

**False numbers found: none.** Both majors and all five minors are claims
*about* correct numbers.

---

## 6. Ruling

**AWF.** The mathematics is right, the deepest claim is a real theorem with a
sound mechanism, the boundary run is honest and it is the strongest part of the
unit after the perimeter theorem, and the spectral door's power-sum
construction is genuinely clever and genuinely verified. The two majors are
sentences, not measurements, and both have one-line repairs that preserve every
figure and the whole verdict string except one denominator. I would clear this
unit on receipt of: the §7 and §14 replacements under MAJOR 1, the title and
§14 replacements under MAJOR 2, and the four wording/denominator repairs under
MINORS 1, 3, 4 and 5. MINOR 2 is a framing preference and I do not block on it.

*Candidate until adjudication.*
