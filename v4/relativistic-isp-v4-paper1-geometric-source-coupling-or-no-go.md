# Relativistic ISP V4 Paper 1: Geometric Source Coupling Or No-Go

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed current-corpus and scoped truth-status settlement.  First
V4 gatekeeper.

## Abstract

V3 ended with a precise obstruction.  Clean heat, channel, gauge, Haar,
selector, passive reflection-positive, and finite-label sources do not cut the
scalar ray

$$
B=cI_2.
$$

The missing input is not another formal coordinate.  It is same-law value
information that actually sees the residual/signed product

$$
R\Sigma.
$$

This paper starts V4 cautiously.  It asks whether finite geometric source
response can provide that missing information.  The geometric source may be a
metric, tetrad, lapse, shift, edge-length, cell-volume, area, or localized
hypersurface-deformation parameter.  It is not assumed to be dynamical gravity.
It is a deterministic same-law source at source value zero.

The positive gate is

$$
\mathrm{V4P1\text{-}GEO\text{-}RSIGMA\text{-}COUPLE}(\varepsilon).
$$

It says that the finite geometric source derivatives recover, up to
\(\varepsilon\), the two scalar live responses \(m,t\) or an equivalent
ray-cutting projection of \(R\Sigma\).

The negative gate is

$$
\mathrm{V4P1\text{-}GEO\text{-}CLEAN\text{-}NOGO}.
$$

It says that every admissible geometric source currently available factors
through clean heat/channel/readout data and is therefore scalar-ray blind.

The completed result is negative at the current-corpus level.  The natural
finite geometric sources presently licensed by the V2/V3 corpus decompose
into clean, null, and unsourced residual-Hamiltonian derivative pieces.  The
clean and null pieces are scalar-ray blind; the residual-Hamiltonian
derivative is not printed by the corpus.  Therefore current-corpus finite
geometric source response does not couple to \(R\Sigma\).

This is not a global no-go over all possible future geometry-coupled ISP
laws.  It is a precise scoped falsification.  For the current licensed
geometric source class, both residual-Hamiltonian gates are false:

$$
\neg\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}^{cur},
\qquad
\neg\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}^{cur}.
$$

The unscoped versions are not meaningful proof targets until the source class
is declared, because arbitrary tilts can fake coupling.  A future positive
geometry route must therefore enlarge the finite law by proving, not naming,
the new primitive package

$$
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}
\quad+\quad
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}.
$$

## 0. Imports And Alignment

### Import 0.1: The V3 Endpoint

V3 Paper 37 reduces the live positive route to

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}COUPLE}
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}GRAM}
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}CURV}.
$$

The negative route is

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}RIGIDFLOOR}.
$$

The critical obstruction is the coupling part.  A source that only sees clean
heat or passive labels is not enough.  It must see the actual residual/signed
product \(R\Sigma\).

### Import 0.2: Paper 35 Scalar-Ray Detector

Any proposed constraint must be tested on deterministic scalar-ray laws
\(\nu_c\) supported on

$$
B=cI_2.
$$

If the constraint allows every admissible \(c\), it is ray-blind.  A useful
theorem must cut, orient, or floor the ray.

### Import 0.3: Local Barandes Corpus

The local Barandes papers used by this corpus treat quantum systems as
Hilbert-space representations of underlying indivisible stochastic processes.
The primitive data are configurations and whole stochastic processes, not
ontic wavefunctions or hidden Markov stages.

For this paper that means:

1. the primitive object is a finite record law or finite hypersurface kernel;
2. geometric sources are probes of that law, not new dynamics;
3. no Markov factorization through unrecorded intermediate states is assumed;
4. metric, tetrad, stress-energy, and curvature language is representational
   until finite same-law data earn it.

### No-Smuggling Rule 0.4

This paper may not import:

1. Einstein equations;
2. continuum stress-energy conservation;
3. a Hilbert-space stress tensor as primitive;
4. metric dynamics;
5. a path integral measure as primitive;
6. Markov divisibility inside the finite record law.

It may use those structures only as motivation or benchmark language after
translating every claim back into finite same-law response.

## 1. The Finite Same-Law Geometry Source

### Definition 1.1: Base Record Law

At fixed finite scale \((N,j,L)\), let

$$
\mu_0^{N,j,L}
$$

denote the actual adaptive pushed-forward record law used at the V3 endpoint.
Its records include the live block \(\Gamma_1\), the residual Hamiltonian
bookkeeping, selector data, endpoint conventions, conditional normalizers, and
the quotient by already licensed rows.

The subscript zero means that all new V4 geometric sources are set to zero.

### Definition 1.2: Geometric Source Family

A finite geometric source family is a \(k\)-parameter family

$$
\mu_\eta^{N,j,L},
\qquad
\eta=(\eta_1,\ldots,\eta_k)\in U\subset\mathbb R^k,
$$

such that:

1. \(\mu_\eta^{N,j,L}\) is a finite record law on the same declared record
   space, or on a canonically identified finite record space;
2. \(\mu_0^{N,j,L}\) is the original actual law;
3. \(\eta_a\) deforms only declared finite geometric data, such as local
   metric, tetrad, edge length, cell volume, face area, lapse, shift, or a
   localized hypersurface-deformation parameter;
4. the deformation is deterministic and externally declared, not sampled as a
   new hidden state;
5. all derivatives below are evaluated at \(\eta=0\).

### Definition 1.3: Same-Law Geometric Score

Assume \(\mu_\eta\) is differentiable at zero with respect to \(\mu_0\).  The
geometric score is

$$
S_a^{geo}
:=
\left.\partial_{\eta_a}\log {d\mu_\eta\over d\mu_0}\right|_{\eta=0}.
$$

This is an observable on the original same law \(\mu_0\).

It is not a new dynamics and not an intermediate Markov generator.

### Definition 1.4: Geometric Source Pressure

