# OCC — the carrier is not the actor

*v14, the limit programme, paper 31. Instrument: `v14/code/occ_exact.py`;
artifacts `occ_output.txt` and `occ_receipt.json`. Exact arithmetic
throughout: the field is Q(ζ₃) carried as integer pairs over Z[ω] with the
common denominator 3, every leak test is an exact zero test in that ring, and
there is no float anywhere. Pin: `v14/note-occ-pin.md`.*

---

**The verdict, in three segments, quoted exactly as the instrument emits it.**
Each segment is a sequence of `LABEL=VALUE` fields built from a declared field
spec whose every field names a receipt path; the audit route types no copy of
any of it and is described in §10.

```
OCC-CARRIER<THESIS=THE-EXCITATION-RIDES-THE-CO-DIVISION-PAIR-NOT-THE-ACTOR; CARRIER-CELLS=27; CO-DIVISION-PAIRS=27; CELL-IS-A-CO-DIVISION-PAIR=YES; ACTOR-SITE-BIJECTION=9-OF-9; ACTOR-LEG-IMAGE-CARDINALITY-AGAINST-THE-CARRIER=9-VS-27; CELLS-WITH-EXACTLY-TWO-ACTORS=27-OF-27; ACTORS-IN-EXACTLY-SIX-CELLS=9-OF-9; EXCITATION-TO-ACTOR-IS-A-FUNCTION=NO; P1=HOLDS-ON-THE-PAIR-LEG>
```

```
OCC-POOL-AND-GRAIN<THESIS=EXCLUSION-SELECTS-ONLY-AT-THE-CARRIER-S-OWN-GRAIN; COIN-CLASSES=6; RING-SOLUTIONS=36; NON-MONOMIAL-COINS=5-OF-6; CARRIER-GRAIN-SYMMETRIC-LEAK-CELLS=81; CARRIER-GRAIN-COINS-LEAKING=5-OF-6; CARRIER-GRAIN-ANTISYMMETRIC-LEAK-CELLS=0; CARRIER-GRAIN-ANTISYMMETRIC-FORBIDDEN-CONFIGURATIONS=0; CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-SITE-CONFIGURATIONS=5-OF-5; CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-ACTOR-CONFIGURATIONS=0-OF-5; CARRIER-GRAIN-LEAK-SOURCES-ARE-ACTOR-GRAIN-FORBIDDEN=27-OF-135; CARRIER-GRAIN-CONTAINMENT-IS-STRICT=5-OF-5; SAME-ACTOR-CONFIGURATIONS-EXCLUDED=108; ACTOR-GRAIN-COINS-WHERE-BOTH-SHAPES-LEAK=6-OF-6; ACTOR-GRAIN-LEAK-CELLS-NON-MONOMIAL=864; ACTOR-GRAIN-LEAK-CELLS-MONOMIAL=81; ACTOR-GRAIN-SHAPE-LEAK-SETS-COINCIDE=6-OF-6; ACTOR-GRAIN-CANCELLATION-CELLS=0; ACTOR-GRAIN-SOURCES-LEAKING-MAX=216-OF-216; ACTOR-GRAIN-SOURCES-LEAKING-MIN=81-OF-216; ACTOR-GRAIN-TARGETS-REACHED-MAX=135-OF-135; ACTOR-GRAIN-TARGETS-REACHED-MIN=81-OF-135; ACTOR-GRAIN-COINS-WHERE-EVERY-ADMISSIBLE-SOURCE-LEAKS=5-OF-6; ACTOR-GRAIN-COINS-WHERE-EVERY-FORBIDDEN-TARGET-IS-REACHED=5-OF-6; WEDGE-FORBIDDEN-SET-EMPTY-IFF-THE-CARRIER-GRAIN=3-OF-3; SITE-GRAIN-COINS-THAT-SELECT=0-OF-6; SITE-GRAIN-COINS-WHERE-NO-SHAPE-CLOSES=6-OF-6; P4-IS-RECORD-BLIND-AT-THE-PROBED-COUNT-FIELDS=4-OF-4; LEAK-ROUTES-AGREE=48-OF-48; PARENT-SPLIT-CITED=48-OF-64>
```

