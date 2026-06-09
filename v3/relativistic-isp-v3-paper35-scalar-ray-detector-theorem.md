# Relativistic ISP V3 Paper 35: Scalar-Ray Detector Theorem

Author: Felix Robles Elvira

Date: 2026-05-26

## Abstract

Papers 33 and 34 isolate the current live obstruction in its simplest form.
The actual same-law signed/residual two-channel block

$$
B_{\Gamma_1}^{N,j}
=
R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}
$$

may lie on the scalar ray

$$
B(c)=cI_2.
$$

Along this ray,

$$
m=c(h_0+h_A),
\qquad
t=ca_N(h_0-h_A),
$$

and the current finite structural, positivity, gauge, selector, source,
and passive reflection-positive constraints do not bound \(c\) below the
retention envelope and do not orient its sign.

This paper develops the scalar-ray detector theorem.  It gives a test for
any proposed future Branch-A constraint: restrict the constraint to the
deterministic scalar-ray laws \(\nu_c\).  If every allowed \(c\) still
survives, the constraint is ray-blind.  If the surviving set of \(c\)'s is
strictly smaller, the constraint is ray-cutting.  If it forces a sign with
enough magnitude, it is ray-orienting and gives a floor route.

The main result is a current-corpus classification.  All passive finite
structures already tried are ray-blind: finite label refinements, ordinary
moment positivity, passive RP/SOS positivity, gauge covariance, recoupling,
heat-diagonal identities, selector relabelings, and source-response
reparametrizations without a bound.  A constraint can move adaptive Branch A
only if its scalar-ray trace contains one of the following non-passive
ingredients:

1. a same-law upper value or score-energy inequality forcing \(|c|\) small;
2. a non-gauge Ward/Stein identity giving \(Ac=\hbox{small defect}\);
3. a structural coupling theorem that realizes the source on \(R\Sigma\);
4. a non-passive reflection theorem, such as upper moment or oddness;
5. an RN block derivative or residual Jacobian theorem with scalar rank;
6. a sign-coherent lower-floor orientation.

Thus Paper 35 does not prove confinement.  It proves something narrower and
useful: from now on a proposed route must pass the scalar-ray detector test
before it deserves a new paper.

## 0. Imports And Notation

### Import 0.1: The Live Scalar Ray

From Paper 33, the scalar-ray laws are deterministic laws \(\nu_c\) supported
on

$$
B(c)=cI_2,
\qquad
|c|\le M_\beta.
$$

They give

$$
m(c)=c(h_0+h_A),
$$

$$
t(c)=ca_N(h_0-h_A),
$$

and

$$
\lambda_+(c)={m(c)+t(c)\over2},
\qquad
\lambda_-(c)={m(c)-t(c)\over2}.
$$

### Import 0.2: Passive RP Completion

From Paper 34, every passive finite reflection-positive moment worksheet
admits an extension of \(\nu_c\).  The RP and ordinary moment matrices are
rank-one positive semidefinite matrices.

### Import 0.3: Barandes Rule

Every constraint in this paper is a constraint on the same finite record
law.  A detector may use representation coordinates, moments, RP matrices,
or source derivatives only as finite functions or derivatives of finite
functions under that law.  It may not insert a hidden Markov factorization,
an off-law comparison measure, or a new physical dynamics.

## 1. Ray Traces

### Definition 1.1: Scalar-Ray Trace Of A Constraint

Let \({\mathcal C}\) be any proposed finite Branch-A constraint package.
Its scalar-ray trace is

$$
\operatorname{Tr}_{ray}({\mathcal C})
:=
\{c\in[-M_\beta,M_\beta]:\nu_c\hbox{ admits an extension satisfying }
{\mathcal C}\}.
$$

The extension clause allows \({\mathcal C}\) to introduce finitely many new
record functions, moments, source columns, or representation coordinates, as
long as they are evaluated under the same law and satisfy the declared
finite identities.

### Definition 1.2: Ray-Blind, Ray-Cutting, Ray-Killing, Ray-Orienting

The package \({\mathcal C}\) is:

1. **ray-blind** if

   $$
   \operatorname{Tr}_{ray}({\mathcal C})=[-M_\beta,M_\beta];
   $$

2. **ray-cutting** if its trace is a proper subset of the allowed interval;
3. **ray-killing** if its trace is \(\{0\}\), or is contained in a
   non-closing neighborhood of \(0\);
