# D13 hostile round-1 mathematics review

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION / INCOMPLETE-INVESTIGATION**  
**Finite iSWAP nonuniqueness witness:** mathematically correct  
**Universal functor/action theorem:** not established  
**Claim that the frozen action gates have been completed:** false at present

## Bottom line

D13 contains one sound theorem inside several claims that are too broad.  The
sound theorem is that the stated finite local-kernel principles do not select a
unique member of the exchange-unitary family: `sqrt-iSWAP` and iSWAP satisfy
the listed algebraic symmetries and give different probabilities in the same
fixed preparation/readout experiment.  That is an exact action/kernel
nonselection witness.

The note does not prove that sealed diamonds form the asserted symmetric
monoidal category, that all admissible quantum laws are functors into the
undefined target `Hilb/CP`, that local amplitude composition produces a
non-Markov visible-record process, or that arbitrary amplitude modulus and
phase are SHARD evidence and sealed holonomy.  The executable tests a single
matrix composition, one disjoint tensor-factor commutator, one change of
unitary basis, and an orthogonal pointer dilation.  Those cells do not execute
the universal A2–A6 quantifiers.  The continuum `phi^4` paragraph is valid only
after significant Minkowski/EFT/asymptotic-state hypotheses, not for any
generally covariant scalar theory.

Most decisively, the protocol says `INCOMPLETE-INVESTIGATION` when a promised
class, gate, calibration, hostile review, or receipt is absent.  The theorem
note itself leaves A12 pending, A0 subject to a future rerun/hash, physical
ontology and couplings primitive, and most architecture classes unimplemented.
It therefore cannot yet assign
`UNIVERSAL-ACTION-ARCHITECTURE/PRIMITIVE-COEFFICIENTS`.

## Frozen artifacts and execution status

```text
c34f7212681007199e73f55ab6a2b7d9861d8e3e38bf3bf248024010c462d6be  note-d13-action-selection-protocol.md
91385afa761ff54a53eecd7e08aabbd33aa473357f498b9ae7f8341587e2caf9  note-d13-maximal-action-theorem.md
1674fc60dffbefd2d39e8ce24e65ffa6e05af3982c38f8268e718ffbe727dd57  code/d13_local_action_family_exact.py
474a234e1eb51100aef57ed658ae3c5fa0a3e2236af88b64d14f0070a6de84ea  data/d13-local-action-family-exact.json
```

The checked-in JSON reports 12/12 true gates and semantic SHA-256
`474a234e...`.  Its bytes are stable.

I attempted both normal and optimized execution.  Both failed before any check
with:

```text
ModuleNotFoundError: No module named 'sympy'
```

The default workspace Python has no declared SymPy dependency, and the bundled
dependency locator did not return a usable runtime.  Thus I could not reproduce
the production script as submitted.  I independently reconstructed the 12
finite claims algebraically below; no listed matrix identity appears wrong.
The dependency failure is nevertheless a receipt defect.  A hostile reviewer
must not be required to infer an unrecorded environment.

**Repair:** provide a locked runtime/dependency manifest or rewrite this small
exact witness using the standard-library `Q(sqrt(2),i)` implementation already
used in D12.  Gate the expected check count, semantic hash, source hash, and
normal/optimized stdout hash.

## 1. The finite iSWAP algebra

Let

$$
X_{\rm ex}=|01\rangle\langle10|+|10\rangle\langle01|,
\qquad U_\theta=e^{i\theta X_{\rm ex}}.
$$

On the one-excitation subspace this is

$$
\begin{pmatrix}\cos\theta&i\sin\theta\\
i\sin\theta&\cos\theta\end{pmatrix},
$$

and it is the identity on `|00>,|11>`.  Therefore:

- `U_theta` is unitary;
- it commutes with total excitation number and leg exchange;
- `U_(pi/4)^2=U_(pi/2)`;
- tensor-disjoint copies commute;
- `U_(pi/4)` does not commute with `Z tensor I`, so overlap can carry physical
  order;
- conjugating input, output, state, and effect consistently by independent
  unitaries preserves the trace probability;
- from `|10>`, the `|10>` probability is `cos^2(theta)`, hence `1/2` and `0`;
- `U_(pi/4)|01>` has concurrence one;
- `U_(pi/2)|++>` also has concurrence one.

