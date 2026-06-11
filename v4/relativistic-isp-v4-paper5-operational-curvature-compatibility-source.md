# Relativistic ISP V4 Paper 5: Operational Curvature Compatibility Source

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed operational-curvature compatibility source audit.

## Abstract

V4 Paper 4 proves that enriched finite operational records can diagnose a
fixed curved background metric \(h^{ij}(x)\).  It also proves that the metric
detector table alone does not produce hypersurface-deformation curvature.

This paper settles the next question:

$$
\hbox{Can finite operational comparison maps source the curvature law}
$$

$$
\mathfrak C_{op}[N,M]
\to
K_i[h^{ij}(N\partial_jM-M\partial_jN)]?
$$

The answer is threefold.

1. **No**, not from the metric detector table alone.
2. **No**, not from the current bare Gamma corpus or any passive function of
   its endpoint probabilities.
3. **Yes, conditionally and constructively**, from an enriched fixed-background
   embedding-flow template: declare finite whole-process comparison maps as
   discretized transports of normal hypersurface deformations in a fixed
   background; if the transports are projectively consistent, locally
   faithful, and first-order accurate on cylinder effects, then their exchange
   two-cell converges to the Dirac-Schwinger tangential vector

   $$
   \beta^i=h^{ij}(N\partial_jM-M\partial_jN).
   $$

The conditional theorem is then advanced inside the paper.  We implement its
conditions as finite interpolation/transport templates and prove exactly what
they buy.  This yields a positive enriched kinematic result:

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{emb,decl}.
$$

It remains explicitly not a Gamma-level theorem and not Einstein dynamics.
The next GR-facing gate is a dynamical-geometry configuration law or a
nonconditional finite stress-response Ward theorem.

## 0. Imports And No-Smuggling Discipline

### Import 0.1: Paper-4 Metric Diagnostic

V4 Paper 4 proves

$$
\mathrm{V4P4\text{-}LOCAL\text{-}METRIC\text{-}DIAG}^{decl}
$$

for enriched local operational metric records.  It also proves

$$
\neg\mathrm{V4P4\text{-}TABLE\text{-}IMPLIES\text{-}OPCURV}^{cur}.
$$

Thus the metric record table supplies a coefficient field \(C_{op}^{ij}=h^{ij}\)
but not the comparison maps or curvature two-cell.

### Import 0.2: V2 Finite Curvature And Projective Lessons

V2 Paper 1 proves that finite exchange defects can converge to a
hypersurface-deformation-like tangential action in a free benchmark.

V2 Paper 2 proves that comparison maps and exchange defects have a projective
naturality language once the primitive kernels and coarse-graining maps are
compatible.

V2 Paper 4 proves that raw comparison maps are not automatically operational
observables; operational instruments must be declared as finite record
procedures.

### Barandes Rule 0.3

This paper may use:

1. finite configuration spaces;
2. finite record/effect spaces;
3. whole-process operational maps;
4. algebraic comparison maps;
5. projective coarse-graining;
6. fixed-background benchmark geometry as enriched representation data.

This paper may not use:

1. hidden Markov factorization through unrecorded intermediate hypersurfaces;
2. Hilbert phase as primitive ontology;
3. Einstein equations;
4. dynamical geometry;
5. the claim that metric readout alone is curvature dynamics.

## 1. Operational Curvature Compatibility Target

### Definition 1.1: Operational Normal Comparison Family

For each regulator \(a\), let \(V_a\) be a finite real record or effect space.
An operational normal comparison family assigns to each smooth compactly
supported lapse \(N\) an invertible algebraic map

$$
J_{op,a}[N]:V_a\to V_a
$$

such that:

1. \(J_{op,a}[0]=I\);
2. \(1^TJ_{op,a}[N]=1^T\) whenever \(V_a\) is read as a probability-state
   space;
3. the map is support-respecting up to a declared collar;
4. the map is a whole-process operational comparison, not a Markov product
   through hidden intermediate states.

The map need not be positive.  It is a comparison map, not a detector
instrument.

### Definition 1.2: Operational Exchange Two-Cell

For two lapses \(N,M\), define the operational exchange two-cell

$$
E_{op,a}[N,M]
:=
J_{op,a}[M|N]J_{op,a}[N]
\bigl(J_{op,a}[N|M]J_{op,a}[M]\bigr)^{-1}.
$$

Here \(J[M|N]\) means that the second comparison map is transported to the
finite support system after the first deformation.  In a fixed-regulator
linearized benchmark this may reduce to the commutator expression