```
OCC-CEILING-OPEN<P1=HOLDS-ON-THE-PAIR-LEG; P2=NOT-AVAILABLE; P2-NAMES-CENSUSED=4945; P2-OCCUPANCY-SHAPED-NAMES=0; P2-DECLARATION-FIBER=3-OF-4; P2-ONE-EXCITATION-RESTRICTIONS-AGREE=53460-OF-53460; P3=SILENT-AND-VACUOUSLY-SATISFIED; P3-EMISSION-READING-FIBER=2; P3-BLINDNESS-PAIR-SITE-FIELDS-AGREE=9-OF-9; P3-SITE-FIELD-CANNOT-SEPARATE=81-OF-81; P3-RECORD-MENU-READING-SEPARATES=0-OF-81; P3-BORN-MENU-READING-SEPARATES=81-OF-81; P3-COMPLETIONS-PRESERVING-THE-PARENT-IDENTITY=2-OF-3; P3-COMPLETIONS-THAT-REFUSE-A-DIVISION=0-OF-3; P4=NO-SHAPE-CLOSES; ASYMMETRY-PERMISSION-ROWS-THAT-SELECT=0-OF-12; ASYMMETRY-EXCLUSION-ROWS-THAT-SELECT=5-OF-12; ASYMMETRY-AT-THE-ACTOR-GRAIN=0-OF-6; ARMS=4-OF-6; CONTROL-CAN-FIRE=C1-SUBSET-CARRIER; CONTROL-CAN-FAIL=C2-MULTISET-CARRIER; SEED-CONDITIONAL=MISTYPED-AT-THE-CARRIER;REFUTED-AT-THE-GRAIN-IT-TYPED; FIBER-PRICED=4-DECLARATIONS-3-THEORIES-3-EMISSION-COMPLETIONS; SCOPE=TWO-EXCITATIONS-ONLY;ONE-RECORD;THE-WELDED-LANDING-RECORD;P4-IS-RECORD-BLIND-OVER-THE-COUNT-FIELD-FAMILY;FREE-LIFT-ONLY(U-TENSOR-U);GRAIN-MENU-AS-DECLARED;SHAPE-WORDS-ONLY;NO-PARTICLE-CLAIM;NO-BRAID-CLAIM;NO-GENERAL-N-CLAIM;NO-CONFIGURATION-MEASURE;COUNTS-ARE-COUNTING-ONLY;NO-CONTINUUM-CLAIM;THE-CEILING-IS-NOT-DECLARED-BY-THIS-UNIT-EITHER>
```

Between delivery and adjudication every headline here is a **candidate
reading**.

---

## What rides what

Paper-22 ended on an opening it stated precisely: the occupancy ceiling is the
coordinate that selects an exchange shape, its own stage declares none, and
whether a deeper layer can be made to force one is open. It handed forward a
conditional — weld bijection, plus an excitation-to-actor injection, plus a
closure requirement, plus the full pool — whose conclusion would have been that
one exchange shape is a theorem rather than a declaration. This unit measures
that conditional premise by premise on the committed layers. It never assumes
it, and the first premise is where the surprise is.

**The excitation does not sit on an actor.** The coupled machine's state is a
vector on its cells, and the committed instrument says in its own words what a
cell is: the unordered co-division pair {*x*, *x*+*l*}. So the excitation's
coordinate is a PAIR of actors, not one. The weld's forced dictionary has two
legs, and the leg that welds the arena the excitations actually use is the
second one, not the first: the ACTOR→SITE leg is a bijection at 9 of 9 and its
image has 9 members against the carrier's 27, while
CO-DIVISION-ACTOR-PAIR→LINK is the bijection onto the carrier itself. The
incidence is measured in both directions, and §3 gives it: a cell has two
actors and an actor has six cells. An excitation-to-actor map is therefore not
a function at all, and *the excitation rides the co-division pair*. The seed
conditional's injection premise is not false on this arena; it is not a
statement about this carrier.

**Nothing beneath the excitations carries an occupancy coordinate.** The
question "how many excitations may one carrier hold" cannot be asked of the
committed layers, because none of them has a place to put the answer. That is a
census with a positive control rather than an absence, and §4 gives its two
arms: nothing occupancy-shaped below, and the same scan firing on the one layer
that declared a ceiling. The committed dynamical instrument constructs no
two-excitation object of any kind — no function in it takes an excitation
number, and no pair or product constructor in it ranges over the carrier — so a
doubly occupied carrier there is neither constructible nor forbidden.
Inexpressibility is not exclusion, and the difference is the whole question.
Four declarations are constructed here to make the point measurable, each one's
one-excitation restriction built from its own declared configuration space;
they give 3 distinct two-excitation theories, and their one-excitation
restrictions agree, as objects, at 53,460 of 53,460 comparisons. The ceiling is
invisible from below by construction, not by accident.

**And the ceiling is not one declaration but two — a value and a GRAIN — which
is what decides the unit.** At the carrier's own grain the old mechanism works:
the symmetric shape leaks at 81 cells at 5 of the 6 coin classes and the
antisymmetric shape leaks at 0, so a hard core there would select. At the
actor's grain — the grain the weld's first leg speaks, the grain in which
"one excitation per actor" is a sentence — **both** shapes leak at 6 of 6 coin
classes, and at the 5 non-monomial classes every one of the 216 admissible
configurations leaks and every one of the 135 forbidden configurations is
reached. No shape closes, so nothing is selected. Exclusion can still select a
shape and permission still cannot, but the refinement this arena forces is
sharper than the original: exclusion selects only at the carrier's own grain,
and that is not a two-point census but a theorem with a residual, since the
automatic closure that makes exclusion selective is available at one grain of
the three this arena admits and structurally nowhere else. The record layer
*names* that grain
— it is the weld's own CO-DIVISION-ACTOR-PAIR→LINK leg — but equips it with no
occupancy coordinate. So no committed layer forces the occupancy ceiling, and
fermionic-shape is not a theorem of the coupled theory here — it is a
declaration, made at a grain the committed dictionary names and never measures.

---

## 1. The question, and what would have answered it the other way

