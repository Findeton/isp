# SEC (paper-32) — K2 EFFECTUS REVIEW

**Seat:** K2, the EFFECTUS lens — verdicts, licensure, meaning. Does the text
claim exactly what was measured?
**Stance:** hostile. Every ruling below is a **candidate ruling until
adjudication**.
**Repo write:** this file only. Git strictly read-only.

## Objects, verified at open and at close

| object | declared | at open | at close |
|---|---|---|---|
| `v14/paper-32-sec.md` | `cfe0825d67b2` | `cfe0825d67b2` | `cfe0825d67b2` |
| `v14/code/sec_exact.py` | `6481a8706503` | `6481a8706503` | `6481a8706503` |
| `v14/code/sec_output.txt` | `e80d2f08a257` | `e80d2f08a257` | `e80d2f08a257` |
| `v14/code/sec_receipt.json` | `fdf66d990dbf` | `fdf66d990dbf` | `fdf66d990dbf` |
| `v14/note-sec-pin.md` | `c46a9927f2a8` | `c46a9927f2a8` | `c46a9927f2a8` |
| `v14/paper-33-aid.md` (authority) | `ecdd3fbf1d06` | `ecdd3fbf1d06` | `ecdd3fbf1d06` |

Read as authority: HANDOFF-PROMPT.md §4/§9; the pin; AID (§4, §6.1, §6.2, §9);
paper-21 §4.5 and its head; paper-01 (R1) §8.2 and its closing OPENS;
paper-19 §-quotes; RUNBOOK E-22/E-23/E-24. Sibling in-flight object files
(PER-R/POT/SPC/FAC) were not opened.

---

# GRADE: **AWF** (accept with fixes) — at the top of its severity band

**Zero published numbers are false.** I recomputed 546 published or
head-carried quantities from my own primitives, plus two exhaustive sweeps
over all 45,010 gluings and 200 driven records re-driven on the unit's own
instrument, and every one reproduced exactly — the whole 16-row
type census (gluings/carriers/pairs/doubled), all 16 automorphism orders, all
three seam systems with their exact minors and indefinite witnesses, the
cross-link algebra, the compatibility census, 4186/45010, 2970/42336,
3359232 = 1296² × 2. The arithmetic layer of this unit is clean.

**The reading layer is not.** Eleven majors below. Ten are prose or head
claims that outrun their receipts; one (MAJOR-3) shows a **free item moving a
head number's referent**. **All four head segments carry a repair order**, and
two head clauses (`EXT-INCIDENCE-REPAIRS-EVERY-TYPE`, `THE SEAM'S GEOMETRY IS
AVAILABLE ONLY BY LEAVING THE TARGET`) have no measurement behind them at all.
One prose sentence — §4.3's "the induced field becomes identically 1" — is
**contradicted by the run's own receipt**.

AWF rather than REJECT because no theorem asserted here is false, no number is
false, and every major has an exact liftable repair. AWF at the top of the band
because the head does not survive unamended.

---

# RECOMPUTATION LEDGER

All recomputation code is mine, written from AG(2,3) and the tripartite
construction, sharing no code, no import and no typed literal with
`sec_exact.py`. Scratch only.

| # | recomputed | quantities | result |
|---|---|---|---|
| R-1 | sector: 27 pairs, all counts 1, degree 6 at 9, parts = the ANT class | 4 | reproduces |
| R-2 | \|Aut(sector relation)\| = 1296 | 1 | reproduces |
| R-3 | family 45010; by k = 1/81/2592/42336; closed form | 6 | reproduces |
| R-4 | doubled-free by k = 1/81/1134/2970, total 4186 | 5 | reproduces |
| R-5 | the 16-row type census: gluings, n, E, dbl | 64 | reproduces |
| R-6 | \|Aut\| and \|Aut_w\| at all 16 types (independent backtracking counter; 8 of them re-derived a third time by hand as wreath/stabilizer orders) | 32 | reproduces |
| R-7 | seam rank/kernel at **all 39 shared sites of the 16 type representatives** | 78 | rank 6, kernel 4 at 39 of 39 |
| R-8 | direct-sum minors (3×4), posdef (3), indefinite witness value (3), count reproduction (3) | 21 | reproduces |
| R-9 | cross-link algebra kernels 4,3,2,1,0 | 5 | reproduces |
| R-10 | compatibility census: shared cells and differing cells, 16 types | 32 | reproduces |
| R-11 | leak grain: both endpoints of every differing cell; pairs with count ≠ 1 touching an unshared actor | 32 | see MAJOR-5 |
| R-12 | the degree claim at all 15 types with k > 0 | 15 | see MAJOR-9 |
| R-13 | alignment criterion vs. the **realised relation, per gluing, at all 45,010** | sweep | 0 mismatches |
| R-14 | arena-is-a-function-of-the-type: WL invariant over all 45,010; constructive (α,β,π) equivalence at 210 sampled gluings | sweep + 210 | true — and **ungated**, see MAJOR-7 |
| R-15 | 16 types collapse to how many union arenas up to isomorphism | 5 | **12, not 16** — MAJOR-7 |
| R-16 | overlap table: welds column vs. doubled-free | 16 | reproduces |
| R-17 | sterility: 18, 54, 0, 0, 0, 3359232, prediction | 7 | reproduces |
| R-18 | k-by-k doubled-free table | 8 | reproduces |
| R-19 | headline scalars 2970, 4186, 62208, 1296, 3359232 | 5 | reproduces |

**Total: 546 quantities + 2 exhaustive 45,010-gluing sweeps + 200 driven
records re-driven on the unit's own instrument.**

Three **hostile probes run on the unit's own instrument** (labelled as such —
they test the unit's claim with the unit's own driver, which is the only way
the question can be posed):

| probe | what | result |
|---|---|---|
| HP-1 | the `first`-rule fate at 25 representatives each of 5 types — **125 driven records** | **the fate moves inside the type at 2 of the 5 tested** — MAJOR-3 |
| HP-3 | the `shared`-rule fate at 5 representatives of each of the 15 types with k > 0 — **75 driven records** | **the fate does not move: 0 of 15 types, 75 of 75 FORCED** — MAJOR-3's counter-measurement, and it defends the paper's other fate clause |
| HP-2 | the same at 20 representatives × 16 types × both rules | **still running at close; not relied on by any ruling** |

MAJOR-3 rests on HP-1 and HP-3, both landed. In each the fate of the *window's
own* representative reproduced the committed table (5 of 5 in HP-1, 15 of 15 in
HP-3), so the probes are faithful to the instrument; the HP-1 flips are then
flips of the same instrument on other members of the same type. HP-2 would only
widen the counts and is disclosed rather than waited on (a disclosed anomaly
beats an undisclosed marathon).

**200 driven records re-driven in total.** The two probes disagree in the way
that matters: the free representative moves the canonical-rule fate and leaves
the shared-rule fate alone, which is the asymmetry §3.2's own mechanism
predicts.

---

# MAJORS

## MAJOR-1 — the segment-4 outcome word is a TYPED LITERAL; the declination of `SEC-K-SELECTED` is asserted, not measured

**Brief item 1.** The pin pre-registered five outcomes:
`SEC-COMPOSES` / `SEC-SEAM-CURVATURE` / `SEC-NEVER-WELDS` / `SEC-K-SELECTED` /
`SEC-BLOCKED-AT`. §13.3 states the declination as a priced deviation:
"`SEC-K-SELECTED` is declined. The pin pre-registered it; the measurement says
alignment selects and k does not."

