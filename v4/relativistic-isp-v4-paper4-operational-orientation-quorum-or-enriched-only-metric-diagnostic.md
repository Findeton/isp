# Relativistic ISP V4 Paper 4: Operational Orientation Quorum Or Enriched-Only Metric Diagnostic

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed enriched-quorum, source-response Ward, and enriched
curved-background coefficient-test settlement.

## Abstract

V4 Paper 3 proves that passive finite records built from the current bare
Gamma data cannot recover the missing rotated-metric orientation.  This paper
settles the remaining operational route.

There is a precise positive theorem, but it is enriched:

$$
\mathrm{V4P4\text{-}OPINST\text{-}ORI\text{-}QUORUM}^{decl}
$$

holds if the finite same-law experiment is allowed to include operational
settings and outcomes whose probabilities respond to the signed metric
coefficient.  A minimal binary finite table distinguishes \(E_+\) from
\(E_-\), extracts the signed \(h^{12}\), and can be extended to an enriched
metric diagnostic satisfying the Paper-2 metric gates.

There is also a precise negative theorem:

$$
\neg\mathrm{V4P4\text{-}OPINST\text{-}ORI\text{-}QUORUM}^{\Gamma,cur}.
$$

The current bare Gamma corpus does not derive such a response table.  If the
instrument probabilities are functions only of the old Gamma-level endpoint
kernels, Paper 3's equal-input no-go applies.  Thus the operational quorum is
Barandes-aligned only as a declared finite record law or enriched
representation diagnostic, not as a rescue of bare Gamma-level metric
reconstruction.

The V4 metric route is therefore settled into a fork:

$$
\boxed{
\hbox{accept enriched operational metric diagnostics}
\quad\hbox{or}\quad
\hbox{stop the Gamma-level ISP-GR metric program.}
}
$$

The paper then asks whether the same operational response layer gives new
quantitative force of the kind missing in V3.  It does, but only
conditionally.  Finite same-law response families obey score-zero,
Fisher-positivity, and Ward/Cauchy-Schwarz inequalities.  These identities
turn a missing signed value into a response bound if a same-law Fisher,
probability-floor, or derivative bound is supplied.  They do not, by
themselves, derive that bound from the current bare Gamma corpus.

Finally, the paper tests the GR-facing question directly.  A local version of
the operational metric table reconstructs a fixed curved background
\(h^{ij}(x)\) as enriched record data.  If an enriched operational exchange
curvature law closes tangentially with that coefficient, then the
Dirac-Schwinger vector

$$
\beta^i(x)=h^{ij}(x)(N\partial_jM-M\partial_jN)
$$

is recovered.  But the metric table alone does not manufacture the
exchange-curvature law.  Thus the fixed curved-background issue is settled:
positive as an enriched coefficient diagnostic and conditional bracket test;
negative as a derivation from bare Gamma data or from the detector table
alone.

## 0. Imports And Discipline

### Import 0.1: Paper-2 Metric Gate

Paper 2 proves that a coefficient \(C^{ij}\) is fixed-background inverse
metric data if it is extracted from local first-jet exchange curvature and
passes tensoriality, symmetry, positivity, and regulator-stability gates.

### Import 0.2: Paper-3 Orientation No-Go

Paper 3 proves:

$$
\neg\mathrm{V4P3\text{-}GAMMA\text{-}ORI\text{-}REC}^{cur}.
$$

The no-go is an equal-input theorem.  If two backgrounds \(E_+,E_-\) have the
same bare Gamma data but opposite \(h^{12}\), then every passive function of
that Gamma data gives the same answer on both backgrounds.

### Barandes Rule 0.3

Operational instruments are allowed only as finite stochastic records:

1. settings are ordinary controlled records;
2. outcomes are ordinary readout records;
3. probabilities belong to the declared finite law;
4. no unrecorded Markov factorization is introduced;
5. Hilbert amplitudes, phases, tetrads, and principal symbols are not primitive
   ontology unless the claim is explicitly marked enriched.

## 1. Same-Law Operational Record Families

### Definition 1.1: Finite Same-Law Operational Family

Fix a regulated background label \(E\).  A finite same-law operational family
is a finite set of settings \(\Theta_a\), finite outcome sets
\(O_{\theta,a}\), and stochastic response maps

$$
P_{a,E}(o\mid\theta,q)
$$

where \(q\) is the declared preparation/readout configuration record.  In the
minimal orientation test, \(q\) can be suppressed and the law is simply

$$
P_{a,E}(o\mid\theta).
$$