The pin sets four premises and four pre-registered outcome words, and the
instrument parses those words out of the pin's own bytes rather than typing
them: `OCC-CEILING-FORCED`, `OCC-CEILING-OPEN`, `OCC-CEILING-PARTIAL`,
`OCC-BLOCKED-AT`. The head is derived from the four premise verdicts by one law
and is exercised on six arenas; the head law returns 4 different pre-registered
outcome words across the 6 arenas, so every branch is reached on a constructed
arena rather than on a synthetic census, and the four words the six arenas
return are compared with the pre-registered set as a set.

| arena | P1 | P2 | P3 | P4 | the head the law returns |
|---|---|---|---|---|---|
| `A0-COMMITTED-COUPLED-MACHINE` | HOLDS-ON-THE-PAIR-LEG | NOT-AVAILABLE | SILENT-AND-VACUOUSLY-SATISFIED | NO-SHAPE-CLOSES | `OCC-CEILING-OPEN` |
| `A1-DECLARED-EXCLUSION-AT-THE-CARRIER-GRAIN` | HOLDS-ON-THE-PAIR-LEG | DECLARED-EXCLUSION | SILENT-AND-VACUOUSLY-SATISFIED | SELECTS | `OCC-CEILING-PARTIAL` |
| `A2-DECLARED-EXCLUSION-AT-THE-ACTOR-GRAIN` | HOLDS-ON-THE-PAIR-LEG | DECLARED-EXCLUSION | SILENT-AND-VACUOUSLY-SATISFIED | NO-SHAPE-CLOSES | `OCC-CEILING-PARTIAL` |
| `A3-C1-SUBSET-CARRIER` | HOLDS-BY-CONSTRUCTION | STRUCTURAL-EXCLUSION | CLOSURE-AVAILABLE | SELECTS | `OCC-CEILING-FORCED` |
| `A4-C2-MULTISET-CARRIER` | HOLDS-BY-CONSTRUCTION | CONSTRUCTIBLE | CLOSURE-AVAILABLE | DOES-NOT-SELECT | `OCC-CEILING-OPEN` |
| `A5-C3-ONE-CARRIER` | HOLDS-BY-CONSTRUCTION | STRUCTURAL-EXCLUSION | CLOSURE-AVAILABLE | DOES-NOT-SELECT | `OCC-BLOCKED-AT` |

The first row is the verdict arena: the committed layers as they stand, with no
declaration added. Rows two and three add the injection as a DECLARATION, at
each of the two grains, and they differ from each other in nothing else. Rows
four and five are the pin's two-way control and are §7's subject. Row six is a
degenerate control, declared as such: on a single carrier the antisymmetric
sector is empty and the comparison is not posable.

What would have produced `OCC-CEILING-FORCED` on the verdict arena is exactly
what row four exhibits and the committed arena lacks: a representation in which
double occupancy is not expressible, a closure requirement that bites, and a
pool with a member whose symmetric square cannot stay inside the admitted
configurations. One of those three is present in a form that carries force: the
pool, read at the carrier's grain. The closure requirement is satisfied but
vacuously, and a premise that holds because the question is invisible carries no
force into the conclusion. The representation is absent, and it is the one that
decides.

## 2. The arena, rebuilt rather than cited

The carrier is rebuilt here from the nine actors and the three declared link
directions and then gated against the coupled machine's own committed receipt —
its cells, its sites, its link list and its landing record — so nothing about
the arena is retyped. The record is the welded landing record, count one at
every cell, which is the record the committed walk runs on; §6 shows that the
leak layer does not depend on that choice.

**A cell is a co-division pair.** The committed instrument's own naming is the
anchor: cell (*x*, *l*) IS the unordered co-division pair {*x*, *x*+*l*}, and
the three shifts along a line of direction *l* cover that line's three unordered
pairs exactly once. This unit rebuilds that map and checks it in both
directions: the coupled machine's carrier is 27 cells, and a cell IS an
unordered co-division pair of actors: the two sets are in bijection at 27 of 27.

**The pool is the arena's own.** The S₃-covariant unitary coins over the
arena's own alphabet — the elements of (1/3)Z[ω] of modulus at most one — are
rebuilt from the definitions and the census is gated against the coupled
machine's committed one: 36 solutions over the ring, 6 classes up to a global
phase, of which one is ±Grover. Each class gives one walk operator on the 27
cells; all six are exactly unitary, checked per column pair rather than by a
norm; five of the six are non-monomial and one — the trivial class, a
deterministic shift — is not. Nothing else about the walk is re-selected: the
coin order, the orientation and the start are inherited as declared.

## 3. P1 — the bijection, measured on the arena the excitations use

The pin asks whether the weld's ACTOR→SITE map is a bijection on the arena the
excitations use, and names the nine sites as that arena. Measured, it is not:
the excitations use the 27 cells. So the premise splits, and both halves are
measured.

The ACTOR→SITE leg is a bijection — injective and surjective, per object — on
nine objects. It is not onto the carrier, and the honest comparison is of two
cardinalities rather than of a covering: the weld's ACTOR→SITE leg is a
bijection at 9 of 9, and its image has 9 members against the carrier's 27 — two
cardinalities of different kind, since the leg's image is a set of sites and the
carrier is a set of cells. That is why the seed
conditional's first premise, true as stated, does not reach the excitations. The
leg that does reach them is the dictionary's second: CO-DIVISION-ACTOR-PAIR→LINK,
whose fiber the weld measured at one, and whose target is exactly the set the
walk's amplitudes live on.

