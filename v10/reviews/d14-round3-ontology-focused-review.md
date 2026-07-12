# D14 focused round-3 ontology/locality review

**Date:** 2026-07-11  
**Review verdict:** **PASS AT `BRIDGE-CONDITIONAL` SCOPE**  
**Executable core:** **`FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED`**

## Executive finding

The two category blockers from round 2 are closed.

Protected records now carry persistent source-to-target correspondences.
Those correspondences propagate through composition and tensor product and
transform correctly under structural symmetry.  A protected two-record swap
is admitted, swapping twice is the identity, and changing the owner attached
to a persistent record identity is rejected.

Primitive ownership admission is also moved into `Mor` itself.  The direct
constructor and `Signature.declare` both reject a two-owner primitive without
the declared entitlement; mixed owned/ownerless live inputs are rejected; and
the declared `("A","B")` entitlement is admitted.  `Signature` now delegates
to the same constructor rather than implementing a separate, bypassable rule.

The entitlement remains supplied grammar.  It names the input owners; it does
not prove that nature generated a prior connected collar owning those legs.
Paper 15 and the theorem note explicitly leave its origin law open.  The
generic ownerless packet is not thereby upgraded into D12-U6 interaction
locality.  This is the correct ceiling for `BRIDGE-CONDITIONAL`: the theorem
evaluates a supplied typed grammar and instruments; it does not derive that
grammar, its join opportunities, the action-to-kernel map or the autonomous
record instrument.

The 41-check receipt reproduces byte-for-byte under normal and optimized
Python.  Sequential seals, exact recorded decoherence, projectivity, the
integrated finite non-Markov memory packet, CPTP memory deletion, repeat-read,
the finite no-signalling cell and the positive-cone pairing remain intact.

No fatal, major or moderate ontology/locality blocker remains at the narrowed
scope.  Three quotable phrases should still be hardened: a motivational
sentence says an action/amplitude “generates” the record picture; the theorem
summary says no global physical commit order is required; and the final arrow
says “CLOCK-FREE.”  The surrounding text already restricts all three to
evaluation inside a supplied DAG with supplied record instruments, so these
are nonblocking wording repairs rather than a reopened construction-law
claim.

## Independent reproduction

The repaired executable and its reviewed arithmetic dependency were copied
to an isolated temporary tree.  Normal and optimized runs did not modify the
primary packet.

```text
checks                         = 41/41
normal stdout SHA-256          = 9fa786d64e66b57850945f88fd97bca9fc275c3ebb7e590701900931e34524ac
-O stdout SHA-256              = 9fa786d64e66b57850945f88fd97bca9fc275c3ebb7e590701900931e34524ac
generated JSON SHA-256         = 8aca977ecc88ab54c9898bbd9c4c8ac1a5f7e142df42e072f506c4f553c714f5
primary JSON SHA-256           = 8aca977ecc88ab54c9898bbd9c4c8ac1a5f7e142df42e072f506c4f553c714f5
semantic SHA-256               = 6b80ba3acfd378602cbbcc046aff3bf4e20f071a852753822512f132c997cb08
source SHA-256                 = c0b384eba1943a76844603eadb6cfbbab42c4858a7990afed1f7c696843843f5
dependency SHA-256             = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

The packet's semantic verdict remains appropriately below the physical
action-level verdict.  It certifies the finite regional-amplitude/instrument
core, not a selected action or final click law.

## Round-2 blocker reprobes

### Protected symmetry and persistent identity

For protected record objects `R_A` and `R_B`, the repaired symmetry has

```text
protected_swap_map=((0,1),(1,0)).
```

The inverse symmetry composes to

```text
protected_double_swap_identity=True
composite_sealed_map=((0,0),(1,1)).
```

Thus the labels travel with the protected wires rather than remaining tied to
tuple positions.  A primitive identity matrix whose target changes owner A to
owner B now gives:

```text
owner_reassignment=rejected protected record identity/type mismatch.
```

The constructor also checks that every sealed source is covered exactly once,
no target record is reused, every target is sealed, the source and target
`Port` objects—including owner and `record_id`—agree, and all nonzero matrix
elements preserve the corresponding basis label.

This closes the exact round-2 contradiction in which valid structural
symmetry failed while invalid owner reassignment passed.

### Closure operations

The propagation rules are correct at their finite typed scope:

- identity maps each protected port to itself;
- composition follows the intermediate correspondence into the final target;
- tensor offsets the second factor's source and target indices; and
- symmetry constructs the explicit crossed source-to-target map.

Fresh target records do not appear in a morphism's source correspondence and
therefore cannot steal an existing record identity.  The receipt executes
protected symmetry, double symmetry and fresh-record tensor cells in addition
to the earlier composition/tensor persistence checks.

The protected portion of the matrix image is now compatible with the claimed
symmetric-monoidal structure.

### Primitive join admission

The exact reprobes give:

```text
direct_unentitled=rejected
  multi-component generator lacks a connected join entitlement

