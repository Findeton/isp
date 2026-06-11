# Relativistic ISP V3 Paper 33: Same-Law Bootstrap Of Live Scalars

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

## Abstract

Papers 30 through 32 reduce adaptive Branch A to actual same-law quantitative
information.  The latest Paper-32 endpoint is the minimal scalar obstruction:
the live singlet-adjoint block is compressed to two scalar responses \(m,t\),
with eigenchannel witnesses

$$
\lambda_+={m+t\over2},
\qquad
\lambda_-={m-t\over2}.
$$

Paper 32 also shows that structural source tomography would be the most
compact positive route:

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM}.
$$

This paper tries a different first-principles viewpoint.  Instead of asking
for the hidden actual values directly, form the convex set of all finite
same-record probability laws satisfying the already proved structural
constraints, positivity constraints, gauge/selector identities, Ward
relations, and heat-kernel marginal data.  The live values \(m,t\) are then
linear functionals on this law space.  A positive proof is a dual certificate
that every admissible law has small \(m,t\).  A negative proof is a dual
floor certificate.  If neither appears, the current constraints genuinely do
not determine the live value.

The first pass executes the minimal two-channel bootstrap.  It proves a
decisive current-corpus no-go: the present structural and positivity
constraints still contain the scalar ray

$$
B_{\Gamma_1}^{N,j}=cI_2,
$$

and therefore allow

$$
m=c(h_0+h_A),
\qquad
t=ca_N(h_0-h_A)
$$

through the full scalar range allowed by the envelope.  Positivity of finite
moments, gauge covariance, the printed recoupling matrix, the heat diagonal,
and the Paper-32 affine compression do not by themselves force either
smallness or a Gram determinant lower bound.  Thus the minimal bootstrap is
useful but non-closing: it proves that the next successful theorem must add
a genuinely new same-law constraint, such as a residual score inequality, a
same-law reflection-positive moment inequality involving \(R\Sigma\), a
non-gauge Ward/Stein identity, a structural coupling theorem, or a
sign-coherent floor.

## 0. Imports And Barandes Rule

### Import 0.1: Paper-32 Minimal Scalars

Paper 32, Lemma 59.1, proves that for the live singlet-adjoint block

$$
B_{\Gamma_1}^{N,j}
=
\begin{pmatrix}
\beta_{00}&\beta_{0A}\\
\beta_{A0}&\beta_{AA}
\end{pmatrix},
$$

one has

$$
\Pi_+^{U_N}
\left(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}\right)
=
{m\over2}I_2+{t\over2}U_N.
$$

Here

$$
m=h_0\beta_{00}+h_A\beta_{AA},
$$

and

$$
t
=
a_N(h_0\beta_{00}-h_A\beta_{AA})
+b_N(h_0\beta_{0A}+h_A\beta_{A0}).
$$

The real trace-norm debit is

$$
\max\{|m|,|t|\}.
$$

### Import 0.2: Paper-32 Structural Source Tomography

Paper 32 defines the structural two-knob source

$$
S_{\alpha,\zeta}
:=
\exp(\alpha I_2+\zeta U_N)
$$

and the conditional route

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM}.
$$

The first gate realizes the structural source on the actual adaptive law.
The second gives a positive covariance determinant for the two realized
structural observables.

### Import 0.3: Paper-31 Source Discipline

Paper 31 proves that a source is only a deterministic probe of the same
finite law:

$$
\Psi_V(s)=\log \mathbf E^{act}e^{sV}.
$$

All physical values are derivatives at \(s=0\).  The source parameter is not
a new physical dynamics, not a replacement measure, and not a Markov
transition.

### Barandes Rule 0.4

This paper follows the same rule.  The primitive object is a finite
same-record law.  Bootstrap variables are moments of actual record
functionals.  The bootstrap does not introduce a hidden Markov chain, a
comparison Yang-Mills measure, or an off-law heat dynamics.

## 1. The Law-Space Bootstrap Viewpoint

The current obstruction has a simple logical shape.  A finite record law
\(\mu_{N,j}\) exists, and \(m,t\) are finite observables under that law.  The
corpus does not know enough about \(\mu_{N,j}\) to evaluate them.

Instead of guessing the values, define the set of all laws compatible with
the constraints already printed by the corpus.  Then optimize \(m,t\) over
that set.

### Definition 1.1: Same-Law Bootstrap Space

Fix a cutoff \(L\) and a finite live record algebra
\({\mathcal A}_{boot}^{N,j,L}\).  Let

$$
{\mathfrak L}_{boot}^{N,j,L}
$$

be the set of probability laws \(\nu\) on the finite record alphabet
supporting \({\mathcal A}_{boot}^{N,j,L}\) such that:

1. \(\nu\ge0\) and \(\sum_x\nu(x)=1\);
2. all imported affine identities among printed observables hold;
3. all imported gauge, selector, recoupling, and heat-kernel structural
   identities hold;
4. all licensed Ward identities hold with their printed error terms;
5. all declared pointwise envelopes for retained observables hold;
6. all finite moment matrices requested in the worksheet are positive
   semidefinite.

The notation is deliberately conservative.  A law belongs to
\({\mathfrak L}_{boot}^{N,j,L}\) only if it is compatible with actual
finite-record data already licensed by the corpus.

### Definition 1.2: Bootstrap Bounds

For a live scalar functional \(F\), define

$$
U_{boot}(F)
:=
\sup_{\nu\in{\mathfrak L}_{boot}^{N,j,L}}
\left|\mathbf E_\nu F\right|,
$$

and for an oriented floor functional \(F\),

$$
L_{boot}(F)
:=
\inf_{\nu\in{\mathfrak L}_{boot}^{N,j,L}}
\mathbf E_\nu F.
$$

The bootstrap is useful if either:

1. \(U_{boot}(F)\) is below the Branch-A budget; or
2. \(L_{boot}(F)\) is above the lower-floor threshold with the correct sign.

### Definition 1.3: The Scalar Bootstrap Target

Write

$$
\mathrm{P33\text{-}LAWBOOT\text{-}SCAL}(B_{rem})
$$

if the bootstrap proves

$$
\sup_{\nu\in{\mathfrak L}_{boot}^{N,j,L}}
\max\{
|\mathbf E_\nu m|,
|\mathbf E_\nu t|
\}
\le B_{rem}
$$

cofinally, including all finite-cutoff and tail debits.

Write

$$
\mathrm{P33\text{-}LAWBOOT\text{-}FLOOR}(M_*)
$$

