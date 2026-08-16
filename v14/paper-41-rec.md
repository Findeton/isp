# REC — can the cast be read off the record?

*v14, the limit programme, paper 41. Instrument: `v14/code/rec_exact.py`;
artifacts `rec_output.txt` and `rec_receipt.json`. Exact arithmetic throughout:
Python integers and `fractions.Fraction`; an AST scan of the instrument and a
recursive type scan of the receipt are gates. Pin: `v14/note-rec-pin.md`,
sha256-12 0b51e47b7b4b. Parents, read at pinned digests: `v14/paper-33-aid.md`
(the naming), `v14/paper-35-fac.md` (the factorizations), `v14/paper-38-epr.md`
(the completeness audit). This is the first unit built on the E-25…E-33
template, and it answers the registered S-1 family with a machine check.*

---

**The verdict, in three segments, quoted exactly as the instrument emits it.**

```
REC-RECONSTRUCTION<CORPUS=5,856; DISTINCT-HISTORIES=5,784; RECORD-BLOCKS=27; SITE-SET=9-OF-9-EXACT; LINK-STRUCTURE=27-OF-27-EXACT; CAST-SIZE=9-DERIVED; MENU=3-OF-6-EXACT; NAMING=1,296-ADMISSIBLE-108-ARENA-COHERENT; RESIDUE-INDEX=12; LEVEL-0-COUNT-FIELD=36-DISTINCT-CAST-NOT-DERIVABLE>
```

```
REC-MINIMALITY<PER-HISTORY=0-OF-5,856-AT-EVERY-PREFIX; CORPUS-ORDER=17-HISTORIES-145-EVENTS; BLOCK-MINIMAL=27-OF-27-DROP-ONE-SURVIVORS-0; COLLAPSE-THRESHOLDS=3-AND-4-AND-5; CRYSTALLIZATION-ON-C1-AND-C2=5; NEVER-CRYSTALLIZING=4>
```

```
REC-CAST-DERIVED-UP-TO-THE-DIRECTION-DECLARATION<OBSTRUCTION=THE-LINK-DECLARATION; UNWRITTEN-EVENTS=768; PARTLY-UNWRITTEN-HISTORIES=175; HISTORIES-WRITING-NOTHING=1; RECORD-COLLISIONS=39-CLASSES-180-HISTORIES; SURPLUS=1-ARENA-FORCED-4-RECORD-CARRIED-4-NOT-CARRIED; CONTROLS=261-SCRAMBLES-0-SURVIVE-AND-4-OF-7-SYNTHETIC-ARMS-RECOVERED; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,COUNTS-ARE-COUNTING-ONLY;THE-CAST-IS-DERIVED-AT-THE-CORPUS-AND-AT-NO-SINGLE-HISTORY>
```

Between delivery and adjudication every headline here is a **candidate
reading**.

---

## The short of it

Every unit before this one declared its actors and then watched them write a
record. This one deletes the actors and asks the record to hand them back.

