# Operational Observable Reconstruction From Relativistic ISP Kernels

Author: Felix Robles Elvira

V2 Paper 4 investigation

Date: 2026-05-13

## Purpose

Paper 3 exports algebraic locality:

```math
J_R=\Gamma_R\Gamma_0^{-1},
\qquad
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1},
```

with anchored inverse, exchange-corridor, sectorwise, and projective-transfer
bounds in the common-collar class. It explicitly does not export observables.

Paper 4 asks the next first-principles question:

> Which operational instruments and observable effects are selected by the
> stochastic endpoint-kernel data, and which must be supplied as additional
> physical structure?

The goal is not to rename raw comparison maps as observables. The goal is to
build or refute a bridge from raw finite endpoint dynamics to operational
measurement theory.

This is also where the ISP measurement-problem claim has to become precise.
The slogan "ISP solves the measurement problem" should mean the following
scoped thesis:

> The primitive ontology is not a unitarily evolving wavefunction that must
> somehow collapse. It is a stochastic endpoint-record dynamics on finite
> configuration spaces. A measurement is a localized stochastic instrument that
> writes a definite record. Selective update is ordinary conditioning on that
> record, not a second physical collapse law.

Paper 4 must use this idea fully, but honestly. ISP can dissolve the
measurement problem only if it proves that realistic detector/readout
procedures can be represented as positive normalized instruments with stable
record sectors, and that the resulting probabilities recover the quantum
interference phenomena that standard QFT already gets right.

Thus Paper 4 is not just "observable reconstruction." It is the finite
operational measurement theory of ISP.

## Measurement-Problem Thesis

The standard measurement problem comes from trying to hold three claims at
once:

1. microscopic dynamics is universally unitary;
2. macroscopic experiments have definite single outcomes;
3. the Born rule gives the observed frequencies.

ISP changes the starting ontology. The primitive object for prediction is a
stochastic transition between finite configuration/record spaces:

```math
p_{\mathrm{out}}=\Gamma p_{\mathrm{in}},
\qquad
\Gamma V_+\subseteq V_+,
\qquad
1^T\Gamma=1^T.
```

There is no extra collapse postulate at this level. A detector outcome is a
configuration record, represented by disjoint record sectors

```math
D_R=\bigsqcup_o D_{R,o}.
```

The probability of outcome `o` is the mass assigned to the corresponding
record sector. If `\mathsf I_{R,o}` is the operation that both couples the
detector and conditions on record `o`, then

```math
\Pr(o|p)=1^T\mathsf I_{R,o}p.
```

After observing `o`, the selective state update is

```math
p\mapsto
p_o
:=
\frac{\mathsf I_{R,o}p}{1^T\mathsf I_{R,o}p},
```

which is just Bayesian conditioning on a definite record. The nonselective
state is

```math
p\mapsto
\sum_o\mathsf I_{R,o}p.
```

The measurement problem is therefore not solved by declaring raw `J_R` to be
an observable. It is addressed by making records, instruments, and conditioning
primitive and positive, then proving that this operational layer is local,
projectively stable, and quantum-compatible.

The remaining hard issue is the **interference problem**: a primitive
Born-squared endpoint kernel can hide phase information. ISP must recover
phase-sensitive phenomena through a sufficiently rich family of controlled
kernels and detector couplings. If it cannot, the measurement problem may be
cleanly dissolved at the stochastic-record level while QFT reconstruction still
fails.

## Ontology Ladder

The clean ontology should have separate levels.

1. **Configuration level.** A finite hypersurface regulator has a configuration
   set `C_a` and a real ordered vector space

```math
V_a=\mathbb R^{C_a},
\qquad
V_{a,+}=\{p:p_c\ge0\}.
```

States are normalized positive vectors:

```math
1^Tp=1.
```

Effects are positive functionals:

```math
0\le e\le 1.
```

2. **Primitive dynamics.** A primitive endpoint kernel is a stochastic map

```math
\Gamma:V_{\Sigma_0,a}\to V_{\Sigma_1,a},
\qquad
\Gamma V_+\subseteq V_+,
\qquad
1^T\Gamma=1^T.
```

3. **Raw relative dynamics.** A comparison map is

```math
J_R=\Gamma_R\Gamma_0^{-1}.
```

It preserves column sums when defined, but it need not preserve positivity.
Thus it is a pseudo-stochastic relative-dynamics map, not an effect and not an
instrument.

4. **Raw exchange curvature.** The exchange defect

