# Relativistic ISP V3 Paper 36: Non-Gauge Ward-Stein Ray-Cut Or Dual Floor

Author: Felix Robles Elvira

Date: 2026-05-26

## Abstract

Paper 35 proves the scalar-ray detector theorem: adaptive Branch A cannot
move unless a future same-law theorem cuts or orients the surviving scalar
ray

$$
B(c)=cI_2.
$$

The first ranked detector is a non-gauge Ward-Stein identity of the form

$$
Ac=D+\epsilon,
$$

where \(A\ne0\) is a scalar-ray coefficient, \(D\) is already licensed, and
\(\epsilon\) is a genuinely bounded residual or selector score defect.

This paper attacks that detector.  It proves that, in the formal
block-entry envelope, the two live scalars \(m,t\) are exact Ward-Stein
derivatives.  Hence the scalar-ray coefficient is explicit and nonzero
unless the heat readout itself degenerates:

$$
A_m=h_0+h_A,
\qquad
A_t=a_N(h_0-h_A).
$$

But it also proves the honest current-corpus endpoint.  Formal block-entry
derivatives are not yet actual same-law vector fields.  To turn the formal
ray cut into a proof, one must source the actual package

$$
\mathrm{P36\text{-}ACT\text{-}SCALFIELD\text{-}ADM}
\quad+\quad
\mathrm{P36\text{-}ACT\text{-}RAYCOEFF}(A_0)
\quad+\quad
\mathrm{P36\text{-}WS\text{-}SCOREDEF}(\epsilon).
$$

Equivalently, if the actual Ward-Stein range misses the scalar direction,
one must source the dual sign theorem

$$
\mathrm{P36\text{-}WS\text{-}DUALSIGN}(M_*).
$$

Thus the non-gauge Ward-Stein route is not empty: the formal ray-cut algebra
works.  The obstruction is narrower and sharper than before: actual
same-law scalar-field admissibility and residual-score control, or else a
dual floor.

## 0. Imports And Barandes Rule

### Import 0.1: Paper-35 Scalar-Ray Test

Paper 35 defines the scalar-ray laws \(\nu_c\), supported on

$$
B(c)=cI_2,
\qquad
|c|\le M_\beta.
$$

Along this ray,

$$
m(c)=c(h_0+h_A),
$$

and

$$
t(c)=ca_N(h_0-h_A).
$$

Paper 35 proves that passive deterministic-character constraints are
ray-blind.  A useful positive theorem must either bound \(|c|\), force a
nonzero equation for \(c\), or produce a sign-coherent floor.

### Import 0.2: Paper-32 Ward-Stein Envelope

Paper 32 defines the live block

$$
B_{\Gamma_1}^{N,j}
=
\begin{pmatrix}
\beta_{00}&\beta_{0A}\\
\beta_{A0}&\beta_{AA}
\end{pmatrix},
$$

with

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

It proves that the formal block-entry scalar Jacobian has rank two and that
the scalar rank problem is solved in the block-entry envelope.  The remaining
obstruction is not scalar linear algebra.  It is actual same-law
admissibility of the block-entry vector fields and a bound on the new
residual or selector Ward score.

### Import 0.3: Paper-33 Score-Energy Warning

Paper 33 proves that Ward identities without a score-energy or score-defect
bound do not close the scalar route.  A formal Ward identity merely trades an
unknown value for an uncontrolled score pairing.

### Barandes Rule 0.4

Every vector field, score, derivative, source, and floor in this paper is a
finite same-record object.  No hidden Markov state, off-law comparison
measure, external heat dynamics, or extra physical transition is introduced.
The only admissible proof is a statement about the actual adaptive
pushed-forward record law and its finite record functions.

## 1. The Non-Gauge Ward-Stein Ray-Cut Target

### Definition 1.1: Scalar Ward-Stein Ray-Cut

Let \(X\) be an admissible finite same-law vector field and \(F\) a finite
test observable.  Their scalar-ray trace is the affine function

$$
\operatorname{Tr}_{ray}(XF)(c)
:=
(XF)(B(c)).
$$

The pair \((X,F)\) is scalar-ray sensitive if

$$
\operatorname{Tr}_{ray}(XF)(c)=Ac+L
$$

