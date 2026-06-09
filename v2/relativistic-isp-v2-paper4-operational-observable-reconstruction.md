# Operational Observable Reconstruction From Relativistic ISP Kernels

Author: Felix Robles Elvira

V2 Paper 4 consolidated draft

Date: 2026-05-14

Status: theorem-framework draft with finite record-instrument,
generalized-readout, measurement-scope, two-path interference,
finite phase-completeness, locality transfer, explicit write-register and
finite-depth detector anchoring benchmarks, screened selective locality,
operational exchange, no-signaling, projective record-naturality, nested
detector coarse-graining, lossy detector refinement, calibration-residual
budget, and exchange-to-experiment pipeline results, plus an operational
underdetermination no-go. This paper begins the operational layer after V2 Paper
3. It does not identify raw comparison maps with observables. It asks which
detector instruments, effects, and local operational statistics are actually
selected by finite ISP kernel data, and which extra control/readout structure
must be declared.

## Abstract

Relativistic ISP begins with stochastic endpoint kernels on finite
configuration spaces and uses localized comparison maps

```math
J_R=\Gamma_R\Gamma_0^{-1}
```

and exchange defects

```math
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}
```

to organize relativistic locality and hypersurface-deformation data. V2 Paper
3 controls these raw algebraic maps in a common-collar interacting class. But
raw relative maps are generally pseudo-stochastic: they preserve total mass but
need not preserve positivity. They are not effects, instruments, observables,
or experimental events.

This paper introduces the next layer: operational detector instruments. The
first result is finite and exact. If a localized detector coupling is described
by a stochastic enlarged endpoint kernel and the detector has disjoint record
sectors, then the induced record-retaining operations form a positive
normalized instrument. Single outcomes are definite record-sector events;
selective update is ordinary conditioning; no additional collapse dynamics is
postulated. This is the precise finite ISP sense in which the measurement
problem is addressed.

The paper then separates this finite record solution from harder
reconstruction questions. A single Born-squared endpoint kernel can
underdetermine phase-sensitive quantum physics. Interference requires a
sufficiently rich family of controlled kernels and detector couplings. Paper 4
therefore has a positive program and a possible no-go: either localized
operational instruments inherit Paper 3's anchored locality and exchange
bounds, or observable reconstruction requires extra primitive Hilbert/circuit
or control data.

The unconditional finite results are the record-instrument theorem,
generalized readout theorem, repeatability/reset analysis, two-path benchmark,
finite phase-completeness criterion, local write-register and finite-depth
detector anchoring benchmarks, finite-depth detector calibration example, nested
and lossy detector coarse-graining benchmarks, calibration residual budget,
exchange-to-experiment pipeline, and operational underdetermination theorem. The
locality, exchange, no-signaling, and projective-continuity results are
conditional transfer theorems: they identify exactly which calibrated locality,
detector compression, and record-refinement hypotheses are needed before the raw
Paper 3 machinery becomes operational physics.

## 1. Scope And Non-Claims

Established in this draft:

1. raw ISP comparison maps and exchange defects are formally separated from
   operational instruments;
2. a finite detector-record ontology is stated;
3. an admissible operational family `\mathcal O_a` is defined;
4. a record-retaining instrument theorem is proved;
5. arbitrary positive detector readouts and classical postprocessing are shown
   to generate positive normalized instruments;
6. selective update is identified with conditioning on a record sector;
7. approximate repeat-readout, record leakage, and detector reset are stated;
8. a finite two-path benchmark proves the coherent fringe and which-path
   record marginal, and a finite phase-completeness criterion states exactly
   which controlled interferometer data recover phase-sensitive statistics;
9. a tree-norm remote-effect lemma, detector-compression theorem, local
   write-register detector benchmark, finite-depth detector anchoring theorem,
   centered and screened selective-outcome theorems, and conditional
   locality-transfer theorem turn calibrated anchored response bounds into
   operational statistic bounds;
10. a calibration residual budget and finite-depth detector example record how
    theorem residuals and experimental uncertainties enter tested statistics;
11. an operational exchange theorem and exchange-to-experiment pipeline bound
    order-dependent statistics by Paper 3's exchange corridor plus calibration
    residuals;
12. exact and approximate finite no-signaling theorems are stated in
    instrument/effect language;
13. nested and lossy detector coarse-graining results prove exact and approximate
    record-sector refinement models;
14. projective record-sector naturality transfers enlarged kernel refinement
    to operational instrument statistics;
15. an operational underdetermination theorem locates the no-go when the
    declared control/detector family is too poor.

Not established here:

1. that every raw `J_R` is realizable by a positive detector instrument;
2. that raw exchange curvature is automatically measurable;
3. a continuum Haag-Kastler net;
4. QFT reconstruction from a single stochastic kernel;
5. recovery of phase-sensitive observables outside declared phase-complete
   controlled kernel families;
6. automatic projective stability of record sectors without detector
   coarse-graining data;
7. anchored calibrated responses for detectors outside the bounded finite-depth
   collar-scaffold class;
8. selective-outcome locality without a screening, remote-pair, centering, or
   clustering hypothesis.

The guiding rule is simple: a physical observable is not a matrix with support.
It is a procedure that turns preparations into outcome frequencies and leaves
records.

### Result Classification

Unconditional finite stochastic facts:

1. Theorem 1, Theorem 3, and Theorem 4: records, conditioning, repeatability
   bounds, reset, and generalized readouts;
2. Proposition 6: coherent versus which-path finite benchmark;
3. Theorem 6A and Corollary 6B: finite phase-completeness criterion and
   phase-incompleteness diagnostic;
4. Proposition 10A and Theorem 10B: local write-register and finite-depth
   detector anchoring;
5. Proposition 11D and Example 11E: calibration residual budget and finite-depth
   detector calibration example;
6. Proposition 19A: nested detector coarse-graining benchmark;
7. Theorem 21 and its corollaries: operational underdetermination.

Conditional transfer results:

1. Theorems 8 and 10: calibrated anchored locality transfers to operational
   statistics when detector compression and remote-test hypotheses hold;
2. Theorem 11A, Corollary 11B, and Theorem 11C: centered, conditional, and
   screened selective-outcome locality follows from explicit clustering,
   screening, and outcome-floor hypotheses;
3. Theorem 13 and Corollaries 14-15: operational exchange follows when
   operational calibrated responses approximate Paper 3 raw maps;
4. Theorems 17-18: no-signaling follows from operational commutation or the
   operational exchange bound;
5. Theorem 19, Theorem 19B, and Corollary 20: projective operational statistics
   follow from enlarged-kernel, record-sector naturality, and explicit lossy
   record bookkeeping.

## 2. Dependency Ledger

This paper uses the following V2 inputs.

1. V2 Paper 2 supplies projective states, cylinder effects, and refinement
   error propagation through comparison maps.
2. V2 Paper 3 supplies common-collar anchored locality for raw relative maps,
   inverse control, exchange-corridor estimates, sectorwise variants, and
   projective transfer hypotheses.
3. Earlier finite operational benchmark papers motivate detector ancillas,
   localized controls, and no-signaling tests, but they do not by themselves
   prove a continuum operational reconstruction theorem.

Paper 3 exports algebraic relative dynamics. Paper 4 must decide which pieces
of that algebraic structure can be operationalized.

## 3. Finite Ordered State Space

For a regulated hypersurface `\Sigma` with finite configuration set
`C_{\Sigma,a}`, define

```math
V_{\Sigma,a}=\mathbb R^{C_{\Sigma,a}},
\qquad
V_{\Sigma,a,+}=\{p:p_c\ge0\}.
```

Normalized states satisfy

```math
1_{\Sigma,a}^Tp=1.
```

Effects are positive functionals bounded by the unit effect:

```math
0\le e\le1_{\Sigma,a}.
```

A primitive endpoint kernel is a column-stochastic map

```math
\Gamma:V_{\Sigma_0,a}\to V_{\Sigma_1,a},
\qquad
\Gamma V_{\Sigma_0,a,+}\subseteq V_{\Sigma_1,a,+},
\qquad
1_{\Sigma_1,a}^T\Gamma=1_{\Sigma_0,a}^T.
```

A comparison map

```math
J_R=\Gamma_R\Gamma_0^{-1}
```

is generally only pseudo-stochastic:

```math
1^TJ_R=1^T,
```

but `J_RV_+` need not be contained in `V_+`. Therefore `J_R` is not an
instrument. This one sentence prevents the main category error.

## 4. Measurement As Definite Record

The standard measurement problem comes from trying to combine universal
unitarity, definite outcomes, and Born probabilities. In this finite operational
layer, ISP changes the primitive predictive object: it is not a wavefunction
awaiting collapse, but a stochastic endpoint-record dynamics.

Let a detector near a region `R` have a finite record space

```math
D_R=\bigsqcup_oD_{R,o},
```

where the `D_{R,o}` are disjoint outcome sectors. Let

```math
W_R=\mathbb R^{D_R},
\qquad
W_{R,+}=\mathbb R_+^{D_R},
```

and let `\Pi_o:W_R\to W_R` be the coordinate projection onto `D_{R,o}`.
Then

```math
\Pi_oW_{R,+}\subseteq W_{R,+},
\qquad
\Pi_o\Pi_{o'}=\delta_{oo'}\Pi_o,
\qquad
\sum_o\Pi_o=I_{W_R}.
```

The detector starts in a normalized ready state

```math
\eta_R\in W_{R,+},
\qquad
1_{D_R}^T\eta_R=1.
```

The enlarged system-detector endpoint kernel is

```math
\Gamma_{R,D}:V_{\Sigma_0,a}\otimes W_R
\to
V_{\Sigma_1,a}\otimes W_R.
```

It is stochastic when

```math
\Gamma_{R,D}(V_{\Sigma_0,a,+}\otimes W_{R,+})
\subseteq
V_{\Sigma_1,a,+}\otimes W_{R,+},
```

and

```math
\left(1_{\Sigma_1,a}^T\otimes1_{D_R}^T\right)
\Gamma_{R,D}
=
1_{\Sigma_0,a}^T\otimes1_{D_R}^T.
```

### Theorem 1: Definite-record instrument theorem

For each outcome `o`, define the record-retaining operation

```math
\widehat{\mathsf I}_{R,o}p
:=
\left(I_{\Sigma_1,a}\otimes\Pi_o\right)
\Gamma_{R,D}(p\otimes\eta_R)
\in
V_{\Sigma_1,a}\otimes W_R,
```

and the compressed system operation

```math
\mathsf I_{R,o}p
:=
\left(I_{\Sigma_1,a}\otimes1_{D_R}^T\right)
\widehat{\mathsf I}_{R,o}p.
```

If `\Gamma_{R,D}` is stochastic, then:

1. `\widehat{\mathsf I}_{R,o}` is positive for every `o`;
2. `\widehat{\mathsf I}_{R,o}` and `\widehat{\mathsf I}_{R,o'}` have disjoint
   detector-record support for `o\ne o'`;
3. the compressed maps `\mathsf I_{R,o}` form a positive normalized
   instrument:

```math
\mathsf I_{R,o}V_{\Sigma_0,a,+}\subseteq V_{\Sigma_1,a,+},
\qquad
\sum_o1_{\Sigma_1,a}^T\mathsf I_{R,o}=1_{\Sigma_0,a}^T.
```

The probability of outcome `o` in preparation `p` is

```math
\Pr(o|p)=1_{\Sigma_1,a}^T\mathsf I_{R,o}p.
```

If this probability is nonzero, the selective full record state is

```math
\widehat p_o
=
\frac{\widehat{\mathsf I}_{R,o}p}
{\left(1_{\Sigma_1,a}^T\otimes1_{D_R}^T\right)
\widehat{\mathsf I}_{R,o}p},
```

and the selective system marginal is

```math
p_o
=
\frac{\mathsf I_{R,o}p}
{1_{\Sigma_1,a}^T\mathsf I_{R,o}p}.
```

No additional collapse map is needed.

Proof. Positivity follows because `p\otimes\eta_R` is positive for positive
`p`, `\Gamma_{R,D}` is positive, and `I\otimes\Pi_o` is positive. Disjoint
record support follows from `\Pi_o\Pi_{o'}=0` for `o\ne o'`.

For normalization, compute

```math
\begin{aligned}
\sum_o1_{\Sigma_1,a}^T\mathsf I_{R,o}p
&=
\sum_o
\left(1_{\Sigma_1,a}^T\otimes1_{D_R}^T\right)
\left(I_{\Sigma_1,a}\otimes\Pi_o\right)
\Gamma_{R,D}(p\otimes\eta_R)
\\
&=
\left(1_{\Sigma_1,a}^T\otimes1_{D_R}^T\right)
\Gamma_{R,D}(p\otimes\eta_R)
\\
&=
\left(1_{\Sigma_0,a}^T\otimes1_{D_R}^T\right)
(p\otimes\eta_R)
\\
&=
\left(1_{\Sigma_0,a}^Tp\right)
\left(1_{D_R}^T\eta_R\right)
=
1_{\Sigma_0,a}^Tp.
\end{aligned}
```

Thus `\sum_o1_{\Sigma_1,a}^T\mathsf I_{R,o}=1_{\Sigma_0,a}^T`. The formulas
for the selective states are ordinary conditional probabilities on the
record-sector event. `square`

### Repeatability

The theorem gives single records. Repeatability is an additional stability
hypothesis, not a word to smuggle in.

For a normalized system-detector state

```math
\widehat q\in
\Delta(V_{\Sigma_1,a}\otimes W_R),
```

define its leakage away from record sector `o` by

```math
\ell_o(\widehat q)
:=
\left(1_{\Sigma_1,a}^T
\otimes
1_{D_R\setminus D_{R,o}}^T\right)\widehat q.
```

Exact support in `D_{R,o}` means `\ell_o(\widehat q)=0`.

An immediate repeat readout may include a short record-holding/readout kernel

```math
\Theta_R:
V_{\Sigma_1,a}\otimes W_R
\to
V_{\Sigma_1,a}\otimes W_R,
```

assumed stochastic. Its one-step sector-instability for outcome `o` is

```math
\epsilon_o(\Theta_R)
:=
\sup_{\substack{
\widehat q\in\Delta(V_{\Sigma_1,a}\otimes W_R)\\
\ell_o(\widehat q)=0}}
\left(1_{\Sigma_1,a}^T
\otimes
1_{D_R\setminus D_{R,o}}^T\right)
\Theta_R\widehat q.
```

This number is zero when the record sector is perfectly stable under immediate
repeat readout.

### Proposition 2: repeat-readout error bound

Let `\widehat q` be a normalized state selected as outcome `o`, possibly with
leakage `\ell_o(\widehat q)`. After the repeat-readout kernel `\Theta_R`, the
probability of obtaining an outcome different from `o` is bounded by

```math
\Pr_\Theta(o'\ne o\mid \widehat q)
\le
\ell_o(\widehat q)+\epsilon_o(\Theta_R).
```

In particular, if `\widehat q=\widehat p_o` is the exact selected state from
Theorem 1 and `\Theta_R` preserves the sector exactly, then

```math
\Pr(o'|o)
=
\left(1_{\Sigma_1,a}^T\otimes1_{D_R}^T\Pi_{o'}\right)\widehat p_o
=
\delta_{o'o}.
```

Proof. Decompose

```math
\widehat q
=
\left(I\otimes\Pi_o\right)\widehat q
+
\left(I\otimes(I-\Pi_o)\right)\widehat q
=:\widehat q_{\mathrm{in}}+\widehat q_{\mathrm{out}}.
```

The mass of `\widehat q_{\mathrm{out}}` is `\ell_o(\widehat q)`. Since
`\Theta_R` is stochastic, the total contribution of
`\widehat q_{\mathrm{out}}` to any event is at most `\ell_o(\widehat q)`. The
normalized version of `\widehat q_{\mathrm{in}}`, when its mass is nonzero, is
supported in sector `o`, so its wrong-sector mass after `\Theta_R` is bounded
by `\epsilon_o(\Theta_R)`. Adding the two contributions gives the bound. If
`\ell_o=0` and `\epsilon_o=0`, the repeat statistics are exact. `square`

### Detector reset

Independent trials and some sequential compositions require a reset operation.
The canonical reset-to-ready map is

```math
\mathcal R_{\eta_R}:W_R\to W_R,
\qquad
\mathcal R_{\eta_R}w:=\eta_R(1_{D_R}^Tw).
```

It is stochastic:

```math
\mathcal R_{\eta_R}W_{R,+}\subseteq W_{R,+},
\qquad
1_{D_R}^T\mathcal R_{\eta_R}=1_{D_R}^T.
```

Reset is not collapse. It is an ordinary physical operation on the detector
record. Without a declared reset, sequential experiments must keep the old
record as part of the state, and outcome statistics may contain memory effects.

### Theorem 3: finite measurement-problem scope

Fix a finite regulator and an admissible family of detector couplings with
record sectors as above. Then within that finite model:

1. each outcome is a concrete event `D_{R,o}` in detector configuration space;
2. outcome probabilities are stochastic masses;
3. selective update is conditionalization on the record event;
4. nonselective evolution is the sum of outcome operations;
5. immediate repeatability is exact or approximate according to Proposition 2;
6. independent repeated trials require a declared reset operation;
7. no additional wavefunction-collapse dynamics is postulated.

Proof. Items 1-4 and 7 are Theorem 1. Item 5 is Proposition 2. Item 6 follows
because, without a reset, the detector marginal after a measurement need not
equal the ready state `\eta_R`; the next trial is then a different physical
initial condition. `square`

This is the precise finite ISP content of addressing the definite-outcome part
of the measurement problem. It removes the need for a second collapse law inside
a declared finite detector-record model. It does not prove the following:

1. that the chosen instrument family is physically complete;
2. that phase-sensitive quantum interference is recovered;
3. that record sectors are projectively stable under refinement;
4. that a continuum QFT local algebra has been reconstructed.

Those are separate Paper 4 and later-paper obligations.

For quick reference, the approximate repeatability bound can also be written as

```math
\Pr_\Theta(o|o)
\ge
1-\ell_o(\widehat q)-\epsilon_o(\Theta_R).
```

## 5. Realizable Local Instruments

A localized instrument near `R` is **realizable** at regulator `a` when it is
generated by:

1. a finite detector record space `D_R`;
2. an initialized detector state `\eta_R`;
3. a record-sector partition `D_R=\bigsqcup_oD_{R,o}`;
4. a stochastic enlarged kernel `\Gamma_{R,D}`;
5. a localized coupling condition saying that outside the collar of `R`, the
   enlarged dynamics agrees with the reference dynamics in the anchored
   topology used by Paper 3.

This definition is deliberately operational. It does not require Hilbert-space
operators as primitive, but it can represent them when a Hilbert benchmark
supplies the detector coupling.

The associated effect is

```math
e_{R,o}^T:=1_{\Sigma_1,a}^T\mathsf I_{R,o}.
```

By Theorem 1,

```math
0\le e_{R,o}\le1,
\qquad
\sum_o e_{R,o}=1.
```

### Theorem 4: generalized positive readout instruments

Let the system-detector coupling be as in Theorem 1, but replace the sharp
record-sector projections by a finite family of positive detector readout
effects

```math
\xi_\alpha\in W_R^*,
\qquad
\xi_\alpha\ge0,
\qquad
\sum_\alpha\xi_\alpha=1_{D_R}^T.
```

Define

```math
\mathsf I_{R,\alpha}^{\xi}p
:=
\left(I_{\Sigma_1,a}\otimes\xi_\alpha\right)
\Gamma_{R,D}(p\otimes\eta_R).
```

Then the `\mathsf I_{R,\alpha}^{\xi}` form a positive normalized instrument:

```math
\mathsf I_{R,\alpha}^{\xi}V_{\Sigma_0,a,+}
\subseteq
V_{\Sigma_1,a,+},
\qquad
\sum_\alpha
1_{\Sigma_1,a}^T\mathsf I_{R,\alpha}^{\xi}
=
1_{\Sigma_0,a}^T.
```

The associated effects

```math
\left(e_{R,\alpha}^{\xi}\right)^T
:=
1_{\Sigma_1,a}^T\mathsf I_{R,\alpha}^{\xi}
```

satisfy

```math
0\le e_{R,\alpha}^{\xi}\le1_{\Sigma_0,a},
\qquad
\sum_\alpha e_{R,\alpha}^{\xi}=1_{\Sigma_0,a}.
```

Proof. Positivity follows from positivity of `p\otimes\eta_R`,
`\Gamma_{R,D}`, and the detector effect `\xi_\alpha`. Normalization follows
from the partition-of-unit condition:

```math
\begin{aligned}
\sum_\alpha1_{\Sigma_1,a}^T
\mathsf I_{R,\alpha}^{\xi}p
&=
\sum_\alpha
\left(1_{\Sigma_1,a}^T\otimes\xi_\alpha\right)
\Gamma_{R,D}(p\otimes\eta_R)
\\
&=
\left(1_{\Sigma_1,a}^T\otimes1_{D_R}^T\right)
\Gamma_{R,D}(p\otimes\eta_R)
\\
&=
1_{\Sigma_0,a}^Tp.
\end{aligned}
```

The effect bounds are the same statement in dual form. `square`

### Classical postprocessing

Sharp record-sector readout followed by classical stochastic postprocessing is
a special case. Let

```math
K_{\alpha|o}\ge0,
\qquad
\sum_\alpha K_{\alpha|o}=1
```

be a classical channel from sharp record outcomes `o` to reported outcomes
`\alpha`. Define

```math
\mathsf I_{R,\alpha}^{K}
:=
\sum_oK_{\alpha|o}\mathsf I_{R,o}.
```

Then the `\mathsf I_{R,\alpha}^{K}` are a positive normalized instrument. They
are obtained from Theorem 4 by choosing

```math
\xi_\alpha
=
\sum_oK_{\alpha|o}\,1_{D_R}^T\Pi_o.
```

The distinction matters. Arbitrary positive detector effects may inspect the
microscopic detector configuration inside a record sector. Classical
postprocessing of the coarse records only uses the sector label `o`. Paper 4
should state which level is physically admitted in `\mathcal O_a`.

## 6. Admissible Operational Family

The symbol `\mathcal O_a` denotes what the finite theory actually allows an
experimenter to prepare, control, couple to, and read out at regulator `a`.
Without this declared family, "observable reconstruction" is ill-posed: two
theories are operationally identical if they agree on all statistics generated
by the declared operations.

Fix a slab `\Sigma_0\to\Sigma_1` and write

```math
V_0:=V_{\Sigma_0,a},
\qquad
V_1:=V_{\Sigma_1,a}.
```

Let `1_0^T` and `1_1^T` denote the unit effects on `V_0` and `V_1`.

An **admissible operational family** `\mathcal O_a` consists of the following
finite data.

1. **Preparation class.** A nonempty convex set

```math
\mathcal P_a\subseteq\Delta(V_0)
```

of normalized positive initial states. Convexity encodes classical
randomization of preparation procedures.

2. **Reference dynamics.** A stochastic reference kernel

```math
\Gamma_0^a:V_0\to V_1.
```

When calibrated responses are used, `\Gamma_0^a` must be invertible on the
declared linear test domain. Positivity of its inverse is not assumed.

3. **Localized control labels.** For each admissible collar region `R`, a set
`\Lambda_a(R)` of control labels. A label `\lambda\in\Lambda_a(R)` specifies a
localized system-detector coupling, its detector record space, and its
readout partition. Its geometric support is written

```math
\operatorname{supp}(\lambda)\subseteq\operatorname{collar}(R).
```

4. **Record instruments.** Each control label `\lambda` determines a finite
detector record space

```math
D_\lambda=\bigsqcup_{o\in O_\lambda}D_{\lambda,o},
```

a normalized ready state `\eta_\lambda`, a stochastic enlarged kernel
`\Gamma_{\lambda,D}`, and record projections `\Pi_{\lambda,o}`. The associated
record-retaining and compressed operations are

```math
\widehat{\mathsf I}_{\lambda,o}p
:=
\left(I_1\otimes\Pi_{\lambda,o}\right)
\Gamma_{\lambda,D}(p\otimes\eta_\lambda),
```

and

```math
\mathsf I_{\lambda,o}p
:=
\left(I_1\otimes1_{D_\lambda}^T\right)
\widehat{\mathsf I}_{\lambda,o}p.
```

The nonselective channel is

```math
\mathsf I_\lambda:=\sum_{o\in O_\lambda}\mathsf I_{\lambda,o}.
```

