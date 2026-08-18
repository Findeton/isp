# WRC hostile review — Seat P: physical ontology, geometry, Barandes, and scope

Status: **FROZEN INDEPENDENT HOSTILE REPORT**.  Target: WRC Paper 8 at
candidate commit `e5fb6047a84805b5bd260d969099bb229e369441`, with replay repair
`3f75079a970b32f95b1740c4bb07bc2bd9fd79f8` and verification
`7aa47427a269bc774412ba1fdc26953190e1b093`.

I did not read, request, summarize, list, or infer either other WRC review.
I treated the Papers 3--7 hostile reports as unavailable.  I rebuilt the
load-bearing physical distinctions from the frozen WRC packet, Paper 20,
GITER, DISC, EPR, exact arithmetic written independently under `/private/tmp`,
and the primary Barandes sources cited below.

## 1. Verdict first

**Grade: ACCEPT-WITH-FIXES.**

The exact fixed-carrier reconstruction survives.  So does the central
negative result: the source CELL-HIT rule is not an affine quantum instrument,
and an affine projective completion that preserves the displayed outcome
probability changes the conditioned future.  Those are substantial and useful
results.

The physical reading must be narrower.  WRC does **not** reconstruct one
dynamic, back-reacting geometry law.  Its exact successor is

```text
(fixed catalogue G0, count record n, process state psi)
    --sample cell c with a Born weight-->
(fixed catalogue G0, count record n+e_c, process state S G D(n) psi).
```

The sampled label changes a register; the register changes a later phase; the
sites, links, 27 cells, incidence relation, carrier dimension, and shift graph
do not change.  This is genuine **state--record feedback on a fixed carrier**.
It is not yet

```text
(relations, geometry, process state)
    -> (new relations, new geometry, new process state).
```

Paper 8 mostly says this correctly in its scope section.  The remaining
overstatement is the abstract's “exact creation-layer representation” and the
primary word insofar as “representable” inherits a physical creation-event
ontology from frozen-but-unadjudicated Papers 3--7.  The self-contained result
is better named:

```text
WRC-FIXED-CARRIER-WALK-PACKET-RECONSTRUCTED-MODULO-CELL-HIT-INSTRUMENT
```

That repair changes an ontological qualifier, not the exact reconstruction.

## 2. Immutable target and independent exact countercheck

I verified the protocol bindings for the pin, provenance addendum, generic
core, core-freeze note, physical fixture, repaired scorer, fixture-freeze note,
transcript, receipt, paper, and candidate verification.  Their SHA-256 values
are respectively:

```text
956d26e22515471c49ed95a43b2956d8f73e8bcd662eeacc82215d9527c00f99
a93f648cbdff08fba97054b2b28fe261375bccc52d4ebc3b81c1d9f25bc04a7e
94c74731179c1302254a3b7424dcb66d1154518bcf936c5531b05a52f42fa6b3
5220f66b187769e6efb0e6f4b1bbc627f5d71f4ac3968ed057d23cc3d3884993
4ced0a163d645072ded79c51c92cf6f847576f062f35091df67db6d6f8a971c8
58555958108ea62d28ebb541c5da8f6e9a3ec9ea50ef9a16540ee0df0ce1a128
f6622aeb0dbd72c7942521a341ce7acfa0fb8340cb9ef1b78fba9c5b5e881fd4
45d386714b600ae3dc78369e3785cd78788333a3d0b6bdd31917289d03c2c34c
017debe87508bd91b64fa413870af47c5969b442240bff2fa998a538b2de4fef
6934297cc2a79a8d7ebfa4dd7c52a58d601d686adf9d91b15c45fe416291e0f5
7e43f3ff699215bb48e6e56cf9c4939ad60c3e9e61922d0010959ca12df21d5a
```

I independently implemented the `Q(w)` arithmetic
`w^2+w+1=0`, the nine sites, three link directions, record phase, Grover
coin, plus shift, Born branching, and fixed-record null without importing WRC
or DISC code.  The Grover rows have squared norm
`(1+4+4)/9=1` and pairwise inner product `(-2-2+4)/9=0`.
The diagonal phase and shift are unitary.  Nine dense `3 x 3` coin blocks
followed by a permutation have exactly `9*9=81` nonzero transport entries on a
27-dimensional fixed carrier.

