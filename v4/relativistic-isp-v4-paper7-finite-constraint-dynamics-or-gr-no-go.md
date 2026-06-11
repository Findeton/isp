# Relativistic ISP V4 Paper 7: Finite Constraint Dynamics Or GR-Dynamics No-Go

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed finite constraint-dynamics selection audit.

## Abstract

V4 Paper 6 proves that geometry can become an ordinary finite ISP
configuration variable:

$$
\mathrm{V4P6\text{-}GEOM\text{-}IN\text{-}CONFIG}^{fin}.
$$

It also proves that this does not determine GR dynamics:

$$
\mathrm{V4P6\text{-}GR\text{-}DYN\text{-}FROM\text{-}CONFIG}^{cur}
\quad\hbox{is not sourced}.
$$

Paper 7 asks the next precise question:

$$
\boxed{
\hbox{Which finite matter-geometry kernels deserve to be called GR-like?}
}
$$

The answer is again two-level.

There is a strong conditional positive theorem.  If a finite
matter-geometry law has:

1. metric reconstruction;
2. frozen-background Paper-5 curvature;
3. projective compatibility;
4. finite tangential covariance;
5. finite normal/tangential constraint-algebra closure;
6. admissible-constraint preservation;
7. finite stress-response Ward compatibility;
8. a regulator-stable continuum interpretation;

then the law passes the Paper-7 GR-like finite dynamics gate:

$$
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cond}.
$$

But the current corpus does not source those assumptions.  The same
configuration alphabets, metric readouts, and fixed-background curvature
tests allow inequivalent kernels whose finite constraint-algebra residuals do
not vanish.  Therefore:

$$
\boxed{
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cur}
\quad\hbox{not sourced}.
}
$$

Paper 7 thus does not close ISP-GR.  It sharpens the next required theorem:
a same-law finite dynamical selection principle strong enough to source the
constraint-algebra residuals or a no-go showing that no such principle is
available in the current framework.

## 0. Imports And No-Smuggling Discipline

### Import 0.1: Fixed-Background Metric And Curvature

V4 Papers 4 and 5 source, at the enriched fixed-background level:

$$
\mathrm{V4P4\text{-}ENRICHED\text{-}METRIC\text{-}DIAGNOSTIC}
$$

and

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{emb,decl}.
$$

Thus fixed geometry can be read and fixed-background normal-deformation
exchange can recover

$$
h^{ij}(N\partial_jM-M\partial_jN).
$$

### Import 0.2: Geometry As Finite Configuration

V4 Paper 6 proves:

$$
\mathrm{V4P6\text{-}GEOM\text{-}IN\text{-}CONFIG}^{fin}
$$

by constructing finite geometry alphabets, total configuration spaces, frozen
lifts, and nontrivial geometry-update kernels.  It also proves that these
data do not determine GR dynamics.

### Barandes Rule 0.3

This paper may use:

1. finite total configuration spaces;
2. finite stochastic whole-process kernels;
3. finite comparison maps acting on record/effect spaces;
4. algebraic commutators of comparison maps as tests;
5. continuum GR expressions as benchmark targets.

This paper may not use:

1. hidden Markov factorization through unrecorded intermediate hypersurfaces;
2. Hilbert phase as primitive ontology;
3. Einstein equations as axioms;
4. continuum metrics as primitive objects;
5. a claim that finite geometry labels automatically imply GR.

The slogan is:

$$
\hbox{finite algebraic residuals first; continuum GR meaning only after they vanish.}
$$

## 1. Finite Deformation Data On Total Configurations

### Definition 1.1: Total Effect Space

For each regulator \(a\), let

$$
V_a^{tot}
:=
\mathbb R^{C_{\Sigma,a}^{matter}\times C_{\Sigma,a}^{geom}}
$$

be the real effect space on total finite configurations.  An element
\(F\in V_a^{tot}\) is a finite observable or cylinder effect on total records.

### Definition 1.2: Tangential Comparison Maps

For a finite tangential vector-field test \(v\), a tangential comparison map is
an invertible algebraic map

$$
D_a[v]:V_a^{tot}\to V_a^{tot}.
$$

It is meant to represent a finite relabeling/transport of matter and geometry
records along \(v\).  It need not be a stochastic matrix.  It is an
operational comparison map.

