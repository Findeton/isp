# Relativistic ISP v10 paper 26

# Admissible regional history specifications

## Finite-cover consistency, global completion, and birth and arbitration as conditionals

**Status:** INDEPENDENT-REVIEW REPAIR CANDIDATE.  The frozen round-one review
at commit `23a4ae0` returned `1B/5M/6m/3n`.  Its typed-carrier blocker and
listed repairs were implemented at `e3161f5`; the focused round-two delta
returned `1B/3M/4m/0n` and found K1 restriction, D26-line, D36-adapter and
countable-identity defects.  Those second-round authorship repairs are now
implemented and D37 remains `PASS 9/9`; promotion still requires a fresh
focused closing delta.
**Date:** 2026-07-14.

## Abstract

Paper 24 left a precise architecture open: normalized conditional laws on
oriented finite causal regions, with incoming and lateral boundary data,
restriction transport, coherent joints on every finite cover and a global
completion.  Paper 25 made the need operational.  Its clock-free transaction
cell safely executes a supplied selected set of overlapping attempts, but does
not supply the opportunity or arbitration law.  Raw restriction changes K1's
probabilities, K1 and K2 disagree on a three-attempt path, and pairwise overlap
agreement does not guarantee a joint law.

This paper constructs representative admitted classical regional-history
families and characterizes K3 at an explicit premise width.  The primitive
object is not a global next-event lottery.  It is a family
`gamma_D(.|b_D)` of conditional kernels on finite typed opportunity regions,
together with deterministic causal realization maps `F_D` for K3, K2 and the
joint birth/arbitration family.  Their pushforwards
`Gamma_D=(F_D)_*gamma_D` are laws on immutable typed event DAGs.  K1's finite
marked probability specification and complete-carrier typed atoms are
retained, but a causal-parent-closed restriction transport for proper K1
subregions is not claimed.
Properness, normalization and nested composition give a
Dobrushin--Lanford--Ruelle-style specification relative to an admitted compact
configuration space.  A global law is any measure `mu` satisfying
`mu gamma_D=mu` for every finite region.  Specification consistency, a
finite-range Gibbs representation and existence or uniqueness of a global
measure are kept as three separate statements.

On the D36 conflict cells, the feasible-support hard-core family K3 passes
`508` intrinsic conditional checks, `7,098` nested DLR towers and `138`
boundary-mixture checks at two activities.  Exact positive feasible support
and fixed feasible-addition odds force the global finite law to have
vertex-activity hard-core form.  The resulting K3 kernel separately has an
accepted one-hop Markov boundary.  Overlap consistency alone does not force
either the support or the numerical odds.

Progress is not excluded.  K2's uniform maximal-feasible-set law is the
explicit hard constraint “independent and dominating.”  Once its radius-two
boundary carries accepted blockers and unmet exterior domination demands, it
passes `188` conditional checks over `165` boundaries and `1,224` DLR towers.
K1 also has a finite marked specification when its component priority click
is retained, but it is not one-hop output-local.  A path-five witness gives
two exteriors with the same empty accepted collar and different local laws:
`{A}:5/11,{B}:6/11` versus `{B}:1`.  No infinite quasilocal completion is
claimed for K1.

A single joint finite functional now carries opportunity mode and arbitration:
each role is `NO_BIRTH`, `TOKEN` or `BORN`, and each present proposal has a
recorded selected/rejected click.  Its typed realization distinguishes an
actual `BORN_CARRIER` from activation of an explicit pre-existing
`DORMANT_TOKEN`.  At one symmetric path point its marginals give
`P_Q(BORN)=P_Q(TOKEN)=34/93`, `P_Q(NO_BIRTH)=25/93` and
`P_Q(selected)=6/31`.  These are marginals of one regional conditional table,
not sequential coins.  They remain unselected coupling-dependent numbers.
D24 supplies the newborn isometry only on the BORN branch; D26 makes that
branch observable on the represented parent line.  At `g=9/25`, one BORN
contributes coherence factor `4/5`, three same-line births contribute
`64/125`, and the joint Q marginal predicts `431/465` relative to the
coherence-neutral TOKEN control.

For K3, K2 and the joint birth/arbitration family, a compactness argument gives
at least one compatible global classical measure on every supplied countable
locally finite pairwise conflict graph at the stated finite-range scope.  Its
typed causal-core pushforward through the recorded selection clicks gives the
corresponding history law on the supplied carrier.  The exact imported D36b
append adapter is a separately audited finite interface; its locked SHA-based
evidence identities are not promoted to a countable injectivity claim.
Uniqueness is not proved and need not hold.  The result unifies D33--D34's
missing untimed regional measure architecture with D35--D36's missing
opportunity-and-arbitration object, but it does not generate the opportunity
carrier, select its activities or mode weights, derive them from the action,
or provide a quantum join.

The accepted candidate noun is therefore:

```text
CLASSICAL TYPED CAUSAL REGIONAL SPECIFICATION FAMILY /
FINITE SPECIFICATION AND COUNTABLE LOCALLY FINITE PAIRWISE-CONFLICT COMPLETION /
SUPPLIED OPPORTUNITY CARRIER AND COUPLINGS /
NONSELECTING.
```

## 1. The answer in ordinary language

Paper 25 supplied a reliable local machine.  Give it a finite set of
transaction attempts and a compatible selected subset, and its actors can
reserve exact record versions, reject conflicts immediately, commit or abort,
apply locally and close an append-only causal diamond without a numerical
clock.

That does not yet make a universe law.  Different regions may see overlapping
pieces of the same contenders.  A local probability assignment must know what
the boundary already blocks, must agree with every larger-region law after the
larger exterior is averaged, and must belong to one positive joint on every
finite cover.  Pairwise matching is not enough.

