# Relativistic ISP V3 Paper 37: Actual Scalar-Field Admissibility Or Kernel Floor

Author: Felix Robles Elvira

Date: 2026-05-26

## Abstract

Paper 36 proves that the formal non-gauge Ward-Stein ray-cut works in the
block-entry envelope.  The remaining question is more primitive:

$$
\hbox{do the two scalar directions }m,t\hbox{ exist as actual same-law
admissible vector-field directions?}
$$

This paper executes that gatekeeper.  It does the five tasks left by Paper
36:

1. define the actual scalar map;
2. print the actual Jacobian target;
3. try to build a controlled right inverse;
4. if rank two passes, define the lifted Ward-Stein fields;
5. if rank fails, extract the finite separator and identify the floor theorem
   still needed.

The result is sharp but not magically closing.  The actual scalar-field
admissibility theorem is equivalent to a same-law pointwise lift plus a
rank-two actual Jacobian with controlled Ward score:

$$
\mathrm{P37\text{-}SCAL\text{-}POINTLIFT}
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}JACRANK}(\sigma)
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}SCOREENV}(C_S).
$$

The current corpus does not prove this package: it has the formal block
entries and formal scalar rank, but not pointwise actual functions
\(m^{pt},t^{pt}\), not their actual Jacobian, and not the Ward-score envelope.
The positive route therefore remains open only as a new actual-law theorem.
If the actual rank fails, finite separation gives a kernel-floor candidate,
but it becomes a Branch-A falsification only after the sign-coherent value
theorem

$$
\mathrm{P37\text{-}SCAL\text{-}KERFLOOR}(M_*).
$$

Part II then follows the source-response/structural route inside the same
paper.  It proves that the two-knob structural source is a valid
Barandes-aligned alternative to configuration vector fields only if the
source is coupled to the actual residual/signed product \(R\Sigma\), not
merely to the clean heat diagonal.  The compact positive route becomes

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}COUPLE}(\varepsilon)
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}GRAM}(\sigma,M)
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}CURV}(\rho,\epsilon).
$$

The negative route is the rigidity/floor theorem

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}RIGIDFLOOR}(M_*).
$$

The current corpus proves none of these primitive value inputs.  Thus Paper
37 closes both the actual-coordinate admissibility audit and the structural
source-response audit at current-corpus level: there is no hidden coordinate
trick and no clean-heat source shortcut left.

## 0. Imports And No-Smuggling Rule

### Import 0.1: Paper-36 Gate

Paper 36 reduced the non-gauge Ward-Stein ray-cut to

$$
\mathrm{P36\text{-}ACT\text{-}SCALFIELD\text{-}ADM}
\quad+\quad
\mathrm{P36\text{-}ACT\text{-}RAYCOEFF}(A_0)
\quad+\quad
\mathrm{P36\text{-}WS\text{-}SCOREDEF}(\epsilon),
$$

or to the dual sign theorem

$$
\mathrm{P36\text{-}WS\text{-}DUALSIGN}(M_*).
$$

This paper attacks the first factor:

$$
\mathrm{P36\text{-}ACT\text{-}SCALFIELD\text{-}ADM}.
$$

### Import 0.2: Paper-32 Scalar Admissibility

Paper 32 already proved that full four-entry block admissibility is
overpayment.  The minimal scalar route needs only the two scalar directions

$$
s_{blk}(\theta)=(m(\theta),t(\theta)).
$$

It named the target `P32-SCALFIELD-ADM` and proved that it can be sourced
only by an actual configuration Jacobian theorem or by a source-response
matrix route with curvature control.

### No-Smuggling Rule 0.3

The variables \(m,t\) cannot be appended as free coordinates.  They must be
finite measurable functions of the actual adaptive pushed-forward record law,
or derivatives of finite same-law source pressures evaluated at source value
zero.  Otherwise the proof would be about an enlarged comparison object, not
about the actual record law.

## 1. Define The Actual Scalar Map

### Definition 1.1: Actual Local Chart

At fixed \((N,j,L)\), let

$$
\Theta_{act}^{N,j,L}
$$

