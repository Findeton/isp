# OCC (paper-31) — K2 EFFECTUS REVIEW

**Seat:** K2, effectus lens (what is *licensed*; scope, register, inheritance,
cross-unit sentences; the head as the thing the ledger and the successors will
quote).  **Protocol:** v14 ledger #256, row K2.  **Object:** commit `7ab2f21`.
**Panel state:** OCC delivered-not-terminal; LOR delivered-not-terminal; **no
LOR reviews are committed anywhere in the repo or its history** (checked
`v14/review-lor-*.md` on the worktree and across all refs), so §R3 rules on
LOR's *delivered artifacts* at `2369290` only.

**Hashes, verified at start and at end** (sha256-12, worktree against
`git show 7ab2f21:`):

| object | hash | start | end |
|---|---|---|---|
| `v14/paper-31-occ.md` | `1b140f7973d4` | ✓ | ✓ |
| `v14/code/occ_exact.py` | `e96c1e14a0b6` | ✓ | ✓ |
| `v14/code/occ_output.txt` | `63d98f4ee6f0` | ✓ | ✓ |
| `v14/code/occ_receipt.json` | `46e757ef9c47` | ✓ | ✓ |
| `v14/note-occ-pin.md` (pin) | `145db72ce547` | ✓ | ✓ |

Worktree clean for all five at close; no repo write other than this file.

---

## GRADE: AWF (accept with fixes)

**58 independent recomputations**, rebuilt from the declared arena
(`Z₃²`, the three declared link directions, the committed walk form) without
importing the instrument, plus four purpose-built probes that import it
read-only.  **Every computed number in the receipt that I could reach is
correct.**  The arena, the pool, the four configuration spaces, all 48 leak
rows at both grains and both shapes, the two-route agreement, the 405
both-nonzero cells, the asymmetry census, all six control arms, the parent
split cited from paper-22's receipt, and the P2/P3 rows all reproduce exactly.
The verdict word `OCC-CEILING-OPEN` is correct and survives every finding
below.

The grade is AWF and not A because **one sealed, gated, load-bearing claim
(C09) is false as written**, one head clause is refuted by the unit's own
verbatim anchor, and the head's second-largest numeral (53,460) is produced by
an instrument that cannot fail — the precise defect paper-22's own K1 review
prescribed a repair for, reintroduced here in a stronger form.

The grade is not R because none of the three touches the verdict, the premise
words, the two-way control, or the asymmetry rows, and every repair is a
re-naming or a demotion — no measurement has to be re-run.

---

# PART I — THE FINDINGS

## MAJOR-1 — C09 is false as written: the leak sources are the **same-site** configurations (27), not "the configurations whose two excitations sit on cells sharing an actor" (135)

This is the decisive finding and it is a *referent* error, not an arithmetic
one.

**What is published.**  Claim C09, sealed, rendered from the run and gated to
occur exactly once in the paper:

> the configurations that leak are exactly the 27 whose two excitations sit on
> cells sharing an actor, by set equality at 5 of 5 leaking coin classes

and, carrying the same referent, the head field
`CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-ACTOR-CONFIGURATIONS=5-OF-5`, §9's
bullet "the two leaks are the same phenomenon seen twice", the receipt key
`/leaks/set_equalities/*/carrier_grain_sources_are_the_same_actor_configurations`,
the gate statement of `G-P4-SET-EQUALITY` ("*that set IS the set of
configurations whose two excitations sit at one actor*"), and ledger #255's
bold headline "**THE TWO GRAINS ARE ONE PHENOMENON** (the carrier-grain leak's
source set = exactly the 27 same-actor configurations, set equality at 5/5)".

**What is measured.**  `occ_exact.py:1480` tests
`r_carrier["source_set"] == same_site_cfgs`, where `same_site_cfgs` is built at
line 1468 from `CELL_SITE[a] == CELL_SITE[b]` — pairs of cells sharing a *base
site*.  The set named in the claim, `same_actor_cfgs`, is built two lines
earlier from `share_an_actor` and is **never compared to anything**; only the
weaker, unpublished `carrier_grain_sources_share_an_actor` uses it.

Recomputed independently, at every one of the 5 leaking coin classes:

| object | count | measured |
|---|---|---|
| carrier-grain symmetric leak source set | **27** | 5/5 coins |
| `= same-SITE configurations` | 27 | **TRUE at 5/5** |
| `= same-ACTOR configurations` | 135 | **FALSE at 5/5** |
| `⊂ same-ACTOR configurations` | 27 of 135 | TRUE at 5/5, **strict** (108 excluded) |

The receipt refutes its own key three paths apart:
`/arena/same_actor_configurations = 135` beside
`/arena/same_site_configurations = 27`, while the boolean named
`..._are_the_same_actor_configurations` is the 27-set's equality.

**Why nothing caught it.**  Every layer of the apparatus is value-bound or
label-bound, and none is referent-bound.  The de-twinned comparator maps the
head *label* to a receipt *path* (`occ_exact.py:1593`) and compares values, so
a mis-named path is transparent to it.  `G-VERDICT-NO-TYPED-LITERAL` and
`G-PAPER-NUMERAL-COVERAGE` license the numeral `27` from any of
`/arena/cells`, `/arena/co_division_pairs`, `/arena/same_site_configurations` —
I confirmed all three carry it.  `G-PAPER-CLAIM-POLARITY` negates the claim's
verb, not its noun phrase.  No mutant can move a name.  **This is the era's
first measured instance of a false claim passing a complete
value-bound gate stack**, and it should be engraved as such.

**What dies.**  The "one phenomenon" reading.  The relation between the two
grains is a *strict containment*, not an identity: every carrier-grain leak
source is actor-grain forbidden, but only 27 of the 135 actor-grain forbidden
configurations are carrier-grain leak sources.  §6's own next sentence has the
correct mechanism ("*a row of the walk operator is supported on the three cells
of one site, so the only sources that can reach a doubly occupied cell are
pairs drawn from those three, and those pairs share an actor*") — the paper
knows the object and mis-names it one sentence earlier.

**What survives.**  The verdict; P4 at both grains; the asymmetry rows; the
strict-containment reading, which is a real and interesting result.

**REPAIR (exact).**
1. C09 → "*the configurations that leak are exactly the 27 whose two
   excitations sit on cells of one site — a strict subset of the 135 the
   actor-grain declaration forbids — by set equality at 5 of 5 leaking coin
   classes*".
2. Head field → `CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-SITE-CONFIGURATIONS=5-OF-5`,
   and add `CARRIER-GRAIN-LEAK-SOURCES-ARE-ACTOR-GRAIN-FORBIDDEN=27-OF-135`.
3. Receipt key → `carrier_grain_sources_are_the_same_site_configurations`;
   promote `carrier_grain_sources_share_an_actor` to a published, gated row
   with its own numerator/denominator.
4. `G-P4-SET-EQUALITY`'s statement → name the same-site set and state the
   containment as strict, with 108 as the measured gap.
5. §9's "*the same phenomenon seen twice*" → "*the carrier-grain leak is
   strictly contained in the actor grain's forbidden set, 27 of 135: the
   actor-grain exclusion is strictly stronger than closing the carrier-grain
   leak requires*".
6. **Ledger erratum required** on #255's bold headline (see §R2's ruling on
   in-ledger ownership).