### Definition 1.3: Normal Comparison Maps

For a finite lapse test \(N\), a normal comparison map is an invertible
algebraic map

$$
H_a[N]:V_a^{tot}\to V_a^{tot}.
$$

It represents a finite normal hypersurface comparison on total
matter-geometry records.

The notation \(H\) is only mnemonic for the GR Hamiltonian constraint.  It is
not a Hilbert operator and not a continuum constraint imposed as primitive
ontology.

### Definition 1.4: Geometry-Dependent Tangential Generator

Given a finite geometry record \(g_a\), let \(I_a(g_a)^{ij}\) be its metric
candidate.  Define the finite bracket vector

$$
\beta_a^i(g;N,M)
:=
I_a(g)^{ij}(N\partial_jM-M\partial_jN)
$$

where derivatives are the declared finite-difference or reconstructed first
jets from Paper 6.

The corresponding tangential comparison map is denoted

$$
D_a[\beta_a(g;N,M)].
$$

## 2. Finite Constraint-Algebra Residuals

The continuum hypersurface-deformation algebra is not used as an axiom.  It
is used as the benchmark shape for finite residuals.

### Definition 2.1: Tangential-Tangential Residual

For tangential tests \(v,w\), define

$$
R_{DD,a}[v,w]
:=
D_a[v]D_a[w]D_a[v]^{-1}D_a[w]^{-1}
D_a[-[v,w]_a].
$$

Here \([v,w]_a\) is the declared finite Lie-bracket approximation.  The
residual is zero if the finite tangential comparisons close to the finite
Lie bracket in multiplicative form.

### Definition 2.2: Tangential-Normal Residual

For \(v,N\), define

$$
R_{DH,a}[v,N]
:=
D_a[v]H_a[N]D_a[v]^{-1}H_a[-{\mathcal L}_{v,a}N].
$$

Here \({\mathcal L}_{v,a}N\) is the finite transported lapse derivative.

### Definition 2.3: Normal-Normal Residual

For \(N,M\), define

$$
R_{HH,a}[N,M]
:=
H_a[N]H_a[M]H_a[N]^{-1}H_a[M]^{-1}
D_a[-\beta_a(g;N,M)].
$$

Because \(g\) is now a finite configuration variable, this residual is tested
on total effects sectorwise or in expectation under a declared total law.

### Definition 2.4: Residual Norms

Let \({\mathcal O}_a\subset V_a^{tot}\) be the declared finite test-observable
class.  Define

$$
\|R\|_{{\mathcal O}_a}
:=
\sup_{F\in{\mathcal O}_a,\ \|F\|\le1}\|RF-F\|.
$$

Any equivalent finite operator norm may be used, provided the chosen norm and
test class are fixed before the theorem is claimed.

### Definition 2.5: Finite Constraint-Algebra Closure

Write

$$
\mathrm{V4P7\text{-}FIN\text{-}ALG\text{-}CLOSE}
$$

if for every tested compactly supported \(v,w,N,M\),

$$
\|R_{DD,a}[v,w]\|_{{\mathcal O}_a}\to0,
$$

$$
\|R_{DH,a}[v,N]\|_{{\mathcal O}_a}\to0,
$$

and

$$
\|R_{HH,a}[N,M]\|_{{\mathcal O}_a}\to0.
$$

This is the finite algebraic version of asking whether the constraint
brackets close with the metric structure functions carried by geometry
records.

## 3. Dynamical Covariance Of The Total Kernel

Algebraic comparison maps alone do not select a dynamics.  The total
stochastic kernel must also be compatible with them.

### Definition 3.1: Total Matter-Geometry Kernel

Let