The pointer map `W|j>=|j>|j>` obeys `W^dagger W=I`.  Orthogonal pointer
projectors satisfy `P_a P_b=delta_(ab)P_a`; consequently the displayed
decoherence matrix is diagonal and its diagonal sums to one.  These are exact
identities, not numerical coincidences.

### Finding M1 — the note's “same support” statement is false

The two matrices have the same ambient four-dimensional carrier and the same
allowed pointer labels, but not the same nonzero matrix or prediction support.
At `theta=pi/2`, the cosine entries vanish.  From `|10>`, quarter-iSWAP has two
positive pointer outcomes whereas half-iSWAP has only one.  Replace “same
support” by “same ambient carrier, types, grammar, and allowed outcome set.”

This does not weaken the nonselection theorem: different induced positive
support is itself part of the different physical law.

### Finding M2 — fix the physical interval before calling the actions inequivalent

The code proves `U_(pi/4)^2=U_(pi/2)`.  Thus the half gate is exactly two
quarter gates composed.  The one-diamond predictions are inequivalent only
when “one diamond” denotes the same fixed operational interval/evidence slab
and is not freely reparameterized.  D13's packet leaves the evidence/proper-time
and physical-unit bridge primitive.

The fixed one-diamond preparation/readout already suffices to distinguish the
kernels inside the declared discrete grammar, so the finite-kernel
nonuniqueness result survives.  But a claim about inequivalent dimensionful
actions must freeze the boundary interval or coupling-time convention.  State
that hypothesis explicitly.

The two gates are also not related merely by unitary conjugation and a common
phase: their eigenvalue ratios differ.  Hence the fixed-kernel distinction is
not just a basis artifact.

## 2. The functor claim

### Finding M3 — `Diam` and `Hilb/CP` are not defined sufficiently to support a theorem

Calling `Diam` a symmetric monoidal category requires definitions and proofs
of:

- objects and typed identity morphisms;
- the exact internal-presentation equivalence relation;
- well-defined composition on equivalence classes;
- associativity and unit laws;
- tensor product, symmetry, and coherence;
- compatibility between coherent alternative sums and the quotient.

None is supplied.  The executable proves only one matrix identity
`U_(pi/4)U_(pi/4)=U_(pi/2)` and one disjoint commutator.  Matrix multiplication
is associative, but that does not prove that arbitrary sealed-diamond gluing,
screen contraction, refinement, coherent summation, and construction quotient
form the claimed category.

The target `Hilb/CP` is also undefined.  Hilbert spaces and linear maps,
projective Hilbert spaces, completely positive maps, and the CPM construction
are different categories with different objects and composition.  A unitary
amplitude functor normally lands in a linear category; open instruments land
in an operator/CP-map category.  The slash does not define how these are mixed.

**Required repair:** either present this section as a candidate architecture,
or define the source and target categories and prove the functor/coherence
laws.  Do not call it “the selected mathematical type” before an A7
architecture comparison.

### Finding M4 — a formal path integral is not a general functor proof

The expression

$$
Z_D=\int \mathcal D\phi\,e^{iS_D/\hbar}
$$

is conditional on the measure, contour, gauge fixing, regulator, anomalies,
boundary and corner terms, and a valid gluing theorem.  The note correctly
lists many of these inputs, but then grades the “standard functorial form” as a
general A3 pass.  In gauge theory and gravity, gluing can require edge modes,
ghost determinants, boundary charges, anomaly cancellation, and nontrivial
sewing measures.  Listing those missing data does not prove the functor.

The safe result is a **maximal candidate schema**: when a supplied action has a
well-defined local sewing construction, it can define such a functor.  D13 has
not proved that all admissible diamond actions do so or that this architecture
is uniquely forced.

## 3. Non-Markov claim

### Finding M5 — amplitude composition permits memory but does not imply it

The statement that visible records “can be non-Markov” is plausible and
standard: an unobserved environment retained between interventions can make
the reduced visible process non-Markov.  But neither the functor clauses nor
the D13 executable construct such a process.

Writing a class operator `C_alpha` for a full sequence does not by itself show
that

$$
P(r_{n+1}\mid r_n,\ldots,r_1)
\ne P(r_{n+1}\mid r_n).
$$

A Markov process also assigns operators or weights to full histories.  The
one-diamond iSWAP experiment has no pair of equal current records with distinct
pasts and different next-record probabilities.  Coarse-graining can produce
memory; it can also produce a Markov reduced process.

