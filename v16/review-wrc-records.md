# WRC Paper 8 hostile review — Seat R: histories, records, covariance, and eliminability

Status: **FROZEN INDEPENDENT HOSTILE REPORT**.  I did not read, request,
summarize, or infer either other WRC report.  I reviewed the immutable WRC
target bound by `v16/note-wrc-hostile-protocol.md`, rebuilt the relevant
walk and DISC calculations without importing WRC or DISC modules, and made no
candidate, board, log, protocol, or git change.

Immutable target: candidate `e5fb6047a84805b5bd260d969099bb229e369441`,
replay repair `3f75079a970b32f95b1740c4bb07bc2bd9fd79f8`, and
verification `7aa47427a269bc774412ba1fdc26953190e1b093`.

## Verdict

**Grade: ACCEPT-WITH-FIXES.**

The frozen primary survives at its explicitly mathematical, fixed-carrier
meaning:

```text
WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT
```

WRC exactly reconstructs the source's 27-cell transport, declared cuts,
registered screens, and the stipulated map from CELL-HIT label histories to a
count-field readout.  It does **not** reconstruct grammar-generated histories,
actualized beables, a permanence theorem, a recurring event type, carrier
growth, or relational-geometry irreducibility.  The paper already refuses most
of those stronger readings.  Two emitted qualifiers nevertheless say more than
the assays establish: `CELL-HIT-BEABLE-DICTIONARY-RECONSTRUCTED` needs an
explicit “candidate/readout only” qualification, and
`RECURRING-VERTEX-COUPLINGS-EXTRACTED-NOT-SELECTED` must be replaced by the
measured statement about repeated numeric record signatures under one imported
rule.  The abstract's “creation-layer representation” is also conditional on
an unadjudicated Papers 3--7 interface and should be retyped as a fixed-carrier
successor-packet representation.

The eliminability result is negative but useful.  WRC's one finite carrier
cannot distinguish relational geometry from a finite memory register with a
hard-coded transition circuit.  DISC independently excludes its registered
memoryless classes—10,380 configurations, 353 distinct third-tick laws, zero
exact matches—but explicitly tests no memory-bearing null.  Thus DISC proves a
class-relative need for memory/record feedback, not a need for dynamic
geometry.  WRC correctly avoids claiming otherwise.

## 1. Exact independent rebuild

I rebuilt the arithmetic over `Q(w)`, `w^2+w+1=0`, the nine sites, three
directions, Grover coin, record phase, and plus shift directly from the frozen
fixture.  No WRC or DISC executable was imported.  The checks below use exact
fractions and exact pairs `a+bw`; none is a receipt gate cited as proof.

### 1.1 CELL-HIT is one pair-cell alternative, not a grammar event

The catalogue contains nine sites, three local direction labels, and 27 cells.
Mapping `(x,l)` to the unordered pair `{x,x+l}` gives 27 distinct unordered
actor pairs, each containing exactly two actors.  At the declared post-coin
cut, CELL-HIT `c` is one of those mutually exclusive cell labels, with Born
weight `|psi_postcoin(c)|^2`, and its only record action is

```text
n -> n + e_c.
```

The four nearby objects must remain separate:

| object | present in WRC? | exact status |
|---|---:|---|
| one selected pair-cell CELL-HIT | yes | one Born alternative; one count increment |
| one three-actor grammar event writing three pair-cells simultaneously | no | outside the source packet |
| a genuine division boundary | no | the cut is an algorithmic walk cut |
| a durable/actual record fact | not proved | a count is stored and monotonically incremented by this rule; no actualization or all-future recoverability theorem |

This agrees with the homonym registry rather than merely with WRC's label:
grammar histories contain three-actor division events, while Paper 20/DISC
histories contain CELL-HIT emissions.  A shared count register does not identify
the writers.

### 1.2 The two-tick “beable” census is a count identity

Starting from the committed basis state and uniform count-one record, exact
enumeration gives branch counts `3, 27` at ticks one and two.  All 27 two-tick
label sequences satisfy