be the finite actual adaptive record chart touching the minimal live block
\(\Gamma_1\), after quotienting:

1. endpoint-additive rows;
2. already licensed retained rows;
3. pure gauge/Haar tangent directions;
4. selector-only directions with zero live Jacobian;
5. normalizer constants already charged in the ledger.

The notation \(\theta\in\Theta_{act}^{N,j,L}\) denotes actual finite record
variables, not hidden Markov states.

### Definition 1.2: Actual Scalar Pointwise Lift

Write

$$
\mathrm{P37\text{-}SCAL\text{-}POINTLIFT}(L,\varepsilon)
$$

if there are finite same-law observables

$$
m_{\Gamma_1}^{pt}(\theta),
\qquad
t_{\Gamma_1}^{pt}(\theta)
$$

on \(\Theta_{act}^{N,j,L}\) such that their actual pushed-forward table
entries recover the scalar responses \(m,t\) with quotient error
\(\varepsilon=o(1)\), using the same endpoint, selector, residual,
Jacobian, and normalizer conventions as the adaptive law.

### Definition 1.3: Actual Scalar Map

Assuming `P37-SCAL-POINTLIFT`, define

$$
s_{act}^{N,j,L}:\Theta_{act}^{N,j,L}\to\mathbb R^2,
\qquad
s_{act}^{N,j,L}(\theta)
:=
\bigl(m_{\Gamma_1}^{pt}(\theta),
t_{\Gamma_1}^{pt}(\theta)\bigr).
$$

This is the actual scalar map.

### Proposition 1.4: The Formal Block Map Is Not The Actual Scalar Map

The formula

$$
m=h_0\beta_{00}+h_A\beta_{AA},
\qquad
t=a_N(h_0\beta_{00}-h_A\beta_{AA})
+b_N(h_0\beta_{0A}+h_A\beta_{A0})
$$

does not by itself prove `P37-SCAL-POINTLIFT`.

Proof.

The displayed formula is a finite algebraic compression after the block
entries \(\beta_{ab}\) are known.  `P37-SCAL-POINTLIFT` asks for those scalar
entries as actual same-law observables on the finite adaptive record chart,
including residual Hamiltonians, Jacobians, selectors, endpoint conventions,
and conditional normalizers.  Paper 32 already showed that formal block
coordinates are not automatically actual admissible coordinates.  `square`

## 2. Print The Actual Jacobian Target

### Definition 2.1: Actual Scalar Jacobian

Assuming `P37-SCAL-POINTLIFT`, the actual scalar Jacobian is

$$
G_{act}^{scal}
:=
D_\theta s_{act}^{N,j,L}
=
D_\theta
\bigl(m_{\Gamma_1}^{pt},t_{\Gamma_1}^{pt}\bigr).
$$

This is a finite \(2\times d\) matrix, where \(d\) is the dimension of the
active chart after quotienting licensed null directions.

### Definition 2.2: Actual Scalar Jacobian Rank

Write

$$
\mathrm{P37\text{-}SCAL\text{-}JACRANK}(\sigma)
$$

if \(G_{act}^{scal}\) has a two-dimensional right inverse on the active
quotient with least singular value at least \(\sigma>0\), cofinally.

Equivalently, there is a finite linear map

$$
R_{act}^{scal}:\mathbb R^2\to T_\theta\Theta_{act}^{N,j,L}
$$

such that

$$
G_{act}^{scal}R_{act}^{scal}=I_2+o(1),
$$

with operator norm at most \(\sigma^{-1}+o(1)\).

### Definition 2.3: Actual Scalar Score Envelope

Write

$$
\mathrm{P37\text{-}SCAL\text{-}SCOREENV}(C_S)
$$

if the Ward scores of the two lifted vector fields

$$
Y_m:=R_{act}^{scal}e_m,
\qquad
Y_t:=R_{act}^{scal}e_t
$$

obey the cofinal finite envelope \(C_S\) after licensed heat, endpoint,
retained-row, selector-null, and normalizer charges are removed.

### Proposition 2.4: This Is The Exact Jacobian Target

The actual scalar-field admissibility of Paper 36 is equivalent to

