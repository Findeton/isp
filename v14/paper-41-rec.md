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
REC-RECONSTRUCTION<CORPUS=5,856; DISTINCT-HISTORIES=5,784; RECORD-BLOCKS=27; SITE-SET=9-OF-9-EXACT; LINK-STRUCTURE=27-OF-27-EXACT; CAST-SIZE=9-DERIVED; MENU=3-OF-6-PARTIAL; NAMING=1,296-ADMISSIBLE-108-ARENA-COHERENT; RESIDUE-INDEX=12; LEVEL-0-COUNT-FIELD=36-DISTINCT-CAST-NOT-DERIVABLE>
```

```
REC-MINIMALITY<PER-HISTORY=0-OF-5,856-AT-EVERY-PREFIX; CORPUS-ORDER=17-HISTORIES-145-EVENTS; BLOCK-MINIMAL=27-OF-27-DROP-ONE-SURVIVORS-0; COLLAPSE-THRESHOLDS=3-AND-4-AND-5; CRYSTALLIZATION-ON-C1-AND-C2=5; NEVER-CRYSTALLIZING=4>
```

```
REC-CAST-DERIVED-UP-TO-THE-DIRECTION-DECLARATION<OBSTRUCTION=THE-DIRECTION-DECLARATION; UNWRITTEN-EVENTS=768; PARTLY-UNWRITTEN-HISTORIES=175; HISTORIES-WRITING-NOTHING=1; RECORD-COLLISIONS=39-CLASSES-180-HISTORIES; SURPLUS=1-ARENA-FORCED-4-RECORD-CARRIED-4-NOT-CARRIED; CONTROLS=261-SCRAMBLES-0-SURVIVE-AND-4-OF-7-SYNTHETIC-ARMS-RECOVERED; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,COUNTS-ARE-COUNTING-ONLY;THE-CAST-IS-DERIVED-AT-THE-CORPUS-AND-AT-NO-SINGLE-HISTORY>
```

Between delivery and adjudication every headline here is a **candidate
reading**.

---

## The short of it

Every unit before this one declared its actors and then watched them write a
record. This one deletes the actors and asks the record to hand them back.

The answer is yes at the corpus, and the yes is exact. Strip every actor label
and every site label from the committed corpus, keep only the cells each
division event wrote, move the cell indices by a declared coordinate, and one
rule recovers the nine actors as specific sets of cells — the same sets, not
merely isomorphic ones. The rule has no free parameter, and the threshold it
uses is read off the record instead of being supplied. From the actors the link
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
one; both are finite and small wherever they are defined. AID's is undefined at
`4` of the `5,856` committed histories. The cast is neither.

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
record's own bytes, as a family of blocks.

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
sequence of cell sets, in the order the events ran, with the cell indices moved
by a declared map, *k* ↦ 5*k* + 11 mod 27.

No actor and no site crosses to the reconstructor, and the emitted object's
shape proves it: a recursive type walk finds three levels — histories, events,
token ids — with integers at the bottom, over an alphabet of exactly 27 ids,
and a site is a PAIR of integers, so a strip that handed over actor triples
instead of the cells they wrote would be caught by the depth rather than by the
leaf type.

One arena datum does cross, and naming it is part of the disclosure. The cells
are enumerated site-major and link-minor, so a cell's index modulo three is its
declared direction; the strip's map is affine and every affine map fixes that
residue, so the three declared direction classes remain readable off the
emitted ids as the residue classes themselves. **The eraser is not arena-blind
as declared, and the reconstruction is arena-blind as measured.** The
reconstructor never reads the channel: it does no arithmetic on token ids at
all, only set membership, set meets and maximal cliques. And the price of the
coordinate is measured rather than argued — every one of `12` quantities this
unit publishes about the reconstruction is unchanged at `60` uniformly random
coordinates, at `0` of which the channel is present at all, and the derived
cast relabels and moves nothing else at `300` further random relabellings, `0`
failing. The `12` declared relabelling trials cannot price this channel: the
direction is a function of the residue at `12` of `12` of them, because every
one of them is affine, and that is exactly why the random census is the leg
that prices it.

The bookkeeping the eraser keeps — which token was which cell — is spent on the
declared side only: on the declared cast, and on the declared direction classes
the coherence count is taken against. Nothing the reconstructor computes
depends on that choice, and the random-coordinate census is what measures it.

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
largest number any never-co-written pair attains; where the never-co-written
pairs attain fewer than two distinct values there is no such largest number and
the rule REFUSES rather than choosing one. On these bytes the meet takes the
values 0, 1 and 3 among never-co-written pairs, so the threshold is 3 — a
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
classes. And the index IS that count rather than merely equalling it. The
declared splitting is itself one of the splittings the record admits, and the
`1,296` namings carry it onto `12` of them — which is all of them. The action
is transitive, so the orbit of the declared splitting has the size of the index
by the orbit-stabilizer count, and the record supplies the structure and leaves
the splitting open.

---

## 3. The inverse direction

The pin's second measurement runs the map backwards: which properties of a
history do the cast and the grammar alone already fix, which does the record
add, and which does the record lose? The criterion is exact. A property is
ARENA-FORCED when it is constant over the whole corpus; RECORD-CARRIED when it
varies but is constant on every fiber of the map from history to bare record;
NOT-CARRIED when it varies inside some fiber.

| property of the history | verdict | distinct values |
|---|---|---|
| EVENTS-IN-THE-HISTORY | NOT-CARRIED | 3 |
| EVENTS-THAT-WROTE | RECORD-CARRIED | 6 |
| THE-COUNT-FIELD | RECORD-CARRIED | 36 |
| THE-CORPUS-IT-CAME-FROM | NOT-CARRIED | 3 |
| THE-EVENT-MULTISET | NOT-CARRIED | 136 |
| THE-SIZE-OF-A-RECORD-BLOCK | RECORD-CARRIED | 2 |
| THE-CRYSTALLIZATION-TIME | NOT-CARRIED | 5 |
| THE-COLLAPSE-THRESHOLD | RECORD-CARRIED | 3 |
| ACTORS-IN-A-DIVISION-EVENT | ARENA-FORCED | 1 |

The fifth row measures the sorted MULTISET of a history's division events, and
it is named as one, because events repeat: the concatenation corpus runs each
of its factors twice over and the class quadruples repeat their classes. Read
instead as the SET of the events, the same property takes `103` values over the
same corpus. The verdict is invariant under the choice — the record splits `6`
fibers either way — and both numbers are in the receipt beside each other.

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
| crystallization time | the naming, given the cast | 72 at 5 | 5,184 at 5 | 5:404, 7:36, 8:144, 11:12, never:4 |
| collapse threshold | coherence width, given the cast | 72 at 4 | 5,184 at 4 | 3, 4, 5 |
| reconstruction depth | the cast itself | never | never | never |

Both parent thresholds are re-derived here rather than cited. AID's constant
comes back from the participation signatures — `identity crystallizes exactly
when every actor has its own signature` — and measured that way AID's own
statement, `the crystallization time is exactly 5 on C1, C2 and the seed fan`,
is re-derived here at the two corpora this unit holds; the seed fan is AID's
and is not separable inside this corpus, so the third conjunct is quoted and
not re-measured. FAC's width comes back from an independent transfer
computation over the sliding coherence window, and its values are the parent's:
`the collapse thresholds this corpus carries are 3, 4, 5, and they are WIDTHS
in event index, not event counts`.

The two declared-side depths carry exactly one relation to each other, and this
corpus makes it a biconditional: a history never crystallizes exactly when its
collapse threshold is the least width the corpus carries. Measured in both
directions, `4` histories never crystallize, `4` sit at that width, and the two
sets are the same `4`.

Against them the reconstruction depth is not merely larger. It is unreached,
and the reason is a counting fact rather than a census: every one of the `27`
record blocks is load-bearing — dropping any one leaves `0` reconstructing, and
so does dropping any two of them, `0` of the `351` such subsets — while **no
committed history sees more than 18 of the 27 record blocks**. No history
carries enough of them. Disjointness is the mechanism at the first corpus,
where a history writes each cell exactly once and its nine record blocks are
pairwise disjoint, so the rule has no meet to threshold and refuses. That
mechanism accounts for `839` of the `5,856` histories, and the most efficient
records — the ones that say each thing once — are precisely the ones that say
nothing about who is saying it. Overlap is what carries identity, and overlap
is waste. But that is the minority mechanism: the modal refusal, at `4,104` of
the `5,856` histories, is a want of record rather than a want of overlap. The
certificate that fires there is the one that finds a token in no derived actor
at all.

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
reconstructor: a block replaced by an alien one, a block dropped, a token
exchanged between two blocks. None reached the declared cast, and — better than
refusal at the comparator — none was ever certified by the reconstructor at
all, so `0` of the `261` scrambles reached the comparator.

Three disclosures belong with that number, because none of them is visible in
it. The alien family is a declared two-member one: each block is replaced by
its two token-index translates, not by an arbitrary alien block. The swap arm
carries a declared cap — a pair of blocks is corrupted only when the lower of
the two indices is at most `8` — under which `180` of the `315` moving swaps
available are run and `135` are dropped; `279` corruptions were built in all,
of which `18` were rejected as non-moving before any of them counted. And the
total is a function of the declared coordinate: recomputed at `10` declared
coordinates this control arm holds between `254` and `261` corruptions, so
`261` is this coordinate's denominator and not a property of the arena.

**Synthetic.** Seven arenas were built from casts that are not this one's, and
their minimal records handed to the same reconstructor.

| parts | tokens | blocks | threshold | certificate | derived cast | cast recovered |
|---|---|---|---|---|---|---|
| 2+2+2 | 12 | 8 | 2 | CERTIFIED | 6 | yes |
| 3+3+3 | 27 | 27 | 3 | CERTIFIED | 9 | yes |
| 4+4+4 | 48 | 64 | 4 | CERTIFIED | 12 | yes |
| 5+5+5 | 75 | 125 | 5 | CERTIFIED | 15 | yes |
| 2+2+2+2 | 24 | 32 | 4 | TOKEN-NOT-IN-EXACTLY-TWO | 24 | no |
| 3+3 | 9 | 0 | none | NO-RECORD-BLOCKS | 0 | no |
| 2+3+4 | 26 | 24 | 4 | TOKEN-IN-NO-ACTOR | 8 | no |

The first four are the point: a cast of six, nine, twelve and fifteen actors,
all recovered exactly from a record that mentions none of them, by the same
rule with the same threshold clause. And the threshold column is the cleanest
evidence that the number is read and not typed: the same clause returns a
different threshold on each of those arms, tracking the part size, and returns
one on two arms where the structure it then builds is wrong and is caught. The
last three rows are equally the point in the other direction: the reconstructor
REFUSES rather than answering wrongly, and the certificate says which leg
failed.

**Where the boundary actually is.** The three-part family is not it. Every
complete multipartite shape up to `16` actors was run through the same arm —
`125` of them — and the ones that come back are exactly the `9` balanced
shapes; `0` unbalanced shapes recover, and `0` arms anywhere in the sweep were
certified for a cast that was not that record's own. So what the arms locate is
balance and not the number of parts, and it is not monotone in the number of
parts either: the `4`-part arm 2+2+2+2 breaks where the `5`-part and `6`-part
arms of the same part size do not, and the `2`-part arms write no event of
three tokens at all.

| parts | balanced | blocks | certificate | cast recovered |
|---|---|---|---|---|
| 2+2 | yes | 0 | NO-RECORD-BLOCKS | no |
| 2+2+2+2 | yes | 32 | TOKEN-NOT-IN-EXACTLY-TWO | no |
| 2+2+2+2+2 | yes | 80 | CERTIFIED | yes |
| 2+2+2+2+2+2 | yes | 160 | CERTIFIED | yes |
| 3+3 | yes | 0 | NO-RECORD-BLOCKS | no |
| 3+3+3+3 | yes | 108 | CERTIFIED | yes |
| 3+3+3+3+3 | yes | 270 | CERTIFIED | yes |
| 4+4 | yes | 0 | NO-RECORD-BLOCKS | no |
| 4+4+4+4 | yes | 256 | CERTIFIED | yes |
| 5+5 | yes | 0 | NO-RECORD-BLOCKS | no |
| 6+6 | yes | 0 | NO-RECORD-BLOCKS | no |

**The comparator's own teeth**, which are a different thing from the
reconstructor's refusals and are measured by running it rather than inferred
from a size. All `4` synthetic reconstructions that carry the reconstructor's
own certificate are refused against this arena's declared cast, and `1` of them
— the 3+3+3 arm — carries a cast of exactly nine, so that refusal is not a
matter of size. Everywhere else the reconstructor refuses first: `0` scrambled
records and `0` per-history attempts ever reach the comparator at all. That is
the honest shape of the result. The refusals this unit reports in the census
are the reconstructor's own; the comparator's teeth are shown on four arms and
no more.

---

## 7. What this does not say

The reconstruction is at ONE arena and over the committed corpus. Nothing here
is a theorem about records in general, and the synthetic arms are a domain
probe, not a classification.

The counts are counting-only. No measure is declared over histories, so no
fraction in this paper is a probability (E-24).

The parents are used at their own scope and no wider. AID's result is about the
stabilizer of a labelled history; it presupposes the cast, which is exactly
what this unit derives, so it cannot be read as having derived it. AID also
records that the link declaration moves no census number of its own; that is
compatible with this unit's finding and sharper here only because the object is
different — AID censuses the stabilizers of a labelled history, and this unit
censuses what the record carries. On EPR: record-completeness is analytic at
EPR's own catalogue — that sentence is this paper's summary and not a
quotation, and it means that EPR's completeness holds by construction over the
elements EPR censuses, at that arena, so this unit inherits no completeness
claim from it. FAC's LEG-2 theorem is about partitions of a declared cast.

The residue is a coordinate residue and is described as one. The claim is not
that direction labels are meaningless; it is that the record does not carry
them. A different corpus — one that used the parallel classes in a way this one
does not — might carry more, and this unit does not test that.

Finally, the refusal of every single history is a fact about THIS corpus's
histories, whose records are short. It is not a proof that no history could
ever suffice; the synthetic 2+2+2 arm shows an eight-block record
reconstructing a six-actor cast, so shortness alone is not the obstruction. The
obstruction at this corpus is that no single history writes enough of the
record: the block set is irredundant one block down and two blocks down alike,
and no history writes more than `18` of the `27` record blocks.

---

## 8. The instrument

`v14/code/rec_exact.py`. The region map is TOTAL by machine check: every
top-level function is a builder, a stripper, a reconstructor, a comparator or
plumbing — the orchestrator is named as plumbing rather than left out of the
census — and an AST scan requires that no reconstructor or comparator function
name any declared-side constant, type any arena cardinality above 3, or REACH
a builder, a stripper or the orchestrator at any depth, through a module-level
alias or through a helper. The declared-side names are derived from the module
rather than typed into a list. That is this corpus's registered S-1 family,
answered here with a mechanism rather than a promise — and the mechanism is
credited where it belongs: the erasure's blindness is carried by the type walk,
the random-coordinate census and the control arms, not by the AST scan, which
polices code and not data.

The three parent receipts are read at their pinned digests and consumed, not
merely digested: 24 quantities this instrument re-derives from its own
constructors are compared against the parents' delivered values, one by one.

The verdict is not trusted to its renderer: every numeral position in the three
head segments is parsed back out of the emitted string and compared, as an
integer, against the receipt leaf it names — a parser against a builder,
sharing no code and no literal.

Two of the pin's four pre-registered outcomes are refusals when the object is
this corpus: the gates that decide them raise, and a raised gate writes no
artifact. Rather than leave them as values of a function no run could print,
the instrument WRITES each of them, through the real reconstructor, the real
certificate and the real comparator, at declared faults.

| declared fault | faulted side | certificate | word the machinery writes |
|---|---|---|---|
| none: this corpus's own record against its own declared arena | NEITHER | CERTIFIED | REC-CAST-DERIVED-UP-TO-THE-DIRECTION-DECLARATION |
| a synthetic arena's own record, read against its own cast, which declares no direction and so owes no residue | RECORD | CERTIFIED | REC-CAST-DERIVED |
| a synthetic arena whose record leaves a token in no actor | RECORD | TOKEN-IN-NO-ACTOR | REC-BLOCKED-AT-THE-CAST |
| this corpus's record, read against a cast short of one actor | RECORD | CERTIFIED | REC-BLOCKED-AT-THE-CAST |
| this corpus's record, read against a declared link structure missing one pair | DECLARED | CERTIFIED | REC-OBSTRUCTED-AT-THE-LINK-STRUCTURE |

The last row's fault is on the declared side, and it has to be. At this arena
the declared pairs are a function of the declared stars, so a cast that is
set-equal cannot carry a link structure that is not: the OBSTRUCTED word is
unreachable from any record whatever, and only a mis-declared link structure
can write it. That is a measured fact about this arena, published as one. The
clean gate sheet is therefore not by itself evidence for the verdict; the
evidence is the set equality of section 2, the residue index of its last row,
and the controls.

The nine template families are imported from `v14/code/era_template.py` and
used rather than copied — each family's check id is read off the template's own
table and matched to a live call in this module, and that match is gated.

What they buy here. Gate-time seals verified at the door with totality
recomputed there. The transcript reconciled with the ledger by content, and
every integer in every finished evidence line bound to the sealed keys of the
gate that wrote it, so the two artifacts cannot be promoted contradicting each
other. Walls whose patterns are written from the finding rather than from a
phrase list, so that natural re-voicings die alongside the literal forms, with
standing sentences the paper must carry. Verbatim anchors consumed by
predicates rather than merely located. Claims and tables and fenced blocks by
two-way equality keyed by table, the load-bearing direction sentences among
them, so that reversing one is a delivery failure rather than an invisible
edit. Referent binding per occurrence over prose. No typed numeral anywhere in
the subtree of a statement, claim, table or fence builder, so that neither a
concatenated fragment nor a hand-typed table column escapes. Every numeral in
the paper, and every quantity it spells out in words, backed by an integer
measurement or by a declared exemption whose token the paper actually carries.
Falsifiers that must move the measured key they name — the payload as it stood
at refusal is what the move is measured against — and die at the gate they
name, with every recipe matched to an implementation and every implementation
to a recipe by AST, no hook that merely appends a constant to the finding list
its gate reads, and no waiver at all. And the read set recorded at an open
audit hook and reconciled twice, the second time after the last gate of all.

The paper's tables and fenced blocks are rendered by the instrument and matched
against these bytes; the referent scan runs on prose with rendered tables
removed, since those are bound more tightly, row by row and keyed by table,
than a referent registry could bind them.
