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
EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY<PRIMARY-ARM=THE-RECORD-S-OWN-LOCALIZATION-AT-EPR-S-OWN-SEPARATION; SECOND-WORD=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-THE-STATE-LOCALIZATION-WITH-316,224-CERTIFIED-AND-316,224-UNCARRIED-AND-STATE-INVARIANT-BY-THEOREM; E4-ASSIGNMENTS-AT-ONE-RECORD=5-AT-THE-DECLARED-PRIMARY-STATE-UNDER-THE-MARGINAL-READING; E5-RECORD-MOVES=0-OF-105,408; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,KINEMATIC-SEPARATION-AS-MEASURED;COUNTS-ARE-COUNTING-ONLY;NO-LOCAL-REALISM-CLAIM>
```

Between delivery and adjudication every headline here is a **candidate
reading**.

---

## The short of it

EPR ask a theory two questions. Their criterion says a quantity predictable
with certainty from data that does not disturb the system has, on their
account, a counterpart that a complete theory must carry; their condition of
completeness says every such counterpart must be there. This unit turns both
into total exact predicates on the committed arena and runs them.

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

The shadow's blindness is not an accident of a state, and it is not a fact
about the state family this unit declares. The coin reads w^{n mod 3}, and
the argument of section 4 shows that every Born menu, at every state whatever,
coarsens the residue partition, which carries nothing: `no residue class of
this corpus is a single record, and none is constant in any direction: 0 of 9
and 0 of 9`. The shadow therefore carries none of the certified elements at
every state, by theorem; `the corpus carries 36 distinct records and the
shadow can separate at most 9 of them`, and `not one of the 64 declared states
separates two committed records that share a residue class`.

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

- **EPR-REALITY(q | D, B, sep)** is the formalised criterion and the only
  predicate in this unit that carries the phrase element of reality — the
  description D fixes the value of the quantity q of block B from its content
  on a region satisfying the declared separation from B. "With probability
  equal to unity" is rendered measure-free: the value is constant on the
  conditioning fibre. That is probability one under every measure of full
  support, and the instrument checks exactly that as exact rationals under two
  declared measures, in both directions, at 1,080 probes.
- **EPR-COMPLETE(D)** — every pair (history, quantity) at which EPR-REALITY
  holds has a counterpart in D: D's own content at the block fixes the value.

Both are total: every predicate is exercised on every combination of a
declared probe set, 240 probes, no failures, and the totality is a gate. The
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

Both axes are this unit's own. The pin fixes the blocks, the separation and
the two descriptions; it does not fix where a cell is read, and the head word
turns on exactly that. The primary arm is declared here, not pre-registered,
and it is declared before the census on the ground that a record entry's
referent is the pair — section 1's measurement — not on the ground of what the
arms returned. Section 11 records this against the pin.

## 3. Measurement one — does EPR's premise exist here?

The complete lattice of subsets of the nine actors is censused: `490 subsets
own a record quantity and 19 have a nonempty far region`, and `0 of 512
subsets of the nine actors own a record quantity and a conditioning region
sharing no link with them`. The nineteen are the empty set, the nine
singletons and the nine unlinked pairs; every one of them lies inside a single
part of the link graph, and a part is a triple no cell lies inside.

The same predicates then run over the corpus's blocks — FAC's per-history
decomposition inventory, forced at 5,852 of 5,856 histories and two-membered
at the other four, rebuilt here from its two binding legs and gated against
the parent's cardinality distribution, its inventory and its four named
exceptions at their own corpus indices. Result: `of 421,656 ordered block
pairs 105,408 are link-disjoint and 18 carry a record quantity at the block,
and 0 carry both`. Of those 421,656 pairs only 18 reach the separation test at
all, the rest failing because a block of one actor cannot own a quantity of
two; the general statement is the lattice's, where every quantity-bearing
region in the arena is tested.

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
smallness and it is stated as one. The pin anticipated this word arriving
through a scarcity of separated pairs. It arrives through the opposite:
separated pairs are abundant at 105,408, and none of them carries a
pair-localized quantity.

EPR guard this case themselves. Immediately after stating the criterion they
write: *"It seems to us that this criterion, while far from exhausting all
possible ways of recognizing a physical reality, at least provides us with one
such way, whenever the conditions set down in it occur. Regarded not as a
necessary, but merely as a sufficient, condition of reality, this criterion is
in agreement with classical as well as quantum-mechanical ideas of reality."*
So the criterion's non-instantiation here is not a verdict against anything.
It decides nothing about what is or is not at the pair localization, and it is
not a defeat of EPR's argument: the criterion is silent where its conditions
do not occur,
and so is this unit. What is measured is what this arena will let their test
be applied to.

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

Second, the audit does not depend on which state is declared. Every Born-menu
partition, at every state whatever, coarsens the residue-class partition,
because equal residues give the same D and a global shift of the residues
multiplies all three post-coin amplitudes by one phase that the modulus cannot
see. Both halves of that are exact identities in Z[w] and both are gated. And
the residue partition already carries nothing: `no residue class of this
corpus is a single record, and none is constant in any direction: 0 of 9 and 0
of 9`. So the shadow carries none of the certified elements at every state, by
theorem, and the state family below is a check on the theorem rather than the
ground of the result.

Within the declared family {0, 1, w, w^2} on each of the three site amplitudes
the best state separates 4 distinct menus and the primary state attains it, so
the audit gives the shadow the best case that family has. That family is not
the widest one available, and the disclosure belongs here: over paper-20's own
alphabet — the elements of (1/3)Z[w] of modulus at most one — the shadow does
better and still carries nothing. `over paper-20's own 37-value alphabet the
sweep runs at 50,653 states, the ceiling of 9 menus is attained at 34,992 of
them, and the shadow carries a certified direction at 0`. The declared family
resolves the record more coarsely than the parent's alphabet permits; the
carried count is 0 at both, because it is a theorem and not a property of
either family.

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
the certified elements, on any arm where there are any. And `at the record's
own localization under the weaker separation the census runs at 18 pairs and
54 quantities` — the three histories whose every round repeats one declared
parallel class, where a block is a line and owns three cells. Same verdict
there.

**What the census could not have found.** Two of the three branches the head
law can take are closed at this corpus before any measurement, and saying so
is part of the result. `the quantity censused at a block is one of the block's
own localization's directions at 132 of 132 declared specs`, so a censused
quantity is always one D-RECORD's own content at the block already fixes: the
record-incomplete branch cannot fire on unmutated data. The record's own
counterpart count is therefore the complement, and it is analytic rather than
measured — no certified element lacks a record counterpart, on any arm, on any
history, and on any arena whatever. The census can put that zero at risk only
through the punctured control of section 10, where it duly moves to 105,228.
`RECORD-COMPLETE` is a statement about what the record is, not a finding about
this corpus; the contentful half of the head word is `SHADOW-INCOMPLETE`. The
same containment holds against the conditioner's directions, which is why
certified equals quantities in every row of the table above. And the
both-complete branch is closed by section 4's ceiling before any state is
declared: the shadow's own fibre fails to fix a value at every record and
every direction of every declared state, so no declared state could have
returned `EPR-BOTH-COMPLETE` here. What the census measures at this corpus is
one column — the shadow's.