**Establishing measurement.** The comparator `reconstruct` (sec_exact.py
2659–2677) is genuinely multi-way, but **only over segment 2's word**: its
branches reach `SEC-NEVER-WELDS`, `SEC-COMPOSES` and
`SEC-BLOCKED-AT-THE-UNION-DICTIONARY`, and G-VERDICT-RECON binds it as
`headword = verdict[1].split("-[")[0]`. Segments 1, 3 and 4 have **no
comparator**. Segment 4's word —
`SEC-OVERLAP-TYPE-SELECTED-NOT-k-SELECTED` — is a typed literal inside the
builder's format string (2635–2652); its five `%d`s are two gluing counts, two
automorphism orders and the typed `4 * 3`. Nothing in the instrument reads
`ks_with_weld` / `ks_without` into a word. Had the census returned
`k_with_a_welding_type = [0,1,2]`, the head would still have read
`TYPE-SELECTED-NOT-k-SELECTED`, and its bracket's first clause would have been
false beside four still-true numbers.

G-FORCED-OVERLAP does not close the gap. Its predicate is `not obad`
(welds ⟺ doubled-free, type by type) — a statement that says nothing about k.
Its *statement* nonetheless asserts "and the criterion is the ALIGNMENT of the
tripartite classes, **not the cardinality k**". The k-selection claim rides in
the gate's prose and in the evidence dict; it is not bound by any predicate.
That is #87 in reverse: the aggregate travels, the object-level predicate does
not exist.

**The #299 standard, honestly reported.** This pin predates #299, and the pin
does not require control arms per outcome word. The measured control the unit
*does* carry is the k = 0 sterility arm and the five dead arms — which
discharge the *detector's* value set (HA requirement 3, and it holds: all six
fates `ARITY-DEAD` / `STRUCT-DEAD` / `COUNT-DEAD` / `FOUND-STRUCTURAL` /
`FOUND-candidate` / `UNMOTIVATED` are exhibited). What is missing is a control
arm for the **selector**: no world is exhibited on which the instrument emits
`SEC-K-SELECTED`, and none on which it emits a seam-determined outcome. The
gap is real and should be recorded against the unit rather than waived on the
pin's date.

**Licensed sentence (replaces §13.3's second clause and gates segment 4's
word).**

> `SEC-K-SELECTED` is declined on the census: at 16 of 16 types the union
> welds exactly at the doubled-free gluings, and k ∈ {2,3} each carries both a
> welding and a non-welding type while k ∈ {0,1} carries only welding types
> (k = 1 has no pair of shared actors to double). The declination is a reading
> of that table; the head's outcome word is TYPED and is not re-derived by any
> comparator, so no measurement in this run would have moved it.

**Repair order.** Extend `reconstruct` to type segment 4's word itself from
`forced_overlap`'s own rows — emitting `SEC-K-SELECTED` when
`ks_without` is a set of k values disjoint from `ks_with_weld`, and
`SEC-OVERLAP-TYPE-SELECTED-NOT-k-SELECTED` otherwise — and bind
`ks_with_weld` / `ks_without` in G-FORCED-OVERLAP's predicate, not only in its
evidence. Until then, segment 4's word carries a `WORD-TYPED-NOT-DERIVED`
stamp.

## MAJOR-2 — §14 makes a false claim about its own comparator

§14: "The head is derived a second time by a comparator that shares neither
code nor input nor typed literal with the builder: **it types all four
templates itself and re-derives the outcome word** from the receipt's own fate
rows."

**Establishing measurement.** `reconstruct` (2659–2677) contains no template
string of any kind. It reads `rec["dictionary"]`, `rec["seam"]`,
`rec["sterility"]` and returns four scalars. It re-derives **one** word, from
**one** segment. Three of the four head segments are unre-derived. The code's
own comment carries the same false sentence.

The gate itself is honest — G-VERDICT-RECON's statement says "re-derives **the
head's outcome word**", singular. The paper inflated it.

**Licensed sentence.**

> The head's second segment is derived a second time by a comparator sharing
> neither code nor input nor typed literal with the builder: it re-derives that
> segment's outcome word from the receipt's own fate rows, and re-checks the
> seam kernel and the sterility identity. Segments 1, 3 and 4 are rendered from
> the receipt and gated verbatim against the run's own verdict strings, but
> their words are not independently re-derived.

## MAJOR-3 — a FREE item moves a head number's referent: the `first`-rule fate is not a property of the type

**This is the sharpest instrument-side finding, and it lands on segment 1. It
is asymmetric between the two seed rules, and the asymmetry is measured: the
`shared`-rule clause survives the probe intact, the `first`-rule clause does
not.**

§11 item 16: "the window's type representative | **free** | — | this unit's;
the type is gated to determine the arena". §11's closing: "item 16 chooses
which gluing of a type is driven, and the type census measures that the arena
is a function of the type." The justification is that the *arena* is a function
of the type — which is true (R-14). But the **driven fate is not a function of
the arena**: it is a function of the gluing's actual site labels, because the
`first` seed rule takes `names[0]` at the lexicographically-first *site* of
each conflict group (sec_exact.py 784–803) and the group order is by
`repr(seed)`, under which a shared actor's name `('S', i)` sorts after every
`('A', …)` and `('B', …)`.

