# ACT (paper-34) — K2 REVIEW: THE EFFECTUS LENS

**Seat:** K2 — verdicts, licensure and meaning.  **Stance:** hostile.
**Date:** 2026-08-12.  **Grade: AWF** (accept with fixes).

**Object, sha256-12, verified at open and at close, unchanged and clean in
git:** `v14/paper-34-act.md` `3fbf109f0d9b`; `v14/code/act_exact.py`
`02df3f00f788`; `v14/code/act_output.txt` `9299f80db2d8`;
`v14/code/act_receipt.json` `f0617d1687a0`; pin `v14/note-act-pin.md`
`766c603c6dbc`.  The paper's own inheritance paragraph names ten parent
digests; all ten verify against the tree (`6df0db523d32`, `126912ae7142`,
`0d6fbadd756d`, `79cc67b4f6cd`, `faf353385905`, `c9edf97a5533`,
`62cfe5689d2c`, `0d98de793b79`, `0c02b7684e5b`, `42255f50328a`).

**Recomputations: 179** — 119 exact-arithmetic recomputations (fractions and
integers only, no float in any verdict-bearing step), 15 digest
verifications, 26 wall-vocabulary sweeps, 11 verdict-segment-to-section
mappings, 8 head-law branch traces.

**Zero false computed numbers.** Every number I recomputed matched: the six
Burnside divisions, the six coupling counts, the six fibre dimensions, both
orbit-size profiles, all six class-size profiles, the extreme-point split at
both readings, the merged-pair counts, the pinned-indicator counts, all three
published expectations (reconstructed from scratch from the trace sum alone),
and the density witness.  Two of the three expectations I rebuilt from an
independent route — from the counting expectation 13/10, which fixes the
total trace sum at 832, I solved for the class size and trace value the
instrument must have used and recovered `4294967399/4294967375` and
`262244/65615` exactly.  The arithmetic of this unit is sound.

**The defects are all licensure, scope and disclosure.**  The delivered
outcome word is true.  What is not established at the delivered standard is
that it *could have been otherwise*, that it survives the arena's own free
axis, and that several of its prose sentences say what was measured.

---

## THE RANKED SUMMARY

| # | finding | what it touches |
|---|---|---|
| MAJOR-1 | three of four pre-registered outcomes were arithmetically unreachable at this arena before any measurement; the control arm forges rows, it does not price a synthetic arena | the verdict architecture — the pin's own named lesson |
| MAJOR-2 | the odd-twist mechanism — the price, the falsifier, the "sharpest surprise" — is contingent on $L=4$ and vanishes at every $L$ divisible by eight; undisclosed | the scope of every headline in the unit |
| MAJOR-3 | `FALSIFIER=HIT` — the pin's falsifier at its own wording is measured NOT hit at 12 of 12 rows | the outcome word of the pin's stage 4 |
| MAJOR-4 | the price paragraph: "a weight system supplies 135 independent numbers" is false at 4 of 6 declared rows; and "the cost is negative" contradicts "not a saving" two paragraphs above | the price sentence — the LOR lesson |
| MAJOR-5 | §7's "every named measure this corpus has on this carrier is run" is false — six named measures are not run | a completeness claim contradicted by a pinned parent |
| MAJOR-6 | the law-native control's own declared fibre is **six** — the unpinned identification its stamp names — and one member is built, undisclosed | the control discipline, seat charge 3 |
| MAJOR-7 | §11 states five verdict-determining choices and names four; the fifth is never named in the paper, and it is the axis carrying §7's headline | the choice inventory at the RSQ standard |
| MAJOR-8 | "lies in the closure" is a limit claim carried by one witness at $6.63\times10^{-5}$ | the head and the Decided list |
| MAJOR-9 | "the first quantity this arena hands over free" contradicts its own next clause, and "free" is unlicensed | the Decided list |
| MAJOR-10 | the POT handoff names "the action functional" as one of R5's three objects; it is not one of them | the successor register, seat charge 7 |
| MINOR-1..6 | below | |

**Walls: PASS.**  **Grain-relativity: PASS as E-24 measure-relativity, with a
ruled emphasis.**  **The stamp itself: PASS, carried verbatim at four sites
and never spent as derived.**

---

## MAJORS

### MAJOR-1 — The selector was not multi-way *at this arena*: three of the four pre-registered outcomes were arithmetically unreachable before a single measurement, and the control arm is one function short of the precedent the pin names

**Establishing measurement (mine, exact).**  An orbit count is at least
$\lceil |{\rm datum}| / |G| \rceil$.  Over the six declared rows, from the
instrument's own `form_census` fields:

| row | \|datum\| | \|G\| | minimum possible orbits | measured |
|---|---|---|---|---|
| LINK-ANCHORED | 640 | 8 | 80 | 136 |
| LINK-EXTENSION | 640 | 16 | 40 | 80 |
| PLAQUETTE-ANCHORED | 167772160000 | 1024 | 163840000 | 265121344 |
| PLAQUETTE-EXTENSION | 167772160000 | 4096 | 40960000 | 66311040 |
| SITE-ANCHORED | 167772160000 | 8192 | 20480000 | 171060256 |
| SITE-EXTENSION | 167772160000 | 32768 | 5120000 | 43398586 |

The smallest orbit count this arena can produce at any declared row is **40**.
`ACT-FORM-FORCED` fires only when `coupling_count == 0` at every row, i.e.
orbits $=1$ everywhere.  **It was impossible at this arena by pigeonhole
before the instrument ran.**  `ACT-GIBBS` fires only when the reachable
dimension is zero at every row, i.e. the stencil group is transitive on the
640-coin carrier; at the link grain the acting group has order 8 and 16, both
$<640$, so that too was impossible before the run — and the measured induced
classes are 136 and 80 at *all three* grains, never 1.  `ACT-BLOCKED-AT` fires
only on a Burnside sum that fails to divide, i.e. on an instrument fault.

So **one** pre-registered outcome was live at this arena from the moment the
arena was declared, and the instrument's job was to name it.

