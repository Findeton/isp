# D7 — characterization and search for the interacting extension rulebook

**Status:** problem specification frozen before the v1–v9 corpus audit,
independent construction campaign, or external literature/priority search,
2026-07-11. Literature claims must use primary sources where available.
Claims of originality are forbidden unless a targeted post-construction
search finds no earlier match; absence from a finite search is evidence only,
not proof of priority.

## 1. The object missing after D6

D6 showed that supplied ordered finite laws determine a relative RN numerical
field. That begins too late. The missing rulebook must assign probabilities
before the compared laws, candidate scope, evidence channel, and accepted
record already exist.

Let `Hist` be the groupoid/category of finite typed marked record histories.
An object `H` contains only committed record data: incidence/order,
orientations and ports, marks, sealed factors, and their provenance. A
morphism may be an isomorphism/relabeling, an admissible sealed quotient, or a
specified restriction map. These morphism classes must not be conflated.

For a history `H`, let

$$
\operatorname{Ext}(H)
$$

be the set or standard Borel space of admissible **typed click packages**. A
package `xi` may add one record or a finite jointly sealed packet and contains:

1. its new record identities;
2. its typed incoming collar/interface into `H`;
3. its proposed incidence/order relations;
4. its marks or outcome space;
5. any proposed numerical factor field and its primitive/derived status;
6. exactly-once ownership/provenance;
7. the seal/commitment witness required to make the package durable.

The space also contains an explicit null extension:

$$
\varnothing_H.
$$

The minimal discrete-click rulebook is a probability kernel

$$
K_H(d\xi)
$$

on `Ext(H) union {empty_H}`. If clicks may occur in packets, `xi` is the
whole indivisible packet; an arbitrary internal ordering is not physical.

A continuous- or evidence-time version may instead begin with a locally
finite marked intensity

$$
\Lambda_H(d\xi),
$$

but intensity alone is not a complete rulebook: it also needs an endogenous
clock/interval and the associated no-event survival law. In discrete record
time, the normalized kernel is the safer primary target.

## 2. Equivalent full-history formulation

Given an initial law and measurable kernels, the rulebook determines a path
measure `mu` on variable marked histories. Conversely, a primitive path
measure gives conditional extension kernels only relative to a filtration and
only `mu`-almost surely; versions on zero-probability histories are extra
data if the generative law must act there.

Thus there are two honest foundations:

```text
primitive path measure mu
```

or

```text
primitive/derived extension kernels K_H plus an initial/root law.
```

The derivation problem exists only for the second ambition. Calling `mu`
primitive is a valid rulebook, but it does not derive the rulebook from sealed
records.

The law may be non-Markovian in any small visible state. It must not be
assumed Markovian without proof. It may nevertheless be Markovian on the full
committed history `H`, since `H` already contains the past; this is notation,
not a claim of finite-memory divisibility.

## 3. Proposal, comparison, evidence, commitment, and birth

Five stages must remain typed.

### 3.1 Opportunity/proposal

A proposal law selects a null-inclusive distribution over extension packages.
It supplies candidate scope and the probability that no candidate is offered.

### 3.2 Ordered comparison

If one proposal contains competing physical protocols or outcomes on a
common atom space, their RN field compares supplied conditional laws. It does
not create the proposal.

### 3.3 Realized evidence

Pointwise log likelihood, expected KL, and an accumulated record-carried
evidence process differ. Only the last can serve as the input to a physical
commitment clock.

### 3.4 Commitment decision

A numerical survival/division weight is not yet a sampled decision. A rulebook
must say whether the random decision is primitive, deterministically hidden,
or encoded in the full history measure.

### 3.5 Durable birth

Only a committed typed package with provenance becomes part of `H`. D5 may
then compose its factor field.

The stages may be mathematically folded into one kernel `K_H`. If factored,
every intermediate object must be physical or explicitly auxiliary; no
hidden proposal oracle may be renamed a boundary observable.

## 4. Mandatory mathematical constraints

### 4.1 Positivity and normalization

For every history in the generative domain,

$$
K_H(A)\ge0,
\qquad
K_H(\operatorname{Ext}(H)\cup\{\varnothing_H\})=1.
$$

If only a measure-almost-sure kernel is supplied, its off-support version
scope must be stated.

### 4.2 Leibniz covariance

For every typed history isomorphism `g:H -> H'`, extensions push forward and