Two disclosures belong beside these counts.

The certainty is carried by a property of the committed window, not by a law:
`the record field is site-constant at 5,856 of 5,856 committed histories`. The
nine site rows of a history are equal, so the record on any nonempty region
fixes the record everywhere. That is this corpus's version of the perfect
correlation EPR's entangled state supplies, and it is measured, not assumed;
without it the criterion would certify far less.

And two things about the shadow's zero belong in the open. `the shadow itself
certifies 0 elements at any of the four arms`, so EPR's argument in its own
form — the description under test certifies something and is then asked to
carry it — has nothing to run on here; the reading measured above is the
cross-description one, elements certified by the theory's own state and asked
for a counterpart in the candidate description. And that cross-description
column is uniform: it equals the certified column at every arm, because the
shadow's fibres are the residue classes and no residue class of this corpus is
a single record or is constant in any direction. 316,224 is 105,408 times
three; the content is section 4's ceiling, counted once per block pair. Both
readings are in the receipt.

## 6. Measurement three — the two reductions

EPR: *"it is possible to assign two different wave functions (in our example
psi_k and phi_r) to the same reality (the second system after the interaction
with the first)."* The subscripted Greek is transliterated here and nowhere
else. The object is a count. One committed record; five declared readings of
the separated block — the record, the Born menu at both coin orders, the
record menu, and paper-20's own curvature; and the description assigned to
this block is the set of values each of its quantities can still take, taken
quantity by quantity, given what the reading reports. Measure-free, so no
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

Three disclosures. The distribution is relative to that definition of the
assignment: the joint reading, which keeps the correlations between a block's
three quantities, is measured on the primary arm and published beside it in
the receipt as the declared alternative. Of the five readings, three unordered
pairs are non-jointly-declarable; the fibre of five counts declared
coarsenings, not conjugate alternatives. And at this corpus the reading's
value does not depend on WHICH separated block is read, because the record
field is site-constant. What is measured here is dependence on the READING,
which is EPR's variable.

## 7. Measurement four — the non-commuting pair, and the dilemma

EPR's dilemma: *"either (1) the quantum-mechanical description of reality
given by the wave function is not complete or (2) when the operators
corresponding to two physical quantities do not commute the two quantities
cannot have simultaneous reality."*

One half of the antecedent is available in the corpus's own terms and one is
not. At the reading level, the five declared readings are measured as
partitions and their refinement relation is computed in both directions for
all 25 ordered pairs:

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
different Born menus. Neither reading is a coarsening of the other. That is
this arena's rendering of two quantities that cannot be declared together, and
it carries the argument below.

At the operator level the unit exhibits no operator for either member of the
pair. What it can measure is paper-20's declared coin-order fibre: `the two
declared coin orders' operators differ at 30 of the 36 committed records` —
G . D(x) against D(x) . G, compared exactly in Z[w]. That number tracks n mod
3 rather than the record. `the two coin orders commute at exactly the 6
records whose three counts are equal modulo three, and at 3 of those the
record observable is not scalar` — at those three the two quantities' own
operators do not commute at all while the leg reports agreement. The 30 is a
disclosure about the encoding, not an instance of EPR's antecedent.