```text
n_2 = n_0 + histogram(c_1,c_2)
```

with zero violations.  This is a useful implementation check, but it follows
from applying `+e_c` after every enumerated label; it is not a record theorem.
The stronger independent census gives:

| quantity | tick 1 | tick 2 | tick 3 |
|---|---:|---:|---:|
| labelled emission histories | 3 | 27 | 486 |
| distinct stored count records | 3 | 27 | 477 |
| distinct process-state vectors | 1 | 1 | 3 |

For every outcome of a given parent at a step, the output process state is
identical; only the CELL-HIT label and count record differ.  At the declared
two-tick assay all 27 histories still share one process state.  The labels are
not forever inert: the differing records feed later phases, and by tick three
three process states occur.  But the object is an **emission-history ensemble
with record memory**, not a grammar history and not an outcome-selected
physical world.  At tick three nine labelled sequences have already merged in
the histogram readout (`486` histories versus `477` records), illustrating the
pin's own warning that the record map forgets order.

Accordingly, `beable=true` survives only under the pin's frozen operational
definition—“complete labelled CELL-HIT history to count field plus current
readout.”  It does not license the ordinary ontological claims “one history
actualizes” or “this record remains recoverable under every licensed future.”
The update is append-only within the imported walk rule, but WRC supplies no
closed continuation catalogue against which absolute permanence could be
tested.

### 1.3 Translation covariance is stronger than the delivered two rows

Let `T_a` translate every site while preserving the local link label.  Directly
from the reconstructed formulas,

```text
T_a C_n = C_(T_a n) T_a,
T_a S = S T_a,
```

because the same local coin is used at every site, the phase is a cellwise
function of the translated count, and the shift is `x -> x+l`.  Therefore
`T_a U_n = U_(T_a n) T_a`, and the CELL-HIT probabilities permute by the same
cell action.  This is an all-state identity on this fixed `Z_3^2` arena, not an
all-arena naturality theorem.

As a hostile control I tested all nine translations on three different exact
state/nonuniform-record preparations: 27 of 27 joint state-and-record rows
pass, including 24 of 24 nonidentity rows.  The absolute origin is retained at
0 of 8 nonidentity translations.  Moving the state while freezing the
nonuniform record fails at 17 of 27 rows (only 7 of 24 nonidentity rows pass by
accidental symmetry).  Thus the paper's qualitative statement is correct:
state, record, labels, and observables must transform together.  The paper
should add the displayed intertwining identity or the complete group control;
the two registered examples alone did not warrant a general-sounding
qualifier, although the underlying theorem does.

### 1.4 The recurrence census is not event-type recurrence

Rebuilding the first three recurrence layers gives exactly four local residue
signatures:

| local residue signature | distinct sites carrying it | token occurrences |
|---|---:|---:|
| `(1,1,1)` | 9 | 222 |
| `(2,1,1)` | 4 | 19 |
| `(1,2,1)` | 4 | 19 |
| `(1,1,2)` | 4 | 19 |

All four therefore repeat across distinct site names.  Equal signatures have
equal local matrices because WRC hard-codes one local function—Grover after the
three record phases—and calls it at every site.  This establishes repeated
numeric inputs to one declared uniform rule.  It does not identify a grammar
event token, derive a recurring event type, compare token-disjoint contexts,
or derive universality of `-1/3` and `2/3`.  Indeed the admitted alternate coin
moves the registered short IPR, which correctly proves nonselection.

The honest qualifier is approximately

```text
REPEATED-LOCAL-RECORD-SIGNATURES-UNDER-ONE-IMPORTED-RULE;
COIN-COUPLINGS-MEASURED-NOT-SELECTED
```

not `RECURRING-VERTEX-COUPLINGS-EXTRACTED-NOT-SELECTED`.  This is a qualifier
repair, not a change to the six-coordinate primary.

## 2. What Paper 20 histories actually are

