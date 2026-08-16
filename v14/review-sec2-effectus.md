# SEC-2 (PAPER-40) — K2 EFFECTUS REVIEW

**Seat:** K2, effectus (meaning, scope, licensure, the choice inventory at
the RSQ standard, the successor register, walls).
**Object, verified at open AND at close:** paper-40-sec2.md `aeeeb6757715` ·
sec2_exact.py `4cb4011cfa05` · sec2_output.txt `57c98674b479` ·
sec2_receipt.json `b66fdfaacc33` · note-sec2-pin.md `bfe5c66be9ec`.
**Authority carried:** the pin (three measurements, the walls, SEAM-CONFINED
per #322); note-sec-adjudication.md `7a82ffe7168a`; HANDOFF §4/§9;
#299-as-extended-at-#348; #119-as-amended; §15; E-24.
**Everything below is a candidate reading until adjudication.**

---

## 0. GRADE

**ACCEPT-WITH-FIXES.**

The measured spine is exact. I rebuilt this unit's arena from the paper's
declared definitions, sharing no code with the instrument, and every
census-level number reproduces: the 49-row completion table entry for entry,
the 16-row gluing census, 132,273 shared sites, 455/9/288/216/72, the four
inventory rows, 36/630/7,140 placements in 1/5/15 arenas, 36-of-36 and
108-of-630, and all 22 values declared-not-read from SEC. **No measured
quantity in this unit is wrong.**

What is wrong is at the reading layer, and eight items of it are MAJOR. Two
published numbers in the §4.2 window table (the declaration fibers 27 and 9)
are typed literals that count index tuples rather than declarations; the
distinct declarations are 24 and 8, at the instrument's own representative
and at all 54 aligned gluings. One structural sentence — "the count leg is
not an axis" — is refuted by the paper's own grid, where the count leg flips
lawfulness at three of the five targets. The §6 wall carries the #322 ruling
unqualified into a paper whose own central arenas break its second clause.
And the head's `IRREDUCIBLE` rests on a declared-laws/named-not-licensed
asymmetry the paper does not establish: of the three criteria measured, only
refinement rests on a corpus law, and that law is empty here.

None of this destroys a headline. All four segments survive re-ruling, three
of them strengthened by being scoped. The repairs are liftable text plus two
computed fibers plus two gates.

---

## 1. RECOMPUTATION LEDGER

Independent rebuild, in scratch, from the paper's declared definitions:
AG(2,3) with links (1,0),(0,1),(1,1); the tripartite parts as the (1,2)
parallel class; the 27 sector pairs by the difference-direction criterion and
again by the three resolvable classes; the gluing family as
C(9,k)·P(9,k); the seam chart as Sym²(Q⁴); my own bitmask
isomorphism search for every graph question. No import of `sec2_exact.py`.

| what | count |
|---|---|
| value-level comparisons against the delivered artifacts | **1,593** |
| of which: the 49-row completion table (lattice/posdef/parity/population) | 196 |
| of which: inventories recomputed for **every one of the 216 lawful groups** | 864 |
| of which: window fibers recomputed at all 54 aligned gluings | 324 |
| of which: the 22 SEC values declared-not-read, each rebuilt from my arena | 22 |
| exhaustive sweeps run | 45,010 gluings × 5 currency predicates; 455 group fates; 216 inventories; 666 detector calls; 7,140 triples orbit-reduced |
| **values found to disagree with the delivered artifacts** | **2** (the typed fibers 27 and 9 — MAJOR-2) |

I additionally git-showed the committed SEC paper at 88e4a834f532 and
confirmed `cfe0825d67b2` — a 23rd binding of the declaration that the unit
itself cannot take (correctly: it must run off-tree and git-less).

Not recomputed, and named as such: the QUOTIENT and LAX fates of the 30-cell
grid (I re-derived the EMBEDDING column from the edge-count identity and
reasoned about the other two from the receipt); the mutant sweep and the seal
layer (K3's seat).

---

## 2. MAJORS

### MAJOR-1 — "The count leg is not an axis" is false, and the paper's own grid says so

**The sentence (§4.2, bolded as the first of three facts):** "**The count leg
is not an axis.**" Carried into §8 as *"the extension window's count leg |
declared, MEASURED DEPENDENT | 2 | M2, and it collapses onto the reading
axis"* and into §8's closing paragraph as *"the count leg collapses onto the
reading axis"*.

**Establishing measurement (the receipt's own `extension_grid`, 30 rows):**

| target | QUOTIENT + POSITIVE | QUOTIENT + NON-NEGATIVE |
|---|---|---|
| ONE-AT-EVERY-SEAM | COUNT-DEAD | **ALIVE** |
| SEAM-MAP | COUNT-DEAD | **ALIVE** |
| FULL-CROSS | COUNT-DEAD | **ALIVE** |

The count leg flips the lawfulness flag at three of the five targets. The
driven crossing is lawful at **11 of the 30 cells**, not at six, and the
NON-NEGATIVE leg is what buys three of them. What is actually measured is
narrower and true: *under QUOTIENT, the POSITIVE leg collapses onto
EMBEDDING* — which is exactly what `G-QUOTIENT-POS-COLLAPSE` compares, and
nothing more.

**Ruling:** the gate is sound; the sentence generalises past it. This also
leaves the window's third relaxation unremarked. The paper gives LAX its
paragraph ("buys the crossing by ceasing to be a test") and gives
NON-NEGATIVE none, though NON-NEGATIVE is the mirror relaxation — it lets the
geometry carry links the record never realises, which is precisely how
declaring *more* cross links than the event realises becomes lawful.

**Exact liftable replacement for the bolded fact:**

> **The count leg collapses only under QUOTIENT, and only at POSITIVE.**
> Requiring every declared cell to carry a positive count under the QUOTIENT
> reading is requiring every declared link to be realised, which with
> containment one way is the EMBEDDING reading; the two agree on liveness at
> every target and die differently when they die, which is paper-19's own
> signature. The other leg is a genuine axis: allowing count zero lets the
> target carry links the record never realises, and that alone makes the
> driven crossing lawful at ONE-AT-EVERY-SEAM, at SEAM-MAP and at FULL-CROSS,
> where the positive leg kills it. Of the window's 30 cells the driven
> crossing is lawful at 11. Exactly one target — ONE-AT-ONE-SEAM — is lawful
> with all three delivered legs intact; every other lawful cell has paid for
> itself by relaxing one.

The last sentence is the paper's real result and it is currently only
implicit. §8's row must be re-classed from `MEASURED DEPENDENT` to
`declared, MEASURED DEPENDENT UNDER QUOTIENT-AT-POSITIVE ONLY`.

### MAJOR-2 — the declaration fibers 27 and 9 are typed, and both are wrong as counts of declarations

**The rows (§4.2, column "declaration fiber"):** ONE-AT-ONE-SEAM 27;
ONE-AT-EVERY-SEAM 9. In source these are literals in `WINDOW_TARGETS`
(`("ONE-AT-ONE-SEAM", cross_at(0, {(2, 2)}), 27, …)`), never computed. The
column is load-bearing: §6's wall reads *"Every target in the window carries
its declaration fiber in the row that reports it, and every lawful cell is
lawful AT a declaration."*

**Establishing measurement (my stage 2/3, at the instrument's own
representative `(((0,0),(0,0)),((1,2),(1,2)),((2,1),(2,1)))` and at all 54
aligned gluings, identical at every one):**

| row | published fiber | distinct declarations |
|---|---|---|
| ONE-AT-ONE-SEAM | 27 | **24** |
| ONE-AT-EVERY-SEAM | 9 | **8** |
| SEAM-MAP | 6 | 6 ✓ |
| FULL-CROSS | 1 | 1 ✓ |

27 counts (seam, i, j) index tuples; three pairs of them name the same cross
link, so the target set has 24 members. 9 counts (i, j) label pairs applied
uniformly at all three seams; two of them give the same three-link set, so
there are 8 targets. (The uniformity restriction is itself unnamed: allowing
a different direction at each seam gives 725 distinct targets, not 9.)

**Two further consequences of the same construction, both unnamed:**

1. The window can declare only **24 of the 36 cross links** — `cross_at`
   takes forward directions only, and `FULL-CROSS` is described as "every
   forward cross direction at every shared site" in the code but is named
   FULL-CROSS in the paper, where "forward" occurs exactly once, in §3.3, and
   in the *opposite* argument: *"the only convention-free reading, since a
   chart's neighbour x + a and its neighbour x − a are both declared."*
   M1 insists both signs are declared; M2's targets use one.
2. Three numbers now stand for one choice: **27** (§4.2's fiber), **24** (the
   declarable cross links), **36** (§4.4's placements and §8's inventory
   fiber). The paper reconciles none of them.

**Repair:** compute the fibers in-run and gate them (a fiber that is a typed
literal is exactly the "counts computed, never typed" prohibition); publish
24 and 8; either rename FULL-CROSS to FULL-FORWARD-CROSS or declare the
forward restriction in §2.2 with one sentence saying why M1's two-sided
argument does not bind M2's targets; and add a clause to §4.4 reading *"the
36 placements are every A-private/B-private pair; 24 of them are declarable
by a target of this window, and all 36 lie in one orbit, so the restriction
moves no verdict."* (That last clause is measured — see §3 Confirmations.)

### MAJOR-3 — the SEAM-CONFINED wall is carried unqualified into a paper whose own arenas break its second clause

**The wall (§6):** *"**The adjudication's ruling is carried.** The union
changes geometry only on links both sectors jointly own; nothing here says
otherwise…"* The ruling it quotes (anchor N-ADJ-SEAM) ends *"…no
sector-private link ever moves."*

**Establishing measurement (mine, stage 2 S22/S23):**

| arena | pairs with count ≠ 1 touching an unshared actor |
|---|---|
| the delivered union, every gluing | **0** ✓ |
| SHARED-SEEDED, driven | **2** — `{A(0,1), S0}` and `{B(0,1), S0}` |
| B-SEEDED-PURE, driven | **1** — `{B(0,1), B(0,2)}`, both endpoints unshared, wholly inside one sector |

The driven events of §4.3 — the two arenas the whole M2 price rests on — put
count 2 on links that are not jointly owned. This does **not** contradict
SEC: SEC's ruling was measured on the 45,010 plain gluings, and there it
holds exactly. It contradicts the paper's own sentence "nothing here says
otherwise".

**Ruling:** the wall is sound and the paper's compliance is real; the
sentence's universe is missing. `G-WALL-SEAMCONFINED` cannot catch this — it
checks that the string "SEAM-CONFINED" occurs and the struck leak wording
does not, which is a text test, not a scope test.

**Exact liftable replacement (§6, second wall):**

> **The adjudication's ruling is carried, at its own universe.** In the
> delivered union — every one of the 45,010 gluings, with no declared cross
> link and no added event — the union changes geometry only on links both
> sectors jointly own, and no sector-private link ever moves; this unit
> re-measures it and finds zero exceptions. The extension arenas of section 4
> are not in that universe and are not offered as counterexamples to it: a
> division event that crosses the seam necessarily doubles links that touch
> an unshared actor — two of them at the shared-seeded crossing, one of them
> wholly inside a sector at the B-seeded one — and that is the mechanism the
> price of section 4.3 measures. The ruling is about what gluing does; those
> two numbers are about what an added event does.

This is not merely a caveat: written this way, the wall and §4.3's price
become one statement, which is the paper's best sentence and it is currently
unwritten.

### MAJOR-4 — `SEAM-DECLARATION-IRREDUCIBLE`: the relativization is right and its ground is not established

**The head:** `SEC2-SEAM-DECLARATION-IRREDUCIBLE-[…] -- POSITIVITY SELECTS
NOTHING; … -- THE ONE PRINCIPLE THAT DOES SELECT, MAXIMUM DETERMINANT, IS
NAMED AND NOT LICENSED`. **The body (§3.4):** *"the freedom is irreducible
relative to the declared laws"*.

The relativizing phrase occurs **only in §3.4**; the head's own word is bare.
The head's closing clause does relativize *in effect* (it names the principle
that breaks the result), and I rule that sufficient for the head — this is
the honest construction and it should be praised, not moved.

What is **not** established is the asymmetry the phrase asserts. Take the
three criteria in turn:

| criterion | is it a law of this corpus? |
|---|---|
| positivity | not declared anywhere as a selection principle; the paper's own ground for it is *"the criterion SEC's own segment leaned on"*, and at 13 of 49 seam types it is implied by admissibility, i.e. carries no information |
| price minimisation | the corpus declares that geometry **costs** counts; it nowhere declares that anything **minimises** that cost. Minimisation is exactly as un-licensed as maximum determinant |
| refinement stability | the only one resting on a corpus law (paper-04's ceiling, via LOR) — **and that law is empty here** (min count 1, ceiling 0), so what is measured is a hypothetical the paper stamps as one |

So the true partition is not licensed/unlicensed. It is: *the pin named three
criteria; the paper measured them; a fourth extremal principle, not in the
pin's list, selects uniquely.* Nothing in the corpus licenses any of the four
as a selection law.

**Exact liftable replacement (§3.4, keeping the verdict word):**

> So **the freedom is irreducible at every criterion the pin named**:
> `SEAM-DECLARATION-IRREDUCIBLE`. The word is relative and this paper says to
> what. Positivity selects nothing and at 13 of the 49 seam types carries no
> information at all; the convention-free price is flat, and the one-sided
> price is a sign convention; refinement is the only one of the three resting
> on a law of this corpus — paper-04's ceiling, carried in LOR's own bytes —
> and that law is empty at this record, so its verdict is a hypothetical and
> is labelled one. It should be said plainly that the corpus declares none of
> the three as a selection principle either: what is measured is that the
> pin's criteria do not narrow the seam, not that nothing does. One extremal
> principle that would, and that no unit here has declared, is the maximum
> determinant: by Fischer's inequality it returns the direct sum, uniquely,
> at all 49 seam types. It is named and not adopted; a unit that adopted it
> would be making a declaration, not reporting a measurement.

### MAJOR-5 — `MOTIVATED AT 0 OF 216`: the modal content is licensed, but it is a theorem the paper proves nowhere and measures at two objects

**The head:** `MOTIVATED AT 0 OF 216`. **The body (§4.5):** *"And not one of
the 216 is MOTIVATED. Gluing can be an event in this theory, at a target that
declares the seam it crosses; what it cannot be is a free one."*

**What the instrument measures:** inventories at the two lawful *orbit
representatives* and at the four named arenas. The extension to 216 objects
rests on the inventory being an orbit invariant — true (conjugation by an
automorphism is a bijection of the map set), but **ungated**:
`G-GROUP-CENSUS`'s invariance leg compares only the effect profile
(crossings, within, doublings) at two members per orbit, never the fate and
never the inventory. Under #87 (gates bind objects, not aggregates) a
per-object claim over 216 objects is discharged at two of them with the
forcing unstated.

**Establishing measurement (mine, object by object):** I computed the
inventory for **all 216** lawful groups. Result:

| profile (crossings, doublings) | I-SITE / I-LABEL / I-ORIENT | free items | groups |
|---|---|---|---|
| (2, 1) | 1 / 3 / 2 | 2 | 108 |
| (1, 2) | 3 / 9 / 4 | 3 | 108 |
| **MOTIVATED** | | | **0** |

The claim stands at object level. It is also **forced**, by an argument the
paper has all the pieces of and never assembles: a conflict group has three
actors, hence three pairs; at most two of them can join the sectors (three
vertices cannot be pairwise cross-sector); a group is lawful at the matched
target only if it opens no within-sector pair; so a lawful group has at least
one doubling — and the free items are exactly what the doublings buy
(`G-INVENTORY` gates `free_items == 0 ⟺ doubled_pairs == 0`, and my 216 rows
confirm it at every object). Never-motivated is therefore not a census
outcome that might have gone the other way at some unexamined group; it is
arithmetic.

**Repair, three parts:** (i) state the counting theorem in §4.3 where the
mechanism paragraph already sits; (ii) add an orbit-invariance leg to
`G-GROUP-CENSUS` that recomputes fate *and* inventory at a second member of
every orbit, so the 216 is bound per object; (iii) re-word §4.5's modal
sentence:

> And not one of the 216 is MOTIVATED — not as a tally that came out that
> way, but because it cannot come out otherwise. Three actors give three
> pairs, at most two of which can join the sectors, so a group that opens no
> pair inside a sector must double at least one link the union already
> carries; and the free items are exactly what a doubling buys. Gluing can be
> an event in this theory, at a target that declares the seam it crosses;
> what it cannot be, at this conflict-group size, is a free one.

The clause **"at this conflict-group size"** is the load-bearing scope: the
theorem is about three-actor groups, which §8 lists as `forced, 1, d66's
committed conflict-group size`. It is the one place the result could move.

**On the ledger's gloss "the motivated crossing exists as a relation and is
unreachable as an event"** (relayed at #350; it does not occur in the paper —
verified by scan): the first half is a *constructed control object*, stamped
NOT DRIVEN, and the paper is right to stamp it. The second half is licensed
only with two scopes. Licensed form, if it is ever put in a paper:

> The relation that carries one extra cross-sector pair and nothing else
> welds with zero free items; no single division event at the committed
> three-actor conflict-group size can produce it from the delivered relation,
> because every such event deposits three incidences and at most two of them
> can cross. It is a point of the relation space that this arena's one-step
> dynamics does not reach.

"Unreachable as an event" without "single", without "three-actor", and
without "from the delivered relation" is not licensed by anything here.

### MAJOR-6 — the gauge sentence, and the record-fitted objection's unanswered half

**The head:** `SO THE PLACEMENT OF A SINGLE CROSS LINK IS A GAUGE AND NOT A
DATUM, AND THE RECORD-FITTED OBJECTION DOES NOT BITE AT ONE CROSSING BECAUSE
EVERY PLACEMENT GIVES THE SAME ARENA`.

**What is measured (reproduced exactly):** 36 placements, 1 orbit under the
union's own automorphism group, 36 of 36 admitted by the detector; at two
crossings, 630 placements in 5 orbits of sizes {72, 72, 108, 162, 216}, 108
admitted, and the admitted set is exactly the orbit of the record's own
placement.

**Ruling on "gauge":** licensed, at three scopes it must carry — *at one
crossing*, *at this arena*, and *for this test*. The word is doing exactly
one job here: two declarations differing only in placement give arenas
related by an automorphism of the union, and the detector cannot separate
them. It imports nothing else — no group acting on a state space, no
redundancy of description in the corpus's sense — and the paper is entitled
to it only because it publishes the sightedness contrast beside it. §8's row
already says `MEASURED INERT AT ONE CROSSING`, which is the right word; the
head says `GAUGE`, which is the borrowed one.

**The unanswered half.** §4.4: *"A target extension that carries exactly the
links the record realises looks like a target fitted to its record. At one
crossing it cannot be: every placement gives the same arena, so there is
nothing to fit."* That answers **where**. It does not answer **how many**:
the target declares one cross link because the event realised one crossing,
and that is the definition of "matched". The cardinality half of the
objection is never disarmed, at one crossing or at two.

**A measured fact that sharpens the paper in its own favour and is not
stated:** at one crossing the target does **not** need to declare the link
the record realises — all 36 single-link targets admit the shared-seeded
event, including the 35 that declare a different link. So at r = 1 the head's
"once the target declares the cross links the event realises" is *stronger
than the measurement requires*; at r = 2 it is exactly right up to the orbit
(108 of 630). Licensed replacement for the fourth segment's tail and §4.4's
last paragraph:

> The placement of a declared cross link is INERT at one crossing and a datum
> at two: at one crossing all 36 placements lie in a single orbit of the
> union's own automorphism group and the detector admits the event at every
> one of them — the target need not even declare the link the record
> realises. At two crossings the 630 placements fall into five orbits and
> exactly 108 admit, which is the orbit the record's own placement lies in.
> So the record-fitted objection is disarmed in its placement half, at one
> crossing, at this arena. Its other half is not disarmed and is not claimed
> to be: the target declares as many cross links as the event realises,
> because that is what "matched" means.

### MAJOR-7 — "FIVE CURRENCIES … ZERO VIOLATIONS" over 45,010: four are measured there, the fifth is not measured there at all

**The head:** `SEC2-COMPOSITE-PRICE-SPLITS-[FIVE CURRENCIES ON ALL 45010
COMPOSITES AGAINST THE LONE SECTOR, ZERO VIOLATIONS: …]`.

**Establishing reading of the source.** In the per-gluing loop the
declaration currency is `p_decl = 4 * k` and its check is `… and p_decl ==
4 * k` — an identity. Four currencies (record, budget, carriers, links) are
derived from the relation and genuinely tested at every gluing; I reproduced
all four at all 45,010 with zero violations. The fifth contributes nothing to
that denominator. Its real ground is elsewhere and is sound but singular: the
seam system's kernel is 4 by the chart alone (rank 6 on 10, RHS-independent —
a theorem, so generic across seam types), an unshared site's system is rank 3
on 3 (price 0, likewise generic), and `G-SEAM-CONFINED-PRICE` then evaluates
`4 × k` **at one arena** (k = 3 aligned, giving 12) against SEC's declared
12.

The additivity across seams is exactly what §12's S-3 registers as **open**
("whether two seams of one union constrain each other, and whether the 4k is
ever less than the sum of its seams, is not run"). The head asserts as
measured over 45,010 what the successor register declares unrun.

**Repair (head bracket and §5):** split the claim.

> FOUR CURRENCIES MEASURED ON ALL 45,010 COMPOSITES, ZERO VIOLATIONS: RECORD
> 54 = 27 + 27 IGNORES COMPOSITION; CARRIERS 18 − k AND LINKS 54 − d FAVOUR
> IT; THE GEOMETRY'S BUDGET 54 + 2d PENALIZES IT — AND THE DECLARATION PRICE
> IS A CHART-LEVEL LAW, FOUR NUMBERS AT EVERY SEAM BY THE RANK THEOREM AND
> ZERO AT EVERY UNSHARED SITE, SUMMED TO 4k AT ONE ARENA AND WITH THE
> ADDITIVITY ACROSS SEAMS REGISTERED OPEN

And in §5, one sentence: *"the 4k is four per seam by the rank theorem, times
the number of seams; whether two seams of one union constrain each other is
S-3 and is not run here."*

**A second, sharper reading-level point in the same table.** The declaration
price counts **continuous parameters** (kernel dimension 4). M1's headline
counts **lattice points** (31 admissible completions at the all-simple seam)
under the declared cross-direction admissibility reading. These are freedoms
of two different objects, and §8's inventory row puts them in one cell — *"the
completion of the seam's four entries | declared, MEASURED IRREDUCIBLE | 31
at the all-simple seam"*. Repair: say once, in §3.2 or §5, that the seam's
freedom is 4-dimensional at the affine reading and 31-valued at the quantised
one, and that the price currency counts the former.

### MAJOR-8 — the non-conservative finding is read as dynamics; the measurement is reading-relative bookkeeping

**The sentence (§4.2):** *"And the extension is not conservative… At that
one-link target the union WITHOUT the crossing is STRUCT-DEAD: the geometry
now carries a link no division event realises, and the record that never
crosses no longer welds onto it. **A declared cross link is a demand rather
than an option — the target that can host a crossing cannot host the process
that declines to make one.**"*

**Establishing measurement (the paper's own grid, ONE-AT-ONE-SEAM row
block):** baseline STRUCT-DEAD under EMBEDDING (both legs), COUNT-DEAD under
QUOTIENT+POSITIVE, **ALIVE under QUOTIENT+NON-NEGATIVE**, STRUCT-DEAD under
LAX. So the non-conservativeness holds at five of six cells and fails at the
sixth — and the mechanism at the five is an edge-count mismatch (55 declared
edges against 54 realised), i.e. bookkeeping relative to a target, not a
force on a process.

**Ruling:** "demand", "host", "the process that declines" are the only
sentences in this paper where an extension is given agency. They must go. The
finding itself is real, interesting, and worth the emphasis — it is the
statement that a matched extension is not a conservative extension of the
delivered dictionary.

**Exact liftable replacement:**

> And the extension is not conservative, which the same table says in its own
> baseline column. At the one-link target, under the delivered legs, the
> union WITHOUT the crossing is STRUCT-DEAD: the geometry carries a link no
> division event realises, and the record that never crosses no longer welds
> onto it. This is bookkeeping against a target, not a force on a process —
> the record has 54 realised pairs against 55 declared cells — and it is
> reading-relative: allow count zero and the same record welds again
> (QUOTIENT at NON-NEGATIVE, ALIVE). What the row licenses is this much and
> no more: a target extended to host a crossing is not an extension of the
> delivered dictionary that leaves the un-crossed record where it was.

---

## 3. MINORS

- **m-1.** §2.1's declared-not-read table has no header row, so in rendered
  Markdown the first of the four declared objects (`v14/paper-32-sec.md`,
  `cfe0825d67b2` — the most important one) becomes the table header. Add a
  header row `| status | path | sha256-12 |`.
- **m-2.** §4.5: *"no cross-link declaration repairs a lattice that has lost a
  link of its own."* The lattice has lost nothing; the **record** has gained a
  pair the lattice does not carry. Re-word: *"…a target that lacks a link the
  record realises."*
- **m-3.** §3.5's two sharpening sentences ("it lies outside the admissible
  lattice"; "the completion SEC declared is the one completion the measured
  crossing forbids") do not restate the declared reading they depend on. Both
  are true only under §3.2's cross-direction admissibility reading. Add "under
  the reading of §3.2" to each — they are the two sentences most likely to be
  quoted alone, and one of them already has been (#350).
- **m-4.** §5's SMU quotation stops mid-sentence and the paper's own words
  complete it with no marker. The paraphrase is faithful (SMU's own head reads
  "EXACTLY THE PARENTS COUNTS"), so this is typography, not fidelity: close
  the quote or mark the continuation.
- **m-5.** §4.2: *"makes every one of the 36 possible crossings lawful too"* is
  not a measured row — the grid runs one relation. It is forced (LAX asks the
  target's incidence to sit inside the realised relation, and adding pairs
  preserves containment), so mark it derived-in-text with that one-line
  forcing per the #20 addendum.
- **m-6.** The five verdict words are derived from each currency's own excess
  in the receipt, but the paper never defines them. One clause in §5: *"a
  currency FAVOURS composition when the composite costs less than the two
  sectors, PENALIZES when more, IGNORES when equal; the words are the pin's
  and carry no preference of the theory's."* With that, the anthropic verbs
  are licensed shorthand — every occurrence in the head already carries its
  exact law beside it, which is what makes them safe.
- **m-7.** §4.4: *"The detector's count and the orbit's size agree without
  being compared into agreement — they are computed by different machinery."*
  Two different computations, yes, but both consume the same automorphism
  enumeration primitive. Soften to "by different routes".
- **m-8.** §4.2's *"Declaring one at every shared site does not"* needs its
  reading named (it is lawful at QUOTIENT+NON-NEGATIVE) — this is MAJOR-1's
  tail, listed here because the fix is local.
- **m-9 (pin ownership).** The pin says *"Outcomes with corpus-argued
  feasibility (#299/#319)"* — it **orders** feasibility rather than supplying
  it. #299 as engraved requires the feasibility line **in the pin**. The pin
  is the adjudicator's; the paper discharges the duty anyway at all four
  segments (see §5 below), so nothing is owed by the unit.

---

## 4. THE SEC INHERITANCE, AND THE RULING THE MANDATE ASKS FOR

**Declared-not-read: honestly stamped.** §2.1 states it, names the commit,
publishes all four digests, and the receipt carries `cited_not_read` with
`values_declared: 22`. The reason given is correct and not a convenience: a
run that must byte-reproduce off-tree and git-less cannot read a committed
object. All 22 reproduce; I rebuilt every one of them from my own arena
(45,010 / 16 / 4,186 / 1·81·2,592·42,336 / 1,134 / 2,970 / 54 / 18 / 1,296 /
62,208 / 15 / 12 / 6 / 4 / 10 / 1 / 1 / 2 / 2) and add the committed paper's
own sha as a 23rd.

**The two sharpenings — errata or findings-about-declarations?** I read SEC's
committed §6.1–§6.3 at 88e4a834f532 (`cfe0825d67b2`). **Both are SEC-2
findings about SEC's declarations. Neither is a SEC erratum. SEC's repair
worker should take no correction from this unit.** Grounds:

1. *The indefinite witness.* SEC wrote: *"at every seam an exact rational
   completion is exhibited which reproduces all six measured counts and is
   NEGATIVE on an exhibited rational vector"*, followed by *"The indefinite
   completion is NAMED AND NOT READ"*. SEC's universe is the **affine**
   family. SEC-2 reproduces the witness exactly (value −2, all six counts) and
   then adds a reading SEC never made — I7's readout carried to every
   direction of the chart — under which the witness assigns count 0 to four
   cross directions. Nothing SEC wrote becomes false. SEC's wall is untouched.
2. *The driven crossing excludes the direct sum.* SEC already carried the
   mechanism: §6.2 ("a co-division pair joining an A-neighbour of the shared
   site to a B-neighbour… its count is one linear equation on one cross
   entry") with the rank/kernel table 0→4, 1→3, 2→2, 3→1, 4→0, which SEC-2
   reproduces. SEC-2 adds that the *particular* crossing the grammar drives
   forces Σ = 1 on the extended block, which excludes the direct sum from the
   admissible lattice (31 → 8). SEC's direct sum was already stamped *"a
   declaration, not a measurement"*, and SEC's own two-sided boxed sentence is
   self-scoped — *"At this arena and this target"* — so SEC-2's change of
   target does not contradict it either.

**What SEC's repair may optionally carry** (not owed): one cross-reference in
its S-3 successor row, which asked the seam's four entries as a physical
question and is now partly answered from outside.

**What SEC-2 must not say:** neither sharpening may be worded as a correction
of SEC. §3.5's current wording ("Rebuilt here from its declared entries…";
"The completion SEC declared is the one completion the measured crossing
forbids") is close to the line and is fixed by m-3's scope clause.

---

## 5. THE FOUR SEGMENTS, RULED

| segment | derived? | multi-way selector? | ruling |
|---|---|---|---|
| 1 `SEAM-DECLARATION-IRREDUCIBLE` | yes — the word is chosen by three measured criteria, each of which **could** have selected | **yes, demonstrably**: max-det DOES select uniquely at 49/49, and refinement selects at the 49th seam type, so the machinery visibly returns "selects" when a criterion selects | **licensed after MAJOR-4's re-wording**; the head's max-det clause is the honest construction and must stay |
| 2 `GLUING-EVENT-LAWFUL-AT-THE-MATCHED-CROSS-LINK-EXTENSION` | yes — the word is derived from `n_lawful > 0` and the pin pre-registered the wall alternative | **yes**: at the delivered target all 288 are dead, i.e. the UNLAWFUL outcome is what the delivered legs actually give; the alternative is reached, not hypothetical | **licensed, with MAJOR-1's 11-of-30 clause and MAJOR-5's theorem added** |
| 3 `COMPOSITE-PRICE-SPLITS` | yes — each verdict word derived from its own excess | **yes, three-way**: all three of the pin's words are realised at once, by different currencies | **licensed for four currencies; the fifth re-scoped per MAJOR-7** |
| 4 `BLIND-AT-ONE-SIGHTED-AT-TWO` | yes | **yes**: both outcomes occur inside one census, at r = 1 and r = 2 | **licensed with MAJOR-6's three scopes**; note this segment is **not** one of the pin's three measurements — it is an unpinned finding, and it should say so |

**Feasibility at the row lists (#299 as extended at #348).** The extension is
discharged at all four segments: segment 1's alternative is exhibited
(max-det, refinement at the 49th); segment 2's alternative is the measured
state of the delivered target; segment 3 realises all three words at once;
segment 4 realises both words in one census. The pin supplied no feasibility
line (m-9, pin-owned); the paper supplies the substance at every segment.

---

## 6. THE CHOICE INVENTORY AT THE RSQ STANDARD

Fifteen rows, three of them stamped inert-or-dependent. The classifications
are honest and the "motivated ⟺ zero free items" standard is applied
correctly at the four inventory arenas. Three defects:

1. **A missing row, and it is verdict-bearing.** There is no item for *the
   union arena of the extension census* — one of the 12 arenas, chosen. §10's
   deviation 2 prices it, but the inventory does not carry it, and the row
   that comes closest — *"the gluing, and k | declared, the axis | 45010 |
   every member enumerated"* — is true for M1 and M3 and **false for M2 and
   M4**, which enumerate one. Add:
   `| the union arena of the extension census | declared | 12 (1 run) | M2 and M4 entire; the seam census and the price laws are exhaustive over all 45,010 |`
   and re-bind the existing row to "M1, M3".
2. **The count-leg row is over-classed** (MAJOR-1): `MEASURED DEPENDENT`
   holds only under QUOTIENT at POSITIVE.
3. **The placement row's fiber (36) contradicts §4.2's fiber (27) and the
   measured 24** (MAJOR-2).

Two further items worth adding as declared-and-named, both currently only in
§10: *which two of SEC's three specifications are re-run as arena objects*
(fiber 3, 2 admitted), and *the crossing-alone control* (declared, stamped
NOT DRIVEN, correctly).

---

## 7. THE SUCCESSOR REGISTER

Well-built and correctly stamped "registered, not claimed". S-1 (which
crossings the grammar admits) is the right first successor and names exactly
the gap deviation 3 prices. S-3 is the open that MAJOR-7 says the head must
stop pre-empting. S-4 is well chosen — R = 6 is where the refinement
criterion could stop being empty, and it is the only route by which segment 1
could change.

**Two additions the measurements here have earned:**

- **S-5 — the cardinality half of the fitting objection.** At one crossing the
  placement is inert and any of the 36 targets admits; what is never tested is
  a target declaring a *different number* of cross links than the event
  realises. The grid's ONE-AT-EVERY-SEAM row is the first data point (three
  declared, one realised: dead under the delivered legs, alive at
  NON-NEGATIVE). A census over declared-count vs realised-count is the test
  that would make "matched" a measured notion rather than a definition.
- **S-6 — the sighted regime's law.** S-2 asks whether it has one; the orbit
  sizes measured here are {72, 72, 108, 162, 216} at r = 2 and fifteen orbits
  at r = 3 summing to 7,140, with the admitted set at r = 2 exactly the
  108-orbit. Record those numbers in S-2 so the successor starts from data.

The "what may not be inherited" row is correct and complete for what it
covers; add **the declaration fibers** to it until MAJOR-2 is repaired.

---

## 8. WALLS

| wall | state |
|---|---|
| no extension is THE theory | **held.** The sentence is present, every target carries a fiber, and `G-WALL-EXTENSION` has teeth (it also checks that no cell is lawful at the delivered legs with zero declared links). This is the wall that mattered most and it is the best-built one in the unit |
| SEAM-CONFINED per #322 | **held as compliance, over-scoped as a sentence** — MAJOR-3 |
| no reading of the union as anything larger | **held**; the forbidden-term scan is real and the paper takes no Lorentzian, causal or dimensional reading |
| the indefinite completions still named and not read | **held**, and correctly restated as a narrowing rather than a signature |
| test-declaration duty (#322 §2) | **discharged** at the blindness probe (§4.4 opens "THE TEST, DECLARED", states both outcomes reachable, and both occur) and in substance at the group census (the 54 non-crossing controls fire ALIVE inside the same census). This is the duty SEC left undischarged; SEC-2 discharges it |
| E-24 / COUNTING-ONLY | **held.** §7 is exemplary: every ratio has its denominator beside it, the orbit-size disparity is disclosed, and the receipt carries the stamp |
| §15 declared-arena | **held**; the arena table is data, and the five window axes are declared before anything is measured |

---

## 9. WHAT I CONFIRM, AND WHAT MUST NOT MOVE IN REPAIR

Every one of these reproduced exactly from an independent rebuild:

- the seam census: **49 seam types over 132,273 shared sites**, (2,2,2) the
  one absent vector, and the population of every one of the 49 types;
- the completion table, **all 49 rows × lattice/posdef/parity**, including
  31/31/1 at the all-simple seam and 275/267/0 at the doubled-doubled ones;
- rank 6, kernel 4, RHS-independent; rank 7, kernel 3 with one crossing;
- positivity's minimum 31 and the **13 of 49** where admissibility implies it;
- the two-sided budget constant at all 49; the one-sided minima 14 and 14 with
  argmin sets of size 8 and 8, **disjoint**;
- Fischer at **49 of 49**, the direct sum the unique maximiser;
- the crossing cut **31 → 8**, all 8 positive definite, the direct sum absent;
- SEC's witness value **−2**, six counts returned, **4** cross counts below 1;
- the 16-row gluing census, all four columns, and 45,010 by two routes;
- the four measured price currencies at **45,010 of 45,010**, zero violations;
- 1,296 and 62,208 (both by my own search), 15 carriers, 36 cross pairs;
- **455** three-actor groups in **9** orbits of sizes {1, 4, 36, 36, 36, 54,
  72, 108, 108}; **288** seam-spanning; **0** alive at the delivered target;
  **54** non-crossing controls alive; **216** lawful; the **72** that stay dead
  are exactly those opening a within-sector pair;
- the four inventory rows exactly (62,208/1/1/1; 1,728/1/1/1; 1,728/3/9/4;
  576/1/3/2) and the free-item counts 0, 0, 3, 2;
- blindness **36/1, 630/5, 7,140/15**; sweeps **36 of 36** and **108 of 630**;
  the r = 2 orbit sizes {72, 72, 108, 162, 216} with the admitted set exactly
  the 108-orbit;
- all 22 declared SEC values, plus the committed SEC paper's sha.

**No delivered measured number may move in repair.** The only numbers that
must change are the two typed fibers (27 → 24, 9 → 8), which were never
measured.

---

## 10. CLOSE

Grade **ACCEPT-WITH-FIXES**. Eight MAJORS, nine MINORS, 1,593 value-level
recomputations, two disagreements found — both in the one column of the paper
that was typed rather than computed. The unit's physics is intact and its
central sentence is better than the one it wrote: gluing can be an event, at a
target that declares the seam it crosses, and it can never be a free one —
because three actors give three pairs and at most two of them can cross.

**Candidate readings until adjudication**, this review included.
