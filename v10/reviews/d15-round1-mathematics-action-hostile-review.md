# D15 hostile round-1 mathematics/action review

**Date:** 2026-07-11  
**Reviewer:** independent mathematics/action/EFT referee  
**Verdict:** **MAJOR REVISION**  
**Current honest protocol status:** `INCOMPLETE-INVESTIGATION`

## Decision first

The 22 exact finite calculations reproduce and are mostly correct as matrix
identities.  They establish a useful supplied qubit-kernel packet: normalized
Hadamard and CNOT matrices glue coherently, prepare an exact Bell state, yield
one exact reduced-state decoherence cell, and support a reversible finite
memory example.  The phase-modified alternative also correctly proves that
this construction is not an action selector.

The receipt does **not yet close S4**, even at its finite nongravitational
scope.  Its Hadamard normalization is a supplied local measure, not a result
of the displayed phase action.  Its CNOT zeros are supplied hard support
constraints, not values of a finite real phase `exp(iS)`.  Most importantly,
the executable never imports or constructs a D14 `Port`, `Obj` or `Mor`: it
only hashes the D14 source and operates on parallel untyped arrays.  Thus the
bit called a sealed record is not protected by D14 admission.  I applied a
perfectly unitary raw record flip after the declared seal and changed an old
record from zero to one without any rejection.

The EFT conclusion is directionally right but not yet a maximal normal-form
theorem.  The displayed gravity-plus-Standard-Model action omits the
symmetry-allowed dimension-four nonminimal term `H^dagger H R`, does not state
an operator-basis equivalence relation or power-counting truncation, and does
not enumerate the matter operators promised by S2.  “Ordinary energies” is
not the regulator/domain/truncation specification frozen in S0.  The
parameter table is a useful summary, but it does not yet classify independent
renormalized coefficients basis-by-basis and scale-by-scale as S3 requires.

These are repairable scope and construction defects, not a refutation of the
finite matrix results or the central conclusion that present evidence selects
an effective rulebook rather than a unique microscopic record law.

## Frozen artifacts and reproduction

Reviewed bytes:

```text
f822de9594ad37204d47f2e9fc58e9cc52871c1e39345fcb823cdb7f5925aaa5  note-d15-empirical-action-selector-protocol.md
62c0a2450edbac5583daebe7164b0718b5d4ba51baa5665909dece81089d5d64  note-d15-maximal-low-energy-action.md
9d9fac31730d1c02ed7cc5694d28b50f8b9277b6da8bea1ce199a2f72b81f47c  code/d15_regulated_action_dictionary_exact.py
b10bd2ce0772f658438aad91b714cf1804b0142800f96a8eedd76872b33d16f2  data/d15-regulated-action-dictionary-exact.json
959455d5e0a641fd16a745a8cd8964c33ebd11fd095369b360c085b292da6a89  data/d14-final-receipt.md
```

Independent normal and optimized execution gave:

```text
checks                         = 22/22
normal stdout SHA-256          = ba3a9a9f29a4722bb73f7e94f181ce1b9aefa38b605406e0bccca50173786591
optimized stdout SHA-256       = ba3a9a9f29a4722bb73f7e94f181ce1b9aefa38b605406e0bccca50173786591
semantic SHA-256               = f3b02e21a208a90d4c77215cae744bae249e903d11f87e197c23972635a104e6
source SHA-256                 = 9d9fac31730d1c02ed7cc5694d28b50f8b9277b6da8bea1ce199a2f72b81f47c
generated packet SHA-256       = b10bd2ce0772f658438aad91b714cf1804b0142800f96a8eedd76872b33d16f2
D13 arithmetic dependency      = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
D14 bridge dependency          = e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
```

Normal and optimized stdout are byte-identical.  No Python `assert` supplies
a gate.  The packet correctly limits its scope to a finite nongravitational
qubit example and denies selection of nature's action.

## Opening ledger