mixed_owned_ownerless=rejected
  primitive generator mixes owned and ownerless live inputs

entitled_join=accepted ('A','B').
```

The rule is applied only to primitive morphisms.  Identities, composites,
tensors and structural symmetries are marked derived and inherit the
admissibility of their primitive factors.  This is the right categorical
location for the check: tensoring two separately admitted components does not
itself make them interact, while a primitive generator consuming both must
declare the join.

The prior direct-`Mor` bypass and the owned-plus-ownerless loophole are closed.

## Join-entitlement provenance and D12 U6

**PASS only as supplied grammar.**

The entitlement is a tuple naming every distinct non-null input owner.  It is
an admission declaration, not a proof object reconstructed from a previous
connected collar.  A caller who supplies `("A","B")` is asserting that the
primitive signature licenses this join.

That is sufficient for a theorem whose antecedent is a **supplied typed
signature**.  It is not sufficient to derive D12 U6, decide how disconnected
components first acquire an interaction opportunity, or prevent a proposed
physical signature from simply postulating its desired joins.  The theorem
note says D14 does not derive how nature creates the entitlement; Paper 15
says the origin law remains open; B10 treats grammar as primitive; and B11
requires the later physical dictionary.

All-ownerless generic morphisms remain deliberately admitted.  The exact
probe confirms:

```text
all_ownerless_generic=accepted True.
```

Therefore the generic finite packet is not an implementation of D12-U6
component ownership.  The owner gate applies when the supplied grammar elects
to use owned live ports.  This is honest at `BRIDGE-CONDITIONAL` scope.

Two nonblocking clarity hardenings are recommended:

1. rename the source error/receipt phrase “connected join entitlement” to
   “declared owner-list entitlement,” because connected provenance is not
   verified; and
2. add one sentence to Paper 15 stating that the generic ownerless witness is
   not a D12-U6 locality proof.

Neither changes the theorem's conditional antecedent or exact result.

## Evaluation-schedule gauge and the global-clock boundary

**PASS at the formal theorem scope.**

The abstract, theorem note and section 4 now make the correct distinction:

```text
fixed supplied DAG
  -> every topological contraction schedule gives the same Z(N);

not proved:
  generation of the DAG,
  support/weights over alternative DAGs,
  a locally computable next-extension rule,
  removal of every global mechanism from a generative model.
```

The paper further says that a whole-history formulation avoids sequential
universe commitment only after an amplitude or measure over complete diagrams
is supplied.  Proper time and physical clock intervals remain analogies, not
D14 outputs.  This is the required resolution of the original universe-ledger
question.

### Residual wording only

Three sentences can still be quoted without their surrounding safeguards:

- section 1 asks whether a regional action/amplitude can “generate the record
  picture” and answers yes, although the record instrument is supplied;
- section 11 says “No global physical commit order is required” without
  repeating “to evaluate and accumulate records within a supplied DAG”; and
- section 14 labels the output “CLOCK-FREE PROJECTIVE NON-MARKOV RECORD
  HISTORIES.”

The safe replacements are:

```text
supplied regional amplitudes plus supplied instruments realize the finite
record picture;

no preferred total contraction order is required within a supplied DAG;

