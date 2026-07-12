# D15 hostile ontology/physics review — round 1

**Date:** 2026-07-11  
**Review verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Exact finite witness:** **REPRODUCIBLE AT A MUCH NARROWER SCOPE**

## Executive finding

D15 has the right high-level answer but has not yet earned its provisional
positive verdict under its own frozen protocol.

The defensible physical answer is:

```text
Observed 3+1 Lorentzian fields and symmetries
  + locality/unitarity/gauge consistency
  + a low-energy derivative expansion
  -> the Einstein–Hilbert + Standard Model EFT operator normal form,
     with measured/free coefficients and an infinite symmetry-allowed tower.

This does not derive 3+1, Lorentzian signature, G, the state, records,
the UV completion, or a V9 record web.
```

The working note usually says exactly this.  Its scale, cone and UV
disclaimers are strong.  It correctly treats `G` as measured, explains that
metres/seconds calibrate rather than round a cone, says EFT4 assumes its metric
cone and dimension, grades the action-to-record map conditional, and refuses
an untouched V9 holdout.

The exact receipt is also mathematically sound as a qubit exercise.  It builds
Hadamard and CNOT matrices from declared finite phase/constraint weights,
checks gluing and interference, couples a qubit to a fresh `|0>` environment,
obtains exact reduced Z-basis decoherence, and preserves the resulting record
marginal under a later system-only unitary.

What it does **not** do is what several labels imply:

1. It does not independently represent an action and derive a kernel from it;
   the “action kernels” are the matrices being defined, with a supplied
   normalization/measure factor.
2. It hash-locks D14 but never constructs a D14 object, morphism, protected
   record, owner, collar capability or join entitlement.
3. Its record basis, system/environment split, environment state, CNOT
   interaction, trace/coarse graining and live collar are supplied.  It derives
   reduced decoherence conditional on that packet, not an autonomous pointer
   instrument from the action alone.
4. It is nongravitational and not generally covariant.  The continuum EFT4
   path integral remains a formal expression rather than the promised
   regulated EFT4-to-D14 dictionary.
5. The draft has no quantitative validity domain/truncation error, coefficient
   fit ledger, complete candidate matrix or untouched prediction protocol.

Thus the exact result is a **regulated qubit kernel/environment-record
compatibility witness**.  It is not yet an action selector, a generally
covariant regional packet, an autonomous record derivation or a completed
low-energy empirical adjudication.

## Exact reproduction

The D15 source and its frozen D13/D14 dependencies were copied to an isolated
temporary tree.  Normal and optimized Python produced byte-identical stdout
and byte-identical regenerated packets.  The regenerated packet matches the
primary artifact.