Now the dilemma, decided per description. `the record carries both members of
the conjugate pair at 5,856 of 5,856 committed histories` — READ-RECORD
refines every declared reading, so the record fixes both values at once. No
single Born menu carries both. So horn (1) holds for D-SHADOW: it is not
complete, measured in section 5. And horn (2) fails for D-RECORD: two readings
whose fibres do not refine each other have simultaneous values there.

That is the shape of EPR's conclusion, exhibited inside a committed theory: a
coarse description that fails the completeness condition and a fine one that
carries a conjugate pair at once. Section 5's disclosure applies — at this
corpus both halves are close to forced — and section 9 says exactly what the
exhibit does not license.

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

What that zero is, exactly. A reading in this unit is a function on records,
not an operation on a history, so nothing declared at A has a path to anything
B holds: no constructor of the arena, the corpus, the record field or the
blocks takes a reading or names one, and that absence is AST-checked. The zero
is forced by that formalisation and would be returned on any arena. The
declared falsifier routes the reading's own index into B's record and into B's
shadow and dies at this gate, which establishes that the instrument carries no
such path by accident — it does not establish that the arena forbids one.

What carries this row as a measurement of the arena is the dynamical census of
section 3, which is one: over the 84 event shapes the arena admits, an event
confined to an actor-disjoint region reaches a record entry the other block
owns 0 times, while 342 unconfined events do reach a block's quantities. That
probe is sighted and its positive control is in the same census.

This is SEC's ruling seen from the other side, and it is a kinematic
statement: no sector-private link moves. It is not a measurement of what any
operation on a separated block would do — the variable moved here is the
declared reading, and section 3's dynamical probe runs at the pair
localization and at block sizes this arm does not contain. Testing SEC's
ruling in EPR's own sense would require an operation on A that the corpus's
dynamics admits, and this unit declares none; that is the honest scope of the
row, and the successor obligation. What EPR would not permit — a reality
depending on the distant choice — does not occur among the readings declared;
what does occur is a description depending on them, which is section 6.

## 9. The Bell wall

The corpus's standing verdict is v5 paper-14's, and it is a wall here, not a
result to be revisited: **ISP cannot satisfy Bell local causality and still
reproduce the Tsirelson violation. It is Bell-nonlocal.** And, on the other
side of it: **ISP is no-signalling and parameter-independent; there is no
superluminal causal influence in its dynamics.** Outcome independence is what
fails.

