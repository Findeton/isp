# WRC Paper 8 pin — full-packet reconstruction of the committed walk

Status: **PIN — FROZEN BEFORE CONSTRUCTION**.

Authorization: the user's 2026-08-18 instruction to construct Paper 8 while
the hostile panels for Papers 3–7 run in parallel.

Immutable base commit:
`0611966f8b6b5f8e60d8b87e0d5f042278404f91`.

Unit code: `WRC` (walk reconstruction). This is a separate v16 continuation.
It does not edit, repair, adjudicate, terminalize, or silently promote Papers
3–7. Their three mutually isolated review seats are in flight under ledger
#74. No report produced by those seats is an anchor or runtime input here.

The conversation's proposed outcome and every external scratchpad are
motivation only. Every positive and negative statement below must be rebuilt
from committed bytes under this pin.

## 1. One-box question

Is the committed v14 walk—the corpus's only fully measured quantum dynamics—a
representation of the v16 creation-event layer at **full packet equivalence**:

```text
state + complete outcome instruments + clock/cuts + observables + beable map,
```

and not merely a matrix with the same spectrum?

The unit must decide this at the walk's committed finite arena and declared
horizon. A positive transport match is not a full reconstruction if the
outcome-conditioned process or record beables disagree. A failure of full
packet equivalence does not erase an exact lower-level representation.

## 2. Immutable antecedents and their grades

| path | SHA-256 | admitted content |
|---|---|---|
| `v14/paper-20-coupling.md` | `4824d190af73df4d2140f6733d7cf74a90daf59f0be934278c13168510141704` | committed walk definitions, cuts, observables, declared fibers, fixed-carrier feedback |
| `v14/code/coupling_exact.py` | `72e7b299f66e9e1e6c93e00cba2b790e185f115a11ffd2d1452dc412ccd825bb` | terminal exact implementation at commit `04815e50abe772624cb72d88fd877c785b259dc2`; definitions may be read, never imported or executed by WRC |
| `v14/code/coupling_receipt.json` | `55273f6b6068a8847435884cf7f08fd92adf3400ea949d738f7f5549f8842ca1` | path-value anchors for the measured walk packet |
| `v14/note-coup-adjudication.md` | `bacf0af964ae8932328688721c1c61ce1191abb01e6f3a139ecbf2ffb3854b1d` | terminal licensure and declared/derived split |
| `v14/paper-31-occ.md` | `0092caa4d9ad4738d7b35a66317493a3187a3af129f489da6ac0cf35a29e5dcb` | the 27 carrier cells are co-division pairs, not actors |
| `v14/paper-38-epr.md` | `22beb66962232240d2e673763e32b1fe451db7c44a2420754ed42f83e99983e2` | record versus quantum shadow and the committed record referent |
| `v15/note-homonym-audit.md` | `4dbdb8f932e1b4e3d3813c7dcb9d2905f37b4c42819cc14537afa993e2ce51d9` | CELL-HIT versus three-actor event type split |
| `v15/note-js-pin.md` | `93ef35b488119b1eff7e82fb7f9fb444b08dac50dac73f74c1f60f4773139257` | restriction 13: recover the walk as representation; do not freeze its incompatible record update |
| `v15/note-js-pin-v2.md` | `99e90f9a2e8db6a67a1cb46902de96d6086a0931897145d5d54ca3a9e78816ea` | governing packet and CP/affinity requirements |
| `v16/paper-04-support-rewrite-weld.md` | `f61dde79e5fc0e10db1e5dbe13dec25dceaff9842d5e0c5c06ba2ae90eb4bcae` | candidate typed bundle interface only; independently re-derived if used |
| `v16/paper-06-completeness-spectrahedra-record-fibers.md` | `543a2c927ecc7bd184fc758e4d72ebd4d4974327ae5ae2bb279d1fe33086c5d9` | candidate all-input kernel/instrument interface only; independently re-derived if used |
| `v16/paper-07-creation-event-universality-recoverable-records.md` | `acf2dafb165d5ceb82bf4bc532b194f760095ce355b0b5ee7c5996df13878f90` | candidate creation-event packet and recurrence ladder only; independently re-derived if used |
| `v16/QUESTIONS.md` | `91ae5d440d9e28df0a459b0ba73f493a756638b0e4d92c5501755466e9bf19b` | Q8's full-packet standard |

The v16 antecedents are replay-verified but under hostile review. Their prose
cannot decide WRC. Only WRC's independent exact constructions may support its
candidate outcome.

## 3. Term-binding table