```text
checks                         = 22/22
normal stdout SHA-256          = ba3a9a9f29a4722bb73f7e94f181ce1b9aefa38b605406e0bccca50173786591
-O stdout SHA-256              = ba3a9a9f29a4722bb73f7e94f181ce1b9aefa38b605406e0bccca50173786591
generated JSON SHA-256         = b10bd2ce0772f658438aad91b714cf1804b0142800f96a8eedd76872b33d16f2
primary JSON SHA-256           = b10bd2ce0772f658438aad91b714cf1804b0142800f96a8eedd76872b33d16f2
semantic SHA-256               = f3b02e21a208a90d4c77215cae744bae249e903d11f87e197c23972635a104e6
source SHA-256                 = 9d9fac31730d1c02ed7cc5694d28b50f8b9277b6da8bea1ce199a2f72b81f47c
D13 dependency SHA-256         = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
D14 dependency SHA-256         = e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

The packet ceiling is honest:

```text
finite Z2/qubit regional action; nongravitational;
does not select nature's action or establish generally covariant gravity.
```

The hostile findings concern labels above that ceiling and missing frozen
gates, not a failure of the exact arithmetic.

## Opening ledger

| ID | Severity | Opening | Required repair |
|---|---:|---|---|
| P1 | **MAJOR** | “Action-derived kernel” mostly relabels a directly declared matrix.  No separate action/measure/regulator object is evaluated. | Represent finite configurations, action, measure and boundary terms separately; derive the kernel by an explicit sum and audit action equivalences. |
| P2 | **MAJOR** | D14 is hash-checked but not used.  No typed D14 dictionary is constructed. | Instantiate D14 `Port/Obj/Mor/Signature`, protected record IDs, owners, collar capability and join entitlement; compose the regulated kernel through that admitted packet. |
| P3 | **MAJOR** | The record instrument depends on supplied environment state, split, CNOT, pointer basis, trace/coarse graining and collar. | Grade S5 conditional; either derive those data from one action/state with stability/redundancy criteria or call them supplied apparatus/coarse-graining inputs. |
| P4 | **MAJOR** | The exact witness is nongravitational, while the EFT4 regional integral remains formal and unregulated. | Add one actual regulated EFT4/gauge or gravity regional example with boundary data, measure, constraints/gauge fixing and D14 map, or withdraw S4 closure for EFT4. |
| P5 | **MAJOR** | S6 is absent: one tensor commutator is not a diagram law, owned join rule or no-global-clock theorem. | State whether complete diagrams are summed or locally generated; use D14 admitted ownership and retain evaluation-schedule gauge only for supplied diagrams. |
| P6 | **MAJOR** | No quantitative EFT domain, truncation order/error or regulator-removal statement is frozen. | Declare scale hierarchy, renormalization scheme/scale, operator truncation and remainder/error target. |
| P7 | **MAJOR** | “Evidence selects” is asserted without a dataset/fit/model-selection ledger. | Separate observed inputs, parameter fits, consistency deductions and model comparisons; record data provenance and uncertainties. |
| P8 | **MODERATE** | UV audit lists three aspirational routes but omits PRIM and does not exhibit two complete UV-compatible packets. | Complete the S0–S10 field-by-field matrix for EFT4, BDQ, ASQ, SFQ and PRIM; do not grade incomplete proposals as proved survivors. |
| P9 | **MODERATE** | The SM and higher-operator discussion references classifications but does not execute S2/S3's requested enumeration and coefficient ledger. | Freeze operator-basis assumptions, redundancies, anomaly conditions and parameter classes at a declared scale. |
| P10 | **PASS** | 3+1, Lorentzian signature, cone shape and `G` are treated as inputs/measured data, not SHARD derivations. | Preserve this language. |
| P11 | **PASS** | No V9 holdout is opened and EFT4-to-V9 is called recovery/calibration, not emergence. | Preserve the refusal. |
| P12 | **FORMAL BLOCKER** | S0, S2–S8, S10 and S11 are not all closed, so the positive provisional verdict outruns the frozen decision rule. | Retain `INCOMPLETE-INVESTIGATION` until repairs and hostile closure; keep narrower findings as interim results. |

## P1 — an action is not merely a renamed kernel

The executable defines

```math
K(b,a)=2^{-1/2}(-1)^{ab}
```

and names the result a local phase action yielding the Hadamard kernel.  The
phase can indeed be written as `exp(i pi a b)`.  But the magnitude
`2^{-1/2}` is a separately supplied vertex/boundary measure factor, not
produced by that phase action.  `cnot_action_kernel()` similarly writes the
CNOT permutation directly as a constraint delta.

There is no data structure for:

```text
configuration space;
local action functional;
boundary term;
measure/reference weight;
regulator;
gauge quotient;
sum over internal configurations.
```

The first actual sum occurs only when already constructed matrices are glued.
That proves kernel composition, not the upstream action-to-kernel map.

Action representation is also nonunique even at this toy level.  Replacing
`S(a,b)` by `S(a,b)+2 pi n(a,b)` gives the same kernel.  Boundary phases can be
moved between regional kernels and boundary states/frames.  Measure factors
can be redistributed across vertices and glued edges while leaving a closed
amplitude unchanged.  Therefore “the action” requires an equivalence ledger,
not merely a matrix formula.

The final phase-dressed alternative proves that more than one unitary kernel
fits the structural cells.  It does not prove that two independently defined
regulated actions were compared.

### Required exact repair

Build a small but explicit finite action model:

```text
boundary labels a,b;
internal labels x;
S_M(a,x,b);
mu_M(a,x,b);
K_M(b,a)=sum_x mu_M exp(i S_M);
```

Then verify boundary gluing, measure-once accounting and at least one
action-equivalence control.  Label the current cell `DECLARED FINITE PHASE
WEIGHT -> KERNEL`, not `ACTION-DERIVED`, until that layer exists.

## P2 — the executable does not enter D14

The D15 source reads and verifies the D14 source hash.  It does not import or
instantiate D14's category objects.  No use is made of:

```text
Port, Obj, Mor, Signature;
sealed_map and persistent record identity;
primitive owner admission;
join entitlements;
live-collar continuation capability;
protected CPTP future algebra.
```

The “seal” is an untyped `8 x 2` matrix.  Record permanence is checked by a
hand-written later system-only action.  The live collar is basis index `1`.
There is no D14 constructor proving that overwrite, owner mixing or invalid
continuation is rejected.

Hash-locking a dependency proves byte provenance, not semantic integration.
The JSON phrase

```text
local action weights -> kernels -> environment seal -> records
```

is valid as an informal finite vector-space chain.  It is not yet the frozen
S4 map to D14 carriers, protected records and collars.

### Required repair

Construct the same witness using D14's admitted types.  Give system,
environment/record and collar ports stable IDs/owners; declare the primitive
kernels through the signature; supply or derive the join entitlement; seal
through an admitted isometry; and execute repeat-read and protected future
composition.  The packet must state which fields remain supplied.

## P3 — decoherence is derived conditional on a supplied apparatus packet

The finite calculation itself is correct:

```text
prepare |+>_S |0>_E;
apply CNOT S -> E;
trace E;
obtain I/2 on S in the Z-record experiment.
```

This demonstrates exact entanglement-induced reduced decoherence.  It also
produces orthogonal environment labels that can be read as a record.

However, D15 supplies all choices that make that statement true:

- the system/environment tensor split;
- the fresh environment state `|0>`;
- the CNOT interaction and its computational control basis;
- which environment basis is read;
- the partial trace/coarse graining;
- the declaration that the register is protected later; and
- the live collar value.

A rotated system basis with a correspondingly rotated copying interaction
would define another exact pointer instrument.  The bare qubit action cells do
not select between them.  Nor does one environment qubit demonstrate
redundancy, macroscopic accessibility, dynamical stability or a tolerance
scale.

The working note is substantially more honest than the executable labels.  It
says the split, initial state, coarse graining and stability tolerance must be
specified and denies a unique fundamental seal from the bare action.  That
means S5 is `ACTION-BRIDGE-CONDITIONAL`, not “autonomous records passed.”

Rename receipt labels from `action-derived environment/record` to `supplied
CNOT environment dilation`.  A stronger claim requires a Hamiltonian/state
whose dynamics selects a robust pointer algebra and demonstrates repeatable,
redundant records without inserting that basis as the readout definition.

## P4/P5 — gravity, covariance, ownership and clock scope

The exact packet declares itself nongravitational.  It contains no spacetime,
metric, diffeomorphism quotient, gauge constraint, boundary charge, edge mode,
corner term or gravitational state.  Its disjoint-cell commutator is tensor
interchange, not general covariance.

The formal continuum expression

```math
K_M=\int Dg Dphi Delta_gf exp(i S_eff/hbar)
```

lists several necessary ingredients but does not define a regulator,
finite-dimensional boundary carrier, gauge-fixed measure, contour, anomaly
control or gluing theorem.  It is the architecture S4 says is insufficient if
left as an `exp(iS)` slogan.

Likewise, the exact disjoint operation check does not answer S6.  There are no
owned boundary objects or join entitlements, no amplitude/measure over
alternative complete diagrams and no local extension-support law.  D14's
evaluation-schedule theorem may be inherited only after an actual supplied
D14 diagram is constructed.  It says nothing about how that diagram is born.

Required repair: grade the qubit example as nongravitational S4 rehearsal;
either build a regulated gauge/gravity regional cell or leave the EFT4-to-D14
dictionary open.  Add an explicit S6 section stating whether the candidate
sums complete diagrams or generates local extensions and separating that law
from contraction-order gauge.

## P6/P7/P9 — the low-energy rulebook is not yet an empirical receipt

The displayed EFT action is a correct schematic normal form, but “ordinary
energies” is not a frozen domain.  The draft does not specify:

```text
renormalization scheme and scale;
energy hierarchy/cutoff;
operator dimension or derivative truncation;
power-counting assumptions;
truncation error/remainder target;
which coefficients/data release are used;
fit likelihood, uncertainties and correlations;
which observations select the operator content versus fit parameters.
```

The ellipsis is physically necessary, but an infinite symmetry-allowed tower
is not a unique numerical action.  Operator bases are related by integrations
by parts, equations of motion and field redefinitions.  The cited Warsaw-basis
paper classifies dimension-six operators under stated assumptions, including
a baryon-number distinction; it is not a complete numerical coefficient fit
([Grzadkowski et al.](https://arxiv.org/abs/1008.4884)).

Similarly, Deser's result supports consistency completion once massless
spin-two gauge structure is assumed ([Deser](https://arxiv.org/abs/gr-qc/0411023)),
and Donoghue supports treating GR as a good low-energy quantum EFT
([Donoghue](https://arxiv.org/abs/gr-qc/9512024)).  Neither selects the observed
field content, dimension, state, coefficients or UV completion.

The note states these limitations correctly.  What is missing is the frozen
S0/S2/S3/S8 ledger that turns the literature synthesis into the protocol's
`LOW-ENERGY-EFFECTIVE-RULEBOOK-IDENTIFIED` grade.  Until then, the result is an
accurate **candidate normal-form statement**, not a completed empirical
selection receipt.

## P8 — UV candidate fairness

The draft is commendably cautious but incomplete.

- The Benincasa–Dowker result defines an approximately local causal-set action
  when the causal set is already well approximated by four-dimensional
  continuum spacetime; it is not a quantum measure, matter/state/record packet
  or a derivation of dimension ([Benincasa–Dowker](https://arxiv.org/abs/1001.2725)).
- The cited spin-foam precursor constructs a four-dimensional **Euclidean**
  vertex with boundary states and weak simplicity constraints; it is not the
  frozen SFQ packet with Lorentzian continuum/refinement, matter, state and
  records ([Engle–Pereira–Rovelli](https://arxiv.org/abs/0708.1236)).
- The 2026 asymptotic-safety review reports strong evidence and current
  progress, while still describing an active route toward realistic
  Lorentzian quantum gravity ([Eichhorn](https://arxiv.org/abs/2606.21522)).
  D15 is fair not to call it a finished selected packet.
- Rideout–Sorkin derives a **family** of classical sequential growth laws from
  causality and discrete covariance, not one quantum action/record packet
  ([Rideout–Sorkin](https://arxiv.org/abs/gr-qc/9904062)).  The draft does not
  adjudicate this anchor.
- The frozen PRIM class is omitted from the survivor discussion.

Because none of BDQ/ASQ/SFQ is completed under D15's target packet, they cannot
yet serve as the two complete survivors required for
`FUNDAMENTAL-NONSELECTION-PROVED`.  It is legitimate to say no UV completion
is currently selected; it is not yet a D15 theorem that two complete packets
survive every frozen established constraint.

Add a field-by-field candidate matrix and classify each entry as implemented,
literature-supported, conjectural or missing.  Keep “candidate route” distinct
from “survivor.”

## P10/P11 — dimension, cone, units and `G`

**PASS.**

This is the draft's strongest ontology section.

- `3+1` and Lorentzian signature are inputs to EFT4, not predictions.
- The local Lorentz-round cone follows from the assumed metric and
  two-derivative principal symbol; it is not emergent record-web roundness.
- GW170817/GRB 170817A constrains gravity/light speed mismatch at the quoted
  order ([LIGO/Virgo/Fermi/INTEGRAL](https://arxiv.org/abs/1710.05834)); it does
  not derive the metric substrate.
- `G` is a measured gravitational coefficient, not produced by dimensionless
  record evidence.
- `G`, `hbar` and `c` define a Planck scale only after those empirical/unit
  bridges are supplied.
- Recovering metres and seconds calibrates coordinates; it does not make a
  polyhedral cone rounder.
- An EFT4-to-V9 exercise would be recovery/calibration because the continuum
  cone and dimension are already in the source.

No V9 cone/dimension holdout is licensed.  Preserve this section nearly
unchanged.

## Provisional-verdict adjudication

The draft itself calls the verdict provisional and says hostile review and UV
work remain.  Under the frozen protocol, the current formal status must be:

```text
INCOMPLETE-INVESTIGATION.
```

`LOW-ENERGY-EFFECTIVE-RULEBOOK-IDENTIFIED` is not yet frozen because the
quantitative S0 domain/truncation, S2/S3 enumeration, S8 empirical ledger and
S11 closure are missing.  `ACTION-BRIDGE-CONDITIONAL` is the right current
physical grade, but even its exact S4 implementation reaches only an untyped
qubit rehearsal rather than the repaired D14 category.

The safe interim findings are:

```text
EINSTEIN–HILBERT + SM EFT OPERATOR NORMAL FORM
  CONDITIONALLY IDENTIFIED FROM OBSERVED 3+1 CONTENT AND SYMMETRIES;