The sharp record partition is one **readout scheme**, denoted
`\rho=\mathrm{sharp}`, with

```math
O_{\lambda,\mathrm{sharp}}:=O_\lambda,
\qquad
\mathsf I_{\lambda,\mathrm{sharp},o}:=\mathsf I_{\lambda,o}.
```

The family may also declare additional readout schemes `\rho` for the same
system-detector coupling, such as generalized detector readout effects

```math
\xi_{\lambda,\rho,\alpha}\in(\mathbb R^{D_\lambda})^*,
\qquad
\xi_{\lambda,\rho,\alpha}\ge0,
\qquad
\sum_{\alpha\in O_{\lambda,\rho}}\xi_{\lambda,\rho,\alpha}
=1_{D_\lambda}^T,
```

with

```math
\mathsf I_{\lambda,\rho,\alpha}p
:=
\left(I_1\otimes\xi_{\lambda,\rho,\alpha}\right)
\Gamma_{\lambda,D}(p\otimes\eta_\lambda),
```

or classical postprocessed readouts of sharp record outcomes. These operations are
admitted only when the scheme `\rho` is named as part of `\mathcal O_a`. Each
scheme has its own outcome set `O_{\lambda,\rho}` and its own normalization.
When no distinction is needed, `\rho` is suppressed and `o` denotes an outcome
label inside one fixed declared readout scheme.

5. **Readout/effect class.** A convex set `\mathcal E_a\subseteq V_1^*` of
positive final effects with `0\le e^T\le1_1^T`. It contains the unit effect
`1_1^T` and all instrument effects

```math
e_{\lambda,\rho,o}^T:=1_1^T\mathsf I_{\lambda,\rho,o}.
```

It is closed under finite classical coarse-graining: if `0\le c_i\le1` and
`\sum_i c_i\le1`, then `\sum_i c_ie_i\in\mathcal E_a` whenever the `e_i` are
jointly declared readouts of the same experiment.

6. **Outcome coarse-graining.** For a fixed readout scheme `\rho`, if
`A\subseteq O_{\lambda,\rho}`, then

```math
\mathsf I_{\lambda,\rho,A}
:=
\sum_{o\in A}\mathsf I_{\lambda,\rho,o}
```

is also an allowed coarse-grained operation, with effect
`e_{\lambda,\rho,A}=\sum_{o\in A}e_{\lambda,\rho,o}`.

7. **Sequential composition domain.** A partial composition law states when
two operations may be performed in sequence. If
`\lambda\prec\mu` is admissible, then the composed outcome operation is

```math
\mathsf I_{\mu,\rho_\mu,o_\mu}\mathsf I_{\lambda,\rho_\lambda,o_\lambda},
```

after identifying the output space of the first operation with the input space
of the second. This is a partial law because different hypersurface slabs,
detector reset assumptions, and overlapping record spaces may make a formal
matrix product physically meaningless.

8. **Locality/calibration domain.** For every `\lambda`, the calibrated
response

```math
\mathscr J_{\lambda,\rho,o}
:=
\mathsf I_{\lambda,\rho,o}(\Gamma_0^a)^{-1}
```

is a declared object only on the same preparation/effect test domain where
`(\Gamma_0^a)^{-1}` is controlled. The family records whether
`\mathscr J_{\lambda,\rho,o}` lies in the anchored topology exported by Paper
3.

9. **Projective data, when comparing regulators.** If `a'\ge a`, the family
includes coarse-graining maps for system configurations and record sectors:

```math
P_{\Sigma_i,a\leftarrow a'}:V_{\Sigma_i,a'}\to V_{\Sigma_i,a},
\qquad
D_{\lambda,o}^{a'}\to D_{\lambda,o}^{a}.
```

These data are not automatic. If record sectors do not refine consistently,
Paper 4 has only a fixed-regulator measurement theory.

The operational statistics generated by `\mathcal O_a` are the numbers

```math
\Pr_{\mathcal O_a}(e,\lambda,\rho,o|p)
:=
e^T\mathsf I_{\lambda,\rho,o}p,
\qquad
p\in\mathcal P_a,\ e\in\mathcal E_a.
```

For the bare outcome probability, take `e=1_1`.

### Operational equivalence

Two outcome operations `\mathsf I_{\lambda,\rho,o}` and
`\mathsf I_{\lambda',\rho',o'}` are operationally equivalent relative to
`\mathcal O_a`, written

```math
\mathsf I_{\lambda,\rho,o}
\sim_{\mathcal O_a}
\mathsf I_{\lambda',\rho',o'},
```

if

```math
e^T\mathsf I_{\lambda,\rho,o}p
=
e^T\mathsf I_{\lambda',\rho',o'}p
```

for every `p\in\mathcal P_a` and every `e\in\mathcal E_a`. An operational
observable is an equivalence class of outcome operations, or equivalently of
effects, relative to the declared preparation/effect class.

This definition is intentionally modest. It does not say that all mathematically
positive maps are physically allowed. It says that Paper 4 must name the
allowed preparation-control-detector-readout family before it can claim
reconstruction or no-go.

### Lemma 5: positivity of generated statistics

For every admissible family `\mathcal O_a`,

```math
\Pr_{\mathcal O_a}(e,\lambda,\rho,o|p)\ge0
```

for all `p\in\mathcal P_a`, `e\in\mathcal E_a`, and outcomes `o` in any fixed
declared readout scheme `\rho`. Moreover, for the unit effect and each fixed
scheme `\rho`,

```math
\sum_{o\in O_{\lambda,\rho}}
\Pr_{\mathcal O_a}(1_1,\lambda,\rho,o|p)
=1.
```

Proof. Positivity follows because `p` is positive,
`\mathsf I_{\lambda,\rho,o}` is positive by Theorem 1 for sharp records and by
Theorem 4 for generalized readouts or postprocessed readouts, and `e` is a
positive functional. Normalization follows from the corresponding normalized
instrument:

```math
\sum_{o\in O_{\lambda,\rho}}
1_1^T\mathsf I_{\lambda,\rho,o}p
=1_0^Tp=1.
```

`square`

## 7. Calibrated Relative Responses

Paper 3 controls relative maps. To connect operational instruments to that
machinery, define the calibrated response

```math
\mathscr J_{R,o}:=\mathsf I_{R,o}\Gamma_0^{-1},
```

when the reference inverse is controlled on the declared preparation/effect
domain. This object may be pseudo-stochastic. It is not the instrument.

The operational statistic is

```math
\Pr(o|p)
=
1^T\mathsf I_{R,o}p
=
1^T\mathscr J_{R,o}\Gamma_0p.
```

This is the bridge: Paper 3 can estimate `\mathscr J`-type relative objects,
but positivity and outcome probabilities live in `\mathsf I`.

## 8. The Two-Path Interference Benchmark

The simplest phase test is a two-path interferometer. Let the path state space
be `\{0,1\}` and let

```math
B=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P_\phi=
\begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix},
\qquad
U_\phi=BP_\phi B.
```

The coherent ISP endpoint kernel supplied by this controlled Hilbert benchmark
is

```math
\Gamma_\phi:=|U_\phi|^2
=
\begin{pmatrix}
\cos^2(\phi/2)&\sin^2(\phi/2)\\
\sin^2(\phi/2)&\cos^2(\phi/2)
\end{pmatrix}.
```

For input path `0`,

```math
\Pr_\phi(0|0)=\cos^2(\phi/2),
\qquad
\Pr_\phi(1|0)=\sin^2(\phi/2).
```

This is the smallest benchmark that can see a phase. If the operational family
contains only one unlabelled endpoint kernel, it has not encoded the phase
control. It has encoded only one stochastic transition.

Now insert a which-path detector between the two beam splitters. Let the
detector record space be

```math
D=\{d_0,d_1\},
```

where `d_x` records that the intermediate path was `x`. The record-retaining
which-path kernel is

```math
\widehat\Gamma_{\mathrm{wp},\phi}:
\mathbb R^{\{0,1\}}
\to
\mathbb R^{\{0,1\}}\otimes\mathbb R^D,
```

with matrix entries

```math
\left[
\widehat\Gamma_{\mathrm{wp},\phi}
\right]_{(y,d_x),j}
=
|B_{yx}|^2\,|B_{xj}|^2.
```

The phase matrix `P_\phi` is absent from this formula because, after the
intermediate path has been recorded and the record is not coherently erased,
the relative phase between the two path alternatives no longer contributes to
the marginal output probabilities.

### Proposition 6: coherent fringe versus which-path record

The coherent controlled kernel is `\Gamma_\phi` above. The system marginal of
the which-path record kernel is

```math
\Gamma_{\mathrm{wp},\phi}
:=
\left(I\otimes1_D^T\right)
\widehat\Gamma_{\mathrm{wp},\phi}
=
\begin{pmatrix}
1/2&1/2\\
1/2&1/2
\end{pmatrix},
```

independent of `\phi`. Hence, for input path `0`,

```math
\Pr_{\mathrm{wp}}(0|0)=\Pr_{\mathrm{wp}}(1|0)=1/2,
```

whereas the coherent control gives

```math
\Pr_\phi(0|0)=\cos^2(\phi/2),
\qquad
\Pr_\phi(1|0)=\sin^2(\phi/2).
```

Proof. The coherent formula follows by direct multiplication:

```math
U_\phi
=
\frac12
\begin{pmatrix}
1+e^{i\phi}&1-e^{i\phi}\\
1-e^{i\phi}&1+e^{i\phi}
\end{pmatrix}.
```

Taking entrywise squared moduli gives the stated `\Gamma_\phi`.

For the which-path kernel, `|B_{yx}|^2=1/2` and `|B_{xj}|^2=1/2` for all
`x,y,j`. Therefore

```math
\left[
\widehat\Gamma_{\mathrm{wp},\phi}
\right]_{(y,d_x),j}
=1/4,
```

and summing over the detector record `d_x` gives

```math
\left[\Gamma_{\mathrm{wp},\phi}\right]_{y,j}
=
\sum_{x=0}^1
\left[
\widehat\Gamma_{\mathrm{wp},\phi}
\right]_{(y,d_x),j}
=
1/2.
```

This proves the incoherent marginal and its independence of `\phi`. `square`

### Theorem 6A: finite phase-completeness criterion

Fix a finite Hilbert benchmark with preferred configuration basis `C` and finite
detector bases for any records. A declared operational family `\mathcal O_a` is
**phase-complete for a finite interferometer class** `\mathfrak C` when it
contains the following data for every circuit word in `\mathfrak C`:

1. **Coherent controls:** each splitter, recombiner, phase shifter, and internal
   coherent control is represented by a named unitary matrix on the relevant
   finite Hilbert space, not merely by its stochastic endpoint matrix.
2. **Coherent composition:** if a word has no intermediate record, its ISP
   endpoint kernel is formed only after composing amplitudes:

```math
\Gamma_w(y|x)
=
\left|
\langle y|U_n\cdots U_1|x\rangle
\right|^2.
```

3. **Record-writing controls:** a which-alternative detector is represented by a
   record-retaining isometry or stochastic endpoint kernel into an enlarged
   configuration space `C\otimes D`, with disjoint detector sectors.
4. **Nonselective record marginal:** ignoring an actual record means summing over
   the detector record sectors, not coherently recombining them.
5. **Erasure controls, when claimed:** if the family claims coherent erasure, it
   declares an operation on the enlarged system-detector space that is inverse to
   the marker on the controlled pre-record subspace. If no such operation is in
   `\mathcal O_a`, erasure is not an available observable procedure.
6. **Common composition domain:** coherent controls, record-writing controls,
   erasure controls, readouts, resets, and postprocessings are all composable in
   the same declared family.

Then for every preparation diagonal in the preferred basis, every declared
output effect, and every operation word in `\mathfrak C`, the ISP operational
statistic agrees with the corresponding finite quantum Born statistic for that
declared circuit.

In particular:

1. coherent two-path words reproduce the fringe

```math
\Pr_\phi(0|0)=\cos^2(\phi/2);
```

2. a retained which-path record gives the incoherent marginal

```math
\Pr_{\mathrm{wp}}(0|0)=1/2;
```

3. a declared coherent erasure before record readout restores the corresponding
   coherent circuit statistic, up to the residuals certified for that erasure
   operation;
4. a formed detector record that is not coherently erased remains a record-sector
   event and is treated by conditioning and nonselective marginalization.

The criterion is sufficient, not automatic. A primitive endpoint kernel alone is
not phase-complete, because it does not tell the theory which amplitude-level
controls may be inserted in later experiments.

Proof. For coherent words, the declared kernel is by definition the Born-squared
matrix of the composed unitary word, so pairing it with diagonal preparations
and output effects gives the finite Born statistic. For record-writing words,
Theorem 1 gives a positive record-retaining instrument on the enlarged
configuration space; summing over detector sectors gives the nonselective
record marginal. If an erasure operation is declared, it is just another
operation word in `\mathcal O_a`; on the controlled pre-record subspace its
amplitude-level inverse property reduces the composed word to the corresponding
coherent word, and any imperfect implementation is accounted for by the
residual-budget theorem. If no erasure operation is declared, no erasure
statistic exists in the operational family. Thus every statistic in the finite
interferometer class is recovered exactly when the required controls are
declared, and is otherwise underdetermined. `square`

### Corollary 6B: phase-incompleteness diagnostic

If `\mathcal O_a` contains only the stochastic kernels of individual gates and
forms interferometer predictions by stochastic composition before amplitude
composition, then it fails the two-path phase benchmark. For example,

```math
|B|^2|P_\phi|^2|B|^2
=
\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},
```

which is independent of `\phi` and therefore cannot reproduce
`\cos^2(\phi/2)`. This is not a failure of the finite record ontology. It is a
failure to declare the coherent control family required for phase-sensitive
physics.

### Measurement lesson

The which-path benchmark does not introduce a collapse law. It introduces a
different physical operation: a record-writing coupling between the two beam
splitters. After that operation, conditioning on `d_0` or `d_1` is ordinary
conditioning on a record. Ignoring the record gives the nonselective mixture.

Thus Paper 4 has two separate obligations:

1. **definite outcome obligation:** prove records, conditioning, repeatability,
   and reset inside finite stochastic dynamics;
2. **phase recovery obligation:** include enough controlled kernels and
   detector couplings in `\mathcal O_a` to reproduce coherent interference,
   which-path decoherence, and, where relevant, coherent erasure controls.

This benchmark says exactly what Paper 4 must not hide:

1. definite detector records and conditioning address the finite definite-outcome
   part of the measurement problem;
2. a single unlabelled endpoint kernel does not reconstruct the coherent
   control family;
3. phase-sensitive physics is recovered only if the ISP operational data
   include enough controlled kernels and detector couplings.

## 9. Locality Transfer

This is the first bridge from Paper 3 to operational statistics. The theorem is
conditional because Paper 3 controls raw or calibrated relative maps, while
experiments see matrix elements against declared preparations and effects.

Let `\mathcal A_{\mu,R}^{\mathrm{anch}}` denote one of the anchored
quasilocal norms exported by Paper 3, with decay rate `\mu` and anchor collar
`R`.

### Remote test pairs

Fix `0<\nu<\mu`. A preparation/effect pair `(p,e)` is
`(R,d,\nu,C_{\mathrm{test}})`-remote relative to the reference channel
`\Gamma_0` if, for every anchored defect

```math
A\in\mathcal A_{\mu,R}^{\mathrm{anch}},
```

the tested matrix element obeys

```math
\left|
e^TA\Gamma_0p
\right|
\le
C_{\mathrm{test}}(e,p)\,
\|A\|_{\mathcal A_{\mu,R}^{\mathrm{anch}}}
e^{-\nu d}.
```

This definition packages the support/cylinder-effect hypothesis honestly. In a
concrete lattice model it should be proved from the anchored tree-polymer norm,
the support of `e`, the preparation class, and the reference light-cone/tail
bound. It is not a consequence of positivity alone.

### Lemma 7: cylinder effects are remote for the tree norm

Use the anchored tree-polymer norm of Paper 3. Let `T` be a final-time cell
region and let `e` be a cylinder effect supported in `T`, with

```math
0\le e\le1.
```

Define the anchored distance from the collar to `T` by

```math
d_R(T)
:=
\inf\{\ell_R(X):X\cap T\ne\emptyset\},
```

where `\ell_R(X)` is the Paper 3 tree length from the collar scaffold to the
local support `X`. Then for every normalized positive `q\in\Delta(V_1)` and
every anchored defect `A\in\mathcal A_{\mu,R}^{\mathrm{tree}}`,

```math
\left|e^TAq\right|
\le
e^{-\mu d_R(T)}
\|A\|_{\mu,R}^{\mathrm{tree}}.
```

Consequently, for every preparation `p`, the pair `(p,e)` is remote relative
to `\Gamma_0` with `q=\Gamma_0p`, `C_{\mathrm{test}}=1`, and any decay
`\nu\le\mu`:

```math
\left|e^TA\Gamma_0p\right|
\le
\|A\|_{\mu,R}^{\mathrm{tree}}e^{-\nu d_R(T)}.
```

Proof. Choose a local decomposition

```math
A=\sum_XA_X
```

with each `A_X` supported in `X` and having zero column sums. If `X\cap T` is
empty, then `e` is constant on the coordinates changed by `A_X`. Since `A_X`
has zero column sums,

```math
e^TA_Xq=0.
```

If `X\cap T` is nonempty, the local induced column-sum norm gives

```math
\left|e^TA_Xq\right|
\le
\|A_X\|_{1,X},
```

because `0\le e\le1` and `q` has total mass one. Therefore

```math
\left|e^TAq\right|
\le
\sum_{X:X\cap T\ne\emptyset}\|A_X\|_{1,X}
\le
e^{-\mu d_R(T)}
\sum_Xe^{\mu\ell_R(X)}\|A_X\|_{1,X}.
```

Taking the infimum over all decompositions gives the stated tree-norm bound.
`square`

This lemma is the concrete reason the transfer theorem is not merely formal.
An anchored defect can affect a remote cylinder effect only through polymer
pieces whose tree support reaches that effect, and those pieces pay the
exponential tree cost.

The zero-column-sum condition is essential. Individual outcome maps can change
the total weight assigned to an outcome near `R`; if the reference state has
long-range correlations, that local reweighting can correlate with a remote
effect. Thus Lemma 7 applies directly to nonselective channel differences and
other zero-column-sum calibrated defects. For selective outcome maps, one must
either use the abstract remote-pair condition above, prove a clustering bound
for the reference preparation, or work with centered/covariance statistics.

### Theorem 8: calibrated locality transfer

Let `\mathsf I_{\lambda,\rho,o}` and
`\mathsf I_{\lambda,\rho,o}^{(0)}` be two operational outcome maps on the same
slab, with calibrated responses

```math
\mathscr J_{\lambda,\rho,o}
:=
\mathsf I_{\lambda,\rho,o}\Gamma_0^{-1},
\qquad
\mathscr J_{\lambda,\rho,o}^{(0)}
:=
\mathsf I_{\lambda,\rho,o}^{(0)}\Gamma_0^{-1}.
```

Assume their calibrated difference has an anchored controlled part
`A_{\lambda,\rho,o}` and a calibration residual
`B_{\lambda,\rho,o}`:

```math
\mathscr J_{\lambda,\rho,o}
-
\mathscr J_{\lambda,\rho,o}^{(0)}
=
A_{\lambda,\rho,o}
+
B_{\lambda,\rho,o},
\qquad
A_{\lambda,\rho,o}\in\mathcal A_{\mu,R}^{\mathrm{anch}}.
```

For a test pair `(p,e)`, define the scalar calibration error

```math
\varepsilon_{\mathrm{cal}}(e,p;\lambda,\rho,o)
:=
\left|
e^TB_{\lambda,\rho,o}\Gamma_0p
\right|.
```

If `(p,e)` is `(R,d,\nu,C_{\mathrm{test}})`-remote, then

```math
\left|
e^T
\left(
\mathsf I_{\lambda,\rho,o}
-
\mathsf I_{\lambda,\rho,o}^{(0)}
\right)p
\right|
\le
C_{\mathrm{test}}(e,p)
\|A_{\lambda,\rho,o}\|_{\mathcal A_{\mu,R}^{\mathrm{anch}}}
e^{-\nu d}
+
\varepsilon_{\mathrm{cal}}(e,p;\lambda,\rho,o).
```

Proof. Since

```math
\mathsf I_{\lambda,\rho,o}
-
\mathsf I_{\lambda,\rho,o}^{(0)}
=
\left(
\mathscr J_{\lambda,\rho,o}
-
\mathscr J_{\lambda,\rho,o}^{(0)}
\right)\Gamma_0,
```

we have

```math
e^T
\left(
\mathsf I_{\lambda,\rho,o}
-
\mathsf I_{\lambda,\rho,o}^{(0)}
\right)p
=
e^TA_{\lambda,\rho,o}\Gamma_0p
+
e^TB_{\lambda,\rho,o}\Gamma_0p.
```

Apply the remote-pair estimate to the anchored term and the definition of
`\varepsilon_{\mathrm{cal}}` to the residual. `square`

### Corollary 9: exact calibrated transfer

If the calibrated residual vanishes on the tested pair, then

```math
\left|
e^T
\left(
\mathsf I_{\lambda,\rho,o}
-
\mathsf I_{\lambda,\rho,o}^{(0)}
\right)p
\right|
\le
C_{\mathrm{test}}(e,p)
\|A_{\lambda,\rho,o}\|_{\mathcal A_{\mu,R}^{\mathrm{anch}}}
e^{-\nu d}.
```

If Paper 3 supplies

```math
\|A_{\lambda,\rho,o}\|_{\mathcal A_{\mu,R}^{\mathrm{anch}}}
\le
C_A\Delta^k,
```

then the operational statistic has the finite-slab locality bound

```math
O\!\left(\Delta^k e^{-\nu d}\right)
```

on all remote test pairs with uniform `C_{\mathrm{test}}`.

### Theorem 10: detector-compression criterion

The remaining model-building problem is to show that a realizable detector
coupling has an anchored calibrated response. A sufficient finite criterion is
available at the enlarged system-detector level.

Let

```math
\widetilde V_i:=V_i\otimes W_\lambda,
\qquad
\widetilde\Gamma_0:=\Gamma_0\otimes I_{W_\lambda},
```

and define the enlarged calibrated response

```math
\widetilde{\mathscr J}_\lambda
:=
\Gamma_{\lambda,D}\widetilde\Gamma_0^{-1}.
```

For a reference detector coupling `\Gamma_{\lambda,D}^{(0)}` define
`\widetilde{\mathscr J}_\lambda^{(0)}` similarly. Let

```math
\widetilde A_\lambda
:=
\widetilde{\mathscr J}_\lambda
-
\widetilde{\mathscr J}_\lambda^{(0)}.
```

For a detector ready state `\eta_\lambda` and readout effect
`\xi_{\lambda,\rho,o}`, define local compression maps

```math
E_{\eta_\lambda}q:=q\otimes\eta_\lambda,
\qquad
C_{\xi_{\lambda,\rho,o}}\widetilde q
:=
\left(I_1\otimes\xi_{\lambda,\rho,o}\right)\widetilde q.
```

Then the compressed calibrated response difference is

```math
\mathscr J_{\lambda,\rho,o}
-
\mathscr J_{\lambda,\rho,o}^{(0)}
=
C_{\xi_{\lambda,\rho,o}}\,
\widetilde A_\lambda\,
E_{\eta_\lambda}.
```

Assume the detector cells are included in the bounded collar scaffold of `R`.
If `\widetilde A_\lambda` has an enlarged anchored tree decomposition with
norm

```math
\|\widetilde A_\lambda\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}},
```

then the compressed response is anchored on the system with

```math
\left\|
\mathscr J_{\lambda,\rho,o}
-
\mathscr J_{\lambda,\rho,o}^{(0)}
\right\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
\le
C_D
\|\widetilde A_\lambda\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}},
```

where `C_D` depends only on the finite detector readout norm and the bounded
collar scaffold. Here `\mathcal A_{\mu,R}^{\mathrm{tree,op}}` denotes the
same weighted local tree norm as Paper 3, but without imposing zero column
sums on the compressed local pieces. For normalized positive `\eta_\lambda`
and detector effects `0\le\xi_{\lambda,\rho,o}\le1_{D_\lambda}^T`, one may
take `C_D=1` if the detector cells are counted as part of the anchor.

Proof. The identity follows by substitution:

```math
\mathscr J_{\lambda,\rho,o}q
=
\left(I_1\otimes\xi_{\lambda,\rho,o}\right)
\Gamma_{\lambda,D}(\Gamma_0^{-1}q\otimes\eta_\lambda)
=
C_{\xi_{\lambda,\rho,o}}
\widetilde{\mathscr J}_\lambda
E_{\eta_\lambda}q,
```

and similarly for the reference coupling. For the norm bound, decompose
`\widetilde A_\lambda=\sum_Y\widetilde A_Y` into enlarged local pieces. The
compressed piece

```math
C_{\xi_{\lambda,\rho,o}}\widetilde A_YE_{\eta_\lambda}
```

is supported on the system projection of `Y`, with the detector cells absorbed
into the bounded anchor scaffold. The local induced column-sum norm is
contracted by `E_{\eta_\lambda}` and `C_{\xi_{\lambda,\rho,o}}` up to the
constant `C_D`. The tree length does not increase except by the same bounded
scaffold convention. Summing over the decomposition and taking the infimum
gives the claimed bound. `square`

### Proposition 10A: local write-register detector anchoring

The abstract detector-compression criterion is not empty. It is satisfied by a
minimal finite detector benchmark: a bounded local write-register coupled to the
system after the reference slab.

Assume, for this benchmark, that final system configurations split as

```math
C_1=C_R\times C_{\bar R},
\qquad
V_1=\mathbb R^{C_1}.
```

Let the detector register have outcome cells

```math
D_R=O,
\qquad
D_{R,o}=\{o\},
\qquad
W_R=\mathbb R^O.
```

For each outcome `o`, choose a positive local substochastic matrix

```math
M_o:\mathbb R^{C_R}\to\mathbb R^{C_R},
\qquad
M_o(y_R|x_R)\ge0,
```

with normalized total local channel

```math
\sum_{o\in O}\sum_{y_R\in C_R}M_o(y_R|x_R)=1
\qquad
\text{for every }x_R\in C_R.
```

Define the enlarged local write map

```math
W_R:V_1\otimes W_R\to V_1\otimes W_R
```

by

```math
(W_R\widetilde q)(y_R,x_{\bar R},o)
:=
\sum_{x_R\in C_R}\sum_{d\in O}
M_o(y_R|x_R)\,
\widetilde q(x_R,x_{\bar R},d).
```

Then `W_R` is stochastic, ignores the previous detector cell, writes the new
record `o`, and is supported only on `R` together with the detector register.
Let

```math
\Gamma_{R,D}^{\mathrm{wr}}
:=
W_R(\Gamma_0\otimes I_{W_R}),
\qquad
\Gamma_{R,D}^{\mathrm{idle}}
:=
\Gamma_0\otimes I_{W_R}.
```

With the enlarged reference

```math
\widetilde\Gamma_0=\Gamma_0\otimes I_{W_R},
```

the enlarged calibrated write response is

```math
\widetilde{\mathscr J}_{R}^{\mathrm{wr}}
=
\Gamma_{R,D}^{\mathrm{wr}}\widetilde\Gamma_0^{-1}
=W_R,
```

while the idle detector response is

```math
\widetilde{\mathscr J}_{R}^{\mathrm{idle}}
=
\Gamma_{R,D}^{\mathrm{idle}}\widetilde\Gamma_0^{-1}
=I.
```

Therefore

```math
\widetilde A_R
:=
\widetilde{\mathscr J}_{R}^{\mathrm{wr}}
-
\widetilde{\mathscr J}_{R}^{\mathrm{idle}}
=
W_R-I.
```

This defect has zero column sums and is an enlarged anchored tree defect. If
the detector cells are counted as part of the collar anchor, then

```math
\|\widetilde A_R\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}}
\le
\|W_R-I\|_{1,R\cup D_R}
\le2.
```

More generally, if the detector register sits at bounded tree distance `r_D`
from the collar scaffold, then

```math
\|\widetilde A_R\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}}
\le
2e^{\mu r_D}.
```

For a tunable weak-to-strong marker

```math
W_R(s):=(1-s)I+sW_R,
\qquad
0\le s\le1,
```

the same bound improves to

```math
\|W_R(s)-I\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}}
\le
2s e^{\mu r_D}.
```

Only `s=1` is the exact overwrite detector above. Values `s<1` are useful as a
controlled weak-marker interpolation for coupling-onset tests.

For the sharp detector readout `\xi_o=\delta_o^T` and any normalized ready
state `\eta_R`, compression gives the explicit system operation

```math
\mathsf I_{R,o}^{\mathrm{wr}}p
=
\left(M_o\otimes I_{\bar R}\right)\Gamma_0p.
```

Thus the local write-register benchmark has a positive normalized instrument,
exact record sectors, exact reset by `\mathcal R_{\eta_R}`, and an anchored
calibrated response satisfying Theorem 10 with `C_D=1` when the detector is
included in the collar anchor.

If the local readout is nondisturbing,

```math
M_o(y_R|x_R)=m_o(x_R)\delta_{y_R,x_R},
\qquad
\sum_o m_o(x_R)=1,
```

then the nonselective system channel is exactly the reference channel:

```math
\sum_o\mathsf I_{R,o}^{\mathrm{wr}}=\Gamma_0.
```

In that case the detector creates selective record statistics but no
nonselective system disturbance. Selective outcome maps may still correlate
with remote effects through the reference state, so the remote-pair or
clustering hypotheses of Section 9 are still needed for selective locality.

Proof. Positivity of `W_R` is immediate from positivity of the matrices `M_o`.
For each input column `(x_R,x_{\bar R},d)`, the total output mass is

```math
\sum_{o,y_R}M_o(y_R|x_R)=1,
```

so `W_R` is stochastic. The formula
`\Gamma_{R,D}^{\mathrm{wr}}=W_R\widetilde\Gamma_0` gives
`\widetilde{\mathscr J}_{R}^{\mathrm{wr}}=W_R` by multiplication with
`\widetilde\Gamma_0^{-1}`. Since both `W_R` and `I` are stochastic,
`1^T(W_R-I)=0`.

The support is contained in `R\cup D_R`: outside `R`, the coordinate
`x_{\bar R}` is copied unchanged. Hence the anchored decomposition has a single
local piece `W_R-I`. In induced column-sum norm, two stochastic columns can
differ by at most `2`, giving the displayed bound; the factor `e^{\mu r_D}`
only records the convention in which detector cells are not absorbed into the
anchor. The bound for `W_R(s)` follows by homogeneity.

Finally,

```math
\begin{aligned}
\mathsf I_{R,o}^{\mathrm{wr}}p
&=
\left(I_1\otimes\delta_o^T\right)
W_R(\Gamma_0p\otimes\eta_R)
\\
&=
\left(M_o\otimes I_{\bar R}\right)\Gamma_0p,
\end{aligned}
```

because `\sum_d\eta_R(d)=1`. Theorem 1 gives the positive normalized
instrument and exact record-sector support. The reset statement is the
stochastic reset map of Section 4. In the nondisturbing case,
`\sum_oM_o=I_{C_R}`, hence the nonselective compressed channel is
`\Gamma_0`. `square`

### Theorem 10B: finite-depth local detector anchoring

The write-register benchmark is the smallest exact model. A more realistic
finite detector may have local propagation, amplification, memory stabilization,
thresholding, and readout gates before the final record is inspected. These
features still satisfy the anchored-response hypothesis when their finite-depth
influence region remains inside a bounded collar scaffold.

Let the enlarged final space be

```math
\widetilde V_1:=V_1\otimes W_\lambda,
```

where the detector cells in `W_\lambda` are embedded in a finite scaffold near
`R`. Assume the actual detector operation after the reference slab factors as a
finite product of local stochastic gates

```math
\mathcal D_\lambda
=
G_mG_{m-1}\cdots G_1
```

and the reference detector operation factors on the same hardware as

```math
\mathcal D_\lambda^{(0)}
=
G_m^{(0)}G_{m-1}^{(0)}\cdots G_1^{(0)}.
```

Each `G_j` and `G_j^{(0)}` is stochastic, acts as the identity outside a finite
system-detector support `Y_j`, and has the same support convention. Let

```math
H_\lambda:=\bigcup_{j=1}^mY_j,
\qquad
r_\lambda:=\ell_R(H_\lambda)
```

be the total detector hardware support and its anchored tree length. Define the
local gate discrepancy

```math
\delta_j:=\|G_j-G_j^{(0)}\|_{1,Y_j}.
```

Then, with

```math
\Gamma_{\lambda,D}
:=
\mathcal D_\lambda(\Gamma_0\otimes I_{W_\lambda}),
\qquad
\Gamma_{\lambda,D}^{(0)}
:=
\mathcal D_\lambda^{(0)}(\Gamma_0\otimes I_{W_\lambda}),
```

the enlarged calibrated difference is

```math
\widetilde A_\lambda
:=
\Gamma_{\lambda,D}\widetilde\Gamma_0^{-1}
-
\Gamma_{\lambda,D}^{(0)}\widetilde\Gamma_0^{-1}
=
\mathcal D_\lambda-\mathcal D_\lambda^{(0)}.
```

It is an enlarged anchored tree defect and satisfies

```math
\|\widetilde A_\lambda\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}}
\le
e^{\mu r_\lambda}\sum_{j=1}^m\delta_j.
```

Consequently every compressed operational outcome map obeys

```math
\left\|
\mathscr J_{\lambda,\rho,o}
-
\mathscr J_{\lambda,\rho,o}^{(0)}
\right\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
\le
C_D
e^{\mu r_\lambda}\sum_{j=1}^m\delta_j,
```

with the same detector-compression constant `C_D` as in Theorem 10. If the
detector cells and readout effects are counted as part of the anchor and
`0\le\xi_{\lambda,\rho,o}\le1_{D_\lambda}^T`, one may take `C_D=1`.

In particular, if the detector architecture has uniform finite range/depth
control

```math
r_\lambda\le r_*,
\qquad
\sum_{j=1}^m\delta_j\le B_D,
```

then

```math
\|\widetilde A_\lambda\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}}
\le
B_D e^{\mu r_*},
```

uniformly in the total volume of the ambient lattice. A cruder but useful
bounded-hardware estimate is

```math
\|\widetilde A_\lambda\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}}
\le
2m_* e^{\mu(r_D+v_D h_D)},
```

when there are at most `m_*` gates, each gate differs from its reference by at
most `2`, the detector scaffold begins at anchored distance `r_D`, each layer
expands influence by at most `v_D`, and the detector circuit depth is `h_D`.

Proof. The calibrated identity follows because
`\widetilde\Gamma_0=\Gamma_0\otimes I_{W_\lambda}` and the detector gates are
applied after the reference slab. Hence

```math
\Gamma_{\lambda,D}\widetilde\Gamma_0^{-1}
=
\mathcal D_\lambda,
\qquad
\Gamma_{\lambda,D}^{(0)}\widetilde\Gamma_0^{-1}
=
\mathcal D_\lambda^{(0)}.
```

Use the product telescoping identity

```math
\mathcal D_\lambda-\mathcal D_\lambda^{(0)}
=
\sum_{j=1}^m
G_m\cdots G_{j+1}
\left(G_j-G_j^{(0)}\right)
G_{j-1}^{(0)}\cdots G_1^{(0)}.
```

The `j`th summand is supported inside the total detector hardware support
`H_\lambda`, because every surrounding gate acts as the identity outside
`H_\lambda`. Since all surrounding gates are stochastic, they are contractions in
induced column-sum norm, so the local norm of the `j`th summand is at most
`\delta_j`. Since `G_j` and `G_j^{(0)}` are stochastic,
`1^T(G_j-G_j^{(0)})=0`; multiplying on the left and right by stochastic gates
preserves zero column sum for the nonselective enlarged defect. Weighting the
`j`th piece by `e^{\mu r_\lambda}` and summing gives the displayed anchored
tree-norm bound. The compressed bound is Theorem 10. The uniform estimates
follow by substituting the stated bounds on `r_\lambda` and the discrepancies.
`square`

This theorem is intentionally finite. It says that amplification does not by
itself break anchoring; it only increases the explicit constants through the
number of gates and the hardware influence radius. If a detector has unbounded
depth, uncontrolled propagation, or a macroscopic number of uncompensated
discrepant gates, the theorem does not provide a uniform locality constant.

When the terminal memory cells of this finite-depth architecture are partitioned
into disjoint record sectors, Theorem 1 supplies the positive normalized
instrument. Theorem 10B supplies the separate locality ingredient: the calibrated
detector response is anchored. Record stability, repeatability, and leakage
still have to be checked by the Section 4 diagnostics for the particular memory
implementation.

### Corollary 11: nonselective detector locality

Let

```math
\mathsf I_\lambda:=\sum_{o\in O_{\lambda,\rho}}\mathsf I_{\lambda,\rho,o}
```

be a nonselective channel for a fixed readout scheme, and define

```math
\mathscr J_\lambda:=\mathsf I_\lambda\Gamma_0^{-1}.
```

If the enlarged nonselective calibrated difference is a zero-column-sum
anchored tree defect with

```math
\|\widetilde A_\lambda\|_{\widetilde{\mathcal A}_{\mu,R}^{\mathrm{tree}}}
\le
C_A\Delta^k,
```

then for every final cylinder effect `e` supported in `T` and every
preparation `p`,

```math
\left|
e^T
\left(
\mathsf I_\lambda-\mathsf I_\lambda^{(0)}
\right)p
\right|
\le
C_D C_A\Delta^k e^{-\mu d_R(T)}.
```

Proof. Apply Theorem 10 with the unit detector readout
`\sum_o\xi_{\lambda,\rho,o}=1_{D_\lambda}^T`, so the compressed nonselective
difference remains zero-column-sum. Then apply Lemma 7 and the calibration
identity of Theorem 8. `square`

This is the central Paper 4 proof chain in finite form:

```text
enlarged detector anchored response
-> compressed calibrated response
-> remote/cylinder statistic bound
-> operational locality.
```

For individual selective outcomes, the same compression identity holds, but
remote locality also requires the remote-pair/clustering hypothesis because an
outcome event near `R` may be statistically correlated with remote final
effects.

### Theorem 11A: centered selective-outcome locality

Selective outcomes are not no-signaling statements. They can be correlated with
remote effects even in standard quantum theory. The local statement that can be
controlled is the **centered** selective statistic.

Let

```math
q:=\Gamma_0p,
\qquad
m_e:=e^Tq,
\qquad
\bar e_q^T:=e^T-m_e1^T.
```

For a selective calibrated response `\mathscr J_o`, define

```math
\operatorname{Cov}_{\mathscr J_o}(e;p)
:=
\bar e_q^T\mathscr J_o q
=
e^T\mathsf I_o p
-
(e^T\Gamma_0p)(1^T\mathsf I_o p).
```

This is the connected correlation between the local outcome event `o` and the
remote effect `e`, measured relative to the reference final state `q`.

Assume two selective response maps satisfy

```math
\mathscr J_o-\mathscr J_o^{(0)}
=
A_o+B_o,
```

where `A_o` has an anchored operational tree decomposition

```math
A_o=\sum_XA_{o,X},
\qquad
\|A_o\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}<\infty,
```

and `B_o` is the calibration residual. Let `e` be a final cylinder effect
supported in a region `T`, with `0\le e\le1`. Suppose the reference final state
`q` satisfies the selective clustering estimate: for some `0<\nu\le\mu` and
constant `C_{\mathrm{cl}}\ge1`, every local operator `A_X` supported in `X`
obeys

```math
\left|
\bar e_q^T A_X q
\right|
\le
C_{\mathrm{cl}}
\|A_X\|_{1,X}
e^{-\nu d(X,T)}
```

where the tree distances obey

```math
d_R(T)\le\ell_R(X)+d(X,T).
```

Define the centered calibration residual

```math
\varepsilon_{\mathrm{cent}}(e,p;o)
:=
\left|
\bar e_q^T B_o q
\right|.
```

Then

```math
\left|
\operatorname{Cov}_{\mathscr J_o}(e;p)
-
\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)
\right|
\le
C_{\mathrm{cl}}
\|A_o\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
e^{-\nu d_R(T)}
+
\varepsilon_{\mathrm{cent}}(e,p;o).
```

If Paper 3 or a detector benchmark gives

```math
\|A_o\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
\le
C_A\Delta^k,
```

then the centered selective statistic obeys

```math
O\!\left(\Delta^ke^{-\nu d_R(T)}\right)
+
\varepsilon_{\mathrm{cent}}.
```

Proof. The centered covariance difference is

```math
\bar e_q^T(\mathscr J_o-\mathscr J_o^{(0)})q
=
\bar e_q^T A_o q+\bar e_q^T B_o q.
```

For the anchored part, use the decomposition and the clustering estimate:

```math
\begin{aligned}
\left|\bar e_q^T A_o q\right|
&\le
\sum_X
C_{\mathrm{cl}}
\|A_{o,X}\|_{1,X}
e^{-\nu d(X,T)}
\\
&\le
C_{\mathrm{cl}}e^{-\nu d_R(T)}
\sum_X
e^{\nu\ell_R(X)}
\|A_{o,X}\|_{1,X}
\\
&\le
C_{\mathrm{cl}}e^{-\nu d_R(T)}
\sum_X
e^{\mu\ell_R(X)}
\|A_{o,X}\|_{1,X}.
\end{aligned}
```

Taking the infimum over anchored decompositions gives the tree-norm term. The
residual is exactly `\varepsilon_{\mathrm{cent}}`. `square`

### Corollary 11B: conditional selective stability

Use the hypotheses of Theorem 11A. Let

```math
p_o:=1^T\mathscr J_o q,
\qquad
p_o^{(0)}:=1^T\mathscr J_o^{(0)}q,
```

and suppose the selected outcome is not rare:

```math
p_o,p_o^{(0)}\ge p_{\min}>0.
```

Define

```math
\varepsilon_{\mathrm{prob}}(p;o)
:=
\left|
1^T(A_o+B_o)q
\right|.
```

Then the conditional remote-effect probabilities satisfy

```math
\left|
\frac{e^T\mathscr J_o q}{p_o}
-
\frac{e^T\mathscr J_o^{(0)}q}{p_o^{(0)}}
\right|
\le
\frac{
C_{\mathrm{cl}}
\|A_o\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
e^{-\nu d_R(T)}
+
\varepsilon_{\mathrm{cent}}(e,p;o)
+
\varepsilon_{\mathrm{prob}}(p;o)
}{p_{\min}}.
```

This is a stability statement for postselected statistics. It is not a
no-signaling theorem: conditioning on a known outcome can reveal ordinary
correlations.

Proof. Write

```math
\frac{e^T\mathscr J_o q}{p_o}
=
m_e+
\frac{\operatorname{Cov}_{\mathscr J_o}(e;p)}{p_o},
```

and similarly for `\mathscr J_o^{(0)}`. Theorem 11A bounds the covariance
difference. Also

```math
\left|p_o-p_o^{(0)}\right|
\le
\varepsilon_{\mathrm{prob}}(p;o).
```

Since `0\le e\le1` and `\mathscr J_o^{(0)}q` is the positive selected state
before normalization,

```math
\left|
\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)
\right|
\le
p_o^{(0)}.
```

Set

```math
\delta_{\mathrm{cov}}
:=
\left|
\operatorname{Cov}_{\mathscr J_o}(e;p)
-
\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)
\right|.
```

Then

```math
\left|
\frac{\operatorname{Cov}_{\mathscr J_o}(e;p)}{p_o}
-
\frac{\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)}{p_o^{(0)}}
\right|
\le
\frac{\delta_{\mathrm{cov}}}{p_{\min}}
+
\frac{\varepsilon_{\mathrm{prob}}(p;o)}{p_{\min}}.
```

Insert the bound on `\delta_{\mathrm{cov}}` from Theorem 11A. `square`

### Theorem 11C: screened selective locality

The preceding corollary is useful, but its hypothesis is still phrased through a
centered covariance estimate. The operational sufficient condition is
**screening**: after the local outcome is formed, its connected correlation with
a remote test must be certified small, and the outcome probability must be
stable enough that postselection does not amplify a residual into a signal.

Use the notation of Theorem 11A and Corollary 11B. For a preparation `p`, let

```math
q:=\Gamma_0p,
\qquad
m_e:=e^Tq,
```

and define the conditional remote statistics

```math
E_o(e;p):=\frac{e^T\mathscr J_o q}{p_o},
\qquad
E_o^{(0)}(e;p):=\frac{e^T\mathscr J_o^{(0)}q}{p_o^{(0)}}.
```

Say that the outcome `o` is **screened from the remote test** `(e,T)` on the
state `p` with constants `p_{\min}`, `\eta_{\mathrm{scr}}`, and
`\varepsilon_{\mathrm{prob}}` when

```math
p_o,p_o^{(0)}\ge p_{\min}>0,
```

```math
\left|
\operatorname{Cov}_{\mathscr J_o}(e;p)
-
\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)
\right|
\le
\eta_{\mathrm{scr}}(e,p;o),
```

and

```math
\left|p_o-p_o^{(0)}\right|
\le
\varepsilon_{\mathrm{prob}}(p;o).
```

Then the postselected remote statistics obey

```math
\left|
E_o(e;p)-E_o^{(0)}(e;p)
\right|
\le
\frac{
\eta_{\mathrm{scr}}(e,p;o)
+
\varepsilon_{\mathrm{prob}}(p;o)
}{p_{\min}}.
```

In particular, the hypotheses of Theorem 11A provide a screening certificate

```math
\eta_{\mathrm{scr}}(e,p;o)
\le
C_{\mathrm{cl}}
\|A_o\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
e^{-\nu d_R(T)}
+
\varepsilon_{\mathrm{cent}}(e,p;o).
```

If Theorem 10B supplies the detector anchoring estimate

```math
\|A_o\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
\le
C_D e^{\mu r_\lambda}\sum_j\delta_j,
```

then the conditional selective statistic has the explicit finite-depth detector
bound

```math
\left|
E_o(e;p)-E_o^{(0)}(e;p)
\right|
\le
\frac{
C_{\mathrm{cl}}C_D e^{\mu r_\lambda}
\left(\sum_j\delta_j\right)
e^{-\nu d_R(T)}
+
\varepsilon_{\mathrm{cent}}(e,p;o)
+
\varepsilon_{\mathrm{prob}}(p;o)
}{p_{\min}}.
```

Proof. By definition of the centered covariance,

```math
E_o(e;p)
=
m_e+
\frac{\operatorname{Cov}_{\mathscr J_o}(e;p)}{p_o},
\qquad
E_o^{(0)}(e;p)
=
m_e+
\frac{\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)}{p_o^{(0)}}.
```

Therefore

```math
\begin{aligned}
\left|E_o(e;p)-E_o^{(0)}(e;p)\right|
&\le
\frac{
\left|
\operatorname{Cov}_{\mathscr J_o}(e;p)
-
\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)
\right|
}{p_{\min}}
\\
&\quad+
\left|\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)\right|
\left|
\frac1{p_o}-\frac1{p_o^{(0)}}
\right|.
\end{aligned}
```

Since `0\le e\le1` and `\mathscr J_o^{(0)}q` is a positive selected state,

```math
\left|\operatorname{Cov}_{\mathscr J_o^{(0)}}(e;p)\right|
\le p_o^{(0)}.
```

The second term is therefore bounded by
`\varepsilon_{\mathrm{prob}}(p;o)/p_{\min}`. The first term is the screening
bound. The displayed anchored and finite-depth estimates follow by substituting
Theorem 11A and Theorem 10B. `square`

This theorem is the precise selective-outcome message. A postselected statistic
is local only after a screening certificate and an outcome floor are supplied.
Without screening, postselection can reveal ordinary long-range correlations and
no locality conclusion follows.

### Proposition 11D: calibration residual budget

Every operational theorem above has the same logical form:

```text
observable statistic = controlled structural term + declared residuals.
```

The residuals are not cosmetic. They are the boundary between a real ISP
prediction and a detector/calibration artifact. The following ledger fixes the
bookkeeping used in the rest of the paper.