**What the instrument does do.**  `demonstrate_reachability` (act_exact.py
:2853–2895, gate `G-HEAD-LAW-REACHABILITY`) hands four synthetic censuses to
the one head law and to the second head law, and requires four distinct
strings.  That is a real gate and it kills a collapsed head law.  But the
synthetic censuses are the *real rows with a field overwritten* —
`dict(r, coupling_count=0)` and `dict(r, reachable_dimension=0)`.  The arm
exercises the last function in the chain and nothing behind it.

**Why that is short of the standard.**  The pin's walls read: "genuinely
multi-way outcome selectors with control arms (the paper-23/SIG lesson)".
Paper-23's own control arm, in its own head, is:

> THE-DERIVE-ARM-IS-REACHABLE-AND-IS-RUN: THE-CONTROL-ARM-ON-A-SYNTHETIC-
> TRANSITIVE-CARRIER-IS-PRICED-AT-0-FREE-ITEMS-BY-THE-SAME-FUNCTION

— a synthetic **arena** run through the **real pricing function**.  ACT runs a
synthetic **census** through the **head law**.  Between those two lies the
whole measurement chain, and it is exactly the chain whose ability to emit
`FORCED` is in question.

**The repair is cheap and the machinery already exists.**  The unit already
builds and runs a declared 19-coin reduced arena, closed under the coin-map
group, at every grain, through the real Burnside/brute-force route
(`reduced_arena_orbits_burnside` = 5, 4, 383, 124 …).  A reduced arena on
which the stencil group acts transitively — an alphabet that is a single
orbit — driven through the same `form_census` code, will return orbits $=1$,
coupling count $0$, and the delivery run will emit `ACT-FORM-FORCED` from a
measurement rather than from a forged dict.  Likewise a reduced arena whose
induced partition on the carrier is a single class emits `ACT-GIBBS`.

**Credit where due.**  §1 does *not* misdescribe what was done: it says "The
head law that chooses between them is handed **synthetic censuses**".  The
disclosure is accurate.  What is missing is the depth, and one sentence of
scope.  The §1 table's "measured" column also gives contingent-sounding
reasons ("not the case: the smallest coupling count measured is 79") where the
true reason is structural and available a priori.

**Candidate ruling — the exact licensed §1 paragraph:**

> **What could have answered the other way, and what could not.**  Four
> outcomes were pre-registered.  The head law that chooses between them is
> handed synthetic censuses in the delivery run and required to return each
> one, by two independent laws, in four distinct strings, so a law that had
> collapsed to a constant dies inside the run; and the same demand is put to
> the measurement chain itself on a declared reduced arena whose stencil group
> is transitive, where the chain returns one orbit, coupling count zero and
> the string `ACT-FORM-FORCED`.  At *this* arena, however, three of the four
> were closed before the instrument ran, and it is more honest to say so than
> to leave them looking live: an orbit count is at least the datum space
> divided by the group order, which is at least forty at every declared row,
> so `ACT-FORM-FORCED` was unreachable by counting alone; the induced
> partition on a 640-coin carrier cannot be a single class under a group of
> order 8 or 16, so `ACT-GIBBS` was too; and `ACT-BLOCKED-AT` fires only on an
> instrument fault.  The arena decided which of the four could be true.  The
> measurement decided that the one that could be, is — and by how much.

*If the adjudicator holds the pin's control-arm clause as a hard gate, this
finding alone is REJECT-grade.  I do not so hold it, because the paper's
description of what it did is accurate, the repair is a few lines against
machinery already present, and the delivered word survives the repair.*

### MAJOR-2 — The whole mechanism is $L=4$-contingent, and vanishes at every $L$ divisible by eight; the paper's "Not decided" list flags only the arithmetic obstruction

**Establishing measurement.**  §2 states the mechanism in its own words:

> A constant link twist is realisable by a gauge transformation exactly at the
> even values, because the phase must close after $L$ steps.

Take that at face value.  The site phases lie in $\mathbb{Z}_8$ (the field is
$\mathbb{Q}(\zeta_8)$); a constant twist $t$ closes around a cycle of length
$L$ exactly when $8 \mid Lt$.  Hence the residual gauge group on the carrier
has order $\gcd(L,8)$, while the *link stencil's* gauge image is the full
order 8 at every $L$ — a single link has two distinct endpoints and no closure
constraint, which is why the receipt records `gauge_image_order: 8` at both
readings.  The index — the factor by which the stencil group exceeds the
arena's own residual gauge group, and therefore the entire source of the
merging — is $8/\gcd(L,8)$:

| L | gcd(L,8) = residual order | stencil gauge image | index | orbit pairs merged |
|---|---|---|---|---|
| 2 | 2 | 8 | 4 | merges in **fours**, not pairs |
| 4 | 4 | 8 | 2 | pairs — **this unit** |
| 8 | 8 | 8 | **1** | **none** |
| 16 | 8 | 8 | **1** | **none** |

At $L=4$ the measured residual order is 4 (`residual_gauge.order_anchored`),
$= \gcd(4,8)$, and `realisable_constant_twists` is exactly $[0,2,4,6]$ — the
formula reproduces the instrument's own measurement.

**What follows.**  At any $L$ divisible by eight the odd twist *is* a gauge
transformation of the torus.  Then: no orbit pairs merge; the induced
partition equals the parent's orbit partition; the price is **not** reduced;
the off-diagonal quartic sign is **not** pinned; and the unit's "sharpest
surprise" does not exist.  At $L=2$ the merges are four-fold and the word
"pairs" is wrong.  Everything this unit calls a prohibition is a property of
$L=4$ — more precisely of $8 \nmid L$ — and the paper never says so.

**What the paper does say.**  §10's "Not decided" carries exactly one
lattice-sensitivity bullet, and it is about the *other* obstruction:

> **Whether the arithmetic obstruction survives a larger lattice.**  The
> exponent is the stencil count, so it grows with the volume …

A reader who takes that list as the register of what is lattice-sensitive will
conclude that the odd-twist finding is not.  The opposite is true: the
arithmetic obstruction is robust in the direction the paper worries about (a
larger exponent does not make $3/2$ a power), and the odd-twist obstruction —
the one carrying the price, the falsifier and the headline — is the one that
dies at $L=8$.

**This is owed to the corpus, not only to the reader.**  PER-L (paper-28) is a
delivered unit whose whole business is per-invariant PERSISTS/BREAKS/
TRANSFORMS along the $L$-ladder, and paper-23 already recorded that this
lattice's structural blade is even-$L$-specific.  ACT hands POT a mechanism
whose $L$-behaviour it has the closed form for and does not state.