EVALUATION-SCHEDULE-INDEPENDENT PROJECTIVE NON-MARKOV RECORDED HISTORIES.
```

Because the detailed theorem and caveats already state this scope, these are
nonblocking edits.  They should nevertheless be made before the final
manifest so the headline cannot be detached from its antecedent.

## Action, instrument and birth ceiling

**PASS at `BRIDGE-CONDITIONAL` scope.**

The paper's title and principal theorem now state the actual arrow:

```text
supplied finite regional amplitudes
+ supplied boundary state
+ supplied protected record/future instruments
+ supplied grammar
-> projective recorded histories.
```

Record permanence is formulated with sectorwise-complete direct-sum CPTP
channels/isometries.  This preserves the unconditional old-record marginal;
future postselection may update inference without overwriting the record.  The
seal, pointer basis, protected algebra and live-collar continuation grammar
remain declared inputs.  The receipt does not claim autonomous environmental
selection, physical redundancy or an action-derived pointer instrument.

The live-collar tests prove exactly that the **declared continuation** consumes
the collar, that omission is ill-typed for that continuation, and that the
dead collar has zero continuation amplitude.  They do not select a universal
birth rule or derive how many collars nature emits.  The prose preserves that
distinction.

This also keeps action translation separate from action selection.  D13's
finite kernel nonuniqueness and D9's conditional partial-angle selection are
unchanged.  D14 supplies a compositional destination for a future selected
action packet; it does not select that packet.

## Sequential histories, memory and Barandes

**PASS.**

The integrated exact packet still closes the round-1 separation:

- sequential seal isometries construct the protected record strings;
- their cylinder masses match the bare class-operator probabilities at
  depths one through three;
- the record-extended functional is diagonal while the bare system functional
  is allowed to retain interference;
- complete future instruments give exact projectivity;
- the X/M/Y/Z packet produces only `000` and `101`, each with probability
  `1/2`, so the visible future depends on X beyond common Y=0; and
- the complete CPTP reset of M removes that dependence and changes the visible
  law.

The claim remains finite.  Neither Paper 15 nor the theorem says every
full-history process has bounded local memory, that the packet realizes a
Barandes indivisible process, or that it selects a unique stochastic path
measure.  A general process may require growing boundary memory.
Disintegration gives the next-record conditional only after the projective
history law and grammar are supplied.

## No-signalling and `SL(2,C)`

**PASS at the named-cell scope.**

The no-signalling statement remains one local-unitary Bell marginal plus
interchange for disjoint tensor factors.  Paper 15 explicitly denies a
class-wide theorem for arbitrary linear kernels or multi-input generators and
does not infer microcausality, finite propagation speed or continuum causal
structure.

The `SL(2,C)` result remains one exact positive-cone dual-pairing cell.  It is
not called a Lorentz theorem and is not used to claim an emergent metric,
round null cone or `3+1` phase.  This scope is stable.

## B10, B11 and the V9 holdout

**PASS.**

B10 continues to list carriers/types, grammar, local kernels, boundary state,
record instrument, pointer basis, protected future algebra, frame/pairing rule
and dimensionful units as primitive.  Join entitlements are part of the
supplied grammar.  Functoriality constrains their composition but selects none
of them.

B11 gives the missing theory-specific dictionary from physical
action/region/state through carriers, gluing measure, diamond grammar,
kernels, an autonomous record instrument, adjacency/influence observables and
proper-unit calibration.  Gauge constraints, edge data, gravity boundary
terms and sums over causal structure remain open where relevant.

Accordingly, the V9 cone/dimension holdout remains correctly refused.  D14 has
not independently selected a physical action or produced its record-web
dictionary.  Feeding a continuum cone or retuned churn into V9 would test an
ansatz, not the conditional bridge.

## Gate adjudication

| Gate | Focused round-3 result |
|---|---|
| B0 typed/protected category | **PASS for the finite admitted class.** Persistent records, overwrite rejection and primitive owner admission execute. |
| B1 category/coherence | **PASS.** Protected symmetry and fresh-record tensor now coexist with the matrix coherence cells. |
| B2 construction-order gauge | **PASS only as evaluation-schedule gauge for a supplied DAG.** Three nonblocking wording edits requested. |
| B3 coherent gluing | **PASS at exact finite scope.** |
| B4 frame/positive-cone pairing | **PASS at unitary internal-frame plus one `SL(2,C)` cell scope.** |
| B5 records and birth | **PASS for the supplied seal/protected algebra/declared continuation; autonomous instrument and entitlement origin remain primitive.** |
| B6 recorded decoherence | **PASS for sequential orthogonal protected records.** |
| B7 projective history law | **PASS for finite cylinders plus completeness induction.** |
| B8 finite visible non-Markov memory | **PASS, including integrated packet and CPTP deletion control.** |
| B9 locality/no-signalling | **PASS for the one finite tensor/unitary witness only; no D12-U6 or continuum theorem inferred.** |
| B10 action scope | **PASS at supplied-packet scope.** |
| B11 downstream handoff | **PASS; dictionary explicit and V9 holdout withheld.** |
| B12 hostile closure | **PASS for the focused ontology/locality round at `BRIDGE-CONDITIONAL` scope.** |

## Verdict

**PASS AT `BRIDGE-CONDITIONAL` SCOPE.**  The exact protected-symmetry and
ownership-admission failures from round 2 are closed, the 41-check receipt is
reproducible, and the paper maintains the correct scientific ceiling.

The accepted result is:

```text
SUPPLIED FINITE TYPED DAG
+ SUPPLIED REGIONAL MATRICES, STATE AND RECORD INSTRUMENTS
+ DECLARED PROTECTED/OWNERSHIP GRAMMAR
-> EVALUATION-SCHEDULE-INDEPENDENT PROJECTIVE RECORDED HISTORIES
   WITH ONE FINITE VISIBLE NON-MARKOV REALIZATION.

ACTION-TO-KERNEL MAP                  NOT DERIVED
AUTONOMOUS RECORD INSTRUMENT          NOT DERIVED
DIAGRAM/JOIN/BIRTH ORIGIN LAW         NOT DERIVED
D12-U6 CONNECTED-COLLAR PROVENANCE    NOT DERIVED
ACTION SELECTION                      OPEN
V9 GEOMETRY                           CORRECTLY WITHHELD
ACTION-LEVEL VERDICT                  BRIDGE-CONDITIONAL
```

The three residual clock/action phrases should be synchronized before the
final manifest, and the entitlement should not be called connected without a
provenance certificate.  Neither issue changes this narrowed pass.
