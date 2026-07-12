# D15 working theorem — the maximal action current evidence warrants

**Status:** derivation draft under the frozen D15 protocol, 2026-07-11.

## 1. Result first

The strongest action law presently selected by independent evidence is not a
complete microscopic click law.  It is a domain-limited effective action:

```math
S_eff
= integral d^4x sqrt(-g) [
    (M_Pl^2/2)(R-2 Lambda)
    + L_SM
    + xi_H H^dagger H R
    + a_1 R^2 + a_2 R_{mu nu}R^{mu nu} + ...
    + sum_{d>4,i} C_i^(d) O_i^(d)/Lambda_UV^(d-4)
  ]
+ S_boundary + S_gf + S_ghost.
```

Here `L_SM` is the Standard Model Lagrangian for the empirically observed
field representations and gauge group.  The ellipses are not optional
ignorance: effective-field-theory logic requires every local operator allowed
by the symmetries, ordered by dimension/derivatives.

Operators are counted only after quotienting integration by parts, algebraic
identities, leading equations of motion and perturbative field redefinitions.
In four dimensions the Euler/Gauss–Bonnet density is topological at fixed
topology.  A truncation is meaningful only with a declared energy/curvature
domain and power-counting error.

At ordinary energies this is the simplest **normal form**, not one uniquely
fixed numerical action.  Field content, dimension and signature are empirical
inputs; many coefficients are measured; higher operators encode possible UV
physics.  No known principle in the SHARD corpus derives all of them.

## 2. What consistency really selects

Start with a massless spin-two field, local propagation and its linear gauge
invariance.  Coupling it consistently to its own conserved stress tensor
forces the nonlinear Einstein interaction, up to field redefinitions,
normalization, cosmological and higher-derivative terms within the declared
low-energy assumptions.  Deser's self-coupling derivation establishes this
kind of consistency completion:
<https://arxiv.org/abs/gr-qc/0411023>.

This selects the leading interaction **form**.  It does not select:

```text
the existence of the spin-two field;
3+1 rather than another dimension;
Lorentzian rather than another signature;
Newton's coefficient G;
the cosmological constant;
the quantum state;
higher-curvature Wilson coefficients;
a UV completion.
```

General relativity is nevertheless a consistent predictive quantum effective
field theory at ordinary energies, as emphasized by Donoghue:
<https://arxiv.org/abs/gr-qc/9512024>.

## 3. What the matter assumptions select

Given, rather than deriving,

```text
3+1 local Lorentzian QFT;
SU(3) x SU(2) x U(1);
the observed chiral fermion representations;
one Higgs doublet;
gauge invariance and renormalizability,
```

the dimension-at-most-four matter action has the Standard Model operator
form.  Quantum consistency constrains anomaly combinations and gauge
couplings relate interaction vertices within each gauge sector.

It does not calculate the representation list, three generations, Yukawa
matrices, mixing phases, Higgs parameters, strong theta angle or gauge
couplings.  Those are empirical inputs at a renormalization scale.  Beyond
dimension four, the symmetry-allowed operator space reopens; the Warsaw-basis
work is one standard explicit classification:
<https://arxiv.org/abs/1008.4884>.

Thus “the Standard Model” is both remarkably constrained and numerically
non-derived.

## 4. Parameter and scale ledger

| Quantity | D15 classification |
|---|---|
| `c`, `hbar` | unit/conversion constants once the quantum-relativistic unit system is fixed; their measured bridge is physical |
| `G` or `M_Pl` | measured coefficient of the leading gravitational action; not set by D14 or SHARD dimensionless records |
| `Lambda` | measured cosmological coefficient; radiative/naturalness problem not solved |
| gauge couplings | measured renormalized coefficients with RG running constrained by the action |
| Yukawas/masses/mixing | measured matrices/coefficients, not fixed by gauge symmetry |
| Higgs scale | measured relevant parameter, not derived here |
| higher EFT coefficients | constrained or unmeasured; encode UV sensitivity |
| causal-set discreteness/nonlocality scale | extra candidate parameter unless predicted and calibrated |
| spin-foam Immirzi/refinement data | extra candidate data unless removed or measured |
| record coarse-graining/environment scale | state/apparatus-dependent in ordinary decoherence; not a universal constant derived here |

Recovering metres and seconds does not by itself make a discrete cone rounder.
It calibrates the axes.  Shape improvement requires the dynamics or a
continuum/refinement limit to reduce anisotropy.  `G` combines with `hbar` and
`c` to define the Planck length, but that uses an empirically known `G`; it is
not generated from dimensionless evidence alone.

## 5. The regional amplitude supplied to D14

For a finite region `M` with boundary data `varphi_boundary`, the formal
regional kernel is

```math
K_M[varphi_boundary]
= integral_{fields|boundary} Dg Dphi
  Delta_gf exp(i S_eff[g,phi]/hbar).
```

Composition across a common unsealed boundary integrates/sums the shared
boundary data.  A controlled regulator or lattice makes this a finite D14
kernel.  Gauge theories require the correct constraints, ghosts or reduced
measure, boundary charges and often edge modes.  Gravity requires appropriate
boundary/corner terms and a definition of the metric/causal-structure sum.

This supplies the D14 regional-amplitude input **conditional on** all those
choices.  It also explains why row-normalizing each local click is wrong:
unrecorded internal alternatives interfere before the final state/effect
pairing.

## 6. Where records enter

The effective action plus a state and an environment can generate an
instrument through unitary entanglement:

```math
|s_0>|E_0>
  -> sum_r M_r|s_0>|E_r>,
qquad <E_r|E_s> approximately delta_{rs}.
```

