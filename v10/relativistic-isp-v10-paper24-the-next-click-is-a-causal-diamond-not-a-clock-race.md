# Relativistic ISP v10 paper 24

# The next click is a causal diamond, not a clock race

## A time-free local probability law, an executable rooted universe and the missing overlap principle

**Status:** paper draft after terminal D35; independent paper-level hostile
review pending.
**Date:** 2026-07-14.

## Abstract

SHARD needs probabilities for the next record on A without assuming a global
commit clock or attaching a numerical proper-time process to every record.
The first question is causal, not metric.  A2 is A1's first successor on A's
record wire.  A remote datum reaches A2 exactly when a finite chain of locally
licensed record transfers lies in A2's newly acquired causal past.  In a
realized history reach is binary.  Before A2 exists, its probability is the
measure of completed causal diamonds containing that transfer chain.

We audit 441 pre-D35 V1--V10 primary papers and notes and separate three layers
that the earlier program sometimes conflated: the causal grammar of allowed
extensions, the probability of selecting an extension, and the conditional
quantum content map once it is selected.  D24 already supplies an exact
one-parent newborn-content isometry `B_g`; it does not select the birth
opportunity probability, the coupling g, a root or an interaction graph.

We then construct and execute a supplied A-rooted nested-call family.  A local
actor may idle, create one D24 child, query one owned child or query two.
Queries move strictly outward on a finite ownership tree and returns move
inward.  A2 is the upper seal.  No elapsed time, rate or global opportunity
normalizer occurs.  Exact local normalization proves finite termination and
construction-order covariance.  Countable iteration gives a completed
classical rooted-history measure.

The terminal implementation is a logical actor/mailbox simulator with
actor-owned tips, ports, issued calls and causal ordinals.  FIFO, LIFO and
canonical mailbox servicing give the same 16 physical histories.  The
complete first law is the exact marginal of 408 second-call refinements.
Supplied and generated event/actor identities inhabit disjoint types, so even
adversarial display-name collisions leave the physical law unchanged.

A bit sealed only at D supplies the operational test.  Six of 16 histories
contain `A -> B -> D`; ten do not.  Paired `do(D=0)`/`do(D=1)` histories have
the same support and probability, while the durable A2 datum changes exactly
on the six queried histories.  The exact reach probability is `1/16` in Q1
and `3/40` in Q2.  An isomorphic disconnected source gadget never changes A.

At the degree-two root, idle, birth, two visits and fork are embedded on one
eight-dimensional input and one 48-dimensional classical-output direct sum.
All five self Grams are identities, all ten cross Grams vanish, and the
probability-weighted Gram sum is exactly the identity.  The D24 birth instant
remains exact.

The result is positive but nonselecting.  Q1 and Q2 pass every causal,
projective, actor, evidence and quantum gate while disagreeing on birth,
visit and causal reach.  Therefore the inherited SHARD/ISP, sealing, diamond,
NSE and profinite principles do not yet determine nature's numerical birth or
interaction law.  The terminal result is a **TIMELESS ROOTED NESTED-CALL
FAMILY / EXECUTABLE**, not a root-free universe law.

The missing object is now precise: an overlap-consistent local specification
on all finite causal diamonds.  Larger and smaller diamond kernels, and two
overlapping peer-initiated diamonds, must induce the same law on their common
region.  Such a family could define a global history measure without a global
next-event race or per-record proper times.  The present laminar construction
is its first solved special case.

## 1. The answer in ordinary language

The investigation changes the picture in four ways.

First, “does B's evidence reach A before A's next click?” does not require a
number of seconds.  A's next click is simply the next record on A's own chain.
Evidence reaches it if the completed history contains an allowed chain of
hand-offs ending at that new A record.

Second, evidence does not arrive with a fractional probability after the
history has occurred.  In one realized history it either arrived or it did
not.  Probability describes our law over the different complete causal
diamonds that could become A's next update.

Third, record birth has two distinct questions:

```text
Does a birth opportunity occur?        q_birth
What quantum content does the child receive once it occurs?   B_g
```

D24 answered the second question for one exact family.  It did not answer the
first or choose g.