**Candidate ruling — the exact licensed sentence, for §2 and for §10's
"Not decided" list:**

> **And the mechanism's own lattice-dependence is closed form.**  A constant
> twist $t$ closes around a cycle of length $L$ exactly when eight divides
> $Lt$, so the residual gauge group on the carrier has order $\gcd(L,8)$ while
> the link stencil's gauge image is the full eight at every $L$.  The merging
> that carries this unit's price, its prohibition and its pinned observable is
> exactly the index $8/\gcd(L,8)$: it is two here at $L=4$, it is four at
> $L=2$ where the merges would come in fours and not in pairs, and it is
> **one at every $L$ divisible by eight**, where the odd twist becomes a gauge
> transformation of the torus, no orbits merge, the price is not reduced and
> no observable is pinned.  Everything this unit measures about the odd twist
> is a statement about lattices whose size the phase order does not divide.

### MAJOR-3 — `FALSIFIER=HIT`: the pin's falsifier at its own wording is measured NOT hit, at 12 of 12 rows

**Establishing measurement.**  The pin asks:

> the cheap falsifier run: is there ANY gauge observable whose expectation
> **the covariance constraints** pin to a proper sub-range?

and SMU, quoted by the paper itself, asks:

> Search for a gauge-invariant functional whose range **over the invariant
> simplex** is *narrower* than its own range.

The receipt answers both, and the answer is no.  In `falsifier.rows`, the
column `range_over_the_invariant_simplex` is, at every one of the twelve rows,
the observable's own full value range: $[0,4]$, $[-1,1]$, $[-2,2]$, $[0,1]$,
$[0,1]$, $[0,1]$, and the same six at the extension.  Not one is narrowed.
Covariance pins nothing — which reproduces SMU's own finding
("COVARIANCE-PINS-THE-EXPECTATION-NOWHERE") and extends it from one observable
to six at two readings.  That is a genuine result and it is the **negative**
answer to the question as posed.

The pinning that *is* measured is by a different constraint set entirely:
`range_over_the_reachable_set` $=[0,0]$ for the off-diagonal quartic sign.
The constraints doing the work are gauge-invariance **of a local weight at a
declared grain** — the locality declaration — not covariance.

**The paper's disclosure is honest and its word is not.**  §8 publishes both
columns and names them correctly; the verdict string says
"EVERY-ADMISSIBLE-WEIGHT-SYSTEM-PINS-TO-…-[0,0]-AGAINST-[-2,2]-OVER-THE-
INVARIANT-SIMPLEX", which names the pinning agent.  But the segment opens
`FALSIFIER=HIT`, §8's bold sentence is "**The falsifier hits**", and §10's
Decided list carries it — and the falsifier that is named in the pin and
quoted in §8 is the one measured not to hit.

**Candidate ruling — the exact licensed §8 verdict, and the segment word:**

Segment: `FALSIFIER=NOT-HIT-AT-THE-PINS-WORDING-COVARIANCE-PINS-NOTHING-
12-OF-12-ROWS-AT-FULL-RANGE;HIT-AT-THE-ACTION-ROUTE:THE-OFF-DIAGONAL-QUARTIC-
SIGN-…` — or, if a single word is wanted, `FALSIFIER=HIT-AT-THE-ACTION-ROUTE-
NOT-AT-COVARIANCE`.

Prose:

> **The falsifier as the pin words it is measured not to hit, and that is the
> first half of the result.**  At 12 of 12 declared observable rows the
> expectation's range over the parent's invariant simplex is the observable's
> own full range, so the covariance constraints pin nothing — SMU's finding
> for the loop trace, reproduced and extended to six observables at both
> readings.  **The hit is at the action route, and only there.**  The
> off-diagonal quartic sign is a gauge observable at both readings; every
> admissible weight system at every declared grain gives it expectation
> exactly zero, against $[-2,2]$ over the parent's invariant simplex.  What
> pins it is not the arena's symmetry but the locality declaration, and the
> distinction is the whole content of the row.

### MAJOR-4 — The price paragraph carries a false relation and an internal contradiction

**(a) "A weight system supplies 135 independent numbers" is false at four of
the six declared rows.**  §6:

> A weight system supplies 135 independent numbers where the parent's
> declaration supplies 207, and 79 and 119 at the extension reading

The instrument's own `weight_space_rank` column says a weight system supplies
**135** at the link grain, **265121343** at the plaquette grain and
**171060255** at the site grain (79 / 66311039 / 43398585 at the extension).
The number 135 is the *reachable dimension*, and it is 135 at all three
grains.  The sentence attributes to the weight system a count that belongs to
its image.  This is the LOR disease exactly: a true number, a true number, and
a false relation between them.  It matters because 135 appears in this paper
in two distinct roles — the link-grain coupling count in the FORM segment and
the grain-invariant reachable dimension in the PRICE segment — and this
sentence is where a reader is invited to conflate them.

**(b) "the cost is negative in the strict sense" contradicts "the deficit is
not a saving", two paragraphs above.**  §6 says both:

> the deficit is not a saving.  It is a prohibition …

> … and the cost is negative in the strict sense: locality buys numbers by
> forbidding them

A negative cost *is* a saving in the free-parameter accounting these two
paragraphs share.  One of the two value words has to go, and it is the second:
the measurement licenses "fewer numbers, because fewer distinctions", not
"cheaper".

**On "locality buys numbers by forbidding them" — RULED LICENSED, as a gloss.**
It compresses an exact measurement: $207-135 = 72$ and the merged pairs number
72; $119-79=40$ and the merged pairs number 40; and the 72 classes that are
not singletons are precisely the edge-midpoint extreme points of the reachable
set (verified at 6 of 6 rows).  The numbers locality removes *are* the numbers
that would have separated odd-twist pairs.  Keep the sentence; delete the
"negative cost" clause it is bolted to.

