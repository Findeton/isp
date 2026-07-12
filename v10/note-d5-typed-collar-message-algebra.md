# D5 — supplied factor partitions, separator messages, and channel-rank limits

**Status:** preregistered before the D5 executable was written or run,
2026-07-11; revised after hostile-review round 1. Reviews ON. The original
preregistration used `typed`, `sealed`, `local`, and `birth` too early; the
round-1 disposition in section 10 records every downgrade. All production code and receipts must remain under
`v10/`. Decisive finite claims use exact integers and rational arithmetic;
transcendental capacity values may be reported at high precision but may not
silently decide a structural verdict.

## 1. Question

D4 proved that demanding silent autonomous evolution for every unmarked
subset is too strong. It leaves only an empty/full universal-precursor
mixture. A supplied global law admits an exact completion quotient, but that
quotient is law-relative, has no constructed carrier, and requires
unboundedly many deterministic token states on a growing chain.

D5 changes the target. Locality need not mean one fixed token for an
arbitrarily large region. A local theory may use many finite records spread
over a growing boundary, provided that every piece of predictive information
is carried by typed records on that boundary and composes without a hidden
universe ledger.

D5 asks:

> Does a supplied complete finite factor partition admit a compositional
> sufficient separator state, and which additional objects would be required
> to turn that conditional theorem into an actual sealed-record click law?

The investigation must keep separate:

1. how candidate records can be born;
2. which candidates are eligible;
3. how an eligible candidate is weighted;
4. how discarded factor history is summarized on a formal separator;
5. whether the summary is bounded per record, per independent channel, per
   boundary, or not at all.

## 2. Corrections frozen before execution

### 2.1 Participant count is not channel rank

Four quantities are different:

```text
number of participating records
number of listed observables/channels
rank after redundancy and constraints
total evidential content
```

One parity observable can involve many records while contributing one
independent channel. Many copied records can likewise be redundant. D5 will
not infer a graph-degree bound from a scalar capacity bound.

### 2.2 “Vector capacity” means a matrix problem

For one binary contrast, Fisher capacity is scalar. For a multichannel record
with observables `Q_alpha`, the natural object is the covariance/Fisher matrix

$$
J_{\alpha\beta}=\operatorname{Cov}(Q_\alpha,Q_\beta).
$$

Its rank counts independent infinitesimal evidential directions. Its
eigenvalues and directional forms describe remaining capacity. A scalar
content cannot be equated to this matrix until a canonical scalarization or
direction has been derived. D5 will test whether the correct result is a
scalar bound, a directional bound, a Pareto frontier, or a refusal.

### 2.3 Distributed finite memory is allowed

D4 rejected one uniform exact deterministic token across all history depths.
D5 does not convert that theorem into a rejection of distributed locality.
The allowed mathematical target is:

- finite state at every finite formal separator;
- bounded information per primitive carrier, if the record axioms force it;
- total separator state allowed to grow with boundary size;
- exact factor-graph composition from supplied factors;
- no unrecorded dependence on remote volume, construction depth, or a global
  clock.

## 3. Frozen finite arena

### 3.1 Primitive binary record variables

A finite cell has binary record variables

$$
x_v\in\{-1,+1\}.
$$

For `n` primitive variables, the nonconstant parity characters are

$$
Q_S(x)=\prod_{v\in S}x_v,
\qquad \varnothing\ne S\subseteq\{1,\ldots,n\}.
$$

The complete character ledger has `2^n-1` listed nonconstant channels. The
screen-relative operational rank is the exact rank of their Gram/covariance
form after the declared quotient by duplicates, constants, and constraints.

This character arena is a finite diagnostic, not an assertion that every
physical SHARD record carries a complete parity ledger.

### 3.2 Supplied factor tokens

A supplied factor token is a triple

$$
f=(\operatorname{scope}(f),\phi_f,\pi_f),
$$

where:

- `scope(f)` is a nonempty finite set of record variables;
- `phi_f` is a strictly positive rational table on that scope;
- `pi_f` is one unique identity allocated under a supplied exactly-once
  ownership convention. It prevents literal duplicate counting; it is not a
  physical carrier type, port orientation, seal, outcome, or evidence witness.

The joint unnormalized weight of a finite marked history is

$$
w_H(x)=\prod_{f\in H}\phi_f(x|_{\operatorname{scope}(f)}).
$$

Positivity avoids support-dependent divisions in the base theorem. The
repaired executable separately types nonnegative support controls, derived
messages, and the multiplicative identity; it rejects every negative weight.

Supplying `phi_f` is supplying factor-law data. The universal
sum-product encoder below may compose supplied factors, but it must not be
misreported as deriving their numerical values from sealed-record principles.

