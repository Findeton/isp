# Atomless regions and the missing gluing law

## A point-free syntax does not yet make a physical regional process

### Abstract

We investigate whether a point-free atomless region algebra, exact regional
questions, and composable open-graph presentations already determine a
physical regional ontology and one dynamical law.  The answer is negative at a
precise boundary.  Finite unions of binary cylinders form an atomless Boolean
algebra: every nonzero region has a proper nonzero subregion.  Positive
finitely additive valuations carry a complete two-port restriction
instrument, with the zero-probability port retained.  Three finite open-tree
factorizations also compose by genuine graph pushouts.

None of those results supplies a total assignment from regional fillings to
physical processes.  The displayed boundary family lacks an adaptive
frontier, identities at its nontrivial objects, tensor composition,
naturality, and a rule selecting a global law from compatible overlapping
regional data.  The last omission is witnessed exactly: two different
probability laws on three binary regions have identical `AB` and `BC`
marginals while giving probabilities `1/2` and `1` to `A=C`.

The earliest conclusion is therefore **blocked at boundary gluing**.  Raw
atomlessness survives only as syntax; the physical regional quotient, a
horizontal process, dynamic locality, and an indivisible transition law are
unconstructed.  This negative result also exposes a methodological error.
Indivisibility cannot be obtained by building regional laws, instruments,
record writers, and relational rewrites separately and welding them later.
A positive successor must preregister one explicit transition-law family on
complete relational configurations and derive every regional shadow from it.

## 1. The result without technical language

A map may divide a territory into arbitrarily small named districts.  That
fact alone does not show that the districts are physical objects, nor that the
map knows how physical events compose.  Subdivision is a property of the
description.  Physical meaning requires a law that makes distinctions
observable, transports them consistently, and agrees when regions are glued.

The construction studied here gets several things exactly right.  Its region
language contains no underlying points.  Every nonempty region can be divided
again.  Questions about a region have two complete branches, including a
branch of probability zero.  Open binary trees can be glued by actual
pushouts rather than by placing diagrams side by side.

The construction nevertheless stops before dynamics.  It has no rule taking
every allowed open filling to a physical process, no identities at most of
its declared boundaries, and no tensor or comparison law.  More decisively,
two overlapping local probability tables do not determine their global
completion.  Choosing one completion by conditional independence, maximum
entropy, sparsity, or canonical order would add a law; it would not derive
one.

This is not an objection to ordinary probability.  Ordinary probabilities are
appropriate for mutually exclusive configurations and durable outcomes.  The
problem is assuming that arbitrary intermediate descriptions are lawful
probabilistic divisions.  Barandes's indivisible-stochastic formulation makes
that distinction explicit: a stochastic law may provide ordinary transition
probabilities while refusing a positive factorization through an arbitrary
inserted cut [1].

## 2. What the primitive objects are

Let a binary word be a finite string in `{0,1}`.  The cylinder `C(w)` denotes
all infinite binary continuations of `w`.  A presentation region is a finite
union of cylinders, reduced to a prefix-free antichain.  The empty antichain is
`0`; the cylinder of the empty word is `1`.

The Boolean operations are induced by union, intersection, and complement of
cylinders.  They can be calculated at any common finite depth and reduced
again by replacing sibling cylinders `C(w0)` and `C(w1)` with `C(w)`.

This language is point-free in a limited, exact sense: its algebraic elements
are regions rather than fundamental point labels.  The infinite binary paths
used to explain cylinders are not promoted to physical points.  The same
algebra may be characterized abstractly as the countable atomless Boolean
algebra.

Nothing in this definition makes an element a **physical** region.  A physical
region would have to be a class preserved by every generated physical future,
with Boolean operations and process gluing descending to that class.  The
distinction between presentation region and physical region is load-bearing
throughout the paper.

## 3. Raw atomlessness

### Theorem 1 — the prefix region algebra is atomless

Every nonzero finite union of binary cylinders contains a proper nonzero
subregion.

### Proof

Write a nonzero region `A` as a reduced prefix-free union and choose one word
`w` in its antichain.  Set

$$
B=C(w0).
$$

