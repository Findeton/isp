# Paper 26 round 1 — independent multilane review

**Frozen manuscript target:** commit
`23a4ae0589ee5c0e631cd4bf8bcaa40fff70d61e`.

**Manuscript:**
`relativistic-isp-v10-paper26-admissible-regional-history-specifications.md`.

**Lanes:** probability/specification mathematics; corpus, causal locality and
physical attribution; executable evidence, reproducibility and manuscript
claims.

**Independence disclosure:** three fresh isolated reviewer contexts inspected
the frozen commit without inheriting the authoring conversation.  They were
instructed to derive the K1 path-five and joint-mode counts before consulting
the D37 self-hostile reviews.  The present file aggregates those independent
reports; it is not a claim of an external human peer review.

**Verdict:** **PAPER 26 PROMOTION WITHHELD.  THE FINITE PROBABILITY FAMILY AND
THEOREMS 1--3 SURVIVE, BUT THE EXECUTED OBJECT DOES NOT CARRY THE ORIENTED
CAUSAL-HISTORY CLAIM MADE BY THE MANUSCRIPT.**

**Count:** **1 blocker / 5 majors / 6 minors / 3 nits.**

No repair is applied in this review.  Findings are frozen before authorship
resumes.

## 1. Reproduction and exact evidence

Fresh D37 executions under hash seeds `0`, `1`, `42`, `314159`, a random
seed, `2718281` and `3141592` all exited zero.  They were byte-identical to
each other and to the committed receipt and printed `PASS 9/9`.

The frozen hashes are:

```text
source
8a8772f878d725ce1f22acc703cd23accd531ca0ebb8a08af2bc01eca92f7f4a

complete stdout / committed receipt
6d0f9ed7bb703e7b17f9836453115b2dd14e9ada74bc9f9fd493deb4798fc9b7

printed stdout body
91a0cb3a85aca73d4cc78266ef29f0a4bdac8cf7a44406a7e258a3d71bb7f5c7

internal science
cf9997407d8cb8b974f442ab341b7f4d3e6a1b3d3db3c43c6c4207189c0df0bf

Paper 26
123f051a04000bdb078f7b4d9db96298946d13875a49f12917d3f6a617c5f9da

D37 note
54b93e984f16d3971611bad8d65b7652fac10df6297243ab86553772f06d02f2
```

Every printed headline reproduces:

```text
registry     8 graphs / 28 roles / 19 edges / 196 regions / 23 interface rows;
K3          508 conditionals / 7,098 towers / 138 mixtures;
forcing     30 traversed additions / 25 reconstructed states / odds 2 and 4;
K2          188 conditionals / 165 boundaries / 1,224 towers;
K1          6 atoms / 35 towers / path-five 5/11,6/11 versus 1;
covers      33+33+33 = 99 overlap checks;
joint       166 conditionals / 134 one-site / 238 towers / 186 atoms;
equal point 93 atoms / Q modes 34,25,34 / Q selected 18;
D26         64/125 / 2744/3375 / 431/465;
covariance  6/6;
factor      4/4 with atom counts 9,4,4,441.
```

The blocker and majors below are therefore not claims that the frozen
arithmetic is false.  They concern the mathematical object executed, the
strength of several gates and the manuscript's attribution of those results.

## 2. Required independent derivations

### 2.1 K1 path-five

On `A-B-C-D-E`, uniform greedy priority over all `5!=120` orders gives:

```text
selected set   priority-order count
{A,C,E}        56
{A,D}          20
{B,D}          24
{B,E}          20.
```

For `{A,D}`, the conditions are `A<B` and D earlier than both C and E, giving

```text
120 * (1/2) * (1/3) = 20.
```

For `{B,D}`, start with `B<A` and `D<E`, which gives 30 orders.  Exclude the
six interleavings of the chains `C<B<A` and `C<D<E`, because C would be
selected first.  This leaves `30-6=24`.

For local region `{A,B}`, exterior `{D}` therefore gives

```text
P({A}|{D}) = 20/44 = 5/11;
P({B}|{D}) = 24/44 = 6/11.
```