$$
\mathrm{P37\text{-}SCAL\text{-}POINTLIFT}
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}JACRANK}(\sigma)
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}SCOREENV}(C_S).
$$

Proof.

Paper 36 requires actual finite vector fields that differentiate the scalar
pair \(m,t\) as coordinate directions and have controlled Ward scores.  The
pointwise lift supplies the actual scalar functions.  The rank condition
supplies a controlled right inverse and therefore the two vector fields
\(Y_m,Y_t\).  The score envelope is exactly the admissibility part needed for
Ward-Stein integration by parts.  Conversely, any actual scalar-field
admissibility package contains actual scalar functions, their derivative
against the lifted fields, and the corresponding score envelope.  `square`

## 3. Try To Build The Controlled Right Inverse

There are three possible ways to build \(R_{act}^{scal}\).  We execute each.

### Route A: Atom-Value Pointwise Lift

The optimistic route is to express \(m^{pt},t^{pt}\) as finite sums of
literal residual atoms and selector factors already present in the adaptive
law.

### Proposition 3.1: Atom-Value Lift Is Not Sourced

The current corpus does not prove the atom-value version of
`P37-SCAL-POINTLIFT`.

Proof.

Papers 23, 26, and 29 identify primitive residual atoms and finite Möbius
rows, but repeatedly distinguish identities from numerical population.
Paper 29 proves that primitive residual atom values are exactly the literal
RPF residual atoms left after retained rows are charged, and that their
defect values remain unsourced.  Therefore the current corpus does not give
finite pointwise formulas for \(m^{pt},t^{pt}\) as actual residual atom sums
with derivative and normalizer control.  `square`

### Route B: Group-Coordinate Pointwise Lift

The second route is to write \(m^{pt},t^{pt}\) directly as smooth functions
of the finite group or chart variables in the adaptive integral.

### Proposition 3.2: Group-Coordinate Lift Is Not Sourced

The current corpus does not prove the group-coordinate version of
`P37-SCAL-POINTLIFT`.

Proof.

The finite adaptive integral has group/chart variables, but no paper prints
the actual residual/signed product

$$
R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}
$$

as a smooth pointwise function of those variables with derivatives,
selector-boundary terms, Jacobian terms, and conditional normalizer
derivatives.  Paper 32 Sections 118 through 129 explicitly close the
configuration-Jacobian route as a current-corpus derivation.  `square`

### Route C: Free Scalar Coordinates

The third apparent route is to append \(m,t\) as coordinates and differentiate
them directly.

### Proposition 3.3: Free Scalar Coordinates Are Not Same-Law Coordinates

Appending \(m,t\) as free coordinates does not prove actual scalar-field
admissibility.

Proof.

If the coordinates are not measurable functions of the actual adaptive
record chart, then Ward-Stein integration by parts is being performed on an
enlarged artificial space.  That violates the same-law discipline.  Formal
coordinates are useful for algebraic diagnosis, but not for actual
admissibility.  `square`

### Route D: Source-Response Substitute

The source-response route does not build \(R_{act}^{scal}\) as a vector field
on configuration variables.  Instead it attempts to move the expectations of
\((m,t)\) by finite same-law source tilts.

### Proposition 3.4: Source Response Is Valid But It Is Not Scalar-Field
Admissibility

The source-response matrix route can replace the need for actual vector
fields only if it supplies its own rank and curvature theorem.  It does not
prove `P37-SCAL-JACRANK`.

Proof.

Source response differentiates

$$
\log\mathbf E^{act}e^{sV}
$$

at \(s=0\).  That is a same-law operation, but it is an expectation-level
operation, not a vector field on \(\Theta_{act}^{N,j,L}\).  Paper 32 names
the corresponding route `P32-SCAL-SRCMAT` and reduces it to source-rank plus
curvature.  Therefore it remains a valid alternative positive route, but it
does not source the actual scalar-field admissibility gate being tested
here.  `square`

### Theorem 3.5: Controlled Right Inverse Is Not Built By The Current Corpus

The current corpus does not build \(R_{act}^{scal}\) in a closing range.