if the bootstrap proves a sign-coherent lower floor for one of

$$
m,\qquad t,\qquad \lambda_+,\qquad \lambda_-.
$$

## 2. Primal And Dual Certificates

At fixed cutoff, the bootstrap is finite-dimensional.  If the record alphabet
is finite, it is a linear program after the moment variables are expanded.
If one keeps moment matrices without expanding to atoms, it is a semidefinite
program.  Both forms have finite dual certificates.

### Definition 2.1: Bootstrap Certificate

A positive scalar bootstrap certificate is a finite identity

$$
B_{rem}^2-F^2
=
\sum_i a_i C_i
+\sum_k \langle P_k,M_k\rangle
+\sum_r s_r^2
+E_{tail},
$$

where:

1. \(C_i=0\) are licensed affine constraints;
2. \(M_k\succeq0\) are licensed moment matrices;
3. \(P_k\succeq0\) are dual positive matrices;
4. \(s_r^2\) are manifest squares;
5. \(E_{tail}\) is a licensed tail debit already below budget.

A floor certificate has the same form with \(F-M_*\) on the left and with a
sign orientation licensed by the Branch-A ledger.

### Theorem 2.2: Soundness Of Bootstrap Certificates

A positive bootstrap certificate for \(F\) implies
\(|\mathbf E_\nu F|\le B_{rem}\) for every
\(\nu\in{\mathfrak L}_{boot}^{N,j,L}\).  A floor certificate implies the
corresponding sign-coherent lower bound for every
\(\nu\in{\mathfrak L}_{boot}^{N,j,L}\).

Proof.

Evaluate the identity under any admissible law.  The affine terms vanish.
The moment terms are nonnegative by \(P_k\succeq0\) and \(M_k\succeq0\).  The
squares are nonnegative.  The tail term is already licensed.  Therefore
\(\mathbf E_\nu[F^2]\le B_{rem}^2\), and Cauchy-Schwarz gives
\(|\mathbf E_\nu F|\le B_{rem}\).  The floor version is the same dual
evaluation with oriented linear functional \(F-M_*\).  `square`

### Corollary 2.3: Branch-A Consequences

If `P33-LAWBOOT-SCAL(B_rem)` holds with \(B_{rem}\) below the scalar
heat-bad budget, then the scalar part of the Paper-32 heat-bad route closes.
If `P33-LAWBOOT-FLOOR(M_*)` holds above the Branch-A lower-floor threshold,
then adaptive Branch A is falsified along the corresponding floor route.

Proof.

This is exactly the Paper-32 scalar ledger: the live scalar debit is
\(\max\{|m|,|t|\}\), and the floor candidates are
\(m,t,\lambda_+,\lambda_-\).  `square`

## 3. Minimal Two-Channel Bootstrap

We now execute the smallest possible bootstrap: use only the two-channel
block variables already printed by Papers 30 and 32.

### Definition 3.1: Two-Channel Bootstrap Variables

Let

$$
\beta=(\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA})
$$

and retain the scalar functions

$$
m(\beta)=h_0\beta_{00}+h_A\beta_{AA},
$$

$$
t(\beta)
=
a_N(h_0\beta_{00}-h_A\beta_{AA})
+b_N(h_0\beta_{0A}+h_A\beta_{A0}).
$$

Let

$$
\lambda_+(\beta)={m(\beta)+t(\beta)\over2},
\qquad
\lambda_-(\beta)={m(\beta)-t(\beta)\over2}.
$$

For a scalar envelope \(M_\beta\), define the pointwise box

$$
|\beta_{ab}|\le M_\beta.
$$

The minimal two-channel bootstrap space
\({\mathfrak L}_{2ch}(M_\beta)\) consists of all finite probability laws on
this box satisfying the printed affine formulas above, gauge-scalar
compatibility, and positivity of all retained moment matrices.

### Remark 3.2: The Envelope Is Not A Value Theorem

The envelope \(M_\beta\) is only a crude pointwise retention bound.  If one
could prove \(M_\beta\) itself below the Branch-A budget, the problem would
already be solved by a direct same-law value theorem.  The question here is
whether positivity and structural constraints improve the bound.

## 4. The Scalar Ray

The first test is the scalar intertwiner ray

$$
B(c)=cI_2.
$$

This ray is gauge-scalar, \(U_N\)-compatible, and satisfies all printed
two-channel structural identities.  It is the smallest possible test of
whether the bootstrap has learned anything beyond the existing corpus.

### Lemma 4.1: The Scalar Ray Is Feasible

For every real \(c\) with \(|c|\le M_\beta\), the deterministic law
\(\nu_c\) supported on

$$
\beta_{00}=c,
\qquad
\beta_{AA}=c,
\qquad
\beta_{0A}=0,
\qquad
\beta_{A0}=0
$$

belongs to \({\mathfrak L}_{2ch}(M_\beta)\).

Proof.

The law is a positive probability measure.  The box envelope holds by
\(|c|\le M_\beta\).  All retained moment matrices are positive semidefinite
because they are Gram matrices of deterministic scalar values.  Gauge-scalar
compatibility holds because \(B(c)=cI_2\) is a scalar intertwiner.  The
Paper-32 affine formulas for \(m,t,\lambda_\pm\) are definitions on the
block variables and therefore hold identically.  No current-corpus
constraint rules out the scalar intertwiner coefficient \(c\).  `square`

### Lemma 4.2: Live Values Along The Scalar Ray

Along \(\nu_c\),

$$
m=c(h_0+h_A),
$$

and

$$
t=ca_N(h_0-h_A).
$$

Consequently

$$
\lambda_+
=
{c\over2}
\left[
h_0+h_A+a_N(h_0-h_A)
\right],
$$

and

$$
\lambda_-
=
{c\over2}
\left[
h_0+h_A-a_N(h_0-h_A)
\right].
$$

Proof.

Substitute \(\beta_{00}=\beta_{AA}=c\) and
\(\beta_{0A}=\beta_{A0}=0\) into Definition 3.1.  `square`

### Corollary 4.3: Minimal Positivity Does Not Bound \(m,t\)

The minimal two-channel bootstrap cannot prove
`P33-LAWBOOT-SCAL(B_rem)` for any

$$
B_{rem}
<
M_\beta
\max\{
|h_0+h_A|,
|a_N(h_0-h_A)|
\}.
$$

Proof.

Choose the sign of \(c\) and set \(|c|=M_\beta\).  Lemma 4.1 makes the law
feasible, and Lemma 4.2 gives the displayed lower range for the supremum of
\(\max\{|m|,|t|\}\).  `square`

