# OVG — overlap Gram/instrument varieties, coherent ports, and arity

Status: **PIN — FROZEN BEFORE CONSTRUCTION**.

Authorization: on 2026-08-18 the user explicitly instructed, “With that,
start paper 5,” after supplying the exact refutation of a proposed
order-holonomy trichotomy and its corrected spectral residue. This starts
Paper 5 as a separate v16 continuation. It does not edit, repair, review,
rescore, or terminalize Papers 3 or 4.

Immutable base commit: `ca31ee036736ca97b9d21af82135d8011c2bd141`.

## One boxed question

> When two or more typed relational events overlap, what exact Gram/operator
> conditions allow their different orders or fine histories to coexist
> coherently inside one or several complete recorded successors; what does
> that constrain about their complex weights; and does any surviving
> constraint select causal order, force a higher-arity primitive, or extend
> coherently from binary events to arbitrary finite overlaps?

The object under test is not an “order trichotomy.” It is the exact
**overlap Gram/instrument variety**. For typed fine histories `h` with maps
`V_h : H_in -> H_out`, and mutually exclusive complete output records `j`,

```text
G_hk = V_h^dagger V_k,
K_j  = sum_h c[j,h] V_h,
sum_j K_j^dagger K_j = I.
```

The first equation records every cross-history comparison at a shared typed
boundary. The second coherently groups fine histories inside one complete
successor. The third is the all-input probability-conservation condition for
the recorded instrument. No coefficient is chosen by inspecting a desired
screen, and no sequence is renamed a primitive event merely because it has a
joint support.

## Refuted proposal retained as a mandatory negative control

Before this pin, an external scratchpad proposed that a non-scalar relative
order operator forces either an order record or fusion into a primitive
higher-support event. Its own registered kill condition was then met. With
two exact unitary order maps `A,B`, non-scalar Hermitian
`Omega = A^dagger B`, and

```text
a = 3/5,      b = 4 i/5,      K = a A + b B,
```

the reported counterexample has `K^dagger K = I`. In addition,

```text
K_plus  = (A+B)/2,
K_minus = (A-B)/2
```

obey `K_plus^dagger K_plus + K_minus^dagger K_minus = I` for every pair of
isometries with a common domain and codomain. These scratchpad claims are
untrusted motivations, not anchors. The new unit must reconstruct them after
the generic core freezes. Failure of the equal-real combination is therefore
never evidence for a no-go over all complex weights.

The following claims are withdrawn unless separately earned here:

- non-scalar order holonomy implies “record or fuse”;
- anticommutation selects one antisymmetric weight point or exchange statistic;
- fusion of two binary maps proves an irreducible ternary primitive;
- a blocked rewrite order is automatically a durable record;
- a coherent control flag is merely a classical order record;
- disjoint composition plus an edge-independence assumption derives a Fock
  carrier or a species table.

## Immutable antecedents and path-value anchors

Runtime code may read only the committed paths below through the immutable
base commit. Every read product must be consumed by a named anchor gate. The
user-supplied scratchpad paths, scripts, calculations, and prose are not
runtime inputs and are not evidence.