Fourth, we can simulate a real mathematical system of local actors without
making the computer's service order physical.  The code uses actor objects and
mailboxes, but it runs in one Python process and evaluates the entangled
carrier in one shared exact vector.  This is a logical actor simulation, not a
claim that the universe consists of operating-system threads or that an
entangled state factors into separate local wavefunctions.

The construction works completely for a supplied A-rooted tree of nested
calls.  It does not yet make a universe in which any actor can initiate an
overlapping transaction.  That remaining distinction is the main result, not
fine print.

## 2. What the corpus already forced

### 2.1 Audit boundary

D35's deterministic inventory content-hashes all 441 primary papers and notes
present in V1--V10 before D35.  Of these, 427 meet at least one registered
causal/birth/time/history/simulation category.  The corpus stream is

```text
b0e4c7e0be1c8587b5f3b35e36a834fa8f485cf4bd7cfbb61331017bcd1541b7.
```

The audit corrects an earlier selector that accidentally omitted four
historical Paper 24 files in V3, V4, V6 and V7.  The inventory is a
completeness and forgetting control, not an automated semantic proof.  The
following synthesis is taken from the terminal results of those artifacts and
their hostile reviews.

### 2.2 Stable inheritance

The V1--V10 record supports these conclusions:

1. finite sealed records constrain evidence and admissible maps but do not by
   themselves select a variable-support history law;
2. sealed holonomy can reconstruct or coordinate a supplied positive law but
   does not generate the first carrier or choose extension weights;
3. causal diamonds sew supplied interfaces and make influence operational,
   but diamond composition is not record birth;
4. a complete primitive history measure would already answer every next-click
   conditional, but SHARD has not derived or uniquely posited that measure;
5. construction order of incomparable events is gauge, while record-wire
   succession is physical causal order;
6. profinite finite-stem machinery can preserve compatible finite laws but
   cannot select one or repair incompatible restrictions;
7. D24 supplies an exact one-parent birth-content family, D25/D27 place it
   inside a broader distinguishability-isometric reception class, and D28
   leaves the opportunity kernel open;
8. D31 excludes a stationary, covariant, diamond-forming graph-blind kernel on
   unbounded growth, pushing any serious selector toward local graph/collar
   structure;
9. D34f/Paper 23 proves that exact complete durable-ancestry prediction under
   the chosen D34b law can require A's whole connected component; and
10. none of those results supplies the full root-free interactive history law.

### 2.3 The foundational separation

For an extension opportunity o at a finite marked history H, write

```text
q(o | H)       probability that this structural opportunity is selected;
B_o(dr | H)    conditional content/reception kernel after selection.
```

Confusing q with B created much of the apparent birth paradox.  A perfect
description of what a newborn receives does not say whether a newborn appears.
Likewise, a causal rule saying which histories are legal does not assign their
relative probabilities.

## 3. Histories without a numerical time

### 3.1 Primitive finite object

A finite marked record history H contains:

```text
immutable events and their directed ancestry;
the linearly ordered wire of each record/actor;
current wire tips;
typed local operation marks and target roles;
birth parentage and active support;
sealed evidence references and bounded payloads.
```

There is no real-valued time coordinate.  The ancestry relation is acyclic and
locally finite.  Each record wire is linearly ordered by its own successive
records.  Events on unrelated branches may remain incomparable.

A completed history is a compatible infinite or terminal extension of these
finite objects.  A probability law may be given by consistent cylinder
probabilities on finite marked histories.  A sequential computer program is
only one sampler of that law.  Its integer loop index and its chosen linear
extension are not physical time.

### 3.2 “Next A”

Let A1 be A's current event.  In a completed history, A2 is the first strict
successor of A1 on A's record wire.  This definition uses order but no duration.

Define A's newly acquired causal past as

```text
NewPast_A(A1,A2) = Anc(A2) minus Anc(A1).
```

A record e can be new evidence at A2 only if it lies in this difference and is
connected to A2 by the declared local transfer grammar.  Mere statistical
correlation, nominal graph distance, a common older cause or earlier computer
processing is not acquisition.

### 3.3 The causal acquisition principle

The **Causal Acquisition Principle (CAP)** is:

> A2 can acquire a datum only through a finite sequence of locally licensed
> adjacent transfers whose persistent records lie in A2's newly acquired
> causal past.  Every accepted transfer is typed, bound to its source and
> consumed by the upper record.  Disconnected and unqueried sources cannot
> change the A2 record law.