For any finite source observable \(X\), define

$$
\Phi_X(\lambda,\eta)
:=
\log \mathbf E_{\mu_\eta}\exp(\lambda X).
$$

At \((\lambda,\eta)=(0,0)\),

$$
\partial_{\eta_a}\Phi_X(0,0)=\mathbf E_{\mu_0}[S_a^{geo}],
$$

and

$$
\partial_{\lambda}\partial_{\eta_a}\Phi_X(0,0)
=
\operatorname{Cov}_{\mu_0}(X,S_a^{geo}).
$$

These are finite same-law quantities.

## 2. What It Means To Couple To \(R\Sigma\)

### Definition 2.1: Live Residual/Signed Product

Let

$$
B_{\Gamma_1}^{N,j}=R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}
$$

be the minimal live residual/signed product isolated in V3.

Its two-scalar compression is

$$
\Pi_+^{U_N}
\bigl(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}\bigr)
=
{mI_2+tU_N\over2}.
$$

The pair \((m,t)\) is the live scalar response pair.

### Definition 2.2: Geometric Coupling Matrix

Choose finite readout observables \(X_1,X_2\) whose scalar compression is the
V3 pair \(m,t\), or a declared equivalent two-dimensional ray detector.  The
geometric coupling matrix is

$$
C_{geo\to scal}
:=
\begin{pmatrix}
\operatorname{Cov}_{\mu_0}(X_1,S_1^{geo})&
\cdots&
\operatorname{Cov}_{\mu_0}(X_1,S_k^{geo})\\
\operatorname{Cov}_{\mu_0}(X_2,S_1^{geo})&
\cdots&
\operatorname{Cov}_{\mu_0}(X_2,S_k^{geo})
\end{pmatrix}.
$$

It is a same-law finite covariance matrix.

### Definition 2.3: `V4P1-GEO-RSIGMA-COUPLE`

Write

$$
\mathrm{V4P1\text{-}GEO\text{-}RSIGMA\text{-}COUPLE}
(\varepsilon,\sigma,M)
$$

if there exist:

1. a finite geometric source family \(\mu_\eta\);
2. two finite live readouts \(X_1,X_2\);
3. a finite reconstruction matrix \(Q\) acting on the vectorized coupling
   table;

such that

$$
\left\|
\begin{pmatrix}m\\ t\end{pmatrix}
-Q\,\operatorname{vec}(C_{geo\to scal})
\right\|
\le\varepsilon,
$$

and the usable two-dimensional part of \(C_{geo\to scal}\) has singular value
at least \(\sigma\), while all source scores and reconstruction coefficients
are bounded by \(M\) in the declared finite norms.

This is the first positive V4 theorem.

### Plain Meaning 2.4

The theorem says:

> If I slightly deform the finite geometry and watch the actual same-law
> probability response, I can recover the two scalar live quantities that V3
> could not source.

That is exactly the kind of change of viewpoint V3 was missing.

## 3. Why Geometry Is A Plausible Source

Clean heat sources alter representation weights.  Gauge/Haar sources alter
symmetry bookkeeping.  Selector sources alter labels.  Those are all blind on
the scalar ray.

A geometric source is different in principle.  It can alter:

1. local cell volumes;
2. local plaquette areas;
3. local lapse/shift weights;
4. local face-pairing costs;
5. local hypersurface-deformation defects;
6. local conditional normalizers;
7. the finite DLR Hamiltonian that defines a residual conditional row.

Those are exactly the places where \(R\Sigma\) lives.

This plausibility is not a proof.  It only explains why V4 Paper 1 is the
right next gate.

## 4. First Positive Implication

### Theorem 4.1: Geometric Coupling Sources The V3 Coupling Gate

If

$$
\mathrm{V4P1\text{-}GEO\text{-}RSIGMA\text{-}COUPLE}
(\varepsilon,\sigma,M)
$$

