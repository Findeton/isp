# EPR — is the shadow a complete description?

*v14, the limit programme, paper 38. Instrument: `v14/code/epr_exact.py`;
artifacts `epr_output.txt` and `epr_receipt.json`. Exact arithmetic throughout:
Python integers, `fractions.Fraction`, and the ring Z[w] carried as integer
pairs; an AST scan of the instrument and a recursive type scan of the receipt
are gates. Pin: `v14/note-epr-pin.md`, sha256-12 b1e4cf9a8b9f. Source of
record: `v14/sources/epr-1935-physrev-47-777.pdf`, sha256-12 66b5deb150c4 —
Einstein, Podolsky and Rosen, Phys. Rev. 47, 777 (1935), read in the original.*

---

**The verdict, in three segments, quoted exactly as the instrument emits it.**

```
EPR-SEPARATION<HISTORIES=5,856; BLOCK-PAIRS=421,656; LINK-DISJOINT=105,408; QUANTITY-BEARING-AT-THE-RECORD-LOCALIZATION=18; PREMISE-AT-THE-RECORD-LOCALIZATION=0; PREMISE-AT-THE-STATE-LOCALIZATION=105,408; SUBSET-LATTICE=512; SUBSETS-WITH-BOTH=0; THEOREM=THE-LINK-GRAPH-IS-COMPLETE-MULTIPARTITE-AND-A-PART-OWNS-NO-CELL>
```

```
EPR-CENSUS<LOC-PAIR-x-SEP-LINK-DISJOINT=EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY-AT-0-PAIRS-0-CERTIFIED-0-UNCARRIED; LOC-PAIR-x-SEP-ACTOR-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-18-PAIRS-54-CERTIFIED-54-UNCARRIED; LOC-WALK-x-SEP-LINK-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-105,408-PAIRS-316,224-CERTIFIED-316,224-UNCARRIED; LOC-WALK-x-SEP-ACTOR-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-421,656-PAIRS-1,265,112-CERTIFIED-1,265,112-UNCARRIED>
```

```
EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY<PRIMARY-ARM=THE-RECORD-S-OWN-LOCALIZATION-AT-EPR-S-OWN-SEPARATION; SECOND-WORD=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-THE-STATE-LOCALIZATION-WITH-316,224-CERTIFIED-AND-316,224-UNCARRIED; E4-ASSIGNMENTS-AT-ONE-RECORD=5; E5-RECORD-MOVES=0-OF-105,408; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,KINEMATIC-SEPARATION-AS-MEASURED;COUNTS-ARE-COUNTING-ONLY;NO-LOCAL-REALISM-CLAIM>
```

Between delivery and adjudication every headline here is a **candidate
reading**.

---

## The short of it

EPR ask a theory two questions. Is there an element of reality here? — yes,
if the quantity can be predicted with certainty from data that does not
disturb the system. Is the description complete? — yes, if every such element
has a counterpart in it. This unit turns both into total exact predicates on
the committed arena and runs them.

The first measurement is not the completeness verdict. It is whether EPR's
premise exists at all. It does not, in the localization the record itself
uses: `0 of 512 subsets of the nine actors own a record quantity and a
conditioning region sharing no link with them`, and of the corpus's block
pairs, `of 421,656 ordered block pairs 105,408 are link-disjoint and 18 carry
a record quantity at the block, and 0 carry both`. The reason is a theorem
about this arena and it is one line long: a record entry is indexed by a cell,
a cell IS a co-division pair of actors, and a set of actors that still has
somewhere to be conditioned from lies, together with that somewhere, inside a
single line of the one parallel class the arena does not declare — a line
inside which no two actors are linked, so no cell lies inside it either.
Quantity-bearing and separated are mutually exclusive here. So **the criterion
is inapplicable at the record's own localization**, and that is the head.

It is not the whole answer, because the quantum state localizes the same
number somewhere else. paper-20's coin at site x reads n_l(x) — a record entry
whose referent is the pair {x, x+l}, one of whose actors lies outside x and is
linked to it. In THAT localization the premise exists: `in the state's own
localization the same predicates return 105,408 instances of the premise`, and
the whole EPR argument runs. The result is EPR's own: the record certifies
`316,224` elements and carries every one of them; the shadow carries none.
So the second word is `EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE`, and the
locality that EPR's criterion needs is bought, here, by attributing to a block
a quantity that belongs to a pair straddling its boundary.