| desideratum | D-RECORD | D-SHADOW | Bell-constrained |
|---|---|---|---|
| E1 counterpart for every element | met on the measured arms | not met | no |
| E2 certainty without disturbance | instantiable only in the state's localization | never here | no |
| E3 simultaneous reality for a conjugate pair | held at every history | refused | yes |
| E4 one reality, several assignments | one record throughout | up to five assignments | no |
| E5 no dependence on the distant choice | zero moves measured | the assigned description moves | no |
| E6 such a theory is possible | complete for the censused certainty-elements on the measured arms | not applicable | yes |

Two rows are constrained and they are the two that matter. EPR close by
saying *"we left open the question of whether or not such a description
exists. We believe, however, that such a theory is possible."* On the arms
where the census runs, D-RECORD carries every certainty-element the census
certifies. That is completeness **for this census, at this arena, over these
histories** — not the completeness EPR left open, which is a claim about
physical reality and which this unit neither makes nor could make. It is also
not a local-realist result. The joint value assignment across separated blocks
that D-RECORD carries lives at the level the corpus's standing verdict already
owns; the identification of that level with Bell's outcome dependence is the
pin's, not this unit's measurement, and the separation here is kinematic. No
sentence of this unit claims a restored locality, an evaded Bell theorem, or a
vindicated hidden-variable completion, and the instrument scans this paper's
own bytes for seven such sentences and for 14 voice-normalised patterns, and
requires the two sentences above to be present. Those two are rendered flat:
v5 paper-14 states them with its own qualifiers, and stripping the qualifiers
makes the wall stronger rather than weaker, which is the only direction this
unit is entitled to move it.

There is also a finding here rather than only a prohibition. The criterion is
applicable here only in the localization the quantum state uses, and there the
quantity attributed to a block has as its referent a co-division pair
straddling that block's own boundary. The element the criterion certifies is
not local to the block it is certified for. That is a fact about this arena's
smallness, reported under EPR's own sufficiency caveat of section 3: their
test is offered as sufficient and not necessary, and where its conditions do
not occur it decides nothing.

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
declared arena, not of this instrument. Every count in that row is computed by
the same predicates as its siblings, the record's counterpart column included.

## 11. What this does not say

Every count here is COUNTING-ONLY over a declared window; no fraction is a
frequency and no count is a probability. Seven windows are declared with their
bounds, and three of the seven are complete — the subset lattice, the event
shapes and the block lattice; the corpus, the states, the readings and the
measures are declared bounds.

The phrase "element of reality" occurs in this unit only inside the formalised
predicate's own declaration and inside verbatim quotation of the 1935 paper,
and that confinement is a gate over this paper's own bytes rather than a
promise: every occurrence is counted and matched against the declared
carriers. Nothing here says what is real. The unit measures which descriptions
satisfy two criteria, at which localization, under which separation, and
reports that the answer depends on all three.

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

**Provenance, and three corrections against the pin.** The pin is frozen and
is not edited; what follows is carried here.

*The localization axis is not the pin's.* The pin fixes the blocks, the
separation and the two descriptions, and never mentions localization; the
strings LOC-PAIR and LOC-WALK do not occur in it. The head word instantiates
the pin's registered word-form EPR-CRITERION-INAPPLICABLE-AT-, and the
instrument requires the emitted word to lie in the vocabulary parsed from the
pin's bytes; but the axis that selects between the two emitted words, and the
object that names the head, are supplied by this unit. The primary arm is
declared on section 1's measured ground and before the census, and that is the
whole of its warrant.

*The pin's worked example for that word is refuted by the corpus.* The pin
offers "no fully link-disjoint block pair exists at R = 3" as the way the word
might arrive. Link-disjoint block pairs are abundant at 105,408. The word
arrives by the opposite route, and section 3 states it.

*The pin's feasibility lines argue abstract conditions, not this corpus.* Of
the five pre-registered outcomes, two were unreachable before the run: the
record-incomplete branch by the containment measured in section 5, and the
both-complete branch by the residue ceiling of section 4 — both decidable at
pin time, neither decided there. The delivered words stand because they are
true; what is owned is that the selector was two-way and not five-way, and the
paper says so where the census reports it.