holds in a closing range, then the V3 structural coupling gate

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}COUPLE}(\varepsilon')
$$

holds with \(\varepsilon'\) equal to \(\varepsilon\) plus the declared
readout, quotient, and normalization ledger errors.

Proof.

`P37-STRUCTSRC-COUPLE` asks for structural same-law source derivatives whose
finite response identifies the live scalar pair or an equivalent ray detector.
Definition 2.3 gives exactly such derivatives, but with geometric source
scores.  The reconstruction matrix \(Q\) transfers the geometric covariance
rows to the scalar pair.  The remaining differences are the finite
bookkeeping errors already declared in the quotient ledger.  `square`

### Corollary 4.2: Why This Would Matter

If Paper 1 proves the positive gate, V4 does not solve confinement.  It does
something narrower and valuable:

1. it breaks the scalar-ray blindness of clean sources;
2. it gives Paper 37 the missing coupling input;
3. it makes Paper 2's Gram/Fisher target meaningful;
4. it justifies continuing the geometry program.

## 5. The Clean-Factorization No-Go

### Definition 5.1: Clean Factorization

A geometric source family has clean factorization if each geometric score
belongs to the closed finite span of already tried clean observables:

$$
S_a^{geo}
\in
\operatorname{span}
\{\hbox{clean heat, channel, gauge/Haar, selector, endpoint-additive,
normalizer-only rows}\}.
$$

### Theorem 5.2: Clean Factorization Is Ray-Blind

If every admissible geometric source at the current level has clean
factorization, then no such source proves
`V4P1-GEO-RSIGMA-COUPLE` in a scalar-ray-cutting range.

Proof.

Papers 32 through 37 prove that the listed clean rows are ray-blind.  On the
deterministic scalar-ray law \(B=cI_2\), their covariances with the live
ray-cutting scalar detector either vanish, reduce to already charged
constants, or remain invariant under every allowed \(c\).  A finite linear
combination of ray-blind rows is ray-blind.  Thus the geometric coupling
matrix \(C_{geo\to scal}\) cannot recover a nontrivial \(c\)-dependent
ray-cutting scalar pair.  `square`

### Definition 5.3: `V4P1-GEO-CLEAN-NOGO`

Write

$$
\mathrm{V4P1\text{-}GEO\text{-}CLEAN\text{-}NOGO}
$$

if clean factorization holds for every geometric source family licensed by the
current V4 setup.

### Corollary 5.4: Early Stop Rule

If `V4P1-GEO-CLEAN-NOGO` holds, then the V4 geometry pivot does not help
adaptive Branch A at this level.  The project should not proceed to dynamical
geometry or Einstein-limit papers until a non-clean geometric source is found.

## 6. What Counts As A Non-Clean Geometric Source

A useful geometric source must produce a score with a component outside the
clean span.  The first candidates are:

1. a local plaquette-area source that changes residual conditional weights
   after endpoint rows are quotiented;
2. a tetrad or frame source that changes the relative weighting of the two
   scalar channels \(I_2\) and \(U_N\);
3. a localized lapse/shift source that changes the finite hypersurface
   exchange defect rather than only the heat time;
4. a Regge-style edge-length source whose derivative changes a live face
   normalizer;
5. a cell-volume source whose derivative couples to the actual residual
   density \(H_{RPF}\);
6. a boundary-shape source whose derivative changes the doubly centered
   bridge residual.

The shared requirement is:

$$
\Pi_{clean^\perp}S_a^{geo}\ne0
$$

in a direction that has nonzero covariance with the live \(R\Sigma\) detector.

## 7. The Stress-Energy Warning

### Proposition 7.1: Metric Variation Does Not Automatically Give A Licensed Stress Tensor

The formal phrase

$$
T_{\mu\nu}\sim{\delta\log Z\over\delta g^{\mu\nu}}
$$

does not by itself prove any V4 theorem.

Proof.

The expression is a continuum representation formula.  V4 requires a finite
same-law score \(S_a^{geo}\) and finite covariances with live observables.
Unless the derivative is realized as a finite record-law Radon-Nikodym score
at source value zero, it is not a Barandes-aligned primitive object.  `square`

### Corollary 7.2: What A Licensed Stress Response Would Be

A stress-energy-like object becomes licensed only if V4 first proves a finite
identity of the form

$$
S_a^{geo}=T_a^{fin}+\hbox{charged quotient rows},
$$

where \(T_a^{fin}\) is an observable of the same record law and the quotient
rows are already accounted for.

## 8. Relation To Older Metric-Curvature Work

The earlier metric-data investigations provide motivation but not a Paper-1
solution.

They suggest that exchange curvature might recover a coefficient of the form

$$
\beta^i=h^{ij}(N\partial_jM-M\partial_jN).
$$

That is a geometric structure-function question.  Paper 1 asks a different
and earlier question:

$$
\hbox{does geometric response couple to }R\Sigma?
$$

Metric reconstruction is not useful for adaptive Branch A unless its finite
source derivative sees the residual/signed scalar obstruction.

## 9. Current-Corpus Audit

### Proposition 9.1: The Current Corpus Does Not Prove The Positive Gate

The current V2/V3 corpus does not prove
`V4P1-GEO-RSIGMA-COUPLE`.

Proof.

V2 Paper 10 investigates metric data from stochastic exchange curvature and
records a Gamma-level obstruction under the present Born-squared rule.  It
does not construct finite geometric source scores whose covariance recovers
the V3 live scalar pair.

V3 Papers 31 through 37 construct a source-response calculus, isolate the
scalar ray, test heat-bad, Peter-Weyl, Dobrushin, Ward, cumulant, residual,
RP, and scalar-field routes, and finally reduce the live source route to
structural coupling/Gram/curvature.  They prove that clean heat/channel
sources do not couple to \(R\Sigma\).  They do not print a metric, tetrad,
cell-volume, lapse-shift, or hypersurface-deformation score with nonzero
live \(R\Sigma\) covariance.  `square`

### Proposition 9.2: The Current Corpus Does Not Prove The Global No-Go

The current corpus also does not prove that all possible geometric sources are
clean-factorizing.

Proof.

The existing no-go theorems cover the sources actually constructed: clean
heat, gauge/Haar, selector, endpoint-additive, normalizer-only, passive RP,
and formal source derivatives with no new value bounds.  They do not classify
all finite metric/tetrad/hypersurface-deformation source families.  Therefore
`V4P1-GEO-CLEAN-NOGO` remains a new theorem, not a consequence already in the
corpus.  `square`

## 10. First Executable Worksheet

The smallest useful Paper-1 worksheet should use two geometric source knobs.

### Candidate A: Area And Shape

Let \(\eta_A\) deform the local plaquette area in \(\Gamma_1\).  Let
\(\eta_S\) deform the local shape or frame orientation while preserving the
same volume to first order.

The score pair is

$$
S_A^{geo},\qquad S_S^{geo}.
$$

The finite test matrix is

$$
C_{AS}
=
\begin{pmatrix}
\operatorname{Cov}(X_m,S_A^{geo})&
\operatorname{Cov}(X_m,S_S^{geo})\\
\operatorname{Cov}(X_t,S_A^{geo})&
\operatorname{Cov}(X_t,S_S^{geo})
\end{pmatrix}.
$$

The first concrete target is

$$
\det C_{AS}\ne0
$$

with controlled score envelope and curvature.

### Candidate B: Lapse And Shift

Let \(\eta_N\) deform local normal thickness and \(\eta_\beta\) deform local
tangential displacement in the finite hypersurface comparison cell.  This
pair is closer to the hypersurface-deformation bracket.

The test is identical:

$$
C_{N\beta}
=
\begin{pmatrix}
\operatorname{Cov}(X_m,S_N^{geo})&
\operatorname{Cov}(X_m,S_\beta^{geo})\\
\operatorname{Cov}(X_t,S_N^{geo})&
\operatorname{Cov}(X_t,S_\beta^{geo})
\end{pmatrix}.
$$

Candidate B is more geometrically meaningful, but it is also more dangerous:
it must not smuggle in Markovian infinitesimal evolution.

### Candidate C: Cell Volume And Boundary Shape

Let \(\eta_V\) change the local cell volume and \(\eta_{\partial}\) change the
boundary shape of the live block while preserving total volume.  This is the
most finite-record-friendly candidate.

The test is

$$
C_{V\partial}
=
\begin{pmatrix}
\operatorname{Cov}(X_m,S_V^{geo})&
\operatorname{Cov}(X_m,S_{\partial}^{geo})\\
\operatorname{Cov}(X_t,S_V^{geo})&
\operatorname{Cov}(X_t,S_{\partial}^{geo})
\end{pmatrix}.
$$

Candidate C is the preferred first worksheet because it can be defined without
continuum metric dynamics.

## 11. Candidate C Reduction: Cell Volume And Boundary Shape

This section begins the preferred worksheet rather than merely naming it.

### Definition 11.1: Local Geometric DLR Form

For the live block \(\Gamma_1\), assume the finite cell-volume and
boundary-shape source family can be written in local finite-DLR form:

$$
{d\mu_{\eta_V,\eta_{\partial}}\over d\mu_0}
=
{1\over Z_{\eta_V,\eta_{\partial}}}
\exp\bigl(-H_{\eta_V,\eta_{\partial}}^{loc}\bigr),
$$

where \(H_{\eta_V,\eta_{\partial}}^{loc}\) is the local finite conditional
Hamiltonian after quotienting endpoint-additive, selector-only, and already
licensed rows.

This is a finite Radon-Nikodym identity.  It is not a Markov decomposition.

### Lemma 11.2: The Candidate C Scores Are Centered Hamiltonian Derivatives

If Definition 11.1 holds and the local Hamiltonian is differentiable at zero,
then

$$
S_V^{geo}
=
-\partial_{\eta_V}H_{\eta}^{loc}\big|_0
+\mathbf E_{\mu_0}
\bigl[\partial_{\eta_V}H_{\eta}^{loc}\big|_0\bigr],
$$

and

$$
S_{\partial}^{geo}
=
-\partial_{\eta_{\partial}}H_{\eta}^{loc}\big|_0
+\mathbf E_{\mu_0}
\bigl[\partial_{\eta_{\partial}}H_{\eta}^{loc}\big|_0\bigr].
$$

Proof.

Differentiate the finite Radon-Nikodym identity in Definition 11.1 and use
the derivative of \(\log Z_{\eta}\) to center the Hamiltonian derivative under
\(\mu_0\).  This is the ordinary finite score identity.  `square`

### Definition 11.3: Clean/Residual Score Split

Split each Candidate C score as

$$
S_a^{geo}=S_a^{clean}+S_a^{res}+S_a^{null},
\qquad
a\in\{V,\partial\},
$$

where:

1. \(S_a^{clean}\) lies in the clean heat/channel/gauge/Haar/selector span;
2. \(S_a^{null}\) lies in the already charged quotient-null span;
3. \(S_a^{res}\) is the remaining residual geometric score.

Define the residual score table

$$
C_{V\partial}^{res}
=
\begin{pmatrix}
\operatorname{Cov}(X_m,S_V^{res})&
\operatorname{Cov}(X_m,S_{\partial}^{res})\\
\operatorname{Cov}(X_t,S_V^{res})&
\operatorname{Cov}(X_t,S_{\partial}^{res})
\end{pmatrix}.
$$

### Theorem 11.4: Candidate C Lives Entirely In The Residual Score Table

Candidate C proves `V4P1-GEO-RSIGMA-COUPLE` only through
\(C_{V\partial}^{res}\).  More precisely:

1. the clean part is scalar-ray blind;
2. the null part is quotient-charged and contributes no live scalar
   coupling;
3. the only possible ray-cutting contribution is
   \(C_{V\partial}^{res}\).

Proof.

The clean part is ray-blind by Theorem 5.2.  The null part is removed by the
same quotient ledger used in V3 Papers 32 through 37.  Therefore the
covariance table that can vary with the live scalar ray is exactly the
residual score covariance table.  `square`

### Definition 11.5: `V4P1-CELLBOUND-RSCORE`

Write

$$
\mathrm{V4P1\text{-}CELLBOUND\text{-}RSCORE}(\varepsilon,\sigma,M)
$$

if Candidate C has residual score table satisfying:

$$
\left\|
\begin{pmatrix}m\\ t\end{pmatrix}
-Q\,\operatorname{vec}(C_{V\partial}^{res})
\right\|
\le\varepsilon,
$$

for some finite reconstruction matrix \(Q\), with usable singular value at
least \(\sigma\), score envelope at most \(M\), and controlled quotient error.

### Corollary 11.6: Candidate C Positive Closure

If `V4P1-CELLBOUND-RSCORE(epsilon,sigma,M)` holds in a closing range, then
`V4P1-GEO-RSIGMA-COUPLE(epsilon',sigma',M')` holds with only finite ledger
losses.

Proof.

By Theorem 11.4, the clean and null parts do not contribute to live
ray-cutting.  Definition 11.5 gives the needed reconstruction from the
residual part.  `square`

### Corollary 11.7: Candidate C No-Go

If

$$
C_{V\partial}^{res}=0
$$

for every licensed cell-volume and boundary-shape source, then Candidate C is
clean-factorizing and cannot move the scalar ray.

### Proposition 11.8: Current-Corpus Status Of Candidate C

The current corpus does not prove `V4P1-CELLBOUND-RSCORE`.

Proof.

V3 prints the residual Hamiltonian bookkeeping and repeatedly identifies where
actual residual values would enter, but it does not print the derivative of
the actual residual conditional Hamiltonian with respect to finite cell volume
or boundary shape.  Without those derivatives, the residual geometric scores
\(S_V^{res}\) and \(S_{\partial}^{res}\) are not populated.  Therefore the
four entries of \(C_{V\partial}^{res}\) are not known.  `square`

### Provisional Lesson 11.9

The geometry pivot has already narrowed:

$$
\boxed{
\hbox{prove a finite residual geometric score table, or prove it vanishes.}
}
$$

This is a smaller and safer target than "derive gravity."  It is also the
first place where the V4 idea can really succeed or fail.

## 12. First Decision Theorem

### Theorem 12.1: V4 Paper 1 Decision Fork

At the current level, V4 Paper 1 has exactly three honest outcomes.

1. Prove `V4P1-GEO-RSIGMA-COUPLE(epsilon,sigma,M)` for a concrete finite
   geometric source family.  Then proceed to V4 Paper 2.
2. Prove `V4P1-GEO-CLEAN-NOGO` for the licensed geometric source class.  Then
   stop the geometry pivot for adaptive Branch A.
3. Prove neither.  Then V4 is not yet a proof route; it is a sharply defined
   experimental/theorem-search program whose next task is to populate one
   finite covariance table \(C_{geo\to scal}\).

Proof.

The V3 endpoint requires structural coupling before Gram and curvature become
useful.  Definition 2.3 is the geometric version of that coupling.  Theorem
5.2 proves the corresponding no-go if the sources factor through clean rows.
If neither side is proved, no downstream geometry theorem has a live scalar
target to act on.  `square`

## 13. Barandes Alignment Check

V4 Paper 1 is Barandes-aligned if read as a finite source-response paper.

1. It keeps finite record laws primary.
2. It does not introduce hidden intermediate Markov states.
3. It treats geometry as a deterministic source probe, not as an ontic
   wavefunction or pre-assumed gravitational field.
4. It requires all derivatives to be Radon-Nikodym scores on the same law at
   source value zero.
5. It forbids imported continuum stress tensors and Einstein equations.
6. It permits Hilbert/continuum/metric language only as benchmark
   representation after finite same-law scores are defined.

Therefore the paper is cautious enough to be aligned, while still allowing a
genuine new idea.

## 14. Provisional Verdict

The right V4 first move is not "unify relativistic ISP with general
relativity."  That phrase is too broad and too easy to overread.

The right first move is:

$$
\boxed{
\hbox{test whether finite geometric source response couples to }R\Sigma.
}
$$

If it does, V4 may have found the external mathematical force V3 lacked.

If it does not, V4 should say so quickly and avoid a beautiful dead end.

## 15. Next Work Inside Paper 1

The next concrete pass should now populate or refute the residual score table
from Section 11:

1. define the finite cell-volume and boundary-shape deformation of the actual
   local residual conditional Hamiltonian;
2. compute \(\partial_{\eta_V}H_{\eta}^{loc}|_0\) and
   \(\partial_{\eta_{\partial}}H_{\eta}^{loc}|_0\);
3. project away clean and null rows;
4. print \(S_V^{res}\), \(S_{\partial}^{res}\), and
   \(C_{V\partial}^{res}\);
5. test whether the scalar-ray trace is nonconstant in \(c\);
6. if nonconstant, send the table to V4 Paper 2 for Gram/Fisher lower bounds;
7. if constant or zero, record Candidate C as clean-factorizing/no-go evidence.

That is the narrowest useful continuation.

## 16. Exhaustive Current-Corpus Test Of The Natural Geometry Knobs

We now execute the test promised in Section 15 for the geometric source
families that are actually licensed by the current corpus.

The word "licensed" is important.  A licensed source is not an arbitrary new
law.  It must be assembled from data already present in the V2/V3 corpus:
finite heat kernels, clean channel weights, selector tables, endpoint rows,
finite hypersurface comparison maps, tree-gauge Jacobians, and the formal
residual Hamiltonian ledger.

### Definition 16.1: Current-Corpus Licensed Geometric Sources

Let \({\mathcal G}_{cur}\) be the class of finite geometric source
directions generated by the following already available operations:

1. changing local heat time or plaquette area in the heat-kernel reference;
2. changing a local frame, channel basis, or finite recoupling convention;
3. changing localized lapse/shift data in the already constructed finite
   hypersurface comparison maps;
4. changing endpoint, boundary, or selector labels already present in the
   adaptive record;
5. changing local normalizer conventions already represented by charged
   quotient rows;
6. differentiating a formally named residual Hamiltonian term only where the
   corpus prints the derivative as a finite same-law observable.

The last clause is deliberately strict.  A formal symbol \(H_{RPF}\) does not
license all of its geometric derivatives.

### Lemma 16.2: Area Sources Are Clean Unless They Differentiate \(H_{RPF}\)

For every area or heat-time source in \({\mathcal G}_{cur}\), the score
decomposes as

$$
S_A^{geo}=S_A^{HK}+S_A^{null}+S_A^{RPF?},
$$

where \(S_A^{HK}\) lies in the clean heat/channel span, \(S_A^{null}\) is
charged by endpoint or normalizer rows, and \(S_A^{RPF?}\) exists only if the
corpus prints a finite same-law derivative

$$
\partial_{\eta_A}H_{RPF}^{loc}\big|_0.
$$

Proof.

The area source changes the finite heat-kernel reference through heat time,
plaquette area, or local heat normalization.  Those pieces are exactly clean
heat/channel pieces.  Endpoint and normalizer variations are quotient rows.
The only remaining place where the area source can see \(R\Sigma\) is the
actual residual conditional Hamiltonian.  But such a derivative is not
created by the clean heat formula; it must be printed as a same-law
observable.  `square`

### Lemma 16.3: Shape And Frame Sources Are Clean Or Representation-Level

For every shape/frame source in \({\mathcal G}_{cur}\), the score decomposes
as

$$
S_S^{geo}=S_S^{rec}+S_S^{null}+S_S^{RPF?},
$$

where \(S_S^{rec}\) is a clean recoupling/frame/channel row, \(S_S^{null}\)
is charged by quotient rows, and \(S_S^{RPF?}\) again requires a printed
finite derivative of \(H_{RPF}^{loc}\).

Proof.

The V2 metric-data and V3 scalar-ray audits allow frame, channel, recoupling,
and representation tests as benchmarks.  They do not turn a change of frame
into a finite value theorem for the residual/signed product.  A frame source
can affect \(I_2\), \(U_N\), clean channel weights, and representation labels.
All of these are ray-blind unless the frame deformation also changes the
actual residual conditional Hamiltonian in a printed same-law way.  `square`

### Lemma 16.4: Lapse/Shift Sources Are Hypersurface-Comparison Data, Not
Residual Value Data

For every lapse/shift source in \({\mathcal G}_{cur}\), the sourced part is
contained in finite hypersurface comparison, exchange-curvature, endpoint, and
clean transport data.  It does not by itself print a covariance with
\(R\Sigma\).

Proof.

The older relativistic ISP and metric-data papers use lapse/shift variations
to test hypersurface-deformation compatibility and possible metric
coefficients.  Those tests are about finite comparison maps and exchange
defects.  They are valuable, but they do not supply the V3 live scalar
entries \(m,t\) or a same-law derivative of the actual adaptive residual
Hamiltonian.  Treating lapse/shift as an infinitesimal Markov generator would
also violate the Barandes alignment rule.  `square`

### Lemma 16.5: Cell Volume And Boundary Shape Reduce To The Residual Score
Table

For every cell-volume/boundary-shape source in \({\mathcal G}_{cur}\), the
only possible non-clean contribution to the scalar coupling is
\(C_{V\partial}^{res}\) from Definition 11.3.

Proof.

This is Theorem 11.4 specialized to the licensed source class.  Volume and
boundary changes alter clean local normalizations and heat weights unless
they differentiate the actual residual conditional Hamiltonian.  After the
clean and null projections are removed, only the residual score table remains.
`square`

## 17. The Residual-Hamiltonian Derivative Gate

The previous section shows that all natural geometric sources pass through
one narrow bottleneck.

### Definition 17.1: `V4P1-GEO-RHAM-DER`

Write

$$
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}
$$

if there exists a licensed finite geometric source direction \(\eta_a\) and a
finite same-law observable \(L_a^{RPF}\) such that

$$
\partial_{\eta_a}H_{RPF}^{loc}\big|_0
=
L_a^{RPF}
+L_a^{clean}
+L_a^{null},
$$

where \(L_a^{clean}\) lies in the clean span and \(L_a^{null}\) is charged by
the quotient ledger.

The residual geometric score is then

$$
S_a^{res}
=
-L_a^{RPF}
+\mathbf E_{\mu_0}[L_a^{RPF}].
$$

### Definition 17.2: `V4P1-GEO-RHAM-COUPLE`

Write

$$
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}
(\varepsilon,\sigma,M)
$$

