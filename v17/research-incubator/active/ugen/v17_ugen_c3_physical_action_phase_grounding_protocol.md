# ISP v17 — U-Gen C3 physical action-phase grounding protocol

**Status:** ACTIVE AUTHOR-SIDE EXPERIMENT DESIGN / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Reality-facing question

C2 showed that a symbol named `T` cannot contain the physical fact
$\theta=\pi/4$. C3 replaces gate names with laboratory referents.

The question is:

> Can one measurable, composition-respecting action character, calibrated
> without a target quantum matrix, predict held-out electromagnetic,
> topological, and gravitational matter-wave phase records from independently
> measured physical controls?

This is a test of cross-domain nomological compression. Passing it would not
derive quantum mechanics or select an ontology. Standard quantum theory is a
zero-explanatory-gain comparator that is already known to pass within its
domains of validity.

No experiment is run and no published data are adjudicated in this author-side
protocol.

---

## 1. Registered referent

The primitive is not a gate, matrix, path amplitude, or abstract phase angle.
It is a complete experimental source contract

$$
\mathcal C_E=(\mathsf{Src},\mathsf{Split},\mathsf{Ctrl},
\mathsf{Geom},\mathsf{Recomb},\mathsf{Read},\mathsf{Met},\mathsf{Prov}).
$$

For each experimental family $E$, the contract must contain:

1. the particle species and preparation procedure;
2. source intensity and independently measured coherence diagnostics;
3. splitter, mirror, interaction, and recombination operations as physical
   apparatus, not named quantum gates;
4. masses, charges, magnetic moments, field histories, source-mass models,
   trajectories, geometry, and timing with uncertainties;
5. every laser, material, electromagnetic, or gravitational interaction
   contributing to the measured port phase;
6. raw output records and the mapping from detector events to registered
   outcomes;
7. calibration data, nuisance parameters, covariance information, and
   exclusion rules; and
8. provenance and version identifiers for every data and apparatus object.

The contract must not contain:

1. the target unitary or density matrix;
2. a table of target phases at held-out settings;
3. a fitted action chosen after seeing held-out records;
4. a per-experiment value of the universal phase scale;
5. a future readout choice inside the source state; or
6. an uncharged simulation that already implements the quantum comparator.

Operational arms are alternatives defined by the apparatus and record model.
C3 does not assert that two localized ontic particles or two actual paths
exist between source and detector.

---

## 2. Raw empirical object

For a control setting $u$, record counts in two output ports for two
independently registered recombiner quadratures:

$$
N_{c,+}(u),N_{c,-}(u),N_{s,+}(u),N_{s,-}(u).
$$

The empirical contrasts are

$$
\widehat C(u)=
\frac{N_{c,+}-N_{c,-}}{N_{c,+}+N_{c,-}},
\qquad
\widehat S(u)=
\frac{N_{s,+}-N_{s,-}}{N_{s,+}+N_{s,-}},
$$

with the complex record coordinate

$$
\widehat Z(u)=\widehat C(u)+i\widehat S(u).
$$

This definition does not presume that $\widehat Z$ is a wavefunction. It
packages four positive record counts. Detector imbalance, background,
visibility, drift, and quadrature miscalibration must be represented by a
registered likelihood, not removed by hand.

If only one quadrature exists in a historical data set, C3 records the
conjugation ambiguity rather than reconstructing an imaginary component.

---

## 3. Physical action and boundary-transport coordinates

The candidate signed propagation coordinate is the classical action
difference

$$
s_E(u)=S_1(u)-S_2(u).
$$

Dimensionless phases supplied by beam splitters, lasers, internal-state
changes, separation mismatch, or the recombiner are not silently added to an
action-valued scalar. They form a separately typed, independently calibrated
boundary transport

$$
\beta_E(u)\in U(1).
$$

The scalar-character prediction is therefore

$$
R_E(u)=\beta_E(u)e^{i\kappa s_E(u)}.
$$

Choose the reference setting so that $s_E(0)=0$ and fix the harmless boundary
gauge $\beta_E(0)=1$. All later ratios are relative to this registered
reference.

Only when an interaction-boundary contribution has an independently derived
action-valued representative may it be folded into $s_E$. Otherwise it remains
in $\beta_E$ and is charged as apparatus input. Supplying the held-out answer
through $\beta_E$ is disallowed.