Then `B` is nonzero and `B <= A`.  It is proper because `C(w1)` is nonzero,
disjoint from `B`, and contained in `A`.  Equivalently,

$$
C(w)=C(w0)\mathbin{\vee}C(w1),
\qquad
C(w0)\mathbin{\wedge}C(w1)=0.
$$

Thus no nonzero element is an atom.  ∎

In the finite display used for exact checks, nine registered nonzero regions
all split properly.  This finite count is only a control; the proof above is
the all-depth result.

### Why the theorem is not yet ontological

Raw atomlessness need not survive an operational identification.  Two exact
controls make this concrete.

First, define the dyadic valuation

$$
\mu(C(w))=2^{-|w|}
$$

and extend it additively to prefix-free unions.  The left and right halves
have the same value,

$$
\mu(C(0))=\mu(C(1))=\frac12,
$$

but meeting both with `C(0)` gives

$$
\mu(C(0)\wedge C(0))=\frac12,
\qquad
\mu(C(1)\wedge C(0))=0.
$$

Equality of scalar volume is therefore not a Boolean congruence.

Second, evaluation at the all-zero branch defines a Boolean character

$$
\chi(A)=
\begin{cases}
1,&\text{if the all-zero branch lies in }A,\\
0,&\text{otherwise.}
\end{cases}
$$

Its image is the two-element Boolean algebra, which is atomic.  Hence an
atomless presentation algebra can have an atomic quotient.  Post-quotient
atomlessness must be proved for the physical equivalence relation actually
generated by the law; it cannot be inherited from syntax.

## 4. Exact regional questions

Let `nu` be a positive finitely additive valuation on the Boolean algebra.  For
each region `C`, define two subnormalized branches by

$$
(Q_C^1\nu)(E)=\nu(E\wedge C),
\qquad
(Q_C^0\nu)(E)=\nu(E\wedge \neg C).
$$

### Theorem 2 — restriction is a complete positive two-port instrument

For every `C`:

1. `Q_C^0` and `Q_C^1` are positive and affine;
2. both ports remain typed even when one branch is zero;
3. their nonselective sum is the identity map:

   $$
   Q_C^1+Q_C^0=I.
   $$

### Proof

Positivity follows because meets of positive regions remain positive inputs to
`nu`.  Affinity follows from finite additivity and linearity in the valuation.
Since `C` and `not C` are disjoint and join to `1`,

$$
\nu(E\wedge C)+\nu(E\wedge\neg C)=\nu(E)
$$

for every `E`.  The branch maps are not normalized independently.  In
particular, asking the unit region has a zero `0` branch, but the typed port is
retained.  ∎

Averaging the two branches would give `I/2`, not `I`.  Dropping the zero port
would change the type.  These elementary controls matter because branchwise
renormalization or port deletion can silently turn an instrument into a
different object.

The theorem describes static conditioning on one fixed Boolean algebra.  It
does not create a new region, write a durable record, define a lawful temporal
division, or assign a process to an open filling.

## 5. Finite trees and genuine graph pushouts

Four complete uniform frontiers are displayed:

$$
\{\epsilon\},\quad
\{0,1\},\quad
\{00,01,10,11\},\quad
\{000,001,010,011,100,101,110,111\}.
$$

The nonuniform set

$$
\{0,10,110,111\}
$$

is also prefix-free and complete, because its dyadic weights sum to one.  It
is absent from the displayed uniform-depth boundary factory.  This is the
smallest explicit reminder that an adaptive decision tree does not in general
have a uniform-depth frontier.

The full depth-three binary tree has `15` vertices and `14` edges.  Three
different cuts—after depth one, after depth two, and after both—compose by
tagged pushout to the same boundary-fixed graph.  These are genuine categorical
composition controls.  Structured cospans are a standard way to formalize
open systems whose apices compose by pushout [2].

The positive graph result has a strict scope.  A graph pushout does not itself
supply a map on valuations, an instrument, or a functor from fillings to
processes.  In the displayed assignment, only the one-port boundary has an
active empty-process identity.  The two-, four-, and eight-port boundaries do
not.  There is also no total filling-to-process assignment, tensor factory, or
nontrivial vertical-horizontal naturality square.