if there are two geometric source directions \(a,b\) satisfying
`V4P1-GEO-RHAM-DER` and the \(2\times2\) table

$$
C_{ab}^{RPF}
=
\begin{pmatrix}
\operatorname{Cov}(X_m,S_a^{res})&
\operatorname{Cov}(X_m,S_b^{res})\\
\operatorname{Cov}(X_t,S_a^{res})&
\operatorname{Cov}(X_t,S_b^{res})
\end{pmatrix}
$$

recovers the scalar pair in the same sense as Definition 11.5, with usable
singular value at least \(\sigma\) and score envelope at most \(M\).

### Theorem 17.3: Residual-Hamiltonian Derivative Is Necessary For Current
Geometric Coupling

Within \({\mathcal G}_{cur}\), the positive gate
`V4P1-GEO-RSIGMA-COUPLE` can hold only through
`V4P1-GEO-RHAM-COUPLE`, up to the already charged clean and null rows.

Proof.

Lemmas 16.2 through 16.5 exhaust the natural current-corpus geometric knobs.
Each one decomposes into clean, null, and residual-Hamiltonian derivative
parts.  Clean and null parts are ray-blind by Theorem 5.2 and the quotient
ledger.  Hence any ray-cutting covariance with \(R\Sigma\) must come from the
residual-Hamiltonian derivative part.  Definition 17.2 is exactly the
two-direction coupling theorem for that part.  `square`