The missing object is a conditional regional law.  It says:

```text
given these typed incoming and lateral boundary records,
what immutable event DAG occurs inside this finite causal region?
```

The same object answers two questions that were previously written as
separate kernels:

```text
which candidate carriers occur?       opportunity / birth mode;
which compatible carriers succeed?    arbitration.
```

It does not need to choose one actor as the globally next actor.  Incomparable
regional events remain incomparable in the represented event poset; all 70
linear-extension serializations of the D33 test history validate the same
immutable DAG and produce one canonical digest, while comparable events
sharing one wire stay ordered.  This is a serialization-gauge gate, not a
second actor-operation replay theorem.

The paper's main negative result is equally important.  Regional consistency
does not select one numerical family.  It admits at least a nonprogressing
hard-core family and a progressing maximal-set family.  A recorded-priority
greedy family also survives finitely but requires wider boundary data.  The
law of nature would still need to select or identify the surviving couplings
and, possibly, a completion phase.

## 2. The queued problem

### 2.1 Paper 24's composition law

For a finite oriented causal region `D`, Paper 24 proposed the following
ingredients:

```text
B_D        admissible incoming and lateral boundary data;
Omega_D    admitted marked interior histories and generated outputs;
beta_D     boundary extraction;
r_E,D      restriction/transport from a larger region E to D;
gamma_D    normalized kernel B_D -> Prob(Omega_D).
```

When `D` lies in `E`, the boundary seen by `D` can be random after `E\D` is
generated.  Therefore restriction has the conditional-mixture form

```text
(r_E,D)_* gamma_E(. | b_E)
  = integral gamma_D(. | b_D) nu_E->D(db_D | b_E).          (1)
```

Paper 24 did not define the region category, the transport kernel or a global
completion.  Its rooted call family was laminar and could not test partially
overlapping peer regions.

### 2.2 Paper 25's exact stress tests

Paper 25 supplied the missing finite conflict cells and three decisive gates.

First, raw K1 restriction fails on the path `P-Q-R`:

```text
larger path restricted to P-Q   P:2/3, Q:1/3;
direct P-Q law                  P:1/2, Q:1/2.
```

Second, two progressing covariant laws disagree on that path:

```text
                         {Q}      {P,R}
K1 random priority       1/3       2/3
K2 uniform maximal       1/2       1/2.
```

Third, three pairwise anticorrelation laws can have matching singleton
marginals while no triple assignment satisfies all three.  Any architecture
that checks only pairwise overlap is incomplete.

### 2.3 The two open lines are one

D34b constructed one chosen timed Harris history measure, but withdrew the
claim that its untimed typed-DAG shadows already formed an intrinsic
projective/profinite system.  D35 and D36 independently left opportunity and
peer arbitration open.

The regional conditional `gamma_D(.|b_D)` is the common missing type:

```text
D33--D34   asks how finite untimed restrictions belong to one history law;
D35--D36   asks how local opportunity and arbitration laws agree on overlaps.
```

Paper 26 does not prove that the chosen D34b law is one of the specifications
constructed here.  It supplies the architecture that both lines were missing.

## 3. Regional specifications

### 3.1 Supplied typed opportunity carrier

The exact classical carrier begins with a supplied typed opportunity carrier

```text
C = (V, E_conf, Part, parentLine, proposalType).
```

`V` contains structurally identified opportunity roles.  `E_conf` records
pairwise incompatibility.  `Part(v)` is the ordered participant tuple,
`parentLine(v)` identifies the supplied causal line that offers the
opportunity, and `proposalType(v)` is its typed record role.  Participant
intersection re-derives `E_conf`; the separately declared conflict graph is
cross-checked rather than described as a single source.  A finite region `D`
includes its finite role set, exact participant-base identities, distinct
typed opportunity-parent identities and every incident lateral proposal.

The word “supplied” is load-bearing.  D37 assigns modes and outcomes to this
carrier; it does not derive which opportunity roles exist or generate their
causal incidence.

The receipt registers eight finite graphs with 28 roles, 19 conflict edges and
196 nonempty regions.  Five reproduce D36-defined conflict fixtures: its four
coordination cells (pair, triangle, disjoint and partial overlap) and the
three-proposal path used to separate K1 from K2.  A two-edge disjoint union is
kept separately for factorization, and five- and seven-vertex paths test
boundary width.

Thirty-eight oriented interface rows make the causal words executable.  For
each region they carry:

```text
incoming     exact participant-base records and one distinct typed parent per proposal;
lateral      exterior proposals sharing a participant with the region;
generated    one mode click and one selection click per interior proposal.
```

S0 checks the content of all 38 rows fail-closed, not merely their count or
hash.  It also realizes six complete fixture histories containing 104 typed
events and 19 signed D36 `PREPARE` envelopes.  Seven negative mutations are
all rejected: a missing parent, duplicate mode branch, forged attempt, forged
signature, wrong K1 priority result, conflicting selection and cross-proposal
TOKEN ancestry.

Mathematical role labels are cylinder coordinates, not dormant physical
records.  Relabeling transports the complete structure and law.  `NO_BIRTH`
at a coordinate does not secretly install a TOKEN there.

### 3.2 Typed causal realization

A regional atom is not itself passed to D36.  A deterministic realization map

```text
F_D : (boundary, mode, arbitration mark, selected set) -> H_D              (F)
```