### 3.3 Cuts and formal separators

For a retained boundary variable set `B` and an eliminated finite interior
`I`, the formal separator input consists of:

- the boundary variables `B`;
- all factor tokens assigned to the region `I union B`;
- unique IDs for every factor touching the cut;
- a supplied factor partition and exactly-once ownership assignment.

The exact boundary message is the effective factor

$$
M_{I\to B}(b)
=
\sum_{i\in\{-1,+1\}^{I}}
\prod_{f\in H_{I\cup B}}\phi_f((i,b)|_{\operatorname{scope}(f)}).
$$

This definition is an encoder computed from supplied factors inside the region.
It does not inspect factors outside the region. Its normalized form may be
used as a predictive state; its unnormalized form is retained for exact
composition.

### 3.4 Composition

When two regions meet only on a declared separator `S` and their allocated
factor identities are disjoint, composition is tensor contraction:

$$
M_{A\cup_S B}(a,b)
=
\sum_s M_A(a,s)M_B(s,b).
$$

The exact gates will test:

- equality with direct elimination;
- associativity over three pieces;
- independence of elimination schedule for one fixed factor multiset;
- covariance under record relabeling;
- refusal of duplicate provenance;
- no invention of cross-component factors.

### 3.5 Supplied candidate and conditional state prediction

A candidate variable `z` is presented by a finite set of supplied proposal
factors whose scopes contain `z` and separator variables. Given an existing
message `M_B`, its conditional state weight is the exact contraction

$$
W(z)=\sum_b M_B(b)\prod_{f\in F_z}\phi_f(z,b).
$$

After normalization over the states of that already supplied candidate, this
gives a conditional state distribution. It does not give a no-birth option,
proposal measure, eligibility rule, seal probability, or normalization across
inequivalent record extensions.

This construction separates:

- the domain of proposed factor tokens;
- eligibility/provenance gates;
- numerical weighting once those factors are supplied.

The v7 survival law may later act on a supplied evidence increment. It is not
used here to invent a scope, carrier, or factor table.

## 4. Preregistered exact gates

### R — channel and rank gates

**R1.** Complete parity ledgers have exact screen-relative covariance/Gram
ranks `1,3,7` for one, two, and three primitive binary variables under the
uniform full-support screen.

**R2.** Duplicating or adding a linearly dependent channel does not increase
rank. Joint bijective relabeling of the whole ledger and screen preserves
rank. Adding a symmetry-translated observable may increase rank.

**R3.** One `n`-body parity channel has rank one while involving `n` record
variables.

**R4.** Independent product channels make screen-relative Fisher rank and
trace extensive in channel count. The single-channel `W_*` therefore cannot
by itself be promoted to a uniform total-record bound.

**R5.** No raw participant-count bound may be claimed unless a positive
irreducible cost per independently participating carrier and an additive
allocation theorem are both proved.

### C — factor-partition composition gates

**C1.** Direct elimination equals sequential message contraction on every
audited path/tree cell.

**C2.** Three-piece contraction is associative and elimination-schedule
invariant for one fixed factor multiset. No physical construction-order gauge
is inferred.

**C3.** Joint relabeling of variables and factor tables preserves every
prediction.

**C4.** Reusing the same unique ID is refused rather than double-counted.
Assigning one separator factor to the left or right gives the same answer when
it is included exactly once. Semantic duplication under fresh IDs remains
outside this control.

**C5.** A loop is not certified by naive independent one-site messages. Exact
composition must either retain a joint separator table or prove a valid lower
rank factorization.

### S — sufficiency and non-Markovian gates

**S1.** Two different interiors with the same exact separator message give the
same prediction for every common external proposal factor.

**S2.** The same unmarked boundary with different exact separator messages can
give different predictions; the mark is load-bearing.

**S3.** A factor history may be non-Markovian in its unmarked visible state
while becoming sufficient after its accumulated message is retained, provided
the supplied factorization screens all external dependence through the
separator. This is not a claim about arbitrary full-history measures.

**S4.** The positive ray is universally minimal only against arbitrary
strictly positive full-separator tests. A restricted physical proposal class
may admit a coarser quotient. The message is law-relative to supplied factor
tables but is not computed from discarded external completions.

### B — proposal-domain and connectedness gates

**B1.** Adding a supplied candidate with factor legs into one existing
connected component preserves connectedness and changes no old factor.

**B2.** A supplied candidate joins two old components only if its proposal
contains primitive factor legs into both. The algebra does not derive that
multileg token or turn syntactic incidence into directed physical transport.

**B3.** Under the additional one-component proposal-domain assumption,
disconnected components cannot join. Given a connected seed, closure preserves
connectedness. Neither the domain nor the seed is derived.