## 18. Current-Corpus Evaluation Of `V4P1-GEO-RHAM-DER`

### Proposition 18.1: The Current Corpus Does Not Print `V4P1-GEO-RHAM-DER`

The current V2/V3 corpus does not prove
`V4P1-GEO-RHAM-DER`.

Proof.

Papers 26 through 30 repeatedly identify \(H_{RPF}\), residual atoms, residual
scores, primitive residual values, RN-MIXAMP ratios, and bridge residual
terms as the actual-law value objects.  Paper 30 even rewrites several
obstructions as pairings against the residual score \(S^{RPF}\).  But the
corpus does not print a finite same-law derivative of
\(H_{RPF}^{loc}\) with respect to cell volume, boundary shape, area, frame,
lapse, shift, edge length, or tetrad.  It also does not print the resulting
observable \(L_a^{RPF}\) after clean/null quotienting.  Therefore the
premise of Definition 17.1 is absent.  `square`

### Proposition 18.2: The Current Corpus Does Not Print
`V4P1-GEO-RHAM-COUPLE`

The current V2/V3 corpus does not prove
`V4P1-GEO-RHAM-COUPLE(epsilon,sigma,M)` in any closing range.

Proof.

By Proposition 18.1, the residual geometric scores \(S_a^{res}\) are not
populated.  Without those scores, the covariance matrix \(C_{ab}^{RPF}\) is
not populated.  Without that matrix, no singular value, reconstruction
matrix, score envelope, or scalar-ray trace can be certified.  `square`