---

## MAJOR-2 — "a grain the record layer never names" is refuted by the unit's own verbatim anchor

The head thesis segment carries
`THESIS=EXCLUSION-SELECTS-ONLY-AT-THE-CARRIER-S-OWN-GRAIN`, and the paper's
summary and §9 gloss it as

> the carrier's grain is one the record layer **never names**
> … at the carrier, where **nothing in the record layer has ever spoken**

and ledger #256 hands me that sentence as the licensed asymmetry sentence.

**It is false, and the unit itself measures it false.**  Verbatim anchor
`VB-DICT`, located in `A-W3` (paper-19, terminal) and consumed by
`G-P1-DICTIONARY`, is:

```
WELD3-FOUND-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|DIVISION-COUNT->n_l(x)]
```

The record layer's forced dictionary **names the carrier's grain explicitly**,
as the co-division actor pair, and gives it a target — the link.  The committed
coupling receipt carries the key `/arena/realised_pairs = 27` (path-value
anchor `PV-PAIRS`).  §3 of the paper says so itself: "*the leg that does reach
them is the dictionary's second: CO-DIVISION-ACTOR-PAIR→LINK … whose target is
exactly the set the walk's amplitudes live on*."

**What the P2 census actually measures** is narrower and is the licensed
statement: 4,945 published names across 6 committed layers, **none
occupancy-shaped**, with a 19-hit positive control on paper-22's receipt.  That
is an absence of an *occupancy coordinate*, not an absence of the *grain's
name*.  §8 gets it right — "*The record layer speaks of actors, links and
counts.  It has nothing to say about how many excitations a link may carry*" —
and the summary and §9 overreach past it.