**On `PRICE=REDUCED-NOT-EVADED` against SMU's committed frame — RULED
COMPATIBLE, with a required clause.**  SMU's head commits to
`PRICE=CONSERVED-NOT-PAID … WHAT-MOVED-IS-WHERE-THE-DECLARATION-IS-MADE-NOT-
HOW-MUCH-IT-COSTS`, and its §7 supplies the carve-out: "the price is conserved
**only under a retained covariance declaration**", with 639 the cost when the
symmetry is dropped.  ACT does not retain the parent's declaration: at the
link grain the acting group has order 8 where the parent's residual gauge
group on the carrier has order 4, and the extra element is a bijection of the
carrier that is *not* a gauge transformation of this torus.  ACT therefore
demands invariance under a strictly larger group, and SMU's own law says a
changed symmetry declaration changes the amount.  The two heads do not
collide — but nothing in ACT's price segment says so, and a reader holding
both heads sees `CONSERVED-NOT-PAID` against `REDUCED-NOT-EVADED` on the same
named price with no scope between them.

**Candidate ruling — the exact licensed price paragraph:**

> An action does not evade the parent's price and it does not pay it.  Under
> the locality declaration the measures an action can reach form a set of
> dimension 135 at the anchored reading and 79 at the extension, inside the
> parent's 207- and 119-dimensional invariant simplexes — and inside the
> 639-dimensional simplex the parent reaches once covariance is dropped.  The
> weight systems themselves are larger objects at two of the three grains: a
> weight system supplies 135 numbers at the link grain but 265121343 at the
> plaquette grain and 171060255 at the site grain, and the difference is
> exactly the fibre the carrier cannot see.  **So the price is reduced and not
> evaded, and the reduction is neither a saving nor a violation of the
> parent's conservation.**  It is a discount bought by demanding invariance
> under a group strictly larger than the arena's own: the link stencil's gauge
> image has order eight where the residual gauge group on the carrier has
> order four, and the extra element is the odd twist, which no gauge
> transformation of this torus performs.  The parent's law — that what moves
> is where a declaration is made and not how much it costs — was stated at a
> retained symmetry declaration, and this unit does not retain it; it demands
> more, and more symmetry discounts, as the parent's own 639 records.  What
> the discount removes is exact and named: 72 pairs of gauge orbits at the
> anchored reading and 40 at the extension are identified by every admissible
> weight system at every declared grain, and they are the pairs whose two
> members differ by the odd twist.  The reachable set is therefore described by
> its extreme points and not only by its dimension: 64 vertices of the
> parent's simplex and 72 midpoints of its edges at the anchored reading, and
> 40 and 40 at the extension.

(The extension's extreme-point split, 40 and 40, is in the receipt and absent
from §6's prose; I verified it independently by the index-2 structure — the
28 sixteen-element classes are pairs of parent octs, twelve of the sixteen
eight-element classes are pairs of parent quads, and four are single parent
octs.  Include it.)

### MAJOR-5 — §7's completeness claim is false: six named measures on this carrier are not run

**The claim.**  §7 opens:

> Every named measure this corpus has on this carrier is run against the Gibbs
> map, and each failure is attributed to a measured species …

**The measurement that falsifies it.**  SMU — pinned, hash-verified, quoted
elsewhere in this very paper — publishes in its §8 twelve named dynamics with
**ten distinct stationary vectors on this carrier**, and names each measure:
COUNTING (three routes), ORBIT-UNIFORM-CHART-32, ORBIT-UNIFORM-CHART-128,
**LAW-NATIVE-012, LAW-NATIVE-021, LAW-NATIVE-102, LAW-NATIVE-120,
LAW-NATIVE-201, LAW-NATIVE-210**, and METROPOLIS-AT-A-NON-INVARIANT-TARGET.
Its receipt confirms `census.distinct_stationary_vectors: 10` and
`relativity.new_law_native_measures_entering_the_comparison: 6`.

ACT's target census runs six: COUNTING, ORBIT-UNIFORM-ANCHORED,
ORBIT-UNIFORM-EXTENSION, LAW-NATIVE-PI, MONOMIAL-HAAR, ODD-TWIST-GRADED.  Of
SMU's ten it runs four.  **Six named measures on this carrier are not run** —
five of the six law-native members and the non-invariant control.

The last of those would fail trivially (it is not orbit-constant, so not
class-constant), which is precisely why running it costs nothing and would
populate the UNREACHABLE-BY-SYMMETRY arm with a corpus object instead of an
object this unit constructed for the purpose.

**Candidate ruling — the exact licensed sentence:**

> Six named measures are run against the Gibbs map — the corpus's three
> reached nulls, one member of the law-native family, the parent's handed-over
> monomial Haar, and one target this unit constructs to populate the symmetry
> arm — and each failure is attributed to a measured species rather than to a
> single verdict.  The declared target list is a choice with an unbounded
> fibre and it is measured verdict-determining, because the census verdict is
> a count over it: the corpus holds ten distinct named measures on this
> carrier at SMU's terminal, and six are run here.

### MAJOR-6 — The law-native control's own declared fibre is six; one member is built, and the delivered reason is member-specific

**The stamp's content.**  SMU's receipt records, for family (c):

- `privilege.instances: 6`
- `privilege.the_unpinned_step: THE-IDENTIFICATION-OF-THE-TRANSPORT-LAWS-THREE-POSITIONS-WITH-THIS-ARENAS-THREE-COIN-SECTORS`
- the six members are named LAW-NATIVE-012 … LAW-NATIVE-210 — the six
  permutations, one per assignment.

The stamp `LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION` is
*about* that six-fold ambiguity.  ACT carries the stamp verbatim (four sites,
swept below) and then treats the control as one object called LAW-NATIVE-PI,
without naming which member it is, and states the obstruction's reason as a
number belonging to one member:

> THE-TARGET-IS-CLASS-CONSTANT-AND-FULL-SUPPORT-AND-UNREACHABLE-BY-ARITHMETIC-
> BECAUSE-**3/2**-IS-NOT-AN-EXACT-POWER

**My measurement.**  The three rates are $15/38$, $5/19 = 10/38$, $13/38$; the
sectors have sizes 64, 64, 512.  The reachability-relevant ratio is the one
between the two equal-sized sectors, and it moves with the assignment:

| assignment (diag, anti, bal) | required ratio | a 32nd power? |
|---|---|---|
| 15/38, 5/19, 13/38 | 3/2 | no |
| 15/38, 13/38, 5/19 | 15/13 | no |
| 5/19, 15/38, 13/38 | 2/3 | no |
| 5/19, 13/38, 15/38 | 10/13 | no |
| 13/38, 15/38, 5/19 | 13/15 | no |
| 13/38, 5/19, 15/38 | 13/10 | no |

**The verdict is robust — all six are UNREACHABLE-BY-ARITHMETIC — and this
unit did not measure that.**  It built one member, and published a reason that
holds for one member.  A reader who checks a different member finds a
different ratio and no statement about it.

**Candidate ruling.**  Run the fibre — it is six evaluations of an existing
predicate — and emit:

> The control enters at its parent's stamp, and the stamp names what is
> unpinned: the identification of the transport law's three positions with
> this arena's three coin sectors, a declared fibre of six.  All six members
> are run.  Every one is class-constant and of full support, so every one lies
> inside the symmetry-allowed set; and every one is unreachable, for a reason
> that is arithmetic rather than structural — the mass ratio each requires
> between the two equal-sized sectors is one of 3/2, 2/3, 15/13, 13/15, 10/13
> and 13/10, and none is an exact power at either declared exponent.  The
> verdict is therefore independent of the unpinned identification, which is
> the only form in which a control carrying that stamp can be reported.