CAP has a structural and an operational row.  Structural ancestry says that a
record lies in the new past.  Operational influence additionally requires an
intervention on a declared datum at the source to change a declared A2
observable.  The two must not be conflated.

### 3.4 Probability of reaching A

If mu is a completed-history law and H0 is the present finite history, then

```text
P(e reaches A2 | H0)
  = mu({H extends H0: e enters A2 through a licensed path})
    / mu({H extends H0}).
```

There is no random “amount of arrival” inside one H.  The event in braces is a
set of completed histories.  If mu were primitive, this conditional would
already be part of the rulebook.  SHARD's harder derivation problem is to
construct or select mu from its record principles.

## 4. The local call-diamond construction

### 4.1 Why an operational diamond

Spacetime geometry is not assumed, so “causal diamond” here is operational.
Its lower seal is A1, its interior is a finite tree of adjacent queries and
returns, and its upper seal is A2.  It is not yet a Lorentzian interval or a
geometric light cone.

The initial specimen has the supplied ownership tree

```text
A -> {B,C}
B -> {D}.
```

Each actor owns its current record tip and typed child ports.

### 4.2 Local menu

When queried, actor v chooses one normalized local alternative:

```text
idle    seal one new v record and return it;
birth   create one fresh D24 child, seal the joint record and return it;
visit   query one existing child, then seal the returned evidence;
fork    query two distinct existing children, then seal both returns.
```

The choice uses only v's owned ports and the supplied parameter cell.  If v
has too few children for visit or fork, that unavailable mass is assigned to
idle.  There is no normalization over every ready actor in the universe.

Queries move strictly to children.  A newborn is not queried in the call that
creates it.  Returns move inward and bind the exact issued child call.  A2 is
created only after every selected return is present.

### 4.3 Finite-call theorem

**Theorem 1.** Every call on a finite rooted ownership tree terminates after
finitely many local cells, without a duration or subcritical-rate assumption.

**Proof.** Induct on subtree height.  A leaf can only idle or birth after
unavailable query mass is folded into idle; both close immediately.  At a
nonleaf, idle/birth close immediately.  Visit/fork call one or two strict child
subtrees, which close by induction, and then one local merge closes the parent.
A newborn is outside the current recursion.  Therefore the root returns after
finitely many cells.  ∎

At most one event and one newborn per queried actor are created in a call.
Every finite call therefore preserves finite support and local finiteness.

### 4.4 Exact local probability

Let

```text
q = (q_idle,q_birth,q_visit,q_fork),  sum q = 1.
```

For a completed call diamond D,

```text
P(D | H,A1)
  = product over queried actors v of
      q(action at v) / number of selected v-local port sets.
```

All factors are local.  Scalar factors from incomparable child branches
commute.  The local quantum gates on disjoint children commute, and the two
fork rotations share only a control while acting on distinct targets.  Thus
every machine linear extension of the same marked call DAG has the same
weight and carrier output.

### 4.5 Construction-order theorem

**Theorem 2.** Within the strict rooted nested-call grammar, FIFO, LIFO and any
other fair service order of ready incomparable mailboxes are presentation
gauge.

**Proof.** The finite-call proof supplies termination.  Every completed marked
call has the same set of local factors regardless of service order.  Swapping
two incomparable ready messages only permutes scalar factors and commuting
local operations.  Authenticated return slots force the same parent merge.
Therefore the canonical physical history and its probability are invariant.
∎

This theorem is not extended to overlapping peer calls, where two operations
may contend for the same held lower tip.

## 5. Record birth

### 5.1 What D24 gives

On the selected birth alternative, D24 supplies:

```text
a fresh child initialized in |0>;
a one-parent controlled rotation with coupling g;
an isometric parent-to-parent+child map;
exact P(child=1) = g P(parent=1) at the birth instant;
construction-order covariance on rooted trees.
```

This is an exact admitted newborn-content kernel.  It respects the D25/D27
distinguishability/no-silent-erasure ceiling.

### 5.2 What D24 does not give

D24 does not select:

```text
q_birth;
g;
which parent/collar has an opportunity;
the root or ownership orientation;
peer, cycle, bridge or disconnected-join sectors.
```