Paper 20 evolves `(psi,n)` on one fixed 27-cell catalogue.  At each step it
computes the post-coin CELL-HIT menu, carries every nonzero label as an
ensemble branch, leaves the same shifted `psi` on all children of that parent,
and increments one count.  The count changes the next local phase, but no cell
is created or removed, no adjacency is rewritten, and no output graph is fed
to a later probe.  WRC accurately reports support size 81 on the same fixed
27-dimensional carrier.

The exact first separation from the record-free frozen-stage walk occurs as
follows in my rebuild:

| tick | coupled versus memoryless site law | total variation |
|---:|---|---:|
| 1 | equal | `0` |
| 2 | equal | `0` |
| 3 | different | `1024/19683` |

This is record-fed transport and genuine feedback in the limited engineering
sense: prior label memory affects later process statistics.  It is not yet the
joint dynamic-geometry successor type

```text
(relations, geometry, process state)
  -> (new relations, new geometry, new process state).
```

The correct corpus statement is **not instantiated**, not **refuted**.  The
source walk avoids the Papers 3--7 graph-eliminability problem by never changing
the graph; it does not solve that problem.

## 3. DISC rebuilt at its exact scope

The DISC receipt and source define two memoryless null classes: every raw
`S_3`-covariant coin solution at every start/direction, and every integral
orthogonal numerator matrix `M M^T=9I` in the registered box with covariance
dropped.  I independently enumerated the coins and ran their exact three-tick
site laws against the two frozen ISP targets:

| arena | class | coins | configurations | distinct tick-3 laws | exact matches | closest max-site gap |
|---|---|---:|---:|---:|---:|---:|
| `AG(2,2)` | covariant | 4 | 48 | 16 | 0 | `10144/59049` |
| `AG(2,2)` | integral | 240 | 2880 | 76 | 0 | `8200/59049` |
| `AG(2,3)` | covariant | 36 | 972 | 90 | 0 | `1024/19683` |
| `AG(2,3)` | integral | 240 | 6480 | 171 | 0 | `1024/19683` |

The totals are exactly 10,380 configurations, 353 distinct laws, and zero
exact reproductions.  The integral census itself has 30 norm-nine rows and
240 orthogonal matrices.  Independently, the coupled/null comparison agrees at
6,216 of 6,216 registered site-by-tick checks through tick two and first differs
at tick three at all 294 nontrivial fiber points, never at the 78 trivial
points.  The null is Paper 20's frozen-stage control up to global phase at
1,116 of 1,116 checks.

DISC's other primary accounting is also exact: six of nine parent results are
reproduced, seven of ten tested rows are reproduced, two are not reproduced,
and one record-only row is not expressible.  That result weakens, rather than
strengthens, any attempt to infer a distinctive ontology from a finite walk.

What DISC excludes is precise: the registered **memoryless** fixed-coin
classes.  Its null function takes no time, record, or memory argument, and the
paper explicitly says “NO-MEMORY-BEARING-NULL-TESTED-AT-ALL.”  At finite
horizon the coupled rule can be compiled into a larger state.  On the WRC
three-tick fixture, for example, a finite controller can retain one of the 477
reachable record states (or simply the 27 count residues) and choose the next
hard-coded local phase.  Calling that controller's memory “geometry” or
“internal state” changes no screen.  DISC therefore demonstrates that
memory/record feedback is operationally non-inert relative to the swept
memoryless classes; it does not establish that the memory is relational
geometry.

## 4. The weakest honest family-level eliminability game

Absolute non-eliminability on a finite table is vacuous: unrestricted lookup
always wins.  The opposite slogan—“finite exact tests can never establish
anything”—is also false.  A finite held-out test can exclude a predeclared
bounded class.  The minimum honest game is the following.

### 4.1 Frozen game tuple

Before construction, freeze

```text
Game = (F, Train, Holdout, I, tau, Blind, B, Gamma, Metric, epsilon).
```