with \(A\ne0\), where \(L\) is a licensed constant or an already charged
term.

### Definition 1.2: `P36-NONGAUGE-WS-RAYCUT`

For \(A_0>0\) and \(\epsilon\ge0\), write

$$
\mathrm{P36\text{-}NONGAUGE\text{-}WS\text{-}RAYCUT}(A_0,\epsilon)
$$

if there is a cofinal family of same-law Ward-Stein pairs
\((X,F)\) such that:

1. the pair is not a pure gauge or passive relabeling direction;
2. its scalar-ray coefficient obeys \(|A|\ge A_0\);
3. all licensed terms are already inside the Branch-A ledger;
4. the new unlicensed score pairing obeys

   $$
   |\mathbf E[F S_{X,new}]|\le\epsilon.
   $$

Here \(S_{X,new}\) is the part of the Ward score coming from actual residual
Hamiltonians, Jacobians, selectors, conditional normalizers, and any
unlicensed residual boundary terms.

### Definition 1.3: Closing Range

Let

$$
H_{ray}:=
\max\{|h_0+h_A|,\ |a_N(h_0-h_A)|\}.
$$

The ray-cut is closing if

$$
{\epsilon\over A_0}H_{ray}
$$

is below the scalar Branch-A budget after all already licensed tail and
finite-cutoff debits.

## 2. The One-Line Ray-Cut Lemma

### Lemma 2.1: Ward-Stein Ray-Cut

Assume a same-law Ward-Stein pair satisfies

$$
\operatorname{Tr}_{ray}(XF)(c)=Ac+L,
\qquad
|A|\ge A_0>0,
$$

with \(L\) licensed, and assume

$$
|\mathbf E[F S_{X,new}]|\le\epsilon.
$$

Then the scalar-ray amplitude obeys

$$
|c|\le{\epsilon\over A_0}
$$

after the licensed ledger terms are subtracted.

Proof.

The same-law Ward identity gives

$$
\mathbf E[XF]=\mathbf E[F S_X].
$$

Split \(S_X=S_{X,lic}+S_{X,new}\).  The licensed part cancels against the
licensed ledger term \(L\) by assumption.  On the scalar ray the remaining
identity is

$$
Ac=\mathbf E[F S_{X,new}].
$$

Taking absolute values gives

$$
|c|\le {| \mathbf E[F S_{X,new}]|\over |A|}
\le{\epsilon\over A_0}.
$$

`square`

### Corollary 2.2: Branch-A Scalar Closure

If `P36-NONGAUGE-WS-RAYCUT(A_0,epsilon)` holds in the closing range of
Definition 1.3, then the scalar-ray obstruction of Papers 33 through 35 is
cut below the Branch-A scalar budget.

Proof.

By Lemma 2.1,

$$
|m|\le{\epsilon\over A_0}|h_0+h_A|,
\qquad
|t|\le{\epsilon\over A_0}|a_N(h_0-h_A)|.
$$

Taking the maximum gives the claimed budget comparison.  `square`

## 3. Formal Block-Entry Certificates

This section proves that the formal algebra is not the problem.

### Definition 3.1: Block-Entry Linear Forms

Let

$$
\beta=(\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA}).
$$

Define

$$
\ell_m=(h_0,0,0,h_A),
$$

and

$$
\ell_t=(a_Nh_0,b_Nh_0,b_Nh_A,-a_Nh_A).
$$

Then

$$
m=\ell_m\cdot\beta,
\qquad
t=\ell_t\cdot\beta.
$$

For any nonzero \(\ell\), define

$$
X_\ell:=\ell\cdot\nabla_\beta,
\qquad
F_\ell(\beta):={(\ell\cdot\beta)^2\over2\|\ell\|_2^2}.
$$

### Lemma 3.2: Exact Formal Ward Derivatives

For \(\ell\in\{\ell_m,\ell_t\}\),

$$
X_\ell F_\ell=\ell\cdot\beta.
$$

In particular,

$$
X_{\ell_m}F_{\ell_m}=m,
\qquad
X_{\ell_t}F_{\ell_t}=t.
$$

Proof.

Differentiate:

$$
X_\ell F_\ell
=
\ell\cdot\nabla_\beta
{(\ell\cdot\beta)^2\over2\|\ell\|_2^2}
=
\ell\cdot\beta.
$$