Calling D24 “the birth law” without this qualification would hide the central
missing physics.

### 5.3 Exact nonselection cells

The investigation freezes two complete cells:

```text
Q1 = (3/8,2/8,2/8,1/8), birth g=9/25;
Q2 = (4/10,2/10,3/10,1/10), birth g=16/25.
```

Both pass every terminal gate, but

```text
P_Q1(A2 is birth)=1/4;
P_Q2(A2 is birth)=1/5.
```

Therefore the current principles do not select a unique birth opportunity or
coupling.

## 6. The common-input quantum instrument

The root initially carries three qubits, A, B and C, so its common input has
dimension eight.  The five local alternatives are:

```text
idle;
birth;
visit B;
visit C;
fork B and C.
```

Idle acts identically on A/B/C.  Each visit applies the controlled rotation to
its named target and identity to the spectator.  Fork applies both rotations.
Birth uses the same input and adds a fresh child, producing a 16-dimensional
output sector.  The other four outputs have dimension eight.  Orthogonal
classical-output injections therefore give total dimension

```text
16 + 8 + 8 + 8 + 8 = 48.
```

Writing V_o for the common-input isometry and J_o for its output-sector
injection, the exact receipt proves

```text
V_o^dag V_o = I_8                         for all five o;
(J_o V_o)^dag (J_p V_p) = 0               for all ten o != p pairs;
sum_o q_o (J_o V_o)^dag(J_o V_o) = I_8.
```

The bounded local operation alphabet has rank four: idle, birth, visit, fork.
The two visit alternatives differ by structural port incidence.  Transaction
path, actor address and persistent provenance may grow without bound and are
not misdescribed as a bounded local flag.

This earns a classical-output common-input direct-sum quantum instrument at
the registered local sector.  It does not create coherent amplitudes between
different support graphs.  Conditional on each classical support alternative,
the carrier map is isometric.

## 7. A nontrivial causal evidence experiment

### 7.1 Source and intervention

After the seed birth record `BD`, D receives one additional D-only source seal
containing a bit.  A and all other connected inputs are fixed.  The experiment
compares paired worlds under `do(D=0)` and `do(D=1)`.

Every child return explicitly carries:

```text
the result event;
the bounded output bit;
the set of source identities;
an evidence digest binding those fields;
the exact issued call to which it responds.
```

B's merge consumes D's carried return; B's return carries the merged datum to
A; A2 stores it durably.

### 7.2 Binary reach

There are 16 completed histories in each Q cell:

```text
6 query D through A -> B -> D;
10 do not query D.
```

In every paired history the action tree and probability are unchanged by the
bit intervention.  A2 differs under `do(D=0/1)` in all six queried histories
and in none of the ten unqueried histories.  The D source identity follows the
same rule.

This is a limited but genuine operational influence result.  It concerns one
declared classical datum and one supplied transport grammar.  It does not say
that every ancestor can signal, that entanglement alone is a message, or that
correlation through an older common cause is acquisition.

### 7.3 Exact reach probabilities

At root A, a visit chooses B or C uniformly.  At B the only child is D.  D is
therefore reached either when A visits B and B visits D, or when A forks to B
and C and B visits D:

```text
P(D reaches A2)
  = (q_visit(A)/2) q_visit(B) + q_fork(A) q_visit(B).
```

For Q1:

```text
(1/4)/2 * (1/4) + (1/8)(1/4)
  = 1/32 + 1/32
  = 1/16.
```

For Q2:

```text
(3/10)/2 * (3/10) + (1/10)(3/10)
  = 9/200 + 6/200
  = 3/40.
```

The same causal criterion selects the counted histories in both cells, but
the probabilities differ.  This cleanly separates causal admissibility from
numerical dynamics.

### 7.4 Disconnected control

The disconnected control contains an exact marked copy of D's source ancestry:
one seed actor event, two successive one-parent seed births and a final source
seal.  It is relabeled into a disjoint typed control domain and has no edge or
event incidence with A's component.

Changing the disconnected bit leaves both A's projected law and the complete
connected 16-atom distribution exactly fixed.  The result is locality by
factorization, not by a large graph distance; no spatial metric exists.

## 8. What the simulation actually is

### 8.1 Logical actors