The consequence is the incidence, and it is measured in both directions: every
cell carries exactly two actors at 27 of 27, and every actor lies in exactly six
cells at 9 of 9. A relation with two values is not a function, so "this
excitation's actor" does not denote. **P1 = HOLDS-ON-THE-PAIR-LEG**: the weld
does weld the excitation's arena, with fiber one, through the leg that maps
actor pairs to links.

That is not a defect of the weld. It is what the weld says: the record's links
ARE co-division pairs of actors, and the walk was built on the links.

## 4. P2 — the turning premise: nothing below has an occupancy coordinate

The premise the whole conditional turns on is whether a doubly occupied state is
constructible in the coupled representation. Three legs measure it, and the
question throughout is about the state space's CONSTRUCTION, never about its
usage.

**The vocabulary.** The published key sets of the committed receipts and the
declared name sets of the committed sources — identifiers, parameters,
attributes and the short string constants used as keys — are scanned token by
token against a declared occupancy vocabulary. The scan is two-armed, and the
second arm is what makes it a measurement: 4945 published names across the 6
committed layers beneath the excitations, and none of them is occupancy-shaped,
while the same scan fires at 19 names on the one layer that declared a ceiling.
The homonym is measured rather than suppressed: the word *ceiling* does occur
below, and every occurrence is matched to a declared non-occupancy referent —
the weld's positive-definiteness ceiling on division counts, a search ceiling
and an arbitration budget. A new referent would fail the gate.

**The construction.** The committed instrument's own abstract syntax tree is
read. Its declared carrier size is this unit's rebuilt carrier; none of its
functions takes an excitation-number parameter; its state-carrying sequence
constructors are eight vectors of the carrier's own dimension, and no
combination, product or permutation constructor in it ranges over the carrier —
the three it does build range over sites, over the scalar alphabet and over the
three link directions, so the scan is discriminating rather than empty. A second
excitation is not forbidden there. It is unsayable there.

**The fiber.** Four declarations are constructed — a ceiling of one or two, at
the carrier's grain or the actor's — and their configuration spaces measured.

| declaration | grain | ceiling | symmetric configurations | antisymmetric configurations |
|---|---|---|---|---|
| `D-CARRIER-2` | CARRIER | 2 | 378 | 351 |
| `D-CARRIER-1` | CARRIER | 1 | 351 | 351 |
| `D-ACTOR-1` | ACTOR | 1 | 216 | 216 |
| `D-ACTOR-2` | ACTOR | 2 | 378 | 351 |

A declaration is a predicate — the load its grain counts, against its value —
and both of its coordinates are parameters of the construction, so the
one-excitation restriction of each declaration is built from that declaration's
own admissible configurations rather than from the walk alone. 4 declarations
give 3 distinct two-excitation theories, and their one-excitation restrictions
agree as objects at 53,460 of 53,460 comparisons — configuration set,
transition matrix and Born shadow, entry by entry, at every coin class. A
declaration that forbade a cell outright, or a ceiling of zero, would build a
different object and move that row, which is what makes it a measurement. The
collapse is itself a row worth stating: an actor-grain ceiling of two forbids
nothing at two excitations, so it is the same theory as the free lift.

**So P2 = NOT-AVAILABLE.** A representation that EXCLUDED double occupancy would
have to forbid it, and forbidding is a thing a representation does; this one
has no coordinate in which to do it. And because every declaration restricts to
the same one-excitation object, no measurement at one excitation — not one of
the coupled machine's, not one of the weld's — could have distinguished them.
The ceiling is invisible from below, and that is why the premise fails as a
matter of type rather than of evidence.

## 5. P3 — closure: the grammar cannot refuse

The third premise asks whether an actor carrying two excitations can still
divide. The committed grammar's division events are decided by the transport
layer's own candidate menu and attached to a cell by the emission rule. Three
measurements make that concrete, and the first of them is scoped to a fiber the
parent declares and this unit inherits.

**What the rule reads, per declared reading.** Two two-excitation configurations
are built: one with its excitations on two different cells of a single actor,
one with both on a single cell. They differ in cell occupation and their site
fields agree at 9 of 9. The parent declares the emission reading at fiber 2 —
the Born menu against the record menu, both run — and the kernel it takes at a
site is the declared menu normalised by its own mass, so the two readings are
different functions of the state and both are applied here. Over a census of
every doubly occupied configuration against every same-site partner, 81 pairs in
all: under the record-menu reading the state does not enter the committed
emission rule's kernel at all and the rule cannot separate any of the 81 pairs,
while under the Born-menu reading — the one the parent's coupled ensemble runs —
it enters per cell and separates 81 of 81. On the witness pair the Born menu
gives 1/2, 1/2, 0 against 1, 0, 0 and the record menu gives 1/3, 1/3, 1/3
against itself. So the blindness is the record menu's, not the rule's, and what
carries P3 is not blindness at all: it is that the grammar has no occupancy
coordinate to condition on, and that no completion refuses.