`square`

### Lemma 3.3: Formal Scalar-Ray Coefficients

On \(B(c)=cI_2\),

$$
X_{\ell_m}F_{\ell_m}=c(h_0+h_A),
$$

and

$$
X_{\ell_t}F_{\ell_t}=ca_N(h_0-h_A).
$$

Thus the formal scalar-ray coefficients are

$$
A_m=h_0+h_A,
\qquad
A_t=a_N(h_0-h_A).
$$

Proof.

On the scalar ray,

$$
\beta_{00}=\beta_{AA}=c,
\qquad
\beta_{0A}=\beta_{A0}=0.
$$

Substitute this into the formulas for \(m\) and \(t\).  `square`

### Corollary 3.4: Formal Ray-Cut Coefficient Passes

If

$$
A_0\le\max\{|h_0+h_A|,\ |a_N(h_0-h_A)|\},
$$

then the formal block-entry envelope contains a scalar-ray-sensitive
Ward-Stein certificate with coefficient at least \(A_0\).

Proof.

Choose \(m\) if \(|h_0+h_A|\ge A_0\), otherwise choose \(t\).  Lemma 3.3 gives
the coefficient.  `square`

## 4. Why Formal Is Not Yet Actual

### Definition 4.1: Actual Scalar-Field Admissibility

Write

$$
\mathrm{P36\text{-}ACT\text{-}SCALFIELD\text{-}ADM}(\sigma,C_S)
$$

if the two formal scalar vector fields \(X_{\ell_m},X_{\ell_t}\) admit
finite same-law lifts \(Y_m,Y_t\) on the actual adaptive record variables
such that:

1. \(Y_r\) differentiates the actual block product in the scalar direction
   \(r\in\{m,t\}\) with quotient error \(o(1)\);
2. the least singular value of the lifted scalar map is at least
   \(\sigma>0\);
3. the new Ward scores of \(Y_m,Y_t\) obey the finite envelope \(C_S\);
4. selector-only, gauge-only, and endpoint-additive directions have already
   been quotiented out.

### Definition 4.2: Actual Ray Coefficient

Write

$$
\mathrm{P36\text{-}ACT\text{-}RAYCOEFF}(A_0)
$$

if, after the actual lifts in Definition 4.1 are chosen, at least one lifted
Ward-Stein pair has scalar-ray coefficient \(|A|\ge A_0\) in the active
quotient.

### Definition 4.3: Ward-Stein Score Defect

Write

$$
\mathrm{P36\text{-}WS\text{-}SCOREDEF}(\epsilon)
$$

if the lifted scalar Ward-Stein pair satisfies

$$
|\mathbf E[F_m S_{m,new}]|
+|\mathbf E[F_t S_{t,new}]|
\le\epsilon
$$

cofinally after licensed heat, endpoint, retained-row, and tail charges.

### Proposition 4.4: Formal Certificates Require Actual Admissibility

The formal certificates of Section 3 become actual same-law Ward-Stein
ray-cut certificates only if

$$
\mathrm{P36\text{-}ACT\text{-}SCALFIELD\text{-}ADM}
\quad+\quad
\mathrm{P36\text{-}ACT\text{-}RAYCOEFF}(A_0)
$$

hold.

Proof.

Ward-Stein integration by parts is an identity on the actual finite
integration variables.  The formal vector fields \(X_{\ell_m},X_{\ell_t}\)
live in block-entry coordinates \(\beta\).  Unless they lift to actual
same-law vector fields \(Y_m,Y_t\), there is no actual score \(S_Y\) and no
actual Ward identity to apply.  If they lift but lose the scalar coefficient
in the quotient, the scalar ray is not cut.  `square`

### Proposition 4.5: The Current Corpus Does Not Prove Actual Admissibility

The current corpus does not prove
`P36-ACT-SCALFIELD-ADM(sigma,C_S)` or
`P36-ACT-RAYCOEFF(A_0)` in a closing range.

Proof.