```math
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}
```

is an algebraic curvature of relative dynamics. Paper 3 controls its support
and tails. It is not automatically a directly measurable operation.

5. **Operational instruments.** A real measurement procedure is a finite family
of positive sub-stochastic maps

```math
\mathsf I_{R,o}:V_{\Sigma_0,a}\to V_{\Sigma_1,a},
\qquad
\mathsf I_{R,o}V_+\subseteq V_+,
\qquad
\sum_o1^T\mathsf I_{R,o}=1^T.
```

Outcome probabilities are

```math
\Pr(o|p)=1^T\mathsf I_{R,o}p.
```

The summed map

```math
\mathsf I_R:=\sum_o\mathsf I_{R,o}
```

is the nonselective operational channel.

For a genuine measurement, not merely a generic operation, the detector output
space should contain record sectors `D_{R,o}` and the instrument should write
one of them. Definite outcomes are mutually exclusive record sectors in
configuration space, not eigenvalue labels added after the fact.

6. **Observables.** An observable is an equivalence class of instruments or
effects that give the same outcome probabilities on the declared preparation
class. In finite stochastic form, the associated effect is

```math
e_{R,o}^T:=1^T\mathsf I_{R,o}.
```

7. **Operational local net.** A local operational algebra/net is generated by
localized instruments and effects, not by raw `J_R` matrices alone.

This ladder is the main discipline of Paper 4. The temptation to collapse
levels 3 and 5 is exactly the mistake Paper 3 warned against.

## Einstein-Style First Principle

Start from coincidences and records, not from hidden mathematical furniture.

A local observable is not "whatever matrix is supported near `R`." It is a
repeatable localized procedure that turns preparations into outcome
frequencies and has a controlled transformation law under refinement and
changes of hypersurface description.

In this sense, the operational primitive is:

```math
(\text{preparation},\ \text{localized instrument},\ \text{readout})
\longmapsto
\text{probability}.
```

Everything else must justify itself by preserving or predicting these
probabilities.

## Paper 3 Export To Use

Paper 4 may use, under the hypotheses of Paper 3:

1. `J_R-I` and `J_R^{-1}-I` are anchored quasilocal relative maps;
2. `E_{R,S}-I` has a two-anchor corridor/window bound;
3. separated collars have a coefficient onset bound;
4. sectorwise versions hold for invariant common-collar fibers;
5. projective refinement transfer holds only after reference-renormalized
   residuals are controlled.

Paper 4 may not assume:

1. `J_R` or `E_{R,S}` are positive;
2. `J_R` or `E_{R,S}` are effects, instruments, or observables;
3. raw exchange curvature is automatically measurable;
4. a Haag-Kastler net already exists;
5. QFT reconstruction follows from finite-kernel locality alone.

## Core Problem

The raw data underdetermine operational physics unless one specifies how
detectors couple.

Two different microscopic Hilbert/circuit descriptions can have the same
endpoint transition matrix

```math
\Gamma=|U|^2
```

but different phase-sensitive interference behavior. Therefore Paper 4 has to
decide whether operational instruments can be reconstructed from a family of
kernel data alone, or whether extra phase/circuit/detector structure must be
declared primitive.

This is the central possible no-go:

> Born-squared endpoint kernels may be too coarse to reconstruct all local QFT
> observables without extra operational data.

The positive route is narrower:

> A sufficiently rich family of controlled kernels, localized detector
> ancillas, and readout effects may reconstruct an operational local net even
> though a single primitive `\Gamma` cannot.

## Simple Scenarios Paper 4 Should Include

These are not decorative examples. They are pressure tests for the ontology.

### Scenario 1: Pointer Record Without Collapse

Let a two-outcome detector have three coarse sectors:

```math
D_R=D_{\mathrm{ready}}\sqcup D_+\sqcup D_-.
```

A measurement coupling maps

```math
p\otimes\eta_{\mathrm{ready}}
\longmapsto
\widehat p_+ + \widehat p_-,
\qquad
\mathrm{supp}(\widehat p_\pm)\subseteq
V_{\Sigma_1,a}\otimes D_\pm.
```

The observed outcome is not an eigenvalue floating above the dynamics. It is
membership in `D_+` or `D_-`. The selective update is ordinary conditioning on
that membership. The nonselective state is the sum. This is the finite ISP
replacement for collapse.

The theorem burden is clear: prove positivity, normalization, and record
stability under repeat readout. Do not say "macroscopic" unless the finite
model contains stable record sectors or an explicit coarse-graining limit.