The independent coupled branch ladder begins

```text
3, 27, 486
```

and the coupled and frozen-record site laws agree through tick two.  At tick
three I obtain, in site order `(0,0),(0,1),...,(2,2)`,

```text
coupled:
[1/81, 68/729, 116/729, 32/729, 0,
 2620/19683, 32/729, 1324/19683, 8800/19683]

frozen record:
[1/81, 68/729, 116/729, 32/729, 0,
 116/729, 32/729, 68/729, 32/81].
```

The inverse participations are exactly
`33596579/129140163` and `40411/177147`, and the total-variation distance is
`1024/19683`.  This independently confirms the important physical fact:
record feedback is non-inert and first becomes visible after the walk returns
to cells whose record has changed.  It does not decide what the record *is*.

The source operation's physical fork is also real.  For an outcome effect
`E_c`, the literal rule is

```text
N_c(rho) = Tr(E_c rho) U rho U^dagger.
```

It is quadratic in `rho`.  A non-scalar `E_c` makes the mixture coefficient
depend on the input state, so this cannot be an affine operation on the full
density-operator state space.  WRC's registered effect is non-scalar.  Thus an
ontic-pure-state stochastic law and an affine ensemble instrument are not two
notations for one delivered process; they are different physical extensions.

## 3. The complete type chain

The type chain is coherent only if its imports and declarations remain visible:

| arrow | delivered object | status | physical reading licensed |
|---|---|---|---|
| actor vocabulary -> sites and links | `x in Z_3^2`, links `(1,0),(0,1),(1,1)` | imported catalogue/dictionary; not selected by WRC | labels of the committed arena |
| sites and links -> cells | 9 sites times 3 link labels = 27 co-division-pair cells | constructed from that catalogue | fixed configuration labels, not 27 actors and not changing relations |
| cells -> carrier state | `psi in C^27` or `rho` | constructed Hilbert representation; ontological status open | process representation on the fixed catalogue |
| cells -> record | `n in N^27`, initially all ones | declared register and declared beable reading | stored counts if the source rule actualizes a cell |
| record -> phase | `D(n)=diag(w^(n_c mod 3))` | declared functional form; exactly evaluated | memory-controlled phase |
| phase -> local transport | `C_n=G D(n)` | Grover `G` imported/admitted, not selected | fixed local coin with record feedback |
| catalogue -> shift | `S|x,l> = |x+l,l>` | constructed from fixed Cayley labels | static-background incidence compiled into a permutation |
| post-coin state -> CELL-HIT | one cell label with Born weight | Born rule and cut declared; exact alternatives computed | outcome label, not a three-actor event and not a division theorem |
| CELL-HIT -> changed record | `n -> n+e_c` | declared noncollapse update | one stored count changes; `psi` is the same on every label branch |
| changed record -> later transport | later `D(n)` and hence later screen changes | exactly constructed and independently witnessed at tick three | reciprocal state--memory feedback |

“Constructed” here means that the stated formula is implemented and its exact
consequences follow.  It does not mean that nature selected the catalogue,
Grover coin, `Z_3` phase rule, GD order, plus orientation, Born menu, cut,
noncollapse update, or initial record.

There is also no genuine Barandes division boundary in this packet.  WRC names
algorithmic cuts and explicitly refuses that promotion.  Likewise, a count
readout with zero short-history inconsistencies does not prove actualization or
durability under every licensed future.

## 4. What Paper 20's “backreaction” actually establishes

Three arrows must not be conflated:

1. **State to record:** the post-coin state fixes Born weights for the sampled
   cell, and the sampled cell increments a count.  This is exact as an
   algorithmic stochastic update.  One actual outcome remains a postulate.
2. **Record to state:** the count residue controls `D(n)` and thereby changes
   later amplitudes.  This is exact and non-inert; the independent third-tick
   witness above exhibits it.
3. **Matter to geometry and geometry to matter:** a relational object must be
   rewritten, and subsequent transport must be computed from the rewritten
   object; conversely the matter/process state must affect that rewrite.  WRC
   does not construct this arrow.