Same-law means that all probabilities are part of one declared finite
experimental law.  It does not mean that the law is a passive function of the
old endpoint kernel \(\Gamma\).

### Definition 1.2: Operational Orientation Quorum

An operational orientation quorum for the ambiguity pair \(E_+,E_-\) is a
finite same-law operational family and a finite statistic \(W\) such that

$$
\sum_{\theta,o}W(\theta,o)P_{a,E_+}(o\mid\theta)
\ne
\sum_{\theta,o}W(\theta,o)P_{a,E_-}(o\mid\theta).
$$

It is metric-useful if the extracted signed coefficient survives the Paper-2
metric gates.

## 2. Minimal Binary Orientation Detector

### Definition 2.1: Normalized Sign Window

Let the ambiguity pair satisfy

$$
h_+^{12}=m,\qquad h_-^{12}=-m,\qquad m>0.
$$

Choose a scale \(\lambda>0\) such that

$$
0<\lambda m<1.
$$

This scale is an instrument normalization.  It is part of the operational
calibration, not a stochastic hidden variable.

### Definition 2.2: Two-Outcome Orientation Instrument

Let

$$
\Theta=\{\theta_{12}\},
\qquad
O_{\theta_{12}}=\{-1,+1\}.
$$

Define

$$
P_E(o\mid\theta_{12})
=
\frac{1}{2}\bigl(1+o\lambda h_E^{12}\bigr).
$$

Because \(0<\lambda |h_E^{12}|<1\), this is a valid probability law.

### Theorem 2.3: The Binary Instrument Distinguishes The Ambiguity Pair

The statistic

$$
S_{12}(E):=\sum_{o=\pm1}oP_E(o\mid\theta_{12})
$$

satisfies

$$
S_{12}(E)=\lambda h_E^{12}.
$$

Hence

$$
S_{12}(E_+)=-S_{12}(E_-)\ne0.
$$

Proof.

Compute:

$$
\sum_{o=\pm1}o\frac{1}{2}(1+o\lambda h_E^{12})
=
\frac{1}{2}\sum_{o=\pm1}o
+
\frac{\lambda h_E^{12}}{2}\sum_{o=\pm1}o^2
=
\lambda h_E^{12}.
$$

The first sum vanishes and the second sum equals \(2\).  Since
\(h_+^{12}=-h_-^{12}\ne0\), the displayed distinction follows.  `square`

### Corollary 2.4: Minimal Positive Enriched Quorum

The finite binary table proves

$$
\mathrm{V4P4\text{-}OPINST\text{-}ORI\text{-}QUORUM}^{decl}
$$

for the single signed off-diagonal ambiguity.

This is a positive finite stochastic record theorem.

## 3. Full Symmetric Metric Diagnostic Table

The previous section detects only the missing sign.  To feed Paper 2's metric
gate, the operational family must extract all symmetric entries.

### Definition 3.1: Entrywise Operational Table

In spatial dimension \(d\), let the settings be

$$
\Theta_d=\{\theta_{ij}:1\le i\le j\le d\}.
$$

For each \(\theta_{ij}\), let the outcome set be \(O_{ij}=\{-1,+1\}\).
Choose calibration scales \(\lambda_{ij}>0\) such that

$$
|\lambda_{ij}h_E^{ij}|<1
$$

for all tested backgrounds \(E\).  Define

$$
P_E(o\mid\theta_{ij})
=
\frac{1}{2}\bigl(1+o\lambda_{ij}h_E^{ij}\bigr).
$$

### Definition 3.2: Operational Metric Extractor

Define

$$
C_{op}^{ij}(E)
:=
\lambda_{ij}^{-1}\sum_{o=\pm1}oP_E(o\mid\theta_{ij})
\qquad (i\le j),
$$

and set \(C_{op}^{ji}=C_{op}^{ij}\).

### Proposition 3.3: The Table Extracts The Symmetric Metric Entries

For every tested fixed background \(E\),

$$
C_{op}^{ij}(E)=h_E^{ij}.
$$

Proof.

The same two-outcome calculation as Theorem 2.3 gives

$$
\sum_{o=\pm1}oP_E(o\mid\theta_{ij})=\lambda_{ij}h_E^{ij}.
$$

Dividing by \(\lambda_{ij}\) gives the claim.  Symmetry is imposed by the
choice \(i\le j\) and the definition \(C_{op}^{ji}=C_{op}^{ij}\).  `square`

### Corollary 3.4: Enriched Metric Diagnostic Passes Paper-2 Gates By
Construction