### Scenario 2: Two-Path Interferometer

A minimal phase benchmark is a two-path system with a controllable phase:

```math
U_\phi
=
B
\begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix}
B,
\qquad
B=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
```

For input path `0`,

```math
\Pr_\phi(0|0)=\cos^2(\phi/2),
\qquad
\Pr_\phi(1|0)=\sin^2(\phi/2).
```

A which-path detector that writes a stable record between the two beam
splitters removes the interference term and gives the incoherent statistics
instead. ISP must be able to describe both operations:

1. a coherent controlled-kernel family `\Gamma_\phi=|U_\phi|^2`;
2. a detector-coupled record kernel `\Gamma_{\mathrm{wp},D}`;
3. the transition between interference and which-path statistics by adding or
   deleting the record-writing coupling.

This example forces the key distinction. The measurement problem is addressed
by records and conditioning, but QFT compatibility requires recovering
phase-sensitive control families. A single endpoint kernel is not enough.

### Scenario 3: Two Separated Detectors

Let `R` and `S` be two spacelike-separated detector collars. Paper 3 provides a
raw corridor estimate for `E_{R,S}-I`. Paper 4 must ask whether there exist
realizable detector instruments whose calibrated responses see that defect.

The directly testable statistic is not `E_{R,S}` itself, but an order
difference in outcome frequencies:

```math
\Delta_{R,S}(e,p)
:=
e^T
\left(
\mathscr J_R\mathscr J_S-\mathscr J_S\mathscr J_R
\right)
\Gamma_0p.
```

If this quantity is operationally meaningful, Paper 3 predicts its corridor
tail. If no positive realizable instruments approximate the calibrated raw
maps, then raw exchange curvature remains a structural diagnostic rather than
an experimental signature.

## Candidate Definition: Realizable Local Instrument

An instrument localized near `R` is **realizable** at regulator `a` if there is:

1. a finite detector configuration space `D_R`;
2. an initialized detector state `\eta_R\in\mathbb R_+^{D_R}`;
3. a record-sector partition

```math
D_R=\bigsqcup_oD_{R,o},
\qquad
\Pi_o:\mathbb R^{D_R}\to\mathbb R^{D_R},
```

where `\Pi_o` is the positive coordinate projection onto `D_{R,o}` and
`\sum_o\Pi_o=I_{D_R}`;
4. an enlarged local endpoint kernel

```math
\Gamma_{R,D}:V_{\Sigma_0,a}\otimes D_R
\to
V_{\Sigma_1,a}\otimes D_R;
```

5. detector readout effects `\chi_o=1_{D_R}^T\Pi_o`, so the readout is the
   mass in the record sector;
6. a localized coupling condition: outside the collar, the enlarged dynamics
   agrees with the reference dynamics in the same anchored topology used in
   Paper 3.

The record-retaining operation is

```math
\widehat{\mathsf I}_{R,o}p
:=
\left(\mathrm{id}\otimes\Pi_o\right)
\Gamma_{R,D}(p\otimes\eta_R)
\in
V_{\Sigma_1,a}\otimes\mathbb R^{D_R}.
```

The system-only operation is the detector marginal

```math
\mathsf I_{R,o}p
:=
\left(\mathrm{id}\otimes1_{D_R}^T\right)
\widehat{\mathsf I}_{R,o}p.
```

The outcome probability is

```math
\Pr(o|p)=1_{\Sigma_1}^T\mathsf I_{R,o}p
=
\left(1_{\Sigma_1}^T\otimes1_{D_R}^T\right)
\widehat{\mathsf I}_{R,o}p.
```

If `\Gamma_{R,D}` is stochastic, the `\widehat{\mathsf I}_{R,o}` are positive
sub-stochastic record operations and the `\mathsf I_{R,o}` are positive
sub-stochastic system instruments.

This definition is deliberately operational. It does not require a Hilbert
operator algebra as primitive, but it allows one when a benchmark supplies it.
The important point is ontological: the definite outcome lives in the
record-retaining object `\widehat{\mathsf I}_{R,o}`. The marginal
`\mathsf I_{R,o}` is what remains after the apparatus record has been ignored.

## Candidate Definition: Calibrated Relative Response

Given a realizable instrument and a reference channel `\Gamma_0`, define a raw
calibrated response only when the reference inverse is controlled:

```math
\mathscr J_{R,o}:=\mathsf I_{R,o}\Gamma_0^{-1}.
```