Each connected actor object owns:

```text
its structural address and current tip;
typed child ports and reciprocal edge data;
its mailbox;
the exact incoming calls issued to it;
used calls and outstanding child-return slots;
its bounded carried evidence state;
for A, its own causal call ordinal.
```

An unissued lookalike cannot act.  The full local option and all identities
validate before the call token is consumed or a durable transfer is written.
Mailbox service peeks first and acknowledges only after success.  Invalid root
inputs reject before any state mutation.

### 8.2 Typed identity and covariance

Raw names are display gauge.  Storage identities inhabit disjoint types:

```text
supplied actors;
generated actors indexed by component, A-call ordinal and causal path;
supplied events;
generated events indexed the same way;
disconnected controls.
```

Consequently a supplied event may be displayed using the printable string of
a future generated event without collision.  Exact tests cover immediate
call-one collision, delayed call-five collision and a supplied actor displayed
as the future root-newborn string.  Ordinary actor/event alpha renaming and
all collision cases preserve the physical law.

### 8.3 Shared exact state

The simulator stores one persistent event DAG and one exact joint carrier
vector.  This is not a hidden global probability normalizer: local action
probabilities do not compare spacelike opportunities.  It is a mathematical
representation of joint ancestry and entanglement.

The implementation is not a multiprocessing benchmark.  Running each actor in
an OS process would not make the law more local.  The scientific test is that
changing the serializer does not change the physical distribution and that
local transitions consult only their declared actor/collar data.  A genuinely
distributed tensor-network implementation remains a separate target.

### 8.4 Exact terminal receipt

For both Q1 and Q2:

| gate | exact result |
|---|---:|
| FIFO/LIFO/canonical histories | 16 / 16 / 16 |
| physical atoms | 16 |
| total mass | 1 |
| ordinary renamed projectivity | 16 / 408 / 408 |
| display-collision projectivity | 16 / 408 / 408 |
| delayed collision continuation | 6 / 6 calls |
| original projectivity | 16 / 408 / 408 |
| common instrument | 8 input, 48 output, 10/10 cross zero |
| closing rejection state | 6 / 6 unchanged |
| inherited rejection state | 9 / 9 unchanged |
| D queried / unqueried | 6 / 10 histories |
| adjacent return checks | 18 |
| grown scheduler checks | 32 |
| deterministic replay | 8 calls, exact equality |

The terminal source, stdout and internal-science hashes are

```text
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574
79e29b8fd5f5a294b3c2faf438ffcca45434ec78af55b4150324b9939a03f26c.
```

Independent seeds reproduce byte-identical output.  Four hostile rounds close
with three clean `0B/0M/0m/0n` terminal deltas.

## 9. Completion and memory

### 9.1 Completed rooted history

After A2 closes, use it as the lower seal of the next A-rooted call.  Every
reachable finite rooted state has a normalized finite-support next-call
kernel.  The state space is countable and discrete.  Ionescu--Tulcea therefore
gives a measure on infinite sequences of completed rooted-call states.
Persistent union maps this sequence to a locally finite event DAG.

This is an infinite classical history measure for the supplied rooted grammar,
not merely a finite trace.

### 9.2 Markov and non-Markov language

Given the complete typed simulator state and a fixed Q cell, the next rooted
call is a Markov kernel: the full current state is sufficient.  A projection
to one record's bounded contents may be non-Markov because relevant ancestry,
ports or carried evidence has been discarded.  This is the standard source of
observable memory.

No clock is required for that distinction.  “Markov” asks whether the chosen
state is sufficient for prediction; it does not mean that a record ticks at a
constant rate.

### 9.3 Relation to Paper 23

Paper 23's whole-component necessity theorem used a different law and a harder
query: exact complete ancestry under D34b with persistent unattenuated records
and no physical return limiter.  D35 supplies a selected finite call diamond
whose upper seal closes after its issued returns.  The predictive boundary is
therefore the completed call boundary for this conditional query.

There is no contradiction.  D35 changes the law by adding a return-limiting
causal protocol and asks for the contents of one selected A2, not every future
full-ancestry observable under D34b.  The result validates the user's proposed
“below-A-click” causal boundary as an analytical object, while showing that its
size and probability depend on the supplied history law.

