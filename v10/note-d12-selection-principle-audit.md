# D12 selector audit — what can and cannot choose the interaction

**Status:** completed after the frozen countermodels and exact symmetric-family
test, before restored implementation or hostile review, 2026-07-11.

## 1. The logical test

A proposed selector `Q` derives a unique law only if the frozen SHARD premises
plus `Q` have exactly one physical equivalence class of models.  It is not
enough that `Q`:

- writes a supplied law in elegant coordinates;
- chooses a coefficient after its support, reference measure, modes, and
  constraints have been supplied;
- fits observations also used to invent the selector;
- selects one member of a preselected toy family;
- or produces favorable V9 geometry.

The two exact D12 witnesses are deliberately complementary:

1. `P_r(x,y,z)=(1+rxyz)/8` gives positive projective whole-history laws with
   the same one- and two-record shadows and different continuations;
2. partial-iSWAP at `theta=pi/4` and iSWAP at `theta=pi/2` have the same local
   record architecture, unitarity, exchange symmetry, excitation conservation,
   entangling capacity, evidence law, continuation, and disjoint construction
   gauge, but predict a later record with probability `1/2` and `0`.

Therefore any successful selector must distinguish either `r` or `theta` by
new physical information.

## 2. Selector-by-selector adjudication

| proposed principle | what it genuinely fixes | why it does not select the D12 law |
|---|---|---|
| probability normalization/projectivity | consistent cylinder probabilities | both whole-history twins pass |
| Barandes indivisibility / proposed stochastic-quantum correspondence | proposes Hilbert representations for a class of supplied indivisible probability dynamics, with the path-measure interpretation contested | even granting the proposal, supplied dynamics is input; Egri et al. show probability dynamics does not uniquely fix probability on trajectories |
| Born rule/decoherence | probability readout from a supplied state, process, and instrument | both unitaries use the same Born rule and differ because the process differs |
| sealed RN evidence `S(I)=exp(-I)` | intrinsic survival coordinate once the evidence process exists | both packets use the same survival law; it does not choose their interaction |
| V6 commitment fixed point | one coefficient vector for one fixed support/reference/basis/orientation | changing the interaction, support, or reference changes the variational problem |
| locality/causal ownership | which legs may interact | permits a continuum of local operators on the same connected collar |
| Lorentz/gauge covariance | transformation law and allowed tensor/operator structures | invariant operators still carry masses, couplings, mixing angles, and initial data |
| exchange symmetry and conservation | commutant/subalgebra of allowed interactions | the exact iSWAP family lies inside the same commutant for every angle |
| unitarity, analyticity, crossing | admissible scattering region | modern bootstrap work maps an allowed space and only sometimes isolates special boundary points |
| least/stationary action | equations of motion for a **supplied** action and boundary conditions | `theta=J tau`; variation does not determine the coupling `J`, duration/evidence conversion `tau`, field content, or action functional |
| maximum entropy/caliber | least-committal law relative to a supplied base measure and supplied constraints | with only uniform one-record marginals it selects the independent law, not an observed interaction; adding correlation constraints imports the missing physics |
| renormalization/fixed point | flow once theory space, coarse graining, and beta functions are supplied | multiple fixed points and relevant directions occur; RG does not create the microscopic theory space or select its trajectory |
| anomaly/consistency cancellation | removes inconsistent field/charge combinations | leaves empirically measured couplings, masses, mixings, vacuum data, and often multiple consistent theories |
| simplicity/MDL | shortest description in a supplied language and prior | changes under recoding and has no record-intrinsic universal language in the corpus |
| favorable round cone or 4D proxy | downstream phenomenological filter | cannot be used to derive the law after the geometry result is known; it is at best an independent holdout observation |
| profinite completion | existence of a measure from a compatible cylinder family | hosts every compatible `P_r`; inverse limits preserve a law but do not choose it |

## 3. Exact maximum-entropy refusal

For two binary records with uniform marginals, every exchange-symmetric
correlation family can be written

```math
p_r(x,y)={1+rxy\over4},\qquad -1<r<1.
```

Its Shannon entropy satisfies

```math
H'(r)={1\over2}\log{1-r\over1+r},
\qquad
H''(r)=-{1\over1-r^2}<0.
```

Hence unconstrained maximum entropy uniquely selects `r=0`: independence.
To select a nonzero interaction one must supply a correlation, energy, flux,
or other constraint, together with its numerical value.  Maximum caliber then
repackages that supplied information into exponential-family multipliers.  It
does not derive the missing interaction.

This is exactly the status of the V6 log-RN exponential family: completeness
and convexity make inference or identification well posed after the physical
statistics are chosen; they do not choose the statistics.