constructs an immutable event DAG `H_D`.  Every theorem-level event identity
is an injective tagged canonical tuple of its finite typed content.  SHA-256 is
used only as a finite receipt/serialization checksum, never as the identity
space in the countable theorem.  Every event also has a type, owner, wire, at
most two causal parents and typed payload.  The legal
event vocabulary and immediate ancestry are:

```text
BASE_RECORD          root for one participant version;
OPPORTUNITY_PARENT   distinct typed supplied parent record, chained when a
                     fixture declares a common parent line;
DORMANT_TOKEN        explicit pre-existing coherence-neutral support root;
MODE_CLICK           <- opportunity parent, and dormant token exactly for TOKEN;
BORN_CARRIER         <- BORN mode click;
TOKEN_ACTIVATION     <- TOKEN mode click;
PRIORITY_CLICK       root carrying one complete K1 component order;
SELECTION_CLICK      <- mode/carrier and, for K1, priority click;
D36_PREPARE          <- selected click plus exact participant base.
```

Legality rejects missing parents, cycles, same-wire incomparable records,
conflicting selections, mode/carrier mismatches and incomplete click coverage.
K1 additionally recomputes greedy selection from the recorded component order.
Every selected proposal generates one authenticated D36b `Record`/`Envelope`
pair per participant, and D36b's `participant_accepts_prepare()` accepts it
before the corresponding `D36_PREPARE` event is credited.  Its
structural-attempt key is exactly

```text
attempt = H(carrier_record_id, body_digest),
```

and the signed envelope binds that attempt, carrier, body, participant,
base-record version zero, route capability, sender/target roles, selected
click and application code.  Its authenticated tuple uses D36b's exact
`PREPARE` field order and signature formula: sender kind `T`, target kind `P`,
injectively encoded arbitrary-precision integer actor indices for the structural proposal and
participant labels, blank response record, carrier as evidence and application
code zero.  These indices are identities, not admission ordinals.  Thus the
adapter uses D36's repaired carrier-derived attempt rather than a global
ordinal.

For K3, K2 and equation (11), the history law is the pushforward

```text
Gamma_D = (F_D)_* gamma_D.                                            (P)
```

Causal restriction keeps exactly the events whose proposals and participant
bases lie in the retained component, plus a component priority click only when
its whole component is retained.  On the registered disjoint carrier the two
typed restrictions equal the independently realized left and right histories
event-for-event.  This is the executable restriction square behind the
probability-level factorization; no claim is made here for a generated random
opportunity carrier.  Proper K1 subregions are excluded from this typed
restriction statement: deleting the exterior of a connected priority
component would orphan retained selection clicks unless a separate typed
priority-boundary transport were constructed.

### 3.3 Kernel axioms

For each supplied carrier let `X_C` be the admitted compact configuration
space: the closed subshift satisfying the applicable local support constraints
(feasibility for K3 and the joint family, independence plus domination for K2,
and the declared marked support for finite K1).  Kernels are defined relative
to `X_C` and only on boundary cylinders induced by `X_C`; no probability is
silently assigned to a nominal but globally inadmissible exterior.

Extend each regional kernel to `X_C` by holding the exterior fixed.  For
finite regions `D` and `E`, require:

```text
normalization     gamma_D 1 = 1;
properness        exterior observables are unchanged;
composition       gamma_E gamma_D = gamma_E,  D subset E.   (2)
```

Equation (2) says that sampling the larger region and then consistently
resampling a smaller region does not change the larger conditional law.  In a
finite system this is equivalent to the conditional tower identity when the
kernels come from one joint distribution.

A probability measure `mu` is compatible when

```text
mu gamma_D = mu                                      (3)
```

for every finite `D`.  Write the compatible set as

```text
G(gamma) = {mu : equation (3) holds for every finite D}.    (4)
```

The same identities lift to `Gamma_D` whenever the realization maps commute
with the declared causal restriction.  D37 gates that commutation on the
typed disjoint-component fixture and separately gates probability towers on
all registered finite kernels.

### 3.4 Three claims that must not be conflated

A specification is a consistent family of conditional kernels.  It need not
automatically have a declared finite-range potential representation.  Even
when it does, the existence and uniqueness of a compatible infinite-volume
measure are further questions.

Paper 26 therefore separates:

1. **specification:** equations (1)--(2);
2. **representation:** a local factor or Gibbs form under explicit support and
   Markov hypotheses;
3. **completion:** nonemptiness, multiplicity or uniqueness of `G(gamma)`.

This separation is what makes a family theorem honest.

## 4. K3 and the finite forcing theorem

### 4.1 Hard-core regional law

Let `x_v in {0,1}` record whether opportunity `v` is selected.  Feasibility is

```text
x_u x_v = 0 for every conflict edge {u,v}.
```

For positive activities `lambda_v`, define

```text
mu_K3(x) = Z^-1 1[x feasible] product_v lambda_v^x_v.       (5)
```

For a finite region `D` and exterior configuration `eta`, the intrinsic
kernel uses the same product over `D` and rejects any local selection blocked
by an accepted exterior neighbor.  Its boundary is therefore exactly the
accepted one-hop conflict collar.

The rejected symbol is safe: changing any selected vertex to rejected cannot
violate feasibility.  K3 permits the empty and nonmaximal sets, so it is a
statistical regional law rather than a progress protocol.

### 4.2 Forcing theorem at its exact width

**Theorem 1.**  On a finite conflict graph, suppose a binary law:

1. has exactly the feasible configurations as positive support;
2. has fixed feasible-addition odds: for every feasible `x` not containing
   `v` for which `x union {v}` is feasible,

```text
mu(x union {v}) / mu(x) = lambda_v.                         (6)
```

Then the law is exactly (5).