### Corollary 18.3: Candidate A/B/C Status

The three candidate pairs from Section 10 have the following status.

| Candidate | Clean part | Residual part | Verdict |
| --- | --- | --- | --- |
| Area/shape | heat time plus recoupling | needs `V4P1-GEO-RHAM-DER` | not coupled by current corpus |
| Lapse/shift | hypersurface comparison/exchange data | needs `V4P1-GEO-RHAM-DER` without Markovizing | not coupled by current corpus |
| Cell volume/boundary shape | normalizer plus heat/channel rows | needs `V4P1-CELLBOUND-RSCORE`, hence `V4P1-GEO-RHAM-DER` | not coupled by current corpus |

## 19. The Current-Corpus No-Go

### Definition 19.1: `V4P1-GEO-CUR-NOGO`

Write

$$
\mathrm{V4P1\text{-}GEO\text{-}CUR\text{-}NOGO}
$$

if every source in \({\mathcal G}_{cur}\) has only clean and null sourced
components after removing unsourced residual-Hamiltonian derivative symbols.

### Theorem 19.2: Current-Corpus Geometric Sources Do Not Couple To \(R\Sigma\)

The current corpus proves

$$
\mathrm{V4P1\text{-}GEO\text{-}CUR\text{-}NOGO}.
$$