**B4.** Listed scope, essential dependence, irreducible interaction,
primitive factor-hyperedge incidence, a derived correlated message, and
directed physical transport are distinct. The executable proves no directed
carrier law.

### K — capacity and scaling gates

**K1.** For boundary width `b`, an arbitrary exact binary boundary potential
has `2^b` entries and `2^b-1` normalized degrees of freedom.

**K2.** Low-treewidth/factorized histories may admit bounded-width messages.
The loop control only proves that one-site marginals can be insufficient; it
does not prove a universal exponential encoding lower bound.

**K3.** The audit will separate per-record alphabet, separator width, numeric
precision, and total boundary storage. “Finite” may not slide between them.

**K4.** A projective interpretation is considered only after a compatible
finite message family exists. Compactness alone may host growing state but may
not be called a physical encoder or a selector of factor values.

## 5. Adversarial cells fixed in advance

The executable must include at least:

1. a one-channel binary factor;
2. two independent channels;
3. copied/redundant channels;
4. a pure many-body parity channel;
5. a three-piece chain with two elimination orders;
6. a branching tree;
7. a loop with an inadequate product-of-marginals summary;
8. two distinct interiors with the same boundary message;
9. two marked interiors with the same unmarked boundary but different
   predictions;
10. one connected birth;
11. an attempted disconnected join without a carrier;
12. an explicit multileg joining proposal;
13. growing separators displaying the distinction between bounded local
   factor arity and growing total boundary state.

## 6. Verdict gates

The initial verdict must be one of:

- `CONDITIONAL-FACTOR-PARTITION-COMPOSITION`: a supplied complete factor
  partition with unique allocated IDs admits exact separator contraction;
- `EXACT-SEPARATOR-STATE-GROWTH`: exact table coordinates or rational
  description grow, without a constructed distributed physical encoding;
- `CONNECTED-DOMAIN-CLOSURE-GIVEN-SEED`: a declared one-component proposal
  domain is closed from a supplied connected seed;
- `BOUNDED-KL-NO-RANK/ARITY-BOUND`: additive KL/evidence alone supplies no raw
  bound absent a carrier/metadata floor;
- `FACTORIZATION-SUFFICIENCY-FAILURE`: permitted separators fail to screen external
  history even after all registered marks are retained;
- `BLOCKED`: the finite arena itself is inconsistent or the executable cannot
  distinguish the claims above.

Combined verdicts are allowed only when their scopes are orthogonal and stated
explicitly.

## 7. Claim ceiling

Even a positive finite factor-message theorem would not yet establish:

- that SHARD derives the factor values or complete cover;
- that every physical history has bounded separator width;
- that arbitrary exact probabilities fit a fixed per-record information cap;
- a unique interacting click law;
- Lorentz invariance, a universal limiting speed, black-hole dynamics, quantum
  theory, cone roundness, four dimensions, or absolute scale.

Only after a candidate passes physical carrier, encoder, composition,
sufficiency, proposal, and seal gates may it be inserted into the v9 geometry
experiments.

## 8. Workflow

1. freeze this note;
2. write one self-contained exact D5 executable under `v10/code/`;
3. record every failed preregistered expectation rather than tuning it away;
4. write Paper 6 at the demonstrated constructive/no-go boundary;
5. run independent hostile mathematics, clean-room reconstruction, and
   ontology/locality reviews;
6. investigate every concrete opening before the next review round;
7. freeze hashes and a final receipt only after all three streams close.

## 9. Initial exact result before hostile review — historical wording

The first executable passes **29/29** exact checks. No floating-point value
decides a gate.

The positive result is conditional but real. Given supplied finite factor
tables with unique allocated IDs, the effective boundary table is computed from the
region alone; direct elimination equals nested separator contraction;
elimination order is invariant for the fixed factor multiset; relabeling is covariant; and
duplicate provenance is refused. Two different interiors with the same
positive-ray boundary message give the same audited continuation, while the
same unmarked boundary with different messages gives different predictions.

The result does not derive the law. Two positive factor tables on the same
scope satisfy every composition axiom and give different conditional
candidate-state probabilities. On a symmetric two-record separator, covariance leaves three different nonempty
scope families: the pair of one-leg proposals, the joint proposal, and their
union. Composition selects none of them.

The capacity/arity investigation strengthens the refusal:

1. complete parity ledgers have ranks `1/3/7`;
2. an `n`-record parity channel has rank one for every audited `n<=10`;
3. independent product channels have rank `n` and Fisher trace `3n/4` in the
   exact rational control;
4. positive rational channels approach zero evidence with no uniform positive
   floor;