| Symbol | First use | What it measures |
| --- | --- | --- |
| `\ell_o(\widehat q)` | Proposition 2 | mass already outside the selected record sector |
| `\epsilon_o(\Theta_R)` | Proposition 2 | instability of an immediate repeat readout |
| `\varepsilon_{\mathrm{cal}}` | Theorem 8 | scalar effect of a calibrated-response residual on a tested pair |
| `C_D` | Theorem 10 | detector-compression norm loss from enlarged to compressed response |
| `\delta_j` | Theorem 10B | local gate discrepancy in a finite-depth detector architecture |
| `B_D` | Theorem 10B | summed finite-depth detector discrepancy controlling uniform anchoring |
| `\varepsilon_{\mathrm{cent}}` | Theorem 11A | centered selective-outcome calibration residual |
| `\varepsilon_{\mathrm{prob}}` | Corollary 11B | selected-outcome probability residual |
| `\eta_{\mathrm{scr}}` | Theorem 11C | screened connected-correlation bound for postselected locality |
| `\varepsilon_{\mathrm{ex}}` | Theorem 13 | difference between operational and raw exchange commutators |
| `\epsilon_{\mathrm{ker}}` | Theorem 19 | enlarged-kernel refinement mismatch |
| `\epsilon_{\mathrm{rec}}` | Theorem 19 | detector record-sector refinement mismatch |
| `\bar\epsilon_\eta` | Theorem 19B | ready-state mismatch after lossy detector extension |
| `\bar\epsilon_{\mathrm{ker}}` | Theorem 19B | enlarged-kernel mismatch with explicit loss record |
| `\bar\epsilon_{\mathrm{rec}}` | Theorem 19B | record-sector mismatch with explicit loss record |
| `\epsilon_{\mathrm{surv}}` | Theorem 19B | survival-probability mismatch when loss records are discarded |
| `\varepsilon_{\mathrm{det}}` | Section 13 | empirical detector/order/timing bias in a proposed experiment |
| `\varepsilon_{\mathrm{sys}}` | Section 13 | aggregate systematic uncertainty after calibration |

For a tested scalar statistic `S(e,p)` define an ideal structural prediction
`S_{\mathrm{str}}(e,p)` and a null or reference prediction
`S_{\mathrm{ref}}(e,p)`. A calibration model is acceptable only after it gives a
finite list of scalar residual bounds

```math
\left|\delta_i(e,p)\right|\le\varepsilon_i(e,p).
```

Then the operational prediction has the certified form

```math
\left|
S(e,p)-S_{\mathrm{str}}(e,p)
\right|
\le
\varepsilon_{\mathrm{op}}(e,p),
\qquad
\varepsilon_{\mathrm{op}}(e,p):=\sum_i\varepsilon_i(e,p).
```

If the statistic is experimental, the comparison uncertainty is

```math
\varepsilon_{\mathrm{tot}}(e,p)^2
:=
\sigma_{\mathrm{stat}}(e,p)^2
+
\varepsilon_{\mathrm{sys}}(e,p)^2
+
\varepsilon_{\mathrm{op}}(e,p)^2.
```

A measured deviation from the reference is therefore interpretable as a
structural ISP term only if

```math
\left|
S_{\mathrm{obs}}(e,p)-S_{\mathrm{ref}}(e,p)
\right|
\gg
\varepsilon_{\mathrm{tot}}(e,p)
```

and its sign, support, coupling-order, distance, refinement, or record-threshold
dependence matches the structural term. Otherwise the honest conclusion is

```text
bounded residual, not new physics.
```

For the theorems in this paper the concrete instantiations are:

| Statistic | Structural term | Operational residual |
| --- | --- | --- |
| Locality transfer | anchored tree tail | `\varepsilon_{\mathrm{cal}}` |
| Finite-depth detector anchoring | `C_D e^{\mu r_\lambda}\sum_j\delta_j` | architecture/gate discrepancy bound |
| Nonselective detector locality | `C_D C_A\Delta^k e^{-\mu d_R(T)}` | detector-compression/model error |
| Centered selective locality | `C_{\mathrm{cl}}\|A_o\|e^{-\nu d_R(T)}` | `\varepsilon_{\mathrm{cent}}` |
| Conditional selective stability | centered bound divided by `p_{\min}` | `(\varepsilon_{\mathrm{cent}}+\varepsilon_{\mathrm{prob}})/p_{\min}` |
| Screened selective locality | `\eta_{\mathrm{scr}}/p_{\min}` | `\varepsilon_{\mathrm{prob}}/p_{\min}` |
| Operational exchange | `C_{\mathrm{corr}}\|E_{R,S}-I\|` | `\varepsilon_{\mathrm{ex}}` |
| Approximate no-signaling | commutator/exchange bound | `\varepsilon_{\mathrm{ex}}(1,p;R,S)` |
| Projective transfer | exact coarse statistic | `\epsilon_{\mathrm{ker}}+\epsilon_{\mathrm{rec}}` |
| Lossy projective transfer | explicit loss-record statistic | `\bar\epsilon_{\mathrm{ker}}+\bar\epsilon_{\mathrm{rec}}+\bar\epsilon_\eta` |
| Record repeatability | exact repeat record | `\ell_o+\epsilon_o(\Theta_R)` |

Proof. Each theorem writes the tested scalar as a controlled term plus one or
more residual terms. Applying the triangle inequality gives the first bound.
Independent statistical and systematic uncertainties are combined in quadrature
only for experimental comparison; if the errors are not independent, replace the
quadrature definition by the conservative linear sum. The final interpretive
criterion is not a theorem of probability but a falsifiability rule: a claimed
structural term must dominate the certified residual budget and display the
predicted structural scaling. `square`

### Example 11E: finite-depth detector calibration ledger

This example shows how Theorem 10B and Theorem 11C become numbers in a finite
model. It is not a universal detector model. It is a reproducible bookkeeping
template for a declared detector architecture.

Consider a binary threshold detector near `R`. The detector has `n` memory cells
and declares outcome `o=1` if at least `t` cells are excited at the final readout;
otherwise it declares `o=0`. Its stochastic circuit has:

1. a local coupling layer from the system cells in `R` to seed memory cells;
2. `h_D` bounded-range amplification/stabilization layers;
3. a threshold readout map;
4. a reset map tested separately by Proposition 2.

Let the actual gate in layer `j` be `G_j` and the calibrated reference gate be
`G_j^{(0)}`. Suppose gate tomography gives

```math
\delta_j
:=
\|G_j-G_j^{(0)}\|_{1,Y_j}
\le
\delta_{\max,j},
\qquad
\sum_{j=1}^m\delta_{\max,j}=B_D.
```

If the hardware support has anchored radius

```math
r_\lambda\le r_*,
```

Theorem 10B gives the concrete detector-anchoring estimate

```math
\|A_o\|_{\mathcal A_{\mu,R}^{\mathrm{tree,op}}}
\le
C_D e^{\mu r_*}B_D.
```

For threshold readout, a simple repeatability/leakage certificate is obtained by
testing each memory cell for a flip probability at most `q_{\mathrm{flip}}`
between two immediate reads. A union bound gives

```math
\epsilon_o(\Theta_R)
\le
n q_{\mathrm{flip}}.
```

If the final memory distribution puts mass at least `1-\ell_o` in the declared
record sector before readout, Proposition 2 gives the operational repeatability
bound

```math
\Pr(\text{second read differs from }o\mid o)
\le
\ell_o+nq_{\mathrm{flip}}.
```

Outcome-floor calibration is separate. If calibration runs give the reference
outcome probability

```math
p_o^{(0)}\ge p_{\mathrm{floor}},
```

and the probability residual obeys

```math
\varepsilon_{\mathrm{prob}}(p;o)
\le
\varepsilon_p,
```

then the usable postselection denominator is

```math
p_{\min}:=p_{\mathrm{floor}}-\varepsilon_p,
\qquad
p_{\min}>0.
```

For a remote effect `e` supported in `T`, suppose the reference final state
satisfies the clustering estimate of Theorem 11A with constants
`C_{\mathrm{cl}}` and `\nu`. Then the screened connected-correlation constant
can be certified as

```math
\eta_{\mathrm{scr}}(e,p;o)
\le
C_{\mathrm{cl}} C_D e^{\mu r_*}B_D e^{-\nu d_R(T)}
+
\varepsilon_{\mathrm{cent}}(e,p;o).
```

Theorem 11C then gives the postselected remote-statistic bound

```math
\left|E_o(e;p)-E_o^{(0)}(e;p)\right|
\le
\frac{
C_{\mathrm{cl}} C_D e^{\mu r_*}B_D e^{-\nu d_R(T)}
+
\varepsilon_{\mathrm{cent}}(e,p;o)
+
\varepsilon_p
}{p_{\mathrm{floor}}-\varepsilon_p}.
```

As a scale check, take a dimensionless finite model with

```math
m=20,\qquad
\delta_{\max,j}\le10^{-3},
\qquad
B_D\le2\times10^{-2},
```

```math
C_D=C_{\mathrm{cl}}=1,
\qquad
e^{\mu r_*}\le e,
\qquad
\nu d_R(T)\ge6.
```

Then the screened structural term is bounded by

```math
e(2\times10^{-2})e^{-6}
<
1.4\times10^{-4}.
```

If `p_{\mathrm{floor}}=0.10`, `\varepsilon_p=0.005`, and
`\varepsilon_{\mathrm{cent}}\le10^{-4}`, the conditional selective difference is
bounded by roughly

```math
\frac{1.4\times10^{-4}+10^{-4}+5\times10^{-3}}{0.095}
<
5.6\times10^{-2}.
```

This last number is deliberately not impressive: the probability calibration
dominates. Improving `\varepsilon_p` by a factor of ten is more valuable than
making the already-small anchored tail smaller. That is exactly the kind of
experimental design lesson the theorem is meant to expose.

## 10. Operational Exchange

Paper 3 controls the raw exchange curvature

```math
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}.
```

Paper 4 can only speak operationally after choosing realizable instruments.
For fixed readout schemes, let the nonselective channels be

```math
O_R:=O_{\lambda_R,\rho_R},
\qquad
O_S:=O_{\lambda_S,\rho_S},
```

and

```math
\mathsf I_R^{\mathrm{op}}
:=
\sum_{o\in O_R}\mathsf I_{R,o},
\qquad
\mathsf I_S^{\mathrm{op}}
:=
\sum_{o\in O_S}\mathsf I_{S,o}.
```

Define calibrated final-space responses

```math
\mathscr J_R^{\mathrm{op}}
:=
\mathsf I_R^{\mathrm{op}}\Gamma_0^{-1},
\qquad
\mathscr J_S^{\mathrm{op}}
:=
\mathsf I_S^{\mathrm{op}}\Gamma_0^{-1}.
```

The meaningful operational order-difference statistic is

```math
\Delta_{R,S}^{\mathrm{op}}(e,p)
:=
e^T
\left(
\mathscr J_R^{\mathrm{op}}\mathscr J_S^{\mathrm{op}}
-
\mathscr J_S^{\mathrm{op}}\mathscr J_R^{\mathrm{op}}
\right)
\Gamma_0p.
```

This is a statistic only after pairing with an admissible preparation `p` and
effect `e`. The raw exchange defect is not itself an observable.

### Corridor test pairs

For a two-anchor corridor defect `Q`, define a pair `(p,e)` to be
`(R:S,C_{\mathrm{corr}})`-controlled if

```math
\left|
e^TQJ_SJ_R\Gamma_0p
\right|
\le
C_{\mathrm{corr}}(e,p;R,S)
\|Q\|_{\nu,R:S}^{\mathrm{corr}}.
```

This is the exchange analogue of the remote-pair condition in Section 9.

### Lemma 12: outside-window cylinder tests

Let `e` be a cylinder effect supported outside the corridor window
`\operatorname{Corr}_{R,S}(w)`. Let `Q` be a zero-column-sum corridor defect.
Then, for any signed vector `q`,

```math
\left|e^TQq\right|
\le
\|q\|_1
\|Q\|_{>w}^{(1),R:S}.
```

In particular, with `q=J_SJ_R\Gamma_0p`,

```math
\left|e^TQJ_SJ_R\Gamma_0p\right|
\le
M_{SR}(p)\,
\|Q\|_{>w}^{(1),R:S},
\qquad
M_{SR}(p):=\|J_SJ_R\Gamma_0p\|_1.
```

Proof. Decompose `Q=\sum_ZQ_Z` into local zero-column-sum pieces. If `Z` does
not meet the support of `e`, then `e^TQ_Zq=0` because `e` is constant on the
coordinates changed by `Q_Z` and `Q_Z` has zero column sums. If `Z` meets the
support of `e`, then `Z` lies outside the corridor window, so
`\ell_{R:S}(Z)>w`. For those pieces,

```math
\left|e^TQ_Zq\right|\le\|Q_Z\|_{1,Z}\|q\|_1.
```

Sum over the outside-window pieces and take the infimum over decompositions.
`square`

### Theorem 13: operational exchange bound

Assume the operational calibrated responses are related to the raw Paper 3
comparison maps by

```math
\mathscr J_R^{\mathrm{op}}=J_R+\mathcal D_R,
\qquad
\mathscr J_S^{\mathrm{op}}=J_S+\mathcal D_S.
```

Define the exchange calibration residual on the tested pair by

```math
\varepsilon_{\mathrm{ex}}(e,p;R,S)
:=
\left|
e^T
\left(
[\mathscr J_R^{\mathrm{op}},\mathscr J_S^{\mathrm{op}}]
-
[J_R,J_S]
\right)
\Gamma_0p
\right|.
```

Equivalently, the bracketed residual is

```math
[\mathcal D_R,J_S]+[J_R,\mathcal D_S]+[\mathcal D_R,\mathcal D_S].
```

If `(p,e)` is `(R:S,C_{\mathrm{corr}})`-controlled, then

```math
\left|
\Delta_{R,S}^{\mathrm{op}}(e,p)
\right|
\le
C_{\mathrm{corr}}(e,p;R,S)
\|E_{R,S}-I\|_{\nu,R:S}^{\mathrm{corr}}
+
\varepsilon_{\mathrm{ex}}(e,p;R,S).
```

Proof. The exact raw identity is

```math
J_RJ_S-J_SJ_R
=
\left(E_{R,S}-I\right)J_SJ_R,
```

because `E_{R,S}J_SJ_R=J_RJ_S`. Therefore

```math
e^T[J_R,J_S]\Gamma_0p
=
e^T(E_{R,S}-I)J_SJ_R\Gamma_0p.
```

Add and subtract the raw commutator inside
`\Delta_{R,S}^{\mathrm{op}}`, apply the corridor test-pair bound to the raw
term, and use the definition of `\varepsilon_{\mathrm{ex}}` for the
operational calibration residual. `square`

### Corollary 14: outside-window exchange tail

Let `e` be a final cylinder effect supported outside
`\operatorname{Corr}_{R,S}(w)`. Under the calibration decomposition of Theorem
13 and the outside-window test hypothesis of Lemma 12,

```math
\left|
\Delta_{R,S}^{\mathrm{op}}(e,p)
\right|
\le
M_{SR}(p)\,
\|E_{R,S}-I\|_{>w}^{(1),R:S}
+
\varepsilon_{\mathrm{ex}}(e,p;R,S).
```

Here `E_{R,S}-I` is zero-column-sum because each comparison map preserves
column sums. Using Paper 3's exchange-defect corridor/window theorem, if
`\kappa_R,\kappa_S=O(\Delta^2)` and the inverse norms are bounded in the
finite-slab window, then

```math
\left|
\Delta_{R,S}^{\mathrm{op}}(e,p)
\right|
\le
C\,M_{SR}(p)\,
\Delta^4 e^{-\nu(d_{R,S}+w)}
+
\varepsilon_{\mathrm{ex}}(e,p;R,S).
```

If the operational calibration residual is of higher order or vanishes on the
tested pair, this is a genuine operational exchange-curvature prediction.
Otherwise the raw exchange curvature remains hidden behind realization error.

### Corollary 15: coefficient onset

Suppose Paper 3's separated-support onset hypotheses hold:

```math
J_R-I=\sum_{m\ge2}\Delta^mK_{R,m},
\qquad
J_S-I=\sum_{m\ge2}\Delta^mK_{S,m},
```

with coefficient supports propagating at speed `v`. Then the raw exchange
contribution to `\Delta_{R,S}^{\mathrm{op}}` has no coefficient below

```math
n_*=\max\left(4,\left\lceil d_{R,S}/v\right\rceil\right).
```

The operational statistic has the same onset whenever
`\varepsilon_{\mathrm{ex}}(e,p;R,S)=O(\Delta^{n_*})` or smaller. If the
calibration residual starts earlier, the experiment is measuring detector
realization error rather than Paper 3 exchange curvature.

### Exchange-to-experiment pipeline

Theorem 13 is useful only if it is converted into an operational recipe. The
pipeline is:

1. **Raw geometric input.** Choose collar regions `R,S`, a corridor/window, and a
   regulator family. Paper 3 supplies or bounds the raw defect

```math
Q_{R,S}:=E_{R,S}-I.
```

2. **Detector realization.** Choose declared instruments in `\mathcal O_a` and
   prove that their calibrated nonselective responses approximate the raw maps:

```math
\mathscr J_R^{\mathrm{op}}=J_R+\mathcal D_R,
\qquad
\mathscr J_S^{\mathrm{op}}=J_S+\mathcal D_S.
```

The detector construction must give a scalar exchange residual
`\varepsilon_{\mathrm{ex}}(e,p;R,S)`, not merely an informal statement that the
detectors are local.

3. **Operational projection.** Choose a preparation/effect pair `(p,e)` and
compute or bound the projected raw exchange coefficient

```math
B_{R,S}(e,p)
:=
e^TQ_{R,S}J_SJ_R\Gamma_0p.
```

This coefficient is the part of the raw exchange curvature visible to the chosen
experiment. If `B_{R,S}(e,p)=0`, the experiment is blind to that exchange
channel even if `Q_{R,S}\ne0`.

4. **Measured order statistic.** Implement the two operational orderings and
estimate

```math
\widehat\Delta_{R,S}^{\mathrm{op}}(e,p)
=
\widehat{\Pr}_{R\prec S}(e|p)
-
\widehat{\Pr}_{S\prec R}(e|p).
```

The theorem-level comparison is

```math
\Delta_{R,S}^{\mathrm{op}}(e,p)
=
B_{R,S}(e,p)
+
\delta_{\mathrm{ex}}(e,p;R,S),
\qquad
|\delta_{\mathrm{ex}}|\le\varepsilon_{\mathrm{ex}}.
```

5. **Decision rule.** With statistical and systematic uncertainty folded into
`\varepsilon_{\mathrm{tot}}`, a positive exchange detection requires

```math
|B_{R,S}(e,p)|
\gg
\varepsilon_{\mathrm{ex}}(e,p;R,S)
+
\varepsilon_{\mathrm{tot}}(e,p;R,S),
```

and the observed residual must have the predicted corridor, support,
coupling-order, and refinement scaling. A null result gives only the projected
bound

```math
|B_{R,S}(e,p)|
\le
|\widehat\Delta_{R,S}^{\mathrm{op}}|
+
\varepsilon_{\mathrm{ex}}
+
\varepsilon_{\mathrm{tot}},
```

for that instrument and that projection. It does not prove that the full raw
operator `Q_{R,S}` vanishes.

This pipeline is the bridge to Section 13. It also states the main limitation:
Paper 4 can export controlled operational projections of exchange curvature, not
a guarantee that every algebraic exchange defect is experimentally visible.

## 11. No-Signaling

Operational no-signaling is a statement about nonselective instruments. A
remote observer may condition on a known outcome in `R`, and that can change
inferred statistics in `S` when the records are correlated. That is not a
signal. A signal would mean that applying the `R` procedure and ignoring its
outcome changes the marginal statistics in `S`.

Let `\mathsf I_R^{\mathrm{op}}` be a nonselective instrument in `R`, and let
`\mathsf I_{S,o_S}` be an outcome operation in `S`. Define the calibrated
responses

```math
\mathscr J_R^{\mathrm{op}}
:=
\mathsf I_R^{\mathrm{op}}\Gamma_0^{-1},
\qquad
\mathscr J_{S,o_S}
:=
\mathsf I_{S,o_S}\Gamma_0^{-1}.
```

The two orderings give the final statistics

```math
\Pr_{R\to S}(o_S|p)
:=
1^T
\mathscr J_{S,o_S}
\mathscr J_R^{\mathrm{op}}
\Gamma_0p,
\qquad
\Pr_{S\to R}(o_S|p)
:=
1^T
\mathscr J_R^{\mathrm{op}}
\mathscr J_{S,o_S}
\Gamma_0p.
```

If `R` is not applied, the `S`-only statistic is

```math
\Pr_S(o_S|p):=
1^T\mathsf I_{S,o_S}p
=
1^T\mathscr J_{S,o_S}\Gamma_0p.
```

### Lemma 16: nonselective normalization identity

If `\mathsf I_R^{\mathrm{op}}` is a positive normalized nonselective channel,
then

```math
1^T\mathscr J_R^{\mathrm{op}}=1^T.
```

Consequently,

```math
\Pr_{S\to R}(o_S|p)=\Pr_S(o_S|p).
```

Proof. Since `1^T\mathsf I_R^{\mathrm{op}}=1^T`,

```math
1^T\mathscr J_R^{\mathrm{op}}
=
1^T\mathsf I_R^{\mathrm{op}}\Gamma_0^{-1}
=
1^T\Gamma_0^{-1}
=
1^T,
```

because `\Gamma_0` is stochastic and therefore `1^T\Gamma_0=1^T`, so
`1^T\Gamma_0^{-1}=1^T` on the calibrated domain. The second identity follows
by substitution. `square`

### Theorem 17: exact finite no-signaling under operational commutation

If

```math
1^T
\left[
\mathscr J_{S,o_S},
\mathscr J_R^{\mathrm{op}}
\right]
\Gamma_0p
=0,
```

then applying the nonselective `R` instrument before the `S` measurement does
not change the `S` marginal:

```math
\Pr_{R\to S}(o_S|p)=\Pr_S(o_S|p).
```

Proof. The commutator condition says

```math
\Pr_{R\to S}(o_S|p)=\Pr_{S\to R}(o_S|p).
```

Lemma 16 gives `\Pr_{S\to R}(o_S|p)=\Pr_S(o_S|p)`. `square`

### Theorem 18: approximate no-signaling from operational exchange

Define the no-signaling defect

```math
\delta_S(o_S;p)
:=
\left|
\Pr_{R\to S}(o_S|p)-\Pr_S(o_S|p)
\right|.
```

Then

```math
\delta_S(o_S;p)
=
\left|
1^T
\left[
\mathscr J_{S,o_S},
\mathscr J_R^{\mathrm{op}}
\right]
\Gamma_0p
\right|.
```

If the operational exchange theorem applies to the pair
`(\mathscr J_{S,o_S},\mathscr J_R^{\mathrm{op}})` with unit final effect
`e=1`, then

```math
\delta_S(o_S;p)
\le
C_{\mathrm{corr}}(1,p;R,S)
\|E_{R,S}-I\|_{\nu,R:S}^{\mathrm{corr}}
+
\varepsilon_{\mathrm{ex}}(1,p;R,S).
```

If the calibrated selective `S` response and nonselective `R` response satisfy
the same corridor hypotheses as Theorem 13, and Paper 3 or a detector-specific
extension supplies

```math
\|E_{S_{o_S},R}-I\|_{\nu,S:R}^{\mathrm{corr}}
\le
C\Delta^4e^{-\nu d_{R,S}},
```

for the exchange defect associated with that calibrated pair, then

```math
\delta_S(o_S;p)
\le
C_{\mathrm{corr}}(1,p;R,S)
C\Delta^4e^{-\nu d_{R,S}}
+
\varepsilon_{\mathrm{ex}}(1,p;R,S).
```

This is deliberately stated for the selective `S` response. The
outside-window cylinder-effect corollary for two nonselective channels is not
by itself a no-signaling theorem for outcome probabilities.

Proof. By Lemma 16,

```math
\Pr_S(o_S|p)=\Pr_{S\to R}(o_S|p).
```

Subtracting gives exactly the tested commutator. The stated inequalities are
Theorem 13 and Corollary 14 with `e=1`. `square`

### Conditioning is not signaling

Selective conditioning on a known remote outcome is different. The conditional
statistic

```math
\Pr(o_S|o_R,p)
=
\frac{\Pr(o_S,o_R|p)}{\Pr(o_R|p)}
```

may differ from `\Pr(o_S|p)` when records are correlated. This is ordinary
Bayesian conditioning on a shared stochastic record structure. It is not a
signal unless the nonselective marginal `\Pr_S(o_S|p)` changes when the `R`
procedure is applied and its outcome is ignored.

## 12. Projective Instrument Naturality