```text
M1  MAJOR  K_H contains a supplied 2^(-1/2) measure not derived from S_H.
M2  MAJOR  CNOT is imposed as delta-function support, not derived from the
           stated phase-action construction.
M3  MAJOR  D14 is hash-checked but never used; S4 bridge entry is unexecuted.
M4  MAJOR  the raw "sealed" bit has no protected admission and is overwritable.
M5  MAJOR  the claimed maximal EFT normal form omits allowed curved-space
           terms and has no declared basis/truncation/domain.
M6  MODERATE S2 enumeration and the S3 independent-coefficient ledger are
           incomplete.
M7  MODERATE the memory matrix is imported, not reconstructed from D15's
           local action cells, and no non-Markov conditional is evaluated.
N1  MINOR  "Bell record" means a Bell-state basis correlation here, not a
           recorded CHSH/Bell-nonlocality experiment.
N2  MINOR  gauge quotient, fixing and edge-mode entries are unstated rather
           than explicitly trivial for the nongauge qubit toy.
```

## 1. Does the Hadamard kernel follow from the action?

The receipt declares

```math
K_H(b,a)=2^{-1/2}\exp(i\pi ab).
```

This is a valid finite regional **weight**, but it consists of two logically
separate inputs:

```math
S_H(b,a)=\pi ab \pmod {2\pi},
\qquad
\mu_H(b,a)=2^{-1/2},
\qquad
K_H=\mu_H e^{iS_H}.
```

The action supplies only the signs.  Without the supplied vertex measure,

```math
P_{ba}=e^{i\pi ab}
=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P^\dagger P=2I,
```

so the phase action alone is not unitary.  The exact hostile probe reproduced
`P^dagger P=2I` and `K_H^dagger K_H=I`.

There is nothing illegitimate about choosing `mu_H=2^(-1/2)`.  A regulated
path integral requires a measure.  The defect is the phrase “the local phase
action exactly yields” the kernel.  The function directly returns the
already-normalized matrix and compares it with a second literal copy; it does
not independently construct an action, a measure and their product.

The gluing convention also needs to be part of the frozen packet.  The
current calculation uses one factor `2^(-1/2)` per `H` vertex and unnormalized
counting measure `sum_{x in Z2}` on the glued boundary.  With exactly that
choice, two cells give

```math
\sum_x K_H(c,x)K_H(x,a)=\delta_{ca}.
```

Changing either measure changes the result.  Therefore the positive theorem
is an action-**plus-measure** dictionary, as S4 itself correctly anticipated.

### Required repair M1

Represent and freeze `S_H`, `mu_H` and the internal-boundary measure as
separate data.  Derive every entry of `K_H` from them and then run the current
unitarity/gluing checks.  Say explicitly whether unitarity fixes the measure
inside a chosen uniform-measure ansatz or whether it is simply supplied.

## 2. Is CNOT a constraint action?

The executable returns

```math
K_C(b_c,b_t;a_c,a_t)
=\delta_{b_c,a_c}\delta_{b_t,a_t\oplus a_c}.
```

This is a correct reversible permutation kernel.  It is not the exponential
of an ordinary finite real action on just the four displayed boundary bits:
`exp(iS)` has unit modulus and cannot itself produce twelve exact zeros.
Those zeros are a hard support constraint or a singular measure.

Again, a constrained regional model is legitimate, but its ingredients must
be named.  One clean finite action derivation introduces two auxiliary
`Z2` Lagrange multipliers:

```math
S_C=\pi\{\lambda_c(b_c+a_c)
          +\lambda_t(b_t+a_t+a_c)\}\pmod {2\pi},
```

with all sums in `Z2`.  Then

```math
K_C={1\over4}\sum_{\lambda_c,\lambda_t\in Z2}e^{iS_C}
=\delta_{b_c,a_c}\delta_{b_t,a_t\oplus a_c}.
```

I enumerated this auxiliary-field sum exactly and recovered the executable's
CNOT matrix.  This supplies a direct repair that keeps the intended finite
action language honest.

### Required repair M2

Either:

1. implement the multiplier action and measure above; or
2. declare CNOT as a primitive support-constrained kernel rather than an
   action-derived phase.

