# Relativistic ISP V4 Paper 2: Fixed-Background Metric Data From Exchange Curvature

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed current-corpus metric-data gate.

## Abstract

V4 Paper 1 closes the attempt to use geometry as a direct source for the V3
Yang-Mills residual \(R\Sigma\).  This paper pivots to the cleaner ISP-GR
question:

$$
\hbox{Can finite ISP hypersurface exchange curvature reconstruct fixed
background metric data?}
$$

The answer is conditional yes, current-corpus Gamma-level no.

The conditional theorem is strong and simple.  If normalized finite
hypersurface exchange curvature has a regulator-stable continuum limit of the
form

$$
\mathcal F[N,M]
=
K_i[C^{ij}(N\partial_jM-M\partial_jN)],
$$

with faithful tangential representation \(K_i\), local first-jet dependence,
tensorial coordinate behavior, symmetry, positivity, and regulator stability,
then \(C^{ij}\) is fixed-background inverse spatial metric data, up to the
declared density convention.

The current-corpus verdict is negative for the bare Gamma-level Born-squared
route.  V2 Paper 10 already shows that the present Gamma-level rule loses the
orientation/cross-term data needed for rotated metric reconstruction.  Thus
the existing finite stochastic kernels do not reconstruct fixed-background
metric data at bare Gamma level.

This does not kill ISP-GR.  It identifies the next nontrivial route:

$$
\hbox{find an orientation-sensitive finite record invariant compatible with
Barandes-style ISP, or mark the result as enriched-representation only.}
$$

## 0. Imports And No-Smuggling Rule

### Import 0.1: V4 Paper 1

V4 Paper 1 proves that the geometry-source shortcut to the V3 Yang-Mills
residual is false for the current licensed source class:

$$
\neg\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}^{cur},
\qquad
\neg\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}^{cur}.
$$

Therefore this paper is not a Yang-Mills continuation.  It is an ISP-GR
metric-data gate.

### Import 0.2: V2 Paper 10

V2 Paper 10 proves the abstract metric-coefficient extraction lemma and then
finds a Gamma-level obstruction under the current Born-squared rule:

1. leading site/cell Born-squared coefficients fail the rotated-metric
   cross-term test;
2. higher-order frame-interference signals are quadratic/signless;
3. full Gamma-level metric reconstruction has an all-order sign ambiguity
   under the present Born-squared rule.

This paper does not ignore that result.  It promotes it to the V4
current-corpus verdict.

### No-Smuggling Rule 0.3

This paper may not import:

1. Einstein equations;
2. dynamical geometry;
3. continuum stress-energy;
4. Hilbert phase as primitive;
5. Markov factorization through unrecorded intermediate hypersurfaces.

The primitive objects are finite stochastic kernels, localized comparison
maps, and algebraic finite exchange-curvature tests.

## 1. Finite Hypersurface Stochastic Connection

### Definition 1.1: Finite Hypersurface Configuration Spaces

For each regulated Cauchy hypersurface \(\Sigma_a\), let

$$
C_{\Sigma_a}
$$

be a finite configuration space, and let

$$
\Delta(C_{\Sigma_a})
$$

be its probability simplex.

### Definition 1.2: Finite Slab Kernel

For a regulated slab or hypersurface path

$$
\gamma:\Sigma_a^0\to\Sigma_a^1,
$$

a finite ISP hypersurface kernel is a stochastic map

$$
\Gamma_{\gamma,a}:
\Delta(C_{\Sigma_a^0})\to\Delta(C_{\Sigma_a^1}).
$$

The kernel is a whole-process transition.  It is not assumed to factor
through unrecorded intermediate hypersurfaces.

### Definition 1.3: Localized Comparison Map

For a localized finite deformation \(R\), define the algebraic relative map

$$
J_{R,a}:=\Gamma_{R,a}\Gamma_{0,a}^{-1},
$$

where the inverse is algebraic on the declared finite image/quotient.  It need
not be stochastic.

### Definition 1.4: Finite Exchange Curvature

For two localized normal deformation profiles \(N,M\), define the finite
exchange-curvature two-cell

$$
E_a[N,M]
:=
J_{M|N,a}J_{N,a}
\bigl(J_{N|M,a}J_{M,a}\bigr)^{-1}.
$$

The normalized curvature is a scaled difference

$$
\mathfrak C_a[N,M]
:=
Z_a\bigl(E_a[N,M]-I\bigr),
$$

where \(Z_a\) is the declared regulator normalization.

This is the finite ISP analogue of comparing two orders of localized
hypersurface deformation.

## 2. Metric Reconstruction Target

The fixed-background target is the Dirac-Schwinger tangential bracket:

$$
[H[N],H[M]]=D[\beta],
\qquad
\beta^i=h^{ij}(N\partial_jM-M\partial_jN).
$$

In ISP language the target is not the operator equation itself.  The target is
that normalized finite exchange curvature converges to a tangential
deformation representation:

$$
\mathfrak C_a[N,M]\to
\mathcal F[N,M]
=
K_i[\beta^i(N,M)].
$$