The answer is yes, and the yes is exact. Strip every actor label, every site
label and every direction label from the committed corpus, keep only the cells
each division event wrote, scramble the cell indices, and one rule recovers the
nine actors as specific sets of cells — the same sets, not merely isomorphic
ones. The rule has no free parameter, and the threshold it uses is read off the
record instead of being supplied. From the actors the link
structure follows: each cell turns out to lie in exactly two of them, so a cell
IS an unordered pair of actors, which is the carrier typing the parents
declared. The parent's own carrier row says `27 cells against 27 pairs, two
actors in each cell at all of them, six cells per actor at all nine`, and those
are the numbers that come back out of the bare record.

Three things do not come back, and naming them is the rest of the paper.

The first is the **coordinate**. The record fixes the cast and the links; it
does not fix which actor is called which. There are `1,296` relabellings of the
derived structure onto the declared one, and only `108` of them also carry the
three declared direction classes — an index of `12`. Those `12` are the
resolvable splittings of the derived link structure into direction classes, and
the record names none of them. So **the cast is derived at the corpus and at no
single history**, and the coordinate is not.

The second is the **depth**. No committed history reconstructs the cast, at any
prefix of its own record, ever: `0 of 5,856 committed histories reconstruct the
cast at any prefix of their own record`. Reconstruction is a corpus-level fact,
reached after `17` histories and `145` division events read in the corpus's own
order. And it is tight in the other direction too: `every one of the 27 record
blocks is load-bearing: of the 27 subsets got by dropping one, 0 reconstruct`.
This is the paper's sharpest contrast with its parents. AID's naming time is a
prefix fact about one history and FAC's coherence width is a window fact about
one; both are finite and small. The cast is neither.

The third is the **declaration itself**, and it is the obstruction. The arena
declares three of the four parallel classes as links. A division event both of
whose ends lie in the fourth class writes nothing: `768` such events run in the
corpus, leaving `175` histories partly unwritten and one history — twelve
division events long — written not at all. The record therefore cannot be
injective on histories, and is not: `39` distinct bare records are shared by
more than one history, `180` histories in all. **The direction declaration is
the datum that resists.**

The level-zero arm settles a question the pin's phrase leaves open. The record
*count field* alone carries `36` distinct values over the whole corpus and is
site-constant at every one of them; it names no cast and could not. What
reconstructs is not the counts but **which cells each event wrote** — the
record's own bytes, in the order it wrote them.

---

## 1. The arena, and what "bare" means

The arena is the parents': AG(2, 3) with nine sites, three declared link
directions of the four parallel classes, the 27 cells, paper-21's I7-STRICT
triples and G-FLAT quadruples and driven window, and the three committed
corpora. This instrument enumerates every one of them from its own
constructors; nothing is inherited.

A cell is the unordered co-division pair {*x*, *x* + *l*}. A division event is
a set of three actors. The record of an event is the set of cells both of whose
actors take part in it — for most events three cells, for an event lying along
the undeclared direction none at all. THE BARE RECORD of a history is that
sequence of cell sets, in the order the events ran, with the cell indices
permuted by a declared arena-blind map. Nothing else crosses to the
reconstructor: no actor, no site, no direction, no count.

Two guarantees make that claim checkable rather than asserted. The first is a
recursive type walk of the emitted object: it carries integers and nothing
else. The second is equivariance — relabel the tokens and the derived cast
relabels with them and nothing else moves, at twelve declared relabellings with
none failing. The permutation the strip chose is therefore priced, not trusted.

The bookkeeping the eraser keeps — which token was which cell — is spent in
exactly one place, and it is not the reconstructor. The comparator uses it to
express the declared cast in the reconstructor's own coordinates, so that the
two families can be compared as sets rather than only up to isomorphism.
Nothing the reconstructor computes depends on that choice, and the equivariance
leg is what measures it.

Which is why the object EPR measured is the right frame for this one. Two
structures decide everything, and both are measured: `two sites are unlinked
exactly when they lie on a common line of the one parallel class the arena does
not declare, at 72 of 72 ordered site pairs`. `The graph is therefore complete
multipartite with those three lines as its parts, and every site has degree
six`. The reconstruction below rebuilds exactly that graph, from bytes that
never mention a site.

---

## 2. The reconstruction map

The pin asks for five things, each by an explicit algorithm reading only record
bytes: `the site set, the link structure, the cast size, the partition menu,
the naming`. Each gets its own gate, and each is compared against the declared
arena by code that built neither side.

**The rule.** Two record cells belong to a common actor exactly when one event
wrote them together, or when the cells written with each of them meet in the
largest number any never-co-written pair attains. On these bytes the meet takes
the values 0, 1 and 3 among never-co-written pairs, so the threshold is 3 — a
number the record supplies. An actor is then a maximal set of cells that
pairwise belong to one actor, of the largest size such a set attains; the
maximal sets come in exactly two sizes, and the larger ones are the cast.

| target | algorithm reads | derived | declared | verdict |
|---|---|---|---|---|
| the site set | record blocks | 9 | 9 | EXACT |
| the link structure | record blocks | 27 | 27 | EXACT |
| the cast size | record blocks | 9 | 9 | EXACT |
| the partition menu | record blocks | 3 | 6 | PARTIAL |
| the naming | record blocks | 1,296 | 108 | UP TO THE RESIDUE |

The first three rows are set equality, not isomorphism: the derived actors are
the declared stars of cells, as sets. The fourth row is the honest middle. FAC's
admissible menu has six members — the coset partitions of the translation
subgroups. Three of them come straight out of the record: the one-block
partition, the discrete partition, and the co-class partition of the derived
link structure, which is the undeclared parallel class. The other three ARE the
declared direction classes, and the record does not name them.

The fifth row is the residue, and it is exactly the structure's own symmetry.
`the record admits 1,296 namings of the derived cast and 108 of them carry the
declared direction classes`. The quotient is an integer, and it counts
something: the ways the derived link structure splits into disjoint direction
classes. The record supplies the structure and leaves the splitting open.

---

## 3. The inverse direction

The pin's second measurement runs the map backwards: which properties of a
history do the cast and the grammar alone already fix, which does the record
add, and which does the record lose? The criterion is exact. A property is
ARENA-FORCED when it is constant over the whole corpus; RECORD-CARRIED when it
varies but is constant on every fiber of the map from history to bare record;
NOT-CARRIED when it varies inside some fiber.

| property of the history | verdict | values |
|---|---|---|
| EVENTS-IN-THE-HISTORY | NOT-CARRIED | 3 |
| EVENTS-THAT-WROTE | RECORD-CARRIED | 6 |
| THE-COUNT-FIELD | RECORD-CARRIED | 36 |
| THE-CORPUS-IT-CAME-FROM | NOT-CARRIED | 3 |
| THE-EVENT-SET-ITSELF | NOT-CARRIED | 136 |
| THE-SIZE-OF-A-RECORD-BLOCK | RECORD-CARRIED | 2 |
| THE-CRYSTALLIZATION-TIME | NOT-CARRIED | 5 |
| THE-COLLAPSE-THRESHOLD | RECORD-CARRIED | 3 |
| ACTORS-IN-A-DIVISION-EVENT | ARENA-FORCED | 1 |

The row worth pausing on is the pair at the bottom. FAC's coherence width is a
function of the bare record; AID's crystallization time is not. Two quantities
of the same shape, both defined on the labelled history, and the record keeps
one and drops the other. The reason is the same everywhere in this section: an
event that wrote nothing is not in the record, so anything that counts events,
or reads their order, or asks when a prefix became rigid, can differ between
two histories the record cannot tell apart.

The corpus's own arithmetic says it plainly. The corpus holds 5,856 slots
carrying 5,784 distinct histories and leaves 5,643 distinct bare records; the
141 that vanish are the collisions. So the record's surplus over the arena is
real — four properties it fixes that the cast and the grammar do not — and its
deficit is real too, and the two are the same fact seen from either end.

---

## 4. The minimality census

| depth | object it measures | C1 | C2 | C3 |
|---|---|---|---|---|
| crystallization time | the naming, given the cast | 72 at 5 | 5,184 at 5 | stratified |
| collapse threshold | coherence width, given the cast | 72 at 4 | 5,184 at 4 | 3, 4, 5 |
| reconstruction depth | the cast itself | never | never | never |

Both parent thresholds are re-derived here rather than cited. AID's constant
comes back from the participation signatures — `identity crystallizes exactly
when every actor has its own signature`, and measured that way `the
crystallization time is exactly 5 on C1, C2 and the seed fan`. FAC's width
comes back from an independent transfer computation over the sliding coherence
window, and its values are the parent's: `the collapse thresholds this corpus
carries are 3, 4, 5, and they are WIDTHS in event index, not event counts`.

Against them the reconstruction depth is not merely larger. It is unreached.
The reason is structural and worth stating, because it inverts an intuition. A
history in the first corpus writes each cell exactly once; its nine record
blocks are pairwise disjoint; no pair of blocks meets at all, so the rule has
no meet to threshold and refuses. The most efficient records — the ones that
say each thing once — are precisely the ones that say nothing about who is
saying it. Overlap is what carries identity, and overlap is waste.

Read in the corpus's own order the record reconstructs after 17 histories and
145 division events. At that point it has seen all 27 distinct record blocks,
and that is not an accident of the order: every one of them is needed.
Nothing here is a worst-case bound over arbitrary subsets; it is a census over the committed
corpus, taken at every prefix of every history. Stated once more in the form
the walls police: the cast is derived at the corpus and at no single history.

---

## 5. The obstruction, named

Of everything this unit measured, the direction declaration is the datum that
resists: the choice of three of the four parallel classes, which resists in two
different ways at once.

It resists **downward**, by deleting events. An event whose three actors lie
along the undeclared direction writes no cell. There are 768 such events in the
corpus; 175 histories carry at least one; and one history of twelve division
events writes nothing whatever, so that its entire record is empty while its
history is not. That is the cleanest possible witness that the record is not
the history.

It resists **sideways**, by refusing to name itself. The undeclared class IS
recoverable — it is the co-class partition of the derived link structure, and
it is one of the three menu members the record hands back. What is not
recoverable is which three of the remaining structure were declared. The record
offers 12 splittings and prefers none.

Both of these are consequences of one asymmetry: the record is written by
co-division along declared directions only. It knows exactly which pairs never
count, and it cannot know why the ones that count were chosen.

---

## 6. The control arms

The pin requires both directions through the real reconstructor. Scrambled
records must fail; synthetic minimal records must succeed.

**Scrambled.** 261 corruptions of these bytes were run through the
reconstructor and its comparator: a block replaced by an alien one,
a block dropped, a token exchanged between two blocks. Each was required to
move the object before it counted — a corruption that leaves the record
byte-identical proves nothing. None reached the declared cast.

**Synthetic.** Seven arenas were built from casts that are not this one's, and
their minimal records handed to the same reconstructor.

| parts | tokens | blocks | certificate | cast recovered |
|---|---|---|---|---|
| 2+2+2 | 12 | 8 | CERTIFIED | yes |
| 3+3+3 | 27 | 27 | CERTIFIED | yes |
| 4+4+4 | 48 | 64 | CERTIFIED | yes |
| 5+5+5 | 75 | 125 | CERTIFIED | yes |
| 2+2+2+2 | 24 | 32 | TOKEN-NOT-IN-EXACTLY-TWO | no |
| 3+3 | 9 | 0 | NO-RECORD-BLOCKS | no |
| 2+3+4 | 26 | 24 | TOKEN-IN-NO-ACTOR | no |

The first four are the point: a cast of six, nine, twelve and fifteen actors,
all recovered exactly from a record that mentions none of them, by the same
rule with the same threshold clause. The reconstructor is not tuned to this
arena. The last three are equally the point in the other direction: outside the
balanced three-part family the reconstructor REFUSES rather than answering
wrongly, and the certificate says which leg failed. Across every arm measured
in this unit — the corpus, its prefixes, the scrambles and the synthetics — no
certificate was ever issued for a cast that was not that record's own.

That certificate is what gives the comparator its teeth, and the teeth are
measured, not asserted: three reconstructions carry the reconstructor's own
certificate and are still refused by the comparator, because their casts are
not this arena's.

---

## 7. What this does not say

The reconstruction is at ONE arena and over the committed corpus. Nothing here
is a theorem about records in general, and the synthetic arms are a domain
probe, not a classification.

The counts are counting-only. No measure is declared over histories, so no
fraction in this paper is a probability (E-24).

The parents are used at their own scope and no wider. AID's result is about the
stabilizer of a labelled history; it presupposes the cast, which is exactly
what this unit derives, so it cannot be read as having derived it.
`record-completeness is analytic at EPR's own catalogue` — EPR's
record-completeness holds by construction over the elements EPR censuses, at
that arena, and this unit inherits no completeness claim from it. FAC's LEG-2
theorem is about partitions of a declared cast.