- `F` is a family of relational carriers/graphs with typed boundary data, not
  several names for one graph.
- `Train` and `Holdout` are disjoint graph isomorphism classes and preparation
  sets; held-out members remain hidden until both model classes freeze.
- `I` is a counterfactual intervention set.  It must include geometry-only
  pairs with calibrated-equal process state and record, record-only changes at
  fixed geometry, relabelings, and at least one rewrite followed by a probe
  computed from the output geometry.
- `tau` is one program and one parameter dictionary used on every family
  member.  Per-graph retuning is forbidden.
- `Blind` specifies exactly what an adversary receives.  A geometry-blind
  model receives neither adjacency, graph identity, graph-derived features,
  nor raw labels that secretly encode those data.  Relabeling equivariance is
  mandatory.
- `B` fixes locality radius, process-state dimension, memory dimension,
  parameter count, description length, circuit depth, allowed ancilla/ports,
  and numerical precision.  Candidate and adversary receive resource parity
  except for the tested graph input.
- `Gamma` is the allowed calibration/relabeling/gauge group.
- `Metric` compares the complete registered outcome distribution/instrument
  after optimizing only over `Gamma`; `epsilon=0` is available in exact finite
  fixtures, otherwise tolerance and sampling protocol are frozen.

Class-relative relational load bearing is earned only if one uniform `tau`
passes every training and held-out intervention, every adversary in the frozen
bounded class fails at least one held-out row, positive controls show the class
is nonempty and capable on easier rows, and the separating row is invariant
under `Gamma`.  The conclusion is exactly “this adversary class is excluded,”
not “geometry is ontologically fundamental.”

### 4.2 Three adversary nests

| nest | inputs and resources | present status | what exclusion would mean | what it would not mean |
|---|---|---|---|---|
| `A0` memoryless walk | current process state, fixed coin/shift, no record or graph-dependent memory | DISC excludes the two registered classes at tick three | those memoryless parametrizations cannot reproduce the feedback screen | record ontology, geometry, or all memoryless quantum processes are impossible |
| `A1` bounded record-bearing, graph-blind | process state plus prebounded equivariant memory; no adjacency, graph ID, or graph-derived labels; one rule across held-outs | untested; on one fixed carrier WRC is exactly reproducible by storing its count/residue memory | a matched graph intervention contains predictive information unavailable to generic bounded memory | unrestricted memory is impossible, or geometry is ontically unique |
| `A2` graph-labelled lookup/compiled circuit | graph ID/labels or per-graph circuit and enough ancilla | unrestricted version always reproduces a finite fixture | excluding a **budgeted** version shows a compression/generalization advantage for the uniform graph rule | ontology; a larger lookup still exists |

The fixed-carrier WRC arena cannot fairly distinguish `A1` from `A2`: any
constant shift/adjacency table may encode the only graph even when no graph is
an explicit input.  That is why a family, held-out graph interventions, raw-name
blindness, and a description-length budget are load-bearing rather than
decorative.

### 4.3 The decisive observation still missing

The clean separating experiment is an input collision for the blind class.
Construct two calibrated cases `(G,R,S)` and `(G#,R,S)` with identical blind
input but a changed relational adjacency/rewrite.  If one uniform graph-fed
rule predicts different later distributions and held-out data confirm them,
every adversary that only sees the common blind input must predict the same row
twice and is excluded.  To earn **dynamic** geometry rather than static graph
dependence, the same successor law must also create `G'` in response to the
process and a later probe must depend on `G'`, with erasure/reconstruction
controls showing that the graph—not a duplicated flag—carries the effect.

Neither WRC nor DISC contains that object.  Generic memory, a finite automaton,
and an enlarged Markov state remain viable at the current scope.  Whether they
can reproduce one uniform future family under the frozen budgets is open.

## 5. Shared methodological seam with Papers 3--7