Metric reconstruction asks whether the coefficient of

$$
N\partial_jM-M\partial_jN
$$

inside \(\beta^i\) can be read as inverse spatial metric data.

## 3. Conditional Extraction Theorem

### Definition 3.1: Metric-Candidate Coefficient

A local coefficient \(C^{ij}(x)\) is a metric-candidate coefficient if

$$
\mathcal F[N,M]
=
K_i[C^{ij}(x)(N\partial_jM-M\partial_jN)]
$$

for all compactly supported lapse profiles in the tested class.

### Theorem 3.2: Pointwise Metric-Coefficient Extraction

Assume spatial dimension \(d\ge2\).  Suppose:

1. \(\mathfrak C_a[N,M]\) has a continuum limit \(\mathcal F[N,M]\);
2. \(\mathcal F[N,M]\) closes tangentially as \(K_i[\beta^i(N,M)]\);
3. \(\beta^i(N,M)(x)\) is local, bilinear, alternating, and depends only on
   first jets of \(N,M\) at \(x\);
4. \(\beta^i(N,M)(x)=0\) whenever \(N(x)=M(x)=0\);
5. \(K_i\) is locally faithful modulo declared tangential gauge.

Then there is a unique local coefficient \(C^{ij}(x)\), modulo tangential
gauge, such that

$$
\beta^i(N,M)(x)
=
C^{ij}(x)(N\partial_jM-M\partial_jN)(x).
$$

Moreover \(C^{ij}(x)\) is pointwise extractable by lapse-jet tests:
choose \(N,M\) with

$$
N(x)=1,\quad M(x)=0,\quad dN_x=0,\quad dM_x=\omega.
$$

Then

$$
\beta^i(N,M)(x)=C^{ij}(x)\omega_j.
$$

Proof.

At a fixed \(x\), write

$$
a=N(x),\quad b=M(x),\quad
\xi_j=\partial_jN(x),\quad \eta_j=\partial_jM(x).
$$

A bilinear alternating first-jet expression has the form

$$
\beta_x^i
=
B^{ij}(x)(a\eta_j-b\xi_j)
+A^{ijk}(x)(\xi_j\eta_k-\eta_j\xi_k).
$$

The anchored condition \(\beta_x=0\) whenever \(a=b=0\) kills the
gradient-wedge term \(A^{ijk}\).  Set \(C^{ij}=B^{ij}\).  Local faithfulness
gives uniqueness: if two coefficients differ, choose compactly supported
lapses realizing an arbitrary covector \(\omega\) at \(x\), and the difference
annihilates every \(\omega\).  `square`

### Corollary 3.3: Metric Upgrade

If the extracted \(C^{ij}\):

1. transforms as a contravariant tensor or declared tensor density;
2. is symmetric;
3. is positive and nondegenerate on covectors;
4. is regulator-stable;

then \(C^{ij}\) is fixed-background inverse spatial metric data, or inverse
metric density data, according to the normalization convention.

## 4. The Full Fixed-Background Metric Gate

### Definition 4.1: `V4P2-METRIC-REC`

Write

$$
\mathrm{V4P2\text{-}METRIC\text{-}REC}
$$

if a finite ISP hypersurface-kernel system satisfies:

1. finite localized comparison maps and exchange curvature exist;
2. a regulator-stable continuum limit \(\mathcal F[N,M]\) exists;
3. tangential closure holds;
4. the local first-jet assumptions of Theorem 3.2 hold;
5. the tangential representation is faithful modulo declared gauge;
6. the extracted \(C^{ij}\) transforms tensorially;
7. \(C^{ij}\) is symmetric, positive, and nondegenerate;
8. in a fixed-background benchmark, \(C^{ij}\) agrees with the known
   background inverse metric or inverse metric density.

### Theorem 4.2: `V4P2-METRIC-REC` Reconstructs Fixed-Background Metric Data

If `V4P2-METRIC-REC` holds, then finite ISP hypersurface exchange curvature
reconstructs fixed-background metric data in the tested benchmark.

Proof.

Theorem 3.2 extracts \(C^{ij}\).  Corollary 3.3 upgrades it to inverse metric
or inverse metric density data.  Gate 8 identifies it with the known
fixed-background benchmark metric.  `square`

## 5. Current-Corpus Gamma-Level Benchmark

### Definition 5.1: Bare Gamma-Level Reconstruction

Write

$$
\mathrm{V4P2\text{-}GAMMA\text{-}METRIC\text{-}REC}
$$

if `V4P2-METRIC-REC` holds using only the finite stochastic kernels,
comparison maps, projective maps, and normalized exchange-curvature data
available at Gamma level, with no extra Hilbert lift, phase convention,
principal symbol, or enriched instrument.

### Proposition 5.2: Current Corpus Falsifies Bare Gamma-Level Metric Recovery

The current corpus proves

$$
\neg
\mathrm{V4P2\text{-}GAMMA\text{-}METRIC\text{-}REC}^{cur}.
$$

Proof.