**Establishing measurement (HP-1, the unit's own driver, 125 driven records).**

| type | window rep's fate at `first` | over 25 representatives |
|---|---|---|
| `(2, (0,0,1), (1,0,1))` | REFUSED | REFUSED 25 |
| `(2, (0,0,2))` | REFUSED | REFUSED 25 |
| `(3, (0,0,3))` | REFUSED | REFUSED 25 |
| `(2, (0,0,1), (0,1,1))` | **FORCED** | **FORCED 8, REFUSED 17** |
| `(3, (0,0,1), (1,1,2))` | **FORCED** | **FORCED 4, REFUSED 21** |

The window's representative reproduces the committed fate at 5 of 5, so the
probe is faithful; and at 2 of the 5 types the same type's other
representatives flip. One flip suffices to defeat the type-level reading; two
of five suggests it is common. **Note the direction: both flips are FORCED
window representatives whose siblings mostly REFUSE**, so the committed
"REFUSED 6 of 16" is if anything an *under*-count of the refusal rate under
paper-19's rule — the repair does not soften the paper's result, it re-scopes
it.

**The counter-measurement, which defends the other clause (HP-3, 75 driven
records).** Under the **shared** rule the fate does **not** move: at all 15
types with k > 0, the window's representative and four further representatives
each drive to FORCED — **0 of 15 types move, 75 of 75 records FORCED**. So the
head's `FORCED 16 OF 16 … AT THE SHARED-SEED RULE` is stable across the free
item at this sample and needs no re-scoping beyond naming its objects records;
only the `REFUSED 6 OF 16 AT PAPER-19'S CANONICAL RULE` clause is
representative-relative. The asymmetry is exactly what §3.2's mechanism
predicts — under the `shared` rule a shared actor always seeds when the group
holds one, so the shared actors always carry the base rather than receive it —
which is a point *for* the paper's mechanism and should be reported as such.

**Consequence.** The head's
`FORCED 16 OF 16 WINDOW RECORDS AT THE SHARED-SEED RULE, REFUSED 6 OF 16 AT
PAPER-19'S CANONICAL RULE` names 16 as the count of **types** (the builder
passes `len(typerep)`), and §3.2 reads it that way: "Under paper-19's canonical
rule it REFUSES at **6** of them" — them being the 16 types. For the second
clause that referent is wrong: the measured object is 16 **chosen gluings**,
one per type, and a different choice of representative — the free item —
returns a different number. G-SEED-RULE inherits the defect on the same side:
its statement says the grammar "REFUSES at some **types**", while its predicate
ranges over the 16 representatives and the type-level reading is false.

§3.2's closing generalisation is separately unlicensed: "**A union is drivable
exactly when the shared actors carry the base into the second sector rather
than receive one.**" HP-3 is consistent with it and is real support — 75 of 75
drivable under the rule that always makes the shared actor carry — but "exactly
when" is a universal drawn from 6 refusals that are all literally the same
event (`propose ('B',(1,0))` at prefix 49 — verified at all 6 rows of the
receipt) plus 26 successes, at one arrangement.

**Licensed sentences.**

Head segment 1, replacing the two fate clauses:

> `FORCED 16 OF 16 DRIVEN WINDOW RECORDS AT THE SHARED-SEED RULE, REFUSED 6 OF
> 16 AT PAPER-19'S CANONICAL RULE; THE FATE AT THE CANONICAL RULE IS A PROPERTY
> OF THE DRIVEN GLUING AND NOT OF ITS TYPE`

§3.2, replacing "Under paper-19's canonical rule it REFUSES at 6 of them":

> Under paper-19's canonical rule the grammar refuses at 6 of the 16 driven
> window records. The window drives one representative per type, and at that
> rule the fate is a property of the representative rather than of its type:
> the seed rule reads the actors' names, which the type does not fix. Under the
> shared-seed rule the fate does not depend on the representative, because a
> shared actor seeds wherever a group holds one.

§3.2's closing sentence:

> At every refusal in this window the same event refuses — `propose ('B',(1,0))`
> at prefix 49, at 6 of 6 — and the mechanism is the version lineage: a group
> seeded by a sector-B actor that holds a shared actor must supply its base to
> that actor, the delivery puts sector A's whole past into the seed's causal
> past, and the layer's menu offers nothing but idle. Whether that mechanism is
> the *only* obstruction to drivability is not measured here.

**Repair order.** Either (a) re-scope every fate statement to "driven window
records" and add the sentences above, or (b) drive the FORCED/REFUSED census
over a declared representative sample per type and publish both fractions. (a)
is the cheap and honest route; (b) is the strong one, and HP-1/HP-3 show it is
cheap enough to run. Reclassify item 16 from **free** to **free,
VERDICT-DETERMINING for the canonical-rule fate clause; measured inert for the
shared-rule clause at 5 representatives × 15 types**.

## MAJOR-4 — `EXT-INCIDENCE-REPAIRS-EVERY-TYPE` has no measurement behind it, and its stated mechanism is contradicted by the receipt

Head segment 2, final clause:
`EXTENDED-CARRIERS:EXT-PAIR-AGREES-WITH-BARE,EXT-INCIDENCE-REPAIRS-EVERY-TYPE(FOUND-16-OF-16)-BECAUSE-THE-DOUBLED-PAIR-SPLITS-INTO-TWO-SITES`.
§4.3: "`EXT-INCIDENCE` is different, and it is the LOR lesson paying out. One
object per (division event, pair) splits a doubled pair into TWO site objects,
**the induced field becomes identically 1**, and the structural test passes at
every type including the doubled ones."

Four establishing measurements, all from the unit's own receipt:

1. **The fate is stamped, not measured.** `detect` returns `FOUND-STRUCTURAL`
   with `inventory = "READ-AT-BARE"`, `maps = "READ-AT-BARE"`,
   `scope = "STRUCTURE-AND-COUNT-ONLY"` at every non-BARE carrier (1388–1407).
   The RSQ inventory — the only thing that could establish a *repair* of the
   free item — is never read there. The head's bare word `FOUND-16-OF-16` is
   the receipt's `FOUND-STRUCTURAL` with its qualifier dropped.
2. **Nothing structural was broken to repair.** The head's own second clause
   says `STRUCT-ALIVE-16-OF-16`, and §4.1 says the structural test passes "at
   both readings and at all three carriers". The BARE carrier already passes
   structure at all 16 types. `EXT-INCIDENCE`'s structural pass at 16 of 16
   repairs nothing that failed.
3. **The stated mechanism is contradicted by the run.** The induced count
   field is carrier-independent by construction — `detect` computes it as
   `target_field(target, rel, phis, …)` from the union's **actor-pair** counts
   (1379), and the code's own comment says so: "no carrier extension changes
   what the record counts." The receipt's `field_values` on the
   `EXT-INCIDENCE` rows is **[1, 2] at all six doubled types**, exactly as at
   BARE. §4.3's "the induced field becomes identically 1" is false of the
   object the receipt publishes under that name in those very rows.
   *Pre-empting the charitable rebuttal*: if "the induced field" is instead
   meant as the extended carrier's own incidence relation, that is all-1 by
   construction on both sides — `r[frozenset((u,p))] = 1` on the record side
   (sec_exact.py:1306 and :1313) and `tinc[frozenset((u,lo))] = 1` on the target side (:1319) —
   i.e. the definition of a subdivision, before any measurement. So the
   sentence is either false of the receipt's object or vacuous of the
   construction's; on neither reading can it carry the head's word `REPAIRS`.
4. **The two extended carriers are indistinguishable in the fate column.**
   `EXT-PAIR` and `EXT-INCIDENCE` carry identical fates at **all 32 rows**, and
   both differ from BARE at **all 32 rows**. The head words one
   `AGREES-WITH-BARE` and the other `REPAIRS-EVERY-TYPE` — two opposite words
   for two columns that are equal to each other and both unequal to the column
   named.

**Licensed sentences.**

§4.3:

> `EXT-PAIR` adds one site object per realised pair and changes no count the
> record makes: a pair carrying two divisions is still one object.
> `EXT-INCIDENCE` adds one object per (division event, pair), so a doubled pair
> becomes two site objects and the carrier's own incidence relation is
> identically 1 by construction. Both extended carriers return
> `FOUND-STRUCTURAL` at all 16 types and at both readings — the structural
> question only, at the scope stamped in the row. The dictionary's induced
> count field is read from the actor pair and is therefore the same at all
> three carriers: it takes the values 1 and 2 at the six doubled types under
> every carrier, `EXT-INCIDENCE` included. Whether the extended carrier removes
> the free item is **not measured**: the RSQ inventory is a statement about the
> map to the target's cells, those cells are the bare carrier's, and the
> inventory is read there.

Head segment 2, final clause:

> `EXTENDED-CARRIERS:BOTH-RETURN-FOUND-STRUCTURAL-AT-16-OF-16-AND-32-OF-32-ROWS-UNDER-CHARTED(EXT-INCIDENCE)-AND-SIMPLE(EXT-PAIR);THE-INDUCED-COUNT-FIELD-IS-CARRIER-INDEPENDENT-AND-UNCHANGED;THE-RSQ-INVENTORY-IS-READ-AT-BARE-ONLY-SO-NO-REPAIR-OF-THE-FREE-ITEM-IS-MEASURED`

**Note for the adjudicator.** §4.3's closing paragraph — "**The extended
carrier repairs the seam by declaring away the thing the seam measures**" — is
the paper's best sentence and it survives the repair intact as a statement
about the CHARTED declaration. It should be kept; only the claim that a repair
was measured must go.

## MAJOR-5 — the leak claim smuggles an influence reading, and the measurement says the opposite of what the sentence says

**Brief item 3.** §5.1: "**This is the sharpest thing in the unit that nobody
asked for.** At a doubled type the union's count on a seam link is 2 while the
sector that owns that link says 1. The sector's own geometry is not preserved
by the gluing: **an actor's local form is changed by an event in the OTHER
sector.**" §12 repeats it: "so a sector's local form is changed by an event in
the other one."

**Establishing measurement (R-11, mine, exhaustive over the 16 types).**

- Every cell at which the union's count differs from 1 has **both endpoints
  shared**, at 16 of 16 types (differing cells: 0,0,0,0,2,0,0,2,4,0,0,4,0,6,4,0
  — reproducing the paper's column exactly).
- Over the **whole** union arena, not only the census's 6k shared cells, the
  number of pairs carrying a count other than 1 that touch an **unshared**
  actor is **0 at every one of the 16 types**.

So: no unshared actor's geometry moves at all, and the cells that do move are
cells of pairs *both of whose actors belong to both sectors*. A doubled pair is
by definition a pair realised in A and in B, which forces both endpoints to be
shared. There is no sector-private link that a foreign event reaches into.
"An event in the OTHER sector" mislocates a link that both sectors own, and
"the sector's own geometry is not preserved" reads as influence where the
measurement is an arithmetic fact about a shared cell: the union counts the
division events of both sectors, and at a link both sectors realise, that is
two.

**The TEST-DECLARATION DUTY (AID §6.1/§6.2), inherited and not discharged.**
The paper contains **0 occurrences** of `transported`, `fixed attribution`,
`relabelling`, `parse` or `orbit-constant`. The compatibility probe compares
"the union's count" against "the count that actor's OWN sector carries" — a
comparison that names a cell by its actor pair across two different objects
with different automorphism groups. That is precisely AID's **fixed
attribution**, and it must say so; under the transported reading no such
comparison is even posed, because nothing carries the union's cells to the
sector's. (Instrument note, for K3: the sector's own count is not read from the
sector — `own = 1` is a typed literal at sec_exact.py:2227. It is *true* — the sector's field
is 1 at 27 of 27 — but a typed literal is standing where a measurement is
claimed.)

**Licensed sentences.** §5.1, replacing the two sentences after the table:

> **Read at the fixed attribution** — a cell named by its actor pair, at the
> naming the gluing declares; AID §6.2's test, and the only one under which
> this comparison is posed at all — the union's count field does not restrict
> to either sector's. At a doubled type the union reads 2 at exactly the cells
> of the pairs that are adjacent in both sectors, where each sector alone reads
> 1. Both endpoints of every such pair are shared actors, necessarily: a pair
> realised in both sectors has both its actors in both. Measured over the whole
> union arena and not only the census's shared cells, no pair carrying a count
> other than 1 touches an unshared actor at any of the 16 types. So the
> deformation is confined to the seam in the strongest sense available: what
> moves is the count on the links the two sectors hold in common, and it moves
> because the union counts the division events of both. Nothing private to
> either sector moves, and no event of one sector reaches a link the other does
> not also carry.

Head segment 4 and §12: delete "a sector's local form is changed by an event in
the other one" and carry instead:

> `SEAM-CONFINED: THE UNION'S COUNT FIELD DIFFERS FROM THE SECTORS' AT EXACTLY
> THE SHARED-SHARED CELLS, 0 CELLS TOUCHING AN UNSHARED ACTOR AT 16 OF 16
> TYPES (FIXED-ATTRIBUTION READING)`

**Why this matters most.** The brief says this claim will travel far. In its
delivered form it would travel as "geography leaks between sectors" — a
locality-violation reading that the measurement flatly refuses. In the repaired
form it travels as something better and true: *the union's geometry is the
sectors' everywhere except on the links they share, and there it is the sum.*
That is a compositionality statement, not a leak.

## MAJOR-6 — "AVAILABLE ONLY BY LEAVING THE TARGET": the "only" is unlicensed and contradicts the unit's own S-3

Head segment 3 closes: `THE SEAM'S GEOMETRY IS AVAILABLE ONLY BY LEAVING THE
TARGET`. §6.3's block quote: "geometry AT the seam is available **only** by
leaving the atlas the seam was built in."

**What is licensed.** The forward half is stronger than the paper claims — it
is a theorem, not two witnesses. By the pin's own definition a cross-sector
division event carries "one actor from each side beyond the shared set", so it
realises an A-only/B-only pair; the amalgam T(k,γ) is built from two copies of
I7's lattice glued along shared sites, so it carries no link between an A-only
and a B-only site; hence **every** cross-sector division event returns
`STRUCT-DEAD` at the declared target. The 2 admitted specifications exhibit it;
they do not establish it, and the paper does not prove it either — §6.3 gives
the argument in prose without gating it.

**What is not licensed.** The converse — that *nothing else* fixes the four
entries. §13.6 concedes "no census of all cross-sector groups is run and none is
claimed", item 15 is classed **free**, and the unit's own successor register
says the opposite of the head:

> **S-3** … Whether any further committed structure fixes the other four, or
> whether they are permanently a declaration, **is the sharpest open question
> this unit creates.**

A head that says "ONLY" and a register that says "open" cannot both stand.

**Licensed sentences.** §6.3's block quote:

> The seam's four undetermined entries are exactly what a cross-sector division
> event would fix — one entry per cross link, measured 4,3,2,1,0 on the exact
> system — and fixing them that way leaves the declared target by theorem: a
> cross-sector event in the pin's sense realises an A-only/B-only pair, and the
> amalgam carries no such link, so the detector returns STRUCT-DEAD. Two of the
> three driven specifications are admitted and both do exactly that. Whether any
> structure other than a cross-sector division event fixes those four entries is
> not decided here, and is registered open at S-3.

Head segment 3's closing clause:

> `EVERY CROSS-SECTOR EVENT THAT WOULD FIX A SEAM ENTRY LEAVES THE TARGET (BY
> THEOREM ON THE AMALGAM'S LINK SET; 2 OF 2 ADMITTED WITNESSES DIE AT
> STRUCTURE); WHETHER ANY OTHER COMMITTED STRUCTURE FIXES THEM IS OPEN (S-3)`

**Also rule (brief item 2, first half).** "**the direct sum is a declaration,
not a measurement**" — **LICENSED EXACTLY AS WRITTEN**, and it is the unit's
best result. It is carried by rank 6 / kernel 4 on the 10 entries of Sym²(Q⁴)
(which I verified at all 39 shared sites of the 16 type representatives, not
only the 3 the instrument runs) together with the exhibited exact rational
completion reproducing all six counts and negative on [2,1,−1,−2] while C = 0 is
positive definite by the exact Sylvester criterion. Six of ten entries fixed,
four free, the direct sum one point of a 4-parameter affine family: the
sentence claims exactly that and no more. §6.1's NAMED-AND-NOT-READ paragraph
correctly refuses the Lorentzian resonance and is mandatory — keep it verbatim.

## MAJOR-7 — the exhaustiveness licence is unmeasured, and §5.2's arena count is wrong

Two separate defects in the same paragraph of the unit's licence to speak past
the window.

**(a) "gated as a per-type check rather than assumed" is false about the
instrument.** §13.2: "the census measures that the union arena is a function of
the type and reports gluings-per-type as the fiber, which is a stronger
statement than the pin required and **is gated as a per-type check rather than
assumed**." The only per-type check in G-GLUING-CENSUS is
`typebad = [t for t, gl in typerep.items() if (len(gl),)+gluing_type(gl) != t]`
— which checks that each representative reproduces the type it was indexed
under. Since `typerep.setdefault(t, gl)` sets the entry *from* `gluing_type(gl)`,
that is a cache-consistency check, not a measurement. **No pair of gluings of
the same type is ever compared.** The claim is assumed exactly where the paper
says it is gated — and it is the claim that converts every 16-type statement
into a 45,010-gluing statement, including the head's
`MOTIVATED-AT-10-OF-16-TYPES(4186-OF-45010-GLUINGS)`.

The claim is nonetheless **true**, and I established it so the adjudicator does
not have to take it on faith: a WL invariant of the weighted union is constant
inside every type across all 45,010 gluings (0 movers), and a constructive
(α, β, π) equivalence between the type's representative and the member was
found at 210 of 210 sampled gluings. It is also a theorem: Aut(K₃,₃,₃) acts
transitively on ordered k-tuples with a given part-pattern, and the type is
exactly the pair of induced index-partitions.

**(b) §5.2's "16 union arenas" is wrong — there are 12.** §5.2: "The gluing
carries 45010 choices collapsing onto **16 union arenas**, so the type map's
fiber is the gluings-per-type column of section 3.1." Measured (R-15): the type
is taken up to permutation of each sector's parts but **not** up to the A↔B
swap, and exactly four mirror pairs of distinct types carry isomorphic union
arenas:

| type | mirror type | gluings |
|---|---|---|
| `(2,(0,0,1),(0,1,1))` | `(2,(0,0,1),(1,0,1))` | 486 + 486 |
| `(3,(0,0,1),(0,1,1),(0,2,1))` | `(3,(0,0,1),(1,0,1),(2,0,1))` | 486 + 486 |
| `(3,(0,0,1),(0,1,1),(1,2,1))` | `(3,(0,0,1),(1,0,1),(2,1,1))` | 8748 + 8748 |
| `(3,(0,0,1),(0,1,2))` | `(3,(0,0,1),(1,0,2))` | 972 + 972 |

So 45,010 gluings collapse onto **12** union arenas up to isomorphism, and the
fiber of the *arena* map is the sum of the two type populations at each mirror
pair (up to 17,496), not the gluings-per-type column. The mirror pairs are
visible in the delivered census itself — identical n, E, dbl and |Aut| at each
pair — so this is a reading the delivered table already contains.

**Licensed sentences.** §5.2:

> The gluing carries 45,010 choices collapsing onto 16 combinatorial types and,
> up to isomorphism of the weighted union, onto 12 arenas: four pairs of types
> are exchanged by the A↔B swap, which the type does not quotient by, and each
> such pair carries one arena. The type map's fiber is the gluings-per-type
> column of §3.1; the arena map's fiber is that column summed over each mirror
> pair. Nothing in this paper is read off a single gluing: every published row
> is a row of a type, and the union arena is a function of the type.

§13.2, replacing "is gated as a per-type check rather than assumed":

> The union arena being a function of the type is what licenses every 16-type
> column to speak about 45,010 gluings. It is a consequence of Aut(K₃,₃,₃)
> acting transitively on ordered k-tuples with a given part-pattern; it is
> **not gated in this run**, and the census computes one representative per
> type without ever comparing two gluings of the same type. Registered as an
> instrument debt.

**Repair order.** Add a gate that, at each type, verifies against a declared
sample of that type's own members that the weighted union is isomorphic to the
representative's — constructively, by exhibiting (α, β). Correct the arena count
to 12 in §5.2.

## MAJOR-8 — §14's rendered-claim boast is false at 56 of 131 data rows, including the compatibility census that carries the leak claim

§14, bolded: "The paper under test is checked in the same run for claim
rendering — **every data row of every table above is a rendered claim of the
receipt** — so a swapped cell dies".

**Establishing measurement.** The paper carries 13 tables with 131 data rows.
`paper_claims` carries 83 entries: 8 prose claims (C01–C08) and 75 table rows
in six families — `T-CENSUS` 16, `T-WINDOW` 32, `T-OVERLAP` 16, `T-SEAM` 3,
`T-CROSS` 3, `T-XALG` 5. **Seven tables, 56 data rows, are not rendered
claims:**

| table | rows | rendered? |
|---|---|---|
| §2.3 the carriers and the readings | 3 | no |
| §4.1 the free-item / fiber table | 2 | **no** — the RSQ inventory |
| §4.4 the controls, two-way | 5 | **no** — the HA-3 discharge |
| §5.1 the compatibility census | 16 | **no** — the leak claim's own table |
| §7 the k-by-k doubled-free table | 4 | no |
| §8 the k = 0 sterility table | 10 | **no** — "the unit's licence to speak" |
| §11 the choice inventory | 16 | **no** |

Verified directly: **no claim in the registry contains the string `COMPATIBLE`
or `SEAM-DEFORMED`**, so not one row of §5.1 is bound. The uncovered set is
precisely the paper's interpretive spine — the RSQ inventory, the two-way
controls, the compatibility census on which MAJOR-5's headline rests, the
sterility arm, and the entire choice inventory.

G-PAPER-COVERAGE still backs the numerals, but a *swap* between two cells whose
numerals both live in the registry passes — e.g. exchanging `carriers | 18` and
`realised pairs | 54` in the §8 table, or moving a `SEAM-DEFORMED` verdict
between rows of §5.1, which carries no numeral at all. The declared mutant
`MUT-PAPER-TABLE` swaps cells in a `T-CENSUS` row, i.e. inside the covered set,
so the falsifier demonstrates the protection only where it already exists
(E-23: a falsifier's published description is part of the sealed surface).

**Licensed sentence.** §14:

> Every data row of the census, window, overlap, seam, cross-sector and
> cross-link tables — 75 of the paper's 131 table rows — is a rendered claim of
> the receipt, so a swapped cell in those dies here. The carrier, free-item,
> control, compatibility, k-by-k, sterility and choice-inventory tables are
> covered by the numeral registry only; a swap inside them is caught if and only
> if it moves a numeral out of the registry, and a swapped verdict word in the
> compatibility census is not caught at all.

**Repair order.** Render the §4.1, §4.4, §5.1, §7 k-by-k and §8 tables as
claims — all five are already in the receipt as `dictionary`, `dead_arms`,
`gluing_fiber.compatibility`, `gluing_totals` and `sterility` — and add a
mutant that swaps a verdict word in the §5.1 table.

## MAJOR-9 — the edge-transitivity mechanism is stated with a false degree law, at exactly the types it is deployed against

§3.1: "The gluing destroys edge transitivity: **a shared actor has twice the
degree of an unshared one**, so the seam is visible in the bare structure,
every automorphism preserves it, and the weight function is stabilised whether
or not it is constant."

**Establishing measurement (R-12, all 15 types with k > 0).** Unshared degree is
6 at every type. Shared degree is 12 at 9 types and **10 or 11 at the other
six** — and at three of those six the shared actors do not even share a degree:

| type | shared degrees | twice? |
|---|---|---|
| `(2,(0,0,1),(1,1,1))` | 11 | no |
| `(3,(0,0,1),(0,1,1),(1,0,1))` | 11, 12 | no |
| `(3,(0,0,1),(0,1,1),(1,2,1))` | 10, 11 | no |
| `(3,(0,0,1),(1,0,1),(2,1,1))` | 10, 11 | no |
| `(3,(0,0,1),(1,1,1),(2,2,1))` | 10 | no |
| `(3,(0,0,1),(1,1,2))` | 10, 11 | no |

The six exceptions are **exactly the six doubled types** — the ones the
sentence's conclusion (site fiber 1 in spite of a non-constant field) is about.
Each doubled pair costs its two shared endpoints one degree apiece, because a
pair realised in both sectors is still one link of the union.

The conclusion survives: 10, 11 and 12 all differ from 6, so the seam is
visible in the bare structure at every type and every automorphism preserves
it. Only the law is false.

**Licensed sentence.** §3.1:

> The gluing destroys edge transitivity. A shared actor carries both sectors'
> links at that site: its degree is 12 where no shared pair is adjacent in both
> sectors, and 10 or 11 where doubled pairs cost it one degree apiece, against
> 6 at every unshared actor. So the shared set is fixed setwise by every
> automorphism of the bare structure, the seam is visible without the weights,
> and the weight function is stabilised whether or not it is constant.

## MAJOR-10 — "CONFIRMS-R1" is an analogy, and six of the ten sterility rows are forced by construction

**Brief item 5.** Head segment 4: `STERILITY-CONTROL=k=0-CONFIRMS-R1`. §8:
"R1's copy-forcing theorem predicts that a disjoint union carries nothing new"
… "**R1's prediction is confirmed at this arena: the disjoint arm adds
nothing.**" G-STERILITY's statement: "R1's copy-forcing theorem **predicts
precisely this** and the arm gates it."

**Establishing reading of the parent.** R1's Theorem B (paper-01 §8.2) is
stated *under the isomorphic-copying hypothesis*: labels
{0} ⊔ B₁ ⊔ … ⊔ B_m, Σ fixing 0 and stabilising each block, an intertwiner
β_k : B₁ → B_k carrying B₁'s declared cyclic order. Its conclusions are (i) N
and N_coh are a disjoint union of m copies plus the isolated chart, (ii) the
**ratio of two quantities additive over connected components and vanishing on
an isolated vertex** is constant in m, (iii) counting quantities have the affine
form am + b. SEC's k = 0 arm instantiates none of that apparatus: there is no
refinement family, no nerve, no atlas, no Σ, no cyclic order, no m. And the
quantity SEC gates — |Aut| — is **multiplicative**, not one of Theorem B's
additive quantities; |Aut(C ⊔ C)| = |Aut(C)|² × 2 is a wreath-product fact,
independent of R1. The sentence SEC anchors the gate on ("must **divide** a
block, not copy one") is from R1's closing OPENS list, not from Theorem B.

**Establishing reading of the arm's own contingency.** Of the ten rows of §8's
table, six are forced by k = 0 before any measurement: carriers 18 = 9 + 9,
realised pairs 54 = 27 + 27, pairs beyond the sectors' own 0, doubled 0, seam
cells 0, shared actors 0 — the union relation *is* the disjoint sum, by the
construction of `combinatorial_rel` on an empty gluing. Two more (the two |Aut|
routes and the direct-sum prediction) are a theorem about disjoint unions of
isomorphic connected components. Exactly one row is genuinely contingent: the
dictionary fate `FOUND-candidate`, which required the amalgam T(0) to weld.
The pin calls this "the it-can-fail arm"; on seven of its ten rows it cannot
fail.

**Licensed sentences.** §8:

> R1's lesson is that disjoint copying cannot generate new structure — a
> refinement family that answers its question must divide a block, not copy
> one. This unit's k = 0 arm re-poses that lesson at a different object, and
> the numbers are measured object by object. [table] At k = 0 the automorphism
> group is 3359232 = |Aut(sector)|² × 2, by two routes that share no code, and
> the dictionary is FOUND and is the direct sum of the two sectors'. Six of
> those rows are forced by the empty gluing and two are a theorem about
> disjoint unions of isomorphic components; the dictionary's fate is the one
> row that could have come back otherwise, and it did not. This is a fresh
> sterility measurement at SEC's own arena and consistent with R1's lesson; it
> is **not** an instance of R1's Theorem B, whose hypothesis — a refinement
> family with Σ-stable blocks and an order-carrying intertwiner — this arena
> does not instantiate, and whose conclusions concern ratios of additive
> quantities rather than an automorphism order.

Head segment 4: `STERILITY-CONTROL=k=0-CONFIRMS-R1` → `STERILITY-CONTROL=k=0-
CONSISTENT-WITH-R1'S-COPYING-LESSON-AT-A-DIFFERENT-OBJECT(NOT-AN-INSTANCE-OF-
THEOREM-B)`.

G-STERILITY's statement: drop "predicts precisely this".

## MAJOR-11 — "the theorem does not extend" is the wrong form: paper-21's theorem was never claimed there

**Brief item 4.** §3.1: "The site assignment never goes free in this family, and
that is not what paper-21's theorem predicts one level up. At R = 3 and R = 4
the site fiber was 1 exactly at the link-constant records because the realised
relation was edge-transitive … **The theorem does not extend**, and the census
says why." Head: `THE-GLUING-BREAKS-EDGE-TRANSITIVITY-SO-THE-SEAM-IS-VISIBLE-IN-
THE-STRUCTURE-ALONE`.

**Establishing reading of the parent.** Paper-21's committed theorem (§4.5,
boxed) is "zero free items holds exactly at the link-constant records, and I7
declares none of them", and its head stamps its scope verbatim:
`SCOPE=THE-SATURATING-STRATUM(276-OF-6,146,560,000;ONE-ARENA-MEASURED-AT-356-
DRIVEN-SCHEDULES)` — a 9-actor R = 4 arena whose realised relation is K₃,₃,₃.
SEC's unions are 15- to 18-actor arenas, outside that stratum entirely. A
scoped theorem does not *fail to extend*; it was **never asserted there**, and
saying it "does not extend" invites the reading that a committed result of the
corpus has been found wanting. It has not.

Two further defects in the same sentence:

- **The R = 3 leg over-attributes an iff.** "At R = 3 **and R = 4** the site
  fiber was 1 **exactly at** the link-constant records" — at R = 3 paper-21
  reports fibers 1/1/1 at one arena whose record is (1,1,1), i.e.
  link-constant, and its own rigidity theorem makes (1,1,1) the only reachable
  I7-STRICT record at that budget. There is no non-link-constant R = 3 record
  against which the "only if" could have been tested. The iff is measured at
  R = 4 and is vacuous-plus-one-point at R = 3.
- **What SEC actually holds is stronger and should be said as such.** Read as a
  universal, the boxed biconditional now has an exhibited counterexample: at the
  6 doubled types the field is not link-constant (values 1 and 2) and the site
  fiber is 1 all the same, by two routes. That is a reason the theorem must
  carry its scope, not a defect in it — and it is the cleanest thing §3.1
  measures.

**Licensed sentence.** §3.1, replacing from "and that is not what paper-21's
theorem predicts" through "the census says why":

> Paper-21's theorem — zero free items exactly at the link-constant records — is
> committed at its own saturating stratum and asserts nothing about a glued
> arena. What carries it there is measured absent here. At R = 4 the realised
> relation is edge-transitive, so a count field invariant under all 1296 of its
> automorphisms is constant on all 27 edges, and the site fiber is 1 exactly at
> the link-constant records. The gluing destroys edge transitivity [MAJOR-9's
> degree sentence]. So the seam is fixed setwise by every automorphism and the
> weight function is stabilised whether or not it is constant — and the census
> exhibits it: at the 6 doubled types the field takes the values 1 and 2 and the
> site fiber is 1 all the same, by two routes. Read as a universal the
> biconditional would forbid that; read at its declared scope it does not reach
> it. The free item moves from the map to the labelling.

**Also rule.** "**The free item moves from the map to the labelling**" (§4.2 and
its head clause) — **LICENSED**. At paper-21's R = 4 arena
`I-SITE-ASSIGNMENT 36 / I-DIRECTION-LABEL 3 / I-ORIENT 1`; at SEC's doubled
types `I-SITE-ASSIGNMENT 1 / I-DIRECTION-LABEL 9 / I-ORIENT 4`. The map is
forced and the labelling is not, exactly as claimed — subject to MINOR-4 (there
are two labelling items free at 5 of the 6, not one). One wording note: §4.2's
"where the map was free and the **structure was rigid**" is loose — paper-21's
R = 4 relation has 1296 automorphisms and is not rigid; what was rigid was the
*count field*, forced link-constant by that symmetry. Say "where the map was
free and the symmetry forced the field".

---

# MINORS

**MINOR-1 — the window's selection principle is not in the string (brief item
7).** `@WINDOW-32-OF-45010-GLUINGS` names a size and a universe and nothing
else. A reader meeting it reads a 0.07% sample; the object is a **complete
transversal of the 16 types at both declared seed rules**, which is a
materially stronger and different thing (§2.4 states it, four sections before
the head is repeated). §15's "match every coordinate" wants the string to name
the object.
Licensed: `@WINDOW-32=16-TYPE-TRANSVERSAL-x-2-SEED-RULES-OF-45010-GLUINGS`.
Do any claims generalise beyond the 32? Only through the arena-function
identification — see MAJOR-7(a). The 4186/45010 and the alignment-criterion
census are genuinely per-gluing (I verified the criterion against the realised
relation at all 45,010; the unit checks it at 16 representatives), so §7's
sentence "The criterion is checked per PAIR at every one of the 45010 gluings
**against that gluing's own realised relation**" is a false compound of two
true facts: `doubled_free` is *evaluated* at all 45,010 (on the part profile),
and it is *validated against a realised relation* at the 16 representatives
(G-CLEAN-CRITERION, `types_checked: 16`).
Licensed: "The criterion is evaluated per PAIR at every one of the 45010
gluings, and is checked against a gluing's own realised relation at the 16 type
representatives."
*(I did run it against the realised relation at all 45,010: 0 mismatches. The
claim is true; the instrument does not make it.)*

**MINOR-2 — "AT EVERY SHARED SITE" and "12 UNDETERMINED ENTRIES" are 3 measured
and 4×3 typed.** G-SEAM-RANK's statement says "at every shared site … measured
object by object"; its evidence is `{"seams": 3}`, each read at the gluing's
**first** shared site (`s0 = gl[0]`). And
`seam_undetermined_entries` is the literal `4 * 3` (sec_exact.py:2517). Both are true — I
verified rank 6 / kernel 4 at all 39 shared sites, and the rank is a property of
the six declared directions, independent of every count (the A-rows touch only
q₁₁,q₁₂,q₂₂ and the B-rows only q₃₃,q₃₄,q₄₄). But a one-line proof is owed
where a universal is asserted from three witnesses, and "the seam carries 12
undetermined entries" should say it is 4 measured at one site times 3 shared
sites, with the three per-site forms never checked for mutual consistency.
Licensed: "the six declared directions give rank 6 on the ten entries of
Sym²(Q⁴) whatever the counts, so the kernel is 4 at every shared site; measured
at three seams and proved by inspection of the row space" and "3 shared sites ×
4 entries = 12 undetermined entries, one system per site, with no cross-site
consistency condition imposed or measured."

**MINOR-3 — the direct-sum chart names a doubled link twice, and §6.1's
determinant comparison rests on it.** At every shared site whose count vector
contains a 2, the A-direction carrying it and the B-direction carrying it are
**the same union link** — measured at 8 of the 39 shared sites, i.e. at every
site incident to a doubled pair. So at a TRIANGLE seam the system imposes
Q(a₂) = 2 and Q(b₂) = 2 on one link, which is **CHARTED individuation** — the
declaration §2.2 says the record cannot make and §4.3 calls "declaring away the
thing the seam measures". §6.1's closing note ("the triangle seam's direct-sum
minors are all 1 where the aligned seam's are 1, 3/4, 3/4, 9/16, so the doubled
link … moves its determinant") compares a 6-distinct-link seam against a
5-distinct-link seam charted as 6. §13.5 prices the seam chart but not this;
item 11 of the choice inventory does not name the individuation, and item 8
binds it only to `EXT-INCIDENCE`.
Licensed: add to §6.1 — "At a seam incident to a doubled pair the direct-sum
chart gives one union link two direction vectors, one per chart; the seam
system there is read under CHARTED individuation, and the determinant
comparison below is a comparison of two charted seams, not of two records." And
reclassify item 8 as binding at §4.3 **and** §6.1.

**MINOR-4 — "THE-FREE-ITEM-IS-ALWAYS-I-DIRECTION-LABEL" is singular where the
measurement gives two.** At 5 of the 6 doubled types the inventory is
`I-DIRECTION-LABEL: 9, I-ORIENT: 4` — two free items; only
`(3,(0,0,1),(1,1,1),(2,2,1))` has `I-ORIENT: 1`. §4.1's table row reads "free
item | `I-DIRECTION-LABEL` | 9" for all six. §11 item 14 discloses "I-ORIENT |
measured | 1 or 4", so the datum is in the paper — the table and the head are
where it goes missing.
Licensed head clause: `THE-FREE-ITEMS-AT-A-DOUBLED-TYPE-ARE-I-DIRECTION-LABEL(9)
-AND-I-ORIENT(4-AT-5-OF-6,1-AT-1-OF-6),NEVER-I-SITE-ASSIGNMENT`.
Also: "free item" is used in two senses in §11 — the RSQ inventory's, and "Two
free items, both instrument-side" (items 15 and 16). Rename the second
"instrument-side free choices".

**MINOR-5 — `SITE-FIBER=1-AT-16-OF-16-TWO-ROUTES` is contentful at 6 of the 16.**
Route A is |Aut| / |Aut_w|; at the 10 doubled-free types the weight is constant
1, so |Aut_w| = |Aut| and the quotient is 1 identically. Route B is
`orbit_of_edgeset(gens, Dset)` with `Dset` the doubled-edge set; at the same 10
types `Dset` is empty and the orbit of the empty set is 1 by inspection. Both
routes are vacuous at 10 of 16. The measurement has content — and is a real
result — at the 6 doubled types.
Licensed: "the site-assignment fiber is 1 at every one of the 16 types, by two
routes: forced at the 10 doubled-free types, where the field is constant and
both routes read a trivial object, and measured at the 6 doubled types, where
the field is not constant and the fiber is 1 all the same."

**MINOR-6 — the seed rule is priced, but not where a departure from a parent's
convention belongs, and it is called the wrong thing.** The shared-seed rule is
disclosed three times (head, §2.1, §3.2) and classed **declared** at fiber 2 in
item 7 — so it is not hidden. Two defects remain. (a) It is **absent from §13
Deviations**, which is where a departure from paper-19's canonical rule
belongs; it is the departure that turns 6 REFUSED into 6 FORCED. (b) §3.2 calls
it "**the gluing's own freedom**" and G-SEED-RULE's statement calls it "a
genuine variable **of the gluing**" — it is a variable of the **driver**, not of
the gluing, and §5.2 uses the same phrase "the gluing's own freedom" for a
different object (the 45,010-to-16 collapse).
What should be said, and is not said anywhere: **no geometric claim in this
paper depends on the seed rule.** The dictionary, type, seam, compatibility and
alignment censuses all run off `combinatorial_rel`, which never reads a seed.
The seed rule decides drivability and nothing else.
Licensed, as a new §13 deviation: "**The shared-seed rule is this unit's, not
paper-19's.** Paper-19's canonical rule refuses at 6 of the 16 driven window
records; the shared-seed rule drives all 16. Price: the FORCED column is
reported at a rule the parent does not declare, and the refusals are recorded
and never patched. Mitigation: no geometric claim in this paper reads the seed
rule — the dictionary, type, seam, compatibility and alignment censuses are all
computed from the schedule alone, and the driven and combinatorial routes agree
at 26 of 26 FORCED window records."

**MINOR-7 — §12's readout gives the type fraction and withholds the gluing
fraction.** "the union welds — zero free items — at 10 of them [the 16 types]".
10/16 of types is 4186/45010 of gluings; §10 warns explicitly that "the type
populations differ by more than two orders of magnitude" and that no likelihood
reading is licensed. The head carries both numbers; the plain-English readout,
which is what travels, carries only the flattering one.
Licensed: "…and the union welds — zero free items — at 10 of the 16 types, which
are 4186 of the 45010 gluings; the two fractions are counts over different
universes and neither is a likelihood."

**MINOR-8 — `SEC-COMPOSES` would have fired at 1 of 16.** The comparator's
branches 2 and 3 both emit `SEC-COMPOSES`, so the word's threshold is "at least
one motivated type". That is disclosed by the bracket's
`MOTIVATED-AT-10-OF-16-TYPES` and is consistent with the pin's own definition
of the word (the union dictionary's existence), so I do not re-rule the word —
but the threshold should be stated in §13, since a reader will take "COMPOSES"
to be a strong verdict.

**MINOR-9 — walls.** L-1 absent and gated with the #125 normaliser ✓. The seam
resonance NAMED and gate-required ✓ — §6.1's naming paragraph is correct and
must not be softened. No sector narrative: the 14-term scan runs on both
surfaces with 0 hits ✓, and the provenance exclusion is named ✓. BHS/K-R: no
dimension reading taken ✓, and the catalog quote verifies verbatim ✓.
E-24: the COUNTING-ONLY stamp is in the receipt, no probability or percentage
is published, and **every one of the eight fractions in the paper names its
universe numerically** (6 of 16, 4186 of 45010, 32 of 45010, 2970 of the 42336,
26 of 26, 2 of the 3, 10 of the 16, 10 of 16) ✓. The only E-24-adjacent defect
is MINOR-7's asymmetry and MAJOR-3's misnamed universe ("6 of 16" is 6 of 16
records, not 6 of 16 types).
E-22: fenced blocks gated by multiset equality with a stray side ✓; inline
spans in coverage ✓. E-23: 30 mutants, each on-target, every gate falsified or
waived with a forcing — but see MAJOR-8: `MUT-PAPER-TABLE` demonstrates table
protection only inside the covered families.
**Not-licensed-list (AID-inherited) — identity language:** the paper uses no
"is really", "nothing but", "the same thing as" construction; the one identity
sentence, "the union's co-division relation **is** I7's own Cayley incidence"
(§1), is a quotation of paper-19 about the sector, not a claim about the union.
Clean.

**MINOR-10 — the pin's Stage 3 wording is answered slightly off-target.** The
pin asks "do the shared actors' links carry consistent counts from both sides
(the compatibility census); **what freedom the gluing itself carries** (priced)".
§5.2 prices the 45,010→16 collapse as the freedom. That is a fair answer, but
the freedom the pin's Stage 3 names is the freedom *at the seam*, which §6.1's
four undetermined entries answer. Cross-reference §5.2 to §6.1.

---

# WHAT SURVIVES UNAMENDED

A hostile seat should say what it could not break.

1. **"The direct sum is a declaration, not a measurement."** Licensed exactly
   as written, and stronger than the paper knows: rank 6 / kernel 4 holds at all
   39 shared sites of the 16 type representatives and is independent of every
   count. The exhibited indefinite completion reproduces all six counts exactly
   and is negative on [2,1,−1,−2], while C = 0 is positive definite by exact
   Sylvester minors 1, 3/4, 3/4, 9/16. This is the unit's result.
2. **The NAMED-AND-NOT-READ paragraph** in §6.1. It refuses the Lorentzian
   resonance in the exact place a reader would take it, and it is gate-required.
   Model discipline; keep verbatim.
3. **The alignment criterion.** "The union welds iff no shared pair is adjacent
   in both sectors, i.e. iff every shared pair shares a tripartite class on at
   least one side." I verified it against each gluing's own realised relation at
   all 45,010 gluings: 0 mismatches. The k = 3 closed reading and 2970 of 42336
   reproduce exactly. This is a clean, exhaustive, correct result.
4. **`SEC-K-SELECTED` is genuinely the wrong word for the world** — whatever
   MAJOR-1 says about how the instrument reached it. k = 2 and k = 3 each carry
   both a welding and a non-welding type; k is not what selects. The
   *finding* is right; only its derivation is unmeasured.
5. **"The extended carrier repairs the seam by declaring away the thing the
   seam measures"** (§4.3) and **§2.2's** "A division event knows an actor pair
   and nothing else, so the record can only ever make the SIMPLE distinction".
   Both correct, both load-bearing, both to be kept.
6. **The type census**, every cell of it, and **all 16 automorphism orders** —
   reproduced by an independent backtracking counter and, at 8 types, a third
   time by hand as wreath and stabilizer orders.
7. **The cited-not-read discipline** for LOR (§1): the abstention is gated on
   the run's read set rather than announced, and the citation is at a pinned
   sha. Correct #91 practice under a concurrently-rewritten sibling.

---

# SUMMARY TABLE OF RULINGS

| # | claim as delivered | ruling |
|---|---|---|
| MAJOR-1 | segment-4 word `TYPE-SELECTED-NOT-k-SELECTED`; §13.3 declination | **not measured** — word typed, no comparator, k-claim unbound by any predicate |
| MAJOR-2 | §14 "types all four templates itself" | **false about the instrument** |
| MAJOR-3 | "REFUSED 6 OF 16" / "6 of them" as a type statement | **wrong referent** — the canonical-rule fate moves with the free representative (HP-1); the shared-rule clause survives (HP-3, 0 of 15) |
| MAJOR-4 | `EXT-INCIDENCE-REPAIRS-EVERY-TYPE`; "the induced field becomes identically 1" | **unmeasured; mechanism contradicted by the receipt** |
| MAJOR-5 | "a sector's own geometry is changed by an event in the OTHER sector" | **not licensed** — deformation confined to shared-shared cells; no test declared |
| MAJOR-6 | "geometry at the seam is available ONLY by leaving the target" | **"only" not licensed**; contradicts S-3. Forward half upgradable to a theorem |
| MAJOR-7 | §13.2 "gated as a per-type check"; §5.2 "16 union arenas" | **ungated (though true); and 12, not 16** |
| MAJOR-8 | §14 "every data row of every table is a rendered claim" | **false at 56 of 131 rows**, incl. the whole §5.1 compatibility census |
| MAJOR-9 | "a shared actor has twice the degree of an unshared one" | **false at 6 of 15 types** — the conclusion survives |
| MAJOR-10 | `k=0-CONFIRMS-R1` | **analogy, not confirmation**; 7 of 10 rows non-contingent |
| MAJOR-11 | "paper-21's theorem does not extend" | **wrong form** — it was never claimed there; the *mechanism* is measured absent, and SEC holds a counterexample to the universal reading |
| MINOR-1..10 | window string, seam universals, chart double-naming, free-item count, fiber routes, seed-rule pricing, readout asymmetry, COMPOSES threshold, walls, pin Stage 3 | as ruled above |

**Head segments carrying a repair order: 1, 2, 3, 4 — all four.**
**Body sections carrying a repair order: 3.1, 3.2, 4.1, 4.3, 5.1, 5.2, 6.1,
6.3, 7, 8, 11, 12, 13, 14.**

Every ruling above is a candidate reading until adjudication.