The residue is a coordinate residue and is described as one. The claim is not
that direction labels are meaningless; it is that the record does not carry
them. A different corpus — one that used the parallel classes in a way this one
does not — might carry more, and this unit does not test that.

Finally, the refusal of every single history is a fact about THIS corpus's
histories, whose records are short. It is not a proof that no history could
ever suffice; the synthetic 2+2+2 arm shows an eight-block record
reconstructing a six-actor cast, so shortness alone is not the obstruction —
disjointness is.

---

## 8. The instrument

`v14/code/rec_exact.py`. The three regions — builder, reconstructor,
comparator — are disjoint by machine check: an AST scan requires that no
reconstructor function name an arena constant or call a builder or comparator
function, and that no comparator function call a builder or a reconstructor.
That is this corpus's registered S-1 family, answered here with a mechanism
rather than a promise.

The three parent receipts are read at their pinned digests and consumed, not
merely digested: 24 quantities this instrument re-derives from its own
constructors are compared against the parents' delivered values, one by one.

The verdict is not trusted to its renderer: each declared head field is parsed
back out of the emitted string and compared, as an integer, against the receipt
leaf it names — a parser against a builder, sharing no code and no literal.

The nine template families are imported from `v14/code/era_template.py` and
used rather than copied: gate-time seals verified at the door with totality
recomputed there, the transcript reconciled with the ledger by content, walls
that scan the paper as patterns with standing sentences they require, verbatim
anchors that are consumed by predicates rather than merely located, claims and
tables and fences by two-way equality keyed by table, referent binding per
occurrence over prose, no typed numeral in anything the unit vouches for,
falsifiers that must move the measured key they name and die at the gate they
name, and the read set recorded at an open audit hook.

The paper's tables and fenced blocks are rendered by the instrument and matched
against these bytes; the referent scan runs on prose with rendered tables
removed, since those are bound more tightly, row by row and keyed by table,
than a referent registry could bind them.