| committed path | SHA-256 at immutable base | binding use |
|---|---|---|
| `v16/paper-01-joint-relational-history-law.md` | `98489edb6a83919199c11b14b92c423965d1a08ad7652a1c1915d5402f9e6003` | complete-history class operators, all-input completeness, binary viability, first-loop/minimum-arity refusal, and the registered AB/BC successor arena |
| `v16/code/jrh_receipt.json` | `1da2e12dbb6f94a8b93c356e31cb8e00593dbcb083cdbba5d57fc7d49af572a9` | exact JRH bridge and arity anchors, not Paper 5 conclusions |
| `v16/paper-03-contextual-pullbacks-permanent-records.md` | `ca7b06e9e5540d81afb4a401beb66cb2834e3e74033fd742ac5257108a19654f` | context-indexed Gram pullbacks, stable-record/eraser distinction, and growing-carrier instrument scope |
| `v16/code/ppr_receipt.json` | `dc88d6a2fbcf350785cc5f12cdcb8ea0805c4df6deaacac9ceffd34b1699c630` | exact pullback, interference, and completeness regression values |
| `v16/paper-04-support-rewrite-weld.md` | `f61dde79e5fc0e10db1e5dbe13dec25dceaff9842d5e0c5c06ba2ae90eb4bcae` | typed rewrite/transport bundle, kinematic-versus-actual support, and unselected coupling/catalogue result |
| `v16/code/srw_receipt.json` | `c9b036c9d6382bfd8f1402fe5eee39d3a362842b82b1690e28e5a0130a4d5675` | repaired exact SRW candidate values and type/gauge anchors |
| `v16/note-srw-hostile-protocol.md` | `bfe09ac0e277045c93a98b8fa6b22471fc42f5fbc54f60e7b1c4476c60083760` | pre-existing overlap, two-to-`n`, and configuration-individuation questions; not a returned review |
| `v12/paper1-composition-defect.md` | `81bdab5673fb67b63cd10c08fbb80870f8aa01088047718c5b4bf447e1669128` | configuration-individuated histories, records/composition, and reduced boundary gauge |
| `v15/note-homonym-audit.md` | `4dbdb8f932e1b4e3d3813c7dcb9d2905f37b4c42819cc14537afa993e2ce51d9` | E-34 term separation and sample-space discipline |

No v15 SCOUT-T path belongs to the read, cite, write, stage, or archive set.

## Term-binding table

The bindings below are mandatory. Shared words do not identify shared
objects.

| term | bound object | explicitly not identified with |
|---|---|---|
| **elementary relational event** | one generator in the frozen local rewrite/transport grammar, including its typed support and bundle map | an interaction vertex of QFT; a measured outcome; a minimum-arity law |
| **fine overlap history** | one typed composition of elementary events, such as `AB` then `BC`, from a common input to a common final boundary | a recorded causal order automatically; a fundamental micro-time slice |
| **common boundary** | one independently typed codomain or common future into which all histories in a coherent sum map | two vector spaces declared equal after amplitudes are inspected |
| **Gram operator** | `G_hk = V_h^dagger V_k` on the common input, induced by typed history maps | a scalar inner product only; a comparison declared independently of the law |
| **relative order operator** | for two unitary common-boundary histories, `Omega=A^dagger B` | spacetime curvature; a process-matrix causal witness; an order record |
| **single port** | one complete recorded successor with class map `K=sum_h c_h V_h` | one fine history; absence of all later records |
| **multiple ports** | mutually exclusive complete recorded successors indexed by `j`, each coherently containing fine histories | classical ignorance over the fine histories inside each port |
| **parity ports** | the exact two-port instrument `(A+B)/2,(A-B)/2` | a claim that nature measures a parity flag; a selected physical implementation |
| **order label** | a record whose calibrated value distinguishes fine event order | durable record unless permanence is separately proved |
| **dependency** | a rewrite-typing fact that one composition is undefined because an earlier rewrite removes a required referent | a probability-zero history; a durable record; causal nonseparability |
| **coherent order sum** | one class operator containing two differently ordered fine histories | a quantum switch; a superposition of causal structures without a process-level witness |
| **causal nonseparability** | failure of a typed higher-order process to be a convex mixture of definite causal orders under a registered witness | noncommutation, interference, or order-sensitive output alone |
| **primitive arity** | the support size of a law generator irreducible under the predeclared lower-arity grammar, resource set, ancillas, and equivalence | support of a composed circuit; number of actors appearing anywhere in a history |
| **event fusion** | replacement of a composite path by a single grammar generator | proof that the composite was ontologically indivisible |
| **local flag** | an explicit record factor assigned to a declared local subsystem/catalogue entry | proof that the flag is locally implementable by the original event grammar |
| **spectral classifier** | the unitary two-history theorem relating the number of distinct eigenphases of `Omega` to nontrivial single-port solutions | the classifier for nonnormal contractions or more than two histories |
| **law selection** | reduction to one empirically equivalent coefficient/instrument class by independently declared constraints | existence of at least one complete coefficient point |

