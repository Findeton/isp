# D14 hostile ontology/locality review — round 1

**Date:** 2026-07-11  
**Review verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Narrow mathematical core:** **SUPPORTED, AFTER CLAIM-SCOPE REPAIR**

## Executive finding

D14 contains a valid and useful finite theorem, but Paper 15 currently gives
that theorem a stronger physical reading than its ontology supports.

The supported result is:

> Given a supplied finite typed acyclic circuit, supplied matrices for every
> generator, a supplied boundary state, supplied orthogonal record
> instruments and supplied complete future instruments, matrix evaluation is
> independent of contraction schedule and defines compatible recorded
> cylinder weights.  One finite reversible dilation can give a non-Markov
> visible process.

That is a finite **circuit-evaluation and instrument-to-history bridge**.  It
does not yet show how the circuit is locally generated, how new record
components acquire permission to interact, or how a physical action produces
the record instrument and protected algebra.

Four implementation-level counterexamples make the distinction decisive:

1. `Mor.__post_init__` accepts an explicit overwrite of a sealed record;
2. the category accepts a seal and later continuation with no collar;
3. it accepts a two-component join with no connected-collar ownership
   witness; and
4. a record-block-diagonal linear map can preserve every label while changing
   normalized record weights.

The first three contradict frozen B0/B5/countercontrol language.  The fourth
shows that label nondemolition and probability permanence are not equivalent
without trace-preserving/instrument-completeness conditions.

Construction-schedule independence is also overread.  The proof removes the
order in which a **fixed supplied DAG is contracted**.  It does not generate
that DAG by a local click law or show that a whole-history sampler can advance
without globally supplied history data.  A free symmetric-monoidal
presentation is an excellent way to avoid an artificial evaluation clock;
it is not by itself a theory of local birth.

The record and memory cells remain scientifically valuable when narrowed.
The seal is a valid supplied isometry.  The repeat-read is exact.  Orthogonal
history strings give exact decoherence, and complete instruments give
projectivity.  The executed four-bit unitary is a genuine finite non-Markov
visible-history witness.  None of those facts derives an autonomous record
instrument, proves bounded local memory for arbitrary full-history laws, or
implements/selects a Barandes indivisible stochastic process.

B10 and B11 are the strongest parts of the paper.  They list the primitive
packet honestly, distinguish action-to-record translation from action
selection, specify the missing theory-dependent dictionary, and correctly
refuse a V9 cone/dimension holdout.  Those sections should become the scope
ceiling for the repaired theorem.

## Exact reproduction

The dependency-free receipt was copied to an isolated temporary tree and run
under normal and optimized Python.  Neither primary source nor primary packet
was modified.