V2 Paper 10 performs the relevant \(2+1D\) metric-data benchmark for the
current Gamma-level Born-squared rule.  It proves the extraction lemma, then
tests rotated/anisotropic fixed metrics.  The leading site/cell Born-squared
coefficient fails to recover rotated metric cross terms, and the higher-order
frame-interference signal is quadratic/signless.  The all-order conclusion is
a sign/orientation ambiguity for full Gamma-level metric reconstruction under
the present rule.  Therefore at least Gates 6 through 8 of Definition 4.1 fail
at current Gamma level: the extracted data do not determine the full tensorial
fixed-background metric.  `square`

### Corollary 5.3: What Exactly Failed

The failure is not that exchange curvature is meaningless.  The failure is
that the current bare stochastic endpoint kernel

$$
\Gamma=|U|^2
$$

loses orientation/cross-term data needed to reconstruct a general spatial
metric in \(d\ge2\).  In one spatial dimension this loss can hide inside a
single scalar coefficient.  In two or more spatial dimensions, rotated metrics
expose it.

## 6. Enriched Representation Is Not Gamma-Level Reconstruction

### Definition 6.1: Enriched Metric Diagnostic

An enriched metric diagnostic is a metric coefficient recovered only after
adding extra representation data, such as:

1. Hilbert phase or unitary amplitudes;
2. Dirac principal symbol;
3. spin frame or tetrad lift;
4. CAR/Fock structure;
5. a specified local field algebra.

### Proposition 6.2: Enriched Recovery Can Be Correct But Does Not Prove
Gamma-Level Metric Reconstruction

If a Dirac principal symbol contains a fixed frame \(E_A^{\ j}\), then the
ordinary QFT representation can recover

$$
h^{ij}=E_A^{\ i}E_A^{\ j}.
$$

But this is not Gamma-level ISP metric reconstruction unless the same
coefficient is determined by finite stochastic kernels and exchange curvature
without adding the principal symbol as primitive.

Proof.

The Dirac principal symbol already contains the frame.  Recovering \(h^{ij}\)
from it checks consistency of the enriched representation.  It does not show
that the stochastic connection alone determined the frame.  `square`

## 7. Orientation-Sensitive Future Route

The current Gamma-level obstruction suggests the next live route.

### Definition 7.1: Orientation-Sensitive Finite Record Invariant

An orientation-sensitive finite record invariant is a finite stochastic
record, instrument, or comparison-loop datum satisfying:

1. it is built from actual finite configurations or recorded outcomes;
2. it is not a hidden wavefunction or unrecorded phase;
3. it distinguishes the cross-term/sign data lost by \(|U|^2\);
4. it still defines finite hypersurface kernels or finite operational
   comparison maps;
5. it remains compatible with Barandes indivisibility, so it is not a Markov
   product through hidden intermediate states.

### Candidate Sources 7.2

Possible orientation-sensitive ISP-compatible data include:

1. signed detector outcomes included as configurations;
2. two-copy comparison records;
3. finite interference instruments whose outcomes are ordinary records;
4. oriented exchange-loop labels that are themselves recorded;
5. operational effect kernels rather than bare endpoint transition kernels.

These are not automatic solutions.  Each enlarges the finite record law and
must be audited for Barandes alignment.

### Definition 7.3: `V4P2-ORI-METRIC-REC`

Write

$$
\mathrm{V4P2\text{-}ORI\text{-}METRIC\text{-}REC}
$$

if an orientation-sensitive finite record invariant satisfies the eight gates
of `V4P2-METRIC-REC` without importing Hilbert phase as primitive.

## 8. Final Status Of The Paper-2 Question

### Theorem 8.1: Fixed-Background Metric Reconstruction Is Conditionally
Possible But Not Sourced By The Current Gamma-Level Corpus

The question

$$
\hbox{Can finite ISP hypersurface exchange curvature reconstruct fixed
background metric data?}
$$

has the following answer.

1. **Conditional theorem:** yes, if `V4P2-METRIC-REC` holds.
2. **Current Gamma-level corpus:** no, because
   \(\neg\mathrm{V4P2\text{-}GAMMA\text{-}METRIC\text{-}REC}^{cur}\).
3. **Enriched representation:** possible as a consistency diagnostic, but not
   Gamma-level reconstruction.
4. **Future ISP-GR route:** open only through an orientation-sensitive finite
   record invariant satisfying `V4P2-ORI-METRIC-REC`.

Proof.

Item 1 is Theorem 4.2.  Item 2 is Proposition 5.2.  Item 3 is Proposition
6.2.  Item 4 is Definition 7.3.  `square`

### Final Verdict 8.2

V4 Paper 2 does not prove that current finite ISP kernels reconstruct metric
data.  It proves the right conditional theorem and identifies the exact
current obstruction:

$$
\hbox{bare Gamma-level Born-squared data are not orientation-sensitive enough
to recover fixed-background metric cross terms.}
$$

The ISP-GR path is therefore not dead, but it cannot proceed by bare
Gamma-level endpoint probabilities alone.  The next paper must either build a
Barandes-aligned orientation-sensitive finite record invariant or accept that
metric reconstruction is only enriched-representation data.