For a nonrelativistic particle in supplied electromagnetic and weak
gravitational potentials, the propagation action uses

$$
L=\frac12m\dot x^2
+qA(x,t)\cdot\dot x
-q\phi(x,t)
-m\Phi_g(x,t).
$$

The full phase of a light-pulse atom interferometer is not generally just the
potential integral. Laser phase, recoil, pulse timing, separation phase, and
the self-consistent arm trajectories must be included in the correctly typed
pair $(s_E,\beta_E)$. C3 forbids the common shortcut of comparing a measured
atom-interferometer phase to $-m\int\Delta\Phi_gdt$ when the apparatus supplies
additional terms.

For a closed electromagnetic comparison,

$$
s_{\rm AB}=q\oint A\cdot dx=q\Phi_B
$$

is gauge invariant modulo the relevant flux sector. For gravity in the weak
nonrelativistic regime,

$$
s_g=-m\int\left[\Phi_g(x_1,t)-\Phi_g(x_2,t)\right]dt
$$

is only one term in the complete interferometer action ledger.

Every construction of $(s_E,\beta_E)$ receives an uncertainty distribution
and an input-origin label:

```text
DIRECT CLASSICAL METROLOGY
INDEPENDENT QUANTUM CALIBRATION
THEORY-DEPENDENT INFERENCE
APPARATUS SIMULATION
CONVENTION / GAUGE
```

No coordinate is called pre-quantum merely because it is written as a
classical action.

---

## 4. Phase-scale policy

The candidate character is

$$
\chi_\kappa(s)=e^{i\kappa s}.
$$

C3 permits two honest scale tracks.

### M0 — declared empirical constant

Declare

$$
\kappa=1/\hbar
$$

as established external physics. This tests only the transport and action
ledger. It earns no derivation of Planck's constant.

### M1 — one calibration, then lock

Estimate one $\kappa_{\rm cal}$ from a signed continuous non-gravitational
matter-wave phase scan. Freeze its uncertainty before opening any held-out
electromagnetic, topological, or gravitational records.

In the revised SI, the numerical values of $h$ and $e$ define units exactly.
Therefore a modern SI-valued regression cannot be advertised as an
independent measurement of their universality. M1 must print the complete
metrological dependency graph or use dimensionless ratios in which the unit
definitions cancel.

No domain-specific refit

$$
\kappa_{\rm kin},\quad\kappa_{\rm EM},\quad\kappa_{\rm top},\quad
\kappa_g
$$

is permitted on the common-character branch.

---

## 5. Calibration family C0 — signed dynamical phase

Use a two-alternative matter-wave interferometer with one arm exposed to a
controlled, independently characterized non-gravitational interaction. The
registered control must produce both positive and negative signed action
differences around zero.

Admissible implementations include:

1. a calibrated magnetic interaction of a neutron or neutral atom with
   independently measured magnetic moment, field, and transit time;
2. a controlled material or optical potential with a separately audited
   coupling model; or
3. a force-balanced scalar-potential protocol whose residual deflection is
   measured independently.

The implementation must provide:

1. at least one open interval of action settings rather than a single phase;
2. both recombiner quadratures or an explicit sign ambiguity;
3. reversal and zero-interaction controls;
4. an independent visibility model; and
5. a blind calibration/validation split.

Fit only:

$$
(\kappa,\delta_0,V_0,\eta_0),
$$

where $\eta_0$ is a preregistered nuisance vector that includes only the
calibration-limited boundary transport. No held-out apparatus parameter may
be absorbed into $\eta_0$.

---

## 6. Held-out H1 — composition within one apparatus

Before moving across interactions, test the character premise itself.

Prepare two independently controlled segments with signed actions $s_1$ and
$s_2$. Compare:

1. segment 1 alone;
2. segment 2 alone;
3. their typed sequential concatenation; and
4. one unsplit segment with total action $s_1+s_2$.

After dividing out the independently registered boundary transports, define

$$
Y_E(u)=
\frac{Z_E(u)Z_E(0)^*}{|Z_E(u)Z_E(0)|}\,\beta_E(u)^{-1}.
$$

The held-out prediction is

$$
Y_E(s_1+s_2)=Y_E(s_1)Y_E(s_2).
$$