### Corollary 4.4: Minimal Positivity Does Not Force A Gram Gap

The minimal two-channel bootstrap cannot prove a positive lower bound for
`P32-SCAL-STRUCTSRC-GRAM`.

Proof.

Under the deterministic law \(\nu_c\), every realized scalar structural
observable is constant.  Therefore its covariance matrix is zero.  Hence the
Gram determinant is zero for an admissible bootstrap law.  Positivity of
moment matrices gives upper consistency, not a positive covariance floor.
`square`

### Corollary 4.5: Minimal Positivity Does Not Force A Floor Either

The minimal two-channel bootstrap cannot prove a sign-coherent floor for
\(m,t,\lambda_+,\lambda_-\) without an additional orientation constraint.

Proof.

Both \(\nu_c\) and \(\nu_{-c}\) are feasible whenever \(\nu_c\) is feasible.
They have opposite signs for all four live scalar functionals.  Therefore no
sign-coherent lower floor follows from the symmetric minimal constraints.
`square`

## 5. Minimal Bootstrap Verdict

### Theorem 5.1: Minimal Two-Channel Bootstrap Is Non-Closing

The current-corpus two-channel law-space bootstrap proves neither:

$$
\mathrm{P33\text{-}LAWBOOT\text{-}SCAL}(B_{rem})
$$

in a closing range, nor

$$
\mathrm{P33\text{-}LAWBOOT\text{-}FLOOR}(M_*),
$$

nor

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM}(\sigma,M)
$$

with \(\sigma>0\).

Proof.

Corollary 4.3 rules out a nontrivial upper bound below the scalar envelope.
Corollary 4.4 rules out a universal positive Gram determinant.  Corollary
4.5 rules out a sign-coherent floor from the symmetric constraints.  `square`

### Corollary 5.2: What The No-Go Means

The no-go is not a proof that the actual Yang-Mills law has large \(m,t\).
It proves only that the already printed finite structural constraints do not
determine \(m,t\).  To move the bootstrap, one must add at least one genuinely
new same-law constraint involving the actual residual/signed product

$$
R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}.
$$

## 6. What Could Move The Bootstrap

The bootstrap viewpoint remains useful because it gives a concrete test for
new ideas.  A proposed theorem is useful only if it cuts off the scalar ray
or orients it into a floor.

### Candidate 6.1: Residual Score Inequality

A residual score inequality would add constraints of the form

$$
\left|
\mathbf E[F_{\ell_m}S_{\ell_m,new}]
\right|
+
\left|
\mathbf E[F_{\ell_t}S_{\ell_t,new}]
\right|
\le\delta.
$$

This is precisely `P32-SCAL-RESDEFECT(delta)`.  In bootstrap language it is
a new affine or quadratic constraint coupling \(m,t\) to the actual residual
score.

Status: valid target, not sourced by the current corpus.

### Candidate 6.2: Structural Coupling

The structural coupling theorem would assert that the clean two-knob source
actually differentiates the residual/signed product:

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}(\varepsilon).
$$

In bootstrap language, this adds two moment columns whose first derivatives
are \(m,t\).  Paired with a nonzero covariance determinant, it gives scalar
rank.

Status: valid target, not sourced by the current corpus.

### Candidate 6.3: Non-Gauge Ward/Stein Identity

Gauge Ward identities annihilate non-invariant directions but leave the
scalar ray \(B=cI_2\) untouched.  A useful Ward identity must act on residual
or selector coordinates and produce a score term that is small in the
Branch-A ledger.

Status: valid target, not sourced by the current corpus.

### Candidate 6.4: Reflection-Positive Moment Constraint

A new reflection-positive constraint involving the actual signed/residual
block could have the schematic form

$$
\mathbf E[
(\alpha m+\zeta t)^2
]
\le
C_{RP}
\mathbf E[\mathcal D_{licensed}],
$$

with \(C_{RP}\) below budget.  Unlike ordinary moment positivity, such an
upper inequality could cut off the scalar ray.

Status: plausible but absent from the printed reflection/selector corpus.

### Candidate 6.5: Sign-Coherent Orientation

If a new theorem oriented the scalar ray, for example forcing

$$
\mathbf E[m]\ge M_*
$$

or the corresponding statement for \(t,\lambda_+,\lambda_-\), then the same
bootstrap would become a floor certificate.

Status: valid negative route, not sourced by the current corpus.

## 7. The Correct Next Bootstrap Worksheet

The minimal two-channel bootstrap is closed negatively.  The next worksheet
should not add passive source labels.  It should add one active constraint at
a time and test whether that constraint cuts off the scalar ray.

### Definition 7.1: Active Constraint Ladder

The active bootstrap ladder is:

1. add the scalar residual score variables from `P32-SCAL-RESDEFECT`;
2. add the structural source covariance variables from
   `P32-SCAL-STRUCTSRC-GRAM`;
3. add the minimal RN-MIXAMP derivative rows from `P32-RN-BLKDER`;
4. add one Peter-Weyl tail shell only after a low-mode certificate exists;
5. add a sign-oriented floor functional if all positive cuts fail.

### Theorem 7.2: The Ladder Is Complete For The Current Scalar Branch

Every positive scalar route listed at the end of Paper 32 enters the
bootstrap ladder through one of the five active constraint types above.

Proof.

Paper 32 leaves exactly the following scalar gates: residual score-defect,
structural coupling plus Gram, RN block derivatives for the joint route,
same-law Peter-Weyl tail transfer, and sign-coherent floors.  These are the
five entries of Definition 7.1.  `square`

### Corollary 7.3: Paper-33 Live Target

The next live target is not a new reformulation.  It is one of the following
new constraints:

$$
\mathrm{P32\text{-}SCAL\text{-}RESDEFECT}(\delta),
$$

or

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM},
$$

or

$$
\mathrm{P32\text{-}RN\text{-}BLKDER}(L),
$$

or a sign-coherent floor.

The bootstrap has made the failure mode precise: any proposed theorem must
remove, constrain, or orient the scalar ray \(B=cI_2\).

## 8. Paper-33 Verdict

### Theorem 8.1: Same-Law Bootstrap Is Valid But Minimal Scalar Bootstrap
Does Not Close

The same-law law-space bootstrap is Barandes-aligned and sound.  At fixed
finite cutoff, positive and negative certificates are finite dual
certificates over actual record-law moments.  However, the minimal
two-channel bootstrap generated by the current corpus is non-closing: it
contains the scalar ray \(B=cI_2\), gives no useful upper bound below the
scalar envelope, gives no positive structural Gram determinant, and gives no
sign-coherent floor.

