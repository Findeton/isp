# From regional amplitudes and instruments to recorded histories

## A finite sewing theorem, exact durable histories, and the remaining selection problem

**Relativistic ISP / SHARD v10 — Paper 15**  
**Status:** final after hostile closure at `BRIDGE-CONDITIONAL` scope,
2026-07-11

## Abstract

Paper 14 proved that the current record principles do not select a unique
local interaction kernel and left regional amplitudes as a candidate bridge.
This paper constructs that bridge on a sharply delimited nontrivial class.

Finite sealed diamonds are presented as typed acyclic circuit generators in a
free strict symmetric-monoidal category, `FSDiam`.  Supplying one finite
linear kernel per generator induces a unique amplitude functor.  Typed
boundary gluing is matrix composition, disjoint union is tensor product, and
arbitrary topological evaluation schedules of a supplied diagram agree.  Thus
evaluation order is gauge.  Diagram generation, support and weights remain a
separate open law.  Overlapping diamonds retain physical causal order.

Protected orthogonal record ports and live output collars then turn the
amplitude network into a durable history theory.  Recorded branches have an
exactly diagonal decoherence functional; complete future instruments make
the finite cylinder weights projective; disintegration gives the next-record
conditional only after the whole-history law exists.  A reversible hidden-
memory circuit gives visibly non-Markov conditionals while all microscopic
composition remains local in that finite packet.  A no-third-party-dependency
exact receipt in `Q(sqrt(2),i)` passes 42/42 cells in normal and optimized
Python.

The positive result is structural, not a final theory of nature.  The
carriers, grammar, local kernels, boundary state, record instrument, protected
algebra and dimensional unit bridge are supplied.  The paper therefore
proves the narrower executable core
`FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED`.  The frozen
protocol verdict is `BRIDGE-CONDITIONAL`, because the physical action-to-kernel and
autonomous-instrument dictionaries remain supplied.  It does not select the physical
action, couplings, `3+1` phase, speed/metric scale or Newton constant.  Those
remain the goal of the next selector investigation.

## 1. Why this bridge matters

The earlier papers separated three questions that had repeatedly been mixed:

```text
What histories are allowed?          grammar
What weights do complete histories get? whole-history measure/amplitude
What is the next visible record?      conditional by disintegration
```

D12 proved that a supplied projective whole-history measure already gives the
next-click law.  D13 proved that locality, covariance, record permanence and
quantum consistency do not by themselves choose one kernel.  What remained
uncertain was whether supplied regional amplitudes and instruments could
realize the record picture on a fixed local DAG without a preferred
evaluation order.

The answer on the frozen finite class is yes.

## 2. The source category

Fix a finite typed signature `Sigma`.  Each boundary-port type `t` has a
finite-dimensional carrier `H_t`.  Each local diamond generator has an
ordered typed input word, an ordered typed output word and a supplied linear
map between the corresponding tensor products.

Abstractly, `FSDiam(Sigma)` is the free strict symmetric-monoidal category on this
signature:

```text
objects    finite ordered words of boundary-port types;
morphisms  finite acyclic typed circuit diagrams;
compose    glue exactly matching output and input words;
tensor     disjoint union/word concatenation;
identity   an eventless typed wire;
symmetry   an explicit typed wire permutation.
```

Calling the category free is a scope choice and an advantage: no geometric
equivalence beyond the symmetric-monoidal relations is silently assumed.
Ill-typed gluing is undefined.  Later theories may impose justified
diffeomorphism, gauge or refinement quotients; this theorem does not invent
them.  The executable implements its typed matrix image, not a syntax-tree
normalizer for string diagrams; the universal property is the abstract proof
and the code tests nontrivial image cells.

Sealed record ports carry an orthonormal pointer basis and are protected by
constructor admission.  Licensed future morphisms may read or copy a label
but may not change it.  The declared continuation requires a live-collar
capability: omission is ill-typed and the dead collar has zero continuation
amplitude.  Component-owned ports require an explicit join entitlement before
a primitive multi-component generator is admitted.  The origin law for that
entitlement is still not derived.

## 3. The amplitude functor

Assign to every generator `g:A->B` its supplied kernel
`K_g:H_A->H_B`.  There is a unique strict symmetric-monoidal functor

```math
Z:FSDiam(Sigma) -> Mat_C
```

with

```math
Z(id_A)=I_A,
Z(g o f)=Z(g)Z(f),
Z(f tensor g)=Z(f) tensor Z(g),
```

and permutation matrices for symmetries.  Existence follows because matrices
satisfy the category, tensor, interchange and symmetry relations; uniqueness
follows because every diagram is generated by those operations.

For external basis labels, a network component is

```math
Z_N(b_out,a_in)
= sum_{internal labels} product_{v in N} K_v(b_v,a_v).
```

This is the finite path-amplitude or regional-action form.  It sums unrecorded
alternatives coherently.  The receipt checks that two Hadamards interfere to
probability one, whereas inserting an intermediate record gives one half.
It also checks that locally row-normalizing kernels before composition gives
a different answer from normalizing the composite.  Classical per-click
normalization is therefore not a substitute for coherent gluing.