Proof.

Routes A and B do not source `P37-SCAL-POINTLIFT` by Propositions 3.1 and
3.2.  Route C is not same-law by Proposition 3.3.  Route D is a different
same-law source-response route, not an actual configuration right inverse,
by Proposition 3.4.  Hence `P37-SCAL-JACRANK` and
`P37-SCAL-SCOREENV` are not currently reached.  `square`

## 4. If Rank Two Passes: Lifted Ward-Stein Fields

Although the current corpus does not prove the rank package, the conditional
closure is exact and useful.

### Definition 4.1: Lifted Scalar Ward-Stein Fields

Assume

$$
\mathrm{P37\text{-}SCAL\text{-}POINTLIFT}
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}JACRANK}(\sigma)
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}SCOREENV}(C_S).
$$

Define

$$
Y_m:=R_{act}^{scal}e_m,
\qquad
Y_t:=R_{act}^{scal}e_t.
$$

Let \(F_m,F_t\) be the quadratic tests pulled back from Paper 36 through
the actual scalar map \(s_{act}\).

### Lemma 4.2: Lifted Fields Recover The Scalar Coefficients

The lifted fields obey

$$
Y_m F_m=m+o(1),
\qquad
Y_t F_t=t+o(1),
$$

and their scalar-ray coefficients are the Paper-36 coefficients

$$
A_m=h_0+h_A,
\qquad
A_t=a_N(h_0-h_A),
$$

up to the same quotient error.

Proof.

The right inverse gives \(D_\theta s_{act}Y_m=e_m+o(1)\) and
\(D_\theta s_{act}Y_t=e_t+o(1)\).  Pulling back the quadratic Ward tests from
the scalar coordinates gives the displayed derivative identities.  On
\(B(c)=cI_2\), Paper 36 computes the coefficients \(A_m,A_t\).  `square`

### Corollary 4.3: Admissibility Plus Score Defect Closes The Rank-1
Detector

If the package of Definition 4.1 holds and, in addition,
`P36-WS-SCOREDEF(epsilon)` holds in the Paper-36 closing range, then
`P36-NONGAUGE-WS-RAYCUT(A_0,epsilon)` holds.

Proof.

Lemma 4.2 supplies the actual nonzero scalar coefficient.  The score-defect
bound supplies the small right-hand side.  Paper 36, Lemma 2.1, gives the
ray cut.  `square`

## 5. If Rank Fails: Kernel Separator And Floor

### Definition 5.1: Scalar Rank Failure

Write

$$
\mathrm{P37\text{-}SCAL\text{-}RANKFAIL}(\eta)
$$

if every admissible actual scalar Jacobian lift has second singular value
less than \(\eta\), after licensed quotienting and after removing directions
with uncontrolled score cost.

### Definition 5.2: Scalar Kernel Separator

At finite cutoff, a scalar kernel separator is a nonzero vector
\(q=(q_m,q_t)\in\mathbb R^2\) such that

$$
q\cdot G_{act}^{scal}v=0
$$

for all admissible active tangent directions \(v\), while

$$
q\cdot(m,t)
$$

is nonzero on the scalar target direction.

Write

$$
\mathrm{P37\text{-}SCAL\text{-}KERSEP}(q)
$$

for the existence of such a finite separator.

### Lemma 5.3: Rank Failure Gives A Separator Candidate

If `P37-SCAL-RANKFAIL(0)` holds at finite cutoff, then a scalar kernel
separator exists.

Proof.

The active image of \(G_{act}^{scal}\) is a proper subspace of
\(\mathbb R^2\).  Finite-dimensional linear algebra gives a nonzero vector
\(q\) in the orthogonal complement of that image.  If \(q\) also separates
the scalar target direction, it is a kernel separator.  If it does not, then
the scalar target was not the missing direction and the rank failure is
irrelevant to the scalar obstruction.  `square`

### Definition 5.4: Kernel Floor Theorem

Write

$$
\mathrm{P37\text{-}SCAL\text{-}KERFLOOR}(M_*)
$$

if some scalar kernel separator \(q\) yields a sign-coherent same-law bound