Proof.

Barandes alignment is Rule 0.4.  Certificate soundness is Theorem 2.2.
Minimal nonclosure is Theorem 5.1.  `square`

### Corollary 8.2: The Next Real Theorem

The next real theorem must be an active same-law constraint on the actual
residual/signed scalar ray.  The best-ranked positive choices are:

1. residual score smallness `P32-SCAL-RESDEFECT(delta)`;
2. structural source coupling plus Gram;
3. a non-gauge Ward/Stein identity that cuts the scalar ray;
4. a reflection-positive upper moment inequality involving \(R\Sigma\);
5. RN block derivatives if the joint route is prioritized.

The best-ranked negative choice is a sign-coherent floor for
\(m,t,\lambda_+,\lambda_-\).

Further passive finite labels, ordinary moment positivity, and gauge-scalar
constraints will not move the minimal scalar obstruction.

## 9. Score-Augmented Bootstrap

We now attack the first active constraint in Corollary 8.2:

$$
\mathrm{P32\text{-}SCAL\text{-}RESDEFECT}(\delta).
$$

Paper 32 already found the right Ward-Stein envelope.  The scalar observables
are exact derivatives in formal block-entry coordinates.  The question is
whether the law-space bootstrap can source the residual score term.

### Definition 9.1: Scalar Score Variables

Let

$$
V_m:=m,
\qquad
V_t:=t,
$$

and recall the Paper-32 quadratic Ward tests

$$
F_{\ell_m}:={V_m^2\over2\|\ell_m\|_2^2},
\qquad
F_{\ell_t}:={V_t^2\over2\|\ell_t\|_2^2}.
$$

Introduce score variables

$$
S_m:=S_{\ell_m,new},
\qquad
S_t:=S_{\ell_t,new},
$$

for the residual/selector part of the actual score after all licensed heat,
endpoint, retained-row, and tail pieces have been charged.

### Definition 9.2: Score-Augmented Bootstrap Space

Let

$$
{\mathfrak L}_{score}^{N,j,L}(M_\beta,I_m,I_t)
$$

be the minimal two-channel bootstrap space enlarged by the following
constraints:

1. the score variables \(S_m,S_t\) are finite record functions;
2. the scalar residual score energies obey

$$
\mathbf E[S_m^2]\le I_m,
\qquad
\mathbf E[S_t^2]\le I_t;
$$

3. the residual score contributions are the only unlicensed terms in the
   scalar Ward identities.

The score-energy bounds \(I_m,I_t\) are not assumed to be known.  They are
the candidate new same-law quantitative input.

### Definition 9.3: Scalar Score-Energy Source

Write

$$
\mathrm{P33\text{-}SCAL\text{-}SCOREENERGY}(I_m,I_t)
$$

if the actual adaptive law lies in
\({\mathfrak L}_{score}^{N,j,L}(M_\beta,I_m,I_t)\) cofinally with the printed
licensed debits.

This is stronger data than a formal Ward identity.  It is a quantitative
bound on the residual score itself.

## 10. Score Energy Sources Score Defect

### Lemma 10.1: Envelope Constants For The Ward Tests

On the box \(|\beta_{ab}|\le M_\beta\), define

$$
A_m(M_\beta)
:=
{M_\beta^2\|\ell_m\|_1^2\over2\|\ell_m\|_2^2},
\qquad
A_t(M_\beta)
:=
{M_\beta^2\|\ell_t\|_1^2\over2\|\ell_t\|_2^2}.
$$

Then

$$
|F_{\ell_m}|\le A_m(M_\beta),
\qquad
|F_{\ell_t}|\le A_t(M_\beta).
$$

Proof.

For any \(\ell\),

$$
|\ell\cdot\beta|\le M_\beta\|\ell\|_1.
$$

Substitute this into
\(F_\ell=(\ell\cdot\beta)^2/(2\|\ell\|_2^2)\).  `square`

### Theorem 10.2: Score Energy Implies `P32-SCAL-RESDEFECT`

If `P33-SCAL-SCOREENERGY(I_m,I_t)` holds, then

$$
\mathrm{P32\text{-}SCAL\text{-}RESDEFECT}(\delta_{score})
$$

holds with

$$
\delta_{score}
=
A_m(M_\beta)\sqrt{I_m}
+A_t(M_\beta)\sqrt{I_t}.
$$

Proof.

By Cauchy-Schwarz,

$$
\left|
\mathbf E[F_{\ell_m}S_m]
\right|
\le
\left(\mathbf E[F_{\ell_m}^2]\right)^{1/2}
\left(\mathbf E[S_m^2]\right)^{1/2}
\le
A_m(M_\beta)\sqrt{I_m}.
$$

The same estimate gives the \(t\)-term.  Sum the two estimates and compare
with Paper 32 Definition 116.2.  `square`

### Corollary 10.3: Positive Score-Energy Closure

If

$$
A_m(M_\beta)\sqrt{I_m}
+A_t(M_\beta)\sqrt{I_t}
<
B_{rem},
$$

where \(B_{rem}\) is the remaining scalar budget after licensed charges, then
the scalar residual-score route closes.

Proof.

Combine Theorem 10.2 with Paper 32 Proposition 116.3.  `square`

## 11. Ward Identities Without Score Energy Do Not Close

The preceding theorem shows exactly what would work.  We now check whether
the score-energy bound is avoidable.  It is not.

### Lemma 11.1: Two-Point Score Realization

Fix one scalar direction \(V=\ell\cdot\beta\) and its Ward test
\(F=V^2/(2\|\ell\|_2^2)\).  Suppose two admissible block points
\(\beta^+,\beta^-\) have

$$
F(\beta^+)\ne F(\beta^-).
$$

For any real number \(r\), there are score values \(S^+,S^-\) with

$$
{S^+ + S^-\over2}=0
$$

and

$$
{F(\beta^+)S^+ + F(\beta^-)S^-\over2}=r.
$$

Proof.

Set \(S^+=s\) and \(S^-=-s\).  Then the second displayed equation becomes

$$
{s\over2}\left(F(\beta^+)-F(\beta^-)\right)=r.
$$

Since the parenthesis is nonzero, choose

$$
s={2r\over F(\beta^+)-F(\beta^-)}.
$$

`square`

### Proposition 11.2: Ward Constraints Alone Leave Arbitrary Score Cost