$$
J_{op,a}[M]J_{op,a}[N]J_{op,a}[M]^{-1}J_{op,a}[N]^{-1}.
$$

### Definition 1.3: Normalized Operational Curvature

Let \(\epsilon_a\) be the declared small deformation scale.  The normalized
operational curvature is

$$
\mathfrak C_{op,a}[N,M]
:=
\epsilon_a^{-2}\bigl(E_{op,a}[N,M]-I\bigr)
$$

whenever the limit is tested on cylinder effects or sampled finite records.

### Definition 1.4: `V4P5-OPCURV-COMPAT`

Write

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT}
$$

if there is a finite tangential representation \(K_{i,a}[v^i]\) such that

$$
\mathfrak C_{op,a}[N,M]
\to
K_i[h^{ij}(N\partial_jM-M\partial_jN)]
$$

in the declared cylinder-effect topology, with \(K_i\) faithful modulo
declared tangential gauge.

## 2. Two Immediate No-Go Results

### Theorem 2.1: Metric Readout Alone Does Not Source Operational Curvature

The local metric detector table of Paper 4 does not determine
`V4P5-OPCURV-COMPAT`.

Proof.

Fix the same local metric record table \(C_{op}^{ij}(x)=h^{ij}(x)\).  There
are at least two compatible operational completions:

1. choose \(J_{op,a}[N]=I\) for every \(N\), giving zero curvature;
2. choose comparison maps from the embedding-flow template of Section 4,
   giving the Dirac-Schwinger tangential curvature under its hypotheses.

Both completions share the same metric readout table, but they have different
exchange two-cells.  Therefore the metric table alone cannot determine
operational curvature.  `square`

### Theorem 2.2: Passive Gamma-Derived Operational Curvature Is Not Sourced

The current corpus does not prove

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT}^{\Gamma,cur}.
$$

Moreover, any construction whose comparison maps are passive functions of the
current Gamma-level data inherits the Paper-3/Paper-4 orientation ambiguity.

Proof.

Paper 3 supplies a pair \(E_+,E_-\) with identical current Gamma data and
opposite signed metric orientation.  If all comparison maps and operational
curvatures are passive functions of those Gamma data, then the full two-cell
data agree on \(E_+\) and \(E_-\).  But the target vector

$$
h^{ij}(N\partial_jM-M\partial_jN)
$$

changes in its off-diagonal contribution when \(h^{12}\) changes sign.
Therefore a passive Gamma-derived construction cannot recover the signed
curvature for both backgrounds.  `square`

### Corollary 2.3: The Only Live Source Is Enriched Operational Dynamics

After Theorems 2.1 and 2.2, an operational curvature source must declare
additional finite comparison-map dynamics beyond metric readout and beyond
passive Gamma data.

## 3. Fixed-Background Embedding-Flow Template

The natural enriched source is not another detector.  It is the finite record
transport induced by fixed-background hypersurface deformations.

### Definition 3.1: Continuum Fixed-Background Normal Flow

Let a fixed background spacetime have spatial inverse metric \(h^{ij}(x)\) on
a reference hypersurface.  For a lapse \(N\), let

$$
\Phi_N^\epsilon
$$

denote the small normal deformation of the hypersurface by signed amount
\(\epsilon N\).  The classical fixed-background hypersurface-deformation
identity says that the exchange loop

$$
\Phi_{-M|N}^\epsilon\Phi_{-N}^\epsilon
\Phi_{M|N}^\epsilon\Phi_N^\epsilon
$$

has tangential part, to order \(\epsilon^2\),

$$
\epsilon^2\beta^i+O(\epsilon^3),
\qquad
\beta^i=h^{ij}(N\partial_jM-M\partial_jN).
$$

This is a fixed-background kinematic identity.  It is not Einstein dynamics.

### Definition 3.2: Finite Transport Of Cylinder Effects

Let \(R_a\) be a finite record grid.  A finite transport scheme assigns to
each small hypersurface map \(\Phi\) a column-stochastic pullback/pushforward
operator

$$
T_a(\Phi):V_a\to V_a
$$

on finite record distributions or cylinder effects.  It is first-order
accurate if for every smooth test effect \(f\),

$$
T_a(\Phi_\xi^\epsilon)\iota_a f
=
\iota_a(f+\epsilon{\mathcal L}_\xi f)+O(\epsilon^2)+O(a)
$$

for tangential vector fields \(\xi\) in the tested class.

### Definition 3.3: Embedding-Declared Operational Comparison Maps

Define

$$
J_{op,a}^{emb}[N]:=T_a(\Phi_N^\epsilon).
$$