$$
s_q\mathbf E\bigl[q_m m+q_t t\bigr]\ge M_*,
$$

with \(s_q\in\{-1,1\}\), and \(M_*\) above the Branch-A floor threshold.

### Proposition 5.5: Separator Alone Is Not A Floor

`P37-SCAL-KERSEP(q)` does not imply
`P37-SCAL-KERFLOOR(M_*)`.

Proof.

The separator is finite linear algebra.  It says which scalar direction is
not reached by admissible tangent fields.  It does not evaluate the actual
same-law expectation of that scalar combination, does not choose its sign,
and does not prove a lower magnitude.  Those are precisely the floor value
data in Definition 5.4.  `square`

### Corollary 5.6: Negative Closure

If `P37-SCAL-KERFLOOR(M_*)` holds in the Branch-A floor range, then adaptive
Branch A is falsified by the scalar floor route.

### Proposition 5.7: The Current Corpus Does Not Prove The Kernel Floor

The current corpus does not prove `P37-SCAL-KERFLOOR(M_*)`.

Proof.

Papers 32 through 36 repeatedly isolate the floor candidates
\(m,t,\lambda_+,\lambda_-\), but no paper prints a sign-coherent lower bound
for any active scalar combination \(q_m m+q_t t\) above the Branch-A floor
threshold.  Finite separation, when available, only supplies a candidate
linear functional.  It does not supply the actual same-law expectation,
sign, or magnitude.  Hence the kernel floor remains a primitive value
theorem.  `square`

## 6. Paper-37 Main Theorem

### Theorem 6.1: Actual Scalar-Field Admissibility Gatekeeper

The five-step attack has the following exact status.

1. The actual scalar map is

   $$
   s_{act}^{N,j,L}(\theta)
   =
   \bigl(m_{\Gamma_1}^{pt}(\theta),
   t_{\Gamma_1}^{pt}(\theta)\bigr),
   $$

   and it exists only after `P37-SCAL-POINTLIFT`.

2. The actual Jacobian target is

   $$
   G_{act}^{scal}=D_\theta s_{act}^{N,j,L}.
   $$

3. A controlled right inverse exists exactly under

   $$
   \mathrm{P37\text{-}SCAL\text{-}JACRANK}(\sigma)
   \quad+\quad
   \mathrm{P37\text{-}SCAL\text{-}SCOREENV}(C_S).
   $$

4. If the pointwise lift, rank, and score-envelope package holds, then the
   lifted fields \(Y_m,Y_t\) exist and reduce Paper 36 to the score-defect
   theorem.

5. If actual rank fails, finite separation gives only a separator candidate.
   Branch-A falsification requires the extra sign-coherent theorem
   `P37-SCAL-KERFLOOR(M_*)`.

6. The current corpus proves none of the positive pointwise-lift, rank,
   score-envelope, or kernel-floor value theorems.

Proof.

Items 1 and 2 are Definitions 1.2, 1.3, and 2.1.  Item 3 is Definitions 2.2
and 2.3.  Item 4 is Lemma 4.2 and Corollary 4.3.  Item 5 is Lemma 5.3 and
Proposition 5.5.  Item 6 is Theorem 3.5 and Proposition 5.7.  `square`

### Corollary 6.2: The Actual Admissibility Route Is Settled At
Current-Corpus Level

Paper 37 does not prove actual scalar-field admissibility.  It proves that
the route is exactly one of:

$$
\boxed{
\mathrm{P37\text{-}SCAL\text{-}POINTLIFT}
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}JACRANK}(\sigma)
\quad+\quad
\mathrm{P37\text{-}SCAL\text{-}SCOREENV}(C_S)
}
$$

followed by the Paper-36 score-defect theorem, or

$$
\boxed{
\mathrm{P37\text{-}SCAL\text{-}KERFLOOR}(M_*)
}.
$$

There is no remaining formal-coordinate shortcut.

### Corollary 6.3: What To Attack Next

The next positive theorem should not try to differentiate formal
\(\beta\)-coordinates again.  The best remaining options are:

1. prove `P37-SCAL-POINTLIFT` by an actual atom-value or group-coordinate
   representation of \(R_{\Gamma_1}\Sigma_{\Gamma_1}\);
2. bypass configuration vector fields by returning to the source-response
   rank and curvature route:

   $$
   \mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}
   \quad+\quad
   \mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM};
   $$

3. attack the residual score-defect theorem directly by the Paper-33
   \(L^2\)/Hessian package;
4. prove the sign-coherent kernel floor.

These are value-bearing same-law inputs.  More finite labels or passive
constraints will not build \(G_{act}^{scal}\).

The rest of this paper executes option 2 inside Paper 37.

## 7. Source-Response Pivot Inside Paper 37

The actual-coordinate route asked for vector fields \(Y_m,Y_t\) on the
finite adaptive chart.  That is very concrete, but Paper 37 Part I shows
that the current corpus does not print the needed pointwise lift.

The source-response route asks a different question.  Instead of moving
hidden coordinates, introduce finite sources inside the same record law and
ask whether the derivatives of the same finite pressure recover \(m,t\).
This stays inside the Barandes rule: a source parameter is a probe of one
finite law, not a new dynamics.

### Definition 7.1: Formal Two-Knob Structural Source

Let

$$
P_I:=I_2,
\qquad
P_U:=U_N.
$$

The formal structural source is

$$
V_{\alpha,\zeta}^{str}
:=
\operatorname{Tr}
\left[
(\alpha P_I+\zeta P_U)
\Pi_+^{U_N}
\left(D_{\Gamma_1}^{HK}R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}\right)
\right].
$$

Using the scalar compression,

$$
\Pi_+^{U_N}
\left(D_{\Gamma_1}^{HK}R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}\right)
=
{m\over2}I_2+{t\over2}U_N,
$$

the formal derivatives at the origin are

$$
\partial_\alpha V_{\alpha,\zeta}^{str}\big|_0=m,
\qquad
\partial_\zeta V_{\alpha,\zeta}^{str}\big|_0=t.
$$

This is still only formal until the expression is realized as a finite
observable of the actual adaptive record law.

### Definition 7.2: Structural Source Coupling

Write

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}COUPLE}(\varepsilon)
$$

if there exist finite actual same-law observables \(V_I,V_U\) such that the
pressure

$$
\Phi_{str}^{N,j}(\alpha,\zeta)
:=
\log\mathbf E_{N,j}^{act}
\exp(\alpha V_I+\zeta V_U)
$$

recovers the scalar pair by

$$
\left|
\partial_\alpha\Phi_{str}^{N,j}(0,0)-m
\right|
+
\left|
\partial_\zeta\Phi_{str}^{N,j}(0,0)-t
\right|
\le\varepsilon
$$

cofinally, with the same endpoint, selector, residual, Jacobian, and
normalizer conventions as the adaptive law.

The word "couple" is important: \(V_I,V_U\) must see the actual
residual/signed product \(R_{\Gamma_1}\Sigma_{\Gamma_1}\), not only the
clean heat diagonal.

### Lemma 7.3: Coupled Structural Sources Recover \(m,t\)

If `P37-STRUCTSRC-COUPLE(epsilon)` holds, then the two scalar responses are
the first derivatives of one finite same-law pressure up to error
\(\varepsilon\).

Proof.

This is exactly Definition 7.2.  The formal normalization in Definition 7.1
is consistent because
\(\operatorname{Tr}(I_2I_2)=2\), \(\operatorname{Tr}(U_N^2)=2\), and
\(\operatorname{Tr}(U_N)=0\), so the factor \(1/2\) in the scalar compression
is canceled by the trace pairing.  `square`

## 8. Structural Gram And Curvature

If the coupling gate passes, the next question is whether the two structural
sources are genuinely two-dimensional under the actual law.

### Definition 8.1: Structural Gram Gate

Assuming `P37-STRUCTSRC-COUPLE(epsilon)`, define

$$
G_{str}^{N,j}
:=
\nabla^2_{\alpha,\zeta}\Phi_{str}^{N,j}(0,0)
=
\operatorname{Cov}_{N,j}^{act}
\left(
\begin{pmatrix}
V_I\\
V_U
\end{pmatrix}
\right).
$$