**The completion fiber, priced.** The committed emission rule is a rule for one
excitation. Three completions to two are constructed and all three run: per
excitation, per configuration, and site-then-record. 2 of the 3 completions
preserve the parent's own emission identity, and 0 of 3 refuse a division to a
doubly occupied carrier — each completion's own field is built for the doubly
occupied state itself and its support measured, so that count is a per-object
read. The per-excitation completion emits twice per step and so breaks the
parent's consistency identity outright; the other two keep it and differ from
each other cell by cell. The declaration the grammar is missing is therefore
verdict-relevant for the parent's own gate, not cosmetic — and none of its three
members supplies an exclusion.

**P3 = SILENT-AND-VACUOUSLY-SATISFIED**, derived from those legs and compared
against its derivation rather than typed. The closure premise is satisfied, and
satisfied in the way that helps least: the grammar cannot refuse a division to a
doubly occupied carrier because it has nothing in which to state the refusal. A
premise that holds because the question is unsayable carries no force into the
conclusion.

## 6. P4 — the pool, at both grains

The pool is censused at every declaration and in both exchange shapes, with the
gate binding coins rather than the tally, and the leak measured by two
independent routes at every row.

| coin | monomial | carrier-grain symmetric leak | actor-grain symmetric leak | actor-grain antisymmetric leak |
|---|---|---|---|---|
| `K-2-1w` | no | 81 | 864 | 864 |
| `K-2+0w` | no | 81 | 864 | 864 |
| `K-1-1w` | no | 81 | 864 | 864 |
| `K-1+1w` | no | 81 | 864 | 864 |
| `K+0+0w` | yes | 0 | 81 | 81 |
| `K+0+1w` | no | 81 | 864 | 864 |

**At the carrier's grain, paper-22's theorem transports intact.** In the
normalised symmetric square the only cell from a hard-core configuration into a
doubly occupied one is a single product of two amplitudes, so the symmetric
shape leaks exactly when some row of the operator carries two nonzero entries,
and the wedge has no doubly occupied configuration to leak into at all — its
forbidden set is empty, which is why its 0 is a vacuous zero and is published as
one. Verified per coin, in both directions: at the carrier's own grain the
symmetric shape leaks at 81 cells at 5 of the 6 coin classes and the
antisymmetric shape leaks at 0. The one class that does not leak is the one
whose walk operator is monomial, and there both shapes close and nothing is
selected.

**And the two grains are related by a set equality and a strict containment:**
the configurations that leak are exactly the 27 whose two excitations sit on two
of the three cells of one site — a set equality at 5 of 5 leaking coin classes —
and every one of them is among the 135 configurations the actor-grain
declaration forbids, a containment that is strict at 5 of 5 and excludes 108 of
them. Both set equalities are measured, element for element: with the same-site
set the equality holds at 5 of 5 leaking classes and with the same-actor set at
0 of 5. So every leak out of the carrier-grain hard core is caused by a
configuration the actor-grain declaration would have forbidden, and actor-grain
exclusion is strictly stronger than closing the carrier-grain leak requires. The
mechanism is visible in the row structure: a row of the walk operator is
supported on the three cells of one site, so the only sources that can reach a
doubly occupied cell are pairs drawn from those three, and those pairs both sit
at one site and share an actor.

**At the actor's grain, both shapes leak, and neither is a law.** Measured:
at the actor's grain both shapes leak at 6 of 6 coin classes; at the 5
non-monomial classes every one of the 216 admissible configurations leaks and
every one of the 135 forbidden configurations is reached, and at the monomial
class 81 of 216 leak and 81 of 135 are reached. The failure is total at every
class and complete at five of them, and it does not spare the monomial one:
even the deterministic shift carries 81 admissible configurations into forbidden
ones, because the shift moves a link to a link that meets another.

**The two shapes leak at the same cells, and that is a theorem here.** For a
target pair of cells sharing an actor, the two products of the lifted matrix
element are supported on disjoint source pairs, so no cancellation is available
to either shape: the two shapes' leak sets coincide cell for cell at 6 of 6 coin
classes, and no cell of either carries two nonzero products, at 0. The wedge and
the symmetric square are indistinguishable to actor-grain exclusion — it does
not merely fail to select between them, it cannot see the difference.

**And none of it depends on the record.** The count field enters the walk only
as a diagonal of unit-modulus ring elements on the source cell, so it cannot
turn a zero into a nonzero and the whole leak layer is a function of the walk's
zero pattern alone. Measured rather than argued: the walk is rebuilt at four
declared probe fields — the all-zero record, the all-two record and two
non-constant ones — and the whole leak census is identical at every one of the 4
declared probe fields, at 48 of 48 rows each, with the support pattern identical
at every coin. The welded landing record is the arena the premises are measured
on; it is not a boundary on P4.

**The parent's own split is cited, not retyped.** paper-22's split is cited from
its own rows: the symmetric shape leaks at 48 of its 64 generators, with the
remaining sixteen closed and its antisymmetric shape leaking at none. The number
is recomputed here from the parent's committed receipt rather than read out of
its prose.

**The two routes.** Every leak row is measured twice — once by forming the
lifted element and testing it against zero in the ring, once by counting the
cells at which at least one of the two products is nonzero without ever forming
the element. Measured: the two routes agree at 48 of 48 leak rows, and the
census of cells where both products are nonzero, the only place they could have
disagreed, is published beside them.

## 7. The controls, two-way

The pin requires an arena where the conditional demonstrably fires and one where
it demonstrably fails, and the two arms differ in one coordinate.