## 4. What evaluation-schedule gauge does—and does not—remove

A finite acyclic diagram has many possible topological evaluation schedules.
They are calculation procedures, not physical histories.  Any two linear
extensions of its dependency order are connected by adjacent swaps of
incomparable steps.  For disjoint steps the interchange law gives

```math
(g_1 tensor g_2)(f_1 tensor f_2)
=(g_1 f_1) tensor (g_2 f_2).
```

For internal contractions, finite distributivity and commutativity of scalar
addition/multiplication give the same result.  Hence every schedule evaluates
to the same `Z(N)`.

This is an evaluation-schedule gauge for one supplied DAG: its amplitude does
not depend on which incomparable contraction a calculator performs first.
When two diamonds
share a live port, their order is encoded in the diagram and cannot be
swapped.

The theorem does not generate the DAG, choose among alternative DAGs or derive
a locally computable next-extension law.  A whole-history formulation can
avoid a sequential universe commit order only after an amplitude/measure over
alternative complete diagrams is supplied.  Proper time and physical clock
intervals are motivational analogies here, not D14 outputs.

## 5. Boundary frames and one positive-cone dual-pairing cell

An independent unitary frame `G_e` may be chosen on every boundary carrier.
A local kernel transforms as

```math
K_v -> G_out K_v G_in^dagger.
```

Frames cancel pairwise on glued internal boundaries; transformed states and
effects leave every closed probability invariant.  The receipt checks this
exactly.

It also checks the dual positive-cone pairing under the exact nonunitary
matrix `diag(2,1/2) in SL(2,C)`:

```math
X -> G X G^dagger,
E -> (G^{-1})^dagger E G^{-1},
Tr(E X) -> Tr(E X).
```

The rank-two positive cone is preserved.  This is relevant to the earlier
spinor/channel route to Lorentzian geometry: Hermitian `2x2` matrices carry a
natural Lorentz-cone representation.  It is not yet a proof that a large
record web has a smooth Lorentz metric, round null cones or `3+1` dimensions.

## 6. A seal that also permits birth

The exact witness uses four-dimensional system and record carriers and a
two-dimensional live collar:

```math
V|j> = |j>_S |j>_R |1>_C.
```

The map is isometric.  Every branch contains a declared live collar.  Later
licensed system dynamics preserves the record label, and a fresh repeat-read
copies that label with exactly zero disagreement probability.  An explicit
record-flip control is rejected.

Unconditional protected future dynamics must be a direct sum of isometries or
CPTP channels.  At Kraus level,

```math
M_k=sum_r |r><r|_R tensor M_{r,k},
qquad sum_k M_{r,k}^dagger M_{r,k}=I\quad\hbox{for every }r.
```

It may respond to a record but cannot rewrite it; branchwise completeness
preserves the unconditional old-record marginal.  Postselecting a later
outcome can update probabilities assigned to an old record without changing
the record itself.  Arbitrary block-diagonal linear maps would not suffice.

The construction is conditional: the seal instrument, pointer basis and
protected algebra are inputs.  Autonomous environmental selection and the
physical cost/redundancy of records are not derived here.

## 7. From amplitudes to the complete history measure

For a supplied boundary state `rho`, recorded alternatives define bare system
class operators `C_alpha`.  Sequential local seal isometries accumulate
mutually orthogonal protected record strings `|alpha>`.  For a pure state the
record-extended branch vectors are

```math
|Psi_alpha>=C_alpha|psi> tensor |alpha>.
```

Therefore

```math
D_R(alpha,beta)
=<Psi_beta|Psi_alpha>
=delta_{alpha,beta} Tr(C_alpha rho C_alpha^dagger).
```

The bare system functional
`D_0(alpha,beta)=Tr(C_alpha rho C_beta^dagger)` is distinct and need not be
diagonal.  The record-extended partition is exactly decoherent.  Its diagonals are nonnegative
and normalized.  Born weighting appears once, at the state/effect pairing;
there is no later stochastic repainting of amplitudes.

Append any complete future instrument `{M_z}`.  Then

```math
sum_z p(alpha z)
=Tr[C_alpha rho C_alpha^dagger sum_z M_z^dagger M_z]
=p(alpha).
```

Induction makes all finite cylinder distributions projectively compatible.
A probability measure on the corresponding infinite product/history space
then follows under the usual projective-extension hypotheses.  On every
positive cylinder,

```math
p(z|alpha)=p(alpha z)/p(alpha).
```

This is the click law conditioned on the entire visible past.  It is derived
from the history measure, not added as a second law.

The executable builds the seals sequentially and verifies exact
normalization, decoherence and projectivity at depths one through three; the
completeness identity supplies the all-depth proof.

## 8. Non-Markov records from local reversible dynamics

The witness retains the first visible result in a hidden two-state memory,
makes the second visible result identical on both branches, and copies the
memory into the third visible result.  The total four-bit transformation is
unitary.  Nevertheless,