The transported second-step maps \(J[M|N]\) and \(J[N|M]\) are defined by the
same finite transport scheme on the deformed support system.

This is a declared finite operational comparison family.  It is enriched
because \(\Phi_N^\epsilon\) is fixed-background geometric input.

## 4. Conditional Positive Theorem

### Hypothesis 4.1: Embedding-Transport Consistency

The embedding-flow template satisfies:

1. **first-order transport accuracy:** Definition 3.2 holds for tangential
   flows and the normal-flow exchange loop;
2. **projective naturality:** finite transports commute with declared
   coarse-graining up to \(o(1)\) in the cylinder-effect topology;
3. **local support:** a lapse supported in \(U\) changes records only in a
   controlled collar of \(U\);
4. **faithfulness:** the finite tangential representation separates vector
   fields modulo declared gauge;
5. **small-loop scaling:** \(\epsilon_a\to0\) and \(a/\epsilon_a^2\to0\), or
   any stated scaling sufficient to make interpolation error negligible after
   \(\epsilon_a^{-2}\) normalization.

### Theorem 4.2: Embedding Flow Sources Operational Curvature Compatibility

Under Hypothesis 4.1,

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{emb,decl}
$$

holds:

$$
\mathfrak C_{op,a}^{emb}[N,M]
\to
K_i[h^{ij}(N\partial_jM-M\partial_jN)].
$$

Proof.

The continuum fixed-background exchange loop has tangential displacement
\(\epsilon^2\beta^i+O(\epsilon^3)\), where

$$
\beta^i=h^{ij}(N\partial_jM-M\partial_jN).
$$

By first-order finite transport accuracy, applying the finite exchange loop to
a sampled cylinder effect \(\iota_a f\) gives

$$
E_{op,a}^{emb}[N,M]\iota_a f
=
\iota_a(f+\epsilon_a^2{\mathcal L}_\beta f)
+O(\epsilon_a^3)+O(a).
$$

After subtracting \(I\) and dividing by \(\epsilon_a^2\), the remainder
vanishes under the scaling in Hypothesis 4.1.  The limit is the finite
tangential representation \(K_i[\beta^i]\).  Faithfulness identifies the
vector field modulo declared gauge.  `square`

### Corollary 4.3: Curved-Background Bracket Test Passes At Enriched
Kinematic Level

Combining Theorem 4.2 with Paper 4's local metric diagnostic gives

$$
\mathrm{V4P5\text{-}ENRICHED\text{-}CURVED\text{-}BACKGROUND\text{-}BRACKET}^{emb,decl}.
$$

The result is kinematic and fixed-background.  It is not a dynamical geometry
law.

## 5. Implementing The Conditional Plan

The theorem is conditional.  Paper 5 now pushes each condition as far as the
current corpus honestly allows.

### Implementation A: Finite Interpolation Transport

On a regular grid in a coordinate patch, define \(T_a(\Phi)\) by barycentric
interpolation: a record at cell center \(x\) is transported to the surrounding
cell vertices of \(\Phi(x)\) with nonnegative barycentric weights.

### Proposition 5.1: Barycentric Transport Is A Finite Stochastic Record Map

For sufficiently small \(\Phi\) staying inside the patch collar,
\(T_a(\Phi)\) is column-stochastic and support-respecting.

Proof.

Barycentric weights are nonnegative and sum to one.  A record at one cell is
distributed only to the finitely many cells adjacent to \(\Phi(x)\).  Thus
columns are probability vectors and support grows by a controlled collar.
`square`

### Proposition 5.2: Barycentric Transport Is First-Order Accurate

For smooth \(f\) and a small tangential flow \(\Phi_\xi^\epsilon\),

$$
T_a(\Phi_\xi^\epsilon)\iota_a f
=
\iota_a(f+\epsilon{\mathcal L}_\xi f)+O(\epsilon^2)+O(a)
$$

uniformly on compact subpatches.

Proof.

Barycentric interpolation is first-order accurate for smooth functions on a
regular mesh.  Taylor expansion of \(f(\Phi_\xi^\epsilon(x))\) gives

$$
f(\Phi_\xi^\epsilon(x))
=
f(x)+\epsilon{\mathcal L}_\xi f(x)+O(\epsilon^2).
$$

The interpolation error contributes \(O(a)\).  `square`

### Proposition 5.3: Scaling Window

If

$$
\epsilon_a\to0,
\qquad
\frac{a}{\epsilon_a^2}\to0,
$$

then the normalized interpolation error in Theorem 4.2 vanishes.

Proof.