Paper 4 cannot claim continuum-facing observables until instruments and record
sectors are stable under refinement. Let `a'\ge a` be a refinement. Write the
system coarse-graining maps as

```math
P_i:=P_{\Sigma_i,a\leftarrow a'}:V_{\Sigma_i,a'}\to V_{\Sigma_i,a},
\qquad
i=0,1.
```

For detector record spaces, introduce a stochastic detector coarse-graining

```math
Q_D:W_{\lambda'}^{a'}\to W_\lambda^a.
```

The enlarged system-detector coarse-graining maps are

```math
\widetilde P_i:=P_i\otimes Q_D.
```

### Record-sector naturality

Sharp record sectors refine exactly if, after matching fine outcomes `o'` to
coarse outcomes `o=r(o')`,

```math
Q_D\Pi_{o'}^{a'}=\Pi_o^aQ_D.
```

For a coarse outcome `o`, let

```math
F_o:=\{o':r(o')=o\}.
```

The corresponding coarse-grained fine record projection is

```math
\Pi_{F_o}^{a'}:=\sum_{o'\in F_o}\Pi_{o'}^{a'}.
```

Exact sector naturality for the coarse outcome is

```math
Q_D\Pi_{F_o}^{a'}=\Pi_o^aQ_D.
```

An approximate version is measured by

```math
\epsilon_{\mathrm{rec}}(o)
:=
\left\|
Q_D\Pi_{F_o}^{a'}-\Pi_o^aQ_D
\right\|_{1,D}.
```

This is the record-level obstruction. If `\epsilon_{\mathrm{rec}}(o)` does
not go to zero along refinement, the outcome label itself is not projectively
stable.

### Proposition 19A: nested detector coarse-graining benchmark

The record-sector naturality condition is not empty. It is satisfied exactly by
a nested detector register in which the fine detector only resolves microscopic
subrecords inside a fixed coarse outcome.

Let the coarse detector record space be

```math
D_R^a=O,
\qquad
W_R^a=\mathbb R^O.
```

For each coarse outcome `o`, let `K_o` be a finite nonempty set of fine
subrecords, and define

```math
D_R^{a'}=\bigsqcup_{o\in O}\{o\}\times K_o,
\qquad
W_R^{a'}=\mathbb R^{D_R^{a'}}.
```

Define the detector coarse-graining map on basis states by

```math
Q_D\delta_{(o,k)}:=\delta_o.
```

Let `\Pi_o^a` be the coarse projection onto `{o}`, and let

```math
\Pi_{F_o}^{a'}
```

be the fine projection onto the union `{o}\times K_o`. Then

```math
Q_D\Pi_{F_o}^{a'}=\Pi_o^aQ_D
```

for every coarse outcome `o`. Hence

```math
\epsilon_{\mathrm{rec}}(o)=0.
```

Ready states are compatible whenever the fine ready distribution has the coarse
marginal

```math
\eta_o^a=\sum_{k\in K_o}\eta_{o,k}^{a'}.
```

Equivalently, for conditional distributions `\nu_o(k)\ge0` with
`\sum_{k\in K_o}\nu_o(k)=1`, one may choose

```math
\eta_{o,k}^{a'}=\eta_o^a\nu_o(k).
```

The benchmark can be made fully dynamical by refining the local write-register
detector of Proposition 10A. Keep the same system regulator and write
subchannels `M_o`. Choose nonnegative splitting weights

```math
\alpha_{k|o}(y_R,x_R)\ge0,
\qquad
\sum_{k\in K_o}\alpha_{k|o}(y_R,x_R)=1,
```

and define fine subchannels

```math
M_{o,k}^{a'}(y_R|x_R)
:=
\alpha_{k|o}(y_R,x_R)M_o^a(y_R|x_R).
```

Let `W_R^{a'}` be the fine write map that writes `(o,k)`, and let `W_R^a` be
the coarse write map that writes `o`. Then

```math
(I_1\otimes Q_D)W_R^{a'}
=
W_R^a(I_1\otimes Q_D).
```

Consequently, for the corresponding enlarged write-register kernels,

```math
(I_1\otimes Q_D)\Gamma_{R,D}^{a'}
=
\Gamma_{R,D}^a(I_0\otimes Q_D),
```

so the kernel refinement error in Theorem 19 is also zero in this pure detector
refinement:

```math
\epsilon_{\mathrm{ker}}=0.
```

Therefore the nested write-register benchmark satisfies exact projective
record-instrument naturality:

```math
P_1\mathsf I_{R,F_o}^{a'}=\mathsf I_{R,o}^aP_0
```

with `P_0=P_1=I` for pure detector refinement. With a simultaneous system
refinement, the same conclusion holds up to the system/enlarged-kernel
compatibility error `\epsilon_{\mathrm{ker}}`.

Proof. The identity `Q_D\Pi_{F_o}^{a'}=\Pi_o^aQ_D` follows on basis vectors. If
the input basis vector is `(o,k)`, both sides send it to `o`; if it is
`(o',k)` with `o'\ne o`, both sides send it to zero. This gives
`\epsilon_{\mathrm{rec}}(o)=0` in the detector column norm. The ready-state
condition is exactly the statement that `Q_D\eta^{a'}=\eta^a`.

For the write maps, compute on a positive array `\widetilde q`:

```math
\begin{aligned}
((I_1\otimes Q_D)W_R^{a'}\widetilde q)(y_R,x_{\bar R},o)
&=
\sum_{k\in K_o}\sum_{x_R,d'}
M_{o,k}^{a'}(y_R|x_R)\widetilde q(x_R,x_{\bar R},d')
\\
&=
\sum_{x_R,d'}
M_o^a(y_R|x_R)\widetilde q(x_R,x_{\bar R},d').
\end{aligned}
```

The right-hand side is exactly
`W_R^a(I_1\otimes Q_D)\widetilde q`, because the coarse write map ignores the
previous detector cell and uses the coarse total mass. Composing with
`\Gamma_0\otimes I` gives the enlarged-kernel equality. The final
instrument identity is Theorem 19 with both error terms zero. `square`

### Theorem 19: projective record-instrument transfer

Assume:

1. detector ready states are compatible,

```math
Q_D\eta_{\lambda'}^{a'}=\eta_\lambda^a;
```

2. enlarged kernels are compatible up to error
`\epsilon_{\mathrm{ker}}` in tested column norm:

```math
\left\|
\widetilde P_1\Gamma_{\lambda',D}^{a'}
-
\Gamma_{\lambda,D}^a\widetilde P_0
\right\|_{1,\mathrm{test}}
\le
\epsilon_{\mathrm{ker}};
```

3. record sectors satisfy the approximate naturality bound
`\epsilon_{\mathrm{rec}}(o)`.

Define the coarse outcome operation at regulator `a`,

```math
\mathsf I_{\lambda,o}^a p
:=
\left(I_1^a\otimes1_D^T\right)
\left(I_1^a\otimes\Pi_o^a\right)
\Gamma_{\lambda,D}^a(p\otimes\eta_\lambda^a),
```

and the fine operation coarse-grained over `F_o`,

```math
\mathsf I_{\lambda',F_o}^{a'}p'
:=
\sum_{o'\in F_o}\mathsf I_{\lambda',o'}^{a'}p'.
```

Then for every normalized fine preparation `p'` in the tested class and every
coarse effect `e_a` with `0\le e_a\le1`,

```math
\left|
e_a^T
\left(
P_1\mathsf I_{\lambda',F_o}^{a'}
-
\mathsf I_{\lambda,o}^aP_0
\right)p'
\right|
\le
\epsilon_{\mathrm{ker}}
+
\epsilon_{\mathrm{rec}}(o).
```

Proof. Write the fine record-retaining operation and coarse-grain it:

```math
\widetilde P_1
\left(I_1^{a'}\otimes\Pi_{F_o}^{a'}\right)
\Gamma_{\lambda',D}^{a'}(p'\otimes\eta_{\lambda'}^{a'}).
```

Insert and subtract

```math
\left(I_1^a\otimes\Pi_o^a\right)
\Gamma_{\lambda,D}^a
\widetilde P_0(p'\otimes\eta_{\lambda'}^{a'}).
```

The difference splits into two terms. The first is controlled by kernel
naturality, because projections and detector summation are contractions in the
column norm. The second is controlled by record-sector naturality:

```math
\widetilde P_1
\left(I\otimes\Pi_{F_o}^{a'}\right)
-
\left(I\otimes\Pi_o^a\right)\widetilde P_1
=
I\otimes
\left(Q_D\Pi_{F_o}^{a'}-\Pi_o^aQ_D\right).
```

Ready-state compatibility identifies
`\widetilde P_0(p'\otimes\eta_{\lambda'}^{a'})` with
`P_0p'\otimes\eta_\lambda^a`. Pairing with a positive effect bounded by the
unit effect cannot increase the column-norm bound. `square`

### Theorem 19B: lossy detector coarse-graining by explicit loss records

The nested-register benchmark is exact because every fine record maps to a
coarse record. Real detector refinements may lose subrecords, merge hardware
states imperfectly, or discard ambiguous events. The correct finite treatment is
not to hide the loss in normalization, but to add an explicit loss record.

Let

```math
Q_D^L:W_{\lambda'}^{a'}\to W_\lambda^a
```

be a positive column-substochastic detector coarse-graining map:

```math
1_{D^a}^TQ_D^L\le1_{D^{a'}}^T.
```

Define the loss functional

```math
\lambda_D^T:=1_{D^{a'}}^T-1_{D^a}^TQ_D^L\ge0.
```

Adjoin a coarse loss record `\bot` and set

```math
\bar W_\lambda^a:=W_\lambda^a\oplus\mathbb R\delta_\bot,
\qquad
\bar Q_D d:=Q_D^L d+\lambda_D(d)\delta_\bot.
```

Then `\bar Q_D` is stochastic. Let `\bar\Pi_o^a` be the ordinary coarse record
projection for `o`, acting as zero on `\bot`, and let `\bar\Pi_\bot^a` project
onto the loss record. For a coarse outcome `o`, define the lossy record
naturality defect

```math
\bar\epsilon_{\mathrm{rec}}(o)
:=
\left\|
\bar Q_D\Pi_{F_o}^{a'}-\bar\Pi_o^a\bar Q_D
\right\|_{1,D}.
```

Let `\bar\eta_\lambda^a` and `\bar\Gamma_{\lambda,D}^a` denote the coarse ready
state and enlarged kernel after adjoining the loss record. Assume extended
ready-state and enlarged-kernel compatibility:

```math
\left\|
\bar Q_D\eta_{\lambda'}^{a'}-\bar\eta_\lambda^a
\right\|_1
\le
\bar\epsilon_\eta,
```

and

```math
\left\|
\bar{\widetilde P}_1\Gamma_{\lambda',D}^{a'}
-
\bar\Gamma_{\lambda,D}^a\bar{\widetilde P}_0
\right\|_{1,\mathrm{test}}
\le
\bar\epsilon_{\mathrm{ker}},
```

where

```math
\bar{\widetilde P}_i:=P_i\otimes\bar Q_D.
```

Then for every normalized fine preparation `p'` in the tested class and every
ordinary coarse effect `0\le e_a\le1`,

```math
\left|
e_a^T
\left(
P_1\mathsf I_{\lambda',F_o}^{a'}
-
\bar{\mathsf I}_{\lambda,o}^aP_0
\right)p'
\right|
\le
\bar\epsilon_{\mathrm{ker}}
+
\bar\epsilon_{\mathrm{rec}}(o)
+
\bar\epsilon_\eta.
```

Here `\bar{\mathsf I}_{\lambda,o}^a` is the ordinary nonloss outcome operation
in the coarse detector with the additional loss record present.

If an experiment discards loss records and reports conditional-on-survival
statistics, define the survival operations

```math
\mathsf I_{\mathrm{surv}}:=\sum_{o\ne\bot}\bar{\mathsf I}_{\lambda,o}^a,
\qquad
\mathsf I_{\mathrm{surv}}'
:=
\sum_{o\ne\bot}\mathsf I_{\lambda',F_o}^{a'}.
```

If their survival probabilities are bounded below by

```math
s,s'\ge s_{\min}>0
```

and their scalar mismatch is bounded by `\epsilon_{\mathrm{surv}}`, then the
renormalized reported outcome obeys

```math
\left|
\frac{
e_a^TP_1\mathsf I_{\lambda',F_o}^{a'}p'
}{s'}
-
\frac{
e_a^T\bar{\mathsf I}_{\lambda,o}^aP_0p'
}{s}
\right|
\le
\frac{
\bar\epsilon_{\mathrm{ker}}
+
\bar\epsilon_{\mathrm{rec}}(o)
+
\bar\epsilon_\eta
+
\epsilon_{\mathrm{surv}}
}{s_{\min}}.
```

Proof. The extension by `\bot` turns a substochastic hardware map into a
stochastic detector coarse-graining map:

```math
1_{\bar D^a}^T\bar Q_D
=
1_{D^a}^TQ_D^L+\lambda_D^T
=
1_{D^{a'}}^T.
```

Therefore Theorem 19 applies to the extended detector. The ordinary outcome
projection `\bar\Pi_o^a` has zero support on the loss record, so any fine mass
that the lossy map sends to `\bot` contributes to
`\bar\epsilon_{\mathrm{rec}}(o)` instead of disappearing. Approximate ready-state
compatibility contributes at most `\bar\epsilon_\eta` because the enlarged kernel
and final effect are positive contractions in column norm. This proves the
nonrenormalized bound.

For the conditional-on-survival statistic, write each reported probability as
the nonrenormalized numerator divided by its survival denominator. The same
denominator algebra as Corollary 11B gives the displayed
`1/s_{\min}` amplification. `square`

This theorem is the safe way to discuss lossy refinement. Loss can be part of
the operational record, but it cannot be silently divided away without paying the
survival-denominator residual.

### Corollary 20: operational projective equivalence

If

```math
\epsilon_{\mathrm{ker}}(a',a)\to0,
\qquad
\epsilon_{\mathrm{rec}}(o;a',a)\to0
```

along the refinement net, then the operational outcome statistics are
projectively compatible:

```math
e_a^TP_1\mathsf I_{\lambda',F_o}^{a'}p'
-
e_a^T\mathsf I_{\lambda,o}^aP_0p'
\to0.
```

Thus the finite record theorem survives refinement for this outcome. If either
the detector record sectors or the enlarged detector kernels fail these
compatibility estimates, Paper 4 has only a fixed-regulator measurement theory
for that instrument.

For lossy detector refinements, the same conclusion holds for the extended
detector with explicit loss record if

```math
\bar\epsilon_{\mathrm{ker}},
\quad
\bar\epsilon_{\mathrm{rec}}(o),
\quad
\bar\epsilon_\eta
\to0.
```

If loss records are discarded and statistics are renormalized on survival, one
also needs a survival floor `s_{\min}` bounded away from zero and
`\epsilon_{\mathrm{surv}}\to0`.

## 13. Possible Empirical Separations From Standard QFT

Paper 4 should not overclaim. Differences from standard relativistic QFT are
operational only after instruments are defined.

All experimental proposals in this section are therefore **templates** unless a
microscopic ISP kernel family, detector instruments, refinement maps, and
calibration residuals have been supplied. A template may show what to measure and
how a deviation would scale; it is not yet a numerical prediction of
relativistic ISP.

The correct comparison is not

```text
raw ISP matrix versus QFT observable.
```

It is

```text
declared ISP operational family
versus
standard QFT detector/instrument model.
```

A proposed separation must therefore specify:

1. the preparation class;
2. the localized instruments and readouts;
3. the calibrated ISP statistic;
4. the corresponding QFT detector statistic;
5. detector/calibration residuals;
6. refinement/cutoff scaling.

Standard local QFT expects exact spacelike commutation in the ideal algebraic
limit. A residual ISP exchange-order effect would have to be separated from
finite-regulator error, detector nonlocality, and imperfect calibration before
it could be called new physics.

### Separation Rule

A candidate difference is serious only if it survives the following test:

```math
\mathrm{measured\ residual}
=
\mathrm{ISP\ structural\ term}
+
\mathrm{calibration/detector\ residual}
+
\mathrm{finite\ regulator\ error}.
```

The structural term must have a predicted scaling that cannot be absorbed into
the last two terms. In this paper the main structural term is the operational
exchange statistic controlled by `E_{R,S}-I`.

### Edge-Case Taxonomy

The useful way to look for "spooky-action" style edge cases is not to ask
whether ISP can reproduce ordinary Bell correlations. It must. The real question
is where ISP adds an operational structure that standard QFT does not need as a
primitive.

There are four possible interfaces where a genuine empirical separation could
enter:

1. **Record interface:** QFT treats the laboratory plus detector as one larger
   reversible quantum system until one coarse-grains or traces an environment.
   Strong ISP treats sufficiently stable finite records as objective
   configuration-sector events. The edge case is a coherent marker that can
   still be erased versus an actual record that cannot be erased.
2. **Spacetime-transport interface:** QFT local operations commute at spacelike
   separation. Relativistic ISP represents finite hypersurface evolution by
   stochastic transports and comparison maps. The edge case is not signaling,
   but a correlation-only order or loop holonomy in spacelike record statistics.
3. **Vacuum-detector interface:** QFT vacuum effects are fixed by field
   correlation functions and detector couplings. ISP must reproduce those
   detector kernels or predict controlled deviations in local detector response,
   detector-detector correlations, Casimir-type forces, or dynamical-vacuum
   emission.
4. **Gravity/vacuum-normalization interface:** QFT assigns enormous formal
   zero-point contributions that are renormalized away in nongravitational
   experiments. ISP may treat raw vacuum normalization differently from
   operational record effects. A possible split would concern what gravitates,
   not ordinary virtual-particle language.

This gives a sharp rule:

```text
If ISP changes only the ontology of a QFT calculation, there is no new
experiment.

If ISP changes an operational kernel, record rule, hypersurface comparison map,
or vacuum detector response, there is a possible experiment.
```

Virtual particles are therefore not themselves observables in this paper. They
are a perturbative bookkeeping language for QFT amplitudes. An ISP explanation
of "virtual particles" is empirically different only if it changes some
observable quantity such as a Lamb shift, anomalous magnetic moment, Casimir
force, detector excitation spectrum, scattering cross-section, or vacuum
correlation function. Existing precision data make large changes in those
channels implausible. The more promising ISP-specific edge cases are therefore
record-threshold effects and hypersurface-comparison effects, because those are
where the ontology changes the operational rules instead of merely relabeling a
standard loop calculation.

### Area 1: Spacelike Exchange-Order Residuals

Operational statistic:

```math
\Delta_{R,S}^{\mathrm{op}}(e,p)
=
e^T[
\mathscr J_R^{\mathrm{op}},
\mathscr J_S^{\mathrm{op}}
]\Gamma_0p.
```

Standard QFT baseline: for ideal spacelike separated local operations in a
local algebraic QFT, the corresponding nonselective local operations commute
on physical statistics, after detector smearing and gauge constraints are
properly handled.

Relativistic ISP possibility: Paper 3 gives a raw exchange-corridor term, and
Section 10 gives

```math
|\Delta_{R,S}^{\mathrm{op}}|
\le
C\|E_{R,S}-I\|_{\mathrm{corr}}
+
\varepsilon_{\mathrm{ex}}.
```

In a finite common-collar slab this may scale like

```math
\Delta^4 e^{-\nu(d_{R,S}+w)}
```

before continuum/refinement limits.

Possible measurable program:

1. reconstruct `J_R`, `J_S`, and `E_{R,S}` in a controlled spin, qudit, or
   gauge-link simulator;
2. implement detector-coupled nonselective instruments realizing
   `\mathscr J_R^{\mathrm{op}}` and `\mathscr J_S^{\mathrm{op}}`;
3. measure the order residual `\Delta_{R,S}^{\mathrm{op}}`;
4. test fourth-order onset, distance decay, and corridor-window scaling;
5. vary detector couplings to bound `\varepsilon_{\mathrm{ex}}`.

Interpretation: this is the nearest-term technical test of the Paper 3/Paper 4
bridge. It is not yet a direct violation of continuum QFT unless the residual
survives detector modeling and refinement in a way standard QFT cannot mimic.

### Area 2: Operational No-Signaling Residuals

Operational statistic:

```math
\delta_S(o_S;p)
=
\left|
\Pr_{R\to S}(o_S|p)-\Pr_S(o_S|p)
\right|.
```

Standard QFT baseline: a nonselective spacelike operation in `R` should not
alter marginal outcome probabilities in `S`.

Relativistic ISP possibility: Section 11 relates this defect to the
commutator between the selective `S` response and the nonselective `R`
response:

```math
\delta_S(o_S;p)
=
\left|
1^T[
\mathscr J_{S,o_S},
\mathscr J_R^{\mathrm{op}}
]\Gamma_0p
\right|.
```

If this commutator is controlled by an operational exchange theorem, then the
same exchange-corridor scaling controls approximate no-signaling.

Experimental warning: postselected statistics `\Pr(o_S|o_R,p)` are not a
signaling test. They can change because of ordinary correlations. The only
signaling test is the nonselective marginal in `S`.

### Area 3: Foliation Or Refinement Residuals

Operational statistic: compare two regulated hypersurface/deformation
descriptions `\pi` and `\pi'` that are meant to represent the same physical
process:

```math
\delta_{\mathrm{fol}}(e,p)
:=
\left|
e^T\mathsf I_{\pi}p
-
e^T\mathsf I_{\pi'}p
\right|.
```

Standard QFT baseline: after renormalization and correct detector modeling,
probabilities should not depend on an arbitrary hypersurface foliation or
refinement path.

Relativistic ISP possibility: Paper 2 and Section 12 say this depends on
projective compatibility of system kernels and detector record sectors. A
nonzero residual can arise from

```math
\epsilon_{\mathrm{ker}}
+
\epsilon_{\mathrm{rec}}.
```

Possible measurable program:

1. in a simulator, implement two circuit/slab decompositions of the same
   target local evolution;
2. reconstruct operational statistics for matching detector readouts;
3. test whether the difference scales to zero under refinement;
4. isolate record-sector mismatch by varying detector coarse-graining `Q_D`.

Interpretation: a persistent foliation residual would be more damaging than a
finite exchange tail, because it would threaten relativistic covariance.

### Area 4: Phase/Interference Completeness

Operational statistic: the controlled two-path family

```math
\Gamma_\phi=|BP_\phi B|^2
```

gives

```math
\Pr_\phi(0|0)=\cos^2(\phi/2).
```

A which-path record coupling gives instead the incoherent marginal

```math
\Pr_{\mathrm{wp}}(0|0)=1/2.
```

Standard QFT/quantum baseline: coherent phase controls, which-path
decoherence, and coherent erasure are all represented within the same
operational quantum theory.

Relativistic ISP possibility: a primitive endpoint kernel by itself does not
recover phase physics. ISP must include a sufficiently rich controlled-kernel
family in `\mathcal O_a`. A measurable difference could appear if ISP imposes
constraints on available phase controls, coherent erasure, or visibility that
standard quantum theory does not.

Possible measurable program:

1. benchmark `\Gamma_\phi` fringes;
2. add record-writing couplings and verify loss of interference;
3. add erasure controls and test whether interference is restored;
4. compare all three operations inside one declared `\mathcal O_a`.

Interpretation: failure here is not a small correction. It is a reconstruction
failure: ISP would address finite definite outcomes but not recover quantum
phase physics.

### Area 5: Record Stability And Refinement Leakage

Operational statistics:

```math
\epsilon_o(\Theta_R),
\qquad
\epsilon_{\mathrm{rec}}(o;a',a).
```

The first measures immediate repeat-readout instability. The second measures
failure of record sectors to refine projectively.

Standard QFT baseline: detector stability is modeled dynamically through
decoherence, amplification, and environmental robustness. It is not usually a
primitive record-sector axiom.

Relativistic ISP possibility: ISP treats finite records as primitive
configuration-sector events at the operational level. A model may therefore
predict specific leakage or refinement-error scalings. These are measurable
only once a detector model fixes the record sectors and coarse-graining maps.

Possible measurable program:

1. repeated readout tests on a controlled finite detector register;
2. refinement/coarse-graining tests on nested detector encodings;
3. scaling of `\epsilon_{\mathrm{rec}}` under increasing detector resolution.

Interpretation: this does not automatically distinguish ISP from QFT. It
becomes distinctive only if ISP predicts universal record-sector stability or
leakage scalings not reproducible by ordinary detector dynamics.