Finite Ward identities and score centering, without a bound on
\(\mathbf E[S_m^2]\) and \(\mathbf E[S_t^2]\), do not imply a closing bound
on the scalar residual-score defect.

Proof.

Lemma 11.1 realizes any desired score pairing \(r\) by increasing the score
magnitude \(s\).  The construction preserves positivity of the two-point
law and score centering.  Its score energy grows like \(s^2\).  Therefore the
Ward identity alone trades the missing scalar value for an uncontrolled
score energy.  It does not bound the value.  `square`

### Corollary 11.3: The Scalar Ray Becomes A Score-Energy Ray

Adding formal Ward identities cuts off the literal deterministic scalar ray,
but it replaces it with nearby two-point score rays unless one also bounds
the residual score energy.

Proof.

A deterministic law with nonzero \(V\) and centered finite score cannot
satisfy \(V=\mathbf E[FS]\).  However, by perturbing the deterministic point
to two nearby admissible points with different \(F\)-values and choosing
large opposite scores, Lemma 11.1 realizes the same scalar pairing.  The
only price is score energy.  Without a score-energy constraint, that price is
not charged.  `square`

## 12. Current-Corpus Verdict On The Score Route

### Proposition 12.1: Score Energy Is Not Printed

The current corpus does not prove
`P33-SCAL-SCOREENERGY(I_m,I_t)` with

$$
A_m(M_\beta)\sqrt{I_m}
+A_t(M_\beta)\sqrt{I_t}
<
B_{rem}.
$$

Proof.

Paper 32 Proposition 116.4 already audits the expectations
\(\mathbf E[F_{\ell_m}S_{\ell_m,new}]\) and
\(\mathbf E[F_{\ell_t}S_{\ell_t,new}]\).  A score-energy theorem is
stronger: it asks for second moments of the same residual/selector score
terms.  Papers 29 through 32 identify residual Hamiltonian, Jacobian,
selector, normalizer, multiplier, and score-regularity terms, but they do not
print cofinal \(L^2\) bounds for \(S_{\ell_m,new}\) and \(S_{\ell_t,new}\)
in the closing range.  `square`

### Theorem 12.2: Score-Augmented Bootstrap Is Conditionally Positive And
Currently Non-Closing

The score-augmented bootstrap proves the exact conditional implication

$$
\mathrm{P33\text{-}SCAL\text{-}SCOREENERGY}(I_m,I_t)
\Longrightarrow
\mathrm{P32\text{-}SCAL\text{-}RESDEFECT}(\delta_{score}),
$$

with

$$
\delta_{score}
=
A_m(M_\beta)\sqrt{I_m}
+A_t(M_\beta)\sqrt{I_t}.
$$

It also proves that Ward identities without score-energy control do not
close the route.  The current corpus does not source the needed score-energy
bound.

Proof.

The implication is Theorem 10.2.  The no-free-Ward statement is Proposition
11.2.  The current-corpus audit is Proposition 12.1.  `square`

### Corollary 12.3: What Must Be Proved Next

The residual-score route has been sharpened to a single quantitative target:

$$
\mathrm{P33\text{-}SCAL\text{-}SCOREENERGY}(I_m,I_t)
$$

with

$$
A_m(M_\beta)\sqrt{I_m}
+A_t(M_\beta)\sqrt{I_t}
<
B_{rem}.
$$

This is not another reformulation of \(m,t\).  It is a new same-law
regularity estimate for the residual/selector score along the two scalar
block-entry directions.

## 13. Anatomy Of The Scalar Residual Score

We now investigate what such an \(L^2\) score theorem would actually have to
prove.  This matters because "score smallness" can otherwise hide the same
unknown value in a different word.

### Definition 13.1: New Scalar Score Decomposition

For \(r\in\{m,t\}\), write \(X_r\) for the corresponding block-entry vector
field \(X_{\ell_r}\).  Decompose the actual score as

$$
S_r^{act}
=
S_{r,HK}
+S_{r,end}
+S_{r,lic}
+S_{r,new},
$$

where \(S_{r,HK}\), \(S_{r,end}\), and \(S_{r,lic}\) are the heat, endpoint,
and already licensed retained-row pieces.  The new term is

$$
S_{r,new}
=
S_{r,res}
+S_{r,Jac}
+S_{r,sel}
+S_{r,norm}.
$$

Here:

1. \(S_{r,res}=X_rH_{res}\) is the residual Hamiltonian score;
2. \(S_{r,Jac}=X_rH_{Jac}\) is the Jacobian/chart score;
3. \(S_{r,sel}=X_rH_{sel}\) is the selector or selector-boundary score;
4. \(S_{r,norm}=X_rH_{norm}\) is the conditional normalizer score.

This is a bookkeeping identity, not a bound.

### Definition 13.2: Component Score-Energy Package

Write

$$
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}COMP}
\left(\{I_{r,q}\}_{r,q}\right)
$$

if, for \(r\in\{m,t\}\) and
\(q\in\{res,Jac,sel,norm\}\),

$$
\mathbf E[(S_{r,q})^2]\le I_{r,q}
$$

cofinally under the actual adaptive law, with all licensed pieces already
charged.

### Lemma 13.3: Component Energy Implies Score Energy

If `P33-SCAL-SCORE-COMP({I_{r,q}})` holds, then
`P33-SCAL-SCOREENERGY(I_m,I_t)` holds with

$$
I_r
=
\left(
\sum_{q\in\{res,Jac,sel,norm\}}
\sqrt{I_{r,q}}
\right)^2.
$$

Proof.

By Minkowski in \(L^2(\mu^{act})\),

$$
\|S_{r,new}\|_2
\le
\sum_q\|S_{r,q}\|_2
\le
\sum_q\sqrt{I_{r,q}}.
$$

Square the estimate.  `square`

### Corollary 13.4: What Must Be Controlled

The \(L^2\) score theorem is not one theorem in disguise.  It asks for four
same-law \(L^2\) controls in two scalar directions:

$$
S_{m,res},S_{m,Jac},S_{m,sel},S_{m,norm},
\qquad
S_{t,res},S_{t,Jac},S_{t,sel},S_{t,norm}.
$$

Any one uncontrolled component can keep
`P33-SCAL-SCOREENERGY` open.

## 14. Three Ways To Source Score Energy

There are three honest ways to source the component bounds above.

### Route A: Pointwise Score Bound

For \(B_r\ge0\), write

$$
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}PTBOUND}(B_m,B_t)
$$