$$
K_{H'}=g_*K_H.
$$

Labels, enumeration order, machine addresses, and analyst-chosen coordinates
cannot change physical probabilities.

### 4.3 Construction-order gauge on commuting packages

Suppose `xi` and `eta` are compatible packages whose physical collars are
spacelike/independent in the record sense and whose final marked history is
the same under either auxiliary construction order. Then path weights must
obey the diamond condition, including any multiplicity factors:

$$
K_H(\xi)
K_{H+\xi}(\eta)
=
K_H(\eta)
K_{H+\eta}(\xi).
$$

This condition applies only when the moves physically commute. Imposing it on
interacting or order-sensitive protocols would erase real holonomy. A
construction-order quotient must therefore distinguish:

```text
auxiliary build order
```

from

```text
physical protocol orientation/order.
```

### 4.4 Candidate-relative recorded locality

D4 refuted autonomous naturality under every unmarked subset. The replacement
cannot be global lookup. For each proposed package `xi`, there must be a
record-carried collar/predictive state `B_H(xi)` such that histories with the
same licensed collar data give the same candidate law:

$$
B_H(\xi)=B_{H'}(\xi')
\Longrightarrow
K_H(\xi)=K_{H'}(\xi')
$$

within the declared physical proposal class.

If discarded history changes the probability, the difference must be carried
as an additional boundary/vertical record. This is the no-silent-history
principle. The boundary may grow; D7 does not demand one fixed token.

This is a locality criterion, not yet a constructor of `B_H` or of `xi`.

### 4.5 Admissible restriction/projective consistency

For an admissible quotient `pi:H_f -> H_c`, a fine extension must push forward
to a coarse extension or to a declared retained residue. Silent fine modes
must have zero future response. One cannot demand equality under arbitrary
induced subsets, which caused D4's collapse.

At the path-measure level, finite cylinder laws must be projectively
compatible. Compatibility hosts laws; it does not select one.

### 4.6 Local finiteness/non-explosion

A finite record region and bounded intrinsic interval must have finite total
proposal mass/intensity. Otherwise infinitely many opportunities can occur
before one durable record is defined.

### 4.7 Root/immigration and bridge sectors

Purely support-local continuation cannot create the first record from the
empty history and cannot join previously independent tensor/record
components. A complete rulebook must explicitly specify:

1. an initial/root distribution or immigration sector;
2. a multileg bridge package class, or a theorem that its probability is
   exactly zero;
3. the law assigning weight to those sectors.

Calling a bridge “nonlocal” does not decide whether it is allowed. The
physical locality test is whether its multileg collar and influence are
explicit committed data and whether later effects propagate through recorded
chains.

### 4.8 Capacity and carrier accounting

Every accepted finite record has finite content in its declared channels.
No uniform arity/degree bound follows from the present scalar capacity result.
A rule may use finite multichannel packets and distributed boundary state,
but it must price every primitive channel, mark, identity, and bridge leg.

### 4.9 Conservation and compatibility

Typed ports may enforce charge, orientation, gauge, or other conservation
constraints. These are eligibility filters. Unless they leave exactly one
normalized candidate, they do not select the probability law.

## 5. Physical interpretation constraints

### 5.1 No universe machine clock

An auxiliary sequential sampler may inspect a complete mathematical history,
but physical predictions must descend to the unlabeled/partial-order history.
No observable global commit counter may define simultaneity or influence.

### 5.2 Proper time is emergent/local

A chain of committed records may count local clicks. Different chains need
not share a global clock. Construction order is gauge when it only linearizes
compatible partial-order growth.

### 5.3 No metric smuggling

Before spacetime emerges, locality must use incidence, collars, screens,
factor support, or recorded predictive dependence—not metres, seconds, or a
pre-existing light cone. A derived speed limit must arise from finite carrier
propagation in the generated order.

### 5.4 Entanglement is not automatically adjacency

High-order dependence can be invisible in proper low-order shadows. It may
license a multileg recorded factor, but statistical dependence alone does not
prove a direct carrier or spatial edge.

### 5.5 Record projection is the law-level object

Deterministic hidden machines and primitive stochastic realizations are
allowed if they induce the same committed-record kernel/path measure. Hidden
details that change future record probabilities must become recorded state.

## 6. Nontriviality and anti-circularity gates

A candidate rulebook fails if it is any of the following:

1. **Full-law lookup:** it computes `K_H` from the already supplied target path
   measure without declaring that measure primitive.
2. **Complete-ledger renaming:** it supplies `m-1` unconstrained coordinates
   for an `m`-atom law and calls Fourier inversion dynamics.
3. **Eligibility-only:** it identifies allowed extensions but supplies no null
   mass or relative weights.
4. **Conditional-only:** it gives RN comparison, evidence, or commitment only
   after the proposal is supplied.
5. **Global-shock collapse:** it permits only empty/full universal precursors
   because locality was imposed under every subset.
6. **Seed-only:** it can continue an existing connected component but cannot
   specify the initial/root law or first bridge.
7. **Metric import:** it uses distance, dimension, or light cones before the
   record order generates them.
8. **Teacher dependence:** it selects features or weights using hidden
   presentation counts unavailable to the physical record.
9. **Unpriced infinity:** it offers infinitely many types/scopes with no
   locally finite total mass.
10. **Gauge failure:** different auxiliary orders of commuting packages give
    different probabilities for the same physical history.

## 7. What would count as closure

A full solution must supply or derive:

```text
history state space and filtration
initial/root law
typed extension domain including bridges
explicit null/no-proposal alternative
normalized weights or locally finite intensity plus clock
record-carried locality/sufficiency map
construction-order gauge on commuting packages
projective/cylinder consistency
evidence carrier and commitment/outcome semantics
exactly-once ownership and D5 factor allocation
```

It must also state all primitive couplings or state data. “No free constants”
is not assumed: physical theories can have couplings and boundary data. What
is forbidden is hiding them inside an object described as derived.

Only after these gates pass may the law be propagated into the v9 geometry
program and tested for round cones, dimension, scale dependence, and the
emergence of finite propagation speed.

## 8. Search protocol

The investigation order is frozen:

1. audit v1–v9 for every object that could fill a rulebook field;
2. classify each as primitive law, admissibility filter, conditional
   comparison, inference principle, or actual extension kernel;
3. develop candidate constructions from the frozen constraints without using
   the literature search to manufacture apparent originality;
4. stress-test them for root, bridge, null mass, covariance, locality,
   construction-order gauge, and nonselection;
5. search primary literature for equivalent or stronger constructions;
6. report originality conservatively as `known`, `adaptation/composition`,
   `apparently distinct in searched sources`, or `not established`.