### Area 6: Gauge-Center And Boundary-Flux Readouts

Operational statistic: compare matter-only readouts with center-resolved
readouts in a gauge theory:

```math
\Pr(o_{\mathrm{matter}}|p)
\quad\text{versus}\quad
\Pr(o_{\mathrm{matter}},z_{\partial R}|p).
```

Standard QFT baseline: careful algebraic gauge theory already recognizes
centers, edge modes, and boundary flux sectors. A naive matter-only local
factorization is not the correct baseline.

Relativistic ISP possibility: ISP's finite configuration ontology may make
boundary-center sectors operationally unavoidable. A difference would appear
only if ISP predicts center-sector constraints, exchange residuals, or
refinement behavior not matched by standard center-resolved gauge theory.

Possible measurable program:

1. finite `Z_2` or truncated compact `U(1)` gauge-link simulator;
2. compare reduced matter readouts with explicit boundary-flux readouts;
3. test whether exchange/no-signaling bounds improve only after center
   resolution.

Interpretation: this is probably a conceptual discriminator before it is a
near-term fundamental experiment. It can still prevent false claims based on
incorrect tensor-factor locality.

### Area 7: Vacuum Detector Correlations And Entanglement Harvesting

Operational statistic: two localized detector instruments coupled to a vacuum
or vacuum-like sector,

```math
\Pr(o_R,o_S|p_{\mathrm{vac}})
-
\Pr(o_R|p_{\mathrm{vac}})\Pr(o_S|p_{\mathrm{vac}}).
```

Standard QFT baseline: local detector models in the vacuum exhibit known
distance-, smearing-, and gap-dependent correlation/entanglement harvesting
behavior.

Relativistic ISP possibility: once a continuum vacuum sector exists, ISP must
reproduce these detector correlations or predict a controlled deviation. The
deviation could come from the allowed controlled-kernel family, record-sector
coarse-graining, or exchange-corridor residuals.

Current status: this is not the first experiment. It requires Paper 5/Paper 6
level continuum/gauge/vacuum reconstruction. But it is one of the cleanest
eventual comparisons to relativistic QFT because it is naturally formulated in
terms of localized detector instruments.

### Area 8: Empty Space, Virtual Particles, And Vacuum Energy

This area is conceptually tempting but dangerous. "Virtual particles" are not
detector clicks. They are internal terms in a perturbative representation of
QFT amplitudes. Therefore ISP should not claim a different prediction merely
because it gives a different story about virtual particles.

The operational question is instead:

```text
Which vacuum effects are actual detector or force statistics, and which are
unobservable normalization conventions?
```

Standard QFT baseline:

1. vacuum correlation functions determine detector response and entanglement
   harvesting;
2. loop effects contribute to measurable quantities such as Lamb shifts,
   anomalous magnetic moments, scattering amplitudes, and running couplings;
3. boundary-modified vacuum modes give Casimir-type forces;
4. absolute vacuum energy is not measured directly in nongravitational
   experiments, while its gravitational role is tied to the cosmological
   constant problem.

Relativistic ISP possibility:

1. ISP may reproduce the same local detector kernels and therefore the same
   ordinary virtual-particle phenomenology;
2. ISP may distinguish raw vacuum normalization from operational record
   effects, which could change how vacuum energy enters gravity;
3. ISP may predict finite-regulator or record-coupled corrections to vacuum
   detector response, but those corrections must survive the precision
   constraints already imposed by spectroscopy, scattering, and Casimir
   measurements.

The first clean vacuum-side experimental family is therefore not "measure the
energy of empty space." It is:

```text
compare a fully specified ISP vacuum detector kernel with the QFT Wightman
detector kernel for the same localized instrument.
```

For a localized two-level detector with energy gap `\Omega` and switching
function `\chi(t)`, the QFT response has the schematic form

```math
P_{\mathrm{QFT}}(\Omega)
=
\lambda^2
\int dt\,dt'\,
\chi(t)\chi(t')
e^{-i\Omega(t-t')}
W(x(t),x(t'))
+O(\lambda^4),
```

where `W` is the field vacuum two-point function. A vacuum-sector ISP deviation
would have to appear as

```math
P_{\mathrm{ISP}}(\Omega)-P_{\mathrm{QFT}}(\Omega)
=
\lambda^2
\int dt\,dt'\,
\chi(t)\chi(t')
e^{-i\Omega(t-t')}
\delta W_{\mathrm{ISP}}(x(t),x(t'))
+\delta P_{\mathrm{rec}}
+O(\lambda^4).
```

Here `\delta W_{\mathrm{ISP}}` is a genuine vacuum-kernel difference and
`\delta P_{\mathrm{rec}}` is a record-sector correction caused by the detector
becoming an ISP record rather than a reversible probe. If both terms vanish, ISP
may still give a different ontology of vacuum fluctuations, but it gives no
different prediction in this channel.

A gravitational vacuum-energy split is possible only after coupling the
hypersurface kernels to geometry. The careful Paper 4 statement is:

```text
ISP may eventually distinguish operational vacuum detector effects from raw
vacuum normalization, but Paper 4 does not yet contain a gravitational theorem
that changes the cosmological constant or the weight of Casimir energy.
```

So this is a future high-value target, not a current Paper 4 claim.

### Current Technology Ranking

The realistic near-term ladder is:

1. **Quantum-simulator raw exchange audit:** reconstruct `J_R`, `J_S`,
   `E_{R,S}` and check onset/corridor scaling. This tests the Paper 3 raw
   mechanism, not a direct QFT deviation.
2. **Detector-coupled exchange audit:** add record instruments and test whether
   operational exchange statistics track the raw exchange theorem after
   calibration.
3. **Record-threshold erasure audit:** test whether a stable finite detector
   record can be coherently erased. This is the sharpest non-simulator
   measurement-ontology edge case.
4. **Interferometer control audit:** verify that the declared ISP operational
   family contains coherent controls, which-path records, and erasure-like
   controls.
5. **Projective detector audit:** test whether nested or lossy detector encodings
   have stable record-sector coarse-graining, explicit loss records, and survival
   denominators bounded away from zero.
6. **Spacelike order and loop audits:** use Bell/GHZ-style non-simulator
   experiments to bound order asymmetry and hypersurface-loop holonomy. These
   are expected-null relativistic consistency tests unless residual constants
   are nonzero.
7. **Continuum-facing QFT comparison:** only after a vacuum/gauge continuum
   sector exists, compare detector correlations, no-signaling residuals,
   foliation dependence, Casimir-type forces, and vacuum response against
   standard relativistic QFT.

The easiest current test is therefore not "find a violation of QFT." It is:

```text
Does the finite ISP operational exchange statistic obey the predicted
onset, corridor, and calibration scaling?
```

That experiment would tell us whether the Paper 3/Paper 4 bridge is physically
usable before we spend effort claiming fundamental deviations.

### Concrete Non-Simulator Proposal: Spacelike Photon Order-Asymmetry Test

The cleanest non-simulator discriminator is a spacelike-separated photon
experiment modeled on loophole-free Bell technology, but with a different
statistic. The goal is not to test Bell nonlocality. The goal is to test
whether joint detector statistics depend on the lab-frame order of two
spacelike localized measurement interactions.

This is deliberately a residual-finding test. Since spacelike order is not
Lorentz invariant, standard relativistic QFT predicts zero, and a fully
Lorentz-invariant operational continuum limit of ISP should also predict zero.
The test differentiates only if a finite-regulator or detector-coupled ISP
exchange residual survives as an operational statistic with the controlled
onset pattern below.

Use a polarization-entangled telecom photon source with a controlled pair
phase:

```math
|\Phi_{\varphi_p}\rangle
=
\frac{|H\rangle_R|H\rangle_S+
e^{i\varphi_p}|V\rangle_R|V\rangle_S}{\sqrt2}.
```

Use the degenerate telecom setting

```math
\lambda_p=775.04\,\mathrm{nm},
\qquad
f_p\simeq386.81\,\mathrm{THz},
```

```math
\lambda_R=\lambda_S=1550.08\,\mathrm{nm},
\qquad
f_R=f_S\simeq193.40\,\mathrm{THz},
```

with narrow spectral filtering, for example `\Delta\nu\le100\,\mathrm{GHz}`.
The primary run sets `\varphi_p=0`; phase-control runs use
`\varphi_p\in\{0,\pi/2,\pi\}` as a calibration of the coherent pair phase.

At each station the measured polarization basis is

```math
|+;\theta,\alpha\rangle
=
\cos\theta\,|H\rangle+e^{i\alpha}\sin\theta\,|V\rangle,
```

```math
|-;\theta,\alpha\rangle
=
\sin\theta\,|H\rangle-e^{i\alpha}\cos\theta\,|V\rangle.
```

Place two measurement stations a distance

```math
L=1\,\mathrm{km}
```

apart, so the light-crossing time is

```math
L/c\simeq3.3\,\mu\mathrm{s}.
```

At each station use a fast electro-optic polarization modulator followed by a
polarizing beam splitter and high-efficiency single-photon detectors. Let the
measurement settings be `(\theta_R,\alpha_R)` at `R` and
`(\theta_S,\alpha_S)` at `S`, with outcomes

```math
r,s\in\{+1,-1\}.
```

Use timing delays to realize two spacelike orderings:

```text
R before S:    t_R-t_S=-\tau,
S before R:    t_R-t_S=+\tau,
```

with a concrete choice

```math
\tau=200\,\mathrm{ns},
\qquad
T_{\mathrm{gate}}=2\,\mathrm{ns},
\qquad
T_{\mathrm{jitter}}\le0.1\,\mathrm{ns},
```

and require

```math
c(|\tau|+2T_{\mathrm{gate}}+T_{\mathrm{jitter}})<L.
```

For the numerical values above,

```math
D=L-c(|\tau|+2T_{\mathrm{gate}}+T_{\mathrm{jitter}})
\simeq0.939\,\mathrm{km},
```

so the events remain spacelike with a large margin.

#### QFT prediction

For the state `|\Phi_{\varphi_p}\rangle`, standard quantum theory/QFT gives
the correlation

```math
E_{\mathrm{QFT}}
(\theta_R,\alpha_R;\theta_S,\alpha_S)
=
\cos2\theta_R\cos2\theta_S
+
\sin2\theta_R\sin2\theta_S
\cos(\alpha_R+\alpha_S-\varphi_p).
```

With visibility `V`, the joint probabilities are

```math
P_{\mathrm{QFT}}
(r,s|\theta_R,\alpha_R;\theta_S,\alpha_S)
=
\frac14
\left[
1+rs\,V
E_{\mathrm{QFT}}
(\theta_R,\alpha_R;\theta_S,\alpha_S)
\right],
```

where `V` is the measured visibility. For the primary linear run
`\alpha_R=\alpha_S=\varphi_p=0`, this reduces to

```math
E_{\mathrm{QFT}}= \cos2(\theta_R-\theta_S).
```

The prediction is independent of which spacelike station is first:

```math
P_{R\prec S}^{\mathrm{QFT}}
(r,s|\theta_R,\alpha_R;\theta_S,\alpha_S)
=
P_{S\prec R}^{\mathrm{QFT}}
(r,s|\theta_R,\alpha_R;\theta_S,\alpha_S).
```

Thus the order-asymmetry correlation

```math
\Omega(\theta_R,\alpha_R;\theta_S,\alpha_S)
:=
\sum_{r,s=\pm1}rs
\left[
P_{R\prec S}(r,s|\theta_R,\alpha_R;\theta_S,\alpha_S)
-
P_{S\prec R}(r,s|\theta_R,\alpha_R;\theta_S,\alpha_S)
\right]
```

has the QFT prediction

```math
\Omega_{\mathrm{QFT}}(\theta_R,\alpha_R;\theta_S,\alpha_S)=0.
```

The single-station marginals should also be order-independent.

#### ISP residual template

If relativistic ISP has a genuine operational exchange-curvature residual,
then the leading observable difference should be correlation-only, with no
single-site marginal shift. A minimal falsifiable two-channel template is

```math
\Omega_{\mathrm{ISP}}
=
\chi_R^2\chi_S^2e^{-D/\ell_{\mathrm{ISP}}}
\left[
A_\theta\sin2(\theta_S-\theta_R)
+
A_\phi\sin2\theta_R\sin2\theta_S
\sin(\alpha_R+\alpha_S-\varphi_p)
\right]
+O(\chi^6)+\varepsilon_{\mathrm{det}}.
```

where:

1. `\chi_R,\chi_S` are controllable local analyzer-coupling strengths, such as
   electro-optic retardance amplitudes;
2. `D=L-c(|\tau|+2T_{\mathrm{gate}}+T_{\mathrm{jitter}})` is the spacelike
   margin;
3. `\ell_{\mathrm{ISP}}` is the exchange-decay length in the operational
   effective model;
4. `A_\theta` and `A_\phi` are model-dependent exchange coefficients;
5. `\varepsilon_{\mathrm{det}}` collects detector bias, timing leakage,
   crosstalk, and calibration error.

Equivalently, at the joint-probability level this corresponds to

```math
P_{R\prec S}-P_{S\prec R}
=
\frac{rs}{4}\Omega_{\mathrm{ISP}}
```

plus outcome-independent detector residuals that must be bounded separately.
The fourth-order coupling dependence is the operational analogue of the
Paper 3 exchange onset. The angle and phase factors are test templates, not
universal constants of the theory: they are the lowest harmonics that are
correlation-only, odd under reversal of the controlled angle/phase quadrature,
and zero in the aligned null settings.

#### Parameter ledger: known, controlled, measured, unknown

Known physical constants used to convert the optical specification into
numbers are:

| Symbol | Meaning | Value used |
| --- | --- | --- |
| `c` | vacuum light speed | `299792458 m/s` |
| `h` | Planck constant | `6.62607015e-34 J s` |
| `\lambda_R,\lambda_S` | signal/idler wavelengths | `1550.08 nm` |
| `f_R,f_S=c/\lambda_R` | signal/idler frequencies | `193.40 THz` |
| `h f_R` | photon energy | `0.7999 eV` |
| `\lambda_p` | pump wavelength | `775.04 nm` |
| `f_p=c/\lambda_p` | pump frequency | `386.81 THz` |
| `h f_p` | pump photon energy | `1.5997 eV` |

Controlled laboratory parameters are:

| Symbol | Meaning | Nominal values |
| --- | --- | --- |
| `L` | station separation | `1 km`, with larger-distance repeats desirable |
| `\tau` | imposed lab-time order offset | `200 ns` |
| `T_{\mathrm{gate}}` | coincidence gate | `2 ns` |
| `T_{\mathrm{jitter}}` | timing jitter bound | `<=0.1 ns` |
| `D` | spacelike margin | `L-c(abs(\tau)+2T_{\mathrm{gate}}+T_{\mathrm{jitter}})=938.8 m` |
| `\theta_R,\theta_S` | linear polarization analyzer angles | rows in the prediction table below |
| `\alpha_R,\alpha_S` | local phase analyzer settings | rows in the phase table below |
| `\varphi_p` | pair-source phase | usually `0`, also `\pi/2,\pi` for calibration |
| `\chi_R,\chi_S` | local analyzer coupling/retardance amplitudes | `\pi/16,\pi/8,3\pi/16,\pi/4` |

Measured apparatus parameters are not theory constants. They must be measured
and inserted into the QFT baseline and the systematic-error budget:

| Symbol | Meaning |
| --- | --- |
| `V` | Bell-fringe visibility in the same settings |
| `\eta_R,\eta_S` | detector efficiencies |
| `p_{\mathrm{dark},R},p_{\mathrm{dark},S}` | dark-count probabilities per gate |
| `T_{\mathrm{jitter}}` | measured timing jitter distribution, not only its bound |
| `\varepsilon_{\mathrm{det}}` | residual detector/order bias after null tests |
| `\varepsilon_{\mathrm{ex}}` | Paper 4 operational exchange calibration residual |

The genuinely unknown ISP parameters are:

| Symbol | Status | Meaning |
| --- | --- | --- |
| `A_\theta` | unknown signed dimensionless coefficient | angle-channel exchange amplitude |
| `A_\phi` | unknown signed dimensionless coefficient | phase-channel exchange amplitude |
| `\ell_{\mathrm{ISP}}` | unknown positive length scale | operational exchange-decay length |
| `C_6` | unknown nuisance coefficient | first higher-order coupling correction in `O(\chi^6)` |

In an exact Lorentz-invariant operational continuum limit with no surviving
regulator/detector exchange residual, the effective prediction is simply
`B_\theta(D)=B_\phi(D)=0`. Equivalently, the relevant operational projections
of `A_\theta` and `A_\phi` vanish. Nonzero values are therefore not generic
ISP constants; they would be evidence of a surviving finite-regulator,
detector-coupled, or incomplete-continuum exchange effect.

At one fixed distance the experiment does not separately identify
`A_\theta`, `A_\phi`, and `\ell_{\mathrm{ISP}}`. It directly measures or
bounds the effective combinations

```math
B_\theta(D)=A_\theta e^{-D/\ell_{\mathrm{ISP}}},
\qquad
B_\phi(D)=A_\phi e^{-D/\ell_{\mathrm{ISP}}}.
```

A null experiment with total one-sigma uncertainty
`\sigma_{\mathrm{tot}}` gives, for an `n`-sigma bound,

```math
|B_i(D)|
\le
\frac{n\sigma_{\mathrm{tot}}}{\chi^4_{\max}},
\qquad
i\in\{\theta,\phi\}.
```

With `\chi_{\max}=\pi/4` and `\sigma_{\mathrm{tot}}=10^{-4}`, this is

```math
|B_i(D)|\lesssim2.6\times10^{-4}
```

at one sigma, or about `7.9e-4` at three sigma. If a nonzero signal is seen at
two spacelike margins `D_1,D_2`, then the decay length can be estimated from

```math
\ell_{\mathrm{ISP}}
=
\frac{D_2-D_1}
{\log |B_i(D_1)|-\log |B_i(D_2)|},
```

provided the same channel `i` keeps a stable sign and the systematic residuals
are below both signals. Then

```math
A_i=B_i(D_1)e^{D_1/\ell_{\mathrm{ISP}}}.
```

There is also a model-independent probability bound: because `\Omega` is the
difference of two correlations, `|\Omega|\le2`. For a single isolated channel,
this implies only the weak consistency condition

```math
|B_i(D)|\chi^4\le2.
```

The experimental and theoretical bounds above are therefore the meaningful
ones; the probability bound is just a sanity check.

The higher-order nuisance coefficient is found from the coupling scan. For a
fixed sign channel `i`,

```math
\Omega_i(\chi)
=
s_iB_i(D)\chi^4+C_{6,i}\chi^6+O(\chi^8)
+\varepsilon_{\mathrm{det}},
```

where `s_i=\pm1` is the predicted sign. Therefore

```math
\frac{\Omega_i(\chi)}{s_i\chi^4}
=
B_i(D)+s_iC_{6,i}\chi^2+O(\chi^4).
```

The intercept gives `B_i(D)`, while curvature in `\chi^2` estimates the
higher-order contamination. If the smallest two or three `\chi` values do not
fit this form, the experiment has not isolated the Paper 3 fourth-order
exchange onset.

#### Theoretical route to the unknown constants

The present paper does not assign universal numerical values to
`A_\theta`, `A_\phi`, or `\ell_{\mathrm{ISP}}`. They are not new fundamental
constants like `c` or `h`. They are effective constants of a declared
regulated ISP model plus a declared detector/control family.

The rigorous way to estimate or bound them is:

1. choose a microscopic regulated ISP kernel family for the photon source,
   propagation channels, electro-optic analyzers, and record detectors;
2. construct the reference and locally deformed kernels
   `\Gamma_0,\Gamma_R,\Gamma_S`;
3. form the raw comparison maps

```math
J_R=\Gamma_R\Gamma_0^{-1},
\qquad
J_S=\Gamma_S\Gamma_0^{-1};
```

4. compute the raw exchange defect

```math
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1};
```

5. push it through the detector instruments/effects used in this experiment
   to obtain the operational `\Omega`;
6. extract the small-coupling coefficients by

```math
B_\theta(D)
=
\lim_{\chi\to0}
\frac{\Omega(0^\circ,45^\circ)}{\chi^4},
```

```math
B_\phi(D)
=
\lim_{\chi\to0}
\frac{\Omega(45^\circ,0;\,45^\circ,\pi/2)}{\chi^4}.
```

For a proof-level bound rather than a numerical finite-matrix calculation,
combine Paper 3's exchange-corridor theorem with Theorem 13 of this paper.
Schematically,

```math
|\Omega|
\le
C_{\mathrm{op}}
C_{\mu,\nu}
\kappa_R\kappa_S
M_R^-M_S^-
e^{-\nu d_{R,S}}
+
\varepsilon_{\mathrm{ex}}.
```

If the detector-coupling expansion gives

```math
\kappa_R\le g_R\chi_R^2,
\qquad
\kappa_S\le g_S\chi_S^2,
```

then the theory predicts the fourth-order envelope

```math
|\Omega|
\le
C_{\mathrm{op}}C_{\mu,\nu}g_Rg_SM_R^-M_S^-
\chi_R^2\chi_S^2
e^{-\nu d_{R,S}}
+
\varepsilon_{\mathrm{ex}}.
```

Thus the theoretical decay length is

```math
\ell_{\mathrm{ISP}}=1/\nu
```

in cell-distance units, or `a_{\mathrm{cell}}/\nu` in physical units if the
regulator cell size is `a_{\mathrm{cell}}`. The coefficient envelope is

```math
|A_i|
\le
C_{\mathrm{shape},i}
C_{\mathrm{op}}C_{\mu,\nu}g_Rg_SM_R^-M_S^-,
```

where `C_{\mathrm{shape},i}` is the projection from the raw exchange defect
onto the chosen angle or phase harmonic. Exact signs and exact values require
the explicit regulated kernel and detector model; the general theorems give
onset, decay, and upper envelopes.

#### Bounds from existing experiments

Existing Bell/order experiments can already constrain the effective constants,
but only in a limited way. They generally did not perform the deliberate
`\chi`-scan or the exact angle/phase sign-pair protocol above. Therefore they
usually bound the product

```math
B_i(D)\chi_{\mathrm{eff}}^4
```

rather than `B_i(D)` itself. If the effective analyzer coupling is not known,
the honest reported quantity is this product.

For an existing event-level Bell dataset with time tags, settings, and
outcomes, the reanalysis is direct. For each setting pair `q`, split events
into two spacelike order bins:

```text
R before S:  t_R-t_S < -T_{\mathrm{guard}},
S before R:  t_R-t_S >  T_{\mathrm{guard}}.
```

Then compute

```math
\widehat E_q^{R\prec S}
=
\frac{N_{++}+N_{--}-N_{+-}-N_{-+}}{N}
\bigg|_{R\prec S,q},
```

```math
\widehat\Omega_q
=
\widehat E_q^{R\prec S}-\widehat E_q^{S\prec R}.
```

The statistical uncertainty is approximately

```math
\sigma^2_{\Omega,q}
=
\frac{1-(\widehat E_q^{R\prec S})^2}{N_{R\prec S,q}}
+
\frac{1-(\widehat E_q^{S\prec R})^2}{N_{S\prec R,q}}
+
\sigma_{\mathrm{sys},q}^2.
```

If the setting pair has ISP shape factor `F_i(q)`, for example
`F_\theta=\sin2(\theta_S-\theta_R)` or
`F_\phi=\sin2\theta_R\sin2\theta_S
\sin(\alpha_R+\alpha_S-\varphi_p)`, then an `n`-sigma event-level bound is

```math
|B_i(D)\chi_{\mathrm{eff}}^4|
\le
\frac{|\widehat\Omega_q|+n\sigma_{\Omega,q}}
{|F_i(q)|}.
```

If `\chi_{\mathrm{eff}}` can be calibrated, this becomes a bound on
`B_i(D)`. If not, it is still a valid operational bound on the measurable
exchange amplitude.

For older visibility/fringe experiments without outcome-by-outcome order
bins, use the fitted fringe

```math
C(\phi)=C_0[1+V\cos(\phi+\phi_0)].
```

Compare the fitted visibility in order-sensitive windows with a reference
visibility:

```math
\Delta V_n
=
|V_1-V_2|
+
n\sqrt{\sigma_{V_1}^2+\sigma_{V_2}^2}
+
\varepsilon_{\mathrm{sys}}.
```

Then, for the matching phase-like channel,