Write

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}GRAM}(\sigma,M)
$$

if

$$
\det G_{str}^{N,j}\ge\sigma^2>0,
\qquad
\|G_{str}^{N,j}\|_{op}\le M<\infty
$$

cofinally.

### Definition 8.2: Structural Curvature Gate

Write

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}CURV}(\rho,\epsilon)
$$

if, for all \(\|u\|_2\le\rho\), the structural pressure satisfies the
third-order remainder bound

$$
\left\|
\nabla\Phi_{str}(u)-\nabla\Phi_{str}(0)-G_{str}u
\right\|_2
\le\epsilon
$$

after all licensed finite-cutoff and tail debits are charged.

This is the source-response analogue of a controlled score envelope.  Gram
rank tells us the two source directions are independent at first order;
curvature tells us the first-order control is usable at finite cofinal scale.

### Lemma 8.3: Gram Positivity Gives Source Rank

If `P37-STRUCTSRC-COUPLE(epsilon)` and
`P37-STRUCTSRC-GRAM(sigma,M)` hold, then the structural two-knob source
supplies a rank-two scalar source matrix with condition number bounded by
\(\sigma^{-1}\) up to the coupling error.

Proof.

The source columns are the derivatives of
\(\nabla\Phi_{str}\) with respect to \(\alpha,\zeta\).  These columns are the
columns of \(G_{str}\).  The determinant lower bound and operator upper bound
give a controlled right inverse by finite \(2\times2\) linear algebra.
`square`

### Corollary 8.4: Structural Source-Response Positive Route

If

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}COUPLE}(\varepsilon)
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}GRAM}(\sigma,M)
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}CURV}(\rho,\epsilon)
$$

hold in a closing range, then the structural source-response route replaces
the missing actual-coordinate right inverse by a same-law source-rank and
curvature theorem.

Proof.

Coupling identifies \(m,t\) as source-gradient components.  Gram positivity
gives rank two.  Curvature controls the finite-scale error of the source
response.  This is exactly the source-response substitute isolated in Paper
32 and recalled in Proposition 3.4, now specialized to the two structural
knobs.  `square`

## 9. Clean Heat Sources Do Not Couple

The tempting shortcut is to source only the clean heat diagonal or the
recoupling matrix.  That does not reach the actual live object.

### Definition 9.1: Clean Structural Source

A clean structural source changes only \(D_{\Gamma_1}^{HK}\), \(I_2\), or
\(U_N\), while treating the residual/signed product

$$
R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}
$$

as absent from the actual finite observable being differentiated.

### Proposition 9.2: Clean Structural Sources Are Ray-Blind

Clean structural sources do not prove `P37-STRUCTSRC-COUPLE(epsilon)`.

Proof.

The scalar pair is

$$
m=h_0\beta_{00}+h_A\beta_{AA},
$$

and

$$
t=a_N(h_0\beta_{00}-h_A\beta_{AA})
+b_N(h_0\beta_{0A}+h_A\beta_{A0}),
$$

where the entries \(\beta_{ab}\) belong to
\(B_{\Gamma_1}=R_{\Gamma_1}\Sigma_{\Gamma_1}\).  A source that changes only
the clean heat weights or channel labels differentiates the readout
coefficients, not the actual residual/signed product entries.  It therefore
does not bound or orient the scalar amplitude \(c\).  `square`

## 10. Rigidity And Floor

If the structural Gram degenerates, the route is not automatically negative.
Degeneracy is useful only if it forces a sign-coherent scalar floor.

### Definition 10.1: Structural Rigidity/Floor

Write

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}RIGIDFLOOR}(M_*)
$$

if structural Gram degeneracy yields a finite relation

$$
aV_I+bV_U=c_0
$$

whose induced scalar combination satisfies

$$
s\mathbf E[am+bt]\ge M_*
$$

for a fixed sign \(s\in\{-1,1\}\), with \(M_*\) above the Branch-A floor
threshold.

### Lemma 10.2: Gram Degeneracy Alone Is Not A Floor