The first option would give D15 a genuine nontrivial action-to-support
derivation.  In either case, distinguish action phase, measure and admissible
support in the semantic packet.

## 3. S4 is not executed through D14

The D15 source reads the D14 file only to verify its SHA-256.  It does not
import the module or instantiate any of the repaired objects:

```text
Port
Obj
Mor
sealed_map
record_id
join_entitlement.
```

Hashing a bridge does not traverse it.  The D15 matrices have compatible
dimensions, but no exact check proves that they are admitted by D14's typed
source category, that the environment record receives persistent identity,
that its owner is preserved, or that the live collar participates in the
declared continuation grammar.

The distinction is operational, not cosmetic.  Starting from the D15 seal on
`|0>`, I applied

```math
I_S\otimes X_R\otimes I_C.
```

The raw record distribution changed exactly from `(1,0)` to `(0,1)`.  No D15
constructor rejected the operation because the receipt has no protected
constructor.  D14 would reject the same map when `R` is a sealed source port.

The built-in later-action check uses only a specially written helper that
acts on the system index and leaves the record index untouched.  It proves
that this selected `H_S tensor I_R tensor I_C` preserves the marginal; it does
not place all later D15 dynamics inside D14's licensed protected class.

### Required repair M3/M4

Construct one end-to-end typed cell through the reviewed D14 API:

1. declare finite system, environment, record and collar ports, with ownership
   and a persistent record ID;
2. construct the action-derived `H` and CNOT kernels as admitted `Mor`s;
3. include the supplied boundary state and fresh environment state;
4. obtain the seal by composing environment preparation, CNOT and live-collar
   preparation, rather than hard-coding a second matrix;
5. verify that the resulting matrix equals the intended seal;
6. append a licensed future system morphism and verify its `sealed_map`;
7. attempt the hostile record flip and require constructor rejection;
8. state whether the system/environment interaction is one owned component or
   carries an explicit join entitlement; and
9. explicitly declare that the finite qubit toy has no gauge redundancy,
   hence identity gauge quotient, unit Faddeev–Popov factor and no boundary
   gauge edge modes.

Only then does the example enter the repaired D14 bridge.  This would close a
finite nongauge S4 witness, not the EFT4/gravity action-to-D14 dictionary.

## 4. Bell, decoherence, record and memory cells

### Bell preparation

**Mathematically correct at finite state-preparation scope.**

`CNOT(H tensor I)|00>` is exactly

```math
(|00>+|11>)/\sqrt2.
```

Both reduced density matrices are `I/2`, the computational-basis outcomes
agree with probability one, and a local Hadamard on the first subsystem
leaves the second reduced state unchanged.  These are valid Bell-state and
one-marginal no-signalling checks.

They are not a CHSH experiment, Bell self-test or action selector.  “Bell
record” should be replaced by “Bell-state computational-basis correlation”
unless explicit local record instruments and measurement settings are added.

### Seal and decoherence

**Exact once the split, basis and fresh state are supplied.**

For `|+>_S|0>_E`, CNOT gives the maximally entangled state

```math
(|00>+|11>)/\sqrt2,
```

and tracing `E` gives `I/2` on `S`.  The pointer-basis off-diagonal is exactly
zero.  This proves one complete dephasing interaction, not autonomous pointer
selection or durable-record redundancy.

The current `seal_from_cnot_with_live` is independently hard-coded.  The
receipt does not compare it with CNOT acting on an injected `|0>` environment,
and the collar `|1>` is appended as another supplied state rather than
generated by the CNOT action.  Add that factorization equality and retain the
paper's correct admission that the split, initial state, pointer reading and
protected interpretation are supplied.

S5 therefore passes only as an honest **disclosure of extra coarse-graining
data**.  It does not pass the autonomous-record branch of S5.  The sentence
that the result “closes a finite instance of S4/S5” should make this split
explicit.

### Memory