This object may be pseudo-stochastic. It is not the instrument; it is the
instrument after reference calibration. Paper 3 locality theorems apply to
objects of this relative type, not automatically to the positive instrument
itself.

The operational statistic remains

```math
\Pr(o|p)=1^T\mathsf I_{R,o}p
=
1^T\mathscr J_{R,o}\Gamma_0p.
```

This distinction may become the main conceptual hinge of Paper 4.

## Theorem Targets

### Theorem A0: Definite-Record Instrument Theorem

Let a localized detector have disjoint record sectors

```math
D_R=\bigsqcup_oD_{R,o},
```

initialized in a ready sector `D_{R,\mathrm{ready}}`. Suppose the enlarged
kernel `\Gamma_{R,D}` is stochastic and the readout projections `\Pi_o` are the
coordinate projections onto the record sectors. Then the record-retaining maps

```math
\widehat{\mathsf I}_{R,o}p
:=
\left(\mathrm{id}\otimes\Pi_o\right)
\Gamma_{R,D}(p\otimes\eta_R)
```

are positive, mutually exclusive, and exhaustive. Their system marginals

```math
\mathsf I_{R,o}p
:=
\left(\mathrm{id}\otimes1_{D_R}^T\right)
\widehat{\mathsf I}_{R,o}p
```

form a positive normalized instrument:

```math
\mathsf I_{R,o}V_+\subseteq V_+,
\qquad
\sum_o1_{\Sigma_1}^T\mathsf I_{R,o}=1_{\Sigma_0}^T.
```

The proof should be finite-dimensional and explicit:

```math
\sum_o
\left(1_{\Sigma_1}^T\otimes1_{D_R}^T\right)
\widehat{\mathsf I}_{R,o}
=
\left(1_{\Sigma_1}^T\otimes1_{D_R}^T\right)
\Gamma_{R,D}(\,\cdot\,\otimes\eta_R)
=
1_{\Sigma_0}^T,
```

using `\sum_o\Pi_o=I_{D_R}`, `1_{D_R}^T\eta_R=1`, and stochasticity of
`\Gamma_{R,D}`.

Conditioning on the observed record gives the full selective record state

```math
\widehat p_o=
\frac{\widehat{\mathsf I}_{R,o}p}
{\left(1_{\Sigma_1}^T\otimes1_{D_R}^T\right)
\widehat{\mathsf I}_{R,o}p},
```

and the compressed selective system state

```math
p_o=
\frac{\mathsf I_{R,o}p}
{1_{\Sigma_1}^T\mathsf I_{R,o}p},
```

and no additional collapse map is postulated.

If the record sectors are stable under immediate repeat readout, then the
record-retaining state has repeat statistics

```math
\Pr(o'\mid o)=\delta_{o'o}
```

exactly. With leakage

```math
\epsilon_o:=
\left(1_{\Sigma_1}^T\otimes1_{D_R\setminus D_{R,o}}^T\right)
\widehat p_o,
```

the repeat-readout error is bounded by `\epsilon_o`. This is the ISP version
of a repeatable macroscopic record.

### Theorem A: Realizable-Instrument Positivity

If a localized detector coupling is represented by a stochastic enlarged kernel
and positive readout effects, then the induced maps `\mathsf I_{R,o}` are
positive sub-stochastic instruments and their effects satisfy

```math
0\le e_{R,o}\le1,
\qquad
\sum_o e_{R,o}=1.
```

This is simple but essential. It prevents raw pseudo-stochastic maps from
masquerading as observables.

### Theorem B: Locality Transfer From Raw Relative Bounds To Instruments

Suppose a realizable instrument admits a calibrated decomposition

```math
\mathscr J_{R,o}-\mathscr J_{R,o}^{(0)}
\in
\mathcal A_{\mu,R}^{\mathrm{tree}}
```

with the same anchored bounds as Paper 3. Then, for preparations and effects
whose support is outside a corridor window,

```math
\left|
e^T(\mathsf I_{R,o}-\mathsf I_{R,o}^{(0)})p
\right|
\le
C e^{-\mu d}
```

after the reference channel is controlled in the matching topology.

This theorem would be the first bridge from raw locality to operational
locality.

### Theorem C: Operational Exchange Bound

Let `\mathsf I_R` and `\mathsf I_S` be nonselective instruments on the same
slab, and let their calibrated final-space response maps be