The shadow's blindness is not an accident of a state. The coin reads
w^{n mod 3}, so `not one of the 64 declared states separates two committed
records that share a residue class`: `the corpus carries 36 distinct records
and the shadow can separate at most 9 of them`, and the best state in the
declared family separates 4. The audit is run at that best state, not at a
strawman.

---

## 1. The arena, the referent, and what separation means

The arena is the parents': AG(2, 3) with nine sites, three declared link
directions of the four parallel classes, the 27 co-division cells, paper-21's
72 I7-STRICT triples at R = 3, their 5,184 ordered concatenations and the 600
driven-window schedules — 5,856 committed histories, rebuilt here by this
unit's own constructors and cross-checked against the parent quantity by
quantity.

Two structures decide everything below and both are measured rather than
assumed.

**The link graph.** Two sites are linked when some declared cell IS the pair
they form. Measured: `two sites are unlinked exactly when they lie on a common
line of the one parallel class the arena does not declare, at 72 of 72 ordered
site pairs`. The graph is therefore complete multipartite with those three
lines as its parts, and every site has degree six. The one direction the arena
does not declare is exactly the direction along which separation is possible.

**The referent of a quantity.** The record is n_l(x), the count of division
events containing both the actor at x and the actor at x + l. Its index is a
cell, and the cell is the unordered co-division pair — re-verified here, not
inherited: the 27 cells are in bijection with the 27 pairs, each cell carries
two actors, each actor sits in six cells. A record entry is a quantity of a
PAIR.

Those two facts are the whole of measurement one. The no-disturbance clause is
SEC's adjudicated ruling read as a definition: **the union changes geometry
only on links both sectors jointly own; no sector-private link ever moves** —
so conditioning data disturbs a block exactly when it shares a link with it,
and the admissible conditioning region is the part of the arena that shares
none.

## 2. The two criteria, as predicates

EPR's criterion of reality is quoted in the pin from the original: *"If,
without in any way disturbing a system, we can predict with certainty (i.e.,
with probability equal to unity) the value of a physical quantity, then there
exists an element of physical reality corresponding to this physical
quantity."* Their condition of completeness is *"every element of the physical
reality must have a counterpart in the physical theory."*

Formalised:

- **EPR-REALITY(q | D, B, sep)** — the description D fixes the value of the
  quantity q of block B from its content on a region satisfying the declared
  separation from B. "With probability equal to unity" is rendered
  measure-free: the value is constant on the conditioning fibre. That is
  probability one under every measure of full support, and the instrument
  checks exactly that as exact rationals under two declared measures, in both
  directions, at 1,080 probes.
- **EPR-COMPLETE(D)** — every pair (history, quantity) at which EPR-REALITY
  holds has a counterpart in D: D's own content at the block fixes the value.

Both are total: every predicate is exercised on every combination of a
declared probe set, 210 probes, no failures, and the totality is a gate. The
twelve predicate functions are located in the instrument's source by AST,
digested individually and jointly before a census row runs, and their free
names are required to contain no census product, so no predicate can consult
the answer it decides.

Two declared axes, both run, neither retired:

- **localization** — LOC-PAIR, the record's own (a cell belongs to a block
  when the block owns both its actors), against LOC-WALK, the state's own (the
  cell (x, l) is read at site x, because the coin consumes it there).
- **separation** — SEP-LINK-DISJOINT, EPR's own clause as ruled, against
  SEP-ACTOR-DISJOINT, the weaker one that only forbids a shared actor.

## 3. Measurement one — does EPR's premise exist here?

The complete lattice of subsets of the nine actors is censused: `490 subsets
own a record quantity and 19 have a nonempty far region`, and `0 of 512
subsets of the nine actors own a record quantity and a conditioning region
sharing no link with them`. The nineteen are the empty set, the nine
singletons and the nine unlinked pairs; every one of them lies inside a single
part of the link graph, and a part is a triple no cell lies inside.

The same predicates then run over the corpus's blocks — FAC's forced
per-history decomposition, rebuilt here from its two binding legs and gated
against the parent's cardinality distribution, its inventory and its four
named exceptions at their own corpus indices. Result: `of 421,656 ordered
block pairs 105,408 are link-disjoint and 18 carry a record quantity at the
block, and 0 carry both`.