if

$$
|S_{m,new}|\le B_m,
\qquad
|S_{t,new}|\le B_t
$$

cofinally on the actual adaptive record space.

Then

$$
\mathrm{P33\text{-}SCAL\text{-}SCOREENERGY}(B_m^2,B_t^2)
$$

holds immediately.

Status: valid, but probably too strong.

### Route B: Same-Law Sobolev Or Analytic Score Regularity

For \(A_m,A_t,C_\mu\ge0\), write

$$
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}SOB0}(A_m,A_t,C_\mu)
$$

if the actual density is \(L^\infty\)-dominated by the reference chart
measure with constant \(C_\mu\), and the residual/selector scores obey

$$
\|S_{m,new}\|_{L^2(d\lambda)}\le A_m,
\qquad
\|S_{t,new}\|_{L^2(d\lambda)}\le A_t.
$$

Then

$$
\mathrm{P33\text{-}SCAL\text{-}SCOREENERGY}
\left(C_\mu A_m^2,C_\mu A_t^2\right)
$$

holds.

Proof.

If \(d\mu^{act}\le C_\mu d\lambda\), then

$$
\mathbf E_{\mu^{act}}[S_{r,new}^2]
\le
C_\mu\int S_{r,new}^2\,d\lambda.
$$

Apply the displayed \(L^2(d\lambda)\) bound.  `square`

This is the \(q=0\) version of the Paper-32 same-law Sobolev and
score-Sobolev gates.

### Route C: Curvature Or Self-Energy Identity

The most structural route uses Ward integration by parts again, now with the
score itself as the test.

Let

$$
S_r^{lic}:=S_{r,HK}+S_{r,end}+S_{r,lic},
\qquad
S_r^{act}=S_r^{lic}+S_{r,new}.
$$

For \(K_r,L_r\ge0\), write

$$
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}CURV}(K_r,L_r)
$$

if

$$
\left|
\mathbf E[X_rS_{r,new}]
\right|\le K_r,
\qquad
\mathbf E[(S_r^{lic})^2]\le L_r^2.
$$

### Lemma 14.1: Curvature Controls New Score Energy

If `P33-SCAL-SCORE-CURV(K_r,L_r)` holds, then

$$
\left(\mathbf E[S_{r,new}^2]\right)^{1/2}
\le
{L_r+\sqrt{L_r^2+4K_r}\over2}.
$$

Proof.

Apply the actual Ward identity to the test \(F=S_{r,new}\):

$$
\mathbf E[X_rS_{r,new}]
=
\mathbf E[S_{r,new}S_r^{act}]
=
\mathbf E[S_{r,new}^2]
+\mathbf E[S_{r,new}S_r^{lic}].
$$

Let \(Y=(\mathbf E[S_{r,new}^2])^{1/2}\).  By Cauchy-Schwarz,

$$
Y^2
\le
K_r+L_rY.
$$

Solving the quadratic inequality gives the displayed bound.  `square`

### Corollary 14.2: Curvature Package Implies Score Energy

If `P33-SCAL-SCORE-CURV(K_m,L_m)` and
`P33-SCAL-SCORE-CURV(K_t,L_t)` hold, then
`P33-SCAL-SCOREENERGY(I_m,I_t)` holds with

$$
I_r
=
\left(
{L_r+\sqrt{L_r^2+4K_r}\over2}
\right)^2.
$$

This route replaces direct \(L^2\) score control by a second-derivative
bound on the new residual/selector score.

## 15. Why The Three Routes Are Not Currently Sourced

### Proposition 15.1: Pointwise Score Bounds Are Not Printed

The current corpus does not prove
`P33-SCAL-SCORE-PTBOUND(B_m,B_t)` in a closing range.

Proof.

A pointwise score bound would require uniform control of
\(X_rH_{res}\), \(X_rH_{Jac}\), selector-boundary terms, and
\(X_rH_{norm}\) along the scalar block-entry directions.  Papers 30 through
32 identify these as actual residual, Jacobian, selector, and normalizer
value data.  They do not print pointwise derivative bounds for them.  `square`

### Proposition 15.2: Sobolev Score Bounds Are Not Printed

The current corpus does not prove
`P33-SCAL-SCORE-SOB0(A_m,A_t,C_mu)` in a closing range.

Proof.

Paper 32 Gate 5, `P32-SLAW-SCORE-SOB`, already records the needed
score-Sobolev regularity.  It requires one higher derivative on the residual
logarithmic factors, plus the actual/reference \(L^2\) comparison.  Paper 32
Proposition 79.3 audits that this is not supplied by Papers 20 through 31,
and Paper 33 has added no new analytic regularity theorem.  `square`

### Proposition 15.3: Curvature Score Bounds Are Not Printed

The current corpus does not prove
`P33-SCAL-SCORE-CURV(K_r,L_r)` in a closing range for
\(r=m,t\).

Proof.

The curvature route needs \(X_rS_{r,new}\), hence second derivatives of the
actual residual Hamiltonian, Jacobian, selector contribution, and
normalizer along scalar block-entry directions.  The selector term may also
include boundary or jump contributions unless scalar-field admissibility is
strengthened.  No current paper prints those second derivative expectations,
their signs, or their cofinal bounds.  `square`

### Proposition 15.4: Log-Sobolev Direction Is Wrong For This Estimate

A same-law log-Sobolev or Poincare inequality does not by itself upper-bound
`P33-SCAL-SCOREENERGY`.

Proof.

Poincare and log-Sobolev inequalities bound variances or entropies by
Dirichlet/Fisher quantities.  Here the missing theorem is an upper bound on
the score energy itself.  Such inequalities are useful only after an
independent Dirichlet or curvature estimate bounds the relevant score.  They
do not supply that upper bound from positivity alone.  `square`

## 16. Score-Energy Investigation Verdict

### Theorem 16.1: Exact Sources For The \(L^2\) Scalar Score Estimate

The \(L^2\)-type residual/selector score estimate can be sourced by any one
of the following same-law packages:

1. pointwise residual/selector score bounds
   `P33-SCAL-SCORE-PTBOUND`;
2. same-law score \(L^2\)/Sobolev regularity
   `P33-SCAL-SCORE-SOB0`;
3. score-curvature/self-energy control
   `P33-SCAL-SCORE-CURV`;
4. component \(L^2\) bounds
   `P33-SCAL-SCORE-COMP`.

Each package implies `P33-SCAL-SCOREENERGY`, hence
`P32-SCAL-RESDEFECT`, with the constants printed above.  The current corpus
proves none in a closing range.