4. **ray-orienting** if its trace lies in one sign sector and yields a
   sign-coherent lower floor for one of \(m,t,\lambda_+,\lambda_-\).

### Definition 1.3: Useful Detector

The package \({\mathcal C}\) is a useful scalar-ray detector if it proves one
of:

$$
\max\{|\mathbf E m|,|\mathbf E t|\}\le B_{rem}
$$

with \(B_{rem}\) below the Branch-A scalar budget, or

$$
\mathbf E F\ge M_*
$$

for an allowed floor functional \(F\in\{m,t,\lambda_+,\lambda_-\}\) with the
correct sign and magnitude.

## 2. Universal Ray-Blindness Criterion

### Definition 2.1: Passive Deterministic-Character Constraint

A constraint package \({\mathcal C}\) is passive deterministic-character
compatible if every new object it adds is one of:

1. a finite record function with a declared scalar-compatible value on
   \(B=cI_2\);
2. an affine identity already satisfied by scalar intertwiners;
3. an ordinary moment matrix of finite record functions;
4. an RP moment matrix whose reflection fixes scalar intertwiners;
5. a finite source or representation coordinate whose value is not bounded
   or oriented by a new inequality.

### Lemma 2.2: Deterministic Characters Pass Passive Constraints

If \({\mathcal C}\) is passive deterministic-character compatible, then
every scalar-ray law \(\nu_c\) extends to a law satisfying \({\mathcal C}\).

Proof.

Assign each added record function its declared scalar-compatible value at
the deterministic record \(B=cI_2\).  Products are evaluated
multiplicatively.  Affine scalar identities hold by assumption.  Ordinary
moment matrices are outer products \(vv^T\).  RP moment matrices are also
outer products, because the passive reflection fixes the scalar-intertwiner
values.  Source and representation coordinates without new bounds merely
record additional finite numbers.  Therefore all passive constraints hold.
`square`

### Theorem 2.3: Passive Deterministic-Character Constraints Are Ray-Blind

Every passive deterministic-character compatible package is ray-blind.

Proof.

By Lemma 2.2, every \(c\in[-M_\beta,M_\beta]\) survives.  This is exactly
Definition 1.2.  `square`

### Corollary 2.4: More Finite Labels Are Ray-Blind Unless They Carry Values

Adding finite labels, channels, selector names, low-mode names, or
Peter-Weyl names is ray-blind unless the added labels come with a new
same-law inequality, sign rule, or value theorem whose scalar-ray trace is
proper.

Proof.

Labels without values are finite coordinates on the same deterministic
record.  They fall under Definition 2.1.  `square`

## 3. Current-Corpus Ray-Blind Classes

### Proposition 3.1: Gauge And Recoupling Constraints Are Ray-Blind

Gauge covariance, scalar-channel compatibility, and the printed recoupling
identities are ray-blind.

Proof.

The scalar ray \(B=cI_2\) is an intertwiner.  It commutes with the retained
two-channel recoupling algebra and satisfies all scalar affine identities
from Paper 33.  Theorem 2.3 applies.  `square`

### Proposition 3.2: Ordinary Moment Positivity Is Ray-Blind

Ordinary finite moment positivity is ray-blind.

Proof.

Under \(\nu_c\), every finite moment matrix is a Gram matrix of deterministic
values, hence an outer product.  It is positive semidefinite for all \(c\).
`square`

### Proposition 3.3: Passive Reflection Positivity Is Ray-Blind

Passive RP/SOS positivity is ray-blind.

Proof.

This is Paper 34, Theorem 3.4 and Corollary 3.6.  In the present language,
passive RP is a deterministic-character compatible constraint.  `square`

### Proposition 3.4: Heat-Diagonal Data Are Ray-Blind

The retained heat-kernel diagonal entries \(h_0,h_A\) do not cut the scalar
ray by themselves.

Proof.

The heat entries determine the linear readout

$$
m=c(h_0+h_A),
\qquad
t=ca_N(h_0-h_A),
$$

but they do not constrain \(c\).  They convert the unknown amplitude into
the live scalars; they do not bound the amplitude.  `square`

### Proposition 3.5: Selector Relabeling Is Ray-Blind

Selector relabelings and canonical-label refinements are ray-blind unless
they produce an actual-law value bound, boundary-flux bound, or orientation.