If the tested background metrics \(h_E^{ij}\) are tensorial, symmetric,
positive, nondegenerate, and regulator-stable, then the operational extraction
\(C_{op}^{ij}\) has the same properties.

Proof.

By Proposition 3.3, \(C_{op}^{ij}=h_E^{ij}\) entrywise.  Therefore every
metric gate possessed by the benchmark metric is inherited by the extracted
operational coefficient.  `square`

## 4. Why This Is Not A Bare Gamma Rescue

### Definition 4.1: Gamma-Derived Operational Quorum

An operational quorum is Gamma-derived if every response probability can be
written as a passive function of current Gamma-level data:

$$
P_E(o\mid\theta)=F_{\theta,o}(\Gamma_E,J_E,\mathfrak C_E).
$$

### Theorem 4.2: No Gamma-Derived Quorum Exists In The Current Corpus

For the rotated-metric ambiguity pair of Paper 3,

$$
\neg\mathrm{V4P4\text{-}OPINST\text{-}ORI\text{-}QUORUM}^{\Gamma,cur}.
$$

Proof.

Paper 3 supplies \(E_+,E_-\) with identical current Gamma-level data and
opposite \(h^{12}\).  If the operational responses are Gamma-derived, then

$$
P_{E_+}(o\mid\theta)
=
F_{\theta,o}(\Gamma_{E_+},J_{E_+},\mathfrak C_{E_+})
=
F_{\theta,o}(\Gamma_{E_-},J_{E_-},\mathfrak C_{E_-})
=
P_{E_-}(o\mid\theta).
$$

Every finite statistic of these responses is therefore equal on \(E_+\) and
\(E_-\).  But an orientation quorum must distinguish them.  Contradiction.
`square`

### Corollary 4.3: The Positive Table Is Enriched

The table in Definition 3.1 cannot be advertised as current Gamma-level metric
reconstruction unless an additional theorem derives its response probabilities
from the bare finite stochastic connection.

Proof.

If it were current Gamma-derived, Theorem 4.2 would forbid it from
distinguishing \(E_+\) and \(E_-\).  But Theorem 2.3 shows it distinguishes
them.  Thus it is not current Gamma-derived.  `square`

## 5. Nonvacuity Filters

The entrywise table is mathematically valid, but it is too easy if read as a
physics theorem.  To avoid a manufactured metric meter, any future use must
pass at least one nonvacuity filter.

### Filter 5.1: Process-Response Derivation

There must be a declared finite process response law

$$
P_E(o\mid\theta,q)
$$

whose dependence on \(h^{ij}\) follows from the same finite instrument
architecture, not from inserting \(h^{ij}\) by hand.

### Filter 5.2: Refinement Stability

For regulator levels \(a\), the extracted coefficients must satisfy

$$
C_{op,a}^{ij}\to C_{op}^{ij}
$$

under the same normalization convention used by Paper 2.

### Filter 5.3: Coordinate Covariance