Consequently it does not prove

$$
\mathrm{V4P1\text{-}GEO\text{-}RSIGMA\text{-}COUPLE}
(\varepsilon,\sigma,M)
$$

for any closing range.

Proof.

For all current-corpus licensed geometric sources, Lemmas 16.2 through 16.5
show that the sourced pieces are clean or null unless
`V4P1-GEO-RHAM-DER` is supplied.  Proposition 18.1 shows that this derivative
is not supplied.  Therefore the only sourced geometric score components are
clean or null.  Clean components are scalar-ray blind by Theorem 5.2, and
null components are removed by the quotient ledger.  Thus no sourced
current-corpus geometric response couples to \(R\Sigma\) in the sense needed
by Definition 2.3.  `square`

### Corollary 19.3: This Is Not A Global Mathematical No-Go

Theorem 19.2 does not prove that every possible future geometry-coupled ISP
law is ray-blind.

It proves only the current-corpus statement:

$$
\hbox{existing finite geometric data do not source the needed residual
Hamiltonian derivative.}
$$

A future positive theorem would have to add precisely
`V4P1-GEO-RHAM-DER` and `V4P1-GEO-RHAM-COUPLE`.

## 20. Final Paper-1 Settlement

### Theorem 20.1: V4 Paper 1 Settles The First Geometry Pivot

V4 Paper 1 settles the question

$$
\hbox{does finite geometric source response couple to }R\Sigma?
$$

as follows.

1. For the finite geometric sources licensed by the current V2/V3 corpus, the
   answer is no.
2. The no is not because geometry is philosophically irrelevant.  It is
   because all sourced geometric score components are clean or null.
3. The only possible non-clean route is a finite derivative of the actual
   residual conditional Hamiltonian with respect to geometric data.
4. That route is exactly

   $$
   \mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}
   \quad+\quad
   \mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}.
   $$

5. The current corpus proves neither of those two gates.

Proof.

Items 1 and 2 are Theorem 19.2.  Item 3 is Theorem 17.3.  Item 4 is
Definitions 17.1 and 17.2.  Item 5 is Propositions 18.1 and 18.2.  `square`

### Corollary 20.2: V4 Paper 2 Is Not Yet Licensed

V4 Paper 2, the geometric Gram/Fisher paper, should not start as if Paper 1
had passed.  A Gram matrix is meaningful only after the source observables
exist and couple to the live scalar object.

The next legitimate move is not geometric Gram.  It is one of:

1. prove `V4P1-GEO-RHAM-DER` for a concrete finite geometric deformation;
2. prove `V4P1-GEO-RHAM-COUPLE` once the derivative is printed;
3. prove a stronger clean-factorization theorem for a broader source class;
4. leave the geometry pivot and return to a different same-law value source.

### Final Verdict 20.3

V4 Paper 1 does not unlock the V3 obstruction.  It does something useful and
protective: it prevents the project from pretending that "geometry" is a
source just because geometry words have been introduced.

The geometric route remains alive only as a new primitive residual-Hamiltonian
geometry theorem:

$$
\boxed{
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}
\quad+\quad
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}.
}
$$

Without that theorem, finite geometric source response is ray-blind at the
current-corpus level.

## 21. Scoped Truth Status Of The Residual-Hamiltonian Gates

The user-facing question is now sharper:

$$
\hbox{prove or falsify }
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}
\hbox{ and }
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}.
$$

This question needs a scope.  Without a source class, the statement is too
loose: one can always introduce an artificial source tilt that couples to any
chosen observable.  Such a tilt would not be a geometric theorem.

### Definition 21.1: Current-Corpus Scoped Derivative Gate

Write

$$
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}^{cur}
$$

if `V4P1-GEO-RHAM-DER` holds with \(\eta_a\in{\mathcal G}_{cur}\), where
\({\mathcal G}_{cur}\) is Definition 16.1.

Equivalently, the derivative

$$
\partial_{\eta_a}H_{RPF}^{loc}\big|_0
$$

must be printed by the current corpus as a finite same-law observable after
clean and null quotienting.

### Definition 21.2: Current-Corpus Scoped Coupling Gate

Write

$$
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}^{cur}
(\varepsilon,\sigma,M)
$$

if `V4P1-GEO-RHAM-COUPLE(epsilon,sigma,M)` holds using two directions from
\({\mathcal G}_{cur}\).