| term in WRC | exact binding | alternatives/consequences |
|---|---|---|
| `CELL-HIT c` | paper-20's one selected pair-cell at one walk step | 27 mutually exclusive outcome labels; not a three-actor division event |
| `division event` | the three-actor grammar object only | outside the source walk packet; never identified with CELL-HIT |
| `carrier cell (x,l)` | one of the 27 co-division-pair basis labels | a basis/configuration label, not an actor and not a spacetime point |
| `record n` | the 27-entry integer count field | the durable beable candidate written by CELL-HITs |
| `process state rho` | density operator on the 27-cell linear shadow; pure walk rays are included | distinct from record, branch probability, and ensemble bookkeeping |
| `Born menu` | post-coin CELL-HIT probabilities | mutually exclusive alternatives normalized globally over 27 cells |
| `record menu` | paper-20's separate count-weighted reading | a control, never identified with the Born instrument |
| `creation arrow` | a typed complete successor carrying record rewrite and process transport together | candidate v16 representation; not spatial adjacency and not automatically a lawful CP outcome map |
| `clock` | declared integer walk-step index | algorithmic/discrete; not physical proper time or a derived genuine division boundary |
| `cuts` | input, post-coin CELL-HIT, and post-shift/output cuts in one committed step | their order is part of the packet and is not movable by prose |
| `beable map` | complete labelled CELL-HIT history to its record field, plus the current record readout | does not make psi or rho ontic |
| `kernel` | always qualified: stochastic `kappa(c|rho,n)` or history Gram kernel | the two are never one object merely because both are called a kernel elsewhere |

The sample space is declared before every probability equation. CELL-HITs are
alternatives. Entries written by one grammar event would be simultaneous
consequences, but no such event is present in the WRC source packet.

## 4. The two packets

### 4.1 Source packet

The scorer must reconstruct, without importing v14 executable code:

```text
W = (C^27, rho, n, C_n = G D(n), S,
     input/post-coin/post-shift cuts,
     kappa_n(c|rho) = Tr(P_c C_n rho C_n^dagger),
     CELL-HIT update n -> n + e_c,
     conditioned process state S C_n rho C_n^dagger S^dagger,
     declared observables, record beable map).
```

The final process state is deliberately the same on every CELL-HIT branch at
that step. This is the source's non-collapse semantics, not a target verdict.
The scorer must derive its consequences rather than accepting the sentence.

Allowed source preparations are separated:

1. the committed translated basis preparations and their exact reachable
   histories through the declared five-step horizon; and
2. the complete density-operator state space required for any claim that the
   CELL-HIT family is an affine all-input quantum instrument.

A finite regression match on set 1 cannot prove an instrument claim on set 2.

### 4.2 Target packet

The target creation-event packet is

```text
E = (pre/post configuration catalogues, typed record rewrites,
     process transports, all-input affine CP outcome maps J_c,
     direct-sum trace preservation, declared cuts,
     calibrated observables, beable map, licensed continuations).
```

Three targets must be kept distinct:

- `TRANSPORT`: the fixed-carrier unitary arrow alone;
- `AFFINE-CP`: outcome maps lawful on every density operator; and
- `ONTIC-PURE-STATE`: the literal source update treated as a nonlinear
  stochastic law on pure-state beables.

The third may be an exact mathematical recoding but is outside the frozen
affine creation-event class. It cannot be silently used to pass the second.

## 5. Equivalence doctrine

For every registered preparation and continuation, empirical packet
equivalence requires equality of:

1. state/ray or density operator at each named cut;
2. every complete-outcome probability and normalized conditioned state;
3. clock and cut order;
4. every registered observable and held-out continuation screen; and
5. the record/beable readout and its branch distribution.

Equality is modulo only a predeclared boundary relabeling/global phase gauge.
The gauge action must be self-tested from a fresh computation. Ontological
equivalence is not available unless both packet state spaces are first shown
ontically complete; WRC therefore reports empirical equivalence only.

## 6. Operational stages and mandatory gates

### Stage 0 — referent and packet census

1. Reconstruct the nine sites, three link classes, 27 carrier cells, exact
   Grover coin, `Z_3` phase register, plus/minus shifts, and three named cuts.
2. Reproduce the source path-value anchors: exact unitarity, the delivered
   horizon, branch mass, branch counts, one horizon-five exit probability,
   the translated-start invariant, and the declared coin fiber. Every reused
   value is computed independently and then compared.
3. Bind the beable map by computing `n_t = n_0 + histogram(c_1,...,c_t)` on
   every registered history; ordering information may be lost by the map and
   must not be smuggled back from the branch label.
4. A swapped-cut mutant and a CELL-HIT/three-actor mutant must both die.

Failure to define any coordinate returns `WRC-BLOCKED-AT-PACKET-REFERENT`.