Under a finite coordinate/refinement change \(x\mapsto x'\), the extracted
array must transform as the declared inverse tensor or inverse tensor density:

$$
C_{op}^{i'j'}
=
\frac{\partial x^{i'}}{\partial x^i}
\frac{\partial x^{j'}}{\partial x^j}
C_{op}^{ij}
$$

up to the declared density factor.

### Filter 5.4: Support And Locality

Settings \(\theta_{ij}(x)\) localized near \(x\) must not read out unrelated
regions.  The instrument must remain support-respecting in the same finite
operational sense used by the existing detector/control stack.

### Filter 5.5: No Hidden Markovization

The instrument may be a whole-process finite stochastic law, but it may not be
explained by inserting unrecorded intermediate states through which the
process is assumed to factor.

## 6. Enriched Process-Quorum Theorem

The previous sections used an explicit table.  The more invariant way to say
the same thing is process tomography.

### Definition 6.1: Finite Process Quorum

A finite process quorum is a finite family of preparations, settings, and
outcomes whose probabilities separate the finite process representatives in
the tested class modulo declared gauge equivalence.

### Theorem 6.2: Process Quorum Distinguishes Any Enriched Orientation
Difference

Suppose the enriched finite representatives \(Q_{E_+}\) and \(Q_{E_-}\) of
the two backgrounds are not gauge-equivalent.  Then there exists a finite
process quorum and a finite statistic distinguishing them.

Proof.

The tested process space is finite dimensional.  If
\(Q_{E_+}\ne Q_{E_-}\) modulo gauge, then some linear functional separates
their equivalence classes.  In finite dimension, such a linear functional can
be represented by a finite list of preparation/setting/outcome probabilities
after choosing a separating operational basis for the tested support.  The
corresponding finite statistic distinguishes \(E_+\) from \(E_-\).  `square`

### Corollary 6.3: What The Quorum Theorem Does And Does Not Prove

The theorem proves that enriched finite operational data can carry the missing
orientation.  It does not prove that the current bare Gamma data already carry
that orientation.

## 7. Operational Source-Response Ward Calculus

The orientation quorum is a finite probability table.  That means it has a
universal differential calculus independent of Hilbert phase.

### Definition 7.1: Finite Source Family

Let \(R\) be a finite record space and let

$$
p_\alpha(r)>0,\qquad r\in R,
$$

be a smooth family of normalized same-law probabilities:

$$
\sum_{r\in R}p_\alpha(r)=1.
$$

The parameter \(\alpha=(\alpha^A)\) may represent a geometric source, an
operational setting calibration, or a residual source parameter.  It is not an
unrecorded intermediate time.

### Definition 7.2: Score And Fisher Matrix

For each source coordinate \(\alpha^A\), define the finite score

$$
X_A(r):=\partial_A\log p_\alpha(r)
$$

and the Fisher matrix

$$
I_{AB}(\alpha):=
\mathbf E_\alpha[X_AX_B].
$$

### Theorem 7.3: Score-Zero Identity

For every finite source family,

$$
\mathbf E_\alpha[X_A]=0.
$$

Proof.

Differentiate normalization:

$$
0=\partial_A\sum_r p_\alpha(r)
=
\sum_r\partial_Ap_\alpha(r)
=
\sum_rp_\alpha(r)\partial_A\log p_\alpha(r)
=
\mathbf E_\alpha[X_A].
$$

`square`

### Theorem 7.4: Fisher Positivity

The Fisher matrix is positive semidefinite:

$$
v^AI_{AB}v^B\ge0.
$$

Proof.

By definition,

$$
v^AI_{AB}v^B
=
\mathbf E_\alpha[(v^AX_A)^2]\ge0.
$$

`square`

### Theorem 7.5: Finite Ward Identity

For any finite observable \(f_\alpha(r)\),

$$
\partial_A\mathbf E_\alpha[f_\alpha]
=
\mathbf E_\alpha[\partial_Af_\alpha]
+
\mathrm{Cov}_\alpha(f_\alpha,X_A).
$$

If \(f\) is source-independent, then

$$
\partial_A\mathbf E_\alpha[f]
=
\mathrm{Cov}_\alpha(f,X_A).
$$

Proof.

Differentiate the finite sum:

$$
\partial_A\sum_r f_\alpha(r)p_\alpha(r)
=
\sum_r(\partial_Af_\alpha(r))p_\alpha(r)
+
\sum_rf_\alpha(r)p_\alpha(r)\partial_A\log p_\alpha(r).
$$

The second term is \(\mathbf E_\alpha[f_\alpha X_A]\).  By Theorem 7.3,
\(\mathbf E_\alpha[X_A]=0\), so it is the covariance.  `square`

### Corollary 7.6: Ward Cauchy-Schwarz Bound

If \(f\) is source-independent, then

$$
|\partial_A\mathbf E_\alpha[f]|^2
\le
\mathrm{Var}_\alpha(f)I_{AA}.
$$

More generally, for a source direction \(u^A\),

$$
|\partial_u\mathbf E_\alpha[f]|^2
\le
\mathrm{Var}_\alpha(f)\,u^AI_{AB}u^B.
$$

Proof.

Use Theorem 7.5 and the ordinary Cauchy-Schwarz inequality in the finite
probability space:

$$
|\mathrm{Cov}(f,u^AX_A)|^2
\le
\mathrm{Var}(f)\mathbf E[(u^AX_A)^2].
$$

`square`

## 8. Applying The Ward Calculus To The Orientation Detector

### Proposition 8.1: Binary Detector Fisher Data

For the binary law

$$
p_x(o)=\frac{1}{2}(1+o\lambda x),
\qquad x=h^{12},
$$

the score and Fisher information are

$$
X_x(o)=\frac{o\lambda}{1+o\lambda x},
\qquad
I_{xx}(x)=\frac{\lambda^2}{1-\lambda^2x^2}.
$$

Proof.

The score formula is immediate from differentiating \(\log p_x(o)\).  Then

$$
I_{xx}
=
\sum_{o=\pm1}\frac{1}{2}(1+o\lambda x)
\frac{\lambda^2}{(1+o\lambda x)^2}
=
\frac{\lambda^2}{2}
\left(\frac{1}{1+\lambda x}+\frac{1}{1-\lambda x}\right)
=
\frac{\lambda^2}{1-\lambda^2x^2}.
$$

`square`

### Proposition 8.2: The Binary Detector Saturates Ward Cauchy-Schwarz

Let \(f(o)=o\).  Then

$$
\partial_x\mathbf E_x[o]=\lambda,
$$

and

$$
\mathrm{Var}_x(o)I_{xx}(x)=\lambda^2.
$$

Thus the Ward Cauchy-Schwarz bound is saturated.

Proof.

The expectation is \(\mathbf E_x[o]=\lambda x\), so its derivative is
\(\lambda\).  Also

$$
\mathrm{Var}_x(o)
=
1-(\lambda x)^2,
$$

and Proposition 8.1 gives

$$
\mathrm{Var}_x(o)I_{xx}(x)
=
(1-\lambda^2x^2)\frac{\lambda^2}{1-\lambda^2x^2}
=
\lambda^2.
$$

`square`

### Corollary 8.3: What The Binary Ward Bound Means

The binary table is an efficient detector for its declared source \(x=h^{12}\).
The Ward bound certifies that the signed off-diagonal response is a legitimate
finite probability response.

It does not prove that \(x\) is determined by bare Gamma data.  The same
Gamma-derived no-go of Theorem 4.2 still applies.

## 9. Off-Diagonal Bounds And Their Limits

### Proposition 9.1: Probability Normalization Gives Only A Calibration Bound

For the binary detector,

$$
|h^{12}|<\lambda^{-1}.
$$

This follows from positivity of the two probabilities, but it is only an
instrument calibration bound.

Proof.

The probabilities

$$
\frac{1}{2}(1\pm\lambda h^{12})
$$

are positive exactly when \(|\lambda h^{12}|<1\).  `square`

### Proposition 9.2: Metric Positivity Gives The Usual Off-Diagonal Bound

If the enriched operational table extracts a positive \(2\times2\) metric
block

$$
\begin{pmatrix}
C_{op}^{11} & C_{op}^{12}\\
C_{op}^{12} & C_{op}^{22}
\end{pmatrix},
$$

then

$$
|C_{op}^{12}|^2\le C_{op}^{11}C_{op}^{22}.
$$

Proof.

Positive semidefiniteness of a \(2\times2\) symmetric block is equivalent to
nonnegative principal minors.  The determinant condition gives

$$
C_{op}^{11}C_{op}^{22}-(C_{op}^{12})^2\ge0.
$$

`square`

### Corollary 9.3: No New Gamma-Level Off-Diagonal Bound Is Obtained

The bounds in Propositions 9.1 and 9.2 do not overcome the current Gamma-level
obstruction.

Reason:

1. Proposition 9.1 bounds only the detector calibration window.
2. Proposition 9.2 uses positivity of the already-extracted enriched metric
   block.
3. Neither bound derives the signed \(h^{12}\) from the current bare Gamma
   endpoint law.

Thus the source-response calculus supplies control once an operational law is
declared, but it does not create missing same-law value information out of
passive Gamma data.

## 10. Conditional Transfer Back To V3

### Definition 10.1: V3-Type Response Encoding

A V3 obstruction quantity \(A\) is response-encoded by a finite same-law
family \(p_s\) if there is a bounded finite record function \(f\) and a source
direction \(s\) such that

$$
A=\partial_s\mathbf E_s[f]\big|_{s=0}.
$$

Examples of possible \(A\)'s include signed residual amplitudes, selector
score responses, RN-MIXAMP derivatives, bridge amplitudes, or heat-bad source
responses.

### Theorem 10.2: Conditional V3 Ward Transfer

If a V3 obstruction quantity \(A\) is response-encoded by a finite same-law
family \(p_s\), then

$$
|A|^2
\le
\mathrm{Var}_{s=0}(f)\,I_{ss}(0).
$$

In particular, if

$$
\mathrm{Var}_{s=0}(f)\le V_*
\qquad\hbox{and}\qquad
I_{ss}(0)\le I_*,
$$

then

$$
|A|\le \sqrt{V_*I_*}.
$$

Proof.

Apply Corollary 7.6 at \(s=0\).  `square`

### Corollary 10.3: What A V3 Transfer Theorem Would Need

The operational Ward route can help V3 only if the corpus supplies:

1. a same-law response encoding of the missing V3 quantity;
2. a bounded record function or variance estimate;
3. a same-law Fisher, probability-floor, derivative, or curvature bound.

Without those inputs, the Ward identity is a tautological finite-probability
identity and does not close a V3 value gap.

### Proposition 10.4: Current Paper-4 V3 Transfer Status

Paper 4 proves the conditional transfer theorem but does not by itself close
any V3 primitive residual value theorem.

Proof.

Theorem 10.2 shows exactly how a finite same-law operational response bound
would imply a value bound.  But the hypotheses of Theorem 10.2 include the
same-law encoding and Fisher/variance inputs.  Those are precisely the kind of
quantitative actual-law inputs that V3 identified as missing.  Therefore Paper
4 maps the missing input into a sharper operational form; it does not erase
the need for that input.  `square`

## 11. Local Enriched Metric Records On A Fixed Curved Background

The constant-background table of Section 3 can be localized.  This section
settles what it can and cannot prove for a known curved background.

### Definition 11.1: Local Operational Metric Detector

Let \(U\) be a coordinate patch of a fixed spatial slice and let
\(\Lambda_a\subset U\) be a finite regulator grid.  For each cell
\(x\in\Lambda_a\), introduce finite settings

$$
\theta_{ij,x},\qquad 1\le i\le j\le d,
$$

and outcomes \(o\in\{-1,+1\}\).  For a fixed background metric \(h^{ij}(x)\),
choose calibration scales \(\lambda_{ij,a}(x)>0\) such that

$$
|\lambda_{ij,a}(x)h^{ij}(x)|<1
$$

on the tested patch.  Define the local response table

$$
P_{a,h}(o\mid\theta_{ij,x})
=
\frac{1}{2}\bigl(1+o\lambda_{ij,a}(x)h^{ij}(x)\bigr).
$$

This is an enriched operational record law.  It is not a passive Gamma-level
law.

### Definition 11.2: Local Operational Metric Extractor

Define

$$
C_{op,a}^{ij}(x)
:=
\lambda_{ij,a}(x)^{-1}
\sum_{o=\pm1}oP_{a,h}(o\mid\theta_{ij,x}),
\qquad i\le j,
$$

and set \(C_{op,a}^{ji}(x)=C_{op,a}^{ij}(x)\).

### Proposition 11.3: Local Metric Extraction

For every regulator cell \(x\in\Lambda_a\),

$$
C_{op,a}^{ij}(x)=h^{ij}(x)
$$

in the declared coordinate chart.

Proof.

The calculation is the same as Proposition 3.3, applied pointwise at \(x\):

$$
\sum_{o=\pm1}oP_{a,h}(o\mid\theta_{ij,x})
=
\lambda_{ij,a}(x)h^{ij}(x).
$$

Dividing by the calibration scale gives the claim.  `square`

### Corollary 11.4: Smooth Refinement Stability

If \(h^{ij}\) is smooth on the patch and the detector table is evaluated on
cell averages

$$
h_a^{ij}(x)=|Q_{a,x}|^{-1}\int_{Q_{a,x}}h^{ij}(y)\,dy,
$$

then

$$
C_{op,a}^{ij}(x)\to h^{ij}(x)
$$

at continuity points of \(h\), and uniformly on compact subpatches for smooth
\(h\) under a regular mesh.

Proof.

Proposition 11.3 gives \(C_{op,a}^{ij}(x)=h_a^{ij}(x)\).  Standard cell-average
convergence gives the stated limit.  `square`

### Proposition 11.5: Coordinate Covariance Requires Co-Transforming Settings

The local table is tensorial only if the operational settings transform with
the coordinate chart.  In a chart \(x'\), the extracted entries must satisfy

$$
C_{op}^{i'j'}
=
\frac{\partial x^{i'}}{\partial x^i}
\frac{\partial x^{j'}}{\partial x^j}
C_{op}^{ij}
$$

up to the declared density convention.  If the labels \(\theta_{ij,x}\) are
kept fixed as mere names under a coordinate change, tensoriality is not
earned.

Proof.

The table extracts whatever components it is calibrated to extract.  If the
settings are co-transformed with the chart, Proposition 11.3 extracts the
transformed components of the same tensor.  If the settings are not
co-transformed, the entries are just chart-labeled numbers with no tensorial
identification rule.  `square`

### Corollary 11.6: Enriched Local Metric Diagnostic

Under co-transforming settings, support localization, smooth refinement, and
positive-definite benchmark \(h^{ij}(x)\), the local operational table gives:

$$
\mathrm{V4P4\text{-}LOCAL\text{-}METRIC\text{-}DIAG}^{decl}.
$$

It is a valid enriched fixed-background metric diagnostic.

## 12. Enriched Curved-Background Exchange-Curvature Test

The local metric table gives a coefficient field.  A GR-facing
hypersurface-deformation test also needs a finite curvature law whose
tangential part uses that coefficient.

### Definition 12.1: Enriched Operational Curvature Compatibility

Write

$$
\mathrm{V4P4\text{-}OPCURV\text{-}COMPAT}
$$

if there are finite operational exchange-curvature maps
\(\mathfrak C_{op,a}[N,M]\) and finite tangential representations
\(K_{i,a}[v^i]\) such that, for smooth compactly supported lapse profiles,

$$
\mathfrak C_{op,a}[N,M]
\to
K_i\!\left[
C_{op}^{ij}(N\partial_jM-M\partial_jN)
\right]
$$

in the declared finite-effect or finite-record topology.

This is an enriched operational curvature law.  It is not supplied merely by
the detector table.

### Theorem 12.2: Enriched Fixed Curved-Background Bracket Test

Assume:

1. `V4P4-LOCAL-METRIC-DIAG^{decl}` holds;
2. `V4P4-OPCURV-COMPAT` holds;
3. the tangential representation \(K_i\) is faithful modulo declared gauge.

Then the enriched operational exchange curvature recovers the fixed
curved-background hypersurface-deformation vector

$$
\beta^i(x)=h^{ij}(x)(N\partial_jM-M\partial_jN).
$$

Proof.

By Corollary 11.6, \(C_{op}^{ij}(x)=h^{ij}(x)\) in the declared tensor
convention.  Substituting this coefficient into Definition 12.1 gives

$$
\mathfrak C_{op}[N,M]
=
K_i\!\left[
h^{ij}(N\partial_jM-M\partial_jN)
\right].
$$

Faithfulness identifies the tangential vector field modulo declared gauge.
`square`

### Corollary 12.3: Lapse-Jet Recovery On A Curved Background

At a point \(x\), choose lapse jets

$$
N(x)=1,\qquad M(x)=0,\qquad dN_x=0,\qquad dM_x=\omega.
$$

Then the recovered tangential vector satisfies

$$
\beta^i(x)=h^{ij}(x)\omega_j.
$$

Thus the enriched operational curvature test recovers the local inverse
metric action on covectors.

Proof.

Substitute the displayed jets into Theorem 12.2.  `square`

### Proposition 12.4: The Metric Table Alone Does Not Produce Curvature

The local operational metric detector does not by itself prove
`V4P4-OPCURV-COMPAT`.

Proof.

The detector table supplies probabilities for metric readout settings
\(\theta_{ij,x}\).  It does not define the localized normal deformation
comparison maps, their exchange two-cell, a tangential representation
\(K_i\), or the regulator-normalized curvature limit.  Those are additional
finite operational curvature data.  Therefore metric readout alone cannot
imply curvature compatibility.  `square`

### Corollary 12.5: Curved-Background Settlement

The fixed curved-background issue is settled as follows:

1. Positive coefficient diagnostic:

   $$
   \mathrm{V4P4\text{-}LOCAL\text{-}METRIC\text{-}DIAG}^{decl}.
   $$

2. Conditional bracket test:

   $$
   \mathrm{V4P4\text{-}OPCURV\text{-}COMPAT}
   \Longrightarrow
   \mathrm{V4P4\text{-}ENRICHED\text{-}CURVED\text{-}BACKGROUND\text{-}TEST}.
   $$

3. Negative automatic-dynamics claim:

   $$
   \neg\mathrm{V4P4\text{-}TABLE\text{-}IMPLIES\text{-}OPCURV}^{cur}.
   $$

The operational metric table is enough to diagnose the fixed curved metric
field.  It is not enough to derive the hypersurface-deformation bracket.

## 13. What This Does Not Yet Make Dynamical

### Proposition 13.1: No Einstein Dynamics Follows

The enriched fixed curved-background test does not imply Einstein equations,
dynamical geometry, or a Wheeler-DeWitt-type constraint.

Proof.

All background metric data in Sections 11 and 12 are fixed external benchmark
data, recorded through enriched operational settings.  No stochastic law on
geometry configurations is introduced, no variation with respect to dynamical
geometry is performed, and no stress-response conservation theorem is proved.
`square`

### Corollary 13.2: Next GR-Facing Gate

After Paper 4, the next GR-facing theorem is not "recover the metric" again.
It is one of:

1. finite stress-response Ward identity on an enriched fixed background;
2. finite operational curvature compatibility from explicit comparison maps;
3. dynamical geometry configuration gate.

## 14. Barandes Alignment Check

The positive enriched theorem is Barandes-aligned in the following limited
sense.

1. It uses finite configuration/readout records.
2. It uses ordinary probabilities.
3. It treats the instrument as a whole-process stochastic law.
4. It does not claim hidden Markov divisibility.
5. It does not make Hilbert phase primitive.

It is not Gamma-level in the following equally important sense.

1. The operational response probabilities are additional same-law records.
2. The bare endpoint kernel \(\Gamma=|U|^2\) still loses the sign.
3. The current corpus does not derive the entrywise table from Gamma.
4. Any Hilbert, tetrad, or principal-symbol derivation is a representation
   explanation of the instrument, not primitive ontology.

The source-response Ward extension is also Barandes-aligned:

1. it differentiates finite probabilities within one declared same-law family;
2. it does not introduce hidden intermediate states;
3. it treats Fisher information as a property of the finite record law;
4. it never identifies a Hilbert phase as primitive.

The fixed curved-background extension is Barandes-aligned in the same limited
sense:

1. local metric entries are read as finite operational records;
2. chart/tensor behavior is an explicit transformation rule for settings;
3. exchange-curvature compatibility is named as an additional finite
   operational law, not assumed from the detector table;
4. no Einstein dynamics is imported.

## 15. Final Settlement

### Theorem 15.1: Operational Orientation Quorum Is Enriched-Positive,
Gamma-Negative, Ward-Conditional, And Curved-Background Conditional

The V4 Paper-4 issue is fully settled as follows:

1. A finite same-law operational orientation quorum exists as a declared
   enriched record law:

   $$
   \mathrm{V4P4\text{-}OPINST\text{-}ORI\text{-}QUORUM}^{decl}.
   $$

2. The quorum can be extended to an enriched operational metric diagnostic:

   $$
   \mathrm{V4P4\text{-}ENRICHED\text{-}METRIC\text{-}DIAGNOSTIC}.
   $$

3. No current Gamma-derived operational quorum exists:

   $$
   \neg\mathrm{V4P4\text{-}OPINST\text{-}ORI\text{-}QUORUM}^{\Gamma,cur}.
   $$

4. Finite same-law operational families obey score-zero, Fisher-positivity,
   Ward, and Ward Cauchy-Schwarz identities.
5. For the binary orientation detector, the Ward Cauchy-Schwarz bound is
   saturated.
6. These identities give a conditional transfer theorem for V3-type signed
   obstruction quantities once same-law response encoding and Fisher/variance
   bounds are supplied.
7. Local enriched metric records recover a fixed curved background coefficient
   field \(h^{ij}(x)\) under co-transforming settings and refinement stability.
8. If enriched operational exchange curvature is compatible with this local
   coefficient, then the fixed curved-background tangential vector
   \(\beta^i=h^{ij}(N\partial_jM-M\partial_jN)\) is recovered.
9. The metric detector table alone does not derive that curvature
   compatibility and does not make geometry dynamical.
10. Therefore the fixed-background metric route cannot continue honestly as
   bare Gamma-level reconstruction.  It can continue only as enriched
   operational ISP-GR, unless a future theorem derives the operational
   response law from the finite stochastic connection itself.

Proof.

Item 1 is Theorem 2.3 and Corollary 2.4.  Item 2 is Proposition 3.3 and
Corollary 3.4.  Item 3 is Theorem 4.2.  Item 4 is Theorems 7.3 through 7.5
and Corollary 7.6.  Item 5 is Proposition 8.2.  Item 6 is Theorem 10.2 and
Corollary 10.3.  Item 7 is Corollary 11.6.  Item 8 is Theorem 12.2.  Item 9
is Proposition 12.4 and Proposition 13.1.  Item 10 follows from the
distinction between declared operational response records and passive
Gamma-derived data.
`square`

### Final Verdict 15.2

V4 should now stop trying to recover full signed metric data from the current
bare Gamma endpoint law.  The positive continuation is:

$$
\boxed{
\hbox{enriched operational ISP-GR metric diagnostics.}
}
$$

For the GR track, Paper 4 now settles the fixed curved-background coefficient
question: yes as enriched local metric records, yes as a conditional
exchange-curvature bracket test, and no as an automatic consequence of the
metric table or bare Gamma data.

The next GR theorem should therefore attack stress-response or explicit
operational curvature compatibility, not another metric-readout table.