```math
\mathscr J_R:=\mathsf I_R\Gamma_0^{-1},
\qquad
\mathscr J_S:=\mathsf I_S\Gamma_0^{-1}.
```

The compositions below are compositions of these calibrated maps acting on the
reference output `q=\Gamma_0p`, not direct compositions of two endpoint kernels
`V_{\Sigma_0}\to V_{\Sigma_1}`. If `\mathscr J_R` and `\mathscr J_S` are
controlled by `J_R` and `J_S`, then for any admissible preparation `p` and
final effect `e`,

```math
\left|
e^T
\left(
\mathscr J_R\mathscr J_S-\mathscr J_S\mathscr J_R
\right)\Gamma_0p
\right|
\le
C_{e,p}
\|E_{R,S}-I\|_{\nu,R:S}^{\mathrm{corr}}
+\text{calibration errors}.
```

Using Paper 3, this gives a finite-slab estimate of the form

```math
O\!\left(\Delta^4e^{-\nu(d_{R,S}+w)}\right)
```

outside the corridor window.

This is the mathematical form of "raw exchange curvature becomes operationally
visible." If no physically realizable instrument can satisfy the calibrated
factorization, then raw exchange curvature remains tomographic rather than
directly operational.

### Theorem D: No-Signaling Under Operational Factorization

If two localized instruments have exact disjoint operational support, or if
their calibrated exchange defect is exactly identity on the tested sector, then
the marginal statistics in `S` are independent of whether the nonselective
instrument in `R` is applied:

```math
\sum_{o_R} \Pr(o_S,o_R|p;\,R\ \mathrm{and}\ S)
=
\Pr(o_S|p;\,S\ \mathrm{only}).
```

Approximate versions should be bounded by the corridor tail from Theorem C.

This is the operational cousin of Einstein causality. It is weaker and more
honest than a Haag-Kastler theorem.

### Theorem E: Projective Instrument Naturality

If sector-resolved instruments satisfy primitive refinement estimates and the
reference-renormalized residual hypotheses of Paper 3, then operational
effects satisfy

```math
e_{a'}\sim P^*e_a
```

in the declared cylinder/effect topology.

This theorem is needed before Paper 4 can make continuum-facing claims.

### Theorem F: Under-Determination No-Go

If two families of microscopic evolutions have identical controlled endpoint
kernels for the declared preparation/control/readout class, then no
operational observable built only from that class can distinguish them.

Conversely, if two Hilbert evolutions have identical primitive `|U|^2` but
different controlled-kernel families once interferometric detector couplings
are allowed, then the missing information is not in the primitive kernel; it is
in the allowed operational control family.

This theorem locates the phase problem sharply instead of burying it.

### Theorem G: Measurement-Problem Scope Theorem

For any finite regulator where localized detector couplings satisfy Theorem
A0, the following are true:

1. single outcomes are represented by mutually exclusive record sectors;
2. outcome probabilities are ordinary stochastic masses;
3. selective state update is conditioning on the record;
4. nonselective evolution is the sum of outcome instruments;
5. no additional wavefunction-collapse dynamics is required inside the ISP
   finite stochastic model.

What remains outside this theorem is equally important:

1. proving that the chosen instrument class is physically complete;
2. recovering phase-sensitive quantum interference;
3. proving projective/continuum stability of record sectors;
4. reconstructing QFT local algebras, if possible.

This theorem is the precise version of the claim "ISP solves the measurement
problem." It is a finite operational-record solution, not a blanket proof of
QFT reconstruction.

## Possible Differences From Standard Relativistic QFT

Paper 4 should be cautious. A difference from standard relativistic QFT can
only appear after operational instruments are defined. Raw `E_{R,S}` alone is
not an experimental prediction.

Candidate scenarios:

1. **Spacelike exchange-order statistics.** If realizable instruments can
   operationally see the raw exchange defect, then the order difference between
   two spacelike-separated calibrated operations could scale like

```math
\Delta^4e^{-\nu d_{R,S}}.
```

Standard local QFT would expect exactly commuting spacelike local operations
under the ideal algebraic hypotheses. Any residual effect must therefore be
identified as finite-regulator/collar physics, detector nonlocality, or a real
departure from standard microcausality.

2. **Foliation/refinement residuals.** If reference-renormalized projective
   residuals fail to vanish, operational statistics may depend on the
   hypersurface/refinement description. Standard relativistic QFT expects
   foliation-independent probabilities after renormalization and proper
   detector modeling.