Paper 20's `18/18` movement against its frozen-stage control proves arrows 1
and 2 matter to its declared observables.  It does not turn `n` into geometry
by theorem.  Its sites, links, and cells never appear or disappear, the shift
never changes, and there is no `G -> G'`.  The quantities called determinant,
admissibility, `q`, and “constant curvature” are readings of the count record.
No calibrated physical length, metric, causal structure, or curvature response
is attached to them.  Paper 20 itself contains the correct limiting sentence:
“THIS UNIT REACHES A RECORD, NOT YET A LAW OVER RECORDS,” and its adjudicated
word is `COUPLING-CONSISTENT-NOT-REQUIRED`.

The strongest fair description is therefore **record-backreacted transport**,
not dynamical spacetime backreaction.  A static graph can influence a walk
because its fixed incidence is compiled into `S`; that is background
dependence, not a dynamical geometry.

## 5. GITER and WRC are neighboring typed constructions

GITER's state is a relational history in an `(A,B)` actor pool.  Its finite
arena contains 3,969 histories, and its constructed carrier is the 185-class
successor-congruence quotient `CONG-185`, contrasted with `MENU-113` and a
2,477-class record quotient.  The equality `r_k=r_q` on 1,362 of 1,362 closing
squares is a result about that quotient's comparison/holonomy readings.  The
history chain is Markov by construction; GITER explicitly says that the
non-Markov signal at `MENU-113` is a property of the description, not of the
underlying history process.

Paper 20 imports the law-native identity `G(h,1)=M(h)` and the normalized menu
`q/M`.  It does **not** import `CONG-185` as WRC's carrier, map its history
classes to the 27 quantum cells, transport the WRC state through a GITER
rewrite, or prove that a GITER successor changes WRC's shift/incidence.  The
two headline numbers therefore have different types:

| unit | state | carrier | measured result |
|---|---|---|---|
| GITER | relational history | re-derived 185-class quotient | agreement on 1,362 closing quotient squares |
| Paper 20/WRC | vector/density operator plus count record | fixed 27-cell one-excitation carrier | 18 declared screen rows move against a frozen count |

No joint state `(history class,n,psi)` and no common successor map are built.
Shared words such as “law,” “carrier,” “connection,” or “holonomy” cannot
weld these objects.  This is a missing construction, not a theorem that such a
joint construction is impossible.

## 6. DISC: exact memory dependence, not geometry irreducibility

The DISC bookkeeping checks.  Its ten displayed rows contain seven
reproductions, two failures, and one unexpressible record-only bundle.  At the
parent-result grain the carved first-two-ticks row is counted with its parent,
giving six of nine parent results reproduced, two not reproduced, and one not
expressible.  The wider denominator also re-sums exactly:

```text
48 + 2880 + 972 + 6480 = 10380 memoryless configurations.
```

Zero of those registered configurations reproduces the third-tick law.  My
independent calculation above reproduces the canonical third-tick difference,
including its IPR and TV witnesses.

What is excluded is nonetheless precise and limited: the frozen-record walk
and the declared swept classes of **memoryless** walks.  DISC says explicitly
that it tested no memory-bearing null.  At any finite horizon, the complete
count history can be included in an enlarged state.  In fact, on this exact
fixture a port-labelled circuit with 27 counters, nine fixed Grover blocks, a
counter-controlled diagonal phase, and the fixed shift permutation reproduces
WRC without treating the counters as spatial geometry.  This is not a cheap
different model; it is the same finite computation with an ordinary-memory
ontology.

Therefore DISC establishes:

```text
registered memoryless class excluded at tick three
=> record/memory feedback is operationally load-bearing at that scope.
```

It does not establish:

```text
record is relational geometry
or
no uniformly resource-matched non-geometric memory model can reproduce it.
```

### The weakest honest successor eliminability game

Absolute non-eliminability on a finite table is impossible against an
unrestricted lookup table.  A useful successor should predeclare all of the
following before generating target screens:

1. a family `F` of relational graphs/carriers, not two relabelings of one
   graph;
2. training members, held-out members, and counterfactual edge rewrites that
   keep the relevant local count/state data matched;
3. one uniform candidate rule
   `tau(G,R,psi)=(G',R',psi')`, including how `G'` selects a later probe;
4. one uniform geometry-blind adversary interface and what raw port labels,
   record data, clock, and sizes it may see;
5. a locality radius and composition/spectator convention;
6. state-dimension and memory-bit bounds, parameter count, program/description
   length, exact-number-field cost, and allowed ancillas;