EPR's clause admits a second reading, and it is measured rather than
dismissed. The kinematic reading — SEC's ruling, and the one the pin declares
— forbids a shared link. The dynamical reading asks the more literal
question: can anything that happens inside the conditioning region change a
record entry the block owns? A record entry of a block is a cell with both its
actors in the block, and an event increments a cell only when it contains both
of that cell's actors, so an event confined to an actor-disjoint region cannot
reach one. Measured over every event shape this arena admits rather than only
over the ones the corpus runs: `over the 84 event shapes this arena admits, an
event confined to an actor-disjoint region changes a record entry the other
block owns 0 times, while 342 unconfined ones do reach a block's quantities`.
The probe is sighted — the positive control is in the same census — and the
consequence is that the second row of the census table below is not a
concession but the dynamical form of "without in any way disturbing". The head
is taken at the kinematic reading, which is the stronger one.

So the premise is not scarce here; it is impossible. Both halves exist —
separated pairs are everywhere, quantity-bearing blocks occur at three
histories — and they never coincide. That is a fact about the arena's
smallness and it is stated as one.

And it is localization-relative: the premise exists in the state's
localization, where `in the state's own localization the same
predicates return 105,408 instances of the premise`. The state reads the same
number at one endpoint of a link the record owns jointly, and that single
difference in bookkeeping is what makes EPR's question askable.

## 4. The two descriptions and the shadow's ceiling

**D-RECORD** is the theory's own state: the committed history and the record
field it writes. **D-SHADOW** is paper-20's Reading A, the Born menu
k_1(l|x) read off the coin at the record — the wave-function analogue, and the
only object in this corpus that plays the wave function's role.

The record enters the shadow through one door: the coin is
C(x) = G . D(x) with D(x) = diag(w^{n_l(x)}), and **the walk consumes the
count residue n mod 3, not the count**. Two consequences, both measured.

First, a ceiling that no state can raise. `not one of the 64 declared states
separates two committed records that share a residue class`, and `the corpus
carries 36 distinct records and the shadow can separate at most 9 of them`.
The corpus really does contain records with equal residues and different
counts — four rounds of one parallel class against one round of it — so this
is not a vacuous bound.

Second, the audit is given the shadow's best case: the primary state is
required to attain the maximum of the sweep, and it does, at 4 distinct menus.

paper-20's other coin order is measured blind altogether: a `phase applied
after the coin cannot enter that step's Born weights at all`, and the reading
it defines has one cell with all 36 records in it.

## 5. Measurement two — the certainty census

Four arms, every ordered block pair of every admissible decomposition of every
committed history, quantity by quantity.

| localization | separation | pairs | quantities | certified | uncarried by the shadow | word |
|---|---|---|---|---|---|---|
| LOC-PAIR | SEP-LINK-DISJOINT | 0 | 0 | 0 | 0 | EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY |
| LOC-PAIR | SEP-ACTOR-DISJOINT | 18 | 54 | 54 | 54 | EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE |
| LOC-WALK | SEP-LINK-DISJOINT | 105,408 | 316,224 | 316,224 | 316,224 | EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE |
| LOC-WALK | SEP-ACTOR-DISJOINT | 421,656 | 1,265,112 | 1,265,112 | 1,265,112 | EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE |

The first row is the head: the census has nothing to run on, and a description
that passes a completeness test with an empty element set has not passed
anything. That is why the honest word there is the inapplicable one and not
`EPR-BOTH-COMPLETE`, which the same law does return — on a control arm, where
it is earned.

`at the state's localization and EPR's own separation the record certifies
316,224 elements and the shadow carries 0 of them`: the shadow carries none of
the certified elements, on any arm where there are any. The record's own
counterpart count is the complement: no certified element lacks a record
counterpart, on any arm. And `at the record's own localization under the
weaker separation the census runs at 18 pairs and 54 quantities` — the three
histories whose every round repeats one declared parallel class, where a block
is a line and owns three cells. Same verdict there.

Two disclosures belong beside these counts.

The certainty is carried by a property of the committed window, not by a law:
`the record field is site-constant at 5,856 of 5,856 committed histories`. The
nine site rows of a history are equal, so the record on any nonempty region
fixes the record everywhere. That is this corpus's version of the perfect
correlation EPR's entangled state supplies, and it is measured, not assumed;
without it the criterion would certify far less.