Failure of `P37-STRUCTSRC-GRAM(sigma,M)` does not imply
`P37-STRUCTSRC-RIGIDFLOOR(M_*)`.

Proof.

A degenerate covariance matrix says that some source combination has small
variance or is rigid in the realized source algebra.  It does not determine
the sign or magnitude of \(am+bt\) under the actual law.  The sign and
magnitude are exactly the additional value data in Definition 10.1.  `square`

## 11. Current-Corpus Structural Source Verdict

### Proposition 11.1: Structural Coupling Is Not Sourced

The current corpus does not prove
`P37-STRUCTSRC-COUPLE(epsilon)` in a closing range.

Proof.

Papers 30 through 37 print the clean heat diagonal, the recoupling matrix,
formal scalar compression, formal block-entry derivatives, and the
source-response dictionary.  They do not print a finite same-law observable
whose derivative couples the clean structural source to the actual
residual/signed product \(R_{\Gamma_1}\Sigma_{\Gamma_1}\).  Papers 26, 29,
32, and 37 identify this product as the missing actual-law value object.
`square`

### Proposition 11.2: Structural Gram And Curvature Are Not Sourced

The current corpus does not prove
`P37-STRUCTSRC-GRAM(sigma,M)` or
`P37-STRUCTSRC-CURV(rho,epsilon)` in a closing range.

Proof.

The Gram and curvature gates are defined for the realized observables
\(V_I,V_U\).  Since structural coupling is not printed, the realized
observables are not available with the required normalization.  Even if they
were available, the corpus does not print their covariance determinant,
operator bound, or third-order source-pressure remainder.  `square`

### Proposition 11.3: Structural Rigidity/Floor Is Not Sourced

The current corpus does not prove
`P37-STRUCTSRC-RIGIDFLOOR(M_*)`.

Proof.

No paper prints a structural Gram null relation together with a sign-coherent
lower bound for the induced scalar combination \(am+bt\).  Lemma 10.2 shows
that Gram degeneracy alone would not be enough.  `square`

### Theorem 11.4: Structural Source-Response Route Is Fully Reduced

The structural source-response route is valid and same-law in the following
conditional form:

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}COUPLE}
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}GRAM}
\quad+\quad
\mathrm{P37\text{-}STRUCTSRC\text{-}CURV}
$$

is the positive route, while

$$
\mathrm{P37\text{-}STRUCTSRC\text{-}RIGIDFLOOR}
$$

is the negative route.  The current corpus proves none of these primitive
inputs.

Proof.

The positive implication is Corollary 8.4.  The clean shortcut is eliminated
by Proposition 9.2.  The negative route is Definition 10.1 and Lemma 10.2.
The current-corpus audit is Propositions 11.1 through 11.3.  `square`

### Corollary 11.5: What Remains After Both Parts Of Paper 37

After the actual-coordinate and structural source-response passes, the live
Branch-A scalar route is reduced to one of four genuinely new same-law value
inputs:

1. actual scalar pointwise lift plus Jacobian rank plus score envelope;
2. structural coupling plus Gram plus source curvature;
3. residual score-defect control by the Paper-33 \(L^2\)/Hessian package;
4. sign-coherent scalar floor, either kernel or structural.

None is a passive label, formal coordinate, clean heat identity, or pure
source dictionary statement.

## 12. Plain Verdict

The formal scalar derivative exists.  The actual scalar vector field is not
yet sourced.

The structural source-response route is valid, but it is not sourced either.
It will work only if the two knobs couple to the actual residual/signed
product \(R\Sigma\), produce a nondegenerate Gram matrix, and have controlled
source curvature.

That is the whole lesson of Paper 37.  The scalar ray is not surviving
because we failed to write down the right \(2\times4\) matrix.  It is
surviving because the program still lacks a theorem saying that the actual
adaptive pushed-forward record law has either two controllable scalar
directions inside \(R\Sigma\), or two realized source-response knobs coupled
to \(R\Sigma\), or a sign-coherent scalar floor.

This is the right next obstruction.  It is small, finite, Barandes-aligned,
and honest.