**Required repair:** either change the claim to “the architecture does not
force Markovity” or build an explicit multi-time environment/process-tensor
witness and evaluate the two conditional probabilities above.  The D12 `P_r`
family could serve as a classical control but does not demonstrate that the
D13 amplitude witness itself is non-Markov.

## 4. Polar/RN representation

For a fixed positive scalar reference `nu(H)` and a nonzero scalar complex
amplitude `K(H)`, the atomwise identity

$$
I(H)=-\log\frac{|K(H)|^2}{\nu(H)},\qquad
\Phi(H)=\arg K(H),
$$

$$
K(H)=\nu(H)^{1/2}e^{-I(H)/2+i\Phi(H)}
$$

is correct.  Its scope is much narrower than the interpretation attached to
it.

### Finding M6 — uniqueness omits the declared global phase/normalization quotient

The protocol declares overall history-independent phase and normalization
physically equivalent.  Replacing

$$
K(H)\mapsto c e^{i\delta}K(H)
$$

shifts every coordinate by

$$
I(H)\mapsto I(H)-2\log|c|,
\qquad
\Phi(H)\mapsto\Phi(H)+\delta.
$$

Therefore the coordinates are not unique merely “modulo `2pi` phase.”  They
are unique only after fixing amplitude normalization and global phase, or
after quotienting common additive constants in both coordinate families.
Changing the positive reference `nu` also shifts `I`.

Zeros are excluded, yet exact destructive interference and forbidden record
outcomes naturally create zero amplitudes.  A complete representation needs a
support field plus polar coordinates on that support, just as D12 eventually
required.

### Finding M7 — arbitrary polar modulus and phase are not automatically SHARD evidence and holonomy

`|K|^2/nu` is an RN derivative only when it is the density of a normalized
positive measure relative to `nu`.  Before coherent alternatives are summed,
individual path-amplitude moduli need not form the physical probability law.
Indeed interference is precisely why probabilities are not generally obtained
by summing `|K(H)|^2` over unresolved microscopic histories.

Moreover `I(H)` may be negative and reference-dependent.  No KL accumulation,
eventless additivity, orientation, or survival law is proved.  Likewise an
arbitrary argument `arg K(H)` is a phase coordinate, not automatically a
sealed holonomy: holonomy requires specified loops/transport, orientation,
gauge transformation, and composition/cocycle laws.

**Required repair:** call this an atomwise polar representation of a supplied
nonzero scalar amplitude.  Identify `I` with SHARD evidence only after proving
the RN normalization and evidence-gluing hypotheses; identify `Phi` with
sealed holonomy only after proving the relevant gauge/cocycle laws.  Coherent
sums must be treated before probability-level RN language is applied.

This is the most important conceptual flaw in the theorem note.

## 5. Covariance and construction order

### Finding M8 — the covariance check is exact but tautologically narrow

The code uses two exact unitary basis changes and transforms all four relevant
objects:

```text
K'   = G_out K G_in^dagger
rho' = G_in rho G_in^dagger
E'   = G_out E G_out^dagger.
```

Trace invariance then follows algebraically.  This is a valid independent
input/output basis-covariance test.  It is not a test of Lorentz covariance,
diffeomorphism covariance, a local gauge constraint, anchors, order units,
screen/link transport across a network, or an anomaly-free path-integral
measure.

The JSON verdict `LOCAL-COVARIANT-ACTION-UNIQUENESS-REFUTED` should therefore
say `FINITE-LOCAL-UNITARY-KERNEL-UNIQUENESS-REFUTED`.  Paper 13 may cite the
D12 multi-vertex unitary-frame construction separately, but D13's one trace
identity cannot earn the full A6 gate.

The disjoint construction check is similarly a correct two-tensor-factor
cell.  General finite schedules require the adjacent-swap/linear-extension
lemma and the hypothesis that every incomparable pair is physically disjoint.
D12 supplied that argument; D13 should import it explicitly rather than infer
the universal quotient from one commutator.

## 6. Records and quantum consistency

### Finding M9 — orthogonal pointer alternatives are not yet durable records

The pointer isometry is exact, and the off-diagonal calculation is correct.
But exact diagonality is built into mutually orthogonal projectors:

$$
P_bP_a=0\quad(a\ne b).
$$

This proves an exclusive projective measurement dilation.  It does not prove:

- autonomous environment-induced decoherence;
- persistence after later allowed interactions;
- repeat-read stability;
- immutable record identity/provenance;
- output-collar birth;
- observational truncation versus physical deletion.

The theorem's premise “exact durable records” and the executable comment
“exclusive durable records” therefore overstate the object.  The gate table is
more honest when it says the record partition/instrument is not uniquely
selected.  Grade A5 as “primitive orthogonal pointer instrument; durability
not executed here,” or explicitly reuse the D12 durable-record constructor and
show compatibility with the action kernels.

### Finding M10 — A4 is not fully executed

The finite witness verifies unitarity, normalized positive pointer
probabilities, entangling capacity, and an exact pointer partition.  It does not
execute an interference experiment, no-signalling with independently chosen
local interventions, an open-system/Kraus limit, or protection against Born
weights being inserted twice.  Those may follow in suitable standard quantum
models, but the frozen A4 gate asks that they be tested.

Do not label A4 a full pass from these 12 checks.  Record exactly the verified
subgates.

## 7. Physical inequivalence

**The finite operational inequivalence claim passes.**

With the preparation `rho=|10><10|` and effect `E=|10><10|` held fixed,

$$
\operatorname{Tr}(E U_{\pi/4}\rho U_{\pi/4}^\dagger)=\frac12,
\qquad
\operatorname{Tr}(E U_{\pi/2}\rho U_{\pi/2}^\dagger)=0.
$$

An allowed record relabeling must preserve every instrument probability, so it
cannot erase this difference in the fixed experiment.  The different spectral
ratios also rule out unitary conjugation plus global phase.  Subject to the
fixed one-diamond interval noted in M2, the kernels are physically
inequivalent under the protocol's equivalence criterion.

This exact pair is sufficient to refute unique derivation from the **shared
finite-kernel premises**.  It is not sufficient to prove that the proposed
functor architecture is universal.

## 8. Continuum `phi^4` strengthening

### Finding M11 — the continuum statement lacks the hypotheses needed for a `2 -> 2` theorem

Adding a nondifferentiated real-scalar interaction

$$
-\int d^4x\sqrt{-g}\,\frac{\lambda}{4!}\phi^4
$$

is diffeomorphism invariant and leaves the **classical differential principal
part** unchanged.  In perturbative scalar QFT on Minkowski or a suitable
asymptotically flat background, with stable particle states and fixed field
normalization, nonzero `lambda` changes the connected `2 -> 2` amplitude.  In
that restricted sector the strengthening is valid.

It is not valid as written starting from “any local generally covariant
scalar-field action”:

- a generic curved spacetime has no global S-matrix or canonical `2 -> 2`
  amplitude;
- the original theory may impose shift, conformal, gauge, supersymmetric, or
  other symmetries that `phi^4` violates;
- the scalar may lack stable asymptotic one-particle states;
- stability/unitarity restricts the sign and UV interpretation of `lambda`;
- quantum corrections and regularization require declared renormalization
  conditions;
- higher-curvature additions can change differential order and introduce extra
  modes, so they cannot all inherit the same principal-part statement.

**Required repair:** state a real scalar EFT on Minkowski/asymptotically flat
background with no symmetry forbidding `phi^4`, perturbative nonzero coupling,
specified vacuum/asymptotic states, and fixed renormalization convention.  Then
the family is a good continuum nonuniqueness witness, not a theorem about every
generally covariant scalar action.

## 9. Gate verdict and architecture census

### Finding M12 — the protocol itself forces `INCOMPLETE-INVESTIGATION`

The gate table cannot support the submitted verdict:

```text
A0  called pass but explicitly awaits final inventory rerun/hash
A1  physical types, grammar, boundaries, reference and scales remain primitive
A2  only one disjoint finite cell is computed
A3  only one matrix gluing identity is computed; general sewing is conditional
A4  several frozen quantum subgates are absent
A5  durability is not constructed in D13
A6  only unitary basis covariance of one probability is computed
A7  unique finite-kernel selection is genuinely refuted
A8  field content and coefficients remain primitive
A9  units, G and clock/length bridges remain open
A10 no empirical selection is performed
A11 correctly prohibited
A12 explicitly pending
```

The protocol says:

```text
INCOMPLETE-INVESTIGATION
  a promised class, gate, calibration, review, or receipt is absent.
```