```math
|B_\phi(D)\chi_{\mathrm{eff}}^4|
\lesssim
\Delta V_n.
```

Three existing data sources are immediately useful:

| Experiment | What it can bound | Conservative translation |
| --- | --- | --- |
| Stefanov-Zbinden-Gisin-Suarez before-before test, PRL 2002 | phase/order visibility loss in a moving-beamsplitter configuration | reported two-photon visibility about `0.85 +/- 0.05` and no disappearance over a `55 m` analyzer separation; this gives a coarse `2 sigma` proxy bound `abs(B_\phi\chi_{\mathrm{eff}}^4) <= 0.10` for a before-before phase-channel residual |
| Salart-Baas-Branciard-Gisin-Zbinden speed-of-quantum-information test, Nature 2008 | daily/preferred-frame visibility modulation over long baseline | reported `18 km` separation and a representative fringe visibility `0.876 +/- 0.011`; using the fit uncertainty gives a conditional `3 sigma` proxy `abs(B_\phi\chi_{\mathrm{eff}}^4) <= 0.033`, while the weaker threshold-only Bell bound is about `0.17` |
| Shalm et al. loophole-free photon Bell test, PRL 2015/NIST data | the closest route to the exact `\Omega` statistic | public time-tagged data can be re-binned by spacelike order and settings; the bound is the event-level formula above, with no need to infer from visibility alone |

If one adopts the full-strength analyzer convention
`\chi_{\mathrm{eff}}=\pi/4`, so that `\chi_{\mathrm{eff}}^4=0.3805`, the
Stefanov proxy gives

```math
|B_\phi(55\,\mathrm m)|\lesssim0.26
```

at roughly `2 sigma`, while the Salart fit-error proxy gives

```math
|B_\phi(18\,\mathrm{km})|\lesssim0.087
```

at roughly `3 sigma`. These are not clean final ISP bounds because the
experiments used energy-time/fringe analyzers rather than the exact
polarization phase-quadrature protocol above, and because
`\chi_{\mathrm{eff}}` was not scanned. They are nevertheless useful prior
constraints on large surviving exchange residuals.

The conversion from a bound at one distance to a bound on
`\ell_{\mathrm{ISP}}` requires an assumption about the microscopic coefficient
scale. If an experiment gives

```math
|B_i(D)|\le U_D
```

and one hypothesizes a nonzero microscopic coefficient scale `|A_i|=A_*` for
that channel, then

```math
|A_i|e^{-D/\ell_{\mathrm{ISP}}}\le U_D.
```

For `A_*>U_D`, the null bound excludes decay lengths

```math
\ell_{\mathrm{ISP}}
>
\frac{D}{\log(A_*/U_D)}.
```

Equivalently, with only an upper coefficient prior `|A_i|\le A_*`, the same
formula is not an exclusion; it is merely the sensitivity length that would be
reached for a coefficient of size `A_*`.

For example, if one assumes an order-one coefficient `A_*=1`, the illustrative
full-strength translations above would imply roughly

```math
\ell_{\mathrm{ISP}}\lesssim41\,\mathrm m
```

from the Stefanov proxy, or

```math
\ell_{\mathrm{ISP}}\lesssim7.4\,\mathrm{km}
```

from the Salart fit-error proxy. These numbers are only conditional
orientation scales, not claimed experimental exclusions of ISP. The clean
bound should come from reprocessing public time-tagged Bell data into
`\widehat\Omega_q` and then, ideally, from a dedicated `\chi`-scan.

#### Current numerical guesstimate

The best current theoretical value in the exact relativistic continuum
interpretation is

```math
A_\theta=A_\phi=0,
```

with `\ell_{\mathrm{ISP}}` physically irrelevant for this operational
projection. Any nonzero number below should therefore be read as a
finite-regulator or detector-coupled residual estimate, not as a universal
constant.

Existing data suggest the following conservative phenomenological picture:

| Quantity | Current best estimate | Reason |
| --- | --- | --- |
| `B_\theta(D)` | no direct existing estimate; use `0` as QFT/continuum central value | existing before-before and speed-of-QI experiments constrain phase/fringe channels, not the exact linear-polarization sign pair |
| `B_\phi(55 m)` | central `0`, proxy range roughly `abs(B_\phi) <= 0.26` if `\chi_{\mathrm{eff}}=\pi/4` | Stefanov before-before visibility did not show an order-window change at the `~0.10` product level |
| `B_\phi(18 km)` | central `0`, proxy range roughly `abs(B_\phi) <= 0.087` if `\chi_{\mathrm{eff}}=\pi/4` | Salart long-baseline fringe visibility was stable at the `~0.033` product level |
| `A_\phi` | central `0`; nonzero values below about `0.05` are essentially unconstrained by these proxy bounds | the existing bounds are on `A_\phi e^{-D/\ell}` and do not scan `\chi` |
| `\ell_{\mathrm{ISP}}` | no direct fitted value; only conditional upper scales | no nonzero residual has been detected at two distances in the same channel |

If one nevertheless uses these proxy bounds as priors and assumes a nonzero
microscopic `A_\phi=A_*`, the combined conditional length scales are:

| Assumed `A_*` | Approximate combined implication |
| --- | --- |
| `1` | `\ell_{\mathrm{ISP}} <= 41 m` |
| `0.5` | `\ell_{\mathrm{ISP}} <= 86 m` |
| `0.3` | `\ell_{\mathrm{ISP}} <= 416 m` |
| `0.2` | `\ell_{\mathrm{ISP}} <= 21.5 km` |
| `0.1` | `\ell_{\mathrm{ISP}} <= 126 km` |
| `<=0.05` | no useful proxy length bound |

Thus a compact guesstimate is:

```text
continuum/QFT-compatible central value: A_theta = A_phi = 0;
large long-range residuals with A_phi ~ 1 are already strongly disfavored;
small residuals A_phi <= 0.05, or exact polarization-angle residuals A_theta,
remain essentially open without a dedicated order-asymmetry chi-scan.
```

For the dedicated `L=1 km` proposal, the proxy priors imply a very different
expected scale depending on `A_*`. If `A_\phi=1` and the Stefanov proxy is
taken literally, then at the proposed spacelike margin `D=0.939 km`,

```math
|B_\phi(D)|\lesssim1.3\times10^{-10},
\qquad
|\Omega|_{\chi=\pi/4}\lesssim4.8\times10^{-11}.
```

That would be experimentally invisible. But if `A_\phi=0.1`, existing proxy
data still allow long decay lengths and a dedicated experiment could in
principle see an order-asymmetry as large as

```math
|\Omega|_{\chi=\pi/4}\sim10^{-2}\text{--}10^{-1},
```

unless the exact polarization/channel projection kills it. This is why the
dedicated test is useful: it measures the actual operational projection rather
than importing a visibility proxy from a different interferometer geometry.

#### Design implication from likely values

Given the current priors, this photon order-asymmetry experiment should be
presented as a precision bound, not as the most likely discovery experiment.
The central value predicted by both standard relativistic QFT and a clean
Lorentz-invariant ISP continuum limit is

```math
\Omega=0.
```

The experimental design should therefore use blind analysis and report
upper limits on `B_\theta(D)` and `B_\phi(D)` as the primary deliverable. A
nonzero claim is credible only if it passes the sign-flip, null-setting,
`\chi^4` onset, distance-decay, and marginal no-signaling controls below.
Without that full pattern, the correct interpretation is detector bias or
timing/calibration leakage.

This conclusion also points to a different kind of non-simulator test. If
spacelike exchange constants are most likely zero, then the more distinctive
place to look is not spacelike order, but the measurement ontology itself:
whether a stable detector record can be coherently erased as ordinary QFT says
it can. In the strong measurement-solution version of ISP, the answer is no:
once an actual record-sector event has formed, it is not a reversible coherent
marker.

#### Concrete prediction table

Define

```math
B_\theta=A_\theta e^{-D/\ell_{\mathrm{ISP}}},
\qquad
B_\phi=A_\phi e^{-D/\ell_{\mathrm{ISP}}}.
```

Primary linear-angle run:

```text
pair phase:       varphi_p = 0
local phases:     alpha_R = alpha_S = 0
photon frequency: f_R = f_S = 193.40 THz
```

Use the following analyzer settings:

```math
(\theta_R,\theta_S)
\in
\{(0^\circ,45^\circ),\ (0^\circ,-45^\circ),\ (0^\circ,0^\circ),\
(22.5^\circ,-22.5^\circ)\}.
```

The specific order-asymmetry predictions are

```math
\Omega_{\mathrm{QFT}}=0
\quad\text{for every row},
```

while the ISP template gives

```math
\Omega(0^\circ,45^\circ)
=
+B_\theta\chi^4,
```

```math
\Omega(0^\circ,-45^\circ)
=
-B_\theta\chi^4,
```

```math
\Omega(0^\circ,0^\circ)=0,
```

```math
\Omega(22.5^\circ,-22.5^\circ)
=
-B_\theta\chi^4,
```

for equal coupling strengths `\chi_R=\chi_S=\chi`, up to higher-order and
detector terms.

Phase-quadrature run:

```text
pair phase:       varphi_p = 0
analyzer angles:  theta_R = theta_S = 45 degrees
photon frequency: f_R = f_S = 193.40 THz
```

Set `\alpha_R=0` and use

```math
\alpha_S\in\{0,\ \pi/2,\ -\pi/2,\ \pi\}.
```

Then QFT predicts the ordinary correlation values

```math
E_{\mathrm{QFT}}\in\{+1,\ 0,\ 0,\ -1\}
```

respectively, again with no order asymmetry. The ISP phase-channel template
predicts

```math
\Omega(45^\circ,0;\,45^\circ,\pi/2)
=
+B_\phi\chi^4,
```

```math
\Omega(45^\circ,0;\,45^\circ,-\pi/2)
=
-B_\phi\chi^4,
```

```math
\Omega(45^\circ,0;\,45^\circ,0)
=
\Omega(45^\circ,0;\,45^\circ,\pi)
=0.
```

This phase run is useful because the ordinary QFT correlation deliberately
moves through `+V,0,-V`, while the order-asymmetry statistic remains exactly
zero in QFT.

Vary

```math
\chi\in\{\pi/16,\ \pi/8,\ 3\pi/16,\ \pi/4\}
```

by changing the electro-optic retardance amplitude. A genuine ISP exchange
signal should scale approximately as `\chi^4` at small `\chi`; halving `\chi`
should suppress the signal by roughly `16`.

Numerically,

```math
\chi^4\in
\{1.49\times10^{-3},\ 2.38\times10^{-2},\
1.20\times10^{-1},\ 3.81\times10^{-1}\}.
```

For example, if the effective benchmark coefficient were
`B_\theta=10^{-3}`, the largest-coupling linear-angle run would give
`|\Omega|\simeq3.8\times10^{-4}`. This number is not a universal ISP
prediction; it is the experimental sensitivity scale needed to make the test
informative for a coefficient of that size.

#### Required controls

The test is meaningful only if the following null checks pass:

1. **marginal no-signaling:** local marginal probabilities at `R` and `S` do
   not change with order;
2. **null settings:** `\Omega(0^\circ,0^\circ)` and the phase nulls
   `\Omega(45^\circ,0;\,45^\circ,0)`,
   `\Omega(45^\circ,0;\,45^\circ,\pi)` are consistent with zero;
3. **sign flip:** `\Omega(0^\circ,45^\circ)` and
   `\Omega(0^\circ,-45^\circ)` have opposite signs, and likewise for
   `\Omega(45^\circ,0;\,45^\circ,\pi/2)` and
   `\Omega(45^\circ,0;\,45^\circ,-\pi/2)`;
4. **coupling onset:** the residual scales as `\chi^4`;
5. **distance test:** increasing `L` suppresses the residual;
6. **delay symmetry:** changing `\tau` while preserving spacelike separation
   changes only the predicted spacelike-margin factor, not detector biases;
7. **Bell calibration:** the same apparatus reproduces the expected
   `|\Phi_{\varphi_p}\rangle` correlations

```math
E(\theta_R,\alpha_R;\theta_S,\alpha_S)
=
V
\left[
\cos2\theta_R\cos2\theta_S
+
\sin2\theta_R\sin2\theta_S
\cos(\alpha_R+\alpha_S-\varphi_p)
\right]
```

independent of order within statistical error.

#### Statistical target

For each setting/order/coupling bin collect enough coincidences that

```math
\sigma_\Omega\lesssim10^{-4}
```

or whatever level is below the independently bounded detector residual. Since
correlation shot noise scales as `N^{-1/2}`, this requires roughly

```math
N\gtrsim10^8
```

valid coincidence events per tested configuration for a `10^{-4}` target.

#### Interpretation

The result would differentiate relativistic ISP from standard QFT only if the
measured order asymmetry is:

```text
nonzero,
correlation-only,
odd under angle reversal,
fourth order in local coupling,
suppressed by separation,
stable under detector calibration,
and not present in QFT detector modeling.
```

A null result does not kill ISP; it bounds `B_\theta(D)` and `B_\phi(D)` for
this operational family, or equivalently the allowed region of
`A_\theta,A_\phi,\ell_{\mathrm{ISP}}`. A nonzero result without the sign,
coupling, distance, and marginal controls is just detector/systematic error.

### Relativistic Null Proposal: Three-Station Hypersurface-Loop Test

Even if the expected exchange-order constants are zero, relativistic ISP still
makes a sharp operational demand: changing the spacelike hypersurface order of
localized record events must not change the final joint record probabilities.
The right experiment is therefore a null test for operational hypersurface-loop
holonomy.

Use a three-photon polarization GHZ source

```math
|{\mathrm{GHZ}}_{\varphi}\rangle
=
\frac{|H\rangle_A|H\rangle_B|H\rangle_C
+e^{i\varphi}|V\rangle_A|V\rangle_B|V\rangle_C}{\sqrt2}.
```

A telecom implementation may use photons near

```math
\lambda_A=\lambda_B=\lambda_C\simeq1550\,\mathrm{nm},
\qquad
f_\gamma\simeq193.4\,\mathrm{THz},
```

generated directly or by pair-source fusion/entanglement swapping. Place three
measurement stations `A,B,C` at the vertices of an approximately equilateral
triangle with side length

```math
L=1\,\mathrm{km}.
```

The light-crossing time between stations is then about `3.3 microseconds`.
Use fast electro-optic analyzers and single-photon detectors with

```math
T_{\mathrm{gate}}=2\,\mathrm{ns},
\qquad
T_{\mathrm{jitter}}\le0.1\,\mathrm{ns}.
```

For each run, trigger the three measurement events in one of the six lab-time
permutations:

```text
A before B before C,
A before C before B,
B before A before C,
B before C before A,
C before A before B,
C before B before A.
```

Use nominal adjacent time offsets of `200 ns`, so the total span between first
and last trigger is `400 ns`. Since `c(400 ns+2T_gate+T_jitter)<<1 km`, every
pair of measurement events remains spacelike separated. Randomize the
permutation from shot to shot or block to block.

For an event pair `i,j`, define the operational spacelike margin

```math
D_{ij}:=
\sqrt{L_{ij}^{2}-c^{2}(\Delta t_{ij}+2T_{\mathrm{gate}}
+T_{\mathrm{jitter}})^{2}},
```

and require `D_{ij}>0` for all three pairs and all six permutations. The loop
margin used below is

```math
D_{\mathrm{loop}}:=\min\{D_{AB},D_{BC},D_{CA}\}.
```

For the nominal `L=1 km`, `\Delta t\le400 ns` design,
`D_{\mathrm{loop}}` is still of order `1 km`, not a laboratory-scale timing
edge effect.

Each station measures in the equatorial polarization basis

```math
|\pm;\alpha_j\rangle
=
\frac{|H\rangle\pm e^{i\alpha_j}|V\rangle}{\sqrt2},
\qquad
j\in\{A,B,C\},
```

with outcomes

```math
a,b,c\in\{+1,-1\}.
```

#### QFT and clean relativistic ISP prediction

For standard relativistic QFT, and for the clean Lorentz-invariant operational
limit of relativistic ISP, the joint distribution is independent of the
spacelike ordering permutation `\pi`. With visibility `V`,

```math
P_{\mathrm{QFT}}(a,b,c|\alpha_A,\alpha_B,\alpha_C;\pi)
=
\frac18
\left[
1+abc\,V\cos(\alpha_A+\alpha_B+\alpha_C-\varphi)
\right].
```

Thus the triple correlator

```math
E_\pi(q):=\sum_{a,b,c=\pm1}abc\,
P(a,b,c|q;\pi),
```

where `q=(\alpha_A,\alpha_B,\alpha_C)`, satisfies

```math
E_\pi(q)=V\cos(\alpha_A+\alpha_B+\alpha_C-\varphi)
```

for every permutation `\pi`. All single-station and two-station marginals are
also permutation-independent.

This is the relativistic ISP null statement:

```math
\Omega_\pi(q):=E_\pi(q)-E_{\pi_0}(q)=0
```

for all permutations `\pi`, relative to any reference permutation `\pi_0`.

#### Hypersurface-loop statistic

Define the orientation-antisymmetric loop statistic

```math
\Lambda(q)
:=
\frac16
\left[
E_{A\prec B\prec C}(q)
+E_{B\prec C\prec A}(q)
+E_{C\prec A\prec B}(q)
-E_{A\prec C\prec B}(q)
-E_{C\prec B\prec A}(q)
-E_{B\prec A\prec C}(q)
\right].
```

QFT predicts

```math
\Lambda_{\mathrm{QFT}}(q)=0.
```

Clean relativistic ISP also predicts

```math
\Lambda_{\mathrm{rISP}}(q)=0.
```

If a finite-regulator or detector-coupled relativistic ISP residual survives,
a minimal falsifiable template is

```math
\Lambda_{\mathrm{res}}(q)
=
C_{\mathrm{loop}}\,
\chi_A^2\chi_B^2\chi_C^2
e^{-D_{\mathrm{loop}}/\ell_{\mathrm{loop}}}
\sin(\alpha_A+\alpha_B+\alpha_C-\varphi)
+O(\chi^8)
+\varepsilon_{\mathrm{det}},
```

where `C_{\mathrm{loop}}` is an effective three-anchor loop coefficient and
`D_{\mathrm{loop}}` is the minimum spacelike margin over the three station
pairs. The current-prior value is

```math
C_{\mathrm{loop}}=0.
```

The experiment is still meaningful because it directly bounds this loop
coefficient and tests the relativistic ISP requirement of hypersurface
independence.

The reason for using three stations is structural. With two spacelike stations
one can test an order asymmetry, but not a closed hypersurface loop. Three
stations allow the six local orderings to be arranged into two orientations of
the same operational loop. A nonzero orientation-antisymmetric component is the
finite-experiment analogue of probability holonomy under a closed deformation
of the comparison hypersurface.

#### Concrete settings

Set the source phase to `\varphi=0` and use:

| Setting `q` | QFT triple correlator | Loop-residual template |
| --- | --- | --- |
| `(0,0,0)` | `+V` | `0` |
| `(0,0,\pi)` | `-V` | `0` |
| `(0,0,\pi/2)` | `0` | `+C_{\mathrm{loop}}\chi^6e^{-D_{\mathrm{loop}}/\ell_{\mathrm{loop}}}` |
| `(0,0,-\pi/2)` | `0` | `-C_{\mathrm{loop}}\chi^6e^{-D_{\mathrm{loop}}/\ell_{\mathrm{loop}}}` |

For the coupling scan, use

```math
\chi\in\{\pi/8,\ 3\pi/16,\ \pi/4\},
```

with equal analyzer-coupling strength at the three stations. A genuine
three-anchor residual should scale as `\chi^6` at small coupling. Standard QFT
and clean relativistic ISP predict zero loop statistic for every `\chi`.

#### Statistical target and controls

The directly measured quantity is `\Lambda(q)`. If `N` valid threefold
coincidences are collected per setting and permutation, equal-count independent
correlators give

```math
\sigma_\Lambda^2
\simeq
\frac1{36}\sum_{\pi}\frac{1-E_\pi(q)^2}{N_\pi}
\le
\frac1{6N}.
```

In practice source drift and detector drift are likely larger than this ideal
counting floor, so the conservative planning scale is `N^{-1/2}` per correlator.
A first useful target is

```math
\sigma_\Lambda\lesssim10^{-3},
```

which requires roughly

```math
N\gtrsim10^6
```

threefold coincidences per setting/permutation. A `10^{-4}` target would be
much more demanding and likely requires long integration or brighter
multipartite sources.

The pre-registered pass criterion for the relativistic ISP null test is

```math
|\Lambda(q)|\le
5\sqrt{\sigma_{\mathrm{stat}}(q)^2+\sigma_{\mathrm{sys}}(q)^2}
```

for all four phase settings and all coupling strengths, with the marginal
controls below satisfied. Failure of this criterion is not automatically a
discovery; it becomes physically interesting only if it has the phase, ordering,
and coupling signatures specified here.

Required controls:

1. **GHZ calibration:** the same data reproduce
   `E(q)=V\cos(\alpha_A+\alpha_B+\alpha_C-\varphi)` after averaging over
   permutations.
2. **Permutation blinding:** permutation labels are randomized and analyzed
   blindly.
3. **Marginal no-signaling:** all one- and two-station marginals are
   independent of remote settings and permutation.
4. **Sign flip:** any nonzero loop statistic flips sign between
   `(0,0,\pi/2)` and `(0,0,-\pi/2)`.
5. **Null settings:** `(0,0,0)` and `(0,0,\pi)` give `\Lambda=0`.
6. **Coupling onset:** any residual scales as `\chi^6`.
7. **Spacelike-margin test:** increasing `L` or reducing the trigger span
   suppresses any finite-margin residual.

#### Interpretation

This is not a likely nonzero-discovery experiment. It is a relativistic ISP
consistency test. The expected result is

```math
\Lambda(q)=0
```

within experimental uncertainty. That null result checks the operational
content of relativistic ISP: no detectable probability holonomy around a
closed loop of spacelike hypersurface deformations.

Thus the experiment has a clean logical status:

```text
QFT prediction:                      pass, Lambda = 0.
Clean relativistic ISP prediction:   pass, Lambda = 0.
Regulated rISP with loop residual:   possible fail, with chi^6 and phase signs.
Generic detector/systematic error:   fail controls or fail marginal tests.
```

A nonzero `\Lambda` would be serious only if it is correlation-only,
permutation-antisymmetric, sign-flipping in the phase setting, has the
predicted coupling onset, and survives all marginal/no-signaling controls.
Otherwise it is detector drift, source drift, timing leakage, or ordinary
postselection bias. A clean null bounds `C_{\mathrm{loop}}
e^{-D_{\mathrm{loop}}/\ell_{\mathrm{loop}}}` for a genuine three-anchor
relativistic ISP loop residual.

### Second Non-Simulator Proposal: Mesoscopic Record-Erasure Threshold Test

The photon order-asymmetry experiment is the clean spacetime test, but the
likely value of its exchange constants is zero. The sharper non-simulator test
of Paper 4's measurement ontology is therefore a record-erasure threshold
experiment. This is primarily a **vanilla ISP** test, not a specifically
relativistic ISP test. It does not use spacelike separation, exchange defects,
or hypersurface-order residuals. It tests the finite ISP claim that a formed
measurement record is a real stochastic event, not a reversible coherent
marker.

It still belongs in Paper 4 because Paper 4 is the operational layer: it asks
which detector procedures and record events can be promoted from raw kernel
data to physical measurement claims. The experiment asks whether a physical
process that standard quantum theory models as a reversible which-path marker
has crossed the ISP threshold into an actual detector record.

The strong ISP record postulate is:

```text
Hypothesis RTH: sufficiently stable finite detector records define objective
record sectors, and once such a sector is formed, coherent erasure is
operationally impossible. An operation may erase a pre-record marker, but not a
formed record-sector event.
```

Thus the ambiguity is not whether ISP permits erasure of records. It does not.
The ambiguity is whether the laboratory interaction has formed a record, or
only a reversible pre-record correlation. The experiment scans that boundary.

#### Conditional expectation if ISP is true

If vanilla ISP is true and standard QFT is only an approximation, the expected
pattern is not a tiny correction everywhere. It is a boundary phenomenon:

| Regime | Operational situation | Expected result if ISP is true |
| --- | --- | --- |
| weak marker | small `n`, little redundancy, short lifetime | erasure works: `\mathcal R_{\mathrm{er}}\simeq1` |
| strong coherent marker | high distinguishability but still controlled | erasure may still work; this remains pre-record territory |
| formed record | repeatable, redundant, long-lived sector event | erasure fails: `\mathcal R_{\mathrm{er}}<1` |
| amplified classical record | many uncontrolled degrees of freedom | erasure fails; QFT also predicts practical failure |