Probability normalizes over complete ports `j`. Fine histories inside one
`K_j` are simultaneous coherent contributions, not separately normalized
outcomes. Relations created inside one successor are consequences, not ports.

## Arena coordinates

| coordinate | frozen declaration |
|---|---|
| **boundary** | finite exact input and common-final process spaces; both equal-carrier unitary and dimension-changing isometric common-boundary sectors |
| **relational arena** | actors `A,B,C` with overlapping binary generators on `AB` and `BC`; disjoint, joinable-overlap, delete/use dependency, and divergent-endpoint controls |
| **family** | exact finite history maps over `Q(i)`, exact algebraic coefficient constraints over real polynomial coordinates, and finite recorded port partitions |
| **law** | the coefficient matrices `c[j,h]` and typed elementary transports are variables unless an antecedent anchor fixes them |
| **state** | operator identities for all inputs are primary; displayed preparations/screens are regression witnesses only |
| **gauge** | composition-compatible boundary frames, typed relabelings, and history rephasings preserving calibrated record partitions; arbitrary mixing of configuration-distinct histories is not presumed gauge |
| **provenance** | immutable base `ca31ee036736ca97b9d21af82135d8011c2bd141`; external scratchpads excluded |
| **runtime** | 300 seconds per ordinary or mutant invocation; no substantive float or tolerance |

This is a finite overlap arena. It is not a continuum, a Lorentzian causal
structure, a quantum field, a process-matrix experiment, or a theory of all
finite graphs.

## Four-gate audit for new objects

| object | referent | necessity | no-smuggling | discriminator |
|---|---|---|---|---|
| overlap history family | all typed composites generated from the frozen rewrite/transport grammar with a common input | an overlap equation cannot be posed before the lawful orders are known | history membership is computed from rewrite typing, never inferred from a nonzero matrix term | delete/use, divergent-endpoint, commuting, and overlapping-joinable controls accept different members |
| common-boundary Gram family | exact operators `V_h^dagger V_k` after codomain typing | instrument completeness depends on cross terms, not on spectra of separate histories | no external pairing is supplied after maps are evaluated | a cross-term tamper changes the completeness variety; a boundary-frame change leaves its physical locus covariant |
| port coefficient variety | exact solution set of `sum_j K_j^dagger K_j=I` in the declared coefficient family | one tested coefficient point cannot support a universal no-go | coefficients start symbolic; expected witnesses are absent from the physical fixture | equal-real failure, complex-success, parity-port, and amplifier controls separate existence from nonexistence |
| spectral classifier | real-linear solution space of `z Omega + zbar Omega^dagger=cI` for unitary `Omega` | the corrected residue predicts phase constraints that can select part of the weight variety | the number of eigenphases is computed exactly and classifier output is not planted | scalar, two-phase Hermitian, two-phase non-Hermitian, and three-or-more-phase controls produce different ranks |
| record-carrier locality test | declared assignment of output-record factors to actor-local catalogue slots plus a typed implementation grammar | a globally defined parity outcome might fail a stronger local implementation rule | attaching a formal flag is separated from generating it by allowed local maps | local Stinespring flag, erased flag, and locally unimplementable/global controls are classified separately |
| primitive-arity test | exact factorization/irreducibility census relative to a frozen lower-arity grammar and resources | support size alone cannot distinguish a primitive event from a circuit | the candidate higher-support map is not inserted as its own factor | explicit binary product, ancilla-assisted factorization, and an independently supplied irreducibility control separate the cases |
| causal-order witness | a process-level functional tested against the causally separable cone in a separately typed higher-order fixture | fixed-order interference is insufficient to justify indefinite causal order | no quantum-switch or process-matrix word may appear as a finding without the object and witness | ordinary order sum is refused; only a future implemented witness could promote it |

