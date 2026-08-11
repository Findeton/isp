# R5M — the configuration measure: what the substrate hands over, and what has to be declared

**Status:** `DELIVERED` — built against the frozen pin `v14/note-r5m-pin.md`
(sha256-12 `e5e09f65f83b`, ledger #174), R5's opening obligation. Verified to
run: two plain runs byte-identical, every gate passed, every declared mutant
dead at its declared target, the falsification self-test fatal at every anchor
class and writing nothing. Between delivery and adjudication every headline
below is a **candidate reading**.

## The Substrate Derives a Law on the States, Not a Measure on the Configurations; Over the Configurations the Symmetry Fixes a Support and Leaves a Simplex

**Unit:** R5M, v14, paper #23.
**Instrument:** `v14/code/r5m_measure_exact.py`.
**Artifacts:** `v14/code/r5m_measure_output.txt`,
`v14/code/r5m_measure_receipt.json`.
**Inheritance, hash-verified at run time and by no other route:** the arena —
the 640-coin family, the link-indexed configurations, the chart group, the
gauge action, the plaquette loops — comes from R5, `v14/paper-18-gauge-rung.md`
(`62cfe5689d2c`) with its instrument (`0d98de793b79`) and receipt
(`0c02b7684e5b`), terminal at commit 987cd73; the candidate derivation source
is the Γ-iteration terminal, `v14/paper-16-gamma-iteration.md`
(`5c1df50673d4`) with its receipt (`42255f50328a`), at commit 2895a9a; the
correspondence prior is weld 2, `v14/paper-13-weld2-carrier-census.md`
(`9cdb10472953`) with its receipt (`bd68497d4510`), and the corpus's one found
dictionary at a committed record arena is weld 3, `v14/paper-19-r3-weld.md`
(`50bb81e67942`) with its receipt (`dfea664f2408`). Every object below is
**reimplemented** from those definitions; nothing is imported from any other
unit's program.
**Anchors are (path, value) pairs and (context, consumer) pairs, not only file
bytes:** 10 file-bytes anchors, 33 path-value anchors and 12 verbatim-text
anchors, 55 anchors in all — each verbatim window pinned by the digest of its
exact bytes, by its own frozen character count and by a declared length floor,
each located exactly once, each perturbed at a content-bearing token and
required to stop being locatable, and each bound to the gate that consumes it.
**Exact arithmetic only:** the field is $\mathbb{Q}(\zeta_8)$ carried as
integer 5-tuples over the basis $(1,z,z^2,z^3)$ reduced modulo $z^4+1$ in
lowest terms, so tuple equality is field equality; every probability is an
exact rational, and the one linear-algebra measurement in the unit — the
dimension of a kernel — is exact elimination over `Fraction` and not a rank
estimate. An AST scan of the instrument's own syntax tree is a gate: no float
literal, no banned import, no banned attribute call, and no moving reference
anywhere, so the run is correct off-tree and in a directory with no version
control at all (#91).
**The seal (#119), native from birth and total:** every published object is
digested at the moment its gate passes; every top-level key of the receipt is
either sealed that way or named in the declaration with the reason it cannot
be; the artifacts are written from the sealed payload through temporaries
moved into place only after the bytes on disk match the gate-time digests, and
a deliberately corrupted payload is written to a probe path and required to be
detected first.

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field; the complete string — head
included — is compared for equality against an *independent reconstruction*
that derives the head **by a second head law of its own**, written from the
same pre-registered outcomes with a different branch structure and sharing no
format string and no helper with the builder's, and that re-renders **every
segment** from the primitive measured tables, reading neither the builder's
segments nor the builder's counts; and the block below is compared, character
for character under whitespace normalisation, against the string this run
emits — and the paper's fenced blocks are compared as a **multiset** against
the single block this run licenses, so neither a stale verdict nor a forged
twin beside the clean one can be delivered:

```
MEASURE-DECLARATION-REQUIRED-<ONE-POINT-OF-THE-INVARIANT-119-SIMPLEX-ON-120-ORBITS-AT-THE-CHART-128-READING;207-SIMPLEX-ON-208-ORBITS-AT-THE-CHART-32-READING -- CENSUS=9-CANDIDATES-0-DERIVE|CLOSURE=A-CANONICAL-MEASURE-EXISTS-EXACTLY-WHERE-SOMETHING-ACTS-TRANSITIVELY-ON-THE-CARRIER-9-OF-9-ROWS-ARE-INSTANCES-AND-A-10TH-CANDIDATE-IS-DECIDED-BY-THE-SAME-TEST|MEASURE-BLOCKED-AT=FORCED-SHUT-CENSUS-RELATIVELY-ONLY-1-NAMED-ABSENT-ROW(THE-STATIONARY-MEASURE-OF-A-DYNAMICS-ON-THE-CONFIGURATIONS)=NOT-CENSUSABLE-NO-PINNED-DYNAMICS-ON-CONFIGURATIONS;A-COVARIANT-CHAIN-DERIVES-IFF-IT-IS-IRREDUCIBLE -- (a)PUSHFORWARD=NO-PINNED-CORRESPONDENCE-TO-THIS-ARENA(WELD2-120-ROWS-60-DISTINCT-CANDIDATES-0-FOUND-AT-THIS-CARRIER;WELD3-IS-THE-ONE-FOUND-DICTIONARY-AT-A-COMMITTED-RECORD-ARENA-AND-ITS-TARGET-CARRIES-9-SITES-AGAINST-16-WITH-A-CONSTANT-LINK-DATUM-AT-27-OF-27-CELLS;ALL-8-FOUND-ROWS-IN-THE-CORPUS-WELD2s-TWO-DECLARED-PROBE-CONTROLS-INCLUDED-DIE-AT-THE-SAME-SITE-COUNT-BLADE;GRANTED-EVERYTHING-THE-RESIDUAL-IS-A-POINT-MASS-WITH-THE-COIN-FREE-AMONG-640)|(b)COUNTING=DECLARED-NULL-2-CARRIERS-x-2-NULLS-ALL-INVARIANT|(c)INVARIANCE=SELECTS-A-SUPPORT-NOT-A-MEASURE|(d)FINITE-GROUP-HAAR=THE-FAMILY-IS-NOT-CLOSED-278528-OF-409600-PRODUCTS-STAY|(e)U(2)-HAAR=A-FINITE-SUBSET-HAS-MEASURE-ZERO-AND-384-OF-640-COINS-HAVE-FINITE-ORDER-IN-FAMILY|(f)GIBBS=NO-ACTION-NO-COUPLING-BY-THE-PARENTS-OWN-DECLARATION|(g)BORN=DERIVES-A-LAW-ON-THE-STATES-EXACTLY-NOT-A-MEASURE-3-KERNELS-FOR-640-CONFIGURATIONS-STATIONARY-SIMPLEX-DIM-15-IN-THE-DIAGONAL-SECTOR-AND-14-IN-THE-OTHER-TWO|(h)HOLONOMY-PULLBACK=NO-SINGLE-GROUP-512-CONFIGURATIONS-CARRY-AN-INFINITE-ONE|(i)MAXENT=RELOCATES-THE-PRICE-IT-RETURNS-ITS-DECLARED-REFERENCE-AND-THE-ARENA-PINS-NO-CONSTRAINT-TO-CONDITION-ON -- UNIQUENESS=GATED-AND-FAILS-AT-BOTH-READINGS(CHART-128:120-ORBITS;CHART-32:208-ORBITS)|INVARIANT-MEASURES-ARE-EXACTLY-THE-ORBIT-CONSTANT-ONES-SO-UNIQUE-IFF-TRANSITIVE|THE-GATE-CAN-PASS-A-SYNTHETIC-TRANSITIVE-ARENA-RETURNS-1-ORBIT|THE-DERIVE-ARM-IS-REACHABLE-AND-IS-RUN:THE-CONTROL-ARM-ON-A-SYNTHETIC-TRANSITIVE-CARRIER-IS-PRICED-AT-0-FREE-ITEMS-BY-THE-SAME-FUNCTION-AND-EMITS-MEASURE-DERIVED-<AN-INVARIANCE-CHARACTERISED-MEASURE;UNIQUE>|FULL-SPACE-NOT-TRANSITIVE-BY-AN-EXHIBITED-INVARIANT-561-SECTOR-MULTISETS-OVER-32-LINKS -- WHAT-THE-SYMMETRY-DOES-FIX=A-SUPPORT:THE-CHART-FIXED-CONFIGURATIONS-ARE-EXACTLY-THE-640-UNIFORM-ONES-AT-655360-OF-655360-CHECKS-SO-THE-PARENTS-DECLARED-SWEEP-IS-THE-FIXED-LOCUS-ITSELF(32-AT-THE-EXTENSION-WHERE-REVERSAL-FORCES-U=XUX)|AND-IT-IS-CARRIED-BY-THE-DIRECTION-RELABELLING:UNDER-THE-TRANSLATIONS-ALONE-THE-LINKS-FALL-INTO-2-ORBITS-AND-THE-FIXED-LOCUS-IS-409600-CONFIGURATIONS-OF-WHICH-THE-PARENTS-640-IS-A-PROPER-SUBSET|FULL-SPACE-CHART-ORBITS=19615942923083377386986841947523957550319860937261713352753238485891465108835574743040000-AND-4903985730770844346746710486880993541417452474995871943159704028721854423865774571520000-AT-THE-TWO-READINGS -- CONSEQUENCE=THE-DECLARATION-IS-NOT-INNOCUOUS:THE-PARENTS-OWN-HEADLINE-SETS-MOVE-BETWEEN-INVARIANT-MEASURES|NON-COMMUTING=9/10-AT-COUNTING-AND-9/13-AND-7/10-AT-THE-TWO-ORBIT-NULLS|DEFECT-CARRYING=3/5-AND-6/13-AND-7/15|WIDEST-DISAGREEMENT=27/130-ATTAINED-ON-2-OF-4-SETS(DIAGONAL,NON-COMMUTING)-NONE-DECLARED-THE-ARG-MAX-SET-IS-PUBLISHED -- THE-ONE-CANONICAL-MEASURE-THIS-ARENA-HANDS-OVER=HAAR-ON-THE-128-ELEMENT-MONOMIAL-SUBGROUP(CLOSED-0-FAILURES-INVERSES-0-FAILURES;MAXIMAL-0-OF-512-INTERFERING-COINS-ADJOINABLE)-AND-IT-CARRIES-0-OF-384-DEFECT-COINS:WHERE-THE-MEASURE-IS-FREE-THE-QUANTUM-LAYER-IS-ABSENT -- WILSON=SEGMENT-WITHHELD-BY-THE-PIN-NO-SOURCE-DERIVES|NO-EXPECTATION-COMPUTED-ANYWHERE-IN-THE-INSTRUMENT|NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM -- SCOPE=D=2;L=4;FIELD=Q(ZETA-8);COINS=640;LINKS=32;PLAQUETTES=16;CONFIGURATION-SPACE=640^32;PRIMARY-CARRIER=THE-UNIFORM-SLICE-WHICH-IS-THE-CHART-FIXED-LOCUS;FULL-SPACE-ORBIT-COUNT-UNDER-THE-JOINT-GROUP=NOT-COMPUTED-BY-COST-A-LOWER-BOUND-IS-EXHIBITED-INSTEAD;THE-CORRESPONDENCE-QUESTION-AT-THIS-TARGET=OPEN-OVER-THE-EVEN-L-FAMILY-ONLY-WELD-2s-STRUCTURAL-BLADE-IS-SILENT-HERE-BECAUSE-THIS-LATTICE-IS-BIPARTITE-WHICH-AT-(Z-L)^2-HOLDS-EXACTLY-WHEN-L-IS-EVEN-SO-AT-ANY-ODD-L-THE-INHERITED-BLADE-FIRES;NO-MEASURE-DERIVED;NO-ACTION;NO-COUPLING;NO-DYNAMICS;NOT-QCD;NO-CONFINEMENT-CLAIM>
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and what could have answered the other way

R5's successor register named this unit's obligation first and said why:

> A confinement analog would need three objects this arena does not have: a
> measure on configurations, a family of loops whose size can grow, and a
> coupling to vary.

and its closing section named the gap in one sentence:

> The gap a coupling unit inherits above all is the one this rung could not
> close: **there is no measure on configurations here**, so there is
> nothing yet to take an expectation over.

So the question is **derive or declare**, at the RSQ standard, where *derived*
means zero free items and nothing weaker. This unit runs 9 candidate sources —
the three the pin names and six more it does not, because a census that
measures only the candidates it was handed cannot report that none survives —
and 0 derive. Every one of those prices is the length of a list this run
measures, and not a constant its author typed.

**What could have answered the other way.** Three outcomes were pre-registered
in the pin. Two of them are reachable on the measurements this instrument
takes, and the reachability is **run rather than advertised**:

| pre-registered outcome | reachable how | measured |
|---|---|---|
| `MEASURE-DERIVED` via invariance | the invariance candidate's price is zero exactly at a transitive reading, by the pricing function itself | the control arm of §5: on a synthetic transitive carrier the control arm is priced at 0 free items and emits `MEASURE-DERIVED-<AN-INVARIANCE-CHARACTERISED-MEASURE;UNIQUE>` |
| `MEASURE-DERIVED` via pushforward | a pinned correspondence would have carried the transport law's exact probabilities across | the corpus's found dictionaries are enumerated and every one lands elsewhere |
| `MEASURE-BLOCKED-AT` | an object that cannot be evaluated at all | **forced shut census-relatively**: of the 9 rows that can be evaluated, none is blocked at an object — but the census also carries 1 named-absent row that cannot be evaluated because the object it needs does not exist, and that row is named rather than omitted (§4.10) |

The falsifiability of this unit therefore lives in the orbit census and in the
correspondence census. Both could have gone the other way. The head is computed
from those counts and cannot be typed: a mutant that declares a candidate to
derive without the transitive structure that would make it derive dies at the
census criterion, a mutant that unwires the invariance price from the
uniqueness measurement dies at the control arm, and a mutant that makes the
head law constant dies at the reachability gate.

## 2. The arena, declared as data (§15)

The stage is R5's, rebuilt here rather than quoted. The lattice is
$(\mathbb{Z}_L)^2$ at the anchored size $L = 4$ and the anchored dimension
$d = 2$: 16 sites, and the link and plaquette sets are derived from the lattice
rather than declared, giving 32 links and 16 plaquettes. The coefficient
alphabet is rebuilt from its declared shape and returns 25 elements; the coin
family is enumerated exhaustively over the admissible rows and returns
640 coins, splitting into 64 diagonal, 64 antidiagonal and 512 balanced with
nothing left over, every one of them confirmed unitary by a second route.

**A configuration is a coin per link.** The configuration space is therefore
$640^{32}$, and the parent swept the **uniform** configurations exhaustively —
one coin repeated on every link — and no others. Section 3 shows that this
window is not the arbitrary restriction it looks like, and says exactly which
declaration carries that result.

**The two measured symmetries.** The chart group is the lattice translations
with the direction relabelling, of order 32, together with this arena's
declared extension by the square point group, of order 128. The gauge action is
site-diagonal, acting on a link's coin by conjugation; its effect depends on
the phase **difference** across the link alone, and every one of its eight
values is measured to permute the derived family, so a gauge transformation
moves a configuration inside the configuration space and never out of it. The
family-covariance identity R5 measured is **forced** — R5 proved it holds at
128 of 128 off-chart probes — so it selects nothing and cannot characterise
anything; this unit does not use it, and the pin says so in as many words.

**Two objects, not one.** The distinction this whole paper turns on is stated
here so that no later section can blur it. A symmetry acting on a space fixes a
**set of configurations** — its fixed locus. It also constrains the
**measures** on that space — the invariant ones. These are different objects
and they answer different questions, and conflating them is the error this unit
exists to prevent. Section 3 measures the first. Sections 4 and 5 measure the
second.

## 3. What the measured symmetry does fix: a support, not a measure

The chart group is measured to be **transitive on the link set** at both
readings — the 32 links form one orbit — and at the anchored reading no chart
element reverses a link. A configuration fixed by the whole chart group must
therefore assign the same coin to every link, and conversely every uniform
configuration is fixed. Run configuration by configuration rather than read off
the orbit formula, at 655360 of 655360 checks with no failures, the chart-fixed
configurations are **exactly the 640 uniform configurations**.

The two halves of that sentence are carried by different measurements and the
unit attributes them separately. The 655360 checks establish the forward
direction — every uniform configuration *is* fixed. The converse — that no
other configuration is — is carried by transitivity on the link set together
with the fact that no anchored chart element reverses a link; both are gated,
the second inside the fixed-locus gate itself, and a planted reversal
falsifies it.

**So R5's declared window is the chart-fixed locus of the declared chart.** The
parent disclosed its uniform sweep as a restriction with a precedent; it is
more than that. It is the set of configurations at which the arena's own chart
symmetry is unbroken, and that is a derivation, not a declaration. This is the
one positive result in this unit's census, and it is worth being exact about
what it is: it fixes **where** a measure would live, and says nothing whatever
about **which** measure lives there.

**And it is the direction relabelling that carries it**, which this unit
measures rather than leaves for a reader to find. R5 declared two charts;
nothing makes two exhaustive. Drop the direction relabelling and keep the 16
translations alone — a third admissible declaration — and the link set falls
into 2 orbits rather than one, no element reverses a link, and the chart-fixed
locus is the 409600 two-coin configurations, one coin per direction, of which
R5's swept 640 is a proper subset. The positive result is therefore
chart-declaration-relative, and the inventory of §10 carries the axis with
three measured instances rather than two.

Under the declared extension by the point group the answer moves too, and the
movement is instructive. A reversed link carries the swap conjugate of its
coin, and 96 of the 128 extension elements reverse at least one link — but a
reversal is not by itself an obstruction, because an element may reverse many
links and still compose to the identity around every cycle. What forces a
fixed configuration's coin to satisfy $U = XUX$ is an **odd-parity cycle**,
and 12 of the 128 elements carry one. Those two counts are kept apart in the
receipt on purpose; conflating them would misreport the fixed locus. Only
32 of them survive the condition — the coins commuting with the swap.

For the full configuration space the same computation is available exactly. The
chart-orbit count of $640^{32}$ is computed by Burnside, the fixed-point count
factorising over each element's cycles on the link set with the parity of the
swap conjugations around each cycle, and the group order divides the
fixed-point total exactly — which is the arithmetic check the formula has to
pass. Both readings are published in the verdict as exact integers.

## 4. The derivation census

9 candidate sources, each measured, each priced in free items, and 0 derive.
One further candidate is **named absent** because it cannot be priced at all.

**The census is a test, not a list.** It has an organizing principle, and every
row is an instance of it:

> A canonical — equivariant, zero-free-item — probability measure on a finite
> carrier exists exactly where some declared structure acts **transitively** on
> that carrier.

Each row below names the transitive structure it would need; whether that
structure acts transitively is measured from this run's own quantities; and a
gate requires the two columns to agree at every row — a row derives if and only
if its structure is transitive. That is what makes "none of these derives" an
argument a tenth candidate can be run through rather than an inventory a reader
has to trust.

| # | source | the transitive structure it would need | acts transitively | free items |
|---|---|---|---|---|
| (a) | the history-measure pushforward | transitivity borrowed through a pinned correspondence | no | 2 |
| (b) | the counting measure | transitivity by fiat, which is the free choice itself | no | 2 |
| (c) | an invariance-characterised measure | the measured symmetry group, acting transitively | no | 1 |
| (d) | Haar from a group structure on the family | a group acting on itself | no | 1 |
| (e) | Haar inherited from $U(2)$ | the carrier as an orbit of the ambient group | no | 1 |
| (f) | Gibbs from an action | an action, which exists to break transitivity | no | 2 |
| (g) | the Born layer | its own kernel, irreducible on the carrier | no | 1 |
| (h) | pull-back from the holonomy group | one holonomy group, plus a section | no | 1 |
| (i) | maximum entropy | a canonical reference measure | no | 2 |
| (j) | the stationary measure of a dynamics on the configurations | an irreducible chain on the carrier | no | NOT-CENSUSABLE |

### 4.1 (a) The history-measure pushforward

The pin names the transition layer's own stochasticity as the candidate source,
and it is a real one: Γ's law is an exact probability. Quoted from its own
pinned bytes,

> Γ is an exact rational column-stochastic family between the five depth cuts,
> of dimensions [1, 5, 17, 49, 113] over 3969 histories and 185 classes

with cut mass 1 at every one of its 5 cuts and the disintegration identity
exact at 3968 of 3968 transitions. Nothing below is a complaint about the
source. **The candidate fails at the correspondence.**

**The vocabulary is a coincidence and is refused.** The two arenas appear to
share words. They do not share referents, and the instrument separates the two
by counting whole words and substrings apart. A configuration word appears
inside *coincidental*; a lattice word appears inside *refinement lattice*; a
link word appears inside a verdict segment denying a link between recurrence
and non-Markovianity; a site word appears inside *revisited*. Those are
substring hits and the census reports them as such.

**The one structural near-miss is measured and it obstructs.** Both arenas do
carry an object called a holonomy, and they are not the same object. The
transport layer's is **abelian**, of measured rank 2 on the primes $\{2,3\}$;
this arena's is non-abelian, and at 3 of the 6 declared local stencils its
class is a **perfect** group — $A_5$, $A_7$, $A_8$. A correspondence required
to transport the connection would need a homomorphism from the first onto the
second; an abelian source has abelian image, and a non-trivial perfect group is
not abelian. So the transport is impossible at exactly those stencils, and
possible at the 3 whose class is abelian, which is why the obstruction is
reported per stencil and never as a universal.

**The pinned correspondences are enumerated, and the enumeration is the
finding.** The corpus has already run this question. Weld 2 asked

> is there a **motivated** map from the transport grammar's carrier to I7's
> spatial record lattice — grammar objects to sites, object-pairs or channels
> to links, sets of division events to link counts — where *motivated* means
> zero free items at the RSQ standard?

at both of the transport layer's own quotients — the very carriers this pin
names as the source — and answered

> The census is **EMPTY under both**: **120 rows, 60 distinct candidates,
> 0 FOUND, 0 SMUGGLED**.

with 0 FOUND across 120 rows, 60 distinct candidates. And the corpus's one
*found* dictionary — one, at a committed record arena — is weld 3's

> The site and link generators are the one cell weld 2 left live at a record
> arena — site ← ACTOR, link ← the co-division actor pair, count ← the division
> events on that pair inside the declared window.

which carries this pin's candidate source **on its own pre-registered dead
list**, naming weld 2's scissors scope and its transport-carrier cells
explicitly.

**And the enumeration is total, which is what makes it a finding.** The
instrument walks every row of both pinned weld receipts whose fate begins
`FOUND`: weld 3's six, and weld 2's own two positive controls, which the
delivered census had not named — `FOUND_at_crystal` at the arena
`CRYSTAL/DOUBLE-GRID(3,2)`, and `FOUND_at_I7_target_declared_probe` at
`DECLARED-PROBE/CAYLEY-AT-I7`. Both carry zero free items at the RSQ standard,
both are built from the same generators a pushforward would need, and both are
therefore exactly the rows nearest this unit's claim. There are
8 FOUND rows across the two pinned receipts, and every one of them dies at the
same blade: each lands on a target carrying 9 sites where this arena carries
16 sites, so none can be read here without being rebuilt — and a rebuilt
dictionary is a declaration, not an inheritance. So the pushforward has no
pinned correspondence by measurement and not by omission.

**Granted everything, the residual is a point mass.** Suppose the dictionary
were granted anyway. Its **link datum is a count, and the count is constant**:

> the same nine site objects, the same 27 unordered realised pairs, the same
> count 1 on every one of them

A constant link datum pulls back to a single configuration whichever coin one
sends it to. The most generous grant available therefore delivers a **point
mass**, with the coin free among 640 — a declaration of one member of the
family, and the least informative measure the arena admits.

**And the arithmetic of the source is measured too**, because a pushforward can
charge no more atoms than its source has. The transport law's finest cut
carries 113 classes against 640 configurations even on the uniform slice, so
any class-grain pushforward leaves at least 527 of them at mass zero, and on
the full space it charges a vanishing fraction of $640^{32}$.

**The blade that does not transfer, disclosed — and scoped.** Weld 2's
structural kill was that a graded class graph is bipartite and cannot carry its
target's odd cycle. **This target is bipartite too** — the link graph is
4-regular and every cycle is even — so that blade is **silent here**, and this
unit does not inherit it. But the silence is a property of the declared **even**
lattice size and not of the target species: measured over $L = 3$ to $8$, the
torus is bipartite at 4, 6, 8 and not at 3, 5, 7, so at any odd $L$ the target
carries odd cycles, the inherited blade fires, and the correspondence question
there is closed by inheritance. Whether some *new* correspondence could be
built to this target is therefore **open over the even-$L$ family** — which
includes R5's own refinement and every scaling step this programme would take
— and is named as such in section 11 rather than claimed closed. What this
unit measures is that none exists now, and that even the best one that does
exist elsewhere would leave the coin free.

### 4.2 (b) The counting measure — the declared null, fibre printed

The counting measure carries no information, which is the point of a null. What
this unit adds is that it is not even a *unique* null. Two carriers are
declared — the uniform slice and the full space — and on the slice two natural
counting measures are declared: counting on **configurations**, and counting on
**orbits**. Both are invariant under everything this arena measures. They are
different measures. Section 6 prices what that costs.

### 4.3 (c) An invariance-characterised measure

A measure is invariant under a group acting on a finite set if and only if it
is constant on the orbits. So invariance fixes a measure uniquely **if and only
if** the group is transitive, and the whole question is an orbit count.

Which group acts on the slice is itself measured rather than assumed. A gauge
transformation carries the uniform slice **as a whole** into itself only if its
twist is constant on every link — on the diagonal sector the twist acts
trivially and a weaker condition would suffice there, but a group acting on the
slice must move every member of it — and the propagation of the site phase
around the torus closes exactly at the even twists, measured by propagation and
not argued. The group whose orbits are counted below is therefore the
**residual** group on the slice, not the chart group, which acts on the slice
trivially: of order 4 at the anchored chart reading, generated by the squared
twist, and of order 8 once the extension's swap conjugation is admitted. Its
orbits are 64 of size 1 and 144 of size 4 at the anchored reading, and 8 of
size 1, 28 of size 2, 24 of size 4 and 60 of size 8 at the extension.

| reading | orbits on the slice | independent numbers a declaration must supply |
|---|---|---|
| CHART-128 | 120 | 119 |
| CHART-32 | 208 | 207 |

Neither orbit count is 1. **The group does not act transitively at either
reading**, so no measure on the configurations derives from invariance:
invariance selects a support, not a measure, and the admissible set is a
simplex of measured dimension rather than a point. This
row's price is therefore 1 — and it is the one price in the census that this
instrument's own measurements could have set to zero.

On the full space the same conclusion is reached without an orbit enumeration,
by exhibiting an invariant: the gauge preserves each link's sector and the
chart permutes the links, so the **multiset of sectors over the links** is
invariant, and it takes 561 sector multisets, every one of them realised. The
orbit count there is at least that many.

### 4.4 (d) Haar from a group structure on the family

A finite group carries a canonical measure — its Haar measure, the uniform one
— so if the coin family were a group the question would be over. It is not:
278528 of 409600 products stay inside the family. The containment that fact
rests on runs one way only, and both directions are measured: every product
that leaves has **both** factors interfering, and no other pair leaves at all,
but only 131072 of the 262144 ordered interfering pairs leave — exactly half.
"The ones that leave are the interfering ones" is a containment, not a
characterisation, and the unit states it as one.

But one part of it **is** a group, and this is the sharpest thing the unit
found. The 128 monomial coins are closed under multiplication and under
inverse — 0 failures of each — and no interfering coin can be adjoined to them
without the closure leaving the family, at 0 of 512 interfering coins. So there
is exactly one place in this arena where a measure is handed over rather than
declared.

**And it is exactly the place where the quantum layer is absent.** The parent
measured 384 coins carrying a composition defect, every one of them
interfering. The Haar carrier contains 0 of the 384 defect-carrying coins. Where
the substrate gives a measure for free, the defect is not; where the defect
lives, the measure has to be declared. That is not a consolation prize, and
this unit enters it as the census's most transferable finding.

### 4.5 (e) Haar inherited from $U(2)$

The ambient group has a Haar measure, and it cannot descend: the family is a
**finite** subset of a positive-dimensional Lie group, so it carries Haar
measure zero and conditioning on it is undefined. A finite *subgroup* would
inherit the ambient invariant measure as its own Haar — that is candidate (d),
and it is exactly why this row's price is keyed to the same measurement — but
the family is not one, and it is not even closed under taking powers:
384 of 640 coins generate a finite cyclic group inside it, and the rest leave,
which is measured here rather than argued.

### 4.6 (f) Gibbs from an action

A weight of the form $e^{-S}$ needs an action functional and a coupling, and
the parent's declaration is quoted from its own pinned bytes:

> It has no configuration measure, no action functional, no coupling and no
> dynamics for the link variables

Both objects this route needs are read off that window rather than typed, which
is where this row's price of 2 comes from. Declaring either is declaring the
measure by another name, at a strictly higher price: an action is a function on
the configurations, which is more data than the measure it produces.

### 4.7 (g) The Born layer — the candidate that derives, and what it derives

The substrate does hand over something exact, and it does so everywhere.
$B(U) = \lvert U\rvert^{\circ 2}$ is doubly stochastic at every one of the
640 configurations, in exact rational arithmetic. This candidate is real and is
not dismissed on a technicality. Naming the object exactly is what decides it.

$B(U)$ is a **kernel**, not a distribution: each of its *rows* is an exact
probability distribution over the carrier's 16 states, at every one of the
640 configurations — a doubly stochastic kernel on the two states of a link's
own domino, padded by the identity everywhere else. And it lands on the wrong
space twice over. Its fibre over the configuration space is enormous: the whole
family collapses to 3 distinct Born kernels, one per sector, with fibres 64, 64
and 512, so the Born layer cannot separate two configurations of the same
sector, let alone weigh them.

Pressed for a **measure** it fixes none either, which is the measurement this
section adds. The kernel is the identity off the link's own domino at every
configuration — checked entry by entry across the whole family — hence
reducible, and its stationary distributions on the states form a simplex of
measured dimension 15 in the diagonal sector, where $B$ is the identity, and 14
in the other two. Double stochasticity does single out the uniform state
measure as stationary; but the uniform measure on the states is the counting
measure, which is the very object candidate (b) calls the declared null.

That is the sentence this unit was built to be able to say, and it is sharper
than the one it replaces. **The substrate derives a LAW. It derives it over the
states, at every configuration, by its own Born layer, exactly. It derives a
measure on neither space — and over the configurations it derives nothing at
all.** The asymmetry this unit reports is law against nothing, not measure
against nothing.

### 4.8 (h) Pull-back from the holonomy group

A finite group's Haar measure could in principle be pulled back along the map
from configurations to holonomies. There is no single group to borrow from: the
parent measures a finite alternating class on one sector and an **infinite**
group on the other, at 512 configurations, so on most of this arena the
holonomy group carries no normalisable invariant measure at all. And the map is
not injective, so a pull-back would in any case need a declared section, which
is one more free item and not one fewer — and that section is what this row's
price counts.

### 4.9 (i) Maximum entropy

Maximum entropy is the move a reader reaches for, so it is a census row and not
a paragraph. It does not escape the price; it relocates it, by two different
routes for its two sub-cases. The entropy functional is defined relative to a
reference measure, and the two references available here are exactly the two
nulls of section 4.2, which are measured to disagree: maximising relative to
counting-on-configurations returns counting-on-configurations, and maximising
relative to counting-on-orbits returns counting-on-orbits. Under a constraint
$\langle f\rangle = c$ the principle instead returns $e^{-\lambda f}$ times
that reference, which is candidate (f) with its constraint supplied. And the
arena pins no quantity to condition on: every quantity the parent pins for the
sets this unit weighs is an integer count greater than one, and a count is not
a mass without a declared measure (E-24), so there is nothing here to set
$\langle f\rangle$ equal to. The price is the reference plus the constraint.

### 4.10 (j) The stationary measure — named absent, not omitted

A stationary measure needs a dynamics to be stationary for. The parent declares
in the window quoted in §4.6 that it has none for the link variables, and
nothing in the corpus supplies one on the configurations: the corpus's update
law carries division counts as its carrier, not coins, which is the same gap
candidate (a) measures. So this row cannot be priced at all, and it is entered
as `NOT-CENSUSABLE` rather than dropped — 1 named-absent row, carrying the
requirement a future unit would owe: a covariant chain's stationary measures
are invariant, so it can only ever pick a point of the same simplex, and it
fixes that point uniquely exactly when **irreducibility** supplies the
transitivity the symmetry group does not. No symmetry supplies it.

This is also why the third pre-registered outcome is **forced shut
census-relatively** and not as a fact about the arena: of the rows that can be
evaluated, none is blocked at an object; the row that could have been blocked
is the one that cannot be evaluated, and it is named.

## 5. The uniqueness gate, which is gated, can pass, and is run

Uniqueness is the claim this kind of unit is most likely to assert without
earning, so it is decided by a predicate that could return the other answer.
The invariant measures are exactly the orbit-constant ones; a measure is
uniquely fixed by invariance if and only if the group acts transitively; the
group is measured not to.

That the derive arm was reachable is not asserted here. It is **run**, in the
plain delivery run, as a labelled control. A synthetic carrier whose declared
group *is* transitive is handed to the same pricing function this arena's
invariance candidate is handed to, to the same fibre builder, and to the same
head law: its orbit predicate returns 1 orbit, its fibre is a 0-simplex — a
point — and the control arm is priced at 0 free items and emits
`MEASURE-DERIVED-<AN-INVARIANCE-CHARACTERISED-MEASURE;UNIQUE>`. Both branches
of the wiring are gated together — zero free items exactly at a transitive
reading, on the control and on this arena alike — so a price unwired from the
measurement dies at that gate. Nothing about this arena is measured on the
control arm; what is measured is that the negative reported here is a property
of the arena and not of the instrument's standard.

## 6. The price: exactly what a declaration must add

This is the BRG dichotomy applied where it belongs — the declaration is
**priced**, not deplored. After every symmetry this arena measures has been
imposed, what remains is:

1. **which chart group is declared** — the axis §3 measures three instances of,
   and the one that moves the simplex from 207 to 119;
2. **the carrier** — the uniform slice or the full space, a free choice with
   unbounded fibre and 2 declared instances;
3. **one point of the invariant simplex over that carrier's orbits** — a
   207-dimensional simplex at the anchored chart reading, and
   119 independent numbers at the extension reading.

That is the whole of it, and it is the head:
`MEASURE-DECLARATION-REQUIRED-<ONE-POINT-OF-THE-INVARIANT-...-SIMPLEX>`. The
word **invariant** is the word that makes the number true: a declaration is not
obliged to be invariant, and a non-invariant declaration on the slice pays 639
numbers instead. A declaration supplying fewer conditions than that has not
fixed a measure; a declaration supplying more has over-determined one and
should say which of its conditions were redundant.

## 7. The consequence: the declaration is not innocuous

If the choice among invariant measures moved nothing, pricing it would be
pedantry. It moves the parent's own headline numbers. Every set below is
checked to be a **union of orbits** at both readings, object by object and
never by a cardinality, so its mass is well defined under every measure
compared; and each is R5's own, reproduced here from the definitions rather
than quoted — the non-flat census returns 632 of 640 are non-flat, the
non-commuting census 576 non-commuting, and the defect census 384, each
measured against the parent's receipt at a named path.

Every column below is labelled with the measure that produces it, and the
column that is not a probability is stamped as a count (E-24): **no count in
this table becomes a probability without one of the declarations to its
right.** The three measures are all invariant under everything this arena
measures — which for the orbit-uniform nulls is not automatic and is measured
rather than argued: an orbit-uniform measure built on one reading's orbits is
invariant under a larger group only if that group carries each orbit onto
another of the same size, and it does, because the swap conjugation normalises
the twist subgroup. Without that check the comparison would be between measures
answering different questions.

| set | configurations (COUNTING-ONLY) | counting measure on configurations | orbit-uniform null, chart-32 | orbit-uniform null, chart-128 |
|---|---|---|---|---|
| NON-FLAT | 632 | 79/80 | 25/26 | 23/24 |
| NON-COMMUTING | 576 | 9/10 | 9/13 | 7/10 |
| DEFECT-CARRYING | 384 | 3/5 | 6/13 | 7/15 |
| DIAGONAL | 64 | 1/10 | 4/13 | 3/10 |

R5's headline — that the commutator subgroup is non-trivial at 576 of 640
uniform configurations — becomes a probability of 9/10 at the counting measure
and 9/13 at the orbit null, a spread of 27/130. The defect-carrying set moves
from 3/5 under counting to 6/13 under the orbit null. The abelian arm, which is
exactly the sector where the holonomy is pure phase and every commutator
vanishes, is 1/10 of the slice by count and 4/13 of it by orbit. That widest
spread is attained **twice** — on DIAGONAL and on NON-COMMUTING — and the
verdict publishes the whole arg-max set with its multiplicity rather than
naming whichever of the two an alphabetical sort returned first.

So a reader handed "the natural measure on configurations" has been handed a
**choice**, and the choice moves the probability of the parent's central
structural fact by more than a fifth. That is the measurement that makes the
declaration price real rather than rhetorical.

## 8. The withheld segment

The pin licenses a Wilson-loop expectation segment **only in the derived case**:

> the Wilson-expectation segment only in the DERIVED case

No source derives, so the segment is withheld — and the discipline is enforced
on the product rather than promised in prose, at a depth that a rename does not
walk past. A gate walks the published payload to the bottom, not at its top
level only, and requires the receipt to carry no expectation-valued key at all
at any depth; the same gate reads the instrument's own syntax tree for a banned
function however it is defined — `def`, `async def`, or a lambda bound to a
name — and a second gate requires the set of functions this source defines to
equal a declared inventory exactly, so a neutrally-named function computing the very quantity this unit
withholds, carrying no banned word at all, dies as surely as a named one.
Four mutants plant those four evasions.

The pin's other must-not is inherited verbatim from R5 and swept over this
paper's own text with the declaring sentences removed first:

> **The confinement word stays behind its gate: this unit builds the measure;
> it makes NO area-law, string-tension, or potential claim**

The list that implements it is the pin's own words, the bare ones included, and
inline emphasis is stripped before the sweep, so a claim under asterisks is
still the same claim. This unit builds no such claim, and could not: every
object such a claim would need is either absent from the arena or, as of this
unit, priced and unpaid.

## 9. What this decides, and what it does not

**Decided, at the declared scope.**

- **No measure on the configurations derives.** 9 candidate sources, 0 derive,
  each priced in free items by a measured list and each with its reason
  measured; and the census carries the criterion that makes the list a test.
- **The measured symmetry fixes a support and not a measure**, and the support
  it fixes is exactly R5's declared sweep: the chart-fixed configurations are
  exactly the 640 uniform configurations, at 655360 of 655360 checks. Under the
  extension 32 of them survive; under the translations alone the fixed locus is
  the 409600 two-coin configurations instead, so the result is carried by the
  direction relabelling and is chart-declaration-relative.
- **Uniqueness fails, and is gated rather than asserted**: 208 orbits at the
  anchored reading and 120 orbits at the extension, against the 1 that
  transitivity would require, with the derive arm demonstrated by a control arm
  that emits the other head.
- **The price is exactly one point of an invariant simplex over the orbits**: a
  207-dimensional simplex, or 119 independent numbers at the other reading,
  after a chart and a carrier have been declared.
- **The substrate does derive a law — over the states.** The Born layer is
  doubly stochastic at every configuration and takes 3 distinct Born kernels
  over the whole family, so it cannot separate configurations within a sector;
  and pressed for a measure it fixes none, its stationary distributions forming
  a simplex of dimension 15 in the diagonal sector, where $B$ is the identity,
  and 14 in the other two.
- **The one canonical measure this arena hands over is Haar on the
  128 monomial coins**, and it carries 0 of the 384 defect-carrying coins.
- **The choice is not innocuous**: the parent's headline sets move between
  invariant measures, by up to 27/130.

**Not decided, and named.**

- **Whether a correspondence to this target could be built.** Weld 2's
  structural blade is silent here because this lattice is bipartite, and this
  unit did not run a fresh census at this target. It measures that no *pinned*
  correspondence reaches this arena, and that the ones that exist elsewhere
  leave the coin free. It does not measure that none can exist. The question is
  open over the even-$L$ family; at odd $L$ the inherited blade fires.
- **The orbit count of the full configuration space under the joint group.**
  Not computed, by cost; the chart-alone count is exact and a lower bound for
  the joint group is exhibited instead, which is all the argument needs.
- **Which measure to declare.** This unit prices the declaration and does not
  make it. Declaring one is a separate act with its own pin, and the price
  above is what it must pay.
- **Anything on the far side of a measure.** No expectation of any kind is
  computed here, and every object a confinement-shaped follow-on would need
  beyond the measure is untouched.

## 10. The instrument

The instrument is `v14/code/r5m_measure_exact.py`, and its contract is the
era's minimum (#82): a delivery run that is the only writer, a `--no-write`
twin, a falsification self-test that corrupts one anchor class in memory and
must die writing nothing, a per-mutant runner, an all-mutants sweep, a mutant
and gate listing, and a `--verify-paper` mode. Unknown flags exit 2. No flag is
a no-op and no flag is mutant-only. The exit conventions invert the usual
reading and are therefore disclosed in the usage string, in the receipt and
here: the delivery run exits 0 on success and 1 on any refusal, writing
nothing; `--selftest` exits 0 when every anchor class is fatal; `--mutant`
exits 0 when the named mutant *dies* on its declared target.

68 gates in the sealed ledger, and two closing gates that cannot be inside it —
the seal and the artifact integrity check — whose warrant is published beside
them. 44 declared mutants, all dead, each at the gate it was declared to
falsify — and the registry is checked TOTAL against the instrument's own syntax
tree, so a falsifier cannot exist as an unswept branch, none can be declared
without a branch to fire, and a switch the scan cannot read — `mut()` on a
variable, or a bare `MUT` comparison outside `mut`'s own body — is fatal rather
than forgiven. The gate ids are read off the same tree and reconciled at the
seal against the ledger this run produced, so a gate closing after the snapshot
cannot go unpublished. 55 anchors in all: 10 file-bytes anchors,
33 path-value anchors and 12 verbatim-text anchors, each window pinned by its own digest and its own
frozen character count against a declared floor, each located exactly once
under whitespace and markdown-prefix normalisation (#125), each perturbed at a
content-bearing token and required to stop being locatable, and each bound to
the gate that consumes it (#87). The #34 ledger is published at an honest
denominator in 3 classes and no more — covered by a declared mutant, registered forcing,
and no falsifier reaches it — the last named rather than folded into the
first; the fourth class an earlier draft published was unreachable by
construction and is gone.

The paper gates run in five legs, in the plain delivery run and not in a
separate mode (#20): claim rendering, the complete verdict string by equality,
the must-not vocabulary sweep with the declaring sentences removed first, claim
polarity, and numeral coverage over every numeral including the fenced verdict
block, the inline code spans, and both sides of every fraction. Claims are
gated at their **occurrence count** rather than by presence anywhere, so a
number corrupted at one of its several occurrences dies; the three tables are
rendered row by row, so a cell swapped under its own column heading dies; and
the fenced blocks are compared as a multiset (E-22). The structural literals
the coverage gate is permitted to forgive — section numbers and the engraving
references — are published in the receipt, so a reader can see exactly what it
was allowed to forgive.

Every published object carries the gate-to-disk seal, and the manifest — each
object, the receipt key it was taken at, the gate whose passing took it, and
the digest — is published in the receipt, so the seal is auditable from the
artifact alone. The manifest is **total**:
every top-level key of the receipt is either sealed at the gate that produced
it or named in the declaration with the reason it cannot be. The gate ledger is
snapshotted before the two closing gates and the snapshot is what is sealed and
written, with the closing gates recorded separately and their count derived
from the same list their names are published from — a seal cannot be inside the
object it seals.

The head is derived twice, by **two laws**. The builder computes it from the
live measurements; the reconstruction reads only the serialized receipt,
carries a second implementation of the head law written from the same
pre-registered outcomes with a different branch structure and no shared format
string or helper, and re-renders every segment from the primitive measured
tables, reading neither the builder's segments nor its counts. The two heads
are compared, and then the two complete strings are compared.

**The choice inventory.** 11 construction choices are inventoried, each with
its fibre and its declared instances. The lattice, the alphabet, the coin
family, the link and plaquette sets and the gauge action's form are FORCED with
fibre 1; the base plaquette is STABILIZER-FIXED; and exactly 4 rows are flagged verdict-determining
— which chart group is declared, which carrier, which null, and which candidate
sources are censused — because each carries a **measured** predicate: re-running
the measurement it governs under this unit's other declared instance moves a
published number. The flag binds the row and not the total, so moving it
between rows dies (#87). A genuinely free choice with fibre 1 is a
contradiction in terms and none is reported.

## 11. The successor register

- **The stationary-measure unit.** New, and unownable today: it requires a
  declared dynamics on configuration space and an irreducibility argument as a
  gate rather than an assumption, and nothing committed supplies either. It is
  the row §4.10 names absent, and it is the next gate on this road.
- **The correspondence census at this target.** Weld 2's structural blade does
  not fire on a bipartite target, so the question it answered elsewhere is
  genuinely open here, over the even-$L$ family: can any grammar object supply
  this arena's sites, and any object pair its links? This unit did not run it.
  At odd $L$ a scaling unit inherits a closed census for free.
- **The declaration itself, with its pin.** If the programme wants
  expectations, it must declare a measure and pay the price section 6 computes.
  The two nulls are the cheapest candidates and they disagree; a pin that
  declares one owes an argument for it that this arena does not supply.
- **The non-uniform configurations.** Everything above is measured on the
  chart-fixed slice. The full space has 561 sector multisets and a chart-orbit
  count this unit computes exactly; the joint-group orbit count, and hence the
  exact simplex dimension there, is open.
- **Whether the Haar carrier is the whole story.** The monomial subgroup is
  maximal among family subgroups containing it, measured at 0 of 512. Whether
  some *other* subgroup of the family is larger is not decided here, and the
  question matters because it is the only route to a derived measure this
  census found.
- **The Born layer's fibre, re-posed at plaquette grain.** The collapse is not
  merely 3-to-640: the kernel is the identity off the link's own domino, so
  every single-link Born functional is blind to the other sites by
  construction. A separating functional must be multi-link, and the first place
  to look is the plaquette, where the parent already measures 384 coins
  carrying a defect.

## 12. Deviations, and the register of scope

The pin's arena, gates and must-nots are followed as written. Four points are
recorded as scope rather than deviation.

First, the pin asks for the pinned correspondences to be enumerated honestly
and says that if none exists, that is the finding. This unit enumerates them —
every FOUND row of both pinned weld receipts, weld 2's two positive controls
included — finds none reaching this arena, and adds the grant-generous reading
rather than stopping at the enumeration, because a census that reports only an
absence cannot be checked, and a priced residual can.

Second, the pin names three candidate sources and this unit runs the pin's
three plus six. The extra are not padding — a group structure on the family,
the ambient Haar, the Gibbs route, the Born layer, the holonomy pull-back and
maximum entropy are exactly the routes a reader would reach for next, and a
census that leaves them unmeasured cannot claim that none survives. Two of them
earned their place: the Born layer is the only candidate that derives anything
at all, and the group structure is the only place the arena hands a measure
over. A tenth is named absent because it cannot be priced.

Third, the joint-group orbit count on the full configuration space is not
computed, and the reason is cost rather than argument. What the conclusion
needs is a lower bound, which is exhibited by an invariant and is exact.

Fourth, the correspondence question at this target is left open rather than
inherited as closed, because the blade that closed it elsewhere is measured to
be silent at this lattice's even size. That disclosure is the unit's own, and
it is the one place a reader could otherwise have taken a stronger claim than
the measurements support.
