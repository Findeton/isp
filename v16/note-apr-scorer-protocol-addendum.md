# APR scorer-protocol addendum — binding interface and scope corrections

**Date:** 2026-08-18

**Status:** BINDING FORWARD CORRECTION TO
`v16/note-apr-scorer-protocol.md`. This correction freezes before
`v16/code/apr_score.py` exists and before any APR fixture truth is computed.

## 1. The contradiction

The frozen fixture correctly types the Bernoulli rows `p=1/2` and `p=1/3`
as preparation states inside the full cone of positive finitely additive
valuations:

```text
regional_question_process / valuation_family / law_role
  = preparation rows inside the full valuation cone.
```

The parent scorer protocol incorrectly says in section 3.1 that the parameter
rows are law inputs and in section 15 that `p` is law data unless selected.
Those two sentences are withdrawn. Treating a state/preparation choice as a
coupling would manufacture a false law-selection debt.

## 2. Binding type correction

The APR classical candidate has three separate inputs:

1. **law data:** the Boolean-region operations, question instrument grammar,
   decision-tree composition, record update, boundary/filling assignment,
   tensor/refinement rules, and replacement grammar;
2. **preparation data:** a positive finitely additive valuation `nu` and any
   support/record boundary condition;
3. **calibration/intervention data:** the generated question, replacement,
   reader, spectator, and coarse-graining choices used to probe the law.

`mu_p` is a one-parameter family of exact preparation controls. It is not the
full state space, a spacetime volume, a coupling constant, or part of the
law-root hash. The all-input gates are proved on an arbitrary positive
finitely additive valuation; `p=1/2` and `p=1/3` only test that proof at two
distinct preparations.

## 3. Binding scorer changes

Read the parent protocol with these replacements:

- section 3.1: “The parameter rows are law inputs” becomes “The parameter
  rows are exact preparation inputs inside the full valuation cone.”
- section 14.2: one callable law must be used across every family member; a
  registered preparation row may be held fixed across a comparison, but it
  is not included in the law identity.
- section 15: remove `valuation parameter` from the law-root hash and record
  it under a separate preparation-root hash.
- section 15: “`p` is law data unless independently selected” becomes “`p`
  labels a preparation family; no APR law-selection statement may count its
  variation as a law modulus.”
- P4 remains mandatory, retyped as a preparation-sensitivity mutant: a scorer
  that silently substitutes the `p=1/2` preparation for the `p=1/3`
  preparation must be detected by regenerated probabilities while the
  law-root hash remains unchanged.
- E-37 resource parity records preparation access separately from law
  parameters. A blind adversary and the regional rule receive the same
  preparation; neither may fit `p` per member.

### 3.1 Semantic branch bits, not identifier order

The neutral fixture identifiers `pt_000` and `pt_001` are not record-bit
values. The scorer binds record bits from the branch operation itself:

```text
Q_C^1(nu)(A)=nu(A meet C)             writes bit 1
Q_C^0(nu)(A)=nu(A meet complement(C)) writes bit 0.
```

The literal `0`/`1` record-tree boundaries use that semantic convention. The
scorer may not infer a bit from list position, an identifier suffix, or
insertion order. It must refuse branch-labelled record, cospan, and recovery
claims if the two branch formulas do not supply exactly one `Q_C^0` and one
`Q_C^1`, or if a later primitive supplies a contradictory port-to-bit map.

### 3.2 Same-law delayed readers versus recovery controls

The regional-question process's `reader_schedules` explicitly compose
`qo_005` identity delays with `qo_006` and are the only frozen rows that may
support a same-law delayed-reader claim. By contrast,
`RECORD_RECOVERY_PRIMITIVES.reader_delays` contains only a delay count plus
writer/reader IDs; it names no continuation generator and has no provenance
edge to `qo_005`.

Those latter rows are therefore finite identity-delay controls only. They may
test the algebra of a copied or reset flag after inserting an identity by
convention, but they cannot be welded into the regional process or used to
claim generated delayed recovery. The receipt must report the control and
same-law coordinates separately.

### 3.3 Preparation scope of the finite-probe collision