3. **Boundary-center gauge readouts.** In gauge systems, operational locality
   may require center-resolved instruments. This may differ from naive
   matter-only reductions, but not necessarily from careful algebraic gauge
   theory with centers and edge modes.

4. **Phase/interference recovery.** A primitive Born-squared kernel can miss
   phase information. Interferometric controls must recover standard phase
   shifts if ISP is to match QFT. Failure here would be a genuine no-go.

5. **Vacuum entanglement harvesting.** Later, if a continuum vacuum sector is
   built, two localized detector instruments should reproduce or sharply fail
   to reproduce standard QFT entanglement-harvesting scalings. This is probably
   not the first experimental target, but it is a powerful conceptual test.

## Near-Term Technology Diagnostic

The easiest current technology test is finite and tomographic, not a direct QFT
deviation:

1. implement a small spin/qudit or matter-link Hamiltonian `H`;
2. implement localized deformations `H_R` and `H_S`;
3. estimate endpoint matrices `\Gamma_0`, `\Gamma_R`, `\Gamma_S`;
4. reconstruct `J_R`, `J_S`, and `E_{R,S}`;
5. check fourth-order onset and corridor-distance decay.

This tests Paper 3's raw exchange-curvature bookkeeping. Paper 4's job is to
decide when, if ever, the same object becomes an operational detector
signature.

## Pass Condition

Paper 4 succeeds if it proves a theorem of the following type:

> For a named class of finite common-collar systems with realizable localized
> detector couplings, the induced operational instruments write definite
> stable records, are positive and normalized, use conditioning rather than an
> extra collapse law, inherit anchored locality from the calibrated raw
> comparison maps, obey no-signaling or exchange-order bounds controlled by
> Paper 3's corridor theorem, and are projectively compatible under the Paper
> 2/Paper 3 refinement hypotheses.

This would mean the raw ISP machinery can seed an operational local theory
without importing the entire observable algebra by fiat.

## Fail Condition

Paper 4 fails, usefully, if it proves or strongly exhibits any of the
following:

1. primitive endpoint kernels underdetermine operational effects even with
   localized controls;
2. positivity of instruments requires Hilbert/circuit data not encoded in the
   stochastic kernel family;
3. raw exchange-defect locality does not transfer to any positive operational
   instrument class;
4. projective refinement is stable for raw maps but unstable for effects;
5. standard QFT phase/interference observables cannot be reconstructed without
   adding phase data as primitive.
6. record sectors cannot be made stable under refinement or repeat readout.

In that case relativistic ISP remains a useful finite stochastic representation
layer, but not a self-contained operational reconstruction of QFT.

## Draft Paper Structure

1. **Introduction:** why Paper 3 is not enough.
2. **Ontology:** states, kernels, raw maps, instruments, effects, nets.
3. **Measurement Problem:** records, conditioning, and no collapse postulate.
4. **Realizable Instruments:** detector ancillas and positive readouts.
5. **Calibrated Relative Responses:** how Paper 3 locality can enter.
6. **Operational Exchange Bounds:** when `E_{R,S}` controls order effects.
7. **No-Signaling And Einstein Causality:** finite operational theorem, not yet
   Haag-Kastler.
8. **Projective Instrument Naturality:** refinement-compatible effects.
9. **Gauge Centers:** sector-resolved instruments and boundary flux.
10. **QFT Comparison Tests:** exchange order, foliation, phase/interference,
   entanglement harvesting.
11. **No-Go Alternatives:** where extra primitive structure is needed.

## Immediate Next Work

The record-retaining definition is now clean enough to start the paper draft.
The next concrete work should be:

1. promote Theorem A0 into a fully written finite-dimensional theorem and
   proof;
2. add the two-path interferometer as the minimum phase/interference benchmark;
3. define the operational model class: preparations, localized controls,
   record instruments, effects, and operational equivalence;
4. prove the simple positivity/effect theorem for general realizable
   instruments;
5. only then attack the hard exchange-bound transfer from Paper 3.

Once these definitions are fixed, the rest of Paper 4 becomes a sequence of
transfer questions:

```math
\text{raw locality}
\quad\Rightarrow?\quad
\text{instrument locality}
\quad\Rightarrow?\quad
\text{observable locality}
\quad\Rightarrow?\quad
\text{QFT-like causality}.
```

The first theorem is the definite-record instrument theorem: positivity,
normalization, stable record sectors, and conditioning-as-update. The first
hard theorem is the operational exchange bound.