## 10. Profinite meaning

The finite rooted-call cylinders form a projective family under forgetting
later calls.  The exact 16/408 checks are finite witnesses of this compatibility,
and the all-size completion proof supplies the classical infinite measure.

This is related to, but not identical with, the v9 profinite stem spectrum.  A
full identification would require:

```text
the construction-order quotient on every finite marked history;
explicit bonding maps across every admitted support sector;
a topology/continuity theorem;
overlap consistency for nonlaminar regions;
and, for a quantum functional, positivity and extension beyond classical mixtures.
```

Most importantly, inverse limits preserve compatible data.  They do not choose
between Q1 and Q2.  The unequal reach probabilities are an exact demonstration
of that nonselection.

## 11. Why a root-free universe is still open

### 11.1 The global-next-event trap

If one insists that exactly one actor in the whole universe must be chosen as
the next actor, its local weights must be compared and normalized across the
ready set, or one must introduce a race of clocks.  The former is global; the
latter reintroduces rate/proper-time data.

The time-free alternative is not to make global construction order physical.
Define a probability law on causal partial histories, allow incomparable local
events, and quotient the machine's linear extension.

### 11.2 Why D35 is not yet enough

D35 externally chooses A as the initiator of every completed macro-call.
Strictly nested child calls cannot overlap or contend.  This makes its
projectivity and scheduler covariance provable, but it leaves open:

```text
B and C initiating overlapping calls;
two peers trying to use the same held lower record;
cycles and repeated visits;
birth that joins previously disconnected components;
coherent alternatives with different support graphs;
and a root-free probability law over all such histories.
```

No elapsed-time variable will solve those consistency problems by itself.

### 11.3 The causal-diamond specification problem

For every finite causal region D with admissible boundary record b, seek a
normalized kernel

```text
gamma_D(interior marked history | boundary b).
```

The family must satisfy:

1. **locality:** gamma_D consults only the causal boundary/collar and inherited
   sufficient marks;
2. **restriction:** sampling a larger region and forgetting down to D agrees
   with gamma_D;
3. **overlap:** two peer regions give the same marginal on their intersection;
4. **covariance:** actor/event display names and machine linear extensions are
   gauge;
5. **variable-support quantum consistency:** births and interactions form one
   normalized positive instrument across admitted support sectors;
6. **finite local ancestry/nonexplosion:** every finite upper record has a
   finite causal past; and
7. **completion:** compatible finite laws extend to a global history measure.

The D35 rooted calls are laminar: regions are nested or disjoint, never partly
overlapping.  They solve the easiest nontrivial subfamily of this specification
problem.

### 11.4 The selection question

Even if overlap consistency admits solutions, it may leave a family.  A real
selection principle must then be identified or nature must supply empirical
parameters.  Plausible constraints inherited from the program include:

```text
NSE/distinguishability preservation;
restriction naturality and strong positivity;
diamond/holonomy composition;
stationarity or a controlled replacement for it;
local graph/collar dependence forced by D31;
channel-manifold symmetry such as the S2 many-clocks/few-factors structure;
and empirical causal-web geometry.
```

D35 proves that these principles, as currently formalized, have not yet been
combined into a uniqueness theorem.

## 12. Consequences for spacetime, cones and dimension

The investigation does not make a light cone rounder or set a dimension.  Its
current A-rooted tree is not the root-free grown causal web measured in
D28--D32.  A laminar call architecture can impose a dimension-like order
artifact unrelated to the physical many-clocks/few-factors manifold.

The correct order of work is:

1. construct or characterize overlap-consistent root-free diamond kernels;
2. prove a completed history measure and construction-order quotient;
3. grow causal webs under frozen candidate laws;
4. measure both directed influence order and circuit/wire order;
5. return to cone anisotropy, dimension, scale ladders and S2 channel symmetry;
6. only then ask how metres, seconds and G emerge.

The interactive law will affect the v9 cone and dimension results because it
determines which diamonds and causal relations are abundant.  D35 makes that
future dependency explicit but does not calculate it prematurely.

## 13. Terminal decision