The registered base-probe collision between `[00]` and `[01]` is a control at
the dyadic preparation `p=1/2`. At `p=1/3`, their unit and `[0]` profile
coordinates already differ because their preparation masses are `1/9` and
`2/9`. M04 must therefore report the collision and appended-probe separation
per preparation; it may not assert one universal collision across both rows.

The general completeness question remains preparation-independent only when
posed on the full valuation cone and all generated contexts. A finite scalar
profile at one preparation cannot establish or refute that full-cone theorem.

### 3.4 E-37 resource scope actually frozen

The regional family rows freeze state dimension, history depth, calibration
slots, and parameter slots. They do not freeze a per-adversary number field,
precision budget, or registered easier-row benchmark. Exact rational
arithmetic is a global scorer discipline shared by both sides, not a measured
resource coordinate.

The scorer may therefore prove the analytic factorization statement for
rules with the frozen blind inputs and declared interfaces: byte-identical
blind projections force equal outputs for any rule factoring through that
projection. It may not report an exhaustive expressivity or resource-parity
exclusion involving an unregistered number field, precision, or easier-row
success. A trivial constant rule may establish nonemptiness of a blind class,
but not competence on an easier physical task that the fixture does not
contain.

The fixture also freezes no regional `Tau`/instrument assignment on the E-37
members. `ec_001`/`ec_002` are expressly external comparator controls, not
the regional law. Thus input/resource matching and the blind factorization
theorem may pass while physical regional prediction and physical-versus-blind
exclusion remain `NOT-CONSTRUCTED`. The scorer must not manufacture a target
screen from relation mode, member IDs, or the comparator namespace.

### 3.5 Replacement closure, fixed algebras, and regional support

The frozen replacement rows support three distinct computations. They may not
be silently identified:

1. the **literally listed** child swaps for `A=[00]` have three exterior leaf
   orbits at the frozen depth-three presentation and therefore two excess
   exterior-scalar directions beyond one common exterior scalar;
2. the **generic child-swap grammar** recursively closes inside the two
   maximal exterior cylinders and therefore has two exterior orbits and one
   excess direction;
3. the **intrinsic relative-complement grammar** declares all-partition
   transitivity and conjugation closure and is intended to leave one exterior
   orbit and no excess direction.

The scorer must publish all three readings separately. Finite registered rows
may verify only their finite fixed spaces. The all-partition intrinsic result
is an analytic theorem conditional on full-cone separation, composition
closure, exterior support, transitivity on every finite exterior partition,
and vertical conjugation closure; two finite target rows do not establish
those hypotheses empirically.

The raw unital fixed-effect algebra is not the physical atomless support
object: it always contains the common exterior scalar as an atom, and raw
fixed-algebra intersections need not preserve regional meets. The support
comparison must instead use the relative variation ideal/effect space
supported in `A`, equivalently the fixed space modulo the common exterior
scalar. Atomlessness is tested on the resulting regional support lattice,
not on the raw fixed algebra.

Any success here is `REGIONAL-SUPPORT` only. Reversible exterior replacements
do not derive causal precedence, irreversible continuation, or gravity.

### 3.6 Generated-question theorem and support initialization

The complete-question separation theorem is licensed only under all of these
hypotheses: a strictly positive reference valuation, a faithful supported
preparation for every nonzero region, a target-independent compiler for every
region question, retained zero ports, calibrated recoverable records, and
presentation naturality. Under those hypotheses complete contextual
equivalence is literal regional equality and hence a Boolean congruence whose
quotient remains atomless.

The frozen finite question catalogue alone does not prove that theorem. If
the generic compiler is only declared rather than constructed through lawful
fillings and effects, report `COMPLETE-PROBES-POSTULATED`, not generated
completeness. The `[00]`/`[01]` finite collision remains a required scope
control.

The question instrument is defined symbolically for an arbitrary nonzero
support `S`:

```text
leaf(b_1...b_n) = S meet C_1^(b_1) meet ... meet C_n^(b_n).
```