The causal-order row is principally a refusal gate in this unit. A full
process-matrix construction is optional only if separately frozen before its
truth is known; its absence cannot be turned into a positive claim.

## Mathematical core to construct

### General finite overlap instrument

For history maps `V_1,...,V_n : H_in -> H_out` and `m` complete ports, compute

```text
G_hk = V_h^dagger V_k,
K_j  = sum_h c[j,h] V_h,
Q(c) = sum_j K_j^dagger K_j - I
     = sum_h,k (sum_j conjugate(c[j,h]) c[j,k]) G_hk - I.
```

The core must return the exact operator polynomial coefficients, not only a
state expectation. A candidate is complete iff every matrix entry of `Q`
vanishes identically. Trace-nonincreasing partial branches are separately
typed; state-relative normalization is insufficient.

For two isometries `A,B` with common source and target,

```text
S = sum_j (|a_j|^2 + |b_j|^2),
C = sum_j conjugate(a_j) b_j,
sum_j K_j^dagger K_j = S I + C Omega + conjugate(C) Omega^dagger,
Omega = A^dagger B.
```

This identity is valid for dimension-changing common codomains too. The
unitary spectral shortcut below is not.

### Two-unitary single-port spectral theorem to test

For one port `K=aA+bB`, set `z=conjugate(a)b` and
`c=1-|a|^2-|b|^2`. When `A,B` are unitary, `Omega` is unitary and the operator
equation becomes, in an eigenbasis,

```text
2 Re(z exp(i phi_k)) = c    for every distinct eigenphase phi_k.
```

The pre-registered candidate theorem is:

1. the real homogeneous solution space in `(Re z, Im z, c)` has dimension
   `2`, `1`, or `0` when `Omega` has respectively `1`, `2`, or at least `3`
   distinct eigenphases;
2. a nontrivial coherent single-port solution with `z != 0` exists exactly in
   the first two cases;
3. at two eigenphases the phase obeys
   `arg z = -(phi_1+phi_2)/2 mod pi`;
4. the statement excludes `z=0` definite-order endpoints and does not select
   the magnitudes uniquely.

The proof must establish existence of actual `a,b` from the real-linear
solution, not stop at a formal `z,c`. Exact `Q(i)` fixtures verify only their
declared phase rows; the theorem itself requires symbolic algebra.

For nonnormal or nonunitary `Omega`, the core solves the full real-linear
operator equation. It may not count eigenvalues and reuse the theorem.

### Multiple ports

The parity construction is a mandatory universal control:

```text
K_plus=(A+B)/2,     K_minus=(A-B)/2.
```

For every isometric common-boundary pair, its completeness must be proved
symbolically and verified on every exact fixture. This establishes existence
of one mathematical instrument, not selection of those ports or an event-law
implementation.

### Typed rewrite critical pairs

The graph side must enumerate, independently of amplitudes:

1. disjoint commuting rewrites;
2. overlapping rewrites whose two orders reach one typed common boundary;
3. a delete/use dependency where one order is undefined;
4. two lawful orders with nonidentical final carriers and no declared common
   future;
5. a dimension-changing pair that reaches one larger common codomain.

Only cases 1, 2, and 5 admit a direct coherent Gram sum at the registered
boundary. Case 3 is a dependency. Case 4 is untyped until a common future is
supplied. Neither is automatically a record or a no-go.

### Arity and locality

Every candidate ternary map is tested against the frozen binary grammar,
allowed ancillas, records, and declared equivalence. `Theta_BC Theta_AB` is a
binary composite even if its support is `{A,B,C}`. Fusion is notation until a
factorization obstruction is proved. Conversely, failure to factor relative
to one finite grammar earns only fixture-relative irreducibility.

For each complete port family the unit constructs the canonical flag dilation

```text
W psi = sum_j K_j psi tensor |j>_flag.
```

Completeness makes `W` an isometry. Assigning `flag` to a local catalogue slot
tests kinematic locality; whether the frozen elementary grammar implements
`W` tests dynamical locality. These are distinct outcomes.

## Locked investigation chronology