Proof.

A relabeling of a deterministic scalar-intertwiner record is still a
deterministic scalar-intertwiner record.  The trace in \(c\) is unchanged.
If the selector creates a value-bearing boundary flux or sign orientation,
that is no longer passive relabeling; it is a new same-law theorem.  `square`

### Proposition 3.6: Source Reparametrization Without Bounds Is Ray-Blind

Writing a live value as a source derivative is ray-blind unless one also
proves source neutrality, curvature, Ward cancellation, tail decay, or a
floor.

Proof.

Paper 31 proves that a source derivative is an exact representation of an
actual value.  It does not make the derivative small.  Along the scalar ray,
the derivative is simply a linear function of \(c\).  Without a new
inequality or sign rule on that derivative, all \(c\)'s survive.  `square`

## 4. Ray-Cutting Mechanisms

A useful positive theorem must make
\(\operatorname{Tr}_{ray}({\mathcal C})\) small enough.  This section gives
the exact forms visible in the current corpus.

### Mechanism A: Upper Amplitude Bound

Suppose a same-law theorem proves

$$
|c|\le C_c
$$

cofinally.  Then

$$
\max\{|m|,|t|\}
\le
C_c
\max\{|h_0+h_A|,\ |a_N(h_0-h_A)|\}.
$$

This cuts the ray if the right side is below the Branch-A budget.

The actual candidates are:

1. direct signed/residual smallness;
2. residual score energy;
3. residual Hessian or normalizer variance control;
4. non-passive RP upper moment;
5. Peter-Weyl tail plus low-mode value control.

### Mechanism B: Ward/Stein Linear Equation

Suppose a non-gauge Ward/Stein identity gives

$$
Ac=D+\epsilon,
$$

where \(A\ne0\), \(D\) is a licensed small defect, and \(\epsilon\) is a
controlled residual score error.  Then

$$
|c|\le {|D|+|\epsilon|\over |A|}.
$$

This cuts the ray when the right side is below the scalar budget after
multiplication by the heat readout constants.

The current corpus does not print such a non-gauge Ward/Stein identity with
small defect.  Pure gauge/Haar Ward identities have \(A=0\) on the scalar
ray.

### Mechanism C: Structural Coupling And Gram

Suppose the structural source columns are realized on the actual
residual/signed product, and the resulting two-column covariance matrix has
determinant at least \(\sigma>0\).  Then the scalar route can solve for the
live direction rather than leaving \(c\) arbitrary.

This is the Paper-32/Paper-33 target

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM}.
$$

It is ray-cutting only if the coupling is to \(R\Sigma\), not merely to the
clean heat channel.

### Mechanism D: Non-Passive Reflection

Reflection positivity cuts the ray only if it adds one of:

$$
\mathrm{P34\text{-}RP\text{-}UPMOM},
\qquad
\mathrm{P34\text{-}RP\text{-}ODD},
\qquad
\mathrm{P34\text{-}RP\text{-}SCHUR}.
$$

Passive RP positivity is ray-blind.  A useful RP theorem must either bound a
live diagonal, make the live scalar odd under reflection, or tie the live
scalar to a licensed small diagonal by a Schur complement.

### Mechanism E: RN Block Derivative Or Residual Jacobian Rank

If an RN block derivative theorem proves that the live scalar direction is
in the image of a same-law residual/selector derivative map with controlled
score defect, then the scalar route closes.

In scalar-ray form, this again becomes a linear detector:

$$
J_{res}v_c=\hbox{controlled row}.
$$

The route cuts the ray only if the residual Jacobian has nonzero projection
onto \(I_2\) and the score defect is bounded.

### Mechanism F: Sign-Coherent Floor

If a same-law theorem proves, for some \(F\in\{m,t,\lambda_+,\lambda_-\}\),

$$
s_F\mathbf E[F]\ge M_*,
$$

with the sign \(s_F\in\{-1,1\}\) fixed cofinally and \(M_*\) above the
Branch-A lower-floor threshold, then the scalar ray is not cut positively;
it is oriented into a negative/floor exit.

## 5. Detector Completeness For The Current Scalar Branch

### Theorem 5.1: Current-Corpus Detector Dichotomy

For every Branch-A scalar constraint package discussed in Papers 30 through
34, exactly one of the following holds:

1. it is ray-blind by Theorem 2.3; or
2. it contains one of Mechanisms A through F; or
3. it is merely a reformulation of a value already covered by Mechanisms A
   through F.

Proof.

Papers 30 through 34 reduce the live obstruction to the two scalar responses
\(m,t\) of \(B=R\Sigma\).  Paper 33 lists the active constraints:
residual score-defect, structural coupling plus Gram, non-gauge Ward/Stein,
reflection-positive upper moment, RN block derivative, and floor.  Paper 34
splits the reflection route into upper moment, oddness, Schur complement,
structural coupling, and floor.  The passive structures eliminated in
Papers 33 and 34 are exactly the deterministic-character compatible
structures of Section 3.  Therefore every current route is either passive
and ray-blind, or non-passive and contained in Mechanisms A through F.
`square`

### Corollary 5.2: Proposed Future Theorem Test

Before opening a new Branch-A paper, restrict the proposed theorem to the
scalar ray.  If its trace remains

$$
[-M_\beta,M_\beta],
$$

then it cannot move the current obstruction.  If it cuts or orients the
trace, the theorem is a legitimate next target.

### Corollary 5.3: Why The Scalar Ray Is The Right Diagnostic

The scalar ray is not claimed to be the actual Yang-Mills law.  It is the
minimal witness that the current constraints do not determine the actual
law.  Any proof that cannot exclude or orient this witness has not used the
missing same-law information.

## 6. Ranking The Remaining Detectors

The detector theorem also ranks the remaining work.

### Rank 1: Non-Gauge Ward/Stein Detector

The most promising positive route is a non-gauge Ward/Stein identity with a
nonzero scalar coefficient \(A\) and a controlled score defect:

$$
Ac=D+\epsilon.
$$

Reason: it would turn the unknown amplitude \(c\) into a constrained
response, without needing a full conditional transition table.

### Rank 2: Sign-Coherent Floor Detector

The most promising negative route is a sign-coherent floor for one of
\(m,t,\lambda_+,\lambda_-\).

Reason: if the ray cannot be cut, orienting it may falsify adaptive Branch A
cleanly.

### Rank 3: Structural Coupling To \(R\Sigma\)

Structural coupling plus Gram remains compact and elegant, but only if the
coupling is proved for the actual residual/signed product, not the clean
heat channel.

### Rank 4: Residual Score Energy Or Hessian

This route is exact and already reduced in Paper 33, but it is closest to
the original actual-law value problem: it asks for residual score energy,
residual Hessian, selector curvature, and normalizer variance.

### Rank 5: Non-Passive RP Theorem

Paper 34 closes passive RP.  Non-passive RP upper moment or oddness remains
valid, but it needs a concrete actual-law mechanism.

## 7. Paper-35 Verdict

### Theorem 7.1: Scalar-Ray Detector Theorem

The current adaptive Branch-A scalar obstruction can be moved only by a
constraint whose scalar-ray trace either:

1. bounds \(|c|\) below the Branch-A budget after heat readout;
2. forces \(c=0\) or a non-closing neighborhood of \(0\);
3. gives a nonzero Ward/Stein or residual-Jacobian equation for \(c\) with
   controlled defect;
4. realizes structural coupling to \(R\Sigma\) with a positive Gram
   determinant;
5. supplies a non-passive RP upper-moment, oddness, or Schur-small-diagonal
   theorem;
6. orients \(c\) into a sign-coherent lower floor.

All passive current-corpus structures are ray-blind.

Proof.

The ray-blind statement is Theorem 2.3 and Section 3.  The positive and
negative moving mechanisms are Mechanisms A through F.  Completeness for the
current corpus is Theorem 5.1.  `square`

### Corollary 7.2: No More Ray-Blind Work Packages

Further work on adaptive Branch A should not add labels, passive moment
matrices, passive RP matrices, or source reparametrizations unless they are
paired with a detector mechanism from Theorem 7.1.

### Corollary 7.3: Next Paper Recommendation

The next constructive paper should attack the Rank-1 detector:

$$
\mathrm{P35\text{-}NONGAUGE\text{-}WS\text{-}RAYCUT}(A,\epsilon).
$$

This theorem should seek an actual same-law Ward/Stein direction for which
the scalar ray has nonzero coefficient \(A\), while the residual/selector
score defect is bounded by \(\epsilon\).  If no such direction exists, the
same finite quotient should produce a dual floor candidate.