```text
checks                         = 30/30
normal stdout SHA-256          = 05edee685a6905408d331cb3546db4edbc2bdaeae6fd154d6f0ec8d2bc80bdbe
-O stdout SHA-256              = 05edee685a6905408d331cb3546db4edbc2bdaeae6fd154d6f0ec8d2bc80bdbe
generated JSON SHA-256         = 9217316b6a98b3b8d42920214933c1d5832137abeb72fedee65a7fbcffc51c5f
primary JSON SHA-256           = 9217316b6a98b3b8d42920214933c1d5832137abeb72fedee65a7fbcffc51c5f
semantic SHA-256               = 3a1c766d1f82986f667b1897b817f44b51250db204659503592f545ce9807490
source SHA-256                 = 287c47f8cee8593956918b62f1c4786506b2af6dd5d9e5568acea73e7051c84f
dependency SHA-256             = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

The arithmetic receipt is reproducible.  This review's adverse verdict is
about the relationship between those exact cells and the stronger ontology
claims, not numerical failure.

## Opening ledger

| ID | Severity | Opening | Required repair |
|---|---:|---|---|
| O1 | **MAJOR** | Contraction-order independence of a supplied DAG is called construction-order gauge for the universe. | Rename it **evaluation-schedule gauge** and state that diagram generation/support and its whole-history weight remain primitive.  Prove a separate local generative quotient before making the wider claim. |
| O2 | **MAJOR** | The advertised protected type rule does not reject overwrites; `Mor` constructs the overwrite and an external predicate notices it afterward. | Split raw matrices from licensed morphisms.  Admission must reject sealed-label changes, and closure under composition, tensor and symmetry must be proved for arbitrary numbers/orderings of records. |
| O3 | **MAJOR** | The frozen “omitting a live collar prevents continuation” countercontrol is absent and false in the present category. | Make a live collar a required continuation capability/typestate, then execute a no-collar composition that fails at construction. |
| O4 | **CRITICAL FOR SHARD LOCALITY** | Ports have type and dimension but no component ownership.  A generator may silently join previously disconnected components. | Add lineage/component ownership and a connected-collar join entitlement, or explicitly withdraw D12-U6/SHARD-locality compatibility.  Add an unowned-join rejection control. |
| O5 | **MAJOR** | The paper says “action to records,” but the orthogonal record instrument, pointer basis and protected algebra are supplied independently of the action kernels. | Call the proved arrow `kernels + state + record instruments -> projective recorded histories`, or derive the record instrument from a theory-specific action/environment. |
| O6 | **MAJOR** | The general block-diagonal future algebra prevents relabeling but does not by itself preserve record probabilities. | Formulate future operations as CP instruments/channels.  Require trace preservation on each protected sector for unconditional marginal permanence and distinguish postselected updating from overwrite. |
| O7 | **MAJOR** | One hidden bit proves one three-time non-Markov witness, then the paper generalizes to “full history” being transported locally. | Restrict the statement to finite compatibility.  For a wider claim, bound the sufficient-memory carrier or allow explicitly growing carriers and prove projectivity/local transport for that same process. |
| O8 | **MODERATE** | The exact projective-history cell and the exact memory cell are different constructions; no single typed network is shown to possess both properties. | Build one integrated FSDiam history packet with sequential seals, complete future instruments, local memory transport, projectivity and the displayed non-Markov conditional. |
| O9 | **MODERATE** | Tensor interchange and one Bell/local-unitary marginal are described as microscopic locality, although arbitrary linear kernels and arbitrary multi-input generators remain allowed. | Limit B9 to one finite unitary no-signalling witness.  Add operational channel/instrument hypotheses before any class-wide no-signalling claim. |
| O10 | **MINOR** | The heading “Lorentz seed” invites more than the one diagonal `SL(2,C)` dual-pairing cell proves. | Call it a positive-cone dual-pairing cell.  Keep determinant/Minkowski norm, frame-link integration, network covariance and emergent Lorentz geometry open. |
| O11 | **PASS** | B10 lists primitive types, grammar, kernels, state, record instrument, protected algebra, frames and units. | Preserve this list and make every theorem headline subordinate to it. |
| O12 | **PASS** | B11 gives the missing action/state-to-diamond-to-record-to-unit dictionary and refuses V9 geometry. | Preserve the refusal.  No V9 holdout is licensed until a complete packet is independently selected and mapped. |
| O13 | **FORMAL BLOCKER** | Frozen countercontrols 5 and 7 are not both executed as stated, and hostile closure had not occurred when the packet printed the positive verdict. | After O1–O10 repairs, add the missing countercontrols, rerun all hostile rounds and only then freeze the protocol verdict. |

## O1 — evaluation order is not the generative click order

### What is proved

For one already supplied finite acyclic circuit `N`, all topological orders of
matrix contraction produce the same `Z(N)`.  The adjacent-incomparable-swap
proof is correct.  It is the familiar invariance of a finite tensor network
under reordering independent contractions.

The exact cell checks two decompositions of one disjoint diagram.  The theorem
then gives the general finite result from interchange and finite
distributivity.  Overlapping generators retain their diagram order.  This is
sound.

### What is not proved

The diagram itself is global supplied data.  `FSDiam` does not decide:

```text
which local event is enabled;
whether a new diamond is born;
which output collars it emits;
whether two existing components may join;
which complete diagram/history occurs;
what probability or amplitude belongs to alternative diagrams.
```

Consequently, D14 removes a global **evaluation scheduler** after a complete
diagram is fixed.  It does not yet remove a universe-wide commit mechanism
from a sequential generative simulator, because it supplies no such simulator
or local extension law.  Nor does it prove that a physical machine can choose
the next extension from only local data.  A whole-history amplitude approach
may avoid sequential construction altogether, but then the measure/amplitude
on alternative complete diagrams—not merely evaluation inside one diagram—is
the physical law.

This is exactly the distinction preserved in D12:

```text
construction presentation quotient
!= extension support and weights
!= local computability of the next extension.
```

### Required wording

Replace broad claims such as

```text
construction order is gauge;
no universe ledger or global commit clock is needed
```

with:

```text
For a fixed supplied finite FSDiam diagram, topological contraction order is
an evaluation gauge.  D14 does not generate the diagram or select a measure
over diagrams.  A local construction law remains open.
```

The analogy with proper time may remain motivational only.  The present
formalism contains causal chains in a DAG; it does not derive physical proper
time, clocks or local metric intervals.

## O2 — sealed records are filtered, not type-protected

The protocol says attempts to overwrite a sealed record “must be rejected.”
The theorem says the flip is rejected “by the protected type rule.”  The code
does something weaker:

```text
overwrite_mor = Mor(... overwrite matrix ...)
check(not preserves_record(overwrite_mor, 1, 1), ...)
```

`Mor.__post_init__` checks matrix dimensions only.  It successfully constructs
the forbidden morphism.  The external function then classifies it as not
record-preserving.  An independent probe reproduced:

```text
overwrite_constructed= True
overwrite_preserves_record= False
```

Thus “detected by a predicate” is exact; “rejected by the type/category” is
not.

This matters beyond terminology.  `preserves_record` is called manually for
one source index and one target index.  It does not define the morphisms of a
subcategory, track persistent record identity through permutations, require
every sealed input to have a matching sealed output, or prove closure for
multiple records.

### Required repair

Define separate layers:

```text
RawMap(source,target,matrix)
LicensedMor(raw_map, protection_certificate)
```

or make the constructor validate every sealed capability.  Record identity
must survive port reordering.  Prove identities, symmetry, tensor and
composition preserve the license.  The overwrite countercontrol must fail to
construct a `LicensedMor`, not first become one and then receive a false
predicate.

## O3 — live collar is a basis label, not a continuation capability

The seal witness places amplitude only on collar basis value `1`, and the code
correctly measures zero mass on value `0`.  That proves emission of one
declared label.  It does not prove that the label licenses future birth.

Nothing in `compose` requires a collar.  Nothing in `Mor` prevents a later map
from continuing on system and record ports alone.  A direct probe constructed
an isometric no-collar seal and composed a later identity:

```text
no_collar_continuation_constructed= True
```

The frozen countercontrol

```text
omitting a live collar prevents continuation
```

is therefore not merely unchecked; it is false for the implemented category.
Similarly, a future generator can accept the two-dimensional collar without
checking that its basis label is `live`.

### Required repair

Use a capability/typestate object rather than an unconstrained two-level
carrier.  Every continuation generator should consume the correct live
capability and emit declared successors.  A terminal record may omit it.  A
dead label must not satisfy a live input.  Execute all three controls:

```text
live collar -> continuation accepted;
no collar   -> continuation ill-typed;
dead collar -> continuation rejected.
```

This will turn “birth” from an amplitude label into a grammar statement.  The
physical law deciding when and how many collars are emitted will still remain
primitive unless independently derived.

## O4 — disconnected-component joining remains unsolved

D12's interaction-locality gate requires a previously recorded connected
collar owning every leg.  It forbids arbitrary graph search and silent joins
between disconnected components.

D14's `Port` contains only:

```text
kind, dimension, sealed flag.
```

There is no owner, component identifier, lineage, connected-screen witness or
join entitlement.  Any supplied multi-input generator can consume a tensor
word of matching port types.  A direct probe constructed a map

```text
q tensor q -> q
```

from two otherwise unrelated components:

```text
unowned_join_constructed= True
```

Calling that generator “local” does not make the legs previously connected.
The free category faithfully evaluates whatever join the signature supplies;
it does not decide whether that join is physically available.

This is the central unresolved answer to the user's earlier question about
how record components first meet.  D14 has not derived a join law.  It has put
the choice into the signature/grammar.

### Required repair

Choose one of two honest paths:

1. **Implement D12 U6.**  Add ownership and connected-collar types, require a
   join certificate owned by a common recorded ancestor or connected screen,
   and reject a cross-component join without it.
2. **Narrow FSDiam.**  State that it is a generic typed circuit category that
   does not yet implement SHARD interaction locality or solve component
   joining.

Either path must add a negative unowned-join test and explain how a valid join
capability is born without a global graph search.

## O5 — the action does not derive the records

D14 supplies separately:

```text
local kernels;
boundary state;
record/seal instrument;
pointer basis;
protected future algebra;
complete future instruments.
```

The exact record is produced because `seal_birth_mor` is explicitly inserted.
Orthogonal history strings decohere because orthogonal record carriers are
explicitly attached.  The action kernels do not select that instrument,
pointer basis or protection rule.

Therefore the theorem is not, in the strong causal sense,

```text
action -> records.
```

It is:

```text
typed kernels + state + supplied record instruments + protected algebra
  -> coherently evaluated projective recorded histories.