Failures may indicate seam memory, uncontrolled boundary phases, loss of
coherence, or failure of the scalar-character model. C3 must not immediately
interpret them as a violation of quantum mechanics.

---

## 7. Held-out H2 — shielded electromagnetic holonomy

Use an electron-interference configuration in which two coherent alternatives
enclose magnetic flux while the electron-accessible region is shielded from
the magnetic field, following the physical logic of the Tonomura toroidal
magnet experiments.

After the independently measured common apparatus transport is removed, the
registered prediction is

$$
\frac{Z(\Phi_B)}{Z(0)}
=e^{i\kappa q\Phi_B},
$$

with no refit of $\kappa$.

Mandatory controls:

1. flux reversal;
2. loop-orientation reversal;
3. zero-flux and leakage bounds;
4. shielding and inaccessible-field audit;
5. electron-energy and path-geometry variation;
6. apparatus phase drift; and
7. the flux-sector and superconducting quantization dependencies.

This held-out family is essential because a purely local-force trajectory
model can fit ordinary dynamical phases while missing closed-loop holonomy.

---

## 8. Held-out H3 — gravity-sensitive matter-wave phase

C3 registers two gravity controls with different discriminatory content.

### H3a — Earth-field neutron interference

Use the Colella--Overhauser--Werner neutron-interferometer geometry with its
complete crystal, wavelength, area, orientation, and systematic-error model.
Predict the gravitational phase from the locked $\kappa$ and the complete
action ledger. Do not replace the source analysis by a remembered textbook
formula.

This tests matter-wave response to a classical external gravitational field.
It does not test whether gravity is quantized.

### H3b — source-mass gravitational Aharonov--Bohm regime

Use a spatially separated atom interferometer near a kilogram-scale source
mass, with arm deflections measured independently. The complete prediction
must include midpoint/laser contributions and the potential-sensitive term,
with action-valued propagation and dimensionless boundary transport kept
distinct.

The discriminatory question is whether the observed phase contains the
registered potential-difference contribution beyond that inferable from arm
deflections alone.

Passing H3b rejects a deflection-only mutant within the experiment's scope.
It still does not establish a quantum gravitational field, because the source
mass and potential may remain classical.

---

## 9. Cross-species universality

C0, H2, H3a, and H3b involve different particles and apparatus. A common
$\kappa$ is therefore a strong compression only if all species-specific
inputs are charged:

$$
(m,q,\mu,\alpha_{\rm pol},\text{scattering data},\text{laser coupling},
\text{source potential}).
$$

The protocol distinguishes:

1. **phase-scale universality:** one $\kappa$;
2. **coupling universality:** one rule for inserting kinetic, EM, and
   gravitational contributions into total action;
3. **equivalence-principle content:** inertial and gravitational mass
   relations; and
4. **apparatus universality:** one readout/composition law across distinct
   interferometers.

Agreement on item 1 does not prove items 2--4.

---

## 10. Candidate comparison table

| candidate | supplied input | obligation | explanatory score |
|---|---|---|---|
| Q0 standard quantum action | full action/Hamiltonian, $\hbar$, boundary state, measurement model | reproduce all records | zero-gain control |
| A1 scalar action character | physical source contract, total action, one $\kappa$, weight/readout law | predict C0/H1/H2/H3 without refit | partial compression only |
| A2 relational pair-history generator | physical source contract and native rule for weights plus correlations | derive $D$ and records across families | live native slot |
| P1 ordinary-positive indivisible generator | same physical controls, no target process table | predict complete record laws uniformly | live if constructed |
| L0 local-force mutant | trajectories and local forces only | fit C0 but not shielded/potential-only effects | hostile control |
| T0 per-family table | target phase response for each family | interpolate records | disallowed laundering |

A1 is not a complete theory because it receives the total action and does not
provide the diagonal weights, record algebra, or actuality rule.

---

## 11. Statistical comparison

A future freeze must bind raw-data versions and a likelihood. At minimum:

1. detector counts are modeled as binomial, multinomial, or an explicitly
   justified overdispersed process;
2. action-coordinate uncertainties enter through a joint errors-in-variables
   model;
3. drift, visibility, background, and quadrature calibration are nuisance
   parameters learned only from registered calibration channels;
4. H2 and H3 predictions are posterior- or confidence-predictive, not refit;
5. residuals are evaluated on $U(1)$ rather than by unwrapped phase after an
   arbitrary branch choice; and