Consequently the tree algebra and graph-cospan algebra remain separate finite
controls.  Calling their conjunction a process would repeat the error of
placing compatible modules beside one another and treating proximity as
composition.

## 6. Overlapping regional data do not select a global law

Let `A`, `B`, and `C` be binary regional labels.  Consider two normalized
global laws.

The first is uniform:

$$
P_0(a,b,c)=\frac18
$$

for all eight triples.  The second enforces `A=C`:

$$
P_1(a,b,c)=
\begin{cases}
\frac14,&a=c,\\
0,&a\ne c.
\end{cases}
$$

### Theorem 3 — the same `AB` and `BC` shadows admit distinct global laws

Both laws have

$$
P(A=a,B=b)=\frac14,
\qquad
P(B=b,C=c)=\frac14
$$

for every binary pair, but

$$
P_0(A=C)=\frac12,
\qquad
P_1(A=C)=1.
$$

### Proof

For `P_0`, marginalizing either omitted binary variable adds two terms of
weight `1/8`.  For `P_1`, fixing either `AB` or `BC` leaves exactly one allowed
value of the omitted endpoint, of weight `1/4`.  The equality event contains
four of the eight uniform triples but every supported triple of `P_1`.  ∎

Thus the two overlapping shadows do not determine the complete object.  A
Markov or conditional-independence condition would select the uniform
completion in this example, but that condition is additional law data.  The
same is true of maximum entropy, sparsity, canonical ordering, or a preferred
hash.

The variables here are simultaneous regional labels, not three successive
measurements.  The construction is therefore a classical gluing diagnostic,
not a microscopic dynamics.  It does not say that the missing physical object
must be a classical copula.  If alternatives can reconverge before a lawful
division, assigning ordinary exclusive probabilities to them may erase the
interference relation.  Quantum measure theory similarly distinguishes a
history-level generalized measure from ordinary additive probabilities on
arbitrary partitions [3].

## 7. The earliest stopping point

The gates are ordered because a later calculation cannot repair an earlier
typing failure.

1. **Normalization passes.**  The restriction branches are positive and sum
   exactly to the identity.
2. **Raw atomlessness passes.**  The prefix Boolean algebra has no atoms.
3. **Boundary gluing fails.**  The displayed construction lacks:

   - an adaptive-frontier factory;
   - active identities at all declared process boundaries;
   - a filling-to-process assignment;
   - tensor composition;
   - a nontrivial naturality square;
   - a selector deriving a global law from the overlapping regional data.

The strict result is therefore:

> **The construction is blocked at boundary gluing.**

The narrower positive results remain true: raw atomlessness, exact restriction
questions, three finite graph pushouts, and explicit global-extension
underdetermination.  They do not jointly establish a physical atomless region
algebra or a horizontal process.

## 8. Indivisibility was not operationalized

The deeper failure is architectural.  The programme sought an indivisible
regional law while continuing to construct regional kernels, instruments,
record writers, comparison maps, and relational rewrites as neighboring
objects.  Even perfect typing of each module would not make their collection
one law.

An indivisible-law construction must reverse the order:

1. specify one complete configuration type;
2. preregister one explicit transition-law family

   $$
   \{\Gamma_\lambda:\lambda\in\Lambda\};
   $$

3. derive `AB`, `BC`, lawful-division instruments, memory updates, delayed
   records, comparison maps, and relational rewrites as restrictions or
   compositions of that same `Gamma_lambda`;
4. exhibit both a lawful division and a native or class-relative failure of
   factorization at a nondivision cut;
5. mutate `Gamma_lambda` while holding its kinematic interfaces fixed and
   recompute every dependent shadow.

The family and parameter domain must be frozen before testing which
constraints they pass.  Otherwise the gates describe a desired future object
rather than an experiment on a candidate law.

A separate finite executable-law consistency test can verify that a software
or mathematical architecture propagates one primitive through its dependent
objects.  That is useful plumbing.  It contributes no physical transition
probability, configuration catalogue, division doctrine, record, or relational
geometry to the present construction.

The primitive state of a successor should also avoid assuming its conclusions.
A schematic payload may contain raw relational structure, matter/process
content, and candidate memory,