The scorer must prove branch partition, telescoping, and total mass for
arbitrary `S`. Numerical `p=1/2` and `p=1/3` branch-weight controls use the
unit support `S=1`; they may not be presented as the generic theorem or used
to infer an unrecorded support from identifier order.

### 3.7 Record forests are not yet a regional process functor

The frozen record-tree cospans are finite instrument presentations and three
positive factorization controls. They do not freeze the total forest functor
required for a horizontal regional process. In particular, the fixture lacks
arbitrary prefix-free adaptive frontiers such as `{0,10,11}`, boundary
carriers carrying the full `(question, bit)` record, a constructed tensor
factory, mixed question/replacement forests, vertical naturality for the
total construction, and a regional-overlap gluing rule.

Therefore the scorer may verify the listed tree grafting identities and may
state the general forest theorem conditionally if it constructs every premise
from the frozen public interfaces. It may not infer a cospan/process functor
from matching node/edge unions or from the provenance declaration. Absent a
total construction, the process coordinate remains an instrument
presentation and the strict outcome is controlled by
`APR-BLOCKED-AT-BOUNDARY-GLUING`.

The frozen spectator row supplies no tensor boundary/map factory. P8 can kill
a sequential impostor or report `TENSOR-UNCONSTRUCTED`; it cannot assert
tensor preservation against a nonexistent positive baseline.

Likewise, the passive pair `vm_002`/`vm_003` is not attached to a nonidentity
horizontal filling. It supplies no nontrivial naturality square or future
profile, so vertical naturality is unconstructed/vacuous rather than a
positive result. The structural writer cospan `hf_008` has no process
assignment either: M08 may reject a passive/ontic type swap structurally, but
not by citing generated record dynamics.

The AB/BC rows deliberately admit two global completions with identical
local marginals. No record-tree result selects between them. A Markov,
conditional-independence, higher-joint-kernel, or other regional gluing rule
remains law data unless independently derived.

### 3.8 Mutant and family-generation availability

The original M06 arena already has zero continuation-stable null after the
registered generator closure. M06 must therefore use a separate paired
four-coordinate control: extend the original three-coordinate action by a
fourth fixed basis direction, so the baseline stable null is its span, then
add a continuation that sends that direction to the observed first
coordinate while acting identically on the first three. The added
continuation must move the final stable-null dimension from one to zero. A
mere change in a finite rank history with the same final null is not a valid
M06 death.

The frozen fixture exposes registered family members and a uniform-rule
interface, but no public family-generation grammar. M29 must therefore report
`NO-FROZEN-FAMILY-GENERATOR` and restrict its held-out claim to the registered
members. The scorer may not call a private helper, infer a generator from
identifier patterns, or synthesize a new member and call it frozen.

### 3.9 Causal and contact controls are not process schedules

The common-source, direct-arrow, cycle, and contact-only arenas freeze arrows,
interventions, and readers but no operation schedule or provenance link to
the regional question process. They are classification controls only. The
scorer may reconstruct the stated static/intervention distinctions, but may
not claim law-generated causal influence, stable causal order, or a joint
regional process without an independently typed schedule built from public
law data.

Likewise, the intrinsic replacements are reversible controls. Their cycles
must never be topologically sorted into causal precedence. Causal order
remains priced or blocked until a stable calibrated influence relation is
generated by one horizontal law.

## 4. Law selection after correction

`law_selection` concerns only genuinely nomological freedom: the event and
question menu, record grammar, boundary/gluing assignment, replacement
semigroup, contact/influence rule, and any process weights not already part of
the prepared state. The scorer must report preparation sensitivity
separately.

This correction does not select the remaining law family. It only prevents a
state choice from being counted as a law choice.

## 5. Ontology consequence

The valuation is part of the process-state representation. APR does not
decide whether that state is ontic, epistemic, or a shadow of a deeper
history law. The physical ontology gate still concerns whether one law makes
regional distinctions operationally faithful and dynamically supported.
Neither a Bernoulli bias nor its fitted value is itself a region, geometry,
matter species, or coupling.

All parent-protocol requirements inconsistent with these interface and scope
corrections are superseded. No registered APR outcome word is changed.
