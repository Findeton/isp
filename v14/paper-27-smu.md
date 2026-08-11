# SMU — the stationary measure: what declaring a dynamics buys, and what it only moves

**Status:** `DELIVERED` — built against the frozen pin `v14/note-smu-pin.md`
(sha256-12 `a1fca5e7b238`), the successor obligation paper-23 named first.
Verified to run: two plain runs byte-identical, every gate passed, every
declared mutant dead at its declared target, the falsification self-test
fatal at every anchor class and writing nothing. Between delivery and
adjudication every headline below is a **candidate reading**.

## The Measure Derives Once a Dynamics Is Declared — and the Declaration Costs Exactly What the Measure Did

**Unit:** SMU, v14, paper #27.
**Instrument:** `v14/code/smu_exact.py`.
**Artifacts:** `v14/code/smu_output.txt`, `v14/code/smu_receipt.json`.
**Inheritance, hash-verified at run time and by no other route:** the
obligation, the criterion, the invariant simplexes and the withholding
machinery come from paper-23, `v14/paper-23-measure.md` (`79cc67b4f6cd`) with
its instrument (`faf353385905`) and receipt (`c9edf97a5533`), terminal at
commit bb26ca4; the arena — the 640-coin family, the link-indexed
configurations, the chart group, the gauge action, the plaquette loops —
comes from R5, `v14/paper-18-gauge-rung.md` (`62cfe5689d2c`) with its
instrument (`0d98de793b79`) and receipt (`0c02b7684e5b`), terminal at commit
987cd73; the rate source for one declared family is the Γ-iteration terminal,
`v14/paper-16-gamma-iteration.md` (`5c1df50673d4`) with its receipt
(`42255f50328a`), at commit 2895a9a. Every object below is **reimplemented**
from those definitions; nothing is imported from any other unit's program.
**Anchors are (path, value) pairs and (context, consumer) pairs, not only file
bytes:** 9 file-bytes anchors, 30 path-value anchors and 12 verbatim-text
anchors, 51 anchors in all — each verbatim window pinned by the digest of its
exact bytes, by its own frozen character count and by a declared length floor,
each located exactly once, each perturbed at a content-bearing token and
required to stop being locatable, and each bound to the gate that consumes it.
**Exact arithmetic only:** the field is $\mathbb{Q}(\zeta_8)$ carried as
integer 5-tuples over the basis $(1,z,z^2,z^3)$ reduced modulo $z^4+1$ in
lowest terms, so tuple equality is field equality; every probability is an
exact rational; and **every stationary vector in this unit is the exact
kernel of an exact matrix**, obtained by elimination over `Fraction` and never
by iteration, never by a rank estimate and never by a tolerance. An AST scan
of the instrument's own syntax tree is a gate: no float literal, no banned
import, no banned call and no moving reference anywhere, so the run is correct
off-tree and in a directory with no version control at all (#91).
**The seal (#119), native from birth and total:** every published object is
digested at the moment its gate passes; every top-level key of the receipt is
either sealed that way or named in the declaration with the reason it cannot
be; the artifacts are written from the sealed payload through temporaries
moved into place only after the bytes on disk match the gate-time digests.

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field; the complete string —
head included — is compared for equality against an *independent
reconstruction* that derives the head **by a second head law of its own**,
written from the same pre-registered outcomes with a different branch
structure and sharing no format string and no helper with the builder's, and
that re-renders **every segment** from the primitive measured tables, reading
neither the builder's segments nor the builder's counts; and the block below
is compared, character for character under whitespace normalisation, against
the string this run emits — and the paper's fenced blocks are compared as a
**multiset** against the single block this run licenses, so neither a stale
verdict nor a forged twin beside the clean one can be delivered:

```
SMU-DYNAMICS-RELATIVE-SPREAD-153/380-OVER-12-DERIVING-INSTANCES-<CENSUS=6-FAMILIES-18-INSTANCES-ALL-RUN-12-DERIVE-6-REDUCIBLE|CRITERION=A-COVARIANT-CHAIN-DERIVES-IFF-IT-HAS-EXACTLY-ONE-CLOSED-COMMUNICATING-CLASS|THE-INHERITED-FORM-IS-SUFFICIENT-NOT-NECESSARY-WITNESS-AT-3-STATES-2-CLASSES-1-CLOSED -- (a)CHART-WALK=THE-ANCHORED-CHART-ACTS-TRIVIALLY-32-OF-32-ELEMENTS-INDUCE-THE-IDENTITY-SO-640-CLOSED-CLASSES-AND-THE-WHOLE-639-SIMPLEX-IS-STATIONARY;THE-EXTENSION-DOES-NOT-ACT-ON-THIS-CARRIER-AT-ALL-64-OF-128-ELEMENTS-CARRY-A-UNIFORM-CONFIGURATION-OFF-IT-AND-ITS-CLOSURE-IS-1248-STATES-WITH-336-CLOSED-CLASSES -- (b)GAUGE-WALK=REDUCIBLE-AT-BOTH-READINGS-208-AND-120-CLOSED-CLASSES-IDENTICAL-AS-SETS-TO-THE-PARENTS-ORBITS-AND-ITS-STATIONARY-SIMPLEX-IS-THE-PARENTS-INVARIANT-SIMPLEX-DIMENSION-207-AND-119 -- (c)LAW-NATIVE-RESAMPLING=IRREDUCIBLE-AND-DERIVES-AT-ALL-6-MEMBERS-OF-ITS-DECLARED-FIBRE;THE-MEASURE-IS-NEW-SECTOR-GRADED-AT-15/38-5/19-13/38-AND-INVARIANT-SO-IT-IS-A-POINT-OF-THE-PARENTS-SIMPLEX -- (d)COMPOSITION-WALK=IRREDUCIBLE-ON-BOTH-SIDES-AND-DERIVES-THE-COUNTING-MEASURE-BECAUSE-THE-FAMILY-IS-CLOSED-UNDER-INVERSE-640-OF-640-SO-THE-WALK-IS-DOUBLY-STOCHASTIC-WITH-278528-OF-409600-PRODUCTS-STAYING -- (e)MONOMIAL-HAAR-WALK=REDUCIBLE-5-CLOSED-CLASSES-OF-128-AND-ONE-OF-THEM-IS-EXACTLY-THE-PARENTS-HAAR-CARRIER-SO-THE-CORPUS-ONE-HANDED-OVER-MEASURE-IS-ONE-EXTREME-POINT-HERE -- (f)COVARIANT-METROPOLIS=EVERY-DECLARED-INVARIANT-TARGET-IS-REACHED-EXACTLY-3-OF-3-AND-THE-NON-INVARIANT-CONTROL-LANDS-OUTSIDE-THE-SIMPLEX-ORBIT-CONSTANT=FALSE;EXHAUSTIVE-ARM-55-TARGETS-0-FAILURES -- MEASURES=10-DISTINCT-STATIONARY-VECTORS-OVER-12-DERIVING-INSTANCES|NAMED-NULLS-REACHED=COUNTING,ORBIT-UNIFORM-CHART-128,ORBIT-UNIFORM-CHART-32|NEW=7 -- RELATIVITY=THE-MEASURE-MOVES|WIDEST-SPREAD-OVER-THE-11-GAUGE-COVARIANT-DERIVING-INSTANCES=153/380-ATTAINED-ON-1-OF-4-SETS(DEFECT-CARRYING)|OVER-ALL-12-DERIVING-INSTANCES-THE-DECLARED-NON-COVARIANT-CONTROL-INCLUDED=1701/3800|AGAINST-THE-PARENTS-WIDEST-OVER-INVARIANT-MEASURES-27/130-SO-DECLARING-A-DYNAMICS-MOVES-THE-PARENTS-OWN-HEADLINE-SETS-FURTHER|QUASI-DERIVATION-ARM-REACHABLE-AND-MEASURED-TO-FAIL -- PRICE=CONSERVED-NOT-PAID:THE-COVARIANT-DYNAMICS-FIBRE-SURJECTS-ONTO-THE-INVARIANT-SIMPLEX-SO-A-DECLARATION-STILL-SUPPLIES-207-INDEPENDENT-NUMBERS-AT-THE-ANCHORED-READING-AND-119-AT-THE-EXTENSION-EXACTLY-THE-PARENTS-COUNTS|WHAT-MOVED-IS-WHERE-THE-DECLARATION-IS-MADE-NOT-HOW-MUCH-IT-COSTS -- WILSON=LICENSED-BY-THE-PIN-AND-STAMPED-CONDITIONAL-ON-THE-DECLARED-DYNAMICS-AT-12-OF-12-ROWS|OBSERVABLE=THE-TRACE-OF-THE-PLAQUETTE-HOLONOMY-ON-ITS-OWN-FOUR-CORNER-BLOCK-PLAQUETTE-INDEPENDENT-AT-16-PLAQUETTES-AND-GAUGE-INVARIANT|VALUES=107/76@NEW,111/76@NEW,13/10@COUNTING,19/13@ORBIT-UNIFORM-CHART-32,205/152@NEW,207/152@NEW,219/152@NEW,225/152@NEW,263/200@NEW,29/20@ORBIT-UNIFORM-CHART-128|RANGE-OVER-THE-INVARIANT-SIMPLEX=[0,4]-BOTH-ENDPOINTS-ATTAINED-AT-EXTREME-POINTS-SO-COVARIANCE-PINS-THE-EXPECTATION-NOWHERE|NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-0-LOOP-FAMILIES-GROWN -- SCOPE=D=2;L=4;FIELD=Q(zeta_8);COINS=640;LINKS=32;PLAQUETTES=16;CARRIER=THE-PARENTS-PRIMARY-CARRIER-THE-640-UNIFORM-CONFIGURATIONS(PLUS-THE-EXTENSIONS-1248-STATE-CLOSURE-WHERE-THE-EXTENSION-IS-DECLARED);FULL-CONFIGURATION-SPACE=640^32-NOT-A-CARRIER-HERE;ELIMINATION-CAP=208-EVERY-EXACT-SOLVE-AT-OR-BELOW-IT;LOCALITY-IS-DEGENERATE-ON-THIS-CARRIER-ONE-COIN-SERVES-ALL-32-LINKS;THE-DYNAMICS-ARE-DECLARED-NOT-DERIVED;NO-ACTION;NO-COUPLING;NOT-QCD;NO-CONFINEMENT-CLAIM>
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and what could have answered the other way

Paper-23 ran nine candidate sources for a measure on R5's configurations, and
none derived. It named a tenth and could not price it, in one sentence quoted
here from its own pinned bytes:

> A stationary measure needs a dynamics to be stationary for.

and it wrote down, in advance, exactly what a unit that supplied one would
owe:

> a covariant chain's stationary measures are invariant, so it can only ever
> pick a point of the same simplex, and it fixes that point uniquely exactly
> when **irreducibility** supplies the transitivity the symmetry group does
> not

This unit declares the dynamics. Six families, 18 declared instances, every
one of them run; 6 families and 18 declared instances is the whole census and
not a sample of it, because every declared axis is swept to the bottom.
12 of them derive and 6 are reducible. And the question the pin exists for is
then asked on the objects: **the stationary measure MOVES across the
declared-dynamics fibre.**

**What could have answered the other way.** Five outcomes were pre-registered
in the pin, and the head law that chooses between them is handed synthetic
census tables in the delivery run and required to return each one, so a head
law that had collapsed to a constant dies inside the run.

| pre-registered outcome | reachable how | measured |
|---|---|---|
| `SMU-DERIVED` | a census in which every deriving instance carried the same vector, with the reducible ones absent | not the case: the deriving instances carry 10 distinct stationary vectors |
| `SMU-QUASI-DERIVED` | all deriving instances agree — decided by comparing their vectors entry by entry, not inferred | the vectors are compared and disagree |
| `SMU-REDUCIBLE` | no declared dynamics has a single closed class | 12 do |
| `SMU-DYNAMICS-RELATIVE` | the deriving instances disagree and the spread is positive | **this is what is measured** |
| `SMU-BLOCKED-AT` | an object that cannot be evaluated at all | every declared instance is evaluable and is evaluated |

The falsifiability of this unit lives in the class counts and in the spread
table, and both could have gone the other way. Three separate declared
dynamics do land on the same measure — the counting measure — by three
different routes; had the other nine landed there too, this paper would carry
the strongest head the pin allows, and the head law that would have emitted it
is exercised in the delivery run.

## 2. The arena and the carrier, declared as data (§15)

The stage is R5's, rebuilt here rather than quoted. The lattice is
$(\mathbb{Z}_L)^2$ at the anchored size $L = 4$ and the anchored dimension
$d = 2$: 16 sites, 32 links and 16 plaquettes, the link and plaquette sets
derived from the lattice rather than declared. The coefficient alphabet
returns 25 elements and the coin family, enumerated exhaustively over the
admissible rows, returns 640 coins splitting into 64 diagonal, 64
antidiagonal and 512 balanced with nothing left over, every one confirmed
unitary by a second route.

**The carrier is the parent's own primary carrier**: the 640 uniform
configurations, one coin repeated on every link, which paper-23 measured to
be exactly the chart-fixed locus of the anchored chart. Two things follow and
both are disclosed rather than discovered by a reader. First, this is where
the parent's simplex lives, so the two units weigh the same partition and are
comparable object for object. Second, **link-locality is degenerate here**:
one coin serves all 32 links, so a "local" resampling and a global one are
the same chain, and no claim about locality is available at this carrier. The
full configuration space is $640^{32}$ and is not a carrier of this unit; it
is named in the scope segment and again in section 12.

**The two measured symmetries.** The residual gauge group on the carrier is
measured by propagation — which constant link twists a site-diagonal gauge
can realise on the torus — and returns the even twists, of order 4 at the
anchored chart reading and of order 8 once the extension's swap conjugation
is admitted. Its orbits are 208 and 120, landing on paper-23's own orbit
counts at named receipt paths. The chart group's action is measured
separately, and section 4.1 reports what that measurement found.

## 3. The criterion, and the one place the inherited form is loose

The pin hands down paper-23's law as the gate: derives iff irreducible. This
unit applies it and, in applying it, measures that **the inherited form is
sufficient and not necessary**. What decides whether a chain fixes a measure
is not irreducibility but the number of **closed** communicating classes: the
stationary simplex has dimension one less than that number, so the chain
fixes a point exactly when it has one closed class. Irreducibility implies
one closed class; the converse fails.

The gap is exhibited rather than argued. A declared three-state chain with one
transient state has more than one communicating class — so it is not
irreducible — yet exactly one closed class and a stationary simplex of
dimension zero, computed by the same exact elimination every instance of the
census uses. It derives. And the identity the reducible verdicts are read
through is verified **exhaustively** on a declared family of small chains,
every one of them solved by the same elimination, with the kernel dimension
and the closed-class count agreeing at every member.

On this census the distinction does not bite — no declared instance has a
transient class at all — which is itself worth recording, because it is the
reason the two readings return the same twelve deriving instances here. The
correction is to the *law*, not to the parent's verdict.

## 4. The declared-dynamics census

Six families. Each is declared in the instrument — its carrier, its transition
law written out, its fibre axis and its declared covariance group — and each
is gated on **its own** objects: row-stochasticity per row, covariance per
generator and per row, communicating classes from its own support, and the
identity $\pi P = \pi$ verified at full size for every vector it publishes.
None is privileged.

| # | family | fibre axis | fibre | irreducible | closed classes | the stationary measure |
|---|---|---|---|---|---|---|
| (a) | the chart-group walk | which chart | 2 | no | 640 / 336 | the whole simplex / orbit-uniform combinations |
| (b) | the gauge-action walk | which residual reading | 2 | no | 208 / 120 | exactly paper-23's invariant simplex |
| (c) | the law-native resampling | which sector carries which position | 6 | yes | 1 | NEW, sector-graded, and invariant |
| (d) | the composition walk | which side composes | 2 | yes | 1 | the counting measure |
| (e) | the monomial-Haar walk | which side multiplies | 2 | no | 5 | paper-23's Haar, and four classes it does not reach |
| (f) | the covariant Metropolis family | which invariant target | the simplex itself | yes | 1 | the declared target, exactly |

### 4.1 (a) The chart-group walk — and the first surprise

Whether a declared group **acts** on a declared carrier is a measurement, and
this unit takes it first, element by element: an element carries a uniform
configuration to a uniform one exactly when its reversal flag is constant over
the link set.

At the anchored reading every element has no reversal at all, so the chart
group acts — and the permutation it induces on the carrier is the identity at
every one of its 32 elements. The walk is therefore the identity chain, with
640 closed classes and a stationary simplex of dimension 639: **every measure
on the carrier is stationary for it.** The chart walk decides nothing, and
that is not a defect of the declaration but a measurement of what the chart
symmetry is worth as a dynamics.

At the extension reading the answer is sharper: **the extension does not act
on this carrier** at all. 64 of 128 extension elements carry a uniform
configuration off the carrier, because their reversal flag is mixed — some
links reversed, others not — and the image assigns one coin to one direction
class and its swap conjugate to the other. A walk cannot be declared there
without enlarging the carrier, so the instrument computes the smallest carrier
on which the extension does act, as an orbit closure taken to a fixed point:
the closure is 1248 states, and on it the walk has 336 closed classes.

The mechanism is worth one sentence, because it explains why this is not an
error in the parent. The carrier is the *fixed locus* of the anchored chart,
and a fixed locus is an invariant set only for elements that normalise the
group fixing it. The extension elements that do carry the carrier into itself
are measured and counted: the 32 that reverse no link and the 32 that reverse
every link. The rest do not, and paper-23 never needed them to — it took a
fixed locus, not an orbit. What follows is only this: a *dynamics* at the
extension reading lives somewhere other than a *census* at the extension
reading does.

### 4.2 (b) The gauge-action walk — the weld

The gauge walk is reducible at both readings, with 208 and 120 closed classes,
and those classes are compared with paper-23's orbits **as sets**, class by
class and never by cardinality: the two partitions are identical at both
readings. The dynamics layer's decomposition and the static layer's orbit
census are the same object arrived at twice.

The consequence is the sharpest weld in the unit. An invariant measure is
exactly an orbit-constant one; a group walk's stationary measures are exactly
the invariant ones; so **the gauge walk's stationary simplex IS paper-23's
invariant simplex**, of dimension 207 at the anchored reading and 119 at the
extension. The dynamics did not shrink the parent's simplex by one number.

### 4.3 (c) The law-native resampling — the candidate the pin named

The pin names the Γ-iteration's law-native normaliser as the rate source, and
what enters here is a law value rather than a carrier statistic, for a reason
that unit measured and this one quotes from its pinned bytes:

> it holds under an arbitrary exact re-pricing of every priced event, so it is
> law-native and not a fact about this carrier

Its step-normalised positional law is read at named receipt paths at both
legs and measured to be a probability vector of three distinct positive
values. One step of this dynamics discards the current coin and draws a new
one: a sector by that law, then uniformly inside the sector. The sector-to-
position assignment is a genuine free choice with fibre 6, and all six
members are built and run.

Every one is irreducible — one closed class over the whole carrier — and
derives. The measure is NEW: it is neither of the counting nulls nor either
orbit-uniform null, and its value profile is flat inside each sector and
different between them. It is also **invariant**, because the sectors are
unions of orbits, so it is a point of paper-23's simplex — the first point of
that simplex anything in this corpus has supplied.

### 4.4 (d) The composition walk — the one that lands on a named null

One step composes the current coin with a uniformly drawn member of the family
and stays put when the product leaves the family. That the product sometimes
leaves is the parent's own measurement, reproduced here: 278528 of 409600
products stay inside the family.

Two facts decide this row and both are measured rather than assumed. The
family is closed under inverse at 640 of 640, which is exactly the identity
that makes the rejection walk **doubly stochastic**; and the walk is
irreducible on both sides. A doubly stochastic irreducible chain has the
counting measure as its unique stationary measure, and that is what the exact
solve returns.

So the counting measure — paper-23's declared null, the one it called the
least informative measure the arena admits — is *derived* here, given a
declared dynamics built only out of the family's own multiplication.

### 4.5 (e) The monomial-Haar walk — where the corpus's one canonical measure lands

Paper-23's single positive finding was that the 128 monomial coins form a
group, so the arena hands over exactly one measure: Haar on them. Multiplying
by a uniformly drawn member of that group is a dynamics, and it never carries
a coin out of the family.

It is reducible: 5 closed classes of 128, and one of them is compared with the
parent's Haar carrier **as a set** and is exactly it. So the corpus's one
handed-over measure appears here as one extreme point of one declared
dynamics' stationary simplex — and the other four extreme points are the
classes that measure does not reach, every one of them inside the interfering
sector where the parent measured the composition defect to live.

### 4.6 (f) The covariant Metropolis family — the fibre's own size

The last family is declared because a census that measures only the dynamics
it was handed cannot report what the fibre costs. One step proposes a
uniformly drawn configuration and accepts it with the usual ratio at a
declared target. At an invariant target the chain is measured covariant under
the residual gauge group, irreducible, reversible with respect to that target
at zero detailed-balance failures, and its unique stationary measure is the
target itself.

Three declared invariant targets are reached exactly. A fourth instance is a
**control**: the same construction at a target measured *not* to be constant
on the parent's orbits. It derives too — and its stationary measure is
measured not to be orbit-constant, and the chain itself is measured not to be
gauge-covariant. So it is covariance, and not dynamics, that confines the
answer to the parent's object.

## 5. The exact solve, and how uniqueness is gated

Every stationary vector this unit publishes is the exact kernel of an exact
matrix, and the route is declared per instance. Where no quotient is declared
and every closed class is at or below the declared elimination cap, the chain
restricted to each class is solved directly — that is every reducible
instance, whose classes are small because the group orbits are. Where a class
is larger than the cap — the twelve deriving instances each carry one closed
class spanning the whole carrier — the solve goes through a quotient:
lumpability
is measured block by block, the blocks are the orbits of a group measured
transitive on each of them, the quotient is solved by the same elimination,
and the within-block distribution follows. The cap is not a free number: it is
set to the parent's own orbit count, so every exact solve this unit performs
is at or below the size of the parent's simplex.

Uniqueness is never asserted. It is the closed-class count, computed from the
chain's own support, read through an identity verified exhaustively on small
chains; and whatever route produced a vector, that vector is verified against
its own transition law at **full** size before it is published.

## 6. The dynamics-relativity census

Every mass below is labelled with the declared dynamics whose stationary
measure produces it, and the configuration column is a count and is stamped
COUNTING-ONLY (E-24). Each set is checked to be a union of orbits at both
readings, orbit by orbit and never by a cardinality, so its mass is well
defined under every invariant measure compared. The sets are the parent's own
headline sets, rebuilt here from their definitions rather than quoted.

| set | configurations (COUNTING-ONLY) | composition walk | law-native (012) | orbit-uniform, chart-32 | orbit-uniform, chart-128 |
|---|---|---|---|---|---|
| NON-FLAT | 632 | 79/80 | 289/304 | 25/26 | 23/24 |
| NON-COMMUTING | 576 | 9/10 | 23/38 | 9/13 | 7/10 |
| DEFECT-CARRYING | 384 | 3/5 | 39/152 | 6/13 | 7/15 |
| DIAGONAL | 64 | 1/10 | 15/38 | 4/13 | 3/10 |

Two of those columns reproduce paper-23's published masses exactly, at named
receipt paths, which is what makes the new columns comparable at all.

The widest spread over the 11 gauge-covariant deriving instances is 153/380,
attained on DEFECT-CARRYING; over all 12 deriving instances it is 1701/3800,
the declared non-covariant control included. Both are to be read against the
number the parent measured over its own invariant measures: the parent's
widest spread over invariant measures was 27/130.

So **declaring a dynamics moves the parent's own headline sets further than
declaring a measure did.** That is the measurement, and it is the opposite of
what a reader might expect from a unit whose job was to supply the missing
object: supplying it did not narrow the answer, it widened the reachable
range. The quasi-derivation arm — the pin's strongest honest outcome — is
decided by comparing the deriving vectors entry by entry rather than inferred
from this table, and it fails.

## 7. The price is conserved, not paid

The census makes the mechanism visible, and it is worth stating as sharply as
the measurements allow.

A covariant chain's stationary measures are invariant, so a covariant chain
that derives picks a point of the invariant simplex. That is the parent's
sentence and this unit confirms it instance by instance. But the converse is
what prices the declaration, and it is where the census earns its last family.
The Metropolis construction is uniform in its target: handed any invariant
measure of full support it returns a chain that is covariant because the
target is orbit-constant, irreducible because the proposal is, and reversible
with respect to that target — so the target is its unique stationary measure.
That is a theorem about the construction, and this unit does not ask a reader
to take it on trust twice over. It is instantiated at three declared invariant
targets, each measured covariant, irreducible, reversible at zero
detailed-balance failures and landing on its target exactly; and it is
verified **exhaustively** on a declared small carrier, where every invariant
target at a declared denominator is enumerated — 55 targets at a declared
denominator, 0 failures, every one reached exactly.

The full-support restriction is the honest edge of the statement: a target
with a zero is the stationary measure of a chain irreducible on its support
and therefore reducible on the carrier, so the reach is onto the simplex's
interior and onto its boundary only through the reducible arm this census
already reports.

The covariant-dynamics fibre therefore surjects onto the invariant simplex, so
declaring a covariant irreducible dynamics on this carrier still supplies
exactly 207 independent numbers at the anchored reading and 119 at the
extension — paper-23's own counts, unchanged. What moved is *where* the
declaration is made, not how much it costs. A programme that hoped to buy the
measure by declaring a dynamics has bought the same object under a different
name, at the same price, with one thing added: a dynamics is more data than
the measure it produces, so the move is not free even where it is not
expensive.

That is the sentence this unit was built to be able to say, and it is the one
the pin's fourth stage was for.

## 8. The licensed segment: expectations, conditional

Paper-23 withheld the Wilson segment because nothing derived. The pin licenses
it here under one condition, quoted from its own bytes:

> expectations are computable ONLY under a measure that derives at the RSQ
> standard GIVEN the declared dynamics

and requires every expectation to carry the stamp
CONDITIONAL-ON-THE-DECLARED-DYNAMICS. That licence is enforced on the product
and per row, not per table: every published expectation names the dynamics it
is conditional on, that dynamics' verdict is looked up in the census this run
computed, every row carries the stamp, and the payload is walked to the bottom
for an expectation-valued key at any depth. An expectation under a reducible
dynamics, or an unstamped one, dies on the delivery run; two mutants plant
exactly those.

**The observable.** It is rebuilt from R5's own definition:

> the holonomy is the ordered product of the four link operators around the
> boundary, each inverted where the boundary runs against the link's own
> direction

and

> the whole holonomy lives in a four-by-four block

so the declared observable is that block's trace. The full carrier trace is
measured to be the same quantity plus the untouched identity, so the
normalisation fibre is 2 and both members are published. The value is
independent of which plaquette on this carrier — checked at every plaquette
and every configuration — it lies in the real subfield $\mathbb{Q}(\sqrt2)$ at
every one of the 640 configurations, it takes 11 distinct values there, and it
is constant on every orbit of the residual gauge group.

**The expectations, each conditional on its declared dynamics.** 13/10 under
COMPOSITION-LEFT; 13/10 under COMPOSITION-RIGHT; 13/10 under
METROPOLIS-AT-COUNTING; 19/13 under METROPOLIS-AT-ORBIT-UNIFORM-CHART-32;
29/20 under METROPOLIS-AT-ORBIT-UNIFORM-CHART-128; 225/152 under
LAW-NATIVE-012; 111/76 under LAW-NATIVE-021; 205/152 under LAW-NATIVE-102;
207/152 under LAW-NATIVE-120; 107/76 under LAW-NATIVE-201; 219/152 under
LAW-NATIVE-210; and 263/200 under METROPOLIS-AT-A-NON-INVARIANT-TARGET, which
carries the control's own reading and not the arena's.

**And here is what the segment is worth.** Because the observable is constant
on orbits, its expectation under an invariant measure is a convex combination
of its orbit values, so the range of the expectation over the invariant
simplex is exactly [0, 4] — the full range of the observable itself, both
endpoints attained at single-point orbits, which are extreme points of the
simplex. Covariance pins the expectation nowhere. An expectation on this arena
is not a number the arena has; it is a coordinate of the declaration, and the
declaration can put it anywhere the observable goes.

This unit therefore reports expectations as expectations. It grows no loop
family and makes no claim about how any expectation would behave as a loop
grows: 0 loop families are grown, and the pin's inherited must-not — no
area-law, string-tension, or potential claim — is swept over this paper's own
text on the delivery run with the declaring sentences removed first.

## 9. What this decides, and what it does not

**Decided, at the declared scope.**

- **The stationary measure derives, per declared dynamics, at 12 of 18
  instances**, each by exact linear algebra with uniqueness gated by a class
  count and every vector verified at full size.
- **The inherited criterion is corrected**: what decides is the closed-class
  count, and the witness that separates it from irreducibility is exhibited.
- **The gauge walk's stationary simplex is paper-23's invariant simplex**,
  class by class as sets, at the parent's own two dimensions.
- **The extension does not act on the parent's carrier**, and the smallest
  carrier on which it does is computed.
- **A named null is derived from the arena's own multiplication** — the
  counting measure, by the composition walk on both sides — and **a new
  measure is derived** by the law-native resampling at all six members of its
  fibre. Both orbit-uniform nulls are also reached, but by chains built *from*
  those measures: that is the surjection of section 7 and not a second
  derivation, and the paper counts it as pricing rather than as evidence.
- **The measure moves**, and the movement is priced on the parent's own sets,
  wider than the parent's own spread over invariant measures.
- **The price is not reduced by the move**: the covariant-dynamics fibre
  surjects onto the invariant simplex.

**Not decided, and named.**

- **The full configuration space.** Everything above is measured on the
  parent's primary carrier. The dynamics declared here all have obvious
  analogues on $640^{32}$; none is run, and the exact solve there is out of
  reach by cost, not by argument.
- **Locality.** This carrier cannot see it: one coin serves every link, so a
  link-local resampling and a global one coincide. A dynamics whose locality
  is a real property needs a carrier where configurations differ link to link,
  and the enlarged carrier of section 4.1 is the smallest one this unit built.
- **Which dynamics to declare.** This unit prices the declaration and does not
  make it. The census shows the fibre is as large as the simplex, so a pin
  that declares one owes an argument this arena does not supply — the same
  debt paper-23 recorded, relocated but not discharged.
- **Convergence.** Nothing here is a claim about approach to stationarity.
  Uniqueness of the stationary measure needs one closed class and not
  aperiodicity, so no mixing statement is made or needed; aperiodicity is
  measured and published per instance, and used for nothing.

## 10. The instrument

The instrument is `v14/code/smu_exact.py`, and its contract is the era's
minimum (#82): a delivery run that is the only writer, a `--no-write` twin, a
falsification self-test that corrupts one anchor class in memory and must die
writing nothing, a per-mutant runner, an all-mutants sweep, gate and mutant
listings, and a `--verify-paper` mode. Unknown flags exit 2. No flag is a
no-op and no flag is mutant-only. The exit conventions invert the usual
reading and are therefore disclosed in the usage string, in the receipt and
here: the delivery run exits 0 on success and 1 on any refusal, writing
nothing; `--selftest` exits 0 when every anchor class is fatal; `--mutant`
exits 0 when the named mutant *dies* on its declared target.

The gate ledger is chained row by row, so that a row edited after its gate
closed no longer matches the digest of its own predecessor. 52 gates close
before the paper gates, 18 of them binding one declared instance each, and 5
paper gates and 2 closing gates follow — the last two being the seal and the
artifact integrity check, which cannot be inside the ledger they close over.
The per-instance gates exist because a census gate that binds only the total
is vacuous at the per-object level (#87). 42 declared mutants, all dead, each at
the gate it was declared to falsify — and the registry is checked TOTAL
against the instrument's own syntax tree, so a falsifier cannot exist as an
unswept branch, none can be declared without a branch to fire, and a switch
the scan cannot read is fatal rather than forgiven. Each mutant's published
description names the exact token it plants and that token is located in the
source text of that mutant's own branch, so a description-inverted mutant
dies here rather than in a reader's trust (E-23). The coverage is published at
an honest denominator (#34): of the gates this run closes, 34 are the declared
targets of falsifiers, 16 are the per-instance gates under one registered
forcing, and 0 are uncovered — the forcing being machine-checked rather than
asserted, since the per-instance gate's predicate is verified to name no
instance, so the two falsifiers that fire it at two different instances fire
the identical predicate every instance is judged by. The two gates no
falsifier reaches are named with the reason, not counted as covered. 51 anchors in all: 9
file-bytes anchors, 30 path-value anchors and 12 verbatim-text anchors, each
window pinned by its own digest and its own frozen character count against a
declared floor, each located exactly once under whitespace and markdown-prefix
normalisation (#125), each perturbed at a content-bearing token and required
to stop being locatable, and each bound to the gate that consumes it.

The paper gates run in five legs, in the plain delivery run and not in a
separate mode (#20): claim rendering at exact occurrence counts, the complete
verdict string by equality, the must-not vocabulary sweep with the declaring
sentences removed first, claim polarity, and numeral coverage over every
numeral including the fenced verdict block, the inline code spans and both
sides of every fraction (E-22). The fenced blocks are compared as a multiset,
so a forged twin beside the clean one dies. The structural literals the
coverage gate is permitted to forgive — section numbers and the engraving
references — are published in the receipt, so a reader can see exactly what it
was allowed to forgive.

Every published object carries the gate-to-disk seal, and the manifest — each
object, the receipt key it was taken at, the gate whose passing took it, and
the digest — is published in the receipt. The manifest is **total**: 23 objects are
sealed before the paper gates, more are sealed by the paper gates themselves,
and every other top-level key is named in the declaration with the reason it
cannot be sealed. The gate ledger is snapshotted before the two
closing gates and the snapshot is what is sealed and written — a seal cannot
be inside the object it seals.

**The choice inventory.** 11 construction choices are inventoried, of which 5
are measured verdict-determining, each with its fibre and its instances. The
lattice and the coin family are FORCED with fibre 1; the elimination cap is
FORCED-BY-COST and set to the parent's orbit count; the carrier is
DECLARED-AND-DISCLOSED at fibre 2, both instances built; and every declared
dynamics axis is DECLARED-AND-SWEPT, with the number of instances built equal
to the fibre at every one of them, so no member of a declared fibre is left
unrun. The verdict-determining flag binds each row by its own measured
predicate — re-running that axis at another instance moves a published vector
— and not the total, which is what makes the two axes that are *not*
verdict-determining informative: composing on the left and composing on the
right give the same measure, so that side is a free choice with no
consequence, while multiplying by the monomial group on the left and on the
right does not.

## 11. The successor register

- **The full-space dynamics.** Every family declared here has an obvious
  analogue on $640^{32}$, and the interesting question — whether locality
  changes any of these answers — cannot be posed on this carrier at all. The
  first tractable step is the 1248-state closure this unit built, where
  configurations already differ direction to direction.
- **The declaration itself, with its pin.** The fibre is now measured to be
  the whole invariant simplex. A unit that wants one measure must argue for
  one point, and section 7 is the exact statement of what that argument owes.
- **The law-native family, pressed.** Its rates are law values and its measure
  is a point of the parent's simplex, which makes it the only candidate in
  this census with a claim to be more than a declaration. Whether the
  sector-to-position assignment can be forced — the axis this unit measures a
  fibre of 6 on — is open, and it is the one place a genuinely derived measure
  could still come from.
- **The extension's carrier.** That the parent's carrier is not closed under
  the parent's own declared extension deserves a unit of its own: the census
  questions paper-23 answered at the fixed locus can be re-asked at the
  closure, where the simplex is a different object.
- **Expectations at a second observable.** This unit computes one loop
  observable and reports that covariance pins its expectation nowhere. Whether
  some *other* gauge-invariant functional on this carrier has a narrower range
  over the invariant simplex is not decided here, and a functional whose range
  were a point would be the first quantity this arena hands over free.

## 12. Deviations, and the register of scope

The pin's arena, gates and must-nots are followed as written. Four points are
recorded as scope rather than deviation.

First, the pin names three candidate dynamics and this unit runs those three
plus three more. The extra are not padding: the composition walk is the only
one built purely from the family's own multiplication, the monomial walk is
where the corpus's one canonical measure lands, and the Metropolis family is
what prices the fibre — without it the census could report that the measures
disagree but not that the disagreement is exactly as large as the parent's
simplex.

Second, the exact elimination is capped, and the cap is disclosed rather than
hidden: above it the solve goes through a measured lumping to a quotient at or
below the cap. Both legs are exact linear algebra and every vector is verified
against its own chain at full size; what the cap costs is not correctness but
a direct 640-dimensional elimination, which is out of reach by time alone.

Third, the relativity spread is published twice — over the gauge-covariant
deriving instances and over all of them — because only the first is
like-for-like with the parent's number, and a single figure would have
flattered or exaggerated depending on which was chosen. The head carries the
like-for-like one.

Fourth, the Wilson segment is reported as expectations and nothing else. Every
value is conditional on a declared dynamics and says so in its own row; the
range measurement in section 8 is the honest summary of how much the arena
constrains any of them, which is: not at all.