### Theorem 21.3: `V4P1-GEO-RHAM-DER^cur` Is False

The current corpus proves

$$
\neg
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}^{cur}.
$$

Proof.

By Definition 16.1, a current-corpus licensed geometric source may
differentiate a residual Hamiltonian term only where the corpus prints that
derivative as a finite same-law observable.  Proposition 18.1 audits the
corpus and shows that no such derivative is printed for cell volume, boundary
shape, area, frame, lapse, shift, edge length, or tetrad.  Therefore there
exists no \(\eta_a\in{\mathcal G}_{cur}\) and no finite same-law observable
\(L_a^{RPF}\) satisfying Definition 17.1.  That is exactly the negation of
Definition 21.1.  `square`

### Corollary 21.4: `V4P1-GEO-RHAM-COUPLE^cur` Is False

For every closing range \((\varepsilon,\sigma,M)\) with \(\sigma>0\),

$$
\neg
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}^{cur}
(\varepsilon,\sigma,M).
$$

Proof.

Definition 21.2 requires two directions satisfying
`V4P1-GEO-RHAM-DER^cur`.  Theorem 21.3 proves that no such direction exists.
Thus the residual score table \(C_{ab}^{RPF}\) cannot be formed from
current-corpus licensed geometric sources, and a positive singular-value
coupling table cannot exist in \({\mathcal G}_{cur}\).  `square`

### Corollary 21.5: The Current Geometry Pivot Is Falsified

The V4 Paper-1 geometry pivot, restricted to source directions actually
licensed by the current corpus, is falsified:

$$
\neg
\left[
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}^{cur}
\quad+\quad
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}^{cur}
\right].
$$

This is stronger than "not sourced."  It says the current source class itself
does not contain the needed residual-Hamiltonian derivative.

## 22. Why The Unscoped Positive Gate Would Be Vacuous

The previous falsification is deliberately scoped.  This section explains why
the unscoped version should not be treated as a theorem target.

### Lemma 22.1: Arbitrary Tilts Can Fake The Derivative Gate

Let \(Y\) be any finite same-law observable on the base record space.  Define
a formal one-parameter family by

$$
{d\mu_\eta\over d\mu_0}
=
{1\over Z_\eta}\exp(\eta Y).
$$

Then the source score at zero is

$$
S_\eta=Y-\mathbf E_{\mu_0}[Y].
$$

Thus, if arbitrary tilts are allowed to count as "geometric", one can choose
\(Y\) to be any desired residual observable and force a fake version of
`V4P1-GEO-RHAM-DER`.

Proof.

Differentiate the finite Radon-Nikodym derivative at \(\eta=0\).  The
normalizer subtracts the expectation.  `square`

### Lemma 22.2: Arbitrary Two-Knob Tilts Can Fake Coupling

If arbitrary tilts are allowed, choose \(Y_1,Y_2\) with nondegenerate
covariance against the scalar readouts \(X_m,X_t\).  Then the formal source
coupling matrix can be made nondegenerate by construction.

Proof.

The coupling matrix is

$$
\begin{pmatrix}
\operatorname{Cov}(X_m,Y_1)&\operatorname{Cov}(X_m,Y_2)\\
\operatorname{Cov}(X_t,Y_1)&\operatorname{Cov}(X_t,Y_2)
\end{pmatrix}
$$

after centering.  Taking \(Y_1=X_m\) and \(Y_2=X_t\), for example, gives the
covariance matrix of \((X_m,X_t)\), whenever that covariance is nondegenerate.
Even when that particular choice degenerates, a formal enlargement can choose
tilts adapted to the desired two-dimensional quotient.  This is not a
geometric theorem; it is source smuggling.  `square`

### Proposition 22.3: The Unscoped Gates Are Not Honest Proof Targets

The bare statements

$$
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}
\quad\hbox{and}\quad
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}
$$

are not honest theorem targets unless the admissible geometric source class is
declared.

Proof.

If the source class is unrestricted, Lemmas 22.1 and 22.2 show that arbitrary
tilts can force the desired derivative and coupling.  If the source class is
restricted to \({\mathcal G}_{cur}\), Theorem 21.3 and Corollary 21.4 falsify
the gates.  Therefore the only meaningful future version must define a new
finite geometry-coupled law and prove that its source is geometric rather
than an arbitrary residual tilt.  `square`

## 23. Final Truth-Status Table

| Gate | Scope | Truth status | Reason |
| --- | --- | --- | --- |
| `V4P1-GEO-RHAM-DER` | current corpus \({\mathcal G}_{cur}\) | false | no printed finite derivative of \(H_{RPF}^{loc}\) with respect to licensed geometric data |
| `V4P1-GEO-RHAM-COUPLE` | current corpus \({\mathcal G}_{cur}\) | false | coupling requires two derivative directions, but none exists |
| `V4P1-GEO-RHAM-DER` | unrestricted source tilts | vacuous/ill-posed | arbitrary tilts can manufacture a score |
| `V4P1-GEO-RHAM-COUPLE` | unrestricted source tilts | vacuous/ill-posed | arbitrary two-knob tilts can manufacture coupling |
| `V4P1-GEO-RHAM-DER + COUPLE` | future declared geometry-coupled law | open | must prove a genuine residual-Hamiltonian geometric derivative and nondegenerate same-law covariance table |

### Final Verdict 23.1

Both gates are settled as follows:

$$
\boxed{
\neg
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}DER}^{cur}
\quad\hbox{and}\quad
\neg
\mathrm{V4P1\text{-}GEO\text{-}RHAM\text{-}COUPLE}^{cur}.
}
$$

The current V4 geometry idea is therefore falsified as a current-corpus proof
route.  It is not globally dead as a future research direction, but any future
revival must introduce a genuinely new finite geometry-coupled residual law,
not just new geometry words or arbitrary source tilts.