And the shadow certifies nothing of its own: `the shadow itself certifies 0
elements at any of the four arms`. A coarse description is trivially complete
about what it can itself predict, which is why the contentful reading is the
cross-description one — elements certified by the theory's own state, asked
for a counterpart in the candidate description. Both readings are in the
receipt.

## 6. Measurement three — the two reductions

EPR: *"it is possible to assign two different wave functions (in our example
psi_k and phi_r) to the same reality."* Here the object is a count. One
committed record; five declared readings of the separated block — the record,
the Born menu at both coin orders, the record menu, and paper-20's own
curvature; and the description assigned to this block is the set of values its
quantities can still take given what the reading reports. Measure-free, so no
measure is smuggled in.

`the five declared readings assign more than one description to the same
record at 105,408 of 105,408 probes, and as many as 5`. The fibre is published
as a distribution rather than as an average:

| arm | assignments at one record | probes |
|---|---|---|
| LOC-PAIR x SEP-ACTOR-DISJOINT | 4 | 18 |
| LOC-WALK x SEP-LINK-DISJOINT | 3 | 594 |
| LOC-WALK x SEP-LINK-DISJOINT | 4 | 8,514 |
| LOC-WALK x SEP-LINK-DISJOINT | 5 | 96,300 |
| LOC-WALK x SEP-ACTOR-DISJOINT | 3 | 2,382 |
| LOC-WALK x SEP-ACTOR-DISJOINT | 4 | 34,062 |
| LOC-WALK x SEP-ACTOR-DISJOINT | 5 | 385,212 |

One disclosure: at this corpus the reading's value does not depend on WHICH
separated block is read, because the record field is site-constant. What is
measured here is dependence on the READING, which is EPR's variable.

## 7. Measurement four — the non-commuting pair, and the dilemma

EPR's dilemma: *"either (1) the quantum-mechanical description of reality
given by the wave function is not complete or (2) when the operators
corresponding to two physical quantities do not commute the two quantities
cannot have simultaneous reality."*

The corpus has both halves of the antecedent. At the operator level, `the two
declared coin orders differ at 30 of the 36 committed records` — G . D(x)
against D(x) . G, compared exactly in Z[w]. At the reading level, the five
declared readings are measured as partitions and their refinement relation is
computed in both directions for all twenty-five ordered pairs:

| reading | cells | largest fibre |
|---|---|---|
| READ-RECORD | 36 | 1 |
| READ-BORN-GD | 4 | 12 |
| READ-BORN-DG | 1 | 36 |
| READ-RECORD-MENU | 23 | 4 |
| READ-CURVATURE | 3 | 13 |

Three pairs are not jointly declarable — neither refines the other — and one
of them is paper-20's own pair: the Born menu against the record menu. Two
records with equal residues have the same Born menu and different record
menus; two records with proportional counts have the same record menu and
different Born menus. Neither reading is a coarsening of the other.

Now the dilemma, decided per description. `the record carries both members of
the conjugate pair at 5,856 of 5,856 committed histories` — READ-RECORD
refines every declared reading, so the record fixes both values at once. No
single Born menu carries both. So horn (1) holds for D-SHADOW: it is not
complete, measured in section 5. And horn (2) fails for D-RECORD: two readings
whose operators do not commute have simultaneous values there.

That is EPR's conclusion reached inside a committed theory rather than argued
for from outside it — and section 9 says exactly what it does not license.

## 8. Measurement five — the E5 audit

EPR refuse a reality that depends on a measurement made elsewhere: *"This
makes the reality of P and Q depend upon the process of measurement carried
out on the first system, which does not disturb the second system in any
way."*

Measured on the arm where the criterion is instantiable here: `B's own record
moves at 0 of 105,408 probes and the description assigned to B moves at
105,408`. B's own shadow does not move either. In one sentence: **B's record
does not move with the reading declared at A**, and nothing B has moves at
all; what moves is the description an observer at A assigns to B.

The test-declaration duty is discharged rather than promised. The probe is
SIGHTED: B's record and B's shadow are recomputed through a
reading-parameterised path, and a declared falsifier routes the reading's own
index into both of them and dies at this gate. The zero is a measurement, not
a blind spot.

This is SEC's ruling seen from the other side. No sector-private link moves,
so nothing done to a separated block can move this one's record. What EPR
would not permit — a reality depending on the distant choice — does not occur;
what does occur is a description depending on it, which is section 6.

## 9. The Bell wall