$$
X=(G_{\rm raw},M,K),
$$

with every additional boundary or native-history context declared in the
source type.  `K` is not a record merely by name: record status requires
same-law recoverability after every licensed continuation.  Likewise
`G_raw` is not geometry merely by name.  Order, contact, valuation, distance,
and curvature are derived readings only after they are calibrated and consumed
by the law; any primitive reading must instead be priced as kinematics.

Barandes provides the relevant architectural precedent: transition
probabilities on a configuration space can be fundamental while Hilbert-space
objects remain representational, and arbitrary positive intermediate
factorization need not exist [1].  That precedent does not provide the
point-free relational catalogue, changing support, record criterion,
backreaction, or numerical law required here.

## 9. Ontology ledger

| Object or claim | Status here | What would be needed for promotion |
|---|---|---|
| Binary prefix word | representation | never a physical point merely by use |
| Prefix-antichain region | atomless syntax | faithful complete process quotient |
| Dyadic valuation | mathematical control | law selection and calibrated physical role |
| Restriction question | static mathematical response | same-law process, records, and contextual closure |
| Tree frontier | presentation boundary | total adaptive boundary factory and process assignment |
| Open binary graph | cospan presentation | filling-to-process functor with identity, tensor, and naturality |
| Graph pushout | finite categorical control | equality of derived physical process composites |
| `AB` and `BC` tables | regional shadows in a diagnostic | derivation from one complete transition law |
| Physical atomless region algebra | unconstructed | faithful contextual/gluing quotient and post-quotient splitting |
| Durable record | unconstructed | writer and delayed reader derived from one law over a closed future grammar |
| Actual relational history | ontological candidate | co-reference, compatibility, and actualization doctrine |
| Indivisible `Gamma` | unconstructed | explicit preregistered family and division/nondivision witnesses |
| Geometry | unconstructed | relational readings calibrated, changed, and used in later responses |
| Hilbert/history objects | representation if introduced | representation-independent predictions and gauge accounting |
| Actualization mechanism | absent | a law or an explicitly retained postulate |

One actual compatible relational history may be postulated, with alternative
configurations serving as counterfactual arguments of the law.  Nothing in the
present normalization, branching, or graph composition selects which
successor becomes actual.

## 10. What has and has not been established

### Established

- a point-free atomless **presentation** algebra;
- an exact positive complete two-port restriction instrument on that algebra;
- retained zero ports and summation rather than averaging;
- complete uniform and adaptive prefix frontiers as mathematical objects;
- three exact finite graph pushouts;
- a boundary-identity and adaptive-frontier obstruction;
- two globally distinct `ABC` laws with identical `AB` and `BC` shadows;
- the earliest boundary-gluing obstruction.

### Not established

- an atomless physical regional referent;
- a complete contextual or gluing congruence;
- a total horizontal classical or quantum process;
- stable records or lawful stochastic divisions;
- one indivisible transition law;
- dynamic locality, contact, or causal order;
- reciprocal matter–relational backreaction;
- operational chronology, extensive physical valuation, metric, connection,
  curvature, stress response, or gravity;
- dimension, signature, Lorentz invariance, continuum recovery, quantum field
  theory, particles, a Hamiltonian, vacuum, constants, or predictions;
- selection of a law or an actualization mechanism.

The negative conclusion is constructive rather than merely skeptical.  It
locates the first missing object and preserves every theorem below it.  The
next physical investigation should not add another neighboring module.  It
should begin with one explicit, preregistered `Gamma_lambda` family and ask
whether regional descriptions, memory-to-record promotion, relational change,
and reciprocal response really descend from that one law.

## References

1. Jacob A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,”
   arXiv:2507.21192 (2025), <https://arxiv.org/abs/2507.21192>.
2. John C. Baez and Kenny Courser, “Structured Cospans,”
   *Theory and Applications of Categories* **35** (2020), arXiv:1911.04630,
   <https://arxiv.org/abs/1911.04630>.
3. Rafael D. Sorkin, “Quantum Mechanics as Quantum Measure Theory,”
   *Modern Physics Letters A* **9** (1994), arXiv:gr-qc/9401003,
   <https://arxiv.org/abs/gr-qc/9401003>.