Stable, redundantly accessible environment states can behave as records.
After specifying the system/environment split, initial state, coarse graining
and stability tolerance, these `M_r` feed D14's sequential protected-record
construction.

But the split and pointer basis are generally state-, interaction- and scale-
dependent.  Ordinary decoherence explains why particular records are stable
in a given world; it does not currently provide a unique fundamental seal
instrument for every possible diamond from the bare action alone.  Therefore
the action-to-D14 dictionary remains conditional at exactly this point.

## 7. What this action says about cones and dimension

For the two-derivative Einstein–Standard-Model action, the principal symbols
of minimally coupled massless fields propagate on the metric null cone.  In a
local inertial frame the infinitesimal cone is Lorentz-round.  The
multimessenger observation GW170817/GRB 170817A tightly constrains a mismatch
between gravity and light speeds:
<https://arxiv.org/abs/1710.05834>.

This is powerful empirical selection of the low-energy propagation law.  It
does not explain why a record graph should first become a smooth metric, why
the dimension is `3+1`, or why finite V9 webs approach that cone.  EFT4 assumes
those structures.  Higher-dimension operators can produce suppressed
dispersion/birefringence, and observations constrain their coefficients.

Consequently an EFT4-to-V9 run would be a **recovery/calibration** test, not an
emergence or fundamental-selection test.  Its continuum target is already
built into the source action.

## 8. UV survivors

At least three structurally different routes can aim to reproduce the same
effective action:

- the Benincasa–Dowker causal-set curvature/action construction introduces a
  discrete causal order and a nonlocality scale
  (<https://arxiv.org/abs/1001.2725>);
- spin-foam amplitudes quantize four-dimensional discrete gravity with
  boundary states and simplicity constraints
  (<https://arxiv.org/abs/0708.1236>);
- asymptotic safety seeks a Lorentzian UV fixed trajectory for matter and
  gravity; the 2026 status review reports substantial progress while still
  describing an active program
  (<https://arxiv.org/abs/2606.21522>).

These are not interchangeable finished packets.  None currently supplies all
of D15's state, autonomous-record, join, scale, `3+1`-selection and untouched-
prediction gates in a uniquely empirically selected form.  Agreement on the
same low-energy coefficients would not select between them.

## 9. Provisional D15 theorem

**Low-energy effective rulebook theorem (scope-limited).**  Given the observed
`3+1` Lorentzian field content and gauge representations, locality, quantum
unitarity/gauge consistency and a derivative expansion select the
Einstein–Hilbert plus Standard-Model EFT **operator normal form**.  Independent
experiments identify or bound many of its coefficients.  Regional path
amplitudes from that action can conditionally feed D14 and produce durable
projective histories after a state/environment/coarse-graining record packet
is supplied.

The premises and evidence do not uniquely select all coefficients, a quantum
state, a fundamental record instrument or a UV completion.  They do not
derive `3+1`, round-cone emergence or `G` from sealed dimensionless records.

The provisional verdict is therefore:

```text
LOW-ENERGY-EFFECTIVE-RULEBOOK-IDENTIFIED
+ ACTION-BRIDGE-CONDITIONAL
+ FUNDAMENTAL-UV/RECORD-LAW-NOT-SELECTED.
```

No untouched V9 holdout is opened by this theorem.  D15 must finish the UV
survivor ledger and undergo hostile review before freezing even this narrowed
verdict; the first regulated regional example follows.

## 10. First regulated dictionary result

The first promised regulated example is now executable.  On binary boundary
variables it uses the local phase weight

```math
K_H(b,a)=2^{-1/2} exp(i pi a b)
```

and the local reversible constraint

```math
K_CNOT(b_c,b_t;a_c,a_t)
=delta_{b_c,a_c} delta_{b_t,a_t xor a_c}.
```

Internal boundary summation exactly gives matrix composition.  Two `H`
regions yield constructive amplitude one and destructive amplitude zero;
disjoint regions commute by tensor interchange.  `H` followed by `CNOT`
prepares an exact Bell state with maximally mixed marginals, perfect same-basis
correlation and an exact local no-signalling cell.

Fixing a fresh environment bit to zero and applying the same CNOT interaction
derives the seal `|s>|0> -> |s>|s>`.  Tracing that environment exactly removes
the system's pointer-basis coherence.  Appending a live collar makes the map
fit D14; later system action preserves its record marginal.  CNOT memory
interactions give the finite visible non-Markov carrier.

The standard-library exact receipt passes 28/28 checks in normal and optimized
Python with byte-identical stdout.  It deliberately includes a different
unitary phase-modified action whose fixed-frame closed probability is `1/2`
rather than `1`, proving that the dictionary is not a selector.  The seal is
now composed through the actual D14 `Obj`/`Mor` interface from fresh
environment injection, the CNOT interaction, explicit commit and live-collar
emission; a D14 protected future then composes and preserves its record.

The result closes only a finite nongravitational instance of S4 and a
conditional environment-decoherence instance of S5.  The
environment initial state, system/environment split, interpretation of the
environment bit as a protected record, continuum limit, general covariance,
gravity, dimensions and scales remain supplied or absent.  Formal D15 status
therefore remains `INCOMPLETE-INVESTIGATION` pending hostile review and the UV
audit.

For this witness the regulator is the printed finite binary boundary/history
sum; the gauge group and gauge quotient are trivial; the boundary basis and
vertex normalization are fixed; every D14 port belongs to the single owner
`cell-A`; no cross-component join is exercised; and all action phases are
dimensionless.  Consequently it supplies no metre/second/`G` bridge and is not
a discretization of `EFT4` or gravity.