1. **Pin freeze.** Commit this file plus ledger/plan/question/status updates.
   No OVG implementation, fixture, result, or Paper 5 path may exist first.
2. **Generic core freeze before physical fixture truth.** Implement exact
   Gaussian-rational matrix algebra, symbolic operator-polynomial extraction,
   real-linear rank/nullspace certificates, typed history enumeration,
   factorization utilities, CLI, sealing, and mutation machinery. Run only
   public calibrations whose answers are stated in their constructors. Commit
   source and public artifacts. The physical fixture and scorer remain absent.
3. **Fixture/scorer freeze.** Add one data-only physical fixture and a
   verdict-neutral scorer. It contains no expected verdict, outcome, pass
   count, or target coefficient point. Freeze source/fixture hashes while all
   official result paths are absent.
4. **One official execution.** Run the frozen scorer once. It renders the
   transcript, sealed receipt, and Paper 5 from one result object. Commit those
   bytes as-is before replay, mutants, or interpretive edits.
5. **Candidate verification.** Rebuild the result independently, run two clean
   worktree replays, all registered mutants, alien-CWD and true no-`.git`
   archive execution, seal/transcript/paper reconciliation, and exact source
   audit.
6. **Hostile protocol.** Freeze three independent seats: operator/algebra;
   rewrite/concurrency/arity; and quantum causality/QFT/ontology. Reviewer
   dispatch requires a separate explicit user instruction under the active
   collaboration rule.
7. **Adjudication and repair.** No terminal status is possible without the
   frozen reports, joint adjudication, bounded repairs, and terminal replay.

## Mandatory exact fixtures and controls

### A. Two-history unitary strata

1. `Omega=I`: projectively identical histories, scalar stratum.
2. `Omega=iI`: nontrivial scalar phase, with the same quotient warning.
3. `spec(Omega)={+1,-1}`: the exact CNOT-order counterexample, including
   equal-real failure and `a=3/5,b=4i/5` success.
4. `spec(Omega)={-i,+i}`: two non-Hermitian eigenphases.
5. at least three distinct eigenphases, including an exact `Q(i)` fixture:
   no nontrivial single-port solution but the parity instrument survives.
6. boundary rephasing/conjugation covariance and exact spectrum/rank controls.

### B. Dimension-changing common boundary

1. two isometries `C^2 -> C^4` with nonnormal overlap
   `Omega=[[0,3/5],[0,0]]`;
2. full operator-equation solution, with no spectral-shortcut claim;
3. parity-port completeness;
4. a completeness-violating amplifier;
5. a reached-subspace/codomain frame covariance control.

### C. Three or more fine histories

1. a three-history Gram matrix whose coefficient variety is solved exactly;
2. two distinct complete port decompositions of the same unconditioned map,
   separated from calibrated outcome instruments;
3. a rank-deficient/dark-history control and a later reactivation control;
4. a port-refinement/coarse-graining composition check;
5. at least one surviving positive-dimensional coefficient family with a
   moving calibrated port statistic, or an exact proof that none survives at
   the registered arena.

### D. Rewrite overlap and arity

1. all five critical-pair cases listed above;
2. actor relabeling covariance and idle-spectator extension;
3. a product of two binary maps explicitly rejected as proof of primitive
   arity three;
4. an irreducibility census over the declared binary grammar, with counts
   computed rather than typed;
5. an ancilla enlargement that can change the factorization answer;
6. no all-`n` conclusion from the three-actor fixture.

### E. Records, locality, and causal language

1. canonical flag dilation for every complete instrument;
2. local catalog assignment versus local grammar implementability;
3. durable, erasable, and untested-permanence order-label controls;
4. explicit refusal of causal-nonseparability for ordinary class-operator sums;
5. if no higher-order process/witness is constructed, a hard wall forbidding
   “quantum switch,” “indefinite causal order,” and equivalent promotions in
   result prose;
6. a preparation-independent fixed-subsystem no-signalling check where typed,
   with changing-subsystem and conditional steering left open unless built.