Proof.

Component bounds imply score energy by Lemma 13.3.  Pointwise bounds are
immediate.  Sobolev \(L^2\) bounds imply score energy by Route B.  Curvature
implies score energy by Lemma 14.1 and Corollary 14.2.  Propositions 15.1
through 15.3 audit the current corpus.  `square`

### Corollary 16.2: Best Next Attack

The most promising next attack is the curvature/self-energy package

$$
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}CURV}(K_m,L_m)
\quad+\quad
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}CURV}(K_t,L_t),
$$

because it asks for expected second score derivatives rather than pointwise
first derivative bounds everywhere.  It remains a genuine same-law analytic
input: one must control the actual residual Hamiltonian, Jacobian, selector,
and normalizer second derivatives along the two scalar block-entry
directions.

## 17. Direct Attack On The Score-Curvature Package

The best live target from Corollary 16.2 is

$$
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}CURV}(K_m,L_m)
\quad+\quad
\mathrm{P33\text{-}SCAL\text{-}SCORE\text{-}CURV}(K_t,L_t).
$$

We now expand it into the smallest same-law component theorems.  The goal is
to avoid hiding the old unknown value table inside the word "curvature."

### Definition 17.1: Scalar Curvature Admissibility

Write

$$
\mathrm{P33\text{-}SCAL\text{-}CURV\text{-}ADM}
$$

if the scalar vector fields \(X_m,X_t\) are admissible tests for the actual
adaptive pushed-forward law in the following sense:

1. \(S_{r,res},S_{r,Jac},S_{r,norm}\) have same-law distributional
   derivatives \(X_rS_{r,q}\) for \(r\in\{m,t\}\);
2. the selector contribution has a finite distributional derivative,
   including all boundary or jump terms, denoted \(X_rS_{r,sel}\);
3. the Ward identity used in Lemma 14.1 is valid with test
   \(F=S_{r,new}\);
4. every displayed expectation below is evaluated under the same actual
   adaptive law, with the same cofinal selector and the same pushed-forward
   scalar record.

This is an admissibility theorem, not a value theorem.

### Definition 17.2: Component Curvature Gates

For \(q\in\{res,Jac,sel,norm\}\), write

$$
\mathrm{P33\text{-}SCAL\text{-}CURV\text{-}COMP}
\left(\{K_{r,q}\}_{r,q},L_m,L_t\right)
$$

if `P33-SCAL-CURV-ADM` holds and, for \(r\in\{m,t\}\),

$$
\left|\mathbf E[X_rS_{r,q}]\right|\le K_{r,q}
\qquad
(q\in\{res,Jac,sel,norm\}),
$$

while the licensed score satisfies

$$
\mathbf E[(S_r^{lic})^2]\le L_r^2.
$$

Equivalently, this is the four-component Hessian/curvature package:

$$
\begin{array}{ll}
\mathrm{P33\text{-}RES\text{-}HESS}(K_{r,res})&
\left|\mathbf E[X_rS_{r,res}]\right|\le K_{r,res},\\
\mathrm{P33\text{-}JAC\text{-}HESS}(K_{r,Jac})&
\left|\mathbf E[X_rS_{r,Jac}]\right|\le K_{r,Jac},\\
\mathrm{P33\text{-}SEL\text{-}CURV}(K_{r,sel})&
\left|\mathbf E[X_rS_{r,sel}]\right|\le K_{r,sel},\\
\mathrm{P33\text{-}NORM\text{-}HESS}(K_{r,norm})&
\left|\mathbf E[X_rS_{r,norm}]\right|\le K_{r,norm}.
\end{array}
$$

### Lemma 17.3: Component Curvature Implies Score Curvature

If `P33-SCAL-CURV-COMP({K_{r,q}},L_m,L_t)` holds, then
`P33-SCAL-SCORE-CURV(K_r,L_r)` holds for \(r=m,t\), with

$$
K_r
=K_{r,res}+K_{r,Jac}+K_{r,sel}+K_{r,norm}.
$$

Proof.

By Definition 13.1,

$$
S_{r,new}
=
S_{r,res}+S_{r,Jac}+S_{r,sel}+S_{r,norm}.
$$

Under `P33-SCAL-CURV-ADM`, \(X_r\) may be applied distributionally and
expectations are linear.  Hence

$$
\left|\mathbf E[X_rS_{r,new}]\right|
\le
\sum_{q\in\{res,Jac,sel,norm\}}
\left|\mathbf E[X_rS_{r,q}]\right|
\le K_r.
$$

The licensed-score estimate is already part of the component package, so
Definition 14.1 applies.  `square`

### Corollary 17.4: Component Curvature Implies Score Energy

If `P33-SCAL-CURV-COMP({K_{r,q}},L_m,L_t)` holds, then
`P33-SCAL-SCOREENERGY(I_m,I_t)` holds with

$$
I_r
=
\left(
{L_r+\sqrt{L_r^2+4K_r}\over2}
\right)^2,
\qquad
K_r=\sum_q K_{r,q}.
$$

Consequently it implies `P32-SCAL-RESDEFECT(delta_score)` with the
constant printed in Theorem 10.2.

## 18. What The Four Curvatures Mean

The four component gates above have different mathematical content.  This
section records them in operational form.

### Definition 18.1: Residual Hessian Gate

`P33-RES-HESS(K_{r,res})` is the assertion that the actual residual
Hamiltonian part has bounded scalar Hessian average,

$$
\left|\mathbf E[X_r^2H_{res}]\right|\le K_{r,res},
$$

with the understanding that \(X_r^2H_{res}\) is the same-law
distributional second derivative when the residual Hamiltonian is only
piecewise smooth in the scalar record.

This is exactly the residual value theorem in differentiated form.

### Definition 18.2: Jacobian Hessian Gate

`P33-JAC-HESS(K_{r,Jac})` is the assertion that the chart/Jacobian factor
has bounded scalar Hessian average,

$$
\left|\mathbf E[X_r^2H_{Jac}]\right|\le K_{r,Jac}.
$$

This gate is more geometric than dynamical, but it is not automatic: it
requires the scalar chart used by the pushed-forward law to have a cofinal
Hessian bound in the same coordinates used for \(m,t\).

### Definition 18.3: Selector Curvature Gate

`P33-SEL-CURV(K_{r,sel})` is the assertion that the selector contribution,
including all boundary terms produced when \(X_r\) crosses a selector
decision surface, satisfies