*The pin's anchor list omits EPR's sufficiency caveat.* The six anchors E1 to
E6 are the pin's; the caveat quoted in section 3 is not among them, and its
absence let section 9 attribute to EPR a premise their own words disclaim.
The passage is restored here from the print, matched verbatim in this paper's
own bytes at a gate, and put to work rather than displayed.

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
parent is provable rather than promised. 15 verbatim anchors are matched in
their sources' bytes, each naming the gate that consumes it — and the naming
is load-bearing: that gate calls for the anchor inside its own condition, and
a closing gate requires every named consumer to be a gate that actually ran.
The six EPR quotes E1 to E6 are matched in the pin, where they were
transcribed from the print; the caveat is matched in this paper, where it was
transcribed from the print by the repair; and the print's own digest is
verified. The pre-registered outcome vocabulary is parsed out of the pin's
bytes and reduced to five families, and the head law may return words from
that set and from no other.

The head is derived twice by routes sharing no dispatcher: the census of
section 5 and a second aggregation by distinct record with corpus
multiplicities, which re-applies the localization and separation predicates
inline and re-runs the head law on its own numbers. They agree on every count
of every arm and on every arm word.

49 falsifiers are declared, each naming the gate it must die at, each carrying
a hook located in the instrument by AST, and each quoting, as its published
description, the annotation the code carries at that hook — so a
description-inverted falsifier cannot pass. Every gate without a falsifier
carries a named waiver with its forcing, the census that checks this sees
every gate the run runs, and a waiver for a gate that has a falsifier is
refused. Seals are taken at gate time, the manifest is required to be total,
every seal's named gate must be one that ran, and at promotion the receipt's
key set is compared again against the set the manifest was totalled over and
every sealed value is re-derived against its gate-time digest.

Twenty claims and all five tables are rendered from the receipt and matched in
this paper's bytes by occurrence count and by multiset, headers included — so
a header swap that leaves every number correct dies at a gate, a fabricated
row built out of registered numerals dies, and a forged twin of a sentence
this paper says twice dies. The three verdict fences are matched the same way.
Every printed class word is recomputed from its predicate; every fraction must
name a declared universe whose bound is its denominator and one of whose
measured values is its numerator; and seven polarity axes are checked in both
directions, the two horns of the dilemma among them. Every numeral is the run's own product or an identifier in a
declared shape, matched at its own position, and spelled numerals are scanned
through a vocabulary of every English number word. The Bell wall is scanned
against this paper's own bytes in both directions — seven banned sentences and
14 voice-normalised patterns that must be absent, and two verdict sentences
that must be present. The bytes are read back from staging and compared with
the gate-time seals before `os.replace` promotes anything, the promoted paths
are re-read afterwards, and the transcript's own PASS and FAIL lines are
compared with the ledger's rows as a multiset.

---

```
EPR-SEPARATION<HISTORIES=5,856; BLOCK-PAIRS=421,656; LINK-DISJOINT=105,408; QUANTITY-BEARING-AT-THE-RECORD-LOCALIZATION=18; PREMISE-AT-THE-RECORD-LOCALIZATION=0; PREMISE-AT-THE-STATE-LOCALIZATION=105,408; SUBSET-LATTICE=512; SUBSETS-WITH-BOTH=0; THEOREM=THE-LINK-GRAPH-IS-COMPLETE-MULTIPARTITE-AND-A-PART-OWNS-NO-CELL>
```

```
EPR-CENSUS<LOC-PAIR-x-SEP-LINK-DISJOINT=EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY-AT-0-PAIRS-0-CERTIFIED-0-UNCARRIED; LOC-PAIR-x-SEP-ACTOR-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-18-PAIRS-54-CERTIFIED-54-UNCARRIED; LOC-WALK-x-SEP-LINK-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-105,408-PAIRS-316,224-CERTIFIED-316,224-UNCARRIED; LOC-WALK-x-SEP-ACTOR-DISJOINT=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-421,656-PAIRS-1,265,112-CERTIFIED-1,265,112-UNCARRIED>
```

```
EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY<PRIMARY-ARM=THE-RECORD-S-OWN-LOCALIZATION-AT-EPR-S-OWN-SEPARATION; SECOND-WORD=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-AT-THE-STATE-LOCALIZATION-WITH-316,224-CERTIFIED-AND-316,224-UNCARRIED-AND-STATE-INVARIANT-BY-THEOREM; E4-ASSIGNMENTS-AT-ONE-RECORD=5-AT-THE-DECLARED-PRIMARY-STATE-UNDER-THE-MARGINAL-READING; E5-RECORD-MOVES=0-OF-105,408; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,KINEMATIC-SEPARATION-AS-MEASURED;COUNTS-ARE-COUNTING-ONLY;NO-LOCAL-REALISM-CLAIM>
```