## Pre-registered primary outcomes

The scorer emits the earliest applicable primary outcome and independent
qualifier segments. Every branch below is reachable by a registered control.

1. `OVG-BLOCKED-AT-TYPED-COMMON-BOUNDARY` — the candidate overlap histories
   do not share a lawful codomain/common future, so the proposed coherent sum
   is undefined rather than false.
2. `OVG-INCONSISTENT-AT-ALL-INPUT-COMPLETENESS` — the advertised coefficient
   family normalizes selected states but no registered complete instrument
   survives the operator identity.
3. `OVG-SINGLE-PORT-SPECTRAL-CLASSIFIER-REFUTED` — any exact unitary control
   violates the pre-registered dimension/existence/phase theorem.
4. `OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED` — the typed Gram family and exact
   complete coefficient variety are computed, the spectral theorem passes at
   its unitary scope, and coherent single- or multiport solutions survive.

The primary may carry these independently derived suffixes:

- `SINGLE-PORT-PHASE-CONSTRAINED` — a two-eigenphase row fixes the relative
  phase modulo pi but not all magnitudes;
- `MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED` — more than one
  operationally different complete instrument survives;
- `LOCAL-FLAG-KINEMATICALLY-PERMITTED-BUT-IMPLEMENTATION-UNSELECTED` — the
  canonical flag fits a local catalogue slot, while the event grammar does
  not select or derive its implementation;
- `LOCAL-IMPLEMENTATION-OBSTRUCTED-AT-DECLARED-GRAMMAR` — the exact
  factorization census excludes the flag dilation at that grammar only;
- `COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY` — every claimed
  higher-support witness is a typed lower-arity composite or changes status
  under allowed ancillas;
- `PRIMITIVE-ARITY-IRREDUCIBLE-AT-DECLARED-GRAMMAR` — one independently
  supplied generator is proved nonfactorizable within the complete frozen
  resource census, explicitly without an all-physics or all-`n` promotion;
- `CAUSAL-NONSEPARABILITY-UNTESTED` — no higher-order process and witness were
  built; order interference earns no causal-structure claim;
- `OVERLAP-LAW-UNSELECTED` — multiple gauge-inequivalent elementary maps or
  port coefficient families move a calibrated statistic.

Outcome 4 is an existence/classification result, not selection of nature's
law. The presence of parity ports prevents “record or fuse” from being an
exhaustive conclusion unless an independently frozen local implementation
rule excludes them.

## Kill conditions

Any one of the following kills the corresponding positive claim:

- testing one equal-real weight point and generalizing its failure to all
  complex coefficients;
- using only `Tr(rho Q)=0` for selected `rho` instead of the all-input operator
  identity `Q=0`;
- counting eigenvalues of a nonnormal contraction and invoking the unitary
  spectral theorem;
- omitting the `z=0`/definite-order distinction from a single-port existence
  statement;
- claiming the two-phase condition selects coefficient magnitudes when it
  constrains only the registered phase combination;
- calling scalar-holonomy histories physically distinct without a record or
  calibration that individuates them;
- declaring two carriers common after amplitudes are known;
- treating a delete/use dependency or divergent codomain as a durable record;
- calling the parity-port construction selected dynamics merely because it is
  a complete instrument;
- calling a formal local flag locally implementable without factorization in
  the frozen elementary grammar;
- calling an erasable or uncensused order label durable;
- renaming a binary product as a primitive ternary event;
- claiming an arity no-go without a frozen lower-arity grammar, resource set,
  ancilla policy, and exhaustive factorization certificate;
- promoting interference of fixed circuit orders to a quantum switch or
  causally nonseparable process without a higher-order object and witness;
- deriving a Fock carrier, field, or particle species from an untested
  edge-independence or strong-monoidal assumption;
- promoting a three-actor overlap fixture to an arbitrary-`n` composition
  theorem;
- using float, tolerance, mutable repository truth, typed counts, a planted
  result, or a comparator sharing the result builder.

## Receipt, CLI, seals, and falsifiers

