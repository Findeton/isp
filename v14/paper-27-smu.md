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
machinery come from paper-23, `v14/paper-23-measure.md` (`79cc67b4f6cd`),
with its instrument `v14/code/r5m_measure_exact.py` (`faf353385905`) and its
receipt `v14/code/r5m_measure_receipt.json` (`c9edf97a5533`), terminal at
commit bb26ca4; the arena — the 640-coin family, the link-indexed
configurations, the chart group, the gauge action, the plaquette loops —
comes from R5, `v14/paper-18-gauge-rung.md` (`62cfe5689d2c`), with its
instrument `v14/code/r5_gauge_exact.py` (`0d98de793b79`) and its receipt
`v14/code/r5_gauge_receipt.json` (`0c02b7684e5b`), terminal at commit
987cd73; the rate source for one declared family is the Γ-iteration terminal,
`v14/paper-16-gamma-iteration.md` (`5c1df50673d4`), with its receipt
`v14/code/giter_receipt.json` (`42255f50328a`), at commit 2895a9a. Each
digest is bound to its own path, so a pair of them exchanged between two
sources dies on the delivery run rather than reading as two digests that are
both still present. Every object below is **reimplemented**
from those definitions; nothing is imported from any other unit's program.
**Anchors are (path, value) pairs and (context, consumer) pairs, not only file
bytes:** 9 file-bytes anchors, 30 path-value anchors and 12 verbatim-text
anchors, 51 anchors in all — each verbatim window pinned by the digest of its
exact bytes, by its own frozen character count and by a declared length floor,
each located exactly once, each perturbed at a content-bearing token and
required to stop being locatable, and each bound to the gate that consumes it.
Every quotation this paper makes of a parent is additionally required to lie
**inside** one of those windows, so a paper that misquotes — or inverts — a
definition it attributes to a parent dies on the delivery run.
**Exact arithmetic only:** the field is $\mathbb{Q}(\zeta_8)$ carried as
integer 5-tuples over the basis $(1,z,z^2,z^3)$ reduced modulo $z^4+1$ in
lowest terms, so tuple equality is field equality; every probability is an
exact rational; and **every stationary vector in this unit is the exact
kernel of an exact matrix**, obtained by elimination over `Fraction` and never
by iteration, never by a rank estimate and never by a tolerance. An AST scan
of the instrument's own syntax tree is a gate: no float literal, no banned
import, no banned call and no moving reference anywhere, so the run is correct
off-tree and in a directory with no version control at all (#91).
**The seal (#119), native from birth, total, and taken at value-close:** every
published object is digested at the moment the gate that vouches *its own
values* passes — each of the 18 instance records at its own gate, each
sub-object at the gate that measured it, with every omission declared in its
manifest row; every top-level key of the receipt is either sealed that way or
named in the declaration with the reason it cannot be; and the artifacts are
written to temporaries, read back and compared against the gate-time digests
**before** either is moved into place, so a refusing integrity gate promotes
nothing.

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field; the complete string —
head included — is compared for equality against an *independent
reconstruction* that derives the head **by a second head law of its own**,
written from the same pre-registered outcomes with a different branch
structure, sharing no format string and no helper with the builder's, and
**de-twinned from it**: the second law accepts neither of the builder's
aggregates, recounting the covariant deriving population from the instance
records one by one and re-taking the widest spread as a maximum over the
published rows, so an edit to one head law alone cannot survive. It re-renders
**every segment** from the primitive measured tables, reading neither the
builder's segments nor the builder's counts; and the block below is compared,
character for character under whitespace normalisation, against the string
this run emits — and the paper's fenced blocks are compared as a **multiset**
against the single block this run licenses, so neither a stale verdict nor a
forged twin beside the clean one can be delivered:

```
SMU-DYNAMICS-RELATIVE-SPREAD-153/380-OVER-THE-11-GAUGE-COVARIANT-DERIVING-INSTANCES-<CENSUS=6-FAMILIES-18-INSTANCES-ALL-RUN-12-DERIVE-6-REDUCIBLE|CRITERION=A-COVARIANT-CHAIN-DERIVES-IFF-IT-HAS-EXACTLY-ONE-CLOSED-COMMUNICATING-CLASS|THE-INHERITED-FORM-IS-SUFFICIENT-NOT-NECESSARY-WITNESS-AT-3-STATES-2-CLASSES-1-CLOSED -- (a)CHART-WALK=THE-ANCHORED-CHART-ACTS-TRIVIALLY-32-OF-32-ELEMENTS-INDUCE-THE-IDENTITY-SO-640-CLOSED-CLASSES-AND-THE-WHOLE-639-SIMPLEX-IS-STATIONARY;THE-EXTENSION-DOES-NOT-ACT-ON-THIS-CARRIER-AT-ALL-64-OF-128-ELEMENTS-CARRY-A-UNIFORM-CONFIGURATION-OFF-IT-AND-ITS-CLOSURE-IS-1248-STATES-WITH-336-CLOSED-CLASSES -- (b)GAUGE-WALK=REDUCIBLE-AT-BOTH-READINGS-208-AND-120-CLOSED-CLASSES-IDENTICAL-AS-SETS-TO-THE-PARENTS-ORBITS-AND-ITS-STATIONARY-SIMPLEX-IS-THE-PARENTS-INVARIANT-SIMPLEX-DIMENSION-207-AND-119 -- (c)LAW-NATIVE-RESAMPLING=IRREDUCIBLE-AND-DERIVES-AT-ALL-6-MEMBERS-OF-ITS-DECLARED-FIBRE;THE-MEASURE-IS-NEW-SECTOR-GRADED-AT-15/38-5/19-13/38-AND-INVARIANT-SO-IT-IS-A-POINT-OF-THE-PARENTS-SIMPLEX;BUT-ITS-KERNEL-IS-RANK-ONE-EVERY-ROW-OF-THE-LAW-IS-THE-SAME-VECTOR-AT-6-OF-6-INSTANCES-SO-THE-DERIVED-MEASURE-IS-THE-DECLARED-DRAW-LAW-READ-BACK-AND-THE-ROW-IS-STAMPED-LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION -- (d)COMPOSITION-WALK=IRREDUCIBLE-ON-BOTH-SIDES-AND-DERIVES-THE-COUNTING-MEASURE-BECAUSE-THE-FAMILY-IS-CLOSED-UNDER-INVERSE-640-OF-640-SO-THE-WALK-IS-DOUBLY-STOCHASTIC-WITH-278528-OF-409600-PRODUCTS-STAYING -- (e)MONOMIAL-HAAR-WALK=REDUCIBLE-5-CLOSED-CLASSES-OF-128-AND-ONE-OF-THEM-IS-EXACTLY-THE-PARENTS-HAAR-CARRIER-SO-THE-CORPUS-ONE-HANDED-OVER-MEASURE-IS-ONE-EXTREME-POINT-HERE -- (f)COVARIANT-METROPOLIS=EVERY-DECLARED-INVARIANT-TARGET-IS-REACHED-EXACTLY-3-OF-3-AND-THE-NON-INVARIANT-CONTROL-LANDS-OUTSIDE-THE-SIMPLEX-ORBIT-CONSTANT=FALSE;EXHAUSTIVE-ARM-55-TARGETS-0-FAILURES -- MEASURES=10-DISTINCT-STATIONARY-VECTORS-OVER-12-DERIVING-INSTANCES|NAMED-NULLS-REACHED=COUNTING,ORBIT-UNIFORM-CHART-128,ORBIT-UNIFORM-CHART-32|NEW=7 -- RELATIVITY=THE-MEASURE-MOVES|WIDEST-SPREAD-OVER-THE-11-GAUGE-COVARIANT-DERIVING-INSTANCES=153/380-ATTAINED-ON-1-OF-4-SETS(DEFECT-CARRYING)|OVER-ALL-12-DERIVING-INSTANCES-THE-DECLARED-NON-COVARIANT-CONTROL-INCLUDED=1701/3800|AT-THE-PARENTS-OWN-THREE-MEASURES-ALL-3-OF-3-PRESENT-HERE-THIS-CENSUS-REPRODUCES-27/130-EXACTLY|THE-RISE-TO-153/380-IS-THE-6-NEW-LAW-NATIVE-MEASURES-ENTERING-THE-SAME-COMPARISON-NOT-A-DYNAMICS-EFFECT|OVER-THE-WHOLE-COVARIANT-FIBRE-THE-RANGE-OF-EVERY-HEADLINE-SET-IS-[0,1]-BY-THE-SURJECTION|QUASI-DERIVATION-ARM-REACHABLE-AND-MEASURED-TO-FAIL -- ENUMERATION=THE-CONTROLS-TARGET-IS-DECLARED-ON-CONTIGUOUS-BLOCKS-OF-THE-COIN-INDEX-SO-ITS-TWO-NUMBERS-ARE-ENUMERATION-RELATIVE:UNDER-A-SECOND-ADMISSIBLE-READING-OF-THE-PARENTS-ALPHABET-THE-CONTROL-EXPECTATION-IS-127/100-NOT-263/200-AND-THE-SPREAD-OVER-ALL-DERIVING-INSTANCES-IS-234/475-NOT-1701/3800|THE-LIKE-FOR-LIKE-HEADLINE-153/380-IS-IDENTICAL-UNDER-BOTH-ENUMERATIONS-BECAUSE-THE-COVARIANT-MEASURES-ARE-FUNCTIONS-OF-SECTOR-AND-ORBIT-MEMBERSHIP-ALONE -- PRICE=CONSERVED-NOT-PAID:THE-COVARIANT-DYNAMICS-FIBRE-SURJECTS-ONTO-THE-CLOSED-INVARIANT-SIMPLEX-BOUNDARY-INCLUDED-38-OF-38-BOUNDARY-TARGETS-AT-THE-DECLARED-SMALL-CARRIERS-AND-3-OF-3-AT-THE-ARENA-SO-A-DECLARATION-STILL-SUPPLIES-207-INDEPENDENT-NUMBERS-AT-THE-ANCHORED-READING-AND-119-AT-THE-EXTENSION-READING-MEASURED-HERE-UNDER-THE-ORDER-8-GROUP-EXACTLY-THE-PARENTS-COUNTS|DROPPED-COVARIANCE-THE-SAME-MOVE-COSTS-639|WHAT-MOVED-IS-WHERE-THE-DECLARATION-IS-MADE-NOT-HOW-MUCH-IT-COSTS -- WILSON=LICENSED-BY-THE-PIN-AND-STAMPED-CONDITIONAL-ON-THE-DECLARED-DYNAMICS-AT-12-OF-12-ROWS|OBSERVABLE=THE-TRACE-OF-THE-PLAQUETTE-HOLONOMY-ON-ITS-OWN-FOUR-CORNER-BLOCK-PLAQUETTE-INDEPENDENT-AT-16-PLAQUETTES-AND-GAUGE-INVARIANT|VALUES=107/76@NEW,111/76@NEW,13/10@COUNTING,19/13@ORBIT-UNIFORM-CHART-32,205/152@NEW,207/152@NEW,219/152@NEW,225/152@NEW,263/200@NEW,29/20@ORBIT-UNIFORM-CHART-128|RANGE-OVER-THE-INVARIANT-SIMPLEX=[0,4]-BOTH-ENDPOINTS-ATTAINED-AT-EXTREME-POINTS-SO-COVARIANCE-PINS-THE-EXPECTATION-NOWHERE|NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-0-LOOP-FAMILIES-GROWN -- SCOPE=D=2;L=4;FIELD=Q(zeta_8);COINS=640;LINKS=32;PLAQUETTES=16;CARRIER=THE-PARENTS-PRIMARY-CARRIER-THE-640-UNIFORM-CONFIGURATIONS(PLUS-THE-EXTENSIONS-1248-STATE-CLOSURE-WHERE-THE-EXTENSION-IS-DECLARED);FULL-CONFIGURATION-SPACE=640^32-NOT-A-CARRIER-HERE;ELIMINATION-CAP=208-EVERY-EXACT-SOLVE-AT-OR-BELOW-IT;LOCALITY-IS-DEGENERATE-ON-THIS-CARRIER-ONE-COIN-SERVES-ALL-32-LINKS;THE-DYNAMICS-ARE-DECLARED-NOT-DERIVED;NO-ACTION;NO-COUPLING;NOT-QCD;NO-CONFINEMENT-CLAIM>
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

This unit declares the dynamics. 6 families and 18 declared instances, every
one of them run; that is the whole census and not a sample of it along every
axis with a finite fibre, because each of those is swept to the bottom — and
the two axes whose fibre is the invariant simplex itself are **sampled**, at
three points and at one, with a theorem standing in for the sweep and the
substitution disclosed rather than absorbed. 12 of them derive and 6 are
reducible. And the question the pin exists for is then asked on the objects:
**the stationary measure MOVES across the declared-dynamics fibre.**

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
be exactly the chart-fixed locus of the anchored chart. That identity is
re-established here element-wise rather than by cardinality: the anchored
chart group is measured **transitive on the link set** and measured to reverse
no link, and a configuration fixed by a group transitive on the links and
reversing none of them is constant — so the chart-fixed locus of the full
configuration space is exactly the uniform configurations, one per coin. Two
things follow and both are disclosed rather than discovered by a reader.
First, this is where the parent's simplex lives, so the two units weigh the
same partition and are comparable object for object. Second, **link-locality
is degenerate here**: one coin serves all 32 links, so a "local" resampling
and a global one are the same chain, and no claim about locality is available
at this carrier. The full configuration space is $640^{32}$ and is not a
carrier of this unit; it is named in the scope segment and again in section 12.

**The two measured symmetries.** The residual gauge group on the carrier is
measured by propagation — which constant link twists a site-diagonal gauge
can realise on the torus — and returns the even twists, of order 4 at the
anchored chart reading and of order 8 once the extension's swap conjugation
is admitted. Its orbits are 208 and 120, landing on paper-23's own orbit
counts at named receipt paths. Covariance is tested against **both** groups at
every instance living on this carrier; section 7 reports what that second
column found. The chart group's action is measured separately, and section 4.1
reports what that measurement found.

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
and the closed-class count agreeing at every member: 50968 chains enumerated
exhaustively over the 3-state and 4-state layers, at zero mismatches.

On this census the distinction does not bite — no declared instance has a
transient class at all — which is itself worth recording, because it is the
reason the two readings return the same twelve deriving instances here. The
correction is to the *law*, not to the parent's verdict, and it is registered
against paper-23 as a standing correction annotation in
`v14/note-paper23-correction.md`; paper-23 itself is untouched. It is not a
correction without consequences, either: section 7's price theorem reaches the
*closed* simplex only because the sharp form licenses the boundary arm.

## 4. The declared-dynamics census

Six families. Each is declared in the instrument — its carrier, its transition
law written out, its fibre axis and its declared covariance group — and each
is gated on **its own** objects: row-stochasticity per row, covariance per
generator and per row, communicating classes from its own support, and the
identity $\pi P = \pi$ verified at full size for every vector it publishes.
None is privileged.

| # | family | fibre axis | fibre | irreducible | closed classes | the stationary measure |
|---|---|---|---|---|---|---|
| (a) | the chart-group walk | which chart group | 2 | no | 640 / 336 | the whole simplex / orbit-uniform combinations |
| (b) | the gauge-action walk | which residual reading | 2 | no | 208 / 120 | exactly paper-23's invariant simplex |
| (c) | the law-native resampling | which sector carries which position | 6 | yes | 1 | NEW, sector-graded, and invariant |
| (d) | the composition walk | which side composes | 2 | yes | 1 | the counting measure |
| (e) | the monomial-Haar walk | which side multiplies | 2 | no | 5 | paper-23's Haar, and four classes it does not reach |
| (f) | the covariant Metropolis family | which invariant target | the invariant simplex itself | yes | 1 | the declared target, exactly |

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
the closure is 1248 states, and on it the walk has 336 closed classes. That
the closure really is closed is measured state by state against the four
declared generators of the extension, every image required to be constant on
each direction class and to lie in the set.

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
Those two dimensions are certified by an **exhibited basis** rather than by a
class count already forced equal upstream: every extreme point is solved by
exact elimination, verified against its own chain at full size, and measured
to have a support disjoint from every other, hence independent.

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

**And here is what the dynamics contributes, measured on the object: nothing.**
Every row of the transition law is the same vector at 6 of 6 instances — a
chain that discards its state has a rank-one kernel — so the "derived" measure
is the declared draw law read back, and the exact solve at 640 states recovers
a vector written down before the solve began. Three of its numbers came from a
confirmed law and nobody chose them as a measure, which is real; but the route
that put them onto *this* carrier — the identification of the transport law's
three positions with this arena's three coin sectors — is not pinned, and
paper-23's own census is where that identification was looked for and not
found. The row is therefore stamped
`LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION`: a
**transported law value**, not a measure derived by a dynamics. Section 9
prices it beside the Metropolis family rather than counting it as evidence.

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
declared dynamics built only out of the family's own multiplication. This row
is the census's cleanest: nothing about it was chosen to make it land where it
did.

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

The control's target is declared on four contiguous blocks of the **coin
index**, which is an artifact of this instrument's enumeration and not an
object of the arena. That is disclosed rather than left for a reader to find,
and section 6 prices it.

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
is at or below the size of the parent's simplex — and that is a gate, record
by record, rather than a claim published beside an unchecked constant.

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

Three of those columns reproduce paper-23's published masses exactly — the
composition walk's column *is* the parent's counting measure, and both
orbit-uniform columns are its own nulls — and two of those cells are
additionally checked against named paths in the parent's receipt. That is what
makes the new column comparable at all.

The widest spread over the 11 gauge-covariant deriving instances is 153/380,
attained on DEFECT-CARRYING; over all 12 deriving instances it is 1701/3800,
the declared non-covariant control included.

**What that is not.** It is not a measurement of what declaring a dynamics
does to the parent's sets, and the paper does not read it that way. The
parent's comparison class is a *subset* of this one: all 3 of 3 of the
parent's compared measures are in this census, reached by the composition
walks, by Metropolis at counting and by the two orbit-uniform Metropolis
instances — and restricted to those same three the widest spread is 27/130,
which is exactly the number the parent published. The parent's widest spread
over its own three named nulls was 27/130, and held at a fixed comparison
class this census reproduces it and moves nothing. A maximum over a superset
can only be at least a maximum over the subset, so the *direction* of any
comparison between them is arithmetic; what is real is the size of the
increment, and it is produced by the six new law-native measures entering the
same comparison, not by the dynamics-versus-measure distinction.

**And what the theorem says instead.** Each headline set contains a whole
gauge orbit and its complement contains a whole gauge orbit, so the two orbit
point masses are invariant measures — extreme points of the parent's simplex —
and the set's mass at them is measured to be exactly 1 and exactly 0. The
reachable range of every headline set's mass over the invariant simplex is
therefore the whole unit interval. How far a declaration can move these sets
is: all the way. Any particular spread, this one included, is a fact about the
declared census and not about what declaring buys.

**The enumeration, priced.** The control's target is index-block-declared, so
its two numbers are enumeration-relative and are labelled so. A second
admissible reading of the parents' own alphabet declaration — enumerating it
modulus-major rather than power-major, with the coin family still exhaustive
over its fourth power — returns the same 640 coins as a set in a different
order; the control is rebuilt on it and its chain is measured to have one
closed class and to land on its own target. There the expectation is 127/100
rather than 263/200 and the spread over all deriving instances is 234/475
rather than 1701/3800. The like-for-like headline is unaffected: it is
computed over the covariant instances only, whose measures are functions of
sector and orbit membership alone, and it is measured identical under both
enumerations.

The quasi-derivation arm — the pin's strongest honest outcome — is decided by
comparing the deriving vectors entry by entry rather than inferred from this
table, and it fails.

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

**The boundary is reached too, and that is the sharp criterion of section 3
earning its keep.** A target with a zero is still reached exactly: the
Metropolis chain at it has its zeros as transient states and exactly one
closed class, so by the sharp criterion it derives and the target is its
unique stationary measure. What the boundary costs is irreducibility, not
derivation. Every zero pattern with at least two supported states is
enumerated on the declared small carriers — 38 boundary targets, 38 reached
exactly, 38 with exactly one closed class, 0 irreducible — and the arm is
repeated on the real 640-state carrier with 1, 5 and 100 whole gauge orbits
set to mass zero, where each chain is additionally measured gauge-covariant
and $\pi P = \pi$ is verified at full size: 3 of 3 at the arena. The reach is
onto the **closed** simplex, boundary included.

The covariant-dynamics fibre therefore surjects onto the invariant simplex, so
declaring a covariant irreducible dynamics on this carrier still supplies
exactly 207 independent numbers at the anchored reading and 119 at the
extension — paper-23's own counts, unchanged. The extension half of that
sentence is measured here rather than inherited: covariance is tested against
the order-8 residual group at every instance on this carrier, and the two
populations coincide — 11 covariant deriving instances under the order-4 group
and 11 under the order-8 group — with the Metropolis chain at the
orbit-uniform chart-128 target measured covariant under the order-8 group,
which is what licenses the second number. (A *dynamics* at the extension
reading is a different question again, and lives on the 1248-state closure of
section 4.1, not here.)

**And the price is conserved only under a retained covariance declaration.**
The construction is silent about invariance except through covariance: at any
full-support target, invariant or not, it returns a chain with that target as
its unique stationary measure. The control is that witness — measured full
support, measured to land on its own non-invariant target, measured not
gauge-covariant — so dropping the covariance declaration lets the fibre reach
the whole simplex over this carrier, and the same move costs 639 numbers
instead of 207.

What moved is *where* the declaration is made, not how much it costs. A
programme that hoped to buy the measure by declaring a dynamics has bought the
same object under a different name, at the same price, with one thing added: a
dynamics is more data than the measure it produces, so the move is not free
even where it is not expensive.

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
simplex. That is a gate and not a remark: the endpoints are taken by exact
ordering on the real subfield, each endpoint orbit is measured constant and
measured to have size one, and every published expectation is required to lie
inside the interval. Covariance pins the expectation nowhere. An expectation
on this arena is not a number the arena has; it is a coordinate of the
declaration, and the declaration can put it anywhere the observable goes.

This unit therefore reports expectations as expectations. It grows no loop
family and makes no claim about how any expectation would behave as a loop
grows: 0 loop families are grown, and the pin's inherited must-not — no
area-law, string-tension, or potential claim — is swept over this paper's own
text on the delivery run with the declaring sentences removed first, and every
declaring sentence the sweep may remove is itself required to be located here,
so an exemption carried from a parent and never used cannot sit latent.

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
  counting measure, by the composition walk on both sides. That row is the
  census's one derivation in the full sense: the chain is built from the coin
  family's own product and its closure under inverse, and nothing about the
  measure it returns was put in by hand.
- **A law-valued point of the parent's simplex is supplied for the first
  time**, by the law-native resampling at all six members of its fibre —
  **by transport, not by dynamics**, at the stamp of section 4.3. Both
  orbit-uniform nulls are also reached, but by chains built *from* those
  measures. Neither family is evidence: a chain whose rows are the target, and
  a chain reversible with respect to the target, are the same species, and the
  paper counts both as pricing rather than as evidence.
- **The measure moves**, and the movement is priced on the parent's own sets —
  wider than the parent's own spread over its own three named nulls, narrower
  than the whole unit interval the surjection licenses, and exactly equal to
  the parent's number when the comparison class is held fixed.
- **The price is not reduced by the move**: the covariant-dynamics fibre
  surjects onto the closed invariant simplex, and it does so at the same price
  only because covariance is declared again on the far side.

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
- **The identification behind the law-native family.** Forcing the
  sector-to-position assignment is the shallower question; the deeper one is
  whether the transport law's positions may be identified with this arena's
  sectors at all. Nothing here pins that, and paper-23's own census is where it
  was looked for and not found.
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
no-op, no flag is mutant-only, and no flag changes the delivered bytes:
`--quiet` suppresses the terminal echo alone, because a flag that quietly
published a different transcript would be a byte-reproducibility hazard
wearing a convenience label. The exit conventions invert the usual
reading and are therefore disclosed in the usage string, in the receipt and
here: the delivery run exits 0 on success and 1 on any refusal, writing
nothing; `--selftest` exits 0 when every anchor class is fatal; `--mutant`
exits 0 when the named mutant *dies* on its declared target. A missing pinned
source is a named gate failure rather than an uncaught traceback, so the
convention holds for a bare copy of the file too.

The gate ledger is chained row by row, so that a row edited after its gate
closed no longer matches the digest of its own predecessor. 62 gates close
before the paper gates, 18 of them binding one declared instance each, and 6
paper gates and 2 closing gates follow — the last two being the seal and the
artifact integrity check, which cannot be inside the ledger they close over.
The per-instance gates exist because a census gate that binds only the total
is vacuous at the per-object level (#87). 57 declared mutants, all dead, each
at the gate it was declared to falsify — that sweep is an external-battery
result and the receipt says so rather than implying the delivery run produced
it. The registry is checked TOTAL
against the instrument's own syntax tree, so a falsifier cannot exist as an
unswept branch, none can be declared without a branch to fire, and a switch
the scan cannot read is fatal rather than forgiven. Each mutant's published
description names the exact token it plants and that token is located in the
source text of that mutant's own branch, so a description-inverted mutant
dies here rather than in a reader's trust (E-23); and every falsifier corrupts
an **object** the gate measures rather than the gate's own verdict variable,
so a green badge is evidence that the gate can detect a corrupted object and
not merely that a boolean can be set. The coverage is published at
an honest denominator (#34): of the gates this run closes, 43 are the declared
targets of falsifiers, 16 are the per-instance gates under one registered forcing, and 0 are uncovered — the forcing being machine-checked rather than
asserted, since the per-instance gate's predicate is verified to name no
instance, so the two falsifiers that fire it at two different instances fire
the identical predicate every instance is judged by. The two gates no
falsifier reaches are named with the reason, not counted as covered. 51 anchors in all: 9
file-bytes anchors, 30 path-value anchors and 12 verbatim-text anchors, each
window pinned by its own digest and its own frozen character count against a
declared floor, each located exactly once under whitespace and markdown-prefix
normalisation (#125), each perturbed at a content-bearing token and required
to stop being locatable, and each bound to the gate that consumes it.

The paper gates run in six legs, in the plain delivery run and not in a
separate mode (#20): claim rendering at exact occurrence counts, the complete
verdict string by equality, the must-not vocabulary sweep with the declaring
sentences removed first, claim polarity, the structural binding of tables and
quotations, and numeral coverage over every numeral including the fenced
verdict block, the inline code spans and both sides of every fraction (E-22).
The fenced blocks are compared as a multiset, so a forged twin beside the
clean one dies. Every data row of every delivered table that carries a numeral
must be covered by a claim rendered from the receipt — so a row swap that
leaves both labels in place dies, and a table added later cannot arrive
unbound — and every blockquote must lie inside one of the pinned verbatim
windows, which is what stops the paper from attributing to a parent a sentence
that parent does not contain. Header rows are the declared exception and are
counted and published rather than silently skipped. The provenance digests are
bound as claims rather than licensed as numeral fragments, and the structural
literals the coverage gate is permitted to forgive are now this paper's own
section numbers and nothing else: the engraving references are forgiven only in
their parenthesised form, so a delivered number that happens to equal an
engraving reference is still gated.

Every published object carries the gate-to-disk seal, and the manifest — each
object, the receipt key it was taken at, the gate whose passing took it, the
digest, and any sub-object sealed separately — is published in the receipt.
The manifest is **total**: 47 objects are sealed before the paper gates,
more are sealed by the paper gates themselves,
and every other top-level key is named in the declaration with the reason it
cannot be sealed. The gate ledger is snapshotted before the two
closing gates and the snapshot is what is sealed and written — a seal cannot
be inside the object it seals.

**The choice inventory.** 11 construction choices are inventoried, of which 5
are measured verdict-determining, each with its fibre and its instances. The
lattice and the coin family are FORCED with fibre 1; the elimination cap is
FORCED-BY-COST and set to the parent's orbit count; the carrier is
DECLARED-AND-DISCLOSED at fibre 2, both instances built; five declared
dynamics axes have a finite fibre and are DECLARED-AND-SWEPT, with the number
of instances built equal to the fibre at every one of them, so along those
axes no member of a declared fibre is left unrun; and the two Metropolis
axes — the invariant target and the control target — have the invariant
simplex itself as their fibre, cannot be swept, and are stamped
DECLARED-AND-SAMPLED, each carrying the licence that names the theorem and the
exhaustive arms standing in for the sweep. Every row is evaluated by the
gate; none is skipped by a type test. The verdict-determining flag binds each
row by its own measured predicate where the axis carries two or more
instances — re-running that axis at another instance moves a published
vector — and is stamped NOT-MEASURED where the axis carries one, rather than
reported as a measured false. That is what makes the two axes that are *not*
verdict-determining informative: composing on the left and composing on the
right give the same measure, so that side is a free choice with no
consequence, while multiplying by the monomial group on the left and on the
right does not.

## 11. The successor register

- **ACT inherits the law-native π as the leading candidate, and inherits it
  stamped.** `LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION`,
  sector-graded, invariant, a point of paper-23's simplex — the first point of
  that simplex anything in the corpus has supplied, and supplied by transport,
  not by dynamics. Inside the conserved-price frame it is one declared point
  of a simplex every point of which is reachable by a covariant irreducible
  chain; its privilege over the other coordinates is that three of its numbers
  came from a confirmed law, and its debt is the identification that put them
  here. **ACT must not treat it as a derived measure and must not spend it as
  one.** The honest use is as a *control*: whatever measure an action supplies,
  compare it to the law-native point and report the distance. If they agree,
  that agreement is the first real evidence in this arena; if the action route
  dies, the law-native point is what the programme has, at its stamp. ACT also
  inherits the price frame — the invariant count with covariance retained, the
  whole-simplex count without it — and the warning that no expectation on this
  arena has content until a measure arrives by a route that is not a
  declaration.
- **The cheap falsifier, and it is cheap.** Search for a gauge-invariant
  functional whose range over the invariant simplex is *narrower* than its own
  range. This unit computes one loop observable and reports that covariance
  pins its expectation nowhere; a functional whose range were a point would be
  the first quantity this arena hands over free, and the outcome is decisive
  either way.
- **The full-space dynamics.** Every family declared here has an obvious
  analogue on $640^{32}$, and the interesting question — whether locality
  changes any of these answers — cannot be posed on this carrier at all. The
  first tractable step is the 1248-state closure this unit built, where
  configurations already differ direction to direction, and where the
  extension genuinely acts.
- **The declaration itself, with its pin.** The fibre is now measured to be
  the whole invariant simplex. A unit that wants one measure must argue for
  one point, and section 7 is the exact statement of what that argument owes.
- **The correspondence question, promoted.** Whether a pinned correspondence
  exists from the transport law's carrier to R5's configurations is no longer
  only a measure-source question: it is the gate on whether "law-native
  dynamics" can mean anything in this arena at all. Forcing the
  sector-to-position assignment stays open but is demoted — even fully forced
  it yields a transported measure, not a derived dynamics.
- **The extension's carrier.** That the parent's carrier is not closed under
  the parent's own declared extension deserves a unit of its own: the census
  questions paper-23 answered at the fixed locus can be re-asked at the
  closure, where the simplex is a different object.

## 12. Deviations, and the register of scope

The pin's arena, gates and must-nots are followed as written. Five points are
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

Third, the relativity spread is published three times — over the
gauge-covariant deriving instances, over all of them, and over the parent's own
three measures — because only the last is like-for-like with the parent's
number, and a single figure would have flattered or exaggerated depending on
which was chosen. The head carries the covariant one and states the restricted
one beside it.

Fourth, two published numbers depend on the order in which this instrument
enumerates the coin family, because the declared control's target is built on
contiguous blocks of the coin index. Both are stamped enumeration-relative and
both are re-measured under a second admissible reading of the parents' own
alphabet declaration, so a reader is told what changes and what does not. The
headline is enumeration-free by construction and is measured to be so.

Fifth, the Wilson segment is reported as expectations and nothing else. Every
value is conditional on a declared dynamics and says so in its own row; the
range measurement in section 8 is the honest summary of how much the arena
constrains any of them, which is: not at all.