The finite loop error after applying the transport scheme is
\(O(\epsilon_a^3)+O(a)\).  Dividing by \(\epsilon_a^2\) gives
\(O(\epsilon_a)+O(a/\epsilon_a^2)\), which vanishes under the displayed
scaling.  `square`

### Implementation B: Projective Naturality

### Proposition 5.4: Projective Naturality Is Conditional, Not Automatic

Barycentric transport satisfies projective naturality only when the
coarse-graining maps are chosen compatibly with the interpolation scheme:

$$
P_{a\leftarrow a'}T_{a'}(\Phi)
-
T_a(\Phi)P_{a\leftarrow a'}
\to0.
$$

Proof.

If coarse cells are unions of fine cells and both transports are induced by
the same geometric map \(\Phi\), standard finite-volume interpolation gives
the displayed convergence for smooth cylinder effects.  If the
coarse-graining map is arbitrary, there is no reason for it to commute with
transport.  Therefore this is a named regulator-compatibility condition, not a
consequence of finite stochasticity alone.  `square`

### Implementation C: Tangential Faithfulness

### Proposition 5.5: Cylinder Effects Give Tangential Faithfulness

On a coordinate patch, if the tested cylinder effects include sampled smooth
coordinate functions and compactly supported smooth probes, then the
tangential representation \(K_i[v^i]\) is faithful modulo boundary/gauge
directions that annihilate all tested probes.

Proof.

If \(K_i[v^i]\) annihilates every sampled smooth probe in the continuum limit,
then

$$
{\mathcal L}_v f=0
$$

for all compactly supported smooth \(f\) in the tested class.  Taking probes
with arbitrary first jet at a point forces \(v=0\) there.  The only remaining
directions are those deliberately quotiented as gauge or boundary-null.
`square`

### Theorem 5.6: Implemented Embedding-Flow Compatibility

For regular coordinate patches, compatible barycentric transports, tested
smooth cylinder effects, and scaling

$$
\epsilon_a\to0,
\qquad
a/\epsilon_a^2\to0,
$$

the finite embedding-flow template satisfies Hypothesis 4.1.  Hence

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{emb,decl}
$$

is proved for this enriched fixed-background benchmark.

Proof.

Propositions 5.1 and 5.2 give finite stochastic support-respecting transport
and first-order accuracy.  Proposition 5.3 gives the required normalization
window.  Proposition 5.4 supplies projective naturality under compatible
coarse-graining.  Proposition 5.5 gives faithfulness.  Theorem 4.2 then
applies.  `square`

## 6. What Was Actually Sourced

### Theorem 6.1: Source Classification

Paper 5 sources operational curvature compatibility in the following precise
sense:

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{emb,decl}
\quad\hbox{true},
$$

but

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{\Gamma,cur}
$$

is not proved and is blocked by the current orientation no-go for passive
Gamma-derived constructions.

Proof.

The positive statement is Theorem 5.6.  The Gamma-level non-source is Theorem
2.2.  `square`

### Corollary 6.2: This Is A GR-Facing Kinematic Theorem

The result is genuinely GR-facing because it recovers the fixed-background
hypersurface-deformation vector.  It is kinematic because the fixed background
and its normal deformation flow are inputs.

It is therefore stronger than a metric readout table and weaker than
dynamical general relativity.

## 7. Stress-Response Ward Identity: Conditional Advancement

The embedding-flow theorem has now been advanced to an implemented finite
transport template.  The next possible advance is stress response on the same
enriched fixed background.

### Definition 7.1: Finite Metric-Source Family

Let \(p_{g,\kappa,a}(r)\) be a finite same-law operational record family
depending on a background metric \(g\) and a compactly supported symmetric
metric source \(\kappa_{ij}\).  Define the finite stress score

$$
T_a^{ij}(x,r):=
\partial_{\kappa_{ij}(x)}\log p_{g,\kappa,a}(r)\big|_{\kappa=0}
$$

whenever the derivative exists in the declared finite source coordinates.

### Definition 7.2: Finite Tangential Covariance

The finite metric-source family is tangentially covariant if, for every
finite tangential transport \(\varphi_a\) approximating a compactly supported
spatial diffeomorphism \(\varphi\),

$$
p_{\varphi^*g,0,a}(\varphi_a r)
=
p_{g,0,a}(r)+o(1)
$$

in the tested cylinder topology.

### Theorem 7.3: Conditional Finite Stress-Response Ward Identity

If the metric-source family is differentiable in \(\kappa\), tangentially
covariant, and has compatible projective limits, then its continuum stress
score satisfies the weak Ward identity

$$
\int T^{ij}{\mathcal L}_\xi g_{ij}\,d\mu_g=0
$$

in expectation, for compactly supported tangential vector fields \(\xi\).  In
the usual Levi-Civita representation this is the weak form of

$$
\nabla_i\mathbf E[T^{ij}]=0
$$

modulo the declared density convention and boundary terms.

Proof.

Tangential covariance says that the probability law is unchanged, to
vanishing regulator error, by simultaneous transport of records and pullback
of the background metric.  Differentiate this invariance at the identity
diffeomorphism.  The derivative of the metric is

$$
\delta g_{ij}=({\mathcal L}_\xi g)_{ij}.
$$

The derivative of the normalized probability law gives the stress score
paired with \({\mathcal L}_\xi g\).  Normalization removes the score mean, as
in Paper 4's score-zero identity.  Passing to the projective limit gives the
weak displayed identity.  Integrating by parts gives the covariant divergence
form when the smooth Levi-Civita representation is admitted as an enriched
benchmark.  `square`

### Proposition 7.4: Stress Ward Is Not Automatic From Curvature

`V4P5-OPCURV-COMPAT-SOURCE^{emb,decl}` does not by itself prove the
stress-response Ward identity.

Proof.

Operational curvature compatibility supplies comparison maps for normal
deformation exchange.  Stress response requires a metric-source family
\(p_{g,\kappa,a}\), differentiability with respect to \(\kappa\), and
tangential covariance of the probability law.  These are additional
same-law response hypotheses.  `square`

### Corollary 7.5: Stress-Response Status

Paper 5 proves:

$$
\mathrm{V4P5\text{-}STRESS\text{-}RESPONSE\text{-}WARD}^{cond}
$$

under finite tangential covariance and metric-source differentiability.  It
does not prove an unconditional stress tensor or Einstein dynamics.

## 8. Barandes Alignment Audit

### Proposition 8.1: Embedding-Flow Compatibility Is Barandes-Aligned As An
Enriched Benchmark

The embedding-flow construction is Barandes-aligned in the following limited
sense:

1. finite maps act on finite record/effect spaces;
2. finite transports are whole-process operational maps;
3. no hidden Markov factorization is assumed;
4. metric and embedding-flow data are explicitly marked enriched
   fixed-background inputs;
5. no Hilbert phase is primitive;
6. no Einstein equation is imported.

Proof.

Each item follows from Definitions 3.2 and 3.3 and the no-smuggling discipline
of Section 0.  `square`

### Proposition 8.2: The Construction Is Not Gamma-Level ISP-GR

The embedding-flow theorem does not show that the current bare Gamma endpoint
law reconstructs or generates the fixed-background hypersurface-deformation
algebra.

Proof.

The comparison maps \(J_{op,a}^{emb}[N]\) are declared from fixed-background
normal deformation transports.  They are not derived as passive functions of
the current Gamma endpoint kernels.  Theorem 2.2 blocks the passive
Gamma-derived route.  `square`

## 9. Final Settlement

### Theorem 9.1: Operational Curvature Compatibility Source Is Settled

The Paper-5 issue is fully settled:

1. metric detector records alone do not source operational curvature;
2. passive Gamma-derived data do not source signed operational curvature in
   the current corpus;
3. fixed-background embedding-flow transports do source enriched operational
   curvature compatibility under explicit finite interpolation, projective
   naturality, support, scaling, and faithfulness hypotheses;
4. those hypotheses are implemented by compatible barycentric transports on
   regular patches;
5. stress-response Ward follows conditionally from a separate finite
   metric-source family with tangential covariance;
6. none of these results is dynamical GR.

Proof.

Item 1 is Theorem 2.1.  Item 2 is Theorem 2.2.  Items 3 and 4 are Theorem 4.2
and Theorem 5.6.  Item 5 is Theorem 7.3 and Proposition 7.4.  Item 6 is the
Barandes alignment audit and the fixed-background status of the construction.
`square`

### Final Verdict 9.2

V4 has now advanced beyond metric readout.  It has a finite enriched
fixed-background kinematic curvature source:

$$
\boxed{
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{emb,decl}.
}
$$

The next real GR gate is no longer "can records see the metric?" or "can
fixed-background comparison maps reproduce the bracket?"  Those are settled
at the enriched fixed-background level.

The next gate is:

$$
\boxed{
\hbox{Can geometry become part of the finite configuration law?}
}
$$

That is the dynamical-geometry configuration gate.  It is where V4 must decide
whether metric data are only enriched external records or are themselves
ordinary ISP configurations with stochastic transition laws.