```

That is still a real bridge: it proves compatibility and composition once the
record packet is present.  But Paper 15's statements that the action-to-record
bridge is “closed” or that records are generated by regional action amplitudes
should be narrowed.  The autonomous instrument remains precisely the
action-to-record dictionary item B11 says is missing.

This distinction is separate from action **selection**.  D13 proved current
principles do not select a unique kernel.  D14 does not attempt to overturn
that result.  Even if the instrument were derived from a supplied action,
selecting which physical action nature uses would remain another problem.

## O6 — label nondemolition is not probability permanence

The theorem's licensed algebra is written

```math
M=\sum_r |r\rangle\langle r|_R\otimes M_r.
```

Such a map cannot relabel `r`.  For arbitrary supplied linear `M_r`, however,
it can change the norm of different record sectors differently.  Starting
with record weights `(1/2,1/2)`, choose `M_0=2I` and `M_1=I`.  After applying
the map and normalizing, the weights are

```text
(4/5,1/5),
```

although neither label was overwritten.

The exact receipt avoids this problem because its tested later map is a
system-only unitary tensored with identity on record and collar.  That cell
does preserve the record marginal.  The general theorem is broader than the
cell.

### Required repair

Distinguish three claims:

1. **label nondemolition:** no matrix element connects different `r`;
2. **unconditional marginal permanence:** the summed future channel is trace
   preserving in every protected sector; and
3. **postselected inference:** conditioning on a later outcome may update the
   probability of an old record without physically overwriting it.

Define the future algebra with CP instruments or isometries and state the
trace/completeness hypotheses required for claim 2.  Do not infer probability
permanence from block support alone.

## O7/O8 — finite memory is not a general full-history locality theorem

The executed memory circuit is genuine.  It carries the first bit in a hidden
bit, makes the current visible value the same on both branches and later
reveals the hidden bit.  It proves:

```text
reversible enlarged dynamics
is compatible with
one non-Markov three-time visible process.
```

It does not prove that an arbitrary full-history conditional has a bounded
local sufficient statistic.  A general conditional may require memory that
grows with history length.  One can transport a complete finite prefix in an
ever-growing carrier, but that is different from a fixed finite local memory
law and must be stated explicitly.

The paper's sentence that the needed past information “is transported locally
in physical state” is therefore valid for the displayed bit-memory process,
not for every whole-history measure.

There is also an integration gap.  The projective-history receipt uses
repeated Hadamard/projector class operators and appends orthogonal record
strings.  The non-Markov receipt uses the separate four-bit memory circuit.
No one typed multidiamond packet is shown to have:

```text
sequential protected seals;
complete future instruments;
depth projectivity;
local hidden-memory transport;
the displayed non-Markov conditional.
```

This is repairable, but the current receipt proves the properties in separate
cells rather than one realized process.

### Barandes/Egri boundary

Paper 15 should carry forward D12/D13's literature boundary explicitly.  A
finite hidden-memory dilation shows compatibility with non-Markov visible
histories.  It does not establish a general Barandes stochastic-quantum
correspondence, prove indivisibility, select a path measure, or show uniqueness
of the stochastic implementation.  Disintegration supplies conditionals only
after a particular whole-history measure has been supplied/constructed.

The safe claim is:

```text
FSDiam amplitudes plus supplied instruments can realize at least one finite
visible non-Markov recorded process.  Barandes-style full-history dynamics is
neither derived nor selected.
```

## Whole-history and projective-law scope

The exact diagonal decoherence calculation is correct because every history
is tensored with a mutually orthogonal record string.  Positivity and
normalization follow for the supplied state and complete projective
instrument.  The completeness identity correctly proves finite-depth
projectivity, and finite-alphabet extension can produce an infinite path
measure under the usual extension hypotheses.

The ontology ceiling is important:

- exact decoherence is conditional on inserting perfect orthogonal protected
  records;
- the receipt does not derive environmental pointer selection;
- `recorded_branch` attaches the history register algebraically rather than
  executing sequential `seal_birth_mor` generators;
- the infinite history is not itself a morphism of the finite category; it is
  an extension of the compatible finite cylinder family; and
- disintegration recovers a next-record conditional but does not compute the
  grammar/support of which next diamonds may exist.

Thus B6/B7 are strong conditional mathematical results, not an autonomous
birth/click law.

## Locality and no-signalling scope

The interchange law is exact for morphisms placed on disjoint tensor factors.
The Bell-state cell correctly shows that one local unitary on the first qubit
does not change the second reduced state.

Those are necessary witnesses, but `FSDiam` also permits arbitrary supplied
linear maps and arbitrary multi-input generators.  Matrix functoriality alone
does not make every generator a normalized quantum channel or decide which
ports are physically spacelike.  Without CP/trace-preserving instrument
structure, a class-wide operational no-signalling theorem is not even
formulated.

Paper 15 mostly states the limitation correctly, but phrases such as “all
microscopic composition remains local” and “finite sealed diamonds” can be
read too broadly.  The receipt proves:

```text
formal tensor-factor separation + one unitary marginal cell.
```

It does not prove continuum microcausality, finite propagation speed,
relativistic locality, locality of the extension grammar or the absence of
silent component joins.

## `SL(2,C)` cell

The exact cell is sound at its stated algebraic core.  For
`G=diag(2,1/2)`, it checks `det G=1`, positive-cone preservation for one
diagonal state and invariance of the dual pairing

```math
Tr(E X).
```

The general dual-congruence identity is elementary and valid.  It is not a
network Lorentz theorem.  The receipt does not test the Hermitian determinant
as a Minkowski norm, noncommuting boosts/rotations, links between independent
vertices, causal-cone propagation, metric emergence or `3+1` selection.

Paper 15 explicitly disavows most of those conclusions.  The remaining repair
is presentational: replace “the Lorentz seed” by “one `SL(2,C)` positive-cone
dual-pairing cell,” unless the stronger integrated representation is added.

## B10 — action scope

**PASS, with headline synchronization required.**

The protocol, theorem note and Paper 15 list the primitive packet accurately:

```text
types/carriers;
local grammar;
local kernels;
boundary state;
record instrument and pointer basis;
protected future algebra;
frame/pairing rule;
dimensionful unit bridge.
```

They also say functoriality constrains composition but does not select values.
This is the correct conclusion after D13.  The problem is not B10's content;
it is that the title, abstract and final verdict sometimes sound stronger than
this ceiling.  Make “given all B10 inputs” visible in every theorem headline.

## B11 — downstream dictionary and V9 refusal

**PASS.**

The missing dictionary is stated with appropriate specificity:

```text
physical region/action/state
  -> boundary carriers and gluing measure
  -> typed grammar and kernels
  -> autonomous record/decoherence instrument
  -> protected algebra and live-collar birth rule
  -> record adjacency/influence observables
  -> metre/second/gravity calibration.