6. model complexity and per-family advice are charged.

### Historical-versus-prospective wall

C0, Tonomura, COW, and the published source-mass experiment are established
physics known to candidate designers. Calling them “held out” means only that
their records and family-specific parameters are not used to fit $\kappa$ or
alter the law after freeze. It does not make them discovery-blind evidence for
a newly invented theory.

An empirical-wedge claim requires a later prospective layer:

1. a frozen candidate prediction for a new apparatus configuration or control
   range;
2. concealed outcome data or data acquired after the prediction;
3. an independently fixed analysis pipeline; and
4. independent replication.

Historical cross-validation can establish source adequacy and compression. It
cannot by itself establish novel predictive success.

A natural invariant residual for nonzero contrasts is

$$
r_E(u)=
d_{U(1)}\left(
\frac{Z_E(u)Z_E(0)^*}{|Z_E(u)Z_E(0)|},
\beta_E(u)e^{i\kappa s_E(u)}
\right).
$$

No numerical pass threshold is set here. It must be fixed from source
uncertainties before opening held-out records.

---

## 12. Preregistered mutants

1. separate $\kappa$ for every interaction;
2. separate $\kappa$ for every species;
3. nonlinear $e^{i[\kappa s+g_E(s)]}$ fitted after inspection;
4. finite-grid interpolator;
5. local-force-only model;
6. endpoint-only stochastic matrix;
7. future-setting or answer table in the source state;
8. target quantum matrix in the apparatus description;
9. missing laser or separation phase;
10. field leakage disguised as topology;
11. deflection-only gravity model;
12. source-mass potential fitted from the interference phase itself;
13. visibility loss treated as phase deviation;
14. decoherence treated as actualization;
15. complex-conjugate convention called a new member;
16. modern SI definitions treated as a fresh measurement of $h$ or $e$;
17. classical-wave interference promoted to single-event ontology;
18. standard quantum compiler reported as native explanatory gain;
19. uncharged numerical simulator;
20. gravitational phase reported as quantized gravity.

---

## 13. Outcome ladder

```text
C3-O0  SOURCE CONTRACT ILL-TYPED
       The action coordinate or physical apparatus cannot be reconstructed
       independently of the target prediction.

C3-O1  CHARACTER PREMISE FAILS IN CALIBRATION/COMPOSITION
       One scalar additive action coordinate is insufficient or seam data
       remain uncontrolled.

C3-O2  CALIBRATED CHARACTER / TOPOLOGY FAILURE
       C0 and H1 pass; shielded H2 fails.

C3-O3  NON-GRAVITY PASS / GRAVITY FAILURE
       C0, H1, and H2 pass; one or both H3 controls fail.

C3-O4  STANDARD ACTION UNIVERSALITY REPRODUCED
       One locked character and complete standard action ledger predict the
       registered held-outs; no native ontology or generator is selected.

C3-O5  NATIVE GENERATOR REDUCES AN INPUT
       A candidate predicts the same profiles while deriving at least one
       action, weight, composition, boundary, or record coordinate that Q0
       receives as input.

C3-O6  REPRODUCIBLE PROSPECTIVE EMPIRICAL DEVIATION
       A frozen candidate predicts and survives a deviation from the standard
       comparator. Independent experiment is then required.
```

Every outcome is conditional on the registered experimental families. C3-O4
is the expected established-physics outcome and is not advertised as a new
discovery.

---

## 14. What this packet can unblock

If C3-O4 is established under independent review, C1 Track A can be repaired
semantically:

1. A0 remains the endpoint-only nonselection theorem;
2. A1 becomes a physically typed action-character source interface; and
3. Q0 remains the complete standard-quantum zero-gain control.

This would make a later U-Gen contest fair. It would not fill the native
candidate slot.

C3 does not directly unblock Q-Cut, Paper 04B, chronology, spacetime, or
gravity. It improves the physical input contract for the generator search.

---

## 15. Authority wall

This protocol does not authorize:

1. acquisition or reinterpretation of experimental data;
2. an official pin or source freeze;
3. independent reviewers;
4. a scientific result;
5. a repair cycle;
6. a native U-Gen candidate;
7. Paper 05 or a clock successor;
8. chronology, spacetime, or gravity construction; or
9. publication or external communication.

It is an author-side specification of the next physical grounding problem.