**REPAIR.**  Everywhere ("What rides what", §9's *Not decided* bullet, and the
ledger's licensed sentence): "*a grain the record layer names — it is the
weld's own CO-DIVISION-ACTOR-PAIR→LINK leg — but never equips with an occupancy
coordinate*".  The sharpness is not lost; it is relocated to where it was
measured.  Adopt §8's wording verbatim as the canonical form.

---

## MAJOR-3 — the declaration fiber's 53,460 comparisons cannot fail, and the defect is one paper-22 already repaired

`P2-ONE-EXCITATION-RESTRICTIONS-AGREE=53460-OF-53460` is the head's second
largest numeral; C05 and §9's second *Decided* bullet both carry it; and
`fib["restrictions_agree_as_objects"]` is one of the **three legs from which
P2's verdict word is derived** (`occ_exact.py:2841`).

`p2_fiber` (line ~1071) builds, for each coin and each declaration,
`objs[did] = one_excitation_object(W)` — **a call with no declaration
argument**.  It then compares `objs[a]` with `objs[b]`.  The two sides are the
same pure function of the same `W`.

I probed it directly (`fiber_probe.py`, importing the instrument read-only):

| declaration list | comparisons | disagreements | theories |
|---|---|---|---|
| as shipped | 53,460 | 0 | 3 |
| all four declarations made **identical** | 53,460 | 0 | 1 |
| grains and ceilings reshuffled | 53,460 | 0 | 3 |

`inspect.signature(one_excitation_object)` is `(W)`.  The number is invariant
under every possible change to the object it claims to measure, including
collapsing the fiber to a single declaration.  `MUT-FIBER` moves
`fiber_disagreements` at the *gate* layer, which is exactly the mutation that
cannot expose this.

The underlying mathematics is **true and trivial**: a single excitation
violates no ceiling ≥ 1 at any grain, so every declaration restricts to the
free one-cell theory.  What is not licensed is presenting it as a
53,460-comparison measurement and consuming it as a live leg of a derived
verdict.  P2's derivation is effectively two-legged, contrary to
`G-P2-TURNING`'s published statement.

**The precedent.**  `v14/review-r4c-operator.md` MINOR-3, on this unit's own
parent:

> ### MINOR-3 — the decisive fixed-point gate compares a constant with itself.
> … The gate binds a cardinality (16 == 16), not the objects (#87), and no
> mutant that actually changed one restriction could die there. …
> **Repair.** Build the one-excitation restriction *from each occupancy
> declaration* as data — configuration set, per-generator transition matrix,
> Born shadow — and gate object-by-object equality across all 64 generators

paper-22 implemented it: `r4c_multi_exact.py:1905` `one_excitation_configs(ceiling)`
derives the set **from the declaration**, and its docstring says "*instead of a
cardinality compared with itself (K1 MINOR-3)*".  OCC then **cites paper-22's
repaired number** (`PV-P22-AGREE = 64`) as a path-value anchor into the very
gate that publishes its own unrepaired one.  The repaired gate's *shape* was
copied (configuration set, transition matrix, Born shadow, object by object,
every coin) without its substance.  A closed era disease, reopened.

**REPAIR — either of two, the second preferred.**
1. Derive the restriction from the declaration: `one_excitation_object(W, grain,
   ceiling)` with the configuration set `{c : {c} is admitted}` and the induced
   matrix, and add a ceiling-0 or per-cell declaration to the menu so the
   comparison has a way to fail; or
2. **Demote the row from a measurement to a one-line theorem** — "*a single
   excitation trips no ceiling ≥ 1 at any grain, so every declaration in the
   menu restricts to the same one-cell theory*" — delete `53,460` from the head,
   from C05 and from §9, reduce P2's published derivation to its two live legs,
   and keep the fiber's real content, which **is** measured: the 4 → 3 collapse
   (`distinct_two_excitation_theories` genuinely varies with the declaration —
   verified: it drops to 1 under my identical-declaration probe).

Note also that `53,460` is **not** among `G-COUNTING-ONLY`'s four re-counted
enumerations, so E-24's denominator re-count does not reach it.

---

## MINOR-1 — §1's ingredient count contradicts §5's own verdict on P3

§1: "*Two of those three are present on the committed arena.  The missing one
is the first.*"  On the verdict arena A0, P3 is
`SILENT-AND-VACUOUSLY-SATISFIED` and §5 says of it "*A premise that holds
because the question is invisible carries no force into the conclusion*", while
the head's P4 on A0 is `NO-SHAPE-CLOSES`.  Exactly one ingredient — the pool,
read at the carrier's grain — is present in a form that carries force.

**REPAIR.**  "*One of those three is present in a form that carries force: the
pool, at the carrier's grain.  The closure requirement is satisfied but
vacuously and carries none.  The representation is absent, and it is the one
that decides.*"

## MINOR-2 — `G-PAPER-TABLES` names three tables and binds four

The gate statement and §10 both say "the 23 rows of the three load-bearing
tables — the pool at both grains, the six arms, and the four declarations".
Those three tables have 6 + 6 + 4 = **16** rows.  The 23 gated rows include the
seven `T-CHOICE-*` rows of the choice inventory, which the statement omits.
The measurement is *stronger* than its description; the description is
arithmetically wrong.

**REPAIR.**  "*the 23 rows of the four load-bearing tables — the pool at both
grains, the six arms, the four declarations and the choice inventory*".

## MINOR-3 — `P2-ONE-EXCITATION-RESTRICTIONS-AGREE` is rendered as `N-OF-N` from one variable

Independently of MAJOR-3: `occ_exact.py:1627` builds the field as
`pair(one_excitation_comparisons, one_excitation_comparisons)`.  The numerator
is not the agreement count.  If the repair of MAJOR-3 keeps any such field, it
must read `pair(comparisons - disagreements, comparisons)` so the head carries
the measurement rather than a tautology.  Same defect in the gate statement of
`G-P2-INVISIBLE-FROM-BELOW`, which prints `com(comparisons)` twice.

## MINOR-4 — the head's SCOPE omits two of the choice inventory's own axes

`SCOPE=` carries eleven clauses but not the two that the unit's own inventory
marks as fibered choices bearing on the result: **the free lift**
(`the two-excitation lift | fiber 3 | INHERITED-AS-DECLARED`) and **the declared
grain menu** (`the grain a ceiling is declared at | fiber 2`).  §9 states the
first in prose; neither reaches the head, and the head is what FCK and the
ledger will quote.

**REPAIR.**  Add `FREE-LIFT-ONLY(U-TENSOR-U)` and
`GRAIN-MENU-AS-DECLARED` to the SCOPE field.

## MINOR-5 — the blindness pair is one witness stated universally

§5: "*The rule cannot tell a doubly occupied carrier from two singly occupied
ones sitting at one actor*".  Measured: one constructed pair (`P = {cell 0,
cell 1}`, `Q = {cell 0, cell 0}`), agreeing on the site field at 9 of 9.  The
two cells chosen share a *base site*, which is the strongest case for the
claim, not a generic one.  The existential is enough for P3's vacuity (which
rests on `0 of 3 completions refuse`), so nothing is lost by saying it
honestly.

**REPAIR.**  "*A witness pair is built and the committed rule cannot separate
it: …*" — or census the site field over all 27 doubly-occupied configurations
against their same-site partners and publish a ratio.

---

# PART II — MY ASSIGNED ROWS

## R1 — THE HEAD'S LICENSURE

### Is the TWO-COORDINATE form the licensed statement of what a ceiling-declaration costs?

**YES, at the declared menu — and the fiber "4 declarations → 3 theories → 3
completions" is the right price.**  What is measured supports it exactly: the
outcome is a function of the *pair* (grain, value) and of neither coordinate
alone.  At `(CARRIER, 1)` exclusion selects at 5 of 6; at `(ACTOR, 1)` at 0 of
6; at ceiling 2 nothing selects at either grain.  A ceiling-declaration on this
arena cannot be *stated* without naming a grain, because the excitation's
coordinate (a cell) and the record's coordinate (an actor) are related by a
2-to-1-and-6-to-1 incidence rather than a bijection — measured 27/27 and 9/9.
That is the real content and it is licensed.

**Three qualifications the licensed sentence must carry.**

1. **The menu, not the universe.**  "The ceiling is two declarations" is
   measured over a *declared* 2×2 menu.  I extended it.  The unit's own
   `same_site` set exhibits a **third grain** — `CELL_SITE`, a genuine
   *function* cells → 9 objects, unlike the ACTOR "grain", which is a
   *relation* (every cell has two actors, so "one per actor" is really "no two
   on cells sharing an actor").  I built the site-grain declaration and ran the
   full census (`third_grain.py`):

   | grain | ceiling-1 admissible | selects | no shape closes |
   |---|---|---|---|
   | CARRIER | 351 | **5 of 6 coins** (ANTISYMMETRIC) | 0 of 6 |
   | SITE (new) | 324 | 0 of 6 | **6 of 6** |
   | ACTOR | 216 | 0 of 6 | **6 of 6** |

   **The head's "ONLY" survives the extension.**  That is a corroboration the
   unit did not earn and should now take.

2. **And it survives for a reason that is a theorem, not a census.**  Under a
   hard core at grain *G*, the *antisymmetric* sector's forbidden set is
   `{distinct pairs {c,d} : c,d collide under G}`, which is **empty iff G is
   the carrier's own grain** — the wedge carries no doubly-occupied cell, so at
   the carrier grain it has nothing to leak into and closes automatically,
   while at any strictly coarser grain the forbidden set contains distinct-cell
   pairs, which the wedge does carry.  The mechanism that makes exclusion
   *selective* is therefore available at the carrier's grain and structurally
   nowhere else; whether a coarser grain nonetheless selects becomes a
   measurement, and it does not — 6 of 6 at both coarser grains now tested.
   **This is stronger and more general than the delivered 2-point census and I
   recommend the unit adopt it**, with the census as its residual.

3. **The value coordinate is informative at one of its two points.**  At two
   excitations, ceiling 2 is the null declaration at either grain (verified:
   `D-CARRIER-2` and `D-ACTOR-2` are the same theory, 378/351).  So the
   "value" axis carries one bit — *constrain or don't* — and its generality is
   S-4, untested.  The two-coordinate claim should say `TWO-COORDINATE
   (GRAIN × VALUE) AT TWO EXCITATIONS`, not as a claim about ceilings in
   general.

**Licensure verdict:** the two-coordinate form is **LICENSED-AT-THE-DECLARED-
MENU**, upgradeable to **LICENSED-BY-MECHANISM** on adopting the wedge-closure
theorem above.

### Is "fermionic-shape is not a theorem of the coupled theory HERE" properly scoped?

**Yes, and it is the best-scoped clause in the unit.**  §9 carries "*at this
arena*", "*paper-22's own arena is untouched by anything here*", "*It remains
available as a declaration at the carrier's grain, at 5 of 6 coin classes*",
and the shape-word wall holds (I scanned the object: `fermionic-shape`,
`bosonic-shape`, `no-particle` are the only compounds; no spin, no relativity,
no cosmology, no continuum, no particle noun).  The arena relativity is real
and correctly drawn: paper-22's carrier is 16 objects it calls sites and its
ceiling is at *that* grain; OCC's is 27 cells; S-5 states the one-way
inheritance and says the transport was checked coin by coin.

**One over-scope in the other direction, and it is an under-claim.**  The head
scopes to `THE-WELDED-LANDING-RECORD`.  I tested whether it needs to
(`record_probe.py`): the count field enters the walk only as
`diag(ω^{n_l(x)})`, a unit-modulus diagonal, which cannot turn a zero into a
nonzero.  Re-running the full leak census at `n ≡ 0`, `n ≡ 2` and two random
fields over all 27 cells returns **byte-identical rows at all six coins**
(81/864/135 and the monomial 0/81/81 throughout).  The P4 result is
**record-blind across the entire 3²⁷ admissible count-field family**, not
merely at the welded landing record.  The head advertises a boundary the
measurement does not have; the real boundaries are the coin family and the free
lift.  This is a licensed strengthening and it is also, notably, an instance of
paper-20's own staleness-blindness family (see R5).

---

## R2 — THE MISTYPED-NOT-FALSE RULING

### What the adjudication must own

**The pin's P1 is an orchestrator design error and must be owned in-ledger, in
the established form.**  The pin (`145db72ce547`, P1) asks whether the
ACTOR→SITE map is a bijection "*ON THE ARENA THE EXCITATIONS USE (the coupled
machine's 9 sites)*".  The parenthetical is simply wrong: the coupled machine's
own instrument declares `NCELL = 27`, `DIM = 27` (`coupling_exact.py:749–750`),
and its own source says "*Cell (x, l) IS the unordered co-division pair
{x, x+l}*" (anchor `VB-CELL`).  The excitations use 27 cells.  The measurement
corrected the pin, and the paper owns it cleanly in §3 ("*The pin … names the
nine sites as that arena.  Measured, it is not*").

**Precedent for the form is in-repo and exact.**  Ledger #2154's
`ADJUDICATOR'S PIN ERROR (my §4 silently converted §3.2's …)` with the
CORRECTED SETTLEMENT stated in the same entry; #286's `ADJUDICATOR'S OWN
ACCOUNT: the pin's gateway criterion was degenerate BY DESIGN (mine); the pin's
invariant wording ambiguous (mine)`; #6785's `the orchestrator's error, owned`.