The corpus's standing verdict is v5 paper-14's, and it is a wall here, not a
result to be revisited: **ISP cannot satisfy Bell local causality and still
reproduce the Tsirelson violation. It is Bell-nonlocal**, while **ISP is
no-signalling and parameter-independent; there is no superluminal causal
influence in its dynamics**. Outcome independence is what fails.

| desideratum | D-RECORD | D-SHADOW | Bell-constrained |
|---|---|---|---|
| E1 counterpart for every element | met on the measured arms | not met | no |
| E2 certainty without disturbance | instantiable only in the state's localization | never here | no |
| E3 simultaneous reality for a conjugate pair | held at every history | refused | yes |
| E4 one reality, several assignments | one record throughout | up to five assignments | no |
| E5 no dependence on the distant choice | zero moves measured | the assigned description moves | no |
| E6 such a theory is possible | one exists on the measured arms | not applicable | yes |

Two rows are constrained and they are the two that matter. EPR close by
saying *"we left open the question of whether or not such a description
exists. We believe, however, that such a theory is possible."* On the measured
arms this corpus has one — and it is not a local-realist one. The joint value
assignment across separated blocks that D-RECORD carries lives at the
outcome-dependence level the corpus already owns; no sentence of this unit claims a
restored locality, an evaded Bell theorem, or a vindicated hidden-variable
completion, and the instrument scans this paper's own bytes for seven such
sentences.

There is also a finding here rather than only a prohibition. At this arena
EPR's criterion is instantiable only in the localization the quantum state
uses, and there the quantity attributed to a block has as its referent a
co-division pair straddling that block's own boundary. The element the
criterion certifies is not local to the block it is certified for. EPR's
premise — that a criterion of reality can be applied to a system in isolation
— is where this arena resists them first, before any question about
completeness is reached.

## 10. The control arms

Every pre-registered word is emitted by the REAL head law on declared data.
None of these rows is forged: each is an evaluation of the same predicates.

| arm | premise instances | certified | uncarried by the record | uncarried by the shadow | word |
|---|---|---|---|---|---|
| CTRL-COMMITTED-LOC-PAIR | 0 | 0 | 0 | 0 | EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY |
| CTRL-COMMITTED-LOC-WALK | 105,408 | 316,224 | 0 | 316,224 | EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE |
| CTRL-D-SHADOW-SYNTH-INJECTIVE | 105,408 | 316,224 | 0 | 0 | EPR-BOTH-COMPLETE |
| CTRL-D-RECORD-SYNTH-PUNCTURED | 105,408 | 316,224 | 105,228 | 316,224 | EPR-RECORD-ALSO-INCOMPLETE |
| CTRL-PREDICATE-PARTIAL | 105,408 | 316,224 | 0 | 316,224 | EPR-BLOCKED-AT-THE-PREDICATE-TOTALITY |
| CTRL-ARENA-ONE-DECLARED-DIRECTION | 35,136 | 105,408 | 0 | 105,408 | EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE |

The synthetic descriptions are the decisive ones. Give the shadow forced
injectivity and the same law returns `EPR-BOTH-COMPLETE`; puncture the record
so that one direction's counts are not in it and the same law returns
`EPR-RECORD-ALSO-INCOMPLETE` — and the punctured column is not the whole
direction, because the fibre of the surviving two sometimes pins the third
anyway; declare one predicate partial and it returns the blocked word, which
is what that word is for.

The last row is the one that fixes the head's scope. Run the same predicate
forms on a synthetic arena with a single declared link direction — FAC's own
L1 — and the link graph falls apart into three unlinked triangles, each of
which owns cells. The premise EXISTS there, at 35,136 instances, and the
census runs. So the inapplicability measured in section 3 is a property of the
declared arena, not of this instrument.

## 11. What this does not say

Every count here is COUNTING-ONLY over a declared window; no fraction is a
frequency and no count is a probability. Six windows are declared with their
bounds; the subset lattice is the only complete one.

The phrase "element of reality" occurs in this unit only inside the formalised
predicate and inside verbatim quotation of the 1935 paper. Nothing here says
what is real. The unit measures which descriptions satisfy two criteria, at
which localization, under which separation, and reports that the answer
depends on all three.

The separation measured is KINEMATIC: link-disjointness in the arena's own
conflict topology. It is not a spacelike separation and no claim about
spacelike separation is made or implied; the corpus's relativistic layer is
not in this unit's scope.