**Proof.**  Every feasible selected set can be reduced to the empty set by
deleting selected vertices.  Reversing that path adds only vertices with no
selected neighbor.  Equation (6) therefore gives

```text
mu(x) / mu(0) = product_(v:x_v=1) lambda_v.
```

The value is independent of deletion order because multiplication commutes.
Normalization gives (5).  ∎

Equation (6) is equivalently the full-exterior one-site conditional-odds
statement on positive feasible support.  A separate Markov premise is not
used: context independence already supplies the ratio needed by the proof.
K3's accepted one-hop Markov boundary remains a separately checked locality
property of its regional kernel.

The theorem does not say overlap consistency alone forces K3.  D37 retains a
context-sensitive feasible-support control whose unblocked odds take values
two and four.  It is not misclassified.  Covariance identifies activities
only across declared structural orbits; it does not choose their values.

### 4.3 Exact receipt

Across the pair, path, triangle, disjoint, partial-overlap and path-five cells,
at activities one and two, D37 reports:

```text
intrinsic regional conditionals       508
nested DLR tower checks              7,098
boundary-mixture checks                138
disconnected factorization               1
```

Thirty traversed feasible additions each directly satisfy the exact `Fraction`
identity `mu(x union {v})/mu(x)=lambda_v`; those ratios reconstruct 25
registered global states exactly.  S2 asserts the expected census and the
ratio itself, rather than merely multiplying a supplied activity along a
reconstruction path.

## 5. K2: progress survives regional consistency

### 5.1 Maximal feasible support

K2 is uniform on maximal feasible sets.  A selected configuration is maximal
exactly when it obeys two local constraints:

```text
independence   no adjacent vertices are selected;
domination     every rejected vertex has a selected neighbor.             (7)
```

Thus K2 has the explicit hard factor

```text
mu_K2(x) proportional to 1[x independent and dominating].                 (8)
```

It has no safe rejected symbol: rejecting a previously selected vertex can
leave it and its neighbors undominated.

### 5.2 Sufficient oriented boundary

For a region `D`, the exterior must report two kinds of information:

```text
blockers   accepted exterior neighbors that forbid local selections;
demands    rejected exterior collar vertices not already dominated outside
           and therefore requiring a selected neighbor inside D.
```

This is a radius-two boundary relative to `D`.  A blocker is selected at
distance one.  To decide whether a rejected distance-one exterior vertex
still carries a demand, the boundary constructor must inspect its selected
exterior neighbors, which can lie at distance two.  The resulting demand bit
is then the sufficient compressed datum delivered to `D`.

Given those data, the local kernel is uniform on assignments that are
independent, dominate every unblocked rejected interior vertex and meet every
carried exterior demand.  Exterior weights cancel in the conditional ratio.

**Theorem 2.**  These blocker/demand kernels are the conditionals of (8) and
satisfy the regional composition identity.

**Proof.**  A local assignment extends the fixed exterior to a maximal
independent configuration iff it meets exactly the three listed conditions:
internal independence, domination of interior rejected vertices, and
satisfaction of every exterior demand.  All admitted global configurations
have equal K2 weight, so conditioning is uniform on those local extensions.
Conditional towers of one joint law give equation (2).  ∎

### 5.3 Raw restriction is the wrong comparison

Restricting the uniform K2 law on a triangle to the edge `P-Q` gives

```text
{}:1/3, {P}:1/3, {Q}:1/3,
```

while direct K2 on the isolated edge gives

```text
{P}:1/2, {Q}:1/2.
```

The empty local outcome in the first line is not a progress failure.  The
forgotten exterior vertex is selected and dominates both local roles.  Once
that boundary is retained, the conditional kernels agree.

D37 checks `188` such conditionals across `165` distinct blocker/demand
boundaries and `1,224` nested towers.  The exact conclusion is:

> overlap consistency does not force nonprogress; it forces progress laws to
> carry the boundary obligations that make progress meaningful.

## 6. K1: a finite marked specification with wider memory

### 6.1 Recorded priority, not service order

K1 samples one strict order per connected conflict component and greedily
accepts a proposal when no already accepted neighbor conflicts.  The order is
an immutable `PRIORITY_CLICK` root carrying the complete component and order.
It is not the order in which the Python process happens to visit proposals.

For a finite graph, let `pi` be the tuple of component orders and `G(pi)` the
greedy selected set.  The marked joint law is

```text
mu_K1(pi,x) = |Pi|^-1 1[x=G(pi)].                          (9)
```

Its finite conditional kernels retain the exterior priority mark and
selected/rejected outcomes.  They satisfy the conditional tower identity.
Projection of (9) to `x` reproduces the D36 path law.

### 6.2 One-hop output locality fails

Finite consistency is not finite-range locality.  On the path

```text
A -- B -- C -- D -- E,
```

take local region `{A,B}`.  In both registered exterior conditions `{D}` and
`{E}`, the accepted one-hop collar at C is empty.  Nevertheless K1 gives

```text
exterior selected set       law on {A,B}
----------------------      ---------------------
{D}                         {A}:5/11, {B}:6/11
{E}                                   {B}:1.
```

Farther priority competition changes the number of global order marks that
lead to each local output.  D37 therefore records K1's finite boundary as

```text
component priority mark plus exterior outcomes,
```

not a one-hop collar.  D34's ancestry results make component-sized exact
dependence unsurprising, but it cannot be advertised as anti-diluting
finite-range locality.

### 6.3 Exact scope