REGULATED QUBIT PHASE/CONSTRAINT KERNEL WITNESS
  PASSED 22/22;

SUPPLIED CNOT ENVIRONMENT DILATION
  PRODUCES EXACT Z-BASIS REDUCED DECOHERENCE;

ACTION/ENVIRONMENT -> AUTONOMOUS D14 RECORD PACKET
  STILL CONDITIONAL/UNIMPLEMENTED;

FUNDAMENTAL ACTION, UV COMPLETION, 3+1, G AND V9 EMERGENCE
  NOT SELECTED.
```

## Gate adjudication

| Gate | Round-1 result |
|---|---|
| S0 effective/fundamental scope | **PARTIAL.** Conceptual scope honest; quantitative domain, regulator and truncation absent. |
| S1 gravity normal form | **PARTIAL.** Leading-form literature argument sound under assumptions; no regulated gravity packet. |
| S2 matter normal form | **PARTIAL.** Conditional SM form stated; requested enumeration/basis ledger absent. |
| S3 couplings/scales | **PARTIAL.** Classification direction correct; full coefficient ledger absent. |
| S4 action-to-D14 dictionary | **FAIL/PARTIAL.** Exact qubit witness does not instantiate D14 and EFT4 integral remains formal. |
| S5 autonomous records | **OPEN/CONDITIONAL.** Environment, state, split, pointer basis and coarse graining supplied. |
| S6 locality/join/global clock | **OPEN.** No owned grammar/diagram law; one tensor commutator only. |
| S7 3+1/cones/influence | **PASS as an assumption/recovery ledger; no emergence claimed.** |
| S8 empirical selection | **OPEN.** No frozen dataset/fit/model-selection receipt. |
| S9 untouched prediction | **CORRECTLY WITHHELD.** |
| S10 UV survivor audit | **OPEN.** Candidate sketches incomplete; PRIM omitted; no two complete packets. |
| S11 hostile closure | **OPEN.** This review finds major repairs. |

## Required repair order

1. Narrow and rename the exact receipt to a declared finite
   phase/constraint-weight-to-kernel/environment witness.
2. Separate action, measure, boundary terms and regulator, then derive the
   finite kernel by an explicit configuration sum.
3. Instantiate the repaired D14 category and protected/owned record packet.
4. Grade record formation conditional unless pointer/stability/redundancy data
   are derived from the same action/state.
5. Add a genuine regulated EFT/gauge or gravity regional example, or explicitly
   leave the EFT4 dictionary open.
6. Freeze the EFT domain, scheme, truncation, power counting and error target.
7. Produce the full coefficient/data provenance ledger and candidate matrix,
   including PRIM.
8. Retain the V9 holdout refusal and run new hostile rounds before a positive
   protocol verdict.

## Verdict

**MAJOR REVISION — `INCOMPLETE-INVESTIGATION`.**  D15's conceptual conclusion
is likely the correct one: current evidence supports a low-energy
Einstein–Standard-Model EFT rulebook while leaving records and UV completion
nonunique.  The present artifacts do not yet prove that conclusion at the
frozen protocol's empirical and dictionary standard.

The exact 22-check witness should survive as a narrow regulated qubit
construction.  It must not be allowed to stand in for a generally covariant
EFT4 action, an autonomous record instrument, a D14 typed dictionary or an
empirical selector of nature's action.