The scope is one arena, its committed histories, and the parents' corpus. The
certainty the census finds rests on site-constancy, which is a measured
property of that window; a corpus without it would certify less, and the
successor that would settle this is SEC's multi-sector route — a union of
sectors sharing neither actor nor link, where a quantity-bearing block can
have a separated conditioner and EPR's premise exists in the record's own
localization. That is the named successor to this unit.

The parents FAC (paper 35) and SEC (paper 32) are both **candidate-under-repair**
at delivery. SEC enters only through its adjudicated ruling, which is quoted.
FAC enters through its delivered receipt at sha256-12 240bad74217a; because
its working-tree copy has drifted under repair, that receipt is not read at
run time — its values are cited and every one of them is re-derived by this
instrument and compared quantity by quantity, so a drift in the parent cannot
carry into this unit unnoticed.

## 12. The instrument

Six committed files are read as sources at pinned digests, plus this paper as
the object under test; no other repository state is read and no subprocess is
invoked, so the run is correct off-tree and with no version control present.
The read set is recorded at the I/O layer, so the abstention from the drifted
parent is provable rather than promised. 14 verbatim anchors are matched in
their sources' bytes, each named with the gate that consumes it; the six EPR
quotes are matched in the pin, where they were transcribed from the print, and
the print's own digest is verified. The pre-registered outcome vocabulary is
parsed out of the pin's bytes and reduced to five families, and the head law
may return words from that set and from no other.

The head is derived twice by routes sharing no dispatcher: the census of
section 5 and a second aggregation by distinct record with corpus
multiplicities, which re-applies the localization and separation predicates
inline and re-runs the head law on its own numbers. They agree on every count
of every arm and on every arm word.

30 falsifiers are declared, each naming the gate it must die at and each
carrying a hook located in the instrument by AST and matched against the
statement that describes it, so a description-inverted falsifier cannot pass;
every gate without a falsifier carries a named waiver with its forcing. Seals
are taken at gate time and the manifest is required to be total. Every table
above is rendered from the receipt with its headers included, so a header swap
that leaves every number correct dies at a gate; every printed class word is
recomputed from its predicate; every fraction is resolved against the receipt
and both members required to be carried by one declared referent universe; and
five polarity axes are checked in both directions. Seven banned sentences —
the Bell wall — are scanned against this paper's own bytes, and the falsifier
for that gate plants one into exactly that text. The bytes are read back from
staging and compared with the gate-time seal before `os.replace` promotes
anything.

---

```
EPR-SEPARATION<HISTORIES=5,856; BLOCK-PAIRS=421,656; LINK-DISJOINT=105,408; QUANTITY-BEARING-AT-THE-RECORD-LOCALIZATION=18; PREMISE-AT-THE-RECORD-LOCALIZATION=0; PREMISE-AT-THE-STATE-LOCALIZATION=105,408; SUBSET-LATTICE=512; SUBSETS-WITH-BOTH=0; THEOREM=THE-LINK-GRAPH-IS-COMPLETE-MULTIPARTITE-AND-A-PART-OWNS-NO-CELL>
```

```
EPR-CENSUS<LOC-PAIR-x-SEP-LINK-DISJOINT=EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY-AT-0-PAIRS-0-CERTIFIED-0-UNCARRIED; LOC-PAIR-x-SEP-ACTOR-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-18-PAIRS-54-CERTIFIED-54-UNCARRIED; LOC-WALK-x-SEP-LINK-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-105,408-PAIRS-316,224-CERTIFIED-316,224-UNCARRIED; LOC-WALK-x-SEP-ACTOR-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-421,656-PAIRS-1,265,112-CERTIFIED-1,265,112-UNCARRIED>
```

```
EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY<PRIMARY-ARM=THE-RECORD-S-OWN-LOCALIZATION-AT-EPR-S-OWN-SEPARATION; SECOND-WORD=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-THE-STATE-LOCALIZATION-WITH-316,224-CERTIFIED-AND-316,224-UNCARRIED; E4-ASSIGNMENTS-AT-ONE-RECORD=5; E5-RECORD-MOVES=0-OF-105,408; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,KINEMATIC-SEPARATION-AS-MEASURED;COUNTS-ARE-COUNTING-ONLY;NO-LOCAL-REALISM-CLAIM>
```