The six marked path atoms pass 35 distinct conditional towers.  Their typed
complete-carrier realizations contain six priority clicks, 140 events and 20
signed D36 prepares; legality recomputes every selected set from its recorded
order.  They are full-carrier typed witnesses, not a region-indexed causal
pushforward: proper restriction currently drops a load-bearing component
priority parent.  All
priority marks and all selected/rejected bits are present before projection.  Raw
path-to-edge restriction remains `2/3` versus `1/3`, rather than the direct
edge's `1/2` versus `1/2`.

No infinite K1 completion is claimed.  An infinite local-priority construction
would require its own mark space, tie discipline, influence-cluster theorem,
quasilocality analysis and completion proof.

## 7. Finite-cover descent

### 7.1 Positive examples

As a deliberately narrow sanity check, D37 projects each supplied global
finite K3, K2 and marked K1 law through two- and three-region covers of the
three-path only.  Restricting that already supplied global joint to each cover
member gives matching overlap marginals:

```text
K3 cover checks          33
K2 cover checks          33
marked K1 cover checks   33
total                    99.
```

These checks neither reconstruct a joint from regional kernels nor enumerate
covers of every registered graph.  They verify three-path marginal descent
from an explicit positive joint.  The completion theorem is analytical, not
credited to this receipt row.

### 7.2 Permanent obstruction

Let binary variables A, B and C be pairwise anticorrelated.  Each pair has the
normalized law

```text
(0,1):1/2, (1,0):1/2,
```

and every singleton marginal is uniform.  But three binary values cannot be
pairwise unequal.  The triple support is empty.

Therefore a regional architecture must demand a positive joint extension on
every finite cover.  Agreement on all pair overlaps is only a necessary gate.

## 8. Birth and arbitration as conditionals of one law

### 8.1 Variable-support alphabet

At every supplied opportunity role `v`, introduce

```text
mode_v in {NO_BIRTH, TOKEN, BORN};
x_v    in {0,1};
x_v=0 whenever mode_v=NO_BIRTH.                           (10)
```

The modes mean:

```text
NO_BIRTH   no carrier occurs in the realized regional history;
TOKEN      an explicit pre-existing DORMANT_TOKEN is activated;
BORN       a new BORN_CARRIER with declared causal parent is created.
```

The state `x_v` is realized as an immutable `SELECTION_CLICK`.  A BORN or
TOKEN carrier may lose arbitration and remain unselected; its carrier record
and rejection history still exist.  No dormant token record is installed on
the `NO_BIRTH` or BORN branch.

### 8.2 Joint family

For supplied positive mode weights `a_0,a_T,a_B` and activities `lambda_v`,
define

```text
mu(m,x) = Z^-1
          product_v a_(m_v)
          product_v lambda_v^x_v
          1[x_v=0 when m_v=NO_BIRTH]
          1[x feasible].                                  (11)
```

Equation (11) is one normalized table.  Birth-mode probabilities and
arbitration probabilities are its marginals and conditionals.  There is no
independent `q_birth` draw followed by a second arbitration draw.

At the symmetric three-path point `a_0=a_T=a_B=lambda=1`, D37 obtains

```text
P_Q(BORN)       34/93
P_Q(TOKEN)      34/93
P_Q(NO_BIRTH)   25/93
P_Q(selected)    6/31.
```

Equal input weights do not give equal `NO_BIRTH` and present-mode marginals:
TOKEN and BORN each admit both selected and rejected continuations, while
NO_BIRTH admits only rejection.  The joint normalization correctly carries
that coupling.

Across two parameter points, equation (11) passes:

```text
intrinsic regional conditionals   166
one-site conditionals             134
nested DLR towers                 238
three-path marginal checks         33
BORN/TOKEN exchange atoms          93 at the symmetric point.
```

At that symmetric point the pushforward contains 93 typed histories, 1,683
events, 106 explicit dormant-token records and 156 signed exact D36 prepares.

### 8.3 WHEN, WHY and HOW

The two-level attribution is now exact:

```text
WHEN   equation (11), or a more general admitted mu, assigns BORN to the
       causal opportunity boundary;

WHY    the physical interpretation is fresh reception: the selected channel
       requires new support rather than dormant capacity;

HOW    D24's B_g supplies newborn content after the BORN mode occurs, and D26
       supplies its parent-coherence shadow.
```

Paper 26 constructs an admitted classical WHEN-family.  It does not derive the
reception principle, the weights or `g` from a deeper action.

## 9. D26 makes the BORN sector observable

### 9.1 History observable

Under D26's one-parent birth realization, a birth with coupling `g_e` changes
the probed parent coherence by

```text
c_e = sqrt(1-g_e).
```

For a realized history `h` on a represented parent line `ell`, define

```text
C_ell(h) = product_(e a BORN_CARRIER in h with parentLine(e)=ell) c_e. (12)
```

The typed DAG supplies the line predicate in (12): each `BORN_CARRIER`
inherits `parent_line` from its distinct `OPPORTUNITY_PARENT`.  The registered
three-opportunity control declares one common parent line in its carrier;
successive opportunity-parent records are chained through the preceding
mode/carrier result, so every pair of BORN carriers on that line is causally
comparable.  The validator rejects a parent line different from the carrier's
declaration.  TOKEN uses the
explicit coherence-neutral dormant-support control and NO_BIRTH has no
carrier, so both contribute factor one to this birth channel.  A different
physical TOKEN activation would have to declare and test its own dynamics.

### 9.2 Exact example

At `g=9/25`, `c=4/5`.  D37 builds and checks all 27 three-opportunity typed
mode histories after assigning their opportunity parents to the same explicit
line:

```text
three realized BORN events        C = 64/125;
equal independent mode mixture    E[C] = 2744/3375;
joint path Q mode marginal         E[C_Q] = 431/465.
```