It also requires every surviving architecture class A–H to be implemented or
excluded.  The theorem note does not execute that comparison.  In particular,
declaring a symmetric monoidal functor as “the selected mathematical type” is
not an A7 proof that primitive path measures, topological/information actions,
geometric actions, bootstraps, or other generalized-process architectures all
reduce uniquely to that schema.

`UNIVERSAL-ACTION-ARCHITECTURE/PRIMITIVE-COEFFICIENTS` would be defensible only
after proving that the local amplitude/functor form itself is fixed across the
surviving architecture census.  The exact iSWAP pair instead proves a narrower
negative result: even inside one finite unitary architecture, the coupling is
not selected.

The correct round-1 endpoint is therefore:

```text
FINITE LOCAL UNITARY KERNEL NONUNIQUENESS = PROVED
GENERAL ACTION/FUNCTOR ARCHITECTURE       = CANDIDATE
D13 FROZEN PROTOCOL VERDICT               = INCOMPLETE-INVESTIGATION
```

## Minor receipt and wording findings

### m1 — the check named `same_local_generator` does not test what its name says

It checks that `X_ex` commutes with number and swap.  Both unitaries are
constructed from the same generator by definition, but no exponential identity
is evaluated.  Rename the check `generator_respects_number_and_exchange`.

### m2 — the JSON is not bound to the source or expected semantic hash

The program computes the JSON hash but has no frozen expected check count,
expected semantic hash, source hash, or normal/optimized stdout receipt.  A
changed program can generate a new self-consistent JSON without failing.  Add
those gates and record the SymPy version.

### m3 — “maximal action theorem” is the wrong title at this stage

The exact result is a nonuniqueness theorem inside a local exchange-unitary
family, plus a proposed action architecture.  “Maximal” suggests an exhausted
class or universal characterization that has not been proved.

## What survives hostile review

- The quarter-/half-iSWAP matrix algebra is exact.
- Both gates share unitarity, exchange symmetry, excitation conservation, and
  nonzero—indeed maximal—entangling capacity.
- One fixed preparation/readout distinguishes them by probabilities `1/2` and
  `0`.
- Disjoint tensor-factor operations commute and the displayed overlap control
  does not.
- Consistent independent unitary input/output basis changes preserve the fixed
  instrument probability.
- The pointer isometry gives a normalized exactly diagonal orthogonal-pointer
  history partition.
- These facts refute unique kernel/coupling selection from the shared finite
  structural principles.
- Action form, symmetry, evidence coordinates, and Born calculus do not by
  themselves choose the numerical coupling.
- No D13 geometry holdout is licensed before an action is independently
  selected.

## Exact opening ledger

```text
M1   MODERATE  “same support” is false; only ambient carrier/grammar are shared.
M2   MODERATE  physical interval/evidence slab must be fixed before action inequivalence.
M3   MAJOR     Diam and Hilb/CP are undefined; symmetric monoidal functor not proved.
M4   MAJOR     formal path integral does not establish general sewing/functoriality.
M5   MAJOR     non-Markov visible-record process is permitted but not constructed.
M6   MAJOR     polar-coordinate uniqueness omits global normalization/phase quotient and zeros.
M7   MAJOR     arbitrary modulus/phase are not automatically SHARD evidence/holonomy.
M8   MAJOR     one unitary basis-covariance identity does not pass general covariance A6.
M9   MAJOR     orthogonal pointer dilation does not establish durable records.
M10  MAJOR     interference/no-signalling/open-system A4 subgates are absent.
M11  MAJOR     phi^4 strengthening needs Minkowski/EFT/asymptotic-state hypotheses.
M12  FATAL-TO-CURRENT-VERDICT
               architecture census and multiple frozen gates are incomplete;
               protocol verdict must be INCOMPLETE-INVESTIGATION.

m1   MINOR     rename misleading same_local_generator check.
m2   MINOR     bind JSON to expected hashes, check count, source and SymPy version.
m3   MINOR     retitle theorem to distinguish candidate schema from proved no-go.
```

## Final decision

**MAJOR REVISION.**  Preserve the exact finite iSWAP nonselection theorem and
the geometry refusal.  Downgrade the functor to a candidate architecture,
downgrade polar/RN language to scalar support-relative polar representation,
construct or withdraw the non-Markov and durable-record claims, narrow the
continuum example, and apply the protocol's own
`INCOMPLETE-INVESTIGATION` verdict until A0–A12 and the A–H census are actually
closed.