5. choosing biases `delta_i=2^{-(i+3)}` gives

   $$
   D(P_i\Vert U)\le \chi^2(P_i\Vert U)=4\delta_i^2,
   \qquad
   \sum_{i=0}^{\infty}4\delta_i^2=\frac1{12}.
   $$

Thus arbitrarily many nonzero independent weak channels fit one finite KL
upper budget. Bounded additive KL/evidence cannot imply a raw arity ceiling
without an irreducible per-carrier cost.

Storage separates into two axes. An arbitrary width-`b` separator table has
`2^b` entries, while a width-one chain retains two entries through 32 steps
but its exact numerator size grows from 2 to 45 bits. Boundary width and exact
numeric precision are distinct resources. The loop control proves that
products of one-site marginals are not generally sufficient; the full joint
separator mark is load-bearing.

Connected growth also separates cleanly. A new record attached inside one old
component preserves that component and rewrites no old factor. It joins two
old components only when the proposal explicitly supplies legs into both.
The tensor algebra composes that multileg carrier but does not create it.

Initial verdict submitted for hostile review, now superseded:

```text
CONDITIONAL-LOCAL-COMPOSITION
+ DISTRIBUTED-BOUNDARY-GROWTH
+ CONNECTED-SEED-ONLY
+ CHANNEL-RANK-NONBOUND
+ SCOPE/VALUE-NONSELECTION
```

Round 1 rejected the `DISTRIBUTED-BOUNDARY-GROWTH`, `CONNECTED-SEED-ONLY`, and
unqualified `LOCAL-COMPOSITION` nouns. They are retained above only as the
historical initial verdict.

## 10. Hostile round-1 opening ledger and dispositions

All three reviewers returned **MAJOR REVISION** while independently
reproducing the numerical core.

1. **Probability type:** repaired. Primitive positive factors, nonnegative
   support controls, derived messages, and the identity are separate table
   kinds; every negative weight is rejected.
2. **Missing receipt cells:** repaired. Both chain parenthesizations, a
   branching tree, exactly-once separator ownership, and nested factor-ID reuse
   are executed.
3. **Ownership/type ceiling:** narrowed. Unique IDs plus a supplied factor
   partition detect literal double counting; they do not derive physical port
   types, semantic ownership, or a complete factor registry.
4. **Scope ontology:** repaired. Listed scope, essential variables,
   separability/irreducible pair interaction, primitive incidence, and derived
   message are tested separately. Directed transport remains absent.
5. **Gauge:** repaired to elimination-schedule invariance for one fixed factor
   multiset. Physical birth-order gauge remains open.
6. **Birth:** repaired to conditional state weighting of an already supplied
   candidate. Proposal/no-birth/eligibility/seal laws remain absent.
7. **Minimality:** scoped to arbitrary positive full-separator tests. It is a
   universal diagnostic ray, not necessarily minimal for a restricted future
   physical proposal class.
8. **Rank:** repaired to screen-relative covariance/Gram or Fisher rank. The
   false claim about adding relabeled channels was removed and the translated-
   channel countercontrol added.
9. **Weak channels:** scoped to additive KL/evidence. Explicit rational
   distributions now reconstruct TV and chi-square; carrier identity and
   exact description cost are not bounded by the `1/12` witness.
10. **State growth:** the chain now checks its recurrence, gcd-one primitive
    ray, and normalized rational bit growth. This is exact table-description
    growth, not an optimal algorithmic lower bound or physical information
    capacity.
11. **Structural zeros:** typed as controls only. Compatible equality support,
    zero fibers, all-zero refusal, incompatible-support refusal, and negative-
    weight refusal are explicit; a general fiberwise support category remains
    open.
12. **Verdict:** revised to

```text
CONDITIONAL-FACTOR-PARTITION-COMPOSITION
+ EXACT-SEPARATOR-STATE-GROWTH
+ CONNECTED-DOMAIN-CLOSURE-GIVEN-SEED
+ BOUNDED-KL-NO-RANK/ARITY-BOUND
+ SCOPE/VALUE-NONSELECTION
```

## 11. Round-2 claim

The repaired executable passes **34/34** exact checks. The positive theorem is
now explicitly limited to a supplied complete factor partition with unique
allocated IDs. Its state is a mathematical separator table, not a constructed
sealed boundary record. The exact conditional distribution concerns the state
of an already supplied candidate, not whether a record is proposed, born, or
sealed.

The live constructive opening is correspondingly sharper:

> derive a physical typed factor token from sealed holonomy, including its
> scope, direction, evidence, ownership, value, eligibility, and seal/no-birth
> rule, or prove that the existing record principles do not select one.