7. a common calibration and an exact or predeclared approximate success
   metric; and
8. resource accounting over the whole family, so a separately compiled
   circuit per held-out graph cannot hide the graph in its program.

At least three nested nulls are required:

- `B0`: memoryless fixed-carrier walks, the class DISC partially audits;
- `B1`: bounded record-bearing finite-state processes with no graph input;
- `B2`: graph-labelled compiled circuits/lookups under a global description
  budget.

Excluding `B0` says memory matters.  Excluding `B1` on held-out graph
interventions says the selected bounded memory class cannot replace explicit
graph input.  Excluding `B2` under resource parity says the uniform relational
rule compresses/predicts the family better than the registered compilation
class.  None of these finite results proves ontology without qualification;
each supports a class-relative causal/model-selection claim.  Conversely, it
would be wrong to say no finite exact family can ever exclude a predeclared
bounded class.

The decisive discriminator is a matched intervention: two states with the
same local `R,psi` but different output relation `G'` must feed a probe derived
from `G'`, and every allowed `B1` model must predict the same answer while the
relational rule predicts and observes different answers.  WRC has no such
pair.  Its two translation rows remain inside one fixed graph and move the
record and state together.

## 7. Outcome A/B and what each would mean

The proposed fork becomes honest only after the preceding game is frozen.

**Outcome A — geometry load-bearing relative to the declared class.**  One
uniform `tau` predicts held-out graph members and rewiring interventions;
output-geometry erasure removes the later effect; all registered geometry-blind
models fail under matched resources.  This would be the first positive,
class-relative evidence for ISP's distinctive dynamic-relational extension.
It would still not be GR, a continuum limit, or absolute metaphysical proof.

**Outcome B — geometry eliminable within the declared class.**  A uniform
record/memory or compiled-circuit law matches the held-out interventions under
resource parity.  This would defeat the geometry-is-load-bearing claim for
that walk realization and adversary boundary.  It would not refute every ISP
dynamic-geometry theory unless a theorem quantified over the whole admitted
joint-law class.  A failed attempt to construct `G -> G'` is “not
instantiated,” not “the joint-law type is refuted.”

The present WRC fixture is already observationally compatible with the lean
side because a fixed port circuit reproduces it.  That is underdetermination,
not a pre-registered Outcome B, since no family or resource boundary was
frozen.

## 8. Comparison with Barandes

The primary source is Jacob Barandes, *Quantum Systems as Indivisible
Stochastic Processes*, arXiv:2507.21192, especially pp. 4, 8--9, 14--15,
18--20, and 27--28; I also checked the original correspondence paper,
*The Stochastic-Quantum Correspondence*, arXiv:2302.10778.

Barandes's ontology is leaner than the ISP research bet:

- the configuration space is a **fixed ingredient of the model** and supplies
  its elementary kinematical/ontological content;
- the dynamical law is a sparse set of indivisible first-order transition
  probabilities between target times and allowed conditioning times;
- those conditioning times are division events and need not exist at every
  intermediate time;
- beables are diagonal random variables with definite values at each
  configuration; it is the transition-law set, not the beables, that the
  source calls sparse; and
- Hilbert spaces, wavefunctions, and their gauge-dependent ingredients are
  representational tools rather than the basic ontology.

A fixed configuration *space* does not logically require one fixed physical
geometry: its configurations could themselves encode different geometries.
But Barandes does not supply a dynamic-spacetime law merely by leaving that
possibility open.  WRC's 27 configurations are fixed cell/excitation labels;
they are not a catalogue of relational graphs, and the graph does not vary.
It therefore sits closer to the lean fixed-configuration process ontology than
to the proposed ISP extension.

Even that identification is incomplete.  WRC has declared algorithmic cuts,
not demonstrated division events, and its literal CELL-HIT density operation
is nonaffine.  The ontic-`psi` branch can be stated as a nonlinear
pure-state stochastic extension, but WRC has not supplied the full
configuration-level transition law for arbitrary preparations that Barandes
treats as nomological.