$$
\left|\mathbf E[X_rS_{r,sel}]\right|\le K_{r,sel}.
$$

If the selector is locally constant along \(X_r\) outside a null boundary,
then \(S_{r,sel}=0\) and this gate holds with \(K_{r,sel}=0\).  Otherwise it
requires an actual bound on selector-boundary flux.

### Definition 18.4: Normalizer Hessian Gate

`P33-NORM-HESS(K_{r,norm})` is the assertion that the conditional
normalizer has bounded scalar Hessian average,

$$
\left|\mathbf E[X_rS_{r,norm}]\right|\le K_{r,norm}.
$$

In a local conditional chart with conditional density proportional to
\(\exp(-G_r(u,z))\), the normalizer term has the schematic second derivative

$$
X_r^2\log Z_r(u)
=
-\mathbf E_{\nu_u}[X_r^2G_r]
+\operatorname{Var}_{\nu_u}(X_rG_r),
$$

up to the sign convention used for \(H_{norm}\).  Thus this gate is not a
free normalization identity: it asks for an expected conditional Hessian
and a conditional score-variance bound.

### Proposition 18.5: Normalization Does Not Remove The Problem

The normalizer Hessian cannot be discarded merely because probabilities
sum to one.

Proof.

The identity \(\int d\nu_u=1\) gives score centering,

$$
\mathbf E_{\nu_u}[S_{r,cond}]=0.
$$

Differentiating once more gives a relation between conditional score
variance and conditional Hessian.  It does not make either term small.
Indeed, the variance term in Definition 18.4 is a positive same-law value.
Unless a Hessian, variance, or cancellation estimate is supplied, the
normalizer contribution can be as large as the residual score energy one is
trying to bound.  `square`

## 19. Current-Corpus Audit Of The Curvature Attack

### Proposition 19.1: Residual Hessian Is Not Printed

The current corpus does not prove `P33-RES-HESS(K_{r,res})` in a closing
range.

Proof.

Papers 26, 29, 30, and 32 repeatedly identify the actual residual atoms,
residual signed products, and residual source responses as the live
same-law value data.  A residual Hessian average is at least as strong as a
second source-response theorem for those same actual objects.  No current
paper prints that table, a domination theorem for it, or a sign rule forcing
its cancellation.  `square`

### Proposition 19.2: Jacobian Hessian Is Not Licensed As A Closing Bound

The current corpus does not prove `P33-JAC-HESS(K_{r,Jac})` in a closing
range.

Proof.

The corpus contains finite chart and scalar-record bookkeeping, but the
score-curvature route needs a numerical cofinal bound on
\(\mathbf E[X_r^2H_{Jac}]\) in the same adaptive pushed-forward chart.
That bound is not printed with constants compatible with the residual-score
budget.  Therefore the Jacobian term is structurally identified but not
closed.  `square`

### Proposition 19.3: Selector Curvature Needs Local Constancy Or Boundary
Control

The selector term is harmless under either of two same-law hypotheses: the
chosen scalar selector is locally constant along \(X_m,X_t\) outside null
boundary sets, or its boundary flux is separately bounded.

Proof.

If the selector is locally constant along \(X_r\), then \(X_rH_{sel}=0\)
away from the boundary and the null-boundary hypothesis removes the
distributional contribution.  If selector decision surfaces carry positive
actual flux, \(X_rS_{r,sel}\) contains boundary mass.  That mass can still
be controlled by a separate boundary-flux theorem, but it is not controlled
by ordinary finite-label counting, because it is weighted by the actual
pushed-forward law.  `square`

### Proposition 19.4: Normalizer Hessian Is A Same-Law Variance Problem

The current corpus does not prove `P33-NORM-HESS(K_{r,norm})` in a closing
range.

Proof.

Definition 18.4 shows that a normalizer Hessian contains conditional
variance and conditional Hessian terms for the same residual/Jacobian
objects.  Normalization centers the conditional score but does not
upper-bound its variance.  The missing estimate is therefore a same-law
conditional score-curvature theorem, not a bookkeeping identity.  `square`

## 20. Score-Curvature Verdict

### Theorem 20.1: Exact Component Theorems Needed For The Curvature Route

The curvature/self-energy route closes the \(L^2\) scalar score estimate if
the following same-law package is proved for \(r=m,t\):

$$
\mathrm{P33\text{-}RES\text{-}HESS}(K_{r,res})
\quad+\quad
\mathrm{P33\text{-}JAC\text{-}HESS}(K_{r,Jac})
\quad+\quad
\mathrm{P33\text{-}SEL\text{-}CURV}(K_{r,sel})
\quad+\quad
\mathrm{P33\text{-}NORM\text{-}HESS}(K_{r,norm}),
$$

together with licensed-score energy \(L_r\).  It then gives
`P33-SCAL-SCOREENERGY(I_m,I_t)` with

$$
I_r
=
\left(
{L_r+\sqrt{L_r^2+4(K_{r,res}+K_{r,Jac}+K_{r,sel}+K_{r,norm})}\over2}
\right)^2.
$$

Proof.

This is Corollary 17.4 after expanding \(K_r\).  `square`

### Corollary 20.2: Best Remaining Positive Subroute

The cleanest positive subroute is now:

1. prove scalar selector local constancy, so \(K_{r,sel}=0\);
2. print a same-law residual Hessian/source-curvature table for
   \(H_{res}\);
3. print a cofinal scalar-chart Jacobian Hessian bound;
4. dominate the conditional normalizer Hessian by the same residual
   Hessian and licensed score energy.

If these four statements hold with

$$
A_m(M_\beta)\sqrt{I_m}+A_t(M_\beta)\sqrt{I_t}<B_{rem},
$$

then the residual-score route closes.  The current corpus proves none of
the three value-bearing pieces in closing range.  Thus the score-curvature
attack has reduced the target, but it has not yet supplied the new
same-law value information.

### Corollary 20.3: No Further Finite-Label Escape

Further finite-label refinement cannot by itself prove the score-curvature
route unless it produces one of the four component curvature estimates
above.

Proof.

The component formula in Theorem 20.1 is exact.  Extra labels can refine the
domains on which \(H_{res}\), \(H_{Jac}\), \(H_{sel}\), and \(H_{norm}\) are
evaluated, but the needed quantities remain the same actual-law
expectations \(\mathbf E[X_rS_{r,q}]\).  Without a numerical upper bound,
sign cancellation, or floor witness for these expectations, label
refinement leaves the \(L^2\) score estimate open.  `square`
