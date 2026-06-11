# Relativistic ISP V4 Paper 6: Dynamical Geometry Configuration Gate

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed geometry-in-configuration gate audit.

## Abstract

V4 Paper 5 ends with the question:

$$
\boxed{
\hbox{Can geometry become part of the finite configuration law?}
}
$$

This paper settles that question in the only honest sense currently available.

The answer is two-level.

1. **Yes, weakly and constructively.**  Geometry can be made an ordinary
   finite ISP configuration component.  One can define finite geometry
   alphabets, finite total configuration spaces

   $$
   C_{\Sigma,a}^{tot}
   =
   C_{\Sigma,a}^{matter}\times C_{\Sigma,a}^{geom},
   $$

   finite same-law kernels on these spaces, frozen-geometry reductions that
   reproduce Paper 5, and nontrivial finite geometry-update kernels that keep
   all variables inside the ordinary record law.

2. **No, not as dynamical GR from the current corpus.**  The same metric
   detector and fixed-background curvature data are compatible with many
   inequivalent geometry-update kernels: frozen, random-walk, reset, biased,
   and constraint-projected.  Therefore Papers 1-5 do not determine Einstein
   dynamics, constraint propagation, or a gravitational action.  A new
   primitive same-law dynamical principle is required.

The precise settlement is:

$$
\boxed{
\mathrm{V4P6\text{-}GEOM\text{-}IN\text{-}CONFIG}^{fin}
\quad\hbox{true}
}
$$

and

$$
\boxed{
\mathrm{V4P6\text{-}GR\text{-}DYN\text{-}FROM\text{-}CONFIG}^{cur}
\quad\hbox{not sourced}.
}
$$

The next real V4 theorem must therefore source a finite dynamical geometry
law, not merely a finite geometry alphabet.

## 0. Imports And Discipline

### Import 0.1: Enriched Metric Records

V4 Paper 4 proves that enriched finite operational records can recover fixed
background metric coefficients:

$$
\mathrm{V4P4\text{-}ENRICHED\text{-}METRIC\text{-}DIAGNOSTIC}.
$$

The result is enriched because the metric-sensitive operational responses are
declared finite records, not passive functions of the old bare Gamma endpoint
law.

### Import 0.2: Fixed-Background Operational Curvature

V4 Paper 5 proves:

$$
\mathrm{V4P5\text{-}OPCURV\text{-}COMPAT\text{-}SOURCE}^{emb,decl}.
$$

Fixed-background finite comparison maps can reproduce

$$
\beta^i=h^{ij}(N\partial_jM-M\partial_jN)
$$

when the background metric and its embedding-flow transports are enriched
inputs.  This is kinematic and fixed-background.  It is not dynamical
geometry.

### Barandes Rule 0.3

Paper 6 may use:

1. finite configuration spaces;
2. finite stochastic whole-process kernels;
3. finite geometry records as ordinary configuration labels;
4. finite coarse-graining maps;
5. continuum metric language only as a benchmark interpretation.

Paper 6 may not use:

1. hidden Markov factorization through unrecorded intermediate hypersurfaces;
2. Hilbert phase as primitive ontology;
3. Einstein equations as an axiom;
4. continuum metrics as primitive ontology;
5. a claim that adding geometry labels automatically proves GR.

The basic rule is:

$$
\hbox{geometry may enter as finite records, but dynamics must be earned.}
$$

## 1. The Gate Statement

### Definition 1.1: Finite Geometry Configuration Component

A finite geometry configuration component at regulator \(a\) is a finite set

$$
C_{\Sigma,a}^{geom}
$$

whose elements \(g_a\) are finite records intended to approximate geometric
data on the regulated hypersurface.  The records may include:

1. cellwise inverse metric candidates;
2. orientation and volume-sign records;
3. adjacency or incidence data;
4. boundary/collar records;
5. finite gauge labels to be quotiented or tracked.

They are finite records.  They are not smooth metrics as primitive objects.

### Definition 1.2: Total Finite ISP Configuration

Given finite matter records \(C_{\Sigma,a}^{matter}\), define the total
configuration space