**The stamp discipline itself: PASS.**  I swept every occurrence.  The stamp
appears verbatim in the verdict string, twice in §5.2 (once as the paper's own
naming, once inside the parent's quoted sentence), and in the §12 handoff; the
receipt carries it at `law_native_control.stamp`, in an anchor row, and in a
declared/measured pair.  The control is never spent as derived: §5.2 "as a
control and nothing else", "It is not spent"; §10 "spent as nothing"; §12
"the law-native control at its stamp"; receipt
`never_spent_as_derived: true`, `the_honest_use: A-CONTROL-THE-DISTANCE-IS-
REPORTED-AND-THE-AGREEMENT-IS-NOT-CLAIMED`.  Its only other appearance is as
one row of the target census, which is use as a *target*, not as a derived
measure — compliant with SMU's order "ACT must not treat it as a derived
measure and must not spend it as one."

### MAJOR-7 — §11 states five verdict-determining choices and names four; the fifth is never named in the paper

**Establishing measurement.**  `fibre.rows` has 13 rows; exactly five carry
`verdict_determining: true`:

`THE-LOCALITY-GRAIN`, `WHICH-CHART-READING`,
`THE-INVARIANCE-FORM-LOCAL-OR-PRODUCT`, `THE-FIELD-THE-WEIGHTS-LIVE-IN`, and
**`THE-NAMED-TARGETS`** (fibre UNBOUNDED, 6 instances built, "the census
verdict is a count over the declared targets, so declaring another moves it").

§11 names the first four and then discusses `THE-DECLARED-OBSERVABLES`, whose
flag is `false`.  `THE-NAMED-TARGETS` appears nowhere in the paper — not in
§11, not in §7, not in §13.  Nine of the thirteen rows are named in §11; the
four unnamed are THE-NAMED-TARGETS, THE-REDUCED-ARENA-FOR-THE-VALIDATION,
THE-DECLARED-NON-UNIFORM-SAMPLE and THE-WITNESS-DENOMINATOR.

**Why this one matters most.**  It is the axis under §7's headline "1 of the 6
named targets is reachable", and it interlocks with MAJOR-5: the undisclosed
verdict-determining axis is exactly where the false completeness claim sits.
A count over an unbounded declared fibre, presented as a census of "every
named measure this corpus has", with the axis's verdict-determining flag
measured `true` in the sealed receipt and absent from the paper — that is the
choice inventory failing at the one row where it was load-bearing.

**Candidate ruling — add to §11:**

> … and the declared target list is DECLARED-AND-DISCLOSED at an unbounded
> fibre and flagged verdict-determining, because §7's verdict is a count over
> it: six targets are declared and run, the corpus holds ten distinct named
> measures on this carrier, and declaring another moves the count.  The
> declared observables carry the opposite disclosure: the falsifier verdict is
> existential, so declaring more of them cannot remove the hit …

### MAJOR-8 — "lies in the closure" is a limit claim carried by one finite witness

**Establishing measurement (mine, exact).**  `density_witness` gives
numerator 101275, denominator 100000, exponent 32.  In lowest terms
$r = 4051/4000$, and
$|r^{32} - 3/2| = 6.631186\ldots\times 10^{-5} < 10^{-4}$ — I recomputed it in
exact rationals and confirmed the bound.  One witness, one error bound.

§5.2 asserts the limit and illustrates it:

> The image is dense where it is not onto: an explicit rational found by
> integer bisection drives the required ratio inside a published bound … The
> control lies in the *closure* of the image and not in the image.

and §10 puts it in the **Decided** list: "lies in the closure of the image".
The verdict string carries "IT-LIES-IN-THE-CLOSURE-EXACT-WITNESS-AT-
DENOMINATOR-100000-WITH-ERROR-BELOW-1/10^4".

**The gap.**  Membership in a closure is a statement about *every* $\epsilon$.
A witness at $6.63\times10^{-5}$ establishes that the image comes within
$10^{-4}$ and nothing more.  The density that would license the word is true
and elementary — the 32nd powers of the positive rationals are dense in the
positive reals — but it is an unproved, ungated assertion in this paper, and
the corpus's own rule is measure, do not argue.  The head is partly honest
(it carries the witness's precision beside the word); the Decided list is not.

**Candidate ruling — the exact licensed sentences:**

> That distinction is made exact rather than left as a word.  The exact
> rational 101275/100000, found by integer bisection with no float and no root
> extraction anywhere, raised to the declared exponent 32 differs from the
> required ratio 3/2 by less than 1/10^4 — the image comes that close.  That
> the control lies in the *closure* and not in the image is a theorem and not
> the witness's doing: the thirty-second powers of the positive rationals are
> dense in the positive reals, so every neighbourhood of the target meets the
> image while the target itself is outside it.  The witness exhibits one point
> of the approach; the limit is carried by the theorem, which is stated here
> and gated as a theorem.

(Or, if the theorem is not to be gated: strike "closure" from the Decided list
and the verdict string and publish the bound alone.  Either is honest; the
current pairing is not.)

### MAJOR-9 — "the first quantity this arena hands over free" is self-contradicted in its own sentence, and "free" is unlicensed

**The sentence**, §8:

> That is the first quantity this arena hands over free, and it is handed over
> by the action route and not by the arena.

Read it twice: the arena hands it over, and the arena does not hand it over.
Three separate defects in one clause:

1. **The contradiction**, above.
2. **"free" is false.**  The pinning is bought by the locality declaration at
   a declared grain over a declared field — the very declarations §11 flags
   verdict-determining.  Nothing about it is free; §6's own analysis is that
   locality *purchases* this by forbidding.
3. **"first" is unchecked.**  Paper-23's head already carries
   `THE-ONE-CANONICAL-MEASURE-THIS-ARENA-HANDS-OVER=HAAR-ON-THE-128-ELEMENT-
   MONOMIAL-SUBGROUP`.  Whether an expectation and a measure are the same kind
   of "quantity" is arguable, but the corpus has a prior "hands over" and this
   paper does not de-conflict it.

§10's Decided list repeats it: "which is the first quantity this arena has
handed over free".

**Candidate ruling — the exact licensed sentence:**

> It is the first expectation this corpus has measured to be independent of
> the declared weights, and it is bought and not free: what pins it is the
> locality declaration at any of the three declared grains, over the declared
> field, and not the arena's own symmetry — which, as the same table shows,
> pins nothing.

### MAJOR-10 — The POT handoff misnames R5's three objects

**R5's own sentence**, quoted correctly by §12:

> A confinement analog would need three objects this arena does not have: **a
> measure on configurations**, a family of loops whose size can grow, and a
> coupling to vary.

**ACT's next sentence:**

> Two of the three are now priced objects rather than absences: **the action
> functional** is a weight system at a declared grain, and the coupling is a
> coordinate of the allowed space.

"The action functional" is not one of R5's three.  It is *paper-23's* object,
from the other quotation this paper opens with ("A weight of the form $e^{-S}$
needs an action functional and a coupling").  The two two-object lists have
been conflated, and the object R5 actually named first — the configuration
measure — is not named in the handoff sentence at all.

**A second, sharper point.**  R5 asked for a measure on **configurations**;
ACT supplies a reachable set of measures on the **carrier**, the 640 uniform
configurations, and its own scope segment says
`FULL-CONFIGURATION-SPACE=640^32-NOT-A-CARRIER-HERE`.  §10's "Not decided"
carries that restriction; §12 does not, and §12 is the sentence POT will read.
R5 was explicit about the ordering — "Any pin that opens such a follow-on has
the configuration measure as its **first** obligation, before a loop family
and before a coupling" — which makes the misnaming consequential rather than
cosmetic.

**Otherwise the handoff inventory is complete and correctly walled.**  What is
handed over (`pot_handoff`): the allowed space and its exact description; the
coupling inventory at all six rows; the three distinguished points; the
reachable measures at both readings; the pinned observable with its mechanism.
What is not: any loop family (0 grown), any selection among the couplings,
anything past POT's gate.  All three refusals are in the receipt, in §12 and
in the verdict string.

**Candidate ruling — the exact licensed §12 paragraph:**

> R5 named three objects: a measure on configurations, a family of loops whose
> size can grow, and a coupling to vary, and it named the first as the first
> obligation of any pin that opens the follow-on.  Two of the three are now
> priced.  The measure is supplied **at the parent's carrier and not at R5's
> configuration space**: the reachable measures are a proper sub-simplex of
> the parent's invariant simplex, of dimension 135 at the anchored reading and
> 79 at the extension, reached from a weight system whose form this unit
> characterises exactly.  The coupling is a coordinate of the allowed space,
> at an inventory that is grain-relative and is handed over at all six
> declared rows.  The second object — a family of loops whose size can grow —
> is recorded as **still absent**, and it is the gate on everything beyond.
> Nothing here is claimed for the $640^{32}$ configuration space.

---

## MINORS

- **MINOR-1 — §11's "the one place" is false, and §6 says so.**  §11: the
  field is "the one place this unit's negative rows depend on a declaration
  rather than on the arena."  But UNREACHABLE-BY-SYMMETRY depends on the
  *locality* declaration — §6: "the reduction is the locality declaration's
  doing, not the arena's" — and the locality grain is itself pin-declared and
  flagged verdict-determining in the same table.  Licensed: "the one place a
  negative row depends on the *field* rather than on the arena; the symmetry
  species depends on the locality declaration, as section 6 measures."

- **MINOR-2 — §8's mechanism argument covers only half the classes.**  "it is
  *reversed* by the odd twist, so every class of size greater than one carries
  it in equal and opposite parts."  The 64 singleton classes are not covered,
  and they are exactly where the argument is easiest: a coin fixed by the odd
  twist has its quartic sign equal to its own negative, hence zero.  The
  *result* is measured (`range_over_the_reachable_set: [0,0]`); only the prose
  argument is incomplete.  Add the clause.

- **MINOR-3 — the §7 verdict column carries no field qualifier.**  Three rows
  read `UNREACHABLE-BY-ARITHMETIC` with no scope in the table; the paragraph
  beneath supplies it correctly ("the field's doing … over the positive reals
  those rows would be reachable").  Since §7's table is the object a reader
  lifts, put the qualifier in the column head:
  "verdict (over the declared field)".
  *This is the only qualification I attach to seat-charge 3's second half:*
  **the UNREACHABLE-BY-ARITHMETIC finding is correctly stated as a property of
  the pin's declared field and not of the world**, in §5.2, §7, §10 and §11,
  and in the choice inventory.  That is a PASS.

- **MINOR-4 — the verdict-determination census is partial and the paper does
  not say so.**  Four of the thirteen rows carry `verdict_determining:
  NOT-MEASURED`, and one of them is `THE-CARRIER` (fibre 2, one instance
  built) — the object on which every statement about measures in this unit is
  made, and whose other member §10 concedes is "untouched".  The count "5" is
  a lower bound over the nine axes where the flag was measured.  §11's word
  "measured" carries this only to a careful reader.  Licensed: "13 choices are
  inventoried; the verdict-determining flag is measured at nine of them and 5
  are positive; the remaining four, the carrier among them, carry an
  unmeasured flag because their alternatives are out of reach by cost."

- **MINOR-5 — §10's Wilson bullet is compressed to the point of a missing
  middle term.**  "the plaquette is not forced because the gauge group is not
  transitive on a single link's datum" — the inference is sound (single-link
  invariants abound, they extend to the plaquette grain, so the Wilson shape
  is one point of a large space) but two of its three steps are absent from
  the sentence.  §5.1 has them; the bullet should not lose them.

- **MINOR-6 — the paper carries no E-24 stamp in its own text.**  The receipt
  carries it twice (`gibbs.every_integer_here_is_a_count_stamp`, and per row).
  The paper publishes many "$n$ of $m$" figures and never converts one to a
  probability, so the discipline is honored in substance; one sentence in §6
  or §3 naming the stamp would put it where a reader is.

---

## THE SEAT'S RULINGS ON THE CHARGES PUT TO IT

**Charge 1 — the outcome word.**  `ACT-FORM-RELATIVE` is **true** and is
correctly instantiated by the pin's registered form `<dimension; the coupling
inventory>`.  The selector is genuinely multi-way **at the head law** (gated,
two independent laws, four distinct strings, `MUT-REACHABILITY` declared).  It
is **not** multi-way at this arena: three of four outcomes were closed by
counting before the run (MAJOR-1).  The control arm is one function shallower
than the paper-23 precedent the pin cites.  *(One registered-form nit: the head
law's `ACT-GIBBS` branch emits `<image>` only, where the pin registered
`ACT-GIBBS-<image; the price verdict>`.  Since the branch is unreachable at
this arena the defect never fires, but a repair that makes it reachable should
fix the form.)*

**Charge 2 — the price sentence.**  Numbers exact and reproduced.
`REDUCED-NOT-EVADED` is compatible with SMU's `CONSERVED-NOT-PAID` under
SMU's own carve-out, because ACT demands invariance under a strictly larger
group — but the compatibility clause is missing and must be added.
"Reduced" is licensed **only of the reachable dimension**, not of the weight
space's rank (MAJOR-4a).  The 72-pair identification **is** correctly stated
as a prohibition, correctly scoped to "every admissible weight system", and
correctly mechanised.  "The cost is negative" must go.  Exact licensed
paragraph given under MAJOR-4.

**Charge 3 — the control discipline.**  Stamp carried verbatim at four sites,
never spent as derived: **PASS**, swept.  The stamp's *content* — the six-fold
unpinned identification — is not honored: **MAJOR-6**.
UNREACHABLE-BY-ARITHMETIC is stated as a property of the declared field and
not of the world: **PASS** (MINOR-3 is presentational).  "Lies in the closure"
is **not** licensed at the measured precision: **MAJOR-8**.

**Charge 4 — grain-relativity as ontology.**  **RULED: E-24 measure-relativity,
a declared axis honestly priced — not a physical relativity.**  I swept the
paper for ontological vocabulary: no "universe", no "gauge-constant", no
α-analogue framing anywhere (the pin's α-analogue language is not carried into
the paper), and the grain is named a "declared axis the arena does not fix" in
both §3 and §10, exactly as §15 requires.  But the emphasis is the less
licensed half.  The unit holds a **grain-invariant** quantity and does not say
so plainly: at 3 of 3 grains the reachable dimension is 135 anchored and 79 at
the extension, over the same 136 and 80 induced classes, and the entire
six-order-of-magnitude spread lies in the fibre (rank − reachable = fibre,
verified at 6 of 6 rows).  §15 directs significance at the invariant.  The
head carries the invariance only implicitly, in the GIBBS segment's
"THE-INDUCED-PARTITION-IS-THE-SAME-136-CLASSES-AT-ALL-3-GRAINS".

*Exact licensed sentence, for §3's verdict paragraph and §10's Decided list:*

> The coupling count is grain-relative and moves by six orders of magnitude
> across a declared axis the arena does not fix.  The number of couplings the
> carrier can see is not.  At each of the three declared grains the reachable
> measures have the same dimension — 135 at the anchored reading and 79 at the
> extension — over the same 136 and 80 induced classes, and the whole
> grain-to-grain difference sits in the fibre, exactly rank minus reachable
> dimension at 6 of 6 rows.  What is grain-relative is the coordinate count of
> the declaration; what is grain-invariant is everything the declaration can
> do to a measure.  Only the second is eligible to mean anything here.

*And "locality buys numbers by forbidding them":* **RULED LICENSED** as a gloss
on an exact measurement ($207-135=72=$ merged pairs; $119-79=40=$ merged
pairs), provided the "negative cost" clause is deleted.

**Charge 5 — the falsifier.**  `HIT` is **not** the licensed word for the
falsifier the pin and SMU worded: **MAJOR-3**.  The comparator object is
correctly chosen and correctly named — it is the *parent's* invariant simplex
on 208 and 120 orbits, and §8 says so.  $[-2,2]$ is the convex hull of the
observable's orbit values, which equals its own full range, which is precisely
why the covariance arm returns nothing.  "The first quantity this arena hands
over free" **overclaims and self-contradicts**: MAJOR-9.

**Charge 6 — the walls.**  **PASS.**  I swept 26 terms including synonyms and
negations.  `area-law` ×3, `string-tension` ×3, `potential` ×3, `confin` ×4 —
every one inside a declaring/negating sentence or inside a quoted parent
must-not, which is the withholding machinery working as designed and is gated
("the must-not vocabulary sweep with the declaring sentences removed first and
every declaring sentence required to be located here").  No `quark`, `flux
tube`, `screening`, `deconfinement`, `linear/static potential`, `glueball`,
`hadron`, `asymptotic freedom`, `running coupling`, `beta function`, `lattice
spacing`.  No SI units.  `0 loop families grown`, stated in the receipt, §9,
§10 and §12.  The 27 "tension" hits are all the substring in "extension".

*The Wilson-shape minimality row applies paper-23's criterion correctly one
grain down.*  Paper-23's criterion is that a canonical, zero-free-item object
exists exactly where the declared structure acts transitively; §3's theorem —
the allowed space is exactly the orbit-constant functions, of rank the orbit
count — **is** that criterion at the stencil grain, so the transport is not an
analogy but an instance.  Non-transitivity on a single link's coin (136
classes where transitivity would leave one) therefore licenses "not forced"
and, since single-class generators exist and the Wilson family spans 10 of the
carrier's 135, licenses "not minimal-support".  Both comparisons are made on
the carrier and stay on it; §13's third scope point correctly refuses the
plaquette-datum-space statement.  Only §10's one-sentence compression loses
the middle term (MINOR-5).

**Charge 7 — the POT handoff.**  Inventory complete and correctly walled, but
the three-object sentence misnames R5's first object: **MAJOR-10**.

**Charge 8 — windows and choices.**  13 choices, 5 verdict-determining, four
disclosed, the fifth never named: **MAJOR-7**; census partial at four rows:
**MINOR-4**.  *The parent's-uniform-carrier-only window is licensed in-string:*
**PASS** — the verdict's SCOPE segment carries
`CARRIER=THE-PARENTS-640-UNIFORM-CONFIGURATIONS;FULL-CONFIGURATION-SPACE=
640^32-NOT-A-CARRIER-HERE`, §2 declares the carrier as data with the reason
(it is the chart-fixed locus, so the two units weigh the same partition), and
§10's "Not decided" names the full space.  §12 is the one place the window
drops out (MAJOR-10).

**Charge 9 — head against body.**  All eleven verdict segments have a body
section that carries them, and I checked each: CENSUS→§3 table; THE-ALLOWED-
SPACE→§3; LOCALITY→§4; (a)WILSON-SHAPE→§5.1; (b)LAW-NATIVE-CONTROL→§5.2;
(c)NULL→§5.3+§7; GIBBS→§6; PRICE→§6; FALSIFIER→§8; WILSON→§9; SCOPE→§2+§13.
No segment is orphaned and no body headline lacks a segment.  The prose that
outruns its receipt is enumerated above: MAJOR-3 (`HIT`), MAJOR-4a (the false
relation), MAJOR-4b (the contradiction), MAJOR-5 (false completeness),
MAJOR-8 (the closure word), MAJOR-9 (the self-contradiction), MINOR-1 (the
false universal), MINOR-2 (the half argument).  **Eight prose defects, zero
numerical ones.**

---

## WHAT I RECOMPUTED, AND WHAT SURVIVED UNTOUCHED

**Verified exactly, matching at every row:** all six Burnside sums divide their
group orders and give the published orbit counts; coupling count = orbits − 1
at 6 of 6; acting group order equals the naive product at 5 rows and half of
it at exactly one (LINK-EXTENSION), as §3 says; both parent orbit-size
profiles sum to 640 and to 208/120; all six class-size profiles sum to 640 and
to 136/80; merged pairs = parent orbits − induced classes at 6 of 6; reachable
dimension = classes − 1 at 6 of 6; fibre = rank − reachable at 6 of 6
(0, 0, 265121208, 66310960, 171060120, 43398506); extreme points sum to the
class count and the midpoint count equals the merged-pair count at 6 of 6;
invariant simplex dimensions 207 and 119 = orbits − 1; 639 = 640 − 1.

**Verified by independent construction, not by reading the receipt:** the
index-2 structure at the extension reading — since ACT's link-extension acting
group has order 16 and the parent's residual gauge group order 8, every class
is one parent orbit or exactly two of equal size, from which the extension's
class profile (8×1, 28×2, 16×8, 28×16) forces 28 sixteen-classes from oct
pairs, 12 eight-classes from quad pairs and 4 from single octs, giving 40
merges, 40 vertices and 40 midpoints — all three matching the receipt, none of
them read from it first.  This also proves the paper's word "**pairs**" exact
at both readings, which it asserts and does not derive.

**Verified by independent construction:** the pinned-indicator counts.  144 of
208 anchored = 72 merged pairs × 2, and 80 of 120 at the extension =
(28+12) × 2.  The "at most half its own range" claim follows because a merged
class is exactly twice its member orbit.

**Verified by independent reconstruction of the physics numbers:** from
$13/10 \times 640 = 832$, the total trace sum, I recovered both non-null
expectations without the instrument — the exhibited witness is a weight of 2
on a size-8 class of trace value 1 at exponent 32, giving
$(8\cdot 2^{32}\cdot 1 + 824)/(8\cdot 2^{32} + 632) = 4294967399/4294967375$;
the Wilson-shape row is a weight of 2 on the 8 coins of trace 4 at exponent
16, giving $262244/65615$.  Both published values reproduce exactly, both lie
in $[0,4]$, and §9's gloss — that a single factor of two moves the expectation
almost all the way from 13/10 to the class's own trace value 1 — is exact:
$4294967399/4294967375 = 1 + 24/4294967375$.

**Verified:** the density witness, $|(101275/100000)^{32} - 3/2| =
6.6312\times10^{-5} < 10^{-4}$, in exact rationals; and $3/2$ is not a 16th or
32nd power of a rational, by unique factorisation.

**Untouched by me, left to the operator and instrument seats:** the coin family
enumeration and its 64/64/512 split; the chart group's transitivity on links,
plaquettes and sites; the two character-route closed forms (530219008 and
342102016) and the "one linear relation" claim; the reduced-arena validation
counts; the 8192 Wilson gauge checks; the seal, the anchors, the mutant sweep
and the CLI contract.

---

## GRADE, AND WHAT IT TURNS ON

**AWF.**  The delivered outcome word is true; the arithmetic is clean at 119
independent recomputations with zero false numbers; the walls hold; the
control stamp is carried and never spent; the grain-relativity is honestly
priced; and every one of the ten majors has an exactly liftable repair, none
of which moves a computed number and none of which changes the verdict word.

Two of them must be repaired before terminal, and they are the two that touch
what the unit is *for*:

- **MAJOR-1**, because the pin walls this unit with the paper-23/SIG lesson by
  name, and at this arena the verdict was decided by the declaration.  The
  repair is a transitive reduced arena through the real chain.
- **MAJOR-2**, because a mechanism that dies at $L=8$ is being handed to POT
  and to a corpus with a live $L$-ladder programme, with a closed form the
  unit already has in its own §2 sentence and does not state.

The rest are prose against receipt, and this seat's standing complaint is that
the receipt was right every time.

---

*Candidate readings until adjudication.  This review is a single repo write;
git was read-only throughout; all execution was in scratch.*