Both use the same carrier of nine objects, the same generator — the declared
control unitary, every entry nonzero — the same free lift and the same census
code. `C1-SUBSET-CARRIER` builds its configurations as SUBSETS: a doubly
occupied carrier is not expressible, the symmetric shape leaks out of the
representation, the antisymmetric shape closes, exactly one shape survives and
the head law returns `OCC-CEILING-FORCED`. `C2-MULTISET-CARRIER` builds them as
MULTISETS: the doubly occupied configurations exist, both shapes close, nothing
is selected and the head returns `OCC-CEILING-OPEN`.

That contrast is the pin's own it-can-fail arm, and it is what licenses reading
the committed arena's `OCC-CEILING-OPEN` as a measurement rather than as an
instrument failure: the same instrument, on an arena where the conditional
holds, returns the other word.

## 8. The asymmetry row, restated at the measured verdict

Paper-22's organizing sentence was that exclusion can select a shape and
permission cannot. Measured here across every coin class and every declaration:
permission selects a shape at 0 of 12 rows and exclusion at 5 of 12, all of them
at the carrier's own grain. At the actor's grain exclusion selects at none of
its six rows, and at all six of them the reason is that no shape closes at all.

So the asymmetry survives and gains a second clause. Permission selects nothing,
at either grain — declaring that a carrier may hold two excitations leaves both
shapes as laws. Exclusion selects, but only where the excluded object is the
excitation's own coordinate. Push the exclusion up to the actor, which is the
object the record layer names, the object the geometry is built from and the
only object the dictionary's first leg mentions, and it stops selecting and
starts destroying: neither shape is a law under it. **Exclusion can select a
shape; permission cannot; and exclusion selects only at the carrier's own
grain.**

**The "only" is a theorem with a residual, not a two-point census.** Under a
hard core at a grain *G* the antisymmetric sector's forbidden set is the set of
distinct-cell pairs that collide under *G*, and it is empty exactly when *G* is
the carrier's own grain, because only there does no pair of distinct cells
collide. Measured over the three grains this arena admits — the cell, its base
site, and the actor — the antisymmetric sector's forbidden set is empty at
exactly 1 of the 3 grains this arena admits, and it is the carrier's own, at 0
against 27 and 135 forbidden configurations. So the automatic closure that makes
exclusion selective exists at the carrier's grain and structurally nowhere else,
and whether a coarser grain nonetheless selects is one census per grain. The
site grain is the one the declared menu did not carry — a genuine function from
cells to nine objects, unlike the actor relation — and it is run: at the site
grain a hard core admits 324 configurations and selects at 0 of 6 coin classes,
with no shape closing at 6 of 6.

**And the seed conditional is refuted at the grain it typed.** Its injection
premise names actors, and the excitation-to-actor relation is not a function, so
as a description of this representation it does not denote — that is the type
measurement. Supply the injection anyway, as a declaration at the grain it
typed, and arm A2 measures the consequent: both shapes leak, no shape closes,
and the head law returns `OCC-CEILING-PARTIAL` rather than the forced word. The
two clauses are derived separately and the unit's word for the conditional is
their conjunction: MISTYPED-AT-THE-CARRIER; REFUTED-AT-THE-GRAIN-IT-TYPED.

The reading that follows is the unit's, and it is a reading about descriptions.
An exchange shape is selectable on this arena only by a declaration about
co-division pairs — about which conflicts may carry an excitation at once — and
not by any declaration about actors. The record layer speaks of actors, links
and counts, and it names the co-division pair itself: the weld's second leg is
exactly that name. What it has nothing to say about is how many excitations a
link may carry, and the one thing it could have said, said at the actor, kills
both shapes.

## 9. What this decides, and what it does not

**Decided, at the declared scope.**

- The excitation's carrier is the co-division pair: the dictionary's first leg
  is a bijection on nine objects whose image has nine members against the
  carrier's twenty-seven, and the incidence §3 measures runs two ways. An
  excitation-to-actor injection is not a statement about this representation.
- No committed layer forces the occupancy ceiling. There is no occupancy
  coordinate below the excitations to force it with — §4's two-armed census —
  and every declaration that could be added restricts to the same
  one-excitation object, at 53,460 of 53,460 comparisons.
- The closure premise holds vacuously: of the three emission completions, two
  keep the parent's identity, all three keep the menu of a doubly occupied
  carrier nonempty, and none supplies an exclusion. The committed rule is not
  uniformly blind to the distinction — under its record-menu reading it is,
  under its Born-menu reading it is not — and P3 rests on the absent coordinate
  rather than on the blindness.
- The ceiling is two declarations, not one: a value and a grain. At the
  carrier's grain a hard core selects the antisymmetric shape at 5 of 6 coin
  classes; at the actor's grain it selects nothing, because both shapes leak at
  6 of 6 and, at the five non-monomial classes, every admissible configuration
  leaks and every forbidden one is reached, while the monomial class carries 81
  of 216 and 81 of 135.
- The two grains are related by strict containment, not identity: the 27
  carrier-grain leak sources are exactly the same-site configurations and a
  strict subset of the 135 the actor-grain declaration forbids, 108 of them
  excluded. Actor-grain exclusion is strictly stronger than closing the
  carrier-grain leak requires.