The imported 16-dimensional permutation is unitary and the two nonzero
terminal states `0000` and `1101` do encode a visible dependence of the final
bit on the earlier bit while the current visible bit agrees.  But D15 imports
this matrix from D13 rather than composing its own CNOT action kernels, and it
checks two density-matrix entries rather than the conditional probabilities.

To claim an action-derived non-Markov record cell, rebuild the permutation
from the D15 CNOT generators, add the sequential D14 record morphisms, and
freeze the exact conditionals

```text
P(Z=1 | Y=0,X=1)=1,
P(Z=1 | Y=0,X=0)=0.
```

Until then this is a correct imported memory carrier, not a new completed
action-to-record derivation.

### Alternative action

**PASS.**  Left multiplication by `diag(1,i)` produces a distinct unitary
kernel.  It can be written as the same supplied measure with an added
output-dependent phase.  This is a valid exact reminder that constructing one
dictionary does not select it.

## 5. EFT normal form and uniqueness

The central limited statement is sound:

```text
given 3+1 Lorentzian fields, representations, gauge structure, locality and
an EFT expansion, consistency strongly constrains the operator architecture
but does not determine all Wilson coefficients or a UV completion.
```

The current formula is nevertheless schematic rather than the maximal action
promised by S1/S2.

### Missing curved-space operator

With the Standard Model Higgs doublet and a dynamical metric, diffeomorphism
and gauge invariance allow

```math
\xi H^\dagger H R.
```

It has canonical dimension four.  It is neither a pure higher-curvature term
nor a `d>4` SMEFT correction.  Omitting it makes the displayed combined
gravity-matter normal form non-maximal even at the renormalizable level.

The full tower also contains mixed curvature-matter operators.  Their basis
depends on integrations by parts, Bianchi identities, equations of motion and
field redefinitions.  Pure curvature-squared terms are likewise basis
dependent; in four dimensions the Euler/Gauss–Bonnet combination requires
special treatment, including boundaries.

### Matter enumeration

Section 3 lists assumptions and unselected parameters but does not enumerate
the renormalizable Standard Model action as frozen S2 requests.  At minimum
the final theorem should name:

```text
gauge kinetic and theta terms;
fermion kinetic/covariant couplings;
Higgs kinetic, mass and quartic terms;
Yukawa matrices and their hermitian conjugates;
gauge fixing, ghosts and anomaly-cancellation status;
the global gauge-group choice, not only its Lie algebra.
```

Observed neutrino masses require an explicit choice: the dimension-five
Weinberg operator in SMEFT, right-handed neutrinos, or another declared field
extension.  That choice may not be hidden inside “observed representations.”

### Normal-form equivalence and truncation

There is no single literal infinite list called *the* EFT action.  A useful
normal form requires:

```text
field content and symmetry/global gauge data;
operator-basis equivalence modulo total derivatives, identities, equations of
motion and allowed field redefinitions;
renormalization scheme and scale;
power counting and cutoff;
finite truncation order and an error estimate for the stated domain.
```

“At ordinary energies” supplies none of the last three.  S0 therefore remains
open.  The honest uniqueness statement is uniqueness of an operator basis
**up to the declared equivalences at a chosen truncation**, not uniqueness of
the numerical action.

Deser's consistency completion supports the leading Einstein interaction
after the massless spin-two seed and other hypotheses are assumed.  It does
not alone prove the entire displayed gravity EFT normal form or choose its
field variables, measure, boundary terms and quantum state.  The working note
mostly states these limits correctly; its word “select” should consistently
mean “fixes the allowed form conditional on the listed premises.”

### Required repair M5/M6

1. Add `xi H^dagger H R` and explicitly include mixed gravity-matter terms in
   the higher-operator tower.
2. State the operator equivalence relation and choose a named basis at each
   frozen truncation.
3. Give an actual energy/cutoff domain, regulator/scheme and truncation error
   convention for the theorem.
4. Enumerate the dimension-at-most-four matter sectors and state the neutrino
   completion.
5. Replace literal-action uniqueness with conditional normal-form uniqueness
   modulo the declared redundancies.

## 6. Coupling and scale ledger