WRC does not repair their graph-eliminability defect.  Its fixed support means
there is no graph rewrite to eliminate.  The exact mathematics of a record
rewrite plus process transport is self-contained, but the claim that this is a
“creation-layer representation” imports a candidate interface from frozen but
unadjudicated Papers 3--7.  Under the protocol's dependency rule, that phrase
must be conditional.  Retype the independent result as a **fixed-carrier
record/process successor bundle**; if the creation-layer interface later
survives adjudication, the representation can be reattached without changing a
number.

This distinction also prevents an invalid negative inference.  WRC's failure
to instantiate changing geometry does not refute the proposed joint-law type.
It says only that the committed v14 walk is not yet such an instance.

## 6. Primary word, Q8, and full-packet scope

The primary word is forced by the frozen coordinate convention once “beable
map” retains the pin's operational meaning.  Reopening Q8 does not move the
referent, transport, cuts, observable, instrument, or readout-map facts, so the
primary survives.  Q8 retirement is bookkeeping, not evidence.

If “full packet” is read as requiring a complete affine outcome instrument,
the terminal answer is **no**: WRC's exact residue is the CELL-HIT instrument.
The paper does state this.  It must not let “Q8 retired” or “full-packet
comparator” be paraphrased as full equivalence.  If an adjudicator instead
requires “beable” to mean an actual fact at a genuine division boundary, then
`beable=true` is false at this scope and the primary must change to the frozen
instrument-and-record-map residue word.  My acceptance keeps the pin's explicit
operational definition and orders the nomenclature repair so that this
conditional is visible.

## 7. Shared procedural audit

### 7.1 Was the generic core answer-blind?

Yes with an important qualification.  The frozen core contains generic exact
matrix, instrument, histogram, covariance, and sealing machinery and no WRC
arena, 27-cell data, Grover declaration, committed observables, comparator
table, result word, or Paper 8 result prose.  It is **physical-answer blind**,
not topic blind: its public calibration already includes a generic nonaffinity
example, a projective instrument, and the `9/25,16/25` control.  Those are
pin-mandated method calibrations and do not encode which WRC coordinate fails.

### 7.2 Did successful pre-freeze runs expose the branch?

Yes.  The fixture-freeze note candidly records successful temporary physical
runs before the scorer freeze.  After exposure, the work added all nine
observable bindings, strengthened translation and affinity controls, separated
the target packets, and added the eliminability refusal.  The frozen outcome
vocabulary and comparator did not change, which blocks simple result-word
shopping, but the process is not a clean blind preregistration of every assay.

Evidentially safe despite exposure are the exact source regression, algebraic
CELL-HIT type split, nonaffinity theorem, full-group translation identity, and
history/record counts independently rebuilt here.  Interpretive qualifiers
about beables, recurrence, and geometry require the hostile narrowing ordered
in this report.

### 7.3 Questions hash and the replay repair

The original pin's malformed Questions digest was a transcription-only
provenance defect; the pre-fixture addendum replaces exactly that table cell.
The later #95 refusal was a separate chronology defect: #94 generated against
the pre-result Questions bytes and then updated the board in the same candidate
commit, so a replay at the new tree correctly refused.  The repair adds one
exact post-result hash and three required tokens while retaining the original
exact hash.  It changes no physics or comparator branch and is the minimum
scientifically honest code repair, although the cleaner chronology would have
updated Questions only after replay verification.

### 7.4 Are #94 and #96 scientifically invariant?

Yes.  At #94 (`ef930124...`) and regenerated #96 (`e5fb6047...`) the transcript
SHA-256 is identically
`45d386714b600ae3dc78369e3785cd78788333a3d0b6bdd31917289d03c2c34c`
and the paper SHA-256 is identically
`6934297cc2a79a8d7ebfa4dd7c52a58d601d686adf9d91b15c45fe416291e0f5`.
The scorer moves from `ff250d...` to the repaired `585559...`; the receipt moves
from `8f475a...` to `017deb...`.  Deleting scorer/payload/seals, gates, runtime
reads, and anchor rows from each receipt and canonicalizing with `jq -c` gives
the same scientific projection hash
`7036ae5b83bbfd01e5f551d91c4954974da126100f8e44088aad389fb7956a1e`.
Only the Questions anchor, dependent procedural seals, and provenance hashes
move.  A clean current replay reproduces transcript `45d386...`, receipt
`017deb...`, and paper `693429...` byte for byte; all 31 gates pass, there are
34 registered no-write mutants, and selftest exits zero.