### Stage 1 — exact transport and observable reconstruction

5. Build `C_n`, `S`, and `U_n=S C_n` as exact matrices from the packet
   declaration. Verify the state at input, post-coin, and output cuts on the
   committed starts and on held-out exact states.
6. Type the 27 basis labels as the one-excitation configuration catalogue and
   show the transport support respects the declared kinematic grammar. This
   is a fixed-carrier shadow; no carrier growth may be claimed.
7. Reproduce all registered finite regression observables rendered in the
   Paper 8 receipt, including at least site mass, CELL-HIT field, inverse
   participation, horizon ladder, record maximum, admissibility exit, and a
   held-out two-step continuation screen.
8. Verify translation covariance of the law by transforming state, record,
   CELL-HIT labels, and observables together. An absolute-anchor control must
   fail while the complete translated packet passes. This supersedes the old
   inference that an asymmetric start makes the law unnatural.
9. State separately that no extension to different arena sizes or actor
   motifs is supplied. Translation covariance inside `Z_3^2` is not an
   all-arena naturality theorem.

### Stage 2 — instrument and beable reconstruction

10. Construct the literal outcome operation

```text
N_c(rho) = kappa_n(c|rho) U_n rho U_n^dagger.
```

Check its outcome trace, normalized conditioned state, sum over outcomes, and
record rewrite against the source packet.
11. Test affinity on an independently constructed exact mixed-state witness.
The witness must use a non-scalar CELL-HIT effect and must move a complete
matrix entry, not merely a prose word.
12. Construct the standard affine CP comparison

```text
J_c(rho) = S P_c C_n rho C_n^dagger P_c S^dagger.
```

It must match CELL-HIT probabilities and direct-sum completeness, then face a
held-out continuation that distinguishes its collapsed branch state from the
source's uncollapsed branch state.
13. Prove or kill the general registered statement: a nontrivial outcome
effect cannot both reveal its Born probability and leave every input state at
the same outcome-independent unitary output under an affine CP instrument.
The exact mixture witness is a control; the proof carries the all-input word.
14. The literal nonlinear pure-state recoding must be scored separately. If it
matches, the result is `ONTIC-PSI-EXTENSION-EXACT` and not `AFFINE-INSTRUMENT`.
15. The beable dictionary must be compared under both targets. Equal classical
labels do not rescue unequal conditioned process states.

### Stage 3 — couplings and recurrence ladder

16. Extract, rather than type as conclusions, the local coin entries, phase
   action, shift, stochastic CELL-HIT probabilities, and recurring local
   operator signatures from the reconstructed source.
17. Census equal local signatures across distinct sites, times, and history
   tokens. Spectator/translation/relabel propagation is separated from
   token-disjoint type universality, exactly as in the recurrence ladder.
18. Run at least one admissible non-Grover member of the committed coin fiber.
If it preserves architecture while moving a calibrated held-out observable,
the Grover values are imported measured couplings, not selected constants.
19. Distinguish state-dependent Born weights from context-independent vertex
   couplings. A Born probability is not promoted to a fundamental constant.

### Stage 4 — full comparator and question retirement

20. Derive the primary word from the five packet coordinates. The comparator
   may not share a target literal or decision table with the fixture.
21. Emit a coordinate-by-coordinate equality table for `TRANSPORT`,
   `AFFINE-CP`, and `ONTIC-PURE-STATE`.
22. Q8 is retired at the registered finite scope whether the outcome is full,
   partial, refusal, or blocked. Retiring Q8 does not select the walk as the
   fundamental law.

## 7. Frozen outcome vocabulary

The primary is exactly one of:

```text
WRC-WALK-PACKET-RECONSTRUCTED
WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT
WRC-WALK-REPRESENTABLE-MODULO-RECORD-BEABLE-MAP
WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT-AND-RECORD-BEABLE-MAP
WRC-WALK-REFUSES-CREATION-EVENT-REPRESENTATION
WRC-BLOCKED-AT-PACKET-REFERENT
WRC-INCONSISTENT
```

Allowed qualifiers, emitted only from gates, are:

```text
FIXED-CARRIER-TRANSPORT-RECONSTRUCTED
DECLARED-CLOCK-AND-CUTS-RECONSTRUCTED
REGISTERED-OBSERVABLES-RECONSTRUCTED
TRANSLATION-COVARIANT-WITH-TRANSFORMED-STATE-AND-RECORD
ARENA-EXTENSION-UNBUILT
CELL-HIT-BEABLE-DICTIONARY-RECONSTRUCTED
NONCOLLAPSE-CELL-HIT-MAP-NONAFFINE
AFFINE-CP-REPAIR-MOVES-CONDITIONED-FUTURE
ONTIC-PSI-EXTENSION-EXACT-BUT-OUTSIDE-AFFINE-CLASS
RECURRING-VERTEX-COUPLINGS-EXTRACTED-NOT-SELECTED
STATE-DEPENDENT-BORN-WEIGHTS-NOT-CONSTANTS
WALK-IS-IMPORTED-CANDIDATE-DYNAMICS-NOT-DERIVED-LAW
Q8-RETIRED-AT-COMMITTED-FINITE-ARENA
```