The Hamiltonian point supports a representational reading but supplies no
missing physics.  Barandes explicitly compares the stochastic process to the
ontologically clearer Newtonian side and Hilbert/Hamiltonian machinery to the
calculational side.  Under his time-dependent Hilbert-space gauge, the
Hamiltonian transforms as a gauge potential and can even be gauged to zero.
WRC gives a sequence of record-dependent discrete unitaries `U_n`.  It does
not choose a physical time interval, a branch of `log U_n`, a continuous
generator, or a gauge, so it reconstructs no unique Hamiltonian.  The real
candidate would be the underlying process law; WRC diagnoses but does not yet
complete that law at the CELL-HIT seam.

If the dynamic-geometry program fails, a Barandes-style fixed-configuration
process ontology can survive: configurations/beables and transition chances
remain candidates for reality while the quantum state remains
representational.  What is lost is the distinctive claim that the same local
law also creates/rearranges spacetime relations and receives backreaction from
them.

## 9. The psi/rho fork in an EPR setting

WRC's one-carrier continuation proves neither signalling nor safety.  The
conditional issue is elementary.  Suppose two remotely selectable ensembles
have the same Bob density matrix,

```text
rho_B = sum_i p_i |psi_i><psi_i| = sum_j q_j |phi_j><phi_j|.
```

If Bob's future statistics under the ontic-pure-state rule depend on which
decomposition is physically present, and Alice can choose those decompositions
remotely, then Bob can in principle distinguish Alice's setting.  An affine
instrument prevents that dependence at the unconditioned density-matrix
level.  This is a conditional implication, not a verdict on WRC.

The corpus's EPR census does not supply the missing premises.  It has no
two-block entangled process state, no Alice operation, no outcome-conditioned
remote steering protocol, no spacelike calibration, and no post-rewrite
definition of Bob's algebra.  Its `0/105408` far-record movement is forced by a
reading that is a function rather than an intervention; its “separation” is
link-disjointness, not a demonstrated causal cone.  Thus it cannot certify the
ontic branch as safe.  Conversely, decomposition sensitivity alone cannot
certify signalling when remote steering is not even typed.

Any successor that adds entangled carriers, reconvergence, or changing
factorizations must define Alice and Bob input/output algebras across the
rewrite and prove all-input equality of Bob's **unconditioned** statistics for
all Alice settings.  It must separately report conditional steering.  A
single controllable movement of Bob's marginal kills the ontic rule as a
relativistically admissible physical extension.

## 10. Audit of broader physics claims

WRC's thirteen scope walls are correct and must remain in the abstract-level
handoff, not only at the end.  The exact status is:

| topic | object required | WRC status |
|---|---|---|
| dynamic geometry/gravity | changing relational/metric data, reciprocal source law, calibrated invariant | absent; only a count register changes |
| Einstein equations | metric/connection dynamics tied to stress-energy and conservation | absent |
| physical curvature | loop/metric response invariant under admitted representation changes and calibrated to probes | absent; “curvature” is a declared record reading |
| Lorentz/continuum/causal cone | continuum or controlled limit, signature, boosts/local cone | absent |
| QFT | local field/operator algebra, vacuum, composition, multiparticle sectors, renormalized observables | absent |
| arbitrary simultaneous interactions | a common overlap/composition law beyond one sequential walk | absent |
| particles/species/statistics | vacuum/excitation sectors, persistent kinds, exchange/statistics rule | absent; 27 cells are not particle species |
| Hamiltonian reconstruction | clock scale, generator/log branch, gauge and continuity law | absent |
| constants, including an affine/gravitational scale | cross-context identification, dimensions, calibration, selection | absent; coin entries and phase order are supplied dimensionless parameters |
| empirical deviations | operational map to a laboratory and comparison with established QFT/GR predictions | absent |

Until the first row is constructed, the word **gravity** is licensed only as a
research target.  Neither `18/18`, `1362/1362`, the determinant spectrum, nor
the count-derived `q` changes that status.

## 11. Strongest nontechnical ontology now licensed

The strongest sober picture is this:

There is a fixed catalogue of possible labelled cells.  A wave-like
calculation moves possibilities over that catalogue.  The calculation also
assigns chances to one labelled hit.  When a hit is entered in a count book,
the book changes the phases used by later motion, and this feedback changes
future statistics.  The bookkeeping is therefore dynamically consequential,
not decorative.  But nothing in the construction yet shows that the count
book *is space*, that a spatial relation was born or removed, or that a new
geometry carried the next motion.

Separated by ontological status:

- **Real-candidates:** configurations/cell events, if a valid transition law
  and actualization rule make one happen; the count register, if future
  dynamics makes it a durable beable; transition chances between genuine
  division events.
- **Representational candidates:** `psi`, `rho`, the 27-dimensional Hilbert
  space, coin/shift matrices, and any Hamiltonian subsequently chosen.  WRC
  shows the representation is exact at its fixed transport/screens but does
  not settle the `psi` ontology.
- **Declared nomological/kinematical data:** the site/link catalogue and its
  actor dictionary, Grover coin, `Z_3` phase alphabet, GD order, shift
  orientation, Born cut, noncollapse update, initial record, and the decision
  to read counts geometrically.
- **Still absent:** a selected event/rewrite law, a lawful affine instrument or
  fully specified ontic alternative, genuine division events, actualization,
  record permanence, carrier/relation growth, state transport across that
  growth, family-level locality/covariance, cross-block no-signalling, and a
  selected interaction/species/constant structure.

The research bet remains imaginative and coherent: the count-like facts may
be shadows of self-modifying relations, with quantum transport a
representation of one relational process.  WRC does not yet cash that bet.

## 12. Shared procedural audit

1. **Generic-core answer blindness.**  The core was byte-frozen before the
   physical fixture and contains no WRC site set, dimension, links, Grover
   entries, horizon, observables, outcome word, comparator, or Paper 8 prose.
   In that narrow provenance sense it is genuinely fixture-blind.  It was not
   question-blind: its public self-tests already target exact instruments,
   nonaffinity, covariance, and histogram machinery appropriate to WRC.  That
   is legitimate tool design, not independent discovery.
2. **Successful pre-freeze exposure.**  Successful temporary physical runs
   exposed the derived branch before the fixture and scorer froze.  After
   exposure, all nine observables were bound, the record was made nonuniform,
   the affinity witness was tied to the theorem, continuation/coin gates were
   split, packet targets were separated, result-conditional prose was revised,
   and the family-eliminability refusal was added.  This is enough flexibility
   to weaken a claim of pristine prospective confirmation.  Safe despite the
   exposure are: the algebraic nonaffinity theorem; exact replay of the
   committed source bytes; deterministic artifact equality; and the negative
   scope statements.  The detailed gate battery is strong verification and
   regression evidence, not an exposure-free discovery test.
3. **Wrong Questions hash and #95.**  The wrong hash was a provenance-only
   pin error.  The first official result legitimately updated the board in the
   pin-authorized way, causing replay to refuse the stale hash.  Repair #95
   adds the exact post-result digest and three semantic tokens as an allowed
   transition.  Given the chosen mutable-board anchor, that was the minimum
   honest replay repair and did not alter physics or the comparator.  A better
   original design would not have made a post-result board a single immutable
   runtime antecedent, or would have frozen both states in advance.
4. **#94/#96 invariance.**  I independently hashed both revisions.  Transcript
   SHA is `45d386...c34c` at both; Paper SHA is `693429...e0f5` at both.  The
   receipt moves from `8f475a...abca` to `017deb...4fef`.  The only scoped
   source changes are the scorer's exact post-result Questions acceptance and
   the regenerated receipt; no transcript or paper line moves.  The movement
   is semantically confined as disclosed.
5. **Q8 bookkeeping.**  Board retirement is no evidence.  Reopening Q8 does
   not change the six measured coordinates or the reconstructed screens.  The
   question is answered only as: fixed-carrier transport/observables/cuts and
   the declared count readout reconstruct; full affine-instrument equivalence
   fails; dynamic-carrier equivalence was never tested.  Any broader meaning
   of “full packet” must remain open.
6. **Papers 3--7 dependence.**  The exact WRC algebra does not require their
   physical conclusions.  “Creation-layer representation,” recurrence as a
   physically recurring vertex type, and a relational flag/beable promotion
   do.  Because those papers are frozen but unadjudicated here, these phrases
   must be conditional.  Failure to instantiate their proposed interface in
   WRC would not refute the abstract joint-law type.

## 13. Grade

**ACCEPT-WITH-FIXES** the exact fixed-carrier packet reconstruction and the
named CELL-HIT instrument obstruction.  **Reject** any reading of WRC as the
first generative dynamic-geometry fixture, a gravity model, a completed
Barandes process law, or a proof that the record is irreducibly geometric.

Recommended registered disposition:

```text
WRC-FIXED-CARRIER-WALK-PACKET-RECONSTRUCTED-MODULO-CELL-HIT-INSTRUMENT;
STATE-RECORD-FEEDBACK-NONINERT;
DYNAMIC-RELATIONAL-GEOMETRY-UNBUILT;
GEOMETRY-IRREDUCIBILITY-UNTESTED
```

## 14. Numbered repairs and kill conditions

1. **NARROW the primary physical noun.**  Replace “exact creation-layer
   representation” with “exact reconstruction in the declared fixed-carrier
   packet interface.”  Use the disposition above unless Papers 3--7 are later
   adjudicated and a relational weld is independently built.
2. **ADD the typed successor equation to the abstract or verdict section.**
   Show explicitly that `G0'=G0`.  Kill condition for a dynamic-geometry
   claim: if no relation, incidence, carrier, or factorization changes, the
   result is record feedback, not geometry evolution.
3. **RETYPE Paper 20's backreaction.**  Preserve “state-to-record and
   record-to-state feedback is exact and non-inert”; delete or qualify
   “geometry backreaction.”  The `18/18` control cannot carry the stronger
   word.
4. **KEEP GITER SEPARATE.**  Require an explicit map from GITER histories and
   `CONG-185` to WRC cells plus one successor on their joint state before
   combining `1362/1362` with `18/18`.  Vocabulary overlap is not a weld.
5. **NARROW Q8 retirement.**  Retire the fixed finite reconstruction question
   with the affine-instrument failure named.  Do not retire carrier growth,
   full process equivalence, a genuine division structure, or family-level
   geometry.
6. **PRICE pre-freeze exposure in the evidential grade.**  Label the artifact
   battery “exact post-exposure verification/reconstruction,” while retaining
   theorem-grade status for the all-input nonaffinity proof.  Do not market
   strengthened post-exposure gates as pristine preregistered discovery.
7. **FREEZE a successor family-level eliminability protocol before data.**
   Include graph family, held-out rewrites, one uniform `tau`, the `B0/B1/B2`
   nulls, locality, memory/dimension/ancilla/description budgets, common
   calibration, and exact success metric.  Kill condition: any unrestricted
   finite lookup comparison is ontologically vacuous.
8. **RUN the port-circuit adversary and graph-erasure control.**  A later probe
   must be computed from `G'`.  Kill condition: if erasing/changing only the
   graph while retaining matrices and counters leaves all calibrated screens
   unchanged, geometry is not load-bearing in that fixture.  If a bounded
   graph-blind model wins held-out members under parity, Outcome A fails for
   that class.
9. **ADD the EPR/no-signalling gate before promoting ontic `psi`.**  Construct
   two-block entanglement, remote steering, and Bob's algebra across any
   rewrite; prove all-input unconditioned marginal invariance.  Kill condition:
   one controllable distant marginal movement rejects the rule.
10. **STATE the Barandes comparison accurately.**  Fixed configuration space
    and indivisible transition chances are the primary ontology; Hilbert
    objects are secondary; dynamic spacetime is neither asserted nor derived.
    Do not call the current count readout a Barandes division event without a
    transition-law and durability construction.
11. **KEEP the broad scope wall at headline level.**  No gravity, metric,
    physical curvature, Einstein equation, Lorentz/continuum structure, QFT,
    arbitrary interaction composition, particles/species/statistics,
    Hamiltonian, constant, or empirical deviation is constructed.  Kill any
    such claim until its typed object and calibrated invariant exist.
12. **MAKE Papers 3--7 dependencies conditional.**  Their absence here means
    “WRC does not instantiate the proposed physical layer,” not “the joint-law
    architecture is impossible.”
13. **PRESERVE #95 as provenance-only.**  Any repair that changes a scientific
    token, comparator branch, paper, transcript, or fixture after this review
    is a new candidate, not an admissible WRC repair.

## 15. Report SHA-256

Normalized report SHA-256:
`1603b16906f2a534e2a6bb2264f0ec9cc02f2965afe6d96828869eb7b72c08b3`.

The normalized digest is computed with the 64 hexadecimal characters in the
preceding field replaced by 64 zeroes.  The ordinary SHA-256 of the final file
bytes is reported separately to the panel coordinator because embedding that
digest would change the bytes being digested.