### 7.5 Does the primary survive reopening Q8?

Yes.  The six coordinate predicates and frozen comparator do not derive from
the board status.  Remove the Q8-retirement qualifier and the same primary is
obtained.  The board line must remain an after-the-fact status report.

### 7.6 Does a candidate claim depend on Papers 3--7?

The exact fixed-carrier reconstruction does not.  The ontological name
“creation-layer representation” and “vertex” recurrence language do depend on
candidate interfaces from those unadjudicated papers.  Those names are demoted
to conditional; none is needed for the primary mathematical reconstruction.

## 8. Numbered repair / kill list

1. **REPAIR — history type.** Replace every potentially bare “history” in the
   WRC result with `EMISSION-HISTORY`; state explicitly that it is not a
   grammar history and that the source enumerates all labels without deriving
   actualization.
2. **REPAIR — beable nomenclature.** Render the positive coordinate as
   `CELL-HIT-HISTORY-TO-COUNT-READOUT-MAP-RECONSTRUCTED` or add “candidate
   beable only; no genuine boundary, actualization, or all-future permanence.”
   Do not advertise the histogram identity as a durability result.
3. **REPAIR — recurrence qualifier.** Replace
   `RECURRING-VERTEX-COUPLINGS-EXTRACTED-NOT-SELECTED` with the measured
   repeated-signature/imported-rule statement.  No recurring grammar event
   type or token-disjoint universality was tested.
4. **REPAIR — covariance warrant.** Add the exact intertwining equations or
   the all-nine-translation/multiple-preparation control.  Preserve the
   all-arena wall.
5. **REPAIR — candidate-layer dependency.** Replace the abstract's
   unconditional “creation-layer representation” with “fixed-carrier
   record/process successor-packet representation,” conditionalizing any
   Papers 3--7 interface language.
6. **REPAIR — DISC scope.** Whenever DISC is used, print “10,380 memoryless
   configurations / 353 distinct laws / no memory-bearing null tested.”  Its
   third-tick witness is memory-specific, not geometry-specific.
7. **SUCCESSOR, NOT WRC REPAIR.** Freeze the family game in section 4, including
   held-out graph interventions, the `A0/A1/A2` nests, equivariant blindness,
   and resource/description budgets.  Adding that family now would change the
   frozen scientific question.
8. **KILL CONDITION — physical beable reading.** If `beable=true` is intended
   to assert an actual fact at a genuine division boundary or absolute
   permanence, change it to false and use the frozen instrument-and-record-map
   residue primary.  The current assay cannot carry that reading.
9. **KILL CONDITION — geometry claim.** Any adjudicated claim that WRC or DISC
   proves dynamic relational geometry irreducible is unsupported and must be
   removed, not repaired by rhetoric.
10. **KILL CONDITION — dependency.** If the primary cannot be stated without
    assuming a Papers 3--7 candidate ontology as terminal, kill the
    creation-layer headline.  The independent fixed-carrier packet result
    remains.

## Hash seal

Ordinary SHA-256 of the report body above this `## Hash seal` heading
(including the newline immediately before the heading):
`73f0c0612c9199d7a1e2a8beb7d91441f2863c1c47fac7839b34d66eb403bdfc`.

Normalized/self SHA-256 of the complete report: replace the two 64-hex digest
values in this seal with 64 ASCII zeroes, preserve all other bytes, and hash the
UTF-8 file:
`0dddf26df229051076b9985c017520929bff9a3695f69a285b9c060daef0cec1`.