- The exchange shape is invisible to actor-grain exclusion as a matter of
  structure: §6's coincidence theorem, at every coin class, with no cell
  available for a cancellation.
- Exclusion selects only at the carrier's own grain: §8's twelve permission
  rows and twelve exclusion rows say where, and where not, and §8's wedge
  theorem says why — the mechanism exists at one grain of the three and the
  site grain's own census is the residual.
- The P4 census does not depend on the record: it is identical at every declared
  probe field, and the count field can only phase entries the zero test does not
  see.

**Not decided, and not attempted.**

- **The ceiling is still declared — and this unit does not declare it either.**
  What is measured is that no committed layer supplies one and that the two
  grains a declaration could use behave differently. Which ceiling this
  substrate has is exactly as open after this unit as before it, and it is now
  open in a sharper place: at the carrier — a grain the record layer names, as
  the weld's own CO-DIVISION-ACTOR-PAIR→LINK leg, but never equips with an
  occupancy coordinate.
- **fermionic-shape is not a theorem of the coupled theory** at this arena. It
  remains available as a declaration at the carrier's grain, at 5 of 6 coin
  classes, and paper-22's own arena is untouched by anything here.
- Two excitations only, one lift. The free lift is inherited as the declared
  shape; a contact term or a distinguishable lift is a different object and is
  not built. Nothing here is about general excitation number, no braid reading
  is taken, and no configuration-space topology is built.
- The grain menu is a declared menu of two, extended here to three by the site
  grain. The lattice of grains between the carrier and the actor is not
  enumerated.
- The controls are declared controls. Their generator is chosen for the property
  under test — every entry nonzero — and no claim is made that either control
  arena is a physical stage.
- Every fraction here is a count over a declared enumeration and none is a
  probability: no measure on configurations, coins, declarations or arenas is
  declared anywhere, and the receipt is stamped COUNTING-ONLY.
- No emission dynamics is run. The three completions are compared at one step on
  declared states; no ensemble, no horizon and no back-reaction is computed, and
  the coupled machine's own admissibility results are cited rather than re-run.
- The no-particle wall stands: *fermionic-shape* and *bosonic-shape* are shape
  words for the antisymmetric and symmetric sectors, and every claim above is a
  claim about a sector of a finite lattice model.

**The choices, and which of them decide.**