Paper 32 proves the formal block-entry rank and then isolates exactly this
missing step under the names `P32-SCALFIELD-ADM`,
`P32-SCAL-CONFJAC`, and `P32-SCAL-SRCMAT`.  It further proves that the
configuration-Jacobian route is not printed by the current corpus and that
the source-matrix route requires a new structural source-rank and curvature
theorem.  Paper 35 confirms that passive source reparametrization is
ray-blind.  Therefore actual scalar-field admissibility is still a
value-bearing same-law theorem, not a consequence of the formal block
coordinates.  `square`

### Proposition 4.6: The Current Corpus Does Not Prove The Score Defect

The current corpus does not prove
`P36-WS-SCOREDEF(epsilon)` in a closing range.

Proof.

Paper 32 defines the corresponding score defect as
`P32-SCAL-RESDEFECT(delta)` and proves that it is not sourced by the current
corpus.  Paper 33 then sharpens the issue: Ward identities without
score-energy or score-curvature control leave arbitrary score cost.  It
reduces a possible proof to residual Hessian, Jacobian Hessian, selector
curvature, and normalizer Hessian inputs, none of which is printed in a
closing range.  Hence the score defect remains a primitive actual-law input.
`square`

## 5. Ray-Blind Subroutes

### Proposition 5.1: Pure Gauge Or Haar Ward Directions Are Ray-Blind

Pure gauge or Haar Ward identities do not supply
`P36-NONGAUGE-WS-RAYCUT`.

Proof.

Paper 32 proves that pure gauge/Haar Ward range does not contain the live
scalar classes.  On the scalar ray \(B=cI_2\), gauge directions commute with
the scalar intertwiner and have zero scalar-ray coefficient.  Thus \(A=0\).
`square`

### Proposition 5.2: Selector-Only Directions Are Ray-Blind

Selector-only Ward directions do not supply
`P36-NONGAUGE-WS-RAYCUT`.

Proof.

Paper 32 proves selector-only directions have zero live Jacobian.  Therefore
they have zero scalar-ray coefficient in the active quotient.  `square`

### Proposition 5.3: Endpoint-Additive And Normalizer-Only Directions Are Not
Enough

Endpoint-additive, licensed normalizer, or already retained-row directions
do not by themselves supply the ray-cut.

Proof.

Those terms are part of the licensed ledger.  After quotienting them out,
they either cancel from the active scalar equation or enter the already
charged \(L\) term of Definition 1.1.  A ray-cut requires a nonzero
unlicensed scalar coefficient with a controlled new score defect.  `square`

### Proposition 5.4: Heat-Only Directions Are Ray-Blind

Heat-diagonal data and clean heat-kernel Ward directions do not source the
non-gauge ray-cut.

Proof.

The heat data provide the readout constants \(h_0,h_A,a_N,b_N\).  They
convert \(c\) into \(m,t\).  They do not create an actual residual or
selector vector field that changes \(c\), and therefore do not bound \(c\).
This is Paper 35, Proposition 3.4, in Ward-Stein language.  `square`

## 6. The Dual Fork

If the actual Ward-Stein range cannot reach the scalar direction, a finite
dual separates the scalar ray from the actual range.  This can be useful
only if the separating functional is sign-coherent under the actual law.

### Definition 6.1: Ward-Stein Dual Floor Candidate

Write

$$
\mathrm{P36\text{-}WS\text{-}DUALCAND}(Q)
$$

if the finite Ward-Stein quotient admits a dual functional \(Q\) such that:

1. \(Q\) vanishes on all licensed Ward-Stein range directions;
2. \(Q\) is positive on the scalar target direction;
3. \(Q\) is represented by a same-law finite observable in the active
   scalar family \(m,t,\lambda_+,\lambda_-\).

### Definition 6.2: Ward-Stein Dual Sign Theorem

Write

$$
\mathrm{P36\text{-}WS\text{-}DUALSIGN}(M_*)
$$

if a dual candidate \(Q\) obeys the same-law sign-coherent lower bound

$$
\mathbf E[Q]\ge M_*
$$

with \(M_*\) above the Branch-A floor threshold.

### Lemma 6.3: Range Failure Gives Only A Candidate

Failure of the actual Ward-Stein range to contain the scalar direction gives
`P36-WS-DUALCAND(Q)` at finite cutoff, but it does not by itself give
`P36-WS-DUALSIGN(M_*)`.

Proof.