The table correctly denies derivation of `G`, `Lambda`, gauge couplings,
Yukawas, the Higgs scale and record coarse-graining scales.  That is an
important positive result.

It does not yet satisfy S3's parameter-by-parameter classification.  Several
rows mix distinct statuses:

- a renormalized coupling is an RG datum at a chosen scale **and** is inferred
  from measurement;
- masses and mixing parameters are derived combinations of Yukawa and Higgs
  parameters after conventions and field redefinitions, not an independent
  undifferentiated row;
- `theta_QCD`, Higgs quartic and mass-squared, CKM/PMNS phases and any neutrino
  parameters need explicit entries;
- Wilson coefficients are meaningful only with their operator basis,
  normalization, scheme and renormalization scale;
- symmetry, anomaly cancellation, hermiticity, positivity/analyticity and RG
  mixing can relate or bound coefficients, so “free” must mean independent
  after those constraints, not arbitrary.

Create a machine-readable or explicit table with columns for operator,
coefficient, mass dimension, basis/scheme/scale, status, evidence source and
remaining uncertainty.  This will separate normalization conventions,
consistency relations, RG input, empirical fit and genuine UV predictions as
the protocol requires.

## 7. Frozen-gate disposition

```text
S0  FAIL/PARTIAL  effective scope is acknowledged, but domain, regulator,
                   scheme and truncation are not specified.
S1  PARTIAL       leading spin-two consistency form is correctly scoped;
                   maximal gravity EFT basis is not derived or enumerated.
S2  FAIL/PARTIAL  assumptions and free data are honest; promised matter
                   enumeration and curved-space completion are absent.
S3  PARTIAL       correct qualitative ledger, insufficient coefficient-level
                   classification.
S4  FAIL          finite matrices exist, but action/measure/support are not
                   separated and no object enters the D14 API.
S5  PASS only for disclosure; FAIL for autonomous records.  The split, state,
                   pointer basis, collar and protected interpretation remain
                   supplied.
S6  PARTIAL       tensor interchange passes for supplied cells; no diagram
                   generation or join-origin law is derived.
S7  PASS in prose  3+1 and Lorentzian structure are correctly called inputs;
                   V9 would be recovery, not emergence.
S8  OPEN          no frozen empirical candidate adjudication has yet run.
S9  PASS          no untouched V9 holdout is opened.
S10 OPEN          listing incomplete UV programs is not yet a matched
                   low-energy survivor construction.
S11 OPEN          this is hostile round 1.
```

The document's retained formal status `INCOMPLETE-INVESTIGATION` is therefore
correct.  Neither `LOW-ENERGY-EFFECTIVE-RULEBOOK-IDENTIFIED` nor a finite S4
closure should be frozen yet.

## Exact repair order

1. Separate phase action, local measure, support constraints and gluing
   measure in the finite packet.
2. Derive CNOT from explicit auxiliary `Z2` multipliers or downgrade it to a
   supplied constrained kernel.
3. Rebuild the seal from that CNOT and explicit environment/collar states.
4. Pass the resulting objects through D14 `Mor`/`Port` admission and add the
   overwrite countercontrol.
5. Rebuild the memory unitary from D15 generators and evaluate the two exact
   non-Markov conditionals.
6. Complete the curved-space EFT basis, including `H^dagger H R`, declare
   equivalences/truncation/domain, and expand the S3 coefficient ledger.
7. Keep the final ceiling conditional unless the state/environment/pointer
   packet is autonomously selected and the UV/empirical gates close.

## Final verdict

**MAJOR REVISION.**  All 22 printed matrix checks pass, and the receipt is a
good finite kernel-and-environment demonstration.  It is not yet an executed
action-to-D14 dictionary: essential measure/support data are supplied but not
separated, and the supposed sealed record lives outside the D14 protection
layer.  The proposed low-energy EFT conclusion is plausible only after the
missing curved-space operator content, truncation/equivalence scope and
coefficient ledger are repaired.  Preserve `INCOMPLETE-INVESTIGATION` through
the next round.