`REPRESENTABLE-MODULO` requires every coordinate except exactly the named
residue to pass. `WALK-REFUSES` is used when even the fixed-carrier transport,
cut, or registered observable dictionary has no lawful common realization.
`INCONSISTENT` is reserved for mutually contradictory gate results or broken
integrity.

## 8. Kill conditions

The following are first-class outcomes, not repair invitations:

1. no exact common state/cut/observable transport dictionary exists;
2. the committed anchors do not reproduce from the written source packet;
3. the literal CELL-HIT operation is affine and CP on the full registered
   state space, killing the proposed residue;
4. a lawful affine CP instrument matches both CELL-HIT probabilities and every
   conditioned continuation while retaining the source's non-collapse rule;
5. the beable dictionary cannot be stated without identifying CELL-HIT with a
   three-actor event;
6. a claimed recurring coupling changes under the predeclared packet gauge;
7. changing the coin within the admitted fiber leaves every calibrated
   observable invariant, killing the extraction-as-physical claim; or
8. any headline depends on in-flight Paper 3–7 reports, mutable repository
   state, a hard-coded answer, float arithmetic, or an unsealed artifact.

## 9. Mandatory mutants and controls

The fixture/scorer stage must freeze mutants covering at least:

- every antecedent hash and consumed path-value token;
- carrier dimension, cell dictionary, coin entry, phase exponent, shift,
  initial state, and cut order;
- Born normalization, branch state, record increment, and beable histogram;
- mixture affinity, CP repair, held-out continuation, and all-input proof word;
- translation action, absolute anchor, link relabeling, and gauge phase;
- recurrence signature, context identity, hidden-coin witness, and coupling
  versus Born-weight typing;
- every primary branch, qualifier, scope wall, transcript, seal, and prewrite
  integrity surface.

Every mechanism carries positive and negative controls. Mutant identity may
not appear in a gate predicate.

## 10. Procedure and whitelist

Chronology is mandatory:

```text
pin commit
-> generic exact core + public-only calibration commit
-> data-only physical fixture and verdict-neutral scorer commit
-> exactly one official invocation
-> commit generated candidate bytes unchanged
-> replay/mutant/independent/off-tree verification commit
-> hostile protocol commit
-> three isolated reviews
-> adjudication and any ordered repair
```

Authorized future construction paths are only:

```text
v16/code/wrc_core.py
v16/code/wrc_public_output.txt
v16/code/wrc_public_receipt.json
v16/note-wrc-core-freeze.md
v16/code/wrc_fixture.json
v16/code/wrc_score.py
v16/note-wrc-fixture-freeze.md
v16/code/wrc_output.txt
v16/code/wrc_receipt.json
v16/paper-08-walk-reconstruction.md
v16/note-wrc-candidate-verification.md
v16/note-wrc-hostile-protocol.md
```

At each ledger event, only the relevant subset plus `v16/LOG.md`,
`v16/README.md`, `STATUS.md`, and after the result `v16/QUESTIONS.md` may move.
No WRC executable may import or run v14/v15/v16 unit executables. Runtime reads
are pinned artifacts plus the unit's own frozen declarations only. Exact
arithmetic, strict CLI, selftest, named mutants, fail-before-write, gate-time
seals, total manifest, byte determinism, alien-CWD and true no-`.git` replay,
and numeric prose rendering from the sealed receipt are mandatory. Runtime cap
is 360 seconds per official or replay invocation.

## 11. Scope walls

Even a full reconstruction would show that one measured finite walk has a
creation-event representation. It would **not** derive or select that walk,
its Grover coin, its phase group, CELL-HIT reading, initial state, horizon, or
universality across arenas.

WRC does not construct carrier growth, relational graph backreaction,
Lorentzian spacetime, continuum limits, QFT, GR, fields, particles, species,
statistics, a Hamiltonian, an affine/gravitational constant, steering,
Bell/EPR reproduction, objective actualization, or empirical deviations. The
record-dependent phase on a fixed 27-cell carrier is feedback, not by itself
gravity. The walk's matrix is representation; no state variable is promoted
to ontology by reconstruction alone.