$$
C_{\Sigma,a}^{tot}
:=
C_{\Sigma,a}^{matter}\times C_{\Sigma,a}^{geom}.
$$

A total configuration is written

$$
q_a=(m_a,g_a).
$$

### Definition 1.3: Dynamical Geometry Kernel

A finite dynamical geometry kernel is a stochastic whole-process map

$$
\Gamma_{\Sigma\to\Sigma',a}^{tot}
:
\Delta(C_{\Sigma,a}^{tot})
\to
\Delta(C_{\Sigma',a}^{tot}).
$$

Equivalently, it is a nonnegative matrix

$$
\Gamma_a^{tot}(m',g'\mid m,g)
$$

whose columns sum to one.

The kernel is a slab law.  It is not assumed to factor as geometry first, then
matter, then another hidden time step.

### Definition 1.4: The Paper-6 Gate

The weak geometry-configuration gate is:

$$
\mathrm{V4P6\text{-}GEOM\text{-}IN\text{-}CONFIG}^{fin}.
$$

It holds if there are finite \(C_{\Sigma,a}^{geom}\), finite stochastic
whole-process kernels on \(C_{\Sigma,a}^{tot}\), and interpretation maps from
finite geometry records to metric candidates such that:

1. frozen geometry reduces to the fixed-background Paper-5 setting;
2. at least one nontrivial kernel changes \(g_a\) with positive probability;
3. all variables remain ordinary finite records;
4. coarse-graining can be imposed or named explicitly.

The strong GR-dynamics gate is:

$$
\mathrm{V4P6\text{-}GR\text{-}DYN\text{-}FROM\text{-}CONFIG}^{cur}.
$$

It holds only if the current corpus determines, from finite ISP data, a
geometry-update law with the correct constraint and continuum GR content.

The distinction is essential.  The weak gate asks whether geometry can be in
the ontology.  The strong gate asks whether GR dynamics has been derived.

## 2. A Finite Geometry Alphabet

### Definition 2.1: Cellwise Metric Alphabet

Fix a coordinate patch and a regulated cell decomposition
\({\mathcal C}_a\).  Fix constants

$$
0<\lambda_-<\lambda_+<\infty
$$

and a quantization mesh \(\eta_a>0\).  Let

$$
{\mathcal H}_{a,\eta}
$$

be the finite set of rational symmetric positive definite matrices \(H\) whose
eigenvalues lie in \([\lambda_-,\lambda_+]\) and whose entries lie on the
\(\eta_a\)-mesh.

Define

$$
C_{\Sigma,a}^{geom}
:=
\prod_{c\in{\mathcal C}_a}{\mathcal H}_{a,\eta}
\times O_a
\times B_a,
$$

where \(O_a\) is a finite orientation/time-orientation record set and \(B_a\)
is a finite boundary/collar record set.

This is finite because \({\mathcal C}_a\), \({\mathcal H}_{a,\eta}\), \(O_a\),
and \(B_a\) are finite.

### Definition 2.2: Metric Interpretation Map

For \(g_a\in C_{\Sigma,a}^{geom}\), define the piecewise constant inverse
metric candidate

$$
I_a(g_a)(x):=H_c
\qquad x\in c.
$$

If a smoother representative is needed, let

$$
\widetilde I_a(g_a)
$$

be a declared local interpolation of the cellwise values.  The interpolation
is representation data, not primitive ontology.

### Proposition 2.3: Smooth Metrics Can Be Approximated By Finite Geometry
Records

Let \(h^{ij}(x)\) be a smooth positive inverse spatial metric on a compact
coordinate patch with eigenvalues in \((\lambda_-,\lambda_+)\).  If
\(\eta_a\to0\) and the cell diameter \(a\to0\), then there are
\(g_a\in C_{\Sigma,a}^{geom}\) such that

$$
\|I_a(g_a)-h\|_{L^\infty}\to0.
$$

If \(\widetilde I_a\) is a standard piecewise-linear or finite-volume
first-order reconstruction, \(h\) is \(C^2\), and

$$
\frac{\eta_a}{a}\to0,
$$

then on compact interior subpatches

$$
\|\widetilde I_a(g_a)-h\|_{C^1}\to0.
$$

Proof.

On each cell choose a representative point \(x_c\).  Approximate
\(h^{ij}(x_c)\) by a rational symmetric positive definite matrix \(H_c\) on
the \(\eta_a\)-mesh.  Uniform continuity of \(h\) controls the cellwise
variation, and \(\eta_a\to0\) controls quantization error.  The eigenvalue
window remains valid for sufficiently fine \(a\) and \(\eta_a\) because the
metric is uniformly positive and bounded on the compact patch.  The
interpolated \(C^1\) statement is the standard first-order reconstruction
estimate: cell-size error contributes \(O(a)\) to values and \(O(a)\) to
derivatives for \(C^2\) data, while quantization contributes \(O(\eta_a)\) to
values and \(O(\eta_a/a)\) to reconstructed derivatives.  The displayed
condition makes the quantized derivative error vanish.  `square`

### Corollary 2.4: Finite Geometry Records Can Carry The Paper-4 Metric
Diagnostic

The enriched metric coefficients of Paper 4 can be represented as finite
geometry records \(g_a\) rather than as external labels, up to the declared
regulator accuracy.

This does not yet give dynamics.

## 3. The Weak Positive Theorem

### Definition 3.1: Frozen-Geometry Lift Of A Fixed-Background Law

Suppose Paper 5 supplies, for each finite geometry record \(g_a\), a matter
kernel

$$
\Gamma_{g_a,a}^{matter}(m'\mid m)
$$

and comparison maps implementing fixed-background operational curvature for
the metric candidate \(I_a(g_a)\).  Define the frozen total kernel

$$
\Gamma_{a}^{fr}(m',g'\mid m,g)
:=
\Gamma_{g,a}^{matter}(m'\mid m)\,\mathbf 1_{\{g'=g\}}.
$$

This is a finite whole-process kernel on \(C_{\Sigma,a}^{tot}\).

### Proposition 3.2: Frozen-Geometry Lift Is Stochastic

If \(\Gamma_{g,a}^{matter}\) is stochastic for every \(g\), then
\(\Gamma_a^{fr}\) is stochastic.

Proof.

For fixed \((m,g)\),

$$
\sum_{m',g'}\Gamma_a^{fr}(m',g'\mid m,g)
=
\sum_{m'}\Gamma_{g,a}^{matter}(m'\mid m)
=1.
$$

Nonnegativity is inherited from the matter kernel.  `square`

### Proposition 3.3: Frozen-Geometry Lift Recovers Paper 5

On each sector \(g'=g\), the exchange-curvature theorem of Paper 5 is
unchanged:

$$
\mathfrak C_{op,a}^{g}[N,M]
\to
K_i[I_a(g)^{ij}(N\partial_jM-M\partial_jN)]
$$

whenever the Paper-5 transport hypotheses hold for that finite geometry
record and its continuum limit.

Proof.

The geometry record is constant under the frozen kernel, so the matter-sector
comparison maps are exactly the fixed-background comparison maps of Paper 5.
The total space only adds a spectator finite label \(g\).  Therefore the
Paper-5 theorem applies on each fixed sector.  `square`

### Definition 3.4: Nontrivial Geometry-Update Kernel

A nontrivial finite geometry-update kernel is a stochastic matrix

$$
G_a(g'\mid g)
$$

on \(C_{\Sigma,a}^{geom}\) such that

$$
G_a(g'\mid g)>0
$$

for at least one \(g'\ne g\).

For example, choose a finite set of local moves that changes one cell's matrix
entry by one quantization step while preserving positive definiteness, then
take a lazy random walk:

$$
G_a(g'\mid g)
=
(1-\rho)\mathbf 1_{\{g'=g\}}
+\rho\,R_a(g'\mid g),
\qquad 0<\rho<1,
$$

where \(R_a\) is uniform over admissible one-cell moves.

### Definition 3.5: Joint Matter-Geometry Kernel

Given a matter kernel depending on both initial and final geometry,

$$
M_a(m'\mid m,g,g'),
$$

define

$$
\Gamma_a^{dyn}(m',g'\mid m,g)
:=
M_a(m'\mid m,g,g')G_a(g'\mid g).
$$

This formula is a definition of a single whole-process joint kernel.  It must
not be read as a hidden temporal factorization.  It is a finite probability
assignment on the pair \((m',g')\).

### Proposition 3.6: Nontrivial Joint Kernel Is Stochastic

If \(G_a\) is stochastic and \(M_a(\cdot\mid m,g,g')\) is stochastic for every
\((m,g,g')\), then \(\Gamma_a^{dyn}\) is stochastic.  If \(G_a\) is nontrivial,
then geometry changes with positive probability.

Proof.

For fixed \((m,g)\),

$$
\sum_{m',g'}\Gamma_a^{dyn}(m',g'\mid m,g)
=
\sum_{g'}G_a(g'\mid g)\sum_{m'}M_a(m'\mid m,g,g')
=
\sum_{g'}G_a(g'\mid g)
=1.
$$

If \(G_a(g'\mid g)>0\) for some \(g'\ne g\), then
\(\sum_{m'}\Gamma_a^{dyn}(m',g'\mid m,g)>0\).  `square`

### Theorem 3.7: Geometry Can Become Part Of The Finite Configuration Law

The weak Paper-6 gate holds:

$$
\mathrm{V4P6\text{-}GEOM\text{-}IN\text{-}CONFIG}^{fin}.
$$

Proof.

Definitions 2.1 and 1.2 give finite total configuration spaces with geometry
records as ordinary finite labels.  Proposition 2.3 shows that the labels can
approximate smooth metric data in the benchmark interpretation.  Definition
3.1 and Propositions 3.2 and 3.3 give a frozen-geometry reduction to Paper 5.
Definitions 3.4 and 3.5 and Proposition 3.6 give nontrivial finite
geometry-update kernels.  No Hilbert phase, continuum metric ontology,
Einstein equation, or hidden Markov intermediate state is used.  `square`

### Corollary 3.8: The Gate Is Not Vacuous

The geometry variable is not merely a decorative label.  It can:

1. carry metric candidates;
2. enter matter transition probabilities;
3. be held fixed to recover Paper 5;
4. change with positive probability under a finite same-law kernel.

It remains dynamically underdetermined.

## 4. Projective Compatibility

### Definition 4.1: Geometry Coarse-Graining

For \(a'<a\) with \(a'\) finer, let

$$
P_{a\leftarrow a'}^{geom}
:
C_{\Sigma,a'}^{geom}\to C_{\Sigma,a}^{geom}
$$

average fine cell matrices into coarse cells and then round to the coarse
quantization mesh, preserving the orientation and boundary records by the
declared finite rule.

Let

$$
P_{a\leftarrow a'}^{tot}
:=
P_{a\leftarrow a'}^{matter}\times P_{a\leftarrow a'}^{geom}.
$$

### Definition 4.2: Projective Dynamical Geometry Compatibility

A family \(\Gamma_a^{tot}\) is projectively compatible if

$$
P_{a\leftarrow a'}^{tot}\Gamma_{a'}^{tot}
-
\Gamma_a^{tot}P_{a\leftarrow a'}^{tot}
\to0
$$

in the declared observable topology.

### Proposition 4.3: Frozen Projective Compatibility Is Inherited

If the matter kernels of Paper 5 are projectively compatible on each fixed
geometry sector and the geometry coarse-graining maps are compatible with the
chosen metric records, then the frozen-geometry lifts are projectively
compatible.

Proof.

On each geometry sector \(g\), the frozen lift is the matter kernel tensored
with the identity on geometry.  Coarse-graining sends one fixed geometry
sector to another fixed geometry sector.  The commutator of coarse-graining
and evolution therefore reduces to the matter-sector commutator plus the
declared geometry rounding error.  Both vanish under the hypotheses.  `square`

### Proposition 4.4: Nontrivial Geometry Dynamics Is Not Automatically
Projective

A nontrivial finite geometry-update kernel \(G_a\) need not satisfy projective
compatibility.

Proof.

Choose a fine geometry kernel that flips one fine cell inside a coarse cell
with positive probability, and choose a coarse kernel that never changes the
corresponding coarse cell.  Then evolving first and coarse-graining changes
the coarse record with positive probability, while coarse-graining first and
evolving does not.  Hence the projective commutator is nonzero.  `square`

### Conditional Theorem 4.5: Projective Dynamical Geometry Gate

The stronger projective gate

$$
\mathrm{V4P6\text{-}PROJ\text{-}DYN\text{-}GEOM}^{cond}
$$

holds if:

1. geometry coarse-graining is declared;
2. \(G_a\) is compatible with that coarse-graining;
3. \(M_a\) is compatible with matter and geometry coarse-graining;
4. the metric interpretation maps are regulator-stable.

Proof.

Under these hypotheses, the projective commutator of the joint kernel splits
into geometry-update, matter-update, and interpretation errors.  Each is
declared to vanish in the observable topology.  Therefore the total
commutator vanishes.  `square`

### Implementation 4.6: A Conservative Projective Template

The safest current implementation is the frozen template plus rare
coarse-cell moves.  At each regulator:

1. select a coarse cell;
2. modify all fine subcells coherently so that coarse-graining sees the same
   move;
3. reject moves that violate positive definiteness or boundary records;
4. use the same move list at all refinements.

This does not produce Einstein dynamics.  It only gives a concrete way to
make nontrivial geometry updates compatible with a chosen projective system.

## 5. Why This Does Not Derive GR Dynamics

### Theorem 5.1: Same Metric Readout, Many Geometry Dynamics

The data sourced in Papers 4 and 5 do not determine the finite geometry
kernel.

Proof.

Fix the same finite geometry alphabet, the same metric interpretation map,
and the same Paper-5 fixed-background matter kernels.  Consider three total
kernels:

1. frozen geometry:

   $$
   \Gamma_a^{fr}(m',g'\mid m,g)
   =
   \Gamma_{g,a}^{matter}(m'\mid m)\mathbf 1_{\{g'=g\}};
   $$

2. lazy random-walk geometry:

   $$
   \Gamma_a^{rw}(m',g'\mid m,g)
   =
   M_a(m'\mid m,g,g')G_a^{rw}(g'\mid g);
   $$

3. reset geometry:

   $$
   \Gamma_a^{reset}(m',g'\mid m,g)
   =
   M_a(m'\mid m,g,g')\pi_a(g'),
   $$

   where \(\pi_a\) is a fixed probability distribution on geometry records.

All three share the same one-time geometry alphabet and can share the same
metric readout map.  They can also agree on the frozen-sector Paper-5 tests
when \(g'=g\).  But they have different transition probabilities for
geometry.  Therefore the metric readout and fixed-background curvature tests
do not determine the geometry dynamics.  `square`

### Corollary 5.2: Finite Geometry In Configuration Does Not Imply Einstein
Dynamics

The theorem

$$
\mathrm{V4P6\text{-}GEOM\text{-}IN\text{-}CONFIG}^{fin}
$$

does not imply

$$
\mathrm{V4P6\text{-}GR\text{-}DYN\text{-}FROM\text{-}CONFIG}^{cur}.
$$

Proof.

If geometry-in-configuration implied GR dynamics, then the same finite
geometry alphabet and metric interpretation data would determine a unique
GR-compatible dynamical law.  Theorem 5.1 gives inequivalent laws with the
same readout and fixed-background tests.  `square`

### Proposition 5.3: Constraint Closure Is A New Input

A geometry-update kernel must satisfy additional conditions before it can be
called a GR candidate:

1. constraint propagation;
2. lapse and shift covariance;
3. compatibility with the hypersurface-deformation algebra;
4. a stress-response or conservation law;
5. a continuum limit selecting Einstein or some other geometric dynamics.

None of these follows from finiteness alone.

Proof.

Finiteness only gives a stochastic matrix on a finite set.  A generic
stochastic matrix has no reason to preserve constraints, transform
covariantly under lapse/shift changes, or have a continuum geometric action.
The frozen, random-walk, and reset kernels already separate these notions.
`square`

## 6. Nonvacuity Filters For Future Dynamical Geometry

The weak positive theorem is real but too easy unless future papers impose
filters.  A finite dynamical geometry law must pass the following gates.

### Filter 6.1: Metric Reconstruction

The finite geometry records must recover tensorial, symmetric, positive,
regulator-stable metric candidates:

$$
I_a(g_a)\to h^{ij}.
$$

### Filter 6.2: Frozen-Background Reduction

Holding \(g_a\) fixed must recover the Paper-5 operational curvature law:

$$
\mathfrak C_{op,a}^{g}[N,M]
\to
K_i[h^{ij}(N\partial_jM-M\partial_jN)].
$$

### Filter 6.3: Projective Consistency

The joint matter-geometry kernels must commute with coarse-graining in the
declared observable topology:

$$
P_{a\leftarrow a'}^{tot}\Gamma_{a'}^{tot}
-
\Gamma_a^{tot}P_{a\leftarrow a'}^{tot}\to0.
$$

### Filter 6.4: Locality Without Hidden Markovization

The kernel may be local in the sense of support/collar dependence, but it may
not be justified by assuming unrecorded intermediate hypersurface states.

### Filter 6.5: Constraint And Gauge Handling

The geometry records must include or quotient gauge redundancies explicitly.
If constraints are imposed, the kernel must preserve them or project onto
them by a declared finite rule.

### Filter 6.6: Stress-Response Compatibility

If matter is present, the joint law should support the Paper-5 style
stress-response Ward identity under tangential covariance.  Otherwise it is
only a kinematic geometry law.

### Filter 6.7: Continuum Limit Identification

If the target is GR, the continuum limit must identify the Einstein dynamics
or a controlled deformation of it.  This cannot be imported by calling the
finite labels "metric."

## 7. Conditional Positive Dynamical Templates

This section advances the conditional positive result as far as it can go
without importing Einstein equations.

### Template 7.1: Constraint-Preserved Finite Geometry Law

Let

$$
{\mathcal K}_a\subset C_{\Sigma,a}^{geom}
$$

be a finite admissible geometry subset, for example records satisfying
positive definiteness, boundary conditions, and any declared discrete
constraints.  A constraint-preserved kernel has

$$
G_a(g'\mid g)=0
\qquad
\hbox{if }g\in{\mathcal K}_a,\ g'\notin{\mathcal K}_a.
$$

This is easy to implement by rejection: propose a local move and reject it if
it leaves \({\mathcal K}_a\).

### Proposition 7.2: Rejection Implements Constraint Preservation

If every inadmissible move is rejected and replaced by \(g'=g\), then
\({\mathcal K}_a\) is preserved with probability one.

Proof.

Starting from \(g\in{\mathcal K}_a\), every accepted move lands in
\({\mathcal K}_a\), and every rejected move leaves the state at \(g\).  Hence
the next state remains in \({\mathcal K}_a\).  `square`

### Template 7.3: Local Detailed-Balance Geometry Law

Let \(S_a(g)\) be any finite real function on \(C_{\Sigma,a}^{geom}\).  Define
a Metropolis-type kernel using local proposals \(Q_a(g'\mid g)\):

$$
G_a(g'\mid g)
=
Q_a(g'\mid g)\min\{1,\exp[-S_a(g')+S_a(g)]\}
$$

for \(g'\ne g\), with the diagonal chosen so columns sum to one.

This is a finite stochastic geometry law.  If \(S_a\) is later shown to
converge to a gravitational action or entropy functional, then the template
could become dynamical.  Without such a theorem, \(S_a\) is only a chosen
finite score.

### Proposition 7.4: Detailed-Balance Template Is Barandes-Compatible

The local detailed-balance geometry law is compatible with ISP ontology as a
finite whole-process probability assignment, provided it is not interpreted as
hidden Euclidean time or an unrecorded Markov factorization.

Proof.

At fixed regulator it is simply a stochastic matrix on a finite configuration
space.  The formula is a way to assign transition probabilities, not an
ontological claim that the slab decomposes into hidden substeps.  `square`

### Template 7.5: Source-Response Geometry Law

Let \(\alpha\) be a finite geometric source coupled to geometry records, and
let

$$
p_{\alpha,a}(m,g)
$$

be a positive normalized finite law on total records.  The score

$$
X_A(m,g)=\partial_A\log p_{\alpha,a}(m,g)
$$

obeys the Paper-4 score and Fisher identities.  This gives a finite response
calculus for geometry variables.  It does not choose the geometry dynamics by
itself.

### Conditional Theorem 7.6: Dynamical Geometry Program Template

If a finite total kernel satisfies:

1. finite geometry records approximate metric data;
2. frozen sectors recover Paper 5;
3. projective consistency holds;
4. admissible geometry constraints are preserved;
5. local detailed-balance or source-response structure has a regulator-stable
   continuum limit;
6. the continuum limit satisfies the hypersurface-deformation algebra and
   stress-response Ward identities;

then the V4 dynamical geometry program advances to the constraint-algebra
stage.

Proof.

Items 1 and 2 give metric meaning and fixed-background curvature.  Item 3
gives regulator stability.  Item 4 gives admissible geometry evolution.
Items 5 and 6 are exactly the missing dynamical selection principles.  With
these in place, the finite law is no longer merely a geometry alphabet; it is
a candidate dynamical geometry law.  `square`

### Implementation Status 7.7

Items 1 through 4 have concrete finite implementations in this paper.  Items
5 and 6 are not sourced by the current corpus.  They are the next real
mathematical target.

## 8. Barandes Alignment Audit

### Proposition 8.1: Weak Geometry-In-Configuration Is Barandes-Aligned

The construction of Sections 2 and 3 is Barandes-aligned.

Proof.

The primitive objects are finite configurations and finite stochastic
whole-process kernels.  Geometry appears as finite records \(g_a\), not as a
smooth metric ontology.  The continuum metric is recovered only through the
interpretation map \(I_a\) and the regulator limit.  No Hilbert phase,
Einstein equation, or hidden Markov intermediate state is used.  `square`

### Proposition 8.2: The Strong GR Claim Would Not Be Barandes-Aligned Unless
Its Dynamics Is Sourced

Claiming that the finite geometry alphabet already proves GR dynamics would
violate the no-smuggling discipline.

Proof.

Theorem 5.1 shows that the same finite geometry records allow multiple
inequivalent dynamics.  Selecting the Einstein one by assertion would import
continuum GR rather than derive it from finite ISP data.  `square`

## 9. Final Settlement

### Theorem 9.1: Paper-6 Gate Settlement

The Paper-6 issue is fully settled:

1. finite geometry records can be ordinary finite configuration variables;
2. total matter-geometry configuration spaces and stochastic kernels are
   straightforward finite ISP objects;
3. frozen geometry recovers Paper 5;
4. nontrivial geometry-update kernels exist;
5. projective nontrivial geometry is conditional, not automatic;
6. GR dynamics is not derived from the current corpus.

Proof.

Items 1 through 4 are Theorem 3.7 and its supporting propositions.  Item 5 is
Propositions 4.3 and 4.4 plus Conditional Theorem 4.5.  Item 6 is Theorem 5.1,
Corollary 5.2, and Proposition 5.3.  `square`

### Final Verdict 9.2

The weak gate passes:

$$
\boxed{
\mathrm{V4P6\text{-}GEOM\text{-}IN\text{-}CONFIG}^{fin}
\quad\hbox{true}.
}
$$

The strong gate remains unsourced:

$$
\boxed{
\mathrm{V4P6\text{-}GR\text{-}DYN\text{-}FROM\text{-}CONFIG}^{cur}
\quad\hbox{not sourced}.
}
$$

Plainly: geometry can become part of the finite ISP configuration law, but
that only moves V4 from "geometry is an external benchmark" to "geometry is an
ordinary finite record variable."  It does not yet move V4 to general
relativity.

The next paper must source the dynamical selection principle:

$$
\boxed{
\hbox{Which finite matter-geometry kernels deserve to be called GR-like?}
}
$$

The live candidates are constraint algebra, finite stress-response
conservation, projective local detailed balance, or a no-go theorem showing
that the current finite setup remains external-geometry only.