## 4. Exact action/coupling refusal

Let `X_ex` exchange `|01>` and `|10>` and vanish on `|00>,|11>`.  The whole
family

```math
U_theta=exp(i theta X_ex)
```

is unitary, exchange symmetric, excitation preserving, local to the same
owned two-leg diamond, and compatible with the same seal-and-birth record
instrument.  A stationary-action presentation is obtained from

```math
H_J=-J X_ex,\qquad theta=J tau/hbar.
```

The variational principle determines evolution **conditional on** `H_J`; it
does not fix `J`, `tau`, or the evidence-to-proper-time bridge.  The two exact
D12 members prove that this freedom changes a durable record probability.

More generally, for any strictly positive finite classical history law `P`
and reference `mu`, the function

```math
A_P(omega)=-log(P(omega)/mu(omega))
```

gives `P(omega) proportional to mu(omega) exp(-A_P(omega))`.  Thus “there is an
action” is a representation theorem, not a selector, until the action is
independently fixed.  The same point holds for finite-dimensional unitary
evolution: a unitary admits Hamiltonian logarithms, but that does not choose
the unitary.

## 5. Literature checks and priority boundary

- Barandes's [stochastic-quantum correspondence](https://arxiv.org/abs/2302.10778)
  proposes a broad correspondence between supplied stochastic dynamics and
  quantum representations; his later
  [indivisible-process paper](https://arxiv.org/abs/2507.21192) treats
  indivisible stochastic laws as the dynamics.  This bridge is contested.
  [Egri et al.](https://arxiv.org/abs/2602.23491) distinguish a trajectory of
  instantaneous probabilities from a probability measure on trajectories,
  prove generic nonuniqueness of implementations, and directly criticize
  stochastic-quantum correspondence claims.  D12 relies only on a supplied
  probability **on histories**, not on reconstructing one from instantaneous
  probability dynamics, and takes no position on the broader dispute.
- Quantum combs give an axiomatic/constructive representation of admissible
  multi-time networks and memory channels
  ([Chiribella, D'Ariano, Perinotti](https://arxiv.org/abs/0904.4483)).  Process
  tensors give operational tests and tomography for general non-Markovian
  dynamics ([Pollock et al.](https://arxiv.org/abs/1801.09811)).  These are
  complete process containers/identifiers, not unique process generators.
- Jaynes described maximum entropy as the least-biased estimate **on given
  information**, not a replacement for physical law
  ([Physical Review 106, 620](https://journals.aps.org/pr/abstract/10.1103/PhysRev.106.620)).
- The modern [S-matrix bootstrap white paper](https://arxiv.org/abs/2203.02421)
  describes an infinite-dimensional allowed space under symmetry, crossing,
  unitarity, and analyticity, with special theories sometimes appearing at
  distinguished points.  This is strong evidence against treating consistency
  conditions alone as a generally unique dynamical selector.
- Explicit four-dimensional gauge theories can possess one or several
  interacting fixed points
  ([Bond and Litim](https://arxiv.org/abs/1707.04217)); RG therefore cannot be
  invoked as a universal one-point selector without extra theory-space data.
- The Particle Data Group treats interaction strengths, masses, and mixing
  quantities as parameters determined from observations; for example its
  [electroweak review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf)
  and [quark-mass review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-quark-masses.pdf)
  report measured inputs rather than deductions from quantum kinematics.

The D12 logical no-go and its exact SHARD countermodels are corpus-specific.
The broader distinction between kinematics/probability calculus and supplied
dynamics is standard; no priority claim is made for it.

## 6. The maximal theorem

Under the V6–V10 frozen principles, the universal result is not a unique
numerical interaction.  It is this conditional form:

```text
typed local sealed-diamond grammar
+ compatible whole-history quantum/classical process measure
+ local durable-record instruments
=> conditional next-record probabilities by disintegration.
```

The process measure can equivalently be specified by an initial condition plus
a local action/Hamiltonian/process tensor when such a representation exists.
Its field content, couplings, state, and record/decoherence instrument are
additional physical data.  They are not derivable from sealed-record
kinematics, the exponential evidence clock, construction-order gauge,
profinite consistency, or the complex rank-two cone.

## 7. Decision

No audited selector rejects all but one exact survivor without importing new
physical information.  The correct D12 verdict at this gate is:

```text
UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS.
```

This is a proof of underdetermination relative to the stated SHARD/ISP
principles, not a metaphysical proof that no future empirical principle can
deepen physics.  Any such future principle must discriminate the exact
countermodels and make an independent prediction.