Exterior `{E}` occurs only for `{B,E}`, so `P({B}|{E})=1`.  In both cases C
is unselected, hence the accepted one-hop collar is empty.  The retained K1
witness is correct.

### 2.2 Joint mode count

At equal mode weights and activity one, a selected vertex has two present-mode
choices and an unselected vertex has three choices.  Summing over independent
selected sets of the three-path gives

```text
empty set          3^3             = 27;
three singletons   3 * 2 * 3^2     = 54;
endpoint pair      2^2 * 3         = 12;
total                                93.
```

Fix Q to BORN.  Q unselected gives `(3+2)^2=25` endpoint continuations; Q
selected gives `3^2=9`, for 34.  TOKEN is symmetric.  `NO_BIRTH` forces Q
unselected and gives 25.  Q is selected in `2*3^2=18` atoms.  Thus

```text
P_Q(BORN)       = 34/93;
P_Q(TOKEN)      = 34/93;
P_Q(NO_BIRTH)   = 25/93;
P_Q(selected)   = 18/93 = 6/31.
```

The independent derivation requirement is satisfied.

## 3. Probability theorems that pass

### 3.1 Theorem 1

Exact positive feasible support permits deletion of any selected set to the
empty state.  Reversing that path uses only feasible additions, so fixed
ratios give

```text
mu(S)/mu(empty) = product_(v in S) lambda_v.
```

Commutativity removes deletion-order dependence and normalization gives the
hard-core law.  The manuscript correctly separates the one-hop Markov
property from the forcing premises.

### 3.2 Theorem 2

For fixed exterior data, a local assignment extends to a maximal independent
set exactly when it is internally independent, dominates every unblocked
rejected interior vertex and satisfies every unmet exterior demand.  Uniform
finite K2 weight makes the conditional uniform on those extensions.  The
sufficient demand constructor really is radius two.

### 3.3 Theorem 3

At the pairwise locally finite conflict-graph scope, the completion proof is
sound.  Each admitted state space is a closed subset of a countable product of
finite alphabets and is nonempty.  Fixed-boundary exhaustion measures have
weakly convergent subsequences.  For fixed finite D, `gamma_D f` has a finite
one-hop collar for K3/joint and radius-two collar for K2, hence is continuous.
Finite specification identities pass to the limit.  Existence is earned;
uniqueness remains correctly open.

The DLR convention and nested identity `gamma_E gamma_D=gamma_E` for
`D subset E` are also correct.

## 4. BLOCKER B1 — the causal/oriented carrier is not implemented

Paper 26 declares a supplied opportunity complex

```text
C = (V, E_conf, parent, type)
```

and describes incoming, lateral and generated data as an oriented causal
regional-history interface.  The executable actually defines:

```text
Graph(name, vertices, edges);
OrientedCell(name, proposals-with-participant-labels).
```

`oriented_interface()` emits `("carrier_parent", proposal)`.  The proposal is
therefore used as its own placeholder parent label.  There is no separate
parent-record identity, type map, port/wire event DAG, causal partial order,
acyclicity check, typed history legality or restriction transport on such a
history.

All K1/K2/K3 and joint-mode probability kernels consume only the undirected
pairwise conflict graph.  The paper admits that the finite orientation layer
does not generate a record DAG, but nevertheless calls the result a causal
regional-history specification and says it supplies the architecture missing
from Papers 24 and D33--D34.  That promotion is not carried by the executed
object.

The S0 gate is also too weak for its interface narration.  It checks the row
count, participant-intersection equality with the separately declared graph,
automorphism counts and an orientation hash.  It does not fail closed on the
presence of participant bases, distinct carrier parents, lateral proposals or
both generated click types.  The four interface claims printed after S0 are
hard-coded.  S8's relabeling check would also pass for uniformly empty rows.

Finally, the paper says conflict edges are “re-derived ... rather than typed
twice.”  Both `GRAPHS` and `ORIENTED_CELLS` declare the incidence; the receipt
cross-checks them.  Cross-checking two declarations is useful, but it is not a
single derived source.

**Required repair:** choose one honest result.