The last value follows directly from equation (11):

```text
1 - P_Q(BORN)(1-4/5)
  = 1 - (34/93)(1/5)
  = 431/465.
```

Thus observed visibility budgets constrain the combined BORN incidence and
coupling data of an admitted regional law relative to the declared
coherence-neutral TOKEN control.  This does not produce a universal rate in
seconds.
That would require a record-to-system dictionary, a monitored dwell interval
and separation from ordinary environmental decoherence.

## 10. Countable completion

### 10.1 The theorem

**Theorem 3.**  Let `C` be a supplied countable typed opportunity carrier
whose incompatibility relation is a locally finite pairwise conflict graph
and whose per-opportunity participant, parent-line and type data are finite.
At their stated finite-range scopes, K3, K2 and the joint birth/arbitration
family (11) each admit at least one compatible global classical measure on its
admitted configuration subshift.  The deterministic typed core realization
through recorded selection has a corresponding pushforward measure on
countable causal histories.

### 10.2 Proof

Every vertex has a finite state alphabet.  K3 exclusion, K2 independence plus
domination, and the constraints in (10)--(11) are closed local conditions.
Their admissible configuration spaces are closed subsets of a compact product
space.

They are nonempty:

```text
K3       all vertices rejected;
K2       a maximal independent set from a fixed countable greedy enumeration;
joint    all modes NO_BIRTH and every x_v=0.
```

Fix one admissible exterior configuration and an exhaustion

```text
D_1 subset D_2 subset ...,
union_n D_n = C.
```

Let `mu_n` be `gamma_Dn(.|exterior)`, extended by the fixed exterior.  Compactness
gives a weakly convergent subsequence.

For a fixed finite region `D` and cylinder observable `f`, `gamma_D f` depends
on finitely many exterior coordinates.  For K3 this is the accepted one-hop
collar.  For K2 it is the radius-two blocker and domination-demand collar.
For (11) it is the one-hop conflict collar and local modes.  Local finiteness
is essential here.  Therefore `gamma_D f` is continuous on the admitted
configuration space.

For all sufficiently large `n`, finite specification consistency gives

```text
mu_n(gamma_D f) = mu_n(f).
```

Passing to the subsequential limit yields

```text
mu(gamma_D f) = mu(f)
```

for every finite `D` and cylinder `f`.  Hence `mu` belongs to `G(gamma)`.

For K3 and K2 use the declared coherence-neutral TOKEN carrier at each
opportunity; for (11) use its sampled mode.  Apply the same local core event
rules as `F_D` through each `SELECTION_CLICK`, with injective tagged canonical
tuple identities and shared participant bases, and take their countable union.
Participant and transaction labels are injected into arbitrary-precision
natural numbers, not hashed into a finite identity space.  Local finiteness
and the parent bound give a
well-defined countable acyclic history.  Its law is `F_*mu`; every finite
cylinder agrees with the corresponding core `Gamma_D` pushforward.  Finite
SHA-256 values are checksums only.  In particular, the exact imported D36b
carrier/envelope adapter remains the separately gated finite append interface:
its locked evidence IDs are SHA-based and are not used as a countable
injectivity premise.  ∎

### 10.3 What completion does not select

The theorem proves nonemptiness, not uniqueness.  Different subsequences,
boundary conditions or phases may yield different members of `G(gamma)`.
Activities and mode weights already produce distinct specifications before
that question arises.

The theorem is also conditional on a supplied typed opportunity carrier.  It
does not define a random law that generates the carrier's own vertices,
conflict edges and causal parents.  Equation (11) selects presence modes on supplied
roles; it is not yet a self-generated universe of opportunity roles.

K1 is absent from Theorem 3 because its receipt exhibits dependence beyond a
one-hop output boundary and supplies no infinite mark/influence theorem.

## 11. Covariance, anti-dilution and click discipline

### 11.1 Construction-order gauge

The finite distributions are functions of structural incidence, boundary
marks and recorded outcomes.  Relabeling every role transports the laws
exactly; the receipt passes six such covariance families:

```text
oriented incoming/lateral/generated interfaces;
K3 at two activities;
K2;
marked K1;
joint birth/arbitration.
```

The typed carrier adds D33's stronger event-poset gate.  A one-proposal BORN
history with two participant prepares has 70 linear extensions.  Replaying
all 70 as valid serializations produces one identical canonical DAG digest;
the gate does not re-execute actor operations in 70 service orders.  At the same
time, the six pairs of events that share a wire are causally comparable, so
the test does not quotient physical same-wire order.  Machine enumeration is
therefore presentation gauge; causal order is not.

### 11.2 Remote anti-dilution

On two disconnected typed carrier components, K3, K2, component-marked K1 and
equation (11) each factor exactly.  Adding the remote component changes no
local marginal or conditional on the first edge.  D37 reports `4/4`
probability factorizations.

The stronger D34 gate builds one 24-event history over both components,
including distinct typed opportunity parents, participant bases, a BORN/TOKEN
mixture and signed prepares.  Causal restriction gives a 13-event left and an
11-event right history, exactly equal to histories realized independently on
those components.  Both typed restriction squares pass.  Thus the registered
anti-dilution witness is causal-record disconnection, not mere graph
nonadjacency.

This is the D34 locality requirement at each registered width: K3 and (11)
use a one-hop conflict collar, K2 uses its radius-two blocker/demand collar,
and K1 retains the connected-component priority mark.  There is no
universe-wide denominator.  Factorization does not turn K1's
connected-component dependency into a bounded collar.

### 11.3 Randomness and the D36 adapter are recorded