| item | fiber | class | verdict-determining |
|---|---|---|---|
| the grain a ceiling is declared at (DECLARED MENU; the space is larger — the site grain is run as a residual) | 2 | MEASURED-BOTH | YES |
| the ceiling value | 2 | MEASURED-BOTH | YES |
| the two-excitation lift | 3 | INHERITED-AS-DECLARED | no |
| the coin class | 6 | MEASURED-ALL | no |
| the emission completion | 3 | DECLARED-AND-ALL-RUN | no |
| the emission reading (the parent's own F10 fiber) | 2 | MEASURED-BOTH | no |
| the control arenas | 3 | DECLARED-CONTROL | no |
| the record, the carrier, the links, the coin order | 1 | FORCED | no |

Two items are verdict-determining, and they are the two halves of one
declaration nobody below has made.

## 10. The instrument

The instrument reads 12 pinned sources by path and hash, holds 8 verbatim
anchors each perturbed at a content-bearing token and required not to locate,
and reads 16 path-value anchors out of the parents' own committed receipts,
every one of them consumed by a named gate that this run evaluates. It shells
out to nothing, consults no version-control state and imports neither parent, so
it reproduces off-tree and on a machine with no git.

Gates bind objects rather than cardinalities: every coin carries its own
monomiality predicate and its own leak row at every declaration and in both
shapes; the set equalities are gated as set equalities, element for element,
with both candidate sets named and both cardinalities published, and the
containment between them gated element by element with its strictness and its
gap; the four declarations' one-excitation restrictions are built from the
declarations themselves and compared as objects; and the actor grain's
completeness is bound per coin in both directions rather than published as a
pool maximum. Every published ratio's denominator is re-counted from the
construction it claims to enumerate, and the check walks the head itself, so a
ratio whose enumeration is undeclared dies inside the run.

The head is a sequence of `LABEL=VALUE` fields built from a declared field spec
whose every field names a receipt path. The audit route is DE-TWINNED: it types
no copy of the template, because a comparator that re-emits the same
concatenation audits the template and not the measurement. It parses the
delivered segments, looks every label up in its own independently typed map from
label to receipt path, compares each value against the serialized receipt,
re-derives each segment's thesis from the predicate that selects it, and
re-derives the outcome word from the premise rows by its own copy of the head
law. A second gate requires every numeral in the head to occur among the
receipt's own measured values, so a number that was written rather than computed
has nowhere to hide.

The paper is verified inside the run. Every claim renders from this run's
measurements and must occur exactly once, and the claim set covers the abstract
in its own words rather than only the body sentences it paraphrases; every row
of the four load-bearing tables — the pool at both grains, the six arms, the
four declarations and the choice inventory — renders the same way, and every
data row the object under test carries must be one of them, so an unrendered
table row is a finding. Every numeral — in prose, in inline code spans and
inside the fenced verdict blocks alike — must be licensed by a measured receipt
value or by a declared structural numeral, and so must every spelled numeral
above twelve; the licensed set is the measured integers together with a declared
handful of exact-rational rows, so prose is not a licence, and digests, source
byte lengths and anchor character counts are excluded from it. The structural
whitelist is itself measured, and an entry the object does not need fails the
gate. The fenced blocks are compared with the derived head by MULTISET EQUALITY,
so an extra fenced verdict block is caught as surely as a missing one. Four
load-bearing sentences carry polarity, so an inverted headline dies. The walls
are instruments: the four inherited abstentions are scanned against this run's
whole measurement layer, each with a falsifier that writes the forbidden reading
into that layer, and the object under test is scanned word by word against a
declared banned list with the shape words surviving only as the compounds the
pin licenses.

Falsifier honesty has three legs and all three are gated. Every declared
falsifier names the symbol it moves and the value it moves it to; the symbol is
re-derived from this file's own abstract syntax tree, the value is read off the
third argument of the falsifier's own hook and matched as a whole token, and the
published description is required to name both on word boundaries; and the sweep
binding requires every falsifier to have been executed and to have died at the
gate it names, with the artifacts untouched. No load-bearing verdict is a typed
constant beside a stamp: P2's and P3's words are both derived from their legs
and gated against those derivations, the seed conditional's own two-clause word
is derived from a type measurement and a leak measurement and compared with the
adjudicated one, and the counts the head publishes are computed rather than
typed.
Every published receipt key is sealed at the moment its gate passes or listed as
declared-unsealed with a forcing; the artifacts are written from the sealed
payload, read back from disk and compared against the gate-time seals, with
every sealed row corrupted in turn on a read-back copy and shown to be detected
first, before either file is promoted by `os.replace`. A run that fails any gate
writes nothing and promotes nothing — the staged files are removed on the way
out, so the failure leaves nothing on disk at all — and the transcript carries
the head it certifies.

## 11. The successor register

Registered, not claimed.

**S-1 — the carrier-grain declaration is the live one.** If a statistics is
wanted on this arena, the declaration that would supply it is a statement about
how many excitations a co-division pair may carry. The record layer names that
object and has never equipped it with such a coordinate, and the first question
for a successor is whether the transport grammar can be given one without
changing what a division event is.

**S-2 — the actor-grain destruction is a result about the geometry, and it is
unexplained.** That no shape closes under actor-grain exclusion is measured at
6 of 6 coin classes and at every admissible configuration of the five
non-monomial classes, and the mechanism is the shift's own incidence structure.
Whether some other walk on the same record admits an actor-grain hard core — and
what such a walk would have to give up — is not measured here.

**S-3 — the emission completion is unowned.** Three completions are run and two
survive the parent's identity. Which one the coupled theory should carry is a
declaration the coupling unit never had to make, and it becomes load-bearing the
moment a second excitation is admitted.

**S-4 — general excitation number.** Every statement here is about two. The
carrier-grain and actor-grain distinction does not obviously collapse at higher
number, and the actor-grain space shrinks fast; nothing about that is measured.

**S-5 — the paper-22 inheritance runs one way.** Its arena had one grain,
because its carrier was a site; the two grains here are a property of a carrier
that is a pair. A successor that changes the carrier changes which of paper-22's
statements transport, and this unit's transport was checked coin by coin rather
than assumed.

**S-6 — the grain lattice, and the weakest closing declaration.** Grains are
quotients of the carrier; three are run here and the lattice between them is not
enumerated. The wedge theorem makes the enumeration cheap — only the carrier's
own grain admits the automatic closure, so every coarser grain costs one census
— and the sharper question is which is the WEAKEST declaration that closes the
carrier-grain symmetric leak, given that removing its 27 sources kills the leak's
source side by construction.

**S-7 — make the probe class a declared coordinate.** Three units have now
measured a declaration invisible to a probe class: the parent's staleness
against single-time closures, paper-22's ceiling against one-excitation objects,
and this unit's ceiling value-and-grain against the committed vocabulary and
construction. The three probe classes are different objects and no unit has made
"probe class" a coordinate it varies, so what is registered here is the SCHEMA
and not a theorem. Distinct from it, and standing on its own: *inexpressibility
is not exclusion* is a type distinction rather than a blindness result — a
representation with no coordinate for a question can neither answer it nor
forbid it — and it is what makes NOT-AVAILABLE a first-class premise verdict.

**S-8 — a registered co-incidence, not a convergence.** A same-hour unit
refining the record layer lands on the unordered co-division pair as the object
its new places are made of, and this unit finds the same object as the carrier
the coupled matter already uses. Both readings are candidate, both are readings
of ONE committed anchor — the weld's own CO-DIVISION-ACTOR-PAIR→LINK leg, which
both units cite — and the grain's name is therefore inherited rather than
co-discovered. No joint claim is licensed until both panels have ruled; what is
registered now is the co-incidence and its shared premise.

**S-9 — what a successor inherits from this unit is a price, not a ceiling.**
There is no ceiling here to inherit. What is inherited is a declaration that
must be made and has two coordinates, a grain menu of three of which only the
carrier's own admits the automatic wedge closure, the three distinct
two-excitation theories as the declared menu at fixed number, the retyped
forcing conditional and its one missing object, and the unowned emission
completion — which S-3 shows becomes load-bearing at the first step that admits
a second excitation.