Thus the likely first run with `M=1` and only a few cavity photons may still
look QFT-like even if ISP is true. A meaningful positive test should scan

```math
M_{\mathrm{eff}},
\qquad
T_{\mathrm{hold}},
\qquad
R(n,M),
\qquad
F_{\mathrm{rep}},
\qquad
\text{amplification strength}.
```

The ISP-positive signature is not merely reduced visibility. It is that the
visibility deficit turns on at the same operational point where the apparatus
crosses from reversible marker to stable record.

#### Physical platform

Use a circuit-QED Ramsey interferometer. The two interferometer paths are the
states of a superconducting qubit:

```math
|0\rangle:=|g\rangle,
\qquad
|1\rangle:=|e\rangle.
```

For definiteness use nominal frequencies

```math
f_q\simeq5\,\mathrm{GHz},
\qquad
f_c\simeq7\,\mathrm{GHz},
```

with dispersive qubit-cavity coupling

```math
H_{\mathrm{int}}/\hbar
=
-\chi_{qc}\,a^\dagger a\,\sigma_z,
\qquad
\chi_{qc}/2\pi\simeq1\,\mathrm{MHz}.
```

The cavity starts near vacuum. A conditional measurement pulse writes a
mesoscopic pointer record into the cavity:

```math
\frac{|g\rangle+e^{i\phi}|e\rangle}{\sqrt2}|0\rangle_c
\longmapsto
\frac{|g\rangle|\alpha\rangle_c
+e^{i\phi}|e\rangle|-\alpha\rangle_c}{\sqrt2}.
```

Let

```math
n:=|\alpha|^2
```

be the mean number of cavity photons in either pointer packet. The overlap of
the two pointer states is

```math
\gamma(n)
=
\langle\alpha|-\alpha\rangle
=
e^{-2n}.
```

The record distinguishability parameter is

```math
R(n):=1-|\gamma(n)|^2
=
1-e^{-4n}.
```

An optional fan-out stage can redundantly write the same pointer into `M`
nearly independent temporal modes. Then

```math
\gamma(n,M)=e^{-2Mn},
\qquad
R(n,M)=1-e^{-4Mn}.
```

The simplest first run uses `M=1`; later runs vary `M` to test redundancy.

#### Protocol

For each record strength

```math
n\in\{0,\ 0.05,\ 0.10,\ 0.25,\ 0.50,\ 1.0,\ 2.0,\ 4.0\},
```

perform three branches.

1. **No-record Ramsey calibration.** Do the Ramsey sequence without the
   conditional cavity pulse and fit

```math
P_e(\phi)
=
\frac12[1+V_0\cos(\phi+\phi_0)].
```

2. **Record, no erasure.** Apply the conditional cavity pulse, ignore the
   cavity, and fit the qubit Ramsey fringe. This verifies ordinary which-record
   dephasing.

3. **Record plus attempted coherent erasure.** Apply the conditional cavity
   pulse, then apply the calibrated inverse operation before any irreversible
   amplification or classical readout. Verify by cavity tomography or
   calibrated homodyne that the cavity returns to the ready state with reversal
   fidelity `F_{\mathrm{rev}}(n)` according to the ordinary Hilbert/cavity
   model.

The measured observable is the erased-fringe visibility ratio

```math
\mathcal R_{\mathrm{er}}(n)
:=
\frac{V_{\mathrm{er}}(n)}
{V_0F_{\mathrm{rev}}(n)e^{-t/T_2}},
```

where `t` is the sequence duration and `T_2` is independently measured. This
normalization removes ordinary decoherence and imperfect reversal.

Also measure immediate record repeatability before erasure:

```math
F_{\mathrm{rep}}(n)
:=
\Pr(\text{same record on immediate reread}).
```

Define the record-stability score

```math
S(n):=R(n)F_{\mathrm{rep}}(n).
```

#### How to tell marker from record

The experiment cannot decide this by vocabulary. It must pre-register an
operational record-formation criterion. A reversible marker is a controlled
correlation that carries which-path information but can still be returned to
the ready state with full normalized fringe recovery. An ISP record is a
stable sector event.

Use the following diagnostic hierarchy.

First define a **candidate record** before attempting erasure. It must pass:

| Diagnostic | Definition | Example threshold |
| --- | --- | --- |
| distinguishability | `R(n,M)=1-e^{-4Mn}` | `R>=0.90` |
| repeatability | same outcome on immediate reread | `F_{\mathrm{rep}}>=0.99` |
| redundancy | number of independently readable copies/modes | `M_{\mathrm{eff}}>=2` |
| lifetime | same record after a hold time `T_{\mathrm{hold}}` | `F_{\mathrm{life}}>=0.99` |

Here

```math
F_{\mathrm{life}}(n,T_{\mathrm{hold}})
:=
\Pr(\text{same record after }T_{\mathrm{hold}}).
```

A compact pre-erasure score is

```math
S_{\mathrm{cand}}
=
R(n,M)F_{\mathrm{rep}}F_{\mathrm{life}}.
```

The experiment should choose thresholds such as

```math
S_{\mathrm{cand}}\ge0.90,
\qquad
M_{\mathrm{eff}}\ge2,
```

before looking at erasure data. These numbers are not universal constants;
they are the declared operational standard for saying that the apparatus made
a record-quality event rather than a weak reversible marker.

Then attempt coherent erasure. A **reversible pre-record marker** is diagnosed
when

```math
\mathcal R_{\mathrm{er}}(n)=1
```

within the pre-registered uncertainty, after correcting by
`F_{\mathrm{rev}}(n)` and auditing all leaked modes. In that case the operation
carried which-path information, but it did not create an ISP record.

A **formed ISP record** is diagnosed only if the candidate record conditions
hold and the attempted erasure leaves a residual deficit

```math
\Delta_{\mathrm{rec}}(n)
=
1-\mathcal R_{\mathrm{er}}(n)
\ge
\delta_{\mathrm{rec}},
```

with, for example, `\delta_{\mathrm{rec}}=0.01` after systematic errors. This
last condition is what separates a record-sector event from an ordinary
controlled ancilla marker.

This makes the test falsifiable. If the pre-registered record-quality
conditions are met at large `n` and `M_{\mathrm{eff}}`, but
`\mathcal R_{\mathrm{er}}=1` within error, then either the experiment has still
not reached the ISP record threshold, or the strong ISP record postulate is
false for that physical regime. Raising `M_{\mathrm{eff}}`,
`T_{\mathrm{hold}}`, and amplification strength is the way to close the first
loophole.

#### How to certify a real discrepancy with standard QFT

A failed erasure is not by itself a discrepancy with standard relativistic
QFT. Standard QFT already predicts failed erasure whenever uncontrolled
degrees of freedom carry away which-record information. The discrepancy exists
only if the failure remains after the ordinary QFT leakage account has been
closed.

The experiment must therefore pre-register a QFT/open-system null model

```math
\mathcal M_{\mathrm{QFT}}
=
(H_{\mathrm{qubit+cavity}},
\kappa,\eta_{\mathrm{det}},T_1,T_2,
\eta_{\mathrm{coll}},F_{\mathrm{rev}},\ldots),
```

where the parameters are calibrated without using the threshold-claim data.
This model predicts a corrected visibility

```math
\mathcal R_{\mathrm{er}}^{\mathcal M_{\mathrm{QFT}}}(n)
=
1\pm\epsilon_{\mathrm{QFT}}(n).
```

Define the observed residual

```math
Z(n)
:=
\frac{
1-\mathcal R_{\mathrm{er}}^{\mathrm{obs}}(n)}
{\sqrt{\sigma_{\mathrm{stat}}^2(n)+
\sigma_{\mathrm{sys}}^2(n)+
\epsilon_{\mathrm{QFT}}^2(n)}}.
```

A genuine discrepancy claim requires all of the following.

1. **Pre-registered QFT null:** the Hamiltonian, damping, detector efficiency,
   collection efficiency, reversal fidelity, and analysis window are fixed
   before looking at the record-threshold residual.
2. **Leakage closure:** every channel that can carry which-record information
   is either reversed, measured, or bounded. Uncollected radiation, amplifier
   modes, phonons, quasiparticles, thermal photons, and control-line leakage
   count as QFT explanations unless independently bounded.
3. **Large residual:** for candidate records, `Z(n)>=5` or another
   pre-registered discovery threshold.
4. **No residual below threshold:** weak reversible markers with
   `S_{\mathrm{cand}}` below threshold satisfy
   `\mathcal R_{\mathrm{er}}=1` within error.
5. **Record-onset scaling:** the residual tracks `S_{\mathrm{cand}}`,
   `M_{\mathrm{eff}}`, and `T_{\mathrm{hold}}`, not merely pulse power,
   cavity loss, or sequence time.
6. **Improved reversal does not remove it:** increasing
   `F_{\mathrm{rev}}` and measured collection efficiency reduces ordinary QFT
   loss but leaves the threshold-correlated residual.
7. **Wrong-erasure control:** intentionally using a wrong inverse destroys
   recovery at all strengths, confirming that the right inverse is really doing
   coherent reversal in the pre-record regime.
8. **Irreversible-readout control:** after genuine amplification/classical
   readout, both QFT and ISP predict no coherent erasure. This branch verifies
   that the apparatus can distinguish reversible markers from ordinary
   irreversible records.

If any uncontrolled leakage channel can explain the deficit within its error
bar, the result is not a QFT discrepancy. It is ordinary decoherence. The
distinctive ISP signature is a residual that appears only after independently
certified record formation, while the same apparatus demonstrably erases
pre-record markers.

#### Prior experimental status

Experiments adjacent to this test already exist, and they mostly support the
standard QFT account in the reversible or weak-measurement regime.

1. Optical quantum eraser experiments show that interference can be recovered
   when which-path information is made unavailable or postselected in an erasing
   basis. These are tests of reversible markers, not redundant stable records.
2. Weak-measurement reversal has been proposed and demonstrated in
   superconducting qubits. These experiments show conditional recovery after
   partial measurement, with success probability decreasing as measurement
   strength increases. They do not demonstrate erasure of a completed
   macroscopic record.
3. Circuit-QED analyses show that measurement-induced dephasing can be undone
   when the measurement signal is fully accounted for. This is precisely the
   QFT/null-model expectation used above.

So the proposed ISP experiment is not "has erasure ever worked?" It has. The
new question is:

```text
Does erasure still work after the apparatus has produced a pre-registered,
repeatable, redundant, long-lived record-quality event?
```

That exact record-threshold test, with leakage closure and a pre-registered
QFT null model, is not known to have been performed.

#### Standard QFT prediction

Standard QFT/quantum theory predicts no objective record threshold. If the
record interaction is coherently reversed and all leaked degrees of freedom are
accounted for by `F_{\mathrm{rev}}`, then

```math
V_{\mathrm{no\,er}}^{\mathrm{QFT}}(n)
=
V_0e^{-2n}e^{-t/T_2},
```

and

```math
V_{\mathrm{er}}^{\mathrm{QFT}}(n)
=
V_0F_{\mathrm{rev}}(n)e^{-t/T_2}.
```

Equivalently,

```math
\mathcal R_{\mathrm{er}}^{\mathrm{QFT}}(n)=1
```

for every `n`, up to independently measured experimental imperfections.

#### ISP record-threshold prediction

Strong ISP predicts an extra visibility deficit when the record-stability score
crosses a threshold. A minimal falsifiable form is

```math
\mathcal R_{\mathrm{er}}^{\mathrm{ISP}}(n)
=
1-\rho_{\mathrm{rec}}\,p_{\mathrm{rec}}(S(n)),
```

where

```math
p_{\mathrm{rec}}(S)
=
\frac1{1+\exp[-(S-S_c)/w]}.
```

Here:

| Symbol | Meaning | Range |
| --- | --- | --- |
| `S_c` | record-sector threshold | `0<S_c<1` |
| `w` | threshold width | `w>0`; sharp threshold means small `w` |
| `\rho_{\mathrm{rec}}` | irreversible visibility-loss fraction after threshold | `0<=\rho_{\mathrm{rec}}<=1` |

The QFT limit is recovered by setting `\rho_{\mathrm{rec}}=0`, but that is not
the strong-ISP record prediction. In strong ISP, `\rho_{\mathrm{rec}}>0` once
the tested operation has formed an actual record-sector event.

#### Concrete prediction table

For `M=1`, the basic record strengths are:

| `n` | `e^{-2n}` | `R(n)=1-e^{-4n}` | QFT `V_no/V_0` | QFT `R_er` |
| --- | --- | --- | --- | --- |
| `0.05` | `0.905` | `0.181` | `0.905` | `1` |
| `0.10` | `0.819` | `0.330` | `0.819` | `1` |
| `0.25` | `0.607` | `0.632` | `0.607` | `1` |
| `0.50` | `0.368` | `0.865` | `0.368` | `1` |
| `1.00` | `0.135` | `0.982` | `0.135` | `1` |
| `2.00` | `0.018` | `0.9997` | `0.018` | `1` |

As an illustrative ISP-threshold benchmark, choose

```math
S_c=0.90,
\qquad
w=0.02,
\qquad
\rho_{\mathrm{rec}}=0.20,
\qquad
F_{\mathrm{rep}}\simeq1.
```

Then the prediction is approximately:

| `n` | QFT `R_er` | ISP-threshold example `R_er` |
| --- | --- | --- |
| `0.10` | `1.00` | `1.00` |
| `0.25` | `1.00` | `1.00` |
| `0.50` | `1.00` | about `0.97` |
| `1.00` | `1.00` | about `0.80` |
| `2.00` | `1.00` | about `0.80` |

Thus the directly measurable difference is

```math
\Delta_{\mathrm{rec}}(n)
:=
1-\mathcal R_{\mathrm{er}}(n).
```

Standard QFT predicts

```math
\Delta_{\mathrm{rec}}^{\mathrm{QFT}}(n)=0,
```

while the illustrative threshold model predicts a sharp or rounded onset near
the record-strength where `S(n)` crosses `S_c`.

#### Statistical target and controls

Use at least eight Ramsey phases

```math
\phi_k=2\pi k/8,
\qquad
k=0,\ldots,7,
```

and at least

```math
N_{\mathrm{shots}}\gtrsim10^5
```

shots per phase and record strength. This gives sub-percent visibility
precision in ordinary binomial scaling, before systematics.

Required controls:

1. **No-record calibration:** `V_0` is stable over the scan.
2. **No-erasure check:** `V_{\mathrm{no\,er}}/V_0` follows `e^{-2n}`.
3. **Reversal tomography:** the cavity after erasure is independently close to
   the ready state, giving `F_{\mathrm{rev}}(n)`.
4. **Leakage audit:** any emitted or amplified field before erasure is measured
   and included in `F_{\mathrm{rev}}`.
5. **Repeatability audit:** `F_{\mathrm{rep}}(n)` is measured separately.
6. **Order randomization:** runs with different `n` and branches are randomized
   to remove drift.
7. **Classical irreversible branch:** after actual amplification/readout, both
   QFT and ISP should predict no coherent erasure. This verifies that the test
   distinguishes reversible records from ordinary irreversible readout.

#### Interpretation

A result consistent with

```math
\mathcal R_{\mathrm{er}}(n)=1
```

for all tested `n`, including large `S(n)`, supports the standard QFT view that
measurement irreversibility is practical/environmental unless actual
uncontrolled degrees of freedom have carried away the record. For strong ISP,
this would mean either that the experiment never formed a true record-sector
event, or that the strong record postulate is false in this regime.

A reproducible deficit

```math
\mathcal R_{\mathrm{er}}(n)<1
```

that turns on with `S(n)`, survives reversal tomography, and is absent in
small-`n` controls would be a genuine measurable difference from standard QFT.
It would support the strong ISP claim that formed records cannot be coherently
erased. Without that onset pattern, an erasure deficit is just ordinary loss,
leakage, or bad calibration.

## 14. Operational Underdetermination And No-Go

The positive theorems above are reconstruction theorems relative to a declared
operational family `\mathcal O_a`. They do not imply that a single primitive
endpoint kernel determines all observables, phases, or detector couplings.

### Theorem 21: declared-family underdetermination

Let two candidate microscopic theories `T` and `T'` have the same finite
operational family `\mathcal O_a` in the following sense:

1. the same preparation set `\mathcal P_a`;
2. the same final effect set `\mathcal E_a`;
3. the same declared control labels, detector record spaces, readout schemes,
   and sequential composition domain;
4. for every declared operation string `s` in `\mathcal O_a`, the same
   stochastic operation

```math
\mathsf K_s^T=\mathsf K_s^{T'}.
```

Then the two theories are operationally indistinguishable inside
`\mathcal O_a`:

```math
e^T\mathsf K_s^Tp
=
e^T\mathsf K_s^{T'}p
```

for every declared preparation `p`, effect `e`, and operation string `s`.

Proof. Every statistic generated by `\mathcal O_a` is, by definition, obtained
by composing one of the declared stochastic operations with a declared
preparation and effect. The composed operation is identical in the two
theories, so the scalar statistic is identical. `square`

This theorem is tautological in the good sense: it says exactly where empirical
content lives. A hidden microscopic distinction is not physical for Paper 4
unless it changes some declared preparation-control-detector-readout statistic.

### Corollary 22: one primitive kernel is insufficient

A single primitive endpoint kernel `\Gamma` cannot determine the operational
observable theory unless the allowed control and detector family is also fixed.
In particular, from one `\Gamma` alone one cannot infer:

1. which phase controls `\Gamma_\phi` are physically available;
2. which detector couplings can write stable records;
3. whether coherent erasure operations are available;
4. which calibrated responses are anchored in the Paper 3 topology;
5. which local operational equivalence classes should count as observables.

Proof. Construct two operational families with the same bare reference kernel
`\Gamma_0` but different additional controls or detectors. Theorem 21 says
statistics agree only on the common declared subfamily. Any statistic involving
a control or detector absent from one family is not determined by `\Gamma_0`.
The two-path benchmark in Section 8 is the minimal explicit witness:
`\Gamma_\phi` as a controlled family contains phase-fringe information, while
one fixed endpoint kernel contains only one transition matrix. `square`

### Corollary 23: phase-data no-go

If the declared operational family contains only uncontrolled endpoint kernels
and no interferometric control family capable of varying or detecting relative
phase, then no observable reconstructed from that family can distinguish two
microscopic theories that agree on those endpoint kernels but differ only in
phase-sensitive amplitudes outside the declared controls.

Equivalently, ISP may address the finite definite-outcome problem by records and
conditioning while still failing to reconstruct standard quantum phase physics
unless the phase-sensitive controlled-kernel family is part of the operational
data.

### Failure classification

Paper 4 should classify failures as follows.

1. **Benign incompleteness:** a statistic is absent because the relevant
   detector or control was not declared in `\mathcal O_a`.
2. **Model-building failure:** the detector is declared, but its calibrated
   response is not anchored, so Paper 3 locality does not transfer.
3. **Phase-recovery failure:** the family includes records but lacks coherent
   controls, so definite outcomes exist but interference physics is not
   reconstructed.
4. **Projective failure:** records exist at fixed regulator but record sectors
   do not refine, so the measurement story is not continuum-facing.
5. **QFT-reconstruction failure:** the finite operational net exists but does
   not converge to, or is inequivalent to, the expected local QFT algebra.

This no-go section is not pessimistic. It is what keeps the reconstruction
claim scientifically sharp: ISP earns only the observables generated by its
declared operational family and its proven refinement/locality theorems.

### Claim audit

The paper's final claims are deliberately narrow.

Allowed claims:

1. finite detector records give positive normalized instruments;
2. selective update is ordinary conditioning on a record-sector event;
3. no extra collapse map is needed inside a declared finite detector-record
   model;
4. locality, exchange, selective, and projective statements hold under the
   explicit calibration, screening, and refinement hypotheses stated above;
5. possible empirical separations are operational projections of declared
   instruments, not raw algebraic matrices.

Disallowed claims:

1. that every raw `J_R` is an observable or a positive instrument;
2. that raw exchange curvature is automatically measurable;
3. that all realistic detectors satisfy anchored locality without a detector
   model;
4. that postselected correlations are signaling;
5. that Paper 4 reconstructs a continuum QFT net;
6. that the full real-world measurement problem is solved without the later
   continuum, phase-completeness, and detector-refinement work.

The slogan version is therefore:

```text
Paper 4 resolves the finite declared-record collapse bookkeeping problem, not
the whole continuum reconstruction problem.
```

## 15. Completion Status And Remaining Risks

The original Paper 4 backlog has now been addressed at theorem-framework
level:

1. `\mathcal O_a` is defined in Section 6.
2. finite measurement, repeatability, leakage, and reset are handled in
   Section 4.
3. the two-path phase benchmark and finite phase-completeness criterion are
   proved in Section 8.
4. generalized positive readouts and postprocessing are handled in Section 5.
5. locality transfer is proved conditionally in Section 9.
6. the local write-register detector benchmark and finite-depth detector
   architecture theorem prove concrete anchoring models for Theorem 10.
7. centered selective-outcome locality, conditional selective stability, and
   screened selective locality are proved under explicit clustering, screening,
   and outcome-floor hypotheses.
8. the calibration residual budget is consolidated in Proposition 11D, with a
   concrete finite-depth detector calibration ledger in Example 11E.
9. operational exchange is proved conditionally in Section 10, and the
   exchange-to-experiment pipeline states exactly which projected raw exchange
   coefficient an experiment can test.
10. finite no-signaling is proved in Section 11.
11. nested and lossy detector coarse-graining results prove exact and approximate
    record-sector refinement models.
12. projective record-instrument naturality is proved conditionally in Section
    12.
13. operational underdetermination, phase/control no-go results, and a claim
    audit are included in Section 14.

The paper is therefore complete as a **theorem-framework draft**. It is not yet
complete as a model-specific reconstruction theorem.

The remaining technical risks are:

1. **Detector anchoring beyond bounded finite-depth architectures.** Proposition
   10A proves the hypotheses for a bounded local write-register detector, and
   Theorem 10B extends this to finite-depth local detector circuits with
   propagation, amplification, memory stabilization, thresholding, and readout
   gates when the summed gate discrepancy and influence radius are controlled.
   Detectors with unbounded depth, uncontrolled propagation, moving hardware, or
   macroscopic uncompensated discrepancy still need their own enlarged
   anchored-response estimates.
2. **Selective outcome locality without screening.** Theorem 11A controls
   centered selective statistics under explicit clustering, Corollary 11B controls
   conditional probabilities with an outcome floor, and Theorem 11C packages the
   usable postselected statement as a screening theorem. Selective outcomes still
   do not obey locality for free; without screening, centering, or clustering
   they can carry ordinary remote correlations.
3. **Model-specific calibration estimates.** Proposition 11D fixes the residual
   ledger and Example 11E shows one finite-depth detector bookkeeping template,
   but each concrete detector model or experiment must still estimate its own
   `\varepsilon_{\mathrm{ex}}`, `\varepsilon_{\mathrm{det}}`,
   `\varepsilon_{\mathrm{sys}}`, leakage, and realization errors.
4. **Projective detector data beyond explicit coarse-graining maps.** Proposition
   19A gives an exact nested-register benchmark and Theorem 19B handles lossy
   coarse-graining by adding an explicit loss record. More realistic detector
   refinements with moving record supports, changing hardware, or nonconvergent
   survival denominators still need explicit `Q_D` or `Q_D^L` maps and
   compatibility estimates.
5. **Phase completeness beyond declared finite interferometers.** Theorem 6A
   gives a sufficient finite criterion: a phase-complete operational family must
   declare coherent controls, amplitude-level composition before Born squaring,
   record-writing couplings, nonselective record marginals, any claimed erasure
   controls, and a common composition domain. What remains open is not the
   finite two-path case, but a model-specific proof that a continuum or QFT-scale
   operational family contains all phase controls required by the target theory.
6. **Continuum QFT reconstruction.** The paper constructs and controls finite
   operational statistics. It does not yet construct a continuum Haag-Kastler
   net or prove equivalence with a target QFT.

The document should continue to advance only by keeping the ontology separated:

```text
primitive kernel
-> raw relative map
-> calibrated response
-> positive detector instrument
-> effect/outcome statistic
-> operational local net.
```