1. **Preserve the Paper 26 thesis:** implement a genuine typed parent/port
   event DAG, legal incoming/generated transport, causal restriction and
   event-poset covariance; then re-run the specification, locality and
   completion claims on that object.
2. **Narrow the theorem:** systematically rename the result an annotated
   pairwise conflict-graph configuration specification and withdraw the claim
   that it closes the causal-history architecture.

The first path is the constructive Paper 26 program.  Until either path is
complete, paper-level promotion is blocked.

## 5. MAJOR M1 — D33 covariance is not tested

D33's construction gauge identifies different linear extensions of one typed
causal partial order while retaining comparable same-wire order as physical.
Paper 26's “construction-order gauge” consists of graph/participant relabeling
and the statement that Python enumeration order is not physical.  With no
event poset, a linear-extension comparison is not expressible.

**Required repair:** demote the current result to relabeling/enumeration
covariance, or add a typed event poset and gate equality across its linear
extensions while preserving comparable event order.

## 6. MAJOR M2 — D34 anti-dilution is only conflict factorization

D34 asks whether a causally unrelated remote record can change a local
conditional.  D37 tests two disconnected edges of an undirected conflict
graph.  The `two_pairs` fixture has no oriented cell, parent data, capability
or record wire.  Nonadjacency in `E_conf` is not yet causal-record
disconnection.

**Required repair:** call the present result disconnected conflict-component
factorization only, or test full causally disjoint record components with
their typed parents, ports and wires before calling it D34 anti-dilution.

## 7. MAJOR M3 — the D26 observable has no represented parent lineage

The manuscript defines a product of `sqrt(1-g_e)` over same-line BORN events.
The mode law has no real parent or line relation and therefore cannot decide
which BORN roles act on the same probed parent line.  The `2744/3375` row is an
externally imposed independent same-line control, not a history observable of
the registered causal object.  The single-Q factor `431/465` is exact given
the supplied BORN marginal and a supplied parent-line interpretation, but
that mapping is outside D37.

TOKEN factor one is also the coherence-neutral matched control, not a theorem
about arbitrary dormant activation dynamics.

**Required repair:** key the visibility observable to an implemented parent
lineage, or state that the numbers constrain the combined BORN-incidence,
coupling and external parent-line mapping relative to a coherence-neutral
TOKEN control.  Do not present that mapping as receipt-carried.

## 8. MAJOR M4 — click records and the D36 adapter are not constructed

For K2, K3 and equation (11), a mode or selected bit is a coordinate in a
mathematical atom.  D37 does not construct an immutable typed arbitration
record, transaction identity, base-version binding, authenticated envelope or
append-only adapter into D36.  The paper concedes that an implementation must
append those outcomes before D36 executes them, but elsewhere calls the
coordinates durable recorded clicks and treats the randomness monopoly as
closed.

The measure-first statement that there is no second hidden lottery is sound.
The record bridge is not yet receipt-established.

**Required repair:** call these click-labeled output coordinates and preserve
the D36 append adapter as an explicit obligation, or implement and gate the
typed record bridge.

## 9. MAJOR M5 — S2 does not perform its advertised ratio checks

`forcing_checks()` increments `ratio_checks` while multiplying the supplied
activity along one sorted reconstruction path.  It never evaluates or asserts

```text
dist[candidate] / dist[current] == activity.
```

The reconstructed weights are then compared with `hard_core()`, which was
built from the same activity formula.  Theorem 1 is correct, but the printed
`single_flip_ratio_checks=30` are 30 traversed feasible additions, not 30
measured probability-ratio identities and not 30 independent ratios.

**Required repair:** compare the exact `Fraction` ratio at every declared
addition, define the census, assert its expected value and replace
“independent” with the exact coverage term.  Regenerate all hashes.

## 10. MINOR m1 — the result is a construction, not a full classification

The paper constructs K3, K2, finite marked K1 and one joint mode family, and
conditionally characterizes K3 under fixed feasible-addition odds.  It does
not classify every regional specification satisfying the broad admissibility
axioms.