Finite-dimensional separation gives a linear functional separating the
closed range from the scalar target.  That is a dual candidate.  However,
separation is an algebraic statement about a quotient.  It does not prove
that the actual same-law expectation of the separating observable has a
fixed sign and magnitude.  The sign and magnitude are exactly the lower-floor
value theorem.  `square`

### Corollary 6.4: Negative Closure Target

If `P36-WS-DUALSIGN(M_*)` holds in the Branch-A floor range, then adaptive
Branch A is falsified by the same scalar floor mechanism isolated in Papers
32 through 35.

## 7. Paper-36 Main Theorem

### Theorem 7.1: Non-Gauge Ward-Stein Ray-Cut Reduction

The Rank-1 detector of Paper 35 has the following exact status.

1. In the formal block-entry envelope, the scalar-ray coefficient is printed:

   $$
   A_m=h_0+h_A,
   \qquad
   A_t=a_N(h_0-h_A).
   $$

2. If

   $$
   \mathrm{P36\text{-}ACT\text{-}SCALFIELD\text{-}ADM}
   +\mathrm{P36\text{-}ACT\text{-}RAYCOEFF}(A_0)
   +\mathrm{P36\text{-}WS\text{-}SCOREDEF}(\epsilon)
   $$

   holds in the closing range, then
   `P36-NONGAUGE-WS-RAYCUT(A_0,epsilon)` holds and the scalar ray is cut.

3. Pure gauge/Haar, selector-only, endpoint-additive, normalizer-only, and
   heat-only subroutes have zero active scalar coefficient or no new score
   bound; they are ray-blind for this detector.

4. If the actual Ward-Stein range misses the scalar direction, the only
   closing negative route is

   $$
   \mathrm{P36\text{-}WS\text{-}DUALSIGN}(M_*).
   $$

5. The current corpus proves the formal coefficient but proves neither the
   actual scalar-field admissibility, nor the closing score-defect bound, nor
   the dual sign theorem.

Proof.

Item 1 is Lemma 3.3.  Item 2 is Lemma 2.1 and Proposition 4.4.  Item 3 is
Section 5.  Item 4 is Section 6.  Item 5 is Propositions 4.5 and 4.6 plus
Lemma 6.3.  `square`

### Corollary 7.2: The Attack Surface Is Reduced Again

The non-gauge Ward-Stein route is now reduced to three primitive same-law
inputs:

$$
\boxed{
\mathrm{P36\text{-}ACT\text{-}SCALFIELD\text{-}ADM}
\quad+\quad
\mathrm{P36\text{-}ACT\text{-}RAYCOEFF}(A_0)
\quad+\quad
\mathrm{P36\text{-}WS\text{-}SCOREDEF}(\epsilon)
}
$$

or to the floor fork

$$
\boxed{
\mathrm{P36\text{-}WS\text{-}DUALSIGN}(M_*)
}.
$$

Further passive labels, passive moments, passive RP/SOS constraints, gauge
Ward identities, selector relabelings, or clean heat-kernel identities do
not move this detector.

### Corollary 7.3: The Next Honest Work Package

The next positive work package should choose exactly one of:

1. prove actual scalar-field admissibility by printing a pointwise
   same-law lift for the two scalar block directions;
2. prove the residual score-defect bound by a same-law \(L^2\),
   Hessian-curvature, or normalizer-variance theorem;
3. compute the finite Ward-Stein quotient and try to turn its dual
   separator into a sign-coherent floor.

No other part of the non-gauge Ward-Stein detector remains hidden.

## 8. Plain Verdict

The good news is that the non-gauge Ward-Stein idea is mathematically sharp:
if an actual same-law vector field can push the live residual/signed block
in the scalar direction, the scalar ray is immediately exposed.

The bad news is equally sharp: the current corpus has only the formal
block-entry derivative, not the actual same-law vector field and not the
closing residual-score defect.  The missing theorem is therefore not another
coordinate calculation.  It is a genuine same-law analytic statement about
how the actual adaptive pushed-forward law changes in the two scalar
residual directions.

This is exactly where the Barandes-aligned discipline matters.  We are not
allowed to pretend that the block entries are independent hidden state
coordinates.  They must be realized as finite record-law directions, or the
route must pivot to the dual floor.