The adjudication must therefore carry a clause of the form:

> **ORCHESTRATOR'S PIN ERROR, OWNED.** P1's parenthetical "(the coupled
> machine's 9 sites)" mis-named the excitations' arena; the coupled machine's
> committed instrument declares 27 cells and identifies a cell with the
> unordered co-division pair.  The error was the pin's, i.e. mine.  The unit
> measured through it rather than around it, and P1 is *strengthened* by the
> correction, not weakened: the weld does weld the excitations' arena, with
> fiber one, through its second leg.

### Does the seed conditional survive RETYPED?

**Half of it survives; the other half is worse off than "mistyped".**

**The corrected conditional, stated:**

> **weld `CO-DIVISION-ACTOR-PAIR→LINK` bijection [SUPPLIED — measured, fiber 1,
> 27/27 both directions]** + **a two-excitation representation carrying a hard
> core at the LINK [NOT SUPPLIED — the committed representation has no
> two-excitation object at all; 4,945 names, 0 occupancy-shaped, 0
> excitation-number parameters]** + **a closure requirement that refuses a
> division to a doubly-occupied link [NOT SUPPLIED — 0 of 3 completions refuse;
> the emission rule's site field agrees at 9/9]** + **a pool member whose
> symmetric square leaks out of the link hard core [SUPPLIED at 5 of 6 coin
> classes; the wedge closes at 6 of 6]** ⟹ **the antisymmetric shape is the
> only closed sector at 5 of 6 coin classes.**

Two of four premises are supplied by committed layers, and the two that are not
are **the same missing object seen twice**: an occupancy coordinate on the
link.  So the retyped conditional reduces to a single missing declaration —
"how many excitations may one link carry" — which is precisely S-1.  That is a
sharper and more useful handoff than the original four-premise chain, and it is
what FCK should inherit.

### The ruling on the word "mistyped-not-false"

**"MISTYPED-NOT-FALSE" is half the story and the ledger word should change.**
The seed conditional is mistyped *at the carrier*: its injection premise names
actors, and the excitation-to-actor relation is not a function (2 actors per
cell at 27/27), so as a description of this representation it does not denote.
That is the delivered ruling and it is correct.

**But the unit also measures what happens if you insist on the grain the seed
conditional typed** — that is exactly arm `A2-DECLARED-EXCLUSION-AT-THE-ACTOR-
GRAIN`.  Supply the actor-grain injection *as a declaration*, keep P1, keep P3,
keep the full pool, and the conclusion **fails**: both shapes leak at 6 of 6
coin classes, all 216 admissible configurations leak, all 135 forbidden ones
are reached, and the head law returns `OCC-CEILING-PARTIAL`, not `FORCED`.  A
conditional whose antecedent is satisfiable by declaration and whose consequent
is then false is a false conditional.

**Licensed ledger word:**
`MISTYPED-AT-THE-CARRIER; REFUTED-AT-THE-GRAIN-IT-TYPED` — with the two clauses
carrying different evidence (a type measurement, 27/27 + 9/9; and a leak
measurement, arm A2 at 6/6).  §8 comes within one sentence of saying this
("*Push the exclusion up to the actor … it stops selecting and starts
destroying*") and the head never draws it.  **This is the unit's strongest
result and it is currently under-claimed.**

---

## R3 — THE LOR CONVERGENCE

**State of the panel.**  Both units are **delivered, not terminal**; all
readings on both sides are candidate.  **No LOR review is committed** (verified
across the worktree and all git refs) — so there is nothing of LOR's panel to
reconcile with, and this row is decided on LOR's delivered artifacts at
`2369290` (`f3e9e9df2c70`) plus ledger #252.

**The material fact.**  LOR: the refinement's new sites are the co-division
pairs, `SITE ← ACTOR ⊕ CO-DIVISION-PAIR`, 9 + 27 = 36, weld FOUND at fibers
1/1/1 with zero free items.  OCC: the excitation's carrier *is* the co-division
pair, 27 cells in bijection with the 27 unordered pairs, incidence 2/27 and
6/9.  **The same object, named identically, arrived at from opposite
directions — the record layer's refinement and the matter layer's carrier.**

**The independence must be qualified, and this is my substantive ruling.**  The
two units are not independent discoveries of one fact.  Both read paper-19: OCC
via `A-W3`/`A-W3REC` and the `VB-DICT` anchor
(`WELD3-FOUND-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|…]`), LOR via
`A-P19`/`A-P19REC`.  **The co-division pair is paper-19's own committed
vocabulary.**  What is genuinely independent is the *route*: OCC reads it off
the coupled machine's state space (`VB-CELL`, `DIM = 27`), LOR constructs it
from paper-04's dyadic refinement and finds it lands there.  So the convergence
is real but it is *two instruments correctly reading one committed anchor and
finding it forced on their own object*, not two blind hits.

### The cross-unit sentence, NOW (both delivered)

**Licensed now — a registered co-incidence, no more:**

> **REGISTERED (not a finding).**  Two same-hour units, reading one committed
> anchor (paper-19's `CO-DIVISION-ACTOR-PAIR→LINK`) by different routes, both
> land on the unordered co-division pair of actors as their object: LOR as the
> carrier the refined record needs (`SITE ← ACTOR ⊕ PAIR`, 9 + 27 = 36), OCC as
> the carrier the coupled matter already uses (27 cells).  Both readings are
> candidate.  No joint claim is licensed until both panels have ruled; in
> particular the grain's *name* is inherited, not co-discovered.

**Not licensed now:** "two independent units, one grain" (ledger #255's bracket)
as a *finding*; any sentence of the form "the record layer's refinement and the
matter layer's carrier are the same object" stated in the indicative; any
inheritance by FCK or SEC of a joint result.

### The cross-unit sentence, AT THEIR TERMINALS

**Licensed then, if both survive:**

> **THE PAIR IS THE COMMON GRAIN.**  The object the refined record needs for
> its new places and the object the coupled matter's excitation rides are the
> same object — the unordered co-division pair of actors.  Measured at the
> record layer as `SITE ← ACTOR ⊕ PAIR` (36-bijection, 54 determined links =
> the actor-in-pair incidences, fibers 1/1/1, zero free items) and at the
> matter layer as the 27-cell carrier (bijection 27/27, incidence 2/27 and
> 6/9).  The two measurements share one committed premise, paper-19's forced
> dictionary, and are otherwise independent in construction.

Even then it must carry the shared-premise clause, and it must **not** be
stated as "matter and geometry agree" — both are readings of one weld.

**Draft ledger rows, both ways:**

- *NOW*: `LOR∥OCC CO-INCIDENCE REGISTERED (candidate²): the co-division pair
  is the object on both sides — LOR's SITE ← ACTOR ⊕ PAIR (9+27=36) and OCC's
  27-cell carrier (2/27, 6/9); ONE SHARED PREMISE (paper-19's
  CO-DIVISION-ACTOR-PAIR→LINK, anchored in both); no joint claim until both
  panels rule.`
- *AT BOTH TERMINALS*: `THE PAIR IS THE COMMON GRAIN — the record layer's new
  places and the matter layer's carrier are one object, measured independently
  in construction from one shared committed dictionary; the record layer names
  the grain (as a link) and equips it with no occupancy coordinate (4,945
  names, 0 occupancy-shaped).`

Note the second row now composes correctly with MAJOR-2's repair: LOR's result
is itself further evidence that the grain **is** named at the record layer —
LOR builds 27 of its 36 refined sites out of it.

---

## R4 — SCOPE-CHECK OF THE LICENSED ASYMMETRY SENTENCE

Sentence handed to me: *"exclusion selects only at the carrier's grain — a
grain the record layer never names."*

**Clause 1, "exclusion selects only at the carrier's grain": LICENSED, and
strengthened.**  Measured 5 of 12 exclusion rows select, all at the carrier
grain; 0 of 12 permission rows select; 0 of 6 actor-grain exclusion rows
select, with no shape closing at 6 of 6.  I reproduced all of it, extended the
grain menu to the site grain and found `selects = 0 of 6`, and supplied the
mechanism theorem (R1.2) that explains why the carrier grain is structurally
the only place the *selection* mechanism can live.  Adopt "only" **as a
theorem about the mechanism plus a 3-grain measurement of the residual**, not
as a census over a 2-element menu.

**Clause 2, "a grain the record layer never names": NOT LICENSED — see
MAJOR-2.**  Answering the row's question directly: **no, it is not measured
over the record layer's published vocabulary.**  The census that exists
(`G-P2-NO-OCCUPANCY-KEY`) measures a different thing — 4,945 published names
across `A-COUPREC`, `A-W3REC`, `A-COUPSRC`, `A-D42B1`, `A-D60`, `A-D66`, scanned
against a 10-token *occupancy* vocabulary, 0 hits, with a 19-hit positive
control on `A-P22REC` and a homonym gate matching every `ceiling` occurrence
(5 + 4 + 5 + 6 hits over four sources) to a declared non-occupancy referent.
That is a clean measurement of "no occupancy coordinate below".  It says
nothing about whether the grain is named — and the unit's own `VB-DICT` anchor
and the `realised_pairs` receipt key show that it is.

**The licensed sentence:**

> **Exclusion selects a shape only at the carrier's own grain — and it is
> structurally the only grain where it could: a hard core at any strictly
> coarser grain gives the antisymmetric sector configurations to leak into,
> and the automatic closure that makes exclusion selective is gone (measured:
> both shapes leak at 6 of 6 coins at each of the two coarser grains tested).
> The record layer *names* that grain — it is the weld's own
> `CO-DIVISION-ACTOR-PAIR→LINK` leg — but equips it with no occupancy
> coordinate: 4,945 published names across six committed layers, none
> occupancy-shaped, against a 19-hit positive control.**

---

## R5 — THE INEXPRESSIBILITY-IS-NOT-EXCLUSION PRINCIPLE: ITS REGISTER ROW

**Ruling: a unified statement is PREMATURE.  Register the schema, not the
theorem.**

The three results share a form — *a declaration D is invisible to a probe class
P* — and differ in every argument of it:

| unit | the invisible declaration | the probe class P | how P is measured |
|---|---|---|---|
| paper-20 §8.3 | the stage's freshness | single-time ψ-internal closures | a **theorem** with a machine-checked *instance* over K1–K4, 1,040,065 checks |
| paper-22 | the occupancy ceiling (2 vs 1) | one-excitation objects | **derived from each declaration**, object by object, 64 generators (the K1 MINOR-3 repair) |
| OCC (paper-31) | the ceiling's value *and grain* | (a) published names of six layers; (b) the committed AST; (c) one-excitation objects | (a) and (b) are measurements about **vocabulary and source code**, not about a probe class; (c) is **instrumentally vacuous** (MAJOR-3) |

Three points do not make a law, and OCC's instance is currently the weakest of
the three: two of its legs do not have the schema's shape at all (they are
censuses of *names*, which is a claim about what a layer *says*, not about what
a probe *can distinguish*), and the one leg that does have the shape is the one
that cannot fail.  Promoting a unified statement now would be the corpus's
familiar failure mode — a headline built on the weakest instance.

**What is licensed as a register row:**

> **REGISTER — THE BLINDNESS SCHEMA (three instances, no theorem).**  Three
> units have measured a declaration invisible to a probe class: paper-20's
> staleness (single-time ψ-internal closures, a stated theorem with a checked
> instance), paper-22's ceiling (one-excitation objects, derived per
> declaration), and OCC's ceiling value-and-grain (published vocabulary and
> the committed construction).  The three probe classes are different objects
> and no unit has yet made "probe class" a declared coordinate.  **The schema
> is registered; the theorem is open.**

**And a fourth instance arrives for free from this review**: the leak census is
**record-blind across the whole 3²⁷ count-field family** (R1, `record_probe.py`)
— which is literally an instance of paper-20's staleness theorem at OCC's
arena, and OCC neither claims it nor notices the connection.  That is the first
*cross-unit* instance of the schema, and it is the natural seed for the
successor that would make the schema measurable.

**A separate register note, and this one is a genuine principle:**
*inexpressibility is not exclusion* is not a blindness result at all — it is a
**type distinction**: a representation with no coordinate for a question can
neither answer it nor forbid it, so a premise demanding exclusion fails as a
matter of type, not of evidence.  It is the sharpest sentence in the unit, it
is what makes `NOT-AVAILABLE` a first-class premise verdict distinct from
`AVAILABLE`/`STRUCTURAL-EXCLUSION`, and it stands on P2's legs (a) and (b),
which MAJOR-3 does not touch.  **Register it on its own, above the blindness
schema, not inside it.**

---

## R6 — FCK'S INHERITANCE ROW

`PLAN.md` (#209 amendment) reads: "*FCK now INHERITS the ceiling from OCC
instead of declaring it*".  **That charter row is now wrong and must be amended
at the adjudication**: OCC returned `OCC-CEILING-OPEN`.  There is no ceiling to
inherit.

**What FCK actually inherits — the priced two-coordinate declaration and its
declared menu:**

1. **A declaration FCK must make, with two coordinates.**  Value × grain, and
   the grain menu it inherits has (with this review's addition) three members —
   CARRIER (the cell = the co-division pair), SITE (the cell's base actor, a
   function), ACTOR (the incidence relation, 2 per cell).  Only CARRIER admits
   the automatic wedge closure that makes exclusion selective (R1.2, a theorem);
   at the other two, no shape closes at 6 of 6 coins.
2. **The three theories as its declared menu** — 378/351 (the free lift, which
   is what both ceiling-2 declarations collapse to), 351/351 (carrier hard
   core), 216/216 (actor hard core) — with the measured note that the two
   permission declarations are the same theory at two excitations, so at fixed
   number the menu has three members and the value axis carries one bit.
3. **The retyped seed conditional** (R2) as the statement of what would have to
   be supplied for FCK's ceiling to be forced rather than declared: it reduces
   to one missing object, an occupancy coordinate on the link.
4. **The unowned emission completion (S-3), and it becomes load-bearing
   immediately for FCK, not eventually.**  OCC measured 3 completions, 2
   preserving the parent's identity, 0 refusing, with fields differing at 3/9/9
   cells.  FCK's whole subject is number change; a creation operator on a
   carrier is *undefined* without a ceiling, and its emission is undefined
   without a completion.  **FCK cannot start without making both declarations
   OCC priced.**  The charter should say so.
5. **The free lift** (fiber 3, `INHERITED-AS-DECLARED`) — inherited untested and
   verdict-adjacent, since the whole leak structure is a statement about
   `U ⊗ U`.

**REPAIR to the charter row.**  "*FCK inherits from OCC not a ceiling but its
PRICE: a two-coordinate declaration (value × grain) over a three-member grain
menu of which only the carrier admits automatic wedge closure; three distinct
two-excitation theories; the retyped forcing conditional and its one missing
object; and the unowned emission completion, which OCC's S-3 shows becomes
load-bearing the moment a second excitation is admitted — i.e. at FCK's first
step.*"

---

## R7 — WALLS, CHOICE INVENTORY, PROSE↔RECEIPT SWEEP

### Walls — CLEAN

- **Shape-words.**  `G-NO-PARTICLE-NAMING` scans the object word by word
  against 24 banned words with `fermionic-shape` / `bosonic-shape` /
  `no-particle` / `particle-shaped` licensed.  I re-ran it hostilely on the
  paper: 3 `fermion*` hits and 1 `boson*` hit, **all** inside the licensed
  compounds; 2 `particle` hits, both inside `no-particle`.  **No spin** — the
  word does not occur.  **No relativity, no Lorentz, no boost.**
- **Cosmology / expansion bars.**  No `cosmolog*`, no `expansion`, no
  `universe`; one `continuum`, inside the head's own
  `NO-CONTINUUM-CLAIM` abstention.  `G-WALL-COSMO` clean.
- **The four inherited walls** are instrumented on the measurement layer
  (34,564 chars) with a falsifier each, per the declared convention, which §10
  states plainly.  **Register note, era-level, not against OCC:** the wall scans
  read the *measurement layer* and not the *paper*, so a wall-violating sentence
  in prose is caught only by the 24-word banned list; and each wall is a single
  literal needle (`cosmological expansion`, `boosted rest frame`,
  `myrheim-meyer`, `order-level covariance is established`), so a paraphrase
  passes.  Both are inherited patterns and both are worth an era row.
- **E-24 counting-only** stamped, `measure_declared: false`, four enumerations
  re-counted from their constructions (6, 216, 135, 24 — all reproduce).  **Gap
  noted in MAJOR-3:** `53,460` is not among them.

### Choice inventory — HONEST AS DATA, with one qualification

7 items, fibers counted not typed, 2 verdict-determining (grain, value).  The
classes are accurate: `MEASURED-BOTH` for the two live axes, `MEASURED-ALL` for
the coin, `INHERITED-AS-DECLARED` for the lift, `DECLARED-AND-ALL-RUN` for the
completion, `DECLARED-CONTROL` for the arms, `FORCED` for the arena.
**Qualification:** `the grain a ceiling is declared at | fiber 2` records the
size of the *declared menu*, and a reader will take it for the size of the
space.  It is now known to be at least 3.  Repair: `fiber 2 (DECLARED MENU; the
space is larger — see the site grain)`.

### Prose ↔ receipt sweep

I ran my own sweep against the serialized receipt: **208 numeral tokens, 26
distinct** (my tokenizer differs from the instrument's 144 + 58 + 10 = 212 —
not a discrepancy, a different token rule).  **Exactly one numeral has no
receipt backing: `22`**, and every occurrence is the proper noun *paper-22*.
Every other numeral in the paper occurs as a measured receipt value.  All
load-bearing values check out and I reproduced each independently: 27, 9, 36,
37, 6, 5, 81, 864, 216, 135, 351, 378, 324, 48, 64, 16, 12, 24, 405, 4945, 19,
102, 53460, 50, 40, 56, 54, 15, 23.

**But the sweep is value-bound, and that is the sweep's own limit.**  `27` is
licensed from `/arena/cells`, `/arena/co_division_pairs` *and*
`/arena/same_site_configurations` alike — which is exactly why MAJOR-1's false
claim carries a fully licensed numeral.  **Recommended era engraving:** a
numeral gate that licenses a value must, for claims flagged load-bearing, also
bind the *path* the claim's own words name.  Numerals were never the exposure;
nouns are.

### Head structure

46 fields across three segments (10 / 17 / 19 — counted, matches
`G-VERDICT-RECONSTRUCTED`'s 46), each naming a receipt path, multiset-matched
against the paper's three fences.  The head conforms to the pin's outcome
grammar `OCC-CEILING-OPEN-<the named premise; the fiber priced>` with P2 named
and the fiber priced.  Repairs owed to the head: MAJOR-1 (field rename +
one added field), MAJOR-3 or MINOR-3 (`53460` deleted or made a real ratio),
MINOR-4 (two SCOPE clauses).

---

# PART III — THE LICENSED CLAIM

Stated as the adjudication should carry it, after the repairs.

> **OCC-CEILING-OPEN.**  No committed layer of this substrate forces the
> occupancy ceiling that selects an exchange shape, and *fermionic-shape is not
> a theorem of the coupled theory at this arena* — it is a declaration.  The
> named premise is P2 and it fails **as a matter of type**: the committed
> representation has no occupancy coordinate at all, so a doubly occupied
> carrier there is neither constructible nor forbidden.  **Inexpressibility is
> not exclusion.**  Measured: 4,945 published names across six committed layers
> beneath the excitations, none occupancy-shaped, against a 19-hit positive
> control on the one layer that declared a ceiling; the committed dynamical
> instrument takes no excitation-number parameter in any of its 102 functions.
>
> **The excitation does not ride an actor.**  The coupled machine's carrier is
> its 27 cells, and a cell *is* an unordered co-division pair of actors — the
> committed instrument's own words, rebuilt and gated at 27/27.  Every cell
> carries exactly two actors (27/27) and every actor lies in exactly six cells
> (9/9), so excitation-to-actor is a relation and not a function.  The weld's
> ACTOR→SITE leg is a bijection on nine objects and reaches 9 of the 27 the
> excitation uses; the leg that welds the excitations' arena is the second,
> `CO-DIVISION-ACTOR-PAIR→LINK`, at fiber one.  **P1 = HOLDS-ON-THE-PAIR-LEG.**
>
> **The seed conditional was MISTYPED AT THE CARRIER AND REFUTED AT THE GRAIN
> IT TYPED.**  Its injection premise names actors and so does not denote on
> this representation; and when the actor-grain injection *is* supplied as a
> declaration (arm A2), the conditional's conclusion fails — both shapes leak
> at 6 of 6 coin classes, all 216 admissible configurations leak, all 135
> forbidden ones are reached.
>
> **A ceiling on this arena is a TWO-COORDINATE declaration — a value and a
> grain — at two excitations and over a declared grain menu.**  At the
> carrier's own grain a hard core selects the antisymmetric shape at 5 of 6
> coin classes (the symmetric shape leaks at 81 cells, the antisymmetric at 0);
> at every coarser grain tested it selects nothing.  **The asymmetry, restated:
> exclusion can select a shape, permission cannot (0 of 12 rows), and exclusion
> selects only at the carrier's own grain (5 of 12 rows, all of them there) —
> and structurally it could not be otherwise: a hard core at any strictly
> coarser grain hands the antisymmetric sector distinct-cell configurations to
> leak into, so the automatic closure that makes exclusion selective exists at
> the carrier's grain alone.**  The record layer *names* that grain — it is the
> weld's own `CO-DIVISION-ACTOR-PAIR→LINK` leg — but equips it with no
> occupancy coordinate.
>
> **The two grains are related by strict containment, not identity:** the 27
> carrier-grain leak sources are exactly the same-site configurations, a strict
> subset of the 135 the actor-grain declaration forbids.  Actor-grain exclusion
> is strictly stronger than closing the carrier-grain leak requires, and it
> cannot see an exchange shape at all: the two shapes' leak sets coincide, with
> 0 cells available for a cancellation.
>
> **Priced fiber:** 4 declarations → 3 distinct two-excitation theories → 3
> emission completions (2 preserving the parent's identity, 0 refusing a
> division to a doubly occupied carrier).  **Scope:** two excitations only; the
> free lift `U ⊗ U`; one record — and the P4 census is in fact record-blind
> across the whole admissible count-field family; the declared grain menu;
> shape-words only; counts are counting-only; the ceiling is not declared by
> this unit either.

**Explicitly NOT licensed:** "the two grains are one phenomenon"; "a grain the
record layer never names"; the 53,460-comparison agreement as a measurement;
"two independent units, one grain" as a finding; any unified blindness theorem;
any statement about general excitation number, other lifts, other coin
families, or paper-22's arena.

---

# PART IV — THE SUCCESSOR REGISTER

The unit's own S-1…S-5 are well drawn and I adopt them.  Six additions, all
posable now.

**S-E1 — THE GRAIN LATTICE, and the minimal closing declaration.**  Grains are
quotients of the 27 cells; the unit tested two, I added a third.  The lattice
between CARRIER (27) and ACTOR (the 135-pair incidence) is not enumerated, and
the theorem in R1.2 makes the enumeration cheap: only the carrier grain admits
automatic wedge closure, so the question for every coarser grain is a single
leak census.  Specifically posable: **what is the *weakest* declaration that
closes the carrier-grain symmetric leak?**  Removing just the 27 same-site
sources kills the leak's source side by construction; whether the residual
324-configuration theory is itself closed is one census.

**S-E2 — THE RECORD-BLINDNESS THEOREM, free and unclaimed.**  The count field
enters the walk as a unit-modulus diagonal and cannot change a zero; measured,
the entire leak census is identical at `n ≡ 1`, `n ≡ 0`, `n ≡ 2` and random
fields.  The head's `THE-WELDED-LANDING-RECORD` scope is retirable by theorem
over the full 3²⁷ family.  This is also the first *cross-unit* instance of
paper-20's staleness-blindness schema and the natural seed for S-E4.

**S-E3 — THE HONEST DECLARATION FIBER.**  Either derive the one-excitation
restriction from each declaration (paper-22's repaired construction) with a
declaration in the menu that could separate them, or demote the row to its
one-line theorem and shrink P2's derivation to its two live legs.  Do not ship
a third variant of the shape without the substance.

**S-E4 — MAKE "PROBE CLASS" A DECLARED COORDINATE.**  The blindness schema has
four instances (paper-20, paper-22, OCC, and S-E2) and no theorem because no
unit has made the probe class an object it varies.  A unit that declares a
lattice of probe classes and measures, for each declaration, the *coarsest*
probe class that sees it would turn three anecdotes into a law — and would be
the first unit in the corpus to measure invisibility rather than exhibit it.

**S-E5 — THE LIFT AXIS.**  Every leak statement here is a statement about
`U ⊗ U`.  The inventory prices the lift at fiber 3 and runs one.  A contact
term is a diagonal phase and provably cannot change the leak pattern; a
genuinely non-product lift can.  This is the one untested axis that could move
P4, and it is the axis FCK's number-changing dynamics will force open.

**S-E6 — THE REFERENT GATE (era engraving).**  MAJOR-1 is the corpus's first
measured case of a false load-bearing claim surviving a complete value-bound
gate stack — 46 de-twinned fields, 50 mutants, 15 claim gates, 4 polarity rows,
212 numerals, 40 seals.  The exposure is that receipt *keys assert referents*
and nothing checks a key's name against the object it holds.  Proposed rule:
**for every claim flagged load-bearing, the gate must bind the claim's own noun
phrase to the receipt path it names, and any published set-equality must name
both sides and publish both cardinalities.**  Cheap, and it closes exactly the
hole that let a 27 stand in for a 135.

---

# REPAIR TABLE

| id | repair | closes | cost | priority |
|---|---|---|---|---|
| R-OCC-E1 | rename the set-equality object to SAME-SITE throughout (claim C09, head field, receipt key, gate statement, §6, §9); add the 27-of-135 containment row; **ledger erratum on #255's "one phenomenon" headline** | MAJOR-1 | ~15 lines + a re-run | **P1** |
| R-OCC-E2 | retype "never names" → "names but never equips with an occupancy coordinate", per §8's own wording, in the summary, §9 and the ledger's licensed sentence | MAJOR-2 | 3 sentences | **P1** |
| R-OCC-E3 | derive the one-excitation restriction from each declaration, **or** demote the row to a theorem, delete `53,460` from head/C05/§9 and reduce P2's published derivation to two legs | MAJOR-3 | ~25 lines | **P1** |
| R-OCC-E4 | ledger word → `MISTYPED-AT-THE-CARRIER; REFUTED-AT-THE-GRAIN-IT-TYPED`; draw the A2 sentence in §8 and in the head's register | R2 (a gain) | 2 sentences | **P1** |
| R-OCC-E5 | own the pin's "(9 sites)" as an **ORCHESTRATOR'S PIN ERROR** in the adjudication row, per the #2154/#286/#6785 form, with the corrected conditional stated | R2 | 1 ledger clause | **P1** |
| R-OCC-E6 | amend `PLAN.md`'s FCK row: FCK inherits the *price*, not a ceiling; the completion is load-bearing at FCK's first step | R6 | 1 charter clause | P2 |
| R-OCC-E7 | add the SITE grain as a third declaration row and the wedge-closure theorem as the mechanism behind "only" | R1 | ~20 lines | P2 |
| R-OCC-E8 | head `SCOPE` gains `FREE-LIFT-ONLY(U-TENSOR-U)` and `GRAIN-MENU-AS-DECLARED` | MINOR-4 | 2 tokens | P2 |
| R-OCC-E9 | §1's ingredient count → one-of-three-carries-force | MINOR-1 | 1 sentence | P2 |
| R-OCC-E10 | `G-PAPER-TABLES` → "four load-bearing tables" | MINOR-2 | 1 string | P3 |
| R-OCC-E11 | `P2-ONE-EXCITATION-…-AGREE` → a real ratio, or deleted with R-OCC-E3 | MINOR-3 | 1 line | P3 |
| R-OCC-E12 | §5's blindness sentence → existential, or census it | MINOR-5 | 1 sentence | P3 |
| R-OCC-E13 | choice inventory: mark the grain fiber as the **declared menu** | R7 | 1 cell | P3 |
| R-OCC-E14 | register S-E2 (record-blindness) and retire the record scope by theorem | S-E2 | ~10 lines | P3 |

---

**Seat closed.**  58 recomputations; zero false *computed numbers*; one false
*published claim* (MAJOR-1), one refuted head clause (MAJOR-2), one vacuous
headline number reopening a closed era disease (MAJOR-3), five minors; four
licensed strengthenings supplied by this review (the wedge-closure mechanism
theorem, the site-grain extension, record-blindness, and the
refuted-at-its-own-grain reading of the seed conditional).  **The verdict
`OCC-CEILING-OPEN` stands unmoved.**