```text
P(z=1 | y=0,x=1)=1,
P(z=1 | y=0,x=0)=0.
```

Thus the current visible record does not screen off its earlier record.  One
integrated local packet now includes sequential protected seals, projective
cylinders, memory transport and the displayed conditionals.  A complete CPTP
reset of the hidden bit changes the visible process and makes both relevant
conditionals zero.

This proves a finite compatibility example.  It does not show that an
arbitrary full-history conditional admits bounded local memory, derive a
Barandes indivisible process, or select its path measure.  A general process
may require a growing boundary carrier.

## 9. Locality and no-signalling at the proved scope

Disjoint unitary cells obey interchange exactly.  The receipt also applies a
local Hadamard to one half of a Bell state and verifies that the other reduced
state is unchanged.  These are one finite no-signalling witness, not a
class-wide theorem for arbitrary linear kernels or multi-input generators.

They are not a derivation of continuum microcausality, Lieb–Robinson bounds,
the speed of light or black-hole causal structure.  Those require a selected
network grammar, spectrum and scaling limit.

## 10. Exact receipt

The no-third-party-dependency executable imports the previously reviewed exact
`Q(sqrt(2),i)` arithmetic and hash-locks that source.  Its 42 checks cover:

```text
typed units, associativity, tensor and interchange;
symmetry naturality/involution and ill-typed rejection;
direct and source-signature rejection of an unowned join;
sealed owned inputs included in primitive join entitlement;
protected identity through symmetry and fresh-record tensor;
owner-reassignment rejection;
evaluation-schedule equality;
coherent interference and normalization controls;
boundary-frame and SL(2,C) pairings;
isometric seal, enforced overwrite rejection, live/dead/missing collar,
permanence and fresh repeat-read;
explicit off-diagonal decoherence calculations;
sequential local seals, depth-1..3 normalization and projectivity;
an integrated projective non-Markov memory packet and CPTP deletion control;
one entangled no-signalling marginal.
```

Normal and optimized Python produce byte-identical stdout.  The frozen hashes
are recorded in the final D14 receipt after hostile review.

## 11. The theorem and its ceiling

**Finite regional-amplitude/instrument-to-history theorem.**  A finite typed acyclic regional
amplitude network with supplied local kernels, boundary state, protected
orthogonal record instrument and complete future instruments generates a
evaluation-schedule-independent, coherently glued, frame-covariant network of
durable records and a projective whole-history measure.  Its visible record
conditionals can be non-Markov.  No preferred total order is required to
evaluate or accumulate records within the supplied DAG; its generative
support/weight law remains open.

The exact executable proves:

```text
FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED.
```

The final D14 protocol verdict is `BRIDGE-CONDITIONAL`: the action-to-kernel and action/environment-to-record-
instrument maps are not derived.

It does not prove:

```text
one unique source category for nature;
one unique action or kernel family;
the Standard Model field content;
the values of dimensionless couplings;
the boundary/cosmological state;
autonomous record selection;
a stable 3+1-dimensional phase;
round continuum light cones;
the metre/second bridge, c, hbar or G.
```

## 12. The exact missing dictionary

A continuum, causal-set or asymptotic-safety candidate can enter the V9 tests
only after providing a complete dictionary:

```text
physical field configurations and regional action
  -> finite boundary carriers and gluing measure
  -> typed local diamond grammar and kernels
  -> boundary state and autonomous record instrument
  -> protected record algebra and live-collar birth rule
  -> record adjacency/influence observables
  -> dimensionless-to-proper-unit calibration.
```

Gauge theories may additionally require constraints, edge modes, boundary
charges and anomaly cancellation.  Gravity may require corner terms and a
sum over causal structure.  The finite theorem says what such a dictionary
must accomplish; it does not supply it.

## 13. What should be selected next

The next investigation must not tune another record-level coupling.  It must
compare action-level candidates on untouched evidence while requiring all of
the following in one packet:

1. local generally covariant regional composition;
2. a derived rather than declared record instrument;
3. a stable causal phase with Lorentzian propagation;
4. a mechanism selecting three spatial channel directions plus local clock;
5. scale generation and a gravity coupling;
6. a pre-registered quantitative record-web prediction.

The live routes remain causal-set quantum dynamics, an asymptotically safe
matter–gravity trajectory, or an experimentally inferred effective action.
The bridge proved here shows how any successful route could be translated into
the SHARD record language without a preferred contraction schedule.  A local
generative support/weight law remains separate.

## 14. Verdict

The generative architecture has advanced one decisive step:

```text
LOCAL REGIONAL AMPLITUDES
  + TYPED BOUNDARY GLUING
  + PROTECTED RECORD INSTRUMENTS
  -> EVALUATION-ORDER-FREE PROJECTIVE NON-MARKOV RECORD HISTORIES.
```

That arrow is now a theorem on the supplied finite `FSDiam` packet, not a
slogan.  The action-to-kernel map, autonomous record instrument, diagram law
and physical action are still not selected.  Paper 15 therefore closes a
conditional regional-amplitude/instrument-to-history bridge—not the full
action-to-record or action-selection problem.