$$
\Gamma_a^{tot}:V_a^{tot}\to V_{a'}^{tot}
$$

be a finite whole-process stochastic kernel on total records.  The source and
target regulators may be the same or linked by the declared refinement/slab
rule.

### Definition 3.2: Tangential Dynamical Covariance

Tangential dynamical covariance holds if

$$
\|\Gamma_a^{tot}D_a[v]-D_{a'}[v']\Gamma_a^{tot}\|_{{\mathcal O}_a}\to0
$$

where \(v'\) is the transported tangential test on the target hypersurface.

Plainly: transporting records tangentially before the slab or after the slab
gives the same finite predictions in the limit.

### Definition 3.3: Normal Dynamical Covariance

Normal dynamical covariance holds if

$$
\|\Gamma_a^{tot}H_a[N]-H_{a'}[N']\Gamma_a^{tot}\|_{{\mathcal O}_a}\to0
$$

for the declared transported lapse \(N'\), modulo the finite algebraic
residuals of Section 2.

This is stronger than Paper 5.  Paper 5 only supplies fixed-background
normal exchange.  Here the normal comparison must be compatible with a law
that can also change geometry.

### Definition 3.4: Finite Dynamical Constraint Compatibility

Write

$$
\mathrm{V4P7\text{-}DYN\text{-}COV}
$$

if tangential and normal dynamical covariance both hold in the declared
observable topology, and the covariance errors are controlled by residuals
that vanish under `V4P7-FIN-ALG-CLOSE`.

## 4. Stress-Response Conservation Gate

Paper 5 proved a conditional stress-response Ward identity.  Paper 7 uses it
as a selection gate for total matter-geometry laws.

### Definition 4.1: Total Metric-Source Family

Let

$$
p_{a,\kappa}(m,g)>0
$$

be a finite normalized family on total records, depending on a compactly
supported finite metric source \(\kappa\).  Define the total stress score

$$
T_a^{ij}(x;m,g)
:=
\partial_{\kappa_{ij}(x)}\log p_{a,\kappa}(m,g)\big|_{\kappa=0}.
$$

### Definition 4.2: Tangential Source Covariance

The source family is tangentially covariant if simultaneous transport of
records and pullback of the finite metric source leaves the law invariant up
to \(o(1)\) in the tested topology.

### Theorem 4.3: Conditional Total Stress Ward

If \(p_{a,\kappa}\) is differentiable, normalized, positive, projectively
compatible, and tangentially source-covariant, then every continuum limit of
the total stress score satisfies the weak Ward identity

$$
\int T^{ij}{\mathcal L}_\xi g_{ij}\,d\mu_g=0
$$

in expectation, for compactly supported tangential \(\xi\).  In the smooth
benchmark representation this is the weak form of

$$
\nabla_i\mathbf E[T^{ij}]=0.
$$

Proof.

This is the Paper-5 stress-response proof applied to total records
\((m,g)\).  Differentiate normalization to get score zero.  Differentiate
tangential source covariance at the identity diffeomorphism.  The derivative
of the metric source produces the pairing with \({\mathcal L}_\xi g\).
Passing to the projective limit gives the displayed weak identity.  `square`

### Proposition 4.4: Stress Ward Does Not Select Normal Dynamics By Itself

The total stress Ward identity does not determine the normal geometry-update
kernel.

Proof.

Tangential covariance constrains response under spatial relabeling.  It does
not determine how geometry changes under normal deformation.  Two kernels may
share the same tangentially covariant finite source family and differ in
their normal update probabilities.  Therefore stress Ward is necessary for a
GR-like matter-geometry law, but not sufficient.  `square`

## 5. The Conditional Positive Theorem

### Hypothesis 5.1: GR-Like Finite Dynamics Package

A finite total law satisfies the GR-like dynamics package if:

1. **metric reconstruction:** finite geometry records recover tensorial,
   symmetric, positive metric candidates;
2. **frozen reduction:** frozen geometry sectors recover Paper 5;
3. **projective compatibility:** total kernels commute with coarse-graining
   in the declared observable topology;
4. **finite algebra closure:** `V4P7-FIN-ALG-CLOSE` holds;
5. **dynamical covariance:** `V4P7-DYN-COV` holds;
6. **constraint preservation:** the total kernel preserves the declared
   admissible finite constraint subset;
7. **stress Ward:** the total source family satisfies Theorem 4.3;
8. **continuum identification:** the limiting structure functions are the
   recovered metric coefficients from the same finite geometry records.

### Theorem 5.2: Conditional GR-Like Finite Dynamics

Under Hypothesis 5.1,

$$
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cond}
$$

holds.

Proof.

Metric reconstruction gives the finite geometry records metric meaning.
Frozen reduction ensures compatibility with the fixed-background curvature
source of Paper 5.  Projective compatibility makes the construction stable
under refinement.  Finite algebra closure gives the finite analogue of
constraint closure.  Dynamical covariance says the stochastic total kernel is
compatible with those finite deformations rather than merely coexisting with
them.  Constraint preservation keeps the law on the declared admissible
geometry sector.  Stress Ward gives the tangential conservation identity for
matter-geometry response.  Continuum identification ties the algebraic
structure functions to the same metric records, rather than to an external
metric.  These are exactly the nonvacuity filters required after Paper 6.
`square`

### Corollary 5.3: What The Conditional Theorem Does Not Claim

The theorem does not assert Einstein equations.  It says that a finite law
passing the listed tests is GR-like enough to move to the Einstein-limit
stage.

The Einstein-limit stage would still need to show that the continuum
selection agrees with Einstein dynamics, or else identify the controlled
deformation.

## 6. Current-Corpus No-Go

### Theorem 6.1: Current Corpus Does Not Source GR-Like Dynamics

The current corpus does not prove

$$
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cur}.
$$

Proof.

Papers 4 and 5 source metric diagnostics and fixed-background operational
curvature.  Paper 6 sources finite geometry configuration variables and
nontrivial geometry-update kernels.  But Paper 6 also proves that the same
readout and fixed-background tests admit many inequivalent geometry kernels.

Choose the reset kernel from Paper 6:

$$
\Gamma_a^{reset}(m',g'\mid m,g)
=
M_a(m'\mid m,g,g')\pi_a(g').
$$

For generic \(\pi_a\), the geometry after the slab is independent of the
input geometry.  Such a law is compatible with the mere existence of geometry
records and can share the same one-time metric readout, but it is not
compatible with normal dynamical covariance or finite constraint-algebra
closure unless \(\pi_a\) is specially tuned.  Nothing in Papers 4-6 supplies
that tuning.

Therefore the assumptions in Hypothesis 5.1 are not sourced by the current
corpus.  `square`

### Corollary 6.2: The Missing Object Is A Same-Law Dynamical Selection
Principle

The missing theorem is not another metric detector and not another finite
geometry alphabet.  It is a same-law principle selecting the total stochastic
kernel so that the finite algebraic residuals vanish.

Equivalently, V4 now needs:

$$
\boxed{
\|R_{DD,a}\|+\|R_{DH,a}\|+\|R_{HH,a}\|
+\hbox{dynamical covariance error}
\to0
}
$$

for the actual finite matter-geometry law.

## 7. Testing The Three Live Routes

Paper 6 named three live constructive routes.  Paper 7 now tests what each
can and cannot source.

### Route A: Constraint Algebra Closure

The most direct route is to prove `V4P7-FIN-ALG-CLOSE` for the actual finite
comparison maps.

#### Proposition 7.1: Constraint Algebra Closure Would Be Sufficiently Sharp

If `V4P7-FIN-ALG-CLOSE`, `V4P7-DYN-COV`, metric reconstruction, and projective
compatibility all hold, then the finite law has the right kinematic
constraint structure to enter the Einstein-limit stage.

Proof.

This is Theorem 5.2 without stress response.  It gives the correct
normal/tangential algebraic structure but not yet matter conservation.
`square`

#### Proposition 7.2: Constraint Algebra Closure Is Not Sourced By
Frozen-Sector Tests

Paper 5's frozen \(HH\) test does not imply `V4P7-FIN-ALG-CLOSE` for a
dynamical geometry kernel.

Proof.

The frozen test holds with \(g'=g\).  A dynamical geometry kernel may change
\(g\) during the slab.  Then the sectorwise structure function
\(\beta_a(g;N,M)\) before the slab need not match the target-sector structure
function after the slab.  The residual can therefore be nonzero even though
every frozen sector individually passes Paper 5.  `square`

### Route B: Stress-Response Conservation

The second route is to use source-response calculus to force conservation.

#### Proposition 7.3: Stress Ward Is Necessary But Not Sufficient

The conditional total stress Ward identity is a necessary GR-facing filter,
but it does not imply finite normal constraint closure.

Proof.

The Ward identity controls tangential diffeomorphism response of the total
source law.  Normal-normal closure involves comparing two normal deformation
orders and the geometry-dependent structure function.  A tangential Ward
identity alone does not determine that normal commutator.  `square`

### Route C: Projective Detailed Balance With Geometric Score

The third route is to choose a finite geometric score \(S_a(m,g)\) and define
a local detailed-balance kernel.

#### Proposition 7.4: Arbitrary Detailed Balance Is Not GR Dynamics

A detailed-balance kernel with arbitrary finite score \(S_a\) does not source
GR-like dynamics.

Proof.

For any finite score \(S_a\), the Metropolis construction gives a stochastic
kernel.  Different scores give different continuum biases.  Unless a theorem
identifies \(S_a\) with a regulator-stable geometric action or entropy
functional satisfying the finite constraint tests, detailed balance is only a
probability assignment, not a GR-selection principle.  `square`

#### Conditional Theorem 7.5: Sourced Geometric Score Route

Suppose a finite score \(S_a(m,g)\) is sourced by the same finite law and
satisfies:

1. locality and support/collar bounds;
2. projective stability;
3. tangential covariance up to boundary terms;
4. first and second variation identities whose continuum limits give the
   desired constraint and stress-response equations;
5. compatibility with finite algebra closure.

Then the local detailed-balance route supplies the dynamical selection
principle required by Paper 7.

Proof.

Under these assumptions, detailed balance is no longer arbitrary.  The score
selects transition weights, its variations supply the response equations, and
compatibility with algebra closure controls the normal/tangential residuals.
Theorem 5.2 then applies.  `square`

### Corollary 7.6: The Best Next Target

The most promising next primitive is not "another finite kernel."  It is a
sourced finite geometric score or constraint residual estimate:

$$
\mathrm{V4P8\text{-}SOURCED\text{-}GEOM\text{-}SCORE}
$$

or

$$
\mathrm{V4P8\text{-}FIN\text{-}ALG\text{-}RESIDUAL\text{-}BOUND}.
$$

Either would move Paper 7's conditional theorem toward an actual positive GR
route.

## 8. Barandes Alignment Audit

### Proposition 8.1: Paper-7 Tests Are Barandes-Aligned

The finite residual tests are Barandes-aligned.

Proof.

They are algebraic tests on finite record/effect spaces.  They use
whole-process kernels and comparison maps.  They do not assume hidden
intermediate hypersurface states, Hilbert phases, or continuum metrics as
primitive ontology.  Continuum GR expressions appear only as benchmark limits
of finite residuals.  `square`

### Proposition 8.2: Importing Einstein Dynamics Would Violate The Program

Declaring \(S_a\) to be a discretized Einstein-Hilbert action without deriving
or licensing it from the finite ISP law would not be a Paper-7 solution.

Proof.

The whole point after Paper 6 is that many geometry dynamics are compatible
with the finite ontology.  Choosing the Einstein one by external declaration
would select dynamics by hand.  A Barandes-aligned V4 theorem must source the
selection principle as a finite same-law fact.  `square`

## 9. Final Settlement

### Theorem 9.1: Paper-7 Selection Gate Is Settled

Paper 7 settles the finite constraint-dynamics gate as follows:

1. it defines finite GR-like algebraic residuals \(R_{DD},R_{DH},R_{HH}\);
2. it defines dynamical covariance of the total matter-geometry kernel;
3. it lifts the stress-response Ward identity to total records;
4. it proves a conditional GR-like finite dynamics theorem;
5. it proves the current corpus does not source that theorem;
6. it identifies the next primitive: a sourced geometric score or a direct
   finite algebra residual bound.

Proof.

Items 1 and 2 are Definitions 2.1 through 3.4.  Item 3 is Theorem 4.3.  Item
4 is Theorem 5.2.  Item 5 is Theorem 6.1.  Item 6 is Corollary 7.6.  `square`

### Final Verdict 9.2

The conditional gate is real:

$$
\boxed{
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cond}.
}
$$

The current-corpus positive theorem is not sourced yet:

$$
\boxed{
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cur}
\quad\hbox{not sourced}.
}
$$

V4 has now reduced the GR problem to a sharper finite source theorem:

$$
\boxed{
\hbox{source a finite geometric score or prove finite constraint residual
decay for the actual matter-geometry law.}
}
$$

That is the honest Paper-8 frontier.