```

This correctly shows why D14 does not license V9 geometry.  A compositional
bridge for supplied finite matrices is not an independently selected action,
does not yield the V9 record web and does not predict its cone or dimension.
The refusal to run a holdout is mandatory, not excessive caution.

D9's conditional selection of `theta=pi/4` inside one frozen preparation
family does not change this verdict.  Its proposed one-number geometry map
failed fresh seeds and it never supplied the complete B11 dictionary.

## Frozen countercontrol audit

| Countercontrol | Result |
|---|---|
| ill-typed boundary gluing | **PASS.** Dimension/type mismatch raises. |
| sealed-record overwrite | **PARTIAL/FAIL AS WORDED.** Predicate detects it, but `Mor` accepts it. |
| intermediate record changes interference | **PASS.** `1` versus `1/2`. |
| local row normalization changes composition | **PASS.** Exact inequality. |
| omitting live collar prevents continuation | **FAIL/MISSING.** No test; present category permits continuation. |
| hidden-memory deletion changes visible process | **PARTIAL.** Hidden-memory realization is executed; deletion control is not separately evaluated. |
| global schedule label observationally absent | **PARTIAL.** Two schedules agree and no label is stored, but no schedule-labelled presentation/quotient control is executed. |

Because the frozen protocol says a promised control missing yields
`INCOMPLETE-INVESTIGATION`, the positive semantic packet is premature even
before the conceptual openings are considered.

## Gate adjudication

| Gate | Round-1 result |
|---|---|
| B0 typed category | **FAIL/PARTIAL.** Ordinary port types work; protected-record admission, ownership and join locality do not. |
| B1 category/coherence | **PASS for the free strict symmetric-monoidal matrix evaluation.** |
| B2 construction-order gauge | **PASS only as fixed-diagram evaluation-schedule gauge; MAJOR overread as generative construction law.** |
| B3 coherent gluing | **PASS for the finite interference and normalization controls.** |
| B4 local frame/gauge covariance | **PASS at unitary internal-frame and one `SL(2,C)` pairing-cell scope only.** |
| B5 records and birth | **PARTIAL/FAIL.** Isometric seal and reread pass; protected admission, general marginal permanence and collar-required continuation fail. |
| B6 whole-history decoherence | **PASS conditional on supplied perfect orthogonal history records.** |
| B7 projective history law | **PASS for supplied complete instruments and finite cylinders; infinite extension remains under stated hypotheses.** |
| B8 visible non-Markov memory | **PASS as one finite compatibility witness; not a general local full-history theorem.** |
| B9 locality/no-signalling | **PASS for tensor interchange and one local-unitary Bell marginal only.** |
| B10 action scope | **PASS in body text; headline synchronization required.** |
| B11 downstream handoff | **PASS.  Dictionary explicit and V9 holdout correctly refused.** |
| B12 hostile closure | **OPEN.  This review finds major repairs.** |

## Concrete repair order

1. **Repair the category first.**  Define licensed morphisms, persistent
   record identities, live capabilities, owner/component lineages and join
   entitlements.  Prove categorical closure.
2. **Add the three decisive negative tests.**  Overwrite must fail admission;
   no-collar continuation must be ill-typed; unowned component join must be
   rejected.
3. **Repair the future-algebra theorem.**  Use CP instruments/isometries and
   state the trace-preserving conditions for unconditional record marginal
   permanence.
4. **Narrow construction gauge.**  Separate fixed-network evaluation order
   from local network generation and from weights over alternative networks.
5. **Build one integrated recorded-memory network.**  Execute sequential
   seals, local memory carriage, complete future instruments, projectivity and
   the non-Markov conditional in one typed packet.
6. **Repair the headline.**  Until an autonomous instrument is derived, call
   the theorem a finite supplied-kernel-and-instrument-to-history bridge.
7. **Retain B10/B11 unchanged in substance.**  They correctly keep action
   selection, physical fields, couplings, units, gravity and V9 geometry open.
8. **Run the next hostile round before freezing a positive protocol verdict.**

## Verdict

The exact algebra is not refuted.  The free-category evaluation theorem,
finite coherent contraction, orthogonal-record decoherence, projectivity,
repeat-read and visible non-Markov witness all survive at narrowed scope.

The frozen D14 verdict does not yet survive because protected records and live
collars are not enforced by the implemented category, disconnected-component
joining is unconstrained, probability permanence is overgeneralized, and
evaluation-schedule independence is promoted into a generative no-global-
clock result.

The honest current result is:

```text
FIXED FINITE FSDiam DIAGRAM EVALUATION             SUPPORTED
SUPPLIED ORTHOGONAL INSTRUMENT -> PROJECTIVE LAW  SUPPORTED
ONE FINITE LOCAL-MEMORY NON-MARKOV WITNESS        SUPPORTED
PROTECTED-MORPHISM CATEGORY                        NOT YET IMPLEMENTED
LIVE-COLLAR-REQUIRED BIRTH                         NOT YET IMPLEMENTED
CONNECTED-COMPONENT JOIN LAW                       NOT YET IMPLEMENTED
LOCAL GENERATION WITHOUT A GLOBAL COMMIT LAW       NOT PROVED
ACTION-DERIVED RECORD INSTRUMENT                    NOT PROVED
ACTION SELECTION / V9 GEOMETRY                      OPEN AND CORRECTLY WITHHELD
PROTOCOL VERDICT                                    INCOMPLETE-INVESTIGATION
```

After the listed repairs, a positive finite bridge theorem is plausible.  It
must remain a conditional translation theorem until the action, record
instrument, local extension grammar, join/birth law and physical scales are
derived or independently selected.