K1's component priority is a typed click root in every pushed-forward atom.
Every proposal has a typed mode click and a selected/rejected click.  K2, K3
and equation (11) use the same realization path; their binary states are no
longer merely click-labeled coordinates.

On the three-path controls, the adapter realizes:

```text
K3    5 histories / 105 events / 10 signed prepares / 15 dormant tokens;
K2    2 histories /  44 events /  6 signed prepares /  6 dormant tokens;
K1    6 histories / 140 events / 20 signed prepares / 18 dormant tokens /
      6 recorded component-priority clicks.
```

Each `D36_PREPARE` has the exact carrier-derived structural-attempt identity,
base-version binding, issued route capability, ideal signature and typed
sender/target roles described in section 3.2.  Two prepares for one selected
proposal share the attempt but target their own participant bases.  This
is no longer a locally imitated field tuple: the receipt imports the locked
D36b implementation, constructs its admitted `T0_BIRTH` or `SLOT_ACTIVATION`
evidence `Record`, signs its actual `Envelope`, and requires
`participant_accepts_prepare()` for all 192 registered prepares.  This closes
the finite append adapter at D36's ideal-authentication scope; it does
not add crash or Byzantine tolerance.

The probability law is not an unrecorded external coin and not mailbox
service order.  Once `mu` is supplied, its conditionals are the click law;
there is no second lottery behind them.

## 12. Relation to the action

Paper 16 proves that a local action does not by itself select a complete
history measure.  Boundary state, orbit or gauge measure, contour,
renormalization, record instruments and continuation data remain part of the
rulebook.

Paper 18's

```text
S(I)=exp(-I)
```

is a survival law for a supplied opportunity.  It is not automatically the
normalizing weight in (5), (8), (9) or (11).

Paper 26 sharpens the remaining action bridge.  The unselected data are now
explicit:

```text
K3 activities lambda_v;
K2 hard-constraint family and any admitted local weights;
K1 priority-mark law and boundary class;
mode weights a_0, a_T, a_B;
birth couplings g_v;
choice or phase inside G(gamma);
and the supplied typed opportunity carrier itself.
```

A successor must either derive these as conditionals of one complete
action/history functional with all required measure and instrument data, or
declare them as empirically identified/posited couplings.  Writing
`exp(-I)` beside them is not a derivation.

## 13. Downstream execution by D36

The regional law and the transaction protocol occupy different layers:

```text
gamma / mu    supplies opportunity modes, recorded marks and a feasible
              selected set;

F             appends typed carrier/mode/selection records and finite signed
              exact D36 PREPARE envelopes keyed by H(carrier,body);

D36 P4        authenticates the selected attempts, reserves exact versions,
              commits or aborts, applies locally, acknowledges and closes.
```

K3 and equation (11) may produce a nonmaximal or empty selected set.  P4 can
execute it safely but cannot manufacture progress.  K2 supplies maximal
progress at the closed finite boundary.  K1 supplies greedy maximal progress
but carries its wider priority boundary.

The finite adapter is receipt-carried, but nothing in Paper 26 changes D36's
assumptions: supplied finite attempts,
ideal authentication, honest record-generating actors, reliable messages,
failure-free coordinators and fair complete servicing.  Crash recovery,
retry fairness and Byzantine behavior remain separate.

## 14. Classical scope and quantum preregistration

Paper 26 is classical.  It does not create a quantum specification by putting
amplitudes on independently normalized regional marginals.  A future lift
must supply one strongly positive decoherence functional or compatible family
of completely positive conditional maps, together with a quantum extension
theorem.

The join sector inherits two corpus limits:

1. D23's rooted controlled-rotation identification ceases to be complete at
   in-degree `>=2`; relative signs can be invisible to the same Z-click data.
2. D31/D32 distinguish structural dependency from operational influence and
   require the alphabet-specific repeated same-pair cancellation census.

Therefore a quantum regional join cannot be called fully click-identifiable
from its causal ancestry alone.

No result here derives Lorentzian geometry, light cones, dimension, units,
`G`, a universal birth rate or a universal transaction coordinator.

## 15. Reproducibility

Primary D37 artifacts:

```text
note-d37-regional-history-specifications.md
code/d37_regional_history_specification_exact.py
data/d37_regional_history_specification_exact.out
```

The exact receipt uses only standard-library integers and `Fraction`.  Its
source, stdout-body and internal-science hashes are

```text
source    dd5f8991569353e8b865370ffde0d9fef49ee5ba03e49505865a9c6fbfbc805c
stdout    be36426e043f1b7c96af989a7e6c82c8760b4ce3b303f25e1a4c8e17b59d9900
science   b57af3d7b0c35a2edb3b21caee8f2452dfcbb63f7320bf9ce3e135cc308b36da
complete  1a8b94e24ce5b1901acd5dc5ff658ccd0420906d788d2b2a0684ce4162880ef4
```

Executions under hash seeds `0`, `1`, `17`, `42`, `104729` and `271828` are
byte-identical.  The registered-object header is:

```text
graphs=8; vertices=28; conflict_edges=19; nonempty_regions=196;
oriented_interface_rows=38; interface_content_checks=38/38;
typed_causal_histories=6/6; typed_events=104; signed_D36_prepare_records=19.
typed_illegal_histories_rejected=7/7.
canonical_tuple_ID_controls=(1000,1000,1000).
D36_participant_accepts_PREPARE=10+6+20+156=192.
```

The receipt verdict is:

```text
S0=PASS  typed interfaces and causal histories
S1=PASS  K3 full finite specification
S2=PASS  safe-support fixed-odds forcing
S3=PASS  K2 maximal-support lift
S4=PASS  K1 recorded-priority probability lift, full atoms and counterexample
S5=PASS  three-path marginal descent and triple-cover obstruction
S6=PASS  joint birth/arbitration functional
S7=PASS  D26 chained lineage plus accepted D36b PREPARE adapters
S8=PASS  relabeling and event-poset serialization covariance; causal anti-dilution

PASS 9/9.
```

## 16. Decision table

```text
Question                                                   Answer
---------------------------------------------------------  ------------------------
Is a regional conditional object now defined?              yes, classically
Is its finite typed causal pushforward implemented?         yes for K3/K2/joint
Does it obey finite nested composition?                     yes, on audited families
Does pairwise cover agreement guarantee a joint?            no
Does fixed-odds safe-support locality force K3?              yes, at stated scope
Does overlap consistency alone force K3?                    no
Can a progressing maximal-set law be regional?              yes, K2 with demands
Is raw induced-subgraph restriction sufficient?             no
Does finite marked K1 compose?                              yes
Does K1 have typed proper-region restriction transport?     no; full-carrier atoms only
Is K1 one-hop output-local?                                 no
Is infinite K1 completion proved?                           no
Are birth mode and arbitration in one finite functional?    yes
Are their numerical weights selected?                       no
Does D26 constrain the BORN sector observationally?         yes, conditionally
Does a countable global classical completion exist?         yes, pairwise-graph scope
Is that completion unique?                                  not proved
Is the typed opportunity carrier generated by the law?      no; supplied
Is the action bridge closed?                                no
Is a quantum regional join supplied?                        no
```

## 17. Candidate conclusion

Paper 25 ended with a local coordination cell and a missing regional law.
Paper 26 supplies the first exact classical version of that law at a useful
scope.  Finite oriented regions carry normalized conditional kernels and the
K3, K2 and joint-family pushforwards carry immutable typed event DAGs.  Nested composition,
three-path marginal descent, 70-extension event-poset covariance and exact
causal restriction on disconnected components are executable gates.  K3, K2
and a joint birth/arbitration family admit global measures on supplied
countable typed carriers with locally finite pairwise conflict graphs.

The construction refuses an attractive overstatement.  Overlap consistency
does not force one Gibbs member or eliminate progress.  K3 is forced only
after exact positive feasible support and fixed feasible-addition odds are
supplied; its one-hop Markov boundary is a separate locality property.  K2
remains a valid regional specification once its radius-two boundary carries
unmet domination obligations.  K1 remains valid as a finite marked
probability specification and has complete-carrier typed witnesses, but lacks
a typed proper-region restriction transport and exposes a path-five failure
of one-hop output locality.

Record birth is now located cleanly.  `NO_BIRTH`, `TOKEN` and `BORN` can be
alternatives inside the same normalized functional that supplies arbitration.
D24 answers how newborn content is attached on BORN.  D26 gives BORN a
measurable shadow on its represented parent line.  The same typed realization
records every stochastic click and emits exact signed D36 prepares.  Neither
result chooses the mode weights, activity, coupling or opportunity carrier.

The strongest candidate noun is:

```text
CLASSICAL TYPED CAUSAL REGIONAL SPECIFICATION FAMILY /
FINITE SPECIFICATION AND COUNTABLE LOCALLY FINITE PAIRWISE-CONFLICT COMPLETION /
SUPPLIED OPPORTUNITY CARRIER AND COUPLINGS /
NONSELECTING.
```

The next foundational question is no longer “what might an overlap law look
like?”  It is precise:

> Which physical principle or complete action/history construction selects or
> identifies the coupling data and completion phase of the admitted regional
> specification family, while also generating rather than supplying the
> opportunity carrier?

## References

1. Relativistic ISP v10 Paper 15, *From regional amplitudes and instruments to
   recorded histories*.
2. Relativistic ISP v10 Paper 16, *The rulebook is the history law, not the
   action alone*.
3. Relativistic ISP v10 Paper 18, *No Silent Erasure, and the identified
   interactive click law*.
4. Relativistic ISP v10 Paper 19, *The complete interactive record law at the
   declared interface*.
5. Relativistic ISP v10 Paper 21, *Local generators do not imply local
   memory*.
6. Relativistic ISP v10 Paper 22, *The predictive record-DAG boundary*.
7. Relativistic ISP v10 Paper 23, *The whole component is the exact ancestry
   boundary*.
8. Relativistic ISP v10 Paper 24, *A's next click is the upper seal of a causal
   call diamond, not the winner of a clock race*.
9. Relativistic ISP v10 Paper 25, *Record birth carries coordination but does
   not select it*.
10. D26 interface note, `note-d26-interface-equivalence-closure.md`.
11. D33 history-law phase note, `note-d33-history-law-phase.md`.
12. D36 terminal note, `note-d36-record-birth-causal-coordination.md`.
13. D37 protocol and theorem note,
    `note-d37-regional-history-specifications.md`.
14. R. L. Dobrushin, “Prescribing a system of random variables by conditional
    distributions,” *Theory of Probability and Its Applications* 15 (1970),
    458--486.
15. O. E. Lanford III and D. Ruelle, “Observables at infinity and states with
    short range correlations in statistical mechanics,” *Communications in
    Mathematical Physics* 13 (1969), 194--215.
16. H.-O. Georgii, *Gibbs Measures and Phase Transitions*, second edition,
    de Gruyter (2011).
17. N. Chandgotia and T. Meyerovitch, “Markov random fields, Markov cocycles
    and the 3-colored chessboard,” *Israel Journal of Mathematics* 215 (2016),
    909--964; `arXiv:1305.0808`.