The accepted result is:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE.
```

It proves that numerical proper time is not logically required to define the
probabilities of A's next record.  A completed causal-diamond law is enough.
It supplies one exact local actor realization, one operational remote-evidence
test, one variable-support quantum instrument and one completed rooted-history
measure.

It does not prove:

```text
a unique q or g;
the universal birth kernel;
a root-free initiator/overlap law;
peer, cycle, join or coherent graph-sector dynamics;
distributed storage of an entangled universal state;
the v9 stem-spectrum bridge;
Lorentzian spacetime, proper time, cone roundness, dimension, units or G;
or the actual interactive click law of nature.
```

The most pressing next investigation is the overlap-consistent causal-diamond
specification.  It is the first target that simultaneously uses whole
histories, sealed records, diamonds, local actors and profinite consistency
without smuggling in a global clock.

## 14. Reproducibility and review record

Primary terminal artifacts:

```text
note-d35-timeless-local-next-click-law.md
code/d35_corpus_causal_inventory.py
data/d35_corpus_causal_inventory.out
code/d35d_typed_identity_terminal_exact.py
data/d35d_typed_identity_terminal_exact.out
```

The rejected D35a/D35b and provisional D35c implementations remain in the
repository with their receipts.  They document, rather than erase, the
openings found by hostile review:

```text
central continuation state;
unissued calls and stale returns;
ephemeral transport routes;
metadata-only quantum flags;
root self-copy masquerading as remote influence;
incomplete event alpha quotient;
raw fresh-name collisions;
and late root-input validation.
```

Four D35 review rounds contain independent probability, locality and
birth/quantum lanes.  The terminal round closes with nine zeroes:

```text
0B/0M/0m/0n
0B/0M/0m/0n
0B/0M/0m/0n.
```

Paper-level hostile review remains required before this synthesis is terminal.

## 15. Paper-level hostile round 1

**Verdict:** terminal D35 survives; Paper 24 promotion is withheld.

```text
probability/mathematics          0B / 2M / 3m / 1n
causal interpretation            0B / 2M / 6m / 1n
birth/quantum/corpus              0B / 3M / 2m / 3n
```

Reports:

- `reviews/paper24-round1-probability-mathematics-hostile-review.md`;
- `reviews/paper24-round1-causal-interpretation-hostile-review.md`;
- `reviews/paper24-round1-birth-quantum-corpus-hostile-review.md`.

Every D35d receipt number, the D24/D27 inheritance, the 8-to-48 instrument,
D-origin pairing, disconnected control, reach probabilities and completed
rooted measure reproduce independently.  The paper nevertheless contains
four load-bearing synthesis defects and several narrower wording errors.

The frozen repairs are:

1. replace the false degree-independent branch product by the effective
   degree-dependent menu, including folded unavailable visit/fork mass;
2. withdraw the unproved predictive-boundary inference: D35 constructs a
   finite realized acquisition/stopping region while its pre-call kernel still
   conditions on the complete typed rooted state;
3. downgrade the overlap object from a precise/solved specification to a
   candidate architecture, and define the missing oriented region category,
   incoming/generated interfaces, boundary transport, kernel composition,
   coherent finite-cover joint extensions and global completion obligations;
4. restore D31's actual width: under its none-free, birth-positive,
   unbounded-growth covariance fork it forces state sensitivity richer than
   the unsealed count, not locality specifically;
5. freeze the 441-file corpus boundary at a pre-D35 git tree rather than scan
   the live folder, which now adds Paper 24 and aborts at 442 files;
6. condition the generic reach ratio on positive cylinder mass and A2
   existence, or supply a cemetery outcome;
7. restrict alpha/collision language to the declared six-event seed and
   reachable rooted grammar;
8. attribute normalization, termination and covariance to their distinct
   premises;
9. describe the eight-dimensional carrier as the root-local A/B/C sector,
   with D and other factors as identity spectators;
10. replace “rooted universe,” identify A2 as the upper seal rather than the
    whole diamond, disclose the shared evaluator wherever actor locality is
    summarized, call `output_sources` the positive-source set, and replace the
    global-normalizer/clock dichotomy by the broader statement that any one-
    next-actor rule adds global selection structure; and
11. repair `S^2` notation and the terminal review-count wording.

No code-level D35d theorem is reopened.  The corpus repair changes only the
historical audit's manifest mechanism and its source/receipt hashes; the
historical 441/427 content stream must remain byte-identical.