- Substantive finite arithmetic is exact over `Q(i)`. Symbolic identities and
  real-linear rank certificates use exact rational/integer coefficients.
- The generic engine freezes on public calibrations before the physical
  fixture/scorer exists. The physical fixture is data-only and contains no
  `expected`, `verdict`, `outcome`, pass count, solution dimension, or target
  coefficient value.
- The CLI rejects unknown arguments with exit 2 and supports `--selftest`,
  `--mutant NAME`, `--output PATH`, and `--receipt PATH`.
- `--selftest` corrupts an anchor, exits 1, and writes no artifact.
- Every runtime path read is recorded at access and consumed by a named gate.
- Every published field is sealed when its gate passes. Promotion recomputes
  seal totality, claim/table/fence equality, term bindings, transcript/ledger
  multiset equality, and independent verdict reconstruction.
- Two worktree runs, alien-CWD execution, and a true no-`.git` archive replay
  must be byte-identical.
- Mutants must alter the measured object, die at the registered gate, emit no
  traceback, and write no artifact.

At minimum these named mutants must exist and die blind to their names:

```text
anchor-corrupt, history-order-drop, common-boundary-forge,
gram-cross-term-move, gram-self-compare, state-only-normalize,
equal-real-universalize, complex-witness-drop, parity-factor-move,
scalar-call-distinct, eigenphase-count-move, phase-constraint-drop,
nonnormal-spectral-shortcut, z-zero-call-coherent, three-history-drop,
port-coarsegrain-break, dependency-call-record, divergent-call-common,
local-flag-call-implemented, local-factorization-drop,
binary-product-call-primitive, ancilla-policy-hide, durability-assume,
causal-switch-word, all-n-promote, typed-count, float-leak,
verdict-flip, transcript-forge, seal-after-write
```

The runtime cap is 300 seconds per ordinary or mutant invocation. Symbolic,
exhaustive, and fixture-only claims are labelled separately.

## Frozen file whitelist

Only these new OVG paths may be created; programme boards may move only in
commits whose ledger entries name the change:

```text
v16/note-ovg-pin.md
v16/code/ovg_core.py
v16/code/ovg_public_output.txt
v16/code/ovg_public_receipt.json
v16/note-ovg-core-freeze.md
v16/code/ovg_fixture.json
v16/code/ovg_score.py
v16/note-ovg-fixture-freeze.md
v16/code/ovg_output.txt
v16/code/ovg_receipt.json
v16/paper-05-overlap-gram-instrument-variety.md
v16/note-ovg-candidate-verification.md
v16/note-ovg-hostile-protocol.md
v16/review-ovg-operator.md
v16/review-ovg-rewrite.md
v16/review-ovg-physics.md
v16/note-ovg-adjudication.md
v16/note-ovg-repair-freeze.md
v16/note-ovg-repaired-artifacts.md
v16/note-ovg-terminal-verification.md
v16/README.md
v16/PLAN.md
v16/QUESTIONS.md
v16/LOG.md
STATUS.md
```

Every git stage names explicit paths. The unrelated untracked v15 SCOUT-T
files remain untouched.

## Scope walls

This unit may derive an exact finite overlap-instrument classifier, show that
complex phases repair a false no-go, and determine factorization relative to
one frozen local grammar. It cannot derive the actual elementary-event maps,
their weights, the configuration catalogue, a universal port/record law,
record permanence outside the frozen continuation grammar, actualization,
arbitrary-`n` composition, a continuum, Lorentz symmetry, gravity, QFT,
particle species, exchange statistics, a Hamiltonian, a coupling constant, an
absolute scale, or a deviation from QFT/GR.

A phase constraint is not spin-statistics. An order-sensitive circuit is not
indefinite causal order. A factorization obstruction in one grammar is not an
ontological proof of indivisibility. A local flag dilation is not a selected
measurement mechanism. Geometry backreaction remains unproved unless a
relational rewrite changes a later calibrated probe through the output
geometry under a nonfactorizing law.