**Required repair:** say “constructs representative admitted families and
characterizes K3 at the stated premise width,” unless an exhaustive
classification theorem is added.

## 11. MINOR m2 — the infinite theorem is pairwise-graph only

D36 preserves the possibility of general forbidden hyperedges, including
three-way-only constraints.  Paper 26 defines and proves completion only for
pairwise conflict graphs.

**Required repair:** state “supplied countable locally finite pairwise
conflict graph” wherever Theorem 3's scope is summarized.  Do not let
“opportunity complex” imply the retained hypergraph case.

## 12. MINOR m3 — kernel domain needs an admitted-subshift definition

The receipt conditions only on extendable positive-mass exteriors.  The
countable proof works naturally on the compact admitted configuration
subshift, but the paper's abstract specification notation can be read as
defining a kernel for every nominal boundary.

**Required repair:** define the specification relative to the admitted compact
state space, or explicitly assign proper kernels on inadmissible boundaries.

## 13. MINOR m4 — finite-cover evidence is only a path sanity check

S5 projects three already supplied global joints on the three-path and checks
pairwise overlap equality.  It does not reconstruct a joint from regional
kernels and does not enumerate covers on every registered graph.  Paper §7.1
mostly states this correctly, but the D37 pin/note says the receipt will
recover the finite completion.

**Required repair:** narrow the receipt description to three-path marginal
descent, or implement an actual regional-to-joint reconstruction and
extendability gate at the claimed coverage.

## 14. MINOR m5 — advertised coverage is not fully fail-closed

Several gates require only positive counts.  A coverage regression could
drop a graph, region, parameter point or cover family while retaining
`PASS 9/9`, provided at least one check remained.  The frozen source currently
executes the printed loops, and the hashes make a silent change visible, but
the receipt's promise that every gate fails closed is stronger.

**Required repair:** assert the exact expected census or independently assert
the complete registered graph/region/parameter coverage for S1, S3--S6.

## 15. MINOR m6 — Q mode values are marginals, not standalone conditionals

The `34/93,25/93,34/93` and `6/31` values are unconditional Q marginals of
one normalized joint table at the symmetric point.  The abstract calls them
conditionals.

**Required repair:** call them “marginals of one regional conditional table.”

## 16. Nits

### n1 — Paper 15 title

Reference 1 uses the obsolete working title *From action to records without a
global clock*.  The paper's actual title is *From regional amplitudes and
instruments to recorded histories*.

### n2 — graph-theoretic path length

The registered fixtures are five- and seven-vertex paths.  Their
graph-theoretic lengths are four and six, not five and seven.

### n3 — exchange symmetry scope

The list introduced as “Across two parameter points” includes 93
BORN/TOKEN-exchange atoms.  Exchange invariance is checked only at the
equal-weight symmetric point; the second point deliberately has unequal
BORN/TOKEN weights.  Label the row accordingly.

## 17. Scope statements that pass

1. The exact K1 and joint-mode headline numbers are correct.
2. Theorem 1's probability statement is correct after the prior Markov repair.
3. K2 progress survives as an independent-plus-dominating conditional law at
   its radius-two boundary.
4. The countable completion proof establishes existence at the admitted
   locally finite pairwise conflict-graph scope and does not claim uniqueness.
5. Pairwise overlap agreement is correctly shown insufficient for a triple
   joint.
6. K1's infinite quasilocal completion remains open.
7. Activities, mode weights, birth couplings and completion phase remain
   unselected.
8. The action bridge and generated opportunity law remain open.
9. The D23 join-identifiability and D31/D32 cancellation limitations are
   accurately preregistered.
10. No quantum regional specification, Lorentzian geometry, universal birth
    rate or universal coordinator is claimed.

## 18. Disposition and required order

```text
B  blockers  1
M  majors    5
m  minors    6
n  nits      3
```

The probability core is worth preserving.  The next repair must begin with
B1: either build the typed causal carrier Paper 26 claims, or narrow the paper
to the conflict-graph object actually executed.  Receipt-strength and wording
repairs follow only after that decision.  A focused independent closing delta
is required after repair; the current review does not authorize promotion.
